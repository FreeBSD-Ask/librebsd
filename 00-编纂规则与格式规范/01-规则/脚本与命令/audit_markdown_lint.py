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
4. `08-核查报告与多轮复核/重构2026/7[0-9]-*.md`（现行号文执行记录；2026-10-05 起闸面扩至 `117-*.md`（含 `117b-*.md`））

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

防衰减护栏（2026-09-20 补）
--------------------------
①**闸面模式零匹配**即 FAIL——防止目录改名／模式失效后「闸面悄悄变成 0 文件」而假绿；
②**号文带上限**：`重构2026/` 下出现编号 > `HAOWEN_MAX_COVERED`（当前 127）的 .md 即 FAIL，
强制把新号文补进 MANIFEST——否则 `7[0-9]-*.md` 这个模式会随号文增长**静默失效**。

用法
----
    python audit_markdown_lint.py            # 跑闸面（0 问题 exit 0）
    python audit_markdown_lint.py --list     # 只打印闸面清单
    python audit_markdown_lint.py --all      # 全审计面（含豁免件）统计，仅供可见性
    python audit_markdown_lint.py --selftest # 判据非空自检（8 条分支，临时目录夹具）
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
    "08-核查报告与多轮复核/重构2026/8[0-9]-*.md",
    "08-核查报告与多轮复核/重构2026/90-*.md",
    "08-核查报告与多轮复核/重构2026/91-*.md",
    "08-核查报告与多轮复核/重构2026/92-*.md",
    "08-核查报告与多轮复核/重构2026/93-*.md",
    "08-核查报告与多轮复核/重构2026/94-*.md",
    "08-核查报告与多轮复核/重构2026/95-*.md",
    "08-核查报告与多轮复核/重构2026/96-*.md",
    "08-核查报告与多轮复核/重构2026/97-*.md",
    "08-核查报告与多轮复核/重构2026/98-*.md",
    "08-核查报告与多轮复核/重构2026/99-*.md",
    "08-核查报告与多轮复核/重构2026/100-*.md",
    "08-核查报告与多轮复核/重构2026/101-*.md",
    "08-核查报告与多轮复核/重构2026/102-*.md",
    "08-核查报告与多轮复核/重构2026/103-*.md",
    "08-核查报告与多轮复核/重构2026/104-*.md",
    "08-核查报告与多轮复核/重构2026/105-*.md",
    "08-核查报告与多轮复核/重构2026/106-*.md",
    "08-核查报告与多轮复核/重构2026/107-*.md",
    "08-核查报告与多轮复核/重构2026/108-*.md",
    "08-核查报告与多轮复核/重构2026/109-*.md",
    "08-核查报告与多轮复核/重构2026/110-*.md",
    "08-核查报告与多轮复核/重构2026/111-*.md",
    "08-核查报告与多轮复核/重构2026/112-*.md",
    "08-核查报告与多轮复核/重构2026/113-*.md",
    "08-核查报告与多轮复核/重构2026/114-*.md",
    "08-核查报告与多轮复核/重构2026/115-*.md",
    "08-核查报告与多轮复核/重构2026/116-*.md",
    "08-核查报告与多轮复核/重构2026/117-*.md",
    "08-核查报告与多轮复核/重构2026/117b-*.md",
    "08-核查报告与多轮复核/重构2026/119-*.md",
    "08-核查报告与多轮复核/重构2026/119b-*.md",
    "08-核查报告与多轮复核/重构2026/119c-*.md",
    "08-核查报告与多轮复核/重构2026/119d-*.md",
    "08-核查报告与多轮复核/重构2026/120-*.md",
    "08-核查报告与多轮复核/重构2026/121-*.md",
    "08-核查报告与多轮复核/重构2026/122-*.md",
    "08-核查报告与多轮复核/重构2026/123-*.md",
    "08-核查报告与多轮复核/重构2026/124-*.md",
    "08-核查报告与多轮复核/重构2026/125-*.md",
    "08-核查报告与多轮复核/重构2026/126-*.md",
    "08-核查报告与多轮复核/重构2026/127-*.md",
    "08-核查报告与多轮复核/重构2026/128-*.md",
    "08-核查报告与多轮复核/重构2026/tests/*.md",
    "10-交叉索引/S03-历史对象登记表.md",
    "08-核查报告与多轮复核/12-重构大纲书目述评/index.md",
    "01-项目管理/01-编纂规划与报告归档/长线任务总登记表.md",
]

