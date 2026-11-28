#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S09 全局工具表生成器（固定脚本；S09-FR-03）。

四源合并：
  ① git ls-files（tracked 真值，一次性全量取）
  ② 规则 grep（01-规则/**/*.md 对工具文件名的引用）
  ③ audit_gate_registry.py 的 REGISTRY（门禁号与 selftest 声明，ast 解析不 import）
  ④ folder_db_registry.csv 行数 + backup_databases.py SCOPE 条目数（仅入 dashboard 交叉核对）

生命周期判据（二值，详见 deliverables/S09/生命周期规则.md）：
  stable       固定工具目录 + tracked + 规则引用 + selftest 声明，四者缺一降 experimental
  experimental 固定工具目录但缺上述任一稳定判据
  deprecated   例外覆盖表显式指定
  one-shot     path 以 script/ 开头（另出 one-shot清单.tsv，30 天 TTL）
  external     仓库外依赖（本表不收录，仅备注）

输出（默认 specs/006-toolchain-db-standardization/deliverables/S09/）：
  工具总表.tsv        21 字段，固定工具全量，按 path 排序，tool_id 随排序稳定
  工具总表.md         dashboard 派生视图（计数可复算）
  one-shot清单.tsv    script/ 顶层文本类脚本清单（TTL 判定，不自动删除）

用法：
  python build_tool_registry.py                # 写三件产物
  python build_tool_registry.py --check        # 只比对不写盘；漂移 exit 1
  python build_tool_registry.py --root <仓库根>  # 跨盘或沙箱
