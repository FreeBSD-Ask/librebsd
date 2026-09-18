#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
auto_ingest_new_pdfs.py
=======================
自动检测新增 PDF/EPUB/CAJ 文献并执行完整入库管线。

入库管线七步：
1. 去重检查（SHA-256 精确 + 标题/作者/年份模糊）
2. 元数据采集（YAML frontmatter → 文件名模式 → PDF metadata）
3. 数据库录入（references + summaries 表）
4. 章节匹配（关键词相似度，写入 chapter_matches 表）
5. 综述追加（chapter_reviews.revised_review_text 追加段落，300-5000 字约束）
6. CSV 更新（_匹配映射表.csv 追加行）
7. 参考文献总目著录（按类别追加到对应 .md 文件）

用法：
    python script/auto_ingest_new_pdfs.py                    # 检测并入库所有新增
    python script/auto_ingest_new_pdfs.py --dry-run          # 仅检测不执行
    python script/auto_ingest_new_pdfs.py --file <路径>      # 指定单个文件入库
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sqlite3
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# =============================================================================
# 常量
# =============================================================================

BASE = Path(r"d:\librebsd")
DB_PATH = BASE / "04-现代研究文献" / "05-参考文献全文数据库" / "references_fulltext.db"
DOWNLOAD_DIR = BASE / "04-现代研究文献" / "03-文献下载"
CSV_PATH = DOWNLOAD_DIR / "04-文献摘要" / "_匹配映射表.csv"
SUMMARY_BASE = DOWNLOAD_DIR / "04-文献摘要"
BIB_DIR = BASE / "04-现代研究文献" / "01-参考文献总目"
OUTLINE_DIR = BASE / "05-卷册大纲"
LOG_DIR = BASE / "script" / "_auto_ingest_logs"
LOG_FILE = LOG_DIR / "ingest_log.jsonl"
DASHBOARD_FILE = LOG_DIR / "dashboard.md"

SCAN_SUBDIRS = ["01-pdf", "02-epub", "04-caj"]
SKIP_DIRS = {"10-无关文件"}
VALID_EXTS = {".pdf", ".epub", ".caj"}

# 目录 → 参考文献总目分类文件映射
BIB_CATEGORY_MAP = {
    "01-pdf/01-BSD核心书籍": "bsd相关经典著作.md",
    "01-pdf/02-UNIX经典著作": "unix与bsd早期技术文献.md",
    "01-pdf/03-学术论文": "bsd学术论文与学位论文.md",
    "01-pdf/04-学位论文": "中文学位论文.md",
    "01-pdf/05-官方文档": "操作系统官方文档.md",
    "01-pdf/06-安全史料": "密码学与安全史料.md",
    "01-pdf/07-法律与合规": "法律判例与法律研究.md",
    "02-epub": "bsd相关经典著作.md",
    "04-caj": "中文学位论文.md",
}
DEFAULT_BIB_FILE = "bsd学术论文与学位论文.md"

# =============================================================================
# 日志
# =============================================================================

def ensure_log_dir():
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    if not LOG_FILE.exists():
        LOG_FILE.touch()
    if not DASHBOARD_FILE.exists():
        DASHBOARD_FILE.write_text("# 新增文献自动入库看板\n\n（尚未运行）\n", encoding="utf-8")

def log_entry(file_path: str, status: str, reference_id: int = 0,
              chapter_matched: str = "", error: str = ""):
    """写入一条日志"""
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "file_path": file_path,
        "status": status,
        "reference_id": reference_id,
        "chapter_matched": chapter_matched,
        "error": error,
    }
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

def update_dashboard(stats: Dict[str, int]):
    """更新看板"""
    content = f"""# 新增文献自动入库看板

## 本次运行统计

| 指标 | 数值 |
| --- | --- |
| 本次检测时间 | {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} |
| 待入库文件数 | {stats.get("pending", 0)} |
| 成功入库数 | {stats.get("success", 0)} |
| 跳过（重复）数 | {stats.get("skipped", 0)} |
| 失败数 | {stats.get("failed", 0)} |
| 需人工确认数 | {stats.get("manual", 0)} |
"""
    DASHBOARD_FILE.write_text(content, encoding="utf-8")

# =============================================================================
# 文件扫描
# =============================================================================

