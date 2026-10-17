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
T1 **直角引号清零**：全库 `*.md`（跳过 `.git`／`node_modules` 等；UTF-8 不可解码者
    计数并披露）中六个码位（U+300C U+300D U+300E U+300F U+FF62 U+FF63）出现即 FAIL。
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
SKIP_DIRS = {".git", "node_modules", ".venv", "__pycache__"}


def iter_md(root: str):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn.lower().endswith(".md"):
                yield os.path.join(dirpath, fn)


def scan(root: str):
    bad = []
    undecodable = 0
    dq_bad = []
    total = 0
    for p in iter_md(root):
        total += 1
        try:
            text = open(p, "rb").read().decode("utf-8-sig")
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
    return total, bad, undecodable, dq_bad


def selftest() -> int:
    with tempfile.TemporaryDirectory() as td:
        good = os.path.join(td, "good.md")
        badf = os.path.join(td, "bad.md")
        with open(good, "w", encoding="utf-8", newline="\n") as fh:
            fh.write("中文引号“成对”与‘单引’。\n")
        with open(badf, "w", encoding="utf-8", newline="\n") as fh:
            fh.write("夹具\u300c直角\u300d与\u300e白双\u300f。\n")
        total, bad, und, _ = scan(td)
        assert total == 2, total
        assert len(bad) == 1 and bad[0][1] == 4, bad
        assert und == 0
        # 豁免面负向自证：删去坏夹具后须 PASS
        os.remove(badf)
        total, bad, und, _ = scan(td)
        assert total == 1 and not bad and not und
    print("selftest PASS（夹具 4 枚直角引号命中、删除后归零）")
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
    total, bad, und, dq_bad = scan(root)
    ok = not bad
    summary = {
        "gate": "第二十四件 audit_md_quote_glyphs",
        "root": root,
        "md_files": total,
        "undecodable": und,
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
        print(f"扫描 .md {total} 个（不可解码 {und}）")
        print(f"T1 直角引号：{summary['T1_corner_chars']} 处 / {summary['T1_corner_files']} 文件 -> {'PASS' if ok else 'FAIL'}")
        for rel, n in bad[:20]:
            print(f"   FAIL {rel} ×{n}")
        print(f"T2 弯引号净差披露（INFO）：{summary['T2_pair_imbalance_files']} 文件，开引号净差 {summary['T2_pair_imbalance_open_delta']}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
