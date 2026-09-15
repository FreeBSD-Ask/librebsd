# -*- coding: utf-8 -*-
"""SUMMARY.md 同步器（重建 `_sync_gitbook_summary.py`，原脚本已缺失）。

**设计要点（经实物核对后确定）**
现行 SUMMARY.md 的**节标题**与磁盘节文件 H1 已**系统性失同步**（数百处：有的为 H1＋正文首段合并的长题、
有的多出 `**` 强调、有的缺节号前缀）。整文件重生成会一次性改写这些标题，属独立的一致性工程。
故本器采用**结构同步**语义：

  - **结构**（卷 / 章 / 条目集合与顺序）以 `05-卷册大纲/` 磁盘实况为唯一真值，完全重算；
  - **标题**对**已在 SUMMARY 中的文件**逐字沿用现行文本（零改写）；**仅对新增文件**取节文件 H1
    （无 H1 则取文件名去 `.md`）；
  - 头部（`# Summary` + 引言引文）与尾部（`<!-- USER-EDIT:开始 -->` … `<!-- USER-EDIT:结束 -->`，
    含第20卷块与读者指引）**逐字保留**。

章内条目顺序（实物核对确定）：`概述.md`(缩进 2) → 节文件 `N.M-*.md`（数值序，缩进 4）→
其他非节 .md（排除清单等；沿用现行相对序，新增者按名称序）→ `index.md`（「本章索引」，恒末，缩进 4）。

用法:
  C:/Python314/python.exe _sync_gitbook_summary.py --check   # 结构差异报告（不写盘）
  C:/Python314/python.exe _sync_gitbook_summary.py --write   # 写盘
"""
import difflib, io, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = r"D:\librebsd"
OUTLINE = os.path.join(ROOT, "05-卷册大纲")
SUM = os.path.join(OUTLINE, "SUMMARY.md")
H2_BODY = "## 正文"
USER_BEGIN = "<!-- USER-EDIT:开始 -->"

PAT_LINK = re.compile(r"^(\s*)- \[(.*?)\]\((.+?)\)\s*$")


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
    except Exception:
        return None
    return None


def vol_no(n):
    m = re.match(r"^第(\d+)卷", n)
    return int(m.group(1)) if m else 10 ** 6


def chap_no(n):
    m = re.match(r"^第(\d+)章", n)
    return int(m.group(1)) if m else 10 ** 6


def sec_key(f):
    """N.M → (M,0) / N.M.K → (M,K)，使 331.9.* 排在 331.10 之前。"""
    m = re.match(r"^(\d+)\.(\d+)(?:\.(\d+))?-", f)
    if not m:
        return (10 ** 9, 10 ** 9)
    return (int(m.group(2)), int(m.group(3) or 0))


def parse_existing(cur):
    """现行 SUMMARY 的 BODY 段 → {相对路径: 标题} 与 {章目录: [条目路径顺序]}。"""
    i_h2 = next(i for i, l in enumerate(cur) if l.strip() == H2_BODY)
    i_user = next(i for i, l in enumerate(cur) if l.strip() == USER_BEGIN)
    titles, order = {}, {}
    cur_chap = None
    for l in cur[i_h2 + 1:i_user]:
        m = PAT_LINK.match(l)
        if not m:
            continue
        ind, title, path = len(m.group(1)), m.group(2), m.group(3)
        p = path[2:] if path.startswith("./") else path
        titles[p] = title
        if ind == 0 and path.startswith("./第") and "/00-总览.md" not in path and "/卷末" not in path:
            vv = p.split("/", 1)[0]
            order.setdefault(vv, []).append(p)
        if ind == 2 and "/概述.md" in path:
            cur_chap = p.rsplit("/", 1)[0]
            order.setdefault(cur_chap, [])
        elif ind == 4 and cur_chap:
            order[cur_chap].append(p)
    return titles, order


