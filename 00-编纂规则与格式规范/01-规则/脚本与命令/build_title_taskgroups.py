#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_title_taskgroups.py —— 按卷任务组注册表与任务卡再生器（2026-10-29 立）。

用途
----
把 Task 3A.6（全卷小节标题设计）拆成 76 个**互相独立、可按卷并行**的任务组：
`05-卷册大纲/映射/parallel/title/taskgroups.tsv`（注册表，76 行）与
`05-卷册大纲/映射/parallel/title/V{NN}/task.md`（每卷任务卡）。

数据源
------
`05-卷册大纲/映射/targets.tsv`（仅 status=active 的卷／章／节）
`05-卷册大纲/映射/mapping.tsv`（各节节点命中的旧料件与字节）
旧树文件（`旧大纲-20261023/`）实际字节。

口径
----
- 节数：targets 实测；已批卷改用该卷台账实测（V01 因 2.3 拆节记 61，ykla 2026-10-29 已批）。
- 标题估算：J3 每节 2—12，中位 6；已批卷改用 `title.ok` 的 `title_count` 实测。
- 状态：由 `title-design/approved/V{NN}.title.ok` 派生（存在且台账在盘即 approved，否则 pending）；
  不再按卷号写死。
- `no_corpus_sections`：mapping.tsv 命中 0 行的节数，与标题层 `corpus_gap` 例外口径不同。
- 波次（wave）：仅排班提示，组间无依赖。

用法
----
`python build_title_taskgroups.py [--root PATH] [--check]`

