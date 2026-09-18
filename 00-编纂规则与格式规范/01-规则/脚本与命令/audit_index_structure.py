# -*- coding: utf-8 -*-
"""重构2026 目录页结构自检门禁（固定脚本，2026-09-18 立，第七件改后必跑门禁）。

用途：对 `08-核查报告与多轮复核/重构2026/index.html` 做**不依赖浏览器**的十一项结构自检，
补足既有门禁未覆盖的维度（既有五件：口径同步 --check、节号连续性、DATA 完整性、
xref 交叉引用、视觉回归套件；第六件为大纲注入块证据等级）。

十一项判据：
  A 编码：UTF-8 无 BOM、无 CRLF、无替换字符 U+FFFD、无直角引号「」
  A2 空格形制（流程规则 L1532，2026-09-18 补入）：无全角空格 U+3000；卷题（h2）卷号与题名
     之间为 2 个半角空格；章题（h3.chapter）与节序号（span.sec-num）后有且只有 1 个半角空格
     （即不得连空两格）。设立缘由：2026-09-18 发现卷题自 2026-09-05 起长期为 U+3000 形制
     （插卷/重编号脚本模板写死），而本门禁原 A 组不检空格，规则无自动化护栏。
  B 卷：卷锚点 1..N 连续唯一；卷题中文序数与锚点一致
  C 章：每卷章号 1..K 连续唯一；章题「第 M 章」与锚点一致；章题全局唯一
  D 节：每章节号 M.1..M.k 连续；节题非空（src 注不计入题文）
  E 述评恒末：**若有**「本章书目述评」节须居章末（与 audit_sequence_continuity.py 同规）；
    27 号文「有则设、无则不设」→ 不以「每章必有述评」为判据，无述评的正章仅列参考
  F 口径：doc-metrics ／ og:description ／ meta description ／ footer ／ JSON-LD ／ 实测 六处一致
  G 标签平衡：section／ul／li／span／h3／h2／div／p 开闭标签数相等
  H 锚点唯一性与站内链接可达性（排除 JS 拼接模板：含 `'` 或 `+` 的 href）
  I 统计小字自洽：doc-metrics 小字「正章 N ＋ 卷末书目述评章 M」与实测相符
  J 内容层 class ↔ 格式层选择器（2026-09-18 补入）：内容层／页壳静态标记所用 class 须在
     `assets/doc.css`／`assets/modern.css` 中有对应规则。设立缘由：`.doc-foot`（四层解耦提取器
     守卫被 `.doc-footer` 子串误命中而漏写）与 `.vol-note`（长期无规则、以正文全尺寸渲染）
     两类缺陷均因「class 无定义」而以默认样式静默渲染，门禁与浏览器回归皆未捕获

触发条件：**目录页结构变动后必跑**（增删卷／章／节、改口径、改述评挂靠、结构重编号）。
0 异常即通过（exit 0），有异常 exit 1。

用法：
  python audit_index_structure.py                 # 默认审计标准路径的 index.html
  python audit_index_structure.py --path <file>   # 指定文件（如备份件交叉验证）
"""
import argparse
import io
import json
import re
import sys

DEFAULT = r"D:/librebsd/08-核查报告与多轮复核/重构2026/index.html"
CN = "零一二三四五六七八九"


