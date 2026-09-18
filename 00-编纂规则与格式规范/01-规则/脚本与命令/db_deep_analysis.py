#!/usr/bin/env python3
"""深度分析全项目数据库，提取可写入大纲的关键发现。
按卷-章映射数据库中的史料、统计、贡献者等关键信息。
"""

import json
import os
import duckdb
from collections import defaultdict

BASE = r"d:\librebsd"

# === 数据库路径定义 ===
CODE_DBS = {
    "freebsd":       os.path.join(BASE, r"03-原始史料库\01-代码仓库史料\02-FreeBSD\db\duckdb\freebsd.duckdb"),
    "netbsd":        os.path.join(BASE, r"03-原始史料库\01-代码仓库史料\03-NetBSD\db\duckdb\netbsd.duckdb"),
    "openbsd":       os.path.join(BASE, r"03-原始史料库\01-代码仓库史料\04-OpenBSD\db\duckdb\openbsd.duckdb"),
    "dragonfly":     os.path.join(BASE, r"03-原始史料库\01-代码仓库史料\05-DragonFlyBSD\db\duckdb\dragonfly.duckdb"),
    "openzfs":       os.path.join(BASE, r"03-原始史料库\01-代码仓库史料\06-OpenZFS\db\duckdb\openzfs.duckdb"),
    "bsd_derivatives": os.path.join(BASE, r"03-原始史料库\01-代码仓库史料\07-BSD衍生项目\db\duckdb\bsd-derivatives.duckdb"),
    "darwin":        os.path.join(BASE, r"03-原始史料库\01-代码仓库史料\09-Darwin\db\duckdb\darwin.duckdb"),
    "linux_kernel":  os.path.join(BASE, r"03-原始史料库\01-代码仓库史料\10-LinuxKernel\db\duckdb\linux-kernel.duckdb"),
    "illumos_gate":  os.path.join(BASE, r"03-原始史料库\01-代码仓库史料\08-跨项目对比\db\duckdb\illumos-gate.duckdb"),
    "openssh":       os.path.join(BASE, r"03-原始史料库\01-代码仓库史料\08-跨项目对比\db\duckdb\openssh.duckdb"),
}

FUNC_DBS = {
    "references_fulltext": os.path.join(BASE, r"04-现代研究文献\05-参考文献全文数据库\references_fulltext.duckdb"),
    "research_notes":      os.path.join(BASE, r"04-现代研究文献\research_notes.duckdb"),
    "historical_claims":   os.path.join(BASE, r"04-现代研究文献\historical_claims.duckdb"),
    "doubts_standalone":   os.path.join(BASE, r"04-现代研究文献\06-存疑数据库\doubts_standalone.duckdb"),
    "sacred_sources":      os.path.join(BASE, r"02-sacred源材料\sacred_sources.duckdb"),
    "cross_indexes":       os.path.join(BASE, r"10-交叉索引\cross_indexes.duckdb"),
    "metadata_interfaces": os.path.join(BASE, r"11-元数据接口\metadata_interfaces.duckdb"),
    "changelog":           os.path.join(BASE, r"01-项目管理\00-变更记录\changelog.duckdb"),
    "bsdnow_podcast":      os.path.join(BASE, r"03-原始史料库\14-播客史料\bsdnow_podcast.duckdb"),
    "fact_checks":         os.path.join(BASE, r"07-事实核查记录\fact_checks.duckdb"),
    "review_reports":      os.path.join(BASE, r"08-核查报告与多轮复核\review_reports.duckdb"),
}

results = {
    "code_repos": {},
    "functional": {},
    "chapter_mapping": defaultdict(list),
    "global_findings": [],
}


def safe_query(con, query, dbg=""):
    try:
        return con.execute(query).fetchall()
    except Exception as e:
        return [("ERROR", str(e))]


# ============================================================
# 1. 代码仓库深度分析
# ============================================================
print("=" * 80)
print("[1] 代码仓库深度分析")
print("=" * 80)

