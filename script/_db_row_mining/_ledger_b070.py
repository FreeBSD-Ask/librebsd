# -*- coding: utf-8 -*-
"""mail2d_read_ledger.json freebsd-hackers 138000→140000 入账（追加 fhk_b070）。

口径（沿用 _ledger_b053.py / _ledger_b054.py）：records 单条（lo=0，hi 左闭右开），
入账后 tags 70 条升序 fhk_b001..fhk_b070；
read_spec / read_judged / read_effective 三水位同步 140000；
updated 推进；note 追加记账一句并保留既有留痕。
输出格式：ensure_ascii=False，缩进取盘上原值（本轮实测 indent=1，见回环探测），
无 BOM／无 CRLF／末尾无换行。
台账只准外科补丁，禁全量重建。

记账事实（块数／等级分布／claim 号段）从 claims 库按 anchor='fhk_b070' 实测，
不硬编码，并把该句原文落到 review_logs/fhk_b070_ledger_append.txt 作为
_verify_ledger_b062.py 的独立比对基准。
"""
import datetime
import io
import json
import os

import duckdb

P = "//DESKTOP-M5P610N/d/librebsd/script/_db_row_mining/mail2d_read_ledger.json"
HC = r"d:\librebsd\04-现代研究文献\historical_claims.duckdb"
RL = os.path.dirname(os.path.abspath(__file__))
APPEND_OUT = os.path.join(RL, "review_logs", "fhk_b070_ledger_append.txt")
LIB = "freebsd-hackers"
OLD = 138000
NEW = 140000
TAG = "fhk_b070"
ANCHOR = "fhk_b070"
PK_LO, PK_HI = 2596416, 2598420
HOSTS = "88.5"

raw = io.open(P, "rb").read()
assert not raw.startswith(b"\xef\xbb\xbf"), "BOM"
assert b"\r\n" not in raw, "CRLF"
assert not raw.endswith(b"\n"), "尾换行"
d = json.loads(raw.decode("utf-8"))
# 回环校验：取能原样重建盘上文本的那种缩进。台账已被并发写手改成 indent=1
# （updated 停在 17:00），b062 脚本硬编 indent=2 在本轮直接断言失败。
# 读写必须同缩进，否则制造 ~12KB 纯缩进 diff 噪音。
IND = None
for _i in (1, 2, 4):
    if json.dumps(d, ensure_ascii=False, indent=_i) == raw.decode("utf-8"):
        IND = _i
        break
assert IND is not None, "台账缩进无法回环（indent 1/2/4 均不匹配盘上格式）"
print("[格式] 盘上缩进 indent=%d（回环通过）" % IND)

t = d["items"][LIB]
assert (t["read_spec"] == OLD and t["read_judged"] == OLD
        and t["read_effective"] == OLD), (t["read_spec"], t["read_judged"])
rec = t["records"][0]
assert rec["lo"] == 0 and rec["hi"] == OLD, (rec["lo"], rec["hi"])
tags = rec["tags"]
assert len(tags) == 69 and tags[-1] == "fhk_b069", (len(tags), tags[-1])
assert tags == ["fhk_b%03d" % i for i in range(1, 70)], "tags 序列不符"
n_items, n_recs = len(d["items"]), len(rec["tags"])
assert n_recs == 69, "tags 应为 69 条，实测 %d" % n_recs
print("[前置] 三水位=%d records[0].hi=%d tags=%d 最后=%s"
      % (t["read_judged"], rec["hi"], len(tags), tags[-1]))

# ---- 记账事实从 claims 库实测，不硬编码 ----
import time as _t
con = None
for _i in range(1, 241):
    try:
        con = duckdb.connect(HC, read_only=True)
        break
    except Exception as _e:
        print("  第 %d 次连接被占（%s），15s 后重试"
              % (_i, str(_e).splitlines()[0][:56]), flush=True)
        _t.sleep(15)
else:
    raise SystemExit("连接失败")
