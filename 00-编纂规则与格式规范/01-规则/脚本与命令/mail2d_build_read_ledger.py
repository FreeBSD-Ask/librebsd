# -*- coding: utf-8 -*-
"""生成（重建／追加）mail2d 已读区间台账 `mail2d_read_ledger.json`。

口径（2026-09-18 ykla 批准；2026-09-19 补“预建队列”修正；2026-10-22 收敛为单入口）：
  1. `records` = 每库**已判读**区间（offset 按行序、左闭右开），合并自现存批次 spec（`_batch_*.json`）；
     历史批次 spec 已删者**不计入 records**（故 records 为下界）。
  2. `read_effective` = 权威已读封数：`catalog` 标记 `completed` 的库视为读毕（= 全库封数）；
     其余库取 `read_judged`（见下）。
  3. `status`／`messages` 以 catalog 为真值；catalog 未列的库沿用现有台账条目（不臆造）。
  4. `status_source` 标注判定来源：`catalog-completed` / `spec-only`。
  5. **预建队列修正**：深队列预建（`_prep_batches.py`）会先建 spec、后判读，若把这类 spec 计入
     已读会**系统性高估**已读量。故约定：预建 spec 带 `"queued": true` 标记，**且**其 `review_logs/
     <tag>_claim_map.json` 尚不存在时，视为「待判读」——不计入 `records`/`read_judged`，
     另记入 `queued_records`/`queued_spec`。判读落库后（claim_map 生成）自动转为已判读，
     标记无需手工清除。无该标记的 spec 一律按旧口径计入（保证他线数值不变）。

两种入口（同一套派生逻辑，ADR-0006 §1.3 的单写入口收敛）：
  - **重建**（无参）：`records` 由现存批次 spec 重算，写出整份台账。
  - **追加**（`--append <JSONL>`）：读现有台账 + 批内追加件，按 key 合并去重后原子落盘。
    追加件形制对齐批内 `_ledger_append_<tag>.py` 的 `LO`／`HI`／`TAG` 三常量，一行一条：
    `{"lib": "openbsd_mail", "lo": 125000, "hi": 127000, "tag": "ob_b024"}`（可带 `"queued": true`）。
    **派生值一律按重建口径重算**（read_spec／read_judged／read_effective／records 皆由区间派生），
    不采信追加件自报总数——否则批内脚本的常量漂移会直接污染台账。

用法:
    C:/Python314/python.exe mail2d_build_read_ledger.py                  # 重建
    C:/Python314/python.exe mail2d_build_read_ledger.py --append <JSONL> # 追加合并
    C:/Python314/python.exe mail2d_build_read_ledger.py --selftest       # 判据非空自检

注：本件为 `script/_db_row_mining/_build_read_ledger.py` 的版本化副本（权威副本），
`--append`／`--selftest` 仅在本副本实现；在途批次仍用 `script/` 原件，路径切换另批执行。
重建入口只读 catalog／spec，只写台账；追加入口只读台账与追加件，只写台账。
"""
import argparse
import collections
import datetime
import glob
import io
import json
import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = r"d:\librebsd"
MAILDIR = os.path.join(ROOT, "03-原始史料库", "11-邮件列表史料")
SCOPE_DIRS = ("01-freebsd", "02-netbsd", "03-openbsd", "04-dragonfly", "06-other-bsd")

NOTE = ("records 为**已判读**区间（行序、左闭右开），合并自现存批次 spec（下界）；"
        "带 \"queued\": true 且尚无 claim_map 的预建 spec 不计入 records，另记 queued_records。"
        "read_effective 对 catalog completed 库取全库封数（权威），其余取 read_judged；"
        "read_spec（旧口径）仍为全部 spec 覆盖之和，保留供对照。")


def discover_scope(maildir=MAILDIR):
    """扫描邮件库目录，返回纳入台账的库名集合（无该目录时为空集）。"""
    scope = set()
    for d in SCOPE_DIRS:
        for sub in ("db", "duckdb"):
            for f in glob.glob(os.path.join(maildir, d, sub, "*.duckdb")):
                scope.add(os.path.basename(f)[:-7])
    return scope


