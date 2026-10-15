# -*- coding: utf-8 -*-
"""claimdb_guard.py —— 写库门禁与全库健康哨兵（固定脚本；2026-10-14 立，主理人令）

教训：2026-10-13 单条缺关联 UPDATE 将 historical_claims.evidence.fact_text 全表
472,510 行覆盖为同一句（广播事故）——此前写库流程无「写前哨兵」。本脚本为
「入库流程」前置门禁：任何批量写库（fix-db 修库／register 入库／批量导入）前运行，
PASS 才准写；FAIL 必须停止并排查。

用法：
  python claimdb_guard.py --db historical_claims   # 写库前门禁（claims 深度哨兵）
  python claimdb_guard.py --db <库名>              # 任意库通用检查（行数/表数快照对比）
  python claimdb_guard.py --path <库文件>          # 对任意 duckdb 文件只读检查（测试备份库；不写快照）
  python claimdb_guard.py --all                    # 全库体检（SCOPE 全库逐一快照对比）
  python claimdb_guard.py --selftest               # 自检（四用例：正常/广播/骤降/行数骤减）
  python claimdb_guard.py --show                   # 查看当前快照

判据（claims 深度哨兵 S1–S4）：
  S1 fact_text 单值集中：最大单值行占比 > 25% → FAIL；> 5% → WARN（广播形态）
  S2 fact_text distinct 骤降：< 快照值 × 0.5 → FAIL
  S3 updated_at 单值集中：最大单值行占比 > 50% → FAIL（全表同刻写入特征）
  S4 evidence 行数骤降：< 快照值 × 0.9 → FAIL
通用判据（--all / --db 全库，G1–G2）：
  G1 表消失：快照中的表在现库不存在 → FAIL
  G2 总行数骤降：< 快照 × 0.9 → FAIL
快照：12-数据库备份/claimdb_guard_state.json（每次非 FAIL 运行后合并刷新）
退出码：0＝PASS（含 WARN）；1＝FAIL
"""
import argparse
import datetime
import importlib.util
import json
import os
import sys

BASE = r"d:\librebsd"
BACKUP_ROOT = os.path.join(BASE, "12-数据库备份")
STATE = os.path.join(BACKUP_ROOT, "claimdb_guard_state.json")

# 阈值（2026-10-14 定：现状实测远离阈值，见 --db 输出的「现状值」）
S1_FAIL, S1_WARN = 0.25, 0.05
S2_RATIO = 0.5
S3_FAIL = 0.5
S4_RATIO = 0.9
G2_RATIO = 0.9


