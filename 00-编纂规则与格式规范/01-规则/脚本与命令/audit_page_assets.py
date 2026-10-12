# -*- coding: utf-8 -*-
"""重构2026 页面资产层完整性门禁（固定脚本，2026-09-18 立，第九件改后必跑门禁）。

用途：对 `08-核查报告与多轮复核/重构2026/` 的**页面级附加件**做完整性自检，
补足既有八件门禁共同未覆盖的维度。

既有八件（见 `重构2026/tests/README.md` 配套门禁清单）：
  一 目录页 DATA 数据完整性    audit_data_integrity.py
  二 口径漂移检测              sync_refactor2026_baseline.py --check
  三 节号／章号连续性          audit_sequence_continuity.py
  四 分工注交叉引用悬空        xref_audit.py
  五 大纲注入块证据等级        audit_evidence_level_labels.py
  六 目录页结构十一项静态自检  audit_index_structure.py
  七 catalog 与内嵌数据块一致  embed.py --check
  八 四层解耦装配零漂移        assemble_index.py --check

**共同盲区**：八件皆以「产物 index.html」或「大纲 .md」为对象，**页面级附加件本身
（内嵌字体子集、品牌派生件、自包含性）无任何门禁**。设立缘由（2026-09-18）：
  ① 内嵌字体子集按「页面可见字符集」精确子集化；大纲增改引入新汉字后若忘记重建
     子集，新字将静默回退系统字体——渲染不破，八件门禁与三套浏览器回归皆不报错；
  ② 品牌派生件（真矢量 logo／三帧 favicon）系第十七批手工产物，形制无护栏，
     若被光栅原件覆盖将静默膨胀体积；
  ③ 「零外部依赖」是单体交付的核心不变量（加载期请求数 = 1），无静态护栏；
  ④ 测试套件含随目录变动须同步的夹具值，陈旧夹具会以「判据缺陷」形式误报；
  ⑤ 页面派生指标「未决项」（N_PENDING）原无门禁守护：存在性与数值变化皆静默
     （2026-10-11 实测事故，见 E4 注；本件以 E4 交叉核验补位）。

核验项（0 异常 exit 0；有异常 exit 1；环境缺失 exit 2）：
  A  装配源清单：五层解耦源文件存在且非空（行为层 src/js/manifest.txt 清单驱动，
     2026-10-12 143 批 wave5；清单缺位回退 9 文件兼容态）
  B  内嵌字体子集：
     B1 `assets/doc.css` 中 `@font-face` 恰 1 片，`src` 为 data:font/woff2 URI（无外链）
     B2 内嵌 woff2 可解析、cmap 非空
     B3 覆盖度：页面字符集（index.html 可见文本 ∪ `data/catalog.json` 字符串值 ∪
        `doc.js`／`theme-preset.js` 源码字符）中，凡**源字体有而内嵌件缺失**者即回归 → FAIL；
        源字体本无者记 INFO（系统 fallback，允许）
     B4 源字体覆盖清单 `data/font-source-cmap.txt` 存在且自洽；字体源 tgz 在场时交叉核验
  C  品牌派生件形制：
     C1 `assets/logo.svg` 为真矢量（含 `<svg`、无 `<image>`、无 base64 光栅）
     C2 `assets/favicon.ico` 为合法 ICO 且含 16／32／48 三帧
     C3 页面内嵌品牌件与磁盘派生件逐字节一致
     C4 og:image 与 apple-touch-icon 逐字节一致且尺寸元数据完整（2026-10-12 141 批）
  D  自包含性（零外部依赖）：
     D1 index.html 无 http(s) 外链资源引用、无 @import
     D2 内嵌数据 blob 的 data-integrity（SRI）与实际内容一致
  E  测试夹具口径一致性：
     E1 `tests/*.mjs` 口径串与页面 doc-metrics 一致
     E2 `tests/*.mjs` 溯源注计数与页面 `.src` 节数一致
     E3 `tests/README.md` 断言清单 T 编号集与 `visual_regression.mjs` 的 record() 编号集一致
     E4 页面 doc-metrics「未决项」格与内容源结构性待补声明双向一致（独立实现交叉核验；
        2026-10-11 立，缘由＝引述文本误报事故——装配器 N_PENDING 旧判据为朴素子串，
        7.3 注引述镜像旧标注致瓦片自 0 复活且静默；装配器判据同期收紧）

触发条件：**改动任一装配源、品牌派生件或字体子集后必跑**。

依赖：fontTools + brotli（解析 woff2）。须以带该依赖的解释器运行（字体子集脚本同源；
任一含 fontTools＋brotli 的解释器均可，2026-10-11 校正——原指定 venv 已失效）：
  C:/Python314/python.exe audit_page_assets.py

字体源 tgz（B4 交叉核验用）位于 `script/_font_embed_20260905/`，该目录被 `.gitignore` 的
`/script` 规则排除（临时目录规则），故**不依赖其存在**：B4 的基准是受版本控制的
`data/font-source-cmap.txt`；tgz 在场时额外交叉核验，缺失时仅记 INFO。

用法（解释器须含 fontTools＋brotli，任选其一）：
  <fontTools+brotli-python> audit_page_assets.py                        # 常规审计
  <fontTools+brotli-python> audit_page_assets.py --root <dir>           # 审计指定树根（备份件／快照交叉验证、
                                                                        # 负向测试；默认 重构2026/）
  <fontTools+brotli-python> audit_page_assets.py --refresh-source-cmap  # 从字体源 tgz 重建 B4 基准清单
  <fontTools+brotli-python> audit_page_assets.py --selftest               # 判据非空自检（E4 双向四用例，临时树）

规则索引：本脚本登记于 `01-规则/README.md`（固定脚本）与流程规则.md
「页面资产层完整性门禁」小节。
"""
import argparse
import base64
import hashlib
import io
import json
import os
import re
import struct
import sys
import tarfile
import tempfile

