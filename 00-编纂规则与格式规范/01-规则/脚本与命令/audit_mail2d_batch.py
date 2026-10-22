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
- 库／宿主：`historical_claims.duckdb`、源消息库与 `05-卷册大纲/` 宿主 `.md`

判据（逐条独立打印；任一 FAIL 退出码 1）
----
B1 spec 存在，`pk_range` 非空且 `lo <= hi`，`n` 与区间跨度自洽
   （`n <= 跨度`；若 spec 声明 `pk_missing_count`，则 `n + 缺号数 == 跨度`）
   `--sampled` 时改按抽样口径：未取行不再计为缺号，须由 spec 声明
   `pk_missing_count`，以“有效窗口行数＝跨度−缺号”与候选数比较，并报未取行数
B2 候选 pk 唯一、全在 `pk_range` 内，且候选数 `<= n`（判读后子集允许少于 n）；
   给 `--srcdb` 时逐 pk 回查源库 `messages`：行须存在且正文字段非空，幽灵 pk
   或空正文 pk 均 FAIL；正文字段按 `body`／`text`／`content` 顺序探测，探测不到
   即 FAIL；抽样行若 `length(正文)==65535` 另加一行 WARN（疑字段截断，不判 FAIL）；
   未给 `--srcdb` 时本项标注 SKIP（源库存在性未核，不得视为 PASS）
B3 `--narr` 行数等于候选行数，pk 集合等于候选 pk 集合；
   另按 H 线口径校验叙述语义：每行叙述 60–140 字且句末不带标点
   （`--narr-min`／`--narr-max` 可调；`--no-narr-semantics` 可关闭）
B4 `--claim-map` 键集合等于候选 pk 集合
B5 `--db`：claim_map 的 claim_id 全部在库内存在；本批 min–max 号段连续无洞
   （跨线共享号段只按本批 min/max 检查，不要求全局连续）
B6 `--outline-host`：宿主内本批候选 pk 的 `ROW_MINE` 块数等于候选行数
   （按 `ROW_MINE:` 标记字符串计数，不解析块体全文；可重复给出多个宿主，按合计判）
B7 `--reject-synthetic`：候选表／叙述表／claim_map 内容含 `pilot-synthetic`
   或文件名含 `pilot` 即 FAIL（默认关闭；生产收口建议开启）

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
        --srcdb 04-现代研究文献/messages.duckdb \\
        --outline-host 05-卷册大纲/第05卷-.../097.1-....md
    python audit_mail2d_batch.py --tag fbug_pilot100 --spec ... --candidates ... \
        --sampled          # 跨年分层抽样：未取行不计缺号
    python audit_mail2d_batch.py --selftest

依赖：仅标准库；`--db`／`--srcdb` 时另需 `duckdb`。
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
SYNTH_MARK = "pilot-synthetic"
# 叙述句末不得出现的标点（对齐 `_vn_narr.py` 的 TAIL 集：，；：。！？ 与空格）
NARR_TAIL = {chr(0xFF0C), chr(0xFF1B), chr(0xFF1A), chr(0x3002),
             chr(0xFF01), chr(0xFF1F), " "}


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
    """返回 ([(pk, 叙述文本)], 错误文本)。mount_narr 为 TAB 三列。"""
    p = pathlib.Path(path)
    if not p.exists():
        return None, "叙述总表不存在：%s" % p
    out = []
    for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        pk = _norm_pk(parts[0])
        text = parts[2] if len(parts) >= 3 else ""
        out.append((pk, text))
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


