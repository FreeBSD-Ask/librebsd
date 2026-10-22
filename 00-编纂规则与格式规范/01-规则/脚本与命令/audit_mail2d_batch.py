#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""audit_mail2d_batch.py —— 第三十一件门禁：mail2d 批次收口对账。

对象
----
单批 mail2d 的六件产物对账（只读，不改任何输入）：

- spec：`script/_db_row_mining/_batch_<tag>.json`
- 候选表：`review_logs/<tag>_candidates.txt`（`pk|等级|摘要` 或 TSV／JSONL）
- 叙述总表：`review_logs/<tag>_mount_narr.tsv`（`pk\\thost\\t叙述`）
- 认领映射：`review_logs/<tag>_claim_map.json`（扁平 `{pk: CL-RM-NNNNNN}`）
- 库／宿主：`historical_claims.duckdb` 与 `05-卷册大纲/` 宿主 `.md`

判据（逐条独立打印；任一 FAIL 退出码 1）
----
B1 spec 存在，`pk_range` 非空且 `lo <= hi`，`n` 与区间跨度自洽
   （`n <= 跨度`；若 spec 声明 `pk_missing_count`，则 `n + 缺号数 == 跨度`）
B2 候选 pk 唯一、全在 `pk_range` 内，且候选数 `<= n`（判读后子集允许少于 n）
B3 `--narr` 行数等于候选行数，且 pk 集合等于候选 pk 集合
B4 `--claim-map` 键集合等于候选 pk 集合
B5 `--db`：claim_map 的 claim_id 全部在库内存在；本批 min–max 号段连续无洞
   （跨线共享号段只按本批 min/max 检查，不要求全局连续）
B6 `--outline-host`：宿主内本批候选 pk 的 `ROW_MINE` 块数等于候选行数
   （按 `ROW_MINE:` 标记字符串计数，不解析块体全文；可重复给出多个宿主，按合计判）

退出码
------
0 全部 PASS（或无可判项）；1 任一 FAIL；2 依赖缺失（如 `duckdb` 模块或库文件不可用）。

用法
----
    python audit_mail2d_batch.py --tag fhk_b085 \\
        --spec script/_db_row_mining/_batch_fhk_b085.json \\
        --candidates review_logs/fhk_b085_candidates.txt \\
        --narr review_logs/fhk_b085_mount_narr.tsv \\
        --claim-map review_logs/fhk_b085_claim_map.json \\
        --db 04-现代研究文献/historical_claims.duckdb \\
        --outline-host 05-卷册大纲/第05卷-.../097.1-....md
    python audit_mail2d_batch.py --selftest

