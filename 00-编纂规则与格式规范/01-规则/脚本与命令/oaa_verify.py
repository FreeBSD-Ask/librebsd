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
AUD = os.path.join(ROOT, "script", "_db_row_mining", "audit_outline")


def load_done():
    """G1 判定集 = 合并集（基线 processed.jsonl ∪ 各组 processed_fN.jsonl）。
    F1–F4 分片台账协议下各组只写自己的 processed_fN.jsonl，故必须并集。"""
    done = set()
    for fn in ["processed.jsonl"] + [f"processed_{g}.jsonl" for g in ("f1", "f2", "f3", "f4")]:
        p = os.path.join(AUD, fn)
        if not os.path.exists(p):
            continue
        for l in open(p, encoding="utf-8"):
            if l.strip():
                try:
                    done.add(json.loads(l)["key"])
                except Exception:
                    pass
    return done

RM = re.compile(r"<!--\s*ROW_MINE:\s*([\w-]+)\.([\w.]+)\.(\d+)\s*-->")


def cjk(s):
    return sum(1 for c in s if ord(c) > 0x2E7F)


def is_bad_star(s):
    """`*` 是否属禁用强调符。仅两种算强调：①成对 Markdown（`*word*` / `**bold**`）；
    ②中文正文里被中文夹住的裸星（`*强调*`）。凡前后为英文/代码/层级通配（`*BSD`、`(*p)`、`comp.unix.*`）均豁免。
    判定：找 `*` 成对包裹（下一个 `*` 之前无换行/空白断裂）→ 强调；或 `*` 两侧直接是中文 → 强调。"""
    # 找成对星号包裹（单词强调 *word*；排除 C 注释 /* */ 与含空白的通配）
    import re as _re
    if _re.search(r"(?<!/)\*([^*\s/]{1,16})\*(?!\w)", s):
        return True
    # 中文夹星（两侧紧邻汉字）
    for i, c in enumerate(s):
        if c != "*":
            continue
        prev = s[i - 1] if i > 0 else ""
        nxt = s[i + 1] if i + 1 < len(s) else ""
        if prev and ord(prev) > 0x2E7F and nxt and ord(nxt) > 0x2E7F:
            return True
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline", type=int, help="快照锚点基线总数")
    ap.add_argument("--db-claim", type=int)
    ap.add_argument("--db-ce", type=int)
    ap.add_argument("--db-ev", type=int)
    ap.add_argument("--len-flex", action="store_true",
                    help="长度上限放宽（F2 用）：只查下限 C<30 仍 FAIL；CJK>80/总>200 记入"
                         "长度超限清单（不 FAIL，批次报告备案）——F2 任务书 §六 字数门禁"
                         "仅设下限、§一体例注明 tech-kern 摘要偏长，且 87,665 块中 993/1000 本就 ≤200/80，"
                         "超限者为技术密集长帖（2026-09-29 实测口径）")
    ap.add_argument("hosts", nargs="+")
    args = ap.parse_args()

    fails = []
    # G1 processed 覆盖（合并集：基线 ∪ 四组分片台账）
    done = load_done()
    # fetch 档案（等级真值＋块型）
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
            fb = fetch.get(key)
            inline = (fb.get("block_type") == "inline") if fb else not ln.lstrip().startswith("<!--")
            if inline:
                # 紧凑列举体例：只查禁字符（行尾锚点含英文引文属合法，排除锚点后查）
                narr = ln[:RM.search(ln).start()]
                if re.search(r"[「」『』＊]", narr) or '"' in narr or is_bad_star(narr):
                    fails.append(f"G3 inline 禁字符: {rel}:{i+1}")
            else:
                summ = lines[i + 3] if i + 3 < len(lines) else ""
                body = summ.split("引用时按")[0].rstrip("。")
                C, L = cjk(body), len(body)
                if C < 30:
                    fails.append(f"G3 字数不足 CJK={C} 总={L}: {rel}:{i+4}")
                elif not args.len_flex and (C > 80 or L > 200):
                    fails.append(f"G3 字数 CJK={C} 总={L}: {rel}:{i+4}")
                elif args.len_flex and (C > 80 or L > 200):
                    print(f"  长度超限(备案): {rel}:{i+4} CJK={C} 总={L}")
                if re.search(r"[「」『』＊]", summ) or '"' in summ or is_bad_star(summ):
                    fails.append(f"G3 禁字符: {rel}:{i+4}")
                if "引用时按" not in summ:
                    fails.append(f"G3 纪律串缺失: {rel}:{i+4}")
                elif summ.count("引用时按") != 1:
                    fails.append(f"G3 纪律串重复 {summ.count('引用时按')} 次: {rel}:{i+4}")
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