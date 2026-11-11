# -*- coding: utf-8 -*-
"""Task 8.2 · G1-S1：V01–V10 四库交叉复核，产出逐卷「库内可用未用」清单。

输入（真值）：
- 缺口题：映射/design/exceptions/V{01..10}.tsv 中 status=open 的 corpus_gap 行
- 题面：映射/title-design/V{NN}.tsv（title＋thesis）
- 已认领：映射/design/supplement/V{NN}.tsv（status=claimed → 本清单标注，不重复推）
语料（四库）：
- references_fulltext：key_facts / summaries / references（题名）
- historical_claims：claim（SQL 侧 bigram AND/OR 检索）
- 释疑库：doubts_standalone.doubts_to_resolve（open 行）
- sacred_sources：blocks

产出：映射/parallel/content/V{NN}/s1-库内交叉复核.tsv
列：subsection_id / title / source / object_id / ref_id / score / snippet / 状态
只读四库，不写库。
"""
import csv
import math
import os
import re
import sys
from collections import defaultdict

import duckdb

ROOT = r"D:\librebsd"
MAP = os.path.join(ROOT, "05-卷册大纲", "映射")
OUTBASE = os.path.join(MAP, "parallel", "content")
FT = os.path.join(ROOT, "04-现代研究文献", "05-参考文献全文数据库", "references_fulltext.duckdb")
HC = os.path.join(ROOT, "04-现代研究文献", "historical_claims.duckdb")
DBT = os.path.join(ROOT, "04-现代研究文献", "06-存疑数据库", "doubts_standalone.duckdb")
SS = os.path.join(ROOT, "02-sacred源材料", "sacred_sources.duckdb")

CJK = re.compile(r"[\u4e00-\u9fff]")
STOP = set("的了和与及是在对为以等这那其有也无之而就都也很将把被从到由即如若则并且或")
SCORE_MIN = 0.22
TOP_PER_SRC = 3
CLAIMS_TOP = 2
USE = {
    "fulltext_fact": "全文补证候选（S1 命中即复用，D1 型）",
    "fulltext_summary": "全文综述候选（D1 型，核对原文后落块）",
    "ref_title": "文献线索（须核全文再定 D1/D2）",
    "doubt_open": "释疑并案（先并到存疑库现有条目）",
    "sacred": "史观参照（不作证据，仅定题面归属）",
    "claim": "claim 复用（S2 先库后网）",
}


def bigrams(s):
    s = "".join(CJK.findall(s or ""))
    return [s[i:i + 2] for i in range(len(s) - 1) if s[i] not in STOP or s[i + 1] not in STOP]


def load_targets(vols):
    """返回 {subsection_id: {'title','thesis','vol'}}，仅 open 缺口题。"""
    tgt = {}
    for v in vols:
        vn = "V%02d" % v
        titles = {}
        p = os.path.join(MAP, "title-design", vn + ".tsv")
        with open(p, encoding="utf-8-sig", newline="") as f:
            for r in csv.DictReader(f, delimiter="\t"):
                titles[r["subsection_id"]] = (r.get("title", ""), r.get("thesis", ""))
        p = os.path.join(MAP, "design", "exceptions", vn + ".tsv")
        with open(p, encoding="utf-8-sig", newline="") as f:
            for r in csv.DictReader(f, delimiter="\t"):
                if r["status"] != "open":
                    continue
                sid = r["subsection_id"]
                t, th = titles.get(sid, ("", ""))
                tgt[sid] = {"title": t, "thesis": th, "vol": vn, "reason": r.get("reason", "")}
    return tgt


def load_claimed(vols):
    """已认领/已补证题集合（supplement 台账任一状态即跳过推送）。"""
    done = {}
    for v in vols:
        vn = "V%02d" % v
        p = os.path.join(MAP, "design", "supplement", vn + ".tsv")
        if not os.path.exists(p):
            continue
        with open(p, encoding="utf-8-sig", newline="") as f:
            for r in csv.DictReader(f, delimiter="\t"):
                done[r["subsection_id"]] = r.get("status", "")
    return done


