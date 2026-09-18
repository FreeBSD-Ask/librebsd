# -*- coding: utf-8 -*-
"""
文件夹级数据库去重脚本

用途：在 7 个文件夹级 SQLite 数据库构建前后执行去重核验。

7 个数据库：
    1. 02-sacred源材料/sacred_sources.db
    2. 03-原始史料库/original_sources.db
    3. 04-现代研究文献/research_notes.db
    4. 07-事实核查记录/fact_checks.db
    5. 08-核查报告与多轮复核/review_reports.db
    6. 10-交叉索引/cross_indexes.db
    7. 11-元数据接口/metadata_interfaces.db

三种运行模式：
    --pre   构建前去重：扫描源文件、计算 SHA-256、识别精确/模糊/跨文件夹重复
    --post  构建后去重：核验各数据库 files 表的 file_path/sha256/content_hash 唯一性
    --all   同时执行 --pre 与 --post

约束：
    - 源文件不可变（IMMUTABLE），仅读取用于哈希与比较
    - 02-sacred源材料为 immutable=true，严格只读
    - 不删除数据库中的重复记录，仅以 duplicate_of_id 与 duplicate_type 标记
    - 使用事务提交数据库变更
    - 缺失数据库时记录警告并跳过（--post 模式）
    - 编码 UTF-8 无 BOM，LF 换行

依赖：仅 Python 3.8+ 标准库（sqlite3, hashlib, json, csv, pathlib, re, argparse,
       difflib, os, time, datetime）

关联规范：convert-folders-to-databases-2026-07-31
关联架构：00-编纂规则与格式规范/01-规则/脚本与命令/folder_db_common_schema.sql
"""

import argparse
import csv
import difflib
import hashlib
import json
import os
import re
import sqlite3
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

# 项目根目录
ROOT = Path(r"d:\librebsd")

# 时区（北京时间）
BJT = timezone(timedelta(hours=8))

# 7 个文件夹级数据库与对应扫描根目录
# (db_name, db_relative_path, scan_folder_relative_path)
DATABASES = [
    ("sacred_sources", "02-sacred源材料/sacred_sources.db", "02-sacred源材料/"),
    ("original_sources", "03-原始史料库/original_sources.db", "03-原始史料库/"),
    ("research_notes", "04-现代研究文献/research_notes.db", "04-现代研究文献/"),
    ("fact_checks", "07-事实核查记录/fact_checks.db", "07-事实核查记录/"),
    ("review_reports", "08-核查报告与多轮复核/review_reports.db", "08-核查报告与多轮复核/"),
    ("cross_indexes", "10-交叉索引/cross_indexes.db", "10-交叉索引/"),
    ("metadata_interfaces", "11-元数据接口/metadata_interfaces.db", "11-元数据接口/"),
]

# 待扫描文件扩展名（小写，含点）
SCAN_EXTENSIONS = {".md", ".txt", ".csv", ".json"}

# 跳过的目录名（任意层级匹配，避免 os.walk 进入）
SKIP_DIR_NAMES = {
    ".git", ".github", ".trae", ".vscode", ".idea",
    "__pycache__", ".ipynb_checkpoints", "node_modules",
}

# 跳过的相对路径前缀（POSIX 风格，相对于项目根目录）
# 用于跳过 git 仓库史料、二进制文件目录、文件夹数据库索引等
SKIP_PATH_PREFIXES = (
    "03-原始史料库/01-代码仓库史料/",            # git 仓库史料（独立数据库已处理）
    "03-原始史料库/02-man源与posix仓库/",        # man 源与 POSIX 仓库（稀疏检出仓库）
    "04-现代研究文献/03-文献下载/01-pdf/",        # 二进制 PDF/PS
    "04-现代研究文献/03-文献下载/04-caj/",        # 二进制 CAJ
    "04-现代研究文献/03-文献下载/05-书籍/01-pdf/",  # 二进制书籍 PDF
    "04-现代研究文献/03-文献下载/05-书籍/02-epub/",  # 二进制书籍 EPUB
    "04-现代研究文献/05-参考文献全文数据库/",    # 参考文献全文数据库（含 PNG 资产，独立 schema）
    "11-元数据接口/09-文件夹数据库索引/",        # 文件夹数据库索引（本脚本输出区）
)

