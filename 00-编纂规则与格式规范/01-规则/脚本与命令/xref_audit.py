# -*- coding: utf-8 -*-
# 交叉引用悬空审计 v6（2026-10-03 第六批：增设「冻结基准语境豁免」判据＋负向夹具）
#
# v4 只覆盖单一形制「第X卷第M章」，第五批复核实证其余三类形制共 229 处错位／越界
# 无法被任何门禁发现（如「卷十二第 11 章」卷十二仅 10 章、「卷三 1.5」自指错位）。
# v5 扩至四类形制：
#   A   第X卷第M章 / X卷第M章            核卷存在且章号 ≤ 该卷最大章号
#   B1  卷X 第N章 / 卷X第N章              同上（卷号在「卷」之后）
#   B2  卷X N.M（可续 /、– 接同卷节号）    核卷存在、章存在、节存在
#   B3  卷X / 卷 N / 第X卷（裸卷引用）    仅核卷存在
#
# 历史层引用（自第X卷第Y章迁入 / 并入 / 归卷 / 自卷 …）→ 指向旧体系，豁免
# 分工注（〔…归第X卷第Y章…〕 / 与第X卷第Y章分工）→ 指向现行体系，必须有效
#
# v6（2026-10-03）：HIST_PAT 增列「冻结基准」。缘由（归口单第五件第 1–2 项）：
#   卷 11 11.4 注文明言「章号沿用冻结基准（12 卷 181 章）旧第 09 卷…第 71 章；
#   现行体系对应本卷第 2 章 2.2」——旧号是**叙述性历史陈述**且已给出现行对应，
#   却被 v5 当作现行引用而判「卷不存在／章越界」。「冻结基准」一词只出现在
#   陈述旧体系编号的语境，凡引用紧邻该词（±25 字符）一律豁免；
#   `--selftest` 以正负夹具双向验证：紧邻者必豁免、远离者必仍报悬空。
#
# 注意：`!` 行（卷级分工注）渲染为 .vol-note，不在 <span class="src"> 内，
# 本脚本不覆盖（由 S6 独立脚本核验）。
import re
import sys

SELFTEST = '--selftest' in sys.argv

TARGET = sys.argv[1] if len(sys.argv) > 1 else r'D:/librebsd/08-核查报告与多轮复核/重构2026/index.html'
if SELFTEST:
    # 负向夹具（2026-10-03 第六批）：「冻结基准语境豁免」判据的双向验证。
    #  夹具1（须豁免）：引用紧邻「冻结基准」，且为叙述性历史旧号；
    #  夹具2/3/4（须报悬空）：不涉冻结基准、指向不存在的卷／越界的章。
    d = (
        '<section class="doc-block" id="vol-1">'
        '<h3 class="chapter" id="vol-1-ch-1">t</h3><ul class="sections">'
        '<span class="sec-num">1.1</span></ul></section>'
        '<span class="src">章号沿用冻结基准（12 卷 181 章）旧第 09 卷第 71 章；现行体系对应本卷第 2 章。</span>'
        '<span class="src">〔分工·迁移：卷 999 分工〕</span>'
        '<span class="src">与第 1 卷第 9 章分工</span>'
        '<span class="src">〔分工·迁移：卷 888 分工〕</span>'
    )
else:
    d = open(TARGET, encoding='utf-8').read()


def strip_tags(s):
    s = re.sub(r'<[^>]+>', '', s)
    return (s.replace('&amp;', '&').replace('&lt;', '<')
            .replace('&gt;', '>').replace('&nbsp;', ' '))


CN_NUM = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8,
          '九': 9, '十': 10, '十一': 11, '十二': 12, '十三': 13, '十四': 14, '十五': 15,
          '十六': 16, '十七': 17, '十八': 18, '十九': 19, '二十': 20, '二十一': 21,
          '二十二': 22, '二十三': 23, '二十四': 24, '二十五': 25, '二十六': 26,
          '二十七': 27, '二十八': 28, '二十九': 29, '三十': 30,
          # 2026-09-18 第二十二批扩至 36 卷（四大 BSD 文化与哲学四卷 ＋ 横向比较卷）：
          # 原表止于「三十」，31–36 卷的引用会被 cn2int 判为 None 而静默跳过（判据失效）。
          '三十一': 31, '三十二': 32, '三十三': 33, '三十四': 34, '三十五': 35,
          '三十六': 36,
          # 2026-09-27 第五批（目录卷级调整：43 卷终态）扩至 43 卷：37–43 卷引用同样会被
          # 静默跳过，故一并补齐。
          '三十七': 37, '三十八': 38, '三十九': 39, '四十': 40,
          '四十一': 41, '四十二': 42, '四十三': 43}


