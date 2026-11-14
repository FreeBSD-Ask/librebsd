"""条文用语门禁（第四十五件，2026-11-15 立）。

依据：GB/T 1.1-2020 附录 C 能愿动词四档（应／不应、宜／不宜、可／不必、能／不能）与
`流程规则/11-治理与体例裁定.md` §二“条文用语（能愿动词）规则”。
判据：规则语料的要求型正文不应使用停用词 必须／不得／严禁／务必／禁止（应改 应／不应）。

适用范围（与 11 §三 同）：`AGENTS.md`、`01-规则/**/*.md`、`02-操作手册/**/*.md`。

豁免面（结构名与逐字面，11 §三“结构名豁免”）：
  · 标题行（`#` 开头）——规则名与章题属结构名
  · 表格中首列或单元格恰为停用词的映射行（11 §二 停用词表本身）
  · 行内代码、弯引号、书名号、直角引号内的字面
  · 加粗标签（`**…**`）——标签名与红线短语
  · 无标点的裸列表项（规则名／目录项）

用法：
    python audit_rule_modality.py --diff [<rev>]   # 只查相对 <rev>（默认 HEAD）的新增行
    python audit_rule_modality.py --all            # 全量扫适用范围
    python audit_rule_modality.py --selftest
退出码：0 通过／1 有 FAIL／2 依赖或环境错误。
"""
from __future__ import annotations

import argparse
import pathlib
import re
import subprocess
import sys
import tempfile

STOP = ("必须", "不得", "严禁", "务必", "禁止")
STOP_RE = re.compile("|".join(STOP))
MASK_RES = [
    re.compile(r"`[^`]*`"),
    re.compile(r"“[^”]*”"),
    re.compile(r"《[^》]*》"),
    re.compile(r"「[^」]*」"),
    re.compile(r"『[^』]*』"),
    re.compile(r"\*\*[^*]*\*\*"),
]
BARE_ITEM = re.compile(r"^\s*[-*+]\s+[^，。；：、！？（）()“”]{2,30}$")
SCOPE = ("AGENTS.md", "00-编纂规则与格式规范/01-规则", "00-编纂规则与格式规范/02-操作手册")


def mask(line: str) -> str:
    for rx in MASK_RES:
        line = rx.sub("", line)
    return line


DISPOSAL = ("历史", "现行", "既成", "已废止")


def violation(line: str) -> str | None:
    s = line.lstrip()
    if s.startswith("#") or s.startswith(">"):
        return None
    if any(k in line for k in DISPOSAL):
        return None  # 追溯性叙述（历史记录、现行状态说明）不属要求型条文
    if BARE_ITEM.match(line):
        return None
    if line.lstrip().startswith("|"):
        return None  # 表格行：规则名、目录项与停用词映射表，属结构名面
    m = STOP_RE.search(mask(line))
    return m.group(0) if m else None


def scan_text(path: str, text: str) -> list[tuple[int, str, str]]:
    out = []
    for i, line in enumerate(text.split("\n"), 1):
        w = violation(line)
        if w:
            out.append((i, w, line.strip()[:100]))
    return out


def scope_files(root: pathlib.Path) -> list[pathlib.Path]:
    files = []
    for t in SCOPE:
        p = root / t
        if p.is_file():
            files.append(p)
        elif p.exists():
            files.extend(sorted(p.rglob("*.md")))
    return files


def run_all(root: pathlib.Path) -> int:
    bad = []
    for f in scope_files(root):
        try:
            text = f.read_text(encoding="utf-8")
        except Exception:
            continue
        for line, w, ctx in scan_text(str(f), text):
            bad.append((f.relative_to(root).as_posix(), line, w, ctx))
    print("条文用语门禁（第四十五件，全量巡检；只报不判）")
    print("=" * 60)
    print(f"扫描 {len(scope_files(root))} 件；提示 {len(bad)} 条（--all 不作 FAIL，判据以 --diff 新增行为准）")
    for p, line, w, ctx in bad[:80]:
        print(f"  [{w}] {p}:{line} → {ctx}")
    return 0


def run_diff(root: pathlib.Path, rev: str) -> int:
    r = subprocess.run(
        ["git", "diff", "-U0", rev, "--"] + [t for t in SCOPE], cwd=str(root),
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    if r.returncode != 0:
        print(r.stderr.strip(), file=sys.stderr)
        return 2
    cur, bad = None, []
    for line in r.stdout.split("\n"):
        if line.startswith("+++ b/"):
            cur = line[6:]
            continue
        if cur is not None and (not cur.endswith(".md") or cur.startswith("00-编纂规则与格式规范/01-规则/脚本与命令/")):
            continue
        if line.startswith("+") and not line.startswith("+++"):
            body = line[1:]
            w = violation(body)
            if w:
                bad.append((cur, w, body.strip()[:100]))
    print("条文用语门禁（第四十五件，diff 模式）")
    print("=" * 60)
    print(f"相对 {rev} 的新增行：FAIL {len(bad)} 条")
    for p, w, ctx in bad[:80]:
        print(f"  [{w}] {p} → {ctx}")
    return 0 if not bad else 1


def selftest() -> int:
    ok = True
    cases = [
        ("复核时应同时参照两份大纲，不得跳过。", "不得", True),
        ("### 何时必须写 ADR", None, False),
        ("| 必须 | 应 | 引文、标准原文、书名与法规名称 |", None, False),
        ("改用 `必须` 以外的写法。", None, False),
        ("“必须”二字按引文原样保留。", None, False),
        ("- 根目录禁止生成新路径规则", None, False),
        ("- **禁止事项**：不应手改装配产物。", None, False),
        ("本节要求：每一批必须留痕。", "必须", True),
    ]
    for text, expect, should in cases:
        got = violation(text)
        good = (got == expect) if should else (got is None)
        if not good:
            print(f"[selftest] FAIL：{text!r} 期望 {expect!r}，实得 {got!r}")
            ok = False
    with tempfile.TemporaryDirectory() as td:
        root = pathlib.Path(td)
        (root / "00-编纂规则与格式规范/01-规则").mkdir(parents=True)
        f = root / "00-编纂规则与格式规范/01-规则/x.md"
        f.write_text("# 标题必须\n\n正文：不得跳过。\n", encoding="utf-8", newline="\n")
        hits = scan_text(str(f), f.read_text(encoding="utf-8"))
        if [h[1] for h in hits] != ["不得"]:
            print(f"[selftest] FAIL：文件级扫描结果 {hits}")
            ok = False
    print("[selftest] PASS" if ok else "[selftest] FAIL")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=None)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--diff", nargs="?", const="HEAD", default=None)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    root = pathlib.Path(a.root).resolve() if a.root else pathlib.Path(__file__).resolve().parents[3]
    if a.diff is not None:
        return run_diff(root, a.diff)
    return run_all(root)


if __name__ == "__main__":
    sys.exit(main())
