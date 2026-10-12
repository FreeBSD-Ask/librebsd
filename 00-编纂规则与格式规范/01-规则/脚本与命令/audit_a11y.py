# -*- coding: utf-8 -*-
"""audit_a11y.py —— 第二十二件门禁：目录页无障碍自动化审计（axe-core 无头扫描）。

设立缘由（2026-10-12，138 批 wave3 批 D；r66 审计 E5「本方案重点新增」）
------------------------------------------------------------------
本页人工无障碍审计已到收益递减点——静态结构（零 style=、零 on*=、img 有 alt、
按钮 aria-label 全覆盖）早已整治，**正因如此才需要自动化**：把 WCAG 2.x 规则
固化为常备门禁，防止回归。首跑即抓出两处真实缺陷（均于 138 批修复）：
  ① `.page-version` 对比度 serious（light 主题，accent＋opacity .55 → ~2.8:1）；
  ② `.opt-tools` 非 landmark（moderate region——顺手修复：aside 包裹）。

判据
----
A **axe 扫描**：四组合（1920×1080 / 390×844 × light/dark）`violations` 中
  `impact ∈ {critical, serious}` 数 = 0；moderate 记 INFO 不 FAIL（方案裁定，避免噪声）。
B **键盘契约**（E4-②，2026-09-19 审计处置项的回归守护）：`#exportMenu` 打开后
  聚焦首项按 ArrowDown/ArrowUp 焦点移动、Escape 关闭并归还焦点至触发钮、
  `aria-expanded` 同步。
C **媒体分支非空转**（E6）：forced-colors / prefers-contrast: more / prefers-reduced-motion
  三态下关键声明实测变化（现代层三个休眠分支不得空转）。
依赖与注入方式：axe.min.js 经 Playwright `addInitScript`（CDP 特权通道）注入——
**不受页面 CSP `script-src` 约束**（2026-10-12 实测：addScriptTag 被 nonce 策略拦截）。

用法
----
    python audit_a11y.py              # 0 通过 / 1 FAIL / 2 依赖缺失
    python audit_a11y.py --selftest   # 判据非空：缺陷副本（去 lang＋空按钮）须命中 serious/critical

依赖：node（PATH）＋ playwright 1.x（既有套件同路径）＋ 同目录 axe.min.js（4.14.0，MPL-2.0）。
"""
import argparse
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile

sys.stdout.reconfigure(encoding="utf-8")

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[2]
INDEX = REPO / "08-核查报告与多轮复核" / "重构2026" / "index.html"
AXE = HERE / "axe.min.js"
PLAYWRIGHT_ENTRY = ("file:///C:/Users/ykla/AppData/Roaming/npm/node_modules/"
                    "@executeautomation/playwright-mcp-server/node_modules/playwright/index.mjs")

