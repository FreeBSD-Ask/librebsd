#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_folder_databases.py — 文件夹级数据库构建脚本

将 7 个一级文件夹中的文本类文件（.md/.txt/.csv/.json）转换为 SQLite 数据库，
每个数据库包含 5 张通用表（files/blocks/blocks_fts/cross_references/update_log）
及若干文件夹专属扩展表，并提供 FTS5 全文检索。

7 个文件夹级数据库映射：
  1. sacred_sources.db       ← 02-sacred源材料/
  2. original_sources.db     ← 03-原始史料库/（跳过 git 仓库与 .db）
  3. research_notes.db       ← 04-现代研究文献/（跳过二进制与既有数据库子目录）
  4. fact_checks.db          ← 07-事实核查记录/
  5. review_reports.db       ← 08-核查报告与多轮复核/
  6. cross_indexes.db        ← 10-交叉索引/
  7. metadata_interfaces.db  ← 11-元数据接口/（跳过 09-文件夹数据库索引/）

5 种运行模式：
  --folder <name>    扫描单个文件夹并构建其数据库
  --all              按顺序构建全部 7 个数据库
  --rebuild <name>   删除已有数据库文件并从零重建（保留历史日志）
  --add-file <path>  将单个文件增量入库（含 SHA-256 去重检查）
  --update-file <path> 更新已有文件（mtime 变化时级联刷新）

