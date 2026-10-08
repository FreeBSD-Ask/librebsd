# -*- coding: utf-8 -*-
"""fhk_b074 叙述层外科修正（第三版，剩 3 条版本回源）。

三条各有独立根因，都是「叙述引了正文之外的事实」：

2604493  自有正文只剩一句 NOTE（必须注册才能下载）与签名；30 天评估版、JFC 1.1
         升级全在引用块里，属被转述者的内容。整句改写为只记他自有正文的事实。

2605199  自有正文写作「FreeBSD⏎2.2.6-stable」（换行分隔），所以子串
         FreeBSD 2.2.6-stable 命中不了。去掉 FreeBSD 前缀，只留 2.2.6-stable。

2605391  自有正文只有 2.2-stable（他手上的机器是无 X11 的服务器），从未出现
         2.2.5(6)——那是引文里的说法。删掉版本号，改为他原话「无法核实该假设」。

一律删断言而非改成别的版本号。
"""
import io
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RV = r"D:\librebsd\script\_db_row_mining\review_logs"
HOST = "885"

FIX = {
    2604493: (2, "terry 转贴前文内容，并在自有正文里特别注明必须向对方注册才能下载该代码，末尾自署 Terry Lambert 并称发帖意见仅代表本人"),
    2605199: (19, "david 请对方说明如何查 cvs 客户端与服务器所用的 login classes，并附 2.2.6-stable 系统跑 cvs -q update -d 在 64MB PPro-200 上几乎必然冻结"),
    2605391: (25, "andreas 称自己也碰到过同样的情况，说 blender 默认以全屏模式启动，改用更小的几何参数只能部分成功，摆弄界面还能触发 segfault，但他手上的 2.2-stable 机器都是没有 X11 的服务器，所以无法核实那个假设"),
}

VERBLIKE = set(["current", "stable", "release", "prerelease", "snapshot", "snap",
                "x", "r", "rc1", "rc2", "x11", "x11r6", "keltia", "www", "hackers"])
FBWORD = re.compile(r"FreeBSD[- ]([A-Za-z][A-Za-z0-9]*)")
FORBID = set("「」『』*|\\")
QUOTES = set(chr(c) for c in [0x2018, 0x2019, 0x201C, 0x201D,
                              0x0027, 0x0022, 0x0060])
TRAIL = set("。，、；：？！…—．·~-.,;:?! ")

for pk, (part, nar) in sorted(FIX.items()):
    probe = re.sub(r"[A-Za-z]+\'[A-Za-z]+", "", nar)
    bad = []
    if not (60 <= len(nar) <= 140):
        bad.append("长度 %d" % len(nar))
    if set(probe) & (FORBID | QUOTES):
        bad.append("禁字符/引号")
    if nar[-1] in TRAIL or nar[:1].isdigit() or "\t" in nar or "\u3000" in nar:
        bad.append("尾标点/数字开头/制表/全角空格")
    for w in FBWORD.findall(nar):
        if w.lower() not in VERBLIKE:
            bad.append("FBWORD %s" % w)
    print("  %d 分件 p%-3d len %d %s" % (pk, part, len(nar), "OK" if not bad else "FAIL %s" % bad))
    if bad:
        raise SystemExit("自检未过 %d" % pk)

parts = {}
for pk, (part, nar) in FIX.items():
    parts.setdefault(part, []).append((pk, nar))

for part in sorted(parts):
    path = os.path.join(RV, "fhk_b074_mount_narr_p%d.tsv" % part)
    lines = [l for l in io.open(path, encoding="utf-8").read().split("\n") if l.strip()]
    rows = {}
    for l in lines:
        f = l.split("\t")
        rows[int(f[0])] = (f[1], f[2])
    for pk, nar in parts[part]:
        assert pk in rows and rows[pk][0] == HOST, "p%d 缺 pk %d" % (part, pk)
        rows[pk] = (HOST, nar)
    out = "".join("%d\t%s\t%s\n" % (pk, rows[pk][0], rows[pk][1])
                  for pk in sorted(rows))
    io.open(path, "w", encoding="utf-8", newline="\n").write(out)
    back = io.open(path, "rb").read()
    assert not back.startswith(b"\xef\xbb\xbf") and b"\r" not in back
    blines = [l for l in back.decode("utf-8").split("\n") if l.strip()]
    assert len(blines) == len(lines), "行数 %d != %d" % (len(blines), len(lines))
    print("  p%-3d 已写 %d 行" % (part, len(blines)))

print("FIXED %d" % len(FIX))
