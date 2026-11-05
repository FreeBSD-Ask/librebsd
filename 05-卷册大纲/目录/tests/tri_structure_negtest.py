# -*- coding: utf-8 -*-
"""结构判据负向自检（K／L／M／N／O／P／Q 各组，2026-09-27 立为常备门禁）。

用途：构造二十二种缺陷副本（含 2026-09-30 补入的 P 种「注文括注不配对」、2026-10-06 补入的
Q 种「可见标记泄漏」加粗与章题 @@ 两形态、2026-10-10 补入的 C 种「卷内重题」、
2026-10-12 补入的 Q 种第三形态「语言标记 ⟦⟧ 泄漏」），确认 `audit_index_structure.py --path` 能把它们判为 FAIL。
判据「存在」不等于判据「有效」——若无负向自检，判据因逻辑写错而恒判 PASS 无法察觉。
  O 标题计数概括式与集合名词（2026-09-27 追加）：卷／章题命中须 FAIL；节题与注文只 WARN；
    专名（四条款 BSD 等）豁免须生效（正控夹具）。
  P 注文括注配对（2026-09-30 追加，98 号文 §11.4 P0-1）：溯源注缺收尾「〕」须 FAIL。
    设立缘由＝66 条注文括注不配对曾长期静默（详见 98 号文 §八·甲-1）。
  K 三级结构：无章之卷／无节之章／章外孤立节行
  L 不设附录：章题以「附录」起首（O1）
  M OS 比较节位次：比较节后接非述评节（O1b）
  N 结构裁决（2026-09-27 追加，MAX 提案 v1.1 M-7＋补遗 N-e～N-i）：N-a2 层序反转／N-b1 缺卷导言／
     N-c 卷名超长／N-d 题文复合词半角连字符／N-e 年序回落／N-g 述评非末位／N-h 节数超载／N-i 未登记同题；
     N-f（节题长度）为**软限**，不自证「拦下」而自证「只 WARN 不阻断」

夹具副本置于 `script/_vol_adjust_20260927/negfix/`（按项目规则临时件不改动源文件、保留不清理）。

用法：python tests/tri_structure_negtest.py

2026-09-27 ykla 裁定：**节题长度阈值为软限制**（逾限只示 WARN、不判 FAIL）；长度计数
口径＝英语单词整体算 1 字。故 N-f 一条改为软限断言（须 WARN 且不得阻断）。
⚠ 夹具必须以 LF 写出（write_text 须显式指定 LF 换行）：Windows 默认 CRLF 会先被 A 组「含 CRLF」拦下，
   判据是否有效被掩盖——2026-09-27 实测 N 组夹具全组曾因此「假拦下」。
"""
import re
import subprocess
import sys
from pathlib import Path

# 路径一律由本件位置推导（2026-10-23 修：原写死 `d:\librebsd\...` 绝对路径）：
# parents[1] ＝ `05-卷册大纲/目录`（本件在 tests/ 内）；其 parents[1] ＝ 仓库根。
BASE = Path(__file__).resolve().parents[1]
REPO = BASE.parents[1]
SRC = BASE / "index.html"
AUDIT = REPO / "00-编纂规则与格式规范" / "01-规则" / "脚本与命令" / "audit_index_structure.py"
# 历史归档引用，勿改：夹具副本目录留在 script 归档区（README 第十二件注明“保留不清理”）。
OUT = Path(r"d:\librebsd\script\_vol_adjust_20260927\negfix")
OUT.mkdir(parents=True, exist_ok=True)

h = SRC.read_text(encoding="utf-8")
# P3-2 起正文含 <noscript> 静态目录（与正文同标，含节号/述评字面），
# 会让夹具的 re.search/h.index 先命中静态目录而非正文 → 剥掉静态目录，夹具以正文为真源。
h = re.sub(r'<noscript>.*?</noscript>', '', h, flags=re.S)


def run(path, tag, want_group):
    """跑门禁，返回（是否被拦下，该组行）。"""
    r = subprocess.run([sys.executable, str(AUDIT), "--path", str(path)],
                       capture_output=True, text=True, encoding="utf-8")
    out = (r.stdout or "") + (r.stderr or "")
    # 优先取本组 ❌ 明细行（N 组判据的命中原因在明细行内）；无则退回本组 INFO 行
    line = ([l for l in out.split("\n") if "\u274c" in l and want_group + " " in l]
            or [l for l in out.split("\n") if l.startswith(want_group + " ")])
    verdict = [l for l in out.split("\n") if l.startswith("总判定")]
    print(f"[{tag}] exit={r.returncode} | {line[0] if line else '(无 %s 行)' % want_group}")
    print(f"        {verdict[0] if verdict else '(无总判定行)'}")
    return r.returncode != 0, (line[0] if line else "")


