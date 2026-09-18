# -*- coding: utf-8 -*-
"""12 个 SQLite 数据库 → DuckDB 转换脚本（2026-08-25 用户决策）

规则：所有 SQLite 库（除 12-数据库备份/ 外）转为 DuckDB 主存储层。
跳过 FTS5 虚拟表及影子表，逐表行数校验，转换后 SQLite 原库归档至 12-数据库备份/ 后删除。
"""
import datetime
import gzip
import hashlib
import json
import os
import re
import shutil
import sqlite3
import sys
import time

import duckdb

BASE = r"d:\librebsd"
BACKUP_ROOT = os.path.join(BASE, "12-数据库备份")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
LOG = os.path.join(BASE, "script", "_sqlite_to_duckdb_log.jsonl")

sys.stdout.reconfigure(encoding="utf-8")

# 12 库：db_name -> (SQLite 相对路径, DuckDB 文件名)
SCOPE = {
    "changelog": (r"01-项目管理\00-变更记录\changelog.db", "changelog.duckdb"),
    "sacred_sources": (r"02-sacred源材料\sacred_sources.db", "sacred_sources.duckdb"),
    "original_sources": (r"03-原始史料库\original_sources.db", "original_sources.duckdb"),
    "research_notes": (r"04-现代研究文献\research_notes.db", "research_notes.duckdb"),
    "historical_claims": (r"04-现代研究文献\historical_claims.db", "historical_claims.duckdb"),
    "causal_graph": (r"04-现代研究文献\causal_graph.db", "causal_graph.duckdb"),
    "references_fulltext": (r"04-现代研究文献\05-参考文献全文数据库\references_fulltext.db", "references_fulltext.duckdb"),
    "doubts_standalone": (r"04-现代研究文献\06-存疑数据库\doubts_standalone.db", "doubts_standalone.duckdb"),
    "fact_checks": (r"07-事实核查记录\fact_checks.db", "fact_checks.duckdb"),
    "review_reports": (r"08-核查报告与多轮复核\review_reports.db", "review_reports.duckdb"),
    "cross_indexes": (r"10-交叉索引\cross_indexes.db", "cross_indexes.duckdb"),
    "metadata_interfaces": (r"11-元数据接口\metadata_interfaces.db", "metadata_interfaces.duckdb"),
}

FTS_SHADOW_SUFFIXES = ("", "_data", "_idx", "_docsize", "_config", "_content")

TYPE_MAP = {"INTEGER": "BIGINT", "INT": "BIGINT", "BIGINT": "BIGINT", "TINYINT": "TINYINT",
            "SMALLINT": "SMALLINT", "UNSIGNED BIG INT": "BIGINT", "REAL": "DOUBLE",
            "FLOAT": "DOUBLE", "DOUBLE": "DOUBLE", "TEXT": "VARCHAR", "": "VARCHAR",
            "BLOB": "BLOB", "BOOLEAN": "BOOLEAN", "DATETIME": "VARCHAR"}


def log(msg):
    print("[{}] {}".format(datetime.datetime.now().strftime("%H:%M:%S"), msg), flush=True)


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def discover_tables(con):
    rows = con.execute(
        "SELECT name, sql FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'").fetchall()
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


