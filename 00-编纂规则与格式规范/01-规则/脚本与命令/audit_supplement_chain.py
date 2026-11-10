#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""audit_supplement_chain.py — DOC_MINE 补证链门禁（第四十三件，2026-11-10 立）

判据正文：《DOC_MINE补证块格式规则》§八 D1–D5。
  D1  例外台账 status 合法性；supplemented 行须在补证台账有记录且 ref_id／claim_id 非空
  D2  DOC_MINE 块形、抬头↔source_type、等级↔纪律串、CID 在库且 supported、等级与库内真值一致
  D3  raw_source.banned_source=0、provenance_url 非空、namespace=ref:<REF_ID>、ref 在 references
  D4  补证新增 ref 的四键（sha256／isbn_doi／source_url／标题＋第一作者＋年份）在库内唯一，
      或已在 reference_duplicates 登记
  D5  含 DOC_MINE 的小节，ROW_MINE＋DOC_MINE 合计 ≤12 块且 ≤16,797 B

用法：
    python audit_supplement_chain.py --check
    python audit_supplement_chain.py --check --vol V37 --json
    python audit_supplement_chain.py --selftest

退出码：0 全绿（可含 WARN）；1 存在 FAIL；2 依赖缺失或路径不可解析。
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import tempfile
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
OUTLINE = ROOT / "05-卷册大纲"
MAP = OUTLINE / "映射"
CLAIM_DB = ROOT / "04-现代研究文献" / "historical_claims.duckdb"
REF_DB = ROOT / "04-现代研究文献" / "05-参考文献全文数据库" / "references_fulltext.duckdb"

ANCHOR_RE = re.compile(r"^<!-- DOC_MINE: ref(\d+)#(\d+|url) -->$")
ROW_RE = re.compile(r"<!-- ROW_MINE: [A-Za-z0-9_.\-]+\.messages\.\d+ -->")
HEAD_RE = re.compile(
    r"^\*\*(?P<head>[^*]+)\*\*（证据等级：(?P<lv>L[1-5])，"
    r"来源：`historical_claims\.duckdb\.claim\.(?P<cid>CL-RM-\d{6})`；(?P<batch>[^）]+)）$"
)
DISC_RE = re.compile(r"引文按 (L[1-5]) 纪律：")

HEAD_MAP = {
    "official_doc": "官方文档",
    "academic_work": "学术记载",
    "magazine-article": "同时代报道",
    "news": "新闻报道",
    "web_archive": "网页存档",
    "reference_book": "工具书记载",
    "talk_interview": "事后追述",
}
TAIL_MAP = {
    "L5": "以上为直接来源记载",
    "L4": "以上为当事人一手记载",
    "L3": "以上为公开文献记载",
    "L2": "以上为背景性材料或学术二手",
    "L1": "以上为仅具相关性的线索",
}
MAIL_HEADS = ("当事人自述", "二手转述", "背景性材料", "存疑材料")
MAX_BLOCKS = 12
MAX_BYTES = 16797
STATUS_OK = ("open", "supplemented", "unresolvable", "claimed")


def rel(p: Path) -> str:
    try:
        return p.resolve().relative_to(ROOT).as_posix()
    except Exception:
        return str(p)


def read_tsv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def norm_url(u: str) -> str:
    u = (u or "").strip().lower()
    u = re.sub(r"^[a-z]+://", "", u)
    u = u.split("#", 1)[0]
    if "?" in u:
        base, qs = u.split("?", 1)
        keep = [x for x in qs.split("&") if x and not x.startswith("utm_")]
        u = base + ("?" + "&".join(keep) if keep else "")
    return u.rstrip("/")


def norm_title(t: str) -> str:
    t = (t or "").lower()
    return re.sub(r"[\s\W_]+", "", t, flags=re.UNICODE)


def surname(a: str) -> str:
    a = (a or "").strip().lower()
    if not a:
        return ""
    if "," in a:
        return a.split(",", 1)[0].strip()
    return a.split()[-1] if a.split() else ""


