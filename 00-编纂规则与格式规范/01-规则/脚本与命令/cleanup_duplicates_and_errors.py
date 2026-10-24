# -*- coding: utf-8 -*-
"""重复与错误文档清理（DuckDB 主存储层版；TD-029 偿还件）。

原 SQLite 版于 2026-10-14 `references_fulltext` 升格 DuckDB 后失效：脚本仍以
`sqlite3.connect(references_fulltext.db)` 为入口，而该 `.db` 是 0 字节空壳，
`sqlite3` 会静默新建空库、把全部读写丢进空壳（退出码仍为 0）。本版改造要点：

1. 连接改为 `duckdb.connect(references_fulltext.duckdb)`；`references` 是 DuckDB
   保留字，SQL 一律写 `"references"`。
2. `id` 列为 VARCHAR，不能直接用 `MIN(id)` 取主副本（字典序会把 "10" 排在 "9" 前）；
   改取组内 id 按数值优先排序后的最小者。
3. 无 `cur.lastrowid`、无 `commit()`（DuckDB 自动提交）；`reference_duplicates`
   实测无唯一约束，`INSERT OR IGNORE` 无冲突目标可用，改为 `WHERE NOT EXISTS` 判重。
4. 补 `--db`、`--selftest`：后者以两份临时库夹具断言“零重复”与“有重复＋错误文件”两类。
5. 默认只识别并生成清单；`--execute` 才删文件（不可逆），删前仍做四项核验。

用法：
    python cleanup_duplicates_and_errors.py                # 仅识别，生成清单
    python cleanup_duplicates_and_errors.py --sample-only   # 打印抽样复核条目
    python cleanup_duplicates_and_errors.py --execute       # 执行删除（不可逆）
    python cleanup_duplicates_and_errors.py --selftest      # 判据非空自检
"""
import argparse
import hashlib
import json
import shutil
import sys
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Tuple

import duckdb

BASE = Path(r"d:\librebsd")
DB_PATH = BASE / "04-现代研究文献" / "05-参考文献全文数据库" / "references_fulltext.duckdb"
LOG_DIR = BASE / "script" / "_cleanup_logs"
PENDING_FILE = LOG_DIR / "pending_deletion.jsonl"
DELETION_LOG = LOG_DIR / "deletion_log.jsonl"
DASHBOARD_FILE = LOG_DIR / "dashboard.md"


def ensure_log_dir():
    LOG_DIR.mkdir(parents=True, exist_ok=True)


def compute_sha256(file_path: Path) -> str:
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def _id_key(rid: Any) -> Tuple[int, Any]:
    """id 排序键：纯数字按数值，其余按字符串，避免 "10" < "9" 的字典序错误。"""
    s = str(rid)
    return (0, int(s)) if s.isdigit() else (1, s)


def _rows_by_id(con, ids: List[Any]) -> Dict[Any, Tuple]:
    if not ids:
        return {}
    ph = ",".join("?" for _ in ids)
    rows = con.execute(
        'SELECT id, file_path, filename, title, author, year, status '
        'FROM "references" WHERE id IN (%s)' % ph, ids).fetchall()
    return {r[0]: r for r in rows}


