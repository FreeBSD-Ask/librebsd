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
4. `08-核查报告与多轮复核/重构2026/` 现行号文与执行记录——**全域号段模式**：
   `[7-9][0-9]-*.md`（70–99）／`1[0-9][0-9]-*.md`（100–199）／`1[0-9][0-9][a-z]-*.md`（单字母变体）
   （2026-10-15 主理人令「解禁目录编号限制」：不设编号上限、新号文零登记自动入面）

5. `08-核查报告与多轮复核/重构2026/tests/*.md`（现行测试夹具文档）
6. `08-核查报告与多轮复核/12-重构大纲书目述评/index.md`（现行外迁目录索引）
7. `01-项目管理/01-编纂规划与报告归档/长线任务总登记表.md`（现行共享登记表；2026-09-20 起纳入）

**豁免**（不属闸面，理由见 CLAUDE.md「Lint 配置」）：
- `01-项目管理/**` 历史规划与报告归档（一次性产物，已冻结）；
- `08-核查报告与多轮复核/重构2026/` 下 70 号以前的**历史规划/映射/审计类文档**
  （一次性分析产物，对应既有「历史快照豁免」概念）；
- `08-核查报告与多轮复核/12-重构大纲书目述评/第*-章级书目述评.md`（逐字保真档案）；
- `00-编纂规则与格式规范/01-规则/script/**`（脚本运行日志）。

> 2026-09-20 起：`长线任务总登记表.md` **已纳入闸面**（原遗留 63 条已按纯格式治理归零；
> 其机读块由 `_longline_status.py --write-block` 生成、不含表格，不影响闸面）。

退出码
------
0 = 闸面 0 问题；1 = 有 lint 问题或闸面失效；2 = 依赖缺失或版本不符。

版本钉定
--------
实测 v0.23.2 与 v0.22.1 对同一语料给出**不同计数**（5,487 条为 v0.23.2 与 v0.22.1
一致值，但历史上 `npx --yes` 曾拉到新版产生漂移）。为保证可复现，本门禁钉定
`markdownlint-cli2 0.22.1 / markdownlint 0.40.0`；升级须显式 `--allow-version`。

防衰减护栏（2026-09-20 补；2026-10-15 解禁改造）
------------------------------------------
①**闸面模式零匹配**即 FAIL——防止目录改名／模式失效后「闸面悄悄变成 0 文件」而假绿；
②**号文全覆盖自警**（2026-10-15 主理人令「解禁目录编号限制」）：号文带**不设编号上限**——
闸面以全域号段模式（70–99／100–199 及单字母变体）覆盖现行与近程号文，新号文**零登记**
自动入面；护栏改为「顶层 70 号以后数字起首的 .md 全部须在闸面解析集内」——出现未覆盖者
（命名异常，或超出已覆盖号段如 200+／四位编号）即 FAIL 自警，补一行模式即续。
（旧制「编号 > 上限 129 即 FAIL ＋ 逐号登记四步」自 2026-10-15 起废止。）

用法
----
    python audit_markdown_lint.py            # 跑闸面（0 问题 exit 0）
    python audit_markdown_lint.py --list     # 只打印闸面清单
    python audit_markdown_lint.py --all      # 全审计面（含豁免件）统计，仅供可见性
    python audit_markdown_lint.py --selftest # 判据非空自检（10 项分支，临时目录夹具）
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
    "08-核查报告与多轮复核/重构2026/[7-9][0-9]-*.md",
    "08-核查报告与多轮复核/重构2026/1[0-9][0-9]-*.md",
    "08-核查报告与多轮复核/重构2026/1[0-9][0-9][a-z]-*.md",
    "08-核查报告与多轮复核/重构2026/tests/*.md",
    "10-交叉索引/S03-历史对象登记表.md",
    "08-核查报告与多轮复核/12-重构大纲书目述评/index.md",
    "01-项目管理/01-编纂规划与报告归档/长线任务总登记表.md",
]

