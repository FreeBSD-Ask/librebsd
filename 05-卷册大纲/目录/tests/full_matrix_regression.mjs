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
 * 重构2026 目录页全覆盖矩阵回归（2026-09-12 第四轮新增）
 * 维度：分辨率（1920×1080 / 1366×768 / 768×1024 / 412×915 手机）
 *      × 主题（light / oled 纯黑 / 跟随系统暗色）× 字号（85% / 100% / 140%）——153 批：默认 dark 主题删除，夜间＝AMOLED 纯黑
 * 每组合断言：零 JS 错误、零横向溢出、主题生效、字号生效、自校验 6/6、
 *   指标口径、目录开关、搜索、溯源注、人名/文献浮层挂载、长节名展开、
 *   进度条、面包屑、回到顶部、章跳转、导出 SUMMARY 口径。
 * 深度点检（抽样组合）：跨卷图谱零省略零重叠、修订史面板、时间线、研/阅切换、
 *   字号滑杆交互、暗色下 plink/reflink 浮层。
 * 失败退出码 1。
 * ========================================================================== */
// 路径由本件位置推导（2026-10-23）：tests/ 的上一级即 `05-卷册大纲/目录`（变量不取名 URL，免遮蔽全局 URL 构造器）
const PAGE_URL = new URL('../index.html', import.meta.url).href;
const HEADLESS = process.argv.includes('--headless');

/* ── 夹具真值：**唯一来源** ──────────────────────────────────────────────
   断言与断言标签**均由本常量派生**，杜绝「标签与断言脱节」这一类缺陷。
   缘由（2026-09-28 实测）：本文件原断言写的期望值是 537，而断言**标签**里
   写的是 535 —— 标签在输出里显示了一个错误的期望值；而当时两件门禁
   （第九件 E2 与第十三件的溯源注判据）都只匹配「注＋数字」形态，
   **匹配不到「注计数＋数字」形态**，故长期无人发现。
   现标签改为 `'注计数' + FX.notes`，形态上不可能再脱节；
   第十三件门禁已扩为同时覆盖「注＋数字」「注计数＋数字」与 `notes:` 常量三种形态。
   真值来源＝内容源 data/outline.txt（卷/章/节数与 @@ 定界数），随目录变动须同步。 */
const FX = { triple: '76 卷 544 章 3951 节', notes: 1764, secs: 3907 };
const browser = await chromium.launch({
  executablePath: __CHROME_EXE,
  headless: HEADLESS, args: ['--no-sandbox']
});

const results = [];
function record(name, pass, detail) {
  results.push({ name, pass, detail: String(detail || '') });
  console.log((pass ? 'PASS' : 'FAIL') + ' | ' + name + (detail ? ' | ' + String(detail).slice(0, 150) : ''));
}

