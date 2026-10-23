# -*- coding: utf-8 -*-
"""build_theme_index.py —— 大纲主题词索引生成器（固定脚本，2026-10-21 立）。

职责：扫描 `05-卷册大纲/` 四层树，按受控词表 `主题词表.json` 为题面与正文取词，
生成两件派生权威件（均写大纲树根级）：

  * `chapter_keywords.json`：schema `theme-index/4`
      章（523）／节（3,705）全覆盖；普通节 3–6 词、元节 1–3 词；
      小节只存与所属节的差分；附 `technical_terms`／`projects`／`subs_sha1`。
  * `theme_index.json`：schema `theme-reverse/2`
      主题→章／节／小节反查，供 claim 库与大纲库按主题分流与上卷。
      节键为“卷／章／节”复合键 `V01-C001-1.1`，避免 `N.M` 跨章碰撞。

取词：题面 ×3、要点段 ×2、正文 ×1；idf 按小节文档频率；最长匹配优先；
`bsd`／`freebsd`／`linux`／`历史` 等无区分度泛词由词表 `banned` 强制排除。

用法：
  C:/Python314/python.exe build_theme_index.py --check         # 结构＋哈希双射（快）
  C:/Python314/python.exe build_theme_index.py --check --deep  # 全量重算比对（慢）
  C:/Python314/python.exe build_theme_index.py --write         # 幂等写盘
  C:/Python314/python.exe build_theme_index.py --list          # 统计
  C:/Python314/python.exe build_theme_index.py --selftest      # 负向夹具自检
"""
import argparse
import copy
import datetime
import hashlib
import io
import json
import math
import os
import re
import shutil
import sys

sys.stdout.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, HERE)
from wo007_idempotency import write_text_lf  # noqa: E402

TREE = os.path.join(REPO, "05-卷册大纲")
VOCAB = os.path.join(HERE, "主题词表.json")
KW = "chapter_keywords.json"
REV = "theme_index.json"
SCHEMA_KW = "theme-index/4"
SCHEMA_REV = "theme-reverse/2"

VOL_RE = re.compile(r"^第(\d{1,3})卷")
CH_RE = re.compile(r"^第(\d{1,3})章(?:-(?P<slug>.+))?$")
SEC_RE = re.compile(r"^(\d{1,3})\.(\d{1,3})-(?P<slug>.+)$")
SUB_RE = re.compile(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,4})-(?P<slug>.+)\.md$")
H1_RE = re.compile(r"^#\s+(?:\d+(?:\.\d+){0,2}\s*)?(?P<title>.*)$")
YD_RE = re.compile(r"\*\*要点\*\*\s*[：:]\s*(?P<y>.*?)(?:\n\s*\n|\n\s*\*\*|$)", re.S)
LAT_RE = re.compile(r"[A-Za-z][A-Za-z0-9.+_-]*")
CJK_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")

MIN_T, MAX_T = 3, 6
META_MIN, META_MAX = 1, 3
MAX_TECH = 8
MAX_PROJ = 3
MAX_BODY_COUNT = 10
TRIM_RATIO = 0.12
META_DOMAIN = "TH-HIS-000"
HIS_TITLE_RE = re.compile("史料|证据|叙事|采访|编纂|书目|索引|元数据|方法论|史学|哲学|反思|形式主义|辩证|自反|争议|传说")
DEFAULT_LABELS = {
    "TH-OS-000": "进程管理", "TH-FS-000": "虚拟文件系统", "TH-NET-000": "TCP/IP 网络协议栈",
    "TH-SEC-000": "访问控制", "TH-HW-000": "设备驱动", "TH-VM-000": "虚拟机",
    "TH-LANG-000": "编译器", "TH-REL-000": "版本发布", "TH-LAW-000": "BSD 许可证",
    "TH-GOV-000": "治理模式", "TH-BIZ-000": "商业模式", "TH-HIS-000": "编纂体例",
}


class Fatal(Exception):
    pass


# ---------------------------------------------------------------- 词表与匹配

def load_vocab(path=VOCAB):
    if not os.path.isfile(path):
        raise Fatal("词表不存在：%s" % path)
    raw = open(path, "rb").read()
    doc = json.loads(raw.decode("utf-8"))
    if doc.get("schema") != "theme-vocab/1":
        raise Fatal("词表 schema 不符：%r" % doc.get("schema"))
    return doc, hashlib.sha256(raw).hexdigest()


def build_matcher(vocab):
    trie, latin, by_id = {}, {}, {}
    for c in vocab["concepts"]:
        by_id[c["id"]] = c
        for p in [c["prefLabel"]] + list(c.get("altLabels") or []):
            p = p.strip()
            if not p:
                continue
            node = trie
            for ch in p:
                node = node.setdefault(ch, {})
            node.setdefault("", []).append(c["id"])
        for t in c.get("techTerms") or []:
            latin.setdefault(t.lower(), []).append(c["id"])
    return trie, latin, by_id


