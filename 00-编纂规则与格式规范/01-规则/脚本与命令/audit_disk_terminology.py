#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""audit_disk_terminology.py —— 磁盘层门禁·术语件（2026-10-02 立，P2-11 甲案）。

设立缘由
--------
磁盘层 `05-卷册大纲/` 长期缺门禁（九件门禁全部面向目录页 `index.html`）。
2026-10-02 主理人裁定 P2-11 甲案（磁盘层＝活跃镜像 → 逐项施工 ＋ 先建磁盘层门禁），
本件为磁盘层门禁第一件（术语）。同源问题：目录层已合规（「基础系统」0 处，统一「基本系统」），
磁盘层未同步。

判据
----
**在效面**内精确词「基础系统」命中 = 0。

在效面定义 = `05-卷册大纲/` 全树 **减去**两类**有意识豁免**（非遗漏）：
  E1 备份件：文件名含 `.preback` / `.bak` / `.pre-` / `.pre_b` —— 快照性质，保留原值
  E2 历史复核登记件：`目录审阅复核纠正对照表-*.md` —— 记录当时的修订建议，不得追改
豁免件仅计 INFO，不判 FAIL。

范围锁定：仅精确词「基础系统」。**不含**「基础设施」「法律基础」等合法合成词
（后者是 2026-10-02 首步盘点「339 文件」口径的误混来源）。

防再生：写盘统一入口 `wo007_idempotency.write_guard()` 已注入 `normalize_terms()`
（基础系统→基本系统），故经该入口的写入不再产出旧词；本件为兜底检验。

用法
----
    python audit_disk_terminology.py              # 0 通过 / 1 命中 / 2 依赖缺失
    python audit_disk_terminology.py --list       # 打印在效面口径与豁免
    python audit_disk_terminology.py --selftest   # 判据非空：造缺陷夹具须 FAIL

依赖：仅标准库。
"""
import argparse
import os
import pathlib
import re
import shutil
import sys
import tempfile

sys.stdout.reconfigure(encoding="utf-8")

REPO = pathlib.Path(__file__).resolve().parents[3]
OUTLINE = REPO / "05-卷册大纲"
TARGET = "基础系统"

BACKUP_RE = re.compile(r"\.(preback|bak|pre[-_])", re.I)
EXEMPT_NAME_RE = re.compile(r"^目录审阅复核纠正对照表-.*\.md$")


def is_exempt(name):
    """返回豁免类名或 None。"""
    if BACKUP_RE.search(name):
        return "E1-backup"
    if EXEMPT_NAME_RE.match(name):
        return "E2-review-record"
    return None


def run(root: pathlib.Path):
    """扫描 root，返回 (hits, exempt_agg)。hits = [(relpath, count)] 在效面命中。"""
    hits = []
    exempt = {}
    for dirpath, _, files in os.walk(root):
        for f in files:
            fp = os.path.join(dirpath, f)
            try:
                text = pathlib.Path(fp).read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            n = text.count(TARGET)
            if not n:
                continue
            ex = is_exempt(f)
            if ex:
                exempt.setdefault(ex, [0, 0])
                exempt[ex][0] += 1
                exempt[ex][1] += n
            else:
                hits.append((os.path.relpath(fp, root).replace("\\", "/"), n))
    return hits, exempt


def _report(root, hits, exempt):
    print("=" * 72)
    print("磁盘层门禁·术语件（%s）" % TARGET)
    print("=" * 72)
    print("对象目录：%s" % root)
    print("判据：在效面命中 = 0")
    tot = sum(n for _, n in hits)
    print("-" * 72)
    if not hits:
        print("  [PASS] 在效面命中 = 0")
    else:
        print("  [FAIL] 在效面命中 %d 处 / %d 文件：" % (tot, len(hits)))
        for rel, n in sorted(hits, key=lambda x: -x[1]):
            print("      %3d  %s" % (n, rel))
    print("-" * 72)
    print("  豁免（INFO，非在效）：")
    for ex, (nf, nh) in sorted(exempt.items()):
        print("      %-18s 文件 %3d ／ 命中 %4d" % (ex, nf, nh))
    if not exempt:
        print("      （无）")
    print("-" * 72)
    print("  合计 %d 项，FAIL %d 项" % (1, 0 if not hits else 1))
    return 0 if not hits else 1


def cmd_selftest():
    """判据非空：造「在效面含旧词」与「仅备份件含旧词」两夹具，须分别 FAIL / PASS。"""
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="diskterm_"))
    try:
        # 夹具A：在效面含旧词（须 FAIL）
        a = tmp / "A"
        a.mkdir()
        (a / "第01章-概述.md").write_text("FreeBSD 基础系统 x\n", encoding="utf-8")
        ha, _ = run(a)
        # 夹具B：仅备份件/复核登记件含旧词（须 PASS，且豁免 2 类）
        b = tmp / "B"
        b.mkdir()
        (b / "x.md.bak_t1").write_text("基础系统\n", encoding="utf-8")
        (b / "目录审阅复核纠正对照表-2026-09-23.md").write_text("基础系统\n", encoding="utf-8")
        (b / "clean.md").write_text("基本系统\n", encoding="utf-8")
        hb, eb = run(b)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    ok = bool(ha) and not hb and set(eb) == {"E1-backup", "E2-review-record"}
    print("夹具A（在效面含旧词）命中 %d 处（须 >0）" % sum(n for _, n in ha))
    print("夹具B（仅豁免件含旧词）命中 %d 处（须 =0）；豁免类 %s" % (sum(n for _, n in hb), sorted(eb)))
    if ok:
        print("  ✅ 判据非空：缺陷命中、豁免正确")
        return 0
    print("  ❌ 判据可能为空", file=sys.stderr)
    return 1


def main():
    ap = argparse.ArgumentParser(description="磁盘层门禁·术语件")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--root", default=str(OUTLINE))
    args = ap.parse_args()

    if args.selftest:
        return cmd_selftest()

    root = pathlib.Path(args.root)
    if args.list:
        print("对象：%s" % root)
        print("判据：在效面「%s」= 0" % TARGET)
        print("豁免：E1 备份件（.preback/.bak/.pre-/.pre_b）｜E2 历史复核登记件（目录审阅复核纠正对照表-*.md）")
        return 0

    if not root.exists():
        print("依赖缺失：%s" % root, file=sys.stderr)
        return 2
    hits, exempt = run(root)
    return _report(root, hits, exempt)


if __name__ == "__main__":
    sys.exit(main())
