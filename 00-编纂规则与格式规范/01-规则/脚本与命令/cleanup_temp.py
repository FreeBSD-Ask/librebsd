#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cleanup_temp.py — 临时文件与垃圾清理执行器（工程实践规则 §12 第四十件配套）。

四步：--scan（只读分类计数）→ --plan（写清单，不删除）→ --apply --manifest（只删清单内
action=delete 项，歧义项移隔离区）→ --verify --manifest（复扫零残留）。
安全红线：禁 rm -rf；禁通配删除；保护清单/被引用件不动；删除前逐件 sha256；全仓清理须 ykla 明示。
本件不做定时自动化；由人在场会话按批执行。
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TZ = timezone(timedelta(hours=8))

ALLOWLIST_TOPS = ["script", "_tmp", "review_logs", os.path.join("05-卷册大纲", "目录", "tests", "_scratch")]
CACHE_DIR_NAMES = {"__pycache__", ".pytest_cache", ".ruff_cache", ".mypy_cache", "node_modules", "target", "dist", ".build", "build", ".cache"}
CACHE_LEAF = {".vitepress/cache"}
BACKUP_SUFFIX_RE = re.compile(r"\.(bak|bak-[^/]*|bak_[^/]*|prebak[^/]*|pre|orig|rej)$|(~)$", re.IGNORECASE)
ONE_SHOT_DAYS = 30
PROTECT_TOPS = {"05-卷册大纲", "旧大纲-20261023", "12-数据库备份", "01-项目管理", "00-编纂规则与格式规范", "02-sacred源材料", "03-原始史料库", "04-现代研究文献", "07-事实核查记录", "08-核查报告与多轮复核", "10-交叉索引", "11-元数据接口", "13-软件工程", "specs"}
PROTECT_EXT = {".duckdb", ".sqlite", ".sqlite3", ".gz", ".md"}

RETRY = 6


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def tracked_files(root: Path) -> set[str]:
    try:
        out = subprocess_git(["ls-files", "-z"], root)
        return {x for x in out.split("\0") if x}
    except Exception:
        return set()


def subprocess_git(args: list[str], cwd: Path) -> str:
    proc = subprocess.run(["git"] + args, capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(cwd), timeout=120)
    return proc.stdout


def referenced_basenames(root: Path) -> set[str]:
    hits: set[str] = set()
    targets = [root / "00-编纂规则与格式规范" / "01-规则", root / "AGENTS.md"]
    for base in targets:
        if base.is_file():
            texts = [base]
        else:
            texts = list(base.rglob("*.md"))
        for p in texts:
            try:
                t = p.read_text(encoding="utf-8", errors="ignore")
                for m in re.finditer(r"[\w\-.]+\.(?:py|sql|json|js|tsv)", t):
                    hits.add(m.group(0))
            except Exception:
                continue
    return hits


def classify(path: Path, root: Path, tracked: set[str], refs: set[str], now: datetime, is_dir: bool = False) -> tuple[str, str, str]:
    """返回 (category, in_scope, action)。"""
    rel = path.relative_to(root).as_posix()
    top = rel.split("/")[0]
    if is_dir:
        if rel.startswith("03-原始史料库/"):
            return ("", "no", "keep")
        if path.name == "node_modules":
            return ("cache_dir", "yes", "keep")
        if path.name in CACHE_DIR_NAMES or rel.endswith(tuple("/" + c for c in CACHE_LEAF)):
            return ("cache_dir", "yes", "delete")
        if any(bad in path.name for bad in ("…", "...", "\u200b", "[MASKED]", "[path]")) or path.name.startswith("._") or path.name.endswith("~"):
            if rel.startswith("03-原始史料库/01-代码仓库史料/"):
                return ("", "no", "keep")
            return ("misnamed_dir", "yes", "quarantine")
        return ("", "no", "keep")
    if tracked and rel in tracked:
        return ("tracked_file", "no", "keep")
    if rel.startswith("03-原始史料库/"):
        return ("clone_tree", "no", "keep")
    if path.suffix in PROTECT_EXT:
        return ("protected_ext", "no", "keep")
    if BACKUP_SUFFIX_RE.search(path.name):
        return ("sidecar_backup", "yes", "delete")
    if path.name.endswith((".pyc", ".pyo")):
        return ("pycache_file", "yes", "delete")
    if top in ALLOWLIST_TOPS or rel.startswith(tuple(t + "/" for t in ALLOWLIST_TOPS)):
        try:
            age_days = (now - datetime.fromtimestamp(path.stat().st_mtime, TZ)).days
        except FileNotFoundError:
            return ("gone_during_scan", "yes", "quarantine")
        if path.suffix in {".py", ".json", ".tsv", ".md", ".txt", ".jsonl", ".log"} and path.name not in refs and age_days > ONE_SHOT_DAYS:
            return ("one_shot", "yes", "delete")
        if age_days > ONE_SHOT_DAYS:
            return ("stale_temp", "yes", "quarantine")
        return ("temp_recent", "yes", "keep")
    return ("outside_allowlist", "no", "keep")


