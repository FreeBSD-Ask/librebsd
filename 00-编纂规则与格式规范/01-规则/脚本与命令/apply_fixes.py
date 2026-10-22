#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""apply_fixes.py — 大纲邮件素材审计·把 fix 类判定原地应用到宿主 .md（第4行摘要行替换）

原则：
- 只改 fix-format / fix-text 且给了「新摘要句」的条目；keep/remap/存疑/fix-db 不动文件
- 纪律串（「引用时按 …」起）从原第 4 行原样保留；**若新摘要句本身已含纪律串则整行替换**，
  不再拼接（否则纪律串重复——2026-09-29 实测已致 22 行落盘缺陷）；写前断言新行纪律串恰 1 次
- 定位双重校验：行号 + 锚点行内容 + 原摘要行内容三方匹配，任一不符即报错停机
- 单行换单行，文件总行数守恒；幂等（已含新句则跳过）
- 零写入不重写盘（幂等空跑不产生假 diff）；写回保留原文件的尾换行状态——
  无条件 `+ "\n"` 会给原本不带尾换行的宿主补 1 字节，而本函数的行数守恒断言
  用 splitlines 计数会把那 1 字节掩盖掉（2026-10-12 b20 65.1、2026-10-13
  b21 65.9 各中招一次，均由差分门禁 G_D0 的 EOF 字节级断言查出）
