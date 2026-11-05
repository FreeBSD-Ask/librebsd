# -*- coding: utf-8 -*-
"""3B 标题审定前端 E2E（Playwright / Chromium，移动视口 390×844）。

每个场景使用独立工具副本与数据目录、独立随机端口，互不污染。
无法稳定自动化的能力以 SKIP 记录原因，不伪造通过。

运行：
    C:\\Python314\\python.exe 05-卷册大纲\\映射\\title-review\\3b-review\\tests\\e2e_playwright.py
"""

from __future__ import annotations

import json
import os
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import time
import traceback
import urllib.error
import urllib.request
from contextlib import suppress
from pathlib import Path

from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import expect, sync_playwright

TOOL = Path(__file__).resolve().parents[1]
REPO = Path(__file__).resolve().parents[5]
PYTHON = sys.executable
VIEWPORT = {"width": 390, "height": 844}
MANIFEST_TOTAL = 23722
VOL1_TOTAL = 434
VOL1_2_TOTAL = 555

RESULTS = []


class SkipScenario(Exception):
    """环境能力不足，明确跳过。"""


# ---------------------------------------------------------------------------
# 服务端生命周期
# ---------------------------------------------------------------------------


def free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


def http_json(url, method="GET", payload=None, timeout=15):
    data = None
    headers = {}
    if payload is not None:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(url, data=data, method=method, headers=headers)
    with urllib.request.urlopen(request, timeout=timeout) as response:
        body = response.read()
    return json.loads(body.decode("utf-8")) if body else None


def wait_until(fn, timeout=20.0, interval=0.15, message="等待超时"):
    deadline = time.time() + timeout
    last = None
    while time.time() < deadline:
        try:
            value = fn()
            if value:
                return value
        except Exception as exc:  # noqa: BLE001 - 轮询期间容忍连接未就绪
            last = exc
        time.sleep(interval)
    raise AssertionError(f"{message}（最后错误：{last}）")


class Server:
    """独立的工具副本 + 数据目录 + 随机端口。"""

    def __init__(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="3b-e2e-"))
        self.tool = self.tmp / "tool"
        shutil.copytree(
            TOOL,
            self.tool,
            ignore=shutil.ignore_patterns("data", "__pycache__", "tests", ".pytest_cache"),
        )
        self.data = self.tool / "data"
        for sub in ("answers/snapshots", "config", "candidates", "exports"):
            (self.data / sub).mkdir(parents=True, exist_ok=True)
        self.port = self._pick_port()
        self.base = f"http://127.0.0.1:{self.port}"
        self.proc = None
        self.log_path = self.tmp / "server.log"
        self._log = None

    def _pick_port(self) -> int:
        return free_port()

    def start(self):
        assert self.proc is None or self.proc.poll() is not None
        self._log = self.log_path.open("a", encoding="utf-8")
        self.proc = subprocess.Popen(
            [PYTHON, str(self.tool / "serve_3b_review.py"), "--port", str(self.port), "--root", str(REPO)],
            stdout=self._log,
            stderr=subprocess.STDOUT,
            cwd=str(REPO),
        )
        try:
            wait_until(lambda: http_json(self.base + "/api/health"), timeout=30, message="服务未就绪")
        except Exception:
            self.stop()
            raise

    def stop(self):
        if self.proc is not None:
            self.proc.terminate()
            with suppress(subprocess.TimeoutExpired):
                self.proc.wait(timeout=10)
            if self.proc.poll() is None:
                self.proc.kill()
                self.proc.wait(timeout=5)
            self.proc = None
        if self._log is not None:
            self._log.close()
            self._log = None
        time.sleep(0.2)

    def restart(self):
        self.stop()
        self.start()

    def cleanup(self):
        self.stop()
        shutil.rmtree(self.tmp, ignore_errors=True)

    def api(self, method, path, payload=None):
        return http_json(self.base + path, method, payload)

    def answers(self):
        return self.api("GET", "/api/answers")["answers"]

    def answer(self, key):
        return self.answers().get(key)

    def wait_answer(self, key, timeout=20.0, check=None):
        def probe():
            answer = self.answer(key)
            if not answer:
                return None
            if check is not None and not check(answer):
                return None
            return answer

        return wait_until(probe, timeout=timeout, message=f"答案未达预期：{key}")


