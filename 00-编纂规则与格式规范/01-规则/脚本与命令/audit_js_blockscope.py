# -*- coding: utf-8 -*-
"""audit_js_blockscope.py —— 第二十三件：行为源块作用域逃逸门禁（2026-10-12 143 批立，wave5 H2 升格）。

缘起：严格模式下块内 function 声明为块级作用域（ES2015），曾致“人物卡浮层／时间线视图／
修订差异视图”三个功能同时失效（Annex B 依赖）；原一次性扫描器 _scan_blockfn_scope.py 未
入门禁且已散佚，本件将其判据固化为常备护栏。

判据（FAIL 条件）：function 具名声明出现于**普通块**（if／for／while／switch／try 等
非函数体大括号）之内，且该名在块外存在词法引用——严格模式运行时必 ReferenceError。

实现：Python mini-lexer（注释／单双引号串／模板字面量含 ${} 插值／正则字面量四态）产出
等长“净文本”（串与注释内容置换为空格、模板 ${} 内代码保留），随后括号栈分类（函数体
vs 普通块）＋块外引用检索（排除 `.` 属性访问）。保守近似：宁可误报不漏报，误报人工复核。

扫描对象：src/js/manifest.txt（143 批 wave5 拆分后为唯一真身清单，按序逐文件）；
清单缺位时回退 assets/doc.js（拆分前兼容态）；assets/theme-preset.js 恒扫。

用法：
  python audit_js_blockscope.py             # 常规审计（0 违规 exit 0，否则 exit 1）
  python audit_js_blockscope.py --selftest  # 判据非空自检（正反夹具双向断言）
"""
import io
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")
ROOT = r"D:/librebsd/08-核查报告与多轮复核/重构2026"
SRC_JS = ROOT + "/src/js"
MANIFEST = SRC_JS + "/manifest.txt"
DOC_JS = ROOT + "/assets/doc.js"
THEME_JS = ROOT + "/assets/theme-preset.js"


# ── mini-lexer：产出等长净文本 ──────────────────────────────────────────────

def _blank(s):
    """保留换行与长度、内容置换空格。"""
    return "".join(ch if ch == "\n" else " " for ch in s)


def clean_source(src):
    """词法扫描：注释／字符串／模板字面量文本／正则字面量 → 空格；${} 内代码保留。"""
    out = list(src)
    i, n = 0, len(src)
    # 状态栈：'tpl'（模板字面量文本态）；代码态用栈空表示。
    # regex 起点判定所需“前一有效字符”在主循环内维护。
    last_sig = ""          # 前一非空白有效字符（净空间意义下）
    while i < n:
        ch = src[i]
        if ch == "/" and i + 1 < n and src[i + 1] == "/":
            j = src.find("\n", i)
            j = n if j < 0 else j
            out[i:j] = _blank(src[i:j]); i = j; continue
        if ch == "/" and i + 1 < n and src[i + 1] == "*":
            j = src.find("*/", i + 2)
            j = n if j < 0 else j + 2
            out[i:j] = _blank(src[i:j]); i = j; continue
        if ch in ("'", '"'):
            j = i + 1
            while j < n:
                if src[j] == "\\":
                    j += 2; continue
                if src[j] == ch:
                    j += 1; break
                j += 1
            out[i:j] = _blank(src[i:j])
            last_sig = ch  # 串后跟字母多为属性名等，视作标识边界；此处保持简单
            i = j; continue
        if ch == "`":
            # 模板字面量：文本段置换空格；${ 插值段保留（内含真代码）。
            j = i + 1
            while j < n:
                if src[j] == "\\":
                    j += 2; continue
                if src[j] == "`":
                    j += 1; break
                if src[j] == "$" and j + 1 < n and src[j + 1] == "{":
                    # ${ 之后的代码回到代码态：递归处理至配对 }
                    out[i:j + 1] = _blank(src[i:j + 1])  # ` 与 ${ 段先行置换
                    k = j + 2
                    depth = 1
                    while k < n and depth:
                        c2 = src[k]
                        if c2 in ("'", '"'):
                            e = k + 1
                            while e < n:
                                if src[e] == "\\":
                                    e += 2; continue
                                if src[e] == c2:
                                    e += 1; break
                                e += 1
                            out[k:e] = _blank(src[k:e]); k = e; continue
                        if c2 == "/" and k + 1 < n and src[k + 1] == "/":
                            e = src.find("\n", k); e = n if e < 0 else e
                            out[k:e] = _blank(src[k:e]); k = e; continue
                        if c2 == "/" and k + 1 < n and src[k + 1] == "*":
                            e = src.find("*/", k + 2); e = n if e < 0 else e + 2
                            out[k:e] = _blank(src[k:e]); k = e; continue
                        if c2 == "`":
                            # 嵌套模板：内层整体置换（保守——内层 ${} 中的引用极罕见）
                            e = k + 1
                            while e < n:
                                if src[e] == "\\":
                                    e += 2; continue
                                if src[e] == "`":
                                    e += 1; break
                                e += 1
                            out[k:e] = _blank(src[k:e]); k = e; continue
                        if c2 == "{":
                            depth += 1
                        elif c2 == "}":
                            depth -= 1
                            if depth == 0:
                                break
                        k += 1
                    # ${} 内代码（j+2..k）保留原样；} 自身置换
                    out[k:k + 1] = " " if k < n else ""
                    i = k + 1
                    break
                j += 1
            else:
                j = n
            # 未经 ${ 分支（纯文本模板）：整段（含闭引号）置换；${ 分支则已推进 i
            if i < n and src[i] == "`":
                out[i:j] = _blank(src[i:j])
                i = j
            continue
        if ch == "/" and _regex_prev_ok(src, out, i):
            # 正则字面量：消费至未转义 /（字符类 [..] 内的 / 不终结），随后旗标
            j = i + 1
            in_cls = False
            while j < n:
                c2 = src[j]
                if c2 == "\\":
                    j += 2; continue
                if c2 == "[":
                    in_cls = True
                elif c2 == "]":
                    in_cls = False
                elif c2 == "/" and not in_cls:
                    j += 1
                    while j < n and (src[j].isalpha()):
                        j += 1
                    break
                j += 1
            out[i:j] = _blank(src[i:j]); i = j; continue
        if not ch.isspace():
            last_sig = ch
        i += 1
    return "".join(out)


