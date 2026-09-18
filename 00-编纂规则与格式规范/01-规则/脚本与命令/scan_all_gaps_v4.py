#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
扫描全部大纲章节，识别真正的子节编号缺口（v4）。

策略：
- 区分两种章节模式：
  1. 拆分模式：章目录下存在 第X.Y节.md 子文件，index.md 应完整引用所有子文件
  2. 单文件模式：所有内容在 index.md 内（用 #### X.Y 作为正文标题），无子文件
- 只对"拆分模式"章节检查缺口
- 真正缺口 = 缺口B（子文件存在但 index.md 未引用）
- 缺口A 在拆分模式下也可能是真缺口（index.md 引用但子文件不存在）

同时排除时间线条目（如 1992.1、2006.11）和版本号条目（如 2.0、10.0）。
"""

import os
import re
import json
from pathlib import Path

OUTLINE_ROOT = Path(r"c:\Users\ykla\Documents\hibsd\大纲")

SECTION_FILE_RE = re.compile(r"第(\d+)\.(\d+)节\.md$")

# 各种 index.md 引用格式
INDEX_TABLE_ROW_RE = re.compile(r"^\|\s*(\d+)\.(\d+)\s*\|")
INDEX_LIST_ROW_RE = re.compile(r"^\d+\.\s*\[?(\d+)\.(\d+)")
INDEX_HEADING4_RE = re.compile(r"^####\s+(\d+)\.(\d+)\s")
INDEX_HEADING3_RE = re.compile(r"^###\s+(\d+)\.(\d+)\s")

GAP_HINT_RE = re.compile(r"(未出现|非拆分导致缺失|无此节号|原文件即无)")
INTERVIEW_FILE_RE = re.compile(r"^采访录(\u003a|:)?", re.UNICODE)

MAX_CHAP = 157


def is_valid_section(chap_num: int, sub_num_str: str) -> bool:
    if chap_num < 1 or chap_num > MAX_CHAP:
        return False
    try:
        sub_num = int(sub_num_str)
        if sub_num == 0:
            return False
    except ValueError:
        return False
    return True


def scan_chapter(chap_dir: Path):
    chap_name = chap_dir.name
    m = re.match(r"第(\d+)章", chap_name)
    if not m:
        return None
    chap_num = int(m.group(1))

    actual_files = {}  # 节号(float) -> 文件名
    interview_files = []
    for f in chap_dir.iterdir():
        if not f.is_file():
            continue
        if (m := SECTION_FILE_RE.match(f.name)):
            sec_str = f"{m.group(1)}.{m.group(2)}"
            sec = float(sec_str)
            actual_files[sec] = f.name
        elif INTERVIEW_FILE_RE.match(f.name):
            interview_files.append(f.name)

    # 单文件模式：无子文件，跳过
    if not actual_files:
        return None

    # 拆分模式：检查 index.md 是否完整引用所有子文件
    index_path = chap_dir / "index.md"
    index_sections = {}
    index_hints = []
    index_interview_refs = []
    if index_path.exists():
        with open(index_path, "r", encoding="utf-8") as fp:
            for line in fp:
                matched_sec = None
                if (m := INDEX_TABLE_ROW_RE.match(line)):
                    chap_n, sub_n = int(m.group(1)), m.group(2)
                    if is_valid_section(chap_n, sub_n) and chap_n == chap_num:
                        matched_sec = float(f"{chap_n}.{sub_n}")
                elif (m := INDEX_HEADING4_RE.match(line)):
                    chap_n, sub_n = int(m.group(1)), m.group(2)
                    if is_valid_section(chap_n, sub_n) and chap_n == chap_num:
                        matched_sec = float(f"{chap_n}.{sub_n}")
                elif (m := INDEX_HEADING3_RE.match(line)):
                    chap_n, sub_n = int(m.group(1)), m.group(2)
                    if is_valid_section(chap_n, sub_n) and chap_n == chap_num:
                        matched_sec = float(f"{chap_n}.{sub_n}")
                elif (m := INDEX_LIST_ROW_RE.match(line)):
                    chap_n, sub_n = int(m.group(1)), m.group(2)
                    if is_valid_section(chap_n, sub_n) and chap_n == chap_num:
                        matched_sec = float(f"{chap_n}.{sub_n}")
                if matched_sec is not None:
                    index_sections[matched_sec] = line.strip()
                    if "采访录" in line:
                        index_interview_refs.append(matched_sec)
                elif "采访录" in line:
                    m2 = re.search(r"第\s*(\d+)\.(\d+)\s", line)
                    if m2:
                        chap_n, sub_n = int(m2.group(1)), m2.group(2)
                        if chap_n == chap_num and is_valid_section(chap_n, sub_n):
                            sec = float(f"{chap_n}.{sub_n}")
                            index_interview_refs.append(sec)
                            index_sections[sec] = line.strip()
                if GAP_HINT_RE.search(line):
                    index_hints.append(line.strip())

    actual_set = set(actual_files.keys())
    index_set = set(index_sections.keys())

    # 缺口A：index.md 引用但无对应子文件（排除采访录独立文件约定）
    missing_files = []
    for sec in sorted(index_set - actual_set):
        if sec in index_interview_refs:
            continue
        missing_files.append((sec, index_sections.get(sec, "")))

    # 缺口B：子文件存在但 index.md 未引用
    missing_in_index = []
    for sec in sorted(actual_set - index_set):
        missing_in_index.append((sec, actual_files[sec]))

    return {
        "chap_num": chap_num,
        "chap_name": chap_name,
        "chap_dir": str(chap_dir),
        "actual_files": actual_files,
        "interview_files": interview_files,
        "index_sections": list(index_set),
        "index_interview_refs": index_interview_refs,
        "index_hints": index_hints,
        "missing_files": missing_files,
        "missing_in_index": missing_in_index,
    }


def main():
    results = []
    for vol_dir in sorted(OUTLINE_ROOT.iterdir()):
        if not vol_dir.is_dir() or not vol_dir.name.startswith("第"):
            continue
        for chap_dir in sorted(vol_dir.iterdir()):
            if not chap_dir.is_dir() or not chap_dir.name.startswith("第"):
                continue
            r = scan_chapter(chap_dir)
            if r:
                results.append(r)

    print("=" * 80)
    print("编号缺口扫描报告（v4，仅检查拆分模式章节）")
    print("=" * 80)

    total_missing_files = 0
    total_missing_in_index = 0
    chapters_with_issues = 0

    for r in results:
        if r["missing_files"] or r["missing_in_index"]:
            chapters_with_issues += 1
            print(f"\n第{r['chap_num']}章 {r['chap_name']}")
            print(f"  目录：{r['chap_dir']}")
            print(f"  实际子文件数：{len(r['actual_files'])}，index.md 引用数：{len(r['index_sections'])}")
            if r["missing_files"]:
                print(f"  [缺口A] index.md 引用但无对应子文件（{len(r['missing_files'])} 处）：")
                for sec, line in r["missing_files"]:
                    print(f"    - {sec}: {line[:120]}")
                total_missing_files += len(r["missing_files"])
            if r["missing_in_index"]:
                print(f"  [缺口B] 子文件存在但 index.md 未引用（{len(r['missing_in_index'])} 处）：")
                for sec, fname in r["missing_in_index"]:
                    print(f"    - {sec}: {fname}")
                total_missing_in_index += len(r["missing_in_index"])

    print("\n" + "=" * 80)
    print(f"扫描完成：共扫描 {len(results)} 个拆分模式章节")
    print(f"  有问题章节：{chapters_with_issues} 章")
    print(f"  缺口A（index.md 引用但无子文件）：{total_missing_files} 处")
    print(f"  缺口B（子文件存在但 index.md 未引用）：{total_missing_in_index} 处")
    print("=" * 80)

    report_path = Path(r"c:\Users\ykla\Documents\hibsd\script\gap-scan-report-v4.json")
    with open(report_path, "w", encoding="utf-8") as fp:
        json.dump(results, fp, ensure_ascii=False, indent=2)
    print(f"详细 JSON 报告已写入：{report_path}")


if __name__ == "__main__":
    main()
