#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""精确重复副记录源文件清理脚本。

遵循"双重校验+安全删除"原则，清理 files 表中 duplicate_type='exact'
且 duplicate_of_id IS NOT NULL 的副记录源文件。

支持三种 CLI 模式：
    --db <db_name>   只清理单个数据库
    --all            清理全部 7 个数据库
    --dry-run        仅输出报告不实际删除文件，不修改数据库

输出报告：script/_folder_db_logs/cleanup_report.md
"""
import argparse
import hashlib
import sqlite3
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent  # d:\librebsd
LOG_DIR = PROJECT_ROOT / "script" / "_folder_db_logs"
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

DB_BUILD_ORDER = ["sacred_sources", "original_sources", "research_notes", "fact_checks", "review_reports", "cross_indexes", "metadata_interfaces"]

SACRED_PREFIX = "02-sacred源材料/"
GIT_REPO_PREFIXES = ("03-原始史料库/01-代码仓库史料/", "03-原始史料库/02-man源与posix仓库/")
BINARY_EXTENSIONS = {".pdf", ".epub", ".caj", ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".zip", ".tar", ".gz", ".7z", ".rar", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx"}
EMPTY_FILE_SHA256 = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"


def get_db_path(db_name: str) -> Path:
    """解析数据库绝对路径。"""
    cfg = FOLDER_DB_MAP[db_name]
    return PROJECT_ROOT / cfg["folder"] / cfg["db_filename"]


def resolve_file_path(rel_path: str) -> Path:
    """将 POSIX 风格相对路径解析为磁盘绝对路径。"""
    return PROJECT_ROOT / rel_path


def compute_sha256(file_path: Path) -> str:
    """计算文件 SHA-256（分块读取）。"""
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def now_bjt_str() -> str:
    """当前北京时间字符串。"""
    return datetime.now(BJT).strftime("%Y-%m-%d %H:%M:%S BJT")


def is_binary_path(rel_path: str) -> bool:
    """判断相对路径是否为二进制文件（按扩展名）。"""
    return Path(rel_path).suffix.lower() in BINARY_EXTENSIONS


def is_sacred_path(rel_path: str) -> bool:
    """判断是否位于 sacred 源材料目录。"""
    return rel_path.startswith(SACRED_PREFIX)


def is_git_repo_path(rel_path: str) -> bool:
    """判断是否位于 git 仓库目录。"""
    return any(rel_path.startswith(p) for p in GIT_REPO_PREFIXES)


class DbProcessor:
    """单个数据库的清理处理器。"""

    def __init__(self, db_name: str, dry_run: bool):
        self.db_name = db_name
        self.dry_run = dry_run
        self.db_path = get_db_path(db_name)

        # 统计与详情
        self.exact_total = 0
        self.fuzzy_total = 0
        self.deleted_count = 0
        self.skipped_count = 0  # 校验失败 + sacred + git/binary
        self.preserved_count = 0

        # 详情列表
        self.deleted_records = []      # list[dict]
        self.preserved_records = []    # list[dict]
        self.skipped_records = []      # list[dict]  校验失败
        self.skipped_sacred_records = []   # list[dict]
        self.skipped_git_or_binary_records = []  # list[dict]
        self.empty_files = []          # list[dict]  0 字节文件（主+副）

    def process(self) -> bool:
        """处理该数据库，返回是否成功。"""
        if not self.db_path.exists():
            print(f"[{self.db_name}] 数据库不存在: {self.db_path}", file=sys.stderr)
            return False

        print(f"[{self.db_name}] 开始处理: {self.db_path}")

        conn = sqlite3.connect(str(self.db_path))
        try:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()

            # 检查 files 表是否存在
            cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='files'")
            if cur.fetchone() is None:
                print(f"[{self.db_name}] 无 files 表，跳过")
                return True

            # 查询 exact 副记录
            cur.execute("""
                SELECT id, file_path, sha256, file_size, duplicate_of_id, duplicate_type, status
                FROM files
                WHERE duplicate_type='exact' AND duplicate_of_id IS NOT NULL
                ORDER BY id
            """)
            sub_rows = cur.fetchall()
            self.exact_total = len(sub_rows)

            # 查询 fuzzy 数量（仅汇总）
            cur.execute("SELECT COUNT(*) FROM files WHERE duplicate_type='fuzzy'")
            self.fuzzy_total = cur.fetchone()[0]

            print(f"[{self.db_name}] exact 副记录 {self.exact_total} 条，fuzzy 记录 {self.fuzzy_total} 条")

            for row in sub_rows:
                self._process_one(cur, row)

        finally:
            conn.close()

        return True

    def _process_one(self, cur, sub_row: sqlite3.Row):
        """处理单条 exact 副记录。"""
        sub_id = sub_row["id"]
        sub_path = sub_row["file_path"]
        sub_sha = sub_row["sha256"]
        sub_size = sub_row["file_size"]
        main_id = sub_row["duplicate_of_id"]

        # 收集 0 字节副记录
        if sub_size == 0:
            self.empty_files.append({
                "db_name": self.db_name,
                "role": "副记录",
                "file_id": sub_id,
                "file_path": sub_path,
                "sha256": sub_sha,
            })

        # 例外 1：sacred 源材料
        if is_sacred_path(sub_path):
            self.skipped_sacred_records.append({
                "db_name": self.db_name,
                "file_id": sub_id,
                "file_path": sub_path,
                "sha256": sub_sha,
                "reason": "sacred immutable",
            })
            self.skipped_count += 1
            print(f"  [skip-sacred] id={sub_id} {sub_path}")
            return

        # 例外 2：git 仓库或二进制文件
        if is_git_repo_path(sub_path) or is_binary_path(sub_path):
            reason_parts = []
            if is_git_repo_path(sub_path):
                reason_parts.append("git 仓库目录")
            if is_binary_path(sub_path):
                reason_parts.append(f"二进制扩展名 {Path(sub_path).suffix.lower()}")
            self.skipped_git_or_binary_records.append({
                "db_name": self.db_name,
                "file_id": sub_id,
                "file_path": sub_path,
                "sha256": sub_sha,
                "reason": "；".join(reason_parts),
            })
            self.skipped_count += 1
            print(f"  [skip-git-or-binary] id={sub_id} {sub_path}")
            return

        # 查询主记录
        cur.execute("SELECT id, file_path, sha256, file_size FROM files WHERE id=?", (main_id,))
        main_row = cur.fetchone()
        if main_row is None:
            self.skipped_records.append({
                "db_name": self.db_name,
                "sub_file_id": sub_id,
                "sub_file_path": sub_path,
                "sub_sha256": sub_sha,
                "main_file_id": main_id,
                "main_file_path": None,
                "main_sha256": None,
                "reason": "主记录不存在（duplicate_of_id 指向的 id 在 files 表中未找到）",
            })
            self.skipped_count += 1
            print(f"  [skip] id={sub_id} 主记录 id={main_id} 不存在")
            return

        main_path = main_row["file_path"]
        main_sha = main_row["sha256"]
        main_size = main_row["file_size"]

        # 收集 0 字节主记录
        if main_size == 0:
            self.empty_files.append({
                "db_name": self.db_name,
                "role": "主记录",
                "file_id": main_id,
                "file_path": main_path,
                "sha256": main_sha,
            })

        # 双重校验
        # 校验 1：副记录磁盘文件存在 + 磁盘 SHA-256 == db SHA-256
        sub_disk = resolve_file_path(sub_path)
        if not sub_disk.exists():
            self._skip_verify_fail(sub_row, main_row,
                f"副记录磁盘文件不存在: {sub_disk}")
            return
        try:
            sub_disk_sha = compute_sha256(sub_disk)
        except OSError as e:
            self._skip_verify_fail(sub_row, main_row,
                f"副记录磁盘 SHA-256 计算失败: {e}")
            return
        if sub_disk_sha != sub_sha:
            self._skip_verify_fail(sub_row, main_row,
                f"副记录磁盘 SHA-256 与 db 不一致: disk={sub_disk_sha} db={sub_sha}")
            return

        # 校验 2：主记录磁盘文件存在 + 磁盘 SHA-256 == db SHA-256
        main_disk = resolve_file_path(main_path)
        if not main_disk.exists():
            self._skip_verify_fail(sub_row, main_row,
                f"主记录磁盘文件不存在: {main_disk}")
            return
        try:
            main_disk_sha = compute_sha256(main_disk)
        except OSError as e:
            self._skip_verify_fail(sub_row, main_row,
                f"主记录磁盘 SHA-256 计算失败: {e}")
            return
        if main_disk_sha != main_sha:
            self._skip_verify_fail(sub_row, main_row,
                f"主记录磁盘 SHA-256 与 db 不一致: disk={main_disk_sha} db={main_sha}")
            return

        # 校验 3：副记录 SHA-256 与主记录 SHA-256 完全相同
        if sub_sha != main_sha:
            self._skip_verify_fail(sub_row, main_row,
                f"副记录与主记录 SHA-256 不一致: sub={sub_sha} main={main_sha}")
            return

        # 三项校验全部通过，执行删除
        delete_time = now_bjt_str()
        if self.dry_run:
            print(f"  [dry-run-delete] id={sub_id} {sub_path}")
            actual_deleted = False
        else:
            try:
                sub_disk.unlink()
                actual_deleted = True
                print(f"  [deleted] id={sub_id} {sub_path}")
            except OSError as e:
                self._skip_verify_fail(sub_row, main_row,
                    f"删除副记录源文件失败: {e}")
                return

        self.deleted_count += 1
        self.preserved_count += 1

        self.deleted_records.append({
            "db_name": self.db_name,
            "sub_file_id": sub_id,
            "sub_file_path": sub_path,
            "main_file_id": main_id,
            "main_file_path": main_path,
            "sha256": sub_sha,
            "delete_time": delete_time,
            "actual_deleted": actual_deleted,
        })
        self.preserved_records.append({
            "db_name": self.db_name,
            "main_file_id": main_id,
            "main_file_path": main_path,
            "sha256": main_sha,
            "sub_file_id": sub_id,
            "sub_file_path": sub_path,
        })

    def _skip_verify_fail(self, sub_row: sqlite3.Row, main_row, reason: str):
        """记录校验失败。"""
        self.skipped_records.append({
            "db_name": self.db_name,
            "sub_file_id": sub_row["id"],
            "sub_file_path": sub_row["file_path"],
            "sub_sha256": sub_row["sha256"],
            "main_file_id": main_row["id"] if main_row else None,
            "main_file_path": main_row["file_path"] if main_row else None,
            "main_sha256": main_row["sha256"] if main_row else None,
            "reason": reason,
        })
        self.skipped_count += 1
        print(f"  [skip-verify] id={sub_row['id']} {sub_row['file_path']} - {reason}")


def build_report(processors, dry_run: bool, target_dbs) -> str:
    """组装清理报告 Markdown 文本。"""
    lines = []
    lines.append("# 重复源文件清理报告")
    lines.append("")
    mode_label = "dry-run 预览（不实际删除文件，不修改数据库）" if dry_run else "实际清理"
    lines.append(f"> 生成时间：{now_bjt_str()}")
    lines.append(f"> 模式：{mode_label}")
    lines.append(f"> 目标数据库：{', '.join(target_dbs)}")
    lines.append("")

    # 汇总表
    lines.append("## 汇总表")
    lines.append("")
    lines.append("| db_name | exact_duplicates | deleted | skipped | preserved |")
    lines.append("|---|---|---|---|---|")
    for p in processors:
        lines.append(f"| {p.db_name} | {p.exact_total} | {p.deleted_count} | {p.skipped_count} | {p.preserved_count} |")
    # 合计行
    tot_exact = sum(p.exact_total for p in processors)
    tot_deleted = sum(p.deleted_count for p in processors)
    tot_skipped = sum(p.skipped_count for p in processors)
    tot_preserved = sum(p.preserved_count for p in processors)
    lines.append(f"| **合计** | **{tot_exact}** | **{tot_deleted}** | **{tot_skipped}** | **{tot_preserved}** |")
    lines.append("")

    # 详情：deleted
    lines.append("## 详情：deleted")
    lines.append("")
    all_deleted = [r for p in processors for r in p.deleted_records]
    if not all_deleted:
        lines.append("无")
        lines.append("")
    else:
        # 按 db_name 分组
        by_db = {}
        for r in all_deleted:
            by_db.setdefault(r["db_name"], []).append(r)
        for db_name in DB_BUILD_ORDER:
            if db_name not in by_db:
                continue
            lines.append(f"### {db_name}")
            lines.append("")
            for r in by_db[db_name]:
                action_note = "" if r["actual_deleted"] else "（dry-run 预览，未实际删除）"
                lines.append(f"- 副记录 file_id: {r['sub_file_id']}, file_path: {r['sub_file_path']}")
                lines.append(f"- 主记录 file_id: {r['main_file_id']}, file_path: {r['main_file_path']}")
                lines.append(f"- SHA-256: {r['sha256']}")
                lines.append(f"- 删除时间: {r['delete_time']}{action_note}")
                lines.append("")

    # 详情：preserved
    lines.append("## 详情：preserved")
    lines.append("")
    all_preserved = [r for p in processors for r in p.preserved_records]
    if not all_preserved:
        lines.append("无")
        lines.append("")
    else:
        by_db = {}
        for r in all_preserved:
            by_db.setdefault(r["db_name"], []).append(r)
        for db_name in DB_BUILD_ORDER:
            if db_name not in by_db:
                continue
            lines.append(f"### {db_name}")
            lines.append("")
            for r in by_db[db_name]:
                lines.append(f"- 主记录 file_id: {r['main_file_id']}, file_path: {r['main_file_path']}")
                lines.append(f"  - SHA-256: {r['sha256']}")
                lines.append(f"  - 对应副记录 file_id: {r['sub_file_id']}, file_path: {r['sub_file_path']}")
                lines.append("")

    # 详情：skipped
    lines.append("## 详情：skipped")
    lines.append("")
    all_skipped = [r for p in processors for r in p.skipped_records]
    if not all_skipped:
        lines.append("无")
        lines.append("")
    else:
        by_db = {}
        for r in all_skipped:
            by_db.setdefault(r["db_name"], []).append(r)
        for db_name in DB_BUILD_ORDER:
            if db_name not in by_db:
                continue
            lines.append(f"### {db_name}")
            lines.append("")
            for r in by_db[db_name]:
                lines.append(f"- 副记录 file_id: {r['sub_file_id']}, file_path: {r['sub_file_path']}")
                main_path = r.get("main_file_path")
                main_id = r.get("main_file_id")
                if main_id is not None:
                    lines.append(f"  - 主记录 file_id: {main_id}, file_path: {main_path}")
                lines.append(f"  - 原因: {r['reason']}")
                lines.append("")

    # 详情：skipped_sacred
    lines.append("## 详情：skipped_sacred")
    lines.append("")
    all_sacred = [r for p in processors for r in p.skipped_sacred_records]
    if not all_sacred:
        lines.append("无")
        lines.append("")
    else:
        by_db = {}
        for r in all_sacred:
            by_db.setdefault(r["db_name"], []).append(r)
        for db_name in DB_BUILD_ORDER:
            if db_name not in by_db:
                continue
            lines.append(f"### {db_name}")
            lines.append("")
            for r in by_db[db_name]:
                lines.append(f"- file_path: {r['file_path']}")
                lines.append(f"  - 原 SHA-256: {r['sha256']}")
                lines.append(f"  - 原因: {r['reason']}（sacred 源材料 immutable=true，禁止删除）")
                lines.append("")

    # 详情：skipped_git_or_binary
    lines.append("## 详情：skipped_git_or_binary")
    lines.append("")
    all_gb = [r for p in processors for r in p.skipped_git_or_binary_records]
    if not all_gb:
        lines.append("无")
        lines.append("")
    else:
        by_db = {}
        for r in all_gb:
            by_db.setdefault(r["db_name"], []).append(r)
        for db_name in DB_BUILD_ORDER:
            if db_name not in by_db:
                continue
            lines.append(f"### {db_name}")
            lines.append("")
            for r in by_db[db_name]:
                lines.append(f"- file_path: {r['file_path']}")
                lines.append(f"  - 原 SHA-256: {r['sha256']}")
                lines.append(f"  - 原因: {r['reason']}")
                lines.append("")

    # 详情：skipped_fuzzy
    lines.append("## 详情：skipped_fuzzy")
    lines.append("")
    any_fuzzy = any(p.fuzzy_total > 0 for p in processors)
    if not any_fuzzy:
        lines.append("无")
        lines.append("")
    else:
        lines.append("模糊重复建议人工复核后决定是否合并。")
        lines.append("")
        lines.append("| db_name | fuzzy_count |")
        lines.append("|---|---|")
        for p in processors:
            if p.fuzzy_total > 0:
                lines.append(f"| {p.db_name} | {p.fuzzy_total} |")
        lines.append("")

    # empty_files
    lines.append("## empty_files")
    lines.append("")
    all_empty = [r for p in processors for r in p.empty_files]
    if not all_empty:
        lines.append("无")
        lines.append("")
    else:
        lines.append("0 字节文件清单（SHA-256 固定值 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`）：")
        lines.append("")
        lines.append("| db_name | 角色 | file_id | file_path |")
        lines.append("|---|---|---|---|")
        for r in all_empty:
            lines.append(f"| {r['db_name']} | {r['role']} | {r['file_id']} | {r['file_path']} |")
        lines.append("")

    # next_actions
    lines.append("## next_actions")
    lines.append("")
    affected = [p.db_name for p in processors if p.deleted_count > 0]
    if not affected:
        lines.append("无受影响数据库（无需重建）。")
        lines.append("")
    else:
        lines.append("建议重建受影响数据库：")
        lines.append("")
        for db_name in affected:
            lines.append(f"- `python script/build_folder_databases.py --rebuild {db_name}`")
        lines.append("")

    return "\n".join(lines)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="精确重复副记录源文件清理脚本（双重校验+安全删除）",
    )
    parser.add_argument("--db", metavar="<db_name>",
                        choices=DB_BUILD_ORDER,
                        help="只清理单个数据库")
    parser.add_argument("--all", action="store_true",
                        help="清理全部 7 个数据库")
    parser.add_argument("--dry-run", action="store_true",
                        help="仅输出报告不实际删除文件，不修改数据库")
    args = parser.parse_args(argv)

    # 参数互斥与组合校验
    if args.all and args.db:
        parser.error("--db 与 --all 互斥，请二选一")
    if not args.all and not args.db:
        parser.error("必须指定 --db <db_name> 或 --all")

    if args.all:
        target_dbs = list(DB_BUILD_ORDER)
    else:
        target_dbs = [args.db]

    # 确保日志目录存在
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    print(f"模式: {'dry-run 预览' if args.dry_run else '实际清理'}")
    print(f"目标数据库: {', '.join(target_dbs)}")
    print(f"报告输出: {LOG_DIR / 'cleanup_report.md'}")
    print("")

    processors = []
    ok = True
    for db_name in target_dbs:
        p = DbProcessor(db_name, dry_run=args.dry_run)
        if not p.process():
            ok = False
            # 仍加入 processors 以便在报告中体现
        processors.append(p)

    # 生成报告
    report_text = build_report(processors, dry_run=args.dry_run, target_dbs=target_dbs)
    report_path = LOG_DIR / "cleanup_report.md"
    with open(report_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(report_text)

    print("")
    print(f"报告已生成: {report_path}")
    tot_deleted = sum(p.deleted_count for p in processors)
    tot_skipped = sum(p.skipped_count for p in processors)
    tot_preserved = sum(p.preserved_count for p in processors)
    print(f"汇总: deleted={tot_deleted}, skipped={tot_skipped}, preserved={tot_preserved}")

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
