# -*- coding: utf-8 -*-
r"""全项目长线任务状态聚合器（**只读**）。

设立缘由（2026-09-19）：项目有 11 条跨会话长线，此前**无一张覆盖全部长线的现行登记表**，
接手方须自行判断「自己在哪条线、真值在哪个文件、下一步跑什么命令」。
本脚本把各线的**权威源**逐一探明，产出一张总表；登记表
`01-项目管理/01-编纂规划与报告归档/长线任务总登记表.md` 的数字由本脚本派生。

🔴 本项目**禁止自动化**（2026-09-16 主理人裁定）。本脚本**只读**，不触发任何后台执行、
不写任何文件；其唯一用途是「人在场时一条命令看清全局」。

🔴 本文件真身路径：`01-项目管理/01-编纂规划与报告归档/_longline_status.py`，**不在 `script/`**。
登记表头部旧记 `script/_longline_status.py`（查无此文件），2026-10-09 已订正；备份目录
`script/_backup_longline/` 仍属 `script/`（gitignore），不变。

用法（cwd 任意，路径为仓库根相对）：
  C:/Python314/python.exe 01-项目管理/01-编纂规划与报告归档/_longline_status.py              # 快档总表
  C:/Python314/python.exe 01-项目管理/01-编纂规划与报告归档/_longline_status.py --deep       # 追加各线自带状态命令
  C:/Python314/python.exe 01-项目管理/01-编纂规划与报告归档/_longline_status.py --json       # 同结构 JSON
  C:/Python314/python.exe 01-项目管理/01-编纂规划与报告归档/_longline_status.py --emit-block # 打印可粘贴进登记表的机读块
  C:/Python314/python.exe 01-项目管理/01-编纂规划与报告归档/_longline_status.py --write-block# ★唯一的写操作：仅刷新登记表内的机读块
  C:/Python314/python.exe 01-项目管理/01-编纂规划与报告归档/_longline_status.py --progress   # 全项目总进度（分档口径，不合并不可通约单位）
  C:/Python314/python.exe 01-项目管理/01-编纂规划与报告归档/_longline_status.py --check      # 与登记表内嵌块比对，exit 1=不一致
  选项：--max-age-days N（默认 7）

只读保证：仅以 read_only=True 开库；子进程白名单见 DEEP_ALLOW；**默认与 --check/--json/--emit-block
均不写任何文件**。唯一例外是 `--write-block`：它只重写登记表 `BEGIN…END` 之间的机读块，
写前备份、写后断言「块外内容逐字节未变」（见 write_block 的安全保证五条）。
"""
import collections
import datetime
import io
import json
import os
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = r"D:\librebsd"
DRM = os.path.join(ROOT, "script", "_db_row_mining")
S64 = os.path.join(ROOT, "08-核查报告与多轮复核", "重构2026", "data", "outline.txt")
TRAV = os.path.join(ROOT, "04-现代研究文献", "rowmine_traversal.duckdb")
PY = r"C:/Python314/python.exe"
REGISTRY = os.path.join(ROOT, "01-项目管理", "01-编纂规划与报告归档",
                        "长线任务总登记表.md")
BLOCK_BEGIN = "<!-- LONGLINE_STATUS_BEGIN"
BLOCK_END = "LONGLINE_STATUS_END -->"


def _p(*a):
    return os.path.join(ROOT, *a)


def _read(p):
    return io.open(p, encoding="utf-8", errors="replace").read()


def _src(path):
    """源的 mtime / 大小（新鲜度用；不哈希大库）。"""
    if not os.path.exists(path):
        return None
    st = os.stat(path)
    return {"mtime": datetime.datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%dT%H:%M"),
            "size": st.st_size}


# ---------------------------------------------------------------- 各线探针
def probe_usenet7():
    p = os.path.join(DRM, "_PROGRESS_AUDIT_7GROUPS_20260915.json")
    if not os.path.exists(p):
        return None
    d = json.loads(_read(p))
    tot = sum(v.get("total", 0) for v in d.values())
    read = sum(v.get("read", 0) for v in d.values())
    rem = sum(v.get("remaining", 0) for v in d.values())
    segs = sum(v.get("segs_rem", 0) for v in d.values())
    open_ids = sorted(k for k, v in d.items() if v.get("remaining", 0) > 0)
    return {
        "status": "ACTIVE" if open_ids else "CLOSED",
        "progress": "七组已读 %s/%s（%.2f%%）｜剩余段 %d｜开放组 %s"
                    % ("{:,}".format(read), "{:,}".format(tot), read / tot * 100,
                       segs, ",".join(open_ids) or "无"),
        "values": {"total": tot, "read": read, "remaining": rem,
                   "segments_remaining": segs, "open_lists": open_ids},
        "sources": [os.path.join(DRM, "_PROGRESS_AUDIT_7GROUPS_20260915.json"),
                    os.path.join(DRM, "long_task_state.json")],
    }


# mail2d 范围：01-freebsd / 02-netbsd / 03-openbsd / 04-dragonfly / 06-other-bsd
# （不含 05-linux-kernel 与 07-usenet；用**完整段名**避免 "06-other" 之类前缀误配）
M2_SCOPE = ("01-freebsd", "02-netbsd", "03-openbsd", "04-dragonfly", "06-other-bsd")


def probe_mail2d():
    """mail2d 探针：读**机读台账** `mail2d_read_ledger.json`（登记表 §一 指定的唯一权威）。

    🔴 教训（2026-09-19）：原实现解析 `_MAIL2D_PLAN_HANDOFF.md` 的正则——而该文档由
    `_gen_plan_handoff_merged.py` 生成、自述「可反复重跑刷新」，实际停在 2026-09-17。
    实测其「已覆盖 268,724（9.1%）／闭环库 205/257」已滞后于真值
    （`_report_today_total.py`：已覆盖 512,611（17.4%）／闭环库 215/257）。
    根因＝**把「人手生成的文档」当机读源**。当时改读 catalog（与脚本逐值一致）。

    🔴 教训（2026-10-17 复核）：改读 catalog 后**仍然失真**——`mail2d_catalog_by_size.json`
    的 `generated` 停在 **2026-09-30**，其 `traversal_status` 记 completed 216／in_progress 35／
    pending 6，而台账实况为 completed **246**／in_progress 8／pending 3、已判读
    **2,026,394/2,945,106（68.81%）**。后果＝同一张登记表两处口径互斥（§一 散文行按台账记
    246/257，机读块按 catalog 记 216/257），且 `--write-block` 只会把过期值原样重写一遍。
    根因同前一次：**下界对照源被当成权威源**。登记表 §一 的「权威源」列与 AGENTS.md 均已明记
    「`mail2d_read_ledger.json` 机读台账，唯一权威；`mail2d_catalog_by_size.json` 仅作下界对照」，
    故本探针一律从台账派生，catalog 只作下界附注写在进度串内、不再参与判据。
    """
    p = os.path.join(DRM, "mail2d_read_ledger.json")
    if not os.path.exists(p):
        return None
    items = json.loads(_read(p)).get("items", {})
    vals = list(items.values()) if isinstance(items, dict) else list(items)
    n = len(vals)
    tot = sum(int(v.get("messages") or 0) for v in vals)
    read = sum(int(v.get("read_effective") or 0) for v in vals)
    cnt = collections.Counter(v.get("status") for v in vals)
    comp = cnt.get("completed", 0)
    # catalog 下界对照（天然陈旧，仅附注，不参与判据）
    cp = os.path.join(DRM, "mail2d_catalog_by_size.json")
    note = ""
    srcs = [p]
    if os.path.exists(cp):
        citems = [x for x in json.loads(_read(cp)).get("items", [])
                  if any(s in (x.get("path") or "") for s in M2_SCOPE)]
        ccomp = sum(1 for x in citems if x.get("traversal_status") == "completed")
        note = "｜catalog 下界 %d/%d" % (ccomp, len(citems))
        srcs.append(cp)
    return {
        "status": "ACTIVE" if comp < n else "CLOSED",
        "progress": "闭环库 %d/%d（%.2f%%）｜全库 %s 封｜已判读 %s（%.2f%%）｜"
                    "completed %d／in_progress %d／pending %d%s"
                    % (comp, n, comp / n * 100 if n else 0, "{:,}".format(tot),
                       "{:,}".format(read), read / tot * 100 if tot else 0,
                       cnt.get("completed", 0), cnt.get("in_progress", 0),
                       cnt.get("pending", 0), note),
        "values": {"libs": n, "closed_libs": comp, "total_msgs": tot,
                   "read_effective": read,
                   "in_progress": cnt.get("in_progress", 0), "pending": cnt.get("pending", 0),
                   "completed_msgs": sum(int(v.get("messages") or 0) for v in vals
                                         if v.get("status") == "completed")},
        "sources": srcs,
    }


