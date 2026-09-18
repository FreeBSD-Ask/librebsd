# -*- coding: utf-8 -*-
"""SQLite → DuckDB 转换、优化与主存储层管理脚本（固定脚本）

规则来源：00-编纂规则与格式规范/01-规则/流程规则.md“DuckDB 分析层与主存储层规则（2026-08-18）”
架构（2026-08-18 用户批准，15 库升格主存储层）：
  登记 15 库：DuckDB = 主存储层（唯一工作副本，可写），SQLite 原库已归档
  （12-数据库备份/<name>/ARCHIVE_FINAL_*.db.gz，永久留存）后自工作区删除；
  其余数据库：SQLite 仍为唯一主存储层，不涉本脚本。
  依据 PoC（dragonfly.db）：856MB → 131MB（15.3%），聚合查询 6~180 倍加速。

用法：
  python sqlite2duckdb.py --all          # 转换登记范围内全部库（须 SQLite 源在档）
  python sqlite2duckdb.py --db netbsd    # 单库转换（db_name 见 SCOPE）
  python sqlite2duckdb.py --optimize     # 15 库优化：OPTIMIZE 压实 + ANALYZE + ART 索引 + manifest 刷新
  python sqlite2duckdb.py --optimize --db netbsd  # 单库优化
  python sqlite2duckdb.py --verify       # 行数校验（在档库比对 SQLite 源；已归档库比对 manifest）
  python sqlite2duckdb.py --list         # 状态清单（在档最新/过期/已归档）
"""
import argparse
import datetime
import json
import os
import re
import sqlite3
import sys
import time

import duckdb

BASE = r"d:\librebsd"
LOG_JSONL = os.path.join(BASE, "script", "_duckdb_sync_log.jsonl")

# 转换范围登记簿：db_name -> SQLite 相对路径（2026-08-18 首批：11 代码仓库库 + 4 邮件合并库）
SCOPE = {
    "freebsd": r"03-原始史料库\01-代码仓库史料\02-FreeBSD\db\freebsd.db",
    "netbsd": r"03-原始史料库\01-代码仓库史料\03-NetBSD\db\netbsd.db",
    "openbsd": r"03-原始史料库\01-代码仓库史料\04-OpenBSD\db\openbsd.db",
    "dragonfly": r"03-原始史料库\01-代码仓库史料\05-DragonFlyBSD\db\dragonfly.db",
    "openzfs": r"03-原始史料库\01-代码仓库史料\06-OpenZFS\db\openzfs.db",
    "bsd-derivatives": r"03-原始史料库\01-代码仓库史料\07-BSD衍生项目\db\bsd-derivatives.db",
    "illumos-gate": r"03-原始史料库\01-代码仓库史料\08-跨项目对比\db\illumos-gate.db",
    "openssh": r"03-原始史料库\01-代码仓库史料\08-跨项目对比\db\openssh.db",
    "openssh-apple": r"03-原始史料库\01-代码仓库史料\08-跨项目对比\db\openssh-apple.db",
    "darwin": r"03-原始史料库\01-代码仓库史料\09-Darwin\db\darwin.db",
    "linux-kernel": r"03-原始史料库\01-代码仓库史料\10-LinuxKernel\db\linux-kernel.db",
    "openbsd_mail": r"03-原始史料库\11-邮件列表史料\03-openbsd\openbsd_mail.db",
    "dragonfly_mail": r"03-原始史料库\11-邮件列表史料\04-dragonfly\dragonfly_mail.db",
    "other-bsd_mail": r"03-原始史料库\11-邮件列表史料\06-other-bsd\other-bsd_mail.db",
    "usenet_mail": r"03-原始史料库\11-邮件列表史料\07-usenet\usenet_mail.db",
}

# FTS5 影子表后缀（虚拟表本体 + 五类影子表一并跳过）
FTS_SHADOW_SUFFIXES = ("", "_data", "_idx", "_docsize", "_config", "_content")

TYPE_MAP = {"INTEGER": "BIGINT", "INT": "BIGINT", "BIGINT": "BIGINT", "TINYINT": "TINYINT",
            "SMALLINT": "SMALLINT", "UNSIGNED BIG INT": "BIGINT", "REAL": "DOUBLE",
            "FLOAT": "DOUBLE", "DOUBLE": "DOUBLE", "TEXT": "VARCHAR", "": "VARCHAR",
            "BLOB": "BLOB"}


def mirror_path(db_name):
    """主库位置：与原 SQLite 同目录下 duckdb/ 子目录，<db_name>.duckdb"""
    src = os.path.join(BASE, SCOPE[db_name])
    return os.path.join(os.path.dirname(src), "duckdb", db_name + ".duckdb")