def build_corpus():
    """返回 docs 列表 [(source, object_id, ref_id, text)]"""
    docs = []
    con = duckdb.connect(FT, read_only=True)
    for oid, rid, txt, cat in con.execute(
            "SELECT id, reference_id, fact_text, fact_category FROM key_facts").fetchall():
        docs.append(("fulltext_fact", oid, rid, txt or ""))
    for rid, sm, kw in con.execute(
            "SELECT reference_id, summary, topic_keywords FROM summaries").fetchall():
        docs.append(("fulltext_summary", rid, rid, (sm or "") + " " + (kw or "")))
    for rid, ti, au, yr in con.execute(
            'SELECT id, title, author, year FROM "references"').fetchall():
        docs.append(("ref_title", rid, rid, " ".join([ti or "", au or "", yr or ""])))
    con.close()
    con = duckdb.connect(DBT, read_only=True)
    for did, dt, kw in con.execute(
            "SELECT id, doubt_text, doubt_keywords FROM doubts_to_resolve WHERE resolution_status='open'").fetchall():
        docs.append(("doubt_open", did, "", (dt or "") + " " + (kw or "")))
    con.close()
    con = duckdb.connect(SS, read_only=True)
    for bid, txt in con.execute("SELECT id, block_content FROM blocks").fetchall():
        docs.append(("sacred", bid, "", txt or ""))
    con.close()
    return docs


def index_corpus(docs):
    post = defaultdict(list)   # bigram -> [doc_idx]
    doc_bg = []
    for i, (_, _, _, text) in enumerate(docs):
        bgs = set(bigrams(text))
        doc_bg.append(bgs)
        for b in bgs:
            post[b].append(i)
    n = len(docs)
    idf = {b: math.log((n + 1) / (len(v) + 0.5)) for b, v in post.items()}
    doc_norm = [math.sqrt(sum(idf[b] ** 2 for b in bgs)) or 1.0 for bgs in doc_bg]
    return post, doc_bg, idf, n, doc_norm


def score_docs(bgs, post, doc_bg, idf, n, doc_norm):
    """标准 IDF 加权余弦：score = Σ(idf_q·idf_d) / (||q||·||d||)。返回 {doc_idx: score}"""
    sc = defaultdict(float)
    uniq = set(bgs)
    if not uniq:
        return sc
    qn = 0.0
    for b in uniq:
        w = idf.get(b)
        if w is None or w < 1.0:      # 过泛（出现在多数文档）不计
            continue
        qn += w * w
        for i in post[b]:
            sc[i] += w * w
    qn = math.sqrt(qn) or 1.0
    out = {}
    for i, s in sc.items():
        out[i] = s / (qn * doc_norm[i])
    return out


def lcs_len(a, b):
    """最长公共子串长度（仅 CJK 序列），精度闸用。"""
    a = "".join(CJK.findall(a or ""))
    b = "".join(CJK.findall(b or ""))
    if not a or not b:
        return 0
    prev = [0] * (len(b) + 1)
    best = 0
    for i in range(1, len(a) + 1):
        cur = [0] * (len(b) + 1)
        ai = a[i - 1]
        for j in range(1, len(b) + 1):
            if ai == b[j - 1]:
                cur[j] = prev[j - 1] + 1
                if cur[j] > best:
                    best = cur[j]
        prev = cur
    return best


def claim_hits(con, bgs, title, limit=80):
    """claims 侧：LIKE 粗召回 → 精度闸（LCS≥5 汉字 或 命中占比≥0.75）。"""
    picked = [b for b in dict.fromkeys(bgs)][:5]
    if not picked:
        return []
    conds, params = [], []
    for b in picked:
        conds.append("claim_text LIKE ?")
        params.append("%" + b + "%")
    sql = ("SELECT claim_id, claim_text, evidence_level FROM claim WHERE ("
           + " OR ".join(conds) + ") LIMIT %d" % limit)
    rows = con.execute(sql, params).fetchall()
    scored = []
    for cid, txt, lv in rows:
        hit = sum(1 for b in picked if b in (txt or ""))
        frac = hit / len(picked)
        lc = lcs_len(title, txt)
        if frac >= 0.75 or lc >= 5:
            scored.append((round(frac + 0.1 * min(lc, 10), 3), cid, txt, lv))
    scored.sort(reverse=True)
    return scored[:CLAIMS_TOP]


