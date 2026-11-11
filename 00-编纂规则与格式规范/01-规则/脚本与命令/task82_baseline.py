#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""task82_baseline.py — Task 8.2 基线生成器（固定脚本，只读扫描）

用途：
    从四处真值重算全 76 卷基线，供 162 号文附表与每卷开批前复算：
      1. 分母：`05-卷册大纲/映射/title-design/V*.tsv` 数据行
      2. 状态：树内小节 `.md` 的 YAML `status`（skeleton／filled／closed）
      3. 缺证：`05-卷册大纲/映射/design/exceptions/V*.tsv` 的 `status=open`
      4. 挂账：`05-卷册大纲/映射/design/surplus/V*.tsv` 数据行
    题号口径：`V{NN}.{chapter}.{section 末段}.{subsection 末段}`，
    与 `design/exceptions` 的 `subsection_id` 一致。

用法：
    python task82_baseline.py --check                 # 只打印汇总与逐卷表
    python task82_baseline.py --write --out <路径>    # 写 TSV（不含 TOTAL 行）
    python task82_baseline.py --markdown              # 输出 Markdown 表，供号文附表
退出码：0 正常；2 路径不可解析。
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
OUTLINE = ROOT / "05-卷册大纲"
MAP = OUTLINE / "映射"


def read_tsv(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def tree_status() -> dict[str, dict[str, int]]:
    """返回 {卷: {skeleton, filled, closed}} 与题号集合。"""
    out: dict[str, dict[str, int]] = defaultdict(lambda: {"skeleton": 0, "filled": 0, "closed": 0})
    ids: dict[str, set[str]] = defaultdict(set)
    for vol in sorted(OUTLINE.glob("第*卷-*")):
        if not vol.is_dir():
            continue
        m = re.match(r"第(\d+)卷", vol.name)
        if not m:
            continue
        vnum = int(m.group(1))
        v = f"V{vnum:02d}"
        for p in vol.rglob("*.md"):
            try:
                text = p.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            if not text.startswith("---"):
                continue
            end = text.find("\n---", 3)
            if end < 0:
                continue
            fm = {}
            for line in text[3:end].splitlines():
                mm = re.match(r"^(\w+):\s*(.*?)\s*$", line)
                if mm:
                    fm[mm.group(1)] = mm.group(2)
            if not fm.get("section") or not fm.get("subsection"):
                continue
            try:
                sid = f"{v}.{int(fm['chapter'])}.{fm['section'].split('.')[-1]}.{fm['subsection'].split('.')[-1]}"
            except (KeyError, ValueError):
                continue
            st = fm.get("status", "")
            if st in out[v]:
                out[v][st] += 1
                ids[v].add(sid)
    return out, ids


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--markdown", action="store_true")
    ap.add_argument("--out", default=str(MAP / "parallel" / "content" / "00-task82-基线-20261111.tsv"))
    a = ap.parse_args()

    for p in (OUTLINE, MAP / "title-design", MAP / "design" / "exceptions", MAP / "design" / "surplus"):
        if not p.exists():
            print(f"[abort] 路径不存在：{p}")
            return 2

    status, ids = tree_status()
    rows = []
    totals = defaultdict(int)
    for v in sorted(ids):
        td = read_tsv(MAP / "title-design" / f"{v}.tsv")
        exc = read_tsv(MAP / "design" / "exceptions" / f"{v}.tsv")
        sp = [r for p in sorted((MAP / "design" / "surplus").glob(f"{v}*.tsv")) for r in read_tsv(p)]
        row = {
            "vol": v,
            "title_count": len(td),
            "filled": status[v]["filled"],
            "skeleton": status[v]["skeleton"],
            "closed": status[v]["closed"],
            "exceptions_open": sum(1 for r in exc if r.get("status") == "open"),
            "surplus": len(sp),
        }
        rows.append(row)
        for k, val in row.items():
            if k != "vol":
                totals[k] += val

    print(f"[汇总] 卷 {len(rows)}｜题 {totals['title_count']}｜filled {totals['filled']}"
          f"｜skeleton {totals['skeleton']}｜closed {totals['closed']}"
          f"｜open {totals['exceptions_open']}｜surplus {totals['surplus']}")
    print(f"[恒等式] title={totals['title_count']} = filled+skeleton+closed="
          f"{totals['filled'] + totals['skeleton'] + totals['closed']}")

    if a.markdown:
        print("| 卷 | 题数 | filled | skeleton | closed | 例外 open | 挂账 |")
        print("| ---- | ----: | ----: | ----: | ----: | ----: | ----: |")
        for r in rows:
            print(f"| {r['vol']} | {r['title_count']} | {r['filled']} | {r['skeleton']} | "
                  f"{r['closed']} | {r['exceptions_open']} | {r['surplus']} |")
        print(f"| **合计** | **{totals['title_count']}** | **{totals['filled']}** | "
              f"**{totals['skeleton']}** | **{totals['closed']}** | "
              f"**{totals['exceptions_open']}** | **{totals['surplus']}** |")

    if a.write:
        out = Path(a.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        with out.open("w", encoding="utf-8", newline="\n") as fh:
            fh.write("vol\ttitle_count\tfilled\tskeleton\tclosed\texceptions_open\tsurplus\n")
            for r in rows:
                fh.write(f"{r['vol']}\t{r['title_count']}\t{r['filled']}\t{r['skeleton']}\t"
                         f"{r['closed']}\t{r['exceptions_open']}\t{r['surplus']}\n")
        print(f"[写盘] {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
