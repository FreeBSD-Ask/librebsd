# -*- coding: utf-8 -*-
"""outline_registry.py —— 目标注册表与漂移机制（Task 3 生产版）。

用途
----
解析目录真值源 ``05-卷册大纲/目录/data/outline.txt``，为卷／章／节／小节四级节点
分配稳定 ID，生成目标注册表 ``05-卷册大纲/映射/targets.tsv``；并提供漂移
检测（``--check``）与漂移同步（``--sync``）能力，以及合成夹具自检
（``--selftest``）。

节点 ID 规则
------------
卷 ``V-001``（三位）、章 ``C-0001``（四位，全书连续）、节 ``S-000001``
（六位，全书连续）、小节 ``SS-0000001``（七位，全书连续；2026-11-06 ADR-0020）。ID 一经分配即稳定；漂移时按“同父同题 → 同层同题 →
模糊改题（相似度 ≥ 0.86）→ 新增”顺序复用旧 ID，退役节点保留原 ID 并置
``status=retired``。

targets.tsv 列
--------------
``node_id`` / ``level``（vol|ch|sec|subsec）/ ``parent_id`` / ``vol_no`` / ``ch_no`` /
``sec_no`` / ``title``（原文含 ``⟦lang:…⟧``）/ ``path_title``（剥离标记后的
显示文本）/ ``status``（active|retired）/ ``first_seen`` / ``last_seen`` /
``renamed_from``。

编号口径（2026-10-23 ykla 裁定）
------------------------------
``ch_no`` 取**卷内章序**（每卷永远以第一章开始，与 ``outline.txt`` 的
``## 第 N 章`` 及磁盘章目录 ``第N章-slug`` 一致），``sec_no`` 取
``M.N`` 原文（M＝卷内章号）。``node_id`` 的 ``C-nnnn`` 仍为**全书连续**，
属逻辑标识，不随目录改名复位。

漂移类别
--------
``exact-parent``（同父同题，无漂移）/ ``exact-level``（同层同题，无漂移）/
``renumber``（题同号变）/ ``RENAME_SUSPECT``（模糊改题）/ ``new``（新增）/
``retired``（退役）。漂移报告落 ``05-卷册大纲/映射/drift/drift-report.tsv``。

用法
----
    python outline_registry.py --write          # 由 outline.txt 生成 targets.tsv
    python outline_registry.py --check          # 漂移检测（只读，0 无漂移 / 1 有漂移）
    python outline_registry.py --sync           # 漂移同步（默认 dry-run）
    python outline_registry.py --sync --write   # 漂移同步并写盘
    python outline_registry.py --selftest       # 合成夹具自检（六类场景）
"""
import argparse
import csv
import datetime
import difflib
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parents[3]
OUTLINE = REPO / "05-卷册大纲" / "目录" / "data" / "outline.txt"
TARGETS = REPO / "05-卷册大纲" / "映射" / "targets.tsv"
DRIFT_DIR = REPO / "05-卷册大纲" / "映射" / "drift"

COLS = ["node_id", "level", "parent_id", "vol_no", "ch_no", "sec_no", "title",
        "path_title", "status", "first_seen", "last_seen", "renamed_from"]

FUZZY = 0.86
TODAY = datetime.date.today().isoformat()

LANG_RE = re.compile(r"⟦[a-zA-Z-]+:([^⟧]*)⟧")
VOL_RE = re.compile(r"^# 第[一二三四五六七八九十百零〇0-9]+卷\s+(.*)$")
CH_RE = re.compile(r"^## 第\s*\d+\s*章\s+(.*)$")
SEC_RE = re.compile(r"^-(\s+)(\d+(?:\.\d+)+)\s+(.*)$")
SUB4_RE = re.compile(r"^  -\s+(\d{1,3})\.(\d{1,3})\.(\d{1,4})\s+(.*)$")


def path_title(title):
    """剥离 ``⟦lang:…⟧`` 语言标记，返回显示文本。"""
    return LANG_RE.sub(r"\1", title).strip()


def norm(s):
    """归一化：去空白、转小写，用于匹配比较。"""
    return re.sub(r"\s+", "", s).lower()


