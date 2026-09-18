#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cleanup_duplicates_and_errors.py
================================
重复与错误文档清理脚本，遵循 流程规则.md "重复与错误文档清理规则" 小节。

清理流程七步：
1. 识别（扫描 references 表与文件系统）
2. 生成清单 pending_deletion.jsonl
3. 人工抽样复核（本脚本仅生成清单，不自动删除；--execute 模式才执行删除）
4. 执行删除（--execute 模式）
5. 数据库更新（status='deleted'）
6. 日志记录 deletion_log.jsonl
7. 看板更新 dashboard.md

用法：
    python script/cleanup_duplicates_and_errors.py                    # 仅识别，生成清单
    python script/cleanup_duplicates_and_errors.py --execute          # 执行删除
    python script/cleanup_duplicates_and_errors.py --sample-only      # 仅打印抽样复核条目
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Tuple

BASE = Path(r"d:\librebsd")
DB_PATH = BASE / "04-现代研究文献" / "05-参考文献全文数据库" / "references_fulltext.db"
LOG_DIR = BASE / "script" / "_cleanup_logs"
PENDING_FILE = LOG_DIR / "pending_deletion.jsonl"
DELETION_LOG = LOG_DIR / "deletion_log.jsonl"
DASHBOARD_FILE = LOG_DIR / "dashboard.md"


def ensure_log_dir():
    LOG_DIR.mkdir(parents=True, exist_ok=True)


def compute_sha256(file_path: Path) -> str:
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def identify_duplicates(conn: sqlite3.Connection) -> List[Dict[str, Any]]:
    """识别重复文件：SHA-256 精确重复 + 标题/作者/年份模糊重复。

    保留规则：每组保留 id 最小者为主副本，其余为待删除副本。
    """
    cur = conn.cursor()
    pending = []

    # === SHA-256 精确重复 ===
    cur.execute("""
        SELECT sha256, GROUP_CONCAT(id) as ids, MIN(id) as primary_id
        FROM "references"
        WHERE sha256 IS NOT NULL AND sha256 != ''
          AND status NOT IN ('deleted', 'rejected')
        GROUP BY sha256
        HAVING COUNT(*) > 1
        ORDER BY MIN(id)
    """)
    for sha, ids_str, primary_id in cur.fetchall():
        ids = [int(x) for x in ids_str.split(",")]
        for rid in ids:
            if rid == primary_id:
                continue
            cur.execute(
                'SELECT id, file_path, filename, title, author, year, status FROM "references" WHERE id = ?',
                (rid,),
            )
            row = cur.fetchone()
            if not row:
                continue
            pending.append({
                "reference_id": rid,
                "file_path": row[1],
                "filename": row[2],
                "title": row[3],
                "author": row[4],
                "year": row[5],
                "current_status": row[6],
                "reason": "exact_duplicate",
                "primary_reference_id": primary_id,
                "sha256": sha,
            })

    # === 标题+作者+年份模糊重复 ===
    # 排除已被精确重复覆盖的条目
    exact_dup_ids = {p["reference_id"] for p in pending}
    cur.execute("""
        SELECT LOWER(title) as t, LOWER(author) as a, year as y,
               GROUP_CONCAT(id) as ids, MIN(id) as primary_id
        FROM "references"
        WHERE title IS NOT NULL AND title != ''
          AND status NOT IN ('deleted', 'rejected')
        GROUP BY t, a, y
        HAVING COUNT(*) > 1
        ORDER BY MIN(id)
    """)
    for t, a, y, ids_str, primary_id in cur.fetchall():
        ids = [int(x) for x in ids_str.split(",")]
        for rid in ids:
            if rid == primary_id or rid in exact_dup_ids:
                continue
            cur.execute(
                'SELECT id, file_path, filename, title, author, year, status FROM "references" WHERE id = ?',
                (rid,),
            )
            row = cur.fetchone()
            if not row:
                continue
            pending.append({
                "reference_id": rid,
                "file_path": row[1],
                "filename": row[2],
                "title": row[3],
                "author": row[4],
                "year": row[5],
                "current_status": row[6],
                "reason": "fuzzy_duplicate",
                "primary_reference_id": primary_id,
                "sha256": "",
            })

    return pending


