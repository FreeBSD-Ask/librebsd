#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""audit_md_bold_spacing.py —— 第二十八件门禁：Markdown 加粗定界符外侧空格。

设立缘由（2026-10-21 主理人令）
------------------------------
加粗写作 `**文字**` 时，定界符外侧若紧贴汉字/字母，部分渲染器（严格 CommonMark
的 flanking 规则）不会把 `**` 识别为强调：`文字**加粗**文字` 两侧均失败，右侧
`**加粗**文字` 也失败。故立规：**第一个 `**` 前须有且只有一个半角空格（段落行首
例外），第二个 `**` 后有且只有一个半角空格（行尾例外）**；中文标点/符号紧邻豁免
（CommonMark 视 P*/S* 为合法边界，`**要点**：`、`（**内容**）` 不应被破坏）。

判据
----
T1 **左边界**：首 `**` 前为行首空白（段落开头例外）、恰好一个半角空格、或
   标点/符号（Unicode P*/S*，豁免）→ PASS；紧贴汉字/字母/数字或其他非标点字符
   → FAIL；多个空格、全角空格、TAB → FAIL（要求“有且只有一个半角空格”）。
T2 **右边界**：尾 `**` 后为行尾、恰好一个半角空格、或标点/符号 → PASS；紧贴
   非标点字符 → FAIL；多个空格/全角空格 → FAIL。

判据面与豁免
------------
- 只扫 `*.md`；默认根为 `05-新大纲/`（新大纲树）。`--root` 可指定子树，
  `--all` 扫全库并跳过本件豁免面。
- **原大纲豁免**：`05-卷册大纲/` 冻结，不在判据面（2026-10-21 主理人令）。
- **逐字保真档案豁免**：`04-现代研究文献/03-文献下载/**`（OCR 原文）。
- 不入库工作区一律跳过：顶层 `script/`、`_tmp/`、`specs/`、`.trae/`、
  `.zcode/`、`.workbuddy/`、`.workbuddy-ai/`、`review_logs/`。
- 围栏代码块（``` / ~~~）与行内代码段内的 `**` 不判。
- **畸形星号豁免**（与修复器 `_fix_bold_spacing.py` 同口径，避免“永远修不完
  的 FAIL”）：行内 `**` 计数为奇数、出现 `***`、内容含 `*`、含 `…` 或半角
  双引号、含“词> 空格”、以开括号结尾、ASCII 词内伪标记（`a**b**c`、
  `U**X`）均不作判据。这些形态属历史 OCR/跨对畸形，须另案人工处置。
  **完整引文除外**：以 `“”` 或 `""` 成对起止的引文（含引文内单星号斜体）
  属真加粗，纳入判据并只修外侧空格。

规则衔接
--------
- `写作规则.md`“加粗渲染边界规则（2026-10-21 立）”。
- `流程规则.md`“Markdown 加粗空格门禁（第二十八件）”。
- 修复器（一次性批处理）为 `script/_fix_bold_spacing.py`；本件只读，不写盘。

用法
----
    python audit_md_bold_spacing.py                 # 扫 05-新大纲（0=PASS/1=FAIL）
    python audit_md_bold_spacing.py --all           # 扫全库（豁免面见上）
    python audit_md_bold_spacing.py --root <目录>   # 限定子树
    python audit_md_bold_spacing.py --json
    python audit_md_bold_spacing.py --selftest      # 判据非空：负向夹具须 FAIL

依赖：仅标准库。
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
import unicodedata

sys.stdout.reconfigure(encoding="utf-8")

FENCE_RE = re.compile(r"^\s{0,3}(`{3,}|~{3,})")
INLINE_CODE_RE = re.compile(r"(`+)(?!`)(.+?)\1")
BOLD_RE = re.compile(r"(?<!\*)\*\*(?!\*)(.+?)(?<!\*)\*\*(?!\*)")

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
DEFAULT_ROOT = os.path.join(REPO, "05-新大纲")

SKIP_DIRS = {
    ".git", "node_modules", ".venv", "__pycache__", ".workbuddy", ".workbuddy-ai",
    ".trae", ".zcode", ".github", ".gitbook", "_tmp", "specs", "review_logs",
}
SKIP_TOPLEVEL_ONLY = {"script"}
# --all 时的额外豁免面（按相对仓库根的前缀）
ALL_EXEMPT_PREFIXES = (
    "05-卷册大纲/",                       # 原大纲冻结（2026-10-21 主理人令）
    "04-现代研究文献/03-文献下载/",       # OCR 逐字保真档案
)