def parse(text):
    """解析 outline.txt → 节点列表（文档序），保留父子引用（四级，ADR-0020）。"""
    nodes = []
    vol = ch = sec = None
    vol_no = 0
    gch = 0   # 全书章序（仅用于稳定 ID 计数，不进 ch_no）
    vch = 0   # 卷内章序（ch_no 的口径，2026-10-23 ykla 裁定：每卷永远以第一章开始）
    for line in text.split("\n"):
        if line.startswith("# "):
            vol_no += 1
            vch = 0
            m = VOL_RE.match(line)
            title = m.group(1).strip() if m else line[2:].strip()
            vol = {"level": "vol", "vol_no": vol_no, "ch_no": "", "sec_no": "",
                   "title": title, "parent": None}
            nodes.append(vol)
            ch = None
        elif line.startswith("## "):
            gch += 1
            vch += 1
            m = CH_RE.match(line)
            title = m.group(1).strip() if m else line[3:].strip()
            ch = {"level": "ch", "vol_no": vol_no, "ch_no": vch, "sec_no": "",
                  "gch": gch, "title": title, "parent": vol}
            nodes.append(ch)
        elif line.startswith("- "):
            m = SEC_RE.match(line)
            if not m:
                continue
            title = m.group(3).split("@@")[0].rstrip()
            sec = {"level": "sec", "vol_no": vol_no, "ch_no": vch,
                   "sec_no": m.group(2), "title": title, "parent": ch}
            nodes.append(sec)
        elif line.startswith("  - "):
            # 第四级小节行（ADR-0020，2026-11-06）：两前导空格＋`- M.N.P 题名`
            m = SUB4_RE.match(line)
            if not m:
                continue
            title = m.group(4).split("@@")[0].rstrip()
            nodes.append({"level": "subsec", "vol_no": vol_no, "ch_no": vch,
                          "sec_no": "%s.%s.%s" % (m.group(1), m.group(2), m.group(3)),
                          "title": title, "parent": sec})
    return nodes


def assign_ids(nodes):
    """按文档序分配稳定 ID：V-001 / C-0001 / S-000001 / SS-0000001（ADR-0020）。"""
    v = c = s = ss = 0
    for n in nodes:
        if n["level"] == "vol":
            v += 1
            n["node_id"] = "V-%03d" % v
            n["parent_id"] = ""
        elif n["level"] == "ch":
            c += 1
            n["node_id"] = "C-%04d" % c
            n["parent_id"] = n["parent"]["node_id"]
        elif n["level"] == "subsec":
            ss += 1
            n["node_id"] = "SS-%07d" % ss
            n["parent_id"] = n["parent"]["node_id"] if n["parent"] else ""
        else:
            s += 1
            n["node_id"] = "S-%06d" % s
            n["parent_id"] = n["parent"]["node_id"]
    return nodes


def build_registry(text):
    """由 outline.txt 文本构建初始注册表节点（全部 active）。"""
    nodes = assign_ids(parse(text))
    for n in nodes:
        n["status"] = "active"
        n["first_seen"] = TODAY
        n["last_seen"] = TODAY
        n["renamed_from"] = ""
    return nodes


