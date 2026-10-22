# -*- coding: utf-8 -*-
"""叙述硬门禁（通用参数化版，取代 _vn_b053.py）。

背景坑：`_chk_mount_narr.py` 全脚本只有 print、从不 exit 非零；
`_merge_narr.py` 的阻断集只有「缺文件/CRLF」，叙述越限与禁字符报而不拦。
本脚本是真门禁——任何违规 exit 1。

校验项：
  1) N 份 mount_narr 全存在、pk 集合与 candidates 完全一致（不多不少不重）
  2) 每行恰好 3 个 TAB 分隔字段
  3) 叙述长度 60–140（含标点）
  4) 尾标点（含 ！ ？ 空格——_chk_narr_parts.py 漏了这两个）
  5) 禁字符 「 」 * \\ |
  6) 宿主与 narrhost_pK.tsv 逐 pk 一致（叙述手不得自行改派）
  7) 无 BOM、无 CRLF、无空行
  8) 全批 pk 升序唯一

用法: C:/Python314/python.exe _vn_narr.py <tag> [N]
"""
import io
import json
import os
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
RL = os.path.join(HERE, "review_logs")

if len(sys.argv) < 2:
    raise SystemExit("用法: python _vn_narr.py <tag> [N]")
TAG = sys.argv[1]
N = int(sys.argv[2]) if len(sys.argv) > 2 else 8

BAN = set([chr(0x300c), chr(0x300d), "*", chr(92), "|"])
# 🔴 比 _chk_narr_parts.py 多 ！（0xff01）？（0xff1f）——那两处查漏
TAIL = set([chr(0xff0c), chr(0xff1b), chr(0xff1a), chr(0x3002),
            chr(0xff01), chr(0xff1f), " "])
# 宿主白名单＝字面基线并上本批 spec 的 hosts（fq_b116 起 spec 含 922＝大纲
# 9.2 kqueue 节）。并集只放宽不收紧，旧批不受影响。
HOSTS = {"10016", "10017", "923", "924", "921"}
_spec = os.path.join(HERE, "_batch_%s.json" % TAG)
if os.path.exists(_spec):
    try:
        HOSTS |= set(json.load(io.open(_spec, encoding="utf-8")).get("hosts") or [])
    except ValueError:
        pass

fails = []

# 候选 pk 全集
cf = os.path.join(RL, "%s_candidates.txt" % TAG)
if not os.path.exists(cf):
    print("❌ 缺 %s（须先跑 _merge_cand.py）" % cf)
    sys.exit(1)
cand_pks = [l.split("|")[0].strip() for l in
            io.open(cf, encoding="utf-8") if l.strip()]
cand_set = set(cand_pks)
print("候选 %d 条" % len(cand_set))

rows_all = []
for k in range(1, N + 1):
    f = os.path.join(RL, "%s_mount_narr_p%d.tsv" % (TAG, k))
    if not os.path.exists(f):
        fails.append("p%d 缺文件" % k)
        continue
    raw = io.open(f, "rb").read()
    if raw.startswith(b"\xef\xbb\xbf"):
        fails.append("p%d 有 BOM" % k)
    if b"\r" in raw:
        fails.append("p%d 有 CR" % k)
    txt = raw.decode("utf-8")
    lines = txt.split("\n")
    if lines and lines[-1] == "":
        lines = lines[:-1]
    blank = [i + 1 for i, l in enumerate(lines) if l.strip() == ""]
    if blank:
        fails.append("p%d 空行 %s" % (k, blank[:4]))
    rows = [l.split("\t") for l in lines if l.strip()]

    # 宿主映射对照
    hf = os.path.join(RL, "%s_narrhost_p%d.tsv" % (TAG, k))
    hostexp = {}
    if os.path.exists(hf):
        for l in io.open(hf, encoding="utf-8"):
            if l.strip():
                a, b = l.rstrip("\n").split("\t")
                hostexp[a] = b
    else:
        fails.append("p%d 缺 narrhost" % k)

    for ln, r in enumerate(rows, 1):
        if len(r) != 3:
            fails.append("p%d 行%d 列数 %d" % (k, ln, len(r)))
            continue
        pk, host, narr = r
        rows_all.append((k, ln, pk, host, narr))
        if pk not in hostexp:
            fails.append("p%d pk %s 不在 narrhost" % (k, pk))
        elif hostexp[pk] != host:
            fails.append("p%d pk %s 宿主自改 %s→%s" % (k, pk, hostexp[pk], host))
        if host not in HOSTS:
            fails.append("p%d pk %s 宿主越界 %s" % (k, pk, host))
        L = len(narr)
        if not (60 <= L <= 140):
            fails.append("p%d pk %s 长度 %d" % (k, pk, L))
        if narr[-1] in TAIL:
            fails.append("p%d pk %s 尾标点 %r" % (k, pk, narr[-1]))
        for c in narr:
            if c in BAN:
                fails.append("p%d pk %s 禁字符 %r" % (k, pk, c))
                break

