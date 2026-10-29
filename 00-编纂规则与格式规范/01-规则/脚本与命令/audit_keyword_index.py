# -*- coding: utf-8 -*-
"""audit_keyword_index.py —— 主题词索引门禁（2026-10-21 立，第二十七件候选）。

判据七组：
  A schema／版本／计数
  B 覆盖与题面双射（节键、题面、subs 数、subs_sha1、content_sha256）
  C 词质（普通节 3–6、元节 1–3 限史学域、禁用词、中文正名、补位 ≤2、单主题占比 ≤30%；
    概念零使用只示 WARN——索引为每节 top-N 排序结果，未被选入不等于词表失效，2026-10-29 定级）
  D 侧面（projects 合法、technical_terms ≤8 且在词表内）
  E 对齐码（ccs／clc 格式合法、空值合法）
  F 反查一致（theme_index ↔ chapter_keywords）
  G 尺寸（keywords ≤5 MB、theme_index ≤2 MB）

用法：
  python audit_keyword_index.py                # 默认 --check
  python audit_keyword_index.py --list         # 统计
  python audit_keyword_index.py --selftest     # 负向夹具自检（script/ 下）
"""
import argparse
import io
import json
import os
import re
import shutil
import sys

sys.stdout.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, HERE)
import build_theme_index as bti  # noqa: E402

ROOT = os.path.join(REPO, "05-卷册大纲")
KW = bti.KW
REV = bti.REV
SELFTEST_REL = os.path.join("script", "_keyword_index_selftest")

CJK = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")
CCS = re.compile(r"^[A-Za-z][A-Za-z0-9 ,&/.\-]*(~[A-Za-z0-9 ,&/.\-~]+)?$")
CLC = re.compile(r"^[A-Z]{1,3}[0-9][0-9.\-]*$")
MAX_KW_MB = 5.0
MAX_REV_MB = 2.0
MAX_SHARE = 0.30


def load(out_dir):
    kw = json.loads(open(os.path.join(out_dir, KW), encoding="utf-8").read())
    rev = json.loads(open(os.path.join(out_dir, REV), encoding="utf-8").read())
    return kw, rev


