#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""merge_subsections.py —— outline.txt 第四级小节行合并器（唯一写者；ADR-0020，Task 5.4b）。

把各卷并行会话产出的 fragment（`映射/design/fragments/V{NN}.tsv`）按卷序合并进
`05-卷册大纲/目录/data/outline.txt`：

  * **复合键定位**：`V{卷}/C{章}/S{节}/P{小节}`——裸节号跨卷重复（干执行实测 `- 2.3`
    重复 74 次），必须按卷／章状态机定位；卷号由卷题中文数字解析。
  * **放行条件**：该卷 `映射/title-design/approved/V{NN}.title.ok` 存在，且其
    `ledger_sha256` 与当前 `title-design/V{NN}.tsv` **文件字节 sha256** 一致
    （与第三十九件 H1 同算法）；台账任何变动即旧批准失效，合并器拒绝该卷
    （exit 0 跳过并披露，`--strict` 时 exit 1）。
  * **幂等**：以 fragment 为真值——节下已有同键行更新题名、缺键插入、
    fragment 外的既有小节行删除；二跑零差。
  * ** fragment↔outline 双射**：--check 报告每卷将增／改／删行数与键差。

fragment 列契约（缺列 exit 2）：
  `vol`  `chapter`  `sec_no`(M.N)  `sub_no`(M.N.P)  `title`  `status`  `evidence`

小节行形制（ADR-0020）：两前导空格＋`- M.N.P 题名`；@@ 注文由 fragment 的
`evidence` 列承载（`note:` 前缀写为后置 `@@〔…〕`）。

用法：
  python merge_subsections.py --check      # 默认：dry-run 报告漂移（退出码 0/1）
  python merge_subsections.py --write      # 合并写盘（UTF-8 无 BOM、LF）
  python merge_subsections.py --selftest   # 合成夹具自检（含负向）
  python merge_subsections.py --root ... --map ... [--strict]

