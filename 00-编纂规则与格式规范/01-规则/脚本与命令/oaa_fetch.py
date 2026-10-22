#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""oaa_fetch.py — 大纲邮件素材审计·块提取与数据库反查工具（只读）

用法（写盘须显式给出输出位置，防误写生产 audit_outline/work/）：
  python oaa_fetch.py --host <大纲文件相对路径> --workdir <输出目录>
  python oaa_fetch.py --host <大纲文件相对路径> --out <输出jsonl>
  python oaa_fetch.py --hosts-file <宿主清单> --workdir <输出目录>   # 一行一个宿主，串行

未显式给出 --workdir 时拒绝写生产 script/_db_row_mining/audit_outline/work/ 并
以 exit 2 退出。所有文本输出统一 UTF-8 无 BOM、LF。

对宿主内每个 ROW_MINE / MAIL_INSIGHT 块输出一行 JSON 档案：
  key / line / db / pk / anchor_line / head_line / summ_line
  claim_id / level / claim_text / fact_text
  src_date / src_from / src_subject / src_body（源库 messages 全文）

反查通路（2026-09-27 实测确认）：
  raw_source.source_db + raw_source.local_pk  →  evidence → claim_evidence → claim
  （evidence.anchor 存批次标签，不是 <库>.messages.<pk>，勿用）