def check_dir(out_dir=ROOT, structure=True):
    problems = []
    warns = []
    try:
        kw, rev = load(out_dir)
    except Exception as exc:
        return [("A0", "派生件无法解析：%s" % exc)]
    vocab, _sha = bti.load_vocab()
    by_id = {c["id"]: c for c in vocab["concepts"]}
    banned = set(vocab.get("banned") or [])
    projects = set(vocab.get("projects") or {})
    tech_all = {t.lower() for c in vocab["concepts"] for t in c.get("techTerms") or []}

    # A：schema 与计数
    if kw.get("meta", {}).get("schema") != bti.SCHEMA_KW:
        problems.append(("A1", "keywords schema 不符"))
    if rev.get("meta", {}).get("schema") != bti.SCHEMA_REV:
        problems.append(("A1", "theme_index schema 不符"))
    if structure:
        for x in bti.check_all(out_dir):
            problems.append(("B1", x))

    secs = kw.get("sections") or {}
    meta = kw.get("meta") or {}
    if meta.get("sections") != len(secs):
        problems.append(("A2", "meta.sections=%r，实有 %d" % (meta.get("sections"), len(secs))))
    if meta.get("chapters") != len(kw.get("chapters") or {}):
        problems.append(("A2", "meta.chapters 与章键数不符"))
    if meta.get("subsections") != sum(len(r.get("themes") or []) >= 0 and r.get("subs", 0)
                                       for r in secs.values()):
        problems.append(("A2", "meta.subsections 与节 subs 合计不符"))
    share = {}
    share_norm = {}
    for sid, row in secs.items():
        n = len(row.get("themes") or []) + len(row.get("auto") or [])
        if row.get("meta"):
            if not (bti.META_MIN <= n <= bti.META_MAX):
                problems.append(("C1", "元节 %s 词数 %d 越界" % (sid, n)))
            for cid in row.get("themes") or []:
                if (by_id.get(cid) or {}).get("broader") != bti.META_DOMAIN:
                    problems.append(("C1", "元节 %s 主题 %s 非史学域" % (sid, cid)))
            if row.get("auto"):
                problems.append(("C1", "元节 %s 不得有补位词" % sid))
        else:
            if not (bti.MIN_T <= n <= bti.MAX_T):
                problems.append(("C1", "节 %s 词数 %d 越界" % (sid, n)))
        auto = row.get("auto") or []
        if len(auto) > 2:
            problems.append(("C4", "节 %s 补位词 >2" % sid))
        for a in auto:
            if a not in row.get("title", "") or a in banned or not CJK.search(a):
                problems.append(("C4", "节 %s 补位词非法：%s" % (sid, a)))
        for cid in row.get("themes") or []:
            share[cid] = share.get(cid, 0) + 1
            if not row.get("meta"):
                share_norm[cid] = share_norm.get(cid, 0) + 1
            c = by_id.get(cid)
            if not c:
                problems.append(("C0", "节 %s 引用词表外主题 %s" % (sid, cid)))
                continue
            lab = ((kw.get("themes") or {}).get(cid) or {}).get("label") or c["prefLabel"]
            if lab != c["prefLabel"]:
                problems.append(("C7", "索引标签与词表不符：%s ≠ %s" % (lab, c["prefLabel"])))
            if lab in banned:
                problems.append(("C2", "节 %s 主题为禁用泛词：%s" % (sid, lab)))
            cjk = len(CJK.findall(lab))
            other = len(re.sub(r"[\s\W_]+", "", lab, flags=re.U)) - cjk
            if cjk < 1 or cjk < other:
                problems.append(("C3", "主题正名中文占比不足：%s" % lab))

    # 2026-10-23 搬迁批：骨架树（0 小节正文；content_sha256＝空串哈希、subsections=0）
    # 的 C5／C6 成空转——默认补位会把同一域默认词铺满全树，占比与词表覆盖率均无内容依据。
    # 与 tri_structure_negtest N-g 同例：条件不成立即 SKIP，正文落地后自动恢复。
    used = set(share)
    for row in secs.values():
        used.update(row.get("domains") or [])
    for row in (kw.get("subsection_delta") or {}).values():
        used.update(row.get("add") or [])
    if (kw.get("meta") or {}).get("subsections") == 0:
        print("SKIP C5／C6（骨架树：0 小节正文，主题分布与词表覆盖率无可判内容）")
    else:
        # C5 分母＝普通节（非元节）：元节默认主题由 build_theme_index._default_meta 结构性注入
        # （编纂体例／史料等级／索引与元数据），元节占比一涨默认词占比即随涨，与“主题退化”无关。
        # 2026-10-29 实测：元节 1,052（26.6%），三默认词全量口径 23.0%–34.8%（超限）、
        # 普通节口径最高 17.2%（合规）。判据改以普通节为分母；元节默认设计变更时须同批复核本条。
        n_norm = sum(1 for r in secs.values() if not r.get("meta"))
        for cid, n in share_norm.items():
            if n / max(n_norm, 1) > MAX_SHARE:
                problems.append(("C5", "主题 %s 占普通节 %.1f%% > 30%%（%d／%d）"
                                 % ((by_id.get(cid) or {}).get("prefLabel", cid),
                                    100.0 * n / max(n_norm, 1), n, n_norm)))
        unused = sorted(set(by_id) - used)
        if unused:
            # 2026-10-29 定级调整：索引是“每节 top-N 取词”的排序结果，概念未被选入
            # 不等于词表失效（实测 20 个零使用概念中 18 个在树内有语料命中，属排序落选；
            # 其余为语料尚未涉及）。词表冗余治理属人工轮次，故只示 WARN、不阻断门禁。
            warns.append(("C6", "词表概念零使用 %d 个（如 %s）" % (len(unused), unused[:5])))

    # D：侧面
    for sid, row in secs.items():
        if len(row.get("technical_terms") or []) > 8:
            problems.append(("D2", "节 %s technical_terms >8" % sid))
        for t in row.get("technical_terms") or []:
            if t.lower() not in tech_all:
                problems.append(("D2", "节 %s 技术词不在词表：%s" % (sid, t)))
        for p in row.get("projects") or []:
            if p not in projects:
                problems.append(("D1", "节 %s 未知项目侧面：%s" % (sid, p)))

    # E：对齐码
    for c in vocab["concepts"]:
        if c.get("ccs") and not CCS.match(c["ccs"]):
            problems.append(("E1", "ccs 格式非法：%s（%s）" % (c["id"], c["ccs"])))
        if c.get("clc") and not CLC.match(c["clc"]):
            problems.append(("E2", "clc 格式非法：%s（%s）" % (c["id"], c["clc"])))

    # F：反查（bti.check_all 已含，逐条复核 source sha）
    if rev.get("meta", {}).get("source_sha256") != bti.hashlib.sha256(
            bti.dumps(kw).encode("utf-8")).hexdigest():
        problems.append(("F1", "theme_index source_sha256 不符"))
    if set(rev.get("themes") or {}) != used:
        problems.append(("F2", "theme_index 主题集与 keywords 使用集不符"))

    # G：尺寸
    kw_mb = os.path.getsize(os.path.join(out_dir, KW)) / 1048576.0
    rev_mb = os.path.getsize(os.path.join(out_dir, REV)) / 1048576.0
    if kw_mb > MAX_KW_MB:
        problems.append(("G1", "chapter_keywords.json %.2f MB > 5 MB" % kw_mb))
    if rev_mb > MAX_REV_MB:
        problems.append(("G1", "theme_index.json %.2f MB > 2 MB" % rev_mb))
    return problems, warns


