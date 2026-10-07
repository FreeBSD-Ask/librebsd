# -*- coding: utf-8 -*-
"""freebsd-hackers fhk_b071（库内序 140001-142000，pk 2598421-2600431）候选落库。

契约（对齐 _register_fhk_b054.py，逐字沿用，勿改口径）：
- 源库只读；source_db='freebsd-hackers'；source_id='SRC-rowmine:freebsd-hackers.messages.<id>'。
- 引文取 body 前 300 字符原样同串（按行/空格边界回退截断），写前复核同串、写后反查命中。
- 单事务 BEGIN/COMMIT，崩溃即 ROLLBACK，禁止部分提交。
- 幂等双去重：source_id + content_hash（sha256(source_id|quote)）。
- CL-RM 续库内 MAX+1（注册时实测，抗并行占号）。
- 四表写入：raw_source / evidence / claim / claim_evidence。
- 词表：role=supporting；strength L4/L3=strong；confidence L4/L3=0.85；
  wording_gate L4/L3=attribution_allowed。
- ANCHOR='fhk_b071'。候选文件为 3 字段（pk|level|summary），date/from 一律以源库为准。
- 按表 executemany（b050/b053/b054 实测比逐条快约 10 倍），claim_evidence 的 MAX(id)+1
  hoist 出循环（该表无 AUTOINCREMENT，循环内重取 MAX 每轮全表扫描）。

用法: C:/Python314/python.exe _register_fhk_b071.py [--apply]
"""
import hashlib
import io
import os
import sys
from datetime import datetime

import duckdb

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
CAND = os.path.join(HERE, "review_logs", "fhk_b071_candidates.txt")
HC = r"d:\librebsd\04-现代研究文献\historical_claims.duckdb"
MAILDB = r"d:\librebsd\03-原始史料库\11-邮件列表史料\01-freebsd\db\freebsd-hackers.duckdb"
ANCHOR = "fhk_b071"
SRCDB = "freebsd-hackers"
NOW = datetime.now().isoformat(timespec="seconds")
QUOTE_LIMIT = 300
mode = "--apply" if "--apply" in sys.argv else "--dry-run"


def sha(s):
    return hashlib.sha256(str(s).encode("utf-8")).hexdigest()


def make_quote(body):
    body = (body or "").strip()
    if len(body) <= QUOTE_LIMIT:
        return body
    cut = body[:QUOTE_LIMIT]
    i = cut.rfind("\n")
    if i > 120:
        return cut[:i]
    j = cut.rfind(" ")
    if j > 120:
        return cut[:j]
    return cut


cands = []
for ln in io.open(CAND, encoding="utf-8"):
    ln = ln.strip()
    if not ln or ln.startswith("#"):
        continue
    p = ln.split("|", 2)
    if len(p) != 3 or not p[0].isdigit() or p[1] not in ("L4", "L3", "L2", "L1"):
        raise SystemExit("契约异常行: %s" % ln[:60])
    cands.append((int(p[0]), p[1], p[2]))
print("候选条数:", len(cands))
assert len({c[0] for c in cands}) == len(cands), "pk 重复"

mail = duckdb.connect(MAILDB, read_only=True)
_pks = [str(c[0]) for c in cands]
_q = ("SELECT CAST(id AS BIGINT), subject, body, date, from_name FROM messages "
      "WHERE CAST(id AS BIGINT) IN (%s)" % ",".join("?" for _ in _pks))
data = {}
for _id, _subj, _body, _date, _frm in mail.execute(_q, _pks).fetchall():
    _s = (_subj or "").strip()
    _b = (_body or "").strip()
    data[int(_id)] = (_subj or "", _b if _b else _s, _date or "", _frm or "")
mail.close()
miss = [c[0] for c in cands if c[0] not in data]
if miss:
    raise SystemExit("源行缺失: %s" % miss[:10])

bad = [pk for pk, _, _ in cands if not make_quote(data[pk][1])
       or make_quote(data[pk][1]) not in data[pk][1]]
print("引文同串失败:", bad if bad else "无")
if bad:
    raise SystemExit("引文同串失败，终止: %s" % bad)