# 模糊重复阈值
FUZZY_THRESHOLD = 0.85

# 长度比预过滤阈值：当 title 长度比 < 0.74 时，相似度必 < 0.85
LEN_RATIO_PREFILTER = 0.74

# 输出目录与文件
LOG_DIR = ROOT / "script" / "_folder_db_logs"
DASHBOARD_DIR_2 = ROOT / "11-元数据接口" / "09-文件夹数据库索引"
REPORT_PRE = LOG_DIR / "dedup_report_pre.md"
REPORT_POST = LOG_DIR / "dedup_report_post.md"
DASHBOARD_1 = LOG_DIR / "dashboard.md"
DASHBOARD_2 = DASHBOARD_DIR_2 / "dashboard.md"


# =============================================================================
# 工具函数
# =============================================================================

def now_str():
    """返回 ISO 8601 北京时间字符串。"""
    return datetime.now(BJT).strftime("%Y-%m-%dT%H:%M:%S")


def to_posix(rel_path):
    """将 Path 转为 POSIX 风格相对路径字符串（用 / 分隔）。"""
    return rel_path.as_posix()


def should_skip_dir(name):
    """判断目录名是否在跳过名单中。"""
    return name in SKIP_DIR_NAMES


def should_skip_path(rel_posix):
    """判断相对路径是否落在跳过的目录前缀内。"""
    for prefix in SKIP_PATH_PREFIXES:
        if rel_posix.startswith(prefix):
            return True
    return False


def compute_sha256(file_path):
    """计算文件 SHA-256（分块读取，避免大文件占内存）。"""
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _write_lf(path, content):
    """以 LF 换行、UTF-8 无 BOM 写入文件。"""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)


# =============================================================================
# 标题与摘要提取
# =============================================================================

def extract_title_summary(file_path, ext):
    """根据文件扩展名提取标题与首段摘要。

    返回 (title, summary) 元组；解析失败时返回 (None, None)。
    """
    try:
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
    except OSError:
        return (None, None)

    if ext == ".md":
        return _extract_md(content)
    if ext == ".txt":
        return _extract_txt(content, file_path.stem)
    if ext == ".csv":
        return _extract_csv(file_path)
    if ext == ".json":
        return _extract_json(content)
    return (None, None)


def _extract_md(content):
    """Markdown：标题为首个 # 标题；摘要为首段非空非标题段落（前 200 字符）。"""
    title = None
    summary = None
    para_lines = []
    in_frontmatter = False
    fm_count = 0
    for line in content.splitlines():
        stripped = line.strip()
        if stripped == "---":
            in_frontmatter = not in_frontmatter
            fm_count += 1
            if fm_count >= 2:
                in_frontmatter = False
            continue
        if in_frontmatter:
            continue
        if not stripped:
            if para_lines:
                summary = "\n".join(para_lines).strip()[:200]
                break
            continue
        if title is None and stripped.startswith("#"):
            m = re.match(r"^#+\s+(.+?)\s*$", stripped)
            if m:
                title = m.group(1)
                continue
        para_lines.append(stripped)
    if summary is None and para_lines:
        summary = "\n".join(para_lines).strip()[:200]
    return (title, summary)


def _extract_txt(content, stem):
    """TXT：标题为文件名 stem；摘要为首段非空段落（前 200 字符）。"""
    summary = None
    para_lines = []
    for line in content.splitlines():
        stripped = line.strip()
        if not stripped:
            if para_lines:
                summary = "\n".join(para_lines).strip()[:200]
                break
            continue
        para_lines.append(stripped)
    if summary is None and para_lines:
        summary = "\n".join(para_lines).strip()[:200]
    return (stem, summary)


