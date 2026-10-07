#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第十七件·改号同源守卫（2026-10-07 立，丁-1；87 号文 R-3 的工程化）。

对象：`重构2026/data/outline.txt`（**内容源**级——不等装配，改后立即回路）。

三种模式：
  A) 静态自检（默认）：逐卷核「章题号 ↔ 节号前缀」同源一致——
     章题 `## 第 N 章` 之下的节行须以 `- N.` 起首；出现他章号前缀即 FAIL
     （1d-1 实测缺陷类：章号顺延而节号未随动，如 `## 第 6 章 …` 下仍为 `7.1`）。
  B) 变更守卫 --renamed "旧→新"（可多条）：给定改号映射（如 `第38卷第10章→第38卷第11章`），
     扫全库报告旧号在**引用面**的残留（「第X卷第Y章」汉字/阿拉伯形态），
     同行含历史层豁免词（旧/原/历史/冻结/迁移/曾/已废）者记豁免；残留非豁免项即 FAIL。
  C) --selftest：临时夹具注入两类缺陷（章节错位＋引用残留）须全数拦下。

用法：
    python audit_renumber_guard.py                     # A 模式
    python audit_renumber_guard.py --renamed "第38卷第10章→第38卷第11章" [--renamed ...]
    python audit_renumber_guard.py --selftest
"""
import argparse
import io
import re
import sys
import tempfile
from pathlib import Path

BASE = Path(__file__).resolve().parents[3]  # d:/librebsd
SRC = BASE / "08-核查报告与多轮复核" / "重构2026" / "data" / "outline.txt"

CN = "零一二三四五六七八九十百"
def cn2int(x):
    if x == "百":
        return 100
    if "十" in x:
        p = x.split("十")
        a = CN.index(p[0]) if p[0] else 1
        b = CN.index(p[1]) if p[1] else 0
        return a * 10 + b
    return CN.index(x)

VOL_RE = re.compile(r"^# 第([" + CN + r"]+)卷")
CH_RE = re.compile(r"^## 第\s*(\d+)\s*章")
SEC_RE = re.compile(r"^- (\d+)\.(\d+) ")
HIST = re.compile(r"(历史层|自原|原卷|原第|旧第|冻结|待考|已废|演进|口径由)")


def check_static(lines):
    """A 模式：卷内「章题号 ↔ 节号前缀」同源检查。"""
    bad = []
    cur_vol = None
    cur_ch = None
    for i, ln in enumerate(lines, 1):
        m = VOL_RE.match(ln)
        if m:
            cur_vol = cn2int(m.group(1)); cur_ch = None
            continue
        m = CH_RE.match(ln)
        if m:
            cur_ch = int(m.group(1))
            continue
        m = SEC_RE.match(ln)
        if m and cur_ch is not None:
            sec_ch = int(m.group(1))
            if sec_ch != cur_ch:
                bad.append((i, "卷 %s：章题「第 %d 章」之下出现 %s.%s 节" % (cur_vol, cur_ch, m.group(1), m.group(2))))
    return bad


def check_renamed(lines, mappings):
    """B 模式：改号映射的引用残留检查。mappings=[(vol, ch_old), ...]"""
    bad = []
    for vol, ch in mappings:
        pats = [
            re.compile(r"第[" + CN + r"]+卷第\s*%d\s*章" % ch),   # 形态一（卷号任意）
            re.compile(r"卷\s*%d\s*第\s*%d\s*章" % (vol, ch)),
        ]
        for i, ln in enumerate(lines, 1):
            for p in pats:
                for m in p.finditer(ln):
                    frag = m.group(0)
                    # 同卷号校验（形态一需核卷号是否为目标卷）
                    if p is pats[0]:
                        vm = re.match(r"第([" + CN + r"]+)卷", frag)
                        if vm and cn2int(vm.group(1)) != vol:
                            continue
                    st = ln[max(0, m.start() - 25):m.end() + 25]
                    if HIST.search(st):
                        continue
                    bad.append((i, frag, ln[:90]))
    return bad


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--renamed", action="append", default=[],
                    help='改名映射，形如 "第38卷第10章→第38卷第11章"（可多条）')
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        # 夹具一：章节错位
        t1 = tempfile.mkdtemp(prefix="rg17a_")
        f1 = Path(t1) / "outline.txt"
        f1.write_text("# 第一卷 测试\n## 第 6 章 甲\n- 7.1 错位节\n", encoding="utf-8")
        b1 = check_static(io.open(f1, encoding="utf-8").read().split("\n"))
        assert len(b1) == 1 and b1[0][0] == 3, b1
        # 夹具二：引用残留（非豁免）
        t2 = tempfile.mkdtemp(prefix="rg17b_")
        lines2 = ["- x @@〔分工·迁移：与第三十八卷第 10 章分工：本体见彼章〕",
                  "- y @@〔分工·迁移：原第三十八卷第 10 章之内容分归各处〕"]
        b2 = check_renamed(lines2, [(38, 10)])
        assert len(b2) == 1 and b2[0][0] == 1, b2  # 第 2 行含「原」→豁免
        print("第十七件 --selftest：PASS（章节错位＋引用残留两夹具全数拦下；历史层豁免正确）")
        return 0

    s = io.open(SRC, encoding="utf-8").read()
    lines = s.split("\n")

    bad_a = check_static(lines)
    print("第十七件·改号同源守卫 ｜ A 静态：章节错位 %d 处" % len(bad_a))
    for i, msg in bad_a:
        print("  ❌ L%d %s" % (i, msg))

    bad_b = []
    if args.renamed:
        maps = []
        for spec in args.renamed:
            m = re.match(r"第([0-9]+)卷第([0-9]+)章", spec)
            assert m, "映射格式：%s" % spec
            maps.append((int(m.group(1)), int(m.group(2))))
        bad_b = check_renamed(lines, maps)
        print("第十七件·改号同源守卫 ｜ B 映射 %s：引用残留 %d 处" % (maps, len(bad_b)))
        for i, frag, ln in bad_b:
            print("  ❌ L%d %s | %s" % (i, frag, ln))

    if bad_a or bad_b:
        print("第十七件：FAIL", file=sys.stderr)
        return 1
    print("第十七件：PASS（A 静态 0；B %s）" % ("未启用" if not args.renamed else "0 残留"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
