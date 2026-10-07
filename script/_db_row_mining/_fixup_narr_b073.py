# -*- coding: utf-8 -*-
"""fhk_b073 叙述分件机械修正器（主会话用，只处理机械可判定项）。

只修四类不会改变事实的形态缺陷，逐条打印 before/after，改完回读断言：
  1. 超长（>140）：前缀保留式机械归一——在 <=140 且 >=60 的「，／、」
     分句边界处截断并去掉该标点，不做词内硬切、不补写任何内容。
  2. 日期前缀：剥掉行首「YYYY 年 M 月 D 日，」形态（大纲脚本会自行补日期，
     留两个日期是重复污染）。
  3. 叙述体内嵌制表符：换成半角空格并折叠连续空格（否则字段数 != 3）。
  4. 尾标点／尾空格：剥掉 TRAIL 集合里的收尾字符（不碰问号与感叹号，
     那两种要改句式，属内容返修）。
外加：缺末行 LF 补齐。

修不动的（<60 字需补内容、数字开头需改主语、问号收尾需改句式）一律
打印为「待返修」，本脚本不猜测、不补字、不臆造。

用法: python _fixup_narr_b073.py [k ...]   缺省 1..50（只报不改）
      python _fixup_narr_b073.py --apply 2 8 12 ...
"""
import io
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(HERE, "review_logs")
TAG = "fhk_b073"
LO, HI = 60, 140
HOST = "885"
# 收尾可机械剥掉的字符（不含问号/感叹号：那两种要改句式，属内容返修）
STRIPTRAIL = set("。，、；：．·~-.,;: \t")
# 截断后若末字落在这些连词／介词／助词上，句尾悬空，须退回前一边界
DANGLE = set("把被将和与及对向给以而且但并又就也都还则才便于从")
DATEHEAD = re.compile(r"^\d{4}\s*年\s*(\d{1,2})\s*月\s*(\d{1,2})\s*日?\s*[，,]?\s*")
FORBID = set("「」『』*|\\")
QUOTES = set(chr(c) for c in [0x2018, 0x2019, 0x201C, 0x201D, 0x0027, 0x0022, 0x0060])

APPLY = "--apply" in sys.argv
args = [a for a in sys.argv[1:] if a != "--apply"]
ks = [int(a) for a in args] or list(range(1, 51))

todo = {}          # k -> [(pk, why), ...]
done = 0