def _mail2d_cov():
    """mail2d 消息覆盖数：只读运行 `_report_today_total.py` 并解析其「已覆盖」行。

    该脚本口径（其 L135 自述）：**completed 库按全库计 ＋ 非闭环库按现存 spec 区间**（后者为下界）。
    """
    p = os.path.join(DRM, "_report_today_total.py")
    if not os.path.exists(p):
        return None
    try:
        pr = subprocess.run([PY, p], cwd=DRM, capture_output=True, text=True,
                            encoding="utf-8", errors="replace", timeout=900)
        m = re.search(r"已覆盖\s+(\d+)（([\d.]+)%；completed 库按全库计", pr.stdout or "")
        if m:
            return {"covered": int(m.group(1)), "percent": float(m.group(2))}
    except Exception:
        pass
    return None


def probe_h1():
    """H1 探针：**从逐批明细（最细粒度真值）派生**，不采信可能滞后的 totals 计数。

    实测 2026-09-19：`_h1_state.json` 的 `totals.done_batches` 记 2，而 `libs[0].batches`
    已有 3 条 `state=='committed'`（fq_b001/b002/b003）；`libs[0].offset` 亦滞后。
    故本探针以逐批明细为准，并把计数差异作为告警报出（不改动他人状态文件）。
    """
    p = os.path.join(DRM, "_h1_state.json")
    d = _json_totals(p, "H1")
    if d is None:
        return None
    t = d.get("totals", {})
    batches = [b for lib in d.get("libs", []) for b in lib.get("batches", [])]
    done = sum(1 for b in batches if b.get("state") == "committed")
    inprog = sum(1 for b in batches if b.get("state") in ("dumped", "split", "cand", "registered"))
    read_rows = sum(b.get("n", 0) for b in batches
                    if b.get("state") in ("committed", "dumped", "split", "cand",
                                          "registered", "narrated", "outlined"))
    tot = len(batches) or t.get("batches")
    stale = []
    if t.get("done_batches") not in (None, done):
        stale.append("totals.done_batches=%s≠明细 %s" % (t.get("done_batches"), done))
    prog = "%s 库（freebsd-questions）｜%s 行｜批 %s/%s 闭环" % (
        t.get("libs"), "{:,}".format(t.get("rows", 0)), done, tot)
    if inprog:
        prog += "｜在途 %d" % inprog
    if stale:
        prog += "｜⚠ %s（已按明细取值）" % "、".join(stale)
    return {
        "status": "ACTIVE" if (tot or 0) > done else "CLOSED",
        "progress": prog,
        "values": {"libs": t.get("libs"), "rows": t.get("rows"),
                   "read_rows": read_rows, "batches": tot,
                   "done_batches": done, "in_progress": inprog},
        "sources": [p],
    }


def _json_totals(path, label):
    if not os.path.exists(path):
        return None
    d = json.loads(_read(path))
    return d


H3_LIBS = ("freebsd-hackers", "freebsd-current", "freebsd-doc", "freebsd-stable")
H4_LIBS = ("freebsd-gnome", "netbsd-bugs", "openbsd_mail", "pkgsrc-bugs", "tech-kern")
H2_LIBS = ("freebsd-ports", "freebsd-bugs", "freebsd-net", "freebsd-isp")


def probe_h3():
    """H3 探针：从**台账** `mail2d_read_ledger.json` 派生（四库求和），不解析人手文档。

    🔴 教训（2026-10-09）：原实现为 `probe_doc(("script","_db_row_mining","_H3_PROGRESS.md"), …)`，
    而该文件已于 2026-09-28 并入 `_HANDOFF_H3.md` 后**删除** → `--check` 恒报「H3：源缺失」、
    机读块恒记「源缺失」，H3 在聚合器中**永久不可计量**（登记表 §三 与 §十五 2026-10-09
    两处均已自记此缺陷，但直到本次仍未修）。台账是四库唯一权威机读源，故改读台账，
    口径与 §一／§三 手工行、§十六 总进度一致：`read_effective` 求和（台账自述其为权威口径；
    H3 四库均 `in_progress`，故与 `read_judged` 逐值相等，一并记入 values 供对账）。
    """
    p = os.path.join(DRM, "mail2d_read_ledger.json")
    if not os.path.exists(p):
        return None
    items = json.loads(_read(p)).get("items", {})
    tot = eff = jud = 0
    closed = []
    missing = []
    last_tag = {}
    for lib in H3_LIBS:
        rec = items.get(lib)
        if not rec:
            missing.append(lib)
            continue
        tot += rec.get("messages") or 0
        eff += rec.get("read_effective") or 0
        jud += rec.get("read_judged") or 0
        if (rec.get("status") or "") == "completed":
            closed.append(lib)
        tag = _ledger_frontier(rec)
        if tag:
            last_tag[lib] = tag
    n = len(H3_LIBS) - len(missing)
    prog = "%d 库｜%s/%s（%.2f%%）" % (
        n, "{:,}".format(eff), "{:,}".format(tot), eff / tot * 100 if tot else 0)
    if closed:
        prog += "｜已 completed %d（%s）" % (len(closed), "、".join(closed))
    else:
        prog += "｜0 库 completed（四库均 in_progress）"
    if last_tag:
        prog += "｜前沿 " + "、".join("%s@%s" % (k, last_tag[k]) for k in sorted(last_tag))
    if missing:
        prog += "｜⚠ 台账缺库 %s" % "、".join(missing)
    return {
        "status": "ACTIVE" if not closed else ("CLOSED" if len(closed) == n else "ACTIVE"),
        "progress": prog,
        "values": {"libs": n, "libs_found": n, "libs_missing": missing,
                   "closed_libs": len(closed), "messages": tot,
                   "read_effective": eff, "read_judged": jud,
                   "last_batch": last_tag},
        "sources": [p],
    }


