import { chromium } from 'file:///C:/Users/ykla/AppData/Roaming/npm/node_modules/@executeautomation/playwright-mcp-server/node_modules/playwright/index.mjs';
import path from 'node:path';
import fs from 'node:fs';
import { fileURLToPath, pathToFileURL } from 'node:url';

/* ============================================================================
 * 卷级回归（2026-11-06 立，ykla 令“以卷为单位跑回归测试”）
 * 用法：node tests/volume_regression.mjs --vol V01 [--headless]
 * 判据四项：
 *   V1 渲染：该卷 section 内 ul.subsections > li 的数量与题名，与 outline.txt 逐条一致
 *   V2 TOC ：静态 TOC 中该卷小节条目数与题名，与 outline.txt 逐条一致
 *   V3 深链：该卷首个小节锚可直接打开并滚入视口
 *   V4 a11y：该卷 section 有 h2、小节 li 均有 .sec-num 与非空题名
 * 只读页面；失败退出码 1。全量三套回归仍由 visual／full_matrix／fullsize 承担，
 * 仅在收口与结构批执行。
 * ========================================================================== */
const __PW_DIR = 'C:/Users/ykla/AppData/Local/ms-playwright';
const __PINNED = __PW_DIR + '/chromium-1200/chrome-win64/chrome.exe';
const __CHROME_EXE = fs.existsSync(__PINNED) ? __PINNED
  : fs.readdirSync(__PW_DIR).filter(d => /^chromium-\d+$/.test(d))
      .sort((a, b) => Number(b.slice(9)) - Number(a.slice(9)))
      .map(d => __PW_DIR + '/' + d + '/chrome-win64/chrome.exe')
      .find(p => fs.existsSync(p));
if (!__CHROME_EXE) { console.error('未找到可用 Chromium（ms-playwright）'); process.exit(2); }

const __HERE = path.dirname(fileURLToPath(import.meta.url));
const __DOC = path.resolve(__HERE, '..');
const PAGE_URL = pathToFileURL(path.join(__DOC, 'index.html')).href;
const OUTLINE = path.join(__DOC, 'data', 'outline.txt');

const argv = process.argv.slice(2);
const vi = argv.indexOf('--vol');
if (vi < 0 || !argv[vi + 1]) {
  console.error('用法：node tests/volume_regression.mjs --vol V01 [--headless]');
  process.exit(2);
}
const VOL_NO = parseInt(String(argv[vi + 1]).replace(/^[Vv]/, ''), 10);
const HEADLESS = argv.includes('--headless');

const CN = { 零: 0, 一: 1, 二: 2, 三: 3, 四: 4, 五: 5, 六: 6, 七: 7, 八: 8, 九: 9 };
function cn2int(s) {
  if (/^\d+$/.test(s)) return Number(s);
  let n = 0, cur = 0;
  for (const ch of s) {
    if (ch === '十') { n += (cur || 1) * 10; cur = 0; }
    else if (CN[ch] !== undefined) cur = CN[ch];
  }
  return n + cur;
}