RUNNER_JS = R'''
import { chromium } from '__PW__';
import { readFileSync } from 'node:fs';
const [INDEX, AXE_PATH] = process.argv.slice(2);
const AXE = readFileSync(AXE_PATH, 'utf8');
const FILE_URL = 'file:///' + INDEX.replace(/\\/g, '/');
const combos = [
  { w: 1920, h: 1080, theme: 'light' },
  { w: 1920, h: 1080, theme: 'dark' },
  { w: 390, h: 844, theme: 'light' },
  { w: 390, h: 844, theme: 'dark' },
];
const out = { combos: [], keyboard: null, media: null, errors: [] };
const browser = await chromium.launch({ headless: true });

async function newPage(w, h) {
  const page = await browser.newPage({ viewport: { width: w, height: h } });
  await page.addInitScript(() => { try { localStorage.setItem('sme-theme', ''); } catch (e) { } });
  await page.addInitScript({ content: AXE });
  page.on('pageerror', e => out.errors.push(String(e).slice(0, 120)));
  await page.goto(FILE_URL, { waitUntil: 'load' });
  await page.waitForTimeout(1200);
  return page;
}

for (const c of combos) {
  const page = await newPage(c.w, c.h);
  if (c.theme === 'dark') {
    await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'dark'));
  } else {
    await page.evaluate(() => document.documentElement.removeAttribute('data-theme'));
  }
  await page.waitForTimeout(300);
  const r = await page.evaluate(async () => {
    const res = await window.axe.run(document, { resultTypes: ['violations'] });
    return res.violations.map(v => ({ id: v.id, impact: v.impact, nodes: v.nodes.length,
      help: String(v.help).slice(0, 70), sample: (v.nodes[0] && (v.nodes[0].target || []).join(' ')) || '' }));
  });
  out.combos.push({ w: c.w, h: c.h, theme: c.theme, violations: r });
  await page.close();
}

/* B 键盘契约（1920 light；先展开工具栏——按钮默认折叠） */
{
  const page = await newPage(1920, 1080);
  try {
    await page.click('#optToolsToggle');
    await page.waitForTimeout(300);
    await page.click('#optExport');
    await page.waitForTimeout(250);
    out.keyboard = await page.evaluate(() => {
      const m = document.getElementById('exportMenu');
      const items = [].slice.call(m.querySelectorAll('[role="menuitem"]'));
      const trig = document.getElementById('optExport');
      const r = { opened: m.classList.contains('open'),
                  expanded: trig.getAttribute('aria-expanded'), n: items.length };
      items[0].focus();
      r.first = document.activeElement === items[0];
      items[0].dispatchEvent(new KeyboardEvent('keydown', { key: 'ArrowDown', bubbles: true }));
      r.afterDown = document.activeElement === items[1];
      items[1].dispatchEvent(new KeyboardEvent('keydown', { key: 'ArrowUp', bubbles: true }));
      r.afterUp = document.activeElement === items[0];
      items[0].dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', bubbles: true }));
      r.afterEsc = document.activeElement === trig;
      r.closed = !m.classList.contains('open');
      return r;
    });
  } catch (e) { out.errors.push('keyboard: ' + String(e).slice(0, 120)); }
  await page.close();
}

/* C 媒体分支（1920 light 页内切换 emulateMedia） */
{
  const page = await newPage(1920, 1080);
  try {
    const sample = () => page.evaluate(() => ({
      breadcrumbBorderTopColor: getComputedStyle(document.querySelector('.breadcrumb')).borderTopColor,
      muted: getComputedStyle(document.documentElement).getPropertyValue('--muted').trim(),
      scrollBehavior: getComputedStyle(document.documentElement).scrollBehavior,
    }));
    const normal = await sample();
    await page.emulateMedia({ forcedColors: 'active' });
    await page.waitForTimeout(250);
    const forced = await sample();
    await page.emulateMedia({ forcedColors: 'none', contrast: 'more' });
    await page.waitForTimeout(250);
    const contrast = await sample();
    await page.emulateMedia({ contrast: 'no-preference', reducedMotion: 'reduce' });
    await page.waitForTimeout(250);
    const reduced = await sample();
    out.media = { normal, forced, contrast, reduced };
  } catch (e) { out.errors.push('media: ' + String(e).slice(0, 120)); }
  await page.close();
}

await browser.close();
console.log('A11Y_JSON::' + JSON.stringify(out));
'''


def run_scan(index_path: pathlib.Path):
    """跑一次 JS 扫描器；返回解析后的 dict（或 None + 错误信息）。"""
    with tempfile.TemporaryDirectory(prefix="a11y_") as td:
        js = pathlib.Path(td) / "a11y_run.mjs"
        js.write_text(RUNNER_JS.replace("__PW__", PLAYWRIGHT_ENTRY), encoding="utf-8", newline="\n")
        p = subprocess.run(["node", str(js), str(index_path), str(AXE)],
                           capture_output=True, text=True, encoding="utf-8",
                           errors="replace", timeout=600)
        out = (p.stdout or "") + "\n" + (p.stderr or "")
        line = next((l for l in (p.stdout or "").splitlines() if l.startswith("A11Y_JSON::")), None)
        if not line:
            return None, out[-800:]
        try:
            return json.loads(line[len("A11Y_JSON::"):]), out[-400:]
        except Exception as e:
            return None, f"JSON 解析失败：{e}\n{out[-400:]}"


def brief(vs):
    return "；".join("%s/%s×%d" % (v["id"], v["impact"], v["nodes"]) for v in vs)