def identify_duplicates(con) -> List[Dict[str, Any]]:
    """识别重复文件：SHA-256 精确重复 + 标题/作者/年份模糊重复。

    保留规则：每组保留 id（数值序）最小者为主副本，其余为待删除副本。
    """
    pending = []

    # === SHA-256 精确重复 ===
    groups = con.execute(
        'SELECT sha256, list(id) AS ids FROM "references" '
        "WHERE sha256 IS NOT NULL AND sha256 <> '' "
        "AND status NOT IN ('deleted', 'rejected') "
        "GROUP BY sha256 HAVING count(*) > 1").fetchall()
    for sha, raw_ids in groups:
        ids = sorted(raw_ids, key=_id_key)
        primary_id = ids[0]
        rows = _rows_by_id(con, [i for i in ids if i != primary_id])
        for rid in ids:
            if rid == primary_id or rid not in rows:
                continue
            row = rows[rid]
            pending.append({
                "reference_id": rid,
                "file_path": row[1],
                "filename": row[2],
                "title": row[3],
                "author": row[4],
                "year": row[5],
                "current_status": row[6],
                "reason": "exact_duplicate",
                "primary_reference_id": primary_id,
                "sha256": sha,
            })

    # === 标题+作者+年份模糊重复 ===
    exact_dup_ids = {p["reference_id"] for p in pending}
    groups = con.execute(
        'SELECT lower(title) AS t, lower(author) AS a, year AS y, list(id) AS ids '
        'FROM "references" WHERE title IS NOT NULL AND title <> \'\' '
        "AND status NOT IN ('deleted', 'rejected') "
        "GROUP BY t, a, y HAVING count(*) > 1").fetchall()
    for _t, _a, _y, raw_ids in groups:
        ids = sorted(raw_ids, key=_id_key)
        primary_id = ids[0]
        targets = [i for i in ids if i != primary_id and i not in exact_dup_ids]
        rows = _rows_by_id(con, targets)
        for rid in targets:
            if rid not in rows:
                continue
            row = rows[rid]
            pending.append({
                "reference_id": rid,
                "file_path": row[1],
                "filename": row[2],
                "title": row[3],
                "author": row[4],
                "year": row[5],
                "current_status": row[6],
                "reason": "fuzzy_duplicate",
                "primary_reference_id": primary_id,
                "sha256": "",
            })

    return pending


def identify_errors(con) -> List[Dict[str, Any]]:
    """识别错误文件：损坏、无法读取、文件过小（仅标记复核，不自动删除）。

    保守策略：仅对明确损坏（header 错误）的文件标记删除；
    文件过小不自动删除（多为合法短论文/幻灯片），仅标记 reason=too_small_review。
    """
    pending = []
    rows = con.execute(
        'SELECT id, file_path, filename, "format", title, author, year, status, file_size '
        'FROM "references" WHERE status NOT IN (\'deleted\', \'rejected\')').fetchall()
    for ref_id, fp, fname, fmt, title, author, year, status, fsize in rows:
        if not fp:
            continue
        full = BASE / fp
        if not full.exists():
            pending.append({
                "reference_id": ref_id, "file_path": fp, "filename": fname,
                "title": title, "author": author, "year": year,
                "current_status": status, "reason": "missing_file",
                "primary_reference_id": 0, "sha256": "",
            })
            continue

        try:
            with open(full, "rb") as f:
                header = f.read(8)
            # 判坏以**实际扩展名**为准，不认 `format` 列：实测 1,248 行 .md 摘要的 format
            # 标为 'pdf'（总目摘要件），按 format 判会把 136 个 .md 文件误判为“损坏”并在
            # --execute 下真删——本版以扩展名闸住该误判（2026-10-24 修）。
            ext = Path(fp).suffix.lower()
            is_corrupted = False
            if ext == ".pdf" and not header.startswith(b"%PDF-"):
                is_corrupted = True
            elif ext == ".epub" and not header.startswith(b"PK"):
                is_corrupted = True

            if is_corrupted:
                pending.append({
                    "reference_id": ref_id, "file_path": fp, "filename": fname,
                    "title": title, "author": author, "year": year,
                    "current_status": status, "reason": "corrupted",
                    "primary_reference_id": 0, "sha256": "", "header_hex": header.hex(),
                })
                continue
        except Exception as e:
            pending.append({
                "reference_id": ref_id, "file_path": fp, "filename": fname,
                "title": title, "author": author, "year": year,
                "current_status": status, "reason": "unreadable",
                "primary_reference_id": 0, "sha256": "", "error": str(e),
            })
            continue

        # 文件过小：仅标记复核（< 10KB 且非 caj）；同样以扩展名判 caj，不认 format 列
        try:
            size_val = int(fsize) if fsize not in (None, "") else 0
        except (TypeError, ValueError):
            size_val = 0
        if ext != ".caj" and 0 < size_val < 10240:
            pending.append({
                "reference_id": ref_id, "file_path": fp, "filename": fname,
                "title": title, "author": author, "year": year,
                "current_status": status, "reason": "too_small_review",
                "primary_reference_id": 0, "sha256": "", "file_size": size_val,
            })

    return pending