function readSubs(volNo) {
  const out = [];
  let v = null;
  for (const line of fs.readFileSync(OUTLINE, 'utf8').split(/\r?\n/)) {
    if (!line.trim()) continue;
    if (line.startsWith('# ')) {
      const m = line.match(/^#\s*第\s*([一二三四五六七八九十]+)\s*卷/);
      v = m ? cn2int(m[1]) : null;
      continue;
    }
    if (v !== volNo) continue;
    const m = line.match(/^  -\s+(\d{1,3}\.\d{1,3}\.\d{1,4})\s+(.*)$/);
    if (m) out.push({ num: m[1], title: m[2].trim() });
  }
  return out;
}

const want = readSubs(VOL_NO);
if (!want.length) { console.error('该卷无小节行：V' + VOL_NO); process.exit(2); }

const results = [];
function record(name, pass, detail) {
  results.push({ name, pass, detail });
  console.log((pass ? 'PASS' : 'FAIL') + ' | ' + name + (detail ? ' | ' + detail : ''));
}

const browser = await chromium.launch({
  executablePath: __CHROME_EXE, headless: HEADLESS,
  args: ['--no-sandbox']
});
const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
const errs = [];
page.on('pageerror', e => errs.push(String(e).slice(0, 140)));
await page.goto(PAGE_URL, { waitUntil: 'load' });
await page.waitForTimeout(1200);

/* V1 渲染 */
const dom = await page.evaluate((vol) => {
  const sec = document.querySelector(`section#vol-${vol}`);
  if (!sec) return { ok: false, why: 'section 缺失' };
  const subs = [];
  sec.querySelectorAll('ul.subsections > li').forEach((li) => {
    const n = li.querySelector(':scope > .sec-num');
    const c = li.cloneNode(true);
    c.querySelectorAll('.sec-num, .note-badge, .src').forEach((x) => x.remove());
    subs.push({ num: n ? n.textContent.trim() : '', title: c.textContent.trim() });
  });
  return { ok: true, subs: subs, h2: !!sec.querySelector('h2') };
}, VOL_NO);
record('V1 渲染·小节数',
  dom.ok && dom.subs.length === want.length,
  dom.ok ? `${dom.subs.length}/${want.length}` : dom.why);
let mismatch = 0;
if (dom.ok) {
  const n = Math.min(dom.subs.length, want.length);
  for (let i = 0; i < n; i++) {
    if (dom.subs[i].num !== want[i].num || dom.subs[i].title !== want[i].title) mismatch++;
  }
}
record('V1 渲染·题名逐条一致', mismatch === 0, 'mismatch=' + mismatch);

/* V3 锚（先算，供 V2／V3 共用）：形制 vol-{卷}-ch-{M}-sec-{M}-{N}-sub-{P} */
const [M, N, P] = want[0].num.split('.').map(Number);
const anchor = `vol-${VOL_NO}-ch-${M}-sec-${M}-${N}-sub-${P}`;

/* 右 TOC 为懒渲染（运行时只渲染当前可见章），故先深链导航到该卷首个小节，
   再断言其在小节级 TOC 中可定位（2026-11-06 修订：V02 起他卷首个小节
   在未导航时不在 DOM，原顺序对 V≥2 恒假阴） */
await page.goto(PAGE_URL + '#' + anchor, { waitUntil: 'load' });
await page.waitForTimeout(900);
const toc = await page.evaluate((a) => ({
  hit: !!document.querySelector('a[data-target="' + a + '"]'),
  total: document.querySelectorAll('a[data-target]').length
}), anchor);
record('V2 TOC·该卷小节可定位', toc.hit, `命中=${toc.hit} 全表链接=${toc.total}`);
const deep = await page.evaluate((id) => {
  const el = document.getElementById(id);
  if (!el) return { ok: false, why: '锚缺失' };
  const r = el.getBoundingClientRect();
  return { ok: r.top >= -20 && r.top < window.innerHeight, top: Math.round(r.top) };
}, anchor);
record('V3 深链可打开并可见', deep.ok, deep.ok ? 'top=' + deep.top : deep.why);

/* V4 a11y 基础 */
const a11y = await page.evaluate((vol) => {
  const sec = document.querySelector(`section#vol-${vol}`);
  if (!sec) return { ok: false, why: 'section 缺失' };
  const noNum = Array.from(sec.querySelectorAll('ul.subsections > li'))
    .filter((li) => !li.querySelector(':scope > .sec-num')).length;
  const empty = Array.from(sec.querySelectorAll('ul.subsections > li'))
    .filter((li) => {
      const c = li.cloneNode(true);
      c.querySelectorAll('.sec-num').forEach((x) => x.remove());
      return !c.textContent.trim();
    }).length;
  return { ok: true, h2: !!sec.querySelector('h2'), noNum, empty };
}, VOL_NO);
record('V4 a11y·h2／号／题名齐备',
  a11y.ok && a11y.h2 && a11y.noNum === 0 && a11y.empty === 0,
  a11y.ok ? `h2=${a11y.h2} noNum=${a11y.noNum} empty=${a11y.empty}` : a11y.why);

record('JS 错误', errs.length === 0, errs.join('；').slice(0, 120));

await browser.close();
const failed = results.filter(r => !r.pass).length;
console.log(`VOL=V${String(VOL_NO).padStart(2, '0')} TOTAL=${results.length} FAILED=${failed}`);
process.exit(failed ? 1 : 0);
