# -*- coding: utf-8 -*-
"""fhk_b072 大纲写回（Phase 3）

- 日期/作者/等级/claim_id 由源库 + claim_map 注入（避免转录错误）；
- 叙述文本来自 review_logs/fhk_b072_mount_narr.tsv（子代理逐条读正文撰写，主会话已校验）；
- 追加至目标文件末尾，幂等（重复 ROW_MINE 标记跳过）；脚本统一补日期前缀与纪律收束句；
- 产出 supplement_log.jsonl 逐条留痕。
用法: C:/Python314/python.exe _outline_fhk_b072.py [--write]
"""
import io
import json
import os
import re
import sys

import duckdb

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = r"d:\librebsd\05-卷册大纲"
MAILDB = r"d:\librebsd\03-原始史料库\11-邮件列表史料\01-freebsd\db\freebsd-hackers.duckdb"
ANCHOR = "fhk_b072"
TAG = "2026-10-07 freebsd-hackers 战线"
WRITE = "--write" in sys.argv

TARGET_REL = {
    "885": r"第05卷-freebsd的工程化奠基\第88章-freebsd2x站稳脚跟\88.5-freebsd2x的开发者群体与core-team代际更替.md",
}


def resolve(rel):
    """按节号前缀在目录内实际解析文件，规避文件名 Unicode 差异。"""
    full = os.path.join(ROOT, rel)
    if os.path.exists(full):
        return full
    d, base = os.path.dirname(full), os.path.basename(full)
    if not os.path.isdir(d):
        return full
    pref = base.split("-", 1)[0] + "-"
    hits = [f for f in os.listdir(d) if f.startswith(pref)]
    if len(hits) == 1:
        print("[resolve] %s -> %s" % (base[:24], hits[0][:40]))
        return os.path.join(d, hits[0])
    return full


TAIL = {
    "L4": "引用时按 L4 纪律：以上为邮件列表当事人一手自述，属过程性证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。",
    "L3": "引用时按 L3 纪律：以上为邮件列表当事人陈述，属过程性证据，具体事实与量化结论仍须交叉复核，不得单独引为定论。",
    "L2": "引用时按 L2 纪律：以上为社区参与者转述或讨论，需以当事人或原始记录复核，仅作语境性参考。",
    "L1": "引用时按 L1 纪律：本条为背景线索，须持慎重态度，不单独支撑论点。",
}

# 等级
lv = {}
for ln in io.open(os.path.join(HERE, "review_logs", "fhk_b072_candidates.txt"), encoding="utf-8"):
    if ln.strip():
        p = ln.rstrip("\n").split("|", 2)
        lv[p[0]] = p[1]
cmap = json.load(io.open(os.path.join(HERE, "review_logs", "fhk_b072_claim_map.json"), encoding="utf-8"))
# 双 schema 归一化（坑 49 根修）：claim_map 既可能是扁平 {pk: claim_id}，
# 也可能是富 schema {pk: {claim_id, level, quote, ...}}（register 脚本各自演化所致）。
# 块头只插 claim_id 字符串，dict 直接插值会把整段 dict 拼进宿主块头并污染整批。
# 修法与 _outline_fhk_b043.py 一致：取 claim_id + 形态断言，两种 schema 都接受。
cmap = {k: (v["claim_id"] if isinstance(v, dict) else v) for k, v in cmap.items()}
assert all(re.match(r"^CL-RM-\d{6}$", x) for x in cmap.values()), "claim_map claim_id 形态非法（坑 49）"
rows = []
for ln in io.open(os.path.join(HERE, "review_logs", "fhk_b072_mount_narr.tsv"), encoding="utf-8"):
    if ln.strip():
        pk, hk, nar = ln.rstrip("\n").split("\t")
        rows.append((pk, hk, nar))