def judge(data):
    """A/B/C 判据求值，返回 (ok, lines)。"""
    ok = True
    lines = []
    # A
    sev = [(c, v) for c in data["combos"] for v in c["violations"]
           if v["impact"] in ("critical", "serious")]
    mods = [(c, v) for c in data["combos"] for v in c["violations"] if v["impact"] == "moderate"]
    if sev:
        ok = False
        lines.append("A axe 扫描: FAIL（critical/serious %d 处）：%s"
                     % (len(sev), brief([v for _, v in sev[:6]])))
    else:
        lines.append("A axe 扫描: PASS（4 组合 critical/serious = 0；moderate = %d）" % len(mods))
    if mods:
        lines.append("   INFO moderate: " + brief([v for _, v in mods[:6]]))
    # B
    kb = data.get("keyboard") or {}
    b_ok = all(kb.get(k) for k in ("opened", "first", "afterDown", "afterUp", "afterEsc", "closed")) \
        and kb.get("expanded") == "true"
    if not b_ok:
        ok = False
        lines.append("B 键盘契约: FAIL %s" % json.dumps(kb, ensure_ascii=False)[:200])
    else:
        lines.append("B 键盘契约: PASS（exportMenu 打开→首项聚焦→ArrowDown/ArrowUp 移动→Escape 关并归还焦点）")
    # C
    med = data.get("media") or {}
    try:
        n, f, ct, rd = med["normal"], med["forced"], med["contrast"], med["reduced"]
        # forced：breadcrumb 边框色 var(--line)=#ffc9df 应被 ButtonText（headless 解析 rgb(0,0,0)）接管；
        # contrast：--muted 加深；reduced：scroll-behavior smooth→auto（doc.css 休眠分支实测非空转）。
        c_ok = (n["breadcrumbBorderTopColor"] == "rgb(255, 201, 223)"
                and f["breadcrumbBorderTopColor"] == "rgb(0, 0, 0)"
                and n["muted"] != ct["muted"]
                and n["scrollBehavior"] == "smooth" and rd["scrollBehavior"] == "auto")
        detail = ("forced: breadcrumb border 色 %s→%s；contrast: --muted %s→%s；reduced: scroll-behavior %s→%s"
                  % (n["breadcrumbBorderTopColor"], f.get("breadcrumbBorderTopColor"),
                     n["muted"], ct.get("muted"), n["scrollBehavior"], rd.get("scrollBehavior")))
        if not c_ok:
            ok = False
            lines.append("C 媒体分支: FAIL " + detail)
        else:
            lines.append("C 媒体分支: PASS（" + detail + "）")
    except Exception as e:
        ok = False
        lines.append("C 媒体分支: FAIL（数据缺失：%s）" % e)
    if data.get("errors"):
        lines.append("   INFO 页面错误: " + "; ".join(data["errors"][:3]))
    return ok, lines


def cmd_selftest():
    """判据非空：缺陷副本（去 html lang ＋ 空按钮）须命中 html-has-lang(serious) 与 button-name(critical)。"""
    src = INDEX.read_text(encoding="utf-8")
    assert 'lang="zh-Hans"' in src, "夹具：未找到 html lang"
    broken = src.replace('lang="zh-Hans"', "", 1)
    # 探针陷阱（2026-10-12 首跑实录）：页面含两处 "</body>" 字面——其一在导出生成器的
    # JS 字符串 H.push('</body></html>') 内。若用 replace(…, 1) 会把缺陷按钮插进脚本字符串
    # （不在真实 DOM → button-name 不触发、selftest 假阴性）。必须以 rpartition 锚定最后一个
    # （DOM 层）关闭标记。
    assert broken.count("</body>") >= 1, "夹具：未找到 </body>"
    head, _, tail = broken.rpartition("</body>")
    broken = head + "<button></button></body>" + tail
    with tempfile.TemporaryDirectory(prefix="a11y_st_") as td:
        f = pathlib.Path(td) / "broken.html"
        f.write_text(broken, encoding="utf-8", newline="\n")
        data, tail = run_scan(f)
    if not data:
        print("selftest FAIL：扫描器未产出（%s）" % tail)
        return 1
    vs = [v for c in data["combos"] for v in c["violations"]]
    ids = {v["id"]: v["impact"] for v in vs}
    hits = (ids.get("html-has-lang") in ("serious", "critical")) and (ids.get("button-name") == "critical")
    print("selftest 结果：violations = %s" % brief(vs[:8]))
    print("  html-has-lang: %s ｜ button-name: %s" % (ids.get("html-has-lang"), ids.get("button-name")))
    print("判据非空自证：%s" % ("通过（去 lang＋空按钮均被对应规则拦下）" if hits else "**未通过**"))
    return 0 if hits else 1


def main():
    ap = argparse.ArgumentParser(description="第二十二件门禁：目录页无障碍自动化审计（axe-core）")
    ap.add_argument("--selftest", action="store_true", help="判据非空：缺陷副本须被拦下")
    args = ap.parse_args()

    if not shutil.which("node") and not pathlib.Path("C:/Program Files/nodejs/node.exe").exists():
        print("依赖缺失：node 不可用（exit 2）")
        return 2
    if not AXE.exists():
        print("依赖缺失：%s 不存在（exit 2）" % AXE)
        return 2
    pw = PLAYWRIGHT_ENTRY.replace("file:///", "")
    if not pathlib.Path(pw).exists():
        print("依赖缺失：playwright 入口不存在（%s）（exit 2）" % pw)
        return 2
    if not INDEX.exists():
        print("依赖缺失：index.html 不存在（exit 2）")
        return 2

    if args.selftest:
        return cmd_selftest()

    data, tail = run_scan(INDEX)
    if not data:
        print("扫描失败：%s" % tail)
        return 2
    ok, lines = judge(data)
    for l in lines:
        print(l)
    print("总判定: " + ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
