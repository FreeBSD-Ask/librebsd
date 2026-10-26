# -*- coding: utf-8 -*-
"""TUHS Wiki 独立 SQL 复核器（verify_tuhs_wiki_sql.py）。

用途
====
对 `03-原始史料库/16-TUHS-Wiki史料/tuhs_wiki.duckdb` 做**第二轮交叉核验**：以独立 SQL 与
独立文件系统扫描复算 V1–V5、V10、V12，供与主验证器 `verify_tuhs_wiki.py` 的第一轮结果比对。
规格出处：`.trae/specs/crawl-tuhs-wiki-20261025/spec.md`（Requirement: 完整抓取验证（V1–V12）、
Requirement: 加强复核（三轮回核））。

独立性
======
- 不 import 主验证器，不复用其任何函数、常量或判据代码。
- 判据全部以本文件自行编写的 SQL 与本文件自行实现的文件系统扫描完成；哈希一律用
  `hashlib.sha256` 现算。
- V1 的页面清单派生由本文件独立实现 `?do=index` 协议（自写 urllib 客户端、自写解析正则），
  与抓取器同一协议但不同实现；`--offline` 时不重派生，只比对 `crawl_runs` 基线与 `pages`
  集合，并把“未重派生”以 INFO 披露。

复算项
======
| 编号 | 判据 |
| ---- | ---- |
| V1 | 页面清单守恒：派生集合 == `crawl_runs` 基线 == `pages` 中 `source_kind='wiki'` 且 `status='active'` 集合；逐命名空间计数一致 |
| V2 | 双形态落盘：每页 `.wikitext`／`.md` 存在、`.wikitext` 非空、`.md` 实测 SHA-256 == `sha256_markdown` |
| V3 | Markdown 覆盖：每页恰 1 条 `fulltext`、`char_count` == `length(content)`、非空页至少 1 块、剥围栏代码后无 HTML 标签残留 |
| V4 | 外链闭合：`links` 外链 URL 集合 ⊆ `pages` 外链行 ∪ `excluded_items` ∪ `crawl_log` 失败 URL ∪ `needs_ocr_deferred`，未覆盖差集为零 |
| V5 | 键与去重：`page_key` 重复、`(page_key, block_index)` 重复、外链归一 URL 重复、`(page_key, converter)` 重复均为 0 |
| V10 | 二进制禁入：语料目录内扩展名只允许 `.md`／`.wikitext`（库文件本身除外），文件头魔数命中为零 |
| V12 | 转换台账：每页有 `conversions` 行、`converter_version` 与 `schema_meta` 一致、`md_sha256` 与文件一致 |

用法
====
    C:/Python314/python.exe verify_tuhs_wiki_sql.py --selftest
    C:/Python314/python.exe verify_tuhs_wiki_sql.py --offline
    C:/Python314/python.exe verify_tuhs_wiki_sql.py              # 含 V1 联网重派生
    C:/Python314/python.exe verify_tuhs_wiki_sql.py --db <库> --root <语料目录> --round R2SQL

退出码
======
0 全部通过；1 任一判据 FAIL；2 库缺失、运行时／存储版本不符或架构不符。

写库说明
========
结果写入 `verification`（`check_id` 前缀 `SQL-`）；写前先删同 `round` 同前缀旧行，`id` 动态取
`max+1`。SKIP 项 `passed` 记为 NULL。

编码：UTF-8 无 BOM、LF；中文弯引号；临时件只落 `script/` 并在结束时清理。
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
import time
import urllib.parse as up
import urllib.request
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Set, Tuple

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

DUCKDB_REQUIRED = "2.0.0"
STORAGE_PREFIX = "v2."
BASE = "https://wiki.tuhs.org"
DOKU = BASE + "/doku.php"
INDEX_USER_AGENT = (
    "librebsd-tuhs-wiki-sqlverify/1.0 (+https://wiki.tuhs.org; "
    "independent SQL re-check for a BSD history project; contact: ykla)"
)
NAMESPACES = (
    "systems", "source", "features", "events", "people", "anecdotes", "images",
    "glossary", "publications", "misc", "wiki", "blog", "playground", "refnotes",
)
TOP_PAGES = ("start", "syste")
TOP_SENTINEL = "(top)"
EXTERNAL_SENTINEL = "(external)"

ALLOWED_TEXT_EXT = {".md", ".wikitext"}
TRANSIENT_SUFFIX = {".wal", ".tmp"}
MAGIC_SIGNATURES = (
    (b"%PDF-", "pdf"),
    (b"PK\x03\x04", "zip"),
    (b"\x89PNG", "png"),
    (b"GIF8", "gif"),
    (b"\xff\xd8\xff", "jpeg"),
)

REQUIRED_TABLES = {
    "pages", "fulltext", "fulltext_blocks", "links", "excluded_items", "conversions",
    "crawl_runs", "crawl_log", "verification", "schema_meta",
}

HTML_TAG_RE = re.compile(
    r"</?(?:html|head|body|script|style|div|span|table|thead|tbody|tfoot|tr|td|th|"
    r"ul|ol|li|p|a|img|h[1-6]|nav|header|footer|aside|form|input|button|textarea|select|"
    r"iframe|frame|frameset|meta|link|section|article|main|pre|code|blockquote|dl|dt|dd|figure|"
    r"figcaption|svg|noscript|template)(?=[\s/>])[^<>\n]{0,300}>",
    re.I,
)
FENCE_RE = re.compile(r"```[^\n]*\n.*?(?:```|\Z)", re.S)
INLINE_CODE_RE = re.compile(r"`+[^`\n]*?`+")

SCRIPT_DIR = Path(__file__).resolve().parent
# 本件位于 00-编纂规则与格式规范/01-规则/脚本与命令/，上溯 3 级为仓库根
PROJECT_ROOT = SCRIPT_DIR.parents[2]
DEFAULT_ROOT = PROJECT_ROOT / "03-原始史料库" / "16-TUHS-Wiki史料"
DEFAULT_DB = DEFAULT_ROOT / "tuhs_wiki.duckdb"
SCHEMA_SQL = SCRIPT_DIR / "tuhs_wiki_schema.sql"
SCRIPT_DIR_TMP = PROJECT_ROOT / "script"


# =============================================================================
# 基础工具
# =============================================================================

def now_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_page_set(page_ids: Iterable[str]) -> str:
    """页面集合排序后以 LF 连接取 SHA-256（与抓取器同一口径，独立实现）。"""
    return sha256_bytes("\n".join(sorted(page_ids)).encode("utf-8"))


def namespace_of(page_id: str, namespaces: Sequence[str]) -> str:
    """最长命名空间前缀；顶层页记 (top)。"""
    best = None
    for ns in namespaces:
        if page_id == ns or page_id.startswith(ns + ":"):
            if best is None or len(ns) > len(best):
                best = ns
    return best if best else TOP_SENTINEL


def fmt_items(items: Sequence[str], limit: int = 20) -> str:
    items = list(items)
    if not items:
        return "（无）"
    shown = "; ".join(items[:limit])
    if len(items) > limit:
        shown += f" …（共 {len(items)} 项）"
    return shown


def clip(text: str, limit: int = 3500) -> str:
    text = text or ""
    return text if len(text) <= limit else text[:limit] + "…（已截断）"


class CheckResult:
    """单条判据结论。"""

    def __init__(self, check_id: str, name: str, expected: str = "", actual: str = "",
                 passed: Optional[bool] = None, detail: str = "", skipped: bool = False):
        self.check_id = check_id
        self.name = name
        self.expected = expected
        self.actual = actual
        self.passed = passed
        self.detail = detail
        self.skipped = skipped

    def status(self) -> str:
        if self.skipped:
            return "INFO"
        return "PASS" if self.passed else "FAIL"


def fail(check_id: str, name: str, expected: str, actual: str, detail: str) -> CheckResult:
    return CheckResult(check_id, name, expected, actual, False, detail)


# =============================================================================
# 独立页面清单派生（V1 联网分支）
# =============================================================================

class IndexClient:
    """独立 urllib 客户端：同主机 ≥1.5 秒间隔、3 次退避重试、逐次计数。"""

    def __init__(self, timeout: int = 30, min_interval: float = 1.5,
                 retries: int = 3):
        self.timeout = timeout
        self.min_interval = min_interval
        self.retries = retries
        self._last_call = 0.0
        self.requests = 0

    def get_text(self, url: str) -> str:
        last_error: Optional[BaseException] = None
        for attempt in range(self.retries):
            wait = self.min_interval - (time.monotonic() - self._last_call)
            if wait > 0:
                time.sleep(wait)
            self._last_call = time.monotonic()
            try:
                request = urllib.request.Request(url, headers={"User-Agent": INDEX_USER_AGENT})
                with urllib.request.urlopen(request, timeout=self.timeout) as resp:
                    self.requests += 1
                    return resp.read().decode("utf-8", "replace")
            except Exception as exc:  # noqa: BLE001
                last_error = exc
                if attempt + 1 < self.retries:
                    time.sleep(2 ** (attempt + 1))
        raise RuntimeError(f"索引请求失败（{self.retries} 次）：{url}：{last_error}")


def parse_index_document(text: str) -> Tuple[Set[str], Set[str], Set[int]]:
    """从索引页 HTML 解析（页面 ID、子命名空间、分页偏移）。"""
    decoded = html_mod.unescape(text)
    page_ids = set()
    for raw in re.findall(r"doku\.php\?id=([^\"'<>\s&]+)", decoded):
        value = up.unquote(raw).strip()
        if value:
            page_ids.add(value)
    subs = set()
    for raw in re.findall(r"idx=([^\"'<>\s&]+)", decoded):
        value = up.unquote(raw).strip()
        if value and ":" in value:
            subs.add(value)
    offsets = {int(raw) for raw in re.findall(r"[?&]s=(\d+)", decoded)}
    return page_ids, subs, offsets


def derive_scope_online(timeout: int = 30) -> Dict[str, Any]:
    """递归派生 14 个命名空间＋顶层页，返回页面集合与基线摘要。"""
    client = IndexClient(timeout=timeout)
    queue: List[str] = list(NAMESPACES)
    visited_ns: List[str] = []
    pages: Set[str] = set()
    errors: List[str] = []

    while queue:
        ns = queue.pop(0)
        if ns in visited_ns:
            continue
        visited_ns.append(ns)
        todo_offsets: List[Optional[int]] = [None]
        fetched_offsets: Set[int] = set()
        while todo_offsets:
            offset = todo_offsets.pop(0)
            if offset is not None:
                if offset in fetched_offsets:
                    continue
                fetched_offsets.add(offset)
            url = DOKU + "?do=index&idx=" + up.quote(ns)
            if offset is not None:
                url += f"&s={offset}"
            try:
                text = client.get_text(url)
            except RuntimeError as exc:
                errors.append(f"{ns}{'@' + str(offset) if offset is not None else ''}: {exc}")
                todo_offsets = []
                break
            found_pages, found_subs, found_offsets = parse_index_document(text)
            pages |= found_pages
            for sub in sorted(found_subs):
                head = sub.split(":")[0]
                if head in NAMESPACES and sub not in visited_ns and sub not in queue:
                    queue.append(sub)
            for value in sorted(found_offsets):
                if value not in fetched_offsets and value not in todo_offsets:
                    todo_offsets.append(value)

    pages |= set(TOP_PAGES)
    known_namespaces = sorted(set(visited_ns) | set(NAMESPACES))
    counts: Counter = Counter(namespace_of(key, known_namespaces) for key in pages)
    ordered = sorted(pages)
    return {
        "pages": set(ordered),
        "baseline": len(ordered),
        "page_set_sha256": sha256_page_set(ordered),
        "namespace_counts": dict(sorted(counts.items())),
        "errors": errors,
        "http_requests": client.requests,
    }


def scope_from_page_set(page_ids: Iterable[str]) -> Dict[str, Any]:
    """由给定页面集合构造基线摘要（自检用，替代联网派生）。"""
    known_namespaces = sorted(NAMESPACES)
    pages = set(page_ids)
    counts: Counter = Counter(namespace_of(key, known_namespaces) for key in pages)
    ordered = sorted(pages)
    return {
        "pages": set(ordered),
        "baseline": len(ordered),
        "page_set_sha256": sha256_page_set(ordered),
        "namespace_counts": dict(sorted(counts.items())),
        "errors": [],
        "http_requests": 0,
    }


# =============================================================================
# 判据实现（V1–V5、V10、V12）
# =============================================================================

def check_v1(conn, derived: Optional[Dict[str, Any]],
             derive_error: Optional[str] = None) -> CheckResult:
    check_id, name = "SQL-V1", "页面清单守恒（独立复算）"
    row = conn.execute(
        "SELECT run_id, scope_json, page_baseline FROM crawl_runs "
        "ORDER BY started_at DESC NULLS LAST, run_id DESC LIMIT 1").fetchone()
    if row is None:
        return fail(check_id, name, "crawl_runs 至少 1 条批次基线",
                    "crawl_runs 0 行", "库内无抓取批次基线，无法核对页面清单")

    run_id, scope_json, run_baseline = row
    try:
        scope = json.loads(scope_json) if scope_json else {}
    except (TypeError, ValueError) as exc:
        return fail(check_id, name, "scope_json 可解析", "解析失败",
                    f"run_id={run_id} scope_json 解析失败：{exc}")

    baseline = scope.get("baseline")
    baseline_sha = scope.get("page_set_sha256")
    baseline_counts = scope.get("namespace_counts") or {}

    rows = conn.execute(
        "SELECT page_key, namespace FROM pages "
        "WHERE source_kind = 'wiki' AND status = 'active' ORDER BY page_key").fetchall()
    if not rows:
        return fail(check_id, name, "至少 1 个 wiki active 页", "0 页",
                    f"判据为空：pages 无 wiki active 行（run_id={run_id}）")

    page_keys = [r[0] for r in rows]
    actual_sha = sha256_page_set(page_keys)
    actual_counts = dict(sorted(Counter(r[1] for r in rows).items()))

    problems: List[str] = []
    if baseline != len(page_keys):
        problems.append(f"基线页数 {baseline} != 实测 {len(page_keys)}")
    if run_baseline is not None and run_baseline != baseline:
        problems.append(f"crawl_runs.page_baseline {run_baseline} != scope.baseline {baseline}")
    if baseline_sha != actual_sha:
        problems.append(f"集合 SHA-256 不一致：基线 {str(baseline_sha)[:16]}… / 实测 {actual_sha[:16]}…")
    if baseline_counts != actual_counts:
        diff = []
        for ns in sorted(set(baseline_counts) | set(actual_counts)):
            want, got = baseline_counts.get(ns, 0), actual_counts.get(ns, 0)
            if want != got:
                diff.append(f"{ns}: 基线 {want} / 实测 {got}")
        problems.append("逐命名空间计数不一致：" + fmt_items(diff))

    info_lines: List[str] = []
    if derive_error is not None:
        problems.append(f"重新派生失败：{derive_error}")
    elif derived is not None:
        derived_pages = derived["pages"]
        missing = sorted(derived_pages - set(page_keys))
        extra = sorted(set(page_keys) - derived_pages)
        if derived.get("errors"):
            problems.append("派生过程存在索引错误：" + fmt_items(derived["errors"], 10))
        if derived.get("baseline") != baseline:
            problems.append(f"派生页数 {derived.get('baseline')} != 基线 {baseline}")
        if derived.get("page_set_sha256") != baseline_sha:
            problems.append("派生集合 SHA-256 与基线不一致")
        if derived.get("namespace_counts") != baseline_counts:
            problems.append("派生逐命名空间计数与基线不一致")
        if missing:
            problems.append("派生有而 pages 缺失（漏抓）：" + fmt_items(missing))
        if extra:
            problems.append("pages 有而派生无（多余）：" + fmt_items(extra))
        info_lines.append(f"重新派生完成，请求 {derived.get('http_requests', 0)} 次")
    else:
        info_lines.append("未重派生（--offline）：仅比对 crawl_runs 基线与 pages 集合")

    expected = (f"基线 {baseline} 页，集合 SHA-256 {str(baseline_sha)[:16]}…，"
                f"逐命名空间计数与 pages 一致")
    actual = (f"{len(page_keys)} 页，SHA-256 {actual_sha[:16]}…，"
              f"命名空间 {len(actual_counts)} 个")
    detail_lines = [f"run_id={run_id}"] + info_lines + problems
    return CheckResult(check_id, name, expected, actual, not problems,
                       "\n".join(detail_lines))


def check_v2(conn, root: Path) -> CheckResult:
    check_id, name = "SQL-V2", "双形态落盘与 Markdown 哈希（独立复算）"
    rows = conn.execute(
        "SELECT page_key, wikitext_path, md_path, sha256_markdown FROM pages "
        "WHERE source_kind = 'wiki' AND status = 'active' ORDER BY page_key").fetchall()
    if not rows:
        return fail(check_id, name, "至少 1 个 wiki active 页", "0 页",
                    "判据为空：pages 无 wiki active 行")

    missing_path = []       # 记录缺失路径字段
    missing_wt = []         # .wikitext 不存在
    empty_wt = []           # .wikitext 为空
    missing_md = []         # .md 不存在
    bad_hash = []           # .md 哈希不符
    checked = 0
    for key, wikitext_path, md_path, recorded in rows:
        if not wikitext_path or not md_path:
            missing_path.append(key)
            continue
        wt_abs = root / wikitext_path
        md_abs = root / md_path
        if not wt_abs.exists():
            missing_wt.append(f"{key}（{wikitext_path}）")
        elif wt_abs.stat().st_size == 0:
            empty_wt.append(f"{key}（{wikitext_path}）")
        if not md_abs.exists():
            missing_md.append(f"{key}（{md_path}）")
            continue
        digest = sha256_file(md_abs)
        checked += 1
        if not recorded:
            bad_hash.append(f"{key}：sha256_markdown 为空，实测 {digest[:12]}…")
        elif digest != recorded:
            bad_hash.append(f"{key}：记录 {recorded[:12]}… / 实测 {digest[:12]}…")

    problems = []
    if missing_path:
        problems.append("路径字段缺失：" + fmt_items(missing_path))
    if missing_wt:
        problems.append(".wikitext 缺失：" + fmt_items(missing_wt))
    if empty_wt:
        problems.append(".wikitext 为空：" + fmt_items(empty_wt))
    if missing_md:
        problems.append(".md 缺失：" + fmt_items(missing_md))
    if bad_hash:
        problems.append("Markdown 哈希不符：" + fmt_items(bad_hash))

    expected = f"{len(rows)} 页 .wikitext／.md 齐备、.wikitext 非空、md 哈希一致"
    actual = (f"核验 {len(rows)} 页（实算哈希 {checked}），缺 wt {len(missing_wt)}、"
              f"空 wt {len(empty_wt)}、缺 md {len(missing_md)}、哈希不符 {len(bad_hash)}")
    return CheckResult(check_id, name, expected, actual, not problems,
                       "\n".join(problems) if problems else "全部一致")


def check_v3(conn) -> CheckResult:
    check_id, name = "SQL-V3", "Markdown 覆盖与 HTML 残留（独立复算）"
    total = conn.execute("SELECT COUNT(*) FROM pages").fetchone()[0]
    if not total:
        return fail(check_id, name, "至少 1 页", "0 页", "判据为空：pages 无行")

    no_fulltext = [r[0] for r in conn.execute(
        "SELECT p.page_key FROM pages p LEFT JOIN fulltext f ON p.page_key = f.page_key "
        "WHERE f.page_key IS NULL ORDER BY p.page_key").fetchall()]
    multi = [f"{r[0]}={r[1]}" for r in conn.execute(
        "SELECT page_key, COUNT(*) FROM fulltext GROUP BY page_key HAVING COUNT(*) > 1 "
        "ORDER BY page_key").fetchall()]
    count_mismatch = [f"{r[0]}：char_count {r[1]} / length {r[2]}" for r in conn.execute(
        "SELECT page_key, char_count, length(content) FROM fulltext "
        "WHERE char_count IS DISTINCT FROM length(content) ORDER BY page_key").fetchall()]
    no_blocks = [r[0] for r in conn.execute(
        "SELECT f.page_key FROM fulltext f LEFT JOIN "
        "(SELECT DISTINCT page_key FROM fulltext_blocks) b ON f.page_key = b.page_key "
        "WHERE length(f.content) > 0 AND b.page_key IS NULL ORDER BY f.page_key").fetchall()]

    html_hits: List[str] = []
    for key, content, method in conn.execute(
            "SELECT page_key, content, extraction_method FROM fulltext WHERE length(content) > 0 "
            "ORDER BY page_key").fetchall():
        if (method or "") in ("pdf-text", "pdf-ocr"):
            continue
        stripped = FENCE_RE.sub("", content or "")
        stripped = INLINE_CODE_RE.sub("", stripped)
        found = HTML_TAG_RE.findall(stripped)
        if found:
            unique = sorted({tag.strip() for tag in found})
            html_hits.append(f"{key}：{fmt_items(unique, 5)}")

    problems = []
    if no_fulltext:
        problems.append("缺 fulltext：" + fmt_items(no_fulltext))
    if multi:
        problems.append("fulltext 多行（UNIQUE 失效）：" + fmt_items(multi))
    if count_mismatch:
        problems.append("char_count 与 length(content) 不符：" + fmt_items(count_mismatch))
    if no_blocks:
        problems.append("非空正文无块：" + fmt_items(no_blocks))
    if html_hits:
        problems.append("HTML 标签残留（剥围栏与行内代码后）：" + fmt_items(html_hits))

    expected = "每页恰 1 条 fulltext；char_count == length(content)；非空页至少 1 块；无 HTML 残留"
    actual = (f"{total} 页：缺 fulltext {len(no_fulltext)}、多行 {len(multi)}、"
              f"char_count 不符 {len(count_mismatch)}、无块 {len(no_blocks)}、"
              f"HTML 残留 {len(html_hits)}")
    return CheckResult(check_id, name, expected, actual, not problems,
                       "\n".join(problems) if problems else "全部一致")


def check_v4(conn) -> CheckResult:
    check_id, name = "SQL-V4", "外链闭合（独立复算）"
    total = conn.execute("SELECT COUNT(*) FROM pages").fetchone()[0]
    if not total:
        return fail(check_id, name, "至少 1 页", "0 页", "判据为空：pages 无行")

    link_urls = {r[0] for r in conn.execute(
        "SELECT DISTINCT target_url FROM links WHERE target_kind = 'external'").fetchall()}
    page_urls = {r[0] for r in conn.execute(
        "SELECT DISTINCT canonical_url FROM pages WHERE source_kind = 'external'").fetchall()}
    excluded_urls = {r[0] for r in conn.execute(
        "SELECT DISTINCT url FROM excluded_items").fetchall()}
    failed_urls = {r[0] for r in conn.execute(
        "SELECT DISTINCT url FROM crawl_log WHERE url_kind = 'external' "
        "AND (error_type IS NOT NULL OR (http_status IS NOT NULL AND http_status >= 400))"
    ).fetchall()}
    deferred_urls = {r[0] for r in conn.execute(
        "SELECT DISTINCT canonical_url FROM pages WHERE status = 'needs_ocr_deferred'"
    ).fetchall()}

    covered = page_urls | excluded_urls | failed_urls | deferred_urls
    uncovered = sorted(link_urls - covered)
    orphan = sorted(page_urls - link_urls)

    problems = []
    if link_urls and not covered:
        problems.append("links 有外链但四类台账全为空（疑似静默丢失）")
    if uncovered:
        problems.append("links 外链未被任何台账覆盖：" + fmt_items(uncovered))

    expected = ("links 外链 URL ⊆ pages 外链行 ∪ excluded_items ∪ crawl_log 失败 URL ∪ "
                "needs_ocr_deferred")
    actual = (f"links 外链 {len(link_urls)} 个；覆盖 {len(link_urls) - len(uncovered)}，"
              f"未覆盖 {len(uncovered)}；pages 外链 {len(page_urls)}，无对应链接 {len(orphan)}")
    detail = [f"excluded {len(excluded_urls)}／crawl_log 失败 {len(failed_urls)}／"
              f"needs_ocr_deferred {len(deferred_urls)}"]
    detail.extend(problems)
    if orphan:
        detail.append("pages 外链无对应 links 行（反向披露，不判 FAIL）：" + fmt_items(orphan))
    return CheckResult(check_id, name, expected, actual, not problems, "\n".join(detail))


def check_v5(conn) -> CheckResult:
    check_id, name = "SQL-V5", "键与去重（独立复算）"
    total = conn.execute("SELECT COUNT(*) FROM pages").fetchone()[0]
    if not total:
        return fail(check_id, name, "至少 1 页", "0 页", "判据为空：pages 无行")

    dup_page_key = [f"{r[0]}×{r[1]}" for r in conn.execute(
        "SELECT page_key, COUNT(*) FROM pages GROUP BY page_key "
        "HAVING COUNT(*) > 1 ORDER BY page_key").fetchall()]
    dup_block = [f"{r[0]}#{r[1]}×{r[2]}" for r in conn.execute(
        "SELECT page_key, block_index, COUNT(*) FROM fulltext_blocks "
        "GROUP BY page_key, block_index HAVING COUNT(*) > 1 "
        "ORDER BY page_key, block_index").fetchall()]
    dup_external = [f"{r[0]}×{r[1]}" for r in conn.execute(
        "SELECT canonical_url, COUNT(*) FROM pages WHERE source_kind = 'external' "
        "GROUP BY canonical_url HAVING COUNT(*) > 1 ORDER BY canonical_url").fetchall()]
    dup_conversion = [f"{r[0]}/{r[1]}×{r[2]}" for r in conn.execute(
        "SELECT page_key, converter, COUNT(*) FROM conversions "
        "GROUP BY page_key, converter HAVING COUNT(*) > 1 "
        "ORDER BY page_key, converter").fetchall()]

    problems = []
    if dup_page_key:
        problems.append("page_key 重复：" + fmt_items(dup_page_key))
    if dup_block:
        problems.append("(page_key, block_index) 重复：" + fmt_items(dup_block))
    if dup_external:
        problems.append("外链归一 URL 重复：" + fmt_items(dup_external))
    if dup_conversion:
        problems.append("(page_key, converter) 重复：" + fmt_items(dup_conversion))

    expected = "page_key／(page_key, block_index)／外链归一 URL／(page_key, converter) 重复均为 0"
    actual = (f"重复 {len(dup_page_key)}／{len(dup_block)}／{len(dup_external)}／"
              f"{len(dup_conversion)}")
    return CheckResult(check_id, name, expected, actual, not problems,
                       "\n".join(problems) if problems else "无重复")


def check_v10(root: Path, db_path: Path) -> CheckResult:
    check_id, name = "SQL-V10", "二进制禁入（独立扫描）"
    if not root.exists():
        return fail(check_id, name, "语料目录存在", f"不存在：{root}",
                    "语料目录缺失，无法扫描")
    db_resolved = db_path.resolve()
    violations_ext: List[str] = []
    violations_magic: List[str] = []
    transient: List[str] = []
    file_count = 0

    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        resolved = path.resolve()
        if resolved == db_resolved:
            continue
        suffix = path.suffix.lower()
        if suffix in TRANSIENT_SUFFIX and path.name.startswith(db_path.name):
            transient.append(f"{path.relative_to(root)}（库临时件）")
            continue
        file_count += 1
        if suffix not in ALLOWED_TEXT_EXT:
            violations_ext.append(f"{path.relative_to(root)}（{suffix or '无扩展名'}）")
        try:
            with path.open("rb") as handle:
                head = handle.read(8)
        except OSError as exc:
            violations_magic.append(f"{path.relative_to(root)}（读取失败：{exc}）")
            continue
        for magic, kind in MAGIC_SIGNATURES:
            if head.startswith(magic):
                violations_magic.append(f"{path.relative_to(root)}（{kind}）")
                break

    problems = []
    if violations_ext:
        problems.append("扩展名不允许：" + fmt_items(violations_ext))
    if violations_magic:
        problems.append("文件头魔数命中：" + fmt_items(violations_magic))

    expected = "目录内仅 .md／.wikitext（库文件本身除外）；二进制魔数命中 0"
    actual = (f"扫描 {file_count} 个文件；扩展名违规 {len(violations_ext)}，"
              f"魔数命中 {len(violations_magic)}")
    detail = problems if problems else ["全部为纯文本"]
    if transient:
        detail.append("库临时件（不判违规）：" + fmt_items(transient))
    return CheckResult(check_id, name, expected, actual, not problems, "\n".join(detail))


def check_v12(conn, root: Path) -> CheckResult:
    check_id, name = "SQL-V12", "转换台账（独立复算）"
    total = conn.execute("SELECT COUNT(*) FROM pages").fetchone()[0]
    if not total:
        return fail(check_id, name, "至少 1 页", "0 页", "判据为空：pages 无行")

    meta_row = conn.execute(
        "SELECT value FROM schema_meta WHERE key = 'converter_version'").fetchone()
    expected_version = meta_row[0] if meta_row else None

    missing = [r[0] for r in conn.execute(
        "SELECT p.page_key FROM pages p LEFT JOIN conversions c ON p.page_key = c.page_key "
        "WHERE c.page_key IS NULL ORDER BY p.page_key").fetchall()]
    version_rows = conn.execute(
        "SELECT converter_version, COUNT(*) FROM conversions "
        "GROUP BY converter_version ORDER BY converter_version").fetchall()
    bad_version = []
    for version, count in version_rows:
        if not expected_version:
            bad_version.append(f"{version or 'NULL'}×{count}（schema_meta 缺 converter_version）")
        elif version != expected_version:
            bad_version.append(f"{version or 'NULL'}×{count}（期望 {expected_version}）")

    md_mismatch: List[str] = []
    for key, md_sha, md_path, page_sha in conn.execute(
            "SELECT c.page_key, c.md_sha256, p.md_path, p.sha256_markdown "
            "FROM conversions c JOIN pages p ON p.page_key = c.page_key "
            "WHERE c.md_sha256 IS NOT NULL ORDER BY c.page_key").fetchall():
        if not md_path:
            md_mismatch.append(f"{key}：有 md_sha256 但无 md_path")
            continue
        target = root / md_path
        if not target.exists():
            md_mismatch.append(f"{key}：{md_path} 不存在")
            continue
        digest = sha256_file(target)
        if digest != md_sha:
            md_mismatch.append(f"{key}：conversions {md_sha[:12]}… / 实测 {digest[:12]}…")
        elif page_sha and digest != page_sha:
            md_mismatch.append(f"{key}：pages.sha256_markdown {page_sha[:12]}… / 实测 {digest[:12]}…")

    missing_sha = [r[0] for r in conn.execute(
        "SELECT c.page_key FROM conversions c JOIN pages p ON p.page_key = c.page_key "
        "WHERE c.md_sha256 IS NULL AND p.status = 'active' ORDER BY c.page_key").fetchall()]

    problems = []
    if missing:
        problems.append("缺 conversions 行：" + fmt_items(missing))
    if bad_version:
        problems.append("converter_version 与 schema_meta 不一致：" + fmt_items(bad_version))
    if missing_sha:
        problems.append("active 页 conversions.md_sha256 为空：" + fmt_items(missing_sha))
    if md_mismatch:
        problems.append("md_sha256 与文件／pages 不一致：" + fmt_items(md_mismatch))

    expected = ("每页 1 条 conversions；converter_version == schema_meta.converter_version；"
                "md_sha256 == 文件 SHA-256")
    actual = (f"{total} 页：缺台账 {len(missing)}、版本不符 {len(bad_version)}、"
              f"缺哈希 {len(missing_sha)}、哈希不符 {len(md_mismatch)}；"
              f"schema_meta 版本 {expected_version or '缺失'}")
    return CheckResult(check_id, name, expected, actual, not problems,
                       "\n".join(problems) if problems else "台账完整")


def run_checks(conn, root: Path, db_path: Path,
               derived: Optional[Dict[str, Any]] = None,
               derive_error: Optional[str] = None) -> List[CheckResult]:
    """按 V1→V5、V10、V12 顺序执行全部判据；derived 为 None 且无派生错误即离线口径。"""
    return [
        check_v1(conn, derived, derive_error),
        check_v2(conn, root),
        check_v3(conn),
        check_v4(conn),
        check_v5(conn),
        check_v10(root, db_path),
        check_v12(conn, root),
    ]


# =============================================================================
# 输出与落库
# =============================================================================

def print_results(results: Sequence[CheckResult], offline: bool) -> None:
    for item in results:
        print(f"[{item.status()}] {item.check_id} {item.name}")
        print(f"       期望：{item.expected}")
        print(f"       实测：{item.actual}")
        if item.detail:
            for line in item.detail.split("\n"):
                if line.strip():
                    print(f"       说明：{line}")
    if offline:
        print("[INFO] --offline：V1 未重派生站点索引，仅比对 crawl_runs 基线与 pages 集合")


def write_verification(conn, results: Sequence[CheckResult], round_name: str,
                       run_id: Optional[str]) -> int:
    conn.execute("DELETE FROM verification WHERE round = ? AND check_id LIKE 'SQL-%'",
                 [round_name])
    next_id = conn.execute("SELECT COALESCE(MAX(id), 0) FROM verification").fetchone()[0]
    stamp = now_iso()
    written = 0
    for item in results:
        next_id += 1
        conn.execute(
            "INSERT INTO verification (id, run_id, round, check_id, check_name, expected, "
            "actual, passed, detail, verified_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [int(next_id), run_id, round_name, item.check_id, item.name,
             clip(item.expected, 800), clip(item.actual, 800), item.passed,
             clip(item.detail, 3500), stamp])
        written += 1
    return written


# =============================================================================
# 自检（七类缺陷夹具）
# =============================================================================

MD_START = "# UNIX Heritage Wiki\n\nWelcome to the TUHS wiki archive.\n"
WT_START = "====== UNIX Heritage Wiki ======\n\nWelcome to the TUHS wiki archive.\n"
MD_ALICE = "## Alice\n\nAlice wrote early UNIX utilities.\n"
WT_ALICE = "===== Alice =====\n\nAlice wrote early UNIX utilities.\n"
MD_EXTERNAL = "# Example Page\n\nExternal reference body.\n"

EXTERNAL_URL = "https://example.org/a"
EXTERNAL_PAGE_KEY = "ext:0000000000000001"


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(text.encode("utf-8"))


def _insert(conn, table: str, row: Dict[str, Any]) -> None:
    columns = list(row)
    placeholders = ", ".join("?" for _ in columns)
    conn.execute(f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({placeholders})",
                 [row[column] for column in columns])


def _execute_script(conn, script: str) -> None:
    for statement in script.split(";"):
        if statement.strip():
            conn.execute(statement)


def build_fixture(db_path: Path, root: Path, schema_text: str,
                  drop_block_unique: bool = False) -> None:
    """构造干净夹具库与落盘文件（自检基线）。"""
    import duckdb

    db_path.parent.mkdir(parents=True, exist_ok=True)
    script = schema_text
    if drop_block_unique:
        script = "\n".join(line for line in script.split("\n")
                           if "UNIQUE(page_key, block_index)" not in line)
    conn = duckdb.connect(str(db_path))
    try:
        _execute_script(conn, script)

        _write_text(root / "raw/wiki/start.wikitext", WT_START)
        _write_text(root / "raw/wiki/start.md", MD_START)
        _write_text(root / "raw/wiki/people/alice.wikitext", WT_ALICE)
        _write_text(root / "raw/wiki/people/alice.md", MD_ALICE)
        _write_text(root / "raw/external/example.org/0000000000000001.md", MD_EXTERNAL)

        pages = [
            {"id": 1, "page_key": "start", "source_kind": "wiki", "namespace": TOP_SENTINEL,
             "title": "UNIX Heritage Wiki", "url": DOKU + "?id=start",
             "canonical_url": DOKU + "?id=start", "depth": 0, "status": "active",
             "wikitext_path": "raw/wiki/start.wikitext", "md_path": "raw/wiki/start.md",
             "sha256_markdown": sha256_bytes(MD_START.encode("utf-8")),
             "char_count": len(MD_START), "fetch_mode": "live",
             "extraction_method": "wikitext", "converter": "dokuwiki-wikitext",
             "sha256_source": "0" * 64},
            {"id": 2, "page_key": "people:alice", "source_kind": "wiki",
             "namespace": "people", "title": "Alice",
             "url": DOKU + "?id=people:alice",
             "canonical_url": DOKU + "?id=people:alice", "depth": 0, "status": "active",
             "wikitext_path": "raw/wiki/people/alice.wikitext",
             "md_path": "raw/wiki/people/alice.md",
             "sha256_markdown": sha256_bytes(MD_ALICE.encode("utf-8")),
             "char_count": len(MD_ALICE), "fetch_mode": "live",
             "extraction_method": "wikitext", "converter": "dokuwiki-wikitext",
             "sha256_source": "0" * 64},
            {"id": 3, "page_key": EXTERNAL_PAGE_KEY, "source_kind": "external",
             "namespace": EXTERNAL_SENTINEL, "title": "Example Page",
             "url": EXTERNAL_URL, "canonical_url": EXTERNAL_URL, "depth": 1,
             "status": "active", "md_path": "raw/external/example.org/0000000000000001.md",
             "sha256_markdown": sha256_bytes(MD_EXTERNAL.encode("utf-8")),
             "char_count": len(MD_EXTERNAL), "fetch_mode": "live",
             "extraction_method": "html", "converter": "html-to-md",
             "sha256_source": "1" * 64},
        ]
        for row in pages:
            _insert(conn, "pages", row)

        fulltexts = [
            ("start", MD_START),
            ("people:alice", MD_ALICE),
            (EXTERNAL_PAGE_KEY, MD_EXTERNAL),
        ]
        for index, (key, body) in enumerate(fulltexts, start=1):
            _insert(conn, "fulltext", {
                "id": index, "page_key": key, "content": body,
                "char_count": len(body), "extraction_method": "wikitext",
                "encoding": "utf-8", "line_ending": "lf"})

        blocks = [
            {"page_key": "start", "block_type": "heading",
             "block_content": "UNIX Heritage Wiki"},
            {"page_key": "people:alice", "block_type": "heading", "block_content": "Alice"},
            {"page_key": EXTERNAL_PAGE_KEY, "block_type": "heading",
             "block_content": "Example Page"},
        ]
        for index, block in enumerate(blocks, start=1):
            _insert(conn, "fulltext_blocks", {
                "id": index, "page_key": block["page_key"], "block_index": 0,
                "block_type": block["block_type"], "block_level": 1,
                "heading_path": block["block_content"],
                "block_content": block["block_content"]})

        _insert(conn, "links", {
            "id": 1, "source_page_key": "start", "target_kind": "external",
            "target_url": EXTERNAL_URL, "resolution_status": "fetched"})
        _insert(conn, "links", {
            "id": 2, "source_page_key": "start", "target_kind": "internal",
            "target_url": DOKU + "?id=people:alice", "target_page_key": "people:alice",
            "resolution_status": "fetched"})

        conversions = [
            ("start", "dokuwiki-wikitext", "wiki", "0" * 64,
             sha256_bytes(MD_START.encode("utf-8"))),
            ("people:alice", "dokuwiki-wikitext", "wiki", "0" * 64,
             sha256_bytes(MD_ALICE.encode("utf-8"))),
            (EXTERNAL_PAGE_KEY, "html-to-md", "external", "1" * 64,
             sha256_bytes(MD_EXTERNAL.encode("utf-8"))),
        ]
        for index, (key, converter, kind, source_sha, md_sha) in enumerate(conversions, start=1):
            _insert(conn, "conversions", {
                "id": index, "page_key": key, "converter": converter,
                "converter_version": "tuhs-md/1.0", "source_kind": kind,
                "source_sha256": source_sha, "md_sha256": md_sha})

        scope = {
            "baseline": 2,
            "page_set_sha256": sha256_page_set(["start", "people:alice"]),
            "namespace_counts": {"people": 1, "(top)": 1},
        }
        _insert(conn, "crawl_runs", {
            "run_id": "selftest-run", "started_at": now_iso(), "finished_at": now_iso(),
            "scope_json": json.dumps(scope, ensure_ascii=False), "page_baseline": 2,
            "page_fetched": 2, "external_fetched": 1, "excluded": 0, "failed": 0,
            "status": "completed", "tool_version": "tuhs-md/1.0"})

        _insert(conn, "schema_meta", {"key": "converter_version", "value": "tuhs-md/1.0"})
        _insert(conn, "schema_meta", {"key": "page_baseline", "value": "2"})
        _insert(conn, "schema_meta", {"key": "schema_version", "value": "1.0"})
    finally:
        conn.close()


def inject_defects(db_path: Path, root: Path) -> None:
    """向夹具注入七类缺陷（漏页／缺 md／md 哈希不符／外链未闭合／重复块／二进制／台账缺失）。"""
    import duckdb

    # V2：删 md 文件（缺 md）与篡改 md 内容（哈希不符）
    (root / "raw/wiki/people/alice.md").unlink()
    with (root / "raw/wiki/start.md").open("wb") as handle:
        handle.write((MD_START + "tampered line\n").encode("utf-8"))
    # V10：二进制混入
    (root / "raw/external/example.org").mkdir(parents=True, exist_ok=True)
    (root / "raw/external/example.org/unix-manual.pdf").write_bytes(
        b"%PDF-1.4\n1 0 obj\n<< /Type /Catalog >>\nendobj\n")

    conn = duckdb.connect(str(db_path))
    try:
        # V1：基线含未抓页面
        ghost = ["features:ghost", "people:alice", "start"]
        scope = {
            "baseline": len(ghost),
            "page_set_sha256": sha256_page_set(ghost),
            "namespace_counts": {"features": 1, "people": 1, "(top)": 1},
        }
        conn.execute("UPDATE crawl_runs SET scope_json = ?, page_baseline = ?",
                     [json.dumps(scope, ensure_ascii=False), len(ghost)])
        # V4：外链未闭合
        _insert(conn, "links", {
            "id": 3, "source_page_key": "start", "target_kind": "external",
            "target_url": "https://example.org/unclosed", "resolution_status": "queued"})
        # V5：重复块（夹具已去掉 UNIQUE(page_key, block_index)）
        _insert(conn, "fulltext_blocks", {
            "id": 10, "page_key": "start", "block_index": 0, "block_type": "paragraph",
            "block_content": "duplicate block"})
        # V12：转换台账缺失
        conn.execute("DELETE FROM conversions WHERE page_key = ?", [EXTERNAL_PAGE_KEY])
    finally:
        conn.close()


def selftest() -> int:
    print("[selftest] 独立 SQL 复核器七项缺陷夹具")
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

    if not SCHEMA_SQL.exists():
        print(f"ERROR: 缺少架构 SQL：{SCHEMA_SQL}", file=sys.stderr)
        return 2
    schema_text = SCHEMA_SQL.read_text(encoding="utf-8")

    workdir = SCRIPT_DIR_TMP / f"_tuhs_sql_selftest_{os.getpid()}"
    if workdir.exists():
        shutil.rmtree(workdir)
    clean_root = workdir / "clean_root"
    defect_root = workdir / "defect_root"
    try:
        SCRIPT_DIR_TMP.mkdir(parents=True, exist_ok=True)
        clean_db = clean_root / "tuhs_wiki.duckdb"
        defect_db = defect_root / "tuhs_wiki.duckdb"
        build_fixture(clean_db, clean_root, schema_text)

        import duckdb

        conn = duckdb.connect(str(clean_db))
        try:
            results = run_checks(conn, clean_root, clean_db)
        finally:
            conn.close()
        for item in results:
            check(f"干净夹具 {item.check_id} 判 PASS", item.passed is True,
                  f"{item.actual}｜{item.detail}")

        build_fixture(defect_db, defect_root, schema_text, drop_block_unique=True)
        inject_defects(defect_db, defect_root)
        conn = duckdb.connect(str(defect_db))
        try:
            derived = scope_from_page_set({"features:ghost", "people:alice", "start"})
            bad_results = run_checks(conn, defect_root, defect_db, derived=derived)
        finally:
            conn.close()

        index = {item.check_id: item for item in bad_results}
        expectations = [
            ("SQL-V1", "features:ghost"),
            ("SQL-V2", "people:alice"),
            ("SQL-V4", "unclosed"),
            ("SQL-V5", "start"),
            ("SQL-V10", "unix-manual.pdf"),
            ("SQL-V12", EXTERNAL_PAGE_KEY),
        ]
        for check_id, marker in expectations:
            item = index[check_id]
            hit = (item.passed is False) and (marker in item.detail)
            check(f"缺陷夹具 {check_id} 命中（{marker}）", hit,
                  f"passed={item.passed} detail={clip(item.detail, 300)}")
        check("缺陷夹具 SQL-V3 未受污染", index["SQL-V3"].passed is True,
              f"{index['SQL-V3'].actual}｜{index['SQL-V3'].detail}")
        check("离线 V1 披露未重派生",
              "未重派生" in "".join(item.detail for item in results if item.check_id == "SQL-V1"))
    finally:
        shutil.rmtree(workdir, ignore_errors=True)

    print(f"[selftest] 共 {checks} 项，失败 {len(failures)} 项")
    if failures:
        for label in failures:
            print(f"  - {label}")
        return 1
    print("[selftest] 全过：七类缺陷均被对应判据命中，干净夹具七项全 PASS")
    return 0


# =============================================================================
# 入口
# =============================================================================

def check_runtime(conn) -> Tuple[Optional[str], Optional[str]]:
    """返回（错误说明，存储版本）。"""
    import duckdb

    if duckdb.__version__ != DUCKDB_REQUIRED:
        return (f"duckdb 运行时版本 {duckdb.__version__} != {DUCKDB_REQUIRED}", None)
    try:
        rows = conn.execute("SELECT database_name, tags FROM duckdb_databases()").fetchall()
    except Exception as exc:  # noqa: BLE001
        return (f"读取 duckdb_databases() 失败：{exc}", None)
    storage = None
    for _name, tags in rows:
        values = tags if isinstance(tags, dict) else {}
        if values.get("storage_version"):
            storage = values["storage_version"]
            break
    if not storage:
        return ("未能读取存储版本（duckdb_databases().tags）", None)
    if not str(storage).startswith(STORAGE_PREFIX):
        return (f"存储版本 {storage} 不满足 {STORAGE_PREFIX}0.0+", storage)
    return (None, str(storage))


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="TUHS Wiki 独立 SQL 复核器（V1–V5、V10、V12）")
    parser.add_argument("--db", default=str(DEFAULT_DB), help="库路径（默认真实库）")
    parser.add_argument("--root", default=None, help="语料目录（默认库所在目录）")
    parser.add_argument("--round", default="R2SQL", help="verification.round（默认 R2SQL）")
    parser.add_argument("--offline", action="store_true",
                        help="不联网重派生页面清单（V1 仅比对 crawl_runs 与 pages）")
    parser.add_argument("--selftest", action="store_true", help="离线七类缺陷自检")
    args = parser.parse_args(argv)

    if args.selftest:
        return selftest()

    db_path = Path(args.db).resolve()
    root = Path(args.root).resolve() if args.root else db_path.parent
    if not db_path.exists():
        print(f"ERROR: 库不存在：{db_path}", file=sys.stderr)
        return 2
    if not root.exists():
        print(f"ERROR: 语料目录不存在：{root}", file=sys.stderr)
        return 2

    try:
        import duckdb
    except ImportError:
        print("ERROR: 缺少 duckdb 依赖", file=sys.stderr)
        return 2

    try:
        conn = duckdb.connect(str(db_path))
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: 打开库失败：{exc}", file=sys.stderr)
        return 2

    try:
        error, storage = check_runtime(conn)
        if error:
            print(f"ERROR: {error}", file=sys.stderr)
            return 2
        existing = {row[0] for row in conn.execute(
            "SELECT table_name FROM information_schema.tables").fetchall()}
        missing_tables = sorted(REQUIRED_TABLES - existing)
        if missing_tables:
            print(f"ERROR: 架构不符，缺表：{fmt_items(missing_tables)}", file=sys.stderr)
            return 2

        run_row = conn.execute(
            "SELECT run_id FROM crawl_runs ORDER BY started_at DESC NULLS LAST, "
            "run_id DESC LIMIT 1").fetchone()
        run_id = run_row[0] if run_row else None

        print(f"[run] db={db_path}")
        print(f"[run] root={root}")
        print(f"[run] round={args.round} duckdb={duckdb.__version__} storage={storage} "
              f"offline={args.offline}")

        derived = None
        derive_error = None
        if not args.offline:
            print("[derive] 独立请求 ?do=index 重派生页面清单（同主机 ≥1.5 秒间隔）…")
            try:
                derived = derive_scope_online()
                print(f"[derive] 派生完成：{derived['baseline']} 页，"
                      f"SHA-256 {derived['page_set_sha256'][:16]}…，"
                      f"请求 {derived['http_requests']} 次")
            except Exception as exc:  # noqa: BLE001
                derive_error = str(exc)
                print(f"[derive] 失败：{derive_error}")

        results = run_checks(conn, root, db_path, derived=derived,
                             derive_error=derive_error)
        print_results(results, args.offline)

        written = write_verification(conn, results, args.round, run_id)
        failed = [item.check_id for item in results if item.passed is False]
        print(f"[verification] 写入 {written} 行（round={args.round}，前缀 SQL-）")
        print(f"[summary] PASS {len(results) - len(failed)}／FAIL {len(failed)}"
              + (f"：{', '.join(failed)}" if failed else ""))
        return 1 if failed else 0
    finally:
        conn.close()


if __name__ == "__main__":
    sys.exit(main())
