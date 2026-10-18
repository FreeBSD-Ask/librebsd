#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""audit_md_quote_glyphs.py —— 第二十四件门禁：全库 Markdown 直角引号清零。

设立缘由（2026-10-17）
----------------------
写作规则（「标点符号规则」「中文引号强制规则」）与 `ROW_MINE块体格式规则.md`
早已禁用中文直角引号（U+300C／U+300D／U+300E／U+300F，含半角 ｢｣ U+FF62／U+FF63），
但长期无机器防线，历史文档累计沉积约 23 万处。2026-10-17 全库转写批一次性清零
（229,705＋105,944 处，5,426 文件），本件把「清零态」固化为不变量，防再生。

判据
----
T1 **直角引号清零**：全库 `*.md` 中六个码位（U+300C U+300D U+300E U+300F
    U+FF62 U+FF63）出现即 FAIL。判据面＝**入库内容**：跳过 `.git`／`node_modules`
    等，并跳过**不入库工作区**（顶层 `script/`、`_tmp/`、`specs/`、`.trae/`、
    `.workbuddy/`、`.zcode/`、`.github/`、`.gitbook/`，均按根 `.gitignore` 排除、
    不入库——对其判直角引号只会使本件恒 FAIL 而被忽略，等于防线空转；
    `00-编纂规则与格式规范/01-规则/script/` 下有入库 `.md`，故 `script` 只在
    根层跳过）。UTF-8 不可解码者与 open 抛 `OSError` 者（walk 与 open 之间被
    并发清理）均计数并披露、不阻断判据。
T2 **弯引号配对披露（INFO，不计 FAIL）**：逐文件统计 “／” 净差与 ‘／’ 净差，
    仅汇总披露——历史 OCR 档案（`04-现代研究文献/03-文献下载/**`）存在批前既有
    失衡（逐字保真档案不回改），修复属另案；本件不把它当作门禁判据，防止
    「把历史债务伪装成本件 FAIL」。

规则衔接
--------
- 字符集字面量（如正则、禁字符清单）须以**码位记法**表述（`U+300C`），不得回写字形；
  见 `写作规则.md`「直角引号与码位记法」。
- 装配源层面的同类防线见 `guard_source_chars.py`（写盘前守卫，第九件判据面）。

用法
----
    python audit_md_quote_glyphs.py                # 全库扫描；0 = PASS / 1 = FAIL
    python audit_md_quote_glyphs.py --root <目录>   # 限定子树（调试用）
    python audit_md_quote_glyphs.py --selftest     # 判据非空：造含 U+300C 夹具须 FAIL

依赖：仅标准库。
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile

sys.stdout.reconfigure(encoding="utf-8")

CORNER = {"\u300c", "\u300d", "\u300e", "\u300f", "\uff62", "\uff63"}
# 不入库工作区一律不在本件判据面：它们按 .gitignore 排除、不入库，
# 对其判直角引号只会让全库门禁恒 FAIL 而被忽略，等于防线空转。
# 与根 .gitignore 及 markdownlint 的排除清单同口径。
SKIP_DIRS = {
    ".git", "node_modules", ".venv", "__pycache__",
    ".workbuddy", ".trae", ".zcode", ".github", ".gitbook",
    "_tmp", "specs",
}
# 顶层 script/ 整树不入库（AGENTS.md 明确“一律不入库”），只在根层跳过；
# 但 00-编纂规则与格式规范/01-规则/script/ 下有入库 .md，须继续扫。
SKIP_TOPLEVEL_ONLY = {"script"}


def iter_md(root: str):
    root_abs = os.path.abspath(root)
    for dirpath, dirnames, filenames in os.walk(root):
        top = os.path.abspath(dirpath) == root_abs
        skip = SKIP_DIRS if not top else SKIP_DIRS | SKIP_TOPLEVEL_ONLY
        dirnames[:] = [d for d in dirnames if d not in skip]
        for fn in filenames:
            if fn.lower().endswith(".md"):
                yield os.path.join(dirpath, fn)


