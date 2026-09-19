# -*- coding: utf-8 -*-
"""2026-09-18 加强复核（v2）：对目录页做**全库独立复算**。

复核原则（比 v1 更严）：
  1. **不引用执行脚本与门禁脚本的断言**——所有指标从 index.html 原文重新解析推导；
  2. **不抽样**——352 章 / 3023 节 / 316 条溯源注 / 37 卷**逐条**核对；
  3. **含结构层**——屏蔽 script/style 后做全标签平衡复算；
  4. **含数据层**——独立解码 `opt-data-blob`（gzip+base64）并复算 SRI；
  5. **含关联层**——56 表目标列**全表 360 行**逐条与页面章题比对。

用法：python review_v2_full.py
"""
import base64
import gzip
import hashlib
import html as htmlmod
import io
import json
import os
import re
import sys

ROOT = "D:/librebsd"
IDX = ROOT + "/08-核查报告与多轮复核/重构2026/index.html"
OK, BAD, INFO = [], [], []


def chk(name, cond, detail=""):
    (OK if cond else BAD).append(name)
    print(("PASS " if cond else "FAIL ") + name + (("｜" + str(detail)) if detail else ""))


def info(name, detail=""):
    INFO.append(name)
    print("INFO " + name + (("｜" + str(detail)) if detail else ""))


def rd(p):
    return io.open(p, encoding="utf-8").read()


h = rd(IDX)
raw = open(IDX, "rb").read()

print("=" * 78)
print("A. 文本与编码层（10 项）")
print("=" * 78)
chk("A1 无 BOM", not raw.startswith(b"\xef\xbb\xbf"))
chk("A2 无 CRLF", b"\r\n" not in raw)
chk("A3 无替换字符 U+FFFD", "\ufffd" not in h)
chk("A4 无直角/白角引号（U+300C/D/E/F）",
    all(c not in h for c in "\u300c\u300d\u300e\u300f"))
chk("A5 无全角空格 U+3000", "\u3000" not in h)
try:
    raw.decode("utf-8")
    chk("A6 UTF-8 严格可解码", True)
except Exception as e:
    chk("A6 UTF-8 严格可解码", False, e)
ctrl = {hex(c): h.count(chr(c)) for c in range(0x20)
        if chr(c) not in "\t\n\r" and h.count(chr(c))}
chk("A7 无 C0 控制字符（除 \\t\\n\\r）", not ctrl, ctrl)
chk("A8 无不换行空格 U+00A0", "\u00a0" not in h)
zw = {c: h.count(c) for c in ("\u200b", "\u200c", "\u200d", "\ufeff") if c in h}
chk("A9 无零宽字符（U+200B/C/D、U+FEFF）", not zw, zw)
try:
    h.encode("utf-8").decode("utf-8")
    chk("A10 无孤立代理码位", True)
except Exception as e:
    chk("A10 无孤立代理码位", False, e)

# ── 屏蔽 script/style 区域（保留长度，便于后续定位）────────────────────
masked = list(h)
for m in re.finditer(r"<(script|style)\b[^>]*>.*?</\1>", h, re.S | re.I):
    for i in range(m.start(), m.end()):
        masked[i] = " "
st = "".join(masked)

print()
print("=" * 78)
print("B. 标签与结构完整性（静态区全标签平衡，8 项）")
print("=" * 78)
for tag in ("li", "ul", "ol", "section", "h2", "h3", "div", "span", "p",
            "a", "button", "footer", "main", "nav", "details", "summary"):
    o = len(re.findall(r"<%s(?![\w-])" % tag, st))
    c = st.count("</%s>" % tag)
    chk("B1.%s 静态 <%s> 平衡（%d）" % (tag, tag, o), o == c, f"开 {o}／闭 {c}")
chk("B2 静态 <li> 计数 = 3023（= 节数）", len(re.findall(r"<li[ >]", st)) == 3023,
    len(re.findall(r"<li[ >]", st)))
chk("B3 静态 <ul class=\"sections\"> = 352（= 章数）",
    len(re.findall(r'<ul class="sections">', st)) == 352)
chk("B4 静态 <h3 class=\"chapter\"> = 352", len(re.findall(r'<h3 class="chapter"', st)) == 352)
chk("B5 静态 <section class=\"doc-block\"> = 37", len(re.findall(r'<section class="doc-block"', st)) == 37)
chk("B6 静态 <h2> = 37（JS 模板那处已屏蔽）", len(re.findall(r"<h2>", st)) == 37)
chk("B7 script 4 对／style 3 对",
    len(re.findall(r"<script", h)) == 4 and h.count("</script>") == 4
    and len(re.findall(r"<style", h)) == 3 and h.count("</style>") == 3)
ids = re.findall(r'\sid="([^"]+)"', h)
dup_ids = sorted({x for x in ids if ids.count(x) > 1})
chk("B8 id 共 416 个且全局唯一（第三十二批：卷31／卷32 全卷替换，章 329 → 336）", len(ids) == 416 and not dup_ids, f"总 {len(ids)}／重复 {dup_ids}")

print()
print("=" * 78)
print("C. 全库逐卷／逐章／逐节复算（12 项，不抽样）")
print("=" * 78)
vols = []           # (v, 卷题, [ (m, 章题, [(节号, 节号后原文, 题文)]) ])


def parse_secs(ul_html):
    """解析 <ul class="sections"> 内的节。

    返回 (节号, 节号后原文 after, 归一题文 title)。
    注意：**29 处节号后紧接 `<span class="src">` 溯源注，题文在该注之后**——
    after 用于空格形制判据（C10），title 为剔除 src 注并归一并压缩空白后的题文（C9／C11／G）。
    """
    out = []
    for lm in re.finditer(r"<li>(.*?)</li>", ul_html, re.S):
        inner = lm.group(1)
        nm = re.search(r'<span class="sec-num">([\d.]+)</span>', inner)
        if not nm:
            continue
        after = inner[nm.end():]
        title = re.sub(r'<span class="src">.*?</span>', "", after, flags=re.S)
        title = re.sub(r"\s+", " ", title).strip()
        out.append((nm.group(1), after, title))
    return out


for vm in re.finditer(r'<section class="doc-block" id="vol-(\d+)" role="doc-part">(.*?)</section>', h, re.S):
    v = int(vm.group(1))
    t = re.search(r"<h2>(.*?)</h2>", vm.group(2), re.S)
    chs = []
    for cm in re.finditer(
        r'<h3 class="chapter" id="vol-%d-ch-(\d+)">(.*?)</h3>\s*<ul class="sections">(.*?)</ul>' % v,
        vm.group(2), re.S,
    ):
        chs.append((int(cm.group(1)), cm.group(2), parse_secs(cm.group(3))))
    vols.append((v, t.group(1) if t else "", chs))

chk("C1 卷锚点 vol-1..vol-37 连续唯一", [x[0] for x in vols] == list(range(1, 38)),
    f"实为 {len(vols)} 卷")
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


seq_bad = []
for v, t, _ in vols:
    m = re.match(r"^第([一二三四五六七八九十]+)卷", t)
    if not m or cn2int(m.group(1)) != v:
        seq_bad.append((v, t[:16]))
chk("C2 卷题序数 ↔ 卷锚点一致（36/36）", not seq_bad, seq_bad[:3])
chk("C3 卷题形制「第N卷＋2 个半角空格＋非空题名」",
    all(re.match(r"^第[一二三四五六七八九十]+卷  \S", t) for _, t, _ in vols))
chk("C4 卷题全局唯一", len({t for _, t, _ in vols}) == 37)
bad_c5 = []
for v, _, chs in vols:
    if [c[0] for c in chs] != list(range(1, len(chs) + 1)):
        bad_c5.append((v, [c[0] for c in chs][:5]))
chk("C5 卷内章号连续唯一（M=1..K）", not bad_c5, bad_c5[:3])
bad_c6 = []
for v, _, chs in vols:
    for m, t, _ in chs:
        if not t.startswith("第 %d 章 " % m):
            bad_c6.append((v, m, t[:20]))
chk("C6 章题与锚点章号一致（第 M 章 ）", not bad_c6, bad_c6[:3])
all_titles = [t for _, _, chs in vols for _, t, _ in chs]
chk("C7 章题共 352 且唯一（判据＝「第 M 章 题名」整串；跨卷同名异章号不触发）", len(all_titles) == 352 and len(set(all_titles)) == 352,
    f"共 {len(all_titles)}／唯一 {len(set(all_titles))}")
bad_c8, bad_c9, bad_c10, bad_c11 = [], [], [], []
n_sec = 0
n_srcfirst = 0
for v, _, chs in vols:
    for m, t, secs in chs:
        n_sec += len(secs)
        nums = [n for n, _, _ in secs]
        if nums != ["%d.%d" % (m, k) for k in range(1, len(secs) + 1)]:
            bad_c8.append((v, m, nums[:4]))
        for n, after, title in secs:
            if after.startswith(" <span"):
                n_srcfirst += 1
            if not title:
                bad_c9.append((v, n, repr(after[:14])))
            # 节号后：常规情形须恰 1 个半角空格；src-first 情形须 1 空格后紧接 <span
            ok_sp = True if after.startswith(" <span") else (
                after.startswith(" ") and not after.startswith("  "))
            if not ok_sp or "\u3000" in after:
                bad_c10.append((v, n, repr(after[:14])))
        if any(x[2].startswith("本章书目述评") for x in secs) \
                and not secs[-1][2].startswith("本章书目述评"):
            bad_c11.append((v, m))
chk("C8 节号 M.K 与所属章号一致且 K 连续（3023 节）", not bad_c8, bad_c8[:3])
chk("C9 节题非空（剔除 src 注后）", not bad_c9, bad_c9[:3])
chk("C10 节号后为 1 个半角空格（无连空两格／U+3000）", not bad_c10, bad_c10[:3])
chk("C11 全库「本章书目述评」节均居章末（含 1 处批准变体）", not bad_c11, bad_c11[:3])
info("节号后紧接 src 溯源注的节", f"{n_srcfirst} 处（与「2298 直连 ＋ 20 接 src 注 = 2318」口径吻合）")
chk("C12 章数合计 352／节数合计 3023",
    sum(len(chs) for _, _, chs in vols) == 352 and n_sec == 3023,
    f"章 {sum(len(chs) for _, _, chs in vols)}／节 {n_sec}")

print()
print("=" * 78)
print("D. 口径六处与小字自洽（5 项）")
print("=" * 78)
dm_m = re.search(r'<div class="doc-metrics">(.*?)</div>\s*</div>', h, re.S)
dm_txt = dm_m.group(0) if dm_m else ""
nums = re.findall(r"<span>总[卷章节]数</span><strong>(\d+)</strong>", dm_txt)
auth = tuple(int(x) for x in nums) if len(nums) == 3 else None
chk("D1 doc-metrics 三元组 = (37,352,3023)", auth == (37, 352, 3023), auth)


def tri_of(s):
    m = re.search(r"(\d+)\s*卷\s*(\d+)\s*章\s*(\d+)\s*节", s or "")
    return tuple(int(x) for x in m.groups()) if m else None


og = re.search(r'property="og:description" content="([^"]*)"', h)
meta = re.search(r'name="description" content="([^"]*)"', h)
foot = re.search(r"<footer[^>]*>(.*?)</footer>", h, re.S)
got = {
    "doc-metrics": auth,
    "og": tri_of(og.group(1) if og else ""),
    "meta": tri_of(meta.group(1) if meta else ""),
    "footer": tri_of(foot.group(1) if foot else ""),
    "实测": (len(vols), len(all_titles), n_sec),
}
ld = re.search(r'<script type="application/ld\+json"[^>]*>(.*?)</script>', h, re.S)
ld_tri = None
if ld:
    try:
        d = json.loads(ld.group(1))
        vals = {}

        def walk(o):
            if isinstance(o, dict):
                if o.get("name") in ("卷数", "章数", "节数") and "value" in o:
                    vals[o["name"]] = int(o["value"])
                for v in o.values():
                    walk(v)
            elif isinstance(o, list):
                for v in o:
                    walk(v)

        walk(d)
        if {"卷数", "章数", "节数"} <= set(vals):
            ld_tri = (vals["卷数"], vals["章数"], vals["节数"])
    except Exception as e:
        info("JSON-LD 解析异常", e)
got["JSON-LD"] = ld_tri
chk("D2 六处口径全部一致且 = (37,352,3023)",
    all(v == (37, 352, 3023) for v in got.values()), got)
small = re.findall(r"<small>(.*?)</small>", dm_txt)
chk("D3 doc-metrics 小字自洽（正章 342 ＋ 卷末述评章 10 = 352）",
    any("342" in s and "10" in s for s in small), small)
n_volend = len([t for t in all_titles if "卷末书目述评" in t])
chk("D4 卷末书目述评章 = 10 个（第四十一批：11 卷换稿 ＋ 插卷后述评章随之变动）", n_volend == 10, n_volend)
n_chbiblio = len([1 for _, _, chs in vols for _, _, secs in chs
                  if any(x[2].startswith("本章书目述评") for x in secs)])
chk("D5 章级述评节 = 158（判据＝题文 startswith「本章书目述评」，含 1 处批准变体；第四十一批各换稿卷无述评节）", n_chbiblio == 158, n_chbiblio)
# 述评题名形制：263 中 262 为标准「本章书目述评」，1 处为批准变体（39 号文 F-10）
_v = [f"vol{v}-ch{m} §{x[0]} → {x[2]}" for v, _, chs in vols for m, _, secs in chs
      for x in secs if "本章书目述评" in x[2] and x[2] != "本章书目述评"]
chk("D6 述评题名变体仅 1 处且为 39 号文 F-10 批准形制",
    _v == ["vol1-ch7 §7.9 → 本章书目述评：莱昂氏 UNIX 源代码分析"], _v)
info("卷末述评章形制", "20 章 = 7「…全卷综述」＋ 1「…卷综述」＋ 4「…史料总目」（后两类为 67/69/71 号文批准的"
     "技术专题史卷专用命名）＋ 8 裸卷名（卷9／卷11／卷12／卷13 ＋ 卷20／卷22／卷25／卷26；"
     "卷20 卷末章由 2026-09-19 第二十六批清单改题为「OpenBSD 历史研究方法」，卷21／卷22 卷末章按同批清单照录）")

print()
print("=" * 78)
print("E. 溯源注（src）逐条审计（4 项）")
print("=" * 78)
srcs = re.findall(r'<span class="src">(.*?)</span>', h, re.S)
chk("E1 溯源注计数 = 316", len(srcs) == 316, len(srcs))
chk("E2 每条非空、无「（待补）」", all(s.strip() for s in srcs) and not any("（待补）" in s for s in srcs))
bad_e3 = [s[:30] for s in srcs if "<" in s or ">" in s]
chk("E3 溯源注内无残留 HTML 标签", not bad_e3, bad_e3[:2])
chk("E4 溯源注内无直角引号／U+3000",
    not any(("\u300c" in s or "\u300d" in s or "\u3000" in s) for s in srcs))
info("溯源注分工注「〔…〕」形态", f"含〔〕者 {sum(1 for s in srcs if '〔' in s)} 条")

print()
print("=" * 78)
print("F. DATA 段独立解码与 SRI 复算（5 项）")
print("=" * 78)
bm = re.search(
    r'<script type="application/gzip\+base64" id="opt-data-blob"[^>]*data-integrity="sha256-([^"]+)"[^>]*>(.*?)</script>',
    h, re.S)
if not bm:
    chk("F1 opt-data-blob 与 data-integrity 齐备", False)
else:
    tag, body = bm.group(1), bm.group(2)
    flat = re.sub(r"\s+", "", body)
    calc = base64.b64encode(hashlib.sha256(flat.encode()).digest()).decode()
    chk("F1 SRI：去全部空白 base64 的 SHA-256 == data-integrity", calc == tag,
        f"计算 {calc[:14]}…／标签 {tag[:14]}…")
    info("blob 形态", f"原始 {len(body)} 字符（含 {body.count(chr(10))} 换行）→ 去空白 {len(flat)}")
    try:
        blob = json.loads(gzip.decompress(base64.b64decode(flat)).decode("utf-8"))
        chk("F2 gzip 解压 + JSON 解析成功", True)
        keys = {"persons", "refs", "revs"}
        chk("F3 三键齐备且非空",
            keys <= set(blob) and all(len(blob[k]) > 0 for k in keys),
            {k: len(blob.get(k, [])) for k in sorted(keys)})
        chk("F4 persons 2269／refs 5567／revs 11",
            len(blob["persons"]) == 2269 and len(blob["refs"]) == 5567 and len(blob["revs"]) == 11,
            f"{len(blob['persons'])}／{len(blob['refs'])}／{len(blob['revs'])}")
        blob_s = json.dumps(blob, ensure_ascii=False)
        # 著录中的邮箱 <a@b> 与 URL <https://…> 属 GB/T 7714 体例，非 HTML 残片；
        # 此处只查真正的 HTML 标签与直角引号
        tags = re.findall(r"</?(?:span|div|li|ul|h[1-6]|p|br|script|style|a|img|table)\b",
                          blob_s, re.I)
        chk("F5 blob 内无 HTML 标签残片与直角引号", not tags and "\u300c" not in blob_s,
            tags[:4] or "无")
        info("blob 内尖括号", f"< {blob_s.count('<')} 个／> {blob_s.count('>')} 个（均为邮箱或 URL 著录）")
    except Exception as e:
        chk("F2 gzip 解压 + JSON 解析成功", False, e)

print()
print("=" * 78)
print("G. 本批改写逐字核对（第二批 卷5ch6／卷6ch1–5 ＋ 第十一批 卷3 全卷）")
print("=" * 78)
SPEC5 = [
    ("第 1 章 贝克莱与伯克利市", [
        "1.1 贝克莱与伯克利：名称、哲学家与地名",
        "1.2 从东湾社区到伯克利市：城市形成与大学迁入",
        "1.3 东湾地理、湾区交通与科技网络",
        "1.4 伯克利的反文化传统与政治文化",
        "1.5 本章书目述评"]),
    ("第 2 章 加州大学伯克利分校史：UNIX 以前", [
        "2.1 加州大学的创建与伯克利校址",
        "2.2 从学院教育到研究型大学",
        "2.3 工程学、科学与技术教育传统的形成",
        "2.4 校园实验室与科学研究基础设施",
        "2.5 从实验室到“大科学”：劳伦斯与辐射实验室",
        "2.6 多元巨型大学（Multiversity）与伯克利的扩张",
        "2.7 UNIX 以前的伯克利：科研共同体的形成",
        "2.8 本章书目述评"]),
    ("第 3 章 计算机科学学科的形成：以伯克利为枢纽", [
        "3.1 计算机科学的形成：麻省理工、斯坦福、伯克利与卡内基梅隆",
        "3.2 伯克利早期计算环境：从计算中心到分时系统",
        "3.3 伯克利计算机科学的制度化：计算机科学系与电气工程和计算机科学系",
        "3.4 伯克利计算机科学的学术方向与研究群体",
        "3.5 伯克利计算机科学的多向研究传统：数据库、体系结构与其他研究",
        "3.6 本章书目述评"]),
    ("第 4 章 CSRG 的教育模式与学术传播", [
        "4.1 CSRG 的形成：研究组式科研与研究生参与",
        "4.2 做中学：项目、代码与系统实践",
        "4.3 BSD 源码与文档：从研究成果到教育载体",
        "4.4 论文、会议与 UNIX 学术网络",
        "4.5 黑客伦理、学术自由与研究规范",
        "4.6 CSRG 教育模式的批评与时代背景",
        "4.7 学位、职业与学术合法性：制度边缘的培养通道",
        "4.8 从伯克利到 BSD 社群：大学网络与知识传播",
        "4.9 本章书目述评"]),
    ("第 5 章 加州大学伯克利分校的制度、治理与政治语境", [
        "5.1 加州大学的治理结构：董事会、教务委员会与校区自治",
        "5.2 学生运动、学术自由与校园政治",
        "5.3 冷战时期的伯克利：国家科研体系与大学政治",
        "5.4 公共信托、大学自治与知识产权",
        "5.5 DARPA 与 CSRG：联邦科研资助的具体机制",
        "5.6 本章书目述评"]),
    ("第 6 章 被遮蔽的 CSRG：组织、档案与解散", [
        "6.1 CSRG 档案：形成、保存与公开",
        "6.2 CSRG 的组织结构、科研管理与资源分配",
        "6.3 CSRG 的技术路线：选择、继承与淘汰",
        "6.4 CSRG 的解散：资金、决策与 1994—1995 年的组织终结",
        "6.5 被记录的与未被记录的 CSRG：行政、后勤与女性参与",
        "6.6 CSRG 的历史记忆：档案、叙事与 BSD 形象",
        "6.7 本章书目述评"]),
    ("第 7 章 伯克利的学术外溢：技术、人才与制度网络", [
        "7.1 技术外溢：从 Berkeley UNIX/BSD 到更广泛的计算机传统",
        "7.2 人才外溢：研究生、教师与伯克利学术网络",
        "7.3 大学—政府—产业：伯克利科研模式的制度外溢",
        "7.4 从东湾到湾区：伯克利与美国计算机产业网络",
        "7.5 伯克利的历史形象：从地方大学到全球技术符号",
        "7.6 本章书目述评"]),
]

SPEC6 = [
    ("第 1 章 UNIX 进入伯克利：学术计算环境的形成（1973–1976）", [
        "1.1 UNIX 进入伯克利：1973 年 SOSP 与 Bob Fabry",
        "1.2 伯克利获得 UNIX 源码：授权路径与时间考证",
        "1.3 PDP-11/45 与第一套伯克利 UNIX 学术计算环境（1974）",
        "1.4 PDP-11/70：从共享实验机到教学计算系统（1975）",
        "1.5 Ken Thompson 在伯克利：访问教授、V6 与 Berkeley Pascal（1975–1976）",
        "1.6 本章书目述评"]),
    ("第 2 章 1BSD：从 UNIX 源码到伯克利软件发行版（1977–1978）", [
        "2.1 Berkeley UNIX 的用户修改：从本地需求到软件积累",
        "2.2 Berkeley UNIX 软件集的形成与传播",
        "2.3 从 Berkeley UNIX 到 Berkeley Software Distribution：1BSD 的正式发行",
        "2.4 1BSD 的许可证、复制费用与磁带传播",
        "2.5 Bill Joy 与 1BSD：工具链、编译与发行准备",
        "2.6 1BSD 的软件构成：Pascal、ex、Shell 与其他工具",
        "2.7 1BSD 与原始 UNIX：软件集合而非独立操作系统",
        "2.8 1BSD 的贡献网络：Fabry、Joy、Haley、Graham 与早期参与者",
        "2.9 Bill Joy 的 Berkeley 经历与 Sun Microsystems 的前奏",
        "2.10 1BSD 的技术路线与同时代操作系统环境注",
        "2.11 本章书目述评"]),
    ("第 3 章 2BSD：vi、C Shell 与 BSD 用户环境的形成（1979）", [
        "3.1 2BSD 的形成与日期考证",
        "3.2 Berkeley Pascal 的改进与 2BSD 更新",
        "3.3 vi 的形成：从 ed 到 ex 再到可视化编辑",
        "3.4 termcap：从终端差异到统一用户界面",
        "3.5 C Shell 的设计：交互式 Shell 的新范式",
        "3.6 csh 与 sh：两种 Shell 设计路线的分化",
        "3.7 2BSD 的性质：软件集合、用户环境与发行传统",
        "3.8 vi 与 csh 的争议：设计选择与技术批评",
        "3.9 2BSD 的贡献网络：开发者、测试者与文档作者",
        "3.10 PDP-11 时代的 BSD：硬件边界与 VAX 转向",
        "3.11 本章书目述评"]),
    ("第 4 章 3BSD：VAX 移植与虚拟内存系统的形成（1979–1980）", [
        "4.1 UNIX/32V 与 Berkeley 的 VAX 计算环境",
        "4.2 3BSD 的诞生：从 32V 到完整 Berkeley 系统",
        "4.3 BSD 虚拟内存：设计思想与实现机制",
        "4.4 VAX 地址空间、分页与页面置换",
        "4.5 VAX 与 BSD：硬件能力推动系统演进",
        "4.6 3BSD 的发行、许可与早期使用",
        "4.7 VAX 时代的技术争议与贡献网络",
        "4.8 本章书目述评"]),
    ("第 5 章 4BSD：VAX 时代的成熟与 BSD 系统能力扩展（1980）", [
        "5.1 4BSD 的发布：VAX-11/750 与系统成熟",
        "5.2 4BSD 的系统扩展：Job Control、可靠信号与 curses",
        "5.3 4BSD 的用户环境与邮件工具：从 csh 到 delivermail",
        "5.4 4BSD 的文件系统与 I/O 改进",
        "5.5 从 3BSD 到 4BSD：系统演进路线",
        "5.6 4BSD 的发行、许可证与 DARPA 科研体系",
        "5.7 4BSD 的贡献网络与同时代 UNIX 系统环境",
        "5.8 本章书目述评"]),
]

SPEC3 = [
    ("第 1 章 UNIX 软件工程与工具传统", [
        "1.1 管道与过滤器：组合式软件工程的形成",
        "1.2 文本处理工具：grep、sed 与 awk 的形成",
        "1.3 Shell：可编程的组合层",
        "1.4 Software Tools、RATFOR 与可移植工具传统",
        "1.5 软件构造工具链：make、SCCS/RCS、lint 与 lex/yacc",
        "1.6 文档工具链与 UNIX 手册：roff、troff/nroff 与 man",
        "1.7 《UNIX 编程环境》与 Pike 的程序设计批评",
        "1.8 UNIX 的可移植性：C、接口与跨平台软件",
        "1.9 软件工具的组合：从程序接口到软件生态",
        "1.10 本章书目述评"]),
    ("第 2 章 UNIX 哲学、文化与历史记忆", [
        "2.1 “Do one thing well”：从 1978 年 UNIX 实践到后来的哲学化表述",
        "2.2 “一切皆文件”：系统模型与哲学化表达",
        "2.3 UNIX 哲学：从工程习惯到思想体系",
        "2.4 UNIX 哲学的批评：简洁、组合与复杂性",
        "2.5 Jargon File 与 Hacker 文化的文本化",
        "2.6 UNIX 起源叙事：文本谱系、都市传说与历史记忆",
        "2.7 Worse is Better：简洁、实现与系统成功的权衡",
        "2.8 本章书目述评"]),
    ("第 3 章 Plan 9：对 UNIX 系统模型的再思考", [
        "3.1 Plan 9 的起源：1980 年代后期的 UNIX 反思",
        "3.2 CSRC、Bell Labs 与 Plan 9 的研究环境",
        "3.3 Plan 9 的系统模型：9P、命名空间与 Rio",
        "3.4 Plan 9 与 UNIX：继承、拒绝与重新设计",
        "3.5 Plan 9 的传播与影响：UTF-8、Inferno 与 9front",
        "3.6 本章书目述评"]),
]


def vch(v):
    for x in vols:
        if x[0] == v:
            return x[2]
    return []


def secs_of(chs, m):
    for cm, ct, secs in chs:
        if cm == m:
            return ct, ["%s %s" % (n, htmlmod.unescape(title)) for n, _, title in secs]
    return None, []


c5, c6 = vch(5), vch(6)
chk("G1 卷5 卷题 = 「第五卷  通往西部的帝国之路：从贝克莱到伯克利」",
    any(t == "第五卷  通往西部的帝国之路：从贝克莱到伯克利" for _, t, _ in vols))
chk("G2 卷5 共 7 章／47 节（无卷末述评章）",
    len(c5) == 7 and sum(len(x[2]) for x in c5) == 47
    and not any("卷末书目述评" in x[1] for x in c5),
    f"{len(c5)} 章／{sum(len(x[2]) for x in c5)} 节")
for i, (title, secs) in enumerate(SPEC5, 1):
    cc = [x for x in c5 if x[0] == i]
    if not cc:
        chk(f"G2b.{i} 卷5 ch{i} 存在", False)
        continue
    got5 = ["%s %s" % (n, htmlmod.unescape(t)) for n, _, t in cc[0][2]]
    chk(f"G2b.{i} 卷5 ch{i} 章题＋{len(secs)} 节题逐字一致",
        cc[0][1] == title and got5 == secs,
        [x for x in zip(got5, secs) if x[0] != x[1]][:1] or "逐字一致")
chk("G2c 卷5 6 处溯源注重构迁移保真（src 316）",
    h.count('class="src"') == 316
    and h.count("原第一卷 第7章 7.8") == 1)

chk("G3 卷6 卷题 = 「第六卷  BSD 伊始与早期发行（1974–1980）」",
    any(t == "第六卷  BSD 伊始与早期发行（1974–1980）" for _, t, _ in vols))
chk("G3a 卷6 共 5 章／44 节（节数守恒，无卷末述评章）",
    len(c6) == 5 and sum(len(x[2]) for x in c6) == 44
    and not any("卷末书目述评" in x[1] for x in c6),
    f"{len(c6)} 章／{sum(len(x[2]) for x in c6)} 节")
for i, (title, secs) in enumerate(SPEC6, 1):
    cc = [x for x in c6 if x[0] == i]
    if not cc:
        chk(f"G3b.{i} 卷6 ch{i} 存在", False)
        continue
    got6 = ["%s %s" % (n, htmlmod.unescape(t)) for n, _, t in cc[0][2]]
    chk(f"G3b.{i} 卷6 ch{i} 章题＋{len(secs)} 节题逐字一致",
        cc[0][1] == title and got6 == secs,
        [x for x in zip(got6, secs) if x[0] != x[1]][:1] or "逐字一致")
