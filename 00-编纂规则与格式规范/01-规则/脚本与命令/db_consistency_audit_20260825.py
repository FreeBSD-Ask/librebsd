# -*- coding: utf-8 -*-
"""逐个数据库一致性复核：表结构、行数、日期范围、NULL 率、重复哈希、异常值。"""
import duckdb
import os
import sqlite3
import sys

sys.stdout.reconfigure(encoding="utf-8")
BASE = r"d:\librebsd"
CODE = os.path.join(BASE, "03-原始史料库", "01-代码仓库史料")

DBS = {
    "freebsd": os.path.join(CODE, "02-FreeBSD", "db", "duckdb", "freebsd.duckdb"),
    "netbsd": os.path.join(CODE, "03-NetBSD", "db", "duckdb", "netbsd.duckdb"),
    "openbsd": os.path.join(CODE, "04-OpenBSD", "db", "duckdb", "openbsd.duckdb"),
    "dragonfly": os.path.join(CODE, "05-DragonFlyBSD", "db", "duckdb", "dragonfly.duckdb"),
    "openzfs": os.path.join(CODE, "06-OpenZFS", "db", "duckdb", "openzfs.duckdb"),
    "bsd-derivatives": os.path.join(CODE, "07-BSD衍生项目", "db", "duckdb", "bsd-derivatives.duckdb"),
    "illumos-gate": os.path.join(CODE, "08-跨项目对比", "db", "duckdb", "illumos-gate.duckdb"),
    "openssh": os.path.join(CODE, "08-跨项目对比", "db", "duckdb", "openssh.duckdb"),
    "openssh-apple": os.path.join(CODE, "08-跨项目对比", "db", "duckdb", "openssh-apple.duckdb"),
    "darwin": os.path.join(CODE, "09-Darwin", "db", "duckdb", "darwin.duckdb"),
    "linux-kernel": os.path.join(CODE, "10-LinuxKernel", "db", "duckdb", "linux-kernel.duckdb"),
    "openbsd_mail": os.path.join(BASE, "03-原始史料库", "11-邮件列表史料", "03-openbsd", "duckdb", "openbsd_mail.duckdb"),
    "dragonfly_mail": os.path.join(BASE, "03-原始史料库", "11-邮件列表史料", "04-dragonfly", "duckdb", "dragonfly_mail.duckdb"),
    "other-bsd_mail": os.path.join(BASE, "03-原始史料库", "11-邮件列表史料", "06-other-bsd", "duckdb", "other-bsd_mail.duckdb"),
    "usenet_mail": os.path.join(BASE, "03-原始史料库", "11-邮件列表史料", "07-usenet", "duckdb", "usenet_mail.duckdb"),
}

issues = []

for name, path in DBS.items():
    if not os.path.exists(path):
        issues.append(f"[缺失] {name} 主库不存在")
        continue
    dk = duckdb.connect(path, read_only=True)
    print(f"\n==== {name} ({os.path.getsize(path)/1048576:.0f}MB) ====")
    try:
        tables = [r[0] for r in dk.execute(
            "SELECT table_name FROM information_schema.tables WHERE table_schema='main'").fetchall()]
        print(f"  表: {tables}")
        for t in tables:
            n = dk.execute(f'SELECT count(*) FROM "{t}"').fetchone()[0]
            cols = dk.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name='{t}'").fetchall()
            print(f"    {t}: {n:,} rows, cols={[c[0] for c in cols]}")

        # commits 专项检查
        if "commits" in tables:
            r = dk.execute("SELECT count(*), count(DISTINCT commit_hash) FROM commits").fetchone()
            if r[0] != r[1]:
                issues.append(f"[重复] {name} commits: {r[0]} rows but {r[1]} unique hashes")

            r = dk.execute("SELECT count(*) FROM commits WHERE commit_hash IS NULL").fetchone()[0]
            if r > 0:
                issues.append(f"[NULL] {name} commits: {r} rows with NULL commit_hash")

            r = dk.execute("SELECT count(*) FROM commits WHERE author_name IS NULL OR author_name=''").fetchone()[0]
            pc = r / max(1, dk.execute("SELECT count(*) FROM commits").fetchone()[0]) * 100
            print(f"    NULL author_name: {r:,} ({pc:.1f}%)")

            dates = dk.execute("SELECT min(author_date), max(author_date), min(committer_date), max(committer_date) FROM commits").fetchone()
            print(f"    日期范围: author {dates[0][:10]} ~ {dates[1][:10]}, committer {dates[2][:10]} ~ {dates[3][:10]}")

            if dates[3] and dates[3][:4] > "2026":
                issues.append(f"[未来] {name} committer_date max={dates[3][:10]}")

            r = dk.execute("SELECT count(*) FROM commits WHERE author_date > '2026-09-01' OR committer_date > '2026-09-01'").fetchone()[0]
            if r > 0:
                issues.append(f"[未来] {name} commits: {r} rows with date > 2026-09-01")

            r = dk.execute("SELECT count(*) FROM commits WHERE author_date < '1970-01-01'").fetchone()[0]
            if r > 0:
                issues.append(f"[异常] {name} commits: {r} rows with author_date < 1970")

        # repos vs commits 一致性
        if "repos" in tables and "commits" in tables:
            repos_in_commits = set(r[0] for r in dk.execute("SELECT DISTINCT repo_name FROM commits").fetchall())
            repos_in_repos = set(r[0] for r in dk.execute("SELECT repo_name FROM repos").fetchall())
            missing = repos_in_commits - repos_in_repos
            extra = repos_in_repos - repos_in_commits
            if missing:
                issues.append(f"[孤立] {name} commits 有 {len(missing)} 个 repo 不在 repos 表: {missing}")
            if extra:
                issues.append(f"[孤立] {name} repos 有 {len(extra)} 个 repo 无 commits: {extra}")
            print(f"    repos一致性: commits={len(repos_in_commits)} repos={len(repos_in_repos)} missing={len(missing)} extra={len(extra)}")

        # messages 专项检查
        if "messages" in tables:
            r = dk.execute("SELECT count(*), count(DISTINCT message_id) FROM messages").fetchone()
            if r[0] != r[1]:
                issues.append(f"[重复] {name} messages: {r[0]} rows but {r[1]} unique message_ids")
            dates = dk.execute("SELECT min(date), max(date) FROM messages").fetchone()
            print(f"    日期范围: {dates[0][:10] if dates[0] else 'NULL'} ~ {dates[1][:10] if dates[1] else 'NULL'}")

    except Exception as e:
        issues.append(f"[异常] {name}: {e}")
    dk.close()

print("\n" + "=" * 60)
if issues:
    print(f"发现问题 {len(issues)} 项:")
    for i in issues:
        print(f"  {i}")
else:
    print("全部 15 库无异常")