def convert_one(name):
    src_rel, dk_fn = SCOPE[name]
    src_path = os.path.join(BASE, src_rel)
    src_dir = os.path.dirname(src_path)
    dst_path = os.path.join(src_dir, dk_fn)

    if not os.path.exists(src_path):
        log(f"[跳过] {name} 源不存在")
        return None

    # WAL 恢复
    con = sqlite3.connect(src_path, timeout=60)
    con.execute("PRAGMA wal_checkpoint(TRUNCATE)")
    integrity = con.execute("PRAGMA quick_check").fetchone()[0]
    if integrity != "ok":
        log(f"[异常] {name} integrity={integrity}")
        con.close()
        return None

    if os.path.exists(dst_path):
        os.remove(dst_path)

    t_all = time.time()
    rec = {"db_name": name, "op": "convert", "started_at": datetime.datetime.now().isoformat(),
           "source": src_rel, "duckdb": os.path.relpath(dst_path, BASE),
           "source_size_mb": round(os.path.getsize(src_path) / 1048576, 1), "tables": {}}

    dk = duckdb.connect(dst_path)
    dk.execute("SET memory_limit='8GB'")
    try:
        import pandas as pd
        tables, skipped = discover_tables(con)
        rec["skipped"] = skipped
        for t in tables:
            t0 = time.time()
            cols = con.execute("PRAGMA table_info('{}')".format(t)).fetchall()
            names = [c[1] for c in cols]
            # SQLite 灵活类型允许 INTEGER 列存 TEXT，DuckDB 严格类型会报错
            # 统一用 VARCHAR 避免类型转换失败
            dk.execute('CREATE TABLE "{}" ({})'.format(t, ", ".join(
                '"{}" VARCHAR'.format(n) for n in names)))
            total = 0
            first = True
            for chunk in pd.read_sql_query('SELECT * FROM "{}"'.format(t), con, chunksize=200000):
                if first:
                    dk.register("_etl_chunk", chunk)
                    dk.execute('INSERT INTO "{}" SELECT * FROM _etl_chunk'.format(t))
                    dk.unregister("_etl_chunk")
                    first = False
                else:
                    dk.append(t, chunk)
                total += len(chunk)
            src_n = con.execute('SELECT count(*) FROM "{}"'.format(t)).fetchone()[0]
            dst_n = dk.execute('SELECT count(*) FROM "{}"'.format(t)).fetchone()[0]
            ok = src_n == dst_n == total
            rec["tables"][t] = {"rows": total, "src_count": src_n, "dst_count": dst_n, "match": ok,
                                "sec": round(time.time() - t0, 1)}
            print("  {:<40} {:>12,} 行 {:>7.1f}s {}".format(t, total, time.time() - t0,
                                                             "OK" if ok else "MISMATCH"))
        dk.execute("CHECKPOINT")
    finally:
        dk.close()
        con.close()

    rec["finished_at"] = datetime.datetime.now().isoformat()
    rec["total_sec"] = round(time.time() - t_all, 1)
    rec["duckdb_size_mb"] = round(os.path.getsize(dst_path) / 1048576, 1)
    rec["all_match"] = all(v["match"] for v in rec["tables"].values())
    with open(LOG, "a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    log("[转换] {} {}MB -> {}MB ({:.1f}%) {}s {}".format(
        name, rec["source_size_mb"], rec["duckdb_size_mb"],
        rec["duckdb_size_mb"] / rec["source_size_mb"] * 100 if rec["source_size_mb"] else 0,
        rec["total_sec"], "全部一致" if rec["all_match"] else "存在不一致"))
    return rec


def archive_one(name):
    """备份 SQLite 原库至 12-数据库备份/ 后删除"""
    src_rel, _ = SCOPE[name]
    src_path = os.path.join(BASE, src_rel)
    if not os.path.exists(src_path):
        return None
    db_dir = os.path.join(BACKUP_ROOT, name)
    os.makedirs(db_dir, exist_ok=True)
    gz = os.path.join(db_dir, "ARCHIVE_FINAL_{}.db.gz".format(TS))
    sha = sha256_of(src_path)
    with open(src_path, "rb") as f_in, gzip.open(gz, "wb", compresslevel=6) as f_out:
        shutil.copyfileobj(f_in, f_out, 1 << 20)
    with gzip.open(gz, "rb") as f:
        while f.read(1 << 20):
            pass
    m = {"op": "archive_final", "db_name": name, "source_path": src_rel,
         "archive_file": os.path.basename(gz), "timestamp": TS,
         "source_size_bytes": os.path.getsize(src_path),
         "archive_size_bytes": os.path.getsize(gz),
         "sha256_uncompressed": sha, "sha256_gz": sha256_of(gz)}
    with open(gz.replace(".db.gz", ".json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(m, f, ensure_ascii=False, indent=2)
    freed = os.path.getsize(src_path)
    for suf in ("", "-wal", "-shm", "-journal"):
        p = src_path + suf
        if os.path.exists(p):
            freed += os.path.getsize(p)
            os.remove(p)
    log("[归档] {} {}MB -> {} {}MB，释放 {:.1f}MB".format(
        name, m["source_size_bytes"] / 1048576, os.path.basename(gz),
        m["archive_size_bytes"] / 1048576, freed / 1048576))
    return m


def main():
    for name in SCOPE:
        rec = convert_one(name)
        if rec and rec["all_match"]:
            archive_one(name)
        elif rec:
            log("[警告] {} 行数不一致，跳过归档".format(name))
    log("全部完成")


if __name__ == "__main__":
    main()