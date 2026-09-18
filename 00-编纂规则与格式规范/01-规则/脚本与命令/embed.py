#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""embed.py — 重构2026 目录页数据装配脚本（固定脚本，规则引用）。

用途：
  把 `重构2026/data/catalog.json`（语义数据中枢）序列化后重写
  `重构2026/index.html` 的压缩数据块 `<script type="application/gzip+base64" id="opt-data-blob">`（发布态装配）。
  单体 HTML 交付物不变：除数据块内容外其余位零改动。
  构建幂等：同一 catalog 两次运行产物位相同（diff 为空；gzip 头 mtime 固定为 0）。

流程：
  1) 校验 catalog 结构（必需字段 + persons 数量 > 0）；
  2) 定位 index.html 的压缩数据块标记（正则锚定，标记外零触碰）；
  3) 以 `json.dumps(..., ensure_ascii=False, separators=(",", ":"))` 序列化，
     gzip -9 压缩（mtime=0 保证幂等）、base64 按 120 列折行；
  4) **同步 data-integrity（SRI）**：对去空白后的 base64 文本取 SHA-256 写回开标签
     （2026-09-18 修复：此前装配改写正文却不刷 SRI，页面装载器校验失败而降级）；
  5) 写回（UTF-8 无 BOM、LF）；
  6) 输出 SHA-256 摘要供 changelog 审计。

  历史（2026-09-13 O-2 前）：数据载体为 behavior-layer 内 `var DATA = {...};` 字面量。
  O-2（2026-09-13 批复施工）后改为压缩数据块 + 运行时 DecompressionStream 异步装配，
  浏览器端装载器见 index.html 数据联动 IIFE 开头（对 base64 文本做 SHA-256 比对）。

  **2026-09-18 起角色调整（四层解耦）**：`index.html` 转为**装配产物**，正式装配走
  `assemble_index.py`（读内容/格式/现代化/行为/数据/页壳六类源，口径由内容源派生）。
  本脚本保留为**数据层序列化模块 ＋ 门禁**——供装配器复用其
  `encode_blob()`／`integrity_of()`／`serialize_content()`；`--check` 三项检测照旧。
  直接运行本脚本（无参）仍可单独重装数据块，但随后须跑 `assemble_index.py --check`
  确认无漂移（否则下次装配会覆盖）。

用法：
  python embed.py              # 装配（默认）
  python embed.py --check      # 仅检测 catalog 与内嵌数据块是否一致（漂移检测）

