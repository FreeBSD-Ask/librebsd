#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""embed.py — 重构2026 目录页数据装配脚本（固定脚本，规则引用）。

用途：
  把 `重构2026/data/catalog.json`（语义数据中枢）序列化后重写
  `重构2026/index.html` 的 `var DATA = {...};` 行（发布态装配）。
  单体 HTML 交付物不变：除 DATA 行外其余位零改动。
  构建幂等：同一 catalog 两次运行产物位相同（diff 为空）。

流程：
  1) 校验 catalog 结构（必需字段 + persons 数量 > 0）；
  2) 定位 index.html 的 `var DATA = ...;` 声明（正则锚定，标记块外零触碰）；
  3) 以 `json.dumps(..., ensure_ascii=False, separators=(",", ":"))` 序列化；
  4) 写回（UTF-8 无 BOM、LF）；
  5) 输出 SHA-256 摘要供 changelog 审计。

用法：
  python embed.py              # 装配（默认）
  python embed.py --check      # 仅检测 catalog 与 html 内嵌 DATA 是否一致（漂移检测）

规则依据：流程规则.md「重构大纲目录口径同步规则」→「DATA 数据完整性门禁」小节。
"""
import argparse
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

DATA_RE = re.compile(r"(var\s+DATA\s*=\s*)(\{.*?\})(;\s*(?=\n\s*var\s+\w+\s*=|$))", re.S)


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
    # 3) JSON-LD additionalProperty 三元组（2026-09-11 修复：键序允许 "name" 在 "@type" 之后，
    #    两种序列化形态均匹配；此前只匹配 @type 先行的形态导致键序不同的 JSON-LD 漏同步）
    html = re.sub(r'("name":"卷数","value":)\d+((?:,"@type":"PropertyValue")?"name":"章数","value":)\d+((?:,"@type":"PropertyValue")?"name":"节数","value":)\d+',
                  lambda mm: f'{mm.group(1)}{m.group(1)}{mm.group(2)}{n.group(1)}{mm.group(3)}{s.group(1)}', html)
    # 兼容键序「@type 先行」的旧形态
    html = re.sub(r'("@type":"PropertyValue","name":"卷数","value":)\d+(,"@type":"PropertyValue","name":"章数","value":)\d+(,"@type":"PropertyValue","name":"节数","value":)\d+',
                  lambda mm: f'{mm.group(1)}{m.group(1)}{mm.group(2)}{n.group(1)}{mm.group(3)}{s.group(1)}', html)
    return html


def cmd_check():
    data = load_catalog()
    html = read_text(INDEX)
    m = DATA_RE.search(html)
    if not m:
        sys.exit("错误：index.html 未定位 var DATA 声明")
    embedded = json.loads(m.group(2))
    # 比较内容字段（catalog 的 $schema/version 为源文件元数据，不在内嵌 DATA 中）
    content_data = {k: v for k, v in data.items() if k not in ("$schema", "version")}
    content_embedded = {k: v for k, v in embedded.items() if k not in ("$schema", "version")}
    same = content_embedded == content_data
    print(f"catalog 与内嵌 DATA 一致性：{'✅ 一致' if same else '❌ 漂移'}")
    if not same:
        # 输出首个差异键
        for k in content_data:
            if content_embedded.get(k) != content_data[k]:
                print(f"  漂移字段：{k}（内嵌 {len(content_embedded.get(k) or []) if isinstance(content_embedded.get(k), (list, dict)) else '?'} vs catalog {len(content_data[k]) if isinstance(content_data[k], (list, dict)) else '?'}）")
                break
        print("  （运行 python embed.py 装配后重检）")
    # 元数据口径漂移检测（2026-09-11）
    synced = sync_meta_triple(html)
    meta_ok = synced == html
    print(f"og/meta/JSON-LD 口径同步：{'✅ 一致' if meta_ok else '❌ 漂移（embed 装配时自动修正）'}")
    return 0 if (same and meta_ok) else 1


def cmd_embed():
    data = load_catalog()
    # 内嵌 DATA 只承载内容字段（$schema/version 为源元数据）
    content = {k: v for k, v in data.items() if k not in ("$schema", "version")}
    html = read_text(INDEX)
    m = DATA_RE.search(html)
    if not m:
        sys.exit("错误：index.html 未定位 var DATA 声明")
    serialized = json.dumps(content, ensure_ascii=False, separators=(",", ":"))
    new_html = html[:m.start(2)] + serialized + html[m.end(2):]
    # 元数据口径同步（og/meta/JSON-LD）
    new_html = sync_meta_triple(new_html)
    if new_html == html:
        print("embed：无变更（catalog 与内嵌 DATA 已一致，幂等）")
    else:
        write_text(INDEX, new_html)
        print(f"embed：已装配（DATA 段 {len(m.group(2))} → {len(serialized)} 字符）")
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