# ===== 路径常量（机器固定值，迁移时同步更新）=====
DEFAULT_ROOT = r"D:/librebsd/08-核查报告与多轮复核/重构2026"
ROOT = DEFAULT_ROOT
ASSETS = ROOT + "/assets"
DATA = ROOT + "/data"
TESTS = ROOT + "/tests"
INDEX = ROOT + "/index.html"
DOC_CSS = ASSETS + "/doc.css"
DOC_JS = ASSETS + "/doc.js"
THEME_JS = ASSETS + "/theme-preset.js"
LOGO_SVG = ASSETS + "/logo.svg"
FAVICON = ASSETS + "/favicon.ico"
TOUCH_ICON = ASSETS + "/apple-touch-icon.png"
CATALOG_JSON = DATA + "/catalog.json"
SRC_CMAP = DATA + "/font-source-cmap.txt"
FONT_SOURCE_TGZ = r"D:/librebsd/script/_font_embed_20260905/lxgw-wenkai-screen-webfont-1.7.0.tgz"
FONT_FAMILY = "LXGW WenKai Screen"


def set_root(root):
    """切换被审计树根（`--root`；用于备份件／快照交叉验证与负向测试）。"""
    global ROOT, ASSETS, DATA, TESTS, INDEX, DOC_CSS, DOC_JS, THEME_JS
    global LOGO_SVG, FAVICON, TOUCH_ICON, CATALOG_JSON, SRC_CMAP
    ROOT = root.rstrip("/\\")
    ASSETS = ROOT + "/assets"
    DATA = ROOT + "/data"
    TESTS = ROOT + "/tests"
    INDEX = ROOT + "/index.html"
    DOC_CSS = ASSETS + "/doc.css"
    DOC_JS = ASSETS + "/doc.js"
    THEME_JS = ASSETS + "/theme-preset.js"
    LOGO_SVG = ASSETS + "/logo.svg"
    FAVICON = ASSETS + "/favicon.ico"
    TOUCH_ICON = ASSETS + "/apple-touch-icon.png"
    CATALOG_JSON = DATA + "/catalog.json"
    SRC_CMAP = DATA + "/font-source-cmap.txt"