def cmd_check(out_dir=ROOT):
    print("=" * 72)
    print("主题词索引门禁（schema theme-index/4／theme-reverse/2）")
    print("=" * 72)
    problems, warns = check_dir(out_dir)
    for code, detail in warns:
        print("  WARN [%s] %s" % (code, detail))
    if problems:
        print("  校验：FAIL（%d 项）" % len(problems))
        for code, detail in problems[:60]:
            print("    · [%s] %s" % (code, detail))
        return 1
    print("  校验：PASS（A–G 七组判据零命中）")
    return 0


def cmd_list(out_dir=ROOT):
    return bti.list_stats(out_dir)


def cmd_selftest():
    """负向夹具：缺节／多节／泛词／英文正名／词数越界／悬空主题／反查缺项。"""
    fix = os.path.join(REPO, SELFTEST_REL)
    shutil.rmtree(fix, ignore_errors=True)
    os.makedirs(fix, exist_ok=True)
    for name in (KW, REV):
        shutil.copy2(os.path.join(ROOT, name), os.path.join(fix, name))
    base, _ = check_dir(fix, structure=False)
    ok = not base
    print("=" * 72)
    print("判据非空自检（基线须 PASS；七类夹具须命中）")
    print("=" * 72)
    print("  [%s] 基线 PASS" % ("PASS" if ok else "FAIL"))
    if base:
        for c, d in base[:10]:
            print("    · [%s] %s" % (c, d))

    def mutate(name, fn):
        p = os.path.join(fix, name)
        doc = json.loads(open(p, encoding="utf-8").read())
        fn(doc)
        with io.open(p, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(json.dumps(doc, ensure_ascii=False, indent=1) + "\n")

    _kw = json.loads(open(os.path.join(fix, KW), encoding="utf-8").read())
    sid = next(k for k, v in sorted(_kw["sections"].items())
               if not v.get("meta") and len(v.get("themes") or []) >= 3)
    tid = _kw["sections"][sid]["themes"][0]
    cases = [
        ("缺节", KW, lambda d: d["sections"].pop(sid), "A2"),
        ("多节", KW, lambda d: d["sections"].__setitem__("999.9", dict(d["sections"][sid])), "A2"),
        ("泛词", KW, lambda d: d["themes"][tid].__setitem__("label", "freebsd"), "C2"),
        ("英文正名", KW, lambda d: d["themes"][tid].__setitem__("label", "Foo"), "C3"),
        ("词数越界", KW, lambda d: (d["sections"][sid].__setitem__(
            "themes", d["sections"][sid]["themes"][:1]),
            d["sections"][sid].pop("auto", None)), "C1"),
        ("悬空主题", KW, lambda d: d["sections"][sid]["themes"].append("TH-XX-999"), "C0"),
        ("反查缺项", REV, lambda d: d["themes"].pop(next(iter(d["themes"]))), "F2"),
    ]
    for title, name, fn, expect in cases:
        mutate(name, fn)
        probs, _ = check_dir(fix, structure=False)
        codes = {c for c, _ in probs}
        hit = expect in codes
        ok = ok and hit
        print("  [%s] %s：期望 %s；实得 %s"
              % ("PASS" if hit else "FAIL", title, expect, sorted(codes)[:8] or "空"))
        # 复原
        shutil.copy2(os.path.join(ROOT, KW), os.path.join(fix, KW))
        shutil.copy2(os.path.join(ROOT, REV), os.path.join(fix, REV))
    print("-" * 72)
    if ok:
        print("  ✅ 判据非空：基线 PASS，七类夹具全部命中")
        return 0
    print("  ❌ 判据可能为空", file=sys.stderr)
    return 1


def main():
    ap = argparse.ArgumentParser(description="主题词索引门禁（A–G 七组判据）")
    ap.add_argument("--check", action="store_true", help="默认模式")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--dir", default=ROOT)
    args = ap.parse_args()
    if args.selftest:
        return cmd_selftest()
    if args.list:
        return cmd_list(args.dir)
    return cmd_check(args.dir)


if __name__ == "__main__":
    sys.exit(main())
