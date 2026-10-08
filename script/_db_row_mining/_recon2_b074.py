# -*- coding: utf-8 -*-
"""fq_b074 二轮取证（只读）：
  A) 占位封 2317892／2318305 的日期复原——source_file 定月 + 邻居 date_local 双端夹取定日；
  B) 稀有版本串定位到 pk（判定落在段A 2007-12-31 还是段B 2007-02，决定其合法性）；
  C) 全窗 6.3*／7.0* 形态普查（6.3-RELEASE 2007-07-29 发布、7.0-RELEASE 2008-03 发布，
     段B 2007-02 内出现即高度可疑）。
"""
import io
import os
import re
import sys

import duckdb

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
DB = "d:/librebsd/03-原始史料库/11-邮件列表史料/01-freebsd/db/freebsd-questions.duckdb"
PH = [2317892, 2318305]

con = duckdb.connect(DB, read_only=True)

print("=== A) 占位封日期复原 ===")
for pk in PH:
    src = con.execute(
        "SELECT coalesce(source_file,'') FROM messages WHERE CAST(id AS BIGINT)=?", [pk]).fetchone()
    nb = con.execute(
        "SELECT CAST(id AS BIGINT), date_local, coalesce(subject,'') "
        "FROM messages WHERE CAST(id AS BIGINT) IN (?, ?, ?, ?) ORDER BY 1",
        [pk - 1, pk, pk + 1, pk + 2]).fetchall()
    print("  pk %d  source_file=%r" % (pk, (src or [""])[0]))
    for r in nb:
        print("      邻居 pk %d  date_local=%r  subj=%r" % (r[0], r[1], r[2][:40]))
    print("      date_local NULL 计数（本 pk 邻域）：见上；月取自 source_file，日取双端夹取")

print("\n=== B) 稀有版本串定位 ===")
RARE = ["7.0-BETA2", "7.0-CURRENT-200702", "5.1.11-BETA", "1.6-RC1",
        "6.2-PRERELEASE", "6.2-RC1", "6.2-RC2", "6.1-STABLE-200609",
        "5.4-STABLE", "5.5-STABLE", "7.0-BETA"]
allrows = con.execute(
    "SELECT CAST(id AS BIGINT), coalesce(date,''), coalesce(subject,''), coalesce(body,'') "
    "FROM messages WHERE CAST(id AS BIGINT) BETWEEN 2316696 AND 2318701 "
    "ORDER BY 1").fetchall()
con.close()
for s in RARE:
    hits = [(p, d[:10], subj[:38]) for p, d, subj, body in allrows
            if s.upper() in (subj + "\n" + body).upper()]
    print("  %-22s %d 处" % (s, len(hits)))
    for p, d, subj in hits[:6]:
        seg = "段A(2007-12-31)" if p <= 2316748 else "段B(2007-02)"
        print("      pk %d  %s  %s  %r" % (p, d, seg, subj))

print("\n=== C) 全窗 6.3* 与 7.0* 形态普查 ===")
V = re.compile(r"\b(?:6\.\d|7\.\d|8\.\d)\.\d*(?:[A-Z0-9-]+)?", re.IGNORECASE)
import collections
c = collections.Counter()
loc = {}
for p, d, subj, body in allrows:
    up = (subj + "\n" + body).upper()
    for m in V.finditer(up):
        t = m.group(0).upper()
        if re.match(r"^(6\.[23]|7\.\d|8\.\d)", t):
            c[t] += 1
            loc.setdefault(t, []).append((p, d[:10]))
for t, n in sorted(c.items()):
    ps = sorted({x[0] for x in loc[t]})
    segs = sorted({"段A" if p <= 2316748 else "段B" for p in ps})
    print("  %-26s %4d 处 / %2d 封  %s  pk=%s" % (t, n, len(ps), "+".join(segs), ps[:8]))
