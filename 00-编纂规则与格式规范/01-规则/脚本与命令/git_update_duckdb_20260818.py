# -*- coding: utf-8 -*-
"""git 增量更新直接写入 DuckDB 主库（15 登记库，规则：不经过 SQLite 中转）

规则来源：流程规则.md“DuckDB 分析层与主存储层规则”“Git 克隆目录与更新规则”
架构：tree:0 克隆仅提交信息 → git log 解析 → INSERT 直接入 DuckDB → --optimize
"""
import datetime
import json
import os
import re
import shutil
import subprocess
import sys
import time

import duckdb

BASE = r"d:\librebsd"
CODE = os.path.join(BASE, "03-原始史料库", "01-代码仓库史料")
STATE = os.path.join(BASE, "script", "_git_update_duckdb_state.jsonl")
LOG = os.path.join(BASE, "script", "_duckdb_sync_log.jsonl")
FIXED = os.path.join(BASE, "00-编纂规则与格式规范", "01-规则", "脚本与命令", "sqlite2duckdb.py")
BACKUP_ROOT = os.path.join(BASE, "12-数据库备份")
GH = "https://github.com"
AP = "apple-oss-distributions"

# 15 登记库：db_name -> (folder, repo_list)
PLAN = {
    "darwin": ("09-Darwin", [
        ("xnu", f"{GH}/{AP}/xnu"), ("autofs", f"{GH}/{AP}/autofs"), ("bash", f"{GH}/{AP}/bash"),
        ("bootp", f"{GH}/{AP}/bootp"), ("cctools", f"{GH}/{AP}/cctools"), ("CF", f"{GH}/{AP}/CF"),
        ("cups", f"{GH}/{AP}/cups"), ("dtrace", f"{GH}/{AP}/dtrace"), ("dyld", f"{GH}/{AP}/dyld"),
        ("EAP8021X", f"{GH}/{AP}/EAP8021X"), ("hfs", f"{GH}/{AP}/hfs"),
        ("IOGraphics", f"{GH}/{AP}/IOGraphics"), ("IOSerialFamily", f"{GH}/{AP}/IOSerialFamily"),
        ("IOStorageFamily", f"{GH}/{AP}/IOStorageFamily"), ("IOUSBFamily", f"{GH}/{AP}/IOUSBFamily"),
        ("kext_tools", f"{GH}/{AP}/kext_tools"), ("ld64", f"{GH}/{AP}/ld64"), ("Libc", f"{GH}/{AP}/Libc"),
        ("libclosure", f"{GH}/{AP}/libclosure"), ("libdispatch", f"{GH}/{AP}/libdispatch"),
        ("libpcap", f"{GH}/{AP}/libpcap"), ("libpthread", f"{GH}/{AP}/libpthread"),
        ("libsecurity_cdsa_client", f"{GH}/{AP}/libsecurity_cdsa_client"),
        ("libsecurity_cdsa_plugin", f"{GH}/{AP}/libsecurity_cdsa_plugin"),
        ("libsecurity_keychain", f"{GH}/{AP}/libsecurity_keychain"),
        ("libsecurity_pkcs12", f"{GH}/{AP}/libsecurity_pkcs12"),
        ("libsecurity_ssl", f"{GH}/{AP}/libsecurity_ssl"),
        ("mDNSResponder", f"{GH}/{AP}/mDNSResponder"), ("msdosfs", f"{GH}/{AP}/msdosfs"),
        ("objc4", f"{GH}/{AP}/objc4"), ("openssl", f"{GH}/{AP}/openssl"), ("perl", f"{GH}/{AP}/perl"),
        ("ppp", f"{GH}/{AP}/ppp"), ("python", f"{GH}/{AP}/python"), ("rsync", f"{GH}/{AP}/rsync"),
        ("Security", f"{GH}/{AP}/Security"), ("SecurityTool", f"{GH}/{AP}/SecurityTool"),
        ("SmartCardServices", f"{GH}/{AP}/SmartCardServices"), ("tcpdump", f"{GH}/{AP}/tcpdump"),
        ("vim", f"{GH}/{AP}/vim"), ("webdavfs", f"{GH}/{AP}/webdavfs"), ("zsh", f"{GH}/{AP}/zsh"),
    ]),
    "openssh": ("08-跨项目对比", [("openssh", f"{GH}/openssh/openssh-portable")]),
    "openssh-apple": ("08-跨项目对比", [("openssh", f"{GH}/{AP}/openssh")]),
    "openzfs": ("06-OpenZFS", [("openzfs-zfs", f"{GH}/openzfs/zfs")]),
    "illumos-gate": ("08-跨项目对比", [("illumos-gate", f"{GH}/illumos/illumos-gate")]),
    "dragonfly": ("05-DragonFlyBSD", [
        ("dragonfly-src", f"{GH}/DragonFlyBSD/DragonFlyBSD"),
        ("dragonfly-dports", f"{GH}/DragonFlyBSD/DPorts"),
        ("dragonfly-docs", f"{GH}/DragonFlyBSD/docs.dragonflybsd.org"),
    ]),
    "openbsd": ("04-OpenBSD", [
        ("openbsd-src", f"{GH}/openbsd/src"), ("openbsd-ports", f"{GH}/openbsd/ports"),
        ("openbsd-www", f"{GH}/openbsd/www"),
    ]),
    "bsd-derivatives": ("07-BSD衍生项目", [
        ("ghostbsd-src", f"{GH}/ghostbsd/ghostbsd-src"),
        ("hardenedbsd-src", f"{GH}/HardenedBSD/hardenedBSD"),
        ("midnightbsd-mports", f"{GH}/MidnightBSD/mports"),
        ("midnightbsd-src", f"{GH}/MidnightBSD/src"),
        ("opnsense-core", f"{GH}/opnsense/core"),
        ("pfsense-src", f"{GH}/pfsense/FreeBSD-src"),
        ("truenas-middleware", f"{GH}/truenas/middleware"),
        ("trueos-src", f"{GH}/trueos/trueos"),
    ]),
    "netbsd": ("03-NetBSD", [
        ("netbsd-src", f"{GH}/NetBSD/src"), ("netbsd-pkgsrc", f"{GH}/NetBSD/pkgsrc"),
    ]),
    "freebsd": ("02-FreeBSD", [
        ("freebsd-src", f"{GH}/freebsd/freebsd-src"), ("freebsd-doc", f"{GH}/freebsd/freebsd-doc"),
        ("freebsd-ports", f"{GH}/freebsd/freebsd-ports"),
    ]),
    "linux-kernel": ("10-LinuxKernel", [("linux-kernel", f"{GH}/torvalds/linux")]),
}

