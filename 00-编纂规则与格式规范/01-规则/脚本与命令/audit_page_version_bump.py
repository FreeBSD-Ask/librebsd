#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第十八件·页面版本号递增兜底门禁（2026-10-07 立）。

背景：116c 立「页面版本号规范」并明定「版本号变更与口径变更同批落账」——但 116c 后各批
（117b/118/119d 系/121 系…）均未执行递增，属「已文档化 ≠ 已生效」缺口（2026-10-07 主理人抓出
「版本号没变」）。2026-10-10（128 号文 T-6）版本号格式由 `X.Y.Z`（结构世代.结构批次.修订批次）
改为 UTC+8 时间戳 `YYYY.MM.DD-HH:MM`。本件以 git 为参照做兜底：HEAD 版 index.html vs 工作区
index.html——**口径三元组或注数发生变化、而版本号未变 → FAIL**（提示本批须刷新版本时间戳）。

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

VER_RE = re.compile(
    r'class="page-version"[^>]*>('
    r'\d{4}\.\d{2}\.\d{2}-\d{2}:\d{2}'   # 新：UTC+8 时间戳 YYYY.MM.DD-HH:MM（2026-10-10 起）
    r'|\d+\.\d+\.\d+'                    # 旧：X.Y.Z（过渡期 HEAD 兼容）
    r')<'
)
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
        old = ("3.0.20", "65 卷 469 章 3467 节", 1194)
        new_bad = ("3.0.20", "65 卷 470 章 3467 节", 1194)             # 变了但版本未动 → 应 FAIL
        new_ok = ("2026.10.10-14:28", "65 卷 470 章 3467 节", 1195)   # 已刷新 → PASS
        ok1, _ = judge(old, new_bad)
        ok2, _ = judge(old, new_ok)
        assert (not ok1) and ok2, (ok1, ok2)
        # 提取器夹具：旧形 X.Y.Z 与时间戳新形均须可提取（过渡态 HEAD=旧形／工作区=时间戳）
        t_old = '<span class="page-version" title="x">3.0.20</span> 统计：65 卷 469 章 3467 节'
        t_new = '<span class="page-version" title="x">2026.10.10-14:28</span> 统计：65 卷 470 章 3467 节'
        vo, mo, _ = extract(t_old)
        vn, mn, _ = extract(t_new)
        assert vo == "3.0.20" and mo == "65 卷 469 章 3467 节", (vo, mo)
        assert vn == "2026.10.10-14:28" and mn == "65 卷 470 章 3467 节", (vn, mn)
        print("第十八件 --selftest：PASS（未刷新须 FAIL／已刷新 PASS／旧形与时间戳双形态提取器正确）")
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
