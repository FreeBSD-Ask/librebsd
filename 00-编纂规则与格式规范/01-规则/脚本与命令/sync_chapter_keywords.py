# -*- coding: utf-8 -*-
"""章节检索关键词库 `05-卷册大纲/chapter_keywords.json` 同步器（固定脚本）。

**职责**：SUMMARY.md 每次更新时，同批把章节关键词库对齐到 `05-卷册大纲/` 磁盘实况。
库结构（键＝全局章号，字符串）：

    {"1": {"volume": "第01卷-unix的起源", "title": "unix前史",
           "subs": ["1.1 ..."], "keywords": ["multics", "ctss", ...]}, ...}

**语义**
  - `volume` / `title` / `subs` 一律由磁盘重算（章目录、`概述.md` H1、节文件 H1）；
  - `keywords` **只增不删**：既有条目原样保留；新增章按其 H1 与节题中的拉丁词元派生
    临时词表（≤8），随后须由并行子代理逐章读 `概述.md` 增补并复核；
  - 归一化沿用旧库惯例：小写、去空白与标点，仅留中日韩文字与字母数字（`subs` 保留
    `N.M` 编号前缀）；
  - 无章号结构的卷（第 20 卷：卷根直挂 00–219 条目，无 `第N章` 目录）不入本库。

**用法**
  C:/Python314/python.exe sync_chapter_keywords.py --check   # 漂移报告（不写盘，有漂移 exit 1）
  C:/Python314/python.exe sync_chapter_keywords.py --write   # 写盘
  C:/Python314/python.exe sync_chapter_keywords.py --list    # 打印当前统计
"""
import io
import json
import os
import re
import shutil
import sys
import tempfile

sys.stdout.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
OUT = os.path.join(ROOT, "05-卷册大纲")
TARGET = os.path.join(OUT, "chapter_keywords.json")

KEEP = re.compile(r"[^0-9a-z\u3400-\u4dbf\u4e00-\u9fff]+")
VOLNO = re.compile(r"^第(\d+)卷")
CHNO = re.compile(r"^第(\d+)章")
SECFILE = re.compile(r"^(\d+\.\d+(?:\.\d+)?)-.*\.md$")
LATIN = re.compile(r"[A-Za-z][A-Za-z0-9.+-]{1,}")
TERM = re.compile(r"^[a-z0-9][a-z0-9._+-]{1,39}$")
STOP = set("""bsd unix os history computer software system technology project community
development open source free internet the and for with from into over under about
its his her their this that these those new old early late modern""".split())


def norm(s):
    return KEEP.sub("", (s or "").lower())


def h1(path):
    """取首个 `# ` 标题（跳过 YAML frontmatter 与空行）。"""
    try:
        in_fm = False
        for ln in io.open(path, encoding="utf-8"):
            s = ln.rstrip("\n")
            if s.strip() == "---":
                in_fm = not in_fm
                continue
            if in_fm or not s.strip():
                continue
            if s.startswith("# "):
                return s[2:].strip()
            if s.startswith("#"):
                continue
            return None
    except OSError:
        return None
    return None


def derive(h1_text, ch, subs):
    """新增章的临时词表：H1 与节题中的拉丁词元（≤8）。"""
    pool = [h1_text or ""] + list(subs)
    out, seen = [], set()
    for text in pool:
        for tok in LATIN.findall(text):
            t = tok.lower().strip(".-+")
            if len(t) < 2 or t in STOP or t in seen or not TERM.match(t):
                continue
            seen.add(t)
            out.append(t)
            if len(out) >= 8:
                return sorted(out)
    return sorted(out)


def scan(out_dir=None):
    out_dir = out_dir or OUT
    vols = sorted(
        [d for d in os.listdir(out_dir)
         if os.path.isdir(os.path.join(out_dir, d)) and VOLNO.match(d)],
        key=lambda x: int(VOLNO.match(x).group(1)))
    rows = []
    for v in vols:
        vdir = os.path.join(out_dir, v)
        chs = sorted(
            [d for d in os.listdir(vdir)
             if os.path.isdir(os.path.join(vdir, d)) and CHNO.match(d)],
            key=lambda x: int(CHNO.match(x).group(1)))
        for c in chs:
            cdir = os.path.join(vdir, c)
            gn = int(CHNO.match(c).group(1))
            files = sorted(os.listdir(cdir))
            secs = [f for f in files if SECFILE.match(f)]
            secs.sort(key=lambda f: tuple(int(x) for x in re.match(r"^(\d+)\.(\d+)", f).groups()))
            sub_rows = []
            for f in secs:
                num = re.match(r"^(\d+\.\d+(?:\.\d+)?)-", f).group(1)
                t = h1(os.path.join(cdir, f)) or f[:-3]
                t = re.sub(r"^%s\s*" % re.escape(num), "", t)
                sub_rows.append(("%s %s" % (num, norm(t))).strip())
            ch_h1 = h1(os.path.join(cdir, "概述.md")) or c
            title = re.sub(r"^第\s*%d\s*章\s*" % gn, "", ch_h1).strip()
            rows.append({
                "ch": gn,
                "volume": v,
                "title": norm(title),
                "subs": sub_rows,
                "h1": ch_h1,
            })
    return rows


def load_current(path=None):
    path = path or TARGET
    if not os.path.exists(path):
        return {}
    try:
        return json.load(io.open(path, encoding="utf-8"))
    except Exception as exc:  # 损坏即停，禁覆盖
        print("FATAL 现有 chapter_keywords.json 无法解析：%s" % exc)
        raise SystemExit(2)


