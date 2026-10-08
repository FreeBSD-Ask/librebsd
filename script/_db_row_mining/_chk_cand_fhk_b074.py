# -*- coding: utf-8 -*-
"""读手自检：给片号 K，打印 review_logs/fhk_b074_candidates_p<K>.txt 的实测统计。

读手落盘后跑本脚本回报真实数字（禁止凭记忆复述）；主会话也用同一份脚本验盘，
避免「子代理自报长度／条数」与门禁口径不一致。

用法: python _chk_cand_fhk_b074.py 1   # 或 1 2 3 ... 40 一次查多片
"""
import io
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
RL = os.path.join(HERE, "review_logs")
TAG = "fhk_b074"
MIN_SUM, MAX_SUM = 20, 80
FORBID = set(u"\u300c\u300d\u300e\u300f\u300a\u300b*|" + u"\u3000\t")
QUOTE = set(u"\u2018\u2019\u201c\u201d\u2032\u2033\u2013\u2014'\u02bc"
            u"`\ufffd\u201e\u201f")
TRAIL = set(u"\u3002\uff0c\uff1a\uff1b\uff1f\uff01\u3001.,:;?!")


def chk(k):
    p = os.path.join(RL, "%s_candidates_p%d.txt" % (TAG, k))
    if not os.path.exists(p):
        print("p%-3d 文件缺失: %s" % (k, p))
        return
    raw = io.open(p, "rb").read()
    ok = os.path.exists(
        os.path.join(RL, "%s_digest_part%d.txt" % (TAG, k)))
    bad_bom = raw[:3] == b"\xef\xbb\xbf"
    bad_cr = b"\r" in raw
    bad_eol = not raw.endswith(b"\n")
    lines = [l for l in raw.decode("utf-8").split("\n") if l.strip()]
    bad = []
    lns = []
    for i, ln in enumerate(lines, 1):
        f = ln.split("|", 2)
        if len(f) != 3:
            bad.append("第%d行 字段%d" % (i, len(f)))
            continue
        pk, lvl, s = f[0].strip(), f[1].strip(), f[2].strip()
        if not pk.isdigit():
            bad.append("第%d行 pk 非数字" % i)
        if lvl not in ("L3", "L4"):
            bad.append("第%d行 等级 %s" % (i, lvl))
        if not (MIN_SUM <= len(s) <= MAX_SUM):
            bad.append("第%d行 %s 摘要 %d 字" % (i, pk, len(s)))
        hit = [c for c in s if c in FORBID or c in QUOTE]
        if hit:
            bad.append("第%d行 %s 禁字符/引号 %s" % (i, pk, "".join(hit)))
        if s[0].isdigit():
            bad.append("第%d行 %s 数字开头" % (i, pk))
        if s[-1] in TRAIL or s[-1].isspace():
            bad.append("第%d行 %s 收尾 %r" % (i, pk, s[-1]))
        lns.append((int(pk), lvl, s))
    # 升序判据必须在排序**之前**取序，否则 self-compare 恒 True（假绿）
    seq = [x[0] for x in lns]
    asc = seq == sorted(seq)
    lns.sort(key=lambda x: x[0])
    dup = len(set(x[0] for x in lns)) != len(lns)
    L = [len(x[2]) for x in lns]
    print("p%-3d 文件 %6d B | 行数 %3d | 摘要 len %d-%d 均 %.1f | L4 %d / L3 %d"
          % (k, len(raw), len(lines),
             min(L) if L else 0, max(L) if L else 0,
             (sum(L) / len(L)) if L else 0.0,
             sum(1 for x in lns if x[1] == "L4"),
             sum(1 for x in lns if x[1] == "L3")))
    print("      输入片存在 %s | BOM %s | CR %s | 缺末行 LF %s | pk 升序 %s | pk 重复 %s"
          % (ok, bad_bom, bad_cr, bad_eol, asc, dup))
    if bad:
        print("      违规 %d 项:" % len(bad))
        for b in bad[:20]:
            print("        ", b)
        if len(bad) > 20:
            print("         …其余 %d 项" % (len(bad) - 20))
    else:
        print("      本片自检全绿")


if __name__ == "__main__":
    args = [int(a) for a in sys.argv[1:]]
    assert args, "用法: python _chk_cand_fhk_b074.py 1 [2 3 ... 40]"
    for k in args:
        chk(k)