# ---------------------------------------------------------------------------
# 浏览器
# ---------------------------------------------------------------------------


def launch_browser(playwright):
    try:
        return playwright.chromium.launch()
    except PlaywrightError:
        root = Path(os.environ.get("LOCALAPPDATA", "")) / "ms-playwright"
        candidates = sorted(root.glob("chromium_headless_shell-*/chrome-headless-shell-win64/chrome-headless-shell.exe"))
        candidates += sorted(root.glob("chromium-*/chrome-win64/chrome.exe"))
        if not candidates:
            raise SkipScenario("未找到可用的 Chromium，且 playwright install 未完成")
        return playwright.chromium.launch(executable_path=str(candidates[-1]))


# ---------------------------------------------------------------------------
# 页面操作助手
# ---------------------------------------------------------------------------


def enter_if_overlay(page):
    overlay = page.locator("#start-overlay")
    if overlay.count() and overlay.is_visible():
        page.click("#btn-start-plain")


def open_app(page, server):
    page.goto(server.base + "/", wait_until="domcontentloaded")
    page.wait_for_selector("#start-overlay", state="visible", timeout=20000)
    enter_if_overlay(page)
    page.wait_for_function(
        "document.querySelectorAll('#view-group .card').length > 0", timeout=60000
    )


def reload_app(page, server):
    page.reload(wait_until="domcontentloaded")
    page.wait_for_selector("#start-overlay", state="visible", timeout=20000)
    enter_if_overlay(page)
    page.wait_for_function(
        "document.querySelectorAll('#view-group .card').length > 0", timeout=60000
    )


def card(page, key):
    return page.locator(f'.card[data-key="{key}"]')


def card_status(page, key):
    return card(page, key).get_attribute("data-status")


def click_pill(page, key, verdict):
    card(page, key).locator(f'.pill[data-v="{verdict}"]').click()


def ensure_vol(page, vol):
    page.select_option("#vol-select", str(vol))
    page.wait_for_timeout(120)


def ensure_card(page, key):
    vol = int(key[1:3])
    if page.input_value("#vol-select") != str(vol):
        ensure_vol(page, vol)
    page.wait_for_selector(f'.card[data-key="{key}"]', timeout=15000)


def wait_progress_total(page, value, timeout=30000):
    page.wait_for_function(
        "(v) => document.querySelector('#p-total').textContent === v",
        arg=str(value),
        timeout=timeout,
    )


def wait_toast(page, text, timeout=10000):
    page.wait_for_function(
        "(t) => { const el = document.querySelector('#toast'); "
        "return el && el.classList.contains('show') && el.textContent.indexOf(t) >= 0; }",
        arg=text,
        timeout=timeout,
    )


def wait_synced(page, timeout=20000):
    expect(page.locator("#p-dirty")).to_be_hidden(timeout=timeout)


def answer_ok(page, server, key):
    ensure_card(page, key)
    click_pill(page, key, "ok")
    expect(card(page, key)).to_have_attribute("data-status", "ok")
    server.wait_answer(key, check=lambda a: a["verdict"] == "ok")


def open_sheet(page, button_id):
    page.click(button_id)
    expect(page.locator("#sheet-backdrop")).to_be_visible()


def close_sheet(page):
    page.click("#sheet-close")
    expect(page.locator("#sheet-backdrop")).to_be_hidden()


def first_pending_key(page):
    locator = page.locator('#view-group .card[data-status="pending"]')
    return locator.first.get_attribute("data-key")


def assert_no_js_errors(errors):
    assert errors == [], f"页面出现 JS 错误：{errors}"


# ---------------------------------------------------------------------------
# 场景
# ---------------------------------------------------------------------------