def is_punct_or_symbol(ch: str) -> bool:
    return unicodedata.category(ch)[0] in ("P", "S")


def is_ascii_word(ch: str) -> bool:
    return ch.isascii() and (ch.isalnum() or ch == "_")


def mask_inline_code(line: str) -> str:
    return INLINE_CODE_RE.sub(lambda m: "\x00" * len(m.group(0)), line)


def skip_span(inner: str, pre_ch: str, post_ch: str, line: str, s: int, e: int) -> bool:
    """与修复器同口径的畸形星号豁免；完整引文（含单星号斜体）不豁免。"""
    is_full_quote = ((inner.startswith("\u201c") and inner.endswith("\u201d"))
                     or (inner.startswith('"') and inner.endswith('"')))
    if "*" in inner and not (is_full_quote and "**" not in inner):
        return True
    if s >= 2 and line[s - 2:s] == "**":
        return True
    if line[e:e + 2] == "**":
        return True
    if re.search(r">[ \u4e00-\u9fff]", inner):
        return True
    if ("\u2026" in inner or '"' in inner) and not is_full_quote:
        return True
    if inner[-1] in "（([【《{<":
        return True
    opener_ok = (s == 0 or line[:s].strip() == "" or
                 (pre_ch and (pre_ch.isspace() or is_punct_or_symbol(pre_ch))))
    if (not opener_ok and pre_ch and pre_ch.isascii() and is_ascii_word(pre_ch)
            and inner and inner[0].isascii() and is_ascii_word(inner[0])):
        return True
    if not opener_ok and inner and is_punct_or_symbol(inner[0]) and not is_full_quote:
        return True
    if (pre_ch and post_ch and is_ascii_word(pre_ch) and is_ascii_word(post_ch)
            and inner and re.fullmatch(r"[A-Za-z0-9_]+", inner)):
        return True
    return False


def check_line(line: str):
    """返回违规列表 [(kind, snippet)]。"""
    masked = mask_inline_code(line)
    n_star = masked.count("**")
    if n_star == 0 or n_star % 2 == 1 or "***" in masked:
        return []
    out = []
    for m in BOLD_RE.finditer(masked):
        inner = m.group(1)
        if not inner.strip() or inner.strip("*") == "":
            continue
        if inner[0].isspace() or inner[-1].isspace():
            continue
        s, e = m.start(), m.end()
        pre_ch = line[s - 1] if s > 0 else ""
        post_ch = line[e] if e < len(line) else ""
        if skip_span(inner, pre_ch, post_ch, line, s, e):
            continue
        snippet = line[max(0, s - 30):e + 30]
        # T1 左边界
        if s > 0 and line[:s].strip() != "":
            if pre_ch.isspace():
                j = s
                while j > 0 and line[j - 1].isspace():
                    j -= 1
                if line[j:s] != " ":
                    out.append(("left_multi_space", snippet))
            elif not is_punct_or_symbol(pre_ch):
                out.append(("left_missing_space", snippet))
        # T2 右边界（行尾空白不属本件，交 MD009）
        if e < len(line):
            if post_ch.isspace():
                k = e
                while k < len(line) and line[k].isspace():
                    k += 1
                if k < len(line) and line[e:k] != " ":
                    out.append(("right_multi_space", snippet))
            elif not is_punct_or_symbol(post_ch):
                out.append(("right_missing_space", snippet))
    return out


def iter_md(root: str):
    root_abs = os.path.abspath(root)
    for dirpath, dirnames, filenames in os.walk(root):
        top = os.path.abspath(dirpath) == root_abs
        skip = SKIP_DIRS if not top else SKIP_DIRS | SKIP_TOPLEVEL_ONLY
        dirnames[:] = [d for d in dirnames if d not in skip]
        for fn in filenames:
            if fn.lower().endswith(".md"):
                yield os.path.join(dirpath, fn)


