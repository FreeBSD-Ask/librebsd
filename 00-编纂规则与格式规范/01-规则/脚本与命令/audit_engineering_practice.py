# -*- coding: utf-8 -*-
"""audit_engineering_practice.py —— 第二十九件门禁：工程实践基线。

对象
----
- `01-项目管理/02-工程决策与技术债/ADR/ADR-*.md`：必填字段、索引、编号、状态与日期
- `01-项目管理/02-工程决策与技术债/技术债登记.md`：表字段、承担者、状态
- `00-编纂规则与格式规范/02-操作手册/14-工程实践模板/`：模板接线
- `00-编纂规则与格式规范/01-规则/工程实践规则.md`：规则登记与复审日期
- `流程规则.md`（拆分后为转发索引存根）与 `流程规则/`：分册索引与各分册 H2 逐条一致
- `01-规则/README.md`、`AGENTS.md`、`脚本与命令/README.md`、`audit_gate_registry.py`：接线

判据
----
E1 ADR 十二项必填字段
E2 ADR 索引、编号、状态与日期
E3 技术债表字段、承担者与状态
E4 模板存在且被规则或模板说明引用；规则引用的模板存在
E5 规则登记与门禁接线
E6 复审日期存在；过期仅 WARN，不判 FAIL
E7 `流程规则.md` 存根内的分册索引表与 `流程规则/` 全部 H2 标题逐条一致
   （2026-10-29 随 2026-10-27 拆分改造：原“单文件 H2 ↔ 列表行”判据在拆分后无对象，
   改为跨分册校验，并逐行核对链接指向的分册内确有该 H2）
E7b `流程规则/00-索引.md` 总索引（2026-11-06 立，ykla“重复行合并去重＋建立机制”令）：
   D1 分册表每分册恰一行（重复路径行＝历史缺陷，直接 FAIL）；
   D2 行目标分册存在，单元格内小节（`<br>` 分隔）逐条属于该分册 H2 且行内无重复；
   D3 各分册 H2 全部登记（表 ↔ H2 双向一致）；
   D4 FLOW_INDEX 块 bullet 与全体 H2 多重集一致（缺项、重复、多出皆 FAIL）。
E8 意图确证接线（理论件／全局节／G0／AGENTS／模板 I）
E11 角色卡与技能模板接线（agents 4／skills 4／plugin.json／README 登记）
E13 标准化文献先行阅读接线（理论件／README 登记／工程实践规则 §0.8／AGENTS／模板 I；
   2026-11-14 立，TG-016）

用法
----
    python audit_engineering_practice.py            # 0 通过 / 1 不通过
    python audit_engineering_practice.py --selftest # 判据非空自检（正样本 + 负向夹具逐类命中）
    python audit_engineering_practice.py --list     # 打印检查对象

依赖：仅标准库。
"""

import argparse
import collections
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
INTENT_KEYS = ["用户原话", "目标", "非目标", "验收判据", "手段自由度", "未知"]
FLOW_INTENT_KEYS = ["全任务适用", "档 A", "档 B"]
STD_KEYS = ["知难行易", "启发式阅读", "吃透", "落地", "失效条件"]


