#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S05 公理化证明的机器验证器（有限模型穷举）。

对象域：任务书 + specs/006-toolchain-db-standardization 的 48 个对象文件。
方法：把实际仓库快照作为有限模型 M0，逐条判定公理 A01—A18；
      全部 PASS ⇒ 公理集可满足（相对一致性）；
      A03/A11 ⇒ 相对充分性；A12/A13 ⇒ 相对完备性。
本件是证明附件（非项目固定工具、非门禁）；解析器与 sha256 是其信任基座。

用法：
  python verify_axioms.py            # 对真实快照判定并写出证书
  python verify_axioms.py --selftest # 负向夹具：6 种变异必须被检出
  python verify_axioms.py --json     # 只输出 JSON
  python verify_axioms.py --root X   # 指定仓库根（selftest 内部使用）
"""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import sys
import tempfile
from datetime import datetime, timezone, timedelta
from pathlib import Path

SPEC_REL = Path("specs") / "006-toolchain-db-standardization"
TASKBOOK_REL = Path("01-项目管理") / "01-编纂规划与报告归档" / "工具链与数据库标准化-任务书-20261127.md"
EXPECTED_SPEC_IDS = ["M"] + [f"S{i:02d}" for i in range(1, 13)]
EXPECTED_DIRS = [f"S{i:02d}" for i in range(1, 13)]
ROOT_AUX = ["spec.md", "plan.md", "research.md", "data-model.md", "binding.md", "tasks.md", "checklist.md"]
CONTRACTS = [
    "contracts/tool-registry.schema.json",
    "contracts/binding-manifest.schema.json",
    "contracts/quality-scorecard.schema.json",
    "contracts/spec-frontmatter.schema.json",
]
STATUS_ENUM = {"draft", "active", "closed", "superseded"}
NOW = datetime.now(timezone(timedelta(hours=8))).isoformat(timespec="seconds")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_frontmatter(text: str) -> dict:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    data = {}
    for line in m.group(1).split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()
    return data


def parse_goals(value: str) -> list[int]:
    return sorted(int(x) for x in re.findall(r"\d+", value or ""))


def table_rows(text: str, start: str | None = None, end: str | None = None) -> list[str]:
    lines = text.split("\n")
    if start is not None:
        for i, line in enumerate(lines):
            if start in line:
                lines = lines[i:]
                break
    if end is not None:
        for i, line in enumerate(lines):
            if i > 0 and end in line:
                lines = lines[:i]
                break
    return [line for line in lines if line.startswith("|")]


def parse_spec_body(text: str) -> dict:
    fr_rows = []
    for line in text.split("\n"):
        if re.match(r"^\|\s*(FR-M-\d+|S\d{2}-FR-\d+)\s*\|", line):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            fr_rows.append({"id": cells[0].strip("` "), "acceptance": cells[-1] if len(cells) >= 3 else "", "cells": cells})
    for mm in re.finditer(r"^- \*\*((?:FR-M-\d+|S\d{2}-FR-\d+))\*\*：(.*)$", text, re.M):
        fr_rows.append({"id": mm.group(1), "acceptance": mm.group(2).strip(), "cells": [mm.group(1), mm.group(2)]})
    check_rows = []
    for line in text.split("\n"):
        m = re.match(r"^\|\s*\[ \]\s+(C-(?:M|S\d{2})-[A-Z0-9]+)\s*\|", line)
        if m:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            check_rows.append({"id": m.group(1), "source": cells[-1] if len(cells) >= 3 else "", "cells": cells})
    for mm in re.finditer(r"^- \[[ x]\]\s*((?:C-(?:M|S\d{2})-[A-Z0-9]+))\b", text, re.M):
        check_rows.append({"id": mm.group(1), "source": "", "cells": [mm.group(1)]})
    task_ids = set(re.findall(r"^\|\s*(T-(?:M|S\d{2})-[A-Z0-9]+)\s*\|", text, re.M))
    scenarios = len(re.findall(r"^\d+\.\s*(?:\*\*)?Given", text, re.M))
    sc_count = len(re.findall(r"^- \*\*SC-[A-Z0-9-]+\*\*", text, re.M))
    trace = {}
    m = re.search(r"## 10\. 追溯\n(.*?)(?=\n## |\Z)", text, re.S)
    if m:
        block = m.group(1)
        for key, pat in (("goal", r"- \*\*目标\*\*：(.*)"), ("tasks", r"- \*\*任务\*\*：(.*)"), ("checks", r"- \*\*验收\*\*：(.*)")):
            mm = re.search(pat, block)
            trace[key] = mm.group(1).strip() if mm else ""
    trace_goals = set(int(x) for x in re.findall(r"G(\d+)", trace.get("goal", "")))
    trace_task_ids = set(re.findall(r"T-[A-Z0-9-]+", trace.get("tasks", "")))
    trace_check_ids = set(re.findall(r"C-[A-Z0-9-]+", trace.get("checks", "")))
    m7 = re.search(r"## 7\. 追溯（Traceability）\n(.*?)(?=\n## |\Z)", text, re.S)
    m7_goals = set(int(x) for x in re.findall(r"^\|\s*G(\d+)\s*\|", m7.group(1), re.M)) if m7 else set()
    return {
        "fr_rows": fr_rows,
        "check_rows": check_rows,
        "task_ids": task_ids,
        "scenarios": scenarios,
        "sc_count": sc_count,
        "trace": trace,
        "trace_goals": trace_goals,
        "trace_task_ids": trace_task_ids,
        "trace_check_ids": trace_check_ids,
        "m7_goals": m7_goals,
    }


def load(root: Path) -> dict:
    spec_root = root / SPEC_REL
    taskbook_path = root / TASKBOOK_REL
    manifest_rows = []
    binding_path = spec_root / "BINDING.tsv"
    if binding_path.exists():
        import csv

        with binding_path.open(encoding="utf-8", newline="") as fh:
            manifest_rows = list(csv.DictReader(fh, delimiter="\t"))
    specs = {}
    for row in manifest_rows:
        sid = row.get("spec_id", "")
        spec_path = root / row.get("spec_path", "")
        entry = {"row": row, "spec_path": spec_path, "exists": spec_path.exists(), "fm": {}, "body": "", "parsed": {}}
        if spec_path.exists():
            text = spec_path.read_text(encoding="utf-8")
            entry["fm"] = parse_frontmatter(text)
            entry["body"] = text
            entry["parsed"] = parse_spec_body(text)
        entry["tasks_path"] = spec_path.parent / "tasks.md"
        entry["checklist_path"] = spec_path.parent / "checklist.md"
        entry["tasks_exists"] = entry["tasks_path"].exists()
        entry["checklist_exists"] = entry["checklist_path"].exists()
        for key, p in (("tasks", entry["tasks_path"]), ("checklist", entry["checklist_path"])):
            if entry[f"{key}_exists"]:
                t = p.read_text(encoding="utf-8")
                fmk = parse_frontmatter(t)
                entry[f"{key}_fm"] = fmk
                entry[f"{key}_parsed"] = parse_spec_body(t)
            else:
                entry[f"{key}_fm"] = {}
                entry[f"{key}_parsed"] = {}
        specs[sid] = entry
    dirs = sorted(p.name for p in (spec_root / "subspecs").glob("S*") if p.is_dir()) if (spec_root / "subspecs").exists() else []
    dirs = [re.match(r"^(S\d{2})", d).group(1) for d in dirs]
    object_files = set()
    if spec_root.exists():
        for p in spec_root.rglob("*"):
            if p.is_file():
                rel = p.relative_to(spec_root).as_posix()
                if rel.startswith(("axiomatic/", "deliverables/")) or "__pycache__" in rel or rel.endswith(".pyc"):
                    continue
                object_files.add(rel)
    expected_files = set(ROOT_AUX) | set(CONTRACTS) | {"BINDING.tsv"}
    for row in manifest_rows:
        sp_rel = Path(row.get("spec_path", "")).relative_to(SPEC_REL)
        expected_files.add(sp_rel.as_posix())
        expected_files.add((sp_rel.parent / "tasks.md").as_posix())
        expected_files.add((sp_rel.parent / "checklist.md").as_posix())
    tb_text = taskbook_path.read_text(encoding="utf-8") if taskbook_path.exists() else ""
    headings = [line[3:].strip() for line in tb_text.split("\n") if line.startswith("## ")]
    matrix = {}
    matrix_rows = table_rows(tb_text, start="## 三、目标—spec 映射", end="## 四、工作分解与阶段")
    for line in matrix_rows:
        m = re.match(r"^\|\s*G(\d+)", line)
        if m:
            g = int(m.group(1))
            matrix.setdefault(g, set()).update(re.findall(r"S\d{2}", line))
            if g == 12:
                matrix[12].add("CONTRACT" if ("binding.md" in line or "BINDING.tsv" in line or "§16" in line) else "MISSING_CONTRACT")
    m_appendix = re.search(r"manifest sha256：`([a-f0-9]{64})`", tb_text)
    appendix_hash = m_appendix.group(1) if m_appendix else ""
    appendix_rows = []
    for line in table_rows(tb_text, start="## 附录 C"):
        cells = [c.strip().strip("`") for c in line.strip().strip("|").split("|")]
        if len(cells) >= 6 and re.match(r"^(M|S\d{2})$", cells[0]):
            appendix_rows.append({"spec_id": cells[0], "goals": cells[1], "path": cells[2], "version": cells[3], "status": cells[4], "hash_prefix": cells[5]})
    return {
        "root": root,
        "spec_root": spec_root,
        "taskbook_path": taskbook_path,
        "taskbook_text": tb_text,
        "headings": headings,
        "matrix": matrix,
        "appendix_hash": appendix_hash,
        "appendix_rows": appendix_rows,
        "manifest_rows": manifest_rows,
        "manifest_ids": [r.get("spec_id", "") for r in manifest_rows],
        "binding_ids": [r.get("binding_id", "") for r in manifest_rows],
        "specs": specs,
        "dirs": dirs,
        "object_files": object_files,
        "expected_files": expected_files,
        "binding_sha": sha256(binding_path) if binding_path.exists() else "",
    }


def ax(name: str, ok: bool, detail: str) -> dict:
    return {"axiom": name, "pass": bool(ok), "detail": detail}


def evaluate(model: dict) -> list[dict]:
    R = []
    specs = model["specs"]
    rows = model["manifest_rows"]
    ids = model["manifest_ids"]
    goals_all = set(range(1, 13))

    # A01 对象域显式有穷
    ok = ids == EXPECTED_SPEC_IDS and set(specs) == set(EXPECTED_SPEC_IDS) and model["dirs"] == EXPECTED_DIRS
    R.append(ax("A01", ok, f"manifest 13 行＝M+S01—S12；subspecs 目录＝S01—S12（实测 {len(model['dirs'])}）"))

    # A02 标识唯一
    ok = len(ids) == len(set(ids)) and len(model["binding_ids"]) == len(set(model["binding_ids"]))
    R.append(ax("A02", ok, f"spec_id 唯一 {len(set(ids))}/{len(ids)}；binding_id 唯一 {len(set(model['binding_ids']))}/{len(model['binding_ids'])}"))

    # A03 目标覆盖（相对充分性）
    covered = set()
    for row in rows:
        covered.update(parse_goals(row.get("goals", "")))
    R.append(ax("A03", covered == goals_all, f"目标并集＝{sorted(covered)}；缺 {sorted(goals_all - covered)}"))

    # A04 无孤儿 spec
    orphans = [r["spec_id"] for r in rows if not parse_goals(r.get("goals", ""))]
    outside = [r["spec_id"] for r in rows if set(parse_goals(r.get("goals", ""))) - goals_all]
    R.append(ax("A04", not orphans and not outside, f"孤儿 {orphans}；越界 {outside}"))

    # A05 交付件完备（三件套）
    missing = []
    for sid, s in specs.items():
        for label in ("exists", "tasks_exists", "checklist_exists"):
            if not s[label]:
                missing.append(f"{sid}:{label}")
    R.append(ax("A05", not missing, f"13×3 件齐备；缺 {missing}"))

    # A06 绑定双射
    ok = len(rows) == 13 and set(ids) == set(EXPECTED_SPEC_IDS) and len(model["binding_ids"]) == 13
    mismatch = [r["spec_id"] for r in rows if r["spec_id"] not in specs]
    R.append(ax("A06", ok and not mismatch, f"行 13↔spec 13；行指向缺失 {mismatch}"))

    # A07 锚点可定位且唯一
    bad_anchor = []
    for r in rows:
        a = r.get("task_book_anchor", "")
        if model["headings"].count(a) != 1:
            bad_anchor.append(f"{r['spec_id']}:{a}")
    R.append(ax("A07", not bad_anchor, f"13 锚点精确命中任务书小节各 1 次；异常 {bad_anchor}"))

    # A08 哈希完整
    bad_hash = []
    for sid, s in specs.items():
        row = s["row"]
        if not s["exists"] or sha256(s["spec_path"]) != row.get("spec_sha256"):
            bad_hash.append(f"{sid}:spec")
        if not s["tasks_exists"] or sha256(s["tasks_path"]) != row.get("tasks_sha256"):
            bad_hash.append(f"{sid}:tasks")
        if not s["checklist_exists"] or sha256(s["checklist_path"]) != row.get("checklist_sha256"):
            bad_hash.append(f"{sid}:checklist")
    R.append(ax("A08", not bad_hash, f"39 个哈希逐件复算相等；异常 {bad_hash}"))

    # A09 状态一致（frontmatter ↔ 清单）
    bad_status = []
    for sid, s in specs.items():
        row, fm = s["row"], s["fm"]
        pairs = [
            (fm.get("spec_id"), sid),
            (fm.get("task_book"), row.get("task_book_path")),
            (fm.get("task_book_anchor"), row.get("task_book_anchor")),
            (fm.get("version"), row.get("spec_version")),
            (fm.get("status"), row.get("status")),
            (fm.get("binding_id"), row.get("binding_id")),
            (str(parse_goals(fm.get("goals", "[]"))), str(parse_goals(row.get("goals", "")))),
        ]
        for left, right in pairs:
            if left != right:
                bad_status.append(f"{sid}:{left!r}≠{right!r}")
        for key in ("tasks_fm", "checklist_fm"):
            fmk = s[key]
            for field in ("spec_id", "binding_id", "task_book", "version", "status"):
                if fmk.get(field) != fm.get(field):
                    bad_status.append(f"{sid}/{key}:{field}")
    R.append(ax("A09", not bad_status, f"13×(spec+tasks+checklist) 状态一致；异常 {bad_status[:6]}"))

    # A10 清单整合（任务书附录 C）
    ok_hash = model["appendix_hash"] == model["binding_sha"]
    R.append(ax("A10", ok_hash and len(model["appendix_rows"]) == 13, f"附录 C manifest 哈希＝BINDING.tsv sha256（{model['binding_sha'][:12]}…）；行 {len(model['appendix_rows'])}"))

    # A11 结构充分性
    bad_struct = []
    for sid in EXPECTED_DIRS:
        s = specs.get(sid)
        if not s:
            continue
        p = s["parsed"]
        checks = s["checklist_parsed"].get("check_rows", [])
        if len(p["fr_rows"]) < 5:
            bad_struct.append(f"{sid}:FR={len(p['fr_rows'])}<5")
        if p["scenarios"] < 3:
            bad_struct.append(f"{sid}:场景={p['scenarios']}<3")
        if len(checks) < 5:
            bad_struct.append(f"{sid}:check={len(checks)}<5")
        for fr in p["fr_rows"]:
            if not fr["acceptance"]:
                bad_struct.append(f"{sid}:{fr['id']} 无验收判据")
        for c in checks:
            if not c["source"] or not re.search(r"(S\d{2}-FR|FR-M|SC-|§|验收判据|C-)", c["source"]):
                bad_struct.append(f"{sid}:{c['id']} 来源弱")
    m = specs.get("M")
    if m:
        mchecks = m["checklist_parsed"].get("check_rows", [])
        if len(m["parsed"]["fr_rows"]) < 10:
            bad_struct.append(f"M:FR={len(m['parsed']['fr_rows'])}<10")
        if m["parsed"]["sc_count"] < 5:
            bad_struct.append(f"M:SC={m['parsed']['sc_count']}<5")
        if len(mchecks) < 30:
            bad_struct.append(f"M:check={len(mchecks)}<30")
    R.append(ax("A11", not bad_struct, f"12 子 spec 均 ≥5FR/≥3场景/≥5check；M ≥10FR/≥5SC/≥30check；异常 {bad_struct[:6]}"))

    # A12 闭包（相对完备性）
    extra = sorted(model["object_files"] - model["expected_files"])
    ghost = sorted(model["expected_files"] - model["object_files"])
    R.append(ax("A12", not extra and not ghost, f"对象域文件集 48 件闭合；盘外 {extra[:4]}；幽灵 {ghost[:4]}"))

    # A13 单一规范路径
    paths = [(model["root"] / r["spec_path"]).as_posix() for r in rows]
    ok = len(paths) == len(set(paths))
    R.append(ax("A13", ok, f"13 条 spec_path 两两不同"))

    # A14 追溯闭合
    bad_trace = []
    for sid in EXPECTED_DIRS:
        s = specs.get(sid)
        if not s:
            continue
        p = s["parsed"]
        task_ids = s["tasks_parsed"].get("task_ids", set())
        check_ids = {c["id"] for c in s["checklist_parsed"].get("check_rows", [])}
        if not p["trace_goals"] or not p["trace_goals"].issubset(set(parse_goals(s["row"].get("goals", "")))):
            bad_trace.append(f"{sid}:目标 {sorted(p['trace_goals'])}")
        if not p["trace_task_ids"] or not p["trace_task_ids"].issubset(task_ids):
            bad_trace.append(f"{sid}:任务悬空 {sorted(p['trace_task_ids'] - task_ids)[:3]}")
        if not p["trace_check_ids"] or not p["trace_check_ids"].issubset(check_ids):
            bad_trace.append(f"{sid}:验收悬空 {sorted(p['trace_check_ids'] - check_ids)[:3]}")
    m7 = specs.get("M", {}).get("parsed", {}).get("m7_goals", set())
    if m7 != goals_all:
        bad_trace.append(f"M:§7 覆盖 {sorted(m7)}")
    R.append(ax("A14", not bad_trace, f"12 子 spec 追溯目标/任务/验收全闭合；M §7 覆盖 1—12；异常 {bad_trace[:4]}"))

    # A15 任务书矩阵 ↔ 清单覆盖
    bad_matrix = []
    non_m = {g: set() for g in goals_all}
    for r in rows:
        if r["spec_id"] == "M":
            continue
        for g in parse_goals(r.get("goals", "")):
            non_m[g].add(r["spec_id"])
    for g in goals_all:
        if g not in model["matrix"]:
            bad_matrix.append(f"G{g} 缺行")
            continue
        if g <= 11 and model["matrix"][g] != non_m[g]:
            bad_matrix.append(f"G{g}:矩阵 {sorted(model['matrix'][g])}≠清单 {sorted(non_m[g])}")
        if g == 12 and "CONTRACT" not in model["matrix"][12]:
            bad_matrix.append("G12 缺绑定契约指称")
    R.append(ax("A15", not bad_matrix, f"§3 矩阵 12 目标与清单覆盖逐格相等；G12 为绑定契约；异常 {bad_matrix[:4]}"))

    # A16 状态/版本良构
    bad_domain = []
    for sid, s in specs.items():
        row, fm = s["row"], s["fm"]
        if row.get("status") not in STATUS_ENUM:
            bad_domain.append(f"{sid}:status={row.get('status')}")
        if not re.match(r"^\d+\.\d+\.\d+$", row.get("spec_version", "")):
            bad_domain.append(f"{sid}:version={row.get('spec_version')}")
        for field in ("created", "updated"):
            if not re.match(r"^\d{4}-\d{2}-\d{2}$", fm.get(field, "")):
                bad_domain.append(f"{sid}:{field}={fm.get(field)}")
    R.append(ax("A16", not bad_domain, f"13 spec 状态∈枚举、版本 SemVer、日期 ISO；异常 {bad_domain[:4]}"))

    # A17 附录 C 逐行 ↔ 清单
    bad_appendix = []
    by_id = {r["spec_id"]: r for r in rows}
    for arow in model["appendix_rows"]:
        r = by_id.get(arow["spec_id"])
        if not r:
            bad_appendix.append(f"{arow['spec_id']} 无清单行")
            continue
        s = specs[arow["spec_id"]]
        if arow["path"] != r.get("spec_path"):
            bad_appendix.append(f"{arow['spec_id']}:path")
        if arow["version"] != r.get("spec_version") or arow["status"] != r.get("status"):
            bad_appendix.append(f"{arow['spec_id']}:version/status")
        if s["exists"] and not sha256(s["spec_path"]).startswith(arow["hash_prefix"]):
            bad_appendix.append(f"{arow['spec_id']}:hash")
        if set(parse_goals(arow["goals"])) != set(parse_goals(r.get("goals", ""))):
            bad_appendix.append(f"{arow['spec_id']}:goals")
    R.append(ax("A17", not bad_appendix and len(model["appendix_rows"]) == 13, f"附录 C 13 行逐列与清单相等；异常 {bad_appendix[:4]}"))

    # A18 任务书可解析
    required = ["## 一、意图确证（档 A 六字段）", "## 三、目标—spec 映射（追溯矩阵）", "## 十六、任务书—specs 绑定协议（G12）", "## 附录 C：绑定清单摘要"]
    missing_h = [h for h in required if h not in model["taskbook_text"]]
    has_quote = "0、建立任务书和对应的specs" in model["taskbook_text"]
    R.append(ax("A18", not missing_h and has_quote and len(model["taskbook_text"]) > 10000, f"必需节 {len(required)-len(missing_h)}/{len(required)}；用户原话在；{len(model['taskbook_text'])} 字符"))
    return R


THEOREMS = {
    "T1 相对充分性（目标覆盖）": ["A03", "A11"],
    "T2 无孤儿 spec": ["A04"],
    "T3 绑定双射": ["A02", "A06"],
    "T4 哈希完整性": ["A08"],
    "T5 锚点可靠性": ["A07"],
    "T6 状态一致性": ["A09"],
    "T7 清单—任务书整合": ["A10", "A17"],
    "T8 结构充分性": ["A11"],
    "T9 闭包（相对完备性）": ["A01", "A12", "A13"],
    "T10 追溯闭合": ["A14"],
    "T11 矩阵一致性": ["A15"],
    "T12 论域良构": ["A16", "A18"],
}


def theorem_results(axioms: list[dict]) -> list[dict]:
    amap = {a["axiom"]: a for a in axioms}
    out = []
    for name, deps in THEOREMS.items():
        ok = all(amap[d]["pass"] for d in deps)
        out.append({"theorem": name, "pass": ok, "depends": deps})
    return out


def run(root: Path) -> tuple[list[dict], list[dict], dict]:
    model = load(root)
    axioms = evaluate(model)
    theorems = theorem_results(axioms)
    cert = {
        "generated_at": NOW,
        "model": {
            "root": str(root),
            "taskbook_sha256": sha256(root / TASKBOOK_REL) if (root / TASKBOOK_REL).exists() else "",
            "binding_sha256": model["binding_sha"],
            "object_file_count": len(model["object_files"]),
            "spec_count": len(model["specs"]),
        },
        "axioms": axioms,
        "theorems": theorems,
    }
    return axioms, theorems, cert


def write_cert(cert: dict) -> None:
    here = Path(__file__).resolve().parent
    (here / "certificate.json").write_text(json.dumps(cert, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    lines = ["# 公理化判定证书（有限模型穷举）", "", f"生成时间：{cert['generated_at']}"]
    lines += [
        f"- 模型快照：taskbook sha256={cert['model']['taskbook_sha256'][:12]}…；BINDING sha256={cert['model']['binding_sha256'][:12]}…；对象域 {cert['model']['object_file_count']} 件；spec {cert['model']['spec_count']} 个",
        "",
        "| 公理 | 判定 | 摘要 |",
        "| ---- | ---- | ---- |",
    ]
    for a in cert["axioms"]:
        lines.append(f"| {a['axiom']} | {'PASS' if a['pass'] else 'FAIL'} | {a['detail']} |")
    lines += ["", "| 定理 | 判定 | 依赖 |", "| ---- | ---- | ---- |"]
    for t in cert["theorems"]:
        lines.append(f"| {t['theorem']} | {'PASS' if t['pass'] else 'FAIL'} | {'＋'.join(t['depends'])} |")
    all_pass = all(a["pass"] for a in cert["axioms"])
    lines += ["", f"结论：{'一致（模型存在）＋相对充分＋相对完备' if all_pass else '存在 FAIL，见上表'}"]
    (here / "verification_output.txt").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def selftest() -> int:
    src_root = Path(__file__).resolve().parents[3]
    mutations = [
        ("哈希变异", lambda tmp: (tmp / SPEC_REL / "subspecs" / "S01-standards-research" / "spec.md").open("a", encoding="utf-8").write("\n"), {"A08"}),
        ("缺件变异", lambda tmp: (tmp / SPEC_REL / "subspecs" / "S01-standards-research" / "checklist.md").unlink(), {"A05", "A08"}),
        ("锚点变异", lambda tmp: _patch_tsv(tmp, "S01", "task_book_anchor", "不存在的锚点"), {"A07"}),
        ("目标变异", lambda tmp: _patch_tsv(tmp, "M", "goals", "1,2,3,4,5,6,7,8,9,10,11"), {"A03"}),
        ("重复绑定变异", lambda tmp: _patch_tsv(tmp, "S02", "binding_id", "TB-20261127-S01"), {"A02"}),
        ("删行变异", lambda tmp: _drop_tsv_row(tmp, "S12"), {"A01"}),
    ]
    failures = []
    for name, mutate, expect in mutations:
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            shutil.copytree(src_root / SPEC_REL, tmp / SPEC_REL)
            (tmp / TASKBOOK_REL).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(src_root / TASKBOOK_REL, tmp / TASKBOOK_REL)
            mutate(tmp)
            axioms, _, _ = run(tmp)
            got_fail = {a["axiom"] for a in axioms if not a["pass"]}
            if not (expect & got_fail):
                failures.append(f"{name}: 期望 {sorted(expect)} 失败，实测 {sorted(got_fail)}")
    if failures:
        print("SELFTEST FAIL")
        for f in failures:
            print(f"- {f}")
        return 1
    print("SELFTEST PASS：6 种变异全部被对应公理检出")
    return 0


def _patch_tsv(tmp: Path, sid: str, field: str, value: str) -> None:
    p = tmp / SPEC_REL / "BINDING.tsv"
    lines = p.read_text(encoding="utf-8").split("\n")
    header = lines[0].split("\t")
    idx = header.index(field)
    for i, line in enumerate(lines[1:], 1):
        cells = line.split("\t")
        if len(cells) > header.index("spec_id") and cells[header.index("spec_id")] == sid:
            cells[idx] = value
            lines[i] = "\t".join(cells)
    p.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def _drop_tsv_row(tmp: Path, sid: str) -> None:
    p = tmp / SPEC_REL / "BINDING.tsv"
    lines = p.read_text(encoding="utf-8").split("\n")
    header = lines[0].split("\t")
    idx = header.index("spec_id")
    kept = [lines[0]]
    for line in lines[1:]:
        cells = line.split("\t")
        if len(cells) > idx and cells[idx] == sid:
            continue
        kept.append(line)
    p.write_text("\n".join(kept), encoding="utf-8", newline="\n")


def _patch_spec_goals(tmp: Path, sid: str, goals: list[int]) -> None:
    row = None
    import csv

    with (tmp / SPEC_REL / "BINDING.tsv").open(encoding="utf-8", newline="") as fh:
        row = [r for r in csv.DictReader(fh, delimiter="\t") if r["spec_id"] == sid][0]
    p = tmp / row["spec_path"]
    text = p.read_text(encoding="utf-8")
    new = re.sub(r"(?m)^goals: \[.*\]$", "goals: [" + ", ".join(str(g) for g in goals) + "]", text, count=1)
    p.write_text(new, encoding="utf-8", newline="\n")


def main() -> int:
    args = sys.argv[1:]
    if "--selftest" in args:
        return selftest()
    root = Path(args[args.index("--root") + 1]).resolve() if "--root" in args else Path(__file__).resolve().parents[3]
    axioms, theorems, cert = run(root)
    write_cert(cert)
    if "--json" in args:
        print(json.dumps(cert, ensure_ascii=False, indent=2))
    else:
        for a in axioms:
            print(f"[{'PASS' if a['pass'] else 'FAIL'}] {a['axiom']}  {a['detail']}")
        for t in theorems:
            print(f"[{'PASS' if t['pass'] else 'FAIL'}] {t['theorem']}  依赖 {'＋'.join(t['depends'])}")
        all_pass = all(a["pass"] for a in axioms)
        print("结论：" + ("公理集可满足（一致）；相对充分；相对完备" if all_pass else "存在 FAIL"))
    return 0 if all(a["pass"] for a in axioms) else 1


if __name__ == "__main__":
    sys.exit(main())
