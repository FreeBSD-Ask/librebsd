# -*- coding: utf-8 -*-
"""邮件线单批运行器（参数化）：把每批 3–4 个一次性脚本合并为一个工具。

设计：每批一个 spec 文件 `_batch_<tag>.json`（由 `new` 子命令生成），
后续子命令都读它，避免重复生成脚本。

子命令
  new       建 spec（校验批号不撞、记录 db/offset/n/hosts/anchor）
  dump      调 _mail2d_batch_dump.py
  body      抽候选正文（调 _extract_cands_body.py，含截断）
  check     候选/叙述校验（调 _chk_mail2d_cand.py / _chk_mount_narr.py）
  register  落库：由模板生成并执行（dry → apply），产出 claim_map；
            `--dry-run` 为严格零写入：只做模板替换与残留计数，**不落生成件**、不执行；
            不带旗标＝生成并只读演练（历史行为），`--apply` 须门禁（不可与 `--dry-run` 并用）
  outline   大纲回写（**阶段二 2026-10-22 起**）：改调固定脚本 `脚本与命令/outline_writer.py`
            （ADR-0010 执行件；宿主权威＝claim_map.hosts，块级锚点幂等，写点/读点 commonpath 断言，
            全或无回滚），dry → write → 二跑 0。旧模板生成链（gen_outline → _outline_<tag>.py）
            已退役——其 TARGET_REL／键空间按扁平布局硬编码，155 批重编号与目录化后失效
  bookkeep  落地核验 + progress + changelog（dry → write，changelog 幂等）
  commit    原子提交：同一次调用内 `git diff HEAD --numstat` 核对 + `git commit -- <paths>`
  status    打印该批当前状态

用法示例
  "C:/Program Files/Python315/python.exe" _mail2d_run_batch.py new --db freebsd-elastic --offset 1500 --n 1000 \\
      --tag fe_b063 --hosts 892,894,895 --changelog-msg "..."
  "C:/Program Files/Python315/python.exe" _mail2d_run_batch.py dump --tag fe_b063
  "C:/Program Files/Python315/python.exe" _mail2d_run_batch.py register --tag fe_b063 --apply
"""
import argparse
import glob
import io
import json
import os
import re
import subprocess
import sys

import _git_lsfiles

import duckdb

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = r"d:\librebsd"
VAULT = os.path.join(ROOT, "05-卷册大纲")
HC = os.path.join(ROOT, "04-现代研究文献", "historical_claims.duckdb")
CLDB = os.path.join(ROOT, "01-项目管理", "00-变更记录", "changelog.duckdb")
MAILDIR = os.path.join(ROOT, "03-原始史料库", "11-邮件列表史料")
PY_SYS = r"C:\Program Files\Python315\python.exe"
PY_MGD = os.path.join(os.path.expanduser("~"), ".workbuddy-ai", "binaries", "python",
                      "versions", "3.13.12", "python.exe")
REG_TPL = os.path.join(HERE, "_register_fe_b051_20260915.py")
TPL_LIB, TPL_ANCHOR = "freebsd-elastic", "fe_b051"
OUT_TPL = os.path.join(HERE, "_outline_fe_b051_20260915.py")
BOSS_WRITER = os.path.join(ROOT, "00-编纂规则与格式规范", "01-规则", "脚本与命令", "outline_writer.py")


def spec_path(tag):
    return os.path.join(HERE, "_batch_%s.json" % tag)


def load(tag):
    p = spec_path(tag)
    if not os.path.exists(p):
        raise SystemExit("缺 spec：%s（先跑 new）" % os.path.basename(p))
    return json.load(io.open(p, encoding="utf-8"))


def save(sp):
    io.open(spec_path(sp["tag"]), "w", encoding="utf-8", newline="\n").write(
        json.dumps(sp, ensure_ascii=False, indent=1) + "\n")


def find_srcdb(lib):
    # 🔴 豁免，刻意不用 git ls-files：目标 *.duckdb 被 .gitignore 整类忽略
    # （git ls-files 返回 0），且 MAILDIR 只有 13 项、其下一层 3 项，非热目录，
    # os.listdir/glob 在这里不会静默漏项。
    for pat in (os.path.join(MAILDIR, "*", "db", lib + ".duckdb"),
                os.path.join(MAILDIR, "*", "duckdb", lib + ".duckdb")):
        g = glob.glob(pat)
        if g:
            return g[0]
    raise SystemExit("找不到源库：%s" % lib)


def used_anchors():
    con = duckdb.connect(HC, read_only=True)
    s = {r[0] for r in con.execute("SELECT DISTINCT anchor FROM evidence").fetchall() if r[0]}
    con.close()
    return s


