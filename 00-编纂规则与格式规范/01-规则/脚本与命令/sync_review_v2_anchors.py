# -*- coding: utf-8 -*-
"""重构2026 加强复核套件**锚点同步器**（固定脚本，2026-09-20 第四十一批立）

**用途**：全卷替换／插卷批次之后，把 `review_v2_full.py` 的**六族锚点**同步到新结构。
原为批次内一次性脚本（`script/_r66/patch_review_v2_41.py`）。提升缘由：该套件**跨批静默失效**
（第二十七批起跨 5 批未同步、第四十一批再次踩到），而它驻 `/script` 未纳版本控制 ——
经主理人 2026-09-20 批准，套件与同步器一并提升为本目录固定脚本。

**同步面（六族）**：
  1. 口径族（标量：卷／章／节、`li`／`ul.sections`／`h3.chapter`／`id`、卷末述评章、章级述评节、
     正章、卷分工注、溯源注／`@@`）
  2. 结构族（`vol-1..vol-N`、`range(1, N+1)`）
  3. G 族 SPEC（**由内容源机械重生成，不手抄**）＋ `_gvol` 计数／卷题参数
  4. OLD 零残留清单（只收「旧本独有」的（旧章号＋旧章题）**对**）
  5. J 族备份件（本批 prebak ＋ git 交叉核验提交号）
  6. 关联族（述评 index 口径行等）

**用法**：
    python sync_review_v2_anchors.py --list
    python sync_review_v2_anchors.py --job r41              # dry-run（只打印，不写盘）
    python sync_review_v2_anchors.py --job r41 --apply      # 写盘

**新增批次**：复制 `review_v2_job_r41.py` 为 `review_v2_job_<name>.py` 并改差异表，
在下方 `JOB_FILES` 登记一行即可（**逻辑不动**）。

**⚠️ 本器为「一次性」同步器（非幂等）**：已同步态再跑会**断言失败**（命中数 0 ≠ 期望）——
这是特性不是缺陷，意在提示「本批已同步」。如需复跑，先从 `<本批改动前提交>` 取回套件再跑。

**🔴 形制陷阱（必读，两次踩过）**：
  · `_gvol` 比对的是**含「第 M 章 」前缀**的章题、**含「M.K 」前缀**的节题 ——
    机械生成器若只取 `^## 第 \\d+ 章 (.+)$` 的 group(1)、或只取节号小数点后的数字，
    **全卷 FAIL 而 detail 却报「逐字一致」**（detail 只显示节题差异）。
  · OLD 清单若收入「新旧同名」项 → **判据自相矛盾必 FAIL**（该题仍在页面）。
  · J 段 prebak 须**每批重建**（`git show <本批改动前提交>:…index.html`），勿沿用上一批文件名。
  · 写盘前**逐条断言命中数**；写盘后必须复跑 `review_v2_full.py` 取 PASS/FAIL 计数。
"""
import importlib.util
import io
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = "D:/librebsd"
SUITE = os.path.join(HERE, "review_v2_full.py")
OUTLINE = "08-核查报告与多轮复核/重构2026/data/outline.txt"

JOB_FILES = {"r41": "review_v2_job_r41.py"}

CN_NUM = {1: "一", 2: "二", 3: "三", 4: "四", 5: "五", 6: "六", 7: "七", 8: "八", 9: "九", 10: "十",
          11: "十一", 12: "十二", 13: "十三", 14: "十四", 15: "十五", 16: "十六", 17: "十七",
          18: "十八", 19: "十九", 20: "二十", 21: "二十一", 22: "二十二", 23: "二十三", 24: "二十四",
          25: "二十五", 26: "二十六", 27: "二十七", 28: "二十八", 29: "二十九", 30: "三十",
          31: "三十一", 32: "三十二", 33: "三十三", 34: "三十四", 35: "三十五", 36: "三十六",
          37: "三十七", 38: "三十八", 39: "三十九", 40: "四十"}


def num_cn(v):
    return CN_NUM[v]


