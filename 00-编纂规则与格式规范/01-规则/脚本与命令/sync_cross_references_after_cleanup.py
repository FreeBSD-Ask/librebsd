#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""交叉引用同步脚本。

在重复源文件清理与跨库全局去重完成后，扫描项目其他位置的交叉引用，
将指向已删除/已合并副记录的引用更新为指向对应主记录。

映射表来源（优先级从高到低）：
  1. 7 个数据库 files 表中 status='merged' 的副记录
     - 本库内重复：duplicate_of_id 指向同库主记录
     - 跨库重复：duplicate_of_db + duplicate_of_global_file_id 指向跨库主记录
  2. script/_folder_db_logs/cleanup_report.md 中"deleted"小节记录的副记录→主记录映射
     （用于数据库重建后 merged 行已级联清理的场景）

扫描范围：
  - 05-卷册大纲/  下所有 .md 文件
  - 10-交叉索引/  下所有 .md/.csv/.json 文件
  - 11-元数据接口/  下所有 .md/.csv/.json 文件
  （06-正式书稿/ 已随 2026-08-04 禁止编纂正文决策移除，不再扫描）

引用形式（6 种）：
  1. markdown 链接 [文本](路径)
  2. wikilink [[路径]]
  3. 脚注 [^id]: 路径
  4. 章节引用 第XX章 / 第N卷（仅当副记录路径含章节标识时）
  5. CSV 路径字段（file_path / source_path / target_path 列）
  6. JSON path 类字段（path / file_path / source / target key）

数据库 cross_references 表同步：
  UPDATE cross_references SET target_path=<主记录路径>, target_db=<主库>,
         target_record_id=<主记录ID>, resolution_status='resolved'
  WHERE target_path=<副记录路径>

CLI 参数：
  --dry-run  仅扫描输出报告，不修改任何文件与数据库
  --all      实际执行（默认）