def negative(pat, repl, name, count=1):
    new, n = re.subn(pat, repl, h, count=count, flags=re.S)
    assert n == count, f"{name}：源文本未匹配（n={n}）"
    p = OUT / f"_neg_{name}.html"
    p.write_text(new, encoding="utf-8", newline="\n")
    return p


# ── K 组 ──────────────────────────────────────────────────────────────
m2 = re.search(r'(<section class="doc-block" id="vol-2".*?)(<section class="doc-block" id="vol-3")',
               h, re.S)
vol2 = m2.group(1)

p1 = OUT / "_neg_k_nochapter.html"
p1.write_text(h[:m2.start(1)] + re.sub(r'<h3 class="chapter".*?</ul>', "", vol2, flags=re.S)
              + h[m2.end(1):], encoding="utf-8", newline="\n")

p2 = OUT / "_neg_k_nosection.html"
p2.write_text(h[:m2.start(1)]
              + re.sub(r'(<h3 class="chapter" id="vol-2-ch-1".*?<ul class="sections">).*?(</ul>)',
                       r"\1\2", vol2, count=1, flags=re.S)
              + h[m2.end(1):], encoding="utf-8", newline="\n")

p3 = OUT / "_neg_k_strayli.html"
p3.write_text(h[:m2.end(1)] + '<ul class="sections"><li>孤立节</li></ul>' + h[m2.end(1):],
              encoding="utf-8", newline="\n")

# ── L 组：章题以「附录」起首 ───────────────────────────────────────────
p4 = negative(r'(<h3 class="chapter" id="vol-1-ch-1">第 1 章 )', r"\1附录 A ", "l_appendix")

# ── M 组：比较节后接非述评节 ──────────────────────────────────────────
m_os = re.search(r'<li[^>]*><span class="sec-num">([\d.]+)</span>[^<]*'
                 r'(?:操作系统比较|OS 比较|同时期操作系统|同时代操作系统|同期操作系统)', h)
assert m_os, "M 组：源文本未找到 OS 比较节"
li_end = h.index("</li>", m_os.end()) + len("</li>")
p5 = OUT / "_neg_m_osorder.html"
p5.write_text(h[:li_end]
              + f'<li><span class="sec-num">{m_os.group(1)}</span> 负向自检插入节</li>'
              + h[li_end:], encoding="utf-8", newline="\n")

# ── C 组（2026-10-10 追加）：卷内重题 ────────────────────────────────────
#   第七件 C 组章题唯一性由「全局」改「卷内」（剥「第 N 章」前缀后按卷比对，与页面自检 dupTitles 同口径）。
#   夹具**动态**取卷 3 第 1 章现题面替换第 2 章题面 → 卷内（剥前缀）重题须被 C 组拦下；
#   禁写死题面，以抗历次题面改写（同 O 组锚点纪律）。
#   2026-10-14 修：章题可含 136 批语言标记 <span lang>（如卷 3 ch1），[^<]+ 会失配 → 非贪婪 (.+?) 容忍行内标签。
_ch1 = re.search(r'<h3 class="chapter" id="vol-3-ch-1">第 1 章 (.+?)</h3>', h)
_ch2 = re.search(r'<h3 class="chapter" id="vol-3-ch-2">第 2 章 (.+?)</h3>', h)
assert _ch1 and _ch2, "C 卷内重题夹具无法定位卷 3 第 1／2 章题"
p_cdup = OUT / "_neg_c_dup_in_vol.html"
p_cdup.write_text(h.replace(_ch2.group(0),
                            '<h3 class="chapter" id="vol-3-ch-2">第 2 章 ' + _ch1.group(1) + '</h3>', 1),
                  encoding="utf-8", newline="\n")


print("＝ 结构判据负向自检（K×3／L×1／M×1／C×1）＝")
cases = [
    (p1, "K 无章之卷", "K"),
    (p2, "K 无节之章", "K"),
    (p3, "K 章外孤立节行", "K"),
    (p4, "L 章题附录起首", "L"),
    (p5, "M 比较节位次", "M"),
    (p_cdup, "C 卷内重题", "C"),
]

