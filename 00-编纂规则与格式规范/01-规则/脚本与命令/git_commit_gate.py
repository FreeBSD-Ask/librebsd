#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Git 提交门禁（双阶段统一后端；2026-10-17 立，2026-10-17 ykla 批准扩展，固定脚本）

由两个 hook 薄壳调用（薄壳位于 `.git/hooks/`，不入库，本件为权威实现）：

    .git/hooks/pre-commit   → exec python …/git_commit_gate.py --stage pre-commit
    .git/hooks/commit-msg   → exec python …/git_commit_gate.py --stage commit-msg "$@"

对应 `流程规则.md`「Git 暂存规则（.gitignore 与体积门槛；2026-10-17 立）」。

── pre-commit 阶段（自动改正，永不拒收；2026-10-17 薄壳安装，清理批合入）──
对暂存区中的文档类文件（.md／.txt，排除内容层与逐字保真档案，见 FIX_EXCLUDE_PREFIX）：

  F1  直角引号「」『』 → 弯引号 “”‘’（开闭字符一一映射；围栏代码块与行内代码段内不动）
  F2  不可见字符全口径清理（2026-10-17 ykla 裁定，算法单一来源＝fix_md_invisible.py 的
      norm_body／canon；整文件范围、含围栏与行内代码——与 commit-msg B4 对象面一致）：
      ①Cf 格式符／填充符（U+200B–200F、U+202A–202E、U+2060–206F、U+FEFF、U+00AD、
        U+0601、U+034F 等）一律删除；
      ②Zs 空格类（U+3000、U+00A0、U+202F 等，除 U+0020）一律归一为 1 个半角空格，
        含此类字符的极大空白串合并为 1 个半角空格，行首／行尾整段删除；
      ③U+FFFD 不改正，逐件打印披露（编码损坏标记，处置另案）；
      ④改写前后以 canon 内容指纹断言（去空白与目标字符后逐字相同），不符即回退本件。
      fix_md_invisible 缺失时降级为窄口径（仅删 U+200B/200C/200D/2060/FEFF）并在改动
      说明中标注「降级窄口径」。
  F3  CRLF → LF；剥离 UTF-8 BOM
  另：非 UTF-8 文件整体跳过不改正（旧实现 errors="replace" 会把坏字节写成 U+FFFD 回盘，已废）。

改后写回工作树并 `git add`，打印改动清单；无源文件级语义变化。

── commit-msg 阶段（阻断，除非提交说明含批准标记）──

  G1  新增（A）路径命中 `.gitignore`（`git check-ignore --no-index`）→ 拒；`APPROVED-IGNORED:` 放行
  G2  暂存 blob 单个 > 5 MB（5,242,880 字节）→ 拒；`APPROVED-BIGFILE:` 放行
  B2  根目录新增一级条目不在白名单 → 拒；`APPROVED-BY-OWNER:` 放行
  B3  删除 `12-数据库备份/**` → 拒；`APPROVED-BY-OWNER:` 放行
  B4  文档类文件含全角空格 U+3000 → 拒；`APPROVED-BY-OWNER:` 放行
  B5  暂存路径为旁路备份副本（`.bak`／`.bak-*`／`.bak_*`／`.bak.<数字>`／`.prebak*`／
      `.orig`／`.rej`／`~` 结尾，或任一路径段含 `prebak`）→ 拒，**无放行标记**
      （2026-10-23 用户令：全库禁止旁路备份副本；留痕与回滚唯一靠 Git）
  B6  暂存路径的任一单段文件名 UTF-8 字节 > 255（Linux NAME_MAX）→ 拒；`APPROVED-BY-OWNER:` 放行。
      缘由（2026-10-29 立）：本机 NTFS 按字符计，256 字节的中文名照样能建，但 CI 在 Linux 检出时
      直接 ENAMETOOLONG，门禁根本跑不到——落地门禁 L18 只能事后报，提交口才是唯一能拦的位置。
  H3  暂存 `.md` 含直角引号六码位（U+300C/300D/300E/300F/FF62/FF63）→ 拒；
      `APPROVED-BY-OWNER:` 放行。对象面＝**全部暂存 .md**（含内容层/逐字保真档案与
      代码上下文），与第二十四件 `audit_md_quote_glyphs.py` 的全库 T1 判据同一口径；
      F1 不自动改正代码上下文与内容层（逐字保真），此两类面的残留由本判据兜底阻断——
      pre-commit 自动改正 + commit-msg 阻断由此闭环。
  H1  提交说明质量（2026-10-17 ykla 批准批，无放行标记）：首行非空、≥8 字符、
      非纯数字／标点占位、消息不以 BOM 起始 → 违者拒（改写消息零成本，不设 bypass）

含 `--no-verify` 时 hook 不被 git 调用；绕过须 ykla 显式指示并留痕 changelog。
为什么阻断类放 commit-msg：pre-commit 阶段提交说明尚未定稿，无法核对批准标记。

用法：
  git_commit_gate.py --stage pre-commit            # pre-commit 调用形态（CWD＝仓库根）
  git_commit_gate.py --stage commit-msg <msgpath>  # commit-msg 调用形态
  git_commit_gate.py --selftest                    # 隔离临时仓库全用例自检