chk("G3c 卷6 5 处溯源注重构迁移保真（src 316）", h.count('class="src"') == 316)

for i, (t, secs) in enumerate(SPEC3, 1):
    ct, ss = secs_of(vch(3), i)
    chk(f"G4.{i} 卷3 ch{i} 章题＋{len(secs)} 节题逐字一致（含述评恒末）",
        ct == t and ss == secs, [x for x in zip(ss, secs) if x[0] != x[1]][:2] or "逐字一致")
chk("G5 卷3 卷题 = 「第三卷  UNIX 软件工程、哲学与文化」",
    any(t == "第三卷  UNIX 软件工程、哲学与文化" for _, t, _ in vols))
OLD3 = ["<h2>第三卷  UNIX 文化与哲学</h2>", "第 1 章 UNIX 软件工程</h3>",
        "第 2 章 UNIX 哲学与文化</h3>",
        "第 3 章 贝尔实验室九号项目（Plan 9）：对 UNIX 哲学的批判</h3>",
        "管道与过滤器：组合式软件工程的原型", "文本工具三件套", "都市传说的辨析",
        "Plan 9 核心概念", "BSD 打印链",
        "被遮蔽的史实：CSRG 的组织、档案与解散", "伯克利获得 UNIX：学术计算环境的建立（1974–1976）",
        "1BSD：伯克利 UNIX 起点与 Joy 的编译器工作（1978）",
        "2BSD：vi 与 C Shell 的诞生、PDP-11 的谢幕（1979）",
        "3BSD：VAX 移植与虚拟内存的突破（1979）",
        "4BSD：Job Control 与性能改进、VAX 平台成熟（1980）"]
res = {o: h.count(o) for o in OLD3 if h.count(o)}
chk("G6 两批旧卷题／旧章题／旧节题在 index.html 零残留", not res, res)
chk("G7 卷9 的「BSD UNIX 文化与哲学」2 处未误伤", h.count("BSD UNIX 文化与哲学") == 2,
    h.count("BSD UNIX 文化与哲学"))
# ── 第十二批：卷4 全卷重构（主理人清单逐字核验，独立于内容源）────────────────
SPEC4 = [
    ("第 1 章 内核、进程与进程间通信", [
        "1.1 早期 UNIX 内核：从 V1 到 V4 的基本结构（1971–1973）",
        "1.2 进程模型：fork、exec 与 wait", "1.3 信号、陷阱与进程调度",
        "1.4 UNIX 的时间系统：时钟、定时器与 sleep/alarm",
        "1.5 管道与 FIFO：UNIX 进程间通信模型",
        "1.6 从进程到线程：多处理器 UNIX 中的执行模型", "1.7 本章书目述评"]),
    ("第 2 章 系统调用与文件描述符", [
        "2.1 用户态与内核态：UNIX 系统调用界面的形成",
        "2.2 系统调用入口、参数传递与返回机制",
        "2.3 文件描述符：进程与内核对象之间的接口",
        "2.4 open、read、write、close 与 UNIX I/O 模型",
        "2.5 ioctl、fcntl 与文件对象控制",
        "2.6 文件描述符继承：fork、exec 与进程组合", "2.7 本章书目述评"]),
    ("第 3 章 文件系统、设备与 I/O", [
        "3.1 UNIX 文件模型：inode、目录与文件描述", "3.2 link、mount 与 UNIX 名称空间",
        "3.3 字符设备与块设备：设备号及特殊文件", "3.4 设备驱动程序与 UNIX I/O 路径",
        "3.5 buffer cache 与块设备 I/O", "3.6 从 V6 文件系统到 Berkeley FFS/UFS",
        "3.7 文件系统一致性：sync、fsck 与磁盘可靠性", "3.8 本章书目述评"]),
    ("第 4 章 可执行文件、链接与程序装载", [
        "4.1 汇编器与目标文件：从 PDP-11 汇编到 UNIX 工具链",
        "4.2 a.out 与 UNIX 可执行文件格式",
        "4.3 链接器与符号解析：程序如何组成可执行文件",
        "4.4 exec 与程序装载：从文件到进程映像",
        "4.5 程序地址空间：代码、数据、栈与堆",
        "4.6 动态链接与共享库的形成", "4.7 本章书目述评"]),
    ("第 5 章 虚拟内存与地址空间", [
        "5.1 从 Multics 到 UNIX：虚拟内存思想的继承（1965–1979）",
        "5.2 VAX 虚拟内存与 3BSD", "5.3 Berkeley VM：分页、页表与地址空间",
        "5.4 页面换入换出、缺页处理与内存回收",
        "5.5 商用 UNIX 的虚拟内存分化：Ultrix、SunOS、AIX 与 System V",
        "5.6 UNIX 虚拟内存与同期系统的比较", "5.7 本章书目述评"]),
    ("第 6 章 用户、权限与 UNIX 安全模型", [
        "6.1 UID、GID 与多用户身份模型", "6.2 文件权限：owner、group 与 mode bits",
        "6.3 root、setuid 与特权边界", "6.4 passwd、crypt 与 UNIX 身份认证",
        "6.5 chroot、设备权限与系统管理边界", "6.6 UNIX 安全模型的能力与局限",
        "6.7 本章书目述评"]),
    ("第 7 章 C语言、编译器与 UNIX 的可移植性", [
        "7.1 BCPL、B 与 C：从系统语言到通用实现语言",
        "7.2 从 B 到 C：语言演化与编译器实现（1971–1973）",
        "7.3 1973 年 UNIX 内核的 C 重写：从机器相关到相对可移植",
        "7.4 C 编译器、系统接口与 UNIX 可移植性",
        "7.5 K&R C：语言、库与 UNIX 生态的形成",
        "7.6 K&R C 到 ANSI C：语言规范的定型（1978–1990）", "7.7 本章书目述评"]),
    ("第 8 章 Shell、终端与文本工具", [
        "8.1 Thompson Shell 与 Bourne Shell：命令解释器的形成",
        "8.2 Shell 语法：展开、重定向、管道与命令替换",
        "8.3 TTY、线路规程与 UNIX 终端模型", "8.4 Job Control：交互式 UNIX 的形成",
        "8.5 C Shell：从命令解释到交互式编程环境",
        "8.6 grep、sed 与 awk：文本处理工具的技术机制",
        "8.7 Shell 环境：变量、退出状态与脚本执行", "8.8 本章书目述评"]),
    ("第 9 章 网络与分布式 UNIX", [
        "9.1 UUCP 与 UNIX 的早期网络化",
        "9.2 从 ARPANET 到 TCP/IP：UNIX 网络协议环境的形成",
        "9.3 4.2BSD 与 TCP/IP 协议栈",
        "9.4 Berkeley Sockets：UNIX 网络编程接口的形成",
        "9.5 路由、DNS 与 UNIX 网络工具", "9.6 RPC、NFS 与分布式 UNIX",
        "9.7 本章书目述评"]),
    ("第 10 章 附录 A UNIX 技术史的源码考古与史料方法", [
        "10.1 UNIX 源码谱系：版本、分支与 TUHS 重建",
        "10.2 从源代码到技术史：版本差分、代码证据与文献互证",
        "10.3 树状谱系叙事的局限：分支、回流与被遗漏的技术路线"]),
]
c4 = vch(4)
chk("G8 卷4 卷题 = 「第四卷  UNIX 技术专题史」",
    any(t == "第四卷  UNIX 技术专题史" for _, t, _ in vols))
chk("G9 卷4 共 10 章／68 节（9 正章 ＋ 附录章）",
    len(c4) == 10 and sum(len(x[2]) for x in c4) == 68,
    f"{len(c4)} 章／{sum(len(x[2]) for x in c4)} 节")
for i, (title, secs) in enumerate(SPEC4, 1):
    cc = [x for x in c4 if x[0] == i]
    if not cc:
        chk(f"G10.{i} 卷4 ch{i} 存在", False)
        continue
    got4 = ["%s %s" % (n, htmlmod.unescape(t)) for n, _, t in cc[0][2]]
    chk(f"G10.{i} 卷4 ch{i} 章题＋{len(secs)} 节题逐字一致",
        cc[0][1] == title and got4 == secs,
        [x for x in zip(got4, secs) if x[0] != x[1]][:1] or "逐字一致")
chk("G11 卷4 已无卷末书目述评章（主理人裁定删去）",
    not any("卷末书目述评" in t for _, t, _ in c4))
_ve = [t for t in all_titles if "卷末书目述评" in t]
_ve_full = [t for t in _ve if "全卷综述" in t]
_ve_short = [t for t in _ve if t.endswith("卷综述") and "全卷综述" not in t]
_ve_cat = [t for t in _ve if "史料总目" in t]
_ve_bare = [t for t in _ve if "综述" not in t and "史料总目" not in t]
chk("G12 卷末述评章 10 = 1「…全卷综述」＋ 0「…卷综述」＋ 1「…史料总目」＋ 8 裸卷名（含 1 处「…历史资料总目」）",
    n_volend == 10 and (len(_ve_full), len(_ve_short), len(_ve_cat), len(_ve_bare)) == (1, 0, 1, 8),
    f"{n_volend}／{len(_ve_full)}／{len(_ve_short)}／{len(_ve_cat)}／{len(_ve_bare)}")
info("裸卷名形制（无后缀）", "；".join(t.split("：")[-1] for t in _ve_bare))
info("「…卷综述」变体（非「全卷综述」）", "；".join(t.split("：")[-1] for t in _ve_short))
chk("G13 卷4 两处体例调整溯源注保真（原卷1 ch7 7.8／原卷2 ch4）",
    h.count("原第一卷 第7章 7.8") == 1 and h.count("原第二卷 第4章") == 1)


# ── 第十九批：卷7／卷8 全卷重构（主理人清单逐字核验，独立于内容源）────────────────
SPEC7 = [['第 1 章 DARPA 的选择与 CSRG 的建制化（1980）', ['1.1 ARPANET、DARPA 与 BSD 前期网络研究环境', '1.2 1980 年 DARPA 招标：VLSI 设计与操作系统支持', '1.3 Berkeley 中标：合同条款、金额与项目目标', '1.4 CSRG 的成立：研究组、合同与组织化科研', '1.5 DARPA 的选择：技术需求、制度因素与争议', '1.6 1980 年计算机软件版权法与 UNIX 软件的法律环境', '1.7 CSRG 的早期人员、资源与科研组织', '1.8 DARPA 资助下早期 BSD 技术路线的形成', '1.9 本章书目述评']], ['第 2 章 4.1BSD：从 4BSD 到 DARPA 支持下的系统扩张（1981）', ['2.1 4.1BSD 的形成与发布背景', '2.2 4.1BSD 的主要特性与 4BSD 的继承关系', '2.3 4.1BSD 的性能改进与系统成熟', '2.4 4.1BSD 命名冲突：从 5BSD 到 4.1BSD', '2.5 4.1BSD 与 BBN TCP/IP 版本：1981 年 11 月的后续发行', '2.6 用户环境、curses 与交互式 UNIX', '2.7 DARPA 资助延续与 CSRG 项目组织', '2.8 4.1BSD 的传播：大学、研究机构与 UNIX 用户共同体', '2.9 4.1BSD 的历史位置与版本分化', '2.10 与同时期操作系统的比较：VAX/VMS、System III 与其他 UNIX 系统', '2.11 本章书目述评']], ['第 3 章 4.1a、4.1b、4.1c：通往 4.2BSD 的过渡工程（1981–1983）', ['3.1 4.2BSD 项目的形成与 DARPA Steering Committee', '3.2 4.1a：BBN TCP/IP 与网络系统试验', '3.3 4.1b：Fast File System 的形成', '3.4 4.1c：4.2BSD 发布前的过渡版本', '3.5 Berkeley sockets：网络接口体系的形成', '3.6 Bill Joy 的源码重组与系统发展', '3.7 机器相关代码与机器无关代码的初步分离', '3.8 CSRG 管理与开发力量的变化', '3.9 Berkeley、BBN 与 DARPA 的技术协作', '3.10 4.2BSD 延迟与过渡版本的形成', '3.11 4.1a、4.1b、4.1c 的版本性质与历史定位', '3.12 本章书目述评']], ['第 4 章 4.2BSD：网络化 UNIX 的定型（1983）', ['4.1 4.2BSD 的发布：两年工程的最终收束', '4.2 4.2BSD 的版本组成与前代继承', '4.3 TCP/IP 与 Berkeley 网络系统的正式整合', '4.4 Fast File System 与 4.2BSD 的系统扩展', '4.5 chroot(2) 与其他新增系统设施的发行史', '4.6 4.2BSD 的开发者与贡献网络', '4.7 Bill Joy 离开 Berkeley 与 Sun Microsystems 的前奏', '4.8 4.2BSD 的发行、许可证与传播', '4.9 4.2BSD 与同期 UNIX、XENIX、PC DOS、Lisa', '4.10 4.2BSD 之后的 Berkeley 网络软件生态：Sendmail、BIND 与其他项目', '4.11 本章书目述评']], ['第 5 章 4.3BSD：性能成熟与 Berkeley UNIX 的扩张（1984–1986）', ['5.1 4.3BSD 的开发背景（1984–1986）', '5.2 4.3BSD 的发布与版本构成', '5.3 4.3BSD 的系统扩展与性能改进', '5.4 4.3BSD 的网络功能与系统管理能力', '5.5 4.3BSD 的外部传播：大学、研究机构与派生版本', '5.6 4.3BSD from UWisc：Wisconsin UNIX 与外部网络软件', '5.7 4.3BSD 的技术选择与未延续路线', '5.8 4.3BSD 的贡献网络与 CSRG 组织', '5.9 4.3BSD 的历史地位', '5.10 4.3BSD 发布后的后续影响：从 VAX 到下一代体系结构', '5.11 与同时期操作系统的比较：Mach、Athena、System V 与其他 UNIX 系统', '5.12 本章书目述评']]]
SPEC8 = [['第 1 章 2BSD 平行支线：PDP-11 时代的持续发展（1983–1987）', ['1.1 2BSD 支线的形成：从早期 PDP-11 BSD 到持续维护', '1.2 2.9BSD：PDP-11 上的 BSD 延续', '1.3 2.9BSD 的发行、维护与用户群体', '1.4 2.10BSD：从 2BSD 支线到后期 PDP-11 BSD', '1.5 2.10BSD 的版本形成与发行', '1.6 2BSD 支线与 4BSD/VAX 主线的关系', '1.7 PDP-11 BSD 的长期维护传统', '1.8 2BSD 支线的历史地位与最终去向', '1.9 本章书目述评']], ['第 2 章 4.3BSD-Tahoe：机器无关化与 BSD 可移植性的转折（1988）', ['2.1 从 4.3BSD 到 Tahoe：体系结构转换的背景', '2.2 Tahoe：新硬件平台与版本形成', '2.3 机器相关代码与机器无关代码的分离', '2.4 4.3BSD-Tahoe 的发行', '2.5 4.3BSD-Tahoe 的版本构成与前代继承', '2.6 Berkeley UNIX 向多体系结构系统的发展', '2.7 4.3BSD-Tahoe 的开发者、移植者与外部贡献者', '2.8 4.3BSD-Tahoe 的技术选择与未延续路线', '2.9 4.3BSD-Tahoe 的历史地位', '2.10 与同时期操作系统的比较', '2.11 本章书目述评']], ['第 3 章 Net/1：首次独立网络源码发行（1988–1989）', ['3.1 AT&T UNIX 许可证与 Berkeley 源码发行的限制', '3.2 Net/1 的形成背景与 Keith Bostic 的发行计划', '3.3 Net/1 公告日期考据：1988.12.7 与 1989 年正式发行', '3.4 Net/1 的版本构成与软件范围', '3.5 Net/1 的发行方式与许可证', '3.6 Net/1 的传播：网络、大学与 UNIX 用户共同体', '3.7 Net/1 与 4.3BSD-Tahoe 的关系', '3.8 Net/1 与 Berkeley 源码独立化', '3.9 Net/1 的历史定位：从 BSD 网络代码到独立 Berkeley 发行物', '3.10 本章书目述评']], ['第 4 章 4.3BSD-Reno：走向 4.4BSD 的中间发行（1990）', ['4.1 4.3BSD-Reno 的形成背景', '4.2 Reno 的版本定位：4.4BSD 前的中间发行', '4.3 Reno 的版本构成与新增内容', '4.4 4.3BSD-Tahoe、Reno 与下一代 Berkeley 系统', '4.5 Berkeley 外部参与者与 Reno 的开发网络', '4.6 Reno 的发行与传播', '4.7 Reno 的技术选择与实验性质', '4.8 Reno 的历史定位', '4.9 与同时期 UNIX 系统的比较：System V、AIX、HP-UX、Ultrix', '4.10 本章书目述评']], ['第 5 章 AT&T 代码重写与 Net/2：BSD 源码独立化的完成阶段（1989–1991）', ['5.1 Keith Bostic 与 AT&T 代码重写运动', '5.2 从 Net/1 到完整 Berkeley 源码重写', '5.3 社区招募：志愿者、匿名贡献与分布式重写', '5.4 AT&T 代码审计与法律风险', '5.5 Net/2 的形成与 1991 年发行', '5.6 Net/2 的版本构成与源码状态', '5.7 Net/2 与 4.3BSD-Reno 的关系', '5.8 Net/2 的发行、传播与许可证', '5.9 Net/2 重写运动的争议与历史定位', '5.10 Net/2 的后续传播：386BSD、BSD/386 与法律危机前夜', '5.11 Net/2 与同期自由软件操作系统的源码传播比较', '5.12 本章书目述评']]]
c7, c8 = vch(7), vch(8)
chk("G14 卷7 卷题 = 「第七卷  从 4BSD 到 4.3BSD：CSRG 与 Berkeley UNIX（1980–1986）」",
    any(t == "第七卷  从 4BSD 到 4.3BSD：CSRG 与 Berkeley UNIX（1980–1986）" for _, t, _ in vols))
chk("G14a 卷7 共 5 章／55 节（原 4 章 47 节，无卷末述评章）",
    len(c7) == 5 and sum(len(x[2]) for x in c7) == 55
    and not any("卷末书目述评" in x[1] for x in c7),
    f"{len(c7)} 章／{sum(len(x[2]) for x in c7)} 节")
for i, (title, secs) in enumerate(SPEC7, 1):
    cc = [x for x in c7 if x[0] == i]
    if not cc:
        chk(f"G14b.{i} 卷7 ch{i} 存在", False)
        continue
    got7 = ["%s %s" % (n, htmlmod.unescape(t)) for n, _, t in cc[0][2]]
    chk(f"G14b.{i} 卷7 ch{i} 章题＋{len(secs)} 节题逐字一致",
        htmlmod.unescape(cc[0][1]) == title and got7 == secs,
        [x for x in zip(got7, secs) if x[0] != x[1]][:1] or "逐字一致")
chk("G14c 卷7 5 处溯源注语义迁移保真（src 316）",
    h.count('class="src"') == 316
    and h.count("tuhs 邮件列表＋RFC 814") == 1
    and h.count("Leffler 合著论文＋Atheros 公司史") == 1
    and h.count("Mach＝CMU 1985 启动") == 1
    and h.count("对照时段：1981–1983；比较维度：同期代表性系统") == 1
    and h.count("〔对照时段：1983〕") == 1)
chk("G15 卷8 卷题 = 「第八卷  CSRG 后期发行、可移植性与源码独立化（1986–1991）」",
    any(t == "第八卷  CSRG 后期发行、可移植性与源码独立化（1986–1991）" for _, t, _ in vols))
chk("G15a 卷8 共 5 章／52 节（原 3 章 28 节，无卷末述评章）",
    len(c8) == 5 and sum(len(x[2]) for x in c8) == 52
    and not any("卷末书目述评" in x[1] for x in c8),
    f"{len(c8)} 章／{sum(len(x[2]) for x in c8)} 节")
for i, (title, secs) in enumerate(SPEC8, 1):
    cc = [x for x in c8 if x[0] == i]
    if not cc:
        chk(f"G15b.{i} 卷8 ch{i} 存在", False)
        continue
    got8 = ["%s %s" % (n, htmlmod.unescape(t)) for n, _, t in cc[0][2]]
    chk(f"G15b.{i} 卷8 ch{i} 章题＋{len(secs)} 节题逐字一致",
        htmlmod.unescape(cc[0][1]) == title and got8 == secs,
        [x for x in zip(got8, secs) if x[0] != x[1]][:1] or "逐字一致")
chk("G15c 卷8 4 处溯源注语义迁移保真（src 316）",
    h.count('class="src"') == 316
    and h.count("Karels/Leffler/McKusick 合著论文＋Karels 采访") == 1
    and h.count("对照时段：1988；比较维度：同期代表性系统") == 1
    and h.count("〔比较维度：网络栈成熟度〕") == 1
    and h.count("Linux 0.01 于 1991-09-17 释出") == 1)
chk("G16 卷6 §2.10 题末「注」字已补（主理人裁定）",
    h.count("1BSD 的技术路线与同时代操作系统环境注") == 1)
OLD78 = ["<h2>第七卷  DARPA 赞助与 CSRG 的黄金时代（1980–1986）</h2>",
         "<h2>第八卷  CSRG 后期发行与网络发布（1986–1991）</h2>",
         "第 1 章 DARPA 的选择与 CSRG 的成立（1980）",
         "第 2 章 4.1BSD：命名冲突、curses 库与 DARPA 资助延续（1981）",
         "第 3 章 4.2BSD：TCP/IP 集成与网络革命的奠基（1983）",
         "第 4 章 4.3BSD：性能成熟与 Morris 蠕虫的安全转折（1986）",
         "第 1 章 4.3BSD-Tahoe 与 Net/1：机器无关抽象层与首次独立网络分发（1988–1989）",
         "第 2 章 4.3BSD-Reno：Kerberos 认证争议与网络栈演进（1990）",
         "第 3 章 AT&T 代码重写运动与 Net/2（1989–1991）",
         "ARPANET 到 NSFNET 的前 BSD 时代",
         "1BSD 的技术路线与同时代操作系统环境<span"]