# ── N 组（2026-09-27 追加）：四类结构裁决缺陷 ──────────────────────────────
# 关键：作缺陷副本必须命中「本组子判据」而不是被别的缺陷顺带拦下。
p6 = OUT / "n_a2_reverse.html"
h6 = h
# 层序反转：把综合总结层（关键词「会者定离」）与后设层（关键词「史学史」）的卷题互换
# → N-a2 应报「后设层先于综合总结层」。2026-10-23 改为按判据同一关键词动态定位，
# 不写死卷号／题面（现行 75 卷：综合总结卷 70、后设卷 73）。
m41 = re.search(r"<h2>(第[一二三四五六七八九十]+卷\s\s*[^<]*会者定离[^<]*)</h2>", h6)
m42 = re.search(r"<h2>(第[一二三四五六七八九十]+卷\s\s*[^<]*史学史[^<]*)</h2>", h6)
assert m41 and m42, "N-a2 夹具无法定位综合总结／后设层卷题"
h6 = h6.replace(m41.group(1), "@@T41@@").replace(m42.group(1), m41.group(1)).replace("@@T41@@", m42.group(1))
p6.write_text(h6, encoding="utf-8", newline="\n")

p7 = OUT / "n_b1_no_overview.html"
# 缺卷导言：删去任一卷的 vol-overview 段
m7 = re.search(r'<p class="vol-overview">.*?</p>\s*', h, re.S)
assert m7, "N-b1 夹具无法定位卷导言"
p7.write_text(h[:m7.start()] + h[m7.end():], encoding="utf-8", newline="\n")

p8 = OUT / "n_c_long_title.html"
# 超长卷名：把「UNIX 技术专题史」卷的卷题扩到 >36 字（保留原卷序号，不写死卷号）
old3 = re.search(r"<h2>(第[一二三四五六七八九十]+卷)\s\s*UNIX 技术专题史[^<]*</h2>", h)
assert old3, "N-c 夹具无法定位 UNIX 技术专题史卷题"
p8.write_text(h.replace(old3.group(0),
                        "<h2>%s  UNIX 技术专题史：内核、进程、文件系统、网络栈、存储、软件工程与工程文化的横向综览（1971–1989）</h2>"
                        % old3.group(1), 1),
              encoding="utf-8", newline="\n")

p9 = OUT / "n_d_half_hyphen.html"
# 半角连字符：把 BSD–Linux 改回 BSD-Linux（项目名复合词形）
assert "BSD–Linux" in h or "BSD–UNIX" in h, "N-d 夹具无法定位复合词"
p9.write_text(h.replace("BSD–Linux", "BSD-Linux", 1).replace("BSD–UNIX", "BSD-UNIX", 1), encoding="utf-8", newline="\n")

cases += [
    (p6, "N-a2 层序反转", "N-a2"),
    (p7, "N-b1 缺卷导言", "N-b1"),
    (p8, "N-c 卷名超长", "N-c"),
    (p9, "N-d 半角连字符", "N-d"),
]

# ── N-e～N-i（2026-09-27 补遗追加）：五种节级结构裁决缺陷 ────────────────────
# N-e 年序回落：把卷 5 ch1 1.5 的年份 1975–1976 改为 1970（早于 ch1 前节 1974）
p10 = OUT / 'n_e_year_regress.html'
assert 'Berkeley Pascal（1975–1976）' in h, 'N-e 夹具无法定位'
p10.write_text(h.replace('Berkeley Pascal（1975–1976）', 'Berkeley Pascal（1970–1976）', 1), encoding='utf-8', newline='\n')

# N-f 节题长度（**软限**，2026-09-27 ykla 裁定）：把卷 3 ch1 1.2 节题拉长到新计数口径下逾 60 字（不含注）。
#   该条**不在**「拦下」式 cases 内（软限不阻断），另以软限断言核验：须报 WARN 且门禁 exit 0。
p11 = OUT / "n_f_long_sec.html"
old_12 = "进程模型：fork、exec 与 wait"
new_12 = ("进程模型：fork、exec 与 wait 的完整机制考据及其在从 PDP-11 汇编实现到 C 语言重写过程中的演化差异与实现路径之详细分析"
          "，并与后续各版本逐条对照与复核记录")
p11.write_text(h.replace(old_12, new_12, 1), encoding="utf-8", newline="\n")

