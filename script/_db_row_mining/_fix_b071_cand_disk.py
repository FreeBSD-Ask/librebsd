# -*- coding: utf-8 -*-
"""fhk_b071 候选分件门禁侧外科修补（只处理磁盘实测的两类缺陷）。

1. 摘要超 80 字 -> 前缀保留式整词截断（机械归一，不改语义不新增内容）。
2. pk 归属错片且为 BLIND + 主体错配 -> 整行删除（删而非改）。
每步都先备份、改完回读校验、字节数守恒核对。
"""
import io
import os
import re
import shutil
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
RL = os.path.join(HERE, "review_logs")
TAG = "fhk_b071"
LIMIT = 80
# 必须整行删除的 pk（删而非改）。两条理由：
#   2598518(p2)  BLIND 行 + 主体错配：FROM 是 Julian Elischer，摘要却把主张
#                挂给被引用块里的 Jamil J. Weatherbee。
#   2600167/170/172/174/176/193(p35)  BLIND 行摘要写进了「本窗口仅见 X 的引用块
#                无自有文字」这类关于 420 字窗口可见性的元描述——那是读手自己的
#                阅读条件泄漏进摘要，不是关于邮件的主张，进宿主叙述会变成无意义残句；
#                其中 2600172 还同时点了人名并断言了 TCP 编码标准的技术立场，
#                而发帖人自有文字在窗口外，该立场无从取证。
DELETE_PKS = {"2598518": 2,
              "2600167": 35, "2600170": 35, "2600172": 35,
              "2600174": 35, "2600176": 35, "2600193": 35}


def load_blind():
    """BLIND 清单：只解析 'p01 2598423/...' 明细行，不扫全文。"""
    b = set()
    fp = os.path.join(RL, "_blind_%s.txt" % TAG)
    for ln in io.open(fp, encoding="utf-8"):
        s = ln.strip()
        m2 = re.match(r"^p(\d+)\s+([\d/]+)\s*$", s)
        if m2:
            for x in m2.group(2).split("/"):
                if x:
                    b.add(int(x))
    return b
TAIL = [u"\u3002", u"\uff0c", u"\uff1a", u"\uff1b", u"\uff1f",
        u"\uff01", u"\u3001", " ", "\t"]
LATIN = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789."


def cut80(s):
    """前缀保留式整词截断到 <=80 字，绝不在词中间断。

    先按 80 字切；若切点落在一个拉丁 token 的内部（切点之后仍有拉丁字符，
    或切点正好把词头留下）则回退到最近一个空白边界；再剥掉尾部标点与空白。
    回退后不足 20 字则放弃回退、退回硬切（宁可断词也不能把摘要截没）。
    """
    if len(s) <= LIMIT:
        return s
    base = s[:LIMIT]
    cand = base
    nxt = s[LIMIT] if LIMIT < len(s) else ""
    mid_word = bool(nxt and nxt in LATIN) or base[-1] in LATIN
    if mid_word:
        i = len(base) - 1
        while i > 0 and base[i] not in " \t":
            i -= 1
        if i > 0 and len(base[:i]) >= 20:
            cand = base[:i]
    while cand and cand[-1] in TAIL:
        cand = cand[:-1]
    return cand


def writeback(path, lines, tag):
    """回写前先备份；写后回读逐位核对。"""
    shutil.copy2(path, path + ".bak_fix")
    body = "\n".join(lines) + "\n"
    with io.open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(body)
        f.flush()
        os.fsync(f.fileno())
    raw = io.open(path, "rb").read()
    assert not raw.startswith(b"\xef\xbb\xbf"), tag + " 写后出现 BOM"
    assert b"\r" not in raw, tag + " 写后出现 CR"
    back = io.open(path, encoding="utf-8").read().rstrip("\n").split("\n")
    back = [x for x in back if x.strip()]
    assert back == lines, tag + " 回读行序与内存不一致"
    assert len(raw) == len(body.encode("utf-8")), tag + " 字节数不符"
    return len(raw)


fixed_len, dropped = [], []
blind = load_blind()

for k in range(1, 41):
    p = os.path.join(RL, "%s_candidates_p%d.txt" % (TAG, k))
    if not os.path.exists(p):
        continue
    # 幂等：上一轮若已备份过，先还原到读手原始产物再改，保证每次都是从原态改
    bak = p + ".bak_fix"
    if os.path.exists(bak):
        shutil.copy2(bak, p)
        os.remove(bak)
        print("p%-2d 已从 .bak_fix 还原到读手原始产物" % k)
    lines = [l.rstrip("\n") for l in
             io.open(p, encoding="utf-8").read().split("\n") if l.strip()]
    out = []
    for l in lines:
        f = l.split("|", 2)
        if len(f) != 3:
            out.append(l)
            continue
        pk, lv, sm = f[0], f[1].strip(), f[2]
        if pk in DELETE_PKS and DELETE_PKS[pk] == k:
            dropped.append((k, pk, lv, sm))
            continue
        if int(pk) in blind:
            dropped.append((k, pk, lv, sm))
            continue
        if len(sm) > LIMIT:
            new = cut80(sm)
            fixed_len.append((k, pk, len(sm), len(new), new))
            out.append("%s|%s|%s" % (pk, lv, new))
        else:
            out.append(l)
    if out != lines:
        n = writeback(p, out, "p%d" % k)
        print("p%-2d 改写 %d 行 -> %d 行  %d B" % (k, len(lines), len(out), n))

print()
print("=== 摘要截断归一 %d 条 ===" % len(fixed_len))
for k, pk, a, b, new in fixed_len:
    print("  p%-2d pk %-8s %2d -> %2d | %s" % (k, pk, a, b, new))
print()
print("=== 整行删除 %d 条（删而非改）===" % len(dropped))
for k, pk, lv, sm in dropped:
    print("  p%-2d pk %s %s | %s" % (k, pk, lv, sm))

# 备份已回读校验通过，清理以免被 git add -f 扫进版本库
left = []
for k in range(1, 41):
    p = os.path.join(RL, "%s_candidates_p%d.txt" % (TAG, k))
    b = p + ".bak_fix"
    if os.path.exists(b):
        os.remove(b)
        left.append(k)
print()
print("已清理 .bak_fix 备份：%d 份 %s" % (len(left), left))
