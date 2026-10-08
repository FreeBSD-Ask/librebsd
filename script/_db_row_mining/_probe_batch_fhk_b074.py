# -*- coding: utf-8 -*-
"""fhk_b074 建批取证（只读源库）：坐标、跳号、月份分布、无头封、正文截断率。

口径与 _batch_fhk_b072.json 同款：选行 ORDER BY CAST(id AS BIGINT) ASC
LIMIT 2000 OFFSET 146000，即库内序 146001-148000。
输出 review_logs/fhk_b074_probe.txt，不写 claim 库、不写大纲、不建批 JSON
（宿主裁定需主会话据月份分布人工过目后落 _batch_fhk_b074.json）。

用法: python _probe_batch_fhk_b074.py
"""
import io
import os
import sys
from collections import Counter

import duckdb

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
RL = os.path.join(HERE, "review_logs")
TAG = "fhk_b074"
DB = (r"d:\librebsd\03-原始史料库\11-邮件列表史料\01-freebsd\db"
      r"\freebsd-hackers.duckdb")
OFFSET, N = 146000, 2000

con = duckdb.connect(DB, read_only=True)
rows = con.execute(
    "SELECT CAST(id AS BIGINT), date, from_name, subject, body FROM messages "
    "ORDER BY CAST(id AS BIGINT) ASC LIMIT ? OFFSET ?", [N, OFFSET]).fetchall()
# 前后各多取 3 行做边界对照
prev = con.execute(
    "SELECT CAST(id AS BIGINT), date FROM messages "
    "ORDER BY CAST(id AS BIGINT) DESC LIMIT 3 OFFSET ?", [OFFSET]).fetchall()
con.close()
assert len(rows) == N, "取到 %d 行非 %d" % (len(rows), N)

out = []
P = out.append
pks = [int(r[0]) for r in rows]
assert pks == sorted(pks) and len(set(pks)) == len(pks), "pk 非升序或重复"
P("== %s 建批取证（OFFSET=%d，库内序 %d-%d）==" % (TAG, OFFSET, OFFSET + 1, OFFSET + N))
P("取行 %d | pk %d ~ %d | span %d" % (len(rows), pks[0], pks[-1], pks[-1] - pks[0] + 1))
P("上一批末 3 行: " + " / ".join("%d %s" % (p, str(d)[:10]) for p, d in prev))

dates = [str(r[1])[:10] for r in rows]
P("日期 min=%s  max=%s" % (min(dates), max(dates)))
md = Counter(dates)
P("月份分布: " + " / ".join("%s=%d" % kv for kv in sorted(md.items())))

# 日期回卷点
drops = [(pks[i - 1], dates[i - 1], pks[i], dates[i]) for i in range(1, len(rows))
         if dates[i] < dates[i - 1]]
P("日期回卷点 %d 处" % len(drops))
for d0 in drops[:12]:
    P("   pk %d(%s) -> pk %d(%s)" % d0)

# 跳号
missing = sorted(set(range(pks[0], pks[-1] + 1)) - set(pks))
P("跳号 %d 个: %s" % (len(missing), missing if missing else "无"))

# 正文
bl = [len((r[4] or "")) for r in rows]
P("正文 len max=%d  均值=%.0f  >20=%d  <=20=%d  空=%d"
  % (max(bl), sum(bl) / len(bl), sum(1 for x in bl if x > 20),
     sum(1 for x in bl if 0 < x <= 20), sum(1 for x in bl if x == 0)))
P("空 subject=%d  空 from_name=%d"
  % (sum(1 for r in rows if not (r[3] or "").strip()),
     sum(1 for r in rows if not (r[2] or "").strip())))

# 头部空字段（导入层无头封）
headless = [int(r[0]) for r in rows
            if not (r[3] or "").strip() and not (r[2] or "").strip()]
P("全头空 pk %d 个: %s" % (len(headless), headless[:20]))
nosem = [int(r[0]) for r in rows if not (r[3] or "").strip()]
P("subject 空 pk %d 个: %s" % (len(nosem), nosem[:20]))

s = "\n".join(out) + "\n"
p = os.path.join(RL, "%s_probe.txt" % TAG)
io.open(p, "w", encoding="utf-8", newline="\n").write(s)
print(s)
print("[写盘] %s (%d B)" % (p, len(s.encode("utf-8"))))
