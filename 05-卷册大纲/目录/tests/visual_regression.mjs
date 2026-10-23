import { chromium } from 'file:///C:/Users/ykla/AppData/Roaming/npm/node_modules/@executeautomation/playwright-mcp-server/node_modules/playwright/index.mjs';
import http from 'node:http';
import path from 'node:path';
// Chromium 可执行路径解析（2026-10-04 立）：钉定修订版优先，环境更新后自动回落现存最高修订版。
const __PW_DIR = 'C:/Users/ykla/AppData/Local/ms-playwright';
const __PINNED = __PW_DIR + '/chromium-1200/chrome-win64/chrome.exe';
const __CHROME_EXE = fs.existsSync(__PINNED) ? __PINNED
  : fs.readdirSync(__PW_DIR).filter(d => /^chromium-\d+$/.test(d))
      .sort((a, b) => Number(b.slice(9)) - Number(a.slice(9)))
      .map(d => __PW_DIR + '/' + d + '/chrome-win64/chrome.exe')
      .find(p => fs.existsSync(p));
if (!__CHROME_EXE) { console.error('未找到可用 Chromium（ms-playwright）'); process.exit(2); }
import fs from 'node:fs';

/* ============================================================================
 * 重构2026 目录页视觉回归套件（2026-09-11 固化，期三）
 * 用法：node tests/visual_regression.mjs
 * 环境：需本机 playwright（借道 @executeautomation/playwright-mcp-server 树内安装）
 *       与 ms-playwright chromium-1200；无头/有头由下方 HEADLESS 开关控制。
 * 断言：17 项视觉几何 + 功能断言（TOC 跟随可见性、浮层、折叠、图谱、进度条、
 *       键盘、抽屉、SUMMARY 导出）。失败退出码 1，供 CI/本地“改后必跑”使用。
 * ========================================================================== */
const URL = 'file:///D:/librebsd/05-卷册大纲/目录/index.html';
const SHOT = 'D:/librebsd/script/_staging/polsplit/';
const HEADLESS = process.argv.includes('--headless');   // 默认有头；--headless 用于静默回归
const browser = await chromium.launch({
  executablePath: __CHROME_EXE,
  headless: HEADLESS, args: ['--no-sandbox', '--start-maximized']
});

const results = [];
function record(name, pass, detail) {
  results.push({ name, pass, detail });
  console.log((pass ? 'PASS' : 'FAIL') + ' | ' + name + (detail ? ' | ' + detail.slice(0, 160) : ''));
}

/* ---------------------------------------------------------------------------
 * 导出保真基准（2026-09-20 立）
 * 真值取**内容源** data/outline.txt（装配产物 index.html 的上游），不取页面 DOM——
 * 页面 DOM 是运行时装饰（计数徽标/溯源注徽标/长节名折叠）的宿主，即被测对象，自证无效。
 * ------------------------------------------------------------------------- */
const OUTLINE_PATH = 'D:/librebsd/05-卷册大纲/目录/data/outline.txt';
/* HTML 本体导出比对基准（T20，2026-10-14）：磁盘装配产物 index.html。 */
const INDEX_PATH = 'D:/librebsd/05-卷册大纲/目录/index.html';
/* 语言标记剥离（2026-10-12，136 批）：内容源 ⟦lang:文本⟧ 于装配期被 esc() 消费，
   DOM 导出为纯文本「文本」；本夹具基准自内容源直读，须同口径剥离，否则 T13/T17
   题面比对恒失败（README 夹具同步纪律⑥「改语法时须同步该常量」）。 */
const LANG_RE = /\u27E6[a-z]{2,3}(?:-[A-Za-z0-9]{2,8})*:([^\u27E6\u27E7]+)\u27E7/g;
const stripLang = s => s.replace(LANG_RE, '$1');
function readOutlineTitles() {
  var volSec = {}, chSec = {};
  const vols = [], chapters = [], sections = [];
  for (const line of fs.readFileSync(OUTLINE_PATH, 'utf8').split(/\r?\n/)) {
    if (!line.trim()) continue;
    if (line.startsWith('# ')) { vols.push(stripLang(line.slice(2).trim())); continue; }
    if (line.startsWith('## ')) { chapters.push(stripLang(line.slice(3).trim())); continue; }
    if (line.startsWith('- ')) {
      const m = line.slice(2).trim().match(/^(\S+)\s+([\s\S]*)$/);
      let num = m ? m[1] : '', body = m ? m[2] : '';
      if (body.startsWith('@@')) { const e = body.indexOf('@@', 2); body = body.slice(e + 2); }
      else if (body.includes('@@')) { body = body.slice(0, body.indexOf('@@')); }
      sections.push(num + ' ' + stripLang(body).trim());
      var _v = vols[vols.length - 1] || '', _c = chapters[chapters.length - 1] || '';
      volSec[_v] = (volSec[_v] || 0) + 1;
      chSec[_v + String.fromCharCode(1) + _c] = (chSec[_v + String.fromCharCode(1) + _c] || 0) + 1;
    }
  }
  /* 附加：按卷/章的节数归组（供 T17 校验 CSV 的卷/章归属） */
  return { vols, chapters, sections, volSec, chSec };
}
const OUTLINE = readOutlineTitles();