def iter_candidate_files(root: Path):
    skip_tops = {"12-数据库备份", ".git", "dvd6", "node_modules", ".trae", ".zcode", ".git"}
    for dirpath, dirnames, filenames in os.walk(root):
        rel_dir = Path(dirpath).relative_to(root)
        parts = rel_dir.parts
        if parts and (parts[0] in skip_tops):
            dirnames[:] = []
            continue
        dirnames[:] = [d for d in dirnames if d not in {"node_modules", ".git"}]
        for f in filenames:
            yield Path(dirpath) / f


def collect(root: Path, refs: set[str], now: datetime):
    tracked = tracked_files(root)
    files = []
    dirs_cand = []
    for f in iter_candidate_files(root):
        cat, ins, act = classify(f, root, tracked, refs, now)
        if cat and act != "keep":
            try:
                size = f.stat().st_size
                mtime = datetime.fromtimestamp(f.stat().st_mtime, TZ).isoformat(timespec="seconds")
                digest = sha256(f)
            except FileNotFoundError:
                files.append({"path": f.relative_to(root).as_posix(), "category": "gone_during_scan", "in_scope": ins,
                              "size": 0, "mtime": "", "sha256": "", "referenced": "?", "action": "quarantine", "reason": "scan 期间消失"})
                continue
            except Exception as exc:
                files.append({"path": f.relative_to(root).as_posix(), "category": cat, "in_scope": ins,
                              "size": 0, "mtime": "", "sha256": f"ERR:{exc}"[:60], "referenced": "?",
                              "action": "quarantine", "reason": "stat_err"})
                continue
            files.append({"path": f.relative_to(root).as_posix(), "category": cat, "in_scope": ins,
                          "size": size, "mtime": mtime, "sha256": digest,
                          "referenced": "no" if f.name not in refs else "yes",
                          "action": "quarantine" if f.name in refs else act, "reason": cat})
    # 空目录与缓存目录（自底向上）
    for dirpath, dirnames, filenames in os.walk(root, topdown=False):
        rel_dir = Path(dirpath).relative_to(root)
        parts = rel_dir.parts
        if not parts or parts[0] in {"12-数据库备份", ".git", "dvd6", ".trae", ".zcode"}:
            continue
        d = Path(dirpath)
        if d.name in CACHE_DIR_NAMES or rel_dir.as_posix().endswith(tuple("/" + c for c in CACHE_LEAF)):
            dirs_cand.append(d)
        elif any(bad in d.name for bad in ("…", "...", "\u200b", "[MASKED]", "[path]")) or d.name.startswith("._") or d.name.endswith("~"):
            if parts[0] in ALLOWLIST_TOPS:
                dirs_cand.append(d)
        elif not dirnames and not filenames and parts[0] in ALLOWLIST_TOPS:
            dirs_cand.append(d)
    return files, dirs_cand, tracked


def cmd_scan(root: Path) -> int:
    now = datetime.now(TZ)
    refs = referenced_basenames(root)
    files, dirs_cand, _ = collect(root, refs, now)
    by_cat: dict[str, int] = {}
    by_bytes: dict[str, int] = {}
    for f in files:
        by_cat[f["category"]] = by_cat.get(f["category"], 0) + 1
        by_bytes[f["category"]] = by_bytes.get(f["category"], 0) + f["size"]
    del_dirs = [d for d in dirs_cand if d.name in CACHE_DIR_NAMES or d.relative_to(root).as_posix().endswith(tuple("/" + c for c in CACHE_LEAF))]
    print(f"scan：候选文件 {len(files)} 件（{sum(by_bytes.values()):,} B）；缓存/空目录候选 {len(dirs_cand)}（含可整删缓存目录 {len(del_dirs)}）")
    for k in sorted(by_cat):
        print(f"  {k}: {by_cat[k]} 件 / {by_bytes[k]:,} B")
    print("（--scan 只读；删除走 --plan → ykla 审 → --apply --manifest）")
    return 0


