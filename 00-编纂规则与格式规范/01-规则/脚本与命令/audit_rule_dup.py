# -*- coding: utf-8 -*-
"""audit_rule_dup.py —— 第四十二件门禁：规则语料单一落点与去重。

设立缘由（2026-11-06，ykla“全量复核＋建立去重机制”令）
----------------------------------------------------
规则语料实测缺陷四类：①`01-规则/` 内 4 处相对链接停留在 2026-10-27 目录化前的扁平层级
（幻影指向）；②`08-ai逐章生成操作流程.md` 与 `09-材料、文献与入库.md` 整行复制“看板文件”
定义（同实两名，改一处漏一处）；③`流程规则/00-索引.md` 名单表 65 行仅 11 键（已由第二十九件
E7b 收口，本件不重复管辖）；④跨文件同题 H2 经实测均为泛名／平行体例，无同实重复。
哲学依据：`13-软件工程/09-reflection-generalization.md` §2.11“单一形式落点（引用不复制）”
——同一事实只允许一个形式落点，其余位置以引用指回；幻影链接即语料断言不存在之物。

对象
----
- `00-编纂规则与格式规范/01-规则/**/*.md`
- `AGENTS.md`
- `13-软件工程/*.md`（顶层）

判据
----
R1 幻影相对链接：剥围栏代码块与行内代码后，`](相对路径.md)` 指向的目标必须存在
   （2026-10-27 目录化将分册移入子目录而链接未随层级更新，是本判据的直接成因）。
R2 跨文件长行复制：剥围栏后规范化（空白归一）长度 ≥60 字符的非表格行，同一文本出现于
   ≥2 文件即 FAIL。白名单（唯一实现，须注明理由）：`> 本件为《流程规则》分册` 体例页眉。
   阈值 60 的实测依据：操作手册模板共享占位行与“→”指针行均 <60，真实规则复制行 ≥70。
R3 同文件同表重复数据行：跳过各表首行（表头）与分隔行后，规范化逐字节相同者 FAIL
   （多表同构的表头重复合法——2026-11-06 实测 8 组全部属此类，故只看数据行）。
R4 同文件同父节重复标题：同一标题文本挂在同一父标题下出现 ≥2 次即 FAIL
   （跨文件同题与不同父节的泛名同题——如“适用场景”——实测均为合法体例，不在判据面）。

用法
----
    python audit_rule_dup.py            # 0 通过 / 1 不通过
    python audit_rule_dup.py --selftest # 判据非空自检（正样本 + 四类负向夹具）
    python audit_rule_dup.py --list     # 打印检查对象

退出码：0＝无 FAIL；1＝有 FAIL；2＝致命（范围目录缺失）。
依赖：仅标准库。
"""

import argparse
import pathlib
import re
import shutil
import sys
import tempfile
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8")

REPO = pathlib.Path(__file__).resolve().parents[3]
WL_PREFIXES = (
    "> 本件为《流程规则》分册",  # 分册体例共享页眉，内容为零信息样板
)
R2_MIN = 60


def _scope_files(root: pathlib.Path):
    rule_dir = root / "00-编纂规则与格式规范" / "01-规则"
    doctrine_dir = root / "13-软件工程"
    files = sorted(rule_dir.rglob("*.md")) + sorted(doctrine_dir.glob("*.md"))
    files.append(root / "AGENTS.md")
    return [p for p in files if p.is_file()]


def _read(path: pathlib.Path) -> str:
    try:
        return path.read_text(encoding="utf-8").replace("\ufeff", "")
    except OSError:
        return ""


def _strip_fences(text: str):
    """剥围栏代码块，返回 [(lineno, line)]。"""
    out, fence = [], False
    for i, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("```"):
            fence = not fence
            continue
        if not fence:
            out.append((i, line))
    return out


INLINE_CODE_RE = re.compile(r"`[^`]*`")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)#?]+?)\)")


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def _check_r1(files, root):
    """幻影相对 .md 链接。"""
    bad = []
    for p in files:
        for i, line in _strip_fences(_read(p)):
            for m in LINK_RE.finditer(INLINE_CODE_RE.sub("", line)):
                t = m.group(1).strip()
                if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", t) or not t.lower().endswith(".md"):
                    continue
                if not (p.parent / t).exists():
                    bad.append("%s L%d → %s" % (p.relative_to(root), i, t))
    return bad