def probe_h4():
    """H4 探针：从**台账** `mail2d_read_ledger.json` 派生（五库求和），不读
    `long_task_state_h4.json`。

    🔴 教训（2026-10-15 复核）：原实现读 `long_task_state_h4.json` 的 `totals`，
    而登记表 §一 H4 行已把权威源指定为台账、并明记「`long_task_state_h4.json`
    **已腐化，勿用**」。后果有两层：
      ① `segments` 口径错位——状态文件的 `segments` 是**队列段数**（按
         segment_size 5000 切出的 94 段），登记表记的是**台账 records 段数**
         （tech-kern 1＋openbsd_mail 14）；两者是不同指标，永不相等。
      ② 新鲜度检查看错文件——`check()` 按 `sources` 的 mtime 判「源是否已更新」。
         状态文件停在 2026-10-12 未动，台账却在持续前进（openbsd_mail
         read 28,000→36,000、records 14→18）⇒「台账已前进 4 批」被误判成
         「源未变、真不一致」，`--check` 恒 FAIL，闸门形同虚设。
    与 probe_h3／probe_h5 改指台账的修法同族（probe_h3 的教训即此缺陷的自记版）。
    """
    p = os.path.join(DRM, "mail2d_read_ledger.json")
    if not os.path.exists(p):
        return None
    items = json.loads(_read(p)).get("items", {})
    n = eff = jud = tot = nseg = 0
    closed = []
    missing = []
    last_tag = {}
    for lib in H4_LIBS:
        rec = items.get(lib)
        if not rec:
            missing.append(lib)
            continue
        n += 1
        tot += rec.get("messages") or 0
        eff += rec.get("read_effective") or 0
        jud += rec.get("read_judged") or 0
        recs = rec.get("records") or []
        nseg += len(recs)
        if (rec.get("status") or "") == "completed":
            closed.append(lib)
        tag = _ledger_frontier(rec)
        if tag:
            last_tag[lib] = tag
    prog = "%d 库｜台账 %d 段｜已读 %s/%s（%.2f%%，台账口径）" % (
        n, nseg, "{:,}".format(eff), "{:,}".format(tot),
        eff / tot * 100 if tot else 0)
    if closed:
        prog += "｜已 completed %d（%s）" % (len(closed), "、".join(closed))
    if last_tag:
        prog += "｜前沿 " + "、".join("%s@%s" % (k, last_tag[k]) for k in sorted(last_tag))
    if missing:
        prog += "｜⚠ 台账缺库 %s" % "、".join(missing)
    return {
        "status": "ACTIVE" if not closed else ("CLOSED" if len(closed) == n else "ACTIVE"),
        "progress": prog,
        "values": {"libs": n, "libs_found": n, "libs_missing": missing,
                   "segments": nseg, "closed_libs": len(closed), "messages": tot,
                   "read": eff, "read_judged": jud, "last_batch": last_tag},
        "sources": [p],
    }


def probe_h5():
    """H5 探针：**从逐库明细派生**（lib 级 `total`/`offset`/`remaining`），并与台账
    `mail2d_read_ledger.json` 的 `read_judged` 交叉核对。

    🔴 教训（2026-10-09 实测）：原实现直读 `_h5_state.json` 的 `totals`，而该字段
    **三层陈旧**——`totals.rows` 534,974 vs 逐库 `total` 合计 547,474（差 12,500）；
    `totals.batches` 110 vs 逐库明细实际 108；lib 级 `offset` 合计仅 315,379，
    而台账 `read_judged` 合计 509,695（**18 库落后，合计 194,316 行**）。
    登记表旧注只记了「totals.rows 差 12,479」，严重低估陈旧幅度。
    故本探针一律按逐库明细 ＋ 台账派生，totals 差异作为告警报出、不采信 totals。
    读进覆盖的唯一权威是台账（见登记表 §三）。
    """
    p = os.path.join(DRM, "_h5_state.json")
    d = _json_totals(p, "H5")
    if d is None:
        return None
    libs = d.get("libs", [])
    tot = sum(int(e.get("total") or 0) for e in libs)
    st_off = sum(int(e.get("offset") or 0) for e in libs)
    nb = sum(len(e.get("batches", [])) for e in libs)
    nb_done = sum(1 for e in libs for b in e.get("batches", [])
                  if b.get("state") == "committed")
    lp = os.path.join(DRM, "mail2d_read_ledger.json")
    rj, closed = 0, 0
    srcs = [p]
    if os.path.exists(lp):
        ld = json.loads(_read(lp))
        items = ld.get("items", {}) if isinstance(ld, dict) else {}
        for e in libs:
            it = items.get(e.get("name"))
            if not it:
                continue
            rj += int(it.get("read_judged") or 0)
            if it.get("status") == "completed":
                closed += 1
        srcs.append(lp)
    t = d.get("totals", {})
    stale = []
    if t.get("rows") not in (None, tot):
        stale.append("totals.rows=%s≠逐库合计%s" % (t.get("rows"), "{:,}".format(tot)))
    if t.get("batches") not in (None, nb):
        stale.append("totals.batches=%s≠明细%s" % (t.get("batches"), nb))
    if rj > st_off:
        stale.append("lib offset 合计落后台账%s行" % "{:,}".format(rj - st_off))
    prog = "%s 库｜已读 %s/%s（%.2f%%，台账口径）｜批 %s/%s 闭环" % (
        len(libs), "{:,}".format(rj), "{:,}".format(tot),
        rj * 100.0 / tot if tot else 0.0, nb_done, nb)
    if srcs[-1] == lp:
        prog += "｜台账 closed %d/%d" % (closed, len(libs))
    if stale:
        prog += "｜⚠ %s（已按逐库＋台账取值）" % "、".join(stale)
    return {
        "status": "ACTIVE" if libs else "CLOSED",
        "progress": prog,
        "values": {"libs": len(libs), "rows": tot, "read_rows": rj,
                   "state_offset_sum": st_off, "batches": nb,
                   "done_batches": nb_done, "closed_libs_ledger": closed},
        "sources": srcs,
    }


def _duck(path, sql):
    import duckdb
    c = duckdb.connect(path, read_only=True)
    try:
        return c.execute(sql).fetchall()
    finally:
        c.close()


def probe_t1():
    if not os.path.exists(TRAV):
        return None
    n, done = _duck(TRAV, "SELECT COUNT(*), SUM(CASE WHEN status='done' THEN 1 ELSE 0 END)"
                          " FROM event_window WHERE tier='T1'")[0]
    return {
        "status": "CLOSED" if n == done else "ACTIVE",
        "progress": "事件窗 T1 %d/%d done" % (done, n),
        "values": {"windows": n, "done": done},
        "sources": [TRAV],
    }


def probe_t2():
    if not os.path.exists(TRAV):
        return None
    rows = _duck(TRAV, "SELECT surveyed, claims FROM db_progress"
                       " WHERE lower(db) LIKE '%dragonfly%'")
    if not rows:
        return None
    surveyed, claims = rows[0]
    return {
        "status": "DORMANT",
        "progress": "dragonfly_mail：已 survey %s｜claim %s（窗口级进度见 R2_TASK 文档）"
                    % ("{:,}".format(surveyed or 0), claims or 0),
        "values": {"surveyed": surveyed or 0, "claims": claims or 0},
        "sources": [TRAV],
    }


