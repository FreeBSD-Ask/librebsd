# -*- coding: utf-8 -*-
"""BEGIN/END 成对锚的**章内配对**审计（TD-022 裁定 6 复核件；第三十四件）。

背景与判据（TD-022 判据书 §四 D4 修订，2026-10-22）：
  1. **作用域＝章**：配对在 `卷/章` 内完成；跨章配对视为异常（跨文件、跨节目录合法）。
  2. **排序＝节号数值序**：目录名与文件名前缀 `\\d+(\\.\\d+)*` 解析为整数元组后比较。
     不得按相对路径字典序——实测 `005.0.10-…` 字典序排在 `005.0.9-…` 之前，会把
     1 处错位累积放大成数十条“跨卷”伪报（159 批 77 项中 75 项由此产生）。
  3. **形态覆盖**：`FAM:BEGIN`／`FAM:END` 与中文 `FAM:开始`／`FAM:结束` 同族同判；
     `ROW_MINE`／`DEEP_ANALYSIS` 单锚不参与；含 `close`（`/FAM`）的 block 家族由
     `audit_anchor_pairs.py` 判平，本脚本跳过。

判据：
  P1 章内孤儿 END（无前置未配 BEGIN）→ FAIL
  P2 章内未配 BEGIN（章末仍挂起）→ FAIL
  P3 跨章配对 → 记账时即表现为 P1＋P2（拆分到两章各一条），不另设判据
  P4 未闭合注释 `<!--`（多行感知剥离后仍残留）→ FAIL

只读：不写树、不写库。退出码 0／1（--check 命中）／2（根目录缺失）。
`--csv` 落异常明细；`--selftest` 正负夹具（含“字典序会产生伪报”的负向对照）。
"""
import argparse
import csv
import re
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
DEFAULT_ROOT = REPO / "05-卷册大纲"

COMMENT_RE = re.compile(r"<!--(.*?)-->", re.S)
SINGLE_ANCHOR = ("ROW_MINE", "DEEP_ANALYSIS")
FAM_RE = re.compile(r"[A-Za-z0-9_\-]+")
FULL_COMMENT_RE = COMMENT_RE


def family_of(body):
    """返回 (family, kind)；kind ∈ begin/end/open/close；无关者返回 (None, None)。"""
    b = body.strip()
    if not b:
        return None, None
    first = b.split()[0]
    if first.startswith("/"):
        fam = first[1:].split(":")[0]
        if fam and fam not in SINGLE_ANCHOR and FAM_RE.fullmatch(fam):
            return fam, "close"
        return None, None
    if ":" in first:
        fam, tok = first.split(":", 1)
        tok = tok.strip()
        if not fam or fam in SINGLE_ANCHOR or not FAM_RE.fullmatch(fam):
            return None, None
        if tok.upper() == "BEGIN" or tok == "开始":
            return fam, "begin"
        if tok.upper() == "END" or tok == "结束":
            return fam, "end"
        return fam, "open"
    if first in SINGLE_ANCHOR or not FAM_RE.fullmatch(first):
        return None, None
    return first, "open"


def num_tuple(name):
    m = re.match(r"(\d+(?:\.\d+)*)", name)
    return tuple(int(x) for x in m.group(1).split(".")) if m else (10 ** 9,)


def head_num(name):
    m = re.search(r"(\d+)", name)
    return int(m.group(1)) if m else 10 ** 9


def chapter_key(rel):
    parts = rel.split("/")
    return (head_num(parts[0]), head_num(parts[1]) if len(parts) > 1 else 0)


def order_key(rel, line):
    """章内排序键：目录节号 → 文件节号 → 文件名 → 行号。"""
    parts = rel.split("/")
    dsec = num_tuple(parts[-2]) if len(parts) > 2 else (0,)
    fsec = num_tuple(parts[-1])
    return (dsec, fsec, parts[-1], line)


def order_key_lexicographic(rel, line):
    """仅用于自检负向对照：字典序（复现伪报）。"""
    return (rel, line)


def has_unclosed(text):
    return "<!--" in FULL_COMMENT_RE.sub("", text)


