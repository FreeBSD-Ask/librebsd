# -*- coding: utf-8 -*-
"""audit_engineering_practice.py —— 第二十九件门禁：工程实践基线。

对象
----
- `01-项目管理/02-工程决策与技术债/ADR/ADR-*.md`：必填字段、索引、编号、状态与日期
- `01-项目管理/02-工程决策与技术债/技术债登记.md`：表字段、承担者、状态
- `00-编纂规则与格式规范/02-操作手册/14-工程实践模板/`：模板接线
- `00-编纂规则与格式规范/01-规则/工程实践规则.md`：规则登记与复审日期
- `流程规则.md`、`01-规则/README.md`、`AGENTS.md`、`脚本与命令/README.md`、`audit_gate_registry.py`：接线

判据
----
E1 ADR 十二项必填字段
E2 ADR 索引、编号、状态与日期
E3 技术债表字段、承担者与状态
E4 模板存在且被规则或模板说明引用；规则引用的模板存在
E5 规则登记与门禁接线
E6 复审日期存在；过期仅 WARN，不判 FAIL
E7 `流程规则.md` 二级索引与全部 H2 标题严格一致

用法
----
    python audit_engineering_practice.py            # 0 通过 / 1 不通过
    python audit_engineering_practice.py --selftest # 判据非空自检（正样本 + 七类负向夹具）
    python audit_engineering_practice.py --list     # 打印检查对象

依赖：仅标准库。
"""

import argparse
import datetime
import pathlib
import re
import shutil
import sys
import tempfile

sys.stdout.reconfigure(encoding="utf-8")

REPO = pathlib.Path(__file__).resolve().parents[3]

ADR_FIELDS = [
    "形式", "矛盾", "正面", "负面", "承担者",
    "过去依据", "现在依据", "将来失效条件",
    "0 信任校验", "自由影响", "安全和解", "复审触发",
]
DEBT_COLUMNS = ["ID", "描述", "来源", "影响", "承担者", "偿还条件", "复审日期或触发", "状态"]
DEBT_STATUS = {"未偿还", "偿还中", "已偿还", "条件失效", "已豁免"}
BAD_OWNERS = {"", "待定", "后续补", "TBD", "无", "项目组", "以后"}
DATE_RE = re.compile(r"复审日期(?:\*\*)?\s*[：:]\s*(\d{4}-\d{2}-\d{2})")
INDEX_BEGIN = "<!-- FLOW_INDEX_BEGIN -->"
INDEX_END = "<!-- FLOW_INDEX_END -->"


def _paths(root: pathlib.Path):
    rule_dir = root / "00-编纂规则与格式规范" / "01-规则"
    gov = root / "01-项目管理" / "02-工程决策与技术债"
    return {
        "rule_dir": rule_dir,
        "rule": rule_dir / "工程实践规则.md",
        "rule_readme": rule_dir / "README.md",
        "flow": rule_dir / "流程规则.md",
        "cmd_readme": rule_dir / "脚本与命令" / "README.md",
        "registry": rule_dir / "脚本与命令" / "audit_gate_registry.py",
        "agents": root / "AGENTS.md",
        "gov": gov,
        "adr_dir": gov / "ADR",
        "index": gov / "index.md",
        "debt": gov / "技术债登记.md",
        "templates": root / "00-编纂规则与格式规范" / "02-操作手册" / "14-工程实践模板",
    }