def generate_pending_list(duplicates: List[Dict], errors: List[Dict]) -> Tuple[int, int]:
    """生成待删除清单。返回 (自动删除条目数, 人工复核条目数)。"""
    ensure_log_dir()
    auto_delete, review_only = [], []
    for item in duplicates:
        auto_delete.append(item)
    for item in errors:
        if item["reason"] in ("corrupted", "unreadable", "missing_file"):
            auto_delete.append(item)
        elif item["reason"] == "too_small_review":
            review_only.append(item)

    with open(PENDING_FILE, "w", encoding="utf-8", newline="\n") as f:
        for item in auto_delete:
            item["action"] = "delete"
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
        for item in review_only:
            item["action"] = "review_only"
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

    return len(auto_delete), len(review_only)


def _dup_row_exists(con, primary_id, ref_id, dup_type) -> bool:
    """等价的 INSERT OR IGNORE 判重（该表无唯一约束，不能靠冲突忽略）。"""
    n = con.execute(
        "SELECT count(*) FROM reference_duplicates "
        "WHERE primary_reference_id = ? AND duplicate_reference_id = ? AND duplicate_type = ?",
        [str(primary_id), str(ref_id), dup_type]).fetchone()[0]
    return n > 0


def pre_deletion_checks(con, item: Dict) -> Tuple[bool, str]:
    """删除前核验：主副本存在性、章节复核引用。返回 (是否通过, 原因)。"""
    ref_id = item["reference_id"]
    reason = item["reason"]

    if reason in ("exact_duplicate", "fuzzy_duplicate"):
        primary_id = item["primary_reference_id"]
        row = con.execute('SELECT file_path FROM "references" WHERE id = ?', [primary_id]).fetchone()
        if not row or not row[0]:
            return False, "主副本 id={} 不存在于数据库".format(primary_id)
        primary_path = BASE / row[0]
        if not primary_path.exists():
            return False, "主副本文件不存在: {}".format(row[0])

    cr_rows = con.execute(
        "SELECT id, chapter FROM chapter_reviews "
        "WHERE revised_reference_ids LIKE ? OR review_reference_ids LIKE ?",
        ["%{}%".format(ref_id), "%{}%".format(ref_id)]).fetchall()
    if cr_rows:
        return False, "被 chapter_reviews 引用: {}".format(cr_rows)

    return True, "通过"


def execute_deletion(con, item: Dict) -> Tuple[bool, str]:
    """执行单个删除操作。返回 (是否成功, 消息)。文件删除不可逆。"""
    ref_id = item["reference_id"]
    fp = item["file_path"]
    full = BASE / fp

    ok, msg = pre_deletion_checks(con, item)
    if not ok:
        return False, "核验失败: {}".format(msg)

    file_deleted = False
    if full.exists():
        try:
            full.unlink()
            file_deleted = True
        except Exception as e:
            return False, "文件删除失败: {}".format(e)

    now = datetime.now().strftime("%Y-%m-%d")
    con.execute('UPDATE "references" SET status = ?, file_path = ? WHERE id = ?',
                ["deleted", "[DELETED {}] {}".format(now, fp), ref_id])

    dup_type = None
    note = ""
    if item["reason"] in ("exact_duplicate", "fuzzy_duplicate"):
        dup_type = "exact" if item["reason"] == "exact_duplicate" else "fuzzy"
        note = "清理脚本删除{}重复: {}".format(dup_type, item.get("title", ""))
    elif item["reason"] in ("corrupted", "unreadable", "missing_file"):
        dup_type = item["reason"]
        note = "清理脚本删除错误文件({}): {}".format(item["reason"], item.get("title", ""))
    if dup_type and not _dup_row_exists(con, item.get("primary_reference_id", 0), ref_id, dup_type):
        con.execute(
            "INSERT INTO reference_duplicates (primary_reference_id, duplicate_reference_id, "
            "duplicate_type, match_score, match_fields, merged_at, merged_by, merge_notes) "
            "VALUES (?, ?, ?, '1.0', ?, ?, 'cleanup_script', ?)",
            [str(item.get("primary_reference_id", 0)), str(ref_id), dup_type,
             "file_path={}".format(fp), datetime.now().strftime("%Y-%m-%d %H:%M:%S"), note])

    return True, "已删除 file_deleted={}".format(file_deleted)


