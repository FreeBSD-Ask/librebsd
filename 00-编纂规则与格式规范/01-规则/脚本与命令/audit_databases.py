r"""Comprehensive database audit for 重构2026 plan enhancement.

Audits all 12 functional DuckDBs + 15 code repo DuckDBs + 4 mail merge DuckDBs.
Reports: table counts, row counts, schema alignment with 06号文 design.
"""
import duckdb
import os
import json
import csv

BASE = r"d:\librebsd"

# 12 functional DBs from folder_db_registry.csv
FUNCTIONAL_DBS = [
    ("changelog", r"01-项目管理\00-变更记录\changelog.duckdb"),
    ("sacred_sources", r"02-sacred源材料\sacred_sources.duckdb"),
    ("phoronix_news", r"03-原始史料库\01-代码仓库史料\01-数据库本体\phoronix_news.duckdb"),
    ("资料数据库", r"03-原始史料库\01-代码仓库史料\01-数据库本体\资料数据库.duckdb"),
    ("bsdnow_podcast", r"03-原始史料库\14-播客史料\bsdnow_podcast.duckdb"),
    ("bsd_podcasts_external", r"03-原始史料库\14-播客史料\bsd_podcasts_external.duckdb"),
    ("original_sources", r"03-原始史料库\original_sources.duckdb"),
    ("research_notes", r"04-现代研究文献\research_notes.duckdb"),
    ("historical_claims", r"04-现代研究文献\historical_claims.duckdb"),
    ("causal_graph", r"04-现代研究文献\causal_graph.duckdb"),
    ("references_fulltext", r"04-现代研究文献\05-参考文献全文数据库\references_fulltext.duckdb"),
    ("doubts_standalone", r"04-现代研究文献\06-存疑数据库\doubts_standalone.duckdb"),
    ("fact_checks", r"07-事实核查记录\fact_checks.duckdb"),
    ("review_reports", r"08-核查报告与多轮复核\review_reports.duckdb"),
    ("cross_indexes", r"10-交叉索引\cross_indexes.duckdb"),
    ("metadata_interfaces", r"11-元数据接口\metadata_interfaces.duckdb"),
]

# 15 code repo DuckDBs
CODE_REPO_DBS = [
    ("freebsd", r"03-原始史料库\01-代码仓库史料\02-FreeBSD\db\duckdb\freebsd.duckdb"),
    ("netbsd", r"03-原始史料库\01-代码仓库史料\03-NetBSD\db\duckdb\netbsd.duckdb"),
    ("openbsd", r"03-原始史料库\01-代码仓库史料\04-OpenBSD\db\duckdb\openbsd.duckdb"),
    ("dragonfly", r"03-原始史料库\01-代码仓库史料\05-DragonFlyBSD\db\duckdb\dragonfly.duckdb"),
    ("openzfs", r"03-原始史料库\01-代码仓库史料\06-OpenZFS\db\duckdb\openzfs.duckdb"),
    ("bsd-derivatives", r"03-原始史料库\01-代码仓库史料\07-BSD衍生项目\db\duckdb\bsd-derivatives.duckdb"),
    ("illumos-gate", r"03-原始史料库\01-代码仓库史料\08-跨项目对比\db\duckdb\illumos-gate.duckdb"),
    ("openssh-apple", r"03-原始史料库\01-代码仓库史料\08-跨项目对比\db\duckdb\openssh-apple.duckdb"),
    ("openssh", r"03-原始史料库\01-代码仓库史料\08-跨项目对比\db\duckdb\openssh.duckdb"),
    ("darwin", r"03-原始史料库\01-代码仓库史料\09-Darwin\db\duckdb\darwin.duckdb"),
    ("linux-kernel", r"03-原始史料库\01-代码仓库史料\10-LinuxKernel\db\duckdb\linux-kernel.duckdb"),
]

# 4 mail merge DuckDBs
MAIL_MERGE_DBS = [
    ("openbsd_mail", r"03-原始史料库\11-邮件列表史料\03-openbsd\duckdb\openbsd_mail.duckdb"),
    ("dragonfly_mail", r"03-原始史料库\11-邮件列表史料\04-dragonfly\duckdb\dragonfly_mail.duckdb"),
    ("other-bsd_mail", r"03-原始史料库\11-邮件列表史料\06-other-bsd\duckdb\other-bsd_mail.duckdb"),
    ("usenet_mail", r"03-原始史料库\11-邮件列表史料\07-usenet\duckdb\usenet_mail.duckdb"),
]


def audit_db(name, rel_path, label):
    full_path = os.path.join(BASE, rel_path)
    if not os.path.exists(full_path):
        return {"name": name, "label": label, "exists": False, "error": "file not found"}

    try:
        con = duckdb.connect(full_path, read_only=True)
        tables = con.execute(
            "SELECT table_name FROM information_schema.tables WHERE table_schema='main' ORDER BY table_name"
        ).fetchall()
        table_names = [t[0] for t in tables]

        total_rows = 0
        table_details = []
        for tname in table_names:
            try:
                rc = con.execute(f"SELECT COUNT(*) FROM \"{tname}\"").fetchone()[0]
                total_rows += rc
                table_details.append({"table": tname, "rows": rc})
            except Exception:
                table_details.append({"table": tname, "rows": "error"})

        size = os.path.getsize(full_path)
        con.close()

        return {
            "name": name,
            "label": label,
            "exists": True,
            "size_mb": round(size / 1048576, 1),
            "table_count": len(table_names),
            "total_rows": total_rows,
            "tables": table_details,
        }
    except Exception as e:
        return {"name": name, "label": label, "exists": True, "error": str(e)[:150]}