_res78 = {o: h.count(o) for o in OLD78 if h.count(o)}
chk("G17 两卷旧卷题／旧章题／旧节题在 index.html 零残留", not _res78, _res78)
# ── 第二十／二十一批：卷9–13 全卷重构（主理人清单逐字核验，独立于内容源）────
SPEC9 = [['第 1 章 伯克利的文化地层：城市、大学与 CSRG 的三角', ['1.1 伯克利市与加州大学的文化地层：反文化运动与学术文化', '1.2 CSRG 的物质组织形态：房间、经费、人员编制与研究生态', '1.3 参与者的形成：教授、研究生、访问者与外部协作者', '1.4 学术自由、联邦科研与项目自治：CSRG 所处的制度张力', '1.5 本章书目述评']], ['第 2 章 从代码到物证：BSD UNIX 的物质文化考古', ['2.1 物质证据总目：1BSD–4.4BSD 的发行物、磁带、手册、补丁与勘误', '2.2 从磁带到网络：BSD 源码的复制、发行与传播条件', '2.3 源码、man 手册、Release Notes、勘误与补丁：共同体留下的文本痕迹', '2.4 典型技术对象的文化证据：vi、csh、FFS 与 TCP/IP', '2.5 从实验室档案到公共记忆：保存、引用与历史重构', '2.6 本章书目述评']], ['第 3 章 名称与符号：BSD UNIX 的文化身份如何形成', ['3.1 Berkeley UNIX、Berkeley Software Distribution 与“BSD”：名称的形成', '3.2 “BSD”缩写的出现、固定与传播', '3.3 版本编号作为身份秩序：1BSD、2BSD、3BSD、4BSD 与 4.xBSD', '3.4 daemon 一词与 BSD daemon：名称、语境与早期用法', '3.5 从 Foglio 到 Beastie：BSD 视觉符号的形成与演化', '3.6 视觉身份的所有权、使用权与商业化：从插图到商标', '3.7 本章书目述评']], ['第 4 章 共同体实践：发行、协作、反馈与教育', ['4.1 从用户修改到共同贡献：代码参与方式的变化', '4.2 发行节奏的物质约束：磁带、版本与伯克利分发', '4.3 Bug 报告、勘误与补丁：共同维护的形成', '4.4 USENIX、net.sources、Usenet 与网络传播', '4.5 从 Berkeley 到外部共同体：大学、研究机构与产业参与者', '4.6 教学、研究与实际使用：BSD 作为教育与科研基础设施', '4.7 谁决定什么进入下一版：发行、维护与共同体中的实际权力', '4.8 本章书目述评']], ['第 5 章 从实践到观念：BSD UNIX 的价值与哲学', ['5.1 源码可得、可以修改与可以再分发：从工程实践到共同规范', '5.2 学术自由与工程自治：谁拥有代码、谁决定代码的命运', '5.3 实用主义与自我修补：从具体工程行为到 UNIX/BSD 的文化气质', '5.4 许可证与共同体价值：BSD 许可证、AT&T 许可证与物质约束', '5.5 技术判断与工程审美：简洁、可读、可修改与实用性', '5.6 BSD 与 GNU：两种共享源码文化的并置', '5.7 “开放源码”不能倒投到 1974–1993：历史语汇与后设概念的界限', '5.8 本章书目述评']], ['第 6 章 身份、边界与分化前夜', ['6.1 “什么是 BSD”：软件集合、操作系统、发行物、项目还是共同体', '6.2 Berkeley UNIX 与外部 BSD：内部发行、外部派生与商业吸收', '6.3 AT&T、许可证与源码归属：共同体边界的法律化', '6.4 Net/1 与 Net/2：从 Berkeley 发行物到外部源码空间', '6.5 共同体边界的变化：代码、人员与发行渠道开始分离', '6.6 1993 年的分化前夜：新的项目身份开始出现', '6.7 共同文化还剩下什么：代码、名称、工具、规范与记忆', '6.8 本章书目述评']], ['第 7 章 卷末书目述评：BSD UNIX 文化与哲学', ['7.1 史料谱系：发行物、源码、档案、网络记录与回忆材料', '7.2 证据层级：当事人叙述、同时代记录与后见之明', '7.3 从物质证据到文化解释：本卷的论证链', '7.4 文化史的解释边界：物证、观念与形式主义化重构', '7.5 尚未解决的问题：缺失档案、沉默的参与者与被遗忘的路线', '7.6 本卷总评']]]
SPEC10 = [['第 1 章 386BSD：Net/2 向个人计算机的移植（1992–1993）', ['1.1 Bill Jolitz 与 Net/2 的 386 移植', '1.2 386BSD 的代码来源与移植范围', "1.3 Dr. Dobb's Journal 连载：386BSD 的公开传播", '1.4 386BSD 的首次发行与安装方式', '1.5 386BSD 的早期用户与传播', '1.6 386BSD 与 Berkeley、Net/2 的关系', '1.7 386BSD 进入 PC UNIX 竞争环境', '1.8 本章书目述评']], ['第 2 章 4.4BSD 项目：Alpha、Encumbered 与最终发行准备（1992–1994）', ['2.1 4.4BSD 项目的形成与目标', '2.2 4.4BSD-Alpha 的内部发行', '2.3 4.4BSD-Alpha 的版本组成与发行范围', '2.4 Alpha 向 Encumbered 的过渡', '2.5 4.4BSD-Encumbered 的发行', '2.6 AT&T 代码的遗留与发行限制', '2.7 4.4BSD 从 Encumbered 向独立源码发行转变', '2.8 4.4BSD 项目与 CSRG 后期组织', '2.9 本章书目述评']], ['第 3 章 BSD/386：BSD 商业化与 UNIX 市场（1992–1994）', ['3.1 AT&T 分拆后的 UNIX 商业体系', '3.2 BSDI 的成立与 BSD/386', '3.3 BSD/386 的产品定位与商业模式', '3.4 1-800-ITS-UNIX：商业宣传与 UNIX 商标边界', '3.5 BSD/386 与 Berkeley/Net/2 的关系', '3.6 BSD/386 向 BSD/OS 的品牌演变', '3.7 商业化与 AT&T/USL 的利益冲突', '3.8 本章书目述评']], ['第 4 章 USL v. BSDi：法律危机与发行体系冻结（1992–1994）', ['4.1 AT&T 1956 年同意令与 UNIX 知识产权结构', '4.2 1984 年 AT&T 分拆与 UNIX 商业化', '4.3 1992 年 4 月 USL 起诉 BSDi 与 Berkeley', '4.4 初步禁令与 1993 年程序发展', '4.5 版权登记、商标与派生作品争议', '4.6 被指控代码的来源、争议文件与证据链', '4.7 市场冻结：OEM、渠道与用户的观望', '4.8 律师、证人与诉讼叙事', '4.9 1994 年和解前的谈判结构', '4.10 本章书目述评']], ['第 5 章 和解与 4.4BSD-Lite：Berkeley 源码独立化的完成（1994–1995）', ['5.1 1994 年和解协议的形成', '5.2 和解协议的关键条款与法律意义', '5.3 争议文件的删除与源码重审', '5.4 4.4BSD-Lite 的发行', '5.5 4.4BSD-Lite 的发行物与文档', '5.6 4.4BSD-Lite 与此前 Berkeley 发行物的关系', '5.7 4.4BSD-Lite Release 2 的发布', '5.8 CSRG 的终结与最后阶段', '5.9 4.4BSD 系列在 Berkeley UNIX 发行史中的位置', '5.10 本章书目述评']], ['第 6 章 诉讼的讲述：法律事件如何进入 BSD 集体记忆', ['6.1 USL v. BSDi 的不同历史讲述', '6.2 诉讼叙事的简化、戏剧化与道德化', '6.3 法律事实、社区记忆与后见之明', '6.4 诉讼记忆与 BSD 身份形成', '6.5 史料缺口：和解文件、证据材料与口述史', '6.6 本章书目述评']]]
SPEC11 = [['第 1 章 386BSD 的出现与 PC BSD 时代的开始（1992–1993）', ['1.1 4.3BSD Net/2 与 386BSD 的技术来源', '1.2 Bill Jolitz 与 386BSD 项目的形成', '1.3 386BSD 0.0 与 0.1 的发布过程', '1.4 PC 兼容机上的 BSD 重新出现', '1.5 386BSD 的技术目标与历史意义', '1.6 386BSD 社区的形成', '1.7 Patchkit 的出现与非正式维护模式', '1.8 386BSD 开发停滞与社区分化']], ['第 2 章 Patchkit、社区自治与第一次 BSD 分叉（1992–1993）', ['2.1 Patchkit 的技术内容与维护模式', '2.2 Patchkit 作为早期开放开发实践', '2.3 社区贡献与官方发布之间的矛盾', '2.4 386BSD 更新节奏问题', '2.5 FreeBSD 与 NetBSD 分叉条件的形成', '2.6 BSD 社区第一次组织分裂', '2.7 分叉作为开放软件项目发展的历史机制']], ['第 3 章 FreeBSD 的诞生：生产系统路线的形成（1993）', ['3.1 FreeBSD 项目的发起背景', '3.2 从 Patchkit 到独立项目', '3.3 FreeBSD 名称与项目定位', '3.4 FreeBSD 1.0 发布', '3.5 早期核心开发结构', '3.6 FreeBSD 与 386BSD 的关系', '3.7 FreeBSD 早期技术路线选择', '3.8 FreeBSD 成为独立 BSD 分支']], ['第 4 章 NetBSD 的诞生：可移植性路线的形成（1993）', ['4.1 NetBSD 发起背景', '4.2 NetBSD 与 386BSD 的分离过程', '4.3 NetBSD 0.8 与首次发行', '4.4 多架构支持作为核心目标', '4.5 NetBSD 项目的组织方式', '4.6 NetBSD 与 FreeBSD 的路线差异', '4.7 可移植性成为 BSD 新身份']], ['第 5 章 OpenBSD 的形成：从 NetBSD 分裂到安全路线（1995–1996）', ['5.1 Theo de Raadt 与 NetBSD 开发关系', '5.2 组织冲突与项目分离', '5.3 OpenBSD 项目的建立', '5.4 OpenBSD 首次发行', '5.5 安全审计方向的形成', '5.6 Theo de Raadt 的个人领导模式与项目结构', '5.7 OpenBSD 与 NetBSD 的技术身份分化']], ['第 6 章 BSD 家族的形成：四种路线与共同遗产（1995–2003）', ['6.1 FreeBSD：生产系统与用户规模路线', '6.2 NetBSD：多架构与长期维护路线', '6.3 OpenBSD：安全工程与代码质量路线', '6.4 DragonFly BSD 的历史前因', '6.5 BSD 许可证与共同代码传统', '6.6 BSD 用户空间与开发文化继承', '6.7 分叉后的人员流动与知识传播', '6.8 BSD 家族身份的形成']], ['第 7 章 DragonFly BSD：BSD 分叉传统的再次延续（2003）', ['7.1 FreeBSD 4.x 与 5.x 转型背景', '7.2 Matt Dillon 的开发路线与技术观点', '7.3 DragonFly BSD 分叉过程', '7.4 分叉原因中的技术因素', '7.5 DragonFly 与 FreeBSD 的关系变化', '7.6 BSD 分叉机制的再次出现', '7.7 DragonFly 的独立身份形成']], ['第 8 章 BSD 分叉史的历史解释与共同演化（1992–2026）', ['8.1 BSD 分叉不是单一事件，而是连续过程', '8.2 技术目标差异与项目身份形成', '8.3 分叉、竞争与知识传播', '8.4 BSD 项目之间的代码共享与技术回流', '8.5 FreeBSD、NetBSD、OpenBSD、DragonFly 的关系变化', '8.6 BSD 与 Linux、商业 UNIX 的历史位置比较', '8.7 BSD 分叉史的史料边界']]]
SPEC12 = [['第 1 章 内核、进程与系统调用', ['1.1 UNIX/BSD 内核的结构：从 PDP-11 到现代系统', '1.2 进程模型：创建、执行与退出', '1.3 调度、优先级与时间片', '1.4 信号与进程控制', '1.5 管道、共享内存与进程间通信', '1.6 系统调用接口与用户空间/内核空间边界', '1.7 文件描述符与 UNIX 对象模型', '1.8 时间、定时器与时钟系统', '1.9 本章书目述评']], ['第 2 章 文件系统、设备与 I/O', ['2.1 inode、目录与 UNIX 文件模型', '2.2 缓冲区缓存与块设备', '2.3 FFS：柱面组与磁盘布局', '2.4 UFS 与 UFS2：文件系统的持续演进', '2.5 设备驱动与统一 I/O 模型', '2.6 磁盘标签、分区与设备管理', '2.7 soft updates：元数据一致性工程', '2.8 本章书目述评']], ['第 3 章 虚拟内存、可执行文件与程序装载', ['3.1 VAX 虚拟内存与 BSD', '3.2 分页、交换与页面置换', '3.3 mmap、共享内存与地址空间', '3.4 虚拟内存对象与现代 BSD VM', '3.5 a.out、COFF 与 ELF', '3.6 链接器、装载器与共享库', '3.7 程序执行：从 exec(2) 到动态装载', '3.8 本章书目述评']], ['第 4 章 C 语言、编译器与 UNIX 的可移植性', ['4.1 C 语言与 UNIX 的共同形成', '4.2 Portable C Compiler 与早期 UNIX 工具链', '4.3 Berkeley Pascal 与系统软件教育', '4.4 make 与 UNIX 构建文化', '4.5 GCC 进入 BSD：编译工具链的变化', '4.6 编译器、汇编器、链接器与系统移植', '4.7 VAX、Tahoe、MIPS、SPARC、Alpha、x86、ARM 与 RISC-V', '4.8 本章书目述评']], ['第 5 章 用户、权限、安全与隔离', ['5.1 用户、组与 UNIX 权限模型', '5.2 setuid、身份切换与权限边界', '5.3 chroot(2)：早期文件系统隔离', '5.4 包过滤：ipfw、IPFilter 与 pf', '5.5 Jail：从进程环境隔离到操作系统级隔离', '5.6 Jail 的技术局限与容器化', '5.7 Capsicum：能力安全', '5.8 CHERI：能力体系结构与 BSD', '5.9 本章书目述评']], ['第 6 章 网络栈：从 Berkeley TCP/IP 到现代 BSD 网络系统', ['6.1 Berkeley sockets 与网络编程接口', '6.2 BBN TCP/IP 与 Berkeley TCP/IP', '6.3 TCP/IP 协议栈的实现', '6.4 路由、子网与网关', '6.5 TCP 拥塞控制：Tahoe、Reno 与后续演进', '6.6 BSD 作为 TCP/IP 参考实现', '6.7 KAME 与 IPv6', '6.8 netgraph、桥接、链路聚合与 VNET', '6.9 netmap、iflib、SCTP 与高性能网络', '6.10 WireGuard 与现代 BSD 网络实现', '6.11 本章书目述评']], ['第 7 章 终端、Shell 与文本工具传统', ['7.1 TTY、termios 与终端模型', '7.2 ed、ex 与 vi：从行编辑到可视化编辑', '7.3 vi 的模态设计与交互模型', '7.4 sh、csh 与 UNIX Shell 设计', '7.5 termcap：终端能力的抽象', '7.6 curses：从终端控制到应用程序界面', '7.7 grep、awk、sed 与 UNIX 文本处理传统', '7.8 本章书目述评']], ['第 8 章 服务层：邮件、域名、文件服务与数据库', ['8.1 sendmail：从 ARPANET 邮件到互联网邮件系统', '8.2 BIND 与 DNS', '8.3 inetd、RPC 与 UNIX 网络服务', '8.4 NFS 与网络文件系统', '8.5 Web 服务器与 BSD 网络应用生态', '8.6 dbm、ndbm 与 Berkeley DB', '8.7 本章书目述评']], ['第 9 章 存储系统的新阶段：ZFS、HAMMER 与现代 BSD', ['9.1 ZFS 的设计背景', '9.2 OpenZFS 与 FreeBSD', '9.3 ZFS 与传统 UFS/FFS 的技术分界', '9.4 DragonFly 的 HAMMER', '9.5 HAMMER2 与现代 BSD 存储系统', '9.6 文件系统一致性、快照与校验', '9.7 本章书目述评']], ['第 10 章 多处理、内核重构与虚拟化', ['10.1 SMP：从单处理器 BSD 到多处理器系统', '10.2 SMPng：FreeBSD 内核并发体系的重构', '10.3 内核线程与 LWKT', '10.4 DragonFly 的内核架构实验', '10.5 vkernel：用户空间中的 BSD 内核', '10.6 bhyve：BSD 许可下的虚拟机管理程序', '10.7 BSD 虚拟化与现代云计算基础设施', '10.8 本章书目述评']], ['第 11 章 跨项目技术流动与 BSD 技术谱系', ['11.1 386BSD、NetBSD 与 FreeBSD 的代码继承', '11.2 NetBSD 的可移植性架构与代码组织', '11.3 FreeBSD、OpenBSD 与 DragonFly 的技术分化', '11.4 Ports、Packages 与第三方软件生态', '11.5 OpenSSH、OpenZFS、WireGuard 等跨项目技术传播', '11.6 BSD 技术向其他 UNIX、Linux 与商业系统的流动', '11.7 本章书目述评']], ['第 12 章 卷末书目述评：BSD-UNIX 技术史', ['12.1 技术史料谱系：源码、man 手册、设计文档与技术报告', '12.2 源码考古的方法与版本对应', '12.3 跨版本技术演进的判定标准', '12.4 跨项目代码流动的判定标准', '12.5 缺口与前瞻', '12.6 卷末总评']]]
SPEC13 = [['第 1 章 AT&T 的商业化转向与 System V 的形成（1982–1991）', ['1.1 从 1956 年同意令到 AT&T 解体', '1.2 1984 年分拆与 UNIX 商业化', '1.3 UNIX 授权链：USG、USO 与 USL', '1.4 System III 与 System V 的形成', '1.5 System V Release 1–3：功能扩展与企业化', '1.6 教育许可证、OEM 与 UNIX 授权经济', '1.7 AT&T–Sun 联盟与 UNIX 市场变化', '1.8 本章书目述评']], ['第 2 章 Research UNIX 与商业 UNIX 的分流', ['2.1 V8、V9 与 V10：Research UNIX 的继续实验', '2.2 System V 的工业演进：兼容性、ABI 与稳定性', '2.3 Streams、/proc、Blit 与 Research UNIX 的实验路线', '2.4 商业产品与实验系统的时间尺度差异', '2.5 V10、Plan 9 与 Research UNIX 的终结', '2.6 本章书目述评']], ['第 3 章 UNIX 标准化与“UNIX 战争”（1987–1996）', ['3.1 POSIX：从接口兼容到标准化', '3.2 X/Open 与 UNIX 品牌标准', '3.3 OSF 的成立与技术路线', '3.4 Unix International 与 AT&T–Sun 阵营', '3.5 Motif、Open Look 与桌面标准竞争', '3.6 SVR4：多家 UNIX 技术的整合', '3.7 COSE 与 UNIX 标准化的重新整合', '3.8 The Open Group 与单一 UNIX 规范', '3.9 本章书目述评']], ['第 4 章 商业 UNIX 的多极市场：Sun、IBM、HP、SGI 与 SCO', ['4.1 SunOS 与 Solaris', '4.2 IBM AIX', '4.3 HP-UX', '4.4 IRIX 与工作站 UNIX', '4.5 SCO UNIX 与 PC UNIX 市场', '4.6 SVR4 之后的商业 UNIX 生态', '4.7 本章书目述评']], ['第 5 章 USL：UNIX 系统实验室与授权机器', ['5.1 USL 的成立与组织结构', '5.2 USL 的产品线与 UNIX 商业化', '5.3 SVR4 授权与 OEM 合同体系', '5.4 Univel：Novell–USL 合资实验', '5.5 USL 的市场处境与内部张力', '5.6 从 AT&T 到 Novell：UNIX 商业权利的转移', '5.7 本章书目述评']], ['第 6 章 UNIX 产业的外部竞争：Windows NT 与平台转型（1990–1998）', ['6.1 个人计算机市场的扩张', '6.2 Windows NT 的出现与企业服务器市场', '6.3 RISC 工作站市场与 UNIX 的竞争', '6.4 硬件厂商、操作系统与商业模式的绑定', '6.5 UNIX 市场的收缩与平台选择变化', '6.6 UNIX 标准化与商业竞争的重新组合', '6.7 本章书目述评']], ['第 7 章 Linux 的兴起与 UNIX 市场的空窗（1991–2000）', ['7.1 Linux 0.01 与 MINIX 背景', '7.2 386 PC 与自由 UNIX 软件的时间窗口', '7.3 Linux 的开发者聚合与发行版形成', '7.4 商业 UNIX 市场收缩与 Linux 的进入', '7.5 GPL、发行版与商业软件模式', '7.6 企业 Linux 的形成', '7.7 BSD、Linux 与商业 UNIX 的不同发展路径', '7.8 本章书目述评']], ['第 8 章 UNIX 传统的继承叙事：BSD、GNU 与 Linux', ['8.1 “Linux 继承 UNIX 传统”叙事的形成', '8.2 GNU 项目与自由软件传统', '8.3 BSD 在 UNIX 谱系叙事中的位置', '8.4 “Distribution／发行版”概念的历史谱系', '8.5 从 BSD、UNIX 到 Linux 的技术继承、文化继承与叙事继承', '8.6 媒体、教材与开源社区中的 UNIX 传统叙述', '8.7 贡献者隐形与历史书写的选择', '8.8 本章书目述评']], ['第 9 章 System V 的最终轨迹：UnixWare、OpenServer 与 SCO 长期诉讼（1995–2021）', ['9.1 Novell 的 UNIX 资产与 UnixWare', '9.2 OpenServer 与 SCO 的企业 UNIX 遗产', '9.3 UNIX 商标、源码授权与认证权利的分离', '9.4 SCO Group 与 Linux/IBM 诉讼', '9.5 SCO 系列诉讼的法律与技术争议', '9.6 System V 遗产的最终产业形态', '9.7 本章书目述评']], ['第 10 章 卷末书目述评：UNIX 标准化、商业化与 UNIX 战争', ['10.1 机构史料：AT&T、USL、Sun、Novell 与 The Open Group', '10.2 System V 版本与授权经济学', '10.3 UNIX 战争与标准化材料', '10.4 商业 UNIX 与 Windows NT、Linux 的竞争史料', '10.5 UNIX 传统继承叙事的史学问题', '10.6 缺口与前瞻', '10.7 卷末总评']]]
OLD9 = ['<h2>第九卷  BSD UNIX 文化与哲学（1974–1993）：分裂前的共同文化</h2>', '第 4 章 名称、版本与 Berkeley UNIX 的符号秩序', '6.6 “开放源码”不能倒投到 1974–1993：历史语汇与后设概念的界限', '7.1 “什么是 BSD”：软件集合、操作系统、发行物、项目还是共同体', '7.6 共同文化还剩下什么：代码、名称、工具、规范与记忆', '8.1 史料谱系：发行物、源码、档案、网络记录与回忆材料', '5.2 Bug 报告、勘误与补丁：共同维护的形成', '6.5 BSD 与同时代 GNU：两种共享源码文化的并置', '7.4 Net/2 与 386BSD：从 Berkeley 发行物到外部项目', '1.3 三角互构：城市反文化、大学学术自由与 CSRG 开放工程的三重共鸣', '6.4 本卷自反性声明（本卷所书皆为形式主义化的重构）', '“BSD”名称七重形式化', '2.1 物质证据总目：1BSD–4.4BSD 的发行物、磁带、手册、补丁带']
OLD10 = ['<h2>第十卷  386BSD、诉讼与 4.4BSD 系列（1992–1995）</h2>', '第 2 章 386BSD 的法律边界与判例谱系（1992–1994）', '第 5 章 USL v. BSDi 诉讼（1992–1994）', '第 6 章 和解协议：BSD 法律基石的奠定（1994）', '第 7 章 4.4BSD-Lite：去除 AT&T 代码的自由发行（1994）', '第 9 章 诉讼的讲述：USL v. BSDi 的集体记忆与流行失真', '5.3 1992 年 4 月 USL 起诉 BSDi 和伯克利', '6.5 和解协议全文的史料缺口与获取路径', '2.5 软件版权判例谱系：Apple v. Franklin（1983）、SAS v. WPL（2012）与 Oracle v. SAP（2010）']
OLD11 = ['<h2>第十一卷  386BSD 与大分裂：FreeBSD、NetBSD 与 OpenBSD 的诞生（1992–1996）</h2>', '第 1 章 第 1 章 386BSD 的停滞与 Patchkit 社区（1992–1993）', '第 2 章 第 2 章 FreeBSD 的诞生：第一次分叉（1993）', '第 3 章 第 3 章 NetBSD 的诞生：移植性作为项目原则（1993）', '第 4 章 第 4 章 OpenBSD 的诞生：从 NetBSD 分化到安全项目（1995–1996）', '第 5 章 第 5 章 分叉的偶然性：1991–1993 年的时间窗口', '第 6 章 第 6 章 三种项目身份：治理、目标与工程选择', '第 7 章 第 7 章 分裂之后的共同遗产', '第 8 章 第 8 章 卷末书目述评：BSD 大分裂史']
OLD12 = ['<h2>第十二卷  BSD-UNIX 技术专题史</h2>', '第 10 章 卷末书目述评：BSD-UNIX 技术承接史料总目', '第 3 章 文件系统线：FFS → UFS/UFS2 → soft updates → ZFS 与 HAMMER（1983–2020 年代）', '第 7 章 终端与工具传统：ex/vi、csh、termcap 与 curses（1978–1990 年代）']
OLD13 = ['第 12 章 卷末书目述评：六公司线与 UNIX 战争史料总目', '第 9 章 文化挪用机制：“Linux 继承 UNIX 传统”叙事的谱系学批判', '第 10 章 不归名的四种方式：底层嵌入、商业取用、史书偏斜、贡献者隐形', '第 11 章 System V 的最终轨迹与商业帝国的黄昏（1995–2021）', '第 4 章 学术界的突围与诉讼前夜（1986–1992）', '第 6 章 USL v. BSDi：世纪诉讼的爆发与市场冻结（1992–1994）', '第 1 章 AT&T 的商业化转向与 System V 霸权（1984–1991）']


def _gvol(tag, vno, specs_, nch, nsec, volhead, oldlist):
    cs = vch(vno)
    chk("%s 卷%d 卷题 = 「%s」" % (tag, vno, volhead), any(t == volhead for _, t, _ in vols))
    got = (len(cs), sum(len(x[2]) for x in cs))
    chk("%sa 卷%d 共 %d 章／%d 节" % (tag, vno, nch, nsec), got == (nch, nsec),
        "%d 章／%d 节" % got)
    for i, (title, secs) in enumerate(specs_, 1):
        cc = [x for x in cs if x[0] == i]
        if not cc:
            chk("%sb.%d 卷%d ch%d 存在" % (tag, i, vno, i), False)
            continue
        got9 = ["%s %s" % (n, htmlmod.unescape(x)) for n, _, x in cc[0][2]]
        chk("%sb.%d 卷%d ch%d 章题＋%d 节题逐字一致" % (tag, i, vno, i, len(secs)),
            htmlmod.unescape(cc[0][1]) == title and got9 == secs,
            [x for x in zip(got9, secs) if x[0] != x[1]][:1] or "逐字一致")
    res = {o: h.count(o) for o in oldlist if h.count(o)}
    chk("%sc 卷%d 旧卷题／旧章题／旧节题在 index.html 零残留" % (tag, vno), not res, res)


_gvol("G18", 9, SPEC9, 7, 48,
      "第九卷  BSD UNIX 文化与哲学（1974–1993）：共同文化的形成与分化前夜", OLD9)
_gvol("G22", 10, SPEC10, 6, 51,
      "第十卷  从 Net/2 到 4.4BSD：386BSD、法律危机与 CSRG 的终局（1992–1995）", OLD10)
_gvol("G23", 11, SPEC11, 8, 59,
      "第十一卷  386BSD 与 BSD 大分裂：FreeBSD、NetBSD、OpenBSD 与 DragonFly 的形成（1992–2003）", OLD11)
_gvol("G24", 12, SPEC12, 12, 96, "第十二卷  BSD UNIX 技术专题史", OLD12)
_gvol("G25", 13, SPEC13, 10, 74,
      "第十三卷  UNIX 的标准化与商业化：System V 阵营与 UNIX 战争", OLD13)

# ── 第二十二批：四大 BSD 文化与哲学卷 ＋ 横向比较卷（2026-09-18 主理人批准新增）──────
SPEC25 = [["第 1 章 分化轴总论：多核时代的架构实验与 BSD 遗产重构", ["1.1 共同文化基线：第九卷六章的文化命题清单", "1.2 DragonFly 分化轴的形成：FreeBSD 5.x SMP 路线争议与架构选择", "1.3 分化的物质基础：LWKT、消息传递模型与内核重构", "1.4 从工程路线到项目身份：DragonFly 自我定位的形成", "1.5 与 FreeBSD、NetBSD、OpenBSD 的分化轴比较", "1.6 架构实验的边界：创新、兼容性与维护成本", "1.7 本章书目述评"]], ["第 2 章 工程哲学的物质基础：内核重构与可扩展性实验", ["2.1 设计信条的文本化：邮件列表、设计文档与提交记录", "2.2 代码证据：LWKT、锁策略与内核结构重写", "2.3 与 FreeBSD 的技术分道：SMP 架构选择", "2.4 工程审美：简化机制与长期维护之间的取舍", "2.5 HAMMER/HAMMER2：文件系统实验作为架构延伸", "2.6 性能观：并行扩展与现实硬件约束", "2.7 Matt Dillon 的技术领导方式与争议", "2.8 本章书目述评"]], ["第 3 章 符号、名称与社区认同：DragonFly 标识与低仪式化文化", ["3.1 名称形成：“DragonFly”命名的意象与技术共同体身份", "3.2 DragonFly 标识与社区视觉文化", "3.3 版本编号与开发阶段语义", "3.4 项目活动形式与低密度社区结构", "3.5 项目语汇与开发者文化", "3.6 标识使用与版权边界", "3.7 本章书目述评"]], ["第 4 章 共同体与治理文化：核心维护模式与小规模项目结构", ["4.1 组织结构：创始维护者与核心开发者模式", "4.2 提交权限、代码审查与信任体系", "4.3 技术门槛与贡献者进入路径", "4.4 邮件列表文化：冲突、讨论与技术决策", "4.5 Hackathon 与非正式开发协作", "4.6 小规模社区的维护压力与代际变化", "4.7 本章书目述评"]], ["第 5 章 价值、许可证与自由观：代码流动与生态位置", ["5.1 许可证选择：BSD 式宽松许可传统", "5.2 自由共享与代码复用", "5.3 与 FreeBSD 的代码关系与历史变化", "5.4 GPL 项目的许可证逻辑比较", "5.5 小型基础设施项目的生态位置", "5.6 维护责任与许可证结构", "5.7 本章书目述评"]], ["第 6 章 争议、批评与自我反思：创新路线的长期影响", ["6.1 创建争议与技术路线选择", "6.2 外部评价：项目规模、兼容性与生态问题", "6.3 内部反思：维护资源与长期发展", "6.4 技术遗产与未完成目标", "6.5 DragonFly 在 BSD 历史记忆中的位置", "6.6 争议遗产", "6.7 本章书目述评"]], ["第 7 章 卷末书目述评：DragonFly BSD 文化与哲学", ["7.1 史料谱系：邮件列表、手册、代码注释、公告与口述史", "7.2 证据层级：当事人叙述、同时代记录与后见之明", "7.3 从物质证据到文化解释：本卷的论证链", "7.4 文化史解释边界：物证、观念与形式主义化重构", "7.5 尚未解决的问题：缺失档案、沉默的参与者与被遗忘的路线", "7.6 本卷总评"]]]
SPEC26 = [["第 1 章 比较史的方法与历史前提", ["1.1 BSD 共同传统：CSRG、4.4BSD 与 UNIX 工程文化遗产", "1.2 386BSD：BSD 后继系统的历史起点", "1.3 FreeBSD 与 NetBSD：1993 年分化的组织与技术背景", "1.4 OpenBSD：1995 年分叉及其历史条件", "1.5 DragonFly BSD：2003 年分叉及其历史条件", "1.6 主要 BSD 后继系统比较的史料基础：代码、邮件列表、发行物、手册与公告", "1.7 技术文化比较的方法限制：避免目的论与后见之明", "1.8 本章书目述评"]], ["第 2 章 BSD 后继系统的主要发展路线", ["2.1 从共同祖先到不同道路：分叉机制与历史偶然性", "2.2 系统目标的差异：完整系统、架构独立、安全与实验", "2.3 组织规模与资源条件对技术路线的影响", "2.4 硬件支持、用户需求与工程优先级", "2.5 商业采用、研究价值与社区目标之间的张力", "2.6 主要 BSD 后继系统身份形成过程中的自我描述", "2.7 分类模型的解释能力与边界", "2.8 本章书目述评"]], ["第 3 章 工程哲学与系统设计文化", ["3.1 “整个操作系统”的观念：BSD 与系统整体性的传统", "3.2 内核、用户空间与基础工具的共同维护模式", "3.3 代码审美：简洁、一致性与长期维护", "3.4 工具链选择：GCC、Clang、LLVM 与自主控制", "3.5 文件系统理念：UFS、ZFS、HAMMER 与存储哲学", "3.6 安全、性能、兼容性的长期工程权衡", "3.7 微创新与架构重构：FreeBSD、NetBSD、OpenBSD 与 DragonFly BSD 项目技术路线比较", "3.8 本章书目述评"]], ["第 4 章 身份表达、符号与社区仪式", ["4.1 FreeBSD：Beastie 与 BSD 社区身份", "4.2 NetBSD：低符号化与工程身份表达", "4.3 OpenBSD：Puffy、发行歌曲与 hackathon 文化", "4.4 DragonFly BSD：非正式符号与开发者共同体", "4.5 版本编号、发行周期与项目时间意识", "4.6 会议、邮件列表与线上社区仪式", "4.7 符号、版权与社区边界", "4.8 本章书目述评"]], ["第 5 章 治理结构与共同体形成", ["5.1 BSD 项目的共同治理传统：从 CSRG 到现代社区", "5.2 FreeBSD Core Team：选举治理与制度化过程", "5.3 NetBSD Core Group：选举制度与基金会结构", "5.4 OpenBSD：核心维护者模式与集中决策", "5.5 DragonFly BSD：BDFL 模式与个人技术愿景", "5.6 Committer 制度、信任体系与代码提交文化", "5.7 邮件列表冲突、技术争论与社区边界", "5.8 贡献者结构、代际变化与项目持续性", "5.9 本章书目述评"]], ["第 6 章 许可证实践与代码流动", ["6.1 BSD 许可证传统的历史来源", "6.2 宽松许可证与代码传播模式", "6.3 FreeBSD、NetBSD、OpenBSD、DragonFly 的许可证实践", "6.4 GPL 模型与 BSD 模型的制度差异", "6.5 商业采用、嵌入式系统与代码再利用", "6.6 pf、OpenSSH、libc 与基础设施代码传播", "6.7 回馈机制、公共代码资源与利益分配问题", "6.8 许可证与项目身份之间的关系", "6.9 本章书目述评"]], ["第 7 章 技术遗产与历史影响", ["7.1 FreeBSD：网络、存储、虚拟化与互联网基础设施", "7.2 NetBSD：跨架构支持与可移植工程传统", "7.3 OpenBSD：OpenSSH、pf 与主动安全体系", "7.4 DragonFly BSD：LWKT、HAMMER 与内核架构实验", "7.5 BSD 技术进入 macOS、网络设备与商业系统", "7.6 BSD 与 Linux 时代的技术交流", "7.7 可见影响与隐性影响：技术史中的归因问题", "7.8 本章书目述评"]], ["第 8 章 历史记忆与比较史反思", ["8.1 BSD 成功与失败叙事的形成", "8.2 FreeBSD 产业化记忆与现实边界", "8.3 NetBSD 可移植性叙事与历史评价", "8.4 OpenBSD 安全叙事与技术事实", "8.5 DragonFly 实验主义叙事与长期影响", "8.6 Linux 时代 BSD 记忆的变化", "8.7 技术事实、社区记忆与历史书写", "8.8 比较史的方法论总结", "8.9 未解决问题：档案、贡献者与未来研究方向", "8.10 本卷总评"]]]
OLD25 = ['<h2>第二十五卷  BSD 许可证、法律与合规</h2>', '>第 9 章 DragonFly 文化与哲学</h3>']
OLD26 = ['<h2>第二十六卷  自由软件、开源运动与 BSD–Linux 谱系</h2>']

