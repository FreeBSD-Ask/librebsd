// 151 批主题探针：四态 data-theme 计算样式 + 修订面板数据 + 媒体回落 + 深检序列复现
import { chromium } from './_pw_loader.mjs';
import path from 'node:path';

const FILE_URL = () => 'file:///' + path.resolve('index.html').replace(/\\/g, '/');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto(FILE_URL());
  await page.waitForTimeout(1200);
  const out = {};
  for (const t of ['light', 'oled', 'eink']) {
    out[t] = await page.evaluate((theme) => {
      document.documentElement.setAttribute('data-theme', theme);
      const cs = getComputedStyle(document.body);
      const before = getComputedStyle(document.body, '::before');
      return {
        bodyBg: cs.backgroundColor, color: cs.color,
        beforeImg: before.backgroundImage.slice(0, 40),
        btnGlyph: document.getElementById('themeToggle').textContent,
        meta: document.querySelector('meta[name="theme-color"]').getAttribute('content'),
      };
    }, t);
  }
  await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'light'));
  const cycle = [];
  for (let i = 0; i < 5; i++) {
    await page.click('#themeToggle');
    await page.waitForTimeout(120);
    cycle.push(await page.evaluate(() => document.documentElement.getAttribute('data-theme') + ':' + document.getElementById('themeToggle').textContent));
  }
  out.cycle = cycle;
  out.persist = await page.evaluate(() => localStorage.getItem('sme-theme'));
  const rev = await page.evaluate(() => {
    document.getElementById('optRev').click();
    const dlg = document.getElementById('optPanelRev');
    return {
      rows: dlg.querySelectorAll('tbody tr').length,
      lastRow: dlg.querySelector('tbody tr:last-child').textContent.trim().slice(0, 80),
      hints: Array.from(dlg.querySelectorAll('.hint')).map((h) => h.textContent.trim()),
    };
  });
  out.rev = rev;
  out.mediaRule = await page.evaluate(() => {
    let found = false;
    for (const ss of document.styleSheets) {
      try {
        for (const r of ss.cssRules) {
          if (r.media && /monochrome|update:\s*slow/.test(r.media.mediaText)) found = r.media.mediaText;
        }
      } catch (e) {}
    }
    return found;
  });
  await page.close();

  // 复现矩阵深检序列：dark + 140% + 1920
  const page2 = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1.4, colorScheme: 'light' });
  await page2.addInitScript(() => { try { localStorage.setItem('sme-theme', 'oled'); } catch (e) {} });
  await page2.goto(FILE_URL());
  await page2.waitForFunction(() => ['1', '0'].includes(document.documentElement.getAttribute('data-opt-ready')), { timeout: 20000 }).catch(() => {});
  await page2.waitForTimeout(300);
  const seq = await page2.evaluate(async () => {
    const log = {};
    const bG = document.getElementById('optGraphBtn');
    if (bG) bG.click();
    await new Promise(r => setTimeout(r, 700));
    const gc = document.querySelector('.graph-close, #graphClose, .modal-close');
    if (gc) gc.click(); else if (bG) bG.click();
    await new Promise(r => setTimeout(r, 100));
    const b = document.getElementById('optRev');
    if (b) b.click();
    await new Promise(r => setTimeout(r, 500));
    const dlg = document.querySelector('#optPanelRev');
    log.revOpen = !!(dlg && dlg.open);
    log.revRows = dlg ? dlg.querySelectorAll('tbody tr').length : 0;
    log.closeBtn = !!document.querySelector('.panel-close, .opt-close');
    const c = document.querySelector('.panel-close, .opt-close');
    if (c) c.click(); else if (b) b.click();
    await new Promise(r => setTimeout(r, 100));
    log.revOpenAfterClose = !!(dlg && dlg.open);
    const bm = document.getElementById('optMode');
    const before = document.body.className;
    bm.click();
    await new Promise(r => setTimeout(r, 150));
    log.modeBefore = before;
    log.modeAfter = document.body.className;
    log.changed = before !== document.body.className;
    log.vtSupported = typeof document.startViewTransition === 'function';
    return log;
  });
  out.seq = seq;
  await page2.close();
  console.log(JSON.stringify(out, null, 1));
  await browser.close();
})();
