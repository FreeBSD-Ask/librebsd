# -*- coding: utf-8 -*-
"""通用候选分件合并器（参数化 fpa_b127 版）。

用法: python _merge_cand.py <tag> <N> <LO> <HI> [--srcdb <xxx.duckdb>]
输入: review_logs/<tag>_candidates_p1..N.txt  (pk|L|摘要)
输出: review_logs/<tag>_candidates.txt
校验: 剥 BOM、字段数 3、等级 ∈{L3,L4}、长度 20-80、pk 越界、pk 重复、禁字符
      [--srcdb] 追加校验 pk 真在源库 messages 表存在（缺省不查，保持旧行为）

为什么有 --srcdb（2026-09-22 freebsd-alpha 批3 实测）：
    pk 842751 是读手臆造的，库里根本没有这行。它同时满足 pk_range、升序、唯一、
    摘要长度、禁字符五道检查，全绿通过合并，最后由宿主分派表的「源库缺行」暴露。
    结构校验查不出"越界之外的不存在"，只有回库查存在性才行。
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RL = os.path.join(HERE, "review_logs")

tag = sys.argv[1]
N = int(sys.argv[2])
LO, HI = int(sys.argv[3]), int(sys.argv[4])

# 可选 --srcdb <路径>：位置参数在 --srcdb 之前，故 argv[1..4] 恒为 tag/N/LO/HI。
SRCDB = None
if "--srcdb" in sys.argv:
    i = sys.argv.index("--srcdb")
    if i + 1 >= len(sys.argv):
        raise SystemExit("--srcdb 缺路径")
    SRCDB = sys.argv[i + 1]

rows = []
bad = []
seen = set()
per = []
for k in range(1, N + 1):
    # 读手命名四种口径并存：`_candidates_p%d`（原始）、`_candidates_p%02d`（fq_b065 起部分读手
    # 照 agent 名零填充写）、`_cand_p%d`（fpo_b177／fn_b173／fbug_b193 起的任务书短写口径）、
    # `_candidates_part%d`（h5sec_b526_3 起，与 digest_part<K> 输入口径对齐）。
    # 都认收；并存时按 mtime 取新，只提示不判违规——谁最后写的就是谁的。
    cand = [os.path.join(RL, "%s_candidates_p%d.txt" % (tag, k)),
            os.path.join(RL, "%s_candidates_p%02d.txt" % (tag, k)),
            os.path.join(RL, "%s_cand_p%d.txt" % (tag, k)),
            os.path.join(RL, "%s_cand_p%02d.txt" % (tag, k)),
            os.path.join(RL, "%s_candidates_part%d.txt" % (tag, k)),
            os.path.join(RL, "%s_candidates_part%02d.txt" % (tag, k)),
            os.path.join(RL, "%s_cand_part%d.txt" % (tag, k)),
            os.path.join(RL, "%s_cand_part%02d.txt" % (tag, k))]
    # p10..p99 时 p%d 与 p%02d 是同一个字符串，去重避免误报「两种命名并存」
    cand = list(dict.fromkeys(cand))
    hits = [c for c in cand if os.path.exists(c)]
    if not hits:
        bad.append((k, u"缺文件", ""))
        per.append((k, 0))
        continue
    if len(hits) > 1:
        print(u"  ! p%d 两种命名并存，按 mtime 取新: %s" % (k,
              ", ".join(os.path.basename(h) for h in hits)))
    p = max(hits, key=os.path.getmtime)
    raw = io.open(p, "rb").read()
    if raw.startswith(b"\xef\xbb\xbf"):
        bad.append((k, u"BOM（已剥）", ""))
        raw = raw[3:]
    if b"\r\n" in raw:
        bad.append((k, "CRLF", ""))
    txt = raw.decode("utf-8")
    n = 0
    for ln in txt.splitlines():
        if not ln.strip():
            continue
        n += 1
        parts = ln.split("|")
        if len(parts) != 3:
            bad.append((k, u"字段数 %d" % len(parts), ln[:60]))
            continue
        pk, lv, summ = parts
        if not re.fullmatch(r"\d+", pk):
            bad.append((k, u"pk 非数字", pk))
            continue
        if lv not in ("L3", "L4"):
            bad.append((k, u"等级非法", lv))
            continue
        if pk in seen:
            bad.append((k, u"pk 重复", pk))
            continue
        seen.add(pk)
        L = len(summ)
        forb = "".join(c for c in u"\u300c\u300d*\\|" if c in summ)
        if L < 20 or L > 80 or forb:
            bad.append((k, u"摘要越限 L=%d forb=%s" % (L, forb or "-"), pk))
        if not (LO <= int(pk) <= HI):
            bad.append((k, u"pk 越界", pk))
        rows.append((int(pk), lv, summ))
    per.append((k, n))

# BOM 已在读入时剥掉，CRLF 属平台提示；其余都是硬结构错误，不得带着缺行写出。
# fq_b045 p2 曾以空格分隔写出：51 行被判违规但仍合并出 156 行文件，下游照收。
hard = [b for b in bad if not b[1].startswith((u"BOM", "CRLF"))]
if hard:
    print(u"[中止] %d 条硬违规，未写盘（已解析 %d 行、丢弃 %d 行）"
          % (len(hard), len(rows), sum(n for _, n in per) - len(rows)))
    for b in hard[:30]:
        print(u"  p%s %s %s" % b)
    sys.exit(2)

# 🔴 存在性校验（仅 --srcdb 时）：pk 在 pk_range 内不等于真存在。
# 842751 满足全部结构检查却在库里根本没有，最后才由宿主分派表暴露。
if SRCDB:
    import duckdb
    con = duckdb.connect(SRCDB, read_only=True)
    have = set(int(x[0]) for x in con.execute(
        "SELECT CAST(id AS BIGINT) FROM messages "
        "WHERE CAST(id AS BIGINT) BETWEEN ? AND ?", [LO, HI]).fetchall())
    con.close()
    # seen 里存的是字符串（split 出来的），have 是 int，必须转成 int 再比对。
    ghost = sorted(int(pk) for pk in seen if int(pk) not in have)
    if ghost:
        rows = [r for r in rows if r[0] not in set(ghost)]
        print(u"!! 源库不存在的臆造 pk %d 个，已剔除: %s" % (len(ghost), ghost[:15]))
    else:
        print(u"源库存在性: 全部 %d 个 pk 命中 messages 表" % len(seen))
    if not rows:
        raise SystemExit(u"[中止] 剔除臆造 pk 后无行可写")

rows.sort(key=lambda r: r[0])
lens = [len(r[2]) for r in rows]
dist = {}
for r in rows:
    dist[r[1]] = dist.get(r[1], 0) + 1

print(u"分件行数: %s" % u" ".join(u"p%d=%d" % x for x in per))
print(u"合并 %d 条 | 唯一 %d | 升序 %s" % (len(rows), len(seen), True))
print(u"等级: %s" % sorted(dist.items()))
print(u"摘要长度 min/max/avg: %d/%d/%.1f" % (min(lens), max(lens), sum(lens) / len(lens)))
print(u"违规 %d" % len(bad))
for b in bad[:30]:
    print(u"  p%s %s %s" % b)

out = os.path.join(RL, "%s_candidates.txt" % tag)
io.open(out, "w", encoding="utf-8", newline="\n").write(
    u"\n".join(u"%d|%s|%s" % r for r in rows) + u"\n")
print(u"[写盘] %s" % out)
