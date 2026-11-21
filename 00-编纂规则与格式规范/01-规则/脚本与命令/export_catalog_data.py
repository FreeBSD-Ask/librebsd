#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""export_catalog_data.py — 目录页数据层派生器（catalog-recon 线，2026-11-21 立；v2 同日）。

**定位**：`05-卷册大纲/目录/data/catalog.json` 两段为派生投影，本器为唯一写者：
  - **persons 段**：真值＝`10-交叉索引/cross_indexes.duckdb.person_bio_research` 全表
    （plink 按树内人名动态触发，任何人名都可能消费——全量投影）。
  - **refs 段（v2）**：键集＝内容层 `data/outline.txt` 注文 `ref N` 显式引用集
    （页面渲染只消费这些编号——旧手工池 5 537 条死键剔除；真值全集＝
    `04-现代研究文献/historical_claims.duckdb.raw_source` 的 `SRC-ref:` 行，6 483 行）。
    著录串链：catalog 旧串 → 残缺者查 references_fulltext.bibliography_entry 修复
    （L1，实物 sha256 在库）→ 仍残缺保留原串并打印待核披露。
  - **revs 段**：目录页自身版本史，透传（不派生）。

派生规则（persons）：
  - id：p-NNNN 顺序号，按 person_name（casefold）稳定排序分配——无外部 id 引用。
  - names：{zh: [name_zh], en: [name_en + aliases.values]}（去重、保序）。
  - status：库 alive_status（JSON 串或 'deceased(日期)' 混形）→
    {alive, birth, death, note}；「在世/在世待核」→ alive=true（待核语义在 note 披露）。
  - volume：库 vol_ch 原样（None→""）。'346' 式旧树挂靠位语义为已知漂移，
    现行卷映射属内容裁决，不在本器机械转换（不臆造）。
  - affiliations：混形拆数组；role/priority 原样；别名净化剔邮箱与内部标识串
    （与 DATA 门禁判据 2／3 同口径）。
  - 同人由库行唯一承载；幻觉人物（120 号文定谳）不在库即自然出清。

用法：
  python export_catalog_data.py            # 派生写盘
  python export_catalog_data.py --check    # 只比对 persons／refs 段（0 差异 exit 0）
