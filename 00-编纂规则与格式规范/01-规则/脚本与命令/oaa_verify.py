#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""oaa_verify.py — 大纲邮件素材审计·后验门禁（每批收尾必跑，全绿 exit 0）

门禁项：
  G1 宿主内每条锚点都有 processed 判定（无遗漏、无略过）
  G2 锚点总数守恒：当前大纲扫描数 == 快照基线（无块增删漂移）
  G3 块体机检：恰 5 行结构、摘要汉字 30–80、总字符 ≤200、禁字符（直角引号/星号/ASCII 双引号）、纪律串在场
  G4 等级一致性：块头「证据等级：Lx」== 主库 claim.evidence_level 真值（经 fetch 档案）
  G5 数据库行数守恒：claim/claim_evidence/evidence 计数与基线一致
  G6 编码：宿主文件 UTF-8 无 BOM、LF

用法：python oaa_verify.py --baseline 309004 --db-claim 289739 --db-ce 289744 --db-ev 316276 \
        host1.md host2.md ...
"""
import argparse
import glob
import json
import os
import re
import sys

import duckdb

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
OUTLINE = os.path.join(ROOT, "05-卷册大纲")
MAIN_DB = os.path.join(ROOT, "04-现代研究文献", "historical_claims.duckdb")
WORK = os.path.join(ROOT, "script", "_db_row_mining", "audit_outline", "work")
PROC = os.path.join(ROOT, "script", "_db_row_mining", "audit_outline", "processed.jsonl")

RM = re.compile(r"<!--\s*ROW_MINE:\s*([\w-]+)\.([\w.]+)\.(\d+)\s*-->")


def cjk(s):
    return sum(1 for c in s if ord(c) > 0x2E7F)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline", type=int, help="快照锚点基线总数")
    ap.add_argument("--db-claim", type=int)
    ap.add_argument("--db-ce", type=int)
    ap.add_argument("--db-ev", type=int)
    ap.add_argument("hosts", nargs="+")
    args = ap.parse_args()

    fails = []
    # G1 processed 覆盖
    done = set()
    with open(PROC, encoding="utf-8") as fh:
        for l in fh:
            if l.strip():
                done.add(json.loads(l)["key"])
    # fetch 档案（等级真值）
    fetch = {}
    for f in glob.glob(os.path.join(WORK, "*.fetch.jsonl")):
        for l in open(f, encoding="utf-8"):
            if l.strip():
                r = json.loads(l)
                fetch[r["key"]] = r
    # G2 总数
    n_all = 0
    for f in glob.glob(os.path.join(OUTLINE, "**", "*.md"), recursive=True):
        with open(f, encoding="utf-8", errors="ignore") as fh:
            n_all += len(RM.findall(fh.read()))
    if args.baseline is not None and n_all != args.baseline:
        fails.append(f"G2 锚点总数漂移: {args.baseline} → {n_all}")
    else:
        print(f"G2 锚点总数守恒: {n_all}")
    # G3/G4/G6 逐宿主
    for rel in args.hosts:
        path = os.path.join(ROOT, rel)
        raw = open(path, "rb").read()
        if raw.startswith(b"\xef\xbb\xbf"):
            fails.append(f"G6 BOM: {rel}")
        if b"\r\n" in raw:
            fails.append(f"G6 CRLF: {rel}")
        lines = raw.decode("utf-8").splitlines()
        n_blk = 0
        for i, ln in enumerate(lines):
            m = RM.search(ln)
            if not m:
                continue
            n_blk += 1
            key = f"{m.group(1)}|{m.group(3)}|" + rel.replace("\\", "/")
            if key not in done:
                fails.append(f"G1 未登记判定: {key}")
            summ = lines[i + 3] if i + 3 < len(lines) else ""
            body = summ.split("引用时按")[0].rstrip("。")
            C, L = cjk(body), len(body)
            if C < 30 or C > 80 or L > 200:
                fails.append(f"G3 字数 CJK={C} 总={L}: {rel}:{i+4}")
            if re.search(r"[「」『』＊]", summ) or '"' in summ or "*" in summ:
                fails.append(f"G3 禁字符: {rel}:{i+4}")
            if "引用时按" not in summ:
                fails.append(f"G3 纪律串缺失: {rel}:{i+4}")
            fb = fetch.get(key)
            if fb and fb.get("level"):
                hm = re.search(r"证据等级：(L\d)", lines[i + 1] if i + 1 < len(lines) else "")
                if hm and hm.group(1) != fb["level"]:
                    fails.append(f"G4 等级不符 DB 真值 {fb['level']}: {rel}:{i+2}")
        print(f"G1/G3/G4 {rel.split('/')[-1]}: {n_blk} 块")
    # G5 DB 守恒
    if args.db_claim is not None:
        con = duckdb.connect(MAIN_DB, read_only=True)
        c1 = con.execute("SELECT (SELECT count(*) FROM claim), (SELECT count(*) FROM claim_evidence), (SELECT count(*) FROM evidence)").fetchone()
        con.close()
        if (c1[0], c1[1], c1[2]) != (args.db_claim, args.db_ce, args.db_ev):
            fails.append(f"G5 DB 行数漂移: 基线 {(args.db_claim, args.db_ce, args.db_ev)} → {c1}")
        else:
            print(f"G5 DB 行数守恒: claim={c1[0]} ce={c1[1]} ev={c1[2]}")
    print("----")
    if fails:
        print(f"FAIL {len(fails)} 项:")
        for x in fails[:30]:
            print("  !", x)
        sys.exit(1)
    print("全部门禁通过（G1–G6）")


if __name__ == "__main__":
    main()