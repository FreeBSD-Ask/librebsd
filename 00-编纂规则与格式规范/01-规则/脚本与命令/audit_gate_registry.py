#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""audit_gate_registry.py —— 第十六件门禁：门禁体系自身的元门禁。

设立缘由（2026-09-28）
----------------------
本项目反复出现同一失效模式：**“工具已文档化 ≠ 工具已生效”**。

- `markdownlint-cli2` 在 `CLAUDE.md` 里写了运行命令、给了配置，却**长期未接入任何门禁**
  → 缺陷静默累积（2026-09-20 实测审计面 89 文件 5,487 条）。
- `_scan_blockfn_scope.py` 曾写出并解决了真实缺陷（严格模式致三个功能失效），却**未升格为门禁**，
  随 `script/` 临时目录一并消失。
- `serve_refactor2026.py` 标称“固定脚本，规则引用资源”，却**未登记进 `脚本与命令/README.md`、
  无任何规则文件引用**，且与另一份实现语义分叉、双双缺安全头——2026-09-28 才发现。

本件把“接线”本身变成可机检的不变量：登记表 ↔ 磁盘实况 ↔ 规则文档，三方须一致。

判据
----
R1 **存在性**：登记表内每个脚本在磁盘上存在
R2 **可编译性**：登记的 `.py` 可 `py_compile`；`.mjs` 跳过（需 node，本件不引入依赖）
R3 **无漏接线**：`脚本与命令/audit_*.py` 全部已登记（防“写了门禁忘了登记”）
R4 **有规则引用**：每个登记脚本名至少出现在 `流程规则.md`／`CLAUDE.md`／
   `脚本与命令/README.md`／`重构2026/tests/README.md` 之一（CLAUDE.md 要求固定脚本须由规则文件引用）
R5 **套件清单一致**：标记 `in_tests_readme` 的登记件，其文件名须出现在 `tests/README.md`

用法
----
    python audit_gate_registry.py                 # 0 一致 / 1 不一致 / 2 依赖缺失
    python audit_gate_registry.py --list          # 打印登记表
    python audit_gate_registry.py --selftest      # 判据非空：造“漏登记 + 缺文件”夹具，须 FAIL