依赖：仅标准库；`--db` 时另需 `duckdb`。
"""
import argparse
import json
import pathlib
import re
import shutil
import sys
import tempfile

sys.stdout.reconfigure(encoding="utf-8")

REPO = pathlib.Path(__file__).resolve().parents[3]

PK_RE = re.compile(r"^CL-RM-(\d{6})$")
MARK_RE = re.compile(r"ROW_MINE:\s*([^\s]+?)\.messages\.(\d+)")


def _norm_pk(value):
    """把 JSON／文本里的 pk 归一为十进制字符串（兼容 100.0、前后空白）。"""
    if isinstance(value, bool):
        return str(value)
    if isinstance(value, int):
        return str(value)
    text = str(value).strip()
    if re.fullmatch(r"\d+\.0+", text):
        text = text.split(".", 1)[0]
    return text


def parse_spec(path):
    """返回 (spec dict, 错误文本)；spec 不存在／非 JSON 对象均为错误。"""
    p = pathlib.Path(path)
    if not p.exists():
        return None, "spec 不存在：%s" % p
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError) as ex:
        return None, "spec 读取／解析失败：%s" % ex
    if not isinstance(data, dict):
        return None, "spec 顶层须为 JSON 对象"
    return data, None


def parse_range(spec):
    """返回 (lo, hi, 错误文本)。兼容 list／tuple、`lo-hi`、`lo..hi` 三种形态。"""
    raw = spec.get("pk_range")
    if raw is None:
        return None, None, "pk_range 缺失"
    if isinstance(raw, str):
        m = re.fullmatch(r"\s*(\d+)\s*(?:-|\.\.)\s*(\d+)\s*", raw)
        if not m:
            return None, None, "pk_range 字符串无法解析：%r" % raw
        lo, hi = int(m.group(1)), int(m.group(2))
    elif isinstance(raw, (list, tuple)):
        if len(raw) != 2:
            return None, None, "pk_range 须为二元数组，实为 %d 项" % len(raw)
        try:
            lo, hi = int(raw[0]), int(raw[1])
        except (TypeError, ValueError):
            return None, None, "pk_range 含非整数：%r" % (raw,)
    else:
        return None, None, "pk_range 类型非法：%s" % type(raw).__name__
    if lo > hi:
        return None, None, "pk_range 下界 %d 大于上界 %d" % (lo, hi)
    return lo, hi, None


def parse_candidates(path):
    """返回 (pk 列表, 错误文本)。支持 JSON 数组、JSONL、TSV、竖线分隔。"""
    p = pathlib.Path(path)
    if not p.exists():
        return None, "候选表不存在：%s" % p
    text = p.read_text(encoding="utf-8", errors="replace")
    if not text.strip():
        return [], None

    head = text.lstrip()[:1]
    parsed = None
    if head in ("[", "{"):
        try:
            parsed = json.loads(text)
        except ValueError:
            parsed = None
        if parsed is not None:
            if not isinstance(parsed, list):
                return None, "候选 JSON 顶层须为数组"
            out = []
            for i, item in enumerate(parsed, start=1):
                if isinstance(item, dict):
                    key = next((k for k in ("pk", "message_id", "id") if k in item), None)
                    if key is None:
                        return None, "候选 JSON 第 %d 项缺 pk／message_id／id" % i
                    out.append(_norm_pk(item[key]))
                elif isinstance(item, (str, int)):
                    out.append(_norm_pk(item))
                else:
                    return None, "候选 JSON 第 %d 项类型非法" % i
            return out, None

    delim = None
    for line in text.splitlines():
        if line.strip():
            if "\t" in line:
                delim = "\t"
            elif "|" in line:
                delim = "|"
            break
    out = []
    for no, line in enumerate(text.splitlines(), start=1):
        if not line.strip():
            continue
        if line.lstrip().startswith("{"):
            try:
                item = json.loads(line)
            except ValueError as ex:
                return None, "候选 JSONL 第 %d 行解析失败：%s" % (no, ex)
            if not isinstance(item, dict):
                return None, "候选 JSONL 第 %d 行须为对象" % no
            key = next((k for k in ("pk", "message_id", "id") if k in item), None)
            if key is None:
                return None, "候选 JSONL 第 %d 行缺 pk／message_id／id" % no
            out.append(_norm_pk(item[key]))
            continue
        first = line.split(delim, 1)[0] if delim else line.split(None, 1)[0]
        out.append(_norm_pk(first))
    return out, None


def parse_narr(path):
    """返回 (pk 列表, 错误文本)。mount_narr 为 TAB 三列，取第一列。"""
    p = pathlib.Path(path)
    if not p.exists():
        return None, "叙述总表不存在：%s" % p
    out = []
    for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.strip():
            continue
        out.append(_norm_pk(line.split("\t", 1)[0]))
    return out, None


def parse_claim_map(path):
    """返回 (pk -> claim_id dict, 错误文本)。兼容扁平 dict 与 [{pk, claim_id}]。"""
    p = pathlib.Path(path)
    if not p.exists():
        return None, "claim_map 不存在：%s" % p
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError) as ex:
        return None, "claim_map 解析失败：%s" % ex
    out = {}
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict):
                value = value.get("claim_id")
            if value is None:
                return None, "claim_map 键 %s 缺 claim_id" % key
            out[_norm_pk(key)] = str(value).strip()
        return out, None
    if isinstance(data, list):
        for i, item in enumerate(data, start=1):
            if not isinstance(item, dict) or "pk" not in item or "claim_id" not in item:
                return None, "claim_map 数组第 %d 项须含 pk 与 claim_id" % i
            out[_norm_pk(item["pk"])] = str(item["claim_id"]).strip()
        return out, None
    return None, "claim_map 顶层须为对象或数组"


def _fmt_set(items, limit=8):
    items = sorted(items)
    if not items:
        return "无"
    head = "、".join(items[:limit])
    return head + ("…（共 %d 项）" % len(items) if len(items) > limit else "")


def check_b1(tag, spec_path):
    spec, err = parse_spec(spec_path)
    if err:
        return "B1", "FAIL", err
    lo, hi, err = parse_range(spec)
    if err:
        return "B1", "FAIL", "spec pk_range 不可用：%s" % err
    try:
        n = int(spec.get("n"))
    except (TypeError, ValueError):
        n = None
    if n is None or n <= 0:
        return "B1", "FAIL", "spec n 缺失或非正整数"
    span = hi - lo + 1
    missing = spec.get("pk_missing_count")
    if n > span:
        return "B1", "FAIL", "n=%d 大于区间跨度 %d（pk_range %d–%d）" % (n, span, lo, hi)
    if missing is not None:
        try:
            missing = int(missing)
        except (TypeError, ValueError):
            return "B1", "FAIL", "pk_missing_count 非整数：%r" % (spec.get("pk_missing_count"),)
        if n + missing != span:
            return ("B1", "FAIL",
                    "n(%d) + pk_missing_count(%d) != 跨度(%d)（pk_range %d–%d）"
                    % (n, missing, span, lo, hi))
    detail = "spec 存在；pk_range %d–%d（跨度 %d）；n=%d" % (lo, hi, span, n)
    if missing is None and span != n:
        detail += "；未声明缺号，区间含 %d 个空位" % (span - n)
    if spec.get("tag") and spec.get("tag") != tag:
        detail += "；⚠ spec tag=%s 与 --tag=%s 不同（仅提示）" % (spec.get("tag"), tag)
    return "B1", "PASS", detail


def check_b2(spec_path, cand_path):
    cands, err = parse_candidates(cand_path)
    if err:
        return "B2", "FAIL", err
    spec, spec_err = parse_spec(spec_path)
    if spec_err:
        return "B2", "FAIL", "无法取得 pk_range：%s" % spec_err
    lo, hi, rng_err = parse_range(spec)
    if rng_err:
        return "B2", "FAIL", "无法取得 pk_range：%s" % rng_err
    try:
        n = int(spec.get("n"))
    except (TypeError, ValueError):
        n = None

    seen = {}
    for pk in cands:
        seen[pk] = seen.get(pk, 0) + 1
    dups = {k for k, v in seen.items() if v > 1}
    outside = {pk for pk in seen if not re.fullmatch(r"-?\d+", pk)
               or not (lo <= int(pk) <= hi)}
    bad = []
    if dups:
        bad.append("重复 pk：%s" % _fmt_set(dups))
    if outside:
        bad.append("越界 pk：%s（区间 %d–%d）" % (_fmt_set(outside), lo, hi))
    if n is not None and n > 0 and len(cands) > n:
        bad.append("候选 %d 行 > n=%d" % (len(cands), n))
    if bad:
        return "B2", "FAIL", "；".join(bad)
    detail = "候选 %d 行；pk 唯一；全在 %d–%d 内；候选数 ≤ n" % (len(cands), lo, hi)
    if n is not None and len(cands) < n:
        detail += "（判读后子集：%d < %d）" % (len(cands), n)
    return "B2", "PASS", detail


def check_b3(cand_path, narr_path):
    cands, err = parse_candidates(cand_path)
    if err:
        return "B3", "FAIL", "无法取得候选集：%s" % err
    narr, err = parse_narr(narr_path)
    if err:
        return "B3", "FAIL", err
    cand_set, narr_set = set(cands), set(narr)
    bad = []
    if len(narr) != len(cands):
        bad.append("narr %d 行 ≠ 候选 %d 行" % (len(narr), len(cands)))
    if narr_set != cand_set:
        only_c = cand_set - narr_set
        only_n = narr_set - cand_set
        bad.append("pk 集合不符：候选独有 %s；narr 独有 %s"
                   % (_fmt_set(only_c), _fmt_set(only_n)))
    if bad:
        return "B3", "FAIL", "；".join(bad)
    return "B3", "PASS", "narr %d 行；pk 集合与候选一致" % len(narr)


def check_b4(cand_path, map_path):
    cands, err = parse_candidates(cand_path)
    if err:
        return "B4", "FAIL", "无法取得候选集：%s" % err
    cmap, err = parse_claim_map(map_path)
    if err:
        return "B4", "FAIL", err
    cand_set, key_set = set(cands), set(cmap)
    if key_set != cand_set:
        return ("B4", "FAIL",
                "键集合不符：claim_map 独有 %s；候选独有 %s"
                % (_fmt_set(key_set - cand_set), _fmt_set(cand_set - key_set)))
    return "B4", "PASS", "claim_map %d 键；与候选 pk 集合一致" % len(cmap)


def check_b5(cand_path, map_path, db_path):
    cands, err = parse_candidates(cand_path)
    if err:
        return "B5", "FAIL", "无法取得候选集：%s" % err, False
    cmap, err = parse_claim_map(map_path)
    if err:
        return "B5", "FAIL", err, False

    ids = list(cmap.values())
    malformed = [cid for cid in ids if not PK_RE.fullmatch(cid)]
    if malformed:
        return ("B5", "FAIL", "claim_id 格式不符（应为 CL-RM-NNNNNN）：%s"
                % _fmt_set(malformed), False)

    db = pathlib.Path(db_path)
    if not db.exists():
        return "B5", "SKIP", "依赖缺失：库文件不存在 %s" % db, True
    try:
        import duckdb
    except ImportError as ex:
        return "B5", "SKIP", "依赖缺失：duckdb 模块不可用（%s）" % ex, True

    try:
        con = duckdb.connect(str(db), read_only=True)
    except Exception as ex:  # 库被写锁／路径不可达均属依赖不可用
        return "B5", "SKIP", "依赖缺失：库连接失败（%s）" % ex, True

    try:
        found = set()
        uniq = sorted(set(ids))
        for i in range(0, len(uniq), 400):
            chunk = uniq[i:i + 400]
            sql = "SELECT claim_id FROM claim WHERE claim_id IN (%s)" % (
                ",".join("?" * len(chunk)),)
            found.update(row[0] for row in con.execute(sql, chunk).fetchall())
    except Exception as ex:
        con.close()
        name = type(ex).__name__
        if "Catalog" in name:
            return "B5", "FAIL", "claim 表缺失或不可查询：%s" % ex, False
        return "B5", "SKIP", "依赖缺失：查询失败（%s）" % ex, True
    con.close()

    missing = set(uniq) - found
    if missing:
        return ("B5", "FAIL", "claim_id 库内不存在：%s" % _fmt_set(missing), False)

    nums = sorted(int(PK_RE.fullmatch(cid).group(1)) for cid in ids)
    if len(nums) != len(set(nums)):
        dup = sorted({x for x in nums if nums.count(x) > 1})
        return "B5", "FAIL", "claim_id 在本批重复：%s" % _fmt_set(dup, 8), False
    holes = sorted(set(range(nums[0], nums[-1] + 1)) - set(nums))
    if holes:
        return ("B5", "FAIL",
                "本批号段 %d–%d 有洞：%s" % (nums[0], nums[-1], _fmt_set(holes)), False)
    return ("B5", "PASS",
            "claim_id 库内命中 %d/%d；号段 %d–%d 连续（%d 号）"
            % (len(ids), len(ids), nums[0], nums[-1], len(nums)), False)


def check_b6(spec_path, cand_path, host_paths):
    cands, err = parse_candidates(cand_path)
    if err:
        return "B6", "FAIL", "无法取得候选集：%s" % err
    cand_set = set(cands)
    spec, spec_err = parse_spec(spec_path)
    want_lib = None if spec_err else (spec.get("lib") or None)

    matched = {}
    total_marks = 0
    for host in host_paths:
        p = pathlib.Path(host)
        if not p.exists():
            return "B6", "FAIL", "宿主不存在：%s" % p
        text = p.read_text(encoding="utf-8", errors="replace")
        for lib, pk in MARK_RE.findall(text):
            total_marks += 1
            if want_lib and lib != want_lib:
                continue
            if _norm_pk(pk) in cand_set:
                matched[_norm_pk(pk)] = matched.get(_norm_pk(pk), 0) + 1

    if sum(matched.values()) != len(cands):
        extra = {k for k, v in matched.items() if v > 1}
        return ("B6", "FAIL",
                "宿主内本批 ROW_MINE 块 %d ≠ 候选 %d 行（宿主标记共 %d；重复块 %s）"
                % (sum(matched.values()), len(cands), total_marks,
                   _fmt_set(extra) if extra else "无"))
    return ("B6", "PASS",
            "宿主内本批 ROW_MINE 块 %d = 候选 %d 行（宿主标记共 %d）"
            % (sum(matched.values()), len(cands), total_marks))


def run_checks(tag, spec_path, cand_path, narr_path, map_path, db_path, host_paths):
    """返回 (rows, dep_missing)；rows 为 (code, status, detail) 三元组。"""
    rows = []
    dep = False

    rows.append(check_b1(tag, spec_path))
    rows.append(check_b2(spec_path, cand_path))
    if narr_path:
        rows.append(check_b3(cand_path, narr_path))
    else:
        rows.append(("B3", "SKIP", "未提供 --narr"))
    if map_path:
        rows.append(check_b4(cand_path, map_path))
    else:
        rows.append(("B4", "SKIP", "未提供 --claim-map"))
    if db_path and map_path:
        code, status, detail, d = check_b5(cand_path, map_path, db_path)
        rows.append((code, status, detail))
        dep = dep or d
    elif db_path:
        rows.append(("B5", "FAIL", "提供 --db 但未提供 --claim-map"))
    else:
        rows.append(("B5", "SKIP", "未提供 --db"))
    if host_paths:
        rows.append(check_b6(spec_path, cand_path, host_paths))
    else:
        rows.append(("B6", "SKIP", "未提供 --outline-host"))
    return rows, dep


def _report(rows, tag):
    print("=" * 72)
    print("mail2d 批次收口门禁 · tag=%s" % tag)
    print("=" * 72)
    fails = 0
    for code, status, detail in rows:
        print("  [%s] %s %s" % (status, code, detail))
        if status == "FAIL":
            fails += 1
    print("-" * 72)
    print("  合计 %d 项：PASS %d／FAIL %d／SKIP %d"
          % (len(rows), sum(1 for r in rows if r[1] == "PASS"), fails,
             sum(1 for r in rows if r[1] == "SKIP")))
    return fails


# ── 判据非空自检 ──────────────────────────────────────────────────────────

POS_PKS = ["100", "101", "102", "103"]
POS_IDS = ["CL-RM-000101", "CL-RM-000102", "CL-RM-000103", "CL-RM-000104"]


def _write_fixture(root, with_db=False):
    root.mkdir(parents=True, exist_ok=True)
    spec = {
        "tag": "tst_b001",
        "lib": "testlib",
        "n": 4,
        "pk_range": [100, 103],
        "queued": True,
    }
    (root / "spec.json").write_text(
        json.dumps(spec, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (root / "cand.tsv").write_text(
        "".join("%s\tL4\t摘要%s\n" % (pk, pk) for pk in POS_PKS), encoding="utf-8")
    (root / "narr.tsv").write_text(
        "".join("%s\t881\t叙述%s\n" % (pk, pk) for pk in POS_PKS), encoding="utf-8")
    (root / "map.json").write_text(
        json.dumps(dict(zip(POS_PKS, POS_IDS)), ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8")
    (root / "host.md").write_text(
        "# 宿主\n\n" + "\n\n".join(
            "<!-- ROW_MINE: testlib.messages.%s -->\n**当事人自述**（证据等级：L4）\n\n正文%s"
            % (pk, pk) for pk in POS_PKS) + "\n", encoding="utf-8")
    if with_db:
        import duckdb
        db = root / "t.duckdb"
        if db.exists():
            db.unlink()
        con = duckdb.connect(str(db))
        con.execute("CREATE TABLE claim(claim_id VARCHAR)")
        con.executemany("INSERT INTO claim VALUES (?)", [(cid,) for cid in POS_IDS])
        con.close()
        return root / "spec.json", root / "cand.tsv", root / "narr.tsv", \
            root / "map.json", db, [root / "host.md"]
    return root / "spec.json", root / "cand.tsv", root / "narr.tsv", \
        root / "map.json", None, [root / "host.md"]


def _status_map(rows):
    return {code: status for code, status, _d in rows}


def cmd_selftest():
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="mail2d_gate_"))
    failures = []
    try:
        try:
            import duckdb  # noqa: F401
            has_db = True
        except ImportError:
            has_db = False

        base = tmp / "base"
        paths = _write_fixture(base, with_db=has_db)

        # 回读断言：夹具确实落盘且规模与预期一致（自检不得空转）
        spec_back = json.loads(paths[0].read_text(encoding="utf-8"))
        cand_back = [ln for ln in paths[1].read_text(encoding="utf-8").splitlines() if ln.strip()]
        narr_back = [ln for ln in paths[2].read_text(encoding="utf-8").splitlines() if ln.strip()]
        map_back = json.loads(paths[3].read_text(encoding="utf-8"))
        mark_back = MARK_RE.findall(paths[5][0].read_text(encoding="utf-8"))
        assert spec_back["n"] == 4 and spec_back["pk_range"] == [100, 103], "正样本 spec 回读不符"
        assert len(cand_back) == 4 and len(narr_back) == 4 and len(map_back) == 4, \
            "正样本行数回读不符"
        assert len(mark_back) == 4, "正样本宿主块数回读不符"

        rows, dep = run_checks("tst_b001", *paths)
        status = _status_map(rows)
        bad = [c for c, s in status.items() if s == "FAIL"]
        if bad:
            failures.append("正样本应 0 FAIL，实际 %s" % bad)
        if has_db:
            if status.get("B5") != "PASS":
                failures.append("正样本 B5 应 PASS，实际 %s" % status.get("B5"))
        elif status.get("B5") != "SKIP":
            failures.append("无 duckdb 时 B5 应 SKIP，实际 %s" % status.get("B5"))
        if status.get("B6") != "PASS":
            failures.append("正样本 B6 应 PASS，实际 %s" % status.get("B6"))
        if dep:
            failures.append("正样本不应报依赖缺失")

        cases = []

        def case_b1(d):
            (d / "spec.json").write_text(
                json.dumps({"tag": "tst_b001", "lib": "testlib", "n": 4,
                            "pk_range": []}, ensure_ascii=False) + "\n",
                encoding="utf-8")
            back = json.loads((d / "spec.json").read_text(encoding="utf-8"))
            assert back["pk_range"] == [], "B1 夹具回读不符"

        def case_b2(d):
            text = (d / "cand.tsv").read_text(encoding="utf-8").replace("103\t", "104\t")
            (d / "cand.tsv").write_text(text, encoding="utf-8")
            pks = [ln.split("\t")[0] for ln in text.splitlines() if ln.strip()]
            assert len(pks) == 4 and "104" in pks and "103" not in pks, "B2 夹具回读不符"

        def case_b3(d):
            lines = [ln for ln in (d / "narr.tsv").read_text(encoding="utf-8").splitlines()
                     if ln.strip()]
            (d / "narr.tsv").write_text("\n".join(lines[:-1]) + "\n", encoding="utf-8")
            back = [ln for ln in (d / "narr.tsv").read_text(encoding="utf-8").splitlines()
                    if ln.strip()]
            assert len(back) == 3, "B3 夹具回读不符"

        def case_b4(d):
            data = json.loads((d / "map.json").read_text(encoding="utf-8"))
            data.pop("103")
            (d / "map.json").write_text(
                json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
            back = json.loads((d / "map.json").read_text(encoding="utf-8"))
            assert len(back) == 3 and "103" not in back, "B4 夹具回读不符"

        def case_b6(d):
            text = (d / "host.md").read_text(encoding="utf-8")
            text = text.rsplit("\n\n<!-- ROW_MINE:", 1)[0] + "\n"
            (d / "host.md").write_text(text, encoding="utf-8")
            back = MARK_RE.findall((d / "host.md").read_text(encoding="utf-8"))
            assert len(back) == 3, "B6 夹具回读不符"

        cases = [("B1", case_b1), ("B2", case_b2), ("B3", case_b3),
                 ("B4", case_b4), ("B6", case_b6)]

        for code, mutate in cases:
            d = tmp / ("neg_" + code.lower())
            shutil.copytree(base, d)
            mutate(d)
            npaths = (d / "spec.json", d / "cand.tsv", d / "narr.tsv", d / "map.json",
                      (d / "t.duckdb") if has_db else None, [d / "host.md"])
            nrows, ndep = run_checks("tst_b001", *npaths)
            nstatus = _status_map(nrows)
            if nstatus.get(code) != "FAIL":
                failures.append("%s 负向夹具未命中（实际 %s）" % (code, nstatus.get(code)))
            fails = sum(1 for _c, s, _d in nrows if s == "FAIL")
            rc = 2 if ndep else (1 if fails else 0)
            if rc != 1:
                failures.append("%s 负向夹具退出码应为 1，实际 %d" % (code, rc))
            if code != "B1" and nstatus.get("B1") != "PASS":
                failures.append("%s 负向夹具不应连带 B1（实际 %s）"
                                % (code, nstatus.get("B1")))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    if failures:
        print("  ❌ 判据非空自检失败：")
        for item in failures:
            print("     - %s" % item)
        return 1
    print("  ✅ 判据非空自检通过：正样本全 PASS；B1／B2／B3／B4／B6 五类负向夹具均命中且退出码 1")
    return 0


def main():
    ap = argparse.ArgumentParser(description="mail2d 批次收口门禁（第三十一件）")
    ap.add_argument("--tag", metavar="TAG", help="批次标签，如 fhk_b085")
    ap.add_argument("--spec", metavar="JSON", help="_batch_<tag>.json")
    ap.add_argument("--candidates", metavar="FILE", help="候选表（TSV／JSONL）")
    ap.add_argument("--narr", metavar="FILE", help="mount_narr.tsv")
    ap.add_argument("--claim-map", metavar="JSON", dest="claim_map",
                    help="<tag>_claim_map.json")
    ap.add_argument("--db", metavar="DUCKDB", help="historical_claims.duckdb（可选）")
    ap.add_argument("--outline-host", metavar="MD", action="append", dest="outline_hosts",
                    help="宿主 .md（可选，可重复）")
    ap.add_argument("--selftest", action="store_true", help="判据非空自检")
    args = ap.parse_args()

    if args.selftest:
        return cmd_selftest()
    if not args.tag or not args.spec or not args.candidates:
        ap.error("需要 --tag／--spec／--candidates（或使用 --selftest）")

    rows, dep = run_checks(args.tag, args.spec, args.candidates, args.narr,
                           args.claim_map, args.db, args.outline_hosts)
    fails = _report(rows, args.tag)
    if dep:
        print("  依赖缺失：退出码 2")
        return 2
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
