#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""oaa_scan.py — 大纲邮件素材审计战役·摸底与台账工具（只读 + 台账写）

用法：
  python oaa_scan.py --snapshot          # 全量扫描大纲 → 快照 JSON
  python oaa_scan.py --stats             # 宿主/源库分布统计
  python oaa_scan.py --top-hosts N      # 块数最多的前 N 个宿主（默认 25）
  python oaa_scan.py --pending          # 快照 − processed.jsonl → pending.md
  python oaa_scan.py --judge keep --key <唯一键> [--to 目标宿主] [--note 备注]
                                        # 判定一条块写入 processed.jsonl

对象面：05-卷册大纲/**/*.md 中
  <!-- ROW_MINE: <库>.messages.<pk> -->      308,421 条
  <!-- MAIL_INSIGHT: <Message-ID> -->            891 条
唯一键：ROW_MINE → "{库}|{pk}|{宿主相对路径}"；MAIL_INSIGHT → "MAIL_INSIGHT|{id}|{宿主}"
台账目录：script/_db_row_mining/audit_outline/
"""
import argparse
import datetime
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
OUTLINE = os.path.join(ROOT, "05-卷册大纲")
OUT_DIR = os.path.join(ROOT, "script", "_db_row_mining", "audit_outline")
SNAP = os.path.join(OUT_DIR, "outline_scan_snapshot.json")
PROC = os.path.join(OUT_DIR, "processed.jsonl")
PEND = os.path.join(OUT_DIR, "pending.md")

ROW_MINE = re.compile(r"<!--\s*ROW_MINE:\s*([\w-]+)\.([\w.]+)\.(\d+)\s*-->")
MAIL_INS = re.compile(r"<!--\s*MAIL_INSIGHT:\s*([^>]+?)\s*-->")


def scan_all():
    """全量扫描大纲，返回 {key: {库, 表, pk, host, 摘要}}"""
    out = {}
    for f in glob.glob(os.path.join(OUTLINE, "**", "*.md"), recursive=True):
        rel = os.path.relpath(f, ROOT).replace("\\", "/")
        try:
            with open(f, encoding="utf-8") as fh:
                txt = fh.read()
        except (OSError, UnicodeDecodeError):
            continue
        for m in ROW_MINE.finditer(txt):
            db, tb, pk = m.group(1), m.group(2), m.group(3)
            key = f"{db}|{pk}|{rel}"
            # 摘要：块头之后第一段（避开锚点行）
            seg = txt[m.end(): m.end() + 400]
            head = re.search(r"\*\*([^*]{2,40})\*\*", seg)
            summ = ""
            for line in seg.splitlines():
                if line.strip() and not line.strip().startswith("<!--"):
                    summ = line.strip()[:32]
                    break
            out[key] = {"db": db, "table": tb, "pk": pk, "host": rel,
                        "抬头": head.group(1) if head else "", "summ": summ}
        for m in MAIL_INS.finditer(txt):
            key = f"MAIL_INSIGHT|{m.group(1).strip()}|{rel}"
            out[key] = {"db": "MAIL_INSIGHT", "table": "", "pk": m.group(1).strip(),
                        "host": rel, "抬头": "", "summ": ""}
    return out


def load_processed():
    """读 processed.jsonl → {key: rec}"""
    seen = {}
    if os.path.exists(PROC):
        with open(PROC, encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                    if "key" in rec:
                        seen[rec["key"]] = rec
                except ValueError:
                    continue
    return seen


def save_snapshot(snap):
    os.makedirs(OUT_DIR, exist_ok=True)
    tmp = SNAP + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump({"time": datetime.datetime.now().isoformat(timespec="seconds"),
                   "n": len(snap), "items": snap},
                  fh, ensure_ascii=False, indent=1)
    os.replace(tmp, SNAP)
    print(f"快照 {len(snap)} 条 → {os.path.relpath(SNAP, ROOT)}")


def write_pending(snap, done):
    pend_keys = [k for k in snap if k not in done]
    pend_keys.sort()
    with open(PEND, "w", encoding="utf-8") as fh:
        fh.write("# 待处理项（= 快照 − 已处理）\n\n")
        fh.write(f"更新时间：{datetime.datetime.now():%Y-%m-%d %H:%M}\n\n")
        fh.write(f"待处理 {len(pend_keys)} 条\n\n")
        for k in pend_keys:
            s = snap[k]
            fh.write(f"- `{k}` ｜ {s.get('db', '')} ｜ {s.get('summ', '')}\n")
    print(f"待处理 {len(pend_keys)} 条 → {os.path.relpath(PEND, ROOT)}")
    return pend_keys


def top_hosts(snap, n):
    hosts = {}
    for s in snap.values():
        hosts[s["host"]] = hosts.get(s["host"], 0) + 1
    for h, c in sorted(hosts.items(), key=lambda x: -x[1])[:n]:
        print(f"{c:6d}  {h}")
    return hosts


def buckets(snap):
    """按宿主块数分档，输出各档宿主数与块数总量"""
    hosts = {}
    for s in snap.values():
        hosts[s["host"]] = hosts.get(s["host"], 0) + 1
    edges = [(1, 10), (11, 50), (51, 200), (201, 1000), (1001, 3000),
             (3001, 8000), (8001, 999999)]
    for lo, hi in edges:
        inb = [(h, c) for h, c in hosts.items() if lo <= c <= hi]
        tot = sum(c for _, c in inb)
        print(f"[{lo:>5},{hi:>6}]  宿主 {len(inb):5d} 个 ｜ 块 {tot:7d} ｜ 每宿主中位 {0 if not inb else sorted(c for _,c in inb)[len(inb)//2]}")
    return hosts


def hosts_in_range(snap, lo, hi, topn=40):
    hosts = {}
    for s in snap.values():
        hosts[s["host"]] = hosts.get(s["host"], 0) + 1
    for h, c in sorted([(h, c) for h, c in hosts.items() if lo <= c <= hi], key=lambda x: -x[1])[:topn]:
        print(f"{c:6d}  {h}")


def db_stats(snap):
    dist = {}
    for s in snap.values():
        dist[s["db"]] = dist.get(s["db"], 0) + 1
    print(f"宿主文件数：{len({s['host'] for s in snap.values()})}")
    print(f"块总数：{len(snap)}")
    for db, c in sorted(dist.items(), key=lambda x: -x[1]):
        print(f"  {db:24s} {c:7d}")


def judge(key, judgement, to_host="", note=""):
    """把一条判写进 processed.jsonl（键相同则覆盖，防重复处理）"""
    os.makedirs(OUT_DIR, exist_ok=True)
    rec = {"key": key, "判定": judgement, "时间": datetime.datetime.now().isoformat(timespec="seconds")}
    if to_host:
        rec["目标宿主"] = to_host
    if note:
        rec["备注"] = note
    lines = []
    if os.path.exists(PROC):
        with open(PROC, encoding="utf-8") as fh:
            lines = [l for l in fh.read().splitlines() if l.strip()]
    # 按 key 去重（保留新判定）
    keep = [l for l in lines if (json.loads(l) or {}).get("key") != key]
    keep.append(json.dumps(rec, ensure_ascii=False))
    with open(PROC, "w", encoding="utf-8") as fh:
        fh.write("\n".join(keep) + "\n")
    print(f"已登记判定 {judgement} → {key}")


def main():
    ap = argparse.ArgumentParser(description="大纲邮件素材审计·摸底台账工具")
    ap.add_argument("--snapshot", action="store_true", help="重新生成全量快照")
    ap.add_argument("--stats", action="store_true", help="源库分布统计")
    ap.add_argument("--top-hosts", type=int, nargs="?", const=25, metavar="N",
                    help="按块数打印前 N 个宿主")
    ap.add_argument("--buckets", action="store_true",
                    help="宿主块数分档统计（宿主数/块总数/每档中位）")
    ap.add_argument("--hosts-in-range", nargs=2, type=int, metavar=("LO", "HI"),
                    help="打印块数落在 [LO,HI] 区间内的宿主")
    ap.add_argument("--topn", type=int, default=40, help="区间筛选时最多打印多少行")
    ap.add_argument("--pending", action="store_true", help="重建 pending.md")
    ap.add_argument("--judge", choices=["keep", "fix-format", "fix-text", "remap", "fix-db", "存疑"],
                    help="判定类型")
    ap.add_argument("--key", help="唯一键")
    ap.add_argument("--prefix", help="键前缀匹配（供批量登记的每条单独登记）")
    ap.add_argument("--to", help="remap 目标宿主前缀")
    ap.add_argument("--note", help="备注")
    args = ap.parse_args()

    snap = scan_all()
    done = load_processed()

    if args.snapshot:
        save_snapshot(snap)
    if args.stats:
        db_stats(snap)
    if args.top_hosts is not None:
        top_hosts(snap, args.top_hosts)
    if args.buckets:
        buckets(snap)
    if args.hosts_in_range:
        hosts_in_range(snap, args.hosts_in_range[0], args.hosts_in_range[1], args.topn)
    if args.pending:
        write_pending(snap, done)
    if args.judge:
        keys = []
        if args.key:
            keys = [args.key]
        elif args.prefix:
            keys = [k for k in snap if k.startswith(args.prefix)]
        for k in keys:
            judge(k, args.judge, args.to or "", args.note or "")
        if not keys:
            print("未找到匹配键", file=sys.stderr)
            sys.exit(2)
    if not (args.snapshot or args.stats or args.top_hosts is not None
            or args.buckets or args.hosts_in_range
            or args.pending or args.judge):
        pend = len([k for k in snap if k not in done])
        print(f"快照 {len(snap)} ｜ 已处理 {len(done)} ｜ 待处理 {pend}")
        print("（用 --snapshot / --stats / --top-hosts N / --buckets / "
              "--hosts-in-range LO HI / --pending 查看明细）")


if __name__ == "__main__":
    main()