def load_registry(path):
    """读取 targets.tsv → 节点字典列表。"""
    rows = []
    with open(path, encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            rows.append(row)
    return rows


def _no_str(n):
    if n["level"] in ("sec", "subsec"):
        return str(n["sec_no"])
    if n["level"] == "ch":
        return str(n["ch_no"])
    return str(n["vol_no"])


def _drift_row(new, old, change, sim):
    ref = new if new is not None else old
    return {
        "node_id": ref["node_id"],
        "level": ref["level"],
        "change": change,
        "old_title": old["title"] if old is not None else "",
        "new_title": new["title"] if new is not None else "",
        "old_no": _no_str(old) if old is not None else "",
        "new_no": _no_str(new) if new is not None else "",
        "similarity": "%.4f" % sim,
    }


def reconcile(new_nodes, old_nodes):
    """漂移算法：同父同题 → 同层同题 → 模糊改题 → 新增；未匹配旧节点退役。

    返回 (new_nodes, old_nodes, drift_rows, stats)。
    """
    used = set()
    by_parent = {}
    by_level = {}
    for o in old_nodes:
        by_parent.setdefault((o["level"], o["parent_id"], norm(o["title"])), []).append(o)
        by_level.setdefault((o["level"], norm(o["title"])), []).append(o)

    counters = {"V": 0, "C": 0, "S": 0, "SS": 0}
    for o in old_nodes:
        pfx, num = o["node_id"].split("-")
        counters[pfx] = max(counters[pfx], int(num))

    def next_id(level):
        pfx = {"vol": "V", "ch": "C", "sec": "S", "subsec": "SS"}[level]
        width = {"vol": 3, "ch": 4, "sec": 6, "subsec": 7}[level]
        counters[pfx] += 1
        return "%s-%0*d" % (pfx, width, counters[pfx])

    drift = []
    stats = {"exact-parent": 0, "exact-level": 0, "renumber": 0,
             "RENAME_SUSPECT": 0, "new": 0, "retired": 0}

    for level in ("vol", "ch", "sec", "subsec"):
        for n in [x for x in new_nodes if x["level"] == level]:
            n["parent_id"] = "" if level == "vol" else n["parent"]["node_id"]
            hit = None
            match = None
            for cand in by_parent.get((level, n["parent_id"], norm(n["title"])), []):
                if cand["node_id"] not in used:
                    hit, match = cand, "exact-parent"
                    break
            if hit is None:
                for cand in by_level.get((level, norm(n["title"])), []):
                    if cand["node_id"] not in used:
                        hit, match = cand, "exact-level"
                        break
            best_r = 0.0
            if hit is None:
                best = None
                for o in old_nodes:
                    if o["level"] != level or o["node_id"] in used:
                        continue
                    r = difflib.SequenceMatcher(None, norm(o["title"]), norm(n["title"])).ratio()
                    if r > best_r:
                        best, best_r = o, r
                if best is not None and best_r >= FUZZY:
                    hit, match = best, "rename"
            if hit is not None:
                n["node_id"] = hit["node_id"]
                n["match"] = match
                n["status"] = "active"
                n["first_seen"] = hit["first_seen"]
                n["last_seen"] = TODAY
                n["renamed_from"] = hit["title"] if match == "rename" else ""
                used.add(hit["node_id"])
                if match == "rename":
                    stats["RENAME_SUSPECT"] += 1
                    drift.append(_drift_row(n, hit, "RENAME_SUSPECT", best_r))
                elif (str(hit["vol_no"]) != str(n["vol_no"])
                      or str(hit["ch_no"]) != str(n["ch_no"])
                      or str(hit["sec_no"]) != str(n["sec_no"])):
                    stats["renumber"] += 1
                    drift.append(_drift_row(n, hit, "renumber", 1.0))
                else:
                    stats[match] += 1
            else:
                n["node_id"] = next_id(level)
                n["match"] = "new"
                n["status"] = "active"
                n["first_seen"] = TODAY
                n["last_seen"] = TODAY
                n["renamed_from"] = ""
                stats["new"] += 1
                drift.append(_drift_row(n, None, "new", 0.0))

    for o in old_nodes:
        if o["node_id"] not in used:
            o["status"] = "retired"
            stats["retired"] += 1
            drift.append(_drift_row(None, o, "retired", 0.0))
        else:
            o["status"] = "active"
    return new_nodes, old_nodes, drift, stats


def write_targets(path, nodes):
    """写 targets.tsv（UTF-8 无 BOM、LF）。"""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(COLS)
        for n in nodes:
            w.writerow([n["node_id"], n["level"], n.get("parent_id", ""),
                        n["vol_no"], n["ch_no"], n["sec_no"], n["title"],
                        path_title(n["title"]), n.get("status", "active"),
                        n.get("first_seen", TODAY), n.get("last_seen", TODAY),
                        n.get("renamed_from", "")])


def write_drift_report(drift_dir, drift):
    """写漂移报告 drift-report.tsv（UTF-8 无 BOM、LF）。"""
    drift_dir.mkdir(parents=True, exist_ok=True)
    path = drift_dir / "drift-report.tsv"
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["node_id", "level", "change", "old_title", "new_title",
                    "old_no", "new_no", "similarity"])
        for d in drift:
            w.writerow([d["node_id"], d["level"], d["change"], d["old_title"],
                        d["new_title"], d["old_no"], d["new_no"], d["similarity"]])
    return path