编码：UTF-8 无 BOM，LF 换行
依赖：仅 Python 3.8+ 标准库（sqlite3, hashlib, json, csv, pathlib, re, argparse, os, time, datetime）
规则引用：00-编纂规则与格式规范/01-规则/脚本与命令/folder_db_common_schema.sql
"""

import argparse
import csv
import datetime
import hashlib
import json
import os
import re
import sqlite3
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


# =============================================================================
# 常量与配置
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_SQL_PATH = (
    PROJECT_ROOT
    / "00-编纂规则与格式规范"
    / "01-规则"
    / "脚本与命令"
    / "folder_db_common_schema.sql"
)
LOG_DIR = PROJECT_ROOT / "script" / "_folder_db_logs"
INDEX_DIR = PROJECT_ROOT / "11-元数据接口" / "09-文件夹数据库索引"

# 7 个文件夹级数据库配置
FOLDER_DB_MAP: Dict[str, Dict[str, Any]] = {
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
            "03-文献下载/01-pdf",
            "03-文献下载/02-epub",
            "03-文献下载/04-caj",
            "03-文献下载/05-书籍/01-pdf",
            "03-文献下载/05-书籍/02-epub",
            "03-文献下载/06-论文/01-pdf",
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
    "sacred_sources",
    "original_sources",
    "research_notes",
    "fact_checks",
    "review_reports",
    "cross_indexes",
    "metadata_interfaces",
]

SUPPORTED_EXTENSIONS = {".md", ".txt", ".csv", ".json"}

# 整个目录跳过（不作为内容文件夹）
SKIP_TOP_FOLDERS = {
    "script",
    "00-编纂规则与格式规范",
    "01-项目管理",
    "05-卷册大纲",
    # "06-正式书稿" 已随 2026-08-04 禁止编纂正文决策移除，无需再跳过
    "09-硬件与物质文化史料",  # 已在 03 下但通常含二进制
}

SCHEMA_VERSION = "1.0"


# =============================================================================
# 工具函数
# =============================================================================


def now_iso() -> str:
    """返回当前时间的 ISO 8601 字符串。"""
    return datetime.datetime.now().isoformat(timespec="seconds")


def compute_sha256(path: Path) -> str:
    """分块计算文件 SHA-256（64KB 块）。"""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            chunk = f.read(65536)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def compute_sha256_bytes(data: bytes) -> str:
    """计算字节串的 SHA-256。"""
    return hashlib.sha256(data).hexdigest()


def slugify(text: str) -> str:
    """将标题文本转为 anchor slug（小写、空格转连字符、去特殊字符）。"""
    s = text.lower().strip()
    s = re.sub(r"\s+", "-", s)
    # 保留字母数字、连字符、下划线、CJK 字符
    s = re.sub(r"[^\w\u4e00-\u9fff\-]", "", s, flags=re.UNICODE)
    s = re.sub(r"-+", "-", s).strip("-")
    return s


def normalize_rel_path(path: Path) -> str:
    """将路径转为相对于项目根的正斜杠字符串。"""
    try:
        rel = path.relative_to(PROJECT_ROOT)
    except ValueError:
        rel = path
    return rel.as_posix()


def detect_line_ending(raw: bytes) -> str:
    """检测原始字节的换行符类型。"""
    if b"\r\n" in raw:
        return "crlf"
    return "lf"


def detect_bom(raw: bytes) -> bool:
    """检测是否存在 UTF-8 BOM。"""
    return raw[:3] == b"\xef\xbb\xbf"


def read_file_text(path: Path) -> Tuple[str, bytes, bool, str]:
    """
    读取文件文本。
    返回 (text, raw_bytes, has_bom, line_ending)。
    始终以 utf-8 解码；存在 BOM 时剥离并报告；解码失败时用 errors='replace'。
    """
    raw = path.read_bytes()
    has_bom = detect_bom(raw)
    if has_bom:
        decode_bytes = raw[3:]
    else:
        decode_bytes = raw
    line_ending = detect_line_ending(raw)
    try:
        text = decode_bytes.decode("utf-8")
    except UnicodeDecodeError:
        text = decode_bytes.decode("utf-8", errors="replace")
    return text, raw, has_bom, line_ending


def file_mtime_iso(path: Path) -> str:
    """返回文件 mtime 的 ISO 8601 字符串。"""
    ts = path.stat().st_mtime
    return datetime.datetime.fromtimestamp(ts).isoformat(timespec="seconds")


# =============================================================================
# 文件扫描
# =============================================================================


def should_skip_path(rel_path: str, db_config: Dict[str, Any]) -> Optional[str]:
    """
    判断相对路径是否应跳过。
    返回跳过原因字符串；不跳过则返回 None。
    """
    parts = rel_path.split("/")
    if len(parts) == 0:
        return None

    # 跳过 .git 目录
    if ".git" in parts:
        return "git_repo"

    # 跳过顶级忽略目录
    if parts[0] in SKIP_TOP_FOLDERS:
        return "skip_top_folder"

    # 检查跳过子目录
    folder = db_config["folder"]
    for skip_sub in db_config["skip_subfolders"]:
        skip_full = folder + "/" + skip_sub
        if rel_path.startswith(skip_full + "/") or rel_path == skip_full:
            return "skip_subfolder"

    return None


def scan_folder(db_name: str) -> List[Path]:
    """
    递归扫描文件夹，返回支持扩展名的文件列表。
    跳过 git 仓库、.db 文件、跳过子目录。
    """
    db_config = FOLDER_DB_MAP[db_name]
    folder_path = PROJECT_ROOT / db_config["folder"]
    if not folder_path.exists():
        return []

    results: List[Path] = []
    for root, dirs, files in os.walk(folder_path):
        root_path = Path(root)
        rel_root = normalize_rel_path(root_path)

        # 过滤目录（原地修改 dirs 以影响 os.walk 递归）
        filtered_dirs = []
        for d in dirs:
            full_d = root_path / d
            rel_d = normalize_rel_path(full_d)
            # 跳过 .git
            if d == ".git":
                continue
            skip_reason = should_skip_path(rel_d, db_config)
            if skip_reason:
                continue
            filtered_dirs.append(d)
        dirs[:] = filtered_dirs

        for fname in files:
            full_f = root_path / fname
            rel_f = normalize_rel_path(full_f)

            # 跳过 .db 文件
            if db_config["skip_db_files"] and fname.endswith(".db"):
                continue
            # 跳过 .bak 文件
            if fname.endswith(".bak"):
                continue
            # 仅支持指定扩展名
            ext = full_f.suffix.lower()
            if ext not in SUPPORTED_EXTENSIONS:
                continue

            results.append(full_f)

    results.sort()
    return results


# =============================================================================
# 元数据提取
# =============================================================================


def extract_yaml_frontmatter(content: str) -> Optional[str]:
    """提取 Markdown 文件开头的 YAML frontmatter（--- 之间的内容）。"""
    if not content.startswith("---"):
        # 允许开头有 BOM 后再是 ---
        stripped = content.lstrip("\ufeff").lstrip()
        if not stripped.startswith("---"):
            return None
        content = stripped
    lines = content.split("\n")
    if not lines or lines[0].strip() != "---":
        return None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[1:i])
    return None


def strip_frontmatter(content: str) -> str:
    """剥离 frontmatter 后返回正文。"""
    stripped = content.lstrip("\ufeff").lstrip()
    if not stripped.startswith("---"):
        return content
    lines = content.split("\n")
    if not lines or lines[0].strip() != "---":
        return content
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[i + 1:])
    return content


def extract_title_summary(
    content: str, ext: str, filename_stem: str
) -> Tuple[Optional[str], Optional[str], Optional[str]]:
    """
    提取 title / summary / frontmatter。
    返回 (title, summary, frontmatter)。
    """
    title: Optional[str] = None
    summary: Optional[str] = None
    frontmatter: Optional[str] = None

    if ext == "md":
        frontmatter = extract_yaml_frontmatter(content)
        body = strip_frontmatter(content)
        lines = body.split("\n")

        # 标题：第一个 # 标题
        for line in lines:
            m = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
            if m:
                title = m.group(2).strip()
                break

        # 摘要：第一个非空非标题非列表非引用非表格的段落
        in_code = False
        para_lines: List[str] = []
        for line in lines:
            ls = line.lstrip()
            if ls.startswith("```") or ls.startswith("~~~"):
                in_code = not in_code
                continue
            if in_code:
                continue
            if not line.strip():
                if para_lines:
                    break
                continue
            if line.startswith("#"):
                continue
            if line.startswith(">"):
                continue
            if re.match(r"^\s*[-*+]\s", line) or re.match(r"^\s*\d+\.\s", line):
                continue
            if "|" in line and line.strip().startswith("|"):
                continue
            para_lines.append(line.strip())
        if para_lines:
            summary = " ".join(para_lines)[:200]

    elif ext == "csv":
        try:
            reader = csv.reader(content.splitlines())
            first_row = next(reader, None)
            if first_row and first_row[0]:
                title = first_row[0]
            second_row = next(reader, None)
            if second_row and second_row[0]:
                summary = second_row[0][:200]
        except Exception:
            pass

    elif ext == "json":
        try:
            data = json.loads(content)
            if isinstance(data, dict):
                title = data.get("title") or data.get("name")
                summary = data.get("description") or data.get("summary")
            elif isinstance(data, list) and data and isinstance(data[0], dict):
                title = data[0].get("title") or data[0].get("name")
                summary = data[0].get("description")
        except Exception:
            pass

    elif ext == "txt":
        title = filename_stem
        stripped = content.lstrip()
        summary = stripped[:200].replace("\n", " ").strip()

    if title is None:
        title = filename_stem

    return title, summary, frontmatter


# =============================================================================
# Markdown 块拆分
# =============================================================================


def split_markdown_blocks(content: str) -> List[Dict[str, Any]]:
    """
    将 Markdown 内容按结构拆分为块。
    代码块（code_block）内容严格保持原样，不做任何改写。
    """
    blocks: List[Dict[str, Any]] = []
    lines = content.split("\n")

    # 计算每行起始字符偏移
    line_offsets = [0]
    for line in lines:
        line_offsets.append(line_offsets[-1] + len(line) + 1)  # +1 for \n

    def make_block(
        block_type: str,
        block_content: str,
        line_start: int,
        line_end: int,
        block_level: Optional[int] = None,
        heading_anchor: Optional[str] = None,
        block_metadata: Optional[dict] = None,
    ) -> Dict[str, Any]:
        char_start = line_offsets[line_start - 1] if line_start - 1 < len(line_offsets) else 0
        char_end = (
            line_offsets[line_end] if line_end < len(line_offsets) else len(content)
        )
        return {
            "block_index": len(blocks),
            "block_type": block_type,
            "block_level": block_level,
            "block_content": block_content,
            "block_line_start": line_start,
            "block_line_end": line_end,
            "block_char_offset_start": char_start,
            "block_char_offset_end": char_end,
            "heading_anchor": heading_anchor,
            "block_metadata": json.dumps(block_metadata or {}, ensure_ascii=False),
        }

    i = 0
    n = len(lines)

    # 处理 frontmatter
    if n > 0 and lines[0].strip() == "---":
        end_idx = -1
        for j in range(1, n):
            if lines[j].strip() == "---":
                end_idx = j
                break
        if end_idx > 0:
            fm_content = "\n".join(lines[1:end_idx])
            blocks.append(
                make_block(
                    "frontmatter",
                    fm_content,
                    1,
                    end_idx + 1,
                    block_metadata={"format": "yaml"},
                )
            )
            i = end_idx + 1

    while i < n:
        line = lines[i]

        # 空行跳过
        if not line.strip():
            i += 1
            continue

        stripped_left = line.lstrip()

        # 围栏代码块（``` 或 ~~~）
        if stripped_left.startswith("```") or stripped_left.startswith("~~~"):
            fence = stripped_left[:3]
            lang = stripped_left[3:].strip()
            start_line = i + 1
            code_lines = [line]
            i += 1
            while i < n:
                code_lines.append(lines[i])
                if lines[i].lstrip().startswith(fence):
                    i += 1
                    break
                i += 1
            # 代码块内容严格保持原样
            blocks.append(
                make_block(
                    "code_block",
                    "\n".join(code_lines),
                    start_line,
                    i,
                    block_metadata={"fence": fence, "language": lang},
                )
            )
            continue

        # 缩进代码块（4 空格开头）
        if line.startswith("    ") and not line.startswith("       "):
            start_line = i + 1
            code_lines: List[str] = []
            while i < n and (lines[i].startswith("    ") or not lines[i].strip()):
                code_lines.append(lines[i])
                i += 1
            blocks.append(
                make_block(
                    "code_block",
                    "\n".join(code_lines),
                    start_line,
                    i,
                    block_metadata={"fence": "indented"},
                )
            )
            continue

        # 标题
        heading_match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if heading_match:
            level = len(heading_match.group(1))
            text = heading_match.group(2).strip()
            anchor = slugify(text)
            blocks.append(
                make_block(
                    "heading",
                    line,
                    i + 1,
                    i + 1,
                    block_level=level,
                    heading_anchor=anchor,
                    block_metadata={"heading_level": level, "text": text},
                )
            )
            i += 1
            continue

        # 脚注定义 [^id]:
        if re.match(r"^\[\^[^\]]+\]:", line):
            start_line = i + 1
            fn_lines = [line]
            i += 1
            while i < n and lines[i].strip() and lines[i].startswith((" ", "\t")):
                fn_lines.append(lines[i])
                i += 1
            blocks.append(
                make_block(
                    "footnote",
                    "\n".join(fn_lines),
                    start_line,
                    i,
                    block_metadata={},
                )
            )
            continue

        # 列表项
        list_match = re.match(r"^(\s*)([-*+]|\d+\.)\s+(.+)$", line)
        if list_match:
            indent = len(list_match.group(1))
            level = indent // 2 + 1
            marker = list_match.group(2)
            start_line = i + 1
            list_lines = [line]
            i += 1
            while i < n:
                nl = lines[i]
                if not nl.strip():
                    # 空行：向前看是否仍是列表
                    if i + 1 < n and re.match(r"^(\s*)([-*+]|\d+\.)\s+", lines[i + 1]):
                        list_lines.append(nl)
                        i += 1
                        continue
                    break
                if re.match(r"^(\s*)([-*+]|\d+\.)\s+", nl):
                    list_lines.append(nl)
                    i += 1
                    continue
                if nl.startswith(("  ", "\t")) and not nl.startswith("    "):
                    list_lines.append(nl)
                    i += 1
                    continue
                break
            blocks.append(
                make_block(
                    "list_item",
                    "\n".join(list_lines),
                    start_line,
                    i,
                    block_level=level,
                    block_metadata={"list_marker": marker, "list_level": level},
                )
            )
            continue

        # 引用
        if line.startswith(">"):
            start_line = i + 1
            quote_lines = [line]
            i += 1
            while i < n:
                nl = lines[i]
                if nl.startswith(">"):
                    quote_lines.append(nl)
                    i += 1
                    continue
                if not nl.strip() and i + 1 < n and lines[i + 1].startswith(">"):
                    quote_lines.append(nl)
                    i += 1
                    continue
                break
            blocks.append(
                make_block(
                    "quote",
                    "\n".join(quote_lines),
                    start_line,
                    i,
                    block_metadata={},
                )
            )
            continue

        # 表格行（含 | 且非标题）
        if "|" in line and not line.lstrip().startswith("#"):
            start_line = i + 1
            table_lines = [line]
            i += 1
            while i < n and "|" in lines[i] and lines[i].strip():
                table_lines.append(lines[i])
                i += 1
            blocks.append(
                make_block(
                    "table_row",
                    "\n".join(table_lines),
                    start_line,
                    i,
                    block_metadata={"row_count": len(table_lines)},
                )
            )
            continue

        # 段落
        start_line = i + 1
        para_lines = [line]
        i += 1
        while i < n:
            nl = lines[i]
            if not nl.strip():
                break
            if nl.lstrip().startswith(("```", "~~~")):
                break
            if nl.startswith("#"):
                break
            if nl.startswith(">"):
                break
            if re.match(r"^(\s*)([-*+]|\d+\.)\s+", nl):
                break
            if "|" in nl and nl.strip().startswith("|"):
                break
            if nl.startswith("    ") and not nl.startswith("       "):
                break
            para_lines.append(nl)
            i += 1
        blocks.append(
            make_block(
                "paragraph",
                "\n".join(para_lines),
                start_line,
                i,
                block_metadata={},
            )
        )

    return blocks


# =============================================================================
# CSV 块拆分
# =============================================================================


def split_csv_blocks(content: str) -> List[Dict[str, Any]]:
    """每行作为一个 csv_row 块；首行为表头。"""
    blocks: List[Dict[str, Any]] = []
    lines = content.split("\n")
    line_offsets = [0]
    for line in lines:
        line_offsets.append(line_offsets[-1] + len(line) + 1)

    for idx, line in enumerate(lines):
        if not line.strip():
            continue
        is_header = idx == 0
        blocks.append(
            {
                "block_index": len(blocks),
                "block_type": "csv_row",
                "block_level": None,
                "block_content": line,
                "block_line_start": idx + 1,
                "block_line_end": idx + 1,
                "block_char_offset_start": line_offsets[idx],
                "block_char_offset_end": line_offsets[idx + 1],
                "heading_anchor": None,
                "block_metadata": json.dumps(
                    {"row_index": idx, "is_header": is_header}, ensure_ascii=False
                ),
            }
        )
    return blocks


# =============================================================================
# JSON 块拆分
# =============================================================================


def split_json_blocks(content: str) -> List[Dict[str, Any]]:
    """将 JSON 扁平化为 json_node 块，使用点号路径。"""
    blocks: List[Dict[str, Any]] = []
    try:
        data = json.loads(content)
    except Exception:
        return blocks

    def add_block(key_path: str, value: Any) -> None:
        value_type = type(value).__name__
        if isinstance(value, str):
            v_str = value
        else:
            try:
                v_str = json.dumps(value, ensure_ascii=False)
            except Exception:
                v_str = str(value)
        blocks.append(
            {
                "block_index": len(blocks),
                "block_type": "json_node",
                "block_level": None,
                "block_content": v_str,
                "block_line_start": None,
                "block_line_end": None,
                "block_char_offset_start": None,
                "block_char_offset_end": None,
                "heading_anchor": None,
                "block_metadata": json.dumps(
                    {"key_path": key_path, "value_type": value_type},
                    ensure_ascii=False,
                ),
            }
        )

    def flatten(obj: Any, prefix: str = "") -> None:
        if isinstance(obj, dict):
            if not obj:
                add_block(prefix or "$", obj)
                return
            for k, v in obj.items():
                kp = f"{prefix}.{k}" if prefix else k
                if isinstance(v, (dict, list)):
                    flatten(v, kp)
                else:
                    add_block(kp, v)
        elif isinstance(obj, list):
            if not obj:
                add_block(prefix or "$", obj)
                return
            for idx, item in enumerate(obj):
                kp = f"{prefix}.{idx}" if prefix else str(idx)
                if isinstance(item, (dict, list)):
                    flatten(item, kp)
                else:
                    add_block(kp, item)
        else:
            add_block(prefix or "$", obj)

    flatten(data)
    return blocks


# =============================================================================
# TXT 块拆分
# =============================================================================


def split_txt_blocks(content: str) -> List[Dict[str, Any]]:
    """按空行分段，每段一个 paragraph 块。"""
    blocks: List[Dict[str, Any]] = []
    lines = content.split("\n")
    line_offsets = [0]
    for line in lines:
        line_offsets.append(line_offsets[-1] + len(line) + 1)

    i = 0
    n = len(lines)
    while i < n:
        if not lines[i].strip():
            i += 1
            continue
        start_line = i + 1
        para_lines: List[str] = []
        while i < n and lines[i].strip():
            para_lines.append(lines[i])
            i += 1
        blocks.append(
            {
                "block_index": len(blocks),
                "block_type": "paragraph",
                "block_level": None,
                "block_content": "\n".join(para_lines),
                "block_line_start": start_line,
                "block_line_end": i,
                "block_char_offset_start": line_offsets[start_line - 1],
                "block_char_offset_end": line_offsets[i] if i < len(line_offsets) else len(content),
                "heading_anchor": None,
                "block_metadata": json.dumps({}, ensure_ascii=False),
            }
        )
    return blocks


def split_blocks(content: str, ext: str) -> List[Dict[str, Any]]:
    """根据扩展名调用对应的块拆分器。"""
    if ext == "md":
        return split_markdown_blocks(content)
    if ext == "csv":
        return split_csv_blocks(content)
    if ext == "json":
        return split_json_blocks(content)
    if ext == "txt":
        return split_txt_blocks(content)
    return []


# =============================================================================
# 交叉引用提取
# =============================================================================


def extract_cross_references(content: str, file_id: int) -> List[Dict[str, Any]]:
    """从文件内容中提取交叉引用（wikilink/markdown_link/footnote/external_url）。"""
    refs: List[Dict[str, Any]] = []

    # Wikilinks: [[target]] 或 [[target|text]]
    for m in re.finditer(r"\[\[([^\]]+?)\]\]", content):
        raw = m.group(1)
        if "|" in raw:
            target, text = raw.split("|", 1)
        else:
            target, text = raw, raw
        refs.append({
            "source_file_id": file_id,
            "source_block_id": None,
            "reference_type": "wikilink",
            "reference_text": text.strip(),
            "target_path": target.strip(),
            "target_db": None,
            "target_record_id": None,
            "target_anchor": None,
            "resolution_status": "pending",
            "reference_context": content[max(0, m.start() - 40):m.end() + 40],
        })

    # Markdown links: [text](target)
    for m in re.finditer(r"\[([^\]]+?)\]\(([^)\s]+?)\)", content):
        text = m.group(1)
        target = m.group(2)
        ref_type = "external_url" if target.startswith(("http://", "https://", "ftp://")) else "markdown_link"
        refs.append({
            "source_file_id": file_id,
            "source_block_id": None,
            "reference_type": ref_type,
            "reference_text": text.strip(),
            "target_path": target.strip(),
            "target_db": None,
            "target_record_id": None,
            "target_anchor": None,
            "resolution_status": "pending",
            "reference_context": content[max(0, m.start() - 40):m.end() + 40],
        })

    # Footnote 引用: [^id]（非定义）
    for m in re.finditer(r"\[\^([^\]]+?)\](?!:)", content):
        refs.append({
            "source_file_id": file_id,
            "source_block_id": None,
            "reference_type": "footnote",
            "reference_text": m.group(1).strip(),
            "target_path": None,
            "target_db": None,
            "target_record_id": None,
            "target_anchor": m.group(1).strip(),
            "resolution_status": "pending",
            "reference_context": content[max(0, m.start() - 40):m.end() + 40],
        })

    return refs


# =============================================================================
# 数据库操作
# =============================================================================


def apply_schema(conn: sqlite3.Connection) -> None:
    """对连接应用通用架构 SQL。"""
    schema_sql = SCHEMA_SQL_PATH.read_text(encoding="utf-8")
    conn.executescript(schema_sql)
    conn.commit()


def open_database(db_path: Path, create: bool = True) -> sqlite3.Connection:
    """打开（或创建）数据库并应用架构。"""
    if not create and not db_path.exists():
        raise FileNotFoundError(f"数据库不存在: {db_path}")
    if db_path.exists():
        db_path.unlink()
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA foreign_keys = ON")
    apply_schema(conn)
    return conn


def connect_existing(db_path: Path) -> sqlite3.Connection:
    """连接已有数据库（不重建）。"""
    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def get_db_path(db_name: str) -> Path:
    """返回数据库文件路径。"""
    cfg = FOLDER_DB_MAP[db_name]
    return PROJECT_ROOT / cfg["folder"] / cfg["db_filename"]


def detect_db_for_file(rel_path: str) -> Optional[str]:
    """根据文件相对路径前缀检测归属数据库。"""
    for db_name in DB_BUILD_ORDER:
        cfg = FOLDER_DB_MAP[db_name]
        folder = cfg["folder"]
        prefix = folder + "/"
        if rel_path.startswith(prefix):
            # 检查是否落在跳过子目录
            for skip_sub in cfg["skip_subfolders"]:
                skip_full = folder + "/" + skip_sub + "/"
                if rel_path.startswith(skip_full):
                    return None
            return db_name
    return None


# =============================================================================
# 文件入库
# =============================================================================


def insert_file_record(
    conn: sqlite3.Connection, meta: Dict[str, Any]
) -> int:
    """插入 files 记录，返回 file_id。"""
    cur = conn.execute(
        """
        INSERT INTO files (
            file_path, filename, folder_path, file_extension, file_size,
            sha256, content_hash, line_count, char_count, encoding,
            line_ending, mtime, ingested_at, title, summary, frontmatter,
            status, duplicate_of_id, duplicate_type
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, NULL, NULL)
        """,
        (
            meta["file_path"],
            meta["filename"],
            meta["folder_path"],
            meta["file_extension"],
            meta["file_size"],
            meta["sha256"],
            meta["content_hash"],
            meta["line_count"],
            meta["char_count"],
            meta["encoding"],
            meta["line_ending"],
            meta["mtime"],
            meta["ingested_at"],
            meta["title"],
            meta["summary"],
            meta["frontmatter"],
            meta["status"],
        ),
    )
    return cur.lastrowid


def insert_blocks(
    conn: sqlite3.Connection, file_id: int, blocks: List[Dict[str, Any]]
) -> int:
    """插入块记录（FTS5 由触发器自动同步）。返回插入数量。"""
    for b in blocks:
        conn.execute(
            """
            INSERT INTO blocks (
                file_id, block_index, block_type, block_level, block_content,
                block_line_start, block_line_end, block_char_offset_start,
                block_char_offset_end, heading_anchor, block_metadata
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                file_id,
                b["block_index"],
                b["block_type"],
                b["block_level"],
                b["block_content"],
                b["block_line_start"],
                b["block_line_end"],
                b["block_char_offset_start"],
                b["block_char_offset_end"],
                b["heading_anchor"],
                b["block_metadata"],
            ),
        )
    return len(blocks)


