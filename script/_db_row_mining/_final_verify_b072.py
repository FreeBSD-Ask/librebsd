# -*- coding: utf-8 -*-
"""fhk_b072 独立四层核验（只读，22 项）。与流水线上各脚本互为交叉复核。

L1 候选层   1-2
L2 claim 库 3-9
L3 叙述层  10-14
L4 大纲宿主 15-19
L5 台账与记账 20-22
用法：C:/Python314/python.exe _final_verify_b070.py
退出码 0＝22/22 全绿；非 0＝有 FAIL。
"""
import io
import json
import os
import re
import sys

import duckdb

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
RL = os.path.join(HERE, "review_logs")
LC = r"d:\librebsd\04-现代研究文献\historical_claims.duckdb"
MD = r"d:\librebsd\03-原始史料库\11-邮件列表史料\01-freebsd\db\freebsd-hackers.duckdb"
LED = os.path.join(HERE, "mail2d_read_ledger.json")
PROG = os.path.join(HERE, "progress.jsonl")
CG = r"d:\librebsd\01-项目管理\00-变更记录\changelog.duckdb"
HOST_DIR = r"d:\librebsd\05-卷册大纲\第05卷-freebsd的工程化奠基\第88章-freebsd2x站稳脚跟"

TAG, LIB, HOST = "fhk_b072", "freebsd-hackers", "885"
N_EXP, L4_EXP, L3_EXP = 1119, 446, 673
CID_LO, CID_HI = 413208, 414326
PK_LO, PK_HI = 2600432, 2602440
HI_EXP, TAGS_EXP = 144000, 72
REFS_BEFORE = 22902

FORBID = set("「」『』*|")
QUOTES = set(chr(c) for c in [0x2018, 0x2019, 0x201C, 0x201D, 0x0027, 0x0022, 0x0060])
TRAIL = set("。，、；：？！…—．·~-.,;:?! ")
DATE_RE = re.compile(r"\d{4}\s*年")
VERS_RE = re.compile(r"FreeBSD[- ][A-Za-z0-9.\~\-]+|\b\d+(?:\.\d+)+(?:-[A-Z][A-Z0-9]*)?")
FBWORD = re.compile(r"FreeBSD[- ]([A-Za-z][A-Za-z0-9]*)")
VERBLIKE = set(["current", "stable", "release", "prerelease", "snapshot", "snap",
                "x", "r", "rc1", "rc2", "x11", "x11r6", "keltia", "www", "hackers"])

res = []


def chk(n, name, ok, detail=""):
    res.append((n, name, bool(ok), detail))


# ---------------- L1 候选层 ----------------
cand = {}
for ln in io.open(os.path.join(RL, TAG + "_candidates.txt"), encoding="utf-8"):
    if ln.strip():
        f = ln.rstrip("\n").split("|", 2)
        cand[f[0]] = (f[1], f[2])
cvals = list(cand.values())
ck = list(cand)
casc = [int(x) for x in ck] == sorted(int(x) for x in ck)
chk(1, "候选件 %d 条 / pk 唯一升序 / 等级 in {L3,L4} / 摘要 20-80 字 / 无禁字符与尾标点"
    % len(cand),
    len(cand) == N_EXP and casc and len(set(cand)) == len(cand)
    and all(v[0] in ("L3", "L4") for v in cvals)
    and all(20 <= len(v[1]) <= 80 for v in cvals)
    and not any(set(v[1]) & (FORBID | QUOTES) for v in cvals)
    and all(v[1].rstrip()[-1] not in TRAIL for v in cvals),
    "条数 %d" % len(cand))

cmap = json.load(io.open(os.path.join(RL, TAG + "_claim_map.json"), encoding="utf-8"))
if cmap and isinstance(list(cmap.values())[0], dict):
    cmap = {k: v["claim_id"] for k, v in cmap.items()}
chk(2, "claim_map %d 条与候选 pk 集合完全一致" % len(cmap),
    len(cmap) == N_EXP and set(cmap) == set(cand), "条数 %d" % len(cmap))

# ---------------- L2 claim 库 ----------------
con = duckdb.connect(LC, read_only=True)


def rows(sql, args=()):
    return con.execute(sql, list(args)).fetchall()


J4 = ("JOIN claim_evidence ce ON ce.claim_id=c.claim_id "
      "JOIN evidence e ON e.evidence_id=ce.evidence_id")
sup = [r[0] for r in rows(
    "SELECT c.claim_id FROM claim c " + J4 + " WHERE e.anchor=?", [TAG])]
seq = sorted(int(c.rsplit("-", 1)[1]) for c in sup)
n_l4 = len(rows("SELECT c.claim_id FROM claim c " + J4 +
                " WHERE e.anchor=? AND c.evidence_level=?", [TAG, "L4"]))
n_l3 = len(rows("SELECT c.claim_id FROM claim c " + J4 +
                " WHERE e.anchor=? AND c.evidence_level=?", [TAG, "L3"]))
pks_db = [int(r[0]) for r in rows(
    "SELECT CAST(rs.local_pk AS INTEGER) FROM claim c " + J4 +
    " JOIN raw_source rs ON rs.source_id=e.source_id WHERE e.anchor=?", [TAG])]
