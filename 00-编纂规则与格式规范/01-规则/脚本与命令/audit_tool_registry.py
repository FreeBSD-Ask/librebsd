#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S09 全局工具表校验器（第四十八件门禁；S09-FR-04）。

判据（--check 默认）：
  B1 工具总表.tsv 存在且表头与 schema（21 字段）全等
  B2 必填字段非空（tool_id/name/path/category/language/purpose/owner/lifecycle/tracked）
  B3 lifecycle ∈ {stable, experimental, deprecated, one-shot, external}
  B4 path 在磁盘存在
  B5 tracked 与 git ls-files 一致（true ⇔ 已跟踪）
  B6 stable 三判据：tracked=true ＋ rule_references 非空 ＋ verification_method=selftest
     （第四判据"90 天调用证据"无调用日志，由 last_verified 人工签收，暂披露不阻断）
  B7 tool_id 唯一且 path 唯一
  B8 孤儿：固定工具目录内 .py/.mjs/.js/.sql 未入表
  B9 one-shot清单.tsv 内 tracked=true 即 FAIL（one-shot 必须 untracked）；
     stale 数只统计输出（清理候选，不阻断）
  B10 工具总表.md 的 stable 计数与 TSV 复算一致
  B11 两个 TSV 直角引号 0 处（TSV 不在 audit_md_quote_glyphs 扫描面）

用法：
  python audit_tool_registry.py --selftest   # 六变异＋干净样本
  python audit_tool_registry.py --check      # 真实仓库
  python audit_tool_registry.py --check --root <仓库根>
