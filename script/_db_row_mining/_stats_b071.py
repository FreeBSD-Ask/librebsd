# -*- coding: utf-8 -*-
"""fhk_b071 建批统计（只读）：月份分布、正文分布、年度切分。写 review_logs/fhk_b071_stats.txt。"""
import io
import os
from collections import Counter

import duckdb

DB = r"d:\librebsd\03-原始史料库\11-邮件列表史料\01-freebsd\db\freebsd-hackers.duckdb"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "review_logs", "fhk_b071_stats.txt")
con = duckdb.connect(DB, read_only=True)
rows = con.execute(
    "SELECT CAST(id AS BIGINT), date, from_name, subject, body FROM messages "
    "ORDER BY CAST(id AS BIGINT) ASC LIMIT 2000 OFFSET 140000").fetchall()
con.close()
assert len(rows) == 2000

out = []
P = out.append
md = Counter(str(r[1])[:7] for r in rows)
P("month_dist:")
for k in sorted(md):
    P("  %s: %d" % (k, md[k]))
yr = {}
for k, v in md.items():
    yr[k[:4]] = yr.get(k[:4], 0) + v
P("年段切分: " + " / ".join("%s=%d" % kv for kv in sorted(yr.items())))
bl = [len((r[4] or "")) for r in rows]
P("body >20=%d  <=20=%d  空=%d  max=%d  均值=%.0f"
  % (sum(1 for x in bl if x > 20), sum(1 for x in bl if 0 < x <= 20),
     sum(1 for x in bl if x == 0), max(bl), sum(bl) / len(bl)))
P("date min=%s max=%s" % (min(str(r[1])[:10] for r in rows),
                          max(str(r[1])[:10] for r in rows)))
pks = [int(r[0]) for r in rows]
missing = sorted(set(range(pks[0], pks[-1] + 1)) - set(pks))
P("pk %d ~ %d  span %d  跳号 %d: %s"
  % (pks[0], pks[-1], pks[-1] - pks[0] + 1, len(missing), missing))
P("subject 空 %d: %s"
  % (sum(1 for r in rows if not (r[3] or "").strip()),
     [int(r[0]) for r in rows if not (r[3] or "").strip()]))
P("正文 <=20 字 %d: %s"
  % (sum(1 for r in rows if len(r[4] or "") <= 20),
     [int(r[0]) for r in rows if 0 < len(r[4] or "") <= 20]))
s = "\n".join(out) + "\n"
io.open(OUT, "w", encoding="utf-8", newline="\n").write(s)
print(s)
