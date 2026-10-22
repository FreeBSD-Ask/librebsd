#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""audit_fixture_freshness.py —— 第十三件门禁：测试夹具新鲜度。

设立缘由（2026-09-28）
----------------------
`重构2026/tests/` 的浏览器套件里**写死**了若干随目录变动的数值，最典型是口径串
`43 卷 412 章 3435 节`（`full_matrix_regression.mjs` 两处、`visual_regression.mjs` 一处）
与溯源注计数 `注 537`（一处）。`tests/README.md` 已列明“夹具同步纪律”八条，但**同步靠人记**。

第九件门禁 `audit_page_assets.py` 的 E3 只验**编号集**（`tests/README.md` 的 T 编号 ↔
`record()` 调用）双向吻合，**不验数值新鲜度** → 内容源一改而夹具未改，套件会以陈旧夹具
静默误报或静默通过。

本件把“人记”变“机检”：从内容源 `data/outline.txt` **派生**真值，与夹具内写死值逐项比对。

判据
----
- **口径族**：夹具中出现的 `N 卷 N 章 N 节` 三元组须**唯一**且等于内容源派生值。
- **溯源注族**：夹具中出现的 `注 N` 须等于内容源 `@@` 定界数。

H 线判据（2026-10-22 新增，技术债 TD-020／规格 NFR-H06）
--------------------------------------------------------
H1–H4 是 mail2d 邮件列表判读线，其判据材料分散在批 spec、`claim_map` 与核心驱动副本清单中，
此前本件只覆盖重构2026，H 线随大纲变动而陈旧时无人机检。新增三条并列判据（**仅在
`--h-line` 时运行，不改变无开关时的既有行为**）：

- **宿主存在率**：读 `script/_db_row_mining/_batch_<tag>.json` 的 `hosts` 字段（实测为
  章.节键的**字符串数组**，如 `"885"` 表 88.5 节；对象映射形制按 key 兜底），先经
  `_*_mount.json` 的 `target` 与**直扫现行大纲树**两源做**直解**，再叠加
  `script/_db_row_mining/_host_map_20261022.tsv`（TD-020 重映射表，`--host-map` 可指定）
  的承接记录。**判定改为“①直解命中 或 ②重映射表命中”**：
  - `direct`／`successor-title`／`successor-merge`：计“可解析”，且表内 `现行路径`
    须真实存在于 `05-卷册大纲/`（表本身过期即不计，防映射表静默腐烂）；
  - `retired`／`ambiguous`：单列 INFO／SKIP，**不计 FAIL**（前者内容已删、后者不猜）；
  - **FAIL 条件**：既未直解、也无可用映射记录的行 > 0。
  映射表缺失时回退旧判据并 WARN（不阻断，避免离线环境误红）。
  **宿主键须经零填充归一**（2026-10-22 复核修正）：spec 键为三位无前导零形（`887`＝88.7），
  而目录派生键带章号零填充（`088.7-…` → `0887`），直键比对会误报“未解析”；故按位切分后
  一律 `int()` 归一为 `(章号, 节号)` 整数对，只做**精确**命中（不做子串／相似度匹配）。
  指定批次无 `_batch_<tag>.json` 者记 `SKIP（无 spec）` 并单列——**无 spec 不等于夹具陈旧**，
  不计缺失、不判 FAIL。
- **claim_id 存在率**：读 `review_logs/<tag>_claim_map.json`（真值目录实测为
  `script/_db_row_mining/review_logs/`），取每条 value 的 `claim_id`（实测为对象映射，
  兼容裸字符串形制），对 `historical_claims.duckdb` 的 `claim.claim_id` 做**只读**存在性
  判定。存在率须 100%；库不存在／不可读／无 duckdb 模块 → SKIP。
- **核心驱动副本哈希**：解析 `脚本与命令/mail2d核心驱动清单.md` 表格的副本名＋SHA-256，
  与磁盘实际文件比对；不一致或文件缺失记 FAIL。清单已声明 `mail2d_run_batch.py` 的加注释
  属**有意偏离**，故一律以清单所载哈希为准，不按原件比对。

用法
----
    python audit_fixture_freshness.py                 # 0 通过 / 1 陈旧 / 2 依赖缺失
    python audit_fixture_freshness.py --tests-dir D   # 指定夹具目录（自检用）
    python audit_fixture_freshness.py --selftest      # 判据非空自检（造陈旧夹具，须 FAIL）
    python audit_fixture_freshness.py --h-line        # 只跑 H 线三判据（重构2026 不跑）
    python audit_fixture_freshness.py --h-line --h-tags fq_b120,fhk_b085  # 限定批次
    python audit_fixture_freshness.py --h-line --host-map PATH  # 指定重映射表（缺省 TD-020 表）
    python audit_fixture_freshness.py --selftest-h    # H 线三判据自检（新鲜件 PASS／坏件 FAIL）