def _extract_csv(file_path):
    """CSV：标题为首个单元格；摘要为第二行首个单元格。"""
    try:
        with open(file_path, "r", encoding="utf-8", errors="replace", newline="") as f:
            reader = csv.reader(f)
            rows = []
            for row in reader:
                rows.append(row)
                if len(rows) >= 2:
                    break
        title = rows[0][0] if rows and rows[0] else None
        summary = rows[1][0] if len(rows) >= 2 and rows[1] else None
        return (title, summary)
    except (OSError, csv.Error):
        return (None, None)


def _extract_json(content):
    """JSON：标题为顶层 title 字段；摘要为顶层 description 字段。"""
    try:
        data = json.loads(content)
    except (json.JSONDecodeError, ValueError):
        return (None, None)
    if not isinstance(data, dict):
        return (None, None)
    title = data.get("title")
    summary = data.get("description")
    if title is not None:
        title = str(title)
    if summary is not None:
        summary = str(summary)[:200]
    return (title, summary)


# =============================================================================
# 构建前去重（--pre）
# =============================================================================

def scan_folder(folder_root):
    """递归扫描指定文件夹，返回 (rel_posix, file_path, sha256, size) 元组列表。"""
    results = []
    for root, dirs, files in os.walk(folder_root):
        root_path = Path(root)
        try:
            root_rel = root_path.relative_to(ROOT)
            root_rel_posix = to_posix(root_rel) + "/"
        except ValueError:
            root_rel_posix = ""
        # 原地修改 dirs 以阻止 os.walk 进入跳过的目录
        dirs[:] = [d for d in dirs if not should_skip_dir(d)
                   and not should_skip_path(root_rel_posix + d + "/")]
        for fname in files:
            ext = os.path.splitext(fname)[1].lower()
            if ext not in SCAN_EXTENSIONS:
                continue
            file_path = root_path / fname
            try:
                rel_path = file_path.relative_to(ROOT)
            except ValueError:
                continue
            rel_posix = to_posix(rel_path)
            if should_skip_path(rel_posix):
                continue
            try:
                size = file_path.stat().st_size
                sha = compute_sha256(file_path)
            except OSError as e:
                print(f"  [warn] cannot read {rel_posix}: {e}")
                continue
            results.append((rel_posix, file_path, sha, size))
    return results


