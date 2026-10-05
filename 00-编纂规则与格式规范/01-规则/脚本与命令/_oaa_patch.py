import sys
import json

out_path = sys.argv[1]
pk = sys.argv[2]
entry_path = sys.argv[3]

with open(entry_path, "r", encoding="utf-8") as f:
    new_entry = json.load(f)

rows = []
with open(out_path, "r", encoding="utf-8") as f:
    for ln in f:
        ln = ln.strip()
        if ln:
            rows.append(json.loads(ln))

hit = 0
for i, r in enumerate(rows):
    if r["key"].split("|")[1] == pk:
        assert r["key"] == new_entry["key"], "key mismatch"
        rows[i] = new_entry
        hit += 1

if hit != 1:
    raise SystemExit("pk %s matched %d rows" % (pk, hit))

with open(out_path, "w", encoding="utf-8", newline="\n") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print("patched pk=%s rows=%d" % (pk, len(rows)))
