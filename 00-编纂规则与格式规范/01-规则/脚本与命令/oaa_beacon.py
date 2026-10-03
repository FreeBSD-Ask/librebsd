#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""oaa_beacon.py — OAA F1-F4 跨组浮标（允许交叉读写的唯一协调文件）

背景：大纲条目动态增长；F1-F4 并行时共写 processed.jsonl 会互相覆盖
（该文件是"读全量→写全量"非原子）。故：

  基线台账 processed.jsonl        只读冻结（B1-B7 历史累计）
  分片台账 processed_f1..f4.jsonl 各组独占写（无并发冲突）
  浮标     beacon/beacon.json     机读：快照/认领/进度/新增
           _BEACON.md             人读：交叉读写协议＋状态摘要

交叉读写协议：
  开工：--refresh（合并全部台账 → 扫大纲 → 算本组 pending/新增；他组新条目自动浮现）
  收工：组内 register 写自己的 processed_fN.jsonl → 再 --refresh 更新浮标
  去重：合并集 = 基线 ∪ 四组台账；认领表 claims_FN.txt 界定组边界（防跨组重复处理）

用法：
  python oaa_beacon.py --claims          # 重生成四组认领清单 beacon/claims_F*.txt
  python oaa_beacon.py --refresh         # 刷新快照与浮标（含目录树变动差分）
  python oaa_beacon.py --status          # 打印浮标状态
  python oaa_beacon.py --pending F1 [N]  # 打印 F1 未处理条目（前 N 条，默认 20）

目录变动路由（2026-10-03 主理人令，F1–F4 同文）：
  05-卷册大纲 目录树随时新增/减少/变动，--refresh 以 tree_prev.json 快照差分识别：
  新增（新目录/新文件）        → 一律计入 F4（claims_F4.txt，持久化 routed_F4.json）
  减少（文件/目录删除）        → 一律交 F3（beacon/changes_F3.txt ＋ 孤儿台账 key 数）
  变动（改名/移动，锚点集不变） → 一律交 F3（changes_F3.txt 记「旧→新」对）
  文件内锚点增减               → 不路由，归原属组 pending（delta_vs_last 可见）
  首次运行只建基线快照（tree_prev.json）、不路由。
