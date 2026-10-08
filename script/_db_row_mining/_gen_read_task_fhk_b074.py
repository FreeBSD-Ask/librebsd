# -*- coding: utf-8 -*-
"""生成 _READ_TASK_fhk_b074.md：以 _READ_TASK_fhk_b072.md 为模板，正则自同步。

与 b072 版的差别（本批修正）：旧版用**手写锚点串**逐处 t.replace，锚点取自上一批
任务书的当前文字，模板每升一批就必须手工重抄一遍旧串，漏抄就 assert 失败或静默
残留（b072 曾因此把 17.6%/325/1673/1322 等一串 b071 时代的值留在替换表里）。
本版改成**正则形状匹配 + 恰好一次**：只锚定版式形状（`库内序 **\\d+-\\d+**`、
`digest 截断 = \\d+ 行（[\\d.]+%）；`…），不锚定具体数字，故跨批零同步成本。

片表与 BLIND 按片分布仍按磁盘实测读取（40 片 digest 与 _blind 文件），不手填。
宿主内容带由 88.5 现场扫描实测，不抄账面。
所有批次实测常量取自 _batch_fhk_b074.json 与 review_logs/_blind_fhk_b074.txt。
"""
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
RL = os.path.join(HERE, "review_logs")
TAG = "fhk_b074"
PREV = "_READ_TASK_fhk_b072.md"
HOST = (r"D:\librebsd\05-卷册大纲\第05卷-freebsd的工程化奠基"
        r"\第88章-freebsd2x站稳脚跟"
        r"\88.5-freebsd2x的开发者群体与core-team代际更替.md")
spec = json.load(io.open(os.path.join(HERE, "_batch_%s.json" % TAG),
                         encoding="utf-8"))
N = spec["n"]
PK_LO, PK_HI = spec["pk_lo"], spec["pk_hi"]
ORD_LO, ORD_HI = spec["offset"] + 1, spec["offset"] + spec["n"]
PKN = PK_HI - PK_LO + 1

# ---- 片表（从磁盘实测）----
rows = []
for k in range(1, spec["parts"] + 1):
    p = os.path.join(RL, "%s_digest_part%d.txt" % (TAG, k))
    assert os.path.exists(p), "缺片 part%d" % k
    L = [l for l in io.open(p, encoding="utf-8").read().split("\n") if l.strip()]
    pks = [int(l.split("|", 1)[0]) for l in L]
    assert pks == sorted(pks), "part%d pk 非升序" % k
    rows.append((k, len(L), pks[0], pks[-1], os.path.getsize(p)))
assert sum(r[1] for r in rows) == N, "片表合计 %d != %d" % (
    sum(r[1] for r in rows), N)
tbl = []
line = []
for k, n, lo, hi, b in rows:
    line.append("p%02d %d %d-%d" % (k, n, lo, hi))
    if len(line) == 4:
        tbl.append(" ".join(line))
        line = []
if line:
    tbl.append(" ".join(line))
HEAD_TAIL = "\n\n**下列纪律不变**"
assert HEAD_TAIL in io.open(os.path.join(HERE, PREV), encoding="utf-8").read()

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
    m = re.match(r"^p(\d+)\s+([\d/]+)\s*$", s)
    if not m:
        continue
    bd[int(m.group(1))] = len([x for x in m.group(2).split("/") if x])
assert BS is not None, "BLIND 汇总行未命中（_blind 输出格式疑已变）"
NFS, NTS, NWS, BSS, NES = BS
assert sum(bd.values()) == BSS, "BLIND 按片 %d != 汇总 %d" % (sum(bd.values()), BSS)
bdlines = []
buf = []
for k in range(1, spec["parts"] + 1):
    buf.append("p%02d:%d" % (k, bd.get(k, 0)))
    if len(buf) == 10:
        bdlines.append(" ".join(buf))
        buf = []
if buf:
    bdlines.append(" ".join(buf))

# ---- 批次实测常量 ----
nos = ", ".join(str(x) for x in spec["empty_subject_pks"])
miss = "／".join(str(x) for x in spec["missing_pks"])
mds = " / ".join("%s=%d" % kv for kv in sorted(spec["month_dist"].items()))
NFULL, NTRUNC, NOWN = NFS, NTS, NWS
assert spec["empty_body"] == NES, \
    "probe 空正文 %d != BLIND %d" % (spec["empty_body"], NES)
