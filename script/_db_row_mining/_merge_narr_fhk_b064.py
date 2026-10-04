# -*- coding: utf-8 -*-
"""fhk_b064 叙述件合并门禁（40 分件 -> 单文件）。

主会话地面真值：不采信任何代理回报，逐文件读盘、逐项断言。
任一硬门禁违反 -> 打印全部违规、EXIT 2、不写盘。

硬门禁
  1. 40 份分件齐、UTF-8、无 BOM、无 CR、TAB 三字段、宿主恒 885；
  2. 片内 pk 升序、全局无重复，与 fhk_b064_candidates.txt 双向对账；
  3. 叙述长度 60-140（Python len）；
  4. 禁字符「」『』*\| 与任何引号形态（撇号在内）；无制表符/换行；
  5. 不以句读号或空格收尾；无日期前缀；无来源尾巴标记；
  6. 版本形态逐 pk 回「本封自有正文」核字面：SUBJ 行不算正文，
     以 > / : 开头的引用块不算正文（引用块里的技术主张/人名/结论
     一律不得署给本封 FROM；无头引文块仍剔除）；
  7. FreeBSD 后接英文普通词是版本误判陷阱，一律改中文衔接；
     放行白名单 VERBLIKE = current stable release prerelease snapshot
     snap x r rc1 rc2 x11 x11r6 keltia www hackers（与任务书 §3.9 同），
     词后接数字（R2.1.0）是版本续写，放行。

与 b053 版的差异（勿回头改回）：
  - TAG/ANCHOR 换 fhk_b064；宿主仍 885（本批 249 条实测全为 1996 年，
    1994-1996 同归 885 单宿主，无主题细分）；
  - 分件文件名用 p%d 无零补（p1..p9 与 p10..p40），b053 版按 p%02d 找
    会把 p1..p9 全判「文件缺失」。此处按 p%d 主取、p%02d 兜底。

用法：
    C:/Python314/python.exe _merge_narr_fhk_b064.py
"""
import io
import os
import re
import sys

import duckdb

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
LOGDIR = os.path.join(HERE, "review_logs")
# 由 HERE 上溯两层定位仓库根：D: 映射是否还在取决于会话宿主，写死盘符会静默失效。
MAILDB = os.path.join(os.path.abspath(os.path.join(HERE, "..", "..")),
                      "03-原始史料库/11-邮件列表史料",
                      "01-freebsd/db/freebsd-hackers.duckdb")
TAG = "fhk_b064"
N_PARTS = 50
HOST = "885"
LO_LEN, HI_LEN = 60, 140
OUT = os.path.join(LOGDIR, TAG + "_mount_narr.tsv")

# 与 _gate_fhk_b064.py / _verify_cand 同口径
VERS_RE = re.compile(
    r"FreeBSD[- ][A-Za-z0-9.\~\-]+"
    r"|\b\d+(?:\.\d+)+(?:-[A-Z][A-Z0-9]*)?"
)
FREEBSD_WORD = re.compile(r"FreeBSD[- ]([A-Za-z][A-Za-z0-9]*)")
TAILNUM = re.compile(r"[\.\-]\d")
VERBLIKE = set(["current", "stable", "release", "prerelease", "snapshot",
                "snap", "x", "r", "rc1", "rc2", "x11", "x11r6",
                "keltia", "www", "hackers"])
FORBID = list("「」『』*\|")
QUOTES = set(chr(c) for c in
             [0x2018, 0x2019, 0x201C, 0x201D, 0x0027, 0x0022, 0x0060])
TRAIL = set("。，、；：？！…—．·~-.,;:?! ")
TAIL_MARK = ["ROW_MINE", "来源：", "消息列表", "freebsd-hackers.messages"]
DATE_RE = re.compile(r"\d{4}\s*年")

errors = []


def fail(part, pk, what):
    errors.append((part, pk, what))


def connect(db, tries=240, sleep=15):
    """并行会话会抢锁；连上即独占，故只在 connect 阶段重试。"""
    import time
    last = None
    for i in range(1, tries + 1):
        try:
            return duckdb.connect(db, read_only=True)
        except Exception as e:
            last = e
            print("  第 %d 次连接被占（%s），%ds 后重试"
                  % (i, str(e).splitlines()[0][:60], sleep))
            time.sleep(sleep)
    raise SystemExit("连接失败 %d 次：%s" % (tries, last))


def part_path(k):
    """分件文件名：p%d 主取（子代理实际写法），p%02d 兜底。"""
    p = os.path.join(LOGDIR, "%s_mount_narr_p%d.tsv" % (TAG, k))
    if os.path.exists(p):
        return p
    q = os.path.join(LOGDIR, "%s_mount_narr_p%02d.tsv" % (TAG, k))
    if os.path.exists(q):
        return q
    return p


def own_body(con, pk, body_cache=None):
    """本封自有正文：剔除 > / : 开头的引用块（SUBJ 由调用方不传入）。"""
    if body_cache is not None:
        b = body_cache.get(int(pk), "")
    else:
        r = con.execute(
            "SELECT body FROM messages WHERE CAST(id AS BIGINT)=?",
            [int(pk)]).fetchone()
        b = r[0] if r else ""
    keep = []
    for ln in str(b or "").split("\n"):
        s = ln.lstrip()
        if s.startswith(">") or s.startswith(":"):
            continue
        keep.append(ln)
    return "\n".join(keep)