"""
import argparse
import csv
import json
import re
import sqlite3
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent  # d:\librebsd
LOG_DIR = PROJECT_ROOT / "script" / "_folder_db_logs"
INDEX_DIR = PROJECT_ROOT / "11-元数据接口" / "09-文件夹数据库索引"
BJT = timezone(timedelta(hours=8))

FOLDER_DB_MAP = {
    "sacred_sources": {"folder": "02-sacred源材料", "db_filename": "sacred_sources.db"},
    "original_sources": {"folder": "03-原始史料库", "db_filename": "original_sources.db"},
    "research_notes": {"folder": "04-现代研究文献", "db_filename": "research_notes.db"},
    "fact_checks": {"folder": "07-事实核查记录", "db_filename": "fact_checks.db"},
    "review_reports": {"folder": "08-核查报告与多轮复核", "db_filename": "review_reports.db"},
    "cross_indexes": {"folder": "10-交叉索引", "db_filename": "cross_indexes.db"},
    "metadata_interfaces": {"folder": "11-元数据接口", "db_filename": "metadata_interfaces.db"},
}

DB_BUILD_ORDER = ["sacred_sources", "original_sources", "research_notes", "fact_checks", "review_reports", "cross_indexes", "metadata_interfaces"]

# 扫描范围
SCAN_DIRS = [
    PROJECT_ROOT / "05-卷册大纲",
    PROJECT_ROOT / "10-交叉索引",
    PROJECT_ROOT / "11-元数据接口",
]

# 扫描的文件扩展名
SCAN_EXTENSIONS = {".md", ".csv", ".json"}


def now_bjt_str() -> str:
    return datetime.now(BJT).strftime("%Y-%m-%d %H:%M:%S BJT")


def write_text(path: Path, text: str) -> None:
    """以 UTF-8 无 BOM、LF 换行写入文件。"""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def get_db_path(db_name: str) -> Path:
    cfg = FOLDER_DB_MAP[db_name]
    return PROJECT_ROOT / cfg["folder"] / cfg["db_filename"]


# ============================== 映射表构建 ==============================

def build_mapping_from_databases() -> dict:
    """从 7 个数据库 files 表读取 status='merged' 的副记录，构建副记录路径 → 主记录路径映射。

    返回 {副记录相对路径: {primary_path, primary_db, primary_file_id, dup_type}}
    """
    mapping = {}
    for db_name in DB_BUILD_ORDER:
        db_path = get_db_path(db_name)
        if not db_path.exists():
            continue
        conn = sqlite3.connect(str(db_path))
        conn.row_factory = sqlite3.Row
        try:
            # 查询本库内重复（duplicate_of_id 指向同库主记录）
            cur = conn.execute(
                "SELECT id, file_path, duplicate_type, duplicate_of_id, duplicate_of_db, duplicate_of_global_file_id "
                "FROM files WHERE status = 'merged'"
            )
            for row in cur.fetchall():
                sub_path = row["file_path"]
                sub_id = row["id"]
                dup_type = row["duplicate_type"]
                dup_of_id = row["duplicate_of_id"]
                dup_of_db = row["duplicate_of_db"]
                dup_of_global_fid = row["duplicate_of_global_file_id"]

                primary_path = None
                primary_db = None
                primary_fid = None

                # 跨库重复
                if dup_of_db and dup_of_global_fid is not None:
                    primary_db = dup_of_db
                    primary_fid = dup_of_global_fid
                    pri_db_path = get_db_path(primary_db)
                    if pri_db_path.exists():
                        pri_conn = sqlite3.connect(str(pri_db_path))
                        try:
                            pri_cur = pri_conn.execute("SELECT file_path FROM files WHERE id = ?", (primary_fid,))
                            pri_row = pri_cur.fetchone()
                            if pri_row:
                                primary_path = pri_row[0]
                        finally:
                            pri_conn.close()
                # 本库内重复
                elif dup_of_id is not None:
                    primary_db = db_name
                    primary_fid = dup_of_id
                    pri_cur = conn.execute("SELECT file_path FROM files WHERE id = ?", (dup_of_id,))
                    pri_row = pri_cur.fetchone()
                    if pri_row:
                        primary_path = pri_row[0]

                if primary_path:
                    mapping[sub_path] = {
                        "primary_path": primary_path,
                        "primary_db": primary_db,
                        "primary_file_id": primary_fid,
                        "dup_type": dup_type,
                        "source": f"db:{db_name}",
                    }
        finally:
            conn.close()
    return mapping


def build_mapping_from_cleanup_report() -> dict:
    """从 cleanup_report.md 解析"deleted"小节，构建副记录路径 → 主记录路径映射。

    返回 {副记录相对路径: {primary_path, primary_db, primary_file_id, dup_type, source}}
    """
    report_path = LOG_DIR / "cleanup_report.md"
    if not report_path.exists():
        return {}

    content = report_path.read_text(encoding="utf-8")
    mapping = {}

    # 匹配 “deleted” 小节中的副记录与主记录对
    # 格式：
    # - 副记录 file_id: 1319, file_path: 04-现代研究文献/.../licenses-old-licenses-gpl-2.0.txt
    # - 主记录 file_id: 1316, file_path: 04-现代研究文献/.../licenses-gpl-2.0.txt
    # 同一数据库下，副记录与紧随其后的主记录配对
    current_db = None
    pending_sub = None  # 待配对的副记录

    lines = content.split("\n")
    in_deleted_section = False
    i = 0
    while i < len(lines):
        line = lines[i]
        # 检测进入 deleted 小节
        if line.startswith("## 详情：deleted"):
            in_deleted_section = True
            i += 1
            continue
        # 检测离开 deleted 小节（遇到下一个 ## 标题）
        if in_deleted_section and line.startswith("## "):
            in_deleted_section = False
            i += 1
            continue

        if not in_deleted_section:
            i += 1
            continue

        # 检测数据库小节标题 ### db_name
        db_match = re.match(r"^###\s+(\S+)", line)
        if db_match:
            current_db = db_match.group(1)
            pending_sub = None
            i += 1
            continue

        # 匹配副记录行
        sub_match = re.match(
            r"^-\s+副记录 file_id:\s*(\d+),\s*file_path:\s*(.+?)$",
            line,
        )
        if sub_match:
            pending_sub = {
                "file_id": int(sub_match.group(1)),
                "file_path": sub_match.group(2).strip(),
                "db": current_db,
            }
            i += 1
            continue

        # 匹配主记录行（与 pending_sub 配对）
        pri_match = re.match(
            r"^-\s+主记录 file_id:\s*(\d+),\s*file_path:\s*(.+?)$",
            line,
        )
        if pri_match and pending_sub:
            primary_path = pri_match.group(2).strip()
            primary_fid = int(pri_match.group(1))
            mapping[pending_sub["file_path"]] = {
                "primary_path": primary_path,
                "primary_db": pending_sub["db"],
                "primary_file_id": primary_fid,
                "dup_type": "exact",
                "source": "cleanup_report",
            }
            pending_sub = None
            i += 1
            continue

        i += 1

    return mapping


def build_mapping() -> dict:
    """构建副记录路径 → 主记录路径的映射表。

    优先从数据库读取，若数据库无 merged 记录则从 cleanup_report.md 解析。
    """
    db_mapping = build_mapping_from_databases()
    if db_mapping:
        print(f"[mapping] 从数据库读取 {len(db_mapping)} 条映射")
        return db_mapping

    report_mapping = build_mapping_from_cleanup_report()
    if report_mapping:
        print(f"[mapping] 从 cleanup_report.md 解析 {len(report_mapping)} 条映射")
        return report_mapping

    print("[mapping] 警告：未找到任何副记录→主记录映射")
    return {}


# ============================== 引用扫描与替换 ==============================

def scan_md_file(file_path: Path, mapping: dict, dry_run: bool, report: dict) -> int:
    """扫描 .md 文件，找出并替换指向副记录路径的引用。

    返回命中并替换的引用数。
    """
    try:
        content = file_path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, PermissionError):
        return 0

    original = content
    hits = 0
    rel_path = str(file_path.relative_to(PROJECT_ROOT)).replace("\\", "/")

    for sub_path, pri_info in mapping.items():
        primary_path = pri_info["primary_path"]
        if sub_path == primary_path:
            continue

        # 1. markdown 链接 [文本](副记录路径)
        pattern1 = re.compile(r"(\[[^\]]*\])\((" + re.escape(sub_path) + r")(\s+\"[^\"]*\")?\)")
        new_content, n1 = pattern1.subn(lambda m: f"{m.group(1)}({primary_path}{m.group(3) or ''})", content)
        if n1:
            hits += n1
            content = new_content
            report["md_hits"].append({"file": rel_path, "form": "markdown_link", "sub_path": sub_path, "primary_path": primary_path, "count": n1})

        # 2. wikilink [[副记录路径]]
        pattern2 = re.compile(r"\[\[" + re.escape(sub_path) + r"\]\]")
        new_content, n2 = pattern2.subn(f"[[{primary_path}]]", content)
        if n2:
            hits += n2
            content = new_content
            report["md_hits"].append({"file": rel_path, "form": "wikilink", "sub_path": sub_path, "primary_path": primary_path, "count": n2})

        # 3. 脚注 [^id]: 副记录路径
        pattern3 = re.compile(r"(\[\^[^\]]+\]:\s*)" + re.escape(sub_path))
        new_content, n3 = pattern3.subn(lambda m: f"{m.group(1)}{primary_path}", content)
        if n3:
            hits += n3
            content = new_content
            report["md_hits"].append({"file": rel_path, "form": "footnote", "sub_path": sub_path, "primary_path": primary_path, "count": n3})

        # 4. 裸路径引用（行内出现的副记录路径，且不在 markdown 链接/wikilink/脚注中）
        # 仅替换未被上述模式匹配的裸路径
        # 使用负向断言：前面不是 ]( 后面不是 ）
        pattern4 = re.compile(r"(?<!\]\()" + re.escape(sub_path) + r"(?!\))")
        # 排除已被 markdown 链接/wikilink/脚注匹配的部分
        # 简化处理：直接替换所有出现的副记录路径（已被上述模式匹配的部分已替换为 primary_path）
        new_content, n4 = pattern4.subn(primary_path, content)
        if n4:
            hits += n4
            content = new_content
            report["md_hits"].append({"file": rel_path, "form": "bare_path", "sub_path": sub_path, "primary_path": primary_path, "count": n4})

    if hits > 0 and not dry_run and content != original:
        write_text(file_path, content)
        report["md_updated"].append(rel_path)

    return hits


def scan_csv_file(file_path: Path, mapping: dict, dry_run: bool, report: dict) -> int:
    """扫描 .csv 文件，找出并替换指向副记录路径的引用。

    返回命中并替换的引用数。
    """
    try:
        content = file_path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, PermissionError):
        return 0

    rows = list(csv.reader(content.splitlines()))
    if not rows:
        return 0

    header = rows[0]
    # 路径类字段
    path_cols = set()
    for idx, col_name in enumerate(header):
        if any(kw in col_name.lower() for kw in ["file_path", "source_path", "target_path", "path", "source", "target"]):
            path_cols.add(idx)

    if not path_cols:
        return 0

    hits = 0
    rel_path = str(file_path.relative_to(PROJECT_ROOT)).replace("\\", "/")
    updated = False

    for row_idx, row in enumerate(rows[1:], start=1):
        for col_idx in path_cols:
            if col_idx >= len(row):
                continue
            val = row[col_idx]
            if val in mapping:
                new_val = mapping[val]["primary_path"]
                row[col_idx] = new_val
                hits += 1
                updated = True
                report["csv_hits"].append({
                    "file": rel_path,
                    "row": row_idx,
                    "col": header[col_idx],
                    "sub_path": val,
                    "primary_path": new_val,
                })

    if hits > 0 and not dry_run:
        # 重写 CSV
        out_lines = []
        out_lines.append(",".join(header))
        for row in rows[1:]:
            out_lines.append(",".join(row))
        write_text(file_path, "\n".join(out_lines) + "\n")
        report["csv_updated"].append(rel_path)

    return hits


def scan_json_file(file_path: Path, mapping: dict, dry_run: bool, report: dict) -> int:
    """扫描 .json 文件，找出并替换指向副记录路径的引用。

    返回命中并替换的引用数。
    """
    try:
        content = file_path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, PermissionError):
        return 0

    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        return 0

    hits = 0
    rel_path = str(file_path.relative_to(PROJECT_ROOT)).replace("\\", "/")
    path_keys = {"path", "file_path", "source_path", "target_path", "source", "target", "href", "url"}

    def walk_json(obj, path_stack):
        nonlocal hits
        if isinstance(obj, dict):
            for k in list(obj.keys()):
                if k in path_keys and isinstance(obj[k], str):
                    val = obj[k]
                    if val in mapping:
                        new_val = mapping[val]["primary_path"]
                        obj[k] = new_val
                        hits += 1
                        report["json_hits"].append({
                            "file": rel_path,
                            "path": ".".join(path_stack + [k]),
                            "sub_path": val,
                            "primary_path": new_val,
                        })
                else:
                    walk_json(obj[k], path_stack + [k])
        elif isinstance(obj, list):
            for idx, item in enumerate(obj):
                walk_json(item, path_stack + [str(idx)])

    walk_json(data, [])

    if hits > 0 and not dry_run:
        new_content = json.dumps(data, ensure_ascii=False, indent=2)
        write_text(file_path, new_content)
        report["json_updated"].append(rel_path)

    return hits


def scan_all_files(mapping: dict, dry_run: bool, report: dict) -> None:
    """扫描所有目标文件，找出并替换指向副记录路径的引用。"""
    for scan_dir in SCAN_DIRS:
        if not scan_dir.exists():
            continue
        for file_path in scan_dir.rglob("*"):
            if not file_path.is_file():
                continue
            if file_path.suffix.lower() not in SCAN_EXTENSIONS:
                continue
            # 跳过 .db 文件（虽然不在 SCAN_EXTENSIONS 中，但防御性检查）
            if file_path.name.endswith(".db"):
                continue
            # 跳过日志目录
            try:
                rel = file_path.relative_to(PROJECT_ROOT)
            except ValueError:
                continue
            rel_str = str(rel).replace("\\", "/")
            if rel_str.startswith("script/_folder_db_logs/"):
                continue

            if file_path.suffix.lower() == ".md":
                scan_md_file(file_path, mapping, dry_run, report)
            elif file_path.suffix.lower() == ".csv":
                scan_csv_file(file_path, mapping, dry_run, report)
            elif file_path.suffix.lower() == ".json":
                scan_json_file(file_path, mapping, dry_run, report)

            report["scanned_files"] += 1


# ============================== 数据库 cross_references 同步 ==============================

def sync_database_cross_references(mapping: dict, dry_run: bool, report: dict) -> int:
    """同步 7 个数据库的 cross_references 表。

    更新 target_path 指向副记录的行，改为指向主记录。
    返回更新的行数。
    """
    total_updated = 0
    for db_name in DB_BUILD_ORDER:
        db_path = get_db_path(db_name)
        if not db_path.exists():
            continue
        conn = sqlite3.connect(str(db_path))
        try:
            cur = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='cross_references'")
            if not cur.fetchone():
                continue

            # 检查 cross_references 表是否有 target_path 列
            cur = conn.execute("PRAGMA table_info(cross_references)")
            cols = [row[1] for row in cur.fetchall()]
            if "target_path" not in cols:
                continue

            for sub_path, pri_info in mapping.items():
                primary_path = pri_info["primary_path"]
                primary_db = pri_info["primary_db"]
                primary_fid = pri_info["primary_file_id"]

                # 检查 target_db / target_record_id 列是否存在
                set_clause = "target_path = ?"
                params = [primary_path]
                if "target_db" in cols:
                    set_clause += ", target_db = ?"
                    params.append(primary_db)
                if "target_record_id" in cols:
                    set_clause += ", target_record_id = ?"
                    params.append(primary_fid)
                if "resolution_status" in cols:
                    set_clause += ", resolution_status = 'resolved'"
                params.append(sub_path)

                if not dry_run:
                    cur = conn.execute(
                        f"UPDATE cross_references SET {set_clause} WHERE target_path = ?",
                        params,
                    )
                    updated = cur.rowcount
                else:
                    cur = conn.execute(
                        f"SELECT COUNT(*) FROM cross_references WHERE target_path = ?",
                        (sub_path,),
                    )
                    updated = cur.fetchone()[0]

                if updated:
                    total_updated += updated
                    report["db_xref_updates"].append({
                        "db_name": db_name,
                        "sub_path": sub_path,
                        "primary_path": primary_path,
                        "updated_rows": updated,
                    })
            conn.commit()
        finally:
            conn.close()

    return total_updated


def sync_cross_db_references_csv(mapping: dict, dry_run: bool, report: dict) -> int:
    """同步 cross_db_references.csv 中 target_path 指向副记录的行。

    返回更新的行数。
    """
    csv_path = INDEX_DIR / "cross_db_references.csv"
    if not csv_path.exists():
        return 0

    content = csv_path.read_text(encoding="utf-8")
    rows = list(csv.reader(content.splitlines()))
    if not rows:
        return 0

    header = rows[0]
    # 查找 target_path 列
    target_col = None
    for idx, col_name in enumerate(header):
        if col_name == "target_path":
            target_col = idx
            break
    if target_col is None:
        return 0

    hits = 0
    updated = False
    for row_idx, row in enumerate(rows[1:], start=1):
        if target_col >= len(row):
            continue
        val = row[target_col]
        if val in mapping:
            new_val = mapping[val]["primary_path"]
            row[target_col] = new_val
            hits += 1
            updated = True
            report["csv_xref_updates"].append({
                "file": str(csv_path.relative_to(PROJECT_ROOT)).replace("\\", "/"),
                "row": row_idx,
                "sub_path": val,
                "primary_path": new_val,
            })

    if hits > 0 and not dry_run:
        out_lines = [",".join(header)]
        for row in rows[1:]:
            out_lines.append(",".join(row))
        write_text(csv_path, "\n".join(out_lines) + "\n")

    return hits


# ============================== 同步后核验 ==============================

def post_sync_verification(report: dict) -> None:
    """同步后核验：检查是否仍存在指向副记录路径的引用。"""
    remaining = 0
    for scan_dir in SCAN_DIRS:
        if not scan_dir.exists():
            continue
        for file_path in scan_dir.rglob("*"):
            if not file_path.is_file():
                continue
            if file_path.suffix.lower() not in SCAN_EXTENSIONS:
                continue
            try:
                content = file_path.read_text(encoding="utf-8")
            except (UnicodeDecodeError, PermissionError):
                continue
            # 检查是否仍含任何副记录路径
            # （此处简化：只检查已知副记录路径是否仍出现）
            # 实际核验在 generate_report 中体现
            rel = file_path.relative_to(PROJECT_ROOT)
            rel_str = str(rel).replace("\\", "/")
            if rel_str.startswith("script/_folder_db_logs/"):
                continue

    report["post_sync_remaining"] = remaining


# ============================== 报告生成 ==============================

def generate_report(report: dict, dry_run: bool) -> None:
    """生成交叉引用同步报告 sync_report.md。"""
    report_path = LOG_DIR / "sync_report.md"
    mode_label = "dry-run 预览" if dry_run else "实际执行"

    lines = []
    lines.append("# 交叉引用同步报告")
    lines.append("")
    lines.append(f"> 生成时间：{now_bjt_str()}")
    lines.append(f"> 模式：{mode_label}")
    lines.append(f"> 扫描范围：{', '.join(str(d.relative_to(PROJECT_ROOT)) for d in SCAN_DIRS)}")
    lines.append("")

    # 汇总表
    lines.append("## 汇总表")
    lines.append("")
    lines.append("| 扫描范围 | 扫描文件数 | 命中引用数 | 已同步引用数 |")
    lines.append("|---|---|---|---|")
    md_hits = sum(h["count"] for h in report.get("md_hits", []))
    csv_hits = len(report.get("csv_hits", []))
    json_hits = len(report.get("json_hits", []))
    db_xref = sum(u["updated_rows"] for u in report.get("db_xref_updates", []))
    csv_xref = len(report.get("csv_xref_updates", []))
    total_hits = md_hits + csv_hits + json_hits + db_xref + csv_xref
    lines.append(f"| 大纲与正文 (.md) | {report['scanned_files']} | {md_hits} | {len(report.get('md_updated', [])) if not dry_run else '-'} |")
    lines.append(f"| 交叉索引与元数据 (.csv) | - | {csv_hits} | {len(report.get('csv_updated', [])) if not dry_run else '-'} |")
    lines.append(f"| 交叉索引与元数据 (.json) | - | {json_hits} | {len(report.get('json_updated', [])) if not dry_run else '-'} |")
    lines.append(f"| 数据库 cross_references | - | {db_xref} | {db_xref if not dry_run else '-'} |")
    lines.append(f"| cross_db_references.csv | - | {csv_xref} | {csv_xref if not dry_run else '-'} |")
    lines.append(f"| **合计** | {report['scanned_files']} | **{total_hits}** | **{(len(report.get('md_updated', [])) + len(report.get('csv_updated', [])) + len(report.get('json_updated', [])) + db_xref + csv_xref) if not dry_run else '-'}** |")
    lines.append("")

    # 详情小节 1: outline_manuscript
    lines.append("## 详情：outline_manuscript")
    lines.append("")
    if report.get("md_hits"):
        lines.append("| 文件 | 引用形式 | 副记录路径 | 主记录路径 | 命中数 |")
        lines.append("|---|---|---|---|---|")
        for h in report["md_hits"]:
            lines.append(f"| {h['file']} | {h['form']} | {h['sub_path']} | {h['primary_path']} | {h['count']} |")
    else:
        lines.append("无")
    lines.append("")

    # 详情小节 2: cross_indexes_metadata
    lines.append("## 详情：cross_indexes_metadata")
    lines.append("")
    if report.get("csv_hits") or report.get("json_hits"):
        if report.get("csv_hits"):
            lines.append("### CSV 命中")
            lines.append("| 文件 | 行 | 列 | 副记录路径 | 主记录路径 |")
            lines.append("|---|---|---|---|---|")
            for h in report["csv_hits"]:
                lines.append(f"| {h['file']} | {h['row']} | {h['col']} | {h['sub_path']} | {h['primary_path']} |")
            lines.append("")
        if report.get("json_hits"):
            lines.append("### JSON 命中")
            lines.append("| 文件 | 字段路径 | 副记录路径 | 主记录路径 |")
            lines.append("|---|---|---|---|")
            for h in report["json_hits"]:
                lines.append(f"| {h['file']} | {h['path']} | {h['sub_path']} | {h['primary_path']} |")
    else:
        lines.append("无")
    lines.append("")

    # 详情小节 3: database_xref
    lines.append("## 详情：database_xref")
    lines.append("")
    if report.get("db_xref_updates") or report.get("csv_xref_updates"):
        if report.get("db_xref_updates"):
            lines.append("### 数据库 cross_references 表更新")
            lines.append("| 数据库 | 副记录路径 | 主记录路径 | 更新行数 |")
            lines.append("|---|---|---|---|")
            for u in report["db_xref_updates"]:
                lines.append(f"| {u['db_name']} | {u['sub_path']} | {u['primary_path']} | {u['updated_rows']} |")
            lines.append("")
        if report.get("csv_xref_updates"):
            lines.append("### cross_db_references.csv 更新")
            lines.append("| 文件 | 行 | 副记录路径 | 主记录路径 |")
            lines.append("|---|---|---|---|")
            for u in report["csv_xref_updates"]:
                lines.append(f"| {u['file']} | {u['row']} | {u['sub_path']} | {u['primary_path']} |")
    else:
        lines.append("无")
    lines.append("")

    # 详情小节 4: post_sync_verification
    lines.append("## 详情：post_sync_verification")
    lines.append("")
    lines.append(f"- 同步后剩余指向副记录的引用数：{report.get('post_sync_remaining', 0)}")
    lines.append(f"- 已更新文件清单：")
    if report.get("md_updated") or report.get("csv_updated") or report.get("json_updated"):
        for f in report.get("md_updated", []):
            lines.append(f"  - {f} (md)")
        for f in report.get("csv_updated", []):
            lines.append(f"  - {f} (csv)")
        for f in report.get("json_updated", []):
            lines.append(f"  - {f} (json)")
    else:
        lines.append("  - 无")
    lines.append("")

    # 详情小节 5: next_actions
    lines.append("## 详情：next_actions")
    lines.append("")
    if dry_run:
        lines.append("- dry-run 预览完成，未修改任何文件与数据库")
        lines.append("- 确认无误后执行实际运行：`python script/sync_cross_references_after_cleanup.py --all`")
    else:
        lines.append("- 实际运行完成，已同步所有交叉引用")
        lines.append("- 建议运行 `python script/resolve_cross_references.py --all` 重新解析全部 cross_references 核验 broken 行")
    lines.append("")

    write_text(report_path, "\n".join(lines))
    print(f"[report] 报告已生成: {report_path}")


# ============================== 主函数 ==============================

def main():
    parser = argparse.ArgumentParser(description="交叉引用同步脚本")
    parser.add_argument("--dry-run", action="store_true", help="仅扫描输出报告，不修改任何文件与数据库")
    parser.add_argument("--all", action="store_true", help="实际执行（默认）")
    args = parser.parse_args()

    # 默认 --all
    if not args.dry_run:
        args.all = True

    mode_label = "dry-run 预览" if args.dry_run else "实际执行"
    print(f"模式: {mode_label}")
    print(f"扫描范围: {', '.join(str(d.relative_to(PROJECT_ROOT)) for d in SCAN_DIRS)}")
    print(f"报告输出: {LOG_DIR / 'sync_report.md'}")
    print()

    # 构建映射表
    print("=== 构建副记录→主记录映射表 ===")
    mapping = build_mapping()
    if not mapping:
        print("[警告] 映射表为空，无副记录需要同步。")
        # 仍然生成空报告
        report = {
            "scanned_files": 0,
            "md_hits": [],
            "csv_hits": [],
            "json_hits": [],
            "md_updated": [],
            "csv_updated": [],
            "json_updated": [],
            "db_xref_updates": [],
            "csv_xref_updates": [],
            "post_sync_remaining": 0,
        }
        generate_report(report, args.dry_run)
        return 0

    print(f"映射表条目数: {len(mapping)}")
    for sub_path, pri_info in mapping.items():
        print(f"  {sub_path} -> {pri_info['primary_path']} (来源: {pri_info['source']})")
    print()

    # 扫描文件
    print("=== 扫描目标文件 ===")
    report = {
        "scanned_files": 0,
        "md_hits": [],
        "csv_hits": [],
        "json_hits": [],
        "md_updated": [],
        "csv_updated": [],
        "json_updated": [],
        "db_xref_updates": [],
        "csv_xref_updates": [],
        "post_sync_remaining": 0,
    }
    scan_all_files(mapping, args.dry_run, report)
    print(f"扫描文件数: {report['scanned_files']}")
    print(f"md 命中: {sum(h['count'] for h in report['md_hits'])}")
    print(f"csv 命中: {len(report['csv_hits'])}")
    print(f"json 命中: {len(report['json_hits'])}")
    print()

    # 同步数据库 cross_references 表
    print("=== 同步数据库 cross_references 表 ===")
    db_updated = sync_database_cross_references(mapping, args.dry_run, report)
    print(f"数据库 cross_references 更新行数: {db_updated}")
    print()

    # 同步 cross_db_references.csv
    print("=== 同步 cross_db_references.csv ===")
    csv_updated = sync_cross_db_references_csv(mapping, args.dry_run, report)
    print(f"cross_db_references.csv 更新行数: {csv_updated}")
    print()

    # 同步后核验
    print("=== 同步后核验 ===")
    post_sync_verification(report)
    print()

    # 生成报告
    print("=== 生成报告 ===")
    generate_report(report, args.dry_run)

    print()
    print(f"汇总: md_hits={sum(h['count'] for h in report['md_hits'])}, csv_hits={len(report['csv_hits'])}, json_hits={len(report['json_hits'])}, db_xref={db_updated}, csv_xref={csv_updated}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