def load_job(name):
    path = os.path.join(HERE, JOB_FILES[name])
    spec = importlib.util.spec_from_file_location("_job_" + name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def read_ref(ref):
    """ref 形如 `<commit>:<path>`（经 git 读，抗并发工作树）或本地路径。"""
    if re.match(r"^[0-9a-f]{7,40}:", ref):
        c, p = ref.split(":", 1)
        out = subprocess.run(["git", "show", "%s:%s" % (c, p)], cwd=ROOT, capture_output=True)
        assert out.returncode == 0, "git show 失败：" + ref
        return out.stdout.decode("utf-8")
    return io.open(ref, encoding="utf-8").read()


def parse(text):
    """→ {volno: [title, [[ch_title, [sec_titles]]]]}"""
    CN = {c: i + 1 for i, c in enumerate("一二三四五六七八九十")}

    def cn2i(s):
        if s == "十":
            return 10
        if s.startswith("十"):
            return 10 + CN.get(s[1:], 0)
        if "十" in s:
            a, b = s.split("十")
            return CN[a] * 10 + (CN.get(b, 0) if b else 0)
        return CN[s]

    out, cur = {}, None
    for l in text.split("\n"):
        m = re.match(r"^# 第([一二三四五六七八九十]+)卷  (.+)$", l)
        if m:
            cur = cn2i(m.group(1))
            out[cur] = [m.group(2), []]
            continue
        m = re.match(r"^## (第 \d+ 章 .+)$", l)
        if m and cur:
            out[cur][1].append([m.group(1), []])
            continue
        m = re.match(r"^- (\d+\.\d+) (.+)$", l)
        if m and cur and out[cur][1]:
            t = m.group(2)
            if "@@" in t:
                t = t[:t.index("@@")]
            out[cur][1][-1][1].append(m.group(1) + " " + t)
    return out


def old_list(v, ov, newvol):
    """零残留清单：只收「旧本独有」的（旧章号＋旧章题）对，新旧同名者不收。"""
    items = []
    if ov[0] != newvol[0]:
        items.append("<h2>第%s卷  %s</h2>" % (num_cn(v), ov[0]))
    newch = {i: c[0] for i, c in enumerate(newvol[1], 1)}
    for i, c in enumerate(ov[1], 1):
        if newch.get(i) != c[0]:
            items.append("第 %d 章 %s" % (i, c[0]))
    return items


def run_job(name, apply=False):
    job = load_job(name)
    txt = io.open(SUITE, encoding="utf-8").read()
    new = parse(io.open(OUTLINE, encoding="utf-8").read())
    old = parse(read_ref(job.OLD_REF))
    log = []

    for o, n, cnt in job.GLOBAL:
        got = txt.count(o)
        assert got == cnt, "[%s] GLOBAL %r 命中 %d（期望 %d）" % (name, o[:56], got, cnt)
        txt = txt.replace(o, n)
        log.append("全局：%s → %s（%d）" % (o[:38], n[:38], cnt))

    if getattr(job, "J_OLD_START", None):
        a, b, newj = job.J_OLD_START, job.J_OLD_END, job.J_NEW
        i, j = txt.index(a), txt.index(b)
        assert i < j, "J 段锚点顺序异常"
        txt = txt[:i] + newj + txt[j + len(b):]
        log.append("J 段重写（备份件换本批／覆盖率阈值重算）")

    for v in getattr(job, "SPEC_REPLACE", []):
        spec = "SPEC%d = %r" % (v, new[v][1])
        txt, k = re.subn(r"^SPEC%d = .*$" % v, lambda m: spec, txt, count=1, flags=re.M)
        assert k == 1, ("SPEC", v)
        log.append("SPEC%d 重写（%d 章 %d 节）"
                   % (v, len(new[v][1]), sum(len(c[1]) for c in new[v][1])))

    for v, tag in getattr(job, "OLD_TAG", {}).items():
        items = old_list(v, old[v], new[v])
        lit = "%s = %r" % (tag, items)
        pat = re.compile(r"^%s = (\[.*?\]|\[.*?\n(?: *'.*\n)*? *\])$" % tag, re.M | re.S)
        txt, k = pat.subn(lambda m: lit, txt, count=1)
        assert k == 1, ("OLD", tag)
        log.append("%s 重写（%d 条）" % (tag, len(items)))

    for tag, (v, nc, ns, title) in getattr(job, "GVOL", {}).items():
        pat = re.compile(r'_gvol\("%s", %d, SPEC%d, \d+, \d+,\s*\n?\s*"[^"]*", (OLD\w+)\)'
                         % (tag, v, v))
        m = pat.search(txt)
        assert m, tag
        rep = '_gvol("%s", %d, SPEC%d, %d, %d,\n      "%s", %s)' % (tag, v, v, nc, ns, title, m.group(1))
        txt = txt[:m.start()] + rep + txt[m.end():]
        log.append("%s 参数：%d 章／%d 节" % (tag, nc, ns))

    ADD = getattr(job, "SPEC_ADD", [])
    if ADD:
        blocks = ["# ── %s──────" % getattr(job, "COMMENT", job.NAME)]
        calls = []
        for tag, v in ADD:
            nv = new[v]
            blocks.append("SPEC%d = %r" % (v, nv[1]))
            ov = getattr(job, "OLDVOL", {}).get(v, v)
            blocks.append("OLD%d = %r" % (v, [] if ov is None else old_list(ov, old[ov], new[v])))
            calls.append('_gvol("%s", %d, SPEC%d, %d, %d,\n      "第%s卷  %s", OLD%d)'
                         % (tag, v, v, len(nv[1]), sum(len(c[1]) for c in nv[1]), num_cn(v), nv[0], v))
        k = txt.index(job.ANCHOR)
        k = txt.index("\n\n", k)
        txt = txt[:k] + "\n" + "\n".join(blocks) + "\n" + "\n".join(calls) + txt[k:]
        log.append("新增 SPEC/OLD/_gvol：卷 " + "／".join(str(v) for _, v in ADD))

    print("\n".join(log))
    if not apply:
        print("（dry-run）—— 加 --apply 写盘")
        return 0
    io.open(SUITE, "w", encoding="utf-8", newline="").write(txt)
    print("已写盘：" + SUITE)
    print("下一步：python review_v2_full.py 复跑，取 PASS/FAIL 计数")
    return 0


def main():
    os.chdir(ROOT)          # 内容源／提交路径均相对仓库根 → 本器与 cwd 无关
    args = sys.argv[1:]
    if "--list" in args or not args:
        print("可用 job：" + "／".join("%s（%s）" % (k, load_job(k).NAME) for k in JOB_FILES))
        return 0
    assert "--job" in args, "须指定 --job <name>"
    name = args[args.index("--job") + 1]
    assert name in JOB_FILES, "未知 job：" + name
    return run_job(name, "--apply" in args)


if __name__ == "__main__":
    sys.exit(main())
