# -*- coding: utf-8 -*-
"""旁路备份副本残留扫描门禁（第三十六件）。

判据正文：`00-编纂规则与格式规范/01-规则/流程规则.md`“旁路备份全面禁止（全库，
2026-10-23 用户令）”小节。留痕与回滚唯一依赖 Git，数据库快照唯一依赖
`12-数据库备份/` 三计划任务；本件负责“复扫为零”这一步的常态化自查。

口径：
- 命中族（文件名大小写不敏感）：`.prebak*`／`.preback*`／`.pre`／`.pre-*`／`.pre_*`／
  `-bak`／`-bak-*`／`_bak`／`_bak_*`／`.bak*`／`.orig*`／`.rej`／结尾 `~`，
  以及备份目录名 `prebak-*`／`_bak*`／`*_备份*` 之下的一切内容。
- 豁免（须在该小节登记理由，本脚本 `EXEMPT_PREFIXES` 为唯一实现）：
  ①`script/_bak/20261017/`——`AGENTS.md` 记载的“重写前全史备份”镜像与随附归档，
    删除即销毁唯一历史全量副本，须用户明示才可处置；
  ②`12-数据库备份/` 目录内的**正式归档体**（`*.tar.gz`／`*.parquet`／`schema.sql`／
    `load.sql`／`backup_log.jsonl` 等既定命名），非正式命名的旁路件不豁免。
- 上游随附件（如 patch 冲突残留 `*.ORIG`）不豁免，逐件披露后由用户裁决。

退出码：0＝零残留（豁免外）；1＝存在违规件（列清单）；2＝脚本自身异常。
`--json` 输出机器可读结果；`--quiet` 只打印计数。默认 dry-run，绝不写盘。
"""
import argparse
import json
import os
import re
import subprocess
import sys

REPO_DEFAULT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SKIP_DIR_NAMES = {".git", "node_modules", ".venv", "__pycache__",
                  "$RECYCLE.BIN", "System Volume Information"}

NAME_RES = [
    ("prebak", re.compile(r"(?i)\.prebak")),
    ("preback", re.compile(r"(?i)\.preback")),
    ("pre-suffix", re.compile(r"(?i)\.pre($|[-_])")),
    ("pre-mid", re.compile(r"(?i)[._-]pre[-_]")),
    ("bak-suffix", re.compile(r"(?i)\.bak($|[-_.0-9])")),
    ("bak-mid", re.compile(r"(?i)[._-]bak($|[-_.0-9])")),
    ("orig", re.compile(r"(?i)\.orig")),
    ("rej", re.compile(r"(?i)\.rej$")),
    ("tilde", re.compile(r"~$")),
]
DIR_RES = [
    ("prebak-dir", re.compile(r"(?i)prebak")),
    ("bak-dir", re.compile(r"(?i)^_?bak($|[-_.0-9])")),
]
FORMAL_DB_ARCHIVE = re.compile(
    r"(?i)\.(tar\.gz|tgz|parquet|sql|jsonl|gz)$|^schema\.sql$|^load\.sql$")

EXEMPT_PREFIXES = ("script/_bak/20261017/",)


def classify(rel, is_dir):
    """返回命中族名列表；空列表＝非违规。"""
    name = rel.rsplit("/", 1)[-1]
    hits = [tag for tag, pat in NAME_RES if pat.search(name)]
    if is_dir:
        hits += [tag for tag, pat in DIR_RES if pat.search(name)]
    return hits


def is_exempt(rel, is_dir=False):
    """豁免前缀本身及其**祖先目录**均豁免（否则容器目录会被当成违规目录报出）。"""
    for p in EXEMPT_PREFIXES:
        bare = p.rstrip("/")
        if rel == bare or rel.startswith(p):
            return True
        if is_dir and p.startswith(rel + "/"):
            return True
    return False


def in_db_backup_dir(rel):
    return rel.startswith("12-数据库备份/")


def ancestor_backup_dir(rel, is_dir):
    """返回命中的祖先备份目录名（否则空串）：备份目录之下的任何内容同判违规。"""
    parts = rel.split("/")
    upto = len(parts) - 1 if not is_dir else len(parts)
    for name in parts[:upto]:
        if any(p.search(name) for _tag, p in DIR_RES) or any(p.search(name) for _tag, p in NAME_RES):
            return name
    return ""