# N-g 述评节非末位：在「本章书目述评」节后插入一节
# 2026-10-09 修：原锚写死 `1\.7</span>\s*本章书目述评`，而补批 17 后**述评体例已整体迁出**
#   （`audit_index_structure.py` L157/L159：231 节＋19 章迁出、BIB_HAS 清空、全书改全正章制），
#   全库「本章书目述评」节＝0 → 夹具无从构造，脚本在 assert 处直接崩（第十二件 FAIL）。
#   判据 N-g 与 E／M 组同为「有则设、无则不设」的**条件判据**，故夹具同步条件化：
#   源文本无述评节时**显式 SKIP**（打印理由，不静默），一旦述评体例回归即自动恢复自证。
p12 = OUT / "n_g_biblio_not_last.html"
m_g = re.search(r'<span class="sec-num">[0-9.]+</span>\s*本章书目述评', h)
NG_ACTIVE = bool(m_g)
if NG_ACTIVE:
    ins = '<li><span class="sec-num">1.8</span> 负向自检插入节</li>'
    # 找到该 li 的 </li> 结束位置
    biblio_end = h.index("</li>", m_g.start()) + len("</li>")
    p12.write_text(h[:biblio_end] + ins + h[biblio_end:], encoding="utf-8", newline="\n")
else:
    print("[N-g] SKIP：源文本无「本章书目述评」节（述评体例已整体迁出、全书改全正章制）"
          "——判据成空转，夹具条件化跳过；述评体例回归即自动恢复自证")

# N-h 章内节数超载（>18 节）：向卷 3 ch1（7 节）复制节使其超过 18 节
p13 = OUT / "n_h_too_many_secs.html"
m_h = re.search(r'(<h3 class="chapter" id="vol-3-ch-1".*?</ul>)', h, re.S)
assert m_h, "N-h 夹具无法定位卷 3 ch1"
ch1_block = m_h.group(1)
extra = re.findall(r'<li[^>]*>.*?</li>', ch1_block, re.S)
adds = "".join(extra) + "".join(extra)
h13 = h[:m_h.end(1) - len("</ul>")] + adds + "</ul>" + h[m_h.end(1):]
p13.write_text(h13, encoding="utf-8", newline="\n")

# N-i 未登记同题：把 3 个分属不同卷的节题改为同一新题（≥12 字、不在 DUP_OK）
# → 使该题面命中 ≥3 章，触发 N-i FAIL 判据（两章只 WARN、三章才 FAIL）。
# 2026-10-05 修：锚点原写死「1.1」节号，而 macOS 卷重构后「NeXT 的创立与操作系统战略」
# 已自 1.1 移至 2.1 → 夹具静默失效（系既有失效，非本次引入）。改为**题面锚定、不锁节号**，
# 以抗历次重编号（同 O 组锚点纪律）。
p14 = OUT / "n_i_unregistered_dup.html"
h14 = h
_NI_TITLE = "跨章节系统测试基线的重复题面"
_NI_ANCHORS = ["NeXT 的创立与操作系统战略", "BSD UNIX 进入计算机工业", "伯克利软件研究与美国版权制度"]
for _a in _NI_ANCHORS:
    _m = re.search(r'(<span class="sec-num">[0-9.]+</span>\s*)' + re.escape(_a) + r'(</li>)', h14)
    assert _m, "N-i 夹具无法定位目标节：%s" % _a
    # 2026-09-30 修（98 号文 §11.4 P0-1 落地时发现）：原实现作
    #   `h14[:_m.start(2)] + _NI_TITLE + h14[_m.end(2):]`，而 group(2) 恰为 `</li>` 的跨度，
    #   于是**把 `</li>` 换成了题面**——li 未闭合、且三章题面各不相同（新题被追挂在原题之后），
    #   N-i 判据因此**从未被真正自证**（该夹具当时 exit=1 系被 G 组「li 未闭合」等其他判据拦下，
    #   属「被别的缺陷顺带拦下而误判判据有效」）。现改为**仅替换锚题面文本**、保留 `</li>`。
    _pre = _m.start(2) - len(_a)
    h14 = h14[:_pre] + _NI_TITLE + h14[_m.start(2):]
p14.write_text(h14, encoding="utf-8", newline="\n")

