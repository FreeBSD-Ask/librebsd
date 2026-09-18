#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""三工具文字格式校验最小可执行入口（仅报告模式）。

依据：
- 流程规则.md“AutoCorrect 调用规范”“三轮完整执行规则”小节
- 脚本与命令/autocorrect-mdpadding-markdownlint-清理工具.md 已记载命令

对指定的改动 Markdown 文件依次执行三个工具的只读检查，汇总输出
违规/建议清单，供人工逐条复核：
1. AutoCorrect        — autocorrect --lint --file <f>（不修复、不写回）
2. md-padding@latest  — npx md-padding@latest <f>（不带 --write，仅打印
                         到标准输出），与原文差异以 diff 形式列为建议
3. markdownlint2      — markdownlint2 -c .markdownlint.json <f>（仅检查）

约束（与“约束”小节一致，不得绕过）：
- 禁止批量接受：输出建议一律不得批量接受，须逐条审阅
- 禁止默认接受：不得以工具输出为最终结果，须经人工判断
- 逐条人工复核：每条建议须结合上下文综合判断，特别注意行间代码、
  代码块、命令、路径是否被误改
- 本入口不调用 --fix / --write，不修改任何目标文件，仅产出清单

用法：
    python 00-编纂规则与格式规范/01-规则/脚本与命令/check_format_three_tools.py <file.md> [<file2.md> ...]
    python .../check_format_three_tools.py --git-changed
    python .../check_format_three_tools.py <file.md> --report <report.md>

退出码：0 = 三工具均无违规/建议；1 = 存在违规/建议待人工复核；
        2 = 用法或执行错误。
