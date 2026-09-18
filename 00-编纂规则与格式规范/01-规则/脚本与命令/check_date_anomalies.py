#!/usr/bin/env python3
"""检查数据库中的日期异常值 -- 只读模式，使用任务指定的精确路径"""
import sqlite3
import os

def check_db(label, db_path, queries):
    """对单个数据库执行一组只读查询"""
    print(f"\n{'='*70}")
    print(f"  [{label}]")
    print(f"  数据库: {db_path}")
    if not os.path.exists(db_path):
        print(f"  *** 文件不存在 ***")
        print(f"  *** 尝试查找替代路径... ***")
        # 尝试 glob 查找
        import glob
        base = os.path.dirname(db_path)
        name = os.path.basename(db_path)
        # 尝试在上级目录搜索
        for root, dirs, files in os.walk(os.path.dirname(base)):
            if name in files:
                print(f"  *** 找到: {os.path.join(root, name)} ***")
                break
        else:
            print(f"  *** 未找到替代路径 ***")
        return
    size = os.path.getsize(db_path)
    print(f"  文件大小: {size:,} 字节 ({size/1024/1024:.2f} MB)")
    print(f"{'='*70}")

    conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    try:
        for desc, sql in queries:
            print(f"\n  --- {desc} ---")
            print(f"  SQL: {sql}")
            cur = conn.execute(sql)
            rows = cur.fetchall()
            if not rows:
                print("  (无结果)")
                continue
            col_names = [d[0] for d in cur.description]
            print(f"  列: {col_names}")
            for row in rows:
                print(f"  -> {row}")
    except sqlite3.OperationalError as e:
        print(f"  *** SQL 执行错误: {e} ***")
        # 尝试列出表
        try:
            cur = conn.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
            tables = cur.fetchall()
            print(f"  可用表: {[t[0] for t in tables]}")
        except:
            pass
    finally:
        conn.close()

# ---- 数据库 1: linux-kernel.db ----
check_db("1. Linux Kernel 代码仓库", 
    r"d:\librebsd\03-原始史料库\01-代码仓库史料\10-LinuxKernel\db\linux-kernel.db",
    [
        ("MAX/MIN author_date", "SELECT MAX(author_date), MIN(author_date) FROM commits;"),
        ("异常日期 (>2030 或 <1970)", "SELECT author_date FROM commits WHERE author_date > '2030-01-01' OR author_date < '1970-01-01' LIMIT 10;"),
    ])

# ---- 数据库 2: freebsd.db ----
check_db("2. FreeBSD 代码仓库",
    r"d:\librebsd\03-原始史料库\01-代码仓库史料\02-FreeBSD\db\freebsd.db",
    [
        ("MAX/MIN author_date", "SELECT MAX(author_date), MIN(author_date) FROM commits;"),
        ("author_date < 1990", "SELECT author_date FROM commits WHERE author_date < '1990-01-01' LIMIT 10;"),
    ])

# ---- 数据库 3: openbsd_mail.db ----
check_db("3. OpenBSD 邮件列表",
    r"d:\librebsd\03-原始史料库\11-邮件列表史料\03-openbsd\openbsd_mail.db",
    [
        ("MAX/MIN year", "SELECT MAX(year), MIN(year) FROM messages;"),
        ("year < 1990 分组统计", "SELECT year, COUNT(*) FROM messages WHERE year < 1990 GROUP BY year ORDER BY year;"),
    ])

# ---- 数据库 4: dragonfly.db (任务指定路径 04-DragonFlyBSD) ----
check_db("4. DragonFly BSD 代码仓库 (任务指定路径 04-DragonFlyBSD)",
    r"d:\librebsd\03-原始史料库\01-代码仓库史料\04-DragonFlyBSD\db\dragonfly.db",
    [
        ("MAX/MIN author_date", "SELECT MAX(author_date), MIN(author_date) FROM commits;"),
        ("author_date < 2000", "SELECT author_date FROM commits WHERE author_date < '2000-01-01' LIMIT 10;"),
    ])

# 补充: 如果 04-DragonFlyBSD 不存在，尝试 05-DragonFlyBSD
check_db("4b. DragonFly BSD 代码仓库 (实际路径 05-DragonFlyBSD)",
    r"d:\librebsd\03-原始史料库\01-代码仓库史料\05-DragonFlyBSD\db\dragonfly.db",
    [
        ("MAX/MIN author_date", "SELECT MAX(author_date), MIN(author_date) FROM commits;"),
        ("author_date < 2000", "SELECT author_date FROM commits WHERE author_date < '2000-01-01' LIMIT 10;"),
    ])

# ---- 数据库 5: freebsd_mail.db ----
check_db("5. FreeBSD 邮件列表",
    r"d:\librebsd\03-原始史料库\11-邮件列表史料\01-freebsd\freebsd_mail.db",
    [
        ("MAX/MIN year", "SELECT MAX(year), MIN(year) FROM messages;"),
        ("year < 1990 分组统计", "SELECT year, COUNT(*) FROM messages WHERE year < 1990 GROUP BY year ORDER BY year;"),
    ])

print("\n" + "="*70)
print("  任务 B 完成")
print("="*70)