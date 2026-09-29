#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""assemble_index.py — 重构2026 目录页装配器（四层解耦，2026-09-18 立）。

**唯一写者**：`重构2026/index.html` 自此为**装配产物**，一切修改走本器。

四层源 → 单文件交付物：

| 层 | 源文件 | 说明 |
| - | - | - |
| 内容层 | `data/outline.txt` | **纯文本行式**，零 HTML 标记；卷/章/节题与溯源注的唯一编辑入口 |
| 格式层 | `assets/doc.css` | 原 `<style id="format-layer">` 正文 |
| 现代化层 | `assets/modern.css` | 原 `<style id="modern-layer">` 正文 |
| 行为层 | `assets/theme-preset.js`、`assets/doc.js` | 主题预设（head 内早执行）＋ 目录引擎 |
| 数据层 | `data/catalog.json`、`data/schema.jsonld` | 运行时数据（persons/refs/revs）＋ 结构化元数据 |
| 页壳 | `assets/page.template.html` | head／页框／main 骨架／tail，含占位符 |

**内容源语法**（`data/outline.txt`，纯文本行式）：

```
# 第一卷  自由与必然：从图灵机到 UNIX      → 卷题（<h2>），「第N卷」与题名间 2 个半角空格
> 本卷所书皆为形式主义化的重构……            → 卷导言（<p class="vol-overview">，可选）
! UNIX 本体技术演进；版本编年见卷1–3……      → 卷分工注（<p class="vol-note">，可选）
## 1 UNIX 的思想与技术前史                  → 章题（<h3 class="chapter">），含「第 M 章 」前缀
- 1.1 从数学逻辑到语言哲学：现代形式化思想的形成      → 节（<li>）：节号 ＋ 1 个半角空格 ＋ 题文
- 2.1 @@〔第一卷第 8 章 8.5 分工注〕@@ 商业大厦…    → @@ 定界＝溯源注**前置**（紧跟节号）
- 7.8 V7 前夜的 UNIX 生态与操作系统谱系@@〔时间：1978 年〕  → @@ 定界＝溯源注**后置**（行尾）
```

**标准形（canonical）**：一元素一行、LF、UTF-8 无 BOM；卷题后空一行；`<h3>` 与 `<ul class="sections">`
紧邻无空行；节 `<li>` 之间无空行；`</ul>` 紧邻下一 `<h3>` 或 `</section>`；卷块之间空一行。
口径数字（卷/章/节）**由内容源派生**，不手工维护。

用法：
  python assemble_index.py            # 装配（写 index.html）
  python assemble_index.py --check    # 漂移检测：重装到内存与磁盘逐字节比对，不一致即退出码 1
