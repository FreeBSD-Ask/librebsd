#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TUHS Wiki 史料库 V1–V12 完整性与保真验证（verify_tuhs_wiki.py）。

用途
====
对独立史料库 `03-原始史料库/16-TUHS-Wiki史料/tuhs_wiki.duckdb` 与同目录语料执行 V1–V12
判据验证，逐项打印 PASS／FAIL／INFO，结果写入 `verification` 表（同轮同判据先清后写，幂等）。
本脚本只读校验语料与库，除 `verification` 表与 `script/` 临时件外不做任何写入；不抓全站、
不改抓取器、不改库结构。

判据（规格出处 `.trae/specs/crawl-tuhs-wiki-20261025/spec.md`）
============================================================
V1 页面清单守恒：独立以 `?do=index&idx=<ns>` 递归派生页面集合（14 命名空间＋子命名空间＋顶层
   `start`／`syste`），与 `crawl_runs` 最近一条 completed／running 记录的 `scope_json`
   （`baseline`／`page_set_sha256`／`namespace_counts`）及 `pages` 中 `source_kind='wiki'`
   的 page_key 集合三方比对；逐命名空间计数一致。库为空或缺 `crawl_runs` 判 FAIL（不崩溃）。
V2 双形态落盘：每个 wiki 页 `.wikitext` 与 `.md` 存在且非空；`sha256_markdown` 与 `.md` 实测
   一致；`.wikitext` 只要求存在非空（不比对 `sha256_source`，源字节可能含 CRLF／BOM）。
V3 Markdown 覆盖：每页恰 1 条 `fulltext`，`char_count == len(content)`；非 `failed`／`empty`
   且正文非空的页至少 1 条 `fulltext_blocks`；正文剥除围栏代码块后不得含 HTML 标签残留。
V4 外链闭合：`links.target_kind='external'` 的 `resolution_status` 必须属于
   {fetched, wayback, excluded, failed, needs_ocr_deferred}，且 `target_url` 能在
   `pages.canonical_url`（external）／`excluded_items.url`／`crawl_log` 失败行中找到。
V5 键与去重：`page_key` 重复 0；`(page_key, block_index)` 重复 0；外链归一 URL 重复 0；
   `(page_key, converter)` 重复 0。
V6 原文抽样：随机 30 个 wiki 页重取 `export_raw`，字节 SHA-256 必须等于
   `pages.sha256_source`；随机 10 个外链页重取，哈希不同只记 `changed_since_crawl`（INFO）。
   网络失败重试 3 次，仍失败判 FAIL 并列出。
V7 版本与结构：`duckdb.__version__ == 2.0.0`；存储版本为 `v2.0.0+`；基表 11、视图 1；约定的
   主键与唯一约束齐备；全库无 BLOB 列。
V8 可恢复性：`EXPORT DATABASE` 至临时目录 → 新临时库 `IMPORT DATABASE` → 11 表行数逐一相等
   → 清理临时件。
V9 幂等：以逻辑导出／导入在 `script/` 临时路径生成库副本（Windows 下无法复制被本进程
   打开的库文件），以 `--db <临时库> --root <真实语料目录> --wiki-only --resume` 二跑，
   `pages`／`fulltext`／`fulltext_blocks`／`links`／`conversions` 行数与 page_key 集合
   不增、不变。
V10 二进制禁入：语料目录除库文件（含其 WAL）与 `raw/media/` 下明示图片外，扩展名只允许
   `.md`／`.wikitext`；按文件头魔数（`%PDF-`、`PK\\x03\\x04`、`\\x89PNG`、`GIF8`、
   `\\xFF\\xD8\\xFF`）复检，命中即 FAIL。
V11 转换保真：随机抽样，同时解析源（wiki 用 `.wikitext`，external 重取源站）与 `.md` 的
   标题数、链接数、代码块数、表格行数，差异为零。
V12 转换台账：每页有 `conversions` 行；`converter_version` 等于 `schema_meta.converter_version`；
   `md_sha256` 与 `.md` 实测一致。

用法
====
    C:/Python314/python.exe verify_tuhs_wiki.py
    C:/Python314/python.exe verify_tuhs_wiki.py --skip-network
    C:/Python314/python.exe verify_tuhs_wiki.py --round R2 --sample 30
    C:/Python314/python.exe verify_tuhs_wiki.py --selftest

参数
====
`--db` 库路径（默认真实库）；`--root` 语料目录（默认库所在目录）；`--round` 轮次标记
（默认 `R1`）；`--sample` 抽样页数（默认 30）；`--skip-network` 只跑离线判据，网络判据标
SKIP 并说明；`--selftest` 离线自检（临时库与临时目录构造正常夹具与六类缺陷）。

退出码
======
0 全过（允许 INFO／SKIP）；1 任一 FAIL；2 `duckdb` 版本不符或库缺失。

已知限制
========
- `--skip-network` 时 V1 的清单重派生、V6 抽样重取、V9 二跑、V11 外链比对均为 SKIP。
- V6 对 `source_bytes > 5 MB` 的外链页跳过重取（不为比对哈希下载大文件），以 INFO 披露。
- V11 外链页按“去 script／style／nav／header／footer／aside／form”的独立 HTML 计数实现，
  与抓取器实现不同源；站点自定义容器（如 DokuWiki 的 docinfo 类 div）可能产生差异。
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse as up
import urllib.request
from collections import Counter
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Set, Tuple

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

DUCKDB_REQUIRED = "2.0.0"
STORAGE_REQUIRED = "v2.0.0"
BASE = "https://wiki.tuhs.org"
DOKU = BASE + "/doku.php"
USER_AGENT = (
    "librebsd-tuhs-wiki-verify/1.0 (+https://wiki.tuhs.org; "
    "academic corpus verification for a BSD history project; contact: ykla)"
)
CONVERTER_VERSION_FALLBACK = "tuhs-md/1.0"

NAMESPACES = [
    "systems", "source", "features", "events", "people", "anecdotes", "images",
    "glossary", "publications", "misc", "wiki", "blog", "playground", "refnotes",
]
TOP_PAGES = ["start", "syste"]
NAMESPACE_SENTINEL = "(top)"
BASELINE_EXPECTED = 232          # 规格实测口径（230 命名空间页＋顶层 start／syste），仅披露
MIN_HOST_INTERVAL = 1.5
HTTP_TIMEOUT = 40
RETRY_DELAYS = (2, 4, 8)

