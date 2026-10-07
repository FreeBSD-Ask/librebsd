# -*- coding: utf-8 -*-
"""BLIND 清单：digest 420 字窗口内看不到发帖人自有文字的行。

口径（与 _digest_fhk_b071.py 的正文压缩列**逐字一致**，b044 起标定、b053/b070 沿用）：
  digest 正文列 = ' '.join(body.split()) 的前 420 字，一律硬截断，无全文内联。
  故四态为：
    full      = 折叠后 <= 420，digest 即完整正文
    own-vis   = 折叠后 > 420（截断），但首段自有文字落在窗口内
    BLIND     = 折叠后 > 420（截断），且首段自有文字落在窗口之外
                -> 读者看到的 420 字整段是信头与引用块，无一句是发帖人自己的话
                -> 读手必须回到全文重判，不得据 420 字窗口写候选
  注：折叠后再做 '|'->'/' 替换不改变长度，故本清单与 digest 的截断点一致。
零正则、零反斜杠。
"""
import io
import json
import os
import sys

import duckdb

NL = chr(10)
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)

spec = json.load(io.open(os.path.join(HERE, "_batch_fhk_b071.json"), encoding="utf-8"))
TAG = spec["tag"]
DB = spec["src_db"]
LO, HI, PER, NPART = spec["pk_lo"], spec["pk_hi"], 50, spec["parts"]
TRIM = 420


def is_own(ln):
    """该行是否为发帖人自有文字（非引用、非信头、非署名）。"""
    t = ln.strip()
    if not t:
        return False
    if t.startswith(">"):
        return False
    if t.startswith("On ") and "wrote:" in t:
        return False
    if t.endswith("wrote:") or ("wrote:" in t and len(t) < 60):
        return False
    if t.startswith("-- ") or t.startswith("P.S."):
        return False
    # 前 32 字符内、冒号前无空格、冒号后接空格 -> 邮件头行
    hdr = False
    for i, ch in enumerate(t):
        if ch == ":" and 1 <= i <= 32:
            if " " not in t[:i] and i + 1 < len(t) and t[i + 1] == " ":
                hdr = True
            break
    return not hdr


def flat(b):
    return " ".join((b or "").split())


c = duckdb.connect(DB, read_only=True)
rows = c.execute(
    "SELECT CAST(id AS BIGINT), body FROM messages "
    "WHERE CAST(id AS BIGINT) BETWEEN ? AND ? "
    "ORDER BY CAST(id AS BIGINT)", [LO, HI]).fetchall()
c.close()
print("取到 %d 封" % len(rows))

full, ownvis, blind, empty = [], [], [], []
for pk, b in rows:
    if not (b or "").strip():
        empty.append(pk)
        continue
    f = flat(b)
    if len(f) <= TRIM:
        full.append(pk)
        continue
    # 截断行：定位首段自有文字的落点
    cut = True
    off = 0
    for ln in (b or "").split(NL):
        seg = " ".join(ln.split())
        if is_own(ln) and off < TRIM:
            cut = False
            break
        if is_own(ln):
            break
        off += (len(seg) if not seg else len(seg) + 1)
    (blind if cut else ownvis).append(pk)

print("digest 完整正文（折叠 <= %d 字）      = %d 行" % (TRIM, len(full)))
print("digest 截断（折叠 > %d 字）          = %d 行" % (TRIM, len(ownvis) + len(blind)))
print("  其中自有文字仍在窗口内             = %d 行" % len(ownvis))
print("  BLIND（自有文字落在窗口之外）      = %d 行（%.1f%%）"
      % (len(blind), 100.0 * len(blind) / len(rows)))
print("  正文全空                           = %d 行 %s" % (len(empty), empty))
print("合计 %d" % (len(full) + len(ownvis) + len(blind) + len(empty)))

with io.open("review_logs/_blind_%s.txt" % TAG, "w", encoding="utf-8",
             newline="\n") as fh:
    fh.write("digest 完整正文 %d | 截断 %d（自有文字在窗内 %d / BLIND %d）| 全空 %d\n"
             % (len(full), len(ownvis) + len(blind), len(ownvis), len(blind),
                len(empty)))
    edge = [p for p, b in rows if len(" ".join((b or "").split())) == TRIM]
    fh.write("注：「完整正文」判据为折叠后 <= %d 字（含恰好 %d）；digest 生成器把恰好 %d 字\n"
             "    的那 %d 行（pk %s）计入「恰 %d 字」桶，故两边桶计数差 %d 是判据开闭之差，\n"
             "    非数据不一致——两侧合计均为 %d 行。\n\n"
             % (TRIM, TRIM, TRIM, len(edge), edge, TRIM, len(edge), len(rows)))
    fh.write("=== BLIND 明细（按片）===\n")
    # 片归属一律以 digest_part*.txt 实际行序为准，不用 idx // PER 算术 ——
    # 切片器是字节平衡（每片 48-50 行不等），PER 行算术会让片标签整体左移；
    # 也不用 pk 算术推断（pk 在窗口内非连续）。此处直接读落盘分片，是唯一地面真值。
    part_of = {}
    for i in range(1, NPART + 1):
        pth = "review_logs/%s_digest_part%d.txt" % (TAG, i)
        for ln in io.open(pth, encoding="utf-8").read().rstrip(NL).split(NL):
            part_of[int(ln.split("|", 1)[0])] = i
    assert len(part_of) == len(rows), "digest 分片未全覆盖窗口 %d != %d" % (
        len(part_of), len(rows))
    assert part_of == dict(
        (int(l.split("|", 1)[0]), part_of[int(l.split("|", 1)[0])])
        for l in io.open("review_logs/%s_digest.txt" % TAG, encoding="utf-8")
        .read().rstrip(NL).split(NL)), "分片 pk 与 digest 全量不一致"
    for i in range(1, NPART + 1):
        hit = [p for p in blind if part_of[p] == i]
        if hit:
            fh.write("p%02d %s\n" % (i, "/".join(str(x) for x in hit)))
print("落盘 review_logs/_blind_%s.txt（片归属按 digest_part*.txt 实测）" % TAG)