def load_own_bodies(con, pks):
    """一次 IN 批查取全批正文：源库单 PK 查询约 0.96s，249 条逐条要 4 分钟，
    批查是一次索引扫描。缓存未命中回退单查。"""
    cache = {}
    for i in range(0, len(pks), 200):
        seg = pks[i:i + 200]
        q = ("SELECT CAST(id AS BIGINT), COALESCE(body, '') FROM messages"
             " WHERE CAST(id AS BIGINT) IN (%s)"
             % ",".join("?" for _ in seg))
        for _id, _b in con.execute(q, [int(x) for x in seg]).fetchall():
            cache[int(_id)] = _b
    return {pk: own_body(con, pk, cache) for pk in pks}


def check_narr(part, pk, nar, con=None, owncache=None):
    L = len(nar)
    if L < LO_LEN or L > HI_LEN:
        fail(part, pk, "长度 %d 越界 %d-%d" % (L, LO_LEN, HI_LEN))
    bad = "".join(c for c in nar if c in FORBID)
    if bad:
        fail(part, pk, "含禁字符 %r" % bad)
    probe = re.sub(r"[A-Za-z]+\'[A-Za-z]+", "", nar)
    q = "".join(c for c in probe if c in QUOTES)
    if q:
        fail(part, pk, "含引号形态 %r" % q)
    if "\t" in nar or "\n" in nar:
        fail(part, pk, "含制表符或换行")
    if nar[-1] in TRAIL:
        fail(part, pk, "尾章标点或空格 %r" % nar[-1])
    if nar[:1].isdigit():
        fail(part, pk, "数字开头，疑日期前缀")
    if DATE_RE.search(nar):
        fail(part, pk, "含日期前缀")
    for m in TAIL_MARK:
        if m in nar:
            fail(part, pk, "含来源尾巴 %r" % m)
            break
    own = (owncache or {}).get(int(pk))
    if own is None:
        own = own_body(con, pk)
    for m in VERS_RE.findall(nar):
        if m not in own:
            fail(part, pk, "版本形态 %r 不在本封自有正文内"
                           "（SUBJ 与引用块不算正文）" % m)
            break
    for m in FREEBSD_WORD.finditer(nar):
        w = m.group(1)
        if w.lower() in VERBLIKE or TAILNUM.match(nar[m.end():m.end() + 2]):
            continue
        fail(part, pk, "FreeBSD 后接英文普通词 %r：版本误判陷阱，须改中文衔接" % w)


def main():
    errors[:] = []
    cand = {}
    for ln in io.open(os.path.join(LOGDIR, TAG + "_candidates.txt"),
                      encoding="utf-8"):
        if ln.strip():
            f = ln.rstrip("\n").split("|", 2)
            cand[f[0]] = f[1]

    con = connect(MAILDB)
    owncache = load_own_bodies(con, list(cand))
    print("自有正文缓存 %d 条" % len(owncache))
    rows = []
    seen = []
    for k in range(1, N_PARTS + 1):
        part = "p%d" % k
        p = part_path(k)
        if not os.path.exists(p):
            fail(part, "-", "文件缺失")
            continue
        raw = io.open(p, "rb").read()
        if raw[:3] == b"\xef\xbb\xbf":
            fail(part, "-", "含 BOM")
        if b"\r" in raw:
            fail(part, "-", "含 CR")
        try:
            txt = raw.decode("utf-8")
        except UnicodeDecodeError as e:
            fail(part, "-", "UTF-8 解码失败 %s" % e)
            continue
        prev = 0
        for ln in txt.split("\n"):
            if not ln.strip():
                continue
            f = ln.split("\t")
            if len(f) != 3:
                fail(part, ln[:24], "字段数 %d != 3" % len(f))
                continue
            pk, hk, nar = f
            if not pk.isdigit():
                fail(part, pk, "pk 非纯数字")
                continue
            if prev and int(pk) <= prev:
                fail(part, pk, "pk 未升序（前 %d）" % prev)
            prev = int(pk)
            if hk != HOST:
                fail(part, pk, "宿主 %r != %s" % (hk, HOST))
            if pk in seen:
                fail(part, pk, "全局重复 pk")
            seen.append(pk)
            rows.append((pk, hk, nar))
            check_narr(part, pk, nar, con, owncache)
    con.close()

    miss = sorted(set(cand) - set(seen), key=int)
    extra = sorted(set(seen) - set(cand), key=int)
    if miss:
        fail("-", "-", "候选有叙述无 %d 条: %s" % (len(miss), miss))
    if extra:
        fail("-", "-", "叙述有候选无 %d 条: %s" % (len(extra), extra))
    if len(rows) != len(cand):
        fail("-", "-", "条数 %d != 候选 %d" % (len(rows), len(cand)))

    print("=" * 78)
    print("%s 叙述件合并门禁（候选 %d / 叙述 %d）" % (TAG, len(cand), len(rows)))
    print("=" * 78)
    if errors:
        print("!! 违规 %d 条（未写盘）" % len(errors))
        for part, pk, what in errors:
            print("   %-6s %-9s %s" % (part, pk, what))
        sys.exit(2)

    rows.sort(key=lambda r: int(r[0]))
    with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
        for pk, hk, nar in rows:
            f.write("%s\t%s\t%s\n" % (pk, hk, nar))
    raw = io.open(OUT, "rb").read()
    L = [len(c) for _, _, c in rows]
    print("EXIT 0：合并件 %s" % OUT)
    print("  %d B | %d 条 | BOM %s | CR %s | 升序 %s"
          % (len(raw), len(rows), raw[:3] == b"\xef\xbb\xbf",
             b"\r" in raw,
             [int(a) for a, _, _ in rows] == sorted(int(a) for a, _, _ in rows)))
    print("  len %d-%d 均值 %.1f | host %s"
          % (min(L), max(L), round(sum(L) * 1.0 / len(L), 1),
             set(b for _, b, _ in rows)))


if __name__ == "__main__":
    main()
