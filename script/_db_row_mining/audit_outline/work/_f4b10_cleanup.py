#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""F4 全历史临时件清理（批次十收口触发，§〇之三：第 10 批＝全量复核触发点）。

用法：
  python _f4b10_cleanup.py            # 只读复核：打印保留／拟删两栏
  python _f4b10_cleanup.py --apply    # 逐个 os.remove，删后重枚举父目录比对（不用 os.path.exists）

判据（任务书 §〇之三）：
  必留：judgements/、shards/ 判读件与分片；work/ 挂账产物、_judge_prompt_*/_pad_prompt_*、
        _f*_resume.md、f4_skip_deepseek.txt；processed*.jsonl 台账；beacon/；
        差分门禁与归属对账脚本；hosts_*.txt 宿主清单
  可删：fetch 档案（oaa_fetch --host 可重取）、台账快照 processed_f4.jsonl.bak-*/pre_*
        （现行台账为严格超集）、宿主 .bak-f4b*（批次已提交、git 持有 pre 态）、
        F4 批次备份目录件（f4b07_bak／b3_bak 内 F4 件）、rescue/*.rescue*.jsonl
        （已整行回填进判定件）、一次性 .py／.log／.txt 转储／.partial
  禁删：git 已跟踪件；他会话（F1/F2/F3/H/D_b06）件一律不进候选集
"""
import os, re, subprocess, sys

ROOT = r"D:\librebsd"
DM = os.path.join(ROOT, "script", "_db_row_mining")
AUD = os.path.join(DM, "audit_outline")
WORK = os.path.join(AUD, "work")
OUTL = os.path.join(ROOT, "05-卷册大纲")

MODE = "apply" if any(a.replace("-", "") == "apply" for a in sys.argv[1:]) else "review"

tracked = set()
r = subprocess.run(["git", "ls-files"], capture_output=True, text=True, cwd=ROOT)
for ln in r.stdout.splitlines():
    tracked.add(ln.replace("\\", "/"))

# F4 归属：批次标签
F4 = re.compile(r"f4b\d\d|f4_b\d\d|f4len\d|f4_skip|f4_pending|f4_b")
# 必留（命中即永不出候选集）
KEEP = re.compile(
    r"/judgements/f4b\d+|/shards/f4b\d+"
    r"|_judge_prompt_.*f4|_pad_prompt_.*f4"
    r"|hosts.*f4|f4.*hosts"
    r"|hang_account|pad_residual|fixdb_triage|ledger_remap|ledger_fixdb|ledger_doubt"
    r"|_f4b\d+_resume|f4_skip_deepseek"
    r"|processed_f4\.jsonl$"
    r"|/beacon/"
    r"|_f4b\d+_diffgate|_f4b\d+_lenstat|_f4b\d+_linetally|_f4b\d+_tail"
    r"|_f4b\d+_postverify|_f4b\d+_reconcile|_f4b\d+_register|_f4b\d+_order"
    r"|_f4b\d+_final_merge|_f4b\d+_verify_register|_f4b\d+_reg_coverage"
    r"|_f4b\d+_gap_scope|_f4b\d+_cjk_baseline|_f4b\d+_cleanup|_f4b\d+_build_ledgers"
    r"|_f4b\d+_fails_existential|_f4b\d+_report_stats|_f4b\d+_commit_list"
    r"|_f4b\d+_ledger_dump|_apply_f4b\d+"
    r"|meta_dump|_f4b\d+_hangdump"
)
# 可删（按形态分类）
DEL = [
    (re.compile(r"\.fetch\.jsonl$"), "fetch 档案（oaa_fetch --host 可重取）"),
    (re.compile(r"processed_f4\.jsonl\.(bak|pre)"), "台账快照（现行台账为严格超集）"),
    (re.compile(r"\.bak-f4b\d\d|\.bak-f4len\d"), "宿主 .bak-f4b*/f4len*（批次已提交，git 持有 pre 态）"),
    (re.compile(r"/f4b07_bak/"), "批次七备份目录件"),
    (re.compile(r"pre_f4len\d|f4len\d_bak"), "批次三/五宿主备份"),
    (re.compile(r"\.rescue\d?\.jsonl$"), "rescue 波次件（已整行回填判定件）"),
    (re.compile(r"\.(log|txt)$"), ".log/.txt 转储"),
    (re.compile(r"\.partial$"), ".partial 半成品"),
    (re.compile(r"_data_|_meta_|_j_data_"), "中间数据"),
    (re.compile(r"\.py$"), "一次性 .py"),
]