def _read(path: pathlib.Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def _has_field(text: str, label: str) -> bool:
    pattern = (
        r"(?m)^\s*(?:#{1,6}\s*)?(?:[-*]\s*)?(?:\d+[.、]\s*)?(?:\*\*)?"
        + re.escape(label)
        + r"(?:\*\*)?\s*(?:[：:]|$)"
    )
    return re.search(pattern, text) is not None


def _adr_files(adr_dir: pathlib.Path):
    if not adr_dir.is_dir():
        return []
    return sorted(adr_dir.glob("ADR-*.md"))


def _parse_debt(text: str):
    """返回 (header, rows, error)。只解析第一张含 ID／描述／承担者 的表。"""
    lines = text.splitlines()
    header_idx = None
    for i, line in enumerate(lines):
        if line.strip().startswith("|") and "ID" in line and "描述" in line and "承担者" in line:
            header_idx = i
            break
    if header_idx is None:
        return None, [], "未找到技术债表头（需含 ID／描述／承担者）"
    header = [c.strip() for c in lines[header_idx].strip().strip("|").split("|")]
    rows = []
    for line in lines[header_idx + 1:]:
        if not line.strip().startswith("|"):
            break
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells and all(re.fullmatch(r":?-+:?", c) for c in cells):
            continue
        rows.append(cells)
    return header, rows, None


def _review_date(text: str):
    m = DATE_RE.search(text)
    return m.group(1) if m else None


def _flow_index_check(text: str):
    h2 = [m.group(1).strip() for m in re.finditer(r"(?m)^##\s+(.+?)\s*$", text)]
    if INDEX_BEGIN not in text or INDEX_END not in text:
        return False, "缺 FLOW_INDEX_BEGIN／FLOW_INDEX_END 标记"
    block = text.split(INDEX_BEGIN, 1)[1].split(INDEX_END, 1)[0]
    entries = [line[2:].strip() for line in block.splitlines() if line.startswith("- ")]
    missing = [t for t in h2 if t not in entries]
    extra = [e for e in entries if e not in h2]
    if missing or extra:
        return False, "缺条目 %s；多条目 %s" % ("、".join(missing) or "无", "、".join(extra) or "无")
    return True, "H2 %d 条与索引一致" % len(h2)


def run_checks(root: pathlib.Path):
    p = _paths(root)
    rows = []

    # E1 ADR 必填字段
    adrs = _adr_files(p["adr_dir"])
    if not adrs:
        rows.append(("E1", "ADR 十二项必填字段", False, "未找到 ADR 文件：%s" % p["adr_dir"]))
    else:
        bad = []
        for adr in adrs:
            text = _read(adr)
            missing = [f for f in ADR_FIELDS if not _has_field(text, f)]
            if missing:
                bad.append("%s 缺 %s" % (adr.name, "、".join(missing)))
        rows.append(("E1", "ADR 十二项必填字段", not bad,
                     "；".join(bad) if bad else "ADR %d 件，字段齐全" % len(adrs)))

    # E2 ADR 索引、编号、状态与日期
    e2_bad = []
    index_text = _read(p["index"])
    numbers = {}
    for adr in adrs:
        m = re.match(r"ADR-(\d{4})-", adr.name)
        if not m:
            e2_bad.append("%s 编号不匹配 ADR-NNNN-" % adr.name)
            continue
        num = m.group(1)
        numbers.setdefault(num, []).append(adr.name)
        text = _read(adr)
        if not _has_field(text, "状态"):
            e2_bad.append("%s 缺状态" % adr.name)
        if not _has_field(text, "日期"):
            e2_bad.append("%s 缺日期" % adr.name)
        if adr.name not in index_text and adr.stem not in index_text:
            e2_bad.append("%s 未入 index.md" % adr.name)
    for num, names in sorted(numbers.items()):
        if len(names) > 1:
            e2_bad.append("编号 %s 重复：%s" % (num, "／".join(names)))
    rows.append(("E2", "ADR 索引、编号、状态与日期", not e2_bad,
                 "；".join(e2_bad) if e2_bad else "ADR %d 件，索引与编号一致" % len(adrs)))

    # E3 技术债字段、承担者与状态
    debt_text = _read(p["debt"])
    header, debt_rows, err = _parse_debt(debt_text)
    e3_bad = []
    if err:
        e3_bad.append(err)
    else:
        if header != DEBT_COLUMNS:
            e3_bad.append("表头应为 %s，实为 %s" % (" | ".join(DEBT_COLUMNS), " | ".join(header)))
        if not debt_rows:
            e3_bad.append("无技术债数据行")
        for i, cells in enumerate(debt_rows, start=1):
            if len(cells) != len(DEBT_COLUMNS):
                e3_bad.append("第 %d 行列数 %d≠%d" % (i, len(cells), len(DEBT_COLUMNS)))
                continue
            record = dict(zip(DEBT_COLUMNS, cells))
            if any(not v for v in cells):
                e3_bad.append("第 %d 行有空单元格" % i)
            if record["承担者"] in BAD_OWNERS:
                e3_bad.append("第 %d 行承担者无效：%s" % (i, record["承担者"]))
            if record["状态"] not in DEBT_STATUS:
                e3_bad.append("第 %d 行状态非法：%s" % (i, record["状态"]))
            if "后续补" in "".join(cells):
                e3_bad.append("第 %d 行含“后续补”" % i)
    rows.append(("E3", "技术债字段、承担者与状态", not e3_bad,
                 "；".join(e3_bad) if e3_bad else "技术债 %d 行" % len(debt_rows)))

    # E4 模板接线
    rule_text = _read(p["rule"])
    tpl_readme = _read(p["templates"] / "00-模板说明.md")
    e4_bad = []
    if not (p["templates"] / "00-模板说明.md").exists():
        e4_bad.append("缺 00-模板说明.md")
    if p["templates"].is_dir():
        for tpl in sorted(p["templates"].glob("模板*.md")):
            if tpl.name not in rule_text and tpl.name not in tpl_readme:
                e4_bad.append("%s 未被规则或模板说明引用" % tpl.name)
    for name in sorted(set(re.findall(r"模板[A-Z]-[^\s`）]+\.md", rule_text))):
        if not (p["templates"] / name).exists():
            e4_bad.append("规则引用的模板不存在：%s" % name)
    rows.append(("E4", "模板存在且被引用", not e4_bad,
                 "；".join(e4_bad) if e4_bad else "模板接线一致"))

    # E5 规则登记与门禁接线
    e5_bad = []
    if not p["rule"].exists():
        e5_bad.append("缺 工程实践规则.md")
    if "工程实践规则.md" not in _read(p["rule_readme"]):
        e5_bad.append("01-规则/README.md 未登记 工程实践规则.md")
    if "工程实践规则.md" not in _read(p["agents"]):
        e5_bad.append("AGENTS.md 未登记 工程实践规则.md")
    if "工程实践生命周期与阶段门禁" not in _read(p["flow"]):
        e5_bad.append("流程规则.md 缺 G0–G5 节")
    if "audit_engineering_practice.py" not in _read(p["cmd_readme"]):
        e5_bad.append("脚本与命令/README.md 未登记 audit_engineering_practice.py")
    if "audit_engineering_practice.py" not in _read(p["registry"]):
        e5_bad.append("audit_gate_registry.py 未登记 audit_engineering_practice.py")
    rows.append(("E5", "规则登记与门禁接线", not e5_bad,
                 "；".join(e5_bad) if e5_bad else "接线一致"))

    # E6 复审日期（过期仅 WARN）
    rule_date = _review_date(rule_text)
    adr_dates = []
    for adr in adrs:
        d = _review_date(_read(adr))
        if d:
            adr_dates.append(d)
    e6_bad = []
    if not rule_date:
        e6_bad.append("工程实践规则.md 缺 复审日期：YYYY-MM-DD")
    if adrs and not adr_dates:
        e6_bad.append("ADR 均缺 复审日期：YYYY-MM-DD")
    rows.append(("E6", "复审日期存在", not e6_bad,
                 "；".join(e6_bad) if e6_bad else "规则 %s；ADR %d 件有复审日期"
                 % (rule_date or "未填", len(adr_dates))))

    # E7 流程规则二级索引与 H2 标题一致
    e7_ok, e7_detail = _flow_index_check(_read(p["flow"]))
    rows.append(("E7", "流程规则二级索引与 H2 标题一致", e7_ok, e7_detail))
    return rows, rule_date


def _report(rows, title):
    print("=" * 72)
    print(title)
    print("=" * 72)
    fails = 0
    for code, name, ok, detail in rows:
        print("  [%s] %-4s %s" % ("PASS" if ok else "FAIL", code, name))
        print("           %s" % detail)
        if not ok:
            fails += 1
    print("-" * 72)
    print("  合计 %d 项，FAIL %d 项" % (len(rows), fails))
    return fails


def _write_fixture(root: pathlib.Path):
    p = _paths(root)
    p["rule_dir"].mkdir(parents=True, exist_ok=True)
    p["cmd_readme"].parent.mkdir(parents=True, exist_ok=True)
    p["adr_dir"].mkdir(parents=True, exist_ok=True)
    p["templates"].mkdir(parents=True, exist_ok=True)
    adr = p["adr_dir"] / "ADR-0001-test.md"
    adr.write_text(
        "# ADR-0001：测试\n\n"
        "- **状态**：已接受\n- **日期**：2026-10-22\n- **复审日期**：2027-01-22\n\n"
        + "\n".join("- %s：x" % f for f in ADR_FIELDS)
        + "\n",
        encoding="utf-8",
    )
    p["index"].write_text("# 索引\n\n| ADR-0001-test.md | x |\n", encoding="utf-8")
    p["debt"].write_text(
        "# 技术债\n\n| ID | 描述 | 来源 | 影响 | 承担者 | 偿还条件 | 复审日期或触发 | 状态 |\n"
        "| --- | --- | --- | --- | --- | --- | --- | --- |\n"
        "| TD-001 | x | audit | x | 主代理 | x | 2027-01-22 | 未偿还 |\n",
        encoding="utf-8",
    )
    for name in ("模板G-架构决策记录.md", "模板H-技术债登记.md",
                 "模板I-批次提交核对清单.md", "模板J-工程实践复审.md"):
        (p["templates"] / name).write_text("# %s\n" % name, encoding="utf-8")
    (p["templates"] / "00-模板说明.md").write_text(
        "# 说明\n\n模板G-架构决策记录.md 模板H-技术债登记.md "
        "模板I-批次提交核对清单.md 模板J-工程实践复审.md\n",
        encoding="utf-8",
    )
    p["rule"].write_text(
        "# 工程实践规则\n\n- **复审日期**：2027-01-22\n\n"
        "模板G-架构决策记录.md 模板H-技术债登记.md "
        "模板I-批次提交核对清单.md 模板J-工程实践复审.md\n",
        encoding="utf-8",
    )
    p["rule_readme"].write_text("工程实践规则.md\n", encoding="utf-8")
    p["agents"].write_text("工程实践规则.md\n", encoding="utf-8")
    p["flow"].write_text(
        "## 工程实践生命周期与阶段门禁（G0–G5）\n\n"
        "**二级索引（按域）**\n\n"
        "<!-- FLOW_INDEX_BEGIN -->\n"
        "- 工程实践生命周期与阶段门禁（G0–G5）\n"
        "<!-- FLOW_INDEX_END -->\n",
        encoding="utf-8",
    )
    p["cmd_readme"].write_text("audit_engineering_practice.py\n", encoding="utf-8")
    p["registry"].write_text("audit_engineering_practice.py\n", encoding="utf-8")


def _failed_codes(root: pathlib.Path):
    rows, _ = run_checks(root)
    return {code for code, _n, ok, _d in rows if not ok}


def cmd_selftest():
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="engprac_"))
    failures = []
    try:
        _write_fixture(tmp)
        got = _failed_codes(tmp)
        if got:
            failures.append("正样本应 0 FAIL，实际 %s" % sorted(got))

        cases = [
            ("E1", lambda: (tmp / "01-项目管理/02-工程决策与技术债/ADR/ADR-0001-test.md")
             .write_text("# ADR\n- **状态**：已接受\n- **日期**：2026-10-22\n", encoding="utf-8")),
            ("E2", lambda: (tmp / "01-项目管理/02-工程决策与技术债/index.md")
             .write_text("# 索引\n\n无\n", encoding="utf-8")),
            ("E3", lambda: (tmp / "01-项目管理/02-工程决策与技术债/技术债登记.md")
             .write_text("# 技术债\n\n| ID | 描述 | 来源 | 影响 | 承担者 | 偿还条件 | 复审日期或触发 | 状态 |\n"
                         "| --- | --- | --- | --- | --- | --- | --- | --- |\n"
                         "| TD-001 | x | x | x |  | x | x | 未偿还 |\n", encoding="utf-8")),
            ("E4", lambda: (tmp / "00-编纂规则与格式规范/02-操作手册/14-工程实践模板/模板G-架构决策记录.md").unlink()),
            ("E5", lambda: (tmp / "00-编纂规则与格式规范/01-规则/README.md")
             .write_text("无\n", encoding="utf-8")),
            ("E6", lambda: (tmp / "00-编纂规则与格式规范/01-规则/工程实践规则.md")
             .write_text("# 工程实践规则\n\n模板G-架构决策记录.md\n", encoding="utf-8")),
            ("E7", lambda: (tmp / "00-编纂规则与格式规范/01-规则/流程规则.md")
             .write_text("## 工程实践生命周期与阶段门禁（G0–G5）\n\n"
                         "**二级索引（按域）**\n\n"
                         "<!-- FLOW_INDEX_BEGIN -->\n"
                         "- 别的标题\n"
                         "<!-- FLOW_INDEX_END -->\n", encoding="utf-8")),
        ]
        for code, mutate in cases:
            _write_fixture(tmp)
            mutate()
            got = _failed_codes(tmp)
            if code not in got:
                failures.append("%s 负向夹具未被命中（实际 %s）" % (code, sorted(got)))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    if failures:
        print("  ❌ 判据非空自检失败：")
        for f in failures:
            print("     - %s" % f)
        return 1
    print("  ✅ 判据非空自检通过：正样本 0 FAIL；E1–E7 七类负向夹具均命中")
    return 0


def main():
    ap = argparse.ArgumentParser(description="工程实践基线门禁（第二十九件）")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--root", metavar="<仓库根>", help="指定仓库根（默认本文件上溯三层）")
    args = ap.parse_args()

    if args.selftest:
        return cmd_selftest()

    root = pathlib.Path(args.root).resolve() if args.root else REPO
    if args.list:
        print("对象：")
        for key in ("rule", "rule_readme", "flow", "agents", "gov", "adr_dir",
                    "index", "debt", "templates", "cmd_readme", "registry"):
            print("  %-10s %s" % (key, _paths(root)[key]))
        return 0

    rows, rule_date = run_checks(root)
    fails = _report(rows, "工程实践基线门禁（第二十九件）")
    if rule_date:
        try:
            due = datetime.date.fromisoformat(rule_date)
            if (datetime.date.today() - due).days > 0:
                print("  [WARN] E6 复审日期已过：%s（不判 FAIL，但应在下批前复审）" % rule_date)
        except ValueError:
            print("  [WARN] E6 复审日期格式无法解析：%s" % rule_date)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
