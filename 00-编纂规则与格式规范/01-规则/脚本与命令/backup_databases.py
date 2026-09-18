# -*- coding: utf-8 -*-
"""数据库常设备份与轮换脚本（固定脚本）——DuckDB 适配版（2026-08-25 修订）

规则来源：00-编纂规则与格式规范/01-规则/流程规则.md“数据库备份保留规则（2026-08-18 新增）”
用途：对范围内 DuckDB 数据库执行导出备份，并按“当次/1日/2日/3日/7日”5 槽轮换保留。

2026-08-25 修订：全项目已升格为 DuckDB 主存储层，SQLite 原库以 ARCHIVE_FINAL 归档。
本脚本从 SQLite 在线备份（sqlite3.backup()）改为 DuckDB 导出备份（EXPORT DATABASE 到 Parquet）。
2026-08-26 修订：播客两库（bsdnow_podcast/bsd_podcasts_external）拆分为 10 个按播客实际名独立的 DuckDB
（bsd-now/bsdtalk/youtube/software-engineering-daily/the-changelog/floss-weekly/nerding-out-with-victor/
freebsd-fridays/bsd-conferences-youtube/freebsd-office-hours），SCOPE 相应更新，库计数由 16 调至 24。

用法：
  python backup_databases.py --all          # 全量备份 + 轮换
  python backup_databases.py --db cross_indexes   # 单库备份 + 轮换
  python backup_databases.py --prune-only   # 仅执行轮换清理（不新增备份）
  python backup_databases.py --list         # 查看各库备份现状
"""
import argparse
import datetime
import hashlib
import json
import os
import gzip
import shutil
import sys
import tarfile
import tempfile

try:
    import duckdb
except ImportError:
    print("错误：需要安装 duckdb（pip install duckdb）")
    sys.exit(1)

BASE = r"d:\librebsd"
BACKUP_ROOT = os.path.join(BASE, "12-数据库备份")
LOG_JSONL = os.path.join(BACKUP_ROOT, "backup_log.jsonl")
PRUNE_PREVIEW = os.path.join(BACKUP_ROOT, "prune_preview_latest.json")

# 备份范围：16 个非邮件正式库（2026-08-25 全部 DuckDB 格式）
SCOPE = {
    "changelog": r"01-项目管理\00-变更记录\changelog.duckdb",
    "sacred_sources": r"02-sacred源材料\sacred_sources.duckdb",
    "phoronix_news": r"03-原始史料库\01-代码仓库史料\01-数据库本体\phoronix_news.duckdb",
    "资料数据库": r"03-原始史料库\01-代码仓库史料\01-数据库本体\资料数据库.duckdb",
    # 播客史料按实际播客名逐一独立 DuckDB（2026-08-26 拆分，替代原 bsdnow_podcast / bsd_podcasts_external 两合成库）
    "bsdnow": r"03-原始史料库\14-播客史料\bsd-now.duckdb",
    "bsdtalk": r"03-原始史料库\14-播客史料\bsdtalk.duckdb",
    "software-engineering-daily": r"03-原始史料库\14-播客史料\software-engineering-daily.duckdb",
    "the-changelog": r"03-原始史料库\14-播客史料\the-changelog.duckdb",
    "floss-weekly": r"03-原始史料库\14-播客史料\floss-weekly.duckdb",
    "nerding-out-with-victor": r"03-原始史料库\14-播客史料\nerding-out-with-victor.duckdb",
    "freebsd-fridays": r"03-原始史料库\14-播客史料\freebsd-fridays.duckdb",
    "bsd-conferences-youtube": r"03-原始史料库\14-播客史料\bsd-conferences-youtube.duckdb",
    "freebsd-office-hours": r"03-原始史料库\14-播客史料\freebsd-office-hours.duckdb",
    "youtube": r"03-原始史料库\14-播客史料\youtube.duckdb",
    "original_sources": r"03-原始史料库\original_sources.duckdb",
    "research_notes": r"04-现代研究文献\research_notes.duckdb",
    "historical_claims": r"04-现代研究文献\historical_claims.duckdb",
    "causal_graph": r"04-现代研究文献\causal_graph.duckdb",
    "references_fulltext": r"04-现代研究文献\05-参考文献全文数据库\references_fulltext.duckdb",
    "doubts_standalone": r"04-现代研究文献\06-存疑数据库\doubts_standalone.duckdb",
    "fact_checks": r"07-事实核查记录\fact_checks.duckdb",
    "review_reports": r"08-核查报告与多轮复核\review_reports.duckdb",
    "cross_indexes": r"10-交叉索引\cross_indexes.duckdb",
    "metadata_interfaces": r"11-元数据接口\metadata_interfaces.duckdb",
}

