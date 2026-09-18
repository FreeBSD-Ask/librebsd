# -*- coding: utf-8 -*-
"""
font_subset_rebuild.py — 目录页字体子集重建与 cmap 审计（重构2026）

用途：
    目录页 `08-核查报告与多轮复核/重构2026/index.html` 内嵌霞鹜文楷字体按
    「页面可见字符集」精确子集化（2026-09-12 起）。大纲内容增改引入新汉字后，
    新字将回退系统字体（渲染不破但字体不齐）。本脚本从完整字体源重建子集并写回。

🔴 四层解耦前提（2026-09-18 起）：
    - 字符集**扫描**对象仍是 `index.html`（装配产物，含正文与 src 注文），
      并**追加** `data/catalog.json` 的字符串值（浮层人物/文献文本；解耦后
      浮层数据已不再内联为页面里的 `var DATA`）；
    - 新 `@font-face` **写回格式层** `assets/doc.css`——`index.html` 是装配产物，
      唯一写者为 `assemble_index.py`，**直接写 index.html 会被下次装配回退**。
      故本脚本写回后**必须再跑一次** `python assemble_index.py`。

流程（改后必跑）：
    1. 扫描 index.html 可见文本 ＋ data/catalog.json 字符串值，提取字符集；
    2. 从完整字体源（LXGW WenKai Screen webfont tgz）合并全部子集分片；
    3. 按页面字符集子集化（fonttools），输出单片 woff2；
    4. 写回 `assets/doc.css`（替换现有 @font-face 块；40 片 → 1 片，font-display:swap）；
    5. cmap 审计：报告「页面用字中字体缺失」清单，逐字区分
       「源字体本无（系统 fallback，允许）」与「源字体有但重建丢失（回归，禁止）」。

前置：
    - fonttools + brotli（venv：C:/Users/ykla/.workbuddy/binaries/python/envs/default）
    - 字体源 tgz：script/_font_embed_20260905/lxgw-wenkai-screen-webfont-1.7.0.tgz
      （若缺失，从 git 历史或字体包重新获取，路径常量在本文件顶部）

用法：
    python font_subset_rebuild.py            # 重建并写回 assets/doc.css（随后须重新装配）
    python font_subset_rebuild.py --check    # 仅审计，不写回

规则索引：本脚本登记于 01-规则/README.md（固定脚本）。
"""
import argparse
import base64
import io
import os
import re
import sys
import tarfile
import tempfile

# ===== 路径常量（机器固定值，迁移时同步更新）=====
INDEX_HTML = r'D:/librebsd/08-核查报告与多轮复核/重构2026/index.html'
DOC_CSS = r'D:/librebsd/08-核查报告与多轮复核/重构2026/assets/doc.css'
DOC_JS = r'D:/librebsd/08-核查报告与多轮复核/重构2026/assets/doc.js'
THEME_JS = r'D:/librebsd/08-核查报告与多轮复核/重构2026/assets/theme-preset.js'
CATALOG_JSON = r'D:/librebsd/08-核查报告与多轮复核/重构2026/data/catalog.json'
FONT_SOURCE_TGZ = r'D:/librebsd/script/_font_embed_20260905/lxgw-wenkai-screen-webfont-1.7.0.tgz'
FONT_FAMILY = 'LXGW WenKai Screen'

from fontTools.merge import Merger
from fontTools.subset import Subsetter, Options
from fontTools.ttLib import TTFont


def load_index():
    with open(INDEX_HTML, encoding='utf-8') as f:
        return f.read()


