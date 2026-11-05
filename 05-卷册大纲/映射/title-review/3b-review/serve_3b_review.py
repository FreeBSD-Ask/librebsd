#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""3B 逐卷人工审定：本地 HTTP 审阅服务。

只读源台账（outline.txt、V01–V75.tsv、机判结果.tsv、人判总表.tsv），
把答案、配置、候选与导出写入本工具目录下的 data/，不改动任何源文件。
第 76 卷整卷排除。仅使用 Python 标准库，无第三方依赖。
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
import os
import re
import socket
import sys
import tempfile
import threading
from collections import OrderedDict, defaultdict
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlsplit

TOOL_DIR = Path(__file__).resolve().parent
try:
    DEFAULT_ROOT = TOOL_DIR.parents[3]
except IndexError:  # pragma: no cover - 仅为极端部署兜底
    DEFAULT_ROOT = TOOL_DIR
WEB_DIR = TOOL_DIR / "web"
DATA_DIR = TOOL_DIR / "data"
ANSWERS_DIR = DATA_DIR / "answers"
SNAPSHOTS_DIR = ANSWERS_DIR / "snapshots"
CONFIG_DIR = DATA_DIR / "config"
CANDIDATES_DIR = DATA_DIR / "candidates"
EXPORTS_DIR = DATA_DIR / "exports"

OUTLINE_REL = Path("05-卷册大纲") / "目录" / "data" / "outline.txt"
DESIGN_REL = Path("05-卷册大纲") / "映射" / "title-design"
MACHINE_REL = Path("05-卷册大纲") / "映射" / "title-review" / "full-review" / "机判结果.tsv"
HUMAN_REL = Path("05-卷册大纲") / "映射" / "title-review" / "full-review" / "人判" / "人判总表.tsv"

VOL_MIN = 1
VOL_MAX = 75
EXCLUDED_VOL = 76
VERDICTS = ("ok", "reroll", "custom")
ANSWER_FIELDS = ("verdict", "custom_title", "note", "tags", "merge_target", "updated_at")
REROLL_TAGS = ("content", "length", "merge", "split", "format", "delete", "term")
MERGE_TARGETS = ("prev", "next", "parent")
EXPECTED_TOTALS = {
    "chapters": 539,
    "sections": 3918,
    "subsections": 19265,
    "units": 23722,
}
MAX_BODY = 64 * 1024 * 1024

DEFAULT_CONFIG = {
    "vol_start": 1,
    "vol_end": 75,
    "daily_goal": 500,
    "theme": "amoled",
    "font_size": "m",
    "labels": {"ok": "通过", "reroll": "重拟", "custom": "自定义"},
    "only_flagged": False,
}

VOL_RE = re.compile(r"^#\s*第([一二三四五六七八九十]+)卷\s*(.*)$")
CHAPTER_RE = re.compile(r"^##\s*第\s*(\d+)\s*章\s*(.*)$")
SECTION_RE = re.compile(r"^-\s*(\d+)\.(\d+)\s+(.*)$")
SUBSECTION_RE = re.compile(r"^V\d{2}\.\d+\.\d+\.\d+$")
SECTION_KEY_RE = re.compile(r"^V(\d{1,2})\.(\d+)\.(\d+)$")

_CN_DIGITS = {ch: idx + 1 for idx, ch in enumerate("一二三四五六七八九十")}
_HUMAN_FAIL_WORDS = {"fail", "有问题", "不通过", "未通过"}


class StartupError(Exception):
    """源数据自校验失败。"""


class ApiError(Exception):
    """HTTP API 可预期错误。"""

    def __init__(self, status: int, error: str, detail: str, extra: dict | None = None):
        super().__init__(detail)
        self.status = status
        self.error = error
        self.detail = detail
        self.extra = extra or {}


def iso_now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def tag_now() -> str:
    return datetime.now().astimezone().strftime("%Y%m%d-%H%M%S")


def parse_cn_int(text: str) -> int:
    if text == "十":
        return 10
    if "十" in text:
        tens, ones = text.split("十", 1)
        return (_CN_DIGITS[tens] if tens else 1) * 10 + (_CN_DIGITS[ones] if ones else 0)
    if text in _CN_DIGITS:
        return _CN_DIGITS[text]
    raise ValueError(f"无法识别的中文数字：{text}")


def clean_title(text: str) -> str:
    return text.split("@@", 1)[0].strip()


def atomic_write_text(path: Path, text: str) -> None:
    """UTF-8 无 BOM、LF、同目录临时文件 + 原子替换。"""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(
        prefix=path.name + ".", suffix=".tmp", dir=str(path.parent)
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_name, path)
    except BaseException:
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
        raise


def dump_json_file(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, indent=2) + "\n"


def _is_int(value) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def parse_ts(value: str):
    if not isinstance(value, str) or not value.strip():
        return None
    text = value.strip().replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(text).timestamp()
    except ValueError:
        pass
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M", "%Y-%m-%d"):
        try:
            return datetime.strptime(text, fmt).timestamp()
        except ValueError:
            continue
    return None


def parse_outline(path: Path):
    volumes = OrderedDict()
    errors = []
    current_vol = None
    current_chapter = None
    text = path.read_text(encoding="utf-8-sig")
    for lineno, raw in enumerate(text.splitlines(), 1):
        line = raw.rstrip()
        if not line:
            continue
        match = VOL_RE.match(line)
        if match:
            vol_no = parse_cn_int(match.group(1))
            if vol_no > VOL_MAX:
                current_vol = None
                current_chapter = None
                continue
            if vol_no in volumes:
                errors.append(f"outline 第 {lineno} 行：第 {vol_no} 卷重复")
            volumes[vol_no] = {
                "title": clean_title(match.group(2)),
                "chapters": OrderedDict(),
            }
            current_vol = vol_no
            current_chapter = None
            continue
        match = CHAPTER_RE.match(line)
        if match:
            if current_vol is None:
                continue
            chapter_no = int(match.group(1))
            chapters = volumes[current_vol]["chapters"]
            if chapter_no in chapters:
                errors.append(f"outline 第 {lineno} 行：第 {current_vol} 卷第 {chapter_no} 章重复")
            chapters[chapter_no] = {
                "title": clean_title(match.group(2)),
                "sections": OrderedDict(),
            }
            current_chapter = chapter_no
            continue
        match = SECTION_RE.match(line)
        if match:
            if current_vol is None or current_chapter is None:
                continue
            chapter_no = int(match.group(1))
            section_no = int(match.group(2))
            if chapter_no != current_chapter:
                errors.append(
                    f"outline 第 {lineno} 行：节号 {chapter_no}.{section_no} 与当前第 {current_chapter} 章不符"
                )
            sections = volumes[current_vol]["chapters"][current_chapter]["sections"]
            if section_no in sections:
                errors.append(
                    f"outline 第 {lineno} 行：第 {current_vol} 卷第 {current_chapter} 章节号 {section_no} 重复"
                )
            sections[section_no] = {"title": clean_title(match.group(3))}
            continue
    return volumes, errors


