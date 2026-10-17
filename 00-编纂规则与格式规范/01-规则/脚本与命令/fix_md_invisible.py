#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""清除受版本控制 .md 中的不可见字符（默认 dry-run，--apply 写盘）。

处置口径（2026-10-17 主理人裁定）：
  1. 零宽／格式控制符（Cf 全体，含 U+200B-200F、U+202A-202E、U+2060-206F、
     U+FEFF、U+00AD、U+0601、U+034F 及 Unicode 填充符）——直接删除；
  2. 空格类（U+3000 全角空格、U+00A0、U+202F 等 Zs 非 U+0020）——一律改
     一个半角空格；含此类字符的极大空白串合并为一个 U+0020；行首／行尾
     的此类串整段删除（避免产生 Markdown 缩进或行尾空白）；
  3. U+FFFD 替换字符不属不可见字符，不处置，另行报告；
  4. 原文件换行符（LF／CRLF）逐行保留，编码 UTF-8 无 BOM，不新增 BOM；
  5. 05-卷册大纲/ 写盘前断言不含 CR（LF 形态）；全库直写字节，不经
     wo007 的 dbnames／术语规范化（避免越界改动）。

校验：写盘前断言“去除全部空白与目标字符后逐字相同”，即内容零改动。
"""
import argparse
import json
import os
import re
import subprocess
import sys
import unicodedata

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
DET = os.path.join(ROOT, "script", "_inv_md", "detail.jsonl")
OUTDIR = os.path.join(ROOT, "script", "_inv_md")

# 空格类（Zs，除 U+0020）
SPACE_EXTRA = set(range(0x2000, 0x200B)) | {0x00A0, 0x1680, 0x202F, 0x205F, 0x3000}
FILLER = {0x034F, 0x115F, 0x1160, 0x3164, 0xFFA0}

_ws_run = re.compile("[" + "\\u0020" + "".join("\\u%04X" % c for c in sorted(SPACE_EXTRA)) + "]+")


def is_invisible_extra(ch):
    cp = ord(ch)
    if cp in SPACE_EXTRA or cp in FILLER:
        return False  # 空格类另走合并逻辑
    return unicodedata.category(ch) == "Cf"


def norm_body(body):
    """返回 (新正文, 删除的格式符数, 合并的空格串数)。"""
    kept = []
    n_del = 0
    for ch in body:
        if is_invisible_extra(ch):
            n_del += 1
            continue
        kept.append(ch)
    line = "".join(kept)
    n_run = [0]

    def repl(m):
        run = m.group(0)
        if not any(ord(c) in SPACE_EXTRA for c in run):
            return run
        n_run[0] += 1
        if m.start() == 0 or m.end() == len(line):
            return ""
        return " "

    return _ws_run.sub(repl, line), n_del, n_run[0]


def split_eol(part):
    m = re.search(r"(\r\n|\n|\r)$", part)
    if not m:
        return part, ""
    return part[: m.start()], m.group(1)


def canon(s):
    """内容指纹：去掉全部空白与全部目标不可见字符。"""
    out = []
    for ch in s:
        if ch.isspace():
            continue
        if ord(ch) in SPACE_EXTRA or ord(ch) in FILLER:
            continue
        if unicodedata.category(ch) == "Cf":
            continue
        out.append(ch)
    return "".join(out)


def md_files():
    p = subprocess.run(["git", "ls-files", "-z", "--", "*.md"], cwd=ROOT,
                       stdout=subprocess.PIPE, check=True)
    return [x.decode("utf-8", "surrogateescape") for x in p.stdout.split(b"\0") if x]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    rows = []
    touched = 0
    for rel in md_files():
        path = os.path.join(ROOT, rel)
        raw = open(path, "rb").read()
        old = raw.decode("utf-8")
        parts = old.splitlines(keepends=True)
        if not parts:
            parts = [old]
        new_parts = []
        n_del = n_run = 0
        for part in parts:
            body, eol = split_eol(part)
            nb, a, b = norm_body(body)
            n_del += a
            n_run += b
            new_parts.append(nb + eol)
        new = "".join(new_parts)
        if new == old:
            continue
        assert canon(new) == canon(old), "内容指纹不符: %s" % rel
        assert len(re.findall(r"\r\n|\r|\n", new)) == len(re.findall(r"\r\n|\r|\n", old)), rel
        for ch in new:
            assert not (ord(ch) in SPACE_EXTRA or is_invisible_extra(ch)), (rel, hex(ord(ch)))
        touched += 1
        rows.append((rel, len(raw), len(new.encode("utf-8")), n_del, n_run))
        if args.apply:
            # 不走 write_guard：其 normalize_dbnames／normalize_terms 会顺带改写
            # *.db 与“基础系统”，超出本批“仅清不可见字符”的改动边界。
            if rel.startswith("05-卷册大纲/"):
                assert "\r" not in new, "05 文件须为 LF: %s" % rel
            with open(path, "wb") as f:
                f.write(new.encode("utf-8"))
        if args.limit and touched >= args.limit:
            break
    print("%s：命中文件 %d" % ("已写盘" if args.apply else "dry-run", touched))
    tot_del = sum(r[3] for r in rows)
    tot_run = sum(r[4] for r in rows)
    print("  删除格式符 %d 处，合并空格串 %d 处" % (tot_del, tot_run))
    with open(os.path.join(OUTDIR, "changes.tsv"), "w", encoding="utf-8", newline="\n") as f:
        f.write("file\tbytes_before\tbytes_after\tdel_cf\tsquash_runs\n")
        for r in rows:
            f.write("%s\t%d\t%d\t%d\t%d\n" % r)


if __name__ == "__main__":
    main()
