import sys
import json

out_path = sys.argv[1]
shard_path = sys.argv[2]
only_pks = sys.argv[3:]

VALID = {"keep", "fix-format", "fix-text", "fix-db", "remap", "存疑"}
BAD = ["\u300c", "\u300d", "\u300e", "\u300f", '"', "*"]


def cjk(s):
    return sum(1 for c in s if ord(c) > 0x2E7F)


shard = []
with open(shard_path, "r", encoding="utf-8") as f:
    for ln in f:
        ln = ln.strip()
        if ln:
            shard.append(json.loads(ln))

rows = []
with open(out_path, "r", encoding="utf-8") as f:
    for ln in f:
        ln = ln.strip()
        if ln:
            rows.append(json.loads(ln))

print("shard_lines=%d out_lines=%d" % (len(shard), len(rows)))
print("keys_equal=%s" % ([r["key"] for r in rows] == [s["key"] for s in shard]))

by_pk = {}
for s in shard:
    by_pk[s["pk"]] = s

fix_total = 0
fix_fail = 0
for r in rows:
    pk = r["key"].split("|")[1]
    if only_pks and pk not in only_pks:
        continue
    verd = r["判定"]
    ok = verd in VALID
    msg = "pk=%s verd=%s" % (pk, verd)
    problems = []
    if not ok:
        problems.append("bad_verdict")
    summ = by_pk[pk]["summ_line"]
    tail = summ.split("引用时按", 1)[1] if "引用时按" in summ else None
    if verd in ("fix-format", "fix-text"):
        fix_total += 1
        ns = r.get("新摘要句", "")
        n = ns.count("引用时按")
        if n != 1:
            problems.append("marker_count=%d" % n)
        body = ns.split("引用时按")[0].rstrip("。")
        c = cjk(body)
        total = len(ns)
        if tail is not None and ns.split("引用时按", 1)[1] != tail:
            problems.append("tail_mismatch")
        if c < 30 or c > 80:
            problems.append("C=%d" % c)
        if total > 200:
            problems.append("len=%d" % total)
        for b in BAD:
            if b in body:
                problems.append("badchar")
        status = "PASS" if not problems else "FAIL:%s" % ",".join(problems)
        if problems:
            fix_fail += 1
        print("  %-8s %-7s tail_ok=%s len=%d" % (status, c, tail is not None and ns.split("引用时按", 1)[1] == tail, total))
    else:
        # keep / others: gate-check the current summ_line body
        body = summ.split("引用时按", 1)[0].rstrip("。")
        c = cjk(body)
        total = len(summ)
        note = "C=%d tot=%d" % (c, total)
        if c < 30:
            problems.append("GATE_FAIL_C=%d" % c)
            print("  %-8s %s <-- 现有摘要不达标" % ("FAIL", note))
        elif c > 80 or total > 200:
            problems.append("OVER_C=%d/tot=%d" % (c, total))
            print("  %-8s %s <-- 超长" % ("FAIL", note))
        else:
            print("  ok       %s" % note)

print("fix_total=%d fix_fail=%d" % (fix_total, fix_fail))
