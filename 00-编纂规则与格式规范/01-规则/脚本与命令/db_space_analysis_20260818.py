# -*- coding: utf-8 -*-
"""空间占用分析：freelist 浪费排名、WAL 挂账、备份副本总量、目录分组体积汇总。
只读 PRAGMA 元数据，不做完整性检查，可与其他检查进程并行。"""
import os
import sqlite3
import sys

ROOT = r"d:\librebsd"
sys.stdout.reconfigure(encoding="utf-8")

freelist_rows = []   # (waste_bytes, free_pages, total_pages, path)
wal_rows = []        # (wal_bytes, path)
backup_total = 0
backup_files = 0
group_totals = {}    # 一级目录 -> [bytes, count]

for dirpath, dirnames, filenames in os.walk(ROOT):
    rel = os.path.relpath(dirpath, ROOT)
    if rel.startswith(".git"):
        dirnames[:] = []
        continue
    for fn in filenames:
        if not fn.endswith((".db", ".sqlite", ".sqlite3")):
            continue
        p = os.path.join(dirpath, fn)
        size = os.path.getsize(p)
        top = rel.split(os.sep)[0] if rel != "." else "(根)"
        sub = rel.split(os.sep)[1] if os.sep in rel else ""
        key = f"{top}{os.sep}{sub}" if sub and top in ("script", "03-原始史料库") else top
        g = group_totals.setdefault(key, [0, 0])
        g[0] += size
        g[1] += 1
        if "script" in rel.split(os.sep)[:2] or rel.startswith("script"):
            backup_total += size
            backup_files += 1
        wal = p + "-wal"
        if os.path.exists(wal) and os.path.getsize(wal) > 0:
            wal_rows.append((os.path.getsize(wal), os.path.relpath(wal, ROOT)))
        try:
            con = sqlite3.connect(f"file:{p}?mode=ro", uri=True, timeout=10)
            pc = con.execute("PRAGMA page_count").fetchone()[0]
            psz = con.execute("PRAGMA page_size").fetchone()[0]
            fl = con.execute("PRAGMA freelist_count").fetchone()[0]
            con.close()
            if fl:
                freelist_rows.append((fl * psz, fl, pc, os.path.relpath(p, ROOT)))
        except Exception:
            pass

freelist_rows.sort(reverse=True)
wal_rows.sort(reverse=True)

print("=== freelist 浪费 TOP 25（VACUUM 可回收） ===")
tot_waste = 0
for waste, fl, pc, path in freelist_rows:
    tot_waste += waste
print(f"全库 freelist 浪费合计：{tot_waste/1048576:.1f} MB，涉及 {len(freelist_rows)} 个库")
for waste, fl, pc, path in freelist_rows[:25]:
    print(f"  {waste/1024:>9.0f}KB  {fl:>6}/{pc:<8} ({fl/pc*100:>5.1f}%)  {path}")

print("\n=== WAL 挂账（checkpoint 可回收） ===")
for wb, path in wal_rows:
    print(f"  {wb/1048576:>8.2f}MB  {path}")

print("\n=== script/ 下数据库副本总量 ===")
print(f"  {backup_files} 个文件，{backup_total/1048576:.1f} MB")

print("\n=== 目录分组体积 ===")
for key, (sz, cnt) in sorted(group_totals.items(), key=lambda kv: -kv[1][0]):
    print(f"  {sz/1048576:>10.1f}MB  {cnt:>4} 库  {key}")
