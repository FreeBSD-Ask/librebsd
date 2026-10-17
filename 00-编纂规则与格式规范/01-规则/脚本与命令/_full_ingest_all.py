# -*- coding: utf-8 -*-
"""全量入库：04-现代研究文献/03-文献下载/ 下所有未入库文件

- html/htm：提取正文（去 script/style/nav 等标签）-> references + fulltext
- md/txt/srt/vtt：native_text
- pdf：文本层（有则入，无则跳过标记）
- epub：ebooklib 提取
- 幂等 + sha256/file_path/filename 三重去重

2026-10-17 DuckDB 改造（原 SQLite 版随库升格失效，见流程规则.md
「新增文献自动检测规则」的 ⚠️ 依赖限制条）：

1. `references_fulltext` 库 2026-10-14 升格 DuckDB 主存储层，SQLite 侧
   `references_fulltext.db` 已成 0 字节空壳。旧版 `sqlite3.connect` 打开 0 字节文件
   会**静默新建一个空库**并把全部写入丢进这个空壳——退出码 0、打印「完成」，主库
   零增量。故改 `duckdb.connect` 直指主库。
2. 四表全部 VARCHAR 且**无 PRIMARY KEY／UNIQUE 约束**（实测 fulltext 4320 行仅 4132
   个不同 id、fulltext_blocks 1000029 行仅 987062 个不同 id，各含 3／12782 个空 id）。
   旧版依赖 `cur.lastrowid` 自增取号会写入 NULL id；`INSERT OR IGNORE` 在 DuckDB 无
   约束表上直接抛 Binder Error（要求显式 ON CONFLICT 列）。现改：
   ① 显式取号——各表纯数字 id 当前上限 +1 起；
   ② 去重改用 `WHERE NOT EXISTS` 显式判重，语义等价于旧版 INSERT OR IGNORE。
3. 取值口径对齐活库现行词表：extraction_method 用 `pymupdf_textlayer`／`native_text`
   （活库实测各 1702／971 行），弃用旧版发明的 `pymupdf/ebooklib/mobi/xparse-ocr`
   （活库 0 行）；source_tier `primary`（2113 行）、ocr_status `verified`（2190 行）、
   line_ending `LF`（2148 行）、encoding `utf-8`（4135 行）、duplicate_type `sha256`
   （274 行）、duplicate_reference_id 占位 `'0'`（454 行）、match_score `'1.0'`
   （814 行）均照旧。
4. 顺带修一处旧版缺陷：fulltext_blocks.block_index 旧版对所有块恒写 0（列名失去意义），
   现写真实序号。char_offset_start／char_offset_end **刻意留空**——para_split 会合并
   短段落并压平空白，块内容并非 content 的连续切片，写入偏移量等于写入错误元数据
   （活库另有 738k 行同样无偏移，口径一致）。

用法：
    python _full_ingest_all.py [--dry-run] [--limit N] [--db PATH]

--dry-run 只扫描与判重、不写库（用于验收判定口径）；--limit 限制本批入库件数；
--db 指向其他 DuckDB 文件（验收请指向临时副本，禁止默认对主库跑）；
--base-dir 指向其他下载根（验收用沙箱目录；亦可用于只对某个批次目录做增量入库）。
"""
import argparse
import hashlib
import os
import re
import sys
from datetime import datetime, timedelta, timezone

import duckdb

# 脚本位于 00-编纂规则与格式规范/01-规则/脚本与命令/，上溯 3 级为仓库根
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DB_REL = os.path.join("04-现代研究文献", "05-参考文献全文数据库",
                      "references_fulltext.duckdb")
BASE_DIR_REL = os.path.join("04-现代研究文献", "03-文献下载")

TZ = timezone(timedelta(hours=8))
MERGED_BY = "full_ingest_duckdb_20261017"
MIN_TEXT = 50  # 提取正文最短字符数，短于此判为无文本
NUM_ID_RE = "^[0-9]+$"


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def extract_html_text(html):
    """提取网页正文：去 script/style/nav/header/footer/iframe 等"""
    text = re.sub(r"<(script|style|nav|header|footer|iframe|form|aside|noscript)[^>]*>.*?</\1>",
                  " ", html, flags=re.S | re.I)
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def para_split(text):
    raw = [p.strip() for p in text.split("\n\n") if p.strip()]
    paras, buf = [], ""
    for p in raw:
        p = " ".join(p.split())
        if len(p) < 40 and buf:
            buf += " " + p
            if len(buf) >= 40:
                paras.append(buf)
                buf = ""
        else:
            if buf:
                paras.append(buf)
                buf = ""
            paras.append(p)
    if buf:
        paras.append(buf)
    return paras