# 五层解耦装配源（第八件 assemble_index.py 的输入；2026-09-30 补文案层）
SRC_FILES = [
    ("内容层", "data/outline.txt"),
    ("文案层", "data/ui-strings.json"),
    ("格式层", "assets/doc.css"),
    ("现代化层", "assets/modern.css"),
    ("行为层", "assets/doc.js"),
    ("行为层", "assets/theme-preset.js"),
    ("页壳", "assets/page.template.html"),
    ("数据层", "data/catalog.json"),
    ("数据层", "data/schema.jsonld"),
]

FAILS = []
INFOS = []


def rec(label, ok, detail=""):
    print(("PASS | " if ok else "FAIL | ") + label + (" | " + detail if detail else ""))
    if not ok:
        FAILS.append(label)
    return ok


def info(label, detail):
    print("INFO | " + label + " | " + detail)
    INFOS.append(label + "：" + detail)


# ---------- 未决项交叉核验（E4；2026-10-11 立） ----------

def count_pending_decl(text):
    """内容源中的**结构性待补声明**计数（独立实现，不复用装配器判据）。

    定义（与装配器收紧后判据同语义、不同实现）：节行（`- N.M `）的注文段
    （`@@` 定界；前置形 `@@〔…〕@@`、后缀形 `…@@〔…〕`）以「〔待补」或「〔待重建」
    **起首**者计入；注文中部的引述（如镜像旧标注名）不计入。
    """
    n = 0
    for ln in text.splitlines():
        if not ln.startswith("- "):
            continue
        for seg in re.findall(r"@@(.*?)(?=@@|$)", ln):
            if re.match(r"〔(?:待补|待重建)", seg):
                n += 1
    return n


def page_pending_value(h):
    """页面 doc-metrics「未决项」格值；无格（N_PENDING=0 时整格隐藏）返回 0。

    锚＝小字文案〔待补／待重建〕（与 E1／E2 同构）；该文案调整时须同步本判据。
    """
    m = re.search(r"<strong>(\d+)</strong><small>〔待补／待重建〕</small>", h)
    return int(m.group(1)) if m else 0


# ---------- 字体源覆盖清单（B4 基准） ----------

def cmap_to_ranges(cps):
    """码位集合 → 区间列表 [(a, b), ...]（升序、已合并）。"""
    srt = sorted(cps)
    out = []
    a = b = srt[0]
    for c in srt[1:]:
        if c == b + 1:
            b = c
        else:
            out.append((a, b))
            a = b = c
    out.append((a, b))
    return out


def ranges_to_text(rng):
    return "\n".join("%04X-%04X" % (a, b) if a != b else "%04X" % a for a, b in rng)


def parse_cmap_text(text):
    """解析区间清单 → 码位集合。忽略空行与 `#` 注释行。"""
    cps = set()
    for ln in text.splitlines():
        ln = ln.strip()
        if not ln or ln.startswith("#"):
            continue
        if "-" in ln:
            a, b = ln.split("-", 1)
            a, b = int(a, 16), int(b, 16)
        else:
            a = b = int(ln, 16)
        cps.update(range(a, b + 1))
    return cps


def load_source_font_cmap(tgz_path):
    """从字体源 tgz 合并全部分片 cmap → 码位集合。"""
    import fontTools.ttLib as _tt
    cps = set()
    n = 0
    with tarfile.open(tgz_path) as t:
        for m in t.getnames():
            if m.endswith(".woff2") and "files/" in m:
                tt = _tt.TTFont(io.BytesIO(t.extractfile(m).read()))
                cps.update(tt.getBestCmap().keys())
                n += 1
    return cps, n