def scan_text(text, trie, latin):
    ids = {}
    n = len(text)
    for i, ch in enumerate(text):
        node = trie.get(ch)
        if node is None:
            continue
        j = i
        while True:
            for cid in node.get("", ()):
                ids[cid] = ids.get(cid, 0) + 1
            j += 1
            if j >= n:
                break
            nxt = node.get(text[j])
            if nxt is None:
                break
            node = nxt
    for m in LAT_RE.finditer(text):
        for cid in latin.get(m.group(0).lower(), ()):
            ids[cid] = ids.get(cid, 0) + 1
    return ids


def cap(counts, limit):
    return {k: min(v, limit) for k, v in counts.items()}


# ---------------------------------------------------------------- 树扫描

def h1_title(path, fallback):
    try:
        with io.open(path, encoding="utf-8") as fh:
            for ln in fh:
                s = ln.rstrip("\n")
                if not s.strip():
                    continue
                if s.startswith("# "):
                    m = H1_RE.match(s)
                    return (m.group("title").strip() if m else s[2:].strip()) or fallback
                break
    except OSError:
        pass
    return fallback


def scan_tree(root=TREE):
    if not os.path.isdir(root):
        raise Fatal("大纲树不存在：%s" % root)
    volumes = []
    for vname in sorted(os.listdir(root)):
        vdir = os.path.join(root, vname)
        if not os.path.isdir(vdir) or not VOL_RE.match(vname):
            continue
        vnum = int(VOL_RE.match(vname).group(1))
        chapters = []
        chs = sorted([d for d in os.listdir(vdir)
                      if os.path.isdir(os.path.join(vdir, d)) and CH_RE.match(d)],
                     key=lambda x: int(CH_RE.match(x).group(1)))
        for ci, cname in enumerate(chs):
            m = CH_RE.match(cname)
            chnum = int(m.group(1))
            cdir = os.path.join(vdir, cname)
            sections = []
            secs = sorted([d for d in os.listdir(cdir)
                           if os.path.isdir(os.path.join(cdir, d)) and SEC_RE.match(d)],
                          key=lambda x: (int(SEC_RE.match(x).group(1)),
                                         int(SEC_RE.match(x).group(2))))
            for sname in secs:
                sm = SEC_RE.match(sname)
                sdir = os.path.join(cdir, sname)
                sec_key = "V%02d-C%03d-%d.%d" % (vnum, chnum, int(sm.group(1)), int(sm.group(2)))
                subs = []
                for f in sorted(os.listdir(sdir)):
                    if not SUB_RE.match(f):
                        continue
                    fm = SUB_RE.match(f)
                    path = os.path.join(sdir, f)
                    subs.append({
                        "id": "%s.%s.%s" % fm.group(1, 2, 3),
                        "key": "%s.%d" % (sec_key, int(fm.group(3))),
                        "slug": fm.group("slug"),
                        "file": f,
                        "path": path,
                        "title": h1_title(path, fm.group("slug")),
                    })
                sections.append({
                    "id": "%s.%s" % (sm.group(1), sm.group(2)),
                    "key": sec_key,
                    "m": int(sm.group(2)),
                    "slug": sm.group("slug"),
                    "subs": subs,
                })
            chapters.append({
                "num": "%03d" % chnum,
                "slug": m.group("slug") or "",
                "first": ci == 0,
                "last": ci == len(chs) - 1,
                "sections": sections,
            })
        volumes.append({"name": vname, "num": vnum, "chapters": chapters})
    return volumes


def tree_stats(volumes):
    ch = sum(len(v["chapters"]) for v in volumes)
    sec = sum(len(c["sections"]) for v in volumes for c in v["chapters"])
    sub = sum(len(s["subs"]) for v in volumes for c in v["chapters"] for s in c["sections"])
    return len(volumes), ch, sec, sub


def content_sha(volumes, root=TREE):
    h = hashlib.sha256()
    rows = []
    for v in volumes:
        for c in v["chapters"]:
            for s in c["sections"]:
                for x in s["subs"]:
                    rows.append((os.path.relpath(x["path"], root).replace("\\", "/"),
                                 hashlib.sha256(open(x["path"], "rb").read()).hexdigest()))
    for rel, sha in sorted(rows):
        h.update(rel.encode("utf-8"))
        h.update(b"\0")
        h.update(sha.encode("ascii"))
        h.update(b"\n")
    return h.hexdigest()


def subs_sha1(section):
    h = hashlib.sha1()
    for x in section["subs"]:
        h.update(("%s-%s-%s\n" % (x.get("key") or x["id"], x["slug"], x["title"])).encode("utf-8"))
    return h.hexdigest()