def pre_dedup():
    """执行构建前去重并生成报告。返回 0 表示成功。"""
    print(f"[pre] start at {now_str()}")
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    # 步骤 1-2：扫描 7 个文件夹并计算 SHA-256
    all_files = []  # [(folder, rel_posix, file_path, sha, size), ...]
    for _db_name, _db_rel, folder_rel in DATABASES:
        folder_root = ROOT / folder_rel
        if not folder_root.exists():
            print(f"[pre] folder missing: {folder_rel}")
            continue
        print(f"[pre] Scanning {folder_rel}...", end=" ", flush=True)
        scanned = scan_folder(folder_root)
        folder_name = folder_rel.rstrip("/")
        for rel_posix, file_path, sha, size in scanned:
            all_files.append((folder_name, rel_posix, file_path, sha, size))
        print(f"[{len(scanned)} files]")

    total = len(all_files)
    print(f"[pre] total scanned files: {total}")

    # 步骤 3：精确重复（同文件夹内 SHA-256 相同）
    # 按 (folder, sha) 分组
    by_folder_sha = {}
    for folder, rel, fp, sha, size in all_files:
        by_folder_sha.setdefault(folder, {}).setdefault(sha, []).append((rel, size))
    exact_pairs = []
    for folder, sha_map in by_folder_sha.items():
        for sha, group in sha_map.items():
            if len(group) < 2:
                continue
            group_sorted = sorted(group, key=lambda x: x[0])
            primary_rel, primary_size = group_sorted[0]
            for dup_rel, _ in group_sorted[1:]:
                exact_pairs.append((primary_rel, dup_rel, sha, primary_size))
    print(f"[pre] exact duplicates: {len(exact_pairs)}")

    # 步骤 4：模糊重复（标题+摘要平均相似度 >= 0.85）
    # 预计算每个文件的 (folder, sha, size, title, summary, ext)
    print(f"[pre] extracting titles/summaries...", end=" ", flush=True)
    t0 = time.time()
    file_meta = {}
    for folder, rel, fp, sha, size in all_files:
        ext = os.path.splitext(rel)[1].lower()
        title, summary = extract_title_summary(fp, ext)
        file_meta[rel] = (folder, sha, size, title, summary, ext)
    print(f"[done in {time.time() - t0:.1f}s]")

    print(f"[pre] computing fuzzy duplicates...", end=" ", flush=True)
    t0 = time.time()
    fuzzy_pairs = _fuzzy_dedup(file_meta)
    print(f"[{len(fuzzy_pairs)} pairs in {time.time() - t0:.1f}s]")

    # 步骤 5：跨文件夹 SHA-256 重复
    cross_pairs = []
    sha_to_files = {}
    for folder, rel, fp, sha, size in all_files:
        sha_to_files.setdefault(sha, []).append((folder, rel))
    for sha, group in sha_to_files.items():
        if len(group) < 2:
            continue
        folders_set = set(g[0] for g in group)
        if len(folders_set) < 2:
            continue
        group_sorted = sorted(group, key=lambda x: (x[0], x[1]))
        for i in range(len(group_sorted)):
            for j in range(i + 1, len(group_sorted)):
                f1, r1 = group_sorted[i]
                f2, r2 = group_sorted[j]
                if f1 != f2:
                    cross_pairs.append((f1, r1, f2, r2, sha))
    print(f"[pre] cross-folder duplicates: {len(cross_pairs)}")

    # 步骤 6：生成报告与看板
    write_pre_report(total, exact_pairs, fuzzy_pairs, cross_pairs)
    update_dashboard_pre(total, exact_pairs, fuzzy_pairs, cross_pairs)

    print(f"[pre] report: {REPORT_PRE}")
    print(f"[pre] done at {now_str()}")
    return 0


def _fuzzy_dedup(file_meta):
    """对所有文件两两比较标题与摘要，返回模糊重复对列表。

    file_meta: {rel -> (folder, sha, size, title, summary, ext)}

    优化：
    1. 仅比较同扩展名的文件（不同格式之间模糊匹配语义不可靠）
    2. 标题长度比 < 0.74 时直接跳过（相似度必 < 0.85）
    3. 跳过标题与摘要均为空的文件
    4. 跳过 SHA-256 相同的文件（已在精确重复中记录）
    """
    fuzzy_pairs = []
    # 按扩展名分组
    by_ext = {}
    for rel, meta in file_meta.items():
        ext = meta[5]
        by_ext.setdefault(ext, []).append(rel)
    for ext, rels in by_ext.items():
        rels_sorted = sorted(rels)
        n = len(rels_sorted)
        for i in range(n):
            r1 = rels_sorted[i]
            m1 = file_meta[r1]
            t1 = m1[3] or ""
            s1 = m1[4] or ""
            if not t1 and not s1:
                continue
            len_t1 = len(t1) if t1 else 0
            for j in range(i + 1, n):
                r2 = rels_sorted[j]
                m2 = file_meta[r2]
                # 跳过精确重复
                if m1[1] == m2[1]:
                    continue
                t2 = m2[3] or ""
                s2 = m2[4] or ""
                if not t2 and not s2:
                    continue
                # 标题长度预过滤（仅当两端都有标题时）
                if t1 and t2:
                    lt1, lt2 = len_t1, len(t2)
                    if lt1 and lt2:
                        ratio = min(lt1, lt2) / max(lt1, lt2)
                        if ratio < LEN_RATIO_PREFILTER:
                            continue
                t_sim = difflib.SequenceMatcher(None, t1, t2).ratio() if (t1 and t2) else 0.0
                s_sim = difflib.SequenceMatcher(None, s1, s2).ratio() if (s1 and s2) else 0.0
                avg = (t_sim + s_sim) / 2
                if avg >= FUZZY_THRESHOLD:
                    fuzzy_pairs.append((r1, r2, t_sim, s_sim, avg))
    return fuzzy_pairs


