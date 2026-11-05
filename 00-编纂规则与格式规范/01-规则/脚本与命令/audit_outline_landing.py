# -*- coding: utf-8 -*-
"""audit_outline_landing.py —— 大纲落地一致性门禁 L1–L19（第三十七件，固定脚本）。

用途
----
对 `05-卷册大纲/` 落地树做 L1–L19 全量一致性审计，回答“目录真值、映射台账、
磁盘落点、派生件四者是否自洽”。判据正文见 `流程规则.md`“大纲落地一致性门禁
（L1–L19）”；本器是唯一执行件。

判据（每条一行结果为 PASS／FAIL／SKIP）
----
L1  落点节数守恒：树 卷／章／节 计数 == `映射/targets.tsv` 中 status=active 的
    三级节点计数。
L2  已确认映射落地：mapping 中 status=CONFIRMED 的每条，其 layout 落点文件存在。
L3  落点无多余 .md：树内 `.md` 集合 == CONFIRMED 映射落点集合。
L4  H1 与路径一致：小节文件名 `M.N.P-slug.md` 的 M.N.P 与首行 `# M.N.P ` 一致。
L5  旧三段号未决：落点正文含旧式 `0NN.M.P` 三段号且该文件对应 source_id 未在
    `映射/ref-unresolved.tsv` 挂账。
L6  落点无重复内容：落点 `.md` 的 SHA-256 无重复组。
L7  SUMMARY 节条目齐全：每条 CONFIRMED 落点的父节目录名在 `SUMMARY.md` 有
    条目行（2026-10-28 SUMMARY 去链接化后口径；文件级列举由镜像器 validate 双射覆盖）。
L8  主题索引口径：`chapter_keywords.json` 的 `meta.schema==theme-index/4`，
    `meta.volumes/chapters/sections` 与树计数一致，`sections` 键数 == 节数。
L9  落点编码：落点 `.md` 无 BOM、无 CRLF。
L10 无散件：卷层只允许章目录，章层只允许节目录，节层只允许 `.md` 与 `.gitkeep`。
L11 布局零漂移：`映射/layout.tsv` 每条 dest 在磁盘存在。
L12 TARGET_LOST 挂账：mapping 标 TARGET_LOST 者须在 `映射/target-lost.tsv`。
L13 路径合规：>260 字符的落点须在 `映射/path-overlong.tsv`；文件名禁
    `< > : " / \\ | ? *` 与反引号。
L14 活动复合键唯一：active 节的 `V{卷}-C{卷内章}-{节号}` 无重复。
L15 REMAP 挂账与后继：mapping 标 REMAP 者须在 `映射/remap.tsv`；其
    `successor_ids` 非空且全部为 active 目标。
L16 旧二段号未决：落点正文含旧式 `0NN.M` 二段号（排除日期形态）且未挂账。
L17 节占位互斥：节目录内 `.md` 与 `.gitkeep` 不得并存；无 `.md` 时必须有 `.gitkeep`。
L18 落点名长度：落点单段文件名（UTF-8 字节）须 ≤255。Linux 的 NAME_MAX 按字节计，
    超限时 checkout 直接 ENAMETOOLONG；本机 NTFS 按字符计，故只能在门禁侧拦。

SKIP 语义
--------
L2／L3／L5／L6／L7／L11／L12／L13／L15／L16 依赖 `映射/mapping.tsv` 与
`映射/layout.tsv`；二者不存在时这些判据标 SKIP（映射基础设施未建，非缺陷），
不计 FAIL。L1／L4／L8／L9／L10／L14／L17／L18 只依赖目录真值与磁盘，常时可判。

用法
----
    python audit_outline_landing.py                # 默认 --check，打印逐条结果
    python audit_outline_landing.py --json         # 附 JSON 汇总
    python audit_outline_landing.py --selftest     # 合成夹具自检（含负向注入）
    python audit_outline_landing.py --root <大纲根> --map <映射层>

退出码：0＝无 FAIL（可能有 SKIP）；1＝至少一条 FAIL；2＝致命错误（根或派生件缺失）。
"""
from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import io
import json
import os
import re
import shutil
import sys
import tempfile

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
DEFAULT_ROOT = os.path.join(REPO, "05-卷册大纲")

VOL_RE = re.compile(r"^第(\d{1,3})卷(?:-(?P<slug>.+))?$")
CH_RE = re.compile(r"^第(\d{1,3})章(?:-(?P<slug>.+))?$")
SEC_RE = re.compile(r"^(\d{1,3})\.(\d{1,3})-(?P<slug>.+)$")
SUB_RE = re.compile(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,4})-(?P<slug>.+\.md)$")

# 依赖映射台账的判据：mapping.tsv 缺失即 SKIP
NEEDS_MAPPING = {"L2", "L3", "L5", "L6", "L7", "L11", "L12", "L13", "L15", "L16"}
ILLEGAL_NAME = set('<>:"/\\|?*`')
OLD3 = re.compile(r"(?<![\d.])0\d{2}\.\d{1,2}\.\d{1,4}(?![\d.])")
OLD2 = re.compile(r"(?<![\d.])0\d{2}\.\d{1,2}(?![\d.])")


def read_tsv(path):
    """读 TSV（首行表头）；文件不存在返回 None。utf-8-sig 吞 BOM 防表头污染。"""
    if not os.path.isfile(path):
        return None
    with open(path, encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def _need_cols(path, need, name):
    """表头契约：读首行原文判列，缺列即致命（空文件同样受检）。"""
    if not os.path.isfile(path):
        return
    with open(path, encoding="utf-8-sig", newline="") as fh:
        head = fh.readline()
    cols = {c.strip() for c in head.rstrip("\r\n").split("\t") if c.strip()}
    miss = need - cols
    if miss:
        print("FATAL %s 缺列：%s（实有 %s）" % (name, sorted(miss), sorted(cols)))
        raise SystemExit(2)


def _norm_status(rows):
    """status 统一去空白并大写（mapping 与 targets 同用）。"""
    for r in rows or []:
        r["status"] = (r.get("status") or "").strip().upper()
    return rows


def _dest_ok(root, rel):
    """dest 必须为大纲根内相对路径且指向文件。返回 (ok, reason)。"""
    if not rel:
        return False, "空"
    if os.path.isabs(rel) or re.match(r"^[A-Za-z]:", rel):
        return False, "绝对路径"
    n = _norm(rel)
    if n == ".." or n.startswith("../") or "/../" in n:
        return False, "越界"
    if not os.path.isfile(os.path.join(root, rel)):
        # 双约定兼容（2026-10-28 落地并行期）：dest 带"05-卷册大纲/"仓库相对前缀时剥前缀重试
        if n.startswith("05-卷册大纲/") and os.path.isfile(
                os.path.join(root, n[len("05-卷册大纲/"):])):
            return True, ""
        return False, "缺文件或指向目录"
    return True, ""


def _dest_rel05(rel):
    """layout dest 归一为 05-卷册大纲 相对（兼容仓库相对带前缀形态）。"""
    n = _norm(rel or "")
    return n[len("05-卷册大纲/"):] if n.startswith("05-卷册大纲/") else n


def _strip_code(text):
    """剥离非引用面：围栏代码、HTML 注释、缩进代码、行内代码、链接目标与裸 URL。

    依据“引用与代码块逐字保真”红线——这些位置的旧号不是正文引用，不应判未决。
    """
    out, fence = [], False
    for ln in text.split("\n"):
        s = ln.lstrip()
        if s.startswith("```") or s.startswith("~~~"):
            fence = not fence
            continue
        if fence:
            continue
        out.append(ln)
    text = "\n".join(out)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"(?m)^(?: {4,}|\t).*$", "", text)
    text = re.sub(r"`[^`]*`", "", text)
    text = re.sub(r"\]\([^)]*\)", "]", text)
    text = re.sub(r"https?://\S+", "", text)
    return text


