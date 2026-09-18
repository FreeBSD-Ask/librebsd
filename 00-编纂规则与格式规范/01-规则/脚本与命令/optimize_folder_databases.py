#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
optimize_folder_databases.py — 优化 7 个文件夹级 SQLite 数据库

对 7 个文件夹级数据库执行 schema 优化、幽灵块清理、VACUUM 收缩操作。

7 个文件夹级数据库：
  1. 02-sacred源材料/sacred_sources.db（sacred，不可变，跳过 ghost-blocks 清理）
  2. 03-原始史料库/original_sources.db
  3. 04-现代研究文献/research_notes.db
  4. 07-事实核查记录/fact_checks.db
  5. 08-核查报告与多轮复核/review_reports.db
  6. 10-交叉索引/cross_indexes.db
  7. 11-元数据接口/metadata_interfaces.db

7 种运行模式（argparse）：
  --schema        Schema 优化（创建 schema_meta 表 + 创建索引 + 删除空扩展表 + 回填 update_log）
  --ghost-blocks  清理幽灵块（删除 files.status='deleted' 的 blocks/blocks_fts 行，跳过 sacred_sources.db）
  --reindex       清理冗余索引（删除 idx_xref_* 与 idx_files_duplicate_type，补建 idx_files_duplicate_of_db）
  --pragma        应用持久化 PRAGMA 优化（WAL/NORMAL/mmap256M/temp_memory/wal_autocheckpoint_1000）
  --vacuum        VACUUM 全部 7 个数据库以回收空间
  --all           依次执行 --schema → --ghost-blocks → --reindex → --pragma → --vacuum
  --dry-run       预览模式（不执行修改；单独使用时预览 --all）