def walk(d):
    out, stack = [], [d]
    while stack:
        cur = stack.pop()
        try:
            names = os.listdir(cur)
        except OSError:
            continue
        for n in names:
            p = os.path.join(cur, n)
            rel = os.path.relpath(p, ROOT).replace("\\", "/")
            if os.path.isdir(p):
                stack.append(p)
            else:
                try:
                    out.append((rel, os.path.getsize(p)))
                except OSError:
                    out.append((rel, 0))
    return out


files = walk(os.path.join(DM, "_tmp")) + walk(AUD)
stack = [OUTL]
while stack:
    cur = stack.pop()
    for n in os.listdir(cur):
        p = os.path.join(cur, n)
        if os.path.isdir(p):
            stack.append(p)
        elif n.endswith(".bak") or ".bak-" in n:
            files.append((os.path.relpath(p, ROOT).replace("\\", "/"), os.path.getsize(p)))

cand, keep, skip_tracked, skip_other = [], 0, [], 0
from collections import Counter
why_c = Counter()
for rel, s in files:
    b = os.path.basename(rel)
    if not F4.search(b):
        skip_other += 1
        continue
    if KEEP.search(rel):
        keep += 1
        continue
    if rel in tracked:
        skip_tracked.append((rel, s))
        continue
    hit = None
    for pat, why in DEL:
        if pat.search(rel):
            hit = why
            break
    if hit:
        cand.append((rel, s, hit))
        why_c[hit] += s

print("=" * 78)
print("F4 件复核（他会话/无标签件 %d 件未进候选集；必留 %d 件；git 已跟踪禁删 %d 件）"
      % (skip_other, keep, len(skip_tracked)))
for rel, s in skip_tracked:
    print("   [禁删] %s" % rel)
print("拟删合计: %d 件 / %.2f MB" % (len(cand), sum(s for _, s, _ in cand) / 1e6))
print("-" * 78)
for why, tot in why_c.most_common():
    print("  %9.2f MB  %s" % (tot / 1e6, why))
print("=" * 78)

ok = True
if MODE == "review":
    print("\n【复核模式】前 30 件拟删明细：")
    for rel, s, why in sorted(cand, key=lambda x: -x[1])[:30]:
        print("  %10.1f KB  %s" % (s / 1e3, rel))
    print("\n复核确认后加 --apply 执行。")
    sys.exit(0)

freed, failed = 0, 0
for rel, s, why in sorted(cand):
    p = os.path.join(ROOT, *rel.split("/"))
    # 守卫：路径必须在 ROOT 下、必须存在、不得是目录、不得被跟踪
    ab = os.path.abspath(p)
    if not ab.startswith(os.path.abspath(ROOT)):
        print("  ! 越界跳过 %s" % rel); ok = False; continue
    if os.path.isdir(ab):
        continue
    if rel in tracked:
        print("  ! 已跟踪跳过 %s" % rel); ok = False; continue
    try:
        os.remove(ab)
        freed += s
    except OSError as e:
        failed += 1
        print("  ! 删除失败 %s: %s" % (rel, e))

# 清空目录（F4 专用备份目录若已空）
for d in (os.path.join(AUD, "f4b07_bak"),):
    if os.path.isdir(d):
        try:
            os.rmdir(d)
            print("  已清空目录 %s" % os.path.relpath(d, ROOT))
        except OSError:
            pass

# 删后重枚举父目录比对（不用 os.path.exists 判断是否已删）
present = set()
st = [os.path.join(DM, "_tmp"), AUD, os.path.join(ROOT, "05-卷册大纲")]
while st:
    cur = st.pop()
    try:
        for n in os.listdir(cur):
            p = os.path.join(cur, n)
            if os.path.isdir(p):
                st.append(p)
            else:
                present.add(os.path.relpath(p, ROOT).replace("\\", "/"))
    except OSError:
        continue
still = [rel for rel, _, _ in cand if rel in present]
print("=" * 78)
print("删除 %d 件 / 释放 %.2f MB ｜ 失败 %d ｜ 删后仍在盘 %d" %
      (len(cand) - failed, freed / 1e6, failed, len(still)))
for rel in still[:20]:
    print("   仍在盘: %s" % rel)
sys.exit(0 if ok and not still else 1)
