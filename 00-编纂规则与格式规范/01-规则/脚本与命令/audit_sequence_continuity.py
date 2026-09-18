# -*- coding: utf-8 -*-
"""目录页节号/章号连续性审计（固定脚本，规则引用）。v2：h3 锚点切章 + 述评恒末检查。

用法：python audit_sequence_continuity.py [index.html 路径]
默认路径：重构2026/index.html。

审计维度（按 h3 章锚点切章，至下一章锚点/文末）：
1) 章内节号：每章节号须为 N.1…N.k 且按文档序严格递增；
2) 节号章号一致性：节号前段须与所在章章题章号一致（无他章节混入）；
3) 卷内章号：每卷章号须为 1…k 连续；
4) 「本章书目述评」恒居章末（主理人规则 2026-09-10）。
输出：问题清单（0 问题即通过，exit 0；有问题 exit 1）。
"""
import re, sys, io, pathlib

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
DEFAULT = pathlib.Path(r"D:/librebsd/08-核查报告与多轮复核/重构2026/index.html")
path = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
html = path.read_text(encoding="utf-8")
issues = []

# 维度 1/2/4：h3 锚点切章
anchors = [(m.start(), int(re.search(r"第 (\d+) 章", m.group(0)).group(1)))
           for m in re.finditer(r'<h3 class="chapter"[^>]*>第 (\d+) 章[^<]*', html)]
for idx, (pos, ch) in enumerate(anchors):
    end = anchors[idx + 1][0] if idx + 1 < len(anchors) else len(html)
    seg = html[pos:end]
    secs = re.findall(r'sec-num[^>]*>(\d+)\.(\d+)</span>([^<]*)', seg)
    if not secs:
        continue
    for i, (ci, mi, _t) in enumerate(secs, 1):
        if int(ci) != ch:
            issues.append(f"章{ch}：第 {i} 节 {ci}.{mi} 章号错位")
        if int(mi) != i:
            issues.append(f"章{ch}：文档序第 {i} 节应为 {ch}.{i}，实际 {ci}.{mi}")
    bib = [i for i, (_ci, _mi, t) in enumerate(secs) if "本章书目述评" in t]
    for i in bib:
        if i != len(secs) - 1:
            issues.append(f"章{ch}：本章书目述评 {secs[i][0]}.{secs[i][1]} 非章末")

# 维度 3：卷内章号连续
vol = 0
chs = []
for m in re.finditer(r"<h2[^>]*>第[一二三四五六七八九十]+卷|<h3 class=\"chapter\"[^>]*>第 (\d+) 章", html):
    if m.group(0).startswith("<h2"):
        if chs and chs != list(range(1, len(chs) + 1)):
            issues.append(f"卷{vol} 章号序列 {chs} 非连续")
        vol += 1
        chs = []
    else:
        chs.append(int(m.group(1)))
if chs and chs != list(range(1, len(chs) + 1)):
    issues.append(f"卷{vol} 章号序列 {chs} 非连续")

print(f"审计文件：{path}")
print(f"节号/章号连续性＋述评恒末审计问题：{len(issues)} 处")
for x in issues:
    print(" -", x)
sys.exit(1 if issues else 0)