def build_body(titles, order, tail_vols):
    out = []
    vols = sorted([d for d in os.listdir(OUTLINE)
                   if os.path.isdir(os.path.join(OUTLINE, d)) and d.startswith("第")], key=vol_no)
    for v in vols:
        vdir = os.path.join(OUTLINE, v)
        if v in tail_vols:
            continue
        vt = titles.get(v + "/00-总览.md") or h1(os.path.join(vdir, "00-总览.md")) or v
        out += ["### " + vt, "", "- [%s](./%s/00-总览.md)" % (vt, v)]
        vroot = sorted([f for f in os.listdir(vdir)
                        if f.endswith(".md") and f != "00-总览.md" and not f.startswith("卷末")
                        and os.path.isfile(os.path.join(vdir, f))])
        prevv = [p.rsplit("/", 1)[-1] for p in order.get(v, [])]
        vroot.sort(key=lambda f: (prevv.index(f) if f in prevv else 10 ** 6, f))
        for f in vroot:
            fp = "%s/%s" % (v, f)
            tt = titles.get(fp) or h1(os.path.join(vdir, f)) or f[:-3]
            out.append("- [%s](./%s)" % (tt, fp))

        out.append("")
        chs = sorted([d for d in os.listdir(vdir)
                      if os.path.isdir(os.path.join(vdir, d)) and re.match(r"^第\d+章", d)], key=chap_no)
        if chs:
            for ci, c in enumerate(chs):
                cdir = os.path.join(vdir, c)
                files = sorted(os.listdir(cdir))
                cp = "%s/%s" % (v, c)
                ct = titles.get(cp + "/概述.md") or h1(os.path.join(cdir, "概述.md")) or c
                out.append("  - [%s](./%s/概述.md)" % (ct, cp))

                secs = sorted([f for f in files if re.match(r"^\d+\.\d+(\.\d+)?-.*\.md$", f)], key=sec_key)
                others = [f for f in files if f.endswith(".md") and f != "概述.md"
                          and f != "index.md" and f not in secs]
                # others：沿用现行相对序，新增者按名称序补后
                prev = [p.rsplit("/", 1)[-1] for p in order.get(cp, [])]
                others.sort(key=lambda f: (prev.index(f) if f in prev else 10 ** 6, f))
                for f in secs + others:
                    fp = "%s/%s" % (cp, f)
                    t = titles.get(fp) or h1(os.path.join(cdir, f)) or f[:-3]
                    out.append("    - [%s](./%s)" % (t, fp))
                if "index.md" in files:
                    t = titles.get(cp + "/index.md") or "本章索引"
                    out.append("    - [%s](./%s/index.md)" % (t, cp))
                if ci != len(chs) - 1:
                    out.append("")
        else:
            for f in sorted(f for f in os.listdir(vdir)
                            if f.endswith(".md") and f != "00-总览.md" and not f.startswith("卷末")):
                fp = "%s/%s" % (v, f)
                t = titles.get(fp) or h1(os.path.join(vdir, f)) or f[:-3]
                out.append("  - [%s](./%s)" % (t, fp))

        if os.path.exists(os.path.join(vdir, "卷末书目述评.md")):
            t = titles.get(v + "/卷末书目述评.md") or "卷末书目述评"
            out += ["", "- [%s](./%s/卷末书目述评.md)" % (t, v)]
        out.append("")
    return out


def main():
    write = "--write" in sys.argv
    cur = io.open(SUM, encoding="utf-8").read().split("\n")
    titles, order = parse_existing(cur)
    i_h2 = next(i for i, l in enumerate(cur) if l.strip() == H2_BODY)
    i_user = next(i for i, l in enumerate(cur) if l.strip() == USER_BEGIN)
    head = cur[:i_h2 + 1] + [""]
    tail = cur[i_user:]
    tail_vols = set()
    for l in tail:
        m = PAT_LINK.match(l)
        if m:
            pth = m.group(3)
            if pth.startswith("./") and pth.endswith("/00-总览.md"):
                tail_vols.add(pth[2:].rsplit("/", 1)[0])
    body = build_body(titles, order, tail_vols)
    new = head + body + [""] + tail

    print("现行 %d 行 / 重生成 %d 行" % (len(cur), len(new)))
    n_vol = sum(1 for l in body if l.startswith("### "))
    n_ch = sum(1 for l in body if re.match(r"^  - \[", l) and "概述.md" in l)
    n_ent = sum(1 for l in body if re.match(r"^    - \[", l))
    print("重生成正文：卷 %d / 章 %d / 章下条目 %d" % (n_vol, n_ch, n_ent))

    if new == cur:
        print("\n结构同步校验：**逐行完全一致（PASS，零改写）**")
        return 0

    d = list(difflib.unified_diff(cur, new, "SUMMARY.md(现行)", "SUMMARY.md(重生成)", lineterm="", n=1))
    adds = sum(1 for l in d if l.startswith("+") and not l.startswith("+++"))
    dels = sum(1 for l in d if l.startswith("-") and not l.startswith("---"))
    print("\n结构同步校验：差异 —— 增 %d 行 / 删 %d 行（diff 块 %d 个）"
          % (adds, dels, sum(1 for l in d if l.startswith("@@"))))
    print("\n差异明细（最多 100 行）：")
    for l in d[:100]:
        print("  " + l[:160])
    if len(d) > 100:
        print("  ...（共 %d 行 diff）" % len(d))

    if write:
        io.open(SUM, "w", encoding="utf-8", newline="\n").write("\n".join(new))
        print("\n[written] %s" % SUM)
    else:
        print("\n[dry] 未写盘；加 --write 落盘")
    return 1


if __name__ == "__main__":
    sys.exit(main())