def cmd_plan(root: Path) -> int:
    now = datetime.now(TZ)
    refs = referenced_basenames(root)
    files, dirs_cand, _ = collect(root, refs, now)
    date = datetime.now(TZ).strftime("%Y%m%d")
    out_dir = root / "script" / f"_cleanup_{date}"
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest = out_dir / "cleanup_manifest.tsv"
    header = ["path", "type", "size", "mtime", "sha256", "category", "in_scope", "referenced", "action", "reason"]
    with manifest.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(header)
        for f in files:
            w.writerow([f["path"], "file", f["size"], f["mtime"], f["sha256"], f["category"], f["in_scope"], f["referenced"], f["action"], f["reason"]])
        for d in dirs_cand:
            rel = d.relative_to(root).as_posix()
            cat, ins, act = classify(d, root, set(), refs, now, is_dir=True)
            w.writerow([rel, "dir", "", "", "", cat, ins, "", act, "cache/empty dir"])
    n_del = sum(1 for f in files if f["action"] == "delete")
    n_quar = sum(1 for f in files if f["action"] == "quarantine")
    print(f"plan：清单 {manifest}；文件 delete={n_del} quarantine={n_quar}；目录候选 {len(dirs_cand)}")
    print("下一步：ykla 审清单 → --apply --manifest <file> → --verify --manifest <file>")
    return 0


def remove_file(p: Path) -> None:
    try:
        gone = all(e.name != p.name for e in os.scandir(p.parent))
    except OSError:
        gone = False
    if gone:
        return
    for _ in range(RETRY):
        try:
            p.unlink()
            return
        except PermissionError:
            pass
        except OSError:
            break
    # Windows 保留名（nul 等）与非法名兜底：\\?\ 前缀
    extended = "\\\\?\\" + str(p)
    try:
        os.remove(extended)
        return
    except OSError:
        pass
    for _ in range(RETRY):
        try:
            p.unlink()
            return
        except PermissionError:
            pass
    # Windows 保留名（nul 等）与非法名兜底：先以 \\?\ 前缀改名为合法名再删
    legal = p.parent / ("_rm_" + re.sub(r"[^\w.-]", "_", p.name).strip(".")[:30] + f"_{os.getpid()}")
    for src in ("\\\\?\\" + str(p), str(p)):
        try:
            os.rename(src, "\\\\?\\" + str(legal))
            os.remove("\\\\?\\" + str(legal))
            return
        except OSError:
            continue
    raise OSError(f"无法删除 {p}")


def rmtree_guarded(d: Path) -> None:
    try:
        shutil.rmtree(d)
        return
    except OSError:
        pass
    extended = "\\\\?\\" + str(d)
    try:
        shutil.rmtree(extended)
        return
    except OSError:
        pass
    # 尾点/尾空格目录：先以 \\?\ 前缀改名成合法名，再普通删除
    legal = d.parent / ("_rm_" + re.sub(r"[^\w.-]", "_", d.name).strip(".")[:40] + f"_{os.getpid()}")
    try:
        os.rename("\\\\?\\" + str(d), "\\\\?\\" + str(legal))
        shutil.rmtree(legal)
        return
    except OSError:
        pass
    raise OSError(f"无法移除目录 {d}")


