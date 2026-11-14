#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""audit_subsection_design.py —— 小节设计台账一致性门禁（第三十八件，固定脚本）。

对 `05-卷册大纲/` 的第四级（小节）设计链做一致性审计（ADR-0020，2026-11-06 Task 5.4a 立）：

  D1  outline ↔ 设计台账双射：`目录/data/outline.txt` 小节行 ↔ `映射/design/V{NN}.tsv`
      台账行，键＝（卷, M, N, P）；有行无账（设计级未冻结）与有账无行（游离）均 FAIL。
  D2  设计台账 ↔ 树内 .md 双射：台账每键须有对应 `M.N.P-*.md`（在对应节目录下）；
      树多 .md 而无台账行亦 FAIL（"每小节必须有 .md"，含空骨架；无"设计级豁免"）。
  L   落盘批准标记：有设计台账且该卷树内小节 .md >0 的卷，须有
      `映射/title-design/approved/V{NN}.land.ok`（kind=landing）；无标记不落盘。

与其他门禁的分工（判据不重复）：
  * 题名形态／四源覆盖／证据齐／title.ok hash／例外登记 → 第三十九件
    `audit_title_consistency.py`（其 E／F／H／I 组）；
  * outline ↔ 树 .md ↔ SUMMARY 三向双射 → 第三十七件 L19；
  * 本件只管**设计台账**这一层的双射与落盘批准。

零态合法：无 outline 小节行且无 design 台账（V*.tsv）时各判据零工作集，PASS。
表头违约（design 台账缺必备列）exit 2。

用法：
  python audit_subsection_design.py                # 默认检查（退出码 0/1/2）
  python audit_subsection_design.py --root <大纲根> --map <映射层>
  python audit_subsection_design.py --selftest     # 合成夹具自检（含负向注入）