# ---------------------------------------------------------------- 取词

def is_meta(chapter, section):
    return section["m"] == 0 or chapter["first"] or chapter["last"]


def domain_of(cid, by_id):
    c = by_id.get(cid) or {}
    return cid if c.get("level") == "domain" else c.get("broader")


def label_of(cid, by_id):
    return (by_id.get(cid) or {}).get("prefLabel", cid)


def pick_themes(cands, kmin, kmax, by_id, mandatory=None, his_cap=None):
    """按分数选题；题面命中词必选；史学域词受 his_cap 限制；不做低分兜底填充。"""
    arr = sorted(cands.items(), key=lambda kv: (-kv[1], kv[0]))
    if not arr:
        return []
    top = arr[0][1]
    mand = set(mandatory or ())
    out = []

    def take(cid):
        lab = label_of(cid, by_id)
        if any(lab in label_of(o, by_id) or label_of(o, by_id) in lab for o in out):
            return False
        out.append(cid)
        return True

    for cid, _score in arr:
        if cid in mand and len(out) < kmax:
            take(cid)
    for cid, score in arr:
        if len(out) >= kmax:
            break
        if cid in out:
            continue
        if score < top * TRIM_RATIO:
            continue
        if (his_cap is not None and domain_of(cid, by_id) == META_DOMAIN
                and cid not in mand):
            n_his = sum(1 for o in out if domain_of(o, by_id) == META_DOMAIN)
            if n_his >= his_cap:
                continue
        take(cid)
    return out


def extract_projects(text, vocab):
    low = text.lower()
    out = []
    for pid, aliases in vocab.get("projects", {}).items():
        n = sum(low.count(a.lower()) for a in aliases)
        if n:
            out.append((pid, n))
    out.sort(key=lambda x: (-x[1], x[0]))
    return [p for p, _n in out[:MAX_PROJ]]


def extract_tech(text, themes, by_id):
    low = text.lower()
    seen, out = set(), []
    for cid in themes:
        for t in (by_id.get(cid) or {}).get("techTerms") or []:
            tl = t.lower()
            if tl in seen:
                continue
            if re.search(r"(?<![a-z0-9])" + re.escape(tl) + r"(?![a-z0-9])", low):
                seen.add(tl)
                out.append(tl)
    return out[:MAX_TECH]


def auto_terms(title, existing, banned, vocab_labels):
    """标题内 2–6 字中文名词补位（最多 2 个，不臆造）。"""
    out = []
    for run in re.findall(r"[\u4e00-\u9fff]{2,6}", title):
        if run in banned or run in vocab_labels or run in existing or run in out:
            continue
        out.append(run)
        if len(out) >= 2:
            break
    return out


def doc_counts(path, title, trie, latin):
    text = open(path, encoding="utf-8").read()
    m = YD_RE.search(text)
    yao = m.group("y") if m else ""
    t = cap(scan_text(title, trie, latin), 3)
    y = cap(scan_text(yao, trie, latin), 3)
    b = cap(scan_text(text, trie, latin), MAX_BODY_COUNT)
    merged = {}
    for cid in set(t) | set(y) | set(b):
        merged[cid] = 3 * t.get(cid, 0) + b.get(cid, 0) + y.get(cid, 0)
    return merged, set(t)


# ---------------------------------------------------------------- 索引构建

def _sec_key(sid):
    m = re.match(r"^V(\d+)-C(\d+)-(\d+)\.(\d+)$", sid)
    if not m:
        raise Fatal("非法节键：%s" % sid)
    return tuple(int(x) for x in m.groups())


def _sub_key(sid):
    m = re.match(r"^V(\d+)-C(\d+)-(\d+)\.(\d+)\.(\d+)$", sid)
    if not m:
        raise Fatal("非法小节键：%s" % sid)
    return tuple(int(x) for x in m.groups())