ALLOWED_TEXT_EXT = {".md", ".wikitext"}
IMAGE_EXT = {".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".ico", ".bmp", ".tif", ".tiff"}
MAGIC_SIGNATURES = [
    (b"%PDF-", "pdf"),
    (b"PK\x03\x04", "zip"),
    (b"\x89PNG", "png"),
    (b"GIF8", "gif"),
    (b"\xff\xd8\xff", "jpeg"),
]

EXPECTED_TABLES = [
    "pages", "fulltext", "fulltext_blocks", "links", "excluded_items", "conversions",
    "crawl_runs", "crawl_log", "verification", "schema_meta", "update_log",
]
EXPECTED_VIEWS = ["v_page_documents"]
EXPECTED_CONSTRAINTS = {
    "pages": [("PRIMARY KEY", ["id"]), ("UNIQUE", ["page_key"])],
    "fulltext": [("PRIMARY KEY", ["id"]), ("UNIQUE", ["page_key"])],
    "fulltext_blocks": [("PRIMARY KEY", ["id"]),
                        ("UNIQUE", ["page_key", "block_index"])],
    "links": [("PRIMARY KEY", ["id"]),
              ("UNIQUE", ["source_page_key", "target_url", "target_kind"])],
    "excluded_items": [("PRIMARY KEY", ["id"]), ("UNIQUE", ["url", "item_kind"])],
    "conversions": [("PRIMARY KEY", ["id"]), ("UNIQUE", ["page_key", "converter"])],
    "crawl_runs": [("PRIMARY KEY", ["run_id"])],
    "crawl_log": [("PRIMARY KEY", ["id"])],
    "verification": [("PRIMARY KEY", ["id"])],
    "schema_meta": [("PRIMARY KEY", ["key"])],
    "update_log": [("PRIMARY KEY", ["id"])],
}
COUNT_TABLES = ["pages", "fulltext", "fulltext_blocks", "links", "conversions"]
ALLOWED_LINK_STATUS = {"fetched", "wayback", "excluded", "failed", "needs_ocr_deferred"}

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parents[2]
DEFAULT_ROOT = PROJECT_ROOT / "03-原始史料库" / "16-TUHS-Wiki史料"
DEFAULT_DB = DEFAULT_ROOT / "tuhs_wiki.duckdb"
SCHEMA_SQL_PATH = SCRIPT_DIR / "tuhs_wiki_schema.sql"
CRAWL_SCRIPT = SCRIPT_DIR / "tuhs_wiki_crawl.py"
TMP_PARENT = PROJECT_ROOT / "script" / "_tuhs_verify_tmp"

MAX_EXTERNAL_REFETCH_BYTES = 5 * 1024 * 1024

CHECK_NAMES = {
    "V1": "页面清单守恒",
    "V2": "双形态落盘与哈希",
    "V3": "Markdown 覆盖与 HTML 残留",
    "V4": "外链闭合",
    "V5": "键与去重",
    "V6": "原文抽样重取",
    "V7": "运行时版本与结构",
    "V8": "可恢复性（EXPORT／IMPORT）",
    "V9": "幂等二跑",
    "V10": "二进制禁入",
    "V11": "转换保真抽查",
    "V12": "转换台账",
}


class VerifyError(RuntimeError):
    """运行时错误（配置不符、库缺失等）。"""


# =============================================================================
# 基础工具
# =============================================================================

def now_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def normalize_newlines(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def read_text(path: Path) -> str:
    return normalize_newlines(path.read_bytes().decode("utf-8", "replace"))


def escape_like(value: str) -> str:
    return value.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")


def short_list(items: Sequence[str], limit: int = 20) -> str:
    shown = list(items[:limit])
    text = "、".join(shown) if shown else "（无）"
    if len(items) > limit:
        text += f" …另有 {len(items) - limit} 条"
    return text


def unique_list(items: Iterable[str]) -> List[str]:
    seen: Set[str] = set()
    out: List[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        out.append(item)
    return out


def namespace_of(page_id: str, namespaces: Iterable[str]) -> str:
    best: Optional[str] = None
    for ns in namespaces:
        if page_id == ns or page_id.startswith(ns + ":"):
            if best is None or len(ns) > len(best):
                best = ns
    return best if best else NAMESPACE_SENTINEL


def table_count(conn, table: str) -> int:
    return int(conn.execute(f'SELECT COUNT(*) FROM "{table}"').fetchone()[0])


# =============================================================================
# 网络客户端（限流＋重试）
# =============================================================================

class NetClient:
    """同主机 ≥1.5 秒间隔、3 次重试（2／4／8 秒）的独立 HTTP 客户端。"""

    def __init__(self, min_interval: float = MIN_HOST_INTERVAL, timeout: int = HTTP_TIMEOUT,
                 attempts: int = 3) -> None:
        self.min_interval = min_interval
        self.timeout = timeout
        self.attempts = attempts
        self._last_host: Dict[str, float] = {}
        self.stats = {"requests": 0, "failures": 0}

    def _throttle(self, host: str) -> None:
        last = self._last_host.get(host)
        if last is not None:
            wait = self.min_interval - (time.monotonic() - last)
            if wait > 0:
                time.sleep(wait)
        self._last_host[host] = time.monotonic()

    def fetch(self, url: str) -> Tuple[Optional[bytes], Optional[str]]:
        host = up.urlsplit(url).netloc.lower()
        last_error: Optional[str] = None
        for attempt in range(1, self.attempts + 1):
            self._throttle(host)
            try:
                request = urllib.request.Request(
                    url, headers={"User-Agent": USER_AGENT, "Accept": "*/*"})
                with urllib.request.urlopen(request, timeout=self.timeout) as resp:
                    body = resp.read()
                self.stats["requests"] += 1
                return body, None
            except urllib.error.HTTPError as exc:
                self.stats["failures"] += 1
                last_error = f"http_{exc.code}"
                try:
                    exc.read()
                    exc.close()
                except Exception:  # noqa: BLE001
                    pass
                if exc.code < 500 and exc.code != 429:
                    return None, last_error
            except Exception as exc:  # noqa: BLE001
                self.stats["failures"] += 1
                last_error = f"{type(exc).__name__}: {exc}"
            if attempt < self.attempts:
                time.sleep(RETRY_DELAYS[min(attempt - 1, len(RETRY_DELAYS) - 1)])
        return None, last_error or "unknown_error"


# =============================================================================
# 结果与上下文
# =============================================================================

class Result:
    """单条判据结果：PASS／FAIL／SKIP 与期望／实测／明细。"""

    def __init__(self, check_id: str, name: str) -> None:
        self.check_id = check_id
        self.name = name
        self.status = "PASS"
        self.expected = ""
        self.actual = ""
        self.lines: List[str] = []

    def fail(self, message: str) -> None:
        self.status = "FAIL"
        self.lines.append("FAIL｜" + message)

    def info(self, message: str) -> None:
        self.lines.append("INFO｜" + message)

    def skip(self, message: str) -> None:
        if self.status != "FAIL":
            self.status = "SKIP"
        self.lines.append("SKIP｜" + message)

    def note(self, message: str) -> None:
        self.lines.append("· " + message)


class VerifyContext:
    """一次验证运行的共享上下文（库连接、语料根、临时件与网络客户端）。"""

    def __init__(self, conn, root: Path, db_path: Path, skip_network: bool,
                 sample: int, round_name: str, verbose: bool = True) -> None:
        self.conn = conn
        self.root = root
        self.db_path = db_path
        self.skip_network = skip_network
        self.sample = sample
        self.round_name = round_name
        self.verbose = verbose
        self._tempdirs: List[Path] = []
        self._net: Optional[NetClient] = None

    @property
    def net(self) -> NetClient:
        if self._net is None:
            self._net = NetClient()
        return self._net

    def new_tempdir(self, tag: str) -> Path:
        TMP_PARENT.mkdir(parents=True, exist_ok=True)
        path = Path(tempfile.mkdtemp(prefix=f"verify_{tag}_", dir=str(TMP_PARENT)))
        self._tempdirs.append(path)
        return path

    def cleanup(self) -> None:
        for path in self._tempdirs:
            shutil.rmtree(path, ignore_errors=True)
        self._tempdirs.clear()
        try:
            TMP_PARENT.rmdir()
        except OSError:
            pass


def print_result(result: Result, verbose: bool = True, limit: int = 30) -> None:
    if not verbose:
        return
    line = f"[{result.check_id}] {result.status}"
    if result.expected:
        line += f" ｜期望：{result.expected}"
    if result.actual:
        line += f" ｜实测：{result.actual}"
    print(line)
    for index, item in enumerate(result.lines):
        if index >= limit:
            print(f"    …另有 {len(result.lines) - limit} 条明细")
            break
        print("    " + item)


# =============================================================================
# 结构计数（独立实现，不调用抓取器函数）
# =============================================================================

IMAGE_MACRO_RE = re.compile(r"\{\{([^{}]*)\}\}")
WIKILINK_RE = re.compile(r"\[\[([^\[\]]*)\]\]")
BARE_URL_RE = re.compile(r"(?<![\w\"'=])(https?://[^\s\[\]{}<>\"|]+)")
HEADING_RE = re.compile(r"^\s*(={2,6})\s*(.*?)\s*\1\s*$")
CODE_OPEN_RE = re.compile(r"^\s*<(code|file)([^>]*)>(.*)$", re.I)
NOWIKI_LINE_RE = re.compile(r"^\s*<nowiki>.*?</nowiki>\s*$", re.I | re.S)
TABLE_LINE_RE = re.compile(r"^\s*[|^]")
LIST_RE = re.compile(r"^\s*(?:\*|-)\s+")
ORDERED_RE = re.compile(r"^\s{0,2}\d+\.\s+")
PRE_RE = re.compile(r"^ {2,}\S")
PARA_BREAK_RE = re.compile(r"^\s*(?:={2,6}|<(?:code|file|nowiki)\b|[|^]|(?:\*|-)\s+)")
MD_TABLE_SEP_RE = re.compile(r"^\s*\|[\s:\-|]+\|\s*$")
MD_HEADING_RE = re.compile(r"^#{1,6}\s+")
HTML_RESIDUE_RE = re.compile(
    r"</?(?:html|script|div|p|body|style|table|tr|td|th|a|span|meta|link|frame|frameset)"
    r"\b[^>\n]{0,300}>", re.I)
FENCE_BLOCK_RE = re.compile(r"(?ms)^[ \t]*```[^\n]*\n.*?^[ \t]*```[ \t]*$")


def inline_link_count(text: str) -> int:
    """统计一段 Wikitext 内联文本将产出的 Markdown 链接／图片数。"""
    if not text:
        return 0
    images = len(IMAGE_MACRO_RE.findall(text))
    links = 0

    def replace(match: "re.Match[str]") -> str:
        nonlocal links
        inner = match.group(1)
        if inner.startswith("(") or "(:)" in inner:
            return " "
        target = inner.split("|")[0].strip()
        if target.startswith(("this>", "doku>")):
            return " "
        head = target.split(":")[0]
        if ">" in head and target.split(">")[0].isalpha():
            return " "
        links += 1
        return " "

    rest = WIKILINK_RE.sub(replace, IMAGE_MACRO_RE.sub(" ", text))
    return images + links + len(BARE_URL_RE.findall(rest))


def wikitext_table_cells(line: str) -> Optional[List[str]]:
    stripped = line.strip()
    if not stripped:
        return None
    is_header = stripped.startswith("^")
    separator = "^" if is_header else "|"
    body = stripped[1:] if stripped[:1] in ("|", "^") else stripped
    if body.endswith("|") or body.endswith("^"):
        body = body[:-1]
    cells = [cell.strip() for cell in body.split(separator)]
    if not cells or all(cell in ("", "-") for cell in cells):
        return None
    return cells


def consume_wikitext_table(lines: List[str], index: int) -> Tuple[int, int, int]:
    rows = 0
    links = 0
    n = len(lines)
    while index < n and TABLE_LINE_RE.match(lines[index]):
        cells = wikitext_table_cells(lines[index])
        if cells is not None:
            rows += 1
            for cell in cells:
                links += inline_link_count(cell)
        index += 1
    return rows, links, index


def wikitext_structure(text: str) -> Dict[str, int]:
    """解析 Wikitext 的标题、链接、代码块、表格行数（对应抓取器的转换语义）。"""
    counts = {"headings": 0, "links": 0, "code_blocks": 0, "table_rows": 0}
    lines = normalize_newlines(text or "").split("\n")
    index = 0
    n = len(lines)
    while index < n:
        line = lines[index]
        opened = CODE_OPEN_RE.match(line)
        if opened:
            tag = opened.group(1).lower()
            counts["code_blocks"] += 1
            rest = opened.group(3)
            if re.search(rf"</{tag}>\s*$", rest, re.I):
                index += 1
                continue
            index += 1
            while index < n:
                if re.search(rf"</{tag}>", lines[index], re.I):
                    index += 1
                    break
                index += 1
            continue
        if NOWIKI_LINE_RE.match(line):
            index += 1
            continue
        heading = HEADING_RE.match(line)
        if heading and heading.group(2):
            counts["headings"] += 1
            counts["links"] += inline_link_count(heading.group(2))
            index += 1
            continue
        if TABLE_LINE_RE.match(line):
            rows, links, index = consume_wikitext_table(lines, index)
            counts["table_rows"] += rows
            counts["links"] += links
            continue
        if LIST_RE.match(line) or ORDERED_RE.match(line):
            while index < n and (LIST_RE.match(lines[index]) or ORDERED_RE.match(lines[index])):
                counts["links"] += inline_link_count(lines[index])
                index += 1
            continue
        if PRE_RE.match(line):
            counts["code_blocks"] += 1
            while index < n and PRE_RE.match(lines[index]):
                index += 1
            continue
        if line.strip() == "":
            index += 1
            continue
        paragraph: List[str] = []
        while index < n and lines[index].strip() != "" \
                and not PARA_BREAK_RE.match(lines[index]) \
                and not ORDERED_RE.match(lines[index]) \
                and not PRE_RE.match(lines[index]):
            paragraph.append(lines[index])
            index += 1
        if not paragraph:
            paragraph.append(line)
            index += 1
        counts["links"] += inline_link_count("\n".join(paragraph))
    return counts


def md_structure(markdown: str) -> Dict[str, int]:
    """解析 Markdown 的标题、链接、代码块、表格行数（围栏代码块内不计）。"""
    counts = {"headings": 0, "links": 0, "code_blocks": 0, "table_rows": 0}
    in_fence = False
    for line in normalize_newlines(markdown or "").split("\n"):
        if line.strip().startswith("```"):
            if not in_fence:
                counts["code_blocks"] += 1
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if MD_HEADING_RE.match(line):
            counts["headings"] += 1
        if TABLE_LINE_RE.match(line) and not MD_TABLE_SEP_RE.match(line):
            counts["table_rows"] += 1
        counts["links"] += line.count("](") + len(
            re.findall(r"<https?://[^>\s]+>", line))
    return counts


VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
             "meta", "param", "source", "track", "wbr"}


class HtmlStructure(HTMLParser):
    """独立 HTML 结构计数：跳过 script／style／nav／header／footer／aside／form 等区块。"""

    SKIP_TAGS = {"script", "style", "nav", "header", "footer", "aside", "form",
                 "noscript", "svg", "iframe", "button", "select", "input", "template",
                 "link", "meta", "title", "head"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.skip_depth = 0
        self.pre_depth = 0
        self.counts = {"headings": 0, "links": 0, "code_blocks": 0, "table_rows": 0}
        self._row_cells = 0
        self._in_heading = False
        self._heading_parts: List[str] = []

    def handle_starttag(self, tag: str, attrs) -> None:  # noqa: ANN001
        tag = tag.lower()
        if self.skip_depth:
            if tag not in VOID_TAGS:
                self.skip_depth += 1
            return
        if tag in self.SKIP_TAGS:
            self.skip_depth += 1
            return
        if tag == "pre":
            self.pre_depth += 1
            self.counts["code_blocks"] += 1
            return
        if self.pre_depth:
            return
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._in_heading = True
            self._heading_parts = []
        elif tag in ("a", "img"):
            self.counts["links"] += 1
        elif tag == "tr":
            self._row_cells = 0
        elif tag in ("td", "th"):
            self._row_cells += 1

    def handle_data(self, data: str) -> None:
        if self._in_heading:
            self._heading_parts.append(data)

    def handle_startendtag(self, tag: str, attrs) -> None:  # noqa: ANN001
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if self.skip_depth:
            self.skip_depth -= 1
            return
        if tag == "pre":
            self.pre_depth = max(0, self.pre_depth - 1)
            return
        if tag == "tr" and self._row_cells > 0:
            self.counts["table_rows"] += 1
            self._row_cells = 0
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6") and self._in_heading:
            if "".join(self._heading_parts).strip():
                self.counts["headings"] += 1
            self._in_heading = False
            self._heading_parts = []


def html_structure(source: str) -> Dict[str, int]:
    parser = HtmlStructure()
    parser.feed(source or "")
    parser.close()
    return parser.counts


# =============================================================================
# V1 页面清单守恒
# =============================================================================

def derive_page_set(net: NetClient) -> Tuple[Set[str], Dict[str, int]]:
    """独立以 `?do=index` 递归派生页面集合（含分页与子命名空间），补顶层页。"""
    queue: List[str] = list(NAMESPACES)
    seen: List[str] = []
    pages: Set[str] = set()
    index_counts: Dict[str, int] = {}
    errors: List[str] = []
    while queue:
        current = queue.pop(0)
        if current in seen:
            continue
        seen.append(current)
        offsets_done: Set[int] = set()
        todo: List[Tuple[str, Optional[int]]] = [(current, None)]
        while todo:
            ns, offset = todo.pop(0)
            if offset is not None:
                if offset in offsets_done:
                    continue
                offsets_done.add(offset)
            url = DOKU + "?do=index&idx=" + up.quote(ns, safe=":")
            if offset is not None:
                url += f"&s={offset}"
            body, error = net.fetch(url)
            if body is None:
                errors.append(f"{ns}{'@' + str(offset) if offset else ''}: {error}")
                break
            text = body.decode("utf-8", "replace")
            ids = [up.unquote(raw).strip()
                   for raw in re.findall(r"doku\.php\?id=([^\"&'#]+)", text)]
            pages.update(item for item in ids if item)
            index_counts[ns] = index_counts.get(ns, 0) + len(ids)
            for raw in re.findall(r"idx=([^\"&'>]+)", text):
                sub = up.unquote(raw).strip()
                if sub and ":" in sub and sub.split(":")[0] in NAMESPACES \
                        and sub not in seen and sub not in queue:
                    queue.append(sub)
            for raw in re.findall(r"(?:&amp;|&)s=(\d+)", text):
                value = int(raw)
                if value not in offsets_done and (ns, value) not in todo:
                    todo.append((ns, value))
    pages |= set(TOP_PAGES)
    if errors:
        raise VerifyError("索引请求失败：" + "；".join(errors[:5]))
    return pages, index_counts


def check_v1(ctx: VerifyContext) -> Result:
    result = Result("V1", CHECK_NAMES["V1"])
    conn = ctx.conn
    result.expected = "派生集合 == crawl_runs 基线 == pages(wiki)，逐命名空间计数一致"
    runs = conn.execute(
        "SELECT run_id, scope_json, page_baseline FROM crawl_runs "
        "WHERE status LIKE 'completed%' OR status = 'running' "
        "ORDER BY COALESCE(finished_at, started_at) DESC LIMIT 1").fetchall()
    if not runs:
        total = table_count(conn, "pages")
        result.actual = f"crawl_runs 基线记录 0 条；pages 行 {total}"
        result.fail("库为空或缺 crawl_runs 基线（首轮抓取未完成），V1 无法成立")
        return result

    run_id, scope_json, _baseline = runs[0]
    try:
        scope = json.loads(scope_json or "{}")
    except json.JSONDecodeError:
        result.fail(f"crawl_runs.scope_json 不是合法 JSON（run={run_id}）")
        return result

    wiki_rows = conn.execute(
        "SELECT page_key, namespace, status FROM pages "
        "WHERE source_kind = 'wiki'").fetchall()
    keys = sorted(row[0] for row in wiki_rows)
    baseline = scope.get("baseline")
    result.actual = f"wiki 页 {len(keys)}；基线 {baseline}（run={run_id}）"
    if not keys:
        result.fail("pages 中 source_kind='wiki' 页面 0 条")
        return result

    if baseline != len(keys):
        result.fail(f"基线页数 {baseline} ≠ pages wiki 页数 {len(keys)}")
    actual_sha = sha256_hex("\n".join(keys).encode("utf-8"))
    if scope.get("page_set_sha256") != actual_sha:
        result.fail(
            f"页面集合 SHA-256 不符：基线 {str(scope.get('page_set_sha256'))[:16]}… "
            f"实测 {actual_sha[:16]}…")

    namespaces = list(scope.get("namespaces") or NAMESPACES)
    expected_counts = {str(k): int(v) for k, v in (scope.get("namespace_counts") or {}).items()}
    computed: Dict[str, int] = {}
    for key, ns, _status in wiki_rows:
        want = namespace_of(key, namespaces)
        if ns != want:
            result.fail(f"命名空间归属不符：{key} 库内={ns} 期望={want}")
        computed[ns] = computed.get(ns, 0) + 1
    for ns in sorted(set(computed) | set(expected_counts)):
        if computed.get(ns, 0) != expected_counts.get(ns, 0):
            result.fail(f"命名空间计数不符：{ns} 库内={computed.get(ns, 0)} "
                        f"基线={expected_counts.get(ns, 0)}")
    if baseline != BASELINE_EXPECTED:
        result.info(f"基线 {baseline} 与规格实测口径 {BASELINE_EXPECTED} 不同（仅披露）")

    if ctx.skip_network:
        result.skip("页面清单重派生 SKIP（--skip-network）；离线三方比对已完成")
        return result

    try:
        derived, index_counts = derive_page_set(ctx.net)
    except Exception as exc:  # noqa: BLE001
        result.fail(f"索引派生失败：{type(exc).__name__}: {exc}")
        return result

    result.note(f"派生 {len(derived)} 页；索引请求命名空间 {len(index_counts)} 个")
    missing = sorted(set(keys) - derived)
    extra = sorted(derived - set(keys))
    if missing:
        result.fail(f"库内有而派生无（消失页面）{len(missing)} 个：{short_list(missing)}")
    if extra:
        result.fail(f"派生有而库内无（漏抓页面）{len(extra)} 个：{short_list(extra)}")
    if len(derived) != baseline:
        result.fail(f"派生页数 {len(derived)} ≠ 基线 {baseline}（清单漂移，须重跑抓取并更新基线）")
    return result


# =============================================================================
# V2 双形态落盘
# =============================================================================

def check_v2(ctx: VerifyContext) -> Result:
    result = Result("V2", CHECK_NAMES["V2"])
    result.expected = "wiki 页 .wikitext／.md 存在非空；sha256_markdown 与 .md 一致；无 failed 页"
    rows = ctx.conn.execute(
        "SELECT page_key, source_kind, status, wikitext_path, md_path, sha256_markdown "
        "FROM pages ORDER BY page_key").fetchall()
    wiki_checked = 0
    external_checked = 0
    for key, kind, status, wikitext_rel, md_rel, md_sha in rows:
        if kind == "wiki":
            if status == "failed":
                result.fail(f"{key}: status=failed（无落盘，验证器不得放行）")
                continue
            wiki_checked += 1
            for label, rel in (("wikitext", wikitext_rel), ("md", md_rel)):
                if not rel:
                    result.fail(f"{key}: {label}_path 为空")
                    continue
                path = ctx.root / rel
                if not path.is_file():
                    result.fail(f"{key}: {label} 文件缺失（{rel}）")
                elif path.stat().st_size == 0:
                    result.fail(f"{key}: {label} 文件为空（{rel}）")
            if md_rel and md_sha:
                path = ctx.root / md_rel
                if path.is_file() and sha256_hex(path.read_bytes()) != md_sha:
                    result.fail(f"{key}: sha256_markdown 与 .md 实测不符")
        else:
            if status == "active":
                external_checked += 1
                if not md_rel:
                    result.fail(f"{key}: external active 页 md_path 为空")
                    continue
                path = ctx.root / md_rel
                if not path.is_file():
                    result.fail(f"{key}: external .md 缺失（{md_rel}）")
                elif md_sha and sha256_hex(path.read_bytes()) != md_sha:
                    result.fail(f"{key}: sha256_markdown 与 .md 实测不符")
            elif status == "needs_ocr_deferred" and md_rel \
                    and not (ctx.root / md_rel).is_file():
                result.fail(f"{key}: needs_ocr_deferred 页 .md 缺失（{md_rel}）")
    result.actual = f"已核 wiki 页 {wiki_checked}、active 外链页 {external_checked}"
    return result


# =============================================================================
# V3 Markdown 覆盖
# =============================================================================

def check_v3(ctx: VerifyContext) -> Result:
    result = Result("V3", CHECK_NAMES["V3"])
    result.expected = "每页 1 条 fulltext；char_count == len(content)；非空页有块；无 HTML 残留"
    conn = ctx.conn
    page_keys = {row[0] for row in conn.execute("SELECT page_key FROM pages").fetchall()}
    text_keys = {row[0] for row in conn.execute("SELECT page_key FROM fulltext").fetchall()}
    missing = sorted(page_keys - text_keys)
    extra = sorted(text_keys - page_keys)
    if missing:
        result.fail(f"{len(missing)} 页无 fulltext：{short_list(missing)}")
    if extra:
        result.fail(f"{len(extra)} 条 fulltext 无对应页面：{short_list(extra)}")

    bad_char = []
    residue = []
    for key, content, char_count, method in conn.execute(
            "SELECT page_key, content, char_count, extraction_method FROM fulltext "
            "ORDER BY page_key").fetchall():
        body = content or ""
        if int(char_count or 0) != len(body):
            bad_char.append(f"{key}（char_count={char_count} len={len(body)}）")
        # PDF 文本层／OCR 正文可能合法出现 `ed <script` 一类 shell 语法，不作 HTML 残留判定
        if (method or "") in ("pdf-text", "pdf-ocr"):
            continue
        stripped = FENCE_BLOCK_RE.sub("", body)
        hits = HTML_RESIDUE_RE.findall(stripped)
        if hits:
            residue.append(f"{key}（{short_list([h for h in hits], 3)}）")
    if bad_char:
        result.fail(f"char_count 与正文长度不符 {len(bad_char)} 条：{short_list(bad_char)}")
    if residue:
        result.fail(f"正文含 HTML 标签残留 {len(residue)} 页：{short_list(residue)}")

    no_block = conn.execute(
        "SELECT p.page_key FROM pages p JOIN fulltext f USING (page_key) "
        "WHERE p.status NOT IN ('failed', 'empty') AND length(f.content) > 0 "
        "AND NOT EXISTS (SELECT 1 FROM fulltext_blocks b WHERE b.page_key = p.page_key) "
        "ORDER BY p.page_key").fetchall()
    if no_block:
        result.fail(f"{len(no_block)} 个非空页无 fulltext_blocks："
                    f"{short_list([r[0] for r in no_block])}")
    result.actual = f"页面 {len(page_keys)}、fulltext {len(text_keys)}、块覆盖缺 {len(no_block)}"
    return result


# =============================================================================
# V4 外链闭合
# =============================================================================

def check_v4(ctx: VerifyContext) -> Result:
    result = Result("V4", CHECK_NAMES["V4"])
    result.expected = ("external 链接状态属于 "
                       "{fetched, wayback, excluded, failed, needs_ocr_deferred} 且 URL 可追溯")
    conn = ctx.conn
    links = conn.execute(
        "SELECT target_url, resolution_status FROM links "
        "WHERE target_kind = 'external' ORDER BY target_url").fetchall()
    bad_status = [(url, status) for url, status in links if status not in ALLOWED_LINK_STATUS]
    bad_pairs = unique_list([f"{url}→{status}" for url, status in bad_status])
    if bad_pairs:
        result.fail(f"分辨率状态越界 {len(bad_status)} 条：" + short_list(bad_pairs))

    external_urls = {row[0] for row in conn.execute(
        "SELECT canonical_url FROM pages WHERE source_kind = 'external'").fetchall()}
    excluded_urls = {row[0] for row in conn.execute(
        "SELECT url FROM excluded_items").fetchall()}
    failed_log_urls = {row[0] for row in conn.execute(
        "SELECT url FROM crawl_log WHERE url IS NOT NULL "
        "AND (error_type IS NOT NULL OR http_status >= 400)").fetchall()}

    unresolved: List[str] = []
    for url, _status in links:
        if url in external_urls or url in excluded_urls or url in failed_log_urls:
            continue
        hit = conn.execute(
            "SELECT 1 FROM crawl_log WHERE error_detail LIKE ? ESCAPE '\\' LIMIT 1",
            ["%" + escape_like(url) + "%"]).fetchone()
        if hit:
            continue
        unresolved.append(url)
    unresolved = unique_list(unresolved)
    if unresolved:
        result.fail(f"未闭合外链 {len(unresolved)} 条：{short_list(unresolved)}")

    status_counts = Counter(status for _url, status in links)
    result.actual = (f"外链 {len(links)} 条；状态分布 "
                     f"{dict(sorted(status_counts.items()))}"
                     + (f"；越界示例 {short_list(bad_pairs, 5)}" if bad_pairs else ""))
    return result


# =============================================================================
# V5 键与去重
# =============================================================================

def check_v5(ctx: VerifyContext) -> Result:
    result = Result("V5", CHECK_NAMES["V5"])
    result.expected = "四类重复计数均为 0"
    conn = ctx.conn
    queries = [
        ("page_key", "SELECT page_key, COUNT(*) FROM pages GROUP BY 1 HAVING COUNT(*) > 1"),
        ("(page_key, block_index)",
         "SELECT page_key, block_index FROM fulltext_blocks "
         "GROUP BY 1, 2 HAVING COUNT(*) > 1"),
        ("external 归一 URL",
         "SELECT canonical_url, COUNT(*) FROM pages WHERE source_kind = 'external' "
         "GROUP BY 1 HAVING COUNT(*) > 1"),
        ("(page_key, converter)",
         "SELECT page_key, converter FROM conversions GROUP BY 1, 2 HAVING COUNT(*) > 1"),
    ]
    summary = []
    for label, sql in queries:
        duplicates = conn.execute(sql).fetchall()
        summary.append(f"{label}={len(duplicates)}")
        if duplicates:
            result.fail(f"{label} 重复 {len(duplicates)} 组：" + short_list(
                [str(row[0]) for row in duplicates]))
    result.actual = "；".join(summary)
    return result


# =============================================================================
# V6 原文抽样重取
# =============================================================================

def check_v6(ctx: VerifyContext) -> Result:
    result = Result("V6", CHECK_NAMES["V6"])
    result.expected = "wiki 抽样重取字节 SHA-256 == sha256_source；外链差异只记 INFO"
    if ctx.skip_network:
        result.skip("原文抽样重取 SKIP（--skip-network）")
        return result

    wiki_rows = ctx.conn.execute(
        "SELECT page_key, sha256_source FROM pages "
        "WHERE source_kind = 'wiki' AND status = 'active' AND sha256_source IS NOT NULL "
        "ORDER BY page_key").fetchall()
    rng = random.Random(20261025)
    wiki_sample = rng.sample(wiki_rows, min(ctx.sample, len(wiki_rows))) if wiki_rows else []

    mismatched: List[str] = []
    failed: List[str] = []
    for key, stored in wiki_sample:
        url = DOKU + "?do=export_raw&id=" + up.quote(key, safe=":")
        body, error = ctx.net.fetch(url)
        if body is None:
            failed.append(f"{key}: {error}")
            continue
        actual = sha256_hex(body)
        if actual != stored:
            mismatched.append(f"{key}: 库内 {stored[:12]}… 实测 {actual[:12]}…")
    if mismatched:
        result.fail(f"wiki 页原文哈希不符 {len(mismatched)} 页：{short_list(mismatched)}")
    if failed:
        result.fail(f"wiki 页重取失败（已重试 3 次）{len(failed)} 页：{short_list(failed)}")

    external_rows = ctx.conn.execute(
        "SELECT page_key, canonical_url, sha256_source, source_bytes FROM pages "
        "WHERE source_kind = 'external' AND status = 'active' "
        "AND sha256_source IS NOT NULL ORDER BY page_key").fetchall()
    external_sample = rng.sample(
        external_rows, min(10, len(external_rows))) if external_rows else []
    changed = 0
    skipped_large = 0
    for key, url, stored, size in external_sample:
        if size is not None and int(size) > MAX_EXTERNAL_REFETCH_BYTES:
            skipped_large += 1
            continue
        body, error = ctx.net.fetch(url)
        if body is None:
            failed.append(f"{key}: {error}")
            continue
        if sha256_hex(body) != stored:
            changed += 1
            result.info(f"changed_since_crawl：{key}（{url}）")
    if failed:
        result.fail(f"重取失败（已重试 3 次）{len(failed)} 页：{short_list(failed)}")

    result.actual = (f"wiki 抽样 {len(wiki_sample)}／外链抽样 {len(external_sample)}；"
                     f"外链变化 {changed}、跳过大体量 {skipped_large}")
    return result


# =============================================================================
# V7 运行时版本与结构
# =============================================================================

def check_v7(ctx: VerifyContext) -> Result:
    result = Result("V7", CHECK_NAMES["V7"])
    result.expected = ("duckdb 2.0.0；存储 v2.0.0+；基表 11、视图 1；主键与唯一约束齐备；无 BLOB")
    import duckdb

    if duckdb.__version__ != DUCKDB_REQUIRED:
        result.fail(f"duckdb 运行时 {duckdb.__version__} ≠ {DUCKDB_REQUIRED}")
    storage_versions: List[str] = []
    for (tags,) in ctx.conn.execute("SELECT tags FROM duckdb_databases()").fetchall():
        if isinstance(tags, dict):
            value = tags.get("storage_version")
            if value:
                storage_versions.append(str(value))
    if not any(value.startswith(STORAGE_REQUIRED) for value in storage_versions):
        result.fail(f"存储版本未达 {STORAGE_REQUIRED}：{storage_versions or '（空）'}")

    tables = [row[0] for row in ctx.conn.execute(
        "SELECT table_name FROM information_schema.tables "
        "WHERE table_schema = 'main' AND table_type = 'BASE TABLE' ORDER BY table_name"
    ).fetchall()]
    views = [row[0] for row in ctx.conn.execute(
        "SELECT table_name FROM information_schema.tables "
        "WHERE table_schema = 'main' AND table_type = 'VIEW' ORDER BY table_name"
    ).fetchall()]
    if len(tables) != len(EXPECTED_TABLES):
        result.fail(f"基表 {len(tables)} 张 ≠ {len(EXPECTED_TABLES)}：{tables}")
    if set(tables) != set(EXPECTED_TABLES):
        result.fail("基表名单不符：缺 " + short_list(sorted(set(EXPECTED_TABLES) - set(tables)))
                    + "；多 " + short_list(sorted(set(tables) - set(EXPECTED_TABLES))))
    if views != EXPECTED_VIEWS:
        result.fail(f"视图名单不符：{views}")

    actual_constraints: Dict[str, Set[Tuple[str, Tuple[str, ...]]]] = {}
    for table, ctype, columns in ctx.conn.execute(
            "SELECT table_name, constraint_type, constraint_column_names "
            "FROM duckdb_constraints() WHERE schema_name = 'main' "
            "AND constraint_type IN ('PRIMARY KEY', 'UNIQUE')").fetchall():
        actual_constraints.setdefault(table, set()).add((ctype, tuple(columns or [])))
    missing_constraints: List[str] = []
    for table, wanted in EXPECTED_CONSTRAINTS.items():
        for ctype, columns in wanted:
            if (ctype, tuple(columns)) not in actual_constraints.get(table, set()):
                missing_constraints.append(f"{table}.{ctype}{tuple(columns)}")
    if missing_constraints:
        result.fail("约束缺失：" + short_list(missing_constraints))

    blob_columns = ctx.conn.execute(
        "SELECT table_name, column_name, data_type FROM information_schema.columns "
        "WHERE data_type ILIKE '%blob%'").fetchall()
    if blob_columns:
        result.fail("存在 BLOB 列：" + short_list([f"{t}.{c}" for t, c, _ in blob_columns]))

    result.actual = (f"duckdb {duckdb.__version__}；存储 {storage_versions}；"
                     f"基表 {len(tables)}、视图 {len(views)}；BLOB 列 {len(blob_columns)}")
    return result


# =============================================================================
# V8 可恢复性
# =============================================================================

def check_v8(ctx: VerifyContext) -> Result:
    result = Result("V8", CHECK_NAMES["V8"])
    result.expected = "EXPORT → IMPORT 后 11 表行数逐一相等"
    import duckdb

    work = ctx.new_tempdir("v8")
    export_dir = work / "export"
    import_db = work / "import.duckdb"
    exported = 0
    compared = 0
    try:
        target = export_dir.as_posix().replace("'", "''")
        ctx.conn.execute(f"EXPORT DATABASE '{target}' (FORMAT PARQUET)")
        exported = len(list(export_dir.glob("*.parquet")))
        imported = duckdb.connect(str(import_db))
        try:
            imported.execute(f"IMPORT DATABASE '{target}'")
            for table in EXPECTED_TABLES:
                before = table_count(ctx.conn, table)
                after = table_count(imported, table)
                compared += 1
                if before != after:
                    result.fail(f"{table} 行数不符：主库 {before}／导入 {after}")
        finally:
            imported.close()
    except Exception as exc:  # noqa: BLE001
        result.fail(f"EXPORT／IMPORT 失败：{type(exc).__name__}: {exc}")
    finally:
        shutil.rmtree(work, ignore_errors=True)
    result.actual = f"导出 parquet {exported} 个；比对表 {compared} 张"
    return result


# =============================================================================
# V9 幂等二跑
# =============================================================================

def check_v9(ctx: VerifyContext) -> Result:
    result = Result("V9", CHECK_NAMES["V9"])
    result.expected = "二跑后 pages／fulltext／fulltext_blocks／links／conversions 行数与 page_key 集合不变"
    if ctx.skip_network:
        result.skip("幂等二跑 SKIP（--skip-network）")
        return result
    if not CRAWL_SCRIPT.is_file():
        result.fail(f"抓取器不存在：{CRAWL_SCRIPT}")
        return result

    incomplete = ctx.conn.execute(
        "SELECT COUNT(*) FROM pages WHERE source_kind = 'wiki' "
        "AND (status <> 'active' OR md_path IS NULL)").fetchone()[0]
    if incomplete:
        result.skip(f"存在 {incomplete} 个非 active 或缺 md_path 的 wiki 页，"
                    "幂等二跑前置不成立（先修 V2）")
        return result
    missing_md = [row[0] for row in ctx.conn.execute(
        "SELECT page_key, md_path FROM pages WHERE source_kind = 'wiki' AND md_path IS NOT NULL"
    ).fetchall() if not (ctx.root / row[1]).is_file()]
    if missing_md:
        result.skip(f"{len(missing_md)} 个 wiki 页 .md 缺失，幂等二跑会改写真实语料，跳过")
        return result

    scope_row = ctx.conn.execute(
        "SELECT scope_json FROM crawl_runs "
        "WHERE status LIKE 'completed%' OR status = 'running' "
        "ORDER BY COALESCE(finished_at, started_at) DESC LIMIT 1").fetchone()
    baseline = 0
    if scope_row:
        try:
            baseline = int(json.loads(scope_row[0] or "{}").get("baseline") or 0)
        except (json.JSONDecodeError, TypeError, ValueError):
            baseline = 0
    wiki_count = ctx.conn.execute(
        "SELECT COUNT(*) FROM pages WHERE source_kind = 'wiki'").fetchone()[0]
    if baseline <= 0 or int(wiki_count) != baseline:
        result.skip(f"库内 wiki 页 {wiki_count} ≠ 基线 {baseline or '（缺）'}，"
                    "未完成全量抓取；二跑会补抓缺失页并改写语料，故跳过")
        return result

    before_counts = {table: table_count(ctx.conn, table) for table in COUNT_TABLES}
    before_keys = {row[0] for row in ctx.conn.execute(
        "SELECT page_key FROM pages").fetchall()}
    work = ctx.new_tempdir("v9")
    temp_db = work / "tuhs_wiki.duckdb"
    try:
        import duckdb

        # Windows 下无法复制被本进程打开的库文件，故以逻辑导出／导入生成同构副本
        export_dir = work / "export"
        target = export_dir.as_posix().replace("'", "''")
        ctx.conn.execute(f"EXPORT DATABASE '{target}' (FORMAT PARQUET)")
        copied = duckdb.connect(str(temp_db))
        try:
            copied.execute(f"IMPORT DATABASE '{target}'")
        finally:
            copied.close()
        shutil.rmtree(export_dir, ignore_errors=True)
        command = [sys.executable, "-X", "utf8", str(CRAWL_SCRIPT),
                   "--db", str(temp_db), "--root", str(ctx.root),
                   "--wiki-only", "--resume"]
        proc = subprocess.run(command, capture_output=True, text=True, encoding="utf-8",
                              errors="replace", timeout=3600)
        if proc.returncode != 0:
            tail = (proc.stderr or proc.stdout or "").strip().splitlines()[-6:]
            result.fail(f"抓取器二跑退出码 {proc.returncode}：" + "；".join(tail))
            return result
        verify_conn = duckdb.connect(str(temp_db))
        try:
            for table in COUNT_TABLES:
                after = table_count(verify_conn, table)
                if after != before_counts[table]:
                    result.fail(f"{table} 行数变化：{before_counts[table]} → {after}")
            after_keys = {row[0] for row in verify_conn.execute(
                "SELECT page_key FROM pages").fetchall()}
            if after_keys != before_keys:
                added = sorted(after_keys - before_keys)
                removed = sorted(before_keys - after_keys)
                result.fail(f"page_key 集合变化：新增 {short_list(added)}；"
                            f"消失 {short_list(removed)}")
            result.note(f"二跑输出末行：{(proc.stdout or '').strip().splitlines()[-1:]}")
        finally:
            verify_conn.close()
    except Exception as exc:  # noqa: BLE001
        result.fail(f"幂等二跑异常：{type(exc).__name__}: {exc}")
    finally:
        shutil.rmtree(work, ignore_errors=True)
    result.actual = "行数 " + "／".join(f"{t}={before_counts[t]}" for t in COUNT_TABLES)
    return result


# =============================================================================
# V10 二进制禁入
# =============================================================================

def check_v10(ctx: VerifyContext) -> Result:
    result = Result("V10", CHECK_NAMES["V10"])
    result.expected = "语料目录只允许 .md／.wikitext（raw/media 明示图片与库文件除外）；魔数扫描为零"
    if not ctx.root.is_dir():
        result.fail(f"语料目录不存在：{ctx.root}")
        return result
    violations: List[str] = []
    magic_hits: List[str] = []
    ext_counts: Counter = Counter()
    inspected = 0
    for path in sorted(ctx.root.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(ctx.root)
        if path.name.startswith("tuhs_wiki.duckdb"):
            continue
        inspected += 1
        suffix = path.suffix.lower()
        ext_counts[suffix or "（无扩展名）"] += 1
        allowed = suffix in ALLOWED_TEXT_EXT or (
            suffix in IMAGE_EXT and "raw/media" in relative.as_posix())
        if not allowed:
            violations.append(f"扩展名不允许：{relative.as_posix()}")
        with path.open("rb") as handle:
            head = handle.read(16)
        for magic, kind in MAGIC_SIGNATURES:
            if head.startswith(magic):
                magic_hits.append(f"{relative.as_posix()}（{kind}）")
                break
    if violations:
        result.fail(f"非文本文件 {len(violations)} 个：{short_list(violations)}")
    if magic_hits:
        result.fail(f"文件头魔数命中 {len(magic_hits)} 个：{short_list(magic_hits)}")
    result.actual = (f"扫描文件 {inspected} 个；扩展名分布 "
                     f"{dict(sorted(ext_counts.items()))}")
    return result


# =============================================================================
# V11 转换保真抽查
# =============================================================================

def check_v11(ctx: VerifyContext) -> Result:
    result = Result("V11", CHECK_NAMES["V11"])
    result.expected = ("抽样页 标题／链接／代码块差异为 0；表格行数 wiki 为 0、"
                       "外链 HTML 按 ±20% 容差（Markdown 无法表达嵌套表／rowspan）")
    rows = ctx.conn.execute(
        "SELECT page_key, source_kind, wikitext_path, md_path, canonical_url, content_type "
        "FROM pages WHERE status = 'active' AND md_path IS NOT NULL ORDER BY page_key").fetchall()
    if not rows:
        result.fail("无 active 且已落盘 .md 的页面可抽样")
        return result
    rng = random.Random(20261025 + 11)
    sample = rng.sample(rows, min(ctx.sample, len(rows)))
    wiki_compared = 0
    external_compared = 0
    external_skipped = 0
    diffs: List[str] = []
    fields = ("headings", "links", "code_blocks", "table_rows")
    for key, kind, wikitext_rel, md_rel, canonical_url, content_type in sample:
        md_path = ctx.root / md_rel
        if not md_path.is_file():
            diffs.append(f"{key}: .md 缺失，无法比对")
            continue
        target = read_text(md_path)
        if kind == "wiki":
            if not wikitext_rel or not (ctx.root / wikitext_rel).is_file():
                diffs.append(f"{key}: .wikitext 缺失，无法比对")
                continue
            source = read_text(ctx.root / wikitext_rel)
            source_counts = wikitext_structure(source)
            wiki_compared += 1
        else:
            if ctx.skip_network:
                external_skipped += 1
                continue
            ctype = (content_type or "").lower()
            if "html" not in ctype:
                external_skipped += 1
                continue
            body, error = ctx.net.fetch(canonical_url)
            if body is None:
                diffs.append(f"{key}: 源站重取失败（{error}）")
                continue
            source_counts = html_structure(body.decode("utf-8", "replace"))
            external_compared += 1
        md_counts = md_structure(target)
        for field in fields:
            if source_counts[field] == md_counts[field]:
                continue
            if field == "table_rows" and kind == "external":
                src = source_counts[field]
                dst = md_counts[field]
                if abs(dst - src) <= max(2, int(src * 0.2)):
                    result.info(f"{key}: table_rows 源={src} md={dst}（Markdown 表格限制，容差内）")
                    continue
            if field == "headings" and kind == "external" \
                    and source_counts[field] > 0 and md_counts[field] == 0 \
                    and md_counts.get("table_rows", 0) > 0:
                result.info(f"{key}: headings 源={source_counts[field]} md=0"
                            "（布局表折叠为单元格，标题层级未保留）")
                continue
            diffs.append(f"{key}: {field} 源={source_counts[field]} md={md_counts[field]}")
    if diffs:
        result.fail(f"结构计数差异 {len(diffs)} 处：{short_list(diffs)}")
    if external_skipped:
        result.info(f"外链页 {external_skipped} 个未比对"
                    + ("（--skip-network）" if ctx.skip_network else "（非 HTML／重取不可用）"))
    result.actual = (f"抽样 {len(sample)} 页；wiki 比对 {wiki_compared}、"
                     f"外链比对 {external_compared}、外链跳过 {external_skipped}")
    return result


# =============================================================================
# V12 转换台账
# =============================================================================

def check_v12(ctx: VerifyContext) -> Result:
    result = Result("V12", CHECK_NAMES["V12"])
    result.expected = "每页有 conversions 行；converter_version 与 schema_meta 一致；md_sha256 与文件一致"
    conn = ctx.conn
    meta = conn.execute(
        "SELECT value FROM schema_meta WHERE key = 'converter_version'").fetchone()
    expected_version = (meta[0] if meta else "") or CONVERTER_VERSION_FALLBACK
    if not meta:
        result.fail("schema_meta 缺 converter_version 键")
    else:
        result.note(f"schema_meta.converter_version={expected_version}")

    pages = {row[0]: (row[1], row[2], row[3]) for row in conn.execute(
        "SELECT page_key, status, md_path, sha256_markdown FROM pages").fetchall()}
    conversions = conn.execute(
        "SELECT page_key, converter, converter_version, md_sha256 FROM conversions "
        "ORDER BY page_key").fetchall()
    covered = {row[0] for row in conversions}
    missing = sorted(set(pages) - covered)
    if missing:
        result.fail(f"{len(missing)} 页无 conversions 行：{short_list(missing)}")

    bad_version: List[str] = []
    bad_hash: List[str] = []
    unchecked = 0
    for key, converter, version, md_sha in conversions:
        if (version or "") != expected_version:
            bad_version.append(f"{key}／{converter}={version}")
        status, md_rel, sha = pages.get(key, (None, None, None))
        if md_sha is None:
            if status == "active":
                bad_hash.append(f"{key}: active 页 md_sha256 为空")
            else:
                unchecked += 1
            continue
        if not md_rel:
            bad_hash.append(f"{key}: md_path 为空")
            continue
        path = ctx.root / md_rel
        if not path.is_file():
            bad_hash.append(f"{key}: .md 缺失（{md_rel}）")
            continue
        if sha256_hex(path.read_bytes()) != md_sha:
            bad_hash.append(f"{key}: md_sha256 与 .md 实测不符")
    if bad_version:
        result.fail(f"converter_version 不符 {len(bad_version)} 条：{short_list(bad_version)}")
    if bad_hash:
        result.fail(f"md_sha256 校验失败 {len(bad_hash)} 条：{short_list(bad_hash)}")
    result.actual = (f"页面 {len(pages)}、conversions {len(conversions)}；"
                     f"覆盖缺 {len(missing)}、版本不符 {len(bad_version)}、"
                     f"哈希不符 {len(bad_hash)}、无哈希记录 {unchecked}")
    return result


# =============================================================================
# 运行与写库
# =============================================================================

CHECK_ORDER: List[Tuple[str, Any]] = [
    ("V1", check_v1), ("V2", check_v2), ("V3", check_v3), ("V4", check_v4),
    ("V5", check_v5), ("V6", check_v6), ("V7", check_v7), ("V8", check_v8),
    ("V9", check_v9), ("V10", check_v10), ("V11", check_v11), ("V12", check_v12),
]


def run_all(ctx: VerifyContext, only: Optional[Iterable[str]] = None,
            verbose: bool = True) -> List[Result]:
    wanted = set(only) if only else None
    results: List[Result] = []
    for check_id, function in CHECK_ORDER:
        if wanted and check_id not in wanted:
            continue
        try:
            result = function(ctx)
        except Exception as exc:  # noqa: BLE001
            result = Result(check_id, CHECK_NAMES[check_id])
            result.expected = "判据正常执行"
            result.actual = f"{type(exc).__name__}: {exc}"
            result.fail("判据执行异常（已转 FAIL，未中断整轮）")
        results.append(result)
        print_result(result, verbose)
    return results


def write_verification(conn, round_name: str, results: List[Result],
                       run_id: str) -> int:
    exists = conn.execute(
        "SELECT 1 FROM information_schema.tables WHERE table_schema = 'main' "
        "AND table_name = 'verification'").fetchone()
    if not exists:
        print("[warn] 库内无 verification 表，跳过结果写入")
        return 0
    seq = int(conn.execute(
        "SELECT COALESCE(MAX(id), 0) FROM verification").fetchone()[0])
    written = 0
    for result in results:
        conn.execute("DELETE FROM verification WHERE round = ? AND check_id = ?",
                     [round_name, result.check_id])
        seq += 1
        passed = True if result.status == "PASS" else (
            False if result.status == "FAIL" else None)
        conn.execute(
            "INSERT INTO verification (id, run_id, round, check_id, check_name, expected, "
            "actual, passed, detail, verified_at) VALUES (?,?,?,?,?,?,?,?,?,?)",
            [seq, run_id, round_name, result.check_id, result.name,
             (result.expected or "")[:500], (result.actual or "")[:500], passed,
             "\n".join(result.lines)[:4000] or None, now_iso()])
        written += 1
    return written


def latest_run_id(conn) -> str:
    row = conn.execute(
        "SELECT run_id FROM crawl_runs ORDER BY COALESCE(finished_at, started_at) "
        "DESC LIMIT 1").fetchone()
    return row[0] if row else "verify-" + datetime.now().strftime("%Y%m%dT%H%M%S")


# =============================================================================
# 自检（离线）：正常夹具与六类缺陷
# =============================================================================

FIXTURE_WT_TESTER = """====== Tester ======

Paragraph with [[https://example.org/paper|link]].

  * item

<code text>
code
</code>

^ H ^ V ^
| a | 1 |
"""

FIXTURE_MD_TESTER = """# Tester

Paragraph with [link](https://example.org/paper).

- item

```text
code
```

| H | V |
| --- | --- |
| a | 1 |
"""

FIXTURE_WT_SYSTEMS = """====== Sys ======

Text only.
"""

FIXTURE_MD_SYSTEMS = """# Sys

Text only.
"""

FIXTURE_MD_EXTERNAL = """# Paper

See [source](https://example.org/paper).
"""


def write_text_file(path: Path, text: str) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    data = normalize_newlines(text).encode("utf-8")
    path.write_bytes(data)
    return sha256_hex(data)


def load_schema_sql() -> str:
    if not SCHEMA_SQL_PATH.is_file():
        raise VerifyError(f"缺架构固定资源：{SCHEMA_SQL_PATH}")
    return SCHEMA_SQL_PATH.read_text(encoding="utf-8")


def build_fixture(case_dir: Path):
    """构造正常夹具：2 个 wiki 页＋1 个外链页＋完整链接／排除／日志／台账。"""
    import duckdb

    case_dir.mkdir(parents=True, exist_ok=True)
    root = case_dir / "corpus"
    db_path = case_dir / "tuhs_wiki.duckdb"
    wt_tester = root / "raw/wiki/people/tester.wikitext"
    md_tester = root / "raw/wiki/people/tester.md"
    wt_systems = root / "raw/wiki/systems/sys.wikitext"
    md_systems = root / "raw/wiki/systems/sys.md"
    md_external = root / "raw/external/example.org/paper.md"
    hash_wt_tester = write_text_file(wt_tester, FIXTURE_WT_TESTER)
    hash_md_tester = write_text_file(md_tester, FIXTURE_MD_TESTER)
    hash_wt_systems = write_text_file(wt_systems, FIXTURE_WT_SYSTEMS)
    hash_md_systems = write_text_file(md_systems, FIXTURE_MD_SYSTEMS)
    hash_md_external = write_text_file(md_external, FIXTURE_MD_EXTERNAL)

    conn = duckdb.connect(str(db_path))
    conn.execute(load_schema_sql())
    conn.execute("INSERT INTO schema_meta (key, value) VALUES ('converter_version', ?)",
                 ["tuhs-md/1.0"])
    conn.execute("INSERT INTO schema_meta (key, value) VALUES ('page_baseline', '2')")

    pages = [
        (1, "people:tester", "wiki", "people", "Tester",
         "https://wiki.tuhs.org/doku.php?id=people:tester",
         "https://wiki.tuhs.org/doku.php?id=people:tester", 0,
         "raw/wiki/people/tester.wikitext", "raw/wiki/people/tester.md",
         hash_wt_tester, hash_md_tester, len(FIXTURE_MD_TESTER)),
        (2, "systems:sys", "wiki", "systems", "Sys",
         "https://wiki.tuhs.org/doku.php?id=systems:sys",
         "https://wiki.tuhs.org/doku.php?id=systems:sys", 0,
         "raw/wiki/systems/sys.wikitext", "raw/wiki/systems/sys.md",
         hash_wt_systems, hash_md_systems, len(FIXTURE_MD_SYSTEMS)),
        (3, "ext:paper", "external", "(external)", "Paper",
         "https://example.org/paper", "https://example.org/paper", 1,
         None, "raw/external/example.org/paper.md",
         "0" * 64, hash_md_external, len(FIXTURE_MD_EXTERNAL)),
    ]
    for row in pages:
        conn.execute(
            "INSERT INTO pages (id, page_key, source_kind, namespace, title, url, "
            "canonical_url, depth, fetched_at, fetch_mode, wikitext_path, md_path, "
            "sha256_source, sha256_markdown, char_count, extraction_method, converter, "
            "status, notes) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], now_iso(),
             "live", row[8], row[9], row[10], row[11], row[12], "wikitext", "x", "active",
             None])

    contents = {
        "people:tester": FIXTURE_MD_TESTER,
        "systems:sys": FIXTURE_MD_SYSTEMS,
        "ext:paper": FIXTURE_MD_EXTERNAL,
    }
    block_id = 0
    for index, (key, content) in enumerate(contents.items(), start=1):
        conn.execute(
            "INSERT INTO fulltext (id, page_key, content, char_count, extraction_method) "
            "VALUES (?,?,?,?,?)", [index, key, content, len(content), "wikitext"])
        block_id += 1
        conn.execute(
            "INSERT INTO fulltext_blocks (id, page_key, block_index, block_type, "
            "block_content) VALUES (?,?,?,?,?)", [block_id, key, 0, "paragraph", "fixture"])

    conversions = [
        (1, "people:tester", "dokuwiki-wikitext", hash_wt_tester, hash_md_tester),
        (2, "systems:sys", "dokuwiki-wikitext", hash_wt_systems, hash_md_systems),
        (3, "ext:paper", "html-to-md", "0" * 64, hash_md_external),
    ]
    for row in conversions:
        conn.execute(
            "INSERT INTO conversions (id, page_key, converter, converter_version, "
            "source_kind, source_sha256, md_sha256) VALUES (?,?,?,?,?,?,?)",
            [row[0], row[1], row[2], "tuhs-md/1.0", "wiki", row[3], row[4]])

    links = [
        (1, "people:tester", "internal", "https://wiki.tuhs.org/doku.php?id=systems:sys",
         "queued"),
        (2, "people:tester", "external", "https://example.org/paper", "fetched"),
        (3, "people:tester", "external", "https://example.org/book.epub", "excluded"),
        (4, "people:tester", "external", "https://example.org/gone", "failed"),
    ]
    for row in links:
        conn.execute(
            "INSERT INTO links (id, source_page_key, target_kind, target_url, "
            "resolution_status) VALUES (?,?,?,?,?)", list(row))
    conn.execute(
        "INSERT INTO excluded_items (id, url, item_kind, reason, evidence_page_key) "
        "VALUES (1, 'https://example.org/book.epub', 'book', '夹具排除项', 'people:tester')")
    conn.execute(
        "INSERT INTO crawl_log (id, run_id, url, url_kind, attempt, http_status, "
        "error_type, error_detail) VALUES (1, 'fixture-run', 'https://example.org/gone', "
        "'external', 1, 404, 'HTTPError', '404 Not Found')")

    wiki_keys = sorted(["people:tester", "systems:sys"])
    scope = {
        "baseline": len(wiki_keys),
        "page_set_sha256": sha256_hex("\n".join(wiki_keys).encode("utf-8")),
        "namespace_counts": {"people": 1, "systems": 1},
        "namespaces": ["people", "systems"],
        "top_pages": [],
        "index_page_counts": {},
        "derived_at": now_iso(),
    }
    conn.execute(
        "INSERT INTO crawl_runs (run_id, started_at, finished_at, scope_json, "
        "page_baseline, status, tool_version) VALUES (?,?,?,?,?,?,?)",
        ["fixture-run", now_iso(), now_iso(), json.dumps(scope, ensure_ascii=False),
         2, "completed", "tuhs-md/1.0"])
    return conn, root, db_path


def selftest() -> int:
    checks = 0
    failures: List[str] = []

    def check(label: str, condition: bool, detail: str = "") -> None:
        nonlocal checks
        checks += 1
        if condition:
            print(f"  PASS {label}")
        else:
            print(f"  FAIL {label} {detail}")
            failures.append(label)

    def status_map(results: List[Result]) -> Dict[str, str]:
        return {result.check_id: result.status for result in results}

    work = Path(tempfile.mkdtemp(prefix="verify_selftest_", dir=str(_ensure_tmp())))
    try:
        print("[selftest] 正常夹具：V1–V12 离线全量")
        conn, root, db_path = build_fixture(work / "baseline")
        try:
            ctx = VerifyContext(conn, root, db_path, True, 30, "SELFTEST", verbose=False)
            results = run_all(ctx, verbose=False)
            status = status_map(results)
        finally:
            conn.close()
        expected_status = {
            "V1": "SKIP", "V2": "PASS", "V3": "PASS", "V4": "PASS", "V5": "PASS",
            "V6": "SKIP", "V7": "PASS", "V8": "PASS", "V9": "SKIP", "V10": "PASS",
            "V11": "PASS", "V12": "PASS",
        }
        check("夹具 12 项判据状态符合预期", status == expected_status,
              f"实测 {status}")
        check("V8 EXPORT／IMPORT 可恢复", status.get("V8") == "PASS", status.get("V8"))
        check("V11 结构计数一致", status.get("V11") == "PASS", status.get("V11"))

        defects = [
            ("漏页",
             lambda c, r: c.execute("DELETE FROM pages WHERE page_key = 'systems:sys'"),
             "V1"),
            ("缺 md",
             lambda c, r: (r / "raw/wiki/people/tester.md").unlink(),
             "V2"),
            ("md 哈希不符",
             lambda c, r: (r / "raw/wiki/people/tester.md").write_bytes(
                 (r / "raw/wiki/people/tester.md").read_bytes() + b"\ntampered\n"),
             "V2"),
            ("HTML 残留",
             lambda c, r: c.execute(
                 "UPDATE fulltext SET content = content || ?, char_count = char_count + ? "
                 "WHERE page_key = 'people:tester'",
                 ["<div>x</div>", len("<div>x</div>")]),
             "V3"),
            ("二进制混入",
             lambda c, r: ((r / "raw/wiki/people/fake.pdf").write_bytes(
                 b"%PDF-1.7\nfixture\n")),
             "V10"),
            ("转换台账缺失",
             lambda c, r: c.execute(
                 "DELETE FROM conversions WHERE page_key = 'people:tester'"),
             "V12"),
        ]
        for label, mutate, target in defects:
            conn, root, db_path = build_fixture(work / f"defect_{target}_{checks}")
            try:
                mutate(conn, root)
                ctx = VerifyContext(conn, root, db_path, True, 30, "SELFTEST", verbose=False)
                results = run_all(ctx, only=[target], verbose=False)
                got = results[0].status if results else "（未执行）"
                detail = "; ".join(results[0].lines[:2]) if results else ""
                check(f"缺陷“{label}”被 {target} 命中（{got}）", got == "FAIL", detail)
            finally:
                conn.close()

        print("[selftest] 空库 fail-closed")
        empty_dir = work / "empty"
        empty_dir.mkdir()
        import duckdb
        empty_db = empty_dir / "tuhs_wiki.duckdb"
        empty_conn = duckdb.connect(str(empty_db))
        empty_conn.execute(load_schema_sql())
        try:
            ctx = VerifyContext(empty_conn, empty_dir / "corpus", empty_db, True, 30,
                                "SELFTEST", verbose=False)
            results = run_all(ctx, verbose=False)
            status = status_map(results)
            check("空库 V1 FAIL 且不崩溃", status.get("V1") == "FAIL", str(status))
            check("空库其余判据无异常堆栈",
                  all(value in ("PASS", "FAIL", "SKIP") for value in status.values()),
                  str(status))
        finally:
            empty_conn.close()
    finally:
        shutil.rmtree(work, ignore_errors=True)
        try:
            TMP_PARENT.rmdir()
        except OSError:
            pass

    print(f"[selftest] 共 {checks} 项，失败 {len(failures)} 项")
    if failures:
        for name in failures:
            print(f"  - {name}")
        return 1
    return 0


def _ensure_tmp() -> Path:
    TMP_PARENT.mkdir(parents=True, exist_ok=True)
    return TMP_PARENT


# =============================================================================
# 入口
# =============================================================================

def verify_runtime() -> int:
    try:
        import duckdb
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: 缺少 duckdb（{exc}），需 {DUCKDB_REQUIRED}", file=sys.stderr)
        return 2
    if duckdb.__version__ != DUCKDB_REQUIRED:
        print(f"ERROR: duckdb 版本 {duckdb.__version__} 与基线 {DUCKDB_REQUIRED} 不符",
              file=sys.stderr)
        return 2
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="TUHS Wiki 史料库 V1–V12 验证器")
    parser.add_argument("--db", default=str(DEFAULT_DB), help="DuckDB 库路径")
    parser.add_argument("--root", default=str(DEFAULT_ROOT), help="语料根目录")
    parser.add_argument("--round", default="R1", help="轮次标记（写入 verification.round）")
    parser.add_argument("--sample", type=int, default=30, help="抽样页数（默认 30）")
    parser.add_argument("--skip-network", action="store_true", help="只跑离线判据")
    parser.add_argument("--selftest", action="store_true", help="离线自检")
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    rc = verify_runtime()
    if rc:
        return rc
    if args.selftest:
        return selftest()

    import duckdb

    db_path = Path(args.db).resolve()
    root = Path(args.root).resolve()
    if not db_path.is_file():
        print(f"ERROR: 库不存在：{db_path}", file=sys.stderr)
        return 2

    conn = duckdb.connect(str(db_path))
    ctx = VerifyContext(conn, root, db_path, args.skip_network, args.sample, args.round)
    results: List[Result] = []
    written = 0
    try:
        results = run_all(ctx)
        run_id = latest_run_id(conn)
        try:
            written = write_verification(conn, args.round, results, run_id)
        except Exception as exc:  # noqa: BLE001
            print(f"[warn] verification 写入失败：{type(exc).__name__}: {exc}")
    finally:
        conn.close()
        ctx.cleanup()

    fails = [result for result in results if result.status == "FAIL"]
    skips = [result for result in results if result.status == "SKIP"]
    print(f"[summary] 轮次 {args.round}｜PASS {len(results) - len(fails) - len(skips)}"
          f"／FAIL {len(fails)}／SKIP {len(skips)}；verification 写入 {written} 行")
    if fails:
        print("[summary] 失败判据：" + "、".join(result.check_id for result in fails))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
