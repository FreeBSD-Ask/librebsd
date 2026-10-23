# -*- coding: utf-8 -*-
"""大纲重复锚与重复块门禁（第三十五件）。

对象：`05-卷册大纲/` 树内 `.md`（根级件不计）。判据：

- A 同文件同锚重复：同一文件内同一 `ROW_MINE` 锚 ID 出现 ≥2 次 → FAIL。
- B 同文件同小节整块重复：同一文件、同一最近上级标题之下，两个“锚行起的块”
  整段逐字相同（块 = 锚行 → 下一锚行／标题／文件尾，去尾部空行）→ FAIL。
  块哈希覆盖锚行、说明行与正文，故同锚不同正文（如 DEEP_ANALYSIS 各挂不同 claim）
  不会相撞。
- C 跨文件同名锚：同一锚 ID 出现在 ≥2 个文件 → 只记 INFO 计数，不判 FAIL
  （各节独立引用同一史料属既有体例，P2／P3 已裁定不作删除）。

退出码：0 全 PASS／1 任一 A 或 B 命中／2 根缺失。
`--csv` 落明细；`--selftest` 内建七例并逐例校验退出码。
"""
import argparse
import hashlib
import re
import sys
import tempfile
from collections import Counter, defaultdict
from pathlib import Path

ROW_MINE = re.compile(r"^<!--\s*ROW_MINE:\s*([^\s>]+)\s*-->\s*$")
DEEP_OPEN = re.compile(r"^<!--\s*DEEP_ANALYSIS(?!\s*/)\s*(?::\s*([^\s>]+))?\s*-->$")
HEAD = re.compile(r"^#{1,6}\s")
ANY_ANCHOR = re.compile(r"^<!--\s*(ROW_MINE|DEEP_ANALYSIS)(?!\s*/)")

ROOT_DEFAULT = Path(__file__).resolve().parents[3] / "05-卷册大纲"


def scan(root):
    """返回（A 违例, B 违例, C 计数, 统计）。只读。"""
    a_bad, b_bad, b2_info = [], [], []
    anchor_files = defaultdict(set)
    files = 0
    anchors = 0

    for p in sorted(root.rglob("*.md")):
        rel = p.relative_to(root).as_posix()
        # 2026-10-23 搬迁批：目录源（号文）与历史映射参考不是大纲内容树，不进本门禁面。
        if rel.split("/")[0] in ("目录", "映射"):
            continue
        if "/" not in rel:            # 根级总览等不计
            continue
        files += 1
        lines = p.read_text(encoding="utf-8", errors="replace").split("\n")

        # 标记每个锚行的位置、ID、类型与所在小节
        section = "(文件首)"
        spans, row_spans = [], []
        for i, ln in enumerate(lines):
            s = ln.strip()
            if HEAD.match(s):
                section = s
                continue
            m_row = ROW_MINE.match(s)
            if m_row:
                anchors += 1
                spans.append((i, m_row.group(1), section))
                row_spans.append((i, m_row.group(1), section))
                anchor_files[m_row.group(1)].add(rel)
                continue
            m_deep = DEEP_OPEN.match(s)
            if m_deep:
                anchors += 1
                # DEEP_ANALYSIS 单标记无唯一 ID，不参与 A；其重复由 B／B2 判
                spans.append((i, m_deep.group(1) or "(无名)", section))

        # A：同文件同 ROW_MINE 锚 ≥2（DEEP_ANALYSIS 单标记不计）
        by_anchor = defaultdict(list)
        for i, aid, sec in row_spans:
            by_anchor[aid].append((i, sec))
        for aid, hits in by_anchor.items():
            if len(hits) >= 2:
                a_bad.append({"path": rel, "anchor": aid, "copies": len(hits),
                              "lines": ",".join(str(i + 1) for i, _ in hits)})

        # B：同文件、同小节、同锚且整块逐字相同（A 的确认子集，可直接删）
        #    同小节同锚但块内容不同者记 B2 仅 INFO（同锚不同正文，交人工判断）
        spans_hashed = []
        starts = [i for i, _, _ in spans]
        for k, (i, aid, sec) in enumerate(spans):
            end = len(lines)
            for j in starts:
                if j > i:
                    end = j
                    break
            for j in range(i + 1, end):
                if HEAD.match(lines[j].strip()):
                    end = j
                    break
            seg = lines[i:end]
            while seg and not seg[-1].strip():
                seg.pop()
            h = hashlib.sha256("\n".join(seg).encode("utf-8")).hexdigest()
            spans_hashed.append((i, aid, sec, h, len(seg)))
        by_key = defaultdict(list)
        for i, aid, sec, h, n in spans_hashed:
            by_key[(aid, sec)].append((i, h, n))
        for (aid, sec), versions in by_key.items():
            if len(versions) < 2:
                continue
            uniq = {v[1] for v in versions}
            if len(uniq) == 1:
                b_bad.append({"path": rel, "section": sec, "anchor": aid,
                              "copies": len(versions),
                              "lines": ",".join(str(v[0] + 1) for v in versions),
                              "block_len": versions[0][2]})
            else:
                b2_info.append({"path": rel, "section": sec, "anchor": aid,
                                "copies": len(versions), "variants": len(uniq)})

    c_info = {aid: len(fs) for aid, fs in anchor_files.items() if len(fs) >= 2}
    return a_bad, b_bad, b2_info, c_info, {"files": files, "anchors": anchors}