def build_docs(volumes, vocab, vocab_sha, content_hash, tree_root=TREE):
    trie, latin, by_id = build_matcher(vocab)
    banned = set(vocab.get("banned") or [])
    vocab_labels = {c["prefLabel"] for c in vocab["concepts"]}

    sub_docs, df, title_ids = [], {}, {}
    for v in volumes:
        for c in v["chapters"]:
            for s in c["sections"]:
                for x in s["subs"]:
                    raw, tids = doc_counts(x["path"], x["title"], trie, latin)
                    raw = {cid: n for cid, n in raw.items() if n > 0}
                    title_ids[x["key"]] = tids
                    for cid in raw:
                        df[cid] = df.get(cid, 0) + 1
                    sub_docs.append((v, c, s, x, raw))
    n_docs = max(len(sub_docs), 1)
    weights = {}
    for _v, _c, _s, x, raw in sub_docs:
        weights[x["key"]] = {
            cid: n * (math.log((n_docs + 1.0) / (df.get(cid, 1) + 0.5)) + 1.0)
            for cid, n in raw.items()
        }
    sub_pick = {}
    for v, c, s, x, _raw in sub_docs:
        cands = weights[x["key"]]
        if is_meta(c, s):
            cands = {cid: sc for cid, sc in cands.items()
                     if domain_of(cid, by_id) == META_DOMAIN}
            pick = pick_themes(cands, META_MIN, META_MAX, by_id)
        else:
            cap = 3 if HIS_TITLE_RE.search(x["title"]) else 1
            pick = pick_themes(cands, MIN_T, MAX_T, by_id,
                               mandatory=title_ids.get(x["id"]), his_cap=cap)
        sub_pick[x["key"]] = pick

    sections_out, chapters_out = {}, {}
    for v in volumes:
        for c in v["chapters"]:
            for s in c["sections"]:
                sec_df, sec_score = {}, {}
                for x in s["subs"]:
                    for cid in sub_pick.get(x["key"], []):
                        sec_df[cid] = sec_df.get(cid, 0) + 1
                        sec_score[cid] = sec_score.get(cid, 0.0) + weights[x["key"]].get(cid, 0.0)
                cands = {cid: sec_df[cid] * 1e6 + sec_score[cid] for cid in sec_df}
                sec_tids = set(scan_text(s["slug"], trie, latin))
                for cid in sec_tids:
                    cands[cid] = max(cands.get(cid, 0.0), 1e9)
                meta = is_meta(c, s)
                if meta:
                    cands = {cid: sc for cid, sc in cands.items()
                             if domain_of(cid, by_id) == META_DOMAIN}
                    themes = pick_themes(cands, META_MIN, META_MAX, by_id)
                    if not themes:
                        themes = _default_meta(by_id)
                else:
                    cap = 3 if HIS_TITLE_RE.search(s["slug"]) else 1
                    themes = pick_themes(cands, MIN_T, MAX_T, by_id,
                                         mandatory=sec_tids, his_cap=cap)
                proj_n, tech_n = {}, {}
                for x in s["subs"]:
                    for p in extract_projects(x["title"], vocab):
                        proj_n[p] = proj_n.get(p, 0) + 1
                    for t in extract_tech(x["title"], sub_pick.get(x["key"], []), by_id):
                        tech_n[t] = tech_n.get(t, 0) + 1
                sections_out[s["key"]] = {
                    "chapter": c["num"],
                    "title": s["slug"],
                    "meta": meta,
                    "domains": [],
                    "themes": themes,
                    "projects": [p for p, _n in sorted(
                        proj_n.items(), key=lambda kv: (-kv[1], kv[0]))[:MAX_PROJ]],
                    "technical_terms": [t for t, _n in sorted(
                        tech_n.items(), key=lambda kv: (-kv[1], kv[0]))[:MAX_TECH]],
                    "subs": len(s["subs"]),
                    "subs_sha1": subs_sha1(s),
                }
            themes, doms, proj = {}, {}, {}
            for s in c["sections"]:
                row = sections_out[s["key"]]
                for cid in row["themes"]:
                    themes[cid] = themes.get(cid, 0) + 1
                for d in row["domains"]:
                    doms[d] = doms.get(d, 0) + 1
                for p in row["projects"]:
                    proj[p] = proj.get(p, 0) + 1
            ch_themes = [cid for cid, _n in sorted(
                themes.items(), key=lambda kv: (-kv[1], kv[0]))[:8]]
            ch_domains = [d for d, _n in sorted(
                doms.items(), key=lambda kv: (-kv[1], kv[0]))[:3]]
            chapters_out[c["num"]] = {
                "volume": v["name"],
                "title": c["slug"] or c["num"],
                "domains": ch_domains,
                "themes": ch_themes,
                "sections": len(c["sections"]),
            }

    default_ids = {}
    for d, lab in DEFAULT_LABELS.items():
        for cid, cc in by_id.items():
            if cc["prefLabel"] == lab:
                default_ids[d] = [cid]
                break
    # 第二遍：节级补位（继承章级→卷级→域默认→标题自动词）
    vol_themes = {}
    for v in volumes:
        agg = {}
        for c in v["chapters"]:
            for cid in chapters_out[c["num"]]["themes"]:
                agg[cid] = agg.get(cid, 0) + 1
        vol_themes[v["name"]] = [cid for cid, _n in sorted(
            agg.items(), key=lambda kv: (-kv[1], kv[0]))[:8]]
    for v in volumes:
        for c in v["chapters"]:
            for s in c["sections"]:
                row = sections_out[s["key"]]
                need = META_MIN if row["meta"] else MIN_T
                allow_his = bool(HIS_TITLE_RE.search(row["title"])) or row["meta"]
                his_n = sum(1 for cid in row["themes"]
                            if domain_of(cid, by_id) == META_DOMAIN)
                if len(row["themes"]) < need:
                    for cid in chapters_out[c["num"]]["themes"]:
                        if cid in row["themes"]:
                            continue
                        if domain_of(cid, by_id) == META_DOMAIN and not allow_his and his_n >= 1:
                            continue
                        row["themes"].append(cid)
                        if domain_of(cid, by_id) == META_DOMAIN:
                            his_n += 1
                        if len(row["themes"]) >= need:
                            break
                if len(row["themes"]) < need:
                    for cid in vol_themes[v["name"]]:
                        if cid in row["themes"]:
                            continue
                        if domain_of(cid, by_id) == META_DOMAIN and not allow_his and his_n >= 1:
                            continue
                        row["themes"].append(cid)
                        if domain_of(cid, by_id) == META_DOMAIN:
                            his_n += 1
                        if len(row["themes"]) >= need:
                            break
                doms = []
                for cid in row["themes"]:
                    d = domain_of(cid, by_id)
                    if d and d not in doms:
                        doms.append(d)
                if not doms:
                    doms = chapters_out[c["num"]]["domains"][:3]
                if len(row["themes"]) < need:
                    for d in doms:
                        for cid in default_ids.get(d, []):
                            if cid not in row["themes"]:
                                row["themes"].append(cid)
                            if len(row["themes"]) >= need:
                                break
                        if len(row["themes"]) >= need:
                            break
                auto = []
                if not row["meta"] and len(row["themes"]) < MIN_T:
                    auto = auto_terms(s["slug"], row["themes"], banned, vocab_labels)
                    auto = auto[:MIN_T - len(row["themes"])]
                    row["auto"] = auto
                total = len(row["themes"]) + len(row.get("auto") or [])
                if total < need:
                    for cid in chapters_out[c["num"]]["themes"]:
                        if cid not in row["themes"]:
                            row["themes"].append(cid)
                        if len(row["themes"]) + len(row.get("auto") or []) >= need:
                            break
                row["themes"] = row["themes"][:(META_MAX if row["meta"] else MAX_T)]
                row["domains"] = doms[:3] or ([META_DOMAIN] if row["meta"] else [])

    # 小节差分
    delta = {}
    for v, c, s, x, _raw in sub_docs:
        own = sub_pick.get(x["key"], [])
        sec = sections_out[s["key"]]
        add = [cid for cid in own if cid not in sec["themes"]]
        own_p = extract_projects(x["title"], vocab)
        dp = [p for p in own_p if p not in sec["projects"]]
        own_t = extract_tech(x["title"], own, by_id)
        dt = [t for t in own_t if t not in sec["technical_terms"]]
        if add or dp or dt:
            row = {}
            if add:
                row["add"] = add
            if dp:
                row["projects"] = dp
            if dt:
                row["technical_terms"] = dt
            delta[x["key"]] = row

    generated = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    used = set()
    for row in sections_out.values():
        used.update(row["themes"])
        used.update(row["domains"])
    for row in delta.values():
        used.update(row.get("add") or [])
    kw_doc = {
        "meta": {
            "schema": SCHEMA_KW, "tree": "05-卷册大纲",
            "volumes": len(volumes), "chapters": len(chapters_out),
            "sections": len(sections_out), "subsections": len(sub_docs),
            "vocab_sha256": vocab_sha, "content_sha256": content_hash,
            "extract": "title+body", "generated_at": generated,
        },
        "themes": {cid: {"label": by_id[cid]["prefLabel"], "level": by_id[cid]["level"],
                         "broader": by_id[cid]["broader"],
                         "tech": list(by_id[cid].get("techTerms") or [])}
                   for cid in sorted(used)},
        "chapters": dict(sorted(chapters_out.items(), key=lambda kv: int(kv[0]))),
        "sections": dict(sorted(sections_out.items(), key=lambda kv: _sec_key(kv[0]))),
        "subsection_delta": dict(sorted(delta.items(), key=lambda kv: _sub_key(kv[0]))),
    }
    rev_doc = reverse_index(kw_doc, by_id, used)
    return kw_doc, rev_doc


