#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""export_catalog_data.py — 目录页数据层派生器（catalog-recon 线，2026-11-21 立）。

**定位**：`05-卷册大纲/目录/data/catalog.json` 的 persons 段自此为
`10-交叉索引/cross_indexes.duckdb.person_bio_research` 全表的**派生投影**；
本器是 persons 段的唯一写者。refs／revs 两段 v1 透传既有值
（refs 真值归位由长线承接后升级 v2 接管，见 98 号文 catalog-recon 条目）。

派生规则：
  - id：p-NNNN 顺序号，按 person_name（casefold）稳定排序分配——旧 catalog 无外部
    id 引用（JS 仅用 length 与遍历），重编号安全。
  - names：{zh: [name_zh], en: [name_en + aliases.values]}（去重、保序）。
  - status：库 alive_status（JSON 串或 'deceased(日期)' 混形）→
    {alive, birth, death, note}；「在世/在世待核」→ alive=true（待核语义在 note 披露）。
  - volume：库 vol_ch 原样（None→""）。旧编号语义（'346' 式）为已知漂移，长线清理。
  - affiliations：分号拆数组；role/priority 原样。
  - Corbató 等同人由库行唯一承载（catalog 旧 p-NNNN 不迁移），Loconti 幻觉人物
    （120 号文定谳）不在库即自然出清——两例为 catalog-recon 对账结论。

用法：
  python export_catalog_data.py            # 派生写盘（写前 --check 级预检）
  python export_catalog_data.py --check    # 只比对不写：与盘上 catalog.json 的
                                           # persons 段一致性（0 差异 exit 0）
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="只比对 persons 段，不写盘")
    args = ap.parse_args()

    old = json.loads(CATALOG.read_text(encoding="utf-8"))
    new_persons = derive_persons()

    if args.check:
        same = old.get("persons") == new_persons
        if same:
            print("catalog.json persons 段与库派生一致（逐字节 JSON 相等）")
            return 0
        op, np_ = len(old.get("persons", [])), len(new_persons)
        print(f"persons 段漂移：盘上 {op} 行 vs 库派生 {np_} 行（跑 export_catalog_data.py 重派生）")
        return 1

    old["persons"] = new_persons
    old["version"] = date.today().isoformat()
    CATALOG.write_text(
        json.dumps(old, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8", newline="\n")
    print(f"catalog.json persons 段已派生：{len(new_persons)} 行（真值=person_bio_research）")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
