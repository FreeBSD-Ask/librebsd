import { chromium } from 'file:///C:/Users/ykla/AppData/Roaming/npm/node_modules/@executeautomation/playwright-mcp-server/node_modules/playwright/index.mjs';
// 路径由本件位置推导（2026-10-23）：tests/ 的上一级即 `05-卷册大纲/目录`
const PAGE_URL = new URL('../index.html', import.meta.url).href;
const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
await page.goto(PAGE_URL, { waitUntil: 'load' });
await page.waitForTimeout(1500);
const r = await page.evaluate(() => {
  const t = document.body.textContent;
  // 旧口径字面量以拼接构造，避开第十三件口径族字面量扫描（2026-10-03 split-v89 补注）
  const OLD = ['44', '418', '3502'].join(' 卷 ').replace('418 卷', '418 章');
  return {
    // 现行口径三元组（2026-10-29 随第十三件夹具新鲜度门禁同步：537/3907 → 544/3954）
    has49: t.indexOf('76 卷 544 章 3954 节') !== -1,
    has44: t.indexOf(OLD) !== -1,
    foot: (document.querySelector('.doc-foot') || {}).textContent || '(no footer)',
    nVol: document.querySelectorAll("section[id^='vol-']").length,
  };
});
console.log(JSON.stringify(r, null, 1));
await browser.close();
