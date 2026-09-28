#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""audit_fixture_freshness.py —— 第十三件门禁：测试夹具新鲜度。

设立缘由（2026-09-28）
----------------------
`重构2026/tests/` 的浏览器套件里**写死**了若干随目录变动的数值，最典型是口径串
`43 卷 412 章 3435 节`（`full_matrix_regression.mjs` 两处、`visual_regression.mjs` 一处）
与溯源注计数 `注 537`（一处）。`tests/README.md` 已列明「夹具同步纪律」八条，但**同步靠人记**。

第九件门禁 `audit_page_assets.py` 的 E3 只验**编号集**（`tests/README.md` 的 T 编号 ↔
`record()` 调用）双向吻合，**不验数值新鲜度** → 内容源一改而夹具未改，套件会以陈旧夹具
静默误报或静默通过。

本件把「人记」变「机检」：从内容源 `data/outline.txt` **派生**真值，与夹具内写死值逐项比对。

判据
----
- **口径族**：夹具中出现的 `N 卷 N 章 N 节` 三元组须**唯一**且等于内容源派生值。
- **溯源注族**：夹具中出现的 `注 N` 须等于内容源 `@@` 定界数。

用法
----
    python audit_fixture_freshness.py                 # 0 通过 / 1 陈旧 / 2 依赖缺失
    python audit_fixture_freshness.py --tests-dir D   # 指定夹具目录（自检用）
    python audit_fixture_freshness.py --selftest      # 判据非空自检（造陈旧夹具，须 FAIL）