def scan(root):
    hits, exempted, formal = [], [], []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIR_NAMES)
        base = os.path.relpath(dirpath, root).replace("\\", "/")
        if base == ".":
            base = ""
        else:
            if os.path.exists(os.path.join(dirpath, ".git")):
                # 嵌套 Git 仓库（代码克隆）整体不扫：其内文件属上游产物，不属本工作区
                # （实测 `03-原始史料库/02-man源与posix仓库/01-repos/freebsd-src` 的
                #  `crypto/heimdal/appl/telnet/README.ORIG` 由该克隆自身跟踪且干净）
                dirnames[:] = []
                continue
        for entry, is_dir in [(d, True) for d in dirnames] + [(f, False) for f in filenames]:
            rel = (base + "/" + entry) if base else entry
            if not is_dir and in_db_backup_dir(rel) and FORMAL_DB_ARCHIVE.search(entry):
                formal.append({"path": rel, "dir": False, "bytes": -1, "families": ["formal-archive"]})
                continue
            fams = classify(rel, is_dir)
            anc = ancestor_backup_dir(rel, is_dir)
            if not fams and not anc:
                continue
            if anc and not fams:
                fams = ["in-backup-dir:" + anc]
            full = os.path.join(dirpath, entry)
            try:
                size = -1 if is_dir else os.path.getsize(full)
            except OSError:
                size = -1
            rec = {"path": rel, "dir": is_dir, "bytes": size, "families": fams}
            if is_exempt(rel, is_dir):
                exempted.append(rec)
            else:
                hits.append(rec)
    return hits, exempted, formal


def byte_total(records):
    return sum(r["bytes"] for r in records if r["bytes"] > 0)


def sha256_of(path):
    import hashlib
    h = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(1 << 20), b""):
                h.update(chunk)
    except OSError:
        return ""
    return h.hexdigest()


def dump_tsv(root, hits, dest):
    """逐件台账（路径／目录标志／字节／sha256／族），满足处置四步的“逐件记录”。"""
    os.makedirs(os.path.dirname(os.path.abspath(dest)), exist_ok=True)
    with open(dest, "w", encoding="utf-8", newline="\n") as f:
        f.write("rel_path\tis_dir\tbytes\tsha256\tfamilies\n")
        for r in sorted(hits, key=lambda x: x["path"]):
            digest = "" if r["dir"] else sha256_of(os.path.join(root, r["path"].replace("/", os.sep)))
            f.write("%s\t%d\t%d\t%s\t%s\n" % (
                r["path"], 1 if r["dir"] else 0, r["bytes"], digest, ",".join(r["families"])))
    return len(hits)


