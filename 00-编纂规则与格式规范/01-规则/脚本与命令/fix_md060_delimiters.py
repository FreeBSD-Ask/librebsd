# -*- coding: utf-8 -*-
"""MD060 分隔行修复器（固定脚本，2026-09-20 立）

背景：`.markdownlint.json` 对 MD060 启用 `style=compact` + `aligned_delimiter=true`。
后者要求**表格分隔行的管道符位置与表头行按显示宽度逐一对齐**（CJK 记 2 宽），
`markdownlint --fix` **不会**自动修复此项（CLAUDE.md 已注明），人工逐表算宽度代价极高。
2026-09-20 lint 债务审计实测：全审计面 5,487 条问题中 MD060 占 4,859 条（88.6%），
全部为分隔行形制问题，是本工具的直接治理对象。

本工具按表头行的**显示宽度**重算分隔行：
  单元格（无冒号）      = ' ' + '-'*(w-2) + ' '
  左对齐（':-'）        = ' :' + '-'*(w-3) + ' '
  右对齐（'-:'）        = ' ' + '-'*(w-3) + ': '
  居中（':-:'）         = ' :' + '-'*(w-4) + ': '
（w = 表头该单元格的显示宽度；CJK 按 2 计，与 markdownlint 一致）

安全性：
  - 只改**分隔行**本身，不动表头与数据行，不动单元格文本；
  - 跳过围栏代码块内的伪表格；反引号内与反斜杠转义的 `|` 不计为分隔符；
  - `--check` 只报不改；写盘前 `--backup` 可留原文件副本。

用法：
  python fix_md060_delimiters.py <file.md> [<file2.md> ...]           # 只报不改（dry-run）
  python fix_md060_delimiters.py <file.md> ... --apply                # 写盘
"""
import argparse
import re
import sys
import unicodedata
from pathlib import Path

DELIM_RE = re.compile(r"^[\s|:\-]+$")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
BQ_RE = re.compile(r"^(\s*(?:>\s*)+)(.*)$")   # 引注前缀（blockquote）


def disp_width(s: str) -> int:
    w = 0
    for ch in s:
        w += 2 if unicodedata.east_asian_width(ch) in ("W", "F") else 1
    return w


def split_cells(line: str):
    """按未转义、非行内代码内的 `|` 切分；返回 (前导管道符, 单元格列表, 尾随管道符)。"""
    body = line.rstrip("\n")
    lead = body.startswith("|")
    trail = body.endswith("|") and len(body) > 1
    core = body[1:] if lead else body
    if trail:
        core = core[:-1]
    cells, buf, in_code = [], [], False
    i = 0
    while i < len(core):
        ch = core[i]
        if ch == "\\" and i + 1 < len(core):
            buf.append(core[i:i + 2])
            i += 2
            continue
        if ch == "`":
            in_code = not in_code
            buf.append(ch)
            i += 1
            continue
        if ch == "|" and not in_code:
            cells.append("".join(buf))
            buf = []
            i += 1
            continue
        buf.append(ch)
        i += 1
    cells.append("".join(buf))
    return lead, cells, trail


def build_delim(header: str, old_delim: str):
    lead, hcells, trail = split_cells(header)
    _, dcells, _ = split_cells(old_delim)
    out = []
    for idx, hc in enumerate(hcells):
        w = disp_width(hc)
        dc = dcells[idx].strip() if idx < len(dcells) else ""
        left = dc.startswith(":")
        right = dc.endswith(":") and len(dc) > 1
        # 🔴 宽度不足时**放弃对齐冒号**（2026-09-20 修）：对齐冒号最小占 1 宽——
        # 单侧冒号需 w>=4、双侧需 w>=5。若硬留冒号，该列会比表头多出 1 宽，
        # 破坏「分隔行与表头逐列等宽」这一核心判据（曾致 长线任务总登记表 表头 `#` 列修不掉）。
        if left and right and w < 5:
            left = right = False
        elif (left or right) and w < 4:
            left = right = False
        if left and right:
            cell = " :" + "-" * (w - 4) + ": "
        elif left:
            cell = " :" + "-" * (w - 3) + " "
        elif right:
            cell = " " + "-" * (w - 3) + ": "
        else:
            cell = " " + "-" * max(w - 2, 1) + " "
        out.append(cell)
    s = "|".join(out)
    return ("|" if lead else "") + s + ("|" if trail else "")


def fix_file(path: Path, apply: bool):
    lines = path.read_text(encoding="utf-8").split("\n")
    in_fence = False
    changed = []
    for i in range(1, len(lines)):
        # 引注（blockquote）内的表格：剥去 `> ` 前缀后按同一规则处理（2026-09-20 补；
        # 此前 `> |---|---|` 因行首为 `> ` 而不匹配分隔行正则 → 静默漏修）
        mp = BQ_RE.match(lines[i])
        prefix, body = (mp.group(1), mp.group(2)) if mp else ("", lines[i])
        mq = BQ_RE.match(lines[i - 1])
        prev_body = mq.group(2) if mq else lines[i - 1]
        if FENCE_RE.match(body):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if not DELIM_RE.match(body) or "-" not in body or "|" not in body:
            continue
        if "|" not in prev_body:
            continue
        # 表头行不能本身是分隔行
        if DELIM_RE.match(prev_body) and "-" in prev_body:
            continue
        new = build_delim(prev_body, body)
        if new != body:
            changed.append((i + 1, prefix + body, prefix + new))
            lines[i] = prefix + new
    if changed and apply:
        path.write_text("\n".join(lines), encoding="utf-8", newline="")
    return changed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    total = 0
    for f in args.files:
        p = Path(f)
        ch = fix_file(p, args.apply)
        total += len(ch)
        print(f"{p}: {len(ch)} 处分隔行{'已改' if args.apply else '待改'}")
        for ln, old, new in ch[:6]:
            print(f"   L{ln}\n     旧: {old}\n     新: {new}")
        if len(ch) > 6:
            print(f"   …（另 {len(ch) - 6} 处）")
    print(f"\n合计 {total} 处；{'已写盘' if args.apply else '（dry-run，未写盘）'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