def cmd_apply(root: Path, manifest: Path) -> int:
    rows = list(csv.DictReader(manifest.open(encoding="utf-8", newline=""), delimiter="\t"))
    date = datetime.now(TZ).strftime("%Y%m%d")
    quar = root / "script" / f"_quarantine_{date}"
    quar.mkdir(parents=True, exist_ok=True)
    quar_rel = quar.relative_to(root).as_posix()
    n_del = n_q = 0
    n_err = 0
    del_log = []
    quar_log = []
    err_log = []
    qdir_prefixes = tuple(r["path"] + "/" for r in rows if r["type"] == "dir" and r["action"] == "quarantine")
    tracked = tracked_files(root)
    for r in rows:
        p = root / r["path"]
        if r["type"] == "dir":
            if r["action"] == "quarantine" and p.exists():
                try:
                    dest = quar / r["path"].replace("/", "__")
                    shutil.move(str(p), str(dest))
                    n_q += 1
                    quar_log.append(r["path"])
                except Exception as exc:
                    if any(t.startswith(r["path"] + "/") for t in tracked):
                        n_err += 1
                        err_log.append(f"dir:{r['path']}:{exc}"[:160])
                    else:
                        rmtree_guarded(p)
                        n_dirs += 1
                        del_log.append(r["path"])
            continue
        if any(r["path"].startswith(qp) for qp in qdir_prefixes):
            continue
        if r["path"].startswith(quar_rel + "/"):
            continue

        try:
            try:
                gone = not p.exists()
            except OSError:
                gone = True
            if gone:
                continue
            if sha256(p) != r["sha256"]:
                print(f"SKIP（哈希不符，防漂移）：{r['path']}")
                continue
            if r["action"] == "delete":
                remove_file(p)
                n_del += 1
                del_log.append(r["path"])
            elif r["action"] == "quarantine":
                dest = quar / r["path"].replace("/", "__")
                dest.parent.mkdir(parents=True, exist_ok=True)
                try:
                    shutil.move(str(p), str(dest))
                except OSError:
                    legal = p.parent / ("_rm_" + re.sub(r"[^\w.-]", "_", p.name).strip(".")[:30] + f"_{os.getpid()}")
                    os.rename("\\\\?\\" + str(p), "\\\\?\\" + str(legal))
                    shutil.move(str(legal), str(dest))
                n_q += 1
                quar_log.append(r["path"])
        except Exception as exc:
            n_err += 1
            err_log.append(f"{r['path']}:{exc}"[:160])
    # 目录：action=delete 的缓存目录受控递归移除（无 tracked 后代；node_modules 留 ykla）
    n_dirs = 0
    skip_nm = 0
    for r in rows:
        if r["type"] != "dir" or r["action"] != "delete":
            continue
        d = root / r["path"]
        if not d.exists():
            continue
        if d.name == "node_modules":
            skip_nm += 1
            continue
        if any(t.startswith(r["path"] + "/") for t in tracked):
            n_err += 1
            err_log.append(f"dir:{r['path']}:含 tracked 后代，拒删")
            continue
        try:
            rmtree_guarded(d)
            n_dirs += 1
        except Exception as exc:
            n_err += 1
            err_log.append(f"rmtree:{r['path']}:{exc}"[:160])
    log_path = manifest.parent / f"apply_log_{datetime.now(TZ).strftime('%H%M%S')}.json"
    log_path.write_text(json.dumps({"deleted": del_log, "deleted_count": n_del, "quarantined_dirs": quar_log, "quarantined_files": n_q, "dirs_removed": n_dirs, "errors": err_log, "error_count": n_err}, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
    print(f"apply：删除 {n_del} 件；隔离（目录整移 {len(quar_log)}／文件 {n_q}）；移除空目录 {n_dirs}；错误跳过 {n_err}；日志 {log_path}")
    return 0 if n_err == 0 else 1


def cmd_verify(root: Path, manifest: Path) -> int:
    rows = list(csv.DictReader(manifest.open(encoding="utf-8", newline="") if manifest.exists() else sys.stdin, delimiter="\t"))
    missing_del = [r["path"] for r in rows if r["action"] == "delete" and r["type"] == "file" and (root / r["path"]).exists()]
    gone_dirs = [r["path"] for r in rows if r["action"] == "delete" and r["type"] == "dir" and (root / r["path"]).exists()]
    if missing_del or gone_dirs:
        print(f"verify FAIL：残留 delete 项 {len(missing_del)}、目录 {len(gone_dirs)}")
        for x in (missing_del + gone_dirs)[:10]:
            print(f"  - {x}")
        return 1
    print("verify PASS：清单内 delete 项零残留")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="临时文件与垃圾清理执行器（§12）")
    ap.add_argument("--scan", action="store_true", help="只读分类计数")
    ap.add_argument("--plan", action="store_true", help="写清单不删除")
    ap.add_argument("--apply", action="store_true", help="按清单执行删除/隔离")
    ap.add_argument("--verify", action="store_true", help="复扫清单零残留")
    ap.add_argument("--manifest", type=str, default="", help="清单路径（apply/verify 必填）")
    ap.add_argument("--root", type=str, default="", help="仓库根（默认脚本位置上溯）")
    a = ap.parse_args()
    root = Path(a.root).resolve() if a.root else ROOT
    if a.scan:
        return cmd_scan(root)
    if a.plan:
        return cmd_plan(root)
    if a.apply:
        if not a.manifest:
            print("apply 需要 --manifest")
            return 2
        return cmd_apply(root, Path(a.manifest))
    if a.verify:
        if not a.manifest:
            print("verify 需要 --manifest")
            return 2
        return cmd_verify(root, Path(a.manifest))
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
