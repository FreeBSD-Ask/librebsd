#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fhk_b062 -> fhk_b063 全链克隆器（只改批次坐标，不改口径）。"""
import io, os
HERE = os.path.dirname(os.path.abspath(__file__))
NL = chr(10)
REPLS = [
    ("124000", "126000"),  # rn_hi
    ("122001", "124001"),  # rn_lo
    ("122000", "124000"),  # offset
    ("2580330", "2582341"),  # pk_lo
    ("2582340", "2584356"),  # pk_hi
    ("b062", "b063"),
    ("b061", "b062"),  # prev-batch ref
    ("span 2011", "span 2016"),
    ("跨度 2011", "跨度 2016"),
    ("2011 个编号", "2016 个编号"),
    ("缺 11", "缺 16"),
    ("11 跳号", "16 跳号"),
    ("11 个编号", "16 个编号"),
    ("len(tags) == 61", "len(tags) == 62"),
    ("range(1, 62)", "range(1, 63)"),
    ("n_recs == 61", "n_recs == 62"),
    ("tags 61 条", "tags 62 条"),
]
MIS_OLD_CSV = "2580608, 2580848, 2580920, 2581110, 2581272, 2581300, 2581352, 2581699, 2581774, 2581860, 2581885"
MIS_NEW_CSV = ("2582801, 2583024, 2583025, 2583026, 2583027, 2583028, 2583029, 2583030, 2583031, 2583032, "
               "2583553, 2583646, 2583829, 2583833, 2583834, 2583934")
MIS_OLD_SLASH = "2580608/2580848/2580920/2581110/2581272/2581300/2581352/2581699/2581774/2581860/2581885"
MIS_NEW_SLASH = ("2582801/2583024/2583025/2583026/2583027/2583028/2583029/2583030/2583031/2583032/"
                 "2583553/2583646/2583829/2583833/2583834/2583934")
F = chr(0xff0f)
MIS_OLD_FSLASH = F.join(["2580608","2580848","2580920","2581110","2581272","2581300","2581352","2581699","2581774","2581860","2581885"])
MIS_NEW_FSLASH = F.join(["2582801","2583024","2583025","2583026","2583027","2583028","2583029","2583030","2583031","2583032","2583553","2583646","2583829","2583833","2583834","2583934"])
JOBS = [
    ("_digest_fhk_b062.py", "_digest_fhk_b063.py"),
    ("_blind_fhk_b062.py", "_blind_fhk_b063.py"),
    ("_part_split_b062.py", "_part_split_b063.py"),
    ("_READ_TASK_fhk_b062.md", "_READ_TASK_fhk_b063.md"),
    ("_register_fhk_b062.py", "_register_fhk_b063.py"),
    ("_claimmap_fhk_b062.py", "_claimmap_fhk_b063.py"),
    ("_gen_narrpkg_b062.py", "_gen_narrpkg_b063.py"),
    ("_merge_narr_fhk_b062.py", "_merge_narr_fhk_b063.py"),
    ("_outline_fhk_b062.py", "_outline_fhk_b063.py"),
    ("_ledger_b062.py", "_ledger_b063.py"),
    ("_backup_claims_b062.py", "_backup_claims_b063.py"),
    ("_chk_cand_b062.py", "_chk_cand_b063.py"),
    ("_gen_hostkeys_b062.py", "_gen_hostkeys_b063.py"),
    ("_NARR_TASK_fhk_b062.md", "_NARR_TASK_fhk_b063.md"),
]
for src, dst in JOBS:
    p = os.path.join(HERE, src)
    if not os.path.exists(p):
        print("  MISSING %s" % src); continue
    s = io.open(p, encoding="utf-8").read()
    n = s
    for a, b in REPLS:
        n = n.replace(a, b)
    n = n.replace(MIS_OLD_CSV, MIS_NEW_CSV)
    n = n.replace(MIS_OLD_SLASH, MIS_NEW_SLASH)
    n = n.replace(MIS_OLD_FSLASH, MIS_NEW_FSLASH)
    # Also replace tag references in filenames within scripts
    n = n.replace("fhk_b062", "fhk_b063")
    out = os.path.join(HERE, dst)
    io.open(out, "w", encoding="utf-8", newline=NL).write(n)
    print("  OK %s" % dst)
print("done")