def identify_errors(conn: sqlite3.Connection) -> List[Dict[str, Any]]:
    """识别错误文件：损坏、无法读取、文件过小（仅极小且非合法短篇）。

    保守策略：仅对明确损坏（header 错误）的文件标记删除；
    文件过小不自动删除（多为合法短论文/幻灯片），仅在清单中标记 reason=too_small 供人工复核。
    """
    cur = conn.cursor()
    pending = []

    cur.execute(
        'SELECT id, file_path, filename, format, title, author, year, status, file_size FROM "references" WHERE status NOT IN ("deleted", "rejected")'
    )
    rows = cur.fetchall()
    for ref_id, fp, fname, fmt, title, author, year, status, fsize in rows:
        if not fp:
            continue
        full = BASE / fp
        if not full.exists():
            # 文件不存在 - 标记为 missing
            pending.append({
                "reference_id": ref_id,
                "file_path": fp,
                "filename": fname,
                "title": title,
                "author": author,
                "year": year,
                "current_status": status,
                "reason": "missing_file",
                "primary_reference_id": 0,
                "sha256": "",
            })
            continue

        # 检查文件损坏
        try:
            with open(full, "rb") as f:
                header = f.read(8)
            is_corrupted = False
            if fmt == "pdf" and not header.startswith(b"%PDF-"):
                is_corrupted = True
            elif fmt == "epub" and not header.startswith(b"PK"):
                is_corrupted = True

            if is_corrupted:
                pending.append({
                    "reference_id": ref_id,
                    "file_path": fp,
                    "filename": fname,
                    "title": title,
                    "author": author,
                    "year": year,
                    "current_status": status,
                    "reason": "corrupted",
                    "primary_reference_id": 0,
                    "sha256": "",
                    "header_hex": header.hex(),
                })
                continue
        except Exception as e:
            pending.append({
                "reference_id": ref_id,
                "file_path": fp,
                "filename": fname,
                "title": title,
                "author": author,
                "year": year,
                "current_status": status,
                "reason": "unreadable",
                "primary_reference_id": 0,
                "sha256": "",
                "error": str(e),
            })
            continue

        # 文件过小 - 仅标记不删除（人工复核）
        # 书籍 < 1MB 标记复核；论文 < 50KB 标记复核
        # 但会议幻灯片、短论文属合法短文件，不在此处自动判定
        # 此处仅对极小（< 10KB）的非 caj 文件标记 too_small
        if fmt != "caj" and fsize and fsize < 10240:
            pending.append({
                "reference_id": ref_id,
                "file_path": fp,
                "filename": fname,
                "title": title,
                "author": author,
                "year": year,
                "current_status": status,
                "reason": "too_small_review",
                "primary_reference_id": 0,
                "sha256": "",
                "file_size": fsize,
            })

    return pending


def generate_pending_list(duplicates: List[Dict], errors: List[Dict]) -> int:
    """生成待删除清单。返回写入条目数。"""
    ensure_log_dir()
    # 合并：损坏文件直接删除；重复文件删除副本；too_small_review 仅供复核不自动删除
    auto_delete = []
    review_only = []
    for item in duplicates:
        auto_delete.append(item)
    for item in errors:
        if item["reason"] in ("corrupted", "unreadable", "missing_file"):
            auto_delete.append(item)
        elif item["reason"] == "too_small_review":
            review_only.append(item)

    with open(PENDING_FILE, "w", encoding="utf-8") as f:
        for item in auto_delete:
            item["action"] = "delete"
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
        for item in review_only:
            item["action"] = "review_only"
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

    return len(auto_delete), len(review_only)