def probe_s64():
    if not os.path.exists(S64):
        return None
    vol = ch = sec = 0
    for ln in _read(S64).splitlines():
        if ln.startswith("## "):
            ch += 1
        elif ln.startswith("# "):
            vol += 1
        elif ln.startswith("- "):
            sec += 1
    return {
        "status": "ACTIVE",
        "progress": "%d 卷 %d 章 %d 节" % (vol, ch, sec),
        "values": {"volumes": vol, "chapters": ch, "sections": sec},
        "sources": [S64],
    }


def probe_bline():
    """B 线探针：**按队列口径**（`queue.tsv` 的单元中有 `progress.tsv` DONE 事件者）。

    🔴 教训（2026-09-19）：原实现用 `progress.tsv` 的行数当分母（46/103）——**分子分母双错**：
    该文件 103 行含 **DRIFT 等非队列事件**，且其 42 个 DONE 单元里有 **20 个已移出现行队列**
    （B 类 COL_SCAN 历史批次）。`LONGTERM-PLAN.md` §一 明示「队列状态以 `queue.tsv`/`progress.tsv` 为准」，
    正确口径＝**队列内 DONE / 队列单元数**（与 `run_round.py` 输出一致）。
    """
    qp = _p("script", "_bline_queue_20260915", "queue.tsv")
    pp = _p("script", "_bline_queue_20260915", "progress.tsv")
    if not (os.path.exists(qp) and os.path.exists(pp)):
        return None
    qu = [ln.split("\t")[0] for ln in _read(qp).splitlines()[1:] if ln.strip()]
    done = {r[0] for r in (ln.split("\t") for ln in _read(pp).splitlines()[1:])
            if len(r) > 1 and r[1] == "DONE"}
    inn = [u for u in qu if u in done]
    n, d = len(qu), len(inn)
    return {
        "status": "DORMANT" if d < n else "CLOSED",
        "progress": "队列 %d/%d 单元 DONE（%.1f%%）｜另有 %d 个历史 DONE 单元不在现行队列"
                    % (d, n, d / n * 100 if n else 0, len(done - set(qu))),
        "values": {"queue_units": n, "done_in_queue": d,
                   "done_historical": len(done - set(qu))},
        "sources": [qp, pp],
    }


SY_LEDGER = os.path.join(ROOT, "shenyue", "review", "_ledger.json")
SY_ROWS = os.path.join(ROOT, "shenyue", "review", "_ledger.jsonl")
SY_REVIEW = os.path.join(ROOT, "shenyue", "review")


def probe_shenyue():
    """shenyue 目录复核探针（2026-09-20 建立，第 17 条线）。

    口径：
      · `done` ＝**台账口径**（`by_class[*].done_pos` 之和），与 `_s25_ledger.py verify`
        的 `seen` 一致 —— 即「已 append 的条目数」；
      · **在途批**（`.partial-*` 已落但未 append）单列于进度串，**不并入 done** ——
        避免把「未交付」当「已交付」（本项目既有教训：判据必须能自我报警）；
      · `values` 只放随 `_ledger.json`／`_ledger.jsonl` 变化而变化的量，
        `in_flight` 仅入进度串 —— 否则 `.partial` 增长会触发 `--check` 的**假 FAIL**
        （源 mtime 未变而 values 变了）；在途 `.partial` 另行计入 `sources` 以出**过期告警**。
    """
    if not os.path.exists(SY_LEDGER):
        return None
    led = json.loads(_read(SY_LEDGER))
    bc = led.get("by_class", {})
    rows = 0
    if os.path.exists(SY_ROWS):
        rows = sum(1 for ln in _read(SY_ROWS).splitlines() if ln.strip())
    total = sum(v.get("total", 0) for v in bc.values())
    done = sum(v.get("done_pos") or 0 for v in bc.values())
    per = "｜".join("%s %s/%s" % (k, v.get("done_pos") or 0, v.get("total", 0))
                    for k, v in sorted(bc.items()))
    # 在途批：编号 ＝ next_batch_no 的 .partial（任一类）
    inflight, if_batch, if_done = "", None, 0
    bn = led.get("next_batch_no")
    if bn:
        for cls in sorted(bc):
            p = os.path.join(SY_REVIEW, ".partial-%s-BATCH-%04d.md" % (cls, bn))
            if os.path.exists(p):
                n = len(re.findall(r"^### R-\d{4} \| 原条目 O-\d{4}\s*$", _read(p), re.M))
                if_batch, if_done = bn, n
                inflight = "｜在途 BATCH %04d（%s 类 %d 条已落未收口）" % (bn, cls, n)
                break
    srcs = [SY_LEDGER, SY_ROWS]
    if if_batch:
        for cls in sorted(bc):
            p = os.path.join(SY_REVIEW, ".partial-%s-BATCH-%04d.md" % (cls, if_batch))
            if os.path.exists(p):
                srcs.append(p)
                break
    open_ = [k for k, v in bc.items() if v.get("next_pos") is not None]
    return {
        "status": "ACTIVE" if open_ else "CLOSED",
        "progress": "%s｜合计 %s/%s（%.2f%%）｜台账 %d 行%s"
                    % (per, "{:,}".format(done), "{:,}".format(total),
                       done / total * 100 if total else 0, rows, inflight),
        "values": {"total": total, "done": done, "ledger_rows": rows,
                   "next_batch_no": bn, "open_classes": open_},
        "sources": [s for s in srcs if os.path.exists(s)],
    }


def probe_doc(rel, note):
    """文档源：只报路径存在性与 mtime（数字以文档为准，不做机读断言）。"""
    p = _p(*rel)
    if not os.path.exists(p):
        return None
    st = os.stat(p)
    return {
        "status": "文档源",
        "progress": "%s（mtime %s）" % (note, datetime.datetime.fromtimestamp(
            st.st_mtime).strftime("%m-%d %H:%M")),
        "values": {},
        "sources": [p],
    }


def probe_manual(note):
    return {"status": "人工维护", "progress": note, "values": {}, "sources": []}


def _ledger_frontier(rec):
    """取台账某库的**前沿批次标签**：跨全部 records 的最后一条 tag。

    台账有两种记录形态：①单 record 累积 tags（H2／H3 各库，tags 单调追加）；
    ②每批一段 record（H4 `openbsd_mail` 已 19 段，各段 tags 仅 1 条）。
    故必须**倒序扫全部 records** 取末条 tag；只取 `records[0]` 会在形态②下
    错指回**首批**（2026-10-16 实测：openbsd_mail 报 `ob_b001`，实际前沿 `ob_b019`）。
    probe_h2／probe_h3 当前恰因各库均为形态①而数值正确，但代码同样脆弱——
    台账一旦按段拆分即静默错指，故三处统一走本函数。
    """
    for r in (rec.get("records") or [])[::-1]:
        tags = r.get("tags") or []
        if tags:
            return tags[-1]
    return None