def merge(spans):
    """把 (lo,hi,tag) 合并为不重叠区间，返回 (merged, 覆盖行数)。"""
    m = []
    for a, b, t in sorted(spans):
        if m and a <= m[-1]["hi"]:
            m[-1]["hi"] = max(m[-1]["hi"], b)
            m[-1]["tags"].append(t)
        else:
            m.append({"lo": a, "hi": b, "tags": [t]})
    for x in m:
        x["source"] = "spec"
    return m, sum(x["hi"] - x["lo"] for x in m)


def collect_spec_spans(spec_dir, review_logs):
    """从批次 spec 收集区间：返回 (已判读 iv, 预建待判读 ivq, 跳过的文件名)。"""
    iv = collections.defaultdict(list)
    ivq = collections.defaultdict(list)
    skipped = []
    for f in sorted(glob.glob(os.path.join(spec_dir, "_batch_*.json"))):
        try:
            d = json.load(io.open(f, encoding="utf-8"))
        except Exception:
            skipped.append(os.path.basename(f))
            continue
        lib, off, n = d.get("lib"), d.get("offset"), d.get("n")
        if not (lib and isinstance(off, int) and isinstance(n, int)):
            skipped.append(os.path.basename(f))
            continue
        if str(d.get("tag", "")).endswith("dry001"):
            continue
        tag = d.get("tag")
        # 预建待判读：带 queued 标记 且 尚无 claim_map（已判读者自动转为已读）
        queued = bool(d.get("queued")) and not os.path.exists(
            os.path.join(review_logs, "%s_claim_map.json" % tag))
        (ivq if queued else iv)[lib].append((off, off + n, tag))
    return iv, ivq, skipped


def spans_from_ledger(ledger):
    """从现有台账条目还原区间：返回 (iv, ivq, 库→(messages,status) 兜底表)。"""
    iv = collections.defaultdict(list)
    ivq = collections.defaultdict(list)
    fallback = {}
    for lib, it in (ledger.get("items") or {}).items():
        if isinstance(it, dict):
            fallback[lib] = (it.get("messages"), it.get("status"))
        for rec in (it.get("records") or []):
            tags = rec.get("tags") or ([rec["tag"]] if rec.get("tag") else [None])
            for tag in tags:
                iv[lib].append((rec["lo"], rec["hi"], tag))
        for rec in (it.get("queued_records") or []):
            tags = rec.get("tags") or ([rec["tag"]] if rec.get("tag") else [None])
            for tag in tags:
                ivq[lib].append((rec["lo"], rec["hi"], tag))
    return iv, ivq, fallback


def read_append_file(path):
    """读取追加件（JSONL）：返回 (记录列表, 错误文本)；任一行不合法即整体拒绝。"""
    p = os.path.abspath(path)
    if not os.path.exists(p):
        return None, "追加件不存在：%s" % p
    out = []
    try:
        with io.open(p, encoding="utf-8") as f:
            for no, line in enumerate(f, start=1):
                if not line.strip():
                    continue
                try:
                    item = json.loads(line)
                except ValueError as ex:
                    return None, "追加件第 %d 行不是合法 JSON：%s" % (no, ex)
                if not isinstance(item, dict):
                    return None, "追加件第 %d 行须为 JSON 对象" % no
                lib, lo, hi = item.get("lib"), item.get("lo"), item.get("hi")
                tag = item.get("tag")
                if tag is None and isinstance(item.get("tags"), list) and item["tags"]:
                    tag = item["tags"][0]
                if not lib or not isinstance(lo, int) or not isinstance(hi, int):
                    return None, "追加件第 %d 行缺 lib／lo／hi（须为整数）" % no
                if lo < 0 or hi < lo:
                    return None, "追加件第 %d 行区间非法：lo=%s hi=%s" % (no, lo, hi)
                out.append({"lib": str(lib), "lo": lo, "hi": hi,
                            "tag": "" if tag is None else str(tag),
                            "queued": bool(item.get("queued"))})
    except (OSError, UnicodeDecodeError) as ex:
        return None, "追加件读取失败：%s" % ex
    return out, None