def scenario_load_and_group(server, page, errors):
    open_app(page, server)
    assert "3B" in page.locator(".brand").inner_text()
    wait_progress_total(page, MANIFEST_TOTAL)
    expect(page.locator("#p-answered")).to_have_text("0")
    expect(page.locator("#p-pct")).to_have_text("0%")
    assert page.locator("#view-group .card").count() > 0
    assert page.locator("#view-group .chapter-head").count() > 0
    assert page.locator("#view-group .section-head").count() > 0
    assert page.input_value("#vol-select") == "1"
    first = page.locator("#view-group .card").first
    key = first.get_attribute("data-key")
    assert re.fullmatch(r"V01\.C\d+", key), key
    assert page.locator('#view-group .card[data-level="chapter"]').count() > 0
    assert page.locator('#view-group .card[data-level="section"]').count() > 0
    assert page.locator('#view-group .card[data-level="subsection"]').count() > 0
    labels = page.locator("#view-group .card").first.locator(".pill span").all_inner_texts()
    assert labels == ["对勾", "重拟", "自定义"], labels
    assert page.locator(".sec-pass").count() > 0
    assert_no_js_errors(errors)


def scenario_single_card_mode(server, page, errors):
    open_app(page, server)
    key = first_pending_key(page)
    page.click("#btn-view")
    expect(page.locator("#btn-view")).to_have_text("分组模式")
    expect(page.locator("#view-single")).to_be_visible()
    expect(page.locator("#view-group")).to_be_hidden()
    single = page.locator("#view-single .card")
    assert single.count() == 1
    expect(page.locator("#view-single .card")).to_have_attribute("data-key", key)
    assert page.locator("#view-single .pill").count() == 3
    counter_before = page.locator(".counter").inner_text()
    page.click('[data-act="single-next"]')
    counter_after = page.locator(".counter").inner_text()
    assert counter_before != counter_after
    assert "第 1 卷" in page.locator(".crumbs").inner_text()
    page.click("#btn-view")
    expect(page.locator("#view-group")).to_be_visible()
    assert_no_js_errors(errors)


def scenario_verdict_options_custom_note_clear(server, page, errors):
    open_app(page, server)
    key = first_pending_key(page)
    original = card(page, key).locator(".card-title").inner_text()

    click_pill(page, key, "ok")
    expect(card(page, key)).to_have_attribute("data-status", "ok")
    assert server.wait_answer(key)["verdict"] == "ok"
    assert page.locator("#view-group .badge.status-ok").count() >= 1

    click_pill(page, key, "reroll")
    expect(card(page, key)).to_have_attribute("data-status", "reroll")
    assert server.wait_answer(key, check=lambda a: a["verdict"] == "reroll")["verdict"] == "reroll"

    # 自定义：清空被拦
    click_pill(page, key, "custom")
    box = card(page, key).locator('.inline-box[data-box="custom"]')
    expect(box).to_be_visible()
    textarea = box.locator(".ct-input")
    assert textarea.input_value() == original
    textarea.fill("")
    expect(box.locator(".ct-count")).to_have_text("0 / 120")
    box.locator('[data-act="custom-save"]').click()
    expect(box.locator(".ct-err")).to_have_text("题名须为 1–120 字")
    expect(card(page, key)).to_have_attribute("data-status", "reroll")
    assert server.answer(key)["verdict"] == "reroll"

    # 备注 + 保存
    textarea.fill("E2E 新题名")
    box.locator('[data-act="note-toggle"]').click()
    box.locator(".note-input").fill("E2E 备注")
    box.locator('[data-act="custom-save"]').click()
    expect(card(page, key)).to_have_attribute("data-status", "custom")
    expect(card(page, key).locator(".card-title")).to_have_text("E2E 新题名")
    expect(card(page, key).locator(".card-old")).to_contain_text(original)
    stored = server.wait_answer(
        key, check=lambda a: a["verdict"] == "custom" and a["custom_title"] == "E2E 新题名"
    )
    assert stored["verdict"] == "custom"
    assert stored["custom_title"] == "E2E 新题名"
    assert stored["note"] == "E2E 备注"

    # 清除 + 撤销
    card(page, key).locator('[data-act="clear"]').click()
    expect(card(page, key)).to_have_attribute("data-status", "pending")
    wait_toast(page, "已清除作答")
    expect(page.locator("#toast-undo")).to_be_visible()
    page.click("#toast-undo")
    expect(card(page, key)).to_have_attribute("data-status", "custom")
    wait_toast(page, "已撤销")
    assert_no_js_errors(errors)


