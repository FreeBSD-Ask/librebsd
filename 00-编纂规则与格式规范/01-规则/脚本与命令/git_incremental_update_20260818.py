# -*- coding: utf-8 -*-
"""git 数据库增量更新编排（2026-08-18）：11 库 66 仓库更新至 2026-08-17/最新。

流程（每库）：
  0. 更新前：现 DuckDB 主库移至 12-数据库备份/<db>/<TS>.preupdate.duckdb（pre-update 快照）
  1. bare --single-branch 克隆（script/_git_update_20260818/<db>/<repo>.git，可复用续跑）
  2. 门禁：库内该 repo 最新已知 commit_hash 须存在于克隆（防代理污染/错库）
  3. 边界 = max(committer_date)，--since=边界-7天，rev-list 得候选，减去库内已有 hash 得增量
  4. git log --numstat --name-status --no-renames -c core.quotepath=false 解析（日期 iso-strict）
  5. 事务 INSERT commits/commit_files + tags 增量（表存在时）+ repos/db_meta 回写
  6. 全库仓库完成后：sqlite2duckdb.py --db X 重建主库 → --optimize --db X
断点续跑：state.jsonl 记录已完成 (db, repo)；克隆目录复用。
说明：增量段使用 --no-renames（改名拆为 A+D，路径无歧义）；signed_off_by 多签以 ", " 连接。
"""
import datetime
import json
import os
import re
import shutil
import sqlite3
import subprocess
import sys
import time

BASE = r"d:\librebsd"
WORK = os.path.join(BASE, "script", "_git_update_20260818")
STATE = os.path.join(WORK, "state.jsonl")
FIXED = os.path.join(BASE, "00-编纂规则与格式规范", "01-规则", "脚本与命令", "sqlite2duckdb.py")
BACKUP_ROOT = os.path.join(BASE, "12-数据库备份")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
GH = "https://github.com"
AP = "apple-oss-distributions"

CODE = os.path.join(BASE, "03-原始史料库", "01-代码仓库史料")

# 全量重灌白名单（上游镜像整体重建、抽样 0/100 不可达，唯一更新途径即重灌）
# netbsd-src：GitHub 镜像 2025 年整体重建，tree:0 仅提交对象可传输
REINGEST_ALLOW = {"trueos-src", "netbsd-src"}

PLAN = {
    "darwin": ("09-Darwin", [
        *(("xnu", f"{GH}/{AP}/xnu"), ("autofs", f"{GH}/{AP}/autofs"), ("bash", f"{GH}/{AP}/bash"),
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
          ("vim", f"{GH}/{AP}/vim"), ("webdavfs", f"{GH}/{AP}/webdavfs"), ("zsh", f"{GH}/{AP}/zsh")),
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
        ("openbsd-src", f"{GH}/openbsd/src"),
        ("openbsd-ports", f"{GH}/openbsd/ports"),
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
        ("netbsd-src", f"{GH}/NetBSD/src"),
        ("netbsd-pkgsrc", f"{GH}/NetBSD/pkgsrc"),
    ]),
    "freebsd": ("02-FreeBSD", [
        ("freebsd-src", f"{GH}/freebsd/freebsd-src"),
        ("freebsd-doc", f"{GH}/freebsd/freebsd-doc"),
        ("freebsd-ports", f"{GH}/freebsd/freebsd-ports"),
    ]),
    "linux-kernel": ("10-LinuxKernel", [("linux-kernel", f"{GH}/torvalds/linux")]),
}

PRETTY = "%x01%H%x02%an%x02%ae%x02%aI%x02%cn%x02%ce%x02%cI%x02%P%x02%s%x02%b"
NUMSTAT_RE = re.compile(r"^(\d+|-)\t(\d+|-)\t(.+)$")
NAMESTAT_RE = re.compile(r"^([A-Z])[0-9]*\t(.+)$")
SOB_RE = re.compile(r"^Signed-off-by:\s*(.+)$", re.MULTILINE)