def extract_text(fp, low):
    """返回 (text, method) 或 None。缺依赖时该格式计为无文本，不中断整批。"""
    if low.endswith((".html", ".htm")):
        with open(fp, encoding="utf-8", errors="ignore") as f:
            text = extract_html_text(f.read())
        return (text, "native_text") if len(text) > MIN_TEXT else None
    if low.endswith((".md", ".txt", ".srt", ".vtt")):
        with open(fp, encoding="utf-8", errors="ignore") as f:
            text = f.read()
        return (text, "native_text") if len(text.strip()) > MIN_TEXT else None
    if low.endswith(".pdf"):
        try:
            import fitz
            fitz.TOOLS.mupdf_display_errors(False)
        except Exception:
            return None
        doc = fitz.open(fp)
        text = ""
        for i in range(len(doc)):
            try:
                text += doc[i].get_text()
            except Exception:
                pass
        doc.close()
        return (text, "pymupdf_textlayer") if len(text.strip()) > MIN_TEXT else None
    if low.endswith(".epub"):
        try:
            import ebooklib
            from ebooklib import epub
        except Exception:
            return None
        try:
            book = epub.read_epub(fp)
            parts = []
            for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
                content = item.get_content().decode("utf-8", errors="ignore")
                parts.append(extract_html_text(content))
            text = "\n\n".join(p for p in parts if p)
            return (text, "native_text") if len(text) > MIN_TEXT else None
        except Exception:
            return None
    return None


def next_ids(con, table, n):
    """取 n 个未占用的新 id，各占 1 个连续序号。

    基准只取**纯数字** id：reference_duplicates 另有 `DUP_<hash>` 形 id（活库实测
    存在），混进数值比较会抛 Conversion Error。DuckDB LIKE 的 `[^...]` 负向字符类
    不可靠（实测把已知非数字 id 判成 0 命中），故一律用 regexp_matches。
    """
    top = con.execute(
        'SELECT MAX(TRY_CAST(id AS BIGINT)) FROM "{}" '
        "WHERE id IS NOT NULL AND id <> '' AND regexp_matches(id, ?)".format(table),
        [NUM_ID_RE]).fetchone()[0]
    top = int(top) if top is not None else 0
    return [str(top + i) for i in range(1, n + 1)]


def dup_exists(con, primary_id, dup_type):
    """该主记录是否已登记过此类型的重复项——等价于旧版 INSERT OR IGNORE 的去重语义。"""
    return con.execute(
        "SELECT COUNT(*) FROM reference_duplicates WHERE primary_reference_id = ? "
        "AND duplicate_type = ?", [primary_id, dup_type]).fetchone()[0] > 0


def dep_report():
    miss = []
    for mod, why in (("fitz", "PDF 文本层"), ("ebooklib", "EPUB")):
        try:
            __import__(mod)
        except Exception:
            miss.append((mod, why))
    if miss:
        print("[依赖缺失] " + "；".join("%s（%s）" % (m, w) for m, w in miss)
              + " — 对应格式计为「无文本/待OCR」，其余格式正常入库", flush=True)
    return miss


