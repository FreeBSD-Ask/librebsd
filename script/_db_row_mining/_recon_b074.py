# -*- coding: utf-8 -*-
"""fq_b074 建批后一次性取证（只读，不做任何写入）。

本线近批段结构各不相同——b066 单段、b067 正向双段（跳变点 2303983）、
b068／b069 反向双段、b070／b071 正向、b072／b073 正向双段——
所以本批段结构**不可假设**，必须实测。本脚本一次性回答：
  1) pk 窗两端点 date；
  2) 占位日期封（YYYY-01-01T00:00:00）——不参与单调性判断，单列普查；
  3) date 回退点（剔占位后 rows 内相邻比较）→ 由回退点切出的各段（起止 pk、方向、封数）；
  4) 大跨度正向跳变（相邻有效封间隔 > 7 天）；
  5) 8 份分件（各 250 行）的 pk / date 范围与跨段情况；
  6) 无头封普查（date 占位／空、from 与 subject 皆空、合成 <no-id-…> message_id）；
  7) 月份分布（含占位）；
  8) 正文长度分布 ＋ 疑似硬截断；
  9) 全窗版本 token 频次统计（**陷阱表必须全窗实测，不得凭记忆**——
     零命中串进 TRAP_UP，有命中串进 WATCH 逐封回源）。

🔴 坑 1：**本批成员一律以 digest 的 pk 列表为准，不得用 pk 区间取。**
   `messages.id` 是 VARCHAR，`WHERE id>='2316696'` 走**字典序**，库内存在短 id `231`，
   会被字典序捞进来。凡用区间取必须再按 digest 成员过滤。
🔴 坑 2：**绝不能用 `int(pk) - LO` 当 rows 下标**——一律走 rows 自带的位置。
🔴 坑 3（b073 新增）：占位封共两族——`date='YYYY-01-01T00:00:00'` 一族，
   以及 `date` 有值但 `date_local IS NULL` 一族（b073 的 2314933／2316064 即后者，
   date 列本身是 2007-01-01 占位）。两族都要单列。
"""
import collections
import datetime as _dt
import io
import os
import re
import sys

import duckdb

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
DB = "d:/librebsd/03-原始史料库/11-邮件列表史料/01-freebsd/db/freebsd-questions.duckdb"
DIG = os.path.join(HERE, "review_logs", "fq_b074_digest.txt")
PART = 250
PLACEHOLDER = re.compile(r"^\d{4}-01-01T00:00:00")

BPK = [int(l.split("|", 1)[0]) for l in io.open(DIG, encoding="utf-8") if l.strip()]
assert len(BPK) == 2000, len(BPK)
assert BPK == sorted(BPK), "digest 序非 pk 升序"

con = duckdb.connect(DB, read_only=True)
raw = con.execute(
    "SELECT id, coalesce(date,''), coalesce(date_local,''), coalesce(from_name,''), "
    "coalesce(subject,''), coalesce(message_id,''), coalesce(body,'') "
    "FROM messages WHERE CAST(id AS BIGINT) >= %d AND CAST(id AS BIGINT) <= %d "
    "ORDER BY CAST(id AS BIGINT)" % (min(BPK), max(BPK))).fetchall()
con.close()
BPK_SET = set(BPK)
rows = [(int(r[0]), r[1], r[2], r[3], r[4], r[5], r[6]) for r in raw if int(r[0]) in BPK_SET]
rows.sort(key=lambda x: x[0])
assert len(rows) == 2000, "过滤后应为 2000 行，实为 %d" % len(rows)

print("=== 0) 窗口 ===")
print("  digest 成员 2000 封，pk 跨距 %d–%d" % (rows[0][0], rows[-1][0]))
phantom = [int(r[0]) for r in raw if int(r[0]) not in BPK_SET]
print("  区间内但**不属本批**（字典序伪命中）：%d 个 %s" % (len(phantom), phantom))
pk_of = {r[0] for r in rows}
gap = sorted(set(range(rows[0][0], rows[-1][0] + 1)) - pk_of)
print("  库内 pk 缺口：%d 个 %s" % (len(gap), gap if len(gap) < 25 else gap[:25]))