def run_check(root, csv_path=None):
    if not root.is_dir():
        print(f"FAIL：扫描根不存在 {root}")
        return 2
    a_bad, b_bad, b2_info, c_info, st = scan(root)
    print(f"扫描 .md {st['files']} 个｜锚行 {st['anchors']}")
    print(f"A 同文件同锚重复：{len(a_bad)} 组 -> {'FAIL' if a_bad else 'PASS'}")
    for g in a_bad[:20]:
        print(f"   {g['path']}｜{g['anchor']}｜{g['copies']} 副本｜L{g['lines']}")
    print(f"B 同小节整块逐字重复：{len(b_bad)} 组 -> {'FAIL' if b_bad else 'PASS'}")
    for g in b_bad[:20]:
        print(f"   {g['path']}｜{g['section'][:40]}｜{g['anchor']}｜{g['copies']} 份｜{g['block_len']} 行｜L{g['lines']}")
    print(f"B2 同小节同锚但块内容不同（INFO，交人工）：{len(b2_info)} 组")
    for g in b2_info[:10]:
        print(f"   {g['path']}｜{g['anchor']}｜{g['copies']} 副本｜{g['variants']} 种内容")
    print(f"C 跨文件同名锚（INFO）：{len(c_info)} 型｜超出首份 {sum(v - 1 for v in c_info.values())}")
    if csv_path:
        import csv
        with open(csv_path, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f, lineterminator="\n")
            w.writerow(["kind", "path", "key", "copies", "detail"])
            for g in a_bad:
                w.writerow(["A", g["path"], g["anchor"], g["copies"], f"L{g['lines']}"])
            for g in b_bad:
                w.writerow(["B", g["path"], g["anchor"], g["copies"], f"L{g['lines']} block={g['block_len']} sec={g['section']}"])
            for g in b2_info:
                w.writerow(["B2-INFO", g["path"], g["anchor"], g["copies"], f"variants={g['variants']}"])
            for aid, n in sorted(c_info.items(), key=lambda x: -x[1]):
                w.writerow(["C-INFO", "—", aid, n, "跨文件复用"])
        print(f"明细已写 {csv_path}")
    return 1 if (a_bad or b_bad) else 0


def selftest():
    """正例 1＋负例 6，逐例校验退出码与判据计数。"""
    cases = []

    def make(base, name, files):
        d = Path(base) / name / "第01卷-test" / "第001章-test" / "001.0-章级综合"
        d.mkdir(parents=True)
        for fn, body in files.items():
            (d / fn).write_text(body, encoding="utf-8", newline="")

    A1 = "<!-- ROW_MINE: lib.messages.1 -->\n**一手刊文**（证据等级：L4，来源：x）\n\n正文甲\n"
    A1B = "<!-- ROW_MINE: lib.messages.1 -->\n**一手刊文**（证据等级：L4，来源：x）\n\n正文丙\n"
    A2 = "<!-- ROW_MINE: lib.messages.9 -->\n**一手刊文**（证据等级：L4，来源：y）\n\n正文乙\n"
    with tempfile.TemporaryDirectory() as t:
        make(t, "clean", {"001.0.1-a.md": "# 标题\n\n" + A1})
        make(t, "dup_anchor", {"001.0.1-a.md": "# 标题\n\n" + A1 + "\n" + A1})
        make(t, "same_anchor_diff_body", {"001.0.1-a.md": "# 标题\n\n" + A1 + "\n" + A1B})
        make(t, "cross", {"001.0.1-a.md": "# 标题\n\n" + A1, "001.0.2-b.md": "# 标题\n\n" + A1})
        make(t, "two_sections", {"001.0.1-a.md": "# 标题\n\n### 甲\n\n" + A1 + "\n### 乙\n\n" + A1})
        make(t, "tail_blank", {"001.0.1-a.md": "# 标题\n\n" + A1 + "\n\n" + A1})
        make(t, "diff_anchor_same_body", {"001.0.1-a.md": "# 标题\n\n" + A1 + "\n" + A2})

        # (名称, 期望退出码, 期望 A 组, 期望 B 组, 期望 B2 组, 期望 C 型)
        expect = [
            ("clean", 0, 0, 0, 0, 0),
            ("dup_anchor", 1, 1, 1, 0, 0),
            ("same_anchor_diff_body", 1, 1, 0, 1, 0),
            ("cross", 0, 0, 0, 0, 1),
            ("two_sections", 1, 1, 0, 0, 0),
            ("tail_blank", 1, 1, 1, 0, 0),
            ("diff_anchor_same_body", 0, 0, 0, 0, 0),
        ]
        for name, exp_code, exp_a, exp_b, exp_b2, exp_c in expect:
            a, b, b2, c, _ = scan(Path(t) / name)
            got = 1 if (a or b) else 0
            ok = (got == exp_code and len(a) == exp_a and len(b) == exp_b
                  and len(b2) == exp_b2 and len(c) == exp_c)
            cases.append((name, exp_code, got, len(a), len(b), len(b2), len(c), ok))

    bad = [c for c in cases if not c[-1]]
    for c in cases:
        print(f"  {'PASS' if c[-1] else 'FAIL'} {c[0]}：exit 期望 {c[1]}／实得 {c[2]}；"
              f"A={c[3]} B={c[4]} B2={c[5]} C={c[6]}")
    print(f"-- selftest：{len(cases) - len(bad)}/{len(cases)} PASS --")
    return 0 if not bad else 1


def main():
    ap = argparse.ArgumentParser(description="大纲重复锚与重复块门禁（第三十五件）")
    ap.add_argument("--root", default=str(ROOT_DEFAULT))
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--csv", default=None)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    return run_check(Path(a.root), a.csv)


if __name__ == "__main__":
    sys.exit(main())