编码：UTF-8 无 BOM，LF 换行
依赖：仅 Python 3.8+ 标准库（sqlite3, json, pathlib, argparse, datetime）
幂等性：所有 CREATE 使用 IF NOT EXISTS，可重复执行
"""

import argparse
import datetime
import json
import sqlite3
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# =============================================================================
# 常量
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent
LOG_DIR = PROJECT_ROOT / "script" / "_folder_db_logs"

# 7 个文件夹级数据库：(db_name, relative_path, immutable)
DB_LIST: List[Tuple[str, str, bool]] = [
    ("sacred_sources", "02-sacred源材料/sacred_sources.db", True),
    ("original_sources", "03-原始史料库/original_sources.db", False),
    ("research_notes", "04-现代研究文献/research_notes.db", False),
    ("fact_checks", "07-事实核查记录/fact_checks.db", False),
    ("review_reports", "08-核查报告与多轮复核/review_reports.db", False),
    ("cross_indexes", "10-交叉索引/cross_indexes.db", False),
    ("metadata_interfaces", "11-元数据接口/metadata_interfaces.db", False),
]

# 通用表（5 张，所有数据库共用）
COMMON_TABLES = {"files", "blocks", "blocks_fts", "cross_references", "update_log"}

# FTS5 影子表（不计入 table_count）
FTS_SHADOW_TABLES = {
    "blocks_fts_config",
    "blocks_fts_content",
    "blocks_fts_data",
    "blocks_fts_docsize",
    "blocks_fts_idx",
}

# 系统表
SYSTEM_TABLES = {"sqlite_sequence", "schema_meta"}

# 空扩展表检查清单：(db_name, table_name)
# 仅检查这两张表是否为空，为空则删除
EMPTY_EXT_CHECK: List[Tuple[str, str]] = [
    ("fact_checks", "fact_check_records"),
    ("metadata_interfaces", "author_index"),
]

SCHEMA_VERSION_NEW = "1.3"

# 预定义索引：(index_name, table_name, column_name)
PREDEFINED_INDEXES: List[Tuple[str, str, str]] = [
    ("idx_files_status", "files", "status"),
    ("idx_files_sha256", "files", "sha256"),
    ("idx_files_content_hash", "files", "content_hash"),
    ("idx_files_duplicate_of_id", "files", "duplicate_of_id"),
    ("idx_blocks_file_id", "blocks", "file_id"),
    ("idx_cross_references_source_file_id", "cross_references", "source_file_id"),
    ("idx_cross_references_target_path", "cross_references", "target_path"),
    ("idx_cross_references_resolution_status", "cross_references", "resolution_status"),
]


# =============================================================================
# 工具函数
# =============================================================================


def now_iso() -> str:
    """返回当前时间的 ISO 8601 字符串。"""
    return datetime.datetime.now().isoformat(timespec="seconds")


def now_timestamp() -> str:
    """返回用于文件名的时间戳（YYYYMMDD_HHMMSS）。"""
    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")


def get_db_path(db_rel_path: str) -> Path:
    """返回数据库文件的绝对路径。"""
    return PROJECT_ROOT / db_rel_path


def get_all_tables(conn: sqlite3.Connection) -> List[str]:
    """获取数据库所有表名（含虚拟表，不含视图）。"""
    cur = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
    )
    return [row[0] for row in cur.fetchall()]


def table_exists(conn: sqlite3.Connection, table_name: str) -> bool:
    """检查表是否存在。"""
    cur = conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?",
        (table_name,),
    )
    return cur.fetchone() is not None


def get_table_row_count(conn: sqlite3.Connection, table_name: str) -> int:
    """获取表行数，失败返回 -1。"""
    try:
        cur = conn.execute(f'SELECT COUNT(*) FROM "{table_name}"')
        return cur.fetchone()[0]
    except sqlite3.Error:
        return -1


def table_has_column(
    conn: sqlite3.Connection, table_name: str, column_name: str
) -> bool:
    """检查表是否包含指定列。"""
    try:
        cur = conn.execute(f'PRAGMA table_info("{table_name}")')
        for row in cur.fetchall():
            if row[1] == column_name:
                return True
    except sqlite3.Error:
        pass
    return False


def ensure_schema_meta(conn: sqlite3.Connection) -> None:
    """确保 schema_meta 表存在。"""
    conn.execute(
        "CREATE TABLE IF NOT EXISTS schema_meta (key TEXT PRIMARY KEY, value TEXT)"
    )
    conn.commit()


def set_schema_meta(conn: sqlite3.Connection, key: str, value: str) -> None:
    """插入或替换 schema_meta 键值。"""
    conn.execute(
        "INSERT INTO schema_meta (key, value) VALUES (?, ?) "
        "ON CONFLICT(key) DO UPDATE SET value=excluded.value",
        (key, value),
    )
    conn.commit()


# =============================================================================
# 日志函数
# =============================================================================


def write_jsonl_log(log_path: Path, entry: Dict[str, Any]) -> None:
    """追加一条 JSONL 日志。"""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    with open(log_path, "a", encoding="utf-8", newline="") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def append_schema_log(content: str) -> None:
    """追加 schema 升级日志到 schema_upgrade_log.md。"""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_path = LOG_DIR / "schema_upgrade_log.md"
    with open(log_path, "a", encoding="utf-8", newline="") as f:
        f.write(content)
        if not content.endswith("\n"):
            f.write("\n")


def append_error_log(db_name: str, error_type: str, error_message: str) -> None:
    """追加错误到 errors.md。"""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    err_path = LOG_DIR / "errors.md"
    if not err_path.exists():
        err_path.write_text(
            "# 文件夹级数据库优化错误清单\n\n"
            "| 时间 | 数据库 | 错误类型 | 错误信息 |\n"
            "| --- | --- | --- | --- |\n",
            encoding="utf-8",
            newline="",
        )
    with open(err_path, "a", encoding="utf-8", newline="") as f:
        f.write(
            f"| {now_iso()} | {db_name} | {error_type} | "
            f"{error_message.replace('|', '/')[:300]} |\n"
        )


# =============================================================================
# --schema 模式
# =============================================================================


def mode_schema_single(
    db_name: str,
    db_path: Path,
    dry_run: bool,
    log_path: Path,
) -> Dict[str, Any]:
    """对单个数据库执行 schema 优化。

    步骤：
    1. 创建 schema_meta 表
    2. 插入/替换 schema_meta 键值对
    3. 创建预定义索引与扩展表 file_id 索引
    4. 删除空扩展表（fact_check_records / author_index）
    5. 回填 update_log（若为空）
    """
    result: Dict[str, Any] = {
        "db_name": db_name,
        "db_path": str(db_path),
        "mode": "schema",
        "dry_run": dry_run,
        "timestamp": now_iso(),
        "actions": [],
        "errors": [],
    }

    if not db_path.exists():
        msg = f"数据库不存在: {db_path}"
        result["errors"].append(msg)
        append_error_log(db_name, "FileNotFoundError", msg)
        return result

    print(f"  [{db_name}] schema 优化... ", end="", flush=True)

    try:
        conn = sqlite3.connect(str(db_path))
        conn.execute("PRAGMA foreign_keys = ON")

        # --- 步骤 1：创建 schema_meta 表 ---
        ensure_schema_meta(conn)
        result["actions"].append("create schema_meta table (IF NOT EXISTS)")

        # --- 步骤 2：计算并写入 schema_meta 键值对 ---
        all_tables = get_all_tables(conn)
        counted_tables = [
            t for t in all_tables if t not in FTS_SHADOW_TABLES
        ]
        table_count = len(counted_tables)

        active_files = 0
        deleted_files = 0
        if table_exists(conn, "files"):
            cur = conn.execute("SELECT COUNT(*) FROM files WHERE status='active'")
            active_files = cur.fetchone()[0]
            cur = conn.execute("SELECT COUNT(*) FROM files WHERE status='deleted'")
            deleted_files = cur.fetchone()[0]

        meta_pairs = {
            "schema_version": SCHEMA_VERSION_NEW,
            "last_optimize_at": now_iso(),
            "table_count": str(table_count),
            "active_files": str(active_files),
            "deleted_files": str(deleted_files),
            "ghost_blocks_cleaned": "0",
        }

        if not dry_run:
            for key, value in meta_pairs.items():
                set_schema_meta(conn, key, value)

        result["actions"].append(
            f"schema_meta: schema_version={SCHEMA_VERSION_NEW}, "
            f"table_count={table_count}, "
            f"active_files={active_files}, deleted_files={deleted_files}"
        )

        # --- 步骤 3：创建预定义索引 ---
        for idx_name, tbl, col in PREDEFINED_INDEXES:
            if table_exists(conn, tbl):
                if dry_run:
                    result["actions"].append(
                        f"would create index {idx_name} ON {tbl}({col})"
                    )
                else:
                    conn.execute(
                        f'CREATE INDEX IF NOT EXISTS "{idx_name}" '
                        f'ON "{tbl}"("{col}")'
                    )
                    result["actions"].append(
                        f"create index {idx_name} ON {tbl}({col})"
                    )

        # 为扩展表创建 file_id 索引
        ext_tables = [
            t
            for t in all_tables
            if t not in COMMON_TABLES
            and t not in FTS_SHADOW_TABLES
            and t not in SYSTEM_TABLES
        ]
        for tbl in ext_tables:
            if table_has_column(conn, tbl, "file_id"):
                idx_name = f"idx_{tbl}_file_id"
                if dry_run:
                    result["actions"].append(
                        f"would create index {idx_name} ON {tbl}(file_id)"
                    )
                else:
                    conn.execute(
                        f'CREATE INDEX IF NOT EXISTS "{idx_name}" '
                        f'ON "{tbl}"("file_id")'
                    )
                    result["actions"].append(
                        f"create index {idx_name} ON {tbl}(file_id)"
                    )

        # --- 步骤 4：删除空扩展表 ---
        for chk_db, chk_tbl in EMPTY_EXT_CHECK:
            if db_name == chk_db and table_exists(conn, chk_tbl):
                row_count = get_table_row_count(conn, chk_tbl)
                if row_count == 0:
                    if dry_run:
                        result["actions"].append(
                            f"would drop empty table {chk_tbl} (0 rows)"
                        )
                    else:
                        # 先删除关联触发器
                        cur = conn.execute(
                            "SELECT name FROM sqlite_master "
                            "WHERE type='trigger' AND tbl_name=?",
                            (chk_tbl,),
                        )
                        for trig_row in cur.fetchall():
                            conn.execute(
                                f'DROP TRIGGER IF EXISTS "{trig_row[0]}"'
                            )
                        conn.execute(f'DROP TABLE IF EXISTS "{chk_tbl}"')
                        result["actions"].append(
                            f"drop empty table {chk_tbl} (0 rows)"
                        )
                else:
                    result["actions"].append(
                        f"keep table {chk_tbl} ({row_count} rows, non-empty)"
                    )

        # --- 步骤 5：回填 update_log ---
        if table_exists(conn, "update_log"):
            ul_count = get_table_row_count(conn, "update_log")
            if ul_count == 0:
                if dry_run:
                    result["actions"].append(
                        "would backfill update_log: operation=optimize, "
                        "field_changed=schema, old_value=1.2, new_value=1.3"
                    )
                else:
                    conn.execute(
                        """INSERT INTO update_log
                           (file_id, operation, field_changed, old_value,
                            new_value, timestamp, operated_by, notes)
                           VALUES (NULL, 'optimize', 'schema', '1.2', '1.3',
                                   ?, 'optimize_folder_databases.py --schema',
                                   '补全 update_log，记录 schema 1.3 升级')""",
                        (now_iso(),),
                    )
                    result["actions"].append(
                        "backfill update_log (was 0 rows → inserted 1 row)"
                    )
            else:
                result["actions"].append(
                    f"update_log already has {ul_count} rows, skip backfill"
                )

        if not dry_run:
            conn.commit()
            append_schema_log(
                f"## {db_name} ({now_iso()})\n\n"
                f"- schema_version: 1.2 → {SCHEMA_VERSION_NEW}\n"
                f"- table_count: {table_count}\n"
                f"- active_files: {active_files}\n"
                f"- deleted_files: {deleted_files}\n"
                f"- actions: {len(result['actions'])} items\n"
            )

        conn.close()
        print("完成")
        result["status"] = "ok"

    except Exception as e:
        err_type = type(e).__name__
        err_msg = str(e).replace("\n", " ")[:300]
        result["errors"].append(f"{err_type}: {err_msg}")
        append_error_log(db_name, err_type, err_msg)
        print(f"错误: {err_msg}")
        result["status"] = "error"

    write_jsonl_log(log_path, result)
    return result


# =============================================================================
# --ghost-blocks 模式
# =============================================================================


def mode_ghost_blocks_single(
    db_name: str,
    db_path: Path,
    immutable: bool,
    dry_run: bool,
    log_path: Path,
) -> Dict[str, Any]:
    """对单个数据库执行幽灵块清理。

    对于非 sacred 数据库：
    1. 查询 files.status='deleted' 的 file_id 列表
    2. 删除 blocks_fts 中对应的行
    3. 删除 blocks 中对应的行
    4. 更新 schema_meta.ghost_blocks_cleaned
    5. 写入 update_log

    对于 sacred_sources.db（immutable）：
    仅在 update_log 中记录跳过原因。
    """
    result: Dict[str, Any] = {
        "db_name": db_name,
        "db_path": str(db_path),
        "mode": "ghost-blocks",
        "dry_run": dry_run,
        "immutable": immutable,
        "timestamp": now_iso(),
        "actions": [],
        "errors": [],
        "ghost_blocks_cleaned": 0,
    }

    if not db_path.exists():
        msg = f"数据库不存在: {db_path}"
        result["errors"].append(msg)
        append_error_log(db_name, "FileNotFoundError", msg)
        return result

    print(f"  [{db_name}] ghost-blocks 清理... ", end="", flush=True)

    try:
        conn = sqlite3.connect(str(db_path))
        conn.execute("PRAGMA foreign_keys = ON")
        ensure_schema_meta(conn)

        if immutable:
            # sacred_sources.db：跳过清理，仅记录日志
            if not dry_run:
                conn.execute(
                    """INSERT INTO update_log
                       (file_id, operation, field_changed, old_value,
                        new_value, timestamp, operated_by, notes)
                       VALUES (NULL, 'optimize', 'blocks', NULL, NULL, ?,
                               'optimize_folder_databases.py --ghost-blocks',
                               'sacred immutable, skipped ghost blocks cleanup')""",
                    (now_iso(),),
                )
                conn.commit()
            result["actions"].append(
                "sacred immutable, skipped ghost blocks cleanup"
            )
            print("跳过（sacred immutable）")
        else:
            # 查询 deleted 文件的 file_id 列表
            if not table_exists(conn, "files"):
                result["actions"].append("files table not found, skip")
                print("跳过（无 files 表）")
            else:
                cur = conn.execute(
                    "SELECT id FROM files WHERE status='deleted'"
                )
                deleted_file_ids = [row[0] for row in cur.fetchall()]

                if not deleted_file_ids:
                    result["actions"].append(
                        "no deleted files, nothing to clean"
                    )
                    print("无 deleted 文件")
                else:
                    # 统计待删除的 blocks 数量
                    placeholders = ",".join("?" * len(deleted_file_ids))
                    cur = conn.execute(
                        f"SELECT COUNT(*) FROM blocks "
                        f"WHERE file_id IN ({placeholders})",
                        deleted_file_ids,
                    )
                    total_ghost_blocks = cur.fetchone()[0]
                    result["ghost_blocks_cleaned"] = total_ghost_blocks

                    if dry_run:
                        result["actions"].append(
                            f"would delete {total_ghost_blocks} ghost blocks "
                            f"from {len(deleted_file_ids)} deleted files"
                        )
                        print(
                            f"预览：{total_ghost_blocks} 个幽灵块"
                            f"（{len(deleted_file_ids)} 个 deleted 文件）"
                        )
                    else:
                        # 删除 blocks_fts 中的幽灵块
                        # blocks_fts 有 file_id 列（UNINDEXED），可直接按 file_id 删除
                        if table_exists(conn, "blocks_fts"):
                            conn.execute(
                                f"DELETE FROM blocks_fts "
                                f"WHERE file_id IN ({placeholders})",
                                deleted_file_ids,
                            )

                        # 删除 blocks 中的幽灵块
                        # 触发器 trigger_blocks_fts_ad 会尝试清理 blocks_fts，
                        # 但对应行已删除，无副作用
                        if table_exists(conn, "blocks"):
                            conn.execute(
                                f"DELETE FROM blocks "
                                f"WHERE file_id IN ({placeholders})",
                                deleted_file_ids,
                            )

                        # 更新 schema_meta
                        set_schema_meta(
                            conn,
                            "ghost_blocks_cleaned",
                            str(total_ghost_blocks),
                        )

                        # 写 update_log
                        conn.execute(
                            """INSERT INTO update_log
                               (file_id, operation, field_changed, old_value,
                                new_value, timestamp, operated_by, notes)
                               VALUES (NULL, 'optimize', 'blocks', ?, '0', ?,
                                       'optimize_folder_databases.py --ghost-blocks',
                                       '清理 deleted 文件的幽灵块')""",
                            (str(total_ghost_blocks), now_iso()),
                        )
                        conn.commit()

                        result["actions"].append(
                            f"deleted {total_ghost_blocks} ghost blocks "
                            f"from {len(deleted_file_ids)} deleted files"
                        )
                        print(f"清理 {total_ghost_blocks} 个幽灵块")

        conn.close()
        result["status"] = "ok"

    except Exception as e:
        err_type = type(e).__name__
        err_msg = str(e).replace("\n", " ")[:300]
        result["errors"].append(f"{err_type}: {err_msg}")
        append_error_log(db_name, err_type, err_msg)
        print(f"错误: {err_msg}")
        result["status"] = "error"

    write_jsonl_log(log_path, result)
    return result


# =============================================================================
# --pragma 模式
# =============================================================================


# 持久化 PRAGMA 优化清单（仅含数据库级持久化项，不含 per-connection 的 cache_size）
# (pragma 名称, 期望值, 写入用 SQL, update_log new_value 标记)
PRAGMA_OPTIMIZATIONS: List[Tuple[str, str, str]] = [
    ("journal_mode", "wal", "PRAGMA journal_mode = WAL"),
    ("synchronous", "NORMAL", "PRAGMA synchronous = NORMAL"),
    ("mmap_size", "268435456", "PRAGMA mmap_size = 268435456"),
    ("temp_store", "MEMORY", "PRAGMA temp_store = MEMORY"),
    ("wal_autocheckpoint", "1000", "PRAGMA wal_autocheckpoint = 1000"),
]

# update_log 记录的 new_value 标记
PRAGMA_NEW_VALUE_TAG = (
    "WAL,NORMAL,mmap256M,temp_memory,wal_autocheckpoint_1000"
)


def mode_pragma_single(
    db_name: str,
    db_path: Path,
    dry_run: bool,
    log_path: Path,
) -> Dict[str, Any]:
    """对单个数据库应用持久化 PRAGMA 优化。

    应用以下持久化 PRAGMA（数据库级，跨连接生效）：
    1. journal_mode = WAL — Write-Ahead Logging，提升并发读写性能
    2. synchronous = NORMAL — WAL 模式下的推荐同步级别
    3. mmap_size = 268435456 — 内存映射 I/O 256MB，加速大数据库读取
    4. temp_store = MEMORY — 临时表存内存
    5. wal_autocheckpoint = 1000 — WAL 自动检查点设为 1000 页

    注意：
    - 不设置 cache_size（per-connection，非持久化，应由应用程序在查询时设置）
    - 在 schema_meta 表中记录 pragma_optimized_at 与 journal_mode
    - 在 update_log 记录 operation='optimize'、field_changed='pragma'
    """
    result: Dict[str, Any] = {
        "db_name": db_name,
        "db_path": str(db_path),
        "mode": "pragma",
        "dry_run": dry_run,
        "timestamp": now_iso(),
        "actions": [],
        "errors": [],
        "pragmas": {},
    }

    if not db_path.exists():
        msg = f"数据库不存在: {db_path}"
        result["errors"].append(msg)
        append_error_log(db_name, "FileNotFoundError", msg)
        return result

    print(f"  [{db_name}] PRAGMA 优化... ", end="", flush=True)

    try:
        conn = sqlite3.connect(str(db_path))
        conn.execute("PRAGMA foreign_keys = ON")
        ensure_schema_meta(conn)

        # 收集每个 PRAGMA 的当前值（预览信息）
        current_values: Dict[str, str] = {}
        for name, _expected, _sql in PRAGMA_OPTIMIZATIONS:
            try:
                cur = conn.execute(f"PRAGMA {name}")
                row = cur.fetchone()
                current_values[name] = str(row[0]) if row else "NULL"
            except sqlite3.Error as e:
                current_values[name] = f"ERR:{e}"
        result["pragmas"]["before"] = current_values

        if dry_run:
            # 预览：列出当前值与目标值
            for name, expected, _sql in PRAGMA_OPTIMIZATIONS:
                result["actions"].append(
                    f"would set PRAGMA {name} = {expected} "
                    f"(current: {current_values.get(name, 'unknown')})"
                )
            print(
                f"预览（{len(PRAGMA_OPTIMIZATIONS)} 个 PRAGMA，"
                f"journal_mode={current_values.get('journal_mode', '?')}）"
            )
        else:
            # 应用持久化 PRAGMA
            # 注意：journal_mode 切换为 WAL 时 SQLite 会自动 commit 事务
            applied: List[Tuple[str, str, str]] = []  # (name, before, after)
            for name, expected, sql in PRAGMA_OPTIMIZATIONS:
                before_val = current_values.get(name, "unknown")
                try:
                    cur = conn.execute(sql)
                    # journal_mode 切换会返回新模式名（如 “wal”）
                    if name == "journal_mode":
                        row = cur.fetchone()
                        after_val = str(row[0]).lower() if row else expected
                    else:
                        # 重新读取以确认
                        cur2 = conn.execute(f"PRAGMA {name}")
                        row2 = cur2.fetchone()
                        after_val = (
                            str(row2[0]) if row2 else expected
                        )
                    applied.append((name, before_val, after_val))
                    result["actions"].append(
                        f"PRAGMA {name}: {before_val} → {after_val}"
                    )
                except sqlite3.Error as e:
                    err_msg = f"PRAGMA {name} 失败: {e}"
                    result["errors"].append(err_msg)
                    append_error_log(db_name, "PragmaError", err_msg)
                    result["actions"].append(
                        f"PRAGMA {name} FAILED: {e}"
                    )

            # 在 schema_meta 记录 pragma 优化元数据
            set_schema_meta(conn, "pragma_optimized_at", now_iso())
            # journal_mode 已持久化为 wal
            set_schema_meta(conn, "journal_mode", "wal")

            # 在 update_log 记录 PRAGMA 优化
            if table_exists(conn, "update_log"):
                conn.execute(
                    """INSERT INTO update_log
                       (file_id, operation, field_changed, old_value,
                        new_value, timestamp, operated_by, notes)
                       VALUES (NULL, 'optimize', 'pragma', NULL, ?, ?,
                               'optimize_folder_databases.py --pragma',
                               '应用持久化 PRAGMA 优化（WAL/NORMAL/mmap/temp/wal_autocheckpoint）')""",
                    (PRAGMA_NEW_VALUE_TAG, now_iso()),
                )

            conn.commit()

            # 收集应用后的值
            after_values: Dict[str, str] = {}
            for name, _expected, _sql in PRAGMA_OPTIMIZATIONS:
                try:
                    cur = conn.execute(f"PRAGMA {name}")
                    row = cur.fetchone()
                    after_values[name] = (
                        str(row[0]) if row else "NULL"
                    )
                except sqlite3.Error:
                    after_values[name] = "ERR"
            result["pragmas"]["after"] = after_values

            print(
                f"完成（journal_mode: "
                f"{current_values.get('journal_mode', '?')} → "
                f"{after_values.get('journal_mode', '?')}）"
            )

            # 写 schema 升级日志（与现有风格保持一致）
            append_schema_log(
                f"## {db_name} --pragma ({now_iso()})\n\n"
                f"- journal_mode: "
                f"{current_values.get('journal_mode', '?')} → "
                f"{after_values.get('journal_mode', '?')}\n"
                f"- synchronous: "
                f"{current_values.get('synchronous', '?')} → "
                f"{after_values.get('synchronous', '?')}\n"
                f"- mmap_size: "
                f"{current_values.get('mmap_size', '?')} → "
                f"{after_values.get('mmap_size', '?')}\n"
                f"- temp_store: "
                f"{current_values.get('temp_store', '?')} → "
                f"{after_values.get('temp_store', '?')}\n"
                f"- wal_autocheckpoint: "
                f"{current_values.get('wal_autocheckpoint', '?')} → "
                f"{after_values.get('wal_autocheckpoint', '?')}\n"
            )

        conn.close()
        result["status"] = "ok"

    except Exception as e:
        err_type = type(e).__name__
        err_msg = str(e).replace("\n", " ")[:300]
        result["errors"].append(f"{err_type}: {err_msg}")
        append_error_log(db_name, err_type, err_msg)
        print(f"错误: {err_msg}")
        result["status"] = "error"

    write_jsonl_log(log_path, result)
    return result


# =============================================================================
# --vacuum 模式
# =============================================================================


def mode_vacuum_single(
    db_name: str,
    db_path: Path,
    dry_run: bool,
    log_path: Path,
) -> Dict[str, Any]:
    """对单个数据库执行 VACUUM。

    1. 记录 VACUUM 前大小
    2. 执行 VACUUM
    3. 记录 VACUUM 后大小
    4. 更新 schema_meta.last_vacuum_at
    5. 记录大小差异
    """
    result: Dict[str, Any] = {
        "db_name": db_name,
        "db_path": str(db_path),
        "mode": "vacuum",
        "dry_run": dry_run,
        "timestamp": now_iso(),
        "actions": [],
        "errors": [],
        "size_before": 0,
        "size_after": 0,
        "size_diff": 0,
    }

    if not db_path.exists():
        msg = f"数据库不存在: {db_path}"
        result["errors"].append(msg)
        append_error_log(db_name, "FileNotFoundError", msg)
        return result

    print(f"  [{db_name}] VACUUM... ", end="", flush=True)

    try:
        size_before = db_path.stat().st_size
        result["size_before"] = size_before

        if dry_run:
            result["actions"].append(
                f"would VACUUM (current size: {size_before:,} bytes)"
            )
            print(f"预览（当前 {size_before:,} 字节）")
        else:
            conn = sqlite3.connect(str(db_path))
            conn.execute("VACUUM")
            ensure_schema_meta(conn)
            set_schema_meta(conn, "last_vacuum_at", now_iso())
            conn.commit()
            conn.close()

            size_after = db_path.stat().st_size
            result["size_after"] = size_after
            result["size_diff"] = size_before - size_after

            result["actions"].append(
                f"VACUUM: {size_before:,} → {size_after:,} bytes "
                f"(saved {size_before - size_after:,} bytes)"
            )
            print(
                f"{size_before:,} → {size_after:,} 字节"
                f"（节省 {size_before - size_after:,}）"
            )

        result["status"] = "ok"

    except Exception as e:
        err_type = type(e).__name__
        err_msg = str(e).replace("\n", " ")[:300]
        result["errors"].append(f"{err_type}: {err_msg}")
        append_error_log(db_name, err_type, err_msg)
        print(f"错误: {err_msg}")
        result["status"] = "error"

    write_jsonl_log(log_path, result)
    return result


# =============================================================================
# --reindex 模式
# =============================================================================


# 冗余索引清单（待删除）：idx_xref_* 旧命名 + idx_files_duplicate_type
REDUNDANT_INDEXES: List[Tuple[str, str]] = [
    ("idx_xref_source", "cross_references"),
    ("idx_xref_target_db", "cross_references"),
    ("idx_xref_resolution_status", "cross_references"),
    ("idx_files_duplicate_type", "files"),
]

# 需补建的索引：(index_name, table_name, column_name)
MISSING_INDEXES_TO_ENSURE: List[Tuple[str, str, str]] = [
    ("idx_files_duplicate_of_db", "files", "duplicate_of_db"),
]


def _index_exists(conn: sqlite3.Connection, index_name: str) -> bool:
    """检查索引是否存在。"""
    cur = conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='index' AND name=?",
        (index_name,),
    )
    return cur.fetchone() is not None


def mode_reindex_single(
    db_name: str,
    db_path: Path,
    dry_run: bool,
    log_path: Path,
) -> Dict[str, Any]:
    """对单个数据库执行冗余索引清理与缺失索引补建。

    步骤：
    1. 删除 idx_xref_source、idx_xref_target_db、idx_xref_resolution_status 旧索引
    2. 删除 idx_files_duplicate_type 旧索引
    3. 补建 idx_files_duplicate_of_db 索引（若缺失）
    4. 在 update_log 记录操作
    5. 在 schema_meta 更新 last_optimize_at 时间戳
    """
    result: Dict[str, Any] = {
        "db_name": db_name,
        "db_path": str(db_path),
        "mode": "reindex",
        "dry_run": dry_run,
        "timestamp": now_iso(),
        "actions": [],
        "errors": [],
        "dropped_indexes": [],
        "created_indexes": [],
    }

    if not db_path.exists():
        msg = f"数据库不存在: {db_path}"
        result["errors"].append(msg)
        append_error_log(db_name, "FileNotFoundError", msg)
        return result

    print(f"  [{db_name}] reindex 清理... ", end="", flush=True)

    try:
        conn = sqlite3.connect(str(db_path))
        conn.execute("PRAGMA foreign_keys = ON")
        ensure_schema_meta(conn)

        # --- 步骤 1 & 2：删除冗余索引 ---
        for idx_name, tbl in REDUNDANT_INDEXES:
            if _index_exists(conn, idx_name):
                if dry_run:
                    result["actions"].append(
                        f"would drop index {idx_name} ON {tbl}"
                    )
                    result["dropped_indexes"].append(idx_name)
                else:
                    conn.execute(f'DROP INDEX IF EXISTS "{idx_name}"')
                    result["actions"].append(
                        f"drop index {idx_name} ON {tbl}"
                    )
                    result["dropped_indexes"].append(idx_name)
            else:
                result["actions"].append(
                    f"index {idx_name} not found, skip"
                )

        # --- 步骤 3：补建缺失索引 ---
        for idx_name, tbl, col in MISSING_INDEXES_TO_ENSURE:
            if table_exists(conn, tbl) and not _index_exists(conn, idx_name):
                if dry_run:
                    result["actions"].append(
                        f"would create index {idx_name} ON {tbl}({col})"
                    )
                    result["created_indexes"].append(idx_name)
                else:
                    conn.execute(
                        f'CREATE INDEX IF NOT EXISTS "{idx_name}" '
                        f'ON "{tbl}"("{col}")'
                    )
                    result["actions"].append(
                        f"create index {idx_name} ON {tbl}({col})"
                    )
                    result["created_indexes"].append(idx_name)
            elif _index_exists(conn, idx_name):
                result["actions"].append(
                    f"index {idx_name} already exists, skip"
                )

        # --- 步骤 4 & 5：记录日志与更新 schema_meta ---
        if not dry_run:
            set_schema_meta(conn, "last_optimize_at", now_iso())
            if table_exists(conn, "update_log"):
                dropped_str = (
                    ", ".join(result["dropped_indexes"])
                    if result["dropped_indexes"]
                    else "none"
                )
                created_str = (
                    ", ".join(result["created_indexes"])
                    if result["created_indexes"]
                    else "none"
                )
                conn.execute(
                    """INSERT INTO update_log
                       (file_id, operation, field_changed, old_value,
                        new_value, timestamp, operated_by, notes)
                       VALUES (NULL, 'optimize', 'indexes', ?, ?, ?,
                               'optimize_folder_databases.py --reindex',
                               '清理冗余索引并补建缺失索引')""",
                    (
                        dropped_str,
                        created_str,
                        now_iso(),
                    ),
                )
            conn.commit()
            append_schema_log(
                f"## {db_name} --reindex ({now_iso()})\n\n"
                f"- dropped_indexes: {result['dropped_indexes']}\n"
                f"- created_indexes: {result['created_indexes']}\n"
            )

        conn.close()
        dropped_count = len(result["dropped_indexes"])
        created_count = len(result["created_indexes"])
        if dry_run:
            print(
                f"预览（删除 {dropped_count} 个，"
                f"补建 {created_count} 个）"
            )
        else:
            print(
                f"完成（删除 {dropped_count} 个，"
                f"补建 {created_count} 个）"
            )
        result["status"] = "ok"

    except Exception as e:
        err_type = type(e).__name__
        err_msg = str(e).replace("\n", " ")[:300]
        result["errors"].append(f"{err_type}: {err_msg}")
        append_error_log(db_name, err_type, err_msg)
        print(f"错误: {err_msg}")
        result["status"] = "error"

    write_jsonl_log(log_path, result)
    return result


# =============================================================================
# 主入口
# =============================================================================


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "优化 7 个文件夹级 SQLite 数据库"
            "（schema / ghost-blocks / reindex / pragma / vacuum）"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "示例:\n"
            "  python script/optimize_folder_databases.py --schema\n"
            "  python script/optimize_folder_databases.py --ghost-blocks\n"
            "  python script/optimize_folder_databases.py --reindex\n"
            "  python script/optimize_folder_databases.py --pragma\n"
            "  python script/optimize_folder_databases.py --vacuum\n"
            "  python script/optimize_folder_databases.py --all\n"
            "  python script/optimize_folder_databases.py --all --dry-run\n"
            "  python script/optimize_folder_databases.py --dry-run\n"
        ),
    )
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument(
        "--schema",
        action="store_true",
        help="Schema 优化（创建 schema_meta + 索引 + 删空表 + 回填 update_log）",
    )
    group.add_argument(
        "--ghost-blocks",
        action="store_true",
        help="清理幽灵块（deleted 文件的 blocks/blocks_fts，跳过 sacred）",
    )
    group.add_argument(
        "--reindex",
        action="store_true",
        help="清理冗余索引（删除 idx_xref_* 与 idx_files_duplicate_type，补建 idx_files_duplicate_of_db）",
    )
    group.add_argument(
        "--pragma",
        action="store_true",
        help="应用持久化 PRAGMA 优化（WAL/NORMAL/mmap256M/temp_memory/wal_autocheckpoint_1000）",
    )
    group.add_argument(
        "--vacuum",
        action="store_true",
        help="VACUUM 全部 7 个数据库以回收空间",
    )
    group.add_argument(
        "--all",
        action="store_true",
        help="依次执行 --schema → --ghost-blocks → --reindex → --pragma → --vacuum",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="预览模式（不执行修改；单独使用时预览 --all）",
    )

    args = parser.parse_args()

    # 确定执行模式
    has_action = any(
        [
            args.schema,
            args.ghost_blocks,
            args.reindex,
            args.pragma,
            args.vacuum,
            args.all,
        ]
    )
    if not has_action and not args.dry_run:
        parser.print_help()
        return 1

    # --dry-run 单独使用时默认预览 --all
    if not has_action and args.dry_run:
        run_schema = True
        run_ghost = True
        run_reindex = True
        run_pragma = True
        run_vacuum = True
    elif args.all:
        run_schema = True
        run_ghost = True
        run_reindex = True
        run_pragma = True
        run_vacuum = True
    elif args.schema:
        run_schema = True
        run_ghost = False
        run_reindex = False
        run_pragma = False
        run_vacuum = False
    elif args.ghost_blocks:
        run_schema = False
        run_ghost = True
        run_reindex = False
        run_pragma = False
        run_vacuum = False
    elif args.reindex:
        run_schema = False
        run_ghost = False
        run_reindex = True
        run_pragma = False
        run_vacuum = False
    elif args.pragma:
        run_schema = False
        run_ghost = False
        run_reindex = False
        run_pragma = True
        run_vacuum = False
    elif args.vacuum:
        run_schema = False
        run_ghost = False
        run_reindex = False
        run_pragma = False
        run_vacuum = True
    else:
        run_schema = False
        run_ghost = False
        run_reindex = False
        run_pragma = False
        run_vacuum = False

    LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_path = LOG_DIR / f"optimize_log_{now_timestamp()}.jsonl"

    if args.dry_run:
        print("=== 预览模式（--dry-run，不执行修改）===")
    print(f"日志文件: {log_path}")
    print()

    total = len(DB_LIST)

    if run_schema:
        print(f"--- --schema 模式（{total} 个数据库）---")
        for idx, (db_name, db_rel, _immutable) in enumerate(DB_LIST, 1):
            db_path = get_db_path(db_rel)
            print(f"[{idx}/{total}]", end="")
            mode_schema_single(db_name, db_path, args.dry_run, log_path)
        print()

    if run_ghost:
        print(f"--- --ghost-blocks 模式（{total} 个数据库）---")
        for idx, (db_name, db_rel, immutable) in enumerate(DB_LIST, 1):
            db_path = get_db_path(db_rel)
            print(f"[{idx}/{total}]", end="")
            mode_ghost_blocks_single(
                db_name, db_path, immutable, args.dry_run, log_path
            )
        print()

    if run_reindex:
        print(f"--- --reindex 模式（{total} 个数据库）---")
        for idx, (db_name, db_rel, _immutable) in enumerate(DB_LIST, 1):
            db_path = get_db_path(db_rel)
            print(f"[{idx}/{total}]", end="")
            mode_reindex_single(db_name, db_path, args.dry_run, log_path)
        print()

    if run_pragma:
        print(f"--- --pragma 模式（{total} 个数据库）---")
        for idx, (db_name, db_rel, _immutable) in enumerate(DB_LIST, 1):
            db_path = get_db_path(db_rel)
            print(f"[{idx}/{total}]", end="")
            mode_pragma_single(db_name, db_path, args.dry_run, log_path)
        print()

    if run_vacuum:
        print(f"--- --vacuum 模式（{total} 个数据库）---")
        for idx, (db_name, db_rel, _immutable) in enumerate(DB_LIST, 1):
            db_path = get_db_path(db_rel)
            print(f"[{idx}/{total}]", end="")
            mode_vacuum_single(db_name, db_path, args.dry_run, log_path)
        print()

    print("完成。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
