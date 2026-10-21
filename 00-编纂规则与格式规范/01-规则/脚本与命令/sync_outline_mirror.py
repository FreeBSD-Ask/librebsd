#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync_outline_mirror.py —— 大纲目录镜像全量再生与双射校验（固定脚本，批 8 立）。

对象
----
大纲树（默认 `05-新大纲/`，`--root` 可覆盖）四层：卷 `第NNN卷-slug`／章 `第NNN章-slug`
（章号 001..449，不得 000／900–910）／节 `NNN.M-slug`／小节 `NNN.M.P-slug.md`。
产物两件，写 `11-元数据接口/03-大纲目录镜像/`（`--out` 可覆盖）：

  * `SUMMARY.md`：`# Summary` 后逐条列表；缩进四层（卷 0／章 2／节 4／小节 6）；
    目录用带尾斜杠的相对链接，小节用 `.md` 相对链接；标题与磁盘目录／文件名**逐字一致**，
    空目录与空文件照列，零树外条目。
  * `chapter_keywords.json`：键＝三位章号字符串；值含 `volume`／`title`／`subs`
    （该章节目录名数组，须非空）／`keywords`（数组）。旧库既有 `keywords` 按**旧章身份**
    保留——旧键（自然数 1..390）经 `script/_b7_mapping.json` 的 `chapter_map` 由 old→new
    映射到新键，旧键不残留；无旧身份的新增结构章按章题与节题中的拉丁词元派生（≤8，小写
    去重）。若现有库已是新键形态（三位），只补不删。

语义
----
`--check`（缺省）在内存生成两份内容，与磁盘**逐字节／逐键**比对，并跑独立校验器：
缺条、树外条、死链、题面改字、缩进错位、`subs` 空键、章键缺／多、编号越界、树结构异常
均判漂移（exit 1）。不得以“条目计数相等”替代逐条比对——题面改字而计数不变须判 FAIL。

写盘
----
写盘前 import 同目录 `wo007_idempotency.py`：优先以 `write_guard()` 写临时件，写完**回读
逐字节**校验；其 `normalize_terms()`（基础系统→基本系统）与库名归一化若会改写目录名，
则先由**中性预检**拒绝写入（报 `W_NORM`，说明大纲树里存在应在上游改名的旧词），回读不符
时退 `write_text_lf()`。最终以 `os.replace` 原子替换（UTF-8 无 BOM ＋ LF）。

用法
----
    C:/Python314/python.exe sync_outline_mirror.py --check     # 缺省：漂移报告，漂移 exit 1
    C:/Python314/python.exe sync_outline_mirror.py --write     # 生成并原子写盘两件
    C:/Python314/python.exe sync_outline_mirror.py --list      # 计数统计
    C:/Python314/python.exe sync_outline_mirror.py --selftest  # 合成夹具自检（保留不清理）

