#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""audit_disk_terminology.py —— 磁盘层门禁·术语件＋换行件（2026-10-02 立术语，2026-10-17 并换行）。

设立缘由
--------
磁盘层 `05-卷册大纲/` 长期缺门禁（九件门禁全部面向目录页 `index.html`）。
2026-10-02 主理人裁定 P2-11 甲案（磁盘层＝活跃镜像 → 逐项施工 ＋ 先建磁盘层门禁），
本件为磁盘层门禁第一件（术语）。同源问题：目录层已合规（「基础系统」0 处，统一「基本系统」），
磁盘层未同步。

2026-10-17 并立第二判据（换行件）：实测 20 个 `.md` 以 CRLF 落盘，却因
`core.autocrlf=true` ＋ `.gitattributes` 的 `text=auto` 在 `git status` 中完全隐形——
写盘产物与检出产物均无法由 git 面发现。Windows 下 `open(path,'w',encoding='utf-8')`
默认把 `\\n` 翻成 `\\r\\n`，故换行必须由磁盘字节直接判，不能由 git 判。

判据
----
T1 **术语**：在效面内精确词「基础系统」命中 = 0。
T2 **换行**：在效面内 `.md` 含 CRLF（或孤立 CR）的文件 = 0；文档须 UTF-8 无 BOM ＋ LF。

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
    python audit_disk_terminology.py              # 0 通过 / 1 任一判据命中 / 2 依赖缺失
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


def run_eol(root: pathlib.Path):
    """换行判据：返回 (hits, exempt_agg)。hits = [(relpath, crlf_lines, lone_cr)]。

    只判 `.md`（文档体裁面）；按**字节**判，不经文本模式，避免读时被透明转换。
    """
    hits = []
    exempt = {}
    for dirpath, _, files in os.walk(root):
        for f in files:
            low = f.lower()
            # 文档面＝`.md` 及其快照改名形（`x.md.bak_t1` 等）；快照由 E1 计 INFO
            if not (low.endswith(".md") or ".md." in low):
                continue
            fp = os.path.join(dirpath, f)
            try:
                b = pathlib.Path(fp).read_bytes()
            except OSError:
                continue
            n_crlf = b.count(b"\r\n")
            n_lone = b.count(b"\r") - n_crlf
            if not (n_crlf or n_lone):
                continue
            ex = is_exempt(f)
            if ex:
                exempt.setdefault(ex, [0, 0])
                exempt[ex][0] += 1
                exempt[ex][1] += n_crlf + n_lone
            else:
                hits.append((os.path.relpath(fp, root).replace("\\", "/"), n_crlf, n_lone))
    return hits, exempt


def _report(root, hits, exempt, eol_hits, eol_exempt):
    print("=" * 72)
    print("磁盘层门禁·术语件（%s）＋换行件（CRLF）" % TARGET)
    print("=" * 72)
    print("对象目录：%s" % root)
    print("判据：T1 在效面「%s」= 0；T2 在效面 CRLF/孤立 CR 文件 = 0" % TARGET)
    tot = sum(n for _, n in hits)
    print("-" * 72)
    print("  【T1 术语】")
    if not hits:
        print("    [PASS] 在效面命中 = 0")
    else:
        print("    [FAIL] 在效面命中 %d 处 / %d 文件：" % (tot, len(hits)))
        for rel, n in sorted(hits, key=lambda x: -x[1]):
            print("        %3d  %s" % (n, rel))
    et = sum(x[1] + x[2] for x in eol_hits)
    print("  【T2 换行】")
    if not eol_hits:
        print("    [PASS] 在效面 CRLF/孤立 CR = 0")
    else:
        print("    [FAIL] 在效面 %d 文件含 CR：CRLF %d 行、孤立 CR %d 行："
              % (len(eol_hits), sum(x[1] for x in eol_hits), sum(x[2] for x in eol_hits)))
        for rel, a, b in sorted(eol_hits, key=lambda x: -(x[1] + x[2])):
            print("        CRLF %5d  孤立CR %3d  %s" % (a, b, rel))
    print("-" * 72)
    print("  豁免（INFO，非在效）：")
    merged = {}
    for src in (exempt, eol_exempt):
        for ex, (nf, nh) in src.items():
            merged.setdefault(ex, [0, 0])
            merged[ex][0] += nf
            merged[ex][1] += nh
    for ex, (nf, nh) in sorted(merged.items()):
        print("      %-18s 文件 %3d ／ 命中 %4d" % (ex, nf, nh))
    if not merged:
        print("      （无）")
    print("-" * 72)
    fails = (1 if hits else 0) + (1 if eol_hits else 0)
    print("  合计 2 项，FAIL %d 项" % fails)
    return 0 if not fails else 1


def cmd_selftest():
    """判据非空：术语与换行各造「在效面缺陷」与「仅豁免件缺陷」两夹具。

    预期：A（在效面术语）FAIL、C（在效面 CRLF）FAIL；B／D（豁免件）不计 FAIL。
    """
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
        # 夹具C：在效面 CRLF（须 FAIL）
        c = tmp / "C"
        c.mkdir()
        (c / "第02章-概述.md").write_bytes(b"line1\r\nline2\r\n")
        (c / "ok.md").write_bytes(b"line1\nline2\n")
        hc, _ = run_eol(c)
        # 夹具D：仅豁免件含 CRLF（须 PASS，豁免 2 类）
        d = tmp / "D"
        d.mkdir()
        (d / "x.md.pre-20261001").write_bytes(b"a\r\nb\r\n")
        (d / "目录审阅复核纠正对照表-2026-09-23.md").write_bytes(b"a\r\nb\r\n")
        (d / "doc.md").write_bytes(b"a\nb\n")
        hd, ed = run_eol(d)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    ok = (bool(ha) and not hb and set(eb) == {"E1-backup", "E2-review-record"}
          and bool(hc) and not hd and set(ed) == {"E1-backup", "E2-review-record"})
    print("T1 夹具A（在效面含旧词）命中 %d 处（须 >0）" % sum(n for _, n in ha))
    print("T1 夹具B（仅豁免件含旧词）命中 %d 处（须 =0）；豁免类 %s"
          % (sum(n for _, n in hb), sorted(eb)))
    print("T2 夹具C（在效面 CRLF）命中 %d 文件（须 >0）" % len(hc))
    print("T2 夹具D（仅豁免件 CRLF）命中 %d 文件（须 =0）；豁免类 %s" % (len(hd), sorted(ed)))
    if ok:
        print("  ✅ 判据非空：两类缺陷均命中、两类豁免均正确")
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
        print("判据：T1 在效面「%s」= 0；T2 在效面 .md 含 CRLF/孤立 CR = 0" % TARGET)
        print("豁免：E1 备份件（.preback/.bak/.pre-/.pre_b）｜E2 历史复核登记件（目录审阅复核纠正对照表-*.md）")
        return 0

    if not root.exists():
        print("依赖缺失：%s" % root, file=sys.stderr)
        return 2
    hits, exempt = run(root)
    eol_hits, eol_exempt = run_eol(root)
    return _report(root, hits, exempt, eol_hits, eol_exempt)


if __name__ == "__main__":
    sys.exit(main())