退出码：0 放行；1 拒收（stdout 列违规件）；2 依赖缺失或运行错误。
"""
import os
import re
import subprocess
import sys

THRESHOLD = 5242880  # 5 MB
TAG_IGNORED = "APPROVED-IGNORED:"
TAG_BIGFILE = "APPROVED-BIGFILE:"
TAG_OWNER = "APPROVED-BY-OWNER:"

ANGLE_MAP = {"\u300c": "\u201c", "\u300d": "\u201d", "\u300e": "\u2018", "\u300f": "\u2019",
             "\uff62": "\u201c", "\uff63": "\u201d"}
CORNER_ALL = "\u300c\u300d\u300e\u300f\uff62\uff63"  # 与第二十四件 audit_md_quote_glyphs 同一六码位
ZERO_WIDTH = "\u200b\u200c\u200d\u2060\ufeff"
IDEOGRAPHIC_SPACE = "\u3000"

# B5：旁路备份副本（2026-10-23 用户令；全库禁止，无放行标记）
# 变体口径与 .gitignore 封禁段一致：prebak 之外，preback／pre_／pre-／_pre_ 一类
# “写前快照”命名同判（复核发现磁盘存在 .pre_*／.pre-*／.preback* 存量，须同堵入口）。
# 2026-10-29 收窄中缀 pre：仅认后接数字的日期形（`-pre-20261023` 一类）。原写法
# `[._-]pre[-_]` 会把题名内含合法版本号的改名件（实测第37卷 10.10.61 节题 `JDK 1.1.3-pre-v1`）
# 拒在提交口，与第三十六件收窄后口径不一致；判据正文本亦不含中缀 pre 形态。
SIDECAR_NAME_RE = (
    re.compile(r"(?i)\.prebak"),
    re.compile(r"(?i)\.preback"),
    re.compile(r"(?i)\.pre[-_]"),
    re.compile(r"(?i)[._-]pre[-_](?=\d)"),
    re.compile(r"(?i)[._-]bak($|[-_.0-9])"),
    re.compile(r"(?i)\.bak($|[-_.0-9])"),
    re.compile(r"(?i)\.orig($|[0-9])"),
    re.compile(r"(?i)\.rej$"),
    re.compile(r"~$"),
)


def is_sidecar(path):
    low = path.lower()
    if "prebak" in low or "preback" in low:
        return True
    name = low.rsplit("/", 1)[-1]
    return any(p.search(name) for p in SIDECAR_NAME_RE)

# F2 全口径清理的算法单一来源＝fix_md_invisible（同目录固定脚本，清理批执行器）。
# 缺失时降级窄口径（仅 5 码位零宽删除），保提交通道可用。
try:
    from fix_md_invisible import canon as _inv_canon, norm_body as _inv_norm_body
    _INV_CORE = True
except Exception:
    _INV_CORE = False

FIXABLE_EXTS = (".md", ".txt")
# 内容层、逐字保真档案、史料与档案不入自动改正面（逐字保真优先）
FIX_EXCLUDE_PREFIX = (
    "05-卷册大纲/", "02-sacred源材料/", "03-原始史料库/", "12-数据库备份/",
    "05-卷册大纲/目录/data/", "08-核查报告与多轮复核/12-重构大纲书目述评/",
)
ROOT_FILE_WHITELIST = {
    ".autocorrectrc", ".gitattributes", ".gitignore", ".zcodeignore", ".markdownlint.json",
    ".textlintrc", ".textlintrc.json", "LICENSE", "AGENTS.md",
    "favicon.ico", "logo.svg", "README.md",
    # 2026-10-29 补登记：第三方 BSD 家族树参照件，被 01-项目管理/03-架构与技术文档/
    # 07-附录-谱系与术语.md 与 115 号文引用；已在库，列入白名单以免删除后重建被 B2 拦。
    "bsd-family-tree.txt", "bsd-family-tree-zh.txt",
}


def run_git(args, cwd=None):
    return subprocess.run(["git"] + args, capture_output=True, cwd=cwd)


def staged_items():
    """返回 [(状态, 新路径, 旧路径), ...]；R/C 解析双路径，D 保留路径。

    注意 `git diff --cached --name-status -z` 的重命名形态为
    `R100\0旧路径\0新路径\0`：旧实现把旧路径当成结果路径，导致重命名批
    全部落到不存在的路径上（2026-10-21 优化时修正）。
    """
    p = run_git(["diff", "--cached", "--name-status", "-z"])
    if p.returncode != 0:
        return None
    tok = p.stdout.decode("utf-8", errors="surrogateescape").split("\0")
    items, i = [], 0
    while i < len(tok):
        st = tok[i]
        if not st:
            i += 1
            continue
        i += 1
        if st[:1] in ("R", "C"):
            old = tok[i] if i < len(tok) else ""
            new = tok[i + 1] if i + 1 < len(tok) else ""
            i += 2
            items.append((st, new, old))
        else:
            path = tok[i] if i < len(tok) else ""
            i += 1
            items.append((st, path, ""))
    return items



def is_doc_fixable(path):
    return (path.lower().endswith(FIXABLE_EXTS)
            and not path.startswith(FIX_EXCLUDE_PREFIX))


def fix_text(text):
    """返回 (新文本, 改动说明列表)。

    F2（不可见字符清理，2026-10-17 裁定全口径）先于 F1 执行：整文件范围、
    含围栏代码块与行内代码段——与 commit-msg B4 的对象面一致，否则 pre-commit
    漏改而 B4 拒收会互相矛盾。算法单一来源＝fix_md_invisible.norm_body／canon。
    F1（直角引号）仍仅处理围栏代码块与行内代码段之外的文本。
    """
    changes = []
    if text.startswith("﻿"):
        text = text[1:]
        changes.append("剥离 UTF-8 BOM")
    if "\r" in text:
        text = text.replace("\r\n", "\n").replace("\r", "\n")
        changes.append("CRLF/CR → LF")
    if _INV_CORE:
        canon_before = _inv_canon(text)
        out_lines, n_del, n_run = [], 0, 0
        for line in text.split("\n"):
            nb, a, b = _inv_norm_body(line)
            n_del += a
            n_run += b
            out_lines.append(nb)
        cand = "\n".join(out_lines)
        if _inv_canon(cand) == canon_before:
            text = cand
            if n_del:
                changes.append("删除 Cf 格式符/填充符 %d 处" % n_del)
            if n_run:
                changes.append("空格类归一半角空格（合并空白串）%d 处" % n_run)
        else:
            changes.append("F2 内容指纹校验异常，本件跳过清理（已回退）")
    else:
        out_lines, fence, n_zero = [], False, 0
        for line in text.split("\n"):
            if line.lstrip().startswith("```") or line.lstrip().startswith("~~~"):
                fence = not fence
                out_lines.append(line)
                continue
            if fence:
                out_lines.append(line)
                continue
            parts = line.split("`")
            if len(parts) % 2 == 0:  # 行内代码不配对，整行按文本处理（语法本身已坏）
                parts = [line]
            buf = []
            for idx, seg in enumerate(parts):
                if idx % 2 == 1:  # 行内代码段原样保留
                    buf.append(seg)
                    continue
                for ch in ZERO_WIDTH:
                    if ch in seg:
                        n_zero += seg.count(ch)
                        seg = seg.replace(ch, "")
                buf.append(seg)
            out_lines.append("`".join(buf))
        text = "\n".join(out_lines)
        if n_zero:
            changes.append("删除零宽字符 %d 处（降级窄口径）" % n_zero)
    out_lines, fence, n_angle = [], False, 0
    for line in text.split("\n"):
        if line.lstrip().startswith("```") or line.lstrip().startswith("~~~"):
            fence = not fence
            out_lines.append(line)
            continue
        if fence:
            out_lines.append(line)
            continue
        parts = line.split("`")
        if len(parts) % 2 == 0:  # 行内代码不配对，整行按文本处理（语法本身已坏）
            parts = [line]
        buf = []
        for idx, seg in enumerate(parts):
            if idx % 2 == 1:  # 行内代码段原样保留
                buf.append(seg)
                continue
            for k, v in ANGLE_MAP.items():
                if k in seg:
                    n_angle += seg.count(k)
                    seg = seg.replace(k, v)
            buf.append(seg)
        out_lines.append("`".join(buf))
    text = "\n".join(out_lines)
    if n_angle:
        changes.append("直角引号 → 弯引号 %d 处" % n_angle)
    return text, changes


def stage_precommit():
    """自动改正暂存文档类文件；永不拒收。R100 重命名无内容变化，直接跳过。"""
    items = staged_items()
    if items is None:
        print("git_commit_gate：无法读取暂存区（git 失败）", file=sys.stderr)
        return 2
    todo = [(st, path) for st, path, old in items
            if st != "D" and not st.startswith("R100") and is_doc_fixable(path)]
    print("[gate] pre-commit：暂存 %d 项，文档候选 %d 项" % (len(items), len(todo)), flush=True)
    touched = []
    for idx, (st, path) in enumerate(todo, 1):
        wt = os.path.join(os.getcwd(), path)
        if os.path.isfile(wt):
            raw = open(wt, "rb").read()
            if b"\0" not in raw[:8000]:
                try:
                    text = raw.decode("utf-8")
                except UnicodeDecodeError:
                    print("git_commit_gate 跳过（非 UTF-8，不改正）：%s" % path, flush=True)
                    text = None
                if text is not None:
                    if "\ufffd" in text:
                        print("git_commit_gate 披露（含 U+FFFD 替换字符，不改正、另行报告）：%s" % path, flush=True)
                    new, changes = fix_text(text)
                    if changes:
                        open(wt, "wb").write(new.encode("utf-8"))
                        touched.append(path)
                        print("git_commit_gate 自动改正：%s（%s）" % (path, "；".join(changes)), flush=True)
        if idx % 500 == 0 or idx == len(todo):
            print("[gate] pre-commit 进度 %d/%d" % (idx, len(todo)), flush=True)
    if touched:
        for i in range(0, len(touched), 500):
            run_git(["add", "--"] + touched[i:i + 500])
        print("git_commit_gate：共自动改正 %d 个文件（已重新暂存），请复核 diff。" % len(touched), flush=True)
    return 0



def _git_batch_check(paths):
    """一次 `git cat-file --batch-check` 取索引 blob 大小；返回 {路径: 字节数}。"""
    res = {}
    for i in range(0, len(paths), 5000):
        chunk = paths[i:i + 5000]
        inp = "".join(":%s\n" % p for p in chunk).encode("utf-8", "surrogateescape")
        p = subprocess.run(["git", "cat-file", "--batch-check"], input=inp,
                           capture_output=True, cwd=os.getcwd())
        for path, line in zip(chunk, p.stdout.split(b"\n")):
            parts = line.split()
            if len(parts) == 3 and parts[1] == b"blob":
                try:
                    res[path] = int(parts[2])
                except ValueError:
                    pass
    return res


def _git_batch_blobs(paths):
    """一次 `git cat-file --batch` 读取索引 blob 内容；按 2,000 件分块控制内存。"""
    res = {}
    for i in range(0, len(paths), 2000):
        chunk = paths[i:i + 2000]
        inp = "".join(":%s\n" % p for p in chunk).encode("utf-8", "surrogateescape")
        proc = subprocess.Popen(["git", "cat-file", "--batch"], stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE, cwd=os.getcwd())
        out, _ = proc.communicate(inp)
        pos = 0
        for path in chunk:
            nl = out.find(b"\n", pos)
            if nl < 0:
                break
            header = out[pos:nl].split()
            pos = nl + 1
            if len(header) == 3 and header[1] == b"blob":
                size = int(header[2])
                res[path] = out[pos:pos + size]
                pos += size + 1
        print("[gate] 内容批读 %d/%d" % (min(i + 2000, len(paths)), len(paths)), flush=True)
    return res


def _batch_ignored(paths):
    """一次 `git check-ignore --stdin -z --no-index` 返回被忽略路径集合。"""
    if not paths:
        return set()
    inp = b"".join(p.encode("utf-8", "surrogateescape") + b"\0" for p in paths)
    p = subprocess.run(["git", "check-ignore", "--stdin", "-z", "--no-index"],
                       input=inp, capture_output=True, cwd=os.getcwd())
    if p.returncode not in (0, 1):
        return set()
    return {x.decode("utf-8", "surrogateescape") for x in p.stdout.split(b"\0") if x}



def check_msg_quality(msg):
    """H1：提交说明质量（2026-10-17 ykla 批准批；无放行标记——改写消息零成本）。

    判据：①消息不以 BOM 起始（PowerShell Set-Content -Encoding UTF8 带 BOM 会污染
    消息首字符——2026-10-17 69ee8a32a6d8 实例）；②首行非空；③首行 ≥4 字符；
    ④首行非纯数字／标点占位（"1/2/！"式整索引提交当日 ≥7 件的教训）。
    """
    bad = []
    if msg.startswith("﻿"):
        bad.append("提交说明以 BOM 起始——将消息文件重写为 UTF-8 无 BOM 再提交"
                   "（PowerShell 用 -Encoding utf8NoBOM 或经 Python 落盘）")
    first = msg.split("\n", 1)[0].strip()
    if not first:
        bad.append("提交说明首行为空")
        return bad
    if len(first) < 4:
        bad.append("首行过短（%d 字符）：%r" % (len(first), first[:40]))
    if re.fullmatch(r"[0-9!\"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~\s]+", first):
        bad.append("首行为纯数字／标点占位（无实质词句）：%r" % first[:40])
    return bad


def stage_commitmsg(msg):
    """阻断检查；批准标记放行。批量读 blob，R100 重命名免检。"""
    items = staged_items()
    if items is None:
        print("git_commit_gate：无法读取暂存区（git 失败）", file=sys.stderr)
        return 2
    adds = [(st, path) for st, path, old in items if st != "D" and not st.startswith("R100")]
    print("[gate] commit-msg：暂存 %d 项，内容待检 %d 项" % (len(items), len(adds)), flush=True)
    bad_ignored, bad_big, bad_root, bad_bakdel, bad_space, bad_corner = [], [], [], [], [], []
    # B5 只拦“新增／修改”旁路副本；D（删除）是整改通道本身，不得阻断（否则遗留副本无法清除）
    bad_sidecar = [path for st, path, old in items if st != "D" and is_sidecar(path)]
    # B6：单段文件名 UTF-8 字节 >255（Linux NAME_MAX）。本机 NTFS 按字符计可建，Linux 检出会
    # ENAMETOOLONG 而使 CI 在「检出」即失败，届时门禁根本跑不到——故必须在提交口拦。
    bad_longname = []
    for st, path, old in items:
        if st == "D":
            continue
        for comp in path.split("/"):
            n = len(comp.encode("utf-8", "surrogateescape"))
            if n > 255:
                bad_longname.append("%s（单段 %d 字节）" % (path, n))
                break
    bad_bakdel = [path for st, path, old in items
                  if st == "D" and path.startswith("12-数据库备份/")]
    new_paths = [path for st, path, old in items
                 if st == "A" and not st.startswith("R100")]
    ignored = _batch_ignored(new_paths)
    bad_ignored = [p for p in new_paths if p in ignored]
    bad_root = [p for p in new_paths if "/" not in p and p not in ROOT_FILE_WHITELIST]
    sizes = _git_batch_check([p for st, p in adds])
    bad_big = ["%s（%d 字节）" % (p, sizes[p]) for st, p in adds
               if sizes.get(p, -1) > THRESHOLD]
    scan = sorted({p for st, p in adds
                   if is_doc_fixable(p) or p.lower().endswith(".md")})
    blobs = _git_batch_blobs(scan)
    for path in scan:
        data = blobs.get(path)
        if data is None:
            continue
        if is_doc_fixable(path) and IDEOGRAPHIC_SPACE.encode("utf-8") in data:
            bad_space.append(path)
        if path.lower().endswith(".md") and any(
                data.count(ch.encode("utf-8")) for ch in CORNER_ALL):
            n = sum(data.count(ch.encode("utf-8")) for ch in CORNER_ALL)
            bad_corner.append("%s（%d 处）" % (path, n))
    errs = []
    if bad_ignored:
        errs.append("G1 被 .gitignore 排除的条目进入了暂存区：\n  " + "\n  ".join(bad_ignored))
    if bad_big:
        errs.append("G2 单个文件超过 5 MB（%d 字节）进入了暂存区：\n  " % THRESHOLD + "\n  ".join(bad_big))
    if bad_root:
        errs.append("B2 根目录新增一级条目不在白名单：\n  " + "\n  ".join(bad_root))
    if bad_bakdel:
        errs.append("B3 暂存区包含 12-数据库备份/ 的删除：\n  " + "\n  ".join(bad_bakdel))
    if bad_space:
        errs.append("B4 文档类文件含全角空格 U+3000（禁 AI 不可见字符）：\n  " + "\n  ".join(bad_space))
    if bad_sidecar:
        errs.append("B5 暂存区含旁路备份副本（全库禁止，无放行标记；回滚靠 Git）：\n  "
                    + "\n  ".join(bad_sidecar))
    if bad_longname:
        errs.append("B6 暂存路径含单段文件名超过 255 字节（Linux NAME_MAX；CI 会在「检出」步骤\n"
                    "   ENAMETOOLONG 失败，门禁跑不到。处置：缩短文件名与 H1 题名，见\n"
                    "   05-卷册大纲/映射/review/longname-fix/ 的 LNF 台账）：\n  "
                    + "\n  ".join(bad_longname))
    if bad_corner:
        errs.append("H3 暂存 .md 含直角引号六码位（第二十四件全库清零不变量的提交期兜底；"
                    "F1 不自动改正代码上下文与内容层/逐字保真面，故此处阻断）：\n  " + "\n  ".join(bad_corner))
    h1 = check_msg_quality(msg)
    if h1:
        errs.append("H1 提交说明不满足质量判据（无放行标记，改写即可）：\n  " + "\n  ".join(h1))
    errs = [e for e in errs if not (
        (e.startswith("G1") and TAG_IGNORED in msg) or
        (e.startswith("G2") and TAG_BIGFILE in msg) or
        (e.startswith(("B2", "B3", "B4", "B6", "H3")) and TAG_OWNER in msg))]
    if errs:
        print("git_commit_gate 拒收（流程规则「Git 暂存规则」；批准标记：%s／%s／%s）：" % (TAG_IGNORED, TAG_BIGFILE, TAG_OWNER), flush=True)
        for e in errs:
            print(e, flush=True)
        return 1
    notes = []
    if bad_ignored:
        notes.append("G1×%d" % len(bad_ignored))
    if bad_big:
        notes.append("G2×%d" % len(bad_big))
    if bad_root or bad_bakdel or bad_space or bad_sidecar:
        notes.append("B×%d" % (len(bad_root) + len(bad_bakdel) + len(bad_space) + len(bad_sidecar)))
    if bad_corner:
        notes.append("H3×%d" % len(bad_corner))
    if notes:
        print("git_commit_gate：检测到批准标记，放行（%s）——请确认 changelog 已留痕批准记录。" % "、".join(notes), flush=True)
    else:
        print("[gate] commit-msg：PASS", flush=True)
    return 0



def selftest():
    """隔离临时仓库全用例：改正区 11（F 改正 6＋链路 2＋排除边界 3）＋阻断 19＝30 用例。"""
    import shutil
    import tempfile

    base = tempfile.mkdtemp(prefix="git_gate_selftest_")
    results = []

    def newrepo(name):
        repo = os.path.join(base, name)
        os.makedirs(repo)
        def g(*a):
            return subprocess.run(["git"] + list(a), cwd=repo, capture_output=True)
        g("init", "-q")
        g("config", "user.email", "gate@test")
        g("config", "user.name", "gate")
        g("config", "commit.gpgsign", "false")  # 全局 commit.gpgsign=true 会让临时仓库签名失败（No secret key）
        return repo, g

    def run_gate(repo, stage, msg=None):
        mp = None
        args = [sys.executable, os.path.abspath(__file__), "--stage", stage]
        if stage == "commit-msg":
            mp = os.path.join(repo, "MSG")
            with open(mp, "w", encoding="utf-8") as f:
                f.write(msg)
            args.append(mp)
        return subprocess.run(args, cwd=repo, capture_output=True)

    def check(name, expect, p, extra=""):
        ok = p.returncode == expect
        results.append((name, expect, p.returncode, ok))
        if not ok:
            print("  ✗ %s（期望 %d 实得 %d）" % (name, expect, p.returncode))
            print("    stdout:", (p.stdout).decode("utf-8", "replace").strip())
            print("    stderr:", (p.stderr).decode("utf-8", "replace").strip()[:300])

    # F1/F2/F3：自动改正（pre-commit 不拒收，文件被改 + re-add）
    repo, g = newrepo("t_fix")
    doc = "标题「甲」与『乙』\n\n```text\n代码内「不动」\n```\n\n行内 `代码「不动」` 结尾\u200b混入\n"
    with open(os.path.join(repo, "doc.md"), "wb") as f:
        f.write(doc.replace("\n", "\r\n").encode("utf-8-sig"))
    g("add", "-A")
    check("F_自动改正放行", 0, run_gate(repo, "pre-commit"))
    fixed = open(os.path.join(repo, "doc.md"), "rb").read().decode("utf-8")
    ok = ("“甲”" in fixed and "‘乙’" in fixed and "代码内「不动」" in fixed
          and "代码「不动」" in fixed and "\u200b" not in fixed and "\r" not in fixed)
    results.append(("F_改正内容正确", 1, 0 if ok else 1, ok))
    if not ok:
        print("  ✗ F_改正内容正确 " + repr(fixed[:160]))

    # F2 全口径：Cf 全删／Zs 归一半角空格／行首行尾删除／围栏行内一并清理／U+FFFD 保留
    repo, g = newrepo("t_f2full")
    src = ("甲\u3000乙\n"
           "a \u3000\u3000 b\n"
           "\u3000行首缩进\n"
           "行尾\u3000\n"
           "Poul\u00adHenning\u200eX\u2060Y\n"
           "```text\n栅内\u3000也清\u3000理\n```\n"
           "行内 `代\u3000码` 尾\n"
           "坏点\ufffd保留\n")
    with open(os.path.join(repo, "f2.md"), "wb") as f:
        f.write(src.encode("utf-8"))
    g("add", "-A")
    check("F2_全口径放行", 0, run_gate(repo, "pre-commit"))
    want = ("甲 乙\n"
            "a b\n"
            "行首缩进\n"
            "行尾\n"
            "PoulHenningXY\n"
            "```text\n栅内 也清 理\n```\n"
            "行内 `代 码` 尾\n"
            "坏点\ufffd保留\n")
    fixed = open(os.path.join(repo, "f2.md"), "rb").read().decode("utf-8")
    ok2 = fixed == want
    results.append(("F2_全口径内容钉死", 1, 0 if ok2 else 1, ok2))
    if not ok2:
        print("  ✗ F2_全口径内容不符 " + repr(fixed))

    # B4 与 pre-commit 链路一致性：自动改正后 B4 不再触发
    repo, g = newrepo("t_b4chain")
    os.makedirs(os.path.join(repo, "docs"))
    with open(os.path.join(repo, "docs", "note.md"), "wb") as f:
        f.write("甲\u3000乙\n".encode("utf-8"))
    g("add", "-A")
    check("B4_链路改正放行", 0, run_gate(repo, "pre-commit"))
    check("B4_链路复检放行", 0, run_gate(repo, "commit-msg", "正常提交说明文本\n"))

    # FIX_EXCLUDE 边界：内容层文件连 B4 也不在对象面（既定契约：fix 与 B4 同为
    # is_doc_fixable；内容层/逐字保真档案两阶段均不涉，存量由 scan/fix 批量工具覆盖）
    repo, g = newrepo("t_b4excl")
    os.makedirs(os.path.join(repo, "05-卷册大纲"))
    with open(os.path.join(repo, "05-卷册大纲", "x.md"), "wb") as f:
        f.write("甲\u3000乙\n".encode("utf-8"))
    g("add", "-A")
    check("EXCL_precommit跳过", 0, run_gate(repo, "pre-commit"))
    kept = open(os.path.join(repo, "05-卷册大纲", "x.md"), "rb").read().decode("utf-8")
    okk = kept == "甲\u3000乙\n"
    results.append(("EXCL_内容原样", 1, 0 if okk else 1, okk))
    if not okk:
        print("  ✗ EXCL_内容被改动 " + repr(kept))
    check("EXCL_提交放行", 0, run_gate(repo, "commit-msg", "正常提交说明文本\n"))

    # G1/G2 既有
    repo, g = newrepo("t_g1")
    with open(os.path.join(repo, ".gitignore"), "w") as f:
        f.write("secret*.txt\n")
    open(os.path.join(repo, "secret.txt"), "wb").write(b"s")
    g("add", "-A")
    g("add", "-f", "secret.txt")
    check("G1_忽略拒", 1, run_gate(repo, "commit-msg", "正常提交说明文本\n"))
    g("reset", "-q", "secret.txt")
    check("G1_撤回后放行", 0, run_gate(repo, "commit-msg", "正常提交说明文本\n"))
    repo, g = newrepo("t_g2")
    os.makedirs(os.path.join(repo, "data"))
    open(os.path.join(repo, "data", "big.bin"), "wb").write(b"x" * (THRESHOLD + 1))
    g("add", "-A")
    check("G2_大文件拒", 1, run_gate(repo, "commit-msg", "正常提交说明文本\n"))
    check("G2_批准放行", 0, run_gate(repo, "commit-msg", TAG_BIGFILE + " m\n"))

    # B2 根目录新条目
    repo, g = newrepo("t_b2")
    open(os.path.join(repo, "mystery.bin"), "wb").write(b"z")
    g("add", "-A")
    check("B2_根目录新条目拒", 1, run_gate(repo, "commit-msg", "正常提交说明文本\n"))
    check("B2_批准放行", 0, run_gate(repo, "commit-msg", TAG_OWNER + " m\n"))
    repo, g = newrepo("t_b2b")
    open(os.path.join(repo, ".autocorrectrc"), "w").write("rules: {}\n")
    g("add", "-A")
    check("B2_白名单放行", 0, run_gate(repo, "commit-msg", "正常提交说明文本\n"))

    # B3 备份删除
    repo, g = newrepo("t_b3")
    os.makedirs(os.path.join(repo, "12-数据库备份", "x"))
    open(os.path.join(repo, "12-数据库备份", "x", "a.gz"), "wb").write(b"b")
    g("add", "-A")
    g("commit", "-q", "-m", "init")
    os.remove(os.path.join(repo, "12-数据库备份", "x", "a.gz"))
    g("add", "-A")
    check("B3_备份删除拒", 1, run_gate(repo, "commit-msg", "正常提交说明文本\n"))
    check("B3_批准放行", 0, run_gate(repo, "commit-msg", TAG_OWNER + " m\n"))

    # B4 全角空格
    repo, g = newrepo("t_b4")
    with open(os.path.join(repo, "note.md"), "w", encoding="utf-8") as f:
        f.write("甲\u3000乙\n")
    g("add", "-A")
    check("B4_全角空格拒", 1, run_gate(repo, "commit-msg", "正常提交说明文本\n"))
    check("B4_批准放行", 0, run_gate(repo, "commit-msg", TAG_OWNER + " m\n"))

    # B6 单段文件名 >255 字节（88 个汉字＝264 字节；NTFS 按字符计可建，Linux 检出会失败）
    repo, g = newrepo("t_b6")
    os.makedirs(os.path.join(repo, "05-卷册大纲"))
    long_name = "长" * 88 + ".md"
    with open(os.path.join(repo, "05-卷册大纲", long_name), "w", encoding="utf-8") as f:
        f.write("# 长名\n")
    g("add", "-A")
    check("B6_超长名拒", 1, run_gate(repo, "commit-msg", "正常提交说明文本\n"))
    check("B6_批准放行", 0, run_gate(repo, "commit-msg", TAG_OWNER + " 有意添加\n"))

    # B5 旁路备份副本（无放行标记）
    repo, g = newrepo("t_b5")
    os.makedirs(os.path.join(repo, "docs"))
    open(os.path.join(repo, "docs", "note.md.prebak-20261023"), "w", encoding="utf-8").write("x\n")
    g("add", "-A")
    check("B5_prebak拒", 1, run_gate(repo, "commit-msg", "正常提交说明文本\n"))
    check("B5_prebak无放行", 1, run_gate(repo, "commit-msg", TAG_OWNER + " 有意添加\n"))
    repo, g = newrepo("t_b5bak")
    open(os.path.join(repo, "note.md.bak_20261023"), "w", encoding="utf-8").write("x\n")
    os.makedirs(os.path.join(repo, "sub"))
    open(os.path.join(repo, "sub", "x.orig"), "w", encoding="utf-8").write("x\n")
    g("add", "-A")
    check("B5_bak与orig拒", 1, run_gate(repo, "commit-msg", "正常提交说明文本\n"))
    # B5 变体命名（写前快照 .pre_*／.preback*／-bak-）同拒
    repo, g = newrepo("t_b5var")
    os.makedirs(os.path.join(repo, "docs"))
    open(os.path.join(repo, "docs", "a.md.pre_b004_20261005"), "w", encoding="utf-8").write("x\n")
    open(os.path.join(repo, "docs", "b.txt.preback-t1"), "w", encoding="utf-8").write("x\n")
    open(os.path.join(repo, "docs", "c.md-bak-20261001"), "w", encoding="utf-8").write("x\n")
    # 中缀 pre 的日期形仍须拒（2026-10-29 收窄后不空转）
    open(os.path.join(repo, "docs", "d.md-foo-pre-20261023.md"), "w", encoding="utf-8").write("x\n")
    g("add", "-A")
    check("B5_变体命名拒", 1, run_gate(repo, "commit-msg", "正常提交说明文本\n"))
    # 版本号题名（`1.1.3-pre-v1` 一类）不是旁路副本：2026-10-29 收窄后须放行
    repo, g = newrepo("t_b5ver")
    os.makedirs(os.path.join(repo, "docs"))
    open(os.path.join(repo, "docs", "10.10.61-实测-JDK-1.1.3-pre-v1-pause.md"),
         "w", encoding="utf-8").write("x\n")
    g("add", "-A")
    check("B5_版本号题名放行", 0, run_gate(repo, "commit-msg", "正常提交说明文本\n"))
    # B5 整改通道：删除遗留副本（状态 D）必须放行，否则违规件永远清不掉
    repo, g = newrepo("t_b5del")
    os.makedirs(os.path.join(repo, "docs"))
    legacy = os.path.join(repo, "docs", "legacy.md.bak")
    open(legacy, "w", encoding="utf-8").write("x\n")
    g("add", "-A")
    subprocess.run(["git", "commit", "-q", "--no-verify", "-m", "基线：遗留旁路副本"],
                   cwd=repo, capture_output=True)
    os.remove(legacy)
    g("add", "-A")
    check("B5_删遗留副本放行", 0, run_gate(repo, "commit-msg", "清除遗留旁路备份副本\n"))
    repo, g = newrepo("t_b5ok")
    os.makedirs(os.path.join(repo, "docs"))
    open(os.path.join(repo, "docs", "note.md"), "w", encoding="utf-8").write("x\n")
    g("add", "-A")
    check("B5_正常件放行", 0, run_gate(repo, "commit-msg", "正常提交说明文本\n"))

    # H1 提交说明质量（无放行标记）
    repo, g = newrepo("t_h1")
    os.makedirs(os.path.join(repo, "docs"))
    open(os.path.join(repo, "docs", "note.md"), "w", encoding="utf-8").write("x\n")
    g("add", "-A")
    check("H1_占位拒", 1, run_gate(repo, "commit-msg", "1\n"))
    check("H1_过短拒", 1, run_gate(repo, "commit-msg", "fix\n"))
    check("H1_BOM拒", 1, run_gate(repo, "commit-msg", "\ufeff正常的提交说明文本\n"))
    check("H1_合规放行", 0, run_gate(repo, "commit-msg", "正常提交说明文本\n"))

    # H3 直角引号六码位（提交期兜底阻断；直接跑 commit-msg 模拟 rebase/漏跑 pre-commit 路径）
    repo, g = newrepo("t_h3prose")
    with open(os.path.join(repo, "doc.md"), "w", encoding="utf-8") as f:
        f.write("正文\u300c甲\u300d\n")
    g("add", "-A")
    check("H3_散文直角引号拒", 1, run_gate(repo, "commit-msg", "正常提交说明文本\n"))
    check("H3_批准放行", 0, run_gate(repo, "commit-msg", TAG_OWNER + " 有意保留直角引号\n"))
    repo, g = newrepo("t_h3excl")
    os.makedirs(os.path.join(repo, "05-卷册大纲"))
    with open(os.path.join(repo, "05-卷册大纲", "x.md"), "w", encoding="utf-8") as f:
        f.write("内容层\u300c甲\u300d\n")
    g("add", "-A")
    check("H3_内容层面拒", 1, run_gate(repo, "commit-msg", "正常提交说明文本\n"))
    repo, g = newrepo("t_h3code")
    with open(os.path.join(repo, "doc.md"), "w", encoding="utf-8") as f:
        f.write("```text\n代码内\u300c不动\u300d\n```\n")
    g("add", "-A")
    check("H3_代码上下文拒", 1, run_gate(repo, "commit-msg", "正常提交说明文本\n"))

    # F1 半角形 ｢｣（U+FF62/FF63）自动改正
    repo, g = newrepo("t_fh")
    with open(os.path.join(repo, "doc.md"), "w", encoding="utf-8") as f:
        f.write("半角｢甲｣与正文\n")
    g("add", "-A")
    check("F1_半角形放行", 0, run_gate(repo, "pre-commit"))
    fixed = open(os.path.join(repo, "doc.md"), "rb").read().decode("utf-8")
    okf = "“甲”" in fixed and "\uff62" not in fixed
    results.append(("F1_半角形改正正确", 1, 0 if okf else 1, okf))
    if not okf:
        print("  ✗ F1_半角形改正正确 " + repr(fixed[:120]))

    shutil.rmtree(base, ignore_errors=True)
    bad = [r for r in results if not r[3]]
    for name, expect, got, ok in results:
        if ok:
            print("  ✓ %s" % name)
    print("git_commit_gate --selftest：%d/%d %s" % (len(results) - len(bad), len(results), "PASS" if not bad else "FAIL"))
    return 0 if not bad else 1


def main(argv):
    if "--selftest" in argv:
        return selftest()
    if len(argv) >= 3 and argv[1] == "--stage":
        stage = argv[2]
        if stage == "pre-commit":
            return stage_precommit()
        if stage == "commit-msg":
            if len(argv) < 4:
                print("commit-msg 形态需要 <commit-msg-path>", file=sys.stderr)
                return 2
            try:
                with open(argv[3], "rb") as f:
                    msg = f.read().decode("utf-8", errors="replace")
            except OSError as e:
                print("git_commit_gate：无法读提交说明 %r：%s" % (argv[3], e), file=sys.stderr)
                return 2
            return stage_commitmsg(msg)
        print("未知阶段 %r" % stage, file=sys.stderr)
        return 2
    # 兼容旧调用形态（无 --stage，传 msg 路径）
    if len(argv) == 2:
        return stage_commitmsg(argv[1])
    print("用法：git_commit_gate.py --stage pre-commit | --stage commit-msg <msg> | --selftest", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
