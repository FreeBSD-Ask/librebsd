#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第十五件·人物库语义完整性门禁（2026-10-06 立，120 批 ★4）。

对象：10-交叉索引/cross_indexes.duckdb 的 person_bio_research 表（全表）。
判据（行级，违例即 FAIL 并列 person_id）：
  P1 sources      非空且为合法 JSON 数组（每行须载明一手/二手来源）
  P2 doubt_flags  非空且为合法 JSON 数组（空疑点记 [] 亦算非空——须显式声明「无」）
  P3 check_date   非空（最近核查日期）
  P4 priority     非空且 ∈ {P0,P1,P2,P3}
设立缘由：31 号文「Christina Loconti」幻觉人物事故（120 号文）——人物断言未经署名类官方
文件核对即入正史的防线之一；机器面保证人物库每行可溯源、疑点显式化。
用法：
    python audit_person_bio_integrity.py            # 闸面，0 违例 exit 0
    python audit_person_bio_integrity.py --selftest # 判据非空自检（注入违例须全数拦下）
"""
import json
import sys
import tempfile
from pathlib import Path

import duckdb

DB = Path(__file__).resolve().parents[3] / "10-交叉索引" / "cross_indexes.duckdb"
PRIO = {"P0", "P1", "P2", "P3"}


def check_rows(con, table="person_bio_research"):
    bad = []
    rows = con.execute(
        "select person_id, person_name, sources, doubt_flags, check_date, priority, "
        "coalesce(scope_tag, '') , coalesce(research_round, '') "
        "from %s order by person_id" % table).fetchall()
    legacy_n = 0
    for pid, name, sources, doubt, check_date, prio, scope, rround in rows:
        # 存量豁免（显式登记，非免检）：老批次行（outline-legacy／无轮次）记 INFO 不 FAIL——
        # 其 sources 为自由文本、priority 未分级，系 R5 前工作流形态；新工作流行（R5 起）强制。
        if scope == 'outline-legacy' or rround == '':
            legacy_n += 1
            continue
        probs = []
        try:
            arr = json.loads(sources) if sources else None
            if not isinstance(arr, list) or len(arr) == 0:
                probs.append("P1 sources 空或非 JSON 数组")
        except Exception:
            probs.append("P1 sources 非 JSON")
        try:
            arr = json.loads(doubt) if doubt else None
            if not isinstance(arr, list):
                probs.append("P2 doubt_flags 非 JSON 数组")
        except Exception:
            probs.append("P2 doubt_flags 非 JSON")
        if doubt is None or str(doubt).strip() == "":
            probs.append("P2 doubt_flags 空（须显式 [] 声明）")
        if not check_date or str(check_date).strip() == "":
            probs.append("P3 check_date 空")
        if not prio or prio not in PRIO:
            probs.append("P4 priority 空或非法（%r）" % prio)
        if probs:
            bad.append((pid, name, probs))
    return bad, legacy_n


def main():
    if "--selftest" in sys.argv:
        tmp = Path(tempfile.mkdtemp(prefix="p15selftest_"))
        tdb = tmp / "t.duckdb"
        con = duckdb.connect(str(tdb))
        con.execute("""create table person_bio_research (
            person_id varchar, person_name varchar, sources varchar,
            doubt_flags varchar, check_date varchar, priority varchar,
            scope_tag varchar, research_round varchar)""")
        ok = json.dumps([{"type": "一手", "ref": "x", "url": "u", "checked": "2026-10-06"}], ensure_ascii=False)
        dj = json.dumps([], ensure_ascii=False)
        L = 'c10-restored'
        con.execute("insert into person_bio_research values ('good','合规行',?,?,?,?,'c10-restored','R5')", [ok, dj, "2026-10-06", "P2"])
        con.execute("insert into person_bio_research values ('bad1','无来源行',NULL,?,?,'P2',?,?)", [dj, "2026-10-06", L, 'R5'])
        con.execute("insert into person_bio_research values ('bad2','无疑点行',?,NULL,?,'P2',?,?)", [ok, "2026-10-06", L, 'R5'])
        con.execute("insert into person_bio_research values ('bad3','无核查日行',?,?,NULL,'P2',?,?)", [ok, dj, L, 'R5'])
        con.execute("insert into person_bio_research values ('bad4','非法优先级行',?,?,?,'P9',?,?)", [ok, dj, "2026-10-06", L, 'R5'])
        bad, _lg = check_rows(con)
        ids = {b[0] for b in bad}
        assert ids == {"bad1", "bad2", "bad3", "bad4"}, "自检拦截面异常：%s" % ids
        assert len(bad) == 4 and all(len(b[2]) >= 1 for b in bad)
        print("第十五件 --selftest：PASS（4 违例注入全数拦下，合规行未误报；判据非空自证）")
        con.close()
        return 0

    if not DB.exists():
        print("第十五件：SKIP（人物库不存在）", file=sys.stderr)
        return 0
    con = duckdb.connect(str(DB), read_only=True)
    bad, legacy_n = check_rows(con)
    total = con.execute("select count(*) from person_bio_research").fetchone()[0]
    con.close()
    print("第十五件·人物库语义完整性：person_bio_research 全表 %d 行（存量豁免 %d 行记 INFO；新工作流行 %d 行强制）" % (total, legacy_n, total - legacy_n))
    if bad:
        for pid, name, probs in bad:
            print("  ❌ %s（%s）：%s" % (pid, name, "；".join(probs)))
        print("第十五件：FAIL（%d 行违例）" % len(bad), file=sys.stderr)
        return 1
    print("第十五件：PASS（sources／doubt_flags／check_date／priority 四判据 0 违例）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