def scan_tree(root):
    """扫描大纲树：返回 (vols, chs, secs, subs, anomalies)。"""
    vols, chs, secs, subs, anomalies = [], [], [], [], []
    for vname in sorted(os.listdir(root)):
        vfull = os.path.join(root, vname)
        if not os.path.isdir(vfull) or not VOL_RE.match(vname):
            continue
        vols.append(vname)
        for cname in sorted(os.listdir(vfull)):
            cfull = os.path.join(vfull, cname)
            if not os.path.isdir(cfull):
                anomalies.append(("vol_file", os.path.join(vname, cname), "卷层散件"))
                continue
            if not CH_RE.match(cname):
                anomalies.append(("vol_baddir", os.path.join(vname, cname), "卷层非章目录"))
                continue
            chs.append(os.path.join(vname, cname))
            for sname in sorted(os.listdir(cfull)):
                sfull = os.path.join(cfull, sname)
                if not os.path.isdir(sfull):
                    anomalies.append(("ch_file", os.path.join(vname, cname, sname), "章层散件"))
                    continue
                if not SEC_RE.match(sname):
                    anomalies.append(("ch_baddir", os.path.join(vname, cname, sname),
                                      "章层非节目录"))
                    continue
                sec_rel = os.path.join(vname, cname, sname)
                secs.append(sec_rel)
                for f in sorted(os.listdir(sfull)):
                    ff = os.path.join(sfull, f)
                    if os.path.isdir(ff):
                        anomalies.append(("sec_dir", os.path.join(sec_rel, f), "节层子目录"))
                        continue
                    if f == ".gitkeep":
                        continue
                    if not SUB_RE.match(f):
                        anomalies.append(("sec_file", os.path.join(sec_rel, f), "节层散件"))
                        continue
                    subs.append(os.path.join(sec_rel, f))
    return vols, chs, secs, subs, anomalies


def count_vol_ch_sec(targets):
    """由 targets.tsv 统计 active 四级节点数（status 已归一为大写；ADR-0020 四级）。"""
    active = [r for r in targets if (r.get("status") or "") == "ACTIVE"]
    nv = sum(1 for r in active if r.get("level") == "vol")
    nc = sum(1 for r in active if r.get("level") == "ch")
    ns = sum(1 for r in active if r.get("level") == "sec")
    nss = sum(1 for r in active if r.get("level") == "subsec")
    return nv, nc, ns, nss, active


_CN2 = "一二三四五六七八九十"


def _cn2int(s):
    """中文数字 → int（1–99；阿拉伯直返；失败 None）。"""
    if s.isdigit():
        return int(s)
    if s in _CN2:
        return _CN2.index(s) + 1
    if s == "十":
        return 10
    if s.startswith("十"):
        return 10 + _CN2.index(s[1]) + 1
    if "十" in s:
        a, _, b = s.partition("十")
        if a in _CN2 and b in _CN2:
            return (_CN2.index(a) + 1) * 10 + (_CN2.index(b) + 1 if b else 0)
    return None


def outline_sub_keys(outline_path):
    """outline.txt → 小节行键集合 {(卷号, M, N, P)}（ADR-0020 L19 第一向）。"""
    keys = set()
    v = None
    with io.open(outline_path, encoding="utf-8") as fh:
        for raw in fh:
            line = raw.rstrip("\r\n").rstrip()
            if not line.strip():
                continue
            if line.startswith("## "):
                mc = re.match(r"^##\s*第\s*(\d{1,3})\s*章", line)
                continue
            if line.startswith("# "):
                mv = re.match(r"^#\s*第\s*([一二三四五六七八九十]+)卷", line)
                v = _cn2int(mv.group(1)) if mv else None
                continue
            ms = re.match(r"^  -\s+(\d{1,3})\.(\d{1,3})\.(\d{1,4})\s", line)
            if ms:
                if v is not None:
                    keys.add((v, int(ms.group(1)), int(ms.group(2)), int(ms.group(3))))
    return keys


def summary_sub_keys(summary_path):
    """SUMMARY.md → 小节条目键集合（缩进 12 行，磁盘名前缀 M.N.P；L19 第三向）。"""
    keys = set()
    v = None
    with io.open(summary_path, encoding="utf-8") as fh:
        for raw in fh:
            line = raw.rstrip("\r\n")
            if not line.strip():
                continue
            indent = len(line) - len(line.lstrip(" "))
            s = line.strip()
            if s.startswith("- "):
                s = s[2:]
            if indent == 0:
                mv = re.match(r"^第(\d{1,3})卷", s)
                v = int(mv.group(1)) if mv else None
            elif indent >= 12:
                ms = re.match(r"^(\d+)\.(\d+)\.(\d+)-", s)
                if ms and v is not None:
                    keys.add((v, int(ms.group(1)), int(ms.group(2)), int(ms.group(3))))
    return keys


def _norm(p):
    return p.replace("\\", "/")


