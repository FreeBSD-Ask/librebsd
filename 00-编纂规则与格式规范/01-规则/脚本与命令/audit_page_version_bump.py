#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第十八件·页面版本号递增兜底门禁（2026-10-07 立）。

背景：116c 立「页面版本号规范」（X.Y.Z＝结构世代.结构批次.修订批次）并明定
「版本号变更与口径变更同批落账」——但 116c 后各批（117b/118/119d 系/121 系…）
均未执行递增，属「已文档化 ≠ 已生效」缺口（2026-10-07 主理人抓出「版本号没变」）。
本件以 git 为参照做兜底：HEAD 版 index.html vs 工作区 index.html——
**口径三元组或注数发生变化、而版本号未变 → FAIL**（提示本批须递增版本号）。

用法：
    python audit_page_version_bump.py            # 兜底检查
    python audit_page_version_bump.py --selftest # 判据非空自证（两版夹具）
"""
import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path

BASE = Path(__file__).resolve().parents[3]  # d:/librebsd
REL = "08-核查报告与多轮复核/重构2026/index.html"
FULL = BASE / REL

VER_RE = re.compile(r'class="page-version"[^>]*>(\d+\.\d+\.\d+)<')
METRIC_RE = re.compile(r"(\d+ 卷 \d+ 章 \d+ 节)")


def extract(text):
    v = VER_RE.search(text)
    m = METRIC_RE.search(text)
    notes = text.count('class="src"')
    return (v.group(1) if v else None, m.group(1) if m else None, notes)


def judge(old, new):
    """返回 (ok, reason)。old/new＝(ver, metric, notes)。"""
    ov, om, on = old
    nv, nm, nn = new
    if nv is None or nm is None:
        return False, "版本号或口径串缺失"
    changed = (om != nm) or (on != nn)
    if changed and nv == ov:
        return False, "结构/注数已变（口径 %s→%s，注 %s→%s）而版本号未递增（仍 %s）" % (om, nm, on, nn, nv)
    if not changed and nv != ov:
        return True, "版本号已递增 %s→%s（无结构变化——允许，如校准批）" % (ov, nv)
    return True, "一致（口径 %s／注 %s／版本 %s）" % (nm, nn, nv)


def head_text():
    r = subprocess.run(["git", "show", "HEAD:" + REL], cwd=str(BASE),
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        return None
    return r.stdout


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        old = ("1.0.0", "54 卷 450 章 3667 节", 884)
        new_bad = ("1.0.0", "54 卷 451 章 3667 节", 885)   # 变了但版本未动 → 应 FAIL
        new_ok = ("1.9.0", "54 卷 451 章 3667 节", 885)    # 已递增 → PASS
        ok1, _ = judge(old, new_bad)
        ok2, _ = judge(old, new_ok)
        assert (not ok1) and ok2, (ok1, ok2)
        # 提取器夹具
        t = '<span class="page-version" title="x">1.9.0</span> 统计：54 卷 451 章 3667 节'
        v, m, n = extract(t)
        assert v == "1.9.0" and m == "54 卷 451 章 3667 节", (v, m)
        print("第十八件 --selftest：PASS（未递增须 FAIL／已递增 PASS／提取器正确）")
        return 0

    h = head_text()
    if h is None:
        print("第十八件：SKIP（无 git HEAD 参照——首次提交或非 git 环境）")
        return 0
    old = extract(h)
    new = extract(FULL.read_text(encoding="utf-8"))
    ok, reason = judge(old, new)
    if not ok:
        print("第十八件：FAIL——" + reason, file=sys.stderr)
        return 1
    print("第十八件：PASS——" + reason)
    return 0


if __name__ == "__main__":
    sys.exit(main())