NEMPTY = NES
rate = 100.0 * BSS / N
trunc_rate = 100.0 * NTRUNC / N
assert NFULL + NTRUNC + NEMPTY == N
assert NOWN + BSS == NTRUNC
# 主窗只取主月（月内 >= 5 封）：本批另有 3 个脏月份各 1 封
# （1994-05/1997-01/2000-01），是日期头解析错乱、非内容跨年；
# 把它们算进「同年内跨 N 月」会造成误述。
MON = sorted((k, v) for k, v in spec["month_dist"].items() if v >= 5)
DIRTY = sorted((k, v) for k, v in spec["month_dist"].items() if v < 5)
assert len(MON) + len(DIRTY) == len(spec["month_dist"])
MAJ = max(MON, key=lambda kv: kv[1])
maj_pct = 100.0 * MAJ[1] / N
# 主窗两端日期：month_dist 只到月粒度，日粒度由 _probe 实测给出（本批 1998-04-11~1998-06-02）
WIN_LO, WIN_HI = "1998-04-11", "1998-06-02"
NMON = len(MON)
MONS = " / ".join("%s=%d" % kv for kv in MON)
DIRTYK = "、".join("%s 各 %d" % kv for kv in DIRTY) if DIRTY else "无"

# ---- 宿主内容带（现场实测，不抄账面）----
H = io.open(HOST, encoding="utf-8").read()
hpks = [int(m) for m in re.findall(r"ROW_MINE: freebsd-hackers\.messages\.(\d+)", H)]
assert hpks and max(hpks) < PK_LO, \
    "宿主已有 fhk 块 max pk %s 不小于本批 pk_lo %d" % (max(hpks), PK_LO)
HOST_N, HOST_LO, HOST_HI = len(hpks), min(hpks), max(hpks)
ROW_TOTAL = H.count("ROW_MINE:")
print("[宿主实测] 88.5 ROW_MINE 合计 %d，其中 fhk %d（pk %d~%d，全 < %d）"
      % (ROW_TOTAL, HOST_N, HOST_LO, HOST_HI, PK_LO))


def sub1(pat, repl, t, label):
    """正则形状替换：恰好命中一处，否则报锚点漂移。恒开 MULTILINE（形状锚 ^$）。"""
    n = len(re.findall(pat, t, re.M))
    assert n == 1, "%s 命中 %d 处（锚点形状疑已变）：%s" % (label, n, pat)
    return re.sub(pat, repl, t, flags=re.M)


t = io.open(os.path.join(HERE, PREV), encoding="utf-8").read()
t0 = t
t = t.replace("fhk_b072", TAG)

# --- 抬头与批次结构 ---
t = sub1(r"库内序 \*\*\d+-\d+\*\*", "库内序 **%d-%d**" % (ORD_LO, ORD_HI), t,
         "抬头库内序")
t = sub1(r"pk \*\*\d+-\d+\*\*", "pk **%d-%d**" % (PK_LO, PK_HI), t, "抬头 pk")
t = sub1(r"^pk \d+-\d+。$", "pk %d-%d。" % (PK_LO, PK_HI), t, "§〇 pk 行")
t = sub1(r"^非尾片行数 \d+-\d+、字节 \d+-\d+；尾片 p\d+ \d+ 行 \d+ B。$",
         "非尾片行数 %d-%d、字节 %d-%d；尾片 p%02d %d 行 %d B。"
         % (min(r[1] for r in rows[:-1]), max(r[1] for r in rows[:-1]),
            min(r[4] for r in rows[:-1]), max(r[4] for r in rows[:-1]),
            rows[-1][0], rows[-1][1], rows[-1][4]), t, "§〇 行数字节行")

# --- 替换片表块 ---
old_tbl_start = t.index("p01 ", t.index("本批已按 40 路切分"))
old_tbl_end = t.index(HEAD_TAIL, old_tbl_start)
t = t[:old_tbl_start] + "\n".join(tbl) + t[old_tbl_end:]

# --- §四 本批结构 ---
t = sub1(r"库内序 \d+-\d+，pk \d+-\d+，全窗 \d+ 封",
         "库内序 %d-%d，pk %d-%d，全窗 %d 封" % (ORD_LO, ORD_HI, PK_LO, PK_HI, N),
         t, "§四 首行")
t = sub1(r"（区间共 \d+ 个编号、\*\*缺 \d+ 个编号：[^*]+\*\*，",
         "（区间共 %d 个编号、**缺 %d 个编号：%s**，"
         % (PKN, len(spec["missing_pks"]), miss), t, "§四 区间跳号")

_dirty_tail = ("，另有脏日期 %d 封（%s，日期头解析错乱、非内容跨年）"
               % (len(DIRTY), DIRTYK)) if DIRTY else ""
_new_mon = ("月份 %s 为主窗（同年内跨 %d 月，%s 占 %.1f%%）%s；"
            "日期 min=%s / max=%s，"
            % (MONS, NMON, MAJ[0], maj_pct, _dirty_tail, WIN_LO, WIN_HI))
t = sub1(r"^月份 .+$", _new_mon, t, "§四 月份行")

