#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""provenance_history 审计表完整性门禁（数据库层，独立计数）。

对象面
------
`04-现代研究文献/historical_claims.duckdb` 的 `provenance_history` 表
（六列：`id`／`source_id`／`seq`／`event_type`／`detail`／`at`）。

设立缘由：为什么这一件是「真重复」判据而不是「键重复」判据
----------------------------------------------------------
2026-10-15 复核曾报「本表 1,077 行重复（7.3%），写审计非幂等」，据此设计过一版
按 `(source_id, event_type, at)` 判重复的哨兵。2026-10-16 实测推翻了该前提：

    总行 10,554；三元组 (source_id, event_type, at) 重复组 601、涉及 1,690 行；
    但这 601 组**全部** `COUNT(DISTINCT detail) > 1`——同键不同内容；
    把 `detail` 也计入键后，真重复 = **0 组**。

也就是说，同一批 `claim_backfill`（4884 行）在同一时刻、同一事件类型下逐条记录
**不同的 claim**，三元组相同是设计使然，不是写重复。按三元组判重复会把 1,690 条
正当审计行全部误报；若把它设成 FAIL，会立即阻断全项目每个写库会话。
故本件只判**真重复**（同键同内容），并对三元组重复以 INFO 反向声明其正当性，
防止后人再把这一形态读成缺陷。

`id` 列的统一约定（2026-10-16 主理人裁定，**前向收紧、不回填**）
--------------------------------------------------------------
实测确认 `id` 是一个**真实的全局单调递增序号**，且跨写手家族连续编号：

    按 "at" 升序后 `id` 出现回落的次数：0 / 1618
    claim_fix        id 1–2      f2_b01_dbfix   3–500
    f2_b10_dbfix   501–512      f2_b10_x1fix  513–1170
    f2_b10_lvfix  1171–1184     w172_rv_reject 1185–1599

空 `id` 共 8,936 行，且**仍在持续产生**（`f4_b24_dbfix` 23 行的 `at` 为
2026-10-16T01:31:07+08:00，是全表最新一行）——这是活着的写手缺陷，不是历史遗留。

裁定**不回填**，理由：向一个真实连续序列（2–2014，其中 id=2014 被 19 行共享，
1600–2013 从未分配）注入 8,936 个编造号，会把「显式错误」变成「静默可信」——
NULL 一眼可辨是缺陷，编造的号无法与合法序号区分，且空 `id` 行的时间戳与已填行
交错，回填无法保持单调性。根因是 `claim_backfill`／`f4_*` 写手路径绕过了取号
助手，那是代码缺陷，应在写手侧修，不应在审计表里伪造序列。

故约定为**前向收紧**：以 `CUTOFF_DATE`（默认 2026-10-17，裁定日为 2026-10-16）
为界，裁定前写入的空 `id` 行显式登记为存量债务（INFO，逐写手列出、不隐藏），
裁定日起的任何新写入缺 `id` 即 FAIL。

判据（**只读连接**，本件不写活库）
----------------------------------
**D1 FAIL —— 真重复（幂等性失守）**
   `GROUP BY source_id, event_type, "at", detail HAVING COUNT(*)>1`。
   今天实测 0 组；>0 即判 FAIL。这是唯一真正表示「同一事件被写了两次」的形态。

**D2a INFO —— 裁定前空 `id`（存量债务，显式登记）**
   逐 `event_type` 列出裁定日之前的空 `id` 行，附各写手最晚写入时刻。不阻断。
   今天实测 8,936 行（`claim_backfill` 4884＋`claim_fix` 3991＋`f4_*` 家族）。

**D2b FAIL —— 裁定日起空 `id`（违反统一约定）**
   `id IS NULL AND "at" 的日期前缀 >= CUTOFF_DATE`。今天实测 0 行。

**D3 WARN —— `source_id` 为空（无法回溯的审计行）**
   今天实测 483 行（`claim_backfill` 482＋`claim_fix` 1）。这是历史写手形态。

**D4 INFO —— 三元组重复但 detail 分歧（正当设计，非缺陷）**
   反向自证「按三元组判重复」是错的，见上。不参与退出码。