def scan_blocks(outline: Path) -> tuple[list[dict], list[str]]:
    blocks: list[dict] = []
    bad: list[str] = []
    for p in sorted(outline.rglob("*.md")):
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            bad.append(f"{rel(p)}: 读取失败 {exc}")
            continue
        if "DOC_MINE" not in text:
            continue
        lines = text.splitlines()
        for i, line in enumerate(lines):
            m = ANCHOR_RE.match(line.strip())
            if not m:
                if "<!-- DOC_MINE" in line:
                    bad.append(f"{rel(p)}:{i + 1}: 锚形不合规 {line.strip()[:80]}")
                continue
            row = {
                "file": rel(p),
                "line": i + 1,
                "ref_id": m.group(1),
                "block": m.group(2),
                "head": None,
                "lv": None,
                "cid": None,
                "batch": None,
                "line4": None,
                "shape_ok": False,
            }
            seg = lines[i + 1:i + 5]
            if len(seg) >= 4 and seg[1].strip() == "" and seg[3].strip() == "":
                hm = HEAD_RE.match(seg[0].strip())
                if hm:
                    row.update(
                        head=hm.group("head").strip(),
                        lv=hm.group("lv"),
                        cid=hm.group("cid"),
                        batch=hm.group("batch").strip(),
                        line4=seg[2],
                        shape_ok=True,
                    )
            blocks.append(row)
    return blocks, bad


def query_claims(db: Path, cids: list[str]) -> dict:
    import duckdb

    out: dict[str, dict] = {}
    if not cids:
        return out
    con = duckdb.connect(str(db), read_only=True)
    try:
        for i in range(0, len(cids), 500):
            chunk = cids[i:i + 500]
            ph = ",".join("?" * len(chunk))
            sql = (
                "select c.claim_id, c.evidence_level, c.status, rs.source_type, "
                "rs.provenance_url, rs.banned_source, rs.namespace, rs.source_id, rs.local_pk "
                "from claim c "
                "left join claim_evidence ce on ce.claim_id = c.claim_id "
                "left join evidence e on e.evidence_id = ce.evidence_id "
                "left join raw_source rs on rs.source_id = e.source_id "
                f"where c.claim_id in ({ph})"
            )
            for r in con.execute(sql, chunk).fetchall():
                out.setdefault(r[0], {
                    "claim_id": r[0], "level": r[1], "status": r[2],
                    "source_type": r[3], "url": r[4], "banned": r[5], "namespace": r[6],
                    "source_id": r[7], "local_pk": r[8],
                })
    finally:
        con.close()
    return out


def ref_rows(db: Path, ids: list[str]) -> dict:
    import duckdb

    out: dict[str, dict] = {}
    if not ids:
        return out
    con = duckdb.connect(str(db), read_only=True)
    try:
        for i in range(0, len(ids), 500):
            chunk = ids[i:i + 500]
            ph = ",".join("?" * len(chunk))
            sql = (
                'select id, sha256, isbn_doi, source_url, title, author, year '
                f'from "references" where id in ({ph})'
            )
            for r in con.execute(sql, chunk).fetchall():
                out[str(r[0])] = {
                    "id": str(r[0]), "sha256": r[1] or "", "doi": r[2] or "",
                    "url": r[3] or "", "title": r[4] or "",
                    "author": r[5] or "", "year": r[6] or "",
                }
    finally:
        con.close()
    return out


def dup_pairs(db: Path) -> set[tuple[str, str]]:
    import duckdb

    con = duckdb.connect(str(db), read_only=True)
    try:
        rows = con.execute(
            "select primary_reference_id, duplicate_reference_id from reference_duplicates"
        ).fetchall()
    finally:
        con.close()
    s = set()
    for a, b in rows:
        s.add((str(a), str(b)))
        s.add((str(b), str(a)))
    return s