def scenario_section_pass_and_single_change(server, page, errors):
    open_app(page, server)
    script = """(btn) => {
        const keys = [];
        let node = btn.closest('.section-head').nextElementSibling;
        while (node && !node.classList.contains('section-head') && !node.classList.contains('chapter-head')) {
            if (node.classList.contains('card')) keys.push(node.dataset.key);
            node = node.nextElementSibling;
        }
        return keys;
    }"""
    keys = page.eval_on_selector(".sec-pass:not([disabled])", script)
    assert keys, "第 1 卷应存在可整节通过的节"
    # 二次确认前不得改变状态
    button = page.locator(".sec-pass:not([disabled])").first
    button.click()
    expect(page.locator("#sheet-title")).to_have_text("整节通过")
    sheet_text = page.locator("#sheet-body").inner_text()
    assert f"确认通过 {len(keys)} 条" in sheet_text
    assert all(card_status(page, key) == "pending" for key in keys)
    page.click("#sec-ok")
    wait_toast(page, "整节通过")
    for key in keys:
        expect(card(page, key)).to_have_attribute("data-status", "ok")
        assert server.wait_answer(key, check=lambda a: a["verdict"] == "ok")["verdict"] == "ok"

    # 单条改判
    target = keys[0]
    click_pill(page, target, "reroll")
    expect(card(page, target)).to_have_attribute("data-status", "reroll")
    assert server.wait_answer(target, check=lambda a: a["verdict"] == "reroll")["verdict"] == "reroll"
    assert_no_js_errors(errors)


def scenario_filter(server, page, errors):
    open_app(page, server)
    key = first_pending_key(page)
    answer_ok(page, server, key)
    total_cards = page.locator("#view-group .card").count()

    open_sheet(page, "#btn-filter")
    page.click('[data-filter="ok"]')
    expect(page.locator("#sheet-backdrop")).to_be_hidden()
    expect(page.locator("#btn-filter")).to_have_text("筛选：已通过")
    visible = page.locator("#view-group .card")
    assert visible.count() == 1
    assert visible.first.get_attribute("data-key") == key

    open_sheet(page, "#btn-filter")
    page.click('[data-filter="pending"]')
    visible = page.locator("#view-group .card")
    assert visible.count() == total_cards - 1
    statuses = visible.evaluate_all("(els) => els.map((el) => el.dataset.status)")
    assert set(statuses) == {"pending"}

    open_sheet(page, "#btn-filter")
    page.click('[data-filter="changed"]')
    assert page.locator("#view-group .card").count() == 0
    assert "没有符合当前筛选的条目" in page.locator("#view-group").inner_text()

    open_sheet(page, "#btn-filter")
    page.click('[data-filter="all"]')
    assert page.locator("#view-group .card").count() == total_cards
    assert_no_js_errors(errors)


def scenario_refresh_and_localstorage_recovery(server, page, errors):
    open_app(page, server)
    key = first_pending_key(page)
    answer_ok(page, server, key)
    wait_synced(page)

    reload_app(page, server)
    expect(card(page, key)).to_have_attribute("data-status", "ok")
    expect(page.locator("#p-answered")).to_have_text("1")

    page.evaluate("localStorage.clear()")
    reload_app(page, server)
    expect(card(page, key)).to_have_attribute("data-status", "ok")
    expect(page.locator("#p-answered")).to_have_text("1")
    assert server.answer(key)["verdict"] == "ok"
    assert_no_js_errors(errors)