def extract_visible_chars(src):
    """提取页面全部可见字符（body 非脚本/样式文本 + 浮层数据文本）。

    2026-09-18（四层解耦后）：浮层数据已不再内联为页面里的 `var DATA`，
    而是 `data/catalog.json` → gzip+base64 blob。故浮层文本改从内容源
    `data/catalog.json` 的**字符串值**取（人物名、著录、述评等）。
    """
    # body 可见文本
    body_start = src.find('<body')
    body_end = src.find('</body>', body_start)
    body = src[body_start:body_end]
    body = re.sub(r'<script[^>]*>.*?</script>', '', body, flags=re.S)
    body = re.sub(r'<style[^>]*>.*?</style>', '', body, flags=re.S)
    text = re.sub(r'<[^>]+>', '', body)
    chars = set(text)
    # 浮层数据可见文本（人物浮层 / 文献浮层）
    if os.path.exists(CATALOG_JSON):
        import json as _json
        with open(CATALOG_JSON, encoding='utf-8') as f:
            cat = _json.load(f)

        def _vals(o):
            if isinstance(o, str):
                yield o
            elif isinstance(o, dict):
                for v in o.values():
                    yield from _vals(v)
            elif isinstance(o, list):
                for v in o:
                    yield from _vals(v)

        for s in _vals(cat):
            chars |= set(s)
    # 行为层/现代化层源码中的字面量（JS 生成的 UI 文案也会上屏；
    # 整文件取字符为安全超集——代码字符皆 ASCII，已在正文集内）
    for extra in (DOC_JS, THEME_JS):
        if os.path.exists(extra):
            with open(extra, encoding='utf-8') as f:
                chars |= set(f.read())
    # 过滤控制字符与 JSON 语法字符（不可见）
    valid = [c for c in sorted(chars)
             if ord(c) >= 0x20 and not (0x7f <= ord(c) < 0xa0)
             and c not in '"\\{}[]:,.']
    return valid


def load_full_font_slices(tgz_path, tmpdir):
    """从字体源 tgz 解出全部子集分片 woff2 的临时路径列表。"""
    paths = []
    with tarfile.open(tgz_path) as t:
        members = [m for m in t.getnames()
                   if m.endswith('.woff2') and 'files/' in m]
        for i, m in enumerate(members):
            data = t.extractfile(m).read()
            p = os.path.join(tmpdir, 'slice_%d.woff2' % i)
            with open(p, 'wb') as f:
                f.write(data)
            paths.append(p)
    return paths


def merge_and_subset(paths, chars):
    """合并全部子集分片 → 按 chars 子集化 → 返回 woff2 字节。
    2026-09-12 优化：先过滤只含目标字符的片再合并（388 片全合并导致
    glyf 表 2.6 MB 冗余——大部分片不含页面用字），合并后子集化。"""
    target = set(ord(c) for c in chars)
    # 预扫描每片 cmap，仅保留含目标字符的片
    used_paths = []
    for p in paths:
        tt = TTFont(p)
        cmap = tt.getBestCmap()
        if any(cp in cmap for cp in target):
            used_paths.append(p)
    print('    过滤后使用片数: %d / %d' % (len(used_paths), len(paths)))
    if not used_paths:
        raise ValueError('无字体片覆盖目标字符集，字体源异常')
    merger = Merger()
    master = merger.merge(used_paths)
    options = Options()
    options.flavor = 'woff2'
    options.name_IDs = [1, 2, 4, 6]
    options.notdef_outline = True
    options.recalc_bounds = True
    options.drop_tables += ['FFTM']
    # 2026-09-12：中文正文不需要连字/变体布局特性。保留 GSUB/GPOS 会连带
    # 保留数千孤儿替换 glyph（实测 4789 个，glyf 2.6 MB）。布局表连同孤儿
    # glyph 一并丢弃，仅保留 cmap 直映 glyph。
    options.layout_features = []
    options.drop_tables += ['GSUB', 'GPOS', 'GDEF']
    sub = Subsetter(options=options)
    sub.populate(text=''.join(chars))
    sub.subset(master)
    out = io.BytesIO()
    master.flavor = 'woff2'
    master.save(out)
    return out.getvalue()


