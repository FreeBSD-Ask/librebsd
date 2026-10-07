# -*- coding: utf-8 -*-
"""fhk_b071 叙述件 r1 定点修复（只改被门禁拦截的 25 行，其余分件字节不动）。

两类缺陷，全部按本封自有正文字面定取舍：
A. 「FreeBSD 后接英文普通词」版本误判陷阱：原文多为**逐字引句**
   （如 FreeBSD ports / FreeBSD port / FreeBSD Nomads / FreeBSD Atapi / FreeBSD support），
   白名单不收这些词 → 在 FreeBSD 与英文词之间插中文衔接词「的」或改译该词，
   不断裂原意、不改断言强度。
B. 版本形态字面不在自有正文：正文把版本换行断开（FreeBSD ⏎ 2.2.5-Release）
   或无空格连写（FreeBSD2.2.2）→ 只保留正文里逐字存在的那一段。
C. 日期前缀（四位数字加年）→ 改中文数字，语义不动。
D. 臆造：2599131 的「标准 1.44 MB 软驱」在本封自有正文 0 命中 → 删而非改。

idempotent：每次运行先按 pk 断言旧串仍在，再替换；重复跑会因旧串已不存在而报错停止。
"""
import io
import os

TAG = "fhk_b071"
RL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "review_logs")
LO, HI = 60, 140

# pk -> (旧串, 新串)；pk -> None 表示整段删除尾句
FIX = {
    # A 类：插中文衔接 / 改译
    "2598645": ("FreeBSD list 的邮件", "FreeBSD 邮件列表的来信"),
    "2599319": ("首个 FreeBSD fdisk 分区", "首个 FreeBSD 的 fdisk 分区"),
    "2599460": ("FreeBSD 应基于自有技术", "FreeBSD 需要自有集成数据库系统"),
    "2599649": ("回答 FreeBSD ACL 询问", "回答 ACL 相关询问"),
    "2599715": ("FreeBSD ports 集合", "FreeBSD 的 ports 集合"),
    "2599846": ("FreeBSD port，", "FreeBSD 的 port，"),
    "2599918": ("FreeBSD halt 时", "从 FreeBSD 执行 halt 时"),
    "2599989": ("FreeBSD Nomads", "FreeBSD 的 Nomads"),
    "2600022": ("FreeBSD support 请求", "FreeBSD 的支持请求"),
    "2600068": ("FreeBSD Atapi Project", "FreeBSD 的 Atapi Project"),
    # FreeBSD Hacker（发帖人化名）→ 拆断相邻，两个词都保留
    "2599367": ("FreeBSD Hacker", "化名 Hacker 的 FreeBSD 发帖人"),
    "2599457": ("FreeBSD Hacker", "化名 Hacker 的 FreeBSD 发帖人"),
    "2599458": ("FreeBSD Hacker", "化名 Hacker 的 FreeBSD 发帖人"),
    "2599528": ("FreeBSD Hacker", "化名 Hacker 的 FreeBSD 发帖人"),
    # B 类：只留正文逐字存在的版本片段
    "2598896": ("FreeBSD 2.2.5-Release", "2.2.5-Release"),
    "2599122": ("FreeBSD current", "-current"),
    "2599201": ("FreeBSD 3.0-971208-SNAP", "3.0-971208-SNAP"),
    "2599565": ("FreeBSD 2.2.2", "FreeBSD2.2.2"),
    "2599624": ("FreeBSD 1.x 时代", "1.x 时代"),
    "2599974": ("FreeBSD 2.2.5", "2.2.5"),
    "2599986": ("FreeBSD 2.0.5", "2.0.5"),
    "2600035": ("FreeBSD 2.2.5-STABLE", "2.2.5-STABLE"),
    # C 类：日期前缀改中文数字
    "2598720": ("1993 年左右", "一九九三年前后"),
    "2599198": ("自 1994 年起", "自一九九四年起"),
    # D 类：臆造断言整段删除
    "2599131": ("，标准 1.44 MB 软驱能正常工作", ""),
}


def part_of(pk):
    """从实际分件里查 pk 属于第几片，不做任何算术外推。"""
    for k in range(1, 51):
        p = os.path.join(RL, "%s_mount_narr_p%d.tsv" % (TAG, k))
        if not os.path.exists(p):
            continue
        for l in io.open(p, encoding="utf-8"):
            f = l.rstrip("\n").split("\t")
            if len(f) == 3 and f[0] == pk:
                return k, f
    raise SystemExit("pk %s 未在任何分件中" % pk)


def main():
    by_part = {}
    for pk, rep in FIX.items():
        k, f = part_of(pk)
        by_part.setdefault(k, []).append((pk, rep, f))
    print("待修 %d 行，涉 %d 个分件" % (len(FIX), len(by_part)))

    for k in sorted(by_part):
        p = os.path.join(RL, "%s_mount_narr_p%d.tsv" % (TAG, k))
        bak = p + ".bak_fix"
        b = io.open(p, "rb").read()
        with io.open(bak, "wb") as fh:
            fh.write(b)
        L = b.decode("utf-8").split("\n")
        assert L[-1] == "", "末行无 LF"
        L = L[:-1]
        n0 = len(L)
        for pk, (old, new), f in by_part[k]:
            line0 = "\t".join(f)
            assert line0 in L, "pk %s 整行不在分件中（已被并发改动）" % pk
            assert old in f[2], "pk %s 旧串 %r 不在叙述中（已修过？）" % (pk, old)
            nt = f[2].replace(old, new)
            assert LO <= len(nt) <= HI, \
                "pk %s 长度越界 %d（%s）" % (pk, len(nt), nt[:40])
            assert not nt.startswith("。") and nt[-1] not in "。，：；？！、·～~ -.:;?!", \
                "pk %s 尾标点 %r" % (pk, nt[-1])
            for ch in "「」『』*|":
                assert ch not in nt, "pk %s 禁字符 %r" % (pk, ch)
            L[L.index(line0)] = "\t".join([f[0], f[1], nt])
            print("  p%-3d %s  %d -> %d 字 | %s -> %s"
                  % (k, pk, len(f[2]), len(nt), old[:24], new[:24]))
        assert len(L) == n0, "分件 p%d 行数变化 %d -> %d" % (k, n0, len(L))
        out = "\n".join(L) + "\n"
        tmp = p + ".tmpw"
        with io.open(tmp, "w", encoding="utf-8", newline="") as fh:
            fh.write(out)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp, p)
        rb = io.open(p, "rb").read()
        assert rb.decode("utf-8").rstrip("\n").split("\n") == L, "p%d 回读不符" % k
        assert not rb.startswith(b"\xef\xbb\xbf") and b"\r" not in rb, "p%d 编码异常" % k
        os.remove(bak)
    print("DONE 全部 %d 个分件已写回并回读校验" % len(by_part))


if __name__ == "__main__":
    main()
