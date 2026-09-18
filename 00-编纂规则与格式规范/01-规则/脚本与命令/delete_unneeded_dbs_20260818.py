# -*- coding: utf-8 -*-
"""按“删除安全规范”执行不需要数据库的删除：
预览 → 备份（gzip+sha256）→ 备份完整性验证 → 删除 → 删除后复核。

复核结论（2026-08-18 会话全量复核）：
  1. script/_msg_date_index.db（583.5MB）——邮件入库期跨库日期缓存；已实测 6 个邮件库 messages 表
     均内建 date/date_local/year/month 列，缓存冗余；仅被历史一次性脚本 _mail_normalize_utc.py 引用，
     可由邮件库重建。
  2. script/backup_cross_indexes_20260815.db（2.3MB）——旧备份，已被 12-数据库备份/cross_indexes/
     轮换体系（20260818_023250.db.gz）取代。
  3. script/poc_dragonfly.duckdb（130.8MB）——DuckDB PoC 产物；正式镜像已建于
     03-原始史料库/01-代码仓库史料/05-DragonFlyBSD/db/duckdb/dragonfly.duckdb（133.3MB，校验一致）。
  4. script/_qa_tmp_20260814/_ddl_selftest_tmp*.db（5 个，~1.2MB）——DDL 自测临时库。
保留：earscribe_profile 浏览器缓存（BSD Now 转写工具活动 profile）、12-数据库备份/ 全部（规则保护）、
  duckdb/ 正式镜像（当日建成并校验）、全部生产库。
"""
import datetime
import gzip
import hashlib
import json
import os
import shutil
import sqlite3
import sys

BASE = r"d:\librebsd"
LOG_DIR = os.path.join(BASE, "script", "_folder_db_logs")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
PREVIEW_MD = os.path.join(LOG_DIR, f"deletion_preview_{TS}.md")
BACKUP_DIR = os.path.join(LOG_DIR, f"deletion_backup_{TS}")
CHANGELOG = os.path.join(BASE, "01-项目管理", "00-变更记录", "changelog.db")

TARGETS = [
    os.path.join(BASE, "script", "_msg_date_index.db"),
    os.path.join(BASE, "script", "backup_cross_indexes_20260815.db"),
    os.path.join(BASE, "script", "poc_dragonfly.duckdb"),
    os.path.join(BASE, "script", "_qa_tmp_20260814", "_ddl_selftest_tmp_1786465586.db"),
    os.path.join(BASE, "script", "_qa_tmp_20260814", "_ddl_selftest_tmp_1786464963.db"),
    os.path.join(BASE, "script", "_qa_tmp_20260814", "_ddl_selftest_tmp_1786464861.db"),
    os.path.join(BASE, "script", "_qa_tmp_20260814", "_ddl_selftest_tmp_1786464743.db"),
    os.path.join(BASE, "script", "_qa_tmp_20260814", "_ddl_selftest_tmp.db"),
]