依赖：仅标准库。路径一律由本文件位置推导，不写死绝对路径。
"""
import argparse
import collections
import json
import os
import re
import shutil
import sys
import tempfile

sys.stdout.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
DEFAULT_ROOT = os.path.join(REPO, "05-新大纲")
DEFAULT_OUT = os.path.join(REPO, "11-元数据接口", "03-大纲目录镜像")
DEFAULT_MAPPING = os.path.join(REPO, "script", "_b7_mapping.json")
SELFTEST_REL = os.path.join("script", "_mirror_selftest")

VOL_RE = re.compile(r"^第(\d{1,3})卷(?:-(?P<slug>.+))?$")
CH_RE = re.compile(r"^第(\d{1,3})章(?:-(?P<slug>.+))?$")
SEC_RE = re.compile(r"^(\d{1,3})\.(\d{1,3})-(?P<slug>.+)$")
SUB_RE = re.compile(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,2})-(?P<slug>.+)\.md$")
KEY3_RE = re.compile(r"^\d{3}$")
KEYN_RE = re.compile(r"^\d{1,3}$")
LINE_RE = re.compile(r"^(?P<indent> *)- \[(?P<title>.+?)\]\((?P<target>.+)\)$")

# 章节词元派生：拉丁词元、合法词形与停用词（沿 sync_chapter_keywords.py 惯例）
LATIN = re.compile(r"[A-Za-z][A-Za-z0-9.+-]{1,}")
TERM = re.compile(r"^[a-z0-9][a-z0-9._+-]{1,39}$")
STOP = set("""bsd unix os history computer software system technology project community
development open source free internet the and for with from into over under about
its his her their this that these those new old early late modern""".split())
MAX_KW = 8
CH_NUM_MIN, CH_NUM_MAX = 1, 449

CODE_TEXT = {
    "T_VOL_NAME_BAD": "卷目录名不合命名法",
    "T_VOL_NUM_BAD": "卷号小于 1",
    "T_CHAPTER_NAME_BAD": "章目录名不合命名法",
    "T_CHAPTER_NUM_RANGE": "章号越界（须 001..449，不得 000／900–910）",
    "T_CHAPTER_NUM_DUP": "章号重复",
    "T_SECTION_NAME_BAD": "节目录名不合命名法",
    "T_SECTION_PREFIX_MISMATCH": "节号前缀与章号不符",
    "T_SECTION_NUM_DUP": "节号重复",
    "T_SUBSECTION_NAME_BAD": "小节名不合命名法",
    "T_SUBSECTION_PREFIX_MISMATCH": "小节号前缀与节号不符",
    "T_SUBSECTION_NUM_DUP": "小节号重复",
    "T_STRAY_FILE_AT_ROOT": "大纲树根级只允许卷目录",
    "T_STRAY_FILE": "该层只允许子目录／小节 .md，发现散件",
    "T_STRAY_DIR": "节层只允许小节 .md 文件，发现子目录",
    "S_HEADER": "SUMMARY 首行须为 `# Summary`",
    "S_FORMAT": "条目行无法解析",
    "S_MISSING": "树中实体未被镜像列出",
    "S_EXTRA": "镜像含树外条目",
    "S_DUP": "同一目标在镜像中重复出现",
    "S_TITLE": "题面与磁盘名不逐字一致",
    "S_INDENT": "缩进与层级不符",
    "S_SLASH": "目录链接缺尾斜杠",
    "S_DEAD": "死链：链接目标在磁盘不存在",
    "S_KIND": "链接目标类型与层级不符",
    "S_PATH": "链接目标路径非法（绝对路径或含 ..）",
    "S_ORDER": "条目序与树序不一致",
    "K_KEY_FMT": "章键非三位数字字符串",
    "K_KEY_RANGE": "章键越界（须 001..449）",
    "K_MISSING": "章键缺失",
    "K_EXTRA": "章键为树外章",
    "K_VOL": "volume 与树不符",
    "K_TITLE": "title 与树不符",
    "K_SUBS": "subs 与树中节目录不符",
    "K_SUBS_EMPTY": "subs 为空（须非空）",
    "K_KW_TYPE": "keywords 非字符串数组",
    "K_SHAPE": "条目缺字段或字段类型不符",
    "D_MISSING_TEXT": "磁盘缺 SUMMARY.md",
    "D_DRIFT_TEXT": "SUMMARY.md 与再生内容不一致",
    "D_MISSING_JSON": "磁盘缺 chapter_keywords.json",
    "K_DRIFT": "chapter_keywords.json 逐键漂移",
    "W_NORM": "写盘归一化会改动产物（拒绝写入）",
}


class Fatal(Exception):
    """致命前提不成立（exit 2）：根缺失、库损坏、映射缺失等。"""


class ScanError(Fatal):
    pass


# ---------------------------------------------------------------- 扫描大纲树

def _rel_join(*parts):
    return "/".join(parts)


def _under(root, rel):
    return os.path.join(root, *rel.split("/"))


def scan_tree(root):
    """扫描大纲树四层，返回 {"volumes": [...], "anomalies": [(kind, rel, detail)]}。

    目录名一律**原样保留**（镜像须逐字一致）；命名法与编号约束只作判据，不改写磁盘名。
    """
    if not os.path.isdir(root):
        raise ScanError("大纲树根不存在或不是目录：%s" % root)
    tree = {"volumes": [], "anomalies": [], "_root": root}
    ch_seen = {}
    for vname in sorted(os.listdir(root)):
        vfull = os.path.join(root, vname)
        if not os.path.isdir(vfull):
            tree["anomalies"].append(("stray_file_at_root", vname,
                                      "大纲树根级只允许卷目录"))
            continue
        vm = VOL_RE.match(vname)
        if not vm:
            tree["anomalies"].append(("vol_name_bad", vname, "须为 第NNN卷-slug"))
            continue
        vnum = int(vm.group(1))
        if vnum < 1:
            tree["anomalies"].append(("vol_num_bad", vname, "卷号须 ≥ 1"))
        vol = {"name": vname, "num": vnum, "slug": vm.group("slug") or "", "chapters": []}
        _scan_chapters(root, vol, tree, ch_seen)
        tree["volumes"].append(vol)
    tree["volumes"].sort(key=lambda v: (v["num"], v["name"]))
    return tree


def _scan_chapters(root, vol, tree, ch_seen):
    vpath = _under(root, vol["name"])
    for cname in sorted(os.listdir(vpath)):
        cfull = os.path.join(vpath, cname)
        rel = _rel_join(vol["name"], cname)
        if not os.path.isdir(cfull):
            tree["anomalies"].append(("stray_file", rel, "卷层只允许章目录"))
            continue
        cm = CH_RE.match(cname)
        if not cm:
            tree["anomalies"].append(("chapter_name_bad", rel, "须为 第NNN章-slug"))
            continue
        cnum = int(cm.group(1))
        if cnum < CH_NUM_MIN or cnum > CH_NUM_MAX:
            tree["anomalies"].append(("chapter_num_range", rel,
                                      "章号 %d 越界（须 001..449）" % cnum))
        if cnum in ch_seen:
            tree["anomalies"].append(("chapter_num_dup", rel,
                                      "章号与 %s 重复" % ch_seen[cnum]))
        else:
            ch_seen[cnum] = rel
        chap = {"name": cname, "num": cnum, "slug": cm.group("slug") or "",
                "volume": vol["name"], "sections": []}
        _scan_sections(root, vol, chap, tree)
        vol["chapters"].append(chap)
    vol["chapters"].sort(key=lambda c: (c["num"], c["name"]))


def _scan_sections(root, vol, chap, tree):
    base_rel = _rel_join(vol["name"], chap["name"])
    base = _under(root, base_rel)
    seen = {}
    for sname in sorted(os.listdir(base)):
        sfull = os.path.join(base, sname)
        rel = _rel_join(base_rel, sname)
        if not os.path.isdir(sfull):
            tree["anomalies"].append(("stray_file", rel,
                                      "章层只允许节目录（禁 index.md／概述.md 等散件）"))
            continue
        sm = SEC_RE.match(sname)
        if not sm:
            tree["anomalies"].append(("section_name_bad", rel, "须为 NNN.M-slug"))
            continue
        if int(sm.group(1)) != chap["num"]:
            tree["anomalies"].append(("section_prefix_mismatch", rel,
                                      "节号前缀 %s 与章号 %d 不符" % (sm.group(1), chap["num"])))
        snum = int(sm.group(2))
        if snum in seen:
            tree["anomalies"].append(("section_num_dup", rel,
                                      "节号 %d 与 %s 重复" % (snum, seen[snum])))
        else:
            seen[snum] = rel
        sec = {"name": sname, "num": snum, "slug": sm.group("slug"), "subs": []}
        _scan_subs(root, vol, chap, sec, tree)
        chap["sections"].append(sec)
    chap["sections"].sort(key=lambda s: (s["num"], s["name"]))


def _scan_subs(root, vol, chap, sec, tree):
    base_rel = _rel_join(vol["name"], chap["name"], sec["name"])
    base = _under(root, base_rel)
    seen = {}
    for fname in sorted(os.listdir(base)):
        ffull = os.path.join(base, fname)
        rel = _rel_join(base_rel, fname)
        if not os.path.isfile(ffull):
            tree["anomalies"].append(("stray_dir", rel, "节层只允许小节 .md 文件"))
            continue
        bm = SUB_RE.match(fname)
        if not bm:
            tree["anomalies"].append(("subsection_name_bad", rel,
                                      "须为 NNN.M.P-slug.md"))
            continue
        if int(bm.group(1)) != chap["num"] or int(bm.group(2)) != sec["num"]:
            tree["anomalies"].append(("subsection_prefix_mismatch", rel,
                                      "小节号前缀 %s.%s 与 %d.%d 不符"
                                      % (bm.group(1), bm.group(2), chap["num"], sec["num"])))
        pnum = int(bm.group(3))
        if pnum in seen:
            tree["anomalies"].append(("subsection_num_dup", rel,
                                      "小节号 %d 与 %s 重复" % (pnum, seen[pnum])))
        else:
            seen[pnum] = rel
        sec["subs"].append({"name": fname, "num": pnum})
    sec["subs"].sort(key=lambda b: (b["num"], b["name"]))


def tree_counts(tree):
    """返回 (卷数, 章数, 节数, 小节数, 实体合计)。"""
    nv = len(tree["volumes"])
    nc = sum(len(v["chapters"]) for v in tree["volumes"])
    ns = sum(len(c["sections"]) for v in tree["volumes"] for c in v["chapters"])
    nb = sum(len(s["subs"]) for v in tree["volumes"] for c in v["chapters"]
             for s in c["sections"])
    return nv, nc, ns, nb, nv + nc + ns + nb


def iter_entities(tree):
    """按树序产出 (缩进层级, 题面, 相对链接目标)——镜像的正序真值。"""
    for vol in tree["volumes"]:
        yield 0, vol["name"], vol["name"] + "/"
        for chap in vol["chapters"]:
            cpath = _rel_join(vol["name"], chap["name"])
            yield 2, chap["name"], cpath + "/"
            for sec in chap["sections"]:
                spath = _rel_join(cpath, sec["name"])
                yield 4, sec["name"], spath + "/"
                for sub in sec["subs"]:
                    yield 6, sub["name"], _rel_join(spath, sub["name"])


# ---------------------------------------------------------------- 生成两件产物

def render_summary(tree):
    """生成 SUMMARY.md 全文（LF 结尾）。"""
    lines = ["# Summary", ""]
    for level, title, target in iter_entities(tree):
        lines.append("%s- [%s](%s)" % ("  " * level, title, target))
    return "\n".join(lines) + "\n"


def _first_h1(path):
    """取首个 `# ` 标题（跳过 YAML frontmatter 与空行）；失败返回 None。"""
    try:
        in_fm = False
        with open(path, encoding="utf-8", errors="replace") as fh:
            for ln in fh:
                s = ln.rstrip("\r\n")
                if s.strip() == "---":
                    in_fm = not in_fm
                    continue
                if in_fm or not s.strip():
                    continue
                if s.startswith("# "):
                    return s[2:].strip()
                if s.startswith("#"):
                    continue
                return None
    except OSError:
        return None
    return None


def chapter_title(root, chap):
    """章题＝章目录 slug；无 slug 时回退首个可读小节 H1（再回退目录名）。"""
    if chap["slug"]:
        return chap["slug"]
    for sec in chap["sections"]:
        for sub in sec["subs"]:
            rel = _rel_join(chap["volume"], chap["name"], sec["name"], sub["name"])
            h1 = _first_h1(_under(root, rel))
            if h1:
                return h1
    return chap["name"]


def derive_keywords(chap, title):
    """新增章按章题与节题中的拉丁词元派生（≤8，小写去重，排序）。"""
    pool = [title] + [s["name"] for s in chap["sections"]]
    out, seen = [], set()
    for text in pool:
        for tok in LATIN.findall(text):
            t = tok.lower().strip(".-+")
            if len(t) < 2 or t in STOP or t in seen or not TERM.match(t):
                continue
            seen.add(t)
            out.append(t)
            if len(out) >= MAX_KW:
                return sorted(out)
    return sorted(out)


def load_legacy_keywords(out_dir):
    """读现有 chapter_keywords.json，返回 (doc, mode)；mode ∈ {absent, legacy, new}。"""
    path = os.path.join(out_dir, "chapter_keywords.json")
    if not os.path.isfile(path):
        return {}, "absent"
    try:
        with open(path, encoding="utf-8") as fh:
            doc = json.load(fh)
    except Exception as exc:
        raise Fatal("现有 chapter_keywords.json 无法解析（拒覆盖）：%s" % exc)
    if not isinstance(doc, dict):
        raise Fatal("现有 chapter_keywords.json 顶层不是对象（拒覆盖）")
    if not doc:
        return {}, "absent"
    three = [k for k in doc if KEY3_RE.match(k)]
    legacy = [k for k in doc if KEYN_RE.match(k) and not KEY3_RE.match(k)]
    if len(three) == len(doc):
        return doc, "new"
    if len(legacy) == len(doc):
        return doc, "legacy"
    raise Fatal("现有 chapter_keywords.json 键形态混杂（三位 %d 个／旧键 %d 个），拒判"
                % (len(three), len(legacy)))


def load_mapping(path):
    """读批 7 映射表，返回 old_num → new_num（仅 old_num ≥ 1 的实质章）。"""
    if not os.path.isfile(path):
        raise Fatal("章号映射表不存在：%s" % path)
    try:
        with open(path, encoding="utf-8") as fh:
            doc = json.load(fh)
    except Exception as exc:
        raise Fatal("章号映射表无法解析：%s" % exc)
    rows = doc.get("chapter_map")
    if not isinstance(rows, list):
        raise Fatal("章号映射表缺 chapter_map 数组：%s" % path)
    old2new = {}
    for row in rows:
        try:
            old = int(row.get("old_num"))
            new = int(row.get("new_num"))
        except (TypeError, ValueError):
            continue
        if old < 1:
            continue
        old2new.setdefault(old, new)
    return old2new


def build_keywords(tree, legacy, mode, old2new, root):
    """生成章关键词库文档与派生说明。"""
    notes = {"mode": mode, "kept": 0, "derived": 0,
             "unmapped": [], "retitled": [], "mapped_from_legacy": 0}
    prev = {}
    if mode == "new":
        prev = dict(legacy)
    elif mode == "legacy":
        for key, value in legacy.items():
            old = int(key)
            if old not in old2new:
                notes["unmapped"].append(key)
                continue
            nk = "%03d" % old2new[old]
            if nk in prev:
                continue
            prev[nk] = value
            notes["mapped_from_legacy"] += 1

    doc = {}
    for vol in tree["volumes"]:
        for chap in vol["chapters"]:
            key = "%03d" % chap["num"]
            title = chapter_title(root, chap)
            subs = [s["name"] for s in chap["sections"]]
            old = prev.get(key) or {}
            kws = [str(x) for x in (old.get("keywords") or [])
                   if isinstance(x, str) and x]
            if kws:
                notes["kept"] += 1
            else:
                kws = derive_keywords(chap, title)
                notes["derived"] += 1
            if old and (old.get("volume") != vol["name"] or old.get("title") != title):
                notes["retitled"].append(key)
            doc[key] = {"volume": vol["name"], "title": title,
                        "subs": subs, "keywords": kws}
    ordered = {k: doc[k] for k in sorted(doc, key=int)}
    return ordered, notes


def render_keywords(doc):
    return json.dumps(doc, ensure_ascii=False, indent=2) + "\n"


# ---------------------------------------------------------------- 校验器（独立函数）

def parse_summary(text):
    """解析 SUMMARY 文本为条目列表；返回 (entries, problems)。

    entries 元素：{"line", "indent", "title", "target"}
    """
    problems = []
    entries = []
    lines = text.split("\n")
    if not lines or lines[0].strip() != "# Summary":
        problems.append(("S_HEADER", "首行为 %r" % (lines[0] if lines else "")))
    for idx, line in enumerate(lines[1:], start=2):
        if not line.strip():
            continue
        if not line.startswith("- ") and not line.lstrip().startswith("- "):
            problems.append(("S_FORMAT", "第 %d 行非列表条目：%r" % (idx, line[:80])))
            continue
        m = LINE_RE.match(line)
        if not m:
            problems.append(("S_FORMAT", "第 %d 行无法解析：%r" % (idx, line[:80])))
            continue
        entries.append({"line": idx, "indent": len(m.group("indent")),
                        "title": m.group("title"), "target": m.group("target")})
    return entries, problems


def validate(tree, summary_text, keywords_doc):
    """独立校验器：树 ↔ 镜像逐条双射 ＋ 章关键词库逐键核对。

    返回 problems 列表，元素为 (判据码, 说明)。零元素即 PASS。
    """
    problems = []

    # 一、树自身结构异常（无法被镜像表达的，先判）
    for kind, rel, detail in tree["anomalies"]:
        problems.append(("T_" + kind.upper(), "%s：%s" % (rel, detail)))

    # 二、SUMMARY 逐条比对
    entries, parse_problems = parse_summary(summary_text)
    problems.extend(parse_problems)

    expected = list(iter_entities(tree))
    exp_by_key = collections.OrderedDict()
    for level, title, target in expected:
        exp_by_key[target.rstrip("/")] = (level, title, target)

    got_by_key = collections.OrderedDict()
    for ent in entries:
        key = ent["target"].rstrip("/")
        if key in got_by_key:
            problems.append(("S_DUP", "第 %d 行与第 %d 行重复指向 %s"
                             % (ent["line"], got_by_key[key]["line"], ent["target"])))
            continue
        got_by_key[key] = ent

    missing = [k for k in exp_by_key if k not in got_by_key]
    extra = [k for k in got_by_key if k not in exp_by_key]
    for key in missing[:40]:
        problems.append(("S_MISSING", "树中实体未列出：%s" % key))
    if len(missing) > 40:
        problems.append(("S_MISSING", "另 %d 条未列出（略）" % (len(missing) - 40)))
    for key in extra[:40]:
        problems.append(("S_EXTRA", "镜像含树外条目：%s" % key))
    if len(extra) > 40:
        problems.append(("S_EXTRA", "另 %d 条树外条目（略）" % (len(extra) - 40)))

    for key, (level, title, target) in exp_by_key.items():
        ent = got_by_key.get(key)
        if ent is None:
            continue
        if ent["title"] != title:
            problems.append(("S_TITLE", "第 %d 行题面 %r ≠ 磁盘名 %r"
                             % (ent["line"], ent["title"], title)))
        if ent["indent"] != 2 * level:
            problems.append(("S_INDENT", "第 %d 行缩进 %d ≠ 第 %d 层应有的 %d"
                             % (ent["line"], ent["indent"], level, 2 * level)))
        if target.endswith("/") and not ent["target"].endswith("/"):
            problems.append(("S_SLASH", "第 %d 行目录链接缺尾斜杠：%s"
                             % (ent["line"], ent["target"])))
        if ent["target"].startswith("/") or ".." in ent["target"].split("/"):
            problems.append(("S_PATH", "第 %d 行链接目标非法：%s"
                             % (ent["line"], ent["target"])))

    # 死链与目标类型（对镜像全部条目，含树外条目）
    for key, ent in got_by_key.items():
        full = _under(tree.get("_root") or "", key)
        want_dir = not key.endswith(".md")
        exists = os.path.isdir(full) if want_dir else os.path.isfile(full)
        if not exists:
            problems.append(("S_DEAD", "第 %d 行死链：%s" % (ent["line"], ent["target"])))
        elif want_dir != os.path.isdir(full):
            problems.append(("S_KIND", "第 %d 行目标类型不符：%s"
                            % (ent["line"], ent["target"])))

    # 条目序（仅在无缺／多时判，避免连锁噪声）
    if not missing and not extra:
        seq_exp = [t.rstrip("/") for _, _, t in expected]
        seq_got = [e["target"].rstrip("/") for e in entries]
        for i, (want, got) in enumerate(zip(seq_exp, seq_got)):
            if want != got:
                problems.append(("S_ORDER", "第 %d 序位应为 %s，实为 %s"
                                 % (i + 1, want, got)))
                break

    # 三、chapter_keywords.json 逐键核对
    problems.extend(validate_keywords(tree, keywords_doc))
    return problems


def validate_keywords(tree, doc):
    problems = []
    if not isinstance(doc, dict):
        return [("K_SHAPE", "顶层不是对象")]

    exp = collections.OrderedDict()
    for vol in tree["volumes"]:
        for chap in vol["chapters"]:
            exp["%03d" % chap["num"]] = (vol["name"], chap)

    for key in doc:
        if not KEY3_RE.match(key):
            problems.append(("K_KEY_FMT", "章键 %r 非三位数字字符串" % key))
            continue
        num = int(key)
        if num < CH_NUM_MIN or num > CH_NUM_MAX:
            problems.append(("K_KEY_RANGE", "章键 %r 越界" % key))

    for key in exp:
        if key not in doc:
            problems.append(("K_MISSING", "章键 %s（%s）缺失" % (key, exp[key][1]["name"])))
    for key in doc:
        if key not in exp:
            problems.append(("K_EXTRA", "章键 %s 为树外章" % key))

    for key, (vol_name, chap) in exp.items():
        item = doc.get(key)
        if not isinstance(item, dict):
            continue
        for field in ("volume", "title", "subs", "keywords"):
            if field not in item:
                problems.append(("K_SHAPE", "章键 %s 缺字段 %s" % (key, field)))
        if item.get("volume") != vol_name:
            problems.append(("K_VOL", "章键 %s volume %r ≠ %r"
                             % (key, item.get("volume"), vol_name)))
        want_title = chapter_title(tree.get("_root") or "", chap)
        if item.get("title") != want_title:
            problems.append(("K_TITLE", "章键 %s title %r ≠ %r"
                             % (key, item.get("title"), want_title)))
        want_subs = [s["name"] for s in chap["sections"]]
        subs = item.get("subs")
        if not isinstance(subs, list):
            problems.append(("K_SHAPE", "章键 %s subs 非数组" % key))
        else:
            if subs != want_subs:
                problems.append(("K_SUBS", "章键 %s subs 与树不符（库 %d 项／树 %d 项）"
                                 % (key, len(subs), len(want_subs))))
            if not subs:
                problems.append(("K_SUBS_EMPTY", "章键 %s subs 为空（须非空）" % key))
        kws = item.get("keywords")
        if not isinstance(kws, list) or any(not isinstance(x, str) for x in kws):
            problems.append(("K_KW_TYPE", "章键 %s keywords 非字符串数组" % key))
    return problems


# ---------------------------------------------------------------- 磁盘比对

def _read_text(path):
    with open(path, "rb") as fh:
        return fh.read()


def compare_disk(out_dir, summary_text, keywords_doc):
    """与磁盘逐字节（SUMMARY）／逐键（JSON）比对，返回 problems。"""
    problems = []
    spath = os.path.join(out_dir, "SUMMARY.md")
    if not os.path.isfile(spath):
        problems.append(("D_MISSING_TEXT", "缺 %s" % spath))
    else:
        disk = _read_text(spath)
        want = summary_text.encode("utf-8")
        if disk != want:
            detail = _first_diff(disk, want)
            problems.append(("D_DRIFT_TEXT", detail))

    jpath = os.path.join(out_dir, "chapter_keywords.json")
    if not os.path.isfile(jpath):
        problems.append(("D_MISSING_JSON", "缺 %s" % jpath))
        return problems
    try:
        with open(jpath, encoding="utf-8") as fh:
            disk_doc = json.load(fh)
    except Exception as exc:
        problems.append(("K_DRIFT", "磁盘 JSON 无法解析：%s" % exc))
        return problems
    problems.extend(diff_keywords(disk_doc, keywords_doc))
    return problems


def _first_diff(disk_bytes, want_bytes):
    """定位首个差异（按行），返回可读摘要。"""
    disk_lines = disk_bytes.decode("utf-8", "replace").split("\n")
    want_lines = want_bytes.decode("utf-8", "replace").split("\n")
    for i, (d, w) in enumerate(zip(disk_lines, want_lines), start=1):
        if d != w:
            return "首个差异在第 %d 行：磁盘 %r ≠ 再生 %r" % (i, d[:90], w[:90])
    return "行数不同：磁盘 %d 行／再生 %d 行" % (len(disk_lines), len(want_lines))


def diff_keywords(disk_doc, new_doc):
    problems = []
    if not isinstance(disk_doc, dict):
        return [("K_DRIFT", "磁盘 JSON 顶层不是对象")]

    def sort_key(k):
        return (int(k) if k.isdigit() else 10 ** 9, k)

    for key in sorted(set(disk_doc) | set(new_doc), key=sort_key):
        if key not in new_doc:
            problems.append(("K_DRIFT", "键 %s 仅存于磁盘（旧键残留或树外章）" % key))
            continue
        if key not in disk_doc:
            problems.append(("K_DRIFT", "键 %s 磁盘缺失（须补）" % key))
            continue
        disk_item, new_item = disk_doc[key], new_doc[key]
        if disk_item == new_item:
            continue
        if not isinstance(disk_item, dict):
            problems.append(("K_DRIFT", "键 %s 磁盘条目非对象" % key))
            continue
        for field in ("volume", "title", "subs", "keywords"):
            if disk_item.get(field) != new_item.get(field):
                d, n = disk_item.get(field), new_item.get(field)
                problems.append(("K_DRIFT", "键 %s 字段 %s 漂移：磁盘 %r ≠ 再生 %r"
                                 % (key, field, _brief(d), _brief(n))))
    return problems


def _brief(value):
    text = json.dumps(value, ensure_ascii=False) if not isinstance(value, str) else value
    return text if len(text) <= 60 else text[:57] + "..."


# ---------------------------------------------------------------- 写盘

def _load_wo007():
    """加载同目录 wo007_idempotency（缺失时返回 None，走显式 UTF-8＋LF 兜底）。"""
    path = HERE
    if path not in sys.path:
        sys.path.insert(0, path)
    try:
        import wo007_idempotency as mod
        return mod
    except Exception:
        return None


def normalization_probe(text):
    """以 wo007 归一化函数做中性预检：返回 (bool 会改动, 说明)。"""
    mod = _load_wo007()
    if mod is None:
        return False, ""
    probe = text
    try:
        probe = mod.normalize_dbnames(probe, repo=None)
        probe = mod.normalize_terms(probe)
    except Exception:
        return False, ""
    if probe == text:
        return False, ""
    return True, "术语／库名归一化会改写产物（大纲名含应在上游改名的旧词），拒绝写入"


def atomic_write(path, text):
    """临时件同目录写入后 os.replace 原子替换；UTF-8 无 BOM ＋ LF。

    优先走 wo007 的 `write_guard()`（库名＋术语＋LF 三归一），写完回读**逐字节**校验；
    若归一化改动了产物（说明大纲名含应在上游改名的旧词），退 `write_text_lf()` 并保留
    原文——调用方已在写盘前以中性预检拒绝此类情形。
    """
    directory = os.path.dirname(path)
    os.makedirs(directory, exist_ok=True)
    mod = _load_wo007()
    want = text.encode("utf-8")
    fd, tmp = tempfile.mkstemp(dir=directory, prefix=".sync_mirror_", suffix=".tmp")
    os.close(fd)
    try:
        wrote = False
        if mod is not None and hasattr(mod, "write_guard"):
            try:
                mod.write_guard(tmp, text)
                with open(tmp, "rb") as fh:
                    wrote = fh.read() == want
            except Exception:
                wrote = False
        if not wrote:
            if mod is not None and hasattr(mod, "write_text_lf"):
                mod.write_text_lf(tmp, text, encoding="utf-8")
            else:
                with open(tmp, "w", encoding="utf-8", newline="\n") as fh:
                    fh.write(text)
                    fh.flush()
                    os.fsync(fh.fileno())
            with open(tmp, "rb") as fh:
                if fh.read() != want:
                    raise OSError("临时件内容与预期不一致：%s" % tmp)
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


# ---------------------------------------------------------------- 命令实现

def _build_all(root, out_dir, mapping_path):
    """扫描＋生成，返回 (tree, summary_text, keywords_doc, notes)。"""
    tree = scan_tree(root)
    tree["_root"] = root
    summary_text = render_summary(tree)
    legacy, mode = load_legacy_keywords(out_dir)
    old2new = {}
    if mode == "legacy":
        old2new = load_mapping(mapping_path)
    keywords_doc, notes = build_keywords(tree, legacy, mode, old2new, root)
    if notes["unmapped"]:
        raise Fatal("旧库章键缺 old→new 映射（关键词将丢失，拒判）：%s"
                    % "、".join(notes["unmapped"][:20]))
    return tree, summary_text, keywords_doc, notes


def _print_targets(root, out_dir):
    print("  大纲树根：%s" % root)
    print("  镜像目录：%s" % out_dir)


def _print_counts(tree, summary_text, keywords_doc):
    nv, nc, ns, nb, total = tree_counts(tree)
    entries, _ = parse_summary(summary_text)
    empty_subs = [k for k, v in keywords_doc.items() if not v.get("subs")]
    print("  树：%d 卷 / %d 章 / %d 节 / %d 小节（实体合计 %d）"
          % (nv, nc, ns, nb, total))
    print("  镜像条目：%d；章键：%d；subs 空键：%d"
          % (len(entries), len(keywords_doc), len(empty_subs)))
    return entries, empty_subs


def _print_problems(problems, limit=80):
    counter = collections.Counter(code for code, _ in problems)
    for code in sorted(counter):
        print("  [%s] %s（%d 项）" % (code, CODE_TEXT.get(code, code), counter[code]))
    print("  " + "-" * 68)
    for code, detail in problems[:limit]:
        print("    · %s：%s" % (code, detail))
    if len(problems) > limit:
        print("    …（另 %d 项，已按判据码汇总）" % (len(problems) - limit))


def cmd_list(root, out_dir, mapping_path):
    tree, summary_text, keywords_doc, notes = _build_all(root, out_dir, mapping_path)
    print("=" * 72)
    print("大纲目录镜像计数统计")
    print("=" * 72)
    _print_targets(root, out_dir)
    entries, empty_subs = _print_counts(tree, summary_text, keywords_doc)
    for vol in tree["volumes"]:
        ns = sum(len(c["sections"]) for c in vol["chapters"])
        nb = sum(len(s["subs"]) for c in vol["chapters"] for s in c["sections"])
        print("    %s：%d 章 / %d 节 / %d 小节"
              % (vol["name"], len(vol["chapters"]), ns, nb))
    print("  旧库形态：%s；沿用旧词表 %d 章；新派生 %d 章；旧键映射 %d"
          % (notes["mode"], notes["kept"], notes["derived"], notes["mapped_from_legacy"]))
    if empty_subs:
        print("  subs 空键：%s" % "、".join(sorted(empty_subs)[:20]))
    if tree["anomalies"]:
        print("  树结构异常：%d 项" % len(tree["anomalies"]))
        for kind, rel, detail in tree["anomalies"][:20]:
            print("    · [%s] %s：%s" % (kind, rel, detail))
    print("  镜像条目合计：%d" % len(entries))
    return 0


def cmd_check(root, out_dir, mapping_path, verbose=False):
    print("=" * 72)
    print("大纲目录镜像双射校验")
    print("=" * 72)
    tree, summary_text, keywords_doc, notes = _build_all(root, out_dir, mapping_path)
    _print_targets(root, out_dir)
    entries, empty_subs = _print_counts(tree, summary_text, keywords_doc)

    self_problems = validate(tree, summary_text, keywords_doc)
    disk_problems = compare_disk(out_dir, summary_text, keywords_doc)
    problems = self_problems + disk_problems

    missing = sum(1 for c, _ in problems if c == "S_MISSING")
    extra = sum(1 for c, _ in problems if c == "S_EXTRA")
    dead = sum(1 for c, _ in problems if c == "S_DEAD")
    print("  缺 %d／多 %d／死链 %d；判据命中 %d 项（自校验 %d ＋ 磁盘比对 %d）"
          % (missing, extra, dead, len(problems), len(self_problems), len(disk_problems)))
    if notes["mode"] == "legacy":
        print("  ⚠ 现有库为旧键形态（自然数），本轮已按 old→new 映射生成三位新键；落盘须 --write")
    if notes["retitled"]:
        print("  INFO 卷属／题面按树刷新 %d 章：" % len(notes["retitled"])
              + "、".join(notes["retitled"][:20]))
    if verbose:
        print("  entries=%d empty_subs=%d" % (len(entries), len(empty_subs)))

    if not problems:
        print("  " + "-" * 68)
        print("  校验：PASS（逐条双射一致，逐键一致，零漂移）")
        return 0
    print("  " + "-" * 68)
    print("  校验：FAIL（%d 项）" % len(problems))
    _print_problems(problems)
    return 1


def cmd_write(root, out_dir, mapping_path):
    print("=" * 72)
    print("大纲目录镜像再生写盘")
    print("=" * 72)
    tree, summary_text, keywords_doc, notes = _build_all(root, out_dir, mapping_path)
    _print_targets(root, out_dir)
    entries, empty_subs = _print_counts(tree, summary_text, keywords_doc)

    problems = validate(tree, summary_text, keywords_doc)
    if problems:
        print("  拒绝写入：自校验未通过 %d 项" % len(problems))
        _print_problems(problems)
        return 1

    dirty, why = normalization_probe(summary_text + render_keywords(keywords_doc))
    if dirty:
        print("  [W_NORM] %s" % why)
        return 1

    summary_path = os.path.join(out_dir, "SUMMARY.md")
    keywords_path = os.path.join(out_dir, "chapter_keywords.json")
    atomic_write(summary_path, summary_text)
    atomic_write(keywords_path, render_keywords(keywords_doc))
    print("  [written] %s（%d 条）" % (summary_path, len(entries)))
    print("  [written] %s（%d 键，subs 空键 %d）"
          % (keywords_path, len(keywords_doc), len(empty_subs)))
    if notes["mode"] == "legacy":
        print("  旧键已按 old→new 映射迁移为三位新键，旧键未残留")
    return 0


# ---------------------------------------------------------------- 自检

def _mk(path, text=""):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def build_fixture_tree(tree_dir):
    """合成树：2 卷、3 章、4 节、6 小节（含 1 个空小节文件）。"""
    shutil.rmtree(tree_dir, ignore_errors=True)
    v1 = os.path.join(tree_dir, "第001卷-合成甲")
    v2 = os.path.join(tree_dir, "第002卷-合成乙")
    entries = [
        (os.path.join(v1, "第001章-卷总览", "001.1-章级综合", "001.1.1-概述.md"),
         "# 001.1.1 概述\n"),
        (os.path.join(v1, "第001章-卷总览", "001.1-章级综合", "001.1.2-空件.md"), ""),
        (os.path.join(v1, "第002章-alpha起点", "002.1-章级综合", "002.1.1-alpha小节.md"),
         "# 002.1.1 alpha\n"),
        (os.path.join(v1, "第002章-alpha起点", "002.2-beta路径", "002.2.1-beta小节.md"),
         "# 002.2.1 beta\n"),
        (os.path.join(v1, "第002章-alpha起点", "002.2-beta路径", "002.2.2-gamma小节.md"),
         "# 002.2.2 gamma\n"),
        (os.path.join(v2, "第003章-delta收束", "003.1-章级综合", "003.1.1-delta小节.md"),
         "# 003.1.1 delta\n"),
    ]
    for path, text in entries:
        _mk(path, text)
    # 保障四个节目录齐备（含空节目录也须照列）
    for path in (
        os.path.join(v1, "第001章-卷总览", "001.1-章级综合"),
        os.path.join(v1, "第002章-alpha起点", "002.1-章级综合"),
        os.path.join(v1, "第002章-alpha起点", "002.2-beta路径"),
        os.path.join(v2, "第003章-delta收束", "003.1-章级综合"),
    ):
        os.makedirs(path, exist_ok=True)


def _codes(problems):
    return [c for c, _ in problems]


def selftest():
    fix = os.path.join(REPO, SELFTEST_REL)
    tree_dir = os.path.join(fix, "tree")
    out_dir = os.path.join(fix, "out")
    legacy_dir = os.path.join(fix, "out_legacy")
    print("=" * 72)
    print("大纲目录镜像自检（合成夹具，保留于 %s）" % SELFTEST_REL)
    print("=" * 72)
    ok = True
    n_chk = [0]

    def chk(name, cond, extra=""):
        nonlocal ok
        ok = ok and bool(cond)
        n_chk[0] += 1
        print("  [%s] %s%s" % ("PASS" if cond else "FAIL", name,
                              ("  " + extra) if extra else ""))

    try:
        build_fixture_tree(tree_dir)
        tree = scan_tree(tree_dir)
        tree["_root"] = tree_dir
        nv, nc, ns, nb, total = tree_counts(tree)
        chk("合成树计数 2 卷／3 章／4 节／6 小节",
            (nv, nc, ns, nb) == (2, 3, 4, 6), "实为 %d/%d/%d/%d" % (nv, nc, ns, nb))

        summary_text = render_summary(tree)
        entries, parse_problems = parse_summary(summary_text)
        chk("镜像条目数＝树实体数", len(entries) == total,
            "%d vs %d" % (len(entries), total))
        chk("SUMMARY 解析零问题", not parse_problems, str(parse_problems[:2]))

        indent_ok = True
        for level, title, target in iter_entities(tree):
            for ent in entries:
                if ent["target"] == target:
                    if ent["indent"] != 2 * level or ent["title"] != title:
                        indent_ok = False
                    break
            else:
                indent_ok = False
        chk("缩进（0/2/4/6）与题面逐条正确", indent_ok)

        dead = [e["target"] for e in entries
                if not os.path.exists(_under(tree_dir, e["target"].rstrip("/")))]
        chk("链接目标全部存在", not dead, str(dead[:3]))
        empty_listed = any(e["target"].endswith("001.1.2-空件.md") for e in entries)
        chk("空小节文件照列", empty_listed)

        keywords_doc, notes = build_keywords(tree, {}, "absent", {}, tree_dir)
        probs_self = validate(tree, summary_text, keywords_doc)
        chk("自校验 PASS（零判据命中）", not probs_self, str(probs_self[:3]))
        chk("章键为三位且 3 个", list(keywords_doc) == ["001", "002", "003"],
            str(list(keywords_doc)))
        chk("subs 非空", all(keywords_doc[k]["subs"] for k in keywords_doc))
        chk("新章按章题／节题派生拉丁词元（无拉丁词元的章为空数组）",
            keywords_doc["001"]["keywords"] == []
            and keywords_doc["002"]["keywords"] == ["alpha", "beta"]
            and keywords_doc["003"]["keywords"] == ["delta"],
            str([keywords_doc[k]["keywords"] for k in keywords_doc]))
        chk("派生词元 ≤8 且小写去重",
            all(len(keywords_doc[k]["keywords"]) <= MAX_KW
                and len(set(keywords_doc[k]["keywords"])) == len(keywords_doc[k]["keywords"])
                and all(x == x.lower() for x in keywords_doc[k]["keywords"])
                for k in keywords_doc))

        chk("再生幂等（二次渲染逐字节相同）",
            render_summary(tree) == summary_text
            and render_keywords(keywords_doc) == render_keywords(keywords_doc))

        # 写盘 → 与磁盘逐字节／逐键比对
        shutil.rmtree(out_dir, ignore_errors=True)
        atomic_write(os.path.join(out_dir, "SUMMARY.md"), summary_text)
        atomic_write(os.path.join(out_dir, "chapter_keywords.json"),
                     render_keywords(keywords_doc))
        chk("写盘后磁盘比对零漂移",
            not compare_disk(out_dir, summary_text, keywords_doc),
            str(compare_disk(out_dir, summary_text, keywords_doc)[:3]))
        raw = _read_text(os.path.join(out_dir, "SUMMARY.md"))
        chk("写盘 LF 且无 BOM", b"\r" not in raw and not raw.startswith(b"\xef\xbb\xbf"))

        # 旧键映射（old 1→new 3、old 2→new 1）
        shutil.rmtree(legacy_dir, ignore_errors=True)
        os.makedirs(legacy_dir, exist_ok=True)
        legacy = {
            "1": {"volume": "第00卷-旧", "title": "旧题一",
                  "subs": ["旧节"], "keywords": ["legacykw"]},
            "2": {"volume": "第00卷-旧", "title": "旧题二",
                  "subs": ["旧节"], "keywords": []},
        }
        _mk(os.path.join(legacy_dir, "chapter_keywords.json"),
            json.dumps(legacy, ensure_ascii=False, indent=2) + "\n")
        mapping_path = os.path.join(fix, "mapping.json")
        _mk(mapping_path, json.dumps(
            {"chapter_map": [{"old_num": 1, "new_num": 3},
                             {"old_num": 2, "new_num": 1}]},
            ensure_ascii=False, indent=2) + "\n")
        legacy_doc, mode = load_legacy_keywords(legacy_dir)
        mapped, mnotes = build_keywords(tree, legacy_doc, mode, load_mapping(mapping_path),
                                        tree_dir)
        chk("旧键形态判定为 legacy", mode == "legacy", mode)
        chk("旧词表按旧章身份保留到新键 003",
            mapped.get("003", {}).get("keywords") == ["legacykw"],
            str(mapped.get("003")))
        chk("旧键不残留", not any(KEYN_RE.match(k) and not KEY3_RE.match(k) for k in mapped))
        chk("无旧身份的章已派生词元", bool(mapped["002"]["keywords"]),
            str(mapped["002"]["keywords"]))
        chk("映射说明记录来源（2 键）", mnotes["mapped_from_legacy"] == 2,
            str(mnotes["mapped_from_legacy"]))

        # 负向夹具（校验器须判 FAIL；题面改字而计数不变亦须 FAIL）
        lines = summary_text.split("\n")
        target_line = next(i for i, ln in enumerate(lines)
                           if "002.2.1-beta小节.md" in ln)

        def mutated(mutator):
            copy = list(lines)
            return "\n".join(mutator(copy))

        def drop_entry(buf):
            del buf[target_line]
            return buf

        def add_extra(buf):
            buf.append("- [第004章-树外](第002卷-合成乙/第004章-树外/)")
            return buf

        def dead_link(buf):
            buf[target_line] = buf[target_line].replace(
                "002.2.1-beta小节.md", "002.2.9-不存在.md")
            return buf

        def retitle(buf):
            buf[target_line] = buf[target_line].replace(
                "[002.2.1-beta小节.md]", "[002.2.1-beta小節.md]")
            return buf

        def empty_subs(mutate_doc):
            for key in mutate_doc:
                mutate_doc[key]["subs"] = []
            return mutate_doc

        cases = [
            ("缺条", drop_entry, "S_MISSING", keywords_doc),
            ("树外条", add_extra, "S_EXTRA", keywords_doc),
            ("死链", dead_link, "S_DEAD", keywords_doc),
            ("题面改字（计数不变）", retitle, "S_TITLE", keywords_doc),
            ("subs 恒空", None, "K_SUBS_EMPTY", empty_subs(json.loads(json.dumps(keywords_doc)))),
        ]
        for name, mutator, expect, kw_doc in cases:
            text = summary_text if mutator is None else mutated(mutator)
            probs = validate(tree, text, kw_doc)
            codes = _codes(probs)
            hit = expect in codes
            chk("负向夹具 %s 命中 %s" % (name, expect), hit, "实得 %s" % sorted(set(codes)))
            chk("负向夹具 %s 整体判 FAIL" % name, bool(probs))
            # 逐条比对的存在性证明：题面改字时条目数须不变
            if name == "题面改字（计数不变）":
                n_before = len(parse_summary(summary_text)[0])
                n_after = len(parse_summary(text)[0])
                chk("题面改字后条目数不变（证明非计数判据）", n_before == n_after,
                    "%d vs %d" % (n_before, n_after))

        print("-" * 72)
        if ok:
            print("  ✅ selftest PASS：自检 %d 项，负向夹具 5 类全部命中" % n_chk[0])
            return 0
        print("  ❌ selftest FAIL", file=sys.stderr)
        return 1
    except Fatal as exc:
        print("  ❌ Fatal：%s" % exc, file=sys.stderr)
        return 1
    except AssertionError as exc:
        print("  ❌ AssertionError：%s" % exc, file=sys.stderr)
        return 1


# ---------------------------------------------------------------- 入口

def main():
    ap = argparse.ArgumentParser(
        description="大纲目录镜像全量再生与双射校验（SUMMARY.md／chapter_keywords.json）")
    ap.add_argument("--check", action="store_true", help="缺省：漂移报告（漂移 exit 1）")
    ap.add_argument("--write", action="store_true", help="生成并原子写盘两件镜像")
    ap.add_argument("--list", action="store_true", help="打印层级计数与镜像统计")
    ap.add_argument("--selftest", action="store_true", help="合成夹具自检（script/_mirror_selftest）")
    ap.add_argument("--root", default=None, help="大纲树根（默认 %s）" % DEFAULT_ROOT)
    ap.add_argument("--out", default=None, help="镜像目录（默认 %s）" % DEFAULT_OUT)
    ap.add_argument("--mapping", default=None, help="章号映射表（默认 %s）" % DEFAULT_MAPPING)
    ap.add_argument("--verbose", action="store_true", help="附加明细")
    args = ap.parse_args()

    if args.selftest:
        return selftest()

    root = os.path.abspath(args.root or DEFAULT_ROOT)
    out_dir = os.path.abspath(args.out or DEFAULT_OUT)
    mapping_path = os.path.abspath(args.mapping or DEFAULT_MAPPING)
    try:
        if args.write:
            return cmd_write(root, out_dir, mapping_path)
        if args.list:
            return cmd_list(root, out_dir, mapping_path)
        return cmd_check(root, out_dir, mapping_path, verbose=args.verbose)
    except Fatal as exc:
        print("FATAL：%s" % exc, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
