#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Git 提交门禁（双阶段统一后端；2026-10-17 立，2026-10-17 主理人批准扩展，固定脚本）

由两个 hook 薄壳调用（薄壳位于 `.git/hooks/`，不入库，本件为权威实现）：

    .git/hooks/pre-commit   → exec python …/git_commit_gate.py --stage pre-commit
    .git/hooks/commit-msg   → exec python …/git_commit_gate.py --stage commit-msg "$@"

对应 `流程规则.md`「Git 暂存规则（.gitignore 与体积门槛；2026-10-17 立）」。

── pre-commit 阶段（自动改正，永不拒收；2026-10-17 薄壳安装，清理批合入）──
对暂存区中的文档类文件（.md／.txt，排除内容层与逐字保真档案，见 FIX_EXCLUDE_PREFIX）：

  F1  直角引号「」『』 → 弯引号 “”‘’（开闭字符一一映射；围栏代码块与行内代码段内不动）
  F2  不可见字符全口径清理（2026-10-17 主理人裁定，算法单一来源＝fix_md_invisible.py 的
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
  F4  别名成对自动 cp（2026-10-17 主理人批准批）：暂存区含 CLAUDE.md 且工作树
      AGENTS.md 与其逐字节不一致时，以工作树 CLAUDE.md 覆写 AGENTS.md 并重新暂存
      （依据：CLAUDE.md 唯一真相、AGENTS.md 逐字节别名副本）；仅暂存 AGENTS.md 而
      CLAUDE.md 未暂存者**不自动改正**（改序违规），交 commit-msg H2 阻断。
  另：非 UTF-8 文件整体跳过不改正（旧实现 errors="replace" 会把坏字节写成 U+FFFD 回盘，已废）。

改后写回工作树并 `git add`，打印改动清单；无源文件级语义变化。

── commit-msg 阶段（阻断，除非提交说明含批准标记）──

  G1  新增（A）路径命中 `.gitignore`（`git check-ignore --no-index`）→ 拒；`APPROVED-IGNORED:` 放行
  G2  暂存 blob 单个 > 5 MB（5,242,880 字节）→ 拒；`APPROVED-BIGFILE:` 放行
  B2  根目录新增一级条目不在白名单 → 拒；`APPROVED-BY-OWNER:` 放行
  B3  删除 `12-数据库备份/**` → 拒；`APPROVED-BY-OWNER:` 放行
  B4  文档类文件含全角空格 U+3000 → 拒；`APPROVED-BY-OWNER:` 放行
  H1  提交说明质量（2026-10-17 主理人批准批，无放行标记）：首行非空、≥8 字符、
      非纯数字／标点占位、消息不以 BOM 起始 → 违者拒（改写消息零成本，不设 bypass）
  H2  CLAUDE.md↔AGENTS.md **提交后**逐字节一致（单方暂存者以 HEAD 内容计）→
      不一致拒；`APPROVED-BY-OWNER:` 放行

含 `--no-verify` 时 hook 不被 git 调用；绕过须主理人显式指示并留痕 changelog。
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

ANGLE_MAP = {"\u300c": "\u201c", "\u300d": "\u201d", "\u300e": "\u2018", "\u300f": "\u2019"}
ZERO_WIDTH = "\u200b\u200c\u200d\u2060\ufeff"
IDEOGRAPHIC_SPACE = "\u3000"

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
    "08-核查报告与多轮复核/重构2026/data/", "08-核查报告与多轮复核/12-重构大纲书目述评/",
)
ROOT_FILE_WHITELIST = {
    ".autocorrectrc", ".gitattributes", ".gitignore", ".markdownlint.json",
    ".textlintrc", ".textlintrc.json", "LICENSE", "CLAUDE.md", "AGENTS.md",
    "favicon.ico", "logo.svg", "README.md",
}


def run_git(args, cwd=None):
    return subprocess.run(["git"] + args, capture_output=True, cwd=cwd)


