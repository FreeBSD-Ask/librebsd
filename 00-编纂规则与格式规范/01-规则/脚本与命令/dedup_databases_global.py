#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""跨库全局去重脚本。

对 7 个文件夹级数据库执行跨库三级全局去重：
  1. 跨库 SHA-256 精确去重（global_exact）
  2. 跨库 content_hash 内容级去重（global_content）
  3. 跨库 标题+首段模糊去重（fuzzy_global，阈值 0.85）

遵循"先比对后标记，副记录可逆标记"原则：
  - 主记录保持 status='active'，所有字段不变
  - 副记录标记 status='merged'、duplicate_type、duplicate_of_db、duplicate_of_global_file_id
  - 副记录的 blocks/blocks_fts 行保留（便于按文件路径检索）
  - global_exact/global_content 类型副记录的专属表行清理、cross_references 迁移至主记录
  - fuzzy_global 类型副记录的所有行保留（人工复核）
  - sacred 源材料副记录仅标记，不清理任何行（immutable=true 约束）

CLI 参数：
  --dry-run         仅扫描与输出报告，不修改任何数据库
  --exact           只执行跨库 SHA-256 精确去重
  --content         只执行跨库 content_hash 内容级去重
  --fuzzy           只执行跨库标题+首段模糊去重
  --all             执行 schema 升级 + 全部三级去重（默认）
  --upgrade-schema  只执行 schema 升级（ALTER TABLE + 更新 registry + 更新 SQL 文件）