def check(outline: Path, claim_db: Path, ref_db: Path, vol: str | None) -> list[dict]:
    F: list[dict] = []

    def add(code: str, level: str, msg: str) -> None:
        F.append({"code": code, "level": level, "msg": msg})

    exc_files = sorted((outline / "映射" / "design" / "exceptions").glob("V*.tsv"))
    sup_files = sorted((outline / "映射" / "design" / "supplement").glob("V*.tsv"))
    if vol:
        exc_files = [p for p in exc_files if p.stem == vol]
        sup_files = [p for p in sup_files if p.stem == vol]

    sup_index: dict[str, dict] = {}
    for p in sup_files:
        for row in read_tsv(p):
            sid = (row.get("subsection_id") or "").strip()
            if sid:
                sup_index[sid] = row

    total_exc = 0
    for p in exc_files:
        for row in read_tsv(p):
            total_exc += 1
            sid = (row.get("subsection_id") or "").strip()
            st = (row.get("status") or "").strip()
            if st not in STATUS_OK:
                add("D1", "FAIL", f"{p.name}:{sid} status 非法 {st!r}")
                continue
            if st == "supplemented":
                s = sup_index.get(sid)
                if not s:
                    add("D1", "FAIL", f"{p.name}:{sid} 标 supplemented 但补证台账无记录")
                else:
                    if not (s.get("ref_id") or "").strip():
                        add("D1", "FAIL", f"{p.name}:{sid} 补证台账 ref_id 为空")
                    if not (s.get("claim_id") or "").strip():
                        add("D1", "FAIL", f"{p.name}:{sid} 补证台账 claim_id 为空")

    blocks, bad = scan_blocks(outline)
    for b in bad:
        add("D2", "FAIL", b)

    shape_bad = [b for b in blocks if not b["shape_ok"]]
    for b in shape_bad:
        add("D2", "FAIL", f"{b['file']}:{b['line']} 块形不合规（须恰好 5 行且抬头行匹配）")

    live = [b for b in blocks if b["shape_ok"]]
    cids = sorted({b["cid"] for b in live})
    claims = query_claims(claim_db, cids) if cids else {}

    for b in live:
        where = f"{b['file']}:{b['line']}"
        if b["head"] in MAIL_HEADS:
            add("D2", "FAIL", f"{where} 补证块套用邮件抬头 {b['head']}")
            continue
        c = claims.get(b["cid"])
        if not c or c.get("status") is None:
            add("D2", "FAIL", f"{where} CID {b['cid']} 在 claim 库不存在")
            continue
        if (c.get("status") or "") != "supported":
            add("D2", "FAIL", f"{where} CID {b['cid']} status={c.get('status')}（须 supported）")
        if (c.get("level") or "") != b["lv"]:
            add("D2", "FAIL", f"{where} 块头等级 {b['lv']} ≠ 库内 {c.get('level')}")
        want_head = HEAD_MAP.get(c.get("source_type") or "")
        if want_head is None:
            add("D2", "FAIL", f"{where} source_type={c.get('source_type')!r} 不在抬头表内")
        elif want_head != b["head"]:
            add("D2", "FAIL", f"{where} 抬头 {b['head']} ≠ 表定 {want_head}")
        dm = DISC_RE.search(b["line4"] or "")
        if not dm:
            add("D2", "FAIL", f"{where} 第 4 行缺纪律串等级")
        else:
            if dm.group(1) != b["lv"]:
                add("D2", "FAIL", f"{where} 纪律串等级 {dm.group(1)} ≠ 块头 {b['lv']}")
            tail = TAIL_MAP.get(dm.group(1), "")
            if tail and tail not in (b["line4"] or ""):
                add("D2", "FAIL", f"{where} 纪律串中段与等级 {dm.group(1)} 不符")
        if c.get("banned") not in (0, None):
            add("D3", "FAIL", f"{where} CID {b['cid']} 来源 banned_source={c.get('banned')}")
        if not (c.get("url") or "").strip():
            add("D3", "FAIL", f"{where} CID {b['cid']} provenance_url 为空")
        if (c.get("source_id") or "") != f"SRC-ref:{b['ref_id']}":
            add("D3", "FAIL", f"{where} raw_source.source_id={c.get('source_id')!r} 应为 SRC-ref:{b['ref_id']}")
        if (c.get("namespace") or "") != "ref":
            add("D3", "FAIL", f"{where} raw_source.namespace={c.get('namespace')!r} 应为 ref")
        if (c.get("local_pk") or "") != b["ref_id"]:
            add("D3", "FAIL", f"{where} raw_source.local_pk={c.get('local_pk')!r} 应为 {b['ref_id']}")

    ref_ids = sorted({b["ref_id"] for b in live})
    refs = ref_rows(ref_db, ref_ids) if ref_ids else {}
    for rid in ref_ids:
        if rid not in refs:
            add("D3", "FAIL", f"ref{rid} 不在 references 表")

    if refs:
        pairs = dup_pairs(ref_db)
        by_hash: dict[str, list[str]] = {}
        by_doi: dict[str, list[str]] = {}
        by_url: dict[str, list[str]] = {}
        by_tri: dict[str, list[str]] = {}
        all_ids = sorted(refs)
        import duckdb

        con = duckdb.connect(str(ref_db), read_only=True)
        try:
            for r in con.execute(
                'select id, sha256, isbn_doi, source_url, title, author, year from "references"'
            ).fetchall():
                rid = str(r[0])
                h = (r[1] or "").strip().lower()
                d = re.sub(r"^(https?://(dx\.)?doi\.org/|doi:)", "", (r[2] or "").strip().lower())
                u = norm_url(r[3] or "")
                t = f"{norm_title(r[4] or '')}|{surname(r[5] or '')}|{(r[6] or '').strip()}"
                if h:
                    by_hash.setdefault(h, []).append(rid)
                if d:
                    by_doi.setdefault(d, []).append(rid)
                if u:
                    by_url.setdefault(u, []).append(rid)
                if t.strip("|"):
                    by_tri.setdefault(t, []).append(rid)
        finally:
            con.close()

        for rid in all_ids:
            r = refs[rid]
            checks = [
                ("sha256", by_hash.get(r["sha256"].strip().lower(), [])),
                ("isbn_doi", by_doi.get(re.sub(r"^(https?://(dx\.)?doi\.org/|doi:)", "",
                                              r["doi"].strip().lower()), [])),
                ("source_url", by_url.get(norm_url(r["url"]), [])),
                ("三元组", by_tri.get(f"{norm_title(r['title'])}|{surname(r['author'])}|{r['year'].strip()}", [])),
            ]
            for key, ids in checks:
                if len(ids) <= 1:
                    continue
                others = [x for x in ids if x != rid]
                if others and all((rid, o) in pairs for o in others):
                    continue
                add("D4", "FAIL", f"ref{rid} 四键 {key} 与 {','.join(others[:5])} 重合且未在 reference_duplicates 登记")

    per_file: dict[str, dict] = {}
    for p in sorted(outline.rglob("*.md")):
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        nd = len(re.findall(r"<!-- DOC_MINE:", text))
        if not nd:
            continue
        nr = len(ROW_RE.findall(text))
        size = p.stat().st_size
        per_file[rel(p)] = {"doc": nd, "row": nr, "total": nd + nr, "bytes": size}
        if nd + nr > MAX_BLOCKS:
            add("D5", "FAIL", f"{rel(p)} 块数 {nd + nr} > {MAX_BLOCKS}")
        if size > MAX_BYTES:
            add("D5", "FAIL", f"{rel(p)} 字节 {size} > {MAX_BYTES}")

    add("INFO", "INFO",
        f"扫描：例外 {total_exc} 行／补证台账 {len(sup_index)} 行／DOC_MINE 块 {len(blocks)} 个"
        f"（合规 {len(live)}）／含块小节 {len(per_file)} 个")
    return F