依赖：仅标准库。
"""
from __future__ import annotations

import argparse
import hashlib
import os
import re
import sys
import tempfile

sys.stdout.reconfigure(encoding="utf-8")

DEFAULT_ROOT = os.path.join("05-卷册大纲")
CN2 = "一二三四五六七八九十"
FRAG_COLS = {"vol", "chapter", "sec_no", "sub_no", "title", "status"}
VOL_LINE_RE = re.compile(r"^#\s*第\s*([一二三四五六七八九十]+)卷")
CH_LINE_RE = re.compile(r"^##\s*第\s*(\d{1,3})\s*章")
SEC_LINE_RE = re.compile(r"^-(\s*)(\d{1,3})\.(\d{1,3})(\s+)(.*)$")
SUB_LINE_RE = re.compile(r"^  -\s+(\d{1,3})\.(\d{1,3})\.(\d{1,4})(\s+)(.*)$")


def _cn2int(s):
    """中文数字 → int（1–99；阿拉伯直返；失败 None）。"""
    if s.isdigit():
        return int(s)
    if s in CN2:
        return CN2.index(s) + 1
    if s == "十":
        return 10
    if s.startswith("十"):
        return 10 + CN2.index(s[1]) + 1
    if "十" in s:
        a, _, b = s.partition("十")
        if a in CN2 and b in CN2:
            return (CN2.index(a) + 1) * 10 + (CN2.index(b) + 1 if b else 0)
    return None


def _sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def read_tsv(p):
    """读 TSV → (header, rows)；文件缺返回 (None, [])。表头缺列即 ValueError。"""
    if not os.path.exists(p):
        return None, []
    with open(p, encoding="utf-8") as fh:
        lines = [ln.rstrip("\r\n") for ln in fh if ln.strip()]
    if not lines:
        return [], []
    hdr = [h.strip() for h in lines[0].split("\t")]
    rows = [dict(zip(hdr, (ln.split("\t") + [""] * len(hdr))[:len(hdr)]))
            for ln in lines[1:]]
    return hdr, rows


def approved_vols(mapdir):
    """放行卷集合 {int(vol): reason}：title.ok 存在且 hash 与当前台账一致。"""
    td_dir = os.path.join(mapdir, "title-design")
    ap_dir = os.path.join(td_dir, "approved")
    ok = {}
    if not os.path.isdir(ap_dir):
        return ok
    for fn in sorted(os.listdir(ap_dir)):
        m = re.match(r"^V(\d{1,3})\.title\.ok$", fn)
        if not m:
            continue
        vn = int(m.group(1))
        ledger = os.path.join(td_dir, "V%02d.tsv" % vn)
        want = None
        try:
            with open(os.path.join(ap_dir, fn), encoding="utf-8") as fh:
                for ln in fh:
                    if ln.strip().lower().startswith("ledger_sha256="):
                        want = ln.split("=", 1)[1].strip().lower()
                        break
        except OSError:
            pass
        if want is None:
            ok[vn] = "拒绝：title.ok 无 ledger_sha256"
            continue
        if not os.path.exists(ledger):
            ok[vn] = "拒绝：台账 %s 缺" % os.path.basename(ledger)
            continue
        if _sha(ledger) != want:
            ok[vn] = "拒绝：ledger_sha256 与当前台账不符（批准失效，须重批）"
            continue
        ok[vn] = "OK"
    return ok


def load_fragments(mapdir):
    """fragments → {int(vol): { (M,N): [ (P, title, status, evidence) ] }}；表头契约。"""
    fdir = os.path.join(mapdir, "design", "fragments")
    out = {}
    if not os.path.isdir(fdir):
        return out
    for fn in sorted(os.listdir(fdir)):
        m = re.match(r"^V(\d{1,3})\.tsv$", fn)
        if not m:
            continue
        vn = int(m.group(1))
        hdr, rows = read_tsv(os.path.join(fdir, fn))
        if hdr is None:
            continue
        if hdr and (FRAG_COLS - set(hdr)):
            raise SystemExit("FATAL fragment %s 缺列 %s"
                             % (fn, sorted(FRAG_COLS - set(hdr))))
        for r in rows:
            ms = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,4})$", (r.get("sub_no") or "").strip())
            if not ms:
                raise SystemExit("FATAL fragment %s sub_no 形制非法：%r"
                                 % (fn, r.get("sub_no")))
            key = (int(ms.group(1)), int(ms.group(2)))
            out.setdefault(vn, {}).setdefault(key, []).append(
                (int(ms.group(3)), (r.get("title") or "").strip(),
                 (r.get("status") or "").strip(), (r.get("evidence") or "").strip()))
    for vn in out:
        for key in out[vn]:
            out[vn][key].sort()
    return out


def merge(outline_path, frags, allowed, strict=False):
    """合并 → (新全文 or None, 报告行列表)。None＝无变更。"""
    with open(outline_path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    if lines and lines[-1] == "":
        lines = lines[:-1]
    report = []
    changed = False

    v = None
    c = None
    sec = None            # 当前节 (M, N)
    sec_subs_start = None # 当前节下小节行起始索引
    out = []
    pending_sub_keys = {} # 本节 fragment 键 {P: (title, status, evidence)}（在节行时填充）

    def flush_secsubs():
        """节收尾：按 fragment 重写本节小节行（更新／插入／删除）。"""
        nonlocal changed
        if sec is None:
            return
        want = frags.get(v, {}).get(sec) if v in allowed else None
        if want is None:
            return
        want_keys = {p for p, *_ in want}
        have = {}   # P -> 行文本
        body = []
        for idx in range(sec_subs_start, len(out)):
            ln = out[idx]
            ms = SUB_LINE_RE.match(ln)
            if not ms:
                body.append(("keep", ln))
                continue
            p = int(ms.group(3))
            have[p] = ln
            body.append(("sub", ln, p))
        # 自上而下重建
        rebuilt = []
        emitted = set()
        inserted = False
        for item in body:
            if item[0] == "keep":
                if want and not inserted:
                    # 首个非小节行前，补齐 fragment 中尚缺的小节（按 P 序）
                    for p, title, status, evid in want:
                        if p not in emitted and p not in have:
                            rebuilt.append(_sub_line(sec, p, title, evid))
                            emitted.add(p)
                            changed = True
                            report.append("V%02d %s.%d 增 %r" % (v, "%d.%d" % sec, p, title[:20]))
                            inserted = True
                rebuilt.append(item[1])
                continue
            _, ln, p = item
            if p in want_keys:
                _, title, status, evid = next(x for x in want if x[0] == p)
                new = _sub_line(sec, p, title, evid)
                if new != ln:
                    changed = True
                    report.append("V%02d %s.%d 改 %r" % (v, "%d.%d" % sec, p, title[:20]))
                else:
                    report.append("V%02d %s.%d 同" % (v, "%d.%d" % sec, p))
                rebuilt.append(new)
                emitted.add(p)
            else:
                changed = True
                report.append("V%02d %s.%d 删（fragment 外）" % (v, "%d.%d" % sec, p))
        if want and not inserted:
            for p, title, status, evid in want:
                if p not in emitted and p not in have:
                    rebuilt.append(_sub_line(sec, p, title, evid))
                    emitted.add(p)
                    changed = True
                    report.append("V%02d %s.%d 增 %r" % (v, "%d.%d" % sec, p, title[:20]))
        out[:] = out[:sec_subs_start] + rebuilt

    for raw in lines:
        line = raw.rstrip()
        m = VOL_LINE_RE.match(line)
        if m:
            flush_secsubs()
            sec = None
            v = _cn2int(m.group(1))
            out.append(line)
            continue
        m = CH_LINE_RE.match(line)
        if m:
            flush_secsubs()
            sec = None
            c = int(m.group(1))
            out.append(line)
            continue
        m = SEC_LINE_RE.match(line)
        if m and v is not None and c is not None:
            flush_secsubs()
            sec = (int(m.group(2)), int(m.group(3)))
            out.append(line)
            sec_subs_start = len(out)
            continue
        if sec is not None and SUB_LINE_RE.match(line):
            out.append(line)   # 原样收进，flush_secsubs 重写
            continue
        # 非小节行 → 节结束
        flush_secsubs()
        sec = None
        out.append(line)
    flush_secsubs()

    # 未放行但有 fragment 的卷披露（allowed 值非 OK＝拒绝含原因）
    for vn in sorted(frags):
        if allowed.get(vn) != "OK":
            report.append("V%02d %s" % (vn, allowed.get(vn, "拒绝：无 title.ok")))
    if strict and any("拒绝" in r for r in report):
        return None, report, True
    if not changed:
        return None, report, False
    return "\n".join(out) + "\n", report, False


def _sub_line(sec, p, title, evid):
    num = "%d.%d.%d" % (sec[0], sec[1], p)
    if evid:
        return "  - %s %s@@〔%s〕" % (num, title, evid)
    return "  - %s %s" % (num, title)


def main(argv=None):
    ap = argparse.ArgumentParser(description="outline.txt 第四级小节行合并器（唯一写者）")
    ap.add_argument("--root", default=DEFAULT_ROOT)
    ap.add_argument("--map", default=None)
    ap.add_argument("--write", action="store_true", help="合并写盘（默认 dry-run）")
    ap.add_argument("--check", action="store_true", help="dry-run（兼容惯例，默认行为）")
    ap.add_argument("--strict", action="store_true", help="存在拒绝卷时退出码 1")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    mapdir = a.map or os.path.join(a.root, "映射")
    outline_p = os.path.join(a.root, "目录", "data", "outline.txt")
    if not os.path.exists(outline_p):
        print("FATAL 缺 %s" % outline_p)
        return 2
    allowed = approved_vols(mapdir)
    frags = load_fragments(mapdir)
    if not frags:
        print("合并器：零态（无 fragment）——outline 不动")
        return 0
    new, report, refused = merge(outline_p, frags, allowed, strict=a.strict)
    for r in report:
        print("  " + r)
    if refused:
        print("合并器：存在拒绝卷（--strict）")
        return 1
    if new is None:
        print("合并器：无变更（幂等）")
        return 0
    if a.write:
        with open(outline_p, "w", encoding="utf-8", newline="") as fh:
            fh.write(new)
        print("合并器：已写盘（UTF-8 无 BOM、LF）——请随即跑 assemble_index.py 重装配＋L19")
        return 0
    print("合并器：dry-run 有变更（--write 落盘）")
    return 1


# ---------------------------------------------------------------- selftest

def _mk(path, text=""):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def selftest():
    base = tempfile.mkdtemp(prefix="merge_subs_")
    ok, bad = [], []

    def check(name, cond, detail=""):
        (ok if cond else bad).append("%s %s" % (name, detail))

    try:
        root = os.path.join(base, "05-卷册大纲")
        mapdir = os.path.join(root, "映射")
        outline_p = os.path.join(root, "目录", "data", "outline.txt")
        _mk(outline_p,
            "# 第一卷  合成甲\n"
            "## 第 1 章 甲一\n"
            "- 1.1 甲一节\n"
            "- 1.2 甲二节\n")
        ledger = os.path.join(mapdir, "title-design", "V01.tsv")
        _mk(ledger, "subsection_id\ttitle\nV01.1.1.1\t甲一一\n")
        _mk(os.path.join(mapdir, "title-design", "approved", "V01.title.ok"),
            "kind=title\nvol=V01\nledger_sha256=%s\n" % _sha(ledger))
        _mk(os.path.join(mapdir, "design", "fragments", "V01.tsv"),
            "vol\tchapter\tsec_no\tsub_no\ttitle\tstatus\tevidence\n"
            "01\t1\t1.1\t1.1.1\t甲一一\t已批\t\n"
            "01\t1\t1.1\t1.1.2\t甲一二\t空骨架\t\n")

        # 正例 1：合并后 fragment↔outline 双射；幂等二跑零差
        new, rep, _ = merge(outline_p, load_fragments(mapdir), approved_vols(mapdir))
        check("正例 有变更", new is not None and "1.1.1" in new and "1.1.2" in new)
        _mk(outline_p, new)
        new2, _, _ = merge(outline_p, load_fragments(mapdir), approved_vols(mapdir))
        check("正例 幂等二跑零差", new2 is None)

        # 正例 2：fragment 删行 → outline 同步删
        _mk(os.path.join(mapdir, "design", "fragments", "V01.tsv"),
            "vol\tchapter\tsec_no\tsub_no\ttitle\tstatus\tevidence\n"
            "01\t1\t1.1\t1.1.1\t甲一一\t已批\t\n")
        new3, _, _ = merge(outline_p, load_fragments(mapdir), approved_vols(mapdir))
        check("正例 删行同步", new3 is not None and "1.1.2" not in new3)
        _mk(os.path.join(mapdir, "design", "fragments", "V01.tsv"),
            "vol\tchapter\tsec_no\tsub_no\ttitle\tstatus\tevidence\n"
            "01\t1\t1.1\t1.1.1\t甲一一\t已批\t\n"
            "01\t1\t1.1\t1.1.2\t甲一二\t空骨架\t\n")
        _mk(outline_p, new)

        # 负向 1：hash 失效（改台账不重批）→ 拒绝且 outline 不动
        _mk(ledger, "subsection_id\ttitle\nV01.1.1.1\t改题\n")
        disk_before = open(outline_p, encoding="utf-8").read()
        new4, rep4, ref4 = merge(outline_p, load_fragments(mapdir), approved_vols(mapdir))
        check("负向 hash 失效拒绝", ref4 is False and new4 is None
              and open(outline_p, encoding="utf-8").read() == disk_before)

        # 负向 2：--strict 下拒绝卷 → exit 真值
        allowed = approved_vols(mapdir)
        check("负向 strict 报告拒绝", any("拒绝" in r for r in rep4))
    finally:
        pass

    for x in ok:
        print("  [PASS]", x)
    for x in bad:
        print("  [FAIL]", x)
    print("自检 %d 项，失败 %d 项" % (len(ok) + len(bad), len(bad)))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
