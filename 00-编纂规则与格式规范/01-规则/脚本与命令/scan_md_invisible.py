#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""扫描 *.md 中的不可见字符（只读，不写盘）。

输出：
  script/_inv_md/inventory.tsv   按码位汇总
  script/_inv_md/detail.jsonl    逐处明细（文件、行、列、码位、容器上下文）
  script/_inv_md/summary.txt     汇总

码位范围：
  Zs 类（除 U+0020 半角空格）：U+00A0 U+1680 U+2000-200A U+202F U+205F U+3000
  Cf 类（格式控制符）：U+00AD U+0600-0605 U+061C U+06DD U+070F U+0890-0891
                        U+08E2 U+180E U+200B-200F U+202A-202E U+2060-2064
                        U+2066-206F U+FEFF U+FFF9-FFFB U+110BD U+110CD
                        U+13430-1343F U+1BCA0-1BCA3 U+1D173-1D17A U+E0001 U+E0020-E007F
  Mn 类孤立不可见：U+034F U+115F U+1160 U+3164 U+FFA0
  替换字符：U+FFFD（单独计，建议只报不删）
"""
import json
import os
import subprocess
import sys
import unicodedata
from collections import Counter, defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
OUT = os.path.join(ROOT, "script", "_inv_md")

SPECIFIC = {
    0x034F: "CGJ 组合字形连接符",
    0x115F: "HANGUL CHOSEONG FILLER",
    0x1160: "HANGUL JUNGSEONG FILLER",
    0x3164: "HANGUL FILLER",
    0xFFA0: "HALFWIDTH HANGUL FILLER",
    0xFFFD: "REPLACEMENT CHARACTER（只报不删）",
}


def is_target(cp):
    ch = chr(cp)
    cat = unicodedata.category(ch)
    if cp == 0x20:
        return False
    if cat == "Zs":
        return True
    if cat == "Cf":
        return True
    if cp in SPECIFIC:
        return True
    return False


def name_of(cp):
    if cp in SPECIFIC:
        return SPECIFIC[cp]
    try:
        return unicodedata.name(chr(cp))
    except ValueError:
        return "UNKNOWN"


def list_md():
    p = subprocess.run(["git", "ls-files", "-z", "--", "*.md"], cwd=ROOT,
                       stdout=subprocess.PIPE, check=True)
    return [x.decode("utf-8", "surrogateescape") for x in p.stdout.split(b"\0") if x]


def fence_state(line, state):
    """返回 (是否处于代码块内[进入前], 新状态)。围栏以 ``` 或 ~~~ 开头。"""
    s = line.lstrip()
    if s.startswith("```") or s.startswith("~~~"):
        return state, (not state)
    return state, state


def classify(ch, line, idx, in_fence):
    prev = line[idx - 1] if idx > 0 else ""
    nxt = line[idx + 1] if idx + 1 < len(line) else ""
    prefix = line[:idx]
    if in_fence:
        box = "fence"
    elif line.lstrip().startswith("|"):
        box = "table"
    elif line.lstrip().startswith("![") or "![" in line:
        box = "image"
    else:
        box = "text"
    if ch in "\u3000\u00a0\u2007\u2008\u2009\u200a\u202f\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u205f\u1680":
        if prefix.strip() == "":
            pos = "line-lead"
        elif nxt == "":
            pos = "line-trail"
        elif prev and _cjk(prev) and nxt and _cjk(nxt):
            pos = "between-cjk"
        elif prev and _cjk(prev):
            pos = "after-cjk"
        elif nxt and _cjk(nxt):
            pos = "before-cjk"
        else:
            pos = "ascii-side"
    else:
        pos = ""
    if ch == "\u200d":
        if _emoji(prev) and _emoji(nxt):
            pos = "emoji-zwj"
        elif _emoji(prev):
            pos = "after-emoji"
    if ch == "\ufeff":
        pos = "bom" if idx == 0 else ("line-lead" if prefix.strip() == "" else "inline")
    return box, pos


def _cjk(ch):
    cp = ord(ch)
    return (0x3400 <= cp <= 0x4DBF or 0x4E00 <= cp <= 0x9FFF or
            0xF900 <= cp <= 0xFAFF or 0x3000 <= cp <= 0x303F or
            0xFF00 <= cp <= 0xFFEF)


def _emoji(ch):
    cp = ord(ch)
    return cp >= 0x1F000 or 0x2600 <= cp <= 0x27BF or cp in (0x2764, 0x2665)


def main():
    os.makedirs(OUT, exist_ok=True)
    files = list_md()
    per_cp = Counter()
    per_cp_files = defaultdict(set)
    per_cp_box = defaultdict(Counter)
    per_cp_pos = defaultdict(Counter)
    per_file = Counter()
    details = []
    bom_files = []
    decode_err = []
    for rel in files:
        path = os.path.join(ROOT, rel)
        raw = open(path, "rb").read()
        if raw.startswith(b"\xef\xbb\xbf"):
            bom_files.append(rel)
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError as e:
            decode_err.append((rel, str(e)))
            continue
        in_fence = False
        for ln, line in enumerate(text.split("\n"), 1):
            was_fence, in_fence = fence_state(line, in_fence)
            for idx, ch in enumerate(line):
                cp = ord(ch)
                if not is_target(cp):
                    continue
                box, pos = classify(ch, line, idx, was_fence)
                per_cp[cp] += 1
                per_cp_files[cp].add(rel)
                per_cp_box[cp][box] += 1
                per_cp_pos[cp][pos] += 1
                per_file[rel] += 1
                details.append({
                    "file": rel, "line": ln, "col": idx + 1, "cp": "U+%04X" % cp,
                    "name": name_of(cp), "box": box, "pos": pos,
                    "text": line,
                })
    with open(os.path.join(OUT, "detail.jsonl"), "w", encoding="utf-8", newline="\n") as f:
        for d in details:
            f.write(json.dumps(d, ensure_ascii=False) + "\n")
    with open(os.path.join(OUT, "inventory.tsv"), "w", encoding="utf-8", newline="\n") as f:
        f.write("codepoint\thex\tcount\tfiles\tname\tbox\tpos\n")
        for cp, n in per_cp.most_common():
            f.write("%s\t%04X\t%d\t%d\t%s\t%s\t%s\n" % (
                chr(cp) if unicodedata.category(chr(cp)) != "Cf" else "-",
                cp, n, len(per_cp_files[cp]), name_of(cp),
                json.dumps(dict(per_cp_box[cp]), ensure_ascii=False),
                json.dumps(dict(per_cp_pos[cp]), ensure_ascii=False)))
    lines = []
    lines.append("md 文件总数: %d" % len(files))
    lines.append("含 BOM 的 md: %d %s" % (len(bom_files), bom_files[:5]))
    lines.append("解码失败: %d %s" % (len(decode_err), decode_err[:5]))
    lines.append("命中总数: %d  涉及文件: %d  不同码位: %d" % (
        len(details), len(per_file), len(per_cp)))
    for cp, n in per_cp.most_common():
        lines.append("  U+%04X %-45s %7d 处  %5d 文件  box=%s  pos=%s" % (
            cp, name_of(cp)[:45], n, len(per_cp_files[cp]),
            dict(per_cp_box[cp]), dict(per_cp_pos[cp])))
    top = per_file.most_common(25)
    lines.append("文件命中 top25:")
    for rel, n in top:
        lines.append("  %6d  %s" % (n, rel))
    with open(os.path.join(OUT, "summary.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    sys.exit(main())
