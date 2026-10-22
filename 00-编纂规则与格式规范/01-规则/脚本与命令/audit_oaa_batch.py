#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""audit_oaa_batch.py —— 第三十件门禁：OAA 批次收口对账（P3）。

对象
----
OAA（大纲邮件素材审计）F1–F4 任一批收口前的三面对账：分片目录 `shards/`、
判读目录 `judgements/`、可选台账 `processed_fN.jsonl`。

判据
----
S1 分片目录与判读目录均存在；给 `--batch` 时批次内两侧均不得为空
S2 每个分片有同名判读件——按文件名 stem 严格匹配，不做模糊猜测
S3 每个分片**都**有同名判读件，且判读件非空行数＝分片非空行数
   （分片按扩展名读 JSONL 或 TSV；TSV 首行为表头，不计入行数）
S4 判读件 key 集合＝分片 key 集合。key 字段须显式或唯一：
   给 `--key-field` 时按指定字段（须为双方全体共有）；
   未给时仅当双方只有一个共同候选（`pk`／`id`／`key`）才自动采用，
   多候选即 FAIL 并列候选，不得静默按 `pk→id→key` 切换；
   零候选时退到双方共同首列
S5 每个分片**都**有同名判读件，且判读 JSON 全合法、同一判读件内无重复 key
S6 若给 `--ledger`：台账 key 总量 ≥ 判读 key 总量，且台账内无重复 key；
   key 字段未定时无法比对，判 FAIL（不空转 PASS）
S7 若给 `--reject-synthetic`：分片／判读文件名含 `pilot`，或判读行含
   `pilot-synthetic`，即 FAIL（默认关闭，生产收口建议开启）

S3–S5 的作用面＝与分片配对的判读件 ＋ 缺配对的那些分片本身，不含判读目录内
其他批次的存量件。`--batch TAG` 按“文件名含 TAG”同时过滤分片与判读件，
批外件不进入 S1–S7 的任一计数。

用法
----
    python audit_oaa_batch.py --shards DIR --judgements DIR [--ledger FILE]
        [--batch TAG] [--key-field pk|id|key] [--reject-synthetic]
    python audit_oaa_batch.py --selftest

退出码：0 全 PASS／1 任一 FAIL／2 依赖缺失（目录不存在，或未给必需参数）

