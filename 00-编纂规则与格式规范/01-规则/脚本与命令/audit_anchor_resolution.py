# -*- coding: utf-8 -*-
"""
第十九件门禁：锚解析审计（audit_anchor_resolution.py）

背景（104 号文 §2.1 ／ 125 号文 ★56 ／ spec converge-all-remaining-tasks SubTask 1.11）：
  目录注中的 mat NNNN 与 CL-RM-NNNNNN、CL-N-NNN 编号曾判“本地三库不可解析”。
  2026-10-09 C-12 批 0 信任实测订正：编号体系在库，系查询格式错配——
    mat N      -> historical_claims.duckdb  raw_source.source_id = 'SRC-mat:N'
    CL-RM-NNNN -> historical_claims.duckdb  evidence.evidence_id = 'EV-RM-NNNNNN'
    CL-N-NNN   -> historical_claims.duckdb  claim.claim_id      = 'CL-N-NNN'
  本件按三键位对内容源 outline.txt 全量锚点做解析审计：
    - 解析率须达到阈值（现行 95%）
    - 悬空锚逐条列出（登记不静默，悬空处置归后续批）
    - 禁止目录注回改（本件为只读审计，不改 outline.txt）

用法：python audit_anchor_resolution.py [--outline PATH] [--db PATH]
退出码：0=PASS，1=FAIL。
"""
import argparse
import io
import os
import re
import sys

import duckdb

DEFAULT_OUTLINE = r"d:\librebsd\08-核查报告与多轮复核\重构2026\data\outline.txt"
DEFAULT_DB = r"d:\librebsd\04-现代研究文献\historical_claims.duckdb"
THRESHOLD = 95  # 解析率阈值（%）

RE_MAT = re.compile(r"\bmat (\d{2,5})\b")
RE_CL_RM = re.compile(r"\bCL-RM-(\d{6})\b")
RE_CL_N = re.compile(r"\bCL-(\d)-(\d{3})\b")


def extract_anchors(text):
    mats = sorted(set(int(m) for m in RE_MAT.findall(text)))
    cl_rms = sorted(set(RE_CL_RM.findall(text)))
    # CL-N-NNN：排除已被 CL-RM-NNNNNN 前缀吞并的匹配
    cl_rms_full = set(RE_CL_RM.findall(text))
    cl_ns = sorted(set((a, b) for a, b in RE_CL_N.findall(text)))
    return mats, cl_rms, cl_ns


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--outline", default=DEFAULT_OUTLINE)
    ap.add_argument("--db", default=DEFAULT_DB)
    args = ap.parse_args()

    text = io.open(args.outline, encoding="utf-8").read()
    mats, cl_rms, cl_ns = extract_anchors(text)
    total = len(mats) + len(cl_rms) + len(cl_ns)
    print("=" * 72)
    print("第十九件：锚解析审计（mat／CL-RM／CL-N 三键位 -> historical_claims 库）")
    print(f"  内容源：{args.outline}")
    print(f"  目标库：{args.db}")
    print(f"  锚点：mat {len(mats)} ／ CL-RM {len(cl_rms)} ／ CL-N {len(cl_ns)}，合计 {total}")
    print("-" * 72)

    con = duckdb.connect(args.db, read_only=True)
    miss_mat, miss_rm, miss_n = [], [], []

    for m in mats:
        n = con.execute(
            "SELECT count(*) FROM raw_source WHERE source_id = ?", [f"SRC-mat:{m}"]
        ).fetchone()[0]
        if n == 0:
            miss_mat.append(f"mat {m}")

    for rm in cl_rms:
        n = con.execute(
            "SELECT count(*) FROM evidence WHERE evidence_id = ?", [f"EV-RM-{rm}"]
        ).fetchone()[0]
        if n == 0:
            miss_rm.append(f"CL-RM-{rm}")

    for vol, seq in cl_ns:
        cid = f"CL-{vol}-{seq}"
        n = con.execute(
            "SELECT count(*) FROM claim WHERE claim_id = ?", [cid]
        ).fetchone()[0]
        if n == 0:
            miss_n.append(cid)
    con.close()

    miss_all = miss_mat + miss_rm + miss_n
    resolved = total - len(miss_all)
    rate = resolved * 100 // total if total else 100

    print(f"  mat   -> SRC-mat:N   命中 {len(mats) - len(miss_mat)}/{len(mats)}"
          + (f"；未命中 {miss_mat}" if miss_mat else ""))
    print(f"  CL-RM -> EV-RM-NNNN 命中 {len(cl_rms) - len(miss_rm)}/{len(cl_rms)}"
          + (f"；未命中 {miss_rm}" if miss_rm else ""))
    print(f"  CL-N  -> claim_id   命中 {len(cl_ns) - len(miss_n)}/{len(cl_ns)}"
          + (f"；未命中 {miss_n}" if miss_n else ""))
    print("-" * 72)
    print(f"  解析率 {rate}%（阈值 {THRESHOLD}%）；悬空 {len(miss_all)} 处"
          + ("——登记不静默，处置归后续批" if miss_all else ""))

    if rate >= THRESHOLD:
        print(f"第十九件：PASS——解析率 {rate}% 达标（悬空逐条登记见上）")
        sys.exit(0)
    else:
        print(f"第十九件：FAIL——解析率 {rate}% 低于阈值 {THRESHOLD}%")
        sys.exit(1)


if __name__ == "__main__":
    main()
