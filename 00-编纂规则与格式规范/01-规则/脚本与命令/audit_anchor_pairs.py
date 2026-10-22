# -*- coding: utf-8 -*-
"""成对锚配平审计（TD-022 固化件；ADR-0011 成对不变量的门禁实现）。

对象：05-卷册大纲/ 树内 .md 的成对锚（HTML 注释，多行感知）：
  open   = <!-- FAM[:X] ... -->
  close  = <!-- /FAM[:X] ... -->
  begin  = <!-- FAM:BEGIN ... -->
  end    = <!-- FAM:END ... -->
单锚 ROW_MINE／DEEP_ANALYSIS 不参与配平。无法解析家族的注释计入 other，不判平。

判据（T1–T4，逐文件）：
  T1 有开无闭：某家族 open(+begin) 计数 > close(+end) 计数
  T2 有闭无开：close(+end) 计数 > open(+begin) 计数
  T3 BEGIN/END 家族失衡：begin != end
  T4 未闭合注释：存在 <!-- 而无配对 -->
仅报告与计数；不修改任何文件。默认输出摘要；--json 落明细；--csv 落异常清单；
--check 任一 T1–T4 命中即 exit 1（供清理批次与常驻门禁使用）。
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
    if ":BEGIN" in first or first.endswith("BEGIN"):
        fam = first.split(":")[0]
        if fam in SINGLE_ANCHOR or not fam:
            return None, "other"
        return fam, "begin"
    if ":END" in first or first.endswith("END"):
        fam = first.split(":")[0]
        if fam in SINGLE_ANCHOR or not fam:
            return None, "other"
        return fam, "end"
    fam = first.split(":")[0]
    if fam in SINGLE_ANCHOR or not fam or not re.fullmatch(r"[A-Za-z0-9_\-]+", fam):
        return None, "other"
    return fam, "open"


def file_report(text: str):
    """返回 (counts, anomalies)；counts: (fam, kind) -> n；anomalies: list[(code, fam, detail)]"""
    counts = Counter()
    anomalies = []
    for m in COMMENT_RE.finditer(text):
        fam, kind = family_of(m.group(1))
        if fam:
            counts[(fam, kind)] += 1
    if UNCLOSED_RE.search(text):
        anomalies.append(("T4", "", "存在未闭合的 <!-- 注释"))
    fams = {k[0] for k in counts}
    for fam in sorted(fams):
        o = counts.get((fam, "open"), 0) + counts.get((fam, "begin"), 0)
        c = counts.get((fam, "close"), 0) + counts.get((fam, "end"), 0)
        bg = counts.get((fam, "begin"), 0)
        en = counts.get((fam, "end"), 0)
        if o > c:
            anomalies.append(("T1", fam, "open+begin=%d > close+end=%d" % (o, c)))
        elif c > o:
            anomalies.append(("T2", fam, "close+end=%d > open+begin=%d" % (c, o)))
        if bg != en:
            anomalies.append(("T3", fam, "BEGIN=%d != END=%d" % (bg, en)))
    return counts, anomalies


def scan(root: Path):
    files_bad = 0
    anomaly_rows = []
    fam_totals = Counter()
    type_totals = Counter()
    n_files = 0
    for p in sorted(root.rglob("*.md")):
        n_files += 1
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            text = p.read_text(encoding="utf-8", errors="replace")
        counts, anomalies = file_report(text)
        fam_totals.update(counts)
        rel = p.relative_to(root).as_posix()
        for (code, fam, detail) in anomalies:
            type_totals[code] += 1
            anomaly_rows.append({
                "code": code, "family": fam, "file": rel, "detail": detail,
            })
        if anomalies:
            files_bad += 1
    return n_files, files_bad, anomaly_rows, fam_totals, type_totals


def cmd_selftest() -> int:
    cases = [
        ("balanced", "<!-- DB_POINTS:x -->\n内容\n<!-- /DB_POINTS:x -->\n", 0),
        ("T1", "<!-- PODCAST_REVIEW -->\n内容\n", 1),
        ("T2", "<!-- /MAIL_INSIGHT -->\n内容\n", 1),
        ("T3", "<!-- REVIEW-ANNOT:BEGIN a -->\n内容\n", 1),
        ("T4", "<!-- DB_POINTS:y\n内容无闭合\n", 1),
        ("single-anchor-ignored", "<!-- ROW_MINE: a.b.1 -->\n<!-- DEEP_ANALYSIS: c.d -->\n", 0),
        ("multiline-pair", "<!--\nDB_REF:z -->\n正文\n<!--\n /DB_REF -->\n", 0),
    ]
    bad = []
    for name, text, expect in cases:
        _counts, anomalies = file_report(text)
        got = len(anomalies)
        if got != expect:
            bad.append(f"{name}: 期望 {expect} 命中 {got}（{anomalies}）")
    if bad:
        print("判据非空自检 FAIL：", file=sys.stderr)
        for b in bad:
            print("  " + b, file=sys.stderr)
        return 1
    print("判据非空自检 PASS：7 例（含多行配对、单锚豁免、T1–T4 各命中）")
    return 0


def main():
    ap = argparse.ArgumentParser(description="成对锚配平审计（第三十三件）")
    ap.add_argument("--root", default=str(DEFAULT_ROOT))
    ap.add_argument("--check", action="store_true", help="任一异常即 exit 1")
    ap.add_argument("--json", help="明细 JSON 落盘路径")
    ap.add_argument("--csv", help="异常清单 CSV 落盘路径")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        return cmd_selftest()

    root = Path(args.root)
    if not root.exists():
        print("根目录不存在：%s" % root, file=sys.stderr)
        return 2
    n_files, files_bad, anomaly_rows, fam_totals, type_totals = scan(root)

    print("=" * 72)
    print("成对锚配平审计（根：%s）" % root)
    print("=" * 72)
    print("  扫描 .md：%d；异常文件：%d（%.2f%%）" % (n_files, files_bad, files_bad / max(1, n_files) * 100))
    print("  异常类型：" + "；".join(f"{k}={v}" for k, v in sorted(type_totals.items())) or "无")
    fam_bad = Counter()
    for r in anomaly_rows:
        if r["family"]:
            fam_bad[r["family"]] += 1
    print("  按家族（仅异常）：" + ("；".join(f"{k}={v}" for k, v in fam_bad.most_common()) if fam_bad else "无"))
    print("  配对锚总量（open/close/begin/end）：" +
          "；".join(f"{k}={v}" for k, v in sorted(fam_totals.items())))

    if args.csv and anomaly_rows:
        with open(args.csv, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["code", "family", "file", "detail"], lineterminator="\n")
            w.writeheader()
            w.writerows(anomaly_rows)
        print("  异常清单：%s（%d 行）" % (args.csv, len(anomaly_rows)))
    if args.json:
        import json
        Path(args.json).write_text(json.dumps({
            "root": str(root), "files": n_files, "files_bad": files_bad,
            "type_totals": dict(type_totals),
            "fam_totals": {"%s|%s" % k: v for k, v in fam_totals.items()},
            "anomalies": anomaly_rows,
        }, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
        print("  明细 JSON：%s" % args.json)
    print("-" * 72)
    verdict = "FAIL（%d 文件异常）" % files_bad if files_bad else "PASS（配平全一致）"
    print("  结论：%s" % verdict)
    return 1 if (args.check and files_bad) else 0


if __name__ == "__main__":
    sys.exit(main())
