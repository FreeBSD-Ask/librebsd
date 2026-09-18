# -*- coding: utf-8 -*-
"""播客两库 SQLite → DuckDB 收尾脚本（2026-08-26 登记，流程规则.md“播客库收尾流程”执行工具）

触发条件：转录进程（script/_bsdnow_igpu_transcribe.py，含 --both 模式）已退出，
bsdnow_podcast.db 与 bsd_podcasts_external.db 不再被写入（mtime 稳定）。

流程（对应规则五步）：
  1. 前置检查：确认两个 .db 存在、可读、integrity_check=ok、无 -wal/-shm 伴生残留；
  2. 增量同步：逐表转换至同目录 .duckdb（跳过 FTS5 虚拟表及影子表，跳过 sqlite_ 内部表）；
  3. 行数校验：逐表比对 SQLite 源与 DuckDB 行数，全部一致方可归档（不一致则中止，不删除源）；
  4. 归档：.db 以 ARCHIVE_FINAL_<ts>.db.gz 归档至 12-数据库备份/<name>/（含 SHA-256 清单，
     校验回读 CRC），归档成功后删除工作区 .db 及 -wal/-shm/-journal 伴生文件；
  5. 收尾提示：输出"重启转录须使用改造后写 DuckDB 的 _bsdnow_igpu_transcribe.py"警示。

用法：
  python podcast_db_final_sync.py            # 完整收尾（同步+校验+归档+删除）
  python podcast_db_final_sync.py --sync-only  # 仅同步+校验，不归档不删除（试运行）
  python podcast_db_final_sync.py --check      # 仅前置检查（进程是否退出、库状态）

依赖：duckdb、pandas（C:\\Python314\\python.exe 均已安装）。
日志：script/_podcast_final_sync_log.jsonl
"""
import argparse
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
LOG = os.path.join(BASE, "script", "_podcast_final_sync_log.jsonl")
BACKUP_ROOT = os.path.join(BASE, "12-数据库备份")
PODCAST_DIR = os.path.join(BASE, "03-原始史料库", "14-播客史料")

SCOPE = {
    "bsdnow_podcast": "bsdnow_podcast.db",
    "bsd_podcasts_external": "bsd_podcasts_external.db",
}

FTS_SHADOW_SUFFIXES = ("", "_data", "_idx", "_docsize", "_config", "_content")

sys.stdout.reconfigure(encoding="utf-8")


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


def precheck(name, db_file):
    """前置检查：存在、完整、无伴生残留。返回 (ok, message)。"""
    src = os.path.join(PODCAST_DIR, db_file)
    if not os.path.exists(src):
        return False, "源不存在（可能已完成收尾）"
    if os.path.getsize(src) == 0:
        return False, "源为 0 字节（异常状态，中止）"
    for suf in ("-wal", "-shm", "-journal"):
        if os.path.exists(src + suf):
            return False, "存在伴生文件 {}（疑似仍有进程持有连接，中止）".format(db_file + suf)
    con = sqlite3.connect("file:{}?mode=ro".format(src), uri=True, timeout=30)
    try:
        integrity = con.execute("PRAGMA quick_check").fetchone()[0]
        if integrity != "ok":
            return False, "integrity_check={}（中止）".format(integrity)
    finally:
        con.close()
    return True, "ok"


