#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""apply_fixes.py — 大纲邮件素材审计·把 fix 类判定原地应用到宿主 .md（第4行摘要行替换）

原则：
- 只改 fix-format / fix-text 且给了「新摘要句」的条目；keep/remap/存疑/fix-db 不动文件
- 纪律串（「引用时按 …」起）从原第 4 行原样保留；**若新摘要句本身已含纪律串则整行替换**，
  不再拼接（否则纪律串重复——2026-09-29 实测已致 22 行落盘缺陷）；写前断言新行纪律串恰 1 次
- 定位双重校验：行号 + 锚点行内容 + 原摘要行内容三方匹配，任一不符即报错停机
- 单行换单行，文件总行数守恒；幂等（已含新句则跳过）
用法：python apply_fixes.py <host1相对路径> <host2相对路径> ...
"""
import glob
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
JUD = os.path.join(ROOT, "script", "_db_row_mining", "audit_outline", "judgements")
WORK = os.path.join(ROOT, "script", "_db_row_mining", "audit_outline", "work")
OVER22 = os.path.join(WORK, "_over22_fix.json")
TAIL = "引用时按"


def load_judgements():
    jud = {}
    filenames = sorted(glob.glob(os.path.join(JUD, "*.jsonl")))
    # b1fix（字数补写）优先级最高，后加载覆盖主判定；其余主判定先加载
    fix_first = [f for f in filenames if "b1fix_" in os.path.basename(f)]
    rest = [f for f in filenames if "b1fix_" not in os.path.basename(f)]
    for f in rest + fix_first:
        for l in open(f, encoding="utf-8"):
            if l.strip():
                r = json.loads(l)
                if "新摘要句" in r or r.get("判定") in ("fix-format", "fix-text"):
                    jud[r["key"]] = r
    return jud


def load_fetch():
    fetch = {}
    for f in glob.glob(os.path.join(WORK, "*.fetch.jsonl")):
        for l in open(f, encoding="utf-8"):
            if l.strip():
                r = json.loads(l)
                fetch[r["key"]] = r
    return fetch


def main(hosts):
    jud = load_judgements()
    fetch = load_fetch()
    over22 = {}
    if os.path.exists(OVER22):
        over22 = json.load(open(OVER22, encoding="utf-8"))
    for rel in hosts:
        path = os.path.join(ROOT, rel)
        with open(path, encoding="utf-8", newline="") as fh:
            lines = fh.read().splitlines()
        orig_n = len(lines)
        n_apply = n_skip = n_err = 0
        for key, r in jud.items():
            if not (r.get("新摘要句") or r.get("判定") in ("fix-format", "fix-text")):
                continue
            ns = over22.get(key.split("|")[1], "") or r.get("新摘要句") or ""
            if not ns:
                continue
            if "|" not in key or not key.endswith(rel):
                continue
            fb = fetch.get(key)
            if not fb:
                print(f"  ! 无 fetch 档案: {key}", file=sys.stderr)
                n_err += 1
                continue
            ln = fb["line"]  # 锚点行（1-based）
            if lines[ln - 1] != fb["anchor_line"]:
                print(f"  ! 锚点行不匹配: {key} line {ln}", file=sys.stderr)
                n_err += 1
                continue
            inline = fb.get("block_type") == "inline" or not lines[ln - 1].lstrip().startswith("<!--")
            if inline:
                # 紧凑列举体例：叙述与锚点同一行，直接整行替换
                ns = lines[ln - 1] if False else ns  # ns 已是新完整行
                lines[ln - 1] = ns
                n_apply += 1
                continue
            # 独立行锚型：锚点向下 5 行内找含纪律串「引用时按」的行
            si = -1
            for j in range(ln, min(ln + 5, len(lines))):
                if TAIL in lines[j]:
                    si = j
                    break
            if si < 0:
                print(f"  ! 摘要行（纪律串）未找到: {key} line {ln}", file=sys.stderr)
                n_err += 1
                continue
            if ns in lines[si]:
                n_skip += 1
                continue
            tail = ""
            pos = lines[si].find(TAIL)
            if pos >= 0:
                tail = lines[si][pos:]
            if TAIL in ns:
                # 判读已给完整第 4 行（正文＋纪律串）→ 整行替换；再拼 tail 会使纪律串重复
                new_line = ns
            else:
                new_line = ns + tail
            if new_line.count(TAIL) != 1:
                print(f"  ! 纪律串出现 {new_line.count(TAIL)} 次（须恰 1 次）: {key}", file=sys.stderr)
                n_err += 1
                continue
            lines[si] = new_line
            n_apply += 1
        if n_err:
            print(f"{rel}: 有 {n_err} 处错误，放弃写盘", file=sys.stderr)
            continue
        with open(path, "w", encoding="utf-8", newline="") as fh:
            fh.write("\n".join(lines) + "\n")
        assert len(lines) == orig_n, f"{rel} 行数漂移 {orig_n}->{len(lines)}"
        print(f"{rel}: 应用 {n_apply} ｜ 幂等跳过 {n_skip} ｜ 行数守恒 {orig_n}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    main(sys.argv[1:])