# ── O 组（2026-09-27 立）：标题计数概括式与集合名词 ────────────────────────
# O 硬：章题改计数概括式（「四大 BSD」）→ 须 FAIL（卷／章题为集合的定义层）
# 锚点改以**章题文本**定位（原锚 `id="vol-12-ch-5"` 在 105／107 两轮重编号后已不存在，
# 夹具静默失效；2026-10-04 108 号文施工时实测复现——系既有失效，非本次引入）。
# 以题面锚定可免于历次卷号重排再次崩坏。
p_o1 = OUT / "o_numerals_chapter.html"
# 2026-10-11 ★22 收口：锚题面随 A-22 并章（V2C1＋V4C11 并为「UNIX 软件工程」）更新——
# 原锚「软件工程：Research UNIX 时代的工程过程」已不存在（系既有失效，非 ★22 引入）。
m_o1 = re.search(
    r"(<h3 class=\"chapter\" id=\"vol-[0-9]+-ch-[0-9]+\">第 [0-9]+ 章 )"
    r"UNIX 软件工程(</h3>)", h)
assert m_o1, "O1 夹具无法定位「UNIX 软件工程」章题"
p_o1.write_text(h[:m_o1.start(1)] + m_o1.group(1) + "软件工程：四大 BSD 的工程过程" + m_o1.group(2) + h[m_o1.end(2):], encoding="utf-8", newline="\n")

# O 正控：专名「四条款 BSD」入节题 → 须**不** FAIL、亦不 WARN（豁免生效）
p_o2 = OUT / "o_exempt_clause.html"
m_o2 = re.search(r"(<li[^>]*><span class=\"sec-num\">2\.1</span> )[^<]*(</li>)", h)
assert m_o2, "O2 正控夹具无法定位卷 30 2.1 节题"
p_o2.write_text(h[:m_o2.start(1)] + m_o2.group(1) + "四条款 BSD 许可证的条款对照" + m_o2.group(2) + h[m_o2.end(2):], encoding="utf-8", newline="\n")

# O 软：节题改计数概括式（「三种路线」）→ 须只 WARN、不阻断
p_o3 = OUT / "o_soft_section.html"
m_o3 = re.search(r"(<li[^>]*><span class=\"sec-num\">1\.2</span> )[^<]*", h)
assert m_o3, "O3 夹具无法定位某章 1.2 节题"
m_o3_end = h.index("</li>", m_o3.end())
p_o3.write_text(h[:m_o3.start(1)] + m_o3.group(1) + "三种路线的对照" + h[m_o3_end:], encoding="utf-8", newline="\n")

# O 硬：章题改集合名词（「各分支」）→ 须 FAIL（集合名词不可用）
# 同上：原锚 `id="vol-29-ch-13"` 已随重编号失效，改以题面锚定。
p_o4 = OUT / "o_collective_chapter.html"
m_o4 = re.search(
    r"(<h3 class=\"chapter\" id=\"vol-[0-9]+-ch-[0-9]+\">第 [0-9]+ 章 )"
    r"BSD 安全工程史的方法与史料(</h3>)", h)
assert m_o4, "O4 夹具无法定位「BSD 安全工程史的方法与史料」章题"
p_o4.write_text(h[:m_o4.start(1)] + m_o4.group(1) + "各分支安全工程路线的历史比较" + m_o4.group(2) + h[m_o4.end(2):], encoding="utf-8", newline="\n")

# ── P 组（2026-09-30 追加）：注文括注不配对 ──────────────────────────────
#   典型形态：溯源注缺收尾「〕」。修复前全库 66 行此形（584 注的 11.3%），
#   在内容源与产物同数传播且无任何护栏（A 编码只查直角引号、G 组只查标签平衡）。
p_paren = negative(r'(〔[^〕]{6,60})〕</span>', r"\1</span>", "p_paren")

# ── Q 组（2026-10-06 追加）：正文可见标记泄漏 ──────────────────────────────
#   ①加粗 **：注入溯源注内（91 号文 §8.3 P0-1 同类缺陷两度复发，2026-10-06 复核再抓
#     5 行 6 处；A 编码／G 标签／P 括注均不覆盖）。
#   ②定界符 @@：注入章题（装配器 @@ 定界仅解析节行，章题行携带 @@〔…〕 会原样透传——
#     2026-10-06 复核抓出卷 49 ch9 章题一处、产物 3 面）。
p_qbold = negative(r'(〔溯源：[^〕]{6,60})〕</span>', r"\1**〕</span>", "q_bold")
m_qc = re.search(r'(<h3 class="chapter" id="vol-1-ch-1">[^<]*)(</h3>)', h)
assert m_qc, "Q 夹具无法定位卷 1 ch1 章题"
p_qch = OUT / "_neg_q_chapter_at.html"
p_qch.write_text(h[:m_qc.start(1)] + m_qc.group(1) + "@@〔分工·迁移：负向自检·章题注透传〕"
                 + m_qc.group(2) + h[m_qc.end(2):], encoding="utf-8", newline="\n")
