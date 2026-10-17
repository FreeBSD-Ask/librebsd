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
    维度四 INFO    present-stale-blind：语义为现在时态、但 PRESENT_RE 未覆盖的旧口径行（如「现行口径 <旧三元组>」）
                   ——**只报不改判定**；升为 FAIL 须先扩 HIST_RE 豁免词表并经主理人裁定（2026-09-20 第四十一批立）
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
# 维度四（INFO 级，2026-09-20 第四十一批立）：PRESENT_RE 未覆盖、但语义上仍属「现在时态」的口径声明词。
# 缘由：52 号文／CLAUDE.md／流程规则.md／55 号文的「现行口径 <旧三元组>」因不在 PRESENT_RE 内而落入 exempt，
# 历批（第二十七至四十一批）均未察觉 —— 该盲区曾致核心规则文件的口径声明滞留「26 卷 240 章 1749 节」等旧值。
# 本维度只报 INFO、不改判定：因另有约 15 行属合法历史件（时点口径／历史提案／批准前时点等），
# 若升为 FAIL 须先扩充 HIST_RE 的豁免词表并经主理人裁定。
PRESENT_EXTRA_RE = re.compile(r"(现行口径|现行基准|当前口径)")
# 「另一套基准」前缀（磁盘实况/冻结基准/映射表数据基线）——同行并列出现时不属目录页口径，豁免。
# 用于 CLAUDE.md 一行内并列 19卷355章（磁盘实况）＋12卷181章（冻结基准）＋23卷237章N节（现行目录）的情形。
OTHER_BASE_RE = re.compile(r"(磁盘实况|冻结基准|数据基线|旧\s*\d+\s*卷|12\s*卷\s*181|19\s*卷\s*355|355\s*章口径)")
# 维度五（2026-10-17 主理人批准批立）：doc-metrics 的**独立数字形**引用——TRIPLE_RE 要求
# “N卷M章”连写，故“doc-metrics 26 卷”“doc-metrics 240 章”这类单单位引用完全漏检
# （流程规则 L1630/L1631“26 卷／240 章”实报，比三连形旧值还旧两代）。本判据捕“doc-metrics
# 附近 ≤32 字符处的单单位数字”，数值 ≠ 权威对应位且行为现在时态（PRESENT_RE／PRESENT_EXTRA）
# 且无历史豁免标记者判 dm-stale（FAIL 级，需人工）。
DM_STANDALONE_RE = re.compile(r"doc-metrics[^。\n]{0,32}?(?P<num>\d{1,4})\s*(?P<unit>[卷章节])")
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


def classify_triple(ln: str, tm, v: tuple, in_block: bool) -> str:
    """单个 TRIPLE 匹配的分类（可测单元；2026-10-17 抽出以支撑 --selftest）。

    返回 "ok" | "drift" | "stale" | "exempt" | "blind"。
    """
    declared = (int(tm.group(1)), int(tm.group(2)),
                int(tm.group(3).replace(",", "")) if tm.group(3) else None)
    same = declared[0] == v[0] and declared[1] == v[1] and (
        declared[2] is None or declared[2] == v[2])
    prefix = ln[max(0, tm.start() - 48):tm.start()]
    if in_block:
        return "ok" if same else "drift"
    if OTHER_BASE_RE.search(prefix):
        return "exempt"
    if PRESENT_RE.search(ln) and not HIST_RE.search(ln):
        return "ok" if same else "stale"
    if (not same) and PRESENT_EXTRA_RE.search(ln) and not HIST_RE.search(ln):
        return "blind"
    return "exempt"


def classify_dm_standalone(ln: str, v: tuple) -> bool:
    """维度五（2026-10-17 主理人批准批立）：doc-metrics **独立数字形**判定。

    TRIPLE_RE 要求“N卷M章”连写，故“doc-metrics 26 卷”“doc-metrics 240 章”这类
    单单位引用完全漏检（流程规则“26 卷／240 章”实报，比三连形旧值还旧两代）。
    本判据捕“doc-metrics 附近 ≤32 字符处的单单位数字”，数值 ≠ 权威对应位、
    行为现在时态（PRESENT_RE／PRESENT_EXTRA）、无历史豁免标记时为 True（FAIL 级）。
    """
    if TRIPLE_RE.search(ln):
        return False
    for dm in DM_STANDALONE_RE.finditer(ln):
        idx = {"卷": 0, "章": 1, "节": 2}[dm.group("unit")]
        if (int(dm.group("num")) != v[idx]
                and (PRESENT_RE.search(ln) or PRESENT_EXTRA_RE.search(ln))
                and not HIST_RE.search(ln)
                and not OTHER_BASE_RE.search(ln)):
            return True
    return False