def check_b1(tag, spec_path, cand_path=None, sampled=False):
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
    if missing is not None:
        try:
            missing = int(missing)
        except (TypeError, ValueError):
            return "B1", "FAIL", "pk_missing_count 非整数：%r" % (spec.get("pk_missing_count"),)

    if sampled:
        # 抽样口径：pk_range 为抽样窗口，区间内未取行不等于缺号；
        # 缺号须由 spec 显式声明，有效窗口行数 = 跨度 − 缺号，与实取候选数比较。
        if missing is None:
            return ("B1", "FAIL",
                    "sampled 模式要求 spec 提供 pk_missing_count（跨度 %d）" % span)
        if missing < 0:
            return "B1", "FAIL", "pk_missing_count 为负：%d" % missing
        valid = span - missing
        if valid < 0:
            return ("B1", "FAIL",
                    "跨度(%d) − 缺号(%d) 为负，spec 不可用" % (span, missing))
        if not cand_path:
            return "B1", "FAIL", "sampled 模式需提供 --candidates 以计未取行数"
        cands, cerr = parse_candidates(cand_path)
        if cerr:
            return "B1", "FAIL", "无法取得候选集：%s" % cerr
        taken = len(cands)
        if taken > valid:
            return ("B1", "FAIL",
                    "实取 %d 行 > 有效窗口行数 %d（跨度 %d − 缺号 %d）"
                    % (taken, valid, span, missing))
        detail = ("sampled 模式；pk_range %d–%d（跨度 %d）；缺号 %d；"
                  "有效窗口行数 = 跨度 − 缺号 = %d；实取 %d；未取行数 = %d"
                  % (lo, hi, span, missing, valid, taken, valid - taken))
        if spec.get("tag") and spec.get("tag") != tag:
            detail += "；⚠ spec tag=%s 与 --tag=%s 不同（仅提示）" % (spec.get("tag"), tag)
        return "B1", "PASS", detail

    if n > span:
        return "B1", "FAIL", "n=%d 大于区间跨度 %d（pk_range %d–%d）" % (n, span, lo, hi)
    if missing is not None:
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


def check_b2(spec_path, cand_path, srcdb_path=None):
    """返回 (rows, dep)；rows 为 (code, status, detail) 列表。

    不给 --srcdb 时标注 SKIP（非 PASS）。给 --srcdb 时逐 pk 回查源库 messages：
    行须存在且正文字段非空（字段按 body／text／content 顺序探测），幽灵 pk 与
    空正文 pk 均 FAIL；抽样行 length(正文)==65535 另加一行 WARN（疑字段截断）。
    """
    cands, err = parse_candidates(cand_path)
    if err:
        return [("B2", "FAIL", err)], False
    spec, spec_err = parse_spec(spec_path)
    if spec_err:
        return [("B2", "FAIL", "无法取得 pk_range：%s" % spec_err)], False
    lo, hi, rng_err = parse_range(spec)
    if rng_err:
        return [("B2", "FAIL", "无法取得 pk_range：%s" % rng_err)], False
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
        return [("B2", "FAIL", "；".join(bad))], False

    static = "候选 %d 行；pk 唯一、全在 %d–%d 内、候选数 ≤ n" % (len(cands), lo, hi)
    if n is not None and len(cands) < n:
        static += "（判读后子集：%d < %d）" % (len(cands), n)

    # 源库存在性：未给 --srcdb 时不得冒充 PASS（幽灵 pk 曾全绿放行）
    if not srcdb_path:
        return [("B2", "SKIP",
                 "%s；未提供 --srcdb，源库存在性未核（SKIP，不得视为 PASS）" % static)], False
    db = pathlib.Path(srcdb_path)
    if not db.exists():
        return [("B2", "SKIP", "依赖缺失：源库文件不存在 %s" % db)], True
    try:
        import duckdb
    except ImportError as ex:
        return [("B2", "SKIP", "依赖缺失：duckdb 模块不可用（%s）" % ex)], True
    try:
        con = duckdb.connect(str(db), read_only=True)
    except Exception as ex:  # 库被写锁／路径不可达均属依赖不可用
        return [("B2", "SKIP", "依赖缺失：源库连接失败（%s）" % ex)], True

    # 探测正文字段名（优先 body，其次 text／content）
    try:
        cols = [c[0] for c in con.execute("SELECT * FROM messages LIMIT 0").description]
    except Exception as ex:
        con.close()
        name = type(ex).__name__
        text = str(ex)
        if "Catalog" in name or "Binder" in name or "messages" in text:
            return [("B2", "FAIL", "源库 messages 表缺失或不可查询：%s" % text)], False
        return [("B2", "SKIP", "依赖缺失：源库查询失败（%s）" % text)], True
    body_col = next((c for c in ("body", "text", "content") if c in cols), None)
    if body_col is None:
        con.close()
        return ([("B2", "FAIL",
                  "源库 messages 表探测不到正文字段（候选列 body／text／content，实有：%s）"
                  % _fmt_set(cols, 12))], False)

    ghost, empty, trunc = [], [], []
    try:
        for pk in sorted(set(cands)):
            row = con.execute(
                "SELECT length(%s) FROM messages WHERE id=? LIMIT 1" % body_col,
                [int(pk)]).fetchone()
            if row is None:
                ghost.append(pk)
                continue
            ln = row[0]
            if ln is None or int(ln) == 0:
                empty.append(pk)
            elif int(ln) == 65535:
                trunc.append(pk)
    except Exception as ex:
        con.close()
        name = type(ex).__name__
        text = str(ex)
        if "Catalog" in name or "Binder" in name or "messages" in text:
            return [("B2", "FAIL", "源库 messages 表缺失或不可查询：%s" % text)], False
        return [("B2", "SKIP", "依赖缺失：源库查询失败（%s）" % text)], True
    con.close()

    rows = []
    if ghost:
        rows.append(("B2", "FAIL",
                     "幽灵 pk（源库 messages 表无该行）：%s" % _fmt_set(ghost, 20)))
    if empty:
        rows.append(("B2", "FAIL",
                     "空正文 pk（行存在但字段 %s 为空，共 %d 个）：%s"
                     % (body_col, len(empty), _fmt_set(empty, 20))))
    if rows:
        return rows, False
    rows.append(("B2", "PASS",
                 "%s；源库 messages 逐 pk 命中 %d 个且字段 %s 正文非空"
                 % (static, len(set(cands)), body_col)))
    if trunc:
        rows.append(("B2", "WARN",
                     "抽样行中 %d 行 length(%s)==65535：疑源库字段截断（仅告警，不判 FAIL）：%s"
                     % (len(trunc), body_col, _fmt_set(trunc, 20))))
    return rows, False


