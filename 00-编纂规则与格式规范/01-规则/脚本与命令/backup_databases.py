# -*- coding: utf-8 -*-
"""数据库常设备份与轮换脚本（固定脚本）——DuckDB 适配版（2026-08-25 修订）

规则来源：00-编纂规则与格式规范/01-规则/流程规则.md“数据库备份保留规则（2026-08-18 新增）”
用途：对范围内 DuckDB 数据库执行导出备份并轮换保留。现行策略为「密槽＋日槽」
（DEFAULT_DENSE / DENSE_POLICY，见下方常量块）；原「当次/1日/2日/3日/7日」5 槽
已于 2026-10-14 废止（见本文件「②二次令」与常量块注释）。

2026-08-25 修订：全项目已升格为 DuckDB 主存储层，SQLite 原库以 ARCHIVE_FINAL 归档。
本脚本从 SQLite 在线备份（sqlite3.backup()）改为 DuckDB 导出备份（EXPORT DATABASE 到 Parquet）。
2026-08-26 修订：播客两库（bsdnow_podcast/bsd_podcasts_external）拆分为 10 个按播客实际名独立的 DuckDB
（bsd-now/bsdtalk/youtube/software-engineering-daily/the-changelog/floss-weekly/nerding-out-with-victor/
freebsd-fridays/bsd-conferences-youtube/freebsd-office-hours），SCOPE 相应更新，库计数由 16 调至 24。
2026-10-14 修订（主理人令，historical_claims 广播事故次日）：启用**强化策略**——
①historical_claims 专项（任务 `librebsd-hc-backup-30min` 每 30 分钟触发）；
②二次令：**全部库统一并入强化策略**（密槽＝最近 24 小时按 30 分钟粒度逐份保留 ≤48 份；
日槽＝1/2/3/4/7/15 日各保留最新一份 ≤6 份；合计 ≤54 份），由任务 `librebsd-dball-backup-30min`
每 30 分钟执行 `--all`；轮换参数见 `DEFAULT_DENSE`／`DENSE_POLICY`。原 5 槽（当次/1/2/3/7 日）
机制废止（2026-08-18 立、2026-10-14 升级）。单套全库 gz 实测约 854MB、全程约 90 秒；
historical_claims 单份约 210.6MB。
③三次令（备份范围裁剪，2026-10-14）：**播客库 10 个自 SCOPE 移除，不纳入备份**（原文物可再生成，
无需常备防护）；**邮件列表库（261 分库）与新闻组库（usenet_mail）确认排除**（本不在范围）；
**references_fulltext 全文数据库保留常备**。裁剪后范围＝14 功能/史料库 + 12 代码仓库库 = 26 库。
详见流程规则「数据库备份保留规则」小节。
④四次裁定（2026-10-14，主理人令「A」）：**historical_claims 由专项任务独担**——`--all` 备份循环
跳过该库（`ALL_SKIP`），消除与 `librebsd-hc-backup-30min` 的重复备份；dball 实轮转 25 库 + hc 专项 1 库；
轮换（prune）维持全库收尾（幂等）。另：三任务执行程序已改 **pythonw.exe**（无窗口后台，2026-10-14 主理人令）——
std 流为空时自动重定向至 `12-数据库备份/backup_console.log`。
⑤五次令（2026-10-14）：**桌面执行日志**——每次运行向 `桌面/数据库备份.txt` 追加一行成功/失败记录
（`record_run_log`），滚动保留 15 日、超期自动清除；写入失败不影响主流程。

2026-10-15 修订（主理人令）：三任务触发频次由每 30 分钟统一调整为每 5 小时（任务名、错峰相位、轮换与日志机制均不变；调度频次以本行为最新基准）。
⑥六次令（2026-10-15，主理人授权）：**归档体级完整性校验**——`backup_one()` 走 `EXPORT DATABASE (FORMAT PARQUET)` → tar → gzip 存成 `<stamp>.duckdb.gz`，归档体并非 DuckDB 文件，而旧 `integrity` 只比对「导出 parquet 件数 vs 源表数」、**从不打开归档体**，传输截断／写盘中断一律记 `ok`（2026-10-14 实测 16 槽整数 MiB 截断、sidecar 全记 ok）。现补 `verify_archive()` 三段校验（解 gzip 读到 EOF 触发 CRC → 读 tar 核表数 → 逐个 parquet 用 DuckDB 加载并计数），失败即把 `integrity` 改判为 `archive_open_failed`／`archive_incomplete`／`archive_unreadable` 并随 `record_run_log` 落到桌面执行日志；manifest 另记 `archive_format`、`archive_verified`、`archive_detail`。备份格式／`BASE`／调度／轮换均未改。差分对照 6/6 命中：同流程合成好档 PASS；gzip-非-tar、表数错配、**真实归档件截到整数 MiB 边界**、尾删 1 字节全部 FAIL。2026-10-15 实查 `historical_claims/` 25 份归档**全部 PASS**（179.0～210.6 MB／34 表），10-14「备份槽全坏」系当时所见、无法复盘。

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

BASE_CANDIDATES = (r"D:\librebsd", r"\\DESKTOP-M5P610N\d\librebsd")


def _resolve_base():
    """仓库根解析：D: 盘符优先，UNC 别名回落；两者皆不可达则回 None。

    教训（2026-10-15 复核坐实）：原先硬编码 d:\\librebsd，盘符未映射时下方
    makedirs(BACKUP_ROOT) 抛 FileNotFoundError，计划任务（pythonw.exe 无窗口）
    不留任何痕迹——备份静默停摆。
    """
    for c in BASE_CANDIDATES:
        if os.path.isdir(c):
            return c
    return None


BASE = _resolve_base()
BACKUP_ROOT = os.path.join(BASE, "12-数据库备份") if BASE else None
LOG_JSONL = os.path.join(BACKUP_ROOT, "backup_log.jsonl") if BASE else None
PRUNE_PREVIEW = os.path.join(BACKUP_ROOT, "prune_preview_latest.json") if BASE else None


def set_base(path):
    """显式指定仓库根（--base）。"""
    g = globals()
    g["BASE"] = path
    g["BACKUP_ROOT"] = os.path.join(path, "12-数据库备份")
    g["LOG_JSONL"] = os.path.join(g["BACKUP_ROOT"], "backup_log.jsonl")
    g["PRUNE_PREVIEW"] = os.path.join(g["BACKUP_ROOT"], "prune_preview_latest.json")

# 2026-10-14：适配计划任务无窗口后台运行（pythonw.exe）——std 流为空时重定向至控制台日志
if (sys.stdout is None or sys.stderr is None) and BASE:
    os.makedirs(BACKUP_ROOT, exist_ok=True)
    _con = open(os.path.join(BACKUP_ROOT, "backup_console.log"), "a", encoding="utf-8", buffering=1)
    if sys.stdout is None:
        sys.stdout = _con
    if sys.stderr is None:
        sys.stderr = _con

# 备份范围：14 个功能/史料正式库 + 12 个代码仓库库 = 26 库
# （2026-10-14 三次令裁剪：播客 10 库移出；邮件列表库/新闻组库本不在范围；references_fulltext 全文数据库保留）
# （2026-10-14 裁定 A：--all 备份循环跳过 historical_claims（ALL_SKIP）——该库由 hc 专项任务独担）
SCOPE = {
    "changelog": r"01-项目管理\00-变更记录\changelog.duckdb",
    "sacred_sources": r"02-sacred源材料\sacred_sources.duckdb",
    "phoronix_news": r"03-原始史料库\01-代码仓库史料\01-数据库本体\phoronix_news.duckdb",
    "资料数据库": r"03-原始史料库\01-代码仓库史料\01-数据库本体\资料数据库.duckdb",
    # 播客史料 10 库（bsd-now/bsdtalk/software-engineering-daily/the-changelog/floss-weekly/
    # nerding-out-with-victor/freebsd-fridays/bsd-conferences-youtube/freebsd-office-hours/youtube）
    # ——2026-10-14 主理人令（三次令）：**不纳入备份范围**，自 SCOPE 移除（原 2026-08-26 拆分并入）。
    # 同步排除（确认）：邮件列表库（261 分库）与新闻组库 usenet_mail 本不在范围；references_fulltext 保留。
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
    # 代码仓库史料库（2026-10-14 并入；体量大，采用轻槽策略——见 DENSE_POLICY）
    "freebsd": r"03-原始史料库\01-代码仓库史料\02-FreeBSD\db\duckdb\freebsd.duckdb",
    "netbsd": r"03-原始史料库\01-代码仓库史料\03-NetBSD\db\duckdb\netbsd.duckdb",
    "openbsd": r"03-原始史料库\01-代码仓库史料\04-OpenBSD\db\duckdb\openbsd.duckdb",
    "dragonfly": r"03-原始史料库\01-代码仓库史料\05-DragonFlyBSD\db\duckdb\dragonfly.duckdb",
    "openzfs": r"03-原始史料库\01-代码仓库史料\06-OpenZFS\db\duckdb\openzfs.duckdb",
    "bsd-derivatives": r"03-原始史料库\01-代码仓库史料\07-BSD衍生项目\db\duckdb\bsd-derivatives.duckdb",
    "cross_source_identity": r"03-原始史料库\01-代码仓库史料\08-跨项目对比\db\duckdb\cross_source_identity.duckdb",
    "illumos-gate": r"03-原始史料库\01-代码仓库史料\08-跨项目对比\db\duckdb\illumos-gate.duckdb",
    "openssh-apple": r"03-原始史料库\01-代码仓库史料\08-跨项目对比\db\duckdb\openssh-apple.duckdb",
    "openssh": r"03-原始史料库\01-代码仓库史料\08-跨项目对比\db\duckdb\openssh.duckdb",
    "darwin": r"03-原始史料库\01-代码仓库史料\09-Darwin\db\duckdb\darwin.duckdb",
    "linux-kernel": r"03-原始史料库\01-代码仓库史料\10-LinuxKernel\db\duckdb\linux-kernel.duckdb",
}

# 原 5 槽参数（SLOT_DAYS）已于 2026-10-14 废止——全库改走 DEFAULT_DENSE / DENSE_POLICY（密槽＋日槽）

# 强化策略（2026-10-14 主理人令）：全库统一走 DEFAULT_DENSE；DENSE_POLICY 保留库级覆盖位
# 密槽：dense_window_hours 小时内按 dense_minutes 分钟粒度逐份保留；
# 日槽：daily_slots 列出的每个时点各保留「距今 ≥ N 日中的最新一份」；
# 2026-10-14 二次令：全部库并入定时任务（librebsd-dball-backup-30min，每 30 分钟 --all）。
DEFAULT_DENSE = {
    "dense_minutes": 30,
    "dense_window_hours": 24,
    "daily_slots": [1, 2, 3, 4, 7, 15],
}
DENSE_POLICY = {
    "historical_claims": {
        "dense_minutes": 30,
        "dense_window_hours": 24,
        "daily_slots": [1, 2, 3, 4, 7, 15],
    },
}
# 代码仓库库群（12 库，合计 gz 约 2.8GB/套）采用轻槽：无密槽，仅「当次＋1/2/3/4/7/15 日槽」（≤7 份）
for _k in ("freebsd", "netbsd", "openbsd", "dragonfly", "openzfs", "bsd-derivatives",
           "cross_source_identity", "illumos-gate", "openssh-apple", "openssh", "darwin", "linux-kernel"):
    DENSE_POLICY[_k] = {"dense_minutes": 30, "dense_window_hours": 0, "daily_slots": [1, 2, 3, 4, 7, 15]}

# 2026-10-14 主理人裁定 A：historical_claims 由专项任务 librebsd-hc-backup-30min 独担——
# --all 备份循环跳过该库（消除重复备份：此前该库每 ~15 分钟被双任务各备一份）；
# 轮换（prune）维持全库收尾（幂等、按库名取策略，不受本表影响）；--db historical_claims 不受影响。
ALL_SKIP = {"historical_claims"}


def _desktop_log_path():
    """桌面《数据库备份.txt》路径（兼容 OneDrive 桌面重定向）。"""
    home = os.path.expanduser("~")
    for cand in (os.path.join(home, "Desktop"), os.path.join(home, "OneDrive", "Desktop")):
        if os.path.isdir(cand):
            return os.path.join(cand, "数据库备份.txt")
    return os.path.join(home, "Desktop", "数据库备份.txt")


def record_run_log(ok, text):
    """向桌面《数据库备份.txt》追加一条 成功/失败 记录；自动清除超过 15 日的旧记录。
    2026-10-14 主理人令；本函数任何失败均不影响备份主流程。"""
    try:
        p = _desktop_log_path()
        now = datetime.datetime.now()
        kept = []
        if os.path.exists(p):
            with open(p, encoding="utf-8") as f:
                for ln in f.read().split("\n"):
                    ln = ln.strip()
                    if not ln:
                        continue
                    try:
                        t = datetime.datetime.strptime(ln[:19], "%Y-%m-%d %H:%M:%S")
                        if (now - t).total_seconds() <= 15 * 86400:
                            kept.append(ln)
                    except ValueError:
                        kept.append(ln)
        kept.append("{} | {} | {}".format(now.strftime("%Y-%m-%d %H:%M:%S"), "成功" if ok else "失败", text))
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(kept) + "\n")
    except Exception as e:
        try:
            print("[警告] 桌面执行日志写入失败：{}".format(str(e)[:100]))
        except Exception:
            pass


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def verify_archive(gz_path, expect_tables):
    """校验归档体本身（对的是档，不是源库）。

    2026-10-14 实测：historical_claims 的 16 个备份槽解包后全部为整数 MiB
    截断、非有效内容，而 sidecar 一律记 integrity: ok——旧判定只覆盖
    「源库导出是否完整」，从不打开归档体，传输截断／写盘中断因此静默放行。

    归档体是 EXPORT DATABASE 的 Parquet 集打包（gzip + tar），并非 DuckDB
    文件，故按「解 gzip 读到 EOF（CRC 校验）→ 读 tar 成员 → 逐个 parquet
    用 DuckDB 加载并计数」三段校验，任一环节失败即判 archive_* 失败。

    返回 (ok, detail)。
    """
    tmpdir = tempfile.mkdtemp(prefix="duckdb_archchk_")
    try:
        # 阶段一：解 gzip 直到流末尾——截断件在此因 EOF/CRC 报错
        tmp_tar = os.path.join(tmpdir, "members.tar")
        with gzip.open(gz_path, "rb") as gz, open(tmp_tar, "wb") as out:
            shutil.copyfileobj(gz, out, 1 << 20)

        # 阶段二：读 tar 成员，核对表数
        with tarfile.open(tmp_tar, "r:") as tar:
            members = tar.getmembers()
        pq = [m for m in members if m.name.endswith(".parquet") and m.isfile()]
        if len(pq) < expect_tables:
            return False, "archive_incomplete: {}/{} tables".format(len(pq), expect_tables)

        # 阶段三：逐个 parquet 用 DuckDB 只读加载并计数
        dst = os.path.join(tmpdir, "out")
        os.makedirs(dst, exist_ok=True)
        with tarfile.open(tmp_tar, "r:") as tar:
            tar.extractall(dst)
        # 只读连接不能以无路径形式启动内存库，此处只计数、不落文件
        con = duckdb.connect()
        total, bad = 0, 0
        try:
            for root, dirs, files in os.walk(dst):
                for fn in files:
                    if not fn.endswith(".parquet"):
                        continue
                    fp = os.path.join(root, fn).replace("\\", "/")
                    try:
                        total += con.execute(
                            "SELECT COUNT(*) FROM read_parquet('{0}')".format(
                                fp.replace("'", "''"))
                        ).fetchone()[0]
                    except Exception:
                        bad += 1
        finally:
            con.close()
        if bad:
            return False, "archive_unreadable: {} parquet".format(bad)
        return True, "verified: {} tables / {} rows".format(len(pq), total)
    except Exception as e:
        return False, "archive_open_failed: {}".format(str(e)[:80])
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


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
            "archive_format": "parquet-tar-gz",
            "integrity": integrity,
        }
        # 归档体级校验（2026-10-15 补）：旧判定只验源库导出完整性，
        # 从不打开归档体——传输截断／写盘中断曾被记成 integrity: ok
        ok_a, detail_a = verify_archive(gz_path, table_count)
        manifest["archive_verified"] = ok_a
        manifest["archive_detail"] = detail_a
        if not ok_a:
            integrity = detail_a
            manifest["integrity"] = integrity
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
        policy = DENSE_POLICY.get(name, DEFAULT_DENSE)  # 2026-10-14 起全库统一强化策略
        # 密槽：最近 dense_window_hours 内按 dense_minutes 分钟分桶，每桶保留最新一份
        window_start = now - datetime.timedelta(hours=policy["dense_window_hours"])
        buckets = {}
        for ts, f in stamped:
            if ts >= window_start:
                key = int((now - ts).total_seconds() // (policy["dense_minutes"] * 60))
                if key not in buckets:
                    buckets[key] = f
        keep.update(buckets.values())
        # 日槽：daily_slots 各时点保留「距今 ≥ N 日中的最新一份」
        for days in policy["daily_slots"]:
            for ts, f in stamped:
                if f in keep:
                    continue
                if (now - ts).total_seconds() >= days * 86400:
                    keep.add(f)
                    break
        # 当次：最新一份兜底
        keep.add(stamped[0][1])
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
    # 轮换参数已随 2026-10-14 令改走 DEFAULT_DENSE / DENSE_POLICY（密槽＋日槽），
    # 原「5 槽」表述废止——帮助文本随之更正，勿再标已废止策略。
    ap = argparse.ArgumentParser(description="数据库常设备份与轮换（密槽＋日槽，2026-10-14 起；原 5 槽已废止）——DuckDB 适配版")
    ap.add_argument("--base", metavar="<仓库根>",
                    help="显式指定仓库根（默认 D:\\librebsd，回落 UNC 别名；不可达即退出码 2）")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--all", action="store_true", help="全范围备份 + 轮换（跳过 ALL_SKIP：historical_claims 由专项任务独担）")
    g.add_argument("--db", metavar="<db_name>", help="单库备份 + 轮换")
    g.add_argument("--prune-only", action="store_true", help="仅轮换清理，不新增备份")
    g.add_argument("--list", action="store_true", help="查看各库备份现状")
    args = ap.parse_args()

    if args.base:
        if not os.path.isdir(args.base):
            print("[FAIL] --base 不存在：{}".format(args.base))
            return 2
        set_base(args.base)
    if not BASE:
        print("[FAIL] 仓库根不可解析：{} 均不可达".format("、".join(BASE_CANDIDATES)))
        print("       备份禁静默停摆；请先挂载盘符，或用 --base <仓库根> 显式指定。")
        return 2

    os.makedirs(BACKUP_ROOT, exist_ok=True)
    now = datetime.datetime.now()

    if args.list:
        cmd_list()
        return 0

    targets = []
    if args.all:
        targets = [t for t in SCOPE.keys() if t not in ALL_SKIP]
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
    if args.all or args.db:
        mode = "全库任务（{} 库）".format(len(done)) if args.all else "单库任务（{}）".format(args.db)
        if bad:
            detail = "、".join("{}（{}）".format(m["db_name"], str(m["integrity"])[:40]) for m in bad)
            record_run_log(False, "{}：{} 库成功、{} 库异常——{}".format(mode, len(done) - len(bad), len(bad), detail))
        else:
            record_run_log(True, "{}：全部成功".format(mode))
    print("完成：备份 {} 库，integrity 异常 {} 库；轮换预览见 {}".format(len(done), len(bad), os.path.basename(PRUNE_PREVIEW)))
    return 1 if bad else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as e:
        record_run_log(False, "脚本异常终止：{}".format(str(e)[:100]))
        raise