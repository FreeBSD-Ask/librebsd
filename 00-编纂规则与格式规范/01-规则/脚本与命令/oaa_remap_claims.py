#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""oaa_remap_claims.py — 大纲 claims 清单只读回映检查器（F 线烟测修复件）

背景：F1–F4 的认领清单 beacon/claims_F*.txt 记的是“宿主 .md 相对路径”；05-卷册大纲
目录树经整卷重排后，路径中的卷号／章号／节号多已变化，清单路径大面积失效。本工具
只读比对清单与现行树，给出每条原路径的候选或 UNMATCHED，**绝不改 claims 文件、
绝不猜测多候选**。

判据：
  1) 逐条判断原路径在现行树中是否仍存在 → 存在率；
  2) 对不存在的路径，按“卷号＋章题＋节题去数字前缀”在当前树中找唯一候选
     （节题＝原文件名去掉首部数字前缀；候选为现行树中章目录下同名的节级目录或 .md）；
     无章级段的清单（卷下直属宿主）退回按“卷号＋节题”在整卷内找唯一候选；
  3) 输出“原路径 → EXISTS / 候选 / AMBIGUOUS(n) / UNMATCHED”，统计
     存在率、可唯一回映数、歧义数、未匹配数。
  exit 0 仅当存在率或唯一回映率（存在∪唯一 / 总数）为 100%，否则 1。

用法：
  python oaa_remap_claims.py --group F1 --check
  python oaa_remap_claims.py --claims <FILE> --root 05-卷册大纲 --report <FILE>
