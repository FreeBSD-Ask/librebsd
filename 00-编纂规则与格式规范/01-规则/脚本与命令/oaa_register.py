#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""oaa_register.py — 把判定 JSONL 批量登记进 processed.jsonl（幂等，同 key 覆盖）

用法：python oaa_register.py <judgement.jsonl> [more.jsonl ...]
每行格式：{"key": ..., "判定": keep|fix-format|fix-text|remap|fix-db|存疑,
          "问题": [...], "备注": ..., "新摘要": ...（可选）}
"""
import contextlib
import datetime
import io
import json
import os
import shutil
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
PROC = os.path.join(ROOT, "script", "_db_row_mining", "audit_outline", "processed.jsonl")


def _atomic_write(proc, by_key):
    """同目录临时件 → os.replace 原子落盘；UTF-8 无 BOM、LF。
    输出字节与原直接写一致：同序、同 json.dumps 默认分隔符、尾随单个 \\n。"""
    d = os.path.dirname(proc)
    os.makedirs(d, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=d, prefix=".processed.", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as fh:
            fh.write("\n".join(by_key[k] for k in sorted(by_key)) + "\n")
        os.replace(tmp, proc)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def main(paths, ledger=None, dry_run=False):
    proc = os.path.join(ROOT, "script", "_db_row_mining", "audit_outline", ledger or "processed.jsonl")
    if not dry_run:
        os.makedirs(os.path.dirname(proc), exist_ok=True)
    lines = []
    if os.path.exists(proc):
        with open(proc, encoding="utf-8") as fh:
            lines = [l for l in fh.read().splitlines() if l.strip()]
    by_key = {}
    for l in lines:
        try:
            r = json.loads(l)
            by_key[r["key"]] = l
        except (ValueError, KeyError):
            continue
    orig_keys = set(by_key)
    touched = set()
    n_in = 0
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
                touched.add(key)
                n_in += 1
    n_new = len(touched - orig_keys)
    n_upd = len(touched & orig_keys)
    if dry_run:
        print(f"dry-run ｜ 将新增 {n_new} ｜ 将覆盖 {n_upd} ｜ processed 总量 {len(by_key)}（未写盘）")
        return n_in, n_new, n_upd
    _atomic_write(proc, by_key)
    print(f"登记 {n_in} 条 ｜ processed 总量 {len(by_key)} ｜ → {os.path.relpath(proc, ROOT)}")
    return n_in, n_new, n_upd


# ---------------- --selftest：系统临时目录夹具 ----------------
def _put(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if isinstance(data, str):
        data = data.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)


def _mkroot():
    root = tempfile.mkdtemp(prefix="oaa_register_selftest_")
    aud = os.path.join(root, "script", "_db_row_mining", "audit_outline")
    os.makedirs(aud, exist_ok=True)
    _put(os.path.join(aud, "processed.jsonl"),
         json.dumps({"key": "a|1|h.md", "判定": "keep"}, ensure_ascii=False) + "\n")
    return root, aud


def _run_fixture(root, paths, dry_run=False):
    global ROOT
    saved = ROOT
    buf = io.StringIO()
    try:
        ROOT = root
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
            stat = main(paths, None, dry_run)
    finally:
        ROOT = saved
    return stat, buf.getvalue()


def _ledger_bytes(aud):
    with open(os.path.join(aud, "processed.jsonl"), "rb") as fh:
        return fh.read()


def _batch(root, name, rows):
    p = os.path.join(root, name)
    if isinstance(rows, str):
        _put(p, rows)
    else:
        _put(p, "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
    return p


def selftest():
    print("== oaa_register --selftest（系统临时目录夹具）==")
    cases = []
    root, aud = _mkroot()
    try:
        b1 = _batch(root, "in1.jsonl", [
            {"key": "a|1|h.md", "判定": "fix-text", "新摘要句": "改写稿"},
            {"key": "a|1|h.md", "判定": "keep"},
            {"key": "b|2|h.md", "判定": "keep"},
        ])
        _stat1, out1 = _run_fixture(root, [b1])
        raw1 = _ledger_bytes(aud)
        keys1 = sorted(json.loads(x)["key"] for x in raw1.decode("utf-8").splitlines())
        leftovers = [f for f in os.listdir(aud) if f.endswith(".tmp")]
        ok1 = (keys1 == ["a|1|h.md", "b|2|h.md"]) and not leftovers \
            and not raw1.startswith(b"\xef\xbb\xbf") and b"\r\n" not in raw1 \
            and "登记 3 条" in out1 and "processed 总量 2" in out1
        cases.append(("key 去重＋行数守恒＋原子写无残留", ok1, out1.strip().splitlines()[-1]))

        _stat2, out2 = _run_fixture(root, [b1])
        ok2 = _ledger_bytes(aud) == raw1 and "processed 总量 2" in out2
        cases.append(("重跑幂等（台账不增长）", ok2, out2.strip().splitlines()[-1]))

        b2 = _batch(root, "in2.jsonl", [
            {"key": "c|3|h.md", "判定": "keep"},
            {"key": "a|1|h.md", "判定": "keep"},
        ])
        before = _ledger_bytes(aud)
        stat3, out3 = _run_fixture(root, [b2], dry_run=True)
        ok3 = stat3[1:] == (1, 1) and _ledger_bytes(aud) == before \
            and "将新增 1" in out3 and "将覆盖 1" in out3
        cases.append(("--dry-run（只统计不写 ledger）", ok3, out3.strip().splitlines()[-1]))

        bbad = _batch(root, "bad.jsonl", "{坏行非 JSON\n")
        before = _ledger_bytes(aud)
        raised = None
        try:
            _run_fixture(root, [bbad])
        except ValueError as e:
            raised = e
        ok4 = raised is not None and _ledger_bytes(aud) == before
        cases.append(("坏行拒绝（非法 JSON，台账字节不变）", ok4,
                      f"抛出 {type(raised).__name__}，台账未改动"))

        bjudge = _batch(root, "badjudge.jsonl", [{"key": "d|3|h.md", "判定": "bogus"}])
        raised2 = None
        try:
            _run_fixture(root, [bjudge])
        except AssertionError as e:
            raised2 = e
        ok5 = raised2 is not None and _ledger_bytes(aud) == before
        cases.append(("坏行拒绝（非法判定，台账字节不变）", ok5,
                      f"抛出 {type(raised2).__name__}，台账未改动"))
    finally:
        shutil.rmtree(root, ignore_errors=True)

    bad_n = 0
    for title, ok, detail in cases:
        if not ok:
            bad_n += 1
        print(f"[{'PASS' if ok else 'FAIL'}] {title}｜ {detail}")
    print("覆盖：key 去重、坏行拒绝（非法 JSON／非法判定）、写入后行数守恒、原子写、--dry-run")
    print("未覆盖：--ledger 自定义台账名未单列用例（与默认名共用同一原子写实现）")
    print(f"== selftest {'PASS' if bad_n == 0 else 'FAIL'}：{len(cases) - bad_n}/{len(cases)} 用例通过 ==")
    return 0 if bad_n == 0 else 1


if __name__ == "__main__":
    # --help 必须在任何文件访问之前拦下：旧写法只判 `len(sys.argv) < 2`，
    # 显式 `--help` 会被当作判读文件名，先读到台账一半才报 FileNotFoundError
    if any(a in ("-h", "--help") for a in sys.argv[1:]):
        print(__doc__)
        sys.exit(0)
    if "--selftest" in sys.argv[1:]:
        sys.exit(selftest())
    # 只识别已定义开关；其余参数一律按判读文件处理（与旧解析一致）
    dry = "--dry-run" in sys.argv[1:]
    args = [a for a in sys.argv[1:] if a != "--dry-run"]
    if not args:
        print(__doc__)
        sys.exit(2)
    ledger = None
    if "--ledger" in args:
        i = args.index("--ledger"); ledger = args[i+1]; del args[i:i+2]
    if not args:
        print(__doc__); sys.exit(2)
    main(args, ledger, dry)