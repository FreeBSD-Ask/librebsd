#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""F4 临时件清理（批次九收口提交后触发，连清 F4 全历史残留）。

用法：
  python _f4b09_cleanup.py             # 复核模式：打印 保留／拟删 两栏，写 work/_f4b09_cleanup_report.txt
  python _f4b09_cleanup.py --apply     # 复核通过后逐个 os.remove

🔴 收窄：本脚本只列 F4 自有件（F4 批次标签件 ＋ F4 宿主专属抓取派生件 ＋
   F4 批次九宿主 .bak-f4b09* 备份 ＋ F4 派生 pyc）。work/ 下他会话
   （F1/F2/F3、H 线、112 线）件一律不进候选集，不出现在任何一栏。

判据（任务书 §〇之三.2，三条须同时成立才删）：
  ① 未被 git 跟踪 —— 一律以 `git ls-files` 实测，不凭文件名推测
     （/script 整树被 .gitignore 忽略，须实测而非推断）；
  ② 不被已提交脚本或批次报告引用 —— 引用集按反引号跨度拆 token 交叉核验；
  ③ 所属批次已闭环 —— 批次一～九均已提交（批次九收口 5470e8c99），
     宿主 .bak-f4b09a 与 git 父提交 0916595a5^ 字节一致，pre 态可复原。

口径（§〇之三.3/6）：先复核后删、无需备份、禁通配符盲删；
   删除用 os.remove 逐个删；删后判「已删」不用 os.path.exists
   （UNC 写后读回滞后），改重新 os.listdir 枚举父目录、间隔 3 秒取一致快照。
