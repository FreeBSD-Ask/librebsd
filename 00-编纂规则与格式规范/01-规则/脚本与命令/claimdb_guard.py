# -*- coding: utf-8 -*-
"""claimdb_guard.py —— 写库门禁与全库健康哨兵（固定脚本；2026-10-14 立，ykla 令）

教训：2026-10-13 单条缺关联 UPDATE 将 historical_claims.evidence.fact_text 全表
472,510 行覆盖为同一句（广播事故）——此前写库流程无“写前哨兵”。本脚本为
“入库流程”前置门禁：任何批量写库（fix-db 修库／register 入库／批量导入）前运行，
PASS 才准写；FAIL 必须停止并排查。

用法：
  python claimdb_guard.py --db historical_claims   # 写库前门禁（claims 深度哨兵）
  python claimdb_guard.py --db <库名>              # 任意库通用检查（行数/表数快照对比）
  python claimdb_guard.py --path <库文件>          # 对任意 duckdb 文件只读检查（基线绑定该文件自身）
  python claimdb_guard.py --path <库文件> --path-state-dir <目录>   # 覆盖绑定快照目录
  python claimdb_guard.py --all                    # 全库体检（SCOPE 全库逐一快照对比）
  python claimdb_guard.py --selftest               # 自检（6 项检查：正常×2/广播/骤降/行数骤减/--path 20 行）
  python claimdb_guard.py --show                   # 查看当前快照

判据（claims 深度哨兵 S1–S4）：
  S1 fact_text 单值集中：最大单值行占比 > 25% → FAIL；> 5% → WARN（广播形态）
  S2 fact_text distinct 骤降：< 快照值 × 0.5 → FAIL
  S3 updated_at 单值集中：最大单值行占比 > 50% → FAIL（全表同刻写入特征）
  S4 evidence 行数骤降：< 快照值 × 0.9 → FAIL
通用判据（--all / --db 全库，G1–G2）：
  G1 表消失：快照中的表在现库不存在 → FAIL
  G2 总行数骤降：< 快照 × 0.9 → FAIL
快照：
  生产快照 12-数据库备份/claimdb_guard_state.json（--db／--all 使用；每次非 FAIL 运行后合并刷新）
  --path 绑定快照 script/_claimdb_guard_path_state/（键＝被检文件绝对路径＋内容 SHA-256；
    只读写该目录，绝不读写生产快照；目录不可写时降级为“无基线，仅执行绝对判据”）
退出码：0＝PASS（含 WARN）；1＝FAIL；2＝无法判定（仓库根不可解析／duckdb 版本与基线不一致）
版本探测：启动即比对 duckdb-version-baseline.txt（同目录），不一致退出码 2；
  --skip-version-check 为逃生参数（基线修复或已知混版本排查时显式放行）。
"""
import argparse
import datetime
import hashlib
import importlib.util
import json
import os
import sys

# ---- 启动版本探测（版本基线文件为唯一声明源，见 ADR-0017）----
BASELINE_NAME = "duckdb-version-baseline.txt"


def _baseline_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), BASELINE_NAME)


def baseline_expected_version():
    """读取版本基线的期望 duckdb 版本（`版本锁定：duckdb==<版本>`）；不可读返 None。"""
    try:
        with open(_baseline_path(), encoding="utf-8") as f:
            for line in f:
                s = line.strip()
                if s.startswith("版本锁定"):
                    idx = s.find("duckdb==")
                    if idx < 0:
                        return None
                    return s[idx + len("duckdb=="):].strip() or None
    except OSError:
        return None
    return None


def require_duckdb_version(skip=False):
    """启动版本探测：与基线一致方继续；不一致返回 2（--skip-version-check 放行）。"""
    if skip:
        print("[INFO] duckdb 版本探测已跳过（--skip-version-check）")
        return 0
    import duckdb
    actual = getattr(duckdb, "__version__", "unknown")
    expected = baseline_expected_version()
    fp = _baseline_path()
    if not expected:
        print("[FAIL] 版本基线不可读或缺“版本锁定：duckdb==<版本>”行：{}".format(fp))
        print("       实际 duckdb=={}；基线修复前如需继续，用 --skip-version-check。".format(actual))
        return 2
    if actual != expected:
        print("[FAIL] duckdb 版本不一致：实际 {}／期望 {}（基线 {}）".format(actual, expected, fp))
        print("       混版本会使存储格式（v64／v69）与判据假设分裂；确认后重装或经 ADR 变更基线。")
        return 2
    print("[INFO] duckdb 版本 {} 与基线一致（{}）".format(actual, fp))
    return 0