def apply_appends(iv, ivq, records):
    """把追加记录并入区间结构。

    去重键＝(lib, tag) + 区间包含：同批 tag 已覆盖 [lo,hi] 即视为重复，不新增行。
    不能按 (lib,lo,hi,tag) 逐字比对——台账把相邻区间合并成一条记录后 lo/hi 已扩张，
    逐字比对会把重复批次当成新批次（自检负例即此项）。
    返回 (新增数, 重复数, 实际新增的记录列表)。
    """
    def covered(pool, lib, lo, hi, tag):
        for a, b, t in pool.get(lib, []):
            if t == tag and a <= lo and b >= hi:
                return True
        return False

    added = dup = 0
    added_recs = []
    for rec in records:
        lib, lo, hi, tag = rec["lib"], rec["lo"], rec["hi"], rec["tag"]
        pool = ivq if rec["queued"] else iv
        other = iv if rec["queued"] else ivq
        if covered(pool, lib, lo, hi, tag) or covered(other, lib, lo, hi, tag):
            dup += 1
            continue
        pool[lib].append((lo, hi, tag))
        added += 1
        added_recs.append(rec)
    return added, dup, added_recs


def derive_item(tot, stt, spans, qspans):
    """单个库的条目派生：区间覆盖 → 四种读量，catalog 的 messages／status 为真值。"""
    merged, cov_judged = merge(spans)
    merged_q, cov_q = merge(qspans)
    read_spec = min(cov_judged + cov_q, tot)
    read_judged = min(cov_judged, tot)
    queued_spec = min(cov_q, tot)
    if stt == "completed":
        read_eff = tot
        src = "catalog-completed"
    else:
        read_eff = read_judged
        src = "spec-only"
    return {
        "messages": tot,
        "status": stt,
        "read_spec": read_spec,
        "read_judged": read_judged,
        "queued_spec": queued_spec,
        "read_effective": read_eff,
        "status_source": src,
        "records": merged,
        "queued_records": merged_q,
    }


def build_items(catalog, scope, iv, ivq, fallback=None):
    """按重建口径派生 items：catalog 给 messages／status，区间给四种读量。"""
    fallback = fallback or {}
    order = []
    base = {}
    for x in (catalog.get("items") or []):
        db = x.get("db")
        if not db:
            continue
        lib = db[:-7] if db.endswith(".duckdb") else db
        base[lib] = (x.get("messages"), x.get("traversal_status"))
        order.append(lib)
    for lib, ms in fallback.items():
        if lib not in base:
            base[lib] = ms
            order.append(lib)

    items = {}
    for lib in order:
        # scope 非空时按邮件库清单过滤；scope 为空（目录不可达／自检）不作过滤，避免静默清空
        if scope and lib not in scope:
            continue
        tot, stt = base[lib]
        if not isinstance(tot, int):
            continue
        items[lib] = derive_item(tot, stt, iv.get(lib, []), ivq.get(lib, []))
    return items


def render(items, updated=None, note=None):
    """组装台账 JSON 对象（updated 缺省取当日；note 缺省为口径说明，追加时沿用原 note）。"""
    return {
        "updated": updated or datetime.date.today().isoformat(),
        "note": NOTE if note is None else note,
        "items": items,
    }


def dumps(out, indent=1):
    """序列化：UTF-8 无 BOM、LF；缩进默认 1（与重建台账形态一致）。"""
    return json.dumps(out, ensure_ascii=False, indent=indent) + "\n"


def detect_indent(raw):
    """探测现有台账的缩进宽度，追加时沿用，避免无谓整文件重排。"""
    text = raw.decode("utf-8", "replace")
    for line in text.split("\n")[1:]:
        if not line.strip():
            continue
        n = len(line) - len(line.lstrip(" "))
        if n and line.lstrip().startswith('"'):
            return n
        break
    return 1


def write_atomic(path, text):
    """原子落盘：同目录临时件 → fsync → os.replace；回读断言与入参逐字节相等。"""
    path = os.path.abspath(path)
    tmp = "%s.tmp-%d" % (path, os.getpid())
    with io.open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
        f.flush()
        os.fsync(f.fileno())
    with io.open(tmp, "rb") as f:
        back = f.read()
    assert back == text.encode("utf-8"), "临时件回读与入参不一致，终止写盘"
    os.replace(tmp, path)


