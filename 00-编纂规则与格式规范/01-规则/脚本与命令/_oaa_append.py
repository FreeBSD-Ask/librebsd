import sys
import json

out_path = sys.argv[1]
seg_path = sys.argv[2]
mode = sys.argv[3] if len(sys.argv) > 3 else "a"

with open(seg_path, "r", encoding="utf-8") as f:
    items = json.load(f)

if not isinstance(items, list):
    raise SystemExit("segment file must hold a JSON array")

with open(out_path, mode, encoding="utf-8", newline="\n") as f:
    for obj in items:
        f.write(json.dumps(obj, ensure_ascii=False) + "\n")

print("appended=%d mode=%s" % (len(items), mode))