BASE_CANDIDATES = (r"D:\librebsd", r"\\DESKTOP-M5P610N\d\librebsd")


def _resolve_base():
    """仓库根解析：D: 盘符优先，UNC 别名回落；两者皆不可达则回 None。

    教训（2026-10-15 复核坐实）：原先硬编码 d:\\librebsd，盘符未映射时 --all 逐库
    连接失败记 SKIP 而整体仍可能 PASS，save_state 还会对不存在目录 makedirs 抛异常
    ——门禁静默空转比报错更危险，哨兵不能无声失效。
    """
    for c in BASE_CANDIDATES:
        if os.path.isdir(c):
            return c
    return None


BASE = _resolve_base()
BASE_OK = BASE is not None
BACKUP_ROOT = os.path.join(BASE, "12-数据库备份") if BASE else None
STATE = os.path.join(BACKUP_ROOT, "claimdb_guard_state.json") if BASE else None


def set_base(path):
    """显式指定仓库根（--base）。"""
    g = globals()
    g["BASE"] = path
    g["BASE_OK"] = True
    g["BACKUP_ROOT"] = os.path.join(path, "12-数据库备份")
    g["STATE"] = os.path.join(g["BACKUP_ROOT"], "claimdb_guard_state.json")

# 阈值（2026-10-14 定：现状实测远离阈值，见 --db 输出的“现状值”）
S1_FAIL, S1_WARN = 0.25, 0.05
S2_RATIO = 0.5
S3_FAIL = 0.5
S4_RATIO = 0.9
G2_RATIO = 0.9


