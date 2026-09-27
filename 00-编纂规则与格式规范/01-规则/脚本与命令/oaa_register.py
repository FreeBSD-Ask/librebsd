#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""oaa_register.py — 把判定 JSONL 批量登记进 processed.jsonl（幂等，同 key 覆盖）

用法：python oaa_register.py <judgement.jsonl> [more.jsonl ...]
每行格式：{"key": ..., "判定": keep|fix-format|fix-text|remap|fix-db|存疑,
          "问题": [...], "备注": ..., "新摘要": ...（可选）}
"""
import datetime
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
PROC = os.path.join(ROOT, "script", "_db_row_mining", "audit_outline", "processed.jsonl")


def main(paths):
    os.makedirs(os.path.dirname(PROC), exist_ok=True)
    lines = []
    if os.path.exists(PROC):
        with open(PROC, encoding="utf-8") as fh:
            lines = [l for l in fh.read().splitlines() if l.strip()]
    by_key = {}
    for l in lines:
        try:
            r = json.loads(l)
            by_key[r["key"]] = l
        except (ValueError, KeyError):
            continue
    n_in = n_new = n_upd = 0
    for p in paths:
        with open(p, encoding="utf-8") as fh:
            for l in fh:
                l = l.strip()
                if not l:
                    continue
                r = json.loads(l)
                key = r["key"]
                jd = r.get("判定") or ("fix-text" if r.get("新摘要句") else None)
                assert jd in ("keep", "fix-format", "fix-text", "remap",
                              "fix-db", "存疑"), f"非法判定 {key}"
                r["判定"] = jd
                r.setdefault("时间", datetime.datetime.now().isoformat(timespec="seconds"))
                r.setdefault("批次", os.path.basename(p).rsplit(".", 1)[0])
                by_key[key] = json.dumps(r, ensure_ascii=False)
                n_in += 1
    with open(PROC, "w", encoding="utf-8") as fh:
        fh.write("\n".join(by_key[k] for k in sorted(by_key)) + "\n")
    print(f"登记 {n_in} 条 ｜ processed 总量 {len(by_key)} ｜ → {os.path.relpath(PROC, ROOT)}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    main(sys.argv[1:])