def manifest_path(db_name):
    """manifest 位置：逐表行数清单，--optimize 刷新，--verify 归档态校验基准"""
    return mirror_path(db_name).replace(".duckdb", ".manifest.json")


def src_exists(db_name):
    return os.path.exists(os.path.join(BASE, SCOPE[db_name]))


def is_archived(db_name):
    """已归档 = SQLite 源不在档且 manifest 存在（ARCHIVE_FINAL 归档态）"""
    return (not src_exists(db_name)) and os.path.exists(manifest_path(db_name))


# ART 索引计划：等值点查热点列（JOIN 走 hash join 不依赖索引；此计划服务高选择性点查）
INDEX_PLAN = {
    "commits": ("commit_hash",),
    "commit_files": ("commit_hash",),
    "messages": ("message_id",),
}


def write_manifest(db_name, dk):
    """将逐表行数写入 manifest（归档态 --verify 的唯一基准）"""
    tables = [r[0] for r in dk.execute(
        "SELECT table_name FROM information_schema.tables WHERE table_schema='main'").fetchall()]
    counts = {}
    for t in tables:
        counts[t] = dk.execute('SELECT count(*) FROM "{}"'.format(t)).fetchone()[0]
    m = {"db_name": db_name, "generated_at": datetime.datetime.now().isoformat(),
         "duckdb_file": os.path.relpath(mirror_path(db_name), BASE), "table_rows": counts,
         "duckdb_size_mb": round(os.path.getsize(mirror_path(db_name)) / 1048576, 1)}
    with open(manifest_path(db_name), "w", encoding="utf-8", newline="\n") as f:
        json.dump(m, f, ensure_ascii=False, indent=2)
    return m


def optimize_one(db_name):
    """单库优化：OPTIMIZE 压实（行组重写压缩）→ ART 索引 → ANALYZE 统计 → manifest 刷新"""
    dst = mirror_path(db_name)
    if not os.path.exists(dst):
        print("[跳过] 主库不存在: {}".format(db_name))
        return None
    if is_archived(db_name):
        print("[归档态] {} SQLite 源已归档，--optimize 直接作用于 DuckDB 主库".format(db_name))
    t0 = time.time()
    dk = duckdb.connect(dst)
    dk.execute("SET memory_limit='8GB'")
    rec = {"db_name": db_name, "op": "optimize", "started_at": datetime.datetime.now().isoformat(),
           "size_before_mb": round(os.path.getsize(dst) / 1048576, 1), "indexes": {}}
    try:
        t1 = time.time()
        # DuckDB 1.5.5 无 OPTIMIZE 语句；新建库无碎片，压实由 CHECKPOINT 完成（行组定稿 + WAL 收敛）
        dk.execute("CHECKPOINT")
        rec["optimize_sec"] = round(time.time() - t1, 1)
        tables = [r[0] for r in dk.execute(
            "SELECT table_name FROM information_schema.tables WHERE table_schema='main'").fetchall()]
        for t in tables:
            for col in INDEX_PLAN.get(t, ()):
                t1 = time.time()
                idx = "idx_{}_{}".format(t, col)
                dk.execute('CREATE INDEX IF NOT EXISTS "{}" ON "{}"("{}")'.format(idx, t, col))
                rec["indexes"][idx] = round(time.time() - t1, 1)
        t1 = time.time()
        dk.execute("ANALYZE")
        rec["analyze_sec"] = round(time.time() - t1, 1)
        dk.execute("CHECKPOINT")
        m = write_manifest(db_name, dk)
        rec["manifest_tables"] = len(m["table_rows"])
    finally:
        dk.close()
    rec["finished_at"] = datetime.datetime.now().isoformat()
    rec["total_sec"] = round(time.time() - t0, 1)
    rec["size_after_mb"] = round(os.path.getsize(dst) / 1048576, 1)
    with open(LOG_JSONL, "a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print("[优化] {} {}MB -> {}MB，{}s，索引 {} 个 {}".format(
        db_name, rec["size_before_mb"], rec["size_after_mb"], rec["total_sec"],
        len(rec["indexes"]), "（{}）".format(", ".join("{}:{:.0f}s".format(k, v) for k, v in rec["indexes"].items())) if rec["indexes"] else ""))
    return rec


