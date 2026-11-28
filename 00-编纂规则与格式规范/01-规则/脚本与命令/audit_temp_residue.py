#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""audit_temp_residue.py — 临时文件残留门禁（第四十件；工程实践规则 §12）。

判据：①备份后缀族（.bak/.prebak/.orig/.rej/~ 等）②__pycache__/.pyc ③错名目录
（…/零宽/[MASKED]/[path]/前导 ._ /尾部 ~）④任务临时目录残留（_audit_tmp/_tmp_*）。
作用域：--scope repo（默认，只扫 Git 跟踪树）｜all（含 script/_tmp/review_logs 本地批跑）。
退出码：0 干净；1 有残留；2 环境/用法错误。
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

BACKUP_RE = re.compile(
    r"\.(bak|bak-[^./]*|bak_[^./]*|prebak[^./]*|pre|orig|rej)$"
    r"|\.bak\.[0-9]+$|-(bak)$|~$",
    re.IGNORECASE,
)
MALFORMED = ("…", "\u200b", "\ufeff", "[MASKED]", "[path]")
LOCAL_TOPS = {"script", "_tmp", "review_logs"}
SKIP_TOPS = {".git", "12-数据库备份", "dvd6", ".trae", ".zcode", "node_modules", ".qoder", "旧大纲-20261023"}


def tracked_set(root: Path) -> set[str]:
    proc = subprocess.run(["git", "ls-files", "-z"], capture_output=True, text=True,
                          encoding="utf-8", errors="replace", cwd=str(root), timeout=120)
    return {x for x in proc.stdout.split("\0") if x}


def has_tracked_descendant(dirpath: Path, root: Path, tracked: set[str]) -> bool:
    prefix = dirpath.relative_to(root).as_posix() + "/"
    return any(t.startswith(prefix) for t in tracked)


def scan(root: Path, scope: str, tracked: set[str], base: Path | None = None, force_tracked: bool = False) -> list[dict]:
    """base=None 时扫 root（repo/all 语义）；base 给定时扫指定沙箱（selftest）。"""
    residues: list[dict] = []
    walk_root = base if base is not None else root

    def to_rel(p: Path) -> str:
        return p.relative_to(walk_root).as_posix()

    for dirpath, dirnames, filenames in __import__("os").walk(walk_root):
        d = Path(dirpath)
        rel = to_rel(d)
        parts = Path(rel).parts
        if base is None:
            if parts and parts[0] in SKIP_TOPS:
                dirnames[:] = []
                continue
            if scope == "repo" and parts and parts[0] in LOCAL_TOPS:
                dirnames[:] = []
                continue
        dirnames[:] = [x for x in dirnames if x not in {"node_modules", ".git"}]

        for dn in dirnames:
            child = d / dn
            crel = to_rel(child)
            if any(bad in dn for bad in MALFORMED) or dn.startswith("._") or dn.endswith("~"):
                if force_tracked or has_tracked_descendant(child, walk_root, tracked) or base is not None:
                    residues.append({"path": crel, "kind": "错名目录", "detail": dn})
            if dn == "__pycache__":
                if base is not None or force_tracked or has_tracked_descendant(child, walk_root, tracked):
                    residues.append({"path": crel, "kind": "__pycache__", "detail": "缓存目录"})
            if dn.startswith("_audit_tmp") or dn.startswith("_tmp_"):
                if base is not None or force_tracked or has_tracked_descendant(child, walk_root, tracked):
                    residues.append({"path": crel, "kind": "任务临时目录", "detail": dn})
        for fn in filenames:
            f = d / fn
            frel = to_rel(f)
            if BACKUP_RE.search(fn):
                if base is not None or force_tracked or frel in tracked:
                    residues.append({"path": frel, "kind": "备份后缀", "detail": fn})
            elif fn.endswith((".pyc", ".pyo")):
                if base is not None or force_tracked or frel in tracked:
                    residues.append({"path": frel, "kind": ".pyc", "detail": fn})
    return residues


def selftest() -> int:
    failures = []
    with tempfile.TemporaryDirectory() as td:
        base = Path(td)
        (base / "tracked.txt").write_text("x", encoding="utf-8")
        (base / "a.bak").write_text("x", encoding="utf-8")
        (base / "b.orig").write_text("x", encoding="utf-8")
        (base / "c~").write_text("x", encoding="utf-8")
        (base / "__pycache__").mkdir()
        (base / "__pycache__" / "m.pyc").write_bytes(b"x")
        (base / "…bad").mkdir()
        (base / "._hidden").mkdir()
        (base / "_audit_tmp_x").mkdir()
        tracked = {"tracked.txt"}
        got = scan(base, "all", tracked, base=base, force_tracked=True)
        kinds = {r["kind"] for r in got}
        for k in ("备份后缀", "__pycache__", "错名目录", "任务临时目录"):
            if k not in kinds:
                failures.append(f"正例未检出：{k}")
        if len([r for r in got if r["kind"] == "备份后缀"]) < 3:
            failures.append("备份后缀检出不全")
    with tempfile.TemporaryDirectory() as td:
        base = Path(td)
        (base / "clean.txt").write_text("x", encoding="utf-8")
        got = scan(base, "all", {"clean.txt"}, base=base, force_tracked=False)
        if got:
            failures.append(f"净目录误报：{got}")
    if failures:
        print("SELFTEST FAIL")
        for f in failures:
            print(f"- {f}")
        return 1
    print("SELFTEST PASS：正例四类全检出＋净目录零误报")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="临时文件残留门禁（第四十件）")
    ap.add_argument("--scope", choices=["repo", "all"], default="repo")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--limit", type=int, default=20)
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    root = ROOT
    tracked = tracked_set(root)
    residues = scan(root, a.scope, tracked)
    print(f"临时文件残留门禁（第四十件）｜scope={a.scope}｜残留 {len(residues)} 项")
    for r in residues[: a.limit]:
        print(f"  [{r['kind']}] {r['path']}")
    if len(residues) > a.limit:
        print(f"  …（其余 {len(residues) - a.limit} 项）")
    if a.json:
        print(json.dumps({"scope": a.scope, "count": len(residues), "items": residues}, ensure_ascii=False, indent=2))
    if residues:
        print("FAIL：存在残留；处置走 cleanup_temp.py --plan → ykla 审 → --apply")
        return 1
    print("PASS：零残留")
    return 0


if __name__ == "__main__":
    sys.exit(main())
