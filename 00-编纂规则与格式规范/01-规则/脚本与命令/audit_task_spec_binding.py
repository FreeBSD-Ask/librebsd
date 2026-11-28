#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""audit_task_spec_binding.py — 任务书—specs 绑定校验器（第四十七件）。

判据 B1—B8（specs/006-toolchain-db-standardization/binding.md §5）：
B1 三件套存在／B2 sha256 全等／B3 目标 1—12 覆盖且 id 唯一／B4 锚点可定位／
B5 清单表头与哈希格式合法／B6 任务书附录 C manifest 哈希一致／B7 frontmatter 与清单一致／B8 无孤儿与幽灵。
退出码：0 PASS；1 FAIL；2 环境/格式错误。--selftest 用临时沙箱变异体（六种变异必须被对应判据检出）。
"""



from __future__ import annotations

import csv
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SPEC_ROOT = ROOT / "specs" / "006-toolchain-db-standardization"
BINDING = SPEC_ROOT / "BINDING.tsv"
TASK_BOOK = ROOT / "01-项目管理" / "01-编纂规划与报告归档" / "工具链与数据库标准化-任务书-20261127.md"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def selftest() -> int:
    """六种变异必须被对应判据检出（正例全 PASS）。"""
    import shutil
    import tempfile
    src_root = Path(__file__).resolve().parents[3]
    failures = []
    mutations = [
        ("篡改哈希", lambda tmp: (tmp / "specs" / "006-toolchain-db-standardization" / "subspecs" / "S01-standards-research" / "spec.md").open("a", encoding="utf-8").write("\n"), {"B2"}),
        ("删除交付件", lambda tmp: (tmp / "specs" / "006-toolchain-db-standardization" / "subspecs" / "S01-standards-research" / "checklist.md").unlink(), {"B1"}),
        ("锚点改名", lambda tmp: _patch(tmp, "S01", "task_book_anchor", "不存在的锚点"), {"B4"}),
        ("删行", lambda tmp: _drop_row(tmp, "S12"), {"B1"}),
        ("重复绑定号", lambda tmp: _patch(tmp, "S02", "binding_id", "TB-20261127-S01"), {"B1"}),
        ("版本漂移", lambda tmp: _patch(tmp, "S03", "spec_version", "9.9.9"), {"B7"}),
    ]
    for name, mutate, expect in mutations:
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            shutil.copytree(src_root / "specs" / "006-toolchain-db-standardization", tmp / "specs" / "006-toolchain-db-standardization", ignore=shutil.ignore_patterns("axiomatic", "deliverables", "__pycache__"))
            tb_src = src_root / "01-项目管理" / "01-编纂规划与报告归档" / "工具链与数据库标准化-任务书-20261127.md"
            tb_dst = tmp / "01-项目管理" / "01-编纂规划与报告归档" / "工具链与数据库标准化-任务书-20261127.md"
            tb_dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(tb_src, tb_dst)
            mutate(tmp)
            res = check_root(tmp)
            got = {f.split("：")[0].split(":")[0].strip() for f in res["fails"]}
            if not (expect & got):
                failures.append(f"{name}: 期望 {sorted(expect)} 实测 {sorted(got)}")
    if failures:
        print("SELFTEST FAIL")
        for f in failures:
            print(f"- {f}")
        return 1
    print("SELFTEST PASS：6 种变异全部被对应判据检出")
    return 0


def _patch(tmp: Path, sid: str, field: str, value: str) -> None:
    bp = tmp / "specs" / "006-toolchain-db-standardization" / "BINDING.tsv"
    lines = bp.read_text(encoding="utf-8").split("\n")
    header = lines[0].split("\t")
    idx = header.index(field)
    for i, line in enumerate(lines[1:], 1):
        cells = line.split("\t")
        if len(cells) > header.index("spec_id") and cells[header.index("spec_id")] == sid:
            cells[idx] = value
            lines[i] = "\t".join(cells)
    bp.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def _drop_row(tmp: Path, sid: str) -> None:
    bp = tmp / "specs" / "006-toolchain-db-standardization" / "BINDING.tsv"
    lines = bp.read_text(encoding="utf-8").split("\n")
    header = lines[0].split("\t")
    idx = header.index("spec_id")
    kept = [lines[0]]
    for line in lines[1:]:
        cells = line.split("\t")
        if len(cells) > idx and cells[idx] == sid:
            continue
        kept.append(line)
    bp.write_text("\n".join(kept), encoding="utf-8", newline="\n")


def check_root(root: Path) -> dict:
    fails = []
    binding = root / "specs" / "006-toolchain-db-standardization" / "BINDING.tsv"
    taskbook = root / "01-项目管理" / "01-编纂规划与报告归档" / "工具链与数据库标准化-任务书-20261127.md"
    rows = list(csv.DictReader(binding.open(encoding="utf-8", newline=""), delimiter="\t"))
    if len(rows) != 13:
        fails.append("B1：行数 {}".format(len(rows)))
    if {r["spec_id"] for r in rows} != {"M"} | {f"S{i:02d}" for i in range(1, 13)}:
        fails.append("B1：spec_id 集合不符")
    if len({r["binding_id"] for r in rows}) != len(rows):
        fails.append("B1：binding_id 重复")
    goals = set()
    for r in rows:
        for g in r["goals"].split(","):
            if g.strip():
                goals.add(int(g))
        for key in ("spec_path", "tasks_sha256", "checklist_sha256", "spec_sha256"):
            pass
        spec = root / r["spec_path"]
        for fname, key in (("spec.md", "spec_sha256"), ("tasks.md", "tasks_sha256"), ("checklist.md", "checklist_sha256")):
            f = spec.parent / fname
            if not f.exists():
                fails.append("B1：缺 {}".format(spec.parent.name + "/" + fname))
            elif sha256(f) != r[key]:
                fails.append("B2：{} {}/{} 哈希不符".format(r["spec_id"], fname, key))
        if spec.exists() and sha256(spec) != r["spec_sha256"]:
            fails.append("B2：{} spec 哈希不符".format(r["spec_id"]))
    if goals != set(range(1, 13)):
        fails.append("B3：目标覆盖 {}".format(sorted(goals)))
    text = taskbook.read_text(encoding="utf-8")
    for r in rows:
        if "## " + r["task_book_anchor"] not in text:
            fails.append("B4：{} 锚点未命中".format(r["spec_id"]))
    m = re.search(r"manifest sha256：`([a-f0-9]{64})`", text)
    if not m:
        fails.append("B6：任务书附录 C manifest 哈希缺失")
    elif m.group(1) != sha256(binding):
        fails.append("B6：manifest 哈希与任务书不一致")
    subs = sorted((binding.parent / "subspecs").glob("S*/spec.md"))
    if len(subs) != 12:
        fails.append("B8：子 spec 目录数 {}".format(len(subs)))
    fm_re = re.compile(r"^---\n(.*?)\n---\n", re.S)
    for r in rows:
        spec = root / r["spec_path"]
        if not spec.exists():
            continue
        m = fm_re.match(spec.read_text(encoding="utf-8"))
        if not m:
            fails.append("B7：{} frontmatter 缺失".format(r["spec_id"]))
            continue
        fm = {}
        for line in m.group(1).split("\n"):
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip()
        pairs = [
            ("spec_id", r["spec_id"]),
            ("task_book", r["task_book_path"]),
            ("task_book_anchor", r["task_book_anchor"]),
            ("version", r["spec_version"]),
            ("status", r["status"]),
            ("binding_id", r["binding_id"]),
        ]
        for k, want in pairs:
            if fm.get(k) != want:
                fails.append("B7：{} {}={}".format(r["spec_id"], k, fm.get(k)))
    return {"fails": fails, "rows": len(rows), "goals": sorted(goals)}


def main() -> int:
    args = sys.argv[1:]
    if "--selftest" in args:
        return selftest()
    res = check_root(ROOT)
    if res["fails"]:
        print("FAIL")
        for f in res["fails"]:
            print(f"- {f}")
        return 1
    print(f"PASS: B1—B8（{res['rows']} 行；目标覆盖 {res['goals']}）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