def discover_tables(con):
    """返回（实体表清单, 跳过清单）。跳过：sqlite_ 内部表、FTS5 虚拟表及其影子表。"""
    rows = con.execute(
        "SELECT name, sql FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"
    ).fetchall()
    virtual = set()
    for name, sql in rows:
        if sql and re.search(r"CREATE\s+VIRTUAL\s+TABLE", sql, re.IGNORECASE):
            virtual.add(name)
    skip = set()
    for vt in virtual:
        for suf in FTS_SHADOW_SUFFIXES:
            skip.add(vt + suf)
    tables = [n for n, _ in rows if n not in skip]
    return tables, sorted(skip)


def convert_one(db_name):
    src_path = os.path.join(BASE, SCOPE[db_name])
    dst_path = mirror_path(db_name)
    if not os.path.exists(src_path):
        print("[跳过] 源不存在: {}".format(db_name))
        return None
    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    if os.path.exists(dst_path):
        os.remove(dst_path)
    rec = {"db_name": db_name, "op": "convert", "started_at": datetime.datetime.now().isoformat(),
           "source": SCOPE[db_name], "mirror": os.path.relpath(dst_path, BASE), "tables": {}}
    t_all = time.time()
    sq = sqlite3.connect("file:{}?mode=ro".format(src_path), uri=True)
    dk = duckdb.connect(dst_path)
    dk.execute("SET memory_limit='8GB'")
    dk.execute("SET preserve_insertion_order=false")
    try:
        import pandas as pd
        tables, skipped = discover_tables(sq)
        rec["skipped_fts_objects"] = skipped
        for t in tables:
            t0 = time.time()
            cols = sq.execute('PRAGMA table_info("{}")'.format(t)).fetchall()
            names = [c[1] for c in cols]
            ddl_cols = ", ".join('"{}" {}'.format(n, TYPE_MAP.get(c[2].upper(), "VARCHAR"))
                                 for n, c in zip(names, cols))
            dk.execute('CREATE TABLE "{}" ({})'.format(t, ddl_cols))
            total = 0
            first = True
            for chunk in pd.read_sql_query('SELECT * FROM "{}"'.format(t), sq, chunksize=200000):
                if first:
                    # 首块走 register + INSERT（按建表 DDL 类型落库），其后逐块 append（Arrow 批量路径）
                    dk.register("_etl_chunk", chunk)
                    dk.execute('INSERT INTO "{}" SELECT * FROM _etl_chunk'.format(t))
                    dk.unregister("_etl_chunk")
                    first = False
                else:
                    dk.append(t, chunk)
                total += len(chunk)
            src_n = sq.execute('SELECT count(*) FROM "{}"'.format(t)).fetchone()[0]
            dst_n = dk.execute('SELECT count(*) FROM "{}"'.format(t)).fetchone()[0]
            ok = src_n == dst_n == total
            rec["tables"][t] = {"rows": total, "src_count": src_n, "dst_count": dst_n, "match": ok,
                                "sec": round(time.time() - t0, 1)}
            print("  {:-<40} {:>12,} 行 {:>7.1f}s {}".format(t, total, time.time() - t0,
                                                             "OK" if ok else "MISMATCH"))
        dk.execute("CHECKPOINT")
    finally:
        dk.close()
        sq.close()
    rec["finished_at"] = datetime.datetime.now().isoformat()
    rec["total_sec"] = round(time.time() - t_all, 1)
    rec["source_size_mb"] = round(os.path.getsize(src_path) / 1048576, 1)
    rec["mirror_size_mb"] = round(os.path.getsize(dst_path) / 1048576, 1)
    rec["all_match"] = all(v["match"] for v in rec["tables"].values())
    with open(LOG_JSONL, "a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print("[转换] {} {}MB -> {}MB（{:.1f}%） {}s {}".format(
        db_name, rec["source_size_mb"], rec["mirror_size_mb"],
        rec["mirror_size_mb"] / rec["source_size_mb"] * 100 if rec["source_size_mb"] else 0,
        rec["total_sec"], "全部一致" if rec["all_match"] else "存在不一致"))
    return rec


