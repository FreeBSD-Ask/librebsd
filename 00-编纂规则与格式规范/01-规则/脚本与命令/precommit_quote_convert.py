#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pre-commit 直角引号自动转换（pre-commit 薄壳后端；2026-10-17 立，固定脚本）

由 `.git/hooks/pre-commit` 薄壳调用（hook 本身不入库，本件为权威实现）：

    exec python "00-编纂规则与格式规范/01-规则/脚本与命令/precommit_quote_convert.py" "$@"

判据源：写作规则.md「标点符号规则」——中文方头括号（U+300C、U+300D）与白双引号
（U+300E、U+300F）禁止出现，改用弯引号。依据主理人 2026-10-17 令，该判据由本件在
每次 `git commit` 时自动执行（流程规则.md「直角引号提交自动转换」），固定映射：

    U+300C → U+201C    U+300D → U+201D
    U+300E → U+2018    U+300F → U+2019

行为（对暂存区 index vs HEAD 的 A/M/T/R/C 文件逐个实测；D 不涉内容不在列）：
  1. 读工作树字节，快速路径无四码位字节序列命中即放行（不解码、不改写）；
  2. 命中者须为合法 UTF-8 方改写：二进制／非 UTF-8／符号链接一律跳过不改；
  3. 字节级等长替换（UTF-8 下源码位与目标码位均为三字节，偏移不受影响），
     换行与编码形态逐字节保留；写回工作树后 `git add` 重新暂存；
  4. 全部成功 exit 0 放行提交；读取／写盘／重新暂存失败 exit 1 中止提交
     （fail-closed；已写盘的转换保留，排查后重新提交即可）。

为什么用 pre-commit 而非 commit-msg：内容改写必须发生在提交对象成形之前，
commit-msg 阶段只能裁决不能改内容。本件先于 `.git/hooks/commit-msg`（Git 暂存
门禁 git_commit_gate.py）执行，二者互补——本件改写并重暂存完毕后，暂存门禁对
改写后的暂存区做 G1／G2 裁决。

已知边界：`git add -p` 分片暂存场景下本件按工作树整体重新暂存（分片选择会被
工作树态覆盖）；rebase／cherry-pick 等序列器提交不触发 pre-commit，该路径不获
自动转换；本件只做四码位替换，不替代装配器等既有流程。

源文件自洁约束：本源文件自身不得出现上述四个直角引号字符（否则提交本件时会被
本钩子转换而自伤），一律以 \\uXXXX 转义或码位名书写；--selftest 含自洁断言。

用法：
  （无参数）     pre-commit 调用形态（CWD＝仓库根）
  --dry-run      只报告将发生的转换，不写盘、不暂存
  --selftest     独立自检（不依赖 git 仓库）

