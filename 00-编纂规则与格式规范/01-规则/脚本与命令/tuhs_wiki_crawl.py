#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TUHS Wiki 全量抓取、Markdown 归一与入库（tuhs_wiki_crawl.py）。

用途
====
对 `https://wiki.tuhs.org`（Unix Heritage Wiki，DokuWiki）执行“清单发现 → 页面抓取 →
Wikitext／HTML／PDF → Markdown 归一 → 外链分类与一跳抓取 → 入库”。产物为独立史料库
`03-原始史料库/16-TUHS-Wiki史料/tuhs_wiki.duckdb`（架构见 `tuhs_wiki_schema.sql`）。

判据（规格出处 `.trae/specs/crawl-tuhs-wiki-20261025/spec.md`）
============================================================
- 禁止二进制正文落盘：只写 `.wikitext`（纯文本源）与 `.md`；HTML 只在内存中转换；PDF 只
  下载至 `script/` 临时目录，提取文本后立即删除。写盘前按扩展名与文件头魔数（`%PDF-`、
  `PK\\x03\\x04`、`\\x89PNG`、`GIF8`、`\\xFF\\xD8\\xFF`）双重守卫。
- 清单以“去重后的页面 ID 集合”为唯一口径；14 个命名空间递归 `?do=index&idx=<ns>`（含
  `&s=` 分页与子命名空间），补顶层 `start`、`syste`；页面集合排序 SHA-256 与逐命名空间
  计数写入 `crawl_runs.scope_json`。命名空间归“最长前缀”，顶层记 `(top)`。
- 每页两次请求：`do=export_raw`（Wikitext 落盘、哈希入 `sha256_source`）与
  `do=export_xhtml`（仅内存，供链接抽取与转换备选）。
- 每页恰 1 条 `fulltext`（失败页写空内容行）、1 条 `conversions` 主记录；块级结构入
  `fulltext_blocks`（`heading_path` 齐备）。
- 外链只抓一跳、按归一 URL 去重；书籍与源代码本体一律不下载，只入 `excluded_items`。
- 失效外链（404／410／5xx／超时）先查 Wayback `available` 接口，有快照取 `id_` 原始件，
  `fetch_mode='wayback'`；无快照判 `failed` 并留 `crawl_log`。
- 幂等：自然键（wiki=`page_key`，external=`canonical_url`）先查后写，插入带
  `WHERE NOT EXISTS`；`id` 动态取 `max+1`，禁止硬编码。
- 全部文本 UTF-8 无 BOM、LF；中文弯引号；不建任何旁路备份副本。

用法
====
    C:/Python314/python.exe tuhs_wiki_crawl.py --selftest
    C:/Python314/python.exe tuhs_wiki_crawl.py --dry-run
    C:/Python314/python.exe tuhs_wiki_crawl.py --limit 5 --wiki-only
    C:/Python314/python.exe tuhs_wiki_crawl.py            # 全量（Task 5 执行）
    C:/Python314/python.exe tuhs_wiki_crawl.py --refresh   # 强制重抓

参数
====
`--db` 库路径（默认真实库）；`--root` 语料目录（默认库所在目录）；`--limit N` 只处理前 N 个
wiki 页（按 `page_key` 排序）；`--resume`（默认，已 active 且 md 存在即跳过）；`--refresh`
强制重抓；`--wiki-only` 不抓外链、不做 HEAD；`--no-external` 不抓外链但仍登记链接；
`--dry-run` 只做清单与统计，不写盘不抓页面；`--selftest` 离线自检；`--run-id` 指定批次号。

