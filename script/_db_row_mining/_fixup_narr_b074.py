# -*- coding: utf-8 -*-
"""fhk_b074 叙述层外科修正（第二版）。

门禁 21 条违规两族，处置方式不同：

A 族「FreeBSD 后接英文普通词」——VERS_RE 只认 FreeBSD 接数字的形态，纯英文词组合
   由 FREEBSD_WORD = FreeBSD[- ]([A-Za-z][A-Za-z0-9]*) 判；注意该式在 FreeBSD 与
   单词之间允许多个 [- ]，所以「插空格」根本不改变匹配，必须让 FreeBSD 之后紧跟
   一个非 [A-Za-z] 字符（中文衔接字 的），正则才会失配。第一版按插空格改，
   等于没改，门禁照旧 21 条。

B 族「版本形态不在本封自有正文内」——SUBJ 与 > / : 引用块不算正文，版本号必须
   逐字出现在本封自有正文里。这类一律删掉或改写，不改成别的版本号、也不加注释
   说明来源（臆造断言一律删而非改）。
"""
import io
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RV = r"D:\librebsd\script\_db_row_mining\review_logs"
HOST = "885"

FBWORD = re.compile(r"FreeBSD[- ]([A-Za-z][A-Za-z0-9]*)")
VERBLIKE = set(["current", "stable", "release", "prerelease", "snapshot", "snap",
                "x", "r", "rc1", "rc2", "x11", "x11r6",
                "keltia", "www", "hackers"])
FORBID = set("「」『』*|\\")
QUOTES = set(chr(c) for c in [0x2018, 0x2019, 0x201C, 0x201D,
                              0x0027, 0x0022, 0x0060])
TRAIL = set("。，、；：？！…—．·~-.,;:?! ")
DATE_RE = re.compile(r"^\d{4}\s*年")

# pk -> (分件, 最终叙述)
FIX = {
    2604490: (2, "amancio 转贴自己早前发过的旧帖到本线，并请 FreeBSD 的 Java Team 把该信息补进 FreeBSD 的 Java 网页，语气轻松并称只是随手贴出旧帖供参考"),
    2604493: (2, "terry 转述 JWS 有 30 天评估版可从 Sun 下载，Sun 中期还将发布支持 JFC 1.1 的升级，并强调必须向对方注册才能下载该代码"),
    2604500: (2, "niall 转述 john 称该报错实为汇编器缺陷且修复已提交至 obj-aout.c，自己表示问题已消失并追问能否把它合并到 -stable"),
    2604507: (2, "niall 转述对方疑问为何需让 Linux 应用强制访问 /compat/linux 而非根目录，并报告创建符号链接后 Linux 二进制能读到真实 /etc 内容，认为该行为已属缺陷并已 send-pr，提议改用 FreeBSD 的 tar 进程收集文件"),
    2604706: (8, "jmb 宣布 FreeBSD 的 tokenring 与 FreeBSD 的 advocacy 两个列表都已就绪可用，tokenring@freebsd.org 与 advocacy@freebsd.org 分别是后两者的快捷别名，供大家直接使用"),
    2604858: (11, "chuck 认为对方看上的这个项目开发相当活跃 而且它有自己的 cvs 树 所以他下注那种期待近几个月都不会成真 并自述在运维 3.0 current 版的 Journey2 与 picnic"),
    2604879: (12, "sos 先反问对方是不是在说自己看过那些东西，随后确认自己确实看过，并表示仍在斟酌如何在 TNG 的 atapi 代码里落实，签名自署 FreeBSD 的 Core Team 成员"),
    2604911: (13, "greenman 作为 FreeBSD 的 Project 联合创始人回称同一份内核内存太小的报错已在另一封邮件里答过，原邮件里给出 HINT 提示必须把 VM_KMEM_SIZE 调大，本封只以 -DG 签名收尾"),
    2605017: (15, "christoph 投票支持建立一个 FreeBSD 的 kde 小组，并在正文自签 Chris Christoph P. U. Kukulies 作为署名"),
    2605019: (16, "jaroslav 反问是否也要建一个 FreeBSD 的 Gnome 小组，并以 PS 附言说这类桌面环境的议题应该归入 freebsd-ports 来讨论"),
    2605199: (19, "david 请对方说明如何查 cvs 客户端与服务器所用的 login classes，并附 FreeBSD 2.2.6-stable 系统跑 cvs -q update -d 在 64MB PPro-200 上几乎必然冻结"),
    2605276: (21, "Robert 引 drosih 建议沿用 SIGDANGER 命名，自述在 2.2.x、SunOs、Solaris、HPUX、AIX 上构建同包都能完成，唯独 AIX 例外"),
    2605391: (25, "andreas 称 blender 默认全屏启动，用较小几何参数部分可行，摆弄界面能触发 segfault；对方在 -current 上试跑后屏幕很快变蓝，与他一致，只因无 X11 的 2.2-stable 服务器而无法核实 2.2.5(6) 的猜测"),
    2605395: (25, "chris 询问 SONY 的 SDT-9000 DDS-3 DAT 磁带机在 FreeBSD 2.2.6 上是否可用，并署名 FreeBSD 的 Book Project 的 Computer Support Analyst"),
    2605733: (33, "ruslan 转达 Cyclades Corp 发布的 FreeBSD 的 Cyclom-Y 驱动适用于 2.2.5 或更新版本，发行版自带的那份不支援 8Yo rev. 6.02 与 SM8/SM16 II，他也问是否有人在把 RELENG_2_2 的驱动与厂商版本同步"),
    2605735: (33, "dg 整封回信只有一句，说此事已列入他的待办清单，没有给出任何时间点，全文除了引用别人的提问之外只剩这一句，落款自称 FreeBSD 的 Project 的联合创始人兼首席架构师"),
    2605863: (36, "sumit 问 2.2.2 下怎么加系统调用，他说自己在 ip_input.c 里加了个全局 u_long 数组做 IP 层改写，数值目前硬编码，想在运行中的系统上改动数组条目，不确定系统调用是否唯一途径、要不要写汇编"),
    2606149: (43, "wilko 放出 FreeBSD 的 WorldCon 的信息稿初稿，地点定在荷兰 Arnhem 的 TCJA，并交代 Arnhem 在莱茵河畔、乘火车距阿姆斯特丹机场约一小时，同时向列表征集更合适的活动名称并欢迎意见"),
    2606398: (50, "hiren 在 FreeBSD 的 vfs 源码里查不到 VOP_ 系列宏的定义，也不知道 vop_create_args 等结构体的声明位置；他举 VOP_OPEN、VOP_CLOSE、VOP_ACCESS 与 vop_mknod_args，请人回复文件"),
}

