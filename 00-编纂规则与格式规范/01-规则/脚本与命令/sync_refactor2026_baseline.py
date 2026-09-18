#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync_refactor2026_baseline.py — 重构2026 大纲目录口径同步脚本（2026-09-08 新增固定脚本）

用途：
  `08-核查报告与多轮复核/重构2026/index.html` 是重构2026 现行大纲目录（唯一权威口径来源），
  其页首 `doc-metrics` 块（总卷数/总章数/总节数）为机器可读基准。本脚本检测口径声明是否与
  权威基准漂移，并仅同步「机器维护标记块」内的基准行。
  扫描范围（2026-09-08 扩展）：`重构2026/*.md` ＋ 根 `CLAUDE.md` ＋ `00-编纂规则与格式规范/01-规则/*.md`
  ——后两者同样手写现行口径，仅扫 重构2026 会漏检并在每次目录变更后重新漂移。

规则依据：
  `00-编纂规则与格式规范/01-规则/流程规则.md`「重构大纲目录口径同步规则（2026-09-08 新增）」小节。

用法：
  python sync_refactor2026_baseline.py --check    # 检测漂移（默认），存在未处置漂移时退出码 1
  python sync_refactor2026_baseline.py --sync      # 仅重写标记块内基准行 + BEGIN 行日期戳
  python sync_refactor2026_baseline.py --list      # 打印当前权威基准
  可选 --verbose：列出全部豁免命中（历史快照/映射数据基线）

检测三维度：
  维度一 口径三元组（N卷M章K节）：
    marker-drift   标记块内声明 ≠ 权威基准（--sync 自动修复）
    present-stale  标记块外、现在时态现行口径声明（适用范围/现行大纲目录/本书全部…）≠ 权威基准（需人工）
    exempt         其余旧口径命中（带日期裁决/审计/映射数据基线等历史事实本体）——永不自动改写
  维度二 ref-stale    指向已归档目录文件（大纲目录-12卷.md / S-me目录预览）且同行无归档标注、文件头无日期/历史声明（需人工补标注或确认历史件）
  维度三 pending-stale 未消解的 ⬜ 待填单元格（`| ⬜ |`）且文件未声明被取代（需人工补取代声明或消解）
  维度二/三的文件级豁免：头部 12 行含日期/复核日期/历史记录/已被取代/已清零/仅作历史等声明的，整体豁免（历史存档件不追改）。

约定：
  标记块格式（独占行）：
    <!-- BEGIN 口径基准（脚本自动维护，勿手改数字） -->
    <基准声明行>
    <!-- END 口径基准（脚本自动维护） -->
  历史注记/快照类文件不加标记块；markdown 表格行不加标记块（会破坏表格结构）。