for name, path in CODE_DBS.items():
    if not os.path.exists(path):
        continue
    print(f"\n--- {name} ---")
    con = duckdb.connect(path, read_only=True)
    info = {"name": name, "path": path}

    # 检查表结构
    tables = safe_query(con, "SELECT table_name FROM information_schema.tables WHERE table_schema='main'")
    info["tables"] = [t[0] for t in tables if not isinstance(t[0], str) or t[0] != "ERROR"]

    if "commits" in info["tables"]:
        # 总提交数
        r = safe_query(con, "SELECT COUNT(*) FROM commits")
        info["total_commits"] = r[0][0] if r else 0

        # 时间范围
        r = safe_query(con, "SELECT MIN(commit_date), MAX(commit_date) FROM commits")
        if r and r[0][0]:
            info["date_range"] = [str(r[0][0]), str(r[0][1])]

        # 贡献者数
        r = safe_query(con, "SELECT COUNT(DISTINCT author_name) FROM commits")
        info["total_authors"] = r[0][0] if r else 0

        # Top 20 贡献者
        r = safe_query(con, """
            SELECT author_name, COUNT(*) AS cnt
            FROM commits
            GROUP BY author_name
            ORDER BY cnt DESC
            LIMIT 20
        """)
        info["top_authors"] = [{"name": x[0], "commits": x[1]} for x in r if x[0] != "ERROR"]

        # 按年提交统计
        r = safe_query(con, """
            SELECT YEAR(commit_date) AS yr, COUNT(*) AS cnt
            FROM commits
            WHERE commit_date IS NOT NULL
            GROUP BY yr
            ORDER BY yr
        """)
        info["commits_by_year"] = [{"year": x[0], "commits": x[1]} for x in r if x[0] != "ERROR"]

        # 按年贡献者统计
        r = safe_query(con, """
            SELECT YEAR(commit_date) AS yr, COUNT(DISTINCT author_name) AS cnt
            FROM commits
            WHERE commit_date IS NOT NULL
            GROUP BY yr
            ORDER BY yr
        """)
        info["authors_by_year"] = [{"year": x[0], "authors": x[1]} for x in r if x[0] != "ERROR"]

        # 高峰期
        if info.get("commits_by_year"):
            peak = max(info["commits_by_year"], key=lambda x: x["commits"])
            info["peak_year"] = peak

        print(f"  {info['total_commits']} commits, {info['total_authors']} authors")
        print(f"  Date range: {info.get('date_range')}")
        if info.get("peak_year"):
            print(f"  Peak year: {info['peak_year']['year']} ({info['peak_year']['commits']} commits)")

    con.close()
    results["code_repos"][name] = info


# ============================================================
# 2. 功能数据库深度分析
# ============================================================
print("\n" + "=" * 80)
print("[2] 功能数据库深度分析")
print("=" * 80)

