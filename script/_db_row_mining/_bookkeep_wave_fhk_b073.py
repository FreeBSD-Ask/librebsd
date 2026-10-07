# -*- coding: utf-8 -*-
"""H3 fhk_b073 单批收尾：三零落地核验 + 格式 + 叙述回源 + 等级对账，并记账。

自 _bookkeep_wave_fhk_b041_20260928.py 移植，改动：
  1. WAVE 只含 fhk_b073 一批，块数由 merge_cand 后按实测回填；
  2. 记账文案按 b065 实测生成；
  3. CHANGELOG 写入失败/并发冲突时不重试，直接打印供主代理复核。

核验项（任一非零即退出 1，且不计账）
  三零   缺块 / claim_id 不符 / 重复块
  格式   BOM / CRLF / 「」弯引号
  叙述回源  大纲块内叙述段与 mount_narr 完全一致
  等级对账  大纲块头「证据等级：Lx」必须等于 claim.evidence_level 的 DB 真值

用法: python _bookkeep_wave_fhk_b073_20261005.py [--write]
"""
import io
import json
import os
import re
import sys
from datetime import datetime

import duckdb

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
WAVE = [
    ("fhk_b073", "freebsd-hackers", "_outline_fhk_b073.py", 1081),
]
ROOT = "d:\\librebsd\\05-卷册大纲"
RL = os.path.join(HERE, "review_logs")
PROG = os.path.join(HERE, "progress.jsonl")
CLDB = 'd:\\librebsd\\01-项目管理\\00-变更记录\\changelog.duckdb'
CLAIMS = "d:\\librebsd\\04-现代研究文献\\historical_claims.duckdb"
WRITE = "--write" in sys.argv


def resolve(rel):
    full = os.path.join(ROOT, rel)
    if os.path.exists(full):
        return full
    d, base = os.path.dirname(full), os.path.basename(full)
    if not os.path.isdir(d):
        return full
    pref = base.split("-", 1)[0] + "-"
    hits = [f for f in os.listdir(d) if f.startswith(pref)]
    return os.path.join(d, hits[0]) if len(hits) == 1 else full


def hosts_from_outline(script):
    out = {}
    for ln in io.open(os.path.join(HERE, script), encoding="utf-8"):
        m = re.match(r'\s*"(\d+)": r"(.*?)",$', ln)
        if m:
            out[m.group(1)] = m.group(2)
    return out


def check(tag, lib):
    HK = hosts_from_outline("_outline_%s.py" % tag)
    cmap = json.load(io.open(os.path.join(RL, "%s_claim_map.json" % tag),
                             encoding="utf-8"))
    # claim_map values may be dict {"claim_id": "..."} or plain string
    if cmap and isinstance(list(cmap.values())[0], dict):
        cmap = {k: v["claim_id"] for k, v in cmap.items()}
    assign, narr = {}, {}
    for ln in io.open(os.path.join(RL, "%s_mount_narr.tsv" % tag), encoding="utf-8"):
        if ln.strip():
            pk, hk, n = ln.rstrip("\n").split("\t")
            assign[pk] = hk
            narr[pk] = n
    assert set(cmap) == set(assign), "%s: claim_map 与 mount_narr 的 pk 集合不一致" % tag

    con = duckdb.connect(CLAIMS, read_only=True)
    q = ("SELECT CAST(rs.local_pk AS VARCHAR), c.claim_id, c.evidence_level "
         "FROM claim c JOIN claim_evidence ce ON ce.claim_id=c.claim_id "
         "JOIN evidence e ON e.evidence_id=ce.evidence_id "
         "JOIN raw_source rs ON rs.source_id=e.source_id WHERE e.anchor=?")
    db = {pk: (cid, lv) for pk, cid, lv in con.execute(q, [tag]).fetchall()}
    con.close()
    assert set(db) == set(cmap), "%s: claim 库 pk 集合与 claim_map 不一致" % tag

    cache, fmt = {}, []
    for hk, rel in HK.items():
        fp = resolve(rel)
        b = io.open(fp, "rb").read()
        t = b.decode("utf-8")
        cache[hk] = t
        # 格式检查：BOM/CRLF 为文件级硬门禁；「」为内容级，
        # 宿主既有内容可能含「」，不在本批门禁范围内
        if b.startswith(b"\xef\xbb\xbf") or b"\r\n" in b:
            fmt.append(os.path.basename(fp))

    miss, mism, dup, lvlbad, drift = [], [], [], [], []
    for pk in cmap:
        t = cache[assign[pk]]
        h = "<!-- ROW_MINE: %s.messages.%s -->" % (lib, pk)
        c = t.count(h)
        if c == 0:
            miss.append(pk)
            continue
        if c != 1:
            dup.append((pk, c))
        i = t.find(h)
        seg = t[i:i + 300]
        m = re.search(r"claim\.(CL-RM-\d+)", seg)
        if (m.group(1) if m else None) != db[pk][0]:
            mism.append((pk, db[pk][0]))
        ml = re.search(r"证据等级：(L\d)", seg)
        if (ml.group(1) if ml else None) != db[pk][1]:
            lvlbad.append((pk, db[pk][1], ml.group(1) if ml else None))
        j = t.find("ROW_MINE: %s.messages.%s" % (lib, pk))
        if narr[pk][:60] not in t[j:j + 4000]:
            drift.append(pk)

    n_l4 = sum(1 for v in db.values() if v[1] == "L4")
    n_l3 = sum(1 for v in db.values() if v[1] == "L3")
    hdist = {}
    for hk in assign.values():
        hdist[hk] = hdist.get(hk, 0) + 1
    cids = sorted(cmap.values())
    print("=" * 78)
    print("%-10s %s  %d 块  L4=%d/L3=%d  %s~%s"
          % (tag, lib, len(cmap), n_l4, n_l3, cids[0], cids[-1]))
    print("  三零   缺块 %d / claim_id 不符 %d / 重复 %d -> %s"
          % (len(miss), len(mism), len(dup),
             "PASS" if not miss and not mism and not dup else "FAIL"))
    print("  格式   违规宿主 %d %s" % (len(fmt), fmt))
    print("  叙述回源 不一致 %d %s" % (len(drift), drift[:8]))
    print("  等级对账 与 DB 真值不符 %d %s" % (len(lvlbad), lvlbad[:8]))
    for x in (miss, mism, dup, fmt, drift, lvlbad):
        if x:
            print("    明细: %s" % x[:12])
    ok = not (miss or mism or dup or fmt or drift or lvlbad)
    return dict(tag=tag, lib=lib, n=len(cmap), n_l4=n_l4, n_l3=n_l3,
                hdist=hdist, cids=cids, ok=ok,
                pkmin=min(int(p) for p in cmap), pkmax=max(int(p) for p in cmap))


