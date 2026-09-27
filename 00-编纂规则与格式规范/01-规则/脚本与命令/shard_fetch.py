#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""shard_fetch.py — 把宿主 fetch.jsonl 切成判读分片（供子代理并行）

用法：python shard_fetch.py <fetch.jsonl> <片数> <输出目录> <片名前缀>
输出：片名前缀_sNN.jsonl，每片约等量
"""
import json
import math
import os
import sys


def main(src, n, outdir, prefix):
    n = int(n)
    os.makedirs(outdir, exist_ok=True)
    rows = [l for l in open(src, encoding="utf-8").read().splitlines() if l.strip()]
    per = math.ceil(len(rows) / n)
    paths = []
    for i in range(n):
        chunk = rows[i * per:(i + 1) * per]
        if not chunk:
            continue
        p = os.path.join(outdir, f"{prefix}_s{i+1:02d}.jsonl")
        with open(p, "w", encoding="utf-8") as fh:
            fh.write("\n".join(chunk) + "\n")
        paths.append((p, len(chunk)))
    for p, c in paths:
        print(f"{c:4d}  {os.path.basename(p)}")
    print(f"共 {sum(c for _, c in paths)} 块 → {len(paths)} 片")


if __name__ == "__main__":
    main(*sys.argv[1:5])