def print_summary(items, lp):
    """打印口径摘要与未闭环库补挖起点（前 15）。"""
    tot_msg = sum(v["messages"] for v in items.values())
    tot_eff = sum(v["read_effective"] for v in items.values())
    tot_spec = sum(v["read_spec"] for v in items.values())
    tot_q = sum(v["queued_spec"] for v in items.values())
    done = sum(1 for v in items.values() if v["status"] == "completed")
    print("[ledger] %s" % lp)
    print("  库 %d ｜ 全库 %d 封" % (len(items), tot_msg))
    if tot_msg <= 0:
        return
    print("  已读（权威口径 read_effective）%d（%.1f%%）｜ 旧口径 read_spec %d（%.1f%%）｜ 其中预建待判读 %d"
          % (tot_eff, tot_eff * 100.0 / tot_msg, tot_spec, tot_spec * 100.0 / tot_msg, tot_q))
    print("  completed 库 %d ｜ 未闭环 %d ｜ 剩余 %d 封" % (done, len(items) - done, tot_msg - tot_eff))
    print("\n  未闭环库补挖起点（按剩余封数升序，前 15）：")
    pend = [(k, v) for k, v in items.items() if v["status"] != "completed"]
    for k, v in sorted(pend, key=lambda y: y[1]["messages"] - y[1]["read_effective"])[:15]:
        hi = max([m["hi"] for m in v["records"]], default=0)
        print("    %-22s 全库 %7d ｜ 已读 %7d ｜ 剩余 %6d ｜ 建议 offset %d%s"
              % (k, v["messages"], v["read_effective"], v["messages"] - v["read_effective"], hi,
                 "  (+预建队列 %d)" % v["queued_spec"] if v["queued_spec"] else ""))


def cmd_rebuild(spec_dir=HERE, review_logs=None, catalog_path=None, ledger_path=None,
                maildir=MAILDIR, quiet=False):
    """重建入口：spec → 台账。返回 (items, 输出路径)。"""
    review_logs = review_logs or os.path.join(spec_dir, "review_logs")
    catalog_path = catalog_path or os.path.join(spec_dir, "mail2d_catalog_by_size.json")
    ledger_path = ledger_path or os.path.join(spec_dir, "mail2d_read_ledger.json")
    cat = json.load(io.open(catalog_path, encoding="utf-8"))
    iv, ivq, skipped = collect_spec_spans(spec_dir, review_logs)
    items = build_items(cat, discover_scope(maildir), iv, ivq)
    out = render(items)
    write_atomic(ledger_path, dumps(out))
    if not quiet:
        for name in skipped:
            print("  ⚠ spec 跳过（无法解析或缺 lib／offset／n）：%s" % name)
        print_summary(items, ledger_path)
    return items, ledger_path


def cmd_append(ledger_path, append_path, catalog_path=None, out_path=None, quiet=False):
    """追加入口：现有台账 + 追加件 → 合并去重 → 只重算涉及的库 → 原子落盘。

    外科口径：只有追加件点名到的库被重算，其余条目**逐字不动**（台账是跨会话共享件，
    整文件重建会把他会话的数据改掉——`ADR-0006` §1.3 的已知风险）。
    返回 (items, 新增数, 重复数, 输出路径)；追加件不合法时抛 ValueError（不写盘）。
    """
    ledger_path = os.path.abspath(ledger_path)
    out_path = out_path or ledger_path
    catalog_path = catalog_path or os.path.join(os.path.dirname(ledger_path),
                                                 "mail2d_catalog_by_size.json")
    records, err = read_append_file(append_path)
    if err:
        raise ValueError(err)

    ledger = {"items": {}}
    if os.path.exists(ledger_path):
        with io.open(ledger_path, encoding="utf-8") as f:
            ledger = json.load(f)
        if not isinstance(ledger, dict):
            raise ValueError("现有台账顶层须为 JSON 对象：%s" % ledger_path)

    iv, ivq, fallback = spans_from_ledger(ledger)
    added, dup, added_recs = apply_appends(iv, ivq, records)

    catalog = {"items": []}
    if os.path.exists(catalog_path):
        catalog = json.load(io.open(catalog_path, encoding="utf-8"))
    cat_map = {}
    for x in (catalog.get("items") or []):
        db = x.get("db")
        if db:
            cat_map[db[:-7] if db.endswith(".duckdb") else db] = (
                x.get("messages"), x.get("traversal_status"))

    items = dict(ledger.get("items") or {})
    changed = []
    for lib in sorted({rec["lib"] for rec in records}):
        ms = cat_map.get(lib) or fallback.get(lib)
        if not ms or not isinstance(ms[0], int):
            print("  ⚠ 追加涉及库 %s 既无 catalog 条目也无台账条目，无法定 messages，跳过" % lib)
            continue
        new = derive_item(ms[0], ms[1], iv.get(lib, []), ivq.get(lib, []))
        old = items.get(lib)
        if old != new:
            diffs = []
            for fld in ("read_spec", "read_judged", "read_effective", "queued_spec",
                        "records", "queued_records"):
                if (old or {}).get(fld) != new.get(fld):
                    diffs.append(fld)
            changed.append("%s（%s）" % (lib, "、".join(diffs)))
            items[lib] = new

    # note 是跨批追加的人类流水账（生产台账已累积 3 万余字），只追加一行、绝不重写
    note = ledger.get("note") or NOTE
    if added:
        stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        desc = "、".join("%s=%s(%d–%d)" % (r["lib"], r["tag"], r["lo"], r["hi"])
                        for r in added_recs)
        note = ("%s｜%s 台账追加（%s；records +%d 条，read_* 按重建口径重算）"
                % (note, stamp, desc, added))
    out = render(items, ledger.get("updated")
                 if added == 0 and ledger.get("updated")
                 else datetime.datetime.now().strftime("%Y-%m-%dT%H:%M"), note)
    text = dumps(out)
    before = None
    if os.path.exists(out_path):
        with io.open(out_path, "rb") as f:
            before = f.read()
        text = dumps(out, detect_indent(before))
    if before != text.encode("utf-8"):
        write_atomic(out_path, text)
    if not quiet:
        print("[ledger] %s（追加 %s：新增 %d 条，重复跳过 %d 条；重算库 %d 个）"
              % (out_path, os.path.basename(append_path), added, dup, len(changed)))
        for line in changed:
            print("    %s" % line)
        print_summary(items, out_path)
    return items, added, dup, out_path


