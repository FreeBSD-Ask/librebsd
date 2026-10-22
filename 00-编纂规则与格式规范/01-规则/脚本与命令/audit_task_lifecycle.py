# -*- coding: utf-8 -*-
"""audit_task_lifecycle.py —— 第三十二件门禁：任务强制审计、复核与轮替。

对象
----
- `01-项目管理/02-工程决策与技术债/任务审计台账.md`：任务准入、复核轮次、收口与轮替主表
- `01-项目管理/02-工程决策与技术债/任务复核台账.md`：复核逐轮明细
- `01-项目管理/02-工程决策与技术债/软件工程理论缺口与增补登记.md`：TG 缺口与采纳状态
- `.trae/specs/<slug>/`：生效后新任务的扫描面
- `01-项目管理/01-编纂规划与报告归档/长线任务归档总登记表/13-任务审计与复核轮替/`：轮替件

判据
----
L1 台账存在与表头
L2 已启动的新任务有准入行（以“已启动”为界；未启动 spec 免准入并计入 SKIP，
   见 ADR-0013 与《工程实践规则》§0.1 第 1 条）
L3 已收口任务有收口行
L4 字段齐全、起算日不早于生效日
L5 枚举合法
L6 任务 ID 唯一
L7 复核轮次与角色合规（普通 ≥2、高风险 ≥3；作者不得自批；高风险须主理人签收）。
   轮次充足性（实有 ≥ 声明 ≥ 最低）、轮次编号连续性与主理人签收以“收口”为界
   （收口结论 ∈ {PASS, 不适用}）：已收口行不足即 FAIL，未收口（在途）行不足只记
   WARN、不影响退出码；声明轮次 < 最低轮次对全部行 FAIL（声明即最低义务）；轮次非
   整数、作者自批、轮次编号重复对全部行判 FAIL（见 ADR-0014）
L8 复核记录字段与引用一致
L9 轮替阈值与指针
L10 轮替件逐字、主表无全文、未收口任务未迁出
L11 规则与登记接线
L12 理论适用性非空且引用的 TG 在缺口登记中存在并有采纳状态

用法
----
    python audit_task_lifecycle.py                 # 0 通过 / 1 不通过 / 2 台账或扫描面缺失
    python audit_task_lifecycle.py --selftest      # 判据非空自检（十九例：3 正样本 + 15 负向夹具 + 1 口径边界例）
    python audit_task_lifecycle.py --list          # 打印检查对象与表头

依赖：仅标准库。
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import pathlib
import re
import sys
import tempfile

sys.stdout.reconfigure(encoding="utf-8")

REPO = pathlib.Path(__file__).resolve().parents[3]

EFFECTIVE = dt.date(2026, 10, 22)
AUDIT_COLS = [
    "任务 ID", "任务名", "类型", "风险级别", "承担者", "起算日", "准入结论", "准入证据",
    "复核轮次", "最新复核 ID", "理论适用性", "收口结论", "收口证据",
    "changelog", "复审触发",
]
REVIEW_COLS = [
    "复核 ID", "任务 ID", "轮次", "角色", "时间", "输入版本", "判据",
    "结论", "发现项", "处置", "证据",
]
TG_COLS = [
    "编号", "理论条款", "不满足处", "项目证据", "增补或修订建议",
    "落地载体", "优先级", "采纳状态", "失效条件", "复审触发",
]
TYPES = {
    "纯文档", "缺陷修复", "需求／范围", "平台／依赖", "紧急修复",
    "内容编纂", "数据迁移", "外部采集", "AI 生成", "长线战役",
}
RISKS = {"普通", "高风险"}
ADMIT = {"PASS", "FAIL"}
CLOSE = {"PASS", "FAIL", "未收口", "不适用"}
REVIEW_VERDICT = {"PASS", "FAIL", "不适用"}
ROLES = {"作者", "复核子代理", "独立复核", "主理人"}
TG_STATUS = {"采纳", "部分采纳", "不采纳", "待定"}
PLACEHOLDER = {"", "—", "-", "／", "/", "待复核", "复核中"}


def _read(path: pathlib.Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def _split_row(line: str) -> list[str]:
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in s.split("|")]


def _parse_table(path: pathlib.Path, required: list[str], exact: list[str] | None = None):
    text = _read(path)
    lines = text.splitlines()
    for idx, line in enumerate(lines):
        if not line.strip().startswith("|"):
            continue
        cells = _split_row(line)
        if all(c in cells for c in required):
            if exact and cells != exact:
                return None, [], "表头不符：期望 %s；实际 %s" % (
                    "／".join(exact), "／".join(cells))
            rows = []
            for line2 in lines[idx + 1:]:
                if not line2.strip().startswith("|"):
                    break
                cells2 = _split_row(line2)
                if cells2 and all(re.fullmatch(r":?-+:?", c) for c in cells2):
                    continue
                if len(cells2) < len(cells):
                    cells2 = cells2 + [""] * (len(cells) - len(cells2))
                row = dict(zip(cells, cells2))
                row["__raw__"] = line2.strip()
                rows.append(row)
            return cells, rows, None
    return None, [], "未找到含 %s 的表" % "／".join(required)


def _parse_rotation(path: pathlib.Path):
    return _parse_table(path, ["轮替日期", "归档指针", "源行哈希"], None)


def _quarter(d: dt.date) -> str:
    return "%d-Q%d" % (d.year, (d.month - 1) // 3 + 1)


def _parse_date(value: str):
    try:
        return dt.date.fromisoformat(value.strip())
    except (ValueError, AttributeError):
        return None


def _is_placeholder(value: str) -> bool:
    return value.strip() in PLACEHOLDER


def _slug_date(slug: str):
    m = re.search(r"(20\d{2})(\d{2})(\d{2})$", slug)
    if m:
        try:
            return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        except ValueError:
            return None
    m = re.search(r"(20\d{2})-(\d{2})-(\d{2})$", slug)
    if m:
        try:
            return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        except ValueError:
            return None
    return None


def _is_exempt(slug: str, spec: pathlib.Path) -> bool:
    d = _slug_date(slug)
    if d is not None:
        return d < EFFECTIVE
    try:
        return dt.date.fromtimestamp(spec.stat().st_ctime) < EFFECTIVE
    except OSError:
        return True


def _spec_slugs(root: pathlib.Path):
    base = root / ".trae" / "specs"
    if not base.is_dir():
        return []
    out = []
    for d in sorted(base.iterdir()):
        if not d.is_dir():
            continue
        spec = d / "spec.md"
        if not spec.is_file():
            continue
        if _is_exempt(d.name, spec):
            continue
        out.append(d.name)
    return out


def _tasks_state(path: pathlib.Path):
    """返回 None（无任务）或 (总数, 已勾选数)。"""
    text = _read(path)
    boxes = re.findall(r"(?m)^\s*-\s*\[(x|X| )\]", text)
    if not boxes:
        return None
    total = len(boxes)
    done = sum(1 for b in boxes if b.lower() == "x")
    return total, done


def _has_checked_box(path: pathlib.Path) -> bool:
    """tasks.md 是否已有已勾选任务（`- [x]`／`- [X]`），即开工信号。"""
    state = _tasks_state(path)
    return state is not None and state[1] > 0


def _paths(root: pathlib.Path):
    rule_dir = root / "00-编纂规则与格式规范" / "01-规则"
    gov = root / "01-项目管理" / "02-工程决策与技术债"
    archive = (root / "01-项目管理" / "01-编纂规划与报告归档"
               / "长线任务归档总登记表" / "13-任务审计与复核轮替")
    return {
        "audit": gov / "任务审计台账.md",
        "review": gov / "任务复核台账.md",
        "tg": gov / "软件工程理论缺口与增补登记.md",
        "rule": rule_dir / "工程实践规则.md",
        "flow": rule_dir / "流程规则.md",
        "rotation_rule": rule_dir / "任务轮替与归档规则.md",
        "rule_readme": rule_dir / "README.md",
        "cmd_readme": rule_dir / "脚本与命令" / "README.md",
        "agents": root / "AGENTS.md",
        "registry": rule_dir / "脚本与命令" / "audit_gate_registry.py",
        "archive": archive,
        "archive_index": archive / "index.md",
        "specs": root / ".trae" / "specs",
    }


def run_checks(root: pathlib.Path):
    p = _paths(root)
    rows = []

    # L1 台账存在与表头
    missing = [str(x) for x in (p["audit"], p["review"], p["tg"]) if not x.is_file()]
    if missing:
        rows.append(("L1", "台账存在与表头", False, "缺失：%s" % "、".join(missing)))
        return rows
    audit_header, audit_rows, audit_err = _parse_table(p["audit"], ["任务 ID"], AUDIT_COLS)
    review_header, review_rows, review_err = _parse_table(p["review"], ["复核 ID"], REVIEW_COLS)
    tg_header, tg_rows, tg_err = _parse_table(p["tg"], ["编号", "采纳状态"], TG_COLS)
    errs = [e for e in (audit_err, review_err, tg_err) if e]
    rows.append(("L1", "台账存在与表头", not errs, "；".join(errs) if errs else "三表表头齐全"))
    if errs:
        return rows

    audit = [r for r in audit_rows if not _is_placeholder(r.get("任务 ID", ""))]
    review = [r for r in review_rows if not _is_placeholder(r.get("复核 ID", ""))]
    tg = [r for r in tg_rows if not _is_placeholder(r.get("编号", ""))]

    # L2 已启动的新任务有准入行（ADR-0013：以已启动为界，未启动 spec 免准入并计入 SKIP）
    audit_ids = {r.get("任务 ID", "").strip() for r in audit}
    review_task_ids = {r.get("任务 ID", "").strip() for r in review}
    specs = _spec_slugs(root)
    started = [
        s for s in specs
        if _has_checked_box(p["specs"] / s / "tasks.md")
        or s in audit_ids or s in review_task_ids
    ]
    skipped = [s for s in specs if s not in started]
    missing_intake = [s for s in started if s not in audit_ids]
    skip_note = ""
    if skipped:
        skip_note = "；未启动 %d 个计入 SKIP：%s%s" % (
            len(skipped), "、".join(skipped[:10]),
            "…（截断，共 %d 个）" % len(skipped) if len(skipped) > 10 else "")
    head = ("缺准入行：%s" % "、".join(missing_intake) if missing_intake
            else "扫描 %d 个生效后 spec，已启动 %d 个均有准入行" % (len(specs), len(started)))
    rows.append(("L2", "生效后新任务有准入行", not missing_intake, head + skip_note))

    # L3 已收口任务有收口行
    close_bad = []
    for slug in specs:
        state = _tasks_state(p["specs"] / slug / "tasks.md")
        if state is None:
            continue
        total, done = state
        if total == 0 or done < total:
            continue
        row = next((r for r in audit if r.get("任务 ID", "").strip() == slug), None)
        if row is None:
            close_bad.append("%s 无审计行" % slug)
            continue
        if row.get("收口结论", "").strip() != "PASS":
            close_bad.append("%s 收口结论=%s" % (slug, row.get("收口结论", "")))
        elif _is_placeholder(row.get("收口证据", "")) or _is_placeholder(row.get("changelog", "")):
            close_bad.append("%s 缺收口证据或 changelog" % slug)
    rows.append(("L3", "已收口任务有收口行", not close_bad,
                 "；".join(close_bad) if close_bad else "已勾选任务均有 PASS 收口行"))

    # L4 字段齐全、起算日不早于生效日
    required = ["任务 ID", "任务名", "类型", "风险级别", "承担者", "起算日", "准入结论",
                "准入证据", "复核轮次", "最新复核 ID", "理论适用性", "收口结论", "复审触发"]
    field_bad = []
    for r in audit:
        tid = r.get("任务 ID", "")
        # ADR-0014：最新复核 ID 属收口期字段——未收口行允许空值，收口行必须可解析
        open_row = r.get("收口结论", "").strip() not in {"PASS", "不适用"}
        need = [k for k in required if not (k == "最新复核 ID" and open_row)]
        miss = [k for k in need if _is_placeholder(r.get(k, ""))]
        if miss:
            field_bad.append("%s 缺 %s" % (tid, "、".join(miss)))
            continue
        d = _parse_date(r.get("起算日", ""))
        if d is None:
            field_bad.append("%s 起算日不可解析" % tid)
        elif d < EFFECTIVE:
            field_bad.append("%s 起算日 %s 早于生效日" % (tid, d.isoformat()))
        try:
            n = int(r.get("复核轮次", ""))
            if n <= 0:
                field_bad.append("%s 复核轮次非正" % tid)
        except ValueError:
            field_bad.append("%s 复核轮次非整数" % tid)
        if r.get("收口结论", "").strip() in {"PASS", "不适用"}:
            ev = r.get("收口证据", "")
            if _is_placeholder(ev) or _is_placeholder(r.get("changelog", "")):
                field_bad.append("%s 收口 PASS 但缺收口证据或 changelog" % tid)
            else:
                for token in ("prebak=", "已知限制=", "轮替=", "归档="):
                    if token not in ev:
                        field_bad.append("%s 收口证据缺 %s" % (tid, token))
    rows.append(("L4", "字段齐全、起算日合规", not field_bad,
                 "；".join(field_bad) if field_bad else "%d 行字段齐全" % len(audit)))

    # L5 枚举合法
    enum_bad = []
    for r in audit:
        tid = r.get("任务 ID", "")
        if r.get("类型", "") not in TYPES:
            enum_bad.append("%s 类型=%s" % (tid, r.get("类型", "")))
        if r.get("风险级别", "") not in RISKS:
            enum_bad.append("%s 风险级别=%s" % (tid, r.get("风险级别", "")))
        if r.get("准入结论", "") not in ADMIT:
            enum_bad.append("%s 准入结论=%s" % (tid, r.get("准入结论", "")))
        if r.get("收口结论", "") not in CLOSE:
            enum_bad.append("%s 收口结论=%s" % (tid, r.get("收口结论", "")))
    for r in review:
        if r.get("结论", "") not in REVIEW_VERDICT:
            enum_bad.append("%s 复核结论=%s" % (r.get("复核 ID", ""), r.get("结论", "")))
        if r.get("角色", "") not in ROLES:
            enum_bad.append("%s 角色=%s" % (r.get("复核 ID", ""), r.get("角色", "")))
    rows.append(("L5", "枚举合法", not enum_bad,
                 "；".join(enum_bad) if enum_bad else "枚举全部合法"))

    # L6 任务 ID 唯一
    seen = {}
    dup = []
    for r in audit:
        tid = r.get("任务 ID", "")
        if tid in seen:
            dup.append(tid)
        seen[tid] = True
    rows.append(("L6", "任务 ID 唯一", not dup,
                 "重复：%s" % "、".join(sorted(set(dup))) if dup else "无重复"))

    # L7 复核轮次与角色合规（ADR-0014：轮次义务在收口时结算，在途不足只记 WARN）
    review_by_task = {}
    for r in review:
        review_by_task.setdefault(r.get("任务 ID", ""), []).append(r)
    role_bad = []
    role_warn = []
    for r in audit:
        tid = r.get("任务 ID", "")
        rs = review_by_task.get(tid, [])
        try:
            declared = int(r.get("复核轮次", "0") or "0")
        except ValueError:
            declared = None  # 非整数轮次由 L4 判 FAIL，此处不重复计
        risk = r.get("风险级别")
        need = 3 if risk == "高风险" else 2
        settled = r.get("收口结论", "").strip() in {"PASS", "不适用"}
        gate = role_bad if settled else role_warn
        if declared is not None and declared < need:
            role_bad.append("%s 声明 %d 轮、%s 至少 %d 轮" % (tid, declared, risk, need))
        if declared is not None and len(rs) < declared:
            gate.append("%s 声明 %d 轮、实有 %d 轮" % (tid, declared, len(rs)))
        if len(rs) < need:
            gate.append("%s %s 实有 %d 轮、至少 %d 轮" % (tid, risk, len(rs), need))
        if any(x.get("角色") == "作者" for x in rs):
            role_bad.append("%s 存在作者自批" % tid)
        if risk == "高风险" and not any(x.get("角色") == "主理人" for x in rs):
            gate.append("%s 高风险缺主理人签收" % tid)
        nums = []
        for x in rs:
            try:
                nums.append(int(x.get("轮次", "0")))
            except ValueError:
                role_bad.append("%s 轮次非整数" % tid)
        if len(set(nums)) != len(nums):
            role_bad.append("%s 轮次编号重复 %s" % (tid, nums))
        elif nums and sorted(nums) != list(range(1, len(nums) + 1)):
            gate.append("%s 轮次不连续 %s" % (tid, nums))
    if role_bad:
        detail = "；".join(role_bad)
        if role_warn:
            detail += "｜WARN 在途未足（不判 FAIL）：" + "；".join(role_warn)
    elif role_warn:
        detail = "WARN 在途未足（不判 FAIL）：" + "；".join(role_warn)
    else:
        detail = "轮次与角色合规"
    rows.append(("L7", "复核轮次与角色合规", not role_bad, detail))

    # L8 复核记录字段与引用一致
    ref_bad = []
    review_ids = {r.get("复核 ID", "").strip(): r for r in review}
    for r in audit:
        tid = r.get("任务 ID", "")
        latest = r.get("最新复核 ID", "").strip()
        if not _is_placeholder(latest) and latest not in review_ids:
            ref_bad.append("%s 最新复核 ID 悬空：%s" % (tid, latest))
    for r in review:
        rid = r.get("复核 ID", "")
        if r.get("任务 ID", "").strip() not in audit_ids:
            ref_bad.append("%s 指向未知任务 %s" % (rid, r.get("任务 ID", "")))
        miss = [k for k in ("输入版本", "判据", "结论", "证据") if _is_placeholder(r.get(k, ""))]
        if miss:
            ref_bad.append("%s 缺 %s" % (rid, "、".join(miss)))
    rows.append(("L8", "复核记录字段与引用一致", not ref_bad,
                 "；".join(ref_bad) if ref_bad else "引用与字段一致"))

    # L9 轮替阈值与指针
    audit_bytes = p["audit"].stat().st_size if p["audit"].is_file() else 0
    review_bytes = p["review"].stat().st_size if p["review"].is_file() else 0
    rot_header, rot_rows, rot_err = _parse_rotation(p["audit"])
    rotation = [r for r in rot_rows if not _is_placeholder(r.get("轮替日期", ""))]
    over = len(audit) > 100 or audit_bytes > 200 * 1024 or review_bytes > 200 * 1024
    rot_bad = []
    if over:
        if not rotation:
            rot_bad.append("已超阈值但无轮替记录")
        else:
            for r in rotation:
                ptr = r.get("归档指针", "")
                if _is_placeholder(ptr):
                    rot_bad.append("轮替行缺归档指针")
                elif not (root / ptr).exists():
                    rot_bad.append("归档指针不存在：%s" % ptr)
    quarter_warn = ""
    if not rot_bad:
        current_q = _quarter(dt.date.today())
        closed = [r for r in audit if r.get("收口结论") in {"PASS", "不适用"}]
        covered = {r.get("覆盖季度", "").strip() for r in rotation}
        old_closed = []
        for r in closed:
            d = _parse_date(r.get("起算日", ""))
            if d and _quarter(d) < current_q and _quarter(d) not in covered:
                old_closed.append(r.get("任务 ID", ""))
        if old_closed:
            quarter_warn = "WARN 跨季度未轮替：%s" % "、".join(old_closed)
    rows.append(("L9", "轮替阈值与指针", not rot_bad,
                 "；".join(rot_bad) if rot_bad else
                 (quarter_warn if quarter_warn else
                  ("已超阈值，轮替指针有效" if over else
                   "未超阈值（行 %d／字节 %d／%d）" % (len(audit), audit_bytes, review_bytes)))))

    # L10 轮替件逐字、主表无全文、未收口任务未迁出
    rot_bad2 = []
    if rotation:
        archived_ids = set()
        for r in rotation:
            ptr = r.get("归档指针", "")
            if _is_placeholder(ptr):
                continue
            target = root / ptr
            if not target.exists():
                continue
            fpath = target
            if fpath.is_dir():
                fpath = fpath / "任务审计台账.md"
            h, arows, err = _parse_table(fpath, ["任务 ID"], AUDIT_COLS)
            if err:
                rot_bad2.append("%s 无法解析：%s" % (ptr, err))
                continue
            for a in arows:
                tid = a.get("任务 ID", "").strip()
                if _is_placeholder(tid):
                    continue
                archived_ids.add(tid)
                if a.get("收口结论", "") not in {"PASS", "不适用"}:
                    rot_bad2.append("%s 收录未收口任务 %s" % (ptr, tid))
                expected = r.get("源行哈希", "").strip()
                raw = a.get("__raw__", "")
                if _is_placeholder(expected):
                    rot_bad2.append("%s 轮替行缺源行哈希" % ptr)
                elif hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16] != expected:
                    rot_bad2.append("%s 归档行哈希不符：%s" % (ptr, tid))
        both = sorted(archived_ids & audit_ids)
        if both:
            rot_bad2.append("主表与轮替件双源：%s" % "、".join(both))
    rows.append(("L10", "轮替件完整、无双源", not rot_bad2,
                 "；".join(rot_bad2) if rot_bad2 else
                 ("轮替件 %d 个任务，无双源" % len(archived_ids) if rotation else "无轮替件")))

    # L11 规则与登记接线
    checks = [
        ("工程实践规则", p["rule"], "任务强制审计、复核与轮替"),
        ("流程规则-准入", p["flow"], "任务准入审计"),
        ("流程规则-收口", p["flow"], "任务收口审计"),
        ("流程规则-复核", p["flow"], "独立复核"),
        ("任务轮替规则", p["rotation_rule"], "任务审计与复核台账轮替"),
        ("规则 README", p["rule_readme"], "audit_task_lifecycle.py"),
        ("脚本 README", p["cmd_readme"], "audit_task_lifecycle.py"),
        ("AGENTS", p["agents"], "audit_task_lifecycle.py"),
        ("门禁登记表", p["registry"], "audit_task_lifecycle.py"),
    ]
    wire_bad = [name for name, path, needle in checks if needle not in _read(path)]
    if not p["archive_index"].is_file():
        wire_bad.append("13 号轮替槽 index.md")
    rows.append(("L11", "规则与登记接线", not wire_bad,
                 "缺：%s" % "、".join(wire_bad) if wire_bad else "接线齐全"))

    # L12 理论适用性
    tg_ids = {r.get("编号", "").strip(): r for r in tg}
    tg_bad = []
    for r in audit:
        tid = r.get("任务 ID", "")
        theory = r.get("理论适用性", "").strip()
        if _is_placeholder(theory):
            tg_bad.append("%s 理论适用性为空" % tid)
            continue
        refs = re.findall(r"TG-\d{3}", theory)
        if not refs and theory != "适用":
            tg_bad.append("%s 理论适用性既非“适用”也无 TG 编号" % tid)
        for ref in refs:
            if ref not in tg_ids:
                tg_bad.append("%s 引用悬空 %s" % (tid, ref))
            elif tg_ids[ref].get("采纳状态", "") not in TG_STATUS:
                tg_bad.append("%s 的 %s 采纳状态非法：%s" % (
                    tid, ref, tg_ids[ref].get("采纳状态", "")))
    rows.append(("L12", "理论适用性", not tg_bad,
                 "；".join(tg_bad) if tg_bad else "理论适用性合规"))

    return rows


def _report(rows, title):
    fails = [r for r in rows if not r[2]]
    print("== %s ==" % title)
    for rid, name, ok, detail in rows:
        print("%s %-28s %s" % (rid, name, "PASS" if ok else "FAIL"))
        if detail:
            print("   %s" % detail)
    print("-- 合计：%d 项，FAIL %d --" % (len(rows), len(fails)))
    return 0 if not fails else 1


def _write(path: pathlib.Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def _fixture(root: pathlib.Path, *, intake=True, close=True, field=True, enum=True,
             duplicate=False, author=False, rounds=3, declared=None, risk="高风险",
             dangling_review=False, rotation_double=False, rotation_open=False,
             bad_hash=False, dangling_tg=False, draft=False, review_skip=False,
             open_tasks=False):
    p = _paths(root)
    _write(p["rule"], "任务强制审计、复核与轮替\n")
    _write(p["flow"], "任务准入审计\n任务收口审计\n独立复核\n")
    _write(p["rotation_rule"], "任务审计与复核台账轮替\n")
    _write(p["rule_readme"], "audit_task_lifecycle.py\n")
    _write(p["cmd_readme"], "audit_task_lifecycle.py\n")
    _write(p["agents"], "audit_task_lifecycle.py\n")
    _write(p["registry"], "audit_task_lifecycle.py\n")
    _write(p["archive_index"], "# 13\n")

    tid = "fixture-task-20261022"
    theory = "TG-999" if dangling_tg else "TG-001"
    close_v = "PASS" if close else "未收口"
    declared_n = rounds if declared is None else declared
    latest_id = "RV-1" if rounds > 0 else "—"
    evidence = ("prebak=fixture；已知限制=无；轮替=未触发；归档=fixture"
                if close else "—")
    changelog = "id=1" if close else "—"
    name = "" if not field else "夹具任务"
    type_v = "杂项" if not enum else "需求／范围"
    audit_rows = []
    if intake:
        audit_rows.append(
            "| %s | %s | %s | %s | 主代理 | 2026-10-22 | PASS | spec.md | %d | %s | %s | %s | %s | %s | 2027-01-22 |"
            % (tid, name, type_v, risk, declared_n, latest_id, theory, close_v,
               evidence, changelog))
    if duplicate:
        audit_rows.append(
            "| %s | 重复 | 需求／范围 | 普通 | 复核子代理 | 2026-10-22 | PASS | spec.md | 2 | RV-2 | 适用 | 未收口 | — | — | 2027-01-22 |"
            % tid)
    header = "| " + " | ".join(AUDIT_COLS) + " |\n| " + " | ".join(["---"] * len(AUDIT_COLS)) + " |\n"
    body = "\n".join(audit_rows)
    _write(p["audit"], "# 任务审计台账\n\n" + header + (body + "\n" if body else "") +
           "\n## 轮替记录\n\n| 轮替日期 | 覆盖季度 | 迁出任务数 | 归档指针 | 源行哈希 | changelog |\n"
           "| --- | --- | --- | --- | --- | --- |\n| — | — | — | — | — | — |\n")

    review_rows = []
    for i in range(1, rounds + 1):
        role = "作者" if author and i == 1 else "主理人"
        rid = "RV-1" if i == 1 else "RV-%d" % i
        review_rows.append(
            "| %s | %s | %d | %s | 2026-10-22 | v%d | 判据 | PASS | 无 | 无 | 证据 |"
            % (rid, tid, i, role, i))
    if dangling_review:
        review_rows = [r.replace("RV-1", "RV-X") for r in review_rows]
    if review_skip:
        review_rows = []
    rheader = "| " + " | ".join(REVIEW_COLS) + " |\n| " + " | ".join(["---"] * len(REVIEW_COLS)) + " |\n"
    _write(p["review"], "# 任务复核台账\n\n" + rheader + "\n".join(review_rows) + "\n")

    theader = "| " + " | ".join(TG_COLS) + " |\n| " + " | ".join(["---"] * len(TG_COLS)) + " |\n"
    tg_body = "| TG-001 | G0–G5 | 缺口 | 证据 | 建议 | 规则 | P0 | 采纳 | 失效 | 2027-01-22 |\n"
    _write(p["tg"], "# TG\n\n" + theader + tg_body)

    # draft=True：另造一个“未启动”spec（任务全未勾选、无审计行、无复核行）
    # open_tasks=True：本任务 spec 只勾首条（在途未收口）
    spec_dir = p["specs"] / ("fixture-draft-20261022" if draft else tid)
    _write(spec_dir / "spec.md", "# fixture\n")
    if draft:
        tasks_body = "- [ ] Task 1\n"
    elif open_tasks:
        tasks_body = "- [x] Task 1\n- [ ] Task 2\n"
    else:
        tasks_body = "- [x] Task 1\n"
    _write(spec_dir / "tasks.md", tasks_body)

    if rotation_double or rotation_open:
        arch_dir = p["archive"] / "2026-Q4"
        _write(arch_dir / "index.md", "# archive\n")
        arch_row = (
            "| %s | 归档 | 需求／范围 | 高风险 | 主代理 | 2026-10-22 | PASS | spec | 3 | RV-1 | 适用 | %s | "
            "prebak=fixture；已知限制=无；轮替=未触发；归档=fixture | id=1 | 2027-01-22 |"
            % (tid, "未收口" if rotation_open else "PASS"))
        row_hash = "0" * 16 if bad_hash else hashlib.sha256(arch_row.encode("utf-8")).hexdigest()[:16]
        _write(arch_dir / "任务审计台账.md",
               "# 归档\n\n" + header + arch_row + "\n")
        _write(p["audit"], _read(p["audit"]).replace(
            "| — | — | — | — | — | — |",
            "| 2026-10-22 | 2026-Q4 | 1 | 01-项目管理/01-编纂规划与报告归档/长线任务归档总登记表/13-任务审计与复核轮替/2026-Q4 | %s | id=2 |" % row_hash))


def _selftest():
    print("== audit_task_lifecycle.py --selftest ==")
    cases = [
        ("positive", {}, None),
        ("missing-intake", {"intake": False}, "L2"),
        ("started-without-intake", {"intake": False, "review_skip": True}, "L2"),
        ("unstarted-without-intake", {"draft": True}, None),
        ("missing-close", {"close": False}, "L3"),
        ("missing-field", {"field": False}, "L4"),
        ("bad-enum", {"enum": False}, "L5"),
        ("duplicate-id", {"duplicate": True}, "L6"),
        ("author-self-review", {"author": True}, "L7"),
        ("insufficient-rounds", {"rounds": 2}, "L7"),
        ("ordinary-insufficient-rounds", {"risk": "普通", "rounds": 1}, "L7"),
        ("in-flight-zero-review-warn", {"close": False, "rounds": 0, "declared": 3,
                                        "open_tasks": True}, "!L7"),
        ("closed-highrisk-two-rounds", {"close": True, "rounds": 2, "declared": 3}, "L7"),
        ("closed-highrisk-three-rounds", {"close": True, "rounds": 3, "declared": 3}, None),
        ("dangling-review", {"dangling_review": True}, "L8"),
        ("rotation-double", {"rotation_double": True}, "L10"),
        ("rotation-open", {"rotation_open": True}, "L10"),
        ("rotation-hash-mismatch", {"rotation_double": True, "bad_hash": True}, "L10"),
        ("dangling-tg", {"dangling_tg": True}, "L12"),
    ]
    ok_all = True
    with tempfile.TemporaryDirectory(prefix="atl_selftest_") as tmp:
        root = pathlib.Path(tmp)
        for name, kwargs, expect in cases:
            _fixture(root, **kwargs)
            rows = run_checks(root)
            fails = {rid for rid, _, ok, _ in rows if not ok}
            if expect is None:
                passed = not fails
            elif expect.startswith("!"):
                passed = expect[1:] not in fails
            else:
                passed = expect in fails
            note = ""
            if passed and expect and expect.startswith("!") and fails:
                note = "（%s 未判 FAIL；同夹具另有 %s，非本判据口径）" % (
                    expect[1:], "、".join(sorted(fails)))
            print("%-30s %s%s%s" % (name, "PASS" if passed else "FAIL", note,
                                   "" if passed else "（期望 %s，实际 %s）" % (expect, sorted(fails))))
            ok_all = ok_all and passed
    print("-- 自检：%d/%d --" % (len(cases) - (0 if ok_all else 1), len(cases)))
    return 0 if ok_all else 1


def main():
    ap = argparse.ArgumentParser(description="任务强制审计、复核与轮替门禁（第三十二件）")
    ap.add_argument("--selftest", action="store_true", help="判据非空自检")
    ap.add_argument("--list", action="store_true", help="打印检查对象与表头")
    ap.add_argument("--root", default=None, help="被审计仓库根（默认脚本所在仓库）")
    args = ap.parse_args()

    if args.selftest:
        return _selftest()

    root = pathlib.Path(args.root).resolve() if args.root else REPO
    p = _paths(root)
    if args.list:
        print("仓库根：%s" % root)
        for key in ("audit", "review", "tg", "archive", "specs"):
            print("%-8s %s" % (key, p[key]))
        print("审计表头：%s" % " | ".join(AUDIT_COLS))
        print("复核表头：%s" % " | ".join(REVIEW_COLS))
        return 0

    if not p["audit"].is_file() or not p["review"].is_file() or not p["tg"].is_file():
        print("台账缺失：任务审计台账／任务复核台账／理论缺口登记三件必须存在")
        return 2
    if not p["specs"].is_dir():
        print("扫描面缺失：%s" % p["specs"])
        return 2

    rows = run_checks(root)
    return _report(rows, "任务强制审计、复核与轮替门禁（第三十二件）")


if __name__ == "__main__":
    raise SystemExit(main())