lvl = {r[0]: r[1] for r in rows(
    "SELECT CAST(rs.local_pk AS VARCHAR), c.evidence_level FROM claim c " + J4 +
    " JOIN raw_source rs ON rs.source_id=e.source_id WHERE e.anchor=?", [TAG])}
orph = rows("SELECT COUNT(*) FROM claim_evidence ce LEFT JOIN evidence e "
            "ON e.evidence_id=ce.evidence_id WHERE e.evidence_id IS NULL")[0][0]
chk(3, "claim 库本批 supported %d 条" % len(sup), len(sup) == N_EXP, "实测 %d" % len(sup))
chk(4, "claim 号段 %d..%d 连续无空洞" % (CID_LO, CID_HI),
    seq == list(range(CID_LO, CID_HI + 1)),
    "首 %d 末 %d 共 %d" % (seq[0], seq[-1], len(seq)))
chk(5, "四表 JOIN（claim/claim_evidence/evidence/raw_source）%d 条" % len(pks_db),
    len(pks_db) == N_EXP, "实测 %d" % len(pks_db))
chk(6, "raw_source pk 唯一且落在批窗 %d..%d" % (PK_LO, PK_HI),
    len(set(pks_db)) == N_EXP and min(pks_db) >= PK_LO and max(pks_db) <= PK_HI,
    "实测 %d..%d" % (min(pks_db), max(pks_db)))
chk(7, "等级分布 L4=%d / L3=%d 合计等于块数" % (n_l4, n_l3),
    n_l4 == L4_EXP and n_l3 == L3_EXP and n_l4 + n_l3 == N_EXP,
    "L4=%d L3=%d" % (n_l4, n_l3))
chk(8, "claim_evidence 无悬挂（孤儿 0）", orph == 0, "孤儿 %d" % orph)
chk(9, "等级逐 pk 与候选件一致",
    len(lvl) == N_EXP and all(lvl[p] == cand[p][0] for p in lvl),
    "对账 %d pk" % len(lvl))

# ---------------- L3 叙述层 ----------------
mb = io.open(os.path.join(RL, TAG + "_mount_narr.tsv"), "rb").read()
lines = [l for l in mb.decode("utf-8").split("\n") if l.strip()]
narr, asgn = {}, {}
for l in lines:
    f = l.split("\t")
    narr[int(f[0])] = f[2]
    asgn[f[0]] = f[1]
bad_len = [p for p in narr if not (60 <= len(narr[p]) <= 140)]
bad_fmt = []
for p in narr:
    s = narr[p]
    # 引号检测与 _merge_narr_fhk_b072.py 同口径：豁免英文所有格/缩写式撇号
    # （Dobb's、I'm、it's），否则专有名词 Dr Dobb's Journal 会被误判。
    probe = re.sub(r"[A-Za-z]+\'[A-Za-z]+", "", s)
    if (set(probe) & (FORBID | QUOTES)) or s[-1] in TRAIL or s[0].isdigit() \
       or DATE_RE.search(s) or "\t" in s or "\u3000" in s:
        bad_fmt.append(p)
fb = [p for p in narr if any(w.lower() not in VERBLIKE
                             for w in FBWORD.findall(narr[p]))]
con_m = duckdb.connect(MD, read_only=True)
cache = {}
for i in range(0, len(narr), 200):
    seg = sorted(narr)[i:i + 200]
    for r in con_m.execute(
            "SELECT CAST(id AS BIGINT), body FROM messages "
            "WHERE CAST(id AS BIGINT) IN (%s)"
            % ",".join("?" for _ in seg), [int(x) for x in seg]).fetchall():
        b = str(r[1] or "")
        cache[r[0]] = "\n".join(l for l in b.split("\n")
                                if not l.lstrip().startswith((">", ":")))
con_m.close()
verbad = []
for p in narr:
    own = cache.get(p, "")
    for m in VERS_RE.findall(narr[p]):
        if m not in own:
            verbad.append((p, m))
            break
pks_n = [int(l.split("\t")[0]) for l in lines]
chk(10, "叙述合并件 %d 行 / 无 BOM / 无 CR / pk 升序唯一 / 宿主全 885" % len(lines),
    len(lines) == N_EXP and not mb.startswith(b"\xef\xbb\xbf") and b"\r" not in mb
    and pks_n == sorted(pks_n) and len(set(pks_n)) == N_EXP
    and set(asgn.values()) == {"885"}, "行数 %d" % len(lines))
chk(11, "叙述长度全在 60-140", not bad_len,
    "越界 %d 条 %s" % (len(bad_len), bad_len[:5]))
chk(12, "叙述格式：无禁字符/引号/尾标点/数字开头/年号前缀/全角空格",
    not bad_fmt, "违规 %d 条 %s" % (len(bad_fmt), bad_fmt[:5]))
chk(13, "叙述版本形态逐条回源自有正文（SUBJ 与 > 引用块不计）",
    not verbad, "违规 %d 条 %s" % (len(verbad), verbad[:5]))
