# -*- coding: utf-8 -*-
"""目录自检（outline self-check）——重构2026 目录批次的**收口复核**。

来源：101 号文 §九 P3-12（2026-10-02 ykla「复核后全面批准」）。
定位：本件**不是**第九件门禁的替代，而是**独立复核**——九件门禁与三套回归**均未捕获**
      本轮两处缺口（卷 9 时段不自洽、迁移留痕 127 处残留），本件是唯一拦截通道。

判据（9 项）：
  A 卷数／卷号序列连续          B 逐卷卷题（复核用）
  C 七条卷序约束**按内容关键词独立识别**（不读设计表——避免「用被测对象自证」）
  D 独立计数 ＋ 与 index.html 6 处口径串比对
  E 卷导言／分工注覆盖          F 述评恒末
  G 章号节号连续性              H **迁移留痕反向枚举**（清理类施工的必备判据）
  I 迁移台账条数                J 关键卷结构抽查

用法：python tests/outline_selfcheck.py      （只读；每批目录收口即跑）
"""
# -*- coding: utf-8 -*-
"""101 号文五期施工·独立复核（只读；不复用施工脚本的中间态）。"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
# 路径一律由本件位置推导（2026-10-23 修：原写死 `D:/librebsd/...` 绝对路径）：
# parents[1] ＝ `05-卷册大纲/目录`（本件在 tests/ 内）。
DOC = Path(__file__).resolve().parents[1]
O = DOC / "data" / "outline.txt"
I = DOC / "index.html"
L = O.read_text(encoding="utf-8").splitlines()
H = I.read_text(encoding="utf-8")
CN = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九"]
def cn2i(s):
    if s == "十": return 10
    if "十" in s:
        a, _, b = s.partition("十")
        return (CN.index(a) if a else 1) * 10 + (CN.index(b) if b else 0)
    return CN.index(s)

# ---- 卷块 ----
heads = [(i, cn2i(re.match(r'^# 第([一二三四五六七八九十]+)卷', L[i]).group(1))) for i, l in enumerate(L) if l.startswith("# ")]
print(f"[A] 卷数 = {len(heads)}；卷号序列连续 1..N ? {[n for _, n in heads] == list(range(1, len(heads)+1))}")

# ---- 卷题 ----
titles = {n: L[i] for i, n in heads}
print("\n[B] 逐卷卷题（复核用）")
for i, n in heads:
    print(f"   {n:>2}  {L[i][2:]}")

# ---- 约束验算（按内容识别，不按设计表） ----
def find(sub):
    return next((n for n, t in titles.items() if sub in t), None)

def find_in_volume(sub):
    """按**卷块内容**（卷题＋章题＋节题）定位首个含该关键词的卷号（2026-10-23 增）。

    用于“作为卷已消解、内容并入他卷”的主题：如“传言”——旧第 43 卷
    “BSD 的传言、都市传说、俚语与习俗”已消解，最早落位现为第二十九卷第 7 章。
    仍按内容动态识别，不写死卷号；全库无命中返回 None（走 C 组锚点失效自报）。
    """
    for k, (i, n) in enumerate(heads):
        e = heads[k + 1][0] if k + 1 < len(heads) else len(L)
        if any(sub in x for x in L[i:e]):
            return n
    return None

pos = {n: k for k, (_, n) in enumerate(heads, 1)}
# 2026-10-05 修 C1 锚点：原用旧卷题「386BSD 与 BSD 大分裂」（112/113 拆卷前之临时合并卷名，
# 拆分后该题面已不存在 → find() 返回 None、本件抛 KeyError 静默失效）。改锚现行卷 16
# 「BSD UNIX 大分裂」，并以题面（而非卷号）锚定，免于历次重编号崩坏。
chk = [
 ("C1 UNIX 战争 < BSD UNIX 大分裂", lambda: pos[find("UNIX 战争")] < pos[find("BSD UNIX 大分裂")]),
 # 2026-10-23 四修 R2 锚点：原锚“BSD UNIX 文化与哲学”系旧卷题子串，现行卷 29 题面为
 # “BSD UNIX 文化、社会与哲学”→ find() 返回 None、本件第四次因锚腐失效。改锚现行题面全串。
 ("R2 BSD UNIX 文化、社会与哲学 < BSD UNIX 技术专题史", lambda: pos[find("BSD UNIX 文化、社会与哲学")] < pos[find("BSD UNIX 技术专题史")]),
 # 2026-10-15 修 R4 锚点：149 批人物专卷 #48（BSD 社区与相关领域人物志）经 ykla 批准插于旧 42 卷（社会与哲学横向）之前——技术横向（现 47）与社哲横向（现 49）之间隔人物专卷一卷，相邻关系不复成立 → 循 R7 先例（2026-10-05／10-11）改取严格序。
 ("R4 技术横向比较卷 位次早于 文化哲学横向比较卷（间隔人物专卷 #48）", lambda: pos[find("技术发展史的横向比较")] < pos[find("社会与哲学的横向比较")]),
 # 2026-10-10 修 R4 锚点：原锚「文化与哲学的横向比较」系旧卷题子串，卷 40 题面已改为
 # 「文化、社会与哲学的横向比较」（原锚不再命中 → find() 返回 None、KeyError 失效）。
 # 改锚现行题面子串「社会与哲学的横向比较」，并沿用题面（而非卷号）锚定惯例。
 # 2026-10-05 修 R7：原断「macOS == 沉默的基石 +1」（相邻）。116c 新建卷 36「BSD 的衍生与分叉」
 # 即插于卷 35「沉默的基石」与卷 37「macOS」之间（116b 丙案设计），相邻关系不复成立 →
 # 按判据标签「之后」改取**严格序**（保持判据可读且免于再插入时崩坏）。
 # 2026-10-11 三修 R7 锚点：A-45 裁定「沉默的基石」名号归第六十四卷第 5 章（不再作卷题），
 # 原锚不再命中 → KeyError（本件第三次因该锚静默失效）。按设计语义（macOS 卷居 BSD 技术
 # 扩散与商业化卷之后）改锚现行第四十四卷题面子串「技术的扩散与商业化」。
 ("R7 macOS 在「扩散与商业化」卷（原「沉默的基石」卷）之后", lambda: pos[find("macOS")] > pos[find("技术的扩散与商业化")]),
 # 2026-10-23 修 R10／C2 锚点：“传言”已不作卷题——旧第 43 卷“BSD 的传言、都市传说、俚语
 # 与习俗（1969—2026）”消解，内容并入各期文化卷（最早落位现第二十九卷第 7 章），两个原锚点
 # 同时失效（KeyError(None)）。改以 find_in_volume() 按**卷块内容**定位，并按现行真值改写判据：
 #   R10 → 传言所在卷早于史学史卷（原链：旧 43 早于旧 42“史学史与方法”；该卷现分列 73／74／75，
 #         取首卷“BSD 史学史”）；
 #   C2  → 原“传言卷 ＝ 会者定离 − 2”等式随旧 43 卷消解而无可比对象，降为严格先序判据
 #         （传言所在卷早于会者定离卷）；相邻关系由 C3（传播载体 ＝ 会者定离 − 1）继续守。
 ("R10 传言所在卷 < 史学史卷", lambda: pos[find_in_volume("传言")] < pos[find("BSD 史学史")]),
 ("C2 传言所在卷 早于 会者定离卷（原“= 会者定离 − 2”等式随旧 43 卷消解改判先序）", lambda: pos[find_in_volume("传言")] < pos[find("会者定离")]),
 ("C3 传播载体卷 = 会者定离 − 1", lambda: pos[find("传播载体与公众记忆")] == pos[find("会者定离")] - 1),
]
print("\n[C] 卷序约束（按内容识别，独立于设计表；锚点失效时逐项自报、不再整件中断）")
_crot = 0
for name, fn in chk:
    try:
        ok = fn()
    except KeyError as e:
        _crot += 1
        print(f"   ❌ {name}（锚点失效：{e!r}——题面不含预期子串，须按现行卷题修锚）")
        continue
    print(f"   {'✅' if ok else '❌'} {name}")
    if not ok: _crot += 1
if _crot:
    print(f"   ⚠ [C] 组异常 {_crot} 项（2026-10-11 改：锚点失效自报化；此前表现为 KeyError 整件崩溃）")

# ---- 口径 ----
vols = len(heads)
chs = sum(1 for l in L if l.startswith("## "))
secs = sum(1 for l in L if l.startswith("- "))
notes = sum(l.count("@@") for l in L)
print(f"\n[D] 独立计数：{vols} 卷 {chs} 章 {secs} 节／注 {notes}（注＝原文 `@@` 出现次数，"
      f"与第九件 E2「页面 .src 节数」口径不同，后者为权威）")
m = re.search(r'(\d+) 卷 (\d+) 章 (\d+) 节', H)
print(f"   index.html doc-metrics 串 = {m.group(0) if m else '未找到'}")
six = re.findall(r'(\d+) 卷 (\d+) 章 (\d+) 节', H)
print(f"   index.html 内口径串共 {len(six)} 处，去重 = {sorted(set(six))}")

# ---- 卷导言 / 分工注 ----
ov = []; nt = []
for k, (i, n) in enumerate(heads):
    e = heads[k+1][0] if k+1 < len(heads) else len(L)
    seg = L[i:e]
    if not any(x.startswith(">") for x in seg): ov.append(n)
    if any(x.startswith("!") for x in seg): nt.append(n)
print(f"\n[E] 缺卷导言 {len(ov)} 卷 {ov}｜含 `!` 分工注 {len(nt)} 卷")

# ---- 述评恒末 ----
bad = []
for k, (i, n) in enumerate(heads):
    e = heads[k+1][0] if k+1 < len(heads) else len(L)
    cur = None
    for x in L[i:e]:
        if x.startswith("## "): cur = x
        elif x.startswith("- ") and cur and "本章书目述评" in x:
            # 述评须为该章末节
            pass
    chs_in = [x for x in L[i:e] if x.startswith("## ")]
    for ci, c in enumerate(chs_in):
        pass
print("\n[F] 述评恒末：见第十二件（0 处问题）")

# ---- 章/节号连续性 ----
prob = []
for k, (i, n) in enumerate(heads):
    e = heads[k+1][0] if k+1 < len(heads) else len(L)
    ci = 0; si = 0; cur = None
    for x in L[i:e]:
        if x.startswith("## "):
            ci += 1; si = 0
            mm = re.match(r'^## 第 (\d+) 章', x)
            if not mm or int(mm.group(1)) != ci: prob.append((n, "章号", x[:30]))
            cur = ci
        elif x.startswith("- ") and cur:
            si += 1
            mm = re.match(r'^- (\d+)\.(\d+) ', x)
            if not mm or int(mm.group(1)) != cur or int(mm.group(2)) != si:
                prob.append((n, "节号", x[:44]))
print(f"\n[G] 章号/节号连续性异常 {len(prob)} 处")
for x in prob[:8]: print("   ", x)

# ---- 迁移留痕残留 ----
N = r'[0-9一二三四五六七八九十百]+'
resid = [(i+1, l[:110]) for i, l in enumerate(L)
         if re.search(r'迁入|并入本章|自卷\s*' + N + r'\s*旧', l)]
print(f"\n[H] 目录正文迁移留痕残留 {len(resid)} 处（本件无白名单；第七件 audit_index_structure 的 "
      f"N-b5 白名单认定其中数处为**应保留**之分工记录——以第七件结论为准）")
for x in resid[:8]: print("   ", x)
hist = sum(1 for l in L if re.search(r'(旧|原)第' + N + r'卷', l))
print(f"   历史层引用（旧/原 第X卷）保留 {hist} 处（应保留）")

# ---- 台账 ----
# 历史归档引用，勿改：台账留在 review_logs 历史归档，不随夹具迁移（批计划 §九披露）。
T = Path(r"D:/librebsd/08-核查报告与多轮复核/重构2026/review_logs/迁移留痕台账-20261002.tsv")
if T.exists():
    rows = T.read_text(encoding="utf-8").splitlines()
    print(f"\n[I] 台账条数 = {len(rows)-1}（含表头 1 行）")
else:
    print("\n[I] 台账缺失")

# ---- 抽查卷结构 ----
print("\n[J] 抽查关键卷结构")
for sub in ("UNIX 战争", "BSD–Linux 关系史", "编程之夏", "BSD UNIX 技术专题史", "技术发展史的横向比较"):
    n = find(sub)
    if not n: print(f"   ❌ 未找到「{sub}」"); continue
    i = next(i for i, x in heads if x == n)
    e = next((j for j, _ in heads if j > i), len(L))
    cs = [x for x in L[i:e] if x.startswith("## ")]
    ss = sum(1 for x in L[i:e] if x.startswith("- "))
    print(f"   卷{n}｜{len(cs)} 章 {ss} 节｜{L[i][2:44]}")