def scan(root: str):
    bad = []
    undecodable = 0
    unreadable = []
    dq_bad = []
    total = 0
    for p in iter_md(root):
        total += 1
        # os.walk 与 open 之间的窗口内文件可能被并发清理删除
        # （script/ 下曾出现文件名含制表符的异常命名件），此时须计数披露而非裸抛——
        # 裸抛会让整件门禁退出码不确定、等于全库直角引号防线空转。
        try:
            with open(p, "rb") as fh:
                raw = fh.read()
        except OSError as exc:
            unreadable.append((os.path.relpath(p, root), type(exc).__name__))
            continue
        try:
            text = raw.decode("utf-8-sig")
        except UnicodeDecodeError:
            undecodable += 1
            continue
        n = sum(text.count(c) for c in CORNER)
        if n:
            bad.append((os.path.relpath(p, root), n))
        dq = text.count("\u201c") - text.count("\u201d")
        sq = text.count("\u2018") - text.count("\u2019")
        if dq or sq:
            dq_bad.append((os.path.relpath(p, root), dq, sq))
    return total, bad, undecodable, unreadable, dq_bad


def selftest() -> int:
    import builtins
    with tempfile.TemporaryDirectory() as td:
        good = os.path.join(td, "good.md")
        badf = os.path.join(td, "bad.md")
        with open(good, "w", encoding="utf-8", newline="\n") as fh:
            fh.write("中文引号“成对”与‘单引’。\n")
        with open(badf, "w", encoding="utf-8", newline="\n") as fh:
            fh.write("夹具\u300c直角\u300d与\u300e白双\u300f。\n")
        total, bad, und, unread, _ = scan(td)
        assert total == 2, total
        assert len(bad) == 1 and bad[0][1] == 4, bad
        assert und == 0 and not unread
        # 豁免面负向自证：删去坏夹具后须 PASS
        os.remove(badf)
        total, bad, und, unread, _ = scan(td)
        assert total == 1 and not bad and not und and not unread
        # OSError 分支非空自证：open 抛 FileNotFoundError 须计数披露而非崩溃
        real_open = builtins.open
        builtins.open = lambda *a, **k: (_ for _ in ()).throw(
            FileNotFoundError(2, "No such file or directory"))
        try:
            total, bad, und, unread, dq = scan(td)
        finally:
            builtins.open = real_open
        assert total == 1 and not bad and und == 0, (total, bad, und)
        assert len(unread) == 1 and unread[0][1] == "FileNotFoundError", unread
        assert not dq, "不可读文件不得进入弯引号统计"
    print("selftest PASS（夹具 4 枚直角引号命中、删除后归零、OSError 计数披露不崩溃）")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=None, help="限定扫描子树（默认仓库根）")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--json", action="store_true", help="输出 JSON 摘要")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    root = args.root or os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    total, bad, und, unreadable, dq_bad = scan(root)
    ok = not bad
    summary = {
        "gate": "第二十四件 audit_md_quote_glyphs",
        "root": root,
        "md_files": total,
        "undecodable": und,
        "unreadable": len(unreadable),
        "unreadable_note": "INFO only：walk 与 open 之间被并发清理者计数披露，"
                           "不阻断判据（否则会裸抛异常、全库防线空转）",
        "unreadable_sample": unreadable[:20],
        "T1_corner_files": len(bad),
        "T1_corner_chars": sum(n for _, n in bad),
        "T1_sample": bad[:30],
        "T2_pair_imbalance_files": len(dq_bad),
        "T2_pair_imbalance_open_delta": sum(x[1] for x in dq_bad),
        "T2_note": "INFO only：批前既有失衡（OCR 档案为主）不属本件判据，另案处置",
    }
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=1))
    else:
        print(f"扫描 .md {total} 个（不可解码 {und}、不可读 {len(unreadable)}）")
        if unreadable:
            for rel, kind in unreadable[:10]:
                print(f"   INFO 不可读 {rel}（{kind}，披露不阻断）")
        print(f"T1 直角引号：{summary['T1_corner_chars']} 处 / {summary['T1_corner_files']} 文件 -> {'PASS' if ok else 'FAIL'}")
        for rel, n in bad[:20]:
            print(f"   FAIL {rel} ×{n}")
        print(f"T2 弯引号净差披露（INFO）：{summary['T2_pair_imbalance_files']} 文件，开引号净差 {summary['T2_pair_imbalance_open_delta']}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
