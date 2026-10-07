# -*- coding: utf-8 -*-
"""从 b071 链路脚本派生 b072 版（机械替换 tag / 批 JSON 名 / pk 端点 / 台账水位）。

只替换字符串，不重写逻辑；替换后逐件断言占位符无残留、tag 计数守恒。
注意：候选数／L4-L3／claim 号段／宿主 ROW_MINE 基线等**数据依赖常量**不在本脚本
范围内（建批时尚未知），留给读手波与 register 之后的第二遍补丁统一回填，
本脚本末尾会打印待回填清单。

替换顺序用占位符避免链式撞车：b071 的 pk_hi 2600431 与 b071 的台账 hi 142000
同时又是 b070 侧「上一批」值的目标，直接替换会二次改写，故先 stash 再落位。
"""
import io
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)

TAG1 = "@@THIS@@"      # b071 本批标签占位
PK1 = "@@PK_LO@@"      # 2598421
PK2 = "@@PK_HI@@"      # 2600431
OFF1 = "@@ORD_LO@@"    # 140001
OFF2 = "@@ORD_HI@@"    # 142000

# 顺序敏感：先 stash 本批值，再平移「上一批」侧值，最后落 b072 值。
COMMON = [
    # --- 本批标签 ---
    ("fhk_b071", TAG1),
    ("fhk_b070", "fhk_b071"),
    (TAG1, "fhk_b072"),
    # --- stash 本批 pk / 库内序 ---
    ("2598421", PK1),
    ("2600431", PK2),
    ("140001", OFF1),
    ("142000", OFF2),
    # --- 「上一批」侧平移（b070 值 -> b071 值）---
    ("2598420", "2600431"),
    ("138001", "140001"),
    ("138000", "140000"),
    ("140000", "142000"),
    # --- 落 b072 值 ---
    (PK1, "2600432"),
    (PK2, "2602440"),
    (OFF1, "142001"),
    (OFF2, "144000"),
]

# 台账专用：tags 计数（b071 入账后 71 条 -> b072 入账后 72 条）
LEDGER_EXTRA = [
    ("len(tags) == 70", "len(tags) == 71"),
    ("range(1, 71)", "range(1, 72)"),
    ("n_recs == 70", "n_recs == 71"),
    ("tags 71 条", "tags 72 条"),
    ("tags 应为 70 条", "tags 应为 71 条"),
]

JOBS = [
    "_digest_fhk_b071.py",
    "_blind_fhk_b071.py",
    "_part_split_b071.py",
    "_gen_read_task_fhk_b071.py",
    "_READ_TASK_fhk_b071.md",
    "_merge_cand_fhk_b071.py",
    "_gate_cand_b071.py",
    "_register_fhk_b071.py",
    "_verify_reg_fhk_b071.py",
    "_gen_narrpkg_b071.py",
    "_merge_narr_fhk_b071.py",
    "_outline_fhk_b071.py",
    "_bookkeep_wave_fhk_b071.py",
    "_ledger_b071.py",
    "_final_verify_b071.py",
    "_NARR_TASK_fhk_b071.md",
]

for src in JOBS:
    assert os.path.exists(src), "缺源 %s" % src
    dst = src.replace("b071", "b072")
    t = io.open(src, encoding="utf-8").read()
    n_this = t.count("fhk_b071")
    n_prev = t.count("fhk_b070")
    assert n_this > 0, "%s 无 fhk_b071 字面" % src
    for a, b in COMMON:
        t = t.replace(a, b)
    if src == "_ledger_b071.py":
        for a, b in LEDGER_EXTRA:
            if a not in t:
                print("  [警告] 台账未命中替换：%r" % a[:40])
            else:
                t = t.replace(a, b)
    for ph in (TAG1, PK1, PK2, OFF1, OFF2):
        assert ph not in t, "%s 残留占位符 %s" % (dst, ph)
    assert t.count("fhk_b072") == n_this, \
        "%s 本批标签 %d != 源 %d" % (dst, t.count("fhk_b072"), n_this)
    assert t.count("fhk_b071") == n_prev, \
        "%s 上一批标签 %d != 源 fhk_b070 %d" % (dst, t.count("fhk_b071"), n_prev)
    with io.open(dst, "w", encoding="utf-8", newline="") as fh:
        fh.write(t)
        fh.flush()
        os.fsync(fh.fileno())
    rb = io.open(dst, "rb").read()
    assert b"\r" not in rb and not rb.startswith(b"\xef\xbb\xbf"), "%s 含 CR/BOM" % dst
    print("[派生] %-34s -> %-34s (%d 本批, %d 上一批, %d B)"
          % (src, dst, n_this, n_prev, len(rb)))

print()
print("=== 待第二遍回填的数据依赖常量（建批时尚未知）===")
for dst, items in [
    ("_gen_read_task_fhk_b072.py",
     ["BLIND 数", "候选数", "claim 号段", "跳号清单", "正文统计"]),
    ("_merge_cand_fhk_b072.py", ["候选条数断言"]),
    ("_register_fhk_b072.py", ["候选条数断言"]),
    ("_gen_narrpkg_b072.py", ["候选条数 / 分片数 / L4-L3 计数"]),
    ("_outline_fhk_b072.py", ["无需回填（已 assert len(rows)==len(lv) 泛化）"]),
    ("_bookkeep_wave_fhk_b072.py", ["WAVE rows 现为 1321（b071 值）"]),
    ("_final_verify_b072.py",
     ["N_EXP=1321", "L4_EXP=498", "L3_EXP=823", "CID 408008/409328",
      "REFS_BEFORE=21581（须实测宿主当前 ROW_MINE＝22902）"]),
    ("_READ_TASK_fhk_b072.md", ["BLIND 数", "候选数", "claim 号段"]),
    ("_NARR_TASK_fhk_b072.md", ["候选数", "分片条数分布", "claim 号段"]),
]:
    print("  %-32s %s" % (dst, "; ".join(items) if items else "无"))