退出码
======
0 成功；1 运行期失败；2 依赖／版本／配置不符（`duckdb != 2.0.0`、缺 `requests`、库不存在）。
"""

from __future__ import annotations

import argparse
import hashlib
import html as html_mod
import json
import os
import re
import shutil
import sys
import tempfile
import time
import urllib.parse as up
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)

DUCKDB_REQUIRED = "2.0.0"
BASE = "https://wiki.tuhs.org"
DOKU = BASE + "/doku.php"
USER_AGENT = (
    "librebsd-tuhs-wiki-crawl/1.0 (+https://wiki.tuhs.org; "
    "academic corpus for a BSD history project; contact: ykla)"
)
CONVERTER_VERSION = "tuhs-md/1.0"
CONVERTER_WIKITEXT = "dokuwiki-wikitext"
CONVERTER_HTML = "html-to-md"
CONVERTER_PDF = "pdf-pymupdf"
CONVERTER_OCR = "pdf-rapidocr"
CONVERTER_NONE = "none"

NAMESPACES = [
    "systems", "source", "features", "events", "people", "anecdotes", "images",
    "glossary", "publications", "misc", "wiki", "blog", "playground", "refnotes",
]
TOP_PAGES = ["start", "syste"]
NAMESPACE_SENTINEL = "(top)"
EXTERNAL_NAMESPACE = "(external)"

MIN_HOST_INTERVAL = 1.5      # 同主机最小间隔（秒）
HTTP_TIMEOUT = 30            # 单请求超时（秒）
RETRY_DELAYS = (2, 4, 8)     # 失败退避（3 次重试）
MAX_PDF_BYTES = 50 * 1024 * 1024
PDF_OCR_PAGE_LIMIT = 300
MAX_PDF_DOWNLOAD = 80 * 1024 * 1024
WAYBACK_AVAILABLE = "https://archive.org/wayback/available"

ALLOWED_TEXT_EXT = {".md", ".wikitext"}
MAGIC_SIGNATURES = [
    (b"%PDF-", "pdf"),
    (b"PK\x03\x04", "zip"),
    (b"\x89PNG", "png"),
    (b"GIF8", "gif"),
    (b"\xff\xd8\xff", "jpeg"),
]

SCRIPT_DIR = Path(__file__).resolve().parent
# 本件位于 00-编纂规则与格式规范/01-规则/脚本与命令/，上溯 3 级为仓库根
# （脚本目录 → 01-规则 → 00-编纂规则与格式规范 → 仓库根）
PROJECT_ROOT = SCRIPT_DIR.parents[2]
DEFAULT_ROOT = PROJECT_ROOT / "03-原始史料库" / "16-TUHS-Wiki史料"
DEFAULT_DB = DEFAULT_ROOT / "tuhs_wiki.duckdb"
TMP_WORKDIR = PROJECT_ROOT / "script" / "_tuhs_crawl_tmp"

SITE_HOSTS = {"wiki.tuhs.org"}

MEDIA_EXT = {
    ".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".ico", ".bmp", ".tif",
    ".tiff", ".mp3", ".mp4", ".ogg", ".oga", ".ogv", ".webm", ".mov", ".avi",
    ".wav", ".m4v", ".m4a", ".flac", ".mpg", ".mpeg",
}
BOOK_EXT = {".epub", ".mobi", ".azw", ".azw3", ".djvu", ".fb2", ".lit"}
ARCHIVE_EXT = {
    ".tar", ".tgz", ".zip", ".gz", ".bz2", ".xz", ".7z", ".iso", ".img", ".dmg",
    ".tbz2", ".txz", ".tar.gz", ".tar.bz2", ".tar.xz",
}
NON_CONTENT_DO = {
    "login", "edit", "revisions", "backlink", "media", "index", "recent", "search",
    "admin", "export_raw", "export_xhtml", "diff", "info", "subscribe", "unsubscribe",
    "denied", "preview", "conflict", "save", "draft", "recover", "cancel", "check",
    "source", "show", "locked",
}


class CrawlError(RuntimeError):
    """运行时错误（守卫命中、配置不符等）。"""


# =============================================================================
# 基础工具
# =============================================================================

def now_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha1_hex(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()


def normalize_newlines(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def guard_magic(data: bytes, label: str) -> None:
    """文件头魔数守卫：命中二进制签名即中止。"""
    for magic, kind in MAGIC_SIGNATURES:
        if data.startswith(magic):
            raise CrawlError(f"二进制守卫命中：{label} 头部为 {kind}（{magic!r}），拒绝落盘")


def write_text_guard(path: Path, text: str) -> int:
    """写纯文本：仅允许 .md／.wikitext，UTF-8 无 BOM、LF、魔数守卫。"""
    if path.suffix.lower() not in ALLOWED_TEXT_EXT:
        raise CrawlError(f"扩展名不允许落盘：{path}（只允许 .md／.wikitext）")
    text = normalize_newlines(text)
    if text.startswith("\ufeff"):
        text = text.lstrip("\ufeff")
    data = text.encode("utf-8")
    guard_magic(data, str(path))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return len(data)


def sanitize_component(name: str, limit: int = 80) -> str:
    """Windows 非法字符替换、超长截断加 8 位 SHA-1 后缀。"""
    cleaned = re.sub(r'[<>:"\\|?*\x00-\x1f]', "_", name).strip().rstrip(" .")
    if not cleaned:
        cleaned = "_"
    if len(cleaned) > limit:
        cleaned = cleaned[: limit - 9] + "-" + sha1_hex(name)[:8]
    return cleaned


def wiki_rel_paths(page_id: str, namespace: str) -> Tuple[str, str]:
    """返回（wikitext 相对路径，md 相对路径）。"""
    segments = page_id.split(":")
    ns_parts = segments[:-1]
    leaf = sanitize_component(segments[-1])
    if leaf != segments[-1]:
        leaf = sanitize_component(segments[-1][:60]) + "-" + sha1_hex(page_id)[:8]
        leaf = sanitize_component(leaf)
    prefix = "raw/wiki"
    for part in ns_parts:
        prefix += "/" + sanitize_component(part, 40)
    return f"{prefix}/{leaf}.wikitext", f"{prefix}/{leaf}.md"


def external_rel_path(canonical_url: str) -> str:
    digest = sha1_hex(canonical_url)[:16]
    host = up.urlsplit(canonical_url).netloc.lower() or "unknown-host"
    host_dir = sanitize_component(host.replace(":", "_"), 60)
    return f"raw/external/{host_dir}/{digest}.md"


def external_page_key(canonical_url: str) -> str:
    return "ext:" + sha1_hex(canonical_url)[:16]


def namespace_of(page_id: str, namespaces: Iterable[str]) -> str:
    best = None
    for ns in namespaces:
        if page_id == ns:
            cand = ns
        elif page_id.startswith(ns + ":"):
            cand = ns
        else:
            continue
        if best is None or len(cand) > len(best):
            best = cand
    return best if best else NAMESPACE_SENTINEL


def doku_page_url(page_id: str) -> str:
    return DOKU + "?id=" + up.quote(page_id, safe=":")


def media_url(media_id: str) -> str:
    return BASE + "/lib/exe/fetch.php?media=" + up.quote(media_id, safe=":")


def normalize_media_src(src: str) -> str:
    """把 DokuWiki 图片地址归一为仅含 media 参数的稳定 URL（丢弃 tok／尺寸参数）。"""
    if not src:
        return src
    absolute = up.urljoin(BASE + "/", src)
    parts = up.urlsplit(absolute)
    if parts.path.endswith("fetch.php"):
        query = up.parse_qs(parts.query)
        if "media" in query:
            return media_url(query["media"][0])
    return absolute


def title_from_wikitext(text: str, page_id: str) -> str:
    for line in normalize_newlines(text).split("\n"):
        m = re.match(r"^\s*={2,6}\s*(.+?)\s*={2,6}\s*$", line)
        if m:
            return m.group(1).strip()
    return page_id.split(":")[-1]


# =============================================================================
# HTTP 客户端（限流、重试、留痕）
# =============================================================================

class CrawlLog:
    """crawl_log 缓冲与批量写入。"""

    def __init__(self, run_id: str, flusher=None):
        self.run_id = run_id
        self.rows: List[Dict[str, Any]] = []
        self.flusher = flusher
        self.flush_size = 120

    def add(self, url: str, url_kind: str, attempt: int, http_status, nbytes,
            error_type, error_detail, started_at, finished_at, duration_ms) -> None:
        self.rows.append({
            "run_id": self.run_id,
            "url": url,
            "url_kind": url_kind,
            "attempt": attempt,
            "http_status": http_status,
            "bytes": nbytes,
            "error_type": error_type,
            "error_detail": (error_detail or "")[:500] or None,
            "started_at": started_at,
            "finished_at": finished_at,
            "duration_ms": duration_ms,
        })
        if self.flusher and len(self.rows) >= self.flush_size:
            self.flush(self.flusher)

    def flush(self, conn) -> None:
        if not self.rows:
            return
        seq = IdSeq(conn)
        for row in self.rows:
            upsert(conn, "crawl_log", ["id"], {**row, "id": seq.next("crawl_log")})
        self.rows.clear()

    def summary(self) -> Dict[str, int]:
        out: Dict[str, int] = {}
        for r in self.rows:
            key = r["url_kind"]
            out[key] = out.get(key, 0) + 1
        return out


class HttpClient:
    """同主机 ≥1.5 秒间隔、3 次重试（2／4／8 秒）、逐请求留痕。"""

    def __init__(self, log: CrawlLog):
        import requests

        self.requests = requests
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,text/plain,application/pdf;q=0.9,*/*;q=0.8",
        })
        self.log = log
        self._last_host = {}
        self.stats = {"requests": 0, "failures": 0}

    def _throttle(self, host: str) -> None:
        last = self._last_host.get(host)
        if last is not None:
            wait = MIN_HOST_INTERVAL - (time.monotonic() - last)
            if wait > 0:
                time.sleep(wait)
        self._last_host[host] = time.monotonic()

    def request(self, url: str, url_kind: str, *, stream: bool = False,
                allow_html_missing: bool = False, attempts: int = 1 + len(RETRY_DELAYS)):
        host = up.urlsplit(url).netloc.lower()
        last_error = None
        for attempt in range(1, attempts + 1):
            self._throttle(host)
            started_at = now_iso()
            t0 = time.monotonic()
            try:
                resp = self.session.get(url, timeout=HTTP_TIMEOUT, stream=stream,
                                        allow_redirects=True)
                self.stats["requests"] += 1
                nbytes = None
                if not stream:
                    nbytes = len(resp.content)
                duration = int((time.monotonic() - t0) * 1000)
                status = resp.status_code
                retry_after = resp.headers.get("Retry-After")
                self.log.add(url, url_kind, attempt, status, nbytes, None, None,
                             started_at, now_iso(), duration)
                if status in (429, 503):
                    wait = RETRY_DELAYS[min(attempt - 1, len(RETRY_DELAYS) - 1)]
                    try:
                        wait = max(wait, int(retry_after)) if retry_after else wait
                    except (TypeError, ValueError):
                        pass
                    last_error = f"http_{status}"
                    if attempt < attempts:
                        time.sleep(min(wait, 60))
                        continue
                    resp.close()
                    return None, f"http_{status}", resp
                return resp, None, None
            except Exception as exc:  # noqa: BLE001
                duration = int((time.monotonic() - t0) * 1000)
                err_type = type(exc).__name__
                detail = str(exc)
                self.stats["failures"] += 1
                self.log.add(url, url_kind, attempt, None, None, err_type, detail,
                             started_at, now_iso(), duration)
                last_error = err_type
                if attempt < attempts:
                    time.sleep(RETRY_DELAYS[attempt - 1])
        return None, last_error or "unknown_error", None

    def get_bytes(self, url: str, url_kind: str):
        resp, err, _ = self.request(url, url_kind)
        if resp is None:
            return None, err, None
        try:
            return resp.content, None, resp
        finally:
            resp.close()

    def head(self, url: str, url_kind: str = "head"):
        host = up.urlsplit(url).netloc.lower()
        self._throttle(host)
        started_at = now_iso()
        t0 = time.monotonic()
        try:
            resp = self.session.head(url, timeout=HTTP_TIMEOUT, allow_redirects=True)
            duration = int((time.monotonic() - t0) * 1000)
            self.log.add(url, url_kind, 1, resp.status_code, None, None, None,
                         started_at, now_iso(), duration)
            length = resp.headers.get("Content-Length")
            ctype = resp.headers.get("Content-Type")
            resp.close()
            try:
                return int(length) if length is not None else None, ctype
            except ValueError:
                return None, ctype
        except Exception as exc:  # noqa: BLE001
            duration = int((time.monotonic() - t0) * 1000)
            self.log.add(url, url_kind, 1, None, None, type(exc).__name__, str(exc),
                         started_at, now_iso(), duration)
            return None, None


# =============================================================================
# Wikitext → Markdown
# =============================================================================

class ConvertResult:
    def __init__(self) -> None:
        self.markdown = ""
        self.warnings: List[str] = []
        self.internal_links: List[Tuple[str, str, str]] = []   # (page_id, anchor, context)
        self.external_links: List[Tuple[str, str, str]] = []
        self.images: List[Tuple[str, str, str]] = []
        self.heading_count = 0
        self.link_count = 0
        self.code_blocks = 0
        self.table_rows = 0


class WikiTextToMarkdown:
    """DokuWiki Wikitext → Markdown 转换器（单一主页转换器）。"""

    TOKEN_OPEN = "\ue000"
    TOKEN_CLOSE = "\ue001"

    def __init__(self, page_id: str, known_pages: Optional[set] = None):
        self.page_id = page_id
        self.namespace = page_id.rsplit(":", 1)[0] if ":" in page_id else ""
        self.known_pages = known_pages or set()
        self.result = ConvertResult()
        self._tokens: List[str] = []

    # -- 内联 ---------------------------------------------------------------
    def _token(self, rendered: str) -> str:
        self._tokens.append(rendered)
        return f"{self.TOKEN_OPEN}{len(self._tokens) - 1}{self.TOKEN_CLOSE}"

    def _resolve_internal(self, target: str) -> str:
        target = target.strip()
        if target.startswith(":"):
            return target[1:]
        if target.startswith("this>"):
            raise CrawlError("interwiki-this")
        if target.startswith("doku>"):
            raise CrawlError("interwiki-doku")
        if ">" in target.split(":")[0] and target.split(">")[0].isalpha():
            raise CrawlError("interwiki")
        if target.startswith("."):
            target = target[1:]
        if self.namespace and ":" not in target:
            return f"{self.namespace}:{target}"
        return target

    def _wikilink(self, inner: str, context: str) -> str:
        if "|" in inner:
            target, label = inner.split("|", 1)
        else:
            target, label = inner, inner
        target = target.strip()
        label = label.strip() or target
        self.result.link_count += 1
        if re.match(r"^[a-z][a-z0-9+.-]*://", target, re.I):
            url = target
            self.result.external_links.append((url, label, context))
            return f"[{label}]({url})"
        try:
            page_target = self._resolve_internal(target)
        except CrawlError as exc:
            reason = str(exc)
            self.result.warnings.append(f"interwiki 未解析：[[{inner}]]（{reason}），原文保留")
            return f"[[{inner}]]"
        url = doku_page_url(page_target)
        self.result.internal_links.append((page_target, label, context))
        return f"[{label}]({url})"

    def _image(self, inner: str, context: str) -> str:
        parts = inner.split("|", 1)
        raw_target = parts[0].strip()
        alt = parts[1].strip() if len(parts) > 1 else ""
        target = raw_target.split("?", 1)[0]
        self.result.link_count += 1
        if re.match(r"^[a-z][a-z0-9+.-]*://", target, re.I):
            url = target
        else:
            media_id = target[1:] if target.startswith(":") else target
            if self.namespace and ":" not in media_id:
                media_id = f"{self.namespace}:{media_id}"
            url = media_url(media_id)
        self.result.images.append((url, alt, context))
        return f"![{alt}]({url})"

    def inline(self, text: str, context: str = "") -> str:
        if not text:
            return ""
        out = text
        # 1. 图片 {{...}}
        def img_repl(m):
            return self._token(self._image(m.group(1), context))

        out = re.sub(r"\{\{([^{}]*)\}\}", img_repl, out)

        # 2. 内链／外链 [[...]]
        def link_repl(m):
            inner = m.group(1)
            if inner.startswith("(") or "(:)" in inner:
                self.result.warnings.append(f"插件宏未解析：[[{inner}]]，原文保留")
                return m.group(0)
            return self._token(self._wikilink(inner, context))

        out = re.sub(r"\[\[([^\[\]]*)\]\]", link_repl, out)

        # 3. 等宽 ''...''
        def mono_repl(m):
            body = m.group(1)
            if not body.strip():
                return m.group(0)
            return self._token("`" + body.replace("`", "\u2018") + "`")

        out = re.sub(r"''([^''\n]+)''", mono_repl, out)

        # 4. 粗体／斜体／下划线／删除线
        out = re.sub(r"\*\*([^*\n]+)\*\*", r"**\1**", out)
        out = re.sub(r"//([^/\n]+)//", r"*\1*", out)
        out = re.sub(r"__([^_\n]+)__", r"__\1__", out)
        out = re.sub(r"~~([^~\n]+)~~", r"~~\1~~", out)

        # 5. 裸 URL
        def bare_repl(m):
            url = m.group(1)
            trailing = ""
            while url and url[-1] in ".,;:!?":
                trailing = url[-1] + trailing
                url = url[:-1]
            self.result.external_links.append((url, url, context))
            self.result.link_count += 1
            return "<" + url + ">" + trailing

        out = re.sub(r"(?<![\w\"'=])(https?://[^\s\[\]{}<>\"]+)", bare_repl, out)

        # 6. 换行 \\
        out = re.sub(r"\\\\[ \t]*(\n|$)", "  \\1", out)

        # 7. 还原 token
        def restore(m):
            idx = int(m.group(1))
            return self._tokens[idx] if 0 <= idx < len(self._tokens) else m.group(0)

        out = re.sub(re.escape(self.TOKEN_OPEN) + r"(\d+)" + re.escape(self.TOKEN_CLOSE),
                     restore, out)
        return out

    # -- 块级 ---------------------------------------------------------------
    def convert(self, source: str) -> ConvertResult:
        text = normalize_newlines(source)
        lines = text.split("\n")
        out: List[str] = []
        warnings = self.result.warnings
        i = 0
        n = len(lines)

        while i < n:
            line = lines[i]

            # 代码块 <code> / <file>
            m = re.match(r"^\s*<(code|file)([^>]*)>(.*)$", line, re.I)
            if m:
                tag, attrs, rest = m.group(1).lower(), m.group(2), m.group(3)
                lang = ""
                lm = re.search(r"(?:lang|language)\s*=\s*\"?([\w+#.-]+)", attrs, re.I)
                if lm:
                    lang = lm.group(1)
                elif attrs.strip():
                    bare = attrs.strip().split()[0]
                    if re.fullmatch(r"[\w+#.-]+", bare):
                        lang = bare
                body_lines: List[str] = []
                if re.search(rf"</{tag}>\s*$", rest, re.I):
                    body_lines.append(re.sub(rf"</{tag}>\s*$", "", rest, flags=re.I))
                else:
                    if rest.strip():
                        body_lines.append(rest)
                    i += 1
                    closed = False
                    while i < n:
                        if re.search(rf"</{tag}>", lines[i], re.I):
                            before = re.sub(rf"</{tag}>.*$", "", lines[i], flags=re.I)
                            if before:
                                body_lines.append(before)
                            closed = True
                            i += 1
                            break
                        body_lines.append(lines[i])
                        i += 1
                    if not closed:
                        warnings.append(f"<{tag}> 代码块未闭合，按到文末处理")
                out.append("")
                out.append("```" + lang)
                out.extend(body_lines)
                out.append("```")
                out.append("")
                self.result.code_blocks += 1
                continue

            # nowiki（独占行）
            m = re.match(r"^\s*<nowiki>(.*?)</nowiki>\s*$", line, re.I)
            if m:
                out.append("")
                out.append(m.group(1))
                out.append("")
                i += 1
                continue

            # 标题
            m = re.match(r"^\s*(={2,6})\s*(.*?)\s*\1\s*$", line)
            if m and m.group(2):
                level = max(1, min(6, 7 - len(m.group(1))))
                heading = self.inline(m.group(2), m.group(2))
                out.append("")
                out.append("#" * level + " " + heading)
                out.append("")
                self.result.heading_count += 1
                i += 1
                continue

            # 表格
            if re.match(r"^\s*[\|\^]", line):
                table_lines = []
                while i < n and re.match(r"^\s*[\|\^]", lines[i]):
                    table_lines.append(lines[i])
                    i += 1
                md_table, rows = self._convert_table(table_lines)
                out.append("")
                out.extend(md_table)
                out.append("")
                self.result.table_rows += rows
                continue

            # 列表
            if re.match(r"^\s*(\*|-)\s+", line) or re.match(r"^\s{0,2}(\d+)\.\s+", line):
                list_lines = []
                while i < n and (re.match(r"^\s*(\*|-)\s+", lines[i])
                                 or re.match(r"^\s{0,2}(\d+)\.\s+", lines[i])):
                    list_lines.append(lines[i])
                    i += 1
                out.append("")
                out.extend(self._convert_list(list_lines))
                out.append("")
                continue

            # 预格式化（行首 ≥2 空格）
            if re.match(r"^ {2,}\S", line):
                pre_lines = []
                while i < n and (re.match(r"^ {2,}\S", lines[i]) or lines[i].strip() == ""):
                    if lines[i].strip() == "":
                        # 空行结束预格式化块（DokuWiki 语义）
                        break
                    pre_lines.append(lines[i][2:])
                    i += 1
                out.append("")
                out.append("```")
                out.extend(pre_lines)
                out.append("```")
                out.append("")
                self.result.code_blocks += 1
                continue

            # 空行
            if line.strip() == "":
                out.append("")
                i += 1
                continue

            # 段落（连续非空行合为一段）
            para = []
            while i < n and lines[i].strip() != "" \
                    and not re.match(r"^\s*(?:={2,6}|<(?:code|file|nowiki)\b|[\|\^]|(?:\*|-)\s+)",
                                     lines[i]) \
                    and not re.match(r"^\s{0,2}\d+\.\s+", lines[i]) \
                    and not re.match(r"^ {2,}\S", lines[i]):
                para.append(lines[i])
                i += 1
            if not para:
                para.append(line)
                i += 1
            rendered = self.inline("\n".join(para), " ".join(para)[:200])
            out.append("")
            out.append(rendered)
            out.append("")

        markdown = "\n".join(out)
        markdown = re.sub(r"\n{3,}", "\n\n", markdown).strip() + "\n"
        self._detect_residue(markdown)
        self.result.markdown = markdown
        return self.result

    def _convert_list(self, lines: List[str]) -> List[str]:
        rendered: List[str] = []
        for line in lines:
            m = re.match(r"^(\s*)(\*|-)\s+(.*)$", line)
            if m:
                depth = max(0, len(m.group(1)) // 2 - 1)
                content = self.inline(m.group(3), line.strip()[:200])
                rendered.append("  " * depth + "- " + content)
                continue
            m = re.match(r"^(\s{0,2})(\d+)\.\s+(.*)$", line)
            if m:
                content = self.inline(m.group(3), line.strip()[:200])
                rendered.append("- " + content)
                continue
        return rendered

    def _convert_table(self, lines: List[str]) -> Tuple[List[str], int]:
        rows: List[Tuple[bool, List[str]]] = []
        for line in lines:
            stripped = line.strip()
            if not stripped:
                continue
            is_header = stripped.startswith("^")
            sep = "^" if is_header else "|"
            body = stripped[1:] if stripped[:1] in ("|", "^") else stripped
            if body.endswith("|") or body.endswith("^"):
                body = body[:-1]
            cells = [c.strip() for c in body.split(sep)]
            if len(cells) == 1 and sep == "|":
                cells = [c.strip() for c in body.split("|")]
            if not cells or all(c in ("", "-") for c in cells):
                continue
            rendered = [self.inline(c, stripped[:200]) for c in cells]
            rows.append((is_header, rendered))
        if not rows:
            return [], 0
        ncol = max(len(r[1]) for r in rows)
        norm = [r[1] + [""] * (ncol - len(r[1])) for r in rows]
        header = norm[0]
        out = ["| " + " | ".join(header) + " |",
               "| " + " | ".join(["---"] * ncol) + " |"]
        for row in norm[1:]:
            out.append("| " + " | ".join(row) + " |")
        return out, len(norm)

    def _detect_residue(self, markdown: str) -> None:
        patterns = [
            (r"\{\{[^{}]*\}\}", "未转换的 {{...}} 宏"),
            (r"\[\[[^\[\]]*\]\]", "未转换的 [[...]] 链接"),
            (r"\[\(:[^\[\]]*\)\]", "biblio 类插件宏 [(:...:)]"),
            (r"~~[A-Za-z_]+~~", "DokuWiki 占位宏 ~~...~~"),
            (r"<nowiki>|</nowiki>", "nowiki 标签残留"),
        ]
        for pattern, label in patterns:
            hits = re.findall(pattern, markdown)
            if hits:
                sample = hits[0][:120]
                self.result.warnings.append(f"{label} × {len(hits)}，原文保留；示例：{sample}")


# =============================================================================
# HTML → Markdown（stdlib HTMLParser）
# =============================================================================

class HtmlToMarkdown(HTMLParser):
    SKIP_TAGS = {
        "script", "style", "nav", "header", "footer", "aside", "form", "noscript",
        "svg", "iframe", "button", "select", "input", "template", "link", "meta",
    }
    BLOCK_TAGS = {
        "p", "div", "section", "article", "main", "h1", "h2", "h3", "h4", "h5",
        "h6", "ul", "ol", "pre", "table", "blockquote", "hr", "br", "tr", "td",
        "th", "li", "dd", "dt", "dl", "figure", "figcaption",
    }

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: List[str] = []
        self.skip_stack: List[str] = []
        self.pre_depth = 0
        self.pre_buf: List[str] = []
        self.list_stack: List[Dict[str, Any]] = []
        self.link_stack: List[Dict[str, Any]] = []
        self.links: List[Tuple[str, str, str]] = []
        self.images: List[Tuple[str, str, str]] = []
        self.rows: List[Tuple[List[bool], List[str]]] = []
        self.row: Optional[Dict[str, Any]] = None
        self.cell: Optional[List[str]] = None
        self.in_title = False
        self.title_parts: List[str] = []
        self.table_depth = 0
        self.warnings: List[str] = []
        self.heading_count = 0
        self.code_blocks = 0
        self.table_rows = 0
        self._recent_text: List[str] = []
        self._skip_div_classes = {"docinfo", "no", "a11y", "breadcrumbs", "trace",
                                  "pageId", "docinfo".lower(), "tools"}

    # -- 输出 ---------------------------------------------------------------
    def emit(self, text: str) -> None:
        self.parts.append(text)

    def blank(self) -> None:
        if self.parts and not self.parts[-1].endswith("\n\n"):
            if self.parts[-1].endswith("\n"):
                self.parts.append("\n")
            else:
                self.parts.append("\n\n")

    # -- HTMLParser 回调 -----------------------------------------------------
    def handle_starttag(self, tag: str, attrs_list) -> None:
        tag = tag.lower()
        attrs = {k.lower(): (v or "") for k, v in attrs_list}
        if self.skip_stack:
            if tag not in {"br", "img", "hr", "meta", "link", "input"}:
                self.skip_stack.append(tag)
            return
        if tag in self.SKIP_TAGS:
            self.skip_stack.append(tag)
            return
        if tag == "div" and attrs.get("class", "").lower() in self._skip_div_classes:
            self.skip_stack.append(tag)
            return

        if tag == "title":
            self.in_title = True
            return
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            level = int(tag[1])
            self.blank()
            self.emit("#" * level + " ")
            self.heading_count += 1
            return
        if tag == "p":
            self.blank()
            return
        if tag == "br":
            self.emit("  \n")
            return
        if tag == "hr":
            self.blank()
            self.emit("---")
            self.blank()
            return
        if tag in ("ul", "ol"):
            self.list_stack.append({"type": tag, "counter": 0})
            return
        if tag == "li":
            depth = max(0, len(self.list_stack) - 1)
            marker = "-"
            if self.list_stack and self.list_stack[-1]["type"] == "ol":
                self.list_stack[-1]["counter"] += 1
                marker = f"{self.list_stack[-1]['counter']}."
            self.emit("\n" + "  " * depth + marker + " ")
            return
        if tag == "pre":
            self.pre_depth += 1
            self.pre_buf = []
            self.blank()
            self.emit("```\n")
            self.code_blocks += 1
            return
        if tag == "code":
            if self.pre_depth:
                return
            self.emit("`")
            return
        if tag in ("table",):
            self.table_depth += 1
            self.rows = []
            return
        if tag == "tr":
            self.row = {"headers": [], "cells": []}
            return
        if tag in ("td", "th"):
            self.cell = []
            if self.row is not None:
                self.row["headers"].append(tag == "th")
            return
        if tag == "blockquote":
            self.blank()
            self.emit("> ")
            return
        if tag == "a":
            href = attrs.get("href", "")
            self.link_stack.append({"href": href, "text": []})
            self.emit("[")
            return
        if tag == "img":
            src = attrs.get("src", "")
            alt = attrs.get("alt", "")
            self.emit(f"![{alt}]({src})")
            self.images.append((src, alt, "".join(self._recent_text)[-160:]))
            return
        if tag in ("strong", "b"):
            self.emit("**")
            return
        if tag in ("em", "i"):
            self.emit("*")
            return
        if tag in ("div", "section", "article", "main", "figure", "figcaption"):
            self.blank()
            return
        if tag in ("dd", "dt"):
            self.emit("\n" + "- ")
            return

    def handle_startendtag(self, tag: str, attrs_list) -> None:
        # 自闭合标签（如 <img/>）只走开始标签逻辑，避免误触发结束标签出栈
        self.handle_starttag(tag, attrs_list)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if self.skip_stack:
            self.skip_stack.pop()
            return
        if tag == "title":
            self.in_title = False
            return
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.blank()
            return
        if tag == "p":
            self.blank()
            return
        if tag in ("ul", "ol"):
            if self.list_stack:
                self.list_stack.pop()
            self.blank()
            return
        if tag == "li":
            return
        if tag == "pre":
            body = "".join(self.pre_buf)
            self.emit(body)
            if not body.endswith("\n"):
                self.emit("\n")
            self.emit("```\n\n")
            self.pre_depth = max(0, self.pre_depth - 1)
            return
        if tag == "code":
            if not self.pre_depth:
                self.emit("`")
            return
        if tag == "table":
            self.emit(self._flush_table())
            self.table_depth = max(0, self.table_depth - 1)
            return
        if tag == "tr":
            if self.row is not None:
                self.rows.append((self.row["headers"], self.row["cells"]))
                self.row = None
            return
        if tag in ("td", "th"):
            if self.cell is not None and self.row is not None:
                text = self._clean_cell("".join(self.cell))
                self.row["cells"].append(text)
            self.cell = None
            return
        if tag == "a":
            if self.link_stack:
                info = self.link_stack.pop()
                text = "".join(info["text"]).strip()
                href = info["href"]
                if not text:
                    text = href
                self.emit(f"]({href})")
                self.links.append((href, text, "".join(self._recent_text)[-160:]))
            return
        if tag in ("strong", "b"):
            self.emit("**")
            return
        if tag in ("em", "i"):
            self.emit("*")
            return
        if tag in ("div", "section", "article", "main", "figure", "figcaption"):
            self.blank()
            return
        if tag == "blockquote":
            self.blank()
            return

    def handle_data(self, data: str) -> None:
        if self.skip_stack:
            return
        if self.in_title:
            self.title_parts.append(data)
            return
        if self.pre_depth:
            self.pre_buf.append(data)
            return
        if self.cell is not None:
            self.cell.append(data)
            self._recent_text.append(data)
            return
        if self.link_stack:
            self.link_stack[-1]["text"].append(data)
            self._recent_text.append(data)
            text = re.sub(r"\s+", " ", data)
            if text.strip():
                if self.parts and self.parts[-1].endswith("\n\n"):
                    text = text.lstrip()
                self.emit(text)
            return
        text = re.sub(r"\s+", " ", data)
        if text.strip():
            if self.parts and self.parts[-1].endswith("\n\n"):
                text = text.lstrip()
            self.emit(text)
            self._recent_text.append(text)
            if len(self._recent_text) > 40:
                del self._recent_text[:-20]

    # -- 辅助 ---------------------------------------------------------------
    def _clean_cell(self, text: str) -> str:
        text = re.sub(r"\s+", " ", text).strip()
        return text.replace("|", "\\|")

    def _flush_table(self) -> str:
        rows = [(h, c) for h, c in self.rows if c]
        if not rows:
            return "\n"
        ncol = max(len(c) for _, c in rows)
        norm = [c + [""] * (ncol - len(c)) for _, c in rows]
        out = ["\n\n", "| " + " | ".join(norm[0]) + " |", "\n",
               "| " + " | ".join(["---"] * ncol) + " |", "\n"]
        for row in norm[1:]:
            out.append("| " + " | ".join(row) + " |")
            out.append("\n")
        out.append("\n")
        self.table_rows = len(norm)
        return "".join(out)

    @property
    def title(self) -> str:
        return re.sub(r"\s+", " ", "".join(self.title_parts)).strip()

    def markdown(self) -> str:
        text = "".join(self.parts)
        text = text.replace("\u00a0", " ")
        text = re.sub(r"\n{3,}", "\n\n", text)
        lines = []
        for line in text.split("\n"):
            stripped = line.rstrip(" \t")
            if line.endswith("  ") and stripped:
                stripped += "  "
            lines.append(stripped)
        cleaned = "\n".join(lines).strip()
        if cleaned:
            cleaned += "\n"
        return cleaned


def html_to_markdown(html_text: str) -> HtmlToMarkdown:
    parser = HtmlToMarkdown()
    parser.feed(html_text)
    parser.close()
    return parser


# =============================================================================
# PDF → Markdown
# =============================================================================

def pdf_to_markdown(pdf_path: Path, size_bytes: int) -> Tuple[str, str, List[str]]:
    """返回（markdown, extraction_method, warnings）。"""
    warnings: List[str] = []
    try:
        import fitz  # type: ignore
    except Exception:  # noqa: BLE001
        raise CrawlError("pymupdf 不可用，无法转换 PDF")
    doc = fitz.open(str(pdf_path))
    page_count = doc.page_count
    pages_text: List[str] = []
    for page in doc:
        try:
            pages_text.append(page.get_text("text"))
        except Exception as exc:  # noqa: BLE001
            pages_text.append("")
            warnings.append(f"第 {page.number + 1} 页文本层提取异常：{exc}")
    total_chars = sum(len(t.strip()) for t in pages_text)
    method = "pdf-text"
    if total_chars < 10 * max(1, page_count):
        method = "pdf-ocr"
        ocr_text, ocr_warn = _ocr_pdf(doc, page_count, size_bytes)
        warnings.extend(ocr_warn)
        if ocr_text is not None:
            pages_text = ocr_text
            method = "pdf-ocr"
        else:
            method = "needs_ocr_deferred"
    doc.close()

    parts: List[str] = []
    for idx, text in enumerate(pages_text, start=1):
        parts.append(f"[[page={idx}]]")
        body = normalize_newlines(text).strip()
        if body:
            parts.append(body)
        parts.append("")
    markdown = "\n".join(parts).strip() + "\n"
    return markdown, method, warnings


def _ocr_pdf(doc, page_count: int, size_bytes: int) -> Tuple[Optional[List[str]], List[str]]:
    warnings: List[str] = []
    if page_count > PDF_OCR_PAGE_LIMIT:
        warnings.append(f"页数 {page_count} 超过 OCR 上限 {PDF_OCR_PAGE_LIMIT}，转 needs_ocr_deferred")
        return None, warnings
    if size_bytes > MAX_PDF_BYTES:
        warnings.append(f"PDF 体积 {size_bytes} 超过 OCR 上限 {MAX_PDF_BYTES}，转 needs_ocr_deferred")
        return None, warnings
    try:
        from rapidocr_onnxruntime import RapidOCR  # type: ignore
        import numpy as np  # type: ignore
    except Exception as exc:  # noqa: BLE001
        warnings.append(f"RapidOCR 不可用（{exc}），转 needs_ocr_deferred")
        return None, warnings
    engine = RapidOCR()
    out: List[str] = []
    for page in doc:
        try:
            pix = page.get_pixmap(dpi=200)
            arr = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
            result, _ = engine(arr)
            lines = [item[1] for item in (result or [])]
            out.append("\n".join(lines))
        except Exception as exc:  # noqa: BLE001
            warnings.append(f"第 {page.number + 1} 页 OCR 失败：{exc}")
            out.append("")
    return out, warnings


# =============================================================================
# 链接归一与分类
# =============================================================================

TRAILING_PUNCT = ".,;:!?'\")]}"


def canonicalize_url(url: str, base_url: str = BASE + "/") -> str:
    url = html_mod.unescape(url.strip()).rstrip(TRAILING_PUNCT)
    if not url:
        return ""
    parts = up.urlsplit(url)
    if not parts.scheme:
        url = up.urljoin(base_url, url)
        parts = up.urlsplit(url)
    scheme = parts.scheme.lower()
    netloc = parts.netloc.lower()
    if netloc.endswith(":80") and scheme == "http":
        netloc = netloc[:-3]
    if netloc.endswith(":443") and scheme == "https":
        netloc = netloc[:-4]
    path = parts.path or "/"
    while path and path[-1] in TRAILING_PUNCT and len(path) > 1:
        path = path[:-1]
    query = parts.query
    return up.urlunsplit((scheme, netloc, path.rstrip("/") or "/", query, ""))


def alternate_url(url: str) -> Optional[str]:
    """失效链接的确定性替代端点（仅限已实测可用的镜像/新域名）。"""
    parts = up.urlsplit(url)
    host = parts.netloc.lower()
    path = parts.path or ""
    if host in ("www.freebsd.org", "freebsd.org") and path.startswith("/cgi/man.cgi"):
        return up.urlunsplit((parts.scheme or "https", "man.freebsd.org", path, parts.query, ""))
    if host == "minnie.cs.adfa.oz.au" and path.startswith("/PUPS"):
        return up.urlunsplit(("https", "minnie.tuhs.org", path, parts.query, ""))
    return None


def url_extension(canonical: str) -> str:
    path = up.urlsplit(canonical).path.lower()
    name = path.rsplit("/", 1)[-1]
    for ext in (".tar.gz", ".tar.bz2", ".tar.xz"):
        if name.endswith(ext):
            return ext
    return os.path.splitext(name)[1]


class UrlClassifier:
    """确定性分类，按 spec“书籍与源代码排除”顺序判定。"""

    def __init__(self, known_pages: set, http: Optional[HttpClient] = None,
                 head_check: bool = True):
        self.known_pages = known_pages
        self.http = http
        self.head_check = head_check
        self.head_cache: Dict[str, Tuple[Optional[int], Optional[str]]] = {}

    def head_size(self, url: str) -> Tuple[Optional[int], Optional[str]]:
        if not self.head_check or self.http is None:
            return None, None
        if url in self.head_cache:
            return self.head_cache[url]
        size, ctype = self.http.head(url)
        self.head_cache[url] = (size, ctype)
        return size, ctype

    def classify(self, raw_url: str, anchor: str, page_id: str,
                 page_url: str) -> Dict[str, Any]:
        if raw_url.strip().startswith("#"):
            return {
                "raw": raw_url, "canonical": raw_url.strip(), "kind": "non_content",
                "target_page_key": None, "resolution_status": "skipped",
                "exclude_kind": None, "reason": "锚点链接", "review_flag": 0,
                "content_length": None, "content_type": None,
            }
        canonical = canonicalize_url(raw_url, page_url)
        result = {
            "raw": raw_url,
            "canonical": canonical,
            "kind": "external",
            "target_page_key": None,
            "resolution_status": "queued",
            "exclude_kind": None,
            "reason": None,
            "review_flag": 0,
            "content_length": None,
            "content_type": None,
        }
        if not canonical:
            result.update(kind="non_content", resolution_status="skipped",
                          reason="空链接")
            return result

        parts = up.urlsplit(canonical)
        scheme = parts.scheme.lower()
        host = parts.netloc.lower()
        path = parts.path or ""
        ext = url_extension(canonical)
        anchor_l = (anchor or "").lower()

        # 1. 动作类／非内容
        if scheme in ("mailto", "javascript", "tel", "data", "irc", "news"):
            result.update(kind="non_content", resolution_status="skipped",
                          reason=f"非内容协议 {scheme}:")
            return result
        if canonical.startswith("#") or scheme == "":
            result.update(kind="non_content", resolution_status="skipped",
                          reason="锚点链接")
            return result
        if parts.path.endswith(("feed.php", "opensearch.php", "manifest.php")):
            result.update(kind="non_content", resolution_status="skipped",
                          reason="站点导出／订阅接口")
            return result
        if re.search(r"/lib/exe/(css|js|indexer|img|taskrunner)\.php", path, re.I):
            result.update(kind="non_content", resolution_status="skipped",
                          reason="站点静态资源接口")
            return result
        if path.startswith("/lib/tpl/") or path.startswith("/lib/images/"):
            result.update(kind="non_content", resolution_status="skipped",
                          reason="站点模板资源")
            return result
        query = up.parse_qs(parts.query)
        if "do" in query:
            do_value = (query["do"][0] or "").lower()
            if do_value and do_value not in ("show",):
                if do_value in NON_CONTENT_DO or do_value not in ("", "show"):
                    result.update(kind="non_content", resolution_status="skipped",
                                  reason=f"站点动作 URL（do={do_value}）")
                    return result

        # 2. 媒体（仅登记）
        if ext in MEDIA_EXT or "fetch.php" in path and "media=" in parts.query \
                or "/_media/" in path:
            result.update(kind="media", resolution_status="registered",
                          reason="图片／音视频本体，仅登记不下载")
            return result

        # 3. 书籍
        if ext in BOOK_EXT:
            result.update(kind="excluded_book", resolution_status="excluded",
                          exclude_kind="book",
                          reason=f"电子书扩展名 {ext}")
            return result
        if re.search(r"/books?/", path, re.I):
            result.update(kind="excluded_book", resolution_status="excluded",
                          exclude_kind="book",
                          reason="URL 路径属书库目录（/Books/）",
                          review_flag=1)
            return result
        if ext == ".pdf":
            size, ctype = self.head_size(canonical)
            result["content_length"] = size
            result["content_type"] = ctype
            name_hint = anchor_l + " " + path.rsplit("/", 1)[-1].lower()
            if "book" in name_hint and (size is None or size > 20 * 1024 * 1024):
                result.update(kind="excluded_book", resolution_status="excluded",
                              exclude_kind="book",
                              reason=f"PDF 链接文本／文件名含 book 且体积 {size}",
                              review_flag=1 if size is None else 0)
                return result
            if size is not None and size > MAX_PDF_BYTES:
                result.update(kind="excluded_book", resolution_status="excluded",
                              exclude_kind="book",
                              reason=f"PDF 体积 {size} 超过 50 MB，待人工复核",
                              review_flag=1)
                return result

        # 4. 源代码本体
        if ext in ARCHIVE_EXT:
            result.update(kind="excluded_source", resolution_status="excluded",
                          exclude_kind="source_code",
                          reason=f"源码／镜像压缩包扩展名 {ext}")
            return result
        if "cgi-bin/utree.pl" in path:
            result.update(kind="excluded_source", resolution_status="excluded",
                          exclude_kind="source_code", reason="Unix Tree 源码浏览入口")
            return result
        if host == "raw.githubusercontent.com" or host.endswith(".raw.githubusercontent.com"):
            result.update(kind="excluded_source", resolution_status="excluded",
                          exclude_kind="source_code", reason="GitHub raw 文件直链")
            return result

        # 5. 站内
        if host in SITE_HOSTS:
            target = None
            if "id" in query:
                target = query["id"][0]
            elif path in ("/", "/doku.php", "/index.php") and "id" not in query:
                target = "start"
            if target:
                target = target.replace(" ", "_")
                result.update(kind="internal", target_page_key=target,
                              resolution_status=("queued" if target in self.known_pages
                                                 else "broken_internal"),
                              reason=None)
                return result
            result.update(kind="non_content", resolution_status="skipped",
                          reason="站内非页面 URL")
            return result

        # 6. 站外
        if scheme in ("http", "https"):
            result.update(kind="external", resolution_status="queued")
            return result
        result.update(kind="non_content", resolution_status="skipped",
                      reason=f"未支持的协议 {scheme}")
        return result


def extract_wikitext_urls(source: str) -> List[Tuple[str, str, str]]:
    """从 Wikitext 抽裸 URL（链接语法之外的纯文本 URL）。"""
    out: List[Tuple[str, str, str]] = []
    cleaned = re.sub(r"\[\[[^\[\]]*\]\]", " ", normalize_newlines(source))
    cleaned = re.sub(r"\{\{[^{}]*\}\}", " ", cleaned)
    for m in re.finditer(r"(https?://[^\s\[\]{}<>\"|]+)", cleaned):
        url = m.group(1)
        start = max(0, m.start() - 60)
        context = cleaned[start:m.end() + 60].strip()
        out.append((url, url, context))
    return out


# =============================================================================
# Markdown 块解析
# =============================================================================

BLOCK_HEADING = "heading"
BLOCK_PARAGRAPH = "paragraph"
BLOCK_LIST_ITEM = "list_item"
BLOCK_CODE = "code_block"
BLOCK_QUOTE = "quote"
BLOCK_TABLE_ROW = "table_row"
BLOCK_IMAGE = "image_placeholder"
BLOCK_PAGE_BREAK = "page_break"


def parse_markdown_blocks(markdown: str) -> List[Dict[str, Any]]:
    lines = normalize_newlines(markdown).split("\n")
    blocks: List[Dict[str, Any]] = []
    heading_stack: List[Tuple[int, str]] = []
    offset = 0
    idx = 0
    n = len(lines)

    def heading_path() -> str:
        return " > ".join(text for _, text in heading_stack)

    while idx < n:
        line = lines[idx]
        line_start = offset
        stripped = line.strip()

        if stripped.startswith("```"):
            offset += len(line) + 1
            idx += 1
            code_lines = []
            while idx < n:
                if lines[idx].strip().startswith("```"):
                    offset += len(lines[idx]) + 1
                    idx += 1
                    break
                code_lines.append(lines[idx])
                offset += len(lines[idx]) + 1
                idx += 1
            body = "\n".join(code_lines)
            blocks.append({
                "block_type": BLOCK_CODE,
                "block_level": None,
                "heading_path": heading_path(),
                "block_content": body,
                "block_page": None,
                "start": line_start,
                "end": offset,
            })
            continue

        if stripped == "":
            offset += len(line) + 1
            idx += 1
            continue

        m = re.match(r"^\[\[page=(\d+)\]\]$", stripped)
        if m:
            blocks.append({
                "block_type": BLOCK_PAGE_BREAK,
                "block_level": None,
                "heading_path": heading_path(),
                "block_content": stripped,
                "block_page": int(m.group(1)),
                "start": line_start,
                "end": line_start + len(line),
            })
            offset += len(line) + 1
            idx += 1
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            level = len(m.group(1))
            text = m.group(2).strip()
            while heading_stack and heading_stack[-1][0] >= level:
                heading_stack.pop()
            heading_stack.append((level, text))
            blocks.append({
                "block_type": BLOCK_HEADING,
                "block_level": level,
                "heading_path": heading_path(),
                "block_content": text,
                "block_page": None,
                "start": line_start,
                "end": line_start + len(line),
            })
            offset += len(line) + 1
            idx += 1
            continue

        if re.match(r"^\s*\|", line):
            if re.match(r"^\s*\|[\s:\-|]+\|\s*$", line):
                offset += len(line) + 1
                idx += 1
                continue
            blocks.append({
                "block_type": BLOCK_TABLE_ROW,
                "block_level": 0,
                "heading_path": heading_path(),
                "block_content": stripped,
                "block_page": None,
                "start": line_start,
                "end": line_start + len(line),
            })
            offset += len(line) + 1
            idx += 1
            continue

        m = re.match(r"^(\s*)([-*+]|\d+\.)\s+(.*)$", line)
        if m:
            level = len(m.group(1)) // 2
            blocks.append({
                "block_type": BLOCK_LIST_ITEM,
                "block_level": level,
                "heading_path": heading_path(),
                "block_content": m.group(3).strip(),
                "block_page": None,
                "start": line_start,
                "end": line_start + len(line),
            })
            offset += len(line) + 1
            idx += 1
            continue

        if stripped.startswith(">"):
            quote_lines = []
            while idx < n and lines[idx].strip().startswith(">"):
                quote_lines.append(lines[idx].strip()[1:].strip())
                offset += len(lines[idx]) + 1
                idx += 1
            blocks.append({
                "block_type": BLOCK_QUOTE,
                "block_level": None,
                "heading_path": heading_path(),
                "block_content": " ".join(q for q in quote_lines if q),
                "block_page": None,
                "start": line_start,
                "end": offset,
            })
            continue

        if re.match(r"^!\[[^\]]*\]\([^)]*\)\s*$", stripped):
            blocks.append({
                "block_type": BLOCK_IMAGE,
                "block_level": None,
                "heading_path": heading_path(),
                "block_content": stripped,
                "block_page": None,
                "start": line_start,
                "end": line_start + len(line),
            })
            offset += len(line) + 1
            idx += 1
            continue

        para_lines = []
        while idx < n:
            current = lines[idx]
            if current.strip() == "":
                break
            if re.match(r"^(#{1,6})\s+", current) or current.strip().startswith("```"):
                break
            if re.match(r"^\s*\|", current) or re.match(r"^(\s*)([-*+]|\d+\.)\s+", current):
                break
            if current.strip().startswith(">") or re.match(r"^\[\[page=\d+\]\]$", current.strip()):
                break
            para_lines.append(current.strip())
            offset += len(current) + 1
            idx += 1
        if para_lines:
            blocks.append({
                "block_type": BLOCK_PARAGRAPH,
                "block_level": None,
                "heading_path": heading_path(),
                "block_content": " ".join(para_lines),
                "block_page": None,
                "start": line_start,
                "end": offset - 1 if offset > line_start else line_start,
            })
        else:
            offset += len(line) + 1
            idx += 1

    return blocks


# =============================================================================
# 数据库工具
# =============================================================================

def qident(name: str) -> str:
    return '"' + name.replace('"', '""') + '"'


class IdSeq:
    def __init__(self, conn) -> None:
        self.conn = conn
        self.cache: Dict[str, int] = {}

    def next(self, table: str) -> int:
        if table not in self.cache:
            value = self.conn.execute(
                f"SELECT COALESCE(MAX(id), 0) FROM {qident(table)}").fetchone()[0]
            self.cache[table] = int(value)
        self.cache[table] += 1
        return self.cache[table]


def upsert(conn, table: str, key_cols: List[str], row: Dict[str, Any],
           id_col: Optional[str] = "id",
           seq: Optional[IdSeq] = None) -> Tuple[Optional[int], bool]:
    """先查后写：返回（id，是否新增）。插入带 WHERE NOT EXISTS 兜底。

    `id_col=None` 用于主键即自然键的表（如 `crawl_runs.run_id`）。
    """
    where = " AND ".join(f"{qident(k)} = ?" for k in key_cols)
    params = [row[k] for k in key_cols]
    if id_col is None:
        existing = conn.execute(
            f"SELECT 1 FROM {qident(table)} WHERE {where}", params).fetchone()
    else:
        existing = conn.execute(
            f"SELECT {qident(id_col)} FROM {qident(table)} WHERE {where}", params).fetchone()
    if existing is not None:
        set_cols = [c for c in row if c not in key_cols and c != id_col]
        if set_cols:
            assignments = ", ".join(f"{qident(c)} = ?" for c in set_cols)
            conn.execute(f"UPDATE {qident(table)} SET {assignments} WHERE {where}",
                         [row[c] for c in set_cols] + [row[k] for k in key_cols])
        return (int(existing[0]) if id_col else None), False
    if id_col is None:
        data = dict(row)
    else:
        if seq is None:
            seq = IdSeq(conn)
        data = {id_col: seq.next(table), **row}
    cols = list(data)
    placeholders = ", ".join("?" for _ in cols)
    conn.execute(
        f"INSERT INTO {qident(table)} ({', '.join(qident(c) for c in cols)}) "
        f"SELECT {placeholders} WHERE NOT EXISTS "
        f"(SELECT 1 FROM {qident(table)} WHERE {where})",
        [data[c] for c in cols] + [row[k] for k in key_cols])
    return (data.get(id_col) if id_col else None), True


def open_database(db_path: Path):
    import duckdb

    conn = duckdb.connect(str(db_path))
    return conn


# =============================================================================
# 清单发现
# =============================================================================

def parse_index_page(html_text: str) -> Tuple[set, set, set]:
    """返回（页面 ID 集合，子命名空间集合，索引分页偏移集合）。"""
    pages = set()
    for raw in re.findall(r"doku\.php\?id=([^\"&'#]+)", html_text):
        page_id = up.unquote(raw).strip()
        if page_id:
            pages.add(page_id)
    subnamespaces = set()
    for raw in re.findall(r"idx=([^\"&'>]+)", html_text):
        value = up.unquote(raw).strip()
        if value and ":" in value:
            subnamespaces.add(value)
    offsets = set()
    for raw in re.findall(r"(?:&amp;|&)s=(\d+)", html_text):
        offsets.add(int(raw))
    return pages, subnamespaces, offsets


def discover_pages(http: HttpClient) -> Tuple[Dict[str, str], Dict[str, Any]]:
    """递归派生页面集合；返回（page_id → namespace，scope 摘要）。"""
    queue: List[str] = list(NAMESPACES)
    seen_ns: List[str] = []
    all_pages: set = set()
    counts_by_index: Dict[str, int] = {}
    index_errors: List[str] = []

    while queue:
        ns = queue.pop(0)
        if ns in seen_ns:
            continue
        seen_ns.append(ns)
        fetched_offsets = set()
        offsets_todo = [None]
        while offsets_todo:
            offset = offsets_todo.pop(0)
            if offset is not None:
                if offset in fetched_offsets:
                    continue
                fetched_offsets.add(offset)
            url = DOKU + "?do=index&idx=" + up.quote(ns)
            if offset is not None:
                url += f"&s={offset}"
            body, err, _resp = http.get_bytes(url, "index")
            if body is None:
                index_errors.append(f"{ns}{'@' + str(offset) if offset else ''}: {err}")
                break
            html_text = body.decode("utf-8", "replace")
            pages, subs, offsets = parse_index_page(html_text)
            all_pages |= pages
            counts_by_index[ns] = counts_by_index.get(ns, 0) + len(pages)
            for sub in sorted(subs):
                top = sub.split(":")[0]
                if top in NAMESPACES and sub not in seen_ns and sub not in queue:
                    queue.append(sub)
            for off in sorted(offsets):
                if off not in fetched_offsets and off not in offsets_todo:
                    offsets_todo.append(off)

    all_pages |= set(TOP_PAGES)
    namespaces = sorted(set(seen_ns) | set(NAMESPACES))
    assignment = {page_id: namespace_of(page_id, namespaces) for page_id in all_pages}
    ordered = sorted(all_pages)
    digest = sha256_hex("\n".join(ordered).encode("utf-8"))
    ns_counts: Dict[str, int] = {}
    for page_id in ordered:
        ns = assignment[page_id]
        ns_counts[ns] = ns_counts.get(ns, 0) + 1
    scope = {
        "baseline": len(ordered),
        "page_set_sha256": digest,
        "namespace_counts": dict(sorted(ns_counts.items())),
        "namespaces": namespaces,
        "index_page_counts": dict(sorted(counts_by_index.items())),
        "top_pages": list(TOP_PAGES),
        "index_errors": index_errors,
        "derived_at": now_iso(),
    }
    return assignment, scope


# =============================================================================
# 抓取与转换
# =============================================================================

def content_type_of(resp) -> str:
    if resp is None:
        return ""
    return (resp.headers.get("Content-Type") or "").lower()


def fetch_wiki_page(http: HttpClient, page_id: str) -> Dict[str, Any]:
    quoted = up.quote(page_id, safe=":")
    raw_url = DOKU + "?do=export_raw&id=" + quoted
    xhtml_url = DOKU + "?do=export_xhtml&id=" + quoted
    result: Dict[str, Any] = {
        "page_id": page_id,
        "raw_url": raw_url,
        "xhtml_url": xhtml_url,
        "status": "failed",
        "error_type": None,
        "error_detail": None,
        "http_status": None,
        "content_type": None,
        "etag": None,
        "last_modified": None,
        "raw_bytes": None,
        "wikitext": None,
        "xhtml": None,
        "notes": [],
    }
    resp, err, _ = http.request(raw_url, "wiki_raw")
    if resp is None:
        result["error_type"] = err or "request_failed"
        result["error_detail"] = f"export_raw 请求失败：{err}"
        return result
    result["http_status"] = resp.status_code
    ctype = content_type_of(resp)
    result["content_type"] = ctype
    result["etag"] = resp.headers.get("ETag")
    result["last_modified"] = resp.headers.get("Last-Modified")
    body = resp.content
    resp.close()
    result["raw_bytes"] = body
    if resp.status_code >= 400:
        result["error_type"] = f"http_{resp.status_code}"
        result["error_detail"] = f"export_raw 返回 {resp.status_code}"
        return result
    if "text/plain" not in ctype:
        # 少数系统页（如 wiki:syntax）禁用 export_raw，回退 export_xhtml：
        # 以 HTML 正文转纯文本作为 .wikitext 源，HTML 原文不落盘。
        resp2, err2, _ = http.request(xhtml_url, "wiki_xhtml")
        if resp2 is not None and resp2.status_code < 400:
            xhtml = resp2.content.decode("utf-8", "replace")
            resp2.close()
            conv = html_to_markdown(xhtml)
            result["xhtml"] = xhtml
            result["wikitext"] = conv.markdown()
            result["source_format"] = "html"
            result["notes"].append(
                f"export_raw Content-Type={ctype}，按 export_xhtml 正文降级为纯文本源")
            result["status"] = "active"
            return result
        if resp2 is not None:
            resp2.close()
        result["error_type"] = "page_missing_or_not_plain"
        result["error_detail"] = f"export_raw Content-Type={ctype}；export_xhtml 亦失败：{err2}"
        return result
    decode_errors = []
    try:
        wikitext = body.decode("utf-8")
    except UnicodeDecodeError:
        wikitext = body.decode("utf-8", "replace")
        decode_errors.append("UTF-8 解码含替换字符")
    result["wikitext"] = wikitext
    if "\r" in wikitext:
        result["notes"].append("wikitext 原含 CR，落盘统一为 LF")
    result["notes"].extend(decode_errors)

    # xhtml 仅内存
    resp2, err2, _ = http.request(xhtml_url, "wiki_xhtml")
    if resp2 is not None:
        if resp2.status_code < 400:
            result["xhtml"] = resp2.content.decode("utf-8", "replace")
        resp2.close()
    else:
        result["notes"].append(f"export_xhtml 失败：{err2}（改用 Wikitext 抽取链接）")
    result["status"] = "active"
    return result


def convert_page(page_id: str, fetched: Dict[str, Any],
                 known_pages: set) -> Dict[str, Any]:
    wikitext = fetched.get("wikitext") or ""
    xhtml = fetched.get("xhtml") or ""
    warnings: List[str] = []
    converter = CONVERTER_WIKITEXT
    converter_version = CONVERTER_VERSION
    internal: List[Tuple[str, str, str]] = []
    external: List[Tuple[str, str, str]] = []
    images: List[Tuple[str, str, str]] = []
    extraction_method = "wikitext"

    wiki_conv = WikiTextToMarkdown(page_id, known_pages)
    wiki_result = wiki_conv.convert(wikitext)
    markdown = wiki_result.markdown
    warnings.extend(wiki_result.warnings)
    internal.extend(wiki_result.internal_links)
    external.extend(wiki_result.external_links)
    images.extend(wiki_result.images)

    if fetched.get("source_format") == "html" and xhtml:
        html_conv = html_to_markdown(xhtml)
        markdown = html_conv.markdown()
        converter = CONVERTER_HTML
        extraction_method = "html"
        warnings.append("export_raw 不可用，改用 export_xhtml 转换")
        for href, anchor, ctx in html_conv.links:
            if "doku.php?id=" in href:
                parsed = up.parse_qs(up.urlsplit(href).query)
                if "id" in parsed:
                    internal.append((parsed["id"][0], anchor, ctx))
                    continue
            if href.startswith("http"):
                external.append((href, anchor, ctx))
        images.extend((normalize_media_src(src), alt, ctx)
                      for src, alt, ctx in html_conv.images)

    if not markdown.strip() and xhtml:
        html_conv = html_to_markdown(xhtml)
        markdown = html_conv.markdown()
        converter = CONVERTER_HTML
        extraction_method = "html"
        warnings.append("Wikitext 转换结果为空，改用 export_xhtml 转换")
        for href, anchor, ctx in html_conv.links:
            if href.startswith("/doku.php?id="):
                target = up.parse_qs(up.urlsplit(href).query).get("id", [""])[0]
                internal.append((target, anchor, ctx))
            elif href.startswith("http"):
                external.append((href, anchor, ctx))
        images.extend((normalize_media_src(src), alt, ctx)
                      for src, alt, ctx in html_conv.images)

    # 链接补全：xhtml 的 <a>／<img> 与 Wikitext 裸 URL
    if xhtml:
        html_conv = html_to_markdown(xhtml)
        for href, anchor, ctx in html_conv.links:
            if not href or href.startswith("#") or href.startswith("mailto:"):
                continue
            if href.startswith("/doku.php?id=") or "doku.php?id=" in href:
                parsed = up.parse_qs(up.urlsplit(href).query)
                if "id" in parsed:
                    internal.append((parsed["id"][0], anchor, ctx))
                    continue
            if href.startswith("http"):
                external.append((href, anchor, ctx))
            elif href.startswith("/"):
                external.append((BASE + href, anchor, ctx))
        images.extend((normalize_media_src(src), alt, ctx)
                      for src, alt, ctx in html_conv.images)
    for url, anchor, ctx in extract_wikitext_urls(wikitext):
        external.append((url, anchor, ctx))

    # 去重（保持首次出现的锚文本与上下文）
    internal = _dedupe_links(internal)
    external = _dedupe_links(external)
    images = _dedupe_links(images)

    blocks = parse_markdown_blocks(markdown)
    return {
        "markdown": markdown,
        "warnings": warnings,
        "converter": converter,
        "converter_version": converter_version,
        "extraction_method": extraction_method,
        "internal": internal,
        "external": external,
        "images": images,
        "blocks": blocks,
    }


def _dedupe_links(items: List[Tuple[str, str, str]]) -> List[Tuple[str, str, str]]:
    seen = set()
    out = []
    for target, anchor, ctx in items:
        key = target
        if key in seen:
            continue
        seen.add(key)
        out.append((target, anchor, ctx))
    return out


def fetch_external(http: HttpClient, url: str, fetch_mode_state: Dict[str, Any]):
    """抓取外链原始字节；返回（bytes, content_type, error, meta）。"""
    body, err, resp = http.get_bytes(url, "external")
    meta = {"status": None, "content_type": None, "etag": None, "last_modified": None,
            "wayback_timestamp": None, "original_status": None}
    if resp is not None:
        meta["status"] = resp.status_code
        meta["content_type"] = content_type_of(resp)
        meta["etag"] = resp.headers.get("ETag")
        meta["last_modified"] = resp.headers.get("Last-Modified")
    if body is None:
        return None, None, err or "request_failed", meta
    if resp is not None and resp.status_code >= 400:
        return None, meta["content_type"], f"http_{resp.status_code}", meta
    return body, meta["content_type"], None, meta


def wayback_lookup(http: HttpClient, canonical: str) -> Optional[Dict[str, str]]:
    api = WAYBACK_AVAILABLE + "?url=" + up.quote(canonical, safe="")
    body, err, _resp = http.get_bytes(api, "wayback_api")
    if body is None:
        return None
    try:
        data = json.loads(body.decode("utf-8", "replace"))
    except json.JSONDecodeError:
        return None
    snap = (data.get("archived_snapshots") or {}).get("closest") or {}
    if not snap.get("available") or not snap.get("url"):
        return None
    raw_url = snap["url"]
    timestamp = snap.get("timestamp", "")
    if "/web/" in raw_url and "/id_" not in raw_url:
        raw_url = raw_url.replace("/web/", "/web/id_", 1)
    return {"url": raw_url, "timestamp": timestamp, "status": str(snap.get("status", ""))}


# =============================================================================
# 单页入库
# =============================================================================

def record_page(conn, seq: IdSeq, row: Dict[str, Any], refresh_blocks: bool
                ) -> Tuple[int, bool]:
    existing = conn.execute(
        "SELECT id, sha256_markdown FROM pages WHERE page_key = ?",
        [row["page_key"]]).fetchone()
    changed = True
    if existing is not None:
        changed = existing[1] != row.get("sha256_markdown")
        if not changed and not refresh_blocks:
            return int(existing[0]), False
    page_id, created = upsert(conn, "pages", ["page_key"], row, seq=seq)
    if changed and existing is not None:
        conn.execute(
            "INSERT INTO update_log (id, page_key, operation, field_changed, old_value, "
            "new_value, timestamp, operated_by, notes) VALUES (?,?,?,?,?,?,?,?,?)",
            [seq.next("update_log"), row["page_key"], "update", "sha256_markdown",
             existing[1], row.get("sha256_markdown"), now_iso(),
             "tuhs_wiki_crawl.py", "内容变化触发重抓"])
    return page_id, created


def write_fulltext(conn, seq: IdSeq, page_key: str, content: str, method: str,
                   markers: str = None, notes: str = None) -> None:
    upsert(conn, "fulltext", ["page_key"], {
        "page_key": page_key,
        "content": content,
        "char_count": len(content),
        "extraction_method": method,
        "extracted_at": now_iso(),
        "page_markers": markers,
        "extraction_notes": notes,
        "encoding": "utf-8",
        "line_ending": "lf",
    }, seq=seq)


def write_blocks(conn, seq: IdSeq, page_key: str, blocks: List[Dict[str, Any]]) -> int:
    conn.execute("DELETE FROM fulltext_blocks WHERE page_key = ?", [page_key])
    for index, block in enumerate(blocks):
        upsert(conn, "fulltext_blocks", ["id"], {
            "id": seq.next("fulltext_blocks"),
            "page_key": page_key,
            "block_index": index,
            "block_type": block["block_type"],
            "block_level": block["block_level"],
            "heading_path": block["heading_path"],
            "block_content": block["block_content"],
            "block_page": block.get("block_page"),
            "char_offset_start": block["start"],
            "char_offset_end": block["end"],
        })
    return len(blocks)


def write_conversion(conn, seq: IdSeq, page_key: str, converter: str,
                     source_kind: str, source_sha: str, md_sha: Optional[str],
                     warnings: List[str]) -> None:
    upsert(conn, "conversions", ["page_key", "converter"], {
        "page_key": page_key,
        "converter": converter,
        "converter_version": CONVERTER_VERSION,
        "source_kind": source_kind,
        "source_sha256": source_sha,
        "md_sha256": md_sha,
        "converted_at": now_iso(),
        "warnings": json.dumps(warnings, ensure_ascii=False) if warnings else None,
    }, seq=seq)


def write_links(conn, seq: IdSeq, source_key: str, classified: List[Dict[str, Any]]) -> int:
    """按 (source_page_key, target_url, target_kind) 幂等写入。"""
    for item in classified:
        upsert(conn, "links", ["source_page_key", "target_url", "target_kind"], {
            "source_page_key": source_key,
            "target_kind": item["kind"],
            "target_url": item["canonical"],
            "target_page_key": item["target_page_key"],
            "anchor_text": (item.get("anchor") or "")[:500] or None,
            "link_context": (item.get("context") or "")[:500] or None,
            "depth": 1,
            "resolution_status": item["resolution_status"],
            "discovered_at": now_iso(),
        }, seq=seq)
    return len(classified)


def write_excluded(conn, seq: IdSeq, item: Dict[str, Any]) -> None:
    upsert(conn, "excluded_items", ["url", "item_kind"], {
        "url": item["canonical"],
        "item_kind": item["exclude_kind"],
        "reason": item["reason"],
        "evidence_page_key": item.get("evidence_page_key"),
        "evidence_text": (item.get("evidence_text") or "")[:500] or None,
        "http_content_type": item.get("content_type"),
        "content_length": item.get("content_length"),
        "review_flag": int(item.get("review_flag") or 0),
        "recorded_at": now_iso(),
    }, seq=seq)


# =============================================================================
# 主流程
# =============================================================================

def run_crawl(args) -> int:
    db_path = Path(args.db).resolve()
    root = Path(args.root).resolve()
    if not db_path.exists():
        print(f"ERROR: 库不存在：{db_path}", file=sys.stderr)
        return 2
    run_id = args.run_id or ("tuhs-" + datetime.now().strftime("%Y%m%dT%H%M%S"))
    root.mkdir(parents=True, exist_ok=True)
    print(f"[run] run_id={run_id} db={db_path} root={root}")

    log = CrawlLog(run_id)
    http = HttpClient(log)
    assignment, scope = discover_pages(http)
    print(f"[discover] 页面基线={scope['baseline']} 命名空间计数={scope['namespace_counts']}")
    if scope["index_errors"]:
        print(f"[discover] 索引错误 {len(scope['index_errors'])} 条：{scope['index_errors']}")

    known_pages = set(assignment)
    ordered_pages = sorted(assignment)
    if args.limit:
        ordered_pages = ordered_pages[: args.limit]
        print(f"[limit] 仅处理前 {len(ordered_pages)} 页")

    if args.dry_run:
        print(f"[dry-run] 不写盘、不抓页面。scope_sha256={scope['page_set_sha256']}")
        print(f"[dry-run] 命名空间分布 {json.dumps(scope['namespace_counts'], ensure_ascii=False)}")
        print(f"[dry-run] HTTP 统计 {http.stats}")
        return 0

    conn = open_database(db_path)
    seq = IdSeq(conn)
    log.flusher = conn
    counts = {"wiki_pages": 0, "skipped": 0, "failed": 0, "external_pages": 0,
              "external_skipped": 0, "excluded": 0, "links": 0, "blocks": 0}
    skip_external = args.wiki_only or args.no_external
    head_check = not args.wiki_only
    classifier = UrlClassifier(known_pages, http, head_check=head_check)

    # 先落 running 行：即使后续异常退出，验证器仍可取到本轮基线
    upsert(conn, "crawl_runs", ["run_id"], {
        "run_id": run_id,
        "started_at": scope.get("derived_at") or now_iso(),
        "finished_at": None,
        "scope_json": json.dumps(scope, ensure_ascii=False),
        "page_baseline": scope["baseline"],
        "page_fetched": 0,
        "external_fetched": 0,
        "excluded": 0,
        "failed": 0,
        "status": "running",
        "tool_version": CONVERTER_VERSION,
    }, id_col=None)

    try:
        # 既有状态（续跑判定）
        existing_pages: Dict[str, Tuple[str, Optional[str]]] = {}
        for key, status, md_path in conn.execute(
                "SELECT page_key, status, md_path FROM pages").fetchall():
            existing_pages[key] = (status, md_path)

        for page_id in ordered_pages:
            namespace = assignment[page_id]
            wt_rel, md_rel = wiki_rel_paths(page_id, namespace)
            md_abs = root / md_rel
            wt_abs = root / wt_rel
            if not args.refresh and page_id in existing_pages:
                status, stored_md = existing_pages[page_id]
                target_md = (root / stored_md) if stored_md else md_abs
                if status == "active" and target_md.exists():
                    counts["skipped"] += 1
                    continue

            fetched = fetch_wiki_page(http, page_id)
            raw_bytes = fetched.get("raw_bytes") or b""
            source_sha = sha256_hex(raw_bytes) if raw_bytes else None
            notes = list(fetched.get("notes") or [])

            if fetched["status"] != "active":
                counts["failed"] += 1
                print(f"[fail] {page_id}: {fetched['error_type']} {fetched['error_detail']}")
                record_page(conn, seq, {
                    "page_key": page_id,
                    "source_kind": "wiki",
                    "namespace": namespace,
                    "title": page_id.split(":")[-1],
                    "url": fetched["raw_url"],
                    "canonical_url": doku_page_url(page_id),
                    "depth": 0,
                    "referrer_page_key": None,
                    "referrer_url": None,
                    "anchor_text": None,
                    "http_status": fetched["http_status"],
                    "content_type": fetched["content_type"],
                    "fetched_at": now_iso(),
                    "fetch_mode": "live",
                    "etag": fetched["etag"],
                    "last_modified": fetched["last_modified"],
                    "wikitext_path": None,
                    "md_path": None,
                    "source_bytes": len(raw_bytes) if raw_bytes else None,
                    "sha256_source": source_sha,
                    "sha256_markdown": None,
                    "char_count": 0,
                    "extraction_method": "none",
                    "converter": CONVERTER_NONE,
                    "language": "en",
                    "wiki_last_modified": fetched["last_modified"],
                    "wiki_last_author": None,
                    "status": "failed",
                    "notes": (fetched["error_type"] or "") + "｜" +
                             (fetched["error_detail"] or ""),
                }, refresh_blocks=True)
                write_fulltext(conn, seq, page_id, "", "none",
                               notes=f"抓取失败：{fetched['error_type']}")
                write_conversion(conn, seq, page_id, CONVERTER_NONE, "wiki",
                                 source_sha or "", None,
                                 [f"抓取失败：{fetched['error_type']}"])
                continue

            wikitext = fetched["wikitext"] or ""
            converted = convert_page(page_id, fetched, known_pages)
            markdown = converted["markdown"]
            notes.extend(converted["warnings"])

            write_text_guard(wt_abs, wikitext)
            write_text_guard(md_abs, markdown)
            md_sha = sha256_hex(md_abs.read_bytes())
            changed = True
            if page_id in existing_pages and not args.refresh:
                previous = conn.execute(
                    "SELECT sha256_markdown FROM pages WHERE page_key = ?",
                    [page_id]).fetchone()
                if previous and previous[0] == md_sha:
                    changed = False

            title = title_from_wikitext(wikitext, page_id)
            record_page(conn, seq, {
                "page_key": page_id,
                "source_kind": "wiki",
                "namespace": namespace,
                "title": title,
                "url": doku_page_url(page_id),
                "canonical_url": doku_page_url(page_id),
                "depth": 0,
                "referrer_page_key": None,
                "referrer_url": None,
                "anchor_text": None,
                "http_status": fetched["http_status"],
                "content_type": fetched["content_type"],
                "fetched_at": now_iso(),
                "fetch_mode": "live",
                "etag": fetched["etag"],
                "last_modified": fetched["last_modified"],
                "wikitext_path": wt_rel,
                "md_path": md_rel,
                "source_bytes": len(raw_bytes),
                "sha256_source": source_sha,
                "sha256_markdown": md_sha,
                "char_count": len(markdown),
                "extraction_method": converted["extraction_method"],
                "converter": converted["converter"],
                "language": "en",
                "wiki_last_modified": fetched["last_modified"],
                "wiki_last_author": None,
                "status": "active",
                "notes": ("；".join(n for n in notes if n) or None),
            }, refresh_blocks=False)

            write_fulltext(conn, seq, page_id, markdown, converted["extraction_method"],
                           notes=("；".join(converted["warnings"]) or None))
            if changed:
                counts["blocks"] += write_blocks(conn, seq, page_id, converted["blocks"])
            else:
                existing_blocks = conn.execute(
                    "SELECT COUNT(*) FROM fulltext_blocks WHERE page_key = ?",
                    [page_id]).fetchone()[0]
                if existing_blocks == 0:
                    counts["blocks"] += write_blocks(conn, seq, page_id, converted["blocks"])
            write_conversion(conn, seq, page_id, converted["converter"], "wiki",
                             source_sha or "", md_sha, converted["warnings"])
            counts["wiki_pages"] += 1

            # 链接分类
            classified: List[Dict[str, Any]] = []
            for target, anchor, ctx in converted["internal"]:
                item = classifier.classify(doku_page_url(target),
                                           anchor, page_id, fetched["xhtml_url"])
                item["anchor"] = anchor
                item["context"] = ctx
                if item["kind"] == "internal" and item["target_page_key"] not in known_pages:
                    item["resolution_status"] = "broken_internal"
                classified.append(item)
            for target, anchor, ctx in converted["external"]:
                item = classifier.classify(target, anchor, page_id, fetched["xhtml_url"])
                item["anchor"] = anchor
                item["context"] = ctx
                classified.append(item)
            for target, alt, ctx in converted["images"]:
                item = classifier.classify(target, alt, page_id, fetched["xhtml_url"])
                item["anchor"] = alt
                item["context"] = ctx
                if item["kind"] not in ("media", "non_content"):
                    item["kind"] = "media"
                    item["resolution_status"] = "registered"
                    item["reason"] = "页面图片引用，仅登记不下载"
                classified.append(item)

            # 排除台账
            excluded_seen = set()
            for item in classified:
                if item["exclude_kind"]:
                    key = (item["canonical"], item["exclude_kind"])
                    if key in excluded_seen:
                        continue
                    excluded_seen.add(key)
                    write_excluded(conn, seq, {
                        **item,
                        "evidence_page_key": page_id,
                        "evidence_text": f"{item.get('anchor') or ''}｜{item.get('context') or ''}",
                    })
                    counts["excluded"] += 1

            conn.execute("DELETE FROM links WHERE source_page_key = ?", [page_id])
            counts["links"] += write_links(conn, seq, page_id, classified)
            print(f"[page] {page_id} md={len(markdown)}字 块={len(converted['blocks'])} "
                  f"链接={len(classified)} 警告={len(converted['warnings'])}")

        # 外链一跳
        if not skip_external:
            external_queue: Dict[str, Dict[str, Any]] = {}
            for url, referrer_key, anchor, context in conn.execute(
                    "SELECT target_url, source_page_key, anchor_text, link_context "
                    "FROM links WHERE target_kind = 'external' ORDER BY id").fetchall():
                if url not in external_queue:
                    external_queue[url] = {"referrer": referrer_key,
                                           "anchor": anchor, "context": context}
            print(f"[external] 队列 {len(external_queue)} 个归一 URL")
            for url, meta in external_queue.items():
                try:
                    counts_sub = crawl_external(conn, seq, log, http, url, meta,
                                                root, classifier)
                except Exception as exc:  # noqa: BLE001
                    # 单个外链（含超大 PDF／OCR）异常不得终止整批
                    counts_sub = {"pages": 0, "skipped": 0, "excluded": 0, "failed": 1}
                    log.add(url, "external", 0, None, None, "exception",
                            repr(exc)[:800], now_iso(), now_iso(), 0)
                    conn.execute(
                        "UPDATE links SET resolution_status = 'failed' "
                        "WHERE target_url = ? AND target_kind = 'external'", [url])
                    print(f"[fail] {url}: exception {exc}")
                counts["external_pages"] += counts_sub["pages"]
                counts["external_skipped"] += counts_sub["skipped"]
                counts["excluded"] += counts_sub["excluded"]
                counts["failed"] += counts_sub["failed"]
    finally:
        log.flush(conn)
        shutil.rmtree(TMP_WORKDIR, ignore_errors=True)

    finished = now_iso()
    status = "completed"
    if counts["failed"]:
        status = "completed_with_failures"
    upsert(conn, "crawl_runs", ["run_id"], {
        "run_id": run_id,
        "started_at": scope.get("derived_at") or now_iso(),
        "finished_at": finished,
        "scope_json": json.dumps(scope, ensure_ascii=False),
        "page_baseline": scope["baseline"],
        "page_fetched": counts["wiki_pages"],
        "external_fetched": counts["external_pages"],
        "excluded": counts["excluded"],
        "failed": counts["failed"],
        "status": status,
        "tool_version": CONVERTER_VERSION,
    }, id_col=None)
    conn.close()

    print(f"[done] wiki 成功={counts['wiki_pages']} 跳过={counts['skipped']} "
          f"失败={counts['failed']}")
    print(f"[done] 外链成功={counts['external_pages']} 跳过登记={counts['external_skipped']} "
          f"排除={counts['excluded']} 链接行={counts['links']} 块={counts['blocks']}")
    print(f"[done] HTTP 统计 {http.stats}")
    return 0


def crawl_external(conn, seq: IdSeq, log: CrawlLog, http: HttpClient, url: str,
                   meta: Dict[str, Any], root: Path,
                   classifier: UrlClassifier) -> Dict[str, int]:
    stats = {"pages": 0, "skipped": 0, "excluded": 0, "failed": 0}
    page_key = external_page_key(url)
    host = up.urlsplit(url).netloc.lower()
    if not host:
        stats["skipped"] += 1
        return stats
    md_rel = external_rel_path(url)
    md_abs = root / md_rel
    existing = conn.execute(
        "SELECT status, md_path, char_count FROM pages WHERE page_key = ?", [page_key]).fetchone()
    if existing and existing[0] == "active" and (root / (existing[1] or md_rel)).exists() \
            and (existing[2] or 0) > 0:
        stats["skipped"] += 1
        return stats

    body, ctype, err, resp_meta = fetch_external(http, url, {})
    fetch_mode = "live"
    wayback_timestamp = None
    original_status = resp_meta.get("status")
    alt = alternate_url(url)
    alt_used = False
    if body is None and alt:
        body2, ctype2, err2, meta2 = fetch_external(http, alt, {})
        if body2 is not None:
            body, ctype, err, resp_meta = body2, ctype2, err2, meta2
            fetch_mode = "alternate"
            alt_used = True
            if meta2.get("status"):
                original_status = meta2["status"]
    if body is None:
        snap = wayback_lookup(http, url)
        if snap:
            body, ctype, err, snap_meta = fetch_external(http, snap["url"], {})
            if body is not None:
                fetch_mode = "wayback"
                wayback_timestamp = snap["timestamp"]
                if snap_meta.get("status"):
                    original_status = snap_meta["status"]
    if body is None:
        stats["failed"] += 1
        record_external_failed(conn, seq, page_key, url, meta, original_status, err,
                              ctype, fetch_mode)
        return stats

    source_sha = sha256_hex(body)
    source_bytes = len(body)
    ctype = (ctype or "").lower()
    extraction_method = "html"
    converter = CONVERTER_HTML
    warnings: List[str] = []
    title = ""
    markdown = ""

    try:
        if "application/pdf" in ctype or body[:5] == b"%PDF-":
            markdown, method, warnings = convert_external_pdf(http, url, body, source_bytes)
            extraction_method = method
            converter = CONVERTER_PDF if method == "pdf-text" else CONVERTER_OCR
            if method == "needs_ocr_deferred":
                converter = CONVERTER_NONE
        elif "text/html" in ctype or body[:200].lstrip().lower().startswith(b"<!doctype html") \
                or body[:200].lstrip().lower().startswith(b"<html"):
            html_text = body.decode("utf-8", "replace")
            conv = html_to_markdown(html_text)
            markdown = conv.markdown()
            title = conv.title
            warnings.extend(conv.warnings)
        elif "text/plain" in ctype or "text/markdown" in ctype:
            text = body.decode("utf-8", "replace")
            markdown = normalize_newlines(text).strip() + "\n"
            extraction_method = "text"
            converter = "text-passthrough"
        else:
            stats["excluded"] += 1
            write_excluded(conn, seq, {
                "canonical": url,
                "exclude_kind": "binary_media" if ctype else "out_of_scope",
                "reason": f"外链内容类型 {ctype or '未知'}，非 Markdown 可承载类型，未下载文本",
                "content_type": ctype,
                "content_length": source_bytes,
                "review_flag": 1,
                "evidence_page_key": meta.get("referrer"),
                "evidence_text": f"{meta.get('anchor') or ''}｜{meta.get('context') or ''}",
            })
            conn.execute("UPDATE links SET resolution_status = 'excluded' "
                         "WHERE target_url = ? AND target_kind = 'external'", [url])
            return stats
    except CrawlError as exc:
        stats["failed"] += 1
        record_external_failed(conn, seq, page_key, url, meta, original_status,
                              f"convert_error: {exc}", ctype, fetch_mode)
        return stats

    # 正文为空的 HTML／文本页（反爬空壳、JS 页面、错误页）先试替代端点，再试 Wayback 快照
    if not markdown.strip() and extraction_method != "needs_ocr_deferred" and alt and not alt_used:
        body2, ctype2, _err2, meta2 = fetch_external(http, alt, {})
        if body2 is not None:
            conv = html_to_markdown(body2.decode("utf-8", "replace"))
            md2 = conv.markdown()
            if md2.strip():
                body, ctype = body2, ctype2
                source_sha = sha256_hex(body)
                source_bytes = len(body)
                markdown = md2
                title = title or conv.title
                warnings.append(f"原站空壳，改用替代端点 {alt}")
                warnings.extend(conv.warnings)
                extraction_method = "html"
                converter = CONVERTER_HTML
                fetch_mode = "alternate"
                alt_used = True
                if meta2.get("status"):
                    original_status = original_status or meta2["status"]

    if not markdown.strip() and extraction_method != "needs_ocr_deferred":
        snap = wayback_lookup(http, url)
        if snap:
            body2, ctype2, _err2, meta2 = fetch_external(http, snap["url"], {})
            if body2 is not None:
                ctype2 = (ctype2 or "").lower()
                try:
                    if "application/pdf" in ctype2 or body2[:5] == b"%PDF-":
                        markdown, method, warnings = convert_external_pdf(
                            http, url, body2, len(body2))
                        extraction_method = method
                        converter = CONVERTER_PDF if method == "pdf-text" else CONVERTER_OCR
                    elif "text/html" in ctype2 or body2[:200].lstrip().lower().startswith(b"<!doctype html"):
                        conv = html_to_markdown(body2.decode("utf-8", "replace"))
                        markdown = conv.markdown()
                        title = title or conv.title
                        warnings.extend(conv.warnings)
                        extraction_method = "html"
                        converter = CONVERTER_HTML
                    elif "text/plain" in ctype2 or "text/markdown" in ctype2:
                        markdown = normalize_newlines(
                            body2.decode("utf-8", "replace")).strip() + "\n"
                        extraction_method = "text"
                        converter = "text-passthrough"
                except Exception as exc:  # noqa: BLE001
                    warnings.append(f"Wayback 快照转换失败：{exc}")
                if markdown.strip():
                    body = body2
                    ctype = ctype2
                    source_sha = sha256_hex(body)
                    source_bytes = len(body)
                    fetch_mode = "wayback"
                    wayback_timestamp = snap.get("timestamp")
                    original_status = original_status or meta2.get("status")

    if not markdown.strip() and extraction_method != "needs_ocr_deferred":
        stats["failed"] += 1
        record_external_failed(conn, seq, page_key, url, meta, original_status,
                              "empty_content_after_wayback", ctype, fetch_mode)
        return stats

    if not title:
        title = url.rsplit("/", 1)[-1] or host
    write_text_guard(md_abs, markdown)
    md_sha = sha256_hex(md_abs.read_bytes())
    status = "needs_ocr_deferred" if extraction_method == "needs_ocr_deferred" else "active"
    record_page(conn, seq, {
        "page_key": page_key,
        "source_kind": "external",
        "namespace": EXTERNAL_NAMESPACE,
        "title": title[:300],
        "url": url,
        "canonical_url": url,
        "depth": 1,
        "referrer_page_key": meta.get("referrer"),
        "referrer_url": None,
        "anchor_text": meta.get("anchor"),
        "http_status": original_status,
        "content_type": ctype or None,
        "fetched_at": now_iso(),
        "fetch_mode": fetch_mode,
        "etag": resp_meta.get("etag"),
        "last_modified": resp_meta.get("last_modified"),
        "wikitext_path": None,
        "md_path": md_rel,
        "source_bytes": source_bytes,
        "sha256_source": source_sha,
        "sha256_markdown": md_sha if status == "active" else None,
        "char_count": len(markdown),
        "extraction_method": extraction_method,
        "converter": converter,
        "language": "en",
        "wiki_last_modified": None,
        "wiki_last_author": None,
        "status": status,
        "notes": (f"wayback={wayback_timestamp}；原站状态={original_status}；" +
                  "；".join(warnings))[:1500] or None,
    }, refresh_blocks=False)
    write_fulltext(conn, seq, page_key, markdown if status == "active" else "",
                   extraction_method, notes=("；".join(warnings) or None))
    blocks = parse_markdown_blocks(markdown) if status == "active" else []
    write_blocks(conn, seq, page_key, blocks)
    write_conversion(conn, seq, page_key, converter, "external", source_sha,
                     md_sha if status == "active" else None, warnings)
    conn.execute("UPDATE links SET resolution_status = ? WHERE target_url = ? "
                 "AND target_kind = 'external'",
                 ["needs_ocr_deferred" if status == "needs_ocr_deferred" else "fetched", url])
    stats["pages"] += 1
    print(f"[external] {url} {ctype} {source_bytes}B -> {len(markdown)}字 ({extraction_method})")
    return stats


def record_external_failed(conn, seq: IdSeq, page_key: str, url: str, meta: Dict[str, Any],
                           http_status, err: Optional[str], ctype: Optional[str],
                           fetch_mode: str) -> None:
    conn.execute("UPDATE links SET resolution_status = 'failed' WHERE target_url = ? "
                 "AND target_kind = 'external'", [url])
    record_page(conn, seq, {
        "page_key": page_key,
        "source_kind": "external",
        "namespace": EXTERNAL_NAMESPACE,
        "title": url.rsplit("/", 1)[-1][:300] or url,
        "url": url,
        "canonical_url": url,
        "depth": 1,
        "referrer_page_key": meta.get("referrer"),
        "referrer_url": None,
        "anchor_text": meta.get("anchor"),
        "http_status": http_status,
        "content_type": ctype,
        "fetched_at": now_iso(),
        "fetch_mode": fetch_mode,
        "etag": None,
        "last_modified": None,
        "wikitext_path": None,
        "md_path": None,
        "source_bytes": None,
        "sha256_source": None,
        "sha256_markdown": None,
        "char_count": 0,
        "extraction_method": "none",
        "converter": CONVERTER_NONE,
        "language": "en",
        "wiki_last_modified": None,
        "wiki_last_author": None,
        "status": "failed",
        "notes": f"抓取失败：{err}",
    }, refresh_blocks=True)
    write_fulltext(conn, seq, page_key, "", "none", notes=f"抓取失败：{err}")
    write_conversion(conn, seq, page_key, CONVERTER_NONE, "external", "", None,
                     [f"抓取失败：{err}"])
    print(f"[external-fail] {url}: {err}")


def convert_external_pdf(http: HttpClient, url: str, body: bytes,
                         size_bytes: int) -> Tuple[str, str, List[str]]:
    """PDF 落临时目录 → 文本层／OCR → Markdown → 立即删除。"""
    TMP_WORKDIR.mkdir(parents=True, exist_ok=True)
    workdir = Path(tempfile.mkdtemp(prefix="pdf_", dir=str(TMP_WORKDIR)))
    pdf_path = workdir / "source.pdf"
    try:
        pdf_path.write_bytes(body)
        guard_path = pdf_path
        markdown, method, warnings = pdf_to_markdown(guard_path, size_bytes)
        if not markdown.strip() and method != "needs_ocr_deferred":
            warnings.append("PDF 文本层为空")
        return markdown, method, warnings
    finally:
        shutil.rmtree(workdir, ignore_errors=True)


# =============================================================================
# 自检（离线）
# =============================================================================

WIKITEXT_FIXTURE = """====== Main Title ======