def staged_items():
    """返回 [(状态, 新路径), ...]；R/C 取新路径，D 跳过（另由删除检查处理）。"""
    p = run_git(["diff", "--cached", "--name-status", "-z"])
    if p.returncode != 0:
        return None
    tok = p.stdout.decode("utf-8", errors="replace").split("\0")
    items, i = [], 0
    while i < len(tok) - 1:
        st = tok[i]
        if not st:
            i += 1
            continue
        i += 1
        path = tok[i] if i < len(tok) else ""
        i += 1
        if st.startswith("R") or st.startswith("C"):
            i += 1  # 跳过原路径
        if st == "D":
            items.append(("D", path))
            continue
        items.append((st, path))
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
    if text.startswith("\ufeff"):
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
    """自动改正暂存文档类文件；永不拒收。"""
    items = staged_items()
    if items is None:
        print("git_commit_gate：无法读取暂存区（git 失败）", file=sys.stderr)
        return 2
    touched = 0
    for st, path in items:
        if st == "D" or not is_doc_fixable(path):
            continue
        wt = os.path.join(os.getcwd(), path)
        if not os.path.isfile(wt):
            continue
        raw = open(wt, "rb").read()
        if b"\0" in raw[:8000]:
            continue  # 二进制跳过
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            print("git_commit_gate 跳过（非 UTF-8，不改正）：%s" % path)
            continue
        if "\ufffd" in text:
            print("git_commit_gate 披露（含 U+FFFD 替换字符，不改正、另行报告）：%s" % path)
        new, changes = fix_text(text)
        if not changes:
            continue
        open(wt, "wb").write(new.encode("utf-8"))
        run_git(["add", "--", path])
        touched += 1
        print("git_commit_gate 自动改正：%s（%s）" % (path, "；".join(changes)))
    if touched:
        print("git_commit_gate：共自动改正 %d 个文件（已重新暂存），请复核 diff。" % touched)
    # F4 别名成对自动 cp（2026-10-17 主理人批准批）：工作树 CLAUDE.md 为唯一真相
    st_map = {path: st for st, path in items if path}
    if st_map.get("CLAUDE.md") not in (None, "D"):
        wt_c = os.path.join(os.getcwd(), "CLAUDE.md")
        wt_a = os.path.join(os.getcwd(), "AGENTS.md")
        if os.path.isfile(wt_c):
            try:
                cb = open(wt_c, "rb").read()
                ab = open(wt_a, "rb").read() if os.path.isfile(wt_a) else None
            except OSError:
                cb = ab = None
            if cb is not None and ab != cb:
                try:
                    open(wt_a, "wb").write(cb)
                    run_git(["add", "--", "AGENTS.md"])
                    touched += 1
                    print("git_commit_gate 自动改正：AGENTS.md（F4 别名成对 cp ← CLAUDE.md）")
                except OSError as e:
                    print("git_commit_gate F4 cp 失败（%s）；如强提交将被 commit-msg H2 阻断。" % e,
                          file=sys.stderr)
    elif "AGENTS.md" in st_map and "CLAUDE.md" not in st_map:
        print("git_commit_gate 提示：AGENTS.md 单独暂存而 CLAUDE.md 未暂存——若内容不一致将被 "
              "commit-msg H2 阻断（规则：先改 CLAUDE.md，再 cp 覆盖 AGENTS.md）。")
    return 0


def blob_has_ideographic_space(path):
    p = run_git(["cat-file", "-p", ":%s" % path])
    if p.returncode != 0:
        return False
    return IDEOGRAPHIC_SPACE in p.stdout.decode("utf-8", errors="replace")


def blob_size(path):
    p = run_git(["cat-file", "-s", ":%s" % path])
    if p.returncode != 0:
        return -1
    try:
        return int(p.stdout.strip())
    except ValueError:
        return -1


def _blob_bytes(rev_path):
    p = run_git(["cat-file", "-p", rev_path])
    return p.stdout if p.returncode == 0 else None


def check_msg_quality(msg):
    """H1：提交说明质量（2026-10-17 主理人批准批；无放行标记——改写消息零成本）。

    判据：①消息不以 BOM 起始（PowerShell Set-Content -Encoding UTF8 带 BOM 会污染
    消息首字符——2026-10-17 ca3134a07 实例）；②首行非空；③首行 ≥8 字符；
    ④首行非纯数字／标点占位（"1/2/！"式整索引提交当日 ≥7 件的教训）。
    """
    bad = []
    if msg.startswith("\ufeff"):
        bad.append("提交说明以 BOM 起始——将消息文件重写为 UTF-8 无 BOM 再提交"
                   "（PowerShell 用 -Encoding utf8NoBOM 或经 Python 落盘）")
    first = msg.split("\n", 1)[0].strip()
    if not first:
        bad.append("提交说明首行为空")
        return bad
    if len(first) < 8:
        bad.append("首行过短（%d 字符）：%r" % (len(first), first[:40]))
    if re.fullmatch(r"[0-9!\"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~\s]+", first):
        bad.append("首行为纯数字／标点占位（无实质词句）：%r" % first[:40])
    return bad