**D5 WARN / FAIL —— `id` 序列冲突（同号多行）**
   `GROUP BY id HAVING COUNT(*)>1`。今天实测 1 组：`id=2014` 被 `w172_rv_keep`
   的 19 行共享（裁定前，WARN）。裁定日起出现新冲突即 FAIL。

`"at"` 列时间格式混杂（`YYYY-MM-DD HH:MM:SS`／`...T..+08:00`／`...Z`），
**字符串比较会因分隔符 ` ` 与 `T` 的码位差异而错序**；实测全部 10,554 行的
前 10 字符均为合规 `YYYY-MM-DD`，故裁定日期比较一律用 `SUBSTR("at",1,10)`。

退出码
------
exit 0 ＝ D1／D2b／D5（裁定后）全干净｜exit 1 ＝ 任一 FAIL 命中｜exit 2 ＝
依赖或表缺失。**本件对活库只读**，`--db` 可指向任意库文件做只读体检。

用法
----
    python audit_provenance_dupes.py            # 体检现行 historical_claims
    python audit_provenance_dupes.py --db <库>   # 体检指定库（只读）
    python audit_provenance_dupes.py --cutoff 2026-11-01   # 调整裁定日
    python audit_provenance_dupes.py --selftest  # 判据非空自检（内存夹具，不落盘）