def _default_meta(by_id):
    out = []
    for lab in ("编纂体例", "史料等级", "索引与元数据"):
        for cid, c in by_id.items():
            if c["prefLabel"] == lab:
                out.append(cid)
                break
    return out[:META_MAX]


def reverse_index(kw_doc, by_id, used):
    themes = {}
    for cid in sorted(used):
        c = by_id[cid]
        themes[cid] = {"label": c["prefLabel"], "broader": c["broader"],
                       "level": c["level"], "chapters": [], "sections": [],
                       "delta_subsections": []}
    for sid, row in kw_doc["sections"].items():
        for cid in row["themes"] + row["domains"]:
            themes[cid]["sections"].append(sid)
            themes[cid]["chapters"].append(row["chapter"])
    for sid, row in kw_doc["subsection_delta"].items():
        sec = sid.rsplit(".", 1)[0]
        ch = kw_doc["sections"][sec]["chapter"]
        for cid in row.get("add") or []:
            themes[cid]["chapters"].append(ch)
            themes[cid]["delta_subsections"].append(sid)
    for cid in themes:
        themes[cid]["chapters"] = sorted(set(themes[cid]["chapters"]))
        themes[cid]["sections"] = sorted(set(themes[cid]["sections"]), key=_sec_key)
        themes[cid]["delta_subsections"] = sorted(
            set(themes[cid]["delta_subsections"]), key=_sub_key)
    return {
        "meta": {"schema": SCHEMA_REV, "source": KW,
                 "source_sha256": "",
                 "subsection_policy": "sections+delta",
                 "generated_at": kw_doc["meta"]["generated_at"]},
        "themes": themes,
    }