依赖：重构2026 判据仅标准库；H 线 claim 判据另需 `duckdb`（缺失则该判据 SKIP）。
"""
import argparse
import hashlib
import json
import pathlib
import re
import shutil
import sys
import tempfile

sys.stdout.reconfigure(encoding="utf-8")

REPO = pathlib.Path(__file__).resolve().parents[3]
BASE = REPO / "08-核查报告与多轮复核" / "重构2026"
OUTLINE = BASE / "data" / "outline.txt"
TESTS = BASE / "tests"

# ── H 线（mail2d）判据的路径基准 ──────────────────────────────────────────
# 批 spec 与 mount 映射的落点；claim_map 的真值目录见 CLAIM_MAP_DIRS 注释。
MINING = REPO / "script" / "_db_row_mining"
VAULT = REPO / "05-卷册大纲"
CLAIMS_DB = REPO / "04-现代研究文献" / "historical_claims.duckdb"
DRIVER_DIR = pathlib.Path(__file__).resolve().parent
DRIVER_MANIFEST = DRIVER_DIR / "mail2d核心驱动清单.md"
# TD-020 重映射表（2026-10-22 立）：批 spec 宿主键 → 现行节目录的**有据承接**记录。
# 逐 (tag, key) 一行，方法枚举 direct／successor-title／successor-merge／retired／ambiguous。
HOST_MAP = MINING / "_host_map_20261022.tsv"
HOST_MAP_COLS = ("tag", "key", "章", "节", "旧节标题", "现行路径", "方法", "置信", "证据")
# 计“可解析”的方法（表内该方法且现行路径真实存在）
HOST_MAP_OK = ("direct", "successor-title", "successor-merge")
HOST_MAP_INFO = ("retired", "ambiguous")
# `_mail2d_run_batch.py` 以 HERE＝script/_db_row_mining 解析 `review_logs/<tag>_claim_map.json`，
# 故真值在 mining/review_logs/（2026-10-22 实测 1255 件）；仓库根 review_logs/ 实测 0 件，
# 仅作后备（若将来搬移）。前者优先。
CLAIM_MAP_DIRS = (MINING / "review_logs", REPO / "review_logs")
# 节目录／节文件名前缀：章号.节号-slug（现行四级树为节目录，旧三级树为节文件）
SEC_RE = re.compile(r"^(\d+)\.(\d+)-")
SIZE_KEEP = 30
# “无 spec”的 SKIP 标记：与“依赖缺失／无处可判”类 SKIP 区分——前者不阻断（exit 0），
# 后者仍按依赖缺失报 exit 2（2026-10-22 复核修正）。
NOSPEC_MARK = "SKIP（无 spec）"

TRIPLE_RE = re.compile(r"(\d+)\s*卷\s*(\d+)\s*章\s*(\d+)\s*节")
# 溯源注计数：须覆盖**三种**形态——
#   ① `注 537`（断言正则）② `注计数537`（断言**标签**）③ `notes: 537`（夹具真值常量）
# ②是 2026-09-28 实测发现：`full_matrix_regression.mjs` 断言写的期望值是 537 而标签写 535
#   ——标签在输出里显示了一个**错误的期望值**；原判据只匹配 `注\s*\d+`，**漏掉标签形态**。
# ③是把真值收敛为单一常量（`const FX = { notes: 537, … }`）后新增的形态：
#   断言与标签均由常量派生，若判据不认 `notes:`，覆盖度反而会下降。
NOTE_RE = re.compile(r"注(?:计数)?\s*(\d+)")
NOTES_CONST_RE = re.compile(r"\bnotes\s*[:=]\s*(\d+)")

# ── 豁免（有意识的选择，非遗漏） ──────────────────────────────────────────
# 这些夹具**刻意**绑定历史快照，其数值不应等于现行口径。
# 豁免不等于免检：本件会断言“豁免项仍然需要豁免”——若某豁免文件已不再含非现行三元组，
# 即判 FAIL，逼人删除腐烂的豁免条目（防豁免清单随目录演进静默失效）。
EXEMPT_FILES = {
    "_regr_on_backup.mjs":
        "对历史备份件 script/_bak_index_before_batch1_20260912.html（2026-09-12，25 卷 233 章 1525 节）"
        "跑的回归，夹具须匹配该快照而非现行口径",
}


def derive_truth(outline: pathlib.Path):
    """内容源 → 真值。"""
    text = outline.read_text(encoding="utf-8")
    n_vol = n_ch = n_sec = n_src = 0
    for raw in text.split("\n"):
        line = raw.rstrip()
        if not line.strip():
            continue
        if line.startswith("# "):
            n_vol += 1
        elif line.startswith("## "):
            n_ch += 1
        elif line.startswith("- "):
            n_sec += 1
            if "@@" in line:
                n_src += 1
    return {"vol": n_vol, "ch": n_ch, "sec": n_sec, "src": n_src}


def scan_fixtures(tests: pathlib.Path):
    """夹具内写死值 → [(文件, 行号, 原文, 三元组 or 注计数)]。"""
    triples, notes = [], []
    for f in sorted(tests.glob("*.mjs")):
        for i, line in enumerate(f.read_text(encoding="utf-8").split("\n"), 1):
            for m in TRIPLE_RE.finditer(line):
                triples.append((f.name, i, m.group(0),
                                tuple(int(x) for x in m.groups())))
            for m in NOTE_RE.finditer(line):
                notes.append((f.name, i, m.group(0), int(m.group(1))))
            for m in NOTES_CONST_RE.finditer(line):
                notes.append((f.name, i, m.group(0), int(m.group(1))))
    return triples, notes


def run(tests_dir: pathlib.Path, outline: pathlib.Path):
    truth = derive_truth(outline)
    triples_all, notes_all = scan_fixtures(tests_dir)
    # 按豁免分拣
    triples = [t for t in triples_all if t[0] not in EXEMPT_FILES]
    notes = [n for n in notes_all if n[0] not in EXEMPT_FILES]
    rows = []

    # 口径族
    want = (truth["vol"], truth["ch"], truth["sec"])
    bad = [t for t in triples if t[3] != want]
    stale = sorted({t[2] for t in bad})
    rows.append((
        "口径族",
        "夹具中 N 卷 N 章 N 节 须唯一且 = 内容源派生值",
        not bad,
        "内容源 = %d 卷 %d 章 %d 节；非豁免命中 %d 处%s"
        % (want[0], want[1], want[2], len(triples),
           "" if not bad else "；陈旧值 %s（%s）"
           % (", ".join(stale),
              ", ".join("%s:%d" % (b[0], b[1]) for b in bad))),
    ))

    # 溯源注族
    want_n = truth["src"]
    bad_n = [n for n in notes if n[3] != want_n]
    rows.append((
        "溯源注族",
        "夹具中 注 N 须 = 内容源 @@ 定界数",
        not bad_n,
        "内容源 = 注 %d；非豁免命中 %d 处%s"
        % (want_n, len(notes),
           "" if not bad_n else "；陈旧值 %s（%s）"
           % (", ".join(sorted({n[2] for n in bad_n})),
              ", ".join("%s:%d" % (n[0], n[1]) for n in bad_n))),
    ))

    # 豁免防腐烂：豁免文件必须存在，且必须仍然含非现行三元组
    gone, rotten = [], []
    for name in EXEMPT_FILES:
        if not (tests_dir / name).exists():
            gone.append(name)
            continue
        hits = [t for t in triples_all if t[0] == name and t[3] != want]
        if not hits:
            rotten.append(name)
    rows.append((
        "豁免防腐烂",
        "每条豁免须仍存在且仍含非现行三元组（否则删除该豁免）",
        not gone and not rotten,
        "豁免 %d 条%s%s" % (
            len(EXEMPT_FILES),
            "" if not gone else "；文件已不存在：%s" % ", ".join(gone),
            "" if not rotten else "；已无需豁免（须删条目）：%s" % ", ".join(rotten)),
    ))

    # 覆盖度：夹具里若一处都没有，判据为空
    rows.append((
        "判据覆盖",
        "非豁免夹具中至少各命中一处（否则判据空转）",
        bool(triples) and bool(notes),
        "口径命中 %d 处、注命中 %d 处" % (len(triples), len(notes)),
    ))
    return rows, triples_all, notes_all


def _report(rows, title):
    print("=" * 72)
    print(title)
    print("=" * 72)
    fails = 0
    for name, desc, ok, detail in rows:
        print("  [%s] %-8s %s" % ("PASS" if ok else "FAIL", name, desc))
        print("           %s" % detail)
        if not ok:
            fails += 1
    print("-" * 72)
    print("  合计 %d 项，FAIL %d 项" % (len(rows), fails))
    return fails


def cmd_selftest():
    """判据非空：把夹具复制一份并把口径串改成陈旧值，须 FAIL。"""
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="fixfresh_"))
    try:
        for f in TESTS.glob("*.mjs"):
            shutil.copy2(f, tmp / f.name)
        truth = derive_truth(OUTLINE)
        want = "%d 卷 %d 章 %d 节" % (truth["vol"], truth["ch"], truth["sec"])
        stale = "%d 卷 %d 章 %d 节" % (truth["vol"] - 1, truth["ch"], truth["sec"])
        hit = 0
        for f in tmp.glob("*.mjs"):
            s = f.read_text(encoding="utf-8")
            if want in s:
                f.write_text(s.replace(want, stale), encoding="utf-8")
                hit += 1
        if hit == 0:
            print("自检无法构造：夹具中未找到口径串 %r" % want, file=sys.stderr)
            return 2
        rows, _t, _n = run(tmp, OUTLINE)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    fails = _report(rows, "判据非空自检：夹具口径串改为陈旧值（预期 口径族 FAIL）")
    if fails >= 1 and any(not ok and n == "口径族" for n, _d, ok, _x in rows):
        print("  ✅ 判据非空：陈旧口径被命中（改了 %d 个夹具文件）" % hit)
        return 0
    print("  ❌ 判据可能为空：陈旧口径未被命中", file=sys.stderr)
    return 1


# ── H 线（mail2d 邮件列表判读线，H1–H4）判据 ─────────────────────────────
# 三条判据与重构2026 判据并列、互不影响：无 --h-line 时一行不跑，避免改变既有批次行为。


def h_context(**over):
    """H 线判据的路径上下文（自检时整体替换为临时目录）。"""
    ctx = {
        "mining": MINING,
        "vault": VAULT,
        "cm_dirs": CLAIM_MAP_DIRS,
        "claims_db": CLAIMS_DB,
        "driver_dir": DRIVER_DIR,
        "manifest": DRIVER_MANIFEST,
        "host_map": HOST_MAP,
    }
    ctx.update(over)
    return ctx


def h_key_pairs(key):
    """宿主键 → 候选 (章号, 节号) 整数对（零填充归一，2026-10-22 复核修正）。

    批 spec 键是“章号＋节号去点”串（`887`＝88.7、`10016`＝100.16），而目录派生键的章号
    带零填充（`088.7-…` → `0887`），直键比对必然失配。此处按位切分并一律 `int()` 归一，
    故 `887` 与 `0887` 都能切出 `(88, 7)`，补零／去零两形互通。实测量到的另一种键形是
    已带点的 `88.5`（`fhk_b064`–`b075` 共 12 行），直接解析为 `(88, 5)`。

    只产生**整数对**，调用方以整数对查目录派生表——**精确命中**，不做子串或相似度匹配。
    """
    k = str(key).strip()
    m = re.match(r"^(\d+)\.(\d+)$", k)
    if m:
        return [(int(m.group(1)), int(m.group(2)))]
    if not k.isdigit():
        return []
    return [(int(k[:i]), int(k[i:])) for i in range(1, len(k))]


def h_load_hostrel(vault: pathlib.Path, mining: pathlib.Path):
    """宿主 key → 章节相对路径；另返回 (章号, 节号) → 相对路径的归一表。

    照 `_mail2d_run_batch.load_hosts` 的两源口径：

    ① 既有 `_*_mount.json` 的 target／target_final（历史映射；key 由 target_final 基名
       去掉 `.md` 与 slug 后去点，如 `88.5-….md` → `885`）；
    ② **直扫现行大纲树**（更权威，同 key 覆盖 ①）：兼容现行“卷/章/节目录/子节文件”四级
       与旧“卷/章/节文件”三级；节 key = 章号数字 + 节号数字（去点），`97.5` → `975`，
       归一表项 = `(章号, 节号)`（如 `088.7-…` → `(88, 7)`），供零填充差异互通。

    注意：全书重编号后同一 slug 的章号会变（如原 88.5 节现为 97.5），key 本身即永久失配
    ——这正是本判据要抓的“判据陈旧”，不得据此反推大纲有错。归一表**不掩盖**重编号：
    整数对同样失配，只是消除了零填充造成的伪失配。
    """
    hostrel, canon = {}, {}
    for f in sorted(mining.glob("_*_mount.json")):
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if not isinstance(d, list) or not d or not isinstance(d[0], dict):
            continue
        for x in d:
            t, tf = x.get("target"), x.get("target_final")
            if t and tf:
                key = pathlib.PurePath(str(tf)).name.split("-", 1)[0].replace(".", "")
                if key:
                    hostrel[key] = t
    for vol in sorted(vault.iterdir()):
        if not vol.is_dir():
            continue
        for chap in sorted(vol.iterdir()):
            if not chap.is_dir():
                continue
            for ent in sorted(chap.iterdir()):
                m = SEC_RE.match(ent.name)
                if not m:
                    continue
                key = m.group(1) + m.group(2)
                pair = (int(m.group(1)), int(m.group(2)))
                rel = "%s/%s/%s" % (vol.name, chap.name, ent.name)
                if ent.is_dir():
                    hostrel[key] = rel
                    canon[pair] = rel
                elif ent.name.endswith(".md"):
                    hostrel.setdefault(key, rel)
                    canon.setdefault(pair, rel)
    return hostrel, canon


def h_specs(mining: pathlib.Path, tags=None):
    """读批 spec。返回 (specs{tag: spec}, 指定批次无 spec 的 tag 列表, 不可读列表)。"""
    if tags:
        cand = [mining / ("_batch_%s.json" % t) for t in tags]
    else:
        cand = sorted(mining.glob("_batch_*.json"))
    specs, absent, bad = {}, [], []
    for p in cand:
        tag = p.name[len("_batch_"):-len(".json")]
        if not p.exists():
            absent.append(tag)
            continue
        try:
            sp = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, ValueError) as e:
            bad.append("%s（%s）" % (tag, e))
            continue
        if not isinstance(sp, dict):
            bad.append("%s（非对象）" % tag)
            continue
        specs[tag] = sp
    return specs, absent, bad


def h_load_hostmap(path):
    """读 TD-020 重映射表 → ({(tag, key): (方法, 现行路径)}, 告警文本)。

    表缺列／某行方法不在枚举内 → 跳过该行并在告警里点名（不静默吞）。表不存在返回空表
    与告警，调用方回退旧判据。空路径（`—`）保留空串，由调用方判其不可用。
    """
    p = pathlib.Path(path)
    if not p.exists():
        return {}, "重映射表不存在：%s（回退旧判据）" % p
    rows, bad = {}, []
    try:
        lines = p.read_text(encoding="utf-8").split("\n")
    except (OSError, UnicodeDecodeError) as e:
        return {}, "重映射表不可读：%s（%s）" % (p, e)
    hdr = None
    for i, line in enumerate(lines, 1):
        if not line.strip():
            continue
        cells = line.split("\t")
        if hdr is None:
            hdr = cells
            miss = [c for c in HOST_MAP_COLS if c not in hdr]
            if miss:
                return {}, "重映射表缺列 %s：%s" % (miss, p)
            continue
        if len(cells) < len(hdr):
            bad.append("第%d行列数不足" % i)
            continue
        d = dict(zip(hdr, cells))
        meth, rel = d["方法"].strip(), d["现行路径"].strip()
        if meth not in HOST_MAP_OK + HOST_MAP_INFO:
            bad.append("第%d行方法未知（%s）" % (i, meth))
            continue
        rows[(d["tag"].strip(), d["key"].strip())] = (meth, "" if rel == "—" else rel)
    warn = ""
    if bad:
        warn = "重映射表 %d 行不可用：%s" % (len(bad), "；".join(bad[:5]))
    return rows, warn


def h_hosts_row(ctx, tags=None):
    """判据一：批 spec 的 hosts 每个宿主键须可解析到 05-卷册大纲/ 下的现行节。

    判定＝**①直解命中 或 ②重映射表命中**（TD-020，2026-10-22）：
    - 直解：`h_key_pairs` 归一整数对精确命中目录派生表（旧路径，原判据不变）；
    - 映射：`_host_map_20261022.tsv` 的 `direct`／`successor-title`／`successor-merge`，
      且表内 `现行路径` 必须在 `05-卷册大纲/` 下真实存在——映射表自身过期不计；
    - `retired`／`ambiguous`：单列 INFO，不计 FAIL（内容已删／不猜）；
    - **FAIL 条件**：既未直解、亦无可用映射的行 > 0。
    映射表缺失 → 回退旧判据并 WARN。
    """
    vault = pathlib.Path(ctx["vault"])
    if not vault.is_dir():
        return "SKIP", "大纲树不存在：%s" % vault
    hostrel, canon = h_load_hostrel(vault, pathlib.Path(ctx["mining"]))
    hostmap, mapwarn = h_load_hostmap(ctx.get("host_map") or HOST_MAP)
    specs, absent, bad = h_specs(pathlib.Path(ctx["mining"]), tags)
    total = present = normalized = 0
    n_direct = n_map = n_map_corr = n_retired = n_ambig = n_parse = 0
    unresolved, missing, bad_tags = [], [], set()
    unmapped, stale_map = [], []
    for tag, sp in sorted(specs.items()):
        hosts = sp.get("hosts") or []
        # 实测形制为字符串数组；若将来改为对象映射，按 key 作宿主键兜底
        if isinstance(hosts, dict):
            hosts = list(hosts.keys())
        for h in hosts:
            key = str(h).strip()
            if not key:
                continue
            total += 1
            # 候选路径：①归一整数对（树派生，精确前缀）②直键（mount 源＋树派生直键）
            rels = []
            for pair in h_key_pairs(key):
                rel = canon.get(pair)
                if rel and rel not in rels:
                    rels.append(rel)
            direct = hostrel.get(key)
            if direct and direct not in rels:
                rels.append(direct)
            direct_ok = bool(direct) and (vault / direct).exists()
            hit = next((r for r in rels if (vault / r).exists()), None)
            rec = hostmap.get((tag, key))
            meth, mrel = rec if rec else ("", "")
            if hit is not None:
                n_parse += 1
            map_ok = bool(rec) and meth in HOST_MAP_OK and bool(mrel) \
                and (vault / mrel).exists()
            if rec and meth in HOST_MAP_OK and not map_ok:
                stale_map.append("%s:%s→%s" % (tag, key, mrel or "（无路径）"))
            if map_ok:
                present += 1
                n_map += 1
                if hit is not None and meth == "direct":
                    n_direct += 1
                elif hit is not None:
                    n_map_corr += 1
                if hit is None:
                    bad_tags.add(tag)
            elif rec and meth in HOST_MAP_INFO:
                n_retired += meth == "retired"
                n_ambig += meth == "ambiguous"
                present += 1
            elif hit is not None:
                present += 1
                n_direct += 1
                if not direct_ok:
                    # 直键未命中／直键所指路径不存在，仅靠归一命中（归因用，不改判据）
                    normalized += 1
            else:
                if not rels:
                    unresolved.append("%s:%s（未解析）" % (tag, key))
                else:
                    missing.append("%s:%s→%s" % (tag, key, rels[0]))
                unmapped.append("%s:%s" % (tag, key))
                bad_tags.add(tag)
    problems = unresolved + missing
    rate = 100.0 * present / total if total else 0.0
    detail = ("批次 %d（全达标 %d／有缺失 %d）／宿主行 %d；可解析 %d（%.2f%%）＝"
              "直解同指 %d ＋ 映射承接 %d（其中直解亦可命中但按映射改指 %d）；"
              "直解本身可命中 %d 行；retired %d／ambiguous %d（INFO，不阻断）；"
              "**无映射 %d**" % (
                  len(specs), len(specs) - len(bad_tags), len(bad_tags), total,
                  present, rate, n_direct, n_map, n_map_corr, n_parse,
                  n_retired, n_ambig, len(unmapped)))
    if normalized:
        detail += "；其中经零填充归一命中 %d" % normalized
    if stale_map:
        detail += "；映射表指向的路径已不存在（不计入，须修表）%d 条：%s" % (
            len(stale_map), "；".join(stale_map[:SIZE_KEEP]))
    if mapwarn:
        detail += "；WARN %s" % mapwarn
    if absent:
        detail += "；%s：%s" % (NOSPEC_MARK, ", ".join(absent[:SIZE_KEEP]))
    if bad:
        detail += "；spec 不可读：%s" % ", ".join(bad[:SIZE_KEEP])
    if problems:
        detail += "；未解析前 %d 条：%s%s" % (
            min(len(problems), SIZE_KEEP), "；".join(problems[:SIZE_KEEP]),
            "" if len(problems) <= SIZE_KEEP else "…（另 %d 条）" % (len(problems) - SIZE_KEEP))
    if not specs:
        return "SKIP", "%s：%s（无可判批次，不判缺失、不判 FAIL）" % (
            NOSPEC_MARK, ", ".join(absent[:SIZE_KEEP]) or "—")
    return ("PASS" if (total > 0 and not unmapped and not bad) else "FAIL"), detail


def _claim_id_of(v):
    """claim_map 的 value → claim_id。实测为对象映射（含 claim_id 字段），兼容裸字符串。"""
    if isinstance(v, str):
        return v.strip() or None
    if isinstance(v, dict):
        cid = v.get("claim_id")
        return str(cid).strip() if cid else None
    return None


def h_claim_row(ctx, tags=None):
    """判据二：claim_map 的 claim_id 须全部存在于 claim.claim_id（只读）。"""
    specs, absent, bad = h_specs(pathlib.Path(ctx["mining"]), tags)
    tags_all = sorted(set(specs) | set(absent))
    paths, no_cm = {}, []
    for tag in tags_all:
        for d in ctx["cm_dirs"]:
            p = pathlib.Path(d) / ("%s_claim_map.json" % tag)
            if p.exists():
                paths[tag] = p
                break
        else:
            no_cm.append(tag)
    if not paths:
        if not specs:
            # 与宿主判据同口径：全批无 spec → SKIP（无 spec），不阻断
            return "SKIP", "%s：%s（无 claim 判据输入）" % (
                NOSPEC_MARK, ", ".join(sorted(absent)[:SIZE_KEEP]) or "—")
        return "SKIP", ("全部 %d 个批次均无 claim_map（%s），claim 判据无输入"
                        % (len(tags_all), pathlib.Path(ctx["cm_dirs"][0])))
    ids, bad_json = {}, []
    for tag, p in sorted(paths.items()):
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, ValueError) as e:
            bad_json.append("%s（%s）" % (tag, e))
            continue
        if not isinstance(d, dict):
            bad_json.append("%s（非对象）" % tag)
            continue
        for v in d.values():
            cid = _claim_id_of(v)
            if cid:
                ids.setdefault(cid, []).append(tag)
    if not ids:
        return "SKIP", "claim_map 内无 claim_id（%d 件）" % len(paths)
    db = pathlib.Path(ctx["claims_db"])
    if not db.exists():
        return "SKIP", "claim 库不存在：%s（%d 个 claim_id 未判）" % (db, len(ids))
    try:
        import duckdb
    except ImportError:
        return "SKIP", "duckdb 模块缺失（%d 个 claim_id 未判）" % len(ids)
    try:
        con = duckdb.connect(str(db), read_only=True)
        try:
            dbids = {r[0] for r in con.execute(
                "select distinct claim_id from claim").fetchall()}
        finally:
            con.close()
    except Exception as e:  # 库被占用／损坏：绝不改成写连接
        return "SKIP", "claim 库不可读（%s）：%s（%d 个 claim_id 未判）" % (
            type(e).__name__, e, len(ids))
    missing = sorted(set(ids) - dbids)
    ok = not missing and not bad_json and not bad
    rate = 100.0 * (len(ids) - len(missing)) / len(ids)
    detail = ("批次 %d（有 claim_map %d／无 %d）／claim_id %d；在库 %d（%.4f%%）；缺失 %d"
              % (len(tags_all), len(paths), len(no_cm), len(ids),
                 len(ids) - len(missing), rate, len(missing)))
    if no_cm:
        detail += "；无 claim_map（SKIP 披露）：%s" % ", ".join(sorted(no_cm)[:SIZE_KEEP])
    if bad:
        detail += "；spec 不可读：%s" % ", ".join(bad[:SIZE_KEEP])
    if bad_json:
        detail += "；claim_map 不可读：%s" % ", ".join(bad_json[:SIZE_KEEP])
    if missing:
        detail += "；缺失前 %d 条：%s%s" % (
            min(len(missing), SIZE_KEEP), "；".join(missing[:SIZE_KEEP]),
            "" if len(missing) <= SIZE_KEEP else "…（另 %d 条）" % (len(missing) - SIZE_KEEP))
    return ("PASS" if ok else "FAIL"), detail


def _sha256(p: pathlib.Path):
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def h_manifest_rows(manifest: pathlib.Path):
    """解析核心驱动清单表格 → [(副本名, 声明的 SHA-256)]。

    只认“第 2 列以 .py 结尾且第 4 列为 64 位十六进制”的数据行，故同文档里“未入库类别”
    等数值表格不会被误收。
    """
    rows = []
    for line in manifest.read_text(encoding="utf-8").split("\n"):
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip().strip("`") for c in s.strip("|").split("|")]
        if len(cells) < 4 or not cells[1].endswith(".py"):
            continue
        if not re.match(r"^[0-9a-fA-F]{64}$", cells[3]):
            continue
        rows.append((cells[1], cells[3].lower()))
    return rows


def h_hash_row(ctx):
    """判据三：清单载明的副本 SHA-256 须与磁盘一致；缺文件亦 FAIL。

    清单已声明 `mail2d_run_batch.py` 的加注释属有意偏离，故一律以清单所载哈希为准。
    """
    manifest = pathlib.Path(ctx["manifest"])
    if not manifest.exists():
        return "FAIL", "清单不存在：%s" % manifest
    rows = h_manifest_rows(manifest)
    if not rows:
        return "FAIL", "清单中未解析到“副本名＋SHA-256”行：%s" % manifest
    bad = []
    for name, want in rows:
        p = pathlib.Path(ctx["driver_dir"]) / name
        if not p.exists():
            bad.append("%s（缺文件）" % name)
            continue
        got = _sha256(p)
        if got != want:
            bad.append("%s（清单 %s… 实得 %s…）" % (name, want[:12], got[:12]))
    ok = not bad
    detail = "清单 %d 件副本；哈希一致 %d；不一致／缺失 %d%s" % (
        len(rows), len(rows) - len(bad), len(bad),
        "" if not bad else "：" + "；".join(bad))
    return ("PASS" if ok else "FAIL"), detail


def h_rows(ctx, tags=None):
    return [
        ("宿主存在率",
         "批 spec 的 hosts 每个宿主键须①直解命中 或②重映射表命中现行节目录"
         "（retired／ambiguous 记 INFO 不阻断）") + h_hosts_row(ctx, tags),
        ("claim_id 存在率",
         "claim_map 的 claim_id 须全部存在于 historical_claims.duckdb（100%）") + h_claim_row(ctx, tags),
        ("副本哈希",
         "mail2d核心驱动清单.md 载明的副本 SHA-256 须与磁盘一致") + h_hash_row(ctx),
    ]


def _report_h(rows, title, note=None):
    print("=" * 72)
    print(title)
    print("=" * 72)
    nf = ns = 0
    for name, desc, status, detail in rows:
        print("  [%s] %-10s %s" % (status, name, desc))
        print("           %s" % detail)
        if status == "FAIL":
            nf += 1
        elif status == "SKIP":
            ns += 1
    print("-" * 72)
    print("  合计 %d 项，FAIL %d 项，SKIP %d 项" % (len(rows), nf, ns))
    if note:
        print("  %s" % note)
    return nf, ns


def _h_exit(rows):
    """H 线退出码：FAIL→1；依赖缺失／无输入类 SKIP→2；**无 spec 的 SKIP 不阻断→0**。

    2026-10-22 复核修正：无 `_batch_<tag>.json` 说明无材料可判，不等同夹具陈旧，
    故不返回 1，也不按依赖缺失返回 2。
    """
    if any(s == "FAIL" for _n, _d, s, _x in rows):
        return 1
    if any(s == "SKIP" and NOSPEC_MARK not in x for _n, _d, s, x in rows):
        return 2
    return 0


def cmd_h_line(tags, ctx=None):
    ctx = ctx or h_context()
    if not pathlib.Path(ctx["mining"]).is_dir():
        print("依赖缺失：%s 不存在（批 spec 目录）" % ctx["mining"], file=sys.stderr)
        return 2
    rows = h_rows(ctx, tags)
    nf, _ns = _report_h(rows, "H 线夹具新鲜度（TD-020／FR-15）：%s" % ctx["mining"])
    code = _h_exit(rows)
    print("  %s" % _h_line_advice(nf))
    if code == 2:
        print("  退出码 2：存在依赖缺失类 SKIP（无 spec 的 SKIP 不阻断）")
    return code


def _h_line_advice(nf):
    """“若并入默认”的建议（本批只披露，不并入）。"""
    if nf:
        return ("若并入默认的建议：暂不并入。H 线现有 %d 项 FAIL（未解析且无映射的行 > 0），"
                "并入会让既有批次全线红；须先补重映射表或重建宿主键。" % nf)
    return ("若并入默认的建议：可并入。三项全 PASS（宿主判据已叠加重映射表，retired／"
            "ambiguous 记 INFO 不阻断），代价仅为一次目录扫描与一次库只读；"
            "建议下一批起与 --selftest 同跑。")


def cmd_selftest_h():
    """H 线判据非空自检：逐判据造新鲜件（须 PASS）与坏件（须 FAIL／SKIP）。

    2026-10-22 复核修正后扩例：新增零填充差异（`975`↔`097.5`）、补零键形（`0887`↔`088.7`）、
    归一后仍缺失（`885`）、无 spec 须 SKIP、混合批次不计 FAIL、退出码不阻断共 6 例，
    连同既有 8 例合计 14 例。TD-020 再扩 5 例（映射承接 PASS／映射 retired INFO 不阻断／
    映射 ambiguous INFO 不阻断／映射表过期 FAIL／映射表缺失回退旧判据），合计 19 例。
    """
    try:
        import duckdb
    except ImportError:
        print("自检无法构造：缺 duckdb 模块（claim 判据无从造库）", file=sys.stderr)
        return 2
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="hfresh_"))
    try:
        vault = tmp / "vault"
        for vol, chap, sec, leaf in (
            ("第01卷-测试卷", "第11章-测试章", "11.1-测试节", "11.1.1-子节.md"),
            ("第02卷-测试卷", "第097章-测试章", "097.5-测试节", "097.5.1-子节.md"),
            ("第03卷-测试卷", "第088章-测试章", "088.7-测试节", "088.7.1-子节.md"),
        ):
            d = vault / vol / chap / sec
            d.mkdir(parents=True)
            (d / leaf).write_text("测试宿主\n", encoding="utf-8")
        mining = tmp / "mining"
        mining.mkdir()

        def spec(name, hosts):
            (mining / ("_batch_%s.json" % name)).write_text(
                json.dumps({"tag": name, "hosts": hosts}, ensure_ascii=False),
                encoding="utf-8")

        spec("ok_b900", ["111"])            # 直键命中
        spec("bad_b901", ["99"])            # 无此章.节，且映射表无记录
        spec("pad_b902", ["975"])           # 键无章号零填充，目录为 097.5
        spec("pad_b903", ["0887"])          # 键带零填充，目录为 088.7
        spec("gone_b904", ["885"])          # 归一后仍无 88.5 节（真缺失）
        # TD-020 重映射判定用例（2026-10-22）
        spec("stale_b906", ["10017"])       # 直解失败，但映射表有 successor-title → PASS
        spec("ret_b907", ["1588"])          # 映射表记 retired → INFO，不阻断
        spec("amb_b908", ["1211"])          # 映射表记 ambiguous → INFO，不阻断
        spec("dead_b909", ["222"])          # 映射表指向的路径已不存在 → 表过期，FAIL
        # nospec_b905 刻意不造 spec：须 SKIP（无 spec），不得 FAIL
        hm = tmp / "host_map.tsv"
        hm.write_text(
            "\t".join(HOST_MAP_COLS) + "\n" +
            "\t".join(["stale_b906", "10017", "11", "1", "旧标题甲",
                       "第01卷-测试卷/第11章-测试章/11.1-测试节", "successor-title", "high",
                       "自检夹具：直解失败、映射承接"]) + "\n" +
            "\t".join(["ret_b907", "1588", "", "", "旧标题乙", "—", "retired", "low",
                       "自检夹具：判删，无承接"]) + "\n" +
            "\t".join(["amb_b908", "1211", "", "", "旧标题丙", "—", "ambiguous", "n/a",
                       "自检夹具：并列不猜"]) + "\n" +
            "\t".join(["dead_b909", "222", "88", "8", "旧标题丁",
                       "第09章-不存在/9.9-不存在", "successor-title", "high",
                       "自检夹具：映射路径已失效"]) + "\n",
            encoding="utf-8", newline="\n")
        cmlogs = tmp / "cmlogs"
        cmlogs.mkdir()
        (cmlogs / "ok_b900_claim_map.json").write_text(
            json.dumps({"1": {"claim_id": "CL-RM-000001"}}, ensure_ascii=False),
            encoding="utf-8")
        (cmlogs / "bad_b901_claim_map.json").write_text(
            json.dumps({"1": {"claim_id": "CL-RM-999999"}}, ensure_ascii=False),
            encoding="utf-8")
        db = tmp / "claims.duckdb"
        con = duckdb.connect(str(db))
        try:
            con.execute("create table claim(claim_id varchar)")
            con.execute("insert into claim values ('CL-RM-000001')")
        finally:
            con.close()
        driver = tmp / "drv"
        driver.mkdir()
        (driver / "copy_a.py").write_text("# a\n", encoding="utf-8")
        (driver / "copy_b.py").write_text("# b\n", encoding="utf-8")
        (driver / "copy_c.py").write_text("# c\n", encoding="utf-8")
        header = ("| 源路径 | 副本 | 字节 | SHA-256 | 职能 | 运行状态 | 可直接运行 |\n"
                  "| ---- | ---- | ----: | ---- | ---- | ---- | ---- |\n")
        (driver / "manifest_ok.md").write_text(
            header + "| `s/_a.py` | `copy_a.py` | 4 | `%s` | x | x | 否 |\n"
            % _sha256(driver / "copy_a.py"), encoding="utf-8")
        (driver / "manifest_bad.md").write_text(
            header + "| `s/_b.py` | `copy_b.py` | 4 | `%s` | x | x | 否 |\n"
            % ("0" * 64), encoding="utf-8")
        (driver / "manifest_gone.md").write_text(
            header + "| `s/_c.py` | `copy_missing.py` | 4 | `%s` | x | x | 否 |\n"
            % _sha256(driver / "copy_c.py"), encoding="utf-8")

        def ctx(manifest, claims_db=None, host_map=None):
            return h_context(mining=mining, vault=vault, cm_dirs=(cmlogs,),
                             claims_db=claims_db or db, driver_dir=driver,
                             manifest=driver / manifest,
                             host_map=host_map if host_map is not None else hm)

        def host(tags):
            return h_hosts_row(ctx("manifest_ok.md"), tags)

        cases = []
        for case, want, tags in (
            ("新鲜件（hosts=111 有节目录）", "PASS", ["ok_b900"]),
            ("坏件（hosts=99 无对应节、无映射）", "FAIL", ["bad_b901"]),
            ("零填充差异（hosts=975 → 097.5 目录）", "PASS", ["pad_b902"]),
            ("补零键形（hosts=0887 → 088.7 目录）", "PASS", ["pad_b903"]),
            ("真缺失（hosts=885 归一后无 88.5）", "FAIL", ["gone_b904"]),
            ("无 spec（nospec_b905 无批 spec）", "SKIP", ["nospec_b905"]),
            ("混合（有 spec PASS ＋ 无 spec 不计 FAIL）", "PASS",
             ["pad_b902", "nospec_b905"]),
            ("映射承接（hosts=10017 直解失败、表记 successor-title）", "PASS",
             ["stale_b906"]),
            ("映射 retired（hosts=1588 表记 retired）", "PASS", ["ret_b907"]),
            ("映射 ambiguous（hosts=1211 表记 ambiguous）", "PASS", ["amb_b908"]),
            ("映射表过期（hosts=222 表内路径已不存在）", "FAIL", ["dead_b909"]),
            ("映射表缺失（回退旧判据，hosts=99 须仍 FAIL）", "FAIL", ["bad_b901"]),
        ):
            got, detail = (host(tags) if case != "映射表缺失（回退旧判据，hosts=99 须仍 FAIL）"
                           else h_hosts_row(ctx("manifest_ok.md", host_map=tmp / "nope.tsv"),
                                            tags))
            cases.append(("宿主存在率", case, want, got, detail))
        # 无 spec 的整线退出码：宿主／claim 两判据均 SKIP（无 spec），副本哈希 PASS → exit 0
        rows_ns = h_rows(ctx("manifest_ok.md"), ["nospec_b905"])
        cases.append((
            "退出码", "无 spec 不阻断（整线 SKIP 无 spec）", "exit=0",
            "exit=%d" % _h_exit(rows_ns),
            "三判据状态 %s" % "／".join(s for _n, _d, s, _x in rows_ns)))
        for name, case, want, tup in (
            ("claim_id 存在率", "新鲜件（claim_id 在库）", "PASS",
             h_claim_row(ctx("manifest_ok.md"), ["ok_b900"])),
            ("claim_id 存在率", "坏件（claim_id 不在库）", "FAIL",
             h_claim_row(ctx("manifest_ok.md"), ["bad_b901"])),
            ("claim_id 存在率", "库缺失（须 SKIP 不得 FAIL）", "SKIP",
             h_claim_row(ctx("manifest_ok.md", claims_db=tmp / "nope.duckdb"),
                         ["ok_b900"])),
            ("副本哈希", "新鲜件（哈希一致）", "PASS", h_hash_row(ctx("manifest_ok.md"))),
            ("副本哈希", "坏件（哈希不符）", "FAIL", h_hash_row(ctx("manifest_bad.md"))),
            ("副本哈希", "坏件（副本缺文件）", "FAIL", h_hash_row(ctx("manifest_gone.md"))),
        ):
            got, detail = tup
            cases.append((name, case, want, got, detail))
        print("=" * 72)
        print("H 线判据非空自检（逐判据：新鲜件须 PASS，坏件须 FAIL／SKIP）")
        print("=" * 72)
        bad = 0
        for name, case, want, got, detail in cases:
            mark = "✅" if got == want else "❌"
            print("  %s %-10s %-30s 预期 %s，实得 %s" % (mark, name, case, want, got))
            print("           %s" % detail)
            if got != want:
                bad += 1
        print("-" * 72)
        print("  合计 %d 例，不符 %d 例" % (len(cases), bad))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    if bad:
        print("  ❌ H 线判据自检未通过", file=sys.stderr)
        return 1
    print("  ✅ H 线判据非空：零填充差异 PASS、真缺失 FAIL、无 spec SKIP 且不阻断")
    return 0


def main():
    ap = argparse.ArgumentParser(description="测试夹具新鲜度门禁（第十三件）")
    ap.add_argument("--tests-dir", default=str(TESTS))
    ap.add_argument("--outline", default=str(OUTLINE))
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--selftest-h", action="store_true",
                    help="H 线三判据自检：逐判据造新鲜件（PASS）与坏件（FAIL）")
    ap.add_argument("--h-line", action="store_true",
                    help="只跑 H 线（mail2d）三判据，不跑重构2026 判据")
    ap.add_argument("--h-tags", default="",
                    help="限定 H 线批次（逗号分隔 tag），缺省全部批 spec")
    ap.add_argument("--host-map", default=str(HOST_MAP),
                    help="TD-020 宿主重映射表（TSV）；缺省 script/_db_row_mining/"
                         "_host_map_20261022.tsv，缺失则回退旧判据并 WARN")
    args = ap.parse_args()

    if args.selftest:
        return cmd_selftest()
    if args.selftest_h:
        return cmd_selftest_h()
    if args.h_line:
        tags = [t.strip() for t in args.h_tags.split(",") if t.strip()] or None
        return cmd_h_line(tags, h_context(host_map=pathlib.Path(args.host_map)))

    tests = pathlib.Path(args.tests_dir)
    outline = pathlib.Path(args.outline)
    for p, what in ((tests, "夹具目录"), (outline, "内容源")):
        if not p.exists():
            print("依赖缺失：%s 不存在（%s）" % (p, what), file=sys.stderr)
            return 2
    rows, triples_all, notes_all = run(tests, outline)
    fails = _report(rows, "测试夹具新鲜度门禁（第十三件）：%s" % tests)
    if EXEMPT_FILES:
        print()
        print("  豁免（有意识的选择，非遗漏；本件已断言其“仍需要豁免”）：")
        for name, why in sorted(EXEMPT_FILES.items()):
            hits = sorted({t[2] for t in triples_all if t[0] == name})
            print("    %-24s %s" % (name, why))
            print("    %-24s 命中值：%s" % ("", ", ".join(hits) or "（无）"))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
