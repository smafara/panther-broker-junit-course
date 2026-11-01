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
page.setDefaultTimeout(20000);
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
    for(const group of root.querySelectorAll('.split.equal,.trio')) {
      const cards=[...group.children].filter(el=>el.classList.contains('card'));
      if(cards.length<2)continue;
      const boxes=cards.map(el=>el.getBoundingClientRect());
      if(boxes.some(box=>Math.abs(box.width-boxes[0].width)>1||Math.abs(box.height-boxes[0].height)>1))
        over.push({element:'tarjetas desiguales',sizes:boxes.map(box=>[Math.round(box.width),Math.round(box.height)])});
    }
    for(const el of root.querySelectorAll('h1,h2,h3,p,pre,table,img,.card,.terminal,.formula,.diagram,.terminal-recording')){
      if(el.closest('.ap-player'))continue;
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
const recordingChecks=[];
const recordingSlides=deck.slides.flatMap((slide,index)=>slide.content.includes('<TerminalRecording ') ? [index+1] : []);
for(const n of recordingSlides){
  await page.goto(`${baseUrl}/${n}?clicks=999`,{waitUntil:'networkidle'});
  const root=page.locator(`#slide-content [data-slidev-no="${n}"]`);
  const terminal=root.locator('.terminal-recording');
  const name=await terminal.getAttribute('data-recording');
  await terminal.locator('.ap-term-text').waitFor();
  const response=await page.request.get(`${baseUrl}/terminal/${name}.cast`);
  if(!response.ok())throw new Error(`No se cargó ${name}`);
  const rows=(await response.text()).trim().split('\n').map(line=>JSON.parse(line));
  if(rows[0].version!==2||rows.length<3)throw new Error(`Grabación inválida: ${name}`);
  if(rows.slice(1).some(row=>/Salida:|echo ["']?Salida/.test(row[2])))throw new Error(`La grabación aún muestra el código de salida: ${name}`);
  const palette=await terminal.locator('.ap-player').evaluate(el=>getComputedStyle(el).getPropertyValue('--term-color-background').trim());
  if(palette!=='#0b1220')throw new Error(`El terminal no usa la paleta de la presentación: ${name}`);
  const grid=await terminal.locator('.ap-term-text').evaluate(pre=>{
    const row=pre.querySelector('.ap-line');
    return {lineHeight:parseFloat(getComputedStyle(pre).lineHeight),rowHeight:parseFloat(getComputedStyle(row).height)};
  });
  if(grid.lineHeight>grid.rowHeight+.5)throw new Error(`Texto recortado en ${name}: ${JSON.stringify(grid)}`);
  if(await terminal.locator('.ap-control-bar:visible,.ap-overlay-start:visible').count())throw new Error(`Controles visibles: ${name}`);
  if(await terminal.getAttribute('data-speed')!=='0.5')throw new Error(`Velocidad incorrecta: ${name}`);
  await page.waitForFunction(name=>document.querySelector(`#slide-content .terminal-recording[data-recording="${name}"]`)?.dataset.playing==='true',name);
  if(await terminal.locator('.test-result:not(.pending)').count())throw new Error(`Resultados revelados antes de terminar: ${name}`);
  const before=await terminal.locator('.ap-term-text').textContent();
  await page.waitForTimeout(1700);
  const after=await terminal.locator('.ap-term-text').textContent();
  if(before===after)throw new Error(`No avanzó la reproducción automática: ${name}`);
  await terminal.locator('.recording-toggle').click();
  await terminal.locator('.recording-toggle[aria-label="Reproducir ejecución"]').waitFor();
  await terminal.locator('.recording-toggle').click();
  await terminal.locator('.recording-toggle[aria-label="Pausar ejecución"]').waitFor();
  if(name.startsWith('tests-')){
    await page.waitForFunction(name=>{
      const root=document.querySelector(`#slide-content .terminal-recording[data-recording="${name}"]`);
      return root?.dataset.completed==='true'&&!root.querySelector('.test-result.pending');
    },name);
    const statuses=await terminal.locator('.test-result').evaluateAll(rows=>rows.map(row=>({name:row.dataset.testName,status:row.dataset.status})));
    const expected=name==='tests-original-green'?['passed','passed']:name==='tests-fractional-red'?['passed','passed','failed']:['passed','passed','passed'];
    if(JSON.stringify(statuses.map(test=>test.status))!==JSON.stringify(expected))throw new Error(`Resultados inesperados: ${JSON.stringify(statuses)}`);
    console.log(`Panel ${name}: ${expected.join(', ')}`);
    await terminal.locator('.recording-toggle').click();
    await terminal.locator('.recording-toggle[aria-label="Pausar ejecución"]').waitFor();
    if(await terminal.locator('.test-result:not(.pending)').count())throw new Error(`Repetición sin reiniciar resultados: ${name}`);
  }
  await page.evaluate(()=>window.__slidev__.nav.nextSlide());
  await page.waitForTimeout(200);
  if(await terminal.getAttribute('data-playing')==='true')
    throw new Error(`La grabación sigue reproduciéndose fuera de su diapositiva: ${name}`);
  recordingChecks.push({slide:n,name,events:rows.length-1,playback:true,pause:true});
}
const redSlide=deck.slides.findIndex(slide=>slide.content.includes('name="tests-fractional-red"'))+1;
await page.goto(`${baseUrl}/${redSlide}?clicks=3`,{waitUntil:'networkidle'});
const gated=page.locator(`#slide-content [data-slidev-no="${redSlide}"] .terminal-recording`);
if(await gated.getAttribute('data-playing')==='true')throw new Error('La ejecución roja comenzó antes de revelar el terminal.');
await page.goto(`${baseUrl}/print?print=true`,{waitUntil:'networkidle'});
await page.waitForTimeout(1000);
const fallback=page.locator('.terminal-recording img.terminal-capture');
if(await fallback.count()!==recordingSlides.length)throw new Error('La exportación necesita una imagen estática por grabación.');
if(!await fallback.evaluateAll(images=>images.every(img=>img.complete&&img.naturalWidth>0)))
  throw new Error('No se cargaron las imágenes de exportación.');
console.log('Grabaciones verificadas:',JSON.stringify(recordingChecks));
await fs.writeFile('.validation/report.json',JSON.stringify({slides:deck.slides.length,missingNotes:missing,errors,external,recordingChecks,staticFallbackImages:recordingSlides.length,results},null,2));
await browser.close();
console.log(JSON.stringify({slides:results.length,notes:deck.slides.length-missing.length,errors,external:[...new Set(external)],overflow:results.filter(x=>x.overflow.length),diagrams:results.reduce((s,x)=>s+x.diagrams,0),magicSlides:results.filter(x=>x.magic>0).map(x=>x.slide)},null,2));
if(results.some(x=>x.captures.some(img=>!img.loaded))||errors.length||external.length||results.some(x=>x.overflow.length)||results.reduce((sum,x)=>sum+x.diagrams,0)!==expectedDiagrams||!results.some(x=>x.magic>0))process.exitCode=1;