# ---------------------------------------------------------------- 序列化与检查

def dumps(doc):
    return json.dumps(doc, ensure_ascii=False, indent=1) + "\n"


def dumps_rev(doc):
    return json.dumps(doc, ensure_ascii=False, indent=0) + "\n"


def strip_ts(doc):
    """幂等比较：只忽略 generated_at；source_sha256 属内容，须参与比较。"""
    d = copy.deepcopy(doc)
    d.get("meta", {}).pop("generated_at", None)
    return d


def load_disk(out_dir, name):
    p = os.path.join(out_dir, name)
    if not os.path.isfile(p):
        return None
    try:
        return json.loads(open(p, encoding="utf-8").read())
    except Exception as exc:
        raise Fatal("磁盘 %s 无法解析：%s" % (name, exc))


def check_all(out_dir=TREE, deep=False):
    problems = []
    kw = load_disk(out_dir, KW)
    rev = load_disk(out_dir, REV)
    if kw is None:
        problems.append("缺 %s" % KW)
    if rev is None:
        problems.append("缺 %s" % REV)
    if problems:
        return problems
    vocab, vsha = load_vocab()
    volumes = scan_tree(out_dir)
    vols, chs, secs, subs = tree_stats(volumes)
    meta = kw.get("meta") or {}
    if meta.get("schema") != SCHEMA_KW:
        problems.append("keywords schema 不符：%r" % meta.get("schema"))
    for k, v in (("volumes", vols), ("chapters", chs), ("sections", secs), ("subsections", subs)):
        if meta.get(k) != v:
            problems.append("meta.%s=%r，树实况 %d" % (k, meta.get(k), v))
    if meta.get("vocab_sha256") != vsha:
        problems.append("vocab_sha256 不符")
    csha = content_sha(volumes, out_dir)
    if meta.get("content_sha256") != csha:
        problems.append("content_sha256 不符（树内容已变）")
    disk_ch = set(kw.get("chapters") or {})
    tree_ch = {"%03d" % int(c["num"]) for v in volumes for c in v["chapters"]}
    if disk_ch != tree_ch:
        problems.append("章键不符：缺 %s／多 %s"
                        % (sorted(tree_ch - disk_ch)[:3], sorted(disk_ch - tree_ch)[:3]))
    disk_sec = set(kw.get("sections") or {})
    tree_sec = {s["key"] for v in volumes for c in v["chapters"] for s in c["sections"]}
    if disk_sec != tree_sec:
        problems.append("节键不符：缺 %s／多 %s"
                        % (sorted(tree_sec - disk_sec)[:3], sorted(disk_sec - tree_sec)[:3]))
    for v in volumes:
        for c in v["chapters"]:
            for s in c["sections"]:
                row = (kw.get("sections") or {}).get(s["key"]) or {}
                if row.get("title") != s["slug"]:
                    problems.append("节 %s 题面不符" % s["key"])
                    break
                if row.get("subs") != len(s["subs"]):
                    problems.append("节 %s 小节数不符" % s["key"])
                    break
                if row.get("subs_sha1") != subs_sha1(s):
                    problems.append("节 %s subs_sha1 不符" % s["key"])
                    break
    if rev.get("meta", {}).get("schema") != SCHEMA_REV:
        problems.append("theme_index schema 不符")
    if rev.get("meta", {}).get("source_sha256") != hashlib.sha256(
            dumps(kw).encode("utf-8")).hexdigest():
        problems.append("theme_index source_sha256 不符")
    used = set()
    for row in (kw.get("sections") or {}).values():
        used.update(row.get("themes") or [])
        used.update(row.get("domains") or [])
    for row in (kw.get("subsection_delta") or {}).values():
        used.update(row.get("add") or [])
    if set(rev.get("themes") or {}) != used:
        problems.append("反查主题集与 keywords 使用集不符")
    sec_by_theme = {}
    for sid, row in (kw.get("sections") or {}).items():
        for cid in (row.get("themes") or []) + (row.get("domains") or []):
            sec_by_theme.setdefault(cid, set()).add(sid)
    delta_by_theme = {}
    for sid, row in (kw.get("subsection_delta") or {}).items():
        for cid in row.get("add") or []:
            delta_by_theme.setdefault(cid, set()).add(sid)
    for cid, row in (rev.get("themes") or {}).items():
        if set(row.get("sections") or []) != sec_by_theme.get(cid, set()):
            problems.append("反查节集不符：%s" % cid)
        if set(row.get("delta_subsections") or []) != delta_by_theme.get(cid, set()):
            problems.append("反查差分小节集不符：%s" % cid)
    if deep:
        kw2, rev2 = build_docs(volumes, vocab, vsha, csha)
        rev2["meta"]["source_sha256"] = hashlib.sha256(
            dumps(kw).encode("utf-8")).hexdigest()
        if strip_ts(kw2) != strip_ts(kw):
            problems.append("deep：keywords 全量重算不一致")
        if strip_ts(rev2) != strip_ts(rev):
            problems.append("deep：theme_index 全量重算不一致")
    return problems