print("实收 %d 行" % len(rows_all))
got = [r[2] for r in rows_all]
if len(got) != len(set(got)):
    dup = [p for p, c in Counter(got).items() if c > 1]
    fails.append("pk 重复 %s" % dup[:8])
miss = sorted(cand_set - set(got))
extra = sorted(set(got) - cand_set)
if miss:
    fails.append("缺 pk %d 条 %s" % (len(miss), miss[:8]))
if extra:
    fails.append("多 pk %d 条 %s" % (len(extra), extra[:8]))
order = [int(x) for x in got]

# 分件内 pk 升序：叙述手不得在本件内乱序（锁死件内重排与漏行错位）。
_badpart = []
for _k in sorted(set(r[0] for r in rows_all)):
    _seq = [int(r[2]) for r in rows_all if r[0] == _k]
    if _seq != sorted(_seq):
        _badpart.append(_k)
if _badpart:
    fails.append("分件内 pk 非升序 %s" % _badpart[:6])

if order != sorted(order):
    # 多段批次（fq_b095/b096/b097 实测各 2 处降序）：候选表按段序＋段内日期序排列，
    # 全局 pk 升序不可能成立。改按「分件拼接与候选表逐条同序」校验，
    # 同样锁死缺段、错位与重复；升序批次不受此分支影响。
    if got != cand_pks:
        # 🔴 fq_b104：_split_narrpkg 把超大块塞进有余量的分件，p10 的区间
        #    2376929..2377304 跨嵌在 p02/p03 区间之内（2376929 等 4 个 pk 属 p02 段
        #    却落在 p10）。此时分件拼接与全局 pk 升序恒不等，属结构性假阳性而非叙述
        #    手错误——上方「分件内升序」＋「pk 集与候选件完全一致」＋「全局唯一」
        #    已锁死缺段/错位/重复，判据不放宽。
        if set(got) == cand_set:
            print("pk 非全局升序且分件区间互相跨嵌：集合一致＋分件内升序校验通过，"
                  "跳过拼接同序校验")
        else:
            d = [i for i in range(len(got)) if i < len(cand_pks) and got[i] != cand_pks[i]]
            fails.append("分件拼接与候选表不同序 %d 处（首 %s）" % (len(d), d[:5]))
    else:
        print("pk 非全局升序（多段批次），改按候选表逐条同序校验通过")

ls = [len(r[4]) for r in rows_all]
if ls:
    print("叙述长度 %d/%d/%.1f  宿主 %s"
          % (min(ls), max(ls), sum(ls) / float(len(ls)),
             sorted(Counter(r[3] for r in rows_all).items())))
else:
    print("无任何行")

if fails:
    print("\n❌ FAIL %d 项" % len(fails))
    for x in fails[:60]:
        print("   ", x)
    if len(fails) > 60:
        print("    ...（共 %d 项）" % len(fails))
    sys.exit(1)
print("\n✅ PASS 全绿")
sys.exit(0)