def write_pre_report(total, exact_pairs, fuzzy_pairs, cross_pairs):
    """生成 dedup_report_pre.md。"""
    lines = []
    lines.append("# 处理前去重报告")
    lines.append("")
    lines.append(f"> 生成时间：{now_str()}")
    lines.append(f"> 扫描文件总数：{total}")
    lines.append("")
    lines.append("## 精确重复（SHA-256 相同）")
    lines.append("")
    if exact_pairs:
        lines.append("| 主记录路径 | 重复路径 | SHA-256 | 大小 |")
        lines.append("| --- | --- | --- | --- |")
        for primary, dup, sha, size in exact_pairs:
            lines.append(f"| {primary} | {dup} | {sha} | {size} |")
        lines.append("")
        lines.append(f"共发现 {len(exact_pairs)} 对精确重复")
    else:
        lines.append("（暂无精确重复记录）")
    lines.append("")
    lines.append("## 模糊重复（标题+首段相似度 ≥ 0.85）")
    lines.append("")
    if fuzzy_pairs:
        lines.append("| 主记录路径 | 重复路径 | 标题相似度 | 首段相似度 | 平均相似度 |")
        lines.append("| --- | --- | --- | --- | --- |")
        for primary, dup, t_sim, s_sim, avg in fuzzy_pairs:
            lines.append(f"| {primary} | {dup} | {t_sim:.4f} | {s_sim:.4f} | {avg:.4f} |")
        lines.append("")
        lines.append(f"共发现 {len(fuzzy_pairs)} 对模糊重复")
    else:
        lines.append("（暂无模糊重复记录）")
    lines.append("")
    lines.append("## 跨文件夹重复（不同文件夹中 SHA-256 相同）")
    lines.append("")
    if cross_pairs:
        lines.append("| 文件夹1 | 文件路径1 | 文件夹2 | 文件路径2 | SHA-256 |")
        lines.append("| --- | --- | --- | --- | --- |")
        for f1, r1, f2, r2, sha in cross_pairs:
            lines.append(f"| {f1} | {r1} | {f2} | {r2} | {sha} |")
        lines.append("")
        lines.append(f"共发现 {len(cross_pairs)} 对跨文件夹重复")
    else:
        lines.append("（暂无跨文件夹重复记录）")
    lines.append("")
    lines.append("## 汇总")
    lines.append("")
    lines.append(f"- 待入库文件总数：{total}")
    lines.append(f"- 精确重复对数：{len(exact_pairs)}")
    lines.append(f"- 模糊重复对数：{len(fuzzy_pairs)}")
    lines.append(f"- 跨文件夹重复对数：{len(cross_pairs)}")
    lines.append("")
    _write_lf(REPORT_PRE, "\n".join(lines))


def update_dashboard_pre(total, exact_pairs, fuzzy_pairs, cross_pairs):
    """更新两个看板的"处理前去重"小节。"""
    new_section = [
        "### 处理前去重",
        "",
        f"- 状态：done（{now_str()}）",
        f"- 待入库文件总数：{total}",
        f"- 精确重复对数：{len(exact_pairs)}",
        f"- 模糊重复对数：{len(fuzzy_pairs)}",
        f"- 跨文件夹重复对数：{len(cross_pairs)}",
        "- 报告文件：`script/_folder_db_logs/dedup_report_pre.md`",
    ]
    for dashboard in (DASHBOARD_1, DASHBOARD_2):
        _replace_dashboard_section(dashboard, "### 处理前去重", "### 处理后去重", new_section)