def load_ledger(path: Path, vol_no: int):
    rows = []
    errors = []
    if not path.exists():
        return rows, [f"缺少台账文件：{path.name}"]
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        required = {
            "subsection_id",
            "vol",
            "chapter",
            "section",
            "title",
            "thesis",
            "order",
            "source_count",
        }
        missing = required - set(reader.fieldnames or [])
        if missing:
            return rows, [f"{path.name} 缺少表头列：{', '.join(sorted(missing))}"]
        for lineno, record in enumerate(reader, 2):
            try:
                vol = int((record.get("vol") or "").strip())
                chapter_no = int((record.get("chapter") or "").strip())
                section_no = int((record.get("section") or "").strip())
            except ValueError:
                errors.append(f"{path.name} 第 {lineno} 行：卷/章/节号不是整数")
                continue
            subsection_id = (record.get("subsection_id") or "").strip()
            if not SUBSECTION_RE.match(subsection_id):
                errors.append(f"{path.name} 第 {lineno} 行：subsection_id 形态非法（{subsection_id}）")
                continue
            if vol != vol_no:
                errors.append(f"{path.name} 第 {lineno} 行：vol={vol} 与文件卷号 {vol_no} 不符")
            if not subsection_id.startswith(f"V{vol_no:02d}."):
                errors.append(f"{path.name} 第 {lineno} 行：subsection_id 前缀与卷号不符（{subsection_id}）")
            title = (record.get("title") or "").strip()
            if not title:
                errors.append(f"{path.name} 第 {lineno} 行：题名为空")
                continue
            source_text = (record.get("source_count") or "").strip()
            try:
                source_count = int(source_text) if source_text else 0
            except ValueError:
                errors.append(f"{path.name} 第 {lineno} 行：source_count 不是整数")
                source_count = 0
            order_text = (record.get("order") or "").strip()
            try:
                order = int(order_text) if order_text else 0
            except ValueError:
                order = 0
            rows.append(
                {
                    "subsection_id": subsection_id,
                    "vol": vol,
                    "chapter": chapter_no,
                    "section": section_no,
                    "title": title,
                    "thesis": (record.get("thesis") or "").strip(),
                    "order": order,
                    "source_count": source_count,
                }
            )
    return rows, errors


def section_key(vol: int, chapter_no: int, section_no: int) -> str:
    return f"V{vol:02d}.{chapter_no:02d}.{section_no:02d}"


def chapter_key(vol: int, chapter_no: int) -> str:
    return f"V{vol:02d}.C{chapter_no:02d}"


def normalize_section_key(raw: str) -> str | None:
    match = SECTION_KEY_RE.match(raw.strip())
    if not match:
        return None
    return section_key(int(match.group(1)), int(match.group(2)), int(match.group(3)))


def source_hash(root: Path, outline_path: Path, design_dir: Path) -> str:
    files = [outline_path] + [design_dir / f"V{vol:02d}.tsv" for vol in range(VOL_MIN, VOL_MAX + 1)]
    entries = []
    for path in files:
        rel = path.relative_to(root).as_posix()
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        entries.append((rel, digest))
    entries.sort(key=lambda item: item[0])
    payload = "".join(f"{rel}\t{digest}\n" for rel, digest in entries)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def validate_config_patch(incoming, base):
    errors = {}
    if not isinstance(incoming, dict):
        return None, {"config": "必须是 JSON 对象"}
    unknown = sorted(set(incoming) - set(DEFAULT_CONFIG))
    if unknown:
        errors["unknown"] = f"未知字段：{', '.join(unknown)}"
    config = copy.deepcopy(base)
    for key, value in incoming.items():
        if key not in DEFAULT_CONFIG:
            continue
        if key == "labels":
            if not isinstance(value, dict):
                errors["labels"] = "labels 必须是对象"
                continue
            extra = sorted(set(value) - set(DEFAULT_CONFIG["labels"]))
            if extra:
                errors["labels"] = f"labels 含未知键：{', '.join(extra)}"
                continue
            labels = dict(config["labels"])
            for label_key, label_value in value.items():
                labels[label_key] = label_value
            config["labels"] = labels
        else:
            config[key] = value

    if not _is_int(config.get("vol_start")) or not (VOL_MIN <= config["vol_start"] <= VOL_MAX):
        errors["vol_start"] = f"vol_start 须为 {VOL_MIN}–{VOL_MAX} 的整数"
    if not _is_int(config.get("vol_end")) or not (VOL_MIN <= config["vol_end"] <= VOL_MAX):
        errors["vol_end"] = f"vol_end 须为 {VOL_MIN}–{VOL_MAX} 的整数"
    if "vol_start" not in errors and "vol_end" not in errors and config["vol_start"] > config["vol_end"]:
        errors["vol_range"] = "vol_start 不得大于 vol_end"
    if not _is_int(config.get("daily_goal")) or not (1 <= config["daily_goal"] <= 5000):
        errors["daily_goal"] = "daily_goal 须为 1–5000 的整数"
    if config.get("theme") not in ("amoled", "day"):
        errors["theme"] = "theme 须为 amoled 或 day"
    if config.get("font_size") not in ("s", "m", "l"):
        errors["font_size"] = "font_size 须为 s、m 或 l"
    if not isinstance(config.get("only_flagged"), bool):
        errors["only_flagged"] = "only_flagged 须为布尔值"
    labels = config.get("labels")
    if not isinstance(labels, dict):
        errors["labels"] = "labels 必须是对象"
    else:
        for label_key in ("ok", "reroll", "custom"):
            label_value = labels.get(label_key)
            if not isinstance(label_value, str) or not (1 <= len(label_value.strip()) <= 8):
                errors["labels"] = f"labels.{label_key} 须为 1–8 字字符串"
                break
    if errors:
        return None, errors
    return config, {}