def scan_files() -> List[Path]:
    """扫描所有 PDF/EPUB/CAJ 文件"""
    files = []
    for subdir in SCAN_SUBDIRS:
        scan_path = DOWNLOAD_DIR / subdir
        if not scan_path.exists():
            continue
        for f in scan_path.rglob("*"):
            if not f.is_file():
                continue
            # 跳过无关目录
            parts = f.parts
            if any(skip in parts for skip in SKIP_DIRS):
                continue
            if f.suffix.lower() in VALID_EXTS:
                files.append(f)
    return files

def get_existing_paths(conn: sqlite3.Connection) -> set:
    """获取数据库中已有的文件路径"""
    cur = conn.cursor()
    cur.execute('SELECT file_path FROM "references"')
    return {row[0] for row in cur.fetchall()}

def find_new_files(conn: sqlite3.Connection, all_files: List[Path]) -> List[Path]:
    """找出未入库的文件"""
    existing = get_existing_paths(conn)
    new_files = []
    for f in all_files:
        rel_path = str(f.relative_to(BASE)).replace("\\", "/")
        if rel_path not in existing:
            new_files.append(f)
    return new_files

# =============================================================================
# 去重检查
# =============================================================================

def compute_sha256(file_path: Path) -> str:
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def check_duplicate(conn: sqlite3.Connection, file_path: Path,
                    title: str, author: str, year: str) -> Tuple[bool, str]:
    """检查是否重复，返回 (是否重复, 重复类型)"""
    sha = compute_sha256(file_path)
    cur = conn.cursor()

    # SHA-256 精确去重
    cur.execute('SELECT id FROM "references" WHERE sha256 = ?', (sha,))
    if cur.fetchone():
        return True, "exact"

    # 标题+作者+年份模糊去重
    if title and author:
        cur.execute(
            'SELECT id FROM "references" WHERE LOWER(title) = LOWER(?) AND LOWER(author) = LOWER(?) AND year = ?',
            (title, author, int(year) if year.isdigit() else 0)
        )
        if cur.fetchone():
            return True, "fuzzy"

    return False, ""

def record_duplicate(conn: sqlite3.Connection, file_path: Path,
                     dup_type: str, title: str, author: str, year: str, sha: str):
    """记录重复到 reference_duplicates 表"""
    cur = conn.cursor()
    # 找到主记录 ID
    if dup_type == "exact":
        cur.execute('SELECT id FROM "references" WHERE sha256 = ?', (sha,))
    else:
        cur.execute(
            'SELECT id FROM "references" WHERE LOWER(title) = LOWER(?) AND LOWER(author) = LOWER(?) AND year = ?',
            (title, author, int(year) if year.isdigit() else 0)
        )
    row = cur.fetchone()
    primary_id = row[0] if row else 0

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur.execute("""
        INSERT OR IGNORE INTO reference_duplicates (primary_reference_id, duplicate_reference_id,
            duplicate_type, match_score, match_fields, merged_at, merged_by, merge_notes)
        VALUES (?, 0, ?, 1.0, ?, ?, 'auto_ingest', ?)
    """, (
        primary_id, dup_type,
        f"file_path={file_path}",
        now,
        f"自动检测到{dup_type}重复: title={title}, author={author}, year={year}",
    ))
    conn.commit()

# =============================================================================
# 元数据采集
# =============================================================================

def parse_filename(filename: str) -> Dict[str, str]:
    """从文件名提取作者/年份/标题"""
    stem = Path(filename).stem
    result = {"author": "", "year": "", "title": "", "lang": ""}

    # 模式1: YYYY_作者_标题_lang
    m = re.match(r"^(\d{4})_([^_]+)_(.+?)_(zh|en|other)$", stem)
    if m:
        result["year"] = m.group(1)
        result["author"] = m.group(2)
        result["title"] = m.group(3)
        result["lang"] = m.group(4)
        return result

    # 模式2: YYYY_作者_标题
    m = re.match(r"^(\d{4})_([^_]+)_(.+)$", stem)
    if m:
        result["year"] = m.group(1)
        result["author"] = m.group(2)
        result["title"] = m.group(3)
        return result

    # 模式3: 未知年份_未知作者_标题
    m = re.match(r"^未知年份_未知作者_(.+)$", stem)
    if m:
        result["title"] = m.group(1)
        return result

    # 兜底
    result["title"] = stem
    return result