def check_b3(cand_path, narr_path, narr_min=60, narr_max=140, semantics=True):
    cands, err = parse_candidates(cand_path)
    if err:
        return "B3", "FAIL", "无法取得候选集：%s" % err
    nrows, err = parse_narr(narr_path)
    if err:
        return "B3", "FAIL", err
    narr = [pk for pk, _t in nrows]
    cand_set, narr_set = set(cands), set(narr)
    bad = []
    if len(narr) != len(cands):
        bad.append("narr %d 行 ≠ 候选 %d 行" % (len(narr), len(cands)))
    if narr_set != cand_set:
        only_c = cand_set - narr_set
        only_n = narr_set - cand_set
        bad.append("pk 集合不符：候选独有 %s；narr 独有 %s"
                   % (_fmt_set(only_c), _fmt_set(only_n)))
    if semantics:
        short, over, tail = [], [], []
        for pk, text in nrows:
            ln = len(text)
            if ln < narr_min:
                short.append("%s(%d)" % (pk, ln))
            elif ln > narr_max:
                over.append("%s(%d)" % (pk, ln))
            if text and text[-1] in NARR_TAIL:
                tail.append("%s(%r)" % (pk, text[-1]))
        if short:
            bad.append("叙述过短 < %d：%s" % (narr_min, _fmt_set(short)))
        if over:
            bad.append("叙述过长 > %d：%s" % (narr_max, _fmt_set(over)))
        if tail:
            bad.append("叙述句末带标点（H 线口径：句末不加标点）：%s" % _fmt_set(tail))
    if bad:
        return "B3", "FAIL", "；".join(bad)
    detail = "narr %d 行；pk 集合与候选一致" % len(narr)
    if semantics:
        detail += "；长度 %d–%d 合规、句末无标点" % (narr_min, narr_max)
    return "B3", "PASS", detail


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


def check_b7_synthetic(cand_path, narr_path, map_path):
    """候选／narr／claim_map 内容含 pilot-synthetic 或文件名含 pilot 即 FAIL。"""
    bad = []
    for label, path in (("候选表", cand_path), ("叙述表", narr_path),
                        ("claim_map", map_path)):
        if not path:
            continue
        p = pathlib.Path(path)
        if "pilot" in p.name.lower():
            bad.append("%s 文件名含 pilot：%s" % (label, p.name))
        if p.exists():
            text = p.read_text(encoding="utf-8", errors="replace")
            if SYNTH_MARK in text:
                bad.append("%s 内容含 %s" % (label, SYNTH_MARK))
    if bad:
        return "B7", "FAIL", "；".join(bad)
    return "B7", "PASS", "候选／叙述／claim_map 无 pilot 文件名或 pilot-synthetic 标记"