class App:
    def __init__(self, root: Path):
        self.root = root
        self.outline_path = root / OUTLINE_REL
        self.design_dir = root / DESIGN_REL
        self.machine_path = root / MACHINE_REL
        self.human_path = root / HUMAN_REL

        self.lock = threading.RLock()
        self.totals = {"units": 0, "chapters": 0, "sections": 0, "subsections": 0, "vols": 0}
        self.vol_meta = OrderedDict()
        self.units_by_vol = OrderedDict()
        self.all_units = []
        self.key_index = {}
        self.key_order = {}
        self.machine_fail = set()
        self.human_fail = set()
        self.source_hash = ""
        self.answers = {}
        self.config = copy.deepcopy(DEFAULT_CONFIG)
        self.scope_list = None
        self.scope_set = None

    # ---------- 装载与自校验 ----------

    def load(self) -> None:
        for path in (self.outline_path, self.machine_path, self.human_path):
            if not path.exists():
                raise StartupError(f"缺少数据源：{path}")
        outline, outline_errors = parse_outline(self.outline_path)
        ledgers = {}
        issues = list(outline_errors)
        for vol in range(VOL_MIN, VOL_MAX + 1):
            rows, errors = load_ledger(self.design_dir / f"V{vol:02d}.tsv", vol)
            ledgers[vol] = rows
            issues.extend(errors)
        self._validate(outline, ledgers, issues)
        self._build_units(outline, ledgers)
        self._load_flags()
        self.source_hash = source_hash(self.root, self.outline_path, self.design_dir)
        ensure_data_dirs()
        self._cleanup_temp_residue()
        self._load_answers()
        self._load_config()
        self._load_scope()

    def _validate(self, outline, ledgers, issues) -> None:
        diff_vols = OrderedDict()

        def add(vol, text):
            diff_vols.setdefault(vol, []).append(text)

        for vol in range(VOL_MIN, VOL_MAX + 1):
            if vol not in outline:
                add(vol, "outline 缺卷")
            if vol not in ledgers:
                add(vol, "台账缺文件")
        if issues:
            for text in issues[:200]:
                add(0, text)

        chapters_total = 0
        sections_total = 0
        subsections_total = 0
        seen_ids = set()
        for vol in range(VOL_MIN, VOL_MAX + 1):
            rows = ledgers.get(vol, [])
            vol_info = outline.get(vol)
            outline_chapters = list(vol_info["chapters"].keys()) if vol_info else []
            outline_sections = set()
            if vol_info:
                for chapter_no, chapter in vol_info["chapters"].items():
                    for section_no in chapter["sections"]:
                        outline_sections.add((chapter_no, section_no))
            ledger_chapters = {row["chapter"] for row in rows}
            ledger_sections = {(row["chapter"], row["section"]) for row in rows}

            if vol_info:
                chapters_total += len(outline_chapters)
                sections_total += len(outline_sections)
            subsections_total += len(rows)

            missing_chapters = sorted(set(outline_chapters) - ledger_chapters)
            extra_chapters = sorted(ledger_chapters - set(outline_chapters))
            if missing_chapters:
                add(vol, f"台账缺章：{missing_chapters[:10]}")
            if extra_chapters:
                add(vol, f"台账多章：{extra_chapters[:10]}")
            missing_sections = sorted(outline_sections - ledger_sections)
            extra_sections = sorted(ledger_sections - outline_sections)
            if missing_sections:
                add(vol, f"台账缺节：{missing_sections[:10]}")
            if extra_sections:
                add(vol, f"台账多节：{extra_sections[:10]}")
            if not rows:
                add(vol, "台账无小节数据")
            for row in rows:
                sid = row["subsection_id"]
                if sid in seen_ids:
                    add(vol, f"小节编号重复：{sid}")
                seen_ids.add(sid)
                if row["chapter"] not in outline_chapters:
                    add(vol, f"小节 {sid} 所属章不在 outline")
                if (row["chapter"], row["section"]) not in outline_sections:
                    add(vol, f"小节 {sid} 所属节不在 outline")

        actual = {
            "chapters": chapters_total,
            "sections": sections_total,
            "subsections": subsections_total,
            "units": chapters_total + sections_total + subsections_total,
        }
        for key, expected in EXPECTED_TOTALS.items():
            if actual[key] != expected:
                add(0, f"合计 {key} 为 {actual[key]}，期望 {expected}")

        if diff_vols:
            lines = ["自校验失败：1–75 卷的 outline 与 title-design 台账不一致。"]
            for vol in sorted(diff_vols):
                label = "全局" if vol == 0 else f"第 {vol} 卷"
                lines.append(f"  {label}：")
                for text in diff_vols[vol][:12]:
                    lines.append(f"    - {text}")
            lines.append(
                "实测合计：章 {chapters}、节 {sections}、小节 {subsections}、合计 {units}".format(**actual)
            )
            raise StartupError("\n".join(lines))

        self.totals = {
            "units": actual["units"],
            "chapters": actual["chapters"],
            "sections": actual["sections"],
            "subsections": actual["subsections"],
            "vols": VOL_MAX,
        }

    def _build_units(self, outline, ledgers) -> None:
        for vol in range(VOL_MIN, VOL_MAX + 1):
            vol_info = outline[vol]
            rows_by_section = defaultdict(list)
            for row in ledgers[vol]:
                rows_by_section[(row["chapter"], row["section"])].append(row)
            units = []
            order = 0
            for chapter_no, chapter in vol_info["chapters"].items():
                order += 1
                units.append(
                    {
                        "key": chapter_key(vol, chapter_no),
                        "level": "chapter",
                        "vol": vol,
                        "chapter_no": chapter_no,
                        "section_no": None,
                        "title": chapter["title"],
                        "thesis": None,
                        "source_count": None,
                        "order": order,
                    }
                )
                for section_no, section in chapter["sections"].items():
                    order += 1
                    units.append(
                        {
                            "key": section_key(vol, chapter_no, section_no),
                            "level": "section",
                            "vol": vol,
                            "chapter_no": chapter_no,
                            "section_no": section_no,
                            "title": section["title"],
                            "thesis": None,
                            "source_count": None,
                            "order": order,
                        }
                    )
                    subset = sorted(
                        rows_by_section.get((chapter_no, section_no), []),
                        key=lambda item: (item["order"], item["subsection_id"]),
                    )
                    for row in subset:
                        order += 1
                        units.append(
                            {
                                "key": row["subsection_id"],
                                "level": "subsection",
                                "vol": vol,
                                "chapter_no": chapter_no,
                                "section_no": section_no,
                                "title": row["title"],
                                "thesis": row["thesis"],
                                "source_count": row["source_count"],
                                "order": order,
                            }
                        )
            self.units_by_vol[vol] = units
            self.vol_meta[vol] = {
                "vol": vol,
                "title": vol_info["title"],
                "chapters": len(vol_info["chapters"]),
                "sections": sum(len(ch["sections"]) for ch in vol_info["chapters"].values()),
                "subsections": len(ledgers[vol]),
                "units": len(units),
            }
            for unit in units:
                if unit["key"] in self.key_index:
                    raise StartupError(f"单元键重复：{unit['key']}")
                self.key_index[unit["key"]] = unit
                self.all_units.append(unit)
        for index, unit in enumerate(self.all_units):
            self.key_order[unit["key"]] = index

    def _load_flags(self) -> None:
        machine_unknown = 0
        if self.machine_path.exists():
            with self.machine_path.open("r", encoding="utf-8-sig", newline="") as handle:
                for record in csv.DictReader(handle, delimiter="\t"):
                    try:
                        vol = int((record.get("vol") or "").strip())
                    except ValueError:
                        continue
                    if vol < VOL_MIN or vol > VOL_MAX:
                        continue
                    if (record.get("result") or "").strip().upper() != "FAIL":
                        continue
                    sid = (record.get("subsection_id") or "").strip()
                    if sid in self.key_index:
                        self.machine_fail.add(sid)
                    else:
                        machine_unknown += 1
        if machine_unknown:
            print(f"提示：机判结果中有 {machine_unknown} 条 FAIL 记录映射不到 1–75 卷小节，已忽略。")

        if self.human_path.exists():
            with self.human_path.open("r", encoding="utf-8-sig", newline="") as handle:
                for record in csv.DictReader(handle, delimiter="\t"):
                    verdict = (record.get("verdict") or "").strip()
                    if verdict.lower() not in _HUMAN_FAIL_WORDS and verdict not in _HUMAN_FAIL_WORDS:
                        continue
                    kind = (record.get("item_kind") or "").strip()
                    raw_key = (record.get("item_key") or "").strip()
                    mapped = None
                    if kind in ("title", "evidence_row"):
                        mapped = raw_key
                    elif kind == "section":
                        mapped = normalize_section_key(raw_key)
                    if mapped and mapped in self.key_index:
                        self.human_fail.add(mapped)

        for unit in self.all_units:
            if unit["key"] in self.machine_fail:
                unit["flag_machine"] = True
            if unit["key"] in self.human_fail:
                unit["flag_human"] = True

    # ---------- 状态装载 ----------

    def _load_answers(self) -> None:
        path = ANSWERS_DIR / "answers.json"
        if not path.exists():
            return
        try:
            raw = json.loads(path.read_text(encoding="utf-8-sig"))
        except (OSError, ValueError) as exc:
            recovered = self._recover_answers_from_snapshot()
            if recovered:
                print(f"警告：answers.json 读取失败（{exc}），已从最新可用快照恢复 {len(self.answers)} 条答案。")
            else:
                print(f"警告：answers.json 读取失败（{exc}），且无可用快照，以空答案启动。")
            return
        entries = raw.get("answers") if isinstance(raw, dict) and "answers" in raw else raw
        if not isinstance(entries, dict):
            return
        dropped = 0
        for key, value in entries.items():
            if key not in self.key_index or not isinstance(value, dict):
                dropped += 1
                continue
            if value.get("verdict") not in VERDICTS:
                dropped += 1
                continue
            self.answers[key] = {
                "verdict": value["verdict"],
                "custom_title": str(value.get("custom_title") or ""),
                "note": str(value.get("note") or ""),
                "tags": [t for t in (value.get("tags") or []) if t in REROLL_TAGS],
                "merge_target": str(value.get("merge_target") or ""),
                "updated_at": str(value.get("updated_at") or ""),
            }
        if dropped:
            print(f"提示：answers.json 有 {dropped} 条无效或越界记录，已忽略。")

    def _recover_answers_from_snapshot(self) -> bool:
        """answers.json 损坏时按时间倒序尝试快照，恢复成功后回写主文件。"""
        if not SNAPSHOTS_DIR.exists():
            return False
        files = sorted(
            SNAPSHOTS_DIR.glob("answers-*.json"),
            key=lambda item: (item.stat().st_mtime_ns, item.name),
            reverse=True,
        )
        for path in files[:10]:
            try:
                raw = json.loads(path.read_text(encoding="utf-8-sig"))
            except (OSError, ValueError):
                continue
            entries = raw.get("answers") if isinstance(raw, dict) and "answers" in raw else raw
            if not isinstance(entries, dict):
                continue
            recovered = {}
            for key, value in entries.items():
                if key not in self.key_index or not isinstance(value, dict):
                    continue
                if value.get("verdict") not in VERDICTS:
                    continue
                recovered[key] = {
                    "verdict": value["verdict"],
                    "custom_title": str(value.get("custom_title") or ""),
                    "note": str(value.get("note") or ""),
                    "updated_at": str(value.get("updated_at") or ""),
                }
            if recovered:
                self.answers = recovered
                self._save_answers_locked()
                return True
        return False

    def _load_config(self) -> None:
        path = CONFIG_DIR / "config.json"
        if not path.exists():
            return
        try:
            raw = json.loads(path.read_text(encoding="utf-8-sig"))
        except (OSError, ValueError) as exc:
            print(f"提示：config.json 读取失败（{exc}），使用默认配置。")
            return
        config, errors = validate_config_patch(raw, DEFAULT_CONFIG)
        if config is None:
            print(f"提示：config.json 校验失败（{errors}），使用默认配置。")
            return
        self.config = config

    def _load_scope(self) -> None:
        path = CONFIG_DIR / "scope.json"
        if not path.exists():
            return
        try:
            raw = json.loads(path.read_text(encoding="utf-8-sig"))
        except (OSError, ValueError) as exc:
            print(f"提示：scope.json 读取失败（{exc}），按全量处理。")
            return
        keys = raw.get("unit_keys") if isinstance(raw, dict) else raw
        if not isinstance(keys, list):
            return
        cleaned = []
        seen = set()
        for key in keys:
            if isinstance(key, str) and key in self.key_index and key not in seen:
                cleaned.append(key)
                seen.add(key)
        if cleaned:
            self.scope_list = cleaned
            self.scope_set = set(cleaned)

    # ---------- 单元与作用域 ----------

    def effective_units(self):
        start = self.config["vol_start"]
        end = self.config["vol_end"]
        scope = self.scope_set
        flagged = self.config["only_flagged"]
        out = []
        for unit in self.all_units:
            if not (start <= unit["vol"] <= end):
                continue
            if scope is not None and unit["key"] not in scope:
                continue
            if flagged and not (unit.get("flag_machine") or unit.get("flag_human")):
                continue
            out.append(unit)
        return out

    def effective_count(self) -> int:
        return len(self.effective_units())

    def _public_unit(self, unit):
        data = dict(unit)
        return data

    def units_response(self, vol: int, chapter=None):
        units = [
            unit
            for unit in self.effective_units()
            if unit["vol"] == vol and (chapter is None or unit["chapter_no"] == chapter)
        ]
        return {"vol": vol, "units": [self._public_unit(unit) for unit in units]}

    def manifest(self):
        scope_active = self.scope_set is not None
        configured = len(self.scope_list) if scope_active else None
        effective = len(self.effective_units())
        vols = [self.vol_meta[vol] for vol in range(VOL_MIN, VOL_MAX + 1)]
        return {
            "source_hash": self.source_hash,
            "totals": dict(self.totals),
            "scope": {"active": scope_active, "configured": configured, "effective": effective},
            "config": copy.deepcopy(self.config),
            "vols": vols,
            "generated_at": iso_now(),
        }

    # ---------- 答案 ----------

    def _validate_answer_value(self, value, now_iso: str):
        if not isinstance(value, dict):
            raise ValueError("答案必须是对象")
        unknown = sorted(set(value) - set(ANSWER_FIELDS))
        if unknown:
            raise ValueError(f"未知字段：{', '.join(unknown)}")
        verdict = value.get("verdict")
        if verdict not in VERDICTS:
            raise ValueError("verdict 须为 ok、reroll 或 custom")
        result = {"verdict": verdict}
        for field in ("custom_title", "note"):
            raw = value.get(field, "")
            if raw is None:
                raw = ""
            if not isinstance(raw, str):
                raise ValueError(f"{field} 须为字符串")
            result[field] = raw
        if len(result["custom_title"]) > 120:
            raise ValueError("custom_title 不得超过 120 字")
        if verdict == "custom" and not result["custom_title"].strip():
            raise ValueError("custom 判定须提供 1–120 字的自定义题名")
        if len(result["note"]) > 500:
            raise ValueError("note 不得超过 500 字")
        tags = value.get("tags", [])
        if tags is None:
            tags = []
        if not isinstance(tags, list):
            raise ValueError("tags 须为数组")
        clean_tags = []
        for tag in tags:
            if not isinstance(tag, str) or tag not in REROLL_TAGS:
                raise ValueError(f"未知重拟标签：{tag}")
            if tag not in clean_tags:
                clean_tags.append(tag)
        if clean_tags and verdict != "reroll":
            raise ValueError("重拟标签仅用于 reroll 判定")
        merge_target = value.get("merge_target", "")
        if merge_target is None:
            merge_target = ""
        if not isinstance(merge_target, str):
            raise ValueError("merge_target 须为字符串")
        if merge_target:
            if "merge" not in clean_tags:
                raise ValueError("merge_target 仅在含 merge 标签时可用")
            if merge_target not in MERGE_TARGETS and merge_target not in self.key_index:
                raise ValueError(f"merge_target 非法：{merge_target}")
        result["tags"] = clean_tags
        result["merge_target"] = merge_target
        updated_at = value.get("updated_at") or now_iso
        if not isinstance(updated_at, str):
            raise ValueError("updated_at 须为字符串")
        result["updated_at"] = updated_at
        return result

    def merge_answers(self, incoming):
        if not isinstance(incoming, dict):
            raise ApiError(400, "invalid_answers", "answers 必须是对象")
        now_iso = iso_now()
        normalized = {}
        invalid = []
        ignored = 0
        invalid_detail = ""
        for key, value in incoming.items():
            if not isinstance(key, str) or key not in self.key_index:
                # 越界或陈旧键（含第 76 卷）不入库，但计数回报，便于前端提示“已忽略 N 条”。
                ignored += 1
                continue
            try:
                normalized[key] = self._validate_answer_value(value, now_iso)
            except ValueError as exc:
                invalid.append(key)
                if not invalid_detail:
                    invalid_detail = f"{key}: {exc}"
        if invalid:
            detail = "无效答案键或取值"
            if invalid_detail:
                detail = f"{detail}：{invalid_detail}"
            raise ApiError(400, "invalid_answers", detail, {"invalid": invalid})
        applied = 0
        with self.lock:
            for key, value in normalized.items():
                old = self.answers.get(key)
                if old is None:
                    self.answers[key] = value
                    applied += 1
                    continue
                new_ts = parse_ts(value["updated_at"])
                old_ts = parse_ts(old.get("updated_at", ""))
                if old_ts is None:
                    self.answers[key] = value
                    applied += 1
                elif new_ts is not None and new_ts > old_ts:
                    self.answers[key] = value
                    applied += 1
            if applied:
                self._save_answers_locked()
            count = len(self.answers)
        return applied, len(normalized), count, ignored

    def delete_answer(self, key: str):
        with self.lock:
            existed = self.answers.pop(key, None) is not None
            if existed:
                self._save_answers_locked()
            return existed, len(self.answers)

    def answers_payload(self):
        with self.lock:
            ordered = OrderedDict()
            for unit in self.all_units:
                key = unit["key"]
                if key in self.answers:
                    ordered[key] = copy.deepcopy(self.answers[key])
            return {"answers": ordered, "count": len(ordered), "source_hash": self.source_hash}

    def _save_answers_locked(self) -> None:
        ordered = OrderedDict()
        for unit in self.all_units:
            key = unit["key"]
            if key in self.answers:
                ordered[key] = self.answers[key]
        payload = {"answers": ordered}
        atomic_write_text(ANSWERS_DIR / "answers.json", dump_json_file(payload))
        self._write_snapshot(payload)
        self._prune_snapshots()
        self._cleanup_temp_residue()

    def _write_snapshot(self, payload) -> None:
        SNAPSHOTS_DIR.mkdir(parents=True, exist_ok=True)
        base = f"answers-{tag_now()}"
        path = SNAPSHOTS_DIR / f"{base}.json"
        index = 1
        while path.exists():
            path = SNAPSHOTS_DIR / f"{base}-{index}.json"
            index += 1
        atomic_write_text(path, dump_json_file(payload))

    def _prune_snapshots(self) -> None:
        if not SNAPSHOTS_DIR.exists():
            return
        files = sorted(
            SNAPSHOTS_DIR.glob("answers-*.json"),
            key=lambda item: (item.stat().st_mtime_ns, item.name),
            reverse=True,
        )
        for stale in files[10:]:
            try:
                stale.unlink()
            except OSError:
                pass

    def _cleanup_temp_residue(self) -> None:
        for directory in (ANSWERS_DIR, SNAPSHOTS_DIR, CONFIG_DIR, CANDIDATES_DIR, EXPORTS_DIR):
            if not directory.exists():
                continue
            for pattern in ("*.tmp", "*.tmp-*", ".*.tmp"):
                for stale in directory.glob(pattern):
                    try:
                        stale.unlink()
                    except OSError:
                        pass

    # ---------- 配置与作用域 ----------

    def config_payload(self):
        with self.lock:
            return {
                "config": copy.deepcopy(self.config),
                "scope": {"unit_keys": list(self.scope_list) if self.scope_list is not None else None},
            }

    def update_config(self, incoming):
        if not isinstance(incoming, dict):
            raise ApiError(400, "invalid_config", "config 必须是对象")
        with self.lock:
            config, errors = validate_config_patch(incoming, self.config)
            if config is None:
                raise ApiError(400, "invalid_config", "配置校验失败", {"errors": errors})
            self.config = config
            atomic_write_text(CONFIG_DIR / "config.json", dump_json_file(config))
            return copy.deepcopy(config)

    def update_scope(self, keys):
        if not isinstance(keys, list):
            raise ApiError(400, "invalid_scope", "unit_keys 必须是数组")
        cleaned = []
        seen = set()
        invalid = []
        for key in keys:
            if not isinstance(key, str):
                invalid.append(str(key))
                continue
            if key.startswith(f"V{EXCLUDED_VOL:02d}.") or key not in self.key_index:
                invalid.append(key)
                continue
            if key not in seen:
                cleaned.append(key)
                seen.add(key)
        if invalid:
            raise ApiError(400, "invalid_scope", "存在无效或越界（含第 76 卷）的单元键", {"invalid": invalid})
        with self.lock:
            if cleaned:
                self.scope_list = cleaned
                self.scope_set = set(cleaned)
            else:
                self.scope_list = None
                self.scope_set = None
            atomic_write_text(
                CONFIG_DIR / "scope.json",
                dump_json_file({"unit_keys": self.scope_list}),
            )
            return len(cleaned)

    # ---------- 候选 ----------

    def save_candidates(self, payload):
        if not isinstance(payload, dict):
            raise ApiError(400, "invalid_candidates", "请求体必须是对象")
        batch_id = payload.get("batch_id")
        candidates = payload.get("candidates")
        if not isinstance(batch_id, str) or not re.fullmatch(r"[A-Za-z0-9._-]{1,80}", batch_id):
            raise ApiError(400, "invalid_batch_id", "batch_id 须为 1–80 位字母、数字、点、下划线或连字符")
        if not isinstance(candidates, dict) or not candidates:
            raise ApiError(400, "invalid_candidates", "candidates 必须是非空对象")
        invalid = []
        cleaned = {}
        for key, items in candidates.items():
            if not isinstance(key, str) or key not in self.key_index:
                invalid.append(str(key))
                continue
            with self.lock:
                answer = self.answers.get(key)
            if not answer or answer.get("verdict") != "reroll":
                invalid.append(key)
                continue
            if not isinstance(items, list) or not items:
                invalid.append(key)
                continue
            item_list = []
            for item in items:
                if not isinstance(item, dict):
                    invalid.append(key)
                    break
                candidate_id = item.get("candidate_id")
                new_title = item.get("new_title")
                if not isinstance(candidate_id, str) or not candidate_id.strip():
                    invalid.append(key)
                    break
                if not isinstance(new_title, str) or not new_title.strip():
                    invalid.append(key)
                    break
                item_list.append(
                    {
                        "candidate_id": candidate_id.strip(),
                        "new_title": new_title.strip(),
                        "rationale": str(item.get("rationale") or ""),
                        "source": str(item.get("source") or ""),
                    }
                )
            if len(item_list) == len(items):
                cleaned[key] = item_list
        if invalid:
            raise ApiError(
                400,
                "invalid_candidates",
                "候选键不存在、当前答案不是 reroll，或候选结构非法",
                {"invalid": invalid},
            )
        record = {
            "batch_id": batch_id,
            "created_at": iso_now(),
            "source_hash": self.source_hash,
            "candidates": cleaned,
        }
        with self.lock:
            atomic_write_text(CANDIDATES_DIR / f"{batch_id}.json", dump_json_file(record))
        return len(cleaned)

    def all_candidates(self):
        merged = {}
        if not CANDIDATES_DIR.exists():
            return merged
        files = sorted(CANDIDATES_DIR.glob("*.json"), key=lambda item: (item.stat().st_mtime, item.name))
        for path in files:
            try:
                raw = json.loads(path.read_text(encoding="utf-8-sig"))
            except (OSError, ValueError):
                continue
            candidates = raw.get("candidates") if isinstance(raw, dict) else None
            if not isinstance(candidates, dict):
                continue
            for key, items in candidates.items():
                if isinstance(items, list):
                    merged[key] = items
        return merged

    # ---------- 导出 ----------

    def _answered_rows(self):
        rows = []
        for unit in self.all_units:
            answer = self.answers.get(unit["key"])
            if answer:
                rows.append((unit, answer))
        return rows

    def _export_json_obj(self):
        rows = self._answered_rows()
        counts = {"ok": 0, "reroll": 0, "custom": 0}
        answers = OrderedDict()
        for unit, answer in rows:
            counts[answer["verdict"]] = counts.get(answer["verdict"], 0) + 1
            answers[unit["key"]] = answer
        return {
            "meta": {
                "generated_at": iso_now(),
                "total_units": self.totals["units"],
                "answered": len(rows),
                "scope_effective": self.effective_count(),
                "source_hash": self.source_hash,
                "counts": counts,
            },
            "answers": answers,
        }

    @staticmethod
    def _tsv_cell(value) -> str:
        return str(value).replace("\t", " ").replace("\r", " ").replace("\n", " ")

    def _export_tsv(self) -> str:
        header = [
            "unit_key",
            "level",
            "vol",
            "chapter_no",
            "section_no",
            "title",
            "verdict",
            "custom_title",
            "note",
            "updated_at",
        ]
        lines = ["\t".join(header)]
        for unit, answer in self._answered_rows():
            row = [
                unit["key"],
                unit["level"],
                unit["vol"],
                unit["chapter_no"],
                unit["section_no"],
                unit["title"],
                answer["verdict"],
                answer["custom_title"],
                answer["note"],
                answer["updated_at"],
            ]
            lines.append("\t".join(self._tsv_cell(item) for item in row))
        return "\n".join(lines) + "\n"

    def _export_rewrite(self) -> str:
        header = [
            "unit_key",
            "level",
            "vol",
            "chapter_no",
            "section_no",
            "old_title",
            "action",
            "new_title",
            "tags",
            "merge_target",
            "note",
            "updated_at",
            "source_hash",
        ]
        lines = ["\t".join(header)]
        for unit, answer in self._answered_rows():
            if answer["verdict"] not in ("custom", "reroll"):
                continue
            action = "改题" if answer["verdict"] == "custom" else "重拟待办"
            new_title = answer["custom_title"] if answer["verdict"] == "custom" else ""
            row = [
                unit["key"],
                unit["level"],
                unit["vol"],
                unit["chapter_no"],
                unit["section_no"],
                unit["title"],
                action,
                new_title,
                "+".join(answer.get("tags") or []),
                answer.get("merge_target") or "",
                answer["note"],
                answer["updated_at"],
                self.source_hash,
            ]
            lines.append("\t".join(self._tsv_cell(item) for item in row))
        return "\n".join(lines) + "\n"

    def _unique_export_path(self, stem: str, suffix: str) -> Path:
        EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
        path = EXPORTS_DIR / f"{stem}{suffix}"
        index = 1
        while path.exists():
            path = EXPORTS_DIR / f"{stem}-{index}{suffix}"
            index += 1
        return path

    def export_file(self, fmt: str):
        stamp = tag_now()
        if fmt == "json":
            text = dump_json_file(self._export_json_obj())
            name = f"3B-answers-{stamp}.json"
            content_type = "application/json; charset=utf-8"
        elif fmt == "tsv":
            text = self._export_tsv()
            name = f"3B-answers-{stamp}.tsv"
            content_type = "text/tab-separated-values; charset=utf-8"
        elif fmt == "rewrite":
            text = self._export_rewrite()
            name = f"3B-rewrite-{stamp}.tsv"
            content_type = "text/tab-separated-values; charset=utf-8"
        else:
            raise ApiError(400, "invalid_format", "fmt 须为 json、tsv 或 rewrite")
        with self.lock:
            path = self._unique_export_path(Path(name).stem, Path(name).suffix)
            atomic_write_text(path, text)
        return path.name, content_type, text

    def export_config_file(self):
        with self.lock:
            payload = {
                "config": copy.deepcopy(self.config),
                "scope": {"unit_keys": list(self.scope_list) if self.scope_list is not None else None},
                "source_hash": self.source_hash,
                "exported_at": iso_now(),
            }
        text = dump_json_file(payload)
        name = f"3B-config-{tag_now()}.json"
        return name, "application/json; charset=utf-8", text

    def archive(self):
        stamp = tag_now()
        with self.lock:
            EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
            target = EXPORTS_DIR / stamp
            index = 1
            while target.exists():
                target = EXPORTS_DIR / f"{stamp}-{index}"
                index += 1
            target.mkdir(parents=True)
            json_text = dump_json_file(self._export_json_obj())
            tsv_text = self._export_tsv()
            rewrite_text = self._export_rewrite()
            atomic_write_text(target / "answers.json", json_text)
            atomic_write_text(target / "answers.tsv", tsv_text)
            atomic_write_text(target / "rewrite.tsv", rewrite_text)
            count = len(self._answered_rows())
            log_line = {
                "ts": iso_now(),
                "count": count,
                "files": ["answers.json", "answers.tsv", "rewrite.tsv"],
                "source_hash": self.source_hash,
            }
            with (EXPORTS_DIR / "archive_log.jsonl").open("a", encoding="utf-8", newline="\n") as handle:
                handle.write(json.dumps(log_line, ensure_ascii=False) + "\n")
                handle.flush()
                os.fsync(handle.fileno())
        return {
            "ok": True,
            "dir": f"data/exports/{target.name}",
            "files": ["answers.json", "answers.tsv", "rewrite.tsv"],
            "count": count,
        }