# =============================================================================
# 构建后去重（--post）
# =============================================================================

def post_dedup():
    """执行构建后去重并生成报告。返回 0 表示成功。"""
    print(f"[post] start at {now_str()}")
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    file_path_rows = []        # (db_name, dup_count, status)
    sha256_rows = []           # (db_name, dup_count, registered, unregistered, status)
    content_hash_rows = []     # (db_name, dup_count, status)
    sha256_summary = {"registered": 0, "unregistered": 0}
    content_hash_total = 0
    file_path_total = 0
    checked = 0

    for db_name, db_rel, _folder_rel in DATABASES:
        db_path = ROOT / db_rel
        if not db_path.exists():
            print(f"[post] WARNING: database missing: {db_rel}（skip）")
            file_path_rows.append((db_name, -1, "missing"))
            sha256_rows.append((db_name, -1, 0, 0, "missing"))
            content_hash_rows.append((db_name, -1, "missing"))
            continue
        checked += 1
        print(f"[post] verifying {db_name} ({db_path.name})...")
        fp_dups_count = 0
        sha_groups_count = 0
        ch_groups_count = 0
        try:
            conn = sqlite3.connect(str(db_path), timeout=60)
            conn.execute("PRAGMA foreign_keys = ON")
            cur = conn.cursor()

            # 步骤 1：file_path 唯一性
            cur.execute(
                "SELECT file_path, COUNT(*) AS cnt FROM files "
                "GROUP BY file_path HAVING cnt > 1"
            )
            fp_dups = cur.fetchall()
            fp_dups_count = len(fp_dups)
            file_path_total += fp_dups_count

            # 步骤 2：sha256 唯一性
            cur.execute(
                "SELECT sha256, COUNT(*) AS cnt FROM files "
                "GROUP BY sha256 HAVING cnt > 1"
            )
            sha_groups = cur.fetchall()
            sha_groups_count = len(sha_groups)
            registered = 0
            unregistered = 0
            for sha, _cnt in sha_groups:
                cur.execute(
                    "SELECT id, duplicate_of_id, status FROM files "
                    "WHERE sha256 = ? ORDER BY id ASC",
                    (sha,)
                )
                rows = cur.fetchall()
                if not rows:
                    continue
                primary_id = rows[0][0]
                non_primary = rows[1:]
                # 检查是否所有非主记录都已登记
                already_registered = all(r[1] is not None for r in non_primary)
                if already_registered:
                    registered += 1
                    continue
                # 补登记：将未登记的非主记录标记为 merged
                try:
                    for r in non_primary:
                        fid = r[0]
                        if r[1] is None:
                            cur.execute(
                                "UPDATE files SET duplicate_of_id = ?, "
                                "duplicate_type = 'exact', status = 'merged' "
                                "WHERE id = ? AND duplicate_of_id IS NULL",
                                (primary_id, fid)
                            )
                    # 记录日志
                    cur.execute(
                        "INSERT INTO update_log (file_id, operation, field_changed, "
                        "old_value, new_value, timestamp, operated_by, notes) "
                        "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                        (None, "merge", "sha256", None, sha, now_str(),
                         "dedup_folder_databases.py",
                         f"post-build dedup: sha256={sha}, primary_id={primary_id}")
                    )
                    conn.commit()
                    unregistered += 1
                except sqlite3.Error as e:
                    conn.rollback()
                    print(f"[post]   ERROR updating duplicates for sha256={sha}: {e}")
                    unregistered += 1
            sha256_summary["registered"] += registered
            sha256_summary["unregistered"] += unregistered

            # 步骤 3：content_hash 唯一性
            cur.execute(
                "SELECT content_hash, COUNT(*) AS cnt FROM files "
                "GROUP BY content_hash HAVING cnt > 1"
            )
            ch_groups = cur.fetchall()
            ch_groups_count = len(ch_groups)
            # 仅标记 duplicate_type='content'，不强制合并
            for ch, _cnt in ch_groups:
                try:
                    cur.execute(
                        "UPDATE files SET duplicate_type = 'content' "
                        "WHERE content_hash = ? AND duplicate_type IS NULL",
                        (ch,)
                    )
                    conn.commit()
                except sqlite3.Error as e:
                    conn.rollback()
                    print(f"[post]   ERROR marking content_hash={ch}: {e}")
            content_hash_total += ch_groups_count

            conn.close()
        except sqlite3.Error as e:
            print(f"[post]   ERROR on {db_name}: {e}")
            file_path_rows.append((db_name, -1, "error"))
            sha256_rows.append((db_name, -1, 0, 0, "error"))
            content_hash_rows.append((db_name, -1, "error"))
            continue

        fp_status = "pass" if fp_dups_count == 0 else "fail"
        sha_status = "pass" if sha_groups_count == 0 else ("fixed" if unregistered > 0 else "pass")
        ch_status = "pass" if ch_groups_count == 0 else "marked"
        file_path_rows.append((db_name, fp_dups_count, fp_status))
        sha256_rows.append((db_name, sha_groups_count, registered, unregistered, sha_status))
        content_hash_rows.append((db_name, ch_groups_count, ch_status))
        print(f"[post]   file_path={fp_dups_count}, sha256={sha_groups_count} "
              f"(reg={registered}, new={unregistered}), content_hash={ch_groups_count}")

    write_post_report(checked, file_path_rows, sha256_rows, content_hash_rows,
                      sha256_summary, content_hash_total, file_path_total)
    update_dashboard_post(checked, file_path_rows, sha256_rows, content_hash_rows,
                          sha256_summary, content_hash_total, file_path_total)

    print(f"[post] checked databases: {checked}")
    print(f"[post] file_path duplicates: {file_path_total}")
    print(f"[post] sha256 duplicates (already registered): {sha256_summary['registered']}")
    print(f"[post] sha256 duplicates (newly registered): {sha256_summary['unregistered']}")
    print(f"[post] content_hash duplicates: {content_hash_total}")
    print(f"[post] report: {REPORT_POST}")
    print(f"[post] done at {now_str()}")
    return 0


