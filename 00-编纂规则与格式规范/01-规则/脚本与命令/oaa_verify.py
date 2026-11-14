#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""oaa_verify.py — 大纲邮件素材审计·后验门禁（每批收尾必跑，全绿 exit 0）

门禁项：
  G1 宿主内每条锚点都有 processed 判定（无遗漏、无略过）
  G2 锚点总数守恒：当前大纲扫描数 == 快照基线（无块增删漂移）
  G3 块体机检：恰 5 行结构、摘要汉字 30—80、总字符 ≤200、禁字符（直角引号/星号/ASCII 双引号）、纪律串在场
  G4 等级一致性：块头「证据等级：Lx」== 主库 claim.evidence_level 真值（经 fetch 档案）
  G5 数据库行数守恒：claim/claim_evidence/evidence 计数与基线一致
  G6 编码：宿主文件 UTF-8 无 BOM、LF

用法：python oaa_verify.py --baseline 309004 --db-claim 289739 --db-ce 289744 --db-ev 316276 \
        host1.md host2.md ...
"""
import argparse
import contextlib
import glob
import io
import json
import os
import re
import shutil
import sys
import tempfile

import duckdb

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
OUTLINE = os.path.join(ROOT, "05-卷册大纲")
MAIN_DB = os.path.join(ROOT, "04-现代研究文献", "historical_claims.duckdb")
WORK = os.path.join(ROOT, "script", "_db_row_mining", "audit_outline", "work")
PROC = os.path.join(ROOT, "script", "_db_row_mining", "audit_outline", "processed.jsonl")
AUD = os.path.join(ROOT, "script", "_db_row_mining", "audit_outline")


def load_done():
    """G1 判定集 = 合并集（基线 processed.jsonl ∪ 各组 processed_fN.jsonl）。
    F1–F4 分片台账协议下各组只写自己的 processed_fN.jsonl，故必须并集。"""
    done = set()
    for fn in ["processed.jsonl"] + [f"processed_{g}.jsonl" for g in ("f1", "f2", "f3", "f4")]:
        p = os.path.join(AUD, fn)
        if not os.path.exists(p):
            continue
        for l in open(p, encoding="utf-8"):
            if l.strip():
                try:
                    done.add(json.loads(l)["key"])
                except Exception:
                    pass
    return done

RM = re.compile(r"<!--\s*ROW_MINE:\s*([\w-]+)\.([\w.]+)\.(\d+)\s*-->")


def cjk(s):
    return sum(1 for c in s if ord(c) > 0x2E7F)


STAR_PAIR = re.compile(r"(?<!/)\*([^*\s/]{1,16})\*(?!\w)")
# 粗体标记 `**` 的两两配对，用于识别「粗体接缝」
DBL_STAR = re.compile(r"\*\*")
# 被强调词的可能内文：纯字母/CJK/数字/下划线/连字符/撇号，不含任何标点
PLAUSIBLE = re.compile(r"^\w[\w'’-]*$")


def _pairs_and_roles(s):
    """`**` 标记按序两两配对。返回 (pairs, role)。
    pairs = [{'a': 开启标记起点, 'b': 闭合标记末位+1}]
    role  = {字符索引: (对序号, 'open'|'close')}"""
    ms = [m.start() for m in DBL_STAR.finditer(s)]
    pairs = []
    for i in range(0, len(ms) - 1, 2):
        a, c = ms[i], ms[i + 1]
        pairs.append({"a": a, "b": c + 2})
    role = {}
    for pid, p in enumerate(pairs):
        role[p["a"]] = (pid, "open")
        role[p["a"] + 1] = (pid, "open")
        role[p["b"] - 2] = (pid, "close")
        role[p["b"] - 1] = (pid, "close")
    return pairs, role


def _is_crossing(a, b, role):
    """起星落在某对的【闭合】标记、终星落在【另一对】的【开启】标记 → 粗体接缝，非强调。"""
    ra, rb = role.get(a), role.get(b)
    return bool(ra and rb and ra[1] == "close" and rb[1] == "open"
                and ra[0] != rb[0])


def violation_stars(s):
    """应判违规的星号索引集合。
    STAR_PAIR 命中当且仅当 (a) 内文匹配 PLAUSIBLE 纯词、(b) 非跨对接缝。
    内文含标点者只可能是通配星间隔（`*BSD`、`comp.unix.*`、`multi_x*_defconfig`）
    或粗体内正则量词，不可能是被强调的词；跨对接缝剥掉会打断两枚相邻粗体。"""
    _pairs, role = _pairs_and_roles(s)
    vs = set()
    for m in STAR_PAIR.finditer(s):
        a, b = m.start(), m.end() - 1
        if not PLAUSIBLE.match(m.group(1)):
            continue
        if _is_crossing(a, b, role):
            continue
        vs.add(a)
        vs.add(b)
    for i, c in enumerate(s):
        if c != "*":
            continue
        prev = s[i - 1] if i > 0 else ""
        nxt = s[i + 1] if i + 1 < len(s) else ""
        if prev and ord(prev) > 0x2E7F and nxt and ord(nxt) > 0x2E7F:
            vs.add(i)
    return vs


def is_bad_star(s):
    """`*` 是否属禁用强调符。返回布尔（兼容旧调用方）。
    判违规两类：①成对短词强调 `*word*`（内文为纯词）；②中文正文里被中文夹住的裸星 `*强调*`。
    豁免三类：(i) 内文含标点的星号区间——通配星间隔 `*BSD`/`comp.unix.*` 与粗体内正则量词；
    (ii) 相邻两枚粗体之间的接缝——起星在前一对闭合标记、终星在下一对开启标记，剥掉会打断粗体
    （2026-10-08 F4 批次十三实测全库 1,040 处）；(iii) 前后为英文/代码/层级通配的裸星。
    收窄依据见 `08-核查报告与多轮复核/07-目录审计/大纲邮件审计_批次OAA_F4批次十三_20261008.md` §二。"""
    return bool(violation_stars(s))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline", type=int, help="快照锚点基线总数")
    ap.add_argument("--db-claim", type=int)
    ap.add_argument("--db-ce", type=int)
    ap.add_argument("--db-ev", type=int)
    ap.add_argument("--len-flex", action="store_true",
                    help="长度上限放宽（F2 用）：只查下限 C<30 仍 FAIL；CJK>80/总>200 记入"
                         "长度超限清单（不 FAIL，批次报告备案）——F2 任务书 §六 字数门禁"
                         "仅设下限、§一体例注明 tech-kern 摘要偏长，且 87,665 块中 993/1000 本就 ≤200/80，"
                         "超限者为技术密集长帖（2026-09-29 实测口径）")
    ap.add_argument("--max-fails", type=int, default=30,
                    help="失败列表最多打印条数（默认 30，保持旧行为）")
    ap.add_argument("--full-dump", action="store_true",
                    help="失败列表全量输出（覆盖 --max-fails）")
    ap.add_argument("--selftest", action="store_true",
                    help="在系统临时目录跑 G1–G6 夹具自测，退出码 0/1；不读生产库")
    ap.add_argument("hosts", nargs="*")
    args = ap.parse_args()
    if args.selftest:
        sys.exit(selftest())
    if not args.hosts:
        ap.error("至少需要一个宿主路径（或用 --selftest）")

    fails = []
    # G1 processed 覆盖（合并集：基线 ∪ 四组分片台账）
    done = load_done()
    # fetch 档案（等级真值＋块型）
    fetch = {}
    for f in glob.glob(os.path.join(WORK, "*.fetch.jsonl")):
        for l in open(f, encoding="utf-8"):
            if l.strip():
                r = json.loads(l)
                fetch[r["key"]] = r
    # G2 总数
    n_all = 0
    for f in glob.glob(os.path.join(OUTLINE, "**", "*.md"), recursive=True):
        with open(f, encoding="utf-8", errors="ignore") as fh:
            n_all += len(RM.findall(fh.read()))
    if args.baseline is not None and n_all != args.baseline:
        fails.append(f"G2 锚点总数漂移: {args.baseline} → {n_all}")
    else:
        print(f"G2 锚点总数守恒: {n_all}")
    # G3/G4/G6 逐宿主
    for rel in args.hosts:
        path = os.path.join(ROOT, rel)
        raw = open(path, "rb").read()
        if raw.startswith(b"\xef\xbb\xbf"):
            fails.append(f"G6 BOM: {rel}")
        if b"\r\n" in raw:
            fails.append(f"G6 CRLF: {rel}")
        lines = raw.decode("utf-8").splitlines()
        n_blk = 0
        for i, ln in enumerate(lines):
            m = RM.search(ln)
            if not m:
                continue
            n_blk += 1
            key = f"{m.group(1)}|{m.group(3)}|" + rel.replace("\\", "/")
            if key not in done:
                fails.append(f"G1 未登记判定: {key}")
            fb = fetch.get(key)
            inline = (fb.get("block_type") == "inline") if fb else not ln.lstrip().startswith("<!--")
            if inline:
                # 紧凑列举体例：只查禁字符（行尾锚点含英文引文属合法，排除锚点后查）
                narr = ln[:RM.search(ln).start()]
                if re.search(r"[「」『』＊]", narr) or '"' in narr or is_bad_star(narr):
                    fails.append(f"G3 inline 禁字符: {rel}:{i+1}")
            else:
                summ = lines[i + 3] if i + 3 < len(lines) else ""
                body = summ.split("引用时按")[0].rstrip("。")
                C, L = cjk(body), len(body)
                if C < 30:
                    fails.append(f"G3 字数不足 CJK={C} 总={L}: {rel}:{i+4}")
                elif not args.len_flex and (C > 80 or L > 200):
                    fails.append(f"G3 字数 CJK={C} 总={L}: {rel}:{i+4}")
                elif args.len_flex and (C > 80 or L > 200):
                    print(f"  长度超限(备案): {rel}:{i+4} CJK={C} 总={L}")
                if re.search(r"[「」『』＊]", summ) or '"' in summ or is_bad_star(summ):
                    fails.append(f"G3 禁字符: {rel}:{i+4}")
                if "引用时按" not in summ:
                    fails.append(f"G3 纪律串缺失: {rel}:{i+4}")
                elif summ.count("引用时按") != 1:
                    fails.append(f"G3 纪律串重复 {summ.count('引用时按')} 次: {rel}:{i+4}")
            if fb and fb.get("level"):
                hm = re.search(r"证据等级：(L\d)", lines[i + 1] if i + 1 < len(lines) else "")
                if hm and hm.group(1) != fb["level"]:
                    fails.append(f"G4 等级不符 DB 真值 {fb['level']}: {rel}:{i+2}")
        print(f"G1/G3/G4 {rel.split('/')[-1]}: {n_blk} 块")
    # G5 DB 守恒
    if args.db_claim is not None:
        con = duckdb.connect(MAIN_DB, read_only=True)
        c1 = con.execute("SELECT (SELECT count(*) FROM claim), (SELECT count(*) FROM claim_evidence), (SELECT count(*) FROM evidence)").fetchone()
        con.close()
        if (c1[0], c1[1], c1[2]) != (args.db_claim, args.db_ce, args.db_ev):
            fails.append(f"G5 DB 行数漂移: 基线 {(args.db_claim, args.db_ce, args.db_ev)} → {c1}")
        else:
            print(f"G5 DB 行数守恒: claim={c1[0]} ce={c1[1]} ev={c1[2]}")
    print("----")
    if fails:
        print(f"FAIL {len(fails)} 项:")
        lim = None if args.full_dump else max(0, args.max_fails)
        for x in (fails if lim is None else fails[:lim]):
            print("  !", x)
        if lim is not None and len(fails) > lim:
            print(f"  ……其余 {len(fails) - lim} 项已省略（--full-dump 或 --max-fails N）")
        sys.exit(1)
    print("全部门禁通过（G1–G6）")


# ---------------- --selftest：系统临时目录最小夹具（不读生产库） ----------------
ANCHOR_LINE = "<!-- ROW_MINE: freebsd.misc.100 -->"
HOST_REL = "05-卷册大纲/sub/host.md"
SUMMARY_OK = ("本块摘要正文用于自测校验，叙述完整且不含禁用符号，末尾收束于纪律串。"
              "引用时按原文核对。")
SUMMARY_SHORT = "本块摘要过短。引用时按原文核对。"


def _put(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if isinstance(data, str):
        data = data.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)


def _host_text(summary=SUMMARY_OK, crlf=False, n_blocks=1):
    nl = "\r\n" if crlf else "\n"
    blocks = [nl.join([ANCHOR_LINE, "**证据等级：L3**", "（占位过渡行一）", summary,
                       "（占位过渡行二）"]) for _ in range(n_blocks)]
    return nl.join(blocks) + nl


def _make_fixture(summary=SUMMARY_OK, register=True, fetch_level="L3",
                  host_bytes=None, crlf=False, db_counts=(1, 0, 0),
                  baseline=1, db_expect=None, n_blocks=1, extra_argv=()):
    """构造最小夹具：宿主 md（5 行块）＋ processed.jsonl ＋ fetch 档案 ＋ 临时 duckdb。
    返回 (夹具根目录, main 的 argv)。"""
    root = tempfile.mkdtemp(prefix="oaa_verify_selftest_")
    aud = os.path.join(root, "script", "_db_row_mining", "audit_outline")
    work = os.path.join(aud, "work")
    rel = HOST_REL
    if host_bytes is None:
        host_bytes = _host_text(summary, crlf=crlf, n_blocks=n_blocks).encode("utf-8")
    _put(os.path.join(root, rel), host_bytes)
    if register:
        _put(os.path.join(aud, "processed.jsonl"),
             json.dumps({"key": f"freebsd|100|{rel}"}, ensure_ascii=False) + "\n")
    fb = {"key": f"freebsd|100|{rel}", "block_type": "block", "level": fetch_level,
          "line": 1, "anchor_line": ANCHOR_LINE, "summ_line": summary}
    _put(os.path.join(work, "t1.fetch.jsonl"), json.dumps(fb, ensure_ascii=False) + "\n")
    dbp = os.path.join(root, "04-现代研究文献", "historical_claims.duckdb")
    os.makedirs(os.path.dirname(dbp), exist_ok=True)
    con = duckdb.connect(dbp)
    for t in ("claim", "claim_evidence", "evidence"):
        con.execute(f"CREATE TABLE {t}(i BIGINT)")
    for t, n in zip(("claim", "claim_evidence", "evidence"), db_counts):
        if n:
            con.execute(f"INSERT INTO {t} SELECT * FROM range({n})")
    con.close()
    exp = db_counts if db_expect is None else db_expect
    argv = ["--baseline", str(baseline), "--db-claim", str(exp[0]),
            "--db-ce", str(exp[1]), "--db-ev", str(exp[2])] + list(extra_argv) + [rel]
    return root, argv


def _run_in_fixture(root, argv):
    """把模块级路径全局量临时指向夹具，再跑一次 main()，返回 (退出码, 合并输出)。"""
    global ROOT, OUTLINE, WORK, AUD, MAIN_DB
    saved = (ROOT, OUTLINE, WORK, AUD, MAIN_DB)
    buf = io.StringIO()
    code = 0
    try:
        ROOT = root
        OUTLINE = os.path.join(root, "05-卷册大纲")
        AUD = os.path.join(root, "script", "_db_row_mining", "audit_outline")
        WORK = os.path.join(AUD, "work")
        MAIN_DB = os.path.join(root, "04-现代研究文献", "historical_claims.duckdb")
        old = sys.argv
        sys.argv = ["oaa_verify.py"] + argv
        try:
            with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
                main()
        except SystemExit as e:
            code = e.code if isinstance(e.code, int) else (1 if e.code else 0)
        finally:
            sys.argv = old
    finally:
        ROOT, OUTLINE, WORK, AUD, MAIN_DB = saved
    return code, buf.getvalue()


def selftest():
    cases = [
        ("正常路径（G1–G6 全通）", dict(), 0, [], None),
        ("缺块（G1 未登记判定）", dict(register=False), 1, ["G1"], None),
        ("块数不符（G2 基线漂移）", dict(baseline=2), 1, ["G2"], None),
        ("字数不足（G3）", dict(summary=SUMMARY_SHORT), 1, ["G3"], None),
        ("等级不符（G4）", dict(fetch_level="L2"), 1, ["G4"], None),
        ("DB 行数漂移（G5）", dict(db_expect=(2, 0, 0)), 1, ["G5"], None),
        ("BOM（G6）", dict(host_bytes=b"\xef\xbb\xbf" + _host_text().encode("utf-8")), 1, ["G6"], None),
        ("CRLF（G6）", dict(crlf=True), 1, ["G6"], None),
        ("失败列表默认截断 30 条＋省略提示",
         dict(register=False, n_blocks=35, baseline=35), 1, ["G1"],
         lambda o: o.count("  ! ") == 30 and "其余 5 项已省略" in o),
        ("--max-fails 5 生效",
         dict(register=False, n_blocks=35, baseline=35, extra_argv=("--max-fails", "5")),
         1, ["G1"], lambda o: o.count("  ! ") == 5 and "其余 30 项已省略" in o),
        ("--full-dump 全量 35 条",
         dict(register=False, n_blocks=35, baseline=35, extra_argv=("--full-dump",)),
         1, ["G1"], lambda o: o.count("  ! ") == 35 and "已省略" not in o),
    ]
    print("== oaa_verify --selftest（系统临时目录夹具，不读生产库）==")
    bad = 0
    for title, kw, want, marks, check in cases:
        root, argv = _make_fixture(**kw)
        try:
            code, out = _run_in_fixture(root, argv)
        finally:
            shutil.rmtree(root, ignore_errors=True)
        hit = [l.strip() for l in out.splitlines() if l.strip().startswith("!")]
        ok = (code == want) and all(mk in out for mk in marks) \
            and (check is None or check(out))
        if not ok:
            bad += 1
        detail = "；".join(hit[:2]) if hit else "；".join(
            l for l in out.splitlines() if l.startswith(("G2 ", "G5 ", "全部门禁")))[:120]
        print(f"[{'PASS' if ok else 'FAIL'}] {title}：退出码 {code}（期望 {want}）｜ {detail}")
    print("覆盖：G1 正/负（未登记）、G2 正/负（基线漂移）、G3 正/负（字数不足）、"
          "G4 正/负（等级不符）、G5 正/负（计数漂移）、G6 正/负（BOM、CRLF）、"
          "失败列表截断/--max-fails/--full-dump")
    print("未覆盖（分支级，G1–G6 判据本身均已独立复现）：G3 禁字符／纪律串缺失／"
          "inline 禁字符、G4 缺“证据等级”行分支；判据阈值与语义未改动")
    print(f"== selftest {'PASS' if bad == 0 else 'FAIL'}：{len(cases) - bad}/{len(cases)} 用例通过 ==")
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    main()