def refresh_source_cmap():
    if not os.path.exists(FONT_SOURCE_TGZ):
        print("错误：字体源 tgz 缺失，无法重建基准清单：", FONT_SOURCE_TGZ)
        return 2
    cps, n = load_source_font_cmap(FONT_SOURCE_TGZ)
    sha = hashlib.sha256(open(FONT_SOURCE_TGZ, "rb").read()).hexdigest()
    head = (
        "# 霞鹜文楷屏幕版（LXGW WenKai Screen）源字体字符覆盖清单\n"
        "# 用途：重构2026 第九件门禁 audit_page_assets.py 的 B4 判据基准\n"
        "# 生成：python audit_page_assets.py --refresh-source-cmap\n"
        "# 字体源：script/_font_embed_20260905/lxgw-wenkai-screen-webfont-1.7.0.tgz\n"
        "#   字体源 sha256：%s\n"
        "#   分片数：%d ／ 合并后码位数：%d\n"
        "# 格式：每行一个码位区间 `XXXX-YYYY`，单码位写作 `XXXX`（十六进制大写，4–6 位）\n"
        % (sha, n, len(cps))
    )
    txt = head + ranges_to_text(cmap_to_ranges(cps)) + "\n"
    with open(SRC_CMAP, "w", encoding="utf-8", newline="\n") as f:
        f.write(txt)
    print("已重建 %s：%d 码位 → %d 区间，%d 字节"
          % (SRC_CMAP, len(cps), len(cmap_to_ranges(cps)), len(txt.encode("utf-8"))))
    return 0