def audit_cmap(new_font_bytes, chars, orig_cmap):
    """cmap 审计：区分源字体本无（允许）与重建丢失（回归）。"""
    tt = TTFont(io.BytesIO(new_font_bytes))
    new_cmap = tt.getBestCmap()
    missing = [c for c in chars if ord(c) not in new_cmap]
    regress = [c for c in missing if ord(c) in orig_cmap]
    fallback_ok = [c for c in missing if ord(c) not in orig_cmap]
    return missing, regress, fallback_ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true', help='仅审计不写回')
    args = ap.parse_args()

    src = load_index()
    chars = extract_visible_chars(src)
    print('[1/5] 页面可见字符集:', len(chars), '字')

    if not os.path.exists(FONT_SOURCE_TGZ):
        print('错误：字体源 tgz 缺失:', FONT_SOURCE_TGZ)
        print('请从 git 历史或 LXGW WenKai Screen 字体包恢复后再运行。')
        sys.exit(1)

    tmpdir = tempfile.mkdtemp()
    try:
        paths = load_full_font_slices(FONT_SOURCE_TGZ, tmpdir)
        print('[2/5] 字体源分片:', len(paths), '片')

        # 源字体 cmap（合并全部片，用于回归判定）
        orig_cmap = {}
        for p in paths:
            tt = TTFont(p)
            orig_cmap.update(tt.getBestCmap())
        print('[3/5] 源字体字符覆盖:', len(orig_cmap), '字')

        new_bytes = merge_and_subset(paths, chars)
        print('[4/5] 子集化 woff2:', round(len(new_bytes) / 1024, 1), 'KB')

        missing, regress, fallback_ok = audit_cmap(new_bytes, chars, orig_cmap)
        print('[5/5] cmap 审计:')
        print('  页面用字缺失:', len(missing))
        if regress:
            print('  ❌ 回归（源有但重建丢失，禁止写回）:', ''.join(regress))
            sys.exit(1)
        if fallback_ok:
            print('  ⚠ 源字体本无（系统 fallback，允许）:', len(fallback_ok), '字')
            print('    ', ''.join(fallback_ok[:60]))
        else:
            print('  ✅ 无缺失')
    finally:
        import shutil
        shutil.rmtree(tmpdir, ignore_errors=True)

    if args.check:
        print('--check 模式：审计完成，未写回。')
        return

    # 写回格式层（2026-09-18 四层解耦后：@font-face 块位于 assets/doc.css；
    # 不再写 index.html——index.html 是装配产物，唯一写者为 assemble_index.py）
    new_b64 = base64.b64encode(new_bytes).decode('ascii')
    # 2026-09-12 主理人裁定：font-display 固定 swap——文字立即以系统字体可见，
    # 字体就绪后必须切换为霞鹜文楷（optional 会在 100ms 窗口后永久回退系统
    # 字体，不符合「最终必须加载新字体」要求）
    new_face = ('@font-face{font-family:"%s";font-style:normal;font-weight:400;'
                'font-display:swap;src:url(data:font/woff2;base64,%s)}'
                % (FONT_FAMILY, new_b64))
    with open(DOC_CSS, encoding='utf-8') as f:
        css = f.read()
    n_old = css.count('@font-face')
    start = css.find('@font-face')
    end = css.rfind('@font-face')
    end = css.find('}', end) + 1
    if start < 0 or end <= start:
        print('错误：assets/doc.css 中未找到 @font-face 块。')
        sys.exit(1)
    out = css[:start] + new_face + css[end:]
    if out.count('@font-face') != 1:
        print('错误：替换后 @font-face 数 != 1（%d）——跨度内混入其它规则，已中止。'
              % out.count('@font-face'))
        sys.exit(1)
    with open(DOC_CSS, 'w', encoding='utf-8', newline='\n') as f:
        f.write(out)
    print('已写回 assets/doc.css：%d 个 face → 1 个；%d → %d 字节（−%.2f MB）'
          % (n_old, len(css.encode('utf-8')), len(out.encode('utf-8')),
             (len(css) - len(out)) / 1048576))
    print('  下一步：python assemble_index.py 重新装配 index.html')


if __name__ == '__main__':
    main()
