# -*- coding: utf-8 -*-
"""目录页注文引用四判据门禁（P0 护栏，2026-09-29 立；2026-09-30 增 P4）

依据：`92-目录内容调整建议书` §四 P0-1 护栏＝85 号文 §一·3 三判据脚本化；87 号文 R-3；
      98 号文 §11.4 P0-3（新增 P4「ref 著录完备性」）。
对象：内容层 `重构2026/data/outline.txt`（卷／章／节题与 `@@` 注的唯一编辑入口）；
      P4 另读页面数据层 `重构2026/data/catalog.json` 的 `refs`。

四判据
------
- **P1 引号节名存在性**（判 FAIL）：注内 `N.M"节名"` 引号节名须与现存节题匹配
  （此判据抓 `L2245「双柱」节` 一类：节号存在但引号题名张冠李戴）。
- **P2 章号与节号存在性**（判 FAIL）：注内「第X卷 第 Y 章 · Z.W」指位须真实存在。
  **不做历史豁免**——凡现行**活指位**（分工／另见／正身／见第／归第）一律核；
  但**显式标注「旧／原／迁入／并入／拆分」等溯源声明**者（非现行指位）剔除，免误报。
- **P3 自指卷号**（仅复核清单，不判 FAIL）：指向「本卷第 Y 章」者列出供人工复核。
- **P4 ref 编号著录完备性**（判 FAIL，2026-09-30 立）：注内 `ref N` 指向的编号须在
- **P5 主体—谓词误配**（仅复核清单，不判 FAIL，2026-10-06 立，119d ★9）：注文内出现「基金会＋版本/发行谓词」「项目＋法人谓词」「操作系统＋授权结构谓词」三类高频误配模式者列出供人工复核（判据真值＝写作规则「历史主体四分与称谓纪律」与 04-史学方法论 09 件之「主体×对象不可承载」表）。
  `catalog.json` 的 `refs` 中有**非空著录**（页面 ref 浮层的唯一取数源）；悬空即 FAIL。
  设立缘由：2026-09-30 产物实读发现 **25 处**引用 7 个未著录编号（`ref 10001`–`ref 10008`），
  而当时的 JS 自校验第 ④ 项为**死判据**（扫描对象恒为空集）、权威库又存在「已登记、`bibliography_entry` 为空」
  的中间态——该缺陷**完全靠人工实读才发现**。`SRC-mat:N` 系内部史料编号，不在判据面内。

判据口径（本文冻结）
------------------
- 只核「卷→章→节」存在性，不核题面语义相似度（不做相似度猜挂）。
- 节号只在该节有明确「卷+章」宿主上下文时判定；孤立「Z.W」不作判断（防把年份／句点当节号）。
- P4 只核「有无非空著录」，不核著录**质量**（质量由 04-现代研究文献 的复核流程负责）。

用法
----
    python audit_note_xref.py            # 跑四判据，P1/P2/P4 有 FAIL 则 exit 1
    python audit_note_xref.py --list     # 只打印 P3 自指复核清单（恒 exit 0）
    python audit_note_xref.py --selftest # 判据非空自检（注入缺陷须命中，含 P4）
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUTLINE = ROOT / "08-核查报告与多轮复核" / "重构2026" / "data" / "outline.txt"
CATALOG = ROOT / "08-核查报告与多轮复核" / "重构2026" / "data" / "catalog.json"
REF_RE = re.compile(r"\bref\s?(\d{1,5})")

CN = {"〇": 0, "一": 1, "二": 2, "三": 3, "四": 4, "五": 5,
      "六": 6, "七": 7, "八": 8, "九": 9, "十": 10}


def cn2int(s):
    """汉字数字 → 整数（〇..九／十／百 的组合写法，位值解析）。

    2026-10-04 修：原实现为「逐字累加」（注释称「项目卷数 ≤43，逐字累加足够」），
    对 ≥20 的卷**系统性错解**——「第三十九卷」得 3+10+9＝22、「第二十卷」得 2+10＝12。
    汉字引用因「索引侧与引用侧同错」而侥幸不报；**阿拉伯卷号引用（如「卷 39」）即暴露为
    假 FAIL**（110 号文施工实测）。改为位值解析；`--selftest` 以 T3 断言四类写法。
    """
    s = s.strip()
    if not s:
        return None
    if s.isdigit():
        return int(s)
    if "百" in s:
        a, _, b = s.partition("百")
        if a and a not in CN:
            return None
        av = (CN[a] if a else 1) * 100
        if not b:
            return av
        rest = cn2int(b)
        return None if rest is None else av + rest
    if "十" in s:
        a, _, b = s.partition("十")
        if (a and a not in CN) or (b and b not in CN):
            return None
        return (CN[a] if a else 1) * 10 + (CN[b] if b else 0)
    if len(s) == 1 and s in CN:
        return CN[s]
    return None


def selftest_cn2int():
    """T3（2026-10-04 补）：位值解析对组合写法的四类断言。"""
    cases = {"九": 9, "十": 10, "十二": 12, "十四": 14, "十九": 19,
             "二十": 20, "二十一": 21, "三十": 30, "三十九": 39,
             "四十九": 49, "一百": 100, "〇": 0}
    bad = [(k, v, cn2int(k)) for k, v in cases.items() if cn2int(k) != v]
    print("T3 cn2int 位值解析:", "PASS" if not bad else "FAIL %s" % bad)
    return 0 if not bad else 1


CN_VOL = re.compile(r"第([〇一二三四五六七八九十百]+)卷")
AR_VOL = re.compile(r"卷\s*(\d+)")
CH_REF = re.compile(r"第\s*(\d+)\s*章")
SEC = re.compile(r"(?<!\d)(\d+)\.(\d+)(?!\d)")
QNAME = re.compile(r"(\d+)\.(\d+)[“\"]([^”\"]{1,50})[”\"]")

# 回溯/溯源声明（这些位非现行活指位，剔除）
PROVEN = re.compile(r"(自第?[〇一二三四五六七八九十百\d]+卷\s*旧\d+|自\s*\d+\s*旧|原第[〇一二三四五六七八九十百]+卷|"
                    r"\b原\b|旧第\d+章|旧\s*第?\d+[\.\d]*\s*章?|迁入|并入|拆分|移入|迁自|"
                    r"沿用冻结|体例调整|注销|失据|按先例|源自卷)")
# 活指位动词
LIVE = re.compile(r"分工|另见|正身|见|归|指")


class Outline:
    def __init__(self, lines):
        self.vol_by_ln = {}
        self.chapters = {}      # vol -> set(ch)
        self.sections = {}      # (vol, ch) -> set((n, m))
        self.title = {}         # (vol, ch, (n, m)) -> title(text only)
        vol = ch = None
        for i, l in enumerate(lines, 1):
            if l.startswith("# "):
                m = re.match(r"第([〇一二三四五六七八九十百]+)卷", l[2:])
                vol = cn2int(m.group(1)) if m else None
                ch = None
                if vol:
                    self.chapters.setdefault(vol, set())
            elif l.startswith("## "):
                m = re.match(r"第\s*(\d+)\s*章", l[3:])
                ch = int(m.group(1)) if m else None
                if vol and ch:
                    self.chapters[vol].add(ch)
            elif l.startswith("- "):
                m = re.match(r"- (\d+)\.(\d+)\s+", l)
                if m and vol and ch:
                    k = (int(m.group(1)), int(m.group(2)))
                    self.sections.setdefault((vol, ch), set()).add(k)
                    self.title[(vol, ch, k)] = l[2:].split("@@")[0].strip()
            self.vol_by_ln[i] = vol

    def has_ch(self, vol, ch):
        return vol in self.chapters and ch in self.chapters[vol]

    def has_sec(self, vol, ch, n, m):
        return (vol, ch) in self.sections and (n, m) in self.sections[(vol, ch)]

    def sec_title(self, vol, ch, n, m):
        return self.title.get((vol, ch, (n, m)))


def norm(s):
    s = re.sub(r"^\d+\.\d+\s*", "", s or "")
    return re.sub(r"\s+", "", s)


def live_clause(text, start):
    """文本 text 中自 start 起是否属活指位（≤20 字符内出现指位动词）。"""
    return bool(LIVE.search(text[start:start + 24]))


def iter_volrefs(note):
    """返回 [(vol, pos)]，pos 为卷 token 起始偏移。"""
    out = []
    for m in CN_VOL.finditer(note):
        out.append((cn2int(m.group(1)), m.start()))
    for m in AR_VOL.finditer(note):
        out.append((int(m.group(1)), m.start()))
    return out


# ── P5（2026-10-06 立，119d ★9）：主体—谓词误配（列复核清单，不判 FAIL，同 P3 例）──
#   真值＝写作规则.md「历史主体四分与称谓纪律」＋04-史学方法论 09 件「主体×对象不可承载」表。
#   仅取三类高频、低歧义模式；命中即列清单，最终判定仍须人工实读一手史料（不以机检替代实读）。
SUBJ_MISMATCH = [
    (re.compile(r"基金会[^。；〔〕]{0,14}(发布|释出|发行)"), "基金会（法人）＋版本／发行谓词：制品面应归项目或发布工程团队"),
    (re.compile(r"项目[^。；〔〕]{0,10}(注册|年报|财务报表|商标权|法人登记)"), "项目（共同体）＋法人谓词：法人面应归基金会"),
    (re.compile(r"操作系统[^。；〔〕]{0,10}(选举|改选|任命)"), "操作系统（制品）＋授权结构谓词：职位面应归团队与职位"),
]


def scan_subject_agency(lines):
    """P5：注文内主体—谓词误配复核清单（不判 FAIL）。"""
    out = []
    for i, l in enumerate(lines, 1):
        if "@@" not in l and "分工" not in l and "另见" not in l:
            continue
        for rx, why in SUBJ_MISMATCH:
            if rx.search(l):
                out.append((i, why, l.strip()[:140]))
    return out


def scan_refs(lines, refs, o=None):
    """P4：注文引用的 ref 编号须在页面数据层 catalog.json 的 refs 中有非空著录。

    返回 {编号: [(行号, 卷标签), …]}；`refs` 可注入（供 --selftest 用）。
    `SRC-mat:N` 系内部史料编号（著录说明在浮层内），不在本判据面内。
    """
    bad = {}
    for i, l in enumerate(lines, 1):
        for m in REF_RE.finditer(l):
            rid = m.group(1)
            if not (refs.get(rid) or "").strip():
                vol = o.vol_by_ln.get(i) if o else None
                bad.setdefault(rid, []).append((i, ("卷%d" % vol) if vol else "?"))
    return bad


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    if args.selftest:
        src = ("# 第一卷  A\n"
               "## 第 1 章  c\n"
               "- 1.1 x@@〔第三十三卷第 12 章分工〕\n"
               "## 第 5 章  z\n"
               "- 5.9 标题甲@@〔第一卷第 5 章 5.9“双柱”节分工〕")
        lines = src.split("\n")
        o = Outline(lines)
        p1, p2, _ = run(o, lines)
        hit = any("第三十三卷" in e[-1] for e in p2) and any("双柱" in e[-1] for e in p1)
        # P4 负向自检：注入一个未著录编号 + 一个已著录编号，须只命中前者
        p4 = scan_refs(["a@@〔溯源：ref 99999（未著录）〕", "b@@〔溯源：ref 12（已著录）〕"],
                       {"12": "X. 有著录[M]. 2020."})
        hit4 = ("99999" in p4) and ("12" not in p4)
        print("selftest:", "PASS" if (hit and hit4) else "FAIL",
              f"(P1 {len(p1)}, P2 {len(p2)}, P4 {sorted(p4)})")
        rc_cn = selftest_cn2int()
        return 0 if (hit and hit4 and rc_cn == 0) else 1

    lines = OUTLINE.read_text(encoding="utf-8").split("\n")
    o = Outline(lines)
    refs = json.loads(CATALOG.read_text(encoding="utf-8")).get("refs", {})
    p1, p2, p3 = run(o, lines)
    p4 = scan_refs(lines, refs, o)
    p5 = scan_subject_agency(lines)
    n_ref = sum(1 for l in lines for _ in REF_RE.finditer(l))
    n_ref_id = len({m.group(1) for l in lines for m in REF_RE.finditer(l)})
    if args.list:
        print("P3 自指卷号复核清单（人工复核，不判 FAIL）：")
        for i, l in p3:
            print(f"  L{i}: {l}")
        print("P5 主体—谓词误配复核清单（人工复核，不判 FAIL）：")
        for i, why, txt in p5:
            print(f"  L{i}: {why}")
            print(f"      {txt}")
        return 0
    for tag, lst in (("P1", p1), ("P2", p2)):
        for i, why, txt in lst:
            print(f"[{tag}] L{i} {why}\n    {txt[:130]}")
    for rid, locs in sorted(p4.items(), key=lambda x: int(x[0])):
        print(f"[P4] ref {rid} 未著录（catalog.json#refs 无非空著录）；出现 {len(locs)} 处："
              + "、".join(f"L{i}（{v}）" for i, v in locs[:4])
              + ("…" if len(locs) > 4 else ""))
    if p1 or p2 or p4:
        print(f"FAIL：P1 {len(p1)} 条，P2 {len(p2)} 条，"
              f"P4 ref 未著录 {len(p4)} 个编号／{sum(len(v) for v in p4.values())} 处")
        return 1
    if p5:
        print(f"[P5] 主体—谓词误配复核清单（{len(p5)} 条，不判 FAIL，--list 查看）：")
        for i, why, txt in p5[:8]:
            print(f"  L{i}: {why}")
            print(f"      {txt}")
    print(f"PASS：P1/P2 无失效；P4 ref 著录完备（{n_ref} 处引用／{n_ref_id} 个编号）；"
          f"P3 自指复核 {len(p3)} 条、P5 主体误配 {len(p5)} 条（--list 查看）")
    return 0


def run(o, lines):
    p1, p2, p3 = [], [], []

    # 卷引用子句边界：一个卷 token ⇒ 到下一个「第X卷/卷 N」token（或句子尾）
    def clauses(seg):
        vr = [(v, p) for v, p in iter_volrefs(seg) if v is not None]
        out = []
        for k, (v, p) in enumerate(vr):
            endp = vr[k + 1][1] if k + 1 < len(vr) else len(seg)
            out.append((v, p, seg[p:endp]))
        return out

    for i, l in enumerate(lines, 1):
        if "@@" not in l and "分工" not in l and "另见" not in l and "归第" not in l:
            continue
        own = o.vol_by_ln.get(i)
        for seg in re.split(r"[；;。]\s*", l):
            if PROVEN.search(seg):
                continue
            for vol, pos, tail in clauses(seg):
                cm = CH_REF.search(tail[:28])
                if not cm or not live_from(tail, cm):
                    continue
                ch = int(cm.group(1))
                if not o.has_ch(vol, ch):
                    p2.append((i, f"章号不存在：第{vol}卷 第{ch}章", seg))
                    continue
                secm = SEC.search(tail[cm.end():][:20])
                if secm:
                    n, m = int(secm.group(1)), int(secm.group(2))
                    if not o.has_sec(vol, ch, n, m):
                        p2.append((i, f"节号不存在：第{vol}卷第{ch}章 {n}.{m}", seg))
            for m in QNAME.finditer(seg):
                n, mm, quoted = int(m.group(1)), int(m.group(2)), m.group(3)
                vol = ch = None
                bound = [cl for cl in clauses(seg) if cl[1] < m.start()]
                for v, _, tail in bound[-1:]:
                    cm = CH_REF.search(tail[:28])
                    if cm and live_from(tail, cm) and o.has_ch(v, int(cm.group(1))):
                        vol, ch = v, int(cm.group(1))
                if vol and ch and o.has_sec(vol, ch, n, mm):
                    t = norm(o.sec_title(vol, ch, n, mm))
                    q = norm(quoted)
                    if t and q and q not in t and t not in q:
                        p1.append((i, f"引号节名不符：第{vol}卷第{ch}章 {n}.{mm} 引「{quoted}」实为「{t[:20]}」", seg))
        if own is not None:
            for vol, pos in iter_volrefs(l):
                tail = l[pos:]
                if vol == own and CH_REF.search(tail[:20]):
                    p3.append((i, l.strip()))
                    break
    return p1, p2, p3


def live_from(tail, cm):
    """tail＝从卷 token 起的子串；卷→章 之后 ≤16 字符内出现指位动词视为活指位。"""
    return bool(LIVE.search(tail[cm.end():cm.end() + 16]))


if __name__ == "__main__":
    sys.exit(main())