#   ③语言标记 ⟦⟧（2026-10-12 追加，136 批）：⟦lang:文本⟧ 应在装配期被 esc()/plain()
#     消费、产物零出现；注入 ⟦ 与 ⟧ 字面（模拟装配未消费的泄漏）即须被 Q 拦下。
#     ⟦⟧ 以 chr() 构造，防本文件经工具链被规范化。
_LB, _RB = chr(0x27E6), chr(0x27E7)
p_qlang = OUT / "_neg_q_lang_mark.html"
p_qlang.write_text(h[:m_qc.start(1)] + m_qc.group(1) + _LB + "en:test" + _RB
                   + m_qc.group(2) + h[m_qc.end(2):], encoding="utf-8", newline="\n")
#   ④「谱系」残留（2026-10-08 追加，125 号文 阶段 F）：ykla 硬令「标题＋注文一并清理」，
#     全库禁用「谱系」二字。注入卷 1 ch1 章题文本，确认 Q2 判据能判为 FAIL。
p_q2 = OUT / "_neg_q2_puxi.html"
p_q2.write_text(h[:m_qc.start(1)] + m_qc.group(1) + "谱系" + m_qc.group(2) + h[m_qc.end(2):],
                encoding="utf-8", newline="\n")

# ── R 组（2026-10-06 追加，119d ★9）：卷头主体声明缺失 ─────────────────────
#   删除卷分工注中的〔主体声明〕定式标记（真值表＝02-操作手册/04-体例参照.md）。
#   2026-10-11 ★22 收口：原「仅删首个」在卷序重排后可能命中非真值表卷（新卷 3＝旧 66 共同体卷，
#   不属 R 真值表）致夹具静默失效（exit=0）；改为删除全部卷分工注之标记，任一 R 卷失标即拦下。
m_r = re.search(r'(<p class="vol-note">[^<]*?)(〔主体声明〕)', h)
assert m_r, "R 夹具无法定位〔主体声明〕"
p_r = OUT / "_neg_r_voldecl.html"
h_r = re.sub(r'(<p class="vol-note">[^<]*?)〔主体声明〕', r'\1', h)
assert h_r != h, "R 夹具未能删除〔主体声明〕"
p_r.write_text(h_r, encoding="utf-8", newline="\n")

# ── S 组（2026-11-06 追加，ADR-0020）：小节（第四级）四缺陷 ────────────────
#   动态锚定卷 2 ch1 节 1.1（M.N 锚恒定）；在其 </li> 前注入嵌套 ul.subsections。
#   四件分别命中：小节编号跳号／不归属父节／空小节题／F 组四级口径漂移。
_m_s = re.search(r'<li id="vol-2-ch-1-sec-1-1">.*?</li>', h, re.S)
assert _m_s, "S 组夹具无法定位 vol-2-ch-1-sec-1-1"
_s_li = _m_s.group(0)
_s_head = h[:_m_s.start()]
_s_tail = h[_m_s.end():]

# S-1 跳号：注入 1.1.1 与 1.1.3（缺 1.1.2）→ D 组 want 序列不匹配
p_s1 = OUT / "_neg_s_sub_gap.html"
p_s1.write_text(_s_head + _s_li.replace("</li>",
    '<ul class="subsections">'
    '<li id="vol-2-ch-1-sec-1-1-sub-1"><span class="sec-num">1.1.1</span> 小节甲</li>'
    '<li id="vol-2-ch-1-sec-1-1-sub-3"><span class="sec-num">1.1.3</span> 小节丙</li>'
    "</ul></li>", 1) + _s_tail, encoding="utf-8", newline="\n")

# S-2 归属破坏：小节号 1.2.1 挂在节 1.1 下
p_s2 = OUT / "_neg_s_sub_orphan.html"
p_s2.write_text(_s_head + _s_li.replace("</li>",
    '<ul class="subsections">'
    '<li id="vol-2-ch-1-sec-1-1-sub-1"><span class="sec-num">1.2.1</span> 小节甲</li>'
    "</ul></li>", 1) + _s_tail, encoding="utf-8", newline="\n")