# ---------- 主流程 ----------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=DEFAULT_ROOT,
                    help="被审计树根（默认 重构2026/；备份件／快照交叉验证与负向测试用）")
    ap.add_argument("--refresh-source-cmap", action="store_true",
                    help="从字体源 tgz 重建 data/font-source-cmap.txt 后退出")
    ap.add_argument("--selftest", action="store_true",
                    help="判据非空自检（E4 双向四用例，临时最小树；不触碰正式树）")
    args = ap.parse_args()

    if args.selftest:
        return cmd_selftest()

    set_root(args.root)

    if args.refresh_source_cmap:
        return refresh_source_cmap()

    try:
        import fontTools.ttLib as _tt  # noqa: F401
    except ImportError:
        print("环境错误：缺少 fontTools（本门禁需解析 woff2）。")
        print("请以带该依赖的解释器运行，例如：")
        print("  C:/Python314/python.exe audit_page_assets.py")
        return 2

    # 字符集定义与 font_subset_rebuild.py 同源（避免两脚本判据漂移）
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    try:
        import font_subset_rebuild as FSR
    except ImportError as e:
        print("环境错误：无法导入 font_subset_rebuild.py（字符集定义同源依赖）：", e)
        return 2

    from fontTools.ttLib import TTFont

    print("=" * 68)
    print("重构2026 页面资产层完整性门禁（第九件）")
    print("=" * 68)

    # ---- A 装配源清单 ----
    src_files = list(SRC_FILES)
    mf = ROOT + "/src/js/manifest.txt"
    if os.path.isfile(mf):
        # 143 批 wave5：行为层源件清单化——manifest＋清单件入列（doc.js 仍列，派生件须在盘）
        names = [ln.strip() for ln in io.open(mf, encoding="utf-8").read().splitlines()
                 if ln.strip() and not ln.strip().startswith("#")]
        src_files.append(("行为层", "src/js/manifest.txt"))
        for nm in names:
            src_files.append(("行为层", "src/js/" + nm))
    miss = [("%s %s" % (l, p)) for l, p in src_files
            if not (os.path.isfile(ROOT + "/" + p) and os.path.getsize(ROOT + "/" + p) > 0)]
    total = len(src_files)
    rec("A 装配源清单（%d 个源文件存在且非空）" % total, not miss,
        ("缺失/空：" + "、".join(miss)) if miss else "%d/%d 齐备" % (total, total))

    # ---- 读取产物 ----
    h = io.open(INDEX, encoding="utf-8").read()
    css = io.open(DOC_CSS, encoding="utf-8").read()

    # ---- B1 @font-face 形制 ----
    n_face = css.count("@font-face")
    m_face = re.search(r"@font-face\s*\{(.*?)\}", css, re.S)
    face = m_face.group(1) if m_face else ""
    m_url = re.search(r"url\(\s*data:font/woff2;base64,([A-Za-z0-9+/=]+)\s*\)", face)
    b1_ok = (n_face == 1) and bool(m_url) and (FONT_FAMILY in face)
    rec("B1 @font-face 恰 1 片且为 data:font/woff2 内嵌", b1_ok,
        "face=%d，data URI=%s，family=%s" % (n_face, "有" if m_url else "无",
                                            "有" if FONT_FAMILY in face else "无"))

    emb_cmap = {}
    if b1_ok:
        blob = base64.b64decode(m_url.group(1))
        try:
            emb_cmap = TTFont(io.BytesIO(blob)).getBestCmap()
            b2_ok = len(emb_cmap) > 0
            b2_detail = "woff2 %d 字节，cmap %d 字" % (len(blob), len(emb_cmap))
        except Exception as e:  # noqa: BLE001
            b2_ok, b2_detail = False, "woff2 解析失败：%r" % (e,)
        rec("B2 内嵌 woff2 可解析且 cmap 非空", b2_ok, b2_detail)

    # ---- B3 覆盖度 ----
    if emb_cmap:
        chars = FSR.extract_visible_chars(h)
        if not os.path.exists(SRC_CMAP):
            rec("B4 源字体覆盖清单存在", False,
                "缺 %s，请运行 --refresh-source-cmap" % SRC_CMAP)
            src_cps = None
        else:
            src_cps = parse_cmap_text(io.open(SRC_CMAP, encoding="utf-8").read())
            rec("B4 源字体覆盖清单存在", len(src_cps) > 0,
                "%d 码位（%d 区间行）" % (len(src_cps),
                                         len([1 for ln in io.open(SRC_CMAP, encoding="utf-8")
                                              if ln.strip() and not ln.startswith("#")])))
        if src_cps:
            missing = [c for c in chars if ord(c) not in emb_cmap]
            regress = [c for c in missing if ord(c) in src_cps]
            fallback = [c for c in missing if ord(c) not in src_cps]
            rec("B3 内嵌字体覆盖页面字符集（无回归缺字）", not regress,
                ("回归缺字 %d：%s" % (len(regress), "".join(regress))) if regress
                else "页面 %d 字，缺 %d 全属源本无" % (len(chars), len(missing)))
            if fallback:
                info("B3 源字体本无（系统 fallback，允许）",
                     "%d 字：%s" % (len(fallback), "".join(fallback)))

        # ---- B4 交叉核验：字体源 tgz 在场时与基准清单比对 ----
        if os.path.exists(FONT_SOURCE_TGZ) and src_cps:
            live, n_slice = load_source_font_cmap(FONT_SOURCE_TGZ)
            rec("B4 基准清单与字体源 tgz 一致", live == src_cps,
                "%d 片，tgz %d 码位 / 基准 %d 码位%s"
                % (n_slice, len(live), len(src_cps),
                   "" if live == src_cps else "（差异 %d，请 --refresh-source-cmap）"
                   % len(live ^ src_cps)))
        elif not os.path.exists(FONT_SOURCE_TGZ):
            info("B4 字体源 tgz 不在场", "跳过交叉核验（基准清单受版本控制，不影响判据）")

    # ---- C 品牌派生件形制 ----
    svg = io.open(LOGO_SVG, encoding="utf-8", errors="replace").read()
    c1_bad = []
    if "<svg" not in svg:
        c1_bad.append("非 SVG")
    if "<image" in svg:
        c1_bad.append("含 <image> 内嵌光栅")
    if "base64" in svg:
        c1_bad.append("含 base64 数据")
    rec("C1 logo.svg 为真矢量（无内嵌光栅）", not c1_bad,
        "；".join(c1_bad) if c1_bad else "%d 字节" % len(svg.encode("utf-8")))

    ico = open(FAVICON, "rb").read()
    c2_bad, frames = [], []
    try:
        res, typ, n = struct.unpack("<HHH", ico[:6])
        if res != 0 or typ != 1:
            c2_bad.append("ICO 头非法（reserved=%d type=%d）" % (res, typ))
        for i in range(n):
            o = 6 + i * 16
            w, hh = struct.unpack("<BB", ico[o:o + 2])
            frames.append(w or 256)
    except Exception as e:  # noqa: BLE001
        c2_bad.append("ICO 解析失败：%r" % (e,))
    need = {16, 32, 48}
    if set(frames) != need:
        c2_bad.append("帧集合 %s ≠ 16/32/48" % sorted(frames))
    rec("C2 favicon.ico 含 16／32／48 三帧", not c2_bad,
        "；".join(c2_bad) if c2_bad else "帧 %s，%d 字节" % (sorted(frames), len(ico)))

    touch = open(TOUCH_ICON, "rb").read()
    c2b_bad = []
    if touch[:8] != b"\x89PNG\r\n\x1a\n":
        c2b_bad.append("非 PNG 签名")
    else:
        # PNG IHDR：宽/高为大端 32 位（偏移 16/20）
        tw, th = struct.unpack(">II", touch[16:24])
        if (tw, th) != (180, 180):
            c2b_bad.append("尺寸 %dx%d ≠ 180x180" % (tw, th))
    rec("C2b apple-touch-icon.png 为 180x180 PNG（2026-10-12 138 批 D2）", not c2b_bad,
        "；".join(c2b_bad) if c2b_bad else "%d 字节" % len(touch))

    m_logo = re.search(r'src="data:image/svg\+xml;base64,([A-Za-z0-9+/=]+)"', h)
    m_ico = re.search(r'href="data:image/x-icon;base64,([A-Za-z0-9+/=]+)"', h)
    m_touch = re.search(r'rel="apple-touch-icon"[^>]*href="data:image/png;base64,([A-Za-z0-9+/=]+)"', h)
    c3_bad = []
    if not m_logo:
        c3_bad.append("页面无内嵌 logo")
    elif base64.b64decode(m_logo.group(1)) != open(LOGO_SVG, "rb").read():
        c3_bad.append("logo 与 assets/logo.svg 不一致")
    if not m_ico:
        c3_bad.append("页面无内嵌 favicon")
    elif base64.b64decode(m_ico.group(1)) != ico:
        c3_bad.append("favicon 与 assets/favicon.ico 不一致")
    if not m_touch:
        c3_bad.append("页面无内嵌 apple-touch-icon")
    elif base64.b64decode(m_touch.group(1)) != touch:
        c3_bad.append("apple-touch-icon 与 assets/apple-touch-icon.png 不一致")
    rec("C3 页面内嵌品牌件与磁盘派生件逐字节一致", not c3_bad,
        "；".join(c3_bad) if c3_bad else "logo ＋ favicon ＋ apple-touch-icon 均一致")

    m_ogi = re.search(r'<meta property="og:image" content="data:image/png;base64,([A-Za-z0-9+/=]+)">', h)
    m_ogw = re.search(r'<meta property="og:image:width" content="(\d+)">', h)
    m_ogh = re.search(r'<meta property="og:image:height" content="(\d+)">', h)
    c4_bad = []
    if not m_ogi:
        c4_bad.append("页面无 og:image data URI")
    elif base64.b64decode(m_ogi.group(1)) != touch:
        c4_bad.append("og:image 与 assets/apple-touch-icon.png 不一致")
    if not m_ogw or m_ogw.group(1) != "180":
        c4_bad.append("og:image:width 非 180")
    if not m_ogh or m_ogh.group(1) != "180":
        c4_bad.append("og:image:height 非 180")
    rec("C4 og:image 与 apple-touch-icon 逐字节一致且尺寸元数据完整（2026-10-12 141 批）", not c4_bad,
        "；".join(c4_bad) if c4_bad else "og:image ＝ apple-touch-icon（%d B），180x180" % len(touch))

    # ---- D 自包含性 ----
    ext = []
    for pat, name in ((r'src\s*=\s*["\']https?://', "src= 外链"),
                      (r'href\s*=\s*["\']https?://', "href= 外链"),
                      (r'url\(\s*["\']?https?://', "url() 外链"),
                      (r"@import", "@import")):
        k = len(re.findall(pat, h))
        if k:
            ext.append("%s %d 处" % (name, k))
    rec("D1 index.html 零外部资源依赖", not ext,
        "；".join(ext) if ext else "无 http(s) 外链、无 @import")

    m_tag = re.search(r'<script\b[^>]*\bid="opt-data-blob"[^>]*>', h)
    if not m_tag:
        rec("D2 内嵌数据 blob 的 SRI 自校验一致", False, "未找到 id=opt-data-blob")
    else:
        mi = re.search(r'data-integrity="sha256-([A-Za-z0-9+/=]+)"', m_tag.group(0))
        if not mi:
            rec("D2 内嵌数据 blob 的 SRI 自校验一致", False, "数据块缺 data-integrity")
        else:
            end = h.find("</script>", m_tag.end())
            payload = re.sub(r"\s", "", h[m_tag.end():end]).encode("ascii")
            got = base64.b64encode(hashlib.sha256(payload).digest()).decode()
            rec("D2 内嵌数据 blob 的 SRI 自校验一致", got == mi.group(1),
                "blob %d 字节%s" % (len(payload),
                                   "" if got == mi.group(1)
                                   else "；声明 %s 实得 %s" % (mi.group(1), got)))

    # ---- E 测试夹具口径一致性 ----
    m_v = re.search(r"<strong>(\d+)</strong><small>主线", h)
    m_c = re.search(r"<strong>(\d+)</strong><small>正章", h)
    m_s = re.search(r"<strong>(\d+)</strong><small>节级落点", h)
    if m_v and m_c and m_s:
        stat = "%s 卷 %s 章 %s 节" % (m_v.group(1), m_c.group(1), m_s.group(1))
        n_src = h.count('class="src"')
        suite_files = sorted(f for f in os.listdir(TESTS) if f.endswith(".mjs")
                             and not f.startswith("_") and not f.startswith("probe"))
        bad_stat, bad_src = [], []
        for fn in suite_files:
            txt = io.open(TESTS + "/" + fn, encoding="utf-8").read()
            for v in set(re.findall(r"\d+ 卷 \d+ 章 \d+ 节", txt)):
                if v != stat:
                    bad_stat.append("%s：%s" % (fn, v))
            for v in set(re.findall(r"注\s*(\d+)", txt)):
                if int(v) != n_src:
                    bad_src.append("%s：注 %s（页面 %d）" % (fn, v, n_src))
        rec("E1 套件口径串与页面 doc-metrics 一致", not bad_stat,
            "；".join(bad_stat) if bad_stat else "%s（%d 个套件文件）" % (stat, len(suite_files)))
        rec("E2 套件溯源注计数与页面 .src 节数一致", not bad_src,
            "；".join(bad_src) if bad_src else "注 %d" % n_src)

        # E3 断言清单 ↔ record() 编号一一对应
        vs = io.open(TESTS + "/visual_regression.mjs", encoding="utf-8").read()
        suite_t = {int(x) for x in re.findall(r"record\(\s*'T(\d+)", vs)}
        rm = io.open(TESTS + "/README.md", encoding="utf-8").read()
        doc_t = set()
        for ln in rm.splitlines():
            if ln.startswith("- T"):
                doc_t.update(int(x) for x in re.findall(r"T(\d+)", ln))
        only_suite = sorted(suite_t - doc_t)
        only_doc = sorted(doc_t - suite_t)
        rec("E3 断言清单 T 编号集与套件 record() 一致", not only_suite and not only_doc,
            ("套件独有 T%s；清单独有 T%s"
             % (only_suite, only_doc)) if (only_suite or only_doc)
            else "T1–T%d 共 %d 项，双向吻合" % (max(suite_t), len(suite_t)))
    else:
        rec("E1/E2/E3 测试夹具口径一致性", False, "无法从 doc-metrics 解析口径三元组")

    # ---- E4 未决项交叉核验（2026-10-11 立；独立实现，不随 ABCD/E1-3 短路） ----
    try:
        ol_text = io.open(os.path.join(ROOT, "data", "outline.txt"), encoding="utf-8").read()
    except OSError as e:
        rec("E4 未决项格与内容源结构性待补声明双向一致", False, "内容源读取失败：%r" % e)
    else:
        n_decl = count_pending_decl(ol_text)
        p_page = page_pending_value(h)
        rec("E4 未决项格与内容源结构性待补声明双向一致", n_decl == p_page,
            "源声明 %d ／ 页面格 %s" % (n_decl, str(p_page) if p_page else "无（N_PENDING=0，整格隐藏）"))

    print("-" * 68)
    if FAILS:
        print("门禁结论：FAIL %d 项 —— %s" % (len(FAILS), "；".join(FAILS)))
        return 1
    print("门禁结论：页面资产层完整性 PASS（INFO %d 项）" % len(INFOS))
    return 0