def write_all(out_dir=TREE, quiet=False):
    vocab, vsha = load_vocab()
    volumes = scan_tree(out_dir)
    csha = content_sha(volumes, out_dir)
    kw_new, rev_new = build_docs(volumes, vocab, vsha, csha)
    kw_disk = load_disk(out_dir, KW)
    rev_disk = load_disk(out_dir, REV)
    kw_changed = kw_disk is None or strip_ts(kw_new) != strip_ts(kw_disk)
    kw_final = kw_new if kw_changed else kw_disk
    kw_text = dumps(kw_final)
    rev_new["meta"]["source_sha256"] = hashlib.sha256(kw_text.encode("utf-8")).hexdigest()
    rev_changed = rev_disk is None or strip_ts(rev_new) != strip_ts(rev_disk)
    written = []
    if kw_changed:
        _atomic(os.path.join(out_dir, KW), kw_text)
        written.append(KW)
    if rev_changed:
        _atomic(os.path.join(out_dir, REV), dumps_rev(rev_new))
        written.append(REV)
    if not quiet:
        if written:
            print("[written] %s" % "、".join(written))
        else:
            print("[skip] 内容未变，不写盘")
    return written


def _atomic(path, text):
    tmp = path + ".tmp"
    write_text_lf(tmp, text)
    os.replace(tmp, path)


# ---------------------------------------------------------------- 统计与自检

def list_stats(out_dir=TREE):
    kw = load_disk(out_dir, KW)
    rev = load_disk(out_dir, REV)
    if not kw or not rev:
        print("缺派生件：先跑 --write")
        return 1
    meta = kw["meta"]
    themes = kw.get("themes") or {}
    sections = kw.get("sections") or {}
    delta = kw.get("subsection_delta") or {}
    counts = [len(r.get("themes") or []) + len(r.get("auto") or []) for r in sections.values()]
    share = {}
    for r in sections.values():
        for cid in r.get("themes") or []:
            share[cid] = share.get(cid, 0) + 1
    top = sorted(share.items(), key=lambda kv: (-kv[1], kv[0]))[:5]
    used = set(share) | {d for r in sections.values() for d in r.get("domains") or []}
    for r in delta.values():
        used.update(r.get("add") or [])
    unused = [cid for cid in themes if cid not in used]
    print("口径：卷 %d｜章 %d｜节 %d｜小节 %d"
          % (meta["volumes"], meta["chapters"], meta["sections"], meta["subsections"]))
    print("词表概念 %d｜使用 %d｜未用 %d" % (len(themes), len(used), len(unused)))
    print("节词数 min %d／max %d／均 %.2f"
          % (min(counts), max(counts), sum(counts) / max(len(counts), 1)))
    print("差分小节 %d（%.1f%%）" % (len(delta), 100.0 * len(delta) / max(meta["subsections"], 1)))
    print("单主题最大占比 %.1f%%（%s）"
          % (100.0 * top[0][1] / max(len(sections), 1),
             (themes.get(top[0][0]) or {}).get("label", top[0][0])))
    for cid, n in top:
        print("  %5.1f%%  %s" % (100.0 * n / max(len(sections), 1),
                                 (themes.get(cid) or {}).get("label", cid)))
    for name in (KW, REV):
        p = os.path.join(out_dir, name)
        if os.path.isfile(p):
            print("%s %.2f MB" % (name, os.path.getsize(p) / 1048576.0))
    return 0


