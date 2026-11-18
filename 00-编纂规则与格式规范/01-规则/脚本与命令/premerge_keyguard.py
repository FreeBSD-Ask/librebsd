#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""premerge_keyguard.py —— merge_subsections 前置键集守卫（Task 8.3 线，2026-11-19 立）。

背景：merge_subsections.py 以 design/fragments/V{NN}.tsv 全集为真值合并 outline.txt
第四级行（缺键插入、fragment 外删除）。他会话在途改号（fragments 键集与已落地
outline/树键集不一致）时直接跑 merge 会误剪他卷行——2026-11-19 V18/V63 91 行事故
（已 HEAD 回填，见 changelog id=3331）。

判据：逐卷比对 fragments 键集（vol,sub_no）与 outline.txt 四级行键集
（卷, M.N.P）；键差非零即 FAIL 并列出卷号与差样。全库一致（或仅 --vol 白名单）
方可行 merge --write。只读，不写任何文件。

用法：
  python premerge_keyguard.py                # 全库扫描（exit 0=安全，1=有键差）
  python premerge_keyguard.py --vol V75      # 只核某卷（本卷键差即 FAIL，他卷忽略）
"""
import argparse
import csv
import os
import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
DEFAULT_ROOT = os.path.join("05-卷册大纲")
CN2 = "一二三四五六七八九十"


def cn2int(s):
    if s.isdigit():
        return int(s)
    if "十" in s:
        a, _, b = s.partition("十")
        return (CN2.index(a) + 1 if a else 1) * 10 + (CN2.index(b) + 1 if b else 0)
    if s in CN2:
        return CN2.index(s) + 1
    return None


def frag_keys(mapdir):
    out = {}
    fd = os.path.join(mapdir, "design", "fragments")
    if not os.path.isdir(fd):
        return out
    for fn in sorted(os.listdir(fd)):
        m = re.match(r"^V(\d{1,3})\.tsv$", fn)
        if not m:
            continue
        v = int(m.group(1))
        keys = set()
        with open(os.path.join(fd, fn), encoding="utf-8", newline="") as f:
            rd = csv.DictReader(f, delimiter="\t")
            for r in rd:
                try:
                    keys.add((v, str(r["sub_no"]).strip()))
                except KeyError:
                    return out
        out[v] = keys
    return out


def outline_keys(root):
    p = os.path.join(root, "目录", "data", "outline.txt")
    out = {}
    vol = None
    for ln in open(p, encoding="utf-8"):
        m = re.match(r"^# 第(.+?)卷", ln)
        if m:
            vol = cn2int(m.group(1))
        m = re.match(r"^  - (\d+\.\d+\.\d+) ", ln)
        if m and vol is not None:
            out.setdefault(vol, set()).add((vol, m.group(1)))
    return out


def main():
    ap = argparse.ArgumentParser(description="merge 前置 fragments↔outline 键集守卫（只读）")
    ap.add_argument("--root", default=DEFAULT_ROOT)
    ap.add_argument("--vol", default=None, help="只核该卷（V75 或 75）")
    a = ap.parse_args()
    root = a.root
    mapdir = os.path.join(root, "映射")
    fk = frag_keys(mapdir)
    ok = outline_keys(root)
    vols = sorted(set(fk) | set(ok))
    want = None
    if a.vol:
        want = int(a.vol) if a.vol.isdigit() else int(a.vol[1:])
    bad = []
    for v in vols:
        if want is not None and v != want:
            continue
        f, o = fk.get(v, set()), ok.get(v, set())
        d1, d2 = f - o, o - f
        if d1 or d2:
            bad.append((v, sorted(d1)[:3], sorted(d2)[:3]))
    print("扫描卷数=%d（fragments 有账 %d／outline 有行 %d）" % (len(vols), len(fk), len(ok)))
    if bad:
        for v, d1, d2 in bad:
            print("FAIL V%03d fragments缺于outline=%s outline缺于fragments=%s" % (v, d1, d2))
        print("键集守卫：FAIL %d 卷——禁止跑 merge --write（他线在途或台账失步）" % len(bad))
        return 1
    print("键集守卫：PASS 全库一致——merge --write 可行")
    return 0


if __name__ == "__main__":
    sys.exit(main())
