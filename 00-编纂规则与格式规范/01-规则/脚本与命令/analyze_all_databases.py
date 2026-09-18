#!/usr/bin/env python3
"""全项目数据库清单与 Schema 分析脚本。
输出 JSON 格式，供后续研究使用。
"""

import os
import json
import sys
import duckdb

BASE = r"d:\librebsd"

# A. 代码仓库数据库（主存储层 DuckDB）
CODE_REPO_DBS = {
    "freebsd":       os.path.join(BASE, r"03-原始史料库\01-代码仓库史料\02-FreeBSD\db\duckdb\freebsd.duckdb"),
    "netbsd":        os.path.join(BASE, r"03-原始史料库\01-代码仓库史料\03-NetBSD\db\duckdb\netbsd.duckdb"),
    "openbsd":       os.path.join(BASE, r"03-原始史料库\01-代码仓库史料\04-OpenBSD\db\duckdb\openbsd.duckdb"),
    "dragonfly":     os.path.join(BASE, r"03-原始史料库\01-代码仓库史料\05-DragonFlyBSD\db\duckdb\dragonfly.duckdb"),
    "openzfs":       os.path.join(BASE, r"03-原始史料库\01-代码仓库史料\06-OpenZFS\db\duckdb\openzfs.duckdb"),
    "bsd_derivatives": os.path.join(BASE, r"03-原始史料库\01-代码仓库史料\07-BSD衍生项目\db\duckdb\bsd-derivatives.duckdb"),
    "illumos_gate":  os.path.join(BASE, r"03-原始史料库\01-代码仓库史料\08-跨项目对比\db\duckdb\illumos-gate.duckdb"),
    "openssh":       os.path.join(BASE, r"03-原始史料库\01-代码仓库史料\08-跨项目对比\db\duckdb\openssh.duckdb"),
    "openssh_apple": os.path.join(BASE, r"03-原始史料库\01-代码仓库史料\08-跨项目对比\db\duckdb\openssh-apple.duckdb"),
    "darwin":        os.path.join(BASE, r"03-原始史料库\01-代码仓库史料\09-Darwin\db\duckdb\darwin.duckdb"),
    "linux_kernel":  os.path.join(BASE, r"03-原始史料库\01-代码仓库史料\10-LinuxKernel\db\duckdb\linux-kernel.duckdb"),
    "资料数据库":    os.path.join(BASE, r"03-原始史料库\01-代码仓库史料\01-数据库本体\资料数据库.duckdb"),
    "phoronix_news": os.path.join(BASE, r"03-原始史料库\01-代码仓库史料\01-数据库本体\phoronix_news.duckdb"),
}

# B. 邮件列表合并数据库（DuckDB）
MAIL_DBS = {
    "freebsd_mail":   os.path.join(BASE, r"03-原始史料库\11-邮件列表史料\01-freebsd\db\freebsd_mail.duckdb"),
    "netbsd_mail":    os.path.join(BASE, r"03-原始史料库\11-邮件列表史料\02-netbsd\db\netbsd_mail.duckdb"),
    "openbsd_mail":   os.path.join(BASE, r"03-原始史料库\11-邮件列表史料\03-openbsd\duckdb\openbsd_mail.duckdb"),
    "dragonfly_mail": os.path.join(BASE, r"03-原始史料库\11-邮件列表史料\04-dragonfly\duckdb\dragonfly_mail.duckdb"),
    "linuxkernel_mail": os.path.join(BASE, r"03-原始史料库\11-邮件列表史料\05-linux-kernel\db\linuxkernel_mail.duckdb"),
    "other_bsd_mail": os.path.join(BASE, r"03-原始史料库\11-邮件列表史料\06-other-bsd\duckdb\other-bsd_mail.duckdb"),
    "usenet_mail":     os.path.join(BASE, r"03-原始史料库\11-邮件列表史料\07-usenet\duckdb\usenet_mail.duckdb"),
}

# 邮件列表子数据库（未合并的独立 DuckDB，位于 subdirs）
FREEBSD_MAIL_SUB_DIR = os.path.join(BASE, r"03-原始史料库\11-邮件列表史料\01-freebsd\db")
NETBSD_MAIL_SUB_DIR = os.path.join(BASE, r"03-原始史料库\11-邮件列表史料\02-netbsd\db")

