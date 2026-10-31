import fs from 'node:fs/promises';
import path from 'node:path';
import {createRequire} from 'node:module';
import {pathToFileURL} from 'node:url';
const require=createRequire(path.resolve('package.json'));
const {chromium}=require('playwright-chromium');
const {parseSync}=await import(pathToFileURL(require.resolve('@slidev/parser')));
const raw=await fs.readFile('slides.md','utf8');
const baseUrl=process.env.SLIDEV_URL || 'http://localhost:3030';
const deck=parseSync(raw);
const expectedDiagrams=(raw.match(/^```mermaid/gm)||[]).length;
const cover=deck.slides[0].content.replace(/<!--[\s\S]*?-->/g,'').trim();
if(!/^# [^\n]+$/.test(cover)) throw new Error('La portada debe contener solo un título, sin subtítulo ni etiquetas.');
if(/class="eyebrow"/.test(raw)||/\d+\s*(?:–\s*\d+\s*)?minutos?\b/i.test(raw)) throw new Error('El deck no debe mostrar antetítulos ni estimaciones de tiempo.');
const normalize=text=>text.replace(/<[^>]*>/g,'').replace(/\s/g,'');
const missing=deck.slides.map((s,i)=>!s.note?.trim()?i+1:null).filter(Boolean);
if(missing.length) throw new Error(`Faltan notas: ${missing}`);
await fs.mkdir('.validation',{recursive:true});
const browser=await chromium.launch({headless:true});
const page=await browser.newPage({viewport:{width:1600,height:900},deviceScaleFactor:1});
await page.addInitScript(()=>{
  localStorage.setItem('slidev-wake-lock','false');
  window.requestAnimationFrame=callback=>window.setTimeout(()=>callback(performance.now()),16);
  window.cancelAnimationFrame=id=>window.clearTimeout(id);
});
const errors=[];
const external=[];
page.on('pageerror',e=>errors.push(e.message));
page.on('request',r=>{if(/^https?:/.test(r.url())&&!r.url().startsWith(baseUrl))external.push(r.url())});
await page.goto(`${baseUrl}/1`,{waitUntil:'networkidle'});
await page.waitForFunction(()=>!!window.__slidev__?.nav);
const results=[];
for(let n=1;n<=deck.slides.length;n++){
  await page.goto(`${baseUrl}/${n}?clicks=999`,{waitUntil:'networkidle'});
  await page.waitForTimeout(800);
  const clicks=await page.evaluate(()=>window.__slidev__.nav.clicksTotal);
  const info=await page.evaluate(no=>{
    const canvas=document.querySelector('#slide-content');
    const root=canvas.querySelector(`[data-slidev-no="${no}"]`);
    if(!root) throw new Error(`No se renderizó la diapositiva ${no}`);
    const bounds=canvas.getBoundingClientRect();
    const over=[];
    for(const el of root.querySelectorAll('h1,h2,h3,p,pre,table,img,.card,.terminal,.formula,.diagram')){
      const style=getComputedStyle(el);
      if(style.visibility==='hidden'||Number(style.opacity)===0||el.closest('.slidev-vclick-hidden'))continue;
      const box=el.getBoundingClientRect();
      if(!box.width||!box.height)continue;
      if(box.bottom>bounds.bottom+2||box.right>bounds.right+2||box.left<bounds.left-2||box.top<bounds.top-2)
        over.push({element:el.tagName,text:el.textContent.slice(0,90),bottom:Math.round(box.bottom-bounds.bottom),right:Math.round(box.right-bounds.right)});
      if(el.tagName==='PRE'&&el.scrollWidth>el.clientWidth+3)
        over.push({element:'PRE horizontal overflow',extra:el.scrollWidth-el.clientWidth});
    }
    return {title:root.querySelector('h1')?.textContent,overflow:over,diagrams:[...root.querySelectorAll('.mermaid')].filter(el=>el.shadowRoot?.querySelector('svg')).length,captures:[...root.querySelectorAll('img.terminal-capture')].map(img=>({loaded:img.complete&&img.naturalWidth>0,src:img.getAttribute('src')})),codeSpans:root.querySelectorAll('pre span').length,magic:root.querySelectorAll('[class*="shiki-magic-move"]').length};
  },n);
  const expectedTitle=deck.slides[n-1].content.match(/^# (.+)$/m)?.[1];
  if(!expectedTitle||normalize(info.title||'')!==normalize(expectedTitle)) throw new Error(`Título desactualizado en diapositiva ${n}: ${info.title}`);
  console.log(`Revisada diapositiva ${n}: ${info.title}`);
  results.push({slide:n,clicks,...info});
}
await fs.writeFile('.validation/report.json',JSON.stringify({slides:deck.slides.length,missingNotes:missing,errors,external,results},null,2));
await browser.close();
console.log(JSON.stringify({slides:results.length,notes:deck.slides.length-missing.length,errors,external:[...new Set(external)],overflow:results.filter(x=>x.overflow.length),diagrams:results.reduce((s,x)=>s+x.diagrams,0),magicSlides:results.filter(x=>x.magic>0).map(x=>x.slide)},null,2));
if(results.some(x=>x.captures.some(img=>!img.loaded))||errors.length||external.length||results.some(x=>x.overflow.length)||results.reduce((sum,x)=>sum+x.diagrams,0)!==expectedDiagrams||!results.some(x=>x.magic>0))process.exitCode=1;