def cmd_new(a):
    used = used_anchors()
    if a.tag in used:
        raise SystemExit("批号已存在（会撞号）：%s" % a.tag)
    if re.search(r"_b\d{3}$", a.tag) and a.tag in used:
        raise SystemExit("撞号")
    sp = dict(tag=a.tag, lib=a.db, offset=a.offset, n=a.n,
              hosts=[h.strip() for h in a.hosts.split(",") if h.strip()],
              anchor=a.tag, src_db=find_srcdb(a.db), note=a.note or "",
              changelog_msg=a.changelog_msg or "")
    save(sp)
    print("spec -> %s" % os.path.basename(spec_path(a.tag)))
    print("  库=%s  offset=%d  n=%d  宿主=%s" % (sp["lib"], sp["offset"], sp["n"], sp["hosts"]))


def run(cmd, **kw):
    save = kw.pop("save", None)
    r = subprocess.run(cmd, cwd=HERE, capture_output=True, text=True,
                       encoding="utf-8", errors="replace", **kw)
    sys.stdout.write(r.stdout or "")
    if r.stderr:
        sys.stderr.write(r.stderr)
    if save:
        io.open(os.path.join(HERE, save), "w", encoding="utf-8", newline="\n").write(
            (r.stdout or "") + (r.stderr or ""))
    return r.returncode


def cmd_dump(a):
    sp = load(a.tag)
    return run([PY_SYS, os.path.join(HERE, "_mail2d_batch_dump.py"),
                sp["lib"], str(sp["offset"]), str(sp["n"]), sp["tag"]])


def cmd_body(a):
    sp = load(a.tag)
    return run([PY_SYS, os.path.join(HERE, "_extract_cands_body.py"), sp["tag"]])


def cmd_check(a):
    sp = load(a.tag)
    rng = sp.get("pk_range")
    if not rng:
        raise SystemExit("spec 无 pk_range，先跑 dump")
    # spec 里 pk_range 是 "826199-832263" 字符串而非 list；直接 rng[0]/rng[1]
    # 会取到 "8"/"2"，令 LO=8 HI=2，把所有候选都误判成越界。
    if isinstance(rng, str):
        a0, b0 = rng.split("-", 1)
        lo, hi = int(a0), int(b0)
    else:
        lo, hi = int(rng[0]), int(rng[1])
    rc = run([PY_SYS, os.path.join(HERE, "_chk_mail2d_cand.py"),
              "review_logs/%s_candidates.txt" % sp["tag"], str(lo), str(hi)])
    run([PY_SYS, os.path.join(HERE, "_chk_mount_narr.py"),
         "review_logs/%s_mount_narr.tsv" % sp["tag"],
         "review_logs/%s_candidates.txt" % sp["tag"], ",".join(sp["hosts"])])
    return rc