print("\n=== 1) 端点 ===")
print("  首 pk %d  %s  %r" % (rows[0][0], rows[0][1], rows[0][4][:44]))
print("  末 pk %d  %s  %r" % (rows[-1][0], rows[-1][1], rows[-1][4][:44]))

print("\n=== 2) 占位日期族（先剔除，不参与回退判断）===")
ph_date = [r[0] for r in rows if PLACEHOLDER.match(r[1])]
no_local = [r[0] for r in rows if r[1] and not r[2].strip()]
print("  族A date=YYYY-01-01T00:00:00：%d 封 %s" % (len(ph_date), ph_date))
print("  族B date_local 为空：%d 封 %s" % (len(no_local), no_local))
for pk in sorted(set(ph_date) | set(no_local)):
    r = [x for x in rows if x[0] == pk][0]
    print("    pk %d  date=%r from=%r subj=%r msgid=%r"
          % (pk, r[1][:19], r[3][:20], r[4][:30], r[5][:26]))

print("\n=== 3) date 回退点（**剔除占位后**，rows 内相邻比较）===")
live = [r for r in rows if r[1] and not PLACEHOLDER.match(r[1])]
cuts = []
for i in range(1, len(live)):
    if live[i][1] < live[i - 1][1]:
        cuts.append(i)
        print("  -> 断点：pk %d %s  ->  pk %d %s"
              % (live[i - 1][0], live[i - 1][1], live[i][0], live[i][1]))
print("  有效封数（剔占位后）%d；断点数：%d" % (len(live), len(cuts)))

print("\n=== 4) 各段 ===")
bounds = [0] + cuts + [len(live)]
for a, b in zip(bounds[:-1], bounds[1:]):
    seg = live[a:b]
    ds = [r[1] for r in seg]
    mono_up = all(ds[j] <= ds[j + 1] for j in range(len(ds) - 1))
    mono_dn = all(ds[j] >= ds[j + 1] for j in range(len(ds) - 1))
    tag = "升序" if mono_up else ("降序" if mono_dn else "非单调")
    print("  段 pk %d-%d（%d 封）%s   %s -> %s"
          % (seg[0][0], seg[-1][0], len(seg), tag, min(ds), max(ds)))

print("\n=== 5) 大跨度正向跳变（相邻有效封间隔 > 7 天）===")


def _d(s):
    return _dt.datetime.strptime(s[:19], "%Y-%m-%dT%H:%M:%S")


for i in range(1, len(live)):
    try:
        gapd = (_d(live[i][1]) - _d(live[i - 1][1])).days
    except ValueError:
        continue
    if gapd > 7:
        print("  跳变 %4d 天：pk %d %s -> pk %d %s"
              % (gapd, live[i - 1][0], live[i - 1][1][:10], live[i][0], live[i][1][:10]))

print("\n=== 6) 8 份分件的 pk / date 范围与跨段 ===")
cut_pk = set(live[i][0] for i in cuts)
for k in range(8):
    seg = rows[k * PART:(k + 1) * PART]
    ds = [r[1] for r in seg if r[1] and not PLACEHOLDER.match(r[1])]
    crossed = [p for p in sorted(cut_pk) if seg[0][0] < p <= seg[-1][0]]
    print("  p%d  pk %d-%d  %s -> %s  跨段 %s"
          % (k + 1, seg[0][0], seg[-1][0], min(ds), max(ds),
             "无" if not crossed else "pk" + u"\u3001".join(str(c) for c in crossed)))

print("\n=== 7) 无头封普查 ===")
empty_fs = [r[0] for r in rows if not r[3].strip() and not r[4].strip()]
nosid = [r[0] for r in rows if r[5].startswith("<no-id-")]
nodate = [r[0] for r in rows if not r[1].strip()]
print("  from 与 subject 皆空：%d %s" % (len(empty_fs), empty_fs[:20]))
print("  合成 <no-id-...>：%d %s" % (len(nosid), nosid[:20]))
print("  date 空：%d %s" % (len(nodate), nodate[:20]))
for pk in sorted(set(empty_fs) | set(nosid) | set(nodate) | set(ph_date))[:20]:
    r = [x for x in rows if x[0] == pk][0]
    print("    pk %d  date=%r from=%r subj=%r" % (pk, r[1][:19], r[3][:20], r[4][:30]))