def check_alias_pair(items):
    """H2：CLAUDE.md↔AGENTS.md 逐字节一致（以本提交落定后的内容为准）。

    单方暂存时，另一方按 HEAD 内容计（未暂存＝本次不动它，提交后仍是 HEAD 版）；
    一方暂存删除按空内容计。仓库尚无 HEAD 且两文件均未暂存 → 跳过（首次提交场景）。
    """
    staged = {path: st for st, path in items if path}
    sa, sb = staged.get("CLAUDE.md"), staged.get("AGENTS.md")
    if sa is None and sb is None:
        return []

    def post(path, st):
        if st == "D":
            return b""
        if st is not None:
            return _blob_bytes(":%s" % path)
        return _blob_bytes("HEAD:%s" % path)

    ca, cb = post("CLAUDE.md", sa), post("AGENTS.md", sb)
    if ca is None and cb is None:
        return []
    if ca != cb:
        return ["CLAUDE.md 提交后 %s ≠ AGENTS.md 提交后 %s（逐字节）——先改 CLAUDE.md，"
                "再 cp CLAUDE.md AGENTS.md；确属有意单改别名件，用 APPROVED-BY-OWNER: 放行"
                % ("缺失" if ca is None else "%d 字节" % len(ca),
                   "缺失" if cb is None else "%d 字节" % len(cb))]
    return []


def stage_commitmsg(msg):
    """阻断检查；批准标记放行。"""
    items = staged_items()
    if items is None:
        print("git_commit_gate：无法读取暂存区（git 失败）", file=sys.stderr)
        return 2
    bad_ignored, bad_big, bad_root, bad_bakdel, bad_space = [], [], [], [], []
    for st, path in items:
        if not path:
            continue
        if st == "D":
            if path.startswith("12-数据库备份/"):
                bad_bakdel.append(path)
            continue
        if st == "A" and run_git(["check-ignore", "--no-index", "-q", "--", path]).returncode == 0:
            bad_ignored.append(path)
        if st == "A" and "/" not in path and path not in ROOT_FILE_WHITELIST:
            bad_root.append(path)
        if is_doc_fixable(path) and blob_has_ideographic_space(path):
            bad_space.append(path)
        sz = blob_size(path)
        if sz > THRESHOLD:
            bad_big.append("%s（%d 字节）" % (path, sz))
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
    bad_pair = check_alias_pair(items)
    if bad_pair:
        errs.append("H2 CLAUDE.md↔AGENTS.md 提交后将不一致：\n  " + "\n  ".join(bad_pair))
    h1 = check_msg_quality(msg)
    if h1:
        errs.append("H1 提交说明不满足质量判据（无放行标记，改写即可）：\n  " + "\n  ".join(h1))
    errs = [e for e in errs if not (
        (e.startswith("G1") and TAG_IGNORED in msg) or
        (e.startswith("G2") and TAG_BIGFILE in msg) or
        (e.startswith(("B2", "B3", "B4", "H2")) and TAG_OWNER in msg))]
    if errs:
        print("git_commit_gate 拒收（流程规则「Git 暂存规则」；批准标记：%s／%s／%s）：" % (TAG_IGNORED, TAG_BIGFILE, TAG_OWNER))
        for e in errs:
            print(e)
        return 1
    notes = []
    if bad_ignored:
        notes.append("G1×%d" % len(bad_ignored))
    if bad_big:
        notes.append("G2×%d" % len(bad_big))
    if bad_root or bad_bakdel or bad_space:
        notes.append("B×%d" % (len(bad_root) + len(bad_bakdel) + len(bad_space)))
    if bad_pair:
        notes.append("H2×%d" % len(bad_pair))
    if notes:
        print("git_commit_gate：检测到批准标记，放行（%s）——请确认 changelog 已留痕批准记录。" % "、".join(notes))
    return 0