依赖：仅标准库。只读，不写任何受审文件。
"""
import argparse
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

sys.stdout.reconfigure(encoding="utf-8")

EXTS = {".jsonl", ".json", ".tsv"}
KEY_PRIORITY = ("pk", "id", "key")
SYNTH_MARK = "pilot-synthetic"


def _data_files(directory: pathlib.Path):
    if not directory.is_dir():
        return []
    return sorted(p for p in directory.iterdir()
                  if p.is_file() and p.suffix.lower() in EXTS
                  and not p.name.startswith("."))


def _match_tag(path: pathlib.Path, tag: str):
    """批次过滤：文件名含 TAG（tag 为空则不过滤）。"""
    return tag is None or tag in path.name


def _read_jsonl(path: pathlib.Path):
    """返回 (records, 非空行数, [(行号, 错因)])。"""
    try:
        raw = path.read_text(encoding="utf-8", errors="strict")
    except (OSError, UnicodeDecodeError) as ex:
        return [], 0, [(0, "读取失败：%s" % ex)]
    lines = [ln for ln in raw.splitlines() if ln.strip()]
    records, errors = [], []
    for i, line in enumerate(lines, 1):
        try:
            obj = json.loads(line)
        except ValueError as ex:
            errors.append((i, "JSON 非法：%s" % ex))
            continue
        if not isinstance(obj, dict):
            errors.append((i, "非 JSON 对象：%s" % type(obj).__name__))
            continue
        records.append(obj)
    return records, len(lines), errors


def _read_shard(path: pathlib.Path):
    """按扩展名读分片，返回 (records, 数据行数, 错因或 None)。"""
    if path.suffix.lower() == ".tsv":
        try:
            raw = path.read_text(encoding="utf-8", errors="strict")
        except (OSError, UnicodeDecodeError) as ex:
            return [], 0, "读取失败：%s" % ex
        lines = [ln for ln in raw.splitlines() if ln.strip()]
        if not lines:
            return [], 0, None
        header = [c.strip() for c in lines[0].split("\t")]
        records = [dict(zip(header, ln.split("\t"))) for ln in lines[1:]]
        return records, len(lines) - 1, None
    records, n_lines, errors = _read_jsonl(path)
    return records, n_lines, errors[0][1] if errors else None


def _committed_fields(records):
    """所有记录共有的字段（保持首条记录的出现顺序）。"""
    if not records:
        return []
    return [f for f in records[0] if all(f in r for r in records)]


def _first_field(records):
    if not records:
        return None
    return next(iter(records[0]))


def _resolve_key_field(a_records, b_records, explicit=None):
    """返回 (字段名, 说明)。字段未定返回 (None, 原因)。"""
    a_fields = _committed_fields(a_records)
    b_fields = _committed_fields(b_records)
    if explicit:
        lack = []
        if explicit not in a_fields:
            lack.append("分片")
        if explicit not in b_fields:
            lack.append("判读")
        if lack:
            return None, ("显式 key 字段“%s”在%s侧非全体共有（分片候选 %s；判读候选 %s）"
                          % (explicit, "、".join(lack),
                             "、".join(a_fields) or "无", "、".join(b_fields) or "无"))
        return explicit, "显式指定“%s”" % explicit
    common = [c for c in KEY_PRIORITY if c in a_fields and c in b_fields]
    if len(common) > 1:
        return None, ("key 字段歧义：双方共有多个候选 %s，须以 --key-field 显式指定"
                      "（分片候选 %s；判读候选 %s）"
                      % ("、".join(common), "、".join(a_fields) or "无",
                         "、".join(b_fields) or "无"))
    if len(common) == 1:
        return common[0], "唯一共同候选“%s”" % common[0]
    a_first, b_first = _first_field(a_records), _first_field(b_records)
    if a_first and a_first == b_first:
        return a_first, "共同首列“%s”" % a_first
    return None, ("探测不到双方共有的 key 字段（分片候选 %s；判读候选 %s）"
                  % ("、".join(a_fields) or "无", "、".join(b_fields) or "无"))


def _ledger_key(record, key_field=None):
    if key_field and key_field in record:
        return record[key_field]
    for cand in KEY_PRIORITY:
        if cand in record:
            return record[cand]
    return next(iter(record.values()), None)


def _ledger_records(path: pathlib.Path):
    if path.suffix.lower() == ".tsv":
        records, _n, err = _read_shard(path)
        return records, err
    records, _n, errors = _read_jsonl(path)
    return records, (errors[0][1] if errors else None)


def audit(shards_dir: pathlib.Path, judgements_dir: pathlib.Path,
          ledger: pathlib.Path = None, tag: str = None,
          key_field: str = None, reject_synthetic: bool = False):
    """返回 (rows, stats)。rows 为 (code, 判据, 是否通过, 细节)。"""
    rows, stats = [], {
        "shards": 0, "judgements": 0, "pairs": 0,
        "shard_rows": 0, "judg_rows": 0, "ledger_keys": 0,
        "dep_missing": False,
    }

    # S1 目录存在；--batch 同时过滤分片与判读件，批外件不进任何判据
    missing_dirs = [str(d) for d in (shards_dir, judgements_dir) if not d.is_dir()]
    shards_all = _data_files(shards_dir)
    judg_all = _data_files(judgements_dir)
    shard_files = [p for p in shards_all if _match_tag(p, tag)]
    judg_files = [p for p in judg_all if _match_tag(p, tag)]
    stats["shards"] = len(shard_files)
    stats["judgements"] = len(judg_files)
    if tag:
        scope = ("批次 %s：分片 %d／%d 件、判读 %d／%d 件"
                 % (tag, len(shard_files), len(shards_all),
                    len(judg_files), len(judg_all)))
    else:
        scope = "分片 %d 件、判读 %d 件" % (len(shard_files), len(judg_files))
    if missing_dirs:
        stats["dep_missing"] = True
        rows.append(("S1", "分片目录与判读目录存在且批次内非空", False,
                     "目录不存在：%s" % "、".join(missing_dirs)))
    elif not shard_files or not judg_files:
        rows.append(("S1", "分片目录与判读目录存在且批次内非空", False,
                     "%s（批次内为空，不得空转）" % scope))
    else:
        rows.append(("S1", "分片目录与判读目录存在且批次内非空", True, scope))

    if stats["dep_missing"]:
        for code, name in (("S2", "每个分片有同名判读件"),
                           ("S3", "判读件行数＝分片行数"),
                           ("S4", "判读件 key 集合＝分片 key 集合"),
                           ("S5", "判读 JSON 全合法且无重复 key"),
                           ("S6", "台账 key 总量与重复"),
                           ("S7", "拒绝合成件（pilot-synthetic／pilot 文件名）")):
            rows.append((code, name, False, "依赖缺失，跳过"))
        return rows, stats

    # S2 同名判读件（判读侧已按同一 tag 过滤）
    judgments_by_stem = {p.stem: p for p in judg_files}
    pairs, no_judg = [], []
    for shard in shard_files:
        mate = judgments_by_stem.get(shard.stem)
        if mate is None:
            no_judg.append(shard.name)
        else:
            pairs.append((shard, mate))
    stats["pairs"] = len(pairs)
    if not shard_files:
        rows.append(("S2", "每个分片有同名判读件", False,
                     "批次前缀 %s 下无分片，判据为空转" % (tag or "—")))
    else:
        rows.append(("S2", "每个分片有同名判读件", not no_judg,
                     "配对 %d/%d；缺判读件 %s"
                     % (len(pairs), len(shard_files),
                        "、".join(no_judg) if no_judg else "无")))

    # 逐件读入（S3–S5 只用配对件；缺件由 no_judg 显式记账）
    shard_data, judg_data = {}, {}
    for shard, mate in pairs:
        recs, n_lines, err = _read_shard(shard)
        shard_data[shard] = (recs, n_lines, err)
        stats["shard_rows"] += n_lines
        jrecs, jn_lines, jerrors = _read_jsonl(mate)
        judg_data[mate] = (jrecs, jn_lines, jerrors)
        stats["judg_rows"] += jn_lines

    # S3 行数：缺判读件的分片必须显式 FAIL，不得因未配对而空转 PASS
    s3_bad = []
    if not shard_files:
        s3_bad.append("批次内无分片，判据无法执行（不得空转）")
    for name in no_judg:
        s3_bad.append("%s 缺同名判读件，行数无从核对" % name)
    for shard, mate in pairs:
        _sr, n_s, shard_err = shard_data[shard]
        _jr, n_j, _je = judg_data[mate]
        if shard_err:
            s3_bad.append("%s 分片读取异常（%s）" % (shard.name, shard_err))
        if n_s != n_j:
            s3_bad.append("%s 分片 %d 行 vs %s 判读 %d 行"
                          % (shard.name, n_s, mate.name, n_j))
    rows.append(("S3", "判读件行数＝分片行数", not s3_bad,
                 "；".join(s3_bad) if s3_bad
                 else "配对 %d 组，分片 %d 行＝判读 %d 行"
                      % (len(pairs), stats["shard_rows"], stats["judg_rows"])))

    # S4 key 集合
    all_srecs = [r for s, _m in pairs for r in shard_data[s][0]]
    all_jrecs = [r for _s, m in pairs for r in judg_data[m][0]]
    key_used, key_note = _resolve_key_field(all_srecs, all_jrecs, key_field)
    s4_bad = []
    if not shard_files:
        s4_bad.append("批次内无分片，判据无法执行（不得空转）")
    if key_used is None:
        s4_bad.append(key_note)
    else:
        for shard, mate in pairs:
            srecs = shard_data[shard][0]
            jrecs = judg_data[mate][0]
            s_keys = {r.get(key_used) for r in srecs}
            j_keys = {r.get(key_used) for r in jrecs}
            null_s = sum(1 for r in srecs if r.get(key_used) is None)
            null_j = sum(1 for r in jrecs if r.get(key_used) is None)
            lack = sorted(map(str, s_keys - j_keys))
            extra = sorted(map(str, j_keys - s_keys))
            if null_s or null_j:
                s4_bad.append("%s／%s 缺“%s”字段 %d／%d 行"
                              % (shard.name, mate.name, key_used, null_s, null_j))
            if lack:
                s4_bad.append("%s 判读缺 key %d 条：%s"
                              % (shard.stem, len(lack), "、".join(lack)))
            if extra:
                s4_bad.append("%s 判读多 key %d 条：%s"
                              % (shard.stem, len(extra), "、".join(extra)))
    rows.append(("S4", "判读件 key 集合＝分片 key 集合", not s4_bad,
                 "；".join(s4_bad) if s4_bad
                 else "key 字段＝%s（%s）；配对 %d 组集合相等"
                      % (key_used, key_note, len(pairs))))

    # S5 JSON 合法性 + 判读件内重复 key；缺判读件的分片同样显式 FAIL
    s5_bad = []
    if not shard_files:
        s5_bad.append("批次内无分片，判据无法执行（不得空转）")
    for name in no_judg:
        s5_bad.append("%s 缺同名判读件，JSON 无从核对（空转即假绿）" % name)
    for mate in [m for _s, m in pairs]:
        _jr, _n, jerrors = judg_data[mate]
        for lineno, msg in jerrors:
            s5_bad.append("%s:%d %s" % (mate.name, lineno, msg))
        if key_used is not None:
            seen, dup = set(), []
            for r in judg_data[mate][0]:
                k = r.get(key_used)
                if k in seen and k not in dup:
                    dup.append(k)
                seen.add(k)
            if dup:
                s5_bad.append("%s 重复 key %d 条：%s"
                              % (mate.name, len(dup), "、".join(map(str, dup))))
    rows.append(("S5", "判读 JSON 全合法且无重复 key", not s5_bad,
                 "；".join(s5_bad) if s5_bad
                 else "配对 %d 件，JSON 全合法、无重复 key" % len(pairs)))

    # S6 台账
    if ledger is None:
        rows.append(("S6", "台账 key 总量与重复", True,
                     "未给 --ledger，跳过（不计 FAIL）"))
    elif key_used is None:
        rows.append(("S6", "台账 key 总量与重复", False,
                     "key 字段未定（%s），台账比对无法执行（不得空转）" % key_note))
    elif not ledger.is_file():
        rows.append(("S6", "台账 key 总量与重复", False,
                     "台账不存在：%s" % ledger))
    else:
        lrecs, lerr = _ledger_records(ledger)
        l_keys = [_ledger_key(r, key_used) for r in lrecs]
        seen, dup = set(), []
        for k in l_keys:
            if k in seen and k not in dup:
                dup.append(k)
            seen.add(k)
        stats["ledger_keys"] = len(l_keys)
        j_key_total = len({r.get(key_used) for r in all_jrecs})
        s6_bad = []
        if lerr:
            s6_bad.append("台账读取异常：%s" % lerr)
        if dup:
            s6_bad.append("台账重复 key %d 条：%s"
                          % (len(dup), "、".join(map(str, dup))))
        if len(l_keys) < j_key_total:
            s6_bad.append("台账 %d key < 判读 %d key" % (len(l_keys), j_key_total))
        rows.append(("S6", "台账 key 总量与重复", not s6_bad,
                     "；".join(s6_bad) if s6_bad
                     else "台账 %d key ≥ 判读 %d key，无重复"
                          % (len(l_keys), j_key_total)))

    # S7 合成件拒绝（默认关闭）
    if not reject_synthetic:
        rows.append(("S7", "拒绝合成件（pilot-synthetic／pilot 文件名）", True,
                     "未启用 --reject-synthetic，跳过（生产收口建议开启）"))
    else:
        s7_bad = []
        for p in shard_files + judg_files:
            if "pilot" in p.name.lower():
                s7_bad.append("文件名含 pilot：%s" % p.name)
        for mate in [m for _s, m in pairs]:
            for rec in judg_data[mate][0]:
                if SYNTH_MARK in json.dumps(rec, ensure_ascii=False):
                    s7_bad.append("%s 判读行含 %s" % (mate.name, SYNTH_MARK))
                    break
        rows.append(("S7", "拒绝合成件（pilot-synthetic／pilot 文件名）",
                     not s7_bad,
                     "；".join(s7_bad) if s7_bad
                     else "批次内分片 %d 件、判读 %d 件，无合成标记"
                          % (len(shard_files), len(judg_files))))
    return rows, stats


def _report(rows, title):
    print("=" * 72)
    print(title)
    print("=" * 72)
    fails = 0
    for code, name, ok, detail in rows:
        print("  [%s] %-4s %s" % ("PASS" if ok else "FAIL", code, name))
        print("           %s" % detail)
        if not ok:
            fails += 1
    print("-" * 72)
    print("  合计 %d 项，FAIL %d 项" % (len(rows), fails))
    return fails


# ── 自检 ────────────────────────────────────────────────────────────────
_SHARD_NAME = "f1_b12_s001.jsonl"
_SHARD_NAME2 = "f1_b12_s002.jsonl"
_OUT_SHARD = "f4_b99_s001.jsonl"          # 批外分片（3 行，故意与判读不成对）
_OUT_JUDG = "pilot_f4_b99_notes.jsonl"    # 批外判读（含合成标记）


def _row(pk):
    key = "host-a|%s|05-卷册大纲/x.md" % pk
    return {"key": key, "line": int(pk) * 5, "db": "host-a", "pk": pk,
            "anchor_line": "<!-- ROW_MINE: host-a.messages.%s -->" % pk,
            "summ_line": "样例行 %s。" % pk}


def _judg(pk):
    return {"key": "host-a|%s|05-卷册大纲/x.md" % pk, "line": int(pk) * 5,
            "判定": "keep", "理由": "样例", "问题": []}


def _write_fixture(root: pathlib.Path):
    shards = root / "shards"
    judg = root / "judgements"
    shards.mkdir(parents=True, exist_ok=True)
    judg.mkdir(parents=True, exist_ok=True)
    for name, pks in ((_SHARD_NAME, (1, 2)), (_SHARD_NAME2, (3, 4))):
        (shards / name).write_text(
            "\n".join(json.dumps(_row(pk), ensure_ascii=False) for pk in pks) + "\n",
            encoding="utf-8")
        (judg / name).write_text(
            "\n".join(json.dumps(_judg(pk), ensure_ascii=False) for pk in pks) + "\n",
            encoding="utf-8")
    # 批外件：与 --batch f1_b12 无关，行数／标记故意不合规
    (shards / _OUT_SHARD).write_text(
        "\n".join(json.dumps(_row(pk), ensure_ascii=False) for pk in (91, 92, 93)) + "\n",
        encoding="utf-8")
    (judg / _OUT_JUDG).write_text(
        json.dumps({"key": "host-a|91|05-卷册大纲/x.md", "判定": "keep",
                    "理由": SYNTH_MARK + " 样例"}, ensure_ascii=False) + "\n",
        encoding="utf-8")
    (root / "processed_f1.jsonl").write_text(
        "\n".join(json.dumps({"key": _row(pk)["key"], "判定": "keep"},
                             ensure_ascii=False) for pk in (1, 2, 3, 4)) + "\n",
        encoding="utf-8")
    return shards, judg


def _mutate_missing_judgement(shards, judg):
    (judg / _SHARD_NAME2).unlink()
    assert not (judg / _SHARD_NAME2).exists(), "回读：缺判读件夹具未落盘"


def _mutate_row_shift(shards, judg):
    lines = (judg / _SHARD_NAME).read_text(encoding="utf-8").splitlines()
    (judg / _SHARD_NAME).write_text(lines[0] + "\n", encoding="utf-8")
    recs, n, _e = _read_jsonl(judg / _SHARD_NAME)
    assert len(recs) == 1 and n == 1, "回读：行数不符夹具未落盘（%d 行）" % n


def _mutate_bad_json(shards, judg):
    with (judg / _SHARD_NAME).open("a", encoding="utf-8") as fh:
        fh.write('{"key": "host-a|9|05-卷册大纲/x.md", "判定": \n')
    recs, n, errors = _read_jsonl(judg / _SHARD_NAME)
    assert n == 3 and errors, "回读：坏 JSON 夹具未落盘（%d 行、错 %d 条）" % (n, len(errors))


def _mutate_dup_key(shards, judg):
    lines = (judg / _SHARD_NAME).read_text(encoding="utf-8").splitlines()
    dup = json.dumps(_judg(1), ensure_ascii=False)
    (judg / _SHARD_NAME).write_text(dup + "\n" + dup + "\n", encoding="utf-8")
    recs, n, _e = _read_jsonl(judg / _SHARD_NAME)
    keys = {r["key"] for r in recs}
    assert n == 2 and len(keys) == 1, "回读：重复 key 夹具未落盘（%d 行、%d key）" % (n, len(keys))


def _mutate_key_ambiguous(shards, judg):
    """双方同时具备 pk／id／key 三候选，未给 --key-field 时必须 FAIL。"""
    for name in (_SHARD_NAME, _SHARD_NAME2):
        p = shards / name
        recs = [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines()
                if l.strip()]
        p.write_text("\n".join(
            json.dumps(dict(r, id=1000 + int(r["pk"])), ensure_ascii=False)
            for r in recs) + "\n", encoding="utf-8")
        q = judg / name
        jrecs = [json.loads(l) for l in q.read_text(encoding="utf-8").splitlines()
                 if l.strip()]
        q.write_text("\n".join(
            json.dumps(dict(r, pk=int(r["key"].split("|")[1]),
                            id=1000 + int(r["key"].split("|")[1])),
                       ensure_ascii=False) for r in jrecs) + "\n",
            encoding="utf-8")
    a = [json.loads(l) for l in (shards / _SHARD_NAME).read_text(
        encoding="utf-8").splitlines() if l.strip()]
    b = [json.loads(l) for l in (judg / _SHARD_NAME).read_text(
        encoding="utf-8").splitlines() if l.strip()]
    for rec in a + b:
        assert {"pk", "id", "key"} <= set(rec), "回读：key 歧义夹具未落盘"


def _mutate_synthetic(shards, judg):
    """判读行内嵌 pilot-synthetic ＋ 判读文件名为 pilot 前缀（均含批次标签）。"""
    p = judg / _SHARD_NAME
    recs = [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines()
            if l.strip()]
    recs[0]["理由"] = SYNTH_MARK + " 合成样例"
    p.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in recs) + "\n",
                 encoding="utf-8")
    (judg / "pilot_f1_b12_notes.jsonl").write_text(
        json.dumps({"key": "host-a|1|05-卷册大纲/x.md", "判定": "keep"},
                   ensure_ascii=False) + "\n", encoding="utf-8")
    back = (judg / _SHARD_NAME).read_text(encoding="utf-8")
    assert SYNTH_MARK in back, "回读：合成标记夹具未落盘"
    assert (judg / "pilot_f1_b12_notes.jsonl").exists(), "回读：pilot 文件名夹具未落盘"


def _readback_positive(shards, judg):
    """回读断言：自检输入本身非空转，且批外件确实在场。"""
    s_all = _data_files(shards)
    j_all = _data_files(judg)
    sfiles = [p for p in s_all if "f1_b12" in p.name]
    jfiles = [p for p in j_all if "f1_b12" in p.name]
    assert len(s_all) == 3, "回读：分片目录应为 3 件（含 1 件批外），实为 %d" % len(s_all)
    assert len(j_all) == 3, "回读：判读目录应为 3 件（含 1 件批外），实为 %d" % len(j_all)
    assert len(sfiles) == 2, "回读：批次内分片应为 2 件，实为 %d" % len(sfiles)
    assert len(jfiles) == 2, "回读：批次内判读应为 2 件，实为 %d" % len(jfiles)
    n_s = sum(len(_read_shard(p)[0]) for p in sfiles)
    n_j = sum(len(_read_jsonl(p)[0]) for p in jfiles)
    assert n_s == 4, "回读：分片应为 2×2＝4 行，实为 %d" % n_s
    assert n_j == 4, "回读：判读应为 2×2＝4 行，实为 %d" % n_j
    for p in sfiles:
        assert (judg / p.name).exists(), "回读：%s 无同名判读件" % p.name
    s_keys = {str(r["pk"]) for p in sfiles for r in _read_shard(p)[0]}
    j_keys = {r["key"].split("|")[1] for p in jfiles for r in _read_jsonl(p)[0]}
    assert s_keys == j_keys, "回读：正样本 key 集合不等（%s vs %s）" % (s_keys, j_keys)
    # 批外件确为不合规样本，否则“批外件过滤”夹具会空转
    out_s = shards / _OUT_SHARD
    out_j = judg / _OUT_JUDG
    assert len(_read_jsonl(out_s)[0]) == 3, "回读：批外分片应为 3 行"
    assert SYNTH_MARK in out_j.read_text(encoding="utf-8"), "回读：批外判读应含合成标记"
    assert not (judg / out_s.name).exists(), "回读：批外分片不应有同名判读"


def _run_cli(shards, judg, ledger=None, batch=None, key_field=None,
             reject_synthetic=False):
    cmd = [sys.executable, str(pathlib.Path(__file__).resolve()),
           "--shards", str(shards), "--judgements", str(judg)]
    if ledger is not None:
        cmd += ["--ledger", str(ledger)]
    if batch is not None:
        cmd += ["--batch", batch]
    if key_field is not None:
        cmd += ["--key-field", key_field]
    if reject_synthetic:
        cmd += ["--reject-synthetic"]
    proc = subprocess.run(cmd, capture_output=True, text=True,
                          encoding="utf-8", errors="replace")
    marks = {code: status for status, code
             in re.findall(r"(?m)^\s*\[(PASS|FAIL)\]\s+(S\d)\b", proc.stdout)}
    return proc.returncode, marks, proc.stdout + proc.stderr


def _expect(title, case_dir, failures, mutate=None, ledger=True, batch="f1_b12",
            key_field=None, reject_synthetic=False,
            want_exit=0, want_fail=()):
    """跑一枚夹具并校验退出码、七条判据齐全与命中集合。"""
    shards, judg = _write_fixture(case_dir)
    _readback_positive(shards, judg)
    if mutate is not None:
        mutate(shards, judg)
    ld = (case_dir / "processed_f1.jsonl") if ledger else None
    code, marks, out = _run_cli(shards, judg, ld, batch, key_field, reject_synthetic)
    fails = {c for c, m in marks.items() if m == "FAIL"}
    print("· %-22s 退出码 %d，FAIL %s" % (title, code, sorted(fails) or "无"))
    if code != want_exit:
        failures.append("%s 退出码 %d≠%d" % (title, code, want_exit))
    if len(marks) != 7:
        failures.append("%s 未打印 S1–S7 七条判据（实 %d 条）" % (title, len(marks)))
    if want_exit == 0:
        if fails:
            failures.append("%s 应全 PASS，实际 FAIL %s" % (title, sorted(fails)))
    else:
        missing = set(want_fail) - fails
        if missing:
            failures.append("%s 未命中 %s（实际 FAIL %s）"
                            % (title, sorted(missing), sorted(fails)))
    if not out.strip():
        failures.append("%s 输出为空，自检空转" % title)
    return shards, judg, code, marks, out


def cmd_selftest():
    failures = []
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="oaabatch_"))
    try:
        _expect("正样本 2 片×2 行", tmp / "case_01", failures)
        _expect("缺判读件不得空转", tmp / "case_02", failures,
                mutate=_mutate_missing_judgement, want_exit=1,
                want_fail=("S2", "S3", "S5"))
        _expect("行数不符", tmp / "case_03", failures,
                mutate=_mutate_row_shift, want_exit=1, want_fail=("S3",))
        _expect("坏 JSON", tmp / "case_04", failures,
                mutate=_mutate_bad_json, want_exit=1, want_fail=("S5",))
        _expect("重复 key", tmp / "case_05", failures,
                mutate=_mutate_dup_key, want_exit=1, want_fail=("S4", "S5"))
        # 批外件：带标签须零 FAIL 且 S1 只计批次内两侧；不带标签须被批外件拉红
        _sh, _j, _c, _m, out = _expect(
            "批外件（--batch 过滤）", tmp / "case_06a", failures)
        if "判读 2／3" not in out:
            failures.append("批外判读件未被过滤：S1 未显示判读 2／3")
        _expect("批外件（不过滤即 FAIL）", tmp / "case_06b", failures,
                batch=None, want_exit=1, want_fail=("S2", "S3", "S5"))
        # key 字段歧义：未显式指定须 FAIL 并提示 --key-field
        _sh, _j, _c, _m, out = _expect(
            "key 字段歧义", tmp / "case_07", failures,
            mutate=_mutate_key_ambiguous, ledger=False,
            want_exit=1, want_fail=("S4",))
        if "--key-field" not in out:
            failures.append("key 字段歧义未提示 --key-field（提示失效）")
        _expect("key 字段显式 pk", tmp / "case_07b", failures,
                mutate=_mutate_key_ambiguous, key_field="pk")
        # 合成件：默认放行，启用 --reject-synthetic 须 FAIL
        _expect("synthetic 默认放行", tmp / "case_08", failures,
                mutate=_mutate_synthetic)
        _expect("synthetic 拒绝", tmp / "case_08b", failures,
                mutate=_mutate_synthetic, reject_synthetic=True,
                want_exit=1, want_fail=("S7",))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    if failures:
        print("  ❌ 判据非空自检失败：")
        for f in failures:
            print("     - %s" % f)
        return 1
    print("  ✅ 判据非空自检通过：正样本 0 FAIL；缺判读件不得空转／批外件过滤／"
          "key 字段歧义／synthetic 拒绝四类新夹具与行数不符／坏 JSON／重复 key "
          "既有夹具均命中，退出码 0／1 正确")
    return 0


def main():
    ap = argparse.ArgumentParser(description="OAA 批次收口对账门禁（第三十件）")
    ap.add_argument("--shards", metavar="DIR", help="分片目录")
    ap.add_argument("--judgements", metavar="DIR", help="判读目录")
    ap.add_argument("--ledger", metavar="FILE", help="台账 processed_fN.jsonl（可选）")
    ap.add_argument("--batch", metavar="TAG",
                    help="批次标签：按“文件名含 TAG”同时过滤分片与判读件（可选）")
    ap.add_argument("--key-field", choices=KEY_PRIORITY, dest="key_field",
                    help="显式指定 key 字段；不给时仅唯一共同候选可自动采用")
    ap.add_argument("--reject-synthetic", action="store_true",
                    help="判读行含 pilot-synthetic 或文件名含 pilot 即 FAIL"
                         "（默认关闭，生产收口建议开启）")
    ap.add_argument("--selftest", action="store_true", help="判据非空自检")
    args = ap.parse_args()

    if args.selftest:
        return cmd_selftest()
    if not args.shards or not args.judgements:
        print("用法：audit_oaa_batch.py --shards DIR --judgements DIR "
              "[--ledger FILE] [--batch TAG] [--key-field pk|id|key] "
              "[--reject-synthetic]｜--selftest", file=sys.stderr)
        return 2

    shards = pathlib.Path(args.shards)
    judg = pathlib.Path(args.judgements)
    ledger = pathlib.Path(args.ledger) if args.ledger else None
    rows, stats = audit(shards, judg, ledger, args.batch, args.key_field,
                        args.reject_synthetic)
    fails = _report(rows, "OAA 批次收口对账门禁（第三十件）")
    if stats["dep_missing"]:
        print("  依赖缺失：目录不存在（退出码 2）", file=sys.stderr)
        return 2
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
