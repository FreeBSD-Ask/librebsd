#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""claimdb_guard 快照多槽轮换与污染识别（2026-10-17 立）。

配套 ``claimdb_guard.py``，不修改它、不与它同文件施工。

设立缘由
--------
``claimdb_guard.py`` 的快照是**单槽**：``12-数据库备份/claimdb_guard_state.json``
被每次非 FAIL 运行就地覆盖。两个后果：

1. **基线不可回溯**——比对基准永远是「上一次运行」，一旦上一次运行发生在污染态
   （2026-10-13 广播事故：``evidence.fact_text`` 472,510 行被写成一字），快照就把
   污染态记成了基线，此后 S2（distinct 骤降）／S4（行数骤降）对污染态比对，
   哨兵等于对着假水位喊话；
2. **污染无法事后识别**——单槽被覆写后，健康基线无从找起，只能靠人工翻别的备份。

本工具把快照改成多槽轮换，并**只用快照自带指标**（不碰库）判定每个槽是健康还是
污染，从而能一键把比对基线换回最近的干净槽：下一次 ``claimdb_guard.py`` 运行即
对健康基线比对，S2／S4 重新有效。

污染指纹（全部取自快照 JSON 自身，不打开任何库）
--------------------------------------------------
* ``claims.fact_max_pct > 0.25`` 或 ``claims.upd_max_pct > 0.5`` ⇒ ``poisoned``
  （对应 S1 FAIL / S3 FAIL 阈值）
* ``claims.fact_max_pct > 0.05`` 或 ``distinct_ratio < 0.9`` ⇒ ``suspect``
  （S1 WARN 档）
* 其余 ⇒ ``healthy``。实测健康槽约 0.994 distinct／0.00017 单值占比；
  2026-10-13 污染槽约 0.025 distinct／0.975 单值占比，两态相差两个数量级。

用法
----
    python rotate_guard_state.py pre         # 门禁运行**前**存档当前快照
    python claimdb_guard.py --db historical_claims      # 门禁运行（刷新单槽）
    python rotate_guard_state.py post        # 门禁运行**后**存档新快照
    python rotate_guard_state.py list        # 全部槽＋健康判定
    python rotate_guard_state.py health      # 只报判定；无健康槽 exit 1
    python rotate_guard_state.py restore --best        # 基线换回最近的健康槽
    python rotate_guard_state.py restore --slot <槽名>  # 指定槽（污染槽需 --force）
    python rotate_guard_state.py prune --keep 12
    python rotate_guard_state.py selftest

退出码：0 成功／1 判定失败或断言失败／2 依赖或路径不可解析。
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import shutil
import sys
import tempfile
from datetime import datetime
from pathlib import Path

STATE_NAME = "claimdb_guard_state.json"
SLOT_PREFIX = "claimdb_guard_state.slot-"
SLOT_GLOB = "claimdb_guard_state.slot-*.json"
DEFAULT_KEEP = 12
SCHEMA = "claimdb_guard_state_slot/1"

# 与 claimdb_guard.py 阈值对齐（S1 FAIL 0.25 / S1 WARN 0.05 / S3 FAIL 0.50）
S1_FAIL, S1_WARN, S3_FAIL, DISTINCT_FLOOR = 0.25, 0.05, 0.50, 0.90

BASE_CANDIDATES = (r"D:\librebsd", r"\\DESKTOP-M5P610N\d\librebsd")


def resolve_base(explicit=None):
    """仓库根解析：显式 > D: 盘符 > UNC 别名；皆不可达返回 None。

    不写死盘符（2026-10-15 教训：硬编码 d:\\librebsd 在盘符未映射时
    让依赖脚本静默空转，而门禁静默失效比报错危险）。
    """
    if explicit:
        return explicit if os.path.isdir(explicit) else None
    for c in BASE_CANDIDATES:
        if os.path.isdir(c):
            return c
    return None


def backup_root(base):
    return os.path.join(base, "12-数据库备份")


def state_path(base):
    return os.path.join(backup_root(base), STATE_NAME)


def die2(msg):
    sys.stderr.write("[exit 2] {}\n".format(msg))
    raise SystemExit(2)


