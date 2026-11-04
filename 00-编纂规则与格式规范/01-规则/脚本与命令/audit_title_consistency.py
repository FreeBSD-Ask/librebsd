#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""audit_title_consistency.py —— 第三十九件门禁：小节标题一致性与证据完整性。

设立缘由（2026-10-29）
--------------------
旧 15,206 个“小节”实为史料颗粒：题面不合格 68.4%、题指纹命中率 6.4%，TF 修补 60 批未解决。
根因之一是无题名门禁——前 60 批只靠人工与提示词。本件把《小节建制与题名规则》§四–§七
的可机读部分固化，使“标题不合规”在写台账当刻即被拦下，而不是落盘后返工。

对象
----
`<root>/05-卷册大纲/映射/title-design/V{NN}.tsv`（标题表）
`<root>/05-卷册大纲/映射/title-evidence/V{NN}.tsv`（证据表）
`<root>/05-卷册大纲/映射/title-design/approvals.tsv`（批准记录，全局）
`<root>/05-卷册大纲/映射/title-design/approved/V{NN}.title.ok`（批准标记）
`<root>/05-卷册大纲/映射/title-design/exceptions/V{NN}.tsv`（例外台账；前五列必备，
尾部可带 registered_date／date_src 两扩展列——2026-11-04 P4 盘库 G-05／R44 增）

判据分组
--------
A 台账结构（表头、唯一性、层级对位、order 连续、status 枚举）
B 形态 T1–T7（名词短语下限、禁日期起头、禁转述动词、禁纯版本号、禁工序词、长度、
   年代括注：全角括号＋U+2013，含全角括号内 ASCII 连字符年份区间（2026-11-04 增补，G-19））
C 字符 C1–C3／C5–C9（中英空格、直角引号、ASCII 句读、空白与不可见字符、术语、
   禁词：Q2「谱系」＋《释读规则》读者面禁名＋进步叙事与等级修辞（R31）＋劳动禁词（R32）；
   技术义「失败」（构建／装载／校验失败等及「失败日志」类技术对象形态）白名单豁免，见
   TECH_FAIL_RE（2026-11-04 P7-1）；
   理论腔词披露不拦；C8 去 AI 味：空转词硬拦、同卷同尾簇 ≤3、单题「的」≤2、AI 腔词披露不拦；
   C9 禁反斜杠与控制字符——2026-11-04 由原「C4」重编，与规则 C4（官方名斜杠两分，
   由第四十一件承载）脱钩对齐（G-01），本判据语义不变）
D 语义 S1–S4 的可机读下限（题旨非空、层级一致、同节平行、异质登记；
   D3 对 V01–V50 卷段豁免（2026-11-04 入库，G-02）：ykla 2026-11-02 改判字数相似不作
   要求，命中改标 EXEMPT 不判 FAIL，豁免不外溢其他判据与其他卷段）
E 证据齐（每条标题有证据行、证据 id 在台账内、层级与日期格式）
F 四源覆盖（计数与集合一致、≥2 源、专名／标准号／年代题 ≥3 源、单源题为 0）
G 重复题（同节、同卷）
H 批准一致（title.ok hash 与台账一致、approvals 有行、已批卷无 draft）
I 例外（id 在台账内、kind 枚举）

零态合法：`title-design/` 下无任何 `V*.tsv` 时全组标 N/A 并 PASS（立线未开工，不是缺陷）。

退出码
------
0 全 PASS；1 有 FAIL；2 输入违约（表头不合 schema，直接停）。

用法
----
`python audit_title_consistency.py [--root PATH] [--selftest] [--check]`
`python audit_title_consistency.py --json [--json-out PATH]`

`--json` 只输出机读 JSON（不打印人读报告），含每判据的逐题命中 id（title_ids／
section_ids／vol_ids 三级粒度），供 3A6-2 P4 全量机判消费（2026-11-04 增补，判据零改动）。
`--json-out` 另把同一 JSON 落盘，人读报告照常打印。