_new_host1 = ("全部归宿主 88.5 单宿主。本批主窗同年内跨 %d 月"
              "（%s，%s 占 %.1f%%），不按年切宿主，"
              % (NMON, MONS, MAJ[0], maj_pct))
t = sub1(r"^全部归宿主 88\.5 单宿主。本批主窗.*$", _new_host1, t, "§四 宿主主窗")
_new_host2 = ("依据是实测宿主内容带：88.5 内已有 %d 个 freebsd-hackers 块"
              "（pk %d~%d，全在本批 pk %d 之前）——"
              % (HOST_N, HOST_LO, HOST_HI, PK_LO))
t = sub1(r"^依据是实测宿主内容带：.*$", _new_host2, t, "§四 宿主内容带")

t = sub1(r"空正文 \d+ 行；空 subject \d+ 行 \[[^\]]*\]",
         "空正文 %d 行；空 subject %d 行 [%s]"
         % (NEMPTY, spec["empty_subject"], nos), t, "§四 空正文")

# --- §五 BLIND ---
t = sub1(r"## 五、可见性盲区（BLIND 率 [\d.]+%）",
         "## 五、可见性盲区（BLIND 率 %.1f%%）" % rate, t, "§五 标题")
t = sub1(r"digest 完整正文（折叠 <= 420 字）= \d+ 行；",
         "digest 完整正文（折叠 <= 420 字）= %d 行；" % NFULL, t, "§五 完整")
t = sub1(r"digest 截断 = \d+ 行（[\d.]+%）；",
         "digest 截断 = %d 行（%.1f%%）；" % (NTRUNC, trunc_rate), t, "§五 截断")
t = sub1(r"其中自有文字仍在窗口内 = \d+ 行；",
         "其中自有文字仍在窗口内 = %d 行；" % NOWN, t, "§五 窗内")
t = sub1(r"\*\*BLIND（自有文字落在窗口之外）= \d+ 行（[\d.]+%）\*\*；",
         "**BLIND（自有文字落在窗口之外）= %d 行（%.1f%%）**；"
         % (BSS, rate), t, "§五 BLIND 行")
_empty_line = ("正文全空 = 0 行。" if NEMPTY == 0
               else "正文全空 = %d 行 %s。" % (NEMPTY, "／".join(
                   str(x) for x in spec.get("empty_body_pks", []))))
t = sub1(r"^正文全空 = .+$", _empty_line, t, "§五 正文全空")
t = sub1(r"\*\*BLIND 行是本批最高危形态\*\*（\d+ 行、[\d.]+%）",
         "**BLIND 行是本批最高危形态**（%d 行、%.1f%%）" % (BSS, rate),
         t, "§五 高危句")

# --- §五 BLIND 按片分布块 ---
old_bs = t.index("p01:")
old_be = t.index("\n\n## 六", old_bs)
t = t[:old_bs] + "\n".join(bdlines) + t[old_be:]

out = os.path.join(HERE, "_READ_TASK_%s.md" % TAG)
with io.open(out, "w", encoding="utf-8", newline="\n") as fh:
    fh.write(t)
    fh.flush()
    os.fsync(fh.fileno())
rb = io.open(out, "rb").read()

# --- 残留旧值自检：上一批的全部关键数字与上一批标签必须清零 ---
# 注：2604443 是 88.5 实测宿主带 max pk（本批之前最后一块），合法保留，
#     故不在残留清单内（与 b073 版注 2602440 同理）。
# 只放**不可能与本批 pk 片段碰撞**的字面（本批 pk 2604444-2606444，
# 故 3 位短数字如 b"362"／b"252" 会命中 2604362／2606252 之类真 pk，禁入清单）。
stale = [b"fhk_b073", b"144001", b"146000", b"2602441",
         b"1998-02=108", b"1998-03=1304", b"1998-04=588",
         b"21.2%", b"1748", b"1823", b"1398", b"425"]
for s in stale:
    assert rb.count(s) == 0, "残留旧值 %r x%d" % (s, rb.count(s))
assert b"\r" not in rb and not rb.startswith(b"\xef\xbb\xbf")
assert t != t0, "替换前后无变化（模板疑已失效）"
print("[写盘] %s %d B" % (out, len(rb)))
print("片表首行:", tbl[0])
print("BLIND 合计 %d（%.1f%%）| 完整 %d | 截断 %d（%.1f%%）| 窗内 %d | 全空 %d"
      % (BSS, rate, NFULL, NTRUNC, trunc_rate, NOWN, NEMPTY))
print("跳号 %d 个 | 空 subject %d | 主窗 %s~%s | 月份 %s"
      % (len(spec["missing_pks"]), spec["empty_subject"], WIN_LO, WIN_HI, MONS))
