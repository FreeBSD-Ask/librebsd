# -*- coding: utf-8 -*-
"""把 2600169 的修正叙述外科补进 88.5 宿主块身。

大纲脚本按 ROW_MINE 标记幂等，2600169 的块已带着旧叙述（＝候选摘要逐字复制）
写进宿主，重跑 outline 只会跳过它。故此单独做定点替换：块头、claim_id、
证据等级、日期前缀与 L3 纪律句一律不动，只换块身里那一句叙述本体。

替换前后各做一次全文唯一性断言——旧串若在本宿主出现不止一处，
说明另有同名文本，贸然替换会污染不相干段落，此时直接中止。
"""
import io
import os

ROOT = r"d:\librebsd\05-卷册大纲\第05卷-freebsd的工程化奠基\第88章-freebsd2x站稳脚跟"
PK = "2600169"
MARK = "<!-- ROW_MINE: freebsd-hackers.messages.%s -->" % PK
OLD = ("Philippe Regnauld 回复 Eicon 讨论，认为 ETInc 能做 Eicon 能做的事，"
       "不必拘泥 Eicon 本身")
NEW = ("Philippe Regnauld 在询问 FreeBSD 上能否运行 Eicon 卡的讨论里回帖 "
       "认为 ETInc 能做 Eicon 能做的事 由此不必执着于 Eicon 本身")


def main():
    fp = os.path.join(ROOT, [f for f in os.listdir(ROOT) if f.startswith("88.5-")][0])
    with io.open(fp, "rb") as fh:
        b = fh.read()
    assert not b.startswith(b"\xef\xbb\xbf") and b"\r\n" not in b, "BOM/CRLF"
    t = b.decode("utf-8")
    assert t.count(MARK) == 1, "标记命中 %d 次" % t.count(MARK)
    blk = t[t.find(MARK):]
    blk = blk[:blk.find("\n\n<!-- ROW_MINE:")] if "\n\n<!-- ROW_MINE:" in blk else blk
    assert OLD in blk, "旧叙述不在本块内（已被改过？）"
    assert t.count(OLD) == 1, "旧串全文件命中 %d 次，非唯一" % t.count(OLD)
    assert NEW not in t, "新串已存在"
    before = t.count("ROW_MINE:")
    t2 = t.replace(OLD, NEW)
    assert t2.count(MARK) == 1 and t2.count("ROW_MINE:") == before, "块数变化"
    assert "证据等级：L3" in t2[t2.find(MARK):t2.find(MARK) + 400], "等级行被破坏"
    tmp = fp + ".tmpw"
    with io.open(tmp, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(t2)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, fp)
    rb = io.open(fp, "rb").read()
    assert rb == t2.encode("utf-8"), "回读失配"
    assert not rb.startswith(b"\xef\xbb\xbf") and b"\r\n" not in rb, "编码异常"
    print("bytes %d -> %d (+%d)" % (len(b), len(rb), len(rb) - len(b)))
    print("ROW_MINE 总量 %d" % rb.decode("utf-8").count("ROW_MINE:"))
    print("DONE 宿主定点替换并回读校验")


if __name__ == "__main__":
    main()