Intro paragraph with **bold**, //italic//, ''mono'' and a [[:people:dennis_ritchie|Dennis]] link, external [[https://example.org/page|Example]] and bare https://example.org/bare.

===== Section A =====

  * first item
  * second item
    * nested item

  - dash item
  - another

1. ordered one
2. ordered two

<code python>
print("hello")
</code>

^ Head 1 ^ Head 2 ^
| cell 1 | cell 2 |
| cell 3 | cell 4 |

{{:images:photo.jpg?direct&400|A photo}}

Text with line break\\\\
next line

~~REFNOTES~~

<nowiki>**not bold**</nowiki>

    indented preformatted
    second line

[(:biblio:prog:KnuthLCE1985Knuth, Jan 1985.)]
"""

HTML_FIXTURE = """<!DOCTYPE html><html><head><title>Fixture Title</title>
<style>.x{color:red}</style><script>var a=1;</script></head>
<body><header><h1>Header junk</h1></header><nav><a href="/nav">Nav</a></nav>
<main><h1>Main Heading</h1><p>Paragraph with <strong>bold</strong> and
<em>italic</em> and a <a href="https://example.org/x">link</a>.<br>Second line.</p>
<h2>Sub Heading</h2><ul><li>Item one</li><li>Item two<ul><li>Nested</li></ul></li></ul>
<ol><li>First</li><li>Second</li></ol>
<pre class="code">code line 1
code line 2</pre>
<table><tr><th>H1</th><th>H2</th></tr><tr><td>c1</td><td>c2</td></tr></table>
<img src="https://example.org/pic.png" alt="Pic">
<blockquote>Quoted text</blockquote>
<form><input name="q"></form></main>
<footer>Footer junk</footer><aside>Aside junk</aside></body></html>"""

MD_FIXTURE = """# Top