def main():
    vols = list(range(1, 11))
    if len(sys.argv) > 1:
        vols = [int(x) for x in sys.argv[1:]]
    tgt = load_targets(vols)
    claimed = load_claimed(vols)
    print("open 缺口题:", len(tgt), "｜已认领/已补证:", sum(1 for s in tgt if s in claimed))
    docs = build_corpus()
    print("语料:", len(docs), "文档")
    post, doc_bg, idf, n, doc_norm = index_corpus(docs)
    print("bigram 索引:", len(post), "键")

    con = duckdb.connect(HC, read_only=True)
    by_vol = defaultdict(list)
    for i, (sid, info) in enumerate(sorted(tgt.items())):
        status = "已认领(" + claimed[sid] + ")" if sid in claimed else "可推"
        bgs = bigrams(info["title"] + " " + info["thesis"])
        sc = score_docs(bgs, post, doc_bg, idf, n, doc_norm)
        top = sorted(sc.items(), key=lambda kv: -kv[1])[:TOP_PER_SRC * 3]
        per_src = defaultdict(int)
        for di, s in top:
            if s < SCORE_MIN:
                continue
            src, oid, rid, text = docs[di]
            if per_src[src] >= TOP_PER_SRC:
                continue
            per_src[src] += 1
            lc = lcs_len(info["title"], text)
            tier = "A" if lc >= 6 else ("B" if s >= 0.30 else "C")
            by_vol[info["vol"]].append([sid, info["title"], src, oid, rid,
                                        "%.3f" % s, tier, re.sub(r"\s+", " ", text)[:120], status,
                                        USE.get(src, "")])
        if status == "可推":
            for s, cid, txt, lv in claim_hits(con, bgs, info["title"]):
                lc = lcs_len(info["title"], txt)
                by_vol[info["vol"]].append([sid, info["title"], "claim", cid, "", "%.2f" % s,
                                            "A" if lc >= 5 else "B",
                                            re.sub(r"\s+", " ", txt or "")[:120], status,
                                            USE["claim"]])
        if (i + 1) % 100 == 0:
            print("  ..%d/%d" % (i + 1, len(tgt)), flush=True)
    con.close()

    HDR = ["subsection_id", "title", "source", "object_id", "ref_id", "score", "quality", "snippet", "status", "拟用途"]
    for vn, rows in sorted(by_vol.items()):
        d = os.path.join(OUTBASE, vn)
        os.makedirs(d, exist_ok=True)
        p = os.path.join(d, "s1-库内交叉复核.tsv")
        with open(p, "w", encoding="utf-8", newline="") as f:
            f.write("\t".join(HDR) + "\n")
            for r in rows:
                f.write("\t".join(str(x).replace("\t", " ") for x in r) + "\n")
        uniq = len({r[0] for r in rows})
        print("WROTE", p, "rows=", len(rows), "覆盖题=", uniq)

    # 覆盖率统计
    cov = defaultdict(set)
    for vn, rows in by_vol.items():
        for r in rows:
            cov[vn].add(r[0])
    tot = 0
    for vn in sorted(cov):
        n_open = sum(1 for s, i in tgt.items() if i["vol"] == vn)
        print("  %s 有候选 %d/%d 题" % (vn, len(cov[vn]), n_open))
        tot += len(cov[vn])
    print("合计有候选 %d/%d 题（%.1f%%）" % (tot, len(tgt), 100.0 * tot / max(1, len(tgt))))


main()