# S-3 空小节题：编号后有且只有空白
p_s3 = OUT / "_neg_s_sub_empty.html"
p_s3.write_text(_s_head + _s_li.replace("</li>",
    '<ul class="subsections">'
    '<li id="vol-2-ch-1-sec-1-1-sub-1"><span class="sec-num">1.1.1</span> </li>'
    "</ul></li>", 1) + _s_tail, encoding="utf-8", newline="\n")

# S-4 F 组口径漂移：footer 四级串的小节数改 5（与实测 0 不符）
m_ft = re.search(r"现行大纲目录 · (\d+ 卷 \d+ 章 \d+ 节) 0 小节", h)
assert m_ft, "S-4 夹具无法定位 footer 四级口径串"
p_s4 = OUT / "_neg_s_quad_drift.html"
p_s4.write_text(h[:m_ft.start()] + m_ft.group(0).replace(" 0 小节", " 5 小节", 1)
                + h[m_ft.end():], encoding="utf-8", newline="\n")

cases += [
    (p10, "N-e 年序回落", "N-e"),
] + ([(p12, "N-g 述评非末位", "N-g")] if NG_ACTIVE else []) + [
    (p13, "N-h 节数超载", "N-h"),
    (p14, "N-i 未登记同题", "N-i"),
    (p_o1, "O 章题计数式", "O"),
    (p_o4, "O 章题集合名词", "O"),
    (p_paren, "P 括注不配对", "P"),
    (p_qbold, "Q 加粗泄漏", "Q"),
    (p_qch, "Q 章题注透传", "Q"),
    (p_qlang, "Q 语言标记泄漏", "Q"),
    (p_q2, "Q2 谱系残留", "Q2"),
    (p_r, "R 卷头主体声明缺失", "R"),
    (p_s1, "S 小节跳号", "D"),
    (p_s2, "S 小节归属", "D"),
    (p_s3, "S 小节空题", "D"),
    (p_s4, "S 口径漂移", "F"),
]

results = [run(p, tag, grp) for p, tag, grp in cases]

# N-f 软限断言（2026-09-27 ykla 裁定：节题长度阈值是**软限制**，逾限只示 WARN）：
#   须报 N-f WARN，且门禁 exit 0（不得判 FAIL、不得阻断）。夹具须 LF 写出，否则先被 A 组
#   「含 CRLF」拦下，本判据被掩盖——2026-09-27 实测该坑曾令 N 组全部夹具「假拦下」。
r_nf = subprocess.run([sys.executable, str(AUDIT), "--path", str(p11)],
                      capture_output=True, text=True, encoding="utf-8")
o_nf = (r_nf.stdout or "") + (r_nf.stderr or "")
nf_warn = [l for l in o_nf.split("\n") if "N-f" in l and "WARN" in l]
nf_fail = [l for l in o_nf.split("\n") if "❌" in l and "N-f" in l]
nf_soft_ok = (r_nf.returncode == 0 and bool(nf_warn) and not nf_fail)   # 须报 WARN、不得判 FAIL、不得阻断

# O 组软硬断言（2026-09-27 立）：①专名正控既不 FAIL 也不 WARN；②节题软示只 WARN 且 exit 0。
def _run_raw(path):
    r = subprocess.run([sys.executable, str(AUDIT), "--path", str(path)],
                       capture_output=True, text=True, encoding="utf-8")
    return r.returncode, (r.stdout or "") + (r.stderr or "")

rc_o2, out_o2 = _run_raw(p_o2)
# 2026-09-30 修（98 号文 §11.4 P0-1 落地时发现）：原断言 `out_o2.count("⚠ O ") == 0` 统计的是
#   输出中**全部** O 软示行，而基线页本身就有 2 处节题／注文软示（见第七件 O 行）→ 该断言恒为 False，
#   第十二件因此长期 FAIL。改为**只断言注入题面本身未被示警**（判据精确化，免受基线软示干扰）。
o2_ok = (rc_o2 == 0 and out_o2.count("❌ O ") == 0 and "四条款 BSD" not in out_o2)
print("[O 专名正控] exit=%d | FAIL 明细 %d ／WARN 明细 %d（断言只看注入题面「四条款 BSD」是否被示警）"
      % (rc_o2, out_o2.count("❌ O "), out_o2.count("⚠ O ")))