def run_checks(tag, spec_path, cand_path, narr_path, map_path, db_path, host_paths,
               srcdb_path=None, narr_min=60, narr_max=140, narr_semantics=True,
               reject_synthetic=False, sampled=False):
    """返回 (rows, dep_missing)；rows 为 (code, status, detail) 三元组。"""
    rows = []
    dep = False

    rows.append(check_b1(tag, spec_path, cand_path, sampled))
    b2_rows, d = check_b2(spec_path, cand_path, srcdb_path)
    rows.extend(b2_rows)
    dep = dep or d
    if narr_path:
        rows.append(check_b3(cand_path, narr_path, narr_min, narr_max, narr_semantics))
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
    if reject_synthetic:
        rows.append(check_b7_synthetic(cand_path, narr_path, map_path))
    else:
        rows.append(("B7", "PASS", "未启用 --reject-synthetic，跳过（默认关闭）"))
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
    warns = sum(1 for r in rows if r[1] == "WARN")
    line = ("  合计 %d 项：PASS %d／FAIL %d／SKIP %d"
            % (len(rows), sum(1 for r in rows if r[1] == "PASS"), fails,
               sum(1 for r in rows if r[1] == "SKIP")))
    if warns:
        line += "／WARN %d" % warns
    print(line)
    return fails


# ── 判据非空自检 ──────────────────────────────────────────────────────────

POS_PKS = ["100", "101", "102", "103"]
POS_IDS = ["CL-RM-000101", "CL-RM-000102", "CL-RM-000103", "CL-RM-000104"]


def _narr_text(pk):
    """合成叙述：长度固定 80 字、句末不带标点（贴合 `_vn_narr.py` 口径）。"""
    head = "合成叙述占位（%s）：用于校验批次收口门禁的 pk 对账与叙述长度尾标点判据" % pk
    text = (head + "述" * 90)[:80]
    assert len(text) == 80 and text[-1] not in NARR_TAIL, "合成叙述违反夹具前提"
    return text


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
        "".join("%s\t881\t%s\n" % (pk, _narr_text(pk)) for pk in POS_PKS),
        encoding="utf-8")
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
        con.execute("CREATE TABLE messages(id BIGINT, body VARCHAR)")
        con.executemany("INSERT INTO messages VALUES (?, ?)",
                        [(int(pk), "正文占位%s" % pk) for pk in POS_PKS])
        con.close()
        return root / "spec.json", root / "cand.tsv", root / "narr.tsv", \
            root / "map.json", db, [root / "host.md"]
    return root / "spec.json", root / "cand.tsv", root / "narr.tsv", \
        root / "map.json", None, [root / "host.md"]


def _status_map(rows):
    """按判据码取状态；WARN 为附加提示行，不覆盖同名判据的 PASS／FAIL／SKIP。"""
    return {code: status for code, status, _d in rows if status != "WARN"}