def ensure_data_dirs() -> None:
    for directory in (ANSWERS_DIR, SNAPSHOTS_DIR, CONFIG_DIR, CANDIDATES_DIR, EXPORTS_DIR):
        directory.mkdir(parents=True, exist_ok=True)


MIME_TYPES = {
    ".html": "text/html; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".js": "text/javascript; charset=utf-8",
    ".webmanifest": "application/manifest+json; charset=utf-8",
    ".woff2": "font/woff2",
    ".png": "image/png",
    ".svg": "image/svg+xml",
    ".ico": "image/x-icon",
    ".json": "application/json; charset=utf-8",
    ".txt": "text/plain; charset=utf-8",
}


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    server_version = "ThreeBReview/1.0"

    @property
    def app(self) -> App:
        return self.server.app  # type: ignore[attr-defined]

    # ---------- 基础响应 ----------

    def _send(self, status: int, body: bytes, content_type: str, headers=None) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "same-origin")
        for key, value in (headers or {}).items():
            self.send_header(key, value)
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    def _send_json(self, obj, status: int = 200) -> None:
        body = json.dumps(obj, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        self._send(status, body, "application/json; charset=utf-8", {"Cache-Control": "no-store"})

    def _send_error_json(self, status: int, code: str, detail: str, extra=None) -> None:
        payload = {"error": code, "detail": detail}
        if extra:
            payload.update(extra)
        self._send_json(payload, status)

    # ---------- 请求分发 ----------

    def do_GET(self):
        self._handle()

    def do_HEAD(self):
        self._handle()

    def do_POST(self):
        self._handle()

    def do_PUT(self):
        self._handle()

    def do_DELETE(self):
        self._handle()

    def _handle(self):
        try:
            self._read_body()
            self._dispatch()
        except ApiError as exc:
            self._send_error_json(exc.status, exc.error, exc.detail, exc.extra)
        except (BrokenPipeError, ConnectionResetError):
            pass
        except Exception as exc:  # noqa: BLE001 - 本地服务需给出可诊断信息
            self._send_error_json(500, "internal_error", f"{type(exc).__name__}: {exc}")

    def _read_body(self) -> None:
        self._body_raw = b""
        if self.command not in ("POST", "PUT", "PATCH"):
            return
        raw_length = self.headers.get("Content-Length")
        if raw_length is None:
            return
        try:
            length = int(raw_length)
        except ValueError:
            raise ApiError(400, "invalid_request", "Content-Length 非法")
        if length < 0:
            raise ApiError(400, "invalid_request", "Content-Length 非法")
        if length > MAX_BODY:
            raise ApiError(413, "payload_too_large", f"请求体超过 {MAX_BODY} 字节")
        self._body_raw = self.rfile.read(length) if length else b""

    def _json_body(self):
        if not self._body_raw:
            raise ApiError(400, "invalid_json", "请求体为空，需为 JSON 对象")
        try:
            payload = json.loads(self._body_raw.decode("utf-8"))
        except (UnicodeDecodeError, ValueError) as exc:
            raise ApiError(400, "invalid_json", f"JSON 解析失败：{exc}")
        if not isinstance(payload, dict):
            raise ApiError(400, "invalid_json", "请求体须为 JSON 对象")
        return payload

    def _dispatch(self):
        parsed = urlsplit(self.path)
        path = unquote(parsed.path)
        if path.startswith("/api/"):
            return self._dispatch_api(path, parsed)
        if self.command not in ("GET", "HEAD"):
            raise ApiError(405, "method_not_allowed", "静态资源仅支持 GET")
        if path in ("/", ""):
            return self._serve_static("index.html")
        return self._serve_static(path.lstrip("/"))

    def _dispatch_api(self, path: str, parsed):
        query = parse_qs(parsed.query, keep_blank_values=True)

        def param(name):
            values = query.get(name)
            return values[0] if values else None

        method = self.command
        app = self.app

        if path == "/api/health":
            self._require(method, "GET")
            self._send_json({"ok": True, "source_hash": app.source_hash, "totals": dict(app.totals)})
            return

        if path == "/api/manifest":
            self._require(method, "GET")
            self._send_json(app.manifest())
            return

        if path == "/api/units":
            self._require(method, "GET")
            vol_raw = param("vol")
            if vol_raw is None:
                raise ApiError(400, "invalid_vol", "缺少 vol 参数")
            try:
                vol = int(vol_raw)
            except ValueError:
                raise ApiError(400, "invalid_vol", "vol 须为整数")
            if vol < VOL_MIN or vol > VOL_MAX:
                raise ApiError(400, "invalid_vol", f"vol 须在 {VOL_MIN}–{VOL_MAX} 之间（第 76 卷已排除）")
            chapter = None
            chapter_raw = param("chapter")
            if chapter_raw is not None:
                try:
                    chapter = int(chapter_raw)
                except ValueError:
                    raise ApiError(400, "invalid_chapter", "chapter 须为整数")
                if chapter < 1:
                    raise ApiError(400, "invalid_chapter", "chapter 须为正整数")
            self._send_json(app.units_response(vol, chapter))
            return

        if path == "/api/answers":
            if method == "GET":
                self._send_json(app.answers_payload())
                return
            if method == "PUT":
                payload = self._json_body()
                if "answers" not in payload:
                    raise ApiError(400, "invalid_answers", "缺少 answers 字段")
                merged, accepted, count, ignored = app.merge_answers(payload["answers"])
                self._send_json(
                    {
                        "merged": merged,
                        "accepted": accepted,
                        "count": count,
                        "ignored": ignored,
                        "source_hash": app.source_hash,
                    }
                )
                return
            if method == "DELETE":
                key = param("key")
                if not key:
                    raise ApiError(400, "invalid_key", "缺少 key 参数")
                deleted, count = app.delete_answer(key)
                self._send_json({"deleted": deleted, "count": count})
                return
            raise ApiError(405, "method_not_allowed", "仅支持 GET、PUT、DELETE")

        if path == "/api/config":
            if method == "GET":
                self._send_json(app.config_payload())
                return
            if method == "POST":
                payload = self._json_body()
                if "config" not in payload:
                    raise ApiError(400, "invalid_config", "缺少 config 字段")
                config = app.update_config(payload["config"])
                self._send_json({"ok": True, "config": config})
                return
            raise ApiError(405, "method_not_allowed", "仅支持 GET、POST")

        if path == "/api/scope":
            self._require(method, "POST")
            payload = self._json_body()
            if "unit_keys" not in payload:
                raise ApiError(400, "invalid_scope", "缺少 unit_keys 字段")
            count = app.update_scope(payload["unit_keys"])
            self._send_json({"ok": True, "count": count})
            return

        if path == "/api/config/export":
            self._require(method, "GET")
            name, content_type, text = app.export_config_file()
            self._send(
                200,
                text.encode("utf-8"),
                content_type,
                {
                    "Cache-Control": "no-store",
                    "Content-Disposition": f'attachment; filename="{name}"',
                },
            )
            return

        if path == "/api/export":
            self._require(method, "GET")
            fmt = param("fmt")
            if fmt not in ("json", "tsv", "rewrite"):
                raise ApiError(400, "invalid_format", "fmt 须为 json、tsv 或 rewrite")
            name, content_type, text = app.export_file(fmt)
            self._send(
                200,
                text.encode("utf-8"),
                content_type,
                {
                    "Cache-Control": "no-store",
                    "Content-Disposition": f'attachment; filename="{name}"',
                },
            )
            return

        if path == "/api/import":
            self._require(method, "POST")
            payload = self._json_body()
            if "answers" not in payload:
                raise ApiError(400, "invalid_answers", "缺少 answers 字段")
            merged, _accepted, count, ignored = app.merge_answers(payload["answers"])
            self._send_json({"merged": merged, "count": count, "ignored": ignored})
            return

        if path == "/api/candidates":
            if method == "POST":
                count = app.save_candidates(self._json_body())
                self._send_json({"ok": True, "count": count})
                return
            if method == "GET":
                self._send_json({"candidates": app.all_candidates()})
                return
            raise ApiError(405, "method_not_allowed", "仅支持 GET、POST")

        if path == "/api/archive":
            self._require(method, "POST")
            self._send_json(app.archive())
            return

        raise ApiError(404, "not_found", f"未知接口：{path}")

    @staticmethod
    def _require(method: str, expected: str) -> None:
        if method != expected:
            raise ApiError(405, "method_not_allowed", f"仅支持 {expected}")

    # ---------- 静态文件 ----------

    def _serve_static(self, rel_path: str) -> None:
        rel_path = rel_path or "index.html"
        if rel_path.endswith("/"):
            rel_path += "index.html"
        if "\x00" in rel_path:
            raise ApiError(400, "invalid_path", "路径非法")
        web_root = WEB_DIR.resolve()
        candidate = (web_root / rel_path).resolve()
        try:
            candidate.relative_to(web_root)
        except ValueError:
            raise ApiError(404, "not_found", "资源不存在")
        if candidate.is_dir():
            candidate = candidate / "index.html"
        if not candidate.is_file():
            raise ApiError(404, "not_found", f"资源不存在：{rel_path}")
        suffix = candidate.suffix.lower()
        content_type = MIME_TYPES.get(suffix, "application/octet-stream")
        headers = {"Cache-Control": "no-cache"}
        if suffix in (".woff2", ".png", ".svg", ".ico"):
            headers["Cache-Control"] = "public, max-age=31536000, immutable"
        body = candidate.read_bytes()
        self._send(200, body, content_type, headers)


def lan_ipv4_addresses():
    addresses = set()
    try:
        for info in socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET, socket.SOCK_STREAM):
            ip = info[4][0]
            if not ip.startswith("127."):
                addresses.add(ip)
    except OSError:
        pass
    try:
        probe = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            probe.connect(("8.8.8.8", 80))
            ip = probe.getsockname()[0]
            if ip and not ip.startswith("127."):
                addresses.add(ip)
        finally:
            probe.close()
    except OSError:
        pass
    return sorted(addresses)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="3B 逐卷人工审定本地审阅服务")
    parser.add_argument("--port", type=int, default=8899, help="监听端口，默认 8899；0 表示随机端口")
    parser.add_argument("--root", default=None, help="仓库根目录，默认自动定位")
    args = parser.parse_args(argv)

    if not (0 <= args.port <= 65535):
        print("端口须在 0–65535 之间", file=sys.stderr)
        return 2

    root = Path(args.root).resolve() if args.root else DEFAULT_ROOT
    app = App(root)
    try:
        app.load()
    except StartupError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    try:
        httpd = ThreadingHTTPServer(("0.0.0.0", args.port), Handler)
    except OSError as exc:
        print(f"无法绑定端口 {args.port}：{exc}", file=sys.stderr)
        return 1
    httpd.app = app  # type: ignore[attr-defined]
    port = httpd.server_address[1]

    print("3B 逐卷人工审定 · 本地审阅服务")
    print(f"  仓库根：{root}")
    print(f"  数据目录：{DATA_DIR}")
    print(
        "  自校验：{vols} 卷 / 章 {chapters} / 节 {sections} / 小节 {subsections} / 合计 {units}".format(
            **app.totals
        )
    )
    print(f"  源指纹：{app.source_hash[:16]}…")
    print(f"  监听：0.0.0.0:{port}")
    for ip in lan_ipv4_addresses():
        print(f"  局域网：http://{ip}:{port}/")
    print(f"  本机：http://127.0.0.1:{port}/")
    print("按 Ctrl+C 停止。")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n已停止。")
    finally:
        httpd.server_close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
