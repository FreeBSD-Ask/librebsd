#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
跨库交叉引用解析器（resolve_cross_references.py）

功能:
    扫描 7 个文件夹级 SQLite 数据库的 blocks.block_content，识别 7 类交叉引用:
      1. wikilink        [[path]] 或 [[path|text]]
      2. markdown_link   [text](path)
      3. footnote        [^id] 引用（非定义 [^id]:）
      4. chapter_ref     第XX章 / 第N卷 / 第NN章-XX
      5. spec_ref        .trae/specs/<name>/ 或 spec `<name>`
      6. db_ref          <name>.db 数据库文件引用
      7. external_url    http://... 或 https://...
    解析目标并写入各库 cross_references 表，汇总跨库引用至
    11-元数据接口/09-文件夹数据库索引/cross_db_references.csv，
    输出失效链接清单至 script/_folder_db_logs/broken_links.md，
    更新 script/_folder_db_logs/dashboard.md 与
    11-元数据接口/09-文件夹数据库索引/dashboard.md 的跨库引用解析进度章节。

7 个数据库:
    1. 02-sacred源材料/sacred_sources.db
    2. 03-原始史料库/original_sources.db
    3. 04-现代研究文献/research_notes.db
    4. 07-事实核查记录/fact_checks.db
    5. 08-核查报告与多轮复核/review_reports.db
    6. 10-交叉索引/cross_indexes.db
    7. 11-元数据接口/metadata_interfaces.db

用法:
    python script/resolve_cross_references.py --all
    python script/resolve_cross_references.py --db original_sources

设计约束:
    - 编码: UTF-8 无 BOM, 换行符 LF
    - 依赖: Python 3.8+ 标准库（sqlite3/re/json/csv/pathlib/argparse/os/time/datetime）
    - 幂等: 每次运行先 DELETE FROM cross_references 再插入，避免重复
    - 0 信任: 外部 URL 不验证，标记为 external；内部引用检查文件/目录是否存在

退出码:
    0 = 成功
    1 = 任何错误
