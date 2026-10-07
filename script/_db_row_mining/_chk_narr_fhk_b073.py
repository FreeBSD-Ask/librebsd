# -*- coding: utf-8 -*-
"""fhk_b073 叙述分件看护自检器（主会话用，只读磁盘）。

用法: python _chk_narr_fhk_b073.py [k ...]   缺省检查 1..50

按磁盘地面真值逐项判定，不采信任何代理回报。输出：
  已落盘 / 缺失 计数、每片行数与期望行数、长度 min/max/avg、
  格式违规明细（BOM/CR/字段/宿主/长度/禁字符/引号/尾标点/数字开头/
  日期前缀/来源尾串/片内非升序）。

期望行数从 fhk_b073_narrpkg_p<k>.txt 实测派生（非硬编码），
因为 _gen_narrpkg 的 divmod 分配可能随候选数变化。
"""
import io
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(HERE, "review_logs")
TAG = "fhk_b073"
LO, HI = 60, 140
HOST = "885"

FORBID = set("「」『』*|\\")
QUOTES = set(chr(c) for c in [0x2018, 0x2019, 0x201C, 0x201D, 0x0027, 0x0022, 0x0060])
TRAIL = set("。，、；：？！…—．·~-.,;:?! ")
DATE_RE = re.compile(r"^\d{4}\s*年")   # 行首日期前缀；句中历史年份属合法事实指涉
TAIL_MARK = ["ROW_MINE", "来源：", "消息列表", "freebsd-hackers.messages"]

ks = [int(a) for a in sys.argv[1:]] or list(range(1, 51))
landed, missing = [], []
bad = {}
tot_rows = 0
tot_len = []

for k in ks:
    p = os.path.join(LOG, "%s_mount_narr_p%d.tsv" % (TAG, k))
    np_ = os.path.join(LOG, "%s_narrpkg_p%d.txt" % (TAG, k))
    exp = 0
    if os.path.exists(np_):
        exp = sum(1 for l in io.open(np_, encoding="utf-8") if l.strip())
    if not os.path.exists(p):
        missing.append(k)
        continue
    landed.append(k)
    raw = io.open(p, "rb").read()
    probs = []
    if raw[:3] == b"\xef\xbb\xbf":
        probs.append("BOM")
    if b"\r" in raw:
        probs.append("CR")
    if not raw.endswith(b"\n"):
        probs.append("缺末行LF")
    try:
        txt = raw.decode("utf-8")
    except UnicodeDecodeError:
        probs.append("非UTF8")
        bad[k] = probs
        continue
    n = 0
    prev = 0
    for ln in txt.split("\n"):
        if not ln.strip():
            continue
        n += 1
        f = ln.split("\t")
        if len(f) != 3:
            probs.append("字段%d@行%d" % (len(f), n))
            continue
        pk, hk, nar = f
        if not pk.isdigit():
            probs.append("pk非数字@行%d" % n)
            continue
        if int(pk) <= prev:
            probs.append("片内非升序@%s(前%s)" % (pk, prev))
        prev = int(pk)
        if hk != HOST:
            probs.append("宿主%s@%s" % (hk, pk))
        L = len(nar)
        if not (LO <= L <= HI):
            probs.append("长度%d@%s" % (L, pk))
        tot_len.append(L)
        hit = "".join(c for c in nar if c in FORBID)
        if hit:
            probs.append("禁字符%r@%s" % (hit, pk))
        probe = re.sub(r"[A-Za-z]+'[A-Za-z]+", "", nar)
        q = "".join(c for c in probe if c in QUOTES)
        if q:
            probs.append("引号%r@%s" % (q, pk))
        if "\t" in nar or "\n" in nar or "\u3000" in nar:
            probs.append("制表/换行/全角空格@%s" % pk)
        if nar[-1] in TRAIL:
            probs.append("尾标点%r@%s" % (nar[-1], pk))
        if nar[0].isdigit():
            probs.append("数字开头@%s" % pk)
        if DATE_RE.search(nar):
            probs.append("日期前缀@%s" % pk)
        for m in TAIL_MARK:
            if m in nar:
                probs.append("来源尾串%r@%s" % (m, pk))
                break
    if n != exp:
        probs.append("行数%d != 分件期望%d" % (n, exp))
    tot_rows += n
    if probs:
        bad[k] = probs

print("=" * 68)
print("fhk_b073 叙述分件自检  检查 %d 片" % len(ks))
print("  已落盘 %d / 缺失 %d%s" % (len(landed), len(missing),
                                   (" " + str(missing)) if missing else ""))
print("  累计行 %d | 长度 %d-%d 均值 %.1f"
      % (tot_rows, (min(tot_len) if tot_len else 0),
         (max(tot_len) if tot_len else 0),
         (round(sum(tot_len) * 1.0 / len(tot_len), 1) if tot_len else 0)))
if bad:
    print("  违规分件 %d 片：" % len(bad))
    for k in sorted(bad):
        print("    p%-3d %s" % (k, " | ".join(bad[k][:8])))
else:
    print("  格式违规 0")
print("=" * 68)
sys.exit(0 if not missing and not bad else 2)
