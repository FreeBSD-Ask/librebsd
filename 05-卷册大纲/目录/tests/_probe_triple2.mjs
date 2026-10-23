import { chromium } from 'file:///C:/Users/ykla/AppData/Roaming/npm/node_modules/@executeautomation/playwright-mcp-server/node_modules/playwright/index.mjs';
const URL = 'file:///D:/librebsd/08-核查报告与多轮复核/重构2026/index.html';
const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 412, height: 915 } });
await page.emulateMedia({ colorScheme: 'dark' });
await page.goto(URL, { waitUntil: 'load' });
await page.waitForTimeout(1200);
const r = await page.evaluate(() => {
  const dp = document.querySelector('.doc-page');
  if (dp) dp.style.zoom = 0.85;
  const t = document.body.textContent;
  return {
    has49: t.indexOf('75 卷 523 章 3705 节') !== -1,
    hasNote: t.indexOf('注 1713') !== -1,
    self: /目录自校验 6\/6 通过/.test(t),
    foot: (document.querySelector('.doc-foot') || {}).textContent || '(no footer)',
  };
});
console.log(JSON.stringify(r));
await browser.close();