def collect(root):
    """返回 markers[(fam, rel, line)] = kind，以及 kinds[fam] 集合。"""
    markers, kinds = {}, {}
    for p in sorted(Path(root).rglob("*.md")):
        rel = p.relative_to(root).as_posix()
        if "/" not in rel:
            continue
        text = p.read_text(encoding="utf-8")
        for m in COMMENT_RE.finditer(text):
            fam, kind = family_of(m.group(1))
            if not fam:
                continue
            kinds.setdefault(fam, set()).add(kind)
            if kind in ("begin", "end"):
                line = text.count("\n", 0, m.start()) + 1
                markers[(fam, rel, line)] = kind
    return markers, kinds


def judge(markers, kinds, keyfunc=order_key):
    """按章分组配对；返回 (anomalies, per_family_counts)。"""
    families = sorted(f for f, ks in kinds.items()
                      if "close" not in ks and ({"begin", "end"} & ks))
    anomalies = []
    totals = {}
    for fam in families:
        by_chap = {}
        for (f, rel, line), kind in markers.items():
            if f != fam:
                continue
            by_chap.setdefault(chapter_key(rel), []).append((keyfunc(rel, line), rel, line, kind))
        for chap, items in sorted(by_chap.items()):
            stack, orphan = [], []
            for _k, rel, line, kind in sorted(items, key=lambda x: x[0]):
                if kind == "begin":
                    stack.append((rel, line))
                elif stack:
                    stack.pop()
                else:
                    orphan.append((rel, line))
            for rel, line in orphan:
                anomalies.append((fam, "P1-孤儿END", rel, line))
            for rel, line in stack:
                anomalies.append((fam, "P2-未配BEGIN", rel, line))
        totals[fam] = (sum(1 for (f, r, l), k in markers.items() if f == fam and k == "begin"),
                       sum(1 for (f, r, l), k in markers.items() if f == fam and k == "end"))
    return anomalies, totals


def unclosed_rows(root):
    rows = []
    for p in sorted(Path(root).rglob("*.md")):
        rel = p.relative_to(root).as_posix()
        text = p.read_text(encoding="utf-8")
        if has_unclosed(text):
            rows.append(("—", "P4-未闭合注释", rel, 0))
    return rows