def insert_cross_references(
    conn: sqlite3.Connection, refs: List[Dict[str, Any]]
) -> int:
    """插入交叉引用记录。"""
    for r in refs:
        conn.execute(
            """
            INSERT INTO cross_references (
                source_file_id, source_block_id, reference_type, reference_text,
                target_path, target_db, target_record_id, target_anchor,
                resolution_status, reference_context
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                r["source_file_id"],
                r.get("source_block_id"),
                r["reference_type"],
                r["reference_text"],
                r.get("target_path"),
                r.get("target_db"),
                r.get("target_record_id"),
                r.get("target_anchor"),
                r.get("resolution_status", "pending"),
                r.get("reference_context"),
            ),
        )
    return len(refs)


def compute_content_hash(blocks: List[Dict[str, Any]]) -> str:
    """计算所有块内容拼接后的 SHA-256。"""
    h = hashlib.sha256()
    for b in blocks:
        h.update(b["block_content"].encode("utf-8"))
        h.update(b"\n")
    return h.hexdigest()


def build_file_metadata(
    path: Path, content: str, raw: bytes, has_bom: bool, line_ending: str
) -> Dict[str, Any]:
    """构建文件元数据字典。"""
    ext = path.suffix.lower().lstrip(".")
    filename = path.name
    folder_path = normalize_rel_path(path.parent)
    file_path = normalize_rel_path(path)
    filename_stem = path.stem

    title, summary, frontmatter = extract_title_summary(content, ext, filename_stem)

    line_count = content.count("\n") + (1 if content and not content.endswith("\n") else 0)
    char_count = len(content)
    sha256 = compute_sha256_bytes(raw)

    meta: Dict[str, Any] = {
        "file_path": file_path,
        "filename": filename,
        "folder_path": folder_path,
        "file_extension": ext,
        "file_size": path.stat().st_size,
        "sha256": sha256,
        "content_hash": "",  # 块拆分后填入
        "line_count": line_count,
        "char_count": char_count,
        "encoding": "utf-8",
        "line_ending": line_ending,
        "mtime": file_mtime_iso(path),
        "ingested_at": now_iso(),
        "title": title,
        "summary": summary,
        "frontmatter": frontmatter,
        "status": "active",
        "has_bom": has_bom,
    }
    return meta


# =============================================================================
# 扩展表入库
# =============================================================================


def try_parse_simple_yaml(text: str) -> Dict[str, str]:
    """简单解析 YAML frontmatter（key: value 形式）。"""
    result: Dict[str, str] = {}
    for line in text.split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = re.match(r"^([A-Za-z_][\w\-]*)\s*:\s*(.*)$", line)
        if m:
            key = m.group(1).strip()
            val = m.group(2).strip().strip("\"'")
            result[key] = val
    return result


def extract_section(content: str, heading_pattern: str) -> Optional[str]:
    """从 Markdown 中提取指定标题下的内容（直到下一个同级或更高级标题）。"""
    lines = content.split("\n")
    start_idx = -1
    start_level = 0
    for i, line in enumerate(lines):
        m = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if m:
            level = len(m.group(1))
            text = m.group(2).strip()
            if re.search(heading_pattern, text):
                start_idx = i + 1
                start_level = level
                break
    if start_idx < 0:
        return None
    end_idx = len(lines)
    for j in range(start_idx, len(lines)):
        m = re.match(r"^(#{1,6})\s+", lines[j])
        if m and len(m.group(1)) <= start_level:
            end_idx = j
            break
    return "\n".join(lines[start_idx:end_idx]).strip()


def ingest_extension_tables(
    conn: sqlite3.Connection,
    db_name: str,
    file_id: int,
    file_path: str,
    content: str,
    ext: str,
    blocks: List[Dict[str, Any]],
) -> Tuple[bool, str]:
    """
    尝试将文件入库到扩展表。
    返回 (ingested, message)。
    """
    try:
        if db_name == "fact_checks" and ext == "md":
            return _ingest_fact_check(conn, file_id, content)
        if db_name == "review_reports" and ext == "md":
            return _ingest_review_report(conn, file_id, file_path, content)
        if db_name == "cross_indexes" and ext == "md":
            return _ingest_cross_index(conn, file_id, file_path, content)
        if db_name == "original_sources" and ext == "md":
            return _ingest_original_source(conn, file_id, file_path, content)
        if db_name == "metadata_interfaces":
            return _ingest_metadata_interface(conn, file_id, file_path, content, ext)
    except Exception as e:
        return False, f"extension_error: {type(e).__name__}: {e}"
    return False, "no_matching_extension"


def _ingest_fact_check(
    conn: sqlite3.Connection, file_id: int, content: str
) -> Tuple[bool, str]:
    """事实核查记录扩展表入库。"""
    fm = extract_yaml_frontmatter(content)
    fields: Dict[str, Optional[str]] = {
        "claim": None,
        "evidence_strength": None,
        "page": None,
        "controversy": None,
        "verifier": None,
        "verified_date": None,
        "status": None,
        "notes": None,
    }
    if fm:
        parsed = try_parse_simple_yaml(fm)
        for k in fields:
            if k in parsed:
                fields[k] = parsed[k]
    # 如果没有 frontmatter 字段，尝试从正文提取
    if not any(fields.values()):
        return False, "extension_skipped: no fact_check fields"
    conn.execute(
        """
        INSERT INTO fact_check_records (
            file_id, claim, evidence_strength, page, controversy,
            verifier, verified_date, status, notes
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            file_id,
            fields["claim"],
            fields["evidence_strength"],
            fields["page"],
            fields["controversy"],
            fields["verifier"],
            fields["verified_date"],
            fields["status"],
            fields["notes"],
        ),
    )
    return True, "extension_ingested: fact_check_records"