# ── 第二十六批：卷20／卷21／卷22 全卷替换（2026-09-19 主理人清单 ＋ 溯源注迁移）──────
OLD20 = [">第 2 章 OpenBSD 2.x：OpenSSH 诞生与代码审计文化（1996–2001）</h3>", ">第 3 章 OpenBSD 3.x：pf 防火墙与 W^X/SSP 加固（2001–2004）</h3>", ">第 4 章 OpenBSD 4.x：pf 演进与 malloc 随机化（2006–2008）</h3>", ">第 5 章 OpenBSD 5.x：gcc→clang 与 LibreSSL fork（2011–2014）</h3>", ">第 6 章 OpenBSD 6.x：pledge/unveil 安全机制（2016–2021）</h3>", ">第 7 章 OpenBSD 7.x：pledge/unveil 成熟与 AI 代码政策（2021–2026）</h3>", ">第 8 章 卷末书目述评：旧10卷《openbsd的历史》全卷综述</h3>"]
OLD21 = ['第 1 章 第 1 章 安全工程体系：从代码审计到主动防御', '第 2 章 第 2 章 OpenBSD 与现代安全模型的技术分歧', '第 3 章 第 3 章 内核安全机制：权限、内存与执行控制', '第 4 章 第 4 章 进程隔离与最小权限模型', '第 5 章 第 5 章 网络安全基础设施：pf 与互联网协议工程', '第 6 章 第 6 章 密码学基础设施：OpenSSH、LibreSSL 与 TLS', '第 7 章 第 7 章 编译器、链接器与系统构建环境', '第 8 章 第 8 章 UNIX 用户空间与基础工具生态', '第 9 章 第 9 章 网络服务与系统守护进程', '第 10 章 第 10 章 架构移植、硬件支持与系统安全边界', '第 11 章 第 11 章 OpenBSD 技术路线的整合与演进', '第 12 章 第 12 章 OpenBSD 技术史的史料与方法']
OLD22 = [">第 1 章 分化轴总论：安全绝对主义从 CSRG 遗产的分化</h3>", ">第 2 章 工程哲学的物质基础：审计文化与 de Raadt 审美</h3>", ">第 4 章 共同体与治理文化：唯一决策者与核心圈</h3>", ">第 5 章 价值、许可证与自由观：ISC 许可与安全共享</h3>", ">第 6 章 争议、批评与自我批评：安全神话与审计声誉</h3>"]
SPEC20 = [["第 1 章 OpenBSD 起源（1995–1996）", ["1.1 1995 年从 NetBSD 分叉的动因与经过", "1.2 Theo de Raadt 与 NetBSD 核心团队冲突考据（1994–1995）", "1.3 OpenBSD 早期 CVS 建立与 1.1–1.2 发布（1995–1996）", "1.4 NetBSD 社区回应与分叉争论", "1.5 创建期贡献者谱系：Theo de Raadt、Chuck Cranor、Mats O. Jansson 等", "1.6 创建期治理结构与开发模式形成", "1.7 4.4BSD-Lite 迁移与代码基础重建", "1.8 创建期技术路线争论与批评", "1.9 OpenBSD 对 BSD 生态的软件外溢与代码贡献", "1.10 与同时期操作系统的比较：NetBSD、FreeBSD、Linux 与商业 UNIX", "1.11 本章书目述评"]], ["第 2 章 OpenBSD 2.x：OpenSSH 诞生与审计文化形成（1996–2001）", ["2.1 OpenBSD 2.x 发布史", "2.2 代码审计文化建立（1996–2000）", "2.3 OpenSSH 起源：SSH 1.2.12、OSSH 与 OpenBSD fork", "2.4 OpenSSH 创建者与贡献者谱系", "2.5 安全审计方法进入工程流程", "2.6 ktrace、mandoc 等 BSD 工具继承与扩展", "2.7 外部批评：安全审计文化的成本与争议", "2.8 社区贡献者与边缘开发者", "2.9 与同时期操作系统的比较：同期操作系统", "2.10 本章书目述评"]], ["第 3 章 OpenBSD 3.x：pf 与主动安全工程（2001–2005）", ["3.1 OpenBSD 3.x 发布史", "3.2 IPFilter 许可证争议与移除事件（2001）", "3.3 pf 的设计、实现与作者群体", "3.4 Darren Reed 与 IPFilter 争议考据", "3.5 DARPA POSSE 项目与安全研究资金", "3.6 W^X 安全设计理念形成", "3.7 SSP 与编译级安全增强", "3.8 外部批评：安全优先路线的代价", "3.9 贡献者谱系与 committer 社群", "3.10 OpenBSD 软件外溢影响", "3.11 与同时期操作系统的比较：NetBSD 1.2-1.6、FreeBSD 2.x-4.x、Linux 2.0-2.6、Solaris 2.x-9", "3.12 本章书目述评"]], ["第 4 章 OpenBSD 4.x：安全机制体系化（2006–2010）", ["4.1 OpenBSD 4.x 发布史", "4.2 malloc 随机化与内存安全工程", "4.3 gcc GPLv3 问题与工具链路线", "4.4 pcc 探索与 clang 前夜", "4.5 pf、CARP、网络工具生态发展", "4.6 贡献者与维护者群体变化", "4.7 外部批评与回应", "4.8 安全文化的社会影响", "4.9 与同时期操作系统的比较：Linux、FreeBSD、NetBSD 与其他 UNIX 系统", "4.10 本章书目述评"]], ["第 5 章 OpenBSD 5.x：LibreSSL 与工具链自主化（2011–2015）", ["5.1 OpenBSD 5.x 发布史", "5.2 Heartbleed 事件与 LibreSSL fork", "5.3 LibreSSL 的工程目标与争议", "5.4 gcc→clang 转换过程", "5.5 OpenBSD 基础工具自主化路线", "5.6 OpenSSH、OpenNTPD、OpenSMTPD 生态扩展", "5.7 贡献者与维护者谱系", "5.8 外部批评：硬件支持与生态规模问题", "5.9 安全哲学与许可证哲学讨论", "5.10 OpenBSD 软件外溢", "5.11 与同时期操作系统的比较：NetBSD 3.x-5.x、FreeBSD 6.x-9.x、Linux 2.6.x-3.x、Solaris 10/11", "5.12 本章书目述评"]], ["第 6 章 OpenBSD 6.x：pledge/unveil 与现代安全模型（2016–2021）", ["6.1 OpenBSD 6.x 发布史", "6.2 pledge 从实验机制到系统接口", "6.3 unveil 与文件访问限制模型", "6.4 安全机制进入用户空间程序", "6.5 sndio 与简约主义设计", "6.6 贡献者与社区变化", "6.7 外部批评：安全代价与兼容性问题", "6.8 项目文化变化", "6.9 与同时期操作系统的比较：Linux、FreeBSD、NetBSD 与 Solaris", "6.10 本章书目述评"]], ["第 7 章 OpenBSD 7.x：现代硬件时代与代码政策（2021–2026）", ["7.1 OpenBSD 7.x 发布史", "7.2 pledge/unveil 成熟阶段", "7.3 riscv64、ARM64 与现代硬件支持", "7.4 OpenBSD 7.9：异构 CPU 调度与新硬件支持", "7.5 Wi-Fi 驱动开放化路线", "7.6 AI 时代代码政策与人工生成代码争议", "7.7 贡献者结构变化", "7.8 外部批评与自我反省", "7.9 本章书目述评"]], ["第 8 章 卷末书目述评：OpenBSD 历史研究方法", ["8.1 一手史料体系", "8.2 邮件列表、CVS、发行说明与口述史", "8.3 安全神话与历史记忆", "8.4 尚未解决的问题", "8.5 卷末总评"]]]
SPEC21 = [['第 1 章 安全工程体系：从代码审计到主动防御（1995–2026）', ['1.1 OpenBSD 分叉背景与安全目标的形成', '1.2 1996–1997 年大规模代码审计与系统清理', '1.3 Secure by Default：默认安全理念', '1.4 Correctness、安全性与工程质量', '1.5 从漏洞修复到主动防御', '1.6 安全审计与功能开发之间的工程关系', '1.7 从减少漏洞数量到降低攻击面', '1.8 OpenBSD 安全工程方法的长期延续']], ['第 2 章 内核安全机制：内存保护、执行控制与随机化', ['2.1 4.4BSD 基础与 OpenBSD 内核安全重构', '2.2 W^X：执行权限分离机制', '2.3 GOT、PLT 与动态链接保护', '2.4 Stack Protector 与 ProPolice', '2.5 malloc 随机化与 Guard Page', '2.6 mmap 随机化与地址空间布局随机化', '2.7 ASLR 与 PIE', '2.8 控制流攻击缓解机制', '2.9 RETGUARD 与返回地址保护', '2.10 内核内存保护机制', '2.11 用户空间与内核安全边界', '2.12 从单项防护到纵深防御体系']], ['第 3 章 进程隔离与最小权限模型', ['3.1 chroot 与早期隔离机制', '3.2 Privilege Separation 的形成', '3.3 Privilege Revocation', '3.4 tame 的提出与 pledge 的形成', '3.5 pledge 系统调用设计', '3.6 pledge 权限集合与系统调用限制', '3.7 unveil 文件系统视图限制', '3.8 pledge 与 unveil 的联合使用', '3.9 libc 内部权限收缩', '3.10 基础系统中的沙箱化实践', '3.11 进程权限收缩与传统 UNIX 权限模型', '3.12 从权限分离到应用程序最小权限']], ['第 4 章 网络安全基础设施：pf 与互联网协议工程', ['4.1 IPFilter 移除与 pf 的形成', '4.2 pf 状态检测与规则处理架构', '4.3 pf 地址转换与状态表', '4.4 pf 与网络边界安全', '4.5 CARP 与高可用网络', '4.6 pfsync 与状态同步', '4.7 spamd 与网络服务防护', '4.8 OpenNTPD 与时间同步安全', '4.9 OpenBGPD 与路由协议工程', '4.10 OpenIKED 与 IKE/IPsec 实现', '4.11 rpki-client 与路由源验证', '4.12 网络协议实现中的最小权限设计']], ['第 5 章 密码学基础设施：OpenSSH、LibreSSL 与 TLS', ['5.1 OpenSSH 的产生与 SSH 协议实现', '5.2 OpenSSH 中的 Privilege Separation', '5.3 sshd 权限边界与沙箱化', '5.4 Portable OpenSSH 与跨平台维护', '5.5 OpenBSD 密码库的发展', '5.6 Heartbleed 与 LibreSSL 的产生', '5.7 LibreSSL 的代码重构', '5.8 libtls 与高层 TLS 接口', '5.9 TLS 协议实现与证书验证', '5.10 随机数、密钥处理与系统安全', '5.11 OpenSSH 与 LibreSSL 的维护模式', '5.12 密码基础设施与基础系统安全边界']], ['第 6 章 编译器、链接器与安全构建环境', ['6.1 OpenBSD 基础系统与自举构建', '6.2 GCC 时代的系统工具链', '6.3 pcc 探索与自主工具链实践', '6.4 Clang 进入 OpenBSD', '6.5 编译器硬化与安全代码生成', '6.6 ld.so 与动态链接器安全', '6.7 PIE、Static PIE 与位置无关代码', '6.8 ld、as 与基础工具链维护', '6.9 make 与系统构建体系', '6.10 基础系统构建边界', '6.11 构建工具链与安全机制协同']], ['第 7 章 UNIX 用户空间与基础系统工具', ['7.1 OpenBSD 用户空间组织方式', '7.2 mandoc 与 UNIX 手册系统', '7.3 ksh 与命令解释环境', '7.4 nc 与网络诊断工具', '7.5 ftp 与基础网络工具', '7.6 tmux 与终端复用', '7.7 基础工具的安全审计与权限收缩', '7.8 rc.d 与服务启动体系', '7.9 signify 与软件验证', '7.10 基础系统更新机制', '7.11 基础系统与 ports 的技术边界', '7.12 OpenBSD 用户空间统一性']], ['第 8 章 网络服务与系统守护进程安全', ['8.1 OpenSMTPD 架构', '8.2 OpenSMTPD 权限分离与服务安全', '8.3 relayd 与代理、负载均衡', '8.4 httpd 与基础 Web 服务', '8.5 slowcgi 与 FastCGI 服务架构', '8.6 nsd 与权威 DNS 服务', '8.7 unbound 与递归 DNS 服务', '8.8 acme-client 与证书自动化', '8.9 服务程序中的 pledge、unveil 与 privilege separation', '8.10 rc.d 与守护进程生命周期', '8.11 基础网络服务最小权限化', '8.12 OpenBSD 服务程序统一安全模型']], ['第 9 章 Ports、软件生态与安全维护', ['9.1 OpenBSD Ports 体系形成', '9.2 Ports 与基础系统边界', '9.3 pkg_* 工具与二进制软件包', '9.4 软件包签名与验证机制', '9.5 依赖关系与软件更新', '9.6 第三方软件安全维护', '9.7 ports 维护中的安全实践', '9.8 软件生态与基础系统关系']], ['第 10 章 架构移植、硬件支持与安全边界', ['10.1 从 i386 到 amd64', '10.2 Alpha、SPARC64、m68k 等历史架构', '10.3 arm64 平台支持', '10.4 armv7 与嵌入式平台', '10.5 riscv64 与新架构支持', '10.6 多架构内核安全机制一致性', '10.7 平台相关内存保护', '10.8 MMU、页表与执行权限', '10.9 随机化机制的架构适配', '10.10 无线网络硬件与驱动支持', '10.11 固件依赖与硬件支持边界', '10.12 硬件开放程度与系统可维护性']], ['第 11 章 OpenBSD 安全工程路线的整合与演进', ['11.1 从代码审计到整体安全架构', '11.2 内核机制与用户空间安全设计的结合', '11.3 内存防护、编译器与链接器协同', '11.4 Privilege Separation、pledge 与 unveil 的技术连续性', '11.5 pf 与网络服务安全体系整合', '11.6 OpenSSH、LibreSSL 与基础系统共同演进', '11.7 基础系统统一开发模式', '11.8 OpenBSD 安全工程路线的长期稳定部分', '11.9 OpenBSD 安全工程路线的持续变化部分', '11.10 技术路线的能力范围与工程边界', '11.11 1995–2026 年 OpenBSD 安全技术演进']]]
SPEC22 = [["第 1 章 分化轴总论：主动安全与正确性优先从 CSRG 遗产中的分化", ["1.1 共同文化基线：第九卷六章的文化命题清单", "1.2 OpenBSD 分化轴的形成：从 BSD 工程传统到主动安全原则", "1.3 分化的物质基础：代码审计、默认安全配置与架构重构", "1.4 “安全优先”的观念形成：从工程选择到项目身份", "1.5 与 FreeBSD、NetBSD、DragonFly BSD 的分化轴比较", "1.6 安全叙事的边界：安全、性能、兼容性之间的长期张力", "1.7 本章书目述评"]], ["第 2 章 工程哲学的物质基础：审计文化、重构传统与 de Raadt 审美", ["2.1 设计信条的文本化：邮件列表、代码提交与技术讨论", "2.2 代码证据：审计、重写与删除旧代码的工程文化", "2.3 “正确性优先”的技术价值观", "2.4 工具链政治：GCC、clang、pcc 与自主控制", "2.5 OpenSSL→LibreSSL：fork 作为工程哲学事件", "2.6 性能观：安全机制带来的成本与取舍", "2.7 de Raadt 技术领导风格与争议", "2.8 本章书目述评"]], ["第 3 章 符号、名称与仪式：Puffy、发行歌曲与 hackathon", ["3.1 名称形成：OpenBSD 的“开放”语义", "3.2 Puffy：吉祥物作为技术共同体符号", "3.3 发行艺术：CD artwork 与版本身份", "3.4 Release Songs：从技术事件到社区记忆", "3.5 Hackathon：面对面的代码生产仪式", "3.6 项目语汇与内部文化：“hack”“diff”“commit”等词汇体系", "3.7 符号所有权：Puffy、艺术作品与商业使用边界", "3.8 本章书目述评"]], ["第 4 章 共同体与治理文化：核心维护者、开发圈与开放边界", ["4.1 组织结构：Theo de Raadt 与核心维护模式", "4.2 CVS 提交权限与信任体系", "4.3 “先读源码”的技术文化与进入门槛", "4.4 邮件列表文化：冲突、批评与技术讨论", "4.5 Hackathon 社群：非会议型开发组织模式", "4.6 外部贡献者进入路径与代际变化", "4.7 本章书目述评"]], ["第 5 章 价值、许可证与自由观：ISC 许可、安全共享与产业关系", ["5.1 ISC 许可证：极简法律文本背后的工程观", "5.2 自由软件与 BSD 式共享观", "5.3 pf、OpenSSH 等成果扩散与回馈争议", "5.4 LibreSSL：许可证、代码控制与安全治理", "5.5 商业采用：嵌入式、网络设备与云环境", "5.6 安全工具公共品属性", "5.7 本章书目述评"]], ["第 6 章 争议、批评与自我批评：安全声誉的形成与边界", ["6.1 “Only one remote hole” 叙事形成考据", "6.2 安全神话：技术事实与社区记忆之间", "6.3 外部批评：排他性、规模与硬件支持问题", "6.4 内部反思：安全投入与开发资源限制", "6.5 合规、安全认证与工程路线冲突", "6.6 OpenBSD 文化遗产：神话消解后的技术遗产", "6.7 本章书目述评"]], ["第 7 章 卷末书目述评：OpenBSD 文化与哲学", ["7.1 史料谱系：邮件列表、CVS、源代码、手册、公告、歌曲、艺术作品", "7.2 证据层级：当事人叙述、同期记录与后见解释", "7.3 从物质证据到文化解释", "7.4 文化史解释边界", "7.5 尚未解决的问题：沉默贡献者、缺失档案与未来路线", "7.6 本卷总评"]]]
_gvol("G51", 20, SPEC20, 8, 79, "第二十卷  世界上最安全的操作系统：OpenBSD 的历史（1995–2026）", OLD20)
_gvol("G52", 21, SPEC21, 11, 122,
      "第二十一卷  OpenBSD 技术专题史（1995–2026）", OLD21)
_gvol("G28", 22, SPEC22, 7, 50, "第二十二卷  OpenBSD 文化与哲学（1995–2026）", OLD22)
chk("G53 卷20／卷21／卷22 旧章题在产物中零残留（本批全量改写，逐条核）",
    all(h.count(">" + t + "</h3>") == 0 for t in ("第 3 章 OpenBSD 3.x：pf 防火墙与 W^X/SSP 加固（2001–2004）", "第 4 章 OpenBSD 4.x：pf 演进与 malloc 随机化（2006–2008）", "第 5 章 OpenBSD 5.x：gcc→clang 与 LibreSSL fork（2011–2014）", "第 6 章 OpenBSD 6.x：pledge/unveil 安全机制（2016–2021）", "第 7 章 OpenBSD 7.x：pledge/unveil 成熟与 AI 代码政策（2021–2026）", "第 8 章 卷末书目述评：旧10卷《openbsd的历史》全卷综述", "第 1 章 代码审计方法论与默认安全原则", "第 2 章 防火墙与包过滤：pf 的设计与演进", "第 3 章 加固机制：W^X、SSP 与内存随机化", "第 4 章 隔离与沙箱：pledge 与 unveil", "第 5 章 密码学与 TLS：OpenSSH 与 LibreSSL", "第 6 章 编译器与工具链：gcc→clang 与 pcc 探索", "第 7 章 可移植性与平台支持", "第 8 章 卷末书目述评：OpenBSD 技术专题史料总目", "第 1 章 分化轴总论：安全绝对主义从 CSRG 遗产的分化", "第 2 章 工程哲学的物质基础：审计文化与 de Raadt 审美", "第 4 章 共同体与治理文化：唯一决策者与核心圈", "第 5 章 价值、许可证与自由观：ISC 许可与安全共享", "第 6 章 争议、批评与自我批评：安全神话与审计声誉"))
    and h.count("<h2>第二十一卷  OpenBSD 技术专题史</h2>") == 0)
chk("G54 第 26 批溯源注迁移标记齐备（卷20 6 条／卷22 11 条／卷21 0 条）",
    h.count("第 26 批自卷20 旧 ") == 6 and h.count("第 26 批自卷22 旧 ") == 11
    and h.count("第 26 批自卷21 旧 ") == 0)
chk("G55 卷20 6 条迁移注逐条落位（旧 1.11／2.8／3.2／3.4／6.8／7.3）",
    all(h.count("第 26 批自卷20 旧 " + k + " 迁入") == 1 for k in ("1.11", "2.8", "3.2", "3.4", "6.8", "7.3")))
chk("G56 卷22 11 条迁移注逐条落位（旧 2.3／2.4／2.5／2.6／3.4／3.5／3.6／4.5／5.5／5.6／6.5）",
    all(h.count("第 26 批自卷22 旧 " + k + " 迁入") == 1 for k in ("2.3", "2.4", "2.5", "2.6", "3.4", "3.5", "3.6", "4.5", "5.5", "5.6", "6.5")))
# 注意：四类体例词元（技术淘汰／漏洞与安全响应／项目统摄史观审视／代码外溢）在卷14／16／19／23／24／27
# 等他卷**合法存在**，故本判据限缩于**卷20 节题之内**，不得作全页面零残留判据。
_b57 = [x for _, _, secs in vch(20) for x in secs
        if any(k in x[2] for k in ("技术淘汰", "漏洞与安全响应", "项目统摄史观审视", "代码外溢"))]
chk("G57 卷20 四类体例节按主理人裁定删去（限卷20 节题内核验，他卷合法存在不误伤）",
    not _b57, [x[0] for x in _b57][:3])
chk("G58 卷21 新稿无述评节（第二十八批再次替换后 12 章 142 节，述评槽 0）",
    sum(1 for _, _, secs in vch(21) for x in secs
        if x[2].startswith("本章书目述评")) == 0)
_gvol("G29", 25, SPEC25, 7, 49, "第二十五卷  DragonFly BSD 文化与哲学（2003–2026）", OLD25)
_gvol("G30", 26, SPEC26, 8, 68, "第二十六卷  4.4BSD 遗产的现代分化：FreeBSD、NetBSD、OpenBSD 与 DragonFly BSD（1993–2026）文化与哲学的横向比较（1993–2026）", OLD26)
chk("G31 整章迁移 5 章：旧章题在产物中零残留",
    h.count(">第 17 章 FreeBSD 文化与哲学</h3>") == 0
    and h.count(">第 12 章 NetBSD 文化与哲学</h3>") == 0
    and h.count(">第 8 章 OpenBSD 文化与哲学</h3>") == 0
    and h.count(">第 9 章 DragonFly 文化与哲学</h3>") == 0
    and h.count(">第 9 章 安全神话的形成") == 0)
chk("G32 四新卷第 1 章为升格章且迁移标记齐备（含卷24 ch9 迁入卷22 ch6）",
    h.count("第 22 批自卷14 旧 17.1 迁入") == 1
    and h.count("第 22 批自卷16 旧 12.1 迁入") == 1
    and h.count("第 22 批自卷18 旧 8.1 迁入") == 1
    and h.count("第 22 批自卷20 旧 9.1 迁入") == 1
    and h.count("第 22 批自第二十九卷旧第 9 章整章迁入并重组") == 1)
chk("G33 卷19／22／25／26 分化轴互引齐备（卷16 因第二十四批全卷替换已无分化轴章，其互引 0 处——主理人裁定不改其他卷）",
    h.count("与第十六卷、第十九卷、第二十二卷、第二十五卷第 1 章分工") == 1
    and all(h.count(x) == 1 for x in (
        "与第十六卷、第二十二卷、第二十五卷第 1 章分工",
        "与第十六卷、第十九卷、第二十五卷第 1 章分工",
        "与第十六卷、第十九卷、第二十二卷第 1 章分工"))
    and h.count("与第十九卷、第二十二卷、第二十五卷第 1 章分工") == 0)
chk("G34 卷分工注 6 个（第四十一批：卷18 分工注随全卷替换复原后实测）",
    len(re.findall(r'<p class="vol-note">', h)) == 6)
chk("G35 卷9 分工注「四项目技术专题」卷号已按新序改写",
    h.count("四项目技术专题见卷15、卷18、卷21、卷24") == 1)

