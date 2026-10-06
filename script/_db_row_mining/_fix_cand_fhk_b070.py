# -*- coding: utf-8 -*-
"""fhk_b070 候选外科删除：2 条 BLIND 泄漏（主体错配）。

取证结论（逐字比对 digest，见 _gate_cand_b070.py 的 B 类违规）：
  2596910  FROM Dmitry Kohmanyuk
           420 字窗口整段是 `> ` 引用块（引 usr06.primenet.com 关于 Sun 与
           PCI 的那段），发帖人自有文字一个字符都不可见。候选却写成
           「Kohmanyuk：Sun 未提供 PCI 源码…推动者是 Motorola/PowerComputing/Apple」
           ——把被引者主张署给 FROM，属最高频缺陷。删而非改。
  2597221  FROM Mike Smith
           420 字窗口是 Richard Costine 的引用块，自有文字仅结尾裸署名
           「mike」。候选却写成「Mike Smith：认为这基本等同 PowerMac 上的
           VirtualPC…」——同样是把被引者主张署给 FROM。删而非改。
两条的技术串在本行 subject/FROM/body 三处自有文字中 0 命中，不可订正，只能删。
"""
import io
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(HERE, "review_logs")
TAG = "fhk_b070"
DROP = (2596910, 2597221)
NL = chr(10)


def clean(path):
    rows = [l.rstrip(NL) for l in io.open(path, encoding="utf-8") if l.strip()]
    kept, cut = [], []
    for r in rows:
        pk = int(r.split("|", 1)[0])
        if pk in DROP:
            cut.append(r)
        else:
            kept.append(r)
    if not cut:
        return 0
    with io.open(path, "w", encoding="utf-8", newline=NL) as fh:
        fh.write(NL.join(kept) + NL)
    raw = io.open(path, "rb").read()
    assert raw[:3] != b"\xef\xbb\xbf" and b"\r" not in raw and raw.endswith(b"\n")
    for c in cut:
        print("  %s 删 pk %d | %s | %s"
              % (os.path.basename(path), int(c.split("|", 1)[0]),
                 c.split("|", 1)[1], c.split("|", 2)[2]))
    return len(cut)


print("=== 合并产物 ===")
n = clean(os.path.join(LOG, TAG + "_candidates.txt"))
print("=== 源分片 ===")
hit = 0
for k in range(1, 41):
    p = os.path.join(LOG, "%s_candidates_p%d.txt" % (TAG, k))
    if os.path.exists(p):
        hit += clean(p)
print("=== 合计删除 %d 条（期望 4：合并产物 2 ＋ 分片 2）===" % (n + hit))
assert n + hit == 4, "删除数不符 %d" % (n + hit)
left = [l for l in io.open(os.path.join(LOG, TAG + "_candidates.txt"),
                           encoding="utf-8") if l.strip()]
assert all(int(l.split("|", 1)[0]) not in DROP for l in left)
print("末行复核：合并产物 %d 条，DROP 全部消失" % len(left))
