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
S4 判读件 key 集合＝分片 key 集合。key 字段须显式或可自动判定：
   给 `--key-field` 时严格按该字段（须为双方全体共有）；
   未给时逐一遍历候选字段（`pk`／`id`／`key`），分别计算两侧 key 集合，
   只要有任一字段使两侧集合相等即 PASS 并注明所用字段；
   候选字段全不相等才 FAIL，并列出各字段的缺／多差异计数；
   零候选时退到双方共同首列。不得静默按 `pk→id→key` 切换。
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
    python audit_oaa_batch.py --reconcile-ledger [--ledger-dir DIR]
        [--beacon-dir DIR] [--anchors FILE|--snapshot-rev REV|--outline DIR]
        [--csv PATH] [--fail-on-other]

台账对账（TD-012／FR-11，`--reconcile-ledger`）
--------------------------------------------
对“台账合并集”与“四组浮标已审合计”逐条对账（F1–F4 的 317,895 对 318,541 一类
的 646 条差）。四组浮标只存**宿主级**计数（`beacon.json` 的 `progress`），
不含被计入的 key 清单，故“已审侧”须由**锚点清单**重建：

* `--anchors FILE`：JSON 数组，元素为 `"<库>|<pk>|<宿主相对路径>"`（与台账同形），
  即浮标计数当刻的锚点清单；
* `--snapshot-rev REV`：以 `git grep -o` 只读重建该提交下 `05-卷册大纲/` 的锚点清单
  （提交须与浮标刷新同刻；给了 `--beacon-dir/tree_prev.json` 时逐宿主校验 n／h，
  一致率不足即判 FAIL，防止拿错提交当快照）；
* `--outline DIR`：直接扫现行大纲树（默认口径，路径漂移时仅供诊断）。

差异分类（每类逐条列 key，证据列写 CSV）：

R1 `mail-insight-invisible`  `MAIL_INSIGHT` 块，浮标扫描器只认 `ROW_MINE`，永不计入
R2 `baseline-unassigned`     key 的宿主不在任何一份认领清单（含路径改名／笔误）
R3 `orphan-key`              宿主已认领，但该锚点不在快照宿主内（已移除／已迁走）
R4 `other`                   key 形制异常（无“库|pk|路径”三段），须人工裁

结算式：`净差 = 合并集 − 浮标已审合计`，`未计入 key 数 − 浮标重复计 = 净差`。
浮标按锚点**出现次数**计数，同一宿主内重复出现的同名锚点会被多计，故两条口径
相差“重复计”条数——该条数由本命令显式给出，不得拿来凑数。

退出码：0 全 PASS／1 任一 FAIL／2 依赖缺失（目录不存在，或未给必需参数）