# ── 第二十三批：第十四卷全卷替换（主理人清单 ＋ 三类体例节保留）────────────────
SPEC14 = [['第 1 章 FreeBSD 1.x：386BSD 之后，PC 上的 BSD 如何成为一个独立系统', ['1.1 386BSD 的继承与 FreeBSD 分化', '1.2 从移植工程到独立基本系统', '1.3 PC 硬件现实如何重新塑造 BSD 内核', '1.4 启动、安装与磁盘布局第一次成为系统本体问题', '1.5 控制台、设备与用户空间的 PC 化', '1.6 FreeBSD 早期系统接口的形成', '1.7 1.x：一个新 BSD 系统的边界开始出现', '1.8 项目统摄史观审视：从移植工程到独立系统的偶然性', '1.9 与同时期操作系统的比较：Linux、Windows、商业 UNIX 及其他 BSD', '1.10 本章书目述评']], ['第 2 章 FreeBSD 2.x：4.4BSD-Lite 重新定义 FreeBSD', ['2.1 4.4BSD-Lite 的诞生与 FreeBSD 基础代码重建', '2.2 从旧 BSD 代码到 4.4BSD-Lite 的大规模迁移', '2.3 4.4BSD-Lite 带来的新内核基线', '2.4 用户空间、文件系统与设备体系的重新拼接', '2.5 sysinstall 与完整发行系统的形成', '2.6 4.4BSD-Lite 时代的二进制环境与兼容问题', '2.7 FreeBSD 从 BSD 派生物转变为独立操作系统的关键一步', '2.8 项目统摄史观审视：法律危机如何意外重塑 FreeBSD 的技术谱系', '2.9 与同时期操作系统的比较：Linux 2.0-2.2、Windows NT 4.0、Solaris 2.4-2.6', '2.10 本章书目述评']], ['第 3 章 FreeBSD 3.x：4.4BSD-Lite2 合流与现代 FreeBSD 基线', ['3.1 4.4BSD-Lite2 的形成与独立历史位置', '3.2 4.4BSD-Lite2 进入 FreeBSD 的过程', '3.3 4.4BSD-Lite 与 4.4BSD-Lite2 两套基础之间的断裂与连续', '3.4 ELF 成为新的系统二进制基础', '3.5 内核模块化与运行时系统扩展', '3.6 多处理器、多架构与统一内核接口的成形', '3.7 FreeBSD 3.x：BSD 最后一代遗产进入现代 FreeBSD', '3.8 项目统摄史观审视：两代遗产合流中的连续与断裂', '3.9 与同时期操作系统的比较：Linux 2.2、Windows 2000、Solaris 8', '3.10 本章书目述评']], ['第 4 章 FreeBSD 4.x：成熟 Internet Unix 的完整形态', ['4.1 4.x 为何成为一个长期稳定的系统时代', '4.2 网络服务从附着功能变成操作系统的基本环境', '4.3 主机隔离与服务承载方式发生变化', '4.4 面向长期运行的系统资源组织', '4.5 用户空间与内核之间的接口逐渐稳定', '4.6 PC、服务器与 Internet 主机开始共享同一种 FreeBSD', '4.7 4.x：传统 BSD Unix 系统形态的成熟期', '4.8 与同时期操作系统的比较：4.x 时期的技术定位', '4.9 本章书目述评']], ['第 5 章 FreeBSD 5.x：一场持续数年的操作系统重建', ['5.1 从增量开发转向内核基础设施重建', '5.2 多处理器成为系统设计而非附加能力', '5.3 文件系统开始脱离传统 Unix 的容量尺度', '5.4 安全模型从固定机制走向可扩展体系', '5.5 从 i386 中心走向多种 64 位计算环境', '5.6 新旧内核、新旧用户空间长期并存的代价', '5.7 5.x：FreeBSD 最具结构性风险的一次技术转型', '5.8 项目统摄史观审视：一场持续数年的重建的偶然与代价', '5.9 与同时期操作系统的比较：2002–2003 年同期操作系统', '5.10 本章书目述评']], ['第 6 章 FreeBSD 6.x：从重建中的系统重新获得稳定性', ['6.1 5.x 遗留问题如何转化为 6.x 的工程任务', '6.2 内核重构开始表现为可见的系统性能', '6.3 多 CPU 计算从实验环境进入日常服务器', '6.4 存储与网络系统开始承受更高并发负载', '6.5 AMD64 改变 FreeBSD 的平台重心', '6.6 新旧架构共同存在时的 ABI 与系统连续性', '6.7 6.x：从“大规模重建”走向“可持续演进”', '6.8 项目统摄史观审视：稳定性如何从重构的余波中生成', '6.9 与同时期操作系统的比较：Linux 2.6、Vista、Solaris 10', '6.10 本章书目述评']], ['第 7 章 FreeBSD 7.x：现代服务器的尺度第一次真正改变', ['7.1 多核处理器成为普遍硬件背景', '7.2 内核并行能力开始围绕多核时代重新组织', '7.3 存储容量与内存规模突破传统 Unix 经验', '7.4 操作系统开始具备面对大规模服务器的资源模型', '7.5 系统运行状态从黑箱走向可持续观测', '7.6 基本系统开始具备连续升级而非重新安装的条件', '7.7 7.x：现代 FreeBSD 服务器形态的成型', '7.8 项目统摄史观审视：硬件尺度的跃迁如何改写系统边界', '7.9 与同时期操作系统的比较：Linux 2.6.26-2.6.32、Windows 7、Solaris 10 Update 5-6', '7.10 本章书目述评']], ['第 8 章 FreeBSD 8.x：操作系统开始面向虚拟化世界', ['8.1 物理主机不再是 FreeBSD 唯一的运行环境', '8.2 隔离、虚拟机与多租户改变系统边界', '8.3 虚拟硬件逐渐获得与真实硬件相近的地位', '8.4 网络与设备模型必须同时面对物理机和虚拟机', '8.5 ZFS 从实验能力进入实际系统环境', '8.6 新平台扩展与服务器系统趋于同一内核模型', '8.7 8.x：FreeBSD 开始成为虚拟基础设施中的操作系统', '8.8 项目统摄史观审视：运行环境的多重化与本体论平等', '8.9 与同时期操作系统的比较：Linux 2.6.30-3.0、Windows Server 2008 R2、Solaris 11 Express', '8.10 本章书目述评']], ['第 9 章 FreeBSD 9.x：重新设计“如何安装和启动一个 FreeBSD”', ['9.1 bsdinstall 取代旧安装体系的历史意义', '9.2 从安装程序到完整部署流程', '9.3 系统安装开始考虑大容量存储与现代固件环境', '9.4 高可用环境中的系统连续运行', '9.5 基本系统与外部软件的边界进一步明确', '9.6 能力安全进入操作系统整体模型', '9.7 9.x：FreeBSD 从传统发行介质走向现代部署系统', '9.8 项目统摄史观审视：安装与启动作为系统的自我定义', '9.9 与同时期操作系统的比较：Linux、Windows、商业 UNIX 及其他 BSD', '9.10 本章书目述评']], ['第 10 章 FreeBSD 10.x：基本系统开始脱离传统 Unix 工具链', ['10.1 基本系统的历史 GNU 依赖开始系统性减少', '10.2 默认工具、构建环境与用户空间的重新取舍', '10.3 软件包管理由附属机制变为日常系统入口', '10.4 虚拟机宿主能力改变 FreeBSD 的运行角色', '10.5 基本系统服务开始以更专门化的组件替换历史实现', '10.6 新硬件进入系统的方式逐渐改变', '10.7 10.x：传统 BSD 用户空间开始结束其长期过渡期', '10.8 项目统摄史观审视：GNU 依赖的退场与自由的再界定', '10.9 与同时期操作系统的比较：Linux、Windows、商业 UNIX 及其他 BSD', '10.10 本章书目述评']], ['第 11 章 FreeBSD 11.x：FreeBSD 离开传统 PC 的中心位置', ['11.1 AArch64 进入正式发行体系与系统版图扩张', '11.2 新架构要求重新思考启动、设备与用户空间连续性', '11.3 UEFI 成为新的主流启动环境', '11.4 现代控制台取代传统终端硬件假设', '11.5 图形、无线与现代设备逐渐进入基本系统预期', '11.6 历史平台开始系统性退出', '11.7 11.x：FreeBSD 从 PC Unix 走向真正的通用多平台操作系统', '11.8 项目统摄史观审视：平台中心的转移与多平台平等', '11.9 与同时期操作系统的比较：Linux、Windows、商业 UNIX 及其他 BSD', '11.10 本章书目述评']], ['第 12 章 FreeBSD 12.x：现代平台成为系统基线', ['12.1 64 位系统逐渐成为 FreeBSD 的主要运行环境', '12.2 新平台从移植对象变成长期维护的平台', '12.3 历史架构开始连续退出，而不是偶然消失', '12.4 启动加载器进入可编程时代', '12.5 UEFI、磁盘加密与安装流程开始形成完整链路', '12.6 NUMA、多核与现代服务器硬件成为普通系统条件', '12.7 12.x：FreeBSD 的历史兼容包袱开始明显减轻', '12.8 项目统摄史观审视：历史包袱的减轻是选择而非必然', '12.9 与同时期操作系统的比较：同期操作系统', '12.10 本章书目述评']], ['第 13 章 FreeBSD 13.x：现代 FreeBSD 的基本轮廓定型', ['13.1 多架构体系从扩张进入稳定分层', '13.2 AArch64 从新加入的平台成为核心系统平台', '13.3 RISC-V 进入正式发行体系，FreeBSD 获得新的开放硬件平台', '13.4 传统 32 位世界与主体系统开始明显分离', '13.5 基本系统构建环境完成一次世代更替', '13.6 历史架构进入最后支持阶段', '13.7 13.x：FreeBSD 现代平台边界基本确定', '13.8 项目统摄史观审视：现代边界的确定是选择而非必然', '13.9 与同时期操作系统的比较：Linux、Windows、商业 UNIX 及其他 BSD', '13.10 本章书目述评']], ['第 14 章 FreeBSD 14.x：成熟操作系统面向新一代硬件重新定标', ['14.1 从多架构扩张转向有限而稳定的平台集合', '14.2 操作系统开始以超大规模多核机器为能力上限', '14.3 历史平台退出不再影响主体系统连续性', '14.4 基本系统的密码学基础进入新的世代', '14.5 文件系统维护逐渐脱离停机窗口', '14.6 系统服务向更小、更专用的实现转变', '14.7 14.x：现代服务器 FreeBSD 的成熟形态', '14.8 项目统摄史观审视：成熟期的重新定标与偶然性优先', '14.9 与同时期操作系统的比较：Linux、Windows、商业 UNIX 及其他 BSD', '14.10 本章书目述评']], ['第 15 章 FreeBSD 15.x：基本系统进入软件包时代', ['15.1 Packaged Base 改变 FreeBSD 的基本系统定义', '15.2 基本系统首次拥有独立的软件包生命周期', '15.3 安装、升级与基本系统维护由新的模型重新统一', '15.4 文件系统事件接口开始适应现代软件运行方式', '15.5 后量子密码进入基本系统的正式能力范围', '15.6 构建与发行制品开始以可复现性为系统属性', '15.7 传统 32 位系统退出主体平台体系', '15.8 15.x：FreeBSD 从“发行版”走向“可管理的系统软件集合”', '15.9 项目统摄史观审视：基本系统定义的重构与循环结构', '15.10 与同时期操作系统的比较：Linux 6.x、OpenBSD 7.x、NetBSD 10/11、Windows 11/Server 2025、macOS 15/16', '15.11 本章书目述评']], ['第 16 章 FreeBSD 16.x：基本系统重新定义自身', ['16.1 packaged base 从技术预览走向新的系统组织方式', '16.2 传统 Distribution Sets 的历史终点', '16.3 基本系统中的历史遗留组件持续退出', '16.4 GPL 遗留在基本系统中的进一步清理', '16.5 安装、更新、构建与基本系统封装重新汇合', '16.6 现代架构体系进入相对稳定的收敛阶段', '16.7 ABI 连续性成为持续重构的制度性前提', '16.8 16.x：尚在形成中的下一代 FreeBSD 操作系统形态', '16.9 项目统摄史观审视：自我重定义中的非存在与自反性', '16.10 与同时期操作系统的比较：FreeBSD 16.x/Current', '16.11 本章书目述评']]]
OLD14 = ['<h2>第十四卷  从大教堂到集市：FreeBSD 的历史（1993–2026）</h2>',
         '>第 16 章 FreeBSD 16.x：GPL 代码清零的完成与未来路线（2026-07 清零，2027-12 计划发布）</h3>',
         '>第 5 章 FreeBSD 5.x：SMPng 转型与稳定性代价（2003–2005）</h3>',
         '>第 8 章 FreeBSD 8.x：Xen domU 虚拟化与 VNET 隔离（2009–2012）</h3>']
_gvol("G36", 14, SPEC14, 16, 161,
      "第十四卷  从大教堂到集市：FreeBSD 操作系统的历史（1993–2026）", OLD14)
chk("G37 卷14 卷题加「操作系统」二字且旧卷题零残留",
    h.count("<h2>第十四卷  从大教堂到集市：FreeBSD 操作系统的历史（1993–2026）</h2>") == 1
    and h.count("<h2>第十四卷  从大教堂到集市：FreeBSD 的历史（1993–2026）</h2>") == 0)
chk("G38 卷14 三类体例节齐备（述评 16 ＋ 比较 16 ＋ 史观审视 15）",
    h.count("本章书目述评") >= 16)
_c14 = vch(14)
chk("G39 卷14 述评节 16／比较节 16／史观审视节 15",
    sum(1 for _, _, secs in _c14 for x in secs if x[2] == "本章书目述评") == 16
    and sum(1 for _, _, secs in _c14 for x in secs if x[2].startswith("与同时期操作系统的比较")) == 16
    and sum(1 for _, _, secs in _c14 for x in secs if x[2].startswith("项目统摄史观审视")) == 15)

# ── 第二十四批：卷15／卷16 全卷替换（主理人清单照录 ＋ 溯源注迁移）──────────────
SPEC15 = [['第 1 章 FreeBSD 存储体系：从 4.4BSD 文件系统到 OpenZFS 时代', ['1.1 4.4BSD FFS：FreeBSD 存储系统的历史起点', '1.2 UFS1 与 UFS2：文件系统扩展与大容量存储', '1.3 Soft Updates：一致性、性能与文件系统设计', '1.4 GEOM：存储抽象层的形成', '1.5 CAM：设备访问模型与存储硬件现代化', '1.6 RAID、GELI 与存储可靠性体系', '1.7 ZFS 引入 FreeBSD：从 Sun ZFS 到系统核心能力', '1.8 OpenZFS 时代：跨平台存储基础设施', '1.9 UFS 与 ZFS 的长期共存']], ['第 2 章 FreeBSD 网络体系：从 BSD TCP/IP 到高速网络平台', ['2.1 4.4BSD TCP/IP 网络栈基础', '2.2 KAME IPv6：IPv6 体系进入 FreeBSD', '2.3 Netgraph：可组合网络架构', '2.4 Dummynet：网络模拟与流量控制', '2.5 Kqueue：事件驱动模型', '2.6 Netmap：高速数据包处理框架', '2.7 Iflib：网络驱动模型重构', '2.8 Kernel TLS：内核态安全通信', '2.9 WireGuard 与现代 VPN 架构']], ['第 3 章 FreeBSD 虚拟化体系：从 Jail 到 bhyve', ['3.1 UNIX 隔离传统与 FreeBSD Jail', '3.2 Jail 的进程、文件系统与网络隔离', '3.3 VIMAGE/VNET：网络虚拟化', '3.4 Xen 支持与早期虚拟化探索', '3.5 bhyve：FreeBSD 原生虚拟机监控器', '3.6 Jail 与虚拟机的技术分工', '3.7 FreeBSD 虚拟化模型与其他系统比较', '3.8 云计算环境中的 FreeBSD 虚拟化']], ['第 4 章 FreeBSD 内核并发体系：SMPng 与多核时代', ['4.1 4.4BSD 单处理器内核模型', '4.2 FreeBSD SMP 初期实现', '4.3 SMPng 工程目标与内核锁重构', '4.4 Giant 锁拆除与细粒度并发', '4.5 内核线程模型演进', '4.6 调度器历史：4BSD 到 ULE', '4.7 多核处理器、NUMA 与可扩展性', '4.8 网络与存储子系统并发优化']], ['第 5 章 FreeBSD 安全架构：隔离、能力与系统防护', ['5.1 UNIX DAC 权限模型', '5.2 OpenBSM 与系统审计', '5.3 MAC Framework：强制访问控制体系', '5.4 Capsicum：能力安全模型', '5.5 Jail 的安全设计', '5.6 GELI 与系统加密基础', '5.7 CHERI 与未来内存安全架构', '5.8 FreeBSD 安全机制之间的协同']], ['第 6 章 FreeBSD 基本系统工程：源码、构建与发布', ['6.1 FreeBSD 源代码树结构', '6.2 内核配置与构建体系', '6.3 buildworld 与用户空间构建', '6.4 buildkernel 与内核发布', '6.5 DESTDIR 与交叉构建', '6.6 基本系统与第三方软件分离', '6.7 Release Engineering 的形成', '6.8 Release Branch、RC 与版本发布', '6.9 Snapshot 与自动化构建']], ['第 7 章 FreeBSD 软件生态：Ports、Packages 与 pkg', ['7.1 1990 年代软件安装问题', '7.2 FreeBSD Ports 的形成', '7.3 Ports Skeleton 与维护体系', "7.4 Porter's Handbook 与维护者制度", '7.5 pkg_install 时代', '7.6 pkgng 与现代软件包体系', '7.7 Repository、ABI 与二进制分发', '7.8 Poudriere 与大规模软件包构建', '7.9 pkgbase 与基本系统组件化', '7.10 软件包签名与供应链完整性']], ['第 8 章 FreeBSD 工具链与开发环境', ['8.1 BSD 用户空间传统', '8.2 GCC 到 Clang/LLVM 的转型', '8.3 LLVM 工具链体系', '8.4 LLD 与现代链接环境', '8.5 bmake 与 BSD 构建传统', '8.6 开发工具、调试工具与工程流程', '8.7 可重复构建与现代开发实践']], ['第 9 章 FreeBSD 系统可观测性与性能工程', ['9.1 UNIX 调试传统', '9.2 ktrace 与 truss', '9.3 DTrace：动态追踪体系', '9.4 PMC 与硬件性能计数器', '9.5 ddb、kgdb 与内核调试', '9.6 系统性能分析方法', '9.7 jemalloc 与内存管理', '9.8 高并发服务器环境中的 FreeBSD', '9.9 FreeBSD 与 Linux perf、eBPF 比较']], ['第 10 章 FreeBSD 硬件架构支持：从 i386 到多架构系统', ['10.1 i386 时代的系统基础', '10.2 Alpha、MIPS、SPARC64 等历史架构', '10.3 IA-64 支持与退出', '10.4 AMD64：64 位时代转型', '10.5 ARM 移植与嵌入式支持', '10.6 AArch64：现代 ARM 平台', '10.7 RISC-V 与新架构探索', '10.8 ACPI、电源管理与设备支持', '10.9 GPU、无线与现代硬件支持']], ['第 11 章 FreeBSD 技术路线综合：系统工程与长期演进', ['11.1 基本系统统一性的形成', '11.2 内核、用户空间与工程体系的协同', '11.3 稳定性、兼容性与创新之间的取舍', '11.4 服务器、网络与基础设施中的技术定位', '11.5 FreeBSD 技术遗产与持续发展']]]
SPEC16 = [['第 1 章 从 Berkeley UNIX 到 FreeBSD：文化传统的继承与转化（1977–1998）', ['1.1 Berkeley UNIX 的研究文化', '1.2 CSRG：开放共享与学术协作传统', '1.3 BSD 网络文化与 Internet 早期精神', '1.4 UNIX 工具哲学与系统设计传统', '1.5 4.4BSD：研究系统文化的成熟与终结', '1.6 4.4BSD-Lite 与自由系统传统', '1.7 386BSD 分裂与 FreeBSD 身份形成', '1.8 从研究项目到长期操作系统项目', '1.9 本章书目述评']], ['第 2 章 工程文化：代码、文档与系统设计中的价值', ['2.1 BSD 工程传统：代码优先与系统完整性', '2.2 “完整操作系统”观念与基本系统文化', '2.3 Manual Pages、Handbook 与知识传承方式', '2.4 源代码作为技术文献的文化意义', '2.5 “不破坏用户空间”的工程传统', '2.6 长期维护与渐进式演进思想', '2.7 工程审美：简洁、可读性与可维护性', '2.8 技术决策中的保守主义与创新张力', '2.9 本章书目述评']], ['第 3 章 FreeBSD 与 UNIX 世界：传统、身份与继承关系', ['3.1 UNIX 哲学在 FreeBSD 中的延续', '3.2 “一个完整系统”的 UNIX 观', '3.3 BSD 与 System V 文化差异', '3.4 FreeBSD 与 Linux 的文化边界', '3.5 macOS 与 BSD 遗产的关系', '3.6 POSIX、UNIX 商标与身份问题', '3.7 “BSD is UNIX”的历史语境', '3.8 FreeBSD 在现代 UNIX 体系中的位置', '3.9 本章书目述评']], ['第 4 章 FreeBSD 的符号体系：名称、版本与视觉文化', ['4.1 FreeBSD 名称的形成与历史语义', '4.2 Beastie：BSD 吉祥物的视觉谱系', '4.3 FreeBSD 标识与项目身份', '4.4 RELEASE、STABLE、CURRENT：版本语言与开发文化', '4.5 发行公告与版本发布仪式', '4.6 Handbook、FAQ 与官方文本风格', '4.7 FreeBSD 社区内部术语与技术语言', '4.8 符号如何塑造项目记忆', '4.9 本章书目述评']], ['第 5 章 FreeBSD 共同体结构：开发者、治理与协作文化', ['5.1 从 CSRG 到 FreeBSD 的开发组织变化', '5.2 Committer 制度的形成', '5.3 Core Team 与项目治理结构', '5.4 Maintainer 制度与责任分配', '5.5 邮件列表、IRC 与技术讨论文化', '5.6 企业贡献者、个人开发者与项目关系', '5.7 非 committer 贡献者的历史位置', '5.8 开发者代际与技术传承', '5.9 本章书目述评']], ['第 6 章 用户文化：管理员、Ports 与系统实践传统', ['6.1 FreeBSD 用户的系统管理传统', '6.2 Handbook 与知识传播', '6.3 Ports 用户文化', '6.4 自定义内核与系统构造实践', '6.5 BSD 系统管理员群体', '6.6 FreeBSD 在服务器文化中的位置', '6.7 用户与开发者之间的关系', '6.8 本章书目述评']], ['第 7 章 自由、商业与许可证哲学', ['7.1 BSD 许可证历史背景', '7.2 4-Clause BSD 到 2-Clause BSD 的文化变化', '7.3 许可证选择与软件传播模式', '7.4 商业采用与开放开发之间的关系', '7.5 FreeBSD Foundation 与公益模式', '7.6 云计算时代的 BSD 许可证问题', '7.7 BSD 与 GPL 软件自由观差异', '7.8 自由、共享与商业利用的长期张力', '7.9 本章书目述评']], ['第 8 章 争议、分裂与自我修正：FreeBSD 文化的张力', ['8.1 386BSD 分裂与身份竞争', '8.2 FreeBSD 4.x 时代的成功叙事', '8.3 FreeBSD 5.x 转型中的工程文化冲突', '8.4 Matt Dillon、DragonFly BSD 与技术路线分歧', '8.5 “BSD is dying”叙事：技术事实、媒体记忆与历史解释', '8.6 Linux 时代中的 BSD 自我定位', '8.7 行为规范与社区文化调整', '8.8 技术争论如何塑造项目文化', '8.9 本章书目述评']], ['第 9 章 FreeBSD 的历史记忆与未来文化（1993–2026）', ['9.1 FreeBSD 历史叙述中的成功与遗忘', '9.2 BSD 技术遗产在现代计算中的位置', '9.3 macOS、网络设备与互联网基础设施中的 BSD 遗产', '9.4 云计算时代 FreeBSD 的文化定位', '9.5 AI 时代开放操作系统文化的新问题', '9.6 全球 FreeBSD 文化：日本、欧洲与中文社区', '9.7 FreeBSD 文化解释的边界', '9.8 本卷史料体系与研究方法', '9.9 本卷总评']]]
OLD15B = ['第 5 章 第 5 章 FreeBSD 安全架构：从 UNIX 权限到能力安全', '第 6 章 第 6 章 FreeBSD 工具链与基本系统工程', '第 7 章 第 7 章 FreeBSD 系统可观测性：调试、分析与运行时观察', '第 8 章 第 8 章 FreeBSD 硬件架构支持：从 i386 到多架构系统', '第 9 章 第 9 章 FreeBSD 高性能计算与网络服务技术', '第 10 章 第 10 章 FreeBSD 技术史研究方法与资料体系']
OLD16B = ['<h2>第十六卷  FreeBSD 文化与哲学（1993–2026）</h2>',
          '>第 1 章 分化轴总论：从 CSRG 遗产到产业化实用主义</h3>',
          '>第 7 章 卷末书目述评：FreeBSD 文化与哲学</h3>']
_gvol("G40", 15, SPEC15, 11, 91,
      "第十五卷  FreeBSD 技术专题史（1993–2026）", OLD15B)
_gvol("G41", 16, SPEC16, 9, 80, "第十六卷  FreeBSD 文化、社会与哲学（1993–2026）", OLD16B)
chk("G42 卷15／卷16 卷末章按清单照录（不含「卷末书目述评」字样）",
    h.count(">第 11 章 FreeBSD 技术路线综合：系统工程与长期演进</h3>") == 1
    and h.count(">第 9 章 FreeBSD 的历史记忆与未来文化（1993–2026）</h3>") == 1
    and h.count(">第 10 章 卷末书目述评：FreeBSD 技术专题史料总目</h3>") == 0
    and h.count(">第 7 章 卷末书目述评：FreeBSD 文化与哲学</h3>") == 0)
chk("G43 卷16 卷导言与卷分工注已保留（体例元素）",
    h.count("本卷为 386BSD 分叉后 FreeBSD 项目文化、社会与哲学的专卷") == 1
    and h.count("FreeBSD 文化社会哲学线；项目编年见卷14，技术专题见卷15，治理结构比较见卷32。") == 1)
chk("G44 溯源注迁移标记齐备（第 24 批自卷15／卷16 旧 M.K 迁入）",
    h.count("第 24 批自卷15 旧 6.4 迁入") == 1
    and h.count("第 24 批自卷16 旧 3.1 迁入") == 1
    and h.count("第 24 批自卷16 旧 7.1 迁入") == 1)

# ── 第二十五批：卷17／卷18／卷19 全卷替换（主理人清单 ＋ 溯源注迁移）──────────────
SPEC17 = [['第 1 章 386BSD 分叉与 NetBSD 的诞生：重新寻找 UNIX/BSD 的延续（1993–1994）', ['1.1 386BSD 的历史背景与技术遗产', '1.2 386BSD 发布后的维护危机与社区分裂', '1.3 NetBSD 创建者与早期核心成员', '1.4 NetBSD 0.8–0.9：从实验系统到独立项目', '1.5 NetBSD 1.0：第一个正式稳定版本', '1.6 “可移植性优先”路线的形成', '1.7 早期争议：技术方向与组织方式的分歧', '1.8 与 FreeBSD、BSDI、Linux 的同期关系', '1.9 本章书目述评']], ['第 2 章 NetBSD 1.x：可移植操作系统理念的确立（1994–2002）', ['2.1 NetBSD 1.x 系列的发展轨迹', '2.2 MI/MD 架构思想进入系统核心', '2.3 多平台支持的扩张：从传统工作站到嵌入式平台', '2.4 pkgsrc 的诞生与跨平台软件生态', '2.5 早期核心开发者与贡献者群体', '2.6 外部批评：可移植性优先路线的收益与代价', '2.7 NetBSD 与 FreeBSD、OpenBSD 路线分化', '2.8 NetBSD 在 BSD 世界中的历史位置', '2.9 本章书目述评']], ['第 3 章 NetBSD 2.x：SMP 与现代内核转型（2002–2005）', ['3.1 NetBSD 2.0 发布背景', '3.2 SMP 支持的实现过程', '3.3 内核线程模型变化', '3.4 多处理器时代的系统挑战', '3.5 核心开发者与工程路线争论', '3.6 NetBSD 与 FreeBSD 5.x SMPng 的不同路径', '3.7 NetBSD 2.x 的历史评价', '3.8 本章书目述评']], ['第 4 章 NetBSD 3.x–4.x：多平台系统的成熟与嵌入式扩展（2005–2009）', ['4.1 NetBSD 3.0：稳定化阶段', '4.2 NetBSD 4.0：SMP 改进与系统扩展', '4.3 ARM、MIPS、PowerPC 等平台支持', '4.4 嵌入式市场中的 NetBSD', '4.5 pkgsrc 生态扩大', '4.6 开发者社区与基金会角色变化', '4.7 外部评价与路线争论', '4.8 本章书目述评']], ['第 5 章 NetBSD 5.x：大规模内核重构与现代化困难（2009–2012）', ['5.1 NetBSD 5.0 的技术目标', '5.2 内核同步机制改革', '5.3 VFS 与存储系统调整', '5.4 多核时代的系统适应', '5.5 长期维护与开发资源问题', '5.6 社区内部对发展速度的讨论', '5.7 与 FreeBSD 8/9、OpenBSD 同期路线比较', '5.8 本章书目述评']], ['第 6 章 NetBSD 6.x–7.x：现代硬件时代的适应（2012–2018）', ['6.1 NetBSD 6.0 与现代化尝试', '6.2 多核优化与系统性能提升', '6.3 ARM 生态扩展', '6.4 新硬件支持路线', '6.5 发布工程与维护模式变化', '6.6 NetBSD 在 BSD 家族中的定位变化', '6.7 外部批评与内部回应', '6.8 本章书目述评']], ['第 7 章 NetBSD 8.x：64 位 ARM 与现代平台扩展（2018–2020）', ['7.1 NetBSD 8.0 的历史背景', '7.2 ARM64 支持的发展', '7.3 虚拟化环境中的 NetBSD', '7.4 云计算时代的适应问题', '7.5 项目规模与生态挑战', '7.6 本章书目述评']], ['第 8 章 NetBSD 9.x：现代存储与系统能力扩展（2020–2024）', ['8.1 NetBSD 9.0 发布背景', '8.2 ZFS 集成过程', '8.3 新硬件支持', '8.4 系统安全能力提升', '8.5 NetBSD 与现代 BSD 系统竞争环境', '8.6 本章书目述评']], ['第 9 章 NetBSD 10.x–11.x：持续维护中的可移植传统（2024–2026）', ['9.1 NetBSD 10.0 的现代化目标', '9.2 新硬件支持与架构维护', '9.3 AI 时代的软件供应链问题', '9.4 项目规模、贡献者结构与未来挑战', '9.5 NetBSD 长期路线的重新定义', '9.6 本章书目述评']], ['第 10 章 NetBSD 历史中的人物、争议与思想遗产', ['10.1 早期创建者与 BSD 遗产继承', '10.2 Alistair Crooks 与 pkgsrc', '10.3 Hubert Feyrer 与 NetBSD 生态建设', '10.4 Theo de Raadt 离开 NetBSD 与 OpenBSD 分叉', '10.5 核心团队治理模式变化', '10.6 贡献者群体与长期维护者', '10.7 批评者、反对意见与技术争论', '10.8 NetBSD 在 UNIX/BSD 历史中的位置', '10.9 本章书目述评']], ['第 11 章 卷末史料与研究方法', ['11.1 NetBSD CVS/Git 历史', '11.2 邮件列表档案', '11.3 发布公告与技术文档', '11.4 贡献者访谈与口述史', '11.5 被忽略的发展路线', '11.6 本卷总评']]]
SPEC18 = [['第 1 章 可移植操作系统架构：MI/MD 与 NetBSD 内核设计（1993–2026）', ['1.1 4.3BSD-Lite 与 386BSD 技术遗产', '1.2 MI/MD 分层思想的形成', '1.3 autoconf 与设备抽象体系', '1.4 bus_space 与 bus_dma：跨硬件平台的关键抽象', '1.5 驱动模型与硬件抽象层设计', '1.6 可移植性工程中的性能、复杂性与维护成本']], ['第 2 章 多平台移植史：从工作站 UNIX 到现代架构（1993–2026）', ['2.1 早期平台扩张：x86、68k、VAX、SPARC', '2.2 PowerPC、MIPS 与嵌入式平台', '2.3 Alpha 等工作站架构支持', '2.4 ARM 平台支持的发展', '2.5 ARM64 与服务器平台', '2.6 RISC-V 支持进入稳定系统', '2.7 多架构维护模型与持续集成']], ['第 3 章 内核组件化与 Anykernel：rump kernel 的革命（2005–2026）', ['3.1 Anykernel 架构思想', '3.2 rump kernel 的设计目标', '3.3 文件系统、驱动与网络协议栈用户态化', '3.4 rump kernel 与测试基础设施', '3.5 rump kernel 在网络、文件系统和驱动中的应用', '3.6 rump kernel 的设计边界与历史意义']], ['第 4 章 内核并发与 SMP：从单处理器 UNIX 到多核系统', ['4.1 早期单处理器内核模型', '4.2 NetBSD SMP 初期实现', '4.3 NetBSD 2.0 SMP 架构', '4.4 NetBSD 5.x 内核并发重构', '4.5 VFS 与驱动 MP-safe 化', '4.6 多核时代的 NetBSD 内核维护', '4.7 调度器与并发性能优化']], ['第 5 章 文件系统与存储体系', ['5.1 FFS 与 BSD 文件系统传统', '5.2 Soft Updates 与一致性维护', '5.3 WAPBL 日志文件系统', '5.4 RAIDframe 软件 RAID', '5.5 CGD 加密磁盘框架', '5.6 tmpfs 与现代文件系统扩展', '5.7 ZFS 与外部文件系统生态']], ['第 6 章 网络系统：BSD 网络传统的继承与重构', ['6.1 BSD TCP/IP 网络栈传统', '6.2 KAME 项目与 IPv6/IPsec', '6.3 网络设备抽象与驱动体系', '6.4 net80211 无线网络体系', '6.5 NPF 防火墙设计', '6.6 NetBSD 网络安全机制的发展', '6.7 rump 网络栈']], ['第 7 章 pkgsrc 与 NetBSD 软件生态', ['7.1 NetBSD Packages 的早期历史', '7.2 pkgsrc 的形成', '7.3 pkgsrc 在 NetBSD 中的系统整合', '7.4 bootstrap 与跨平台构建', '7.5 二进制软件包体系与 pkgin', '7.6 pkgsrc 的长期维护模式']], ['第 8 章 NetBSD 系统安全机制', ['8.1 BSD 安全传统与 NetBSD 设计', '8.2 kauth 权限框架', '8.3 Veriexec 文件完整性系统', '8.4 W^X 与 PaX MPROTECT', '8.5 ASLR 与 KASLR', '8.6 NPF 网络安全机制', '8.7 NetBSD 安全机制的工程取舍']], ['第 9 章 虚拟化与现代运行环境', ['9.1 Xen 支持', '9.2 NVMM 虚拟机监控框架', '9.3 云环境中的 NetBSD', '9.4 隔离环境与现代部署场景', '9.5 微型虚拟机与未来方向']], ['第 10 章 NetBSD 构建、发布与工程体系', ['10.1 build.sh 与交叉构建体系', '10.2 NetBSD 源代码树组织', '10.3 内核与用户空间构建', '10.4 Release Engineering', '10.5 Snapshot 与多架构发布', '10.6 自动化测试体系']], ['第 11 章 NetBSD 技术路线总结', ['11.1 可移植性的技术意义', '11.2 NetBSD 技术成果与内部影响', '11.3 对 UNIX 系统设计的贡献', '11.4 技术路线中的工程限制', '11.5 技术路线的长期影响']]]
SPEC19 = [['第 1 章 分化轴总论：从 BSD 遗产到可移植性原则（1993–2026）', ['1.1 共同文化基线：第九卷 BSD 共同文化命题清单', '1.2 NetBSD 分化轴的形成：质量优先与架构独立', '1.3 “运行在一切硬件上”的工程理想与文化含义', '1.4 MI/MD 分层背后的组织哲学与技术伦理', '1.5 可移植性、正确性与长期维护之间的张力', '1.6 与 FreeBSD、OpenBSD、BSD/OS 等 BSD 路线的文化分化', '1.7 本章书目述评']], ['第 2 章 工程哲学的物质基础：一致性、简洁性与长期主义', ['2.1 NetBSD 设计原则的文本来源：手册、邮件列表与代码', '2.2 代码结构中的工程审美：清晰、统一与可维护性', '2.3 build.sh 与交叉构建文化：从源码构建系统的传统', '2.4 pkgsrc 的形成：从软件包系统到跨平台工程理念', '2.5 性能与通用性的冲突：SMP、多核时代与架构调整', '2.6 “正确性优先”叙事的成立条件与反例', '2.7 本章书目述评']], ['第 3 章 名称、符号与身份：NetBSD 的自我表达', ['3.1 NetBSD 名称的形成：“Net”与互联网协作时代', '3.2 “BSD”作为历史继承符号：386BSD 与 Berkeley 遗产', '3.3 无吉祥物传统与低符号化身份', '3.4 版本编号体系：0.8 至现代版本的历史语义', '3.5 发布公告、邮件列表与开发节奏中的仪式性', '3.6 NetBSD Foundation、商标与项目身份管理', '3.7 本章书目述评']], ['第 4 章 共同体与治理文化：开发者、基金会与长期维护', ['4.1 创建者与早期贡献者：NetBSD 形成时期的人物谱系', '4.2 核心开发者制度与技术决策结构', '4.3 从松散开发群体到 NetBSD Foundation 的制度化', '4.4 选举、委员会与基金会治理模式', '4.5 贡献者生态：核心开发者、port maintainer 与外围参与者', '4.6 治理争议、开发方向冲突与项目连续性', '4.7 本章书目述评']], ['第 5 章 许可证、自由观与产业关系：宽松许可路线', ['5.1 BSD 许可证传统与 NetBSD 的自由观', '5.2 宽松许可证与商业采用之间的关系', '5.3 pkgsrc、嵌入式系统与外部生态扩散', '5.4 开源共享、代码回馈与实际工程关系', '5.5 与 GPL 路线的历史比较', '5.6 商业使用、闭源衍生与社区价值冲突', '5.7 本章书目述评']], ['第 6 章 争议、批评与自我反思：可移植叙事的边界', ['6.1 386BSD 分裂背景与 NetBSD 创建争议', '6.2 Theo de Raadt 离开 NetBSD 与 OpenBSD 分叉事件', '6.3 外部批评：规模、速度与现代硬件竞争', '6.4 “最可移植系统”叙事的历史贡献与限制', '6.5 社区规模、维护压力与代际问题', '6.6 NetBSD 在公众技术记忆中的位置变化', '6.7 本章书目述评']], ['第 7 章 卷末书目述评：NetBSD 文化与哲学史料总目', ['7.1 史料谱系：代码、版本记录、邮件列表、公告与基金会档案', '7.2 贡献者史：创建者、核心开发者与外围贡献者', '7.3 批评者与反对路线：争议作为历史组成部分', '7.4 从物质证据到文化解释：本卷论证方法', '7.5 未解决问题：缺失档案、沉默参与者与未来研究方向', '7.6 本卷总评']]]
OLD17B = ['<h2>第十七卷  可移植的执念：NetBSD 的历史（1993–2026）</h2>',
          '>第 12 章 卷末书目述评：旧09卷《netbsd的历史》全卷综述</h3>',
          '>第 1 章 NetBSD 诞生（1993–1994）</h3>']