def load_scope():
    """复用 backup_databases.py 的 SCOPE（全库枚举，27 库）。"""
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "backup_databases.py")
    spec = importlib.util.spec_from_file_location("backup_databases", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.SCOPE


def load_state():
    if os.path.exists(STATE):
        try:
            with open(STATE, encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def save_state(state):
    state["v"] = 1
    state["updated_at"] = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    os.makedirs(BACKUP_ROOT, exist_ok=True)
    with open(STATE, "w", encoding="utf-8", newline="\n") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


# ---- --path 模式：与被检文件绑定的独立快照（TD-016 第 1 项，2026-10-22）----
# 缺陷 D2（script/_pilot_20261022/drill_h/H-drill.md §3.4）：--path 原先加载生产快照，
# 把 20 行测试库与 51.9 万行生产基线相比，必触 S2／S3／S4 伪 FAIL。现改为按
# “绝对路径＋内容 SHA-256”绑定独立快照，且只落在 script/ 临时区。

PATH_NO_SNAP_NOTE = "（首次运行：无基线，仅执行绝对判据；本次结果将写入绑定快照）"
PATH_NO_SNAP_NOTE_DEGRADED = "（首次运行：无基线，仅执行绝对判据；快照目录不可写，本次不落基线）"
PATH_STATE_DIR_REL = os.path.join("script", "_claimdb_guard_path_state")


def default_path_state_dir():
    """--path 绑定快照默认目录（script/ 为项目允许的临时区，不入库）。"""
    return os.path.join(BASE, PATH_STATE_DIR_REL)


def _sha256_file(path):
    """文件内容 SHA-256（分块读，不整文件入内存）。"""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            chunk = f.read(1024 * 1024)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def _path_state_file(state_dir, abs_path):
    """快照文件名：由绝对路径（Windows 大小写不敏感，故 normcase）派生。"""
    key = hashlib.sha256(os.path.normcase(abs_path).encode("utf-8")).hexdigest()[:24]
    return os.path.join(state_dir, "path-{}.json".format(key))


def load_path_baseline(state_dir, abs_path, file_sha):
    """读取被检文件的绑定快照。

    返回 (snap, state_fp, note)。note 非空表示不可用基线及原因。
    内容 SHA-256 不符即视为无基线：同一文件的不同内容状态互比会产生伪 FAIL，
    宁可退回绝对判据，也不误报。
    """
    fp = _path_state_file(state_dir, abs_path)
    if not os.path.exists(fp):
        return {}, fp, None
    try:
        with open(fp, encoding="utf-8") as f:
            rec = json.load(f)
    except Exception:
        return {}, fp, "绑定快照不可解析，按无基线处理"
    if os.path.normcase(rec.get("path", "")) != os.path.normcase(abs_path):
        return {}, fp, "绑定快照路径不符，按无基线处理"
    if rec.get("file_sha256") != file_sha:
        return {}, fp, "内容 SHA-256 已变（基线 {}…），按无基线处理".format((rec.get("file_sha256") or "")[:16])
    return rec, fp, None


def _path_state_payload(rec):
    """比较用载荷：剔除写入时刻等易变字段（顶层 updated_at、逐库 at）。

    幂等要求“内容相同即不写盘”，故时间戳不参与比较；否则二跑字节必变。
    """
    out = {k: v for k, v in rec.items() if k != "updated_at"}
    dbs = {}
    for name, d in (out.get("dbs") or {}).items():
        dbs[name] = {k: v for k, v in d.items() if k != "at"} if isinstance(d, dict) else d
    out["dbs"] = dbs
    return out


def save_path_baseline(state_dir, abs_path, file_sha, snap):
    """写绑定快照，只碰 state_dir，绝不写生产快照。

    返回 "written"／"unchanged"／"failed"；内容无变化时不写盘（幂等，二跑字节不变）。
    任何 OSError 均降级返回 "failed"，由调用方明示，不改变退出码。
    """
    rec = dict(snap)
    rec["v"] = 1
    rec["path"] = abs_path
    rec["file_sha256"] = file_sha
    rec["updated_at"] = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    fp = _path_state_file(state_dir, abs_path)
    try:
        os.makedirs(state_dir, exist_ok=True)
    except OSError:
        return "failed"
    if os.path.exists(fp):
        try:
            with open(fp, encoding="utf-8") as f:
                old = json.load(f)
            if _path_state_payload(old) == _path_state_payload(rec):
                return "unchanged"
        except Exception:
            pass
    try:
        with open(fp, "w", encoding="utf-8", newline="\n") as f:
            json.dump(rec, f, ensure_ascii=False, indent=2)
    except OSError:
        return "failed"
    return "written"


def collect_claims_stats(con):
    """claims 库深度指标（evidence 表）。"""
    rows = con.execute("SELECT COUNT(*) FROM evidence").fetchone()[0]
    fact_distinct, fact_top = con.execute("""
        WITH t AS (SELECT fact_text, COUNT(*) AS c FROM evidence GROUP BY 1)
        SELECT (SELECT COUNT(*) FROM t), COALESCE(MAX(c), 0) FROM t
    """).fetchone()
    upd_top = con.execute("""
        WITH t AS (SELECT updated_at, COUNT(*) AS c FROM evidence GROUP BY 1)
        SELECT COALESCE(MAX(c), 0) FROM t
    """).fetchone()[0]
    return {
        "rows": rows,
        "fact_distinct": fact_distinct,
        "fact_max_pct": (fact_top / rows) if rows else 0.0,
        "upd_max_pct": (upd_top / rows) if rows else 0.0,
    }


def evaluate_claims(stats, snap, no_snap_note=None):
    """claims 深度判决：返回 (verdict, reasons)。verdict ∈ PASS/WARN/FAIL。"""
    reasons = []
    verdict = "PASS"

    def bump(v):
        nonlocal verdict
        order = {"PASS": 0, "WARN": 1, "FAIL": 2}
        if order[v] > order[verdict]:
            verdict = v

    if stats["fact_max_pct"] > S1_FAIL:
        bump("FAIL")
        reasons.append("S1 fact_text 单值集中 {:.1%} > {:.0%}（广播形态高危）".format(stats["fact_max_pct"], S1_FAIL))
    elif stats["fact_max_pct"] > S1_WARN:
        bump("WARN")
        reasons.append("S1 fact_text 单值集中 {:.1%} > {:.0%}（需人工目验）".format(stats["fact_max_pct"], S1_WARN))

    if snap:
        sd = snap.get("claims", {}).get("fact_distinct")
        if sd and stats["fact_distinct"] < sd * S2_RATIO:
            bump("FAIL")
            reasons.append("S2 fact_text distinct 骤降 {} < 快照 {} × {}".format(stats["fact_distinct"], sd, S2_RATIO))

    if stats["upd_max_pct"] > S3_FAIL:
        bump("FAIL")
        reasons.append("S3 updated_at 单值集中 {:.1%} > {:.0%}（全表同刻写入特征）".format(stats["upd_max_pct"], S3_FAIL))

    if snap:
        sr = snap.get("claims", {}).get("rows")
        if sr and stats["rows"] < sr * S4_RATIO:
            bump("FAIL")
            reasons.append("S4 evidence 行数骤降 {} < 快照 {} × {}".format(stats["rows"], sr, S4_RATIO))
    else:
        reasons.append(no_snap_note or "（首次运行：无快照，仅执行绝对判据；本次结果将写入基线）")
    return verdict, reasons


def collect_db_stats(con):
    """通用库指标：逐表行数。"""
    tables = {}
    rows = con.execute(
        "SELECT table_name FROM information_schema.tables WHERE table_schema='main' ORDER BY table_name"
    ).fetchall()
    for (t,) in rows:
        tables[t] = con.execute('SELECT COUNT(*) FROM main."{}"'.format(t)).fetchone()[0]
    return tables


def evaluate_generic(name, tables, snap_dbs):
    """通用库判决：G1 表消失 / G2 总行数骤降。返回 (verdict, reasons)。"""
    reasons = []
    verdict = "PASS"
    total = sum(tables.values())
    prev = (snap_dbs or {}).get(name)
    if prev:
        prev_tables = prev.get("tables", {})
        missing = [t for t in prev_tables if t not in tables]
        if missing:
            verdict = "FAIL"
            reasons.append("G1 表消失：{}".format("、".join(missing[:5])))
        pt = prev.get("total_rows")
        if pt and total < pt * G2_RATIO:
            verdict = "FAIL"
            reasons.append("G2 总行数骤降 {} < 快照 {} × {}".format(total, pt, G2_RATIO))
    if not reasons:
        reasons.append("表 {} 张、总行数 {}".format(len(tables), total))
    return verdict, reasons


def _connect(path):
    import duckdb
    return duckdb.connect(path, read_only=True)


def _check_file(path, label, snap, write_state, state_writer=None, state_target=None,
                no_snap_note=None, header_lines=None):
    """对任意 duckdb 文件执行门禁检查（自动探测 claims 深度面）。

    state_writer 为 None 时走生产快照 save_state()（--db 原行为）；--path 传入
    save_path_baseline 的偏函数，只写绑定快照。
    """
    try:
        con = _connect(path)
    except Exception as e:
        print("[FAIL-open] 无法连接 {}：{}".format(label, str(e)[:120]))
        print("提示：目标被写连接占用时属正常操作态——待其结束后重试；门禁未通过前禁写。")
        return 1
    # 存储版本：唯一合法读法是 duckdb_databases().tags（2.0.0 起文件头偏移 12 为弃用哨兵 999，
    # 见流程规则“存储版本的读取口径”）；读不到记 unknown，不臆测、不影响裁决。
    try:
        _tags = con.execute(
            "SELECT tags FROM duckdb_databases() WHERE database_name = current_database()").fetchone()[0]
        storage_version = dict(_tags).get("storage_version", "unknown") if _tags else "unknown"
    except Exception:
        storage_version = "unknown"
    tables = collect_db_stats(con)
    has_claims = False
    if "evidence" in tables:
        cols = [c[0] for c in con.execute("DESCRIBE main.evidence").fetchall()]
        has_claims = "fact_text" in cols
    print("== claimdb_guard · {} ==".format(label))
    print("  存储版本={}  引擎={}".format(storage_version, __import__("duckdb").__version__))
    for line in (header_lines or []):
        print("  {}".format(line))
    if has_claims:
        stats = collect_claims_stats(con)
        verdict, reasons = evaluate_claims(stats, snap, no_snap_note)
        print("  行数={rows}  distinct={fact_distinct}  单值占比={fact_max_pct:.4%}  updated_at 单值占比={upd_max_pct:.4%}".format(**stats))
    else:
        verdict, reasons = evaluate_generic(label, tables, snap.get("dbs", {}))
    for r in reasons:
        print("  - {}".format(r))
    print("  裁决: {}".format(verdict))
    con.close()
    if write_state and verdict != "FAIL":
        if has_claims:
            snap["claims"] = {k: stats[k] for k in ("rows", "fact_distinct", "fact_max_pct", "upd_max_pct")}
        snap.setdefault("dbs", {})[label] = {
            "total_rows": sum(tables.values()), "tables": tables,
            "at": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")}
        if state_writer is None:
            save_state(snap)
            print("  快照已刷新 -> {}".format(STATE))
        else:
            status = state_writer(snap)
            if status == "written":
                print("  绑定快照已刷新 -> {}".format(state_target))
            elif status == "unchanged":
                print("  绑定快照无变化（内容相同，未写盘） -> {}".format(state_target))
            else:
                print("  [降级] 绑定快照目录不可写（{}）——本次仅执行绝对判据，不落基线".format(state_target))
    return 1 if verdict == "FAIL" else 0


def run_db(name):
    scope = load_scope()
    if name not in scope:
        print("未知库名: {}（可用：{}）".format(name, ", ".join(sorted(scope))))
        return 1
    return _check_file(os.path.join(BASE, scope[name]), name, load_state(), True)


def run_path(path, state_dir=None):
    """测试模式：对任意库文件只读检查；基线绑定被检文件自身。

    键＝被检文件绝对路径＋内容 SHA-256，快照只存在 script/_claimdb_guard_path_state/
    （--path-state-dir 可覆盖），绝不读写生产快照 claimdb_guard_state.json。
    首次（无基线）判 PASS 并明示；目录不可写时降级为无基线，退出码不变。
    """
    if not os.path.exists(path):
        print("文件不存在: {}".format(path))
        return 1
    abs_path = os.path.abspath(path)
    try:
        file_sha = _sha256_file(abs_path)
    except OSError as e:
        print("无法读取文件（SHA-256 计算失败）：{}".format(str(e)[:120]))
        return 1
    label = os.path.basename(abs_path)
    sdir = state_dir or default_path_state_dir()
    snap, state_fp, note = load_path_baseline(sdir, abs_path, file_sha)
    try:
        os.makedirs(sdir, exist_ok=True)
        writable = True
    except OSError:
        writable = False
    header = ["文件 SHA-256={}".format(file_sha),
              "绑定快照={}{}".format(state_fp, "（已有基线）" if snap else "（无基线）")]
    if note:
        header.append(note)
    if not writable:
        header.append("[降级] 绑定快照目录不可写（{}）——本次仅执行绝对判据，不落基线".format(sdir))
    return _check_file(
        abs_path, "{}（--path）".format(label), snap, writable,
        state_writer=(lambda s: save_path_baseline(sdir, abs_path, file_sha, s)) if writable else None,
        state_target=state_fp,
        no_snap_note=PATH_NO_SNAP_NOTE if writable else PATH_NO_SNAP_NOTE_DEGRADED,
        header_lines=header)


def run_all():
    scope = load_scope()
    snap = load_state()
    # 快照 dbs 只保留本轮 SCOPE 内的条目：库被移出 SCOPE 或本轮 SKIP 时，旧行数不得
    # 滞留——滞留会让下方的通过/跳过计数被陈旧条目污染（2026-10-15 复核坐实）。
    dbs = {k: v for k, v in (snap.get("dbs") or {}).items() if k in scope}
    fails, skips = [], []
    print("== claimdb_guard · --all 全库体检（{} 库）==".format(len(scope)))
    for name in sorted(scope):
        path = os.path.join(BASE, scope[name])
        try:
            con = _connect(path)
            tables = collect_db_stats(con)
            con.close()
        except Exception as e:
            print("  {:<24} SKIP（{}）".format(name, str(e)[:60]))
            skips.append(name)
            continue
        verdict, reasons = evaluate_generic(name, tables, dbs)
        total = sum(tables.values())
        mark = {"PASS": "OK  ", "FAIL": "FAIL"}[verdict]
        print("  {:<24} {} 表 {} 行 {}".format(name, mark, len(tables), total))
        for r in reasons:
            if verdict == "FAIL":
                print("        - {}".format(r))
        if verdict == "FAIL":
            fails.append(name)
        else:
            dbs[name] = {"total_rows": total, "tables": tables, "at": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")}
    if fails:
        print("== 裁决: FAIL（{}）——修复前禁写 ==".format("、".join(fails)))
        return 1
    snap["dbs"] = dbs
    save_state(snap)
    print("== 裁决: PASS（{}/{} 库通过，{} SKIP；快照已刷新）==".format(len(dbs), len(scope), len(skips)))
    return 0


def selftest():
    import duckdb
    print("== claimdb_guard · selftest ==")
    fails = []

    def report(name, verdict, reasons, want_verdict, want_kw=None, want_kw2=None):
        ok = verdict == want_verdict
        if want_kw:
            ok = ok and any(want_kw in r for r in reasons)
        if want_kw2:
            ok = ok and any(want_kw2 in r for r in reasons)
        print("  [{}] {}：裁决={} {}".format("PASS" if ok else "FAIL", name, verdict, "（原因命中判据）" if ok else ("——期望 {} / 原因 {}".format(want_verdict, reasons))))
        if not ok:
            fails.append(name)

    # 用例 1a：正常态（无快照，全链）
    con = duckdb.connect(":memory:")
    con.execute("CREATE TABLE evidence (evidence_id VARCHAR, fact_text VARCHAR, updated_at VARCHAR)")
    con.executemany(
        "INSERT INTO evidence VALUES (?, ?, ?)",
        [("E{:05d}".format(i), "fact-{}".format(i), "2026-01-{:02d} 00:00:00".format(i % 28 + 1)) for i in range(500)],
    )
    stats = collect_claims_stats(con)
    v, r = evaluate_claims(stats, None)
    report("正常态（无快照）", v, r, "PASS")
    # 用例 1b：正常态（有近值快照）
    v, r = evaluate_claims(stats, {"claims": {"rows": 480, "fact_distinct": 480}})
    report("正常态（有快照）", v, r, "PASS")
    # 用例 2：广播态（全链：同值 fact_text + 同刻 updated_at）
    con2 = duckdb.connect(":memory:")
    con2.execute("CREATE TABLE evidence (evidence_id VARCHAR, fact_text VARCHAR, updated_at VARCHAR)")
    con2.executemany(
        "INSERT INTO evidence VALUES (?, ?, ?)",
        [("B{:05d}".format(i), "同一句广播文本", "2026-10-13 08:52:13") for i in range(2000)],
    )
    stats2 = collect_claims_stats(con2)
    v, r = evaluate_claims(stats2, None)
    report("广播态", v, r, "FAIL", want_kw="S1", want_kw2="S3")
    # 用例 3：distinct 骤降（对快照）
    stats3 = {"rows": 100000, "fact_distinct": 100, "fact_max_pct": 0.01, "upd_max_pct": 0.01}
    v, r = evaluate_claims(stats3, {"claims": {"rows": 100000, "fact_distinct": 5000}})
    report("distinct 骤降", v, r, "FAIL", want_kw="S2")
    # 用例 4：行数骤减（对快照）
    stats4 = {"rows": 10000, "fact_distinct": 9900, "fact_max_pct": 0.001, "upd_max_pct": 0.001}
    v, r = evaluate_claims(stats4, {"claims": {"rows": 100000, "fact_distinct": 99000}})
    report("行数骤减", v, r, "FAIL", want_kw="S4")

    # 用例 5：--path 绑定快照（TD-016 第 1 项）——20 行合成库必须 PASS，
    # 且生产快照 SHA-256 前后一致（本用例只在临时目录读写）。
    import contextlib
    import io
    import shutil
    import tempfile
    tmpdir = tempfile.mkdtemp(prefix="claimdb_guard_path_")
    try:
        dbp = os.path.join(tmpdir, "path20.duckdb")
        c5 = duckdb.connect(dbp)
        c5.execute("CREATE TABLE evidence (evidence_id VARCHAR, fact_text VARCHAR, updated_at VARCHAR)")
        c5.executemany(
            "INSERT INTO evidence VALUES (?, ?, ?)",
            [("P{:05d}".format(i), "fact-path-{}".format(i), "2026-10-{:02d} 09:00:00".format(i + 1))
             for i in range(20)],
        )
        c5.close()
        sha_before = _sha256_file(STATE) if (STATE and os.path.exists(STATE)) else "(不存在)"
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc5 = run_path(dbp, state_dir=os.path.join(tmpdir, "_state"))
        out5 = buf.getvalue()
        sha_after = _sha256_file(STATE) if (STATE and os.path.exists(STATE)) else "(不存在)"
        first_run_hint = "首次运行：无基线" in out5
        ok5 = (rc5 == 0) and first_run_hint and (sha_before == sha_after)
        print("  [{}] --path 20 行合成库：退出码={}（期望 0）首次运行提示={} 生产快照 SHA-256 {}".format(
            "PASS" if ok5 else "FAIL", rc5, "有" if first_run_hint else "无",
            "前后一致" if sha_before == sha_after else "前后不一致"))
        print("        生产快照 before={} after={}".format(sha_before, sha_after))
        for line in out5.rstrip("\n").splitlines():
            print("        | {}".format(line))
        if not ok5:
            fails.append("--path 20 行合成库")
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)

    if fails:
        print("== selftest: FAIL（{}）==".format("、".join(fails)))
        return 1
    print("== selftest: 全部通过（6 项检查：正常×2/广播/骤降/骤减/--path 20 行，拦下原因命中判据）==")
    return 0


def show():
    snap = load_state()
    if not snap:
        print("（无快照：尚未运行过）")
        return 0
    print("== claimdb_guard 快照（{}）==".format(snap.get("updated_at")))
    c = snap.get("claims")
    if c:
        print("  claims: 行={rows} distinct={fact_distinct} 单值占比={fact_max_pct:.4%} upd单值占比={upd_max_pct:.4%}".format(**c))
    for name, d in sorted(snap.get("dbs", {}).items()):
        print("  {:<24} 表 {} 行 {}（{}）".format(name, len(d.get("tables", {})), d.get("total_rows"), d.get("at", "")))
    return 0


def main():
    ap = argparse.ArgumentParser(description="写库门禁与全库健康哨兵（2026-10-14 立；2026-10-16 补仓库根解析）")
    ap.add_argument("--base", metavar="<仓库根>",
                    help="显式指定仓库根（默认 D:\\librebsd，回落 UNC 别名；不可达即报错退出码 2）")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--db", metavar="<库名>", help="单库门禁检查（historical_claims 为深度哨兵 S1–S4）")
    g.add_argument("--path", metavar="<库文件>", help="对任意 duckdb 文件做只读检查（基线绑定该文件自身，不碰生产快照）")
    g.add_argument("--all", action="store_true", help="全库体检（SCOPE 全库快照对比）")
    g.add_argument("--selftest", action="store_true", help="自检（6 项检查）")
    g.add_argument("--show", action="store_true", help="查看快照")
    ap.add_argument("--path-state-dir", metavar="<目录>", default=None,
                    help="--path 绑定快照目录（默认 script/_claimdb_guard_path_state）")
    ap.add_argument("--skip-version-check", action="store_true",
                    help="跳过 duckdb 版本基线探测（逃生参数；基线修复或已知混版本排查时用）")
    args = ap.parse_args()

    rc = require_duckdb_version(args.skip_version_check)
    if rc:
        return rc

    # 仓库根不可达时禁止静默空转：能自持内存库自证的就跑（--selftest），
    # 其余一律显式退出码 2——哨兵空转比报错危险。
    if args.base:
        if not os.path.isdir(args.base):
            print("[FAIL] --base 不存在：{}".format(args.base))
            return 2
        set_base(args.base)
    elif not BASE_OK and not args.selftest:
        print("[FAIL] 仓库根不可解析：{} 均不可达".format("、".join(BASE_CANDIDATES)))
        print("       门禁禁静默空转（--all 会把逐库 SKIP 报成 PASS）；")
        print("       请先挂载盘符，或用 --base <仓库根> 显式指定。")
        return 2

    if args.selftest:
        return selftest()
    if args.show:
        return show()
    if args.all:
        return run_all()
    if args.path:
        return run_path(args.path, args.path_state_dir)
    return run_db(args.db)


if __name__ == "__main__":
    sys.exit(main())
