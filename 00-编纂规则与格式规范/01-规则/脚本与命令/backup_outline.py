# -*- coding: utf-8 -*-
"""05-卷册大纲 目录压缩备份与轮换脚本（固定脚本）

规则来源：00-编纂规则与格式规范/01-规则/流程规则.md「数据库备份保留规则」小节
专项强化条目（2026-10-14 主理人令）：05-卷册大纲 目录与 historical_claims 同规则保护——
每 30 分钟一次；保留 24 小时密槽（30 分钟粒度，≤48 份）+ 1/2/3/4/7/15 日槽（各最新一份）；
合计 ≤54 份；tar+gzip 压缩存 12-数据库备份/05-卷册大纲/；日志追加 backup_log.jsonl。

2026-10-15 修订（主理人令）：触发频次由每 30 分钟调整为每 5 小时（任务名、保留策略与其余机制不变；调度频次以本行为最新基准）。

用法：
  python backup_outline.py --backup      # 备份 + 轮换
  python backup_outline.py --prune-only  # 仅轮换清理
  python backup_outline.py --list        # 查看现状
"""
import argparse
import datetime
import gzip
import json
import os
import shutil
import sys
import tarfile
import tempfile

BASE = r"d:\librebsd"
SRC_DIR = os.path.join(BASE, "05-卷册大纲")
BACKUP_ROOT = os.path.join(BASE, "12-数据库备份")
DEST_DIR = os.path.join(BACKUP_ROOT, "05-卷册大纲")
LOG_JSONL = os.path.join(BACKUP_ROOT, "backup_log.jsonl")

# 2026-10-14：适配计划任务无窗口后台运行（pythonw.exe）——std 流为空时重定向至控制台日志
if sys.stdout is None or sys.stderr is None:
    os.makedirs(BACKUP_ROOT, exist_ok=True)
    _con = open(os.path.join(BACKUP_ROOT, "backup_console.log"), "a", encoding="utf-8", buffering=1)
    if sys.stdout is None:
        sys.stdout = _con
    if sys.stderr is None:
        sys.stderr = _con

DENSE_MINUTES = 30
DENSE_WINDOW_HOURS = 24
DAILY_SLOTS = [1, 2, 3, 4, 7, 15]


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


def parse_stamp(fname):
    base = fname
    if base.endswith(".tar.gz"):
        base = base[:-7]
    try:
        return datetime.datetime.strptime(base, "%Y%m%d_%H%M%S")
    except ValueError:
        return None


def scan_stats():
    n = 0
    total = 0
    for root, dirs, files in os.walk(SRC_DIR):
        for f in files:
            n += 1
            try:
                total += os.path.getsize(os.path.join(root, f))
            except OSError:
                pass
    return n, total


def backup_one():
    os.makedirs(DEST_DIR, exist_ok=True)
    stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    gz_path = os.path.join(DEST_DIR, stamp + ".tar.gz")
    integrity = "ok"
    n_files, total_bytes = scan_stats()
    tmp_tar = os.path.join(tempfile.gettempdir(), "outline_bak_{}.tar".format(stamp))
    try:
        with tarfile.open(tmp_tar, "w") as tar:
            tar.add(SRC_DIR, arcname=os.path.basename(SRC_DIR))
        with open(tmp_tar, "rb") as f_in, gzip.open(gz_path, "wb", compresslevel=6) as f_out:
            shutil.copyfileobj(f_in, f_out, 1 << 20)
    except Exception as e:
        integrity = "failed: {}".format(str(e)[:120])
    finally:
        if os.path.exists(tmp_tar):
            os.remove(tmp_tar)
    comp = os.path.getsize(gz_path) if os.path.exists(gz_path) else 0
    manifest = {
        "op": "backup_outline",
        "target": "05-卷册大纲",
        "backup_file": stamp + ".tar.gz" if integrity == "ok" else None,
        "timestamp": stamp,
        "file_count": n_files,
        "size_bytes": total_bytes,
        "compressed_size_bytes": comp,
        "integrity": integrity,
    }
    with open(os.path.join(DEST_DIR, stamp + ".json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    with open(LOG_JSONL, "a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(manifest, ensure_ascii=False) + "\n")
    print("[备份] 05-卷册大纲 -> {} ({} 文件 {:.1f}MB -> gz {:.1f}MB, integrity={})".format(
        manifest["backup_file"], n_files, total_bytes / 1048576, comp / 1048576, integrity))
    return manifest


def prune_one(now):
    if not os.path.isdir(DEST_DIR):
        return [], []
    files = [f for f in os.listdir(DEST_DIR) if f.endswith(".tar.gz")]
    stamped = []
    for f in files:
        ts = parse_stamp(f)
        if ts:
            stamped.append((ts, f))
    stamped.sort(reverse=True)
    keep = set()
    if stamped:
        window_start = now - datetime.timedelta(hours=DENSE_WINDOW_HOURS)
        buckets = {}
        for ts, f in stamped:
            if ts >= window_start:
                key = int((now - ts).total_seconds() // (DENSE_MINUTES * 60))
                if key not in buckets:
                    buckets[key] = f
        keep.update(buckets.values())
        for days in DAILY_SLOTS:
            for ts, f in stamped:
                if f in keep:
                    continue
                if (now - ts).total_seconds() >= days * 86400:
                    keep.add(f)
                    break
        keep.add(stamped[0][1])
    removed = [f for ts, f in stamped if f not in keep]
    return sorted(keep), sorted(removed)


def prune_execute(removed_files):
    for f in removed_files:
        for target in (f, f[:-7] + ".json"):
            p = os.path.join(DEST_DIR, target)
            if os.path.exists(p):
                os.remove(p)
    if removed_files:
        print("[轮换] 05-卷册大纲 清理 {} 份".format(len(removed_files)))


def cmd_list():
    now = datetime.datetime.now()
    files = sorted([f for f in os.listdir(DEST_DIR) if f.endswith(".tar.gz")]) if os.path.isdir(DEST_DIR) else []
    size = sum(os.path.getsize(os.path.join(DEST_DIR, f)) for f in files) if files else 0
    keep, removed = prune_one(now)
    print("05-卷册大纲 备份 {} 份 | {:.1f} MB（压缩态） | 轮换后保留 {} 份".format(len(files), size / 1048576, len(keep)))
    for ts, f in sorted([(parse_stamp(f), f) for f in files], reverse=True)[:60]:
        print("  {} {}".format(ts, f))


def main():
    ap = argparse.ArgumentParser(description="05-卷册大纲 目录压缩备份与轮换（30 分钟密槽 + 1/2/3/4/7/15 日槽）")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--backup", action="store_true", help="备份 + 轮换")
    g.add_argument("--prune-only", action="store_true", help="仅轮换清理")
    g.add_argument("--list", action="store_true", help="查看现状")
    args = ap.parse_args()
    os.makedirs(BACKUP_ROOT, exist_ok=True)
    now = datetime.datetime.now()
    if args.list:
        cmd_list()
        return 0
    if args.backup:
        m = backup_one()
        if m["integrity"] != "ok":
            print("integrity 异常: {}".format(m["integrity"]))
            record_run_log(False, "大纲任务：备份异常——{}".format(str(m["integrity"])[:60]))
        else:
            record_run_log(True, "大纲任务：05-卷册大纲 备份成功（{:.1f}MB）".format(m["compressed_size_bytes"] / 1048576))
    keep, removed = prune_one(now)
    if removed:
        prune_execute(removed)
    print("完成：保留 {} 份".format(len(keep)))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as e:
        record_run_log(False, "脚本异常终止：{}".format(str(e)[:100]))
        raise
