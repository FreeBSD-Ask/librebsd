#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""oaa_remap_claims.py — 大纲 claims 清单只读回映检查器（F 线烟测修复件）

背景：F1–F4 的认领清单 beacon/claims_F*.txt 记的是“宿主 .md 相对路径”；05-卷册大纲
目录树经整卷重排后，路径中的卷号／章号／节号多已变化，清单路径大面积失效。本工具
只读比对清单与现行树，给出每条原路径的候选或 UNMATCHED，**绝不改 claims 文件、
绝不猜测多候选**。

判据：
  1) 逐条判断原路径在现行树中是否仍存在 → 存在率；
  2) 对不存在的路径，按“卷号＋章题＋节题去数字前缀”在当前树中找唯一候选
     （节题＝原文件名去掉首部数字前缀；候选为现行树中章目录下同名的节级目录或 .md）；
     无章级段的清单（卷下直属宿主）退回按“卷号＋节题”在整卷内找唯一候选；
  3) 输出“原路径 → EXISTS / 候选 / AMBIGUOUS(n) / UNMATCHED”，统计
     存在率、可唯一回映数、歧义数、未匹配数。
  exit 0 仅当存在率或唯一回映率（存在∪唯一 / 总数）为 100%，否则 1。

**写模式（2026-10-22 立，TD-015 偿还）**：`--write` 把可唯一回映的行**就地改写**为现行路径
（默认 dry-run；ADR-0008 §1.3 CLI 安全默认）。安全轨：
  - 任一条 AMBIGUOUS／UNMATCHED → 拒绝写盘（exit 2，零写入）；
  - 写前 prebak `<file>.prebak-<stamp>`（**已存在即拒写**，防同 stamp 覆盖唯一原始备份）；行数与无用行（空行／# 注）原样保留；UTF-8 无 BOM＋LF；
  - 写后断言：回读逐行校验**每条路径在盘上存在**（目录或 .md），行数不变；
  - 幂等：二跑应 0 条改写（全部 EXISTS）；文件末尾确保恰一个 LF（**路径行计数**不变）。
  - 另三项 fail-closed：`--apply` 须与 `--write` 同用（禁静默退化为检查）；`--stamp` 禁路径分隔符与空值；**空清单（0 条）拒写**。
回映目标可能是**节目录**（目录化后节＝目录，其下诸小节 .md 由 F 线自行展开）或单个 `.md`。

用法：
  python oaa_remap_claims.py --group F1 --check
  python oaa_remap_claims.py --group F1 --write          # dry-run 计划
  python oaa_remap_claims.py --group F1 --write --apply  # 落盘（含 prebak）
  python oaa_remap_claims.py --claims <FILE> --root 05-卷册大纲 --report <FILE>
