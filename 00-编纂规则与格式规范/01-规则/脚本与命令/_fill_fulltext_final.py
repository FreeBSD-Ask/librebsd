# -*- coding: utf-8 -*-
"""final 补齐 fulltext v2：子进程隔离 + 30 秒超时，处理剩余无 fulltext 记录

- PDF：文本层提取（子进程，超时保护）
- HTML/TXT：native_text
- 跳过：无文件、lit、CAJ、无文本层

2026-10-17 DuckDB 改造（原 SQLite 版随库升格失效，见流程规则.md
「新增文献自动检测规则」的 ⚠️ 依赖限制条）：

1. `references_fulltext` 库 2026-10-14 升格 DuckDB 主存储层，SQLite 侧
   `references_fulltext.db` 已成 0 字节空壳。旧版 `sqlite3.connect` 打开 0 字节文件会
   **静默新建空库**并把写入全丢进去——退出码 0、打印「完成」，主库零增量。故改
   `duckdb.connect`。
2. fulltext／fulltext_blocks 全 VARCHAR 且**无 PRIMARY KEY／UNIQUE 约束**（实测
   fulltext 4320 行仅 4132 个不同 id、fulltext_blocks 1000029 行仅 987062 个不同 id）。
   旧版依赖 `cur.lastrowid` 自增取号会写入 NULL id，导致新 fulltext 行 reference_id 悬空。
   现改显式取号——各表纯数字 id 当前上限 +1 起。
3. 顺带修两处旧版缺陷：
   ① PDF 子进程旧版用 `text=True`，Windows 控制台编码（cp936/cp1252）下解 PDF 抽出的
      中日韩字符会抛 UnicodeDecodeError，令可提取的文献被判「失败」——活库已有 264 条
      language='zh' 记录，该缺陷真实触发。现按字节捕获再按 UTF-8 宽容解码。
   ② fulltext_blocks.block_index 旧版对所有块恒写 0（列名失去意义），现写真实序号。
   char_offset_start／char_offset_end **刻意留空**：para_split 合并短段落并压平空白，
   块内容并非 content 的连续切片，写入偏移量等于写入错误元数据（活库另有 738k 行同样
   无偏移，口径一致）。
4. 旧版每 50 件 `commit()` 提供崩溃恢复粒度；DuckDB 逐语句自动提交，崩溃后状态仍一致
   （单条 INSERT 原子），配合幂等的「无 fulltext 才补」前置条件可直接重跑，故不再显式
   commit。

用法：
    python _fill_fulltext_final.py [--dry-run] [--limit N] [--db PATH] [--timeout S]
                                   [--resolve-root DIR]

--db 指向其他 DuckDB 文件（验收请指向临时副本，禁止默认对主库跑）；
--resolve-root 改库内相对 file_path 的解析根（默认仓库根，与活库现行值同形）。
"""
import argparse
import os
import re
import subprocess
import sys
from datetime import datetime, timedelta, timezone

import duckdb

# 脚本位于 00-编纂规则与格式规范/01-规则/脚本与命令/，上溯 3 级为仓库根
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DB_REL = os.path.join("04-现代研究文献", "05-参考文献全文数据库",
                      "references_fulltext.duckdb")

TZ = timezone(timedelta(hours=8))
MIN_TEXT = 50
NUM_ID_RE = "^[0-9]+$"
MERGED_BY = "fill_fulltext_duckdb_20261017"

PDF_WORKER = """import fitz, sys, os
fitz.TOOLS.mupdf_display_errors(False)
p = sys.argv[1]
doc = fitz.open(p)
t = ""
for i in range(len(doc)):
    try: t += doc[i].get_text()
    except Exception: pass
doc.close()
sys.stdout.write("TEXT_START")
sys.stdout.write(t)
sys.stdout.write("TEXT_END")
"""


def resolve(fp, root=ROOT):
    """把库内相对 file_path 解析为磁盘绝对路径。

    活库现行值以仓库根为基准（实测 5786 条有值中 5067 条按仓库根可解析、0 条仅按
    03-文献下载 可解析），故先试仓库根，再试直接挂到 03-文献下载 下的旧形制。
    """
    if not fp:
        return None
    p = fp.replace("\\", "/")
    for cand in (os.path.join(root, p),
                 os.path.join(root, "04-现代研究文献/03-文献下载", p)):
        if os.path.exists(cand):
            return cand
    return None


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