def connect_retry(read_only, tries=280, sleep=15):
    """claim 库同一时刻只容一个写者，且 Windows 独占锁会连只读连接一起挡住。

    别抢、别杀持有者，只在 connect 阶段退避重试；本脚本幂等
    （source_id + content_hash 双去重），中断后整脚本重跑安全。
    """
    import time
    last = None
    for i in range(1, tries + 1):
        try:
            return duckdb.connect(HC, read_only=read_only)
        except Exception as e:
            last = e
            print("  [退避] 第 %d/%d 次连接被占（%s），%ds 后重试"
                  % (i, tries, str(e).splitlines()[0][:70], sleep))
            time.sleep(sleep)
    raise SystemExit("claim 库连接失败 %d 次：%s" % (tries, last))


con = connect_retry(mode == "--dry-run")
existing_hash = {r[0] for r in con.execute(
    "SELECT content_hash FROM raw_source WHERE content_hash IS NOT NULL").fetchall()}
existing_src = {r[0] for r in con.execute(
    "SELECT source_id FROM raw_source WHERE source_db=?", [SRCDB]).fetchall()}
mx = con.execute("SELECT MAX(CAST(SUBSTR(claim_id,7) AS INTEGER)) FROM claim"
                 " WHERE claim_id LIKE 'CL-RM-%'").fetchone()[0] or 0
seq = mx + 1
print("库内 max claim seq:", mx, "-> 本次起始:", seq)

plan, skip_src, skip_hash = [], 0, 0
for p, lv, summ in cands:
    src_id = "SRC-rowmine:%s.messages.%d" % (SRCDB, p)
    if src_id in existing_src:
        skip_src += 1
        continue
    q = make_quote(data[p][1])
    h = sha(src_id + "|" + q)
    if h in existing_hash:
        skip_hash += 1
        continue
    plan.append((p, data[p][2], data[p][3], lv, summ, src_id, q, h))
print("待写:", len(plan), "| 跳过 source_id:", skip_src, "| 跳过 hash:", skip_hash)

if mode == "--dry-run":
    print("[dry-run] 未写入任何数据。")
    print("首尾 claim 号:", "CL-RM-%06d" % seq, "..", "CL-RM-%06d" % (seq + len(plan) - 1))
    con.close()
    sys.exit(0)

_evid_next = con.execute("SELECT COALESCE(MAX(id),0)+1 FROM claim_evidence").fetchone()[0]
print("claim_evidence 起始 id:", _evid_next, flush=True)

SQL_RS = (
    "INSERT INTO raw_source (source_id, namespace, source_db, source_table, local_pk,"
    " content_hash, title, source_type, carrier, source_layer, source_date, date_precision,"
    " author, first_hand, contemporary, retrospective, banned_source, doubt_flag,"
    " created_at, updated_at) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)")
SQL_EV = (
    "INSERT INTO evidence (evidence_id, source_id, anchor, quote, quote_lang, fact_text,"
    " evidence_kind, event_date, event_date_precision, confidence, extracted_by,"
    " extraction_review, created_at, updated_at) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)")
SQL_CL = (
    "INSERT INTO claim (claim_id, claim_text, claim_type, time_start, time_end,"
    " time_precision, evidence_level, wording_gate, status, created_by, created_at, updated_at)"
    " VALUES (?,?,?,?,?,?,?,?,?,?,?,?)")
SQL_CE = (
    "INSERT INTO claim_evidence (id, claim_id, evidence_id, role, strength, disposition, created_at)"
    " VALUES (?,?,?,?,?,?,?)")

written = []
rs_rows, ev_rows, cl_rows, ce_rows = [], [], [], []
for p, d, frm, lv, summ, src_id, q, h in plan:
    ev_id, cl_id = "EV-RM-%06d" % seq, "CL-RM-%06d" % seq
    rs_rows.append((src_id, "row_mine_db", SRCDB, "messages", str(p), h,
                    (data[p][0] or "")[:200], "mailing_list", "mail_archive", 1, d, "day",
                    frm, 1, 1, 0, 0, 0, NOW, NOW))
    ev_rows.append((ev_id, src_id, ANCHOR, q, "en", summ, "quote", d, "day",
                    0.85 if lv in ("L4", "L3") else 0.6, "llm:agent", "checked", NOW, NOW))
    gate = "attribution_allowed" if lv in ("L4", "L3") else "contextual_only"
    cl_rows.append((cl_id, summ, "FACT", d, d, "day", lv, gate, "supported",
                    "llm:agent", NOW, NOW))
    ce_rows.append((_evid_next, cl_id, ev_id, "supporting",
                    "strong" if lv in ("L4", "L3") else "contextual", "accept", NOW))
    _evid_next += 1
    written.append((cl_id, ev_id, p))
    seq += 1
