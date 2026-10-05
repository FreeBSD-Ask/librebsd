import json
import sys
from collections import Counter

OUT = r"D:\librebsd\script\_db_row_mining\audit_outline\judgements\f4b10_s052.jsonl"
SHARD = r"D:\librebsd\script\_db_row_mining\audit_outline\shards\f4b10_s052.jsonl"
ALLOWED = {"keep", "fix-format", "fix-text", "fix-db", "remap", "存疑"}
BAD = ("「", "」", "『", "』", '"', "*")

with open(SHARD, "r", encoding="utf-8") as fh:
    shard = [json.loads(x) for x in fh if x.strip()]
with open(OUT, "r", encoding="utf-8") as fh:
    out = [json.loads(x) for x in fh if x.strip()]

print("shard_lines=%d  out_lines=%d  line_count_match=%s" % (len(shard), len(out), len(shard) == len(out)))

key_ok = all(a["key"] == b["key"] for a, b in zip(shard, out))
print("key_verbatim_match=%s" % key_ok)
if not key_ok:
    for i, (a, b) in enumerate(zip(shard, out), 1):
        if a["key"] != b["key"]:
            print("  LINE %d MISMATCH" % i)
            print("    shard: %r" % a["key"])
            print("    out  : %r" % b["key"])
            break

sk = [x["key"] for x in shard]
print("shard_keys_unique=%s  out_keys_unique=%s" % (len(set(sk)) == len(sk),
                                                    len({x["key"] for x in out}) == len(out)))

verd = Counter(x["判定"] for x in out)
print("verdict_distribution=%s" % dict(sorted(verd.items())))
print("all_verdicts_allowed=%s" % all(v in ALLOWED for v in verd))

smap = {x["key"]: x["summ_line"] for x in shard}
fix_bad, keep_bad, cmin, cmax, lmax = 0, 0, 10 ** 9, 0, 0
for r, s in zip(out, shard):
    sl = r["key"]
    verd_ = r["判定"]
    if verd_ not in ALLOWED:
        keep_bad += 1
        print("  BAD_VERDICT %s" % sl)
    if verd_ in ("fix-format", "fix-text"):
        n = r["新摘要句"]
        if n.count("引用时按") != 1:
            fix_bad += 1
            print("  MARKER!=1 %s count=%d" % (sl, n.count("引用时按")))
        else:
            body, tail = n.split("引用时按")
            if tail != smap[sl].split("引用时按")[1]:
                fix_bad += 1
                print("  TAIL_MISMATCH %s" % sl)
            c = sum(1 for ch in body.rstrip("。") if ord(ch) > 0x2E7F)
            cmin, cmax = min(cmin, c), max(cmax, c)
            lmax = max(lmax, len(n))
            if not (30 <= c <= 80) or len(n) > 200 or any(b in body for b in BAD):
                fix_bad += 1
                print("  GATE_FAIL %s C=%d len=%d badchar=%s" % (sl, c, len(n),
                                                                  [b for b in BAD if b in body]))
    else:
        body = smap[sl].split("引用时按")[0]
        c = sum(1 for ch in body.rstrip("。") if ord(ch) > 0x2E7F)
        lmax = max(lmax, len(body + "引用时按"))
        if not (30 <= c <= 80) or any(b in body for b in BAD):
            keep_bad += 1
            print("  KEEP_GATE_FAIL %s C=%d badchar=%s" % (sl, c, [b for b in BAD if b in body]))

print("fix_rows=%d  fix_gate_fail=%d  other_gate_fail=%d"
      % (sum(1 for r in out if r["判定"] in ("fix-format", "fix-text")), fix_bad, keep_bad))
print("fix_C_range=[%d,%d]  longest_total=%d" % (cmin, cmax, lmax))
