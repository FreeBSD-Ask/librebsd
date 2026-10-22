#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""outline_writer.py —— 入纲写入器（唯一实现；ADR-0010 执行件）

契约（ADR-0010 §1）
-------------------
1. **宿主权威解析**：宿主＝小节 `.md`；候选来自 `--claim-map` 的 `hosts` 字段或
   `--outline-map`；`multi` 由 narr 宿主列（键经 `--host-map`）消歧。
   缺失／歧义／目标不存在即中止——**禁止按文件名猜**（不得回退到目录内“首个含锚 .md”）。
2. **块级锚点幂等**：判重集合＝扫描面内 `<!-- ROW_MINE: <lib>.messages.<pk> -->` 锚点；
   命中即跳过，并在既有锚点的 `claim_id` 不符时可见告警。文件级判据废止
   （目录化宿主上会重复插入，ADR-0010 §2 实测 +16/20）。
3. **路径覆盖**：显式 `--root`／`--host`／`--claim-map`／`--outline-map`／`--work`／`--ledger`；
   **写点**（root／ledger／host／work／scan-root）经 `commonpath` 断言落在 `--allow-root` 内，
   **读点**（narr／claim-map／outline-map／host-map／candidates／db）落在 `--input-root` 内；
   启动打印两组生效绝对路径（防静默读生产）；沙箱路径不得逃逸。

写盘契约
--------
同目录临时件 → `flush` + `fsync` → `os.replace`；写后断言：新增锚点＝计划数、
每个新键在宿主内恰一次、旧锚集合保留、块文本逐字节可回读、无 BOM／无 CRLF。
失败路径（坏 key／空正文／越界 pk／宿主未解析／claim 悬空／路径越界）→
stdout 可见 `[check]`／`[abort]`、exit 2、**零写入**；任一宿主写入或断言失败 →
回滚本批已写宿主后退出。

语义边界（沿用既有实践，不另立口径）
------------------------------------
- narr 多出 `claim_map` 的行＝register 后剔除／跨批已登记 → 可见计数跳过，不写入；
  pk 落在批号段之外＝坏件（abort）。`claim_map` 多出于 narr 的行同理只作 info 披露。
- 等级优先取 `--db`（`claim.evidence_level` 真值）；`--candidates` 为交叉核对源，二者
  冲突即坏件。块头抬头／纪律串按标签表（默认 `mail2d` 现行线约定；`--labels rule` 切
  《ROW_MINE块体格式规则.md》§四 主理人 2026-09-17 批准映射；`--label-map` 覆盖）。

用法
----
    # 只读核查（不写盘）
    C:/Python314/python.exe outline_writer.py --narr <mount_narr.tsv> \\
        --claim-map <claim_map.json> --candidates <candidates.txt> --lib openbsd_mail --check-only

    # 写入（先 dry-run 看计划，再加 --write）
    C:/Python314/python.exe outline_writer.py --narr ... --claim-map ... --candidates ... \\
        --lib openbsd_mail --anchor ob_b025 --ts 2026-10-22 [--tag "2026-10-22 openbsd_mail 战线"] --write

    # 判据非空自检
    C:/Python314/python.exe outline_writer.py --selftest

退出码：0 成功／dry-run 无坏件；1 自检失败；2 坏件、路径越界、断言失败或依赖缺失。

