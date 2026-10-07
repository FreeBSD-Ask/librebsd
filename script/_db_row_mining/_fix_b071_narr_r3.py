# -*- coding: utf-8 -*-
"""fhk_b071 叙述件 r3：只重订 2600169 一行（final_verify 第 14 项抓出）。

缺陷不是格式问题而是「零增量」：叙述手把候选摘要逐字抄成叙述，
等于把摘要又印了一遍，宿主块头与块身变成同一句话。

本封自有正文（剥掉 > 与 : 引导的引用块后）实际只有两行：
    Seems ETInc can do what Eicon does.
    （签名行）
真正属于 Philippe Regnauld 的断言只有一句：ETInc 能做 Eicon 能做的事。
「不必拘泥 Eicon 本身」是这句的直读推论，摘要里已有，叙述沿用不改强度。

线程语境（有人问 FreeBSD 上能否跑 Eicon 卡、有人被 Eicon 的 NDA 挡住）
在正文里是**引用块**，属被引者陈述，不得写成 Philippe 的主张，
所以叙述只把它当「回帖所在的讨论串」来交代，不替他背书。

关键字回查（须在自有正文逐字命中）：ETInc ✓、Eicon ✓；
版本号形态：无；FreeBSD 后接「上」（汉字），FREEBSD_WORD 不吃。
"""
import io
import os

TAG = "fhk_b071"
RL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "review_logs")
PART, PK = 43, "2600169"
NEW = ("Philippe Regnauld 在询问 FreeBSD 上能否运行 Eicon 卡的讨论里回帖 "
       "认为 ETInc 能做 Eicon 能做的事 由此不必执着于 Eicon 本身")
LO, HI = 60, 140


def main():
    assert LO <= len(NEW) <= HI, "新叙述长度 %d 越界" % len(NEW)
    for ch in "「」『』*|":
        assert ch not in NEW, "禁字符 %r" % ch
    for ch in [chr(0x2018), chr(0x2019), chr(0x201C), chr(0x201D),
               chr(0x0027), chr(0x0022), chr(0x0060)]:
        assert ch not in NEW, "引号形态 %r" % ch
    assert "\t" not in NEW and "\u3000" not in NEW, "制表符/全角空格"
    assert not NEW.startswith("。") and not NEW[0].isdigit(), "首字符 %r" % NEW[0]
    assert NEW[-1] not in "。，、；：？！…—．·~-.,;:?! ", "尾标点 %r" % NEW[-1]
    for bad in ["ROW_MINE", "来源：", "消息列表", "freebsd-hackers.messages"]:
        assert bad not in NEW, "来源尾巴 %r" % bad
    import re
    assert not re.search(r"\d{4}\s*年", NEW), "日期前缀"

    # 与候选摘要不得逐字相同（final_verify 第 14 项）
    cand = {}
    for ln in io.open(os.path.join(RL, TAG + "_candidates.txt"), encoding="utf-8"):
        if ln.strip():
            f = ln.rstrip("\n").split("|", 2)
            cand[f[0]] = (f[1], f[2])
    assert PK in cand, "pk 不在候选件"
    assert NEW != cand[PK][1], "新叙述仍与候选摘要逐字相同"

    # 关键字回查：叙述里的英文实体须在自有正文逐字命中
    own = ""
    for ln in io.open(os.path.join(RL, "fhk_b071_cands_body_p%d.txt" % PART),
                      encoding="utf-8"):
        s = ln.lstrip()
        if not s or s.startswith(">") or s.startswith(":"):
            continue
        if re.match(r"^(DATE|FROM|SUBJ|摘要|=====)", s):
            continue
        own += ln
    for tok in ("ETInc", "Eicon"):
        assert tok in own, "关键字 %r 不在自有正文（臆造）" % tok

    p = os.path.join(RL, "%s_mount_narr_p%d.tsv" % (TAG, PART))
    bak = p + ".bak_fix"
    with io.open(p, "rb") as fh:
        b = fh.read()
    with io.open(bak, "wb") as fh:
        fh.write(b)
    L = b.decode("utf-8").split("\n")
    assert L[-1] == "", "末行无 LF"
    L = L[:-1]
    n0 = len(L)
    hits = [i for i, l in enumerate(L)
            if l.split("\t")[0] == PK and len(l.split("\t")) == 3]
    assert len(hits) == 1, "pk %s 命中 %d 行" % (PK, len(hits))
    i = hits[0]
    f = L[i].split("\t")
    assert f[1] == "885", "宿主列 %r" % f[1]
    print("旧 %d 字: %s" % (len(f[2]), f[2]))
    L[i] = "\t".join([f[0], f[1], NEW])
    print("新 %d 字: %s" % (len(NEW), NEW))
    assert len(L) == n0, "行数变化 %d -> %d" % (n0, len(L))
    out = "\n".join(L) + "\n"
    tmp = p + ".tmpw"
    with io.open(tmp, "w", encoding="utf-8", newline="") as fh:
        fh.write(out)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, p)
    rb = io.open(p, "rb").read()
    assert rb.decode("utf-8").rstrip("\n").split("\n") == L, "回读不符"
    assert not rb.startswith(b"\xef\xbb\xbf") and b"\r" not in rb, "编码异常"
    os.remove(bak)
    print("DONE p%d 写回并回读校验" % PART)


if __name__ == "__main__":
    main()
