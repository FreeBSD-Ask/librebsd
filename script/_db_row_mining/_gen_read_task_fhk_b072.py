# -*- coding: utf-8 -*-
"""生成 _READ_TASK_fhk_b072.md：以 b071 任务书为模板，逐处替换批次专属数值。

片表与 BLIND 按片分布一律从磁盘实测读取，不手填。
锚点字符串取自 _READ_TASK_fhk_b071.md 的**当前**内容（b071 终态），
不是 b070 时代的旧串——模板每升一批就要同步本表的锚点。

b072 数值全部来自 _batch_fhk_b072.json（probe 实测）与 review_logs/_blind_fhk_b072.txt
（BLIND 实测），宿主内容带 pk 带由 88.5 现场扫描实测。
"""
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
RL = os.path.join(HERE, "review_logs")
TAG = "fhk_b072"
PREV = "_READ_TASK_fhk_b071.md"
HOST = (r"D:\librebsd\05-卷册大纲\第05卷-freebsd的工程化奠基"
        r"\第88章-freebsd2x站稳脚跟"
        r"\88.5-freebsd2x的开发者群体与core-team代际更替.md")
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
BS = None
for ln in io.open(os.path.join(RL, "_blind_%s.txt" % TAG), encoding="utf-8"):
    s = ln.strip()
    m0 = re.match(r"^digest 完整正文 (\d+) \| 截断 (\d+)（自有文字在窗内 (\d+) / "
                  r"BLIND (\d+)）\| 全空 (\d+)$", s)
    if m0:
        BS = [int(x) for x in m0.groups()]
        continue
    m = re.match(r"^p(\d+)\s+(.*)$", s)
    if not m:
        continue
    pks = [x for x in m.group(2).split("/") if x]
    bd[int(m.group(1))] = len(pks)
assert BS is not None, "BLIND 汇总行未命中正则"
NFS, NTS, NWS, BSS, NES = BS
blind_total = sum(v for v in bd.values())
assert blind_total == BSS, "BLIND 按片合计 %d != 汇总 %d" % (blind_total, BSS)
bdlines = []
buf = []
for k in range(1, 41):
    buf.append("p%02d:%d" % (k, bd.get(k, 0)))
    if len(buf) == 10:
        bdlines.append(" ".join(buf))
        buf = []
if buf:
    bdlines.append(" ".join(buf))

# ---- 批次实测常量（b072）----
PKN = spec["pk_hi"] - spec["pk_lo"] + 1
nos = ", ".join(str(x) for x in spec["empty_subject_pks"])
miss = "／".join(str(x) for x in spec["missing_pks"])
mds = " / ".join("%s=%d" % kv for kv in sorted(spec["month_dist"].items()))
NFULL, NTRUNC, NOWN = NFS, NTS, NWS
assert spec["empty_body"] == NES, "probe 空正文 %d != BLIND %d" % (spec["empty_body"], NES)
NEMPTY = NES
EMPTY_PKS = "[]"
rate = 100.0 * blind_total / 2000
trunc_rate = 100.0 * NTRUNC / 2000
assert NFULL + NTRUNC + NEMPTY == 2000
assert NOWN + blind_total == NTRUNC

# 宿主内容带（现场实测，不抄账面）
H = io.open(HOST, encoding="utf-8").read()
hpks = [int(m) for m in re.findall(r"ROW_MINE: freebsd-hackers\.messages\.(\d+)", H)]
assert hpks and max(hpks) < spec["pk_lo"], \
    "宿主已有 fhk 块 max pk %s 不小于本批 pk_lo" % max(hpks)
HOST_N, HOST_LO, HOST_HI = len(hpks), min(hpks), max(hpks)
ROW_TOTAL = H.count("ROW_MINE:")
print("[宿主实测] 88.5 ROW_MINE 合计 %d，其中 fhk %d（pk %d~%d，全 < %d）"
      % (ROW_TOTAL, HOST_N, HOST_LO, HOST_HI, spec["pk_lo"]))

t = io.open(os.path.join(HERE, PREV), encoding="utf-8").read()
t = t.replace("fhk_b071", TAG)
# --- 抬头与批次结构 ---
t = t.replace("库内序 **140001-142000**", "库内序 **142001-144000**")
t = t.replace("pk **2598421-2600431**", "pk **2600432-2602440**")
t = t.replace("库内序 140001-142000，pk 2598421-2600431",
              "库内序 142001-144000，pk 2600432-2602440")
t = t.replace("pk 2598421-2600431。", "pk 2600432-2602440。")

# --- 替换旧片表块 ---
old_tbl_start = t.index("p01 ", t.index("本批已按 40 路切分"))
old_tbl_end = t.index("\n\n**下列纪律不变**", old_tbl_start)
t = t[:old_tbl_start] + "\n".join(tbl) + t[old_tbl_end:]

# --- 替换字节范围描述 ---
t = re.sub(r"非尾片行数 \d+-\d+、字节 \d+-\d+；尾片 p40 \d+ 行 \d+ B",
           "非尾片行数 %d-%d、字节 %d-%d；尾片 p40 %d 行 %d B"
           % (min(r[1] for r in rows[:39]), max(r[1] for r in rows[:39]),
              min(r[4] for r in rows[:39]), max(r[4] for r in rows[:39]),
              rows[39][1], rows[39][4]), t)

# --- 区间 / 跳号 ---
t = t.replace(
    "（区间共 2011 个编号、**缺 11 个编号：2599401／2599717／2599883／2599929／"
    "2599934／2599935／2600069／2600075／2600077／2600246／2600283**，",
    "（区间共 %d 个编号、**缺 %d 个编号：%s**，"
    % (PKN, len(spec["missing_pks"]), miss))