# Audit all
results = []
for name, path in FUNCTIONAL_DBS:
    results.append(audit_db(name, path, "functional"))
for name, path in CODE_REPO_DBS:
    results.append(audit_db(name, path, "code_repo"))
for name, path in MAIL_MERGE_DBS:
    results.append(audit_db(name, path, "mail_merge"))

# Print summary
print("=" * 80)
print("DATABASE AUDIT REPORT")
print("=" * 80)

for label, title in [("functional", "12+ Functional DBs"), ("code_repo", "11 Code Repo DBs"), ("mail_merge", "4 Mail Merge DBs")]:
    group = [r for r in results if r["label"] == label]
    print(f"\n--- {title} ({len(group)} total) ---")
    print(f"{'Name':<25} {'Exists':<7} {'Size(MB)':<10} {'Tables':<8} {'Rows':<15} {'Error' if any('error' in r for r in group) else ''}")
    print("-" * 80)
    for r in group:
        if r.get("error"):
            print(f"{r['name']:<25} {'YES' if r['exists'] else 'NO':<7} {'N/A':<10} {'N/A':<8} {'N/A':<15} {r['error'][:50]}")
        else:
            print(f"{r['name']:<25} {'YES':<7} {r['size_mb']:<10} {r['table_count']:<8} {r['total_rows']:<15}")

# Detailed table listing for key DBs
key_dbs = ["historical_claims", "causal_graph", "original_sources", "research_notes", "cross_indexes", "metadata_interfaces", "review_reports", "fact_checks", "doubts_standalone", "references_fulltext", "sacred_sources", "changelog"]
print("\n" + "=" * 80)
print("KEY DB TABLE DETAILS")
print("=" * 80)
for r in results:
    if r["name"] in key_dbs and r.get("tables"):
        print(f"\n{r['name']} ({r['table_count']} tables, {r['total_rows']} rows, {r['size_mb']} MB):")
        for t in r["tables"]:
            print(f"  {t['table']:<40} {t['rows']:>12,} rows")

# Check historical_claims against 06号文 design
print("\n" + "=" * 80)
print("HISTORICAL_CLAIMS SCHEMA vs 06号文 DESIGN")
print("=" * 80)
hc = [r for r in results if r["name"] == "historical_claims"]
if hc and hc[0].get("tables"):
    actual_tables = {t["table"] for t in hc[0]["tables"]}
    # 06号文 design tables (from 00号文 §5)
    design_tables = {
        "raw_source", "evidence", "claim", "entity", "chapter",
        "source_chapter", "source_period", "source_independence",
        "evidence_entity", "claim_evidence", "claim_entity", "claim_relation", "claim_period",
        "entity_relation", "entity_relation_type", "entity_type_class",
        "controlled_vocab", "historical_period",
        "controversy", "controversy_position",
        "interpretation", "interp_claim", "interp_evidence",
        "narrative_unit", "narrative_citation",
        "consistency_rule", "consistency_check",
        "provenance_history", "wording_gate_rule",
        "cross_ref", "schema_meta", "update_log",
    }
    missing = design_tables - actual_tables
    extra = actual_tables - design_tables
    matching = design_tables & actual_tables
    print(f"  Design tables: {len(design_tables)}")
    print(f"  Actual tables: {len(actual_tables)}")
    print(f"  Matching: {len(matching)}")
    print(f"  Missing from design: {len(missing)} - {sorted(missing) if missing else 'NONE'}")
    print(f"  Extra (not in design): {len(extra)} - {sorted(extra) if extra else 'NONE'}")

# Causal graph
print("\n" + "=" * 80)
print("CAUSAL_GRAPH SCHEMA")
print("=" * 80)
cg = [r for r in results if r["name"] == "causal_graph"]
if cg and cg[0].get("tables"):
    print(f"  Tables: {len(cg[0]['tables'])}, Rows: {cg[0]['total_rows']}")
    for t in cg[0]["tables"]:
        print(f"  {t['table']:<40} {t['rows']:>12,} rows")

# Summary stats
print("\n" + "=" * 80)
print("SUMMARY")
print("=" * 80)
existing = [r for r in results if r.get("exists") and not r.get("error")]
missing = [r for r in results if not r.get("exists")]
errored = [r for r in results if r.get("error") and r.get("exists")]
total_size = sum(r["size_mb"] for r in existing)
total_tables = sum(r["table_count"] for r in existing)
total_rows = sum(r["total_rows"] for r in existing)
print(f"  Total DBs audited: {len(results)}")
print(f"  Existing: {len(existing)}, Missing: {len(missing)}, Errored: {len(errored)}")
print(f"  Total size: {total_size:.1f} MB ({total_size/1024:.2f} GB)")
print(f"  Total tables: {total_tables}")
print(f"  Total rows: {total_rows:,}")