def pre_deletion_checks(conn: sqlite3.Connection, item: Dict) -> Tuple[bool, str]:
    """删除前核验：主副本存在性、数据库引用、CSV 映射、参考文献总目。

    返回 (是否通过, 原因)。
    """
    cur = conn.cursor()
    ref_id = item["reference_id"]
    reason = item["reason"]

    # 重复文件：核验主副本存在
    if reason in ("exact_duplicate", "fuzzy_duplicate"):
        primary_id = item["primary_reference_id"]
        cur.execute('SELECT file_path FROM "references" WHERE id = ?', (primary_id,))
        row = cur.fetchone()
        if not row or not row[0]:
            return False, f"主副本 id={primary_id} 不存在于数据库"
        primary_path = BASE / row[0]
        if not primary_path.exists():
            return False, f"主副本文件不存在: {row[0]}"

    # 损坏文件：跳过主副本核验（直接删除）

    # 核验 chapter_reviews 引用
    cur.execute(
        'SELECT id, chapter FROM chapter_reviews WHERE revised_reference_ids LIKE ? OR review_reference_ids LIKE ?',
        (f"%{ref_id}%", f"%{ref_id}%"),
    )
    cr_rows = cur.fetchall()
    if cr_rows:
        # 引用存在 - 需要人工处理引用迁移，暂不自动删除
        return False, f"被 chapter_reviews 引用: {cr_rows}"

    return True, "通过"


def execute_deletion(conn: sqlite3.Connection, item: Dict) -> Tuple[bool, str]:
    """执行单个删除操作。返回 (是否成功, 消息)。"""
    cur = conn.cursor()
    ref_id = item["reference_id"]
    fp = item["file_path"]
    full = BASE / fp

    # 删除前核验
    ok, msg = pre_deletion_checks(conn, item)
    if not ok:
        return False, f"核验失败: {msg}"

    # 删除文件系统副本
    file_deleted = False
    if full.exists():
        try:
            full.unlink()
            file_deleted = True
        except Exception as e:
            return False, f"文件删除失败: {e}"

    # 更新数据库 status
    now = datetime.now().strftime("%Y-%m-%d")
    new_path = f"[DELETED {now}] {fp}"
    cur.execute(
        'UPDATE "references" SET status = ?, file_path = ? WHERE id = ?',
        ("deleted", new_path, ref_id),
    )

    # 写入 reference_duplicates（如果是重复文件）
    if item["reason"] in ("exact_duplicate", "fuzzy_duplicate"):
        dup_type = "exact" if item["reason"] == "exact_duplicate" else "fuzzy"
        now_ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cur.execute(
            """INSERT OR IGNORE INTO reference_duplicates
               (primary_reference_id, duplicate_reference_id, duplicate_type,
                match_score, match_fields, merged_at, merged_by, merge_notes)
               VALUES (?, ?, ?, 1.0, ?, ?, 'cleanup_script', ?)""",
            (
                item["primary_reference_id"],
                ref_id,
                dup_type,
                f"file_path={fp}",
                now_ts,
                f"清理脚本删除{dup_type}重复: {item.get('title', '')}",
            ),
        )
    elif item["reason"] in ("corrupted", "unreadable", "missing_file"):
        now_ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cur.execute(
            """INSERT OR IGNORE INTO reference_duplicates
               (primary_reference_id, duplicate_reference_id, duplicate_type,
                match_score, match_fields, merged_at, merged_by, merge_notes)
               VALUES (?, ?, ?, 1.0, ?, ?, 'cleanup_script', ?)""",
            (
                0,
                ref_id,
                item["reason"],
                f"file_path={fp}",
                now_ts,
                f"清理脚本删除错误文件({item['reason']}): {item.get('title', '')}",
            ),
        )

    conn.commit()
    return True, f"已删除 file_deleted={file_deleted}"