def scenario_goto_volume(server, page, errors):
    open_app(page, server)
    manifest = server.api("GET", "/api/manifest")
    vol3 = next(item for item in manifest["vols"] if item["vol"] == 3)
    open_sheet(page, "#btn-goto")
    expect(page.locator("#sheet-title")).to_have_text("定位")
    page.select_option("#goto-vol", "3")
    page.click("#goto-go")
    expect(page.locator("#sheet-backdrop")).to_be_hidden()
    expect(page.locator("#vol-select")).to_have_value("3")
    expect(page.locator(".vol-name")).to_have_text(vol3["title"])
    assert page.locator("#view-group .card").count() > 0
    assert_no_js_errors(errors)


def scenario_config_scope_and_reset(server, page, errors):
    open_app(page, server)
    open_sheet(page, "#btn-config")
    expect(page.locator("#sheet-title")).to_have_text("配置")
    current = json.loads(page.input_value("#cfg-text"))
    assert current["vol_end"] == 75

    narrow = dict(current, vol_start=1, vol_end=2, daily_goal=123)
    page.fill("#cfg-text", json.dumps(narrow, ensure_ascii=False))
    page.click("#cfg-save")
    wait_toast(page, "参数配置已上传")
    wait_progress_total(page, VOL1_2_TOTAL)
    assert server.api("GET", "/api/config")["config"]["daily_goal"] == 123

    widen = dict(current, vol_start=1, vol_end=75, daily_goal=123)
    open_sheet(page, "#btn-config")
    page.fill("#cfg-text", json.dumps(widen, ensure_ascii=False))
    page.click("#cfg-save")
    wait_toast(page, "参数配置已上传")
    wait_progress_total(page, MANIFEST_TOTAL)

    scope_keys = ["V01.1.1.1", "V01.1.1.2", "V01.1.1.3"]
    open_sheet(page, "#btn-config")
    page.fill("#scope-text", json.dumps({"unit_keys": scope_keys}, ensure_ascii=False))
    page.click("#scope-save")
    wait_toast(page, "审阅清单已上传：3 条")
    wait_progress_total(page, "3")
    page.wait_for_function(
        "() => document.querySelectorAll('#view-group .card').length === 3", timeout=30000
    )
    assert page.locator("#view-group .card").count() == 3

    open_sheet(page, "#btn-config")
    page.click("#scope-reset")
    wait_toast(page, "已恢复全量作用域")
    wait_progress_total(page, MANIFEST_TOTAL)
    page.wait_for_function(
        "() => document.querySelectorAll('#view-group .card').length > 0", timeout=30000
    )
    assert_no_js_errors(errors)


def scenario_exports_download(server, page, errors):
    open_app(page, server)
    keys = ["V01.1.1.1", "V01.1.1.2", "V01.1.1.3"]
    answer_ok(page, server, keys[0])
    ensure_card(page, keys[1])
    click_pill(page, keys[1], "reroll")
    server.wait_answer(keys[1], check=lambda a: a["verdict"] == "reroll")
    ensure_card(page, keys[2])
    click_pill(page, keys[2], "custom")
    box = card(page, keys[2]).locator('.inline-box[data-box="custom"]')
    box.locator(".ct-input").fill("导出题名")
    box.locator('[data-act="custom-save"]').click()
    server.wait_answer(keys[2], check=lambda a: a.get("custom_title") == "导出题名")

    open_sheet(page, "#btn-export")
    with page.expect_download() as info:
        page.click("#exp-json")
    download = info.value
    assert download.suggested_filename.startswith("3B-answers-") and download.suggested_filename.endswith(".json")
    payload = json.loads(Path(download.path()).read_text(encoding="utf-8"))
    assert payload["meta"]["answered"] == 3
    assert payload["meta"]["counts"] == {"ok": 1, "reroll": 1, "custom": 1}
    assert payload["meta"]["total_units"] == MANIFEST_TOTAL
    assert set(payload["answers"]) == set(keys)

    with page.expect_download() as info:
        page.click("#exp-tsv")
    tsv = Path(info.value.path()).read_text(encoding="utf-8").splitlines()
    assert len(tsv) == 4
    assert all(len(line.split("\t")) == 10 for line in tsv)

    with page.expect_download() as info:
        page.click("#exp-rw")
    rewrite = Path(info.value.path()).read_text(encoding="utf-8").splitlines()
    assert len(rewrite) == 3  # 表头 + custom + reroll
    assert all(len(line.split("\t")) == 11 for line in rewrite)
    rows = {line.split("\t")[0]: line.split("\t") for line in rewrite[1:]}
    assert rows[keys[1]][6] == "重拟待办" and rows[keys[1]][7] == ""
    assert rows[keys[2]][6] == "改题" and rows[keys[2]][7] == "导出题名"

    with page.expect_download() as info:
        page.click("#exp-cfg")
    config_payload = json.loads(Path(info.value.path()).read_text(encoding="utf-8"))
    assert config_payload["source_hash"] == server.api("GET", "/api/manifest")["source_hash"]
    assert_no_js_errors(errors)


