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

判据（**只读连接**，本件不写活库）
----------------------------------
**D1 FAIL —— 真重复（幂等性失守）**
   `GROUP BY source_id, event_type, "at", detail HAVING COUNT(*)>1`。
   今天实测 0 组；>0 即判 FAIL。这是唯一真正表示「同一事件被写了两次」的形态。

**D2 WARN —— `id` 列填充率（结构性缺口）**
   按 `event_type` 分组统计 `id IS NULL`。今天实测：`claim_backfill` 4884/4884、
   `claim_fix` 3991/3993 全为空，而 `f2_*`／`w172_*` 家族全填充——**本表无可用
   主键**，不同写手对 `id` 的语义不一致，按 `id` 做幂等去重在本表上不成立。
   记 WARN 并给出写手级明细，供知情方决定是否统一写手约定。

**D3 WARN —— `source_id` 为空（无法回溯的审计行）**
   今天实测 483 行（`claim_backfill` 482 + `claim_fix` 1）无法回溯到源。
   记 WARN，不阻断——这是历史遗留写手的形态，非本次可治。

**D4 INFO —— 三元组重复但 detail 分歧（正当设计，非缺陷）**
   反向自证「按三元组判重复」是错的，见上。不参与退出码。

退出码
------
exit 0 ＝ D1 干净（D2／D3 仅告警）｜exit 1 ＝ D1 命中真重复｜exit 2 ＝ 依赖或
表缺失。**本件对活库只读**，`--db` 可指向任意库文件做只读体检。

用法
----
    python audit_provenance_dupes.py            # 体检现行 historical_claims
    python audit_provenance_dupes.py --db <库>   # 体检指定库（只读）
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
    """三元组重复组里，有多少组 detail 有分歧（即「伪重复」＝正当设计）。"""
    key3 = ', '.join(_q(c) for c in ("source_id", "event_type", "at"))
    total = _one(con, "SELECT COUNT(*) FROM (SELECT COUNT(*) c FROM %s GROUP BY %s "
                     "HAVING COUNT(*)>1)" % (TABLE, key3))
    divergent = _one(con, "SELECT COUNT(*) FROM (SELECT COUNT(*) c FROM %s "
                          "GROUP BY %s HAVING COUNT(*)>1 AND COUNT(DISTINCT detail)>1)"
                     % (TABLE, key3))
    return total, divergent


def _id_fill(con):
    """D2：按 event_type 统计 id 空值。返回 [(event_type, null, total), ...] 降序。"""
    return con.execute(
        "SELECT event_type, SUM(CASE WHEN id IS NULL THEN 1 ELSE 0 END), "
        "COUNT(*) FROM %s GROUP BY event_type ORDER BY 3 DESC" % TABLE
    ).fetchall()


def _null_source(con):
    """D3：source_id 为空的行数。"""
    return _one(con, "SELECT COALESCE(SUM(CASE WHEN source_id IS NULL "
                     "THEN 1 ELSE 0 END),0) FROM %s" % TABLE)


def _create_fixture(con):
    """建最小夹具：1 条真重复 + 1 组三元组同而 detail 异的正当记录。"""
    con.execute(
        'CREATE TABLE %s (id BIGINT, source_id VARCHAR, seq BIGINT,'
        ' event_type VARCHAR, detail VARCHAR, "at" VARCHAR)' % TABLE)
    rows = [
        # (a) 真重复：同键同 detail，写了两遍 → D1 应命中
        (1, "SRC-x.messages.1", 1, "batch_a", "claim.CL-1.claim_text: 甲", "t1"),
        (2, "SRC-x.messages.1", 1, "batch_a", "claim.CL-1.claim_text: 甲", "t1"),
        # (b) 正当记录：同三元组、detail 不同 → D1 不应命中
        (3, "SRC-y.messages.2", 1, "batch_b", "claim.CL-9.claim_text: 乙", "t2"),
        (4, "SRC-y.messages.2", 1, "batch_b", "claim.CL-10.claim_text: 丙", "t2"),
        # (c) 干净单条 + id 空 + source_id 空 → D2／D3 应命中
        (None, None, 1, "batch_c", "claim.CL-20.claim_text: 丁", "t3"),
    ]
    con.executemany(
        "INSERT INTO %s VALUES (?,?,?,?,?,?)" % TABLE, rows)