def _ingest_review_report(
    conn: sqlite3.Connection, file_id: int, file_path: str, content: str
) -> Tuple[bool, str]:
    """核查报告扩展表入库（disputes / peer_reviews）。"""
    if "08-历史争议图谱" in file_path:
        dispute_name = None
        title_match = re.search(r"^#\s+(.+?)\s*$", content, re.MULTILINE)
        if title_match:
            dispute_name = title_match.group(1).strip()
        summary = extract_section(content, r"概述|简介|背景")
        positions = extract_section(content, r"立场|各方|观点")
        evidence = extract_section(content, r"证据|史料")
        resolution = extract_section(content, r"结论|解决|定论")
        if dispute_name or summary:
            conn.execute(
                """
                INSERT INTO disputes (
                    file_id, dispute_name, parties, period, summary,
                    positions, evidence, resolution_status
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    file_id,
                    dispute_name,
                    None,
                    None,
                    summary,
                    positions,
                    evidence,
                    resolution,
                ),
            )
            return True, "extension_ingested: disputes"
    elif "10-同行评议" in file_path:
        reviewer = None
        title_match = re.search(r"^#\s+(.+?)\s*$", content, re.MULTILINE)
        if title_match:
            reviewer = title_match.group(1).strip()
        comments = extract_section(content, r"意见|评论|建议")
        verdict = extract_section(content, r"结论|判定|评价")
        if reviewer or comments:
            conn.execute(
                """
                INSERT INTO peer_reviews (
                    file_id, reviewer, review_round, submission_date,
                    verdict, comments
                ) VALUES (?, ?, ?, ?, ?, ?)
                """,
                (file_id, reviewer, None, None, verdict, comments),
            )
            return True, "extension_ingested: peer_reviews"
    return False, "extension_skipped: no review_report fields"


def _ingest_cross_index(
    conn: sqlite3.Connection, file_id: int, file_path: str, content: str
) -> Tuple[bool, str]:
    """交叉索引扩展表入库。"""
    title_match = re.search(r"^#\s+(.+?)\s*$", content, re.MULTILINE)
    name = title_match.group(1).strip() if title_match else None
    summary = extract_section(content, r"概述|简介|定义|生平|传记")
    if "01-人名索引" in file_path:
        if name:
            conn.execute(
                """
                INSERT INTO person_index (
                    file_id, person_name, normalized_name, aliases, role,
                    biography_summary, page_refs
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (file_id, name, None, None, None, summary, None),
            )
            return True, "extension_ingested: person_index"
    elif "03-命令索引" in file_path:
        if name:
            desc = extract_section(content, r"描述|说明|用途")
            conn.execute(
                """
                INSERT INTO command_index (
                    file_id, command_name, manual_section, category,
                    description, page_refs
                ) VALUES (?, ?, ?, ?, ?, ?)
                """,
                (file_id, name, None, None, desc, None),
            )
            return True, "extension_ingested: command_index"
    elif "04-术语表" in file_path:
        if name:
            trans = extract_section(content, r"译名|翻译|英文")
            defn = extract_section(content, r"定义|释义|说明")
            conn.execute(
                """
                INSERT INTO term_index (
                    file_id, term, translation, category, definition, page_refs
                ) VALUES (?, ?, ?, ?, ?, ?)
                """,
                (file_id, name, trans, None, defn, None),
            )
            return True, "extension_ingested: term_index"
    elif "07-概念史与思想谱系" in file_path:
        if name:
            etym = extract_section(content, r"词源|语源|etymology")
            hist = extract_section(content, r"历史|沿革|演变")
            related = extract_section(content, r"相关|关联|参见")
            conn.execute(
                """
                INSERT INTO concept_history (
                    file_id, concept_name, etymology, history_summary,
                    related_concepts, page_refs
                ) VALUES (?, ?, ?, ?, ?, ?)
                """,
                (file_id, name, etym, hist, related, None),
            )
            return True, "extension_ingested: concept_history"
    elif "08-人物传记与学术谱系" in file_path:
        if name:
            bio = extract_section(content, r"传记|生平|简历")
            genealogy = extract_section(content, r"师承|谱系|学术")
            affil = extract_section(content, r"机构|任职|单位")
            works = extract_section(content, r"著作|作品|贡献")
            conn.execute(
                """
                INSERT INTO person_biography (
                    file_id, person_name, biography, academic_genealogy,
                    affiliations, works
                ) VALUES (?, ?, ?, ?, ?, ?)
                """,
                (file_id, name, bio, genealogy, affil, works),
            )
            return True, "extension_ingested: person_biography"
    return False, "extension_skipped: no cross_index fields"


def _ingest_original_source(
    conn: sqlite3.Connection, file_id: int, file_path: str, content: str
) -> Tuple[bool, str]:
    """原始史料扩展表入库。"""
    if "06-考据记录" in file_path:
        source_ver = extract_section(content, r"查证来源|一手来源|史料来源")
        cross_ver = extract_section(content, r"交叉验证|多源对比")
        doubt = extract_section(content, r"存疑|存疑判定|存疑依据")
        if source_ver or cross_ver or doubt:
            conn.execute(
                """
                INSERT INTO kaoju_records (
                    file_id, source_verification, cross_verification_method,
                    doubt_basis, page_refs
                ) VALUES (?, ?, ?, ?, ?)
                """,
                (file_id, source_ver, cross_ver, doubt, None),
            )
            return True, "extension_ingested: kaoju_records"
    elif "05-bsd官方安全公告" in file_path:
        title_match = re.search(r"^#\s+(.+?)\s*$", content, re.MULTILINE)
        advisory_id = title_match.group(1).strip() if title_match else None
        date_section = extract_section(content, r"发布日期|发布时间|日期")
        affected = extract_section(content, r"影响版本|受影响")
        if advisory_id:
            conn.execute(
                """
                INSERT INTO security_advisories (
                    file_id, advisory_id, project, release_date,
                    affected_versions, component, severity, cve_references
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (file_id, advisory_id, None, date_section, affected, None, None, None),
            )
            return True, "extension_ingested: security_advisories"
    elif "04-nvd漏洞元数据" in file_path:
        cve_match = re.search(r"CVE-\d{4}-\d+", content)
        cve_id = cve_match.group(0) if cve_match else None
        if cve_id:
            score_match = re.search(r"CVSS[\s:]*([\d.]+)", content)
            cvss_score = float(score_match.group(1)) if score_match else None
            conn.execute(
                """
                INSERT INTO vulnerability_metadata (
                    file_id, cve_id, published_date, modified_date,
                    cvss_score, cvss_vector, cwe, affected_products
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (file_id, cve_id, None, None, cvss_score, None, None, None),
            )
            return True, "extension_ingested: vulnerability_metadata"
    return False, "extension_skipped: no original_source fields"


def _ingest_metadata_interface(
    conn: sqlite3.Connection, file_id: int, file_path: str, content: str, ext: str
) -> Tuple[bool, str]:
    """元数据接口扩展表入库。"""
    filename = Path(file_path).name

    if filename == "chapter_index.json" and ext == "json":
        try:
            data = json.loads(content)
            if isinstance(data, list):
                for item in data:
                    if not isinstance(item, dict):
                        continue
                    conn.execute(
                        """
                        INSERT INTO chapter_metadata (
                            file_id, chapter_id, volume, chapter, title,
                            word_count, main_thread, status
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            file_id,
                            item.get("id"),
                            item.get("volume"),
                            item.get("chapter"),
                            item.get("title"),
                            item.get("word_count_actual"),
                            None,
                            item.get("status"),
                        ),
                    )
                return True, f"extension_ingested: chapter_metadata ({len(data)} rows)"
        except Exception:
            pass
        return False, "extension_skipped: chapter_metadata parse failed"

    if ext == "csv":
        reader = csv.reader(content.splitlines())
        rows = list(reader)
        if not rows:
            return False, "extension_skipped: empty csv"
        header = [h.strip() for h in rows[0]]

        if filename == "build_status.csv":
            for row in rows[1:]:
                if not row:
                    continue
                row_dict = dict(zip(header, row))
                conn.execute(
                    """
                    INSERT INTO build_status (
                        file_id, target, last_build, last_success, last_failure, status
                    ) VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (
                        file_id,
                        row_dict.get("chapter_id"),
                        row_dict.get("last_updated"),
                        None,
                        None,
                        row_dict.get("status"),
                    ),
                )
            return True, f"extension_ingested: build_status ({len(rows)-1} rows)"

        if filename == "timeline.csv":
            for row in rows[1:]:
                if not row:
                    continue
                row_dict = dict(zip(header, row))
                conn.execute(
                    """
                    INSERT INTO timeline_records (
                        file_id, event_date, event_description, event_type, source_chapter
                    ) VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        file_id,
                        row_dict.get("date"),
                        row_dict.get("event"),
                        row_dict.get("category"),
                        row_dict.get("chapter"),
                    ),
                )
            return True, f"extension_ingested: timeline_records ({len(rows)-1} rows)"

        if filename == "citation_frequency.csv":
            for row in rows[1:]:
                if not row:
                    continue
                row_dict = dict(zip(header, row))
                cited_count = None
                try:
                    cited_count = int(row_dict.get("cited_count", 0))
                except (ValueError, TypeError):
                    pass
                conn.execute(
                    """
                    INSERT INTO citation_frequency (
                        file_id, reference_id, citation_count, cited_in_chapters, last_cited
                    ) VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        file_id,
                        row_dict.get("citation_id"),
                        cited_count,
                        None,
                        row_dict.get("last_verified"),
                    ),
                )
            return True, f"extension_ingested: citation_frequency ({len(rows)-1} rows)"

        if filename == "authors_index.csv":
            # authors_index.csv 实际可能没有作者字段；尽力提取
            for row in rows[1:]:
                if not row:
                    continue
                row_dict = dict(zip(header, row))
                author_name = row_dict.get("author_name") or row_dict.get("author")
                if author_name:
                    conn.execute(
                        """
                        INSERT INTO author_index (
                            file_id, author_name, email, affiliation, chapters_contributed
                        ) VALUES (?, ?, ?, ?, ?)
                        """,
                        (file_id, author_name, None, None, None),
                    )
            return True, f"extension_ingested: author_index ({len(rows)-1} rows)"

    return False, "extension_skipped: no metadata_interface match"


# =============================================================================
# 日志与看板
# =============================================================================


def write_build_log_entry(db_name: str, entry: Dict[str, Any]) -> None:
    """追加一条 JSONL 日志到 build_log_<db_name>.jsonl。"""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_path = LOG_DIR / f"build_log_{db_name}.jsonl"
    line = json.dumps(entry, ensure_ascii=False)
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def append_error(
    db_name: str,
    file_path: str,
    error_type: str,
    error_message: str,
    suggested_fix: str = "",
) -> None:
    """追加错误到 errors.md。"""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    err_path = LOG_DIR / "errors.md"
    if not err_path.exists():
        err_path.write_text(
            "# 文件夹级数据库构建错误清单\n\n"
            "> 按时间倒序列出最近 50 条错误。\n\n"
            "| 时间 | 数据库 | 文件 | 错误类型 | 错误信息 | 建议修复动作 |\n"
            "| --- | --- | --- | --- | --- | --- |\n",
            encoding="utf-8",
        )
    # 读取现有内容
    lines = err_path.read_text(encoding="utf-8").split("\n")
    header = lines[:5]
    body = lines[5:]
    new_row = f"| {now_iso()} | {db_name} | {file_path} | {error_type} | {error_message} | {suggested_fix} |"
    # 在表格末尾（最近 50 条）插入
    body = [new_row] + body[:49]
    err_path.write_text("\n".join(header + body), encoding="utf-8")


def update_dashboard(db_name: str, stats: Dict[str, Any]) -> None:
    """更新两个位置的 dashboard.md。"""
    table_row = (
        f"| {db_name} | completed | {stats['file_count']} | {stats['block_count']} | "
        f"{stats['size_bytes']} | {stats['sha256']} | {stats['built_at']} | "
        f"{stats['build_duration_ms']} ms |"
    )
    for dash_path in [LOG_DIR / "dashboard.md", INDEX_DIR / "dashboard.md"]:
        if not dash_path.exists():
            continue
        content = dash_path.read_text(encoding="utf-8")
        lines = content.split("\n")
        new_lines: List[str] = []
        for line in lines:
            if line.startswith(f"| {db_name} "):
                new_lines.append(table_row)
            else:
                new_lines.append(line)
        dash_path.write_text("\n".join(new_lines), encoding="utf-8")


def update_registry(db_name: str, stats: Dict[str, Any]) -> None:
    """更新 folder_db_registry.csv。"""
    reg_path = INDEX_DIR / "folder_db_registry.csv"
    if not reg_path.exists():
        return
    cfg = FOLDER_DB_MAP[db_name]
    rows: List[List[str]] = []
    reader = csv.reader(reg_path.read_text(encoding="utf-8").splitlines())
    header = next(reader, None)
    if header is None:
        return
    rows.append(header)
    found = False
    for row in reader:
        if len(row) > 0 and row[0] == db_name:
            row = [
                db_name,
                f"{cfg['folder']}/{cfg['db_filename']}",
                cfg["folder"],
                str(stats["file_count"]),
                str(stats["block_count"]),
                str(stats["size_bytes"]),
                stats["sha256"],
                SCHEMA_VERSION,
                stats["built_at"],
                str(stats["build_duration_ms"]),
            ]
            found = True
        rows.append(row)
    if not found:
        rows.append([
            db_name,
            f"{cfg['folder']}/{cfg['db_filename']}",
            cfg["folder"],
            str(stats["file_count"]),
            str(stats["block_count"]),
            str(stats["size_bytes"]),
            stats["sha256"],
            SCHEMA_VERSION,
            stats["built_at"],
            str(stats["build_duration_ms"]),
        ])
    with open(reg_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)


# =============================================================================
# 核心构建逻辑
# =============================================================================


def ingest_one_file(
    conn: sqlite3.Connection,
    db_name: str,
    path: Path,
    log_entries: List[Dict[str, Any]],
) -> Optional[int]:
    """
    将单个文件入库。
    返回 file_id（失败返回 None）。
    log_entries 用于收集日志条目。
    """
    t0 = time.time()
    rel_path = normalize_rel_path(path)
    try:
        text, raw, has_bom, line_ending = read_file_text(path)
        ext = path.suffix.lower().lstrip(".")
        meta = build_file_metadata(path, text, raw, has_bom, line_ending)

        # 块拆分
        blocks = split_blocks(text, ext)
        meta["content_hash"] = compute_content_hash(blocks)

        # 入库 files
        file_id = insert_file_record(conn, meta)

        # 入库 blocks（触发器自动同步 blocks_fts）
        insert_blocks(conn, file_id, blocks)

        # 交叉引用
        refs = extract_cross_references(text, file_id)
        if refs:
            insert_cross_references(conn, refs)

        # 扩展表
        ext_ok, ext_msg = ingest_extension_tables(
            conn, db_name, file_id, rel_path, text, ext, blocks
        )
        if ext_ok:
            log_entries.append({
                "timestamp": now_iso(),
                "action": "extension_ingested",
                "db_name": db_name,
                "file_path": rel_path,
                "file_id": file_id,
                "status": "ok",
                "message": ext_msg,
                "duration_ms": int((time.time() - t0) * 1000),
            })
        else:
            log_entries.append({
                "timestamp": now_iso(),
                "action": "extension_skipped",
                "db_name": db_name,
                "file_path": rel_path,
                "file_id": file_id,
                "status": "ok",
                "message": ext_msg,
                "duration_ms": 0,
            })

        log_entries.append({
            "timestamp": now_iso(),
            "action": "file_ingested",
            "db_name": db_name,
            "file_path": rel_path,
            "file_id": file_id,
            "status": "ok",
            "message": f"Ingested {len(blocks)} blocks",
            "duration_ms": int((time.time() - t0) * 1000),
        })
        return file_id

    except Exception as e:
        err_type = type(e).__name__
        err_msg = str(e).replace("\n", " ")[:300]
        log_entries.append({
            "timestamp": now_iso(),
            "action": "error",
            "db_name": db_name,
            "file_path": rel_path,
            "status": "error",
            "message": f"{err_type}: {err_msg}",
            "duration_ms": int((time.time() - t0) * 1000),
        })
        append_error(db_name, rel_path, err_type, err_msg, "检查文件编码与格式")
        return None


def build_database(db_name: str, rebuild: bool = False) -> Dict[str, Any]:
    """
    构建单个数据库。
    返回统计字典。
    """
    cfg = FOLDER_DB_MAP[db_name]
    db_path = get_db_path(db_name)
    t_start = time.time()

    log_entries: List[Dict[str, Any]] = []
    log_entries.append({
        "timestamp": now_iso(),
        "action": "start",
        "db_name": db_name,
        "status": "ok",
        "message": f"Starting build (rebuild={rebuild})",
        "duration_ms": 0,
    })

    # 打开/创建数据库
    conn = open_database(db_path, create=True)

    # 扫描文件
    files = scan_folder(db_name)
    total = len(files)

    file_count = 0
    block_count = 0
    commit_counter = 0

    for path in files:
        file_id = ingest_one_file(conn, db_name, path, log_entries)
        if file_id is not None:
            file_count += 1
            # 查询该文件的块数
            cur = conn.execute(
                "SELECT COUNT(*) FROM blocks WHERE file_id = ?", (file_id,)
            )
            block_count += cur.fetchone()[0]
        commit_counter += 1
        if commit_counter % 100 == 0:
            conn.commit()

    conn.commit()

    # 计算数据库文件 SHA-256 与大小
    conn.close()
    db_sha = compute_sha256(db_path)
    db_size = db_path.stat().st_size
    duration_ms = int((time.time() - t_start) * 1000)
    built_at = now_iso()

    stats = {
        "file_count": file_count,
        "block_count": block_count,
        "size_bytes": db_size,
        "sha256": db_sha,
        "built_at": built_at,
        "build_duration_ms": duration_ms,
    }

    log_entries.append({
        "timestamp": now_iso(),
        "action": "complete",
        "db_name": db_name,
        "status": "ok",
        "message": f"Built {file_count}/{total} files, {block_count} blocks",
        "duration_ms": duration_ms,
    })

    # 写入日志
    for entry in log_entries:
        write_build_log_entry(db_name, entry)

    # 更新看板与注册表
    update_dashboard(db_name, stats)
    update_registry(db_name, stats)

    return stats


# =============================================================================
# 模式实现
# =============================================================================


def resolve_db_name_by_folder(folder_name: str) -> Optional[str]:
    """根据文件夹名（中文）解析数据库名。"""
    for db_name, cfg in FOLDER_DB_MAP.items():
        if cfg["folder"] == folder_name:
            return db_name
    return None


def mode_folder(folder_name: str) -> int:
    """模式 1：构建单个文件夹。"""
    db_name = resolve_db_name_by_folder(folder_name)
    if db_name is None:
        print(f"[错误] 未知文件夹: {folder_name}", file=sys.stderr)
        print(f"  可选: {', '.join(cfg['folder'] for cfg in FOLDER_DB_MAP.values())}")
        return 1

    db_path = get_db_path(db_name)
    print(f"[1/1] Building {db_path.name}... ", end="", flush=True)
    t0 = time.time()
    stats = build_database(db_name, rebuild=False)
    elapsed = time.time() - t0
    print(f"[{stats['file_count']} files, {stats['block_count']} blocks] done in {elapsed:.1f}s")
    return 0


def mode_all() -> int:
    """模式 2：按顺序构建全部 7 个数据库。"""
    total = len(DB_BUILD_ORDER)
    had_error = False
    for idx, db_name in enumerate(DB_BUILD_ORDER, 1):
        db_path = get_db_path(db_name)
        print(f"[{idx}/{total}] Building {db_path.name}... ", end="", flush=True)
        t0 = time.time()
        try:
            stats = build_database(db_name, rebuild=False)
            elapsed = time.time() - t0
            print(
                f"[{stats['file_count']} files, {stats['block_count']} blocks] "
                f"done in {elapsed:.1f}s"
            )
        except Exception as e:
            elapsed = time.time() - t0
            print(f"ERROR in {elapsed:.1f}s: {e}", file=sys.stderr)
            had_error = True
    return 1 if had_error else 0


def mode_rebuild(db_name: str) -> int:
    """模式 3：删除并重建单个数据库。"""
    if db_name not in FOLDER_DB_MAP:
        print(f"[错误] 未知数据库名: {db_name}", file=sys.stderr)
        print(f"  可选: {', '.join(FOLDER_DB_MAP.keys())}")
        return 1

    db_path = get_db_path(db_name)
    print(f"[1/1] Rebuilding {db_path.name}... ", end="", flush=True)
    t0 = time.time()
    # build_database 会先删除再创建
    stats = build_database(db_name, rebuild=True)
    elapsed = time.time() - t0
    print(f"[{stats['file_count']} files, {stats['block_count']} blocks] done in {elapsed:.1f}s")
    return 0


def mode_add_file(file_path_str: str) -> int:
    """模式 4：增量添加单个文件。"""
    target = Path(file_path_str)
    if not target.is_absolute():
        target = PROJECT_ROOT / target
    if not target.exists():
        print(f"[错误] 文件不存在: {file_path_str}", file=sys.stderr)
        return 1

    rel_path = normalize_rel_path(target)
    db_name = detect_db_for_file(rel_path)
    if db_name is None:
        print(f"[错误] 无法确定文件归属数据库: {rel_path}", file=sys.stderr)
        print("  文件可能位于跳过子目录或不属于任何内容文件夹。")
        return 1

    db_path = get_db_path(db_name)
    if not db_path.exists():
        print(f"[信息] 数据库不存在，先创建: {db_path.name}")
        conn = open_database(db_path, create=True)
    else:
        conn = connect_existing(db_path)

    ext_with_dot = target.suffix.lower()
    if ext_with_dot not in SUPPORTED_EXTENSIONS:
        print(f"[错误] 不支持的扩展名: {ext_with_dot}", file=sys.stderr)
        conn.close()
        return 1
    ext = ext_with_dot.lstrip(".")

    # 检查 file_path 是否已存在
    cur = conn.execute("SELECT id FROM files WHERE file_path = ?", (rel_path,))
    existing = cur.fetchone()
    if existing:
        print(f"[信息] 文件已入库 (file_id={existing[0]})，请使用 --update-file。", file=sys.stderr)
        conn.close()
        return 1

    # SHA-256 去重检查
    sha = compute_sha256(target)
    cur = conn.execute("SELECT id, file_path FROM files WHERE sha256 = ?", (sha,))
    dup = cur.fetchone()
    if dup:
        print(f"[警告] SHA-256 与已入库文件重复: file_id={dup[0]} path={dup[1]}", file=sys.stderr)
        print("  跳过入库。如需强制入库请先删除重复记录。")
        conn.close()
        return 1

    # 入库
    log_entries: List[Dict[str, Any]] = []
    file_id = ingest_one_file(conn, db_name, target, log_entries)

    if file_id is not None:
        # 写入 update_log
        conn.execute(
            """
            INSERT INTO update_log (file_id, operation, field_changed, old_value, new_value, timestamp, operated_by, notes)
            VALUES (?, 'add', '*', NULL, ?, ?, 'build_folder_databases.py', '增量添加')
            """,
            (file_id, rel_path, now_iso()),
        )
        conn.commit()

        # 写入日志
        for entry in log_entries:
            write_build_log_entry(db_name, entry)

        print(f"[成功] 已入库: {rel_path} -> {db_name} (file_id={file_id})")
        conn.close()
        return 0
    else:
        conn.rollback()
        print(f"[失败] 入库失败: {rel_path}", file=sys.stderr)
        for entry in log_entries:
            write_build_log_entry(db_name, entry)
        conn.close()
        return 1


def mode_update_file(file_path_str: str) -> int:
    """模式 5：更新已有文件。"""
    target = Path(file_path_str)
    if not target.is_absolute():
        target = PROJECT_ROOT / target
    if not target.exists():
        print(f"[错误] 文件不存在: {file_path_str}", file=sys.stderr)
        return 1

    rel_path = normalize_rel_path(target)
    db_name = detect_db_for_file(rel_path)
    if db_name is None:
        print(f"[错误] 无法确定文件归属数据库: {rel_path}", file=sys.stderr)
        return 1

    db_path = get_db_path(db_name)
    if not db_path.exists():
        print(f"[信息] 数据库不存在，转为添加模式: {db_path.name}")
        return mode_add_file(file_path_str)

    conn = connect_existing(db_path)

    # 查询现有记录
    cur = conn.execute(
        "SELECT id, sha256, mtime FROM files WHERE file_path = ?",
        (rel_path,),
    )
    row = cur.fetchone()
    if not row:
        print(f"[信息] 文件未入库，转为添加模式: {rel_path}")
        conn.close()
        return mode_add_file(file_path_str)

    file_id, old_sha, old_mtime = row
    new_mtime = file_mtime_iso(target)

    # mtime 未变 → 跳过
    if new_mtime == old_mtime:
        print(f"[跳过] mtime 未变: {rel_path}")
        conn.close()
        return 0

    # mtime 变了，重算 SHA-256
    new_sha = compute_sha256(target)
    if new_sha == old_sha:
        # 仅更新 mtime
        conn.execute(
            "UPDATE files SET mtime = ? WHERE id = ?",
            (new_mtime, file_id),
        )
        conn.execute(
            """
            INSERT INTO update_log (file_id, operation, field_changed, old_value, new_value, timestamp, operated_by, notes)
            VALUES (?, 'update', 'mtime', ?, ?, ?, 'build_folder_databases.py', 'SHA-256 未变，仅更新 mtime')
            """,
            (file_id, old_mtime, new_mtime, now_iso()),
        )
        conn.commit()
        print(f"[跳过] SHA-256 未变（仅 mtime 更新）: {rel_path}")
        conn.close()
        return 0

    # SHA-256 变了 → 级联刷新
    print(f"[更新] 检测到内容变化，级联刷新: {rel_path}")
    t0 = time.time()

    text, raw, has_bom, line_ending = read_file_text(target)
    ext = target.suffix.lower().lstrip(".")
    meta = build_file_metadata(target, text, raw, has_bom, line_ending)
    blocks = split_blocks(text, ext)
    meta["content_hash"] = compute_content_hash(blocks)

    # 记录旧值
    old_values = {
        "sha256": old_sha,
        "mtime": old_mtime,
    }

    # 删除旧 blocks（触发器自动删除 blocks_fts）；删除旧 cross_references（级联）；
    # 删除旧扩展表记录（级联）；然后更新 files 并重新插入 blocks
    conn.execute("DELETE FROM blocks WHERE file_id = ?", (file_id,))
    conn.execute("DELETE FROM cross_references WHERE source_file_id = ?", (file_id,))
    # 删除扩展表记录（跳过当前库中不存在的扩展表——Schema 精简后部分扩展表已删除）
    existing_tables = {
        row[0]
        for row in conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        ).fetchall()
    }
    for ext_table in [
        "fact_check_records",
        "disputes",
        "peer_reviews",
        "person_index",
        "command_index",
        "term_index",
        "concept_history",
        "person_biography",
        "kaoju_records",
        "security_advisories",
        "vulnerability_metadata",
        "chapter_metadata",
        "author_index",
        "build_status",
        "timeline_records",
        "citation_frequency",
    ]:
        if ext_table in existing_tables:
            conn.execute(f"DELETE FROM {ext_table} WHERE file_id = ?", (file_id,))

    # 更新 files
    conn.execute(
        """
        UPDATE files SET
            file_size = ?, sha256 = ?, content_hash = ?, line_count = ?,
            char_count = ?, line_ending = ?, mtime = ?, ingested_at = ?,
            title = ?, summary = ?, frontmatter = ?
        WHERE id = ?
        """,
        (
            meta["file_size"],
            meta["sha256"],
            meta["content_hash"],
            meta["line_count"],
            meta["char_count"],
            meta["line_ending"],
            meta["mtime"],
            meta["ingested_at"],
            meta["title"],
            meta["summary"],
            meta["frontmatter"],
            file_id,
        ),
    )

    # 重新插入 blocks
    insert_blocks(conn, file_id, blocks)

    # 重新插入 cross_references
    refs = extract_cross_references(text, file_id)
    if refs:
        insert_cross_references(conn, refs)

    # 重新插入扩展表
    ingest_extension_tables(
        conn, db_name, file_id, rel_path, text, ext, blocks
    )

    # 写 update_log
    for field, old_val in old_values.items():
        new_val = meta.get(field, "")
        conn.execute(
            """
            INSERT INTO update_log (file_id, operation, field_changed, old_value, new_value, timestamp, operated_by, notes)
            VALUES (?, 'update', ?, ?, ?, ?, 'build_folder_databases.py', '内容变化级联刷新')
            """,
            (file_id, field, str(old_val), str(new_val), now_iso()),
        )

    conn.commit()

    # 写日志
    duration_ms = int((time.time() - t0) * 1000)
    write_build_log_entry(db_name, {
        "timestamp": now_iso(),
        "action": "file_ingested",
        "db_name": db_name,
        "file_path": rel_path,
        "file_id": file_id,
        "status": "ok",
        "message": f"Updated: {len(blocks)} blocks (cascade refresh)",
        "duration_ms": duration_ms,
    })

    print(f"[成功] 已更新: {rel_path} ({len(blocks)} blocks, {duration_ms} ms)")
    conn.close()
    return 0


