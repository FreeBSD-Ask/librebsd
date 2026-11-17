# -*- coding: utf-8 -*-
"""里程碑标签台账门禁（第四十六件，2026-11-17 立；G-01 偿还）。

对象：仓库 annotated tag 集合 ↔ `01-项目管理/02-工程决策与技术债/里程碑标签台账.tsv`（唯一台账）。
判据：
  T1 台账覆盖双向相等——git tag 集合 == 台账 tag 列（缺行／多行均 FAIL）；
  T2 台账 target_sha 在仓库中可解析（`git cat-file -e <sha>`）；
  T3 台账 target_sha == 该 tag **当前**指向的提交（检测 tag 被移动／force 改写）；
  T4 新增 lightweight：tag 提交日期 ≥ CUTOFF 且对象类型非 tag → FAIL；存量 lightweight → WARN；
  T5 命名形态 `<项目>-<状态>-<YYYYMMDD>`；存量旧代命名 → WARN（不回改历史）。
用法：
  python audit_tag_ledger.py --check              # 判据（FAIL 即 exit 1）
  python audit_tag_ledger.py --dump               # 由 git 生成／补齐台账（只增不改；幂等）
  python audit_tag_ledger.py --selftest           # 判据非空自检（临时 git 仓库夹具）
  python audit_tag_ledger.py --list               # 打印台账摘要
退出码：0 无 FAIL／1 有 FAIL／2 致命（git 不可用、台账缺失）。
"""
import argparse
import datetime as _dt
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

sys.stdout.reconfigure(encoding="utf-8")

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[2]
LEDGER = REPO / "01-项目管理" / "02-工程决策与技术债" / "里程碑标签台账.tsv"
CUTOFF = "2026-11-17"          # 本门禁立件日：此后新增 tag 一律 annotated
NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]*-[a-z0-9-]*-\d{8}$")
HEADER = "tag\tobject_type\ttarget_sha\tcommit_date\tsubject\n"


def _git(args, cwd=None):
    return subprocess.run(["git"] + args, cwd=str(cwd or REPO),
                          capture_output=True, text=True, encoding="utf-8", errors="replace")


def collect_tags(root):
    """返回 {tag: dict(type, target, date, subject)}；target 为 tag 指向的提交 sha。"""
    r = _git(["for-each-ref", "refs/tags",
              "--format=%(refname:short)\t%(objecttype)\t%(*objectname)\t%(objectname)"], root)
    if r.returncode != 0:
        return None
    out = {}
    for line in r.stdout.splitlines():
        if not line.strip():
            continue
        name, otype, peeled, obj = (line.split("\t") + ["", "", ""])[:4]
        target = peeled or obj
        info = _git(["log", "-1", "--format=%cs\t%s", target], root)
        date, subject = (info.stdout.rstrip("\n").split("\t", 1) + [""])[:2] if info.returncode == 0 else ("", "")
        out[name] = dict(type=otype, target=target, date=date, subject=subject)
    return out


def read_ledger(path):
    if not path.exists():
        return None
    rows = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("tag\t"):
            continue
        parts = line.split("\t")
        if len(parts) < 3:
            continue
        rows[parts[0]] = dict(type=parts[1], target=parts[2],
                              date=parts[3] if len(parts) > 3 else "",
                              subject=parts[4] if len(parts) > 4 else "")
    return rows


def cmd_dump():
    tags = collect_tags(REPO)
    if tags is None:
        print("[exit 2] git 不可用")
        return 2
    rows = read_ledger(LEDGER) or {}
    added = [t for t in sorted(tags) if t not in rows]
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    if not LEDGER.exists():
        LEDGER.write_text(HEADER, encoding="utf-8", newline="\n")
    with open(LEDGER, "a", encoding="utf-8", newline="\n") as f:
        for t in added:
            d = tags[t]
            f.write("%s\t%s\t%s\t%s\t%s\n" % (t, d["type"], d["target"], d["date"], d["subject"]))
    print("台账：新增 %d 行，共 %d 行（只增不改；sha 变更请人工核对，勿静默覆盖）"
          % (len(added), len(rows) + len(added)))
    return 0


def cmd_list():
    rows = read_ledger(LEDGER)
    if rows is None:
        print("台账缺失：%s" % LEDGER)
        return 2
    by_type = {}
    for t, d in rows.items():
        by_type[d["type"]] = by_type.get(d["type"], 0) + 1
    print("台账行数 %d｜对象类型 %s" % (len(rows), by_type))
    for t in sorted(rows)[:10]:
        print("  %-40s %s %s" % (t, rows[t]["type"], rows[t]["target"][:10]))
    return 0