def scan(v: tuple[int, int, int]):
    """返回 (marker_drift, present_stale, exempt, marker_ok, ref_stale, pending_stale,
    present_stale_blind, dm_stale)。末两项为 INFO 盲区与维度五独立数字形。"""
    drift, stale, exempt, ok, ref_stale, pending_stale, blind, dm_stale = [], [], [], [], [], [], [], []
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
            had_triple = False
            for tm in TRIPLE_RE.finditer(ln):
                had_triple = True
                cat = classify_triple(ln, tm, v, in_block)
                declared = (int(tm.group(1)), int(tm.group(2)),
                            int(tm.group(3).replace(",", "")) if tm.group(3) else None)
                if cat == "ok":
                    ok.append((fp, i, ln.strip(), declared))
                elif cat == "drift":
                    drift.append((fp, i, ln.strip(), declared))
                elif cat == "stale":
                    stale.append((fp, i, ln.strip(), declared))
                elif cat == "blind":
                    blind.append((fp, i, ln.strip()[:150], declared))
                else:
                    exempt.append((fp, i, ln.strip()[:120], declared))
            # 维度五：doc-metrics 独立数字形旧口径（FAIL 级）
            if classify_dm_standalone(ln, v):
                dm_stale.append((fp, i, ln.strip()[:150]))
            # 维度二：指向已归档目录文件但同行无归档标注（带日期历史文件整体豁免）
            if ARCHIVED_REF_RE.search(ln) and not ARCHIVE_NOTED_RE.search(ln) and not hist_file:
                ref_stale.append((fp, i, ln.strip()[:150]))
            # 维度三：未消解 ⬜ 待填标记（仅独立单元格 `| ⬜ |`，说明句/匹配列定义不算待办）且文件未声明被取代
            # 先剔除行内代码段：规则文件会以 `| ⬜ |` 形式描述该标记本身，属文档而非待办
            plain = re.sub(r"`[^`]*`", "", ln)
            if re.search(r"\|\s*⬜\s*\|", plain) and not superseded:
                pending_stale.append((fp, i, ln.strip()[:150]))
    return drift, stale, exempt, ok, ref_stale, pending_stale, blind, dm_stale


