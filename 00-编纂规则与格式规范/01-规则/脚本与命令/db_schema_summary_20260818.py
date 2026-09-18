# -*- coding: utf-8 -*-
"""采集代表性数据库的 schema 摘要：表/行数/索引/FTS/视图/触发器/页统计，供迁移评估使用。
行数优先取 sqlite_stat1，缺统计且 count 超预算则标 approx/timeout。轻 IO 设计。"""
import json
import os
import sqlite3
import sys
import time

ROOT = r"d:\librebsd"
OUT = os.path.join(ROOT, "script", "db_schema_summary_20260818.jsonl")
sys.stdout.reconfigure(encoding="utf-8")

TARGETS = [
    r"01-项目管理\00-变更记录\changelog.db",
    r"02-sacred源材料\sacred_sources.db",
    r"03-原始史料库\original_sources.db",
    r"03-原始史料库\01-代码仓库史料\01-数据库本体\资料数据库.db",
    r"03-原始史料库\01-代码仓库史料\01-数据库本体\phoronix_news.db",
    r"03-原始史料库\01-代码仓库史料\02-FreeBSD\db\freebsd.db",
    r"03-原始史料库\01-代码仓库史料\03-NetBSD\db\netbsd.db",
    r"03-原始史料库\01-代码仓库史料\04-OpenBSD\db\openbsd.db",
    r"03-原始史料库\01-代码仓库史料\05-DragonFlyBSD\db\dragonfly.db",
    r"03-原始史料库\01-代码仓库史料\06-OpenZFS\db\openzfs.db",
    r"03-原始史料库\01-代码仓库史料\07-BSD衍生项目\db\bsd-derivatives.db",
    r"03-原始史料库\01-代码仓库史料\08-跨项目对比\db\illumos-gate.db",
    r"03-原始史料库\01-代码仓库史料\08-跨项目对比\db\openssh.db",
    r"03-原始史料库\01-代码仓库史料\08-跨项目对比\db\openssh-apple.db",
    r"03-原始史料库\01-代码仓库史料\09-Darwin\db\darwin.db",
    r"03-原始史料库\01-代码仓库史料\10-LinuxKernel\db\linux-kernel.db",
    r"03-原始史料库\11-邮件列表史料\01-freebsd\db\freebsd-stable.db",
    r"03-原始史料库\11-邮件列表史料\02-netbsd\db\tech-kern.db",
    r"03-原始史料库\11-邮件列表史料\03-openbsd\openbsd_mail.db",
    r"03-原始史料库\11-邮件列表史料\04-dragonfly\dragonfly_mail.db",
    r"03-原始史料库\11-邮件列表史料\06-other-bsd\other-bsd_mail.db",
    r"03-原始史料库\11-邮件列表史料\07-usenet\usenet_mail.db",
    r"03-原始史料库\14-播客史料\bsdnow_podcast.db",
    r"03-原始史料库\14-播客史料\bsd_podcasts_external.db",
    r"04-现代研究文献\research_notes.db",
    r"04-现代研究文献\historical_claims.db",
    r"04-现代研究文献\causal_graph.db",
    r"04-现代研究文献\05-参考文献全文数据库\references_fulltext.db",
    r"04-现代研究文献\06-存疑数据库\doubts_standalone.db",
    r"07-事实核查记录\fact_checks.db",
    r"08-核查报告与多轮复核\review_reports.db",
    r"10-交叉索引\cross_indexes.db",
    r"11-元数据接口\metadata_interfaces.db",
    r"script\_msg_date_index.db",
]


def rowcount(cur, table, has_stat1, stat1_rows):
    if has_stat1 and table in stat1_rows:
        return {"rows": stat1_rows[table], "src": "stat1"}
    # count 预算 60s
    deadline = time.monotonic() + 60

    def h():
        return 1 if time.monotonic() > deadline else 0
    cur.connection.set_progress_handler(h, 500000)
    try:
        n = cur.execute(f'SELECT count(*) FROM "{table}"').fetchone()[0]
        cur.connection.set_progress_handler(None, 0)
        return {"rows": n, "src": "count"}
    except Exception:
        cur.connection.set_progress_handler(None, 0)
        return {"rows": None, "src": "timeout"}


def summarize(rel):
    path = os.path.join(ROOT, rel)
    rec = {"path": rel, "size_mb": round(os.path.getsize(path) / 1048576, 2)}
    con = sqlite3.connect(f"file:{path}?mode=ro", uri=True, timeout=30)
    cur = con.cursor()
    rec["page_size"] = cur.execute("PRAGMA page_size").fetchone()[0]
    rec["page_count"] = cur.execute("PRAGMA page_count").fetchone()[0]
    rec["freelist"] = cur.execute("PRAGMA freelist_count").fetchone()[0]
    rec["journal_mode"] = cur.execute("PRAGMA journal_mode").fetchone()[0]
    objs = cur.execute(
        "SELECT type,name,tbl_name,sql FROM sqlite_master WHERE name NOT LIKE 'sqlite_%'"
    ).fetchall()
    # stat1
    stat1_rows = {}
    has_stat1 = any(o[1] == "sqlite_stat1" for o in objs)
    if has_stat1:
        for t, stat in cur.execute("SELECT tbl, stat FROM sqlite_stat1"):
            try:
                stat1_rows[t] = int(stat.split()[0])
            except Exception:
                pass
    tables = {}
    for typ, name, tbl, sql in objs:
        if typ == "table":
            rc = rowcount(cur, name, has_stat1, stat1_rows)
            tables[name] = {
                "rows": rc["rows"], "rows_src": rc["src"],
                "is_fts": name.startswith(("fts", "sqlite_fts")) or "fts5" in (sql or ""),
                "has_rowid": True,
                "cols": [c[1] for c in cur.execute(f'PRAGMA table_info("{name}")')],
            }
            try:
                cur.execute(f'SELECT rowid FROM "{name}" LIMIT 1')
            except Exception:
                tables[name]["has_rowid"] = False
    idx = {}
    for typ, name, tbl, sql in objs:
        if typ == "index":
            idx[name] = {"table": tbl, "auto": sql is None,
                         "unique": bool(sql and "UNIQUE" in sql.upper())}
    rec["tables"] = tables
    rec["indexes"] = idx
    rec["views"] = [o[1] for o in objs if o[0] == "view"]
    rec["triggers"] = [o[1] for o in objs if o[0] == "trigger"]
    con.close()
    return rec


with open(OUT, "w", encoding="utf-8") as f:
    for rel in TARGETS:
        try:
            rec = summarize(rel)
        except Exception as e:
            rec = {"path": rel, "error": f"{type(e).__name__}: {e}"}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        f.flush()
        tcount = len(rec.get("tables", {}))
        print(f"done {rel} tables={tcount}", flush=True)
print("全部完成", flush=True)