依赖：仅标准库。
"""
from __future__ import annotations

import argparse
import os
import re
import sys
import tempfile

sys.stdout.reconfigure(encoding="utf-8")

DEFAULT_ROOT = os.path.join("05-卷册大纲")
VOL_RE = re.compile(r"^第(\d{1,3})卷(?:-(?P<slug>.+))?$")
CH_RE = re.compile(r"^第(\d{1,3})章(?:-(?P<slug>.+))?$")
SEC_RE = re.compile(r"^(\d{1,3})\.(\d{1,3})-(?P<slug>.+)$")
SUB_RE = re.compile(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,4})-(?P<slug>.+\.md)$")
CN2 = "一二三四五六七八九十"
DESIGN_COLS = {"subsection_id", "vol", "chapter", "section", "title", "order"}


def _cn2int(s):
    """中文数字 → int（1—99；阿拉伯直返；失败 None）。"""
    if s.isdigit():
        return int(s)
    if s in CN2:
        return CN2.index(s) + 1
    if s == "十":
        return 10
    if s.startswith("十"):
        return 10 + CN2.index(s[1]) + 1
    if "十" in s:
        a, _, b = s.partition("十")
        if a in CN2 and b in CN2:
            return (CN2.index(a) + 1) * 10 + (CN2.index(b) + 1 if b else 0)
    return None


def _read_tsv(path):
    """读 TSV → [dict]；文件缺返回 None；空返回 []。"""
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as fh:
        lines = [ln.rstrip("\r\n") for ln in fh if ln.strip()]
    if not lines:
        return []
    head = lines[0].split("\t")
    return [dict(zip(head, (ln.split("\t") + [""] * len(head))[:len(head)]))
            for ln in lines[1:]]


def outline_sub_keys(outline_path):
    """outline.txt → {卷号: set((M, N, P))}（小节行，两前导空格＋`- M.N.P 题名`）。"""
    by_vol: dict = {}
    v = None
    with open(outline_path, encoding="utf-8") as fh:
        for raw in fh:
            line = raw.rstrip("\r\n").rstrip()
            if not line.strip():
                continue
            if line.startswith("## "):
                continue
            if line.startswith("# "):
                mv = re.match(r"^#\s*第\s*([一二三四五六七八九十]+)卷", line)
                v = _cn2int(mv.group(1)) if mv else None
                continue
            ms = re.match(r"^  -\s+(\d{1,3})\.(\d{1,3})\.(\d{1,4})\s", line)
            if ms and v is not None:
                by_vol.setdefault(v, set()).add(
                    (int(ms.group(1)), int(ms.group(2)), int(ms.group(3))))
    return by_vol


def tree_sub_keys(root):
    """树扫描 → {卷号: set((M, N, P))}（小节 .md 文件名前缀；.gitkeep 不计）。"""
    by_vol: dict = {}
    if not os.path.isdir(root):
        return by_vol
    for vname in sorted(os.listdir(root)):
        vfull = os.path.join(root, vname)
        if not os.path.isdir(vfull) or not VOL_RE.match(vname):
            continue
        vn = int(VOL_RE.match(vname).group(1))
        for cname in sorted(os.listdir(vfull)):
            cfull = os.path.join(vfull, cname)
            if not os.path.isdir(cfull) or not CH_RE.match(cname):
                continue
            for sname in sorted(os.listdir(cfull)):
                sfull = os.path.join(cfull, sname)
                if not os.path.isdir(sfull) or not SEC_RE.match(sname):
                    continue
                for f in sorted(os.listdir(sfull)):
                    if f == ".gitkeep" or not f.endswith(".md"):
                        continue
                    mm = SUB_RE.match(f)
                    if mm:
                        by_vol.setdefault(vn, set()).add(
                            (int(mm.group(1)), int(mm.group(2)), int(mm.group(3))))
    return by_vol


def design_sub_keys(mapdir):
    """设计台账 → ({卷号: set((M,N,P))}, 违约列表)。缺台账的卷不出现在首表。"""
    by_vol: dict = {}
    bad = []
    ddir = os.path.join(mapdir, "design")
    if not os.path.isdir(ddir):
        return by_vol, bad
    for fn in sorted(os.listdir(ddir)):
        mm = re.match(r"^V(\d{1,3})\.tsv$", fn)
        if not mm:
            continue
        vn = int(mm.group(1))
        rows = _read_tsv(os.path.join(ddir, fn))
        if rows is None:
            continue
        if rows:
            miss = DESIGN_COLS - set(rows[0].keys())
            if miss:
                bad.append("V%03d 台账缺列 %s" % (vn, sorted(miss)))
                continue
        for r in rows:
            sid = (r.get("subsection_id") or "").strip()
            m3 = re.match(r"^V\d+\.(\d+)\.(\d+)\.(\d+)$", sid)
            if m3:
                by_vol.setdefault(vn, set()).add((int(m3.group(1)), int(m3.group(2)),
                                                  int(m3.group(3))))
            else:
                bad.append("V%03d subsection_id 形制非法：%s" % (vn, sid[:30]))
    return by_vol, bad


def land_ok_vols(approved_dir):
    """有 kind=landing 标记的卷号集合（V{NN}.land.ok）。"""
    out = set()
    if not os.path.isdir(approved_dir):
        return out
    for fn in sorted(os.listdir(approved_dir)):
        mm = re.match(r"^V(\d{1,3})\.land\.ok$", fn)
        if not mm:
            continue
        try:
            with open(os.path.join(approved_dir, fn), encoding="utf-8") as fh:
                if any(ln.strip().lower().startswith("kind=landing")
                       for ln in fh):
                    out.add(int(mm.group(1)))
        except OSError:
            pass
    return out


def run_gate(root, mapdir):
    """执行 D1／D2／L，返回 [(判据, 结果, 说明)]。"""
    outline_p = os.path.join(root, "目录", "data", "outline.txt")
    approved_dir = os.path.join(mapdir, "title-design", "approved")
    if not os.path.exists(outline_p):
        print("FATAL 缺 %s（四级 outline 真值）" % outline_p)
        raise SystemExit(2)
    okeys = outline_sub_keys(outline_p)
    tkeys = tree_sub_keys(root)
    dkeys, dbad = design_sub_keys(mapdir)
    lands = land_ok_vols(approved_dir)
    res = []

    def add(no, ok, detail):
        res.append((no, "PASS" if ok else "FAIL", detail))

    all_vols = sorted(set(okeys) | set(dkeys) | set(tkeys))
    if not all_vols and not dbad:
        add("D1", True, "零态：无 outline 小节行、无设计台账")
        add("D2", True, "零态：树内无小节 .md")
        add("L", True, "零态：无落盘卷")
        return res

    # D1 outline ↔ 设计台账
    d1_bad = []
    for vn in all_vols:
        ov, dv = okeys.get(vn, set()), dkeys.get(vn, set())
        if not ov and not dv:
            continue
        if ov and not dv:
            d1_bad.append("V%03d 有 %d 行无台账" % (vn, len(ov)))
        elif dv and not ov:
            d1_bad.append("V%03d 台账 %d 行无 outline 行" % (vn, len(dv)))
        elif ov != dv:
            d1_bad.append("V%03d 差集 outline-台账=%s 台账-outline=%s"
                          % (vn, sorted(ov - dv)[:3], sorted(dv - ov)[:3]))
    add("D1", not d1_bad and not dbad,
        "vols=%d ghost=%d orphan=%d%s"
        % (len(all_vols), len([x for x in d1_bad if "无台账" in x]),
           len([x for x in d1_bad if "无 outline" in x]),
           "" if not dbad else " 违约=%s" % dbad[:2]))

    # D2 设计台账 ↔ 树内 .md
    d2_bad = []
    for vn in all_vols:
        dv, tv = dkeys.get(vn, set()), tkeys.get(vn, set())
        if not dv and not tv:
            continue
        if dv and dv != tv:
            d2_bad.append("V%03d 台账-树=%s 树-台账=%s"
                          % (vn, sorted(dv - tv)[:3], sorted(tv - dv)[:3]))
        elif not dv and tv and vn in okeys:
            d2_bad.append("V%03d 树 %d 件无台账" % (vn, len(tv)))
    add("D2", not d2_bad, "vols=%d mismatch=%d" % (len(all_vols), len(d2_bad)))

    # L 落盘批准标记
    l_bad = []
    for vn in all_vols:
        if dkeys.get(vn) and tkeys.get(vn) and vn not in lands:
            l_bad.append("V%03d" % vn)
    add("L", not l_bad, "需 land.ok 卷=%d 缺=%s" % (len(lands), l_bad[:5]))
    return res


# ---------------------------------------------------------------- selftest

def _mk(path, text=""):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def build_fixture(base):
    """合成夹具：1 卷 1 章 1 节 2 小节（outline＋design 台账＋树 .md＋land.ok 三向对齐）。"""
    root = os.path.join(base, "05-卷册大纲")
    mapdir = os.path.join(root, "映射")
    _mk(os.path.join(root, "目录", "data", "outline.txt"),
        "# 第一卷  合成甲\n"
        "## 第 1 章 甲一\n"
        "- 1.1 甲一节\n"
        "  - 1.1.1 甲一一\n"
        "  - 1.1.2 甲一二\n")
    _mk(os.path.join(root, "第01卷-合成甲", "第1章-甲一", "1.1-甲一节", "1.1.1-甲一一.md"),
        "# 1.1.1 甲一一\n")
    _mk(os.path.join(root, "第01卷-合成甲", "第1章-甲一", "1.1-甲一节", "1.1.2-甲一二.md"),
        "# 1.1.2 甲一二\n")
    _mk(os.path.join(mapdir, "design", "V01.tsv"),
        "subsection_id\tvol\tchapter\tsection\ttitle\torder\n"
        "V01.1.1.1\t01\t1\t1\t甲一一\t1\n"
        "V01.1.1.2\t01\t1\t1\t甲一二\t2\n")
    _mk(os.path.join(mapdir, "title-design", "approved", "V01.land.ok"),
        "kind=landing\nvol=V01\n")
    return root, mapdir


def selftest():
    """合成夹具全 PASS ＋ 四类负向注入必 FAIL。"""
    base = tempfile.mkdtemp(prefix="subsec_design_")
    ok, bad = [], []

    def check(name, cond, detail=""):
        (ok if cond else bad).append("%s %s" % (name, detail))

    try:
        root, mapdir = build_fixture(base)
        r = run_gate(root, mapdir)
        fails = [x for x in r if x[1] == "FAIL"]
        check("正例全 PASS", not fails, "%d 项 FAIL %s" % (len(fails), fails))

        # 负向 1：outline 幽灵小节行（有行无台账＝设计级）
        _mk(os.path.join(root, "目录", "data", "outline.txt"),
            open(os.path.join(root, "目录", "data", "outline.txt"), encoding="utf-8").read()
            + "  - 1.1.3 幽灵\n")
        check("负向 D1 幽灵行", run_gate(root, mapdir)[0][1] == "FAIL")
        _mk(os.path.join(root, "目录", "data", "outline.txt"),
            open(os.path.join(root, "目录", "data", "outline.txt"), encoding="utf-8").read()
            .replace("  - 1.1.3 幽灵\n", ""))

        # 负向 2：树缺 .md（台账有行而 .md 被删）
        miss = os.path.join(root, "第01卷-合成甲", "第1章-甲一", "1.1-甲一节", "1.1.2-甲一二.md")
        tmp = miss + ".tmp"
        os.rename(miss, tmp)
        check("负向 D2 缺 .md", run_gate(root, mapdir)[1][1] == "FAIL")
        os.rename(tmp, miss)

        # 负向 3：台账游离行（.md 与 outline 均无）
        _mk(os.path.join(mapdir, "design", "V01.tsv"),
            "subsection_id\tvol\tchapter\tsection\ttitle\torder\n"
            "V01.1.1.1\t01\t1\t1\t甲一一\t1\n"
            "V01.1.1.2\t01\t1\t1\t甲一二\t2\n"
            "V01.1.1.9\t01\t1\t1\t游离\t9\n")
        r3 = run_gate(root, mapdir)
        check("负向 D2 游离台账行", r3[1][1] == "FAIL")

        # 负向 4：缺 land.ok（有台账有落盘）
        _mk(os.path.join(mapdir, "design", "V01.tsv"),
            "subsection_id\tvol\tchapter\tsection\ttitle\torder\n"
            "V01.1.1.1\t01\t1\t1\t甲一一\t1\n"
            "V01.1.1.2\t01\t1\t1\t甲一二\t2\n")
        lk = os.path.join(mapdir, "title-design", "approved", "V01.land.ok")
        ltmp = lk + ".tmp"
        os.rename(lk, ltmp)
        check("负向 L 缺 land.ok", run_gate(root, mapdir)[2][1] == "FAIL")
        os.rename(ltmp, lk)
    finally:
        pass

    for x in ok:
        print("  [PASS]", x)
    for x in bad:
        print("  [FAIL]", x)
    print("自检 %d 项，失败 %d 项" % (len(ok) + len(bad), len(bad)))
    return 1 if bad else 0


def main(argv=None):
    ap = argparse.ArgumentParser(description="小节设计台账一致性门禁（第三十八件）")
    ap.add_argument("--root", default=DEFAULT_ROOT, help="大纲树根（默认 05-卷册大纲）")
    ap.add_argument("--map", default=None, help="映射层目录（默认 <root>/映射）")
    ap.add_argument("--check", action="store_true", help="只读检查（默认行为）")
    ap.add_argument("--selftest", action="store_true", help="合成夹具自检")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    mapdir = a.map or os.path.join(a.root, "映射")
    print("小节设计台账一致性门禁（第三十八件）")
    res = run_gate(a.root, mapdir)
    n_fail = 0
    for no, st, detail in res:
        print("  %s %s %s" % (st, no, detail))
        n_fail += 1 if st == "FAIL" else 0
    print("合计 %d 条：PASS %d／FAIL %d"
          % (len(res), len(res) - n_fail, n_fail))
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