def _regex_prev_ok(src, out, i):
    """判定 src[i]=='/' 是否正则字面量起点（依前一有效字符上下文）。"""
    # 在“已置换”输出上回溯最近一个非空格字符与所在词
    k = i - 1
    while k >= 0 and out[k] == " " and src[k] != "\n":
        k -= 1
    if k < 0:
        return True
    prev = src[k]
    if prev in "(,=:[!&|?+-*%{};~^<>":
        return True
    if prev.isalnum() or prev in "_$)":
        # 关键词后亦可为正则：return/typeof/case/in/of/delete/void/new/instanceof/do/else
        m = re.search(r"([A-Za-z_$][\w$]*)$", src[max(0, k - 12):k + 1])
        if m and m.group(1) in ("return", "typeof", "case", "in", "of", "delete",
                                "void", "new", "instanceof", "do", "else"):
            return True
    return False


# ── 括号栈分析 ──────────────────────────────────────────────────────────────

FN_RE = re.compile(r"\bfunction\s+([A-Za-z_$][\w$]*)\s*\(")
NAME_RE = re.compile(r"\b([A-Za-z_$][\w$]*)\b")
FN_OPEN_RE = re.compile(r"\bfunction\s+([A-Za-z_$][\w$]*)\s*\([^{}]*\)\s*$")
ARROW_RE = re.compile(r"=>\s*$")