assert len(rows) == len(lv), "叙述 %d 条 != 候选 %d 条" % (len(rows), len(lv))
assert not (set(p for p, _, _ in rows) - set(cmap)), "叙述含 claim_map 之外的 pk"
# register 后可有 pk 被剔除（元数据缺失等），claim_map 不随之删；剔除项须确已判 rejected
_rpks = set(p for p, _, _ in rows)
_missing = set(cmap) - _rpks
if _missing:
    _cids = tuple(cmap[p] for p in _missing)
    _con = duckdb.connect(r"d:\librebsd\04-现代研究文献\historical_claims.duckdb", read_only=True)
    _st = dict(_con.execute("SELECT claim_id,status FROM claim WHERE claim_id IN (%s)" % ",".join("?" for _ in _cids),
                            list(_cids)).fetchall())
    _con.close()
    _bad = {p: _st.get(cmap[p]) for p in _missing if _st.get(cmap[p]) != "rejected"}
    assert not _bad, "claim_map 多出的 pk 未判 rejected，不得静默跳过: %s" % _bad
    print("[info] claim_map 多出 %d 条（已判 rejected，不入大纲）: %s" % (len(_missing), sorted(_missing)))
cmap = {k: v for k, v in cmap.items() if k in _rpks}
assert set(p for p, _, _ in rows) == set(cmap), "pk 与 claim_map 不一致"

mail = duckdb.connect(MAILDB, read_only=True)
# 批查取日期：源库单 PK 查询约 0.96s，1077 条逐条要 17 分钟，批查是一次索引扫描。
date = {}
for _i in range(0, len(rows), 200):
    _seg = [int(p) for p, _, _ in rows[_i:_i + 200]]
    for _id, _d in mail.execute(
            "SELECT CAST(id AS BIGINT), date FROM messages WHERE CAST(id AS BIGINT) IN (%s)"
            % ",".join("?" for _ in _seg), _seg).fetchall():
        date[str(_id)] = _d
mail.close()
_miss = [p for p, _, _ in rows if p not in date]
assert not _miss, "源库缺日期 pk: %s" % _miss[:10]


def zh_date(iso):
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", str(iso or ""))
    if not m:
        return ""
    y, mo, d = m.groups()
    return "%s 年 %d 月 %d 日" % (y, int(mo), int(d))


def make_block(pk, nar):
    l = lv[pk]
    d = zh_date(date[pk])
    body = nar.strip()
    if body and body[-1] not in "。？！":
        body = body + "。" + TAIL[l]
    else:
        body = body + TAIL[l]
    text = ("%s，%s" % (d, body)) if d else body
    return ("<!-- ROW_MINE: freebsd-hackers.messages.%s -->\n"
            "**当事人自述**（证据等级：%s，来源：`historical_claims.duckdb.claim.%s`；%s 全库行级遍历考据采纳）\n\n%s"
            % (pk, l, cmap[pk], TAG, text))


groups = {}
for pk, hk, nar in rows:
    groups.setdefault(hk, []).append((pk, nar))

log_rows, total = [], 0
for hk, recs in groups.items():
    rel = TARGET_REL[hk]
    fp = resolve(rel)
    if not os.path.exists(fp):
        raise SystemExit("目标不存在: " + fp)
    txt = io.open(fp, encoding="utf-8").read()
    new = []
    for pk, nar in recs:
        if ("ROW_MINE: freebsd-hackers.messages.%s" % pk) in txt:
            continue
        new.append((pk, make_block(pk, nar)))
    if new and WRITE:
        out = txt.rstrip("\n") + "\n\n" + "\n\n".join(b for _, b in new) + "\n"
        assert "\ufeff" not in out and "\r" not in out, "BOM/CRLF 检测失败"
        io.open(fp, "w", encoding="utf-8", newline="\n").write(out)
        txt = out
    for pk, _ in new:
        log_rows.append({"ts": "2026-10-07", "db": "freebsd-hackers", "batch": ANCHOR,
                         "row_id": int(pk), "claim_id": cmap[pk],
                         "target": rel.replace("\\", "/"), "block": "ROW_MINE",
                         "kind": "当事人自述", "level": lv[pk],
                         "note": next(n for p, _, n in rows if p == pk)[:80]})
    total += len(new)
    print("%-52s +%-3d total_refs=%d" % (rel.split("\\")[-1][:50], len(new), txt.count("ROW_MINE:")))

print("合计拟插 %d 块" % total)
if WRITE and log_rows:
    with io.open(os.path.join(HERE, "supplement_log.jsonl"), "a", encoding="utf-8", newline="\n") as f:
        for r in log_rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print("supplement_log +%d" % len(log_rows))
if not WRITE:
    print("[dry] 未写盘")
