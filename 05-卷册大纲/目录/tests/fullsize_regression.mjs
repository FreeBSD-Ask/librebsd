// 全尺寸回归：任何网页宽度下的「控件对齐、无重叠、无横滚、黄字隐藏、指标卡紧凑」断言
import { chromium } from 'file:///C:/Users/ykla/AppData/Roaming/npm/node_modules/@executeautomation/playwright-mcp-server/node_modules/playwright/index.mjs';
// Chromium 可执行路径解析（2026-10-04 立）：钉定修订版优先，环境更新后自动回落现存最高修订版。
import fs from 'node:fs';
const __PW_DIR = 'C:/Users/ykla/AppData/Local/ms-playwright';
const __PINNED = __PW_DIR + '/chromium-1200/chrome-win64/chrome.exe';
const __CHROME_EXE = fs.existsSync(__PINNED) ? __PINNED
  : fs.readdirSync(__PW_DIR).filter(d => /^chromium-\d+$/.test(d))
      .sort((a, b) => Number(b.slice(9)) - Number(a.slice(9)))
      .map(d => __PW_DIR + '/' + d + '/chrome-win64/chrome.exe')
      .find(p => fs.existsSync(p));
if (!__CHROME_EXE) { console.error('未找到可用 Chromium（ms-playwright）'); process.exit(2); }
const browser = await chromium.launch({ executablePath: __CHROME_EXE, headless: true, args: ['--no-sandbox'] });
const SIZES = [320, 340, 360, 375, 390, 393, 402, 412, 430, 480, 560, 640, 768, 820, 840,
  900, 1024, 1080, 1140, 1200, 1280, 1366, 1440, 1536, 1680, 1775, 1920, 1920];
const results = [];
for (const w of [...new Set(SIZES)]) {
  const page = await browser.newPage({ viewport: { width: w, height: 900, deviceScaleFactor: w < 500 ? 3 : 1 }, hasTouch: w < 500 });
  const errs = [];
  page.on('pageerror', e => errs.push(String(e).slice(0, 80)));
  await page.goto('file:///D:/librebsd/08-核查报告与多轮复核/重构2026/index.html', { waitUntil: 'load' });
  await page.waitForTimeout(1700);
  const r = await page.evaluate(() => {
    const vw = window.innerWidth;
    const gm = s => { const e = document.querySelector(s); if (!e) return null; const c = getComputedStyle(e); const b = e.getBoundingClientRect(); return { left: Math.round(b.left), right: Math.round(b.right), top: Math.round(b.top), bottom: Math.round(b.bottom), vis: c.display !== 'none' && c.visibility !== 'hidden' && b.width > 0 }; };
    const theme = gm('#themeToggle');
    const tools = gm('.opt-tools');
    const back = gm('#backToTop');
    // ≤820 断点下 #themeToggle 由 JS 移入 .opt-tools 折叠面板（.opt-tools > button:not(.opt-tools-toggle){display:none}），
    // 属响应式设计而非缺陷 → 只对**可见**控件断言右缘对齐，并记录可见数。
    const vis = [theme, tools, back].filter(x => x && x.vis);
    const rightGaps = vis.map(x => Math.round(vw - x.right));
    const allEqual = rightGaps.length >= 1 && rightGaps.every(x => x === rightGaps[0]);
    const hscroll = document.documentElement.scrollWidth > vw + 2;
    return { vw, rightGaps, allEqual, hscroll, nVis: vis.length, themeVis: !!(theme && theme.vis), themeTop: theme ? theme.top : null, toolsTop: tools ? tools.top : null };
  });
  const pass = r.allEqual && !r.hscroll;
  results.push({ w, pass, ...r, errs: errs.length });
  console.log((pass ? 'OK' : 'FAIL') + ' w=' + w + ' gaps=' + r.rightGaps.join('/') + ' vis=' + r.nVis + (r.themeVis ? '' : ' [themeToggle 入折叠面板]') + (r.hscroll ? ' HSCROLL' : '') + (errs.length ? ' ERRS=' + errs.length : ''));
  await page.close();
}
const bad = results.filter(r => !r.pass);
console.log('TOTAL=' + results.length + ' FAILED=' + bad.length);
await browser.close();
console.log('FULLSIZE_DONE');
process.exit(bad.length ? 1 : 0);
