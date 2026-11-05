# -*- coding: utf-8 -*-
"""暂存（staging）与续点（resume）端到端测试：离线队列跨刷新、断点恢复、导出格式与导入回灌。

默认无头；设置 E2E_HEADED=1 以有头方式观看。退出码非零即失败。
"""
import json
import os
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

from playwright.sync_api import sync_playwright

TOOL = Path(__file__).resolve().parents[1]
TMP = Path(tempfile.mkdtemp(prefix="3b-stage-"))
DATA = TMP / "data"
LS_KEY = "3b_review_v1"
results = []
HEADED = os.environ.get("E2E_HEADED") == "1"


def free_port():
    sock = socket.socket()
    sock.bind(("127.0.0.1", 0))
    port = sock.getsockname()[1]
    sock.close()
    return port


PORT = free_port()
BASE = "http://127.0.0.1:%d" % PORT


def api(path, method="GET", body=None, timeout=20):
    data = json.dumps(body, ensure_ascii=False).encode("utf-8") if body is not None else None
    req = urllib.request.Request(BASE + path, data=data, method=method,
                                 headers={"Content-Type": "application/json"} if data else {})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read())


def start():
    proc = subprocess.Popen([sys.executable, str(TOOL / "serve_3b_review.py"), "--port", str(PORT),
                             "--data-dir", str(DATA)],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(120):
        try:
            api("/api/health", timeout=2)
            return proc
        except Exception:
            if proc.poll() is not None:
                raise SystemExit("服务启动即退出")
            time.sleep(0.5)
    raise SystemExit("服务启动超时")


def stop(proc):
    if not proc:
        return
    proc.terminate()
    try:
        proc.wait(timeout=10)
    except Exception:
        proc.kill()


def step(name, cond, extra=""):
    results.append((name, bool(cond), extra))
    print(("PASS " if cond else "FAIL ") + name + ((" | " + extra) if extra else ""))


def wait_until(fn, timeout=40):
    end = time.time() + timeout
    while time.time() < end:
        try:
            if fn():
                return True
        except Exception:
            pass
        time.sleep(0.3)
    return False


def wait_count(n):
    return wait_until(lambda: api("/api/answers")["count"] == n)


def enter(page):
    page.goto(BASE + "/", wait_until="load")
    if page.is_visible("#start-overlay"):
        page.click("#btn-start-plain")
    page.wait_for_selector("article.card")


def local_state(page):
    return page.evaluate("JSON.parse(localStorage.getItem('%s') || '{}')" % LS_KEY)


def dirty_n(page):
    if not page.is_visible("#p-dirty"):
        return 0
    found = re.search(r"(\d+)", page.inner_text("#p-dirty"))
    return int(found.group(1)) if found else 0


def close_sheet(page):
    if page.is_visible("#sheet-backdrop"):
        page.click("#sheet-close")
        page.wait_for_timeout(200)


srv = start()
try:
    units = api("/api/units?vol=1")["units"]
    subs = [u["key"] for u in units if u["level"] == "subsection"]
    k = subs[:7]
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=not HEADED, slow_mo=40 if HEADED else 0)
        page = browser.new_page(viewport={"width": 393, "height": 873}, device_scale_factor=2.75)
        enter(page)
        ready = wait_until(
            lambda: page.evaluate("!!navigator.serviceWorker.controller"), timeout=25
        )
        step("Service Worker 接管页面（离线整页前提）", ready)
        wait_until(
            lambda: page.evaluate("caches.keys().then(function(k){return k.length>0;})"), timeout=25
        )

        # 1 在线作答 3 条
        page.click('.card[data-key="%s"] button.pill[data-v="ok"]' % k[0])
        page.click('.card[data-key="%s"] button.pill[data-v="reroll"]' % k[1])
        page.wait_for_selector('.card[data-key="%s"] .chip[data-tag="term"]' % k[1])
        page.click('.card[data-key="%s"] .chip[data-tag="term"]' % k[1])
        page.click('.card[data-key="%s"] [data-act="tag-save"]' % k[1])
        page.click('.card[data-key="%s"] button.pill[data-v="custom"]' % k[2])
        page.fill('.card[data-key="%s"] .ct-input' % k[2], "暂存测试改题")
        page.click('.card[data-key="%s"] [data-act="note-toggle"]' % k[2])
        page.fill('.card[data-key="%s"] .note-input' % k[2], "含逗号,与“引号”")
        page.click('.card[data-key="%s"] [data-act="custom-save"]' % k[2])
        ok = wait_count(3)
        step("在线作答 3 条已入服务端", ok, str(api("/api/answers")["count"]))
        ls = local_state(page)
        step("localStorage 暂存 3 条", len(ls.get("answers") or {}) == 3, str(len(ls.get("answers") or {})))
        step("暂存含游标卷号", (ls.get("cursor") or {}).get("vol") == 1, str((ls.get("cursor") or {}).get("vol")))

        # 2 停服 → 离线答 2 条 → 刷新 → 队列跨刷新保留
        stop(srv)
        page.wait_for_timeout(800)
        page.click('.card[data-key="%s"] button.pill[data-v="ok"]' % k[3])
        page.click('.card[data-key="%s"] button.pill[data-v="reroll"]' % k[4])
        page.wait_for_timeout(1200)
        step("离线作答后进度 5 / 未同步 ≥2", page.inner_text("#p-answered") == "5"
             and dirty_n(page) >= 2,
             "%s / %s" % (page.inner_text("#p-answered"), page.inner_text("#p-dirty")))
        page.reload(wait_until="load")
        if page.is_visible("#start-overlay"):
            page.click("#btn-start-plain")
        try:
            page.wait_for_selector("article.card", timeout=30000)
        except Exception:
            print("OFFLINE-RELOAD-DIAG url=", page.url)
            try:
                print("OFFLINE-RELOAD-DIAG body=", page.inner_text("body")[:400].replace("\n", " / "))
            except Exception:
                pass
            page.screenshot(path=str(Path(r"d:\librebsd\script\_e2e_3b_shots") / "15-offline-reload-fail.png"))
            raise
        page.wait_for_timeout(800)
        step("离线刷新后暂存不丢（5 条 / 未同步 ≥2）", page.inner_text("#p-answered") == "5"
             and dirty_n(page) >= 2,
             "%s / %s" % (page.inner_text("#p-answered"), page.inner_text("#p-dirty")))
        page.screenshot(path=str(Path(r"d:\librebsd\script\_e2e_3b_shots") / "12-stage-offline.png"))

        # 3 离线再加 1 条 → 起服 → 自动同步
        page.click('.card[data-key="%s"] button.pill[data-v="ok"]' % k[5])
        page.wait_for_timeout(600)
        step("离线累计未同步 ≥3", dirty_n(page) >= 3, page.inner_text("#p-dirty"))
        srv = start()
        synced = wait_until(lambda: api("/api/answers")["count"] == 6, timeout=60)
        step("起服后离线队列全部落库 6 条", synced, str(api("/api/answers")["count"]))
        step("未同步提示清零", not page.is_visible("#p-dirty"))
        server = api("/api/answers")["answers"]
        step("离线 3 条内容与判定一致",
             server[k[3]]["verdict"] == "ok" and server[k[4]]["verdict"] == "reroll"
             and server[k[5]]["verdict"] == "ok")

        # 4 续点：跳到第 7 卷作答，刷新后回到 V07，再点“继续上次”
        page.click("#btn-goto")
        page.select_option("#goto-vol", "7")
        page.click("#goto-go")
        page.wait_for_timeout(500)
        v7_units = api("/api/units?vol=7")["units"]
        v7_sub = [u["key"] for u in v7_units if u["level"] == "subsection"][0]
        page.click('.card[data-key="%s"] button.pill[data-v="ok"]' % v7_sub)
        ok7 = wait_count(7)
        step("V07 作答并落库 7 条", ok7, str(api("/api/answers")["count"]))
        cursor = (local_state(page).get("cursor") or {})
        step("游标记录 V07", cursor.get("vol") == 7, str(cursor.get("vol")))
        page.reload(wait_until="load")
        if page.is_visible("#start-overlay"):
            page.click("#btn-start-plain")
        page.wait_for_selector("article.card")
        page.wait_for_timeout(600)
        first_key = page.locator("#view-group article.card").first.get_attribute("data-key")
        step("刷新后续点回到 V07", first_key.startswith("V07"), first_key)
        page.click("#btn-resume")
        page.wait_for_timeout(400)
        step("“继续上次”停留在 V07",
             page.locator("#view-group article.card").first.get_attribute("data-key").startswith("V07"))
        page.screenshot(path=str(Path(r"d:\librebsd\script\_e2e_3b_shots") / "13-resume.png"))

        # 5 导出格式与内容
        close_sheet(page)
        page.click("#btn-export")
        with page.expect_download() as d1:
            page.click("#exp-json")
        js_path = d1.value.path()
        exported = json.loads(Path(js_path).read_text(encoding="utf-8"))
        server = api("/api/answers")["answers"]
        step("JSON 元信息 answered=7", exported["meta"]["answered"] == 7, str(exported["meta"]["answered"]))
        step("JSON 轮次统计与库一致",
             exported["meta"]["counts"] == {"ok": 4, "reroll": 2, "custom": 1},
             str(exported["meta"]["counts"]))
        same = all(exported["answers"][key] == server[key] for key in exported["answers"])
        step("JSON 逐条全字段一致（含 tags/merge_target/note）", same)
        step("JSON 带 source_hash", bool(exported["meta"].get("source_hash")))

        close_sheet(page)
        page.click("#btn-export")
        with page.expect_download() as d2:
            page.click("#exp-tsv")
        tsv = Path(d2.value.path()).read_text(encoding="utf-8").splitlines()
        step("TSV 行数 8（表头+7）", len(tsv) == 8, str(len(tsv)))
        step("TSV 表头 10 列且顺序固定",
             tsv[0].split("\t") == ["unit_key", "level", "vol", "chapter_no", "section_no",
                                    "title", "verdict", "custom_title", "note", "updated_at"],
             tsv[0])
        tsv_custom = [ln.split("\t") for ln in tsv[1:] if ln.startswith(k[2])][0]
        step("TSV 内容保真（含逗号与弯引号）",
             tsv_custom[7] == "暂存测试改题" and tsv_custom[8] == "含逗号,与“引号”",
             "%s / %s" % (tsv_custom[7], tsv_custom[8]))

        close_sheet(page)
        page.click("#btn-export")
        with page.expect_download() as d3:
            page.click("#exp-rw")
        rw = Path(d3.value.path()).read_text(encoding="utf-8").splitlines()
        step("回写清单行数＝重拟2+改题1+表头", len(rw) == 4, str(len(rw)))
        step("回写清单 13 列", all(len(ln.split("\t")) == 13 for ln in rw))
        rw_map = {ln.split("\t")[0]: ln.split("\t") for ln in rw[1:]}
        step("重拟行 new_title 为空且 tags 保留",
             rw_map[k[1]][7] == "" and "term" in rw_map[k[1]][8], rw_map[k[1]][8])

        # 6 全损：删答案与快照、清 localStorage → 归零
        stop(srv)
        for patch in [DATA / "answers" / "answers.json"]:
            if patch.exists():
                patch.unlink()
        snap = DATA / "answers" / "snapshots"
        if snap.exists():
            for f in snap.iterdir():
                f.unlink()
        srv = start()
        step("清库后服务端归零", api("/api/answers")["count"] == 0)
        page.evaluate("localStorage.clear()")
        page.reload(wait_until="load")
        if page.is_visible("#start-overlay"):
            page.click("#btn-start-plain")
        page.wait_for_selector("article.card")
        page.wait_for_timeout(600)
        step("清暂存后界面归零", page.inner_text("#p-answered") == "0", page.inner_text("#p-answered"))

        # 7 导入回灌：格式与内容完整还原
        close_sheet(page)
        page.click("#btn-export")
        page.set_input_files("#imp-file", js_path)
        restored = wait_count(7)
        step("导入后服务端恢复 7 条", restored, str(api("/api/answers")["count"]))
        page.wait_for_timeout(1200)
        step("导入后界面进度恢复 7", page.inner_text("#p-answered") == "7", page.inner_text("#p-answered"))
        server = api("/api/answers")["answers"]
        step("导入逐条全字段还原",
             all(server[key] == exported["answers"][key] for key in exported["answers"]))
        page.screenshot(path=str(Path(r"d:\librebsd\script\_e2e_3b_shots") / "14-import.png"))

        # 8 重复导入幂等
        before = api("/api/answers")
        close_sheet(page)
        page.click("#btn-export")
        page.set_input_files("#imp-file", js_path)
        page.wait_for_timeout(1500)
        after = api("/api/answers")
        step("重复导入幂等（条数与时间戳不变）",
             after["count"] == before["count"]
             and all(after["answers"][x]["updated_at"] == before["answers"][x]["updated_at"]
                     for x in after["answers"]))
        browser.close()
finally:
    stop(srv)
    shutil.rmtree(TMP, ignore_errors=True)

bad = [r for r in results if not r[1]]
print("\n===== 暂存／续点／导入导出：%d 项，FAIL %d =====" % (len(results), len(bad)))
for name, _, extra in bad:
    print("  FAIL", name, extra)
sys.exit(1 if bad else 0)