`--check` 只比对磁盘与再生结果，不写盘（漂移 exit 1）。
"""
import argparse
import csv
import io
import os
import sys

HDR = ["group_id", "vol", "vol_title", "chapters", "sections", "no_corpus_sections",
       "mapped_files", "corpus_bytes", "titles_est_min", "titles_est_target",
       "titles_est_max", "wave", "status", "outputs"]


def approved_info(mapd, v):
    """读 `approved/V{NN}.title.ok` 与该卷台账；齐备返回 dict，否则 None。

    status 与实测计数只由批准标记派生，不在脚本里按卷号写死。
    """
    ok = os.path.join(mapd, "title-design", "approved", "V%02d.title.ok" % v)
    led = os.path.join(mapd, "title-design", "V%02d.tsv" % v)
    if not (os.path.exists(ok) and os.path.exists(led)):
        return None
    kv = {}
    for ln in io.open(ok, encoding="utf-8").read().split("\n"):
        if "=" in ln:
            k, val = ln.split("=", 1)
            kv[k.strip()] = val.strip()
    lines = [ln for ln in io.open(led, encoding="utf-8").read().split("\n") if ln.strip()]
    hdr = lines[0].split("\t")
    body = [dict(zip(hdr, ln.split("\t"))) for ln in lines[1:]]
    nsec = len({(r["chapter"], r["section"]) for r in body})
    return {"count": int(kv.get("title_count") or len(body)),
            "sha": kv.get("ledger_sha256", ""), "nsec": nsec}


def build(root):
    mapd = os.path.join(root, "05-卷册大纲", "映射")
    targets = os.path.join(mapd, "targets.tsv")
    mapping = os.path.join(mapd, "mapping.tsv")

    vols, chs, secs = {}, {}, {}
    with io.open(targets, encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            if r.get("status") != "active":
                continue
            if r["level"] == "vol":
                vols[int(r["vol_no"])] = r["title"]
            elif r["level"] == "ch":
                chs.setdefault(int(r["vol_no"]), set()).add(r["ch_no"])
            elif r["level"] == "sec":
                secs.setdefault(int(r["vol_no"]), []).append(r["node_id"])

    per_target, path_bytes, rows_map = {}, {}, []
    with io.open(mapping, encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            tid = r["target_id"]
            rows_map.append(r)
            if not tid:
                continue
            per_target[tid] = per_target.get(tid, 0) + 1
            p = r["source_relpath"]
            if p not in path_bytes:
                full = os.path.join(root, p)
                path_bytes[p] = os.path.getsize(full) if os.path.exists(full) else 0

    out = []
    for v in sorted(vols):
        ids = set(secs.get(v, []))
        files = sum(per_target.get(n, 0) for n in ids)
        nohis = sum(1 for n in ids if per_target.get(n, 0) == 0)
        seen = {r["source_relpath"] for r in rows_map if r["target_id"] in ids}
        nbytes = sum(path_bytes.get(p, 0) for p in seen)
        nsec = len(ids)
        info = approved_info(mapd, v)
        status = "approved" if info else "pending"
        if info:
            nsec = info["nsec"]
        titles_min, titles_mid, titles_max = 2 * nsec, 6 * nsec, 12 * nsec
        if info:
            titles_min = titles_mid = titles_max = info["count"]
        wave = 1 if v == 1 else (v - 2) // 8 + 1
        outs = ("title-design/V%02d.tsv;title-evidence/V%02d.tsv;"
                "exceptions/V%02d.tsv(按需);V%02d-标题呈审报告.md" % (v, v, v, v))
        out.append([("TG-V%02d" % v), str(v), vols[v], str(len(chs.get(v, ()))),
                    str(nsec), str(nohis), str(files), str(nbytes), str(titles_min),
                    str(titles_mid), str(titles_max), str(wave), status, outs])
    return out


def render_tsv(rows):
    lines = ["\t".join(HDR)] + ["\t".join(r) for r in rows]
    return "\n".join(lines) + "\n"


def render_card(r, sha=""):
    (gid, vol, vt, ch, sec, nohis, files, nbytes, tmin, tmid, tmax,
     wave, status, _outs) = r
    v = int(vol)
    extra = ""
    if status == "approved":
        extra = ("- **已批**：%s 条定稿，ledger_sha256=%s…；tag 与批准时间见 "
                 "`映射/里程碑tag台账.tsv`。本组不再重复作业。\n"
                 % (tmid, (sha or "?")[:8]))
    if status == "approved":
        title_line = "- 已定稿标题：%s 条（台账实测；J3 每节 2—12）\n" % tmid
    else:
        title_line = "- 预计标题：%s–%s（中位 %s；J3 每节 2—12）\n" % (tmin, tmax, tmid)
    return "".join([
        "# %s 第 %s 卷 标题设计任务组\n\n" % (gid, vol),
        "> 协议：`../README.md`；注册表：`../taskgroups.tsv`（本组数值以该行为准）。\n",
        "> 状态：`%s`；波次：%s（波次仅是排班提示，互不依赖）。\n\n" % (status, wave),
        "## 一、范围\n\n",
        "- 卷题：%s\n" % vt,
        "- 章数 %s；节数 %s（V01 已含 2.3 拆节 6 节，其余卷按 `targets.tsv` 实测）；"
        "`mapping.tsv` 命中 0 行的节 %s 个\n" % (ch, sec, nohis),
        "- 旧料：映射件 %s 件、%s 字节（`mapping.tsv` 该卷节点命中）\n" % (files, nbytes),
        title_line,
        extra,
        "\n## 二、产出（只写这些）\n\n",
        "- `05-卷册大纲/映射/title-design/V%02d.tsv`\n" % v,
        "- `05-卷册大纲/映射/title-evidence/V%02d.tsv`\n" % v,
        "- `05-卷册大纲/映射/title-design/exceptions/V%02d.tsv`（有例外才建）\n" % v,
        "- `05-卷册大纲/映射/title-design/V%02d-标题呈审报告.md`\n" % v,
        "- `05-卷册大纲/映射/parallel/title/V%02d/{claim,counts.tsv,done.json}`\n" % v,
        "\n## 三、禁止\n\n",
        "- 不写他人卷台账；不写 `approvals.tsv`／`approved/`／`outline.txt`／`index.html`／树内 `.md`\n",
        "- 不建旁路副本；不改本卡数值（数值由注册表再生）\n",
        "\n## 四、作业顺序\n\n",
        "1. `claim` 原子创建（存在即让出）。\n",
        "2. 读 `data/outline.txt` 本卷段落＋`targets.tsv` 本卷节点＋`mapping.tsv` 对应件。\n",
        "3. 按 `title-design/风格规范.md` 八步拟题；无史料节标题避用拉丁字母，免踩三源下限。\n",
        "4. `python 00-编纂规则与格式规范/01-规则/脚本与命令/audit_title_consistency.py --check` 须 FAIL 0。\n",
        "5. 写 `done.json`（titles／ledger_sha256／selftest_exit=0）→ 呈 ykla 卷级批准"
        "（合并者写 `title.ok`）。\n",
    ])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=None)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    root = a.root or os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
    rows = build(root)
    mapd = os.path.join(root, "05-卷册大纲", "映射")
    shas = {}
    for r in rows:
        if r[12] == "approved":
            info = approved_info(mapd, int(r[1]))
            shas[int(r[1])] = info["sha"] if info else ""
    tsv = render_tsv(rows)
    drift = 0
    for r in rows:
        p = os.path.join(root, "05-卷册大纲", "映射", "parallel", "title",
                         "V%02d" % int(r[1]), "task.md")
        card = render_card(r, shas.get(int(r[1]), ""))
        if a.check:
            cur = io.open(p, encoding="utf-8").read() if os.path.exists(p) else ""
            if cur != card:
                print("漂移：%s" % p)
                drift += 1
        else:
            os.makedirs(os.path.dirname(p), exist_ok=True)
            with io.open(p, "w", encoding="utf-8", newline="\n") as f:
                f.write(card)
    reg = os.path.join(root, "05-卷册大纲", "映射", "parallel", "title", "taskgroups.tsv")
    if a.check:
        cur = io.open(reg, encoding="utf-8").read() if os.path.exists(reg) else ""
        if cur != tsv:
            print("漂移：%s" % reg)
            drift += 1
        print("check：%d 组，漂移 %d" % (len(rows), drift))
        return 1 if drift else 0
    with io.open(reg, "w", encoding="utf-8", newline="\n") as f:
        f.write(tsv)
    print("已再生：注册表 %d 组、任务卡 %d 件" % (len(rows), len(rows)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
