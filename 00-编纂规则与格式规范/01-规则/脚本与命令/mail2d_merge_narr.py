# -*- coding: utf-8 -*-
"""通用叙述分件合并器（pa_b083 版参数化）。

用法: python _merge_narr.py <tag> <N> <host1,host2,...>
输入: review_logs/<tag>_mount_narr_p1..N.tsv   (pk\thost\t叙述)
      review_logs/<tag>_candidates.txt          (权威 pk 全集)
输出: review_logs/<tag>_mount_narr.tsv
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RL = os.path.join(HERE, "review_logs")

tag = sys.argv[1]
N = int(sys.argv[2])
HOSTS = set(sys.argv[3].split(","))


def read_clean(path):
    b = io.open(path, "rb").read()
    if b.startswith(b"\xef\xbb\xbf"):
        b = b[3:]
    return b.decode("utf-8")


cand = [ln.split("|")[0] for ln in read_clean(
    os.path.join(RL, "%s_candidates.txt" % tag)).splitlines() if ln.strip()]

rows = []
bad = []
seen = set()
for k in range(1, N + 1):
    p = os.path.join(RL, "%s_mount_narr_p%d.tsv" % (tag, k))
    if not os.path.exists(p):
        bad.append((k, u"缺文件", ""))
        print(u"p%-2d 缺文件" % k)
        continue
    raw = io.open(p, "rb").read()
    if b"\r\n" in raw:
        bad.append((k, "CRLF", ""))
    txt = read_clean(p)
    n = 0
    for ln in txt.splitlines():
        if not ln.strip():
            continue
        n += 1
        parts = ln.split("\t")
        if len(parts) != 3:
            bad.append((k, u"字段数 %d" % len(parts), ln[:60]))
            continue
        pk, hk, narr = parts
        if not re.fullmatch(r"\d+", pk):
            bad.append((k, u"pk 非数字", pk))
            continue
        if hk not in HOSTS:
            bad.append((k, u"host 非法", hk))
            continue
        if pk in seen:
            bad.append((k, u"pk 重复", pk))
            continue
        seen.add(pk)
        L = len(narr)
        forb = "".join(c for c in u"\u300c\u300d*\\|" if c in narr)
        if L < 60 or L > 140 or forb:
            bad.append((k, u"叙述越限 L=%d forb=%s" % (L, forb or "-"), pk))
        rows.append((pk, hk, narr))
    print(u"p%-2d 行数 %d" % (k, n))

rows.sort(key=lambda r: int(r[0]))
pks = [r[0] for r in rows]
missing = [p for p in cand if p not in seen]
extra = [p for p in pks if p not in set(cand)]

print(u"\n合并条数: %d | 候选全集: %d" % (len(rows), len(cand)))
print(u"缺: %d %s" % (len(missing), missing[:10]))
print(u"多: %d %s" % (len(extra), extra[:10]))
print(u"升序: %s" % (pks == sorted(pks, key=int)))
dist = {}
for r in rows:
    dist[r[1]] = dist.get(r[1], 0) + 1
print(u"host 分布: %s" % sorted(dist.items()))
lens = [len(r[2]) for r in rows]
if lens:
    print(u"叙述长度 min/max/avg: %d/%d/%.1f" % (min(lens), max(lens), sum(lens) / len(lens)))
else:
    print(u"叙述长度 min/max/avg: -(无叙述行)")
print(u"违规: %d" % len(bad))
for b in bad[:20]:
    print(u"  p%s %s %s" % b)

# 🔴 阻断级：缺文件/CRLF/空集一律中止不写盘，避免不完整总表覆盖（对齐 _merge_parts.py 行为）
fatal = [b for b in bad if b[1] in (u"缺文件", "CRLF")]
if fatal or not rows:
    print(u"[中止] 阻断级问题 %d 项（缺文件/CRLF/空集）：不写盘，保留既有 %s" % (len(fatal) or 1, out if 'out' in dir() else "<tag>_mount_narr.tsv"))
    print(u"        -> 先补齐缺失分件再跑本脚本")
    sys.exit(1)

out = os.path.join(RL, "%s_mount_narr.tsv" % tag)
io.open(out, "w", encoding="utf-8", newline="\n").write(
    u"\n".join(u"%s\t%s\t%s" % r for r in rows) + u"\n")
print(u"[写盘] %s" % out)