def log_deletion(item: Dict, success: bool, msg: str):
    ensure_log_dir()
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "reference_id": item["reference_id"],
        "file_path": item["file_path"],
        "reason": item["reason"],
        "primary_reference_id": item.get("primary_reference_id", 0),
        "success": success,
        "message": msg,
        "operator": "cleanup_script",
    }
    with open(DELETION_LOG, "a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def update_dashboard(stats: Dict[str, int]):
    ensure_log_dir()
    content = """# 重复与错误文档清理看板

## 本次清理统计

| 指标 | 数值 |
| --- | --- |
| 本次清理时间 | {ts} |
| 待删除（自动）数 | {pending_delete} |
| 待复核（人工）数 | {pending_review} |
| 成功删除数 | {deleted} |
| 删除失败数 | {failed} |
| 保留主副本数 | {primary_kept} |
""".format(ts=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), **stats)
    DASHBOARD_FILE.write_text(content, encoding="utf-8", newline="\n")


# ---------------- 自检（判据非空） ----------------

FIXTURE_DDL = [
    'CREATE TABLE "references"(id VARCHAR, file_path VARCHAR, filename VARCHAR, '
    '"format" VARCHAR, title VARCHAR, author VARCHAR, year VARCHAR, status VARCHAR, '
    'file_size VARCHAR, sha256 VARCHAR)',
    "CREATE TABLE reference_duplicates(id VARCHAR, primary_reference_id VARCHAR, "
    "duplicate_reference_id VARCHAR, duplicate_type VARCHAR, match_score VARCHAR, "
    "match_fields VARCHAR, merged_at VARCHAR, merged_by VARCHAR, merge_notes VARCHAR)",
    "CREATE TABLE chapter_reviews(id VARCHAR, chapter VARCHAR, "
    "revised_reference_ids VARCHAR, review_reference_ids VARCHAR)",
]