REASONS = {
    "_msg_date_index.db": "邮件日期缓存冗余（messages 表内建日期列，可重建，仅历史一次性脚本引用）",
    "backup_cross_indexes_20260815.db": "旧备份，已被 12-数据库备份/cross_indexes/ 轮换体系取代",
    "poc_dragonfly.duckdb": "PoC 产物，正式镜像已建成并校验一致",
    "_ddl_selftest_tmp": "DDL 自测临时库",
}


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def reason_of(path):
    for key, r in REASONS.items():
        if key in path:
            return r
    return ""


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    os.makedirs(LOG_DIR, exist_ok=True)
    os.makedirs(BACKUP_DIR, exist_ok=True)

    # 步骤 1：删除前预览（含大小、sha256、删除理由）
    rows = []
    for p in TARGETS:
        if not os.path.exists(p):
            print(f"[缺失跳过] {p}")
            continue
        rows.append({"path": os.path.relpath(p, BASE), "size": os.path.getsize(p),
                     "sha256": sha256_of(p), "reason": reason_of(p)})
    total = sum(r["size"] for r in rows)
    with open(PREVIEW_MD, "w", encoding="utf-8", newline="\n") as f:
        f.write(f"# 不需要数据库删除预览（{TS}）\n\n共 {len(rows)} 个文件，合计 {total/1048576:.1f} MB\n\n")
        f.write("| 文件 | 大小MB | sha256 | 删除理由 |\n| --- | --- | --- | --- |\n")
        for r in rows:
            f.write(f"| {r['path']} | {r['size']/1048576:.1f} | {r['sha256'][:16]}… | {r['reason']} |\n")
        f.write("\n保留：earscribe_profile（活动转写工具）、12-数据库备份/ 全部、duckdb/ 正式镜像、全部生产库。\n")
    print(f"[预览] {len(rows)} 个文件 {total/1048576:.1f}MB -> {os.path.basename(PREVIEW_MD)}")

    # 步骤 2：预览确认（核验清单与复核结论一致：全部为缓存/旧备份/PoC/临时，无生产库）
    assert all(("script" in r["path"]) for r in rows), "越界：含 script/ 外对象"
    assert not any(("12-数据库备份" in r["path"]) for r in rows), "越界：含受保护备份"

    # 步骤 3：删除前备份（gzip 压缩，逐文件 CRC 回读校验）
    manifest = []
    for r in rows:
        src = os.path.join(BASE, r["path"])
        gz = os.path.join(BACKUP_DIR, os.path.basename(src) + ".gz")
        with open(src, "rb") as f_in, gzip.open(gz, "wb", compresslevel=6) as f_out:
            shutil.copyfileobj(f_in, f_out, 1 << 20)
        with gzip.open(gz, "rb") as f:  # CRC 校验
            while f.read(1 << 20):
                pass
        manifest.append({**r, "backup_gz": os.path.basename(gz),
                         "gz_size": os.path.getsize(gz), "gz_sha256": sha256_of(gz)})
    with open(os.path.join(BACKUP_DIR, "manifest.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    # 步骤 4：备份完整性验证（数量 + 解压内容 sha256 比对）
    assert len(manifest) == len(rows), "备份数量不符"
    for m in manifest:
        src = os.path.join(BASE, m["path"])
        with gzip.open(os.path.join(BACKUP_DIR, m["backup_gz"]), "rb") as f:
            h = hashlib.sha256()
            while True:
                chunk = f.read(1 << 20)
                if not chunk:
                    break
                h.update(chunk)
        assert h.hexdigest() == m["sha256"], f"备份内容不符: {m['path']}"
    print(f"[备份] {len(manifest)} 个文件 gzip+sha256 验证通过 -> {os.path.basename(BACKUP_DIR)}")

    # 步骤 5：执行删除（逐个删除+核验）
    for m in manifest:
        p = os.path.join(BASE, m["path"])
        os.remove(p)
        assert not os.path.exists(p), f"删除失败: {p}"
        print(f"[删除] {m['path']}")

    # 步骤 6：删除后复核（对象全删、生产库可开、活动库正常）
    for m in manifest:
        assert not os.path.exists(os.path.join(BASE, m["path"]))
    for probe in (r"04-现代研究文献\research_notes.db", r"04-现代研究文献\historical_claims.db",
                  r"04-现代研究文献\05-参考文献全文数据库\references_fulltext.db",
                  r"10-交叉索引\cross_indexes.db"):
        con = sqlite3.connect(f"file:{os.path.join(BASE, probe)}?mode=ro", uri=True)
        con.execute("SELECT count(*) FROM sqlite_master").fetchone()
        con.close()
    print("[复核] 待删对象全部清除；4 个生产库打开正常")

    # changelog 登记
    con = sqlite3.connect(CHANGELOG)
    cur = con.cursor()
    nxt = cur.execute("SELECT IFNULL(MAX(entry_order),0)+1 FROM entries WHERE date='2026-08-18'").fetchone()[0]
    cur.execute(
        "INSERT INTO entries(date,entry_order,summary,content,created_at) VALUES(?,?,?,?,?)",
        ("2026-08-18", nxt, "按删除安全规范清除不需要的数据库 8 个（释放 717.8MB，备份留存 script/_folder_db_logs/deletion_backup_" + TS + "/）",
         "全量复核后判定：_msg_date_index.db（583.5MB，邮件日期缓存冗余，messages 表内建日期列，仅历史一次性脚本引用可重建）、"
         "backup_cross_indexes_20260815.db（2.3MB，被 12-数据库备份轮换体系取代）、poc_dragonfly.duckdb（130.8MB，PoC 产物，"
         "正式镜像已建成校验）、_qa_tmp_20260814 DDL 自测临时库 5 个。执行五步安全流程：预览（deletion_preview_" + TS + ".md）"
         "→ gzip 备份+sha256 验证 → 逐个删除 → 删除后复核（生产库打开正常）。保留：earscribe_profile（活动转写工具）、"
         "12-数据库备份/ 全部、duckdb/ 正式镜像、全部生产库。",
         datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    con.commit()
    rid = cur.execute("SELECT id FROM entries ORDER BY id DESC LIMIT 1").fetchone()[0]
    con.close()
    gz_total = sum(m["gz_size"] for m in manifest)
    print(f"[changelog] id={rid} 已登记")
    print(f"\n完成：删除 {len(manifest)} 个文件，释放 {total/1048576:.1f}MB；备份压缩态 {gz_total/1048576:.1f}MB 留存")


if __name__ == "__main__":
    main()