# 号文系列「防衰减」护栏（2026-09-20 补；2026-10-02 扩至 102 号）
# 闸面以 `7[0-9]-*.md`＋`8[0-9]-*.md`＋`90-*.md` 至 `128-*.md`（含 `117b-*.md`、`119b-*.md`、`119c-*.md`、`119d-*.md`）覆盖现行号文带。**判据会随号文增长而静默失效**——
# 一旦出现 117 号及以后的号文，该文件既不在闸面内、也无任何提示，护栏形同虚设。
# 故立此护栏：`重构2026/` 下任何「编号 > 带上限」的 .md 一律判 FAIL，
# 强制把新号文补进 MANIFEST 并同步 CLAUDE.md／流程规则.md 的闸面清单。
HAOWEN_DIR = "08-核查报告与多轮复核/重构2026"
HAOWEN_NUM_RE = re.compile(r"^(\d+)-.*\.md$")
HAOWEN_MAX_COVERED = 128

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
    "08-核查报告与多轮复核/重构2026/90-x.md",
    "08-核查报告与多轮复核/重构2026/91-x.md",
    "08-核查报告与多轮复核/重构2026/92-x.md",
    "08-核查报告与多轮复核/重构2026/93-x.md",
    "08-核查报告与多轮复核/重构2026/94-x.md",
    "08-核查报告与多轮复核/重构2026/95-x.md",
    "08-核查报告与多轮复核/重构2026/96-x.md",
    "08-核查报告与多轮复核/重构2026/97-x.md",
    "08-核查报告与多轮复核/重构2026/98-x.md",
    "08-核查报告与多轮复核/重构2026/99-x.md",
    "08-核查报告与多轮复核/重构2026/100-x.md",
    "08-核查报告与多轮复核/重构2026/101-x.md",
    "08-核查报告与多轮复核/重构2026/102-x.md",
    "08-核查报告与多轮复核/重构2026/103-x.md",
    "08-核查报告与多轮复核/重构2026/104-x.md",
    "08-核查报告与多轮复核/重构2026/105-x.md",
    "08-核查报告与多轮复核/重构2026/106-x.md",
    "08-核查报告与多轮复核/重构2026/107-x.md",
    "08-核查报告与多轮复核/重构2026/108-x.md",
    "08-核查报告与多轮复核/重构2026/109-x.md",
    "08-核查报告与多轮复核/重构2026/110-x.md",
    "08-核查报告与多轮复核/重构2026/111-x.md",
    "08-核查报告与多轮复核/重构2026/112-x.md",
    "08-核查报告与多轮复核/重构2026/113-x.md",
    "08-核查报告与多轮复核/重构2026/114-x.md",
    "08-核查报告与多轮复核/重构2026/115-x.md",
    "08-核查报告与多轮复核/重构2026/116-x.md",
    "08-核查报告与多轮复核/重构2026/117-x.md",
    "08-核查报告与多轮复核/重构2026/117b-x.md",
    "08-核查报告与多轮复核/重构2026/119-x.md",
    "08-核查报告与多轮复核/重构2026/119b-x.md",
    "08-核查报告与多轮复核/重构2026/119c-x.md",
    "08-核查报告与多轮复核/重构2026/119d-x.md",
    "08-核查报告与多轮复核/重构2026/120-x.md",
    "08-核查报告与多轮复核/重构2026/121-x.md",
    "08-核查报告与多轮复核/重构2026/122-x.md",
    "08-核查报告与多轮复核/重构2026/123-x.md",
    "08-核查报告与多轮复核/重构2026/124-x.md",
    "08-核查报告与多轮复核/重构2026/125-x.md",
    "08-核查报告与多轮复核/重构2026/126-x.md",
    "08-核查报告与多轮复核/重构2026/127-x.md",
    "08-核查报告与多轮复核/重构2026/128-x.md",
    "08-核查报告与多轮复核/重构2026/tests/README.md",
    "10-交叉索引/S03-历史对象登记表.md",
    "08-核查报告与多轮复核/12-重构大纲书目述评/index.md",
    "01-项目管理/01-编纂规划与报告归档/长线任务总登记表.md",
]


def selftest():
    """判据非空自检：在系统临时目录搭隔离夹具树，逐条实测**全部分支**。

    不触碰工作树；覆盖正常／lint 命中／零匹配／新号文／版本不符／依赖缺失／
    `--allow-version`／`--list` 八条路径。返回 0 全通过，1 有未通过项。
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

    newdoc = tmp / HAOWEN_DIR / "129-new.md"
    newdoc.write_text("# t\n", encoding="utf-8")
    cases.append(("T2 号文防衰减护栏（编号 > 上限）", run([]), 1))
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

    # 号文系列防衰减护栏：编号超出闸面覆盖带者一律 FAIL（详见文件头注释）
    over = []
    for p in sorted((ROOT / HAOWEN_DIR).glob("*.md")):
        m = HAOWEN_NUM_RE.match(p.name)
        if m and int(m.group(1)) > HAOWEN_MAX_COVERED:
            over.append(p.relative_to(ROOT).as_posix())
    if over:
        print(f"[exit 1] 新号文未入闸面（编号 > {HAOWEN_MAX_COVERED}）：{over}", file=sys.stderr)
        print("         请把上述文件纳入 MANIFEST，并同步 CLAUDE.md／流程规则.md 的闸面清单"
              f"（当前带：7[0-9]、8[0-9]、90–128，上限 {HAOWEN_MAX_COVERED}）。", file=sys.stderr)
        return 1
    band = [p.name for p in (ROOT / HAOWEN_DIR).glob("*.md")
            if (mm := HAOWEN_NUM_RE.match(p.name)) and int(mm.group(1)) <= HAOWEN_MAX_COVERED]
    print(f"号文带覆盖：同目录 ≤{HAOWEN_MAX_COVERED} 号 .md 共 {len(band)} 个"
          f"（70–{HAOWEN_MAX_COVERED} 在闸面内；≤69 属豁免历史件）")

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