print("plan 装配完成 %d 条，开事务" % len(plan), flush=True)
con.execute("BEGIN TRANSACTION")
print("BEGIN 完成", flush=True)

# executemany 在本机对本库的病态慢（1226 行 108s 起、跨 SMB 挂死 40 分钟不返回）：
# 改 CSV + read_csv_auto 每表一条语句，同规模本地盘实测 0.56s。列类型显式给死，
# 不做类型推断，避免 local_pk / 各类 0/1 标记位被推成 INT 后与表定义失配。
import csv as _csv

TD = os.environ.get("TEMP", r"C:\Windows\Temp")
CSVDIR = os.path.join(TD, "fhk_b071_reg_%d" % os.getpid())
os.makedirs(CSVDIR, exist_ok=True)
COLS = {
    "raw_source": ("source_id, namespace, source_db, source_table, local_pk, content_hash,"
                   " title, source_type, carrier, source_layer, source_date, date_precision,"
                   " author, first_hand, contemporary, retrospective, banned_source,"
                   " doubt_flag, created_at, updated_at").split(", "),
    "evidence": ("evidence_id, source_id, anchor, quote, quote_lang, fact_text,"
                 " evidence_kind, event_date, event_date_precision, confidence, extracted_by,"
                 " extraction_review, created_at, updated_at").split(", "),
    "claim": ("claim_id, claim_text, claim_type, time_start, time_end, time_precision,"
              " evidence_level, wording_gate, status, created_by, created_at, updated_at")
            .split(", "),
    "claim_evidence": ("id, claim_id, evidence_id, role, strength, disposition, created_at")
                     .split(", "),
}
BATCH = {"raw_source": rs_rows, "evidence": ev_rows, "claim": cl_rows,
         "claim_evidence": ce_rows}
try:
    for tag, rows in BATCH.items():
        cols = COLS[tag]
        p = os.path.join(CSVDIR, tag + ".csv")
        with open(p, "w", newline="", encoding="utf-8") as f:
            w = _csv.writer(f)
            w.writerow(cols)
            for r in rows:
                w.writerow(["" if v is None else v for v in r])
        p = p.replace("\\", "/")
        tcols = ", ".join("'%s': VARCHAR" % c for c in cols)
        sel = ", ".join(cols)
        con.execute(
            "INSERT INTO %s (%s) SELECT %s FROM read_csv_auto(?, header=true,"
            " columns={%s})" % (tag, sel, sel, tcols), [p])
        print("  %s: %d 行" % (tag, len(rows)), flush=True)
    con.execute("COMMIT")
    print("COMMITTED:", len(written))
except Exception:
    try:
        con.execute("ROLLBACK")
    except Exception:
        pass
    raise
finally:
    import shutil
    shutil.rmtree(CSVDIR, ignore_errors=True)

ok, fails = 0, []
if written:
    q_by_ev = dict(con.execute(
        "SELECT evidence_id, quote FROM evidence WHERE evidence_id IN (%s)"
        % ",".join("?" for _ in written),
        [ev for _, ev, _ in written]).fetchall())
    m3 = duckdb.connect(MAILDB, read_only=True)
    body_by_pk = dict(m3.execute(
        "SELECT CAST(id AS BIGINT), COALESCE(body,'') || '\n' || COALESCE(subject,'')"
        " FROM messages WHERE CAST(id AS BIGINT) IN (%s)"
        % ",".join("?" for _ in written),
        [p for _, _, p in written]).fetchall())
    m3.close()
    for cl_id, ev_id, p in written:
        if q_by_ev.get(ev_id, "") in body_by_pk.get(p, ""):
            ok += 1
        else:
            fails.append((cl_id, p))
print("写后反查 quote: %d/%d" % (ok, len(written)))
if fails:
    print("反查失败:", fails[:20])
n = con.execute(
    "SELECT COUNT(*) FROM claim_evidence ce JOIN claim c ON c.claim_id=ce.claim_id"
    " JOIN evidence e ON e.evidence_id=ce.evidence_id JOIN raw_source r ON r.source_id=e.source_id"
    " WHERE e.anchor=?", [ANCHOR]).fetchone()[0]
print("四表 join 命中:", n)
print("MAPJSON:", __import__("json").dumps(
    {str(p): cl for cl, _, p in written}, ensure_ascii=False))