"""
import argparse
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
BEACON = os.path.join(ROOT, "script", "_db_row_mining", "audit_outline", "beacon")

VOL_RE = re.compile(r"^第(\d+)卷")
CHAP_RE = re.compile(r"^第\d+章-")
# 节题去数字前缀：形如 100.16- / 012.1- / 10.9- 的首部编号（数字与点，后接连字符）
NUM_PREFIX_RE = re.compile(r"^[\d.]+-")


def _utf8_stdout():
    """统一文本输出为 UTF-8 无 BOM、LF。"""
    for st in (sys.stdout, sys.stderr):
        try:
            st.reconfigure(encoding="utf-8", newline="\n")
        except Exception:
            pass


def vol_no(name):
    m = VOL_RE.match(name)
    return int(m.group(1)) if m else None


def strip_chap(name):
    return CHAP_RE.sub("", name, count=1)


def strip_num(name):
    return NUM_PREFIX_RE.sub("", name, count=1)


def stem(name):
    return name[:-3] if name.endswith(".md") else name


def parse_claim(rel):
    """宿主相对路径 → (卷号, 章题, 节题, 是否有章级)；无法解析返回 None。"""
    parts = rel.replace("\\", "/").split("/")
    if len(parts) < 3:
        return None
    v = vol_no(parts[1])
    if v is None:
        return None
    mids = parts[2:-1]
    chap = strip_chap(mids[0]) if mids else ""
    sect = strip_num(stem(parts[-1]))
    return v, chap, sect, bool(mids)


def build_index(root_dir):
    """扫现行树 → (sec_index, vol_index)：
    sec_index[(卷号, 章题, 节题)] → [相对路径…]（章目录下直属的节级目录或 .md）
    vol_index[(卷号, 节题)]       → [相对路径…]（无章级清单的整卷回退用）"""
    sec, volidx = {}, {}
    for vol in sorted(os.listdir(root_dir)):
        vp = os.path.join(root_dir, vol)
        if not os.path.isdir(vp):
            continue
        v = vol_no(vol)
        if v is None:
            continue
        for chap in sorted(os.listdir(vp)):
            cp = os.path.join(vp, chap)
            if not CHAP_RE.match(chap) or not os.path.isdir(cp):
                continue
            ct = strip_chap(chap)
            for ent in sorted(os.listdir(cp)):
                ep = os.path.join(cp, ent)
                if os.path.isdir(ep):
                    st = strip_num(ent)
                elif ent.endswith(".md"):
                    st = strip_num(ent[:-3])
                else:
                    continue
                relp = os.path.relpath(ep, ROOT).replace("\\", "/")
                sec.setdefault((v, ct, st), []).append(relp)
                volidx.setdefault((v, st), []).append(relp)
    return sec, volidx


def resolve_all(claims_file, root_name):
    """→ (results, stats)。results = [(原行, 回映后路径或 None)]，None＝该行未解析；
    stats = dict(total/exist/unique/amb/unmatch)。空行与 # 注行不参与统计，原样保留。"""
    root_dir = os.path.join(ROOT, root_name)
    if not os.path.isdir(root_dir):
        print(f"错误：根目录不存在 {root_dir}", file=sys.stderr)
        return None, None
    with open(claims_file, encoding="utf-8") as fh:
        raw = fh.read().split(chr(10))
    sec, volidx = build_index(root_dir)
    results = []
    st = dict(total=0, exist=0, unique=0, amb=0, unmatch=0)
    for l in raw:
        s = l.strip()
        if not s or s.startswith("#"):
            results.append((l, l))
            continue
        st["total"] += 1
        if os.path.exists(os.path.join(ROOT, s)):
            st["exist"] += 1
            results.append((l, s))
            continue
        parsed = parse_claim(s)
        if parsed is None:
            st["unmatch"] += 1
            results.append((l, None))
            continue
        v, chap, sect, has_chap = parsed
        cands = sec.get((v, chap, sect), []) if has_chap else volidx.get((v, sect), [])
        if len(cands) == 1:
            st["unique"] += 1
            results.append((l, cands[0]))
        elif len(cands) > 1:
            st["amb"] += 1
            results.append((l, None))
        else:
            st["unmatch"] += 1
            results.append((l, None))
    return results, st


def rewrite(claims_file, root_name, apply=False, stamp="20261022"):
    """写模式：可唯一回映的行就地改写为现行路径（默认 dry-run；含 prebak 与写后断言）。"""
    import shutil
    results, st = resolve_all(claims_file, root_name)
    if results is None:
        return 2
    if not stamp or any(c in stamp for c in ("/", chr(92), ":")):
        print("[check] 非法 --stamp：%r（禁路径分隔符与空值）" % stamp, file=sys.stderr)
        return 2
    if st["amb"] or st["unmatch"]:
        print("[check] 存在歧义 %d／未匹配 %d —— 拒绝写盘（零写入）"
              % (st["amb"], st["unmatch"]))
        return 2
    new_lines = [new if new is not None else old for old, new in results]
    changed = sum(1 for old, new in results if new is not None and new.strip() != old.strip())
    total = st["total"]
    print("[plan] 总条数 %d | 已存在 %d | 回映 %d | 改写 %d | 歧义 0 | 未匹配 0"
          % (total, st["exist"], st["unique"], changed))
    if total == 0:
        print("[check] 清单为空（0 条路径）——拒绝写盘（零写入）", file=sys.stderr)
        return 2
    if not apply:
        print("[dry] 未写盘（加 --apply 执行）")
        return 0
    body = chr(10).join(new_lines)
    if not body.endswith(chr(10)):
        body += chr(10)
    if chr(0xFEFF) in body or chr(13) in body:
        print("[check] 产物编码违规（BOM／CRLF）——零写入", file=sys.stderr)
        return 2
    bak = claims_file + ".prebak-" + stamp
    if os.path.exists(bak):
        print("[check] prebak 已存在：%s —— 拒绝覆盖（请改用 --stamp <新时间戳>）"
              % os.path.relpath(bak, ROOT).replace(chr(92), "/"))
        return 2
    shutil.copy2(claims_file, bak)
    print("[prebak] %s" % os.path.relpath(bak, ROOT).replace(chr(92), "/"))
    with open(claims_file, "w", encoding="utf-8", newline=chr(10)) as fh:
        fh.write(body)
    # 写后断言：行数不变＋每条路径在盘存在（目录或 .md）
    with open(claims_file, encoding="utf-8") as fh:
        again = fh.read().split(chr(10))
    n_old = len([1 for l in raw_lines_of(bak) if l.strip() and not l.strip().startswith("#")])
    n_new = len([1 for l in again if l.strip() and not l.strip().startswith("#")])
    missing = []
    for l in again:
        s = l.strip()
        if not s or s.startswith("#"):
            continue
        full = os.path.join(ROOT, s)
        if not (os.path.isdir(full) or (os.path.isfile(full) and s.endswith(".md"))):
            missing.append(s)
    if n_old != n_new or missing:
        print("[check] 写后断言失败：行数 %d→%d、不在盘 %d 条 %s" % (n_old, n_new, len(missing), missing[:3]),
              file=sys.stderr)
        return 2
    print("[assert] 回读：行数 %d 不变、全部路径在盘存在（%d/%d）" % (n_new, n_new, n_new))
    # 幂等复核（本次进程内）
    _, st2 = resolve_all(claims_file, root_name)
    print("[idempotent] 二跑：已存在 %d | 回映 %d | 改动 %d（应 0）"
          % (st2["exist"], st2["unique"], st2["unique"]))
    return 0 if st2["unique"] == 0 else 1