def log(msg):
    print("[{}] {}".format(datetime.datetime.now().strftime("%H:%M:%S"), msg), flush=True)


def db_path(db):
    folder = PLAN[db][0]
    return os.path.join(CODE, folder, "db", db + ".db")


def run_git(args, cwd=None, timeout=None):
    return subprocess.run(["git"] + args, cwd=cwd, capture_output=True, timeout=timeout)


def ensure_clone(db, repo, url):
    # 规则：克隆统一存放于代码仓库目录，优先复用既有克隆
    folder = PLAN[db][0]
    cdir = os.path.join(CODE, folder, repo + ".git")
    if os.path.isdir(cdir) and os.path.exists(os.path.join(cdir, "HEAD")):
        if db == "darwin":
            run_git(["remote", "set-branches", "origin", "*"], cwd=cdir)
            r = run_git(["fetch", "--tags", "origin"], cwd=cdir)
            if r.returncode != 0:
                log("  {} {} fetch 失败：{}".format(db, repo, r.stderr.decode('utf-8', 'replace')[-200:]))
        return cdir
    os.makedirs(os.path.dirname(cdir), exist_ok=True)
    t0 = time.time()
    single = [] if db == "darwin" else ["--single-branch"]
    # 规则：永远只拉取提交信息（--filter=tree:0），禁止全量克隆
    # 仅 commit 对象，无 tree/blob，git log 元数据完整，commit_files 不更新
    extra = ["--filter=tree:0"]
    r = subprocess.run(
        ["git", "clone", "--bare"] + single + extra + ["--progress", url, cdir],
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        tail = (r.stderr or "")[-500:]
        log("  克隆失败 {} {}: {}".format(db, repo, tail.replace("\r", " ")))
        # 清理半成品，允许下次重试
        if os.path.isdir(cdir):
            shutil.rmtree(cdir, ignore_errors=True)
        return None
    log("  克隆完成 {} {} {:.0f}s".format(db, repo, time.time() - t0))
    return cdir


def since_str(iso):
    dt = datetime.datetime.fromisoformat(iso)
    return (dt - datetime.timedelta(days=7)).strftime("%Y-%m-%dT%H:%M:%S")


def update_repo(db, repo, url, con):
    cur = con.cursor()
    row = cur.execute(
        "SELECT commit_hash, committer_date FROM commits WHERE repo_name=? "
        "ORDER BY committer_date DESC LIMIT 1", (repo,)).fetchone()
    if not row:
        return "skip", "库内无该 repo 存量记录"
    known_hash, boundary = row
    cdir = ensure_clone(db, repo, url)
    if not cdir:
        return "error", "克隆失败"
    # 门禁：已知旧哈希必须存在于新克隆对象库
    r = run_git(["cat-file", "-e", known_hash + "^{commit}"], cwd=cdir)
    reingest = False
    if r.returncode != 0 and db != "darwin":
        # 多分支仓库：单支克隆可能不含旧边界哈希 → 补全所有引用后重试
        run_git(["remote", "set-branches", "origin", "*"], cwd=cdir)
        fr = run_git(["fetch", "--tags", "origin"], cwd=cdir)
        if fr.returncode == 0:
            r = run_git(["cat-file", "-e", known_hash + "^{commit}"], cwd=cdir)
            if r.returncode == 0:
                log("  {}/{} 单支缺边界哈希，全引用补全后命中".format(db, repo))
    if r.returncode != 0:
        # 锚点降级：库内最新哈希不在克隆（分支重写/镜像差异）→ 向下探测最近可达哈希作边界
        anchor = None
        for h, dt in cur.execute(
                "SELECT commit_hash, committer_date FROM commits WHERE repo_name=? "
                "ORDER BY committer_date DESC LIMIT 300", (repo,)):
            rr = run_git(["cat-file", "-e", h + "^{commit}"], cwd=cdir)
            if rr.returncode == 0:
                anchor = (h, dt)
                break
        if anchor:
            known_hash, boundary = anchor
            log("  {}/{} 边界锚点降级至 {}（原最新哈希不在克隆）".format(db, repo, boundary[:10]))
        else:
            # 兜底：小库（克隆全历史 ≤2000 提交）或白名单仓库允许全量重灌
            n_all_refs = run_git(["rev-list", "--all", "--count"], cwd=cdir)
            n_str = n_all_refs.stdout.decode().strip() if n_all_refs.returncode == 0 else ""
            existing_count = cur.execute(
                "SELECT count(*) FROM commits WHERE repo_name=?", (repo,)).fetchone()[0]
            # 白名单：上游镜像整体重建，唯一更新途径即全量重灌（trueos-src 2026-08-18 判定，0/100 抽样不可达）
            allow_big = repo in REINGEST_ALLOW
            ok_small = n_str.isdigit() and 0 < int(n_str) <= 2000 and int(n_str) >= existing_count // 2
            # 下限保护：白名单大库也要求克隆非空（netbsd-src 等未白名单仓库一律拒绝）
            ok_big = allow_big and n_str.isdigit() and int(n_str) > 0
            if ok_small or ok_big:
                reingest = True
                log("  {}/{} 已知哈希缺失，进入全量重灌（克隆全引用 {} 提交，存量 {}）".format(
                    db, repo, n_str, existing_count))
            else:
                return "error", "门禁失败：锚点全不可达，克隆 {} 提交（存量 {}），拒绝操作".format(
                    n_str or "?", existing_count)
    existing = {h for (h,) in cur.execute("SELECT commit_hash FROM commits WHERE repo_name=?", (repo,))}
    if reingest:
        # 全量重灌：清空该 repo 存量后按克隆全引用重建
        has_cf_ri = cur.execute(
            "SELECT count(*) FROM sqlite_master WHERE type='table' AND name='commit_files'").fetchone()[0]
        has_tags_ri = cur.execute(
            "SELECT count(*) FROM sqlite_master WHERE type='table' AND name='tags'").fetchone()[0]
        with con:
            if has_cf_ri:
                con.execute("DELETE FROM commit_files WHERE repo_name=?", (repo,))
            con.execute("DELETE FROM commits WHERE repo_name=?", (repo,))
            if has_tags_ri:
                con.execute("DELETE FROM tags WHERE repo_name=?", (repo,))
        existing = set()
        since_arg = ["--all"]
        boundary_note = "全量重灌"
    else:
        since_arg = ["--all", "--since=" + since_str(boundary)]
        boundary_note = boundary[:10]
    # rev-list 候选
    r = run_git(["rev-list"] + since_arg, cwd=cdir)
    if r.returncode != 0:
        return "error", "rev-list 失败: " + r.stderr.decode("utf-8", "replace")[:200]
    cand = set(r.stdout.decode().split())
    new_hashes = cand - existing
    if not new_hashes:
        return "uptodate", "无新提交（边界 {}）".format(boundary[:10])
    # log 解析（tree:0 模式下仅元数据，无 numstat/name-status；Darwin 既有完整克隆例外）
    tree_mode = db != "darwin"
    log_args = (["git", "-c", "core.quotepath=false", "log"] + since_arg +
                ["--date=iso-strict", "--pretty=format:" + PRETTY])
    if not tree_mode:
        log_args += ["--numstat", "--name-status", "--no-renames"]
    r = subprocess.run(log_args, cwd=cdir, capture_output=True)
    if r.returncode != 0:
        return "error", "git log 失败"
    text = r.stdout.decode("utf-8", "replace")
    commits = []
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
        files = []
        if not tree_mode:
            numstat, namestat = {}, {}
            for ln in lines[1:]:
                m = NUMSTAT_RE.match(ln)
                if m:
                    a = None if m.group(1) == "-" else int(m.group(1))
                    d = None if m.group(2) == "-" else int(m.group(2))
                    numstat[m.group(3)] = (a, d)
                    continue
                m = NAMESTAT_RE.match(ln)
                if m and len(m.group(1)) == 1:
                    namestat[m.group(2)] = m.group(1)
            for path, letter in namestat.items():
                a, d = numstat.get(path, (None, None))
                files.append((repo, h, path, letter, a, d))
        commits.append((
            h, repo, head[1], head[2], head[3], head[4], head[5], head[6],
            head[8], head[9] if len(head) > 9 else "", head[7], sob, files))
    fs = [f for c in commits for f in c[12]]
    has_cf = cur.execute(
        "SELECT count(*) FROM sqlite_master WHERE type='table' AND name='commit_files'").fetchone()[0]
    # 事务写入
    with con:
        con.executemany(
            "INSERT OR IGNORE INTO commits (commit_hash,repo_name,author_name,author_email,"
            "author_date,committer_name,committer_email,committer_date,message_subject,"
            "message_body,parent_hashes,signed_off_by) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
            [c[:12] for c in commits])
        if fs and has_cf:
            con.executemany(
                "INSERT INTO commit_files (repo_name,commit_hash,file_path,status,additions,deletions)"
                " VALUES (?,?,?,?,?,?)", fs)
        # tags 增量（表存在时；for-each-ref 字段直出，%(*objectname) 优先保证指向提交）
        has_tags = cur.execute(
            "SELECT count(*) FROM sqlite_master WHERE type='table' AND name='tags'").fetchone()[0]
        new_tags = 0
        if has_tags:
            r = run_git(
                ["for-each-ref", "refs/tags", "--sort=refname",
                 "--format=%(refname:short)%09%(objecttype)%09"
                 "%(if)%(*objectname)%(then)%(*objectname)%(else)%(objectname)%(end)%09"
                 "%(taggerdate:iso-strict)%09%(taggername)%09%(contents:subject)"], cwd=cdir)
            known_tags = {t for (t,) in cur.execute("SELECT tag_name FROM tags WHERE repo_name=?", (repo,))}
            tag_rows = []
            for line in r.stdout.decode("utf-8", "replace").splitlines():
                parts = line.split("\t")
                if len(parts) != 6:
                    continue
                name, objtype, target, tdate, tname, tmsg = parts
                if name in known_tags:
                    continue
                ttype = "annotated" if objtype == "tag" else "lightweight"
                # 与存量格式对齐：+00:00 统一写作 Z
                if tdate.endswith("+00:00"):
                    tdate = tdate[:-6] + "Z"
                cdate = run_git(["show", "-s", "--format=%cI", target], cwd=cdir
                                ).stdout.decode("utf-8", "replace").strip()
                if cdate.endswith("+00:00"):
                    cdate = cdate[:-6] + "Z"
                tag_rows.append((repo, name, ttype, tdate, tname, tmsg.strip(), target, cdate))
            if tag_rows:
                con.executemany(
                    "INSERT OR IGNORE INTO tags (repo_name,tag_name,tag_type,tagger_date,tagger_name,"
                    "tag_message,target_commit_hash,target_commit_date) VALUES (?,?,?,?,?,?,?,?)", tag_rows)
                new_tags = len(tag_rows)
        # repos/db_meta 回写
        n_all = cur.execute("SELECT count(*) FROM commits WHERE repo_name=?", (repo,)).fetchone()[0]
        latest = cur.execute(
            "SELECT max(committer_date) FROM commits WHERE repo_name=?", (repo,)).fetchone()[0]
        con.execute(
            "UPDATE repos SET clone_date='2026-08-18', commit_count=?, latest_commit_date=?, "
            "notes=COALESCE(notes,'')||'; 增量更新 2026-08-18（--no-renames，GitHub 镜像）' WHERE repo_name=?",
            (n_all, latest, repo))
        con.execute(
            "INSERT INTO db_meta (key,value,updated_at) VALUES ('last_incremental_update',?,?) "
            "ON CONFLICT(key) DO UPDATE SET value=excluded.value, updated_at=excluded.updated_at",
            ("2026-08-18（增量 " + str(len(commits)) + " commits, " + str(new_tags) + " tags）",
             datetime.datetime.now().isoformat(timespec="seconds")))
    return "ok", "增量 {} commits / {} tags / {} 文件行（{}）".format(
        len(commits), new_tags, len(fs), boundary_note)


def rebuild_duckdb(db):
    """pre-update 快照移入 12-，然后重建主库并优化"""
    src_db = db_path(db)
    duck_dir = os.path.join(os.path.dirname(src_db), "duckdb")
    dpath = os.path.join(duck_dir, db + ".duckdb")
    if os.path.exists(dpath):
        snap_dir = os.path.join(BACKUP_ROOT, db)
        os.makedirs(snap_dir, exist_ok=True)
        dst = os.path.join(snap_dir, TS + ".preupdate.duckdb")
        shutil.move(dpath, dst)
        log("  preupdate 快照 -> {}".format(os.path.relpath(dst, BASE)))
    for args in (["--db", db], ["--optimize", "--db", db]):
        r = subprocess.run([sys.executable, FIXED] + args, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", cwd=BASE)
        out = (r.stdout or "") + (r.stderr or "")
        log("  sqlite2duckdb {} -> exit {}".format(" ".join(args), r.returncode))
        for line in out.strip().splitlines()[-6:]:
            log("    | " + line)
        if r.returncode != 0:
            return False
    return True


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
    sys.stdout.reconfigure(encoding="utf-8")
    os.makedirs(WORK, exist_ok=True)
    done = load_done()
    log("断点：已完成 {} 个 (db,repo)".format(len(done)))
    results = []
    state_f = open(STATE, "a", encoding="utf-8", newline="\n")
    for db in PLAN:
        folder, repos = PLAN[db]
        all_ok, any_work = True, False
        src_path = os.path.join(CODE, folder, "db", db + ".db")
        if not os.path.exists(src_path):
            log("[skip] {} 已归档（SQLite 源不在档），跳过全部仓库".format(db))
            for repo, url in repos:
                if (db, repo) not in done:
                    rec = {"db": db, "repo": repo, "status": "skip", "note": "archived",
                           "ts": datetime.datetime.now().isoformat(timespec="seconds")}
                    state_f.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    state_f.flush()
                    done.add((db, repo))
            continue
        con = sqlite3.connect(db_path(db))
        for repo, url in repos:
            if (db, repo) in done:
                continue
            status, note = update_repo(db, repo, url, con)
            rec = {"db": db, "repo": repo, "status": status, "note": note, "ts": datetime.datetime.now().isoformat(timespec="seconds")}
            state_f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            state_f.flush()
            results.append(rec)
            if status in ("ok", "uptodate", "skip"):
                done.add((db, repo))
            if status == "ok":
                any_work = True
            if status == "error":
                all_ok = False
            log("  [{}] {}/{}: {}".format(status, db, repo, note))
        con.close()
        # 该库全部仓库处理完且发生过写入 → 重建 DuckDB
        pending = [r for r, _ in repos if (db, r) not in done]
        if not pending and any_work and all_ok:
            log("{} 开始重建 DuckDB 主库".format(db))
            rebuild_duckdb(db)
        elif pending:
            log("{} 尚有未完成仓库 {}，暂不重建".format(db, pending))
    ok_n = sum(1 for r in results if r["status"] == "ok")
    up_n = sum(1 for r in results if r["status"] == "uptodate")
    err_n = sum(1 for r in results if r["status"] == "error")
    log("编排完成：增量 {} 仓库 / 已最新 {} / 失败 {}（详见 state.jsonl）".format(ok_n, up_n, err_n))


if __name__ == "__main__":
    main()