def cn2int(s):
    if s == "十":
        return 10
    if s.startswith("十"):
        return 10 + CN.index(s[1])
    if "十" in s:
        a, b = s.split("十")
        return CN.index(a) * 10 + (CN.index(b) if b else 0)
    return CN.index(s)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", default=DEFAULT, help="index.html 路径")
    args = ap.parse_args()
    P = args.path

    raw = io.open(P, "rb").read()
    bad = []
    if raw.startswith(b"\xef\xbb\xbf"):
        bad.append("含 UTF-8 BOM")
    if b"\r\n" in raw:
        bad.append("含 CRLF")
    h = raw.decode("utf-8")
    if "\ufffd" in h:
        bad.append("含替换字符 U+FFFD")
    n_corner = h.count("\u300c") + h.count("\u300d") + h.count("\u300e") + h.count("\u300f")
    if n_corner:
        bad.append(f"含直角/白角引号 {n_corner} 处")
    print("A 编码:", "PASS" if not bad else "FAIL " + "; ".join(bad))

    # A2 空格形制（流程规则 L1532，2026-09-09 主理人裁定；2026-09-18 补入门禁）：
    #   禁用全角空格 U+3000；卷题（h2）卷号与题名之间用 2 个半角空格；
    #   章题（h3.chapter）与节序号（span.sec-num）后有且只有 1 个半角空格。
    sp_bad = []
    n_u3000 = h.count("\u3000")
    if n_u3000:
        sp_bad.append(f"含全角空格 U+3000 {n_u3000} 处（禁用；卷题应用 2 个半角空格）")
    h2_static = [
        t for t in re.findall(r"<h2>(.*?)</h2>", h, re.S) if "'" not in t and "+" not in t
    ]
    bad_vt = [t[:18] for t in h2_static if not re.match(r"^第[一二三四五六七八九十]+卷  \S", t)]
    if bad_vt:
        sp_bad.append(
            f"卷题形制异常 {len(bad_vt)} 处（应「第N卷」＋2 个半角空格＋题名）：{bad_vt[:3]}"
        )
    n_ch_ok = len(re.findall(r'<h3 class="chapter" id="vol-\d+-ch-\d+">第 \d+ 章 [^<]', h))
    n_ch_all = len(re.findall(r'<h3 class="chapter" id="vol-\d+-ch-\d+">', h))
    if n_ch_ok != n_ch_all:
        sp_bad.append(
            f"章题形制异常 {n_ch_all - n_ch_ok} 处（应「第 N 章」＋1 个半角空格＋题名）"
        )
    n_dbl = len(re.findall(r"</span>  ", h)) + len(re.findall(r"章  [^<]", h))
    if n_dbl:
        sp_bad.append(f"序号或章题后连空两格 {n_dbl} 处（应有且只有 1 个半角空格）")
    print(
        "A2 空格形制:",
        "PASS" if not sp_bad else "FAIL " + "; ".join(sp_bad),
        f"（卷题 {len(h2_static)} 处／章题 {n_ch_all} 处／U+3000 {n_u3000} 处）",
    )

    vols = []
    for m in re.finditer(
        r'<section class="doc-block" id="(vol-\d+)" role="doc-part">\s*<h2>(.*?)</h2>', h, re.S
    ):
        vols.append((m.group(1), re.sub(r"<[^>]+>", "", m.group(2)).strip(), m.start()))
    vols.append(("END", "", len(h)))
    vno = [int(v[0].split("-")[1]) for v in vols[:-1]]
    okB = vno == list(range(1, len(vno) + 1))
    vtitle_bad = []
    for i, (vid, t, _) in enumerate(vols[:-1]):
        m = re.match(r"^第([一二三四五六七八九十]+)卷[　\s]*(.*)$", t)
        if not m or cn2int(m.group(1)) != i + 1:
            vtitle_bad.append(t)
    print(f"B 卷: 锚点 {len(vno)} 个，1..{len(vno)} 连续唯一 ? {okB} | 卷题序数不符 {len(vtitle_bad)}")
    for t in vtitle_bad:
        print("   ❌", t)

    ch_total = 0
    ch_bad, sec_bad, bib_bad, dup_ch, bib_none = [], [], [], [], []
    seen_ch = {}
    sec_total = src_total = 0
    for i, (vid, vt, st) in enumerate(vols[:-1]):
        seg = h[st : vols[i + 1][2]]
        chs = re.findall(
            r'<h3 class="chapter" id="([^"]+)">(.*?)</h3>\s*<ul class="sections">(.*?)</ul>',
            seg,
            re.S,
        )
        nums = [int(re.search(r"ch-(\d+)$", c[0]).group(1)) for c in chs]
        if nums != list(range(1, len(chs) + 1)):
            ch_bad.append((vid, nums))
        for cid, ct, raw_ul in chs:
            ch_total += 1
            cn_ = int(re.search(r"ch-(\d+)$", cid).group(1))
            t = re.sub(r"<[^>]+>", "", ct).strip()
            m = re.match(r"^第\s*(\d+)\s*章\s*(.*)$", t)
            if not m or int(m.group(1)) != cn_:
                ch_bad.append((cid, t))
            if t in seen_ch:
                dup_ch.append((t, seen_ch[t], cid))
            seen_ch[t] = cid
            lis = re.findall(r"<li>(.*?)</li>", raw_ul, re.S)
            snums = []
            for li in lis:
                sec_total += 1
                sm = re.search(r'<span class="sec-num">([\d.]+)</span>(.*)$', li, re.S)
                if not sm:
                    sec_bad.append((cid, li[:60]))
                    continue
                snums.append(sm.group(1))
                rest = re.sub(r'<span class="src">.*?</span>', "", sm.group(2), flags=re.S)
                if not re.sub(r"<[^>]+>", "", rest).strip():
                    sec_bad.append((cid, "空节题 " + sm.group(1)))
                if 'class="src"' in li:
                    src_total += 1
            want = [f"{cn_}.{k}" for k in range(1, len(lis) + 1)]
            if snums != want:
                sec_bad.append((cid, f"{snums} != {want}"))
            txts = [re.sub(r"<[^>]+>", "", x) for x in lis]
            last = txts[-1].strip() if txts else ""
            has_bib = any("本章书目述评" in x for x in txts)
            if has_bib and "本章书目述评" not in last:
                bib_bad.append((cid, last[:40]))
            elif not has_bib and "卷末书目述评" not in t:
                _lt = re.sub(
                    r'<span class="src">.*?</span>', "", lis[-1], flags=re.S
                )
                bib_none.append((cid, re.sub(r"<[^>]+>", "", _lt).strip()[:40]))
    print(f"C 章: 共 {ch_total} 章 | 卷内章号异常 {len([x for x in ch_bad if isinstance(x[1], list)])} 卷 |"
          f" 章题/锚点异常 {len([x for x in ch_bad if not isinstance(x[1], list)])} | 重题 {len(dup_ch)}")
    for x in ch_bad[:10]:
        print("   ❌", x)
    for x in dup_ch[:5]:
        print("   ❌ 重题", x)
    print(f"D 节: 共 {sec_total} 节（含 src 注 {src_total}）| 异常 {len(sec_bad)}")
    for x in sec_bad[:10]:
        print("   ❌", x)
    print(f"E 述评恒末（若有述评须居末）: 异常 {len(bib_bad)}")
    for x in bib_bad[:10]:
        print("   ❌", x)
    print(f"   参考：无「本章书目述评」节的正章 {len(bib_none)} 个（合 27 号文「有则设、无则不设」，不计异常）")
    for x in bib_none[:6]:
        print("     ·", x[0], x[1])

    dm = re.search(r'<span>总卷数</span><strong>(\d+)</strong>', h)
    dmc = re.search(r'<span>总章数</span><strong>(\d+)</strong>', h)
    dms = re.search(r'<span>总节数</span><strong>(\d+)</strong>', h)
    og = re.search(r'og:description" content="(\d+) 卷 (\d+) 章 (\d+) 节', h)
    md = re.search(r'name="description" content="[^"]*?(\d+) 卷 (\d+) 章 (\d+) 节', h)
    ft = re.search(r'现行大纲目录 · (\d+) 卷 (\d+) 章 (\d+) 节', h)
    jl = json.loads(
        re.search(r'<script type="application/ld\+json"[^>]*>(.*?)</script>', h, re.S).group(1)
    )
    jap = {x["name"]: x["value"] for x in jl["additionalProperty"]}
    measured = (len(vno), ch_total, sec_total)
    got = {
        "doc-metrics": (int(dm.group(1)), int(dmc.group(1)), int(dms.group(1))),
        "og": tuple(map(int, og.groups())),
        "meta": tuple(map(int, md.groups())),
        "footer": tuple(map(int, ft.groups())),
        "JSON-LD": (jap["卷数"], jap["章数"], jap["节数"]),
        "实测": measured,
    }
    okF = all(v == measured for v in got.values())
    print("F 口径六处:", "PASS" if okF else "FAIL", got)

    tags = {}
    for t in ("section", "ul", "li", "span", "h3", "div", "h2", "p"):
        tags[t] = (len(re.findall(rf"<{t}[\s>]", h)), h.count(f"</{t}>"))
    print("G 标签平衡:", {k: v for k, v in tags.items() if v[0] != v[1]} or "全部平衡")

    ids = re.findall(r'\sid="([^"]+)"', h)
    dupids = {x for x in ids if ids.count(x) > 1}
    hrefs = set(re.findall(r'href="#([^"]+)"', h))
    static_hrefs = {x for x in hrefs if "'" not in x and "+" not in x}
    miss = sorted(x for x in static_hrefs if x not in set(ids))
    print(f"H 锚点: 共 {len(ids)} 个，重复 {len(dupids)} {sorted(dupids)[:5]} |"
          f" 静态站内链接 {len(static_hrefs)} 条，悬空 {len(miss)} {miss[:8]}")

    small = re.findall(r"<small>(.*?)</small>", h)
    print("I doc-metrics 小字:", small)
    n_bibch = sum(1 for t in seen_ch if "卷末书目述评" in t)
    print(f"   卷末书目述评章 {n_bibch} 个；正章 {ch_total - n_bibch} 个；vol-note 分工注 {h.count('class=\"vol-note\"')} 个")

    # ── J 内容层 class ↔ 格式层选择器（2026-09-18 补入）─────────────────────
    # 缘由：.doc-foot（四层解耦提取器守卫被 .doc-footer 子串误命中而漏写）与 .vol-note
    # （长期无规则、以正文全尺寸渲染）两类缺陷均因「class 无定义」而以默认样式静默渲染，
    # 门禁与浏览器回归皆未捕获。判「某规则是否已存在」须用词边界，禁用裸子串 in。
    import os as _os
    _base = _os.path.dirname(_os.path.abspath(P))
    css_all = ""
    for _f in ("assets/doc.css", "assets/modern.css"):
        _p = _os.path.join(_base, _f)
        if _os.path.exists(_p):
            css_all += io.open(_p, encoding="utf-8").read() + chr(10)
    _masked = re.sub(r"<(script|style)[^>]*>.*?</\1>",
                     lambda m: " " * len(m.group(0)), h, flags=re.S | re.I)
    static_cls = set()
    for _m in re.finditer('class="([^"]+)"', _masked):
        static_cls.update(_m.group(1).split())
    undef = sorted(c for c in static_cls
                   if not re.search(re.escape("." + c) + r"(?![\w-])", css_all))
    print("J 内容层 class ↔ 格式层: %d 个 class，未定义 %d %s"
          % (len(static_cls), len(undef), undef[:8]))

    allbad = (
        bad
        or sp_bad
        or (not okB)
        or vtitle_bad
        or ch_bad
        or sec_bad
        or bib_bad
        or (not okF)
        or dupids
        or miss
        or undef
    )
    print("\n总判定:", "FAIL" if allbad else "PASS")
    return 1 if allbad else 0


if __name__ == "__main__":
    sys.exit(main())