"""
import argparse
import base64
import html
import importlib.util
import io
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")   # 勿用 io.TextIOWrapper 包装：会让先前的包装器被回收而关闭共享缓冲区

REPO = pathlib.Path(__file__).resolve().parents[3]
BASE = REPO / "08-核查报告与多轮复核" / "重构2026"
INDEX = BASE / "index.html"
TPL = BASE / "assets" / "page.template.html"
DOC_CSS = BASE / "assets" / "doc.css"
MODERN_CSS = BASE / "assets" / "modern.css"
THEME_JS = BASE / "assets" / "theme-preset.js"
DOC_JS = BASE / "assets" / "doc.js"
OUTLINE = BASE / "data" / "outline.txt"
CATALOG = BASE / "data" / "catalog.json"
SCHEMA = BASE / "data" / "schema.jsonld"
# 品牌资源：**页面资产层**承载页面用派生件（2026-09-18 第十六批）
#   - 源：仓库根 logo.svg（1336px 光栅内嵌）／favicon.ico（单帧 256²）
#   - 页面用：BASE/assets/logo.svg（真矢量，21,887 B）／assets/favicon.ico（16²／32²／48²，6,424 B）
#   - 生成器：script/_r66/vectorize_logo.py（源文件不动，与字体子集同模式：源全量、页面用派生件）
BRAND_LOGO = BASE / "assets" / "logo.svg"
BRAND_FAVICON = BASE / "assets" / "favicon.ico"

# 复用 embed.py 的数据层序列化／SRI 函数（同目录）
_spec = importlib.util.spec_from_file_location("_embed", pathlib.Path(__file__).with_name("embed.py"))
_embed = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_embed)

SEC_RE = re.compile(r"^(\d+\.\d+)\s(.*)$")
VOL_RE = re.compile(r"^# (.*)$")
OVER_RE = re.compile(r"^> (.*)$")
NOTE_RE = re.compile(r"^! (.*)$")
CH_RE = re.compile(r"^## (.*)$")
SEC_LINE_RE = re.compile(r"^- (.*)$")
CN = "一二三四五六七八九十"


def cn2int(s):
    if s == "十":
        return 10
    if s.startswith("十"):
        return 10 + CN.index(s[1]) + 1
    if "十" in s:
        a, b = s.split("十")
        return (CN.index(a) + 1) * 10 + (CN.index(b) + 1 if b else 0)
    return CN.index(s) + 1


def read(p):
    return p.read_text(encoding="utf-8")


def write(p, s):
    p.write_bytes(s.replace("\r\n", "\n").encode("utf-8"))


# ── 内容层：解析 ────────────────────────────────────────────────────────
def parse_outline(text):
    """outline.txt → [{卷题, overview, note, chapters:[{章题, secs:[(节号, 题文, src, 前置?)]}]}]"""
    vols, vol = [], None
    ch = None
    for ln, raw in enumerate(text.split("\n"), 1):
        line = raw.rstrip()
        if not line.strip():
            continue
        m = VOL_RE.match(line)
        if m:
            vol = {"title": m.group(1), "overview": None, "note": None, "chapters": []}
            vols.append(vol)
            ch = None
            continue
        if vol is None:
            sys.exit("outline.txt 第 %d 行：卷题之前出现内容：%r" % (ln, line[:40]))
        m = OVER_RE.match(line)
        if m:
            if vol["overview"] is not None:
                sys.exit("outline.txt 第 %d 行：同一卷出现两个卷导言" % ln)
            vol["overview"] = m.group(1)
            continue
        m = NOTE_RE.match(line)
        if m:
            if vol["note"] is not None:
                sys.exit("outline.txt 第 %d 行：同一卷出现两个卷分工注" % ln)
            vol["note"] = m.group(1)
            continue
        m = CH_RE.match(line)
        if m:
            ch = {"title": m.group(1), "secs": []}
            vol["chapters"].append(ch)
            continue
        m = SEC_LINE_RE.match(line)
        if m:
            if ch is None:
                sys.exit("outline.txt 第 %d 行：章题之前出现节" % ln)
            body = m.group(1)
            ms = SEC_RE.match(body)
            if not ms:
                sys.exit("outline.txt 第 %d 行：节行缺少「节号 空格」前缀：%r" % (ln, body[:40]))
            num, rest = ms.group(1), ms.group(2)
            if rest.startswith("@@"):
                end = rest.index("@@", 2)
                ch["secs"].append((num, rest[end + 2:].lstrip(), rest[2:end], True))
            elif "@@" in rest:
                i = rest.index("@@")
                ch["secs"].append((num, rest[:i].rstrip(), rest[i + 2:], False))
            else:
                ch["secs"].append((num, rest, None, False))
            continue
        sys.exit("outline.txt 第 %d 行：无法识别的行：%r" % (ln, line[:50]))
    return vols


def esc(t):
    """文本 → HTML（内容源存解码文本，转义由格式层负责）。"""
    return html.escape(t, quote=False)


def render_outline(vols):
    """标准形渲染：31 卷块（每块以 </section> + 空行 结尾）。"""
    out = []
    for v, vol in enumerate(vols, 1):
        out.append('<section class="doc-block" id="vol-%d" role="doc-part">' % v)
        out.append("<h2>%s</h2>" % esc(vol["title"]))
        out.append("")
        if vol["overview"] is not None:
            out.append('<p class="vol-overview">%s</p>' % esc(vol["overview"]))
            out.append("")
        if vol["note"] is not None:
            out.append('<p class="vol-note">%s</p>' % esc(vol["note"]))
            out.append("")
        for m, ch in enumerate(vol["chapters"], 1):
            out.append('<h3 class="chapter" id="vol-%d-ch-%d">%s</h3>' % (v, m, esc(ch["title"])))
            out.append('<ul class="sections">')
            for num, title, src, pre in ch["secs"]:
                if src is None:
                    inner = esc(title)
                elif pre:
                    inner = '<span class="src">%s</span> %s' % (esc(src), esc(title))
                else:
                    inner = '%s<span class="src">%s</span>' % (esc(title), esc(src))
                out.append('<li><span class="sec-num">%s</span> %s</li>' % (num, inner))
            out.append("</ul>")
        out.append("</section>")
        out.append("")
    return "\n".join(out)


def derive_has_part(vols):
    """P3-3：JSON-LD Book.hasPart —— 卷级 Chapter 节点（position/name）。"""
    import json as _json
    parts = [{"@type": "Chapter", "position": i, "name": v["title"]}
             for i, v in enumerate(vols, 1)]
    return _json.dumps(parts, ensure_ascii=False, separators=(",", ":"))


def derive_metrics(vols):
    n_vol = len(vols)
    n_ch = sum(len(v["chapters"]) for v in vols)
    n_sec = sum(len(c["secs"]) for v in vols for c in v["chapters"])
    n_bib = sum(1 for v in vols for c in v["chapters"] if "卷末书目述评" in c["title"])
    n_src = sum(1 for v in vols for c in v["chapters"] for (num, title, src, pre) in c["secs"] if src)
    return {
        "N_VOL": n_vol, "N_CH": n_ch, "N_SEC": n_sec,
        "N_CH_MAIN": n_ch - n_bib, "N_CH_BIBLIO": n_bib,
        "N_SRC": n_src,
        "TRIPLE": "%d 卷 %d 章 %d 节" % (n_vol, n_ch, n_sec),
    }


# ── 装配 ────────────────────────────────────────────────────────────────
def data_uri(path, mime):
    """品牌资源 → data URI（保持单文件交付物；CSP 允许 data:）。"""
    return "data:%s;base64,%s" % (mime, base64.b64encode(path.read_bytes()).decode("ascii"))


def assemble():
    tpl = read(TPL)
    vols = parse_outline(read(OUTLINE))
    met = derive_metrics(vols)
    met["HAS_PART"] = derive_has_part(vols)
    body = render_outline(vols)

    catalog = _embed.load_catalog()
    content = {k: v for k, v in catalog.items() if k not in ("$schema", "version")}
    blob_body = _embed.encode_blob(_embed.serialize_content(content))
    sri = _embed.integrity_of(blob_body)

    schema = read(SCHEMA)
    for k, v in met.items():
        schema = schema.replace("{{%s}}" % k, str(v))
    for k, v in met.items():
        tpl = tpl.replace("{{%s}}" % k, str(v))

    subs = {
        "THEME_JS": read(THEME_JS).strip("\n"),
        "CSS_FORMAT": read(DOC_CSS).strip("\n"),
        "CSS_MODERN": read(MODERN_CSS).strip("\n"),
        "JSONLD": schema.strip("\n"),
        "OUTLINE": body,
        "BLOB": blob_body,
        "SRI": sri,
        "JS_BEHAVIOR": read(DOC_JS).strip("\n"),
        "LOGO": data_uri(BRAND_LOGO, "image/svg+xml"),
        "FAVICON": data_uri(BRAND_FAVICON, "image/x-icon"),
    }
    for k, v in subs.items():
        if ("{{%s}}" % k) not in tpl:
            sys.exit("模板缺少占位符 {{%s}}" % k)
        tpl = tpl.replace("{{%s}}" % k, v)
    left = re.findall(r"\{\{[A-Z_]+\}\}", tpl)
    if left:
        sys.exit("模板存在未替换占位符：%s" % sorted(set(left)))
    # 首尾规范化（2026-09-18 版式整治）：DOCTYPE 前不留空行；结尾恰一个换行
    tpl = tpl.lstrip("\n")
    tpl = tpl.rstrip("\n") + "\n"
    return tpl


def cmd_check():
    disk = read(INDEX)
    built = assemble()
    if disk == built:
        print("装配产物与磁盘 index.html 一致：✅ 无漂移")
        return 0
    d, b = disk.split("\n"), built.split("\n")
    print("装配产物与磁盘 index.html 不一致：❌ 漂移（%d 行 vs %d 行）" % (len(d), len(b)))
    shown = 0
    for i in range(max(len(d), len(b))):
        x = d[i] if i < len(d) else "<缺行>"
        y = b[i] if i < len(b) else "<缺行>"
        if x != y:
            print("  首差 行 %d：\n    磁盘 %r\n    装配 %r" % (i + 1, x[:110], y[:110]))
            shown += 1
            if shown >= 3:
                break
    print("  （运行 python assemble_index.py 重新装配）")
    return 1


def main():
    ap = argparse.ArgumentParser(description="重构2026 目录页装配器（四层解耦）")
    ap.add_argument("--check", action="store_true", help="漂移检测（重装到内存与磁盘比对）")
    args = ap.parse_args()
    if args.check:
        return cmd_check()
    built = assemble()
    old = read(INDEX)
    if built == old:
        print("assemble：无变更（幂等）")
    else:
        write(INDEX, built)
        _old_n, _new_n = len(old.encode("utf-8")), len(built.encode("utf-8"))
        print("assemble：已装配 %d → %d 字节" % (_old_n, _new_n))
        # O17 单体膨胀守卫（2026-09-27 补入）：产物字节较上一版增幅 >5% 时告警。
        # 单体性由第九件门禁硬校验（零外链／SRI／内嵌字体），但膨胀失控无护栏；
        # 本项**只告警不 FAIL**（不改变退出码）——正常增删章节约在千分之几量级，
        # 越过 5% 通常是内嵌资源被整块替换或装配源被重复注入。
        if _old_n and _new_n > _old_n * 1.05:
            print("  ⚠ 单体膨胀告警：增幅 %.1f%%（%d → %d 字节，阈值 5%%）"
                  % ((_new_n / _old_n - 1) * 100, _old_n, _new_n))
    vols = parse_outline(read(OUTLINE))
    met = derive_metrics(vols)
    print("口径（由内容源派生）：%s" % met["TRIPLE"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