def read_summary_md(file_path: Path) -> Dict[str, str]:
    """从 .md 摘要文件读取 YAML frontmatter"""
    rel_path = file_path.relative_to(DOWNLOAD_DIR)
    summary_path = SUMMARY_BASE / rel_path
    summary_path = summary_path.with_suffix(".md")

    result = {"author": "", "year": "", "page_count": "", "summary": "",
              "topic_keywords": "", "important_excerpts": "", "summary_md_path": ""}

    if not summary_path.exists():
        return result

    result["summary_md_path"] = str(summary_path.relative_to(BASE)).replace("\\", "/")
    content = summary_path.read_text(encoding="utf-8")

    # 提取 YAML frontmatter
    m = re.search(r"^---\n(.*?)\n---", content, re.DOTALL)
    if m:
        yaml_text = m.group(1)
        for line in yaml_text.split("\n"):
            if ":" in line:
                key, _, val = line.partition(":")
                key = key.strip()
                val = val.strip()
                if key == "作者":
                    result["author"] = val
                elif key == "年份":
                    result["year"] = val
                elif key == "页数":
                    result["page_count"] = val

    # 提取 ## 摘要 段落
    m = re.search(r"## 摘要\s*\n+(.+?)(?:\n## |\Z)", content, re.DOTALL)
    if m:
        result["summary"] = m.group(1).strip()

    # 提取 ## 议题关键词
    m = re.search(r"## 议题关键词\s*\n+(.+?)(?:\n## |\Z)", content, re.DOTALL)
    if m:
        result["topic_keywords"] = m.group(1).strip()

    # 提取 ## 重要段落摘录
    m = re.search(r"## 重要段落摘录\s*\n+(.+?)(?:\n## |\Z)", content, re.DOTALL)
    if m:
        result["important_excerpts"] = m.group(1).strip()

    return result

def try_pdf_metadata(file_path: Path) -> Dict[str, str]:
    """尝试从 PDF 读取元数据"""
    result = {"author": "", "year": "", "page_count": ""}
    try:
        import fitz  # PyMuPDF
        doc = fitz.open(str(file_path))
        result["page_count"] = str(doc.page_count)
        meta = doc.metadata
        if meta:
            if meta.get("author"):
                result["author"] = meta["author"]
            if meta.get("creationDate"):
                # 格式 D:YYYYMMDD...
                m = re.match(r"D:(\d{4})", meta["creationDate"])
                if m:
                    result["year"] = m.group(1)
        doc.close()
    except Exception:
        pass
    return result

def collect_metadata(file_path: Path) -> Dict[str, Any]:
    """三级回退采集元数据"""
    # 相对路径
    rel_path = str(file_path.relative_to(BASE)).replace("\\", "/")

    # 第一级：.md 摘要文件
    md_meta = read_summary_md(file_path)

    # 第二级：文件名
    fn_meta = parse_filename(file_path.name)

    # 第三级：PDF metadata
    pdf_meta = {}
    if file_path.suffix.lower() == ".pdf":
        pdf_meta = try_pdf_metadata(file_path)

    # 合并：优先级 md > filename > pdf
    author = md_meta["author"] or fn_meta["author"] or pdf_meta.get("author", "") or "未知"
    year = md_meta["year"] or fn_meta["year"] or pdf_meta.get("year", "") or "不详"
    page_count = md_meta["page_count"] or pdf_meta.get("page_count", "0")
    title = fn_meta["title"] or file_path.stem

    # 语言推断
    lang = "other"
    if fn_meta.get("lang"):
        lang = fn_meta["lang"]
    elif "_zh" in file_path.name:
        lang = "zh"
    elif "_en" in file_path.name:
        lang = "en"
    elif re.search(r"[\u4e00-\u9fff]", title):
        lang = "zh"
    else:
        lang = "en"

    return {
        "file_path": rel_path,
        "filename": file_path.name,
        "format": file_path.suffix.lstrip(".").lower(),
        "title": title,
        "author": author,
        "year": int(year) if year.isdigit() else 0,
        "year_str": year,
        "page_count": int(page_count) if str(page_count).isdigit() else 0,
        "language": lang,
        "file_size": file_path.stat().st_size,
        "summary": md_meta["summary"],
        "topic_keywords": md_meta["topic_keywords"],
        "important_excerpts": md_meta["important_excerpts"],
        "summary_md_path": md_meta["summary_md_path"],
    }

# =============================================================================
# 数据库录入
# =============================================================================