边界：不改 ROW_MINE 块形（5 行）、claim schema、已落盘块；不做重复块清理；
不替代 F 线块内整行替换写入器（`apply_fixes.py`，见 TD-016／TD-017）。
"""
from __future__ import annotations

import argparse
import datetime as dt
import io
import json
import os
import re
import sys
import tempfile

sys.stdout.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))

ANCHOR_RE = re.compile(r"<!-- ROW_MINE: *([A-Za-z0-9_.\-]+)\.messages\.(\d+) *-->")
CID_RE = re.compile(r"^CL-RM-\d{6}$")
PK_RE = re.compile(r"^[0-9]+$")
LEVELS = ("L1", "L2", "L3", "L4")

# 块头标签表（抬头＋纪律串）。默认 mail2d 线现行约定（与 _outline_fe_b051_20260915.py
# 模板、2026-10 各批已落盘块一致；全库实测 当事人自述×L3 136,813／二手转述×L3 25,158）。
# `rule` 档＝《ROW_MINE块体格式规则.md》§四 主理人 2026-09-17 批准映射。
# 两档差异（L3 抬头／纪律串）已登记披露；改判须主理人裁定（该规则 §七）。
LABELS = {
    "mail2d": {
        "L4": {"head": "当事人自述", "tail": "引用时按 L4 纪律：以上为邮件列表当事人一手自述，属过程性证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。"},
        "L3": {"head": "当事人自述", "tail": "引用时按 L3 纪律：以上为邮件列表当事人陈述，属过程性证据，具体事实与量化结论仍须交叉复核，不得单独引为定论。"},
        "L2": {"head": "当事人自述", "tail": "引用时按 L2 纪律：以上为社区参与者转述或讨论，需以当事人或原始记录复核，仅作语境性参考。"},
        "L1": {"head": "当事人自述", "tail": "引用时按 L1 纪律：本条为背景线索，须持慎重态度，不单独支撑论点。"},
    },
    "rule": {
        "L4": {"head": "当事人自述", "tail": "引用时按 L4 纪律：以上为邮件列表当事人一手自述，属过程性证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。"},
        "L3": {"head": "二手转述", "tail": "引用时按 L3 纪律：以上为邮件列表二手转述，非当事人一手证词，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。"},
        "L2": {"head": "背景性材料", "tail": "引用时按 L2 纪律：以上为背景性材料，非当事人一手证词，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。"},
        "L1": {"head": "存疑材料", "tail": "引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。"},
    },
}

BANNED = ("\u300c", "\u300d", "\u300e", "\u300f", "*", "\\", "|", "\t", "\r")


class Abort(Exception):
    """坏件／越界／断言失败：stdout 已可见，调用方以 exit 2 收口。"""


# ── 路径安全 ────────────────────────────────────────────────────────────
def under(base: str, path: str, what: str) -> str:
    """断言 path 落在 base 内（commonpath），返回 path 的 abspath。"""
    b = os.path.abspath(base)
    p = os.path.abspath(path)
    try:
        common = os.path.commonpath([os.path.normcase(b), os.path.normcase(p)])
    except ValueError:
        common = None
    if common is None or common != os.path.normcase(b):
        raise Abort("[check] 路径越界：%s=%s 不在允许根 %s 内" % (what, p, b))
    return p


def norm_host(rel: str, outline_rel_prefix: str = "05-卷册大纲") -> str:
    """宿主路径归一：反斜杠→正斜杠、去 './'、去 '05-卷册大纲/' 前缀（含绝对路径）。"""
    s = str(rel).strip().replace("\\", "/")
    if os.path.isabs(s):
        try:
            s = os.path.relpath(s, REPO).replace("\\", "/")
        except ValueError:
            raise Abort("[check] 宿主路径不可归一（跨盘/非法绝对路径）：%s" % rel)
    while s.startswith("./"):
        s = s[2:]
    if s.startswith(outline_rel_prefix + "/"):
        s = s[len(outline_rel_prefix) + 1:]
    return s


def looks_path(s: str) -> bool:
    return ("/" in s) or ("\\" in s) or s.endswith(".md")


def chapter_dir_of(host_path: str) -> str:
    """宿主所属章节目录（最小含 '第NNN章' 的祖先）；找不到则取宿主所在目录。"""
    d = os.path.dirname(os.path.abspath(host_path))
    cur = d
    while True:
        if re.match(r"^第\d+章", os.path.basename(cur)):
            return cur
        parent = os.path.dirname(cur)
        if parent == cur:
            return d
        cur = parent


# ── 输入装载 ────────────────────────────────────────────────────────────
def load_json(path: str, what: str):
    try:
        return json.load(io.open(path, encoding="utf-8"))
    except ValueError as ex:
        raise Abort("[check] %s 非合法 JSON：%s（%s）" % (what, path, ex))


def _dedupe(seq):
    """保序去重（R5：hosts:[A,A] 不应判成 multi=2）。"""
    seen, out = set(), []
    for x in seq:
        k = str(x)
        if k not in seen:
            seen.add(k)
            out.append(x)
    return out


def load_claim_map(path: str):
    raw = load_json(path, "--claim-map")
    out = {}
    for k, v in raw.items():
        if isinstance(v, dict):
            hosts = v.get("hosts")
            if isinstance(hosts, str):
                print("[warn] claim_map[%s].hosts 非数组，按单值处理：%r" % (k, hosts[:80]))
                hosts = [hosts]
            elif isinstance(hosts, list):
                hosts = _dedupe(hosts)
            out[str(k)] = {
                "claim_id": str(v.get("claim_id", "")),
                "hosts": hosts,
                "host_status": v.get("host_status"),
                "lib": v.get("lib"),
            }
        else:
            out[str(k)] = {"claim_id": str(v), "hosts": None, "host_status": None, "lib": None}
    return out


def load_outline_map(path: str):
    raw = load_json(path, "--outline-map")
    return {str(k): _dedupe([str(x) for x in v] if isinstance(v, list) else [str(v)])
            for k, v in raw.items()}


def load_host_map(path: str):
    raw = load_json(path, "--host-map")
    return {str(k): str(v) for k, v in raw.items()}


def load_narr(path: str):
    rows = []
    for ln in io.open(path, encoding="utf-8"):
        if not ln.strip():
            continue
        parts = ln.rstrip("\n").split("\t")
        if len(parts) != 3:
            raise Abort("[check] narr 行字段数≠3（%d）：%r" % (len(parts), ln[:80]))
        rows.append((parts[0].strip(), parts[1].strip(), parts[2]))
    return rows


def load_candidates(path: str):
    lv = {}
    for ln in io.open(path, encoding="utf-8"):
        if not ln.strip():
            continue
        p = ln.rstrip("\n").split("|", 2)
        if len(p) < 2:
            raise Abort("[check] candidates 行字段数<2：%r" % ln[:80])
        lv[p[0].strip()] = p[1].strip()
    return lv


def db_levels(db: str, cids):
    """claim_id → (evidence_level, status)。只读连接。"""
    try:
        import duckdb
    except ImportError:
        raise Abort("[check] 依赖缺失：duckdb 不可导入，无法使用 --db")
    con = duckdb.connect(db, read_only=True)
    try:
        out = {}
        cids = sorted(cids)
        for i in range(0, len(cids), 500):
            chunk = cids[i:i + 500]
            q = "SELECT claim_id, evidence_level, status FROM claim WHERE claim_id IN (%s)" % (
                ",".join("?" * len(chunk)))
            for cid, lvl, st in con.execute(q, chunk).fetchall():
                out[str(cid)] = (str(lvl), str(st))
        return out
    finally:
        con.close()


# ── 块与锚点 ────────────────────────────────────────────────────────────
def make_block(lib, pk, cid, level, nar, tag, labels):
    body = nar.strip()
    if body and body[-1] not in "。？！":
        body = body + "。"
    head = labels[level]["head"]
    tail = labels[level]["tail"]
    return ("<!-- ROW_MINE: %s.messages.%s -->\n"
            "**%s**（证据等级：%s，来源：`historical_claims.duckdb.claim.%s`；%s 全库行级遍历考据采纳）\n\n"
            "%s%s" % (lib, pk, head, level, cid, tag, body, tail))


def scan_anchors(scan_root: str):
    """扫描面内锚点 → {(lib,pk): 次数}、锚后 claim_id 列表、首见文件相对路径。"""
    counts, cids, where = {}, {}, {}
    files = []
    for d, _, fs in os.walk(scan_root):
        for f in fs:
            if f.endswith(".md"):
                files.append(os.path.join(d, f))
    files.sort(key=lambda p: os.path.relpath(p, scan_root).replace("\\", "/"))
    for p in files:
        try:
            txt = read_raw(p)
        except OSError:
            continue
        for m in ANCHOR_RE.finditer(txt):
            k = (m.group(1), m.group(2))
            counts[k] = counts.get(k, 0) + 1
            where.setdefault(k, os.path.abspath(p))
            tail = txt[m.end():m.end() + 300]
            mc = re.search(r"claim\.(CL-RM-\d+)", tail)
            if mc:
                cids.setdefault(k, []).append(mc.group(1))
    return counts, cids, where


def read_raw(path: str) -> str:
    """严格读：newline='' 不做换行转换（CRLF 检测与 append-only 前提）。"""
    with io.open(path, encoding="utf-8", newline="") as f:
        return f.read()


def atomic_write(path: str, text: str):
    d = os.path.dirname(path)
    tmp = os.path.join(d, ".%s.tmp-%d" % (os.path.basename(path), os.getpid()))
    try:
        with io.open(tmp, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)
    except OSError:
        try:
            if os.path.exists(tmp):
                os.remove(tmp)
        except OSError:
            pass
        raise


# ── 计划构建（装载 → 体检 → 宿主解析 → 幂等判重） ───────────────────────
def _must_exist(path: str, what: str) -> str:
    if not os.path.isfile(path):
        raise Abort("[check] 输入文件不存在：%s=%s" % (what, path))
    return path


def build_plan(a):
    def abs_work(p):
        """顶层路径：相对路径以仓库根为基准。"""
        return os.path.abspath(p if os.path.isabs(p) else os.path.join(REPO, p))

    allow = abs_work(a.allow_root)
    input_root = abs_work(a.input_root)
    work = abs_work(a.work)
    under(input_root, work, "--work")

    def write_path(p, what):
        """写点：相对路径以 --work 为基准，须落在 --allow-root 内。"""
        full = p if os.path.isabs(p) else os.path.join(work, p)
        return under(allow, full, what)

    root = write_path(a.root, "--root")
    ledger = write_path(a.ledger, "--ledger") if a.ledger else None
    scan_root_fixed = write_path(a.scan_root, "--scan-root") if a.scan_root else None

    def inp(p, what):
        """只读输入：相对 --work 解析；须存在且落在 --input-root（默认仓库根）内。"""
        full = p if os.path.isabs(p) else os.path.join(work, p)
        full = under(input_root, full, what)
        return _must_exist(full, what)

    if scan_root_fixed and not os.path.isdir(scan_root_fixed):
        raise Abort("[check] --scan-root 不是目录：%s" % scan_root_fixed)

    narr_path = inp(a.narr, "--narr")
    cmap_path = inp(a.claim_map, "--claim-map") if a.claim_map else None
    omap_path = inp(a.outline_map, "--outline-map") if a.outline_map else None
    hmap_path = inp(a.host_map, "--host-map") if a.host_map else None
    cand_path = inp(a.candidates, "--candidates") if a.candidates else None
    db_path = inp(a.db, "--db") if a.db else None

    print("[paths] root=%s work=%s ledger=%s scan-root=%s allow-root=%s write=%s"
          % (root, work, ledger or "-", scan_root_fixed or "(per-host chapter)", allow, bool(a.write)))
    print("[inputs] narr=%s claim-map=%s outline-map=%s host-map=%s candidates=%s db=%s"
          % (narr_path, cmap_path or "-", omap_path or "-", hmap_path or "-",
             cand_path or "-", db_path or "-"))

    labels = {k: dict(v) for k, v in LABELS[a.labels].items()}
    if a.label_map:
        lm = load_json(inp(a.label_map, "--label-map"), "--label-map")
        for lvl, spec in lm.items():
            if str(lvl) not in LEVELS:
                raise Abort("[check] --label-map 含未知等级键：%r（合法 %s）" % (lvl, list(LEVELS)))
            if not isinstance(spec, dict) or not str(spec.get("head", "")).strip() \
                    or not str(spec.get("tail", "")).strip():
                raise Abort("[check] --label-map[%s] 缺 head 或 tail（须为非空字符串）" % lvl)
            labels[str(lvl)] = {"head": str(spec["head"]), "tail": str(spec["tail"])}
    print("[info] 标签表=%s（L3→%s）" % (a.labels, labels["L3"]["head"]))

    cmap = load_claim_map(cmap_path) if cmap_path else {}
    omap = load_outline_map(omap_path) if omap_path else {}
    hmap = load_host_map(hmap_path) if hmap_path else {}
    narr = load_narr(narr_path)
    cand = load_candidates(cand_path) if cand_path else {}

    if not cmap and not omap and not hmap:
        raise Abort("[check] 至少须提供 --claim-map／--outline-map／--host-map 之一作为宿主权威映射")

    lib = a.lib
    if not lib:
        libs = {v["lib"] for v in cmap.values() if v.get("lib")}
        if len(libs) == 1:
            lib = libs.pop()
        else:
            raise Abort("[check] 无法唯一判定 --lib（claim_map.lib 取值 %s）；请显式指定"
                        % (sorted(libs) if libs else "空"))

    cids_all = sorted({v["claim_id"] for v in cmap.values() if v["claim_id"]})
    dlv = {}
    if db_path:
        dlv = db_levels(db_path, cids_all)
        print("[check] DB 真值：%d 条 claim_id 命中 %d 条" % (len(cids_all), len(dlv)))

    ckeys = sorted(int(p) for p in cmap if PK_RE.match(p))
    span = (ckeys[0], ckeys[-1]) if ckeys else None
    narr_pks = {p for p, _, _ in narr}

    bad, plan, skipped, unregistered = [], [], [], []

    def add_bad(pk, why):
        bad.append((pk, why))
        print("[check] 坏件 %s：%s" % (pk, why))

    for pk, col2, nar in narr:
        if not PK_RE.match(pk):
            add_bad(pk, "pk 非数字（须 ASCII 数字）")
            continue
        if not nar.strip():
            add_bad(pk, "正文为空")
            continue
        for ch in BANNED:
            if ch in nar:
                add_bad(pk, "正文含禁字符 %r" % ch)
                break
        if any(b[0] == pk for b in bad):
            continue
        if span and not (span[0] <= int(pk) <= span[1]):
            add_bad(pk, "pk 越界（批号段 %d-%d）" % span)
            continue
        entry = cmap.get(pk)
        if entry is None:
            unregistered.append(pk)
            continue
        cid = entry["claim_id"]
        if not CID_RE.match(cid):
            add_bad(pk, "claim_id 形态非法：%r" % cid)
            continue
        if db_path and cid not in dlv:
            add_bad(pk, "claim 不在库：%s" % cid)
            continue
        lv_c = cand.get(pk)
        lv_d = dlv.get(cid, (None, None))[0] if db_path else None
        lv = lv_d or lv_c
        if lv is None:
            add_bad(pk, "等级来源缺失（须 --db 或 --candidates）")
            continue
        if lv not in LEVELS:
            add_bad(pk, "等级非法：%r" % lv)
            continue
        if lv_c and lv_d and lv_c != lv_d:
            add_bad(pk, "等级冲突：candidates=%s／db=%s" % (lv_c, lv_d))
            continue
        # ── 宿主权威解析
        cands, via = [], ""
        if pk in omap:
            cands, via = omap[pk], "outline_map"
            if entry.get("hosts"):
                other = [norm_host(str(x)) for x in entry["hosts"]]
                if sorted(other) != sorted(norm_host(x) for x in cands):
                    print("[warn] 宿主映射分歧（outline_map vs claim_map.hosts）：pk %s，"
                          "取 outline_map=%s（claim_map=%s）" % (pk, cands, other))
        elif entry.get("hosts"):
            cands, via = [str(x) for x in entry["hosts"]], "claim_map.hosts"
        cands = _dedupe([norm_host(x) for x in cands])
        if not cands:
            if col2 in hmap:
                cands, via = [norm_host(hmap[col2])], "host_map"
            elif looks_path(col2) and a.allow_narr_host:
                cands, via = [norm_host(col2)], "narr.path"
                print("[info] pk %s 宿主映射缺失，按 --allow-narr-host 采用 narr 声明路径"
                      "（host_via=narr.path）" % pk)
            elif looks_path(col2):
                add_bad(pk, "宿主未解析（无 claim_map.hosts／outline_map／host_map 映射；"
                            "如确以 narr 宿主列为权威须显式 --allow-narr-host）")
                continue
            else:
                add_bad(pk, "宿主未解析（映射缺失且 narr 宿主列非路径：%r）" % col2)
                continue
        if len(cands) > 1:
            c2 = norm_host(col2) if looks_path(col2) else (
                norm_host(hmap[col2]) if col2 in hmap else None)
            picked = [c for c in cands if c == c2] if c2 is not None else []
            if len(picked) != 1:
                add_bad(pk, "宿主歧义（multi=%d，narr 宿主列未能唯一消歧：%r）" % (len(cands), col2))
                continue
            host_rel, via = picked[0], via + "+narr"
            print("[info] pk %s multi=%d，按 narr 宿主列消歧 → %s" % (pk, len(cands), host_rel))
        else:
            host_rel = cands[0]
            if looks_path(col2) and norm_host(col2) != host_rel:
                add_bad(pk, "映射分歧（权威=%s，narr=%s）" % (host_rel, norm_host(col2)))
                continue
        target = under(root, os.path.join(root, host_rel), "--host")
        if not os.path.isfile(target):
            add_bad(pk, "宿主不存在：%s" % host_rel)
            continue
        plan.append({"pk": pk, "claim_id": cid, "level": lv, "nar": nar,
                     "host_rel": host_rel, "host": target, "via": via, "lib": lib})

    extra = sorted(set(cmap) - narr_pks)
    print("[check] 计划 %d | 通过 %d | 坏件 %d | 跳过（未登记，register 后剔除／跨批）%d"
          % (len(narr), len(plan), len(bad), len(unregistered)))
    if unregistered:
        print("[info] 跳过明细（不写入）：%s%s"
              % (",".join(sorted(unregistered)[:12]), "…" if len(unregistered) > 12 else ""))
    if extra:
        print("[info] claim_map 多出 %d 条未入 narr：%s%s"
              % (len(extra), ",".join(extra[:12]), "…" if len(extra) > 12 else ""))
    if bad:
        raise Abort("[abort] 坏件 %d | 已写 0 | 宿主停摆，未产生任何写入" % len(bad))

    # ── 幂等判重（块级锚点，按扫描面）
    by_host = {}
    for it in plan:
        by_host.setdefault(it["host"], []).append(it)
    scan_cache = {}

    def anchors_for(host):
        scope = scan_root_fixed or chapter_dir_of(host)
        if scope not in scan_cache:
            counts, cids, where = scan_anchors(scope)
            scan_cache[scope] = (counts, cids, where)
            dups = sum(1 for v in counts.values() if v > 1)
            print("[scan] 扫描面 %s：锚点 %d 个／distinct %d；既有重复锚 %d"
                  % (os.path.relpath(scope, root), sum(counts.values()), len(counts), dups))
        counts, cids, where = scan_cache[scope]
        # 权威宿主自身文件必并入判重集合（--scan-root 指偏／指文件时不致漏判宿主内既有锚）
        scope_n = os.path.normcase(os.path.abspath(scope))
        host_n = os.path.normcase(os.path.abspath(host))
        covered = os.path.isdir(scope) and host_n.startswith(scope_n + os.sep)
        if not covered:
            txt = read_raw(host)
            counts = dict(counts)
            cids = {k: list(v) for k, v in cids.items()}
            where = dict(where)
            for m in ANCHOR_RE.finditer(txt):
                k = (m.group(1), m.group(2))
                counts[k] = counts.get(k, 0) + 1
                where.setdefault(k, os.path.abspath(host))
                mc = re.search(r"claim\.(CL-RM-\d+)", txt[m.end():m.end() + 300])
                if mc:
                    cids.setdefault(k, []).append(mc.group(1))
        return counts, cids, where

    have, mismatch, new_total, crossfile = 0, 0, 0, 0
    for host in sorted(by_host):
        items = by_host[host]
        counts, cids, where = anchors_for(host)
        keep = []
        for it in items:
            k = (it["lib"], it["pk"])
            if k in counts:
                have += 1
                seen = cids.get(k, [])
                loc = where.get(k, "")
                if os.path.normcase(loc) != os.path.normcase(os.path.abspath(host)):
                    crossfile += 1
                    if crossfile <= 8:
                        print("[info] 已存在锚点在非权威文件（跳过不写）：%s.messages.%s @ %s"
                              % (it["lib"], it["pk"],
                                 os.path.relpath(loc, root).replace("\\", "/") if loc else "?"))
                if not seen:
                    print("[warn] 已存在锚点但锚点后 300 字内未见 claim 引用（A 型块或格式差异）："
                          "%s.messages.%s" % (it["lib"], it["pk"]))
                elif it["claim_id"] not in seen:
                    mismatch += 1
                    print("[warn] 已存在锚点 claim_id 不符：%s.messages.%s 现存 %s／本批 %s"
                          % (it["lib"], it["pk"], seen, it["claim_id"]))
            else:
                keep.append(it)
        by_host[host] = keep
        new_total += len(keep)
    print("[plan] 计划 %d | 已存在 %d（claim_id 不符 %d；非权威文件命中 %d）| 新增 %d | "
          "判据=块级锚点(扫描面∪权威宿主)"
          % (len(plan), have, mismatch, crossfile, new_total))
    distinct_all = sum(len(c) for c, _i, _w in scan_cache.values())
    if distinct_all == 0 and new_total > 0:
        print("[warn] 扫描面内 0 个既有锚点而本批新增 %d——幂等判据无对照（首写章节目录属正常；"
              "若该章已有块，请检查 --scan-root 指向）" % new_total)

    if a.host:
        host_rel_want = norm_host(a.host)
        matched = False
        for host in list(by_host):
            if os.path.relpath(host, root).replace("\\", "/") == host_rel_want:
                matched = True
            else:
                by_host[host] = []
        if not matched:
            raise Abort("[check] --host 指定的宿主不在本批计划中：%s（零写入）" % host_rel_want)
        new_total = sum(len(v) for v in by_host.values())
        print("[info] --host 过滤：%s → 本批实际写入 %d 块" % (host_rel_want, new_total))

    return {"root": root, "work": work, "ledger": ledger, "labels": labels, "lib": lib,
            "by_host": by_host, "plan": plan, "have": have, "mismatch": mismatch,
            "new_total": new_total}


# ── 写入 ────────────────────────────────────────────────────────────────
def do_write(st, a):
    labels, lib = st["labels"], st["lib"]
    ts = a.ts or dt.date.today().isoformat()
    tag = a.tag or ("%s %s 战线" % (ts, lib))
    total, hosts = 0, 0
    originals, written, log_rows = {}, [], []
    ledger_fh = None
    ledger_existed = os.path.exists(st["ledger"])
    if a.write:
        # 台账可写性前置：打不开即停（零写入，不进入宿主写入环）
        try:
            ledger_fh = io.open(st["ledger"], "a", encoding="utf-8", newline="\n")
        except OSError as ex:
            raise Abort("[check] 台账不可写：%s（%s）——零写入" % (st["ledger"], ex))

    def _close_ledger():
        """关台账；失败路径不得留下本次新建的空台账（R2：零写入须字面成立）。"""
        nonlocal ledger_fh
        if ledger_fh is not None:
            ledger_fh.close()
            ledger_fh = None
        if not ledger_existed:
            try:
                if os.path.exists(st["ledger"]) and os.path.getsize(st["ledger"]) == 0:
                    os.remove(st["ledger"])
                    print("[cleanup] 已删除本次新建的空台账：%s" % st["ledger"])
            except OSError:
                pass

    try:
        for host in sorted(st["by_host"]):
            items = sorted(st["by_host"][host], key=lambda it: int(it["pk"]))
            txt = read_raw(host)
            if txt.startswith("\ufeff") or "\r" in txt:
                raise Abort("[check] 宿主编码违规（BOM／CRLF）：%s"
                            % os.path.relpath(host, st["root"]))
            blocks = [make_block(lib, it["pk"], it["claim_id"], it["level"], it["nar"],
                                 tag, labels) for it in items]
            new_text = txt.rstrip("\n") + "\n\n" + "\n\n".join(blocks) + "\n"
            if blocks:
                originals[host] = txt
            # 写盘（原子）＋写后断言
            if a.write and blocks:
                try:
                    atomic_write(host, new_text)
                except OSError as ex:
                    raise Abort("[check] 写入失败：%s（%s）"
                                % (os.path.relpath(host, st["root"]), ex))
                written.append(host)
                _post_assert(host, txt, items, blocks, st["root"], lib)
            rel = os.path.relpath(host, st["root"]).replace("\\", "/")
            print("%-58s +%-3d total_refs=%d" % (os.path.basename(host)[:56], len(blocks),
                                                 new_text.count("<!-- ROW_MINE:")))
            total += len(blocks)
            if blocks:
                hosts += 1
            for it in items:
                log_rows.append({"ts": ts, "db": lib, "batch": a.anchor, "row_id": int(it["pk"]),
                                 "claim_id": it["claim_id"], "target": rel, "block": "ROW_MINE",
                                 "kind": labels[it["level"]]["head"], "level": it["level"],
                                 "note": it["nar"].strip()[:80]})
    except Abort:
        _rollback(originals, written, st["root"])
        _close_ledger()
        raise
    except OSError as ex:
        _rollback(originals, written, st["root"])
        _close_ledger()
        raise Abort("[check] 写盘 IO 失败并已回滚：%s" % ex)
    print("[assert] 新增锚点 %d／计划 %d" % (total, st["new_total"]))
    print("[done] 写入 %d 块／%d 宿主%s" % (total, hosts, "" if a.write else "（dry-run 未写盘）"))
    if ledger_fh is not None:
        try:
            for r in log_rows:
                ledger_fh.write(json.dumps(r, ensure_ascii=False) + "\n")
            ledger_fh.flush()
            os.fsync(ledger_fh.fileno())
        except OSError as ex:
            _rollback(originals, written, st["root"])
            _close_ledger()
            raise Abort("[check] 台账写入失败并已回滚宿主：%s（%s）" % (st["ledger"], ex))
        _close_ledger()
        if log_rows:
            print("ledger +%d → %s" % (len(log_rows), st["ledger"]))
    return 0


def _post_assert(host, old_text, items, blocks, root, lib):
    """写后断言：append-only 前缀未动、回读逐字节、每键恰一次、锚点增量、编码。"""
    now = read_raw(host)
    rel = os.path.relpath(host, root)
    if now.startswith("\ufeff") or "\r" in now:
        raise Abort("[check] 写后编码违规：%s" % rel)
    prefix = old_text.rstrip("\n") + "\n\n"
    if not now.startswith(prefix):
        raise Abort("[check] 写后断言失败：%s 非 append-only（原内容前缀被改动）" % rel)
    for blk in blocks:
        if blk not in now:
            raise Abort("[check] 写后断块失败（块文本不可回读）：%s" % rel)
    old_anchors = ANCHOR_RE.findall(old_text)
    new_counts = {}
    for m in ANCHOR_RE.finditer(now):
        k = (m.group(1), m.group(2))
        new_counts[k] = new_counts.get(k, 0) + 1
    for it in items:
        n = new_counts.get((lib, it["pk"]), 0)
        if n != 1:
            raise Abort("[check] 写后断言失败：%s 内 %s.messages.%s 出现 %d 次（应恰 1）"
                        % (rel, lib, it["pk"], n))
    delta = sum(new_counts.values()) - len(old_anchors)
    if delta != len(blocks):
        raise Abort("[check] 写后断言失败：%s 锚点增量 %d≠计划 %d" % (rel, delta, len(blocks)))


def _rollback(originals, written, root):
    for host in written:
        try:
            atomic_write(host, originals[host])
            print("[rollback] 已还原 %s" % os.path.relpath(host, root))
        except OSError as ex:
            print("[rollback] 还原失败 %s：%s" % (os.path.relpath(host, root), ex))


def run(a):
    st = build_plan(a)
    if a.check_only:
        print("[check-only] 只读核查完成：计划 %d | 已存在 %d | 新增 %d | 未写盘"
              % (len(st["plan"]), st["have"], st["new_total"]))
        return 0
    if not st["plan"]:
        raise Abort("[check] 计划为空（narr 全部未登记／映射缺失）——拒绝写入，零写入")
    if a.write and not a.anchor:
        raise Abort("[check] --write 须显式 --anchor（台账 batch 字段）")
    return do_write(st, a)


# ── 判据非空自检 ────────────────────────────────────────────────────────
def selftest():
    import contextlib
    import shutil
    ok = True
    tmp = tempfile.mkdtemp(prefix="outline_writer_st_")
    try:
        allow = os.path.join(tmp, "allow")
        outs = os.path.join(allow, "05-卷册大纲")
        chap = os.path.join(outs, "第01卷-x", "第001章-y")
        sec = os.path.join(chap, "001.1-z")
        os.makedirs(sec)
        host_a = os.path.join(sec, "001.1.1-a.md")
        host_b = os.path.join(sec, "001.1.2-b.md")
        hostrel = "05-卷册大纲/第01卷-x/第001章-y/001.1-z/001.1.1-a.md"
        io.open(host_a, "w", encoding="utf-8", newline="\n").write("正文 A。\n")
        io.open(host_b, "w", encoding="utf-8", newline="\n").write("正文 B。\n")
        inp = os.path.join(allow, "_inputs")
        os.makedirs(inp)
        n = 3

        def write_inputs(bad_key=False, empty_narr=False):
            cmap = {str(1000 + i): {"claim_id": "CL-RM-%06d" % (900000 + i), "hosts": [hostrel],
                                    "lib": "stlib"}
                    for i in range(1, n + 1)}
            io.open(os.path.join(inp, "claim_map.json"), "w", encoding="utf-8",
                    newline="\n").write(json.dumps(cmap, ensure_ascii=False, indent=1))
            rows = ["%d\t%s\t第 %d 条演练叙述，用于自检判据非空。" % (1000 + i, hostrel, i)
                    for i in range(1, n + 1)]
            if bad_key:
                # 坏 key 只进 narr／candidates，不进 claim_map——即“claim 不在映射且越界”形态
                rows.append("9999999\t%s\t坏 key 演练叙述，claim 越界。" % hostrel)
            if empty_narr:
                rows[-1] = rows[-1].split("\t")[0] + "\t" + hostrel + "\t"
            io.open(os.path.join(inp, "narr.tsv"), "w", encoding="utf-8",
                    newline="\n").write("\n".join(rows) + "\n")
            cands = ["%d|L4|第 %d 条演练候选摘要。" % (1000 + i, i) for i in range(1, n + 1)]
            if bad_key:
                cands.append("9999999|L4|坏 key 候选。")
            io.open(os.path.join(inp, "candidates.txt"), "w", encoding="utf-8",
                    newline="\n").write("\n".join(cands) + "\n")

        def argv(extra=None, **kw):
            base = ["--narr", os.path.join(inp, "narr.tsv"),
                    "--claim-map", os.path.join(inp, "claim_map.json"),
                    "--candidates", os.path.join(inp, "candidates.txt"),
                    "--lib", "stlib", "--root", outs, "--work", allow,
                    "--ledger", os.path.join(allow, "ledger.jsonl"),
                    "--allow-root", allow, "--input-root", allow,
                    "--anchor", "st_b001", "--ts", "2026-10-22"]
            base += list(extra or [])
            for k, v in kw.items():
                base += ["--" + k.replace("_", "-"), v]
            return base

        def run_case(name, args, want_exit, want_out=()):
            nonlocal ok
            buf = io.StringIO()
            code = 0
            try:
                with contextlib.redirect_stdout(buf):
                    run(parse(args))
            except Abort as ex:
                buf.write(str(ex) + "\n")
                code = 2
            out = buf.getvalue()
            hit = all(s in out for s in want_out)
            judge = "PASS" if (code == want_exit and hit) else "FAIL"
            if code != want_exit or not hit:
                ok = False
                print("[selftest] %s FAIL（exit=%d 期望 %d；缺失输出 %s）"
                      % (name, code, want_exit,
                         [s for s in want_out if s not in out]))
            else:
                print("[selftest] %s PASS（exit=%d）" % (name, code))
            return out

        write_inputs()
        run_case("T1 写入 +3", argv(["--write"]), 0, ["[done] 写入 3 块／1 宿主", "ledger +3"])
        after1 = io.open(host_a, encoding="utf-8").read()
        if after1.count("<!-- ROW_MINE:") != 3:
            ok = False
            print("[selftest] T1b 宿主块数=3 FAIL（实际 %d）" % after1.count("<!-- ROW_MINE:"))
        else:
            print("[selftest] T1b 宿主块数=3 PASS")
        o2 = run_case("T2 幂等二跑 +0", argv(["--write"]), 0, ["[plan] 计划 3 | 已存在 3",
                                                              "[done] 写入 0 块／0 宿主"])
        o3 = run_case("T3 三跑 +0", argv(["--write"]), 0, ["[plan] 计划 3 | 已存在 3",
                                                           "[done] 写入 0 块／0 宿主"])
        if o2 == o3 and after1 == io.open(host_a, encoding="utf-8").read():
            print("[selftest] T4 幂等稳态（二跑≡三跑＋宿主字节不变）PASS")
        else:
            ok = False
            print("[selftest] T4 幂等稳态 FAIL")
        before_bad = io.open(host_a, encoding="utf-8").read()
        write_inputs(bad_key=True)
        run_case("T5 坏 key（越界）→ exit 2", argv(["--write"]), 2,
                 ["pk 越界", "[abort] 坏件 1"])
        if before_bad == io.open(host_a, encoding="utf-8").read():
            print("[selftest] T6 坏件零写入 PASS")
        else:
            ok = False
            print("[selftest] T6 坏件零写入 FAIL")
        write_inputs(empty_narr=True)
        run_case("T7 空正文 → exit 2", argv(["--write"]), 2, ["正文为空", "[abort] 坏件 1"])
        write_inputs()
        run_case("T8 台账越界 → exit 2", argv(["--write", "--ledger",
                                              os.path.join(tmp, "escape.jsonl")]), 2, ["路径越界"])
        # T9 兄弟文件既有锚点：块级判据应识别（文件级会漏）
        with io.open(host_b, "a", encoding="utf-8", newline="\n") as f:
            f.write(make_block("stlib", "1002", "CL-RM-900002", "L4", "占位叙述。",
                               "2026-10-22 stlib 战线", LABELS["mail2d"]) + "\n\n")
        io.open(host_a, "w", encoding="utf-8", newline="\n").write("正文 A。\n")
        run_case("T9 跨文件锚点判重（dry-run 新增 2）", argv(), 0,
                 ["已存在 1（claim_id 不符 0；非权威文件命中 1）| 新增 2",
                  "已存在锚点在非权威文件"])
        if io.open(host_a, encoding="utf-8").read().count("ROW_MINE:") == 0:
            print("[selftest] T9b dry-run 零写入 PASS")
        else:
            ok = False
            print("[selftest] T9b dry-run 零写入 FAIL")
        # T10 claim_id 不符告警
        io.open(host_a, "w", encoding="utf-8", newline="\n").write(
            make_block("stlib", "1001", "CL-RM-111111", "L4", "异号叙述。",
                       "2026-10-22 stlib 战线", LABELS["mail2d"]) + "\n\n")
        run_case("T10 claim_id 不符告警", argv(), 0,
                 ["[warn] 已存在锚点 claim_id 不符",
                  "已存在 2（claim_id 不符 1；非权威文件命中 1）| 新增 1"])
        # T11 计划为空（narr 全部未登记）→ 拒绝写入
        gap = {"1001": {"claim_id": "CL-RM-900001", "hosts": [hostrel], "lib": "stlib"},
               "1003": {"claim_id": "CL-RM-900003", "hosts": [hostrel], "lib": "stlib"}}
        io.open(os.path.join(inp, "claim_map_gap.json"), "w", encoding="utf-8",
                newline="\n").write(json.dumps(gap, ensure_ascii=False, indent=1))
        io.open(os.path.join(inp, "narr_gap.tsv"), "w", encoding="utf-8", newline="\n").write(
            "1002\t%s\t批内未登记项（号段内、不在 claim_map）。\n" % hostrel)
        run_case("T11 计划为空 → exit 2", argv(["--write", "--narr",
                                               os.path.join(inp, "narr_gap.tsv"),
                                               "--claim-map",
                                               os.path.join(inp, "claim_map_gap.json")]), 2,
                 ["计划为空"])
        # T12 CRLF 宿主 → 拒写（F1：newline='' 严格读，禁止静默归一既有行尾）
        io.open(host_a, "w", encoding="utf-8", newline="").write("正文 A。\r\n第二行 A。\r\n")
        before_crlf = io.open(host_a, "rb").read()
        run_case("T12 CRLF 宿主 → exit 2", argv(["--write"]), 2, ["宿主编码违规"])
        if io.open(host_a, "rb").read() == before_crlf:
            print("[selftest] T12b CRLF 宿主零写入 PASS")
        else:
            ok = False
            print("[selftest] T12b CRLF 宿主零写入 FAIL")
        # T13 台账不可写（指向目录）→ 前置停摆、零写入（F2）
        io.open(host_a, "w", encoding="utf-8", newline="\n").write("正文 A。\n")
        before_t13 = io.open(host_a, "rb").read()
        run_case("T13 台账不可写 → exit 2", argv(["--write", "--ledger", allow]), 2,
                 ["台账不可写"])
        if io.open(host_a, "rb").read() == before_t13:
            print("[selftest] T13b 台账前置停摆零写入 PASS")
        else:
            ok = False
            print("[selftest] T13b 台账前置停摆零写入 FAIL")
        # T14 全角数字 pk → 坏件
        io.open(os.path.join(inp, "narr_fullwidth.tsv"), "w", encoding="utf-8",
                newline="\n").write("１００１\t%s\t全角数字 pk。\n" % hostrel)
        run_case("T14 全角数字 pk → exit 2", argv(["--write", "--narr",
                                                  os.path.join(inp, "narr_fullwidth.tsv")]), 2,
                 ["pk 非数字"])
        # T15 narr.path 未授权 → 宿主未解析（须显式 --allow-narr-host）
        cmap_nomap = {k: {"claim_id": v["claim_id"], "lib": "stlib"}
                      for k, v in
                      json.load(io.open(os.path.join(inp, "claim_map.json"),
                                        encoding="utf-8")).items()}
        io.open(os.path.join(inp, "claim_map_nomap.json"), "w", encoding="utf-8",
                newline="\n").write(json.dumps(cmap_nomap, ensure_ascii=False, indent=1))
        run_case("T15 narr.path 未授权 → exit 2",
                 argv(["--write", "--claim-map", os.path.join(inp, "claim_map_nomap.json")]), 2,
                 ["宿主未解析"])
        # T16 label-map 非 JSON → exit 2（R1）
        io.open(os.path.join(inp, "labelmap_bad.json"), "w", encoding="utf-8",
                newline="\n").write("not json {")
        run_case("T16 label-map 非 JSON → exit 2", argv(["--label-map",
                                                        os.path.join(inp, "labelmap_bad.json")]), 2,
                 ["非合法 JSON"])
        # T17 --scan-root 指文件 → exit 2（R4）
        run_case("T17 scan-root 指文件 → exit 2",
                 argv(["--scan-root", os.path.join(inp, "claim_map.json")]), 2,
                 ["--scan-root 不是目录"])
        # T18 hosts:[A,A] 保序去重后按单宿主处理（R5）
        dup = {"1001": {"claim_id": "CL-RM-900001", "hosts": [hostrel, hostrel], "lib": "stlib"}}
        io.open(os.path.join(inp, "claim_map_dup.json"), "w", encoding="utf-8",
                newline="\n").write(json.dumps(dup, ensure_ascii=False, indent=1))
        io.open(os.path.join(inp, "narr_one.tsv"), "w", encoding="utf-8", newline="\n").write(
            "1001\t%s\t单条去重夹具叙述。\n" % hostrel)
        before_t18 = io.open(host_a, encoding="utf-8").read()
        run_case("T18 hosts 重复项去重（dry-run 新增 1）",
                 argv(["--narr", os.path.join(inp, "narr_one.tsv"),
                       "--claim-map", os.path.join(inp, "claim_map_dup.json")]), 0,
                 ["新增 1"])
        if io.open(host_a, encoding="utf-8").read() == before_t18:
            print("[selftest] T18b dry-run 零写入 PASS")
        else:
            ok = False
            print("[selftest] T18b dry-run 零写入 FAIL")
        # T19 失败路径不得留下本次新建的空台账（R2）
        fresh_ledger = os.path.join(allow, "fresh_ledger.jsonl")
        if os.path.exists(fresh_ledger):
            os.remove(fresh_ledger)
        io.open(host_a, "w", encoding="utf-8", newline="").write("正文 A。\r\n")
        run_case("T19 CRLF＋全新台账 → exit 2", argv(["--write", "--ledger", fresh_ledger]), 2,
                 ["宿主编码违规"])
        if not os.path.exists(fresh_ledger):
            print("[selftest] T19b 新建空台账已清理 PASS")
        else:
            ok = False
            print("[selftest] T19b 新建空台账已清理 FAIL")
        # T20 扫描面无既有锚而新增>0 → 可见 warn（R6）
        io.open(host_a, "w", encoding="utf-8", newline="\n").write("正文 A。\n")
        empty_scan = os.path.join(allow, "_empty_scan")
        os.makedirs(empty_scan, exist_ok=True)
        run_case("T20 扫描面无既有锚 → warn", argv(["--scan-root", empty_scan]), 0,
                 ["[warn] 扫描面内 0 个既有锚点而本批新增"])
        print("[selftest] 合计 %s" % ("PASS" if ok else "FAIL"))
        return 0 if ok else 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# ── CLI ─────────────────────────────────────────────────────────────────
def parse(argv=None):
    ap = argparse.ArgumentParser(
        description="入纲写入器（ADR-0010 执行件）：宿主权威解析＋块级锚点幂等＋路径断言＋原子写")
    ap.add_argument("--narr", help="narr TSV：pk<TAB>宿主（路径或键）<TAB>叙述")
    ap.add_argument("--claim-map", help="claim_map JSON（pk→claim_id 或富 schema 含 hosts/lib）")
    ap.add_argument("--outline-map", help="outline_map JSON（pk→宿主路径数组）")
    ap.add_argument("--host-map", help="host_map JSON（narr 宿主列键→宿主路径）")
    ap.add_argument("--candidates", help="候选清单（pk|等级|摘要）——等级来源之一")
    ap.add_argument("--db", help="historical_claims.duckdb（只读；等级真值来源）")
    ap.add_argument("--lib", help="源库名（锚点 lib 段；缺省由 claim_map.lib 唯一判定）")
    ap.add_argument("--root", default=os.path.join(REPO, "05-卷册大纲"), help="大纲根（默认生产）")
    ap.add_argument("--work", default=REPO, help="相对输入／台账路径的解析基准（默认仓库根）")
    ap.add_argument("--ledger",
                    default=os.path.join(REPO, "script", "_db_row_mining", "supplement_log.jsonl"),
                    help="台账 JSONL（默认生产 supplement_log）")
    ap.add_argument("--allow-root", default=REPO, help="写点允许根（commonpath 断言；默认仓库根）")
    ap.add_argument("--input-root", default=REPO,
                    help="读点允许根（--narr/--claim-map/--db 等只读输入；默认仓库根）")
    ap.add_argument("--scan-root", help="幂等扫描面（默认各宿主所在章节目录）")
    ap.add_argument("--host", help="只写该宿主（大纲根相对路径）")
    ap.add_argument("--anchor", help="批标识（台账 batch 字段；--write 必填）")
    ap.add_argument("--tag", help="块头采纳批次（默认 '<ts> <lib> 战线'）")
    ap.add_argument("--ts", help="台账日期（默认当日）")
    ap.add_argument("--labels", choices=sorted(LABELS), default="mail2d",
                    help="块头标签表：mail2d（现行线约定，默认）／rule（ROW_MINE块体格式规则 §四）")
    ap.add_argument("--label-map", help="标签表覆盖 JSON（{等级: {head, tail}}）")
    ap.add_argument("--allow-narr-host", action="store_true",
                    help="允许 narr 宿主列作为唯一权威（无 claim_map.hosts／outline_map／host_map 映射时；"
                         "缺省为拒绝——ADR-0010 §1.1 映射缺失即中止）")
    ap.add_argument("--write", action="store_true", help="写盘（缺省 dry-run）")
    ap.add_argument("--check-only", action="store_true", help="只读核查：不写盘、不建临时件")
    ap.add_argument("--selftest", action="store_true", help="判据非空自检")
    return ap.parse_args(argv)


def main(argv=None):
    a = parse(argv)
    if a.selftest:
        return selftest()
    if not a.narr:
        print("[check] 缺少 --narr（或使用 --selftest）", file=sys.stderr)
        return 2
    if a.write and a.check_only:
        print("[check] --write 与 --check-only 互斥", file=sys.stderr)
        return 2
    try:
        return run(a)
    except Abort as ex:
        print(str(ex))
        return 2


if __name__ == "__main__":
    sys.exit(main())