def selftest():
    """判据非空自检：真重复须命中、正当三元组须不误报、D2／D3 须报出。"""
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
        # 夹具两组合计 4 行：(SRC-x,batch_a,t1) 两行同 detail（真重复组）、
        # (SRC-y,batch_b,t2) 两行 detail 不同（正当三元组重复）→ t3=2、dv=1。
        if t3 != 2 or dv != 1:
            fails.append("D4 夹具应 2 组三元组重复、其中 1 组 detail 分歧，"
                         "实得 %d/%d" % (t3, dv))

        fill = _id_fill(con)
        if not any(r[1] == r[2] for r in fill):  # batch_c 的 id 全空
            fails.append("D2 应报出某写手 id 全空，实得 %s" % fill)
        if _null_source(con) != 1:
            fails.append("D3 应报 1 行 source_id 空，实得 %d" % _null_source(con))
    finally:
        con.close()

    if fails:
        for f in fails:
            print("  ✗ %s" % f)
        print("自检 FAIL：%d 项不通过" % len(fails))
        return 1
    print("自检 PASS：D1 真重复命中 1/1、正当三元组未误报、D2／D3 均报出")
    print("           （判据非空：夹具里那组同三元组不同 detail 的记录"
          "若被误判为重复，本件即失守）")
    return 0


def audit(path):
    """体检指定库（只读）。返回退出码。"""
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
        print("对象面：%s（%d 行，只读连接）" % (path, total))
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

        fill = _id_fill(con)
        null_total = sum(r[1] for r in fill)
        pct = 100.0 * null_total / total if total else 0.0
        tag = "WARN" if null_total else "PASS"
        print("D2 id 列空值：%s —— %d / %d 行（%.2f%%），本表无可用主键" %
              (tag, null_total, total, pct))
        print("   按写手（event_type）：")
        for ev, nid, tot in fill:
            mark = "全空" if nid == tot else ("全填" if nid == 0
                                              else "部分空 %d/%d" % (nid, tot))
            print("    %-22s %d/%-6d %s" % (ev, nid, tot, mark))

        ns = _null_source(con)
        tag = "WARN" if ns else "PASS"
        pct2 = 100.0 * ns / total if total else 0.0
        print("D3 source_id 空值：%s —— %d 行（%.2f%%）无法回溯到源"
              % (tag, ns, pct2))
        if ns:
            for ev, c in con.execute(
                    "SELECT event_type, COUNT(*) FROM %s WHERE source_id IS NULL "
                    "GROUP BY event_type ORDER BY 2 DESC" % TABLE).fetchall():
                print("    %-22s %d" % (ev, c))
    finally:
        con.close()

    if fails:
        print()
        for f in fails:
            print("  ✗ %s" % f)
        print("FAIL：%s（exit 1）。D2／D3 为存量形态、仅告警不阻断。" % TABLE)
        return 1
    print()
    print("PASS：无真重复（D1）；D2／D3 为存量写手形态，仅告警（exit 0）")
    return 0


def main():
    ap = argparse.ArgumentParser(
        description="provenance_history 审计表完整性门禁（只读；D1 真重复 FAIL，"
                    "D2/D3 id／source_id 填充率 WARN）")
    ap.add_argument("--db", default=DEFAULT_DB, help="被体检的 DuckDB 库（只读）")
    ap.add_argument("--selftest", action="store_true",
                    help="判据非空自检（内存夹具，不触碰活库）")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    return audit(a.db)


if __name__ == "__main__":
    sys.exit(main())
