# -*- coding: utf-8 -*-
"""成对锚配平审计（TD-022 固化件；ADR-0011 成对不变量的门禁实现）。

对象：05-卷册大纲/ 树内 .md 的 HTML 注释锚（多行感知）。家族模式（TD-022 判据书 §三裁定）：
  block     : open/close 成对，可跨文件；全树 open==close 为 PASS
  single    : 只有单标记（open 即完整标记，标记头＋引用块）；close 出现即孤儿
  begin_end : BEGIN/END 成对，可跨文件；全树 begin==end 为 PASS
默认 single。ROW_MINE／DEEP_ANALYSIS 单锚不参与。

判据：
  T1 有开无闭（block，文件级 INFO）
  T2 有闭无开（block，文件级 INFO）
  T4 未闭合注释（全局 FAIL）
  G1 全树 block 家族 open!=close → FAIL
  G2 single 家族出现 close → FAIL（唯一补对侧例外：MAIL_INSIGHT_SECTION 若有 open 同卷则补 close，见判据书 §六）
--check 仅在 T4 或 G1／G2 命中时 exit 1；文件级异常只作 INFO 与清单。
不修改任何文件。--csv／--json 落文件级明细；--selftest 判据非空。
"""
import argparse
import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
DEFAULT_ROOT = REPO / "05-卷册大纲"

COMMENT_RE = re.compile(r"<!--(.*?)-->", re.S)
UNCLOSED_RE = re.compile(r"<!--(?!.*?-->)", re.S)
SINGLE_ANCHOR = ("ROW_MINE", "DEEP_ANALYSIS")


def family_of(body: str):
    b = body.strip()
    if not b:
        return None, "other"
    first = b.split()[0]
    if first.startswith("/"):
        fam = first[1:].split(":")[0]
        if fam in SINGLE_ANCHOR or not fam:
            return None, "other"
        return fam, "close"
    fam = first.split(":")[0]
    if fam in SINGLE_ANCHOR or not fam or not re.fullmatch(r"[A-Za-z0-9_\-]+", fam):
        return None, "other"
    return fam, "open"