# ── 判据非空自检 ──────────────────────────────────────────────────────────

def _write_json(path, obj):
    with io.open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(obj, ensure_ascii=False, indent=1) + "\n")


def _assert_clean_bytes(path):
    """断言落盘件 UTF-8 无 BOM、无 CR（LF 形态）。"""
    with io.open(path, "rb") as f:
        raw = f.read()
    assert not raw.startswith(b"\xef\xbb\xbf"), "落盘件带 BOM：%s" % path
    assert b"\r" not in raw, "落盘件含 CR：%s" % path
    return raw


def cmd_selftest():
    """正例：空台账 + 2 条追加 ≡ 同输入重建；负例：重复 key 不增行、坏 JSON 拒收且字节不变。"""
    tmp = tempfile.mkdtemp(prefix="mail2d_ledger_")
    fails = []
    try:
        catalog = {"items": [{"db": "lib.duckdb", "messages": 40,
                              "traversal_status": "in_progress"}]}

        # ① 重建基线：两份等价 spec
        spec_dir = os.path.join(tmp, "rebuild")
        os.makedirs(spec_dir)
        os.makedirs(os.path.join(spec_dir, "review_logs"))
        _write_json(os.path.join(spec_dir, "mail2d_catalog_by_size.json"), catalog)
        _write_json(os.path.join(spec_dir, "_batch_t_b001.json"),
                    {"lib": "lib", "offset": 0, "n": 20, "tag": "t_b001"})
        _write_json(os.path.join(spec_dir, "_batch_t_b002.json"),
                    {"lib": "lib", "offset": 20, "n": 20, "tag": "t_b002"})
        rebuilt, _p = cmd_rebuild(spec_dir=spec_dir, maildir=os.path.join(tmp, "nomail"),
                                  quiet=True)

        # ② 追加路径：空台账 + 2 条追加件
        app_dir = os.path.join(tmp, "append")
        os.makedirs(app_dir)
        _write_json(os.path.join(app_dir, "mail2d_catalog_by_size.json"), catalog)
        ledger = os.path.join(app_dir, "mail2d_read_ledger.json")
        _write_json(ledger, {"updated": "2026-10-22", "note": "", "items": {}})
        append_file = os.path.join(app_dir, "append.jsonl")
        with io.open(append_file, "w", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps({"lib": "lib", "lo": 0, "hi": 20, "tag": "t_b001"}) + "\n")
            f.write(json.dumps({"lib": "lib", "lo": 20, "hi": 40, "tag": "t_b002"}) + "\n")
        items, added, dup, out = cmd_append(ledger, append_file, quiet=True)
        if (added, dup) != (2, 0):
            fails.append("正例应新增 2 条、重复 0 条，实际 %d／%d" % (added, dup))
        if items != rebuilt:
            fails.append("正例结果与同输入重建不一致：追加 %r ≠ 重建 %r" % (items, rebuilt))
        rec = items["lib"]["records"]
        if rec != [{"lo": 0, "hi": 40, "tags": ["t_b001", "t_b002"], "source": "spec"}]:
            fails.append("正例 records 未按重建口径合并：%r" % (rec,))
        if items["lib"]["read_effective"] != 40 or items["lib"]["read_spec"] != 40:
            fails.append("正例派生读量不符：%r" % (items["lib"],))
        back = json.loads(_assert_clean_bytes(out).decode("utf-8"))
        if back["items"]["lib"]["records"] != rec:
            fails.append("正例落盘回读与内存结果不符")

        # ③ 重复 key：再跑同一追加件 → 不新增行、台账字节不变
        raw_before = _assert_clean_bytes(out)
        _items2, added2, dup2, out2 = cmd_append(ledger, append_file, quiet=True)
        if added2 != 0 or dup2 != 2:
            fails.append("重复 key 应新增 0 条、跳过 2 条，实际 %d／%d" % (added2, dup2))
        if _assert_clean_bytes(out2) != raw_before:
            fails.append("重复 key 复跑后台账字节被改写")

        # ④ 坏 JSON：整体拒收，台账字节不变、退出码非零
        bad_file = os.path.join(app_dir, "bad.jsonl")
        with io.open(bad_file, "w", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps({"lib": "lib", "lo": 40, "hi": 60, "tag": "t_b003"}) + "\n")
            f.write("{坏 JSON\n")
        rc = _append_rc(ledger, bad_file)
        if rc != 1:
            fails.append("坏 JSON 追加件应返回 1，实际 %d" % rc)
        if _assert_clean_bytes(out) != raw_before:
            fails.append("坏 JSON 拒收后台账字节被改动")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    if fails:
        print("  ❌ 判据非空自检失败：")
        for item in fails:
            print("     - %s" % item)
        return 1
    print("  ✅ 判据非空自检通过：正例（空台账＋2 条追加 ≡ 同输入重建）1／1；"
          "负例（重复 key 不增行、坏 JSON 拒收且字节不变）2／2")
    return 0