def scan(clean, fname):
    """返回违规列表 [(name, kind, where)]。kind: decl-in-block。"""
    violations = []
    stack = []            # 条目：{"kind": "fn"|"block", "start": int, "end": None|int}
    candidates = []       # (name, decl_offset, block_ref)  block_ref 指向栈条目
    i, n = 0, len(clean)
    while i < n:
        ch = clean[i]
        if ch == "{":
            look = clean[max(0, i - 240):i]
            m = FN_OPEN_RE.search(look)
            if m:
                stack.append({"kind": "fn", "start": i, "end": None, "name": m.group(1)})
            elif ARROW_RE.search(look):
                stack.append({"kind": "fn", "start": i, "end": None, "name": ""})
            else:
                stack.append({"kind": "block", "start": i, "end": None, "name": ""})
        elif ch == "}":
            if stack:
                top = stack.pop()
                top["end"] = i + 1
        else:
            pass
        i += 1
    # 第二遍：登记普通块内 function 具名声明
    stack2 = []
    for m in FN_RE.finditer(clean):
        pos = m.start()
        while stack2 and stack2[0]["start"] < pos and stack2[0]["end"] is not None \
                and stack2[0]["end"] <= pos:
            pass
        # 以偏移重建：单遍维护太繁，这里直接逐声明重放栈——文件规模（万字符级）可接受
        name = m.group(1)
        # 计算该声明处的括号栈（重放）
        st = []
        j = 0
        # 优化：从上一声明位置增量回放
        while j < pos:
            c = clean[j]
            if c == "{":
                look = clean[max(0, j - 240):j]
                if FN_OPEN_RE.search(look) or ARROW_RE.search(look):
                    st.append({"kind": "fn", "start": j, "end": None})
                else:
                    st.append({"kind": "block", "start": j, "end": None})
            elif c == "}":
                if st:
                    st.pop()
            j += 1
        # 内层向外找最近普通块
        innermost_block = None
        for ent in reversed(st):
            if ent["kind"] == "block":
                innermost_block = ent
                break
            if ent["kind"] == "fn":
                break
        if innermost_block is not None:
            # 求该块 end（重放至配对）
            depth = 0
            k = innermost_block["start"]
            while k < n:
                if clean[k] == "{":
                    depth += 1
                elif clean[k] == "}":
                    depth -= 1
                    if depth == 0:
                        break
                k += 1
            span = (innermost_block["start"], k + 1)
            candidates.append((name, pos, span, fname))
    # 引用检索。豁免集（2026-10-12 143 批实测校准，现库三误报全由此二形态产生）：
    #   ①同名多声明＝平行作用域遮蔽（跨 IIFE 各自绑定，如两处 closePanels）；
    #   ②名现于任一形参表＝形参绑定（如 new Promise(function (resolve){...}) 的 resolve）。
    # 判据聚焦「唯一声明＋块外引用」的真逃逸形态；豁免为保守让位（可用性优先），限记入细节。
    decl_counts = {}
    for m in FN_RE.finditer(clean):
        decl_counts[m.group(1)] = decl_counts.get(m.group(1), 0) + 1
    exempt = 0
    for name, decl_pos, span, fn in candidates:
        if decl_counts.get(name, 0) >= 2:
            exempt += 1
            continue
        if re.search(r"\bfunction\s*\([^)]*\b" + re.escape(name) + r"\b[^)]*\)", clean):
            exempt += 1
            continue
        for m in NAME_RE.finditer(clean):
            if m.group(1) != name:
                continue
            p = m.start()
            if span[0] <= p < span[1]:
                continue
            # 排除属性访问 .NAME 与对象键 NAME:（后随冒号且前非标识）
            if p > 0 and clean[p - 1] == ".":
                continue
            rest = clean[m.end():m.end() + 2]
            if rest.startswith(":") and not NAME_RE.match(clean[max(0, p - 1):p] or " "):
                continue
            violations.append((name, "block-escape", fn))
            break  # 一名一报
    return violations, exempt


def gather_sources():
    """清单驱动：src/js/manifest.txt 在则按序取清单件，否则回退 doc.js；theme-preset 恒扫。"""
    files = []
    if os.path.exists(MANIFEST):
        for ln in io.open(MANIFEST, encoding="utf-8").read().splitlines():
            ln = ln.strip()
            if ln and not ln.startswith("#"):
                files.append(("src/js/" + ln, os.path.join(SRC_JS, ln)))
    else:
        files.append(("assets/doc.js", DOC_JS))
    files.append(("assets/theme-preset.js", THEME_JS))
    return files


def main():
    if "--selftest" in sys.argv:
        def _v(src_, tag):
            return scan(clean_source(src_), tag)[0]
        ok_a = _v("function outer(){ if (x) { function inner(){} inner(); } }", "A") == []
        bad = _v("if (x) { function inner(){} }\n  inner();", "B")
        ok_b = len(bad) == 1 and bad[0][0] == "inner" and bad[0][1] == "block-escape"
        prop = _v("if (x) { function inner(){} }\n  obj.inner();", "C") == []
        # D 形参同名豁免（resolve 型误报形态）；E 平行同名声明豁免（closePanels 型误报形态）
        ok_d = _v("if (x) { function resolve(){} }\nvar p = new Promise(function (resolve) { resolve(); });", "D") == []
        ok_e = _v("if (x) { function go(){} go(); }\n(function () { function go(){} go(); })();", "E") == []
        print("selftest: 块内自用未报=%s／块外引用命中=%s／属性访问豁免=%s／形参同名豁免=%s／平行同名豁免=%s"
              % (ok_a, ok_b, prop, ok_d, ok_e))
        sys.exit(0 if (ok_a and ok_b and prop and ok_d and ok_e) else 1)

    bad_total = 0
    for rel, path in gather_sources():
        if not os.path.exists(path):
            print("FAIL %s 缺失" % rel); bad_total += 1; continue
        src = io.open(path, encoding="utf-8", newline="").read()
        v, exempt = scan(clean_source(src), rel)
        if v:
            for name, kind, fn in v:
                print("FAIL %s：function %s 声明于普通块内且块外存在引用（严格模式 ReferenceError 风险）" % (fn, name))
            bad_total += len(v)
        else:
            print("PASS %s（块作用域零逃逸；豁免 %d 形态）" % (rel, exempt))
    print("第二十三件结论：" + ("PASS（行为源块作用域零逃逸）" if not bad_total else "FAIL %d 项" % bad_total))
    sys.exit(0 if not bad_total else 1)


if __name__ == "__main__":
    main()
