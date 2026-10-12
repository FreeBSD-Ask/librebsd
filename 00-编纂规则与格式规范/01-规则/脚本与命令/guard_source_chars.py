# -*- coding: utf-8 -*-
"""装配源字符守卫：拦截源件（.js／.css／模板）中会被门禁 A 拦下的字符。

设立缘由（2026-09-19）：本轮在源件注释里**三次**误用直角引号（「」），每次都要等门禁 A 报错
才发现，来回三次。本守卫把该检查前移到「写盘前」，一条命令即可自检。

检查项（与门禁 A 同口径）：
  · 直角引号 U+300C／U+300D（中文弯引号 “” 是允许的）
  · 全角空格 U+3000（流程规则 L1532 禁用）
  · 制表符 TAB
  · UTF-8 BOM、CRLF、替换字符 U+FFFD

用法：python script/_r66/_guard_source_chars.py [--fix]
       --fix 仅对「直角引号 → 中文弯引号」做自动归一（其余项只报不改）
"""

# 2026-09-20 第四十一批：经主理人批准提升为固定脚本
#   00-编纂规则与格式规范/01-规则/脚本与命令/guard_source_chars.py
# 缘由：原驻 /script（.gitignore 忽略）→ 未纳版本控制；且**覆盖清单漏掉内容源 `data/outline.txt`**，
#       致「改注时误用直角引号」只能在装配后由加强复核套件 A4／E4／K5 抓出（多一轮往返）。
#       现覆盖清单已含内容源；`script/_r66/_guard_source_chars.py` 为兼容薄壳。

import io
import os
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")
ROOT = r"D:/librebsd/08-核查报告与多轮复核/重构2026/"
FILES = [
    "data/outline.txt",          # 内容源（唯一真身）——2026-09-20 第四十一批补入：
                                 #   此前未覆盖，致「改注时误用直角引号」只能在装配后由套件 A4/E4/K5 抓出
    "assets/doc.js", "assets/theme-preset.js", "assets/doc.css",
    "assets/modern.css", "assets/page.template.html", "index.html",
]
BAD = [
    ("\u300c", "直角引号左 U+300C"),
    ("\u300d", "直角引号右 U+300D"),
    ("\u3000", "全角空格 U+3000"),
    ("\t", "制表符 TAB"),
    ("\ufffd", "替换字符 U+FFFD"),
]


def main():
    fix = "--fix" in sys.argv
    files = list(FILES)
    # 143 批 wave5（2026-10-12）：行为层源件清单化——src/js 清单项入守卫面
    mf = ROOT + "src/js/manifest.txt"
    if os.path.exists(mf):
        for ln in io.open(mf, encoding="utf-8").read().splitlines():
            ln = ln.strip()
            if ln and not ln.startswith("#"):
                files.append("src/js/" + ln)
    bad_total = 0
    for rel in files:
        p = ROOT + rel
        if not os.path.exists(p):
            print("  %-28s 缺失" % rel)
            continue
        raw = open(p, "rb").read()
        s = raw.decode("utf-8")
        issues = []
        notes = []
        if raw[:3] == b"\xef\xbb\xbf":
            issues.append("UTF-8 BOM")
        # ⚠️ CRLF 仅作提示、不计失败：本仓库 core.autocrlf=true 且 .gitattributes 未对
        #    *.js／*.css／*.html 声明 eol=lf → 工作树换行随环境而变，不是可靠不变量。
        #    实测装配产物 index.html 为 LF（装配器已归一），故无功能影响。
        if b"\r\n" in raw:
            notes.append("CRLF 换行 ×%d（本地 autocrlf 所致，装配产物为 LF，无功能影响）"
                         % raw.count(b"\r\n"))
        for ch, name in BAD:
            n = s.count(ch)
            if n:
                issues.append("%s ×%d" % (name, n))
        if issues:
            bad_total += 1
            print("  🔴 %-26s %s" % (rel, " ｜ ".join(issues)))
            if fix and ("\u300c" in s or "\u300d" in s):
                s2 = s.replace("\u300c", "\u201c").replace("\u300d", "\u201d")
                io.open(p, "w", encoding="utf-8", newline="\n").write(s2)
                print("       → 已归一：直角引号 -> 中文弯引号")
        else:
            print("  ✅ %-26s 通过%s" % (rel, ("  ｜ 提示：" + " ｜ ".join(notes)) if notes else ""))
    print()
    if bad_total == 0:
        print("守卫结论：全部源件字符合规（PASS）")
        return 0
    print("守卫结论：%d 个文件存在问题（%s）" % (bad_total, "已按 --fix 归一引号" if fix else "未修复"))
    return 1


if __name__ == "__main__":
    sys.exit(main())