def verify_one(db_name):
    src_path = os.path.join(BASE, SCOPE[db_name])
    dst_path = mirror_path(db_name)
    if not os.path.exists(dst_path):
        print("[校验] {} 主库缺失".format(db_name))
        return False
    # 归档态：按 manifest 逐表行数校验
    if not os.path.exists(src_path):
        mp = manifest_path(db_name)
        if not os.path.exists(mp):
            print("[校验] {} SQLite 源不在档且无 manifest，无法校验".format(db_name))
            return False
        m = json.load(open(mp, encoding="utf-8"))
        dk = duckdb.connect(dst_path, read_only=True)
        all_ok = True
        for t, exp in m["table_rows"].items():
            try:
                dst_n = dk.execute('SELECT count(*) FROM "{}"'.format(t)).fetchone()[0]
            except Exception as e:
                print("  [校验] {} {} 表异常: {}".format(db_name, t, e))
                all_ok = False
                continue
            if dst_n != exp:
                print("  [校验] {} {} manifest {:,} != 主库 {:,}".format(db_name, t, exp, dst_n))
                all_ok = False
        dk.close()
        print("[校验] {}（归档态，基准 manifest {}）{}".format(
            db_name, m["generated_at"][:19], "一致" if all_ok else "不一致"))
        return all_ok
    # 在档态：源-镜像行数比对
    sq = sqlite3.connect("file:{}?mode=ro".format(src_path), uri=True)
    dk = duckdb.connect(dst_path, read_only=True)
    tables, _ = discover_tables(sq)
    all_ok = True
    for t in tables:
        try:
            src_n = sq.execute('SELECT count(*) FROM "{}"'.format(t)).fetchone()[0]
            dst_n = dk.execute('SELECT count(*) FROM "{}"'.format(t)).fetchone()[0]
        except Exception as e:
            print("  [校验] {} {} 表缺失/异常: {}".format(db_name, t, e))
            all_ok = False
            continue
        ok = src_n == dst_n
        all_ok = all_ok and ok
        if not ok:
            print("  [校验] {} {} 源 {:,} != 主库 {:,}".format(db_name, t, src_n, dst_n))
    sq.close()
    dk.close()
    print("[校验] {} {}".format(db_name, "一致" if all_ok else "不一致（须重新同步）"))
    return all_ok


def cmd_list():
    print("{:<18} {:>10} {:>10} {:>12} {}".format("db_name", "SQLiteMB", "主库MB", "主库修改时间", "状态"))
    for name in sorted(SCOPE):
        src = os.path.join(BASE, SCOPE[name])
        dst = mirror_path(name)
        if os.path.exists(dst):
            d_mb = os.path.getsize(dst) / 1048576
            mtime = datetime.datetime.fromtimestamp(os.path.getmtime(dst)).strftime("%m-%d %H:%M")
            if not os.path.exists(src):
                status = "已归档（主存储层）"
                s_mb = -1.0
            else:
                s_mb = os.path.getsize(src) / 1048576
                stale = os.path.getmtime(dst) < os.path.getmtime(src)
                status = "过期（源已更新）" if stale else "最新"
        else:
            s_mb = os.path.getsize(src) / 1048576 if os.path.exists(src) else -1.0
            d_mb, mtime, status = -1.0, "-", "未建立"
        print("{:<18} {:>10.1f} {:>10.1f} {:>12} {}".format(name, s_mb, d_mb, mtime, status))


def main():
    ap = argparse.ArgumentParser(description="SQLite → DuckDB 转换、优化与主存储层管理")
    ap.add_argument("--all", action="store_true", help="转换登记范围内全部库（须 SQLite 源在档）")
    ap.add_argument("--db", metavar="<db_name>", help="单库操作（转换，或配合 --optimize 单库优化）")
    ap.add_argument("--optimize", action="store_true", help="优化：OPTIMIZE+索引+ANALYZE+manifest（全范围或配合 --db）")
    ap.add_argument("--verify", action="store_true", help="行数校验（在档比源，归档比 manifest）")
    ap.add_argument("--list", action="store_true", help="状态清单")
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    if args.list:
        cmd_list()
        return 0
    if args.verify:
        results = [verify_one(n) for n in sorted(SCOPE)]
        bad = [n for n, r in zip(sorted(SCOPE), results) if not r]
        print("校验完成：{} 库，不一致/缺失 {} 库{}".format(
            len(results), len(bad), "（" + ", ".join(bad) + "）" if bad else ""))
        return 1 if bad else 0
    if args.db and args.db not in SCOPE:
        print("未知库名: {}（可用：{}）".format(args.db, ", ".join(SCOPE)))
        return 1
    if args.optimize:
        names = [args.db] if args.db else list(SCOPE)
        for n in names:
            optimize_one(n)
        print("优化完成：{} 库".format(len(names)))
        return 0
    if args.all or args.db:
        names = list(SCOPE) if args.all else [args.db]
        bad = []
        for n in names:
            if is_archived(n):
                print("[跳过] {} 已归档：转换须先自 12-数据库备份/<name>/ARCHIVE_FINAL_*.db.gz 恢复 SQLite（流程规则“更新与写入流程”）".format(n))
                continue
            rec = convert_one(n)
            if rec and not rec["all_match"]:
                bad.append(n)
        print("转换完成：{} 库，行数不一致 {} 库".format(len(names), len(bad)))
        return 1 if bad else 0
    ap.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