def write_post_report(checked, file_path_rows, sha256_rows, content_hash_rows,
                      sha256_summary, content_hash_total, file_path_total):
    """生成 dedup_report_post.md。"""
    lines = []
    lines.append("# 处理后去重报告")
    lines.append("")
    lines.append(f"> 生成时间：{now_str()}")
    lines.append(f"> 核验数据库数：{checked}")
    lines.append("")
    lines.append("## file_path 唯一性核验")
    lines.append("")
    if file_path_rows:
        lines.append("| 数据库 | 重复数 | 状态 |")
        lines.append("| --- | --- | --- |")
        for db, cnt, status in file_path_rows:
            lines.append(f"| {db} | {cnt} | {status} |")
    else:
        lines.append("（暂无 file_path 重复记录）")
    lines.append("")
    lines.append("## sha256 唯一性核验")
    lines.append("")
    if sha256_rows:
        lines.append("| 数据库 | 重复数 | 已登记 | 未登记 | 状态 |")
        lines.append("| --- | --- | --- | --- | --- |")
        for db, cnt, reg, unreg, status in sha256_rows:
            lines.append(f"| {db} | {cnt} | {reg} | {unreg} | {status} |")
    else:
        lines.append("（暂无 sha256 重复记录）")
    lines.append("")
    lines.append("## content_hash 唯一性核验")
    lines.append("")
    if content_hash_rows:
        lines.append("| 数据库 | 重复数 | 状态 |")
        lines.append("| --- | --- | --- |")
        for db, cnt, status in content_hash_rows:
            lines.append(f"| {db} | {cnt} | {status} |")
    else:
        lines.append("（暂无 content_hash 重复记录）")
    lines.append("")
    lines.append("## 汇总")
    lines.append("")
    lines.append(f"- 核验数据库数：{checked}")
    lines.append(f"- file_path 重复：{file_path_total}")
    lines.append(f"- sha256 重复（已登记）：{sha256_summary['registered']}")
    lines.append(f"- sha256 重复（未登记，已补登记）：{sha256_summary['unregistered']}")
    lines.append(f"- content_hash 重复：{content_hash_total}")
    lines.append("")
    _write_lf(REPORT_POST, "\n".join(lines))