退出码：0 一致／1 有差异或错误（供 DATA 门禁与批后自检调用）。
"""
import argparse
import io
import json
import re
import sys
from datetime import date
from pathlib import Path

import duckdb

# 注意：勿在模块顶层包装 sys.stdout（本模块会被 audit_data_integrity.py
# importlib 动态加载——顶层包装会使宿主的 stdout 包装器被回收而关闭共享缓冲区，
# 见 AGENTS.md「勿用 io.TextIOWrapper 包装」）。主入口内 reconfigure 足够。

ROOT = Path(__file__).resolve().parents[3]
CATALOG = ROOT / "05-卷册大纲" / "目录" / "data" / "catalog.json"
DB = ROOT / "10-交叉索引" / "cross_indexes.duckdb"


def parse_alive(val):
    """库 alive_status 混形 → catalog {alive,birth,death,note}。"""
    if not val:
        return {"alive": None, "birth": None, "death": None, "note": None}
    s = str(val).strip()
    if s.startswith("{"):
        try:
            d = json.loads(s)
            st = d.get("status") or ""
            return {"alive": True if st.startswith("在世") else (False if st == "已故" else None),
                    "birth": d.get("birth") or None, "death": d.get("death") or None,
                    "note": d.get("note") or None}
        except json.JSONDecodeError:
            pass
    m = re.match(r"^(deceased|died)\((.+?)\)$", s, re.I)
    if m:
        return {"alive": False, "birth": None, "death": m.group(2), "note": None}
    return {"alive": None, "birth": None, "death": None, "note": None}


def split_affil(val):
    """库 affiliations 混形（JSON 数组串／分号分隔／'None' 字面）→ 数组。"""
    s = (val or "").strip()
    if not s or s == "None":
        return []
    if s.startswith("["):
        try:
            d = json.loads(s)
            if isinstance(d, list):
                return [str(x).strip() for x in d if str(x).strip() and str(x) != "None"]
        except json.JSONDecodeError:
            pass
    return [t.strip() for t in re.split(r"[;；]", s) if t.strip() and t.strip() != "None"]


def clean_name(v):
    """别名净化：剔邮箱残片与内部标识串（DATA 门禁判据 2／3 同口径）。"""
    v = (v or "").strip()
    if not v or "@" in v or len(v) <= 1:
        return None
    if re.match(r"^(person_id_(legacy|new):|freebsd_account|openbsd_account|netbsd_account|dragonflybsd_account:)", v):
        return None
    return v


def derive_persons():
    con = duckdb.connect(str(DB), read_only=True)
    rows = con.execute(
        "select person_id, person_name, coalesce(name_en,''), coalesce(name_zh,''), "
        "coalesce(aliases,''), coalesce(role,''), coalesce(priority,'P2'), vol_ch, "
        "alive_status, coalesce(affiliations,'') "
        "from person_bio_research order by lower(person_name), person_id"
    ).fetchall()
    con.close()

    persons = []
    for i, (pid, pname, en, zh, al, role, prio, vol_ch, alive_st, affil) in enumerate(rows, 1):
        zh_list = [t.strip() for t in re.split(r"[;；]", zh) if t.strip()]
        en_list = [en.strip()] if en.strip() else []
        if al.strip():
            try:
                for a in json.loads(al):
                    v = clean_name(str(a.get("value", "")))
                    if v:
                        en_list.append(v) if re.match(r"^[\x00-\x7F]", v) else zh_list.append(v)
            except json.JSONDecodeError:
                pass
        # 去重保序
        zh_list = list(dict.fromkeys(zh_list))
        en_list = list(dict.fromkeys(en_list))
        st = parse_alive(alive_st)
        persons.append({
            "id": f"p-{i:04d}",
            "names": {"zh": zh_list, "en": en_list},
            "role": role,
            "priority": prio,
            "volume": str(vol_ch) if vol_ch is not None else "",
            "status": {"alive": st["alive"], "birth": st["birth"], "death": st["death"], "note": st["note"]},
            "affiliations": split_affil(affil),
        })
    return persons


def _broken_bib(s):
    """著录残缺判据：<25 字符，或无 GB/T 类型标且 <40 字符。"""
    if len(s) < 25:
        return True
    return (not re.search(r"\[[A-Z]{1,2}(/OL)?\]", s)) and len(s) < 40


def cited_ref_ids():
    """目录页注文的 ref N 显式引用集——真值源＝内容层 data/outline.txt（装配前源）。"""
    outline = ROOT / "05-卷册大纲" / "目录" / "data" / "outline.txt"
    text = outline.read_text(encoding="utf-8")
    return {int(m.group(1)) for m in re.finditer(r"\bref\s?(\d{1,5})", text)}


def derive_refs():
    """refs 段 v2（catalog-recon 补遗 2026-11-21）：按注文引用集裁剪的投影。

    键集＝outline.txt 注文 `ref N` 显式引用集（页面渲染只消费这些编号；
    旧手工池 5 537 条死键剔除，真值全集＝raw_source SRC-ref 6 483 行）。
    著录串链：catalog 旧串 → 残缺者查 references_fulltext.bibliography_entry
    修复（L1，实物 sha256 在库）→ 仍残缺保留原串（待核，批记披露）。
    """
    old_refs = json.loads(CATALOG.read_text(encoding="utf-8")).get("refs") or {}
    ids = sorted(cited_ref_ids())
    out = {}
    unfixed = []
    ft = duckdb.connect(str(ROOT / "04-现代研究文献" / "05-参考文献全文数据库" / "references_fulltext.duckdb"),
                        read_only=True)
    for i in ids:
        s = str(i)
        cur = old_refs.get(s, "")
        if _broken_bib(cur):
            row = ft.execute(
                'select bibliography_entry from "references" where id = ?', [s]).fetchone()
            cand = str(row[0]).strip() if row and row[0] else ""
            if len(cand) >= 25:
                cur = cand
            if _broken_bib(cur) and s not in unfixed:
                unfixed.append(s)
        out[s] = cur
    ft.close()
    if unfixed:
        print(f"refs 修复披露：{len(unfixed)} 条仍残缺待核（ft 无完整著录）：{unfixed}")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="只比对 persons 与 refs 段，不写盘")
    args = ap.parse_args()

    old = json.loads(CATALOG.read_text(encoding="utf-8"))
    new_persons = derive_persons()
    new_refs = derive_refs()

    if args.check:
        ok_p = old.get("persons") == new_persons
        ok_r = old.get("refs") == new_refs
        if ok_p and ok_r:
            print("catalog.json persons／refs 段与库派生一致（逐字节 JSON 相等）")
            return 0
        if not ok_p:
            print(f"persons 段漂移：盘上 {len(old.get('persons', []))} vs 派生 {len(new_persons)}")
        if not ok_r:
            print(f"refs 段漂移：盘上 {len(old.get('refs', {}))} vs 派生 {len(new_refs)}"
                  "（跑 export_catalog_data.py 重派生）")
        return 1

    old["persons"] = new_persons
    old["refs"] = new_refs
    old["version"] = date.today().isoformat()
    CATALOG.write_text(
        json.dumps(old, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8", newline="\n")
    print(f"catalog.json 已派生：persons {len(new_persons)} 行（真值=person_bio_research）；"
          f"refs {len(new_refs)} 行（引用集投影，真值全集=raw_source SRC-ref）")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
