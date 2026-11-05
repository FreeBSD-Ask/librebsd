# -*- coding: utf-8 -*-
"""3B 逐卷人工审定本地服务的全量自动化测试（pytest）。

覆盖：manifest 口径与源指纹、1–75 卷逐卷对位、徽标映射、答案合并、
原子写与快照轮转、配置与作用域校验、三种导出、归档、导入幂等、候选批次。

数据源只读；每个测试使用独立的 tmp_path 数据目录，服务绑定随机端口。
"""

from __future__ import annotations

import csv
import importlib.util
import json
import re
import socket
import threading
import urllib.error
import urllib.parse
import urllib.request
from collections import OrderedDict
from functools import lru_cache
from http.server import ThreadingHTTPServer
from pathlib import Path

import pytest

TOOL = Path(__file__).resolve().parents[1]
REPO = Path(__file__).resolve().parents[5]

OUTLINE_REL = Path("05-卷册大纲") / "目录" / "data" / "outline.txt"
DESIGN_REL = Path("05-卷册大纲") / "映射" / "title-design"
MACHINE_REL = Path("05-卷册大纲") / "映射" / "title-review" / "full-review" / "机判结果.tsv"
HUMAN_REL = Path("05-卷册大纲") / "映射" / "title-review" / "full-review" / "人判" / "人判总表.tsv"

EXPECTED = {"units": 23722, "chapters": 539, "sections": 3918, "subsections": 19265, "vols": 75}
HUMAN_FAIL_WORDS = {"fail", "有问题", "不通过", "未通过"}


