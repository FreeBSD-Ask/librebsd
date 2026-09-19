#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""文档格式门禁（markdownlint）——2026-09-20 立

设立缘由
--------
`CLAUDE.md` 的「Lint 配置」章节长期把 `markdownlint-cli2` 列为本地 lint 工具并给出
运行命令，但**门禁套件中无一件调用它** → lint 缺陷无人自动发现，静默累积
（2026-09-20 实测：审计面内 89 文件 5,487 条）。教训：**「工具已文档化」≠「工具已生效」**。

对象面（闸面＝活动文件，显式清单）
--------------------------------
1. `CLAUDE.md`（协作指南）
2. `00-编纂规则与格式规范/01-规则/*.md`（**现行规则全部在效**）
3. `00-编纂规则与格式规范/01-规则/脚本与命令/*.md`
4. `08-核查报告与多轮复核/重构2026/7[0-9]-*.md`（现行号文执行记录）
5. `08-核查报告与多轮复核/重构2026/tests/*.md`（现行测试夹具文档）
6. `08-核查报告与多轮复核/12-重构大纲书目述评/index.md`（现行外迁目录索引）

**豁免**（不属闸面，理由见 CLAUDE.md「Lint 配置」）：
- `01-项目管理/**` 历史规划与报告归档（一次性产物，已冻结）；
- `08-核查报告与多轮复核/重构2026/` 下 70 号以前的**历史规划/映射/审计类文档**
  （一次性分析产物，对应既有「历史快照豁免」概念）；
- `08-核查报告与多轮复核/12-重构大纲书目述评/第*-章级书目述评.md`（逐字保真档案）；
- `00-编纂规则与格式规范/01-规则/script/**`（脚本运行日志）。

退出码
------
0 = 闸面 0 问题；1 = 有 lint 问题或闸面失效；2 = 依赖缺失或版本不符。

版本钉定
--------
实测 v0.23.2 与 v0.22.1 对同一语料给出**不同计数**（5,487 条为 v0.23.2 与 v0.22.1
一致值，但历史上 `npx --yes` 曾拉到新版产生漂移）。为保证可复现，本门禁钉定
`markdownlint-cli2 0.22.1 / markdownlint 0.40.0`；升级须显式 `--allow-version`。

用法
----
    python audit_markdown_lint.py            # 跑闸面（0 问题 exit 0）
    python audit_markdown_lint.py --list     # 只打印闸面清单
    python audit_markdown_lint.py --all      # 全审计面（含豁免件）统计，仅供可见性
    python audit_markdown_lint.py --allow-version
"""
import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

PINNED = ("0.22.1", "0.40.0")  # markdownlint-cli2 / markdownlint

MANIFEST = [
    "CLAUDE.md",
    "00-编纂规则与格式规范/01-规则/*.md",
    "00-编纂规则与格式规范/01-规则/脚本与命令/*.md",
    "08-核查报告与多轮复核/重构2026/7[0-9]-*.md",
    "08-核查报告与多轮复核/重构2026/tests/*.md",
    "08-核查报告与多轮复核/12-重构大纲书目述评/index.md",
]

# 全审计面（--all 用，含豁免件）：口径同 2026-09-20 lint 债务审计
AUDIT_SCOPE = [
    "08-核查报告与多轮复核/重构2026/**/*.md",
    "08-核查报告与多轮复核/12-重构大纲书目述评/index.md",
    "00-编纂规则与格式规范/01-规则/*.md",
    "01-项目管理/**/*.md",
    "CLAUDE.md",
    "spec/*.md",
]

SUMMARY_RE = re.compile(r"Summary: (\d+) error")


def find_bin():
    exe = shutil.which("markdownlint-cli2")
    if exe:
        return exe
    return None


def version_of(exe):
    out = subprocess.run([exe, "--version"], capture_output=True, text=True,
                         cwd=str(ROOT))
    text = (out.stdout or "") + (out.stderr or "")
    m = re.search(r"markdownlint-cli2 v([\d.]+) \(markdownlint v([\d.]+)\)", text)
    if not m:
        return None
    return m.group(1), m.group(2)


def resolve(patterns):
    """展开 glob；返回 (文件列表, 零匹配的模式列表)。"""
    files, empty = [], []
    for pat in patterns:
        hits = sorted(p.relative_to(ROOT).as_posix()
                      for p in ROOT.glob(pat) if p.is_file())
        if not hits:
            empty.append(pat)
        files.extend(hits)
    # 去重且保序
    seen, uniq = set(), []
    for f in files:
        if f not in seen:
            seen.add(f)
            uniq.append(f)
    return uniq, empty


def run_lint(exe, files):
    cmd = [exe] + files + ["--config", ".markdownlint.json"]
    out = subprocess.run(cmd, capture_output=True, text=True, cwd=str(ROOT),
                         encoding="utf-8", errors="replace")
    text = (out.stdout or "") + (out.stderr or "")
    m = SUMMARY_RE.search(text)
    return (int(m.group(1)) if m else None), text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true", help="只打印闸面清单")
    ap.add_argument("--all", action="store_true", help="全审计面统计（仅可见性，恒 exit 0）")
    ap.add_argument("--allow-version", action="store_true", help="允许非钉定版本")
    args = ap.parse_args()

    if args.list:
        print("闸面清单（活动文件）：")
        for pat in MANIFEST:
            hits, _ = resolve([pat])
            print(f"  {pat}   → {len(hits)} 文件")
            for h in hits:
                print(f"      {h}")
        return 0

    exe = find_bin()
    if not exe:
        print("[exit 2] 未找到 markdownlint-cli2；请安装（npm i -g markdownlint-cli2）", file=sys.stderr)
        return 2
    ver = version_of(exe)
    if ver is None:
        print("[exit 2] 无法解析 markdownlint-cli2 版本", file=sys.stderr)
        return 2
    print(f"markdownlint-cli2 v{ver[0]} (markdownlint v{ver[1]})")
    if ver != PINNED and not args.allow_version:
        print(f"[exit 2] 版本不符：钉定 {PINNED[0]}/{PINNED[1]}，实测 {ver[0]}/{ver[1]}。"
              f"计数随版本漂移，须显式 --allow-version 方可继续。", file=sys.stderr)
        return 2

    patterns = AUDIT_SCOPE if args.all else MANIFEST
    files, empty = resolve(patterns)
    label = "全审计面（含豁免件）" if args.all else "闸面"
    print(f"{label}：{len(files)} 文件")
    if empty:
        print(f"[exit 1] 以下模式零匹配（闸面可能已失效）：{empty}", file=sys.stderr)
        return 1

    total, text = run_lint(exe, files)
    if total is None:
        print("[exit 1] 无法解析 lint 输出；原始输出前 20 行：", file=sys.stderr)
        print("\n".join(text.splitlines()[:20]), file=sys.stderr)
        return 1

    print(f"Summary: {total} error(s)")
    if args.all:
        for line in text.splitlines():
            if " error " in line:
                print(line)
        return 0

    if total == 0:
        print("PASS：闸面 0 问题")
        return 0
    for line in text.splitlines():
        if " error " in line:
            print(line)
    print(f"FAIL：闸面 {total} 条 lint 问题")
    return 1


if __name__ == "__main__":
    sys.exit(main())