def run_gate(root, mapdir):
    """执行 L1–L19，返回 [(判据, 结果, 说明)]。"""
    if not os.path.isdir(root):
        print("FATAL 大纲根不存在或不是目录：%s" % root)
        raise SystemExit(2)
    mapdir = mapdir or os.path.join(root, "映射")
    targets = read_tsv(os.path.join(mapdir, "targets.tsv"))
    if targets is None:
        print("FATAL 缺 %s/targets.tsv（目标注册表；先跑 outline_registry.py --write）" % mapdir)
        raise SystemExit(2)
    mapping = read_tsv(os.path.join(mapdir, "mapping.tsv"))
    layout = read_tsv(os.path.join(mapdir, "layout.tsv"))
    _need_cols(os.path.join(mapdir, "mapping.tsv"), {"source_id", "status"}, "mapping.tsv")
    _need_cols(os.path.join(mapdir, "layout.tsv"), {"source_id", "dest_relpath"}, "layout.tsv")
    _norm_status(mapping)
    _norm_status(targets)
    if (mapping is None) != (layout is None):
        print("FATAL 映射台账半损：mapping.tsv=%s、layout.tsv=%s（两件须同存同缺，防半损被判绿）"
              % ("在" if mapping is not None else "缺", "在" if layout is not None else "缺"))
        raise SystemExit(2)
    has_map = mapping is not None and layout is not None

    vols, chs, secs, subs, anomalies = scan_tree(root)
    nv, nc, ns, nss, active = count_vol_ch_sec(targets)
    res = []

    def add(no, ok, detail):
        res.append((no, "PASS" if ok else "FAIL", detail))

    def skip(no, reason):
        res.append((no, "SKIP", reason))

    # L1 落点层级守恒（2026-11-06 四级：卷/章/节/小节，ADR-0020）
    add("L1", (len(vols), len(chs), len(secs), len(subs)) == (nv, nc, ns, nss),
        "tree=%d/%d/%d/%d targets=%d/%d/%d/%d"
        % (len(vols), len(chs), len(secs), len(subs), nv, nc, ns, nss))

    lay = {r.get("source_id"): r for r in (layout or [])}
    confirmed = [r for r in (mapping or []) if (r.get("status") or "") == "CONFIRMED"]

    # L2 已确认映射落地（空 dest_relpath 一律计缺失，防 join(root,"") 假 PASS）
    if not has_map:
        skip("L2", "映射基础设施未建（mapping.tsv／layout.tsv 不存在）")
    else:
        miss = []
        for r in confirmed:
            rel = (lay.get(r.get("source_id")) or {}).get("dest_relpath") or ""
            ok, _why = _dest_ok(root, rel)
            if not ok:
                miss.append(r.get("source_id"))
        add("L2", not miss, "confirmed=%d missing=%d" % (len(confirmed), len(miss)))

    dest_md = [os.path.join(root, p) for p in subs]
    # L3 落点无多余 .md
    if not has_map:
        skip("L3", "映射基础设施未建")
    else:
        mapped = {_dest_rel05(lay[r["source_id"]].get("dest_relpath"))
                  for r in confirmed if r.get("source_id") in lay}
        extra = [_norm(os.path.relpath(p, root)) for p in dest_md
                 if _norm(os.path.relpath(p, root)) not in mapped]
        add("L3", not extra, "dest_md=%d mapped=%d extra=%d" % (len(dest_md), len(mapped), len(extra)))

    # L4 H1 与路径一致（数字边界防 1.1.10 冒充 1.1.1；支持 YAML frontmatter 前置）
    h1bad, empty = [], []
    for p in dest_md:
        m = SUB_RE.match(os.path.basename(p))
        if not m:
            continue
        with open(p, encoding="utf-8", errors="replace") as fh:
            lines = fh.read().split("\n")
        if not "".join(lines).strip():
            empty.append(os.path.relpath(p, root))
            continue
        start = 0
        if lines and lines[0].strip() == "---":
            for i in range(1, len(lines)):
                if lines[i].strip() == "---":
                    start = i + 1
                    break
        h1 = next((ln for ln in lines[start:] if ln.startswith("# ")), "")
        pat = re.compile(r"^# %s\.%s\.%s(?!\d)" % (m.group(1), m.group(2), m.group(3)))
        if not pat.match(h1):
            h1bad.append(os.path.relpath(p, root))
    add("L4", not h1bad and not empty,
        "subs=%d h1/path mismatch=%d empty=%d" % (len(dest_md), len(h1bad), len(empty)))

    # L5／L16 旧号未决
    unresolved = set()
    up = read_tsv(os.path.join(mapdir, "ref-unresolved.tsv"))
    if up:
        unresolved = {r.get("source_id") for r in up if r.get("source_id")}
    src_by_dest = {_dest_rel05(lay[r["source_id"]].get("dest_relpath")): r.get("source_id")
                   for r in confirmed if r.get("source_id") in lay}

    def oldref_hits(pat):
        hits = []
        for p in dest_md:
            rel = _norm(os.path.relpath(p, root))
            with open(p, encoding="utf-8", errors="replace") as fh:
                text = _strip_code(fh.read())
            if pat.search(text) and src_by_dest.get(rel) not in unresolved:
                hits.append(rel)
        return hits

    if not has_map:
        skip("L5", "映射基础设施未建")
        skip("L16", "映射基础设施未建")
    else:
        h5 = oldref_hits(OLD3)
        add("L5", not h5, "ledger=%d unlisted old3=%d" % (len(unresolved), len(h5)))
        h16 = oldref_hits(OLD2)
        add("L16", not h16, "ledger=%d unlisted old2=%d" % (len(unresolved), len(h16)))

    # L6 重复内容
    if not has_map:
        skip("L6", "映射基础设施未建")
    else:
        seen = {}
        for p in dest_md:
            with open(p, "rb") as fh:
                h = hashlib.sha256(fh.read()).hexdigest()
            seen.setdefault(h, []).append(os.path.relpath(p, root))
        dups = {h: v for h, v in seen.items() if len(v) > 1}
        add("L6", not dups, "duplicate hash groups=%d" % len(dups))

    # L7 SUMMARY 节条目齐全（SUMMARY 2026-10-27 去链接化改纯文本后，链接判据失配；
    # 新口径＝每条 CONFIRMED 落点的父节目录名在 SUMMARY.md 有条目行，缺行／空 dest
    # 计失败，不索引崩溃；文件级列举由镜像器 validate 双射在收口覆盖）
    if not has_map:
        skip("L7", "映射基础设施未建")
    else:
        sp = os.path.join(root, "SUMMARY.md")
        summary = open(sp, encoding="utf-8").read() if os.path.isfile(sp) else ""
        missline, emptydest = [], []
        for r in confirmed:
            rel = (lay.get(r.get("source_id")) or {}).get("dest_relpath") or ""
            if not rel:
                emptydest.append(r.get("source_id"))
                continue
            secdir = _norm(rel).split("/")[-2]
            if not re.search(r"(?m)^\s*- %s\s*$" % re.escape(secdir), summary):
                missline.append(_norm(rel))
        add("L7", not missline and not emptydest and bool(summary),
            "summary=%s confirmed=%d missing=%d emptydest=%d"
            % ("存在" if summary else "缺失", len(confirmed), len(missline), len(emptydest)))

    # L8 主题索引口径（schema＋三元组＋键集；空树缺件按 SKIP 处理）
    kwp = os.path.join(root, "chapter_keywords.json")
    sec_keys = set()
    for r in active:
        if r.get("level") != "sec":
            continue
        try:
            sec_keys.add("V%02d-C%03d-%s" % (int(r["vol_no"]), int(r["ch_no"]),
                                             (r["sec_no"] or "").strip()))
        except (KeyError, ValueError, TypeError):
            pass
    if not os.path.isfile(kwp):
        if (nv, nc, ns) == (0, 0, 0):
            skip("L8", "空树且缺 chapter_keywords.json")
        else:
            add("L8", False, "缺 chapter_keywords.json")
    else:
        try:
            doc = json.load(open(kwp, encoding="utf-8"))
            meta = doc.get("meta") or {}
            kset = set((doc.get("sections") or {}).keys())
            nsec = len(kset)
            ok8 = (meta.get("schema") == "theme-index/4"
                   and (meta.get("volumes"), meta.get("chapters"), meta.get("sections")) == (nv, nc, ns)
                   and kset == sec_keys)
            add("L8", ok8, "schema=%s meta=%s/%s/%s keys=%d keyset=%s tree=%d/%d/%d"
                % (meta.get("schema"), meta.get("volumes"), meta.get("chapters"),
                   meta.get("sections"), nsec, "同" if kset == sec_keys else "异", nv, nc, ns))
        except Exception as exc:
            add("L8", False, "解析失败：%s" % exc)

    # L9 落点编码
    encbad = []
    for p in dest_md:
        with open(p, "rb") as fh:
            b = fh.read()
        if b.startswith(b"\xef\xbb\xbf") or b"\r\n" in b:
            encbad.append(os.path.relpath(p, root))
    add("L9", not encbad, "encoding bad=%d" % len(encbad))

    # L10 无散件（结构异常扫描已覆盖卷／章／节三层）
    add("L10", not anomalies, "stray=%d%s" % (
        len(anomalies), "" if not anomalies else "（首项：%s %s）" % (anomalies[0][1], anomalies[0][2])))

    # L11 布局零漂移（空 dest 计漂移）
    if not has_map:
        skip("L11", "映射基础设施未建")
    else:
        drift = []
        for r in (layout or []):
            rel = r.get("dest_relpath") or ""
            ok, _why = _dest_ok(root, rel)
            if not ok:
                drift.append(rel or "<空>")
        add("L11", not drift, "layout=%d drift=%d" % (len(layout or []), len(drift)))

    # L12 TARGET_LOST 挂账
    if not has_map:
        skip("L12", "映射基础设施未建")
    else:
        lost_ledger = {r.get("source_id") for r in (read_tsv(os.path.join(mapdir, "target-lost.tsv")) or [])}
        lost = [r for r in (mapping or [])
                if (r.get("status") or "") == "TARGET_LOST" and r.get("source_id") not in lost_ledger]
        add("L12", not lost, "unlisted target_lost=%d ledger=%d" % (len(lost), len(lost_ledger)))

    # L13 路径合规
    if not has_map:
        skip("L13", "映射基础设施未建")
    else:
        over_ledger = {r.get("source_id") for r in (read_tsv(os.path.join(mapdir, "path-overlong.tsv")) or [])}
        over, badname = [], []
        for r in (layout or []):
            rel = r.get("dest_relpath") or ""
            n = _norm(rel)
            unsafe = (not rel) or os.path.isabs(rel) or re.match(r"^[A-Za-z]:", rel) \
                or n == ".." or n.startswith("../") or "/../" in n
            if unsafe:
                badname.append(rel or "<空>")
            elif ILLEGAL_NAME & set(os.path.basename(rel)):
                badname.append(rel)
            elif len(os.path.join(root, _dest_rel05(rel))) > 260 and r.get("source_id") not in over_ledger:
                over.append(rel)
        add("L13", not over and not badname,
            "over260=%d ledger=%d badpath=%d" % (len(over), len(over_ledger), len(badname)))

    # L14 活动复合键唯一
    keys, badnum = [], []
    for r in active:
        if r.get("level") != "sec":
            continue
        try:
            secno = (r["sec_no"] or "").strip()
            if not secno:
                raise ValueError("sec_no 空")
            keys.append("V%02d-C%03d-%s" % (int(r["vol_no"]), int(r["ch_no"]), secno))
        except (KeyError, ValueError, TypeError):
            badnum.append(r.get("node_id"))
    dupk = [k for k, n in collections.Counter(keys).items() if n > 1]
    add("L14", not dupk and not badnum,
        "active sec keys=%d dup=%d badnum=%d" % (len(keys), len(dupk), len(badnum)))

    # L15 REMAP 挂账与后继
    if not has_map:
        skip("L15", "映射基础设施未建")
    else:
        remap_ledger = {r.get("source_id"): r
                        for r in (read_tsv(os.path.join(mapdir, "remap.tsv")) or [])}
        by_id = {r.get("node_id"): r for r in targets}
        bad_succ = []
        for sid, row in remap_ledger.items():
            ids = [x for x in re.split(r"[,;\s]+", (row.get("successor_ids") or "").strip()) if x]
            if not ids or any((by_id.get(x) or {}).get("status") != "ACTIVE" for x in ids):
                bad_succ.append(sid)
        remap = [r for r in (mapping or [])
                 if (r.get("status") or "") == "REMAP" and r.get("source_id") not in remap_ledger]
        add("L15", not remap and not bad_succ,
            "unlisted remap=%d ledger=%d bad successors=%d"
            % (len(remap), len(remap_ledger), len(bad_succ)))

    # L17 节占位互斥
    both, nogk = [], []
    for rel in secs:
        sp = os.path.join(root, rel)
        names = os.listdir(sp)
        has_md = any(n.endswith(".md") for n in names)
        has_gk = ".gitkeep" in names
        if has_md and has_gk:
            both.append(rel)
        elif not has_md and not has_gk:
            nogk.append(rel)
    add("L17", not both and not nogk,
        "secs=%d md+gitkeep=%d empty_without_gitkeep=%d" % (len(secs), len(both), len(nogk)))

    # L18 落点名长度：单段文件名（UTF-8 字节）须 ≤255，否则 Linux 检出 ENAMETOOLONG
    # （2026-10-29 立：CI 三次因 255 字节上限在「检出」即失败，而本机 NTFS 按字符计、无感）
    n_md, overname = 0, []
    for dirpath, _dirs, files in os.walk(root):
        for fn in files:
            if not fn.endswith(".md"):
                continue
            n_md += 1
            nb = len(fn.encode("utf-8"))
            if nb > 255:
                rel = os.path.relpath(os.path.join(dirpath, fn), root).replace("\\", "/")
                overname.append((nb, rel))
    overname.sort(reverse=True)
    add("L18", not overname,
        "md=%d over255=%d%s" % (n_md, len(overname),
                                "" if not overname else
                                " 首例=%dB %s" % (overname[0][0], overname[0][1])))

    # L19 小节三向双射（ADR-0020，2026-11-06）：outline.txt 小节行 ↔ 树内 .md ↔ SUMMARY 条目。
    # 全部小节必须有 .md（含空骨架）；无"设计级豁免"。零态（三方皆空）合法 PASS。
    outline_p = os.path.join(root, "目录", "data", "outline.txt")
    summary_p = os.path.join(root, "SUMMARY.md")
    if not os.path.exists(outline_p) or not os.path.exists(summary_p):
        skip("L19", "outline.txt 或 SUMMARY.md 缺（四级三向不可判）")
    else:
        okeys = outline_sub_keys(outline_p)
        tkeys = set()
        for rel in subs:
            parts = rel.split(os.sep)
            mv, mc = VOL_RE.match(parts[0]), CH_RE.match(parts[1])
            mm = SUB_RE.match(parts[3])
            if mv and mc and mm:
                tkeys.add((int(mv.group(1)), int(mm.group(1)), int(mm.group(2)), int(mm.group(3))))
        skeys = summary_sub_keys(summary_p)
        o_no_t = sorted(okeys - tkeys)      # outline 有行、树无 .md（设计级，禁）
        t_no_o = sorted(tkeys - okeys)      # 树有 .md、outline 无行（游离）
        s_diff = sorted(skeys ^ okeys)      # SUMMARY 与 outline 不一致
        add("L19", okeys == tkeys == skeys,
            "outline=%d tree=%d summary=%d ghost_row=%d orphan_md=%d summary_diff=%d%s"
            % (len(okeys), len(tkeys), len(skeys), len(o_no_t), len(t_no_o), len(s_diff),
               "" if not (o_no_t or t_no_o or s_diff) else
               " 首例=%s" % ((o_no_t or t_no_o or s_diff)[0],)))

    # 按 L1..L19 顺序输出
    order = {("L%d" % i): i for i in range(1, 20)}
    res.sort(key=lambda t: order.get(t[0], 99))
    return res


