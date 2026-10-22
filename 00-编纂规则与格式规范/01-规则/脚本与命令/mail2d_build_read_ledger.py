# -*- coding: utf-8 -*-
"""生成 mail2d 已读区间台账 `mail2d_read_ledger.json`。

口径（2026-09-18 主理人批准；2026-09-19 补「预建队列」修正）：
  1. `records` = 每库**已判读**区间（offset 按行序、左闭右开），合并自现存批次 spec（`_batch_*.json`）；
     历史批次 spec 已删者**不计入 records**（故 records 为下界）。
  2. `read_effective` = 权威已读封数：`catalog` 标记 `completed` 的库视为读毕（= 全库封数）；
     其余库取 `read_judged`（见下）。
  3. `status_source` 标注判定来源：`catalog-completed` / `spec-only`。
  4. 🆕 **预建队列修正**：深队列预建（`_prep_batches.py`）会先建 spec、后判读，若把这类 spec 计入
     已读会**系统性高估**已读量。故约定：预建 spec 带 `"queued": true` 标记，**且**其 `review_logs/
     <tag>_claim_map.json` 尚不存在时，视为「待判读」——不计入 `records`/`read_judged`，
     另记入 `queued_records`/`queued_spec`。判读落库后（claim_map 生成）自动转为已判读，
     标记无需手工清除。
     ⚠ 无该标记的 spec 一律按旧口径计入（保证他线数值不变）。

用途：为措施 ③「优先清最易闭环库」提供精确补挖起点；由 `bookkeep` 在每批提交后追加 records。

用法: C:/Python314/python.exe _build_read_ledger.py
只读 catalog/spec，只写 ledger（不改其他文件）。
"""
import collections
import datetime
import glob
import io
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = r"d:\librebsd"
MAILDIR = os.path.join(ROOT, "03-原始史料库", "11-邮件列表史料")
RL = os.path.join(HERE, "review_logs")
SCOPE_DIRS = ("01-freebsd", "02-netbsd", "03-openbsd", "04-dragonfly", "06-other-bsd")

SCOPE = set()
for _d in SCOPE_DIRS:
    for _sub in ("db", "duckdb"):
        for _f in glob.glob(os.path.join(MAILDIR, _d, _sub, "*.duckdb")):
            SCOPE.add(os.path.basename(_f)[:-7])

cat = json.load(io.open(os.path.join(HERE, "mail2d_catalog_by_size.json"), encoding="utf-8"))

iv = collections.defaultdict(list)      # 已判读（或旧口径）区间
ivq = collections.defaultdict(list)     # 预建待判读区间
for _f in sorted(glob.glob(os.path.join(HERE, "_batch_*.json"))):
    try:
        _d = json.load(io.open(_f, encoding="utf-8"))
    except Exception:
        continue
    _lib, _off, _n = _d.get("lib"), _d.get("offset"), _d.get("n")
    if not (_lib and isinstance(_off, int) and isinstance(_n, int)):
        continue
    if str(_d.get("tag", "")).endswith("dry001"):
        continue
    _tag = _d.get("tag")
    # 预建待判读：带 queued 标记 且 尚无 claim_map（已判读者自动转为已读）
    _queued = bool(_d.get("queued")) and not os.path.exists(
        os.path.join(RL, "%s_claim_map.json" % _tag))
    (ivq if _queued else iv)[_lib].append((_off, _off + _n, _tag))


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


items = {}
for x in cat["items"]:
    lib = x["db"][:-7]
    if lib not in SCOPE or not isinstance(x.get("messages"), int):
        continue
    tot = x["messages"]
    stt = x.get("traversal_status")
    merged, cov_judged = merge(iv.get(lib, []))
    merged_q, cov_q = merge(ivq.get(lib, []))
    read_spec = min(cov_judged + cov_q, tot)
    read_judged = min(cov_judged, tot)
    queued_spec = min(cov_q, tot)
    if stt == "completed":
        read_eff = tot
        src = "catalog-completed"
    else:
        read_eff = read_judged
        src = "spec-only"
    items[lib] = {
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

out = {
    "updated": datetime.date.today().isoformat(),
    "note": "records 为**已判读**区间（行序、左闭右开），合并自现存批次 spec（下界）；"
            "带 \"queued\": true 且尚无 claim_map 的预建 spec 不计入 records，另记 queued_records。"
            "read_effective 对 catalog completed 库取全库封数（权威），其余取 read_judged；"
            "read_spec（旧口径）仍为全部 spec 覆盖之和，保留供对照。",
    "items": items,
}
lp = os.path.join(HERE, "mail2d_read_ledger.json")
io.open(lp, "w", encoding="utf-8", newline="\n").write(json.dumps(out, ensure_ascii=False, indent=1))

tot_msg = sum(v["messages"] for v in items.values())
tot_eff = sum(v["read_effective"] for v in items.values())
tot_spec = sum(v["read_spec"] for v in items.values())
tot_q = sum(v["queued_spec"] for v in items.values())
done = sum(1 for v in items.values() if v["status"] == "completed")
print("[ledger] %s" % lp)
print("  库 %d ｜ 全库 %d 封" % (len(items), tot_msg))
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