def _selftest_case(tmp: Path, with_dups: bool) -> Dict[str, int]:
    dbp = tmp / "case.duckdb"
    if dbp.exists():
        dbp.unlink()
    con = duckdb.connect(str(dbp))
    for ddl in FIXTURE_DDL:
        con.execute(ddl)

    data = tmp / "files"
    data.mkdir(exist_ok=True)
    big_a = b"%PDF-1.4\n" + b"A" * 20000
    (data / "a.pdf").write_bytes(big_a)
    (data / "b.pdf").write_bytes(big_a)                     # 与 a 同内容 → 精确重复
    (data / "c.pdf").write_bytes(b"%PDF-1.4\n" + b"C" * 20000)  # 同标题作者年份 → 模糊重复
    same = b"%PDF-1.4\n" + b"D" * 20000
    (data / "d.pdf").write_bytes(same)                      # id 7 与 11 同内容 → 数值序取 7
    (data / "e.pdf").write_bytes(same)
    (data / "bad.pdf").write_bytes(b"NOTPDF!!")             # 损坏
    (data / "small.pdf").write_bytes(b"%PDF-1.4\nx")        # 过小（<10KB）
    (data / "note.md").write_text("# 摘要\n正文\n", encoding="utf-8")  # .md 摘要，format 却标 pdf

    rel = lambda p: str(data / p)  # 夹具用绝对路径：BASE / 绝对路径 == 绝对路径
    sha_a = compute_sha256(data / "a.pdf")
    sha_b = compute_sha256(data / "b.pdf")
    sha_c = compute_sha256(data / "c.pdf")
    sha_d = compute_sha256(data / "d.pdf")
    sha_e = compute_sha256(data / "e.pdf")
    rows = [
        ("1", rel("a.pdf"), "a.pdf", "pdf", "Book", "Author", "2000", "active", "20009", sha_a),
        ("2", rel("bad.pdf"), "bad.pdf", "pdf", "Bad", "Author", "2001", "active", "8", ""),
        ("3", rel("small.pdf"), "small.pdf", "pdf", "Tiny", "Author", "2002", "active", "11", ""),
        ("4", str(tmp / "files" / "ghost.pdf"), "ghost.pdf", "pdf", "Ghost", "A", "2003", "active", "0", ""),
        ("5", rel("note.md"), "note.md", "pdf", "Note", "A", "2004", "active", "20000", ""),
    ]
    if with_dups:
        rows += [
            ("10", rel("b.pdf"), "b.pdf", "pdf", "Book", "Author", "2000", "active", "20009", sha_b),
            ("9", rel("c.pdf"), "c.pdf", "pdf", "book", "author", "2000", "active", "20009", sha_c),
            ("7", rel("d.pdf"), "d.pdf", "pdf", "Delta", "D", "1999", "active", "20009", sha_d),
            ("11", rel("e.pdf"), "e.pdf", "pdf", "Echo", "E", "1998", "active", "20009", sha_e),
        ]
    con.executemany('INSERT INTO "references" VALUES (?,?,?,?,?,?,?,?,?,?)', rows)
    con.close()

    con = duckdb.connect(str(dbp), read_only=True)
    try:
        dups = identify_duplicates(con)
        errs = identify_errors(con)
    finally:
        con.close()
    return {
        "exact": sum(1 for d in dups if d["reason"] == "exact_duplicate"),
        "fuzzy": sum(1 for d in dups if d["reason"] == "fuzzy_duplicate"),
        "missing": sum(1 for e in errs if e["reason"] == "missing_file"),
        "corrupted": sum(1 for e in errs if e["reason"] == "corrupted"),
        "small": sum(1 for e in errs if e["reason"] == "too_small_review"),
        "md_corrupted": sum(1 for e in errs
                            if e["reason"] == "corrupted" and e["file_path"].endswith(".md")),
        "primary": sorted({d["primary_reference_id"] for d in dups}),
    }