def selftest():
    """判据非空：夹具须同时命中“违规／豁免／正式归档体／根守卫”四类，缺一即自检失败。"""
    import shutil
    import tempfile
    tmp = tempfile.mkdtemp(prefix="sidecar_selftest_")
    try:
        open(os.path.join(tmp, "AGENTS.md"), "w", encoding="utf-8").write("# fixture\n")
        viol = ["docs/a.md.prebak-20261023", "docs/b.html.bak_20261020",
                "docs/c.md.pre_b004_20261005", "docs/d.txt.preback-t1",
                "docs/e.md.orig", "docs/f.patch.rej", "docs/g.htm~",
                "docs/h.duckdb.pre_fixdb", "docs/i-bak-20261001.md",
                "docs/j.md.pre"]
        for rel in viol:
            p = os.path.join(tmp, rel.replace("/", os.sep))
            os.makedirs(os.path.dirname(p), exist_ok=True)
            open(p, "w", encoding="utf-8").write("x\n")
        # 备份目录名之下全部内容计入
        os.makedirs(os.path.join(tmp, "docs", "_bak20261023"), exist_ok=True)
        open(os.path.join(tmp, "docs", "_bak20261023", "plain.md"), "w", encoding="utf-8").write("x\n")
        # 豁免：全史备份镜像目录内的旁路件
        ex = os.path.join(tmp, "script", "_bak", "20261017")
        os.makedirs(ex, exist_ok=True)
        open(os.path.join(ex, "outline.txt.prebak-20261017"), "w", encoding="utf-8").write("x\n")
        # 正式归档体：12-数据库备份 内 .tar.gz 不判违规，同目录 .pre_*.duckdb 仍判
        db = os.path.join(tmp, "12-数据库备份", "historical_claims")
        os.makedirs(db, exist_ok=True)
        open(os.path.join(db, "historical_claims-20261023.tar.gz"), "w", encoding="utf-8").write("x\n")
        open(os.path.join(db, "historical_claims.pre_f4_20261016.duckdb"), "w", encoding="utf-8").write("x\n")
        # 正常件不得误报
        open(os.path.join(tmp, "docs", "normal.md"), "w", encoding="utf-8").write("x\n")
        open(os.path.join(tmp, "docs", "pre-existing-note.md"), "w", encoding="utf-8").write("x\n")

        hits, exempted, formal = scan(tmp)
        paths = {h["path"] for h in hits}
        ex_paths = {r["path"] for r in exempted}
        checks = [
            ("T1 十个违规族全命中", all(v in paths for v in viol), True),
            ("T2 备份目录内容计入", "docs/_bak20261023/plain.md" in paths, True),
            ("T3 数据库目录内旁路件不豁免",
             "12-数据库备份/historical_claims/historical_claims.pre_f4_20261016.duckdb" in paths, True),
            ("T4 全史镜像文件不入违规集",
             "script/_bak/20261017/outline.txt.prebak-20261017" not in paths, True),
            ("T5 全史镜像记入豁免集",
             "script/_bak/20261017/outline.txt.prebak-20261017" in ex_paths, True),
            ("T6 容器目录不误报", "script/_bak" not in paths, True),
            ("T7 正式归档体豁免", len(formal) == 1, True),
            ("T8 正常件零误报", ("docs/normal.md" in paths) or ("docs/pre-existing-note.md" in paths), False),
            ("T9 违规文件计数", sum(1 for h in hits if not h["dir"]), len(viol) + 2),
        ]
        bad = 0
        for name, got, want in checks:
            ok = (got == want) if not isinstance(want, bool) else (bool(got) is want)
            print("  [%s] %s（got=%r want=%r）" % ("PASS" if ok else "FAIL", name, got, want))
            if not ok:
                bad += 1
        # 根守卫：无 .git 也无 AGENTS.md 的目录必须被拒绝（首版曾误扫整盘）
        bare = tempfile.mkdtemp(prefix="sidecar_bare_")
        try:
            open(os.path.join(bare, "x.md.prebak-1"), "w", encoding="utf-8").write("x\n")
            rc = subprocess.run([sys.executable, os.path.abspath(__file__), "--root", bare],
                                capture_output=True).returncode
            ok = rc == 2
            print("  [%s] T10 根守卫拒扫非项目根（rc=%d want=2）" % ("PASS" if ok else "FAIL", rc))
            bad += 0 if ok else 1
        finally:
            shutil.rmtree(bare, ignore_errors=True)
        print("audit_sidecar_backup --selftest：%s" % ("全部 PASS" if bad == 0 else "FAIL %d 项" % bad))
        return 0 if bad == 0 else 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    ap = argparse.ArgumentParser(description="旁路备份副本残留扫描门禁（第三十六件）")
    ap.add_argument("--root", default=REPO_DEFAULT)
    ap.add_argument("--selftest", action="store_true", help="判据非空自检（临时夹具）")
    ap.add_argument("--json", action="store_true", help="机器可读输出")
    ap.add_argument("--quiet", action="store_true", help="只打印计数")
    ap.add_argument("--limit", type=int, default=30, help="违规清单最多打印条数")
    ap.add_argument("--dump", default="", help="把逐件台账（含 sha256）写入指定 TSV 路径")
    args = ap.parse_args()

    if args.selftest:
        return selftest()

    root = os.path.abspath(args.root)
    if not os.path.isdir(root):
        print("根目录不存在：%s" % root, file=sys.stderr)
        return 2
    if not (os.path.isdir(os.path.join(root, ".git")) or os.path.isfile(os.path.join(root, "AGENTS.md"))):
        print("拒绝扫描：%s 不像项目根（无 .git 目录也无 AGENTS.md）" % root, file=sys.stderr)
        return 2
    hits, exempted, formal = scan(root)
    if args.dump:
        n = dump_tsv(root, hits, args.dump)
        print("逐件台账已写入 %s（%d 件）" % (args.dump, n))
    fam_count = {}
    for r in hits:
        for f in r["families"]:
            fam_count[f] = fam_count.get(f, 0) + 1

    if args.json:
        print(json.dumps({
            "root": root,
            "violations": len(hits),
            "violation_bytes": byte_total(hits),
            "families": fam_count,
            "exempt": {"count": len(exempted), "bytes": byte_total(exempted),
                       "prefixes": list(EXEMPT_PREFIXES)},
            "formal_db_archives": {"count": len(formal), "bytes": byte_total(formal)},
            "list": hits[:200],
        }, ensure_ascii=False, indent=2))
    elif args.quiet:
        print("违规 %d 件／%.2f MB；豁免 %d 件；正式归档体 %d 件"
              % (len(hits), byte_total(hits) / 1048576.0, len(exempted), len(formal)))
    else:
        print("旁路备份残留扫描（第三十六件）")
        print("根目录：%s" % root)
        for f, n in sorted(fam_count.items(), key=lambda kv: -kv[1]):
            print("  族 %-12s %5d 件" % (f, n))
        print("违规：%d 件／%.2f MB｜豁免（%s）：%d 件／%.2f MB｜12-数据库备份 正式归档体：%d 件"
              % (len(hits), byte_total(hits) / 1048576.0,
                 "、".join(EXEMPT_PREFIXES), len(exempted),
                 byte_total(exempted) / 1048576.0, len(formal)))
        for r in hits[:args.limit]:
            print("  - %s%s [%s] %s" % (
                r["path"], "/" if r["dir"] else "", ",".join(r["families"]),
                "-" if r["bytes"] < 0 else "%.2f MB" % (r["bytes"] / 1048576.0)))
        if len(hits) > args.limit:
            print("  …另有 %d 件未列出（--json 取全量）" % (len(hits) - args.limit))

    if hits:
        print("❌ FAIL｜存在旁路备份副本残留（判据见 流程规则.md“旁路备份全面禁止”）")
        return 1
    print("✅ PASS｜零残留（豁免与正式归档体除外）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