"""
import argparse
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
BEACON = os.path.join(ROOT, "script", "_db_row_mining", "audit_outline", "beacon")

VOL_RE = re.compile(r"^第(\d+)卷")
CHAP_RE = re.compile(r"^第\d+章-")
# 节题去数字前缀：形如 100.16- / 012.1- / 10.9- 的首部编号（数字与点，后接连字符）
NUM_PREFIX_RE = re.compile(r"^[\d.]+-")


def _utf8_stdout():
    """统一文本输出为 UTF-8 无 BOM、LF。"""
    for st in (sys.stdout, sys.stderr):
        try:
            st.reconfigure(encoding="utf-8", newline="\n")
        except Exception:
            pass


def vol_no(name):
    m = VOL_RE.match(name)
    return int(m.group(1)) if m else None


def strip_chap(name):
    return CHAP_RE.sub("", name, count=1)


def strip_num(name):
    return NUM_PREFIX_RE.sub("", name, count=1)


def stem(name):
    return name[:-3] if name.endswith(".md") else name


def parse_claim(rel):
    """宿主相对路径 → (卷号, 章题, 节题, 是否有章级)；无法解析返回 None。"""
    parts = rel.replace("\\", "/").split("/")
    if len(parts) < 3:
        return None
    v = vol_no(parts[1])
    if v is None:
        return None
    mids = parts[2:-1]
    chap = strip_chap(mids[0]) if mids else ""
    sect = strip_num(stem(parts[-1]))
    return v, chap, sect, bool(mids)


def build_index(root_dir):
    """扫现行树 → (sec_index, vol_index)：
    sec_index[(卷号, 章题, 节题)] → [相对路径…]（章目录下直属的节级目录或 .md）
    vol_index[(卷号, 节题)]       → [相对路径…]（无章级清单的整卷回退用）"""
    sec, volidx = {}, {}
    for vol in sorted(os.listdir(root_dir)):
        vp = os.path.join(root_dir, vol)
        if not os.path.isdir(vp):
            continue
        v = vol_no(vol)
        if v is None:
            continue
        for chap in sorted(os.listdir(vp)):
            cp = os.path.join(vp, chap)
            if not CHAP_RE.match(chap) or not os.path.isdir(cp):
                continue
            ct = strip_chap(chap)
            for ent in sorted(os.listdir(cp)):
                ep = os.path.join(cp, ent)
                if os.path.isdir(ep):
                    st = strip_num(ent)
                elif ent.endswith(".md"):
                    st = strip_num(ent[:-3])
                else:
                    continue
                relp = os.path.relpath(ep, ROOT).replace("\\", "/")
                sec.setdefault((v, ct, st), []).append(relp)
                volidx.setdefault((v, st), []).append(relp)
    return sec, volidx


def check(claims_file, root_name):
    """只读检查 → (退出码, 报告行列表)。"""
    root_dir = os.path.join(ROOT, root_name)
    if not os.path.isdir(root_dir):
        print(f"错误：根目录不存在 {root_dir}", file=sys.stderr)
        return 2, []
    with open(claims_file, encoding="utf-8") as fh:
        rels = [l.strip() for l in fh if l.strip() and not l.startswith("#")]
    sec, volidx = build_index(root_dir)
    lines = []
    n_exist = n_unique = n_amb = n_unmatch = 0
    for rel in rels:
        if os.path.exists(os.path.join(ROOT, rel)):
            n_exist += 1
            lines.append(f"{rel} → EXISTS")
            continue
        parsed = parse_claim(rel)
        if parsed is None:
            n_unmatch += 1
            lines.append(f"{rel} → UNMATCHED（无法解析卷/章/节）")
            continue
        v, chap, sect, has_chap = parsed
        cands = sec.get((v, chap, sect), []) if has_chap else volidx.get((v, sect), [])
        if len(cands) == 1:
            n_unique += 1
            lines.append(f"{rel} → {cands[0]}")
        elif len(cands) > 1:
            n_amb += 1
            lines.append(f"{rel} → AMBIGUOUS({len(cands)}): " + " | ".join(cands))
        else:
            n_unmatch += 1
            lines.append(f"{rel} → UNMATCHED")
    total = len(rels)
    resolved = n_exist + n_unique
    exist_rate = (n_exist / total) if total else 0.0
    uniq_rate = (resolved / total) if total else 0.0
    ok = bool(total) and (n_exist == total or resolved == total)
    lines += [
        "",
        f"清单：{os.path.relpath(claims_file, ROOT).replace(chr(92), '/')}",
        f"根目录：{root_name}",
        f"总条数：{total}",
        f"存在：{n_exist}（存在率 {exist_rate:.2%}）",
        f"可唯一回映：{n_unique}",
        f"歧义：{n_amb}",
        f"未匹配：{n_unmatch}",
        f"唯一回映率（存在∪唯一 / 总数）：{uniq_rate:.2%}",
        f"判定：{'PASS' if ok else 'FAIL'}",
    ]
    return (0 if ok else 1), lines


def main():
    _utf8_stdout()
    ap = argparse.ArgumentParser(description="大纲 claims 清单只读回映检查器")
    ap.add_argument("--claims", help="claims 清单文件（一行一个宿主相对路径）")
    ap.add_argument("--group", choices=["F1", "F2", "F3", "F4"], help="按组取 beacon/claims_F*.txt")
    ap.add_argument("--root", default="05-卷册大纲", help="现行大纲根目录（默认 05-卷册大纲）")
    ap.add_argument("--check", action="store_true", help="执行只读检查（默认动作）")
    ap.add_argument("--report", help="报告输出文件（UTF-8 无 BOM / LF）")
    args = ap.parse_args()
    claims = args.claims
    if not claims:
        if not args.group:
            ap.error("需要 --claims FILE 或 --group F1..F4")
        claims = os.path.join(BEACON, f"claims_{args.group}.txt")
    if not os.path.exists(claims):
        print(f"错误：claims 文件不存在 {claims}", file=sys.stderr)
        return 2
    rc, lines = check(claims, args.root)
    if rc == 2:
        return 2
    text = "\n".join(lines) + "\n"
    sys.stdout.write(text)
    if args.report:
        parent = os.path.dirname(os.path.abspath(args.report))
        if parent:
            os.makedirs(parent, exist_ok=True)
        with open(args.report, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
    return rc


if __name__ == "__main__":
    sys.exit(main())