def read_text(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return p.read_text(encoding="utf-8", errors="replace")


def collect_families(root: Path):
    kinds = defaultdict(set)
    n_files = 0
    for p in sorted(root.rglob("*.md")):
        n_files += 1
        for m in COMMENT_RE.finditer(read_text(p)):
            fam, kind = family_of(m.group(1))
            if fam:
                kinds[fam].add(kind)
    return n_files, kinds


def file_report(text: str, paired=None):
    counts, anomalies = Counter(), []
    for m in COMMENT_RE.finditer(text):
        fam, kind = family_of(m.group(1))
        if not fam or (paired is not None and fam not in paired):
            continue
        counts[(fam, kind)] += 1
    if UNCLOSED_RE.search(text):
        anomalies.append(("T4", "", "存在未闭合的 <!-- 注释"))
    for fam in sorted({k[0] for k in counts}):
        if fam == "block":
            o, c = counts.get((fam, "open"), 0), counts.get((fam, "close"), 0)
            if o > c:
                anomalies.append(("T1", fam, "open=%d > close=%d" % (o, c)))
            elif c > o:
                anomalies.append(("T2", fam, "close=%d > open=%d" % (c, o)))
    return counts, anomalies


def scan(root: Path):
    n_files, kinds = collect_families(root)
    files_bad, rows = 0, []
    fam_totals, type_totals, fam_bad = Counter(), Counter(), Counter()
    for p in sorted(root.rglob("*.md")):
        counts, anomalies = file_report(read_text(p), None)
        fam_totals.update(counts)
        rel = p.relative_to(root).as_posix()
        for (code, fam, detail) in anomalies:
            type_totals[code] += 1
            if fam:
                fam_bad[fam] += 1
            rows.append({"code": code, "family": fam, "file": rel, "detail": detail})
        if anomalies:
            files_bad += 1

    global_fail = []
    for fam, ks in sorted(kinds.items()):
        if "close" not in ks:
            continue  # single 家族
        o, c = fam_totals.get((fam, "open"), 0), fam_totals.get((fam, "close"), 0)
        if o != c:
            global_fail.append(("G1", fam, "open=%d != close=%d" % (o, c)))
    t4 = type_totals.get("T4", 0)
    return n_files, files_bad, rows, fam_totals, type_totals, fam_bad, global_fail, t4, kinds


def cmd_selftest() -> int:
    cases = [
        ("balanced", "<!-- PODCAST_REVIEW -->\n内容\n<!-- /PODCAST_REVIEW -->\n", 0),
        ("T1-block", "<!-- PODCAST_REVIEW -->\n内容\n", 1),
        ("T2-block", "<!-- /MAIL_INSIGHT -->\n内容\n", 1),
        ("T4", "<!-- PODCAST_REVIEW\n内容无闭合\n", 1),
        ("single-anchor-ignored", "<!-- ROW_MINE: a.b.1 -->\n<!-- DEEP_ANALYSIS: c.d -->\n", 0),
        ("multiline-pair", "<!--\nMAIL_MINE:x -->\n正文\n<!--\n /MAIL_MINE -->\n", 0),
        ("single-mode-open-only", "<!-- DB_REF:x.duckdb -->\n> 引用\n", 0),
        ("unpaired-family-ignored", "<!-- FINE_SP_linux_114 -->\n", 0),
    ]
    bad = []
    for name, text, expect in cases:
        paired = {"PODCAST_REVIEW"} if name == "unpaired-family-ignored" else None
        _counts, anomalies = file_report(text, paired)
        if len(anomalies) != expect:
            bad.append(f"{name}: 期望 {expect} 命中 {len(anomalies)}（{anomalies}）")
    if bad:
        print("判据非空自检 FAIL：", file=sys.stderr)
        for b in bad:
            print("  " + b, file=sys.stderr)
        return 1
    print("判据非空自检 PASS：8 例（block／single 两模式、多行配对、单锚豁免、一次性标记豁免、T1/T2/T4 各命中）")
    return 0


def main():
    ap = argparse.ArgumentParser(description="成对锚配平审计（第三十三件）")
    ap.add_argument("--root", default=str(DEFAULT_ROOT))
    ap.add_argument("--check", action="store_true", help="T4 或 G1 命中即 exit 1")
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
    n_files, files_bad, rows, fam_totals, type_totals, fam_bad, global_fail, t4, kinds = scan(root)

    print("=" * 72)
    print("成对锚配平审计（根：%s）" % root)
    print("=" * 72)
    print("  扫描 .md：%d；文件级 INFO 异常：%d（%.2f%%）" % (n_files, files_bad, files_bad / max(1, n_files) * 100))
    block_fams = [f for f, ks in sorted(kinds.items()) if "close" in ks]
    print("  block 家族（全树判据 G1）：%s" % ("、".join(block_fams) or "无"))
    print("  文件级类型（INFO）：" + ("；".join(f"{k}={v}" for k, v in sorted(type_totals.items())) or "无"))
    print("  按家族（仅异常）：" + ("；".join(f"{k}={v}" for k, v in fam_bad.most_common()) or "无"))
    print()
    print("  家族全树配平（模式｜open/close｜判定）：")
    for fam, ks in sorted(kinds.items()):
        o, c = fam_totals.get((fam, "open"), 0), fam_totals.get((fam, "close"), 0)
        mode = "block" if "close" in ks else "single"
        ok = (o == c) if mode == "block" else True
        print("    %-22s %-7s %5d/%-5d %s" % (fam, mode, o, c, "PASS" if ok else "FAIL"))
    print()
    print("  全局判据：T4=%d；G1 失败 %d 项%s"
          % (t4, len(global_fail),
             "：" + "；".join("%s %s %s" % x for x in global_fail) if global_fail else ""))

    if args.csv and rows:
        with open(args.csv, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["code", "family", "file", "detail"], lineterminator="\n")
            w.writeheader()
            w.writerows(rows)
        print("  文件级清单：%s（%d 行）" % (args.csv, len(rows)))
    if args.json:
        import json
        Path(args.json).write_text(json.dumps({
            "root": str(root), "files": n_files, "files_bad": files_bad,
            "fam_totals": {"%s|%s" % k: v for k, v in fam_totals.items()},
            "type_totals": dict(type_totals),
            "global_fail": global_fail,
            "file_level_anomalies": rows,
        }, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
        print("  明细 JSON：%s" % args.json)
    fails = len(global_fail) + (1 if t4 else 0)
    print("-" * 72)
    print("  结论：%s" % ("PASS（全树差值归零）" if fails == 0 else "FAIL（%d 项全局判据）" % fails))
    return 1 if (args.check and fails) else 0


if __name__ == "__main__":
    sys.exit(main())