def _print_stats(stats):
    print("  匹配：exact-parent=%d  exact-level=%d  renumber=%d  RENAME_SUSPECT=%d"
          % (stats["exact-parent"], stats["exact-level"], stats["renumber"],
             stats["RENAME_SUSPECT"]))
    print("  漂移：new=%d  retired=%d" % (stats["new"], stats["retired"]))


def cmd_write(outline, targets):
    text = outline.read_text(encoding="utf-8")
    nodes = build_registry(text)
    write_targets(targets, nodes)
    nv = sum(1 for n in nodes if n["level"] == "vol")
    nc = sum(1 for n in nodes if n["level"] == "ch")
    ns = sum(1 for n in nodes if n["level"] == "sec")
    nss = sum(1 for n in nodes if n["level"] == "subsec")
    print("已写 %s：%d 卷 / %d 章 / %d 节 / %d 小节（共 %d 行）"
          % (targets, nv, nc, ns, nss, len(nodes)))
    return 0


def cmd_check(outline, targets, drift_dir):
    text = outline.read_text(encoding="utf-8")
    new_nodes = parse(text)
    if not targets.exists():
        print("targets.tsv 不存在：%s（视为全量新增）" % targets)
        return 1
    old_nodes = load_registry(targets)
    new_nodes, old_nodes, drift, stats = reconcile(new_nodes, old_nodes)
    path = write_drift_report(drift_dir, drift)
    print("漂移检测：%s" % targets)
    _print_stats(stats)
    print("  报告：%s（%d 行）" % (path, len(drift)))
    drift_n = stats["renumber"] + stats["RENAME_SUSPECT"] + stats["new"] + stats["retired"]
    if drift_n == 0:
        print("结果：零漂移")
        return 0
    print("结果：存在漂移 %d 项" % drift_n)
    return 1


def cmd_sync(outline, targets, drift_dir, do_write):
    text = outline.read_text(encoding="utf-8")
    new_nodes = parse(text)
    old_nodes = load_registry(targets) if targets.exists() else []
    new_nodes, old_nodes, drift, stats = reconcile(new_nodes, old_nodes)
    path = write_drift_report(drift_dir, drift)
    print("漂移同步（%s）：%s" % ("写盘" if do_write else "dry-run", targets))
    _print_stats(stats)
    print("  报告：%s（%d 行）" % (path, len(drift)))
    if do_write:
        out = list(new_nodes) + [o for o in old_nodes if o["status"] == "retired"]
        write_targets(targets, out)
        print("已写 %s（%d 行）" % (targets, len(out)))
    else:
        print("dry-run：未写盘（加 --write 落盘）")
    return 0


FIXTURE = """# 第一卷  测试卷
## 第 1 章 测试章一
- 1.1 机械计算与自动计算思想
  - 1.1.1 巴贝奇的差分机方案
  - 1.1.2 分析机与通用计算构想
- 1.2 差分机与分析机
- 1.3 可计算性与机电计算机
## 第 2 章 测试章二
- 2.1 存储程序概念
- 2.2 分时计算
"""