def md5_of(path):
    h = hashlib.md5()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def atomic_copy(src, dst):
    """同目录临时件 + os.replace（SMB2 上 replace 原子；不跨盘）。"""
    d = os.path.dirname(dst)
    fd, tmp = tempfile.mkstemp(prefix=".rgs_tmp_", dir=d)
    try:
        with os.fdopen(fd, "rb+") as out:
            shutil.copyfileobj(open(src, "rb"), out, 1 << 20)
        os.replace(tmp, dst)
    except Exception:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def distinct_ratio(claims):
    rows = claims.get("rows") or 0
    dd = claims.get("fact_distinct") or 0
    return None if not rows else round(dd / rows, 6)


def verdict(claims):
    """只用快照自带指标判定槽的健康度；claims 缺失返回 ('unknown', [])。"""
    if not isinstance(claims, dict) or not claims.get("rows"):
        return "unknown", ["无 claims 深度指标（非 claims 门禁快照）"]
    fmp = claims.get("fact_max_pct")
    ump = claims.get("upd_max_pct")
    dr = distinct_ratio(claims)
    notes = []
    if fmp is not None and fmp > S1_FAIL:
        notes.append("fact 单值占比 {:.2%} > {:.0%}（S1 FAIL）".format(fmp, S1_FAIL))
    if ump is not None and ump > S3_FAIL:
        notes.append("updated_at 单值占比 {:.2%} > {:.0%}（S3 FAIL）".format(ump, S3_FAIL))
    if notes:
        return "poisoned", notes
    if (fmp is not None and fmp > S1_WARN):
        notes.append("fact 单值占比 {:.2%} > {:.0%}（S1 WARN）".format(fmp, S1_WARN))
    if dr is not None and dr < DISTINCT_FLOOR:
        notes.append("distinct/rows {:.3f} < {:.2f}".format(dr, DISTINCT_FLOOR))
    if notes:
        return "suspect", notes
    return "healthy", ["distinct/rows {:.3f}".format(dr) if dr else "distinct 计数字段缺失"]


def row_for(path, src_label):
    """把单个槽读成结构化记录（供 list/health/restore 共用）。"""
    try:
        with io.open(path, encoding="utf-8") as fh:
            d = json.load(fh)
        claims = d.get("claims") or {}
        v, notes = verdict(claims)
        return {
            "name": os.path.basename(path),
            "path": path,
            "source": src_label,
            "size": os.path.getsize(path),
            "md5": md5_of(path),
            "at": datetime.fromtimestamp(os.path.getmtime(path)).isoformat(timespec="seconds"),
            "schema": d.get("v") if isinstance(d.get("v"), str) else None,
            "updated_at": d.get("updated_at"),
            "claim_rows": claims.get("rows"),
            "fact_distinct": claims.get("fact_distinct"),
            "distinct_ratio": distinct_ratio(claims),
            "fact_max_pct": round(claims.get("fact_max_pct") or 0, 8),
            "upd_max_pct": round(claims.get("upd_max_pct") or 0, 8),
            "dbs": sorted((d.get("dbs") or {}).keys()),
            "verdict": v,
            "notes": notes,
        }
    except Exception as e:  # noqa: BLE001
        return {"name": os.path.basename(path), "path": path, "source": src_label,
                "verdict": "unreadable", "notes": [type(e).__name__ + ": " + str(e)[:120]]}


def all_slots(base):
    """全部槽，按文件名（时间戳）升序。单槽现件不并入——它由 restore 管理。"""
    root = backup_root(base)
    if not os.path.isdir(root):
        return []
    out = []
    for n in sorted(x for x in os.listdir(root)
                    if x.startswith(SLOT_PREFIX) and x.endswith(".json")):
        out.append(row_for(os.path.join(root, n), "slot"))
    return out


def dump(rows):
    print(json.dumps(rows, ensure_ascii=False, indent=1))


# ---------------------------------------------------------------- CLI 子命令

