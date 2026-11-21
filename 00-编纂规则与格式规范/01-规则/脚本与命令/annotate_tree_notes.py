#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""annotate_tree_notes.py — 目录注文落树器（catalog-recon 补遗线，2026-11-21 立）。

把目录内容层 `目录/data/outline.txt` 承载的三类注文同步落到大纲磁盘树：
  1. 卷自反性声明（`>` 行）＋卷分工注（`!` 行）→ `第{NN}卷-*/00-总览.md`
     （新建卷头文件；AGENTS.md 内容扩展接口本就要求卷头登记；不匹配第三十八件
     D2 的 `M.N.P-*.md` 键模式，双射安全）。
  2. 节级溯源注（节行 `@@〔…〕`）→ 该节全部小节 .md 的 frontmatter 追加
     `section_note: |-`（节注是节级分工边界语义，深化作者应逐小节可见；
     键＝文件名不变，D2 双射安全）。
  3. 小节自有注（小节行 `@@〔…〕`）→ 该 .md frontmatter 追加 `note: |-`。

幂等：frontmatter 已有同键字段即跳过；00-总览.md 已存在即跳过。
第三十八件 D2 安全性：只追加 frontmatter 字段与新建非 `M.N.P-*.md` 文件，
不增删树内小节文件、不改文件名。

用法：
  python annotate_tree_notes.py            # 落树（幂等）
  python annotate_tree_notes.py --dry      # 只报数不写