def _check_r2(files, root):
    """跨文件长行复制（非表格行）。"""
    occ = defaultdict(list)
    for p in files:
        for i, line in _strip_fences(_read(p)):
            n = _norm(line)
            if len(n) < R2_MIN or n.startswith("|"):
                continue
            if any(n.startswith(w) for w in WL_PREFIXES):
                continue
            occ[n].append((p, i))
    bad = []
    for n, occs in sorted(occ.items(), key=lambda kv: -len(kv[1])):
        ps = {o[0] for o in occs}
        if len(ps) > 1:
            locs = "、".join("%s L%d" % (o[0].relative_to(root), o[1]) for o in occs[:4])
            bad.append("×%d（%s）：%s" % (len(occs), locs, n[:60]))
    return bad


def _check_r3(files, root):
    """同文件同表重复数据行。"""
    bad = []
    for p in files:
        lines = [l for _, l in _strip_fences(_read(p))]
        table, start = [], None
        tables = []

        def flush(tb, s):
            if len(tb) >= 2:
                tables.append((s, tb))

        for idx, line in enumerate(lines):
            if line.lstrip().startswith("|"):
                if start is None:
                    start = idx + 1
                table.append(line)
            else:
                flush(table, start)
                table, start = [], None
        flush(table, start)
        for s, tb in tables:
            seen = defaultdict(list)
            for j, row in enumerate(tb):
                if j == 0 or re.match(r"^\s*\|[\s:|-]+\|\s*$", row):
                    continue  # 表头与分隔行豁免（多表同构表头重复合法）
                seen[_norm(row)].append(s + j)
            for n, lns in seen.items():
                if len(lns) > 1:
                    bad.append("%s L%s 同表数据行 ×%d：%s" % (
                        p.relative_to(root), lns, len(lns), n[:50]))
    return bad


def _check_r4(files, root):
    """同文件同父节重复标题。"""
    bad = []
    for p in files:
        stack = {}  # level -> norm(title)
        seen = defaultdict(list)
        for i, line in _strip_fences(_read(p)):
            m = re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", line)
            if not m:
                continue
            lvl, title = len(m.group(1)), _norm(m.group(2))
            parent = stack.get(lvl - 1) if lvl > 1 else None
            for k in [k for k in stack if k >= lvl]:
                del stack[k]
            stack[lvl] = title
            seen[(parent, title)].append(i)
        for (parent, title), lns in seen.items():
            if len(lns) > 1:
                bad.append("%s L%s 同父节（%s）重复标题“%s”" % (
                    p.relative_to(root), lns, parent or "顶层", title[:40]))
    return bad


def run_checks(root: pathlib.Path):
    files = _scope_files(root)
    rows = []
    checks = (
        ("R1", "幻影相对 .md 链接", _check_r1),
        ("R2", "跨文件长行复制（≥%d 字符，非表格行）" % R2_MIN, _check_r2),
        ("R3", "同文件同表重复数据行", _check_r3),
        ("R4", "同文件同父节重复标题", _check_r4),
    )
    for code, name, fn in checks:
        bad = fn(files, root)
        rows.append((code, name, not bad,
                     "0 处" if not bad else "%d 处：%s" % (len(bad), "；".join(bad[:5]))))
    return rows


def _report(rows):
    print("=" * 72)
    print("规则语料单一落点与去重门禁（第四十二件）")
    print("=" * 72)
    fails = 0
    for code, name, ok, detail in rows:
        print("  [%s] %-4s %s" % ("PASS" if ok else "FAIL", code, name))
        print("           %s" % detail)
        fails += 0 if ok else 1
    print("-" * 72)
    print("  合计 %d 项，FAIL %d 项" % (len(rows), fails))
    return fails


def _write_fixture(tmp: pathlib.Path):
    rule = tmp / "00-编纂规则与格式规范" / "01-规则"
    (rule / "子").mkdir(parents=True, exist_ok=True)
    (tmp / "13-软件工程").mkdir(parents=True, exist_ok=True)
    (tmp / "AGENTS.md").write_text("# AGENTS\n\n根指南。\n", encoding="utf-8")
    (rule / "子" / "规则B.md").write_text("# 规则B\n\n## 小节一\n\n正文。\n", encoding="utf-8")
    (tmp / "13-软件工程" / "01-理论.md").write_text("# 理论\n\n## 1. 命题\n\n正文。\n", encoding="utf-8")
    (rule / "规则A.md").write_text(
        "# 规则A\n\n"
        "## 域一\n\n"
        "### 用法\n\n"
        "这是一条足够长的独有正文行，用于占住正样本基线，确保跨文件复制判据在正样本上保持沉默，"
        "字数务必超过六十字符阈值才行。\n\n"
        "| 项 | 值 |\n| ---- | ---- |\n| 甲 | 1 |\n| 乙 | 2 |\n\n"
        "参见 [规则B](子/规则B.md)。\n\n"
        "## 域二\n\n"
        "### 用法\n\n"
        "域二的用法小节与域一同名但父节不同，属合法体例。\n",
        encoding="utf-8")