def probe_h2():
    """H2 探针：从**台账** `mail2d_read_ledger.json` 派生（四库求和）。

    🔴 教训（2026-10-15 复核）：原实现是 `probe_doc(("_HANDOFF_H2.md"), "交接书已备，未开工")`，
    而 `probe_doc` 恒返回 `values: {}`。后果：任何人跑 `--write-block` 刷新机读块，
    H2 段都会被**压平为空 values**（台账 417,961/489,312＝85.42% 那一版就是这样被抹掉的，
    b112 记录已自记"须外科还原"）——等于 `--write-block` 对 H2 只能破坏、不能修复。
    台账是四库唯一机读权威源，故改读台账，与 probe_h3／probe_h4／probe_h5 同口径
    （`read_effective` 求和）；`ports_remaining` 保留登记表原有字段供 §一 直接引用。
    """
    p = os.path.join(DRM, "mail2d_read_ledger.json")
    if not os.path.exists(p):
        return None
    items = json.loads(_read(p)).get("items", {})
    n = eff = jud = tot = 0
    closed = []
    missing = []
    last_batch = {}
    ports_rem = 0
    for lib in H2_LIBS:
        rec = items.get(lib)
        if not rec:
            missing.append(lib)
            continue
        n += 1
        m = rec.get("messages") or 0
        eff += rec.get("read_effective") or 0
        jud += rec.get("read_judged") or 0
        tot += m
        if lib == "freebsd-ports":
            ports_rem = int(m) - int(rec.get("read_effective") or 0)
        if (rec.get("status") or "") == "completed":
            closed.append(lib)
        tag = _ledger_frontier(rec)
        if tag:
            last_batch[lib] = tag
    prog = "%d 库｜已读 %s/%s（%.2f%%，台账口径）" % (
        n, "{:,}".format(eff), "{:,}".format(tot), eff / tot * 100 if tot else 0)
    if closed:
        prog += "｜已 completed %d（%s）" % (len(closed), "、".join(closed))
    if ports_rem:
        prog += "｜ports 余 %s" % "{:,}".format(ports_rem)
    if last_batch:
        prog += "｜前沿 " + "、".join("%s@%s" % (k, last_batch[k]) for k in sorted(last_batch))
    if missing:
        prog += "｜⚠ 台账缺库 %s" % "、".join(missing)
    return {
        "status": "ACTIVE" if not closed else ("CLOSED" if len(closed) == n else "ACTIVE"),
        "progress": prog,
        "values": {"libs": n, "libs_found": n, "libs_missing": missing,
                   "closed_libs": len(closed), "messages": tot,
                   "read_effective": eff, "read_judged": jud,
                   "ports_remaining": ports_rem, "last_batch": last_batch},
        "sources": [p],
    }


def probe_doc_resilient(rel, note, last):
    """文档源探针的降级版：源在则同 probe_doc；源已被清理则降级为「人工维护」。

    🔴 教训（2026-10-15 复核）：A／B／三方／播客四线的唯一机读源都在 `script/`
    临时区，按 2026-10-09 临时件清理令执行后已不存在 → 探针返回 None 被 collect()
    归为「源缺失」，`--check` 恒报 4 项 FAIL，闸门形同虚设（真不一致反被淹没）。
    与 mig／linux3 同族改走 probe_manual：源缺时降级为 ⚠ 而非 FAIL，并把登记表
    最后记录值留在 note 里（数字仍以登记表为真值）。源目录若重建，自动回到原探针
    口径。与 probe_h3 的修法（改指 durable 台账）并列——此处无 durable 机读源可用，
    只能降级留痕。
    """
    p = _p(*rel)
    if not os.path.exists(p):
        return probe_manual("%s（机读源目录已按临时件规则清理；最后记录：%s；数字以登记表为准）"
                            % (note, last))
    st = os.stat(p)
    return {
        "status": "文档源",
        "progress": "%s（mtime %s）" % (note, datetime.datetime.fromtimestamp(
            st.st_mtime).strftime("%m-%d %H:%M")),
        "values": {},
        "sources": [p],
    }


# ---------------------------------------------------------------- 线定义
LINES = [
    dict(id="usenet7", name="usenet 行级挖掘（7 组）", probe=probe_usenet7,
         resume="读 `01-项目管理/01-编纂规划与报告归档/usenet任务书与交接书/_RESUME.md` → `script/_db_row_mining/_resume.py`",
         health="`script/_db_row_mining/_progress_audit_7groups.py --check-state`",
         deep=[PY, os.path.join(DRM, "_progress_audit_7groups.py"), "--check-state"]),
    dict(id="mail2d", name="mail2d 邮件列表挖掘（257 库）", probe=probe_mail2d,
         resume="读 `01-项目管理/01-编纂规划与报告归档/mail2d任务书与交接书/_MAIL2D_PLAN_HANDOFF.md`",
         health="`script/_db_row_mining/_report_today_total.py`",
         deep=[PY, os.path.join(DRM, "_report_today_total.py")]),
    dict(id="H1", name="mail2d · H1 巨型问答库（freebsd-questions）", probe=probe_h1,
         resume="读 `01-项目管理/01-编纂规划与报告归档/mail2d任务书与交接书/_HANDOFF_H1.md`（唯一交接书）",
         health="`_h1_state.json` ＋ `_h1_resume.py`", deep=None),
    dict(id="H2", name="mail2d · H2 ports/缺陷/网络（4 库）", probe=probe_h2,
        resume="读 `01-项目管理/01-编纂规划与报告归档/mail2d任务书与交接书/_HANDOFF_H2.md`",
        health="`mail2d_read_ledger.json`（H2 四库 read_effective 求和）", deep=None),
    dict(id="H3", name="mail2d · H3 开发者社群/分支/文档", probe=probe_h3,
        resume="读 `01-项目管理/01-编纂规划与报告归档/mail2d任务书与交接书/_HANDOFF_H3.md`",
        health="`mail2d_read_ledger.json`（H3 四库 read_effective 求和）", deep=None),
    dict(id="H4", name="mail2d · H4 NetBSD/OpenBSD/pkgsrc/桌面", probe=probe_h4,
         resume="读 `01-项目管理/01-编纂规划与报告归档/mail2d任务书与交接书/_HANDOFF_H4.md`",
         health="`script/_db_row_mining/mail2d_read_ledger.json`（`long_task_state_h4.json` **已腐化，勿用**）", deep=None),
    dict(id="H5", name="mail2d · H5 小库收尾（27 库）", probe=probe_h5,
         resume="`script/_db_row_mining/_h5_resume.py --status`＋交接书 `01-项目管理/01-编纂规划与报告归档/mail2d任务书与交接书/_HANDOFF_H5.md`",
         health="`_h5_state.json`",
         deep=[PY, os.path.join(DRM, "_h5_resume.py"), "--status"]),
    dict(id="T1", name="事件窗线 T1（九窗）", probe=probe_t1,
         resume="读 `01-项目管理/01-编纂规划与报告归档/事件窗T1与dragonflyT2任务书/_HANDOFF_EVENTWINDOW_20260913.md`",
         health="`rowmine_traversal.duckdb` 表 `event_window`", deep=None),
    dict(id="T2", name="dragonfly 邮件窗口 T2", probe=probe_t2,
         resume="读 `01-项目管理/01-编纂规划与报告归档/事件窗T1与dragonflyT2任务书/R2_TASK_dragonfly_eBgBqB.md`",
         health="`rowmine_traversal.duckdb` 视图 `db_progress`", deep=None),
    dict(id="s64", name="重构2026 目录页", probe=probe_s64,
         resume="`00-编纂规则与格式规范/01-规则/脚本与命令/assemble_index.py`",
         health="`08-核查报告与多轮复核/重构2026/data/outline.txt` 口径", deep=None),
    dict(id="aline", name="A 线 大纲逐文件核查报告", probe=lambda: probe_doc_resilient(
        ("script", "_outline_audit_20260906"), "见该目录 PROGRESS/HANDOFF",
        "97.87%（3,215/3,285 权威覆盖率）"),
        resume="读 `script/_outline_audit_20260906/`", health="`coverage_check.py`", deep=None),
    dict(id="bline", name="B 线 核查报告整改 / 大纲专项治理",
        probe=lambda: (probe_bline() or probe_doc_resilient(
            ("script", "_bline_queue_20260915"), "队列口径（queue.tsv／progress.tsv）",
            "DORMANT 40.0%（22/55 队列单元）")),
        resume="`run_round.py`（无参＝只读）",
        health="`script/_bline_queue_20260915/progress.tsv`", deep=None),
    dict(id="tri", name="三方一致性核查", probe=lambda: probe_doc_resilient(
        ("script", "_outline_consistency_20260914", "out"), "见 out/*.json",
        "见登记表 §九"),
        resume="读 `script/_outline_consistency_20260914/`", health="人工判读", deep=None),
    dict(id="mig", name="迁移准备层 T1–T10", probe=lambda: probe_manual(
        "无机器可读源；见 `01-项目管理/01-编纂规划与报告归档/长线任务交接书-20260915.md` §十二"),
        resume="同上", health="人工判读", deep=None),
    dict(id="podcast", name="播客语义复核", probe=lambda: probe_doc_resilient(
        ("script", "_podcast_semantic_review", "HANDOFF.md"), "见 HANDOFF.md",
        "见登记表 §十一"),
        resume="读 `script/_podcast_semantic_review/HANDOFF.md`", health="人工判读", deep=None),
    dict(id="linux3", name="Linux 战线 Phase 3", probe=lambda: probe_manual(
        "无机器可读源；已由主理人移出长线范围"),
        resume="见 `01-项目管理/` 下 Linux 遗留事项计划", health="人工判读", deep=None),
    dict(id="shenyue", name="shenyue 目录复核（3412 条）",
         probe=lambda: (probe_shenyue() or probe_manual(
             "已收官归档（CLOSED 3,412/3,412，2026-10-17 实测台账全读）；工程目录已由主理人 "
             "2026-10-17 裁决删除（提交 5ec23ec5136c），终态凭证＝changelog＋该提交；数字以登记表为准")),
         resume="（归档线）历史件见提交 5ec23ec5136c 与登记表 §十七；如目录重建则探针自动回到台账口径",
         health="归档线（源已删，仅核登记存在性）", deep=None),
]


