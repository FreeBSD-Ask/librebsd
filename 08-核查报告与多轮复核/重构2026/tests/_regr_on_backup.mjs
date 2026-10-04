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

/* ============================================================================
 * 重构2026 目录页视觉回归套件（2026-09-11 固化，期三）
 * 用法：node tests/visual_regression.mjs
 * 环境：需本机 playwright（借道 @executeautomation/playwright-mcp-server 树内安装）
 *       与 ms-playwright chromium-1200；无头/有头由下方 HEADLESS 开关控制。
 * 断言：17 项视觉几何 + 功能断言（TOC 跟随可见性、浮层、折叠、图谱、进度条、
 *       键盘、抽屉、SUMMARY 导出）。失败退出码 1，供 CI/本地「改后必跑」使用。
 * ========================================================================== */
const URL = 'file:///D:/librebsd/script/_bak_index_before_batch1_20260912.html';
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

async function newPage(w, h, dpr) {
  const page = await browser.newPage({
    viewport: { width: w, height: h, deviceScaleFactor: dpr || 1 },
    hasTouch: w < 900
  });
  const errs = [];
  page.on('pageerror', e => errs.push(String(e).slice(0, 140)));
  await page.goto(URL, { waitUntil: 'load' });
  await page.waitForTimeout(2500);
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

  /* T5：长节名折叠 */
  const longRes = await page.evaluate(() => {
    const li = document.querySelector('li.long-title');
    if (!li) return 'none';
    const btn = li.querySelector('.t-more');
    btn.click();
    return li.classList.contains('open') ? 'open' : 'closed';
  });
  record('T5 长节名展开/收起', longRes === 'open', longRes);

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
  const graph = await page.evaluate(() => {
    const labels = Array.from(document.querySelectorAll('#optGraph text.graph-label'));
    let hasEllipsis = 0;
    labels.forEach(t => { if (t.textContent.includes('…')) hasEllipsis++; });
    // 完整性与无省略：标签文本应含各卷短名
    const missing = [];
    document.querySelectorAll("section[id^='vol-'] > h2").forEach(h2 => {
      const t = h2.textContent.trim();
      const short = t.indexOf('　') >= 0 ? t.slice(t.indexOf('　') + 1) : t;
      let found = false;
      labels.forEach(l => { if (l.textContent.replace(/\s+/g, '').includes(short.replace(/\s+/g, ''))) found = true; });
      if (!found) missing.push(short.slice(0, 10));
    });
    let overlaps = 0;
    for (let i = 0; i < labels.length; i++) for (let j = i + 1; j < labels.length; j++) {
      const a = labels[i].getBoundingClientRect(), b = labels[j].getBoundingClientRect();
      if (a.x < b.x + b.width && a.x + a.width > b.x && a.y < b.y + b.height && a.y + a.height > b.y) overlaps++;
    }
    return { labels: labels.length, hasEllipsis, missing, overlaps };
  });
  console.log('GRAPH_RAW', JSON.stringify(graph));
  record('T7a 图谱标签完整显示（无省略）', graph.labels === 25 && graph.hasEllipsis === 0 && graph.missing.length === 0, 'labels=' + graph.labels + ' ellipsis=' + graph.hasEllipsis + ' missing=' + graph.missing.length);
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
    return i ? i.style.width : 'none';
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
  await page.waitForTimeout(500);
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
  await page.evaluate(() => { document.getElementById('tocDrawer').classList.remove('open'); document.body.style.overflow = ''; });
  await page.waitForTimeout(300);

  /* T12：手机图谱完整无省略 */
  await page.evaluate(() => document.getElementById('optGraphBtn').click());
  await page.waitForTimeout(500);
  const gPhone = await page.evaluate(() => {
    const labels = Array.from(document.querySelectorAll('#optGraph text.graph-label'));
    return {
      labels: labels.length,
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
  record('T12 手机图谱完整零重叠', gPhone.labels === 25 && gPhone.ellipsis === 0 && gPhone.overlaps === 0, JSON.stringify(gPhone));
  await page.screenshot({ path: SHOT + 'headful_graph_phone.png' });
  await page.keyboard.press('Escape');

  record('手机 JS 错误', errs.length === 0, errs.join('; '));
  await page.close();
}

/* ============ 视口 C：窄屏抽屉 + summary + 主题持久化 ============ */
{
  const { page, errs } = await newPage(820, 1180, 1);
  const summary = await page.evaluate(() => {
    const t = window.exportSummaryText();
    return { len: t.split('\n').length, hasStats: /统计：25 卷 233 章 1525 节/.test(t) };
  });
  record('T13 SUMMARY 导出内容', summary.len > 1800 && summary.hasStats, JSON.stringify(summary));
  await page.close();
}

await browser.close();
console.log('RESULT ' + JSON.stringify(results));
const failed = results.filter(r => !r.pass);
console.log('TOTAL=' + results.length + ' FAILED=' + failed.length);
process.exit(failed.length === 0 ? 0 : 1);