def selftest() -> int:
    tmp = Path(tempfile.mkdtemp(prefix="cleanup_selftest_"))
    try:
        clean = _selftest_case(tmp, with_dups=False)
        dup = _selftest_case(tmp, with_dups=True)
        checks = [
            ("S1 无重复时零误报", (clean["exact"], clean["fuzzy"]), (0, 0)),
            ("S2 精确重复命中 2 组（a/b、d/e）", dup["exact"], 2),
            ("S3 模糊重复命中 1 条", dup["fuzzy"], 1),
            ("S4 主副本取数值最小 id（7 而非 11）", dup["primary"], ["1", "7"]),
            ("S5 缺文件命中 1", clean["missing"], 1),
            ("S6 损坏文件命中 1", clean["corrupted"], 1),
            ("S7 过小仅标记复核 1", clean["small"], 1),
            ("S8 .md 摘要不被判坏（format 标 pdf 亦不误判）", clean["md_corrupted"], 0),
        ]
        bad = 0
        for name, got, want in checks:
            ok = got == want
            print("  [{}] {}（got={!r} want={!r}）".format("PASS" if ok else "FAIL", name, got, want))
            bad += 0 if ok else 1
        print("cleanup_duplicates_and_errors --selftest：{}".format(
            "全部 PASS" if bad == 0 else "{} 项 FAIL".format(bad)))
        return 0 if bad == 0 else 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    parser = argparse.ArgumentParser(description="重复与错误文档清理（DuckDB 主存储层）")
    parser.add_argument("--execute", action="store_true", help="执行删除（默认仅生成清单，删除不可逆）")
    parser.add_argument("--sample-only", action="store_true", help="仅打印抽样复核条目")
    parser.add_argument("--db", default=str(DB_PATH), help="目标库路径（默认 references_fulltext.duckdb）")
    parser.add_argument("--selftest", action="store_true", help="判据非空自检（临时库夹具）")
    args = parser.parse_args()

    if args.selftest:
        sys.exit(selftest())

    ensure_log_dir()
    db = Path(args.db)
    if not db.exists():
        print("[ABORT] 目标库不存在：{}".format(db))
        sys.exit(2)

    con = duckdb.connect(str(db), read_only=not args.execute)

    print("=" * 70)
    print("步骤 1：识别重复与错误文件")
    print("=" * 70)
    duplicates = identify_duplicates(con)
    errors = identify_errors(con)
    print("重复文件数: {}（exact={}, fuzzy={}）".format(
        len(duplicates), sum(1 for d in duplicates if d["reason"] == "exact_duplicate"),
        sum(1 for d in duplicates if d["reason"] == "fuzzy_duplicate")))
    print("错误文件数: {}".format(len(errors)))
    for e in errors:
        print("  id={} reason={} path={}".format(e["reference_id"], e["reason"], e["file_path"]))

    print()
    print("=" * 70)
    print("步骤 2：生成待删除清单")
    print("=" * 70)
    auto_count, review_count = generate_pending_list(duplicates, errors)
    print("自动删除条目数: {}".format(auto_count))
    print("人工复核条目数: {}".format(review_count))
    print("清单文件: {}".format(PENDING_FILE))

    if args.sample_only:
        print()
        print("=" * 70)
        print("步骤 3：人工抽样复核（每 10 条抽 1 条）")
        print("=" * 70)
        all_items = duplicates + [e for e in errors if e["reason"] != "too_small_review"]
        for i, item in enumerate(all_items[::10], 1):
            print("  [{}] id={} reason={} primary={}".format(
                i, item["reference_id"], item["reason"], item.get("primary_reference_id", 0)))
            print("       title={}".format(item.get("title", "")[:60]))
            print("       path={}".format(item["file_path"]))
        con.close()
        return

    if not args.execute:
        print()
        print("（仅识别模式，未执行删除。使用 --execute 执行删除，--sample-only 查看抽样）")
        update_dashboard({
            "pending_delete": auto_count,
            "pending_review": review_count,
            "deleted": 0,
            "failed": 0,
            "primary_kept": len({d["primary_reference_id"] for d in duplicates
                                 if d["reason"] in ("exact_duplicate", "fuzzy_duplicate")}),
        })
        con.close()
        return

    print()
    print("=" * 70)
    print("步骤 3-7：执行删除、数据库更新、日志记录、看板更新")
    print("=" * 70)
    auto_items = []
    with open(PENDING_FILE, "r", encoding="utf-8") as f:
        for line in f:
            item = json.loads(line)
            if item.get("action") == "delete":
                auto_items.append(item)

    deleted_count = 0
    failed_count = 0
    primary_ids = set()
    for item in auto_items:
        if item["reason"] in ("exact_duplicate", "fuzzy_duplicate"):
            primary_ids.add(item["primary_reference_id"])
        success, msg = execute_deletion(con, item)
        log_deletion(item, success, msg)
        if success:
            deleted_count += 1
            print("  [OK] id={} reason={} - {}".format(item["reference_id"], item["reason"], msg))
        else:
            failed_count += 1
            print("  [FAIL] id={} reason={} - {}".format(item["reference_id"], item["reason"], msg))

    print()
    print("删除完成: 成功 {}, 失败 {}".format(deleted_count, failed_count))
    print("保留主副本数: {}".format(len(primary_ids)))

    update_dashboard({
        "pending_delete": auto_count,
        "pending_review": review_count,
        "deleted": deleted_count,
        "failed": failed_count,
        "primary_kept": len(primary_ids),
    })
    print("看板已更新: {}".format(DASHBOARD_FILE))
    con.close()
    print()
    print("=" * 70)
    print("清理完成")
    print("=" * 70)


if __name__ == "__main__":
    main()