用法：python apply_fixes.py <host1相对路径> <host2相对路径> ...
"""
import contextlib
import glob
import io
import json
import os
import re
import shutil
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
JUD = os.path.join(ROOT, "script", "_db_row_mining", "audit_outline", "judgements")
WORK = os.path.join(ROOT, "script", "_db_row_mining", "audit_outline", "work")
OVER22 = os.path.join(WORK, "_over22_fix.json")
TAIL = "引用时按"
# DSLXC 族（13-deepseek 战线收编块）摘要行不用「引用时按」，用「以上为邮件列表当事人…」收尾
ALT_TAIL = "以上为邮件列表当事人"

# 来源标记独占行（【linux邮件提取】等）：DSLXC 块体模板的固定尾元素
TAG_ONLY = re.compile(r"^[【\[（(][^】\]）)]{1,24}[】\]）)]$")
# H 线紧凑内联族（22.4／31.3）块尾分隔符：`---- PK <n>` 指向紧随的下一个 ROW_MINE 锚点
SEP_PK = re.compile(r"^-{3,}\s*PK\s*\d+\s*$")
# markdown 标题（任意级）：叙述章的小节标题落在锚点窗口内，但不是素材摘要
MD_HEAD = re.compile(r"^#{1,6} ")
# 其他战役线的结构性行前缀：机读台账块 / 编排注
STRUCT_HEADS = ("####", "{", "〔")


def is_structural(s):
    """块内非摘要正文的结构性行。误把这些当「重复摘要」会把 DSLXC 族的合法写入整批拒掉
    ——实测 3,167 条 RISK 全部是来源标记独占行，另含 H 线 claim-id 溯源串
    （数据库分析发现｜L4｜…CL-RM-…｜批次 …）、机读台账块、编排注。"""
    if not s:
        return True
    if s.startswith("<!--") or s.startswith("**"):
        return True
    if TAG_ONLY.match(s) or SEP_PK.match(s) or MD_HEAD.match(s) \
            or s.startswith(STRUCT_HEADS):
        return True
    if "CL-RM-" in s or "批次 " in s:
        return True
    return len(s) < 12


def load_judgements():
    jud = {}
    filenames = sorted(glob.glob(os.path.join(JUD, "*.jsonl")))
    # b1fix（字数补写）优先级最高，后加载覆盖主判定；其余主判定先加载
    fix_first = [f for f in filenames if "b1fix_" in os.path.basename(f)]
    rest = [f for f in filenames if "b1fix_" not in os.path.basename(f)]
    for f in rest + fix_first:
        for l in open(f, encoding="utf-8"):
            if l.strip():
                try:
                    r = json.loads(l)
                except ValueError:
                    # 并行组（F1-F4）同目录在途半成品判读文件：跳过坏行不崩
                    print(f"  ! 判读坏行跳过: {os.path.basename(f)}", file=sys.stderr)
                    continue
                if "新摘要句" in r or r.get("判定") in ("fix-format", "fix-text"):
                    jud[r["key"]] = r
    return jud


def load_fetch():
    fetch = {}
    for f in glob.glob(os.path.join(WORK, "*.fetch.jsonl")):
        for l in open(f, encoding="utf-8"):
            if l.strip():
                try:
                    r = json.loads(l)
                except ValueError:
                    continue
                fetch[r["key"]] = r
    return fetch


def load_over22():
    """over22 覆盖表按「db|pk」复合键查找——pk 在各源库各自编号，裸 pk 键
    会把别的库/批次的改写稿安到本批同号块上（跨库污染）。"""
    over22 = {}
    if os.path.exists(OVER22):
        raw = json.load(open(OVER22, encoding="utf-8"))
        for k, v in raw.items():
            if "|" in k:
                over22[k] = v
            else:
                print(f"  ! over22 裸 pk 键已忽略（须 db|pk 复合键）: {k}", file=sys.stderr)
    return over22


def main(hosts, dry_run=False):
    jud = load_judgements()
    fetch = load_fetch()
    over22 = load_over22()
    tot_apply = tot_skip = tot_abandon = 0
    for rel in hosts:
        path = os.path.join(ROOT, rel)
        # 先记原文件的尾换行状态：splitlines 会丢掉它，写回时必须按原样恢复
        with open(path, "rb") as fbr:
            had_lf = fbr.read().endswith(b"\n")
        with open(path, encoding="utf-8", newline="") as fh:
            lines = fh.read().splitlines()
        orig_n = len(lines)
        n_apply = n_skip = n_err = 0
        for key, r in jud.items():
            if r.get("判定") == "fix-db":
                # 情形③ 等级挂账交专项 X1（任务书 §五）；head_line 未随改会造成块内
                # 抬头↔纪律串不一致，故 fix-db 一律不入大纲（与文档串契约一致）
                continue
            if r.get("判定") in ("keep", "remap", "存疑"):
                # 按文档契约这几类一律不动文件。须显式拦：本工具按「新摘要句非空」判定
                # 是否可写，而 keep/存疑 判读的 新摘要句 可能被归一器回填为原 summ_line、
                # 或被写手顺手填了一句改写稿——2026-10-03 F1-05 88.1 实证补丁前一轮
                # 写入 9 条非 fix 行（keep 8＋存疑 1），补丁后重跑得 4269 行 100% 命中 fix 判定。
                continue
            if not (r.get("新摘要句") or r.get("判定") in ("fix-format", "fix-text")):
                continue
            db_pk = "|".join(key.split("|")[:2])
            ns = over22.get(db_pk, "") or r.get("新摘要句") or ""
            if not ns:
                continue
            if "|" not in key or not key.endswith(rel):
                continue
            fb = fetch.get(key)
            if not fb:
                print(f"  ! 无 fetch 档案: {key}", file=sys.stderr)
                n_err += 1
                continue
            ln = fb["line"]  # 锚点行（1-based）
            # 越界先拦：fetch 档案里存在指向宿主行数之外的 line（宿主被收缩或跨档案
            # 键覆盖后未刷新），直接 lines[ln-1] 会 IndexError 使整轮 apply 中断，
            # 前面已写盘的宿主全部失去事后核验。改为按锚点行不匹配处理并计入 n_err。
            if not isinstance(ln, int) or not (1 <= ln <= len(lines)):
                print(f"  ! 锚点行越界: {key} line {ln}（宿主仅 {len(lines)} 行）",
                      file=sys.stderr)
                n_err += 1
                continue
            if lines[ln - 1] != fb["anchor_line"]:
                print(f"  ! 锚点行不匹配: {key} line {ln}", file=sys.stderr)
                n_err += 1
                continue
            inline = fb.get("block_type") == "inline" or not lines[ln - 1].lstrip().startswith("<!--")
            if inline:
                # 紧凑列举体例：整行替换，但必须保留原行尾锚尾巴（含同行多锚），
                # 否则丢锚——B001 丢 814 行、B002 在 161-nd/159-fsd/160-mm 丢 2,769 锚的根因
                orig = lines[ln - 1]
                idx = orig.find("<!--")
                if idx > 0 and orig[idx - 1] == "`":
                    idx -= 1
                if idx >= 0:
                    tail = orig[idx:]
                    if ns.rstrip().endswith("`"):
                        ns = ns.rstrip()[:-1].rstrip()
                    lines[ln - 1] = ns.rstrip() + tail
                else:
                    lines[ln - 1] = ns
                n_apply += 1
                continue
            # 独立行锚型：锚点向下 5 行内找摘要行。窗口一律止于下一个 ROW_MINE 锚点——
            # 否则窗口内命中的纪律串／摘要行可能属于下一块（2026-10-04 F3 波 1 实测 157.6
            # 有 11 条命中下一块锚点行、1 条命中下一块摘要行，旧代码整宿主照写）。
            nxt = len(lines)
            for j in range(ln, len(lines)):
                if lines[j].lstrip().startswith("<!--"):
                    nxt = j
                    break
            hi = min(ln + 5, nxt)
            summ = (fb.get("summ_line") or "").strip()
            si = -1
            # 优先逐字命中 fetch 摘要行。独立行锚型下摘要正文与收尾常分处两行，先搜纪律串
            # 会落到收尾行、旧摘要正文原地残留成双重摘要（F3 波 1 实测 3,189 条）。
            if summ:
                for j in range(ln, hi):
                    if lines[j].strip() == summ:
                        si = j
                        break
            if si < 0:
                for j in range(ln, hi):
                    if TAIL in lines[j]:
                        si = j
                        break
            if si < 0:
                for j in range(ln, hi):
                    if ALT_TAIL in lines[j]:
                        si = j
                        break
            if si < 0:
                print(f"  ! 摘要行（纪律串）未找到: {key} line {ln}", file=sys.stderr)
                n_err += 1
                continue
            # 落点校验：落点须是 fetch 摘要行逐字命中，或是纪律尾行（收尾已含在尾串里）。
            # 二者皆非＝落到了别块的正文，宁可报错也不写入。
            if summ and lines[si].strip() != summ \
                    and TAIL not in lines[si] and ALT_TAIL not in lines[si]:
                print(f"  ! 摘要行落点与 fetch summ_line 不一致: {key} line {ln}", file=sys.stderr)
                n_err += 1
                continue
            # 双重摘要防护：块内若已有另一份非结构性摘要行，写入会与其并存成两份摘要。
            # 结构性行（来源标记／claim-id 溯源串／机读台账／编排注／锚点／抬头）一律豁免。
            # 扫描上界止于本块自己的纪律尾行（si+1）而非下一个锚点：块体以纪律尾收口，
            # 尾行之后的内容属于别块或叙述章。锚点缺失的宿主上，窗口会一路延伸到章节末，
            # 把叙述章正文当成「另一份摘要」拒写——282.2 实测 1 处此类误拒就因 all-or-nothing
            # 挡掉整宿主 436 条合法写入。收窄只缩小扫描范围，不放松块体内的任何判据。
            if summ and lines[si].strip() == summ:
                dup = -1
                for j in range(ln, si + 1):
                    if j == si:
                        continue
                    s = lines[j].strip()
                    if is_structural(s):
                        continue
                    if s == summ or TAIL in s or ALT_TAIL in s:
                        continue
                    dup = j
                    break
                if dup >= 0:
                    print(f"  ! 块内已有另一份摘要行，拒绝写入避免双重摘要: {key} line {dup+1}",
                          file=sys.stderr)
                    n_err += 1
                    continue
            # 幂等判据：先按 tail 规则构造 new_line，再与现行整行比对相等才跳过
            # （勿用「ns 是现行子串」判幂等——重复日期前缀族会让真改动被假跳，2026-09-29 F1/F3-02 实证 13+41 行）
            tail = ""
            pos = lines[si].find(TAIL)
            if pos >= 0:
                tail = lines[si][pos:]
            else:
                pos = lines[si].find(ALT_TAIL)
                if pos >= 0:
                    tail = lines[si][pos:]
            if TAIL in ns or ALT_TAIL in ns:
                # 判读已给完整第 4 行（正文＋纪律串）→ 整行替换；再拼 tail 会使纪律串重复
                new_line = ns
            else:
                new_line = ns + tail
            if new_line == lines[si]:
                n_skip += 1
                continue
            # 纪律串守恒：原行有哪种收尾，新行就须恰含该收尾 1 次；原行无收尾（英文结尾等）不设限
            for mk in (TAIL, ALT_TAIL):
                # ALT_TAIL 只是缺「引用时按」的 DSLXC 族收尾兜底：原行已带主纪律串时，
                # 「以上为邮件列表当事人」会作为「以上为邮件列表当事人陈述」的前缀被误命中，
                # 令 L3 二手转述改写稿假报 0 次——2026-10-03 F1-05 88.1 实证 22 行假拦。
                # 主纪律串已在 loop 首项按 count==1 校验，故此跳过只收窄不改严。
                if mk == ALT_TAIL and TAIL in tail:
                    continue
                if mk in tail and new_line.count(mk) != 1:
                    print(f"  ! 纪律串出现 {new_line.count(mk)} 次（须恰 1 次）: {key}", file=sys.stderr)
                    n_err += 1
                    break
            lines[si] = new_line
            n_apply += 1
        if n_err:
            tot_abandon += 1
            if dry_run:
                print(f"{rel}: 有 {n_err} 处错误，放弃宿主（dry-run 未写盘）", file=sys.stderr)
            else:
                print(f"{rel}: 有 {n_err} 处错误，放弃写盘", file=sys.stderr)
            continue
        tot_apply += n_apply
        tot_skip += n_skip
        if dry_run:
            print(f"{rel}: 将写入 {n_apply} 条（dry-run 未写盘）｜ 幂等跳过 {n_skip} 条"
                  f"｜ 行数守恒 {orig_n}")
            continue
        if n_apply == 0:
            # 零写入不重写盘：无条件补尾换行会给不带尾换行的宿主加 1 字节，
            # 且幂等空跑也会凭空产生 diff（b20 65.1／b21 65.9 各中招一次）
            print(f"{rel}: 应用 {n_apply} ｜ 幂等跳过 {n_skip} ｜ 未写盘（行数守恒 {orig_n}）")
            continue
        with open(path, "w", encoding="utf-8", newline="") as fh:
            fh.write("\n".join(lines) + ("\n" if had_lf else ""))
        assert len(lines) == orig_n, f"{rel} 行数漂移 {orig_n}->{len(lines)}"
        print(f"{rel}: 应用 {n_apply} ｜ 幂等跳过 {n_skip} ｜ 行数守恒 {orig_n}"
              f"｜尾换行={'保留' if had_lf else '去除'}")
    if dry_run:
        print(f"将写入 {tot_apply} 条／幂等跳过 {tot_skip} 条／放弃宿主 {tot_abandon} 个"
              f"（dry-run 未写盘）")
    return tot_apply, tot_skip, tot_abandon


# ---------------- --selftest：系统临时目录夹具 ----------------
HOST_REL = "05-卷册大纲/sub/host.md"
ANCHOR_LINE = "<!-- ROW_MINE: freebsd.misc.100 -->"
OLD_SUMM = "原摘要正文，用于自测校验定位路径。引用时按原文核对。"
NEW_SUMM = "改写后的摘要正文，用于自测校验替换路径。引用时按原文核对。"
HOST_TEXT = "\n".join([ANCHOR_LINE, "**证据等级：L3**", "（占位过渡行一）", OLD_SUMM,
                       "（占位过渡行二）"]) + "\n"


def _put(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if isinstance(data, str):
        data = data.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)


def _read(path):
    with open(path, "rb") as fh:
        return fh.read()


def _make_fixture(jud_rows, fetch=True, text=HOST_TEXT):
    root = tempfile.mkdtemp(prefix="oaa_apply_selftest_")
    aud = os.path.join(root, "script", "_db_row_mining", "audit_outline")
    jud_dir, work = os.path.join(aud, "judgements"), os.path.join(aud, "work")
    _put(os.path.join(root, HOST_REL), text)
    _put(os.path.join(jud_dir, "batch_test.jsonl"),
         "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in jud_rows))
    if fetch:
        fb = {"key": f"freebsd|100|{HOST_REL}", "block_type": "block", "level": "L3",
              "line": 1, "anchor_line": ANCHOR_LINE, "summ_line": OLD_SUMM}
        _put(os.path.join(work, "t1.fetch.jsonl"), json.dumps(fb, ensure_ascii=False) + "\n")
    return root


def _run_fixture(root, dry_run=False):
    global ROOT, JUD, WORK, OVER22
    saved = (ROOT, JUD, WORK, OVER22)
    buf = io.StringIO()
    try:
        ROOT = root
        JUD = os.path.join(root, "script", "_db_row_mining", "audit_outline", "judgements")
        WORK = os.path.join(root, "script", "_db_row_mining", "audit_outline", "work")
        OVER22 = os.path.join(WORK, "_over22_fix.json")
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
            main([HOST_REL], dry_run)
    finally:
        ROOT, JUD, WORK, OVER22 = saved
    return buf.getvalue()


def selftest():
    print("== apply_fixes --selftest（系统临时目录夹具）==")
    cases = []

    good = [{"key": f"freebsd|100|{HOST_REL}", "判定": "fix-text", "新摘要句": NEW_SUMM}]
    root = _make_fixture(good)
    try:
        host = os.path.join(root, HOST_REL)
        before = _read(host)
        out1 = _run_fixture(root)
        after1 = _read(host)
        lines = after1.decode("utf-8").splitlines()
        ok = ("应用 1" in out1) and after1 != before and len(lines) == 5 and lines[3] == NEW_SUMM
        cases.append(("正常替换（单行换单行、行数守恒）", ok, out1.strip().splitlines()[-1]))
        out2 = _run_fixture(root)
        after2 = _read(host)
        ok2 = ("幂等跳过 1" in out2) and ("未写盘" in out2) and after2 == after1
        cases.append(("幂等跳过（二次运行不重写盘）", ok2, out2.strip().splitlines()[-1]))
    finally:
        shutil.rmtree(root, ignore_errors=True)

    bad = [{"key": f"freebsd|999|{HOST_REL}", "判定": "fix-text", "新摘要句": NEW_SUMM}]
    root = _make_fixture(bad)
    try:
        host = os.path.join(root, HOST_REL)
        before = _read(host)
        out = _run_fixture(root)
        ok = ("无 fetch 档案" in out) and ("放弃写盘" in out) and _read(host) == before
        cases.append(("坏 key（无 fetch 档案）→ 整宿主放弃、零写盘", ok,
                      [l for l in out.splitlines() if "放弃" in l][0]))
    finally:
        shutil.rmtree(root, ignore_errors=True)

    root = _make_fixture(good)
    try:
        host = os.path.join(root, HOST_REL)
        before = _read(host)
        out = _run_fixture(root, dry_run=True)
        ok = ("将写入 1 条" in out) and ("放弃宿主 0 个" in out) and _read(host) == before
        cases.append(("--dry-run（计数但不写盘）", ok,
                      [l for l in out.splitlines() if l.startswith("将写入")][0]))
    finally:
        shutil.rmtree(root, ignore_errors=True)

    bad_n = 0
    for title, ok, detail in cases:
        if not ok:
            bad_n += 1
        print(f"[{'PASS' if ok else 'FAIL'}] {title}｜ {detail}")
    print("覆盖：正常替换、幂等跳过、坏 key 整宿主放弃、--dry-run 零写盘")
    print("未覆盖（分支级）：inline 整行替换与尾锚保留、块内双重摘要拦截、纪律串重复拦截")
    print("——三类须更复杂宿主夹具，未纳入；本次三项目标路径均已断言")
    print(f"== selftest {'PASS' if bad_n == 0 else 'FAIL'}：{len(cases) - bad_n}/{len(cases)} 用例通过 ==")
    return 0 if bad_n == 0 else 1


if __name__ == "__main__":
    argv = sys.argv[1:]
    # --help/-h 最先处理：打印用法后即退，不读 judgements、不写盘（零副作用）
    if "--help" in argv or "-h" in argv:
        print(__doc__)
        print("说明：本工具默认直接写盘（无 --apply 开关）；加 --dry-run 只计数不写盘；"
              "--selftest 跑内置系统临时目录夹具。")
        sys.exit(0)
    if "--selftest" in argv:
        sys.exit(selftest())
    if not argv:
        print(__doc__)
        sys.exit(2)
    # 只识别已定义开关，其余参数一律按宿主路径处理（与旧解析一致，不误判组合）
    dry = "--dry-run" in argv
    hosts = [a for a in argv if a != "--dry-run"]
    if not hosts:
        print(__doc__)
        sys.exit(2)
    main(hosts, dry)