# C. 功能数据库（DuckDB）
FUNCTIONAL_DBS = {
    "sacred_sources":       os.path.join(BASE, r"02-sacred源材料\sacred_sources.duckdb"),
    "original_sources":     os.path.join(BASE, r"03-原始史料库\original_sources.duckdb"),
    "research_notes":        os.path.join(BASE, r"04-现代研究文献\research_notes.duckdb"),
    "references_fulltext":  os.path.join(BASE, r"04-现代研究文献\05-参考文献全文数据库\references_fulltext.duckdb"),
    "doubts_standalone":    os.path.join(BASE, r"04-现代研究文献\06-存疑数据库\doubts_standalone.duckdb"),
    "historical_claims":    os.path.join(BASE, r"04-现代研究文献\historical_claims.duckdb"),
    "causal_graph":         os.path.join(BASE, r"04-现代研究文献\causal_graph.duckdb"),
    "fact_checks":          os.path.join(BASE, r"07-事实核查记录\fact_checks.duckdb"),
    "review_reports":       os.path.join(BASE, r"08-核查报告与多轮复核\review_reports.duckdb"),
    "cross_indexes":        os.path.join(BASE, r"10-交叉索引\cross_indexes.duckdb"),
    "metadata_interfaces":  os.path.join(BASE, r"11-元数据接口\metadata_interfaces.duckdb"),
    "changelog":            os.path.join(BASE, r"01-项目管理\00-变更记录\changelog.duckdb"),
    "bsdnow_podcast":       os.path.join(BASE, r"03-原始史料库\14-播客史料\bsdnow_podcast.duckdb"),
    "bsd_podcasts_external": os.path.join(BASE, r"03-原始史料库\14-播客史料\bsd_podcasts_external.duckdb"),
}


def db_size_mb(path):
    """Return file size in MB, or 0 if missing."""
    try:
        return round(os.path.getsize(path) / (1024 * 1024), 2)
    except OSError:
        return 0


def analyze_schema(con, db_name):
    """Extract tables, row counts, and sample columns for a DuckDB database."""
    tables = con.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='main'").fetchall()
    result = {"db_name": db_name, "tables": []}
    for (tbl,) in tables:
        cols = con.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name='{tbl}'").fetchall()
        try:
            n = con.execute(f"SELECT COUNT(*) FROM \"{tbl}\"").fetchone()[0]
        except Exception:
            n = -1
        result["tables"].append({
            "table": tbl,
            "row_count": n,
            "columns": [{"name": c, "type": d} for c, d in cols]
        })
    return result