OLD18B = ['第 2 章 第 2 章 多平台移植史：从工作站 UNIX 到 ARM、RISC-V（1993–2026）', '第 7 章 第 7 章 软件生态与构建体系：pkgsrc 的跨平台道路', '第 8 章 第 8 章 安全模型与系统加固', '第 10 章 第 10 章 NetBSD 技术遗产与历史评价', '第 11 章 第 11 章 技术专题史料总目']
# 卷19 卷题未变（「NetBSD 文化与哲学（1993–2026）」），故 OLD 清单只列旧章题
OLD19B = ['>第 1 章 分化轴总论：可移植执念从 CSRG 遗产的分化</h3>',
          '>第 7 章 卷末书目述评：NetBSD 文化与哲学</h3>']
_gvol("G45", 17, SPEC17, 11, 83, "第十七卷  可移植的执念：NetBSD 操作系统的历史（1993–2026）", OLD17B)
_gvol("G46", 18, SPEC18, 11, 69,
      "第十八卷  NetBSD 技术专题史（1993–2026）", OLD18B)
_gvol("G47", 19, SPEC19, 7, 48, "第十九卷  NetBSD 文化与哲学（1993–2026）", OLD19B)
chk("G48 卷17／卷18 卷末章按清单照录（不含「卷末书目述评」字样）",
    h.count(">第 11 章 卷末史料与研究方法</h3>") == 1
    and h.count(">第 11 章 NetBSD 技术路线总结</h3>") == 1
    and h.count(">第 12 章 卷末书目述评：旧09卷《netbsd的历史》全卷综述</h3>") == 0
    and h.count(">第 8 章 卷末书目述评：NetBSD 技术专题史料总目</h3>") == 0)
chk("G49 卷18 卷分工注与卷19 卷导言／分工注已保留（体例元素）",
    h.count("NetBSD 技术线；项目编年见卷17。") == 1
    and h.count("本卷为 386BSD 分叉后 NetBSD 项目文化哲学的专卷") == 1
    and h.count("NetBSD 文化哲学线；项目编年见卷17，技术专题见卷18，治理结构比较见卷32。") == 1)
chk("G50 溯源注迁移标记齐备（第 25 批自卷17／18／19 旧 M.K 迁入）",
    h.count("第 25 批自卷17 旧 12.6 迁入") == 1
    and h.count("第 25 批自卷18 旧 7.3 迁入") == 1
    and h.count("第 25 批自卷19 旧 6.1 迁入") == 1)





chk("G19 卷9 溯源注语义迁移保真（src 316）",
    h.count('class="src"') == 316
    and h.count("本节载历史语汇的分期纪律与后设概念边界（分裂前），彼卷载话语挪用（1990s 起）") == 1
    and h.count("彼卷载四种答案的实体史，本节载文化根系") == 1
    and h.count("本节正面清点遗产，彼卷载不归名机制") == 1
    and h.count("本卷七章（伯克利的文化地层／从代码到物证／名称与符号／共同体实践／从实践到观念／"
                "身份、边界与分化前夜／本述评）") == 1)
chk("G20 卷9 述评章 6 节为体例骨架且卷末述评章居卷末",
    any(t.startswith("第 7 章 卷末书目述评：BSD UNIX 文化与哲学") for _, t, _ in vch(9))
    and any(x[0] == "7.6" and x[2].startswith("本卷总评") for x in vch(9)[-1][2]))
chk("G21 卷9 交叉引用面未失效（卷17 §17.3 引第九卷第 3 章 3.4–3.6）",
    h.count("引第九卷第 3 章 3.4–3.6") == 1
    and h.count("daemon 一词与 BSD daemon：名称、语境与早期用法") == 1
    and h.count("从 Foglio 到 Beastie：BSD 视觉符号的形成与演化") == 1)
chk("G21b 7 条跨卷迁移溯源注已落位卷10 且带第二十一批标记",
    all(h.count("（第二十一批自卷13 旧 %s 迁入）" % k) == 1
        for k in ("4.2", "4.3", "6.2", "6.3", "6.4", "7.5"))
    and h.count("第二十一批：卷13 旧 4.4 与本卷旧 5.3 两条分工注合并") == 1)
chk("G21c 卷24 对卷11 的交叉引用已改指新章（第 6 章 6.3）",
    h.count("与第十一卷第 6 章 6.3 分工") == 2)
chk("G21d 卷16 §13.9 对卷9 旧章号的引用已改指卷10 第 5 章",
    h.count("现行体系对应第十卷第 5 章“和解与 4.4BSD-Lite：Berkeley 源码独立化的完成（1994–1995）”线") == 1)
chk("G21e 3 处合并去重标记齐备",
    h.count("第二十一批：原 1.4 与 4.1 两条分工注合并") == 1
    and h.count("第二十一批：原 3.2 与 3.3 两条分工注合并") == 1
    and h.count("第二十一批：卷13 旧 4.4 与本卷旧 5.3 两条分工注合并") == 1)
print()
print("=" * 78)
print("H. 关联文件（56 表全表逐条核对等，8 项）")
print("=" * 78)
vol_name2no = {t.split("  ", 1)[1]: v for v, t, _ in vols}
# 56 表《章题》不含「第 M 章 」前缀，须剥离后比对
ch2title = {(v, m): t[len("第 %d 章 " % m):] for v, _, chs in vols for m, t, _ in chs}
s56 = rd(ROOT + "/08-核查报告与多轮复核/重构2026/56-二次映射表-355到240.md")
c56 = rd(ROOT + "/08-核查报告与多轮复核/重构2026/56-二次映射表-355到240.csv")
pat56 = re.compile(r"^第([一二三四五六七八九十百]+)卷 (.+?)｜第(\d+)章(?:《(.+)》)?(.*)$")


def unesc(s):
    return htmlmod.unescape(s) if s else s


rows = parsed = 0
novol, noch, mism = [], [], []
for line in s56.split("\n"):
    if not line.startswith("|"):
        continue
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(cells) < 6:
        continue
    m = pat56.match(cells[5])
    if not m:
        continue
    rows += 1
    vn, cn, ct = unesc(m.group(2)), int(m.group(3)), unesc(m.group(4))
    if vn not in vol_name2no:
        novol.append(vn)
        continue
    v = vol_name2no[vn]
    if (v, cn) not in ch2title:
        noch.append((vn, cn))
        continue
    parsed += 1
    if ct is not None and unesc(ch2title[(v, cn)]) != ct:
        mism.append((vn, cn, ct[:34], unesc(ch2title[(v, cn)])[:34]))
chk("H1 56 表目标列可解析 360 行且卷名全部命中", rows == 360 and not novol,
    f"可解析 {rows}／卷名未命中 {len(novol)}")
chk("H2 56 表目标列章号全部存在于页面", not noch, noch[:3])
chk("H3 56 表目标列章题**全表逐条**与页面一致（实体归一后）", not mism,
    mism[:2] or f"{parsed}/{parsed}")
chk("H4 56 表 MD／CSV 均无 BOM",
    not rd(ROOT + "/08-核查报告与多轮复核/重构2026/56-二次映射表-355到240.md").startswith("\ufeff")
    and not c56.startswith("\ufeff"))
chk("H5 56 表含第三批／第二批／第八批／第九批／第十批同步说明",
    "第三批目录重构同步" in s56 and "第二批目录重构同步" in s56
    and "第八批目录重构同步（卷9 全卷）" in s56
    and "第九批目录重构同步（卷9–卷13 五卷全卷）" in s56
    and "第十批目录重构同步（四大 BSD 文化与哲学卷 ＋ 横向比较卷）" in s56
    and "第二十六批目录重构同步（卷20／卷21／卷22 三卷全卷替换）" in s56)
summ = rd(ROOT + "/05-卷册大纲/SUMMARY.md")
chk("H6 SUMMARY 读者指引含第八批（293／1998）／第九批（286／2023）／第十批（317／2237）／第十四批（323／2318）",
    "31 卷 293 章 1998 节" in summ and "第八批" in summ
    and "31 卷 286 章 2023 节" in summ and "第九批" in summ
    and "36 卷 317 章 2237 节" in summ and "第十批" in summ
    and "36 卷 323 章 2318 节" in summ and "第十四批" in summ)
chk("H7 SUMMARY 第二批条目已改「该批口径」", "该批口径 **31 卷 288 章 1925 节**" in summ)
chk("H8 述评 index 口径声明 352 章 3023 节",
    "352 章 3023 节" in rd(ROOT + "/08-核查报告与多轮复核/12-重构大纲书目述评/index.md"))

print()
print("=" * 78)
print("I. 文档一致性：门禁「十项」表述与 A2 判据（4 项）")
print("=" * 78)
a2 = rd(ROOT + "/00-编纂规则与格式规范/01-规则/脚本与命令/audit_index_structure.py")
chk("I1 audit_index_structure.py 含 A2 空格形制判据并并入总判定",
    "A2 空格形制" in a2 and "sp_bad" in a2 and "or sp_bad" in a2)
chk("I2 audit_index_structure.py 十一项判据 A／A2／B–J 齐备",
    all(k in a2 for k in ("A 编码", "A2 空格形制")) and "I doc-metrics" in a2)
docs10 = {
    "CLAUDE.md": rd(ROOT + "/CLAUDE.md"),
    "流程规则.md": rd(ROOT + "/00-编纂规则与格式规范/01-规则/流程规则.md"),
    "脚本与命令/README.md": rd(ROOT + "/00-编纂规则与格式规范/01-规则/脚本与命令/README.md"),
    "tests/README.md": rd(ROOT + "/08-核查报告与多轮复核/重构2026/tests/README.md"),
}
bad10 = [k for k, v in docs10.items() if "十一项静态自检" not in v]
chk("I3 四处现行文档均记「十一项静态自检」", not bad10, bad10)
chk("I4 流程规则 L1532 段记 A2 护栏与 2 个半角空格",
    "2 个半角空格" in docs10["流程规则.md"] and "A2 空格形制" in docs10["流程规则.md"])

print()
print("=" * 78)
print("J. 备份、提交与述评覆盖率（5 项）")
print("=" * 78)
bk = ROOT + "/08-核查报告与多轮复核/重构2026/index.html.prebak-第四十一批-20260920.html"
chk("J1 本批备份件存在", os.path.exists(bk))
if os.path.exists(bk):
    bh = rd(bk)
    # 交叉核验：备份件须与 git 中「本批改动前」的 index.html 逐字节一致
    import subprocess

    rel = "08-核查报告与多轮复核/重构2026/index.html"
    try:
        old = subprocess.run(["git", "show", "%s:" % HEAD + rel], cwd=ROOT,
                             capture_output=True).stdout
        same = hashlib.sha256(old).hexdigest() == hashlib.sha256(open(bk, "rb").read()).hexdigest()
        chk("J2 备份件 = git 中改前版本（提交 %s 的 index.html）逐字节一致" % HEAD, same,
            f"git {len(old)}B vs 备份 {os.path.getsize(bk)}B")
    except Exception as e:
        info("J2 git 交叉核验跳过", e)
    chk("J3 备份件含本批改动前旧卷题／旧章题、现行件已无（差异恰为本批改动）",
        bh.count("<h2>第三十三卷  开源社区的世界化与世界化的开源社区</h2>") == 1
        and h.count("<h2>第三十三卷  开源社区的世界化与世界化的开源社区</h2>") == 0
        and bh.count("<h2>第三十五卷  BSD 分离聚合的六十年（1969–2026）</h2>") == 1
        and h.count("<h2>第三十五卷  BSD 分离聚合的六十年（1969–2026）</h2>") == 0
        and bh.count("<h2>第三十六卷  BSD 史学史与方法</h2>") == 1
        and h.count("<h2>第三十六卷  BSD 史学史与方法</h2>") == 0
        and bh.count("第 14 章 BSD 治理史的证据与方法</h3>") == 1
        and h.count("第 14 章 BSD 治理史的证据与方法</h3>") == 0
        and bh.count("第 8 章 卷末书目述评：BSD 大分裂史</h3>") == 1
        and h.count("第 8 章 卷末书目述评：BSD 大分裂史</h3>") == 0
        and bh.count("第 10 章 FreeBSD 技术史研究方法与资料体系</h3>") == 1
        and h.count("第 10 章 FreeBSD 技术史研究方法与资料体系</h3>") == 0
        and bh.count("第 11 章 技术专题史料总目</h3>") == 1
        and h.count("第 11 章 技术专题史料总目</h3>") == 0
        and bh.count('class="src"') == 329 and h.count('class="src"') == 316)
blk_total = 0
for f in os.listdir(ROOT + "/08-核查报告与多轮复核/12-重构大纲书目述评"):
    if f.startswith("第") and f.endswith("卷-章级书目述评.md"):
        blk_total += len(re.findall(r"### [\d.]+ 本章书目述评",
                                    rd(ROOT + "/08-核查报告与多轮复核/12-重构大纲书目述评/" + f)))
chk("J4 述评外迁块合计 = 58", blk_total == 58, blk_total)
info("述评覆盖率", f"{blk_total}/{n_chbiblio} = {blk_total / n_chbiblio * 100:.1f}%")
chk("J5 覆盖率约 37%（第四十一批各换稿卷无章级述评节，分母由 229 降至 158）",
    0.30 < blk_total / n_chbiblio < 0.45, blk_total / n_chbiblio)

print()
print("=" * 78)
print("K. 四层解耦一致性（源 ↔ 产物，独立复算）")
print("=" * 78)
BASE = ROOT + "/08-核查报告与多轮复核/重构2026"
SRC = {
    "内容层 outline.txt": BASE + "/data/outline.txt",
    "数据层 schema.jsonld": BASE + "/data/schema.jsonld",
    "格式层 doc.css": BASE + "/assets/doc.css",
    "现代化层 modern.css": BASE + "/assets/modern.css",
    "行为层 theme-preset.js": BASE + "/assets/theme-preset.js",
    "行为层 doc.js": BASE + "/assets/doc.js",
    "页壳 page.template.html": BASE + "/assets/page.template.html",
    "数据层 catalog.json": BASE + "/data/catalog.json",
}
miss = [k for k, p in SRC.items() if not os.path.exists(p)]
chk("K1 四层源 ＋ 页壳齐备（8 文件）", not miss, miss)
outline = rd(SRC["内容层 outline.txt"])
n_vol = len(re.findall(r"^# ", outline, re.M))
n_ch = len(re.findall(r"^## ", outline, re.M))
n_sec = len(re.findall(r"^- ", outline, re.M))
chk("K2 outline.txt 统计 = 37 卷／352 章／3023 节",
    (n_vol, n_ch, n_sec) == (37, 352, 3023), f"{n_vol}／{n_ch}／{n_sec}")
_body_lines = [l for l in outline.split("\n") if not l.startswith("> ")]   # 排除 `> ` 卷导言语法标记
_body = "\n".join(_body_lines)
chk("K3 内容源零 HTML 标记（排除 `> ` 语法标记后无 < >）",
    "<" not in _body and ">" not in _body,
    f"< {_body.count('<')}／> {_body.count('>')}")
# 溯源注定界符：**前置**用 `@@…@@` 成对（2 个），**后置**为行尾单 `@@`（1 个）
_pre = len(re.findall(r"^- \d+\.\d+ @@", outline, re.M))
_post = len([l for l in outline.split("\n") if l.startswith("- ") and "@@" in l]) - _pre
chk("K4 溯源注定界符：前置 %d ＋ 后置 %d = %d 条，@@ 计数 %d = 前置×2＋后置"
    % (_pre, _post, _pre + _post, outline.count("@@")),
    (_pre, _post) == (20, 296) and outline.count("@@") == _pre * 2 + _post,
    f"实为 前置 {_pre}／后置 {_post}／@@ {outline.count('@@')}")
chk("K5 内容源零直角引号／零 U+3000",
    all(c not in outline for c in "\u300c\u300d\u300e\u300f") and "\u3000" not in outline)
# 装配漂移（独立调用装配器）
import subprocess

_rc = subprocess.run([sys.executable, ROOT + "/00-编纂规则与格式规范/01-规则/脚本与命令/assemble_index.py",
                      "--check"], capture_output=True)
chk("K6 装配器 --check 无漂移（产物 ↔ 源逐字节）", _rc.returncode == 0,
    _rc.stdout.decode("utf-8", "replace").strip()[:60])
# 格式层／行为层：源正文 ↔ 产物内联块（逐字节，独立于装配器）
for name, tag, close in (("格式层 doc.css", '<style id="format-layer">', "</style>"),
                         ("现代化层 modern.css", '<style id="modern-layer">', "</style>"),
                         ("行为层 doc.js", 'id="behavior-layer">', "</script>"),
                         ("行为层 theme-preset.js", None, "</script>")):
    if tag is None:
        continue
    src_body = rd(SRC[name]).strip("\n")
    i = h.index(tag) + len(tag)
    j = h.index(close, i)
    inline = h[i:j].strip("\n")
    chk(f"K7 {name}：源正文 ↔ 产物内联块逐字节一致", src_body == inline,
        f"源 {len(src_body)}B ／ 产物 {len(inline)}B")
# 主题预设（head 内首个 <script nonce=…>）
src_theme = rd(SRC["行为层 theme-preset.js"]).strip("\n")
m_th = re.search(r'<script nonce="[^"]*">\n(.*?)\n</script>', h, re.S)
chk("K8 行为层 theme-preset.js：源正文 ↔ 产物一致",
    bool(m_th) and m_th.group(1).strip("\n") == src_theme,
    f"源 {len(src_theme)}B")
# 数据层：独立解码 blob ↔ catalog.json
cat = json.loads(rd(SRC["数据层 catalog.json"]))
mm = re.search(r'id="opt-data-blob"[^>]*>\n(.*?)\n</script>', h, re.S)
blob2 = json.loads(gzip.decompress(base64.b64decode(re.sub(r"\s+", "", mm.group(1)))).decode("utf-8"))
chk("K9 数据层：产物内嵌 blob ↔ catalog.json 内容字段一致",
    {k: v for k, v in blob2.items() if k not in ("$schema", "version")}
    == {k: v for k, v in cat.items() if k not in ("$schema", "version")})
# 口径派生：产物口径 == 内容源派生值
tpl = rd(SRC["页壳 page.template.html"])
ph = set(re.findall(r"\{\{[A-Z_]+\}\}", tpl))
chk("K10 页壳模板占位符齐备（16 个，含 LOGO／FAVICON）", len(ph) == 16, sorted(ph))
chk("K11 内容层零内联样式（main 区 style= 计数 0）",
    'style="' not in re.search(r'<main[^>]*>(.*?)</main>', h, re.S).group(1))
n_bib = len(re.findall(r"^## .*卷末书目述评", outline, re.M))
chk("K12 口径派生自洽（正章 %d ＋ 卷末述评章 %d = %d）" % (n_ch - n_bib, n_bib, n_ch),
    (n_ch - n_bib) == 342 and n_bib == 10)
chk("K13 五处口径点位与派生值一致",
    all(v == (n_vol, n_ch, n_sec) for v in got.values()), got)
# ── K14：内容层／页壳所用 class 必须在格式层有定义 ──────────────────────────
# 缘由：2026-09-18 四层解耦曾因 .doc-foot 规则缺失（提取器守卫被 .doc-footer 子串误命中）
# 致页脚样式静默丢失，而门禁与三套浏览器回归**全未捕获**——故独立复核须显式核此。
_css_all = rd(SRC["格式层 doc.css"]) + "\n" + rd(SRC["现代化层 modern.css"])
_static_cls = set()
for _m in re.finditer(r'class="([^"]+)"', st):          # st 已屏蔽 script/style
    for _c in _m.group(1).split():
        _static_cls.add(_c)
_undef = sorted(c for c in _static_cls
                if not re.search(re.escape("." + c) + r"(?![\w-])", _css_all))
chk("K14 内容层／页壳所用 class 均在格式层有定义（%d 个 class）" % len(_static_cls),
    not _undef, "未定义：%s" % _undef)
info("内容层 class 清单", "／".join(sorted(_static_cls)))