rc_o3, out_o3 = _run_raw(p_o3)
# 同理精确化：须**由注入题面「三种路线」**触发 WARN，且不得判 FAIL、不得阻断。
o3_ok = (rc_o3 == 0 and "三种路线" in out_o3 and out_o3.count("❌ O ") == 0)
print("[O 节题软示] exit=%d | FAIL 明细 %d ／WARN 明细 %d（断言看注入题面「三种路线」须命中 WARN）"
      % (rc_o3, out_o3.count("❌ O "), out_o3.count("⚠ O ")))
print("[N-f 软限] exit=%d | WARN %d 条／FAIL 明细 %d 条 | %s"
      % (r_nf.returncode, len(nf_warn), len(nf_fail), nf_warn[0].strip() if nf_warn else "(无 N-f WARN 行)"))

# 2026-09-30（98 号文 §11.4 P0-1 落地时发现并修复）两处**夹具自身失效**，均属「判据看起来被自证、
# 实为被别的缺陷顺带拦下」的典型，值得永久留痕：
#   ① **N-i 夹具构造有误**：原 `h14[:_m.start(2)] + _NI_TITLE + h14[_m.end(2):]` 中 group(2) 恰为
#      `</li>` 的跨度，等于**把 `</li>` 换成题面** → li 未闭合、三章题面各不相同，N-i 判据**从未被真正自证**
#      （当时该夹具 exit=1 系被 G 组「li 未闭合」拦下）。已改为仅替换锚题面文本。
#   ② **O 正控断言恒 False**：原 `out_o2.count("⚠ O ") == 0` 统计输出中**全部** O 软示行，而基线页自身
#      就有 2 处节题／注文软示 → 第十二件长期 FAIL。已改为只断言**注入题面本身**未被示警。
# 教训：**负向自检须同时断言「拦下原因正是本组判据」**（本文件 targets 字典即为此设），
#      且**不得以输出中的全局计数代替对注入项的定向断言**。
HARD_IDX = list(range(len(cases)))   # 2026-09-30：P 组已纳入；N-i 夹具修复后真复现（先前为假复现）
ok = all(results[k][0] for k in HARD_IDX) and nf_soft_ok and o2_ok and o3_ok
# 逐组确认「拦下原因正是本组判据」（避免被其他组缺陷顺带拦下而误判判据有效）
targets = {"K 无章之卷": "无章之卷 1", "K 无节之章": "无节之章 1",
           "K 章外孤立节行": "孤立节行 1", "L 章题附录起首": "命中 1 处",
           "M 比较节位次": "违规 1 处",
           "C 卷内重题": "卷内重题 1",
           "N-a2 层序反转": "N-a2 后设层",
           "N-b1 缺卷导言": "N-b1 缺卷导言",
           "N-c 卷名超长": "N-c 卷名超 36 字",
           "N-d 半角连字符": "N-d 题文复合词用半角连字符",
           "N-e 年序回落": "N-e 年序回落",
           "N-g 述评非末位": "N-g",
           "N-h 节数超载": "N-h",
           "O 章题计数式": "O 章题计数概括式",
           "O 章题集合名词": "O 章题计数概括式",
           "P 括注不配对": "P 注文括注不配对",
           "Q 加粗泄漏": "Q 可见标记泄漏",
           "Q 章题注透传": "Q 可见标记泄漏",
           "Q 语言标记泄漏": "Q 可见标记泄漏",
           "Q2 谱系残留": "Q2 谱系残留",
           "R 卷头主体声明缺失": "R 卷头缺〔主体声明〕",
           "S 小节跳号": "小节 ['1.1.1', '1.1.3']",
           "S 小节归属": "小节 ['1.2.1'] != ['1.1.1']",
           "S 小节空题": "空小节题 1.1.1",
           "S 口径漂移": "F 口径六处: FAIL",
           }
precise = all(targets[cases[k][1]] in results[k][1] for k in HARD_IDX if cases[k][1] in targets)

print()
print("负向自检结论：" + ("PASS（二十二种缺陷被对应判据拦下＋N-f／O 两组软限只示 WARN 不阻断）"
                     if (ok and precise) else "FAIL（有缺陷未被拦下或非本组判据命中）"))
if len(results) > 12:
    pass  # （2026-09-29：N-e/N-g/N-h/N-i 均已复现；N-i 已纳入断言）
sys.exit(0 if (ok and precise) else 1)