# 轮换槽位（日）
SLOT_DAYS = [1, 2, 3, 7]


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def backup_one(name, rel_path):
    src_path = os.path.join(BASE, rel_path)
    if not os.path.exists(src_path):
        print("[跳过] 源不存在: {}".format(name))
        return None
    db_dir = os.path.join(BACKUP_ROOT, name)
    os.makedirs(db_dir, exist_ok=True)
    stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    tmpdir = tempfile.mkdtemp(prefix="duckdb_bak_")
    integrity = "ok"
    try:
        con = duckdb.connect(src_path, read_only=True)
        # DuckDB 无 PRAGMA integrity_check；用表计数 + CHECKPOINT 作为基本健康检查
        con.execute("CHECKPOINT")
        table_count = con.execute(
            "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema='main'"
        ).fetchone()[0]
        con.execute("EXPORT DATABASE '{}' (FORMAT PARQUET)".format(tmpdir.replace("\\", "/")))
        con.close()

        # 验证导出：检查 parquet 文件数是否与表数一致
        exported_files = []
        for root, dirs, files in os.walk(tmpdir):
            for f in files:
                if f.endswith(".parquet"):
                    exported_files.append(os.path.join(root, f))
        if len(exported_files) < table_count:
            integrity = "export_incomplete: {}/{} tables".format(len(exported_files), table_count)

        tar_path = os.path.join(db_dir, stamp + ".tar")
        with tarfile.open(tar_path, "w") as tar:
            for root, dirs, files in os.walk(tmpdir):
                for f in files:
                    fp = os.path.join(root, f)
                    arcname = os.path.relpath(fp, tmpdir)
                    tar.add(fp, arcname=arcname)

        gz_path = os.path.join(db_dir, stamp + ".duckdb.gz")
        with open(tar_path, "rb") as f_in, gzip.open(gz_path, "wb", compresslevel=6) as f_out:
            shutil.copyfileobj(f_in, f_out, 1 << 20)
        os.remove(tar_path)

        manifest = {
            "db_name": name,
            "source_path": rel_path,
            "backup_file": stamp + ".duckdb.gz",
            "timestamp": stamp,
            "size_bytes": os.path.getsize(src_path),
            "compressed_size_bytes": os.path.getsize(gz_path),
            "table_count": table_count,
            "sha256": sha256_of(src_path),
            "integrity": integrity,
        }
    except Exception as e:
        integrity = "export_failed: {}".format(str(e)[:100])
        manifest = {
            "db_name": name,
            "source_path": rel_path,
            "backup_file": None,
            "timestamp": stamp,
            "size_bytes": os.path.getsize(src_path),
            "compressed_size_bytes": 0,
            "sha256": sha256_of(src_path) if os.path.exists(src_path) else "",
            "integrity": integrity,
        }
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)

    with open(os.path.join(db_dir, stamp + ".json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    with open(LOG_JSONL, "a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps({"op": "backup", **manifest}, ensure_ascii=False) + "\n")
    status = "ok" if str(integrity) == "ok" else "INTEGRITY_FAIL"
    print("[备份] {} -> {} ({:.1f}MB -> gz {:.1f}MB, integrity={})".format(
        name, manifest["backup_file"],
        manifest["size_bytes"] / 1048576, manifest["compressed_size_bytes"] / 1048576, status))
    return manifest


def parse_stamp(fname):
    base = fname
    for suffix in (".duckdb.gz", ".duckdb", ".db.gz", ".db"):
        if base.endswith(suffix):
            base = base[: -len(suffix)]
            break
    try:
        return datetime.datetime.strptime(base, "%Y%m%d_%H%M%S")
    except ValueError:
        return None


def prune_one(name, now):
    db_dir = os.path.join(BACKUP_ROOT, name)
    if not os.path.isdir(db_dir):
        return [], []
    files = [f for f in os.listdir(db_dir)
             if f.endswith(".duckdb.gz") or f.endswith(".db.gz") or f.endswith(".duckdb") or f.endswith(".db")]
    stamped = []
    for f in files:
        ts = parse_stamp(f)
        if ts:
            stamped.append((ts, f))
    stamped.sort(reverse=True)
    keep = set()
    if stamped:
        keep.add(stamped[0][1])
        for days in SLOT_DAYS:
            for ts, f in stamped:
                if f in keep:
                    continue
                if (now - ts).total_seconds() >= days * 86400:
                    keep.add(f)
                    break
    removed = []
    for ts, f in stamped:
        if f not in keep:
            removed.append(f)
    return sorted(keep), sorted(removed)


def prune_execute(name, removed_files):
    db_dir = os.path.join(BACKUP_ROOT, name)
    for f in removed_files:
        for suffix in (".duckdb.gz", ".db.gz", ".duckdb", ".db"):
            if f.endswith(suffix):
                base = f[:-len(suffix)]
                break
        else:
            continue
        for target in (f, base + ".json"):
            p = os.path.join(db_dir, target)
            if os.path.exists(p):
                os.remove(p)
    if removed_files:
        print("[轮换] {} 清理 {} 份".format(name, len(removed_files)))


def cmd_list():
    now = datetime.datetime.now()
    total = 0
    for name in sorted(SCOPE):
        db_dir = os.path.join(BACKUP_ROOT, name)
        if os.path.isdir(db_dir):
            files = sorted([f for f in os.listdir(db_dir)
                           if f.endswith(".duckdb.gz") or f.endswith(".db.gz") or f.endswith(".duckdb") or f.endswith(".db")])
        else:
            files = []
        size = sum(os.path.getsize(os.path.join(db_dir, f)) for f in files) if files else 0
        total += size
        keep, removed = prune_one(name, now)
        print("{:<24} 备份 {} 份 | {:.1f} MB（压缩态） | 轮换后保留 {} 份".format(
            name, len(files), size / 1048576, len(keep)))
    print("合计 {:.2f} GB（压缩态）".format(total / 1073741824))


def main():
    ap = argparse.ArgumentParser(description="数据库常设备份与轮换（5 槽：当次/1日/2日/3日/7日）——DuckDB 适配版")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--all", action="store_true", help="全部 16 库备份 + 轮换")
    g.add_argument("--db", metavar="<db_name>", help="单库备份 + 轮换")
    g.add_argument("--prune-only", action="store_true", help="仅轮换清理，不新增备份")
    g.add_argument("--list", action="store_true", help="查看各库备份现状")
    args = ap.parse_args()

    os.makedirs(BACKUP_ROOT, exist_ok=True)
    now = datetime.datetime.now()

    if args.list:
        cmd_list()
        return 0

    targets = []
    if args.all:
        targets = list(SCOPE.keys())
    elif args.db:
        if args.db not in SCOPE:
            print("未知库名: {}（可用：{}）".format(args.db, ", ".join(SCOPE)))
            return 1
        targets = [args.db]

    done = []
    for name in targets:
        m = backup_one(name, SCOPE[name])
        if m:
            done.append(m)

    preview = {"generated_at": now.isoformat(), "prune": {}}
    for name in sorted(SCOPE):
        keep, removed = prune_one(name, now)
        preview["prune"][name] = {"keep": keep, "removed": removed}
        if removed:
            prune_execute(name, removed)
    with open(PRUNE_PREVIEW, "w", encoding="utf-8", newline="\n") as f:
        json.dump(preview, f, ensure_ascii=False, indent=2)

    bad = [m for m in done if m["integrity"] != "ok"]
    print("完成：备份 {} 库，integrity 异常 {} 库；轮换预览见 {}".format(len(done), len(bad), os.path.basename(PRUNE_PREVIEW)))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())