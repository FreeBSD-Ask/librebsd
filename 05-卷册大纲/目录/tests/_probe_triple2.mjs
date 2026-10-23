import { chromium } from 'file:///C:/Users/ykla/AppData/Roaming/npm/node_modules/@executeautomation/playwright-mcp-server/node_modules/playwright/index.mjs';
// 路径由本件位置推导（2026-10-23）：tests/ 的上一级即 `05-卷册大纲/目录`
const PAGE_URL = new URL('../index.html', import.meta.url).href;
const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 412, height: 915 } });
await page.emulateMedia({ colorScheme: 'dark' });
await page.goto(PAGE_URL, { waitUntil: 'load' });
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
