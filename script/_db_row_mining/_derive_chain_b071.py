# -*- coding: utf-8 -*-
"""从 b070 链路脚本派生 b071 版（机械替换 tag / 批 JSON 名 / pk 端点 / 台账水位）。

只替换字符串，不重写逻辑；替换后逐件断言关键字面存在。
注意：候选数／L4-L3／claim 号段／宿主 ROW_MINE 基线等**数据依赖常量**不在本脚本
范围内（建批时尚未知），留给读手波与 register 之后的第二遍补丁统一回填，
本脚本末尾会打印待回填清单。

替换顺序用占位符避免 138000→140000→142000 的链式撞车。
"""
import io
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)

PREV = "@@PREVTAG@@"
PKHI = "@@PKHI@@"
OFFHI = "@@OFFHI@@"

# 全件通用替换（顺序敏感）
COMMON = [
    ("fhk_b069", PREV),        # 上一批标签（台账 tags[-1] 断言）
    ("fhk_b070", "fhk_b071"),  # 本批标签
    (PREV, "fhk_b070"),        # 落回：b071 的上一批是 fhk_b070
    ("2598420", PKHI),
    ("2596415", "2598420"),
    ("2596416", "2598421"),
    (PKHI, "2600431"),
    ("140000", OFFHI),
    ("138001", "140001"),
    ("138000", "140000"),
    (OFFHI, "142000"),
]

# 台账专用：tags 计数（69→70，上一批 69 条，入账后 71 条）
LEDGER_EXTRA = [
    ("len(tags) == 69", "len(tags) == 70"),
    ("range(1, 70)", "range(1, 71)"),
    ("n_recs == 69", "n_recs == 70"),
    ("tags 70 条", "tags 71 条"),
    ("tags 应为 69 条", "tags 应为 70 条"),
    ("tags[-1] == \"fhk_b069\"", "tags[-1] == \"fhk_b070\""),
]

JOBS = [
    "_part_split_b070.py",
    "_gen_read_task_fhk_b070.py",
    "_READ_TASK_fhk_b070.md",
    "_merge_cand_fhk_b070.py",
    "_gate_cand_b070.py",
    "_register_fhk_b070.py",
    "_verify_reg_fhk_b070.py",
    "_gen_narrpkg_b070.py",
    "_merge_narr_fhk_b070.py",
    "_outline_fhk_b070.py",
    "_bookkeep_wave_fhk_b070.py",
    "_ledger_b070.py",
    "_final_verify_b070.py",
    "_NARR_TASK_fhk_b070.md",
]

for src in JOBS:
    assert os.path.exists(src), "缺源 %s" % src
    dst = src.replace("b070", "b071")
    t = io.open(src, encoding="utf-8").read()
    n0 = t.count("fhk_b070")
    assert n0 > 0, "%s 无 fhk_b070 字面" % src
    n_prev = t.count("fhk_b069")   # 原文件里「上一批」引用数
    for a, b in COMMON:
        t = t.replace(a, b)
    if src == "_ledger_b070.py":
        for a, b in LEDGER_EXTRA:
            if a not in t:
                print("  [警告] 台账未命中替换：%r" % a[:40])
            else:
                t = t.replace(a, b)
    # fhk_b070 允许残留，且残留数必须恰好等于原 fhk_b069 数（上一批引用改指 b070）
    left = t.count("fhk_b070")
    assert left == n_prev, "%s 残留 fhk_b070 %d 条 != 原 fhk_b069 %d 条" % (dst, left, n_prev)
    assert PREV not in t and PKHI not in t and OFFHI not in t, "%s 残留占位符" % dst
    with io.open(dst, "w", encoding="utf-8", newline="") as fh:
        fh.write(t)
        fh.flush()
        os.fsync(fh.fileno())
    rb = io.open(dst, "rb").read()
    assert b"\r" not in rb and not rb.startswith(b"\xef\xbb\xbf"), "%s 含 CR/BOM" % dst
    print("[派生] %-34s -> %-34s (%d 处 tag, %d B)"
          % (src, dst, n0, len(rb)))

print()
print("=== 待第二遍回填的数据依赖常量（建批时尚未知）===")
for dst, items in [
    ("_gen_read_task_fhk_b071.py", []),
    ("_merge_cand_fhk_b071.py", ["候选条数断言"]),
    ("_register_fhk_b071.py", ["候选条数断言"]),
    ("_gen_narrpkg_b071.py", ["候选条数 / 分片数 / L4-L3 计数"]),
    ("_outline_fhk_b071.py", ["assert len(rows)==1077"]),
    ("_bookkeep_wave_fhk_b071.py", ["WAVE rows=1077"]),
    ("_final_verify_b071.py",
     ["N_EXP=1077", "L4_EXP=451", "L3_EXP=626", "CID 403349/404425",
      "REFS_BEFORE=20504（须实测宿主当前 ROW_MINE）"]),
    ("_READ_TASK_fhk_b071.md", ["BLIND 数 332→351", "候选数", "claim 号段"]),
    ("_NARR_TASK_fhk_b071.md", ["候选数", "分片条数分布", "claim 号段"]),
]:
    print("  %-32s %s" % (dst, "; ".join(items) if items else "无"))
