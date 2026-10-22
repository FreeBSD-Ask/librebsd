# -*- coding: utf-8 -*-
"""成对锚配平审计（TD-022 固化件；ADR-0011 成对不变量的门禁实现）。

对象：05-卷册大纲/ 树内 .md 的 HTML 注释锚（多行感知）。家族模式按 TD-022
判据书 §三／§七 裁定，由全树 kinds 数据驱动：
  block     : 家族出现 close → open/close 成对（可跨文件）；全树 open==close 为 PASS（G1）
  begin_end : 家族无 close 但出现 BEGIN/END → 全树 begin==end 为 PASS（G2）；
              同族单标记（如 REVIEW-ANNOT 的 702 处批注头）按裁定 4 豁免
  single    : 只有 open 单标记（如 DB_REF 裁定 1 后、NEWREF 等原生单标记）→ 不判平
单锚 ROW_MINE／DEEP_ANALYSIS 不参与。

判据：
  T4 未闭合注释（全局 FAIL）
  G1 block 家族全树 open!=close → FAIL
  G2 begin_end 家族全树 begin!=end → FAIL
文件级一律 INFO（跨文件块合法，文件级失衡不判罚）。
--check 仅在 T4／G1／G2 命中时 exit 1。--csv／--json 落文件级明细。--selftest 判据非空。
"""
import argparse
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
DEFAULT_ROOT = REPO / "05-卷册大纲"

COMMENT_RE = re.compile(r"<!--(.*?)-->", re.S)
SINGLE_ANCHOR = ("ROW_MINE", "DEEP_ANALYSIS")


def family_of(body: str):
    """返回 (family, kind)；kind ∈ open/close/begin/end/other。"""
    b = body.strip()
    if not b:
        return None, "other"
    first = b.split()[0]
    if first.startswith("/"):
        fam = first[1:].split(":")[0]
        if fam in SINGLE_ANCHOR or not fam:
            return None, "other"
        return fam, "close"
    if first.endswith("BEGIN") or ":BEGIN" in first:
        fam = first.split(":")[0]
        if fam in SINGLE_ANCHOR or not fam:
            return None, "other"
        return fam, "begin"
    if first.endswith("END") or ":END" in first:
        fam = first.split(":")[0]
        if fam in SINGLE_ANCHOR or not fam:
            return None, "other"
        return fam, "end"
    fam = first.split(":")[0]
    if fam in SINGLE_ANCHOR or not fam or not re.fullmatch(r"[A-Za-z0-9_\-]+", fam):
        return None, "other"
    return fam, "open"


def has_unclosed(text: str) -> bool:
    """剥离全部完整注释后若残留 <!-- 即存在未闭合。"""
    return "<!--" in COMMENT_RE.sub("", text)


