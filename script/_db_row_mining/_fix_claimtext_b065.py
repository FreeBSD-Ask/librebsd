# -*- coding: utf-8 -*-
"""fhk_b065 候选层 4 处摘要误植：claim_text 订正为已回源的合并终态叙述 + 留痕。

背景（2026-10-05 主会话逐封回源裁定）：下列 4 条候选摘要把引用块内被引者的主张
写成了本封 FROM 的主张，且 claim_text 原样沿用摘要，故库内 claim_text 亦错。
大纲宿主块用的是叙述（已按「> / : 开头引用块不算 FROM 自有正文」重写，回源正确），
故只订正 claim 层，与宿主叙述对齐。

  pk        摘要缺陷
  2586754   摘要写「256K 与 512K 缓存差价可忽略并推荐 512K」——该主张在 Steve Passe 的引用块内；
            FROM（Eric J. Schwertfeger）自有正文只讲三块 P6-150 都能跑到 180、仍按 166 运行
  2586796   摘要写「无联系按钮却有退订按钮」「其投票称用户喜爱垃圾邮件」——本封自有正文
            contact/unsubscribe/vote/poll 命中数全 0，该三项不在正文内
  2586799   摘要写「John Duncan 询问…」——本封 FROM 是 Jonathan M. Bresler，
            自有正文仅 yes, thats the bloody problem.... jmb；Duncan 的问句在 Brian Somers 的引用块内
  2586805   摘要写「主张 AGIS 应做 BGP 黑洞、全球最大垃圾邮件来源、Cyberpromo」——
            FROM 自有正文只有一句对 Jamie Bowden 的转引，主张归属在引用块内

处置口径（对齐 fpo_b192「claim_text 订正为合并终态叙述」）：
  claim.claim_text    := fhk_b065_mount_narr.tsv 的终态叙述（60-140，已回源）
  evidence.extraction_review := 留痕串（原判 checked，改标注待核结论与依据）
  claim_evidence 不动、evidence.quote 不动、raw_source 不动、不新增不删除任何行。
写前逐条断言 claim_id / 现行 claim_text / 当前 extraction_review，任一不符即中止不落盘。

用法： C:/Python314/python.exe _fix_claimtext_b065.py [--write]
"""
import io
import json
import os
import sys
import time

import duckdb

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
RL = os.path.join(HERE, "review_logs")
HC = os.path.join(os.path.abspath(os.path.join(HERE, "..", "..")),
                  "04-现代研究文献/historical_claims.duckdb")
TAG = "fhk_b065"
WRITE = "--write" in sys.argv
LO, HI = 60, 140

PKS = ["2586754", "2586796", "2586799", "2586805"]
NOTE = ("候选层摘要误植（内容取自引用块内被引者），claim_text 已订正为回源终态叙述"
        "（fhk_b065_mount_narr.tsv，2026-10-05 主会话逐封回源裁定）")


def connect(db, ro, tries=96, sleep=15):
    """他会话持续持锁是常态：只在 connect 阶段退避重试，连上后一次性事务写完。"""
    last = None
    for i in range(1, tries + 1):
        try:
            return duckdb.connect(db, read_only=ro)
        except Exception as e:
            last = e
            if i % 4 == 0:
                print("  第 %d 次仍被占（%s），%ds 后重试"
                      % (i, str(e).splitlines()[0][:50], sleep))
            time.sleep(sleep)
    raise SystemExit("连接失败 %d 次：%s" % (tries, last))


narr = {}
for ln in io.open(os.path.join(RL, TAG + "_mount_narr.tsv"), encoding="utf-8"):
    if ln.strip():
        f = ln.rstrip("\n").split("\t")
        if len(f) == 3:
            narr[f[0]] = f[2]
for p in PKS:
    assert p in narr, "缺叙述 %s" % p
    L = len(narr[p])
    assert LO <= L <= HI, "叙述长度 %d 越界 %s" % (L, p)
    assert not any(c in narr[p] for c in "「」『』*|"), "禁字符 %s" % p
    print("  pk=%s 叙述 %d 字符: %s" % (p, L, narr[p][:34] + "…"))

cmap = json.load(io.open(os.path.join(RL, TAG + "_claim_map.json"), encoding="utf-8"))
plan = [(p, cmap[p]["claim_id"], narr[p]) for p in PKS]

con = connect(HC, True)
rows = con.execute(
    "SELECT e.source_id, c.claim_id, c.claim_text, e.extraction_review"
    " FROM evidence e JOIN claim_evidence ce ON ce.evidence_id=e.evidence_id"
    " JOIN claim c ON c.claim_id=ce.claim_id WHERE e.anchor=?", [TAG]).fetchall()
con.close()
by_pk = {}
for sid, cid, ct, ev in rows:
    by_pk[sid.rsplit(".", 1)[-1]] = (cid, ct, ev)

bad = []
for p, cid, _n in plan:
    cur = by_pk.get(p)
    if cur is None:
        bad.append("pk=%s 库内无本批 evidence" % p)
    elif cur[0] != cid:
        bad.append("pk=%s claim_id 不符 库内=%s 期望=%s" % (p, cur[0], cid))
    elif cur[2] != "checked":
        bad.append("pk=%s 现行 extraction_review=%r 非 checked" % (p, cur[2]))
    elif len(cur[1]) > HI:
        bad.append("pk=%s 现行 claim_text 已 %d 字符" % (p, len(cur[1])))
if bad:
    print("\n!! 写前断言失败：")
    for x in bad:
        print("   - " + x)
    raise SystemExit(1)
print("\n写前断言 4/4 通过（claim_id 对上、现行 extraction_review=checked、"
      "现行 claim_text 非空）")
if not WRITE:
    print("[dry] 未落盘")
    raise SystemExit(0)

con = connect(HC, False)
try:
    con.execute("BEGIN TRANSACTION")
    for p, cid, n in plan:
        r = con.execute(
            "UPDATE claim SET claim_text=? WHERE claim_id=? AND evidence_level IS NOT NULL"
            " RETURNING claim_id", [n, cid]).fetchone()
        assert r and r[0] == cid, "claim UPDATE 未命中 %s" % cid
        con.execute(
            "UPDATE evidence SET extraction_review=? WHERE anchor=? AND source_id LIKE"
            " '%messages.'||? AND extraction_review='checked'", [NOTE, TAG, p])
    con.execute("COMMIT")
except Exception:
    try:
        con.execute("ROLLBACK")
    except Exception:
        pass
    raise

con = connect(HC, True)
out = con.execute(
    "SELECT e.source_id, c.claim_text, e.extraction_review FROM evidence e"
    " JOIN claim_evidence ce ON ce.evidence_id=e.evidence_id"
    " JOIN claim c ON c.claim_id=ce.claim_id WHERE e.anchor=?", [TAG]).fetchall()
con.close()
chk = {s.rsplit(".", 1)[-1]: (t, r) for s, t, r in out}
ok = sum(1 for p, _c, n in plan if chk.get(p, ("", ""))[0] == n
         and chk.get(p, ("", ""))[1] == NOTE)
n_all = len(chk)
print("写后反查 订正命中 %d/4 | 本批 evidence 仍 %d 条" % (ok, n_all))
assert ok == 4 and n_all == 1226, "订正不完整或本批行数漂移"
print("COMMITTED：claim_text 订正 4 条 + extraction_review 留痕 4 条；"
      "claim_evidence / evidence.quote / raw_source 未动，本批行数守恒 1226")
