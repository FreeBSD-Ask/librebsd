# -*- coding: utf-8 -*-
"""大纲注入块「证据等级」门禁（2026-09-14 立，第六件改后必跑门禁）

用途：审计 `05-卷册大纲/` 全部 md 中注入块头的 `（证据等级：Lx，来源：`db.table.id`）`
标注是否与其引用项的真实等级一致。**凡引用 `historical_claims.duckdb.claim` 者一律严格核验**
（该库 `claim.evidence_level` 为逐条真值）；其余来源库无逐条等级字段者仅作族内分布报告，
不作 PASS/FAIL 判定。

设立缘由：2026-09-14 主控核查发现全库 439 处块头等级错标（全部为 L3 被块脚本模板写死为
`证据等级：L4`），波及 list12/16/18/19/23/38/40/41/44 共 69 个宿主文件。根因＝模板字面常量，
且缺两道断言门禁。此门禁即该缺陷的常设阻断措施。

判定口径：
  FAIL（退出码 1）：任一块头等级 ≠ 所引 claim 的真实等级；或所引 claim 号在库中不存在。
  INFO（不影响退出码）：非 claim 来源族的族内等级为单一值（提示可能为按族约定而非逐条判定）。

用法：
  python audit_evidence_level_labels.py            # 全库审计
  python audit_evidence_level_labels.py --verbose  # 附错标明细（前 40 条）
"""
import glob
import io
import os
import re
import sys
from collections import Counter, defaultdict

import duckdb

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))   # D:\librebsd
OUTLINE = os.path.join(ROOT, "05-卷册大纲")
HC = os.path.join(ROOT, "04-现代研究文献", "historical_claims.duckdb")

HDR = re.compile(r"（证据等级：(L[0-9])，来源：`([a-zA-Z0-9\-_]+)\.duckdb\.([^`]+)`")
CLAIM_HDR = re.compile(
    r"（证据等级：(L[0-9])，来源：`historical_claims\.duckdb\.claim\.([^`]+)`")


def main():
    verbose = "--verbose" in sys.argv
    if not os.path.isdir(OUTLINE):
        print("找不到大纲目录：%s" % OUTLINE)
        return 2

    con = duckdb.connect(HC, read_only=True)
    try:
        levels = {str(k): v for k, v in
                  con.execute("select claim_id, evidence_level from claim").fetchall()}
    finally:
        con.close()

    files = sorted(glob.glob(os.path.join(OUTLINE, "**", "*.md"), recursive=True))
    n_claim = 0
    n_ok = 0
    bad = []
    per_file = Counter()
    fam = defaultdict(Counter)

    for path in files:
        try:
            txt = io.open(path, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        for m in HDR.finditer(txt):
            fam[m.group(2)][m.group(1)] += 1
        for tag, cid in CLAIM_HDR.findall(txt):
            n_claim += 1
            real = levels.get(cid)
            if real is None:
                bad.append((path, cid, tag, "库中无此 claim 号"))
                per_file[os.path.basename(path)] += 1
            elif real != tag:
                bad.append((path, cid, tag, real))
                per_file[os.path.basename(path)] += 1
            else:
                n_ok += 1

    print("大纲 md 文件数：%d" % len(files))
    print("引用 historical_claims 的块头：%d" % n_claim)
    print("  等级与库中真值一致：%d" % n_ok)
    print("  错标／悬空：%d" % len(bad))
    if bad and verbose:
        print("\n错标明细（前 40 条）：")
        for p, cid, tag, real in bad[:40]:
            print("  %-52s %s 标签=%s 真值=%s" % (os.path.basename(p)[:50], cid, tag, real))
    if per_file:
        print("\n错标集中文件：")
        for k, v in per_file.most_common(12):
            print("  %-60s %d" % (k[:58], v))

    print("\n按来源库的等级分布（族内单一值者为 INFO，非 FAIL）：")
    for db in sorted(fam, key=lambda d: -sum(fam[d].values())):
        c = fam[db]
        n = sum(c.values())
        dist = " ".join("%s=%d" % (k, v) for k, v in sorted(c.items()))
        mark = "  [INFO 单一等级]" if len(c) == 1 and n >= 50 else ""
        print("  %-22s %7d  %s%s" % (db, n, dist, mark))

    print()
    if bad:
        print("判定：FAIL（%d 处块头等级与库中真值不符）" % len(bad))
        return 1
    print("判定：PASS（claim 引用块头等级与库中真值全部一致）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