function firstDiff(got, want) {
  const n = Math.min(got.length, want.length);
  for (let i = 0; i < n; i++) if (got[i] !== want[i]) return '#' + (i + 1) + ' 基准=[' + want[i] + '] 导出=[' + got[i] + ']';
  if (got.length !== want.length) return '条数 基准=' + want.length + ' 导出=' + got.length;
  return '';
}
function diffCount(got, want) {
  let n = Math.abs(got.length - want.length);
  const m = Math.min(got.length, want.length);
  for (let i = 0; i < m; i++) if (got[i] !== want[i]) n++;
  return n;
}
/* 导出内容 vs 内容源逐条比对；返回 {pass, detail} */
function checkExportFidelity(exp) {
  const sv = [], sc = [], ss = [];
  for (const line of exp.summary.split('\n')) {
    let m;
    if ((m = line.match(/^### (.*)$/))) sv.push(m[1].trim());
    else if ((m = line.match(/^- \[(.*?)\]\(.*?\)$/))) sc.push(m[1].trim());
    else if ((m = line.match(/^ {2}- \[(.*?)\]\(.*?\)$/))) ss.push(m[1].trim());
  }
  const jv = [], jc = [], js = [];
  let jparse = '';
  try {
    const j = JSON.parse(exp.json);
    for (const v of j.volumes || []) {
      jv.push(v.title);
      for (const c of v.chapters || []) {
        jc.push(c.title);
        for (const s of c.sections || []) js.push(s.num + ' ' + s.title);
      }
    }
  } catch (e) { jparse = String(e).slice(0, 60); }
  const tv = [], tc = [], ts = [];
  for (const line of exp.txt.split('\n')) {
    if (line.startsWith('# ') && !line.includes('完整目录')) tv.push(line.slice(2).trim());
    else if (line.startsWith('  ## ')) tc.push(line.slice(5).trim());
    else if (line.startsWith('    - ')) ts.push(line.slice(6).trim());
  }
  const parts = {
    'SUMMARY 卷': [sv, OUTLINE.vols], 'SUMMARY 章': [sc, OUTLINE.chapters], 'SUMMARY 节': [ss, OUTLINE.sections],
    'JSON 卷': [jv, OUTLINE.vols], 'JSON 章': [jc, OUTLINE.chapters], 'JSON 节': [js, OUTLINE.sections],
    'TXT 卷': [tv, OUTLINE.vols], 'TXT 章': [tc, OUTLINE.chapters], 'TXT 节': [ts, OUTLINE.sections]
  };
  const bad = [], detail = {};
  for (const k of Object.keys(parts)) {
    const n = diffCount(parts[k][0], parts[k][1]);
    detail[k] = n;
    if (n) bad.push(k + '(' + n + ') ' + firstDiff(parts[k][0], parts[k][1]));
  }
  if (jparse) bad.push('JSON 解析失败: ' + jparse);
  return { pass: bad.length === 0, detail: bad.length ? bad.join(' ｜ ').slice(0, 600) : JSON.stringify(detail) };
}

async function newPage(w, h, dpr) {
  const page = await browser.newPage({
    viewport: { width: w, height: h, deviceScaleFactor: dpr || 1 },
    hasTouch: w < 900
  });
  const errs = [];
  page.on('pageerror', e => errs.push(String(e).slice(0, 140)));
  await page.goto(URL, { waitUntil: 'load' });
  /* O-2（2026-09-13）数据层异步装配：等待 data-opt-ready 哨兵（数据联动初始化完成），
     降级态（哨兵=0 或缺失）按原 2.5s 落定继续，保证降级路径可测 */
  const ready = await page.waitForFunction(
    () => ['1', '0'].includes(document.documentElement.getAttribute('data-opt-ready')),
    { timeout: 20000 }
  ).then(() => true).catch(() => false);
  if (!ready) await page.waitForTimeout(2500);
  await page.waitForTimeout(300);
  await page.evaluate(() => { document.documentElement.style.scrollBehavior = 'auto'; });
  await page.waitForTimeout(300);
  return { page, errs };
}

function linkVisible(link) {
  let sp = link.parentElement;
  while (sp) {
    const st = getComputedStyle(sp);
    if (/(auto|scroll)/.test(st.overflowY)) break;
    sp = sp.parentElement;
  }
  const lr = link.getBoundingClientRect();
  const sr = sp ? sp.getBoundingClientRect() : { top: 0, bottom: window.innerHeight };
  return lr.top >= sr.top - 1 && lr.bottom <= sr.bottom + 1;
}

/* ============ 视口 A：桌面 1920×1080 ============ */
{
  const { page, errs } = await newPage(1920, 1080, 1);

  /* T1-T5：TOC 跟随视觉几何（此前盲区：只测 class 不测可见性） */
  const scrollTargets = [0, 9000, 21000, 38000, 59000];
  let tocFollowOk = true;
  const followDetail = [];
  for (const y of scrollTargets) {
    await page.evaluate(v => window.scrollTo(0, v), y);
    await page.waitForTimeout(550);
    const d = await page.evaluate(() => {
      const act = Array.from(document.querySelectorAll('.toc-left a.active, .toc-left a.current'));
      for (let sp = act[0] ? act[0].parentElement : null; sp; sp = sp.parentElement) {
        const st = getComputedStyle(sp);
        if (/(auto|scroll)/.test(st.overflowY)) {
          const lr = act[0].getBoundingClientRect();
          const sr = sp.getBoundingClientRect();
          return {
            scrollTop: Math.round(sp.scrollTop),
            linkTop: Math.round(lr.top - sr.top),
            linkBottom: Math.round(lr.bottom - sr.top),
            visH: Math.round(sr.height),
            target: act[0].dataset.target,
            visible: lr.top >= sr.top - 1 && lr.bottom <= sr.bottom + 1,
          };
        }
      }
      return { visible: false, target: act[0] ? act[0].dataset.target : 'none', reason: 'no-scroll-parent' };
    });
    followDetail.push({ y: Math.round(y), ...d });
    if (!d.visible) tocFollowOk = false;
  }
  record('T1 桌面 TOC 激活链接可见性（5 位点）', tocFollowOk, JSON.stringify(followDetail));

  /* T2：连线/溯源注折叠按钮 */
  await page.evaluate(() => window.scrollTo(0, 9000));
  await page.waitForTimeout(400);
  const badge = await page.evaluate(() => {
    const b = document.querySelector('li .note-badge');
    if (!b) return null;
    const li = b.closest('li');
    b.click();
    return li.classList.contains('note-open');
  });
  record('T2 溯源注徽标展开', badge === true, 'note-open=' + badge);

  /* T3：人名浮层 */
  await page.evaluate(() => { document.body.classList.add('notes-all'); });
  await page.waitForTimeout(200);
  const plinkCount = await page.evaluate(() => document.querySelectorAll('a.plink').length);
  const plinkRes = await page.evaluate(() => {
    const a = document.querySelector('a.plink');
    if (!a) return 'no-plink';
    a.click();
    const p = document.getElementById('optPop');
    return p && p.classList.contains('open') ? p.textContent.trim().slice(0, 60) : 'not-open';
  });
  await page.evaluate(() => { const p = document.getElementById('optPop'); if (p) p.classList.remove('open'); document.body.classList.remove('notes-all'); });
  record('T3 人名浮层（plink）', typeof plinkRes === 'string' && plinkRes !== 'no-plink' && plinkRes !== 'not-open', plinkCount + ' links, ' + plinkRes);

  /* T4：文献浮层（reflink） */
  const refRes = await page.evaluate(() => {
    document.body.classList.add('notes-all');
    const a = document.querySelector('a.reflink');
    if (!a) return 'no-reflink';
    a.click();
    const p = document.getElementById('optPop');
    const r = p && p.classList.contains('open') ? p.textContent.trim().slice(0, 60) : 'not-open';
    if (p) p.classList.remove('open');
    document.body.classList.remove('notes-all');
    return r;
  });
  record('T4 文献浮层（reflink）', typeof refRes === 'string' && refRes.indexOf('no-') !== 0 && refRes !== 'not-open', refRes);

  /* T5：长节名折叠（阈值 150 字符；若全库节题均未越阈则功能休眠，须验证休眠与内容一致） */
  const longRes = await page.evaluate(() => {
    const li = document.querySelector('li.long-title');
    if (!li) {
      const mx = Array.from(document.querySelectorAll('ul.sections > li')).reduce((m, el) => {
        const c = el.cloneNode(true);
        c.querySelectorAll('.src, .sec-num, .note-badge, .t-more, .t-short, .t-full, button').forEach(n => n.remove());
        return Math.max(m, (window.__LB && window.__LB.pureTitle ? window.__LB.pureTitle(c) : c.textContent.trim()).length);
      }, 0);
      return mx < 150 ? 'dormant(' + mx + ')' : 'missing(' + mx + ')';
    }
    const btn = li.querySelector('.t-more');
    btn.click();
    return li.classList.contains('open') ? 'open' : 'closed';
  });
  record('T5 长节名展开/收起', longRes === 'open' || longRes.indexOf('dormant') === 0, longRes);

  /* T6：卷导航 prev/next */
  await page.evaluate(() => window.scrollTo(0, 0));
  await page.waitForTimeout(400);
  const volNav = await page.evaluate(() => {
    const nav = document.querySelector('.vol-nav');
    if (!nav) return 'none';
    const links = Array.from(nav.querySelectorAll('a[href^="#vol-"]'));
    links[links.length - 1].click();
    return links.length;
  });
  await page.waitForTimeout(700);
  const volNavY = await page.evaluate(() => Math.round(window.scrollY));
  record('T6 卷导航点击跳转', volNav !== 'none' && volNavY > 0, volNav + ' links, y=' + volNavY);

  /* T7：跨卷图谱几何（完整无省略 + 零重叠 + 点击放大） */
  await page.evaluate(() => document.getElementById('optGraphBtn').click());
  await page.waitForTimeout(500);
  const graph = await page.evaluate((outlineVols) => {
    const labels = Array.from(document.querySelectorAll('#optGraph text.graph-label'));
    let hasEllipsis = 0;
    labels.forEach(t => { if (t.textContent.includes('…')) hasEllipsis++; });
    // 完整性与无省略：标签文本应含各卷短名。
    // 真值取**内容源**卷题（outlineVols），**不取页面 h2**——页面 h2 含运行时计数徽标，
    // 与图谱标签同源，两侧同带徽标会使“包含”判据恒成立而失灵（2026-09-20 修正）。
    const missing = [];
    outlineVols.forEach(full => {
      const short = full.indexOf('  ') >= 0 ? full.slice(full.indexOf('  ') + 2) : full;
      let found = false;
      labels.forEach(l => { if (l.textContent.replace(/\s+/g, '').includes(short.replace(/\s+/g, ''))) found = true; });
      if (!found) missing.push(short.slice(0, 10));
    });
    let overlaps = 0;
    for (let i = 0; i < labels.length; i++) for (let j = i + 1; j < labels.length; j++) {
      const a = labels[i].getBoundingClientRect(), b = labels[j].getBoundingClientRect();
      if (a.x < b.x + b.width && a.x + a.width > b.x && a.y < b.y + b.height && a.y + a.height > b.y) overlaps++;
    }
    return { labels: labels.length, vols: document.querySelectorAll("section[id^='vol-']").length, hasEllipsis, missing, overlaps };
  }, OUTLINE.vols);
  console.log('GRAPH_RAW', JSON.stringify(graph));
  record('T7a 图谱标签完整显示（无省略）', graph.labels === graph.vols && graph.hasEllipsis === 0 && graph.missing.length === 0, 'labels=' + graph.labels + ' vols=' + graph.vols + ' ellipsis=' + graph.hasEllipsis + ' missing=' + graph.missing.length);
  record('T7b 图谱零重叠（视觉几何）', graph.overlaps === 0, 'overlaps=' + graph.overlaps);
  const zoomRes = await page.evaluate(() => {
    const t = document.querySelector('#optGraph text.graph-label');
    if (!t) return 'none';
    const before = parseFloat(getComputedStyle(t).fontSize);
    t.dispatchEvent(new MouseEvent('click', { bubbles: true }));
    const afterClick = parseFloat(getComputedStyle(t).fontSize);
    const cls = t.classList.contains('zoomed');
    t.dispatchEvent(new MouseEvent('click', { bubbles: true }));
    const afterClick2 = parseFloat(getComputedStyle(t).fontSize);
    return { before, afterClick, cls, afterClick2 };
  });
  record('T7c 图谱点击放大/还原', zoomRes !== 'none' && zoomRes.afterClick > zoomRes.before && zoomRes.cls === true && zoomRes.afterClick2 === zoomRes.before, JSON.stringify(zoomRes));
  await page.screenshot({ path: SHOT + 'headful_graph_1920.png' });
  await page.keyboard.press('Escape');
  await page.waitForTimeout(300);

  /* T8：进度条 */
  await page.evaluate(() => window.scrollTo(0, 30000));
  await page.waitForTimeout(500);
  const progW = await page.evaluate(() => {
    const i = document.querySelector('.breadcrumb .prog i');
    if (!i) return 'none';
    if (window.CSS && CSS.supports && CSS.supports('animation-timeline: scroll()')) {
      const w = getComputedStyle(i).width;   /* CSS 滚动时间线驱动：读动画生效值 */
      return w && w !== '0px' && w !== 'auto' ? w : '0%';
    }
    return i.style.width || 'none';
  });
  record('T8 阅读进度条', progW !== 'none' && progW !== '0%' && progW !== '', progW);

  /* T9：面包屑可见 */
  const bcVisible = await page.evaluate(() => {
    const b = document.querySelector('.breadcrumb');
    return b ? getComputedStyle(b).display === 'flex' : false;
  });
  record('T9 面包屑可见', bcVisible === true, 'display');

  /* T10：全局键盘 Alt+R 已在前轮测过，此处附 j/k */
  await page.evaluate(() => window.scrollTo(0, 10000));
  await page.waitForTimeout(300);
  await page.keyboard.press('j');
  await page.waitForTimeout(700);
  const jY = await page.evaluate(() => Math.round(window.scrollY));
  record('T10 键盘 j 跳下一章', jY > 10000, 'y=' + jY);

  /* T21：页内导航历史中性（数据／回归）——主理人令「无论怎样点击都不应当产生
     历史记录（应仅有一个）」。判据＝ history.length 差量恒 0：①点卷链接、
     ②点章链接、③按 n、④按 p、⑤滚轮增量滑动，逐步记 len；全部等于初始值；
     同时以滚动位置变化与片段非空确证操作已生效（防「全拦死」假绿）。 */
  await page.evaluate(() => { try { window.scrollTo({ top: 0, behavior: 'instant' }); } catch (e) { window.scrollTo(0, 0); } });
  await page.waitForTimeout(400);
  const h0 = await page.evaluate(() => history.length);
  const hSteps = [];
  await page.evaluate(() => { const a = document.querySelector('.toc-left a[data-target="vol-3"]'); if (a) a.click(); });
  await page.waitForTimeout(1600);
  hSteps.push(await page.evaluate(() => ({ tag: 'click-vol', len: history.length, y: Math.round(scrollY), hash: location.hash })));
  await page.evaluate(() => { const a = document.querySelector('.toc-left a[data-target^="vol-5-ch-"]'); if (a) a.click(); });
  await page.waitForTimeout(1600);
  hSteps.push(await page.evaluate(() => ({ tag: 'click-ch', len: history.length, y: Math.round(scrollY), hash: location.hash })));
  await page.keyboard.press('n');
  await page.waitForTimeout(1000);
  hSteps.push(await page.evaluate(() => ({ tag: 'key-n', len: history.length, y: Math.round(scrollY), hash: location.hash })));
  await page.keyboard.press('p');
  await page.waitForTimeout(1000);
  hSteps.push(await page.evaluate(() => ({ tag: 'key-p', len: history.length, y: Math.round(scrollY), hash: location.hash })));
  await page.mouse.wheel(0, 2400);
  await page.waitForTimeout(500);
  hSteps.push(await page.evaluate(() => ({ tag: 'wheel', len: history.length, y: Math.round(scrollY), hash: location.hash })));
  const hNeutral = hSteps.every(s => s.len === h0);
  const hMoved = hSteps[0].y > 0 && hSteps[1].y !== hSteps[0].y;
  const hHashed = hSteps.every(s => s.hash && s.hash.charAt(0) === '#');
  record('T21 页内导航历史中性（零新增条目）', hNeutral && hMoved && hHashed,
    'L0=' + h0 + ' neutral=' + hNeutral + ' moved=' + hMoved + ' ' + JSON.stringify(hSteps));

  record('桌面 JS 错误', errs.length === 0, errs.join('; '));
  await page.close();
}

/* ============ 视口 B：手机 2400x1080 6.67寸（412x915@2.75） ============ */
{
  const { page, errs } = await newPage(412, 915, 2.75);

  /* T11：抽屉模式 TOC 滚动跟随（视觉） */
  await page.evaluate(() => document.getElementById('tocToggle').click());
  await page.waitForTimeout(400);
  const drawerRes = await page.evaluate(() => {
    const d = document.getElementById('tocDrawer');
    if (!d.classList.contains('open')) return 'not-open';
    // 点击第 20 卷链接（后段，必在滚动区外）
    const links = Array.from(d.querySelectorAll('.toc-left a[data-target]'));
    const target = links.find(a => a.dataset.target === 'vol-20');
    if (!target) return 'no-link';
    target.click();
    return 'clicked';
  });
  await page.waitForTimeout(1600); // 抽屉长距平滑滚动（c-v 按需渲染）需较长落定
  const drawerGeo = await page.evaluate(() => {
    const link = Array.from(document.querySelectorAll('.toc-drawer a[data-target]')).find(a => a.dataset.target === 'vol-20');
    const d = document.getElementById('tocDrawer');
    const lr = link.getBoundingClientRect(), dr = d.getBoundingClientRect();
    return {
      scrollTop: Math.round(d.scrollTop),
      linkTop: Math.round(lr.top - dr.top),
      visible: lr.top >= dr.top - 1 && lr.bottom <= dr.bottom + 1,
    };
  });
  record('T11 手机抽屉选中卷可见（视觉几何）', drawerRes === 'clicked' && drawerGeo.visible, JSON.stringify({ drawerRes, ...drawerGeo }));
  /* 清理须与页面 setOpen(false) 同构：抽屉与遮罩两件都关——只关抽屉会留下遮罩（z44）
     盖住全屏，污染后续 T16 的量测（2026-10-14 负向自证时实测：命中对象为 tocScrim）。 */
  await page.evaluate(() => { document.getElementById('tocDrawer').classList.remove('open'); document.getElementById('tocScrim').classList.remove('open'); document.body.style.overflow = ''; });
  await page.waitForTimeout(300);

  /* T15：层叠秩序——抽屉/遮罩须高于面包屑，且面包屑不得压住抽屉顶部
     （2026-09-26 补：原套件只断言元素各自可见，从不测跨层遮挡，故「面包屑压住左侧目录」漏检） */
  {
    await page.evaluate(() => { var b = document.getElementById('tocToggle'); if (b) b.click(); });
    await page.waitForTimeout(500);
    const z = await page.evaluate(() => {
      const bc = document.querySelector('.breadcrumb');
      const dr = document.getElementById('tocDrawer');
      const sc = document.querySelector('.toc-scrim');
      if (!bc || !dr) return { ok: false, why: 'missing' };
      const zbc = parseInt(getComputedStyle(bc).zIndex) || 0;
      const zdr = parseInt(getComputedStyle(dr).zIndex) || 0;
      const zsc = sc ? (parseInt(getComputedStyle(sc).zIndex) || 0) : 0;
      // 命中测试：面包屑中心处的最上层元素不应是面包屑自身（抽屉打开时）
      const r = bc.getBoundingClientRect();
      const el = document.elementFromPoint(r.x + Math.min(40, r.width / 2), r.y + r.height / 2);
      const hitsBc = el ? (el === bc || bc.contains(el)) : true;
      return { ok: true, zbc, zdr, zsc, hitsBc, hitCls: el ? String(el.className || el.tagName) : null };
    });
    record('T15 抽屉层叠高于面包屑（无压盖）', z.ok && z.zdr > z.zbc && z.zsc > z.zbc && !z.hitsBc, JSON.stringify(z));
    /* 同 T11 清理：抽屉与遮罩两件俱关（仅关抽屉会留 z44 遮罩全屏污染 T16 量测）。 */
    await page.evaluate(() => { var d = document.getElementById('tocDrawer'); if (d) d.classList.remove('open'); var s = document.getElementById('tocScrim'); if (s) s.classList.remove('open'); document.body.style.overflow = ''; });
    await page.waitForTimeout(300);
  }

  /* T16：面包屑可见态下两角浮动按钮中心可点（2026-09-26 立，2026-10-14 重写）
     主理人 2026-10-14 报障「左侧边栏按钮与面包屑存在干涉」，处置＝同右侧按钮
     （按钮浮于面包屑之上、中心可点）。判据：滚动态（scrollY>120，面包屑须为
     visible）下，左上「目录」与右上「设置」两按钮**中心**的 elementFromPoint
     须命中按钮自身；并以 visibility 断言锚定「可见态」，防隐藏态量测恒真空转
     （142 批曾以 scrollTo(0,0) 使判据在隐藏态空转：不可见面包屑不构成压盖，恒过）。 */
  {
    await page.evaluate(() => { try { window.scrollTo({ top: 3000, behavior: 'instant' }); } catch (e) { window.scrollTo(0, 3000); } });
    await page.waitForTimeout(700);
    const geo = await page.evaluate(() => {
      const bc = document.querySelector('.breadcrumb');
      const bcVis = bc ? getComputedStyle(bc).visibility : 'missing';
      const centers = [];
      ['.toc-toggle', '.opt-tools-toggle'].forEach(function (sel) {
        const e = document.querySelector(sel);
        if (!e) { centers.push({ sel, hit: false, why: 'missing' }); return; }
        const r = e.getBoundingClientRect();
        const el = document.elementFromPoint(r.x + r.width / 2, r.y + r.height / 2);
        centers.push({ sel, hit: !!(el && (el === e || e.contains(el))), top: el ? (el.id || el.className || el.tagName) : null });
      });
      return { bcVis, centers };
    });
    record('T16 面包屑可见态下两角按钮中心可点（无压盖）',
      geo.bcVis === 'visible' && geo.centers.every(c => c.hit), JSON.stringify(geo));
  }

  /* T12：手机图谱完整无省略 */
  await page.evaluate(() => document.getElementById('optGraphBtn').click());
  await page.waitForTimeout(500);
  const gPhone = await page.evaluate(() => {
    const labels = Array.from(document.querySelectorAll('#optGraph text.graph-label'));
    return {
      labels: labels.length,
      vols: document.querySelectorAll("section[id^='vol-']").length,
      ellipsis: labels.filter(t => t.textContent.includes('…')).length,
      overlaps: (() => {
        let c = 0;
        for (let i = 0; i < labels.length; i++) for (let j = i + 1; j < labels.length; j++) {
          const a = labels[i].getBoundingClientRect(), b = labels[j].getBoundingClientRect();
          if (a.x < b.x + b.width && a.x + a.width > b.x && a.y < b.y + b.height && a.y + a.height > b.y) c++;
        }
        return c;
      })(),
    };
  });
  record('T12 手机图谱完整零重叠', gPhone.labels === gPhone.vols && gPhone.ellipsis === 0 && gPhone.overlaps === 0, JSON.stringify(gPhone));
  await page.screenshot({ path: SHOT + 'headful_graph_phone.png' });
  await page.keyboard.press('Escape');

  record('手机 JS 错误', errs.length === 0, errs.join('; '));
  await page.close();
}

/* ============ 视口 C：窄屏抽屉 + summary + 主题持久化 ============ */
{
  const { page, errs } = await newPage(820, 1180, 1);
  /* T13（2026-09-20 强化）：除行数与统计串外，追加“导出内容与内容源逐条一致”判据——
     SUMMARY／JSON／TXT 三种导出的卷题、章题、节名必须与 data/outline.txt 完全一致。
     缘由：原判据只查行数 > 1800 与统计串，故“卷题带 N 章 · N 节 徽标、章题带 N 节 徽标、
     节名带注字徽标、题文被尾正则误删”等不一致在套件中完全不可见（缺陷长期潜伏）。 */
  const summary = await page.evaluate(async () => {
    const caps = [];
    const _B = window.Blob;
    window.Blob = function (parts, opts) {
      try { caps.push((parts || []).map(function (p) { return typeof p === 'string' ? p : ''; }).join('')); } catch (e) {}
      return new _B(parts, opts);
    };
    window.Blob.prototype = _B.prototype;
    const t = window.exportSummaryText();
    const click = function (k) {
      const b = document.getElementById('optExport');
      if (b) b.click();
      const it = document.querySelector('#exportMenu button[data-x="' + k + '"]');
      if (it) it.click();
    };
    click('json');
    click('txt');
    await new Promise(function (r) { setTimeout(r, 400); });
    return { len: t.split('\n').length, hasStats: /统计：75 卷 523 章 3705 节/.test(t),
             summary: t, json: caps[0] || '', txt: caps[1] || '' };
  });
  const fid = checkExportFidelity(summary);
  record('T13 SUMMARY 导出内容', summary.len > 1800 && summary.hasStats && fid.pass,
         JSON.stringify({ len: summary.len, hasStats: summary.hasStats, fid: fid.detail }));
  await page.close();
}

/* ============ 视口 C2：CSV 与 PDF 导出内容复核（2026-09-26 增） ============
   T13 只覆盖 SUMMARY／JSON／TXT；CSV 与 PDF 两项此前无断言。判据：
   CSV 逐行（卷／章／节号／节名）与内容源多重集一致；PDF 打印视图 h2／h3／li 计数与
   副题计数串同内容源一致。 */
{
  const { page, errs } = await newPage(1200, 900, 1);
  const ex = await page.evaluate(async () => {
    const caps = []; const _B = window.Blob;
    window.Blob = function (parts, opts) {
      try { caps.push((parts || []).map(function (p) { return typeof p === "string" ? p : ""; }).join("")); } catch (e) {}
      return new _B(parts, opts);
    };
    window.Blob.prototype = _B.prototype;
    const _p = window.print; window.print = function () {};
    const _o = window.open;
    window.open = function () { return { document: { write: function () {}, close: function () {} }, focus: function () {}, print: function () {}, addEventListener: function () {}, close: function () {} }; };
    const click = function (k) {
      const b = document.getElementById("optExport"); if (b) b.click();
      const it = document.querySelector("#exportMenu button[data-x=\"" + k + "\"]"); if (it) it.click();
    };
    click("csv"); click("pdf");
    await new Promise(function (r) { setTimeout(r, 700); });
    window.print = _p; window.open = _o;
    return { csv: caps[0] || "", pdf: caps[1] || "" };
  });
  var CRLF = String.fromCharCode(13) + String.fromCharCode(10);
  var SEP = String.fromCharCode(1);
  var Q = String.fromCharCode(34);
  var D = String.fromCharCode(34) + String.fromCharCode(34);
  const csvRows = ex.csv.split(CRLF).filter(function (l) { return l.length; }).slice(1).map(function (l) {
    var out = []; var re = new RegExp(Q + "((?:[^" + Q + "]|" + D + ")*)" + Q, "g"); var m;
    while ((m = re.exec(l))) out.push(m[1].split(D).join(Q));
    return out;
  });
  const secKey = r => r[2] + " " + r[3];
  const join = a => a.slice().sort().join(SEP);
  const csvSecSet = join(csvRows.map(secKey));
  const truthSecSet = join(OUTLINE.sections);
  /* 卷/章列按「每卷/每章节数」归组比对（CSV 一节一行，卷/章自然重复） */
  const csvVolCnt = {}, csvChCnt = {};
  csvRows.forEach(function (r) {
    csvVolCnt[r[0]] = (csvVolCnt[r[0]] || 0) + 1;
    const k = r[0] + SEP + r[1];
    csvChCnt[k] = (csvChCnt[k] || 0) + 1;
  });
  const cntEq = (a, b) => { const ka = Object.keys(a).sort(), kb = Object.keys(b).sort();
    if (ka.length !== kb.length) return false;
    for (let i = 0; i < ka.length; i++) { if (ka[i] !== kb[i] || a[ka[i]] !== b[kb[i]]) return false; }
    return true; };
  const csvVolOk = cntEq(csvVolCnt, OUTLINE.volSec);
  const csvChOk = cntEq(csvChCnt, OUTLINE.chSec);
  const cnt = (t, re) => (t.match(re) || []).length;
  const pv = cnt(ex.pdf, /<h2>/g), pc = cnt(ex.pdf, /<h3>/g), ps = cnt(ex.pdf, /<li>/g);
  const subOk = ex.pdf.includes(OUTLINE.vols.length + " 卷 · " + OUTLINE.chapters.length + " 章 · " + OUTLINE.sections.length + " 节");
  const bomOk = ex.csv.charCodeAt(0) === 65279;
  const ok = bomOk && csvRows.length === OUTLINE.sections.length && csvSecSet === truthSecSet
    && csvVolOk && csvChOk
    && pv === OUTLINE.vols.length && pc === OUTLINE.chapters.length && ps === OUTLINE.sections.length && subOk && errs.length === 0;
  record('T17 CSV 与 PDF 导出内容', ok, JSON.stringify({
    csvRows: csvRows.length, csvSec: csvSecSet === truthSecSet, csvVolGroups: Object.keys(csvVolCnt).length, csvVolOk: csvVolOk, csvChOk: csvChOk, bom: bomOk,
    pdf: { h2: pv, h3: pc, li: ps }, pdfSub: subOk, errs: errs.length, csvLen: ex.csv.length, pdfLen: ex.pdf.length
  }));
  await page.close();
}

/* ============ 视口 C3：HTML 本体导出一致性（T20，2026-10-14 增） ============
   「HTML 本体」菜单项按打开方式双通道：
   Part 1 http(s)：同源 <a download> 由浏览器下载器直取服务器原始字节——判据＝
     下载事件触发＋下载名形制“目录-<页面版本>.html”（版本取 .page-version、
     冒号净化为“-”，五项导出共用 exportFileName() 单一实现）＋文件与磁盘
     index.html **逐字节相等**。套件自起 127.0.0.1 随机空闲端口临时服务器
    （跑完即关）；服务器↔磁盘逐字节等价由第十一件 A 判据常备守护。
   Part 2 file://：Chromium 对 file 源不授同源（含自身），download 属性不生效、
     脚本亦无 API 直读自身原始字节——页面回退为文档序列化导出（blob 通道）。
     判据＝导出可下载、文件名同形制、DOMParser 解析后**逐条**卷／章／节题面
     （与页面 pureTitle 同构净化后）与内容源 outline 派生真值全等（非仅计数——
     防“计数同而内容错”的静默假绿）。逐字节保真仅 http 通道承诺。 */
{
  const { page, errs } = await newPage(1200, 900, 1);
  const T20DIR = 'D:/librebsd/script/_staging/export_html_t20/';
  let ok20 = false;
  const det20 = { mode: 'http+file' };
  try {
    const ver = await page.evaluate(() => {
      const el = document.querySelector('.page-version');
      return el ? el.textContent.trim() : '';
    });
    const wantName = '目录-' + ver.split(':').join('-') + '.html';
    fs.mkdirSync(T20DIR, { recursive: true });

    /* —— Part 1：http 通道逐字节 —— */
    /* ROOT 以 normalize＋sep 收口，与 path.join 产物分隔符一致（否则 startsWith 守卫恒假 → 403）。 */
    const ROOT = path.normalize('D:/librebsd/05-卷册大纲/目录') + path.sep;
    const srv = http.createServer((req, res) => {
      const rel = decodeURIComponent((req.url || '/').split('?')[0].split('#')[0]);
      const p = path.join(ROOT, rel === '/' ? 'index.html' : rel);
      if (!p.startsWith(ROOT)) { res.writeHead(403); res.end(); return; }
      fs.readFile(p, (e, buf) => {
        if (e) { res.writeHead(404); res.end(); return; }
        res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
        res.end(buf);
      });
    });
    await new Promise(r => srv.listen(0, '127.0.0.1', r));
    const port = srv.address().port;
    try {
      const p2 = await browser.newPage({ viewport: { width: 1200, height: 900 } });
      const errs2 = [];
      p2.on('pageerror', e => errs2.push(String(e).slice(0, 140)));
      await p2.goto('http://127.0.0.1:' + port + '/index.html', { waitUntil: 'load' });
      await p2.waitForFunction(
        () => ['1', '0'].includes(document.documentElement.getAttribute('data-opt-ready')),
        { timeout: 20000 }
      ).catch(() => {});
      await p2.waitForTimeout(400);
      const ver2 = await p2.evaluate(() => {
        const el = document.querySelector('.page-version');
        return el ? el.textContent.trim() : '';
      });
      const want2 = '目录-' + ver2.split(':').join('-') + '.html';
      const [dl] = await Promise.all([
        p2.waitForEvent('download', { timeout: 15000 }),
        p2.evaluate(() => {
          const b = document.getElementById('optExport'); if (b) b.click();
          const it = document.querySelector('#exportMenu button[data-x="html"]'); if (it) it.click();
        })
      ]);
      det20.httpName = dl.suggestedFilename();
      const dest1 = T20DIR + 'exported_http.html';
      await dl.saveAs(dest1);
      const got = fs.readFileSync(dest1);
      const want = fs.readFileSync(INDEX_PATH);
      det20.httpBytes = got.length + '/' + want.length;
      det20.httpNameOk = det20.httpName === want2;
      det20.httpByteOk = got.equals(want);
      det20.httpErrs = errs2.length;
      await p2.close();
    } finally {
      srv.close();
      if (srv.closeAllConnections) srv.closeAllConnections();
    }

    /* —— Part 2：file:// 回退通道内容完整 —— */
    const [dl2] = await Promise.all([
      page.waitForEvent('download', { timeout: 15000 }),
      page.evaluate(() => {
        const b = document.getElementById('optExport'); if (b) b.click();
        const it = document.querySelector('#exportMenu button[data-x="html"]'); if (it) it.click();
      })
    ]);
    det20.fileName = dl2.suggestedFilename();
    const dest2 = T20DIR + 'exported_file.html';
    await dl2.saveAs(dest2);
    const s = fs.readFileSync(dest2, 'utf8');
    det20.fileBytes = Buffer.byteLength(s);
    det20.fileNameOk = det20.fileName === wantName;
    const deep = await page.evaluate((content) => {
      const d = new DOMParser().parseFromString(content, 'text/html');
      /* 与页面 __LB.pureTitle 同构的净化器（10-boot.js）：仅剥离运行时注入件与注／节号，
         返回内容层题面。file 导出＝运行时 DOM 序列化（含装饰），须同口径净化后
         才能与内容源逐条比对（同 T13「导出读运行时 DOM 须净化」的既有处理）。 */
      const PURE_SEL = '.vol-badge, .ch-badge, .note-badge, .t-more, .t-short, .src, .sec-num, .path, .pv';
      const pure = (el) => {
        if (!el) return '';
        const c = el.cloneNode(true);
        const full = c.querySelector('.t-full');
        if (full) return full.textContent.trim();
        c.querySelectorAll(PURE_SEL).forEach((n) => n.remove());
        return c.textContent.trim();
      };
      const sv = [], sc = [], ss = [];
      d.querySelectorAll("section[id^='vol-']").forEach((v) => {
        sv.push(pure(v.querySelector('h2')));
        v.querySelectorAll('h3.chapter[id]').forEach((ch) => {
          sc.push(pure(ch));
          const ul = ch.nextElementSibling;
          if (ul && ul.classList && ul.classList.contains('sections')) {
            Array.prototype.slice.call(ul.children).forEach((li) => {
              const n = li.querySelector(':scope > .sec-num');
              if (!n) return;
              ss.push(n.textContent.trim() + ' ' + pure(li));
            });
          }
        });
      });
      return { sv: sv, sc: sc, ss: ss, hasVer: !!d.querySelector('.page-version') };
    }, s);
    const dv = diffCount(deep.sv, OUTLINE.vols);
    const dc = diffCount(deep.sc, OUTLINE.chapters);
    const ds = diffCount(deep.ss, OUTLINE.sections);
    det20.fileFid = { v: dv, c: dc, s: ds, cnt: [deep.sv.length, deep.sc.length, deep.ss.length] };
    const fileOk = deep.hasVer && dv === 0 && dc === 0 && ds === 0;
    ok20 = det20.httpNameOk && det20.httpByteOk && det20.httpErrs === 0
      && det20.fileNameOk && fileOk && errs.length === 0;
  } catch (e) {
    det20.err = String(e).slice(0, 140);
  }
  record('T20 HTML 本体导出一致性', ok20, JSON.stringify(det20));
  await page.close();
}

/* ============ 视口 D：打印媒体回落浅色 ============
   2026-09-18 第十八批：暗色主题下打印原为“浅字印白纸”（body/h2 亮度 0.95）
   ——页面自带的“输出 PDF”是 JS 另开窗口并自带打印样式，会掩盖此缺陷，
   故须以 emulateMedia('print') 直接测主页面。修法：暗色规则全部包进 @media screen。 */
{
  const { page, errs } = await newPage(1200, 900, 1);
  const lum = s => {
    const m = /rgba?\((\d+),\s*(\d+),\s*(\d+)/.exec(s || '');
    return m ? (0.2126 * +m[1] + 0.7152 * +m[2] + 0.0722 * +m[3]) / 255 : null;
  };
  const res = {};
  for (const theme of ['light', 'oled']) {
    await page.evaluate(t => document.documentElement.setAttribute('data-theme', t), theme);
    await page.emulateMedia({ media: 'print' });
    await page.waitForTimeout(220);
    res[theme] = await page.evaluate(() => {
      const g = s => { const e = document.querySelector(s); return e ? getComputedStyle(e) : null; };
      return {
        body: g('body').color,
        h2: g('.doc-block h2').color,
        bg: g('body').backgroundColor,
        before: getComputedStyle(document.body, '::before').backgroundImage.slice(0, 70)
      };
    });
  }
  await page.emulateMedia({ media: 'screen' });
  const darkText = t => lum(res[t].body) < 0.4 && lum(res[t].h2) < 0.4;
  const whiteBg = t => /255,\s*255,\s*255/.test(res[t].bg);
  const lightBefore = /249,\s*245,\s*240/.test(res.oled.before);
  record('T14 打印媒体回落浅色（纯黑/浅双主题）',
    darkText('light') && darkText('oled') && whiteBg('light') && whiteBg('oled') && lightBefore && errs.length === 0,
    JSON.stringify({
      dark: { body: res.oled.body, h2: res.oled.h2, bg: res.oled.bg, lum: +lum(res.oled.body).toFixed(3) },
      light: { lum: +lum(res.light.body).toFixed(3) }, beforeLight: lightBefore, errs: errs.length
    }));
  await page.close();
}

/* ============ 视口 E：载入后收窄（T18 横向溢出回归） ============
   2026-09-27 立。缘由：本件与 fullsize_regression／full_matrix_regression 三套件
   均「每档重新载入」，故「宽度在载入时被固化为内联值、此后不随视口回流」一类缺陷
   对它们恒不可见——实测该缺陷曾使 .doc-page 在载入 1920 后收窄到 390／320 时
   仍为 958.391px、documentElement.scrollWidth 停在 958（出现横向滚动条、右缘被裁）。
   故本项**先载入再改宽**：断言 .doc-page 渲染宽度跟随视口、文档无横向溢出、左右不越界。 */
{
  const { page, errs } = await newPage(1920, 1080, 1);
  const steps = [];
  for (const [w, h] of [[390, 844], [320, 568], [820, 1180]]) {
    await page.setViewportSize({ width: w, height: h });
    await page.waitForTimeout(400);
    steps.push(await page.evaluate(() => {
      const r = document.querySelector('.doc-page').getBoundingClientRect();
      return {
        vw: window.innerWidth, sw: document.documentElement.scrollWidth,
        width: +r.width.toFixed(1), left: +r.left.toFixed(1), right: +r.right.toFixed(1)
      };
    }));
  }
  const bad = steps.filter(s => s.sw > s.vw + 1 || s.width > s.vw + 1 || s.right > s.vw + 1 || s.left < -1);
  record('T18 载入后收窄视口仍无横向溢出（几何／回归）', bad.length === 0 && errs.length === 0,
    JSON.stringify({ steps, errs: errs.length }));
  await page.close();
}

/* ============ 视口 F：章卷题面可选性（T19，2026-09-27 增） ============
   缘由：2026-09-26 的「卷/章折叠」给 h2／h3.chapter 加了 user-select:none，致**题面
   文字整块不可选**（主理人报障“章卷文字在网页上无法选中”）；且同一手势收尾的 click
   还会顺手把整卷折起（拖选一无所获、卷却折了）。
   本项锁五条：①题面本体可选；②装饰箭头仍不入选区（判据取 ::after 伪元素计算值，
   不取选区文本——否则“选区里没有 ▾”可由选择失败被动满足，属空转判据）；③拖选只做
   选择、不折叠；④**双击选词全程版面零跳动**——在确认窗内逐次采样，折叠计数须恒 0
   （初版“先折后折回”会令整卷闪一下，此采样即专拦该回归）；⑤单击仍能折／展
   （**特征正控**：把折叠闸死也算 FAIL）。
   点击点一律取「文字行」几何（h2 盒左缘是 4px 强调竖线＋内边距、h3 盒心可能落在题文
   右侧空白，用元素盒会把点击落到非文字处，探针曾据此误判）。 */
{
  const { page, errs } = await newPage(1920, 1080, 1);
  async function titlePoint(sel) {
    return page.evaluate((s) => {
      const el = document.querySelector(s);
      if (!el) return null;
      const tn = Array.from(el.childNodes).find(n => n.nodeType === 3 && n.textContent.trim());
      if (!tn) return null;
      const r = document.createRange(); r.selectNodeContents(tn);
      const rect = r.getBoundingClientRect();
      return { x: rect.left + 2, y: rect.top + rect.height / 2, full: el.textContent };
    }, sel);
  }
  const foldState = () => page.evaluate(() => ({
    blocks: document.querySelectorAll('.doc-block.folded').length,
    chapters: document.querySelectorAll('h3.chapter.folded').length
  }));
  const foldedTotal = async () => { const f = await foldState(); return f.blocks + f.chapters; };
  const clearSel = () => page.evaluate(() => { window.getSelection().removeAllRanges(); });
  const selText = () => page.evaluate(() => window.getSelection().toString());
  /* 归一：选区文本经 Selection.toString() 取的是**渲染文本**（连续空白折为一个），
     而 textContent 保留原字符——卷题「第N卷」与题名之间正是 2 个半角空格（夹具纪律⑤），
     两侧不归一则子串判据对卷题恒假（实测 sel“第一卷 自由”/ full“第一卷  自由与必然…”）。 */
  const norm = (t) => t.replace(/\s+/g, ' ').trim();

  /* ① 题面可选 ② 箭头不可选（伪元素计算值） */
  const css = await page.evaluate(() => {
    const h2 = document.querySelector('.doc-block > h2'), h3 = document.querySelector('h3.chapter');
    const us = (el, ps) => getComputedStyle(el, ps || null).userSelect;
    return { h2: us(h2), h3: us(h3), h2Arrow: us(h2, '::after'), h3Arrow: us(h3, '::after') };
  });
  const selectable = ['auto', 'text'].indexOf(css.h2) >= 0 && ['auto', 'text'].indexOf(css.h3) >= 0;
  const arrowOff = css.h2Arrow === 'none' && css.h3Arrow === 'none';

  /* ③ 拖选卷题／章题：须真选到本处题文（判据＝选区文本是本题文的子串）且不折叠 */
  const pv = await titlePoint('.doc-block > h2');
  await clearSel();
  await page.mouse.move(pv.x, pv.y); await page.mouse.down();
  await page.mouse.move(pv.x + 120, pv.y, { steps: 10 }); await page.mouse.up();
  await page.waitForTimeout(400);
  const dragVol = { text: await selText(), fold: await foldState() };
  dragVol.inTitle = dragVol.text.length >= 4 && norm(pv.full).indexOf(norm(dragVol.text)) >= 0;

  const pc = await titlePoint('h3.chapter');
  await clearSel();
  await page.mouse.move(pc.x, pc.y); await page.mouse.down();
  await page.mouse.move(pc.x + 120, pc.y, { steps: 10 }); await page.mouse.up();
  await page.waitForTimeout(400);
  const dragCh = { text: await selText(), fold: await foldState() };
  dragCh.inTitle = dragCh.text.length >= 4 && norm(pc.full).indexOf(norm(dragCh.text)) >= 0;

  /* ④ 双击选词：确认窗内逐次采样折叠计数，须恒 0（零跳动）；选词须成立
     ⚠ 第二击须显式 clickCount:2 —— Playwright 的 mouse.down／up 每击都是 detail=1，
       双击手势（detail>1）与选词都不会发生（首版即据此误判成“撤单失效”）。 */
  const flash = [];
  await clearSel();
  await page.mouse.click(pc.x, pc.y);                        /* 首击（detail=1，入确认窗） */
  await page.waitForTimeout(120); flash.push(await foldedTotal());
  await page.mouse.click(pc.x, pc.y, { clickCount: 2 });     /* 第二击（detail=2 → 双击手势，撤单） */
  await page.waitForTimeout(120); flash.push(await foldedTotal());
  await page.waitForTimeout(320); flash.push(await foldedTotal());
  const dblCh = { text: await selText(), fold: await foldState(), flash: flash };
  dblCh.inTitle = dblCh.text.length >= 1 && norm(pc.full).indexOf(norm(dblCh.text)) >= 0;
  dblCh.noFlash = flash.every(v => v === 0);

  /* ⑤ 正控：单击卷题仍能折、再单击仍能展；单击章题仍能折（确认窗后生效）。
     先清场，使本段判据不依赖前段残留的折叠态。 */
  await page.evaluate(() => {
    document.querySelectorAll('.folded').forEach(function (el) { el.classList.remove('folded'); });
  });
  await clearSel();
  await page.mouse.click(pv.x, pv.y);
  await page.waitForTimeout(120);
  const ctrlPreWindow = await foldedTotal();                  /* 确认窗内应尚未折 */
  await page.waitForTimeout(400);
  const ctrlFoldVol = await foldedTotal();
  await page.waitForTimeout(800);                             /* 拉出双击窗口，确保是独立单击 */
  await clearSel();
  await page.mouse.click(pv.x, pv.y);
  await page.waitForTimeout(520);
  const ctrlUnfoldVol = await foldedTotal();
  await clearSel();
  await page.mouse.click(pc.x, pc.y);
  await page.waitForTimeout(520);
  const ctrlFoldCh = await foldedTotal();

  const pass = selectable && arrowOff
    && dragVol.inTitle && dragVol.fold.blocks === 0
    && dragCh.inTitle && dragCh.fold.chapters === 0
    && dblCh.inTitle && dblCh.noFlash && dblCh.fold.blocks === 0 && dblCh.fold.chapters === 0
    && ctrlFoldVol === 1 && ctrlUnfoldVol === 0 && ctrlFoldCh === 1
    && errs.length === 0;
  record('T19 章卷题面文字可选中（选择手势不折叠、零跳动）', pass,
    JSON.stringify({ css, dragVol: { len: dragVol.text.length, inTitle: dragVol.inTitle, fold: dragVol.fold.blocks },
      dragCh: { len: dragCh.text.length, inTitle: dragCh.inTitle, fold: dragCh.fold.chapters },
      dblCh: { len: dblCh.text.length, inTitle: dblCh.inTitle, noFlash: dblCh.noFlash, flash: dblCh.flash, fold: dblCh.fold },
      ctrl: { preWindow: ctrlPreWindow, volFold: ctrlFoldVol, volUnfold: ctrlUnfoldVol, chFold: ctrlFoldCh },
      errs: errs.length }));
  await page.close();
}

await browser.close();
console.log('RESULT ' + JSON.stringify(results));
const failed = results.filter(r => !r.pass);
console.log('TOTAL=' + results.length + ' FAILED=' + failed.length);
process.exit(failed.length === 0 ? 0 : 1);