# --- 月份分布 / 错序 ---
A_MON = ("月份 1997-10=1 / 1997-12=877 / 1998-01=1120 / 2036-02=2 为主窗"
         "（1997-12=877 / 1998-01=1120，跨年度），另有 3 封错序"
         "（1997-10-22×1 / 1997-12-04×1 / 2036-02-07×2，2036 系源库脏日期），"
         "日期 min=1997-10-22 / max=2036-02-07，")
R_MON = ("月份 %s 为主窗（1998-01=609 / 1998-02=1389，同年内跨月，"
         "1998-02 占 69.5%%），另有 2 封错序（1997-01-28×2，"
         "均为 merson@juno.com 的退订与求助，属源库脏日期），"
         "日期 min=1997-01-28 / max=1998-02-27，" % mds)

# --- 宿主时间带说明（本批跨月，按实测宿主内容带改口径）---
A_HOST = ("全部归宿主 88.5 单宿主。本批主窗跨年度（1997-12=877 / 1998-01=1120，"
          "1998 段占 56%），不按年切宿主，\n"
          "依据是实测宿主内容带：88.5 内已有 977 个 1998-2000 年的 "
          "freebsd-hackers 块（pk 2525047~2596485，全在本批 pk 2598421 之前）——\n"
          "H3 线既有实践是把 freebsd-hackers 全时段内容一律落 88.5。")
R_HOST = ("全部归宿主 88.5 单宿主。本批主窗同年内跨月"
          "（1998-01=609 / 1998-02=1389，1998-02 占 69.5%%），不按年切宿主，\n"
          "依据是实测宿主内容带：88.5 内已有 %d 个 freebsd-hackers 块"
          "（pk %d~%d，全在本批 pk %d 之前）——\n"
          "H3 线既有实践是把 freebsd-hackers 全时段内容一律落 88.5。"
          % (HOST_N, HOST_LO, HOST_HI, spec["pk_lo"]))

# --- 空正文 / 空 subject ---
A_EMPTY = ("空正文 0 行；空 subject 12 行 [2598875, 2598876, 2599086, 2599090, "
           "2599093, 2599455, 2599472, 2599597, 2599713, 2600155, 2600156, "
           "2600157]")
R_EMPTY = "空正文 %d 行；空 subject %d 行 [%s]" % (
    NEMPTY, spec["empty_subject"], nos)

# --- BLIND 段 ---
PAIRS = [
    (A_MON, R_MON),
    (A_HOST, R_HOST),
    (A_EMPTY, R_EMPTY),
    ("## 五、可见性盲区（BLIND 率 17.6%）",
     "## 五、可见性盲区（BLIND 率 %.1f%%）" % rate),
    ("digest 完整正文（折叠 <= 420 字）= 325 行；",
     "digest 完整正文（折叠 <= 420 字）= %d 行；" % NFULL),
    ("digest 截断 = 1673 行（83.7%）；",
     "digest 截断 = %d 行（%.1f%%）；" % (NTRUNC, trunc_rate)),
    ("其中自有文字仍在窗口内 = 1322 行；",
     "其中自有文字仍在窗口内 = %d 行；" % NOWN),
    ("**BLIND（自有文字落在窗口之外）= 351 行（17.6%）**；",
     "**BLIND（自有文字落在窗口之外）= %d 行（%.1f%%）**；"
     % (blind_total, rate)),
    ("正文全空 = 2 行 [2598732、2599641]。",
     ("正文全空 = 0 行。" if NEMPTY == 0
      else "正文全空 = %d 行 %s。" % (NEMPTY, EMPTY_PKS))),
    ("**BLIND 行是本批最高危形态**（351 行、17.6%）",
     "**BLIND 行是本批最高危形态**（%d 行、%.1f%%）" % (blind_total, rate)),
]
for a, b in PAIRS:
    assert a in t, "锚点未命中（模板已变）：%r" % a[:60]
    assert t.count(a) == 1, "锚点非唯一 %d 处：%r" % (t.count(a), a[:60])
    t = t.replace(a, b)

# --- BLIND 按片分布块 ---
old_bs = t.index("p01:11 p02:12")
old_be = t.index("\n\n## 六", old_bs)
t = t[:old_bs] + "\n".join(bdlines) + t[old_be:]

out = os.path.join(HERE, "_READ_TASK_%s.md" % TAG)
with io.open(out, "w", encoding="utf-8", newline="\n") as fh:
    fh.write(t)
    fh.flush()
    os.fsync(fh.fileno())
rb = io.open(out, "rb").read()
# 注：2600431 是 88.5 实测宿主带 max pk（合法保留），不在残留清单内。
for stale in (b"fhk_b071", b"140001", b"142000", b"2598421",
              b"17.6%", b"1673", b"1322",
              b"= 325 \xe8\xa1\x8c", b"p01:11", b"2036"):
    assert rb.count(stale) == 0, "残留旧值 %r x%d" % (stale, rb.count(stale))
assert b"\r" not in rb and not rb.startswith(b"\xef\xbb\xbf")
print("[写盘] %s %d B" % (out, len(rb)))
print("片表首行:", tbl[0])
print("BLIND 合计 %d（%.1f%%）| 完整 %d | 截断 %d（%.1f%%）| 窗内 %d"
      % (blind_total, rate, NFULL, NTRUNC, trunc_rate, NOWN))