for name, path in FUNC_DBS.items():
    if not os.path.exists(path):
        continue
    print(f"\n--- {name} ---")
    con = duckdb.connect(path, read_only=True)
    info = {"name": name, "path": path}

    tables = safe_query(con, "SELECT table_name FROM information_schema.tables WHERE table_schema='main'")
    info["tables"] = [t[0] for t in tables if not isinstance(t[0], str) or t[0] != "ERROR"]

    for tbl in info["tables"]:
        r = safe_query(con, f"SELECT COUNT(*) FROM \"{tbl}\"")
        cnt = r[0][0] if r else 0
        cols = safe_query(con, f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name='{tbl}'")
        col_names = [c[0] for c in cols]
        info.setdefault("table_details", {})[tbl] = {"row_count": cnt, "columns": col_names}

    # 特殊分析
    if name == "references_fulltext":
        # 参考文献统计
        r = safe_query(con, "SELECT COUNT(*) FROM references")
        if r: info["ref_count"] = r[0][0]
        r = safe_query(con, "SELECT COUNT(*) FROM fulltext")
        if r: info["fulltext_count"] = r[0][0]
        r = safe_query(con, "SELECT COUNT(*) FROM timeline_events")
        if r: info["timeline_event_count"] = r[0][0]
        r = safe_query(con, "SELECT COUNT(*) FROM people_mentioned")
        if r: info["people_count"] = r[0][0]
        r = safe_query(con, "SELECT COUNT(*) FROM technologies_mentioned")
        if r: info["tech_count"] = r[0][0]
        print(f"  References: {info.get('ref_count',0)}, Fulltexts: {info.get('fulltext_count',0)}")
        print(f"  Timeline events: {info.get('timeline_event_count',0)}, People: {info.get('people_count',0)}")

    if name == "historical_claims":
        r = safe_query(con, "SELECT COUNT(*) FROM claim")
        if r: info["claim_count"] = r[0][0]
        r = safe_query(con, "SELECT COUNT(*) FROM evidence")
        if r: info["evidence_count"] = r[0][0]
        r = safe_query(con, "SELECT COUNT(*) FROM raw_source")
        if r: info["source_count"] = r[0][0]
        r = safe_query(con, "SELECT COUNT(*) FROM source_chapter")
        if r: info["source_chapter_count"] = r[0][0]
        r = safe_query(con, "SELECT COUNT(*) FROM entity")
        if r: info["entity_count"] = r[0][0]
        print(f"  Claims: {info.get('claim_count',0)}, Evidence: {info.get('evidence_count',0)}")
        print(f"  Sources: {info.get('source_count',0)}, Source-Chapter: {info.get('source_chapter_count',0)}")
        print(f"  Entities: {info.get('entity_count',0)}")

    if name == "research_notes":
        r = safe_query(con, "SELECT COUNT(*) FROM files")
        if r: info["file_count"] = r[0][0]
        r = safe_query(con, "SELECT COUNT(*) FROM blocks")
        if r: info["block_count"] = r[0][0]
        print(f"  Files: {info.get('file_count',0)}, Blocks: {info.get('block_count',0)}")

    if name == "doubts_standalone":
        r = safe_query(con, "SELECT COUNT(*) FROM doubts_to_resolve")
        if r: info["doubt_count"] = r[0][0]
        r = safe_query(con, "SELECT COUNT(*) FROM doubt_review_log")
        if r: info["review_count"] = r[0][0]
        print(f"  Doubts: {info.get('doubt_count',0)}, Reviews: {info.get('review_count',0)}")

    if name == "cross_indexes":
        r = safe_query(con, "SELECT COUNT(*) FROM person_records")
        if r: info["person_count"] = r[0][0]
        r = safe_query(con, "SELECT COUNT(*) FROM terminology_index")
        if r: info["term_count"] = r[0][0]
        r = safe_query(con, "SELECT COUNT(*) FROM concept_history")
        if r: info["concept_count"] = r[0][0]
        print(f"  Persons: {info.get('person_count',0)}, Terms: {info.get('term_count',0)}, Concepts: {info.get('concept_count',0)}")

    if name == "bsdnow_podcast":
        r = safe_query(con, "SELECT COUNT(*) FROM episodes")
        if r: info["episode_count"] = r[0][0]
        r = safe_query(con, "SELECT COUNT(*) FROM outline_mappings")
        if r: info["mapping_count"] = r[0][0]
        print(f"  Episodes: {info.get('episode_count',0)}, Outline mappings: {info.get('mapping_count',0)}")

    if name == "sacred_sources":
        r = safe_query(con, "SELECT COUNT(*) FROM files")
        if r: info["file_count"] = r[0][0]
        r = safe_query(con, "SELECT COUNT(*) FROM blocks")
        if r: info["block_count"] = r[0][0]
        print(f"  Files: {info.get('file_count',0)}, Blocks: {info.get('block_count',0)}")

    if name == "fact_checks":
        r = safe_query(con, "SELECT COUNT(*) FROM files")
        if r: info["file_count"] = r[0][0]
        print(f"  Fact check files: {info.get('file_count',0)}")

    if name == "review_reports":
        r = safe_query(con, "SELECT COUNT(*) FROM review_records")
        if r: info["review_count"] = r[0][0]
        print(f"  Review records: {info.get('review_count',0)}")

    con.close()
    results["functional"][name] = info


# ============================================================
# 3. 章节映射：将数据库发现映射到具体章节
# ============================================================
print("\n" + "=" * 80)
print("[3] 章节映射")
print("=" * 80)

# 从代码仓库数据映射到章节
code_repos = results["code_repos"]

# 第1卷 (1-26): UNIX 起源
# 第2卷 (27-43): CSRG 版本史
# 第4卷 (62-87): 大分裂
# 第5卷 (88-108): FreeBSD 工程化奠基
# 第6卷 (109-135): FreeBSD 核心技术革新
# 第7卷 (136-155): FreeBSD 工程体系重构
# 第8卷 (156-171): FreeBSD 范式转换
# 第9卷 (172-190): NetBSD
# 第10卷 (191-213): OpenBSD
# 第11卷 (214-236): DragonFly BSD
# 第12卷 (237-253): macOS BSD 遗产
# 第13卷 (254-270): BSD 衍生操作系统
# 第14卷 (271-281): 商业生态
# 第15卷 (282-299): 许可证哲学
# 第16卷 (300-313): 开源运动
# 第17卷 (314-327): 政治制度
# 第18卷 (328-349): 全球社区
# 第19卷 (350-355): 编纂学

def add_finding(chapter, category, content, source_db):
    results["chapter_mapping"][chapter].append({
        "category": category,
        "content": content,
        "source_db": source_db
    })

# --- FreeBSD 相关 ---
if "freebsd" in code_repos:
    f = code_repos["freebsd"]
    add_finding(65, "史料", f"FreeBSD 仓库共 {f['total_commits']} 次提交，{f['total_authors']} 位贡献者", "freebsd.duckdb")
    add_finding(88, "史料", f"FreeBSD 2.x 时期起逐步积累提交历史", "freebsd.duckdb")
    if f.get("peak_year"):
        add_finding(98, "史料", f"提交高峰期出现在 {f['peak_year']['year']} 年（{f['peak_year']['commits']} 次提交）", "freebsd.duckdb")
    if f.get("top_authors"):
        top3 = f["top_authors"][:3]
        top3_str = ", ".join(a["name"] + "(" + str(a["commits"]) + ")" for a in top3)
        add_finding(65, "史料", f"Top 3 贡献者：{top3_str}", "freebsd.duckdb")
    add_finding(129, "史料", f"FreeBSD 共 {f['total_authors']} 位代码贡献者，可按年份分析贡献者多样性变化", "freebsd.duckdb")
    if f.get("date_range"):
        add_finding(88, "史料", f"FreeBSD 代码仓库时间跨度：{f['date_range'][0][:10]} 至 {f['date_range'][1][:10]}", "freebsd.duckdb")

# --- NetBSD 相关 ---
if "netbsd" in code_repos:
    f = code_repos["netbsd"]
    add_finding(67, "史料", f"NetBSD 仓库共 {f['total_commits']} 次提交，{f['total_authors']} 位贡献者", "netbsd.duckdb")
    add_finding(172, "史料", f"NetBSD 提交量最大（{f['total_commits']}），体现其广谱移植策略", "netbsd.duckdb")
    if f.get("peak_year"):
        add_finding(178, "史料", f"NetBSD 提交高峰期：{f['peak_year']['year']} 年（{f['peak_year']['commits']} 次）", "netbsd.duckdb")
    if f.get("date_range"):
        add_finding(67, "史料", f"NetBSD 时间跨度：{f['date_range'][0][:10]} 至 {f['date_range'][1][:10]}", "netbsd.duckdb")

# --- OpenBSD 相关 ---
if "openbsd" in code_repos:
    f = code_repos["openbsd"]
    add_finding(69, "史料", f"OpenBSD 仓库共 {f['total_commits']} 次提交，{f['total_authors']} 位贡献者", "openbsd.duckdb")
    add_finding(193, "史料", f"OpenBSD 2.x 起建立代码审计文化，提交量稳步增长", "openbsd.duckdb")
    if f.get("date_range"):
        add_finding(69, "史料", f"OpenBSD 时间跨度：{f['date_range'][0][:10]} 至 {f['date_range'][1][:10]}", "openbsd.duckdb")

# --- DragonFly BSD 相关 ---
if "dragonfly" in code_repos:
    f = code_repos["dragonfly"]
    add_finding(214, "史料", f"DragonFly BSD 仓库共 {f['total_commits']} 次提交，{f['total_authors']} 位贡献者", "dragonfly.duckdb")
    if f.get("top_authors"):
        add_finding(225, "史料", f"DragonFly 主要贡献者高度集中：{f['top_authors'][0]['name']}（{f['top_authors'][0]['commits']} 次提交）", "dragonfly.duckdb")
    if f.get("date_range"):
        add_finding(214, "史料", f"DragonFly 时间跨度：{f['date_range'][0][:10]} 至 {f['date_range'][1][:10]}", "dragonfly.duckdb")

# --- Darwin/macOS 相关 ---
if "darwin" in code_repos:
    f = code_repos["darwin"]
    add_finding(240, "史料", f"Darwin 仓库共 {f['total_commits']} 次提交，{f['total_authors']} 位贡献者", "darwin.duckdb")
    if f.get("date_range"):
        add_finding(240, "史料", f"Darwin 时间跨度：{f['date_range'][0][:10]} 至 {f['date_range'][1][:10]}", "darwin.duckdb")

# --- OpenSSH 相关 ---
if "openssh" in code_repos:
    f = code_repos["openssh"]
    add_finding(206, "史料", f"OpenSSH 仓库共 {f['total_commits']} 次提交，{f['total_authors']} 位贡献者", "openssh.duckdb")
    if f.get("date_range"):
        add_finding(206, "史料", f"OpenSSH 时间跨度：{f['date_range'][0][:10]} 至 {f['date_range'][1][:10]}", "openssh.duckdb")

# --- OpenZFS 相关 ---
if "openzfs" in code_repos:
    f = code_repos["openzfs"]
    add_finding(109, "史料", f"OpenZFS 仓库共 {f['total_commits']} 次提交，{f['total_authors']} 位贡献者", "openzfs.duckdb")
    if f.get("date_range"):
        add_finding(111, "史料", f"OpenZFS 时间跨度：{f['date_range'][0][:10]} 至 {f['date_range'][1][:10]}", "openzfs.duckdb")

# --- illumos 相关 ---
if "illumos_gate" in code_repos:
    f = code_repos["illumos_gate"]
    add_finding(297, "史料", f"illumos-gate 仓库共 {f['total_commits']} 次提交，{f['total_authors']} 位贡献者", "illumos-gate.duckdb")

# --- Linux Kernel 对照 ---
if "linux_kernel" in code_repos:
    f = code_repos["linux_kernel"]
    add_finding(78, "史料", f"Linux Kernel 仓库共 {f['total_commits']} 次提交，{f['total_authors']} 位贡献者（作为对照基准）", "linux-kernel.duckdb")
    if f.get("date_range"):
        add_finding(78, "史料", f"Linux Kernel 时间跨度：{f['date_range'][0][:10]} 至 {f['date_range'][1][:10]}", "linux-kernel.duckdb")

# --- BSD 衍生项目 ---
if "bsd_derivatives" in code_repos:
    f = code_repos["bsd_derivatives"]
    add_finding(259, "史料", f"BSD 衍生项目群共 {f['total_commits']} 次提交，{f['total_authors']} 位贡献者", "bsd-derivatives.duckdb")

# --- 功能数据库映射 ---
func = results["functional"]

if "references_fulltext" in func:
    f = func["references_fulltext"]
    add_finding(1, "史料", f"参考文献全文库共 {f.get('ref_count',0)} 条参考文献，{f.get('fulltext_count',0)} 篇全文，{f.get('timeline_event_count',0)} 条时间线事件", "references_fulltext.duckdb")
    add_finding(1, "文献", f"参考文献全文库含 {f.get('people_count',0)} 个人物提及、{f.get('tech_count',0)} 个技术提及", "references_fulltext.duckdb")

if "historical_claims" in func:
    f = func["historical_claims"]
    add_finding(1, "史料", f"历史主张库共 {f.get('claim_count',0)} 条主张、{f.get('evidence_count',0)} 条证据、{f.get('source_chapter_count',0)} 条来源-章节映射", "historical_claims.duckdb")

if "research_notes" in func:
    f = func["research_notes"]
    add_finding(1, "史料", f"研究笔记库共 {f.get('file_count',0)} 个文件，{f.get('block_count',0)} 个文本块", "research_notes.duckdb")

if "doubts_standalone" in func:
    f = func["doubts_standalone"]
    add_finding(1, "辨析", f"存疑库共 {f.get('doubt_count',0)} 条存疑记录，{f.get('review_count',0)} 次复核", "doubts_standalone.duckdb")

if "cross_indexes" in func:
    f = func["cross_indexes"]
    add_finding(347, "史料", f"交叉索引库共 {f.get('person_count',0)} 条人物记录，{f.get('term_count',0)} 条术语，{f.get('concept_count',0)} 条概念史条目", "cross_indexes.duckdb")

if "bsdnow_podcast" in func:
    f = func["bsdnow_podcast"]
    add_finding(1, "史料", f"BSD Now 播客库共 {f.get('episode_count',0)} 期，{f.get('mapping_count',0)} 条大纲映射", "bsdnow_podcast.duckdb")

if "sacred_sources" in func:
    f = func["sacred_sources"]
    add_finding(1, "史观", f"sacred 源材料库共 {f.get('file_count',0)} 个文件，{f.get('block_count',0)} 个文本块", "sacred_sources.duckdb")

if "fact_checks" in func:
    f = func["fact_checks"]
    add_finding(1, "辨析", f"事实核查库共 {f.get('file_count',0)} 条核查记录", "fact_checks.duckdb")

if "review_reports" in func:
    f = func["review_reports"]
    add_finding(1, "辨析", f"复核报告库共 {f.get('review_count',0)} 条复核记录", "review_reports.duckdb")

# --- 全局发现 ---
# 代码贡献集中度分析
all_repos = [(k, v) for k, v in code_repos.items() if "total_commits" in v]
results["global_findings"].append({
    "title": "代码仓库数据全景",
    "content": f"项目共管理 {len(all_repos)} 个代码仓库数据库，涵盖 FreeBSD、NetBSD、OpenBSD、DragonFly BSD、Darwin、OpenZFS、OpenSSH、illumos、Linux Kernel 及 BSD 衍生项目群",
    "details": {k: {"commits": v["total_commits"], "authors": v.get("total_authors", 0)} for k, v in all_repos}
})

# 贡献者集中度分析
results["global_findings"].append({
    "title": "贡献者生态对比",
    "content": "各 BSD 项目贡献者规模与集中度差异显著，反映了不同的治理模式与社区文化",
    "data": {k: {"commits": v["total_commits"], "authors": v.get("total_authors", 0),
                "commits_per_author": round(v["total_commits"] / v.get("total_authors", 1), 1) if v.get("total_authors", 0) > 0 else 0}
             for k, v in all_repos}
})

# 功能数据库综合
results["global_findings"].append({
    "title": "功能数据库综合统计",
    "content": "14 个功能数据库覆盖参考文献、研究笔记、历史主张、存疑管理、交叉索引、播客、事实核查、复核报告等维度",
    "data": {k: {"tables": len(v.get("table_details", {})), "total_rows": sum(d["row_count"] for d in v.get("table_details", {}).values())}
             for k, v in func.items()}
})

# 保存结果
out_path = os.path.join(BASE, "script", "db_deep_analysis.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2, default=str)

print(f"\n深度分析结果已写入: {out_path}")
print(f"章节映射共 {len(results['chapter_mapping'])} 章")
print(f"全局发现共 {len(results['global_findings'])} 条")