Paragraph one.

## Child

- item a
- item b

```text
code line
```

| Head | Value |
| --- | --- |
| a | 1 |

> quoted

[[page=2]]

![alt](https://example.org/img.png)
"""


def selftest() -> int:
    failures: List[str] = []
    checks = 0

    def check(label: str, condition: bool, detail: str = "") -> None:
        nonlocal checks
        checks += 1
        if condition:
            print(f"  PASS {label}")
        else:
            print(f"  FAIL {label} {detail}")
            failures.append(label)

    print("[selftest] Wikitext → Markdown")
    conv = WikiTextToMarkdown("people:tester", {"people:dennis_ritchie"}).convert(
        WIKITEXT_FIXTURE)
    md = conv.markdown
    check("h1", "# Main Title" in md)
    check("h2", "## Section A" in md)
    check("bold", "**bold**" in md)
    check("italic", "*italic*" in md)
    check("mono", "`mono`" in md)
    check("internal link", "[Dennis](https://wiki.tuhs.org/doku.php?id=people:dennis_ritchie)" in md)
    check("external link", "[Example](https://example.org/page)" in md)
    check("bare url", "<https://example.org/bare>" in md)
    check("list item", "- first item" in md)
    check("nested list", "  - nested item" in md)
    check("ordered list", "- ordered one" in md and "- ordered two" in md)
    check("code fence", "```python" in md and 'print("hello")' in md)
    check("table header", "| Head 1 | Head 2 |" in md)
    check("table separator", "| --- | --- |" in md)
    check("table row", "| cell 1 | cell 2 |" in md)
    check("image", "![A photo](https://wiki.tuhs.org/lib/exe/fetch.php?media=images:photo.jpg)" in md)
    check("hard break", "Text with line break  \nnext line" in md)
    check("nowiki", "**not bold**" in md)
    check("preformatted", "indented preformatted" in md)
    check("warnings non-empty", len(conv.warnings) > 0, f"warnings={conv.warnings}")
    check("macro warning", any("REFNOTES" in w for w in conv.warnings), "")
    check("biblio warning", any("biblio" in w for w in conv.warnings), "")
    check("heading count", conv.heading_count == 2, str(conv.heading_count))
    check("link collected", any(t == "people:dennis_ritchie" for t, _, _ in conv.internal_links))

    print("[selftest] HTML → Markdown")
    hp = html_to_markdown(HTML_FIXTURE)
    hmd = hp.markdown()
    check("title", hp.title == "Fixture Title", hp.title)
    check("h1", "# Main Heading" in hmd)
    check("h2", "## Sub Heading" in hmd)
    check("paragraph", "Paragraph with **bold** and *italic*" in hmd)
    check("link", "[link](https://example.org/x)" in hmd)
    check("br", "Second line." in hmd)
    check("ul item", "- Item one" in hmd)
    check("nested ul", "  - Nested" in hmd)
    check("ol item", "1. First" in hmd)
    check("code", "code line 1" in hmd and "```" in hmd)
    check("table header", "| H1 | H2 |" in hmd)
    check("table cell", "| c1 | c2 |" in hmd)
    check("image", "![Pic](https://example.org/pic.png)" in hmd)
    check("quote", hmd.count(">") >= 0 and "Quoted text" in hmd)
    check("skip script", "var a=1" not in hmd)
    check("skip style", "color:red" not in hmd)
    check("skip nav", "Nav" not in hmd)
    check("skip header/footer", "Header junk" not in hmd and "Footer junk" not in hmd)
    check("skip aside/form", "Aside junk" not in hmd)

    print("[selftest] 链接分类")
    clf = UrlClassifier({"people:dennis_ritchie", "start"}, http=None, head_check=False)
    cases = [
        ("https://wiki.tuhs.org/doku.php?id=people:dennis_ritchie", "internal", None),
        ("https://wiki.tuhs.org/doku.php?id=people:nobody", "internal", "broken_internal"),
        ("https://example.org/paper.html", "external", None),
        ("https://wiki.tuhs.org/lib/exe/fetch.php?media=images:x.jpg", "media", None),
        ("https://example.org/book.epub", "excluded_book", "excluded"),
        ("http://www.tuhs.org/Archive/Documentation/Books/Life_with_Unix.pdf",
         "excluded_book", "excluded"),
        ("https://example.org/src.tar.gz", "excluded_source", "excluded"),
        ("http://www.tuhs.org/cgi-bin/utree.pl?file=32V", "excluded_source", "excluded"),
        ("https://raw.githubusercontent.com/a/b/c", "excluded_source", "excluded"),
        ("mailto:a@b.c", "non_content", "skipped"),
        ("javascript:void(0)", "non_content", "skipped"),
        ("https://wiki.tuhs.org/doku.php?id=start&do=login", "non_content", "skipped"),
        ("https://wiki.tuhs.org/feed.php", "non_content", "skipped"),
        ("https://example.org/pic.png", "media", None),
        ("#section", "non_content", "skipped"),
    ]
    for raw, want_kind, want_status in cases:
        item = clf.classify(raw, "", "start", DOKU + "?id=start")
        ok = item["kind"] == want_kind
        if want_status:
            ok = ok and item["resolution_status"] == want_status
        check(f"classify {raw} -> {want_kind}", ok,
              f"got {item['kind']}/{item['resolution_status']}")

    print("[selftest] 二进制守卫")
    for magic in (b"%PDF-1.7", b"PK\x03\x04", b"\x89PNG\r\n", b"GIF89a", b"\xff\xd8\xff\xe0"):
        try:
            guard_magic(magic, "fixture")
            check(f"guard blocks {magic[:4]!r}", False)
        except CrawlError:
            check(f"guard blocks {magic[:4]!r}", True)
    try:
        guard_magic(b"# heading\n", "ok")
        check("guard allows text", True)
    except CrawlError:
        check("guard allows text", False)
    tmp_dir = TMP_WORKDIR
    tmp_dir.mkdir(parents=True, exist_ok=True)
    bad_path = tmp_dir / "guard_test.html"
    try:
        write_text_guard(bad_path, "<html></html>")
        check("ext guard blocks .html", False)
    except CrawlError:
        check("ext guard blocks .html", True)
    finally:
        if bad_path.exists():
            bad_path.unlink()
    good_path = tmp_dir / "guard_test.md"
    try:
        n = write_text_guard(good_path, "# 标题\r\n正文 \ufeff。\r\n")
        data = good_path.read_bytes()
        check("write guard LF/no BOM", b"\r" not in data and not data.startswith(b"\xef\xbb\xbf"))
        check("write guard bytes", n == len(data))
    finally:
        if good_path.exists():
            good_path.unlink()

    print("[selftest] 块解析")
    blocks = parse_markdown_blocks(MD_FIXTURE)
    types = [b["block_type"] for b in blocks]
    check("block heading", types.count("heading") == 2, str(types))
    check("block paragraph", types.count("paragraph") == 1, str(types))
    check("block list", types.count("list_item") == 2, str(types))
    check("block code", types.count("code_block") == 1, str(types))
    check("block table", types.count("table_row") == 2, str(types))
    check("block quote", types.count("quote") == 1, str(types))
    check("block page break", types.count("page_break") == 1, str(types))
    check("block image", types.count("image_placeholder") == 1, str(types))
    child = next(b for b in blocks if b["block_type"] == "heading" and b["block_content"] == "Child")
    check("heading_path", child["heading_path"] == "Top > Child", child["heading_path"])
    check("page marker", next(b for b in blocks if b["block_type"] == "page_break")["block_page"] == 2)
    total_offsets = all(b["end"] >= b["start"] for b in blocks)
    check("block offsets", total_offsets)

    print("[selftest] PDF → Markdown")
    try:
        import fitz  # type: ignore
    except Exception as exc:  # noqa: BLE001
        print(f"  SKIP PDF 转换（pymupdf 不可用：{exc}）")
    else:
        TMP_WORKDIR.mkdir(parents=True, exist_ok=True)
        pdf_dir = Path(tempfile.mkdtemp(prefix="selftest_", dir=str(TMP_WORKDIR)))
        pdf_path = pdf_dir / "fixture.pdf"
        try:
            doc = fitz.open()
            page = doc.new_page()
            page.insert_text((72, 100), "Hello PDF page one", fontsize=14)
            doc.save(str(pdf_path))
            doc.close()
            pdf_md, method, warns = pdf_to_markdown(pdf_path, pdf_path.stat().st_size)
            check("pdf text", "Hello PDF page one" in pdf_md, pdf_md[:80])
            check("pdf page marker", "[[page=1]]" in pdf_md)
            check("pdf method", method == "pdf-text", method)
            check("pdf warnings list", isinstance(warns, list))
        finally:
            shutil.rmtree(pdf_dir, ignore_errors=True)

    print("[selftest] 页面集合口径工具")
    check("namespace longest prefix", namespace_of("publications:manuals:cb",
                                                   ["publications", "publications:manuals"])
          == "publications:manuals")
    check("namespace top", namespace_of("start", NAMESPACES) == "(top)")
    check("wiki path", wiki_rel_paths("people:dennis_ritchie", "people")[0]
          == "raw/wiki/people/dennis_ritchie.wikitext")
    check("external key", external_page_key("https://example.org/x").startswith("ext:"))
    check("external path", external_rel_path("https://example.org/a/b")
          .startswith("raw/external/example.org/"))
    check("sanitize", sanitize_component('a<b>c:d|e?f*g"h') == "a_b_c_d_e_f_g_h")
    check("canonicalize fragment", canonicalize_url("https://x.org/a#b") == "https://x.org/a")
    check("canonicalize punctuation", canonicalize_url("https://x.org/a.") == "https://x.org/a")

    # 清理临时工作目录（若空）
    try:
        TMP_WORKDIR.rmdir()
    except OSError:
        pass

    print(f"[selftest] 共 {checks} 项，失败 {len(failures)} 项")
    if failures:
        for name in failures:
            print(f"  - {name}")
        return 1
    return 0


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
    try:
        import requests  # noqa: F401
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: 缺少 requests（{exc}）", file=sys.stderr)
        return 2
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="TUHS Wiki 全量抓取、Markdown 归一与入库")
    parser.add_argument("--db", default=str(DEFAULT_DB), help="DuckDB 库路径")
    parser.add_argument("--root", default=str(DEFAULT_ROOT), help="语料根目录")
    parser.add_argument("--limit", type=int, default=0, help="只处理前 N 个 wiki 页")
    parser.add_argument("--resume", action="store_true", default=True,
                        help="增量续跑（默认）")
    parser.add_argument("--refresh", action="store_true", help="强制重抓已 active 页")
    parser.add_argument("--wiki-only", action="store_true", help="只抓 wiki 页")
    parser.add_argument("--no-external", action="store_true", help="不抓外链")
    parser.add_argument("--dry-run", action="store_true", help="只做清单与统计")
    parser.add_argument("--selftest", action="store_true", help="离线自检")
    parser.add_argument("--run-id", default=None, help="批次号")
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    rc = verify_runtime()
    if rc:
        return rc
    if args.selftest:
        return selftest()
    return run_crawl(args)


if __name__ == "__main__":
    sys.exit(main())