# =============================================================================
# 主入口
# =============================================================================


def main() -> int:
    parser = argparse.ArgumentParser(
        description="文件夹级数据库构建脚本（7 个一级文件夹 → SQLite + FTS5）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "示例:\n"
            "  python script/build_folder_databases.py --folder 11-元数据接口\n"
            "  python script/build_folder_databases.py --all\n"
            "  python script/build_folder_databases.py --rebuild original_sources\n"
            "  python script/build_folder_databases.py --add-file 03-原始史料库/06-考据记录/xxx.md\n"
            "  python script/build_folder_databases.py --update-file 03-原始史料库/06-考据记录/xxx.md\n"
        ),
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--folder", metavar="<folder_name>", help="扫描单个文件夹并构建其数据库")
    group.add_argument("--all", action="store_true", help="按顺序构建全部 7 个数据库")
    group.add_argument("--rebuild", metavar="<db_name>", help="删除已有数据库并从零重建")
    group.add_argument("--add-file", metavar="<file_path>", help="增量添加单个文件（含去重）")
    group.add_argument("--update-file", metavar="<file_path>", help="更新已有文件（mtime 变化时级联刷新）")

    args = parser.parse_args()

    # 确保 schema SQL 存在
    if not SCHEMA_SQL_PATH.exists():
        print(f"[错误] 找不到架构 SQL: {SCHEMA_SQL_PATH}", file=sys.stderr)
        return 1

    # 确保日志目录存在
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    INDEX_DIR.mkdir(parents=True, exist_ok=True)

    if args.all:
        return mode_all()
    if args.folder:
        return mode_folder(args.folder)
    if args.rebuild:
        return mode_rebuild(args.rebuild)
    if args.add_file:
        return mode_add_file(args.add_file)
    if args.update_file:
        return mode_update_file(args.update_file)
    return 0


if __name__ == "__main__":
    sys.exit(main())