def selftest():
    """隔离临时仓库全用例：改正区 12（F 区 5＋链路 2＋排除边界 3＋别名 2）＋阻断与既有 18＝30 用例。"""
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
    check("B4_链路复检放行", 0, run_gate(repo, "commit-msg", "m\n"))

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
    check("EXCL_提交放行", 0, run_gate(repo, "commit-msg", "m\n"))

    # G1/G2 既有
    repo, g = newrepo("t_g1")
    with open(os.path.join(repo, ".gitignore"), "w") as f:
        f.write("secret*.txt\n")
    open(os.path.join(repo, "secret.txt"), "wb").write(b"s")
    g("add", "-A")
    g("add", "-f", "secret.txt")
    check("G1_忽略拒", 1, run_gate(repo, "commit-msg", "m\n"))
    g("reset", "-q", "secret.txt")
    check("G1_撤回后放行", 0, run_gate(repo, "commit-msg", "m\n"))
    repo, g = newrepo("t_g2")
    os.makedirs(os.path.join(repo, "data"))
    open(os.path.join(repo, "data", "big.bin"), "wb").write(b"x" * (THRESHOLD + 1))
    g("add", "-A")
    check("G2_大文件拒", 1, run_gate(repo, "commit-msg", "m\n"))
    check("G2_批准放行", 0, run_gate(repo, "commit-msg", TAG_BIGFILE + " m\n"))

    # B2 根目录新条目
    repo, g = newrepo("t_b2")
    open(os.path.join(repo, "mystery.bin"), "wb").write(b"z")
    g("add", "-A")
    check("B2_根目录新条目拒", 1, run_gate(repo, "commit-msg", "m\n"))
    check("B2_批准放行", 0, run_gate(repo, "commit-msg", TAG_OWNER + " m\n"))
    repo, g = newrepo("t_b2b")
    open(os.path.join(repo, ".autocorrectrc"), "w").write("rules: {}\n")
    g("add", "-A")
    check("B2_白名单放行", 0, run_gate(repo, "commit-msg", "m\n"))

    # B3 备份删除
    repo, g = newrepo("t_b3")
    os.makedirs(os.path.join(repo, "12-数据库备份", "x"))
    open(os.path.join(repo, "12-数据库备份", "x", "a.gz"), "wb").write(b"b")
    g("add", "-A")
    g("commit", "-q", "-m", "init")
    os.remove(os.path.join(repo, "12-数据库备份", "x", "a.gz"))
    g("add", "-A")
    check("B3_备份删除拒", 1, run_gate(repo, "commit-msg", "m\n"))
    check("B3_批准放行", 0, run_gate(repo, "commit-msg", TAG_OWNER + " m\n"))

    # B4 全角空格
    repo, g = newrepo("t_b4")
    with open(os.path.join(repo, "note.md"), "w", encoding="utf-8") as f:
        f.write("甲\u3000乙\n")
    g("add", "-A")
    check("B4_全角空格拒", 1, run_gate(repo, "commit-msg", "m\n"))
    check("B4_批准放行", 0, run_gate(repo, "commit-msg", TAG_OWNER + " m\n"))

    # F4 别名成对自动 cp（2026-10-17 主理人批准批）
    repo, g = newrepo("t_f4")
    with open(os.path.join(repo, "CLAUDE.md"), "w", encoding="utf-8") as f:
        f.write("v1 正文\n")
    with open(os.path.join(repo, "AGENTS.md"), "w", encoding="utf-8") as f:
        f.write("过期副本\n")
    g("add", "CLAUDE.md")                       # 只暂存 CLAUDE.md
    check("F4_precommit放行", 0, run_gate(repo, "pre-commit"))
    fixed_a = open(os.path.join(repo, "AGENTS.md"), encoding="utf-8").read()
    okf4 = fixed_a == "v1 正文\n"
    results.append(("F4_别名自动cp", 1, 0 if okf4 else 1, okf4))
    if not okf4:
        print("  ✗ F4_AGENTS 未同步 " + repr(fixed_a))
    check("F4_成对后commit-msg放行", 0, run_gate(repo, "commit-msg", "shenyue 线归档处置批\n"))

    # H1 提交说明质量（无放行标记）
    repo, g = newrepo("t_h1")
    open(os.path.join(repo, "a.md"), "w", encoding="utf-8").write("x\n")
    g("add", "-A")
    check("H1_占位拒", 1, run_gate(repo, "commit-msg", "1\n"))
    check("H1_过短拒", 1, run_gate(repo, "commit-msg", "fix\n"))
    check("H1_BOM拒", 1, run_gate(repo, "commit-msg", "正常的提交说明文本\n"))
    check("H1_合规放行", 0, run_gate(repo, "commit-msg", "正常提交说明\n"))

    # H2 成对一致性阻断
    repo, g = newrepo("t_h2")
    with open(os.path.join(repo, "CLAUDE.md"), "w", encoding="utf-8") as f:
        f.write("v1\n")
    with open(os.path.join(repo, "AGENTS.md"), "w", encoding="utf-8") as f:
        f.write("v1\n")
    g("add", "-A")
    g("commit", "-q", "-m", "初始基线提交")
    with open(os.path.join(repo, "CLAUDE.md"), "w", encoding="utf-8") as f:
        f.write("v2 新内容\n")
    with open(os.path.join(repo, "AGENTS.md"), "w", encoding="utf-8") as f:
        f.write("v2 新内容\n")
    g("add", "AGENTS.md")                       # 只暂存 AGENTS.md（改序违规）
    check("H2_分叉拒", 1, run_gate(repo, "commit-msg", "正常提交说明\n"))
    g("add", "CLAUDE.md")                       # 成对暂存后
    check("H2_成对放行", 0, run_gate(repo, "commit-msg", "正常提交说明\n"))
    g("reset", "-q", "CLAUDE.md")               # 再造单方暂存分叉
    check("H2_批准放行", 0, run_gate(repo, "commit-msg", TAG_OWNER + " 有意单改别名件\n"))

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