# ── 自检 ────────────────────────────────────────────────────────────────
def _mk_claim_db(path: Path, rows: list[tuple]) -> None:
    import duckdb

    con = duckdb.connect(str(path))
    con.execute("create table claim(claim_id varchar, evidence_level varchar, status varchar)")
    con.execute("create table evidence(evidence_id varchar, source_id varchar)")
    con.execute("create table claim_evidence(claim_id varchar, evidence_id varchar)")
    con.execute(
        "create table raw_source(source_id varchar, namespace varchar, source_type varchar, "
        "provenance_url varchar, banned_source integer, local_pk varchar)"
    )
    for cid, lv, st, stype, url, banned, rid in rows:
        con.execute("insert into claim values (?,?,?)", [cid, lv, st])
        con.execute("insert into evidence values (?,?)", [f"E-{cid}", f"SRC-ref:{rid}"])
        con.execute("insert into claim_evidence values (?,?)", [cid, f"E-{cid}"])
        con.execute("insert into raw_source values (?,?,?,?,?,?)",
                    [f"SRC-ref:{rid}", "ref", stype, url, banned, rid])
    con.close()


def _mk_ref_db(path: Path, rows: list[tuple]) -> None:
    import duckdb

    con = duckdb.connect(str(path))
    con.execute(
        'create table "references"(id varchar, sha256 varchar, isbn_doi varchar, '
        "source_url varchar, title varchar, author varchar, year varchar)"
    )
    con.execute("create table reference_duplicates(primary_reference_id varchar, duplicate_reference_id varchar)")
    for r in rows:
        con.execute('insert into "references" values (?,?,?,?,?,?,?)', list(r))
    con.close()