"""
import argparse
import os
import sys

import duckdb

REPO = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
DEFAULT_DB = os.path.join(REPO, "04-现代研究文献", "historical_claims.duckdb")
TABLE = "provenance_history"
COLS = ("id", "source_id", "seq", "event_type", "detail", "at")

# `at` 是 DuckDB 保留字，SQL 里一律带引号
AT = '"at"'

# 日期前缀（"at" 混合格式下唯一可靠的比较键）
DAY = 'SUBSTR(%s, 1, 10)' % AT

# 统一约定的裁定日：裁定日为 2026-10-16，约定自次日 00:00 起对新写入生效。
# 裁定日之前的空 id 行一律登记为存量债务（D2a INFO），不回填。
CUTOFF_DATE = "2026-10-17"


def _q(col):
    """列名转义：`at` 是保留字，其余照抄。"""
    return AT if col == "at" else col


def _one(con, sql):
    return con.execute(sql).fetchone()[0]


def _schema_ok(con):
    rows = con.execute(
        "SELECT column_name FROM information_schema.columns "
        "WHERE table_name = ?", [TABLE]).fetchall()
    have = set(r[0] for r in rows)
    return sorted(set(COLS) - have)


def _true_dupes(con):
    """D1：同键（含 detail）多行 = 真重复。返回 (组数, 涉及行数, 最大组行)。"""
    key = ", ".join(_q(c) for c in ("source_id", "event_type", "at", "detail"))
    sub = "SELECT COUNT(*) c FROM %s GROUP BY %s HAVING COUNT(*)>1" % (TABLE, key)
    return (_one(con, "SELECT COUNT(*) FROM (%s)" % sub),
            _one(con, "SELECT COALESCE(SUM(c),0) FROM (%s)" % sub),
            _one(con, "SELECT COALESCE(MAX(c),0) FROM (%s)" % sub))


def _triplet_split(con):
    """D4：三元组重复组里，有多少组 detail 有分歧（即「伪重复」＝正当设计）。"""
    key3 = ', '.join(_q(c) for c in ("source_id", "event_type", "at"))
    total = _one(con, "SELECT COUNT(*) FROM (SELECT COUNT(*) c FROM %s GROUP BY %s "
                     "HAVING COUNT(*)>1)" % (TABLE, key3))
    divergent = _one(con, "SELECT COUNT(*) FROM (SELECT COUNT(*) c FROM %s "
                          "GROUP BY %s HAVING COUNT(*)>1 AND COUNT(DISTINCT detail)>1)"
                     % (TABLE, key3))
    return total, divergent


def _null_id_by_writer(con):
    """按写手统计空 id 行，并附各写手最晚写入时刻与其中越界的行数。"""
    return con.execute(
        "SELECT event_type,"
        " SUM(CASE WHEN id IS NULL THEN 1 ELSE 0 END),"
        " COUNT(*),"
        " MAX(%s),"
        " SUM(CASE WHEN id IS NULL AND %s >= ? THEN 1 ELSE 0 END)"
        " FROM %s GROUP BY event_type ORDER BY 3 DESC" % (DAY, DAY, TABLE),
        [CUTOFF_DATE]).fetchall()


def _id_collisions(con):
    """D5：id 冲突组（同号多行）。返回 (组数, 涉及行数, 裁定后组数, 明细)。

    明细行：(id, 行数, 最早 at, 最晚 at, 是否裁定后)。
    """
    sub = ("SELECT id, COUNT(*) c, MIN(%s) mn, MAX(%s) mx FROM %s "
           "WHERE id IS NOT NULL GROUP BY id HAVING COUNT(*)>1"
           % (DAY, DAY, TABLE))
    groups = _one(con, "SELECT COUNT(*) FROM (%s)" % sub)
    rows = _one(con, "SELECT COALESCE(SUM(c),0) FROM (%s)" % sub)
    detail = con.execute(
        "(SELECT id, c, mn, mx, CASE WHEN mx >= ? THEN 1 ELSE 0 END post FROM (%s) "
        "ORDER BY c DESC, id LIMIT 20)" % sub, [CUTOFF_DATE]).fetchall()
    post = sum(1 for d in detail if d[4])
    return groups, rows, post, detail


def _null_source(con):
    """D3：source_id 为空的行数。"""
    return _one(con, "SELECT COALESCE(SUM(CASE WHEN source_id IS NULL "
                     "THEN 1 ELSE 0 END),0) FROM %s" % TABLE)


def _create_fixture(con):
    """建最小夹具：真重复、正当三元组、裁定前/后空 id、id 冲突、source_id 空。"""
    con.execute(
        'CREATE TABLE %s (id BIGINT, source_id VARCHAR, seq BIGINT,'
        ' event_type VARCHAR, detail VARCHAR, "at" VARCHAR)' % TABLE)
    rows = [
        # (a) 真重复：同键同 detail，写了两遍 → D1 应命中 1 组 2 行
        (1, "SRC-x.messages.1", 1, "batch_a", "claim.CL-1.claim_text: 甲",
         "2026-09-20 10:00:00"),
        (2, "SRC-x.messages.1", 1, "batch_a", "claim.CL-1.claim_text: 甲",
         "2026-09-20 10:00:00"),
        # (b) 正当记录：同三元组、detail 不同 → D4 应报 1 组 detail 分歧
        (3, "SRC-y.messages.2", 1, "batch_b", "claim.CL-9.claim_text: 乙",
         "2026-09-20 11:00:00"),
        (4, "SRC-y.messages.2", 1, "batch_b", "claim.CL-10.claim_text: 丙",
         "2026-09-20 11:00:00"),
        # (c) 裁定前空 id → D2a INFO；(d) 裁定前空 source_id → D3
        (None, "SRC-z.messages.3", 1, "claim_backfill",
         "claim.CL-20.claim_text: 丁", "2026-09-24 01:28:11"),
        (None, None, 1, "batch_c", "claim.CL-21.claim_text: 戊",
         "2026-09-24 02:00:00"),
        # (e) 裁定后空 id → D2b 应 FAIL
        (None, "SRC-w.messages.4", 1, "f4_new", "claim.CL-22.claim_text: 己",
         "2026-10-20T09:00:00+08"),
        # (f) 裁定前 id 冲突（id=7 两行）→ D5 WARN；裁定后无冲突
        (7, "SRC-m.messages.5", 1, "batch_m", "claim.CL-30.claim_text: 庚",
         "2026-09-25 08:00:00"),
        (7, "SRC-n.messages.6", 1, "batch_m", "claim.CL-31.claim_text: 辛",
         "2026-09-25 09:00:00"),
        # (g) 裁定后正常行（id 已填）→ 不应触发任何 FAIL
        (8, "SRC-ok.messages.7", 1, "batch_ok", "claim.CL-50.claim_text: 壬",
         "2026-10-20T10:00:00+08"),
    ]
    con.executemany(
        "INSERT INTO %s VALUES (?,?,?,?,?,?)" % TABLE, rows)


def selftest():
    """判据非空自检：五项判据逐项验真，含反向用例（不应误报的形态）。"""
    con = duckdb.connect(":memory:")
    _create_fixture(con)
    fails = []
    try:
        miss = _schema_ok(con)
        if miss:
            fails.append("夹具缺列 %s" % miss)

        groups, rows, mx = _true_dupes(con)
        if groups != 1 or rows != 2 or mx != 2:
            fails.append("D1 应报 1 组 2 行，实得 %d 组 %d 行（最大组 %d）"
                         % (groups, rows, mx))

        t3, dv = _triplet_split(con)
        # (SRC-x,batch_a) 两行同 detail（真重复组）、(SRC-y,batch_b) 两行 detail
        # 不同（正当三元组重复）→ t3=2、dv=1。
        if t3 != 2 or dv != 1:
            fails.append("D4 夹具应 2 组三元组重复、其中 1 组 detail 分歧，"
                         "实得 %d/%d" % (t3, dv))

        # D2a/D2b：裁定前 2 行空 id、裁定后 1 行空 id
        legacy, post = 0, 0
        for ev, nid, tot, mx_at, npost in _null_id_by_writer(con):
            legacy += nid - (npost or 0)
            post += npost or 0
        if legacy != 2:
            fails.append("D2a 应报 2 行裁定前存量空 id，实得 %d" % legacy)
        if post != 1:
            fails.append("D2b 应报 1 行裁定后空 id（应 FAIL），实得 %d" % post)

        if _null_source(con) != 1:
            fails.append("D3 应报 1 行 source_id 空，实得 %d" % _null_source(con))

        cg, cr, cpost, detail = _id_collisions(con)
        if cg != 1 or cr != 2:
            fails.append("D5 应报 1 组冲突共 2 行，实得 %d 组 %d 行" % (cg, cr))
        if cpost != 0:
            fails.append("D5 裁定后冲突应为 0（夹具冲突均在裁定前），实得 %d" % cpost)
        # 反向用例：id=8 的单行裁定后正常行不得进入冲突组
        if any(d[0] == 8 for d in detail):
            fails.append("D5 反向用例失守：单行 id=8 被误报为冲突组")
    finally:
        con.close()

    if fails:
        for f in fails:
            print("  ✗ %s" % f)
        print("自检 FAIL：%d 项不通过" % len(fails))
        return 1
    print("自检 PASS：D1 真重复 1/1、D2a 存量 2 行、D2b 裁定后 1 行（应 FAIL）、"
          "D3 1 行")
    print("           D4 正当三元组未误报、D5 冲突 1 组且单行 id 未误报")
    print("           （判据非空：夹具里同三元组不同 detail 的正当记录、"
          "裁定后的正常行若被误报，本件即失守）")
    return 0


def audit(path, cutoff=None):
    """体检指定库（只读）。返回退出码。"""
    global CUTOFF_DATE
    if cutoff:
        CUTOFF_DATE = cutoff
    if not os.path.exists(path):
        print("[exit 2] 库不存在：%s" % path)
        return 2
    con = duckdb.connect(path, read_only=True)
    try:
        miss = _schema_ok(con)
        if miss:
            print("[exit 2] %s 缺列：%s" % (TABLE, ", ".join(miss)))
            return 2
        total = _one(con, "SELECT COUNT(*) FROM %s" % TABLE)
        print("对象面：%s（%d 行，只读连接，裁定日 %s）"
              % (path, total, CUTOFF_DATE))
        print()

        fails = []

        g, rows, mx = _true_dupes(con)
        tag = "PASS" if g == 0 else "FAIL"
        print("D1 真重复（同 source_id/event_type/at/detail 多行）：%s —— %d 组、"
              "%d 行、最大组 %d 行" % (tag, g, rows, mx))
        if g:
            print("   明细：")
            for r in con.execute(
                    "SELECT source_id, event_type, %s, detail, COUNT(*) c FROM %s "
                    "GROUP BY source_id, event_type, %s, detail "
                    "HAVING COUNT(*)>1 ORDER BY c DESC LIMIT 15"
                    % (AT, TABLE, AT)).fetchall():
                print("    (%r, %r, %r) x%d  detail=%s" % (r[0], r[1], r[2], r[4],
                                                           r[3][:60]))
            fails.append("D1 命中真重复 %d 组" % g)

        t3, dv = _triplet_split(con)
        print("D4 三元组重复组 %d，其中 detail 分歧 %d 组、同内容 %d 组"
              "（分歧＝同批不同 claim 的正当形态，不计缺陷）"
              % (t3, dv, t3 - dv))

        fill = _null_id_by_writer(con)
        null_total = sum(r[1] for r in fill)
        pct = 100.0 * null_total / total if total else 0.0
        post_rows = sum(r[4] or 0 for r in fill)
        legacy_rows = null_total - post_rows

        print("D2a 裁定前空 id（存量债务，显式登记、不回填）：INFO —— %d / %d 行"
              "（%.2f%%）" % (legacy_rows, total, pct))
        print("   按写手（event_type）：")
        for ev, nid, tot, mx_at, npost in fill:
            if nid == 0:
                print("    %-24s %d/%-6d 全填" % (ev, nid, tot))
            else:
                mark = "全空" if nid == tot else "部分空 %d/%d" % (nid, tot)
                print("    %-24s %d/%-6d %s  最晚写入 %s"
                      % (ev, nid, tot, mark, mx_at))

        tag = "PASS" if post_rows == 0 else "FAIL"
        print("D2b 裁定日起空 id（违反统一约定）：%s —— %d 行" % (tag, post_rows))
        if post_rows:
            print("   明细：")
            for ev, nid, tot, mx_at, npost in fill:
                if npost:
                    print("    %-24s %d 行（该写手最晚写入 %s）" % (ev, npost, mx_at))
            fails.append("D2b 裁定日起空 id %d 行" % post_rows)

        ns = _null_source(con)
        tag = "WARN" if ns else "PASS"
        pct2 = 100.0 * ns / total if total else 0.0
        print("D3 source_id 空值：%s —— %d 行（%.2f%%）无法回溯到源"
              % (tag, ns, pct2))
        if ns:
            for ev, c in con.execute(
                    "SELECT event_type, COUNT(*) FROM %s WHERE source_id IS NULL "
                    "GROUP BY event_type ORDER BY 2 DESC" % TABLE).fetchall():
                print("    %-24s %d" % (ev, c))

        cg, cr, cpost, detail = _id_collisions(con)
        if cpost:
            print("D5 id 序列冲突：%s —— 共 %d 组 %d 行，其中裁定后 %d 组"
                  % ("FAIL", cg, cr, cpost))
            fails.append("D5 裁定日后 id 冲突 %d 组" % cpost)
        elif cg:
            print("D5 id 序列冲突：WARN —— %d 组 %d 行（均在裁定日前，存量形态）"
                  % (cg, cr))
        else:
            print("D5 id 序列冲突：PASS —— 0 组")
        if cg:
            for cid, c, mn, mx, post in detail:
                print("    id=%-8s x%-4d %s .. %s%s"
                      % (cid, c, mn, mx, "（裁定后）" if post else ""))
    finally:
        con.close()

    if fails:
        print()
        for f in fails:
            print("  ✗ %s" % f)
        print("FAIL：exit 1。D2a／D3／D5（裁定前）为存量形态，仅登记不阻断。")
        return 1
    print()
    print("PASS：D1 无真重复、D2b 无越界空 id、D5 无越界冲突（exit 0）。"
          "D2a／D3／D5（裁定前）为存量形态，仅登记不阻断。")
    return 0


def main():
    ap = argparse.ArgumentParser(
        description="provenance_history 审计表完整性门禁（只读）。"
                    "D1 真重复 FAIL；D2a 裁定前空 id 仅登记、D2b 裁定后空 id FAIL；"
                    "D3 source_id 空值 WARN；D4 三元组重复 INFO；"
                    "D5 id 冲突裁定后 FAIL／裁定前 WARN")
    ap.add_argument("--db", default=DEFAULT_DB, help="被体检的 DuckDB 库（只读）")
    ap.add_argument("--cutoff", default=CUTOFF_DATE, metavar="YYYY-MM-DD",
                    help="统一约定的裁定日（默认 %s；裁定日起新写入缺 id 即 FAIL）"
                         % CUTOFF_DATE)
    ap.add_argument("--selftest", action="store_true",
                    help="判据非空自检（内存夹具，不触碰活库）")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    return audit(a.db, cutoff=a.cutoff)


if __name__ == "__main__":
    sys.exit(main())
