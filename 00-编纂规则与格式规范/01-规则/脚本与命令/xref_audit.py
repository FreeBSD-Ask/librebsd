# -*- coding: utf-8 -*-
# 交叉引用悬空审计 v4：逐条 src 标注分类处理
#   历史层引用（← 自第X卷第Y章迁入 / 并入 / 归卷）→ 指向旧体系，豁免
#   分工注（〔...归第X卷第Y章...〕 / 与第X卷第Y章分工）→ 指向现行体系，必须有效
import re
from collections import defaultdict

import sys
TARGET = sys.argv[1] if len(sys.argv) > 1 else r'D:/librebsd/08-核查报告与多轮复核/重构2026/index.html'
d = open(TARGET, encoding='utf-8').read()

def strip_tags(s):
    s = re.sub(r'<[^>]+>', '', s)
    return s.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&nbsp;', ' ')

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

vol_ch = {}
for m in re.finditer(r'<section class="doc-block" id="vol-(\d+)"', d):
    vid = int(m.group(1)); s = m.end()
    nxt = re.search(r'<section class="doc-block" id="vol-\d+"', d[s:])
    e = s + nxt.start() if nxt else len(d)
    seg = d[s:e]
    vol_ch[vid] = set(int(x) for x in re.findall(r'id="vol-\d+-ch-(\d+)"', seg))
maxch = {v: max(c) for v, c in vol_ch.items()}

def cn2int(s):
    return int(s) if s.isdigit() else CN_NUM.get(s)

# 逐条 src 标注分析
ref_pat = re.compile(r'第([\u4e00-\u9fff]{1,3}|\d{1,2})卷\s*第\s*(\d{1,3})\s*章')
bad_div = []   # 分工注悬空
hist_refs = 0
div_ok = 0
HIST_PAT = re.compile(r'迁入|并入|归卷|自原|自第|移入|待考|历史层')
for m in re.finditer(r'<span class="src">([\s\S]*?)</span>', d):
    raw = m.group(1)
    t = strip_tags(raw)
    for rm in ref_pat.finditer(t):
        v = cn2int(rm.group(1)); c = int(rm.group(2))
        if v is None:
            continue
        # 历史层判定：
        #   a. 引用前后 25 字符内出现历史词（迁入/并入/归卷/自原/自第/移入/待考/历史层）
        #   b. 引用前后 8 字符内出现「；」→ 成组溯源括号（旧节号序列格式）
        pre = t[max(0, rm.start()-25):rm.start()]
        post = t[rm.end():rm.end()+25]
        pre8 = t[max(0, rm.start()-8):rm.start()]
        post8 = t[rm.end():rm.end()+8]
        if HIST_PAT.search(pre) or HIST_PAT.search(post) or '；' in pre8 or '；' in post8:
            hist_refs += 1
            continue
        # 现行层分工注：必须有效
        if v in vol_ch and c <= maxch[v]:
            div_ok += 1
        else:
            bad_div.append((v, c, m.start(), t[max(0, rm.start()-30):rm.end()+30]))

print('历史层引用（豁免）:', hist_refs)
print('分工注有效:', div_ok)
print('分工注悬空:', len(bad_div))
for v, c, pos, ctx in bad_div:
    print('\n[悬空分工注] 第%d卷第%d章（现行第%d卷%d章）' % (v, c, v, maxch.get(v, 0)))
    print('    ...%s...' % ctx)

print('门禁结论：分工注悬空 %d 处%s' % (len(bad_div), '，FAIL' if bad_div else '，PASS'))
sys.exit(1 if bad_div else 0)