# 号文系列「防衰减」护栏（2026-09-20 补；2026-10-15 解禁改造——主理人令「解禁目录编号限制」）：
# 不再设编号上限、不再逐号登记。闸面以全域号段模式覆盖：`[7-9][0-9]-`（70–99）、
# `1[0-9][0-9]-`（100–199）、`1[0-9][0-9][a-z]-`（单字母变体）。70–99 字母变体与 200+
# 暂无可匹配文件（零匹配模式即 FAIL），故不预置——出现时由护栏自警、补一行模式续接。
# 护栏：顶层 70 号以后数字起首的 .md 未被闸面解析集覆盖即 FAIL（防「静默漏检」）。
HAOWEN_DIR = "08-核查报告与多轮复核/重构2026"
HAOWEN_NUM_RE = re.compile(r"^(\d+)[a-z]?-.*\.md$")
HAOWEN_MIN_NUM = 70

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


# 自检夹具：覆盖 MANIFEST 全部模式（T0 断言覆盖，防夹具与闸面脱钩）
SELFTEST_FIXTURE = [
    "CLAUDE.md",
    "00-编纂规则与格式规范/01-规则/README.md",
    "00-编纂规则与格式规范/01-规则/脚本与命令/README.md",
    "08-核查报告与多轮复核/重构2026/75-x.md",
    "08-核查报告与多轮复核/重构2026/80-x.md",
    "08-核查报告与多轮复核/重构2026/146-x.md",
    "08-核查报告与多轮复核/重构2026/146b-x.md",
    "08-核查报告与多轮复核/重构2026/tests/README.md",
    "10-交叉索引/S03-历史对象登记表.md",
    "08-核查报告与多轮复核/12-重构大纲书目述评/index.md",
    "01-项目管理/01-编纂规划与报告归档/长线任务总登记表.md",
]