"""
import argparse
import glob
import hashlib
import json
import os
import re
import sys
import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
OUT = os.path.join(ROOT, "script", "_db_row_mining", "audit_outline")
BEACON_DIR = os.path.join(OUT, "beacon")
BEACON = os.path.join(BEACON_DIR, "beacon.json")
MARKDOWN = os.path.join(OUT, "_BEACON.md")
TREE_PREV = os.path.join(BEACON_DIR, "tree_prev.json")
ROUTED_F4 = os.path.join(BEACON_DIR, "routed_F4.json")
CHANGES_JSON = os.path.join(BEACON_DIR, "changes.json")
CHANGES_F3 = os.path.join(BEACON_DIR, "changes_F3.txt")
RM = re.compile(r"ROW_MINE:\s*([\w-]+)\.([\w.]+)\.(\d+)")

# 第05卷外围库集（F3 认领；与 F1 精确互斥）——与 F1/F3 任务书 §三.1 同一集合
PERIPH = {
    "freebsd-doc", "freebsd-advocacy", "freebsd-chat", "freebsd-newbies", "freebsd-hubs",
    "freebsd-hardware", "freebsd-office", "freebsd-openoffice", "freebsd-chromium",
    "freebsd-gecko", "freebsd-x11", "freebsd-apache", "freebsd-elastic", "freebsd-www",
    "freebsd-perl", "freebsd-alpha", "freebsd-ppc", "freebsd-sparc64", "freebsd-i386",
    "freebsd-ia64", "freebsd-mips", "freebsd-arm", "freebsd-lite", "freebsd-vendors",
    "freebsd-binup", "ctm-announce",
    "freebsd-smp", "freebsd-emulation", "freebsd-scsi", "freebsd-acpi", "freebsd-geom",
    "freebsd-ipfw", "freebsd-isdn", "freebsd-net", "freebsd-isp",
}
# 组 → 卷目录 glob（F4 长尾；F1/F3 共用第05卷按 PERIPH 分）
GROUP_VOLS = {
    "F2": ["第09卷-netbsd的历史"],
    "F3": ["第06卷-freebsd的核心技术革新", "第07卷-freebsd的工程体系重构",
           "第08卷-freebsd的范式转换", "第15卷-许可证哲学与法律分析"],
    "F4": ["第01卷-unix的起源", "第02卷-伯克利的岁月", "第03卷-伯克利学术文化外溢影响",
           "第04卷-大分裂与四大bsd的诞生", "第10卷-openbsd的历史", "第11卷-dragonflybsd的历史",
           "第12卷-macos的bsd遗产", "第13卷-bsd衍生操作系统", "第14卷-商业生态与企业案例",
           "第16卷-开源运动与合规治理", "第17卷-政治制度与社区治理", "第18卷-全球社区地区bsd史",
           "第20卷-linux社区史与比较研究", "第21卷-传播渠道与工具生态"],
}
V5 = "第05卷-freebsd的工程化奠基"
SKIP_NAMES = {"index.md", "概述.md", "00-总览.md"}


def merged_done():
    """合并集 = 基线台账 ∪ 四组分片台账（去重）。"""
    done = set()
    for fn in ["processed.jsonl"] + [f"processed_{g.lower()}.jsonl" for g in ("F1", "F2", "F3", "F4")]:
        p = os.path.join(OUT, fn)
        if not os.path.exists(p):
            continue
        for l in open(p, encoding="utf-8"):
            if l.strip():
                try:
                    done.add(json.loads(l)["key"])
                except Exception:
                    pass
    return done


def scan_outline():
    """扫全量锚点 → (per_host, tree)；含新增（大纲动态增长自动发现）。
    per_host: {宿主相对路径: {库: n}}
    tree:     {宿主相对路径: {"n": 锚点数, "h": 锚点集合哈希}}（目录变动差分用，
              哈希不含路径 → 改名/移动后哈希不变，可识别「旧→新」对）。"""
    per_host = {}
    tree = {}
    seen = set()
    for f in glob.glob(os.path.join(ROOT, "05-卷册大纲", "**", "*.md"), recursive=True):
        if os.path.basename(f) in SKIP_NAMES:
            continue
        rp = os.path.realpath(f)
        if rp in seen:
            continue
        try:
            txt = open(f, encoding="utf-8").read()
        except Exception:
            continue
        ms = RM.findall(txt)
        if not ms:
            continue
        seen.add(rp)
        rel = os.path.relpath(f, ROOT).replace("\\", "/")
        libs = {}
        anchors = []
        for db, _sub, pk in ms:
            libs[db] = libs.get(db, 0) + 1
            anchors.append(f"{db}|{pk}")
        per_host[rel] = libs
        anchors.sort()
        tree[rel] = {
            "n": len(anchors),
            "h": hashlib.sha1(",".join(anchors).encode("utf-8")).hexdigest()[:12],
        }
    return per_host, tree


def load_routed():
    """持久化路由表：新增目录一律计入 F4（2026-10-03 主理人令）。"""
    if not os.path.exists(ROUTED_F4):
        return []
    try:
        return json.load(open(ROUTED_F4, encoding="utf-8"))
    except Exception:
        return []


def diff_tree(cur, prev):
    """目录树差分 → (added, removed, moved, changed_n)。
    moved＝改名/移动对（锚点集合哈希相同）；changed_n＝原地锚点数变化（动态增长，不路由）。"""
    added = sorted(set(cur) - set(prev))
    removed = sorted(set(prev) - set(cur))
    h_added = {cur[r]["h"]: r for r in added}
    moved = []
    for r in list(removed):
        a = h_added.get(prev[r]["h"])
        if a is not None:
            moved.append({"from": r, "to": a})
            removed.remove(r)
            added.remove(a)
            del h_added[prev[r]["h"]]
    changed_n = {
        r: [prev[r]["n"], cur[r]["n"]]
        for r in sorted(set(prev) & set(cur))
        if prev[r]["n"] != cur[r]["n"]
    }
    return added, removed, moved, changed_n


def orphan_counts(done, rels):
    """台账合并集中指向已删除路径的 key 数（孤儿条目，F3 处置对象）。"""
    relset = set(rels)
    out = {r: 0 for r in rels}
    for k in done:
        try:
            _db, _pk, rel = k.split("|", 2)
        except ValueError:
            continue
        if rel in relset:
            out[rel] += 1
    return out


def route_changes(added, removed, moved, changed_n, done, now):
    """按主理人令路由：新增→F4（持久化）、减少/变动→F3（changes_F3.txt）。返回路由集与变动摘要。"""
    routed = sorted(set(load_routed()) | set(added))
    with open(ROUTED_F4, "w", encoding="utf-8", newline="") as fh:
        json.dump(routed, fh, ensure_ascii=False, indent=1)
    orph = orphan_counts(done, removed) if removed else {}
    changes = {
        "updated_at": now,
        "added_to_F4": added,
        "removed_to_F3": [{"path": r, "orphan_ledger_keys": orph[r]} for r in removed],
        "moved_to_F3": moved,
        "anchor_growth_in_place": {
            "count": len(changed_n),
            "top20": sorted(
                ({"path": r, "from": v[0], "to": v[1], "delta": v[1] - v[0]}
                 for r, v in changed_n.items()),
                key=lambda x: -x["delta"],
            )[:20],
        },
    }
    with open(CHANGES_JSON, "w", encoding="utf-8", newline="") as fh:
        json.dump(changes, fh, ensure_ascii=False, indent=1)
    lines = ["# 目录变动处置清单（F3 专属，oaa_beacon.py --refresh 生成）",
             f"> 刷新：{now}｜新增目录一律计入 F4（beacon/routed_F4.json）；减少/变动一律交 F3。",
             ""]
    for r in removed:
        lines.append(f"- 减少 {r}（孤儿台账 key {orph[r]} 条）")
    for m in moved:
        lines.append(f"- 变动 {m['from']} → {m['to']}")
    if not removed and not moved:
        lines.append("（本次无减少/变动）")
    with open(CHANGES_F3, "w", encoding="utf-8", newline="") as fh:
        fh.write("\n".join(lines) + "\n")
    return routed, changes


def group_of(rel, libs):
    """宿主归组：F1/F3 按第05卷主库 vs PERIPH；F2/F4 按卷。"""
    parts = rel.split("/")
    vol = parts[1] if len(parts) > 1 else ""
    if vol == V5:
        main = max(libs.items(), key=lambda x: x[1])[0]
        return "F3" if main in PERIPH else "F1"
    for g, vols in GROUP_VOLS.items():
        if vol in vols:
            return g
    return None  # 未归组（新卷等）


def write_claims(per_host, routed=()):
    """生成四组认领清单 beacon/claims_F*.txt（宿主相对路径，一行一宿主）。
    routed 中的路径强制归 F4（目录变动路由：新增一律计入 F4）。"""
    os.makedirs(BEACON_DIR, exist_ok=True)
    buckets = {"F1": [], "F2": [], "F3": [], "F4": []}
    unclaimed = []
    routed_set = set(routed)
    for rel, libs in sorted(per_host.items()):
        if rel in routed_set:
            buckets["F4"].append(rel)
            continue
        g = group_of(rel, libs)
        (buckets[g] if g else unclaimed).append(rel)
    meta = {}
    for g, rels in buckets.items():
        p = os.path.join(BEACON_DIR, f"claims_{g}.txt")
        with open(p, "w", encoding="utf-8", newline="") as fh:
            fh.write("\n".join(rels) + ("\n" if rels else ""))
        h = hashlib.sha1("\n".join(rels).encode("utf-8")).hexdigest()[:12]
        meta[g] = {"hosts": len(rels), "hosts_hash": h, "file": f"beacon/claims_{g}.txt"}
    # 空集也重写（清空）——否则上一次遗留的告警文件会永久阻塞各组「先归组再执行」前置
    p = os.path.join(BEACON_DIR, "claims_UNCLAIMED.txt")
    with open(p, "w", encoding="utf-8", newline="") as fh:
        fh.write("\n".join(unclaimed) + ("\n" if unclaimed else ""))
    if unclaimed:
        print(f"! 有 {len(unclaimed)} 个未归组宿主 → beacon/claims_UNCLAIMED.txt（须人工归组）", file=sys.stderr)
    return meta, unclaimed


def refresh():
    done = merged_done()
    per_host, tree = scan_outline()
    now = datetime.datetime.now().isoformat(timespec="seconds")

    # 目录树变动差分（2026-10-03 主理人令：新增→F4、减少/变动→F3；首次运行只建基线快照）
    routed_set = set(load_routed())
    if os.path.exists(TREE_PREV):
        try:
            prev_tree = json.load(open(TREE_PREV, encoding="utf-8"))
        except Exception:
            prev_tree = None
    else:
        prev_tree = None
    if prev_tree is None:
        changes = None
        print("目录树基线快照已建立（首次运行，不路由）→ beacon/tree_prev.json")
    else:
        added, removed, moved, changed_n = diff_tree(tree, prev_tree)
        routed_set, changes = route_changes(added, removed, moved, changed_n, done, now)
        if added or removed or moved:
            print(f"! 目录变动：新增→F4 {len(added)}｜减少→F3 {len(removed)}｜变动→F3 {len(moved)}"
                  f"（beacon/changes.json ＋ changes_F3.txt）", file=sys.stderr)
        if changed_n:
            print(f"  文件内锚点增长（不路由）：{len(changed_n)} 个文件", file=sys.stderr)
    with open(TREE_PREV, "w", encoding="utf-8", newline="") as fh:
        json.dump(tree, fh, ensure_ascii=False, indent=1)

    claims_meta, unclaimed = write_claims(per_host, routed_set)
    anchors_total = sum(sum(v.values()) for v in per_host.values())

    # 逐组统计（认领范围内已处理/未处理）
    prog = {}
    done_total = 0
    pend_total = 0
    for g in ("F1", "F2", "F3", "F4"):
        p = os.path.join(BEACON_DIR, f"claims_{g}.txt")
        rels = [l.strip() for l in open(p, encoding="utf-8") if l.strip()] if os.path.exists(p) else []
        n_done = n_pend = 0
        for rel in rels:
            for db, n in per_host.get(rel, {}).items():
                for i in range(n):
                    pass  # 数量统计（明细由 --pending 给）
            # 精确判定需要逐锚，做一次缓存
        prog[g] = None
    # 精确逐锚判定（一次遍历）
    detail = {g: {"done": 0, "pend": 0} for g in ("F1", "F2", "F3", "F4")}
    pend_list = {g: [] for g in ("F1", "F2", "F3", "F4")}
    for f in glob.glob(os.path.join(ROOT, "05-卷册大纲", "**", "*.md"), recursive=True):
        if os.path.basename(f) in SKIP_NAMES:
            continue
        rel = os.path.relpath(f, ROOT).replace("\\", "/")
        if rel not in per_host:
            continue
        g = "F4" if rel in routed_set else group_of(rel, per_host[rel])
        if not g:
            continue
        try:
            txt = open(f, encoding="utf-8").read()
        except Exception:
            continue
        for m in RM.finditer(txt):
            k = f"{m.group(1)}|{m.group(3)}|{rel}"
            if k in done:
                detail[g]["done"] += 1
                done_total += 1
            else:
                detail[g]["pend"] += 1
                pend_total += 1
                pend_list[g].append(k)
    for g in ("F1", "F2", "F3", "F4"):
        detail[g].update(claims_meta.get(g, {}))

    # 与上次浮标对比 → 新增条目数（大纲动态增长检测）
    prev = {}
    if os.path.exists(BEACON):
        try:
            prev = json.load(open(BEACON, encoding="utf-8"))
        except Exception:
            prev = {}
    prev_pend = {g: (prev.get("progress", {}).get(g, {}) or {}).get("pend", 0) for g in detail}
    for g in detail:
        detail[g]["delta_vs_last"] = detail[g]["pend"] - prev_pend.get(g, detail[g]["pend"])

    beacon = {
        "updated_at": datetime.datetime.now().isoformat(timespec="seconds"),
        "ledgers": {
            "baseline": "processed.jsonl（只读冻结，B1-B7 历史）",
            **{g: f"processed_{g.lower()}.jsonl（{g} 独占写）" for g in ("F1", "F2", "F3", "F4")},
        },
        "claims": {g: {k: v for k, v in detail[g].items() if k in ("hosts", "hosts_hash", "file")}
                   for g in detail},
        "progress": {g: {k: v for k, v in detail[g].items() if k in ("done", "pend", "delta_vs_last",
                                                                    "hosts")} for g in detail},
        "totals": {
            "anchors_total": anchors_total,
            "done": done_total + (sum(prev.get("totals", {}).get("done", 0) for _ in [0]) if False else 0),
            "pending": pend_total,
        },
        "unclaimed": len(unclaimed),
    }
    # 已处理总数（含已从大纲移除的 remap-removed，故并集口径单列）
    beacon["totals"]["done"] = len(done)
    os.makedirs(BEACON_DIR, exist_ok=True)
    with open(BEACON, "w", encoding="utf-8", newline="") as fh:
        json.dump(beacon, fh, ensure_ascii=False, indent=1)

    # 人读浮标
    lines = [
        "# OAA 跨组浮标（_BEACON.md，机读副本 beacon/beacon.json）",
        f"> 刷新：{beacon['updated_at']}｜由 `oaa_beacon.py --refresh` 生成，**所有组可交叉读写**",
        "",
        "## 交叉读写协议",
        "1. **开工**：`python 00-…/脚本与命令/oaa_beacon.py --refresh` → 读本组 `beacon/claims_FN.txt` 认领清单 → `--pending FN` 取待办（他组新入账条目自动扣除）；",
        "2. **收工**：组内 `oaa_register.py` **写自己的 `processed_fN.jsonl`**（勿写基线 `processed.jsonl`）→ 再 `--refresh`；",
        "3. **去重**：合并集 = `processed.jsonl`（基线）∪ `processed_f1..f4.jsonl`；",
        "4. **新增**：大纲新增条目在下次 `--refresh` 自动出现在对应组 pending（`delta_vs_last` 为正即本组新增数）；",
        "5. **越界防护**：处理前核对宿主 ∈ 本组 `claims_FN.txt`；`claims_UNCLAIMED.txt` 非空须先归组。",
        "",
        "## 各组进度",
        "| 组 | 宿主 | 已处理 | 待处理 | 较上次 | 认领清单 |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for g in ("F1", "F2", "F3", "F4"):
        d = detail[g]
        lines.append(f"| {g} | {d['hosts']} | {d['done']} | {d['pend']} | {d['delta_vs_last']:+d} | `{d['file']}` |")
    lines += [
        "",
        f"**全局**：锚点总数 {anchors_total}｜待处理 {pend_total}｜台账合并集 {len(done)} 条｜未归组宿主 {len(unclaimed)}",
    ]
    # 目录变动段（2026-10-03 主理人令：新增→F4、减少/变动→F3）
    lines += [
        "",
        "## 目录变动路由（新增→F4，减少/变动→F3）",
    ]
    if changes is None:
        lines.append("本次为基线快照首建（未差分）。此后每次 `--refresh` 差分一次："
                     "新增目录/文件一律计入 F4（`beacon/routed_F4.json`）；"
                     "减少/变动一律交 F3（`beacon/changes_F3.txt`）；"
                     "文件内锚点增长不路由，归原属组 pending。")
    else:
        a = changes["added_to_F4"]
        r = changes["removed_to_F3"]
        mv = changes["moved_to_F3"]
        gr = changes["anchor_growth_in_place"]
        lines.append(f"- 新增→F4：{len(a)}（{'; '.join(a[:10])}{'…' if len(a) > 10 else ''}）")
        lines.append(f"- 减少→F3：{len(r)}｜变动→F3：{len(mv)}（明细见 `beacon/changes_F3.txt`）")
        lines.append(f"- 文件内锚点增长（不路由）：{gr['count']} 个文件"
                     + (f"，最大 {gr['top20'][0]['path']} {gr['top20'][0]['from']}→{gr['top20'][0]['to']}" if gr["top20"] else ""))
    lines += [
        "",
        "",
    ]
    with open(MARKDOWN, "w", encoding="utf-8", newline="") as fh:
        fh.write("\n".join(lines))
    print(f"浮标已刷新 → beacon/beacon.json ＋ _BEACON.md")
    for g in ("F1", "F2", "F3", "F4"):
        d = detail[g]
        print(f"  {g}: 宿主{d['hosts']:3d} 已{d['done']:6d} 待{d['pend']:6d} 较上次{d['delta_vs_last']:+d}")
    print(f"  全局: 待处理 {pend_total}｜台账合并 {len(done)} 条｜未归组 {len(unclaimed)}")


def status():
    if not os.path.exists(BEACON):
        print("浮标未生成，先跑 --refresh")
        return
    b = json.load(open(BEACON, encoding="utf-8"))
    print(f"浮标时间：{b['updated_at']}")
    for g, p in b["progress"].items():
        print(f"  {g}: 宿主{p['hosts']} 已{p['done']} 待{p['pend']} 较上次{p['delta_vs_last']:+d}")
    t = b["totals"]
    print(f"  全局：锚点 {t['anchors_total']}｜待处理 {t['pending']}｜台账 {t['done']}｜未归组 {b['unclaimed']}")


def pending(g, n=20):
    done = merged_done()
    p = os.path.join(BEACON_DIR, f"claims_{g}.txt")
    if not os.path.exists(p):
        print(f"无认领清单 {p}，先跑 --claims")
        return
    rels = {l.strip() for l in open(p, encoding="utf-8") if l.strip()}
    shown = 0
    for f in glob.glob(os.path.join(ROOT, "05-卷册大纲", "**", "*.md"), recursive=True):
        rel = os.path.relpath(f, ROOT).replace("\\", "/")
        if rel not in rels:
            continue
        try:
            txt = open(f, encoding="utf-8").read()
        except Exception:
            continue
        for m in RM.finditer(txt):
            k = f"{m.group(1)}|{m.group(3)}|{rel}"
            if k not in done:
                print(k)
                shown += 1
                if shown >= n:
                    return
    print(f"(仅 {shown} 条)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--claims", action="store_true", help="重生成认领清单")
    ap.add_argument("--refresh", action="store_true", help="刷新快照与浮标")
    ap.add_argument("--status", action="store_true", help="打印浮标状态")
    ap.add_argument("--pending", nargs="+", metavar=("G", "N"), help="打印某组待办（G [N]）")
    a = ap.parse_args()
    if a.refresh:
        refresh()
    elif a.claims:
        per_host, _tree = scan_outline()
        m, u = write_claims(per_host, load_routed())
        print("认领清单已生成：", {k: v["hosts"] for k, v in m.items()}, "未归组", len(u))
    elif a.status:
        status()
    elif a.pending:
        pending(a.pending[0], int(a.pending[1]) if len(a.pending) > 1 else 20)
    else:
        ap.print_help()
