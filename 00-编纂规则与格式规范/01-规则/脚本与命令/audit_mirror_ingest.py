#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""audit_mirror_ingest.py —— 第二十五件门禁：大纲目录镜像派生件入库白名单校验。

设立缘由
--------
`11-元数据接口/03-大纲目录镜像/` 下的 `SUMMARY.md` 与 `chapter_keywords.json` 是
大纲树的结构镜像与逐章检索索引（规则见 `大纲层级与目录规则.md` §四），属**派生权威件**，
须随大纲树一同进入版本管理。但根 `.gitignore` 有全局 `*.json` 规则，镜像 JSON 一旦
被再生（删除后重写即变为未跟踪件）就会被静默忽略——此后 `git add` 不收、`git status`
不报，提交里少一件而无人察觉。本件把“两件镜像的入库状态”变成可机检的不变量。

判据
----
E1 **存在**：文件在磁盘上存在
E2 **已跟踪**：`git ls-files --error-unmatch` 命中（index 中有该路径）
E3 **未被忽略**：`git check-ignore -v --no-index` 的命中模式不是否定式（`!` 开头）。
   `--no-index` 必需——对已跟踪路径，`git check-ignore` 缺省不按 ignore 规则评估，
   去掉该选项判据即空转；又因 `-v` 在“仅否定式命中”时同样返回 0（实测 git 2.54），
   故不可只看退出码，须解析模式首字符。
E4 **不在忽略清单**：`git status --porcelain --ignored` 中该路径不被 `!!` 条目覆盖
   （被整体忽略的父目录条目按前缀归属，如 `!! script/` 覆盖其下全部路径）

任一件任一判据失败即 exit 1；git 不可用 exit 2。

用法
----
    python audit_mirror_ingest.py                # 默认 --check（0 通过 / 1 失败 / 2 依赖缺失）
    python audit_mirror_ingest.py --list         # 打印两件镜像的四项状态
    python audit_mirror_ingest.py --selftest     # 判据非空：夹具须命中 E1／E2／E3／E4

