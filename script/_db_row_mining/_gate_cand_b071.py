# -*- coding: utf-8 -*-
"""fhk_b071 候选门禁（独立于 _merge_cand，不复用其判定，只做验收）。

校验六类：
  F 格式      三字段 / pk 数字 / 等级白名单 / pk 升序唯一
  W 窗口      pk 落在库内序窗口 140001-142000 的实测 pk 集合内
  L 长度      摘要 20-80 字
  C 字符      禁字符「」『』*|、全角空格、制表符、换行、任何引号形态
  T 边界      不以标点或空格收尾、不以数字开头
  B 盲区      pk 不得出现在 BLIND 清单 / 空正文清单 / 跳号清单
"""
import io
import os
import re
import sys
import collections

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(HERE, "review_logs")
TAG = "fhk_b071"
MIN_SUM, MAX_SUM = 20, 80

# 跳号 5 个（库内不存在）
JUMPS = set([2597698, 2597700, 2597750, 2598185, 2598208])
# 正文全空 2 封
EMPTY = set([2597172, 2598073])

# 禁字符：直角引号、书名号、星号、竖线、反斜杠、全角空格、制表符
FORBID = set(u"\u300c\u300d\u300e\u300f\u300a\u300b*|" + u"\u3000\t")
# 引号形态：弯引号、单双引号、撇号、反引号、U+FFFD 替换符
QUOTE = set(u"\u2018\u2019\u201c\u201d\u2032\u2033\u2013\u2014'\u02bc"
            u"`\ufffd\u201e\u201f")
# 句末标点（不得收尾）
TRAIL = set(u"\u3002\uff0c\uff1a\uff1b\uff1f\uff01\u3001.,:;?!")

fails = collections.OrderedDict()


def bad(cls, msg):
    fails.setdefault(cls, []).append(msg)


# ---- 读 digest 实际 pk 集合（权威）----
dig = io.open(os.path.join(LOG, "%s_digest.txt" % TAG), encoding="utf-8")
digest_pk = set()
for ln in dig:
    if ln.strip():
        digest_pk.add(int(ln.split("|", 1)[0]))
dig.close()
print("digest 实际 pk 数 %d" % len(digest_pk))
assert len(digest_pk) == 2000

# ---- 读 BLIND 清单 ----
# 只能解析 "p01 2598423/2598424" 这一族明细行。
# 不能对全文扫 \b2\d{6}\b：_blind_*.txt 的说明段里也出现 pk（例如「恰好 420 字」
# 边界行的 pk [2599847, 2599858]），那是「完整正文」桶里的行、不是 BLIND，
# 全文扫会把它们误判成 BLIND（本批因此曾把 351 误读成 353），再让 [B] 误杀
# 两条合法候选。
blind = set()
bf = io.open(os.path.join(LOG, "_blind_%s.txt" % TAG), encoding="utf-8")
for ln in bf:
    s = ln.strip()
    m2 = re.match(r"^p(\d+)\s+([\d/]+)\s*$", s)
    if not m2:
        continue
    for x in m2.group(2).split("/"):
        if x:
            blind.add(int(x))
bf.close()
print("BLIND 清单 %d 条" % len(blind))
assert len(blind) == 351, "BLIND 清单 %d != 351（b071 定值）" % len(blind)

# ---- 读候选 ----
cands = []
cp = os.path.join(LOG, "%s_candidates.txt" % TAG)
raw = io.open(cp, "rb").read()
assert raw[:3] != b"\xef\xbb\xbf", "输出含 BOM"
assert b"\r" not in raw, "输出含 CR"
assert raw.endswith(b"\n"), "输出末行缺 LF"
txt = raw.decode("utf-8")
lines = [l for l in txt.split("\n") if l.strip()]
for ln in lines:
    f = ln.split("|", 2)
    if len(f) != 3:
        bad("F", "字段%d %s" % (len(f), ln[:30]))
        continue
    pk, lvl, summ = f[0].strip(), f[1].strip(), f[2].strip()
    if not pk.isdigit():
        bad("F", "pk 非数字 %s" % pk)
        continue
    pk = int(pk)
    if lvl not in ("L3", "L4"):
        bad("F", "等级 %s @%d" % (lvl, pk))
    cands.append((pk, lvl, summ))

pks = [c[0] for c in cands]
if pks != sorted(pks):
    bad("F", "pk 非升序")
if len(set(pks)) != len(pks):
    bad("F", "pk 重复 %d" % (len(pks) - len(set(pks))))

for pk, lvl, summ in cands:
    if pk not in digest_pk:
        bad("W", "pk %d 不在 digest 窗口" % pk)
    if pk in JUMPS:
        bad("W", "pk %d 是跳号编号" % pk)
    if pk in EMPTY:
        bad("W", "pk %d 正文全空" % pk)
    if not (MIN_SUM <= len(summ) <= MAX_SUM):
        bad("L", "%d 摘要 %d 字: %s" % (pk, len(summ), summ[:40]))
    for ch in summ:
        if ch in FORBID:
            bad("C", "%d 禁字符 U+%04X" % (pk, ord(ch)))
        if ch in QUOTE:
            bad("C", "%d 引号形态 U+%04X" % (pk, ord(ch)))
    if summ[0] in "0123456789":
        bad("T", "%d 以数字开头" % pk)
    if summ[-1] in TRAIL or summ[-1].isspace():
        bad("T", "%d 以 %r 收尾" % (pk, summ[-1]))
    if summ != summ.strip():
        bad("T", "%d 首尾含空白" % pk)
    if pk in blind:
        bad("B", "%d 在 BLIND 清单" % pk)

print("=" * 66)
print("候选 %d 条 | L4=%d L3=%d"
      % (len(cands), sum(1 for c in cands if c[1] == "L4"),
         sum(1 for c in cands if c[1] == "L3")))
if fails:
    for k, v in fails.items():
        print("\n[%s] %d 项" % (k, len(v)))
        for x in v[:25]:
            print("   ", x)
        if len(v) > 25:
            print("    …其余 %d 项" % (len(v) - 25))
    sys.exit(2)
print("门禁全绿：0 违规")