def cmd_selftest() -> int:
    """判据非空自检（2026-10-17 立，负向夹具）：合成行喂分类器，断言必须命中。

    判据存在 ≠ 判据有效——本 selftest 的核心负向用例是维度五：
    “doc-metrics 26 卷”独立数字形在旧判据（TRIPLE_RE）下完全漏检，
    新判据必须判 dm_stale；外加 TRIPLE 三连形／豁免／盲区／一致各形。
    """
    v = (74, 521, 3671)
    cases = [
        # (说明, 行, in_block, 期望 triple 类别（无 TRIPLE 则 None）, 期望 dm_stale)
        (u"旧三连形现在时态须判 stale",
         u"- 现行大纲目录 `x/index.html` 的 doc-metrics 67 卷 482 章 3468 节",
         False, "stale", False),
        (u"新独立数字形（旧判据漏检）须判 dm_stale",
         u"- **卷数核对**：须与现行口径一致（`x/index.html` 的 doc-metrics 26 卷；过渡期以磁盘为锚）",
         False, None, True),
        (u"独立数字形-章",
         u"- **章数核对**：须与现行口径章数一致（`x/index.html` 的 doc-metrics 240 章）",
         False, None, True),
        (u"独立数字形-现值一致不判",
         u"- **卷数核对**：须与现行口径卷数一致（`x/index.html` 的 doc-metrics 74 卷）",
         False, None, False),
        (u"历史豁免行不判 dm_stale（无三连形，triple=None）",
         u"- 历史记录：原现行口径 26 卷（已于 2026-09-20 取代）",
         False, None, False),
        (u"另一套基准（磁盘实况）豁免",
         u"当前磁盘实况 19卷355章；现行大纲目录 67 卷 482 章 3468 节",
         False, "exempt", False),
        (u"标记块内漂移判 drift",
         u"- 重构2026 现行大纲目录口径：67 卷 482 章 3468 节",
         True, "drift", False),
        (u"标记块内一致判 ok",
         u"- 重构2026 现行大纲目录口径：74 卷 521 章 3671 节",
         True, "ok", False),
        (u"历史标记（修订）豁免不判盲区",
         u"- 现行口径 67 卷 482 章 3468 节（修订（2026-09-20）：已按 74 卷演进）",
         False, "exempt", False),
    ]
    bad = 0
    for name, ln, in_blk, want_cat, want_dm in cases:
        got_cat, got_dm = None, False
        tm = TRIPLE_RE.search(ln)
        if tm:
            got_cat = classify_triple(ln, tm, v, in_blk)
        got_dm = classify_dm_standalone(ln, v)
        if (got_cat != want_cat) or (got_dm != want_dm):
            bad += 1
            print(u"  ✗ %s：triple=%r（期望 %r）dm_stale=%r（期望 %r）"
                  % (name, got_cat, want_cat, got_dm, want_dm))
    print("sync_refactor2026_baseline --selftest：%d/%d %s"
          % (len(cases) - bad, len(cases), "PASS" if not bad else "FAIL"))
    return 0 if not bad else 1


def cmd_list(v):
    print(f"权威基准（index.html doc-metrics）：{fmt(v)}")


def cmd_check(v, verbose: bool):
    drift, stale, exempt, ok, ref_stale, pending_stale, blind, dm_stale = scan(v)
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
    if blind:
        print(f"⚠️ INFO｜present-stale-blind（语义为现在时态、但 PRESENT_RE 未覆盖的旧口径，{len(blind)} 处）"
              f"——**不改判定，请人工核**：")
        for fp, i, ln, d in blind:
            print(f"  ~ {fp.name} L{i}: {ln[:130]}")
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
    # D9：92 号文 frontmatter「现行口径（唯一权威）」行须与权威基准一致（2026-09-29 加，防施工后累积漂移）
    try:
        _f92 = (Path(__file__).resolve().parents[3] / "08-核查报告与多轮复核" / "重构2026" /
                "92-目录内容调整建议书-综合释疑库与未实施建议.md")
        _head = "\n".join(_f92.read_text(encoding="utf-8").split("\n")[:10])
        _m92 = re.search(r"(\d+) 卷 (\d+) 章 (\d+) 节", _head)
        _d92 = (int(_m92.group(1)), int(_m92.group(2)), int(_m92.group(3))) if _m92 else None
        d92_bad = 0 if (_d92 == v) else 1
        if d92_bad:
            print(f"❌ 92号文口径漂移：frontmatter 现 {_d92} ≠ 权威基准 {fmt(v)}（施工后未回写）")
        else:
            print(f"92号文 frontmatter 口径：一致（{fmt(v)}）")
    except Exception as _e:
        d92_bad = 0
        print(f"（92号文口径校验跳过：{_e}）")
    if dm_stale:
        print(f"❌ dm-stale（doc-metrics 独立数字形旧口径——TRIPLE_RE 漏检形，2026-10-17 新判据，需人工）：{len(dm_stale)} 处")
        for fp, i, ln in dm_stale[:20]:
            print(f"  {fp.name} L{i}: {ln[:120]}")
    bad = len(drift) + len(stale) + len(ref_stale) + len(pending_stale) + len(dm_stale) + jsonld_bad + d92_bad
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
    g.add_argument("--selftest", action="store_true", help="判据非空自检（负向夹具）")
    ap.add_argument("--verbose", action="store_true", help="列出全部豁免命中")
    args = ap.parse_args()
    if args.selftest:
        return cmd_selftest()
    v = parse_authoritative()
    if args.list:
        cmd_list(v)
        return 0
    if args.sync:
        return cmd_sync(v)
    return cmd_check(v, args.verbose)


if __name__ == "__main__":
    sys.exit(main())