def collect():
    out = {}
    for L in LINES:
        try:
            r = L["probe"]()
        except Exception as e:                                  # 探针失败不阻断全表
            r = {"status": "探针失败", "progress": repr(e)[:80], "values": {}, "sources": []}
        if r is None:
            r = {"status": "源缺失", "progress": "权威源不存在", "values": {}, "sources": []}
        r["sources_stat"] = {os.path.relpath(s, ROOT).replace("\\", "/"): _src(s)
                             for s in r.get("sources", [])}
        r["resume"] = L["resume"]
        r["health"] = L["health"]
        r["name"] = L["name"]
        out[L["id"]] = r
    return out


def print_table(res):
    print("=" * 132)
    print("全项目长线任务总表  %s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 132)
    print("%-10s %-34s %-10s %s" % ("id", "线", "状态", "进度（权威源实测）"))
    print("-" * 132)
    for L in LINES:
        r = res[L["id"]]
        print("%-10s %-34s %-10s %s" % (L["id"], L["name"][:34], r["status"], r["progress"]))
    print("-" * 132)
    n_ok = sum(1 for r in res.values() if r["status"] not in ("源缺失", "探针失败"))
    print("共 %d 条线｜权威源可用 %d｜源缺失/失败 %d"
          % (len(LINES), n_ok, len(LINES) - n_ok))


def run_deep(res):
    print("\n" + "=" * 132)
    print("深档探针（各线自带只读状态命令）")
    print("=" * 132)
    for L in LINES:
        if not L.get("deep"):
            print("[%-8s] （无深档探针）" % L["id"])
            continue
        try:
            p = subprocess.run(L["deep"], cwd=L.get("cwd", DRM), capture_output=True, text=True,
                               encoding="utf-8", errors="replace", timeout=300)
            tail = [x for x in ((p.stdout or "") + (p.stderr or "")).splitlines() if x.strip()]
            print("[%-8s] %s" % (L["id"], tail[-1][:110] if tail else "(无输出)"))
        except Exception as e:
            print("[%-8s] 深档失败：%s" % (L["id"], repr(e)[:80]))


def emit_block(res):
    blk = {"generated": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M"),
           "lines": {k: {"name": v["name"], "status": v["status"], "progress": v["progress"],
                         "values": v["values"], "sources": v["sources_stat"]}
                     for k, v in res.items()}}
    print(BLOCK_BEGIN)
    print(json.dumps(blk, ensure_ascii=False, indent=1))
    print(BLOCK_END)


def check(res, max_age_days):
    if not os.path.exists(REGISTRY):
        print("✗ 登记表不存在：%s" % REGISTRY)
        return 1
    t = _read(REGISTRY)
    i = t.find(BLOCK_BEGIN)
    j = t.find(BLOCK_END)
    if i < 0 or j < 0:
        print("✗ 登记表未含机读块（%s … %s）" % (BLOCK_BEGIN, BLOCK_END))
        return 1
    blk = json.loads(t[t.find("\n", i) + 1:j].strip())
    gen = datetime.datetime.strptime(blk["generated"], "%Y-%m-%dT%H:%M")
    fails, warns, stale = [], [], []
    for k, now in res.items():
        old = blk["lines"].get(k)
        if old is None:
            fails.append("%s：登记表缺该线" % k)
            continue
        if now["status"] in ("源缺失", "探针失败"):
            fails.append("%s：%s" % (k, now["status"]))
            continue
        if now["status"] == "人工维护":
            print("  ⚠ %s：人工维护，仅查源存在性（见登记表 §十三）" % k)
            continue
        # 源在机读块生成之后又被更新 → 登记表**过期**（正常现象，刷新即可），不算 FAIL
        newer = []
        for sp, st in now["sources_stat"].items():
            if st is None:
                fails.append("%s：源缺失 %s" % (k, sp))
                continue
            if datetime.datetime.strptime(st["mtime"], "%Y-%m-%dT%H:%M") > gen:
                newer.append(sp)
        if newer:
            stale.append("%s：源已更新（%s），登记表数值可能过期 → 重跑 --emit-block 刷新"
                         % (k, "、".join(newer)))
            continue
        # 源未变而数值不符 → **真不一致**（探针缺陷或机读块被手改）
        if now["values"] and now["values"] != old.get("values"):
            fails.append("%s：数值不一致（源未变，故属真不一致）\n      登记表 %s\n      实  测 %s"
                         % (k, old.get("values"), now["values"]))
    for w in warns + stale:
        print("  ⚠ %s" % w)
    if (datetime.datetime.now() - gen).days > max_age_days:
        print("  ⚠ 登记表机读块生成于 %s，已超 %d 天，建议刷新"
              % (blk["generated"], max_age_days))
    if fails:
        print("\n✗ 一致性检查 FAIL（%d 项）：" % len(fails))
        for f in fails:
            print("   · %s" % f)
        return 1
    print("\n✓ 一致性检查 PASS：%d 条线数值与登记表一致%s"
          % (len(res), "（另有 %d 条过期告警）" % len(stale) if stale else ""))
    return 0


def write_block(res):
    """**唯一写操作**：仅重写登记表内 BEGIN/END 之间的机读块，其余字节必须不变。

    安全保证（缺一不可）：
      ① 仅触碰 REGISTRY 一个文件，且只在 BEGIN…END 之间替换；
      ② 写前备份为 `<registry>.prebak-block-<ts>`；
      ③ 断言 BEGIN/END 各恰 1 处；
      ④ 写后断言「块外内容」与写前**逐字节相同**；
      ⑤ 断言新块可被 json.loads 解析；
      ⑥ **原子替换**：先写同目录临时件（flush＋fsync＋回读断言）再 `os.replace`，
         带 SMB 退避（0/1/3/7/15/30s，共 6 次）；替换全程失败则返回 1 且登记表
         **一字未动**（临时件清理）——原实现在 REGISTRY 上直接 `open("w")` 截断写，
         非原子，写中途失败会留下半份／空文件，且 ④ 无法检测半写（2026-10-15 实测）。
    """
    import datetime
    import shutil
    if not os.path.exists(REGISTRY):
        print("✗ 登记表不存在：%s" % REGISTRY)
        return 1
    old = io.open(REGISTRY, encoding="utf-8").read()
    nb, ne = old.count(BLOCK_BEGIN), old.count(BLOCK_END)
    if nb != 1 or ne != 1:
        print("✗ BEGIN/END 标记数异常（%d/%d），拒绝写入" % (nb, ne))
        return 1
    i, j = old.find(BLOCK_BEGIN), old.find(BLOCK_END)
    blk = {"generated": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M"),
           "lines": {k: {"name": v["name"], "status": v["status"], "progress": v["progress"],
                         "values": v["values"], "sources": v["sources_stat"]}
                     for k, v in res.items()}}
    body = json.dumps(blk, ensure_ascii=False, indent=1)
    json.loads(body)                                    # ⑤ 可解析
    # 幂等：仅当**内容（lines）**变化才写盘；`generated` 时间戳本身不构成变更
    try:
        _old_blk = json.loads(old[old.find("\n", i) + 1:j].strip())
        if _old_blk.get("lines") == blk["lines"]:
            print("  [write-block] 内容（lines）无变化，未写盘（幂等）；generated 保持 %s"
                  % _old_blk.get("generated"))
            return 0
    except Exception:
        pass                                            # 旧块损坏 → 照常重写
    new = old[:i] + BLOCK_BEGIN + "\n" + body + "\n" + old[j:]
    if old[:i] + old[j:] != new[:i] + new[new.find(BLOCK_END):]:
        print("✗ 块外内容自检失败，拒绝写入")
        return 1
    # 备份落到 `script/`（已 gitignore），避免污染受控目录
    _bd = os.path.join(ROOT, "script", "_backup_longline")
    os.makedirs(_bd, exist_ok=True)
    _bn = "长线任务总登记表.md.prebak-block-"
    bak = os.path.join(_bd, _bn + datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
    shutil.copy2(REGISTRY, bak)                         # ②
    # 保留策略：仅留最近 3 个（防累积）
    for _o in sorted(g for g in os.listdir(_bd) if g.startswith(_bn))[:-3]:
        os.remove(os.path.join(_bd, _o))
    # 原子替换：先写同目录临时件，校验后再 os.replace。
    # 教训（2026-10-15 实测）：原实现在 REGISTRY 上直接 open("w") 截断写——非原子，
    # 写中途失败即留下半份／空文件，且 ④ 的「写后断言块外未变」无法检测半写。
    # 实测该 SMB 路径连续 3 次 PermissionError（Errno 13）；改原子替换后失败即
    # 整份未动，登记表永不被半写。os.replace 在 SMB 上 rename-over 已存在文件亦会
    # 突发 WinError 5，故退避重试，且每次重试前先验临时件字节未被改动。
    import time
    _tmp = os.path.join(os.path.dirname(REGISTRY),
                        os.path.basename(REGISTRY) + ".tmp-block-%d" % os.getpid())
    _err = None
    for _a in (0, 1, 3, 7, 15, 30):
        if _a:
            time.sleep(_a)
        with io.open(_tmp, "w", encoding="utf-8", newline="\n") as f:
            f.write(new)
            f.flush()
            os.fsync(f.fileno())
        if io.open(_tmp, encoding="utf-8").read() != new:
            _err = RuntimeError("临时件回读不符")
            continue
        try:
            os.replace(_tmp, REGISTRY)
            _err = None
            break
        except (PermissionError, OSError) as e:
            _err = e
    if _err is not None:
        try:
            os.remove(_tmp)
        except OSError:
            pass
        print("✗ 原子替换失败（%s）；登记表未改动，临时件已清理" % _err)
        return 1
    chk = io.open(REGISTRY, encoding="utf-8").read()
    assert chk[:i] + chk[chk.find(BLOCK_END):] == old[:i] + old[j:], "块外内容被改动"   # ④
    assert chk.count(BLOCK_BEGIN) == 1 and chk.count(BLOCK_END) == 1
    print("  [write-block] 已刷新机读块（%d 条线，generated=%s）；备份 -> %s"
          % (len(res), blk["generated"], os.path.basename(bak)))
    print("  [write-block] 块外内容逐字节未变 ✓")
    return 0


def _usenet43():
    """全库 43 组口径（DB 真值）：只读运行 `_plan_sync_dbtruth.py` 并解析其汇总行。"""
    try:
        pr = subprocess.run([PY, os.path.join(DRM, "_plan_sync_dbtruth.py")], cwd=DRM,
                            capture_output=True, text=True, encoding="utf-8",
                            errors="replace", timeout=900)
        m = re.search(r"total=(\d+)\s+done=(\d+)\s+\(([\d.]+)%\)\s+closed=(\d+)/(\d+)",
                      pr.stdout or "")
        if m:
            return {"total": int(m.group(1)), "done": int(m.group(2)),
                    "percent": float(m.group(3)), "closed": int(m.group(4)),
                    "groups": int(m.group(5))}
    except Exception:
        pass
    return None


def _aline():
    """A 线权威覆盖率：只读运行 `coverage_check.py` 并解析其第②行。"""
    p = _p("script", "_outline_audit_20260906", "coverage_check.py")
    if not os.path.exists(p):
        return None
    try:
        pr = subprocess.run([PY, p], cwd=os.path.dirname(p), capture_output=True,
                            text=True, encoding="utf-8", errors="replace", timeout=900)
        m = re.search(r"权威覆盖率:\s*(\d+)\s*/\s*(\d+)\s*=\s*([\d.]+)%", pr.stdout or "")
        if m:
            return {"done": int(m.group(1)), "total": int(m.group(2)),
                    "percent": float(m.group(3))}
    except Exception:
        pass
    return None


def progress_report(res):
    print("=" * 118)
    print("全项目总进度  %s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 118)
    print("【口径说明】各线单位不可通约（消息数 / 文件数 / 单元数 / 卷章节），故**分档呈现，不强行合并为单一数字**。")
    print("            唯「行级史料挖掘」一档内两语料互不重叠，可相加。子集行以 `└` 标注，**不并入合计**。")
    print()

    # ---------- 一、行级挖掘（消息口径） ----------
    u43, m2 = _usenet43(), res["mail2d"]["values"]
    m2c = _mail2d_cov()                                 # mail2d 消息覆盖（现跑脚本，非过期文档）
    v7 = res["usenet7"]["values"]
    print("一、行级史料挖掘（按消息数；体量主导）")
    print("-" * 118)
    print("%-46s %12s %12s %10s" % ("语料", "已读", "总量", "完成率"))
    tot_d = tot_n = 0
    if u43:
        tot_d += u43["done"]; tot_n += u43["total"]
        print("%-46s %12s %12s %9.2f%%" % ("usenet 全库（43 组 newsgroups）",
                                           "{:,}".format(u43["done"]),
                                           "{:,}".format(u43["total"]), u43["percent"]))
    print("%-46s %12s %12s %9.2f%%" % ("  └ 本线七组（子集，不并入）",
                                       "{:,}".format(v7["read"]), "{:,}".format(v7["total"]),
                                       v7["read"] / v7["total"] * 100))
    m2_total = m2.get("total_msgs")
    m2_done = m2c["covered"] if m2c else None
    if m2_total and m2_done is not None:
        tot_d += m2_done; tot_n += m2_total
        print("%-46s %12s %12s %9.2f%%" % ("mail2d（257 库，含 dragonfly 72,062）",
                                           "{:,}".format(m2_done), "{:,}".format(m2_total),
                                           m2_done / m2_total * 100))
        print("%-46s %12s %12s" % ("  （闭环库比）", "%d/%d" % (m2["closed_libs"], m2["libs"]),
                                   "%.1f%%" % (m2["closed_libs"] / m2["libs"] * 100)))
    print("-" * 118)
    print("%-46s %12s %12s %9.2f%%" % ("合计（usenet 全库 ＋ mail2d）",
                                       "{:,}".format(tot_d), "{:,}".format(tot_n),
                                       tot_d / tot_n * 100))
    print("%-46s %12s" % ("剩余待读", "{:,}".format(tot_n - tot_d)))
    print("  注：mail2d 覆盖数取自 `_report_today_total.py`（现跑）；其口径为"
          "「completed 库按全库计 ＋ 非闭环库按现存 spec 区间」（后者为**下界**）。")
    print("      🔴 `_MAIL2D_PLAN_HANDOFF.md` 的「已覆盖 268,724（9.1%）／闭环库 205/257」已**过期**"
          "（停于 2026-09-17，需重跑 `_gen_plan_handoff_merged.py` 刷新）。")
    print()
    print("  子线明细（均为 mail2d 子集，已含于上行合计）：")
    for k in ("H1", "H2", "H3", "H4", "H5"):
        print("    %-4s %s" % (k, res[k]["progress"]))
    print()

    # ---------- 二、结构 / 编纂线 ----------
    al = _aline()
    bl = res["bline"]["values"]
    print("二、结构 / 编纂线（各自单元，**不与上表相加**）")
    print("-" * 118)
    print("%-46s %12s %12s %10s" % ("线", "已完成", "总量", "完成率"))
    rat = []
    # 体量两线（与上表同源）也计入等权
    if u43:
        rat.append(u43["percent"])
        print("%-46s %12s %12s %9.2f%%" % ("usenet 全库（43 组）", "{:,}".format(u43["done"]),
                                           "{:,}".format(u43["total"]), u43["percent"]))
    if m2_total and m2_done is not None:
        rat.append(m2_done / m2_total * 100)
        print("%-46s %12s %12s %9.2f%%" % ("mail2d（257 库）", "{:,}".format(m2_done),
                                           "{:,}".format(m2_total), m2_done / m2_total * 100))
    if al:
        rat.append(al["percent"])
        print("%-46s %12s %12s %9.2f%%" % ("A 线 大纲逐文件核查报告（权威覆盖率）",
                                           "{:,}".format(al["done"]), "{:,}".format(al["total"]),
                                           al["percent"]))
    if bl.get("queue_units"):
        r = bl["done_in_queue"] / bl["queue_units"] * 100
        rat.append(r)
        print("%-46s %12s %12s %9.2f%%" % ("B 线 核查报告整改（队列单元口径）",
                                           bl["done_in_queue"], bl["queue_units"], r))
    t1 = res["T1"]["values"]
    if t1.get("windows"):
        r = t1["done"] / t1["windows"] * 100
        rat.append(r)
        print("%-46s %12s %12s %9.2f%%" % ("T1 事件窗线（九窗）", t1["done"], t1["windows"], r))
    s64 = res["s64"]["values"]
    print("%-46s %12s" % ("重构2026 目录页", "不可计量（目录已装配：%d 卷 %d 章 %d 节；余为述评撰写，无既定完成率）"
                                             % (s64["volumes"], s64["chapters"], s64["sections"])))
    print("%-46s %12s" % ("T2 dragonfly 窗口线", "不可计量（窗口级进度仅存于 R2_TASK 文档）"))
    print("%-46s %12s" % ("迁移准备层 T1–T10", "人工维护（约 4.5/10，见长线任务交接书 §十二）"))
    print("%-46s %12s" % ("播客语义复核 / 三方一致性", "CLOSED（638/638 卡片 / 16 份报告，已收官）"))
    print()

    # ---------- 三、等权平均 ----------
    print("三、等权平均（**仅计有既定完成率的线**，各线一票）")
    print("-" * 118)
    if rat:
        print("  可计量 %d 条 → 等权平均 **%.2f%%**" % (len(rat), sum(rat) / len(rat)))
    print("  不可计量 %d 条：重构2026／T2／迁移／播客／三方／H2／H3（无既定完成率或已收官）"
          % 7)
    print()
    print("=" * 118)
    print("【结论】不提供「单一总进度」——它取决于口径：")
    print("  · **消息口径（体量主导）**：%.2f%%（%s / %s 封）" % (tot_d / tot_n * 100,
                                                                  "{:,}".format(tot_d), "{:,}".format(tot_n)))
    if rat:
        print("  · **等权口径（各线一票，仅 %d 条可计量）**：%.2f%%" % (len(rat), sum(rat) / len(rat)))
    print("  两者差异极大，原因是 mail2d（%.1f 万封，占语料 %.1f%%）已读仅 %.2f%%，"
          % ((m2_total or 0) / 10000, (m2_total or 0) / tot_n * 100,
             (m2_done or 0) / m2_total * 100 if m2_total else 0))
    print("  故消息口径被 mail2d 主导，等权口径则被已收官的小线抬高。")
    print("  剩余量的 %.1f%% 集中在 mail2d。"
          % (((m2_total or 0) - (m2_done or 0)) / (tot_n - tot_d) * 100))
    print("=" * 118)


def main():
    argv = sys.argv[1:]
    res = collect()
    if "--json" in argv:
        print(json.dumps({k: {kk: v[kk] for kk in ("name", "status", "progress", "values")}
                          for k, v in res.items()}, ensure_ascii=False, indent=1))
    elif "--emit-block" in argv:
        emit_block(res)
    elif "--write-block" in argv:
        sys.exit(write_block(res))
    elif "--progress" in argv:
        progress_report(res)
    elif "--check" in argv:
        n = 7
        if "--max-age-days" in argv:
            n = int(argv[argv.index("--max-age-days") + 1])
        sys.exit(check(res, n))
    else:
        print_table(res)
        if "--deep" in argv:
            run_deep(res)


if __name__ == "__main__":
    main()
