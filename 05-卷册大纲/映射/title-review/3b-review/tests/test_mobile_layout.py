# -*- coding: utf-8 -*-
"""手机适配（2400×1080／6.67 英寸 OLED）布局单元测试。

覆盖：媒体查询方向、底部固定工具栏、触控尺寸、题名字号档位、末条遮挡、
过滚抑制、对勾符号化、浅色主题一致性、PWA manifest 关键字段。
不写入任何答案；启动的服务在收尾时停掉，并清理运行期新建文件。
"""
import json
import os
import socket
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright

TOOL = Path(__file__).resolve().parents[1]
DATA = TOOL / "data"
CSS = TOOL / "web" / "app.css"
MANIFEST = TOOL / "web" / "manifest.webmanifest"
VIEWPORTS = [(393, 873, 2.75), (412, 915, 2.625), (360, 800, 3)]


def free_port():
    sock = socket.socket()
    sock.bind(("127.0.0.1", 0))
    port = sock.getsockname()[1]
    sock.close()
    return port


@pytest.fixture(scope="module")
def server():
    pre = {str(p) for p in DATA.rglob("*") if p.is_file()} if DATA.exists() else set()
    port = free_port()
    proc = subprocess.Popen(
        [sys.executable, str(TOOL / "serve_3b_review.py"), "--port", str(port)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    base = "http://127.0.0.1:%d" % port
    for _ in range(120):
        try:
            urllib.request.urlopen(base + "/api/health", timeout=2)
            break
        except Exception:
            if proc.poll() is not None:
                pytest.fail("服务启动即退出")
            time.sleep(0.5)
    else:
        proc.kill()
        pytest.fail("服务启动超时")
    yield base
    proc.terminate()
    try:
        proc.wait(timeout=10)
    except Exception:
        proc.kill()
    for path in sorted(DATA.rglob("*"), reverse=True):
        if path.is_file() and str(path) not in pre:
            path.unlink()
        elif path.is_dir() and path != DATA:
            try:
                path.rmdir()
            except OSError:
                pass


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as pw:
        instance = pw.chromium.launch()
        yield instance
        instance.close()


def open_page(browser, base, width, height, dpr):
    context = browser.new_context(viewport={"width": width, "height": height}, device_scale_factor=dpr)
    page = context.new_page()
    page.goto(base + "/")
    if page.is_visible("#start-overlay"):
        page.click("#btn-start-plain")
    page.wait_for_selector("article.card")
    return context, page


# ---------------------------------------------------------------------------
# 静态：适配逻辑本身（不依赖浏览器，防止断点方向写反）
# ---------------------------------------------------------------------------


def test_media_query_uses_portrait_aspect():
    css = CSS.read_text(encoding="utf-8")
    assert "max-aspect-ratio: 1/2" in css
    assert "min-aspect-ratio: 2/1" not in css


def test_css_has_safe_area_and_overscroll():
    css = CSS.read_text(encoding="utf-8")
    assert "env(safe-area-inset-bottom" in css
    assert "overscroll-behavior-y: none" in css
    assert "position: fixed" in css
    assert "color-mix(in srgb, var(--bg) 94%, transparent)" in css


def test_manifest_phone_fields():
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert data["orientation"] == "portrait"
    assert data["background_color"] == "#000000"
    assert data["theme_color"] == "#000000"
    assert data["display_override"][0] == "fullscreen"


# ---------------------------------------------------------------------------
# 浏览器：三档目标视口
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("width,height,dpr", VIEWPORTS)
def test_no_horizontal_overflow(browser, server, width, height, dpr):
    context, page = open_page(browser, server, width, height, dpr)
    try:
        overflow = page.evaluate("document.documentElement.scrollWidth - window.innerWidth")
        assert overflow <= 0, overflow
    finally:
        context.close()


@pytest.mark.parametrize("width,height,dpr", VIEWPORTS)
def test_toolbar_fixed_to_bottom(browser, server, width, height, dpr):
    context, page = open_page(browser, server, width, height, dpr)
    try:
        assert page.evaluate("getComputedStyle(document.querySelector('.toolbar')).position") == "fixed"
        box = page.locator(".toolbar").bounding_box()
        assert abs((box["y"] + box["height"]) - height) <= 2, (box, height)
        body_pad = page.evaluate(
            "parseFloat(getComputedStyle(document.body).paddingBottom)"
        )
        assert body_pad >= 72, body_pad
    finally:
        context.close()


@pytest.mark.parametrize("width,height,dpr", VIEWPORTS)
def test_touch_targets(browser, server, width, height, dpr):
    context, page = open_page(browser, server, width, height, dpr)
    try:
        toolbar_h = page.locator(".toolbar button").first.bounding_box()["height"]
        assert toolbar_h >= 44, toolbar_h
        pill_h = page.locator('.card .pill[data-v="ok"]').first.bounding_box()["height"]
        assert pill_h >= 44, pill_h
        chip_h = page.evaluate(
            "(() => { const el=document.createElement('button'); el.className='chip';"
            " el.textContent='内容'; document.body.appendChild(el);"
            " const h=el.getBoundingClientRect().height; el.remove(); return h; })()"
        )
        assert chip_h >= 44, chip_h
    finally:
        context.close()


@pytest.mark.parametrize("width,height,dpr", VIEWPORTS)
def test_title_font_size_tiers(browser, server, width, height, dpr):
    context, page = open_page(browser, server, width, height, dpr)
    try:
        size = page.evaluate(
            "getComputedStyle(document.querySelector('.card[data-level=\"subsection\"] .card-title')).fontSize"
        )
        assert size == ("21px" if width >= 380 else "20px"), size
    finally:
        context.close()


@pytest.mark.parametrize("width,height,dpr", VIEWPORTS)
def test_last_card_not_covered_by_toolbar(browser, server, width, height, dpr):
    context, page = open_page(browser, server, width, height, dpr)
    try:
        page.locator("#view-group .card").last.scroll_into_view_if_needed()
        page.wait_for_timeout(200)
        bottom = page.evaluate(
            "(() => { const c=document.querySelectorAll('#view-group .card');"
            " const r=c[c.length-1].getBoundingClientRect(); return r.bottom; })()"
        )
        toolbar_top = page.locator(".toolbar").bounding_box()["y"]
        assert bottom <= toolbar_top + 1, (bottom, toolbar_top)
    finally:
        context.close()


@pytest.mark.parametrize("width,height,dpr", VIEWPORTS)
def test_ok_pill_is_symbol_only(browser, server, width, height, dpr):
    context, page = open_page(browser, server, width, height, dpr)
    try:
        pill = page.locator('.card .pill[data-v="ok"]').first
        assert pill.inner_text().strip() == ""
        assert pill.locator("svg").count() == 1
        assert pill.get_attribute("aria-label") == "通过（维持原题）"
        assert "对勾" not in page.locator("#view-group .card").first.inner_text()
    finally:
        context.close()


def test_overscroll_disabled(browser, server):
    width, height, dpr = VIEWPORTS[0]
    context, page = open_page(browser, server, width, height, dpr)
    try:
        assert page.evaluate("getComputedStyle(document.documentElement).overscrollBehaviorY") == "none"
        assert page.evaluate("getComputedStyle(document.body).overscrollBehaviorY") == "none"
    finally:
        context.close()


def test_light_theme_keeps_bottom_toolbar(browser, server):
    width, height, dpr = VIEWPORTS[0]
    context, page = open_page(browser, server, width, height, dpr)
    try:
        page.click("#btn-theme")
        page.wait_for_timeout(200)
        assert page.evaluate("document.documentElement.dataset.theme") != "dark"
        assert page.evaluate("getComputedStyle(document.querySelector('.toolbar')).position") == "fixed"
        box = page.locator(".toolbar").bounding_box()
        assert abs((box["y"] + box["height"]) - height) <= 2
    finally:
        context.close()


def test_adaptation_scoped_to_phones(browser, server):
    """平板宽度不套用手机规则：工具栏回到文档流、题名维持 20px。"""
    context, page = open_page(browser, server, 600, 960, 2)
    try:
        assert page.evaluate("getComputedStyle(document.querySelector('.toolbar')).position") == "static"
        size = page.evaluate(
            "getComputedStyle(document.querySelector('.card[data-level=\"subsection\"] .card-title')).fontSize"
        )
        assert size == "20px", size
    finally:
        context.close()


def test_hierarchy_colors_and_fold(browser, server):
    """章、节头为绿色且字号递减，小节题名不用绿色；章、节可折叠且可恢复。"""
    width, height, dpr = VIEWPORTS[0]
    context, page = open_page(browser, server, width, height, dpr)
    try:
        info = page.evaluate(
            """() => {
                const cs = (el) => getComputedStyle(el);
                const ch = document.querySelector('.chapter-head .ch-title');
                const sec = document.querySelector('.section-fold .sec-title');
                const sub = document.querySelector('.card[data-level="subsection"] .card-title');
                return {
                    chColor: cs(ch).color,
                    chSize: parseFloat(cs(ch).fontSize),
                    secColor: cs(sec).color,
                    secSize: parseFloat(cs(sec).fontSize),
                    subColor: cs(sub).color
                };
            }"""
        )
        assert info["chColor"] == info["secColor"], info
        assert info["chSize"] > info["secSize"], info
        assert info["subColor"] != info["chColor"], info

        first = page.locator("#view-group .chapter-block").first
        before = first.locator(".card[data-level=subsection]").count()
        assert before > 0
        page.click(".chapter-head")
        page.wait_for_timeout(250)
        assert first.locator(".card[data-level=subsection]").count() == 0
        page.click(".chapter-head")
        page.wait_for_timeout(250)
        assert first.locator(".card[data-level=subsection]").count() == before

        page.click(".section-fold")
        page.wait_for_timeout(250)
        assert first.locator(".card[data-level=subsection]").count() < before
    finally:
        context.close()


def test_all_volumes_filter_and_progress(browser, server):
    """卷下拉含“全部卷”：列出 75 个卷块（默认折叠），卷头显示百分比进度，可展开。"""
    width, height, dpr = VIEWPORTS[0]
    context, page = open_page(browser, server, width, height, dpr)
    try:
        assert page.locator('#vol-select option[value="all"]').count() == 1
        page.select_option("#vol-select", "all")
        page.wait_for_function(
            "document.querySelectorAll('#view-group .vol-block').length === 75", timeout=30000
        )
        assert page.locator("#view-group .card[data-level=subsection]").count() == 0
        head = page.locator(".vol-block-head").first
        text = head.inner_text()
        assert "%" in text and "/" in text, text
        head.click()
        page.wait_for_function(
            "document.querySelectorAll('#view-group .card[data-level=subsection]').length > 0",
            timeout=30000,
        )
        page.select_option("#vol-select", "1")
        page.wait_for_function(
            "document.querySelectorAll('#view-group .vol-block').length === 0"
            " && document.querySelectorAll('#view-group .chapter-block').length > 0",
            timeout=30000,
        )
    finally:
        context.close()