def update_dashboard_post(checked, file_path_rows, sha256_rows, content_hash_rows,
                          sha256_summary, content_hash_total, file_path_total):
    """更新两个看板的"处理后去重"小节。"""
    sha_total = sha256_summary["registered"] + sha256_summary["unregistered"]
    new_section = [
        "### 处理后去重",
        "",
        f"- 状态：done（{now_str()}）",
        f"- 核验数据库数：{checked}",
        f"- file_path 重复：{file_path_total}",
        f"- sha256 重复：{sha_total}（已登记 {sha256_summary['registered']}，"
        f"补登记 {sha256_summary['unregistered']}）",
        f"- content_hash 重复：{content_hash_total}",
        "- 报告文件：`script/_folder_db_logs/dedup_report_post.md`",
    ]
    for dashboard in (DASHBOARD_1, DASHBOARD_2):
        _replace_dashboard_section(dashboard, "### 处理后去重",
                                   "## 跨库引用解析进度", new_section)


# =============================================================================
# 看板更新工具
# =============================================================================

def _replace_dashboard_section(dashboard_path, start_header, next_header, new_lines):
    """替换看板中从 start_header 到 next_header 之前的整段内容为 new_lines。

    若 next_header 未找到，则替换到文件末尾。
    """
    if not dashboard_path.exists():
        print(f"[dashboard] missing: {dashboard_path}")
        return
    try:
        with open(dashboard_path, "r", encoding="utf-8") as f:
            content = f.read()
    except OSError as e:
        print(f"[dashboard] read error: {dashboard_path}: {e}")
        return
    start_idx = content.find(start_header)
    if start_idx < 0:
        print(f"[dashboard] section not found: {start_header} in {dashboard_path}")
        return
    next_idx = content.find(next_header, start_idx)
    if next_idx < 0:
        new_content = content[:start_idx] + "\n".join(new_lines) + "\n"
    else:
        new_content = content[:start_idx] + "\n".join(new_lines) + "\n\n" + content[next_idx:]
    _write_lf(dashboard_path, new_content)
    print(f"[dashboard] updated: {dashboard_path}")


# =============================================================================
# 主入口
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="文件夹级数据库去重脚本（--pre / --post / --all）"
    )
    parser.add_argument(
        "--pre", action="store_true",
        help="构建前去重：扫描源文件、SHA-256 精确去重 + 标题/首段模糊去重 + 跨文件夹去重"
    )
    parser.add_argument(
        "--post", action="store_true",
        help="构建后去重：核验 files 表 file_path/sha256/content_hash 唯一性"
    )
    parser.add_argument(
        "--all", action="store_true",
        help="同时执行 --pre 与 --post"
    )
    args = parser.parse_args()

    if args.all:
        args.pre = True
        args.post = True
    if not (args.pre or args.post):
        parser.print_help()
        return 1

    rc = 0
    try:
        if args.pre:
            rc = pre_dedup() or rc
        if args.post:
            rc = post_dedup() or rc
    except Exception as e:
        print(f"[FATAL] {type(e).__name__}: {e}")
        return 1
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