"""

from __future__ import annotations

import argparse
import csv
import re
import subprocess
import sys
import tempfile
from pathlib import Path

FIXED_DIR = "00-编纂规则与格式规范/01-规则/脚本与命令"
OUT_REL = "specs/006-toolchain-db-standardization/deliverables/S09"
SCAN_EXTS = {".py", ".mjs", ".js", ".sql"}
REQUIRED = ["tool_id", "name", "path", "category", "language", "purpose",
            "owner", "lifecycle", "tracked"]
LIFECYCLES = {"stable", "experimental", "deprecated", "one-shot", "external"}
HEADER = [
    "tool_id", "name", "path", "category", "language", "entrypoint", "purpose",
    "owner", "created_at", "last_modified", "lifecycle", "tracked",
    "rule_references", "gates", "dependencies", "invocation", "exit_codes",
    "last_verified", "verification_method", "risk", "notes",
]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def git_tracked(root: Path) -> set[str]:
    try:
        out = subprocess.run(["git", "ls-files", "-z"], capture_output=True, cwd=str(root),
                             timeout=300)
        if out.returncode != 0:
            return set()
        return {p.replace("\\", "/") for p in out.stdout.decode("utf-8", "replace").split("\0") if p}
    except Exception:  # noqa: BLE001
        return set()


def load_tsv(path: Path) -> tuple[list[str], list[dict]]:
    with path.open(encoding="utf-8", newline="") as fh:
        rd = csv.DictReader(fh, delimiter="\t")
        return list(rd.fieldnames or []), list(rd)


def check(root: Path, tracked: set[str] | None = None) -> tuple[list[str], list[str], dict]:
    tracked = git_tracked(root) if tracked is None else tracked
    out = root / OUT_REL
    tsv = out / "工具总表.tsv"
    one = out / "one-shot清单.tsv"
    md = out / "工具总表.md"
    errors: list[str] = []
    warns: list[str] = []
    stats: dict = {}

    # B1
    if not tsv.exists():
        return [f"B1 缺失 {tsv.relative_to(root).as_posix()}"], warns, stats
    header, rows = load_tsv(tsv)
    if header != HEADER:
        errors.append(f"B1 表头漂移：{header} ≠ {HEADER}")
    stats["rows"] = len(rows)
    if not rows:
        errors.append("B1 表为空")
        return errors, warns, stats

    # B2/B3/B4/B5/B6
    seen_ids: dict[str, int] = {}
    seen_paths: dict[str, int] = {}
    for i, r in enumerate(rows, start=2):
        for f in REQUIRED:
            if not (r.get(f) or "").strip():
                errors.append(f"B2 行{i} {r.get('path','?')} 必填字段空：{f}")
        life = (r.get("lifecycle") or "").strip()
        if life and life not in LIFECYCLES:
            errors.append(f"B3 行{i} {r.get('path','?')} lifecycle 非法：{life}")
        rel = (r.get("path") or "").replace("\\", "/")
        if rel and not (root / rel).exists():
            errors.append(f"B4 行{i} path 不存在：{rel}")
        is_trk = (r.get("tracked") or "").strip() == "true"
        in_git = rel in tracked
        if rel and is_trk != in_git:
            errors.append(f"B5 行{i} tracked 不一致：表={'true' if is_trk else 'false'} "
                          f"真值={'true' if in_git else 'false'}：{rel}")
        if life == "stable":
            if not is_trk:
                errors.append(f"B6 行{i} stable 但未 tracked：{rel}")
            if not (r.get("rule_references") or "").strip():
                errors.append(f"B6 行{i} stable 但无规则引用：{rel}")
            if (r.get("verification_method") or "").strip() != "selftest":
                errors.append(f"B6 行{i} stable 但无 selftest 声明：{rel}")
            if not (r.get("last_verified") or "").strip():
                warns.append(f"B6 行{i} stable 缺 90 天调用证据（last_verified 空）：{rel}")
        tid = r.get("tool_id") or ""
        seen_ids[tid] = seen_ids.get(tid, 0) + 1
        seen_paths[rel] = seen_paths.get(rel, 0) + 1

    # B7
    dup_ids = [k for k, v in seen_ids.items() if v > 1]
    dup_paths = [k for k, v in seen_paths.items() if v > 1]
    if dup_ids:
        errors.append(f"B7 tool_id 重复：{dup_ids}")
    if dup_paths:
        errors.append(f"B7 path 重复：{dup_paths}")

    # B8 孤儿
    fixed = root / FIXED_DIR
    if fixed.exists():
        on_disk = {p.relative_to(root).as_posix() for p in fixed.iterdir()
                   if p.is_file() and p.suffix.lower() in SCAN_EXTS}
        orphans = sorted(on_disk - set(seen_paths))
        if orphans:
            errors.append(f"B8 孤儿未入表 {len(orphans)} 件：{orphans[:10]}")
    stats["orphans"] = len(orphans) if fixed.exists() else 0

    # B9 one-shot 清单
    if not one.exists():
        errors.append(f"B9 缺失 one-shot清单.tsv")
    else:
        _, orows = load_tsv(one)
        bad = [r["path"] for r in orows if (r.get("tracked") or "") == "true"]
        if bad:
            errors.append(f"B9 one-shot 清单含已跟踪件 {len(bad)}：{bad[:5]}")
        stats["oneshot"] = len(orows)
        stats["stale"] = sum(1 for r in orows if r.get("ttl") == "stale")
        stats["unknown"] = sum(1 for r in orows if r.get("ttl") == "unknown")
        if stats["stale"]:
            warns.append(f"B9 清理候选 {stats['stale']} 件（TTL 超期，不自动删除，"
                         f"执行见 S11 机制）")

    # B10 dashboard 计数
    if not md.exists():
        errors.append("B10 缺失 工具总表.md")
    else:
        m = re.search(r"stable (\d+)", md.read_text(encoding="utf-8"))
        n_stable = sum(1 for r in rows if r.get("lifecycle") == "stable")
        if not m:
            errors.append("B10 dashboard 缺 stable 计数")
        elif int(m.group(1)) != n_stable:
            errors.append(f"B10 dashboard stable {m.group(1)} ≠ TSV 复算 {n_stable}")

    # B11 TSV 直角引号（TSV 不在 audit_md_quote_glyphs 扫描面，须由本门禁兜底）
    corner = "\u300c\u300d\u300e\u300f"
    for p, label in ((tsv, "工具总表.tsv"), (one, "one-shot清单.tsv")):
        if p.exists():
            txt = p.read_text(encoding="utf-8", errors="replace")
            hits = sum(txt.count(c) for c in corner)
            if hits:
                errors.append(f"B11 {label} 含直角引号 {hits} 处（生成器应弯化）")

    stats["stable"] = sum(1 for r in rows if r.get("lifecycle") == "stable")
    return errors, warns, stats


def run(root: Path, tracked: set[str] | None = None, quiet: bool = False) -> int:
    errors, warns, stats = check(root, tracked)
    if not quiet:
        print(f"工具总表 {stats.get('rows', 0)} 行；stable {stats.get('stable', 0)}；"
              f"one-shot {stats.get('oneshot', 0)}（stale {stats.get('stale', 0)}／"
              f"unknown {stats.get('unknown', 0)}）；孤儿 {stats.get('orphans', 0)}")
    for w in warns:
        print(f"WARN {w}")
    for e in errors:
        print(f"FAIL {e}")
    if errors:
        print(f"RESULT: FAIL（{len(errors)} 条）")
        return 1
    print("RESULT: PASS")
    return 0


def selftest() -> int:
    """六变异＋干净样本。变异各断言对应判据命中。"""
    fails = []

    def expect(name: str, mutate, want_code: str, want_error: bool = True) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            fixed = root / FIXED_DIR
            fixed.mkdir(parents=True)
            out = root / OUT_REL
            out.mkdir(parents=True)
            # 干净基线：a.py 满足 stable 四判据（tracked 由 override 传入）
            (fixed / "a.py").write_text('"""A 测试工具。"""\nimport argparse\n'
                                        'ap=argparse.ArgumentParser()\n'
                                        'ap.add_argument("--selftest",action="store_true")\n',
                                        encoding="utf-8", newline="\n")
            rel_a = f"{FIXED_DIR}/a.py"
            row = {k: "" for k in HEADER}
            row.update({"tool_id": "T-GA-001", "name": "a.py", "path": rel_a,
                        "category": "gate", "language": "python",
                        "entrypoint": f"python {rel_a}", "purpose": "A 测试工具。",
                        "owner": "ykla", "created_at": "2026-01-01",
                        "last_modified": "2026-01-01", "lifecycle": "stable",
                        "tracked": "true", "rule_references": "00-编纂规则与格式规范/01-规则/x.md",
                        "gates": "第X件", "invocation": f"python {rel_a} --selftest",
                        "exit_codes": "0=ok;1=fail", "last_verified": "",
                        "verification_method": "selftest", "risk": "high", "notes": ""})
            rows = [dict(row)]
            mutate(rows, fixed, out)
            # 写 TSV
            with (out / "工具总表.tsv").open("w", encoding="utf-8", newline="") as fh:
                w = csv.DictWriter(fh, fieldnames=HEADER, delimiter="\t", lineterminator="\n")
                w.writeheader()
                for r in rows:
                    w.writerow(r)
            # one-shot 清单
            (out / "one-shot清单.tsv").write_text(
                "path\text\tbytes\tdate_asof\tdate_source\tage_days\tttl\ttracked\tpurpose\n",
                encoding="utf-8", newline="\n")
            n_stable = sum(1 for r in rows if r.get("lifecycle") == "stable")
            (out / "工具总表.md").write_text(
                f"# t\n\n- 生命周期：stable {n_stable}／experimental 0\n", encoding="utf-8",
                newline="\n")
            code = run(root, tracked={rel_a}, quiet=True)
            errors, _, _ = check(root, tracked={rel_a})
            hit = any(e.startswith(want_code) for e in errors)
            if want_error and (code == 0 or not hit):
                fails.append(f"{name}: 期望 {want_code} 命中，实际 code={code} errors={errors[:3]}")
            if not want_error and code != 0:
                fails.append(f"{name}: 期望 PASS，实际 code={code} errors={errors[:3]}")

    def m1(rows, fixed, out):
        rows[0]["purpose"] = ""

    def m2(rows, fixed, out):
        rows[0]["lifecycle"] = "zombie"

    def m3(rows, fixed, out):
        rows[0]["verification_method"] = ""

    def m4(rows, fixed, out):
        rows[0]["lifecycle"] = "experimental"   # 绕过 B6，只测 B5
        rows[0]["tracked"] = "false"            # 但真值在 tracked_set 里

    def m5(rows, fixed, out):
        r2 = dict(rows[0])
        r2["path"] = f"{FIXED_DIR}/a.py"
        rows.append(r2)  # 同 id 同 path

    def m6(rows, fixed, out):
        (fixed / "b.py").write_text('"""B 孤儿。"""\n', encoding="utf-8", newline="\n")

    def clean(rows, fixed, out):
        pass

    expect("干净样本", clean, "", want_error=False)
    expect("M1 必填缺失", m1, "B2")
    expect("M2 lifecycle 非法", m2, "B3")
    expect("M3 stable 缺 selftest", m3, "B6")
    expect("M4 tracked 不一致", m4, "B5")
    expect("M5 id/path 重复", m5, "B7")
    expect("M6 孤儿未入表", m6, "B8")

    if fails:
        for f in fails:
            print(f"FAIL {f}")
        print(f"SELFTEST: FAIL（{len(fails)}/7）")
        return 1
    print("SELFTEST: PASS（7/7：干净样本＋M1—M6）")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="S09 全局工具表校验器（第四十八件）")
    ap.add_argument("--root", default="", help="仓库根（默认由脚本位置派生）")
    ap.add_argument("--check", action="store_true", help="校验真实仓库（默认动作）")
    ap.add_argument("--selftest", action="store_true", help="沙箱自检七项")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    root = Path(a.root).resolve() if a.root else repo_root()
    return run(root)


if __name__ == "__main__":
    raise SystemExit(main())
