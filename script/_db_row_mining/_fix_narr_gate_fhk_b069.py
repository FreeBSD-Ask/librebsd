# -*- coding: utf-8 -*-
"""fhk_b069 合并门禁违规外科修复（第二版）。

第一版 bug：FIX 列表里同一 part 出现多次，循环每轮重新读盘并把
changes[part] 覆盖，导致同一片里先前的替换全部丢失。本版按 part 聚合，
每片只读一次、只写一次，且对「已被上一版修好」的条目幂等跳过。
"""
import collections
import io
import os

LO_LEN, HI_LEN = 60, 140
HOST = "885"
TRAIL = set("。，、；：？！…—．·~-.,;:?! ")
FORBID = set(chr(c) for c in (0x300c, 0x300d, 0x2018, 0x2019, 0x201c, 0x201d,
                              0x0027, 0x0022, 0x0060, 0x002a, 0x005c, 0x007c))

HERE = os.path.dirname(os.path.abspath(__file__))
RL = os.path.join(HERE, "review_logs")

# (part, pk, old_sub, new_sub)
FIX = [
    ("2", 2594477, "自 1994 年起", "自九四年起"),
    ("3", 2594499, "在 1989 年写过", "在八九年写过"),
    ("14", 2594960, "自 1994 年起", "自九四年起"),
    ("14", 2594961,
     "约 1994 年在 sandia 建过一个基于 FreeBSD 的集群",
     "约九四年间在 sandia 建过一个基于 FreeBSD 的集群 年份他还在当场向 russell 求证"),
    ("6", 2594648,
     "J Wunsch 追问 CVSup 15.2 修正异常权限时是否也把文件创建即缺失的组写权限一并补上，并称此修正结果令人满意",
     "J Wunsch 追问此前文件创建时缺失组写权限的问题如今是否已彻底解决，确认不再出现该情形后表示非常满意，认为这确实是个不错的改进结果"),
    ("32", 2595635, "3.3.1 分发包", "XF86331 分发包"),
    ("33", 2595679, "2.2.2-STABLE", "2.2-STABLE"),
    ("33", 2595687, "在 FreeBSD 2.2.1 上使用", "在 2.2.1 上使用"),
    ("33", 2595688, "跟进 FreeBSD 2.2.2 中的", "跟进其 FreeBSD 系统中的"),
    ("42", 2596063, "跑 FreeBSD 2.2.5-RELEASE", "跑 2.2.5-RELEASE"),
]


def part_path(part):
    return os.path.join(RL, "fhk_b069_mount_narr_p%s.tsv" % part)


def check_nar(pk, nar):
    assert LO_LEN <= len(nar) <= HI_LEN, "p%s len %d 越界" % (pk, len(nar))
    assert not set(nar) & FORBID, "p%s 含禁字符" % pk
    assert nar[-1] not in TRAIL, "p%s 尾标点 %r" % (pk, nar[-1])
    assert not nar[:1].isdigit(), "p%s 数字开头" % pk
    assert "\t" not in nar and "\n" not in nar, "p%s 含制表换行" % pk


by_part = collections.OrderedDict()
for part, pk, old, new in FIX:
    by_part.setdefault(part, []).append((pk, old, new))

changed_parts = []
for part, entries in by_part.items():
    path = part_path(part)
    with io.open(path, "r", encoding="utf-8", newline="") as fh:
        rows = [ln.rstrip("\n") for ln in fh.read().split("\n") if ln.strip()]

    applied = skipped = 0
    for pk, old, new in entries:
        hit = 0
        for i, ln in enumerate(rows):
            f = ln.split("\t")
            assert len(f) == 3, "p%s 字段异常" % part
            if f[0] == str(pk):
                if old in f[2]:
                    assert f[2].count(old) == 1, "p%s pk%s old 出现 %d 次" % (part, pk, f[2].count(old))
                    f[2] = f[2].replace(old, new)
                    applied += 1
                    label = "改"
                else:
                    assert new in f[2], "p%s pk%s 既无 old 也无 new（状态不明）" % (part, pk)
                    skipped += 1
                    label = "幂等跳过（上版已修）"
                assert f[1] == HOST, "p%s 宿主异常" % part
                check_nar(pk, f[2])
                rows[i] = "\t".join(f)
                print("[%s] p%s pk=%s len=%d" % (label, part, pk, len(f[2])))
                hit += 1
        assert hit == 1, "p%s pk%s 命中 %d 行（应为 1）" % (part, pk, hit)

    if applied:
        changed_parts.append(part)
        with io.open(path + ".tmpw", "w", encoding="utf-8", newline="") as fh:
            fh.write("\n".join(rows) + "\n")
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(path + ".tmpw", path)

print("-" * 72)
print("本轮改写片: %s" % (changed_parts or "无（全部已修）"))

# ---- 独立回读核验（全 50 片）----
print("=" * 72)
tot = 0
prob = []
for k in range(1, 51):
    pth = part_path("%02d" % k) if os.path.exists(part_path("%02d" % k)) else part_path("%d" % k)
    assert os.path.exists(pth), "缺片 %s" % pth
    rb = open(pth, "rb").read()
    with io.open(pth, "r", encoding="utf-8", newline="") as fh:
        raw = fh.read().split("\n")
    rows = [x for x in raw if x.strip()]
    tot += len(rows)
    for ln in rows:
        f = ln.split("\t")
        if len(f) != 3 or f[1] != HOST:
            prob.append((os.path.basename(pth), ln[:40], "字段"))
        else:
            try:
                check_nar(f[0], f[2])
            except AssertionError as e:
                prob.append((os.path.basename(pth), f[0], str(e)))
    if b"\r" in rb:
        prob.append((os.path.basename(pth), "", "CR"))
    if rb.startswith(b"\xef\xbb\xbf"):
        prob.append((os.path.basename(pth), "", "BOM"))
    if not rb.endswith(b"\n"):
        prob.append((os.path.basename(pth), "", "缺尾LF"))
print("总条数 %d（期望 1362）" % tot)
print("问题:", prob if prob else "NONE")