def scan(root: str, all_mode: bool = False):
    bad_files = 0
    bad_items = 0
    files = 0
    samples = []
    kinds = {}
    for p in iter_md(root):
        rel = os.path.relpath(p, root)
        if all_mode and any(rel.replace(os.sep, "/").startswith(pre) for pre in ALL_EXEMPT_PREFIXES):
            continue
        files += 1
        try:
            text = open(p, "rb").read().decode("utf-8-sig")
        except (OSError, UnicodeDecodeError):
            continue
        in_fence = False
        fence_char = ""
        file_bad = 0
        for line_no, line in enumerate(text.replace("\r\n", "\n").replace("\r", "\n").split("\n"), 1):
            m = FENCE_RE.match(line)
            if m:
                mark = m.group(1)
                if not in_fence:
                    in_fence = True
                    fence_char = mark[0]
                elif mark[0] == fence_char:
                    in_fence = False
                continue
            if in_fence:
                continue
            for kind, snip in check_line(line):
                file_bad += 1
                kinds[kind] = kinds.get(kind, 0) + 1
                if len(samples) < 60:
                    samples.append({"file": rel, "line": line_no, "kind": kind, "snippet": snip})
        if file_bad:
            bad_files += 1
            bad_items += file_bad
    return files, bad_files, bad_items, kinds, samples


def selftest() -> int:
    with tempfile.TemporaryDirectory() as td:
        good = os.path.join(td, "good.md")
        bad = os.path.join(td, "bad.md")
        code = os.path.join(td, "code.md")
        with open(good, "w", encoding="utf-8", newline="\n") as fh:
            fh.write("**段落开头** 与文字\n")
            fh.write("中文 **加粗** 中文\n")
            fh.write("中文 **要点**：标点豁免\n")
            fh.write("中文 **加粗**（括号豁免）\n")
            fh.write("中文 **加粗**，逗号豁免\n")
            fh.write("路径 `**代码**` 不判\n")
            fh.write("幂运算 a**b**c 不判\n")
        with open(bad, "w", encoding="utf-8", newline="\n") as fh:
            fh.write("中文**缺左空格**\n")
            fh.write("中文 **缺右空格**中文\n")
            fh.write("中文  **多空格**  中文\n")
        with open(code, "w", encoding="utf-8", newline="\n") as fh:
            fh.write("```\n中文**代码块内**不判\n```\n")
            fh.write("行内 `中文**代码**` 不判\n")
        files, bf, bi, kinds, _ = scan(td)
        assert files == 3, files
        assert bf == 1, (bf, kinds)
        # bad.md：左缺 1、右缺 1、多空格左右各 1
        assert bi == 4, (bi, kinds)
        assert kinds.get("left_missing_space") == 1, kinds
        assert kinds.get("right_missing_space") == 1, kinds
        assert kinds.get("left_multi_space") == 1, kinds
        assert kinds.get("right_multi_space") == 1, kinds
        # 负向自证：删坏夹具后须 PASS
        os.remove(bad)
        files, bf, bi, kinds, _ = scan(td)
        assert bf == 0 and bi == 0, (bf, bi, kinds)
    print("selftest PASS（正例 7 项、负例 4 项命中、代码/伪标记豁免、删除坏夹具后归零）")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=None)
    ap.add_argument("--all", action="store_true", help="扫全库（豁免原大纲与 OCR 档案）")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    root = args.root or (REPO if args.all else DEFAULT_ROOT)
    files, bf, bi, kinds, samples = scan(root, all_mode=args.all)
    ok = bi == 0
    summary = {
        "gate": "第二十八件 audit_md_bold_spacing",
        "root": root,
        "md_files": files,
        "bad_files": bf,
        "bad_items": bi,
        "kinds": kinds,
        "samples": samples,
        "rule": "首 ** 前恰好一个半角空格（段落行首例外）；尾 ** 后恰好一个半角空格"
                "（行尾例外）；P*/S* 标点符号紧邻豁免",
        "exempt": "--all 时豁免 05-卷册大纲/（原大纲冻结）与 "
                  "04-现代研究文献/03-文献下载/（OCR 逐字保真）",
    }
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=1))
    else:
        print(f"root={root}")
        print(f"扫描 .md {files} 个")
        print(f"加粗空格违规：{bi} 处 / {bf} 文件 -> {'PASS' if ok else 'FAIL'}")
        for kind, n in sorted(kinds.items()):
            print(f"  {kind}={n}")
        for s in samples[:30]:
            print(f"  FAIL {s['file']}:{s['line']} [{s['kind']}] {s['snippet']}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