"""
import argparse
import difflib
import json
import shutil
import subprocess
import sys
from pathlib import Path

# 项目根目录：自本文件向上查找含 .git 的祖先目录
_HERE = Path(__file__).resolve()
PROJECT_ROOT = next(
    (p for p in [_HERE.parent, *_HERE.parents] if (p / ".git").exists()),
    _HERE.parents[3],
)
MARKDOWNLINT_CONFIG = PROJECT_ROOT / ".markdownlint.json"

BANNER = (
    "提醒：本清单仅为报告，禁止批量接受、禁止默认接受任何工具建议；"
    "每条建议须逐条人工复核，行间代码与代码块内容被建议修改时一律拒绝。"
)


def resolve_cmd(cmd):
    """解析命令为可执行形式。

    返回 (argv_or_str, use_shell)：Windows 下 npm 工具为 .CMD/.ps1 shim，
    须经 cmd.exe 调用（shell=True，由 list2cmdline 处理引号）。
    """
    exe = shutil.which(cmd[0])
    if exe is None:
        return None, False
    if sys.platform == "win32" and exe.lower().endswith((".cmd", ".bat", ".ps1")):
        # .ps1 shim 无对应 .cmd 时无法经 cmd.exe 调用，视为不可用
        if exe.lower().endswith(".ps1"):
            base = exe[:-4] + ".cmd"
            if not Path(base).exists():
                return None, False
            exe = base
        return [exe, *cmd[1:]], True
    return [exe, *cmd[1:]], False


def run_cmd(cmd):
    """执行外部命令，返回 (returncode, stdout, stderr)；命令不存在返回 None。"""
    resolved, use_shell = resolve_cmd(cmd)
    if resolved is None:
        return None
    try:
        proc = subprocess.run(
            resolved, capture_output=True, text=True, encoding="utf-8", errors="replace",
            cwd=str(PROJECT_ROOT), shell=use_shell,
        )
    except (FileNotFoundError, OSError):
        return None
    return proc.returncode, proc.stdout, proc.stderr


def check_autocorrect(path):
    """AutoCorrect：--lint 仅报告不修复。返回建议条目列表。"""
    if shutil.which("autocorrect") is None:
        return None, "autocorrect 未安装或不在 PATH，跳过（请人工执行）"
    result = run_cmd(["autocorrect", "--lint", "--format=json", str(path)])
    if result is None:
        return None, "autocorrect 调用失败"
    code, out, err = result
    items = []
    parsed = None
    try:
        parsed = json.loads(out)
    except (json.JSONDecodeError, ValueError):
        parsed = None
    if isinstance(parsed, dict):
        # JSON 结构容错：逐层查找含 error 条目的文件记录
        file_records = parsed.get("fileReports") or parsed.get("files") or []
        if not file_records and parsed.get("errors"):
            file_records = [parsed]
        for rec in file_records:
            for e in rec.get("errors") or []:
                line = e.get("line", "?")
                col = e.get("col", "?")
                rule = e.get("rule") or e.get("name") or ""
                msg = e.get("message") or ""
                items.append(f"[AutoCorrect] {path}:{line}:{col} 规则 {rule} — {msg}")
    else:
        # 回退：按文本输出逐行收录非空行
        for ln in out.splitlines():
            if ln.strip():
                items.append(f"[AutoCorrect] {ln.strip()}")
    if not items and code != 0:
        # JSON 解析正常且无条目时，非零退出码（如 --strict 告警）不构成违规
        if not (isinstance(parsed, (dict, list))):
            items.append(f"[AutoCorrect] 退出码 {code}，原始输出见下；stderr: {err.strip()[:200]}")
            for ln in out.splitlines()[:50]:
                if ln.strip():
                    items.append(f"[AutoCorrect] {ln.strip()}")
    return items, None


def check_md_padding(path):
    """md-padding：不带 --write，仅比较标准输出与原文，差异列为建议。"""
    if shutil.which("npx") is None:
        return None, "npx 未安装或不在 PATH，跳过（请人工执行）"
    result = run_cmd(["npx", "--yes", "md-padding@latest", str(path)])
    if result is None:
        return None, "npx md-padding@latest 调用失败"
    code, out, err = result
    if code != 0:
        return [f"[md-padding] 执行失败（退出码 {code}）：{err.strip()[:200]}"], None
    original = path.read_text(encoding="utf-8", errors="replace")
    if out.rstrip("\n") == original.rstrip("\n"):
        return [], None
    items = [f"[md-padding] {path}：建议添加中英文/数字间距（未写回，仅报告）"]
    diff = difflib.unified_diff(
        original.splitlines(), out.splitlines(),
        fromfile=f"{path.name}（原文）", tofile=f"{path.name}（md-padding 建议，勿直接采纳）",
        lineterm="",
    )
    items.extend(f"[md-padding] {ln}" for ln in list(diff)[:80])
    return items, None


def check_markdownlint2(path):
    """markdownlint2：按项目根目录 .markdownlint.json 检查，输出违规行。

    优先规则记载的 `markdownlint2`；本机未安装时回退等价的
    `markdownlint-cli2`（同配置文件、同规则集，仅二进制名不同）。
    """
    rel = str(path)
    if shutil.which("markdownlint2") is not None:
        cmd = ["markdownlint2"]
        if MARKDOWNLINT_CONFIG.exists():
            cmd += ["-c", str(MARKDOWNLINT_CONFIG)]
        cmd.append(rel)
    elif shutil.which("markdownlint-cli2") is not None:
        # markdownlint-cli2 自动读取根目录 .markdownlint.json 等配置
        cmd = ["markdownlint-cli2", rel]
    else:
        return None, ("markdownlint2 与 markdownlint-cli2 均未安装或不在 PATH"
                      "（npm i -g markdownlint-cli2 后重试），请人工执行")
    result = run_cmd(cmd)
    if result is None:
        return None, "markdownlint2 调用失败"
    code, out, err = result
    items = []
    for ln in (out or err).splitlines():
        ln = ln.strip()
        if not ln:
            continue
        # 过滤 markdownlint-cli2 的信息性输出，仅保留违规行与错误信息
        if ln.startswith(("markdownlint-cli2 v", "Finding:", "Linting:", "Summary:")):
            continue
        items.append(f"[markdownlint2] {ln}")
    if not items and code != 0:
        items.append(f"[markdownlint2] 退出码 {code}，无可解析输出")
    return items, None


def collect_git_changed_md():
    """收集 git 工作区与暂存区中改动的 .md 文件。"""
    result = run_cmd(["git", "status", "--porcelain"])
    if result is None or result[0] != 0:
        return []
    files = []
    for ln in result[1].splitlines():
        if len(ln) < 4 or not ln[3:].strip().endswith(".md"):
            continue
        rel = ln[3:].strip().strip('"')
        if " -> " in rel:  # 重命名取新路径
            rel = rel.split(" -> ")[-1]
        p = PROJECT_ROOT / rel
        if p.is_file():
            files.append(p)
    return files


def main():
    parser = argparse.ArgumentParser(
        description="三工具（AutoCorrect / md-padding@latest / markdownlint2）"
                    "格式校验报告入口——仅输出清单，禁止批量/默认接受",
    )
    parser.add_argument("files", nargs="*", help="待检查的 Markdown 文件路径")
    parser.add_argument("--git-changed", action="store_true",
                        help="自动选取 git 工作区中改动的 .md 文件")
    parser.add_argument("--report", metavar="PATH",
                        help="将清单另存为 Markdown 报告文件（清单本身仍打印到标准输出）")
    args = parser.parse_args()

    targets = [Path(f).resolve() for f in args.files]
    if args.git_changed:
        targets.extend(collect_git_changed_md())
    # 去重并保持顺序
    seen, ordered = set(), []
    for t in targets:
        if t not in seen:
            seen.add(t)
            ordered.append(t)
    if not ordered:
        parser.error("未指定文件：请给出 .md 文件路径或使用 --git-changed")

    missing = [t for t in ordered if not t.is_file()]
    if missing:
        for t in missing:
            print(f"错误：文件不存在：{t}", file=sys.stderr)
        return 2

    all_items, skips = [], []
    print(BANNER)
    print()
    for t in ordered:
        print(f"== 检查文件：{t} ==")
        for name, fn in (("AutoCorrect", check_autocorrect),
                         ("md-padding@latest", check_md_padding),
                         ("markdownlint2", check_markdownlint2)):
            items, skip_reason = fn(t)
            if items is None:
                skips.append(f"{name}（{t.name}）：{skip_reason}")
                print(f"-- {name}：跳过（{skip_reason}）")
                continue
            if not items:
                print(f"-- {name}：无违规/建议")
                continue
            for it in items:
                print(it)
            all_items.extend(items)
        print()

    print("== 汇总 ==")
    print(f"违规/建议合计：{len(all_items)} 条（待逐条人工复核）")
    for s in skips:
        print(f"跳过：{s}")
    print()
    print(BANNER)

    if args.report:
        report = Path(args.report).resolve()
        report.parent.mkdir(parents=True, exist_ok=True)
        lines = ["# 三工具格式校验报告（仅报告模式）", "", BANNER, ""]
        lines += [f"- 违规/建议合计：{len(all_items)} 条", ""]
        lines += ["## 清单", ""]
        lines += [f"- {it}" for it in all_items] or ["- （无）"]
        if skips:
            lines += ["", "## 跳过项", ""]
            lines += [f"- {s}" for s in skips]
        report.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
        print(f"报告已写入：{report}")

    return 1 if all_items else 0


if __name__ == "__main__":
    sys.exit(main())