def gen_register(sp, write=True):
    """模板替换生成 `_register_<tag>.py`，返回（目标路径, 旧值残留数）。

    `write=False`（`register --dry-run`）只做替换与残留计数、**不落盘**，
    使 dry-run 保持零写入（模板替换本身不依赖磁盘，故残留判据完全等价）。
    """
    s = io.open(REG_TPL, encoding="utf-8").read()
    s = s.replace('"review_logs", "fe_b051_candidates.txt"',
                  '"review_logs", "%s_candidates.txt"' % sp["tag"])
    # src_db 在各批 spec 里写法不一：`D:\`（大写盘符）、`d:\`（ROOT 原值小写）、
    # `\\DESKTOP-...\d\`（UNC）三种都出现过。前缀剥离靠 startswith 大小写敏感且
    # 前缀是闭集，任一失配都会把绝对路径整段拼到 MAILDIR 尾部（实测产出
    # ...\11-邮件列表史料\D:\librebsd\... 这类非法路径，duckdb 报「指定的路径无效」）。
    # 故不按前缀剥，改按库名定位文件名、只保留 `01-freebsd\db\<lib>.duckdb` 尾巴。
    tail = sp["src_db"].replace("/", "\\")
    _lib = sp["lib"] + ".duckdb"
    _i = tail.lower().find(_lib.lower())
    if _i < 0:
        raise SystemExit("src_db 定位不到 %s：%s" % (_lib, sp["src_db"]))
    # 目录段（如 `01-freebsd\db` / `03-openbsd\duckdb`）必须从 spec 的 src_db 里
    # 现取，不能硬编码 `01-freebsd`+`db`：openbsd 系库落在 `03-openbsd\duckdb\`。
    _parts = [p for p in tail.split("\\") if p]
    if len(_parts) < 3:
        raise SystemExit("src_db 段数不足：%s" % sp["src_db"])
    tail = _parts[-3] + "\\" + _parts[-2] + "\\" + _parts[-1]
    s = s.replace(r"01-freebsd\db\freebsd-elastic.duckdb", tail)
    s = s.replace('ANCHOR = "fe_b051"', 'ANCHOR = "%s"' % sp["anchor"])
    s = s.replace('SRCDB = "freebsd-elastic"', 'SRCDB = "%s"' % sp["lib"])
    s = s.replace("source_db='freebsd-elastic'", "source_db='%s'" % sp["lib"])
    s = s.replace("freebsd-elastic.messages.<id>", "%s.messages.<id>" % sp["lib"])
    s = s.replace("freebsd-elastic b051（库内序 500-999）候选落库",
                  "%s %s（库内序 %d-%d）候选落库" % (sp["lib"], sp["tag"], sp["offset"],
                                                    sp["offset"] + sp["n"] - 1))
    s = s.replace("ANCHOR='fe_b051'", "ANCHOR='%s'" % sp["anchor"])
    s = s.replace("_register_fe_b051_20260915.py", "_register_%s.py" % sp["tag"])
    # 引文兜底：正文为空的行（个别库存在空正文）改以主题作引文，否则引文为空串无法唯一
    s = s.replace('    data[pk] = (r[0] or "", r[1] or "", r[2] or "", r[3] or "")',
                  '    _s = (r[0] or "").strip()\n'
                  '    _b = (r[1] or "").strip()\n'
                  '    data[pk] = (r[0] or "", _b if _b else _s, r[2] or "", r[3] or "")')
    s = s.replace('    body = m3.execute("SELECT body FROM messages WHERE CAST(id AS BIGINT)=?", [p]).fetchone()[0] or ""',
                  '    _row = m3.execute("SELECT body, subject FROM messages WHERE CAST(id AS BIGINT)=?", [p]).fetchone()\n'
                  '    body = ((_row[0] or "") + "\\n" + (_row[1] or "")) if _row else ""')
    out = os.path.join(HERE, "_register_%s.py" % sp["tag"])
    if write:
        io.open(out, "w", encoding="utf-8", newline="\n").write(s)
    # 残留检查：只看功能常量行，且**仅当本批的库/批号与模板不同**时才算残留
    # （本批库恰为 freebsd-elastic 时，SRCDB 保持原值是正确的，不应误判）
    func = "\n".join(l for l in s.split("\n")
                     if l.strip().startswith(("ANCHOR", "SRCDB", "CAND")) or "messages.%s" in l)
    resid = 0
    if sp["lib"] != TPL_LIB:
        resid += func.count(TPL_LIB)
    if sp["anchor"] != TPL_ANCHOR:
        resid += func.count(TPL_ANCHOR)
    return out, resid


def cmd_register(a):
    sp = load(a.tag)
    dry = bool(getattr(a, "dry_run", False))
    if dry and a.apply:
        raise SystemExit("--dry-run 与 --apply 互斥：dry-run 为零写入，写库须单独跑 --apply")
    out, resid = gen_register(sp, write=not dry)
    if dry:
        print("[gen] （dry-run 未落盘）%s（旧值残留 %d）" % (os.path.basename(out), resid))
    else:
        print("[gen] %s（旧值残留 %d）" % (os.path.basename(out), resid))
    if resid:
        raise SystemExit("模板替换有残留，已中止")
    if dry:
        # 零写入：无生成件可执行，到此返回（不落文件、不落 _reg_*_out.txt、不写 claim_map）
        return 0
    cmd = [PY_SYS, out] + (["--apply"] if a.apply else [])
    rc = run(cmd, save="_reg_%s_out.txt" % sp["tag"])
    if a.apply:
        p = os.path.join(HERE, "_reg_%s_out.txt" % sp["tag"])
        t = io.open(p, encoding="utf-8").read() if os.path.exists(p) else ""
        m = re.search(r"MAPJSON:(.*)", t, re.S)
        if m:
            cm = json.loads(m.group(1).strip())
            cm = merge_claim_map(sp, cm)
            io.open(os.path.join(HERE, "review_logs", "%s_claim_map.json" % sp["tag"]),
                    "w", encoding="utf-8", newline="\n").write(
                json.dumps(cm, ensure_ascii=False, indent=1) + "\n")
            print("[claim_map] %d 条" % len(cm))
    return rc