"""
import os
import re
import subprocess
import sys
import time
from collections import Counter

# 🔴 路径一律用 Windows 盘符形式：UNC 上以 POSIX 路径（/d/librebsd/…）写文件
#    会静默失败（报成功但不落盘），实测复核清单写不进去。
ROOT = r'D:\librebsd'
AO = os.path.join(ROOT, r'script\_db_row_mining\audit_outline')
TMP = os.path.join(ROOT, r'script\_db_row_mining\_tmp')
W = os.path.join(AO, 'work')
PC = os.path.join(W, '__pycache__')
CH = os.path.join(ROOT, '05-卷册大纲', '第01卷-unix的起源', '第11章-操作系统的谱系')
MODE = 'report'
for a in sys.argv[1:]:
    if a.startswith('--'):
        a = a[2:]
    if a in ('apply', 'report'):
        MODE = a

F4 = re.compile(r'f4b0[1-9]|f4_b0[1-9]|f4b1[0-9]')
BAK = re.compile(r'\.bak-f4b0[1-9]')

# ---- ① git 跟踪集（判据①） ----
r = subprocess.run(['git', 'ls-files'], cwd=ROOT, stdout=subprocess.PIPE,
                   text=True, encoding='utf-8', errors='replace')
tracked = set()
for line in r.stdout.splitlines():
    line = line.strip()
    if line:
        tracked.add(os.path.normpath(os.path.join(ROOT, line)))

# ---- ② 引用集（判据②） ----
ref = set()


def collect_docs(d):
    out = []
    if not os.path.isdir(d):
        return out
    stack = [d]
    while stack:
        cur = stack.pop()
        try:
            for e in os.listdir(cur):
                p = os.path.join(cur, e)
                if os.path.isdir(p):
                    stack.append(p)
                elif p.endswith('.md'):
                    out.append(p)
        except OSError:
            continue
    return out


for d in (os.path.join(ROOT, '08-核查报告与多轮复核', '07-目录审计'),
          os.path.join(ROOT, '01-项目管理', '01-编纂规划与报告归档'), W, TMP):
    for p in collect_docs(d):
        try:
            t = open(p, encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        for m in re.finditer(r'`([^`]+)`', t):
            for tok in re.split(r'[、，,；;\s/]+', m.group(1)):
                tok = tok.strip()
                if len(tok) > 4:
                    ref.add(tok)
        for m in re.finditer(r'[\w.\-\u4e00-\u9fff]{5,}(?:\.(?:py|json|jsonl|md|txt|log|pyc))', t):
            ref.add(m.group(0))


def referenced(p):
    base = os.path.basename(p)
    stem = re.sub(r'\.(jsonl|json|md|txt|log|py|pyc)$', '', base)
    for cand in (base, stem):
        if len(cand) < 5:
            continue
        for t in ref:
            if cand in t:
                return True
    return False


# ---- F4 宿主集合（判定抓取派生件归属的唯一依据） ----
F4_HOST_LISTS = ['hosts_f4_b02.txt', 'hosts_f4_b03.txt', 'hosts_f4_b04.txt',
                 'hosts_f4_b05.txt', 'hosts_f4_b06.txt', 'f4b07_hosts.txt',
                 'f4b08_hosts.txt', 'hosts.txt', 'hosts_b7a.txt']
f4_hosts = set()
for e in F4_HOST_LISTS:
    p = os.path.join(W, e)
    if not os.path.isfile(p):
        continue
    for l in open(p, encoding='utf-8', errors='replace'):
        l = l.strip()
        if not l:
            continue
        b = l.split('\t')[0].strip().split('\\')[-1].split('/')[-1]
        if b.endswith('.md'):
            b = b[:-3]
        f4_hosts.add(b)
for b in ('11.3-unix碎片化各厂商版本彼此不兼容数据库厂商informix需为超过100种',
          '11.10-1978年同时期操作系统的比较cpm1974appledos1978vms',
          '11.12-关键词行级挖掘素材线索'):
    f4_hosts.add(b)

# ---- 候选集：只收 F4 自有件 ----
# 排除复核清单自身（每跑一次重写，纳入候选会自我拟删）
SELF_EXCLUDE = ('_f4b09_cleanup_report.txt',)
cand = []
for base in (W, TMP, os.path.join(AO, 'shards'), os.path.join(AO, 'judgements'),
             os.path.join(AO, 'beacon'), AO, PC):
    if not os.path.isdir(base):
        continue
    try:
        ents = os.listdir(base)
    except OSError:
        continue
    for e in ents:
        if e in SELF_EXCLUDE:
            continue
        p = os.path.join(base, e)
        if not os.path.isfile(p):
            continue
        if F4.search(e) or BAK.search(e):
            cand.append(p)
# F4 宿主专属抓取档案（无 F4 标签）
for e in os.listdir(W):
    p = os.path.join(W, e)
    if not os.path.isfile(p):
        continue
    if e.endswith('.fetch.jsonl') and e[:-len('.fetch.jsonl')] in f4_hosts:
        cand.append(p)
    if e in ('b7b_fetch_all.jsonl', 'f4_b09_all.jsonl'):
        cand.append(p)
# 大纲树 F4 批次宿主备份
if os.path.isdir(CH):
    for e in os.listdir(CH):
        p = os.path.join(CH, e)
        if os.path.isfile(p) and BAK.search(e):
            cand.append(p)

# ---- 必留规则 ----
KEEP_PAT = [
    r'[\\/]judgements[\\/][^\\/]*\.jsonl$',
    r'[\\/]shards[\\/][^\\/]*\.jsonl$',
    r'processed(_f\d)?\.jsonl$',
    r'beacon\.json$',
    r'claims_(F\d|UNCLAIMED)\.txt$',
    r'_judge_prompt_', r'_pad_prompt_',
    r'_resume\.md$',
    r'f4_skip_deepseek\.txt$',
    r'_hang_account\.json$',
    r'_pad_residual\.json$',
    r'_triage\.json$',
    r'_register_files\.txt$',
    r'_ledger_',
    # 批次七挂账 key 清单（X1 等级／X2 remap 交接依据）
    r'_f4b0[1-8]_(x1_level|x1_text|x2_remap|fixdb_remap_keys)\.json$',
    # 宿主清单：新旧两制都留（§〇之三.4 明列永不删），含子波后缀
    r'hosts_f4_b0\d\w*\.txt$', r'f4b0[678]_hosts\.txt$',
    r'_f4b0\d\w*_hosts\.txt$', r'_f4b0\d\w*hosts\.txt$',
    r'ledger_(fixdb|remap|doubt)\.md$',
    r'_f4_cleanup\.py$', r'_f4b09_cleanup\.py$',
    r'diffgate|provenance|verify_f4|_verify\b',
]
# 批次九报告 §四 明列引用的核验脚本
B09_KEEP = ['final_merge', 'reg_coverage', 'verify_register', 'order.py',
            'tail.py', 'linetally', 'six.py', 'lenstat']
# 批次八门禁与对账族（批次八已闭环，脚本是复核依据）
B08D_KEEP = ('f4b08d_diffgate', 'f4b08d_provenance', 'f4b08d_g2',
             'f4b08d_gate9', 'f4b08d_recon')
# 批次九挂账台账生成器与 fix-db 分诊（台账复核依据）
LEDGER_KEEP = ('f4b09_ledger', 'f4b09_fixdb_triage', 'f4b09_hosts.txt')


def keep_reason(p):
    n = os.path.basename(p).lower()
    r_ = os.path.relpath(p, ROOT).replace(os.sep, '/')
    if r_ in tracked or os.path.normpath(p) in tracked:
        return 'GIT_TRACKED'
    if any(re.search(x, r_) for x in KEEP_PAT):
        return 'KEEP_PAT'
    if referenced(p):
        return 'REF'
    if any(t in n for t in B09_KEEP):
        return 'B09_REPORT_REF'
    if any(t in n for t in B08D_KEEP):
        return 'B08_GATE'
    if any(t in n for t in LEDGER_KEEP):
        return 'LEDGER_TOOL'
    if '_dec_f4' in n:
        return 'DEC_RECORD'
    # 宿主 .bak-f4b09* 是差分门禁基线（§〇之三.4 明列必留类别），
    # 被保留的 _f4b09_diffgate / lenstat / linetally / six 四个脚本按名硬编码读取。
    if re.search(r'\.bak-f4b0[1-9]', n):
        return 'GATE_BASELINE'
    return None


KEEP_LABEL = {'GIT_TRACKED': 'git已跟踪', 'KEEP_PAT': '必留清单', 'REF': '被报告引用',
              'B09_REPORT_REF': '批次九报告引用', 'B08_GATE': '批次八门禁对账',
              'LEDGER_TOOL': '挂账台账工具', 'DEC_RECORD': '判定决策留痕',
              'GATE_BASELINE': '差分门禁基线'}


def drop_reason(p):
    r_ = os.path.relpath(p, ROOT).replace(os.sep, '/')
    n = os.path.basename(p)
    if re.search(r'\.md\.bak-f4b0[1-9]', r_):
        return '宿主备份·批次已提交'
    if re.search(r'f4b09_all\.jsonl$|b7b_fetch_all\.jsonl$|\.fetch\.jsonl$', r_):
        return '抓取派生件·可重取'
    if n.endswith('.pyc'):
        return 'pyc 编译缓存'
    if re.search(r'\.(log|txt)$', n) and F4.search(n):
        return '一次性日志转储'
    if re.search(r'\.py$', n):
        return '一次性脚本'
    if F4.search(n):
        return '一次性中间件'
    return '临时件'


st = []
for p in dict.fromkeys(cand):
    try:
        st.append((p, os.path.getsize(p)))
    except OSError:
        pass

keep, drop = [], []
for p, sz in st:
    why = keep_reason(p)
    if why:
        keep.append((p, sz, KEEP_LABEL[why]))
    else:
        drop.append((p, sz, drop_reason(p)))

tot_k = sum(s for _, s, _ in keep)
tot_d = sum(s for _, s, _ in drop)
lines = []


def out(s=''):
    print(s)
    lines.append(s)


out('=' * 84)
out('F4 收窄清理复核（批次九收口触发）    git 跟踪 %d 项    引用 token %d 项    F4 宿主 %d 个'
    % (len(tracked), len(ref), len(f4_hosts)))
out('候选 F4 自有件 %d 件 = 保留 %d + 拟删 %d' % (len(keep) + len(drop), len(keep), len(drop)))
out('=' * 84)
out('【拟删】%d 件 / %.2f MB' % (len(drop), tot_d / 1e6))
for p, sz, w in sorted(drop, key=lambda x: -x[1]):
    out('   %9.2f KB  %-20s %s' % (sz / 1024, w, os.path.relpath(p, ROOT)))
out('--- 拟删按原因归并 ---')
c = Counter(w for _, _, w in drop)
for w, n in c.most_common():
    out('   %5d 件  %8.2f MB  %s' % (n, sum(s for _, s, x in drop if x == w) / 1e6, w))
out()
out('【保留】%d 件 / %.2f MB' % (len(keep), tot_k / 1e6))
for p, sz, w in sorted(keep, key=lambda x: (x[2], x[0])):
    out('   %-14s %s' % (w, os.path.relpath(p, ROOT)))
out('=' * 84)

out_path = os.path.join(W, '_f4b09_cleanup_report.txt')
with open(out_path, 'w', encoding='utf-8') as fh:
    fh.write('F4 临时件清理复核清单（批次九收口触发，连清 F4 全历史）\n')
    fh.write('生成 %s\n' % time.strftime('%Y-%m-%d %H:%M:%S'))
    fh.write('候选 %d 件 / 保留 %d 件 (%.2f MB) / 拟删 %d 件 (%.2f MB)\n\n' % (
        len(keep) + len(drop), len(keep), tot_k / 1e6, len(drop), tot_d / 1e6))
    fh.write('# 拟删\n')
    for p, sz, w in sorted(drop, key=lambda x: -x[1]):
        fh.write('%s\t%.2f KB\t%s\n' % (w, sz / 1024, os.path.relpath(p, ROOT)))
    fh.write('\n# 保留\n')
    for p, sz, w in sorted(keep, key=lambda x: (x[2], x[0])):
        fh.write('%s\t%.2f KB\t%s\n' % (w, sz / 1024, os.path.relpath(p, ROOT)))
out('清单已写 work/_f4b09_cleanup_report.txt')

if not drop:
    out('拟删清单为空，无需操作。')
    sys.exit(0)
if MODE != 'apply':
    out('复核模式：未删除任何文件。确认无误后重跑并加 --apply。')
    sys.exit(0)

out('')
out('开始删除 %d 件 …' % len(drop))
fail = []
for p, sz, _ in sorted(drop, key=lambda x: -x[1]):
    try:
        os.remove(p)
    except OSError as ex:
        fail.append((p, sz, str(ex)))
        print('! 删除失败 %s : %s' % (os.path.relpath(p, ROOT), ex))
time.sleep(3)


def still_present(p):
    par = os.path.dirname(p)
    try:
        return os.path.basename(p) in os.listdir(par)
    except OSError:
        return True


snap1 = sum(1 for p, _, _ in drop if still_present(p))
time.sleep(3)
snap2 = [p for p, _, _ in drop if still_present(p)]
out('--- 删除复核（重枚举父目录，非 exists）---')
out('拟删 %d 件 | 一次枚举残留 %d 件 | 二次枚举残留 %d 件' % (len(drop), snap1, len(snap2)))
out('删除异常 %d 件' % len(fail))
for p, _, e in fail:
    out('   %s : %s' % (os.path.relpath(p, ROOT), e))
ok_sz = sum(s for p, s, _ in drop if p not in snap2)
out('实际删除 %d 件 / %.2f MB；残留 %d 件 / %.2f MB' % (
    len(drop) - len(snap2), ok_sz / 1e6, len(snap2),
    sum(s for p, s, _ in drop if p in snap2) / 1e6))
for p in snap2:
    out('   残留 %s' % os.path.relpath(p, ROOT))