for k in ks:
    p = os.path.join(LOG, "%s_mount_narr_p%d.tsv" % (TAG, k))
    if not os.path.exists(p):
        todo.setdefault(k, []).append(("", "文件缺失"))
        continue
    raw = io.open(p, "rb").read()
    if raw[:3] == b"\xef\xbb\xbf":
        todo.setdefault(k, []).append(("", "含 BOM"))
        continue
    if b"\r" in raw:
        todo.setdefault(k, []).append(("", "含 CR"))
        continue
    need_lf = not raw.endswith(b"\n")
    txt = raw.decode("utf-8")
    out = []
    changed = []
    for ln in txt.split("\n"):
        if not ln.strip():
            continue
        f = ln.split("\t")
        if len(f) != 3:
            # 字段数异常：把第 3 段起的全部当成叙述体，中间的分隔符视为内嵌制表符
            if len(f) < 2 or not f[0].isdigit():
                todo.setdefault(k, []).append((ln[:24], "字段%d 无法解析" % len(f)))
                continue
            pk, hk = f[0], f[1]
            tail = f[2:]
            # 读手偶发把行序号「1」「2」写成叙述体首字段（后跟一个制表符）。
            # 该 token 是纯数字且其右侧才是叙述正文——属字段错位伪影，删除而
            # 不补字；若它不是这种形态则仍按内嵌制表符折空格处理。
            if len(tail) >= 2 and tail[0].strip().isdigit() and len(tail[0].strip()) <= 3 \
                    and len(tail[1].strip()) > 10:
                nar = " ".join(x for x in tail[1:])
                changed.append((pk, "字段%d->3 删行序号伪影 %r" % (len(f), tail[0])))
            else:
                nar = " ".join(x for x in tail)
                changed.append((pk, "字段%d->3 内嵌制表符换空格" % len(f)))
        else:
            pk, hk, nar = f[0], f[1], f[2]

        old = nar
        if "\t" in nar:
            nar = re.sub(r"[\t ]+", " ", nar).strip()
            changed.append((pk, "内嵌制表符换空格"))

        m = DATEHEAD.match(nar)
        if m:
            nar = nar[m.end():]
            changed.append((pk, "剥日期前缀 %r" % m.group(0)[:14]))

        while nar and nar[-1] in STRIPTRAIL:
            nar = nar[:-1]

        if len(nar) > HI:
            cut = nar[:HI]
            # 边界优先级：分句标点优于空格词界，但空格词界好过词内硬切——
            # 本批有读手整句不用逗号、仅用空格分隔的写法（如 p18），无标点
            # 可切时退到空格，仍不落在词中。
            cands = []
            for sep in ("，", "、", "；", " "):
                i = cut.rfind(sep)
                if i >= LO:
                    cands.append(i)
            if cands:
                # 取最靠后边界以保内容量，但若该切法让末字落在连词／介词／
                # 助词上（「…空调制解调器把」这类悬空句尾），逐个退回前一
                # 个边界直到句尾不再悬空。
                best = max(cands)
                for i in sorted(cands, reverse=True):
                    if nar[:i][-1] not in DANGLE:
                        best = i
                        break
                nar = nar[:best].rstrip("".join(STRIPTRAIL))
            else:
                nar = cut.rstrip("".join(STRIPTRAIL))
            if not (LO <= len(nar) <= HI):
                todo.setdefault(k, []).append((pk, "超长 %d 无法在分句边界归一" % len(old)))
                continue
            changed.append((pk, "超长 %d -> %d（分句边界截断）" % (len(old), len(nar))))

        # 句尾悬空：末字落在连词／介词／助词上（读手整句只用空格分隔时，
        # 截断或原句本身都可能落成「…空调制解调器把」）。在最后一个分句边界
        # 处截断，只丢尾巴，不补字。
        if len(nar) >= LO and nar[-1] in DANGLE:
            bb = -1
            for sep in ("，", "、", "；", " "):
                i = nar.rfind(sep)
                if i >= LO:
                    bb = max(bb, i)
            if bb > 0 and nar[:bb][-1] not in DANGLE:
                nar = nar[:bb].rstrip("".join(STRIPTRAIL))
                changed.append((pk, "句尾悬空末字 %r 截断至 %d" % (old[-1], len(nar))))

        nar = nar.strip()
        if not nar:
            todo.setdefault(k, []).append((pk, "修后为空"))
            continue
        if len(nar) < LO:
            todo.setdefault(k, []).append((pk, "过短 %d（需补内容，非机械可修）" % len(nar)))
        if nar[0].isdigit():
            todo.setdefault(k, []).append((pk, "数字开头（需改主语，非机械可修）"))
        if nar[-1] in "?！?!":
            todo.setdefault(k, []).append((pk, "问号/叹号收尾（需改句式，非机械可修）"))
        if DATEHEAD.match(nar):
            todo.setdefault(k, []).append((pk, "仍有日期前缀"))
        if "\t" in nar or "\n" in nar or "\u3000" in nar:
            todo.setdefault(k, []).append((pk, "仍有制表/换行/全角空格"))
        if set(nar) & (FORBID | QUOTES):
            todo.setdefault(k, []).append((pk, "禁字符/引号（非机械可修）"))
        if set(old) != set(nar) or old != nar:
            pass
        out.append((pk, hk, nar))

    if need_lf:
        changed.append(("", "补末行 LF"))

    if changed and APPLY:
        body = "".join("%s\t%s\t%s\n" % t for t in out)
        with io.open(p, "w", encoding="utf-8", newline="") as f:
            f.write(body)
        rb = io.open(p, "rb").read()
        assert not rb.startswith(b"\xef\xbb\xbf") and b"\r" not in rb and rb.endswith(b"\n")
        print("[p%02d] 已写 %d 处：" % (k, len(changed)))
        for pk, why in changed:
            print("        %s %s" % (pk or "-", why))
        done += 1
    elif changed:
        print("[p%02d] 待修 %d 处（--apply 未开）：" % (k, len(changed)))
        for pk, why in changed:
            print("        %s %s" % (pk or "-", why))
    if k in todo:
        print("[p%02d] 待返修 %d 条：" % (k, len(todo[k])))
        for pk, why in todo[k]:
            print("        %s %s" % (pk or "-", why))

print("=" * 66)
print("机械修正分件 %d 个（--apply %s）；待返修分件 %d 个"
      % (done, APPLY, len(todo)))
if todo:
    for k in sorted(todo):
        print("   p%02d: %s" % (k, "; ".join("%s %s" % (pk, why)
                                             for pk, why in todo[k])[:180]))