def _block(cid: str, lv: str, head: str, ref: str = "2511", block: str = "3") -> str:
    tail = TAIL_MAP[lv]
    return (
        f"<!-- DOC_MINE: ref{ref}#{block} -->\n"
        f"**{head}**（证据等级：{lv}，来源：`historical_claims.duckdb.claim.{cid}`；2026-11-12 V37 补证批 b003）\n"
        "\n"
        f"1993 年该文档记载了接口的初始形态，可与同期提交记录对照。引文出处：Test Doc. 1993.；"
        f"引文按 {lv} 纪律：{tail}，具体结论仍须回核原文与同期一手材料，不得单独引为定论。\n"
        "\n"
    )


def selftest() -> int:
    tmp = Path(tempfile.mkdtemp(prefix="supchain_"))
    ok = 0
    total = 0

    def run_case(name: str, blocks: str, exc_rows: list[tuple], sup_rows: list[tuple],
                 claim_rows: list[tuple], ref_rows: list[tuple], want: str | None) -> None:
        nonlocal ok, total
        total += 1
        base = tmp / name
        (base / "映射/design/exceptions").mkdir(parents=True, exist_ok=True)
        (base / "映射/design/supplement").mkdir(parents=True, exist_ok=True)
        (base / "第37卷-T/sub").mkdir(parents=True, exist_ok=True)
        with (base / "映射/design/exceptions/V37.tsv").open("w", encoding="utf-8", newline="\n") as fh:
            fh.write("subsection_id\tkind\treason\tproposal\tstatus\tregistered_date\tdate_src\n")
            for r in exc_rows:
                fh.write("\t".join(r) + "\n")
        with (base / "映射/design/supplement/V37.tsv").open("w", encoding="utf-8", newline="\n") as fh:
            fh.write("subsection_id\tref_id\tclaim_id\tstatus\n")
            for r in sup_rows:
                fh.write("\t".join(r) + "\n")
        (base / "第37卷-T/sub/1.1.1-x.md").write_text(blocks, encoding="utf-8", newline="\n")
        cdb, rdb = base / "c.duckdb", base / "r.duckdb"
        _mk_claim_db(cdb, claim_rows)
        _mk_ref_db(rdb, ref_rows)
        fs = check(base, cdb, rdb, None)
        fails = [f for f in fs if f["level"] == "FAIL"]
        hit = [f for f in fails if want and f["code"] == want]
        passed = (not fails) if want is None else bool(hit)
        print(f"[{'PASS' if passed else 'FAIL'}] {name}: FAIL={len(fails)}"
              + ("" if not fails else " → " + "; ".join(f"{f['code']} {f['msg']}" for f in fails[:3])))
        if passed:
            ok += 1

    C = ("CL-RM-000001", "L4", "supported", "official_doc", "https://example.org/a", 0, "2511")
    R = ("2511", "a" * 64, "", "https://example.org/a", "Test Doc", "Doe", "1993")
    exc_ok = [("V37.1.1.1", "corpus_gap", "r", "p", "supplemented", "2026-11-09", "git")]
    sup_ok = [("V37.1.1.1", "2511", "CL-RM-000001", "supplemented")]

    run_case("pos_basic", _block("CL-RM-000001", "L4", "官方文档"), exc_ok, sup_ok, [C], [R], None)
    run_case("neg_level", _block("CL-RM-000001", "L3", "官方文档"), exc_ok, sup_ok, [C], [R], "D2")
    run_case("neg_cid", _block("CL-RM-000999", "L4", "官方文档"), exc_ok, sup_ok, [C], [R], "D2")
    run_case("neg_mailhead", _block("CL-RM-000001", "L4", "当事人自述"), exc_ok, sup_ok, [C], [R], "D2")
    exc_bad = [("V37.1.1.1", "corpus_gap", "r", "p", "supplemented", "2026-11-09", "git")]
    run_case("neg_d1", _block("CL-RM-000001", "L4", "官方文档"), exc_bad, [], [C], [R], "D1")
    R2 = ("2512", "b" * 64, "", "https://example.org/a/", "Test Doc", "Doe", "1993")
    run_case("neg_d4", _block("CL-RM-000001", "L4", "官方文档"), exc_ok, sup_ok, [C], [R, R2], "D4")
    many = "".join(_block("CL-RM-000001", "L4", "官方文档") for _ in range(13))
    run_case("neg_d5", many, exc_ok, sup_ok, [C], [R], "D5")
    Cb = ("CL-RM-000001", "L4", "supported", "official_doc", "https://example.org/a", 1, "2511")
    run_case("neg_d3", _block("CL-RM-000001", "L4", "官方文档"), exc_ok, sup_ok, [Cb], [R], "D3")

    print(f"自检：{ok}/{total} 通过")
    return 0 if ok == total else 1