# ---- 先在内存里逐条自检，任一条不过就不写盘 ----
print("== 自检 %d 条 ==" % len(FIX))
for pk, (part, nar) in sorted(FIX.items()):
    probe = re.sub(r"[A-Za-z]+\'[A-Za-z]+", "", nar)
    bad = []
    if not (60 <= len(nar) <= 140):
        bad.append("长度 %d" % len(nar))
    if set(probe) & (FORBID | QUOTES):
        bad.append("禁字符/引号")
    if nar[-1] in TRAIL:
        bad.append("尾标点")
    if nar[:1].isdigit():
        bad.append("数字开头")
    if DATE_RE.search(nar) or "\t" in nar or "\n" in nar or "\u3000" in nar:
        bad.append("日期/制表/全角空格")
    for w in FBWORD.findall(nar):
        if w.lower() not in VERBLIKE:
            bad.append("FBWORD %s" % w)
    print("  %d 分件 p%-3d len %d %s" % (pk, part, len(nar), "OK" if not bad else "FAIL %s" % bad))
    if bad:
        raise SystemExit("自检未过：%d %s" % (pk, bad))

# ---- 按分件重写：读原文件、替换目标行、按 pk 升序写回 ----
parts = {}
for pk, (part, nar) in FIX.items():
    parts.setdefault(part, []).append((pk, nar))

for part in sorted(parts):
    path = os.path.join(RV, "fhk_b074_mount_narr_p%d.tsv" % part)
    lines = [l for l in io.open(path, encoding="utf-8").read().split("\n")
             if l.strip()]
    rows = {}
    for l in lines:
        f = l.split("\t")
        rows[int(f[0])] = (f[1], f[2])
    for pk, nar in parts[part]:
        if pk not in rows:
            raise SystemExit("p%d 无 pk %d" % (part, pk))
        if rows[pk][0] != HOST:
            raise SystemExit("p%d pk %d 宿主 %s != %s" % (part, pk, rows[pk][0], HOST))
        if rows[pk][1] == nar:
            print("  p%-3d pk %d 已为目标文本，跳过" % (part, pk))
        rows[pk] = (HOST, nar)
    out = "".join("%d\t%s\t%s\n" % (pk, rows[pk][0], rows[pk][1])
                  for pk in sorted(rows))
    io.open(path, "w", encoding="utf-8", newline="\n").write(out)

    back = io.open(path, "rb").read()
    assert not back.startswith(b"\xef\xbb\xbf") and b"\r" not in back
    assert back.endswith(b"\n")
    blines = [l for l in back.decode("utf-8").split("\n") if l.strip()]
    assert len(blines) == len(lines), "行数 %d != %d" % (len(blines), len(lines))
    for l in blines:
        f = l.split("\t")
        assert len(f) == 3 and f[0].isdigit() and f[1] == HOST, l[:40]
    print("  p%-3d 已写 %d 行" % (part, len(blines)))

# ---- 复核：FBWORD 全清 ----
left = []
for part in sorted(parts):
    path = os.path.join(RV, "fhk_b074_mount_narr_p%d.tsv" % part)
    for l in io.open(path, encoding="utf-8").read().split("\n"):
        if not l.strip():
            continue
        f = l.split("\t")
        for w in FBWORD.findall(f[2]):
            if w.lower() not in VERBLIKE:
                left.append((f[0], w))
print("FBWORD 残留 %d 处 %s" % (len(left), left[:8]))
print("FIXED %d" % len(FIX))