def analyze_git_commits(con, db_name):
    """Extract commit statistics from a git-commit DuckDB."""
    stats = {"db_name": db_name, "total_commits": 0, "total_authors": 0, "date_range": None, "top_authors": []}
    try:
        tables = [r[0] for r in con.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='main'").fetchall()]
        if "commits" in tables:
            stats["total_commits"] = con.execute("SELECT COUNT(*) FROM commits").fetchone()[0]
            stats["total_authors"] = con.execute("SELECT COUNT(DISTINCT author_name) FROM commits").fetchone()[0]
            try:
                dr = con.execute("SELECT MIN(commit_date), MAX(commit_date) FROM commits").fetchone()
                stats["date_range"] = [str(dr[0]) if dr[0] else None, str(dr[1]) if dr[1] else None]
            except Exception:
                pass
            try:
                stats["top_authors"] = [
                    {"name": r[0], "commits": r[1]}
                    for r in con.execute(
                        "SELECT author_name, COUNT(*) AS cnt FROM commits GROUP BY author_name ORDER BY cnt DESC LIMIT 10"
                    ).fetchall()
                ]
            except Exception:
                pass
        if "changes" in tables:
            stats["total_changes"] = con.execute("SELECT COUNT(*) FROM changes").fetchone()[0]
    except Exception as e:
        stats["error"] = str(e)
    return stats


def analyze_mail_db(con, db_name):
    """Extract mail statistics from a mail-list DuckDB."""
    stats = {"db_name": db_name, "total_emails": 0, "total_senders": 0, "date_range": None}
    try:
        tables = [r[0] for r in con.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='main'").fetchall()]
        # Common mail table names
        mail_tables = [t for t in tables if t in ("emails", "messages", "mail", "posts")]
        if mail_tables:
            tbl = mail_tables[0]
            stats["total_emails"] = con.execute(f"SELECT COUNT(*) FROM \"{tbl}\"").fetchone()[0]
            cols = [r[0] for r in con.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name='{tbl}'").fetchall()]
            if "sender" in cols or "from" in cols:
                sc = "sender" if "sender" in cols else "from"
                stats["total_senders"] = con.execute(f"SELECT COUNT(DISTINCT \"{sc}\") FROM \"{tbl}\"").fetchone()[0]
            if "date" in cols:
                dr = con.execute(f"SELECT MIN(\"date\"), MAX(\"date\") FROM \"{tbl}\"").fetchone()
                stats["date_range"] = [str(dr[0]) if dr[0] else None, str(dr[1]) if dr[1] else None]
    except Exception as e:
        stats["error"] = str(e)
    return stats


def main():
    print("=" * 80)
    print("全项目数据库清单与分析")
    print("=" * 80)

    all_results = {}

    # --- A. 代码仓库数据库 ---
    print("\n[1/4] 分析代码仓库数据库...")
    code_results = {}
    for name, path in sorted(CODE_REPO_DBS.items()):
        size = db_size_mb(path)
        if not os.path.exists(path):
            code_results[name] = {"path": path, "size_mb": 0, "error": "FILE_NOT_FOUND"}
            continue
        print(f"  {name}: {size} MB")
        con = duckdb.connect(path, read_only=True)
        schema = analyze_schema(con, name)
        commits = analyze_git_commits(con, name)
        con.close()
        code_results[name] = {"path": path, "size_mb": size, "schema": schema, "commits": commits}
    all_results["code_repo_dbs"] = code_results

    # --- B. 邮件列表合并数据库 ---
    print("\n[2/4] 分析邮件列表合并数据库...")
    mail_results = {}
    for name, path in sorted(MAIL_DBS.items()):
        if not os.path.exists(path):
            mail_results[name] = {"path": path, "size_mb": 0, "error": "FILE_NOT_FOUND"}
            continue
        size = db_size_mb(path)
        print(f"  {name}: {size} MB")
        con = duckdb.connect(path, read_only=True)
        schema = analyze_schema(con, name)
        mail_stats = analyze_mail_db(con, name)
        con.close()
        mail_results[name] = {"path": path, "size_mb": size, "schema": schema, "mail": mail_stats}
    all_results["mail_dbs"] = mail_results

    # --- B2. 邮件列表子数据库 ---
    print("\n[2b/4] 分析邮件列表子数据库...")
    mail_sub_results = {}
    for label, subdir in [("freebsd_sub", FREEBSD_MAIL_SUB_DIR), ("netbsd_sub", NETBSD_MAIL_SUB_DIR)]:
        if not os.path.isdir(subdir):
            continue
        for fname in sorted(os.listdir(subdir)):
            if not fname.endswith(".duckdb"):
                continue
            path = os.path.join(subdir, fname)
            key = f"{label}/{fname}"
            size = db_size_mb(path)
            try:
                con = duckdb.connect(path, read_only=True)
                schema = analyze_schema(con, key)
                mail_stats = analyze_mail_db(con, key)
                con.close()
                mail_sub_results[key] = {"path": path, "size_mb": size, "schema": schema, "mail": mail_stats}
            except Exception as e:
                mail_sub_results[key] = {"path": path, "size_mb": size, "error": str(e)}
            if len(mail_sub_results) % 20 == 0:
                print(f"  ... processed {len(mail_sub_results)} sub-dbs ...")
    print(f"  Total sub-dbs: {len(mail_sub_results)}")
    all_results["mail_sub_dbs"] = mail_sub_results

    # --- C. 功能数据库 ---
    print("\n[3/4] 分析功能数据库...")
    func_results = {}
    for name, path in sorted(FUNCTIONAL_DBS.items()):
        if not os.path.exists(path):
            func_results[name] = {"path": path, "size_mb": 0, "error": "FILE_NOT_FOUND"}
            continue
        size = db_size_mb(path)
        print(f"  {name}: {size} MB")
        con = duckdb.connect(path, read_only=True)
        schema = analyze_schema(con, name)
        con.close()
        func_results[name] = {"path": path, "size_mb": size, "schema": schema}
    all_results["functional_dbs"] = func_results

    # --- Summary ---
    print("\n[4/4] 生成汇总...")
    total_code_size = sum(v.get("size_mb", 0) for v in code_results.values())
    total_mail_size = sum(v.get("size_mb", 0) for v in mail_results.values())
    total_mail_sub_size = sum(v.get("size_mb", 0) for v in mail_sub_results.values())
    total_func_size = sum(v.get("size_mb", 0) for v in func_results.values())
    total_all = total_code_size + total_mail_size + total_mail_sub_size + total_func_size

    summary = {
        "code_repo_count": len(code_results),
        "code_repo_total_mb": total_code_size,
        "mail_merged_count": len(mail_results),
        "mail_merged_total_mb": total_mail_size,
        "mail_sub_count": len(mail_sub_results),
        "mail_sub_total_mb": total_mail_sub_size,
        "functional_count": len(func_results),
        "functional_total_mb": total_func_size,
        "grand_total_mb": total_all,
        "grand_total_gb": round(total_all / 1024, 2),
    }
    all_results["summary"] = summary

    # Output
    out_path = os.path.join(BASE, "script", "db_analysis_results.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2, default=str)
    print(f"\n结果已写入: {out_path}")

    print("\n" + "=" * 80)
    print("汇总:")
    print(f"  代码仓库数据库: {summary['code_repo_count']} 个, {summary['code_repo_total_mb']:.0f} MB")
    print(f"  邮件合并数据库: {summary['mail_merged_count']} 个, {summary['mail_merged_total_mb']:.0f} MB")
    print(f"  邮件子数据库:   {summary['mail_sub_count']} 个, {summary['mail_sub_total_mb']:.0f} MB")
    print(f"  功能数据库:     {summary['functional_count']} 个, {summary['functional_total_mb']:.0f} MB")
    print(f"  总计:           {summary['grand_total_gb']} GB")
    print("=" * 80)


if __name__ == "__main__":
    main()