def selftest():
    """判据非空自检：在系统临时目录搭隔离夹具树，逐条实测**全部分支**。

    不触碰工作树；T0–T7 共 **10 项**：夹具覆盖／正常／新号文自动入面（解禁）／
    未覆盖号段自警／零匹配／版本不符／`--allow-version`／依赖缺失／`--list`／注入缺陷。
    返回 0 全通过，1 有未通过项。
    """
    import os
    import tempfile

    tmp = Path(tempfile.mkdtemp(prefix="mdlint_gate_selftest_"))
    gate = tmp / "a" / "b" / "c" / "audit_markdown_lint.py"
    gate.parent.mkdir(parents=True)
    shutil.copy2(Path(__file__).resolve(), gate)
    shutil.copy2(ROOT / ".markdownlint.json", tmp / ".markdownlint.json")
    for rel in SELFTEST_FIXTURE:
        p = tmp / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("# t\n", encoding="utf-8")

    # T0：夹具须覆盖 MANIFEST 的每个模式（闸面扩容而夹具未同步时立即暴露）
    t0 = all(any(True for _ in tmp.glob(pat)) for pat in MANIFEST)

    fake = tmp / "_fakebin"
    fake.mkdir()
    real = find_bin()
    if os.name == "nt":
        (fake / "markdownlint-cli2.cmd").write_text(
            "@echo off\r\nif not \"%~1\"==\"--version\" goto delegate\r\n"
            "echo markdownlint-cli2 v0.99.9 (markdownlint v9.9.9)\r\n"
            "exit /b 0\r\n:delegate\r\n"
            f'call "{real}" %*\r\n', encoding="ascii", newline="")
    else:
        sh = fake / "markdownlint-cli2"
        sh.write_text(
            "#!/bin/sh\n"
            "if [ \"$1\" = \"--version\" ]; then "
            "echo 'markdownlint-cli2 v0.99.9 (markdownlint v9.9.9)'; exit 0; fi\n"
            f'exec "{real}" "$@"\n', encoding="utf-8")
        sh.chmod(0o755)

    def run(args, path_prefix=None, isolate_path=False):
        env = dict(os.environ)
        if path_prefix is not None:
            env["PATH"] = str(path_prefix) + os.pathsep + env.get("PATH", "")
        if isolate_path:
            env["PATH"] = str(tmp)  # 仅含夹具目录 → 查不到 markdownlint-cli2
        out = subprocess.run([sys.executable, str(gate)] + args, env=env,
                             capture_output=True, text=True,
                             encoding="utf-8", errors="replace")
        return out.returncode

    cases = [("T0 夹具覆盖闸面全部模式", 0 if t0 else 1, 0)]
    cases.append(("T1 正常（全模式命中、lint 干净）", run([]), 0))

    newdoc = tmp / HAOWEN_DIR / "146-new.md"
    newdoc.write_text("# t\n", encoding="utf-8")
    cases.append(("T2a 新号文自动入面（解禁后零登记）", run([]), 0))
    newdoc.unlink()

    newdoc = tmp / HAOWEN_DIR / "999-new.md"
    newdoc.write_text("# t\n", encoding="utf-8")
    cases.append(("T2b 未覆盖号段自警 → FAIL", run([]), 1))
    newdoc.unlink()

    rule_readme = tmp / "00-编纂规则与格式规范/01-规则/README.md"
    kept = rule_readme.read_text(encoding="utf-8")
    rule_readme.unlink()
    cases.append(("T3 闸面模式零匹配 → FAIL", run([]), 1))
    rule_readme.write_text(kept, encoding="utf-8")

    cases.append(("T4a 版本不符 → exit 2", run([], path_prefix=fake), 2))
    cases.append(("T4b --allow-version 放行", run(["--allow-version"], path_prefix=fake), 0))
    cases.append(("T5 依赖缺失 → exit 2", run([], isolate_path=True), 2))
    cases.append(("T6 --list", run(["--list"]), 0))

    (tmp / "CLAUDE.md").write_text("# t\n| a|b |\n|---|---|\n", encoding="utf-8")
    cases.append(("T7 闸面内注入缺陷 → exit 1", run([]), 1))

    ok = True
    for name, got, want in cases:
        if got != want:
            ok = False
        print(f"{'PASS' if got == want else 'FAIL'} | {name} | 期望 exit {want}，实得 {got}")
    shutil.rmtree(tmp, ignore_errors=True)
    print("自检结论：" + ("全部通过" if ok else "有未通过项"))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true", help="只打印闸面清单")
    ap.add_argument("--all", action="store_true", help="全审计面统计（仅可见性，恒 exit 0）")
    ap.add_argument("--allow-version", action="store_true", help="允许非钉定版本")
    ap.add_argument("--selftest", action="store_true", help="判据非空自检（临时目录夹具，不触碰工作树）")
    args = ap.parse_args()

    if args.selftest:
        return selftest()

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

    # 号文系列防衰减护栏（2026-10-15 解禁版，详见文件头注释）：不设编号上限——
    # 「顶层 70 号以后数字起首的 .md 全部须在闸面解析集内」；未覆盖者（命名异常
    # 或超出已覆盖号段）即 FAIL 自警——防「静默漏检」，但不再需要逐号登记。
    face_set = set(files)
    over = []
    for p in sorted((ROOT / HAOWEN_DIR).glob("*.md")):
        m = HAOWEN_NUM_RE.match(p.name)
        if m and int(m.group(1)) >= HAOWEN_MIN_NUM:
            rel = p.relative_to(ROOT).as_posix()
            if rel not in face_set:
                over.append(rel)
    if over:
        print("[exit 1] 顶层号文未入闸面（命名不合全域模式或超出已覆盖号段）：", file=sys.stderr)
        for o in over:
            print(f"         {o}", file=sys.stderr)
        print("         闸面号段模式＝[7-9][0-9]-／1[0-9][0-9]-／1[0-9][0-9][a-z]-"
              "（70–199 系，含单字母变体）；新形态按同法补一行模式"
              "（并同步 CLAUDE.md／流程规则.md 闸面清单）。", file=sys.stderr)
        return 1
    band = [p.name for p in (ROOT / HAOWEN_DIR).glob("*.md")
            if (mm := HAOWEN_NUM_RE.match(p.name)) and int(mm.group(1)) >= HAOWEN_MIN_NUM]
    print(f"号文带覆盖：同目录 70 号以后 .md 共 {len(band)} 个"
          f"（全域模式自动覆盖，不设编号上限；≤69 属豁免历史件）")

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
