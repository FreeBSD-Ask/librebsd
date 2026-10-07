# -*- coding: utf-8 -*-
"""fhk_b071 叙述件 r2：只重订 2599460 一行。

r1 用了「FreeBSD 应基于自有技术 → FreeBSD 需要自有集成数据库系统」的局部替换，
结果原句「构建集成数据库系统」被叠在替换后，读成「需要自有集成数据库系统构建
集成数据库系统」——同一短语重复两次，且「FreeBSD Hacker」化名仍未拆断。

按本封自有正文字面整行重订：
  FROM  FreeBSD Hacker <freebsd@acroal.com>
  正文  "spent the last week trying to get PostGreSQL to work with windows, unsuccessfully"
        "FreeBSD needs to have its own integrated database system based on noone elses technology"
        "10x more efficient than any 2 bit half-ass commercial port"
化名拆成「化名 Hacker 的 FreeBSD 发帖人」，两个词都留但不再相邻（门禁的
FREEBSD_WORD 只吃 FreeBSD 后接拉丁词）。强度词按原文：unsuccessfully / 10x。
"""
import io
import os

TAG = "fhk_b071"
RL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "review_logs")
PART, PK = 23, "2599460"
NEW = ("化名 Hacker 的 FreeBSD 发帖人称花整整一周想让 PostGreSQL 在 windows 上跑通都失败 "
       "主张 FreeBSD 应有不依赖任何人技术的自有集成数据库 "
       "认为社区自研会比半吊子商业移植版高效十倍")
LO, HI = 60, 140


def main():
    assert LO <= len(NEW) <= HI, "新叙述长度 %d 越界" % len(NEW)
    for ch in "「」『』*|":
        assert ch not in NEW, "禁字符 %r" % ch
    for ch in [chr(0x2018), chr(0x2019), chr(0x201C), chr(0x201D),
               chr(0x0027), chr(0x0022), chr(0x0060)]:
        assert ch not in NEW, "引号形态 %r" % ch
    assert not NEW.startswith("。") and not NEW[0].isdigit(), "首字符 %r" % NEW[0]
    assert NEW[-1] not in "。，、；：？！…—．·~-.,;:?! ", "尾标点 %r" % NEW[-1]
    for bad in ["ROW_MINE", "来源：", "消息列表", "freebsd-hackers.messages"]:
        assert bad not in NEW, "来源尾巴 %r" % bad

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