def next_ids(con, table, n):
    """取 n 个未占用的新 id。

    基准只取**纯数字** id：reference_duplicates 另有 `DUP_<hash>` 形 id（活库实测存在），
    混进数值比较会抛 Conversion Error。DuckDB LIKE 的 `[^...]` 负向字符类不可靠
    （实测把已知非数字 id 判成 0 命中），故一律用 regexp_matches。
    """
    top = con.execute(
        'SELECT MAX(TRY_CAST(id AS BIGINT)) FROM "{}" '
        "WHERE id IS NOT NULL AND id <> '' AND regexp_matches(id, ?)".format(table),
        [NUM_ID_RE]).fetchone()[0]
    top = int(top) if top is not None else 0
    return [str(top + i) for i in range(1, n + 1)]


def pdf_extract(real, timeout):
    """子进程提取 PDF 文本层，超时保护；按字节捕获避免控制台编码破坏中日韩字符。"""
    r = subprocess.run([sys.executable, "-c", PDF_WORKER, real],
                       capture_output=True, timeout=timeout)
    out = (r.stdout or b"").decode("utf-8", errors="ignore")
    if "TEXT_START" not in out:
        return None
    return out.split("TEXT_START", 1)[1].split("TEXT_END", 1)[0]


def dep_report():
    try:
        __import__("fitz")
    except Exception:
        print("[依赖缺失] fitz（PyMuPDF）— PDF 文本层将无法提取，"
              "PDF 记录将计为「无文本层」", flush=True)


def main():
    ap = argparse.ArgumentParser(description="补齐 references_fulltext 的 fulltext")
    ap.add_argument("--db", default=os.path.join(ROOT, DB_REL),
                    help="目标 DuckDB 路径（默认主库；验收请指向临时副本）")
    ap.add_argument("--dry-run", action="store_true", help="只判定，不写库")
    ap.add_argument("--limit", type=int, default=0, help="本批最多处理件数，0＝不限")
    ap.add_argument("--timeout", type=int, default=30, help="单件 PDF 提取超时秒数")
    ap.add_argument("--resolve-root", default=ROOT, help="库内相对 file_path 的解析根")
    args = ap.parse_args()

    db = os.path.abspath(args.db)
    if not os.path.exists(db):
        print("数据库不存在: %s" % db)
        return 2
    dep_report()

    con = duckdb.connect(db)
    try:
        now = datetime.now(TZ).strftime("%Y-%m-%dT%H:%M:%S+08:00")
        rows = con.execute(
            'SELECT r.id, r.filename, r.file_path FROM "references" r '
            "WHERE NOT EXISTS (SELECT 1 FROM fulltext f WHERE f.reference_id = r.id) "
            "AND r.filename NOT LIKE 'SFU_PUPS_%' "
            "AND r.filename NOT LIKE '%.caj' "
            "ORDER BY TRY_CAST(r.id AS BIGINT)").fetchall()
        print("待处理: %d" % len(rows), flush=True)

        if args.limit > 0:
            rows = rows[:args.limit]

        done = no_file = no_text = fail = 0
        for i, (rid, fn, fp) in enumerate(rows, 1):
            real = resolve(fp, args.resolve_root)
            if not real:
                no_file += 1
                continue
            low = fn.lower()
            try:
                if low.endswith((".html", ".htm", ".txt")):
                    with open(real, encoding="utf-8", errors="ignore") as f:
                        text = f.read()
                    if low.endswith((".html", ".htm")):
                        text = re.sub(r"<[^>]+>", " ", text)
                        text = re.sub(r"\s+", " ", text)
                    method = "native_text"
                    if len(text.strip()) < MIN_TEXT:
                        no_text += 1
                        continue
                else:
                    text = pdf_extract(real, args.timeout)
                    if text is None:
                        fail += 1
                        continue
                    method = "pymupdf_textlayer"
                    if len(text.strip()) < MIN_TEXT:
                        no_text += 1
                        continue
            except subprocess.TimeoutExpired:
                fail += 1
                continue
            except Exception:
                fail += 1
                continue

            if args.dry_run:
                print("  [dry-run] 会补 id=%s %s method=%s 字数=%d"
                      % (rid, fn, method, len(text)), flush=True)
                done += 1
                continue

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
            if done % 50 == 0:
                print("  进度 %d/%d" % (done, i), flush=True)

        print("完成: 写入 %d, 无文件 %d, 无文本层 %d, 失败 %d%s"
              % (done, no_file, no_text, fail, "  [dry-run]" if args.dry_run else ""),
              flush=True)
    finally:
        con.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