def selftest():
    """合成夹具自证六类漂移场景：改号、重排、改题、删除、拆分、合并。"""
    base = build_registry(FIXTURE)
    cases = []

    # 1 改号：节号 1.1 → 1.9，题不变 → renumber
    cases.append(("改号 renumber",
                  FIXTURE.replace("- 1.1 机械计算与自动计算思想",
                                  "- 1.9 机械计算与自动计算思想"),
                  {"renumber": 1, "new": 0, "retired": 0}))

    # 2 重排：交换前两节行（号随题走，无新增无退役）
    lines = FIXTURE.split("\n")
    i1 = lines.index("- 1.1 机械计算与自动计算思想")
    i2 = lines.index("- 1.2 差分机与分析机")
    lines[i1], lines[i2] = lines[i2], lines[i1]
    cases.append(("重排 reorder", "\n".join(lines),
                  {"new": 0, "retired": 0, "renumber": 0, "RENAME_SUSPECT": 0}))

    # 3 改题：加一字，相似度 ≥ 0.86 → RENAME_SUSPECT
    cases.append(("改题 rename",
                  FIXTURE.replace("- 1.1 机械计算与自动计算思想",
                                  "- 1.1 机械计算与自动计算思想史"),
                  {"RENAME_SUSPECT": 1, "new": 0, "retired": 0}))

    # 4 删除：删一节 → 退役 1
    cases.append(("删除 delete",
                  FIXTURE.replace("- 1.3 可计算性与机电计算机\n", ""),
                  {"new": 0, "retired": 1}))

    # 5 拆分：一节拆为两节（原题保留，另一节为全新题）→ 新增 1
    cases.append(("拆分 split",
                  FIXTURE.replace("- 1.1 机械计算与自动计算思想",
                                  "- 1.1 机械计算与自动计算思想\n"
                                  "- 1.4 自动计算思想的分期与谱系"),
                  {"new": 1, "retired": 0}))

    # 6 合并：两节并为一节（合并题与两原题相似度均 < 0.86）→ 新增 1、退役 2
    # 6 合并：两节并为一节（含其下两小节行一并撤销；合并题与两原题相似度均 < 0.86）
    # → sec 新增 1＋退役 2、subsec 退役 2（宿主节亡则小节退役）（2026-11-06 四级口径）
    cases.append(("合并 merge",
                  FIXTURE.replace("- 1.1 机械计算与自动计算思想\n"
                                  "  - 1.1.1 巴贝奇的差分机方案\n"
                                  "  - 1.1.2 分析机与通用计算构想\n"
                                  "- 1.2 差分机与分析机",
                                  "- 1.1 机械计算与自动计算思想与差分机与分析机"),
                  {"new": 1, "retired": 4}))

    # 7 小节（ADR-0020，2026-11-06）：新增一小节 → subsec new 1；删一小节 → subsec retired 1
    cases.append(("小节新增 subsec-new",
                  FIXTURE.replace("  - 1.1.2 分析机与通用计算构想",
                                  "  - 1.1.2 分析机与通用计算构想\n  - 1.1.3 差分机的经济史"),
                  {"new": 1, "retired": 0}))
    cases.append(("小节退役 subsec-retired",
                  FIXTURE.replace("  - 1.1.2 分析机与通用计算构想\n", ""),
                  {"new": 0, "retired": 1}))

    passed = 0
    for name, text, expect in cases:
        old = [dict(o) for o in base]
        _, _, _, stats = reconcile(parse(text), old)
        ok = all(stats.get(k) == v for k, v in expect.items())
        passed += 1 if ok else 0
        detail = "  ".join("%s=%d(期望 %d)" % (k, stats.get(k, -1), v)
                           for k, v in expect.items())
        print("[%s] %s  %s" % ("PASS" if ok else "FAIL", name, detail))
    print("自检结果：%s（%d/%d）" % ("全 PASS" if passed == len(cases) else "存在 FAIL",
                                    passed, len(cases)))
    return 0 if passed == len(cases) else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description="目标注册表与漂移机制")
    ap.add_argument("--write", action="store_true", help="由 outline.txt 生成 targets.tsv")
    ap.add_argument("--check", action="store_true", help="漂移检测（只读）")
    ap.add_argument("--sync", action="store_true", help="漂移同步（默认 dry-run）")
    ap.add_argument("--selftest", action="store_true", help="合成夹具自检")
    ap.add_argument("--outline", type=pathlib.Path, default=OUTLINE)
    ap.add_argument("--targets", type=pathlib.Path, default=TARGETS)
    ap.add_argument("--drift-dir", type=pathlib.Path, default=DRIFT_DIR)
    args = ap.parse_args(argv)

    if args.selftest:
        return selftest()
    if args.sync:
        return cmd_sync(args.outline, args.targets, args.drift_dir, args.write)
    if args.check:
        return cmd_check(args.outline, args.targets, args.drift_dir)
    if args.write:
        return cmd_write(args.outline, args.targets)
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