"""
import argparse
import re
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
INDEX_HTML = REPO / "08-核查报告与多轮复核" / "重构2026" / "index.html"
TARGET_DIR = REPO / "08-核查报告与多轮复核" / "重构2026"
# 口径声明外溢位置（2026-09-08 扩展）：根协作指南与规则目录同样手写现行口径，
# 仅扫 重构2026/*.md 会漏检，导致每次目录变更后这两处重新漂移。
EXTRA_TARGETS = [REPO / "CLAUDE.md"] + sorted(
    (REPO / "00-编纂规则与格式规范" / "01-规则").glob("*.md"))


def target_files():
    return sorted(TARGET_DIR.glob("*.md")) + [p for p in EXTRA_TARGETS if p.exists()]

# 标记块必须为独占行（规则约定），故整行锚定：
# 否则规则文件里「举例说明标记块语法」的行会误触发状态机，把其后全文当成块内内容。
BEGIN_RE = re.compile(r"^\s*<!--\s*BEGIN 口径基准（脚本自动维护[^>]*?）\s*-->\s*$")
END_RE = re.compile(r"^\s*<!--\s*END 口径基准（脚本自动维护）\s*-->\s*$")
TRIPLE_RE = re.compile(r"(\d{1,3})\s*卷\s*(\d{1,4})\s*章(?:\s*([\d,]{2,7})\s*节)?")
# 现在时态现行口径声明（标记块外仍出现即视为漂移，需人工）
PRESENT_RE = re.compile(r"(适用范围|本书全部|全书全部|现行大纲目录|现行目录|当前大纲)")
# 「另一套基准」前缀（磁盘实况/冻结基准/映射表数据基线）——同行并列出现时不属目录页口径，豁免。
# 用于 CLAUDE.md 一行内并列 19卷355章（磁盘实况）＋12卷181章（冻结基准）＋23卷237章N节（现行目录）的情形。
OTHER_BASE_RE = re.compile(r"(磁盘实况|冻结基准|数据基线|旧\s*\d+\s*卷|12\s*卷\s*181|19\s*卷\s*355|355\s*章口径)")
# 历史标记（修订记录/数据基线声明/已同步/取代/归档/演进史）——命中即豁免，属历史事实本体
HIST_RE = re.compile(r"(修订（|已同步|数据基线|→|已归档|已被取代|取代并归档|历史记录|演进为|口径由|下称「目录页」)")
# 维度二：指向已归档目录文件的引用（同行无归档标注即漂移）
ARCHIVED_REF_RE = re.compile(r"大纲目录-12卷\.md|S-me目录预览|S-me\.md")
ARCHIVE_NOTED_RE = re.compile(r"(已归档|已被取代|取代并归档|归档于|已自本目录|被本目录|随.*归档|原指向)")
# 维度三：未消解的待填标记（独立单元格 `| ⬜ |`），须文件级有取代/存档声明方可豁免
SUPERSEDED_HEAD_RE = re.compile(r"(已被取代|已清零|历史存档|不再填写|仅作历史)")
# 文件级历史声明（头部含日期/历史记录/复核日期/生成日期）→ 维度二整文件豁免
HIST_FILE_HEAD_RE = re.compile(
    r"(日期.{0,4}2026-|复核日期|生成日期|制定人|修订记录|本报告为|属历史记录|历史存档|已被取代|已清零|仅作)")


def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def write_text(p: Path, s: str) -> None:
    # UTF-8 无 BOM、LF
    p.write_bytes(s.replace("\r\n", "\n").encode("utf-8"))


def parse_authoritative() -> tuple[int, int, int]:
    html = read_text(INDEX_HTML)
    m = re.search(r"总卷数</span><strong[^>]*>\s*(\d+)\s*</strong>", html)
    n = re.search(r"总章数</span><strong[^>]*>\s*(\d+)\s*</strong>", html)
    s = re.search(r"总节数</span><strong[^>]*>\s*(\d+)\s*</strong>", html)
    if not (m and n and s):
        sys.exit("错误：无法从 index.html 解析 doc-metrics 权威三元组")
    return int(m.group(1)), int(n.group(1)), int(s.group(1))


def parse_jsonld_metrics():
    """T10.2：从 index.html 的 JSON-LD 块解析「卷数/章数/节数」。

    返回 (vol, ch, sec)；块缺失或字段不全返回 None。
    口径依据：index.html 页首 `<script type="application/ld+json">` 的
    additionalProperty（name=卷数/章数/节数, value=N）。
    """
    html = read_text(INDEX_HTML)
    m = re.search(r"<script[^>]*application/ld\+json[^>]*>(.*?)</script>", html, re.S)
    if not m:
        return None
    blob = m.group(1)
    def grab(name: str):
        mm = re.search(r'"name"\s*:\s*"%s"\s*,\s*"value"\s*:\s*(\d+)' % name, blob)
        return int(mm.group(1)) if mm else None
    vol, ch, sec = grab("卷数"), grab("章数"), grab("节数")
    if vol is None or ch is None or sec is None:
        return None
    return vol, ch, sec


def fmt(v: tuple[int, int, int]) -> str:
    return f"{v[0]} 卷 {v[1]} 章 {v[2]} 节"


def scan(v: tuple[int, int, int]):
    """返回 (marker_drift, present_stale, exempt, marker_ok, ref_stale, pending_stale)。"""
    drift, stale, exempt, ok, ref_stale, pending_stale = [], [], [], [], [], []
    for fp in target_files():
        text = read_text(fp)
        lines = text.split("\n")
        head = "\n".join(lines[:12])
        superseded = bool(SUPERSEDED_HEAD_RE.search(head))
        hist_file = bool(HIST_FILE_HEAD_RE.search(head))
        in_block = False
        for i, ln in enumerate(lines, 1):
            if BEGIN_RE.search(ln):
                in_block = True
                continue
            if END_RE.search(ln):
                in_block = False
                continue
            # 口径三元组判定：一行可含多个不同基准（如 CLAUDE.md 同行并列
            # 「磁盘实况 19卷355章」「冻结基准 12卷181章」「现行大纲目录 23卷237章N节」），
            # 须逐个匹配按其前缀窗口分类，不能只取首个匹配，否则误判为漂移。
            for tm in TRIPLE_RE.finditer(ln):
                declared = (int(tm.group(1)), int(tm.group(2)),
                            int(tm.group(3).replace(",", "")) if tm.group(3) else None)
                same = declared[0] == v[0] and declared[1] == v[1] and (
                    declared[2] is None or declared[2] == v[2])
                prefix = ln[max(0, tm.start() - 48):tm.start()]
                if in_block:
                    (ok if same else drift).append((fp, i, ln.strip(), declared))
                elif OTHER_BASE_RE.search(prefix):
                    # 磁盘实况/冻结基准/映射表数据基线等「另一套基准」，非目录页口径
                    exempt.append((fp, i, ln.strip()[:120], declared))
                elif PRESENT_RE.search(ln) and not HIST_RE.search(ln):
                    (ok if same else stale).append((fp, i, ln.strip(), declared))
                else:
                    exempt.append((fp, i, ln.strip()[:120], declared))
            # 维度二：指向已归档目录文件但同行无归档标注（带日期历史文件整体豁免）
            if ARCHIVED_REF_RE.search(ln) and not ARCHIVE_NOTED_RE.search(ln) and not hist_file:
                ref_stale.append((fp, i, ln.strip()[:150]))
            # 维度三：未消解 ⬜ 待填标记（仅独立单元格 `| ⬜ |`，说明句/匹配列定义不算待办）且文件未声明被取代
            # 先剔除行内代码段：规则文件会以 `| ⬜ |` 形式描述该标记本身，属文档而非待办
            plain = re.sub(r"`[^`]*`", "", ln)
            if re.search(r"\|\s*⬜\s*\|", plain) and not superseded:
                pending_stale.append((fp, i, ln.strip()[:150]))
    return drift, stale, exempt, ok, ref_stale, pending_stale


def cmd_list(v):
    print(f"权威基准（index.html doc-metrics）：{fmt(v)}")


def cmd_check(v, verbose: bool):
    drift, stale, exempt, ok, ref_stale, pending_stale = scan(v)
    print(f"权威基准：{fmt(v)}")
    print(f"标记块内声明：一致 {len(ok)} 处")
    if drift:
        print(f"❌ marker-drift（标记块内过时，运行 --sync 修复）：{len(drift)} 处")
        for fp, i, ln, d in drift:
            print(f"  {fp.name} L{i}: {ln[:120]}")
    if stale:
        print(f"❌ present-stale（标记块外现在时态旧口径，需人工）：{len(stale)} 处")
        for fp, i, ln, d in stale:
            print(f"  {fp.name} L{i}: {ln[:120]}")
    if ref_stale:
        print(f"❌ ref-stale（指向已归档目录文件且无归档标注，需人工）：{len(ref_stale)} 处")
        for fp, i, ln in ref_stale[:20]:
            print(f"  {fp.name} L{i}: {ln[:120]}")
        if len(ref_stale) > 20:
            print(f"  ... +{len(ref_stale) - 20} more")
    if pending_stale:
        print(f"❌ pending-stale（未消解 ⬜ 待填标记且无取代声明，需人工）：{len(pending_stale)} 处")
        for fp, i, ln in pending_stale[:20]:
            print(f"  {fp.name} L{i}: {ln[:120]}")
        if len(pending_stale) > 20:
            print(f"  ... +{len(pending_stale) - 20} more")
    print(f"豁免命中（历史快照/数据基线，不处置）：{len(exempt)} 处")
    if verbose:
        for fp, i, ln, d in exempt:
            print(f"  ~ {fp.name} L{i}: {ln}")
    # T10.2：JSON-LD 口径声明纳入漂移检测（index.html 内嵌 application/ld+json）
    jsonld = parse_jsonld_metrics()
    if jsonld is None:
        print("❌ jsonld-missing（index.html 未找到 application/ld+json 块或其卷/章/节字段）：需人工")
        jsonld_bad = 1
    elif jsonld != v:
        print(f"❌ jsonld-drift（JSON-LD {jsonld[0]} 卷 {jsonld[1]} 章 {jsonld[2]} 节 "
              f"≠ 权威基准 {fmt(v)}）：需同步")
        jsonld_bad = 1
    else:
        print(f"JSON-LD 口径：一致（{jsonld[0]} 卷 {jsonld[1]} 章 {jsonld[2]} 节）")
        jsonld_bad = 0
    bad = len(drift) + len(stale) + len(ref_stale) + len(pending_stale) + jsonld_bad
    print("✅ 零未处置漂移" if bad == 0 else f"⚠️ 未处置漂移 {bad} 处")
    return 1 if bad else 0


def cmd_sync(v):
    stamp = date.today().isoformat()
    changed = []
    for fp in target_files():
        text = read_text(fp)
        lines = text.split("\n")
        out, in_block, dirty = [], False, False
        for ln in lines:
            if BEGIN_RE.search(ln):
                in_block = True
                out.append(f"<!-- BEGIN 口径基准（脚本自动维护，勿手改数字，最后同步 {stamp}） -->")
                continue
            if END_RE.search(ln):
                in_block = False
                out.append(ln)
                continue
            if in_block:
                tm = TRIPLE_RE.search(ln)
                if tm:
                    repl = f"{v[0]} 卷 {v[1]} 章" + (f" {v[2]} 节" if tm.group(3) else "")
                    new = TRIPLE_RE.sub(repl, ln, count=1)
                    if new != ln:
                        dirty = True
                        changed.append((fp.name, new.strip()[:120]))
                    out.append(new)
                    continue
            out.append(ln)
        if dirty:
            write_text(fp, "\n".join(out))
    if changed:
        print(f"--sync 更新 {len(changed)} 行：")
        for name, ln in changed:
            print(f"  {name}: {ln}")
    else:
        print("--sync 无变更（标记块内已与权威基准一致，幂等）")
    return 0


def main():
    ap = argparse.ArgumentParser(description="重构2026 大纲目录口径同步")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--check", action="store_true", help="检测漂移（默认）")
    g.add_argument("--sync", action="store_true", help="仅同步标记块内基准行")
    g.add_argument("--list", action="store_true", help="打印权威基准")
    ap.add_argument("--verbose", action="store_true", help="列出全部豁免命中")
    args = ap.parse_args()
    v = parse_authoritative()
    if args.list:
        cmd_list(v)
        return 0
    if args.sync:
        return cmd_sync(v)
    return cmd_check(v, args.verbose)


if __name__ == "__main__":
    sys.exit(main())