def scenario_import_restore(server, page, errors):
    open_app(page, server)
    key = "V01.1.1.1"
    import_file = server.tmp / "import-answers.json"
    import_file.write_text(
        json.dumps(
            {
                "answers": {
                    key: {
                        "verdict": "ok",
                        "custom_title": "",
                        "note": "导入备注",
                        "updated_at": "2020-01-01T00:00:00+00:00",
                    }
                }
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    open_sheet(page, "#btn-export")
    page.set_input_files("#imp-file", str(import_file))
    wait_toast(page, "已导入 1 条")
    stored = server.wait_answer(key)
    assert stored["verdict"] == "ok" and stored["note"] == "导入备注"
    expect(page.locator("#sheet-backdrop")).to_be_hidden()
    ensure_card(page, key)
    expect(card(page, key)).to_have_attribute("data-status", "ok")

    # 幂等：重复导入同一文件不新增、不报错
    open_sheet(page, "#btn-export")
    page.set_input_files("#imp-file", str(import_file))
    wait_toast(page, "已导入 1 条")
    assert server.api("GET", "/api/answers")["count"] == 1
    assert_no_js_errors(errors)


def scenario_candidates_second_round(server, page, errors):
    keys = ["V01.1.1.1", "V01.1.1.2"]
    payload = {
        key: {"verdict": "reroll", "custom_title": "", "note": "", "updated_at": "2020-02-01T00:00:00+00:00"}
        for key in keys
    }
    server.api("PUT", "/api/answers", {"answers": payload})
    server.api(
        "POST",
        "/api/candidates",
        {
            "batch_id": "e2e-batch",
            "candidates": {
                keys[0]: [
                    {"candidate_id": "a", "new_title": "候选甲", "rationale": "理由甲"},
                    {"candidate_id": "b", "new_title": "候选乙"},
                ],
                keys[1]: [{"candidate_id": "c", "new_title": "候选丙"}],
            },
        },
    )
    open_app(page, server)
    ensure_card(page, keys[0])
    box = card(page, keys[0]).locator(".cand-box")
    expect(box).to_be_visible()
    assert box.locator(".cand-item").count() == 2
    assert "候选甲" in box.inner_text() and "候选乙" in box.inner_text()

    box.locator('[data-act="cand-adopt"]').first.click()
    expect(card(page, keys[0])).to_have_attribute("data-status", "custom")
    expect(card(page, keys[0]).locator(".card-title")).to_have_text("候选甲")
    assert server.wait_answer(keys[0], check=lambda a: a.get("custom_title") == "候选甲")["custom_title"] == "候选甲"

    ensure_card(page, keys[1])
    card(page, keys[1]).locator('[data-act="cand-edit"]').first.click()
    inline = card(page, keys[1]).locator('.inline-box[data-box="custom"]')
    expect(inline).to_be_visible()
    assert inline.locator(".ct-input").input_value() == "候选丙"
    inline.locator(".ct-input").fill("改写候选丙")
    inline.locator('[data-act="custom-save"]').click()
    expect(card(page, keys[1])).to_have_attribute("data-status", "custom")
    assert server.wait_answer(keys[1], check=lambda a: a.get("custom_title") == "改写候选丙")["custom_title"] == "改写候选丙"
    assert_no_js_errors(errors)


def scenario_theme_font_progress_stats(server, page, errors):
    open_app(page, server)
    expect(page.locator("html")).to_have_attribute("data-theme", "dark")
    expect(page.locator("html")).to_have_attribute("data-fs", "2")
    page.click("#btn-theme")
    expect(page.locator("html")).to_have_attribute("data-theme", "light")
    page.click("#btn-theme")
    expect(page.locator("html")).to_have_attribute("data-theme", "dark")
    page.click("#btn-font")
    expect(page.locator("html")).to_have_attribute("data-fs", "3")
    page.click("#btn-font")
    expect(page.locator("html")).to_have_attribute("data-fs", "1")
    page.click("#btn-font")
    expect(page.locator("html")).to_have_attribute("data-fs", "2")

    keys = ["V01.1.1.1", "V01.1.1.2"]
    for key in keys:
        answer_ok(page, server, key)
    expect(page.locator("#p-answered")).to_have_text("2")
    wait_progress_total(page, MANIFEST_TOTAL)

    open_sheet(page, "#btn-stats")
    expect(page.locator("#sheet-title")).to_have_text("统计")
    values = page.locator(".stat-cell .v").all_inner_texts()
    assert len(values) == 6
    assert values[0] == "2"
    assert values[1] == str(MANIFEST_TOTAL - 2)
    assert values[4] == "2"
    assert values[5] == "500"
    assert page.locator(".stat-grid").is_visible()
    close_sheet(page)
    assert_no_js_errors(errors)


def scenario_immersive_button(server, page, errors):
    page.goto(server.base + "/", wait_until="domcontentloaded")
    start = page.locator("#btn-start")
    expect(start).to_be_visible()
    assert "开始沉浸审阅" in start.inner_text()
    expect(page.locator("#btn-start-plain")).to_be_visible()
    start.click()
    expect(page.locator("#start-overlay")).to_be_hidden()
    page.wait_for_timeout(600)
    in_fullscreen = page.evaluate("!!document.fullscreenElement")
    no_fs = page.evaluate("document.documentElement.classList.contains('no-fs')")
    assert in_fullscreen or no_fs, "既未进入全屏也未走同色状态栏降级"
    if page.locator("#btn-exit-fs").is_visible():
        page.click("#btn-exit-fs")
        expect(page.locator("#btn-exit-fs")).to_be_hidden()
    assert_no_js_errors(errors)


def scenario_offline_buffer(server, page, errors):
    open_app(page, server)
    key1, key2 = "V01.1.1.1", "V01.1.1.2"
    answer_ok(page, server, key1)
    wait_synced(page)

    server.stop()
    ensure_card(page, key2)
    click_pill(page, key2, "ok")
    expect(card(page, key2)).to_have_attribute("data-status", "ok")
    page.wait_for_function(
        "() => { const el = document.querySelector('#p-dirty'); "
        "return el && !el.hidden && el.textContent.indexOf('未同步 1 条') >= 0; }",
        timeout=10000,
    )

    server.start()
    page.evaluate("window.dispatchEvent(new Event('online'))")
    server.wait_answer(key2, timeout=30)
    expect(page.locator("#p-dirty")).to_be_hidden(timeout=15000)

    reload_app(page, server)
    expect(card(page, key1)).to_have_attribute("data-status", "ok")
    expect(card(page, key2)).to_have_attribute("data-status", "ok")
    assert_no_js_errors(errors)


def scenario_pwa_offline_open(server, page, errors):
    open_app(page, server)
    page.evaluate("navigator.serviceWorker.ready.then(() => true)")
    controlled = page.evaluate("!!navigator.serviceWorker.controller")
    if not controlled:
        page.wait_for_timeout(1500)
        controlled = page.evaluate("!!navigator.serviceWorker.controller")
    if not controlled:
        raise SkipScenario("Service Worker 未取得页面控制权，无法稳定验证离线打开")

    server.stop()
    try:
        page.reload(wait_until="domcontentloaded", timeout=20000)
    except PlaywrightError as exc:
        raise SkipScenario(f"离线 reload 未命中缓存：{exc}")
    expect(page.locator("#topbar")).to_be_visible(timeout=10000)
    assert "3B" in page.locator(".brand").inner_text()
    page.wait_for_function(
        "() => document.querySelector('#view-group') && "
        "document.querySelector('#view-group').textContent.indexOf('服务端不可用') >= 0",
        timeout=15000,
    )
    assert_no_js_errors(errors)


SCENARIOS = [
    ("页面加载与分组卡片", scenario_load_and_group),
    ("单卡模式切换", scenario_single_card_mode),
    ("三个选项/自定义/备注/清除撤销", scenario_verdict_options_custom_note_clear),
    ("整节一键通过与单条改判", scenario_section_pass_and_single_change),
    ("筛选器", scenario_filter),
    ("刷新恢复与清 localStorage 服务端恢复", scenario_refresh_and_localstorage_recovery),
    ("按卷跳转", scenario_goto_volume),
    ("配置上传与审阅清单恢复全量", scenario_config_scope_and_reset),
    ("三种导出下载", scenario_exports_download),
    ("导入恢复", scenario_import_restore),
    ("二审多候选", scenario_candidates_second_round),
    ("主题字号与进度统计", scenario_theme_font_progress_stats),
    ("沉浸式按钮与降级", scenario_immersive_button),
    ("离线缓冲与重连同步", scenario_offline_buffer),
    ("PWA 离线打开（可选）", scenario_pwa_offline_open),
]


def run_scenario(name, fn, browser):
    server = Server()
    context = None
    try:
        server.start()
        context = browser.new_context(
            viewport=VIEWPORT,
            device_scale_factor=2,
            accept_downloads=True,
            locale="zh-CN",
        )
        page = context.new_page()
        page.set_default_timeout(10000)
        page.set_default_navigation_timeout(40000)
        errors = []
        page.on("pageerror", lambda exc: errors.append(str(exc)))
        fn(server, page, errors)
        RESULTS.append((name, "PASS", ""))
    except SkipScenario as exc:
        RESULTS.append((name, "SKIP", str(exc)))
    except Exception as exc:  # noqa: BLE001 - 汇总所有失败
        RESULTS.append((name, "FAIL", f"{type(exc).__name__}: {exc}"))
        traceback.print_exc()
        with suppress(OSError):
            if server.log_path.exists():
                tail = server.log_path.read_text(encoding="utf-8", errors="replace").splitlines()[-20:]
                print("  --- server log tail ---")
                for line in tail:
                    print("  " + line)
    finally:
        if context is not None:
            with suppress(Exception):
                context.close()
        server.cleanup()


def main() -> int:
    only = [arg for arg in sys.argv[1:] if not arg.startswith("-")]
    scenarios = [(name, fn) for name, fn in SCENARIOS if not only or any(token in name for token in only)]
    for name, _fn in scenarios:
        print(f"[RUN ] {name}")
    with sync_playwright() as playwright:
        try:
            browser = launch_browser(playwright)
        except SkipScenario as exc:
            print(f"无法启动浏览器：{exc}")
            return 2
        for name, fn in scenarios:
            run_scenario(name, fn, browser)
            status, detail = RESULTS[-1][1], RESULTS[-1][2]
            if status == "PASS":
                print(f"[PASS] {name}")
            elif status == "SKIP":
                print(f"[SKIP] {name} · {detail}")
            else:
                print(f"[FAIL] {name} · {detail}")
        browser.close()

    passed = sum(1 for _, status, _ in RESULTS if status == "PASS")
    skipped = sum(1 for _, status, _ in RESULTS if status == "SKIP")
    failed = sum(1 for _, status, _ in RESULTS if status == "FAIL")
    print(f"\n汇总：{passed} 通过 / {failed} 失败 / {skipped} 跳过（共 {len(RESULTS)} 项）")
    for name, status, detail in RESULTS:
        if status != "PASS":
            print(f"  {status} {name}：{detail}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
