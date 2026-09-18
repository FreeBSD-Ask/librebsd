# -*- coding: utf-8 -*-
"""快速盘点项目内全部 SQLite 数据库文件体积与 WAL 状态（只读，不做完整性检查）。"""
import os
import sqlite3
import sys

ROOT = r"d:\librebsd"
sys.stdout.reconfigure(encoding="utf-8")

rows = []
for dirpath, dirnames, filenames in os.walk(ROOT):
    # 跳过 .git
    rel = os.path.relpath(dirpath, ROOT)
    if rel.startswith(".git"):
        dirnames[:] = []
        continue
    for fn in filenames:
        if fn.endswith(("-wal", "-shm", "-journal")):
            continue
        if not fn.endswith((".db", ".sqlite", ".sqlite3", ".db3")):
            continue
        p = os.path.join(dirpath, fn)
        try:
            size = os.path.getsize(p)
        except OSError:
            continue
        wal = p + "-wal"
        wal_size = os.path.getsize(wal) if os.path.exists(wal) else 0
        # 只读打开取页信息
        page_info = ("?", "?", "?", "?")
        table_count = "?"
        err = ""
        try:
            con = sqlite3.connect(f"file:{p}?mode=ro", uri=True, timeout=5)
            cur = con.cursor()
            pc = cur.execute("PRAGMA page_count").fetchone()[0]
            psz = cur.execute("PRAGMA page_size").fetchone()[0]
            fl = cur.execute("PRAGMA freelist_count").fetchone()[0]
            ver = cur.execute("select sqlite_version()").fetchone()[0]
            try:
                table_count = cur.execute(
                    "select count(*) from sqlite_master where type='table' and name not like 'sqlite_%'"
                ).fetchone()[0]
            except Exception:
                table_count = "?"
            page_info = (pc, psz, fl, ver)
            con.close()
        except Exception as e:
            err = f"{type(e).__name__}: {e}"
        rows.append((size, wal_size, rel, fn, page_info, table_count, err))

rows.sort(reverse=True)
total = sum(r[0] for r in rows)
print(f"共 {len(rows)} 个库，主文件总体积 {total/1024/1024/1024:.2f} GB")
print()
print(f"{'体积MB':>10} {'WAL_MB':>8} {'页数':>12} {'页大小':>6} {'空闲页':>10} {'表数':>5}  路径")
for size, wal_size, rel, fn, (pc, psz, fl, ver), tc, err in rows:
    print(f"{size/1024/1024:>10.2f} {wal_size/1024/1024:>8.2f} {str(pc):>12} {str(psz):>6} {str(fl):>10} {str(tc):>5}  {rel}{'' if not err else '  [ERR:' + err + ']'}")