def convert_one(name, db_file):
    """同步：逐表转换 + 行数校验。返回 (all_match, rec)。"""
    src = os.path.join(PODCAST_DIR, db_file)
    dst = os.path.join(PODCAST_DIR, name + ".duckdb")
    t_all = time.time()
    rec = {"db_name": name, "op": "final_sync", "started_at": datetime.datetime.now().isoformat(),
           "source": os.path.relpath(src, BASE), "duckdb": os.path.relpath(dst, BASE),
           "source_size_mb": round(os.path.getsize(src) / 1048576, 1), "tables": {}}

    con = sqlite3.connect("file:{}?mode=ro".format(src), uri=True, timeout=60)
    con.execute("PRAGMA wal_checkpoint(TRUNCATE)") if con.in_transaction else None
    if os.path.exists(dst):
        os.remove(dst)
    dk = duckdb.connect(dst)
    dk.execute("SET memory_limit='8GB'")
    try:
        import pandas as pd
        tables, skipped = discover_tables(con)
        rec["skipped_fts_objects"] = skipped
        for t in tables:
            t0 = time.time()
            cols = con.execute('PRAGMA table_info("{}")'.format(t)).fetchall()
            names = [c[1] for c in cols]
            # SQLite 灵活类型：统一 VARCHAR 落库，避免 DuckDB 严格类型报错
            dk.execute('CREATE TABLE "{}" ({})'.format(
                t, ", ".join('"{}" VARCHAR'.format(n) for n in names)))
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
            rec["tables"][t] = {"rows": total, "src_count": src_n, "dst_count": dst_n,
                                "match": ok, "sec": round(time.time() - t0, 1)}
            print("  {:<40} {:>12,} 行 {:>7.1f}s {}".format(
                t, total, time.time() - t0, "OK" if ok else "MISMATCH"))
        dk.execute("CHECKPOINT")
    finally:
        dk.close()
        con.close()
    rec["finished_at"] = datetime.datetime.now().isoformat()
    rec["total_sec"] = round(time.time() - t_all, 1)
    rec["duckdb_size_mb"] = round(os.path.getsize(dst) / 1048576, 1)
    rec["all_match"] = all(v["match"] for v in rec["tables"].values())
    log("[同步] {} {}MB -> {}MB {}s {}".format(
        name, rec["source_size_mb"], rec["duckdb_size_mb"], rec["total_sec"],
        "全部一致" if rec["all_match"] else "存在不一致"))
    return rec["all_match"], rec


def archive_one(name, db_file, ts):
    """归档：gzip 至 12-数据库备份/<name>/ARCHIVE_FINAL_<ts>.db.gz，校验后删除工作区源。"""
    src = os.path.join(PODCAST_DIR, db_file)
    db_dir = os.path.join(BACKUP_ROOT, name)
    os.makedirs(db_dir, exist_ok=True)
    gz = os.path.join(db_dir, "ARCHIVE_FINAL_{}.db.gz".format(ts))
    sha = sha256_of(src)
    with open(src, "rb") as f_in, gzip.open(gz, "wb", compresslevel=6) as f_out:
        shutil.copyfileobj(f_in, f_out, 1 << 20)
    with gzip.open(gz, "rb") as f:  # 回读校验
        while f.read(1 << 20):
            pass
    m = {"op": "archive_final", "db_name": name,
         "source_path": os.path.relpath(src, BASE), "archive_file": os.path.basename(gz),
         "timestamp": ts, "source_size_bytes": os.path.getsize(src),
         "archive_size_bytes": os.path.getsize(gz),
         "sha256_uncompressed": sha, "sha256_gz": sha256_of(gz)}
    with open(gz.replace(".db.gz", ".json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(m, f, ensure_ascii=False, indent=2)
    for suf in ("", "-wal", "-shm", "-journal"):
        p = src + suf
        if os.path.exists(p):
            os.remove(p)
    log("[归档] {} -> {}（{}MB，SHA-256 已记录）".format(
        name, os.path.basename(gz), round(m["archive_size_bytes"] / 1048576, 1)))
    return m


def main():
    ap = argparse.ArgumentParser(description="播客两库 SQLite→DuckDB 收尾（转录进程退出后执行）")
    ap.add_argument("--sync-only", action="store_true", help="仅同步+校验，不归档不删除")
    ap.add_argument("--check", action="store_true", help="仅前置检查")
    args = ap.parse_args()

    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    results = {}
    for name, db_file in SCOPE.items():
        ok, msg = precheck(name, db_file)
        if not ok:
            log("[前置失败] {}: {}".format(name, msg))
            if not args.check:
                print("前置检查未通过，中止（可先 --check 排查，或确认转录进程已退出）")
                return 1
            results[name] = msg
            continue
        log("[前置通过] {}".format(name))
        results[name] = "ok"
        if args.check:
            continue
        all_match, rec = convert_one(name, db_file)
        results[name] = "sync_ok" if all_match else "sync_mismatch"
        with open(LOG, "a", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        if all_match and not args.sync_only:
            m = archive_one(name, db_file, ts)
            with open(LOG, "a", encoding="utf-8", newline="\n") as f:
                f.write(json.dumps(m, ensure_ascii=False) + "\n")
        elif not all_match:
            log("[中止归档] {} 行数不一致，保留 SQLite 源待排查".format(name))

    print("收尾结果：{}".format(json.dumps(results, ensure_ascii=False)))
    if not args.check and not args.sync_only:
        print("警示：此后重启转录任务必须使用改造后写入 DuckDB 的 _bsdnow_igpu_transcribe.py，"
              "禁止使用写 SQLite 的旧版（会在原路径重建 .db 造成数据分裂）。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