"""

from __future__ import annotations

import argparse
import ast
import csv
import hashlib
import re
import subprocess
import sys
import warnings
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

DATE_RE = re.compile(r"20\d{6}|20\d{2}-\d{2}-\d{2}")

FIXED_DIR = "00-编纂规则与格式规范/01-规则/脚本与命令"
OUT_REL = "specs/006-toolchain-db-standardization/deliverables/S09"
GATE_REG = FIXED_DIR + "/audit_gate_registry.py"
TZ = timezone(timedelta(hours=8))
TTL_DAYS = 30
SCRIPT_EXTS = {".py", ".mjs", ".js", ".sql"}

HEADER = [
    "tool_id", "name", "path", "category", "language", "entrypoint", "purpose",
    "owner", "created_at", "last_modified", "lifecycle", "tracked",
    "rule_references", "gates", "dependencies", "invocation", "exit_codes",
    "last_verified", "verification_method", "risk", "notes",
]
CAT_CODE = {"gate": "GA", "writer": "WR", "scanner": "SC", "collector": "CO",
            "converter": "CV", "service": "SE", "analysis": "AN", "other": "OT"}
LIFECYCLES = {"stable", "experimental", "deprecated", "one-shot", "external"}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def categorize(name: str) -> str:
    n = name.lower()
    if n.startswith("audit_") or n in {"git_commit_gate.py", "claimdb_guard.py",
                                       "register_waterlock.py", "rotate_guard_state.py",
                                       "premerge_keyguard.py", "wo007_idempotency.py"}:
        return "gate"
    if n.startswith(("verify_", "scan_")) or n.endswith("_dup.py"):
        return "scanner"
    if n.startswith(("crawl", "fetch", "download", "auto_ingest", "git_update")) or \
            "_crawl" in n or "_run_batch" in n or "_ingest" in n or "mine" in n:
        return "collector"
    if any(k in n for k in ("ocr", "transcribe", "convert", "pandoc", "epub",
                            "fix_md", "_to_", "2md")):
        return "converter"
    if n.startswith(("outline_writer", "register_", "insert_", "build_", "assemble_",
                     "sync_", "_full_", "batch_", "renumber", "_gen")) or \
            "write" in n or "_fill_" in n:
        return "writer"
    if n.startswith("serve_") or "server" in n:
        return "service"
    if n.startswith(("analyze_", "_longline", "baseline", "dashboard", "probe",
                     "task82_", "_progress")) or "audit_" in n:
        return "analysis"
    return "other"


def git_tracked(root: Path) -> set[str]:
    """git ls-files 全量（posix 相对路径）。失败返回空集并告警。"""
    try:
        out = subprocess.run(["git", "ls-files", "-z"], capture_output=True, cwd=str(root),
                             timeout=300)
        if out.returncode != 0:
            print("WARN: git ls-files 失败，tracked 判定退化为空集", file=sys.stderr)
            return set()
        return {p.replace("\\", "/") for p in out.stdout.decode("utf-8", "replace").split("\0") if p}
    except Exception as exc:  # noqa: BLE001
        print(f"WARN: git ls-files 异常 {exc}", file=sys.stderr)
        return set()


def git_created_all(root: Path) -> dict[str, str]:
    """一次 git log --diff-filter=A 拿全仓首次加入日期：{path: YYYY-MM-DD}。"""
    try:
        out = subprocess.run(
            ["git", "log", "--diff-filter=A", "--format=@%as", "--name-only", "-z"],
            capture_output=True, cwd=str(root), timeout=600)
        if out.returncode != 0:
            return {}
        text = out.stdout.decode("utf-8", "replace")
        dates: dict[str, str] = {}
        cur = ""
        for tok in text.split("\0"):
            tok = tok.strip("\n")
            if not tok:
                continue
            if tok.startswith("@"):
                cur = tok[1:].strip()
            elif cur:
                dates.setdefault(tok.replace("\\", "/"), cur)
        return dates
    except Exception:  # noqa: BLE001
        return {}


def load_registry_gates(root: Path) -> dict[str, dict]:
    """ast 解析 audit_gate_registry.py 的 REGISTRY：{script_relpath: {no, selftest}}。"""
    p = root / GATE_REG
    if not p.exists():
        return {}
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            tree = ast.parse(p.read_text(encoding="utf-8"))
    except SyntaxError:
        return {}
    out: dict[str, dict] = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and any(
                isinstance(t, ast.Name) and t.id == "REGISTRY" for t in node.targets):
            if not isinstance(node.value, ast.List):
                continue
            for elt in node.value.elts:
                if not (isinstance(elt, ast.Call) and isinstance(elt.func, ast.Name)
                        and elt.func.id == "dict"):
                    continue
                kv = {}
                for kw in elt.keywords:
                    if kw.arg in {"no", "script", "selftest", "kind"} and \
                            isinstance(kw.value, ast.Constant):
                        kv[kw.arg] = kw.value.value
                if kv.get("script"):
                    out[kv["script"].replace("\\", "/")] = kv
    return out


def rule_tokens(root: Path) -> dict[str, set[str]]:
    """扫 01-规则/**/*.md，返回 {文件名: {引用它的规则文件相对路径}}。"""
    rules = root / "00-编纂规则与格式规范" / "01-规则"
    names: dict[str, set[str]] = {}
    if not rules.exists():
        return names
    for p in rules.rglob("*.md"):
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:  # noqa: BLE001
            continue
        rel = p.relative_to(root).as_posix()
        for tok in set(re.findall(r"[\w.\-]+\.(?:py|mjs|js|sql)", text)):
            names.setdefault(tok, set()).add(rel)
    return names


def docstring_first(path: Path) -> str:
    if path.suffix.lower() != ".py":
        return ""
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            tree = ast.parse(path.read_text(encoding="utf-8", errors="replace"))
        doc = ast.get_docstring(tree) or ""
        return doc.strip().splitlines()[0].strip() if doc.strip() else ""
    except Exception:  # noqa: BLE001
        try:
            for line in path.read_text(encoding="utf-8", errors="replace").splitlines()[:40]:
                s = line.strip()
                if s.startswith("#") and not s.startswith("#!") and "-*-" not in s:
                    return s.lstrip("# ").strip()[:100]
        except Exception:  # noqa: BLE001
            pass
        return ""


def purpose_of(path: Path) -> str:
    """purpose 兜底：docstring 优先；资源件标类型；无 docstring 的 .py 显式披露。"""
    doc = docstring_first(path)
    if doc:
        return doc[:100]
    ext = path.suffix.lower()
    if ext != ".py":
        return f"{ext.lstrip('.') or '无扩展'} 资源件（无 docstring 概念）"
    return f"{path.name}（无 docstring 声明）"


def has_selftest_decl(path: Path) -> bool:
    if path.suffix.lower() != ".py":
        return False
    try:
        return "--selftest" in path.read_text(encoding="utf-8", errors="ignore")
    except Exception:  # noqa: BLE001
        return False


def load_overrides(root: Path) -> dict[str, dict]:
    """例外覆盖.tsv：tool_id|path, field, value, reason（只许 notes/risk/deprecated）。"""
    p = root / OUT_REL / "例外覆盖.tsv"
    out: dict[str, dict] = {}
    if not p.exists():
        return out
    with p.open(encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            key = row.get("tool_id") or row.get("path") or ""
            if key:
                out[key] = row
    return out


def build_rows(root: Path, tracked: set[str], gates: dict[str, dict],
               refs: dict[str, set[str]], created: dict[str, str],
               overrides: dict[str, dict]) -> list[dict]:
    fixed = root / FIXED_DIR
    rows: list[dict] = []
    seq = 0
    for p in sorted(fixed.iterdir(), key=lambda x: x.name):
        if not p.is_file():
            continue
        rel = p.relative_to(root).as_posix()
        name = p.name
        cat = categorize(name)
        ext = p.suffix.lower()
        lang = {".py": "python", ".sql": "sql", ".mjs": "js", ".js": "js"}.get(ext, "other")
        gref = sorted(refs.get(name, set()))
        g = gates.get(rel, {})
        st = has_selftest_decl(p) or bool(g.get("selftest"))
        is_tracked = rel in tracked
        stable_ok = is_tracked and bool(gref) and st
        life = "stable" if stable_ok else "experimental"
        ov = overrides.get(rel) or overrides.get("") or {}
        if ov.get("field") == "lifecycle" and ov.get("value") in LIFECYCLES:
            life = ov["value"]
        notes = []
        if not stable_ok:
            miss = []
            if not is_tracked:
                miss.append("tracked")
            if not gref:
                miss.append("规则引用")
            if not st:
                miss.append("selftest")
            notes.append("stable 判据缺：" + "／".join(miss))
        if ext != ".py":
            notes.append("非 Python 资源件")
        seq += 1
        rows.append({
            "tool_id": f"T-{CAT_CODE[cat]}-{seq:03d}",
            "name": name,
            "path": rel,
            "category": cat,
            "language": lang,
            "entrypoint": f"python {rel}" if ext == ".py" else "（资源件，随规则引用）",
            "purpose": purpose_of(p),
            "owner": "ykla",
            "created_at": created.get(rel, "") or datetime.fromtimestamp(
                p.stat().st_mtime, TZ).strftime("%Y-%m-%d"),
            "last_modified": datetime.fromtimestamp(p.stat().st_mtime, TZ).strftime("%Y-%m-%d"),
            "lifecycle": life,
            "tracked": "true" if is_tracked else "false",
            "rule_references": ";".join(gref[:3]) + (f";…共{len(gref)}" if len(gref) > 3 else ""),
            "gates": g.get("no", ""),
            "dependencies": "",
            "invocation": f"python {rel} --help" if ext == ".py" else "",
            "exit_codes": "0=ok;1=fail;2=usage" if ext == ".py" else "",
            "last_verified": "",
            "verification_method": "selftest" if st else "",
            "risk": "high" if cat in {"gate", "writer"} else "low",
            "notes": "；".join(notes + ([ov["reason"]] if ov.get("reason") else [])),
        })
    return rows


def embedded_date(path: Path) -> tuple[datetime | None, str]:
    """文件名内嵌日期优先（17%），其次内容首 4KB（合计 68%）；mtime 因 2026-10-28 批量
    刷新而失真，仅作最后兜底且标记来源，TTL 判 unknown 不入清理候选。"""
    for tok in DATE_RE.findall(path.name):
        d = parse_date_tok(tok)
        if d:
            return d, "filename"
    try:
        head = path.read_text(encoding="utf-8", errors="ignore")[:4000]
    except Exception:  # noqa: BLE001
        head = ""
    found = [parse_date_tok(t) for t in DATE_RE.findall(head)]
    found = [d for d in found if d]
    if found:
        return max(found), "content"
    return None, "mtime-suspect"


def parse_date_tok(tok: str) -> datetime | None:
    tok = tok.replace("-", "")
    try:
        return datetime.strptime(tok, "%Y%m%d").replace(tzinfo=TZ)
    except ValueError:
        return None


def build_oneshot(root: Path, tracked: set[str], as_of: datetime | None = None) -> list[dict]:
    script = root / "script"
    out: list[dict] = []
    if not script.exists():
        return out
    ref = (as_of or datetime.now(TZ)).date()
    for p in sorted(script.iterdir(), key=lambda x: x.name):
        if not p.is_file() or p.suffix.lower() not in SCRIPT_EXTS:
            continue
        rel = p.relative_to(root).as_posix()
        st = p.stat()
        dt, src = embedded_date(p)
        if dt:
            age = (ref - dt.date()).days
            ttl = "stale" if age > TTL_DAYS else "fresh"
            asof = dt.strftime("%Y-%m-%d")
        else:
            age = -1
            ttl = "unknown"
            asof = datetime.fromtimestamp(st.st_mtime, TZ).strftime("%Y-%m-%d")
        out.append({
            "path": rel,
            "ext": p.suffix.lower(),
            "bytes": st.st_size,
            "as_of": ref.isoformat(),
            "date_asof": asof,
            "date_source": src,
            "age_days": age,
            "ttl": ttl,
            "tracked": "true" if rel in tracked else "false",
            "purpose": docstring_first(p)[:80],
        })
    return out


def write_tsv(path: Path, header: list[str], rows: list[dict]) -> bytes:
    import io
    buf = io.StringIO(newline="")
    w = csv.DictWriter(buf, fieldnames=header, delimiter="\t", lineterminator="\n")
    w.writeheader()
    for r in rows:
        w.writerow(r)
    data = buf.getvalue().encode("utf-8")
    path.write_bytes(data)
    return data


def dashboard(root: Path, rows: list[dict], oneshot: list[dict]) -> str:
    life = Counter(r["lifecycle"] for r in rows)
    lang = Counter(r["language"] for r in rows)
    cat = Counter(r["category"] for r in rows)
    trk = Counter(r["tracked"] for r in rows)
    stable = [r for r in rows if r["lifecycle"] == "stable"]
    ttl_stale = [r for r in oneshot if r["ttl"] == "stale"]
    ttl_unknown = sum(1 for r in oneshot if r["ttl"] == "unknown")
    src_dist = Counter(r["date_source"] for r in oneshot)
    # ④ 源交叉核对
    reg_csv = root / "11-元数据接口" / "09-文件夹数据库索引" / "folder_db_registry.csv"
    n_reg = 0
    if reg_csv.exists():
        with reg_csv.open(encoding="utf-8", newline="") as fh:
            n_reg = max(0, sum(1 for _ in fh) - 1)
    n_scope = 0
    scope_py = root / FIXED_DIR / "backup_databases.py"
    if scope_py.exists():
        m = re.search(r"SCOPE\s*=\s*\{(.*?)\n\}", scope_py.read_text(encoding="utf-8"), re.S)
        if m:
            n_scope = len(re.findall(r'"[^"]+"\s*:\s*r"', m.group(1)))
    lines = [
        "# 工具总表（S09 派生视图；由 build_tool_registry.py 生成，勿手改）",
        "",
        f"- 主表：`工具总表.tsv`（{len(rows)} 件固定工具，21 字段，按 path 排序）",
        f"- one-shot：`one-shot清单.tsv`（{len(oneshot)} 件；超 {TTL_DAYS} 天 {len(ttl_stale)} 件为清理候选，"
        f"日期不可信 {ttl_unknown} 件判 unknown 不入候选）",
        f"- one-shot 日期来源：{json_dumps(src_dist)}（mtime 因 2026-10-28 批量刷新失真，仅兜底）",
        f"- 生命周期：stable {life.get('stable', 0)}／experimental {life.get('experimental', 0)}"
        f"／deprecated {life.get('deprecated', 0)}／one-shot {life.get('one-shot', 0)}"
        f"／external {life.get('external', 0)}",
        f"- 语言：{json_dumps(lang)}",
        f"- 类别：{json_dumps(cat)}",
        f"- tracked：true {trk.get('true', 0)}／false {trk.get('false', 0)}",
        "",
        "## 四源交叉核对",
        "",
        f"- ① git ls-files：tracked 判定真值（主表 true {trk.get('true', 0)} 件）",
        f"- ② 规则 grep：规则引用覆盖 {sum(1 for r in rows if r['rule_references'])} 件",
        f"- ③ audit_gate_registry.py：门禁号回填 {sum(1 for r in rows if r['gates'])} 件",
        f"- ④ folder_db_registry.csv {n_reg} 行／backup_databases.py SCOPE {n_scope} 库（量级核对）",
        "",
        "## stable 清单",
        "",
        "| tool_id | name | 门禁 | selftest |",
        "| ---- | ---- | ---- | ---- |",
    ]
    for r in stable:
        lines.append(f"| {r['tool_id']} | {r['name']} | {r['gates']} | {r['verification_method']} |")
    lines += [
        "",
        "## one-shot 清理候选（TTL 超期，不自动删除；执行见 S11 机制）",
        "",
        f"- 超期 {len(ttl_stale)} 件，前 20 件：",
        "",
        "| path | age_days | bytes |",
        "| ---- | ---- | ---- |",
    ]
    for r in ttl_stale[:20]:
        lines.append(f"| {r['path']} | {r['age_days']} | {r['bytes']} |")
    lines += [
        "",
        "## 验证",
        "",
        f"- `--check` 复算：TSV 字节一致（manifest sha256 见下）",
        f"- 主表 sha256＝{hashlib.sha256(render_tsv_bytes(rows)).hexdigest()}",
        "",
    ]
    return "\n".join(lines)


def json_dumps(c: Counter) -> str:
    import json
    return json.dumps(dict(c), ensure_ascii=False, sort_keys=True)


def render_tsv_bytes(rows: list[dict]) -> bytes:
    import io
    buf = io.StringIO(newline="")
    w = csv.DictWriter(buf, fieldnames=HEADER, delimiter="\t", lineterminator="\n")
    w.writeheader()
    for r in rows:
        w.writerow(r)
    return buf.getvalue().encode("utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description="S09 全局工具表生成器（S09-FR-03）")
    ap.add_argument("--root", default="", help="仓库根（默认由脚本位置派生）")
    ap.add_argument("--out-dir", default="", help=f"输出目录（默认 {OUT_REL}）")
    ap.add_argument("--check", action="store_true", help="只比对不写盘；漂移 exit 1")
    a = ap.parse_args()
    root = Path(a.root).resolve() if a.root else repo_root()
    out = Path(a.out_dir) if a.out_dir else root / OUT_REL

    tracked = git_tracked(root)
    gates = load_registry_gates(root)
    refs = rule_tokens(root)
    created = git_created_all(root)
    overrides = load_overrides(root)
    rows = build_rows(root, tracked, gates, refs, created, overrides)
    # --check 回读既有清单的 as_of 基准，保证跨日复算字节稳定
    as_of = None
    one_p = out / "one-shot清单.tsv"
    if a.check and one_p.exists():
        try:
            with one_p.open(encoding="utf-8", newline="") as fh:
                first = next(csv.DictReader(fh, delimiter="\t"), None)
            if first and first.get("as_of"):
                as_of = datetime.strptime(first["as_of"], "%Y-%m-%d").replace(tzinfo=TZ)
        except Exception:  # noqa: BLE001
            as_of = None
    oneshot = build_oneshot(root, tracked, as_of)

    tsv_bytes = render_tsv_bytes(rows)
    md = dashboard(root, rows, oneshot)
    one_header = ["path", "ext", "bytes", "as_of", "date_asof", "date_source", "age_days",
                  "ttl", "tracked", "purpose"]
    import io
    buf = io.StringIO(newline="")
    w = csv.DictWriter(buf, fieldnames=one_header, delimiter="\t", lineterminator="\n")
    w.writeheader()
    for r in oneshot:
        w.writerow(r)
    one_bytes = buf.getvalue().encode("utf-8")

    if a.check:
        tsv_p = out / "工具总表.tsv"
        one_p = out / "one-shot清单.tsv"
        bad = []
        for p, want in ((tsv_p, tsv_bytes), (one_p, one_bytes)):
            if not p.exists():
                bad.append(f"缺失 {p.name}")
            elif p.read_bytes() != want:
                bad.append(f"漂移 {p.name}（磁盘 {p.stat().st_size}B ≠ 复算 {len(want)}B）")
        if bad:
            print("FAIL: " + "；".join(bad))
            return 1
        print(f"PASS: 工具总表 {len(rows)} 行、one-shot {len(oneshot)} 行，复算字节一致")
        return 0

    out.mkdir(parents=True, exist_ok=True)
    write_tsv(out / "工具总表.tsv", HEADER, rows)
    (out / "one-shot清单.tsv").write_bytes(one_bytes)
    (out / "工具总表.md").write_text(md, encoding="utf-8", newline="\n")
    life = Counter(r["lifecycle"] for r in rows)
    print(f"rows={len(rows)} stable={life.get('stable',0)} experimental={life.get('experimental',0)} "
          f"one-shot={len(oneshot)} stale={sum(1 for r in oneshot if r['ttl']=='stale')}")
    print(f"written: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
