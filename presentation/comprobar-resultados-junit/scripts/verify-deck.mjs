import { chromium } from 'playwright-chromium';
const browser=await chromium.launch({headless:true});
try {
const page=await browser.newPage({viewport:{width:1280,height:720}});
await page.goto('http://localhost:3032/');await page.waitForFunction(()=>!!window.__slidev__?.nav);
for(let n=1;n<=10;n++){
await page.goto(`http://localhost:3032/${n}?clicks=20`);const s=page.locator(`#slide-content [data-slidev-no="${n}"]`);await s.locator('h1').waitFor();await page.waitForTimeout(400);
const bad=await s.evaluate(s=>({overflow:s.scrollHeight>s.clientHeight+5,raw:s.textContent.includes('```')}));if(bad.overflow||bad.raw)throw Error(JSON.stringify({slide:n,...bad}));console.log('Slide',n,'OK');}
await page.goto('http://localhost:3032/7');await page.waitForFunction(()=>document.querySelector('#slide-content [data-recording="assertion-red"]')?.dataset.playing==='true');await page.waitForFunction(()=>document.querySelector('#slide-content [data-recording="assertion-red"]')?.dataset.completed==='true');console.log('Autoplay and completion OK');
} finally {await browser.close();}