依赖：仅标准库。路径一律相对仓库根解析（由本文件位置上行推导，不写死绝对路径）。
"""
import argparse
import pathlib
import shutil
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

REPO = pathlib.Path(__file__).resolve().parents[3]
MIRROR_DIR = "11-元数据接口/03-大纲目录镜像"
TARGETS = ("SUMMARY.md", "chapter_keywords.json")
SELFTEST_REL = "script/_mirror_ingest_selftest"

CODES = {
    "E1": "文件不存在",
    "E2": "未被 git 跟踪",
    "E3": "被 .gitignore 命中",
    "E4": "出现在 git status --ignored 的忽略清单",
}


def _git(args, root):
    """在 root 目录下跑 git，返回 CompletedProcess（bytes 输出）。"""
    return subprocess.run(["git"] + args, cwd=str(root), capture_output=True)


def inspect(root, rel):
    """返回单个路径的四项状态与失败判据码。"""
    ap = root / rel
    st = {
        "path": rel,
        "exists": ap.exists(),
        "tracked": False,
        "ignored": False,
        "ignore_rule": "",
        "status_ignored": False,
        "fails": [],
    }

    r = _git(["ls-files", "--error-unmatch", "--", rel], root)
    st["tracked"] = r.returncode == 0
    if not st["exists"]:
        st["fails"].append("E1")
    if not st["tracked"]:
        st["fails"].append("E2")

    r = _git(["check-ignore", "-v", "--no-index", "--", rel], root)
    out = r.stdout.decode("utf-8", "replace").strip()
    rule = out.split("\t")[0] if out else ""
    pattern = rule.split(":", 2)[2] if rule.count(":") >= 2 else ""
    if out and not pattern.startswith("!"):
        st["ignored"] = True
        st["ignore_rule"] = rule
        st["fails"].append("E3")

    r = _git(["status", "--porcelain", "--ignored", "-z", "--", rel], root)
    for ent in r.stdout.split(b"\0"):
        if not ent:
            continue
        line = ent.decode("utf-8", "replace")
        code, path = line[:2], line[3:]
        if code == "!!" and (rel == path or rel.startswith(path.rstrip("/") + "/")):
            st["status_ignored"] = True
            break
    if st["status_ignored"]:
        st["fails"].append("E4")
    return st


def _line(st):
    return ("  %s %-24s 存在=%s 跟踪=%s 忽略=%s 忽略清单=%s%s"
            % ("PASS" if not st["fails"] else "FAIL",
               st["path"].split("/")[-1],
               "Y" if st["exists"] else "N",
               "Y" if st["tracked"] else "N",
               "Y" if st["ignored"] else "N",
               "Y" if st["status_ignored"] else "N",
               "" if not st["ignore_rule"] else "（规则 %s）" % st["ignore_rule"]))


def targets(root=REPO):
    return [inspect(root, "%s/%s" % (MIRROR_DIR, name)) for name in TARGETS]


def cmd_check():
    print("=" * 72)
    print("大纲目录镜像派生件入库白名单校验（第二十五件）")
    print("=" * 72)
    fails = 0
    for st in targets():
        print(_line(st))
        for code in st["fails"]:
            print("        [%s] %s" % (code, CODES[code]))
        fails += len(st["fails"])
    print("-" * 72)
    print("  合计 %d 件，失败判据 %d 项" % (len(TARGETS), fails))
    if fails:
        print("  处置：镜像 JSON 须保留 `.gitignore` 白名单 `!%s/chapter_keywords.json`；"
              "重生成后未跟进者以 `git add -f` 补入并跑本件复核" % MIRROR_DIR)
        return 1
    return 0


def cmd_list():
    for st in targets():
        print(_line(st))
    return 0


def cmd_selftest():
    """判据非空：在 script/ 下造两类缺陷夹具，断言对应判据命中；再断言真实仓库两件 PASS。"""
    fix = REPO / SELFTEST_REL
    shutil.rmtree(fix, ignore_errors=True)
    fix.mkdir(parents=True, exist_ok=True)
    (fix / "ignored.json").write_text('{"fixture": 1}\n', encoding="utf-8", newline="\n")
    (fix / "untracked.md").write_text("# fixture\n", encoding="utf-8", newline="\n")

    cases = [
        ("F1 存在但被忽略（未跟踪）", "%s/ignored.json" % SELFTEST_REL, {"E2", "E3", "E4"}),
        ("F2 未被跟踪", "%s/untracked.md" % SELFTEST_REL, {"E2"}),
        ("F3 文件不存在", "%s/absent.json" % SELFTEST_REL, {"E1"}),
    ]
    ok = True
    print("=" * 72)
    print("判据非空自检：夹具须命中 E1／E2／E3／E4（预期 FAIL）")
    print("=" * 72)
    for title, rel, expect in cases:
        st = inspect(REPO, rel)
        got = set(st["fails"])
        hit = expect <= got
        ok = ok and hit
        print("  [%s] %s" % ("PASS" if hit else "FAIL", title))
        print("           期望 %s；实际 %s" % (sorted(expect), sorted(got) or "空"))
        if st["ignore_rule"]:
            print("           规则 %s" % st["ignore_rule"])

    print("-" * 72)
    print("正常仓库：两件镜像须四项全过（预期 PASS）")
    clean = True
    for st in targets():
        print(_line(st))
        clean = clean and not st["fails"]
    ok = ok and clean

    print("-" * 72)
    if ok:
        print("  ✅ 判据非空：E1／E2／E3／E4 均被夹具实测命中，真实镜像全过")
        return 0
    print("  ❌ 判据可能为空或镜像未达标", file=sys.stderr)
    return 1


def main():
    ap = argparse.ArgumentParser(description="大纲目录镜像派生件入库白名单校验（第二十五件）")
    ap.add_argument("--check", action="store_true", help="默认模式：四项判据校验两件镜像")
    ap.add_argument("--list", action="store_true", help="打印两件镜像的四项状态")
    ap.add_argument("--selftest", action="store_true", help="判据非空自检（script/ 下夹具）")
    args = ap.parse_args()

    try:
        if _git(["--version"], REPO).returncode != 0:
            raise OSError
    except OSError:
        print("依赖缺失：git 不可用", file=sys.stderr)
        return 2

    if args.selftest:
        return cmd_selftest()
    if args.list:
        return cmd_list()
    return cmd_check()


if __name__ == "__main__":
    sys.exit(main())
