#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Git 提交门禁（commit-msg 薄壳后端；2026-10-17 立，固定脚本）

由 `.git/hooks/commit-msg` 薄壳调用（hook 本身不入库，本件为权威实现）：

    exec python "00-编纂规则与格式规范/01-规则/脚本与命令/git_commit_gate.py" "$@"

对应 `流程规则.md`「Git 暂存规则（.gitignore 与体积门槛；2026-10-17 立）」两条硬规则，
除非提交说明含批准标记，否则拒收（exit 1）：

  G1  新增（A）路径命中 `.gitignore`（`git check-ignore`）——被忽略条目不得入库；
  G2  暂存 blob 单个 > 5 MB（5,242,880 字节）——大件不得入库。

批准标记（在提交说明全文中检索，规范要求标注于首行）：
  `APPROVED-IGNORED:` 放行 G1；`APPROVED-BIGFILE:` 放行 G2。
含 `--no-verify` 时本 hook 不被 git 调用；绕过须主理人显式指示并留痕 changelog。

为什么用 commit-msg 而非 pre-commit：pre-commit 阶段提交说明尚未定稿，无法核对
批准标记；commit-msg 运行时暂存区与说明均已固定。

用法：
  git_commit_gate.py <commit-msg-path>   # commit-msg 调用形态（CWD＝仓库根）
  git_commit_gate.py --selftest          # 隔离临时仓库五用例负向自检

退出码：0 放行；1 拒收（stdout 列违规件）；2 依赖缺失（git 不可用）。
"""
import os
import subprocess
import sys

THRESHOLD = 5242880  # 5 MB
TAG_IGNORED = "APPROVED-IGNORED:"
TAG_BIGFILE = "APPROVED-BIGFILE:"


def run_git(args, cwd=None):
    return subprocess.run(["git"] + args, capture_output=True, cwd=cwd)


def staged_items():
    """返回 [(状态, 新路径), ...]；R/C 取新路径，D 跳过。"""
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
            continue
        items.append((st, path))
    return items


def blob_size(path, cwd=None):
    p = run_git(["cat-file", "-s", ":%s" % path], cwd=cwd)
    if p.returncode != 0:
        return -1
    try:
        return int(p.stdout.strip())
    except ValueError:
        return -1


def gate(cwd=None):
    items = staged_items()
    if items is None:
        print("git_commit_gate：无法读取暂存区（git 失败）", file=sys.stderr)
        return 2
    if not items:
        return 0  # 无暂存内容（如空提交检查），放行由 git 自行裁决
    bad_ignored, bad_big = [], []
    for st, path in items:
        if not path:
            continue
        if run_git(["check-ignore", "-q", "--", path], cwd=cwd).returncode == 0:
            bad_ignored.append(path)
        sz = blob_size(path, cwd=cwd)
        if sz > THRESHOLD:
            bad_big.append("%s（%d 字节）" % (path, sz))
    return (bad_ignored, bad_big)


def main(argv):
    if len(argv) == 2 and argv[1] == "--selftest":
        return selftest()
    if len(argv) < 2:
        print("用法：git_commit_gate.py <commit-msg-path> | --selftest", file=sys.stderr)
        return 2
    msg_path = argv[1]
    try:
        with open(msg_path, "rb") as f:
            msg = f.read().decode("utf-8", errors="replace")
    except OSError as e:
        print("git_commit_gate：无法读提交说明 %r：%s" % (msg_path, e), file=sys.stderr)
        return 2
    bad_ignored, bad_big = gate()
    ok_i = TAG_IGNORED in msg
    ok_b = TAG_BIGFILE in msg
    errs = []
    if bad_ignored and not ok_i:
        errs.append("G1 被 .gitignore 排除的条目进入了暂存区：\n  " + "\n  ".join(bad_ignored))
    if bad_big and not ok_b:
        errs.append("G2 单个文件超过 5 MB（%d 字节）进入了暂存区：\n  " % THRESHOLD + "\n  ".join(bad_big))
    if errs:
        print("git_commit_gate 拒收（流程规则「Git 暂存规则」；主理人批准须在提交说明标注 %s / %s）：" % (TAG_IGNORED, TAG_BIGFILE))
        for e in errs:
            print(e)
        return 1
    if (bad_ignored and ok_i) or (bad_big and ok_b):
        print("git_commit_gate：检测到批准标记，放行（G1×%d 件被忽略条目、G2×%d 件大文件）——请确认 changelog 已留痕批准记录。" % (len(bad_ignored), len(bad_big)))
    return 0


def selftest():
    """隔离临时仓库五用例：G1 拒／G1 放／G2 拒／G2 放／正常放。"""
    import tempfile
    import shutil

    base = tempfile.mkdtemp(prefix="git_gate_selftest_")
    results = []

    def case(name, files, ignore_lines, msg, expect):
        repo = os.path.join(base, name)
        os.makedirs(repo)
        def g(*a):
            return subprocess.run(["git"] + list(a), cwd=repo, capture_output=True)
        g("init", "-q")
        g("config", "user.email", "gate@test")
        g("config", "user.name", "gate")
        with open(os.path.join(repo, ".gitignore"), "w", encoding="utf-8") as f:
            f.write("\n".join(ignore_lines) + "\n")
        for fn, data in files.items():
            fp = os.path.join(repo, fn)
            if os.path.dirname(fn):
                os.makedirs(os.path.dirname(fp), exist_ok=True)
            with open(fp, "wb") as f:
                f.write(data)
        g("add", "-A")
        # 正常 add 不会收录被忽略文件——须显式 -f 才构成「忽略条目入库」场景
        g("add", "-f", "secret.txt")
        mp = os.path.join(repo, "MSG")
        with open(mp, "w", encoding="utf-8") as f:
            f.write(msg)
        p = subprocess.run([sys.executable, os.path.abspath(__file__), mp], cwd=repo, capture_output=True)
        got = p.returncode
        ok = got == expect
        results.append((name, expect, got, ok, p.stdout.decode("utf-8", "replace").strip()[:120]))

    big = b"x" * (THRESHOLD + 1024)
    case("t1_ignored_reject", {"secret.txt": b"s"}, ["secret*.txt"], "test\n", 1)
    case("t2_ignored_allow", {"secret.txt": b"s"}, ["secret*.txt"], "APPROVED-IGNORED: test\n", 0)
    case("t3_big_reject", {"big.bin": big}, [], "test\n", 1)
    case("t4_big_allow", {"big.bin": big}, [], "APPROVED-BIGFILE: test\n", 0)
    case("t5_normal", {"ok.txt": b"hello"}, ["secret*.txt"], "normal commit\n", 0)

    shutil.rmtree(base, ignore_errors=True)
    all_ok = all(r[3] for r in results)
    for name, expect, got, ok, out in results:
        print("  %s %s（期望 %d 实得 %d）%s" % ("✓" if ok else "✗", name, expect, got, out if not ok else ""))
    print("git_commit_gate --selftest：%d/5 %s" % (sum(1 for r in results if r[3]), "PASS" if all_ok else "FAIL"))
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