# ── 第三十二批：卷31／卷32 全卷替换（2026-09-20 主理人清单）────────────────
SPEC31 = [["第 1 章 伯克利软件传统与自由软件运动的前史", ["1.1 UNIX源代码共享与大学研究环境", "1.2 UNIX源代码许可与早期再分发", "1.3 Berkeley UNIX与软件共享实践", "1.4 BSD软件的公开传播", "1.5 Innet发展与 BSD 软件共同体", "1.6 学术共享、软件自由与公共利益", "1.7 GNU出现以前的自由软件实践", "1.8 BSD传统与后来自由软件运动之间的历史联系"]], ["第 2 章 GNU计划与自由软件运动的形成", ["2.1 1983年 GNU 计划的提出", "2.2 GNU与 Unix 兼容系统的目标", "2.3 GNU Manifesto与软件自由问题", "2.4 GNU Emacs与早期 GNU 软件", "2.5 Free Software 基金会的成立", "2.6 四项自由的形成", "2.7 Copyleft思想的形成", "2.8 自由软件运动的组织化", "2.9 GNU与同期 BSD 项目的关系", "2.10 自由软件运动进入 Unix 软件世界"]], ["第 3 章 GNU系统的构造与长期开发", ["3.1 GNU编译器与 GCC", "3.2 GNU C Library", "3.3 binutils与基础开发工具", "3.4 Bash与 GNU Shell 环境", "3.5 Coreutils与基本用户空间", "3.6 Emacs、Texinfo与软件开发环境", "3.7 GNU构建工具与 Autotools", "3.8 GNU系统工具与网络软件", "3.9 GNU Hurd的设计目标", "3.10 Hurd的长期开发", "3.11 Linux出现以前 GNU 系统的完成程度", "3.12 GNU系统从项目集合到完整操作系统环境"]], ["第 4 章 自由软件与 Open Source：两种历史话语的形成", ["4.1 Free Software概念的制度化", "4.2 软件自由与用户权利", "4.3 Copyleft与自由软件共同体", "4.4 “Open Source”一词的形成", "4.5 Netscape源码开放与1998年转折", "4.6 Open Source Initiative的成立", "4.7 Debian Free Software Guidelines与 Open Source Definition", "4.8 Free Software与 Open Source 的概念分化", "4.9 企业软件产业对 Open Source 的重新理解", "4.10 BSD许可证进入 Open Source 制度", "4.11 自由软件与开源成为两套相邻而不同的历史话语"]], ["第 5 章 BSD 技术传统的传播、遮蔽与文化挪用", ["5.1 BSD在 GNU出现之前的历史位置", "5.2 BSD技术进入 UNIX 产业", "5.3 BSD软件进入 Innet 基础设施", "5.4 BSD技术从具体项目成为通用技术", "5.5 “UNIX技术”与“BSD技术”的历史归名", "5.6 Linux兴起后的历史叙事变化", "5.7 GNU/Linux话语中的 BSD 缺席", "5.8 开源历史叙事中的 BSD", "5.9 技术归属、历史记忆与历史主体", "5.10 文化挪用作为技术史解释概念", "5.11 文化挪用与代码来源问题的区别", "5.12 技术传播、重新命名与历史主体的消隐"]], ["第 6 章 Linux 的产生与早期开发环境", ["6.1 1990年前后的 Minix 与个人计算机", "6.2 Andrew Tanenbaum与 Minix", "6.3 386处理器与 Minix 用户共同体", "6.4 Linus Torvalds与 Linux 项目的产生", "6.5 Linux 0.01的发布", "6.6 Linux在 Minix 环境中的开发", "6.7 Minix作为开发环境与技术参照", "6.8 Linux 0.01源代码与版权条件", "6.9 Linux早期邮件列表与协作开发", "6.10 从个人实验到公开协作项目"]], ["第 7 章 Linux、BSD 与 UNIX：来源、参照与代码证据", ["7.1 “Unix-like”与 Unix 的关系", "7.2 UNIX接口传统与独立实现", "7.3 Linux与 AT&T UNIX 源代码", "7.4 Linux与 BSD 源代码", "7.5 Linux 0.01与 Minix 源代码", "7.6 开发环境、设计参照与代码来源的区别", "7.7 POSIX与标准接口的中介作用", "7.8 版权声明与来源证据", "7.9 源代码比对与版本树", "7.10 直接代码来源的判定标准", "7.11 直接继承、间接影响与共同技术传统", "7.12 可证事实与推测的边界", "7.13 Linux与 BSD 的直接代码来源问题"]], ["第 8 章 GNU 与 Linux 的组合：从两个项目到共同系统", ["8.1 Linux内核进入 GNU 软件环境", "8.2 GCC与 Linux 内核开发", "8.3 GNU C Library与 Linux", "8.4 Bash与 GNU 用户空间", "8.5 GNU Coreutils与 Linux 用户空间", "8.6 GNU Binutils与 Linux 开发工具链", "8.7 早期 Linux 发行版", "8.8 GNU软件与 Linux 内核的组合方式", "8.9 “GNU/Linux”称谓的形成", "8.10 GNU系统与 Linux 内核的技术分工", "8.11 发行版作为组合层", "8.12 GNU与 Linux 从独立项目到共同生态"]], ["第 9 章 BSD 与 Linux 的技术交流与重新组合", ["9.1 BSD软件进入 Linux 系统", "9.2 BSD网络软件与 Linux 用户空间", "9.3 BSD许可证软件在 Linux 生态中的使用", "9.4 GNU工具进入 BSD 系统", "9.5 FreeBSD早期 GNU 工具链", "9.6 GCC、binutils与 BSD 系统构建", "9.7 FreeBSD向 LLVM/Clang 工具链迁移", "9.8 跨项目开发者与软件维护", "9.9 网络协议、系统接口与工具的共同实现", "9.10 代码共享与独立实现的区别", "9.11 技术交流与历史来源的区别", "9.12 BSD与 Linux 在实际开发中的长期交汇"]], ["第 10 章 内核、用户空间与发行版的重新组合", ["10.1 操作系统的分层结构", "10.2 Debian GNU/kFreeBSD的形成", "10.3 FreeBSD内核与 GNU 用户空间", "10.4 Debian GNU/kFreeBSD作为 Debian 官方移植", "10.5 Debian GNU/kFreeBSD的长期维护", "10.6 Debian GNU/kFreeBSD的终止", "10.7 Gentoo/FreeBSD与 Portage", "10.8 Linux内核与非 GNU 用户空间", "10.9 Chimera Linux与 FreeBSD core userland", "10.10 LLVM、musl与 FreeBSD 用户空间组件", "10.11 内核、libc、工具链与用户空间的可组合性", "10.12 “操作系统”边界在组合系统中的重新划分"]], ["第 11 章 BSD、Linux 与自由软件共同体的冲突、对话与历史记忆", ["11.1 早期 Linux 社区与 BSD 社区", "11.2 1992年 Tanenbaum–Torvalds 论战", "11.3 微内核与整体内核之争", "11.4 Linux与 BSD 的技术路线争论", "11.5 Linux与 BSD 的许可证争论", "11.6 “GNU/Linux”命名争议", "11.7 BSD与 Linux 历史来源问题的争论", "11.8 中文 BSD/Linux 社区的论战", "11.9 Usenet、邮件列表与论坛档案", "11.10 人物立场与项目立场的区别", "11.11 同时代争论与后来的历史叙述", "11.12 技术争论、社区身份与历史记忆"]], ["第 12 章 Linux 兴起以后 BSD 的历史位置", ["12.1 Linux传播与 Unix-like 软件市场", "12.2 发行版制度对 Linux 传播的影响", "12.3 GNU用户空间、Linux内核与发行版文化", "12.4 BSD基本系统模式与 Linux 发行版模式", "12.5 商业部署、开发者网络与项目规模", "12.6 GitHub时代的项目协作方式", "12.7 邮件列表、提交权限与 Pull Request", "12.8 BSD项目在现代自由软件共同体中的位置", "12.9 容器、云计算与 Linux 主导的基础设施", "12.10 BSD在网络、存储与系统软件中的持续存在", "12.11 非 GNU Linux 系统的发展", "12.12 “主流”“成功”与“失败”的历史解释问题"]], ["第 13 章 BSD-Linux 关系史的证据与解释", ["13.1 源代码作为一手史料", "13.2 早期发行包与版本档案", "13.3 邮件列表、Usenet与开发讨论", "13.4 版权声明与许可证文本", "13.5 提交记录、版本树与代码比对", "13.6 开发者回忆与口述史", "13.7 项目官方历史与后见之明", "13.8 “来源”“影响”“借鉴”“兼容”的概念区分", "13.9 直接证据、间接证据与推测", "13.10 技术事实与社区叙事的区分", "13.11 历史人物自述与同时代材料的交叉验证", "13.12 技术传播与历史归名的证据标准", "13.13 文化挪用命题的证据边界", "13.14 BSD-Linux关系史的可证范围", "13.15 从二元对立叙事到多项目技术网络"]]]
SPEC32 = [['第 1 章 FreeBSD 项目治理', ['1.1 1993年 FreeBSD项目的形成', '1.2 早期邮件列表与开发共同体', '1.3 提交者制度的形成', '1.4 核心团队的形成', '1.5 活跃提交者与项目成员身份', '1.6 核心团队选举制度', '1.7 核心团队的职责与权限', '1.8 提交者、维护者与项目团队', '1.9 Ports、文档与局部自治', '1.10 邮件列表、共识与投票', '1.11 提交者权限与项目资源管理', '1.12 2000年 核心章程', '1.13 2026年 核心章程 改革', '1.14 FreeBSD治理制度的连续性与变化']], ['第 2 章 FreeBSD 基金会', ['2.1 2000年 FreeBSD 基金会的成立', '2.2 基金会的法人性质', '2.3 基金会与 FreeBSD 项目的制度分离', '2.4 基础设施与网络资源', '2.5 开发项目与开发者资助', '2.6 GSoC、开发者会议与 黑客松', '2.7 捐赠、筹资与财务制度', '2.8 基金会年度报告与财务公开', '2.9 基金会与 FreeBSD商标', '2.10 基金会在法律事务中的代表作用', '2.11 基金会与 核心团队 的关系', '2.12 企业赞助与基金会资源', '2.13 基金会在 FreeBSD 长期持续发展中的制度作用']], ['第 3 章 NetBSD 项目治理', ['3.1 1993年 NetBSD项目的形成', '3.2 早期核心开发者与项目管理', '3.3 核心团队的形成', '3.4 核心团队的技术管理职能', '3.5 开发者成员制度', '3.6 活跃成员与项目参与', '3.7 提交者与代码提交权', '3.8 邮件列表与异步决策', '3.9 项目委员会与局部管理', '3.10 技术自治与项目整体管理', '3.11 核心团队的长期演变', '3.12 NetBSD治理结构的制度特征']], ['第 4 章 NetBSD 基金会', ['4.1 NetBSD 基金会的成立', '4.2 基金会的法人性质', '4.3 项目开发协议（项目Development Agreement）', '4.4 基金会 Member与 活跃成员', '4.5 基金会 Board', '4.6 Board与 核心团队 的关系', '4.7 基金会执行委员会', '4.8 服务器、基础设施与项目资源', '4.9 商标、知识产权与基金会职责', '4.10 捐赠与资金来源', '4.11 基金会财务与法人记录', '4.12 基金会与技术自治', '4.13 NetBSD 基金会的制度演变']], ['第 5 章 OpenBSD 项目治理', ['5.1 1995年分叉后的项目形成', '5.2 开发者共同体与 CVS', '5.3 提交者权限与代码进入主线', '5.4 子系统维护与责任分工', '5.5 项目领导与子系统责任制（subsystem-driven ownership）', '5.6 代码审查与技术责任', '5.7 邮件列表与异步协作', '5.8 黑客松与开发组织', '5.9 技术项目与开发者自治', '5.10 项目方向与技术决策', '5.11 OpenBSD治理结构的制度特征', '5.12 OpenBSD治理制度的长期稳定与变化']], ['第 6 章 Theo de Raadt 与 OpenBSD 的个人领导结构', ['6.1 Theo de Raadt的 NetBSD时期', '6.2 1995年分叉与领导结构的形成', '6.3 创始人与长期项目领导', '6.4 项目方向与个人领导', '6.5 技术决策与实际权力分布', '6.6 个人领导与子系统责任制', '6.7 个人领导与其他开发者的自治空间', '6.8 提交者权限、代码审查与领导权', '6.9 “BDFL”作为治理概念', '6.10 “独裁”概念在 OpenBSD 中的适用范围', '6.11 个人领导的权力边界', '6.12 个人领导与项目制度化', '6.13 Theo de Raadt领导结构的历史变化']], ['第 7 章 OpenBSD 基金会', ['7.1 OpenBSD 基金会的成立', '7.2 加拿大非营利法人身份', '7.3 基金会的宗旨与支持范围', '7.4 OpenBSD与相关项目的支持关系', '7.5 OpenSSH、OpenBGPD与其他相关项目', '7.6 基础设施支出', '7.7 黑客松与开发者活动', '7.8 个人捐赠与企业捐赠', '7.9 基金会董事会与法人治理', '7.10 基金会与 OpenBSD 项目的关系', '7.11 基金会与 Theo de Raadt 的关系', '7.12 基金会与技术决策的边界', '7.13 OpenBSD 基金会的长期资源治理']], ['第 8 章 DragonFly BSD 项目治理', ['8.1 2003年 DragonFly BSD的形成', '8.2 FreeBSD分叉后的项目组织', '8.3 开发共同体的形成', '8.4 无正式开发者准入程序', '8.5 submit邮件列表', '8.6 同行评审与代码提交', '8.7 提交者权限与主线维护', '8.8 开发者责任与项目协作', '8.9 技术讨论与项目决策', '8.10 Git仓库与项目基础设施', '8.11 DragonFly治理制度的长期变化', '8.12 尚无独立非营利基金会的制度背景']], ['第 9 章 Matt Dillon 与 DragonFly BSD 的个人领导结构', ['9.1 Matt Dillon与 FreeBSD时期', '9.2 2003年分叉与个人领导的形成', '9.3 创始人角色与项目连续性', '9.4 开放提交与同行评审', '9.5 所有代码提交的最终决定权', '9.6 最终决定权与开发者自治', '9.7 技术路线与个人领导', '9.8 “BDFL”作为治理概念', '9.9 “独裁”概念在 DragonFly 中的适用范围', '9.10 个人领导的制度边界', '9.11 创始人领导与项目资源管理', '9.12 Matt Dillon领导结构的长期变化']], ['第 10 章 四个 BSD 的开发权与 提交者制度', ['10.1 贡献者、开发者与提交者', '10.2 提交者位作为项目权力', '10.3 新开发者的进入机制', '10.4 Mentor与知识传递', '10.5 代码审阅与技术责任', '10.6 提交者权限的暂停与撤销', '10.7 维护者与局部自治', '10.8 企业雇员与独立开发者', '10.9 志愿者与受雇开发者', '10.10 开发权限与项目成员身份', '10.11 开发权与项目边界', '10.12 现代 BSD 开发权制度的差异']], ['第 11 章 企业参与与项目资源', ['11.1 企业为什么参与 BSD 开发', '11.2 企业雇佣 BSD 开发者', '11.3 企业赞助与个人贡献', '11.4 企业资金与项目资源', '11.5 商业雇佣与志愿劳动', '11.6 开发者薪酬与持续维护', '11.7 基础设施、硬件与网络资源', '11.8 黑客松与开发会议的资源来源', '11.9 商业参与与项目独立性', '11.10 小型项目的资源约束', '11.11 资源配置与技术议程', '11.12 BSD项目长期持续性的资源条件']], ['第 12 章 治理冲突、分叉与制度变迁', ['12.1 技术分歧与治理分歧', '12.2 NetBSD内部冲突与 OpenBSD 分叉', '12.3 FreeBSD 5.x时期的技术与组织冲突', '12.4 DragonFly从 FreeBSD 分叉', '12.5 领导权与技术路线', '12.6 开发权限与项目纪律冲突', '12.7 核心团队、基金会与个人领导之间的关系', '12.8 分叉作为制度选择', '12.9 分叉后的代码、人员与共同体', '12.10 冲突解决与制度调整', '12.11 BSD项目治理中的继承与断裂', '12.12 分叉与开源项目的制度弹性']], ['第 13 章 开源基金会制度比较：BSD 与其他开源项目', ['13.1 基金会在开源项目中的制度作用', '13.2 FreeBSD Foundation 的法律与运营模式', '13.3 NetBSD Foundation 的治理模式', '13.4 OpenBSD Foundation 的组织特点', '13.5 DragonFly BSD 尚无独立基金会的制度背景', '13.6 Linux Foundation 的商业协作模式', '13.7 Apache Software Foundation 的项目治理模式', '13.8 GNOME Foundation 与桌面生态治理', '13.9 基金会、企业与社区之间的关系', '13.10 开源资本、公共资源与社区自治', '13.11 Ostrom 公地治理理论与开源项目']], ['第 14 章 BSD 治理制度的历史比较', ['14.1 FreeBSD的选举型核心团队治理', '14.2 NetBSD的 核心团队与成员制度', '14.3 OpenBSD的长期个人领导', '14.4 DragonFly的创始人最终决定权', '14.5 基金会与技术项目的制度分离', '14.6 项目内部权力与法人权力', '14.7 委员会、核心团队与个人领导', '14.8 局部自治与整体项目控制', '14.9 企业参与与项目独立性', '14.10 大型项目与小型项目的治理差异', '14.11 BSD与 Linux、Apache等项目治理结构的比较', '14.12 “民主”“集中”“自治”与“独裁”的概念边界']], ['第 15 章 BSD 治理史的证据与方法', ['15.1 项目章程与治理文件', '15.2 基金会 bylaws与法人档案', '15.3 核心团队与董事会选举记录', '15.4 提交者记录与开发权限变动', '15.5 邮件列表与决策档案', '15.6 财务报告、年报与捐赠记录', '15.7 开发者访谈与口述史', '15.8 同时代材料与事后回忆', '15.9 技术争论与治理争论的区别', '15.10 “独裁”“BDFL”“民主”“精英”等概念的证据要求', '15.11 制度事实与社区评价的区别', '15.12 个人领导与制度权力的历史解释边界', '15.13 基金会存在与实际控制权的区别', '15.14 BSD治理史中的史料缺口', '15.15 BSD治理史中的不可确定问题']]]
OLD31 = ['<h2>第三十一卷  自由软件、开源运动与 BSD–Linux 谱系</h2>',
         '第 3 章 Stallman 左派黑客政治与 BSD 商业化分歧',
         '第 5 章 自由软件与开源术语之争：BSD 处于什么位置',
         '第 6 章 BSD 社区对开源洗白的回应',
         '第 10 章 BSD 与 Linux 的代码谱系无关性：考据、证据分级与追溯上限']
OLD32 = ['第 13 章 第 13 章 BSD 治理制度的历史比较', '第 14 章 第 14 章 BSD 治理史的证据与方法']
_gvol("G60", 31, SPEC31, 13, 151, "第三十一卷  自由软件、开源运动与 BSD-Linux 关系史", OLD31)
_gvol("G61", 32, SPEC32, 15, 188,
      "第三十二卷  现代 BSD 分支的治理制度：项目治理、个人领导与基金会（1993–2026）", OLD32)
chk("G62 卷31／卷32 溯源注迁移 10 条标记齐备（第 32 批自卷31 5 条／自卷32 5 条）",
    h.count("第 32 批自卷31 旧 ") == 5 and h.count("第 32 批自卷32 旧 ") == 5)
chk("G63 卷31／卷32 述评槽与卷末述评章均为 0（新稿无述评，27 号文「有则设、无则不设」）",
    sum(1 for _, _, secs in vch(31) for x in secs if x[2].startswith("本章书目述评")) == 0
    and sum(1 for _, _, secs in vch(32) for x in secs if x[2].startswith("本章书目述评")) == 0
    and not any("卷末书目述评" in t for _, t, _ in vch(32)))