def cn2int(s):
    return int(s) if s.isdigit() else CN_NUM.get(s)


# ── 现行体系地图：卷→章、卷→章→节 ────────────────────────────────────
vol_ch = {}
vol_sec = {}
for m in re.finditer(r'<section class="doc-block" id="vol-(\d+)"', d):
    vid = int(m.group(1)); s = m.end()
    nxt = re.search(r'<section class="doc-block" id="vol-\d+"', d[s:])
    e = s + nxt.start() if nxt else len(d)
    seg = d[s:e]
    vol_ch[vid] = set(int(x) for x in re.findall(r'id="vol-\d+-ch-(\d+)"', seg))
    for cm in re.finditer(r'<h3 class="chapter" id="vol-\d+-ch-(\d+)">(.*?)</h3>\s*'
                          r'<ul class="sections">(.*?)</ul>', seg, re.S):
        cno = int(cm.group(1))
        vol_sec[(vid, cno)] = set(
            int(re.match(r'\d+\.(\d+)$', y).group(1))
            for y in re.findall(r'<span class="sec-num">([\d.]+)</span>', cm.group(3))
        )
maxch = {v: (max(c) if c else 0) for v, c in vol_ch.items()}

# ── 引用正则（四类形制，交替按「长优先」排列，避免短形制吞掉长形制）────────
NUM = r'[\d零一二三四五六七八九十]{1,3}'
NOTBARE = r'(?<![本该全各诸同每某两双多前上此彼其])'
PAT = re.compile(
    r'第?\s*(?P<a>{N})\s*卷\s*第\s*(?P<ach>\d{{1,3}})\s*章'
    r'|{NB}卷\s*(?P<b1>{N})\s*第\s*(?P<b1ch>\d{{1,3}})\s*章'
    r'|{NB}卷\s*(?P<b2>{N})\s*(?P<b2ch>\d{{1,3}})\.(?P<b2sec>\d{{1,3}})'
    r'|{NB}卷\s*(?P<c>{N})'
    r'|第\s*(?P<e>{N})\s*卷'.format(N=NUM, NB=NOTBARE)
)
CONT = re.compile(r'\s*[/、–—-]\s*(\d{1,3})\.(\d{1,3})')

HIST_PAT = re.compile(r'迁入|并入|归卷|自原|自第|自卷|移入|待考|历史层|冻结基准')
# 成组溯源括号的序列形制（2026-09-27 收窄）：v4 原以「引用前后 8 字符内出现『；』」
# 即判历史层，过宽——实测遮蔽真实悬空 6 处（如「〔卷三十 10.11 分工；ref 10005…〕」
# 中 `；` 之后是文献号而非引用，却被整条豁免）。现仅当 `；` 与引用共同构成
# `；第X卷…`／`；卷X…` 序列（或 `第X卷…；`）时才豁免。
HIST_SEQ = re.compile(
    r'；\s*(?:第\s*)?[\d零一二三四五六七八九十]{1,3}\s*卷'
    r'|卷\s*[0-9一二三四五六七八九十]{1,3}\s*；')
bad_div = []          # 悬空（现行层）
hist_refs = 0
div_ok = 0
form_stat = {k: 0 for k in ('A', 'B1', 'B2', 'B3')}
bad_stat = {k: 0 for k in ('A', 'B1', 'B2', 'B3')}


def is_hist(t, s0, s1):
    """历史层判定：引用前后 25 字符内有历史词；或前后 8 字符内构成 `；`＋引用序列。"""
    pre = t[max(0, s0 - 25):s0]
    post = t[s1:s1 + 25]
    pre8 = t[max(0, s0 - 8):s0]
    post8 = t[s1:s1 + 8]
    return (HIST_PAT.search(pre) or HIST_PAT.search(post)
            or HIST_SEQ.search(pre8) or HIST_SEQ.search(post8))