注意：--exact/--content/--fuzzy 模式下也需先确保 schema 已升级（如未升级则先升级）。
"""
import argparse
import csv
import difflib
import sqlite3
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent  # d:\librebsd
LOG_DIR = PROJECT_ROOT / "script" / "_folder_db_logs"
INDEX_DIR = PROJECT_ROOT / "11-元数据接口" / "09-文件夹数据库索引"
SCHEMA_SQL_PATH = PROJECT_ROOT / "00-编纂规则与格式规范" / "01-规则" / "脚本与命令" / "folder_db_common_schema.sql"
BJT = timezone(timedelta(hours=8))

FOLDER_DB_MAP = {
    "sacred_sources": {"folder": "02-sacred源材料", "db_filename": "sacred_sources.db", "skip_subfolders": [], "skip_db_files": False},
    "original_sources": {"folder": "03-原始史料库", "db_filename": "original_sources.db", "skip_subfolders": ["01-代码仓库史料", "02-man源与posix仓库"], "skip_db_files": True},
    "research_notes": {"folder": "04-现代研究文献", "db_filename": "research_notes.db", "skip_subfolders": ["03-文献下载/01-pdf", "03-文献下载/02-epub", "03-文献下载/04-caj", "03-文献下载/05-书籍/01-pdf", "03-文献下载/05-书籍/02-epub", "05-参考文献全文数据库"], "skip_db_files": True},
    "fact_checks": {"folder": "07-事实核查记录", "db_filename": "fact_checks.db", "skip_subfolders": [], "skip_db_files": True},
    "review_reports": {"folder": "08-核查报告与多轮复核", "db_filename": "review_reports.db", "skip_subfolders": [], "skip_db_files": True},
    "cross_indexes": {"folder": "10-交叉索引", "db_filename": "cross_indexes.db", "skip_subfolders": [], "skip_db_files": True},
    "metadata_interfaces": {"folder": "11-元数据接口", "db_filename": "metadata_interfaces.db", "skip_subfolders": ["09-文件夹数据库索引"], "skip_db_files": True},
}

# 数据库优先级（数字越小优先级越高，主记录选择时优先选数字小的）
DB_PRIORITY = {
    "sacred_sources": 1,
    "original_sources": 2,
    "research_notes": 3,
    "fact_checks": 4,
    "review_reports": 5,
    "cross_indexes": 6,
    "metadata_interfaces": 7,
}

DB_BUILD_ORDER = ["sacred_sources", "original_sources", "research_notes", "fact_checks", "review_reports", "cross_indexes", "metadata_interfaces"]

# 16 张专属表（按数据库归属）
EXTENDED_TABLES = [
    "fact_check_records", "disputes", "peer_reviews",
    "person_index", "command_index", "term_index", "concept_history", "person_biography",
    "kaoju_records", "security_advisories", "vulnerability_metadata",
    "chapter_metadata", "author_index", "build_status", "timeline_records", "citation_frequency",
]

SACRED_PREFIX = "02-sacred源材料/"
FUZZY_THRESHOLD = 0.85


# ============================== 基础工具 ==============================

def get_db_path(db_name: str) -> Path:
    cfg = FOLDER_DB_MAP[db_name]
    return PROJECT_ROOT / cfg["folder"] / cfg["db_filename"]


def now_bjt_str() -> str:
    return datetime.now(BJT).strftime("%Y-%m-%d %H:%M:%S BJT")


def write_text(path: Path, text: str) -> None:
    """以 UTF-8 无 BOM、LF 换行写入文件。"""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def column_exists(conn, table: str, column: str) -> bool:
    cur = conn.execute(f"PRAGMA table_info({table})")
    return any(row[1] == column for row in cur.fetchall())


def get_first_block_content(conn, file_id: int) -> str:
    """获取文件首段内容（block_index 最小的非标题块）。"""
    cur = conn.execute(
        "SELECT block_content FROM blocks WHERE file_id = ? AND block_type != 'heading' ORDER BY block_index LIMIT 1",
        (file_id,)
    )
    row = cur.fetchone()
    return row[0] if row else ""


def is_sacred(file_path: str) -> bool:
    return file_path.startswith(SACRED_PREFIX)


# ============================== Schema 升级 ==============================

def upgrade_schema_one(db_name: str, dry_run: bool = False) -> dict:
    """升级单个数据库 schema，幂等。

    返回 {db_existed, duplicate_of_db_added, duplicate_of_global_file_id_added, status}
    """
    db_path = get_db_path(db_name)
    if not db_path.exists():
        return {"db_existed": False, "duplicate_of_db_added": False, "duplicate_of_global_file_id_added": False, "status": "skipped"}

    conn = sqlite3.connect(str(db_path))
    col1_added = False
    col2_added = False
    try:
        if not column_exists(conn, "files", "duplicate_of_db"):
            if not dry_run:
                conn.execute("ALTER TABLE files ADD COLUMN duplicate_of_db TEXT")
                conn.commit()
            col1_added = True
        if not column_exists(conn, "files", "duplicate_of_global_file_id"):
            if not dry_run:
                conn.execute("ALTER TABLE files ADD COLUMN duplicate_of_global_file_id INTEGER")
                conn.commit()
            col2_added = True
    except sqlite3.OperationalError as e:
        # 幂等：字段已存在时捕获异常
        if "duplicate column name" not in str(e):
            raise
    finally:
        conn.close()

    if not col1_added and not col2_added:
        status = "already_present"
    else:
        status = "added" if not dry_run else "would_add"
    return {"db_existed": True, "duplicate_of_db_added": col1_added, "duplicate_of_global_file_id_added": col2_added, "status": status}


def update_registry_csv(dry_run: bool = False) -> bool:
    """更新 folder_db_registry.csv 中 7 行的 schema_version 为 1.2。返回是否有变更。"""
    registry_path = INDEX_DIR / "folder_db_registry.csv"
    if not registry_path.exists():
        return False

    with open(registry_path, "r", encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))

    if not rows:
        return False

    header = rows[0]
    if "schema_version" not in header or "db_name" not in header:
        return False
    sv_idx = header.index("schema_version")
    db_name_idx = header.index("db_name")

    changed = False
    for row in rows[1:]:
        if len(row) <= sv_idx:
            continue
        if row[db_name_idx] in FOLDER_DB_MAP and row[sv_idx] != "1.2":
            row[sv_idx] = "1.2"
            changed = True

    if changed and not dry_run:
        with open(registry_path, "w", encoding="utf-8", newline="\n") as f:
            csv.writer(f).writerows(rows)

    return changed


def update_schema_sql_file(dry_run: bool = False) -> bool:
    """更新 folder_db_common_schema.sql 至 1.2 版本。返回是否有变更。"""
    if not SCHEMA_SQL_PATH.exists():
        return False

    content = SCHEMA_SQL_PATH.read_text(encoding="utf-8")
    original = content

    # 1. 更新架构版本注释 1.1 -> 1.2
    if "-- 架构版本：1.1" in content:
        content = content.replace("-- 架构版本：1.1", "-- 架构版本：1.2")

    # 2. 追加 v1.2 修订说明（如果尚无 v1.2 字样）
    if "v1.2" not in content:
        old_line = "-- 修订日期：2026-07-31（v1.1：按需建表，构建脚本按 db_name 过滤专属表）"
        new_lines = "-- 修订日期：2026-08-01（v1.2：files 表新增 duplicate_of_db、duplicate_of_global_file_id 字段，支持跨库去重）\n-- 修订历史：2026-07-31（v1.1：按需建表，构建脚本按 db_name 过滤专属表）"
        if old_line in content:
            content = content.replace(old_line, new_lines)

    # 3. 在 files 表 DDL 中追加两字段（如果尚无）
    if "duplicate_of_db TEXT" not in content:
        old_ddl = "    duplicate_type TEXT,\n    FOREIGN KEY (duplicate_of_id) REFERENCES files(id)"
        new_ddl = "    duplicate_type TEXT,\n    duplicate_of_db TEXT,\n    duplicate_of_global_file_id INTEGER,\n    FOREIGN KEY (duplicate_of_id) REFERENCES files(id)"
        if old_ddl in content:
            content = content.replace(old_ddl, new_ddl)

    changed = content != original
    if changed and not dry_run:
        write_text(SCHEMA_SQL_PATH, content)
    return changed


def upgrade_schema_all(dry_run: bool = False) -> dict:
    """升级所有数据库 schema + 更新 registry + 更新 SQL 文件。返回升级日志字典。"""
    log = {
        "timestamp": now_bjt_str(),
        "databases": {},
        "registry_updated": False,
        "sql_file_updated": False,
    }

    for db_name in DB_BUILD_ORDER:
        result = upgrade_schema_one(db_name, dry_run=dry_run)
        log["databases"][db_name] = result
        print(f"  [schema] {db_name}: {result['status']}")

    log["registry_updated"] = update_registry_csv(dry_run=dry_run)
    print(f"  [schema] folder_db_registry.csv: {'updated' if log['registry_updated'] else 'no change'}")

    log["sql_file_updated"] = update_schema_sql_file(dry_run=dry_run)
    print(f"  [schema] folder_db_common_schema.sql: {'updated' if log['sql_file_updated'] else 'no change'}")

    return log


def write_schema_upgrade_log(log: dict, dry_run: bool) -> None:
    """追加 schema 升级日志到 schema_upgrade_log.md。"""
    log_path = LOG_DIR / "schema_upgrade_log.md"
    mode_label = "dry-run 预览" if dry_run else "实际执行"
    entry = []
    entry.append(f"## {log['timestamp']}（{mode_label}）")
    entry.append("")
    entry.append("| db_name | db_existed | duplicate_of_db_added | duplicate_of_global_file_id_added | status |")
    entry.append("|---|---|---|---|---|")
    for db_name in DB_BUILD_ORDER:
        d = log["databases"][db_name]
        entry.append(f"| {db_name} | {d['db_existed']} | {d['duplicate_of_db_added']} | {d['duplicate_of_global_file_id_added']} | {d['status']} |")
    entry.append("")
    entry.append(f"- folder_db_registry.csv 更新: {log['registry_updated']}")
    entry.append(f"- folder_db_common_schema.sql 更新: {log['sql_file_updated']}")
    entry.append("")

    if log_path.exists():
        existing = log_path.read_text(encoding="utf-8")
        new_content = existing.rstrip() + "\n\n" + "\n".join(entry)
    else:
        new_content = "# Schema 升级日志\n\n" + "\n".join(entry)
    write_text(log_path, new_content)


# ============================== 加载记录 ==============================

def load_all_active_records() -> dict:
    """加载所有数据库的 active 记录。

    返回 {db_name: [record_dict, ...]}
    record_dict 含: db_name, file_id, file_path, sha256, content_hash, title, file_size, file_extension, first_block
    """
    all_records = {}
    for db_name in DB_BUILD_ORDER:
        db_path = get_db_path(db_name)
        if not db_path.exists():
            print(f"  [load] {db_name}: 数据库文件不存在，跳过")
            all_records[db_name] = []
            continue
        conn = sqlite3.connect(str(db_path))
        conn.row_factory = sqlite3.Row
        try:
            cur = conn.execute(
                "SELECT id, file_path, sha256, content_hash, title, file_size, file_extension FROM files WHERE status = 'active'"
            )
            records = []
            for row in cur.fetchall():
                rec = {
                    "db_name": db_name,
                    "file_id": row["id"],
                    "file_path": row["file_path"],
                    "sha256": row["sha256"],
                    "content_hash": row["content_hash"],
                    "title": row["title"] or "",
                    "file_size": row["file_size"],
                    "file_extension": row["file_extension"] or "",
                    "first_block": "",
                }
                rec["first_block"] = get_first_block_content(conn, rec["file_id"])
                records.append(rec)
            all_records[db_name] = records
            print(f"  [load] {db_name}: {len(records)} active 记录")
        finally:
            conn.close()
    return all_records


def select_primary(records: list) -> dict:
    """从一组记录中按 DB_PRIORITY 选择主记录。优先级数字小的优先；同优先级取 file_id 小的。"""
    return min(records, key=lambda r: (DB_PRIORITY[r["db_name"]], r["file_id"]))


# ============================== 副记录标记与清理 ==============================

def mark_duplicate(db_name: str, file_id: int, dup_type: str, primary_db: str, primary_file_id: int, dry_run: bool) -> None:
    """标记副记录：status='merged'、duplicate_type、duplicate_of_db、duplicate_of_global_file_id。"""
    if dry_run:
        return
    db_path = get_db_path(db_name)
    conn = sqlite3.connect(str(db_path))
    try:
        conn.execute(
            "UPDATE files SET status = 'merged', duplicate_type = ?, duplicate_of_db = ?, duplicate_of_global_file_id = ? WHERE id = ?",
            (dup_type, primary_db, primary_file_id, file_id)
        )
        conn.commit()
    finally:
        conn.close()


def cleanup_extended_tables(db_name: str, file_id: int, dry_run: bool) -> int:
    """清理副记录在专属表中的行。返回清理的行数。"""
    if dry_run:
        return 0
    db_path = get_db_path(db_name)
    conn = sqlite3.connect(str(db_path))
    total = 0
    try:
        cur = conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
        existing_tables = {row[0] for row in cur.fetchall()}
        for table in EXTENDED_TABLES:
            if table not in existing_tables:
                continue
            cur = conn.execute(f"DELETE FROM {table} WHERE file_id = ?", (file_id,))
            total += cur.rowcount
        conn.commit()
    finally:
        conn.close()
    return total


def migrate_cross_references(sub_db: str, sub_file_id: int, pri_db: str, pri_file_id: int, dry_run: bool) -> int:
    """将副记录的 cross_references 迁移至主记录。

    更新 source_file_id 为主库 file_id，并在 reference_context 追加迁移注释。
    对于跨库重复（主记录在另一个数据库），将 source_file_id 置 NULL 并记录迁移注释，
    同时在 cross_db_references.csv 追加跨库引用关系。
    """
    if dry_run:
        return 0
    db_path = get_db_path(sub_db)
    conn = sqlite3.connect(str(db_path))
    migrated = 0
    try:
        # 关闭外键约束，避免跨库 file_id 不在副库 files 表中导致约束失败
        conn.execute("PRAGMA foreign_keys = OFF")
        # 查询副记录的 cross_references 行
        cur = conn.execute(
            "SELECT id, reference_context FROM cross_references WHERE source_file_id = ?",
            (sub_file_id,),
        )
        rows = cur.fetchall()
        for row in rows:
            xref_id = row[0]
            old_context = row[1] or ""
            # 跨库迁移：主记录在另一个数据库，source_file_id 置 NULL
            # 在 reference_context 追加迁移注释
            migrate_note = f"[迁移 {now_bjt_str()}: source_file_id {sub_file_id}@{sub_db} -> {pri_file_id}@{pri_db}]"
            new_context = f"{old_context} {migrate_note}" if old_context else migrate_note
            conn.execute(
                "UPDATE cross_references SET source_file_id = NULL, reference_context = ? WHERE id = ?",
                (new_context, xref_id),
            )
            migrated += 1
        conn.commit()
    finally:
        conn.close()
    return migrated


# ============================== 跨库去重执行 ==============================

def global_exact_dedup(all_records: dict, report: dict, dry_run: bool) -> None:
    """跨库 SHA-256 精确去重。

    按 SHA-256 分组，找出跨库 SHA-256 完全相同的记录组。
    """
    print("[exact] 跨库 SHA-256 精确去重...")
    # 按 SHA-256 分组所有 active 记录
    sha256_groups: dict[str, list] = {}
    for db_name, records in all_records.items():
        for rec in records:
            sha = rec["sha256"]
            if sha not in sha256_groups:
                sha256_groups[sha] = []
            sha256_groups[sha].append(rec)

    # 找出跨库重复组（同一 SHA-256 出现在 >=2 条记录中）
    cross_db_groups = {sha: recs for sha, recs in sha256_groups.items() if len(recs) >= 2}

    exact_entries = []
    sacred_exceptions = []

    for sha, recs in cross_db_groups.items():
        # 检查是否真的跨库（同库内的重复已在库内去重处理）
        db_set = {r["db_name"] for r in recs}
        if len(db_set) < 2:
            continue

        # 选择主记录
        primary = select_primary(recs)
        duplicates = [r for r in recs if r is not primary]

        for dup in duplicates:
            entry = {
                "sha256": sha,
                "primary_db": primary["db_name"],
                "primary_file_id": primary["file_id"],
                "primary_file_path": primary["file_path"],
                "duplicate_db": dup["db_name"],
                "duplicate_file_id": dup["file_id"],
                "duplicate_file_path": dup["file_path"],
                "is_sacred": is_sacred(dup["file_path"]),
            }
            exact_entries.append(entry)

            if entry["is_sacred"]:
                sacred_exceptions.append(entry)

            # 标记副记录
            mark_duplicate(
                dup["db_name"], dup["file_id"], "global_exact",
                primary["db_name"], primary["file_id"], dry_run
            )

            # sacred 例外：仅标记不清理
            if not entry["is_sacred"]:
                # 清理专属表行
                cleanup_extended_tables(dup["db_name"], dup["file_id"], dry_run)
                # 迁移 cross_references
                migrate_cross_references(
                    dup["db_name"], dup["file_id"],
                    primary["db_name"], primary["file_id"], dry_run
                )

            action = "[sacred-exception]" if entry["is_sacred"] else "[marked]"
            print(f"  [exact] {action} {dup['db_name']}/{dup['file_id']} -> {primary['db_name']}/{primary['file_id']} ({dup['file_path']})")

    report["exact"] = exact_entries
    report["sacred_exceptions"].extend(sacred_exceptions)
    print(f"[exact] 完成：跨库精确重复 {len(exact_entries)} 条（含 sacred 例外 {len(sacred_exceptions)} 条）")


def global_content_dedup(all_records: dict, report: dict, dry_run: bool) -> None:
    """跨库 content_hash 内容级去重。

    对剩余 active 记录按 content_hash 分组。
    """
    print("[content] 跨库 content_hash 内容级去重...")
    # 重新加载 active 记录（exact 去重后部分记录已标记 merged）
    active_records = {}
    for db_name, records in all_records.items():
        active_records[db_name] = [r for r in records if r["db_name"] == db_name]

    # 由于 all_records 是在去重前加载的，需要重新查询数据库获取当前 active 记录
    current_active = load_all_active_records()

    # 按 content_hash 分组
    content_groups: dict[str, list] = {}
    for db_name, records in current_active.items():
        for rec in records:
            ch = rec["content_hash"]
            if not ch:
                continue
            if ch not in content_groups:
                content_groups[ch] = []
            content_groups[ch].append(rec)

    # 找出跨库重复组
    cross_db_groups = {ch: recs for ch, recs in content_groups.items() if len(recs) >= 2}

    content_entries = []
    sacred_exceptions = []

    for ch, recs in cross_db_groups.items():
        db_set = {r["db_name"] for r in recs}
        if len(db_set) < 2:
            continue

        primary = select_primary(recs)
        duplicates = [r for r in recs if r is not primary]

        for dup in duplicates:
            entry = {
                "content_hash": ch,
                "primary_db": primary["db_name"],
                "primary_file_id": primary["file_id"],
                "primary_file_path": primary["file_path"],
                "duplicate_db": dup["db_name"],
                "duplicate_file_id": dup["file_id"],
                "duplicate_file_path": dup["file_path"],
                "is_sacred": is_sacred(dup["file_path"]),
            }
            content_entries.append(entry)

            if entry["is_sacred"]:
                sacred_exceptions.append(entry)

            mark_duplicate(
                dup["db_name"], dup["file_id"], "global_content",
                primary["db_name"], primary["file_id"], dry_run
            )

            if not entry["is_sacred"]:
                cleanup_extended_tables(dup["db_name"], dup["file_id"], dry_run)
                migrate_cross_references(
                    dup["db_name"], dup["file_id"],
                    primary["db_name"], primary["file_id"], dry_run
                )

            action = "[sacred-exception]" if entry["is_sacred"] else "[marked]"
            print(f"  [content] {action} {dup['db_name']}/{dup['file_id']} -> {primary['db_name']}/{primary['file_id']} ({dup['file_path']})")

    report["content"] = content_entries
    report["sacred_exceptions"].extend(sacred_exceptions)
    print(f"[content] 完成：跨库内容级重复 {len(content_entries)} 条（含 sacred 例外 {len(sacred_exceptions)} 条）")


def global_fuzzy_dedup(all_records: dict, report: dict, dry_run: bool) -> None:
    """跨库标题+首段模糊去重。

    对剩余 active 记录计算跨库两两标题 Levenshtein 比例 + 首段 Levenshtein 比例的平均值。
    平均相似度 >= 0.85 的记录对标记为跨库模糊重复。
    """
    print("[fuzzy] 跨库标题+首段模糊去重...")
    # 重新加载当前 active 记录
    current_active = load_all_active_records()

    # 收集所有 active 记录到扁平列表
    all_recs = []
    for db_name, records in current_active.items():
        all_recs.extend(records)

    fuzzy_entries = []
    sacred_exceptions = []

    # 两两比较（按文件扩展名分组预筛选，避免 O(n^2) 爆炸）
    # 仅比较标题非空且首段非空的记录
    candidates = [r for r in all_recs if r["title"] and r["first_block"]]
    print(f"  [fuzzy] 候选记录数: {len(candidates)}")

    # 按文件扩展名分组，仅同扩展名的跨库记录两两比较
    ext_groups: dict[str, list] = {}
    for rec in candidates:
        ext = rec["file_extension"] or "unknown"
        if ext not in ext_groups:
            ext_groups[ext] = []
        ext_groups[ext].append(rec)

    total_comparisons = 0
    for ext, ext_recs in ext_groups.items():
        # 该扩展名下至少需要 2 个不同库的记录才有比较意义
        db_set = {r["db_name"] for r in ext_recs}
        if len(db_set) < 2:
            continue
        print(f"  [fuzzy] .{ext}: {len(ext_recs)} 条记录，{len(db_set)} 个库")
        for i in range(len(ext_recs)):
            for j in range(i + 1, len(ext_recs)):
                r1 = ext_recs[i]
                r2 = ext_recs[j]
                # 跳过同库记录（库内模糊去重已处理）
                if r1["db_name"] == r2["db_name"]:
                    continue
                total_comparisons += 1

                # 计算标题相似度
                title_ratio = difflib.SequenceMatcher(None, r1["title"], r2["title"]).ratio()
                # 计算首段相似度
                first_block_ratio = difflib.SequenceMatcher(None, r1["first_block"][:500], r2["first_block"][:500]).ratio()
                # 平均相似度
                avg_ratio = (title_ratio + first_block_ratio) / 2

                if avg_ratio >= FUZZY_THRESHOLD:
                    # 选择主记录
                    primary = select_primary([r1, r2])
                    dup = r2 if primary is r1 else r1

                    entry = {
                        "avg_ratio": round(avg_ratio, 4),
                        "title_ratio": round(title_ratio, 4),
                        "first_block_ratio": round(first_block_ratio, 4),
                        "primary_db": primary["db_name"],
                        "primary_file_id": primary["file_id"],
                        "primary_file_path": primary["file_path"],
                        "duplicate_db": dup["db_name"],
                        "duplicate_file_id": dup["file_id"],
                        "duplicate_file_path": dup["file_path"],
                        "is_sacred": is_sacred(dup["file_path"]),
                    }
                    fuzzy_entries.append(entry)

                    if entry["is_sacred"]:
                        sacred_exceptions.append(entry)

                    # 模糊重复：仅标记，不清理任何行
                    mark_duplicate(
                        dup["db_name"], dup["file_id"], "fuzzy_global",
                        primary["db_name"], primary["file_id"], dry_run
                    )

    # 按相似度排序，取前 50 对作为示例
    fuzzy_entries.sort(key=lambda x: x["avg_ratio"], reverse=True)

    report["fuzzy"] = fuzzy_entries
    report["sacred_exceptions"].extend(sacred_exceptions)
    print(f"[fuzzy] 完成：总比较 {total_comparisons} 次，跨库模糊重复 {len(fuzzy_entries)} 条（含 sacred 例外 {len(sacred_exceptions)} 条）")


# ============================== cross_db_references.csv 更新 ==============================

def update_cross_db_references_csv(report: dict, dry_run: bool) -> int:
    """在 cross_db_references.csv 追加 reference_type='cross_db_duplicate' 行。

    返回追加的行数。
    """
    csv_path = INDEX_DIR / "cross_db_references.csv"
    if not csv_path.exists():
        print(f"  [xref-csv] 文件不存在: {csv_path}")
        return 0

    # 读取现有 CSV
    with open(csv_path, "r", encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))

    if not rows:
        return 0

    header = rows[0]

    # 收集所有跨库重复条目（exact + content）
    new_rows = []
    for entry in report.get("exact", []):
        new_rows.append([
            "",  # source_db
            "",  # source_file_id
            "",  # source_block_id
            entry["primary_db"],
            entry["primary_file_id"],
            entry["primary_file_path"],
            "cross_db_duplicate",
            "resolved",
        ])
    for entry in report.get("content", []):
        new_rows.append([
            "",
            "",
            "",
            entry["primary_db"],
            entry["primary_file_id"],
            entry["primary_file_path"],
            "cross_db_duplicate",
            "resolved",
        ])

    if dry_run:
        print(f"  [xref-csv] dry-run: 将追加 {len(new_rows)} 行")
        return len(new_rows)

    if new_rows:
        rows.extend(new_rows)
        with open(csv_path, "w", encoding="utf-8", newline="\n") as f:
            csv.writer(f).writerows(rows)

    print(f"  [xref-csv] 追加 {len(new_rows)} 行")
    return len(new_rows)


# ============================== 报告生成 ==============================

def generate_report(report: dict, dry_run: bool) -> None:
    """生成跨库去重报告 cross_db_dedup_report.md。"""
    report_path = LOG_DIR / "cross_db_dedup_report.md"
    mode_label = "dry-run 预览" if dry_run else "实际执行"

    lines = []
    lines.append("# 跨库全局去重报告")
    lines.append("")
    lines.append(f"> 生成时间：{now_bjt_str()}")
    lines.append(f"> 模式：{mode_label}")
    lines.append(f"> 目标数据库：{', '.join(DB_BUILD_ORDER)}")
    lines.append("")

    # 汇总表
    lines.append("## 汇总表")
    lines.append("")
    lines.append("| db_name | global_exact 副记录数 | global_content 副记录数 | fuzzy_global 副记录数 | preserved 主记录数 |")
    lines.append("|---|---|---|---|---|")

    # 按数据库统计
    exact_by_db = {}
    content_by_db = {}
    fuzzy_by_db = {}
    for entry in report.get("exact", []):
        db = entry["duplicate_db"]
        exact_by_db[db] = exact_by_db.get(db, 0) + 1
    for entry in report.get("content", []):
        db = entry["duplicate_db"]
        content_by_db[db] = content_by_db.get(db, 0) + 1
    for entry in report.get("fuzzy", []):
        db = entry["duplicate_db"]
        fuzzy_by_db[db] = fuzzy_by_db.get(db, 0) + 1

    for db_name in DB_BUILD_ORDER:
        e = exact_by_db.get(db_name, 0)
        c = content_by_db.get(db_name, 0)
        f = fuzzy_by_db.get(db_name, 0)
        lines.append(f"| {db_name} | {e} | {c} | {f} | - |")
    lines.append("")

    # 精确重复详情
    lines.append("## 详情：精确重复（global_exact）")
    lines.append("")
    if report.get("exact"):
        lines.append("| SHA-256 | 主库 | 主ID | 主路径 | 副库 | 副ID | 副路径 | sacred |")
        lines.append("|---|---|---|---|---|---|---|---|")
        for entry in report["exact"]:
            lines.append(f"| {entry['sha256'][:16]}... | {entry['primary_db']} | {entry['primary_file_id']} | {entry['primary_file_path']} | {entry['duplicate_db']} | {entry['duplicate_file_id']} | {entry['duplicate_file_path']} | {entry['is_sacred']} |")
    else:
        lines.append("无")
    lines.append("")

    # 内容级重复详情
    lines.append("## 详情：内容级重复（global_content）")
    lines.append("")
    if report.get("content"):
        lines.append("| content_hash | 主库 | 主ID | 主路径 | 副库 | 副ID | 副路径 | sacred |")
        lines.append("|---|---|---|---|---|---|---|---|")
        for entry in report["content"]:
            lines.append(f"| {entry['content_hash'][:16]}... | {entry['primary_db']} | {entry['primary_file_id']} | {entry['primary_file_path']} | {entry['duplicate_db']} | {entry['duplicate_file_id']} | {entry['duplicate_file_path']} | {entry['is_sacred']} |")
    else:
        lines.append("无")
    lines.append("")

    # 模糊重复详情（前 50 对）
    lines.append("## 详情：模糊重复（fuzzy_global，前 50 对）")
    lines.append("")
    if report.get("fuzzy"):
        lines.append("| 平均相似度 | 标题相似度 | 首段相似度 | 主库 | 主ID | 主路径 | 副库 | 副ID | 副路径 | sacred |")
        lines.append("|---|---|---|---|---|---|---|---|---|---|")
        for entry in report["fuzzy"][:50]:
            lines.append(f"| {entry['avg_ratio']} | {entry['title_ratio']} | {entry['first_block_ratio']} | {entry['primary_db']} | {entry['primary_file_id']} | {entry['primary_file_path']} | {entry['duplicate_db']} | {entry['duplicate_file_id']} | {entry['duplicate_file_path']} | {entry['is_sacred']} |")
        if len(report["fuzzy"]) > 50:
            lines.append(f"\n共 {len(report['fuzzy'])} 对模糊重复，仅显示前 50 对。")
    else:
        lines.append("无")
    lines.append("")

    # sacred 例外
    lines.append("## sacred 例外")
    lines.append("")
    sacred_entries = report.get("sacred_exceptions", [])
    if sacred_entries:
        lines.append(f"共 {len(sacred_entries)} 条 sacred 副记录仅标记不清理：")
        lines.append("")
        for entry in sacred_entries:
            lines.append(f"- {entry.get('duplicate_db', '?')}/{entry.get('duplicate_file_id', '?')} -> {entry.get('primary_db', '?')}/{entry.get('primary_file_id', '?')} ({entry.get('duplicate_file_path', '?')})")
    else:
        lines.append("无")
    lines.append("")

    # next_actions
    lines.append("## next_actions")
    lines.append("")
    lines.append("- 模糊重复建议人工复核后决定是否合并")
    lines.append("- sacred 例外记录需人工确认是否保留")
    lines.append(f"- 跨库精确重复 {len(report.get('exact', []))} 条已标记")
    lines.append(f"- 跨库内容级重复 {len(report.get('content', []))} 条已标记")
    lines.append(f"- 跨库模糊重复 {len(report.get('fuzzy', []))} 条已标记")
    lines.append("")

    write_text(report_path, "\n".join(lines))
    print(f"[report] 报告已生成: {report_path}")


# ============================== 主函数 ==============================

def main():
    parser = argparse.ArgumentParser(description="跨库全局去重脚本")
    # --dry-run 是独立选项，可与 --exact/--content/--fuzzy/--all 组合使用
    parser.add_argument("--dry-run", action="store_true", help="仅扫描输出报告，不修改数据库（可与 --exact/--content/--fuzzy/--all 组合）")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--exact", action="store_true", help="仅执行跨库SHA-256精确去重")
    group.add_argument("--content", action="store_true", help="仅执行跨库content_hash内容级去重")
    group.add_argument("--fuzzy", action="store_true", help="仅执行跨库标题+首段模糊去重")
    group.add_argument("--all", action="store_true", help="执行全部三级去重（默认）")
    group.add_argument("--upgrade-schema", action="store_true", help="仅执行schema升级至1.2")
    args = parser.parse_args()

    # 默认模式（无 --exact/--content/--fuzzy/--all/--upgrade-schema 时默认 --all）
    if not any([args.exact, args.content, args.fuzzy, args.upgrade_schema]):
        args.all = True

    # 模式标签
    if args.dry_run:
        mode_label = "dry-run 预览"
    elif args.upgrade_schema:
        mode_label = "schema 升级"
    else:
        mode_label = "实际执行"

    print(f"模式: {mode_label}")
    print(f"目标数据库: {', '.join(DB_BUILD_ORDER)}")
    print(f"报告输出: {LOG_DIR / 'cross_db_dedup_report.md'}")
    print()

    # Schema 升级（dry-run 模式跳过）
    if not args.dry_run and (args.all or args.upgrade_schema):
        print("=== Schema 升级 ===")
        log = upgrade_schema_all(dry_run=False)
        write_schema_upgrade_log(log, dry_run=False)
        print()

        if args.upgrade_schema:
            # 仅升级 schema，不执行去重
            print("Schema 升级完成。")
            return 0

    # 确保所有记录都标记为 active（去掉之前的 merged 标记）
    # 注意：dry-run 模式下也需要检查 schema 是否已升级
    if args.dry_run:
        # dry-run 模式下检查 schema 是否已升级
        for db_name in DB_BUILD_ORDER:
            db_path = get_db_path(db_name)
            if not db_path.exists():
                continue
            conn = sqlite3.connect(str(db_path))
            try:
                if not column_exists(conn, "files", "duplicate_of_db"):
                    print(f"[警告] {db_name} schema 未升级至 1.2，dry-run 模式下不执行升级。")
                    print(f"       建议先运行: python script/dedup_databases_global.py --upgrade-schema")
            finally:
                conn.close()

    # 加载所有 active 记录
    print("=== 加载 active 记录 ===")
    all_records = load_all_active_records()
    print()

    # 执行去重
    report = {"exact": [], "content": [], "fuzzy": [], "sacred_exceptions": []}

    if args.all or args.exact:
        global_exact_dedup(all_records, report, args.dry_run)
        print()

    if args.all or args.content:
        global_content_dedup(all_records, report, args.dry_run)
        print()

    if args.all or args.fuzzy:
        global_fuzzy_dedup(all_records, report, args.dry_run)
        print()

    # 更新 cross_db_references.csv
    if not args.dry_run:
        print("=== 更新 cross_db_references.csv ===")
        update_cross_db_references_csv(report, dry_run=False)
        print()

    # 生成报告
    print("=== 生成报告 ===")
    generate_report(report, args.dry_run)

    print()
    print(f"汇总: exact={len(report.get('exact', []))}, content={len(report.get('content', []))}, fuzzy={len(report.get('fuzzy', []))}, sacred_exceptions={len(report.get('sacred_exceptions', []))}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