def build(rows, cur):
    out = {}
    derived = []
    for r in rows:
        key = str(r["ch"])
        prev = cur.get(key) or {}
        kws = [k for k in (prev.get("keywords") or []) if TERM.match(str(k))]
        if not kws:
            kws = derive(r["h1"], r["ch"], r["subs"])
            derived.append(r["ch"])
        out[key] = {
            "volume": r["volume"],
            "title": r["title"],
            "subs": r["subs"],
            "keywords": kws,
        }
    return out, derived


def diff(cur, new):
    d = []
    for key in sorted(new, key=int):
        if key not in cur:
            d.append("新增章 %s（%s）" % (key, new[key]["title"]))
            continue
        old = cur[key]
        if old.get("volume") != new[key]["volume"]:
            d.append("章 %s 卷属 %r → %r" % (key, old.get("volume"), new[key]["volume"]))
        if old.get("title") != new[key]["title"]:
            d.append("章 %s 题面 %r → %r" % (key, old.get("title"), new[key]["title"]))
        if old.get("subs") != new[key]["subs"]:
            o, n = old.get("subs") or [], new[key]["subs"]
            gone = [x for x in o if x not in n]
            add = [x for x in n if x not in o]
            d.append("章 %s 节表变化（+%d/−%d）%s%s" % (
                key, len(add), len(gone),
                "；新增 " + "、".join(add[:3]) if add else "",
                "；移除 " + "、".join(gone[:3]) if gone else ""))
        if old.get("keywords") != new[key]["keywords"]:
            d.append("章 %s 词表漂移（%d → %d）" % (
                key, len(old.get("keywords") or []), len(new[key]["keywords"])))
    for key in sorted(set(cur) - set(new), key=int):
        d.append("消失章 %s（库中存在、磁盘已无）" % key)
    return d


def selftest():
    """负向夹具：题面改动、新增章、消失章三类漂移必须被 diff 捕获。"""
    tmp = tempfile.mkdtemp(prefix="kwselftest_")
    try:
        c1 = os.path.join(tmp, "第01卷-t", "第1章-a")
        os.makedirs(c1)
        io.open(os.path.join(c1, "概述.md"), "w", encoding="utf-8", newline="\n").write(
            "# 第 1 章 Alpha 史\n")
        io.open(os.path.join(c1, "1.1-beta.md"), "w", encoding="utf-8", newline="\n").write(
            "# 1.1 Beta 起源\n")
        rows = scan(tmp)
        base, derived = build(rows, {})
        assert len(base) == 1 and base["1"]["subs"] == ["1.1 beta起源"], base
        assert "alpha" in base["1"]["keywords"] and "beta" in base["1"]["keywords"], derived

        io.open(os.path.join(c1, "概述.md"), "w", encoding="utf-8", newline="\n").write(
            "# 第 1 章 Alpha 新史\n")
        d1 = diff(base, build(scan(tmp), base)[0])
        assert any("题面" in x for x in d1), d1

        c2 = os.path.join(tmp, "第01卷-t", "第2章-b")
        os.makedirs(c2)
        io.open(os.path.join(c2, "概述.md"), "w", encoding="utf-8", newline="\n").write(
            "# 第 2 章 Gamma\n")
        d2 = diff(base, build(scan(tmp), base)[0])
        assert any("新增章" in x for x in d2), d2

        base2, _ = build(scan(tmp), base)
        assert "2" in base2, base2
        shutil.rmtree(c2)
        d3 = diff(base2, build(scan(tmp), base2)[0])
        assert any("消失章" in x for x in d3), d3
        print("selftest: PASS（题面漂移／新增章／消失章三类均被捕获）")
        return 0
    except AssertionError as exc:
        import traceback
        traceback.print_exc()
        print("selftest: FAIL %s" % (exc,))
        return 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    if "--selftest" in sys.argv:
        return selftest()
    write = "--write" in sys.argv
    list_only = "--list" in sys.argv
    rows = scan()
    cur = load_current()
    new, derived = build(rows, cur)

    n_kw = sum(len(v["keywords"]) for v in new.values())
    print("磁盘章数 %d；库内章数 %d；词条合计 %d；卷数 %d"
          % (len(rows), len(cur), n_kw, len(set(v["volume"] for v in new.values()))))
    if derived:
        print("按 H1/节题派生临时词表的章 %d 个：%s" % (
            len(derived), ",".join(str(x) for x in derived[:20]) + ("…" if len(derived) > 20 else "")))
    d = diff(cur, new)
    cur_kw = {k: (v.get("keywords") or []) for k, v in cur.items()}
    new_kw = {k: v["keywords"] for k, v in new.items()}
    structural = [x for x in d if "词表漂移" not in x]

    if list_only:
        return 0
    if not d:
        print("同步校验：PASS（结构逐字段一致，零漂移）")
        return 0
    print("同步校验：差异 %d 项（结构 %d 项）：" % (len(d), len(structural)))
    for line in d[:80]:
        print("  " + line)
    if len(d) > 80:
        print("  …（共 %d 项）" % len(d))
    if write:
        with io.open(TARGET, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(new, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
        print("[written] %s" % TARGET)
        return 0
    print("[dry] 未写盘；加 --write 落盘")
    return 1 if structural else 0


if __name__ == "__main__":
    sys.exit(main())
