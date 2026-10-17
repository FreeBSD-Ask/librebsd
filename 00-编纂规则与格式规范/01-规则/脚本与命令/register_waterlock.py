#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""register 跨会话水位锁（water-level lock）——2026-10-16 立，H3 线用。

设立缘由
--------
``historical_claims`` 的 ``claim_id``（``CL-RM-NNNNNN``）**无主键约束**
（实测 ``information_schema.table_constraints`` 计数 0），撞号会**静默成功**；
同时又无跨会话水位锁：fhk_b081 探测期读数 470,485、写时实测 475,486
（途中被他会话推进 +4,981），fhk_b080 曾与他会话号段互踩。故 register 之前
须先取得水位锁：**锁内实测 MAX → 锁内写入 → 释放前断言 rows == distinct ==
预期条数**。锁是串行化设施，不替代 claimdb_guard，也不替代写前 prebak。

升格入库（2026-10-17，主理人令「允许等级水位线」）
----------------------------------------------------
原位于 ``script/_db_row_mining/register_waterlock.py``。``script/`` 整体受
``.gitignore *.py`` 排除（全库唯一豁免是 ``!00-编纂规则与格式规范/01-规则/
脚本与命令/*.py``），故该脚本此前**永久不可入库**——改一轮丢一轮，与
``_longline_status.py`` 迁入前（2026-10-15）的处境完全相同。现迁至本目录：

* 本文件（``01-规则/脚本与命令/register_waterlock.py``）为**权威副本**；
* ``script/_db_row_mining/register_waterlock.py`` 为 gitignore 下的历史留盘，
  保留不删（删除须用户明示），两者内容除本段说明外逐字节相同；
* ``repo_root()`` 从脚本位置向上找仓库根（本目录上行 3 层即达），迁入后仍在
  其 6 层上限内，路径解析不破；
* 已在 ``01-规则/README.md`` 固定脚本清单、``脚本与命令/README.md`` 与
  ``audit_gate_registry.py`` REGISTRY（``no="—"``）登记，R1／R2／R4 可机检。

用法
----
    # 1) 取锁：锁内实测水位，回吐本批 claim_id 号段
    python register_waterlock.py acquire --db historical_claims \
        --tag fhk_b082 --count 2000 --session h3-b082

    # 2) 调用方在锁内完成 register 写入（锁文件在盘，他会话 acquire 会被拦）

    # 3) 释放：rows 与 distinct 与 count 不等即拒放锁
    python register_waterlock.py release --db historical_claims \
        --tag fhk_b082 --rows 652 --distinct 652

    # 库形式：
    from register_waterlock import waterlock
    with waterlock("historical_claims", "fhk_b082", count=2000) as w:
        ...  # w.min_claim_id / w.max_claim_id / w.live_max

    # 只读模式（不改锁）
    python register_waterlock.py probe    --db historical_claims
    python register_waterlock.py show
    python register_waterlock.py selftest

退出码：0 成功／1 断言或冲突失败／2 依赖或路径不可解析。
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import socket
import sys
import tempfile
import time
import unicodedata
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterator, Optional

SCHEMA = "register_waterlock/1"
DEFAULT_TTL = 3 * 60 * 60          # 锁最长存活 3 小时
DEFAULT_MAX_AGE = 24 * 60 * 60     # 超过此龄视为陈旧锁
PROBE_TIMEOUT = 180                # DuckDB 只读打开超时（秒）
PROBE_SQL = (
    "SELECT MAX(CAST(SUBSTR(claim_id, 7) AS INTEGER)) AS m "
    "FROM claim WHERE claim_id LIKE 'CL-RM-%'"
)

# claim 库唯一真值路径（相对仓库根；不写死盘符，见 AGENTS.md
# 「功能数据库唯一真值路径与空壳防治」节）
DEFAULT_DB_PATHS = {
    "historical_claims": "04-现代研究文献/historical_claims.duckdb",
}


# --------------------------------------------------------------------------
# 路径解析：UNC 为主，盘符映射为降级方案（D: 在 Git Bash 不可见，在 Python
# 进程可见；DuckDB 对 UNC 有已知路径重复问题，故保留盘符降级）
# --------------------------------------------------------------------------

def repo_root(start: Optional[Path] = None) -> Path:
    """从脚本位置向上找仓库根；找不到则报错退出 2。"""
    p = (start or Path(__file__).resolve()).parent
    for _ in range(6):
        if (p / "04-现代研究文献").is_dir() and (p / "12-数据库备份").is_dir():
            return p
        p = p.parent
    raise SystemExit("[exit 2] 无法定位仓库根（未找到 04-现代研究文献 与 12-数据库备份）")


def drive_variant(unc: Path, drive: str = "D:") -> Optional[Path]:
    """把 ``\\\\HOST\\share\\d\\...`` 映射成 ``D:\\...``；不可映射返回 None。"""
    s = str(unc)
    parts = s.split("\\")
    if len(parts) >= 4 and parts[0] == "" and parts[1].startswith("\\"):
        i = parts.index(drive.rstrip(":").lower()) if drive.rstrip(":").lower() in [
            x.lower() for x in parts
        ] else -1
        if i > 0:
            return Path(drive + "\\" + "\\".join(parts[i + 1:]))
    return None


def resolve_db(db: str, db_path: Optional[str]) -> Path:
    if db_path:
        p = Path(db_path)
        if not p.is_file():
            raise SystemExit(f"[exit 2] 库文件不存在：{p}")
        return p
    rel = DEFAULT_DB_PATHS.get(db)
    if rel is None:
        raise SystemExit(
            f"[exit 2] 未知库 {db!r}；请显式传 --db-path（已知：{list(DEFAULT_DB_PATHS)}）"
        )
    p = repo_root() / rel
    if p.is_file():
        return p
    raise SystemExit(f"[exit 2] 库文件不存在：{p}（可显式传 --db-path 覆盖）")


# --------------------------------------------------------------------------
# 水位实测（可插拔；失败时不阻断互斥，但必须在载荷里显式留痕）
# --------------------------------------------------------------------------

def probe_max_claim_id(db_file: Path, timeout: int = PROBE_TIMEOUT) -> Optional[int]:
    """只读打开 claim 库实测 MAX(CL-RM 序号)。任何异常一律返回 None 并留痕。"""
    import importlib.util

    if importlib.util.find_spec("duckdb") is None:
        return None
    try:
        import duckdb  # type: ignore

        cands = [db_file]
        dv = drive_variant(db_file)
        if dv is not None and dv.is_file():
            cands.append(dv)
        last = None
        for c in cands:
            try:
                con = duckdb.connect(str(c), read_only=True)
                try:
                    row = con.execute(PROBE_SQL).fetchone()
                    return None if row is None or row[0] is None else int(row[0])
                finally:
                    con.close()
            except Exception as e:  # noqa: BLE001
                last = e
        if last is not None:
            sys.stderr.write(f"[warn] 水位实测失败（互斥仍有效，需 --max-claim-id 显式给定）：{last}\n")
        return None
    except Exception as e:  # noqa: BLE001
        sys.stderr.write(f"[warn] duckdb 导入失败：{e}\n")
        return None


# --------------------------------------------------------------------------
# 锁文件：O_EXCL 原子创建（SMB2/NTFS 上 create-exclusive 原子）
# --------------------------------------------------------------------------

def lock_dir(base: Path) -> Path:
    d = base / "12-数据库备份" / "waterlock"
    d.mkdir(parents=True, exist_ok=True)
    return d


def _safe(tag: str) -> str:
    """把 tag 收敛成可安全拼进文件名的串。

    必须保留字母与**数字**（`Nd` 的类首字符是 `N`，不是 `L`）——否则
    ``fhk_b081`` 与 ``fhk_b082`` 会被收敛成同一个文件名，两批共用一把锁，
    互相覆盖且互相误拦。
    """
    out = []
    for ch in tag:
        if unicodedata.category(ch)[0] in "LN":
            out.append(ch)
        else:
            out.append("_")
    s = "".join(out).strip("_")
    return s[:64] or "untagged"


def lock_path(base: Path, db: str, tag: str) -> Path:
    return lock_dir(base) / f"register__{_safe(db)}__{_safe(tag)}.lock"


def _json_write(p: Path, payload: Dict[str, Any]) -> None:
    """原子写 JSON：同目录临时件 + os.replace（SMB2 上 replace 原子）。"""
    fd, tmp = tempfile.mkstemp(prefix=".wl_tmp_", dir=str(p.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, ensure_ascii=False, indent=1)
        os.replace(tmp, str(p))
    except Exception:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def _now() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def _epoch(ts: str) -> float:
    return datetime.fromisoformat(ts).timestamp()


class LockFile:
    """一把水位锁的句柄。

    live_max 为 None 表示水位未能实测（互斥仍成立，调用方须自己给号段）。
    """

    def __init__(self, path: Path, payload: Dict[str, Any]):
        self.path = path
        self.p = payload

    @property
    def tag(self) -> str:
        return self.p["tag"]

    @property
    def db(self) -> str:
        return self.p["db"]

    @property
    def live_max(self) -> Optional[int]:
        return self.p.get("live_max")

    @property
    def min_claim_id(self) -> Optional[int]:
        return self.p.get("min_claim_id")

    @property
    def max_claim_id(self) -> Optional[int]:
        return self.p.get("max_claim_id")

    @property
    def claim_count(self) -> Optional[int]:
        return self.p.get("claim_count")

    def alive(self, now: Optional[float] = None) -> bool:
        now = now if now is not None else time.time()
        acquired = _epoch(self.p.get("acquired_at", _now()))
        ttl = float(self.p.get("ttl_seconds", DEFAULT_TTL))
        return (now - acquired) < ttl

    def age(self, now: Optional[float] = None) -> float:
        now = now if now is not None else time.time()
        return now - _epoch(self.p.get("acquired_at", _now()))

    def verdict(self, now: Optional[float] = None) -> str:
        """alive / stale / expired——供 show 与拒绝信息用。"""
        now = now if now is not None else time.time()
        if self.alive(now):
            return "alive"
        if self.age(now) < DEFAULT_MAX_AGE:
            return "stale"
        return "expired"

    def release(self, rows: Optional[int], distinct: Optional[int],
                reason: str = "released") -> None:
        if self.p.get("claim_count") is not None:
            if rows is None or distinct is None:
                raise SystemExit(
                    "[exit 1] 释放水位锁须给出 --rows 与 --distinct"
                    "（无主键约束下这是唯一能证明号段连续的机会）"
                )
            if rows != self.p["claim_count"]:
                raise SystemExit(
                    f"[exit 1] rows {rows} != 预期 {self.p['claim_count']}，拒放锁"
                )
            if distinct != rows:
                raise SystemExit(
                    f"[exit 1] distinct {distinct} != rows {rows}⇒claim_id 撞号，拒放锁"
                )
        self.p["released_at"] = _now()
        self.p["reason"] = reason
        self.p["committed_rows"] = rows
        self.p["committed_distinct"] = distinct
        _json_write(self.path, self.p)
        try:
            os.unlink(str(self.path))
        except OSError as e:
            raise SystemExit(
                f"[exit 1] 已写入释放留痕但无法删除锁文件：{self.path}（{e}）"
            )

    def takeover(self, reason: str) -> None:
        self.p["taken_over_at"] = _now()
        self.p["taken_over_by"] = f"{socket.gethostname()}:{os.getpid()}"
        self.p["takeover_reason"] = reason
        self.p["acquired_at"] = _now()
        _json_write(self.path, self.p)

    def abort(self, reason: str) -> None:
        """本会话放弃本次取号：只留痕不删锁（锁仍是本会话持有的）。"""
        self.p["aborted_at"] = _now()
        self.p["abort_reason"] = reason
        _json_write(self.path, self.p)
        try:
            os.unlink(str(self.path))
        except OSError:
            pass


def _try_create(path: Path, payload: Dict[str, Any]) -> None:
    """O_EXCL 原子创建；EEXIST 抛 FileExistsError。"""
    last = None
    for _ in range(5):
        fd = None
        try:
            fd = os.open(str(path), os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o644)
            with os.fdopen(fd, "w", encoding="utf-8") as fh:
                json.dump(payload, fh, ensure_ascii=False, indent=1)
            return
        except FileExistsError:
            raise
        except OSError as e:
            last = e
            if fd is not None:
                try:
                    os.close(fd)
                except OSError:
                    pass
            time.sleep(0.2)
    raise OSError(f"创建锁文件失败：{last}")


def list_locks(base: Path) -> list:
    out = []
    d = base / "12-数据库备份" / "waterlock"
    if not d.is_dir():
        return out
    for f in sorted(d.glob("register__*.lock")):
        try:
            lp = LockFile(f, json.loads(f.read_text(encoding="utf-8")))
            out.append(lp)
        except Exception:  # noqa: BLE001
            continue
    return out


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def cmd_acquire(a: argparse.Namespace) -> int:
    base = Path(a.base) if a.base else repo_root()
    lp = lock_path(base, a.db, a.tag)

    if lp.exists():
        other = LockFile(lp, json.loads(lp.read_text(encoding="utf-8")))
        v = other.verdict()
        if v == "alive":
            print(json.dumps({
                "ok": False, "verdict": v, "held_by": other.p.get("session"),
                "db": other.db, "tag": other.tag,
                "min_claim_id": other.min_claim_id, "max_claim_id": other.max_claim_id,
                "age_seconds": round(other.age()), "lock_file": str(lp),
            }, ensure_ascii=False, indent=1))
            return 1
        if not a.force:
            print(json.dumps({
                "ok": False, "verdict": v, "held_by": other.p.get("session"),
                "db": other.db, "tag": other.tag, "age_seconds": round(other.age()),
                "lock_file": str(lp),
                "hint": "疑似遗留锁；确认可接管后再带 --force 重跑（不会删他会话在跑的锁）",
            }, ensure_ascii=False, indent=1))
            return 1
        other.takeover(a.force_reason or "force")

    db_file = resolve_db(a.db, a.db_path)
    live_max = a.max_claim_id if a.max_claim_id is not None else probe_max_claim_id(db_file)

    payload: Dict[str, Any] = {
        "schema": SCHEMA,
        "db": a.db,
        "tag": a.tag,
        "session": a.session or f"{socket.gethostname()}:{os.getpid()}",
        "host": socket.gethostname(),
        "pid": os.getpid(),
        "ttl_seconds": a.ttl,
        "claim_count": a.count,
        "db_file": str(db_file),
        "live_max": live_max,
        "probe_sql": PROBE_SQL,
        "acquired_at": _now(),
    }
    if live_max is not None:
        payload["min_claim_id"] = live_max + 1
        payload["max_claim_id"] = live_max + a.count
    else:
        payload["min_claim_id"] = None
        payload["max_claim_id"] = None
        payload["note"] = "水位未能实测；互斥成立，号段须调用方另行确定"

    if lp.exists():  # 上面走了 takeover 分支
        _json_write(lp, payload)
    else:
        _try_create(lp, payload)

    if live_max is None:
        print(json.dumps({
            "ok": False, "verdict": "alive", "db": a.db, "tag": a.tag,
            "lock_file": str(lp),
            "error": "水位实测失败：请显式传 --max-claim-id 后重取锁",
        }, ensure_ascii=False, indent=1))
        payload["aborted_at"] = _now()
        payload["abort_reason"] = "probe failed"
        _json_write(lp, payload)
        os.unlink(str(lp))
        return 2

    if a.dry_run:
        payload["dry_run"] = True
        _json_write(lp, payload)
        print(json.dumps({
            "ok": True, "dry_run": True, "db": a.db, "tag": a.tag,
            "live_max": live_max, "min_claim_id": payload["min_claim_id"],
            "max_claim_id": payload["max_claim_id"], "lock_file": str(lp),
            "note": "dry-run：号段已占用但尚未 register；请删除锁文件后再取真锁",
        }, ensure_ascii=False, indent=1))
        return 0

    print(json.dumps({
        "ok": True, "verdict": "alive", "db": a.db, "tag": a.tag,
        "live_max": live_max, "min_claim_id": payload["min_claim_id"],
        "max_claim_id": payload["max_claim_id"], "claim_count": a.count,
        "lock_file": str(lp),
        "warning": "claim_id 无主键约束：写后须独立断言 rows == distinct == claim_count",
    }, ensure_ascii=False, indent=1))
    return 0


def cmd_release(a: argparse.Namespace) -> int:
    base = Path(a.base) if a.base else repo_root()
    lp = lock_path(base, a.db, a.tag)
    if not lp.exists():
        print(json.dumps({"ok": False, "error": f"锁文件不存在：{lp}",
                          "hint": "无锁释放＝本批从未取过水位锁"}, ensure_ascii=False, indent=1))
        return 1
    lf = LockFile(lp, json.loads(lp.read_text(encoding="utf-8")))
    if lf.p.get("session") != (a.session or f"{socket.gethostname()}:{os.getpid()}") and not a.force:
        print(json.dumps({"ok": False, "verdict": "not_owner",
                          "held_by": lf.p.get("session"), "lock_file": str(lp),
                          "hint": "非本会话锁；确认后再带 --force"}, ensure_ascii=False, indent=1))
        return 1
    lf.release(a.rows, a.distinct)
    print(json.dumps({"ok": True, "db": a.db, "tag": a.tag, "rows": a.rows,
                      "distinct": a.distinct, "min_claim_id": lf.min_claim_id,
                      "max_claim_id": lf.max_claim_id}, ensure_ascii=False, indent=1))
    return 0


def cmd_abort(a: argparse.Namespace) -> int:
    base = Path(a.base) if a.base else repo_root()
    lp = lock_path(base, a.db, a.tag)
    if not lp.exists():
        return 0
    lf = LockFile(lp, json.loads(lp.read_text(encoding="utf-8")))
    lf.abort(a.reason or "aborted by session")
    print(json.dumps({"ok": True, "aborted": True, "db": a.db, "tag": a.tag},
                     ensure_ascii=False, indent=1))
    return 0


def cmd_probe(a: argparse.Namespace) -> int:
    base = Path(a.base) if a.base else repo_root()
    db_file = resolve_db(a.db, a.db_path)
    m = probe_max_claim_id(db_file)
    print(json.dumps({"db": a.db, "db_file": str(db_file), "max_claim_id": m,
                      "sql": PROBE_SQL,
                      "next_available": (m + 1) if m is not None else None},
                     ensure_ascii=False, indent=1))
    return 0 if m is not None else 2


def cmd_show(a: argparse.Namespace) -> int:
    base = Path(a.base) if a.base else repo_root()
    locks = list_locks(base)
    print(json.dumps([
        {"db": l.db, "tag": l.tag, "verdict": l.verdict(),
         "session": l.p.get("session"), "host": l.p.get("host"), "pid": l.p.get("pid"),
         "age_seconds": round(l.age()), "acquired_at": l.p.get("acquired_at"),
         "min_claim_id": l.min_claim_id, "max_claim_id": l.max_claim_id,
         "claim_count": l.claim_count,
         "committed_rows": l.p.get("committed_rows"),
         "dry_run": l.p.get("dry_run", False),
         "lock_file": str(l.path)}
        for l in locks
    ], ensure_ascii=False, indent=1))
    return 0


@contextmanager
def waterlock(db: str, tag: str, *, count: Optional[int] = None,
              session: Optional[str] = None, base: Optional[Path] = None,
              max_claim_id: Optional[int] = None, force: bool = False,
              ttl: int = DEFAULT_TTL, db_path: Optional[str] = None) -> Iterator[LockFile]:
    """库形式的取锁／释放。进入即持锁，退出即释放（不做 rows 断言）。"""
    b = base or repo_root()
    lp = lock_path(b, db, tag)
    if lp.exists() and not force:
        other = LockFile(lp, json.loads(lp.read_text(encoding="utf-8")))
        if other.verdict() == "alive":
            raise SystemExit(f"[exit 1] 水位锁已被占用：{other.tag}（{other.p.get('session')}）")
        if other.verdict() != "expired":
            raise SystemExit(f"[exit 1] 疑似遗留锁（{other.verdict()}），需 force=True 并留痕")
    m = max_claim_id
    if m is None:
        m = probe_max_claim_id(resolve_db(db, db_path))
    if m is None:
        raise SystemExit("[exit 2] 水位未能实测")
    payload: Dict[str, Any] = {
        "schema": SCHEMA, "db": db, "tag": tag,
        "session": session or f"{socket.gethostname()}:{os.getpid()}",
        "host": socket.gethostname(), "pid": os.getpid(),
        "ttl_seconds": ttl, "claim_count": count,
        "db_file": str(resolve_db(db, db_path)), "live_max": m,
        "min_claim_id": m + 1, "max_claim_id": (m + count) if count else None,
        "acquired_at": _now(),
    }
    if lp.exists():
        _json_write(lp, payload)
    else:
        _try_create(lp, payload)
    lf = LockFile(lp, payload)
    try:
        yield lf
    finally:
        try:
            os.unlink(str(lf.path))
        except OSError:
            pass


# --------------------------------------------------------------------------
# 自检：判据非空自证（锁必须真能互斥，不能是空转）
# --------------------------------------------------------------------------

def selftest() -> int:
    import subprocess
    tmp = Path(tempfile.mkdtemp(prefix="wl_selftest_"))
    me = f"{socket.gethostname()}:{os.getpid()}"
    fails = []

    def chk(name: str, cond: bool, detail: str = "") -> None:
        if not cond:
            fails.append(f"{name}{('　' + detail) if detail else ''}")

    try:
        # 造一个假的 claim 库：只测「锁文件互斥」这条判据，不依赖真库
        b = tmp / "repo"
        (b / "04-现代研究文献").mkdir(parents=True)
        (b / "12-数据库备份").mkdir(parents=True)
        (b / "04-现代研究文献" / "t.duckdb").write_bytes(b"x")
        lp = lock_path(b, "t", "tagA")

        # T1 取锁成功，且载荷里 min/max 号段正确
        p1: Dict[str, Any] = {
            "schema": SCHEMA, "db": "t", "tag": "tagA", "session": me,
            "host": socket.gethostname(), "pid": os.getpid(),
            "ttl_seconds": 60, "claim_count": 5, "live_max": 100,
            "min_claim_id": 101, "max_claim_id": 105, "acquired_at": _now(),
        }
        _try_create(lp, p1)
        lf = LockFile(lp, p1)
        chk("T1 取锁成功", lf.alive())
        chk("T1 号段", lf.min_claim_id == 101 and lf.max_claim_id == 105)

        # T2 同行同号并发创建必须失败（互斥判据非空）
        try:
            _try_create(lp, dict(p1, tag="tagB"))
            chk("T2 互斥", False, "同行同 tag 竟创建成功")
        except FileExistsError:
            chk("T2 互斥", True)

        # T3 释放前断言：distinct != rows 必须拒放
        try:
            lf.release(5, 4)
            chk("T3 distinct!=rows 拒放", False, "撞号竟被放行")
        except SystemExit:
            chk("T3 distinct!=rows 拒放", True)
        chk("T3 锁仍在", lp.exists())

        # T4 缺参释放必须拒放
        try:
            lf.release(5, None)
            chk("T4 缺参拒放", False, "缺 distinct 竟被放行")
        except SystemExit:
            chk("T4 缺参拒放", True)

        # T5 正常释放成功且锁文件删除
        lf.release(5, 5)
        chk("T5 正常释放", not lp.exists())

        # T6 陈旧锁判定（ttl 已过、龄未超上限）
        old = dict(p1, acquired_at=datetime.fromtimestamp(
            time.time() - 3600).astimezone().isoformat(timespec="seconds"))
        _try_create(lp, old)
        lf2 = LockFile(lp, old)
        chk("T6 陈旧锁判定", lf2.verdict() == "stale")

        # T7 已死进程锁不可自动接管，须显式 force
        chk("T7 非 force 不接管", not lf2.alive())
        try:
            os.unlink(str(lp))
        except OSError:
            pass
        chk("T7 已清理", not lp.exists())

        # T8 真互斥：两把不同 tag 的锁可并存
        _try_create(lock_path(b, "t", "tagX"), dict(p1, tag="tagX"))
        _try_create(lock_path(b, "t", "tagY"), dict(p1, tag="tagY"))
        chk("T8 异 tag 并存", lock_path(b, "t", "tagX").exists()
            and lock_path(b, "t", "tagY").exists())

        # T9 _safe 对非法字符收敛（/ 空格 . 一律转 _，长度截到 64）
        chk("T9 _safe", _safe("a/b c.d") == "a_b_c_d" and len(_safe("x" * 99)) == 64)

        # T11 数字必须保留——否则相邻批次共用一把锁（互斥的致命缺陷）
        chk("T11 数字保留", _safe("fhk_b081") == "fhk_b081"
            and _safe("fhk_b082") == "fhk_b082"
            and _safe("fhk_b081") != _safe("fhk_b082"))
        chk("T11 锁文件名互不撞", lock_path(b, "t", "fhk_b081") != lock_path(b, "t", "fhk_b082"))

        # T10 CLI 自身：show 在空锁目录返回空列表且 exit 0
        r = subprocess.run([sys.executable, str(Path(__file__).resolve()),
                            "show", "--base", str(b)],
                           capture_output=True, text=True)
        chk("T10 show exit 0", r.returncode == 0, (r.stdout + r.stderr)[:200])

        print("PASS" if not fails else "FAIL")
        for f in fails:
            print("  FAIL |", f)
        print(f"自检结论：{'全部通过' if not fails else f'{len(fails)} 项未通过'}")
        return 0 if not fails else 1
    finally:
        shutil.rmtree(str(tmp), ignore_errors=True)


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        description="register 跨会话水位锁：claim_id 无主键约束，撞号会静默成功")
    sub = ap.add_subparsers(dest="cmd", required=True)
    for n in ("acquire", "release", "abort"):
        p = sub.add_parser(n)
        p.add_argument("--db", required=True)
        p.add_argument("--tag", required=True)
        p.add_argument("--session")
        p.add_argument("--base")
        p.add_argument("--db-path", dest="db_path")
        p.add_argument("--count", type=int)
        p.add_argument("--ttl", type=int, default=DEFAULT_TTL)
        p.add_argument("--force", action="store_true")
        p.add_argument("--force-reason", dest="force_reason")
        p.add_argument("--reason")
        p.add_argument("--max-claim-id", dest="max_claim_id", type=int)
        p.add_argument("--dry-run", dest="dry_run", action="store_true")
        p.add_argument("--rows", type=int)
        p.add_argument("--distinct", type=int)
    p = sub.add_parser("probe")
    p.add_argument("--db", required=True)
    p.add_argument("--base")
    p.add_argument("--db-path", dest="db_path")
    p = sub.add_parser("show")
    p.add_argument("--base")
    p = sub.add_parser("selftest")
    return ap


def main(argv: Optional[list] = None) -> int:
    a = build_parser().parse_args(argv)
    if a.cmd == "acquire":
        if a.count is None or a.count <= 0:
            print("[exit 2] --count 必填且 >0（锁须知道本批要占多少个号）", file=sys.stderr)
            return 2
        return cmd_acquire(a)
    if a.cmd == "release":
        return cmd_release(a)
    if a.cmd == "abort":
        return cmd_abort(a)
    if a.cmd == "probe":
        return cmd_probe(a)
    if a.cmd == "show":
        return cmd_show(a)
    return selftest()


if __name__ == "__main__":
    sys.exit(main())
