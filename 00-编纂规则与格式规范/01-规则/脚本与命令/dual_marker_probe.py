# 先导样本探针（T007）：P-1 括注配对／P-2 引号合规／P-3 形制合规／P-4 编号可复算／
# P-5 改动边界（仅插入）／P-6 旧式未受影响。含 --self-test 负向自检。
# 用法: --file <路径(相对 05-卷册大纲)> | --all | --self-test
import csv
import re
import sys
from pathlib import Path

ROOT = Path(r"D:\librebsd")
STG = ROOT / "script/_staging/pilot_samples_20260930"
SNAP = STG / "snapshots"
OUTLINE = ROOT / "05-卷册大纲"
RANKS = {}          # id -> rank
for r in csv.DictReader((STG / "rank_table.def.csv").open(encoding="utf-8")):
    RANKS[int(r["id"])] = int(r["rank"])

MARKER_RE = re.compile(r"\u3014DX-(\d{4})\uff0fid(\d+)\u3015")   # 〔DX-nnnn／idN〕
BARE_DX_RE = re.compile(r"DX-\d{4}")
OLD_D_RE = re.compile(r"D-\d+")
RAQ = "\u300c\u300d\u300e\u300f"                                  # 「」『』


def load(rel):
    cur = (OUTLINE / rel).read_text(encoding="utf-8")
    snap_p = SNAP / rel.replace("/", "__")
    old = snap_p.read_text(encoding="utf-8") if snap_p.exists() else None
    return cur, old


def probe(rel):
    """返回 (ok, [FAIL 明细])。"""
    cur, old = load(rel)
    fails = []
    # P-1 括注配对
    if cur.count("\u3014") != cur.count("\u3015"):
        fails.append(f"P-1 FAIL: 〔 {cur.count(chr(0x3014))} ≠ 〕 {cur.count(chr(0x3015))}")
    # P-2 引号合规（与快照比不新增）
    if old is not None and sum(cur.count(c) for c in RAQ) != sum(old.count(c) for c in RAQ):
        fails.append(f"P-2 FAIL: 直角引号数变化 {sum(old.count(c) for c in RAQ)} -> {sum(cur.count(c) for c in RAQ)}")
    # P-3 形制合规：每个 DX-nnnn 都在完整标记内
    n_bare = len(BARE_DX_RE.findall(cur))
    n_marked = len(MARKER_RE.findall(cur))
    if n_bare != n_marked:
        fails.append(f"P-3 FAIL: 裸 DX-nnnn {n_bare} 处 ≠ 完整标记 {n_marked} 处")
    # P-4 编号可复算
    for m in MARKER_RE.finditer(cur):
        rank, did = int(m.group(1)), int(m.group(2))
        if RANKS.get(did) != rank:
            fails.append(f"P-4 FAIL: 标记 {m.group(0)} 复算不符（id {did} 实际秩位 {RANKS.get(did)}）")
    # P-5 改动边界：仅插入标记（删除标记后应与快照逐字相同）
    if old is not None:
        recon = cur
        for m in set(MARKER_RE.findall(cur)):
            recon = recon.replace("\u3014DX-%s\uff0fid%s\u3015" % m, "")
        if recon != old:
            fails.append("P-5 FAIL: 与快照差异不止『新增标记』（存在改写或删除）")
    # P-6 旧式未受影响
    if old is not None and len(OLD_D_RE.findall(cur)) != len(OLD_D_RE.findall(old)):
        fails.append(f"P-6 FAIL: 旧式 D-n 条目数变化 {len(OLD_D_RE.findall(old))} -> {len(OLD_D_RE.findall(cur))}")
    return (not fails), fails


def run_all():
    ok_all = True
    for snap in sorted(SNAP.glob("*")):
        rel = snap.name.replace("__", "/")
        if not (OUTLINE / rel).exists():
            continue
        ok, fails = probe(rel)
        tag = "PASS" if ok else "FAIL"
        print(f"[{tag}] {rel}")
        for f in fails:
            print("   ", f)
        ok_all = ok_all and ok
    print("ALL PASS" if ok_all else "HAS FAIL")
    return 0 if ok_all else 1


def self_test():
    """负向自检：构造不合规样本，探针必须报 FAIL。"""
    tmp = OUTLINE / "_pilot_selftest_tmp.md"
    results = []

    def expect_fail(name, text, checks=("P-1", "P-2", "P-3", "P-4", "P-5", "P-6")):
        tmp.write_text(text, encoding="utf-8", newline="\n")
        snap_p = SNAP / "_pilot_selftest_tmp.md"
        snap_p.write_text("基线文本。\n", encoding="utf-8", newline="\n")
        ok, fails = probe("_pilot_selftest_tmp.md")
        hit = [c for c in checks if any(f.startswith(c) for f in fails)]
        results.append((name, ok, hit, fails))
        snap_p.unlink()

    expect_fail("括注不配对", "文本〔DX-0001／id1 缺右括号\n", checks=("P-1", "P-3", "P-4", "P-5"))
    expect_fail("裸编号无括号", "文本 DX-0001 无括号\n", checks=("P-3", "P-5"))
    expect_fail("秩位伪造", "文本〔DX-9999／id1〕伪造秩位\n", checks=("P-3", "P-4", "P-5"))
    expect_fail("改写既有文字", "文本〔DX-0001／id1〕被改写。\n", checks=("P-3", "P-4", "P-5"))
    expect_fail("新增直角引号", "文本〔DX-0001／id1〕「新增」引号\n", checks=("P-2", "P-3", "P-4", "P-5"))
    expect_fail("删除旧式条目", "", checks=("P-5", "P-6"))
    tmp.unlink(missing_ok=True)

    all_hit = True
    print("== 负向自检（期望每项 FAIL 且命中预期探针）==")
    for name, ok, hit, fails in results:
        status = "OK" if (not ok and hit) else "MISS"
        if ok or not hit:
            all_hit = False
        print(f"[{status}] {name}: probe={'PASS(误!)' if ok else 'FAIL'} 命中={hit or fails}")
    print("SELF-TEST PASS" if all_hit else "SELF-TEST FAIL")
    return 0 if all_hit else 1


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    if "--all" in sys.argv:
        sys.exit(run_all())
    if "--file" in sys.argv:
        rel = sys.argv[sys.argv.index("--file") + 1]
        ok, fails = probe(rel)
        print(("PASS" if ok else "FAIL"), rel)
        for f in fails:
            print("  ", f)
        sys.exit(0 if ok else 1)
    print(__doc__)
    sys.exit(2)