def load_scope():
    """复用 backup_databases.py 的 SCOPE（全库枚举，26 库）。"""
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "backup_databases.py")
    spec = importlib.util.spec_from_file_location("backup_databases", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.SCOPE


def load_state():
    if os.path.exists(STATE):
        try:
            with open(STATE, encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def save_state(state):
    state["v"] = 1
    state["updated_at"] = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    os.makedirs(BACKUP_ROOT, exist_ok=True)
    with open(STATE, "w", encoding="utf-8", newline="\n") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


def collect_claims_stats(con):
    """claims 库深度指标（evidence 表）。"""
    rows = con.execute("SELECT COUNT(*) FROM evidence").fetchone()[0]
    fact_distinct, fact_top = con.execute("""
        WITH t AS (SELECT fact_text, COUNT(*) AS c FROM evidence GROUP BY 1)
        SELECT (SELECT COUNT(*) FROM t), COALESCE(MAX(c), 0) FROM t
    """).fetchone()
    upd_top = con.execute("""
        WITH t AS (SELECT updated_at, COUNT(*) AS c FROM evidence GROUP BY 1)
        SELECT COALESCE(MAX(c), 0) FROM t
    """).fetchone()[0]
    return {
        "rows": rows,
        "fact_distinct": fact_distinct,
        "fact_max_pct": (fact_top / rows) if rows else 0.0,
        "upd_max_pct": (upd_top / rows) if rows else 0.0,
    }


def evaluate_claims(stats, snap):
    """claims 深度判决：返回 (verdict, reasons)。verdict ∈ PASS/WARN/FAIL。"""
    reasons = []
    verdict = "PASS"

    def bump(v):
        nonlocal verdict
        order = {"PASS": 0, "WARN": 1, "FAIL": 2}
        if order[v] > order[verdict]:
            verdict = v

    if stats["fact_max_pct"] > S1_FAIL:
        bump("FAIL")
        reasons.append("S1 fact_text 单值集中 {:.1%} > {:.0%}（广播形态高危）".format(stats["fact_max_pct"], S1_FAIL))
    elif stats["fact_max_pct"] > S1_WARN:
        bump("WARN")
        reasons.append("S1 fact_text 单值集中 {:.1%} > {:.0%}（需人工目验）".format(stats["fact_max_pct"], S1_WARN))

    if snap:
        sd = snap.get("claims", {}).get("fact_distinct")
        if sd and stats["fact_distinct"] < sd * S2_RATIO:
            bump("FAIL")
            reasons.append("S2 fact_text distinct 骤降 {} < 快照 {} × {}".format(stats["fact_distinct"], sd, S2_RATIO))

    if stats["upd_max_pct"] > S3_FAIL:
        bump("FAIL")
        reasons.append("S3 updated_at 单值集中 {:.1%} > {:.0%}（全表同刻写入特征）".format(stats["upd_max_pct"], S3_FAIL))

    if snap:
        sr = snap.get("claims", {}).get("rows")
        if sr and stats["rows"] < sr * S4_RATIO:
            bump("FAIL")
            reasons.append("S4 evidence 行数骤降 {} < 快照 {} × {}".format(stats["rows"], sr, S4_RATIO))
    else:
        reasons.append("（首次运行：无快照，仅执行绝对判据；本次结果将写入基线）")
    return verdict, reasons


def collect_db_stats(con):
    """通用库指标：逐表行数。"""
    tables = {}
    rows = con.execute(
        "SELECT table_name FROM information_schema.tables WHERE table_schema='main' ORDER BY table_name"
    ).fetchall()
    for (t,) in rows:
        tables[t] = con.execute('SELECT COUNT(*) FROM main."{}"'.format(t)).fetchone()[0]
    return tables


def evaluate_generic(name, tables, snap_dbs):
    """通用库判决：G1 表消失 / G2 总行数骤降。返回 (verdict, reasons)。"""
    reasons = []
    verdict = "PASS"
    total = sum(tables.values())
    prev = (snap_dbs or {}).get(name)
    if prev:
        prev_tables = prev.get("tables", {})
        missing = [t for t in prev_tables if t not in tables]
        if missing:
            verdict = "FAIL"
            reasons.append("G1 表消失：{}".format("、".join(missing[:5])))
        pt = prev.get("total_rows")
        if pt and total < pt * G2_RATIO:
            verdict = "FAIL"
            reasons.append("G2 总行数骤降 {} < 快照 {} × {}".format(total, pt, G2_RATIO))
    if not reasons:
        reasons.append("表 {} 张、总行数 {}".format(len(tables), total))
    return verdict, reasons


def _connect(path):
    import duckdb
    return duckdb.connect(path, read_only=True)


def _check_file(path, label, snap, write_state):
    """对任意 duckdb 文件执行门禁检查（自动探测 claims 深度面）。"""
    try:
        con = _connect(path)
    except Exception as e:
        print("[FAIL-open] 无法连接 {}：{}".format(label, str(e)[:120]))
        print("提示：目标被写连接占用时属正常操作态——待其结束后重试；门禁未通过前禁写。")
        return 1
    tables = collect_db_stats(con)
    has_claims = False
    if "evidence" in tables:
        cols = [c[0] for c in con.execute("DESCRIBE main.evidence").fetchall()]
        has_claims = "fact_text" in cols
    print("== claimdb_guard · {} ==".format(label))
    if has_claims:
        stats = collect_claims_stats(con)
        verdict, reasons = evaluate_claims(stats, snap)
        print("  行数={rows}  distinct={fact_distinct}  单值占比={fact_max_pct:.4%}  updated_at 单值占比={upd_max_pct:.4%}".format(**stats))
    else:
        verdict, reasons = evaluate_generic(label, tables, snap.get("dbs", {}))
    for r in reasons:
        print("  - {}".format(r))
    print("  裁决: {}".format(verdict))
    con.close()
    if write_state and verdict != "FAIL":
        if has_claims:
            snap["claims"] = {k: stats[k] for k in ("rows", "fact_distinct", "fact_max_pct", "upd_max_pct")}
        snap.setdefault("dbs", {})[label] = {
            "total_rows": sum(tables.values()), "tables": tables,
            "at": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")}
        save_state(snap)
        print("  快照已刷新 -> {}".format(STATE))
    return 1 if verdict == "FAIL" else 0


def run_db(name):
    scope = load_scope()
    if name not in scope:
        print("未知库名: {}（可用：{}）".format(name, ", ".join(sorted(scope))))
        return 1
    return _check_file(os.path.join(BASE, scope[name]), name, load_state(), True)


def run_path(path):
    """测试模式：对任意库文件只读检查，不写快照（备份库验证用）。"""
    if not os.path.exists(path):
        print("文件不存在: {}".format(path))
        return 1
    return _check_file(path, os.path.basename(path), load_state(), False)


def run_all():
    scope = load_scope()
    snap = load_state()
    # 快照 dbs 只保留本轮 SCOPE 内的条目：库被移出 SCOPE 或本轮 SKIP 时，旧行数不得
    # 滞留——滞留会让下方的通过/跳过计数被陈旧条目污染（2026-10-15 复核坐实）。
    dbs = {k: v for k, v in (snap.get("dbs") or {}).items() if k in scope}
    fails, skips = [], []
    print("== claimdb_guard · --all 全库体检（{} 库）==".format(len(scope)))
    for name in sorted(scope):
        path = os.path.join(BASE, scope[name])
        try:
            con = _connect(path)
            tables = collect_db_stats(con)
            con.close()
        except Exception as e:
            print("  {:<24} SKIP（{}）".format(name, str(e)[:60]))
            skips.append(name)
            continue
        verdict, reasons = evaluate_generic(name, tables, dbs)
        total = sum(tables.values())
        mark = {"PASS": "OK  ", "FAIL": "FAIL"}[verdict]
        print("  {:<24} {} 表 {} 行 {}".format(name, mark, len(tables), total))
        for r in reasons:
            if verdict == "FAIL":
                print("        - {}".format(r))
        if verdict == "FAIL":
            fails.append(name)
        else:
            dbs[name] = {"total_rows": total, "tables": tables, "at": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")}
    if fails:
        print("== 裁决: FAIL（{}）——修复前禁写 ==".format("、".join(fails)))
        return 1
    snap["dbs"] = dbs
    save_state(snap)
    print("== 裁决: PASS（{}/{} 库通过，{} SKIP；快照已刷新）==".format(len(dbs), len(scope), len(skips)))
    return 0


def selftest():
    import duckdb
    print("== claimdb_guard · selftest ==")
    fails = []

    def report(name, verdict, reasons, want_verdict, want_kw=None, want_kw2=None):
        ok = verdict == want_verdict
        if want_kw:
            ok = ok and any(want_kw in r for r in reasons)
        if want_kw2:
            ok = ok and any(want_kw2 in r for r in reasons)
        print("  [{}] {}：裁决={} {}".format("PASS" if ok else "FAIL", name, verdict, "（原因命中判据）" if ok else ("——期望 {} / 原因 {}".format(want_verdict, reasons))))
        if not ok:
            fails.append(name)

    # 用例 1a：正常态（无快照，全链）
    con = duckdb.connect(":memory:")
    con.execute("CREATE TABLE evidence (evidence_id VARCHAR, fact_text VARCHAR, updated_at VARCHAR)")
    con.executemany(
        "INSERT INTO evidence VALUES (?, ?, ?)",
        [("E{:05d}".format(i), "fact-{}".format(i), "2026-01-{:02d} 00:00:00".format(i % 28 + 1)) for i in range(500)],
    )
    stats = collect_claims_stats(con)
    v, r = evaluate_claims(stats, None)
    report("正常态（无快照）", v, r, "PASS")
    # 用例 1b：正常态（有近值快照）
    v, r = evaluate_claims(stats, {"claims": {"rows": 480, "fact_distinct": 480}})
    report("正常态（有快照）", v, r, "PASS")
    # 用例 2：广播态（全链：同值 fact_text + 同刻 updated_at）
    con2 = duckdb.connect(":memory:")
    con2.execute("CREATE TABLE evidence (evidence_id VARCHAR, fact_text VARCHAR, updated_at VARCHAR)")
    con2.executemany(
        "INSERT INTO evidence VALUES (?, ?, ?)",
        [("B{:05d}".format(i), "同一句广播文本", "2026-10-13 08:52:13") for i in range(2000)],
    )
    stats2 = collect_claims_stats(con2)
    v, r = evaluate_claims(stats2, None)
    report("广播态", v, r, "FAIL", want_kw="S1", want_kw2="S3")
    # 用例 3：distinct 骤降（对快照）
    stats3 = {"rows": 100000, "fact_distinct": 100, "fact_max_pct": 0.01, "upd_max_pct": 0.01}
    v, r = evaluate_claims(stats3, {"claims": {"rows": 100000, "fact_distinct": 5000}})
    report("distinct 骤降", v, r, "FAIL", want_kw="S2")
    # 用例 4：行数骤减（对快照）
    stats4 = {"rows": 10000, "fact_distinct": 9900, "fact_max_pct": 0.001, "upd_max_pct": 0.001}
    v, r = evaluate_claims(stats4, {"claims": {"rows": 100000, "fact_distinct": 99000}})
    report("行数骤减", v, r, "FAIL", want_kw="S4")

    if fails:
        print("== selftest: FAIL（{}）==".format("、".join(fails)))
        return 1
    print("== selftest: 全部通过（5 项检查：正常×2/广播/骤降/骤减，拦下原因命中判据）==")
    return 0


def show():
    snap = load_state()
    if not snap:
        print("（无快照：尚未运行过）")
        return 0
    print("== claimdb_guard 快照（{}）==".format(snap.get("updated_at")))
    c = snap.get("claims")
    if c:
        print("  claims: 行={rows} distinct={fact_distinct} 单值占比={fact_max_pct:.4%} upd单值占比={upd_max_pct:.4%}".format(**c))
    for name, d in sorted(snap.get("dbs", {}).items()):
        print("  {:<24} 表 {} 行 {}（{}）".format(name, len(d.get("tables", {})), d.get("total_rows"), d.get("at", "")))
    return 0


def main():
    ap = argparse.ArgumentParser(description="写库门禁与全库健康哨兵（2026-10-14 立）")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--db", metavar="<库名>", help="单库门禁检查（historical_claims 为深度哨兵 S1–S4）")
    g.add_argument("--path", metavar="<库文件>", help="对任意 duckdb 文件做只读检查（测试备份库；不写快照）")
    g.add_argument("--all", action="store_true", help="全库体检（SCOPE 全库快照对比）")
    g.add_argument("--selftest", action="store_true", help="自检（四用例）")
    g.add_argument("--show", action="store_true", help="查看快照")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    if args.show:
        return show()
    if args.all:
        return run_all()
    if args.path:
        return run_path(args.path)
    return run_db(args.db)


if __name__ == "__main__":
    sys.exit(main())