chk(14, "叙述非候选摘要逐字复制；FreeBSD 后不接英文普通词",
    all(narr[p] != cand[str(p)][1] for p in narr) and not fb,
    "FreeBSD 衔接违规 %d 条 %s" % (len(fb), fb[:5]))

# ---------------- L4 大纲宿主 ----------------
hfile = os.path.join(HOST_DIR,
                     [f for f in os.listdir(HOST_DIR) if f.startswith("88.5-")][0])
hb = io.open(hfile, "rb").read()
ht = hb.decode("utf-8")
marks = re.findall(r"<!-- ROW_MINE: %s\.messages\.(\d+) -->" % LIB, ht)
mkset = [m for m in marks if m in cand]
cid_bad, lvl_bad, txt_bad = [], [], []
for p in mkset:
    i = ht.find("ROW_MINE: %s.messages.%s" % (LIB, p))
    seg = ht[i:i + 200]
    m = re.search(r"claim\.(CL-RM-\d+)", seg)
    if (m.group(1) if m else None) != cmap[p]:
        cid_bad.append(p)
    ml = re.search(r"证据等级：(L\d)", seg)
    if (ml.group(1) if ml else None) != cand[p][0]:
        lvl_bad.append(p)
    if narr[int(p)][:60] not in ht[i:i + 4000]:
        txt_bad.append(p)
chk(15, "宿主含 %d 个本批 ROW_MINE 标记且各恰 1 次" % len(mkset),
    len(mkset) == N_EXP and len(set(mkset)) == N_EXP,
    "命中 %d 唯一 %d" % (len(mkset), len(set(mkset))))
chk(16, "宿主块头 claim.CL-RM 与库内真值逐条一致", not cid_bad,
    "不符 %d 条 %s" % (len(cid_bad), cid_bad[:5]))
chk(17, "宿主块头证据等级与库内真值逐条一致", not lvl_bad,
    "不符 %d 条 %s" % (len(lvl_bad), lvl_bad[:5]))
chk(18, "宿主文本与叙述件回源一致（前 60 字逐条命中）", not txt_bad,
    "漂移 %d 条 %s" % (len(txt_bad), txt_bad[:5]))
tot = len(re.findall(r"<!-- ROW_MINE:", ht))
chk(19, "宿主无 BOM/CRLF 且 ROW_MINE 总量 %d＝批前 %d 加本批 %d"
    % (tot, REFS_BEFORE, N_EXP),
    not hb.startswith(b"\xef\xbb\xbf") and b"\r\n" not in hb
    and tot == REFS_BEFORE + N_EXP, "总量 %d" % tot)

# ---------------- L5 台账与记账 ----------------
lb = io.open(LED, "rb").read()
led = json.loads(lb.decode("utf-8"))
li = led["items"][LIB]
rec = li["records"][0]
tags = rec["tags"]
seq_ok = tags == ["fhk_b%03d" % i for i in range(1, TAGS_EXP + 1)]
ind = None
for _i in (1, 2, 4):
    if json.dumps(led, ensure_ascii=False, indent=_i) == lb.decode("utf-8"):
        ind = _i
        break
chk(20, "台账三水位=%d / hi=%d / tags=%d 条连续 / 无 BOM·CRLF·尾换行 / 缩进回环"
    % (li["read_judged"], rec["hi"], len(tags)),
    li["read_spec"] == li["read_judged"] == li["read_effective"] == HI_EXP
    and rec["hi"] == HI_EXP and len(tags) == TAGS_EXP and seq_ok
    and not lb.startswith(b"\xef\xbb\xbf") and b"\r\n" not in lb
    and not lb.endswith(b"\n") and ind is not None,
    "hi=%d tags=%d indent=%s" % (rec["hi"], len(tags), ind))
note_ok = ("fhk_b072" in led.get("note", "")
           and ("142000→144000" in led.get("note", "")))
prog_ok = any(json.loads(l).get("batch") == TAG
              for l in io.open(PROG, encoding="utf-8") if l.strip())
con2 = duckdb.connect(CG, read_only=True)
cl_ok = con2.execute(
    "SELECT COUNT(*) FROM entries WHERE summary LIKE 'H3 fhk_b072%'").fetchone()[0]
con2.close()
chk(21, "台账 note 追加了本批记账句（含 142000→144000）", note_ok,
    "note 命中 %s" % note_ok)
chk(22, "progress.jsonl 与 changelog.entries 均已记账",
    prog_ok and cl_ok == 1, "progress=%s changelog=%d" % (prog_ok, cl_ok))

con.close()

# ---------------- 汇总 ----------------
print("=" * 78)
print("fhk_b072 独立四层核验（只读 %d 项）" % len(res))
print("=" * 78)
for n, name, ok, det in res:
    print("  [%s] %2d  %s%s" % ("PASS" if ok else "FAIL", n, name,
                                ("    " + det) if det else ""))
nf = [r for r in res if not r[2]]
print("-" * 78)
print("PASS %d / %d   %s" % (len(res) - len(nf), len(res),
                             "全绿" if not nf else "失败项 %s" % [r[0] for r in nf]))
sys.exit(0 if not nf else 1)