退出码：0 放行（含无需转换）；1 转换后处理失败（提交中止）；2 git 不可用。
"""
import subprocess
import sys
import tempfile
from pathlib import Path

# 直角引号 → 弯引号 固定映射（源码以转义书写，防钩子自伤）
CORNERS = {
    "\u300c": "\u201c",  # 左角引号 → 左弯双引号
    "\u300d": "\u201d",  # 右角引号 → 右弯双引号
    "\u300e": "\u2018",  # 左白双引号 → 左弯单引号
    "\u300f": "\u2019",  # 右白双引号 → 右弯单引号
}
BINARY_MAP = {k.encode("utf-8"): v.encode("utf-8") for k, v in CORNERS.items()}


def run_git(args):
    return subprocess.run(["git"] + args, capture_output=True)


def convert_bytes(data):
    """返回 (新字节, 命中计数, 状态)；状态 ∈ clean / converted / nonutf8。

    命中计数的键为直角引号 UTF-8 字节序列。仅合法 UTF-8 才改写；含命中字节
    但非合法 UTF-8（二进制等）原样返回并标 nonutf8，由调用方跳过。
    """
    hits = {}
    for seq in BINARY_MAP:
        n = data.count(seq)
        if n:
            hits[seq] = n
    if not hits:
        return data, hits, "clean"
    try:
        data.decode("utf-8")
    except UnicodeDecodeError:
        return data, hits, "nonutf8"
    out = data
    for seq, rep in BINARY_MAP.items():
        out = out.replace(seq, rep)
    return out, hits, "converted"


def staged_files(toplevel):
    """返回暂存区相对路径列表（A/M/T/R/C；D 不在列）。git 不可用返回 None。

    R/C 的 -z 双路径以「工作树存在者」为新路径消歧（两者皆存在时取后者，
    即人工输出形态的目的路径）；配合主流程 is_file 守卫，两种输出序均正确。
    """
    p = run_git(["diff", "--cached", "--name-status", "-z"])
    if p.returncode != 0:
        sys.stderr.write(p.stderr.decode("utf-8", "replace"))
        return None
    try:
        tok = p.stdout.decode("utf-8", "strict").split("\0")
    except UnicodeDecodeError:
        sys.stderr.write("pre-commit 直角引号转换：暂存路径含非 UTF-8 字节，无法安全处理\n")
        return None
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
            path2 = tok[i] if i < len(tok) else ""
            i += 1
            e1 = bool(path) and (toplevel / path).exists()
            e2 = bool(path2) and (toplevel / path2).exists()
            if e1 and not e2:
                items.append(path)
            elif path2:
                items.append(path2)
            else:
                items.append(path)
            continue
        if st == "D" or not path:
            continue
        items.append(path)
    return items


def main(argv):
    if "--selftest" in argv:
        return selftest()
    dry = "--dry-run" in argv

    top = run_git(["rev-parse", "--show-toplevel"])
    if top.returncode != 0:
        return 0  # 不在 git 仓库内：静默放行，交由调用方自行裁决
    toplevel = Path(top.stdout.decode("utf-8", "replace").strip())

    items = staged_files(toplevel)
    if items is None:
        return 2

    converted, skipped, failures = [], [], []
    for rel in items:
        wt = toplevel / rel
        if wt.is_symlink() or not wt.is_file():
            continue  # 仅索引条目（删除／子模块指针）或符号链接：不按常规文件改写
        try:
            data = wt.read_bytes()
        except OSError as e:
            failures.append("%s（读取失败：%s）" % (rel, e))
            continue
        new, hits, status = convert_bytes(data)
        if status == "clean":
            continue
        if status == "nonutf8":
            skipped.append(rel)
            continue
        if dry:
            converted.append((rel, hits))
            continue
        try:
            wt.write_bytes(new)
        except OSError as e:
            failures.append("%s（写盘失败：%s）" % (rel, e))
            continue
        r = run_git(["add", "--", rel])
        if r.returncode != 0:
            failures.append("%s（重新暂存失败：%s）" % (
                rel, r.stderr.decode("utf-8", "replace").strip()))
        else:
            converted.append((rel, hits))

    if skipped:
        print("pre-commit 直角引号转换：非 UTF-8（含二进制）跳过 %d 件不改：%s"
              % (len(skipped), "；".join(skipped)))
    if converted:
        print("pre-commit --dry-run 预览（未写盘、未暂存）：" if dry
              else "pre-commit 直角引号已自动转换为弯引号并重新暂存：")
        total = 0
        for rel, hits in converted:
            detail = "、".join("%s×%d" % (seq.decode("utf-8"), n)
                               for seq, n in sorted(hits.items()))
            print("  %s（%s）" % (rel, detail))
            total += sum(hits.values())
        print("  共 %d 件 %d 处" % (len(converted), total))
    if failures:
        sys.stderr.write(
            "pre-commit 直角引号转换失败（提交中止；已写盘的转换保留，排查后重新提交）：\n  "
            + "\n  ".join(failures) + "\n")
        return 1
    return 0


def selftest():
    """判据非空自检（隔离临时目录，不依赖 git）。"""
    L, R = chr(0x300C), chr(0x300D)
    L2, R2 = chr(0x300E), chr(0x300F)
    LD, RD = chr(0x201C), chr(0x201D)
    LS, RS = chr(0x2018), chr(0x2019)
    results = []

    def ck(name, cond):
        results.append((name, bool(cond)))

    # t1 四码位全映射
    new, hits, st = convert_bytes((L + R + L2 + R2).encode("utf-8"))
    ck("t1 四码位全映射", st == "converted" and new == (LD + RD + LS + RS).encode("utf-8"))

    # t2 CRLF 逐字节保留
    raw = ("行一" + L + "x" + R + "行二\r\n行三" + L2 + "y" + R2).encode("utf-8")
    new, hits, st = convert_bytes(raw)
    ck("t2 CRLF 保留", b"\r\n" in new and new == (
        "行一" + LD + "x" + RD + "行二\r\n行三" + LS + "y" + RS).encode("utf-8"))

    # t3 干净文件恒等（无命中不改动）
    clean = "本文件没有角引号，只有普通文本。".encode("utf-8")
    new, hits, st = convert_bytes(clean)
    ck("t3 干净恒等", st == "clean" and hits == {} and new == clean)

    # t4 非 UTF-8（含命中字节）跳过
    blob = b"\x00\x01\xff\xfe" + bytes([0xE3, 0x80, 0x8C]) + b"\x80\x8d"
    new, hits, st = convert_bytes(blob)
    ck("t4 非 UTF-8 跳过", st == "nonutf8" and new == blob)

    # t5 嵌套（白双引号包裹角引号）
    new, hits, st = convert_bytes((L2 + "外" + L + "内" + R + "外" + R2).encode("utf-8"))
    ck("t5 嵌套映射", new == (LS + "外" + LD + "内" + RD + "外" + RS).encode("utf-8"))

    # t6 计数正确
    new, hits, st = convert_bytes((L * 3 + R * 2).encode("utf-8"))
    ck("t6 计数正确", st == "converted"
       and hits.get(L.encode("utf-8")) == 3 and hits.get(R.encode("utf-8")) == 2
       and new == (LD * 3 + RD * 2).encode("utf-8"))

    # t7 边界（首尾字符即直角引号）
    new, hits, st = convert_bytes((L + "中" + R).encode("utf-8"))
    ck("t7 边界映射", new == (LD + "中" + RD).encode("utf-8"))

    # t8 文件级往返（临时目录写读）
    try:
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "sample.md"
            raw = ("题" + L + "甲" + R + L2 + "乙" + R2 + "\r\n尾" + R2).encode("utf-8")
            p.write_bytes(raw)
            new, hits, st = convert_bytes(p.read_bytes())
            if st == "converted":
                p.write_bytes(new)
            ck("t8 文件往返", p.read_bytes() == (
                "题" + LD + "甲" + RD + LS + "乙" + RS + "\r\n尾" + RS).encode("utf-8"))

            # t9 干净文件不重写（字节与 mtime_ns 不变）
            q = Path(td) / "clean.md"
            qraw = "无角引号。".encode("utf-8")
            q.write_bytes(qraw)
            m0 = q.stat().st_mtime_ns
            new, hits, st = convert_bytes(q.read_bytes())
            if st == "converted":
                q.write_bytes(new)
            ck("t9 干净不重写", st == "clean" and q.read_bytes() == qraw
               and q.stat().st_mtime_ns == m0)
    except OSError as e:
        ck("t8 文件往返", False)
        ck("t9 干净不重写", False)
        sys.stderr.write("[selftest] 临时文件异常：%s\n" % e)

    # t10 映射完备性与等长性（四键四值互异、全为三字节、目标恰为弯引号四码位）
    vals = set(CORNERS.values())
    ck("t10 映射完备等长", len(CORNERS) == 4 and len(vals) == 4
       and vals == {LD, RD, LS, RS}
       and all(len(k.encode("utf-8")) == 3 and len(v.encode("utf-8")) == 3
               for k, v in CORNERS.items()))

    # t11 源文件自洁（本源文件无四字节序列、无 BOM、无 CRLF）
    try:
        src = Path(__file__).read_bytes()
        ck("t11 源文件自洁", all(seq not in src for seq in BINARY_MAP)
           and not src.startswith(b"\xef\xbb\xbf") and b"\r\n" not in src)
    except OSError as e:
        ck("t11 源文件自洁", False)
        sys.stderr.write("[selftest] 源文件读取异常：%s\n" % e)

    npass = sum(1 for _, ok in results if ok)
    for name, ok in results:
        print("[selftest] %s %s" % ("PASS" if ok else "FAIL", name))
    print("[selftest] %d/%d %s" % (npass, len(results),
                                   "全部通过" if npass == len(results) else "存在失败"))
    return 0 if npass == len(results) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