def _failed_codes(root: pathlib.Path):
    return {code for code, _n, ok, _d in run_checks(root) if not ok}


def cmd_selftest():
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="ruledup_"))
    failures = []
    try:
        _write_fixture(tmp)
        got = _failed_codes(tmp)
        if got:
            failures.append("正样本应 0 FAIL，实际 %s" % sorted(got))

        def rewrite(name, text):
            (tmp / "00-编纂规则与格式规范" / "01-规则" / name).write_text(text, encoding="utf-8")

        base = None  # 每例先重建夹具再变异
        cases = [
            # R1 负向：幻影相对链接
            ("R1", True, lambda: rewrite("规则A.md",
                "# 规则A\n\n参见 [不存在](不存在.md) 与 [规则B](子/规则B.md)。\n")),
            # R2 负向：同一条 ≥60 字符行出现于两个文件
            ("R2", True, lambda: (rewrite("规则A.md",
                "# 规则A\n\n这是一条被蓄意复制到两个文件的超长正文行，用来触发跨文件长行复制判据，"
                "复制即负债而引用即保全，它的长度必须稳超六十个字符的阈值才能被稳定命中。\n"),
                (tmp / "13-软件工程" / "01-理论.md").write_text(
                    "# 理论\n\n这是一条被蓄意复制到两个文件的超长正文行，用来触发跨文件长行复制判据，"
                    "复制即负债而引用即保全，它的长度必须稳超六十个字符的阈值才能被稳定命中。\n", encoding="utf-8"))),
            # R3 负向：同表重复数据行
            ("R3", True, lambda: rewrite("规则A.md",
                "# 规则A\n\n| 项 | 值 |\n| ---- | ---- |\n| 甲 | 1 |\n| 甲 | 1 |\n")),
            # R4 负向：同父节重复标题
            ("R4", True, lambda: rewrite("规则A.md",
                "# 规则A\n\n## 域一\n\n### 用法\n\n甲。\n\n### 用法\n\n乙。\n")),
            # R2 豁免正例：分册页眉白名单不触发 R2
            ("R2", False, lambda: (rewrite("规则A.md",
                "# 规则A\n\n> 本件为《流程规则》分册（2026-10-27 ykla 令按主题拆分；原文 2,574 行 62 节）。"
                "判据正文以下列各节为准；总索引见同目录 `00-索引.md`。\n"),
                (tmp / "13-软件工程" / "01-理论.md").write_text(
                    "# 理论\n\n> 本件为《流程规则》分册（2026-10-27 ykla 令按主题拆分；原文 2,574 行 62 节）。"
                    "判据正文以下列各节为准；总索引见同目录 `00-索引.md`。\n", encoding="utf-8"))),
        ]
        for code, expect_fail, mutate in cases:
            shutil.rmtree(tmp / "00-编纂规则与格式规范", ignore_errors=True)
            _write_fixture(tmp)
            mutate()
            got = _failed_codes(tmp)
            if expect_fail:
                if code not in got:
                    failures.append("%s 负向夹具未被命中（实际 %s）" % (code, sorted(got)))
            elif got:
                failures.append("白名单正例误杀（实际 %s）" % sorted(got))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    if failures:
        print("  ❌ 判据非空自检失败：")
        for f in failures:
            print("     - %s" % f)
        return 1
    print("  ✅ 判据非空自检通过：正样本 0 FAIL；R1–R4 四类负向夹具均命中，白名单正例不误杀")
    return 0


def main():
    ap = argparse.ArgumentParser(description="规则语料单一落点与去重门禁（第四十二件）")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--root", metavar="<仓库根>", help="指定仓库根（默认本文件上溯三层）")
    args = ap.parse_args()

    if args.selftest:
        return cmd_selftest()

    root = pathlib.Path(args.root).resolve() if args.root else REPO
    if args.list:
        print("对象：")
        for p in _scope_files(root):
            print("  %s" % p.relative_to(root) if p.is_relative_to(root) else "  %s" % p)
        return 0
    if not (root / "00-编纂规则与格式规范" / "01-规则").is_dir():
        print("  [FATAL] 范围目录缺失：%s" % root)
        return 2

    rows = run_checks(root)
    fails = _report(rows)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