def run_checks(root=REPO, ledger=LEDGER, cutoff=CUTOFF, verbose=True):
    fails, warns = [], []
    tags = collect_tags(root)
    if tags is None:
        return None, None, "git 不可用"
    rows = read_ledger(ledger)
    if rows is None:
        return None, None, "台账缺失：%s（先跑 --dump）" % ledger

    # T1 双向覆盖
    miss = sorted(set(tags) - set(rows))
    extra = sorted(set(rows) - set(tags))
    if miss:
        fails.append("T1 tag 未入台账 %d 个：%s" % (len(miss), miss[:5]))
    if extra:
        fails.append("T1 台账含不存在的 tag %d 个：%s" % (len(extra), extra[:5]))

    for t in sorted(set(tags) & set(rows)):
        d, r = tags[t], rows[t]
        # T2 sha 可解析
        if _git(["cat-file", "-e", r["target"] + "^{commit}"], root).returncode != 0:
            fails.append("T2 台账 target 不可解析：%s -> %s" % (t, r["target"][:12]))
        # T3 未被移动
        elif r["target"] != d["target"]:
            fails.append("T3 tag 指向与台账不符（疑似移动／force）：%s 台账=%s 现=%s"
                         % (t, r["target"][:12], d["target"][:12]))
        # T4 lightweight
        if d["type"] != "tag":
            if d["date"] and d["date"] >= cutoff:
                fails.append("T4 新增 lightweight tag（应 annotated）：%s（%s）" % (t, d["date"]))
            else:
                warns.append("T4 存量 lightweight：%s" % t)
        # T5 命名
        if not NAME_RE.match(t):
            warns.append("T5 旧代命名（不回改）：%s" % t)

    if verbose:
        print("=" * 72)
        print("里程碑标签台账门禁（第四十六件；G-01）")
        print("=" * 72)
        print("tag 总数 %d｜台账 %d 行｜annotated %d｜lightweight %d"
              % (len(tags), len(rows),
                 sum(1 for d in tags.values() if d["type"] == "tag"),
                 sum(1 for d in tags.values() if d["type"] != "tag")))
        for w in warns:
            print("  WARN " + w)
        for f in fails:
            print("  FAIL " + f)
        print("判定：%s（FAIL %d／WARN %d）" % ("PASS" if not fails else "FAIL", len(fails), len(warns)))
    return fails, warns, None


def _init_tmp_repo(td):
    p = pathlib.Path(td)
    env = dict(os.environ, GIT_AUTHOR_DATE="2026-11-17T10:00:00",
               GIT_COMMITTER_DATE="2026-11-17T10:00:00")
    def g(*a):
        subprocess.run(["git"] + list(a), cwd=str(p), check=True,
                       capture_output=True, env=env)
    g("init", "-q")
    g("config", "user.email", "t@t")
    g("config", "user.name", "t")
    (p / "a.txt").write_text("x", encoding="utf-8")
    g("add", "a.txt")
    g("commit", "-q", "-m", "init")
    g("tag", "-a", "proj-alpha-20261117", "-m", "milestone")
    return p


def cmd_selftest():
    ok = True
    td = tempfile.mkdtemp(prefix="tagledger_")
    try:
        p = _init_tmp_repo(td)
        led = pathlib.Path(td) / "ledger.tsv"
        tags = collect_tags(p)
        sha = tags["proj-alpha-20261117"]["target"]
        # 正例
        led.write_text(HEADER + "proj-alpha-20261117\ttag\t%s\t2026-11-17\tmilestone\n" % sha,
                       encoding="utf-8", newline="\n")
        f, w, err = run_checks(p, led, verbose=False)
        print("[%s] 正例：FAIL=%d（期望 0）" % ("PASS" if not f else "FAIL", len(f)))
        ok &= not f
        # T1 缺行
        led.write_text(HEADER, encoding="utf-8", newline="\n")
        f, w, err = run_checks(p, led, verbose=False)
        hit = any(x.startswith("T1 tag 未入台账") for x in f or [])
        print("[%s] 负例 T1 缺行：%s" % ("PASS" if hit else "FAIL", f[:1]))
        ok &= hit
        # T3／T2：台账写一个不可解析 sha → 触发 T2
        led.write_text(HEADER + "proj-alpha-20261117\ttag\t%s\t2026-11-17\tmilestone\n" % ("0" * 40),
                       encoding="utf-8", newline="\n")
        f, w, err = run_checks(p, led, verbose=False)
        hit = any(x.startswith("T2 台账 target 不可解析") for x in f or [])
        print("[%s] 负例 T2 sha 不可解析：%s" % ("PASS" if hit else "FAIL", f[:1]))
        ok &= hit
        # T4 新增 lightweight
        subprocess.run(["git", "tag", "proj-beta-20261118"], cwd=str(p), check=True,
                       capture_output=True)
        led.write_text(HEADER
                       + "proj-alpha-20261117\ttag\t%s\t2026-11-17\tmilestone\n" % sha
                       + "proj-beta-20261118\ttag\t%s\t2026-11-17\tinit\n" % sha,
                       encoding="utf-8", newline="\n")
        f, w, err = run_checks(p, led, cutoff="2026-11-17", verbose=False)
        hit = any(x.startswith("T4 新增 lightweight") for x in f or [])
        print("[%s] 负例 T4 lightweight：%s" % ("PASS" if hit else "FAIL", f[:1]))
        ok &= hit
    finally:
        shutil.rmtree(td, ignore_errors=True)
    print("自检：%s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description="第四十六件：里程碑标签台账门禁（G-01）")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--check", action="store_true", help="判据（默认动作）")
    g.add_argument("--dump", action="store_true", help="由 git 生成／补齐台账（只增不改）")
    g.add_argument("--selftest", action="store_true", help="判据非空自检")
    g.add_argument("--list", action="store_true", help="台账摘要")
    a = ap.parse_args()
    if shutil.which("git") is None:
        print("[exit 2] git 不可用")
        return 2
    if a.selftest:
        return cmd_selftest()
    if a.dump:
        return cmd_dump()
    if a.list:
        return cmd_list()
    fails, warns, err = run_checks()
    if err:
        print("[exit 2] " + err)
        return 2
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