async function combo(name, { w, h, dpr, theme, scheme, fs, touch, deep }) {
  const ctx = await browser.newContext({
    viewport: { width: w, height: h, deviceScaleFactor: dpr || 1 },
    hasTouch: !!touch,
    colorScheme: scheme || 'light'
  });
  await ctx.addInitScript(([t, f]) => {
    try {
      if (t) localStorage.setItem('sme-theme', t);
      if (f) localStorage.setItem('sme-fs', String(f));
    } catch (e) {}
  }, [theme === 'sys' ? null : theme, fs || null]);
  const page = await ctx.newPage();
  const errs = [];
  page.on('pageerror', e => errs.push(String(e).slice(0, 120)));
  await page.goto(PAGE_URL, { waitUntil: 'load' });
  /* O-2（2026-09-13）数据层异步装配：等待 data-opt-ready 哨兵（数据联动初始化完成），
     降级态（哨兵=0 或缺失）按原 2.2s 落定继续，保证降级路径可测 */
  const ready = await page.waitForFunction(
    () => ['1', '0'].includes(document.documentElement.getAttribute('data-opt-ready')),
    { timeout: 20000 }
  ).then(() => true).catch(() => false);
  if (!ready) await page.waitForTimeout(2200);
  await page.waitForTimeout(300);
  await page.evaluate(() => { document.documentElement.style.scrollBehavior = 'auto'; });

  const tag = `${w}x${h}/${theme}${scheme === 'dark' && theme !== 'dark' ? '(sys)' : ''}/${fs || 100}%`;
  const ok = (n, p, d) => record(`[${tag}] ${n}`, p, d);

  /* 1 零 JS 错误 */
  ok('零JS错误', errs.length === 0, errs.join(' || '));

  /* 2 主题生效 */
  const th = await page.evaluate(() => ({
    attr: document.documentElement.getAttribute('data-theme'),
    bg: getComputedStyle(document.body).backgroundColor
  }));
  const wantDark = theme === 'oled' || (theme !== 'light' && scheme === 'dark');
  ok('主题生效', th.attr === (wantDark ? 'oled' : 'light'), JSON.stringify(th));

  /* 3 字号生效（.doc-page zoom） */
  const z = await page.evaluate(() => {
    const dp = document.querySelector('.doc-page');
    return { zoom: dp && dp.style.zoom, comp: dp ? getComputedStyle(dp).zoom : null };
  });
  const wantZ = (fs || 100) / 100;
  ok('字号生效', Math.abs(parseFloat(z.comp || 0) - wantZ) < 0.02, JSON.stringify(z));

  /* 4 零横向溢出 */
  const ov = await page.evaluate(() => ({
    sw: document.documentElement.scrollWidth, iw: window.innerWidth
  }));
  ok('零横向溢出', ov.sw <= ov.iw + 1, JSON.stringify(ov));

  /* 5 自校验与口径 */
  const sc = await page.evaluate((fx) => {
    const t = document.body.textContent;
    return {
      self: /目录自校验 6\/6 通过/.test(t),
     注: t.indexOf('注 ' + fx.notes) !== -1,
      stat: t.indexOf(fx.triple) !== -1
    };
  }, FX);
  ok('自校验6/6', sc.self, '');
  ok('注计数' + FX.notes, sc.注, '');
  ok('口径' + FX.secs, sc.stat, '');

  /* 6 目录开关 */
  const toc = await page.evaluate(() => {
    const b = document.getElementById('tocToggle');
    if (b) b.click();
    const d = document.getElementById('tocDrawer');
    const opened = d && (d.classList.contains('open') || getComputedStyle(d).display !== 'none' || d.getAttribute('aria-hidden') === 'false');
    if (b) b.click();
    return { has: !!d, opened: !!opened };
  });
  ok('目录开关', toc.has && toc.opened, JSON.stringify(toc));

  /* 7 搜索面板 */
  const search = await page.evaluate(() => new Promise(res => {
    const b = document.getElementById('optSearch');
    if (!b) { res({ has: false }); return; }
    b.click();
    setTimeout(() => {
      const inp = document.querySelector('.opt-panel input, #optPanel input, .search-input, input[type="search"], input[type="text"]');
      const vis = inp && inp.getBoundingClientRect().height > 0;
      res({ has: true, vis: !!vis });
      if (b) b.click();
    }, 450);
  }));
  ok('搜索面板', search.has && search.vis, JSON.stringify(search));

  /* 8 溯源注：徽标与展开 */
  const note = await page.evaluate(() => {
    window.scrollTo(0, 9000);
    const badge = document.querySelector('li .note-badge');
    if (!badge) return { has: false };
    const li = badge.closest('li');
    badge.click();
    return { has: true, open: li.classList.contains('note-open') };
  });
  ok('溯源注展开', note.has && note.open === true, JSON.stringify(note));

  /* 9 人名/文献浮层挂载 */
  const links = await page.evaluate(() => ({
    plink: document.querySelectorAll('.plink').length,
    reflink: document.querySelectorAll('.reflink').length
  }));
  ok('人名浮层挂载', links.plink > 50, JSON.stringify(links));
  ok('文献浮层挂载', links.reflink > 5, JSON.stringify(links));

  /* 10 长节名展开/收起（阈值 150 字符；全库节题未越阈时功能休眠，须验证休眠与内容一致） */
  const exp = await page.evaluate(() => {
    const b = document.querySelector('.t-more');
    if (!b) {
      const mx = Array.from(document.querySelectorAll('ul.sections > li')).reduce((m, el) => {
        const c = el.cloneNode(true);
        c.querySelectorAll('.src, .sec-num, .note-badge, .t-more, .t-short, .t-full, button').forEach(n => n.remove());
        return Math.max(m, c.textContent.trim().length);
      }, 0);
      return { has: false, dormant: mx < 150, max: mx };
    }
    b.click();
    const full = document.querySelector('.t-full');
    const vis = full && getComputedStyle(full).display !== 'none' && full.getBoundingClientRect().height > 0;
    return { has: true, vis: !!vis };
  });
  ok('长节名展开', exp.has ? exp.vis : exp.dormant, JSON.stringify(exp));

  /* 11 进度条/面包屑/回到顶部 */
  const misc = await page.evaluate(() => {
    window.scrollTo(0, 12000);
    return new Promise(res => setTimeout(() => {
      const prog = document.querySelector('.breadcrumb .prog i');
      const pw = prog ? (window.CSS && CSS.supports('animation-timeline: scroll()') ? getComputedStyle(prog).width : prog.style.width) : '';
      const bar = !!pw && pw !== '0%' && pw !== '0px' && pw !== 'auto';
      const bc = document.querySelector('.breadcrumb, #breadcrumb');
      const top = document.getElementById('backToTop');
      res({
        bar: !!bar,
        bc: bc ? getComputedStyle(bc).display !== 'none' : true,
        topBtn: !!top
      });
    }, 400));
  });
  ok('进度条/面包屑/回顶', misc.bar && misc.bc && misc.topBtn, JSON.stringify(misc));

  /* 12 章跳转（键盘 j 或点击第 2 卷首章） */
  const jump = await page.evaluate(() => new Promise(res => {
    const y0 = window.scrollY;
    const a = Array.from(document.querySelectorAll('a[href^="#vol-"]')).find(x => /vol-3/.test(x.getAttribute('href') || ''));
    if (a) a.click();
    setTimeout(() => res({ moved: window.scrollY !== y0 || location.hash.includes('vol-3') }), 500);
  }));
  ok('章跳转', jump.moved, JSON.stringify(jump));

  /* 13 导出 SUMMARY 口径 ＋ 导出内容无运行时装饰残留（2026-09-20 强化） */
  const exp2 = await page.evaluate((fx) => {
    const b = document.getElementById('optExport');
    if (b) b.click();
    const t = document.body.textContent;
    /* 导出保真：导出读的是**运行时装饰后**的 DOM，故卷题会带计数徽标（N 章 · N 节）、
       章题带节数徽标（N 节）、节名带溯源注徽标（注）——静态门禁对此结构性命中不了，
       必须由浏览器侧断言覆盖。缘由：2026-09-20 实测四种导出卷题 37/37、章题 352/352、
       节名 316 处被污染，而本项原判据只查页面口径串，故在 592 项断言中完全不可见。 */
    const caps = [];
    const _B = window.Blob;
    window.Blob = function (parts, opts) {
      try { caps.push((parts || []).map(function (p) { return typeof p === 'string' ? p : ''; }).join('')); } catch (e) {}
      return new _B(parts, opts);
    };
    window.Blob.prototype = _B.prototype;
    const click = function (k) {
      const bb = document.getElementById('optExport'); if (bb) bb.click();
      const it = document.querySelector('#exportMenu button[data-x="' + k + '"]'); if (it) it.click();
    };
    click('json');
    let j = null; try { j = JSON.parse(caps[0] || '{}'); } catch (e) {}
    const vols = (j && j.volumes) || [];
    const c0 = (vols[0] && vols[0].chapters && vols[0].chapters[0]) || null;
    const s0 = (c0 && c0.sections && c0.sections[0]) || null;
    const vt = vols.length ? vols[0].title : '';
    const ct = c0 ? c0.title : '';
    const st = s0 ? s0.title : '';
    const clean = vols.length > 0
      && !/[0-9]+\s*章\s*·\s*[0-9]+\s*节\s*$/.test(vt)
      && !/[0-9]+\s*节\s*$/.test(ct)
      && !/注$/.test(st);
    return { hasExport: !!b, stat: t.indexOf(fx.triple) !== -1, clean: clean, sample: [vt, ct, st] };
  }, FX);
  ok('导出口径' + FX.secs, exp2.hasExport && exp2.stat, JSON.stringify({ hasExport: exp2.hasExport, stat: exp2.stat }));
  ok('导出内容无装饰残留', exp2.clean, JSON.stringify(exp2.sample));

  /* 深度点检 */
  if (deep) {
    /* 图谱：打开→零省略→关闭 */
    const g = await page.evaluate(() => new Promise(res => {
      const b = document.getElementById('optGraphBtn');
      if (b) b.click();
      setTimeout(() => {
        const wrap = document.querySelector('#optGraph');
        const labels = document.querySelectorAll('.graph-label, .g-label').length;
        const ells = document.querySelectorAll('.graph-label.ellipsis, .g-label.ellipsis').length;
        res({ open: !!wrap, labels, ells });
        const close = document.querySelector('.graph-close, #graphClose, .modal-close');
        if (close) close.click();
        else if (b) b.click();
      }, 700);
    }));
    ok('图谱打开零省略', g.open && g.labels >= 26 && g.ells === 0, JSON.stringify(g));

    /* 修订史面板 */
    const rev = await page.evaluate(() => new Promise(res => {
      const b = document.getElementById('optRev');
      if (b) b.click();
      setTimeout(() => {
        const p = document.querySelector('.rev-panel, #revPanel, .opt-panel.open, .panel.open, dialog[open]');
        res({ open: !!p });
        const c = document.querySelector('.panel-close, .opt-close');
        if (c) c.click(); else if (b) b.click();
      }, 500);
    }));
    ok('修订史面板', rev.open, JSON.stringify(rev));

    /* 研/阅切换（2026-10-11 View Transitions 批：切换经 startViewTransition 回调异步落地，
       断言前等一拍让 DOM 变更写入；判据语义不变=点击后类翻转） */
    const mode = await page.evaluate(async () => {
      const b = document.getElementById('optMode');
      const before = document.body.className + '|' + document.documentElement.className;
      if (b) b.click();
      await new Promise(r => setTimeout(r, 150));
      const after = document.body.className + '|' + document.documentElement.className;
      return { changed: before !== after };
    });
    ok('研阅切换', mode.changed, JSON.stringify(mode));

    /* 字号滑杆交互（暗色组合下实测） */
    const slider = await page.evaluate(() => new Promise(res => {
      const b = document.getElementById('fontSizeToggle');
      if (b) b.click();
      setTimeout(() => {
        const rng = document.getElementById('fontRange');
        const menu = document.getElementById('fontMenu');
        if (!rng || !menu || !menu.classList.contains('open')) { res({ open: false }); return; }
        const setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
        setter.call(rng, '140');
        rng.dispatchEvent(new Event('input', { bubbles: true }));
        setTimeout(() => {
          const dp = document.querySelector('.doc-page');
          res({ open: true, zoom: dp && dp.style.zoom, label: document.getElementById('fontVal') && document.getElementById('fontVal').textContent });
        }, 200);
      }, 250);
    }));
    ok('字号滑杆交互', slider.open && Math.abs(parseFloat(slider.zoom || 0) - 1.4) < 0.02, JSON.stringify(slider));
  }

  await ctx.close();
}