def cmd_selftest():
    bad = []
    with tempfile.TemporaryDirectory() as td:
        root = Path(td) / "tree"
        vol = root / "第01卷-测试" / "第001章-测试"

        def mk(rel, text):
            p = vol / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(text, encoding="utf-8", newline="\n")

        mk("001.0-章级综合/001.0.9-批注.md",
           "# t\n\n<!-- FAM:BEGIN x -->\n正文\n")
        mk("001.0-章级综合/001.0.10-增补.md",
           "# t\n\n正文\n<!-- FAM:END -->\n")
        markers, kinds = collect(root)
        a1, _ = judge(markers, kinds)
        if a1:
            bad.append(f"配对跨 .9/.10 应零异常，实得 {a1}")
        a2, _ = judge(markers, kinds, keyfunc=order_key_lexicographic)
        if len(a2) != 2:
            bad.append(f"字典序负向对照应得 2 条伪报，实得 {len(a2)}")

        mk("001.0-章级综合/001.0.11-孤儿.md", "# t\n\n<!-- FAM:END -->\n")
        markers, kinds = collect(root)
        a3, _ = judge(markers, kinds)
        if not any(x[1] == "P1-孤儿END" and x[2].endswith("001.0.11-孤儿.md") for x in a3):
            bad.append(f"未命中 P1 孤儿 END：{a3}")

        mk("001.0-章级综合/001.0.12-未配.md", "# t\n\n<!-- FAM:BEGIN y -->\n正文\n")
        markers, kinds = collect(root)
        a4, _ = judge(markers, kinds)
        if not any(x[1] == "P2-未配BEGIN" and x[2].endswith("001.0.12-未配.md") for x in a4):
            bad.append(f"未命中 P2 未配 BEGIN：{a4}")

    with tempfile.TemporaryDirectory() as td:
        root = Path(td) / "tree"
        vol = root / "第02卷-测试" / "第002章-测试" / "002.0-章级综合"
        vol.mkdir(parents=True)

        def mk2(name, text):
            (vol / name).write_text(text, encoding="utf-8", newline="\n")

        mk2("002.0.1-开始.md", "# t\n\n<!-- CN:开始 -->\n正文\n")
        mk2("002.0.2-结束.md", "# t\n\n正文\n<!-- CN:结束 -->\n")
        markers, kinds = collect(root)
        a5, _ = judge(markers, kinds)
        if a5:
            bad.append(f"中文 开始／结束 同族应零异常，实得 {a5}")

        mk2("002.0.3-块开.md", "# t\n\n<!-- BLK:x -->\n")
        mk2("002.0.4-块闭.md", "# t\n\n<!-- /BLK -->\n")
        markers, kinds = collect(root)
        a6, _ = judge(markers, kinds)
        if any(x[0] == "BLK" for x in a6):
            bad.append(f"block 家族不应由本脚本判：{a6}")

        mk2("002.0.5-未闭合.md", "# t\n\n<!-- BROKEN\n")
        if not unclosed_rows(root):
            bad.append("未命中 P4 未闭合注释")

    with tempfile.TemporaryDirectory() as td:
        root = Path(td) / "tree"
        d1 = root / "第03卷-测试" / "第003章-测试" / "003.0-章级综合"
        d2 = root / "第03卷-测试" / "第004章-测试" / "004.0-章级综合"
        d1.mkdir(parents=True)
        d2.mkdir(parents=True)
        (d1 / "003.0.1-a.md").write_text("# t\n\n<!-- XC:BEGIN -->\n正文\n", encoding="utf-8", newline="\n")
        (d2 / "004.0.1-b.md").write_text("# t\n\n正文\n<!-- XC:END -->\n", encoding="utf-8", newline="\n")
        markers, kinds = collect(root)
        a7, _ = judge(markers, kinds)
        codes = sorted(x[1] for x in a7 if x[0] == "XC")
        if codes != ["P1-孤儿END", "P2-未配BEGIN"]:
            bad.append(f"跨章配对应拆成一孤一未配，实得 {a7}")
        if len(a7) != 2:
            bad.append(f"跨章异常总数应为 2，实得 {len(a7)}")

    if bad:
        print("判据非空自检 FAIL：", file=sys.stderr)
        for b in bad:
            print("  " + b, file=sys.stderr)
        return 1
    print("判据非空自检 PASS：10 项（数值序配对 1／字典序负向对照 2／P1 3／P2 4／"
          "中文形态 5／block 豁免 6／P4 7／跨章拆解 8–10）")
    return 0


def main():
    ap = argparse.ArgumentParser(description="BEGIN/END 章内配对审计（第三十四件）")
    ap.add_argument("--root", default=str(DEFAULT_ROOT))
    ap.add_argument("--check", action="store_true", help="P1／P2／P4 命中即 exit 1")
    ap.add_argument("--csv", help="异常明细落盘路径")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        return cmd_selftest()

    root = Path(args.root)
    if not root.exists():
        print("根目录不存在：%s" % root, file=sys.stderr)
        return 2
    markers, kinds = collect(root)
    anomalies, totals = judge(markers, kinds)
    anomalies += unclosed_rows(root)

    print("=" * 72)
    print("BEGIN/END 章内配对审计（根：%s）" % root)
    print("=" * 72)
    for fam in sorted(totals):
        b, e = totals[fam]
        print("  %-22s BEGIN %4d / END %4d" % (fam, b, e))
    print("  异常 %d 条" % len(anomalies))
    for fam, code, rel, line in anomalies:
        print("    %-10s %-14s %s:%d" % (code, fam, rel, line))

    if args.csv:
        with open(args.csv, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f, lineterminator="\n")
            w.writerow(["family", "code", "file", "line"])
            w.writerows(anomalies)
        print("  明细：%s" % args.csv)

    print("-" * 72)
    print("  结论：%s" % ("PASS（章内配对零残余）" if not anomalies else "FAIL"))
    return 1 if (args.check and anomalies) else 0


if __name__ == "__main__":
    sys.exit(main())
