# -*- coding: utf-8 -*-
"""fhk_b073 注册入库独立只读核验：四表计数 + 写后反查 + MAPJSON 重建。
带退避（他会话持锁是常态），只读，绝不写。"""
import io
import json
import os
import sys
import time

import duckdb

sys.stdout.reconfigure(encoding="utf-8")
HERE = r"D:\librebsd\script\_db_row_mining"
HC = r"d:\librebsd\04-现代研究文献\historical_claims.duckdb"
MAILDB = (r"d:\librebsd\03-原始史料库\11-邮件列表史料"
          r"\01-freebsd\db\freebsd-hackers.duckdb")
CAND = os.path.join(HERE, "review_logs", "fhk_b073_candidates.txt")
MAPJ = os.path.join(HERE, "review_logs", "fhk_b073_claim_map.json")
A = "fhk_b073"


def connect(db, ro, tries=240, sleep=10):
    last = None
    for i in range(1, tries + 1):
        try:
            return duckdb.connect(db, read_only=ro)
        except Exception as e:
            last = e
            if i % 6 == 0:
                print("  第 %d 次仍被占（%s）" % (i, str(e).splitlines()[0][:50]))
            time.sleep(sleep)
    raise SystemExit("连接失败：%s" % last)


cand = {}
for ln in io.open(CAND, encoding="utf-8"):
    ln = ln.strip()
    if ln:
        f = ln.split("|", 2)
        cand[f[0]] = f[1]

con = connect(HC, True)
n_ev = con.execute("SELECT COUNT(*) FROM evidence WHERE anchor=?", [A]).fetchone()[0]
n_join = con.execute(
    "SELECT COUNT(*) FROM claim_evidence ce JOIN claim c ON c.claim_id=ce.claim_id"
    " JOIN evidence e ON e.evidence_id=ce.evidence_id"
    " JOIN raw_source r ON r.source_id=e.source_id WHERE e.anchor=?", [A]
).fetchone()[0]
n_rs = con.execute(
    "SELECT COUNT(*) FROM raw_source WHERE source_db='freebsd-hackers'"
    " AND CAST(local_pk AS BIGINT) BETWEEN 2602441 AND 2604443"
).fetchone()[0]
print("evidence(anchor)=%d  四表join=%d  raw_source(pk范围)=%d  候选=%d"
      % (n_ev, n_join, n_rs, len(cand)))

rows = con.execute(
    "SELECT e.source_id, c.claim_id FROM evidence e"
    " JOIN claim_evidence ce ON ce.evidence_id=e.evidence_id"
    " JOIN claim c ON c.claim_id=ce.claim_id WHERE e.anchor=?", [A]
).fetchall()
con.close()
p2c = {}
for sid, clid in rows:
    p = sid.rsplit(".", 1)[-1]
    p2c[p] = clid
print("claim_map 可重建条数:", len(p2c))
print("候选未落库:", sorted(set(cand) - set(p2c), key=int)[:12])
print("落库多余(候选无):", sorted(set(p2c) - set(cand), key=int)[:12])
if p2c and not os.path.exists(MAPJ):
    with io.open(MAPJ, "w", encoding="utf-8", newline="\n") as fh:
        json.dump({k: {"claim_id": p2c[k]} for k in sorted(p2c, key=int)}, fh,
                  ensure_ascii=False, indent=0)
    print("已写 claim_map.json", len(p2c), "条")
if p2c:
    ks = sorted(p2c, key=int)
    print("首尾:", ks[0], p2c[ks[0]], "|", ks[-1], p2c[ks[-1]])
    seqs = sorted(int(v.split("-")[-1]) for v in p2c.values())
    print("claim seq %d..%d 连续=%s" % (seqs[0], seqs[-1],
          seqs == list(range(seqs[0], seqs[0] + len(seqs)))))
    lv = {}
    for k in p2c:
        lv[cand.get(k, "?")] = lv.get(cand.get(k, "?"), 0) + 1
    print("等级分布:", lv)