def _readback_positive(paths):
    """回读断言：夹具确实落盘、规模与叙述语义前提一致（自检不得空转）。"""
    spec_back = json.loads(paths[0].read_text(encoding="utf-8"))
    cand_back = [ln for ln in paths[1].read_text(encoding="utf-8").splitlines() if ln.strip()]
    narr_lines = [ln for ln in paths[2].read_text(encoding="utf-8").splitlines() if ln.strip()]
    map_back = json.loads(paths[3].read_text(encoding="utf-8"))
    mark_back = MARK_RE.findall(paths[5][0].read_text(encoding="utf-8"))
    assert spec_back["n"] == 4 and spec_back["pk_range"] == [100, 103], "正样本 spec 回读不符"
    assert len(cand_back) == 4 and len(narr_lines) == 4 and len(map_back) == 4, \
        "正样本行数回读不符"
    assert len(mark_back) == 4, "正样本宿主块数回读不符"
    for ln in narr_lines:
        text = ln.split("\t")[2]
        assert 60 <= len(text) <= 140, "正样本叙述长度越界：%d" % len(text)
        assert text[-1] not in NARR_TAIL, "正样本叙述句末带标点"


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
        _readback_positive(paths)

        # 正样本（给 --srcdb：B2 应 PASS 而非 SKIP）
        rows, dep = run_checks("tst_b001", *paths, srcdb_path=paths[4])
        status = _status_map(rows)
        bad = [c for c, s in status.items() if s == "FAIL"]
        if bad:
            failures.append("正样本应 0 FAIL，实际 %s" % bad)
        if has_db:
            if status.get("B2") != "PASS":
                failures.append("有 srcdb 时正样本 B2 应 PASS，实际 %s" % status.get("B2"))
            if status.get("B5") != "PASS":
                failures.append("正样本 B5 应 PASS，实际 %s" % status.get("B5"))
        else:
            if status.get("B2") != "SKIP":
                failures.append("无 duckdb 时正样本 B2 应 SKIP，实际 %s" % status.get("B2"))
            if status.get("B5") != "SKIP":
                failures.append("无 duckdb 时正样本 B5 应 SKIP，实际 %s" % status.get("B5"))
        if status.get("B3") != "PASS":
            failures.append("正样本 B3 应 PASS，实际 %s" % status.get("B3"))
        if status.get("B6") != "PASS":
            failures.append("正样本 B6 应 PASS，实际 %s" % status.get("B6"))
        if dep:
            failures.append("正样本不应报依赖缺失")

        # 无 --srcdb：B2 须 SKIP（不得冒充 PASS）
        rows_no, _d = run_checks("tst_b001", *paths, srcdb_path=None)
        if _status_map(rows_no).get("B2") != "SKIP":
            failures.append("无 --srcdb 时 B2 应 SKIP，实际 %s"
                            % _status_map(rows_no).get("B2"))

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

        def case_b2_ghost(d):
            import duckdb
            con = duckdb.connect(str(d / "t.duckdb"))
            con.execute("DELETE FROM messages WHERE id=103")
            left = [r[0] for r in con.execute("SELECT id FROM messages ORDER BY id").fetchall()]
            con.close()
            assert left == [100, 101, 102], "幽灵 pk 夹具回读不符：%s" % left

        def case_b2_emptybody(d):
            import duckdb
            con = duckdb.connect(str(d / "t.duckdb"))
            con.execute("UPDATE messages SET body='' WHERE id=103")
            body = con.execute("SELECT body FROM messages WHERE id=103").fetchone()[0]
            con.close()
            assert body == "", "空正文夹具回读不符：%r" % body

        def case_b3(d):
            lines = [ln for ln in (d / "narr.tsv").read_text(encoding="utf-8").splitlines()
                     if ln.strip()]
            (d / "narr.tsv").write_text("\n".join(lines[:-1]) + "\n", encoding="utf-8")
            back = [ln for ln in (d / "narr.tsv").read_text(encoding="utf-8").splitlines()
                    if ln.strip()]
            assert len(back) == 3, "B3 夹具回读不符"

        def case_b3_short(d):
            lines = (d / "narr.tsv").read_text(encoding="utf-8").splitlines()
            parts = lines[0].split("\t")
            lines[0] = "%s\t%s\t短句" % (parts[0], parts[1])
            (d / "narr.tsv").write_text("\n".join(lines) + "\n", encoding="utf-8")
            text = lines[0].split("\t")[2]
            assert len(text) < 60, "narr 过短夹具回读不符"

        def case_b3_tail(d):
            lines = (d / "narr.tsv").read_text(encoding="utf-8").splitlines()
            parts = lines[0].split("\t")
            long_tail = ("尾标点探针" + "述" * 90)[:80] + "。"
            lines[0] = "%s\t%s\t%s" % (parts[0], parts[1], long_tail)
            (d / "narr.tsv").write_text("\n".join(lines) + "\n", encoding="utf-8")
            text = lines[0].split("\t")[2]
            assert text[-1] in NARR_TAIL and len(text) >= 60, "尾标点夹具回读不符"

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

        def case_b7(d):
            text = (d / "cand.tsv").read_text(encoding="utf-8").replace(
                "摘要100", "%s 摘要" % SYNTH_MARK)
            (d / "cand.tsv").write_text(text, encoding="utf-8")
            assert SYNTH_MARK in (d / "cand.tsv").read_text(encoding="utf-8"), \
                "synthetic 夹具回读不符"

        # (判据码, 变异, 是否需 --srcdb, 是否启用 --reject-synthetic)
        cases = [
            ("B1", case_b1, False, False),
            ("B2", case_b2, True, False),
            ("B3", case_b3, False, False),
            ("B3", case_b3_short, False, False),
            ("B3", case_b3_tail, False, False),
            ("B4", case_b4, False, False),
            ("B6", case_b6, False, False),
            ("B7", case_b7, False, True),
        ]
        if has_db:
            cases.append(("B2", case_b2_ghost, True, False))
            cases.append(("B2", case_b2_emptybody, True, False))
        else:
            print("· 跳过幽灵 pk 夹具（无 duckdb 模块）")
            print("· 跳过空正文 pk 夹具（无 duckdb 模块）")

        for idx, (code, mutate, need_src, rej) in enumerate(cases, 1):
            d = tmp / ("neg_%02d_%s" % (idx, code.lower()))
            shutil.copytree(base, d)
            mutate(d)
            npaths = (d / "spec.json", d / "cand.tsv", d / "narr.tsv", d / "map.json",
                      (d / "t.duckdb") if has_db else None, [d / "host.md"])
            src = npaths[4] if (need_src and has_db) else None
            nrows, ndep = run_checks("tst_b001", *npaths, srcdb_path=src,
                                     reject_synthetic=rej)
            nstatus = _status_map(nrows)
            if nstatus.get(code) != "FAIL":
                failures.append("%s 负向夹具（%s）未命中（实际 %s）"
                                % (code, mutate.__name__, nstatus.get(code)))
            fails = sum(1 for _c, s, _d in nrows if s == "FAIL")
            rc = 2 if ndep else (1 if fails else 0)
            if rc != 1:
                failures.append("%s 负向夹具（%s）退出码应为 1，实际 %d"
                                % (code, mutate.__name__, rc))
            if code != "B1" and nstatus.get("B1") != "PASS":
                failures.append("%s 负向夹具不应连带 B1（实际 %s）"
                                % (code, nstatus.get("B1")))

        # 空正文夹具须点名空正文 pk（不得与幽灵 pk 混为一谈）
        if has_db:
            d = tmp / "neg_emptybody_detail"
            shutil.copytree(base, d)
            case_b2_emptybody(d)
            erows, _ed = run_checks(
                "tst_b001", d / "spec.json", d / "cand.tsv", d / "narr.tsv",
                d / "map.json", None, [d / "host.md"], srcdb_path=d / "t.duckdb")
            edetail = "；".join(x for c, s, x in erows if c == "B2" and s == "FAIL")
            if "空正文" not in edetail or "103" not in edetail:
                failures.append("空正文夹具未点名空正文 pk 103：%s" % (edetail or "无 FAIL"))

        # --sampled：宽窗口（跨年分层抽样）不得把未取行误报为缺号
        def _wide_spec(d, missing):
            data = {"tag": "tst_b001", "lib": "testlib", "n": 4,
                    "pk_range": [100, 10099]}
            if missing is not None:
                data["pk_missing_count"] = missing
            (d / "spec.json").write_text(
                json.dumps(data, ensure_ascii=False) + "\n", encoding="utf-8")
            back = json.loads((d / "spec.json").read_text(encoding="utf-8"))
            assert back["pk_range"] == [100, 10099], "宽窗口夹具回读不符"
            assert back.get("pk_missing_count") == missing, "宽窗口缺号回读不符"

        wide = tmp / "sampled_wide"
        shutil.copytree(base, wide)
        _wide_spec(wide, 2)  # 跨度 10000，真实缺号仅 2；未取行 9994 不是缺号
        wpaths = (wide / "spec.json", wide / "cand.tsv", wide / "narr.tsv",
                  wide / "map.json", None, [wide / "host.md"])
        wrows, _wd = run_checks("tst_b001", *wpaths, srcdb_path=None, sampled=True)
        wstatus = _status_map(wrows)
        wdetail = next(x for c, _s, x in wrows if c == "B1")
        if wstatus.get("B1") != "PASS":
            failures.append("--sampled 宽窗口 B1 应 PASS（不误报缺号），实际 %s：%s"
                            % (wstatus.get("B1"), wdetail))
        if "未取行数 = 9994" not in wdetail or "有效窗口行数" not in wdetail:
            failures.append("--sampled 未按有效窗口口径报数：%s" % wdetail)
        prow, _pd = run_checks("tst_b001", *wpaths, srcdb_path=None)
        if _status_map(prow).get("B1") != "FAIL":
            failures.append("关 --sampled 时宽窗口应按旧口径判 FAIL（缺号被混入未取行）")

        wide2 = tmp / "sampled_wide_nomissing"
        shutil.copytree(base, wide2)
        _wide_spec(wide2, None)
        r2, _d2 = run_checks(
            "tst_b001", wide2 / "spec.json", wide2 / "cand.tsv", wide2 / "narr.tsv",
            wide2 / "map.json", None, [wide2 / "host.md"], srcdb_path=None, sampled=True)
        if _status_map(r2).get("B1") != "FAIL":
            failures.append("--sampled 缺 pk_missing_count 时应 FAIL，实际 %s"
                            % _status_map(r2).get("B1"))

        wide3 = tmp / "sampled_over_taken"
        shutil.copytree(base, wide3)
        _wide_spec(wide3, 9997)  # 有效窗口 3 行 < 实取 4 行
        r3, _d3 = run_checks(
            "tst_b001", wide3 / "spec.json", wide3 / "cand.tsv", wide3 / "narr.tsv",
            wide3 / "map.json", None, [wide3 / "host.md"], srcdb_path=None, sampled=True)
        if _status_map(r3).get("B1") != "FAIL":
            failures.append("--sampled 实取 > 有效窗口时应 FAIL，实际 %s"
                            % _status_map(r3).get("B1"))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    if failures:
        print("  ❌ 判据非空自检失败：")
        for item in failures:
            print("     - %s" % item)
        return 1
    print("  ✅ 判据非空自检通过：正样本全 PASS；" + (
        "B1／B2／B2幽灵 pk／B2空正文 pk／B3／B3过短／B3尾标点／B4／B6／B7 负向夹具"
        "与 --sampled 宽窗口口径均命中且退出码 1"
        if has_db else
        "B1／B2／B3／B3过短／B3尾标点／B4／B6／B7 负向夹具与 --sampled 宽窗口口径"
        "均命中且退出码 1（无 duckdb，幽灵 pk／空正文 pk／B2 存在性未核）"))
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
    ap.add_argument("--srcdb", metavar="DUCKDB",
                    help="源消息库：B2 逐 pk 回查 messages 存在性与正文非空（可选）")
    ap.add_argument("--sampled", action="store_true",
                    help="抽样口径：B1 未取行不计缺号，按 spec 的 pk_missing_count 算有效窗口")
    ap.add_argument("--narr-min", type=int, default=60, dest="narr_min",
                    help="叙述长度下限（默认 60，H 线口径）")
    ap.add_argument("--narr-max", type=int, default=140, dest="narr_max",
                    help="叙述长度上限（默认 140，H 线口径）")
    ap.add_argument("--no-narr-semantics", action="store_true", dest="no_narr_semantics",
                    help="关闭叙述长度与尾标点判据")
    ap.add_argument("--reject-synthetic", action="store_true", dest="reject_synthetic",
                    help="候选／narr／claim_map 含 pilot-synthetic 或文件名含 pilot 即 FAIL")
    ap.add_argument("--outline-host", metavar="MD", action="append", dest="outline_hosts",
                    help="宿主 .md（可选，可重复）")
    ap.add_argument("--selftest", action="store_true", help="判据非空自检")
    args = ap.parse_args()

    if args.selftest:
        return cmd_selftest()
    if not args.tag or not args.spec or not args.candidates:
        ap.error("需要 --tag／--spec／--candidates（或使用 --selftest）")

    rows, dep = run_checks(
        args.tag, args.spec, args.candidates, args.narr, args.claim_map, args.db,
        args.outline_hosts, srcdb_path=args.srcdb, narr_min=args.narr_min,
        narr_max=args.narr_max, narr_semantics=not args.no_narr_semantics,
        reject_synthetic=args.reject_synthetic, sampled=args.sampled)
    fails = _report(rows, args.tag)
    if dep:
        print("  依赖缺失：退出码 2")
        return 2
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