print("\n=== 8) 月份分布（含占位）===")
mc = collections.Counter(r[1][:7] for r in rows if r[1])
for m, c in sorted(mc.items()):
    print("  %s  %d" % (m, c))

print("\n=== 9) 正文长度 ===")
bl = sorted(len(r[6]) for r in rows)
print("  min=%d  max=%d  中位=%d  均=%.0f"
      % (bl[0], bl[-1], bl[len(bl) // 2], sum(bl) / float(len(bl))))
print("  >4000 字：%d 封" % len([r for r in rows if len(r[6]) > 4000]))
for r in sorted(rows, key=lambda x: -len(x[6]))[:12]:
    print("    pk %d  %d 字" % (r[0], len(r[6])))
print("  <200 字：%d 封" % len([r for r in rows if len(r[6]) < 200]))
print("  空正文： %d 封" % len([r for r in rows if not r[6]]))

print("\n=== 10) 源库正文疑似硬截断 ===")
trunc = []
for r in rows:
    tail = r[6].rstrip()[-12:]
    if len(tail) >= 8 and " " not in tail and tail[-1].isalpha():
        trunc.append(r[0])
print("  疑似硬截断：%d 封" % len(trunc))
for pk in trunc[:10]:
    r = [x for x in rows if x[0] == pk][0]
    print("    pk %d  尾 30 字：...%r" % (pk, r[6].rstrip()[-30:]))

print("\n=== 11) 全窗版本 token 频次（**陷阱表必须全窗实测，不得凭记忆**）===")
# 抽形如 4.11-RELEASE-p7 / 5.2.1-RELEASE / 7.0-beta4 / 6.3-prerelease / 5.6-STABLE-p1
VER = re.compile(
    r"\b\d{1,2}\.\d{1,2}(?:\.\d{1,2})?-"
    r"(?:RELEASE|STABLE|CURRENT|PRERELEASE|PRERELASE|BETA|RC|ALPHA|DEVEL)"
    r"(?:-?\d+|-p\d+)?",
    re.IGNORECASE,
)
corpus = [(r[0], (r[4] + "\n" + r[6]).upper()) for r in rows]
cnt = collections.Counter()
for pk, up in corpus:
    for m in VER.finditer(up):
        cnt[m.group(0).upper()] += 1
print("  全窗版本串种类 %d，总命中 %d" % (len(cnt), sum(cnt.values())))
for s in sorted(cnt):
    print("    %-28s %d" % (s, cnt[s]))

# 候选串逐个「全窗裸子串计数」：0 命中者方可进 TRAP_UP，有命中者进 WATCH 逐封回源
CANDIDATES = [
    "4.11-RELEASE", "4.11-STABLE", "5.2.1-RELEASE", "5.3-RELEASE", "5.6-RELEASE",
    "5.7-RELEASE", "5.8-RELEASE", "6.2-PRERELEASE", "6.2-RC1", "6.2-RC2", "6.2-RC3",
    "6.3-BETA1", "6.3-RC2", "6.4-RELEASE", "7.0-BETA1", "7.0-RC2", "7.0-PRERELEASE",
    "7.0-RC3", "7.1-RELEASE", "7.1-BETA", "8.0-RELEASE", "8.0-BETA", "8.0-RC",
    "4.10-RELEASE", "5.4-RELEASE", "5.5-RELEASE", "6.0-STABLE", "6.1-RC",
    "7.0-RELEASE", "6.3-RELEASE", "7.0-RC1", "6.3-RC1", "6.1-STABLE",
    "6.2-RELEASE", "7.0-BETA", "6.1-RELEASE",
]
print("\n  候选串全窗命中数（**0 命中者方可进 TRAP_UP**）：")
for s in CANDIDATES:
    hits = sum(1 for _pk, up in corpus if s.upper() in up)
    print("    %-24s %d %s" % (s, hits, "<-- TRAP_UP 候选" if hits == 0 else ""))