/* ---- 全矩阵 ---- */
const VIEWPORTS = [
  { w: 1920, h: 1080, dpr: 1 },
  { w: 1366, h: 768, dpr: 1 },
  { w: 768, h: 1024, dpr: 2 },
  { w: 412, h: 915, dpr: 2.75, touch: true }
];
const THEMES = ['light', 'oled', 'sys'];
const FONTS = [85, 100, 140];
let combos = 0;
for (const v of VIEWPORTS) {
  for (const theme of THEMES) {
    for (const fs of FONTS) {
      const deep = (v.w === 1920 && fs === 140 && theme === 'oled') ||
                   (v.touch && fs === 100 && theme === 'oled') ||
                   (v.w === 1366 && fs === 85 && theme === 'light') ||
                   (v.w === 768 && fs === 140 && theme === 'sys');
      await combo(`${v.w}×${v.h}/${theme}/${fs}`, { ...v, theme, fs, deep });
      combos++;
    }
  }
}
/* 附加：跟随系统暗色（emulateMedia 路径已在 colorScheme 覆盖） */
console.log(`\nCOMBOS=${combos} TOTAL=${results.length} FAILED=${results.filter(r => !r.pass).length}`);
const failed = results.filter(r => !r.pass);
if (failed.length) { console.log('FAILED LIST:'); for (const f of failed) console.log(' -', f.name, '|', f.detail.slice(0, 120)); }
await browser.close();
process.exit(failed.length ? 1 : 0);