依赖：仅标准库（`--snapshot-rev` 另需本机 git）。只读，不写任何受审文件。
"""
import argparse
import collections
import csv
import hashlib
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

# 台账对账口径
LEDGER_FILES = ("processed.jsonl", "processed_f1.jsonl", "processed_f2.jsonl",
                "processed_f3.jsonl", "processed_f4.jsonl")
CLAIM_GROUPS = ("F1", "F2", "F3", "F4")
RM_PAT = re.compile(r"ROW_MINE:\s*([\w-]+)\.([\w.]+)\.(\d+)")
MI_PAT = re.compile(r"<!--\s*MAIL_INSIGHT:\s*([^>]+?)\s*-->")
CAT_ORDER = ("mail-insight-invisible", "baseline-unassigned", "orphan-key", "other")
CSV_HEADER = ("key", "category", "group", "ledger_files", "verdict", "batch", "evidence")


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


def _candidate_key_fields(a_records, b_records, explicit=None):
    """返回 (候选字段列表, 说明, 分片候选, 判读候选)。

    explicit 给定时候选即该字段；未给定时取 KEY_PRIORITY 中双方共有者；
    零候选退到双方共同首列；仍无则候选为空、说明为失败原因。
    """
    a_fields = _committed_fields(a_records)
    b_fields = _committed_fields(b_records)
    if explicit:
        lack = []
        if explicit not in a_fields:
            lack.append("分片")
        if explicit not in b_fields:
            lack.append("判读")
        if lack:
            return [], ("显式 key 字段“%s”在%s侧非全体共有（分片候选 %s；判读候选 %s）"
                        % (explicit, "、".join(lack),
                           "、".join(a_fields) or "无", "、".join(b_fields) or "无")), \
                   a_fields, b_fields
        return [explicit], "显式指定“%s”" % explicit, a_fields, b_fields
    common = [c for c in KEY_PRIORITY if c in a_fields and c in b_fields]
    if len(common) == 1:
        return common, "唯一共同候选“%s”" % common[0], a_fields, b_fields
    if common:
        return common, "", a_fields, b_fields
    a_first, b_first = _first_field(a_records), _first_field(b_records)
    if a_first and a_first == b_first:
        return [a_first], "共同首列“%s”" % a_first, a_fields, b_fields
    return [], ("探测不到双方共有的 key 字段（分片候选 %s；判读候选 %s）"
                % ("、".join(a_fields) or "无", "、".join(b_fields) or "无")), \
           a_fields, b_fields


def _key_set_diff(shard_data, judg_data, pairs, field):
    """按 field 逐配对比较 key 集合。

    返回 (全配对两侧相等且无空值, lack 列表, extra 列表, 两侧空值数)。
    """
    lack, extra, null_s, null_j = [], [], 0, 0
    equal = True
    for shard, mate in pairs:
        srecs = shard_data[shard][0]
        jrecs = judg_data[mate][0]
        s_keys = {r.get(field) for r in srecs}
        j_keys = {r.get(field) for r in jrecs}
        null_s += sum(1 for r in srecs if r.get(field) is None)
        null_j += sum(1 for r in jrecs if r.get(field) is None)
        lack += sorted(map(str, s_keys - j_keys))
        extra += sorted(map(str, j_keys - s_keys))
        if s_keys != j_keys:
            equal = False
    return (equal and not null_s and not null_j), lack, extra, null_s, null_j


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

    # S4 key 集合：显式字段严格；未显式时逐候选字段试算，任一字段两侧集合相等即 PASS
    all_srecs = [r for s, _m in pairs for r in shard_data[s][0]]
    all_jrecs = [r for _s, m in pairs for r in judg_data[m][0]]
    cands, cand_note, _a_fields, _b_fields = _candidate_key_fields(
        all_srecs, all_jrecs, key_field)
    key_used, key_note = None, cand_note
    s4_bad = []
    if not shard_files:
        s4_bad.append("批次内无分片，判据无法执行（不得空转）")
    if not cands:
        s4_bad.append(cand_note)
    elif key_field is not None:
        key_used = cands[0]
        ok, lack, extra, null_s, null_j = _key_set_diff(
            shard_data, judg_data, pairs, key_used)
        if not ok:
            if null_s or null_j:
                s4_bad.append("缺“%s”字段 %d／%d 行" % (key_used, null_s, null_j))
            if lack:
                s4_bad.append("判读缺 key %d 条：%s" % (len(lack), "、".join(lack)))
            if extra:
                s4_bad.append("判读多 key %d 条：%s" % (len(extra), "、".join(extra)))
    else:
        chosen, diffs = None, []
        for f in cands:
            ok, lack, extra, null_s, null_j = _key_set_diff(
                shard_data, judg_data, pairs, f)
            diffs.append((f, ok, len(lack), len(extra), null_s, null_j))
            if ok and chosen is None:
                chosen = f
        if chosen is not None:
            key_used = chosen
            key_note = (("多候选 %s 中“%s”两侧集合相等，自动采用"
                         % ("、".join(cands), chosen)) if len(cands) > 1 else cand_note)
        else:
            # 全部不等：S4 FAIL；S5／S6 仍取最高优先候选作字段，
            # 以免重复 key／台账比对因字段缺失而空转（不放宽 S4 判据）。
            key_used = cands[0]
            s4_bad.append("候选字段无一使两侧集合相等：%s"
                          % "；".join("%s 缺 %d／多 %d（空值 %d／%d）"
                                      % (f, lk, ex, ns, nj)
                                      for f, _ok, lk, ex, ns, nj in diffs))
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


# ── 台账对账（--reconcile-ledger，TD-012／FR-11）────────────────────────
def _ledger_index(directory: pathlib.Path):
    """读合并台账 → ({key: [(件名, 判定, 批次)]}, 各件非空行数, 异常列表)。"""
    index, rows, errors = {}, {}, []
    for name in LEDGER_FILES:
        path = directory / name
        if not path.is_file():
            errors.append("%s 不存在" % name)
            continue
        records, n_lines, bad = _read_jsonl(path)
        rows[name] = n_lines
        for lineno, msg in bad:
            errors.append("%s:%d %s" % (name, lineno, msg))
        for rec in records:
            key = rec.get("key")
            if not isinstance(key, str):
                errors.append("%s 有记录缺 key 字段" % name)
                continue
            index.setdefault(key, []).append(
                (name, str(rec.get("判定", "")), str(rec.get("批次", ""))))
    return index, rows, errors


def _host_list(path: pathlib.Path):
    if not path.is_file():
        return []
    return [ln.strip() for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip()]


def _anchor_key(db, pk, rel):
    return "%s|%s|%s" % (db, pk, rel)


def _anchors_from_outline(directory: pathlib.Path):
    """扫大纲树 → (全部出现计数, ROW_MINE 每宿主计数, MAIL_INSIGHT key 集, 异常)。

    只读。`per_host` 只计 `ROW_MINE`（浮标 scan_outline 同口径），`MAIL_INSIGHT`
    另存，故能同时给出“块仍在盘”与“浮标可见锚点数”两件事。
    """
    occ = collections.Counter()
    per_host = collections.Counter()
    mi_keys = set()
    if not directory.is_dir():
        return occ, per_host, mi_keys, ["大纲目录不存在：%s" % directory]
    for path in sorted(directory.rglob("*.md")):
        try:
            txt = path.read_text(encoding="utf-8", errors="replace")
        except OSError as ex:
            return occ, per_host, mi_keys, ["读取失败 %s：%s" % (path, ex)]
        rel = path.relative_to(directory.parent).as_posix()
        for m in RM_PAT.finditer(txt):
            occ[_anchor_key(m.group(1), m.group(3), rel)] += 1
            per_host[rel] += 1
        for m in MI_PAT.finditer(txt):
            key = _anchor_key("MAIL_INSIGHT", m.group(1).strip(), rel)
            occ[key] += 1
            mi_keys.add(key)
    return occ, per_host, mi_keys, []


def _anchors_from_file(path: pathlib.Path):
    """读锚点清单 JSON（数组，元素形如 `<库>|<pk>|<宿主>`）→ 同 outline 口径。"""
    occ, per_host, mi_keys = collections.Counter(), collections.Counter(), set()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as ex:
        return occ, per_host, mi_keys, ["锚点清单读取失败：%s" % ex]
    if not isinstance(data, list):
        return occ, per_host, mi_keys, ["锚点清单须为 JSON 数组"]
    for key in data:
        if not isinstance(key, str) or key.count("|") < 2:
            return occ, per_host, mi_keys, ["锚点清单有非“库|pk|宿主”元素：%r" % (key,)]
        occ[key] += 1
        if key.startswith("MAIL_INSIGHT|"):
            mi_keys.add(key)
        else:
            per_host[key.split("|", 2)[2]] += 1
    return occ, per_host, mi_keys, []


def _anchors_from_git(rev: str, repo_root: pathlib.Path):
    """以 git grep -o 只读重建某提交下 `05-卷册大纲/` 的锚点清单。"""
    occ, per_host, mi_keys = collections.Counter(), collections.Counter(), set()
    for pat, kind in ((r"ROW_MINE:[^>]*", "rm"), (r"MAIL_INSIGHT:[^>]*", "mi")):
        proc = subprocess.run(["git", "grep", "-o", "-E", pat, rev, "--", "05-卷册大纲"],
                              cwd=str(repo_root), capture_output=True)
        if proc.returncode not in (0, 1):
            return occ, per_host, mi_keys, ["git grep 失败（rev=%s）：%s"
                                            % (rev, proc.stderr.decode("utf-8",
                                                                       "replace").strip())]
        for line in proc.stdout.decode("utf-8", "replace").splitlines():
            _rev, sep, rest = line.partition(":")
            if not sep or not rest:
                continue
            idx = rest.find("ROW_MINE:" if kind == "rm" else "MAIL_INSIGHT:")
            if idx <= 0:
                continue
            rel, match = rest[:idx].rstrip(":"), rest[idx:]
            if kind == "rm":
                m = RM_PAT.search(match)
                if not m:
                    continue
                key = _anchor_key(m.group(1), m.group(3), rel)
                per_host[rel] += 1
            else:
                mid = match.split("MAIL_INSIGHT:", 1)[1].strip().rstrip("-").strip()
                if not mid:
                    continue
                key = _anchor_key("MAIL_INSIGHT", mid, rel)
                mi_keys.add(key)
            occ[key] += 1
    return occ, per_host, mi_keys, []


def _tree_prev_check(beacon_dir: pathlib.Path):
    """读 tree_prev.json（浮标刷新当刻的逐宿主 n／h 指纹）；无则 None。"""
    path = beacon_dir / "tree_prev.json"
    if not path.is_file():
        return None
    try:
        prev = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    if not isinstance(prev, dict) or not prev:
        return None
    return prev


def _anchor_hashes(occ, mi_keys=()):
    """→ ({宿主: (n, h)})，只计 ROW_MINE；h 与 oaa_beacon.scan_outline 同法。"""
    per = collections.defaultdict(list)
    for key, n in occ.items():
        if key in mi_keys:
            continue
        db_pk, rel = key.rsplit("|", 1)
        per[rel].extend([db_pk] * n)
    out = {}
    for rel, anchors in per.items():
        anchors.sort()
        out[rel] = (len(anchors),
                    hashlib.sha1(",".join(anchors).encode("utf-8")).hexdigest()[:12])
    return out


def _classify_key(key, claims, unclaimed, occ, per_host, host_keys):
    """→ (类别, 组, 证据)。判定顺序：形制 → MAIL_INSIGHT → 认领 → 锚点。"""
    parts = key.split("|", 2)
    if (len(parts) != 3 or not all(parts) or not re.match(r"^[A-Za-z0-9_-]+\|", key)
            or not parts[2].startswith("05-卷册大纲/")):
        return "other", "", "key 形制异常（无“库|pk|05-卷册大纲/路径”三段形制，须人工裁）"
    db, _pk, rel = parts
    group = ""
    for g in CLAIM_GROUPS:
        if rel in claims.get(g, ()):
            group = g
            break
    if db == "MAIL_INSIGHT":
        return ("mail-insight-invisible", group,
                "MAIL_INSIGHT 块：浮标扫描器只认 ROW_MINE，块永不计入已审；"
                + ("宿主组=%s；块仍在快照宿主内" % group if occ.get(key, 0)
                   else "宿主组=%s；块已不在快照宿主内" % group if group
                   else "宿主亦未归组"))
    if not group:
        return ("baseline-unassigned", "",
                "宿主不在任何认领清单（claims_F1..F4 与 UNCLAIMED 均无）；"
                + ("该路径不在快照大纲树内" if rel not in per_host else "该路径在快照树内但未被认领"))
    if occ.get(key, 0) == 0:
        n = per_host.get(rel, 0)
        return ("orphan-key", group,
                "宿主组=%s；快照宿主锚点 n=%d；台账该宿主 key M=%d；M−n=%+d"
                % (group, n, host_keys[rel], host_keys[rel] - n))
    return ("other", group, "锚点在快照宿主内却未计入（计数逻辑不一致，须人工核）")


def cmd_reconcile(ledger_dir: pathlib.Path, beacon_dir: pathlib.Path,
                  anchors: pathlib.Path = None, snapshot_rev: str = None,
                  outline: pathlib.Path = None, csv_path: pathlib.Path = None,
                  fail_on_other: bool = False):
    """对账主流程。返回退出码（0 结算闭合／1 FAIL／2 依赖缺失）。"""
    import collections
    fails = []
    print("=" * 72)
    print("OAA 台账对账（--reconcile-ledger，TD-012／FR-11）")
    print("=" * 72)

    if not ledger_dir.is_dir():
        print("  依赖缺失：台账目录不存在 %s" % ledger_dir)
        return 2
    index, row_counts, ledger_errors = _ledger_index(ledger_dir)
    merged = set(index)
    print("  台账件行数：%s" % "｜".join("%s %d" % (n, row_counts[n]) for n in LEDGER_FILES
                                       if n in row_counts))
    print("  台账合并集（去重 key）：%d" % len(merged))
    for msg in ledger_errors:
        fails.append("台账读取异常：%s" % msg)

    beacon_json = beacon_dir / "beacon.json"
    if not beacon_json.is_file():
        print("  依赖缺失：浮标不存在 %s" % beacon_json)
        return 2
    try:
        beacon = json.loads(beacon_json.read_text(encoding="utf-8"))
    except (OSError, ValueError) as ex:
        print("  依赖缺失：浮标读取失败 %s" % ex)
        return 2
    progress = beacon.get("progress", {})
    report = {g: int((progress.get(g) or {}).get("done", 0)) for g in CLAIM_GROUPS}
    report_total = sum(report.values())
    print("  浮标已审合计（四组）：%d（%s）｜beacon.totals.done %s"
          % (report_total, "｜".join("%s %d" % (g, report[g]) for g in CLAIM_GROUPS),
             beacon.get("totals", {}).get("done")))

    claims, unclaimed = {}, set()
    for g in CLAIM_GROUPS:
        claims[g] = set(_host_list(beacon_dir / ("claims_%s.txt" % g)))
    unclaimed = set(_host_list(beacon_dir / "claims_UNCLAIMED.txt"))
    print("  认领清单宿主：%s｜未归组 %d"
          % ("｜".join("%s %d" % (g, len(claims[g])) for g in CLAIM_GROUPS), len(unclaimed)))

    if anchors is None and not snapshot_rev and outline is None:
        print("  依赖缺失：须给 --anchors／--snapshot-rev／--outline 之一（三选一）")
        return 2
    if anchors is not None:
        occ, per_host, mi_keys, err = _anchors_from_file(anchors)
        src = "锚点清单 %s" % anchors
    elif snapshot_rev:
        occ, per_host, mi_keys, err = _anchors_from_git(snapshot_rev, pathlib.Path.cwd())
        src = "git %s @ 05-卷册大纲" % snapshot_rev[:9]
    else:
        occ, per_host, mi_keys, err = _anchors_from_outline(outline)
        src = "现行大纲树 %s（路径漂移时仅供诊断）" % outline
    if err:
        fails += err
        print("  锚点清单不可用：%s" % "；".join(err))
        return 2
    print("  锚点清单：%s｜宿主 %d｜ROW_MINE %d ｜MAIL_INSIGHT %d"
          % (src, len(per_host), sum(per_host.values()), len(mi_keys)))

    prev = _tree_prev_check(beacon_dir)
    if snapshot_rev and prev:
        mine = _anchor_hashes(occ, mi_keys)
        n_ok = sum(1 for r, v in prev.items() if mine.get(r, (None,))[0] == v.get("n"))
        h_ok = sum(1 for r, v in prev.items() if mine.get(r, (None, None))[1] == v.get("h"))
        print("  tree_prev 校验：n 一致 %d／%d，h 一致 %d／%d"
              % (n_ok, len(prev), h_ok, len(prev)))
        if n_ok != len(prev) or h_ok != len(prev):
            fails.append("tree_prev 校验不一致：锚点清单与浮标刷新当刻不同源"
                         "（n %d／%d，h %d／%d）" % (n_ok, len(prev), h_ok, len(prev)))

    # 复原已审侧：逐个 ROW_MINE 锚点出现，key ∈ 合并集即计入（MAIL_INSIGHT 不计）
    occ_done = collections.Counter()
    counted = set()
    dup_keys = []
    for key, n in occ.items():
        if key in mi_keys or key not in merged:
            continue
        counted.add(key)
        rel = key.split("|", 2)[2]
        for g in CLAIM_GROUPS:
            if rel in claims[g]:
                occ_done[g] += n
                break
        if n > 1:
            dup_keys.append((key, n))
    print("  重建已审合计（出现次）：%d（%s）"
          % (sum(occ_done.values()),
             "｜".join("%s %d" % (g, occ_done[g]) for g in CLAIM_GROUPS)))
    print("  重建已审（去重 key）：%d｜浮标重复计：%d"
          % (len(counted), sum(occ_done.values()) - len(counted)))
    if sum(occ_done.values()) != report_total:
        fails.append("重建已审 %d ≠ 浮标 %d（锚点清单非同刻或浮标已陈旧）"
                     % (sum(occ_done.values()), report_total))

    uncounted = merged - counted
    host_keys = collections.Counter(k.split("|", 2)[2] for k in merged if k.count("|") >= 2)
    rows, cat = [], collections.Counter()
    for key in sorted(uncounted):
        category, group, evidence = _classify_key(
            key, claims, unclaimed, occ, per_host, host_keys)
        rec = index.get(key) or [("", "", "")]
        cat[category] += 1
        rows.append((key, category, group, ";".join(sorted({r[0] for r in rec if r[0]})),
                     rec[0][1], rec[0][2], evidence))

    if csv_path is not None:
        csv_path.parent.mkdir(parents=True, exist_ok=True)
        with csv_path.open("w", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh, lineterminator="\n")
            w.writerow(CSV_HEADER)
            w.writerows(rows)
        print("  逐条差异已落：%s（%d 行＋表头）" % (csv_path, len(rows)))

    print("-" * 72)
    for category in CAT_ORDER:
        print("  [%-23s] %6d 条" % (category, cat[category]))
    net = len(merged) - report_total
    dup = sum(occ_done.values()) - len(counted)
    print("  未计入 key 合计 %d ＝ %s" % (len(rows),
                                       "＋".join(str(cat[c]) for c in CAT_ORDER)))
    print("  净差（合并集 − 浮标已审）%d ＝ 未计入 %d − 浮标重复计 %d"
          % (net, len(rows), dup))
    for key, n in dup_keys:
        print("  重复计明细：%s 在宿主内出现 %d 次" % (key, n))

    if len(rows) - dup != net:
        fails.append("结算不闭合：未计入 %d − 重复计 %d ≠ 净差 %d"
                     % (len(rows), dup, net))
    else:
        print("  结算闭合：未计入 %d − 重复计 %d ＝ 净差 %d ✅" % (len(rows), dup, net))
    if fails:
        print("-" * 72)
        for msg in fails:
            print("  [FAIL] %s" % msg)
    other = cat["other"]
    if other:
        print("  ⚠ other %d 条须人工裁（逐条见 %s）"
              % (other, csv_path or "未给 --csv，故未落盘"))
        if fail_on_other:
            fails.append("other %d 条（--fail-on-other）" % other)
    print("=" * 72)
    return 1 if fails else 0


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
    """双方同时具备 pk／id／key 三候选；pk 与 id 两侧集合相等。

    未给 --key-field 时应自动采用 pk（或 id）并 PASS，而非因多候选直接 FAIL。
    """
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


def _mutate_key_all_mismatch(shards, judg):
    """双方同含 pk／id／key 三候选，但三字段两侧集合两两皆不等。

    未给 --key-field 时应 FAIL，并列出各字段缺／多差异计数。
    """
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
            json.dumps(dict(
                r,
                key="host-a|%d|05-卷册大纲/x.md" % (int(r["key"].split("|")[1]) + 500),
                pk=int(r["key"].split("|")[1]) + 100,
                id=2000 + int(r["key"].split("|")[1])), ensure_ascii=False)
            for r in jrecs) + "\n", encoding="utf-8")
    a = [json.loads(l) for l in (shards / _SHARD_NAME).read_text(
        encoding="utf-8").splitlines() if l.strip()]
    b = [json.loads(l) for l in (judg / _SHARD_NAME).read_text(
        encoding="utf-8").splitlines() if l.strip()]
    for rec in a + b:
        assert {"pk", "id", "key"} <= set(rec), "回读：全不等夹具未落盘"
    for f in KEY_PRIORITY:
        assert {r[f] for r in a} != {r[f] for r in b}, \
            "回读：全不等夹具字段“%s”竟两侧相等" % f


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


def _write_reconcile_fixture(root: pathlib.Path):
    """造台账对账夹具：六条 key 覆盖四类差异 ＋ 一处宿主内重复锚点（重复计 1）。"""
    ledger = root / "ledger"
    beacon = root / "beacon"
    ledger.mkdir(parents=True, exist_ok=True)
    beacon.mkdir(parents=True, exist_ok=True)
    host = "05-卷册大纲/f1_host.md"
    other = "05-卷册大纲/unclaimed_host.md"
    base = [{"key": "db1|1|" + host, "判定": "keep", "批次": "b01"},
            {"key": "db1|9|" + host, "判定": "remap-removed", "批次": "b02"},
            {"key": "NOTAKEY", "判定": "存疑", "批次": "b03"}]
    f1 = [{"key": "db1|2|" + host, "判定": "fix-text", "批次": "f1b01"},
          {"key": "dbX|7|" + other, "判定": "keep", "批次": "f1b01"},
          {"key": "MAIL_INSIGHT|m1|" + host, "判定": "keep", "批次": "f1b01"}]
    for name, recs in (("processed.jsonl", base), ("processed_f1.jsonl", f1),
                       ("processed_f2.jsonl", []), ("processed_f3.jsonl", []),
                       ("processed_f4.jsonl", [])):
        (ledger / name).write_text(
            "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in recs), encoding="utf-8")
    (beacon / "claims_F1.txt").write_text(host + "\n", encoding="utf-8")
    for g in ("F2", "F3", "F4"):
        (beacon / ("claims_%s.txt" % g)).write_text("", encoding="utf-8")
    (beacon / "claims_UNCLAIMED.txt").write_text("", encoding="utf-8")
    beacon_obj = {"progress": {"F1": {"done": 3}, "F2": {"done": 0},
                               "F3": {"done": 0}, "F4": {"done": 0}},
                  "totals": {"done": 6, "pending": 0, "anchors_total": 3}}
    (beacon / "beacon.json").write_text(
        json.dumps(beacon_obj, ensure_ascii=False, indent=1), encoding="utf-8")
    # 锚点清单：db1|1 与 db1|2 已审；db1|2 在宿主内出现两次 → 浮标重复计 1
    anchors = ["db1|1|" + host, "db1|2|" + host, "db1|2|" + host]
    (root / "anchors.json").write_text(
        json.dumps(anchors, ensure_ascii=False), encoding="utf-8")
    return ledger, beacon, root / "anchors.json"


def _run_reconcile(ledger, beacon, anchors, csv_path, extra=()):
    cmd = [sys.executable, str(pathlib.Path(__file__).resolve()),
           "--reconcile-ledger", "--ledger-dir", str(ledger),
           "--beacon-dir", str(beacon), "--anchors", str(anchors),
           "--csv", str(csv_path)] + list(extra)
    proc = subprocess.run(cmd, capture_output=True, text=True,
                          encoding="utf-8", errors="replace")
    return proc.returncode, proc.stdout + proc.stderr


def _expect_reconcile(title, case_dir, failures):
    """一枚夹具：四类各 1 条、重复计 1 条、结算闭合，并逐项校验 CSV。"""
    ledger, beacon, anchors = _write_reconcile_fixture(case_dir)
    csv_path = case_dir / "diff.csv"
    code, out = _run_reconcile(ledger, beacon, anchors, csv_path)
    print("· %-22s 退出码 %d" % (title, code))
    if code != 0:
        failures.append("%s 退出码 %d≠0（%s）" % (title, code, out.strip()[-200:]))
    want = {"mail-insight-invisible": 1, "baseline-unassigned": 1,
            "orphan-key": 1, "other": 1}
    for category, n in want.items():
        if not re.search(r"\[\s*%s\s*\]\s+%d 条" % (re.escape(category), n), out):
            failures.append("%s 未命中类别 %s（判据失效或计数≠%d）"
                            % (title, category, n))
    if "结算闭合" not in out:
        failures.append("%s 结算未闭合（未计入 − 重复计 ≠ 净差）" % title)
    if not csv_path.is_file():
        failures.append("%s 未落 CSV" % title)
        return code, out, csv_path
    rows = list(csv.reader(csv_path.read_text(encoding="utf-8").splitlines()))
    if rows[0] != list(CSV_HEADER):
        failures.append("%s CSV 表头不符：%s" % (title, rows[0]))
    body = rows[1:]
    if len(body) != 4:
        failures.append("%s CSV 应为 4 行，实为 %d" % (title, len(body)))
    cats = collections.Counter(r[1] for r in body if len(r) > 1)
    for category, n in want.items():
        if cats[category] != n:
            failures.append("%s CSV 类别 %s 计数 %d≠%d"
                            % (title, category, cats[category], n))
    if not all(r[6] for r in body if len(r) > 6):
        failures.append("%s CSV 有证据列为空的行" % title)
    return code, out, csv_path


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
        # pk 与 key 同存且 pk 集合相等：默认按 pk 自动采用并 PASS（注明字段）
        _sh, _j, _c, _m, out = _expect(
            "pk/key 同存自动采用", tmp / "case_07", failures,
            mutate=_mutate_key_ambiguous, ledger=False)
        if "key 字段＝pk" not in out:
            failures.append("pk/key 同存未注明采用字段 pk（自动采用失效）")
        _expect("key 字段显式 pk", tmp / "case_07b", failures,
                mutate=_mutate_key_ambiguous, key_field="pk")
        # 所有候选字段皆不等：必须 FAIL 并列出各字段差异计数
        _sh, _j, _c, _m, out = _expect(
            "候选字段皆不等", tmp / "case_07c", failures,
            mutate=_mutate_key_all_mismatch, ledger=False,
            want_exit=1, want_fail=("S4",))
        if "无一使两侧集合相等" not in out:
            failures.append("候选字段皆不等未列出各字段差异计数")
        # 合成件：默认放行，启用 --reject-synthetic 须 FAIL
        _expect("synthetic 默认放行", tmp / "case_08", failures,
                mutate=_mutate_synthetic)
        _expect("synthetic 拒绝", tmp / "case_08b", failures,
                mutate=_mutate_synthetic, reject_synthetic=True,
                want_exit=1, want_fail=("S7",))
        # 台账对账：四类差异各 1 条 ＋ 宿主内重复锚点 1，结算须闭合且 CSV 逐项对上
        _expect_reconcile("台账对账四类命中", tmp / "rec_01", failures)
        # 负向一：浮标已审与重建不符须 FAIL（不得空转 PASS）
        _l, _b, _a = _write_reconcile_fixture(tmp / "rec_02")
        bj = json.loads((_b / "beacon.json").read_text(encoding="utf-8"))
        bj["progress"]["F1"]["done"] = 99
        (_b / "beacon.json").write_text(json.dumps(bj, ensure_ascii=False), encoding="utf-8")
        code, out = _run_reconcile(_l, _b, _a, tmp / "rec_02" / "d.csv")
        print("· %-22s 退出码 %d" % ("台账对账浮标不符", code))
        if code != 1 or "重建已审" not in out:
            failures.append("台账对账浮标不符未判 FAIL（退出码 %d）" % code)
        # 负向二：--fail-on-other 时 other 非空即 FAIL
        _l2, _b2, _a2 = _write_reconcile_fixture(tmp / "rec_03")
        code, out = _run_reconcile(_l2, _b2, _a2, tmp / "rec_03" / "d.csv",
                                   ("--fail-on-other",))
        print("· %-22s 退出码 %d" % ("台账对账 other 即 FAIL", code))
        if code != 1 or "other" not in out:
            failures.append("--fail-on-other 未判 FAIL（退出码 %d）" % code)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    if failures:
        print("  ❌ 判据非空自检失败：")
        for f in failures:
            print("     - %s" % f)
        return 1
    print("  ✅ 判据非空自检通过：正样本 0 FAIL；缺判读件不得空转／批外件过滤／"
          "pk/key 同存自动采用／候选字段皆不等／synthetic 拒绝五类新夹具与行数不符／"
          "坏 JSON／重复 key 既有夹具均命中；台账对账四类差异＋重复计结算闭合、"
          "浮标不符与 --fail-on-other 双双判红，退出码 0／1 正确")
    return 0


def main():
    ap = argparse.ArgumentParser(description="OAA 批次收口对账门禁（第三十件）")
    ap.add_argument("--shards", metavar="DIR", help="分片目录")
    ap.add_argument("--judgements", metavar="DIR", help="判读目录")
    ap.add_argument("--ledger", metavar="FILE", help="台账 processed_fN.jsonl（可选）")
    ap.add_argument("--batch", metavar="TAG",
                    help="批次标签：按“文件名含 TAG”同时过滤分片与判读件（可选）")
    ap.add_argument("--key-field", choices=KEY_PRIORITY, dest="key_field",
                    help="显式指定 key 字段；不给时逐候选字段试算，"
                         "任一字段两侧集合相等即自动采用")
    ap.add_argument("--reject-synthetic", action="store_true",
                    help="判读行含 pilot-synthetic 或文件名含 pilot 即 FAIL"
                         "（默认关闭，生产收口建议开启）")
    ap.add_argument("--selftest", action="store_true", help="判据非空自检")
    ap.add_argument("--reconcile-ledger", action="store_true", dest="reconcile",
                    help="台账合并集与四组浮标已审逐条对账（TD-012／FR-11）")
    ap.add_argument("--ledger-dir", metavar="DIR",
                    help="台账目录（默认 script/_db_row_mining/audit_outline）")
    ap.add_argument("--beacon-dir", metavar="DIR", help="浮标目录（默认 <台账目录>/beacon）")
    ap.add_argument("--anchors", metavar="FILE",
                    help="锚点清单 JSON（元素形如“库|pk|宿主”，浮标计数当刻）")
    ap.add_argument("--snapshot-rev", metavar="REV",
                    help="以 git 重建该提交下 05-卷册大纲/ 的锚点清单（须与浮标同刻）")
    ap.add_argument("--outline", metavar="DIR",
                    help="现行大纲目录（仅在既无 --anchors 亦无 --snapshot-rev 时使用）")
    ap.add_argument("--csv", metavar="PATH", help="逐条差异落 CSV 的路径")
    ap.add_argument("--fail-on-other", action="store_true",
                    help="other 类非空即判 FAIL（默认只告警，因 other 须人工裁）")
    args = ap.parse_args()

    if args.selftest:
        return cmd_selftest()
    if args.reconcile:
        root = pathlib.Path(__file__).resolve().parents[3]
        ledger_dir = (pathlib.Path(args.ledger_dir) if args.ledger_dir
                      else root / "script" / "_db_row_mining" / "audit_outline")
        beacon_dir = (pathlib.Path(args.beacon_dir) if args.beacon_dir
                      else ledger_dir / "beacon")
        return cmd_reconcile(
            ledger_dir, beacon_dir,
            anchors=pathlib.Path(args.anchors) if args.anchors else None,
            snapshot_rev=args.snapshot_rev,
            outline=pathlib.Path(args.outline) if args.outline else None,
            csv_path=pathlib.Path(args.csv) if args.csv else None,
            fail_on_other=args.fail_on_other)
    if not args.shards or not args.judgements:
        print("用法：audit_oaa_batch.py --shards DIR --judgements DIR "
              "[--ledger FILE] [--batch TAG] [--key-field pk|id|key] "
              "[--reject-synthetic]｜--selftest｜--reconcile-ledger "
              "[--snapshot-rev REV] [--csv PATH]", file=sys.stderr)
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
