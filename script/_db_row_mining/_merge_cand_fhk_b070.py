# -*- coding: utf-8 -*-
"""fhk_b070 候选合并：40 片 -> fhk_b070_candidates.txt。
外科修长度（>80 截断到 80）、去重、去空行、去注释行，输出按 pk 升序。
只改摘要越界，不动 pk/等级；截断在字符边界，不补全注。
"""
import io
import os
import sys
import collections

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(HERE, "review_logs")
TAG = "fhk_b070"
N = 40
MAX_SUM = 80

def part_path(k):
    for f in ("%s_candidates_p%d.txt" % (TAG, k),
              "%s_candidates_p%02d.txt" % (TAG, k)):
        p = os.path.join(LOG, f)
        if os.path.exists(p):
            return p
    return os.path.join(LOG, "%s_candidates_p%d.txt" % (TAG, k))

rows = collections.OrderedDict()
stats = []
for k in range(1, N + 1):
    p = part_path(k)
    if not os.path.exists(p):
        print("缺 p%d" % k)
        continue
    raw = open(p, "rb").read()
    probs = []
    if raw[:3] == b"\xef\xbb\xbf":
        probs.append("BOM")
    if b"\r" in raw:
        probs.append("CR")
    txt = raw.decode("utf-8")
    n = 0
    for ln in txt.split("\n"):
        s = ln.strip()
        if not s or s.startswith("#"):
            continue
        f = ln.split("|", 2)
        if len(f) != 3:
            probs.append("字段%d:%s" % (len(f), s[:24]))
            continue
        pk, lvl, summ = f[0].strip(), f[1].strip(), f[2].strip()
        if not pk.isdigit():
            probs.append("pk非数字:%s" % pk)
            continue
        if lvl not in ("L3", "L4"):
            probs.append("等级%s:%s" % (lvl, pk))
            continue
        cut = ""
        if len(summ) > MAX_SUM:
            cut = "截断%d->%d" % (len(summ), MAX_SUM)
            summ = summ[:MAX_SUM]
        prev = rows.get(pk)
        if prev is not None:
            probs.append("跨片重复pk %s（p%d 已有）" % (pk, prev[0]))
            continue
        rows[pk] = (k, lvl, summ)
        n += 1
        if cut:
            probs.append("%s %s" % (pk, cut))
    stats.append((k, n, probs))

out = []
for pk in sorted(rows, key=int):
    k, lvl, summ = rows[pk]
    out.append("%s|%s|%s" % (pk, lvl, summ))

with io.open(os.path.join(LOG, TAG + "_candidates.txt"), "w",
             encoding="utf-8", newline="\n") as fh:
    fh.write("\n".join(out) + "\n")

print("=" * 70)
print("%s 候选合并：%d 片 -> %d 条" % (TAG, len(stats), len(out)))
lv = collections.Counter(r[1] for r in rows.values())
print("等级分布 L4=%d L3=%d" % (lv["L4"], lv["L3"]))
print("pk 范围 %s - %s" % (out[0].split("|")[0], out[-1].split("|")[0]))
print("-" * 70)
tot = 0
for k, n, probs in stats:
    tot += n
    tag = "" if not probs else "  " + "; ".join(probs[:4]) + ("…" if len(probs) > 4 else "")
    print("p%02d %3d%s" % (k, n, tag))
print("-" * 70)
print("分片计数合计 %d，去重后落盘 %d" % (tot, len(out)))
assert len(out) == len(rows)