def _mk(path, text=""):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def _write_tsv(path, header, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(header)
        w.writerows(rows)


def build_fixture(base):
    """合成夹具：2 卷 3 章 4 节 5 小节，映射完备，全判据应 PASS。"""
    root = os.path.join(base, "05-卷册大纲")
    mapdir = os.path.join(root, "映射")
    v1 = os.path.join(root, "第01卷-合成甲")
    v2 = os.path.join(root, "第02卷-合成乙")
    _mk(os.path.join(v1, "第1章-甲一", "1.1-甲一节", "1.1.1-甲一一.md"), "# 1.1.1 甲一一\n")
    _mk(os.path.join(v1, "第2章-甲二", "2.1-甲二节", "2.1.1-甲二一.md"), "# 2.1.1 甲二一\n")
    _mk(os.path.join(v2, "第1章-乙一", "1.1-乙一节", "1.1.1-乙一一.md"), "# 1.1.1 乙一一\n")
    _mk(os.path.join(v2, "第1章-乙一", "1.2-乙一二节", ".gitkeep"))
    # targets.tsv：2 卷 / 3 章 / 4 节
    targets = [
        ("V-001", "vol", "", 1, "", ""),
        ("V-002", "vol", "", 2, "", ""),
        ("C-0001", "ch", "V-001", 1, 1, ""),
        ("C-0002", "ch", "V-001", 1, 2, ""),
        ("C-0003", "ch", "V-002", 2, 1, ""),
        ("S-000001", "sec", "C-0001", 1, 1, "1.1"),
        ("S-000002", "sec", "C-0002", 1, 2, "2.1"),
        ("S-000003", "sec", "C-0003", 2, 1, "1.1"),
        ("S-000004", "sec", "C-0003", 2, 1, "1.2"),
        # 第四级 subsec（ADR-0020）：与树 3 个小节 .md 对齐（2026-11-06）
        ("SS-0000001", "subsec", "S-000001", 1, 1, "1.1.1"),
        ("SS-0000002", "subsec", "S-000002", 1, 2, "2.1.1"),
        ("SS-0000003", "subsec", "S-000003", 2, 1, "1.1.1"),
    ]
    _write_tsv(os.path.join(mapdir, "targets.tsv"),
               ["node_id", "level", "parent_id", "vol_no", "ch_no", "sec_no",
                "title", "path_title", "status", "first_seen", "last_seen", "renamed_from"],
               [r + ("t", "t", "active", "2026-10-23", "2026-10-23", "") for r in targets])
    # mapping.tsv：3 件 CONFIRMED
    srcs = [
        ("S-900001", "第01卷-合成甲/第1章-甲一/1.1-甲一节/1.1.1-甲一一.md", "CONFIRMED"),
        ("S-900002", "第01卷-合成甲/第2章-甲二/2.1-甲二节/2.1.1-甲二一.md", "CONFIRMED"),
        ("S-900003", "第02卷-合成乙/第1章-乙一/1.1-乙一节/1.1.1-乙一一.md", "CONFIRMED"),
    ]
    _write_tsv(os.path.join(mapdir, "mapping.tsv"),
               ["source_id", "source_relpath", "status"],
               [[s, p, st] for s, p, st in srcs])
    _write_tsv(os.path.join(mapdir, "layout.tsv"),
               ["source_id", "dest_relpath"],
               [[s, p] for s, p, _ in srcs])
    # SUMMARY 纯文本条目（2026-10-28 去链接化口径）：列全落点父节目录名
    lines = ["# Summary", "",
             "- 第01卷-合成甲",
             "    - 第1章-甲一",
             "        - 1.1-甲一节",
             "                            - 1.1.1-甲一一.md",
             "    - 第2章-甲二",
             "        - 2.1-甲二节",
             "                            - 2.1.1-甲二一.md",
             "- 第02卷-合成乙",
             "    - 第1章-乙一",
             "        - 1.1-乙一节",
             "                            - 1.1.1-乙一一.md",
             "        - 1.2-乙一二节"]
    _mk(os.path.join(root, "SUMMARY.md"), "\n".join(lines) + "\n")
    # outline.txt（L19 第一向，ADR-0020）：与树 3 个小节 .md 三向对齐
    _mk(os.path.join(root, "目录", "data", "outline.txt"),
        "# 第一卷  合成甲\n"
        "> 本卷所书皆为形式主义化的重构。\n"
        "## 第 1 章 甲一\n"
        "- 1.1 甲一节\n"
        "  - 1.1.1 甲一一\n"
        "## 第 2 章 甲二\n"
        "- 2.1 甲二节\n"
        "  - 2.1.1 甲二一\n"
        "# 第二卷  合成乙\n"
        "## 第 1 章 乙一\n"
        "- 1.1 乙一节\n"
        "  - 1.1.1 乙一一\n")
    # 主题索引
    kw = {"meta": {"schema": "theme-index/4", "volumes": 2, "chapters": 3, "sections": 4},
          "chapters": {}, "sections": {"V01-C001-1.1": {}, "V01-C002-2.1": {},
                                       "V02-C001-1.1": {}, "V02-C001-1.2": {}}}
    _mk(os.path.join(root, "chapter_keywords.json"),
        json.dumps(kw, ensure_ascii=False, indent=2) + "\n")
    return root


def selftest():
    """合成夹具全 PASS ＋ 逐条负向注入必 FAIL ＋ 缺映射必 SKIP。"""
    base = tempfile.mkdtemp(prefix="landing_gate_")
    ok = []
    bad = []

    def check(name, cond, detail=""):
        (ok if cond else bad).append("%s %s" % (name, detail))

    try:
        root = build_fixture(base)
        r = run_gate(root, os.path.join(root, "映射"))
        fails = [x for x in r if x[1] == "FAIL"]
        check("正例全 PASS", not fails, "%d 项 FAIL" % len(fails))
        check("L1–L19 齐 19 条", len([x for x in r if x[0].startswith("L")]) == 19)

        # 负向：L17 节内 .md 与 .gitkeep 并存
        gk = os.path.join(root, "第01卷-合成甲", "第1章-甲一", "1.1-甲一节", ".gitkeep")
        _mk(gk)
        r17 = {x[0]: x for x in run_gate(root, os.path.join(root, "映射"))}
        check("负向 L17 并存", r17["L17"][1] == "FAIL")
        os.remove(gk)

        # 负向：L18 单段文件名 >255 字节（88 个汉字＝264 字节；NTFS 按字符计，可建）
        p18 = os.path.join(root, "第01卷-合成甲", "第2章-甲二", "2.1-甲二节",
                           "9.9.9-" + "长" * 88 + ".md")
        _mk(p18, "# 9.9.9 长名\n")
        r18 = {x[0]: x for x in run_gate(root, os.path.join(root, "映射"))}
        check("负向 L18 超 255 字节", r18["L18"][1] == "FAIL")
        os.remove(p18)

        # 负向：L19 outline 幽灵小节行（树无 .md——设计级，禁）
        _mk(os.path.join(root, "目录", "data", "outline.txt"),
            io.open(os.path.join(root, "目录", "data", "outline.txt"), encoding="utf-8").read()
            + "  - 1.1.2 幽灵小节\n")
        r19 = {x[0]: x for x in run_gate(root, os.path.join(root, "映射"))}
        check("负向 L19 幽灵行", r19["L19"][1] == "FAIL", r19["L19"][2])
        _mk(os.path.join(root, "目录", "data", "outline.txt"),
            io.open(os.path.join(root, "目录", "data", "outline.txt"), encoding="utf-8").read()
            .replace("  - 1.1.2 幽灵小节\n", ""))

        # 负向：L19 树缺 .md（outline 有行而 .md 被删）
        _miss = os.path.join(root, "第02卷-合成乙", "第1章-乙一", "1.1-乙一节", "1.1.1-乙一一.md")
        _bak = _miss + ".tmp"
        os.rename(_miss, _bak)
        r19b = {x[0]: x for x in run_gate(root, os.path.join(root, "映射"))}
        check("负向 L19 缺 .md", r19b["L19"][1] == "FAIL", r19b["L19"][2])
        os.rename(_bak, _miss)

        # 负向：L4 H1 前缀不符
        p4 = os.path.join(root, "第01卷-合成甲", "第2章-甲二", "2.1-甲二节", "2.1.1-甲二一.md")
        _mk(p4, "# 9.9.9 错号\n")
        r4 = {x[0]: x for x in run_gate(root, os.path.join(root, "映射"))}
        check("负向 L4 H1 不符", r4["L4"][1] == "FAIL")
        _mk(p4, "# 2.1.1 甲二一\n")

        # 负向：L9 CRLF
        p9 = os.path.join(root, "第02卷-合成乙", "第1章-乙一", "1.1-乙一节", "1.1.1-乙一一.md")
        with open(p9, "wb") as fh:
            fh.write(b"# 1.1.1 \xe4\xb9\x99\xe4\xb8\x80\xe4\xb8\x80\r\n")
        r9 = {x[0]: x for x in run_gate(root, os.path.join(root, "映射"))}
        check("负向 L9 CRLF", r9["L9"][1] == "FAIL")
        _mk(p9, "# 1.1.1 乙一一\n")

        # 负向：L1 树多一节（空节目录未在 targets）
        os.makedirs(os.path.join(root, "第02卷-合成乙", "第1章-乙一", "1.3-多余节"),
                    exist_ok=True)
        _mk(os.path.join(root, "第02卷-合成乙", "第1章-乙一", "1.3-多余节", ".gitkeep"))
        r1 = {x[0]: x for x in run_gate(root, os.path.join(root, "映射"))}
        check("负向 L1 计数不符", r1["L1"][1] == "FAIL")
        shutil.rmtree(os.path.join(root, "第02卷-合成乙", "第1章-乙一", "1.3-多余节"))

        # 负向：L3 落点多出 .md
        extra = os.path.join(root, "第01卷-合成甲", "第1章-甲一", "1.1-甲一节", "1.1.2-多出.md")
        _mk(extra, "# 1.1.2 多出\n")
        r3 = {x[0]: x for x in run_gate(root, os.path.join(root, "映射"))}
        check("负向 L3 多余落点", r3["L3"][1] == "FAIL")
        os.remove(extra)

        # 负向：L2 映射落点缺失
        lay_path = os.path.join(root, "映射", "layout.tsv")
        rows = read_tsv(lay_path)
        _write_tsv(lay_path, ["source_id", "dest_relpath"],
                   [[r["source_id"], r["dest_relpath"]] for r in rows]
                   + [["S-900009", "第01卷-合成甲/第1章-甲一/1.1-甲一节/1.1.9-缺.md"]])
        mrows = read_tsv(os.path.join(root, "映射", "mapping.tsv"))
        _write_tsv(os.path.join(root, "映射", "mapping.tsv"),
                   ["source_id", "source_relpath", "status"],
                   [[r["source_id"], r["source_relpath"], r["status"]] for r in mrows]
                   + [["S-900009", "旧/缺.md", "CONFIRMED"]])
        r2 = {x[0]: x for x in run_gate(root, os.path.join(root, "映射"))}
        check("负向 L2 落点缺失", r2["L2"][1] == "FAIL")
        _write_tsv(lay_path, ["source_id", "dest_relpath"],
                   [[r["source_id"], r["dest_relpath"]] for r in rows])
        _write_tsv(os.path.join(root, "映射", "mapping.tsv"),
                   ["source_id", "source_relpath", "status"],
                   [[r["source_id"], r["source_relpath"], r["status"]] for r in mrows])

        # 负向：L5 旧三段号未挂账
        p5 = os.path.join(root, "第01卷-合成甲", "第1章-甲一", "1.1-甲一节", "1.1.1-甲一一.md")
        _mk(p5, "# 1.1.1 甲一一\n\n参见 005.2.1 旧节。\n")
        r5 = {x[0]: x for x in run_gate(root, os.path.join(root, "映射"))}
        check("负向 L5 旧三段号", r5["L5"][1] == "FAIL")
        _mk(p5, "# 1.1.1 甲一一\n\n日期 2024.1.20 不应命中。\n")
        r5b = {x[0]: x for x in run_gate(root, os.path.join(root, "映射"))}
        check("负向 L5 日期不误判", r5b["L5"][1] == "PASS")

        # 负向：L16 旧二段号未挂账
        _mk(p5, "# 1.1.1 甲一一\n\n参见 003.8 旧节。\n")
        r16 = {x[0]: x for x in run_gate(root, os.path.join(root, "映射"))}
        check("负向 L16 旧二段号", r16["L16"][1] == "FAIL")
        _mk(p5, "# 1.1.1 甲一一\n")

        # 负向：L6 重复内容
        p6 = os.path.join(root, "第01卷-合成甲", "第2章-甲二", "2.1-甲二节", "2.1.1-甲二一.md")
        _mk(p6, "# 1.1.1 甲一一\n")
        r6 = {x[0]: x for x in run_gate(root, os.path.join(root, "映射"))}
        check("负向 L6 重复内容", r6["L6"][1] == "FAIL")
        _mk(p6, "# 2.1.1 甲二一\n")

        # 负向：L12 TARGET_LOST 未挂账
        mrows = read_tsv(os.path.join(root, "映射", "mapping.tsv"))
        _write_tsv(os.path.join(root, "映射", "mapping.tsv"),
                   ["source_id", "source_relpath", "status"],
                   [[r["source_id"], r["source_relpath"], r["status"]] for r in mrows]
                   + [["S-900010", "旧/丢.md", "TARGET_LOST"]])
        r12 = {x[0]: x for x in run_gate(root, os.path.join(root, "映射"))}
        check("负向 L12 缺挂账", r12["L12"][1] == "FAIL")
        _write_tsv(os.path.join(root, "映射", "mapping.tsv"),
                   ["source_id", "source_relpath", "status"],
                   [[r["source_id"], r["source_relpath"], r["status"]] for r in mrows])

        # 负向：L15 后继无效
        _write_tsv(os.path.join(root, "映射", "remap.tsv"),
                   ["source_id", "successor_ids"], [["S-900001", "S-不存在"]])
        r15 = {x[0]: x for x in run_gate(root, os.path.join(root, "映射"))}
        check("负向 L15 后继无效", r15["L15"][1] == "FAIL")
        os.remove(os.path.join(root, "映射", "remap.tsv"))

        # 负向：L8 schema 不符
        kw = {"meta": {"schema": "theme-index/3", "volumes": 2, "chapters": 3, "sections": 4},
              "chapters": {}, "sections": {}}
        _mk(os.path.join(root, "chapter_keywords.json"),
            json.dumps(kw, ensure_ascii=False, indent=2) + "\n")
        r8 = {x[0]: x for x in run_gate(root, os.path.join(root, "映射"))}
        check("负向 L8 schema 不符", r8["L8"][1] == "FAIL")

        # —— 补齐夹具（2026-10-23 第二轮）：逐条负向与豁免正例 ——
        mp = os.path.join(root, "映射")

        def g():
            return {x[0]: x for x in run_gate(root, mp)}

        good_kw = {"meta": {"schema": "theme-index/4", "volumes": 2, "chapters": 3, "sections": 4},
                   "chapters": {}, "sections": {"V01-C001-1.1": {}, "V01-C002-2.1": {},
                                                "V02-C001-1.1": {}, "V02-C001-1.2": {}}}

        # L4 数字边界：1.1.10 不得冒充 1.1.1
        p4b = os.path.join(root, "第01卷-合成甲", "第1章-甲一", "1.1-甲一节", "1.1.1-甲一一.md")
        _mk(p4b, "# 1.1.10 冒充\n")
        check("负向 L4 数字边界", g()["L4"][1] == "FAIL")
        _mk(p4b, "# 1.1.1 甲一一\n")

        # L4 空落点
        _mk(p4b, "")
        check("负向 L4 空落点", g()["L4"][1] == "FAIL")
        _mk(p4b, "# 1.1.1 甲一一\n")

        # L7 缺行不崩（mapping CONFIRMED 但 layout 无该 source_id）
        lay_path = os.path.join(mp, "layout.tsv")
        rows = read_tsv(lay_path)
        _write_tsv(lay_path, ["source_id", "dest_relpath"],
                   [[r["source_id"], r["dest_relpath"]] for r in rows if r["source_id"] != "S-900002"])
        try:
            r7 = g()
            check("负向 L7 缺行 FAIL 且不崩", r7["L7"][1] == "FAIL")
        except SystemExit:
            check("负向 L7 缺行 FAIL 且不崩", False, "仍抛 SystemExit")
        _write_tsv(lay_path, ["source_id", "dest_relpath"],
                   [[r["source_id"], r["dest_relpath"]] for r in rows])

        # L7 SUMMARY 为空
        sp = os.path.join(root, "SUMMARY.md")
        good_summary = open(sp, encoding="utf-8").read()
        _mk(sp, "")
        check("负向 L7 SUMMARY 空", g()["L7"][1] == "FAIL")
        _mk(sp, good_summary)

        # L7 缺节条目（CONFIRMED 落点父节目录名不在 SUMMARY）
        cut = [ln for ln in good_summary.split("\n") if ln.strip() != "- 2.1-甲二节"]
        _mk(sp, "\n".join(cut))
        check("负向 L7 缺节条目", g()["L7"][1] == "FAIL")
        _mk(sp, good_summary)

        # L2 dest 空串（不得因 join(root,"") 假 PASS）
        _write_tsv(lay_path, ["source_id", "dest_relpath"],
                   [[r["source_id"], ""] if r["source_id"] == "S-900001" else
                    [r["source_id"], r["dest_relpath"]] for r in rows])
        r2e = g()
        check("负向 L2 空 dest", r2e["L2"][1] == "FAIL")
        check("负向 L11 空 dest", r2e["L11"][1] == "FAIL")
        _write_tsv(lay_path, ["source_id", "dest_relpath"],
                   [[r["source_id"], r["dest_relpath"]] for r in rows])

        # L11 布局漂移
        _write_tsv(lay_path, ["source_id", "dest_relpath"],
                   [[r["source_id"], r["dest_relpath"]] for r in rows]
                   + [["S-900030", "第01卷-合成甲/第1章-甲一/1.1-甲一节/1.1.8-无.md"]])
        check("负向 L11 漂移", g()["L11"][1] == "FAIL")
        _write_tsv(lay_path, ["source_id", "dest_relpath"],
                   [[r["source_id"], r["dest_relpath"]] for r in rows])

        # L10 卷层散件
        stray = os.path.join(root, "第01卷-合成甲", "stray.txt")
        _mk(stray, "x\n")
        check("负向 L10 卷层散件", g()["L10"][1] == "FAIL")
        os.remove(stray)

        # L13 非法文件名与超长路径
        _write_tsv(lay_path, ["source_id", "dest_relpath"],
                   [[r["source_id"], r["dest_relpath"]] for r in rows]
                   + [["S-900031", "第01卷-合成甲/第1章-甲一/1.1-甲一节/1.1.9-a*b.md"]])
        check("负向 L13 非法字符", g()["L13"][1] == "FAIL")
        longdest = "第01卷-合成甲/第1章-甲一/1.1-甲一节/" + ("超" * 200) + ".md"
        _write_tsv(lay_path, ["source_id", "dest_relpath"],
                   [[r["source_id"], r["dest_relpath"]] for r in rows]
                   + [["S-900032", longdest]])
        check("负向 L13 超长路径", g()["L13"][1] == "FAIL")
        _write_tsv(lay_path, ["source_id", "dest_relpath"],
                   [[r["source_id"], r["dest_relpath"]] for r in rows])
        _write_tsv(os.path.join(mp, "path-overlong.tsv"), ["source_id"], [["S-900032"]])
        _write_tsv(lay_path, ["source_id", "dest_relpath"],
                   [[r["source_id"], r["dest_relpath"]] for r in rows]
                   + [["S-900032", longdest]])
        check("正向 L13 已挂账豁免", g()["L13"][1] == "PASS")
        _write_tsv(lay_path, ["source_id", "dest_relpath"],
                   [[r["source_id"], r["dest_relpath"]] for r in rows])
        os.remove(os.path.join(mp, "path-overlong.tsv"))

        # L14 复合键重复与坏行
        tp = os.path.join(mp, "targets.tsv")
        trows = read_tsv(tp)
        tcols = list(trows[0].keys())
        dup_row = dict(trows[5])
        dup_row["node_id"] = "S-000099"
        _write_tsv(tp, tcols, [[r[c] for c in tcols] for r in trows]
                   + [[dup_row[c] for c in tcols]])
        check("负向 L14 复合键重复", g()["L14"][1] == "FAIL")
        bad_row = dict(trows[5])
        bad_row["node_id"] = "S-000098"
        bad_row["vol_no"] = ""
        _write_tsv(tp, tcols, [[r[c] for c in tcols] for r in trows]
                   + [[bad_row[c] for c in tcols]])
        check("负向 L14 坏行", g()["L14"][1] == "FAIL")
        _write_tsv(tp, tcols, [[r[c] for c in tcols] for r in trows])

        # L15 REMAP 未挂账与后继为空
        mpath = os.path.join(mp, "mapping.tsv")
        mrows2 = read_tsv(mpath)
        mcols = list(mrows2[0].keys())
        remap_row = dict(mrows2[0])
        remap_row["source_id"] = "S-900040"
        remap_row["status"] = "REMAP"
        _write_tsv(mpath, mcols, [[r[c] for c in mcols] for r in mrows2]
                   + [[remap_row[c] for c in mcols]])
        check("负向 L15 REMAP 未挂账", g()["L15"][1] == "FAIL")
        _write_tsv(os.path.join(mp, "remap.tsv"), ["source_id", "successor_ids"],
                   [["S-900040", ""]])
        check("负向 L15 后继为空", g()["L15"][1] == "FAIL")
        os.remove(os.path.join(mp, "remap.tsv"))
        _write_tsv(mpath, mcols, [[r[c] for c in mcols] for r in mrows2])

        # L8 键集不符
        bad_kw = dict(good_kw)
        bad_kw["sections"] = {"V01-C001-1.1": {}, "V01-C002-2.1": {},
                              "V02-C001-1.1": {}, "V02-C001-9.9": {}}
        _mk(os.path.join(root, "chapter_keywords.json"),
            json.dumps(bad_kw, ensure_ascii=False, indent=2) + "\n")
        check("负向 L8 键集不符", g()["L8"][1] == "FAIL")
        _mk(os.path.join(root, "chapter_keywords.json"),
            json.dumps(good_kw, ensure_ascii=False, indent=2) + "\n")

        # L9 BOM
        p9b = os.path.join(root, "第01卷-合成甲", "第1章-甲一", "1.1-甲一节", "1.1.1-甲一一.md")
        with open(p9b, "wb") as fh:
            fh.write(b"\xef\xbb\xbf# 1.1.1 \xe7\x94\xb2\xe4\xb8\x80\xe4\xb8\x80\n")
        check("负向 L9 BOM", g()["L9"][1] == "FAIL")
        _mk(p9b, "# 1.1.1 甲一一\n")

        # L17 空节缺 .gitkeep
        gk2 = os.path.join(root, "第02卷-合成乙", "第1章-乙一", "1.2-乙一二节", ".gitkeep")
        os.remove(gk2)
        check("负向 L17 空节缺 gitkeep", g()["L17"][1] == "FAIL")
        _mk(gk2, "")

        # L16 仅日期不误判
        _mk(p9b, "# 1.1.1 甲一一\n\n日期 2024.1.20。\n")
        check("正向 L16 日期不误判", g()["L16"][1] == "PASS")
        _mk(p9b, "# 1.1.1 甲一一\n")

        # L5／L16 代码块内旧号不误判
        _mk(p9b, "# 1.1.1 甲一一\n\n```\n旧号 005.2.1 在代码里\n```\n")
        check("正向 L5 代码块豁免", g()["L5"][1] == "PASS")
        _mk(p9b, "# 1.1.1 甲一一\n")

        # 表头契约：mapping 缺 status 列应致命退出
        _write_tsv(mpath, ["source_id", "source_relpath"],
                   [[r["source_id"], r["source_relpath"]] for r in mrows2])
        try:
            run_gate(root, mp)
            check("表头契约 缺 status 致命", False, "未退出")
        except SystemExit as exc:
            check("表头契约 缺 status 致命", int(str(exc.code)) == 2 if str(exc.code).isdigit() else False,
                  "exit=%s" % exc.code)
        _write_tsv(mpath, mcols, [[r[c] for c in mcols] for r in mrows2])

        # 负向：缺 mapping.tsv → 依赖判据 SKIP、无 FAIL
        # 先恢复 L8 负向注入前的主索引（避免与本用例无关的 FAIL 混入）
        good_kw = {"meta": {"schema": "theme-index/4", "volumes": 2, "chapters": 3, "sections": 4},
                   "chapters": {}, "sections": {"V01-C001-1.1": {}, "V01-C002-2.1": {},
                                                "V02-C001-1.1": {}, "V02-C001-1.2": {}}}
        _mk(os.path.join(root, "chapter_keywords.json"),
            json.dumps(good_kw, ensure_ascii=False, indent=2) + "\n")
        mp = os.path.join(root, "映射")
        src_rows = read_tsv(os.path.join(mp, "targets.tsv"))
        cols = list(src_rows[0].keys())
        shutil.rmtree(mp)
        os.makedirs(mp, exist_ok=True)
        _write_tsv(os.path.join(mp, "targets.tsv"), cols,
                   [[r[c] for c in cols] for r in src_rows])
        r2s = run_gate(root, mp)
        skips = {x[0] for x in r2s if x[1] == "SKIP"}
        dep_fails = [x for x in r2s if x[1] == "FAIL" and x[0] in NEEDS_MAPPING]
        check("缺 mapping → 依赖判据 SKIP", NEEDS_MAPPING <= skips,
              "缺 %s" % sorted(NEEDS_MAPPING - skips))
        check("缺 mapping → 依赖判据无 FAIL", not dep_fails,
              "FAIL：%s" % [x[0] for x in dep_fails])
        check("缺 mapping → 非依赖判据仍 PASS",
              not [x for x in r2s if x[1] == "FAIL"])
    finally:
        shutil.rmtree(base, ignore_errors=True)

    print("=" * 72)
    print("audit_outline_landing --selftest")
    print("=" * 72)
    for s in ok:
        print("  [PASS]", s)
    for s in bad:
        print("  [FAIL]", s)
    print("-" * 72)
    print("自检 %d 项，失败 %d 项" % (len(ok) + len(bad), len(bad)))
    return 0 if not bad else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description="大纲落地一致性门禁 L1–L19")
    ap.add_argument("--root", default=DEFAULT_ROOT, help="大纲树根（默认 05-卷册大纲）")
    ap.add_argument("--map", default=None, help="映射层目录（默认 <root>/映射）")
    ap.add_argument("--check", action="store_true", help="只读检查（默认行为，兼容门禁调用惯例）")
    ap.add_argument("--json", action="store_true", help="附 JSON 汇总")
    ap.add_argument("--selftest", action="store_true", help="合成夹具自检")
    args = ap.parse_args(argv)

    if args.selftest:
        return selftest()

    res = run_gate(args.root, args.map)
    fails = [x for x in res if x[1] == "FAIL"]
    skips = [x for x in res if x[1] == "SKIP"]
    print("=" * 72)
    print("大纲落地一致性门禁 L1–L19")
    print("=" * 72)
    for no, verdict, detail in res:
        print("  %-4s %-4s %s" % (no, verdict, detail))
    print("-" * 72)
    print("合计 %d 条：PASS %d／FAIL %d／SKIP %d"
          % (len(res), len(res) - len(fails) - len(skips), len(fails), len(skips)))
    if args.json:
        print(json.dumps({"results": res, "fail": len(fails), "skip": len(skips)},
                         ensure_ascii=False, indent=2))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