规则依据：流程规则.md「重构大纲目录口径同步规则」→「DATA 数据完整性门禁」小节。
"""
import argparse
import base64
import gzip
import hashlib
import io
import json
import pathlib
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
# 脚本位于 00-编纂规则与格式规范/01-规则/脚本与命令/embed.py
REPO = pathlib.Path(__file__).resolve().parents[3]
CATALOG = REPO / "08-核查报告与多轮复核" / "重构2026" / "data" / "catalog.json"
INDEX = REPO / "08-核查报告与多轮复核" / "重构2026" / "index.html"

# 压缩数据块标记（2026-09-13 O-2 起；历史载体 var DATA 字面量已废弃）
BLOB_RE = re.compile(
    r'(<script type="application/gzip\+base64" id="opt-data-blob"[^>]*>\n)(.*?)(\n</script>)', re.S)


def serialize_content(content):
    return json.dumps(content, ensure_ascii=False, separators=(",", ":"))


def encode_blob(serialized: str) -> str:
    """gzip -9（mtime=0 幂等）→ base64 → 120 列折行。"""
    gz = gzip.compress(serialized.encode("utf-8"), 9, mtime=0)
    b64 = base64.b64encode(gz).decode("ascii")
    return "\n".join(b64[i:i + 120] for i in range(0, len(b64), 120))


def integrity_of(blob_body: str) -> str:
    """数据块 SRI 哈希：与页面装载器同口径 —— 对去空白后的 base64 文本取 SHA-256。"""
    b64 = re.sub(r"\s+", "", blob_body)
    return "sha256-" + base64.b64encode(hashlib.sha256(b64.encode("utf-8")).digest()).decode("ascii")


def sync_integrity(tag_attrs: str, blob_body: str) -> str:
    """把 data-integrity 属性同步为当前数据块正文的 SRI 哈希（2026-09-18 修复：
    装配改写正文后必须同刷 SRI，否则页面装载器校验失败而降级）。"""
    want = integrity_of(blob_body)
    if 'data-integrity="' in tag_attrs:
        return re.sub(r'data-integrity="[^"]*"', f'data-integrity="{want}"', tag_attrs)
    return tag_attrs + f' data-integrity="{want}"'


def decode_blob(blob_body: str):
    """数据块正文（折行 base64）→ JSON 对象。任一步失败抛异常。"""
    raw = base64.b64decode(re.sub(r"\s+", "", blob_body))
    return json.loads(gzip.decompress(raw).decode("utf-8"))


def read_text(p):
    return p.read_text(encoding="utf-8")


def write_text(p, s):
    # UTF-8 无 BOM、LF
    p.write_bytes(s.replace("\r\n", "\n").encode("utf-8"))


def load_catalog():
    if not CATALOG.exists():
        sys.exit(f"错误：catalog 不存在：{CATALOG}")
    try:
        data = json.loads(read_text(CATALOG))
    except json.JSONDecodeError as e:
        sys.exit(f"错误：catalog 非法 JSON：{e}")
    if not isinstance(data.get("persons"), list) or len(data["persons"]) == 0:
        sys.exit("错误：catalog.persons 缺失或为空")
    if not isinstance(data.get("refs"), dict):
        sys.exit("错误：catalog.refs 缺失或非对象")
    return data


def sync_meta_triple(html: str) -> str:
    """同步 og:description / meta description / JSON-LD additionalProperty 三处口径
    至当前 HTML 的 doc-metrics 三元组（权威口径）。2026-09-11 主理人指示接入。"""
    m = re.search(r"总卷数</span><strong[^>]*>\s*(\d+)\s*</strong>", html)
    n = re.search(r"总章数</span><strong[^>]*>\s*(\d+)\s*</strong>", html)
    s = re.search(r"总节数</span><strong[^>]*>\s*(\d+)\s*</strong>", html)
    if not (m and n and s):
        return html  # 无 doc-metrics 时不动
    triple = f"{m.group(1)} 卷 {n.group(1)} 章 {s.group(1)} 节"
    # 1) og:description
    html = re.sub(r'(<meta property="og:description" content=")\d+ 卷 \d+ 章 \d+ 节([^"]*">)',
                  lambda mm: mm.group(1) + triple + mm.group(2), html)
    # 2) meta description（含书名前缀）
    html = re.sub(r'(<meta name="description" content="[^：]*：)\d+ 卷 \d+ 章 \d+ 节',
                  lambda mm: mm.group(1) + triple, html)
    # 3) JSON-LD additionalProperty 三元组（2026-09-18 重写为逐字段替换：
    #    旧版正则要求两键之间仅有 `,`，而现序列化形态为 `},{"@type":...`，
    #    故旧版静默不命中 → 检测恒真、JSON-LD 长期停在旧口径）
    def _fix_jsonld(mm):
        blob = mm.group(2)
        for name, val in (("卷数", m.group(1)), ("章数", n.group(1)), ("节数", s.group(1))):
            blob = re.sub(
                r'("name"\s*:\s*"%s"\s*,\s*"value"\s*:\s*)\d+' % name,
                lambda x: x.group(1) + val, blob)
        return mm.group(1) + blob + mm.group(3)

    html = re.sub(r'(<script[^>]*application/ld\+json[^>]*>)(.*?)(</script>)',
                  _fix_jsonld, html, flags=re.S)
    return html


def jsonld_matches(html: str) -> bool:
    """JSON-LD 的卷/章/节三元组是否与 doc-metrics 权威三元组一致（2026-09-18 新增）。"""
    m = re.search(r"总卷数</span><strong[^>]*>\s*(\d+)\s*</strong>", html)
    n = re.search(r"总章数</span><strong[^>]*>\s*(\d+)\s*</strong>", html)
    s = re.search(r"总节数</span><strong[^>]*>\s*(\d+)\s*</strong>", html)
    j = re.search(r"<script[^>]*application/ld\+json[^>]*>(.*?)</script>", html, re.S)
    if not (m and n and s and j):
        return False
    blob = j.group(1)
    for name, val in (("卷数", m.group(1)), ("章数", n.group(1)), ("节数", s.group(1))):
        mm = re.search(r'"name"\s*:\s*"%s"\s*,\s*"value"\s*:\s*(\d+)' % name, blob)
        if not mm or mm.group(1) != val:
            return False
    return True


def cmd_check():
    data = load_catalog()
    html = read_text(INDEX)
    m = BLOB_RE.search(html)
    if not m:
        sys.exit("错误：index.html 未定位压缩数据块 opt-data-blob")
    try:
        embedded = decode_blob(m.group(2))
    except Exception as e:
        sys.exit(f"错误：数据块解码失败：{e}")
    # 比较内容字段（catalog 的 $schema/version 为源文件元数据，不在内嵌数据中）
    content_data = {k: v for k, v in data.items() if k not in ("$schema", "version")}
    content_embedded = {k: v for k, v in embedded.items() if k not in ("$schema", "version")}
    same = content_embedded == content_data
    print(f"catalog 与内嵌数据块一致性：{'✅ 一致' if same else '❌ 漂移'}")
    if not same:
        # 输出首个差异键
        for k in content_data:
            if content_embedded.get(k) != content_data[k]:
                print(f"  漂移字段：{k}（内嵌 {len(content_embedded.get(k) or []) if isinstance(content_embedded.get(k), (list, dict)) else '?'} vs catalog {len(content_data[k]) if isinstance(content_data[k], (list, dict)) else '?'}）")
                break
        print("  （运行 python embed.py 装配后重检）")
    # 元数据口径漂移检测（2026-09-11；2026-09-18 改为「内容比对」而非「可否再替换」）
    synced = sync_meta_triple(html)
    meta_ok = (synced == html) and jsonld_matches(html)
    print(f"og/meta/JSON-LD 口径同步：{'✅ 一致' if meta_ok else '❌ 漂移（embed 装配时自动修正）'}")
    # 数据块 SRI 自洽检测（2026-09-18 新增）
    sri_ok = (m.group(1)[:-2].find(f'data-integrity="{integrity_of(m.group(2))}"') != -1)
    print(f"数据块 data-integrity 自洽：{'✅ 一致' if sri_ok else '❌ 漂移（embed 装配时自动修正）'}")
    return 0 if (same and meta_ok and sri_ok) else 1


def cmd_embed():
    data = load_catalog()
    # 内嵌数据只承载内容字段（$schema/version 为源元数据）
    content = {k: v for k, v in data.items() if k not in ("$schema", "version")}
    html = read_text(INDEX)
    m = BLOB_RE.search(html)
    if not m:
        sys.exit("错误：index.html 未定位压缩数据块 opt-data-blob")
    serialized = serialize_content(content)
    body_new = encode_blob(serialized)
    tag = m.group(1)                      # '<script ...>\n'
    head, tail = tag[:-2], tag[-2:]       # head = 开标签（不含 '>'），tail = '>\n'
    new_html = html[:m.start(1)] + sync_integrity(head, body_new) + tail + body_new + html[m.end(2):]
    # 元数据口径同步（og/meta/JSON-LD）
    new_html = sync_meta_triple(new_html)
    if new_html == html:
        print("embed：无变更（catalog 与内嵌数据块已一致，幂等）")
    else:
        write_text(INDEX, new_html)
        print(f"embed：已装配（数据块正文 {len(m.group(2))} → {len(body_new)} 字符）")
    digest = hashlib.sha256(serialized.encode("utf-8")).hexdigest()
    print(f"SHA-256（序列化 DATA）：{digest[:16]}…")
    return 0


def main():
    ap = argparse.ArgumentParser(description="目录页 DATA 装配脚本")
    ap.add_argument("--check", action="store_true", help="仅检测 catalog 与内嵌 DATA 漂移")
    args = ap.parse_args()
    return cmd_check() if args.check else cmd_embed()


if __name__ == "__main__":
    sys.exit(main())