"""

import argparse
import csv
import os
import re
import sqlite3
import sys
import time
from datetime import datetime
from pathlib import Path

# ============================================================
# 常量定义
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

# 7 个文件夹级数据库注册表：db_name -> 相对项目根的路径
DB_REGISTRY = {
    'sacred_sources': '02-sacred源材料/sacred_sources.db',
    'original_sources': '03-原始史料库/original_sources.db',
    'research_notes': '04-现代研究文献/research_notes.db',
    'fact_checks': '07-事实核查记录/fact_checks.db',
    'review_reports': '08-核查报告与多轮复核/review_reports.db',
    'cross_indexes': '10-交叉索引/cross_indexes.db',
    'metadata_interfaces': '11-元数据接口/metadata_interfaces.db',
}

# 输出文件路径
CROSS_DB_CSV = BASE_DIR / '11-元数据接口' / '09-文件夹数据库索引' / 'cross_db_references.csv'
DASHBOARD_MAIN = BASE_DIR / '11-元数据接口' / '09-文件夹数据库索引' / 'dashboard.md'
DASHBOARD_LOG = BASE_DIR / 'script' / '_folder_db_logs' / 'dashboard.md'
BROKEN_LINKS_MD = BASE_DIR / 'script' / '_folder_db_logs' / 'broken_links.md'

# 索引源目录
OUTLINE_DIR = BASE_DIR / '05-卷册大纲'
SPECS_DIR = BASE_DIR / '.trae' / 'specs'

# 引用上下文字符数（前后各 N 字）
CONTEXT_CHARS = 50

# ============================================================
# 编译正则表达式（7 类引用模式）
# ============================================================

# Type 1: wikilink [[path]] 或 [[path|display text]]
RE_WIKILINK = re.compile(r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]')

# Type 2: markdown link [display text](path)
RE_MARKDOWN_LINK = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

# Type 3: footnote reference [^id]（排除定义 [^id]:）
RE_FOOTNOTE = re.compile(r'\[\^([^\]]+)\](?!\s*:)')

# Type 4: chapter ref 第XX章（阿拉伯数字或中文数字）
RE_CHAPTER = re.compile(r'第(\d+|[零一二三四五六七八九十百千]+)章')

# Type 4b: volume ref 第N卷
RE_VOLUME = re.compile(r'第(\d+|[零一二三四五六七八九十百千]+)卷')

# Type 5: spec ref .trae/specs/<name>/
RE_SPEC_PATH = re.compile(r'\.trae/specs/([a-z0-9][a-z0-9-]*)/')

# Type 5b: spec ref `spec `<name>`` 或 `specification `<name>``
RE_SPEC_BACKTICK = re.compile(r'(?:spec|specification)\s+`([a-z0-9][a-z0-9-]*)`')

# Type 6: db ref <name>.db（\w 含 Unicode 字母，可匹配中文数据库名）
RE_DB = re.compile(r'([\w]+\.db)\b')

# Type 7: external URL http://... 或 https://...
RE_URL = re.compile(r'https?://[^\s\)]+')

# ============================================================
# 中文数字转换
# ============================================================

CN_DIGITS = {
    '零': 0, '一': 1, '二': 2, '三': 3, '四': 4,
    '五': 5, '六': 6, '七': 7, '八': 8, '九': 9,
}
CN_UNITS = {'十': 10, '百': 100, '千': 1000}


def cn2num(s):
    """将中文数字字符串转换为 int。无法转换时返回 None。

    支持示例:
        '52' -> 52
        '五十二' -> 52
        '一百六十八' -> 168
        '十' -> 10
        '二十' -> 20
    """
    if not s:
        return None
    if s.isdigit():
        return int(s)
    result = 0
    current = 0
    for ch in s:
        if ch in CN_DIGITS:
            current = CN_DIGITS[ch]
        elif ch in CN_UNITS:
            if current == 0:
                current = 1
            result += current * CN_UNITS[ch]
            current = 0
        else:
            return None
    result += current
    return result if result > 0 else None


# ============================================================
# 索引构建
# ============================================================

def build_chapter_index(outline_dir):
    """扫描 05-卷册大纲/，构建 chapter_num(int) -> relative_path(str) 映射。

    匹配 第NN卷-*/ 下的 第XX章-*/ 文件夹（仅普通章，不含字母后缀章）。
    """
    index = {}
    if not outline_dir.exists():
        return index
    try:
        for vol_dir in sorted(outline_dir.iterdir()):
            if not vol_dir.is_dir() or not vol_dir.name.startswith('第'):
                continue
            if not re.match(r'第\d+卷', vol_dir.name):
                continue
            for ch_dir in sorted(vol_dir.iterdir()):
                if not ch_dir.is_dir() or not ch_dir.name.startswith('第'):
                    continue
                m = re.match(r'第(\d+)章', ch_dir.name)
                if m:
                    ch_num = int(m.group(1))
                    rel_path = str(ch_dir.relative_to(outline_dir.parent)).replace('\\', '/')
                    if ch_num not in index:
                        index[ch_num] = rel_path
    except OSError:
        pass
    return index


def build_volume_index(outline_dir):
    """扫描 05-卷册大纲/，构建 volume_num(int) -> relative_path(str) 映射。"""
    index = {}
    if not outline_dir.exists():
        return index
    try:
        for vol_dir in sorted(outline_dir.iterdir()):
            if not vol_dir.is_dir() or not vol_dir.name.startswith('第'):
                continue
            m = re.match(r'第(\d+)卷', vol_dir.name)
            if m:
                vol_num = int(m.group(1))
                rel_path = str(vol_dir.relative_to(outline_dir.parent)).replace('\\', '/')
                index[vol_num] = rel_path
    except OSError:
        pass
    return index


def find_all_db_files(base_dir):
    """扫描项目内所有 .db 文件，构建 filename -> relative_path 映射。

    跳过 .trae/ 与 caj2pdf/ 目录下的 .db 文件。
    """
    db_files = {}
    try:
        for path in base_dir.rglob('*.db'):
            parts = set(path.parts)
            if '.trae' in parts or 'caj2pdf' in parts:
                continue
            try:
                rel = str(path.relative_to(base_dir)).replace('\\', '/')
                db_files[path.name] = rel
            except ValueError:
                pass
    except OSError:
        pass
    return db_files


# ============================================================
# 目标解析函数
# ============================================================

def resolve_relative_path(path, source_file_path, base_dir):
    """解析相对路径，返回 (resolution_status, resolved_path)。

    - path 以 # 开头：锚点引用，返回 ('resolved', path)
    - path 以 http/https/mailto 开头：返回 ('external', path)
    - 否则：相对源文件目录解析，检查文件是否存在
    """
    if not path:
        return 'broken', path
    if path.startswith('#'):
        return 'resolved', path
    if path.startswith(('http://', 'https://', 'mailto:')):
        return 'external', path

    try:
        source_dir = (base_dir / source_file_path).parent
        target = (source_dir / path).resolve()
    except (OSError, ValueError):
        return 'broken', path

    if target.exists():
        try:
            rel = str(target.relative_to(base_dir.resolve())).replace('\\', '/')
            return 'resolved', rel
        except ValueError:
            return 'resolved', str(target).replace('\\', '/')
    return 'broken', path


def resolve_footnote(fn_id, file_content):
    """检查脚注定义是否存在于文件内容中。返回 'resolved' 或 'broken'。"""
    pattern = re.compile(r'\[\^' + re.escape(fn_id) + r'\]\s*:')
    if pattern.search(file_content):
        return 'resolved'
    return 'broken'


def resolve_chapter(ch_num, chapter_index):
    """解析章节号到章节文件夹路径。返回 (status, path)。"""
    if ch_num in chapter_index:
        return 'resolved', chapter_index[ch_num]
    return 'broken', None


def resolve_volume(vol_num, volume_index):
    """解析卷号到卷文件夹路径。返回 (status, path)。"""
    if vol_num in volume_index:
        return 'resolved', volume_index[vol_num]
    return 'broken', None


def resolve_spec(spec_name, base_dir):
    """检查 spec 目录是否存在。返回 'resolved' 或 'broken'。"""
    spec_dir = base_dir / '.trae' / 'specs' / spec_name
    if spec_dir.exists() and spec_dir.is_dir():
        return 'resolved'
    return 'broken'


def resolve_db(db_filename, db_files_index):
    """检查 .db 文件是否存在于项目中。返回 (status, path)。"""
    if db_filename in db_files_index:
        return 'resolved', db_files_index[db_filename]
    return 'broken', None


# ============================================================
# 引用扫描
# ============================================================

def extract_context(content, start, end, chars=CONTEXT_CHARS):
    """提取匹配位置前后的上下文（各 chars 字符）。"""
    ctx_start = max(0, start - chars)
    ctx_end = min(len(content), end + chars)
    return content[ctx_start:ctx_end]


def scan_block(block_id, file_id, file_path, block_content, file_content,
               chapter_index, volume_index, db_files_index, base_dir):
    """扫描单个 block 的内容，识别全部 7 类交叉引用。

    返回引用字典列表，每个字典对应 cross_references 表一行。
    """
    refs = []
    now = datetime.now().isoformat()
    src_dir_for_rel = file_path

    # --- Type 1: wikilink [[path]] 或 [[path|text]] ---
    for m in RE_WIKILINK.finditer(block_content):
        target_path = m.group(1)
        ref_text = m.group(0)
        status, resolved = resolve_relative_path(target_path, src_dir_for_rel, base_dir)
        refs.append({
            'source_file_id': file_id,
            'source_block_id': block_id,
            'reference_type': 'wikilink',
            'reference_text': ref_text,
            'target_path': resolved or target_path,
            'target_db': None,
            'target_record_id': None,
            'target_anchor': None,
            'resolution_status': status,
            'reference_context': extract_context(block_content, m.start(), m.end()),
            'resolved_at': now if status in ('resolved', 'broken', 'external') else None,
        })

    # --- Type 2: markdown link [text](path) ---
    for m in RE_MARKDOWN_LINK.finditer(block_content):
        path = m.group(2)
        if path.startswith(('http://', 'https://')):
            continue  # 跳过，由 external_url 捕获
        ref_text = m.group(0)
        status, resolved = resolve_relative_path(path, src_dir_for_rel, base_dir)
        refs.append({
            'source_file_id': file_id,
            'source_block_id': block_id,
            'reference_type': 'markdown_link',
            'reference_text': ref_text,
            'target_path': resolved or path,
            'target_db': None,
            'target_record_id': None,
            'target_anchor': None,
            'resolution_status': status,
            'reference_context': extract_context(block_content, m.start(), m.end()),
            'resolved_at': now if status in ('resolved', 'broken', 'external') else None,
        })

    # --- Type 3: footnote [^id]（非定义） ---
    for m in RE_FOOTNOTE.finditer(block_content):
        fn_id = m.group(1)
        ref_text = m.group(0)
        status = resolve_footnote(fn_id, file_content)
        refs.append({
            'source_file_id': file_id,
            'source_block_id': block_id,
            'reference_type': 'footnote',
            'reference_text': ref_text,
            'target_path': None,
            'target_db': None,
            'target_record_id': None,
            'target_anchor': fn_id,
            'resolution_status': status,
            'reference_context': extract_context(block_content, m.start(), m.end()),
            'resolved_at': now if status in ('resolved', 'broken') else None,
        })

    # --- Type 4: chapter ref 第XX章 ---
    for m in RE_CHAPTER.finditer(block_content):
        ch_num_str = m.group(1)
        ch_num = cn2num(ch_num_str)
        ref_text = m.group(0)
        if ch_num is not None:
            status, path = resolve_chapter(ch_num, chapter_index)
        else:
            status, path = 'broken', None
        refs.append({
            'source_file_id': file_id,
            'source_block_id': block_id,
            'reference_type': 'chapter_ref',
            'reference_text': ref_text,
            'target_path': path,
            'target_db': None,
            'target_record_id': None,
            'target_anchor': None,
            'resolution_status': status,
            'reference_context': extract_context(block_content, m.start(), m.end()),
            'resolved_at': now if status in ('resolved', 'broken') else None,
        })

    # --- Type 4b: volume ref 第N卷（归入 chapter_ref 类型） ---
    for m in RE_VOLUME.finditer(block_content):
        vol_num_str = m.group(1)
        vol_num = cn2num(vol_num_str)
        ref_text = m.group(0)
        if vol_num is not None:
            status, path = resolve_volume(vol_num, volume_index)
        else:
            status, path = 'broken', None
        refs.append({
            'source_file_id': file_id,
            'source_block_id': block_id,
            'reference_type': 'chapter_ref',
            'reference_text': ref_text,
            'target_path': path,
            'target_db': None,
            'target_record_id': None,
            'target_anchor': None,
            'resolution_status': status,
            'reference_context': extract_context(block_content, m.start(), m.end()),
            'resolved_at': now if status in ('resolved', 'broken') else None,
        })

    # --- Type 5: spec ref .trae/specs/<name>/ ---
    for m in RE_SPEC_PATH.finditer(block_content):
        spec_name = m.group(1)
        ref_text = m.group(0)
        status = resolve_spec(spec_name, base_dir)
        refs.append({
            'source_file_id': file_id,
            'source_block_id': block_id,
            'reference_type': 'spec_ref',
            'reference_text': ref_text,
            'target_path': '.trae/specs/' + spec_name + '/',
            'target_db': None,
            'target_record_id': None,
            'target_anchor': None,
            'resolution_status': status,
            'reference_context': extract_context(block_content, m.start(), m.end()),
            'resolved_at': now if status in ('resolved', 'broken') else None,
        })

    # --- Type 5b: spec ref `spec `<name>`` ---
    for m in RE_SPEC_BACKTICK.finditer(block_content):
        spec_name = m.group(1)
        ref_text = m.group(0)
        status = resolve_spec(spec_name, base_dir)
        refs.append({
            'source_file_id': file_id,
            'source_block_id': block_id,
            'reference_type': 'spec_ref',
            'reference_text': ref_text,
            'target_path': '.trae/specs/' + spec_name + '/',
            'target_db': None,
            'target_record_id': None,
            'target_anchor': None,
            'resolution_status': status,
            'reference_context': extract_context(block_content, m.start(), m.end()),
            'resolved_at': now if status in ('resolved', 'broken') else None,
        })

    # --- Type 6: db ref <name>.db ---
    for m in RE_DB.finditer(block_content):
        db_filename = m.group(1)
        db_name = db_filename[:-3]  # 去除 .db 扩展名
        ref_text = m.group(0)
        status, path = resolve_db(db_filename, db_files_index)
        refs.append({
            'source_file_id': file_id,
            'source_block_id': block_id,
            'reference_type': 'db_ref',
            'reference_text': ref_text,
            'target_path': path,
            'target_db': db_name,
            'target_record_id': None,
            'target_anchor': None,
            'resolution_status': status,
            'reference_context': extract_context(block_content, m.start(), m.end()),
            'resolved_at': now if status in ('resolved', 'broken') else None,
        })

    # --- Type 7: external URL http://... 或 https://... ---
    for m in RE_URL.finditer(block_content):
        url = m.group(0)
        refs.append({
            'source_file_id': file_id,
            'source_block_id': block_id,
            'reference_type': 'external_url',
            'reference_text': url,
            'target_path': url,
            'target_db': None,
            'target_record_id': None,
            'target_anchor': None,
            'resolution_status': 'external',
            'reference_context': extract_context(block_content, m.start(), m.end()),
            'resolved_at': now,
        })

    return refs


# ============================================================
# 数据库处理
# ============================================================

# cross_references 表 DDL（与 folder_db_common_schema.sql 一致）
CREATE_XREF_SQL = """
CREATE TABLE IF NOT EXISTS cross_references (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_file_id INTEGER NOT NULL,
    source_block_id INTEGER,
    reference_type TEXT NOT NULL,
    reference_text TEXT NOT NULL,
    target_path TEXT,
    target_db TEXT,
    target_record_id INTEGER,
    target_anchor TEXT,
    resolution_status TEXT NOT NULL DEFAULT 'pending',
    reference_context TEXT,
    resolved_at TEXT,
    FOREIGN KEY (source_file_id) REFERENCES files(id) ON DELETE CASCADE,
    FOREIGN KEY (source_block_id) REFERENCES blocks(id) ON DELETE SET NULL
);
"""


def table_exists(conn, table_name):
    """检查数据库中是否存在指定表。"""
    cur = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
        (table_name,)
    )
    return cur.fetchone() is not None


def process_database(db_name, db_rel_path, chapter_index, volume_index,
                     db_files_index, base_dir):
    """处理单个数据库：扫描 blocks，识别引用，更新 cross_references 表。

    返回 (total_refs, broken_links, cross_db_refs, status_counts, file_paths)。
    """
    db_path = base_dir / db_rel_path
    if not db_path.exists():
        print('数据库不存在，跳过')
        return 0, [], [], {}, {}

    conn = sqlite3.connect(str(db_path))
    conn.execute('PRAGMA foreign_keys = OFF')

    # 检查 blocks 表是否存在
    if not table_exists(conn, 'blocks'):
        print('无 blocks 表，跳过')
        conn.close()
        return 0, [], [], {}, {}

    # 确保 cross_references 表存在
    conn.execute(CREATE_XREF_SQL)

    # 清空既有引用记录（幂等）
    conn.execute('DELETE FROM cross_references')

    # 预加载所有 blocks（按 file_id, block_index 排序）
    cur = conn.execute(
        'SELECT id, file_id, block_content FROM blocks ORDER BY file_id, block_index'
    )
    blocks_data = cur.fetchall()

    # 构建 file_id -> 拼接内容（用于脚注定义查找）
    file_to_blocks = {}
    for block_id, file_id, content in blocks_data:
        if file_id not in file_to_blocks:
            file_to_blocks[file_id] = []
        file_to_blocks[file_id].append((block_id, content))

    file_contents = {}
    for file_id, blocks_list in file_to_blocks.items():
        file_contents[file_id] = '\n'.join(c for _, c in blocks_list)

    # 获取 file_id -> file_path 映射
    cur = conn.execute('SELECT id, file_path FROM files')
    file_paths = {row[0]: row[1] for row in cur.fetchall()}

    # 扫描所有 blocks
    all_refs = []
    for block_id, file_id, block_content in blocks_data:
        file_path = file_paths.get(file_id, '')
        file_content = file_contents.get(file_id, '')
        refs = scan_block(
            block_id, file_id, file_path, block_content, file_content,
            chapter_index, volume_index, db_files_index, base_dir
        )
        all_refs.extend(refs)

    # 批量插入 cross_references
    insert_rows = [
        (ref['source_file_id'], ref['source_block_id'], ref['reference_type'],
         ref['reference_text'], ref['target_path'], ref['target_db'],
         ref['target_record_id'], ref['target_anchor'],
         ref['resolution_status'], ref['reference_context'], ref['resolved_at'])
        for ref in all_refs
    ]
    try:
        conn.executemany(
            '''INSERT INTO cross_references
               (source_file_id, source_block_id, reference_type, reference_text,
                target_path, target_db, target_record_id, target_anchor,
                resolution_status, reference_context, resolved_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            insert_rows
        )
        conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        print('插入失败: ' + str(e))
        conn.close()
        return 0, [], [], {}, file_paths

    conn.close()

    # 统计状态计数
    status_counts = {'resolved': 0, 'broken': 0, 'external': 0, 'pending': 0}
    for ref in all_refs:
        status = ref['resolution_status']
        status_counts[status] = status_counts.get(status, 0) + 1

    # 收集失效链接与跨库引用
    broken_links = []
    cross_db_refs = []
    for ref in all_refs:
        if ref['resolution_status'] == 'broken':
            broken_links.append({
                'db_name': db_name,
                'source_file_path': file_paths.get(ref['source_file_id'], ''),
                'reference_text': ref['reference_text'],
                'target_path': ref['target_path'] or '',
                'reference_type': ref['reference_type'],
            })
        if ref['target_db'] and ref['target_db'] != db_name:
            cross_db_refs.append({
                'source_db': db_name,
                'source_file_id': ref['source_file_id'],
                'source_block_id': ref['source_block_id'],
                'target_db': ref['target_db'],
                'target_record_id': ref['target_record_id'],
                'target_path': ref['target_path'] or '',
                'reference_type': ref['reference_type'],
                'resolution_status': ref['resolution_status'],
            })

    return len(all_refs), broken_links, cross_db_refs, status_counts, file_paths


# ============================================================
# 输出函数
# ============================================================

def write_cross_db_csv(cross_db_refs):
    """重写 cross_db_references.csv（截断后写入表头 + 全部跨库引用行）。"""
    CROSS_DB_CSV.parent.mkdir(parents=True, exist_ok=True)
    with open(CROSS_DB_CSV, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            'source_db', 'source_file_id', 'source_block_id',
            'target_db', 'target_record_id', 'target_path',
            'reference_type', 'resolution_status'
        ])
        for ref in cross_db_refs:
            writer.writerow([
                ref['source_db'],
                ref['source_file_id'],
                ref['source_block_id'] if ref['source_block_id'] is not None else '',
                ref['target_db'],
                ref['target_record_id'] if ref['target_record_id'] is not None else '',
                ref['target_path'],
                ref['reference_type'],
                ref['resolution_status'],
            ])


def write_broken_links(broken_links):
    """写入 broken_links.md，按数据库分组列出所有失效引用。"""
    now = datetime.now().isoformat()
    lines = [
        '# 失效链接清单',
        '',
        '> 生成时间：' + now,
        '> 失效链接总数：' + str(len(broken_links)),
        '',
        '## 按 数据库分组',
        '',
    ]

    # 按数据库分组
    by_db = {}
    for link in broken_links:
        by_db.setdefault(link['db_name'], []).append(link)

    # 按 DB_REGISTRY 顺序输出
    for db_name in DB_REGISTRY.keys():
        if db_name not in by_db:
            continue
        lines.append('### ' + db_name)
        lines.append('')
        lines.append('| 源文件 | 引用文本 | 目标路径 | 引用类型 |')
        lines.append('| --- | --- | --- | --- |')
        for link in by_db[db_name]:
            file_path = link['source_file_path'] or ('id:' + str(link.get('source_file_id', '')))
            # 转义表格分隔符与换行
            ref_text = link['reference_text'].replace('|', '\\|').replace('\n', ' ')
            target = (link['target_path'] or '').replace('|', '\\|').replace('\n', ' ')
            lines.append('| ' + file_path + ' | ' + ref_text + ' | ' + target + ' | ' + link['reference_type'] + ' |')
        lines.append('')

    # 若无失效链接
    if not broken_links:
        lines.append('（暂无失效链接记录）')
        lines.append('')

    BROKEN_LINKS_MD.parent.mkdir(parents=True, exist_ok=True)
    BROKEN_LINKS_MD.write_text('\n'.join(lines), encoding='utf-8', newline='\n')


def update_dashboard(stats):
    """更新两个 dashboard.md 的"跨库引用解析进度"章节。

    stats: dict with keys 'resolved', 'broken', 'external', 'pending'
    """
    new_section_lines = [
        '## 跨库引用解析进度',
        '',
        '- 状态：completed',
        '- 已解析（resolved）：' + str(stats.get('resolved', 0)),
        '- 失效（broken）：' + str(stats.get('broken', 0)),
        '- 外部（external）：' + str(stats.get('external', 0)),
        '- 待解析（pending）：' + str(stats.get('pending', 0)),
        '- 跨库引用映射：`cross_db_references.csv`',
        '- 失效链接清单：`script/_folder_db_logs/broken_links.md`',
    ]
    new_section = '\n'.join(new_section_lines)

    for dashboard_path in [DASHBOARD_MAIN, DASHBOARD_LOG]:
        if not dashboard_path.exists():
            continue
        try:
            content = dashboard_path.read_text(encoding='utf-8')
        except OSError:
            continue

        lines = content.split('\n')
        start_idx = None
        end_idx = len(lines)
        for i, line in enumerate(lines):
            if line.strip() == '## 跨库引用解析进度':
                start_idx = i
            elif start_idx is not None and line.startswith('## ') and i > start_idx:
                end_idx = i
                break

        if start_idx is not None:
            new_lines = lines[:start_idx] + new_section.split('\n') + lines[end_idx:]
            new_content = '\n'.join(new_lines)
        else:
            # 章节不存在，追加到末尾
            new_content = content.rstrip('\n') + '\n\n' + new_section + '\n'

        dashboard_path.write_text(new_content, encoding='utf-8', newline='\n')


# ============================================================
# 主函数
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description='跨库交叉引用解析器：扫描文件夹级数据库，识别并解析 7 类交叉引用',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            '示例:\n'
            '  python script/resolve_cross_references.py --all\n'
            '  python script/resolve_cross_references.py --db original_sources\n'
            '\n'
            '可选数据库名:\n'
            '  ' + ', '.join(DB_REGISTRY.keys())
        )
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--all', action='store_true', help='处理全部 7 个数据库')
    group.add_argument(
        '--db', metavar='<db_name>',
        choices=list(DB_REGISTRY.keys()),
        help='处理单个数据库'
    )

    args = parser.parse_args()

    start_time = time.time()

    # 确定处理范围
    if args.all:
        db_list = list(DB_REGISTRY.items())
    else:
        db_list = [(args.db, DB_REGISTRY[args.db])]

    # 构建索引
    print('[索引] 构建章节索引...')
    chapter_index = build_chapter_index(OUTLINE_DIR)
    print('  章节索引: ' + str(len(chapter_index)) + ' 条')

    print('[索引] 构建卷索引...')
    volume_index = build_volume_index(OUTLINE_DIR)
    print('  卷索引: ' + str(len(volume_index)) + ' 条')

    print('[索引] 扫描项目 .db 文件...')
    db_files_index = find_all_db_files(BASE_DIR)
    print('  .db 文件: ' + str(len(db_files_index)) + ' 个')

    # 处理各数据库
    all_broken_links = []
    all_cross_db_refs = []
    total_stats = {'resolved': 0, 'broken': 0, 'external': 0, 'pending': 0}
    total_db_count = len(db_list)
    processed_count = 0
    has_error = False

    for i, (db_name, db_rel_path) in enumerate(db_list, 1):
        prefix = '[' + str(i) + '/' + str(total_db_count) + '] Scanning ' + db_name + '.db...'
        print(prefix, end=' ', flush=True)
        try:
            total_refs, broken, cross_db, status_counts, _ = process_database(
                db_name, db_rel_path, chapter_index, volume_index,
                db_files_index, BASE_DIR
            )
            print('[' + str(total_refs) + ' refs found]')
            all_broken_links.extend(broken)
            all_cross_db_refs.extend(cross_db)
            for k in total_stats:
                total_stats[k] += status_counts.get(k, 0)
            processed_count += 1
        except Exception as e:
            print('[ERROR] ' + str(e))
            has_error = True

    # 输出跨库引用 CSV
    print('[输出] 写入 cross_db_references.csv... (' + str(len(all_cross_db_refs)) + ' 条跨库引用)')
    try:
        write_cross_db_csv(all_cross_db_refs)
    except OSError as e:
        print('[ERROR] 写入 cross_db_references.csv 失败: ' + str(e))
        has_error = True

    # 输出失效链接清单
    print('[输出] 写入 broken_links.md... (' + str(len(all_broken_links)) + ' 条失效链接)')
    try:
        write_broken_links(all_broken_links)
    except OSError as e:
        print('[ERROR] 写入 broken_links.md 失败: ' + str(e))
        has_error = True

    # 更新看板
    print('[输出] 更新 dashboard.md...')
    try:
        update_dashboard(total_stats)
    except OSError as e:
        print('[ERROR] 更新 dashboard.md 失败: ' + str(e))
        has_error = True

    elapsed = time.time() - start_time
    print('')
    print('=== 汇总 ===')
    print('已处理数据库: ' + str(processed_count) + '/' + str(total_db_count))
    print('已解析(resolved): ' + str(total_stats['resolved']))
    print('失效(broken): ' + str(total_stats['broken']))
    print('外部(external): ' + str(total_stats['external']))
    print('待解析(pending): ' + str(total_stats['pending']))
    print('跨库引用: ' + str(len(all_cross_db_refs)))
    print('耗时: ' + str(round(elapsed, 2)) + ' 秒')

    if has_error:
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
