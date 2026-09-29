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
  python oaa_beacon.py --refresh         # 刷新快照与浮标
  python oaa_beacon.py --status          # 打印浮标状态
  python oaa_beacon.py --pending F1 [N]  # 打印 F1 未处理条目（前 N 条，默认 20）
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
    """扫全量锚点 → {宿主相对路径: {库: n}}；含新增（大纲动态增长自动发现）。"""
    per_host = {}
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
        for db, _sub, _pk in ms:
            libs[db] = libs.get(db, 0) + 1
        per_host[rel] = libs
    return per_host


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


def write_claims(per_host):
    """生成四组认领清单 beacon/claims_F*.txt（宿主相对路径，一行一宿主）。"""
    os.makedirs(BEACON_DIR, exist_ok=True)
    buckets = {"F1": [], "F2": [], "F3": [], "F4": []}
    unclaimed = []
    for rel, libs in sorted(per_host.items()):
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
    per_host = scan_outline()
    claims_meta, unclaimed = write_claims(per_host)
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
        g = group_of(rel, per_host[rel])
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
    prev_pend = {g: (prev.get("progress", {}).get(g, {}) or {}).get("pending", 0) for g in detail}
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
        m, u = write_claims(scan_outline())
        print("认领清单已生成：", {k: v["hosts"] for k, v in m.items()}, "未归组", len(u))
    elif a.status:
        status()
    elif a.pending:
        pending(a.pending[0], int(a.pending[1]) if len(a.pending) > 1 else 20)
    else:
        ap.print_help()