def cmd_adopt(args, label):
    """把当前单槽快照存成一个槽。"""
    base = resolve_base(args.base)
    if base is None:
        die2("仓库根不可解析：{} 均不可达；请用 --base 显式指定".format("、".join(BASE_CANDIDATES)))
    sp = state_path(base)
    if not os.path.isfile(sp):
        die2("无快照可存档：{} 不存在（先跑一次 claimdb_guard 生成基线）".format(sp))
    cur = row_for(sp, "live")
    dup = [r for r in all_slots(base) if r.get("md5") == cur.get("md5")]
    ts = datetime.now().strftime("%Y%m%dT%H%M%S")
    dst = os.path.join(backup_root(base), "{}{}-{}.json".format(SLOT_PREFIX, ts, cur["md5"][:8]))
    atomic_copy(sp, dst)
    row = row_for(dst, label)
    row["duplicated"] = bool(dup)
    row["note"] = "与既有槽内容相同，轮换未推进基线" if dup else "已存档"
    dump([row])
    return 0


def cmd_list(args):
    base = resolve_base(args.base)
    if base is None:
        die2("仓库根不可解析")
    rows = all_slots(base)
    sp = state_path(base)
    live = [row_for(sp, "live")] if os.path.isfile(sp) else []
    rows = live + rows
    dump(rows)
    return 0


def cmd_health(args):
    base = resolve_base(args.base)
    if base is None:
        die2("仓库根不可解析")
    rows = all_slots(base)
    good = [r for r in rows if r.get("verdict") == "healthy"]
    bad = [r for r in rows if r.get("verdict") in ("poisoned", "suspect", "unreadable")]
    print(json.dumps({"total": len(rows), "healthy": len(good),
                      "bad": len(bad),
                      "newest_healthy": good[-1]["name"] if good else None,
                      "newest_slot": rows[-1]["name"] if rows else None},
                     ensure_ascii=False, indent=1))
    if args.verbose:
        dump(rows)
    return 0 if good else 1


def cmd_restore(args):
    base = resolve_base(args.base)
    if base is None:
        die2("仓库根不可解析")
    rows = all_slots(base)
    if not rows:
        die2("无槽可恢复（先 pre/post 存档）")
    if args.slot:
        target = [r for r in rows if r["name"] == args.slot
                  or r["name"].endswith(args.slot) or r["name"] == args.slot]
        if not target:
            die2("找不到槽：{}；现有：{}".format(args.slot, [r["name"] for r in rows]))
        t = target[-1]
    else:
        good = [r for r in rows if r.get("verdict") == "healthy"]
        if not good:
            print(json.dumps({"ok": False, "error": "无健康槽可恢复",
                              "slots": [{"name": r["name"], "verdict": r["verdict"],
                                         "notes": r["notes"]} for r in rows]},
                             ensure_ascii=False, indent=1))
            return 1
        t = good[-1]
    if t["verdict"] != "healthy" and not args.force:
        print(json.dumps({"ok": False, "slot": t["name"], "verdict": t["verdict"],
                          "notes": t["notes"],
                          "hint": "污染／可疑槽会污染门禁基线；确认无误后加 --force"},
                         ensure_ascii=False, indent=1))
        return 1
    sp = state_path(base)
    if os.path.isfile(sp):
        pre = os.path.join(backup_root(base), STATE_NAME + ".pre_restore")
        atomic_copy(sp, pre)
        prev = row_for(pre, "pre_restore")
    else:
        pre, prev = None, None
    atomic_copy(t["path"], sp)
    print(json.dumps({"ok": True, "restored": t["name"], "verdict": t["verdict"],
                      "distinct_ratio": t["distinct_ratio"],
                      "fact_max_pct": t["fact_max_pct"],
                      "into": sp,
                      "previous_backup": os.path.basename(pre) if pre else None,
                      "next": "重跑 claimdb_guard.py 即对该基线比对（S2/S4 重新有效）"},
                     ensure_ascii=False, indent=1))
    return 0


def cmd_prune(args):
    base = resolve_base(args.base)
    if base is None:
        die2("仓库根不可解析")
    rows = all_slots(base)
    keep = max(1, args.keep)
    keep_set = {r["name"] for r in rows[-keep:]}
    # 健康槽永不因「非最新」被删：若删完没有健康槽，补留最近一个健康槽
    healthy = [r["name"] for r in rows if r.get("verdict") == "healthy"]
    for h in reversed(healthy):
        if h not in keep_set:
            keep_set.add(h)
            break
    removed = []
    for r in rows:
        if r["name"] in keep_set:
            continue
        p = r["path"]
        os.unlink(p)
        removed.append({"name": r["name"], "verdict": r["verdict"]})
    print(json.dumps({"kept": sorted(keep_set), "removed": removed,
                      "remaining": len([r for r in rows if r["name"] in keep_set])},
                     ensure_ascii=False, indent=1))
    return 0