def raw_lines_of(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read().split(chr(10))


def check(claims_file, root_name):
    """只读检查 → (退出码, 报告行列表)。"""
    root_dir = os.path.join(ROOT, root_name)
    if not os.path.isdir(root_dir):
        print(f"错误：根目录不存在 {root_dir}", file=sys.stderr)
        return 2, []
    with open(claims_file, encoding="utf-8") as fh:
        rels = [l.strip() for l in fh if l.strip() and not l.startswith("#")]
    sec, volidx = build_index(root_dir)
    lines = []
    n_exist = n_unique = n_amb = n_unmatch = 0
    for rel in rels:
        if os.path.exists(os.path.join(ROOT, rel)):
            n_exist += 1
            lines.append(f"{rel} → EXISTS")
            continue
        parsed = parse_claim(rel)
        if parsed is None:
            n_unmatch += 1
            lines.append(f"{rel} → UNMATCHED（无法解析卷/章/节）")
            continue
        v, chap, sect, has_chap = parsed
        cands = sec.get((v, chap, sect), []) if has_chap else volidx.get((v, sect), [])
        if len(cands) == 1:
            n_unique += 1
            lines.append(f"{rel} → {cands[0]}")
        elif len(cands) > 1:
            n_amb += 1
            lines.append(f"{rel} → AMBIGUOUS({len(cands)}): " + " | ".join(cands))
        else:
            n_unmatch += 1
            lines.append(f"{rel} → UNMATCHED")
    total = len(rels)
    resolved = n_exist + n_unique
    exist_rate = (n_exist / total) if total else 0.0
    uniq_rate = (resolved / total) if total else 0.0
    ok = bool(total) and (n_exist == total or resolved == total)
    lines += [
        "",
        f"清单：{os.path.relpath(claims_file, ROOT).replace(chr(92), '/')}",
        f"根目录：{root_name}",
        f"总条数：{total}",
        f"存在：{n_exist}（存在率 {exist_rate:.2%}）",
        f"可唯一回映：{n_unique}",
        f"歧义：{n_amb}",
        f"未匹配：{n_unmatch}",
        f"唯一回映率（存在∪唯一 / 总数）：{uniq_rate:.2%}",
        f"判定：{'PASS' if ok else 'FAIL'}",
    ]
    return (0 if ok else 1), lines


def selftest():
    """判据非空自检：临时树内造旧式清单 → 回映落盘 → 断言存在率/行数/幂等/歧义拒写。"""
    import shutil
    import tempfile
    ok = True
    tmp = tempfile.mkdtemp(prefix="remap_st_")
    old_root = globals().get("ROOT")
    try:
        root = os.path.join(tmp, "05-卷册大纲", "第05卷-x", "第050章-y")
        os.makedirs(os.path.join(root, "050.1-z"), exist_ok=True)
        open(os.path.join(root, "050.1-z", "050.1.1-a.md"), "w", encoding="utf-8",
                newline=chr(10)).write("正文。" + chr(10))
        claims = os.path.join(tmp, "claims.txt")
        open(claims, "w", encoding="utf-8", newline=chr(10)).write(
            "05-卷册大纲/第05卷-x/第050章-y/050.1-z.md" + chr(10))
        globals()["ROOT"] = tmp
        rc = rewrite(claims, "05-卷册大纲", apply=True, stamp="selftest")
        body = open(claims, encoding="utf-8").read().strip()
        good = (rc == 0 and os.path.isdir(os.path.join(tmp, body))
                and os.path.exists(claims + ".prebak-selftest"))
        print("[selftest] S1 旧式清单回映落盘＋prebak %s（rc=%d, %s）"
              % ("PASS" if good else "FAIL", rc, body))
        ok &= good
        # 二跑幂等
        bef = open(claims, encoding="utf-8").read()
        rc2 = rewrite(claims, "05-卷册大纲", apply=True, stamp="selftest2")
        idem = (rc2 == 0 and open(claims, encoding="utf-8").read() == bef)
        print("[selftest] S2 二跑幂等（0 改动）%s" % ("PASS" if idem else "FAIL"))
        ok &= idem
        # 不可解析：节题对不上现行树（等价于歧义/未匹配）→ 拒写
        open(os.path.join(root, "050.1-z-b"), "w", encoding="utf-8").close()
        claims2 = os.path.join(tmp, "claims2.txt")
        open(claims2, "w", encoding="utf-8", newline=chr(10)).write(
            "05-卷册大纲/第05卷-x/第050章-y/050.1-旧.md" + chr(10))
        rc3 = rewrite(claims2, "05-卷册大纲", apply=True, stamp="selftest3")
        amb = (rc3 == 2 and not os.path.exists(claims2 + ".prebak-selftest3"))
        print("[selftest] S3 不可解析（未匹配／歧义）拒写（rc=%d，零写入）%s" % (rc3, "PASS" if amb else "FAIL"))
        ok &= amb
        # S4：同 stamp 二跑 → prebak 已存在则拒写（防覆盖唯一原始备份）
        bak_keep = open(claims + ".prebak-selftest2", encoding="utf-8").read()
        rc4 = rewrite(claims, "05-卷册大纲", apply=True, stamp="selftest2")
        keep = (rc4 == 2
                and open(claims + ".prebak-selftest2", encoding="utf-8").read() == bak_keep)
        print("[selftest] S4 同 stamp 拒写（rc=%d，prebak 未被覆盖）%s"
              % (rc4, "PASS" if keep else "FAIL"))
        ok &= keep
        print("[selftest] 合计 %s" % ("PASS" if ok else "FAIL"))
        return 0 if ok else 1
    finally:
        if old_root is not None:
            globals()["ROOT"] = old_root
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    _utf8_stdout()
    ap = argparse.ArgumentParser(description="大纲 claims 清单只读回映检查器")
    ap.add_argument("--claims", help="claims 清单文件（一行一个宿主相对路径）")
    ap.add_argument("--group", choices=["F1", "F2", "F3", "F4"], help="按组取 beacon/claims_F*.txt")
    ap.add_argument("--root", default="05-卷册大纲", help="现行大纲根目录（默认 05-卷册大纲）")
    ap.add_argument("--check", action="store_true", help="执行只读检查（默认动作）")
    ap.add_argument("--write", action="store_true", help="写模式：可唯一回映的行就地改写（默认 dry-run）")
    ap.add_argument("--apply", action="store_true", help="写模式落盘（须与 --write 同用）")
    ap.add_argument("--stamp", default="20261022", help="prebak 时间戳（默认 20261022）")
    ap.add_argument("--report", help="报告输出文件（UTF-8 无 BOM / LF）")
    ap.add_argument("--selftest", action="store_true", help="判据非空自检（临时树）")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    claims = args.claims
    if not claims:
        if not args.group:
            ap.error("需要 --claims FILE 或 --group F1..F4")
        claims = os.path.join(BEACON, f"claims_{args.group}.txt")
    if not os.path.exists(claims):
        print(f"错误：claims 文件不存在 {claims}", file=sys.stderr)
        return 2
    if args.apply and not args.write:
        print("[check] --apply 须与 --write 同用（禁止静默退化为 --check）", file=sys.stderr)
        return 2
    if args.write:
        return rewrite(claims, args.root, apply=args.apply, stamp=args.stamp)
    rc, lines = check(claims, args.root)
    if rc == 2:
        return 2
    text = "\n".join(lines) + "\n"
    sys.stdout.write(text)
    if args.report:
        parent = os.path.dirname(os.path.abspath(args.report))
        if parent:
            os.makedirs(parent, exist_ok=True)
        with open(args.report, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
    return rc


if __name__ == "__main__":
    sys.exit(main())