def _paths(root: pathlib.Path):
    rule_dir = root / "00-编纂规则与格式规范" / "01-规则"
    gov = root / "01-项目管理" / "02-工程决策与技术债"
    return {
        "rule_dir": rule_dir,
        "rule": rule_dir / "工程实践规则.md",
        "rule_readme": rule_dir / "README.md",
        "flow": rule_dir / "流程规则.md",
        "flow_dir": rule_dir / "流程规则",
        "cmd_readme": rule_dir / "脚本与命令" / "README.md",
        "registry": rule_dir / "脚本与命令" / "audit_gate_registry.py",
        "agents": root / "AGENTS.md",
        "gov": gov,
        "adr_dir": gov / "ADR",
        "index": gov / "index.md",
        "debt": gov / "技术债登记.md",
        "templates": root / "00-编纂规则与格式规范" / "02-操作手册" / "14-工程实践模板",
        "doctrine": root / "13-软件工程" / "08-intent-first.md",
        "doctrine10": root / "13-软件工程" / "10-standards-first.md",
        "doctrine_readme": root / "13-软件工程" / "README.md",
        "templ_i": root / "00-编纂规则与格式规范" / "02-操作手册" / "14-工程实践模板"
                   / "模板I-批次提交核对清单.md",
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


FLOW_ROW_RE = re.compile(r"(?m)^\|\s*\[[^\]]*\]\(([^)]+)\)\s*\|\s*(.+?)\s*\|\s*$")
FLOW_PART_RE = re.compile(r"^\d\d-.+\.md$")


def _flow_h2_map(flow_dir: pathlib.Path):
    """分册 H2 清单 {分册文件名: [H2, ...]}。

    分册集合＝`流程规则/NN-*.md` 且 NN≠00：`00-索引.md` 的 H2 是原文导言标题
    （H1 降级为 H3 以免双 H1 的约定），属容器文件，不是可登记规则小节。
    """
    out = {}
    if not flow_dir.is_dir():
        return out
    for f in sorted(flow_dir.glob("*.md")):
        if not FLOW_PART_RE.match(f.name) or f.name.startswith("00-"):
            continue
        hs = [m.group(1).strip() for m in re.finditer(r"(?m)^##\s+(.+?)\s*$", _read(f))]
        out[f.name] = hs
    return out


def _flow_part_texts(flow_dir: pathlib.Path):
    """分册正文 [(文件名, 文本)]；分册集合口径同 `_flow_h2_map`（NN≠00）。"""
    out = []
    if not flow_dir.is_dir():
        return out
    for f in sorted(flow_dir.glob("*.md")):
        if not FLOW_PART_RE.match(f.name) or f.name.startswith("00-"):
            continue
        out.append((f.name, _read(f)))
    return out


def _h2_section(text: str, needle: str) -> str:
    """取标题含 needle 的首个顶层 H2 所在整节正文（自该 `##` 行至下一 `##` 行或文件末）。

    顶层 H2 判定为正则 `^##` 后接空白：`### ` 第三字符为 `#`，不匹配，故三级标题不会截断本节。
    未找到含 needle 的 H2 时返回空串。
    """
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if re.match(r"^##\s", line) and needle in line:
            start = i
            break
    if start is None:
        return ""
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if re.match(r"^##\s", lines[j]):
            end = j
            break
    return "\n".join(lines[start:end])


def _flow_index_check(text: str, flow_dir: pathlib.Path):
    """存根分册索引 ↔ 各分册 H2 逐条一致（2026-10-29 跨分册改造，见模块 docstring E7）。"""
    if INDEX_BEGIN not in text or INDEX_END not in text:
        return False, "缺 FLOW_INDEX_BEGIN／FLOW_INDEX_END 标记"
    block = text.split(INDEX_BEGIN, 1)[1].split(INDEX_END, 1)[0]
    rows = [(m.group(1).strip(), m.group(2).strip()) for m in FLOW_ROW_RE.finditer(block)]
    h2map = _flow_h2_map(flow_dir)
    if not h2map:
        return False, "未找到分册：%s" % flow_dir
    if not rows:
        return False, "索引块内无“分册链接 | 小节”表格行"
    covered, bad = {}, []
    for target, title in rows:
        name = target.rsplit("/", 1)[-1]
        if name not in h2map:
            bad.append("%s（分册不存在）" % target)
        elif title not in h2map[name]:
            bad.append("%s 无 H2“%s”" % (name, title))
        else:
            covered.setdefault(name, set()).add(title)
    missing = ["%s：%s" % (n, h) for n, hs in h2map.items()
               for h in hs if h not in covered.get(n, set())]
    if bad or missing:
        return False, "错指 %d 条%s；未登记 %d 条%s" % (
            len(bad), "（%s）" % "、".join(bad[:3]) if bad else "",
            len(missing), "（%s）" % "、".join(missing[:3]) if missing else "")
    return True, "分册 %d 件／H2 %d 条与索引 %d 行一致" % (
        len(h2map), sum(len(v) for v in h2map.values()), len(rows))


def _flow_index00_check(flow_dir: pathlib.Path):
    """总索引 00-索引.md 判据（E7b，2026-11-06 立，ykla“重复行合并去重＋建立机制”令）。

    分册表历史上每小节一行，同分册路径随小节增长不断重复（实测 65 行仅 11 个分册），
    且曾混入分册中不存在的幻影行、FLOW_INDEX 块漏登新 H2——存根有 E7 看护而总索引无人看护。
    判据：D1 每分册恰一行（重复路径行 FAIL）；D2 行目标分册存在、单元格小节（`<br>` 分隔）
    逐条属于该分册 H2 且行内无重复；D3 各分册 H2 全部登记（双向一致）；
    D4 FLOW_INDEX 块 bullet 与全体 H2 多重集一致。
    """
    path = flow_dir / "00-索引.md"
    if not path.exists():
        return False, "缺 %s" % path.name
    text = _read(path)
    if INDEX_BEGIN not in text or INDEX_END not in text:
        return False, "缺 FLOW_INDEX_BEGIN／FLOW_INDEX_END 标记"
    head = text.split(INDEX_BEGIN, 1)[0]
    rows = [(m.group(1).strip(), m.group(2).strip()) for m in FLOW_ROW_RE.finditer(head)]
    h2map = _flow_h2_map(flow_dir)
    if not h2map:
        return False, "未找到分册：%s" % flow_dir
    if not rows:
        return False, "总索引无“分册链接 | 原小节”表格行"
    bad, dup, covered = [], [], {}
    for target, cell in rows:
        name = target.rsplit("/", 1)[-1]
        if name in covered:
            dup.append(name)
            continue
        titles, cseen = [t.strip() for t in cell.split("<br>") if t.strip()], set()
        for t in titles:
            if t in cseen:
                bad.append("%s 行内重复“%s”" % (name, t))
            elif t not in h2map.get(name, set()):
                bad.append("%s 无 H2“%s”" % (name, t))
            cseen.add(t)
        covered[name] = cseen
    if dup:
        bad.insert(0, "重复路径行：%s" % "、".join(sorted(set(dup))))
    missing = ["%s：%s" % (n, h) for n, hs in h2map.items()
               for h in hs if h not in covered.get(n, set())]
    block = text.split(INDEX_BEGIN, 1)[1].split(INDEX_END, 1)[0]
    bullets = []
    for m in re.finditer(r"(?m)^-\s+(.+?)\s*$", block):
        t = m.group(1).replace(INDEX_END, "").strip()
        if t:
            bullets.append(t)
    hcount = collections.Counter(h for hs in h2map.values() for h in hs)
    bcount = collections.Counter(bullets)
    bextra = sorted((bcount - hcount).elements())
    bmiss = sorted((hcount - bcount).elements())
    if bad or missing or bextra or bmiss:
        parts = []
        if bad:
            parts.append("错指/重复 %d 条（%s）" % (len(bad), "、".join(bad[:3])))
        if missing:
            parts.append("未登记 %d 条（%s）" % (len(missing), "、".join(missing[:3])))
        if bextra:
            parts.append("bullet 块多出/重复 %d 条（%s）" % (len(bextra), "、".join(bextra[:3])))
        if bmiss:
            parts.append("bullet 块缺 %d 条（%s）" % (len(bmiss), "、".join(bmiss[:3])))
        return False, "；".join(parts)
    return True, "分册 %d 件／H2 %d 条：总索引表 %d 行（每分册一行）与 bullet %d 条全部一致" % (
        len(h2map), sum(hcount.values()), len(rows), len(bullets))


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
    e7_ok, e7_detail = _flow_index_check(_read(p["flow"]), p["flow_dir"])
    rows.append(("E7", "流程规则二级索引与 H2 标题一致", e7_ok, e7_detail))

    # E7b 流程规则总索引（00-索引.md）：分册表去重与 H2 双向一致（2026-11-06 立）
    e7b_ok, e7b_detail = _flow_index00_check(p["flow_dir"])
    rows.append(("E7b", "流程规则总索引（00-索引.md）分册表去重与 H2 一致", e7b_ok, e7b_detail))

    # E8 意图确证接线（理论件／全局节／G0／AGENTS／模板 I）
    e8_bad = []
    if not p["doctrine"].exists():
        e8_bad.append("缺 13-软件工程/08-intent-first.md")
    else:
        doctrine_text = _read(p["doctrine"])
        lack = []
        for k in INTENT_KEYS:
            # “目标”不得被“非目标”子串满足（负向后视排除“非”前缀）
            if k == "目标":
                if re.search(r"(?<!非)目标", doctrine_text) is None:
                    lack.append(k)
            elif k not in doctrine_text:
                lack.append(k)
        if lack:
            e8_bad.append("08-intent-first.md 缺字段关键词：%s" % "、".join(lack))
    readme_lines = _read(p["doctrine_readme"]).splitlines()
    if not any(line.strip().startswith("|") and "08-intent-first.md" in line
               for line in readme_lines):
        e8_bad.append("13-软件工程/README.md 未在表格行登记 08-intent-first.md")
    parts = _flow_part_texts(p["flow_dir"])
    sec_ok = False
    for _name, text in parts:
        # 三关键词只在含“意图确证”的顶层 H2 整节正文内判定，避免节外文字误满足
        sec = _h2_section(text, "意图确证")
        if sec and all(k in sec for k in FLOW_INTENT_KEYS):
            sec_ok = True
            break
    if not sec_ok:
        e8_bad.append("流程规则/ 分册无顶层 H2 含“意图确证”且该节正文含 %s"
                      % "、".join(FLOW_INTENT_KEYS))
    g0_ok = any(re.match(r"^\|\s*G0\s*\|", line) and "意图" in line
                for _n, text in parts for line in text.splitlines())
    if not g0_ok:
        e8_bad.append("流程规则/ 分册无“| G0 |”开头且含“意图”的表格行")
    if "意图确证" not in rule_text or "08-intent-first.md" not in rule_text:
        e8_bad.append("工程实践规则.md 缺“意图确证”或 08-intent-first.md 引用")
    agents_ok = any("意图确证" in line and ("所有任务" in line or "任何任务" in line)
                    for line in _read(p["agents"]).splitlines())
    if not agents_ok:
        e8_bad.append("AGENTS.md 无同一行含“意图确证”与“所有任务／任何任务”")
    if not p["templ_i"].exists() or "意图确证" not in _read(p["templ_i"]):
        e8_bad.append("模板I-批次提交核对清单.md 缺失或未含“意图确证”")
    rows.append(("E8", "意图确证接线", not e8_bad,
                 "；".join(e8_bad) if e8_bad else
                 "理论件／全局节／G0／AGENTS／模板 I 接线一致"))

    # E11 角色卡与技能模板接线（Task 12.5，2026-11-06 立）
    e11_bad = []
    tdir = p["doctrine"].parent / "templates"
    AGENT_FIELDS = ["职责", "输入", "输出", "禁止", "交接"]
    SKILL_FIELDS = ["触发", "步骤", "产物", "判据", "失效"]
    agents = {"title-designer": AGENT_FIELDS, "block-triage": AGENT_FIELDS,
              "gate-reviewer": AGENT_FIELDS, "volume-merger": AGENT_FIELDS}
    skills = {"four-source-title": SKILL_FIELDS, "gate-runner": SKILL_FIELDS,
              "milestone-tag": SKILL_FIELDS, "volume-parallel": SKILL_FIELDS}
    adir, sdir = tdir / "agents", tdir / "skills"
    for name, fields in agents.items():
        f = adir / ("%s.md" % name)
        if not f.exists():
            e11_bad.append("角色卡缺失：%s" % f.name)
            continue
        txt = _read(f)
        miss = [x for x in fields if ("## %s" % x) not in txt]
        if miss:
            e11_bad.append("角色卡 %s 缺字段 %s" % (name, "、".join(miss)))
    for name, fields in skills.items():
        f = sdir / ("%s.md" % name)
        if not f.exists():
            e11_bad.append("技能缺失：%s" % f.name)
            continue
        txt = _read(f)
        miss = [x for x in fields if ("## %s" % x) not in txt]
        if miss:
            e11_bad.append("技能 %s 缺字段 %s" % (name, "、".join(miss)))
    pj = tdir / "qoder-plugin" / "plugin.json"
    if not pj.exists():
        e11_bad.append("plugin.json 缺失")
    else:
        try:
            import json as _json
            data = _json.loads(_read(pj))
            for kind, expect_dir, n in (("agents", "agents", 4), ("skills", "skills", 4)):
                lst = data.get(kind) or []
                if len(lst) != n:
                    e11_bad.append("plugin.json %s 应 %d 条，实 %d" % (kind, n, len(lst)))
                for it in lst:
                    ref = tdir / "qoder-plugin" / (it.get("file") or "")
                    if not ref.exists():
                        e11_bad.append("plugin.json %s 引用不可达：%s" % (kind, it.get("file")))
        except Exception as _e:
            e11_bad.append("plugin.json 解析失败：%s" % _e)
    readme13 = _read(p["doctrine"].parent / "README.md")
    if "templates/agents" not in readme13 or "templates/skills" not in readme13:
        e11_bad.append("13-软件工程/README.md 未登记 templates/agents 与 templates/skills")
    rows.append(("E11", "角色卡与技能模板接线", not e11_bad,
                 "；".join(e11_bad) if e11_bad else
                 "角色卡 4／技能 4／plugin.json 引用可达／README 登记一致"))

    # E13 标准化文献先行阅读接线（2026-11-14 立，TG-016）
    e13_bad = []
    if not p["doctrine10"].exists():
        e13_bad.append("缺 13-软件工程/10-standards-first.md")
    else:
        d10 = _read(p["doctrine10"])
        lack = [k for k in STD_KEYS if k not in d10]
        if lack:
            e13_bad.append("10-standards-first.md 缺关键词：%s" % "、".join(lack))
    readme13 = _read(p["doctrine_readme"]).splitlines()
    if not any(line.strip().startswith("|") and "10-standards-first.md" in line
               for line in readme13):
        e13_bad.append("13-软件工程/README.md 未在表格行登记 10-standards-first.md")
    if "0.8 标准化文献先行阅读" not in rule_text or "10-standards-first.md" not in rule_text:
        e13_bad.append("工程实践规则.md 缺 §0.8 节或 10-standards-first.md 引用")
    agents13_ok = any("标准化文献" in line and "工程实践规则.md" in line
                      for line in _read(p["agents"]).splitlines())
    if not agents13_ok:
        e13_bad.append("AGENTS.md 无同一行含“标准化文献”与“工程实践规则.md”")
    if not p["templ_i"].exists() or "标准化文献" not in _read(p["templ_i"]):
        e13_bad.append("模板I-批次提交核对清单.md 缺失或未含“标准化文献”项")
    rows.append(("E13", "标准化文献先行阅读接线", not e13_bad,
                 "；".join(e13_bad) if e13_bad else
                 "理论件／README 登记／§0.8／AGENTS 行／模板 I 接线一致"))
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
                 "模板J-工程实践复审.md"):
        (p["templates"] / name).write_text("# %s\n" % name, encoding="utf-8")
    p["templ_i"].write_text(
        "# 模板I\n- [ ] 意图确证单已写\n- [ ] 标准化文献清单已锁定并完成四问抽取\n",
        encoding="utf-8")
    (p["templates"] / "00-模板说明.md").write_text(
        "# 说明\n\n模板G-架构决策记录.md 模板H-技术债登记.md "
        "模板I-批次提交核对清单.md 模板J-工程实践复审.md\n",
        encoding="utf-8",
    )
    p["rule"].write_text(
        "# 工程实践规则\n\n- **复审日期**：2027-01-22\n\n"
        "模板G-架构决策记录.md 模板H-技术债登记.md "
        "模板I-批次提交核对清单.md 模板J-工程实践复审.md\n"
        "意图确证 见 08-intent-first.md\n\n"
        "## 0.8 标准化文献先行阅读\n\n判据见 10-standards-first.md\n",
        encoding="utf-8",
    )
    p["rule_readme"].write_text("工程实践规则.md\n", encoding="utf-8")
    p["doctrine"].parent.mkdir(parents=True, exist_ok=True)
    p["doctrine"].write_text(
        "# 知难行易：意图确证先于手段\n\n"
        "档 A：用户原话、目标、非目标、验收判据、手段自由度、未知\n",
        encoding="utf-8",
    )
    p["doctrine10"].write_text(
        "# 10 标准先行：开工前标准化文献启发式阅读\n\n"
        "知难行易第二体现：开工前分级检索标准化文献，启发式阅读后吃透并落地；失效条件见下。\n",
        encoding="utf-8",
    )
    p["doctrine_readme"].write_text(
        "# 13-软件工程\n\n| 文件 | 内文 | 必读 |\n| ---- | ---- | ---- |\n"
        "| `08-intent-first.md` | x | 是 |\n"
        "| `10-standards-first.md` | x | 是 |\n\n"
        "templates/agents 与 templates/skills：角色卡与技能模板见 templates/qoder-plugin/README.md。\n",
        encoding="utf-8",
    )
    p["agents"].write_text(
        "工程实践规则.md\n任何任务开工前先写意图确证（所有任务）\n"
        "工程类批次开工前的标准化文献启发式阅读（工程实践规则.md §0.8）\n",
        encoding="utf-8")
    p["flow_dir"].mkdir(parents=True, exist_ok=True)
    (p["flow_dir"] / "01-测试分册.md").write_text(
        "# 测试分册\n\n## 工程实践生命周期与阶段门禁（G0–G5）\n\n"
        "## 意图确证（知难行易；全任务适用；2026-10-29 立）\n\n"
        "全任务适用（不限工程类批次）；档 A：全量六字段；档 B：轻量三要素。\n\n"
        "| 阶段 | 名称 | 活动 | 退出判据 |\n"
        "| ---- | ---- | ---- | ---- |\n"
        "| G0 | 立项与范围 | 写意图确证 | 意图确证单已写 |\n",
        encoding="utf-8")
    p["flow"].write_text(
        "# 流程规则（转发索引存根）\n\n"
        "<!-- FLOW_INDEX_BEGIN -->\n\n"
        "| 分册 | 原小节 |\n"
        "| ---- | ------ |\n"
        "| [流程规则/01-测试分册.md](流程规则/01-测试分册.md) "
        "| 工程实践生命周期与阶段门禁（G0–G5） |\n"
        "| [流程规则/01-测试分册.md](流程规则/01-测试分册.md) "
        "| 意图确证（知难行易；全任务适用；2026-10-29 立） |\n\n"
        "<!-- FLOW_INDEX_END -->\n",
        encoding="utf-8",
    )
    # E7b 正样本夹具（2026-11-06 立）：总索引每分册恰一行＋bullet 块与 H2 一致
    (p["flow_dir"] / "00-索引.md").write_text(
        "# 流程规则·总索引\n\n"
        "| 分册 | 原小节 |\n"
        "| ---- | ------ |\n"
        "| [01-测试分册.md](01-测试分册.md) "
        "| 工程实践生命周期与阶段门禁（G0–G5）<br>意图确证（知难行易；全任务适用；2026-10-29 立） |\n\n"
        "<!-- FLOW_INDEX_BEGIN -->\n\n"
        "- 工程实践生命周期与阶段门禁（G0–G5）\n"
        "- 意图确证（知难行易；全任务适用；2026-10-29 立）<!-- FLOW_INDEX_END -->\n",
        encoding="utf-8",
    )
    p["cmd_readme"].write_text("audit_engineering_practice.py\n", encoding="utf-8")
    p["registry"].write_text("audit_engineering_practice.py\n", encoding="utf-8")
    # E11 正样本夹具（2026-11-06 立）：4 角色卡／4 技能／plugin.json／README 登记
    _t13 = p["doctrine"].parent / "templates"
    for _d in ("agents", "skills", "qoder-plugin"):
        (_t13 / _d).mkdir(parents=True, exist_ok=True)
    for _n in ("title-designer", "block-triage", "gate-reviewer", "volume-merger"):
        (_t13 / "agents" / ("%s.md" % _n)).write_text(
            "# %s\n\n## 职责\nx\n## 输入\nx\n## 输出\nx\n## 禁止\nx\n## 交接\nx\n" % _n,
            encoding="utf-8")
    for _n in ("four-source-title", "gate-runner", "milestone-tag", "volume-parallel"):
        (_t13 / "skills" / ("%s.md" % _n)).write_text(
            "# %s\n\n## 触发\nx\n## 步骤\nx\n## 产物\nx\n## 判据\nx\n## 失效\nx\n" % _n,
            encoding="utf-8")
    (_t13 / "qoder-plugin" / "plugin.json").write_text(
        '{"agents":[{"file":"../agents/title-designer.md"},{"file":"../agents/block-triage.md"},'
        '{"file":"../agents/gate-reviewer.md"},{"file":"../agents/volume-merger.md"}],'
        '"skills":[{"file":"../skills/four-source-title.md"},{"file":"../skills/gate-runner.md"},'
        '{"file":"../skills/milestone-tag.md"},{"file":"../skills/volume-parallel.md"}]}',
        encoding="utf-8")


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
            ("E7", lambda: (tmp / "00-编纂规则与格式规范/01-规则/流程规则.md").write_text(
                "# 流程规则（转发索引存根）\n\n"
                "<!-- FLOW_INDEX_BEGIN -->\n\n"
                "| 分册 | 原小节 |\n"
                "| ---- | ------ |\n"
                "| [流程规则/01-测试分册.md](流程规则/01-测试分册.md) | 别的标题 |\n\n"
                "<!-- FLOW_INDEX_END -->\n", encoding="utf-8")),
            # E7 负向之二（2026-10-29 随跨分册改造补）：分册新增 H2 而存根未登记
            ("E7", lambda: (tmp / "00-编纂规则与格式规范/01-规则/流程规则/01-测试分册.md")
             .write_text("# 测试分册\n\n## 工程实践生命周期与阶段门禁（G0–G5）\n\n"
                         "## 新增未登记小节\n", encoding="utf-8")),
            # E7b 负向之一（2026-11-06 立）：同分册另起新行（重复路径行，ykla 去重令的主对象）
            ("E7b", lambda: (tmp / "00-编纂规则与格式规范/01-规则/流程规则/00-索引.md").write_text(
                "# 流程规则·总索引\n\n| 分册 | 原小节 |\n| ---- | ------ |\n"
                "| [01-测试分册.md](01-测试分册.md) | 工程实践生命周期与阶段门禁（G0–G5）<br>意图确证（知难行易；全任务适用；2026-10-29 立） |\n"
                "| [01-测试分册.md](01-测试分册.md) | 意图确证（知难行易；全任务适用；2026-10-29 立） |\n\n"
                "<!-- FLOW_INDEX_BEGIN -->\n\n"
                "- 工程实践生命周期与阶段门禁（G0–G5）\n"
                "- 意图确证（知难行易；全任务适用；2026-10-29 立）<!-- FLOW_INDEX_END -->\n",
                encoding="utf-8")),
            # E7b 负向之二：单元格小节非该分册 H2（错指）
            ("E7b", lambda: (tmp / "00-编纂规则与格式规范/01-规则/流程规则/00-索引.md").write_text(
                "# 流程规则·总索引\n\n| 分册 | 原小节 |\n| ---- | ------ |\n"
                "| [01-测试分册.md](01-测试分册.md) | 别的标题<br>意图确证（知难行易；全任务适用；2026-10-29 立） |\n\n"
                "<!-- FLOW_INDEX_BEGIN -->\n\n"
                "- 工程实践生命周期与阶段门禁（G0–G5）\n"
                "- 意图确证（知难行易；全任务适用；2026-10-29 立）<!-- FLOW_INDEX_END -->\n",
                encoding="utf-8")),
            # E7b 负向之三：分册 H2 未在总索引登记
            ("E7b", lambda: (tmp / "00-编纂规则与格式规范/01-规则/流程规则/00-索引.md").write_text(
                "# 流程规则·总索引\n\n| 分册 | 原小节 |\n| ---- | ------ |\n"
                "| [01-测试分册.md](01-测试分册.md) | 意图确证（知难行易；全任务适用；2026-10-29 立） |\n\n"
                "<!-- FLOW_INDEX_BEGIN -->\n\n"
                "- 工程实践生命周期与阶段门禁（G0–G5）\n"
                "- 意图确证（知难行易；全任务适用；2026-10-29 立）<!-- FLOW_INDEX_END -->\n",
                encoding="utf-8")),
            # E7b 负向之四：FLOW_INDEX 块 bullet 缺项（实测历史漂移形态）
            ("E7b", lambda: (tmp / "00-编纂规则与格式规范/01-规则/流程规则/00-索引.md").write_text(
                "# 流程规则·总索引\n\n| 分册 | 原小节 |\n| ---- | ------ |\n"
                "| [01-测试分册.md](01-测试分册.md) | 工程实践生命周期与阶段门禁（G0–G5）<br>意图确证（知难行易；全任务适用；2026-10-29 立） |\n\n"
                "<!-- FLOW_INDEX_BEGIN -->\n\n"
                "- 工程实践生命周期与阶段门禁（G0–G5）<!-- FLOW_INDEX_END -->\n",
                encoding="utf-8")),
            # E7b 负向之五：FLOW_INDEX 块 bullet 重复
            ("E7b", lambda: (tmp / "00-编纂规则与格式规范/01-规则/流程规则/00-索引.md").write_text(
                "# 流程规则·总索引\n\n| 分册 | 原小节 |\n| ---- | ------ |\n"
                "| [01-测试分册.md](01-测试分册.md) | 工程实践生命周期与阶段门禁（G0–G5）<br>意图确证（知难行易；全任务适用；2026-10-29 立） |\n\n"
                "<!-- FLOW_INDEX_BEGIN -->\n\n"
                "- 工程实践生命周期与阶段门禁（G0–G5）\n"
                "- 工程实践生命周期与阶段门禁（G0–G5）\n"
                "- 意图确证（知难行易；全任务适用；2026-10-29 立）<!-- FLOW_INDEX_END -->\n",
                encoding="utf-8")),
            # E8 负向之一（2026-10-29 立）：缺理论件
            ("E8", lambda: (tmp / "13-软件工程/08-intent-first.md").unlink()),
            # E11 负向（2026-11-06 立）：删一张角色卡
            ("E11", lambda: (tmp / "13-软件工程/templates/agents/block-triage.md").unlink()),
            # E8 负向之二：全局节缺“档 B”
            ("E8", lambda: (tmp / "00-编纂规则与格式规范/01-规则/流程规则/01-测试分册.md")
             .write_text("# 测试分册\n\n## 工程实践生命周期与阶段门禁（G0–G5）\n\n"
                         "## 意图确证（知难行易；全任务适用；2026-10-29 立）\n\n"
                         "全任务适用（不限工程类批次）；档 A：全量六字段。\n\n"
                         "| 阶段 | 名称 | 活动 | 退出判据 |\n"
                         "| ---- | ---- | ---- | ---- |\n"
                         "| G0 | 立项与范围 | 写意图确证 | 意图确证单已写 |\n",
                         encoding="utf-8")),
            # E8 负向之三：G0 行缺“意图”
            ("E8", lambda: (tmp / "00-编纂规则与格式规范/01-规则/流程规则/01-测试分册.md")
             .write_text("# 测试分册\n\n## 工程实践生命周期与阶段门禁（G0–G5）\n\n"
                         "## 意图确证（知难行易；全任务适用；2026-10-29 立）\n\n"
                         "全任务适用（不限工程类批次）；档 A：全量六字段；档 B：轻量三要素。\n\n"
                         "| 阶段 | 名称 | 活动 | 退出判据 |\n"
                         "| ---- | ---- | ---- | ---- |\n"
                         "| G0 | 立项与范围 | 定范围 | 范围有书面结论 |\n",
                         encoding="utf-8")),
            # E8 负向之四：模板 I 缺“意图确证”条目
            ("E8", lambda: (tmp / "00-编纂规则与格式规范/02-操作手册/14-工程实践模板"
                            "/模板I-批次提交核对清单.md").write_text("# 模板I\n", encoding="utf-8")),
            # E8 目标子串覆盖（2026-10-29 补）：08 件只留“非目标”、删去“目标”，须判缺
            ("E8", lambda: (tmp / "13-软件工程/08-intent-first.md").write_text(
                "# 知难行易：意图确证先于手段\n\n"
                "档 A：用户原话、非目标、验收判据、手段自由度、未知\n",
                encoding="utf-8")),
            # E8 README 表格行判定（2026-10-29 补）：仅非表格行提及 08-intent-first.md 须 FAIL
            ("E8", lambda: (tmp / "13-软件工程/README.md").write_text(
                "# 13-软件工程\n\n08-intent-first.md\n", encoding="utf-8")),
            # E13 负向之一（2026-11-14 立）：缺理论件
            ("E13", lambda: (tmp / "13-软件工程/10-standards-first.md").unlink()),
            # E13 负向之二：规则文件缺 §0.8 节（其余接线保持，只 E13 FAIL）
            ("E13", lambda: (tmp / "00-编纂规则与格式规范/01-规则/工程实践规则.md").write_text(
                "# 工程实践规则\n\n- **复审日期**：2027-01-22\n\n"
                "模板G-架构决策记录.md 模板H-技术债登记.md "
                "模板I-批次提交核对清单.md 模板J-工程实践复审.md\n"
                "意图确证 见 08-intent-first.md\n",
                encoding="utf-8")),
            # E13 负向之三：AGENTS 行缺“标准化文献”（意图确证行保持）
            ("E13", lambda: (tmp / "AGENTS.md").write_text(
                "工程实践规则.md\n任何任务开工前先写意图确证（所有任务）\n", encoding="utf-8")),
            # E13 负向之四：模板 I 缺“标准化文献”项（意图确证项保持）
            ("E13", lambda: (tmp / "00-编纂规则与格式规范/02-操作手册/14-工程实践模板"
                            "/模板I-批次提交核对清单.md").write_text(
                "# 模板I\n- [ ] 意图确证单已写\n", encoding="utf-8")),
            # E13 负向之五：README 表格行缺 10-standards-first.md（08 行与 agents/skills 行保持）
            ("E13", lambda: (tmp / "13-软件工程/README.md").write_text(
                "# 13-软件工程\n\n| 文件 | 内文 | 必读 |\n| ---- | ---- | ---- |\n"
                "| `08-intent-first.md` | x | 是 |\n\n"
                "templates/agents 与 templates/skills：角色卡与技能模板见 templates/qoder-plugin/README.md。\n",
                encoding="utf-8")),
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
    print("  ✅ 判据非空自检通过：正样本 0 FAIL；E1–E8/E7b/E11/E13 %d 项负向夹具均命中" % len(cases))
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
        for key in ("rule", "rule_readme", "flow", "flow_dir", "agents", "gov", "adr_dir",
                    "index", "debt", "templates", "cmd_readme", "registry",
                    "doctrine", "doctrine10", "doctrine_readme", "templ_i"):
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
