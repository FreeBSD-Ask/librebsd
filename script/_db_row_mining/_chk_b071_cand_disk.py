# -*- coding: utf-8 -*-
"""fhk_b071 候选分件磁盘验收（唯一地面真值）。

逐片核对：文件存在、三字段、等级合法、pk 归属本片 digest、摘要 20-80、
禁字符、尾标点、编码（无 BOM/CR）。再跨片核对：pk 全局唯一、无越界、
无源库缺号、无正文全空行。
"""
import io
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
RL = os.path.join(HERE, "review_logs")
TAG = "fhk_b071"
PK_LO, PK_HI = 2598421, 2600431
MISSING = {2599401, 2599717, 2599883, 2599929, 2599934, 2599935,
           2600069, 2600075, 2600077, 2600246, 2600283}
EMPTY_BODY = {2598732, 2599641}
BANNED = [u"\u300c", u"\u300d", "*", "\\", u"\u3000", "\t",
          "\"", "'", u"\u2018", u"\u2019", u"\u201c", u"\u201d", "`"]
TAIL = [u"\u3002", u"\uff0c", u"\uff1a", u"\uff1b", u"\uff1f",
        u"\uff01", u"\u3001", " ", "\t"]
# BLIND 行若被收录，只能按 subject 陈述主题：不得点名发帖人、不得写归属动词、
# 不得把 420 字窗口的可见性条件写进摘要。
BLIND_META = [u"\u672c\u7a97\u53e3", u"\u5f15\u7528\u5757", u"\u65e0\u81ea\u6709",
              u"\u4ec5\u89c1", u"\u622a\u65ad\u5916"]
BLIND_VERB = [u"\u8ba4\u4e3a", u"\u6307\u51fa", u"\u5efa\u8bae", u"\u786e\u8ba4",
              u"\u5ba3\u5e03", u"\u51b3\u5b9a", u"\u53d1\u73b0", u"\u8bc1\u660e",
              u"\u8868\u793a", u"\u5f3a\u8c03"]

# ---- 片归属（从落盘分片实测）----
part_of, part_lines = {}, {}
for k in range(1, 41):
    p = os.path.join(RL, "%s_digest_part%d.txt" % (TAG, k))
    if not os.path.exists(p):
        raise SystemExit("缺分片 part%d" % k)
    ls = [l for l in io.open(p, encoding="utf-8").read().split("\n") if l.strip()]
    part_lines[k] = len(ls)
    for l in ls:
        part_of[int(l.split("|", 1)[0])] = k
assert len(part_of) == 2000, "分片 pk 合计 %d != 2000" % len(part_of)

# ---- BLIND 清单 ----
blind = set()
for ln in io.open(os.path.join(RL, "_blind_%s.txt" % TAG), encoding="utf-8"):
    s = ln.strip()
    if s.startswith("p"):
        a = s[1:].split(" ", 1)
        for x in (a[1].split("/") if len(a) > 1 and a[1] else []):
            if x:
                blind.add(int(x))
assert len(blind) == 351, "BLIND %d != 351" % len(blind)

all_pks, fails, per, blind_collected = {}, [], [], []
for k in range(1, 41):
    p = os.path.join(RL, "%s_candidates_p%d.txt" % (TAG, k))
    if not os.path.exists(p):
        fails.append("缺 candidates_p%d" % k)
        per.append((k, -1, 0, 0))
        continue
    raw = io.open(p, "rb").read()
    if raw.startswith(b"\xef\xbb\xbf"):
        fails.append("p%d BOM" % k)
    if b"\r" in raw:
        fails.append("p%d CR" % k)
    lines = [l.rstrip("\n") for l in io.open(p, encoding="utf-8").read().split("\n") if l.strip()]
    n4 = n3 = 0
    for l in lines:
        f = l.split("|", 2)
        if len(f) != 3:
            fails.append("p%d 字段数 %d: %s" % (k, len(f), l[:40]))
            continue
        pk, lv, sm = int(f[0]), f[1].strip(), f[2]
        if lv not in ("L3", "L4"):
            fails.append("p%d pk %d 等级非法 %s" % (k, pk, lv))
            n4 += 1
        if lv == "L4":
            n4 += 1
        else:
            n3 += 1
        if pk not in part_of:
            fails.append("p%d pk %d 不在任何分片" % (k, pk))
        elif part_of[pk] != k:
            fails.append("p%d pk %d 实际属 part%d" % (k, pk, part_of[pk]))
        if pk < PK_LO or pk > PK_HI:
            fails.append("p%d pk %d 越界" % (k, pk))
        if pk in MISSING:
            fails.append("p%d pk %d 是源库缺号" % (k, pk))
        if pk in EMPTY_BODY:
            fails.append("p%d pk %d 正文全空却收录" % (k, pk))
        if pk in all_pks:
            fails.append("pk %d 重复出现于 p%d 与 p%d" % (pk, all_pks[pk], k))
        else:
            all_pks[pk] = k
        if not (20 <= len(sm) <= 80):
            fails.append("p%d pk %d 摘要 %d 字越界" % (k, pk, len(sm)))
        for b in BANNED:
            if b in sm:
                fails.append("p%d pk %d 摘要含禁字符 %r" % (k, pk, b))
        for t in TAIL:
            if sm.endswith(t):
                fails.append("p%d pk %d 摘要以 %r 收尾" % (k, pk, t))
                break
        if pk in blind:
            blind_collected.append(pk)
            if sm.startswith(u"\uff1a") or u"\uff1a" in sm[:14]:
                fails.append("p%d pk %d BLIND 行摘要点名发帖人: %s" % (k, pk, sm[:30]))
            for m in BLIND_META:
                if m in sm:
                    fails.append("p%d pk %d BLIND 行摘要泄漏窗口可见性元描述(%s): %s"
                                 % (k, pk, m, sm[:30]))
            for v in BLIND_VERB:
                if v in sm:
                    fails.append("p%d pk %d BLIND 行摘要含归属动词(%s): %s"
                                 % (k, pk, v, sm[:30]))
    per.append((k, len(lines), n4, n3))

tot = sum(x[1] for x in per)
tot4 = sum(x[2] for x in per)
tot3 = sum(x[3] for x in per)
print("=== 逐片 ===")
print("  %-4s %5s %5s %5s %8s" % ("part", "条数", "L4", "L3", "字节"))
for k, n, a, b in per:
    p = os.path.join(RL, "%s_candidates_p%d.txt" % (TAG, k))
    sz = os.path.getsize(p) if os.path.exists(p) else -1
    print("  p%-4d %5d %5d %5d %8d" % (k, n, a, b, sz))
print("=== 合计 %d 条 | L4 %d | L3 %3d | 分片行数合计 %d ==="
      % (tot, tot4, tot3, sum(part_lines.values())))
print("L3 占比 %.1f%%" % (100.0 * tot3 / tot if tot else 0))
print("覆盖 pk %d 个（分片 2000 行，覆盖率 %.1f%%）"
      % (len(all_pks), 100.0 * len(all_pks) / 2000))
print("BLIND 被收录 %d 条（须按 subject 陈述、不点人名、不断言结论）" % len(blind_collected))
print("BLIND 未收录 %d / %d" % (len(blind) - len(blind_collected), len(blind)))
print()
if fails:
    print("=== 门禁 FAIL %d 项 ===" % len(fails))
    for f in fails:
        print("  " + f)
else:
    print("=== 门禁 PASS：格式/归属/长度/禁字符/尾标点/编码/唯一性 全部通过 ===")