def _load_server_module():
    spec = importlib.util.spec_from_file_location("serve_3b_review_under_test", TOOL / "serve_3b_review.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


srv = _load_server_module()


# ---------------------------------------------------------------------------
# 数据源独立解析（不复用被测实现，避免自证）
# ---------------------------------------------------------------------------

_CN = {ch: idx + 1 for idx, ch in enumerate("一二三四五六七八九十")}


def cn_int(text: str) -> int:
    if text == "十":
        return 10
    if "十" in text:
        tens, ones = text.split("十", 1)
        return (_CN[tens] if tens else 1) * 10 + (_CN[ones] if ones else 0)
    return _CN[text]


def clean_title(text: str) -> str:
    return text.split("@@", 1)[0].strip()


@lru_cache(maxsize=1)
def expected_model():
    """独立解析 outline 与台账，返回逐卷期望键序列、题名、计数与合计。"""
    vol_re = re.compile(r"^#\s*第([一二三四五六七八九十]+)卷\s*(.*)$")
    chapter_re = re.compile(r"^##\s*第\s*(\d+)\s*章\s*(.*)$")
    section_re = re.compile(r"^-\s*(\d+)\.(\d+)\s+(.*)$")

    outline = OrderedDict()
    cur_vol = cur_chapter = None
    for raw in (REPO / OUTLINE_REL).read_text(encoding="utf-8-sig").splitlines():
        line = raw.rstrip()
        if not line:
            continue
        m = vol_re.match(line)
        if m:
            vol = cn_int(m.group(1))
            if vol > 75:
                cur_vol = cur_chapter = None
                continue
            outline[vol] = {"title": clean_title(m.group(2)), "chapters": OrderedDict()}
            cur_vol, cur_chapter = vol, None
            continue
        m = chapter_re.match(line)
        if m and cur_vol is not None:
            chapter = int(m.group(1))
            outline[cur_vol]["chapters"][chapter] = {"title": clean_title(m.group(2)), "sections": OrderedDict()}
            cur_chapter = chapter
            continue
        m = section_re.match(line)
        if m and cur_vol is not None and cur_chapter is not None:
            section = int(m.group(2))
            outline[cur_vol]["chapters"][cur_chapter]["sections"][section] = {
                "title": clean_title(m.group(3))
            }

    ledgers = {}
    for vol in range(1, 76):
        path = REPO / DESIGN_REL / f"V{vol:02d}.tsv"
        rows = []
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            for record in csv.DictReader(handle, delimiter="\t"):
                rows.append(
                    {
                        "subsection_id": record["subsection_id"].strip(),
                        "chapter": int(record["chapter"]),
                        "section": int(record["section"]),
                        "title": record["title"].strip(),
                        "order": int(record["order"] or 0),
                        "source_count": int(record["source_count"] or 0),
                    }
                )
        ledgers[vol] = rows

    keys_by_vol = OrderedDict()
    titles = {}
    counts = OrderedDict()
    total_chapters = total_sections = total_subsections = 0
    for vol in range(1, 76):
        grouped = {}
        for row in ledgers[vol]:
            grouped.setdefault((row["chapter"], row["section"]), []).append(row)
        keys = []
        chapters = sections = 0
        for chapter_no, chapter in outline[vol]["chapters"].items():
            chapters += 1
            key = f"V{vol:02d}.C{chapter_no:02d}"
            keys.append(key)
            titles[key] = chapter["title"]
            for section_no, section in chapter["sections"].items():
                sections += 1
                skey = f"V{vol:02d}.{chapter_no:02d}.{section_no:02d}"
                keys.append(skey)
                titles[skey] = section["title"]
                subset = sorted(grouped.get((chapter_no, section_no), []), key=lambda r: (r["order"], r["subsection_id"]))
                for row in subset:
                    keys.append(row["subsection_id"])
                    titles[row["subsection_id"]] = row["title"]
        keys_by_vol[vol] = keys
        counts[vol] = {
            "chapters": chapters,
            "sections": sections,
            "subsections": len(ledgers[vol]),
            "units": len(keys),
        }
        total_chapters += chapters
        total_sections += sections
        total_subsections += len(ledgers[vol])

    totals = {
        "chapters": total_chapters,
        "sections": total_sections,
        "subsections": total_subsections,
        "units": total_chapters + total_sections + total_subsections,
    }
    assert totals == {k: EXPECTED[k] for k in totals}, totals
    return outline, ledgers, keys_by_vol, titles, counts, totals


@lru_cache(maxsize=1)
def expected_flags():
    _, _, _, _, _, _ = expected_model()
    outline, ledgers, keys_by_vol, _, _, _ = expected_model()
    valid = {key for keys in keys_by_vol.values() for key in keys}

    machine = set()
    with (REPO / MACHINE_REL).open("r", encoding="utf-8-sig", newline="") as handle:
        for record in csv.DictReader(handle, delimiter="\t"):
            try:
                vol = int((record.get("vol") or "").strip())
            except ValueError:
                continue
            if not (1 <= vol <= 75):
                continue
            if (record.get("result") or "").strip().upper() != "FAIL":
                continue
            sid = (record.get("subsection_id") or "").strip()
            if sid in valid:
                machine.add(sid)

    human = set()
    with (REPO / HUMAN_REL).open("r", encoding="utf-8-sig", newline="") as handle:
        for record in csv.DictReader(handle, delimiter="\t"):
            verdict = (record.get("verdict") or "").strip()
            if verdict.lower() not in HUMAN_FAIL_WORDS and verdict not in HUMAN_FAIL_WORDS:
                continue
            kind = (record.get("item_kind") or "").strip()
            raw_key = (record.get("item_key") or "").strip()
            mapped = None
            if kind in ("title", "evidence_row"):
                mapped = raw_key
            elif kind == "section":
                m = re.match(r"^V(\d{1,2})\.(\d+)\.(\d+)$", raw_key)
                if m:
                    mapped = f"V{int(m.group(1)):02d}.{int(m.group(2)):02d}.{int(m.group(3)):02d}"
            if mapped in valid:
                human.add(mapped)
    return machine, human


# ---------------------------------------------------------------------------
# 隔离环境：独立 data 目录 + 随机端口
# ---------------------------------------------------------------------------


class Env:
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir
        self.app = None
        self.httpd = None
        self.thread = None
        self.base = None

    def _patch_globals(self):
        data = self.data_dir
        srv.DATA_DIR = data
        srv.ANSWERS_DIR = data / "answers"
        srv.SNAPSHOTS_DIR = data / "answers" / "snapshots"
        srv.CONFIG_DIR = data / "config"
        srv.CANDIDATES_DIR = data / "candidates"
        srv.EXPORTS_DIR = data / "exports"

    def start(self):
        self._patch_globals()
        self.app = srv.App(REPO)
        self.app.load()
        self.httpd = ThreadingHTTPServer(("127.0.0.1", 0), srv.Handler)
        self.httpd.app = self.app
        self.thread = threading.Thread(target=self.httpd.serve_forever, daemon=True)
        self.thread.start()
        self.base = f"http://127.0.0.1:{self.httpd.server_address[1]}"
        return self

    def stop(self):
        if self.httpd is not None:
            self.httpd.shutdown()
            self.httpd.server_close()
            self.thread.join(timeout=5)
            self.httpd = None
            self.thread = None

    def restart(self):
        self.stop()
        self.start()
        return self

    # ---- 便捷读写 ----
    def call(self, method, path, payload=None, headers=None):
        data = None
        hdrs = dict(headers or {})
        if payload is not None:
            data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
            hdrs["Content-Type"] = "application/json"
        request = urllib.request.Request(self.base + path, data=data, method=method, headers=hdrs)
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return response.status, response.headers, response.read()
        except urllib.error.HTTPError as exc:
            return exc.code, exc.headers, exc.read()

    def json(self, path):
        status, _headers, body = self.call("GET", path)
        assert status == 200, (path, status, body[:300])
        return json.loads(body.decode("utf-8"))

    def put_answers(self, answers):
        return self.call("PUT", "/api/answers", {"answers": answers})

    def answers(self):
        return self.json("/api/answers")["answers"]

    def answer(self, key):
        return self.answers().get(key)


@pytest.fixture
def env(tmp_path):
    instance = Env(tmp_path / "data").start()
    try:
        yield instance
    finally:
        instance.stop()


def error_of(body: bytes) -> dict:
    return json.loads(body.decode("utf-8"))


def answer_payload(verdict="ok", title="", note="", updated_at="2031-01-01T00:00:00+00:00"):
    return {"verdict": verdict, "custom_title": title, "note": note, "updated_at": updated_at}


# ---------------------------------------------------------------------------
# manifest / 口径 / 源指纹
# ---------------------------------------------------------------------------


def test_manifest_totals_vols_and_source_hash(env):
    manifest = env.json("/api/manifest")
    assert manifest["totals"] == EXPECTED
    assert len(manifest["vols"]) == EXPECTED["vols"]
    assert [item["vol"] for item in manifest["vols"]] == list(range(1, 76))
    assert sum(item["units"] for item in manifest["vols"]) == EXPECTED["units"]
    assert manifest["scope"] == {"active": False, "configured": None, "effective": EXPECTED["units"]}
    assert manifest["config"]["vol_start"] == 1 and manifest["config"]["vol_end"] == 75

    again = env.json("/api/manifest")
    assert again["source_hash"] == manifest["source_hash"]

    health = env.json("/api/health")
    assert health["ok"] is True
    assert health["totals"] == EXPECTED
    assert health["source_hash"] == manifest["source_hash"]

    hash_before = manifest["source_hash"]
    env.restart()
    assert env.json("/api/manifest")["source_hash"] == hash_before


def test_vol76_and_invalid_vol_rejected(env):
    for query in ("vol=76", "vol=0", "vol=-1", "vol=abc", "vol="):
        status, _headers, body = env.call("GET", f"/api/units?{query}")
        assert status == 400, (query, status)
        payload = error_of(body)
        assert payload["error"] in ("invalid_vol",)
        assert "units" not in payload
    status, _headers, _body = env.call("GET", "/api/units")
    assert status == 400


def test_all_volumes_units_match_outline_and_ledgers(env):
    outline, ledgers, keys_by_vol, titles, counts, _totals = expected_model()
    manifest = env.json("/api/manifest")
    meta = {item["vol"]: item for item in manifest["vols"]}

    for vol in range(1, 76):
        data = env.json(f"/api/units?vol={vol}")
        assert data["vol"] == vol
        units = data["units"]
        assert [u["key"] for u in units] == keys_by_vol[vol], f"第 {vol} 卷键序列不符"
        assert len(units) == counts[vol]["units"]
        assert meta[vol]["chapters"] == counts[vol]["chapters"]
        assert meta[vol]["sections"] == counts[vol]["sections"]
        assert meta[vol]["subsections"] == counts[vol]["subsections"]
        assert meta[vol]["units"] == counts[vol]["units"]

        expect_level = []
        for key in keys_by_vol[vol]:
            expect_level.append(
                "chapter" if ".C" in key else ("section" if key.count(".") == 2 else "subsection")
            )
        assert [u["level"] for u in units] == expect_level

        for unit in units:
            assert unit["vol"] == vol
            assert unit["title"] == titles[unit["key"]], unit["key"]
            if unit["level"] == "subsection":
                assert unit["source_count"] is not None
                assert unit["thesis"] is not None
            else:
                assert unit["source_count"] is None
                assert unit["thesis"] is None
            # 章/节/小节顺序由 order 递增保证
        assert [u["order"] for u in units] == list(range(1, len(units) + 1))

    # 交叉核对台账小节数与 outline 章/节数
    total_subsections = sum(len(rows) for rows in ledgers.values())
    assert total_subsections == EXPECTED["subsections"]
    assert sum(len(item["chapters"]) for item in outline.values()) == EXPECTED["chapters"]


def test_badges_match_machine_and_human_fail_sets(env):
    machine, human = expected_flags()
    assert machine and human
    seen_machine = seen_human = 0
    for vol in range(1, 76):
        units = env.json(f"/api/units?vol={vol}")["units"]
        for unit in units:
            key = unit["key"]
            got_machine = bool(unit.get("flag_machine"))
            got_human = bool(unit.get("flag_human"))
            assert got_machine == (key in machine), key
            assert got_human == (key in human), key
            seen_machine += got_machine
            seen_human += got_human
    assert seen_machine == len(machine)
    assert seen_human == len(human)


# ---------------------------------------------------------------------------
# 答案合并 / 删除
# ---------------------------------------------------------------------------


def test_answers_put_get_merge_and_validation(env):
    key = "V01.1.1.1"
    status, _h, body = env.put_answers({key: answer_payload("ok", updated_at="2031-01-01T00:00:00+00:00")})
    assert status == 200
    result = error_of(body)
    assert result["merged"] == 1 and result["accepted"] == 1 and result["count"] == 1
    assert result["source_hash"] == env.app.source_hash

    payload = env.json("/api/answers")
    assert payload["count"] == 1
    assert payload["source_hash"] == env.app.source_hash
    assert payload["answers"][key]["verdict"] == "ok"
    assert payload["answers"][key]["custom_title"] == ""

    # 较新者胜
    status, _h, body = env.put_answers({key: answer_payload("reroll", updated_at="2031-02-01T00:00:00+00:00")})
    assert status == 200 and error_of(body)["merged"] == 1
    assert env.answer(key)["verdict"] == "reroll"

    # 较旧者被忽略
    status, _h, body = env.put_answers({key: answer_payload("custom", "旧题", "n", "2030-01-01T00:00:00+00:00")})
    assert status == 200 and error_of(body)["merged"] == 0
    assert env.answer(key)["verdict"] == "reroll"

    # 相等时间戳保留旧值
    status, _h, body = env.put_answers({key: answer_payload("custom", "同刻", "", "2031-02-01T00:00:00+00:00")})
    assert status == 200 and error_of(body)["merged"] == 0
    assert env.answer(key)["verdict"] == "reroll"

    # 非法 verdict：整批 4xx 且状态不变
    status, _h, body = env.put_answers({key: answer_payload("maybe", updated_at="2032-01-01T00:00:00+00:00")})
    assert status == 400
    err = error_of(body)
    assert err["error"] == "invalid_answers"
    assert err["invalid"] == [key]
    assert env.answer(key)["verdict"] == "reroll"

    # 空 custom 题名
    status, _h, body = env.put_answers({key: answer_payload("custom", "   ", "", "2032-01-01T00:00:00+00:00")})
    assert status == 400
    assert error_of(body)["invalid"] == [key]

    # 超长 custom 题名（121 字）
    status, _h, body = env.put_answers(
        {key: answer_payload("custom", "题" * 121, "", "2032-01-01T00:00:00+00:00")}
    )
    assert status == 400

    # 超长备注（501 字）
    status, _h, body = env.put_answers(
        {key: answer_payload("custom", "正常题名", "备" * 501, "2032-01-01T00:00:00+00:00")}
    )
    assert status == 400

    # 未知字段
    bad = answer_payload("ok", updated_at="2032-01-01T00:00:00+00:00")
    bad["extra"] = 1
    status, _h, body = env.put_answers({key: bad})
    assert status == 400

    # 混合批次：有效项也不得落库
    other = "V01.1.1.2"
    status, _h, body = env.put_answers(
        {
            other: answer_payload("ok", updated_at="2032-01-01T00:00:00+00:00"),
            key: answer_payload("bad", updated_at="2032-01-01T00:00:00+00:00"),
        }
    )
    assert status == 400
    assert other not in env.answers()

    # 越界/陈旧键静默丢弃
    status, _h, body = env.put_answers({"V76.1.1.1": answer_payload("ok"), "NOT-A-KEY": answer_payload("ok")})
    assert status == 200
    result = error_of(body)
    assert result["merged"] == 0 and result["accepted"] == 0
    assert result["count"] == 1

    # 请求体形态校验
    status, _h, _b = env.call("PUT", "/api/answers", {})
    assert status == 400
    status, _h, _b = env.call("PUT", "/api/answers", {"answers": []})
    assert status == 400
    status, _h, _b = env.call("PUT", "/api/answers", None)
    assert status == 400


def test_delete_answer(env):
    key = "V01.1.1.3"
    env.put_answers({key: answer_payload("ok", updated_at="2031-01-01T00:00:00+00:00")})
    assert env.answer(key) is not None

    status, _h, body = env.call("DELETE", "/api/answers?key=" + urllib.parse.quote(key))
    assert status == 200
    assert error_of(body) == {"deleted": True, "count": 0}
    assert env.answer(key) is None

    status, _h, body = env.call("DELETE", "/api/answers?key=" + urllib.parse.quote(key))
    assert status == 200
    assert error_of(body) == {"deleted": False, "count": 0}

    status, _h, _b = env.call("DELETE", "/api/answers")
    assert status == 400


def test_answers_persist_across_restart(env):
    key = "V01.1.1.4"
    env.put_answers({key: answer_payload("custom", "持久化题名", "备注", "2031-03-01T00:00:00+00:00")})
    env.restart()
    stored = env.answer(key)
    assert stored["verdict"] == "custom"
    assert stored["custom_title"] == "持久化题名"
    assert stored["note"] == "备注"
    assert env.json("/api/answers")["count"] == 1


# ---------------------------------------------------------------------------
# 原子写 / 快照轮转
# ---------------------------------------------------------------------------


def test_atomic_write_and_snapshot_rotation(env):
    keys = [key for key in expected_model()[2][1] if key.count(".") == 3][:12]
    assert len(keys) == 12
    for index, key in enumerate(keys):
        status, _h, body = env.put_answers(
            {key: answer_payload("ok", updated_at=f"2031-01-{index + 1:02d}T00:00:00+00:00")}
        )
        assert status == 200

    answers_path = env.data_dir / "answers" / "answers.json"
    assert answers_path.is_file()
    raw = answers_path.read_bytes()
    assert not raw.startswith(b"\xef\xbb\xbf"), "answers.json 不得带 BOM"
    assert b"\r" not in raw, "answers.json 须为 LF"
    parsed = json.loads(raw.decode("utf-8"))
    assert sorted(parsed["answers"]) == sorted(keys)
    assert len(parsed["answers"]) == 12

    residue = [p for p in env.data_dir.rglob("*") if p.is_file() and (p.name.endswith(".tmp") or ".tmp-" in p.name)]
    assert residue == [], residue

    snapshots = sorted((env.data_dir / "answers" / "snapshots").glob("answers-*.json"))
    assert len(snapshots) == 10, len(snapshots)
    for path in snapshots:
        json.loads(path.read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
# 配置
# ---------------------------------------------------------------------------


def test_config_validation_and_effect(env):
    default = env.json("/api/config")
    assert default["config"] == srv.DEFAULT_CONFIG
    assert default["scope"]["unit_keys"] is None

    invalid_cases = [
        ({"vol_start": 0}, "vol_start"),
        ({"vol_start": 76}, "vol_start"),
        ({"vol_end": 0}, "vol_end"),
        ({"vol_end": 76}, "vol_end"),
        ({"vol_start": 5, "vol_end": 2}, "vol_range"),
        ({"daily_goal": 0}, "daily_goal"),
        ({"daily_goal": 5001}, "daily_goal"),
        ({"theme": "dark"}, "theme"),
        ({"font_size": "xl"}, "font_size"),
        ({"only_flagged": "yes"}, "only_flagged"),
        ({"labels": {"ok": "九个字九个字九个字"}}, "labels"),
        ({"labels": {"ok": "好", "extra": "x"}}, "labels"),
        ({"labels": "不是对象"}, "labels"),
        ({"unknown_key": 1}, "unknown"),
        ({"vol_start": "2"}, "vol_start"),
    ]
    for patch, field in invalid_cases:
        status, _h, body = env.call("POST", "/api/config", {"config": patch})
        assert status == 400, (patch, status)
        err = error_of(body)
        assert err["error"] == "invalid_config"
        assert field in err.get("errors", {}), (patch, err)

    # 非法请求不得改变现有配置
    assert env.json("/api/config")["config"] == srv.DEFAULT_CONFIG

    status, _h, _b = env.call("POST", "/api/config", {})
    assert status == 400
    status, _h, _b = env.call("POST", "/api/config", {"config": "x"})
    assert status == 400

    patch = {
        "daily_goal": 321,
        "theme": "day",
        "font_size": "l",
        "labels": {"ok": "通过"},
        "only_flagged": True,
    }
    status, _h, body = env.call("POST", "/api/config", {"config": patch})
    assert status == 200
    config = error_of(body)["config"]
    assert config["daily_goal"] == 321
    assert config["theme"] == "day"
    assert config["font_size"] == "l"
    assert config["labels"] == {"ok": "通过", "reroll": "重拟", "custom": "自定义"}
    assert config["only_flagged"] is True
    assert env.json("/api/config")["config"] == config

    stored = json.loads((env.data_dir / "config" / "config.json").read_text(encoding="utf-8"))
    assert stored == config

    # only_flagged 生效：第 1 卷仅返回带徽标单元
    machine, human = expected_flags()
    flagged = set(machine) | set(human)
    units = env.json("/api/units?vol=1")["units"]
    assert units
    assert all(unit["key"] in flagged for unit in units)
    expected_keys = [
        key for key in expected_model()[2][1] if key in flagged
    ]
    assert [unit["key"] for unit in units] == expected_keys

    # 重新启动后配置仍在
    env.restart()
    assert env.json("/api/config")["config"]["daily_goal"] == 321


# ---------------------------------------------------------------------------
# 作用域
# ---------------------------------------------------------------------------


def test_scope_validation_and_filtered_counts(env):
    status, _h, body = env.call(
        "POST", "/api/scope", {"unit_keys": ["V76.1.1.1", "NOT-A-KEY"]}
    )
    assert status == 400
    err = error_of(body)
    assert err["error"] == "invalid_scope"
    assert err["invalid"] == ["V76.1.1.1", "NOT-A-KEY"]
    assert env.json("/api/manifest")["scope"]["active"] is False

    status, _h, _b = env.call("POST", "/api/scope", {})
    assert status == 400

    keys = expected_model()[2][1][:5]
    status, _h, body = env.call("POST", "/api/scope", {"unit_keys": keys})
    assert status == 200
    assert error_of(body) == {"ok": True, "count": 5}

    manifest = env.json("/api/manifest")
    assert manifest["scope"] == {"active": True, "configured": 5, "effective": 5}
    assert env.json("/api/config")["scope"]["unit_keys"] == keys

    units = env.json("/api/units?vol=1")["units"]
    assert [unit["key"] for unit in units] == keys
    assert env.json("/api/units?vol=2")["units"] == []

    # 重复键去重
    status, _h, body = env.call("POST", "/api/scope", {"unit_keys": [keys[0], keys[0]]})
    assert status == 200 and error_of(body)["count"] == 1
    assert env.json("/api/manifest")["scope"]["effective"] == 1

    # 重启保持
    env.restart()
    assert env.json("/api/manifest")["scope"]["effective"] == 1

    # 空数组恢复全量
    status, _h, body = env.call("POST", "/api/scope", {"unit_keys": []})
    assert status == 200 and error_of(body)["count"] == 0
    manifest = env.json("/api/manifest")
    assert manifest["scope"]["active"] is False
    assert manifest["scope"]["effective"] == EXPECTED["units"]
    assert env.json("/api/config")["scope"]["unit_keys"] is None

    status, _h, _b = env.call("POST", "/api/scope", {"unit_keys": "x"})
    assert status == 400


# ---------------------------------------------------------------------------
# 导出
# ---------------------------------------------------------------------------

EXPORT_HEADER_TSV = [
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
EXPORT_HEADER_REWRITE = [
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


def seed_three_answers(env):
    keys = expected_model()[2][1]
    ok_key, reroll_key, custom_key = keys[0], keys[1], keys[2]
    env.put_answers(
        {
            ok_key: answer_payload("ok", updated_at="2031-01-01T00:00:00+00:00"),
            reroll_key: answer_payload("reroll", "", "待重拟", "2031-01-02T00:00:00+00:00"),
            custom_key: answer_payload("custom", "自定义题名", "备注文本", "2031-01-03T00:00:00+00:00"),
        }
    )
    return ok_key, reroll_key, custom_key


def test_export_json_tsv_rewrite(env):
    ok_key, reroll_key, custom_key = seed_three_answers(env)

    status, headers, body = env.call("GET", "/api/export?fmt=json")
    assert status == 200
    assert "application/json" in headers.get("Content-Type", "")
    assert headers.get("Content-Disposition", "").startswith("attachment;")
    payload = json.loads(body.decode("utf-8"))
    assert payload["meta"]["total_units"] == EXPECTED["units"]
    assert payload["meta"]["answered"] == 3
    assert payload["meta"]["scope_effective"] == EXPECTED["units"]
    assert payload["meta"]["source_hash"] == env.app.source_hash
    assert payload["meta"]["counts"] == {"ok": 1, "reroll": 1, "custom": 1}
    assert set(payload["answers"]) == {ok_key, reroll_key, custom_key}

    status, headers, body = env.call("GET", "/api/export?fmt=tsv")
    assert status == 200
    assert "tab-separated-values" in headers.get("Content-Type", "")
    lines = body.decode("utf-8").splitlines()
    assert lines[0].split("\t") == EXPORT_HEADER_TSV
    assert len(lines) == 4
    rows = [line.split("\t") for line in lines[1:]]
    assert all(len(row) == 10 for row in rows)
    assert [row[0] for row in rows] == [ok_key, reroll_key, custom_key]
    assert [row[6] for row in rows] == ["ok", "reroll", "custom"]

    status, headers, body = env.call("GET", "/api/export?fmt=rewrite")
    assert status == 200
    lines = body.decode("utf-8").splitlines()
    assert lines[0].split("\t") == EXPORT_HEADER_REWRITE
    assert len(lines) == 3  # 表头 + custom + reroll，ok 行不导出
    rows = [line.split("\t") for line in lines[1:]]
    assert all(len(row) == 13 for row in rows)
    by_key = {row[0]: row for row in rows}
    assert ok_key not in by_key
    assert by_key[reroll_key][6] == "重拟待办"
    assert by_key[reroll_key][7] == ""
    assert by_key[custom_key][6] == "改题"
    assert by_key[custom_key][7] == "自定义题名"
    assert all(row[12] == env.app.source_hash for row in rows)

    status, _h, _b = env.call("GET", "/api/export?fmt=xml")
    assert status == 400
    status, _h, _b = env.call("GET", "/api/export")
    assert status == 400

    # 导出文件落盘且同秒导出不覆盖
    export_dir = env.data_dir / "exports"
    json_files = sorted(export_dir.glob("3B-answers-*.json"))
    assert len(json_files) >= 1
    env.call("GET", "/api/export?fmt=json")
    assert len(sorted(export_dir.glob("3B-answers-*.json"))) == len(json_files) + 1
    assert len(sorted(export_dir.glob("3B-answers-*.tsv"))) == 1


def test_archive_directory_and_log(env):
    seed_three_answers(env)
    status, _h, body = env.call("POST", "/api/archive", {})
    assert status == 200
    payload = error_of(body)
    assert payload["ok"] is True
    assert payload["files"] == ["answers.json", "answers.tsv", "rewrite.tsv"]
    assert payload["count"] == 3
    assert payload["dir"].startswith("data/exports/")

    target = env.data_dir / "exports" / Path(payload["dir"]).name
    assert target.is_dir()
    assert {p.name for p in target.iterdir()} == {"answers.json", "answers.tsv", "rewrite.tsv"}
    json.loads((target / "answers.json").read_text(encoding="utf-8"))
    assert (target / "answers.tsv").read_text(encoding="utf-8").splitlines()[0].split("\t") == EXPORT_HEADER_TSV
    assert (target / "rewrite.tsv").read_text(encoding="utf-8").splitlines()[0].split("\t") == EXPORT_HEADER_REWRITE

    log_path = env.data_dir / "exports" / "archive_log.jsonl"
    lines = [json.loads(line) for line in log_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    assert len(lines) == 1
    assert lines[0]["count"] == 3
    assert lines[0]["files"] == ["answers.json", "answers.tsv", "rewrite.tsv"]
    assert lines[0]["source_hash"] == env.app.source_hash

    status, _h, _b = env.call("POST", "/api/archive", {})
    assert status == 200
    lines = [json.loads(line) for line in log_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    assert len(lines) == 2
    assert len([p for p in (env.data_dir / "exports").iterdir() if p.is_dir()]) == 2


# ---------------------------------------------------------------------------
# 导入 / 候选
# ---------------------------------------------------------------------------


def test_import_is_idempotent(env):
    payload = {"answers": {"V01.1.1.1": answer_payload("ok", updated_at="2031-05-01T00:00:00+00:00")}}
    status, _h, body = env.call("POST", "/api/import", payload)
    assert status == 200
    assert error_of(body) == {"merged": 1, "count": 1, "ignored": 0}

    status, _h, body = env.call("POST", "/api/import", payload)
    assert status == 200
    assert error_of(body) == {"merged": 0, "count": 1, "ignored": 0}
    assert env.json("/api/answers")["count"] == 1
    assert env.answer("V01.1.1.1")["verdict"] == "ok"

    status, _h, _b = env.call("POST", "/api/import", {})
    assert status == 400
    status, _h, _b = env.call(
        "POST", "/api/import", {"answers": {"V01.1.1.1": answer_payload("invalid")}}
    )
    assert status == 400


def test_candidates_batch_validation_and_merge(env):
    key1, key2 = "V01.1.1.1", "V01.1.1.2"

    # 未标记 reroll 不得写候选
    status, _h, body = env.call(
        "POST",
        "/api/candidates",
        {"batch_id": "b1", "candidates": {key1: [{"candidate_id": "c1", "new_title": "候选一"}]}},
    )
    assert status == 400
    assert error_of(body)["invalid"] == [key1]

    # 非法 batch_id / 空候选 / 结构非法
    for payload in (
        {"batch_id": "含有中文", "candidates": {key1: [{"candidate_id": "c1", "new_title": "x"}]}},
        {"batch_id": "", "candidates": {key1: [{"candidate_id": "c1", "new_title": "x"}]}},
        {"batch_id": "b1", "candidates": {}},
        {"batch_id": "b1", "candidates": []},
    ):
        status, _h, _b = env.call("POST", "/api/candidates", payload)
        assert status == 400, payload

    env.put_answers(
        {
            key1: answer_payload("reroll", updated_at="2031-06-01T00:00:00+00:00"),
            key2: answer_payload("reroll", updated_at="2031-06-01T00:00:00+00:00"),
        }
    )

    # 结构非法项整批拒绝
    status, _h, body = env.call(
        "POST",
        "/api/candidates",
        {
            "batch_id": "b-bad",
            "candidates": {
                key1: [{"candidate_id": "c1", "new_title": "候选一"}],
                key2: [{"candidate_id": "c2", "new_title": "  "}],
            },
        },
    )
    assert status == 400
    assert error_of(body)["invalid"] == [key2]
    assert not (env.data_dir / "candidates" / "b-bad.json").exists()

    status, _h, body = env.call(
        "POST",
        "/api/candidates",
        {
            "batch_id": "b1",
            "candidates": {
                key1: [
                    {"candidate_id": "c1", "new_title": "候选一", "rationale": "理由一", "source": "来源一"},
                    {"candidate_id": "c2", "new_title": "候选二"},
                ]
            },
        },
    )
    assert status == 200 and error_of(body) == {"ok": True, "count": 1}
    assert (env.data_dir / "candidates" / "b1.json").is_file()

    merged = env.json("/api/candidates")["candidates"]
    assert [item["new_title"] for item in merged[key1]] == ["候选一", "候选二"]
    assert merged[key1][0]["rationale"] == "理由一"

    status, _h, body = env.call(
        "POST",
        "/api/candidates",
        {"batch_id": "b2", "candidates": {key2: [{"candidate_id": "d1", "new_title": "另一候选"}]}},
    )
    assert status == 200
    merged = env.json("/api/candidates")["candidates"]
    assert set(merged) == {key1, key2}

    status, _h, _b = env.call(
        "POST",
        "/api/candidates",
        {"batch_id": "b3", "candidates": {key1: [{"candidate_id": "e1", "new_title": "最新候选"}]}},
    )
    assert status == 200
    merged = env.json("/api/candidates")["candidates"]
    assert [item["new_title"] for item in merged[key1]] == ["最新候选"]

    env.restart()
    merged = env.json("/api/candidates")["candidates"]
    assert [item["new_title"] for item in merged[key1]] == ["最新候选"]
    assert set(merged) == {key1, key2}


# ---------------------------------------------------------------------------
# 静态资源与错误口径
# ---------------------------------------------------------------------------


def test_static_assets_and_error_responses(env):
    status, headers, body = env.call("GET", "/")
    assert status == 200
    assert "text/html" in headers.get("Content-Type", "")
    assert b"./app.js" in body

    status, _h, body = env.call("GET", "/app.js")
    assert status == 200 and b"loadAll" in body

    status, _h, _b = env.call("GET", "/manifest.webmanifest")
    assert status == 200

    status, _h, body = env.call("GET", "/icons/icon-192.png")
    assert status == 200 and body.startswith(b"\x89PNG")

    status, _h, _b = env.call("GET", "/..%2fserve_3b_review.py")
    assert status == 404

    status, _h, body = env.call("GET", "/api/nope")
    assert status == 404 and error_of(body)["error"] == "not_found"

    status, _h, _b = env.call("POST", "/api/units?vol=1", {})
    assert status == 405

    status, _h, _b = env.call("GET", "/api/answers?key=x")
    assert status == 200

    status, _h, _b = env.call("HEAD", "/")
    assert status == 200

    status, _h, _b = env.call("PUT", "/api/config", {"config": {}})
    assert status == 405


# ---------------------------------------------------------------------------
# 重拟标签（reroll tags）：给 AI 重拟批的指令面
# ---------------------------------------------------------------------------


def _reroll_answer(tags=None, merge_target=None):
    payload = answer_payload("reroll")
    payload["tags"] = tags or []
    payload["merge_target"] = merge_target or ""
    return payload


def test_reroll_tags_valid_and_rewrite_columns(env):
    keys = expected_model()[2][1]
    status, _h, _b = env.put_answers({
        keys[0]: _reroll_answer(["content", "length"]),
        keys[1]: _reroll_answer(["content", "merge", "format"], "prev"),
    })
    assert status == 200
    answers = env.json("/api/answers")["answers"]
    assert answers[keys[0]]["tags"] == ["content", "length"]
    assert answers[keys[1]]["merge_target"] == "prev"
    status, _h, body = env.call("GET", "/api/export?fmt=rewrite")
    rows = {line.split("\t")[0]: line.split("\t") for line in body.decode("utf-8").splitlines()[1:]}
    assert rows[keys[0]][8] == "content+length"
    assert rows[keys[1]][8] == "content+merge+format"
    assert rows[keys[1]][9] == "prev"


def test_reroll_tags_reject_invalid(env):
    keys = expected_model()[2][1]
    status, _h, _b = env.put_answers({keys[0]: _reroll_answer(["nope"])})
    assert status == 400
    status, _h, _b = env.put_answers({keys[0]: answer_payload("ok") | {"tags": ["content"]}})
    assert status == 400
    status, _h, _b = env.put_answers({keys[0]: _reroll_answer(["content"], "prev")})
    assert status == 400  # merge_target 需与 merge 标签同现
    status, _h, _b = env.put_answers({
        keys[0]: _reroll_answer(["merge"], "V76.1.1.1"),
    })
    assert status == 400  # merge_target 不得指向第 76 卷或未知键
    status, _h, _b = env.put_answers({
        keys[0]: _reroll_answer(["merge"], "next"),
    })
    assert status == 200


# ---------------------------------------------------------------------------
# 回归：对抗性探针发现的问题（2026-11-05）
# ---------------------------------------------------------------------------


def test_unknown_keys_are_reported_not_stored(env):
    status, _h, body = env.put_answers(
        {"V76.1.1.1": answer_payload("ok"), "garbage": answer_payload("ok")}
    )
    assert status == 200
    result = error_of(body)
    assert result["ignored"] == 2 and result["count"] == 0
    assert env.answers() == {}


def test_only_flagged_denominator_matches_visible(env):
    status, _h, _b = env.call("POST", "/api/config", {"config": {"only_flagged": True}})
    assert status == 200
    effective = env.json("/api/manifest")["scope"]["effective"]
    visible = 0
    for vol in range(1, 76):
        visible += len(env.json("/api/units?vol=%d" % vol)["units"])
    assert effective == visible and effective > 0


def test_scope_intersects_vol_range(env):
    first_key = env.json("/api/units?vol=1")["units"][0]["key"]
    status, _h, _b = env.call("POST", "/api/config", {"config": {"vol_start": 2, "vol_end": 75}})
    assert status == 200
    status, _h, _b = env.call("POST", "/api/scope", {"unit_keys": [first_key]})
    assert status == 200
    assert env.json("/api/manifest")["scope"]["effective"] == 0
    assert env.json("/api/units?vol=1")["units"] == []


def test_corrupt_answers_recovers_from_snapshot(env):
    key = "V01.1.1.1"
    status, _h, _b = env.put_answers({key: answer_payload("ok")})
    assert status == 200
    answers_path = env.data_dir / "answers" / "answers.json"
    assert answers_path.exists()
    answers_path.write_bytes(b'{"answers": {"V01.1.1.1": {"verdict": "ok"')
    env.restart()
    assert env.json("/api/answers")["count"] == 1
    assert env.answer(key)["verdict"] == "ok"


def test_path_traversal_blocked(env):
    parsed = urllib.parse.urlsplit(env.base)
    for path in ("/../README.md", "/..%2f..%2fREADME.md", "/%2e%2e/%2e%2e/README.md"):
        sock = socket.create_connection((parsed.hostname, parsed.port), 5)
        try:
            sock.sendall(
                ("GET %s HTTP/1.1\r\nHost: 127.0.0.1\r\nConnection: close\r\n\r\n" % path).encode("latin-1")
            )
            raw = b""
            while True:
                chunk = sock.recv(65536)
                if not chunk:
                    break
                raw += chunk
        finally:
            sock.close()
        head = raw.split(b"\r\n", 1)[0]
        assert b"200" not in head, (path, head)
        assert "3B 逐卷人工审定工具".encode("utf-8") not in raw


# ---------------------------------------------------------------------------
# 导入导出：格式与内容保真（转义、合并语义、行序、动作映射）
# ---------------------------------------------------------------------------


def _payload(verdict="ok", title="", note="", tags=None, target="", ts="2026-11-05T10:00:00Z"):
    return {
        "verdict": verdict,
        "custom_title": title,
        "note": note,
        "tags": tags or [],
        "merge_target": target,
        "updated_at": ts,
    }


def test_export_tsv_escapes_and_json_preserves(env):
    keys = expected_model()[2][1]
    tricky = "题名 “引号” ‘单’ 🚀"
    note = "第一行\t制表\n第二行,逗号"
    status, _h, _b = env.put_answers({keys[0]: _payload("custom", tricky, note)})
    assert status == 200
    saved = env.json("/api/answers")["answers"][keys[0]]
    assert saved["custom_title"] == tricky and saved["note"] == note
    status, _h, body = env.call("GET", "/api/export?fmt=tsv")
    lines = body.decode("utf-8").splitlines()
    row = [ln for ln in lines[1:] if ln.startswith(keys[0])][0].split("\t")
    assert len(row) == 10
    assert row[7] == tricky
    assert row[8] == "第一行 制表 第二行,逗号"
    assert len(lines) == 2
    status, _h, body = env.call("GET", "/api/export?fmt=rewrite")
    rw = [ln for ln in body.decode("utf-8").splitlines()[1:] if ln.startswith(keys[0])][0].split("\t")
    assert len(rw) == 13
    assert rw[7] == tricky and rw[10] == "第一行 制表 第二行,逗号"


def test_import_merge_semantics(env):
    keys = expected_model()[2][1]
    env.put_answers({
        keys[0]: _payload("ok", ts="2026-11-05T10:00:00Z"),
        keys[1]: _payload("ok", ts="2026-11-05T10:00:00Z"),
    })
    status, _h, _b = env.call("POST", "/api/import", {"answers": {
        keys[0]: _payload("custom", "旧值", ts="2026-11-05T09:00:00Z")}})
    assert status == 200 and env.answer(keys[0])["verdict"] == "ok"
    status, _h, _b = env.call("POST", "/api/import", {"answers": {
        keys[0]: _payload("custom", "新值", ts="2026-11-05T11:00:00Z")}})
    assert status == 200 and env.answer(keys[0])["custom_title"] == "新值"
    assert env.json("/api/answers")["count"] == 2
    status, _h, body = env.call("POST", "/api/import", {"answers": {
        "V76.1.1.1": _payload(), "no-such-key": _payload()}})
    result = json.loads(body)
    assert status == 200 and result["ignored"] == 2
    assert env.json("/api/answers")["count"] == 2


def test_export_rows_follow_outline_order(env):
    units = env.json("/api/units?vol=1")["units"]
    subs = [u["key"] for u in units if u["level"] == "subsection"]
    first, second = subs[0], subs[3]
    env.put_answers({second: _payload(), first: _payload()})
    status, _h, body = env.call("GET", "/api/export?fmt=tsv")
    rows = [ln.split("\t")[0] for ln in body.decode("utf-8").splitlines()[1:]]
    assert rows == [first, second], rows


def test_rewrite_actions_and_empty_new_title(env):
    keys = expected_model()[2][1]
    env.put_answers({
        keys[0]: _payload("ok"),
        keys[1]: _payload("reroll", tags=["content", "length"], ts="2026-11-05T10:00:01Z"),
        keys[2]: _payload("custom", "改题", ts="2026-11-05T10:00:02Z"),
    })
    status, _h, body = env.call("GET", "/api/export?fmt=rewrite")
    rows = {ln.split("\t")[0]: ln.split("\t") for ln in body.decode("utf-8").splitlines()[1:]}
    assert keys[0] not in rows
    assert rows[keys[1]][6] == "重拟待办" and rows[keys[1]][7] == ""
    assert rows[keys[1]][8] == "content+length"
    assert rows[keys[2]][6] == "改题" and rows[keys[2]][7] == "改题"