# 镜像重建白名单
REINGEST_ALLOW = {"trueos-src", "netbsd-src", "openssh-apple/openssh"}
PRETTY = "%x01%H%x02%an%x02%ae%x02%aI%x02%cn%x02%ce%x02%cI%x02%P%x02%s%x02%b"
SOB_RE = re.compile(r"^Signed-off-by:\s*(.+)$", re.MULTILINE)

sys.stdout.reconfigure(encoding="utf-8")


def log(msg):
    print("[{}] {}".format(datetime.datetime.now().strftime("%H:%M:%S"), msg), flush=True)


def duck_path(db):
    folder = PLAN[db][0]
    return os.path.join(CODE, folder, "db", "duckdb", db + ".duckdb")


def clone_path(db, repo):
    folder = PLAN[db][0]
    return os.path.join(CODE, folder, repo + ".git")


def run_git(args, cwd=None):
    return subprocess.run(["git"] + args, cwd=cwd, capture_output=True)


def ensure_clone(db, repo, url):
    cdir = clone_path(db, repo)
    if os.path.isdir(cdir) and os.path.exists(os.path.join(cdir, "HEAD")):
        return cdir
    os.makedirs(os.path.dirname(cdir), exist_ok=True)
    t0 = time.time()
    r = subprocess.run(
        ["git", "clone", "--bare", "--single-branch", "--filter=tree:0", "--progress", url, cdir],
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        tail = (r.stderr or "")[-300:]
        log("  克隆失败 {} {}: {}".format(db, repo, tail.replace("\r", " ")))
        if os.path.isdir(cdir):
            shutil.rmtree(cdir, ignore_errors=True)
        return None
    log("  克隆完成 {} {} {:.0f}s".format(db, repo, time.time() - t0))
    return cdir


def since_str(iso):
    return (datetime.datetime.fromisoformat(iso) - datetime.timedelta(days=7)).strftime("%Y-%m-%dT%H:%M:%S")


def update_repo(db, repo, url, dk):
    cur = dk.cursor()
    row = cur.execute(
        "SELECT commit_hash, committer_date FROM commits WHERE repo_name=? "
        "ORDER BY committer_date DESC LIMIT 1", (repo,)).fetchone()
    if not row:
        return "skip", "库内无该 repo 存量记录"
    known_hash, boundary = row
    cdir = ensure_clone(db, repo, url)
    if not cdir:
        return "error", "克隆失败"
    r = run_git(["cat-file", "-e", known_hash + "^{commit}"], cwd=cdir)
    reingest = False
    if r.returncode != 0:
        anchor = None
        for h, dt in cur.execute(
                "SELECT commit_hash, committer_date FROM commits WHERE repo_name=? "
                "ORDER BY committer_date DESC LIMIT 300", (repo,)).fetchall():
            rr = run_git(["cat-file", "-e", h + "^{commit}"], cwd=cdir)
            if rr.returncode == 0:
                anchor = (h, dt)
                break
        if anchor:
            known_hash, boundary = anchor
            log("  {}/{} 边界锚点降级至 {}".format(db, repo, boundary[:10]))
        else:
            n_all = run_git(["rev-list", "--all", "--count"], cwd=cdir)
            n_str = n_all.stdout.decode().strip() if n_all.returncode == 0 else ""
            existing = cur.execute("SELECT count(*) FROM commits WHERE repo_name=?", (repo,)).fetchone()[0]
            allow_big = repo in REINGEST_ALLOW
            ok_small = n_str.isdigit() and 0 < int(n_str) <= 2000 and int(n_str) >= existing // 2
            ok_big = allow_big and n_str.isdigit() and int(n_str) > 0
            if ok_small or ok_big:
                reingest = True
                log("  {}/{} 进入全量重灌（克隆 {} 提交，存量 {}）".format(db, repo, n_str, existing))
            else:
                return "error", "锚点全不可达，克隆 {} 提交（存量 {}），拒绝".format(n_str or "?", existing)
    existing = {h for (h,) in cur.execute("SELECT commit_hash FROM commits WHERE repo_name=?", (repo,)).fetchall()}
    if reingest:
        dk.execute("BEGIN TRANSACTION")
        dk.execute("DELETE FROM commits WHERE repo_name=?", (repo,))
        dk.execute("COMMIT")
        existing = set()
        since_arg = ["--all"]
        boundary_note = "全量重灌"
    else:
        since_arg = ["--all", "--since=" + since_str(boundary)]
        boundary_note = boundary[:10]
    r = run_git(["rev-list"] + since_arg, cwd=cdir)
    if r.returncode != 0:
        return "error", "rev-list 失败"
    cand = set(r.stdout.decode().split())
    new_hashes = cand - existing
    if not new_hashes:
        return "uptodate", "无新提交（边界 {}）".format(boundary[:10])
    r = subprocess.run(
        ["git", "-c", "core.quotepath=false", "log"] + since_arg +
        ["--date=iso-strict", "--pretty=format:" + PRETTY], cwd=cdir, capture_output=True)
    if r.returncode != 0:
        return "error", "git log 失败"
    text = r.stdout.decode("utf-8", "replace")
    rows = []
    for block in text.split("\n\x01")[1:]:
        lines = block.split("\n")
        head = lines[0].split("\x02")
        if len(head) < 10:
            continue
        h = head[0]
        if h not in new_hashes:
            continue
        body = head[9] if len(head) > 9 else ""
        sob = ", ".join(SOB_RE.findall(body or ""))
        rows.append((h, repo, head[1], head[2], head[3], head[4], head[5], head[6],
                     head[8], head[9] if len(head) > 9 else "", head[7], sob))
    # 过滤已存在的哈希（用 reingest 清空后的 existing 或存量查询结果）
    rows = [r for r in rows if r[0] not in existing]
    if not rows:
        return "uptodate", "无新提交（边界 {}）".format(boundary[:10])
    dk.execute("BEGIN TRANSACTION")
    dk.executemany(
        "INSERT INTO commits (commit_hash,repo_name,author_name,author_email,"
        "author_date,committer_name,committer_email,committer_date,message_subject,"
        "message_body,parent_hashes,signed_off_by) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", rows)
    dk.execute("COMMIT")
    n_all = dk.execute("SELECT count(*) FROM commits WHERE repo_name=?", (repo,)).fetchone()[0]
    latest = dk.execute("SELECT max(committer_date) FROM commits WHERE repo_name=?", (repo,)).fetchone()[0]
    dk.execute("UPDATE repos SET commit_count=?, latest_commit_date=? WHERE repo_name=?", (n_all, latest, repo))
    return "ok", "{} commits（{}）".format(len(rows), boundary_note)


def optimize_db(db):
    """调用固定脚本优化（索引 + ANALYZE + manifest）"""
    r = subprocess.run([sys.executable, FIXED, "--optimize", "--db", db],
                       capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=BASE)
    for line in (r.stdout + r.stderr).strip().splitlines()[-3:]:
        log("  | " + line)
    return r.returncode == 0


def load_done():
    done = set()
    if os.path.exists(STATE):
        for line in open(STATE, encoding="utf-8"):
            try:
                r = json.loads(line)
                if r.get("status") in ("ok", "uptodate", "skip"):
                    done.add((r["db"], r["repo"]))
            except Exception:
                pass
    return done


def main():
    os.makedirs(os.path.dirname(STATE), exist_ok=True)
    done = load_done()
    log("断点：已完成 {} 个 (db,repo)".format(len(done)))
    state_f = open(STATE, "a", encoding="utf-8", newline="\n")
    for db in PLAN:
        folder, repos = PLAN[db]
        dp = duck_path(db)
        if not os.path.exists(dp):
            log("[skip] {} DuckDB 主库不存在".format(db))
            continue
        dk = duckdb.connect(dp)
        dk.execute("SET memory_limit='8GB'")
        all_ok, any_work = True, False
        for repo, url in repos:
            if (db, repo) in done:
                continue
            status, note = update_repo(db, repo, url, dk)
            rec = {"db": db, "repo": repo, "status": status, "note": note,
                   "ts": datetime.datetime.now().isoformat(timespec="seconds")}
            state_f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            state_f.flush()
            if status in ("ok", "uptodate", "skip"):
                done.add((db, repo))
            if status == "ok":
                any_work = True
            if status == "error":
                all_ok = False
            log("  [{}] {}/{}: {}".format(status, db, repo, note))
        dk.close()
        pending = [r for r, _ in repos if (db, r) not in done]
        if not pending and any_work and all_ok:
            log("{} 优化".format(db))
            optimize_db(db)
        elif pending:
            log("{} 尚有 {} 个未完成仓库，暂不优化".format(db, len(pending)))
    state_f.close()
    log("编排完成")


if __name__ == "__main__":
    main()