def main() -> int:
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--vol", default=None)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--outline-root", default=str(OUTLINE))
    ap.add_argument("--claim-db", default=str(CLAIM_DB))
    ap.add_argument("--ref-db", default=str(REF_DB))
    a = ap.parse_args()

    if a.selftest:
        return selftest()
    if not a.check:
        ap.print_help()
        return 2

    outline = Path(a.outline_root)
    claim_db, ref_db = Path(a.claim_db), Path(a.ref_db)
    for p in (outline, claim_db, ref_db):
        if not p.exists():
            print(f"[abort] 路径不存在：{p}")
            return 2
    try:
        import duckdb  # noqa: F401
    except Exception as exc:
        print(f"[abort] 依赖缺失 duckdb：{exc}")
        return 2

    fs = check(outline, claim_db, ref_db, a.vol)
    fails = [f for f in fs if f["level"] == "FAIL"]
    warns = [f for f in fs if f["level"] == "WARN"]
    if a.json:
        print(json.dumps({"fails": fails, "warns": warns,
                          "info": [f for f in fs if f["level"] == "INFO"]},
                         ensure_ascii=False, indent=2))
    else:
        for f in fs:
            print(f"[{f['level']}] {f['code']} {f['msg']}")
        print(f"Summary: {len(fails)} FAIL, {len(warns)} WARN")
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