def cmd_selftest():
    """E4 判据非空自检（2026-10-11 立）：临时最小树注入四用例——
    T1 页面有格 N=1 而源仅含引述（非结构性）→ 应 FAIL（引述误报守护）；
    T2 页面无格而源有结构性声明 → 应 FAIL（反向脱节）；
    T3 页面格 N=1 且源有 1 条结构性声明 → 应 PASS（合法对）；
    T4 页面无格且源仅含引述 → 应 PASS（引述不计入）。
    四用例全中 exit 0，否则 exit 1。"""
    import shutil
    tmp = tempfile.mkdtemp(prefix="pageassets_selftest_")
    LQ, RQ = chr(0x201c), chr(0x201d)
    note = "〔待补／待重建〕"
    decl_line = "- 1.1 测试节@@〔待补·待重建：正文期补齐〕"
    quote_line = "- 1.1 测试节@@〔溯源：镜像旧标注" + LQ + "待补（B3 深化）" + RQ + "——引述不计〕"

    def mk(idx_val, ol_lines):
        d = tempfile.mkdtemp(dir=tmp)
        os.makedirs(os.path.join(d, "data"))
        if idx_val is None:
            idx = '<div class="doc-metrics"></div>'
        else:
            idx = ('<div class="doc-metric"><span>未决项</span><strong>%d</strong>'
                   '<small>%s</small></div>' % (idx_val, note))
        io.open(os.path.join(d, "index.html"), "w", encoding="utf-8", newline="\n").write(idx)
        io.open(os.path.join(d, "data", "outline.txt"), "w", encoding="utf-8",
                newline="\n").write("\n".join(ol_lines) + "\n")
        return d

    cases = [
        ("T1 引述误报守护（页面 1 ／ 源引述）", 1, [quote_line], True),
        ("T2 反向脱节（页面无 ／ 源声明）", None, [decl_line], True),
        ("T3 合法对（页面 1 ／ 源声明 1）", 1, [decl_line], False),
        ("T4 引述不计入（页面无 ／ 源引述）", None, [quote_line], False),
    ]
    ok_all = True
    print("第九件 --selftest：E4 判据非空（临时最小树四用例）")
    for name, val, lines, exp_fail in cases:
        d = mk(val, lines)
        n_src = count_pending_decl(io.open(os.path.join(d, "data", "outline.txt"),
                                           encoding="utf-8").read())
        n_page = page_pending_value(io.open(os.path.join(d, "index.html"),
                                            encoding="utf-8").read())
        got_fail = (n_src != n_page)
        ok = (got_fail == exp_fail)
        ok_all = ok_all and ok
        print("  %s %s（源 %d ／ 页面 %d；预期 %s，实得 %s）"
              % ("✅" if ok else "❌", name, n_src, n_page,
                 "FAIL" if exp_fail else "PASS", "FAIL" if got_fail else "PASS"))
    shutil.rmtree(tmp, ignore_errors=True)
    if ok_all:
        print("  ✅ E4 判据非空：四用例（双向×正反）全部命中")
        return 0
    print("  ❌ E4 判据可能为空：存在未命中用例", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