def main():
    ap = argparse.ArgumentParser(description="全量入库：03-文献下载 下未入库文件")
    ap.add_argument("--db", default=os.path.join(ROOT, DB_REL),
                    help="目标 DuckDB 路径（默认主库；验收请指向临时副本）")
    ap.add_argument("--dry-run", action="store_true", help="只扫描判重，不写库")
    ap.add_argument("--limit", type=int, default=0, help="本批最多入库件数，0＝不限")
    ap.add_argument("--base-dir", default=os.path.join(ROOT, BASE_DIR_REL),
                    help="下载根目录（默认 03-文献下载；验收请指向沙箱目录）")
    args = ap.parse_args()

    db = os.path.abspath(args.db)
    if not os.path.exists(db):
        print("数据库不存在: %s" % db)
        return 2
    base_dir = os.path.abspath(args.base_dir)
    if not os.path.isdir(base_dir):
        print("下载目录不存在: %s" % base_dir)
        return 2
    dep_report()

    con = duckdb.connect(db)
    try:
        now = datetime.now(TZ).strftime("%Y-%m-%dT%H:%M:%S+08:00")

        existing_fns, existing_paths, existing_shas = set(), set(), set()
        for (fn,) in con.execute('SELECT filename FROM "references" WHERE filename IS NOT NULL '
                                 "AND filename <> ''"):
            existing_fns.add(fn)
        for (fp,) in con.execute('SELECT file_path FROM "references" WHERE file_path IS NOT NULL '
                                 "AND file_path <> ''"):
            existing_paths.add(fp.replace("\\", "/"))
        for (s,) in con.execute('SELECT sha256 FROM "references" WHERE sha256 IS NOT NULL '
                                "AND sha256 <> ''"):
            existing_shas.add(s)

        files = []
        # 活库 file_path 现行值以**仓库根**为基准（实测 5786 条有值中 4953 条以
        # `04-现代研究文献` 起首、5067 条按仓库根可解析、0 条仅按 03-文献下载 可解析），
        # 故 rel 一律相对仓库根计算，保持与既有行同形；沙箱目录不在仓库内时回退相对
        # CWD（与旧版一致）。
        base_ref = ROOT if base_dir.startswith(os.path.normpath(ROOT) + os.sep) \
            else os.getcwd()
        for root, _, fs in os.walk(base_dir):
            parts = root.split(os.sep)
            if "ocr" in parts or "00-临时放置" in parts or "10-无关文件" in parts:
                continue
            for fn in fs:
                if fn.startswith("._"):
                    continue
                low = fn.lower()
                if not low.endswith((".pdf", ".html", ".htm", ".md", ".txt", ".srt",
                                     ".vtt", ".epub")):
                    continue
                rel = os.path.relpath(os.path.join(root, fn), base_ref).replace("\\", "/")
                if fn in existing_fns or rel in existing_paths:
                    continue
                files.append((os.path.join(root, fn), fn, rel))
        print("未入库文件: %d" % len(files), flush=True)

        if args.limit > 0:
            files = files[:args.limit]

        done = no_text = dup = fail = 0
        for i, (fp, fn, rel) in enumerate(files, 1):
            low = fn.lower()
            try:
                with open(fp, "rb") as f:
                    head = f.read(4)
                if low.endswith(".pdf") and head != b"%PDF":
                    fail += 1
                    continue
                sha = sha256_file(fp)
                if sha in existing_shas:
                    row = con.execute(
                        'SELECT id FROM "references" WHERE sha256 = ? LIMIT 1',
                        [sha]).fetchone()
                    if row and not args.dry_run and not dup_exists(con, row[0], "sha256"):
                        con.execute(
                            "INSERT INTO reference_duplicates (id, primary_reference_id, "
                            "duplicate_reference_id, duplicate_type, match_score, "
                            "match_fields, merged_at, merged_by, merge_notes) VALUES "
                            "(?,?,?,?,?,?,?,?,?)",
                            next_ids(con, "reference_duplicates", 1) + [
                                row[0], "0", "sha256", "1.0", "sha256",
                                now, MERGED_BY, "sha256 dup for " + fn])
                    dup += 1
                    continue
                res = extract_text(fp, low)
                if res is None:
                    no_text += 1
                    continue
                text, method = res
            except Exception:
                fail += 1
                continue

            if args.dry_run:
                print("  [dry-run] 会入库 %s method=%s 字数=%d" % (rel, method, len(text)),
                      flush=True)
                done += 1
                continue

            rid = next_ids(con, "references", 1)[0]
            title = os.path.splitext(fn)[0].replace("_", " ").replace("-", " ")
            fmt = ("html" if low.endswith((".html", ".htm")) else
                   ("epub" if low.endswith(".epub") else "txt"))
            con.execute(
                'INSERT INTO "references" (id, title, author, year, format, file_path, '
                "filename, sha256, file_size, source_tier, created_at, updated_at, "
                "ocr_status) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                [rid, title, "unknown", None, fmt, rel, fn, sha, str(os.path.getsize(fp)),
                 "primary", now, now, "verified"])
            existing_shas.add(sha)
            existing_fns.add(fn)
            existing_paths.add(rel)

            con.execute(
                "INSERT INTO fulltext (id, reference_id, content, char_count, "
                "extraction_method, extracted_at, encoding, line_ending) VALUES "
                "(?,?,?,?,?,?,?,?)",
                next_ids(con, "fulltext", 1) + [rid, text, str(len(text)), method,
                                                now, "utf-8", "LF"])
            paras = para_split(text)
            for k, blk in enumerate(paras):
                con.execute(
                    "INSERT INTO fulltext_blocks (id, reference_id, block_index, "
                    "block_type, block_level, block_content) VALUES (?,?,?,?,?,?)",
                    next_ids(con, "fulltext_blocks", 1) + [rid, str(k), "paragraph",
                                                            1, blk])
            done += 1
            if done % 100 == 0:
                print("  进度 %d/%d" % (done, i), flush=True)

        print("完成: 入库 %d, 无文本/待OCR %d, sha256重复 %d, 失败 %d%s"
              % (done, no_text, dup, fail, "  [dry-run]" if args.dry_run else ""),
              flush=True)
    finally:
        con.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