def read_text(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return p.read_text(encoding="utf-8", errors="replace")


def collect(root: Path):
    """返回 (n_files, kinds{fam→kind集合}, totals{(fam,kind)→n})。"""
    kinds = defaultdict(set)
    totals = Counter()
    n_files = 0
    for p in sorted(root.rglob("*.md")):
        n_files += 1
        for m in COMMENT_RE.finditer(read_text(p)):
            fam, kind = family_of(m.group(1))
            if fam:
                kinds[fam].add(kind)
                totals[(fam, kind)] += 1
    return n_files, kinds, totals


def mode_of(fam: str, kinds) -> str:
    ks = kinds.get(fam, set())
    if "close" in ks:
        return "block"
    if "begin" in ks or "end" in ks:
        return "begin_end"
    return "single"


def global_verdicts(kinds, totals):
    """全树判据：G1 block 家族 open==close；G2 begin_end 家族 begin==end。"""
    fails = []
    for fam in sorted(kinds):
        mode = mode_of(fam, kinds)
        o, c = totals.get((fam, "open"), 0), totals.get((fam, "close"), 0)
        b, e = totals.get((fam, "begin"), 0), totals.get((fam, "end"), 0)
        if mode == "block" and o != c:
            fails.append(("G1", fam, "open=%d != close=%d" % (o, c)))
        if mode == "begin_end" and b != e:
            fails.append(("G2", fam, "BEGIN=%d != END=%d" % (b, e)))
    return fails


def file_report(text: str):
    """文件级 INFO 明细：各家族计数＋T4；不作文件级判罚。"""
    counts, anomalies = Counter(), []
    for m in COMMENT_RE.finditer(text):
        fam, kind = family_of(m.group(1))
        if fam:
            counts[(fam, kind)] += 1
    if has_unclosed(text):
        anomalies.append(("T4", "", "存在未闭合的 <!-- 注释"))
    return counts, anomalies


def scan(root: Path):
    n_files, kinds, totals = collect(root)
    files_bad, rows = 0, []
    type_totals = Counter()
    for p in sorted(root.rglob("*.md")):
        _counts, anomalies = file_report(read_text(p))
        rel = p.relative_to(root).as_posix()
        for (code, fam, detail) in anomalies:
            type_totals[code] += 1
            rows.append({"code": code, "family": fam, "file": rel, "detail": detail})
        if anomalies:
            files_bad += 1
    gfails = global_verdicts(kinds, totals)
    t4 = type_totals.get("T4", 0)
    return n_files, kinds, totals, files_bad, rows, type_totals, gfails, t4


def cmd_selftest() -> int:
    bad = []

    def fam_case(name, body, want_fam, want_kind):
        got = family_of(body)
        if got != (want_fam, want_kind):
            bad.append(f"{name}: family_of 期望 {want_fam}/{want_kind} 实得 {got}")

    fam_case("close", "/FAM", "FAM", "close")
    fam_case("close-arg", "/DB_REF:x", "DB_REF", "close")
    fam_case("begin", "REVIEW-ANNOT:BEGIN 2026-10-14 x", "REVIEW-ANNOT", "begin")
    fam_case("end", "W172-YT-ROUTE:END", "W172-YT-ROUTE", "end")
    fam_case("open", "COL_SCAN v20260914-lit", "COL_SCAN", "open")
    fam_case("open-arg", "MAIL_INSIGHT: marc:123", "MAIL_INSIGHT", "open")
    fam_case("single-anchor", "ROW_MINE: a.b.1", None, "other")
    fam_case("empty", "", None, "other")

    def t4_case(name, text, want):
        got = has_unclosed(text)
        if got != want:
            bad.append(f"{name}: has_unclosed 期望 {want} 实得 {got}")

    t4_case("closed-only", "<!-- A -->\n正文\n", False)
    t4_case("unclosed", "<!-- A\n正文", True)
    t4_case("closed-then-unclosed", "<!-- A -->\n<!-- B\n", True)

    def g_case(name, kinds, totals, want_codes):
        got = global_verdicts(kinds, totals)
        codes = sorted(x[0] for x in got)
        if codes != sorted(want_codes):
            bad.append(f"{name}: global_verdicts 期望 {sorted(want_codes)} 实得 {got}")

    g_case("block-ok", {"F": {"open", "close"}},
           {("F", "open"): 2, ("F", "close"): 2}, [])
    g_case("block-fail", {"F": {"open", "close"}},
           {("F", "open"): 2, ("F", "close"): 1}, ["G1"])
    g_case("be-ok", {"F": {"begin", "end"}},
           {("F", "begin"): 3, ("F", "end"): 3}, [])
    g_case("be-fail", {"F": {"begin", "end"}},
           {("F", "begin"): 3, ("F", "end"): 2}, ["G2"])
    g_case("mixed-opens-exempt", {"F": {"open", "begin", "end"}},
           {("F", "open"): 702, ("F", "begin"): 1, ("F", "end"): 1}, [])
    g_case("single-exempt", {"F": {"open"}}, {("F", "open"): 99}, [])

    if bad:
        print("判据非空自检 FAIL：", file=sys.stderr)
        for b in bad:
            print("  " + b, file=sys.stderr)
        return 1
    print("判据非空自检 PASS：16 例（family_of 七形态、T4 三态、global_verdicts 六判据含混合家族豁免）")
    return 0


def main():
    ap = argparse.ArgumentParser(description="成对锚配平审计（第三十三件）")
    ap.add_argument("--root", default=str(DEFAULT_ROOT))
    ap.add_argument("--check", action="store_true", help="T4／G1／G2 命中即 exit 1")
    ap.add_argument("--json", help="明细 JSON 落盘路径")
    ap.add_argument("--csv", help="文件级 INFO 清单 CSV 落盘路径")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        return cmd_selftest()

    root = Path(args.root)
    if not root.exists():
        print("根目录不存在：%s" % root, file=sys.stderr)
        return 2
    n_files, kinds, totals, files_bad, rows, type_totals, gfails, t4 = scan(root)

    print("=" * 72)
    print("成对锚配平审计（根：%s）" % root)
    print("=" * 72)
    print("  扫描 .md：%d；T4 文件：%d；文件级 INFO 明细 %d 行" % (n_files, files_bad, len(rows)))
    print("  文件级类型（INFO）：" + ("；".join(f"{k}={v}" for k, v in sorted(type_totals.items())) or "无"))
    print()
    print("  家族模式与全树配平（模式｜open/close｜begin/end｜判定）：")
    for fam in sorted(kinds):
        mode = mode_of(fam, kinds)
        o, c = totals.get((fam, "open"), 0), totals.get((fam, "close"), 0)
        b, e = totals.get((fam, "begin"), 0), totals.get((fam, "end"), 0)
        ok = (o == c) if mode == "block" else (b == e if mode == "begin_end" else True)
        print("    %-22s %-9s %5d/%-5d %5d/%-5d %s"
              % (fam, mode, o, c, b, e, "PASS" if ok else "FAIL"))
    print()
    print("  全局判据：T4=%d；G1/G2 失败 %d 项%s"
          % (t4, len(gfails),
             "：" + "；".join("%s %s %s" % x for x in gfails) if gfails else ""))

    if args.csv and rows:
        with open(args.csv, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["code", "family", "file", "detail"], lineterminator="\n")
            w.writeheader()
            w.writerows(rows)
        print("  文件级清单：%s（%d 行）" % (args.csv, len(rows)))
    if args.json:
        Path(args.json).write_text(json.dumps({
            "root": str(root), "files": n_files,
            "family_mode": {f: mode_of(f, kinds) for f in sorted(kinds)},
            "fam_totals": {"%s|%s" % k: v for k, v in sorted(totals.items())},
            "type_totals": dict(type_totals),
            "global_fail": gfails,
            "file_level_anomalies": rows,
        }, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
        print("  明细 JSON：%s" % args.json)
    fails = len(gfails) + (1 if t4 else 0)
    print("-" * 72)
    print("  结论：%s" % ("PASS（全树差值归零）" if fails == 0 else "FAIL（%d 项全局判据）" % fails))
    return 1 if (args.check and fails) else 0


if __name__ == "__main__":
    sys.exit(main())