"""
import argparse
import csv
import datetime
import glob
import json
import os
import re
import sys

import duckdb

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
OUTLINE = os.path.join(ROOT, "05-卷册大纲")
MAIN_DB = os.path.join(ROOT, "04-现代研究文献", "historical_claims.duckdb")
REG_CSV = os.path.join(ROOT, "11-元数据接口", "09-文件夹数据库索引", "folder_db_registry.csv")
WORK = os.path.join(ROOT, "script", "_db_row_mining", "audit_outline", "work")

# pk 允许字母数字连字符形态（如 CL-15-3303），不仅是纯数字；
# 旧式 (\d+) 会静默漏掉 CL-<任意>-<数字> 一类 pk，令宿主提取块数为 0。
ROW_MINE = re.compile(r"<!--\s*ROW_MINE:\s*([\w-]+)\.([\w.]+)\.([\w-]+)\s*-->")
MAIL_INS = re.compile(r"<!--\s*MAIL_INSIGHT:\s*([^>]+?)\s*-->")


def _utf8_stdout():
    """统一文本输出为 UTF-8 无 BOM、LF（Windows 控制台默认 cp936 且换行为 CRLF）。"""
    for st in (sys.stdout, sys.stderr):
        try:
            st.reconfigure(encoding="utf-8", newline="\n")
        except Exception:
            pass


def load_registry():
    reg = {}
    with open(REG_CSV, encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            reg[row["db_name"]] = row["db_path"]
    # 补扫描邮件列表史料各分支 db/ 目录（folder_db_registry 未含 sparclinux/lkml 等）
    ml_dir = os.path.join(ROOT, "03-原始史料库", "11-邮件列表史料")
    for sub in sorted(glob.glob(os.path.join(ml_dir, "*", "db", "*.duckdb"))):
        name = os.path.basename(sub).replace(".duckdb", "")
        reg.setdefault(name, os.path.relpath(sub, ROOT).replace("\\", "/"))
    return reg


def extract_blocks(path):
    """提取宿主内全部邮件素材块。返回 [{key,line,db,pk,anchor_line,head_line,summ_line,insight_body}]"""
    with open(path, encoding="utf-8", newline="") as fh:
        lines = fh.read().splitlines()
    rel = os.path.relpath(path, ROOT).replace("\\", "/")
    out = []
    for i, ln in enumerate(lines):
        ms = list(ROW_MINE.finditer(ln))
        if not ms:
            continue
        if ln.lstrip().startswith("<!--"):
            # 独立行锚型（H 线 5 行块）：向下找抬头行与摘要行
            head_line, summ_line = "", ""
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines):
                head_line = lines[j]
            j += 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines):
                summ_line = lines[j]
            for m in ms:
                db, tb, pk = m.group(1), m.group(2), m.group(3)
                out.append({"key": f"{db}|{pk}|{rel}", "line": i + 1, "db": db, "pk": pk,
                            "block_type": "standalone", "anchor_line": ln,
                            "head_line": head_line, "summ_line": summ_line,
                            "insight_body": ""})
        else:
            # 内联锚型（T1/L1 紧凑列举体例）：叙述与锚点同行，行尾反引号包裹。
            # 必须逐锚提取（finditer）：史料锚行一行可挂多锚（实测一行至 18 锚、
            # 全库 492 行 2,166 锚），search 只取首个会让其余锚对审计不可见。
            narr = ln[:ms[0].start()].rstrip().rstrip("`").rstrip()
            for m in ms:
                db, tb, pk = m.group(1), m.group(2), m.group(3)
                out.append({"key": f"{db}|{pk}|{rel}", "line": i + 1, "db": db, "pk": pk,
                            "block_type": "inline", "anchor_line": ln,
                            "head_line": "", "summ_line": narr, "insight_body": ""})
    # MAIL_INSIGHT 块
    for i, ln in enumerate(lines):
        m = MAIL_INS.search(ln)
        if m and ROW_MINE.search(ln):
            continue
        if m:
            body = [ln]
            k = i + 1
            while k < len(lines) and "/MAIL_INSIGHT" not in lines[k]:
                body.append(lines[k])
                k += 1
            if k < len(lines):
                body.append(lines[k])
            out.append({"key": f"MAIL_INSIGHT|{m.group(1).strip()}|{rel}",
                        "line": i + 1, "db": "MAIL_INSIGHT", "pk": m.group(1).strip(),
                        "block_type": "insight", "anchor_line": ln, "head_line": "",
                        "summ_line": "", "insight_body": "\n".join(body)})
    return out


def fetch_db_meta(con, blocks):
    """批量反查主库：{key: {claim_id, level, claim_text, fact_text}}"""
    by_db = {}
    for b in blocks:
        if b["db"] == "MAIL_INSIGHT":
            continue
        by_db.setdefault(b["db"], []).append(b["pk"])
    meta = {}
    for db, pks in by_db.items():
        ph = ",".join(["?"] * len(pks))
        q = (
            "SELECT CAST(rs.local_pk AS VARCHAR), c.claim_id, c.evidence_level, "
            "c.claim_text, e.fact_text "
            "FROM raw_source rs "
            "JOIN evidence e ON e.source_id = rs.source_id "
            "JOIN claim_evidence ce ON ce.evidence_id = e.evidence_id "
            "JOIN claim c ON c.claim_id = ce.claim_id "
            f"WHERE rs.source_db = ? AND CAST(rs.local_pk AS VARCHAR) IN ({ph})"
        )
        try:
            rows = con.execute(q, [db] + pks).fetchall()
        except duckdb.Error as ex:
            print(f"  ! 主库查询失败 {db}: {ex}", file=sys.stderr)
            continue
        # 一 pk 可能多 claim：主 claim 取第一条，其余记 claim_ids
        agg = {}
        for pk, cid, lv, ct, ft in rows:
            d = agg.setdefault(pk, {"claim_id": cid, "level": lv,
                                    "claim_text": ct or "", "fact_text": ft or "",
                                    "claim_ids": [cid]})
            if cid not in d["claim_ids"]:
                d["claim_ids"].append(cid)
        meta[db] = agg
    return meta


def fetch_src_meta(reg, blocks):
    """批量反查源库全文：{key: {src_date, src_from, src_subject, src_body}}"""
    by_db = {}
    for b in blocks:
        if b["db"] == "MAIL_INSIGHT":
            continue
        by_db.setdefault(b["db"], set()).add(b["pk"])
    src = {}
    for db, pks in by_db.items():
        path = reg.get(db)
        if not path:
            print(f"  ! 注册表无此库: {db}", file=sys.stderr)
            continue
        full = os.path.join(ROOT, path)
        if not os.path.exists(full):
            print(f"  ! 源库文件不存在: {full}", file=sys.stderr)
            continue
        try:
            s = duckdb.connect(full, read_only=True)
        except duckdb.Error as ex:
            print(f"  ! 源库连接失败 {db}: {ex}", file=sys.stderr)
            continue
        cols = {r[0] for r in s.execute(
            "SELECT column_name FROM information_schema.columns "
            "WHERE table_name='messages'").fetchall()}
        sel_parts = ["CAST(id AS VARCHAR)"]
        for c in ("date", "from_name", "from_email", "subject"):
            if c in cols:
                sel_parts.append(c)
        sel_parts.append("body" if "body" in cols else "NULL")
        sel = ", ".join(sel_parts)
        col_names = ["id"] + [c for c in ("date", "from_name", "from_email",
                                          "subject") if c in cols] + ["body"]
        ph = ",".join(["?"] * len(pks))
        try:
            rows = s.execute(
                f"SELECT {sel} FROM messages WHERE CAST(id AS BIGINT) IN ({ph})",
                list(pks)).fetchall()
        except duckdb.Error as ex:
            print(f"  ! 源库查询失败 {db}: {ex}", file=sys.stderr)
            s.close()
            continue
        idx = {c: i for i, c in enumerate(col_names)}
        for r in rows:
            pk = r[0]
            frm = " ".join(str(r[idx[c]]) for c in ("from_name", "from_email")
                           if c in idx and r[idx[c]])
            d = {"src_date": str(r[idx["date"]]) if "date" in idx and r[idx["date"]] else "",
                 "src_from": frm,
                 "src_subject": str(r[idx["subject"]]) if "subject" in idx and r[idx["subject"]] else "",
                 "src_body": str(r[idx["body"]] or "")}
            src[f"{db}|{pk}"] = d
        s.close()
    return src


def count_row_mine(path):
    """统计宿主内 ROW_MINE 字面出现次数（含未识别形态），用于零块告警。"""
    with open(path, encoding="utf-8", newline="") as fh:
        return fh.read().count("ROW_MINE")


def run_host(rel, out_path=None):
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        print(f"宿主不存在: {path}", file=sys.stderr)
        return 1, False, False
    blocks = extract_blocks(path)
    print(f"{rel}: 提取 {len(blocks)} 块")
    # 零块宿主检测：块数=0 但文中确有 ROW_MINE，说明 pk 形态未被识别（静默漏块）。
    zero_block = len(blocks) == 0
    zero_with_rowmine = False
    if zero_block:
        hits = count_row_mine(path)
        if hits:
            zero_with_rowmine = True
            print(f"  ! 警告：{rel} 提取 0 块，但 ROW_MINE 出现 {hits} 次"
                  f"（疑似 pk 形态未识别，未入 fetch.jsonl）", file=sys.stderr)
    try:
        con = duckdb.connect(MAIN_DB, read_only=True)
        meta = fetch_db_meta(con, blocks)
        con.close()
    except duckdb.Error as ex:
        # 主库被并行会话锁定等场景：降级为不含 claim 元数据（src_body 仍独立反查）
        print(f"  ! 主库不可用（{ex}），降级：claim 元数据留空，仅反查 src_body", file=sys.stderr)
        meta = {}
    reg = load_registry()
    src = fetch_src_meta(reg, blocks)
    miss_claim = miss_src = 0
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        for b in blocks:
            db, pk = b["db"], b["pk"]
            m = meta.get(db, {}).get(pk, {})
            s = src.get(f"{db}|{pk}", {})
            b["claim_id"] = m.get("claim_id", "")
            b["level"] = m.get("level", "")
            b["claim_text"] = m.get("claim_text", "")
            b["fact_text"] = m.get("fact_text", "")
            b["claim_ids"] = m.get("claim_ids", [])
            b.update({k: s.get(k, "") for k in
                      ("src_date", "src_from", "src_subject", "src_body")})
            if db != "MAIL_INSIGHT":
                if not b["claim_id"]:
                    miss_claim += 1
                if not b["src_body"]:
                    miss_src += 1
            fh.write(json.dumps(b, ensure_ascii=False) + "\n")
    n_mi = sum(1 for b in blocks if b["db"] == "MAIL_INSIGHT")
    print(f"  → {out_path} ｜ claim 缺 {miss_claim} ｜ src 缺 {miss_src}"
          f" ｜ MAIL_INSIGHT {n_mi}")
    return 0, zero_block, zero_with_rowmine


def out_for(host, out_path=None, workdir=None):
    """输出路径：显式 --out 优先，否则 --workdir/<宿主名>.fetch.jsonl。"""
    if out_path:
        return out_path
    name = os.path.basename(host).replace(".md", "")
    return os.path.join(workdir, f"{name}.fetch.jsonl")


def main():
    _utf8_stdout()
    ap = argparse.ArgumentParser(
        description="大纲邮件素材审计·反查工具（写盘位置须显式给出）",
        epilog="未显式给出 --out 或 --workdir 时拒绝写生产 "
               "script/_db_row_mining/audit_outline/work/，并以 exit 2 退出。")
    ap.add_argument("--host", help="宿主文件相对仓库根路径")
    ap.add_argument("--out", help="输出 JSONL 路径（显式指定，单宿主用）")
    ap.add_argument("--workdir", metavar="DIR",
                    help="输出目录；输出文件名为 <宿主名>.fetch.jsonl")
    ap.add_argument("--hosts-file", metavar="FILE",
                    help="批量入口：一行一个宿主相对路径（# 开头为注释），串行不做并发")
    args = ap.parse_args()
    if not (args.out or args.workdir):
        print("错误：未显式给出输出位置（--out 或 --workdir DIR）。\n"
              "拒绝写入生产 script/_db_row_mining/audit_outline/work/。",
              file=sys.stderr)
        return 2
    if args.hosts_file and args.host:
        ap.error("--hosts-file 与 --host 互斥")
    if args.hosts_file:
        with open(args.hosts_file, encoding="utf-8") as fh:
            hosts = [l.strip() for l in fh if l.strip() and not l.startswith("#")]
        fails = zero_hosts = zero_rowmine = 0
        for h in hosts:
            rc, zb, zw = run_host(h, out_for(h, workdir=args.workdir))
            if rc != 0:
                fails += 1
            zero_hosts += 1 if zb else 0
            zero_rowmine += 1 if zw else 0
        print(f"批量完成：{len(hosts)} 个宿主｜失败 {fails}"
              f"｜zero_block_hosts {zero_hosts}"
              f"｜zero_block_with_rowmine {zero_rowmine}")
        return 1 if fails else 0
    if not args.host:
        ap.error("需要 --host 或 --hosts-file")
    rc, _zb, _zw = run_host(args.host, out_for(args.host, args.out, args.workdir))
    return rc


if __name__ == "__main__":
    sys.exit(main())