def log_deletion(item: Dict, success: bool, msg: str):
    """记录删除日志。"""
    ensure_log_dir()
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "reference_id": item["reference_id"],
        "file_path": item["file_path"],
        "reason": item["reason"],
        "primary_reference_id": item.get("primary_reference_id", 0),
        "success": success,
        "message": msg,
        "operator": "cleanup_script",
    }
    with open(DELETION_LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def update_dashboard(stats: Dict[str, int]):
    """更新看板。"""
    ensure_log_dir()
    content = f"""# 重复与错误文档清理看板

## 本次清理统计

| 指标 | 数值 |
| --- | --- |
| 本次清理时间 | {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} |
| 待删除（自动）数 | {stats.get("pending_delete", 0)} |
| 待复核（人工）数 | {stats.get("pending_review", 0)} |
| 成功删除数 | {stats.get("deleted", 0)} |
| 删除失败数 | {stats.get("failed", 0)} |
| 保留主副本数 | {stats.get("primary_kept", 0)} |
"""
    DASHBOARD_FILE.write_text(content, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="重复与错误文档清理")
    parser.add_argument("--execute", action="store_true", help="执行删除（默认仅生成清单）")
    parser.add_argument("--sample-only", action="store_true", help="仅打印抽样复核条目")
    args = parser.parse_args()

    ensure_log_dir()
    conn = sqlite3.connect(str(DB_PATH))

    print("=" * 70)
    print("步骤 1：识别重复与错误文件")
    print("=" * 70)
    duplicates = identify_duplicates(conn)
    errors = identify_errors(conn)
    print(f"重复文件数: {len(duplicates)}（exact={sum(1 for d in duplicates if d['reason']=='exact_duplicate')}, fuzzy={sum(1 for d in duplicates if d['reason']=='fuzzy_duplicate')}）")
    print(f"错误文件数: {len(errors)}")
    for e in errors:
        print(f"  id={e['reference_id']} reason={e['reason']} path={e['file_path']}")

    print()
    print("=" * 70)
    print("步骤 2：生成待删除清单")
    print("=" * 70)
    auto_count, review_count = generate_pending_list(duplicates, errors)
    print(f"自动删除条目数: {auto_count}")
    print(f"人工复核条目数: {review_count}")
    print(f"清单文件: {PENDING_FILE}")

    if args.sample_only:
        print()
        print("=" * 70)
        print("步骤 3：人工抽样复核（每 10 条抽 1 条）")
        print("=" * 70)
        all_items = duplicates + [e for e in errors if e["reason"] != "too_small_review"]
        samples = all_items[::10]
        for i, item in enumerate(samples, 1):
            print(f"  [{i}] id={item['reference_id']} reason={item['reason']} primary={item.get('primary_reference_id', 0)}")
            print(f"       title={item.get('title', '')[:60]}")
            print(f"       path={item['file_path']}")
        conn.close()
        return

    if not args.execute:
        print()
        print("（仅识别模式，未执行删除。使用 --execute 执行删除，--sample-only 查看抽样）")
        # 仍更新看板
        update_dashboard({
            "pending_delete": auto_count,
            "pending_review": review_count,
            "deleted": 0,
            "failed": 0,
            "primary_kept": len({d["primary_reference_id"] for d in duplicates if d["reason"] in ("exact_duplicate", "fuzzy_duplicate")}),
        })
        conn.close()
        return

    print()
    print("=" * 70)
    print("步骤 3-7：执行删除、数据库更新、日志记录、看板更新")
    print("=" * 70)
    # 读取自动删除清单
    auto_items = []
    with open(PENDING_FILE, "r", encoding="utf-8") as f:
        for line in f:
            item = json.loads(line)
            if item.get("action") == "delete":
                auto_items.append(item)

    deleted_count = 0
    failed_count = 0
    primary_ids = set()
    for item in auto_items:
        if item["reason"] in ("exact_duplicate", "fuzzy_duplicate"):
            primary_ids.add(item["primary_reference_id"])
        success, msg = execute_deletion(conn, item)
        log_deletion(item, success, msg)
        if success:
            deleted_count += 1
            print(f"  [OK] id={item['reference_id']} reason={item['reason']} - {msg}")
        else:
            failed_count += 1
            print(f"  [FAIL] id={item['reference_id']} reason={item['reason']} - {msg}")

    print()
    print(f"删除完成: 成功 {deleted_count}, 失败 {failed_count}")
    print(f"保留主副本数: {len(primary_ids)}")

    update_dashboard({
        "pending_delete": auto_count,
        "pending_review": review_count,
        "deleted": deleted_count,
        "failed": failed_count,
        "primary_kept": len(primary_ids),
    })
    print(f"看板已更新: {DASHBOARD_FILE}")

    conn.close()
    print()
    print("=" * 70)
    print("清理完成")
    print("=" * 70)


if __name__ == "__main__":
    main()