def check(v, c, sec=None):
    """现行层有效性；返回 None 表示有效，否则返回原因。"""
    if v is None:
        return None                     # 无法解析的卷号（非中文数字／数字）→ 交由人工
    if v not in vol_ch:
        return '卷不存在'
    if c is not None and c > maxch[v]:
        return '章越界（该卷仅 %d 章）' % maxch[v]
    if c is not None and c not in vol_ch[v]:
        return '章号缺失'
    if sec is not None and sec not in vol_sec.get((v, c), set()):
        return '节号缺失（该章仅 %d 节）' % len(vol_sec.get((v, c), set()))
    return None


for m in re.finditer(r'<span class="src">([\s\S]*?)</span>', d):
    raw = m.group(1)
    t = strip_tags(raw)
    for rm in PAT.finditer(t):
        gd = rm.groupdict()
        if gd['a'] is not None:
            form, vch = 'A', gd['a']
            v, c, sec = cn2int(vch), int(gd['ach']), None
        elif gd['b1'] is not None:
            form, vch = 'B1', gd['b1']
            v, c, sec = cn2int(vch), int(gd['b1ch']), None
        elif gd['b2'] is not None:
            form, vch = 'B2', gd['b2']
            v, c, sec = cn2int(vch), int(gd['b2ch']), int(gd['b2sec'])
        elif gd['c'] is not None:
            form, vch = 'B3', gd['c']
            v, c, sec = cn2int(vch), None, None
        else:
            form, vch = 'B3', gd['e']
            v, c, sec = cn2int(gd['e']), None, None
        form_stat[form] += 1
        if is_hist(t, rm.start(), rm.end()):
            hist_refs += 1
            continue
        why = check(v, c, sec)
        if why is None:
            div_ok += 1
        else:
            bad_stat[form] += 1
            bad_div.append((form, v, c, sec, why,
                            t[max(0, rm.start() - 30):rm.end() + 30]))
        # B2 续引（卷X N.M/N.M、N.M–N.M…）：同卷同章后续节号一并核验
        if form == 'B2':
            p = rm.end()
            while True:
                cm2 = CONT.match(t[p:])
                if not cm2:
                    break
                c2, s2 = int(cm2.group(1)), int(cm2.group(2))
                if is_hist(t, rm.start(), p + cm2.end()):
                    pass
                else:
                    why2 = check(v, c2, s2)
                    if why2 is None:
                        div_ok += 1
                    else:
                        bad_stat['B2'] += 1
                        bad_div.append(('B2续', v, c2, s2, why2,
                                        t[max(0, rm.start() - 30):p + cm2.end() + 30]))
                form_stat['B2'] += 1
                p += cm2.end()

print('形制命中：' + '  '.join('%s=%d' % (k, form_stat[k]) for k in ('A', 'B1', 'B2', 'B3')))
print('历史层引用（豁免）:', hist_refs)
print('分工注有效:', div_ok)
print('分工注悬空:', len(bad_div),
      '' if not bad_div else '（' + ' '.join('%s=%d' % (k, bad_stat[k])
                                            for k in ('A', 'B1', 'B2', 'B3') if bad_stat[k]) + '）')
for form, v, c, sec, why, ctx in bad_div:
    loc = '卷%s' % v if v is not None else '卷（未解析）'
    if c is not None:
        loc += ' 第%s章' % c
    if sec is not None:
        loc += ' %s.%s' % (c, sec)
    print('\n[悬空分工注] %s 形制%s：%s' % (loc, form, why))
    print('    ...%s...' % ctx)

print('门禁结论：分工注悬空 %d 处%s' % (len(bad_div), '，FAIL' if bad_div else '，PASS'))

if SELFTEST:
    ctx_all = ' '.join(c for *_, c in bad_div)
    ok_exempt = '冻结基准' not in ctx_all
    ok_pos = len(bad_div) == 3
    print('自检·夹具1（冻结基准语境须豁免）:', 'PASS' if ok_exempt else 'FAIL')
    print('自检·夹具2–4（真悬空须 3 处全数报出）:', 'PASS' if ok_pos else 'FAIL（实报 %d 处）' % len(bad_div))
    print('自检结论：', 'PASS' if (ok_exempt and ok_pos) else 'FAIL')
    sys.exit(0 if (ok_exempt and ok_pos) else 1)

sys.exit(1 if bad_div else 0)
