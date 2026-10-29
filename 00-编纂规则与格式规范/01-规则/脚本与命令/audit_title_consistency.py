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
`<root>/05-卷册大纲/映射/title-design/exceptions/V{NN}.tsv`（例外台账）

判据分组
--------
A 台账结构（表头、唯一性、层级对位、order 连续、status 枚举）
B 形态 T1–T7（名词短语下限、禁日期起头、禁转述动词、禁纯版本号、禁工序词、长度、年代括注）
C 字符 C1–C6（中英空格、直角引号、ASCII 句读、危险字符、空白与不可见字符、术语）
D 语义 S1–S4 的可机读下限（题旨非空、层级一致、同节平行、异质登记）
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
PATTERN_TECH = re.compile(r"[A-Za-z]{2,}|POSIX|IEEE|ANSI|ISO|RFC|USENIX|ACM")
STANDARD = re.compile(r"(IEEE\s*Std|POSIX|ISO/IEC|ANSI|RFC\s*\d+|USENIX)")
YEAR_IN = re.compile(r"\d{4}")
BAD_PAREN = re.compile(r"\(\s*\d{4}|\d{4}\s*\)")
CROSS_REF = re.compile(u"（另见[^）]*）")


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


def run(root):
    rows_out = []
    design_dir = os.path.join(root, DESIGN_REL)
    evid_dir = os.path.join(root, REL, "title-evidence")
    appr = os.path.join(design_dir, "approvals.tsv")
    okdir = os.path.join(design_dir, "approved")
    excdir = os.path.join(design_dir, "exceptions")

    design = load_design(design_dir)
    evid = load_evid(evid_dir)

    if not design:
        rows_out.append(("A1", "零态：无标题台账（立线未开工，合法状态）", True, "N/A"))
        return rows_out

    # 汇总
    all_rows = []          # (vol, idx, cols)
    for vol, (p, hdr, body) in design.items():
        for i, c in enumerate(body, 2):
            if len(c) != len(DESIGN_HDR):
                raise ValueError("%s 第 %d 行列数 %d ≠ %d" % (p, i, len(c), len(DESIGN_HDR)))
            all_rows.append((vol, i, dict(zip(DESIGN_HDR, c))))

    def f(code, name, bad, detail):
        rows_out.append((code, name, not bad, detail))

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

    bad_t7 = [r["subsection_id"] for _, _, r in all_rows if BAD_PAREN.search(r["title"])]
    f("B7", "B7 年代括注须全角括号与 U+2013", bad_t7,
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

    bad_c4 = [r["subsection_id"] for _, _, r in all_rows
              if "\\" in r["title"] or any(ord(ch) < 32 or ord(ch) == 127 for ch in r["title"])]
    f("C4", "C4 禁反斜杠与控制字符（路径字符由落盘器全角化）", bad_c4,
      "命中 %d 处：%s" % (len(bad_c4), "、".join(bad_c4[:5]) or "无"))

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

    # ---------------- D 语义下限
    bad_d1 = ["%s（thesis 空或过短）" % r["subsection_id"] for _, _, r in all_rows
              if len(r["thesis"].strip()) < 8]
    f("D1", "D1 S1 题旨非空（thesis ≥8 字）", bad_d1,
      "不符 %d 处：%s" % (len(bad_d1), "、".join(bad_d1[:5]) or "无"))

    f("D2", "D2 S2 上下位一致（依赖 A2 层级对位）", bad2, "同 A2")

    bad_d3 = []
    for k, rs in by_sec.items():
        lens = [_title_len(x["title"]) for x in rs]
        if lens and (max(lens) - min(lens)) > 14:
            bad_d3.append("V%s.%s.%s（极差 %d）" % (k[0], k[1], k[2], max(lens) - min(lens)))
    f("D3", "D3 S3 同节平行：字数极差 ≤14", bad_d3,
      "越界节 %d 个：%s" % (len(bad_d3), "、".join(bad_d3[:3]) or "无"))

    n_exc = 0
    exc_rows = []
    if os.path.isdir(excdir):
        for name in sorted(os.listdir(excdir)):
            if name.endswith(".tsv"):
                hdr, body = _rows(os.path.join(excdir, name))
                if hdr is None:
                    continue
                if hdr != EXC_HDR:
                    raise ValueError("%s 表头不合 schema" % name)
                exc_rows.extend(body)
    n_exc = len(exc_rows)
    bad_d4 = [c[0] for c in exc_rows
              if len(c) == len(EXC_HDR) and c[1] == "single_source" and c[0] in seen]
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
    bad_g1, bad_g2 = [], []
    for k, rs in by_sec.items():
        ts = [x["title"] for x in rs]
        dup = sorted({t for t in ts if ts.count(t) > 1})
        if dup:
            bad_g1.append("V%s.%s.%s：%s" % (k[0], k[1], k[2], "／".join(dup[:2])))
    for vol, (p, hdr, body) in design.items():
        ts = [dict(zip(DESIGN_HDR, c))["title"] for c in body]
        groups = {}
        for t in ts:
            cross = bool(CROSS_REF.search(t))
            base = CROSS_REF.sub("", t).strip()
            groups.setdefault(base, []).append(cross)
        for base, flags in groups.items():
            n_cross = sum(1 for x in flags if x)
            n_bare = len(flags) - n_cross
            if n_bare > 1 or n_cross > 1 or (n_cross and n_bare == 0):
                bad_g2.append("V%s：%s（主 %d／从 %d）" % (vol, base[:26], n_bare, n_cross))
    f("G1", "G1 同节内题名不重复", bad_g1,
      "重复 %d 节：%s" % (len(bad_g1), "、".join(bad_g1[:3]) or "无"))
    f("G2", "G2 同卷内题名不重复（每基名主 1 从 ≤1）", bad_g2,
      "重复 %d 卷：%s" % (len(bad_g2), "、".join(bad_g2[:3]) or "无"))

    # ---------------- H 批准一致
    appr_rows = []
    if os.path.exists(appr):
        hdr, body = _rows(appr)
        if hdr != APPR_HDR:
            raise ValueError("approvals.tsv 表头不合 schema")
        appr_rows = [dict(zip(APPR_HDR, c)) for c in body]

    bad_h1, bad_h2, bad_h3 = [], [], []
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
    f("H1", "H1 title.ok 的 ledger_sha256 与台账一致", bad_h1,
      "不符 %d 处：%s" % (len(bad_h1), "、".join(bad_h1[:3]) or "无"))
    f("H2", "H2 每份 title.ok 有 approvals 行", bad_h2,
      "缺行 %d 处：%s" % (len(bad_h2), "、".join(bad_h2[:3]) or "无"))
    f("H3", "H3 已批卷无 draft 残留", bad_h3,
      "残留 %d 卷：%s" % (len(bad_h3), "、".join(bad_h3[:3]) or "无"))

    # ---------------- I 例外
    bad_i1 = [c[0] for c in exc_rows if len(c) == len(EXC_HDR) and c[0] not in seen]
    bad_i2 = [c[0] for c in exc_rows
              if len(c) == len(EXC_HDR) and (c[1] not in EXC_KIND or c[4] not in EXC_STATUS)]
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
        print("  [%s] %s" % ("PASS" if ok else "FAIL", code))
        print("         %s" % name)
        print("         %s" % detail)
        if not ok:
            fails += 1
    print("-" * 78)
    print("  合计 %d 项，FAIL %d 项" % (len(rows), fails))
    return fails


def cmd_selftest():
    """正例 1 例＋反例 16 例，各自独立临时根；断言正例零 FAIL、反例命中指定判据码。

    全部在临时目录，不触碰真实工作区；反例覆盖 B2／B3／B4／B5／B6／C2／F2／F3／G1／H1／
    A2／A3／D1／G2／H2／H3 十六类。
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
    a = ap.parse_args()
    if a.selftest:
        return cmd_selftest()
    root = os.path.abspath(a.root) if a.root else find_root()
    try:
        rows = run(root)
    except ValueError as e:
        print("✗ 输入违约（表头／列数不合 schema）：%s" % e)
        return 2
    except Exception:
        traceback.print_exc()
        return 2
    mode = "校验（--check）" if a.check else "校验（缺省）"
    fails = report(rows, "小节标题一致性门禁（第三十九件）  %s  root=%s" % (mode, root))
    return 0 if fails == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