依赖：仅标准库。
"""
import argparse
import py_compile
import pathlib
import re
import shutil
import sys
import tempfile

sys.stdout.reconfigure(encoding="utf-8")

REPO = pathlib.Path(__file__).resolve().parents[3]
CMD = REPO / "00-编纂规则与格式规范" / "01-规则" / "脚本与命令"
TESTS = REPO / "08-核查报告与多轮复核" / "重构2026" / "tests"
RULE_DOCS = [
    REPO / "00-编纂规则与格式规范" / "01-规则" / "流程规则.md",
    REPO / "CLAUDE.md",
    CMD / "README.md",
    TESTS / "README.md",
]

# ── 登记表（唯一真值） ────────────────────────────────────────────────────
# 字段：no 编号｜script 文件名（相对 REPO）｜kind 类别｜object 对象面｜
#       trigger 触发条件｜selftest 判据非空自检命令（None = 未提供，见 R6 待办）
REGISTRY = [
    dict(no="第一件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_data_integrity.py",
         kind="门禁", object="目录页 DATA 段", trigger="改 DATA 段后",
         selftest="--selftest", in_tests_readme=True),
    dict(no="第二件", script="00-编纂规则与格式规范/01-规则/脚本与命令/sync_refactor2026_baseline.py",
         kind="门禁", object="口径声明（重构2026/*.md + CLAUDE.md + 规则目录）", trigger="目录页结构或计数变动后",
         selftest="--check", in_tests_readme=True),
    dict(no="第三件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_sequence_continuity.py",
         kind="门禁", object="节号／章号连续性 + 述评恒末", trigger="结构变动后",
         selftest=None, in_tests_readme=True),
    dict(no="第四件", script="08-核查报告与多轮复核/重构2026/tests/visual_regression.mjs",
         kind="浏览器套件", object="目录页视觉几何与功能（21 项）", trigger="改装配源后",
         selftest=None, in_tests_readme=True),
    dict(no="第五件", script="00-编纂规则与格式规范/01-规则/脚本与命令/xref_audit.py",
         kind="门禁", object="分工注交叉引用悬空", trigger="结构重编号后",
         selftest=None, in_tests_readme=True),
    dict(no="第六件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_evidence_level_labels.py",
         kind="门禁", object="大纲注入块证据等级", trigger="向 05-卷册大纲 写回带等级块后",
         selftest=None, in_tests_readme=False),
    dict(no="第七件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_index_structure.py",
         kind="门禁", object="目录页结构静态自检 A/A2/B–O", trigger="目录页结构变动后",
         selftest=None, in_tests_readme=True),
    dict(no="第八件", script="00-编纂规则与格式规范/01-规则/脚本与命令/assemble_index.py",
         kind="装配器/门禁", object="四层装配漂移（逐字节）", trigger="改任一装配源后",
         selftest="--check", in_tests_readme=True),
    dict(no="第九件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_page_assets.py",
         kind="门禁", object="页面资产层（字体子集／品牌件／自包含／夹具）", trigger="改装配源或字体子集后",
         selftest="--selftest", in_tests_readme=True),
    dict(no="第十件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_markdown_lint.py",
         kind="门禁（文档格式类，独立计数）", object="活动 .md 文件格式", trigger="改闸面内 .md 后",
         selftest="--selftest", in_tests_readme=False),
    dict(no="第十一件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_server_contract.py",
         kind="门禁（服务器，独立计数）", object="运行中的目录页服务器（8 项 HTTP 契约）", trigger="改服务器脚本后",
         selftest="--selftest", in_tests_readme=False),
    dict(no="第十二件", script="08-核查报告与多轮复核/重构2026/tests/tri_structure_negtest.py",
         kind="负向自检", object="第七件结构判据的有效性（九种缺陷副本）", trigger="改第七件判据后",
         selftest=None, in_tests_readme=True),
    dict(no="第十三件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_fixture_freshness.py",
         kind="门禁（夹具新鲜度）", object="tests/*.mjs 写死值 vs 内容源派生值", trigger="改内容源或夹具后",
         selftest="--selftest", in_tests_readme=False),
    dict(no="第十六件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_gate_registry.py",
         kind="门禁（元门禁，独立计数）", object="门禁体系自身：登记表 ↔ 磁盘 ↔ 规则文档三方一致", trigger="新增/删除门禁脚本后",
         selftest="--selftest", in_tests_readme=False),
    dict(no="—", script="00-编纂规则与格式规范/01-规则/脚本与命令/embed.py",
         kind="门禁", object="catalog 与内嵌数据块一致性", trigger="改 catalog 或数据块后",
         selftest="--check", in_tests_readme=True),
    dict(no="—", script="00-编纂规则与格式规范/01-规则/脚本与命令/guard_source_chars.py",
         kind="写盘前守卫", object="装配源字符（直角引号／U+3000／TAB／BOM）", trigger="写装配源前",
         selftest=None, in_tests_readme=False),
    dict(no="—", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_databases.py",
         kind="一次性审计（**非固定脚本**）", object="12 功能库 + 15 代码库 + 4 邮件库一次性盘点（英文 docstring，绑 06 号文设计）",
         trigger="—", selftest=None, in_tests_readme=False, fixed=False),
    dict(no="—", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_folder_db_integrity.py",
         kind="门禁（数据库类）", object="文件夹级数据库与磁盘文件清单一致性", trigger="改文件夹库后",
         selftest=None, in_tests_readme=False),
]


def _read(p):
    try:
        return p.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def run(cmd_dir: pathlib.Path, tests_dir: pathlib.Path, registry):
    rows = []

    # R1 存在性
    missing = [e["script"] for e in registry if not (REPO / e["script"]).exists()]
    rows.append(("R1", "登记脚本全部存在", not missing,
                 "登记 %d 件；缺失 %s" % (len(registry), ", ".join(missing) or "无")))

    # R2 可编译性
    bad = []
    for e in registry:
        p = REPO / e["script"]
        if p.suffix != ".py" or not p.exists():
            continue
        try:
            py_compile.compile(str(p), cfile=str(pathlib.Path(tempfile.gettempdir())
                                                 / "_grc.pyc"), doraise=True)
        except py_compile.PyCompileError as ex:
            bad.append("%s：%s" % (p.name, str(ex).splitlines()[0][:80]))
    rows.append(("R2", "登记脚本可编译（.py）", not bad,
                 "不通过 %d 件%s" % (len(bad), "：" + "；".join(bad) if bad else "")))

    # R3 无漏接线
    on_disk = {p.name for p in cmd_dir.glob("audit_*.py")}
    registered = {pathlib.Path(e["script"]).name for e in registry}
    unreg = sorted(on_disk - registered)
    rows.append(("R3", "脚本与命令/audit_*.py 全部已登记", not unreg,
                 "磁盘 %d 件、登记 %d 件；未登记 %s"
                 % (len(on_disk), len(registered & on_disk), ", ".join(unreg) or "无")))

    # R4 有规则引用（仅对固定脚本；非固定脚本见 R7）
    docs = "".join(_read(p) for p in RULE_DOCS if p.exists())
    noref = [pathlib.Path(e["script"]).name for e in registry
             if e.get("fixed", True) and pathlib.Path(e["script"]).name not in docs]
    rows.append(("R4", "每个**固定**脚本至少被一处规则／索引文档引用", not noref,
                 "无引用 %s" % (", ".join(noref) or "无")))

    # R5 套件清单一致
    tr = _read(tests_dir / "README.md")
    tbad = [pathlib.Path(e["script"]).name for e in registry
            if e["in_tests_readme"] and pathlib.Path(e["script"]).name not in tr]
    rows.append(("R5", "标记 in_tests_readme 者出现在 tests/README.md", not tbad,
                 "未出现 %s" % (", ".join(tbad) or "无")))

    # R6 自检覆盖（仅报告，不判 FAIL —— 存量多件无自检，属既有债）
    no_st = [e["no"] + " " + pathlib.Path(e["script"]).name
             for e in registry if not e["selftest"]]
    rows.append(("R6", "（仅报告）无判据非空自检的登记件", True,
                 "%d/%d 件：%s" % (len(no_st), len(registry),
                                   "、".join(no_st) if no_st else "无")))

    # R7 未登记脚本（仅报告）：规则目录内既不在登记表、也未在 README 索引者
    readme = _read(cmd_dir / "README.md")
    loose = sorted(p.name for p in cmd_dir.glob("*.py")
                   if p.name not in registered and p.name not in readme)
    rows.append(("R7", "（仅报告）规则目录内既未入登记表、也未入 README 索引的 .py", True,
                 "共 %d 件：%s" % (len(loose), "、".join(loose) if loose else "无")))
    return rows


def _report(rows, title):
    print("=" * 72)
    print(title)
    print("=" * 72)
    fails = 0
    for code, name, ok, detail in rows:
        print("  [%s] %-4s %s" % ("PASS" if ok else "FAIL", code, name))
        print("           %s" % detail)
        if not ok:
            fails += 1
    print("-" * 72)
    print("  合计 %d 项，FAIL %d 项" % (len(rows), fails))
    return fails


def cmd_selftest():
    """判据非空：造“登记了但文件不存在”＋“磁盘有 audit_*.py 未登记”两类缺陷，须 FAIL。"""
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="gatereg_"))
    try:
        cmd = tmp / "cmd"
        cmd.mkdir()
        (cmd / "audit_unregistered.py").write_text("x = 1\n", encoding="utf-8")
        reg = [
            # T1 指向真实存在的脚本（R1 应通过该项）
            dict(no="T1",
                 script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_server_contract.py",
                 kind="t", object="t", trigger="t", selftest=None,
                 in_tests_readme=False),
            # T2 登记了但磁盘不存在（R1 必 FAIL）
            dict(no="T2", script="___missing___/audit_absent.py",
                 kind="t", object="t", trigger="t", selftest=None,
                 in_tests_readme=False),
        ]
        rows = run(cmd, tmp, reg)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    fails = _report(rows, "判据非空自检：登记缺失 + 磁盘漏登记（预期 R1/R3 FAIL）")
    got = {c for c, _n, ok, _d in rows if not ok}
    if {"R1", "R3"} <= got:
        print("  ✅ 判据非空：R1（文件缺失）与 R3（漏登记）均命中")
        return 0
    print("  ❌ 判据可能为空：未同时命中 R1/R3（实际 %s）" % (sorted(got) or "空"),
          file=sys.stderr)
    return 1


def main():
    ap = argparse.ArgumentParser(description="门禁体系元门禁（第十六件）")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        return cmd_selftest()

    if args.list:
        print("%-8s %-44s %-14s %s" % ("编号", "脚本", "类别", "对象面"))
        for e in REGISTRY:
            print("%-8s %-44s %-14s %s" % (e["no"], pathlib.Path(e["script"]).name,
                                           e["kind"], e["object"]))
        print("\n合计 %d 件（其中 %d 件未提供判据非空自检）"
              % (len(REGISTRY), sum(1 for e in REGISTRY if not e["selftest"])))
        return 0

    for p, what in ((CMD, "脚本与命令目录"), (TESTS / "README.md", "tests/README.md")):
        if not p.exists():
            print("依赖缺失：%s（%s）" % (p, what), file=sys.stderr)
            return 2
    rows = run(CMD, TESTS, REGISTRY)
    return 1 if _report(rows, "门禁体系元门禁（第十六件）") else 0


if __name__ == "__main__":
    sys.exit(main())