# ---------------------------------------------------------------- 自检

def selftest():
    import subprocess

    tmp = Path(tempfile.mkdtemp(prefix="rgs_selftest_"))
    fails = []

    def chk(name, cond, detail=""):
        if not cond:
            fails.append("{}{}".format(name, "　" + detail if detail else ""))

    def mk(base_dir, claims):
        b = tmp / base_dir
        r = b / "12-数据库备份"
        r.mkdir(parents=True, exist_ok=True)
        (b / "04-现代研究文献").mkdir(parents=True, exist_ok=True)
        d = {"v": "1.0", "updated_at": "2026-10-17T00:00:00",
             "claims": claims,
             "dbs": {"historical_claims": {"total_rows": 2000000, "tables": {}, "at": "x"}}}
        (r / STATE_NAME).write_text(json.dumps(d), encoding="utf-8")
        return str(b)

    def run(*args):
        r = subprocess.run([sys.executable, str(Path(__file__).resolve())] + list(args),
                           capture_output=True, text=True, encoding="utf-8")
        j = None
        s = (r.stdout or "").strip()
        if s.startswith("{") or s.startswith("["):
            try:
                j = json.loads(s)
            except Exception:
                pass
        return r.returncode, j, (r.stdout or "") + (r.stderr or "")

    try:
        healthy = {"rows": 490449, "fact_distinct": 487325,
                   "fact_max_pct": 0.0001733, "upd_max_pct": 0.0531}
        poisoned = {"rows": 484684, "fact_distinct": 12166,
                    "fact_max_pct": 0.974883, "upd_max_pct": 0.974883}
        suspect = {"rows": 490449, "fact_distinct": 300000,
                   "fact_max_pct": 0.08, "upd_max_pct": 0.1}

        # T1 健康判定
        v, _ = verdict(healthy)
        chk("T1 健康判定", v == "healthy", v)
        # T2 污染判定（2026-10-13 广播指纹）
        v, n = verdict(poisoned)
        chk("T2 污染判定", v == "poisoned" and any("S1 FAIL" in x for x in n),
            "{} {}".format(v, n))
        # T3 可疑判定（S1 WARN 档）
        chk("T3 可疑判定", verdict(suspect)[0] == "suspect")
        # T4 缺指标 => unknown
        chk("T4 缺指标", verdict({})[0] == "unknown" and verdict(None)[0] == "unknown")

        # T5/T6 pre 存档：健康槽 -> post 存档污染槽（模拟基线被污染）
        b1 = mk("r1", healthy)
        rc, _, _ = run("pre", "--base", b1)
        chk("T5 pre 建槽", rc == 0)
        with io.open(os.path.join(b1, "12-数据库备份", STATE_NAME), encoding="utf-8") as fh:
            d = json.load(fh)
        d["claims"] = poisoned
        io.open(os.path.join(b1, "12-数据库备份", STATE_NAME), "w",
                encoding="utf-8").write(json.dumps(d))
        rc, _, _ = run("post", "--base", b1)
        chk("T6 post 建槽", rc == 0)
        rc, j, _ = run("list", "--base", b1)
        names = [r["name"] for r in (j or [])]
        chk("T7 两槽＋live", rc == 0 and len(j) == 3 and names[-1].startswith(SLOT_PREFIX),
            "{} {}".format(rc, names))

        # T8 health：有健康槽 => exit 0，且 newest_healthy 指向健康槽
        rc, j, _ = run("health", "--base", b1)
        chk("T8 health 有健康槽 exit 0", rc == 0 and j["healthy"] == 1
            and j["newest_healthy"] != j["newest_slot"], j)

        # T9 restore --best 必须回到健康槽（不能取最新=污染槽）
        rc, j, _ = run("restore", "--best", "--base", b1)
        chk("T9 restore --best 选健康槽", rc == 0 and j["verdict"] == "healthy", j)
        with io.open(os.path.join(b1, "12-数据库备份", STATE_NAME), encoding="utf-8") as fh:
            restored = json.load(fh)["claims"]
        chk("T9b 内容确已换回健康基线",
            restored.get("fact_distinct") == healthy["fact_distinct"], restored)

        poison_name = [r["name"] for r in all_slots(b1) if r["verdict"] == "poisoned"][-1]
        # T10 恢复污染槽无 --force 必须拒绝
        rc2, j2, _ = run("restore", "--slot", poison_name, "--base", b1)
        chk("T10 污染槽拒恢复", rc2 == 1 and j2["verdict"] == "poisoned", j2)

        # T11 显式 --force 才可恢复污染槽
        rc3, j3, _ = run("restore", "--slot", poison_name, "--force", "--base", b1)
        chk("T11 --force 放行", rc3 == 0 and j3["verdict"] == "poisoned", j3)

        # T12 prune --keep 1 不得删掉最近的健康槽
        b2 = mk("r2", healthy)
        run("pre", "--base", b2)
        rc, _, _ = run("prune", "--keep", "1", "--base", b2)
        rem = all_slots(b2)
        chk("T12 prune 后仍有槽", rc == 0 and len(rem) >= 1, rem)

        # T13 无快照时 pre 必须 exit 2（不是静默成功）
        b3 = mk("r3", healthy)
        os.unlink(os.path.join(b3, "12-数据库备份", STATE_NAME))
        rc, _, _ = run("pre", "--base", b3)
        chk("T13 无快照 exit 2", rc == 2)

        # T14 仓库根不可达必须 exit 2
        rc, _, _ = run("pre", "--base", str(tmp / "not_exist"))
        chk("T14 不可达 base exit 2", rc == 2)

        # T15 md5 去重：内容未变再次存档应标记 duplicated
        b4 = mk("r4", healthy)
        run("pre", "--base", b4)
        rc, j, _ = run("pre", "--base", b4)
        chk("T15 内容未变标记 duplicated", rc == 0 and j[0]["duplicated"] is True, j)

        print("PASS" if not fails else "FAIL")
        for f in fails:
            print("  FAIL |", f)
        print("自检结论：{}".format("全部通过" if not fails else "{} 项未通过".format(len(fails))))
        return 0 if not fails else 1
    finally:
        shutil.rmtree(str(tmp), ignore_errors=True)


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="claimdb_guard 快照多槽轮换与污染识别（不修改 claimdb_guard.py）")
    sub = ap.add_subparsers(dest="cmd", required=True)
    for n in ("pre", "post"):
        p = sub.add_parser(n, help="{}门禁运行后存档当前快照".format("运行前" if n == "pre" else "运行"))
        p.add_argument("--base", metavar="<仓库根>")
    p = sub.add_parser("list", help="全部槽＋健康判定")
    p.add_argument("--base", metavar="<仓库根>")
    p = sub.add_parser("health", help="只报判定；无健康槽 exit 1")
    p.add_argument("--base", metavar="<仓库根>")
    p.add_argument("-v", "--verbose", action="store_true")
    p = sub.add_parser("restore", help="把单槽基线换回指定槽／最近健康槽")
    p.add_argument("--base", metavar="<仓库根>")
    p.add_argument("--slot", metavar="<槽名>")
    p.add_argument("--best", action="store_true", help="取最近的健康槽（默认）")
    p.add_argument("--force", action="store_true", help="允许恢复污染／可疑槽")
    p = sub.add_parser("prune", help="保留最近 N 个槽（健康槽兜底保留 1 个）")
    p.add_argument("--base", metavar="<仓库根>")
    p.add_argument("--keep", type=int, default=DEFAULT_KEEP)
    sub.add_parser("selftest", help="判据非空自检")
    a = ap.parse_args(argv)

    if a.cmd in ("pre", "post"):
        return cmd_adopt(a, a.cmd)
    if a.cmd == "list":
        return cmd_list(a)
    if a.cmd == "health":
        return cmd_health(a)
    if a.cmd == "restore":
        return cmd_restore(a)
    if a.cmd == "prune":
        return cmd_prune(a)
    return selftest()


if __name__ == "__main__":
    sys.exit(main())
