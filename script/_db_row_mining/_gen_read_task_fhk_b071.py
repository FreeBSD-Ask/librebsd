# -*- coding: utf-8 -*-
"""生成 _READ_TASK_fhk_b071.md：以 b070 任务书为模板，逐处替换批次专属数值。

片表与 BLIND 按片分布一律从磁盘实测读取，不手填。
锚点字符串取自 _READ_TASK_fhk_b070.md 的**当前**内容（b070 终态），
不是 b069 时代的旧串——模板每升一批就要同步本表的锚点。
"""
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
RL = os.path.join(HERE, "review_logs")
TAG = "fhk_b071"
PREV = "_READ_TASK_fhk_b070.md"
spec = json.load(io.open(os.path.join(HERE, "_batch_%s.json" % TAG),
                         encoding="utf-8"))

# ---- 片表（从磁盘实测）----
rows = []
for k in range(1, 41):
    p = os.path.join(RL, "%s_digest_part%d.txt" % (TAG, k))
    assert os.path.exists(p), "缺片 part%d" % k
    L = [l for l in io.open(p, encoding="utf-8").read().split("\n") if l.strip()]
    pks = [int(l.split("|", 1)[0]) for l in L]
    rows.append((k, len(L), pks[0], pks[-1], os.path.getsize(p)))
assert sum(r[1] for r in rows) == 2000

tbl = []
line = []
for k, n, lo, hi, b in rows:
    line.append("p%02d %d %d-%d" % (k, n, lo, hi))
    if len(line) == 4:
        tbl.append(" ".join(line))
        line = []
if line:
    tbl.append(" ".join(line))

# ---- BLIND 按片分布（从 _blind 文件实测）----
bd = {}
for ln in io.open(os.path.join(RL, "_blind_%s.txt" % TAG), encoding="utf-8"):
    s = ln.strip()
    if s.startswith("p"):
        a = s[1:].split(" ", 1)
        n = int(a[0])
        bd[n] = len(a[1].split("/")) if len(a) > 1 and a[1] else 0
blind_total = sum(v for v in bd.values())
bdlines = []
buf = []
for k in range(1, 41):
    buf.append("p%02d:%d" % (k, bd.get(k, 0)))
    if len(buf) == 10:
        bdlines.append(" ".join(buf))
        buf = []
if buf:
    bdlines.append(" ".join(buf))

# ---- 空 subject 清单 / 缺号 / 空正文 ----
nos = ", ".join(str(x) for x in spec["empty_subject_pks"])
miss = "／".join(str(x) for x in spec["missing_pks"])
nfull = 325
ntrunc = 1673
nown = 1322
nempty = len(spec["short_body_pks"]) if False else 2
empty_pks = "[2598732、2599641]"
rate = 100.0 * blind_total / 2000
trunc_rate = 100.0 * ntrunc / 2000

t = io.open(os.path.join(HERE, PREV), encoding="utf-8").read()
t = t.replace("fhk_b070", TAG)
t = t.replace("库内序 **138001-140000**", "库内序 **140001-142000**")
t = t.replace("库内序 138001-140000", "库内序 140001-142000")
t = t.replace("pk **2596416-2598420**", "pk **2598421-2600431**")
t = t.replace("C:\Python314\python.exe", "python")
t = t.replace("C:/Python314/python.exe", "python")
t = t.replace("pk 2596416-2598420", "pk 2598421-2600431")

# 替换旧片表块
old_tbl_start = t.index("p01 ", t.index("本批已按 40 路切分"))
old_tbl_end = t.index("\n\n**下列纪律不变**", old_tbl_start)
t = t[:old_tbl_start] + "\n".join(tbl) + t[old_tbl_end:]

# 替换字节范围描述
t = re.sub(r"非尾片行数 \d+-\d+、字节 \d+-\d+；尾片 p40 \d+ 行 \d+ B",
           "非尾片行数 %d-%d、字节 %d-%d；尾片 p40 %d 行 %d B"
           % (min(r[1] for r in rows[:39]), max(r[1] for r in rows[:39]),
              min(r[4] for r in rows[:39]), max(r[4] for r in rows[:39]),
              rows[39][1], rows[39][4]), t)