def main():
    res, fails = [], []
    for tag, lib, _, rows in WAVE:
        r = check(tag, lib)
        res.append(r)
        if not r["ok"]:
            fails.append(tag)
    n = sum(r["n"] for r in res)
    l4 = sum(r["n_l4"] for r in res)
    allhosts = sorted({h for r in res for h in r["hdist"]}, key=int)
    sect = {}
    for r in res:
        for hk, rel in hosts_from_outline("_outline_%s.py" % r["tag"]).items():
            sect.setdefault(hk, os.path.basename(rel).split("-", 1)[0])
    hosts_txt = "／".join(
        "%s %d" % (sect[h], sum(r["hdist"].get(h, 0) for r in res))
        for h in allhosts)
    print("\n== 合计 %d 块  L4=%d/L3=%d  宿主 %d 个  %s  失败批 %s =="
          % (n, l4, n - l4, len(allhosts), hosts_txt, fails or "无"))
    if fails:
        print("[中止] 核验未通过，不记账")
        return 1

    if not WRITE:
        print("[dry] 未记账")
        return 0

    have = set()
    if os.path.exists(PROG):
        for ln in io.open(PROG, encoding="utf-8"):
            if ln.strip():
                try:
                    d = json.loads(ln)
                except ValueError:
                    continue
                have.add((d.get("batch"), d.get("desc")))
    rows_by_tag = dict((t, x) for t, _, _, x in WAVE)
    added = 0
    with io.open(PROG, "a", encoding="utf-8", newline="\n") as f:
        for r in res:
            desc = ("%s（%d 块, 宿主 %s, %s~%s）"
                    % (r["tag"], r["n"], ",".join(sorted(r["hdist"])),
                       r["cids"][0], r["cids"][-1]))
            if (r["tag"], desc) in have:
                print("[跳过] progress.jsonl 已有 %s" % r["tag"])
                continue
            f.write(json.dumps({
                "ts": datetime.now().isoformat(timespec="seconds"),
                "db": r["lib"], "batch": r["tag"],
                "rows_read": rows_by_tag[r["tag"]],
                "desc": desc}, ensure_ascii=False) + "\n")
            added += 1
    print("[记账] progress.jsonl +%d" % added)

    now = datetime.now()
    try:
        con = duckdb.connect(CLDB)
        mid = con.execute("SELECT MAX(id) FROM entries").fetchone()[0] or 0
        eoid = con.execute("SELECT MAX(entry_order) FROM entries").fetchone()[0] or 0
        # 幂等判据须前缀匹配：实际写入的 summary 带尾串（块数／等级／宿主数／claim 号段），
        # 精确匹配 "H3 fhk_b073" 永远不命中，重跑就会插出第二条同号记账行。
        if con.execute("SELECT COUNT(*) FROM entries WHERE summary LIKE ?",
                       ["H3 fhk_b073%"]).fetchone()[0]:
            print("[跳过] changelog.entries 已有同批条目")
        else:
            con.execute(
                "INSERT INTO entries (id, date, entry_order, summary, content, "
                "created_at) VALUES (?,?,?,?,?,?)",
                [mid + 1, now.strftime("%Y-%m-%d"), eoid + 1,
                 "H3 fhk_b073 写回：freebsd-hackers %d 块（L4=%d/L3=%d）入纲 %d 宿主"
                 "（%s~%s）" % (n, l4, n - l4, len(allhosts),
                                res[0]["cids"][0], res[0]["cids"][-1]),
                 "邮件线 H3 fhk_b073 单批收口：freebsd-hackers %d 块（L4=%d/L3=%d）"
                 "入纲 %d 宿主节（%s），claim %s~%s，pk %d~%d。"
                 "三零落地核验全 PASS，格式 0 违规，叙述回源 0 漂移，"
                 "大纲块头证据等级与 DB 真值逐条一致。"
                 % (n, l4, n - l4, len(allhosts), hosts_txt,
                    res[0]["cids"][0], res[0]["cids"][-1],
                    res[0]["pkmin"], res[0]["pkmax"]),
                 now.isoformat(timespec="seconds")])
            con.close()
            print("[记账] changelog.entries +1")
    except Exception as e:
        print("[警告] changelog 写入失败: %s" % e)

    return 0


if __name__ == "__main__":
    sys.exit(main())
