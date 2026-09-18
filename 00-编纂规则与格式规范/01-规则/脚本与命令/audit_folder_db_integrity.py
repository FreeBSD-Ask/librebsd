#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""文件夹级数据库完整性复核脚本。

对 7 个文件夹级数据库执行三维度审计：
1. dangling_db_records — 数据库登记但磁盘不存在的记录
2. unindexed_disk_files — 磁盘存在但数据库未登记的文件
3. sha256_mismatch — SHA-256 一致性核验

输出：script/_folder_db_logs/integrity_audit_report.md（UTF-8 无 BOM，LF）

用法：
    python script/audit_folder_db_integrity.py --all
    python script/audit_folder_db_integrity.py --db sacred_sources
    python script/audit_folder_db_integrity.py --all --dry-run
"""
import argparse
import hashlib
import json
import os
import sqlite3
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent  # d:\librebsd
LOG_DIR = PROJECT_ROOT / "script" / "_folder_db_logs"
REPORT_FILE = LOG_DIR / "integrity_audit_report.md"
BJT = timezone(timedelta(hours=8))

# 7 个数据库配置映射
FOLDER_DB_MAP = {
    "sacred_sources": {
        "folder": "02-sacred源材料",
        "db_filename": "sacred_sources.db",
        "skip_subfolders": [],
        "skip_db_files": False,
    },
    "original_sources": {
        "folder": "03-原始史料库",
        "db_filename": "original_sources.db",
        "skip_subfolders": ["01-代码仓库史料", "02-man源与posix仓库"],
        "skip_db_files": True,
    },
    "research_notes": {
        "folder": "04-现代研究文献",
        "db_filename": "research_notes.db",
        "skip_subfolders": [
            "03-文献下载/01-pdf", "03-文献下载/02-epub", "03-文献下载/04-caj",
            "03-文献下载/05-书籍/01-pdf", "03-文献下载/05-书籍/02-epub",
            "05-参考文献全文数据库",
        ],
        "skip_db_files": True,
    },
    "fact_checks": {
        "folder": "07-事实核查记录",
        "db_filename": "fact_checks.db",
        "skip_subfolders": [],
        "skip_db_files": True,
    },
    "review_reports": {
        "folder": "08-核查报告与多轮复核",
        "db_filename": "review_reports.db",
        "skip_subfolders": [],
        "skip_db_files": True,
    },
    "cross_indexes": {
        "folder": "10-交叉索引",
        "db_filename": "cross_indexes.db",
        "skip_subfolders": [],
        "skip_db_files": True,
    },
    "metadata_interfaces": {
        "folder": "11-元数据接口",
        "db_filename": "metadata_interfaces.db",
        "skip_subfolders": ["09-文件夹数据库索引"],
        "skip_db_files": True,
    },
}

DB_BUILD_ORDER = [
    "sacred_sources", "original_sources", "research_notes",
    "fact_checks", "review_reports", "cross_indexes", "metadata_interfaces",
]

SUPPORTED_EXTENSIONS = {".md", ".txt", ".csv", ".json"}

BINARY_EXTENSIONS = {
    ".pdf", ".epub", ".caj", ".png", ".jpg", ".jpeg", ".gif", ".bmp",
    ".zip", ".tar", ".gz", ".7z", ".rar",
    ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
}

# git 仓库目录（硬跳过，不扫描、不报告）
GIT_REPO_DIRS = {"01-代码仓库史料", "02-man源与posix仓库"}


def get_db_path(db_name: str) -> Path:
    cfg = FOLDER_DB_MAP[db_name]
    return PROJECT_ROOT / cfg["folder"] / cfg["db_filename"]


def compute_sha256(file_path: Path) -> str:
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def to_rel_posix(file_path: Path) -> str:
    return file_path.relative_to(PROJECT_ROOT).as_posix()


def get_db_built_at(db_name: str):
    """从 build_log JSONL 解析数据库构建起始时间，失败返回 None。"""
    log_file = LOG_DIR / f"build_log_{db_name}.jsonl"
    if not log_file.exists():
        return None
    try:
        with open(log_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    entry = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if entry.get("action") == "start":
                    return entry.get("timestamp")
    except OSError:
        return None
    return None


def parse_iso(ts):
    """解析 ISO 时间字符串（无时区），失败返回 None。"""
    if not ts:
        return None
    try:
        return datetime.fromisoformat(ts)
    except (ValueError, TypeError):
        return None


def is_in_skip_subfolder(folder_rel: str, skip_subfolders) -> bool:
    """判断 folder 相对路径是否位于任一 skip_subfolder 下。

    folder_rel 为相对于该数据库文件夹的 POSIX 路径（如 "05-参考文献全文数据库/index.md"）；
    skip_subfolders 条目亦为 folder 相对路径（如 "05-参考文献全文数据库"）。
    """
    for skip in skip_subfolders:
        prefix = skip.rstrip("/") + "/"
        if folder_rel.startswith(prefix) or folder_rel == skip:
            return True
    return False


def infer_unindexed_reason(folder_rel, skip_subfolders, mtime_dt, built_at_dt):
    """推断 unindexed_disk_files 原因。"""
    if is_in_skip_subfolder(folder_rel, skip_subfolders):
        return "skipped_by_rules"
    if mtime_dt is not None and built_at_dt is not None:
        if mtime_dt > built_at_dt:
            return "newly_added"
    return "others"


def infer_mismatch_reason(abs_path: Path, db_mtime_str: str):
    """推断 sha256_mismatch 原因。"""
    try:
        disk_mtime_dt = datetime.fromtimestamp(abs_path.stat().st_mtime, tz=BJT)
    except OSError:
        return "others"
    db_mtime_dt = parse_iso(db_mtime_str)
    if db_mtime_dt is not None:
        db_mtime_local = db_mtime_dt.replace(tzinfo=BJT)
        if disk_mtime_dt > db_mtime_local:
            return "modified_after_ingest"
    return "encoding_change"


def audit_one_db(db_name: str):
    """复核单个数据库，返回 (dangling, unindexed, mismatch) 三类记录列表。"""
    cfg = FOLDER_DB_MAP[db_name]
    folder_path = PROJECT_ROOT / cfg["folder"]
    db_path = get_db_path(db_name)
    skip_subfolders = cfg["skip_subfolders"]

    dangling = []
    unindexed = []
    mismatch = []

    if not db_path.exists():
        print(f"  [警告] 数据库文件不存在：{db_path}", file=sys.stderr)
        return dangling, unindexed, mismatch

    # 1. 读取 files 表全部记录
    conn = sqlite3.connect(str(db_path))
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT id, file_path, sha256, status, duplicate_of_id, mtime FROM files"
        )
        db_rows = cur.fetchall()
    except sqlite3.Error as e:
        print(f"  [错误] 读取 {db_name} files 表失败：{e}", file=sys.stderr)
        conn.close()
        return dangling, unindexed, mismatch
    conn.close()

    db_paths_set = set()

    # 维度 1 + 3：dangling_db_records 与 sha256_mismatch
    for row in db_rows:
        file_id, file_path_str, sha256, status, dup_of, mtime_str = row
        db_paths_set.add(file_path_str)
        abs_path = PROJECT_ROOT / file_path_str
        if not abs_path.exists():
            dangling.append({
                "db_name": db_name,
                "file_id": file_id,
                "file_path": file_path_str,
                "sha256": sha256,
                "status": status,
                "duplicate_of_id": dup_of,
            })
            continue
        # SHA-256 核验
        try:
            disk_sha = compute_sha256(abs_path)
        except OSError as e:
            print(f"  [警告] 无法读取文件 {abs_path}: {e}", file=sys.stderr)
            continue
        if disk_sha != sha256:
            try:
                stat = abs_path.stat()
                disk_mtime_iso = datetime.fromtimestamp(
                    stat.st_mtime, tz=BJT
                ).strftime("%Y-%m-%dT%H:%M:%S")
            except OSError:
                disk_mtime_iso = "unknown"
            reason = infer_mismatch_reason(abs_path, mtime_str)
            mismatch.append({
                "db_name": db_name,
                "file_id": file_id,
                "file_path": file_path_str,
                "db_sha256": sha256,
                "disk_sha256": disk_sha,
                "mtime": disk_mtime_iso,
                "reason": reason,
            })

    # 维度 2：unindexed_disk_files
    built_at = get_db_built_at(db_name)
    built_at_dt = parse_iso(built_at)
    if built_at_dt is not None:
        # build_log 时间戳为本地时间（BJT），补齐时区以便与磁盘 mtime 比较
        built_at_dt = built_at_dt.replace(tzinfo=BJT)

    for root, dirs, files in os.walk(folder_path):
        # 硬跳过 git 仓库目录与 .git 目录（不递归进入）
        dirs[:] = [d for d in dirs if d not in GIT_REPO_DIRS and d != ".git"]
        for fname in files:
            file_path = Path(root) / fname
            ext = file_path.suffix.lower()
            # 跳过 .db 文件（数据库文件本身不入库）
            if ext == ".db":
                continue
            # 跳过二进制文件
            if ext in BINARY_EXTENSIONS:
                continue
            # 仅处理受支持扩展名
            if ext not in SUPPORTED_EXTENSIONS:
                continue
            try:
                rel_posix = to_rel_posix(file_path)
            except ValueError:
                continue
            # 已登记则跳过
            if rel_posix in db_paths_set:
                continue
            # folder 相对路径，用于 skip_subfolder 匹配
            try:
                folder_rel = file_path.relative_to(folder_path).as_posix()
            except ValueError:
                folder_rel = rel_posix
            # 未登记 → 记录
            try:
                stat = file_path.stat()
                size = stat.st_size
                mtime_dt = datetime.fromtimestamp(stat.st_mtime, tz=BJT)
                mtime_iso = mtime_dt.strftime("%Y-%m-%dT%H:%M:%S")
            except OSError:
                size = -1
                mtime_iso = "unknown"
                mtime_dt = None
            reason = infer_unindexed_reason(
                folder_rel, skip_subfolders, mtime_dt, built_at_dt
            )
            unindexed.append({
                "db_name": db_name,
                "file_path": rel_posix,
                "size": size,
                "mtime": mtime_iso,
                "reason": reason,
            })

    return dangling, unindexed, mismatch


def format_report(all_results, mode_label):
    """生成 Markdown 报告字符串。"""
    now = datetime.now(tz=BJT).strftime("%Y-%m-%d %H:%M:%S")
    lines = []
    lines.append("# 文件夹级数据库完整性复核报告")
    lines.append("")
    lines.append(f"> 生成时间：{now} BJT")
    lines.append(f"> 模式：{mode_label}")
    lines.append("")

    # 汇总表
    lines.append("## 汇总表")
    lines.append("")
    lines.append("| db_name | dangling_db_records | unindexed_disk_files | sha256_mismatch |")
    lines.append("|---|---|---|---|")
    totals = {"dangling": 0, "unindexed": 0, "mismatch": 0}
    for db_name in DB_BUILD_ORDER:
        if db_name not in all_results:
            continue
        r = all_results[db_name]
        d = len(r["dangling"])
        u = len(r["unindexed"])
        m = len(r["mismatch"])
        totals["dangling"] += d
        totals["unindexed"] += u
        totals["mismatch"] += m
        lines.append(f"| {db_name} | {d} | {u} | {m} |")
    lines.append(
        f"| **合计** | **{totals['dangling']}** | "
        f"**{totals['unindexed']}** | **{totals['mismatch']}** |"
    )
    lines.append("")

    # 详情：dangling_db_records
    lines.append("## 详情：dangling_db_records")
    lines.append("")
    any_dangling = False
    for db_name in DB_BUILD_ORDER:
        if db_name not in all_results:
            continue
        records = all_results[db_name]["dangling"]
        if not records:
            continue
        any_dangling = True
        lines.append(f"### {db_name}")
        lines.append("")
        for r in records:
            dup = r["duplicate_of_id"] if r["duplicate_of_id"] is not None else "NULL"
            lines.append(
                f"- file_id: {r['file_id']}, file_path: `{r['file_path']}`, "
                f"sha256: `{r['sha256']}`, status: {r['status']}, "
                f"duplicate_of_id: {dup}"
            )
        lines.append("")
    if not any_dangling:
        lines.append("无")
        lines.append("")

    # 详情：unindexed_disk_files
    lines.append("## 详情：unindexed_disk_files")
    lines.append("")
    any_unindexed = False
    for db_name in DB_BUILD_ORDER:
        if db_name not in all_results:
            continue
        records = all_results[db_name]["unindexed"]
        if not records:
            continue
        any_unindexed = True
        lines.append(f"### {db_name}")
        lines.append("")
        for r in records:
            lines.append(
                f"- file_path: `{r['file_path']}`, size: {r['size']} bytes, "
                f"mtime: {r['mtime']}, 推断原因: {r['reason']}"
            )
        lines.append("")
    if not any_unindexed:
        lines.append("无")
        lines.append("")

    # 详情：sha256_mismatch
    lines.append("## 详情：sha256_mismatch")
    lines.append("")
    any_mismatch = False
    for db_name in DB_BUILD_ORDER:
        if db_name not in all_results:
            continue
        records = all_results[db_name]["mismatch"]
        if not records:
            continue
        any_mismatch = True
        lines.append(f"### {db_name}")
        lines.append("")
        for r in records:
            lines.append(
                f"- file_id: {r['file_id']}, file_path: `{r['file_path']}`, "
                f"db_sha256: `{r['db_sha256']}`, disk_sha256: `{r['disk_sha256']}`, "
                f"mtime: {r['mtime']}, 推断原因: {r['reason']}"
            )
        lines.append("")
    if not any_mismatch:
        lines.append("无")
        lines.append("")

    # 建议动作
    lines.append("## 建议动作")
    lines.append("")
    lines.append("### dangling_db_records")
    lines.append("")
    lines.append(
        "- 建议：从数据库删除记录"
        "（`python script/build_folder_databases.py --update-file <path>` 或手动 DELETE）"
    )
    lines.append(f"- 影响数量：{totals['dangling']}")
    lines.append("")
    lines.append("### unindexed_disk_files")
    lines.append("")
    lines.append(
        "- 建议：使用 `python script/build_folder_databases.py --add-file <path>` 入库"
    )
    lines.append(f"- 影响数量：{totals['unindexed']}")
    lines.append("")
    lines.append("### sha256_mismatch")
    lines.append("")
    lines.append(
        "- 建议：使用 `python script/build_folder_databases.py --update-file <path>` 刷新"
    )
    lines.append(f"- 影响数量：{totals['mismatch']}")
    lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="文件夹级数据库完整性复核脚本"
    )
    parser.add_argument(
        "--db", metavar="<db_name>",
        help="只复核单个数据库"
    )
    parser.add_argument(
        "--all", action="store_true",
        help="复核全部 7 个数据库"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="仅输出报告不修改任何文件（dry-run 预览）"
    )
    args = parser.parse_args()

    if not args.all and not args.db:
        parser.error("请指定 --all 或 --db <db_name>")
    if args.all and args.db:
        parser.error("--all 与 --db 不可同时使用")
    if args.db and args.db not in FOLDER_DB_MAP:
        parser.error(
            f"未知数据库名：{args.db}，可选：{', '.join(DB_BUILD_ORDER)}"
        )

    if args.all:
        target_dbs = DB_BUILD_ORDER
    else:
        target_dbs = [args.db]

    if args.dry_run:
        mode_label = "dry-run 预览"
    elif args.all:
        mode_label = "全量复核"
    else:
        mode_label = f"单库复核（{args.db}）"

    all_results = {}
    for db_name in target_dbs:
        print(f"[开始] 复核 {db_name} ...")
        try:
            dangling, unindexed, mismatch = audit_one_db(db_name)
        except Exception as e:
            print(f"  [错误] 复核 {db_name} 失败：{e}", file=sys.stderr)
            dangling, unindexed, mismatch = [], [], []
        all_results[db_name] = {
            "dangling": dangling,
            "unindexed": unindexed,
            "mismatch": mismatch,
        }
        print(
            f"[完成] {db_name}：dangling={len(dangling)}, "
            f"unindexed={len(unindexed)}, mismatch={len(mismatch)}"
        )

    LOG_DIR.mkdir(parents=True, exist_ok=True)
    report = format_report(all_results, mode_label)
    with open(REPORT_FILE, "w", encoding="utf-8", newline="\n") as f:
        f.write(report)
    print(f"\n报告已生成：{REPORT_FILE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