def merge_claim_map(sp, new_cm):
    """把本次 register 的增量 map 合并进既有全量 map，再裁到当前候选集。

    register 只落本次新增的 claim，其 MAPJSON 不含先前各片已落库的 pk；
    直接覆盖会让 claim_map 缩水，使 check 的 `assert len(rows) == n` 崩
    （rows 来自候选集，n 取自 claim_map）。故必须合并。

    裁到候选集是必要的：已落库但候选被裁掉的 pk 属孤儿 claim——
    仍在库中但不再挂载，留着无害；若写进 claim_map 则 check 的 assert 会因
    两侧口径不一致而失败。孤儿不删，只不登记。
    """
    cands = os.path.join(HERE, "review_logs", "%s_candidates.txt" % sp["tag"])
    keep = set()
    if os.path.exists(cands):
        with io.open(cands, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    keep.add(line.split("|", 1)[0])

    p = os.path.join(HERE, "review_logs", "%s_claim_map.json" % sp["tag"])
    old = {}
    if os.path.exists(p):
        try:
            old = json.load(io.open(p, encoding="utf-8"))
        except ValueError:
            old = {}
        print("[claim_map] 既有 %d 条，本次增量 %d 条" % (len(old), len(new_cm)))

    merged = dict(old)
    merged.update(new_cm)

    cm = {k: v for k, v in merged.items() if not keep or k in keep}
    dropped = len(merged) - len(cm)
    if dropped:
        print("[claim_map] 裁掉 %d 条不在候选集的孤儿（仍在库中，无害）" % dropped)
    if keep:
        missing = sorted(keep - set(cm))
        if missing:
            print("[claim_map] ⚠ %d 条候选无 claim_id：%s" % (len(missing), missing[:10]))
    return cm


HOSTREL = {}


def load_hosts(sp=None):
    """host_key -> 章节相对路径（**进程内单例**：模块级 HOSTREL 缓存，重复调用忽略参数变化；
    返回副本，调用方改动不影响缓存）。

    两源合并（后者优先，更权威）：
      ① 既有 `_*_mount.json` 的 target 字段；
      ② **直接遍历 05-卷册大纲**，把 `NNN.M-*.md` 的节号去点后作为 key（如 172.2 -> 1722）。
    """
    global HOSTREL
    if HOSTREL:
        return dict(HOSTREL)
    # 🔴 豁免，刻意不用 git ls-files：`_*_mount.json` 在 /script 忽略树内且
    # 从未 git add -f（实测 git ls-files 命中 0 条），改走 git ls-files 会让这
    # 一路映射整体消失。热目录枚举风险由下面「直接遍历 05-卷册大纲」那一路
    # （已改 git ls-files）兜住：即便这里漏读个别 mount.json，大纲直扫的 key
    # 也会覆盖同名宿主。
    dropped, dropped_keys = 0, set()
    for f in glob.glob(os.path.join(HERE, "_*_mount.json")):
        try:
            d = json.load(io.open(f, encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(d, list) or not d or not isinstance(d[0], dict):
            continue
        for x in d:
            t, tf = x.get("target"), x.get("target_final")
            if not (t and tf):
                continue
            # F2：mount 源为旧扁平布局（节文件），目录化后大量目标已不存在——须与
            # git 源同样做落盘校验，宁缺勿错（键缺席会在 bookkeep/commit 处可见失败）
            cand = [os.path.join(VAULT, *t.replace("\\", "/").split("/")),
                    os.path.join(ROOT, *t.replace("\\", "/").split("/"))]
            if not any(os.path.isfile(c) for c in cand):
                dropped += 1
                dropped_keys.add(os.path.basename(tf).split("-", 1)[0])
                continue
            HOSTREL[os.path.basename(tf).split("-", 1)[0]] = t
    if dropped:
        print("[warn] load_hosts：mount 源 %d 条目标不在盘（旧扁平布局残留；去重后 %d 键），已剔除"
              % (dropped, len(dropped_keys)))
    # UNC 上 os.listdir 扫热目录会静默漏项（同目录两次调用回 16 与 8 项）且超时，
    # 改用一次 git ls-files 取全量已跟踪 .md（宿主全在版本控制内），再按路径段拆分。
    stale, dup, poisoned = [], {}, set()
    try:
        vrel = os.path.relpath(VAULT, _git_lsfiles.repo_root()).replace(os.sep, "/")
    except ValueError:
        # UNC 路径与 d: 盘符映射并存时 relpath 抛 ValueError
        # （"path is on mount 'd:', start on '\\\\DESKTOP-...\\d'"）：
        # 脚本按 UNC 路径启动时 HERE/repo_root 是 UNC、ROOT 是盘符，两者跨挂载。
        # VAULT 恒为 ROOT 下一层，取基名即仓库相对路径段。
        vrel = os.path.basename(os.path.normpath(VAULT))
    for rel in _git_lsfiles.tracked(vrel + "/"):
        parts = rel[len(vrel) + 1:].split("/")
        if len(parts) not in (3, 4):
            # 3 段＝扁平布局（卷/章/文件）；4 段＝现行目录化（卷/章/节目录/小节）
            continue
        fn = parts[-1]
        m = re.match(r"^(\d+(?:\.\d+)*)-", fn)
        if not (m and fn.endswith(".md")):
            continue
        relp = os.path.join(*parts)
        if not os.path.isfile(os.path.join(VAULT, *parts)):
            stale.append(relp)          # 重编号／改版在途：索引路径尚未落盘
            continue
        key = m.group(1)
        if key in poisoned:
            continue
        if key in HOSTREL and os.path.normcase(HOSTREL[key]) != os.path.normcase(relp):
            dup[key] = (HOSTREL[key], relp)
            HOSTREL.pop(key, None)      # 多义键剔除，宁可缺不宁可错
            poisoned.add(key)           # F3：剔除后不再被后续同键路径静默写回
            continue
        HOSTREL[key] = relp
    if stale:
        print("[warn] load_hosts：%d 条索引路径不在工作树（改版／重编号在途），已跳过；例：%s"
              % (len(stale), stale[:3]))
    if dup:
        print("[warn] load_hosts：%d 个键多义（同章号多路径），已从映射剔除并列候选：%s"
              % (len(dup), list(dup.items())[:3]))
    return dict(HOSTREL)


def gen_outline(sp):
    """【已退役 2026-10-22 阶段二】旧模板生成链：仅保留供考古／紧急回退参考，
    不再由 cmd_outline 调用（其 TARGET_REL＝host_index() 与 narr 键空间按扁平布局，
    155 批重编号与目录化后失效，详见 _outline_common 头部）。"""
    s = io.open(OUT_TPL, encoding="utf-8").read()
    s = s.replace("freebsd-elastic b051 大纲写回（Phase 3）：95 条 → 目标宿主三段式幂等块。",
                  "%s 大纲写回（Phase 3）" % sp["tag"])
    s = s.replace(r"d:\librebsd\03-原始史料库\11-邮件列表史料\01-freebsd\db\freebsd-elastic.duckdb",
                  sp["src_db"])
    s = s.replace('ANCHOR = "fe_b051"', 'ANCHOR = "%s"' % sp["anchor"])
    # 战线日期：取 spec 的 line_date（无则由主代理在 spec 中补写），缺省用当日；
    # 不可沿用模板里写死的日期——块头「YYYY-MM-DD <库> 战线」是该库遍历的实际日期，属考据标注（实测各库 09-11/09-12/09-15/09-16 各异）
    _ld = sp.get("line_date") or __import__("datetime").date.today().isoformat()
    s = s.replace('TAG = "2026-09-15 freebsd-elastic 战线"', 'TAG = "%s %s 战线"' % (_ld, sp["lib"]))
    for old, new in (("fe_b051_candidates.txt", "%s_candidates.txt" % sp["tag"]),
                     ("fe_b051_claim_map.json", "%s_claim_map.json" % sp["tag"]),
                     ("fe_b051_mount_narr.tsv", "%s_mount_narr.tsv" % sp["tag"])):
        s = s.replace('"review_logs", "%s"' % old, '"review_logs", "%s"' % new)
    # 文档字符串里的裸路径（无引号）也一并替换，避免生成脚本残留模板批号（不影响行为，仅免误读）
    s = s.replace("review_logs/fe_b051_mount_narr.tsv", "review_logs/%s_mount_narr.tsv" % sp["tag"])
    # 行数权威源＝合并后的 mount_narr TSV（register 后可有 pk 被剔，claim_map 不随之删，
    # 故不能拿 claim_map 的长度当期望行数——fhk_b021 剔 1312976 后 256->255 曾因此断言崩）
    _nt = os.path.join(HERE, "review_logs", "%s_mount_narr.tsv" % sp["tag"])
    n = sum(1 for _l in io.open(_nt, encoding="utf-8") if _l.strip())
    s = re.sub(r"assert len\(rows\) == \d+, len\(rows\)", "assert len(rows) == %d, len(rows)" % n, s)
    s = s.replace('"db": "freebsd-elastic", "batch": ANCHOR', '"db": "%s", "batch": ANCHOR' % sp["lib"])
    s = s.replace("freebsd-elastic.messages.%s", ("%s.messages.%%s" % sp["lib"]))
    s = s.replace('"ts": "2026-09-15"', '"ts": "2026-09-16"')
    s = s.replace("ANCHOR='fe_b051'", "ANCHOR='%s'" % sp["anchor"])
    s = s.replace("_outline_fe_b051_20260915.py", "_outline_%s.py" % sp["tag"])
    # TARGET_REL：用 Python 按索引替换，路径里的反斜杠不经 bash，避开八进制陷阱
    hr = load_hosts(sp)
    tbl, miss = [], []
    for hk in sp["hosts"]:
        rel = hr.get(hk)
        if rel is None:
            miss.append(hk)
        else:
            tbl.append('    "%s": r"%s",' % (hk, rel))
    if miss:
        raise SystemExit("宿主 key 无对应章节路径：%s（检查既有 mount 文件）" % miss)
    i = s.index("TARGET_REL = {")
    j = s.index("}\n\n\ndef resolve")
    s = s[:i] + "TARGET_REL = {\n" + "\n".join(tbl) + "\n" + s[j:]
    out = os.path.join(HERE, "_outline_%s.py" % sp["tag"])
    io.open(out, "w", encoding="utf-8", newline="\n").write(s)
    return out


def outline_bans_preflight(sp):
    """承重冻结前置：显式禁写名单（_outline_common.BANS_PATHS）按 claim_map.hosts 路径比对；
    并打印承重参考（refs ≥ 阈值的节，仅提示不拦截）。"""
    sys.path.insert(0, HERE)
    import _outline_common as C
    rl = os.path.join(HERE, "review_logs", "%s_claim_map.json" % sp["tag"])
    cmap = json.load(io.open(rl, encoding="utf-8"))
    frozen = set(C.BANS_PATHS)
    hits = []
    if frozen:
        for pk, v in cmap.items():
            for h in ((v.get("hosts") if isinstance(v, dict) else None) or []):
                hn = h.replace("\\", "/")
                if hn.startswith("05-卷册大纲/"):
                    hn = hn[len("05-卷册大纲/"):]
                if any(hn == p or hn.startswith(p + "/") for p in frozen):
                    hits.append((pk, hn))
    if hits:
        raise SystemExit("禁写宿主命中 %d 条（BANS_PATHS）：%s" % (len(hits), hits[:5]))
    heavy = C.frozen_sections()
    if heavy:
        print("[承重参考] refs ≥ %d 的节 %d 个（仅提示，不拦截）：%s"
              % (C.FROZEN_MIN_REFS, len(heavy), "；".join(heavy[:4])))


def outline_argv(sp, write=False):
    """阶段二：大纲回写改调 outline_writer.py（ADR-0010 执行件）。"""
    rl = os.path.join(HERE, "review_logs")
    line_date = sp.get("line_date") or __import__("datetime").date.today().isoformat()
    argv = [PY_SYS, BOSS_WRITER,
            "--narr", os.path.join(rl, "%s_mount_narr.tsv" % sp["tag"]),
            "--claim-map", os.path.join(rl, "%s_claim_map.json" % sp["tag"]),
            "--candidates", os.path.join(rl, "%s_candidates.txt" % sp["tag"]),
            "--lib", sp["lib"],
            "--root", VAULT,
            "--work", ROOT,
            "--ledger", os.path.join(HERE, "supplement_log.jsonl"),
            "--anchor", sp["anchor"],
            "--ts", line_date,
            "--tag", "%s %s 战线" % (line_date, sp["lib"])]
    if write:
        argv.append("--write")
    return argv


def cmd_outline(a):
    """大纲回写（阶段二 2026-10-22 起）：改调 `脚本与命令/outline_writer.py`。

    旧模板生成链（gen_outline → _outline_<tag>.py）已退役（TARGET_REL／键空间按扁平
    布局硬编码，155 批重编号与目录化后失效）；历史生成件保留可读，不再新生成。
    退出码语义：任一步非零即**短路返回该码**（不进入 --write／二跑），与 writer 的
    「坏件停摆、exit 2、零写入」一致（复核 F1）。
    """
    sp = load(a.tag)
    outline_bans_preflight(sp)
    base = outline_argv(sp)
    print("[gen] 调 outline_writer.py（dry-run；写盘须 --write）")
    rc = run(base)
    if rc != 0:
        print("[outline] dry-run 非零（%d）——已停手，不进入 --write／二跑（零写入）" % rc)
        return rc
    if a.write:
        rc = run(base + ["--write"])
        if rc != 0:
            print("[outline] 写入非零（%d）——已停手，不进入二跑（writer 内建回滚）" % rc)
            return rc
        print("=== 幂等二跑 ===")
        rc = run(base + ["--write"])
        if rc != 0:
            print("[outline] 二跑非零（%d）" % rc)
            return rc
    return 0


def cmd_bookkeep(a):
    sp = load(a.tag)
    cmap = json.load(io.open(os.path.join(HERE, "review_logs", "%s_claim_map.json" % sp["tag"]),
                             encoding="utf-8"))
    narr = {}
    for ln in io.open(os.path.join(HERE, "review_logs", "%s_mount_narr.tsv" % sp["tag"]),
                      encoding="utf-8"):
        if ln.strip():
            pk, hk, _ = ln.rstrip("\n").split("\t")
            narr[pk] = hk
    hr = load_hosts(sp)
    cache, fmt, miss, mism, dup, skipped = {}, [], [], [], [], []
    for hk in sp["hosts"]:
        full = os.path.join(VAULT, hr[hk])
        if not os.path.exists(full):
            d, base = os.path.dirname(full), os.path.basename(full)
            drel = os.path.relpath(d, _git_lsfiles.repo_root()).replace(os.sep, "/")
            hits = [os.path.basename(x) for x in _git_lsfiles.tracked(drel + "/")
                    if os.path.basename(x).startswith(base.split("-", 1)[0] + "-")]
            full = os.path.join(d, hits[0]) if len(hits) == 1 else full
        b = io.open(full, "rb").read()
        t = b.decode("utf-8")
        cache[hk] = t
        if b.startswith(b"\xef\xbb\xbf") or b"\r\n" in b or t.count("\u300c") + t.count("\u300d"):
            fmt.append(os.path.basename(full))
    for pk, _v in cmap.items():
        # 兼容两种 claim_map schema：扁平 {pk: cid} 与富 {pk: {claim_id, ...}}
        cid = _v["claim_id"] if isinstance(_v, dict) else _v
        if pk not in narr:
            # register 后被剔（元数据缺失等）的 pk 不入大纲，claim_map 不随之删
            skipped.append(pk)
            continue
        t = cache[narr[pk]]
        h = "<!-- ROW_MINE: %s.messages.%s -->" % (sp["lib"], pk)
        n = t.count(h)
        if n == 0:
            miss.append(pk)
            continue
        if n != 1:
            dup.append((pk, n))
        i = t.find(h)
        m = re.search(r"claim\.(CL-RM-\d+)", t[i:i + 300])
        if (m.group(1) if m else None) != cid:
            mism.append((pk, cid))
    ok = not miss and not mism and not dup
    print("[落地核验] 缺块 %d / claim_id 不符 %d / 重复 %d → %s"
          % (len(miss), len(mism), len(dup), "PASS" if ok else "FAIL"))
    print("[格式] 违规宿主 %d %s" % (len(fmt), fmt))
    if skipped:
        print("[info] claim_map 多出 %d 条未入大纲（register 后剔除）: %s" % (len(skipped), sorted(skipped)))
    if a.write:
        rec = dict(ts=__import__("datetime").datetime.now().isoformat(timespec="seconds"),
                   db=sp["lib"], batch=sp["anchor"], rows_read=sp["n"],
                   desc="%s（offset %d, n %d, %d 块, 宿主 %s）"
                        % (sp["tag"], sp["offset"], sp["n"],
                           len([p for p in cmap if p in narr]), ",".join(sp["hosts"])))
        with io.open(os.path.join(HERE, "progress.jsonl"), "a", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        print("[progress] +1")
        upd_catalog(sp)
    if not ok:
        raise SystemExit("核验未过，已中止")
    return 0


def upd_catalog(sp):
    """catalog 状态**只升不降**：pending/deferred → in_progress。

    ⚠ 绝不可用 `批数 × n` 估算覆盖率去反推 completed/in_progress ——
    部分库的批并非 500 行（甚至同一库内 n 不同），且 deferred 有 covered_by 豁免，
    据此推算会把大量 completed 误降级（2026-09-16 已踩，需人工回滚）。
    completed 的判定由专门的前沿核对流程负责，本函数不碰。
    """
    p = os.path.join(HERE, "mail2d_catalog_by_size.json")
    d = json.load(io.open(p, encoding="utf-8"))
    changed = []
    for x in d["items"]:
        if x["db"][:-7] != sp["lib"]:
            continue
        if x.get("traversal_status") in ("pending", "deferred"):
            changed.append((x.get("traversal_status"), "in_progress"))
            x["traversal_status"] = "in_progress"
    if changed:
        io.open(p, "w", encoding="utf-8", newline="\n").write(
            json.dumps(d, ensure_ascii=False, indent=1) + "\n")
    print("[catalog] %s %s" % (sp["lib"], changed or "无变化"))


def cmd_commit(a):
    sp = load(a.tag)
    hr = load_hosts(sp)
    rels = [os.path.join("05-卷册大纲", hr[hk]) for hk in sp["hosts"]]
    listing = os.path.join(HERE, "_hosts_%s.txt" % sp["tag"])
    io.open(listing, "w", encoding="utf-8", newline="\n").write("".join(r + "\n" for r in rels))
    # 逐文件核对（工作区 vs HEAD），必须 == 块数 × 5
    cmap = json.load(io.open(os.path.join(HERE, "review_logs", "%s_claim_map.json" % sp["tag"]),
                             encoding="utf-8"))
    narr = {}
    for ln in io.open(os.path.join(HERE, "review_logs", "%s_mount_narr.tsv" % sp["tag"]),
                      encoding="utf-8"):
        if ln.strip():
            pk, hk, _ = ln.rstrip("\n").split("\t")
            narr[pk] = hk
    per = {}
    for pk in cmap:
        if pk not in narr:
            continue            # register 后被剔的 pk 未入大纲，不占块数
        per[narr[pk]] = per.get(narr[pk], 0) + 1
    r = subprocess.run(["git", "diff", "HEAD", "--numstat", "--"] + rels, cwd=ROOT,
                       capture_output=True, text=True, encoding="utf-8")
    print("=== 逐文件核对 ===")
    got = {}
    for ln in (r.stdout or "").splitlines():
        if not ln.strip():
            continue
        add, _, path = ln.split("\t")
        got[os.path.basename(path)] = int(add)
        print("  %-70s +%s" % (os.path.basename(path), add))
    total = sum(got.values())
    # claim_map 可能含 register 后被剔的 pk（判 rejected 未入大纲），块数须按实入纲计
    nblk = len([p for p in cmap if p in narr])
    want = nblk * 5
    # 权威核对：按宿主数「文件中本库块数」，行数仅作 ±宿主数 的辅助校验
    hr = load_hosts(sp)
    short = []
    for hk, n in per.items():
        fp = os.path.join(VAULT, hr[hk])
        t = io.open(fp, encoding="utf-8").read()
        c = t.count("ROW_MINE: %s.messages." % sp["lib"])
        if c < n:
            short.append((hk, n, c))
    print("  合计 +%d（本方 %d 块 × 5 = %d，容差 ±%d 为分隔空行）"
          % (total, nblk, want, len(per)))
    if short:
        print("  ❌ 有宿主块数不足：%s" % short)
    elif total == 0:
        print("  ✓ 工作区无待提交改动（该批已提交），按宿主核块数全部就位")
    elif abs(total - want) > len(per):
        print("  ⚠ 行数与预期差 >宿主数，疑裹挟他方改动，请人工确认")
    else:
        print("  ✓ 按宿主核块数全部就位，行数在容差内")
    if a.apply:
        msg = a.msg or "%s 写回：%s %d 块入纲 %d 宿主（offset %d）" % (
            sp["tag"], sp["lib"], nblk, len(per), sp["offset"])
        r = subprocess.run(["git", "commit", "-m", msg, "--"] + rels, cwd=ROOT,
                           capture_output=True, text=True, encoding="utf-8")
        print((r.stdout or "") + (r.stderr or ""))
    else:
        print("[dry] 未提交")
    return 0


def cmd_status(a):
    sp = load(a.tag)
    print(json.dumps(sp, ensure_ascii=False, indent=1))
    for p in ("review_logs/%s_candidates.txt" % sp["tag"], "review_logs/%s_claim_map.json" % sp["tag"],
              "review_logs/%s_mount_narr.tsv" % sp["tag"], "_outline_%s.py" % sp["tag"]):
        print("  %-52s %s" % (p, "有" if os.path.exists(os.path.join(HERE, p)) else "—"))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("new")
    p.add_argument("--db", required=True)
    p.add_argument("--offset", type=int, required=True)
    p.add_argument("--n", type=int, default=500)
    p.add_argument("--tag", required=True)
    p.add_argument("--hosts", required=True)
    p.add_argument("--note", default="")
    p.add_argument("--changelog-msg", default="")
    p.set_defaults(fn=cmd_new)
    for name, fn, extra in (("dump", cmd_dump, []), ("body", cmd_body, []), ("check", cmd_check, []),
                            ("status", cmd_status, [])):
        q = sub.add_parser(name)
        q.add_argument("--tag", required=True)
        for e in extra:
            q.add_argument(e)
        q.set_defaults(fn=fn)
    q = sub.add_parser("register")
    q.add_argument("--tag", required=True)
    q.add_argument("--apply", action="store_true")
    q.add_argument("--dry-run", action="store_true")
    q.set_defaults(fn=cmd_register)
    q = sub.add_parser("outline")
    q.add_argument("--tag", required=True)
    q.add_argument("--write", action="store_true")
    q.set_defaults(fn=cmd_outline)
    q = sub.add_parser("bookkeep")
    q.add_argument("--tag", required=True)
    q.add_argument("--write", action="store_true")
    q.set_defaults(fn=cmd_bookkeep)
    q = sub.add_parser("commit")
    q.add_argument("--tag", required=True)
    q.add_argument("--msg", default="")
    q.add_argument("--apply", action="store_true")
    q.set_defaults(fn=cmd_commit)
    a = ap.parse_args()
    return a.fn(a) or 0


if __name__ == "__main__":
    sys.exit(main())