def insert_reference(conn: sqlite3.Connection, meta: Dict[str, Any]) -> int:
    """写入 references 表，返回新 id"""
    cur = conn.cursor()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    sha = compute_sha256(BASE / meta["file_path"])

    # GB/T 7714-2015 著录
    author_str = meta["author"]
    title_str = meta["title"]
    year_str = str(meta["year"]) if meta["year"] else meta["year_str"]
    bib_entry = f"{author_str}. {title_str}[M]. {year_str}."

    cur.execute('SELECT MAX(id) FROM "references"')
    max_id = cur.fetchone()[0] or 0
    new_id = max_id + 1

    cur.execute("""
        INSERT INTO "references" (
            id, file_path, filename, format, title, author, year, publisher,
            isbn_doi, language, page_count, file_size, sha256,
            bibliography_entry, source_url, download_date, ocr_status, status,
            summary_md_path, created_at, updated_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, '', '', ?, ?, ?, ?, ?, '', ?, '', 'pending', ?, ?, ?)
    """, (
        new_id, meta["file_path"], meta["filename"], meta["format"],
        meta["title"], meta["author"], meta["year"], meta["language"],
        meta["page_count"], meta["file_size"], sha,
        bib_entry, now, meta["summary_md_path"], now, now,
    ))

    # 写入 summaries 表
    cur.execute("SELECT MAX(id) FROM summaries")
    max_sum_id = cur.fetchone()[0] or 0
    cur.execute("""
        INSERT INTO summaries (id, reference_id, summary, topic_keywords,
            important_excerpts, processing_status, processed_at)
        VALUES (?, ?, ?, ?, ?, 'success', ?)
    """, (
        max_sum_id + 1, new_id, meta["summary"],
        meta["topic_keywords"], meta["important_excerpts"], now,
    ))

    conn.commit()
    return new_id

# =============================================================================
# 章节匹配
# =============================================================================

def load_chapter_titles() -> List[Dict[str, Any]]:
    """加载全部章节标题"""
    chapters = []
    for vol_dir in sorted(OUTLINE_DIR.iterdir()):
        if not vol_dir.is_dir() or not vol_dir.name.startswith("第"):
            continue
        # 提取卷号
        vm = re.match(r"^第(\d+)卷", vol_dir.name)
        if not vm:
            continue
        vol_num = int(vm.group(1))
        for ch_dir in sorted(vol_dir.iterdir()):
            if not ch_dir.is_dir() or not ch_dir.name.startswith("第"):
                continue
            m = re.match(r"^第(\d+)[A-Z]*章-(.+)", ch_dir.name)
            if not m:
                continue
            ch_num = int(m.group(1))
            ch_slug = m.group(2)
            chapters.append({
                "vol": vol_num,
                "ch_num": ch_num,
                "ch_slug": ch_slug,
                "dir_name": ch_dir.name,
                "path": ch_dir,
            })
    return chapters

def match_chapter(meta: Dict[str, Any], chapters: List[Dict]) -> Dict[str, Any]:
    """基于关键词相似度匹配章节"""
    # 提取文件名和摘要的关键词
    keywords = set()
    title_lower = meta["title"].lower()
    for part in re.split(r"[_\-\s]+", title_lower):
        if len(part) >= 4:
            keywords.add(part)
    if meta["topic_keywords"]:
        for kw in re.split(r"[，,、\s]+", meta["topic_keywords"].lower()):
            if len(kw) >= 3:
                keywords.add(kw)

    if not keywords:
        return {"vol": 0, "ch_num": 0, "confidence": 0.0, "reasoning": "无法提取关键词"}

    # 与章节标题比对
    best_match = None
    best_score = 0
    for ch in chapters:
        slug_lower = ch["ch_slug"].lower()
        score = 0
        for kw in keywords:
            if kw in slug_lower:
                score += 1
        if score > best_score:
            best_score = score
            best_match = ch

    if best_match and best_score >= 2:
        confidence = min(0.95, 0.5 + best_score * 0.15)
    elif best_match and best_score >= 1:
        confidence = 0.4
    else:
        confidence = 0.1

    reasoning = f"关键词重合 {best_score} 项（{', '.join(list(keywords)[:5])}）" if best_match else "无关键词重合"

    if best_match:
        return {
            "vol": best_match["vol"],
            "ch_num": best_match["ch_num"],
            "confidence": confidence,
            "reasoning": reasoning,
        }
    return {"vol": 0, "ch_num": 0, "confidence": 0.0, "reasoning": "无匹配"}