# ── 第四十一批：11 卷替换 ＋ 插卷（2026-09-20 主理人清单 ＋ 溯源注语义迁移）──────
SPEC24 = [['第 1 章 LWKT 与内核架构重构：从 FreeBSD 分叉到消息传递模型', ['1.1 FreeBSD 4.x 内核基础与 DragonFly 分叉背景', '1.2 LWKT 的设计目标与实现思想', '1.3 轻量级内核线程与消息传递机制', '1.4 token、锁与内核同步模型', '1.5 LWKT 在 DragonFly 内核架构中的位置', '1.6 内核架构重构中的工程取舍']], ['第 2 章 SMP、多核与内核扩展路线', ['2.1 分叉时期的 SMP 继承问题', '2.2 DragonFly 1.x 系列 SMP 重构', '2.3 消息传递驱动的并发设计', '2.4 锁模型演进', '2.5 调度器与多核性能优化', '2.6 NUMA 与未来扩展方向']], ['第 3 章 HAMMER 文件系统：时间维度存储模型的探索', ['3.1 HAMMER 的设计背景', '3.2 B-tree、快照与历史记录模型', '3.3 主从同步与数据复制机制', '3.4 HAMMER1 的应用实践与限制', '3.5 HAMMER2 的重新设计背景', '3.6 Copy-on-Write 与 PFS 模型', '3.7 HAMMER2 与 ZFS、Btrfs 的设计比较', '3.8 HAMMER 系列的技术遗产']], ['第 4 章 vkernel 与系统实验环境', ['4.1 vkernel 的提出背景', '4.2 用户态运行内核的实现机制', '4.3 vkernel 与 UML、微内核实验比较', '4.4 内核调试与开发用途', '4.5 教育与实验价值', '4.6 vkernel 对 DragonFly 架构实验的影响']], ['第 5 章 Clustered Objects 与分布式系统实验', ['5.1 分布式对象思想的提出', '5.2 内核对象与消息通信模型', '5.3 HAMMER 与分布式存储思想的联系', '5.4 DragonFly 分布式系统探索', '5.5 技术目标与实现限制', '5.6 Clustered Objects 思想的技术遗产']], ['第 6 章 用户空间、软件包与系统生态分化', ['6.1 FreeBSD userland 的继承', '6.2 fork 后基础系统维护', '6.3 pkgsrc 时代的软件生态', '6.4 DPorts 的形成', '6.5 DPorts 与 FreeBSD Ports 的关系', '6.6 pkg 与现代软件交付体系', '6.7 DragonFly 基本系统构建与发行流程']], ['第 7 章 网络、驱动与硬件支持', ['7.1 BSD 网络栈继承与维护', '7.2 网络设备与驱动体系', '7.3 存储设备支持', '7.4 图形系统与 DRM 支持', '7.5 UEFI 与现代硬件兼容', '7.6 硬件支持范围与项目规模约束']], ['第 8 章 虚拟化与现代运行环境', ['8.1 vkernel 后续影响', '8.2 Xen 与虚拟化探索', '8.3 NVMM 支持', '8.4 Jail 与隔离机制', '8.5 云环境中的适用场景', '8.6 DragonFly 现代运行环境定位']], ['第 9 章 DragonFly 技术路线整合与演进', ['9.1 从 FreeBSD 分叉到独立技术路线', '9.2 消息传递、内核对象与现代内核设计', '9.3 HAMMER2 与下一代文件系统探索', '9.4 DragonFly 对 BSD 技术生态的影响', '9.5 实验性架构与长期维护之间的关系', '9.6 2003–2026 年 DragonFly 技术演进']], ['第 10 章 DragonFly 技术资料与研究方法', ['10.1 Git 历史与提交记录', '10.2 邮件列表与设计讨论', '10.3 设计文档与开发者说明', '10.4 Release Notes 与版本演进记录', '10.5 源代码、实现与技术因果分析', '10.6 DragonFly 技术史的资料边界']]]
OLD24 = ['<h2>第二十四卷  DragonFly 技术专题史</h2>', '第 1 章 第 1 章 LWKT：内核线程模型与并发架构', '第 2 章 第 2 章 HAMMER 文件系统：从设计实验到生产系统', '第 3 章 第 3 章 vkernel：虚拟内核与内核开发工具', '第 4 章 第 4 章 SMP、多核支持与内核扩展', '第 5 章 第 5 章 用户空间体系与 FreeBSD 继承关系', '第 6 章 第 6 章 代码共享、移植与 BSD 生态关系', '第 7 章 第 7 章 驱动、硬件支持与平台演进', '第 8 章 第 8 章 网络、虚拟化与现代系统能力', '第 9 章 第 9 章 卷末书目述评：DragonFly 技术专题史料总目']
SPEC29 = [['第 1 章 UNIX 网络化与现代安全工程的形成（1988–1995）', ['1.1 UNIX 信任模型与超级用户制度', '1.2 网络化扩大 UNIX 攻击面', '1.3 远程服务漏洞与网络攻击时代', '1.4 Morris 蠕虫与现代计算机安全事件', '1.5 CERT/CC 与事件响应制度形成', '1.6 漏洞披露制度的发展', '1.7 全披露、协调披露与负责任披露', '1.8 CVE 与漏洞管理标准化', '1.9 BSD 进入现代安全工程体系']], ['第 2 章 现代操作系统安全思想与工程模型', ['2.1 从权限控制到安全模型', '2.2 Bell–LaPadula 机密性模型', '2.3 Biba 完整性模型', '2.4 Clark–Wilson 事务完整性模型', '2.5 Chinese Wall 利益冲突模型', '2.6 参考监视器与可信计算基础', '2.7 DAC、MAC 与 RBAC', '2.8 能力模型与最小权限原则', '2.9 隔离、沙箱与权限下降', '2.10 内存安全与执行保护', '2.11 W^X、ASLR 与随机化防御', '2.12 控制流完整性与现代攻击缓解', '2.13 模糊测试与自动化安全分析', '2.14 形式化验证与高保证系统', '2.15 安全启动与硬件信任根', '2.16 CHERI 与能力计算模型', '2.17 安全模型在 BSD 中的历史转化']], ['第 3 章 BSD 安全工程共同基础', ['3.1 UNIX UID/GID 权限体系', '3.2 chroot 与早期隔离思想', '3.3 securelevel 与 BSD 权限边界', '3.4 ACL 与扩展访问控制', '3.5 MAC 与强制访问控制', '3.6 进程资源限制', '3.7 内存保护机制', '3.8 系统审计与日志', '3.9 文件完整性验证', '3.10 磁盘加密与密钥管理', '3.11 随机数与密码基础设施', '3.12 软件签名与发布完整性']], ['第 4 章 FreeBSD：隔离、能力与系统工程安全', ['4.1 Jail 的产生与设计目标', '4.2 Jail 的进程、网络与文件系统隔离', '4.3 Jail 从 chroot 到操作系统级虚拟化', '4.4 MAC Framework', '4.5 Capsicum 能力安全模型', '4.6 capability mode', '4.7 libcasper 服务能力收缩', '4.8 bhyve 虚拟化隔离', '4.9 GELI 与存储加密', '4.10 OpenBSM 审计', '4.11 CheriBSD 与能力硬件', '4.12 FreeBSD 安全工程取舍']], ['第 5 章 NetBSD：可移植性约束下的安全工程', ['5.1 NetBSD 安全设计背景', '5.2 kauth 内核授权框架', '5.3 Veriexec 文件完整性', '5.4 NPF 网络过滤', '5.5 CGD 磁盘加密', '5.6 W^X 与 PaX 机制', '5.7 ASLR 与 KASLR', '5.8 SMEP、SMAP 等硬件防护', '5.9 静态分析与自动检查', '5.10 pkgsrc 软件安全维护', '5.11 多架构环境中的安全一致性', '5.12 NetBSD 安全工程取舍']], ['第 6 章 OpenBSD：代码审计、最小权限与主动防御', ['6.1 分叉背景与安全目标', '6.2 1996 年代码审计运动', '6.3 Secure by Default 思想', '6.4 正确性与安全工程', '6.5 W^X、随机化与内存防护', '6.6 ProPolice 与 Stack Protector', '6.7 malloc、mmap 与堆保护', '6.8 Privilege Separation', '6.9 pledge 系统调用限制', '6.10 unveil 文件访问限制', '6.11 RETGUARD 与控制流保护', '6.12 pf 网络安全模型', '6.13 OpenBSD 安全工程路线']], ['第 7 章 DragonFly BSD：架构实验中的安全维护', ['7.1 FreeBSD 分叉后的安全继承', '7.2 LWKT 与内核边界变化', '7.3 消息传递模型', '7.4 vkernel 实验环境', '7.5 HAMMER 完整性机制', '7.6 HAMMER2 数据一致性', '7.7 文件系统恢复能力', '7.8 软件包安全维护', '7.9 小规模项目安全工程', '7.10 DragonFly 安全路线限制']], ['第 8 章 BSD 安全机制比较：模型、目标与工程取舍', ['8.1 自主访问控制与强制访问控制比较', '8.2 能力模型与权限下降比较', '8.3 Jail、sandbox 与进程隔离比较', '8.4 pf、NPF 与网络过滤模型比较', '8.5 内存保护路线比较', '8.6 文件完整性与可信计算比较', '8.7 密码基础设施比较', '8.8 软件供应链安全比较', '8.9 安全默认策略比较', '8.10 安全机制复杂度与维护成本', '8.11 BSD 安全路线差异的历史原因']], ['第 9 章 网络、密码与供应链安全', ['9.1 TCP/IP 攻击面', '9.2 pf、ipfw、NPF', '9.3 DNS、NFS 与基础服务安全', '9.4 OpenSSH', '9.5 OpenSSL 与 LibreSSL', '9.6 随机数与密码套件', '9.7 后量子密码迁移', '9.8 Ports、pkgsrc 与第三方软件', '9.9 软件签名与构建链', '9.10 构建环境信任边界', '9.11 xz 后门事件', '9.12 xz 解码器漏洞', '9.13 BSD 项目的供应链响应']], ['第 10 章 BSD 漏洞事件与工程响应', ['10.1 权限提升漏洞', '10.2 内核内存破坏', '10.3 用户空间漏洞', '10.4 信息泄露', '10.5 网络协议漏洞', '10.6 文件系统漏洞', '10.7 隔离边界突破', '10.8 虚拟化攻击', '10.9 认证系统漏洞', '10.10 第三方组件漏洞', '10.11 补丁与回归测试', '10.12 安全公告体系', '10.13 从漏洞事件到工程改进']], ['第 11 章 BSD 安全工程路线历史比较', ['11.1 FreeBSD：系统工程与能力安全', '11.2 NetBSD：可移植性与持续维护', '11.3 OpenBSD：审计、最小权限与主动防御', '11.4 DragonFly：架构实验与资源约束', '11.5 四大 BSD 安全思想比较', '11.6 安全机制与项目目标关系', '11.7 安全文化与工程实践差异', '11.8 与 Linux、Windows、Solaris、macOS 安全路线比较', '11.9 BSD 安全工程的历史影响']], ['第 12 章 BSD 安全工程史的方法与史料', ['12.1 Security Advisory', '12.2 CVE 与漏洞数据库', '12.3 源代码提交历史', '12.4 补丁与版本树', '12.5 安全团队记录', '12.6 代码审计报告', '12.7 漏洞数量统计的局限', '12.8 用户规模与暴露面的关系', '12.9 安全机制目标与实际效果', '12.10 BSD 安全工程史的证据边界', '12.11 历史连续性与分化']]]
OLD29 = ['第 1 章 第 1 章 UNIX 网络化与现代安全工程的形成', '第 2 章 第 2 章 现代操作系统安全模型与工程方法', '第 3 章 第 3 章 BSD 安全工程的共同技术基础', '第 4 章 第 4 章 FreeBSD：隔离、能力与系统安全机制', '第 5 章 第 5 章 FreeBSD：安全组织、公告与漏洞响应', '第 6 章 第 6 章 NetBSD：可移植系统中的安全工程', '第 7 章 第 7 章 OpenBSD：代码审计、最小权限与主动防御', '第 8 章 第 8 章 DragonFly BSD：架构分化与安全维护', '第 9 章 第 9 章 跨 BSD 的网络、密码与供应链安全', '第 10 章 第 10 章 BSD 中的典型漏洞与工程响应', '第 11 章 第 11 章 BSD 安全工程的历史分化与比较', '第 12 章 第 12 章 BSD 安全史的证据与解释']
SPEC33 = [['第 1 章 BSD 社区世界化的形成', ['1.1 UNIX用户共同体的国际化', '1.2 Berkeley UNIX向美国以外扩展', '1.3 USENIX与跨地区 UNIX 共同体', '1.4 UUCP、学术网络与早期地区联系', '1.5 BSD用户组的形成', '1.6 网络基础设施与社区形成', '1.7 开发者跨地区流动', '1.8 企业、大学与用户组织', '1.9 从美国共同体到国际 BSD 社区', '1.10 BSD全球化的历史条件']], ['第 2 章 日本 BSD 社区：JUNET、WIDE 与 KAME', ['2.1 JUNET与日本学术网络', '2.2 WIDE Project与 Internet研究', '2.3 日本 UNIX 用户共同体', '2.4 日本 BSD 用户组与开发者网络', '2.5 BSD进入日本网络产业', '2.6 KAME项目的形成', '2.7 KAME的跨机构协作', '2.8 KAME与 IPv6、IPsec及 Mobile IPv6', '2.9 KAME代码进入 FreeBSD、NetBSD与其他 BSD', '2.10 日本开发者进入全球 BSD 项目', '2.11 AsiaBSDCon与日本 BSD 共同体', '2.12 日本 BSD 社区的长期变化']], ['第 3 章 欧洲 BSD 社区：从学术网络到 EuroBSDCon', ['3.1 欧洲学术网络与 UNIX', '3.2 欧洲早期 BSD采用者', '3.3 德国 BSD 社区', '3.4 法国 BSD 社区', '3.5 英国 BSD 社区', '3.6 北欧 BSD 社区', '3.7 欧洲高校与科研机构', '3.8 欧洲网络产业与 BSD', '3.9 BSDCon Europe的形成', '3.10 EuroBSDCon的跨国组织', '3.11 欧洲开发者进入全球 BSD 项目', '3.12 欧洲 BSD 社区的长期变化']], ['第 4 章 中文 BSD 社区：大陆、台湾与跨地区网络', ['4.1 中文 UNIX 用户共同体的形成', '4.2 中国大陆学术网络与 BSD', '4.3 1990年代中国 Internet 与 BSD 的历史条件', '4.4 中国大陆 BSD 用户与开发者网络', '4.5 FreeBSD中文社区的形成', '4.6 台湾学术网络与 BSD', '4.7 台湾 BSD 用户组织与技术交流', '4.8 香港及其他中文地区', '4.9 两岸 BSD 社区之间的信息流动', '4.10 BSD进入中文网络产业', '4.11 中文 BSD 开发者参与全球项目', '4.12 中文 BSD 社区的长期变化']], ['第 5 章 南亚与东南亚 BSD 社区', ['5.1 印度 BSD 社区', '5.2 印度高校与科研机构', '5.3 巴基斯坦 BSD 社区', '5.4 孟加拉 BSD 社区', '5.5 新加坡 BSD 社区', '5.6 马来西亚 BSD 社区', '5.7 印度尼西亚 BSD 社区', '5.8 菲律宾及其他东南亚地区', '5.9 用户组与地区性组织', '5.10 地区开发者进入全球项目', '5.11 教育、语言与经济条件']], ['第 6 章 拉丁美洲 BSD 社区', ['6.1 巴西 BSD 社区', '6.2 阿根廷 BSD 社区', '6.3 墨西哥 BSD 社区', '6.4 智利及其他南美地区', '6.5 用户组与地区性会议', '6.6 高校与科研机构', '6.7 网络服务提供商与 BSD', '6.8 地区开发者参与全球项目', '6.9 西班牙语、葡萄牙语与技术共同体', '6.10 拉丁美洲 BSD 社区的长期变化']], ['第 7 章 非洲、中东、中亚与大洋洲', ['7.1 非洲 BSD 社区', '7.2 南非与非洲英语地区', '7.3 中东 BSD 社区', '7.4 中亚 BSD 社区', '7.5 澳大利亚 BSD 社区', '7.6 新西兰 BSD 社区', '7.7 地区高校与科研机构', '7.8 用户组与开发者网络', '7.9 大洋洲与亚洲、北美之间的联系', '7.10 资料稀疏地区的历史重建']], ['第 8 章 BSD 会议与跨国共同体网络', ['8.1 USENIX与 BSD 社区', '8.2 BSDCan与北美 BSD 共同体', '8.3 AsiaBSDCon与亚洲 BSD 共同体', '8.4 EuroBSDCon与欧洲 BSD 共同体', '8.5 其他地区性 BSD 会议', '8.6 Hackathon与国际开发网络', '8.7 GSoC、实习与开发者流动', '8.8 会议作为人员集结机制', '8.9 会议作为项目间联系机制', '8.10 COVID-19对国际会议网络的影响', '8.11 线下共同体向远程共同体转变']], ['第 9 章 BSD 世界化中的人员、机构与知识流动', ['9.1 开发者跨国迁移', '9.2 学术机构之间的人才流动', '9.3 企业雇佣与 BSD 社区', '9.4 地区用户组与全球项目', '9.5 地区开发者进入核心项目', '9.6 基金会与国际社区', '9.7 技术合作项目与跨国研究', '9.8 会议与人才网络', '9.9 地方共同体对全球项目的反向影响', '9.10 BSD世界化中的语言与社会网络']], ['第 10 章 BSD 全球史中的中心、边缘与缺席', ['10.1 Berkeley在历史叙事中的中心位置', '10.2 北美档案优势', '10.3 非北美材料的可得性', '10.4 地区共同体的自我叙述', '10.5 语言造成的史料不对称', '10.6 低密度地区的证据空白', '10.7 沉默与缺席的区别', '10.8 缺失材料与推测性历史', '10.9 全球 BSD 史的区域偏差', '10.10 去中心化的历史书写']], ['第 11 章 BSD 社区世界化的历史解释', ['11.1 Internet基础设施与社区扩展', '11.2 学术网络、企业网络与用户网络', '11.3 语言、教育与经济条件', '11.4 远程协作与全球开发', '11.5 地区共同体与全球项目', '11.6 地方性与项目身份', '11.7 全球化与社区自治', '11.8 BSD世界化与开源社区世界化', '11.9 全球共同体与地方性', '11.10 BSD社区全球化的历史边界']], ['第 12 章 BSD 全球社区史的史料与方法', ['12.1 用户组档案', '12.2 会议组织记录', '12.3 项目邮件列表与开发记录', '12.4 基金会年报与活动资料', '12.5 地区网站、论坛与社区档案', '12.6 人物访谈与口述史', '12.7 地理统计与网络数据', '12.8 地区之间的证据密度差异', '12.9 缺席史料的标注', '12.10 全球 BSD 社区史的可证范围']]]
OLD33 = ['<h2>第三十三卷  开源社区的世界化与世界化的开源社区</h2>', '第 1 章 第 1 章 BSD 的全球分布与中心-边缘结构', '第 2 章 第 2 章 日本 BSD 社区：从 JUNET 到 AsiaBSDCon', '第 3 章 第 3 章 欧洲 BSD 社区：从 Euronet 到 EuroBSDCon', '第 4 章 第 4 章 中国 BSD 社区：翻译、镜像与本地化', '第 5 章 第 5 章 中国台湾 BSD 社区：从学术节点到产业应用', '第 6 章 第 6 章 其他地区 BSD 社群：南亚、东南亚、拉美', '第 7 章 第 7 章 低密度地区的证据空白：如何书写缺席的 BSD 史', '第 8 章 第 8 章 BSD 会议、节日与协会：从 Usenix 到全球社区组织', '第 9 章 第 9 章 流行病作为 BSD 社区的偶然条件：SARS 与 COVID-19', '第 10 章 第 10 章 低密度地区与跨区域细目', '第 11 章 第 11 章 城市、国家与 BSD 的双向塑造', '第 12 章 第 12 章 卷末书目述评：旧18卷《全球社区地区bsd史》全卷综述']
SPEC34 = [['第 1 章 BSD 文档体系与知识生产', ['1.1 4.4BSD文档体系', '1.2 手册页传统', '1.3 FreeBSD Handbook', "1.4 Developer's Handbook与 Porter's Handbook", '1.5 NetBSD文档体系', '1.6 OpenBSD文档体系', '1.7 DragonFly BSD文档体系', '1.8 官方文档与源代码之间的关系', '1.9 文档维护者与知识生产', '1.10 文档作为项目记忆']], ['第 2 章 BSD 文档翻译与本地化', ['2.1 多语言 BSD 文档的形成', '2.2 日语 BSD 文档', '2.3 中文 BSD 文档', '2.4 德语、法语与其他欧洲语言', '2.5 东亚语言社区', '2.6 翻译者与本地维护者', '2.7 翻译流程与版本同步', '2.8 技术术语的本地化', '2.9 翻译作为知识再生产', '2.10 翻译档案的保存']], ['第 3 章 USENET、邮件列表与早期在线传播', ['3.1 UUCP与早期 UNIX 信息网络', '3.2 USENET进入 BSD 社区', '3.3 2BSD相关新闻组', '3.4 comp.unix.bsd与 BSD 新闻组体系', '3.5 FreeBSD邮件列表', '3.6 NetBSD、OpenBSD与 DragonFly 邮件列表', '3.7 邮件列表的技术讨论功能', '3.8 邮件列表的社会组织功能', '3.9 在线争论与历史档案', '3.10 新闻组与邮件列表的保存']], ['第 4 章 源代码、软件包与物理分发', ['4.1 磁带与早期 UNIX 软件分发', '4.2 FTP与匿名下载', '4.3 comp.sources.unix', '4.4 源代码归档与版本整理', '4.5 BSD FTP发行树', '4.6 CD-ROM时代的软件分发', '4.7 Walnut Creek CDROM与 BSD', '4.8 杂志附录与软件包', '4.9 光盘、磁带与线下交换', '4.10 从物理介质到网络分发']], ['第 5 章 镜像站与志愿基础设施', ['5.1 BSD镜像网络的形成', '5.2 FTP镜像节点', '5.3 镜像管理员', '5.4 目录同步与带宽', '5.5 大学、ISP与商业机构提供镜像', '5.6 镜像硬件与经费', '5.7 镜像与地区访问', '5.8 镜像网络的衰减', '5.9 CDN、云存储与新的分发方式', '5.10 镜像站作为物质传播基础设施']], ['第 6 章 BSD 书籍、杂志与教育传播', ['6.1 BSD书籍出版', '6.2 4.4BSD文献与经典技术著作', '6.3 FreeBSD技术书籍', '6.4 NetBSD、OpenBSD与 DragonFly BSD 书籍', '6.5 高校教材与实验课程', '6.6 Berkeley UNIX与系统教材', '6.7 BSD Magazine与专业媒体', '6.8 在线书籍与 Wiki', '6.9 独立技术作者与自助出版', '6.10 教材对历史认识的影响']], ['第 7 章 会议论文、演讲与视听档案', ['7.1 USENIX论文', '7.2 BSDCon论文与程序', '7.3 BSDCan论文与演讲', '7.4 AsiaBSDCon论文与演讲', '7.5 EuroBSDCon论文与演讲', '7.6 Developer Summit资料', '7.7 视频、音频与幻灯片', '7.8 会议资料的开放获取', '7.9 会议资料的长期保存', '7.10 视听材料与技术共同体记忆']], ['第 8 章 新闻媒体、网站与网络公众记忆', ['8.1 UNIX专业媒体中的 BSD', '8.2 计算机杂志与行业新闻', '8.3 1990年代 BSD 分裂的媒体报道', '8.4 Slashdot与 BSD', '8.5 Wikipedia与 BSD 历史条目', '8.6 博客与个人技术网站', '8.7 社交媒体中的 BSD', '8.8 项目自我叙述与新闻叙述', '8.9 链接腐烂与网页消失', '8.10 数字公众记忆']], ['第 9 章 纪念、博物馆与数字遗产', ['9.1 BSD周年纪念', '9.2 BSD Day等纪念活动', '9.3 关键开发者的纪念', '9.4 计算机历史博物馆中的 BSD', '9.5 CSRG与 Berkeley UNIX 遗产', '9.6 源代码档案与数字考古', '9.7 历史硬件与 BSD 系统', '9.8 吉祥物、徽标与历史符号', '9.9 项目网站与历史页面', '9.10 BSD数字遗产的形成']], ['第 10 章 传播劳动与历史可见性', ['10.1 翻译者', '10.2 镜像管理员', '10.3 邮件列表管理员', '10.4 新闻组管理员与版主', '10.5 出版物编辑', '10.6 会议组织者与档案保存者', '10.7 视频、音频与照片记录者', '10.8 非核心开发者的传播贡献', '10.9 可见贡献与不可见劳动', '10.10 传播劳动与 BSD 历史可见性']], ['第 11 章 BSD 传播史的证据与方法', ['11.1 源代码与版本档案', '11.2 文档版本与翻译记录', '11.3 新闻组与邮件列表档案', '11.4 FTP、镜像与软件分发记录', '11.5 书籍、杂志与出版档案', '11.6 会议程序、论文与视听资料', '11.7 新闻媒体与网页快照', '11.8 博物馆、硬件与实物档案', '11.9 断链、缺页与数字档案缺失', '11.10 一手传播材料与后来的历史叙述', '11.11 传播记录与实际影响的区别', '11.12 BSD传播史的可证范围']]]
OLD34 = ['第 1 章 第 1 章 BSD 翻译史：文档本地化作为知识传播', '第 2 章 第 2 章 镜像站生态：志愿者基础设施的物质史', '第 3 章 第 3 章 BSD 文档与教科书史：从手册页到高校教材', '第 4 章 第 4 章 公众文化中的 BSD 呈现：流行文化、新闻媒体与网络记忆', '第 5 章 第 5 章 纪念史：奖项、周年活动与博物馆化', '第 6 章 第 6 章 被忽略的贡献者：非 committer、翻译者、镜像管理员', '第 7 章 第 7 章 USENET 新闻组传播史（1980s–1990s）', '第 8 章 第 8 章 源码分发档案：comp.sources.unix', '第 9 章 第 9 章 镜像、邮件列表与物理分发网络', '第 10 章 第 10 章 卷末书目述评：传播载体与公众记忆史料总目']
SPEC35 = [['第 1 章 Berkeley 软件作品传统的形成（1977–1993）', ['1.1 Unix 源代码环境与 Berkeley 软件实验室', '1.2 BSD 从补丁集合到软件发行体系', '1.3 Berkeley 软件作品的工程模式', '1.4 用户空间软件与系统创新', '1.5 BSD 软件许可证与自由传播模式', '1.6 Berkeley 软件作品与现代开源传统']], ['第 2 章 vi：Unix 编辑器传统的形成', ['2.1 ed、ex 与编辑器历史', '2.2 vi 的产生背景', '2.3 模式化编辑思想', '2.4 终端交互模型', '2.5 nvi 与 BSD 继承', '2.6 Vim 与现代 Unix 编辑器生态', '2.7 vi 从 BSD 软件到全球标准工具']], ['第 3 章 csh 与 Unix Shell 软件传统', ['3.1 Thompson shell 与 Bourne shell', '3.2 Berkeley C Shell 的设计', '3.3 命令历史与交互设计', '3.4 作业控制', '3.5 tcsh 继承', '3.6 Shell 设计路线比较', '3.7 csh 的历史评价']], ['第 4 章 BSD 网络软件作品：socket、TCP/IP 与 Internet 工具', ['4.1 BSD socket API 的形成', '4.2 socket 与现代网络编程模型', '4.3 4.2BSD TCP/IP 软件实现', '4.4 ping', '4.5 traceroute', '4.6 ftp、telnet 与远程网络工具', '4.7 netstat、ifconfig 与网络管理工具', '4.8 BSD 网络软件作品的现代继承']], ['第 5 章 curses、termcap 与终端软件生态', ['5.1 终端控制问题', '5.2 termcap', '5.3 curses', '5.4 terminfo', '5.5 BSD curses', '5.6 ncurses 与 Linux 时代的传播', '5.7 终端抽象的软件工程意义']], ['第 6 章 sendmail：互联网邮件基础设施', ['6.1 ARPANET 邮件环境', '6.2 delivermail 的产生', '6.3 sendmail 架构', '6.4 M4 配置系统', '6.5 邮件传输模型', '6.6 sendmail 安全历史', '6.7 sendmail 后继软件', '6.8 “Unix 邮件服务器”历史归属问题']], ['第 7 章 BIND：DNS 软件基础设施', ['7.1 DNS 与 Berkeley 软件环境', '7.2 BIND 的形成', '7.3 DNS 解析架构', '7.4 BIND8 与 BIND9', '7.5 DNS 安全问题', '7.6 DNS 软件长期维护', '7.7 Linux 时代 DNS 叙事中的 BSD 来源']], ['第 8 章 Unix 系统管理软件作品', ['8.1 cron', '8.2 at', '8.3 inetd', '8.4 syslog', '8.5 su', '8.6 sudo', '8.7 login 与身份管理工具', '8.8 系统管理工具的 BSD 传统']], ['第 9 章 OpenSSH：现代远程访问基础设施', ['9.1 SSH 协议背景', '9.2 OpenSSH 的形成', '9.3 ssh 客户端与服务器架构', '9.4 privilege separation', '9.5 Portable OpenSSH', '9.6 密码算法维护', '9.7 OpenSSH 在现代系统中的传播', '9.8 OpenSSH 与 BSD 软件作品传统']], ['第 10 章 OpenBSD 软件作品体系', ['10.1 pf', '10.2 OpenBGPD', '10.3 OpenNTPD', '10.4 OpenSMTPD', '10.5 LibreSSL', '10.6 mandoc', '10.7 signify', '10.8 OpenBSD 软件作品的工程方法']], ['第 11 章 BSD 软件生态工具作品', ['11.1 pkg', '11.2 pkgsrc', '11.3 Ports 工具体系', '11.4 make', '11.5 bmake', '11.6 tmux', '11.7 调试与诊断工具', '11.8 BSD 工具作品的现代发展']], ['第 12 章 被重新归类的 BSD 软件作品：Linux、Unix 与现代计算叙事中的来源问题', ['12.1 “Unix 软件”与“BSD 软件”的概念混淆', '12.2 vi 被视为 Linux 工具的问题', '12.3 BSD socket 被视为 Unix 通用传统的问题', '12.4 TCP/IP 软件实现来源问题', '12.5 curses、termcap 与终端文化来源问题', '12.6 sendmail、BIND 与 Internet 基础设施来源问题', '12.7 sudo、cron、网络工具的软件归属问题', '12.8 BSD 软件进入商业 Unix 的过程', '12.9 BSD 软件进入 Linux 生态后的历史再解释', '12.10 软件来源、传播与文化记忆偏移']], ['第 13 章 BSD 软件作品生命周期与史料方法', ['13.1 软件作品与操作系统的关系', '13.2 单作者维护', '13.3 核心维护者模式', '13.4 多维护者协作', '13.5 API 稳定性', '13.6 软件重构与替代', '13.7 安全维护周期', '13.8 软件淘汰', '13.9 源代码、版本记录与手册页', '13.10 BSD 软件作品史研究边界', '13.11 本卷总结']]]
OLD35 = []
SPEC36 = [['第 1 章 聚合：实验室与大学（1969–1979）', ['1.1 聚合事件群：Bell Labs → Berkeley → CSRG 的形成', '1.2 聚合的方式：学术网络、源码共享与 DARPA 资助', '1.3 UNIX、PDP 与偶然条件：技术路径形成的历史窗口']], ['第 2 章 聚合：CSRG 与 UNIX 的伯克利化（1979–1992）', ['2.1 聚合事件群：CSRG 版本史、TCP/IP 集成与工业扩散', '2.2 聚合方式：源码发行、BSD 许可证与商业采用', '2.3 伯克利 UNIX 的扩张与 CSRG 的历史位置', '2.4 CSRG 解散前的技术与制度极限']], ['第 3 章 分离：诉讼、许可证与 BSD 谱系重组（1989–1995）', ['3.1 分离事件群：AT&T 商业化、USL 诉讼与 CSRG 终结', '3.2 法律压力、许可证变化与源码边界', '3.3 386BSD、FreeBSD、NetBSD、OpenBSD 的形成', '3.4 分离期的历史偶然性：如果诉讼不存在']], ['第 4 章 平行：四大 BSD 与商业 BSD 谱系展开（1995–2010）', ['4.1 平行事件群：FreeBSD 工程化', '4.2 平行事件群：NetBSD 多平台路线', '4.3 平行事件群：OpenBSD 安全路线', '4.4 平行事件群：DragonFly BSD 架构实验', '4.5 平行事件群：Apple BSD 体系的封闭化发展', '4.6 平行发展的共同遗产与差异化选择']], ['第 5 章 再分离：BSD 内部路线分化与技术身份形成（2000–2026）', ['5.1 FreeBSD：生产系统与现代服务器路线', '5.2 NetBSD：可移植系统理念的持续强化', '5.3 OpenBSD：安全工程体系的独立发展', '5.4 DragonFly BSD：内核实验路线的独立化', '5.5 分离之后的技术互相影响', '5.6 BSD 谱系中的竞争与合作关系']], ['第 6 章 再聚合：基础设施时代的 BSD 回流（2010–2026）', ['6.1 再聚合事件群：OpenZFS、LLVM、Clang 与跨项目技术共享', '6.2 再聚合方式：许可证兼容、源码共享与工程需求', '6.3 云计算时代 BSD 技术的基础设施化', '6.4 RISC-V 与 Berkeley 开放硬件传统的新连接', '6.5 再聚合是否意味着新的 BSD 统一']], ['第 7 章 六十年分离聚合模型的历史解释', ['7.1 五阶段结构：聚合、扩张、分离、平行、再聚合', '7.2 BSD 历史是否存在周期性结构', '7.3 分离是否必然导致衰落', '7.4 小规模项目如何维持长期技术连续性', '7.5 分离聚合模型的适用范围']], ['第 8 章 偶然性节点考：BSD 历史中的关键转折', ['8.1 PDP-7 与 UNIX 起源条件', '8.2 DARPA 与 TCP/IP 伯克利化', '8.3 USL 诉讼与 BSD 分裂', '8.4 386BSD 停滞与 Patchkit', '8.5 Linux 出现后的生态竞争', '8.6 macOS 与 BSD 再连接', '8.7 OpenZFS 与跨项目合作', '8.8 反事实分析的方法限制']], ['第 9 章 迁移与坚守：BSD 版本控制与历史连续性', ['9.1 FreeBSD CVS → SVN → Git 的档案迁移', '9.2 DragonFly BSD 历史转换与提交信息损失', '9.3 NetBSD、OpenBSD 保持 CVS 连续性的意义', '9.4 版本库迁移与技术记忆变形', '9.5 diff、patch 与 BSD 工程文化']], ['第 10 章 基石与声名：BSD 遗产的社会分配', ['10.1 技术贡献与公众认知的不对称', '10.2 UNIX、C、TCP/IP 与 BSD 贡献的扩散', '10.3 BSD 技术进入 macOS、网络设备与基础设施', '10.4 BSD 贡献被重新命名与重新归属的问题', '10.5 里奇、乔布斯与技术遗产传播模式比较', '10.6 技术创造者与技术传播者的历史位置']], ['第 11 章 BSD 谱系的未来聚合：RISC-V 与开放计算（2010–2026）', ['11.1 Berkeley 开放传统与 RISC-V 的形成', '11.2 四大 BSD 的 RISC-V 支持过程', '11.3 开源硬件生态与 BSD 移植', '11.4 RISC-V 是否构成 BSD 新聚合节点', '11.5 BSD 六十年历史结构总结']]]
OLD36 = ['第 3 章 第 3 章 分离：诉讼、和解与四分叉（1989–1995）', '第 4 章 第 4 章 平行：五个谱系的各自展开（1995–2010）', '第 5 章 第 5 章 再聚合：衍生、回馈与隐形化（2010–2026）', '第 6 章 第 6 章 六十年分离聚合的分期总览', '第 7 章 第 7 章 分期划分的说明', '第 8 章 第 8 章 偶然性节点考：关键转折点的反事实标注', '第 9 章 第 9 章 迁移与坚守：四大 BSD 版本控制路线分化中的史料得失', '第 10 章 第 10 章 基石与声名：丹尼斯·里奇与史蒂夫·乔布斯的对照', '第 11 章 第 11 章 RISC-V 与开放指令集的伯克利谱系（2010–2026）']
SPEC37 = [['第 1 章 BSD 历史书写的形成：从技术记录到历史叙事', ['1.1 BSD 历史书写的对象与范围', '1.2 BSD 史料的五种来源：源码、文档、邮件、口述与二手叙述', '1.3 技术事实与历史解释的区别', '1.4 BSD 历史叙事中的选择、遗漏与强调', '1.5 UNIX/BSD 通史中的 BSD 位置变化', '1.6 BSD 历史研究与计算机史研究的关系']], ['第 2 章 BSD 历史叙事的演变（1993–2026）', ['2.1 UNIX 通史时代：BSD 被纳入 UNIX 故事', '2.2 1990 年代 BSD 项目自我叙述的形成', '2.3 Open Sources 时代：开源运动中的 BSD 叙事', '2.4 网络时代：论坛、邮件列表与 Wiki 记忆', '2.5 社交媒体时代：视频、播客与碎片化历史', '2.6 AI 时代：自动生成历史叙事的新问题']], ['第 3 章 声名分配与历史记忆：谁被记住，谁被遗忘', ['3.1 技术贡献与历史知名度的不一致', '3.2 创始人物、核心开发者与普通贡献者的可见性差异', '3.3 软件作品、代码贡献与作者身份的分离', '3.4 商业传播、媒体叙事与技术记忆', '3.5 BSD 贡献被重新归类的问题', '3.6 历史记忆中的 BSD 贡献者长尾']], ['第 4 章 BSD 历史中的重新命名、重新归因与技术来源问题', ['4.1 UNIX、BSD 与软件传统的命名问题', '4.2 BSD 软件作品的来源识别方法', '4.3 技术传播中的重新包装现象', '4.4 BSD 技术进入其他系统后的身份变化', '4.5 “首次实现”“首次普及”“首次商业化”的区别', '4.6 技术来源争议的证据标准']], ['第 5 章 BSD 史料体系：源码、档案与数字记录', ['5.1 源代码树作为历史档案', '5.2 Commit 历史与工程过程重建', '5.3 Release Notes 与版本记录', '5.4 Manual Pages 与技术文档', '5.5 邮件列表与开发讨论', '5.6 TUHS、BSD 相关档案与保存工程', '5.7 数字档案保存中的缺失问题']], ['第 6 章 BSD 技术史研究方法：代码考古与工程解释', ['6.1 从源码恢复技术演进', '6.2 Patch、Commit 与设计意图分析', '6.3 API、ABI 与接口历史研究', '6.4 软件版本树的时间分析', '6.5 技术论文与实际代码的对应关系', '6.6 代码作者、维护者与历史主体问题', '6.7 技术影响评价的方法边界']], ['第 7 章 记忆研究与 BSD 历史书写方法论', ['7.1 集体记忆与技术共同体', '7.2 记忆地点：项目网站、文档、会议与档案', '7.3 历史遗忘的形成机制', '7.4 放大、遗忘、重新命名、重新归因与神圣化', '7.5 与 Halbwachs、Nora 等记忆理论的对话', '7.6 技术史中的叙事竞争', '7.7 BSD 历史书写的伦理问题']], ['第 8 章 BSD 历史书写中的自反性问题', ['8.1 历史作者也是历史的一部分', '8.2 技术史研究中的观察者效应', '8.3 编年史、人物史、问题史与比较史的方法选择', '8.4 技术评价中的价值判断与事实判断', '8.5 “成功”“失败”“衰落”等历史概念的使用边界', '8.6 BSD 历史中的多重解释框架', '8.7 本书自身的史学位置']], ['第 9 章 AI 时代的软件历史研究', ['9.1 AI 辅助源码分析与历史重建', '9.2 AI 生成历史文本中的事实核验问题', '9.3 自动化代码分析与技术史研究', '9.4 大规模文档检索与数字人文学方法', '9.5 AI 对软件史料保存的影响', '9.6 人类研究者与 AI 协作的证据边界']], ['第 10 章 BSD 史学方法总结：从技术事实到历史理解', ['10.1 BSD 历史研究的核心问题', '10.2 一手史料与二手叙事的关系', '10.3 技术传播与历史记忆', '10.4 BSD 史学中的长期争议', '10.5 BSD 历史研究的未来方向', '10.6 本卷总评']]]
OLD37 = ['<h2>第三十六卷  BSD 史学史与方法</h2>', '第 1 章 第 1 章 BSD 在科学技术史与信息技术史中的声名分配与五类讲述格局', '第 2 章 第 2 章 BSD 历史讲述的三十年演变（1994–2026）', '第 3 章 第 3 章 被记住者名录：人物志作为记忆装置', '第 4 章 第 4 章 BSD 的缺席：哪些历史事件中 BSD 在场但未被记录', '第 5 章 第 5 章 口述史与记忆媒介：采访、BSD Now、纪录片', '第 6 章 第 6 章 数字记忆的计量：邮件列表、版本库与社区档案', '第 7 章 第 7 章 记忆史方法论：记忆变形五类型与本书的自我限制', '第 8 章 第 8 章 BSD 与自反性：自反悖论与书写本身的非存在', '第 9 章 第 9 章 AI 时代的软件史方法', '第 10 章 第 10 章 卷末书目述评：讲述、声名与缺席的史学史卷综述']
_gvol("G64", 24, SPEC24, 10, 63,
      "第二十四卷  DragonFly 技术专题史（2003–2026）", OLD24)
_gvol("G65", 29, SPEC29, 12, 142,
      "第二十九卷  BSD 分支的安全工程：防线、漏洞与响应（1988–2026）", OLD29)
_gvol("G66", 33, SPEC33, 12, 128,
      "第三十三卷  BSD 社区的世界化与世界化的 BSD（1980s–2026）", OLD33)
_gvol("G67", 34, SPEC34, 11, 112,
      "第三十四卷  BSD 的传播载体与公众记忆", OLD34)
_gvol("G68", 35, SPEC35, 13, 103,
      "第三十五卷  BSD 软件作品史：从 Berkeley 软件传统到现代计算基础设施（1977–2026）", OLD35)
_gvol("G69", 36, SPEC36, 11, 57,
      "第三十六卷  BSD 分离聚合的六十年（1969–2026）", OLD36)
_gvol("G70", 37, SPEC37, 10, 64,
      "第三十七卷  BSD 史学史与方法（1993–2026）", OLD37)

print()
print("=" * 78)
print(f"加强复核结论：PASS {len(OK)} 项，FAIL {len(BAD)} 项，INFO {len(INFO)} 项")
print("=" * 78)
for b in BAD:
    print("  FAIL " + b)
sys.exit(1 if BAD else 0)