def selftest():
    tmp = os.path.join(REPO, "script", "_theme_selftest")
    shutil.rmtree(tmp, ignore_errors=True)
    try:
        os.makedirs(os.path.join(tmp, "第01卷-测试卷", "第001章-卷总览", "001.0-章级综合"), exist_ok=True)
        os.makedirs(os.path.join(tmp, "第01卷-测试卷", "第002章-进程与文件系统", "002.1-进程管理"), exist_ok=True)
        os.makedirs(os.path.join(tmp, "第01卷-测试卷", "第003章-卷末书目述评", "003.0-章级综合"), exist_ok=True)
        _w(os.path.join(tmp, "第01卷-测试卷", "第001章-卷总览", "001.0-章级综合",
                        "001.0.1-卷级导言.md"), "# 001.0.1 卷级导言\n\n**要点**：史料等级与编纂体例说明。\n")
        _w(os.path.join(tmp, "第01卷-测试卷", "第002章-进程与文件系统", "002.1-进程管理",
                        "002.1.1-进程调度与fork.md"),
           "# 002.1.1 进程调度与fork\n\n**要点**：进程管理中的调度器与 fork 系统调用。\n")
        _w(os.path.join(tmp, "第01卷-测试卷", "第002章-进程与文件系统", "002.1-进程管理",
                        "002.1.2-ZFS快照.md"),
           "# 002.1.2 ZFS快照\n\n**要点**：ZFS 文件系统的写时复制与快照。\n")
        _w(os.path.join(tmp, "第01卷-测试卷", "第003章-卷末书目述评", "003.0-章级综合",
                        "003.0.1-书目述评.md"), "# 003.0.1 书目述评\n\n**要点**：文献综述与书目述评。\n")
        volumes = scan_tree(tmp)
        vols, chs, secs, subs = tree_stats(volumes)
        assert (vols, chs, secs, subs) == (1, 3, 3, 4), (vols, chs, secs, subs)
        assert "第01卷-测试卷" == volumes[0]["name"]
        vocab, vsha = load_vocab()
        kw, rev = build_docs(volumes, vocab, vsha, content_sha(volumes), tmp)
        assert kw["meta"]["schema"] == SCHEMA_KW
        assert len(kw["chapters"]) == 3 and len(kw["sections"]) == 3
        assert kw["sections"]["V01-C001-1.0"]["meta"] is True
        assert kw["sections"]["V01-C002-2.1"]["meta"] is False
        assert 3 <= len(kw["sections"]["V01-C002-2.1"]["themes"]) + len(kw["sections"]["V01-C002-2.1"].get("auto") or []) <= 6
        assert rev["themes"], "反查为空"
        # 负向：题面改字而计数不变
        p = os.path.join(tmp, "第01卷-测试卷", "第002章-进程与文件系统", "002.1-进程管理",
                         "002.1.1-进程调度与fork.md")
        _w(p, "# 002.1.1 进程调度与fork 改\n\n**要点**：进程管理中的调度器与 fork 系统调用。\n")
        volumes2 = scan_tree(tmp)
        kw2, _ = build_docs(volumes2, vocab, vsha, content_sha(volumes2), tmp)
        assert kw2["sections"]["V01-C002-2.1"]["subs_sha1"] != kw["sections"]["V01-C002-2.1"]["subs_sha1"]
        print("selftest: PASS（结构／元节／词数／反查／题面漂移均命中）")
        return 0
    except AssertionError as exc:
        import traceback
        traceback.print_exc()
        print("selftest: FAIL %s" % (exc,))
        return 1


def _w(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    write_text_lf(path, text)


def main():
    ap = argparse.ArgumentParser(description="大纲主题词索引生成器（theme-index/4）")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--deep", action="store_true")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--out", default=TREE)
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    if args.write:
        write_all(args.out)
        problems = check_all(args.out)
        if problems:
            print("写后复核 FAIL %d 项：" % len(problems))
            for p in problems[:20]:
                print("  " + p)
            return 1
        print("写后复核 PASS")
        return 0
    if args.list:
        return list_stats(args.out)
    problems = check_all(args.out, deep=args.deep)
    if problems:
        print("主题词索引校验 FAIL %d 项：" % len(problems))
        for p in problems[:40]:
            print("  " + p)
        return 1
    print("主题词索引校验 PASS（schema %s／%s%s）"
          % (SCHEMA_KW, SCHEMA_REV, "，deep" if args.deep else ""))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Fatal as exc:
        print("FATAL %s" % exc)
        sys.exit(2)