依赖：仅标准库。
"""
import argparse
import pathlib
import re
import shutil
import sys
import tempfile

sys.stdout.reconfigure(encoding="utf-8")

REPO = pathlib.Path(__file__).resolve().parents[3]
BASE = REPO / "08-核查报告与多轮复核" / "重构2026"
OUTLINE = BASE / "data" / "outline.txt"
TESTS = BASE / "tests"

TRIPLE_RE = re.compile(r"(\d+)\s*卷\s*(\d+)\s*章\s*(\d+)\s*节")
NOTE_RE = re.compile(r"注\s*(\d+)")

# ── 豁免（有意识的选择，非遗漏） ──────────────────────────────────────────
# 这些夹具**刻意**绑定历史快照，其数值不应等于现行口径。
# 豁免不等于免检：本件会断言「豁免项仍然需要豁免」——若某豁免文件已不再含非现行三元组，
# 即判 FAIL，逼人删除腐烂的豁免条目（防豁免清单随目录演进静默失效）。
EXEMPT_FILES = {
    "_regr_on_backup.mjs":
        "对历史备份件 script/_bak_index_before_batch1_20260912.html（2026-09-12，25 卷 233 章 1525 节）"
        "跑的回归，夹具须匹配该快照而非现行口径",
}


def derive_truth(outline: pathlib.Path):
    """内容源 → 真值。"""
    text = outline.read_text(encoding="utf-8")
    n_vol = n_ch = n_sec = n_src = 0
    for raw in text.split("\n"):
        line = raw.rstrip()
        if not line.strip():
            continue
        if line.startswith("# "):
            n_vol += 1
        elif line.startswith("## "):
            n_ch += 1
        elif line.startswith("- "):
            n_sec += 1
            if "@@" in line:
                n_src += 1
    return {"vol": n_vol, "ch": n_ch, "sec": n_sec, "src": n_src}


def scan_fixtures(tests: pathlib.Path):
    """夹具内写死值 → [(文件, 行号, 原文, 三元组 or 注计数)]。"""
    triples, notes = [], []
    for f in sorted(tests.glob("*.mjs")):
        for i, line in enumerate(f.read_text(encoding="utf-8").split("\n"), 1):
            for m in TRIPLE_RE.finditer(line):
                triples.append((f.name, i, m.group(0),
                                tuple(int(x) for x in m.groups())))
            for m in NOTE_RE.finditer(line):
                notes.append((f.name, i, m.group(0), int(m.group(1))))
    return triples, notes


def run(tests_dir: pathlib.Path, outline: pathlib.Path):
    truth = derive_truth(outline)
    triples_all, notes_all = scan_fixtures(tests_dir)
    # 按豁免分拣
    triples = [t for t in triples_all if t[0] not in EXEMPT_FILES]
    notes = [n for n in notes_all if n[0] not in EXEMPT_FILES]
    rows = []

    # 口径族
    want = (truth["vol"], truth["ch"], truth["sec"])
    bad = [t for t in triples if t[3] != want]
    stale = sorted({t[2] for t in bad})
    rows.append((
        "口径族",
        "夹具中 N 卷 N 章 N 节 须唯一且 = 内容源派生值",
        not bad,
        "内容源 = %d 卷 %d 章 %d 节；非豁免命中 %d 处%s"
        % (want[0], want[1], want[2], len(triples),
           "" if not bad else "；陈旧值 %s（%s）"
           % (", ".join(stale),
              ", ".join("%s:%d" % (b[0], b[1]) for b in bad))),
    ))

    # 溯源注族
    want_n = truth["src"]
    bad_n = [n for n in notes if n[3] != want_n]
    rows.append((
        "溯源注族",
        "夹具中 注 N 须 = 内容源 @@ 定界数",
        not bad_n,
        "内容源 = 注 %d；非豁免命中 %d 处%s"
        % (want_n, len(notes),
           "" if not bad_n else "；陈旧值 %s（%s）"
           % (", ".join(sorted({n[2] for n in bad_n})),
              ", ".join("%s:%d" % (n[0], n[1]) for n in bad_n))),
    ))

    # 豁免防腐烂：豁免文件必须存在，且必须仍然含非现行三元组
    gone, rotten = [], []
    for name in EXEMPT_FILES:
        if not (tests_dir / name).exists():
            gone.append(name)
            continue
        hits = [t for t in triples_all if t[0] == name and t[3] != want]
        if not hits:
            rotten.append(name)
    rows.append((
        "豁免防腐烂",
        "每条豁免须仍存在且仍含非现行三元组（否则删除该豁免）",
        not gone and not rotten,
        "豁免 %d 条%s%s" % (
            len(EXEMPT_FILES),
            "" if not gone else "；文件已不存在：%s" % ", ".join(gone),
            "" if not rotten else "；已无需豁免（须删条目）：%s" % ", ".join(rotten)),
    ))

    # 覆盖度：夹具里若一处都没有，判据为空
    rows.append((
        "判据覆盖",
        "非豁免夹具中至少各命中一处（否则判据空转）",
        bool(triples) and bool(notes),
        "口径命中 %d 处、注命中 %d 处" % (len(triples), len(notes)),
    ))
    return rows, triples_all, notes_all


def _report(rows, title):
    print("=" * 72)
    print(title)
    print("=" * 72)
    fails = 0
    for name, desc, ok, detail in rows:
        print("  [%s] %-8s %s" % ("PASS" if ok else "FAIL", name, desc))
        print("           %s" % detail)
        if not ok:
            fails += 1
    print("-" * 72)
    print("  合计 %d 项，FAIL %d 项" % (len(rows), fails))
    return fails


def cmd_selftest():
    """判据非空：把夹具复制一份并把口径串改成陈旧值，须 FAIL。"""
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="fixfresh_"))
    try:
        for f in TESTS.glob("*.mjs"):
            shutil.copy2(f, tmp / f.name)
        truth = derive_truth(OUTLINE)
        want = "%d 卷 %d 章 %d 节" % (truth["vol"], truth["ch"], truth["sec"])
        stale = "%d 卷 %d 章 %d 节" % (truth["vol"] - 1, truth["ch"], truth["sec"])
        hit = 0
        for f in tmp.glob("*.mjs"):
            s = f.read_text(encoding="utf-8")
            if want in s:
                f.write_text(s.replace(want, stale), encoding="utf-8")
                hit += 1
        if hit == 0:
            print("自检无法构造：夹具中未找到口径串 %r" % want, file=sys.stderr)
            return 2
        rows, _t, _n = run(tmp, OUTLINE)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    fails = _report(rows, "判据非空自检：夹具口径串改为陈旧值（预期 口径族 FAIL）")
    if fails >= 1 and any(not ok and n == "口径族" for n, _d, ok, _x in rows):
        print("  ✅ 判据非空：陈旧口径被命中（改了 %d 个夹具文件）" % hit)
        return 0
    print("  ❌ 判据可能为空：陈旧口径未被命中", file=sys.stderr)
    return 1


def main():
    ap = argparse.ArgumentParser(description="测试夹具新鲜度门禁（第十三件）")
    ap.add_argument("--tests-dir", default=str(TESTS))
    ap.add_argument("--outline", default=str(OUTLINE))
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        return cmd_selftest()

    tests = pathlib.Path(args.tests_dir)
    outline = pathlib.Path(args.outline)
    for p, what in ((tests, "夹具目录"), (outline, "内容源")):
        if not p.exists():
            print("依赖缺失：%s 不存在（%s）" % (p, what), file=sys.stderr)
            return 2
    rows, triples_all, notes_all = run(tests, outline)
    fails = _report(rows, "测试夹具新鲜度门禁（第十三件）：%s" % tests)
    if EXEMPT_FILES:
        print()
        print("  豁免（有意识的选择，非遗漏；本件已断言其「仍需要豁免」）：")
        for name, why in sorted(EXEMPT_FILES.items()):
            hits = sorted({t[2] for t in triples_all if t[0] == name})
            print("    %-24s %s" % (name, why))
            print("    %-24s 命中值：%s" % ("", ", ".join(hits) or "（无）"))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