退出码：0 成功。
"""
import argparse
import io
import re
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = Path(__file__).resolve().parents[3]
OUTLINE = ROOT / "05-卷册大纲" / "目录" / "data" / "outline.txt"
TREE = ROOT / "05-卷册大纲"

NOTE_RE = re.compile(r"@@(.*?)@@")
CN_NUM = str.maketrans("〇零一二三四五六七八九十", "〇零一二三四五六七八九十")


def cn2int(s):
    """卷行中文数字 → int（一至九十九）。"""
    t = s.translate(str.maketrans("〇零一二三四五六七八九", "0O123456789")).replace("O", "")
    if not t:
        return None
    if "十" in s:
        parts = s.split("十")
        tens = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9, "": 1}
        ones = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9, "": 0}
        return tens.get(parts[0], 0) * 10 + ones.get(parts[1] if len(parts) > 1 else "", 0)
    return int(t) if t.isdigit() else None


def extract_note(line):
    """节/小节行的 @@ 注文——前置（@@〔〕@@ 题）与后置（题@@〔〕）两形态通吃：
    提取行内全部 `〔…〕` 完整片段逐字拼接（注文体例＝〔〕包裹，照录）。"""
    if "@@" not in line:
        return ""
    return "".join(re.findall(r"〔[^〕]*〕", line)).strip()


def parse_outline():
    """outline.txt → [{no, title, declare, note, sections:[{no, note, subs:[{no, note}]}]}]"""
    vols, cur = [], None
    for raw in OUTLINE.read_text(encoding="utf-8").splitlines():
        if raw.startswith("# ") and not raw.startswith("#!"):
            m = re.match(r"#\s*第([0-9〇零一二三四五六七八九十]+)卷\s+(.*)", raw)
            if m:
                no = cn2int(m.group(1))
                if no is None:
                    print(f"警告：卷行中文数字无法解析：{raw[:30]}")
                    continue
                cur = {"no": no, "title": m.group(2).strip(), "declare": None, "note": None, "sections": []}
                vols.append(cur)
            continue
        if cur is None:
            continue
        if raw.startswith("> "):
            cur["declare"] = raw[2:].strip()
        elif raw.startswith("! "):
            cur["note"] = raw[2:].strip()
        elif raw.startswith("- "):
            m = re.match(r"-\s*([0-9]+(?:\.[0-9]+)?)\s+(.*)", raw)
            if m:
                cur["sections"].append({"no": m.group(1), "note": extract_note(m.group(2)), "subs": []})
        elif raw.startswith("  - "):
            m = re.match(r"-\s*([0-9]+(?:\.[0-9]+)?)\s+(.*)", raw)
            if m and cur["sections"]:
                cur["sections"][-1]["subs"].append({"no": m.group(1), "note": extract_note(m.group(2))})
    return vols


def vol_dir(no):
    hits = list(TREE.glob(f"第{no:02d}卷-*"))
    return hits[0] if len(hits) == 1 else None


def fm_has_key(text, key):
    """frontmatter 是否已有指定键（行首精确匹配）。"""
    if not (text.startswith("---") and text.count("---") >= 2):
        return True  # 无合法 frontmatter 的文件不动
    fm = text.split("---")[1]
    return re.search(rf"^{key}:", fm, re.M) is not None


def fm_append(text, key, value):
    """frontmatter 末尾追加块标量键。"""
    fm_end = text.index("---", 4)
    block = f"{key}: |-\n" + "".join(f"  {ln}\n" for ln in (value.splitlines() or [""]))
    return text[:fm_end] + block + text[fm_end:]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true", help="只报数不写")
    args = ap.parse_args()

    vols = parse_outline()
    made_ov, ov_skip = 0, 0
    n_sec_note, n_sub_note, sub_files = 0, 0, 0

    for v in vols:
        d = vol_dir(v["no"])
        if d is None:
            print(f"警告：V{v['no']:02d} 树目录未命中")
            continue
        ov = d / "00-总览.md"
        if v["declare"] or v["note"]:
            if ov.exists():
                ov_skip += 1
            elif not args.dry:
                body = [f"# 第{v['no']}卷  {v['title']}", ""]
                if v["declare"]:
                    body += [f"> {v['declare']}", ""]
                if v["note"]:
                    body += [f"**卷分工注**：{v['note']}", ""]
                body += ["---", "", "本文件由 `annotate_tree_notes.py` 从目录内容层同步（自反性声明＋卷分工注；"
                          "方法论规范第 1 条要求自反性声明居卷首），目录页为渲染权威、本文件为树内工作面。", ""]
                ov.write_text("\n".join(body), encoding="utf-8", newline="\n")
                made_ov += 1
            else:
                made_ov += 1

        for sec in v["sections"]:
            sn = sec["note"]
            if not sn:
                for sub in sec["subs"]:
                    if sub["note"]:
                        n_sub_note += 1
                continue
            sec_dir = None
            for ch in d.glob("第*章-*"):
                hit = [p for p in ch.iterdir() if p.is_dir() and p.name.startswith(f"{sec['no']}-")]
                if hit:
                    sec_dir = hit[0]
                    break
            if sec_dir is None:
                print(f"警告：V{v['no']:02d} 节 {sec['no']} 树目录未命中")
                continue
            for sub_md in sec_dir.glob(f"{sec['no']}.[0-9]*-*.md"):
                sub_files += 1
                t = sub_md.read_text(encoding="utf-8")
                if fm_has_key(t, "section_note"):
                    continue
                if not args.dry:
                    sub_md.write_text(fm_append(t, "section_note", sn), encoding="utf-8", newline="\n")
                n_sec_note += 1
            for sub in sec["subs"]:
                if not sub["note"]:
                    continue
                n_sub_note += 1
                hits = list(sec_dir.glob(f"{sub['no']}-*.md"))
                if not hits:
                    continue
                p = hits[0]
                t = p.read_text(encoding="utf-8")
                if fm_has_key(t, "note"):
                    continue
                if not args.dry:
                    p.write_text(fm_append(t, "note", sub["note"]), encoding="utf-8", newline="\n")

    tag = "dry 预检" if args.dry else "落树"
    print(f"{tag}：新建卷总览 {made_ov}（已存在跳过 {ov_skip}）；节注覆盖小节 .md {n_sec_note}；"
          f"小节自有注 {n_sub_note}（命中小节数 {sub_files}）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