def _append_rc(ledger, append_file):
    """自检用：跑一次追加并只回退出码（异常即 1）。"""
    try:
        cmd_append(ledger, append_file, quiet=True)
    except Exception:
        return 1
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description="mail2d 已读区间台账：重建／追加／自检")
    ap.add_argument("--append", metavar="JSONL",
                    help="批内追加件（每行 {lib,lo,hi,tag[,queued]}）；按 key 合并去重")
    ap.add_argument("--ledger", metavar="JSON", help="台账路径（缺省为本目录 mail2d_read_ledger.json）")
    ap.add_argument("--catalog", metavar="JSON", help="catalog 路径（缺省为本目录 mail2d_catalog_by_size.json）")
    ap.add_argument("--maildir", metavar="DIR", help="邮件库根目录（缺省 03-原始史料库/11-邮件列表史料）")
    ap.add_argument("--selftest", action="store_true", help="判据非空自检")
    args = ap.parse_args(argv)

    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    if args.selftest:
        return cmd_selftest()

    maildir = args.maildir or MAILDIR
    ledger = args.ledger or os.path.join(HERE, "mail2d_read_ledger.json")
    if args.append:
        try:
            cmd_append(ledger, args.append, args.catalog)
        except (ValueError, OSError) as ex:
            print("追加失败（未写盘）：%s" % ex)
            return 1
        return 0
    catalog = args.catalog or os.path.join(HERE, "mail2d_catalog_by_size.json")
    if not os.path.exists(catalog):
        print("重建失败：catalog 不存在 %s（本目录为参考件，运行请用 script/_db_row_mining/ 原件）"
              % catalog)
        return 2
    cmd_rebuild(spec_dir=HERE, catalog_path=catalog, ledger_path=ledger, maildir=maildir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