# 批次结构段
t = t.replace(
    "区间共 2005 个编号、**缺 5 个编号：2597698／2597700／2597750／2598185／2598208**",
    "区间共 %d 个编号、**缺 %d 个编号：%s**"
    % (spec["pk_hi"] - spec["pk_lo"] + 1, len(spec["missing_pks"]), miss))
t = t.replace(
    "月份 1996-11=2 / 1997-09=1 / 1997-11=1530 / 1997-12=464 / 1998-11=1 / 2010-11=2"
    " 为主窗（1997-11=1530 / 1997-12=464），另有 6 封跨年代错序"
    "（1996-11-20×2 / 1997-09-08×1 / 1998-11-04×1 / 2010-11-24×2），"
    "日期 min=1996-11-20 / max=2010-11-24，",
    "月份 %s 为主窗（1997-12=877 / 1998-01=1120，跨年度），另有 3 封错序"
    "（1997-10-22×1 / 1997-12-04×1 / 2036-02-07×2，2036 系源库脏日期），"
    "日期 min=1997-10-22 / max=2036-02-07，"
    % " / ".join("%s=%d" % kv for kv in sorted(spec["month_dist"].items())))
t = t.replace(
    "空正文 0 行；空 subject 16 行 [2596447, 2596690, 2597140, 2597163, 2597172, "
    "2597220, 2597225, 2597664, 2597688, 2597689, 2597764, 2597768, 2598073, "
    "2598163, 2598164, 2598380]",
    "空正文 0 行；空 subject %d 行 [%s]" % (spec["empty_subject"], nos))
# 宿主时间带说明（本批跨年，按实测宿主内容带改口径）
t = t.replace(
    "全部归宿主 88.5 单宿主（88.5 的时间带是 1994-1997，\n"
    "与「FreeBSD 2.x 站稳脚跟」吻合）。",
    "全部归宿主 88.5 单宿主。本批主窗跨年度（1997-12=877 / 1998-01=1120，"
    "1998 段占 56%），不按年切宿主，\n依据是实测宿主内容带：88.5 内已有 977 个 "
    "1998-2000 年的 freebsd-hackers 块（pk 2525047~2596485，全在本批 pk 2598421 "
    "之前）——\nH3 线既有实践是把 freebsd-hackers 全时段内容一律落 88.5。")

# BLIND 段
t = t.replace("## 五、可见性盲区（BLIND 率 16.6%）",
              "## 五、可见性盲区（BLIND 率 %.1f%%）" % rate)
t = t.replace("digest 完整正文（折叠 <= 420 字）= 366 行；",
              "digest 完整正文（折叠 <= 420 字）= %d 行；" % nfull)
t = t.replace("digest 截断 = 1632 行（81.6%）；",
              "digest 截断 = %d 行（%.1f%%）；" % (ntrunc, trunc_rate))
t = t.replace("其中自有文字仍在窗口内 = 1300 行；",
              "其中自有文字仍在窗口内 = %d 行；" % nown)
t = t.replace("**BLIND（自有文字落在窗口之外）= 332 行（16.6%）**；",
              "**BLIND（自有文字落在窗口之外）= %d 行（%.1f%%）**；"
              % (blind_total, rate))
t = t.replace("正文全空 = 2 行 [2597172、2598073]。",
              "正文全空 = %d 行 %s。" % (nempty, empty_pks))
t = t.replace("**BLIND 行是本批最高危形态**（332 行、16.6%）",
              "**BLIND 行是本批最高危形态**（%d 行、%.1f%%）" % (blind_total, rate))

# BLIND 按片分布块
old_bs = t.index("p01:6 p02:14")
old_be = t.index("\n\n## 六", old_bs)
t = t[:old_bs] + "\n".join(bdlines) + t[old_be:]

out = os.path.join(HERE, "_READ_TASK_%s.md" % TAG)
with io.open(out, "w", encoding="utf-8", newline="\n") as fh:
    fh.write(t)
    fh.flush()
    os.fsync(fh.fileno())
rb = io.open(out, "rb").read()
print("[写盘] %s %d B" % (out, len(rb)))
print("残留 fhk_b070 :", rb.count(b"fhk_b070"), "| CR:", rb.count(b"\r"),
      "| BOM:", rb.startswith(b"\xef\xbb\xbf"))
print("片表首行:", tbl[0])
print("BLIND 合计 %d" % blind_total)