def insert_chapter_match(conn: sqlite3.Connection, ref_id: int, match: Dict[str, Any]):
    """写入 chapter_matches 表"""
    cur = conn.cursor()
    cur.execute("SELECT MAX(id) FROM chapter_matches")
    max_id = cur.fetchone()[0] or 0
    cur.execute("""
        INSERT INTO chapter_matches (id, reference_id, primary_volume, primary_chapter,
            secondary_chapters, match_reasoning, match_confidence, match_source)
        VALUES (?, ?, ?, ?, '', ?, ?, 'auto')
    """, (
        max_id + 1, ref_id, match["vol"], str(match["ch_num"]),
        match["reasoning"], match["confidence"],
    ))
    conn.commit()

# =============================================================================
# 综述追加
# =============================================================================

def find_chapter_review_id(conn: sqlite3.Connection, ch_num: int) -> Optional[int]:
    """找到章节对应的 chapter_reviews 记录 ID"""
    cur = conn.cursor()
    # chapter 字段格式: "01B", "03", "04A", "158B" 等
    # 先尝试精确匹配
    for pattern in [f"{ch_num:02d}%", f"{ch_num}%"]:
        cur.execute(
            "SELECT id FROM chapter_reviews WHERE chapter LIKE ?",
            (pattern,)
        )
        row = cur.fetchone()
        if row:
            return row[0]
    return None

def append_review(conn: sqlite3.Connection, review_id: int, ref_id: int,
                  meta: Dict[str, Any]) -> Tuple[bool, str]:
    """在综述末尾追加新文献段落，返回 (是否成功, 消息)"""
    cur = conn.cursor()
    cur.execute("SELECT revised_review_text FROM chapter_reviews WHERE id = ?", (review_id,))
    row = cur.fetchone()
    if not row:
        return False, f"chapter_reviews id={review_id} 不存在"

    old_text = row[0] or ""
    author = meta["author"]
    year_str = str(meta["year"]) if meta["year"] else meta["year_str"]
    title = meta["title"]

    # 构建追加段落
    addition = f"\n\n此外，本次自动入库新增文献 {author} 的《{title}》（{year_str}），与本章主题相关。"

    new_text = old_text + addition

    # 字数检查
    cn = len(re.findall(r"[\u4e00-\u9fff]", new_text))
    en = len(re.findall(r"[a-zA-Z]+", new_text))
    wc = cn + en

    if wc > 5000:
        return False, f"追加后字数 {wc} 超过 5000 上限，需人工精简"

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur.execute("""
        UPDATE chapter_reviews
        SET revised_review_text = ?, revised_word_count = ?,
            revised_at = ?, revised_by = 'auto_ingest',
            revision_status = 'revised'
        WHERE id = ?
    """, (new_text, wc, now, review_id))
    conn.commit()
    return True, f"追加成功 ({len(old_text)} -> {len(new_text)} 字符, {wc} 字)"

# =============================================================================
# CSV 更新
# =============================================================================