说明
----
本件是**机器下限**判据：T3 全表、S1 忠于内容、S4 异质不上题等语义判据无法穷举，
由设计卡复核与卷级呈审承担；本件只保证“明显不合规不给写进台账”。
"""
import argparse
import hashlib
import io
import json
import os
import re
import sys
import tempfile
import traceback

DESIGN_HDR = ["subsection_id", "vol", "chapter", "section", "title", "thesis",
              "order", "source_count", "sources", "status"]
EVID_HDR = ["subsection_id", "query", "url", "source_type", "tier", "accessed",
            "quote", "conflict"]
APPR_HDR = ["kind", "vol", "title_count", "ledger_sha256", "approved_by",
            "approved_at", "note"]
EXC_HDR = ["subsection_id", "kind", "reason", "proposal", "status"]
# 例外台账尾部扩展列（2026-11-04 P4 盘库，G-05／R44）：前五列为必备前缀，尾部允许且仅
# 允许 registered_date（登记日期，git 逐行首现）与 date_src（取值来源 git／file／manual）
# 两列；行宽放宽为 ≥ 前缀长度，兼容未回填卷与已回填卷并存。
EXC_HDR_EXT = ("registered_date", "date_src")

STATUS_OK = {"draft", "final", "approved"}
SRC_OK = {"史料", "联网", "目录", "规则"}
TIER_OK = {"A", "B", "C"}
CONFLICT_OK = {"none", "noted"}
EXC_KIND = {"single_source", "cannot_name", "propose_section", "propose_chapter",
            "propose_volume", "corpus_gap"}
EXC_STATUS = {"open", "accepted", "rejected"}

REL = os.path.join("05-卷册大纲", "映射")
DESIGN_REL = os.path.join(REL, "title-design")

CJK = "\u4e00-\u9fff"
BAD_INVISIBLE = re.compile(u"[\u200b-\u200f\u2060-\u206f\ufeff\u00ad\u3000\u00a0\u202f]")
DATE_HEAD = re.compile(r"^(\d{4}\s*年|\d{1,2}\s*月\s*\d{1,2}\s*日|年\s*\d{1,2}\s*月)")
VERSION_ONLY = re.compile(r"^[0-9][0-9A-Za-z._\-]*$")
VERB_HEAD = ("讨论", "分析", "介绍", "说明", "论述", "研究", "探讨", "浅析", "初探")
TRANSCRIBE = ("宣布", "指出", "表示", "认为", "建议", "询问", "承认", "强调",
              "透露", "提议", "反驳", "呼吁", "质疑", "回复", "答复")
WORKER_JARGON = ("未判定", "待定", "杂项", "空模板件", "属英文原件", "属引文原件")
# C7 禁词（2026-10-30 增补，ykla 授权；2026-11-04 扩充，3A6-2 R31／R32 固化）：
# BANNED_TITLE：Q2「谱系」禁用（2026-10-08 立，125 号文 阶段 F，ykla 硬令「标题＋注文一并
# 清理」）与《释读规则》读者面禁名，小节题名同口径（原组不变）。
# BANNED_HIERARCHY：进步叙事与等级修辞禁词（2026-11-04 增补，G-08／R31）：总纲 8 禁
# 「主流/支流」「成功/失败」等级表述；源头为 18 号文 G3 禁用表与 03／10／13／22 号文
# 复核账未执行项，整词硬拦。
# BANNED_INEVITABLE：「必然」两字过宽——「偶然性与必然（性）」类辩证合法用例不作要求，
# 故不裸拦「必然」，按历史必然义词组级匹配硬拦（2026-11-04 增补，G-08／R31）。
# BANNED_LABOR：劳动／雇佣／资本（2026-11-04 增补，G-16／R32；77／79 号文三十条映射，
# 目录层已全库清理，此处防回归），整词硬拦；「劳动关系史」类合法学术题若命中属真发现，
# 逐条披露不改词表。
# REVIEW_TERMS 为理论腔披露表（人工复核项，不拦退出码）：对象层研究题（如史学辨析章
# 以「叙事」为研究对象者）合法，故只披露不硬拦，防误杀。
BANNED_TITLE = ("谱系", "一刻哲学", "构造哲学")
BANNED_HIERARCHY = ("黄金时代", "飞跃", "正统", "主流", "支流", "成功", "失败", "成败")
BANNED_INEVITABLE = ("历史必然", "必然趋势", "必然胜利", "必然失败", "必然成功",
                     "必然产生", "必然结果", "必然结局", "必然取代", "必然规律", "必然命运")
BANNED_LABOR = ("劳动", "雇佣", "资本")
# C7 技术义白名单（2026-11-04 P7-1，3A6-2 遗留 4 项细化）：R31 所禁者是**施加于历史
# 行动者／项目的等级修辞**（把项目判为「成功／失败」），而「构建失败」「装载失败」
# 「校验失败」一类指**机器操作的返回状态**，属技术义，不构成进步叙事判断。故先在题名内
# 剥离「技术操作词（可带期／的／之）＋失败」与「失败＋技术对象词」两类形态，其余等级
# 修辞词照判。剥离只作用于 BANNED_HIERARCHY 的「失败」一处，不涉其他禁词与判据。
# 评价义（如「失败项目的归档」）不在此列，仍属 R31 命中，须人工逐条判定。
TECH_FAIL_OP = ("构建", "装载", "校验", "编译", "检验", "安装", "升级", "引导",
                "启动", "挂载", "运行", "测试", "链接", "解析", "下载", "打包",
                "签名", "同步", "部署", "认证", "鉴权", "登录")
TECH_FAIL_OBJ = ("日志", "诊断", "监测", "告警", "恢复", "处理", "分类", "定位",
                 "追踪", "上报", "复现", "统计", "率")
TECH_FAIL_RE = re.compile(u"(?:%s)(?:期|的|之)?失败|失败(?:%s)"
                          % ("|".join(TECH_FAIL_OP), "|".join(TECH_FAIL_OBJ)))
REVIEW_TERMS = ("叙事", "话语", "互构", "建构", "解构", "范式", "语境", "他者", "视域", "主体性")
# C8 去 AI 味（2026-10-30 ykla 令“标题风格应一致，去 AI 味的同时保持学术性”）：
# 硬拦 AI 高频空转词、同卷结尾二字簇超限、单题「的」超密；临界词只披露防误杀。
BANNED_AI = ("赋能", "抓手", "闭环", "颗粒度", "锚点", "景深", "温差", "样态")
REVIEW_AI = ("图景", "维度", "对位", "坐标", "版图", "生态", "张力", "轨迹", "格局", "画像")
PATTERN_TECH = re.compile(r"[A-Za-z]{2,}|POSIX|IEEE|ANSI|ISO|RFC|USENIX|ACM")
STANDARD = re.compile(r"(IEEE\s*Std|POSIX|ISO/IEC|ANSI|RFC\s*\d+|USENIX)")
YEAR_IN = re.compile(r"\d{4}")
BAD_PAREN = re.compile(r"\(\s*\d{4}|\d{4}\s*\)")
# B7 扩展（2026-11-04 增补，G-19／3A6-2 R42）：全角括号内年份区间用 ASCII 连字符
# （如「（1980-2026）」）判 FAIL，须改 U+2013「–」（T7 正形）；既有 BAD_PAREN 语义不变。
BAD_PAREN_FW_HYPHEN = re.compile(u"（[^（）]*\\d{4}\\s*-\\s*\\d{4}[^（）]*）")
CROSS_REF = re.compile(u"（另见[^）]*）")
# D3 卷段豁免（2026-11-04 入库，G-02／3A6-2 R04）：ykla 2026-11-02 改判——V01–V50 卷段
# 「同节字数极差 ≤14」不作要求（字数相似豁免）。豁免仅限 D3 本判据与 V01–V50 两界，
# 不外溢其他判据（同节 B／C／G 组照判），也不外溢 V51–V76（照判 FAIL）。
D3_EXEMPT_VOLS = frozenset("%02d" % n for n in range(1, 51))
D3_EXEMPT_BASIS = "ykla 2026-11-02 改判（3A6-2 R04 固化）：V01–V50 字数相似不作要求"

# 逐题命中还原（2026-11-04 P4 增补）：各判据内部 bad_* 列表以「id（说明）」承载，
# --json 由此还原 title／section／volume 三级粒度，判据语义不变。
ID_TITLE = re.compile(r"V\d{2}\.\d+\.\d+\.\d+")
ID_SECTION = re.compile(r"V\d{2}\.\d+\.\d+(?!\.\d)")
ID_VOL = re.compile(r"^V\d{2}(?![.\d])")


def _read(p):
    with io.open(p, encoding="utf-8") as f:
        return f.read()


def _rows(p):
    txt = _read(p)
    if txt.startswith("\ufeff"):
        txt = txt[1:]
    lines = [ln for ln in txt.split("\n") if ln.strip()]
    if not lines:
        return None, []
    hdr = lines[0].split("\t")
    body = [ln.split("\t") for ln in lines[1:]]
    return [h.strip() for h in hdr], body


def _title_len(t):
    return len([c for c in t if not c.isspace()])


def _sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def _id_parts(sid):
    """V01.2.3.1 → ('V01', '2', '3', '1')"""
    p = sid.split(".")
    return tuple(p) if len(p) == 4 else None


def load_design(design_dir):
    """返回 {vol: (path, hdr, rows)}；无台账返回 {}。表头违约抛 ValueError。"""
    out = {}
    if not os.path.isdir(design_dir):
        return out
    for name in sorted(os.listdir(design_dir)):
        m = re.match(r"V(\d{2})\.tsv$", name)
        if not m:
            continue
        p = os.path.join(design_dir, name)
        hdr, rows = _rows(p)
        if hdr is None:
            continue
        if hdr != DESIGN_HDR:
            raise ValueError("%s 表头不合 schema：%s" % (name, hdr))
        out[m.group(1)] = (p, hdr, rows)
    return out


def load_evid(evid_dir):
    out = {}
    if not os.path.isdir(evid_dir):
        return out
    for name in sorted(os.listdir(evid_dir)):
        m = re.match(r"V(\d{2})\.tsv$", name)
        if not m:
            continue
        p = os.path.join(evid_dir, name)
        hdr, rows = _rows(p)
        if hdr is None:
            continue
        if hdr != EVID_HDR:
            raise ValueError("%s 表头不合 schema：%s" % (name, hdr))
        out[m.group(1)] = (p, hdr, rows)
    return out


def run(root, collect=None):
    """跑全部判据，返回 [(code, name, ok, detail)]；ok 三态 True／"EXEMPT"／False。

    collect 非 None 时按判据码回填机读命中：{code: {name, ok, detail, title_ids,
    section_ids, vol_ids}}（2026-11-04 P4 增补，供 --json 与机判结果.tsv 消费）。
    """
    rows_out = []
    design_dir = os.path.join(root, DESIGN_REL)
    evid_dir = os.path.join(root, REL, "title-evidence")
    appr = os.path.join(design_dir, "approvals.tsv")
    okdir = os.path.join(design_dir, "approved")
    excdir = os.path.join(design_dir, "exceptions")

    design = load_design(design_dir)
    evid = load_evid(evid_dir)

    def _hit_levels(items):
        """把「id（说明）」列表还原为 title／section／volume 三级命中集合。"""
        titles, sections, vols = set(), set(), set()
        for item in items:
            t = ID_TITLE.findall(item)
            if t:
                titles.update(t)
                continue
            s = ID_SECTION.findall(item)
            if s:
                sections.update(s)
                continue
            m = ID_VOL.match(item)
            if m:
                vols.add(m.group(0))
        return titles, sections, vols

    def rec(code, name, ok, detail, title_ids=(), section_ids=(), vol_ids=(), items=()):
        rows_out.append((code, name, ok, detail))
        if collect is not None:
            collect[code] = {"name": name, "ok": ok, "detail": detail,
                             "title_ids": sorted(set(title_ids)),
                             "section_ids": sorted(set(section_ids)),
                             "vol_ids": sorted(set(vol_ids)),
                             "items": list(items)}

    def f(code, name, bad, detail, ids=None, section_ids=None, vol_ids=None):
        if ids is not None or section_ids is not None or vol_ids is not None:
            rec(code, name, not bad, detail, ids or (), section_ids or (), vol_ids or (),
                items=bad)
            return
        titles, sections, vols = _hit_levels(bad)
        rec(code, name, not bad, detail, titles, sections, vols, items=bad)

    if not design:
        rec("A1", "零态：无标题台账（立线未开工，合法状态）", True, "N/A")
        return rows_out

    # 汇总
    all_rows = []          # (vol, idx, cols)
    for vol, (p, hdr, body) in design.items():
        for i, c in enumerate(body, 2):
            if len(c) != len(DESIGN_HDR):
                raise ValueError("%s 第 %d 行列数 %d ≠ %d" % (p, i, len(c), len(DESIGN_HDR)))
            all_rows.append((vol, i, dict(zip(DESIGN_HDR, c))))

    # ---------------- A 台账结构
    bad1 = []
    seen = {}
    for vol, ln, r in all_rows:
        sid = r["subsection_id"]
        if sid in seen:
            bad1.append("%s（%s 与第 %d 行重）" % (sid, vol, seen[sid]))
        else:
            seen[sid] = ln
    f("A1", "A1 subsection_id 全卷唯一", bad1, "重复 %d 处：%s" % (len(bad1), "、".join(bad1[:5]) or "无"))

    bad2 = []
    for vol, ln, r in all_rows:
        parts = _id_parts(r["subsection_id"])
        if not parts:
            bad2.append("%s（段数≠4）" % r["subsection_id"])
            continue
        want = ("V%02d" % int(r["vol"]) if r["vol"].isdigit() else r["vol"],
                r["chapter"].strip(), r["section"].strip())
        if (parts[0], parts[1], parts[2]) != want:
            bad2.append("%s（id 与 vol/chapter/section 不对位）" % r["subsection_id"])
    f("A2", "A2 id 层级与 vol/chapter/section 对位", bad2,
      "不符 %d 处：%s" % (len(bad2), "、".join(bad2[:5]) or "无"))

    bad3 = []
    by_sec = {}
    for vol, ln, r in all_rows:
        by_sec.setdefault((r["vol"], r["chapter"], r["section"]), []).append(r)
    for k, rs in by_sec.items():
        orders = sorted(int(x["order"]) for x in rs if x["order"].isdigit())
        if orders != list(range(1, len(rs) + 1)):
            bad3.append("V%s.%s.%s" % k)
    f("A3", "A3 节内 order 连续 1..n", bad3,
      "异常节 %d 个：%s" % (len(bad3), "、".join(bad3[:5]) or "无"))

    bad4 = [r["subsection_id"] for _, _, r in all_rows if r["status"] not in STATUS_OK]
    f("A4", "A4 status 枚举合法", bad4,
      "非法 %d 处：%s" % (len(bad4), "、".join(bad4[:5]) or "无"))

    # ---------------- B 形态 T1–T7
    bad_t1 = []
    for _, _, r in all_rows:
        t = r["title"].strip()
        if not t:
            bad_t1.append("%s（空题）" % r["subsection_id"])
            continue
        if t.startswith(VERB_HEAD):
            bad_t1.append("%s（动词起首）" % r["subsection_id"])
        if t.endswith(("吗", "呢", "吧", "？", "!", "！", "。")) or "如何" in t:
            bad_t1.append("%s（非名词短语收尾）" % r["subsection_id"])
    f("B1", "B1 论题名词短语（机器下限）", bad_t1,
      "不符 %d 处：%s" % (len(bad_t1), "、".join(bad_t1[:5]) or "无"))

    bad_t2 = [r["subsection_id"] for _, _, r in all_rows if DATE_HEAD.match(r["title"].strip())]
    f("B2", "B2 禁日期起头", bad_t2,
      "命中 %d 处：%s" % (len(bad_t2), "、".join(bad_t2[:5]) or "无"))

    bad_t3 = [r["subsection_id"] for _, _, r in all_rows
              if any(v in r["title"] for v in TRANSCRIBE)]
    f("B3", "B3 禁转述动词作主干（长名单下限）", bad_t3,
      "命中 %d 处：%s" % (len(bad_t3), "、".join(bad_t3[:5]) or "无"))

    bad_t4 = [r["subsection_id"] for _, _, r in all_rows
              if VERSION_ONLY.match(r["title"].strip())]
    f("B4", "B4 禁纯版本号与行号独立成题", bad_t4,
      "命中 %d 处：%s" % (len(bad_t4), "、".join(bad_t4[:5]) or "无"))

    bad_t5 = [r["subsection_id"] for _, _, r in all_rows
              if any(w in r["title"] for w in WORKER_JARGON)]
    f("B5", "B5 禁工序状态词", bad_t5,
      "命中 %d 处：%s" % (len(bad_t5), "、".join(bad_t5[:5]) or "无"))

    bad_t6 = ["%s（%d 字）" % (r["subsection_id"], _title_len(r["title"]))
              for _, _, r in all_rows if not (8 <= _title_len(r["title"]) <= 40)]
    f("B6", "B6 长度 8–40 字（去空格）", bad_t6,
      "越界 %d 处：%s" % (len(bad_t6), "、".join(bad_t6[:5]) or "无"))

    bad_t7 = [r["subsection_id"] for _, _, r in all_rows
              if BAD_PAREN.search(r["title"]) or BAD_PAREN_FW_HYPHEN.search(r["title"])]
    f("B7", "B7 年代括注须全角括号与 U+2013（全角括号内禁 ASCII 连字符年份区间）", bad_t7,
      "命中 %d 处：%s" % (len(bad_t7), "、".join(bad_t7[:5]) or "无"))

    # ---------------- C 字符
    bad_c1 = []
    for _, _, r in all_rows:
        t = r["title"]
        if re.search(u"[A-Za-z0-9][%s]" % CJK, t) or re.search(u"[%s][A-Za-z0-9]" % CJK, t):
            bad_c1.append(r["subsection_id"])
    f("C1", "C1 中英／中数之间各一个半角空格", bad_c1,
      "紧邻 %d 处：%s" % (len(bad_c1), "、".join(bad_c1[:5]) or "无"))

    bad_c2 = [r["subsection_id"] for _, _, r in all_rows
              if any(ch in r["title"] for ch in "\u300c\u300d\u300e\u300f\"'")]
    f("C2", "C2 弯引号；禁直角引号与 ASCII 直引号", bad_c2,
      "命中 %d 处：%s" % (len(bad_c2), "、".join(bad_c2[:5]) or "无"))

    bad_c3 = [r["subsection_id"] for _, _, r in all_rows
              if any(ch in r["title"] for ch in ",;:!?")]
    f("C3", "C3 句读全角；禁 ASCII 逗号分号冒号叹问", bad_c3,
      "命中 %d 处：%s" % (len(bad_c3), "、".join(bad_c3[:5]) or "无"))

    bad_c5 = []
    for _, _, r in all_rows:
        t = r["title"]
        if "  " in t or t != t.strip() or BAD_INVISIBLE.search(t):
            bad_c5.append(r["subsection_id"])
    f("C5", "C5 禁双空格／首尾空格／不可见字符", bad_c5,
      "不符 %d 处：%s" % (len(bad_c5), "、".join(bad_c5[:5]) or "无"))

    bad_c6 = []
    for _, _, r in all_rows:
        t = r["title"]
        if "端口" in t and "网络端口" not in t and "网络" not in t:
            bad_c6.append("%s（端口误译）" % r["subsection_id"])
        if "Ports" in t and not re.search(r"Ports(\s*树|\s*Collection|\s*系统|\s*集合)", t):
            bad_c6.append("%s（Ports 须为专名形态）" % r["subsection_id"])
    f("C6", "C6 术语（Port 单数／禁端口误译／Ports 专名）", bad_c6,
      "命中 %d 处：%s" % (len(bad_c6), "、".join(bad_c6[:5]) or "无"))

    bad_c7 = []
    for _, _, r in all_rows:
        hits = [w for w in BANNED_TITLE if w in r["title"]]
        # 技术义「失败」先剥离（P7-1 白名单），其余等级修辞照原题名判。
        t_chk = TECH_FAIL_RE.sub(u"·", r["title"])
        hits += [w for w in BANNED_HIERARCHY if w in t_chk]
        hits += [w for w in BANNED_INEVITABLE if w in r["title"]]
        hits += [w for w in BANNED_LABOR if w in r["title"]]
        if hits:
            bad_c7.append("%s（%s）" % (r["subsection_id"], "、".join(hits)))
    f("C7", "C7 禁词（Q2 谱系；释读规则读者面禁名；进步叙事与等级修辞 R31；劳动禁词 R32）",
      bad_c7, "命中 %d 处：%s" % (len(bad_c7), "、".join(bad_c7[:5]) or "无"))
    info_c7 = ["%s（%s）" % (r["subsection_id"], "、".join(w for w in REVIEW_TERMS if w in r["title"]))
               for _, _, r in all_rows if any(w in r["title"] for w in REVIEW_TERMS)]
    info_c7_ids = [r["subsection_id"] for _, _, r in all_rows
                   if any(w in r["title"] for w in REVIEW_TERMS)]
    rec("C7i", "C7i 理论腔词披露（人工复核项，不拦退出码）", True,
        "命中 %d 处：%s" % (len(info_c7), "、".join(info_c7[:6]) or "无"), info_c7_ids,
        items=info_c7)

    # C8 去 AI 味与风格一致（2026-10-30 ykla 令：标题风格应一致，去 AI 味的同时保持学术性）
    bad_c8a = []
    for _, _, r in all_rows:
        hits = [w for w in BANNED_AI if w in r["title"]]
        if hits:
            bad_c8a.append("%s（%s）" % (r["subsection_id"], "、".join(hits)))
    f("C8a", "C8a 禁 AI 高频空转词", bad_c8a,
      "命中 %d 处：%s" % (len(bad_c8a), "、".join(bad_c8a[:5]) or "无"))

    bad_c8b, bad_c8b_ids = [], []
    tail_groups = {}
    for vol, ln, r in all_rows:
        t = "".join(r["title"].split())
        if len(t) >= 2:
            tail_groups.setdefault((vol, t[-2:]), []).append(r["subsection_id"])
    for (vol, tail), ids in sorted(tail_groups.items()):
        if len(ids) > 3:
            bad_c8b.append("V%s 尾“%s”×%d（%s…）" % (vol, tail, len(ids), "、".join(ids[:4])))
            bad_c8b_ids.extend(ids)
    f("C8b", "C8b 风格一致：同卷同结尾二字簇 ≤3", bad_c8b,
      "超限簇 %d 处：%s" % (len(bad_c8b), "、".join(bad_c8b[:5]) or "无"), bad_c8b_ids)

    bad_c8c = ["%s（的×%d）" % (r["subsection_id"], r["title"].count("的"))
               for _, _, r in all_rows if r["title"].count("的") > 2]
    f("C8c", "C8c 单题“的”字 ≤2（去 AI 味）", bad_c8c,
      "超限 %d 处：%s" % (len(bad_c8c), "、".join(bad_c8c[:5]) or "无"))

    info_c8 = ["%s（%s）" % (r["subsection_id"], "、".join(w for w in REVIEW_AI if w in r["title"]))
               for _, _, r in all_rows if any(w in r["title"] for w in REVIEW_AI)]
    info_c8_ids = [r["subsection_id"] for _, _, r in all_rows
                   if any(w in r["title"] for w in REVIEW_AI)]
    rec("C8i", "C8i AI 腔词披露（人工复核项，不拦退出码）", True,
        "命中 %d 处：%s" % (len(info_c8), "、".join(info_c8[:6]) or "无"), info_c8_ids,
        items=info_c8)

    # C9 禁反斜杠与控制字符（2026-11-04 由「C4」重编：规则 C4＝官方名斜杠两分，由第四十一件
    # audit_title_term_forms.py 承载；本判据与规则编号脱钩对齐，G-01／3A6-2 R28。语义不变。）
    bad_c9 = [r["subsection_id"] for _, _, r in all_rows
              if "\\" in r["title"] or any(ord(ch) < 32 or ord(ch) == 127 for ch in r["title"])]
    f("C9", "C9 禁反斜杠与控制字符（路径字符由落盘器全角化）", bad_c9,
      "命中 %d 处：%s" % (len(bad_c9), "、".join(bad_c9[:5]) or "无"))

    # ---------------- D 语义下限
    bad_d1 = ["%s（thesis 空或过短）" % r["subsection_id"] for _, _, r in all_rows
              if len(r["thesis"].strip()) < 8]
    f("D1", "D1 S1 题旨非空（thesis ≥8 字）", bad_d1,
      "不符 %d 处：%s" % (len(bad_d1), "、".join(bad_d1[:5]) or "无"))

    f("D2", "D2 S2 上下位一致（依赖 A2 层级对位）", bad2, "同 A2")

    # D3 卷段豁免（G-02／3A6-2 R04）：V01–V50 命中改标 EXEMPT（不拦退出码）并注明豁免
    # 依据；V51–V76 照判 FAIL。豁免只作用于本判据，同节其他判据不受影响。
    bad_d3, exempt_d3 = [], []
    for k, rs in by_sec.items():
        lens = [_title_len(x["title"]) for x in rs]
        if lens and (max(lens) - min(lens)) > 14:
            item = "V%s.%s.%s（极差 %d）" % (k[0], k[1], k[2], max(lens) - min(lens))
            if k[0].strip() in D3_EXEMPT_VOLS:
                exempt_d3.append(item)
            else:
                bad_d3.append(item)
    d3_name = "D3 S3 同节平行：字数极差 ≤14（V01–V50 卷段豁免）"
    bad_d3_sec = sorted({m for it in bad_d3 for m in ID_SECTION.findall(it)})
    exempt_d3_sec = sorted({m for it in exempt_d3 for m in ID_SECTION.findall(it)})
    if bad_d3:
        d3_detail = "越界节 %d 个：%s" % (len(bad_d3), "、".join(bad_d3[:3]) or "无")
        if exempt_d3:
            d3_detail += "；另 V01–V50 豁免 %d 节（%s）" % (len(exempt_d3), D3_EXEMPT_BASIS)
        rec("D3", d3_name, False, d3_detail, section_ids=bad_d3_sec, items=bad_d3)
    elif exempt_d3:
        rec("D3", d3_name, "EXEMPT",
            "豁免节 %d 个：%s｜依据：%s"
            % (len(exempt_d3), "、".join(exempt_d3[:3]) or "无", D3_EXEMPT_BASIS),
            section_ids=exempt_d3_sec, items=exempt_d3)
    else:
        rec("D3", d3_name, True, "越界节 0 个：无")

    n_exc = 0
    exc_rows = []
    if os.path.isdir(excdir):
        for name in sorted(os.listdir(excdir)):
            if name.endswith(".tsv"):
                hdr, body = _rows(os.path.join(excdir, name))
                if hdr is None:
                    continue
                # 前五列为必备前缀；尾部只允许 registered_date／date_src 两扩展列（R44）。
                if hdr[:len(EXC_HDR)] != EXC_HDR:
                    raise ValueError("%s 表头不合 schema" % name)
                unknown = [h for h in hdr[len(EXC_HDR):] if h not in EXC_HDR_EXT]
                if unknown:
                    raise ValueError("%s 表头含未知扩展列：%s" % (name, unknown))
                exc_rows.extend(body)
    n_exc = len(exc_rows)
    bad_d4 = [c[0] for c in exc_rows
              if len(c) >= len(EXC_HDR) and c[1] == "single_source" and c[0] in seen]
    f("D4", "D4 S4 单源题进例外后不得成题", bad_d4,
      "违例 %d 条：%s（例外台账共 %d 条）"
      % (len(bad_d4), "、".join(bad_d4[:5]) or "无", n_exc))

    # ---------------- E 证据
    ev_by_id = {}
    bad_e0 = []
    for vol, (p, hdr, body) in evid.items():
        for c in body:
            if len(c) != len(EVID_HDR):
                raise ValueError("%s 证据行列数违约" % p)
            d = dict(zip(EVID_HDR, c))
            sid = d["subsection_id"]
            ev_by_id.setdefault(sid, []).append(d)
            if d["tier"] not in TIER_OK:
                bad_e0.append("%s（tier=%s）" % (sid, d["tier"]))
            if d["source_type"] not in SRC_OK:
                bad_e0.append("%s（source_type=%s）" % (sid, d["source_type"]))
            if d["conflict"] not in CONFLICT_OK:
                bad_e0.append("%s（conflict=%s）" % (sid, d["conflict"]))
            if not re.match(r"\d{4}-\d{2}-\d{2}$", d["accessed"]):
                bad_e0.append("%s（accessed=%s）" % (sid, d["accessed"]))
    f("E1", "E1 证据行字段枚举与日期格式", bad_e0,
      "不符 %d 处：%s" % (len(bad_e0), "、".join(bad_e0[:5]) or "无"))

    no_ev = [r["subsection_id"] for _, _, r in all_rows if r["subsection_id"] not in ev_by_id]
    f("E2", "E2 每条标题至少一行证据", no_ev,
      "缺证 %d 条：%s" % (len(no_ev), "、".join(no_ev[:5]) or "无"))

    orphan = sorted(set(ev_by_id) - set(seen))
    f("E3", "E3 证据 id 必须落在台账内", orphan,
      "悬空 %d 条：%s" % (len(orphan), "、".join(orphan[:5]) or "无"))

    # ---------------- F 四源覆盖
    bad_f1 = []
    for _, _, r in all_rows:
        srcs = [s for s in re.split(u"[;；]", r["sources"]) if s.strip()]
        n = r["source_count"].strip()
        if not n.isdigit():
            bad_f1.append("%s（source_count 非整数）" % r["subsection_id"])
            continue
        if int(n) != len(set(srcs)):
            bad_f1.append("%s（count=%s，集合=%d）" % (r["subsection_id"], n, len(set(srcs))))
        if any(s.strip() not in SRC_OK for s in srcs):
            bad_f1.append("%s（源名非法）" % r["subsection_id"])
    f("F1", "F1 source_count 与 sources 集合一致", bad_f1,
      "不符 %d 处：%s" % (len(bad_f1), "、".join(bad_f1[:5]) or "无"))

    bad_f2 = []
    for _, _, r in all_rows:
        t = r["title"]
        proper = bool(PATTERN_TECH.search(t)) or bool(STANDARD.search(t)) or bool(YEAR_IN.search(t))
        if proper and sum(1 for s in re.split(u"[;；]", r["sources"]) if s.strip()) < 3:
            bad_f2.append(r["subsection_id"])
    f("F2", "F2 专名／标准号／年代题 ≥3 源", bad_f2,
      "不足 %d 条：%s" % (len(bad_f2), "、".join(bad_f2[:5]) or "无"))

    bad_f3 = [r["subsection_id"] for _, _, r in all_rows
              if len([s for s in re.split(u"[;；]", r["sources"]) if s.strip()]) < 2]
    f("F3", "F3 单源题为 0", bad_f3,
      "单源 %d 条：%s" % (len(bad_f3), "、".join(bad_f3[:5]) or "无"))

    # ---------------- G 重复题
    bad_g1, bad_g2, bad_g2_ids = [], [], []
    for k, rs in by_sec.items():
        ts = [x["title"] for x in rs]
        dup = sorted({t for t in ts if ts.count(t) > 1})
        if dup:
            bad_g1.append("V%s.%s.%s：%s" % (k[0], k[1], k[2], "／".join(dup[:2])))
    for vol, (p, hdr, body) in design.items():
        groups, groups_ids = {}, {}
        for c in body:
            d = dict(zip(DESIGN_HDR, c))
            t = d["title"]
            cross = bool(CROSS_REF.search(t))
            base = CROSS_REF.sub("", t).strip()
            groups.setdefault(base, []).append(cross)
            groups_ids.setdefault(base, []).append(d["subsection_id"])
        for base, flags in groups.items():
            n_cross = sum(1 for x in flags if x)
            n_bare = len(flags) - n_cross
            if n_bare > 1 or n_cross > 1 or (n_cross and n_bare == 0):
                bad_g2.append("V%s：%s（主 %d／从 %d）" % (vol, base[:26], n_bare, n_cross))
                bad_g2_ids.extend(groups_ids[base])
    f("G1", "G1 同节内题名不重复", bad_g1,
      "重复 %d 节：%s" % (len(bad_g1), "、".join(bad_g1[:3]) or "无"))
    f("G2", "G2 同卷内题名不重复（每基名主 1 从 ≤1）", bad_g2,
      "重复 %d 卷：%s" % (len(bad_g2), "、".join(bad_g2[:3]) or "无"), bad_g2_ids)

    # ---------------- H 批准一致
    appr_rows = []
    if os.path.exists(appr):
        hdr, body = _rows(appr)
        if hdr != APPR_HDR:
            raise ValueError("approvals.tsv 表头不合 schema")
        appr_rows = [dict(zip(APPR_HDR, c)) for c in body]

    bad_h1, bad_h2, bad_h3, bad_h3_ids = [], [], [], []
    if os.path.isdir(okdir):
        for name in sorted(os.listdir(okdir)):
            m = re.match(r"V(\d{2})\.title\.ok$", name)
            if not m:
                continue
            vol = m.group(1)
            kv = {}
            for ln in _read(os.path.join(okdir, name)).split("\n"):
                if "=" in ln:
                    k, v = ln.split("=", 1)
                    kv[k.strip()] = v.strip()
            if vol not in design:
                bad_h1.append("V%s（无台账却存在 title.ok）" % vol)
                continue
            cur = _sha(design[vol][0])
            if kv.get("ledger_sha256") != cur:
                bad_h1.append("V%s（hash 不符：标记 %s ≠ 实 %s）"
                              % (vol, (kv.get("ledger_sha256") or "空")[:12], cur[:12]))
            if not any(a["kind"] == "title" and a["vol"] == "V" + vol for a in appr_rows):
                bad_h2.append("V%s" % vol)
            drafts = [r for _, _, r in all_rows if r["vol"] == vol and r["status"] == "draft"]
            if drafts:
                bad_h3.append("V%s（%d 条仍为 draft）" % (vol, len(drafts)))
                bad_h3_ids.extend(r["subsection_id"] for r in drafts)
    f("H1", "H1 title.ok 的 ledger_sha256 与台账一致", bad_h1,
      "不符 %d 处：%s" % (len(bad_h1), "、".join(bad_h1[:3]) or "无"))
    f("H2", "H2 每份 title.ok 有 approvals 行", bad_h2,
      "缺行 %d 处：%s" % (len(bad_h2), "、".join(bad_h2[:3]) or "无"))
    f("H3", "H3 已批卷无 draft 残留", bad_h3,
      "残留 %d 卷：%s" % (len(bad_h3), "、".join(bad_h3[:3]) or "无"), bad_h3_ids)

    # ---------------- I 例外
    bad_i1 = [c[0] for c in exc_rows if len(c) >= len(EXC_HDR) and c[0] not in seen]
    bad_i2 = [c[0] for c in exc_rows
              if len(c) >= len(EXC_HDR) and (c[1] not in EXC_KIND or c[4] not in EXC_STATUS)]
    f("I1", "I1 例外 id 落在台账内", bad_i1,
      "悬空 %d 条：%s" % (len(bad_i1), "、".join(bad_i1[:5]) or "无"))
    f("I2", "I2 例外 kind／status 枚举", bad_i2,
      "非法 %d 条：%s" % (len(bad_i2), "、".join(bad_i2[:5]) or "无"))

    return rows_out


def report(rows, title):
    print("=" * 78)
    print(title)
    print("=" * 78)
    fails = 0
    for code, name, ok, detail in rows:
        # ok 三态：True＝PASS；"EXEMPT"＝豁免披露（不拦退出码）；False＝FAIL。
        mark = "FAIL" if ok is False else ("EXEMPT" if ok == "EXEMPT" else "PASS")
        print("  [%s] %s" % (mark, code))
        print("         %s" % name)
        print("         %s" % detail)
        if mark == "FAIL":
            fails += 1
    print("-" * 78)
    print("  合计 %d 项，FAIL %d 项" % (len(rows), fails))
    return fails


def cmd_selftest():
    """正例 3 例＋反例 34 例＋P4 数据面 2 例，各自独立临时根；断言正例零 FAIL、反例命中指定判据码。

    全部在临时目录，不触碰真实工作区；反例覆盖 B2／B3／B4／B5／B6／C2／C7（谱系＋
    进步叙事与等级修辞＋历史必然词组＋劳动禁词，R31／R32）／C9（原 C4 重编，G-01）／
    C8a／C8b／C8c／F2／F3／G1／H1／A2／A3／D1／G2／H2／H3，另含 B7 全角括号内
    ASCII 连字符（G-19）、D3 V01–V50 豁免（EXEMPT 且 B2 照判不外溢，G-02）与
    D3 V51+ 照判两组豁免用例；正例含「偶然性与必然性」辩证合法用例与 B7 U+2013
    正形各一（零误报）。
    """
    good = ["自动计算的观念源流", "差分机与通用计算的分离", "形式化纲领的边界"]
    TAB = "\t"

    def newroot():
        tmp = tempfile.mkdtemp(prefix="atc_")
        base = os.path.join(tmp, "05-卷册大纲", "映射")
        dd = os.path.join(base, "title-design")
        ed = os.path.join(base, "title-evidence")
        od = os.path.join(dd, "approved")
        for d in (dd, ed, od, os.path.join(dd, "exceptions")):
            os.makedirs(d, exist_ok=True)
        return tmp, dd, ed, od

    def w(p, s):
        with io.open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(s)

    def build(vol, titles, sources="史料;联网", orders=None, ok_mode=None,
              thesis="本小节论证一个可命名的论题", status="final",
              secs=None, id_secs=None):
        tmp, dd, ed, od = newroot()
        n = len(titles)
        secs = secs if secs else [1] * n
        id_secs = id_secs if id_secs else secs
        lines = [TAB.join(DESIGN_HDR)]
        for i, t in enumerate(titles):
            o = orders[i] if orders else i + 1
            n_src = len([x for x in sources.split(";") if x.strip()])
            sid = "V%s.1.%d.%d" % (vol, id_secs[i], i + 1)
            lines.append(TAB.join([sid, vol, "1", str(secs[i]), t,
                                   thesis, str(o), str(n_src), sources, status]))
        ledger = os.path.join(dd, "V%s.tsv" % vol)
        w(ledger, "\n".join(lines) + "\n")

        ev = [TAB.join(EVID_HDR)]
        for i in range(n):
            sid = "V%s.1.%d.%d" % (vol, id_secs[i], i + 1)
            ev.append(TAB.join([sid, "q", "https://example.org",
                                "史料", "A", "2026-10-29", "引文", "none"]))
        w(os.path.join(ed, "V%s.tsv" % vol), "\n".join(ev) + "\n")

        appr = os.path.join(dd, "approvals.tsv")
        if ok_mode in ("good", "noappr"):
            body = TAB.join(APPR_HDR) + "\n"
            if ok_mode == "good":
                body += TAB.join(["title", "V%s" % vol, str(n), _sha(ledger), "ykla",
                                  "2026-10-29", "首轮"]) + "\n"
            w(appr, body)
            w(os.path.join(od, "V%s.title.ok" % vol),
              "kind=title\nvol=V%s\ntitle_count=%d\nledger_sha256=%s\n"
              "approved_by=ykla\napproved_at=2026-10-29\n"
              % (vol, n, _sha(ledger)))
        elif ok_mode == "badhash":
            w(appr, TAB.join(APPR_HDR) + "\n")
            w(os.path.join(od, "V%s.title.ok" % vol),
              "kind=title\nvol=V%s\ntitle_count=%d\nledger_sha256=%s\n"
              "approved_by=ykla\napproved_at=2026-10-29\n"
              % (vol, n, "0" * 64))
        else:
            w(appr, TAB.join(APPR_HDR) + "\n")
        return tmp

    cases = []

    tmp = build("01", good, "史料;联网;目录;规则", ok_mode="good")
    rows = run(tmp)
    n_fail = sum(1 for _, _, ok, _ in rows if not ok)
    cases.append(("正例（全合规，期望零 FAIL）", n_fail == 0, "FAIL=%d" % n_fail))

    def expect(label, code, titles, sources="史料;联网", orders=None, ok_mode=None, **kw):
        t2 = build("02", titles, sources, orders=orders, ok_mode=ok_mode, **kw)
        r2 = run(t2)
        hit = any((not ok) and c == code for c, _, ok, _ in r2)
        cases.append((label, hit, "期望命中 %s" % code))

    expect("反例 B2 日期起头", "B2", ["1975 年 UNIX 的分裂"] + good[1:])
    expect("反例 B3 转述动词", "B3", ["宣布 X 的合并"] + good[1:])
    expect("反例 B4 纯版本号", "B4", ["2.6.19-rc2"] + good[1:])
    expect("反例 B5 工序词", "B5", ["待定的技术路线"] + good[1:])
    expect("反例 B6 超 40 字", "B6",
           ["这是一条被刻意写得非常非常长的小节标题用于验证四十字硬上限是否真的会被门禁拦下并报错"] + good[1:])
    expect("反例 C2 ASCII 直引号", "C2", ['"自由"的两种含义'] + good[1:])
    expect("反例 C7 谱系禁词", "C7", ["Unix 谱系的分岔"] + good[1:])
    expect("反例 C8a AI 空转词", "C8a", ["系统架构的赋能设计"] + good[1:])
    expect("反例 C8b 同尾簇超限", "C8b",
           ["管道机制的引入过程", "文件系统的形成过程", "命令解释的演化过程", "编程风格的定型过程"])
    expect("反例 C8c 三重“的”", "C8c", ["系统的状态的管理的统一"] + good[1:])
    expect("反例 F2 专名题仅 2 源", "F2",
           ["TCP/IP 的移植", "内核接口的约定", "许可安排的演变"])
    expect("反例 F3 单源题", "F3", good, sources="史料")
    expect("反例 G1 同节重复", "G1", [good[0], good[0], good[2]])
    expect("反例 H1 title.ok hash 不符", "H1", good, ok_mode="badhash")
    expect("反例 A2 id 与 section 不对位", "A2", good, id_secs=[2, 1, 1])
    expect("反例 A3 order 有洞", "A3", good, orders=[1, 3, 4])
    expect("反例 D1 thesis 为空", "D1", good, thesis="")
    expect("反例 G2 同卷跨节重名", "G2", [good[0], good[1], good[0]],
           secs=[1, 1, 2])
    expect("反例 H2 有 title.ok 无 approvals 行", "H2", good, ok_mode="noappr")
    expect("反例 H3 已批卷残留 draft", "H3", good, ok_mode="good", status="draft")

    # ---- 2026-11-04 增补（3A6-2 P4 前置批）：D3 豁免／C9 重编／C7 新禁词／B7 连字符
    long_t = "从早期分时系统到个人工作站的终端设备演进过程及其影响"
    src3 = "史料;联网;目录"

    # D3 豁免命中：V22（V01–V50 段）极差 18 → 标 EXEMPT 并注明 2026-11-02 改判依据；
    # 同节 B2 照判 FAIL，证豁免不外溢其他判据。
    t2 = build("22", ["1975 年 UNIX 的分裂", long_t, good[2]], sources=src3)
    r2 = run(t2)
    d3rows = [(ok, det) for c, _, ok, det in r2 if c == "D3"]
    ok_d3 = (len(d3rows) == 1 and d3rows[0][0] == "EXEMPT"
             and "2026-11-02" in d3rows[0][1]
             and any((not ok) and c == "B2" for c, _, ok, _ in r2))
    cases.append(("D3 豁免命中（V22 极差超限标 EXEMPT，B2 照判不外溢）", ok_d3,
                  "期望 D3=EXEMPT 且 B2 FAIL"))

    # D3 豁免不命中：V62（V51+ 段）同形极差 → 照判 FAIL。
    t2 = build("62", [long_t, good[1], good[2]], sources=src3)
    r2 = run(t2)
    ok_d3 = any((not ok) and c == "D3" for c, _, ok, _ in r2)
    cases.append(("D3 豁免不命中（V62 极差超限照判 FAIL）", ok_d3, "期望命中 D3"))

    # C9 重编：反斜杠题命中 C9，且输出中不再存在 C4 判据码。
    t2 = build("02", ["路径里的 \\ 与转义"] + good[1:])
    r2 = run(t2)
    ok_c9 = (any((not ok) and c == "C9" for c, _, ok, _ in r2)
             and all(c != "C4" for c, _, _, _ in r2))
    cases.append(("反例 C9 反斜杠（原 C4 重编，C4 码不再存在）", ok_c9,
                  "期望命中 C9 且无 C4"))

    # C7 新禁词（R31／R32）：逐词命中。
    for label, t in (("黄金时代", "UNIX 的黄金时代"),
                     ("飞跃", "性能的飞跃与代价"),
                     ("正统", "UNIX 的正统之争"),
                     ("主流＋支流", "主流与支流的分野"),
                     ("成败", "版本迁移的成败得失"),
                     ("历史必然（词组）", "开放标准的历史必然"),
                     ("必然趋势（词组）", "标准化推进的必然趋势"),
                     ("劳动", "劳动与贡献的区分"),
                     ("雇佣", "雇佣关系的项目史"),
                     ("资本", "资本与贡献的区分")):
        expect("反例 C7 %s" % label, "C7", [t] + good[1:], sources=src3)

    # C7 合法用例不误报：「偶然性与必然性」辩证用法裸「必然」不拦，全卷零 FAIL。
    tmp = build("03", ["偶然性与必然性：早期分时的两条路线", good[1], good[2]],
                sources=src3)
    rows = run(tmp)
    n_fail = sum(1 for _, _, ok, _ in rows if not ok)
    cases.append(("C7 正例：偶然性与必然性（辩证合法，零 FAIL）", n_fail == 0,
                  "FAIL=%d" % n_fail))

    # C7 技术义「失败」白名单（2026-11-04 P7-1）：机器操作义零 FAIL；评价义照判 FAIL。
    for label, t in (("构建失败", "构建失败的分类表"),
                     ("装载失败", "装载失败的处置规程"),
                     ("构建的失败（带“的”）", "Port 构建的失败"),
                     ("校验失败", "校验失败的处理法"),
                     ("失败监测（技术对象在后）", "tinderbox 的失败监测")):
        tmp = build("07", [t, good[1], good[2]], sources=src3)
        rows = run(tmp)
        n_fail = sum(1 for _, _, ok, _ in rows if not ok)
        cases.append(("C7 正例：技术义「%s」零 FAIL" % label, n_fail == 0,
                      "FAIL=%d" % n_fail))
    expect("反例 C7 评价义失败（非技术语境仍拦）", "C7",
           ["失败项目的归档与记述"] + good[1:], sources=src3)

    # B7 扩展：全角括号内年份区间用 ASCII 连字符命中。
    expect("反例 B7 全角括号内 ASCII 连字符", "B7",
           ["网络栈的重构（1980-2026）", good[1], good[2]], sources=src3)

    # B7 U+2013 正形不误报：零 FAIL。
    tmp = build("04", ["网络栈的重构（1980–2026）", good[1], good[2]], sources=src3)
    rows = run(tmp)
    n_fail = sum(1 for _, _, ok, _ in rows if not ok)
    cases.append(("B7 正例：U+2013 正形（零 FAIL）", n_fail == 0, "FAIL=%d" % n_fail))

    # ---- 2026-11-04 P4 增补自检：collect 逐题命中（--json 数据面）＋例外台账扩展列兼容
    col = {}
    t2 = build("05", ["Unix 谱系的分岔", good[1], good[2]], sources=src3)
    run(t2, col)
    ok_json = ("C7" in col and col["C7"]["ok"] is False
               and col["C7"]["title_ids"] == ["V05.1.1.1"])
    cases.append(("collect 逐题命中（C7 title_ids 精确到题）", ok_json, "期望 V05.1.1.1"))

    t3 = build("06", good, sources=src3)
    exdir = os.path.join(t3, "05-卷册大纲", "映射", "title-design", "exceptions")
    os.makedirs(exdir, exist_ok=True)
    w(os.path.join(exdir, "V06.tsv"),
      TAB.join(EXC_HDR + list(EXC_HDR_EXT)) + "\n" +
      TAB.join(["V06.1.1.1", "corpus_gap", "无史料", "改题", "open", "2026-10-29", "git"]) + "\n")
    try:
        r3 = run(t3, {})
        ok_exc = (any(c == "I2" and det.startswith("非法 0") for c, _, _, det in r3)
                  and any(c == "D4" and "例外台账共 1 条" in det for c, _, _, det in r3))
    except ValueError:
        ok_exc = False
    cases.append(("例外台账扩展两列兼容（registered_date／date_src 不判 schema 违约）",
                  ok_exc, "期望 I2 非法 0 且例外行数计入 1"))

    bad = [c for c in cases if not c[1]]
    for label, ok, detail in cases:
        print("  [%s] %s（%s）" % ("PASS" if ok else "FAIL", label, detail))
    print("-" * 78)
    print("  selftest：%d 例，未达预期 %d 例" % (len(cases), len(bad)))
    return 0 if not bad else 1


def find_root():
    cur = os.path.abspath(os.path.dirname(__file__))
    for _ in range(8):
        if os.path.isdir(os.path.join(cur, "05-卷册大纲")):
            return cur
        cur = os.path.dirname(cur)
    return os.getcwd()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=None)
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--check", action="store_true",
                    help="显式校验模式（与缺省等价；供批流程统一写法）")
    ap.add_argument("--json", action="store_true",
                    help="只输出机读 JSON（含逐题命中 id），不打印人读报告")
    ap.add_argument("--json-out", default=None,
                    help="同一 JSON 落盘路径（人读报告照常打印）")
    a = ap.parse_args()
    if a.selftest:
        return cmd_selftest()
    root = os.path.abspath(a.root) if a.root else find_root()
    collect = {}
    try:
        rows = run(root, collect)
    except ValueError as e:
        print("✗ 输入违约（表头／列数不合 schema）：%s" % e)
        return 2
    except Exception:
        traceback.print_exc()
        return 2
    fails = sum(1 for _, _, ok, _ in rows if ok is False)
    if a.json or a.json_out:
        doc = {"root": root,
               "indicator_count": len(rows),
               "fail_count": fails,
               "indicators": collect}
        s = json.dumps(doc, ensure_ascii=False, indent=2, sort_keys=True)
        if a.json_out:
            with io.open(a.json_out, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(s + "\n")
        if a.json:
            print(s)
            return 0 if fails == 0 else 1
    mode = "校验（--check）" if a.check else "校验（缺省）"
    fails = report(rows, "小节标题一致性门禁（第三十九件）  %s  root=%s" % (mode, root))
    return 0 if fails == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