try:
    n = con.execute(
        "SELECT COUNT(*) FROM claim c JOIN claim_evidence ce ON ce.claim_id=c.claim_id"
        " JOIN evidence e ON e.evidence_id=ce.evidence_id"
        " JOIN raw_source r ON r.source_id=e.source_id WHERE e.anchor=? AND c.status='supported'",
        [ANCHOR]).fetchone()[0]
    lvl = con.execute(
        "SELECT c.evidence_level, COUNT(*) FROM claim c JOIN claim_evidence ce"
        " ON ce.claim_id=c.claim_id JOIN evidence e ON e.evidence_id=ce.evidence_id"
        " WHERE e.anchor=? AND c.status='supported' GROUP BY c.evidence_level",
        [ANCHOR]).fetchall()
    l4 = dict(lvl).get("L4", 0)
    l3 = dict(lvl).get("L3", 0)
    lo = con.execute(
        "SELECT MIN(CAST(SUBSTR(c.claim_id,7) AS INTEGER)) FROM claim c"
        " JOIN claim_evidence ce ON ce.claim_id=c.claim_id"
        " JOIN evidence e ON e.evidence_id=ce.evidence_id WHERE e.anchor=?",
        [ANCHOR]).fetchone()[0]
    hi = con.execute(
        "SELECT MAX(CAST(SUBSTR(c.claim_id,7) AS INTEGER)) FROM claim c"
        " JOIN claim_evidence ce ON ce.claim_id=c.claim_id"
        " JOIN evidence e ON e.evidence_id=ce.evidence_id WHERE e.anchor=?",
        [ANCHOR]).fetchone()[0]
    cont = con.execute(
        "SELECT COUNT(*) FROM claim c JOIN claim_evidence ce ON ce.claim_id=c.claim_id"
        " JOIN evidence e ON e.evidence_id=ce.evidence_id WHERE e.anchor=?",
        [ANCHOR]).fetchone()[0]
    orph = con.execute(
        "SELECT COUNT(*) FROM claim_evidence ce LEFT JOIN evidence e ON e.evidence_id=ce.evidence_id"
        " WHERE e.evidence_id IS NULL").fetchone()[0]
finally:
    con.close()
assert n == l3 + l4, "等级分布合计 %d != 块数 %d" % (l3 + l4, n)
assert hi - lo + 1 == cont == n, "claim 号段不连续 %d..%d 共 %d 但 supported %d" % (lo, hi, cont, n)
print("[实测] 块 %d（L4=%d／L3=%d）claim CL-RM-%d~%d（连续 %d）悬挂 %d"
      % (n, l4, l3, lo, hi, cont, orph))

APPEND = ("本次追加：freebsd-hackers %s（offset %d，pk %d–%d，"
          "%d 块入 1 宿主 %s=%d，claim CL-RM-%d~%d 连续，L4=%d／L3=%d），"
          "%d→%d，tags %d→%d 条。｜" % (
              TAG, OLD, PK_LO, PK_HI, n, HOSTS, n, lo, hi, l4, l3,
              OLD, NEW, n_recs, n_recs + 1))
io.open(APPEND_OUT, "w", encoding="utf-8", newline="\n").write(APPEND)
print("[记账句] %s" % APPEND)

# 台账外事实核验：候选件行数须与库内块数一致
cand_f = os.path.join(RL, "review_logs", "fhk_b070_candidates.txt")
cand = sum(1 for l in io.open(cand_f, encoding="utf-8") if l.strip())
assert cand == n, "候选件 %d != 库内块 %d" % (cand, n)
print("[对账] 候选件 %d == 库内 %d" % (cand, n))

for f in ("read_spec", "read_judged", "read_effective"):
    t[f] = NEW
rec["hi"] = NEW
rec["tags"] = list(tags) + [TAG]

d["updated"] = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")
d["note"] = d["note"] + APPEND

out = json.dumps(d, ensure_ascii=False, indent=IND)
assert "\r" not in out
assert json.loads(out) == d
io.open(P, "w", encoding="utf-8", newline="\n").write(out)
back = io.open(P, "rb").read()
assert not back.startswith(b"\xef\xbb\xbf") and b"\r\n" not in back
assert not back.endswith(b"\n"), "写后尾换行"
assert back == out.encode("utf-8"), "回读失配"
assert json.loads(back.decode("utf-8")) == d, "round-trip 不等"
print("[写盘] bytes=%d" % len(back))
print("[台账] %s hi=%d tags=%d 三水位=%d"
      % (LIB, rec["hi"], len(rec["tags"]), t["read_judged"]))
cov = t["read_judged"] * 100.0 / t["messages"]
print("[INFO] 覆盖率 %d/%d = %.2f%%  剩余 %d 封"
      % (t["read_judged"], t["messages"], cov, t["messages"] - t["read_judged"]))