def append_csv(meta: Dict[str, Any], match: Dict[str, Any]):
    """向 _匹配映射表.csv 追加行"""
    fieldnames = ["文件路径", "作者", "年份", "主匹配卷号", "主匹配章号", "副匹配章号", "匹配依据"]
    row = {
        "文件路径": meta["file_path"],
        "作者": meta["author"],
        "年份": meta["year_str"],
        "主匹配卷号": str(match["vol"]) if match["vol"] else "",
        "主匹配章号": str(match["ch_num"]) if match["ch_num"] else "",
        "副匹配章号": "",
        "匹配依据": match["reasoning"],
    }

    # 读取现有
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        existing = list(reader)

    # 检查是否已存在
    for r in existing:
        if r["文件路径"] == row["文件路径"]:
            return  # 已存在

    existing.append(row)
    with open(CSV_PATH, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(existing)

# =============================================================================
# 参考文献总目著录
# =============================================================================

def get_bib_file(file_path: Path) -> str:
    """根据文件路径确定参考文献总目分类文件"""
    rel = file_path.relative_to(DOWNLOAD_DIR)
    rel_str = str(rel).replace("\\", "/")
    for prefix, bib_file in BIB_CATEGORY_MAP.items():
        if rel_str.startswith(prefix):
            return bib_file
    return DEFAULT_BIB_FILE

def append_bibliography(meta: Dict[str, Any], bib_file: str):
    """追加 GB/T 7714-2015 著录到参考文献总目"""
    bib_path = BIB_DIR / bib_file
    if not bib_path.exists():
        bib_path = BIB_DIR / DEFAULT_BIB_FILE

    author = meta["author"]
    title = meta["title"]
    year_str = str(meta["year"]) if meta["year"] else meta["year_str"]
    entry = f"\n{author}. {title}[M]. {year_str}.\n"

    content = bib_path.read_text(encoding="utf-8")
    if meta["file_path"] not in content and title not in content:
        content = content.rstrip() + "\n" + entry
        bib_path.write_text(content, encoding="utf-8")

# =============================================================================
# 主流程
# =============================================================================

def process_file(conn: sqlite3.Connection, file_path: Path,
                 chapters: List[Dict], dry_run: bool = False) -> str:
    """处理单个文件，返回状态"""
    try:
        # 1. 元数据采集
        meta = collect_metadata(file_path)

        # 2. 去重检查
        is_dup, dup_type = check_duplicate(
            conn, file_path, meta["title"], meta["author"], meta["year_str"]
        )
        if is_dup:
            if not dry_run:
                sha = compute_sha256(file_path)
                record_duplicate(conn, file_path, dup_type,
                                 meta["title"], meta["author"], meta["year_str"], sha)
            log_entry(meta["file_path"], "skipped", 0, "", f"{dup_type} duplicate")
            return "skipped"

        # 3. 章节匹配
        match = match_chapter(meta, chapters)

        if dry_run:
            manual = " (需人工确认)" if match["confidence"] < 0.5 else ""
            log_entry(meta["file_path"], "dry-run", 0,
                      str(match["ch_num"]), f"confidence={match['confidence']:.2f}{manual}")
            return "manual" if match["confidence"] < 0.5 else "success"

        # 4. 数据库录入
        ref_id = insert_reference(conn, meta)

        # 5. 章节匹配入库
        insert_chapter_match(conn, ref_id, match)

        # 6. 综述追加
        review_msg = ""
        if match["ch_num"] > 0 and match["confidence"] >= 0.5:
            review_id = find_chapter_review_id(conn, match["ch_num"])
            if review_id:
                ok, review_msg = append_review(conn, review_id, ref_id, meta)
            else:
                review_msg = f"章{match['ch_num']} 无 chapter_reviews 记录"

        # 7. CSV 更新
        append_csv(meta, match)

        # 8. 参考文献总目著录
        bib_file = get_bib_file(file_path)
        append_bibliography(meta, bib_file)

        status = "success" if match["confidence"] >= 0.5 else "manual"
        log_entry(meta["file_path"], status, ref_id,
                  str(match["ch_num"]), review_msg)
        return status

    except Exception as e:
        log_entry(str(file_path), "failed", 0, "", str(e))
        return "failed"

def main() -> int:
    parser = argparse.ArgumentParser(
        description="自动检测新增 PDF/EPUB/CAJ 文献并入库"
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="仅检测不执行入库")
    parser.add_argument("--file", metavar="PATH",
                        help="指定单个文件入库")
    args = parser.parse_args()

    ensure_log_dir()

    # 连接数据库
    conn = sqlite3.connect(str(DB_PATH))

    # 加载章节标题
    chapters = load_chapter_titles()
    print(f"加载 {len(chapters)} 个章节")

    if args.file:
        # 单文件模式
        file_path = Path(args.file)
        if not file_path.is_absolute():
            file_path = BASE / args.file
        if not file_path.exists():
            print(f"文件不存在: {file_path}")
            return 1
        files = [file_path]
    else:
        # 全量扫描
        all_files = scan_files()
        print(f"扫描到 {len(all_files)} 个文件")
        files = find_new_files(conn, all_files)

    print(f"待入库: {len(files)} 个文件")

    if not files:
        print("无新增文件，全部已入库。")
        update_dashboard({"pending": 0, "success": 0, "skipped": 0,
                          "failed": 0, "manual": 0})
        conn.close()
        return 0

    # 逐个处理
    stats = {"pending": len(files), "success": 0, "skipped": 0,
             "failed": 0, "manual": 0}
    for i, f in enumerate(files, 1):
        print(f"[{i}/{len(files)}] {f.name}")
        status = process_file(conn, f, chapters, dry_run=args.dry_run)
        stats[status] = stats.get(status, 0) + 1

    update_dashboard(stats)
    print(f"\n完成: 成功 {stats['success']}, 跳过 {stats['skipped']}, "
          f"失败 {stats['failed']}, 需人工 {stats['manual']}")

    conn.close()
    return 0

if __name__ == "__main__":
    sys.exit(main())
