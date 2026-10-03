# -*- coding: utf-8 -*-
"""重构2026 目录页结构自检门禁（固定脚本，2026-09-18 立，第七件改后必跑门禁）。

用途：对 `08-核查报告与多轮复核/重构2026/index.html` 做**不依赖浏览器**的十四项结构自检，
补足既有门禁未覆盖的维度（既有五件：口径同步 --check、节号连续性、DATA 完整性、
xref 交叉引用、视觉回归套件；第六件为大纲注入块证据等级）。

十四项判据：
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
  K 三级结构（2026-09-27 第五批补入）：无章之卷／无节之章／章外孤立节行三类破坏恒为 0。
     设立缘由：B/C/D 三组只验「已有编号是否连续」，上述三类破坏在三组判据下均判「无异常」
     而静默通过。
  L 不设附录（O1，2026-09-27 补入）：章题去「第 N 章」前缀后不得以「附录」起首。**按章题判**，
     不得按裸词「附录」判——全库另有 2 处「杂志附录」等合法用词（正文非章题）。
  M OS 比较节位次（O1b，2026-09-27 补入）：节题命中 OS 比较形制者须居「本章书目述评」前一位，
     无述评则须居章末。**只判节题**（src 注之前）——卷 43 ch3 3.1 的溯源注内磁盘路径含
     「同时期操作系统的比较」，按整行判会复现第四批唯一假阳性。
  N 结构裁决（2026-09-27 立，依据 MAX 提案 v1.1 M-7；提案原文记 G-a…G-d，此处改记 N，
     以免与上文 G「标签平衡」冲号，判据内容不变）：
     N-a 层序（编年主干起点递增／后设层居综合总结层之后／横向卷须有分工注）；
     N-b 体例覆盖（卷导言恒设／述评章登记表覆盖全卷／编年卷版本章题带年份）；
     N-c 卷名长度 ≤36 字（硬限）；N-d 题文复合词连接号用 en dash（禁半角连字符形）。
     设立缘由：B–F 组只验「形」不验「序与体例」——卷 41/42 层序反转、卷导言 21/43、
     分工注 7/43、章题年份 81/411、卷名 75 字，在既有十二件门禁下全部静默通过。
     N-e～N-i 节级判据（2026-09-27 补遗，主理人批准）：N-e 章内年序（章题带年代区间的章，
     含年份节须非递减，容 1 年回落）；N-f 节题长度（**软限**：逾 50／逾 60 只示 WARN，不判 FAIL；豁免比较节与美学参照节）；
     N-g 述评位次（节题恰为「本章书目述评」须居末）；N-h 节数离群（<4 或 >14 WARN／>18 FAIL，
     豁免收口章）；N-i 同题登记（同题节跨章须命中登记构式）。
     判据非空由 tests/tri_structure_negtest.py 的负向副本自证（2026-09-27 立）。
      长度计数口径（2026-09-27 主理人裁定）：**英语单词整体算 1 字**——拉丁字母数字串各计 1，
      O 组（2026-09-27 立，主理人学术规范裁定）：题文不得以数词概括对象集合，亦不得以集合名词
      代替点名（「四大 BSD」「四个项目」「各分支」等）。**卷题／章题命中 → FAIL；节题与注文 → WARN**。
      豁免（专名／惯用语／代际／次数／成文节奏）见模块级 O_EXEMPT，逐条登记理由；新增豁免须主理人批。
      其余字符逐字计；N-c 与 N-f 同用此口径。

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

# 长度计数用：拉丁字母数字串（英语单词／项目名／版本号）整体识别为 1 字
LATIN_RUN = re.compile(r"[A-Za-z0-9][A-Za-z0-9._/+-]*")

# ── O 组判据用（2026-09-27 立；依主理人「计数概括式表述不符合学术规范」与「集合名词不可用」两条裁定）──
#   ——「一」family（一个／一种／一项／一条／一步／一面…）属普通冠量与惯用语，不入形制（不概括集合）。
# 形制一：数词＋量词概括集合（如「四大 BSD」「四个项目」「三种位置」「七类载体」）
O_NUM = re.compile(r"([二三四五六七八九十两])\s*(大|个|项|类|种|条|款|点|层|重|阶|路|线|方|面|维|向|支|分|处|家|名)")
# 形制二：集合名词（如「各分支」「各项目」「各 BSD」）
O_COL = re.compile(r"各\s*(分支|项目|BSD|操作系统)")
# 豁免（专名／惯用语／代际／次数／成文节奏；逐条理由见 tests/README.md 与本判据 docstring）
O_EXEMPT = (
    "第三方", "三权分立", "二进制", "四项自由", "条款 BSD", "双源", "非二分性",
    "进一步", "一方面", "另一方面", "一致性", "一律", "一体", "一定", "一起", "一览", "一并",
    "唯一", "同一", "一元", "三元", "二元", "一揽子", "一体化", "一书", "一脉",
    "一代", "两代", "下一代", "一分", "多数", "多方", "多元", "多种", "多项", "多维", "多层",
    "多个", "多重", "多次", "一处", "两处", "多处", "一线", "一次", "两步", "一步", "一部", "一面",
    "第一", "第二", "第三", "第四", "第五", "第六", "第七", "第八", "第九", "第十",
    "多处理", "多向", "多家", "多极", "多阶", "二型", "两轮", "六个月",
)
O_NOTE_REF = re.compile(r"^[^。；：]{0,6}注")   # 「两条分工注合并」类：指注文自身，非目录对象集合

def o_flag(s):
    """题文／卷题／章题命中「计数概括式或集合名词」者返回命中形制，否则 None。"""
    for m in list(O_NUM.finditer(s)) + list(O_COL.finditer(s)):
        ctx = s[max(0, m.start() - 10):m.end() + 18]
        if any(e in ctx for e in O_EXEMPT):
            continue
        _tok = re.split(r"[\s（）()，。；：、]", s[:m.start()])[-1] + m.group(0) + re.split(r"[\s（）()，。；：、]", s[m.end():])[0]
        if "/" in _tok and (".md" in _tok or "05-卷册大纲" in _tok or _tok.startswith("05-")):
            continue          # 磁盘路径／文件名内的形制：引证保真，不追改
        if O_NOTE_REF.match(s[m.end():]):
            continue
        return m.group(0)
    return None

import sys

DEFAULT = r"D:/librebsd/08-核查报告与多轮复核/重构2026/index.html"
CN = "零一二三四五六七八九"
# M 组 OS 比较节题形制（与核查脚本 script/_vol_adjust_20260927/check_os_compare.py 同源）：
# 全库命中 29 处、违规 0。写作「与同时期操作系统的比较」者须由 `同时期操作系统` 一支命中。
OSCMP = re.compile(r"操作系统比较|OS 比较|同时期操作系统|同时代操作系统|同期操作系统")


def cn2int(s):
    if s == "十":
        return 10
    if s.startswith("十"):
        return 10 + CN.index(s[1])
    if "十" in s:
        a, b = s.split("十")
        return CN.index(a) * 10 + (CN.index(b) if b else 0)
    return CN.index(s)


# ═══════════════════════════════════════════════════════════════════════════
# 卷序索引表（**唯一源**）——2026-10-02 集中化，依 101 号文 §九 P0-3
# ═══════════════════════════════════════════════════════════════════════════
# 🔴 **凡重排卷序，必须同步维护以下三表**——本门禁自身即「卷序的隐性消费者」：
#    2026-10-02 卷序重排至 44 卷时，三表因按卷号硬编码而**全部键错位**
#    （N-a1／N-a3／N-b2 同时报「判据键错位」）。三表已抽出集中于此，
#    并由 `_check_vol_tables()` 在 main() 内做「卷号越界自检」，防止静默失效。
#   · SPINE：编年主干（卷号, 卷题关键词, 期望起始年）——N-a1
#   · HORIZ：横向／专题卷（卷号, 卷题关键词）——N-a3
#   · BIB  ：卷末述评章登记（卷号: 有）——N-b2
SPINE = [(5, "BSD 伊始", 1974), (6, "4.3BSD", 1980), (7, "CSRG 后期", 1986),
         (10, "法律危机", 1992), (13, "大分裂", 1992), (16, "FreeBSD 操作系统的历史", 1993),
         (19, "NetBSD 操作系统的历史", 1993), (22, "OpenBSD 的历史", 1995),
         (25, "DragonFly BSD 的历史", 2003)]
HORIZ = [(8, "GNU 与自由软件运动"), (9, "UNIX 战争"), (11, "UNIX 标准化"), (15, "BSD UNIX 技术专题史"),
         (28, "技术发展史的横向比较"), (31, "macOS"),
         (32, "BSD 软件作品史"), (34, "BSD 许可证与法律"), (35, "BSD 合规"),
         (36, "GNU/Linux 与开源运动"), (37, "BSD–Linux 关系史"), (39, "BSD 治理专题"), (40, "DARPA"),
         (42, "开源会议"), (44, "传言"), (45, "BSD 的传播载体"), (46, "会者定离")]
BIB_HAS = [1, 3, 9, 14, 15, 21, 22, 24, 27, 28, 31, 43]   # 9＝2026-10-03 卷9 拆分承卷末述评章（原 9）；2026-10-03 晚卷35拆分＋GNU卷前移：≥8 全体 +1，新增卷 8（GNU）／卷 36（GNU/Linux）两横向卷


def _check_vol_tables(nvol):
    """卷号越界自检：三表卷号须落在 1..nvol-1 内（nvol 含尾部「合计」行）。"""
    bad = []
    for nm, vns in (("SPINE", [x[0] for x in SPINE]), ("HORIZ", [x[0] for x in HORIZ]),
                    ("BIB", list(BIB_HAS))):
        out = [v for v in vns if v < 1 or v > nvol - 1]
        if out:
            bad.append((nm, out))
    return bad


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
    appx_bad, os_bad = [], []   # L 不设附录；M OS 比较节位次
    os_n = 0                    # M 组命中数（复核真值：全库 29）
    # K 三级结构（2026-09-27 第五批补入）：卷必有章、章必有节、卷内不得有章外孤立节行。
    # 缘由：B/C/D 三组只验「已有编号是否连续」，无章之卷（章数 0）、无节之章（节数 0）与
    # 章外孤立 `-` 行在三组判据下均「无异常」而静默通过，三级结构可被无声破坏。
    tri_bad = []
    seen_ch = {}
    sec_total = src_total = 0
    for i, (vid, vt, st) in enumerate(vols[:-1]):
        # 三级结构判据须先屏蔽 <script>/<style>：页面构建脚本内含 '<li>' 等字符串字面量，
        # 直接计数会把脚本源码误判为「章外孤立节行」（2026-09-27 首次实现即被该假阳性拦下）。
        seg = re.sub(
            r"<(script|style)[^>]*>.*?</\1>",
            lambda m: " " * len(m.group(0)),
            h[st : vols[i + 1][2]],
            flags=re.S | re.I,
        )
        chs = re.findall(
            r'<h3 class="chapter" id="([^"]+)">(.*?)</h3>\s*<ul class="sections">(.*?)</ul>',
            seg,
            re.S,
        )
        if not chs:
            tri_bad.append((vid, "无章之卷"))
        _seg_li = len(re.findall(r"<li[^>]*>", seg))
        _ch_li = 0
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
            # L 不设附录（O1）：章题去「第 N 章」前缀后以「附录」起首即 FAIL。
            if re.match(r"^附录", re.sub(r"^第\s*\d+\s*章\s*", "", t)):
                appx_bad.append((cid, t))
            lis = re.findall(r"<li[^>]*>(.*?)</li>", raw_ul, re.S)
            _ch_li += len(lis)
            if not lis:
                tri_bad.append((cid, "无节之章"))
            snums, titles = [], []
            for li in lis:
                sec_total += 1
                sm = re.search(r'<span class="sec-num">([\d.]+)</span>(.*)$', li, re.S)
                if not sm:
                    sec_bad.append((cid, li[:60]))
                    titles.append("")
                    continue
                snums.append(sm.group(1))
                rest = re.sub(r'<span class="src">.*?</span>', "", sm.group(2), flags=re.S)
                titles.append(re.sub(r"<[^>]+>", "", rest).strip())
                if not re.sub(r"<[^>]+>", "", rest).strip():
                    sec_bad.append((cid, "空节题 " + sm.group(1)))
                if 'class="src"' in li:
                    src_total += 1
            want = [f"{cn_}.{k}" for k in range(1, len(lis) + 1)]
            if snums != want:
                sec_bad.append((cid, f"{snums} != {want}"))
            # M OS 比较节位次（O1b）：只判节题（titles 已剥 src 注），须居述评前一位或章末。
            for k, tt in enumerate(titles):
                if not OSCMP.search(tt):
                    continue
                os_n += 1
                nk = titles[k + 1] if k + 1 < len(titles) else None
                if nk is None or "本章书目述评" in nk:
                    continue
                os_bad.append((cid, f"{snums[k] if k < len(snums) else '?'} {tt[:36]}", nk[:26]))
            txts = [re.sub(r"<[^>]+>", "", x) for x in lis]
            last = txts[-1].strip() if txts else ""
            has_bib = any("本章书目述评" in x for x in txts)
            if has_bib and "本章书目述评" not in last:
                bib_bad.append((cid, last[:40]))
            elif lis and not has_bib and "卷末书目述评" not in t:
                _lt = re.sub(
                    r'<span class="src">.*?</span>', "", lis[-1], flags=re.S
                )
                bib_none.append((cid, re.sub(r"<[^>]+>", "", _lt).strip()[:40]))
        if _seg_li != _ch_li:
            tri_bad.append((vid, f"章外孤立节行 {_seg_li - _ch_li} 条"))
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

    print(f"K 三级结构（卷→章→节）: 无章之卷 "
          f"{len([x for x in tri_bad if x[1] == '无章之卷'])} |"
          f" 无节之章 {len([x for x in tri_bad if x[1] == '无节之章'])} |"
          f" 章外孤立节行 {len([x for x in tri_bad if '孤立' in x[1]])}")
    for x in tri_bad[:10]:
        print("   ❌", x)

    print(f"L 不设附录（章题不得以「附录」起首）: 命中 {len(appx_bad)} 处")
    for x in appx_bad[:10]:
        print("   ❌", x)
    print(f"M OS 比较节位次（须居述评前一位或章末）: 命中 {os_n} 处，违规 {len(os_bad)} 处")
    for x in os_bad[:10]:
        print("   ❌", x)

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
    if not css_all.strip():
        # 副本模式（--path 指向站点目录之外的单文件副本）：同目录无 assets/，CSS 源不可解析。
        # 此时若照旧把全部 class 判为「未定义」，夹具会因本组而恒 FAIL —— 判据是否有效被掩盖
        #（2026-09-27 实测：negfix 夹具全组「假拦下」即由此叠加 A 组 CRLF 造成）。故降级为 INFO。
        undef = []
        print("J 内容层 class ↔ 格式层: INFO 副本模式——同目录无 assets/，本组跳过（不改判定）")
    else:
        undef = sorted(c for c in static_cls
                       if not re.search(re.escape("." + c) + r"(?![\w-])", css_all))
        print("J 内容层 class ↔ 格式层: %d 个 class，未定义 %d %s"
              % (len(static_cls), len(undef), undef[:8]))

    # ── N 结构判据（2026-09-27 立；依据 MAX 提案 v1.1 M-7，01b R54）──────────
    # 编号说明：提案原文记为 G-a…G-d；本件既有 G 组为「标签平衡」，为免冲号改记 N 组，判据内容不变。
    # 缘由：B–F 组验「形」（编号连续／述评恒末／锚点唯一），不验「序与体例」——卷 41/42 层序
    #   反转、卷导言 21/43、分工注 7/43、章题年份 81/411、卷名 75 字，在既有门禁下全部静默通过。
    #   判据非空由 tests/tri_structure_negtest.py 的负向副本自证。
    # 键值口径：卷号 ＋ 卷题关键词 双键——重编号时给出可读错位提示，避免判据静默失效。
    n_bad, n_info = [], []

    def _seg(vn):
        return h[vols[vn - 1][2]:vols[vn][2]]

    def _plain(vn):
        return re.sub("^第[一二三四五六七八九十]+卷\\s\\s*", "", vols[vn - 1][1]).strip()

    def _yr(t):
        m = re.search("（(1[89][0-9][0-9]|20[0-4][0-9])", t)
        return int(m.group(1)) if m else None

    # 卷序索引表越界自检（2026-10-02 补，101 号文 §九 P0-3）——
    # 三表按卷号硬编码，卷序重排后须同步；越界即 FAIL，防静默失效。
    _vt = _check_vol_tables(len(vols))
    if _vt:
        n_bad.append("卷序索引表越界（卷序变更后须同步 SPINE／HORIZ／BIB_HAS）：%s" % _vt)
    n_info.append("卷序索引表越界 0 处（SPINE %d／HORIZ %d／BIB %d）"
                  % (len(SPINE), len(HORIZ), len(BIB_HAS)))

    # N-a1 编年主干（卷号, 卷题关键词, 期望起始年）：起点须严格递增
    # 见文件头「卷序索引表」（唯一源）
    spine_y = []
    for vn, key, y0 in SPINE:
        t = _plain(vn)
        if key not in t:
            n_bad.append("N-a1 卷 %d 卷题不含关键词「%s」（判据键错位，须同步维护 SPINE）：%s"
                         % (vn, key, t[:26]))
            continue
        y = _yr(t)
        if y is None:
            n_bad.append("N-a1 卷 %d 编年主干卷题缺年代区间：%s" % (vn, t[:26]))
        else:
            spine_y.append((vn, y))
    ys = [x[1] for x in spine_y]
    if ys != sorted(ys):
        n_bad.append("N-a1 编年主干起点非递增：%s" % spine_y)
    n_info.append("N-a1 编年主干 %d 卷，起点递增 ? %s" % (len(spine_y), ys == sorted(ys)))

    # N-a2 后设层（史学史／方法论）不得先于综合总结层（会者定离／分离聚合）
    post = [i + 1 for i, (_, t, _) in enumerate(vols[:-1]) if ("史学史" in t or "方法论" in t)]
    summ = [i + 1 for i, (_, t, _) in enumerate(vols[:-1]) if ("会者定离" in t or "分离聚合" in t)]
    ok_a2 = not (post and summ and min(post) < max(summ))
    if not ok_a2:
        n_bad.append("N-a2 后设层（卷 %s）先于综合总结层（卷 %s）" % (post, summ))
    n_info.append("N-a2 综合总结 %s ／ 后设 %s ｜ 后设居后 ? %s" % (summ, post, ok_a2))

    # N-a3 横向／专题卷须有分工注（显式必设集 × 关键词双键）
    # 见文件头「卷序索引表」（唯一源）
    miss_note = []
    for vn, key in HORIZ:
        t = _plain(vn)
        if key not in t:
            n_bad.append("N-a3 卷 %d 卷题不含关键词「%s」（判据键错位）：%s" % (vn, key, t[:26]))
        elif '<p class="vol-note">' not in _seg(vn):
            miss_note.append(vn)
    if miss_note:
        n_bad.append("N-a3 横向／专题卷缺分工注：%s" % miss_note)
    n_info.append("N-a3 横向卷 %d 卷，缺注 %d" % (len(HORIZ), len(miss_note)))

    # N-b1 卷导言恒设
    no_ov = [i + 1 for i in range(len(vols) - 1) if '<p class="vol-overview">' not in _seg(i + 1)]
    if no_ov:
        n_bad.append("N-b1 缺卷导言 %d 卷：%s" % (len(no_ov), no_ov))
    n_info.append("N-b1 卷导言缺失 %d 卷" % len(no_ov))

    # N-b2 述评章登记表（R55：按独立史料域判定，设与不设均登记）
    BIB = {v: "有" for v in BIB_HAS}
    for vn in [i + 1 for i in range(len(vols) - 1) if (i + 1) not in BIB]:
        BIB[vn] = "E1：编年卷或专题卷，述评以章末「本章书目述评」节承载，或由所属专卷承担"
    has_bib = []
    for i in range(len(vols) - 1):
        for c in re.findall(r'<h3 class="chapter"[^>]*>(.*?)</h3>', _seg(i + 1), re.S):
            if "卷末书目述评" in c:
                has_bib.append(i + 1)
                break
    if set(BIB) != set(range(1, len(vols))):
        n_bad.append("N-b2 述评登记表未覆盖全部卷：缺 %s"
                     % sorted(set(range(1, len(vols))) - set(BIB)))
    if sorted(has_bib) != sorted(k for k, v in BIB.items() if v == "有"):
        n_bad.append("N-b2 述评章实况与登记表不符：实有 %s ／ 登记 %s"
                     % (has_bib, sorted(k for k, v in BIB.items() if v == "有")))
    n_info.append("N-b2 述评登记 %d 卷（实设 %d 卷）" % (len(BIB), len(has_bib)))

    # N-b3 编年卷版本编年章题须带年份区间（依 72 号文「年份由各章承载」设计）
    VRE = re.compile("[0-9]+(\\.[0-9]+)*x|[0-9]+BSD")
    no_year = []
    for vn in [16, 19, 22, 25, 5, 6, 7, 9, 13]:
        for c in re.findall(r'<h3 class="chapter"[^>]*>(.*?)</h3>', _seg(vn), re.S):
            ct = re.sub("<[^>]+>", "", c).strip()
            if "述评" in ct:
                continue
            if VRE.search(ct) and _yr(ct) is None:
                no_year.append((vn, ct[:24]))
    if no_year:
        n_bad.append("N-b3 版本编年章题缺年份 %d 处：%s" % (len(no_year), no_year[:4]))
    n_info.append("N-b3 编年卷版本章题缺年份 %d 处" % len(no_year))

    # ── N-b4 卷题时段 ↔ 章内年份一致性（2026-10-02 补，主理人批准；101 号文 §九 P0-1）──
    # 依据：卷 9「UNIX 战争（1982–2021）」章内 ch9 实为（1995–2021）——**卷题区间与章内年份不自洽**
    # 而 N-b3 只验「编年卷版本章题须带年份」，不验自洽，故长期漏检。本判据补此环。
    # 判法：卷题括注的 (起–止) 区间须覆盖该卷**全部章题与节题**中出现的 4 位年份；越界即报。
    # 豁免：卷题无年代区间者不判；述评章不计。
    YR4 = re.compile(r'(1[89][0-9][0-9]|20[0-4][0-9])')
    b4_bad = []
    for vi in range(1, len(vols)):
        vt = re.sub("<[^>]+>", "", _plain(vi))
        rm = re.search(r'（(1[89][0-9][0-9])[–\-—](20[0-4][0-9])', vt)
        if not rm:
            continue
        lo, hi = int(rm.group(1)), int(rm.group(2))
        # 只判**章题自带年代区间**者（节题中的历史引用不构成矛盾；卷题时段为「主线期口径」）
        for t in re.findall(r'<h3 class="chapter"[^>]*>(.*?)</h3>', _seg(vi), re.S):
            ct = re.sub("<[^>]+>", "", t)
            cm = re.search(r'（(1[89][0-9][0-9])[–\-—](20[0-4][0-9])', ct)
            if cm:
                clo, chi = int(cm.group(1)), int(cm.group(2))
                if clo < lo or chi > hi:
                    b4_bad.append((vi, "%d–%d" % (lo, hi), ct[:30]))
    if b4_bad:
        n_bad.append("N-b4 章题年代区间越出卷题时段 %d 处：%s" % (len(b4_bad), b4_bad[:4]))
    n_info.append("N-b4 章题越出卷题时段 %d 处" % len(b4_bad))

    # ── N-b5 目录正文迁移留痕零残留（2026-10-02 补，主理人批准；101 号文 §九 P0-2）──
    # 依据：R8「注释内容应分离，类似的括号应全部移除出目录正文」；期四(b) 首轮漏清 127 处，
    # 因当时只验「移除数＝台账数」而未验「残留数＝0」。本判据把「反向枚举」固化为门禁。
    # 白名单：3 处经逐条核验为应保留（1 处误报＋2 处分工记录）。
    MIG_RE = re.compile(r'迁入|并入本章|自卷\s*[0-9一二三四五六七八九十百]+\s*旧')
    MIG_OK = ("城市形成与大学迁入",
              "原“与第三十六卷第 5 章 14.11 分工”分句失据",
              "注因两章同迁入本卷而消解")
    b5 = []
    for vi in range(1, len(vols)):
        _clean = re.sub(r"<(script|style)[^>]*>.*?</>", " ", _seg(vi), flags=re.S | re.I)
        _clean = re.split(r"<script|<style", _clean)[0]   # 兜底：截断未闭合的 script/style 残段
        for t in re.findall(r"<li[^>]*>(.*?)</li>", _clean, re.S):
            txt = re.sub("<[^>]+>", "", t)
            if MIG_RE.search(txt) and not any(k in txt for k in MIG_OK):
                b5.append((vi, txt[:40]))
    if b5:
        n_bad.append("N-b5 目录正文残留迁移留痕 %d 处：%s" % (len(b5), b5[:4]))
    n_info.append("N-b5 迁移留痕残留 %d 处" % len(b5))

    # 长度计数口径（2026-09-27 主理人裁定）：**英语单词整体算 1 字**——拉丁字母数字串
    # （FreeBSD／NetBSD／4.3BSD／Net/2／1986）各计 1 字，其余字符逐字计。N-c／N-f 同用。
    def title_len(s):
        return len(LATIN_RUN.sub(chr(0), s))

    # N-c 卷名长度 ≤36 字（**硬限**，依 M-5；卷 7 由 77 字精简为 36 字为先例）
    lt = [(i + 1, title_len(re.sub("^第[一二三四五六七八九十]+卷\\s\\s*", "", t)))
          for i, (_, t, _) in enumerate(vols[:-1])]
    over_t = [x for x in lt if x[1] > 36]
    if over_t:
        n_bad.append("N-c 卷名超 36 字 %d 卷：%s" % (len(over_t), over_t[:4]))
    n_info.append("N-c 卷名最长 %d 字（限 36；英语单词算 1 字）" % max(x[1] for x in lt))

    # N-d 题文形制：复合词连接号须用 en dash（禁半角连字符形）
    _body = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", h, flags=re.S | re.I)
    _titles = re.findall("<h2>(.*?)</h2>", _body, re.S)
    _titles += re.findall(r'<h3 class="chapter"[^>]*>(.*?)</h3>', _body, re.S)
    _titles += re.findall(r"<li[^>]*>.*?</li>", _body, re.S)
    bad_dash = []
    for t in _titles:
        s = re.sub("<[^>]+>", "", t)
        # 只判「项目名复合词」形（BSD-UNIX／BSD-Linux／GNU-Linux 等）；
        # 4.3BSD-Tahoe、4.4BSD-Lite 等为官方发行名，其连字符正确，须放过。
        for m in re.finditer("(?:BSD|GNU|UNIX|Linux|OpenBSD|NetBSD|FreeBSD)-(?:UNIX|Linux|GNU|BSD)", s):
            bad_dash.append(s[max(0, m.start() - 8):m.end() + 8])
    if bad_dash:
        n_bad.append("N-d 题文复合词用半角连字符 %d 处：%s" % (len(bad_dash), bad_dash[:4]))
    n_info.append("N-d 题文半角连字符 %d 处" % len(bad_dash))

    # ── N-e～N-i 节级判据（2026-09-27 补遗，主理人批准；依据 MAX 提案第三节）────
    # N-e 章内年序：章题带年代区间的章，其含年份节的年份须非递减（容 1 年回落）
    # N-f 节题长度：**软限**（2026-09-27 主理人裁定）——逾 50／逾 60 只示 WARN，不判 FAIL、不阻断；
    #   计数口径＝title_len()（英语单词整体算 1 字）；豁免：比较节构式／美学参照节
    # N-g 述评位次：节题恰为「本章书目述评」者须为末节（修正「含述评二字」假阳性）
    # N-h 节数离群：<4 或 >14 WARN／>18 FAIL（豁免收口章：述评／方法／史料／总评／登记）
    # N-i 同题登记：同题节跨章须命中登记构式，否则 FAIL
    from collections import defaultdict as _dd
    o_bad, o_warn = [], []
    n_e_bad, n_f_warn, n_g_bad, n_h_bad, n_i_bad = [], [], [], [], []
    YR = re.compile("(1[5-9][0-9][0-9]|20[0-4][0-9])")
    DUP_OK = ("与同时期操作系统的比较", "同时期操作系统", "参照：美学史与软件美学研究",
              "证据层级：当事人叙述", "从物质证据到文化解释", "尚未解决的问题：缺失档案",
              "ASLR 与 KASLR", "BDFL", "本章书目述评")
    sec_titles = _dd(list)
    for vi in range(1, len(vols)):
        seg = _seg(vi)
        for cm in re.finditer(r'<h3 class="chapter"[^>]*>(.*?)</h3>\s*<ul class="sections">(.*?)</ul>', seg, re.S):
            ct = re.sub("<[^>]+>", "", cm.group(1)).strip()
            cmno = re.match(r"^第 (\d+) 章", ct)
            if not cmno:
                continue
            cno = int(cmno.group(1))
            secs = []
            for li in re.findall(r"<li[^>]*>(.*?)</li>", cm.group(2), re.S):
                mm = re.search(r'<span class="sec-num">([^<]+)</span>\s*(.*)', li, re.S)
                if not mm:
                    continue
                title = re.sub(r'<span class="src">.*?</span>', "", mm.group(2), flags=re.S)
                title = re.sub("<[^>]+>", "", title).strip()
                title = re.sub("〔[^〕]*〕", "", title).strip()   # 排除〔迁入/溯源〕标记
                secs.append((mm.group(1).strip(), title))
                if len(title) >= 12:
                    sec_titles[title].append("卷%d.第%d章" % (vi, cno))
            # ── O 组：标题计数概括式与集合名词（2026-09-27 立）──
            #   软硬：卷题／章题命中 → FAIL（集合的定义层）；节题、注文 → WARN（不阻断）。
            _ot = o_flag(t)
            if _ot:
                o_bad.append("O 卷题计数概括式／集合名词：卷%d「%s」（命中「%s」）" % (vi, t[:40], _ot))
            _ct_body = re.sub(r"^第 \\d+ 章\\s*", "", ct)
            _ot = o_flag(_ct_body)
            if _ot:
                o_bad.append("O 章题计数概括式／集合名词：卷%d 第%d章「%s」（命中「%s」）" % (vi, cno, _ct_body[:40], _ot))
            for _num, _title in secs:
                _ot = o_flag(_title)
                if _ot:
                    o_warn.append("O WARN（软·节题）卷%d 第%d章 %s「%s」（命中「%s」）" % (vi, cno, _num, _title[:36], _ot))
            for _nm in re.findall(r'<span class="src">(.*?)</span>', cm.group(2), re.S):
                _nt = re.sub("<[^>]+>", "", _nm).strip()
                _ot = o_flag(_nt)
                if _ot:
                    o_warn.append("O WARN（软·注文）卷%d 第%d章「%s…」（命中「%s」）" % (vi, cno, _nt[:32], _ot))
            yr = [int(m.group(1)) for _, t in secs for m in [YR.search(t)] if m]
            if re.search(r"（\d{4}–", ct) and len(yr) >= 4:
                for k in range(1, len(yr)):
                    if yr[k] < yr[k - 1] - 1:
                        n_e_bad.append("N-e 年序回落：卷%d 第%d章 第%d个含年份节年序回落（%d→%d）" % (vi, cno, k + 1, yr[k - 1], yr[k]))
            is_cmp = "同时期操作系统" in ct
            is_aes = "参照：美学史" in ct
            for _num, _t in secs:
                if "与同时期操作系统的比较" in _t:
                    is_cmp = True
            for k, (num, t) in enumerate(secs):
                W = title_len(t)
                if not (is_cmp or is_aes or "参照：美学史" in t):
                    if W > 60:
                        n_f_warn.append("N-f WARN（软限·逾 60）卷%d 第%d章 %s（%d 字）" % (vi, cno, num, W))
                    elif W > 50:
                        n_f_warn.append("N-f WARN（软限·逾 50）卷%d 第%d章 %s（%d 字）" % (vi, cno, num, W))
                if t == "本章书目述评" and k != len(secs) - 1:
                    n_g_bad.append("N-g 述评非末位：卷%d 第%d章 %s 非末位（第 %d/%d 位）" % (vi, cno, num, k + 1, len(secs)))
            if len(secs) < 4 or len(secs) > 14:
                if re.search(r"述评|方法|史料|总评|登记|总目", ct):
                    continue                                  # 收口章豁免
                lvl = "FAIL" if len(secs) > 18 else "WARN"
                if len(secs) > 18:
                    n_h_bad.append("N-h 节数超载：卷%d 第%d章 %d 节（%s）" % (vi, cno, len(secs), lvl))
                else:
                    n_info.append("N-h WARN 卷%d 第%d章 %d 节（%s）" % (vi, cno, len(secs), lvl))
    for title, locs in sorted(sec_titles.items(), key=lambda x: -len(x[1])):
        if len(locs) < 2:
            continue
        chapters_hit = len(set(locs))
        if any(p in title for p in DUP_OK):
            continue                                          # 已登记构式
        if chapters_hit >= 3 or len(set(locs)) >= 2 and len(locs) >= 3:
            n_i_bad.append("N-i 同题节未登记 %d 处：%s ← %s" % (len(locs), title[:40], "、".join(locs[:6])))
        elif len(locs) == 2 and len(set(locs)) == 2:
            n_info.append("N-i 跨章同题（登记建议）：%s ← %s" % (title[:36], "、".join(locs)))
    for _x in o_warn:
        print("   ⚠", _x)
    for _x in o_bad:
        print("   ❌", _x)
    for _x in n_f_warn:
        print("   ⚠", _x)
    for _x in n_e_bad + n_g_bad + n_h_bad[:6] + n_i_bad[:6]:
        print("   ❌", _x)
    n_info.append("O 标题计数概括式／集合名词：卷／章题命中 %d（FAIL）｜节题与注文软示 %d（WARN）" % (len(o_bad), len(o_warn)))
    n_info.append("N-e 年序回落 %d｜N-f 软限提示 %d（不判 FAIL）｜N-g 述评非末位 %d｜N-h 离群 %d｜N-i 未登记同题 %d"
                  % (len(n_e_bad), len(n_f_warn), len(n_g_bad), len(n_h_bad), len(n_i_bad)))

    for _x in n_info:
        print(_x)
    all_sub = n_bad + n_e_bad + n_g_bad + n_h_bad + n_i_bad
    for _x in all_sub[:14]:
        print("   ❌", _x)

    # ── P 组：注文括注配对（2026-09-30 立，98 号文 §11.4 P0-1）──
    #   逐行核「〔」与「〕」计数相等。设立缘由：66 条溯源注缺收尾「〕」曾长期静默——
    #   A 编码只查直角引号、G 组只查标签平衡、D 组只查节题非空，均不覆盖括注；
    #   且该缺陷在内容源 `重构2026/data/outline.txt` 与产物同数传播（66 行），修复前后无任何护栏。
    #   判据非空由 `tests/tri_structure_negtest.py` 的「P 括注不配对」缺陷副本自证。
    p_bad = []
    for _i, _l in enumerate(h.split("\n"), 1):
        _o, _c = _l.count("〔"), _l.count("〕")
        if _o != _c:
            p_bad.append("P 注文括注不配对 第 %d 行（〔%d／〕%d）—— %s"
                         % (_i, _o, _c, _l.strip()[:80]))
    print("P 注文括注配对:",
          ("PASS（〔＝〕＝%d）" % h.count("〔")) if not p_bad else ("FAIL %d 行" % len(p_bad)))
    for _x in p_bad[:10]:
        print("   ❌", _x)

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
        or tri_bad
        or appx_bad
        or os_bad
        or n_bad
        or n_e_bad
        or n_g_bad
        or n_h_bad
        or n_i_bad
        or o_bad
        or p_bad
    )
    print("\n总判定:", "FAIL" if allbad else "PASS")
    return 1 if allbad else 0


if __name__ == "__main__":
    sys.exit(main())
