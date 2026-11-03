# -*- coding: utf-8 -*-
"""audit_title_term_forms.py —— 第四十一件：题名术语形态门禁（2026-11-03 立；2026-11-04 3A6-2 P4 前置批三项扩容）。
    判据：《小节建制与题名规则》§4.4 形态附表，扫描 title-design/*.tsv 题名（col5）＋论题（col6）两列：
      R29（G-03）专名官方形白名单：斜杠官方名之全角变体（/ → ／）出现即机拦；白名单扩至
        §4.4 附表一全表＋§4.4 三官方形示例（共 49 项，其中斜杠项 17 项产变体——与 2026-11-03
        基线变体面完全一致；无斜杠项不产变体，作 R35／R36 剔除词）；白名单外拉丁专名仍只披露
        不机拦（R10 口径不变）。
      R35（G-10）人物名双层：教科书级人物之拉丁姓氏机拦（§4.4 二应作既定中译；Bell 因机构语境
        例外不拦）；疑似自译形与“拉丁串＋冒号”待判形披露不拦。
      R36（G-11）版次称名分流：Research Unix 版次之阿拉伯序数、-RELEASE 拼写非全大写机拦；
        阿拉伯序数版次、-RELEASE 与裸版本号两态并存、拉丁序数版次形披露不拦。
    用法：
        python audit_title_term_forms.py            # 0 一致 / 1 不一致 / 2 依赖缺失
        python audit_title_term_forms.py --selftest # 判据非空＋新判据夹具必命中／合法夹具必不误报
    纪律：判据非空（OFFICIAL 为空即退出码 2）；拿不准形态只披露不拦；命中位于弯引号引文内者
        注记逐字保真红线适用；元语言题与逐字引文剔引号后判（R36 拉丁序数面）。
"""
import re
import sys
from pathlib import Path

ROOT = Path(r"D:/librebsd")
TD = ROOT / "05-卷册大纲/映射/title-design"

# —— R29：官方名白名单（半角为唯一合法形态）——
OFFICIAL = [
    # 附表一·斜杠官方名 15 项（全角变体机拦面）
    "CP/M", "Net/1", "Net/2", "System/360", "VAX-11/750", "TCP/IP",
    "BSD/386", "BSD/OS", "GNU/Linux", "Power 6/32", "MI/MD", "AIEE/IRE",
    "Darwin/XNU", "BSD/Mach", "V6/PWB",
    # 表外斜杠保留 2 项（2026-11-03 初版即有，非附表一来源，防回归保留）
    "GNU/kFreeBSD", "macOS/Darwin",
    # 附表一·无斜杠官方名 28 项（2026-11-04 G-03 扩容；无变体面，作 R35/R36 剔除词）
    "IBM", "DEC", "Apple", "Sun", "System V", "System III", "Pascal",
    "Bourne shell",
    "OSF", "USL", "SVR4", "Motif", "Open Look", "UnixWare", "SunOS",
    "Solaris", "AIX", "HP-UX", "IRIX", "Ultrix", "Xenix", "SCO UNIX",
    "COSE", "UFS", "ZFS", "HAMMER", "LWKT", "NUMA",
    # §4.4 三官方形示例 4 项（规则正文另列，注明纳入）
    "4.1BSD", "2BSD", "SunOS 4.0", "FreeBSD 1.0",
]

def build_variants():
    """斜杠官方名 → 全角变体（/ → ／）。判据非空纪律：OFFICIAL 为空即失败；
    无斜杠项不产变体（2026-11-04 起显式按“含斜杠”过滤——无斜杠项的自身映射会把该专名的
    合法出现误报为“「X」应为「X」”，属潜在误报面，显式排除）。"""
    assert OFFICIAL, "判据非空纪律：OFFICIAL 白名单不得为空"
    return {name: name.replace("/", "／") for name in OFFICIAL if "/" in name}

# —— R35：§4.4 二 人物名双层 ——
# 教科书级人物（既定中译）的拉丁姓氏：出现即机拦。贝尔（Bell）除外：实验室语境按机构名
# “贝尔实验室”，拉丁机构名合法，裸 Bell 指人指所拿不准，故不设拉丁机拦（人工判）。
TEXTBOOK_LATIN = {
    "Thompson": "汤普森", "Ritchie": "里奇", "Kernighan": "克尼汉",
    "McIlroy": "麦基尔罗伊", "Corbato": "科尔巴托", "Corbató": "科尔巴托",
    "Raymond": "雷蒙德", "McKusick": "麦库西克", "Torvalds": "托瓦兹",
    "Joy": "乔伊", "Cutler": "卡特勒", "Roberts": "罗伯茨",
}
# §4.4 二“无术语表译名者保留拉丁（禁自译）”名单人物的疑似中文自译形：译名归属以术语表
# 为准，脚本不载术语表，故一律披露不拦（狄龙为规则点名的演员译名冲突回避形，亦披露）。
NOLATIN_ZH = {
    "杜恩·亚当斯": "Duane Adams", "亚当斯": "Duane Adams",
    "卡尔·史密斯": "Carl Smith", "史密斯": "Carl Smith",
    "格威茨": "Gurwitz", "布拉德纳": "Bradner", "诺尔达": "Noorda",
    "乔利茨": "Jolitz", "卡雷尔斯": "Karels", "吉布斯": "Gibbs",
    "狄龙": "Matt Dillon",
}
RE_NAME = {name: re.compile(r"(?<![A-Za-z])" + re.escape(name) + r"(?![A-Za-z])")
           for name in TEXTBOOK_LATIN}

# “拉丁串＋冒号”披露面的剔除词（官方名词元＋常见技术词；小写比对）。
_COLON_EXTRA = [
    "freebsd", "openbsd", "netbsd", "dragonfly", "pcbsd", "midnightbsd",
    "xv6", "posix", "rfc", "iso", "ansi", "ieee", "acm", "usenix", "osi",
    "ietf", "fsf", "arpanet", "milnet", "csnet", "bitnet", "uucp", "usenet",
    "tcp", "udp", "ftp", "http", "nfs", "ntp", "dns", "smtp", "att",
    "intel", "amd", "microsoft", "csrg", "btl", "sitecom", "unisig", "arxiv",
    "nginx", "apache", "ddb", "gdb", "awk", "csh", "ksh", "tcsh", "bash",
    "sed", "make", "yacc", "lex", "troff", "nroff", "ditroff", "diff",
    "patch", "tar", "cpio", "dump", "restore", "fsck", "cvs", "rcs", "sccs",
    "inetd", "sendmail", "sunhme", "fixes", "student", "patches", "group",
    "errata", "release", "stable", "current", "releng", "ports", "packages",
    "man", "cam", "isa", "pci", "scsi", "eisa", "vga", "edition", "version",
    "first", "second", "third", "fourth", "fifth", "sixth", "seventh",
    "eighth", "ninth", "tenth",
]
COLON_EXCLUDE = set(_COLON_EXTRA)
for _n in OFFICIAL:
    for _t in re.split(r"[^A-Za-z]+", _n):
        if len(_t) >= 3:
            COLON_EXCLUDE.add(_t.lower())

# “拉丁串＋冒号”待判形：取完整拉丁串（≥3 字符）并要求首字母大写（人名为专名大写；
# 小写拉丁串接冒号多为网页标题转述或标识符，如 developer expenses for:／sunhme:／
# arXiv:1910.05798，不属人名形，不披露）。
RE_COLON = re.compile(r"([A-Za-z]{3,})\s*[：:]")

# —— R36：§4.4 三 版次称名分流 ——
RE_ARABIC_ED = re.compile(r"第\s*\d+\s*版")
RE_RU_CTX = re.compile(r"research\s+unix", re.I)
RE_REL_ANY = re.compile(r"\d+(?:\.\d+)*-[Rr][Ee][Ll][Ee][Aa][Ss][Ee]\b")
RE_REL_BARE = re.compile(r"FreeBSD\s+\d+(?:\.\d+)+(?!\s*-RELEASE)", re.I)
RE_LATIN_ORD = re.compile(
    r"(?:First|Second|Third|Fourth|Fifth|Sixth|Seventh|Eighth|Ninth|Tenth"
    r"|\d+(?:st|nd|rd|th))\s+(?:Edition|Version)\b", re.I)

# 弯引号引文（逐字保真档案面）：R35 命中注记、R36 拉丁序数与 RELEASE 面剔引后判。
RE_DQ = re.compile(r"“[^”]*”")
RE_SQ = re.compile(r"‘[^’]*’")

def quote_spans(text):
    return [m.span() for m in RE_DQ.finditer(text)] + [m.span() for m in RE_SQ.finditer(text)]

def strip_quotes(text):
    return RE_SQ.sub("", RE_DQ.sub("", text))

def in_quote(spans, pos):
    return any(s <= pos < e for s, e in spans)

def check_cell(text, variants):
    """单面（一格题名或一格论题）过三组判据。返回命中列表：
    kind＝block（机拦）／disc（披露不拦），judge＝R29／R35／R36／R35披露／R36披露。"""
    hits = []
    spans = quote_spans(text)
    # R29：官方名全角变体（沿 2026-11-03 形制，不剔引号——基线行为不变）
    for name, var in variants.items():
        if var in text:
            hits.append({"kind": "block", "judge": "R29",
                         "note": f"官方名全角变体，应作半角官方形{name}"})
    # R35 机拦：教科书级人物拉丁姓氏（每中译一面一格一行）
    seen_zh = set()
    for name, pat in RE_NAME.items():
        m = pat.search(text)
        if not m:
            continue
        zh = TEXTBOOK_LATIN[name]
        if zh in seen_zh:
            continue
        seen_zh.add(zh)
        note = f"教科书级人物拉丁形，§4.4 二应作既定中译{zh}"
        if in_quote(spans, m.start()):
            note += "；命中位于弯引号引文内，逐字保真红线适用，人工判改法"
        prefix = text[:m.start()]
        if prefix.strip() and re.search(r"[A-Z][a-z]+(?:\s[A-Z][a-z]+)*\s$", prefix):
            note += "；全名形（姓氏应作中译，名段改法人工判）"
        hits.append({"kind": "block", "judge": "R35", "note": note})
    # R35 披露一：无译名名单人物疑似自译形（每人物一行）
    seen_en = set()
    for zh, en in NOLATIN_ZH.items():
        if zh in text and en not in seen_en:
            seen_en.add(en)
            hits.append({"kind": "disc", "judge": "R35披露",
                         "note": f"披露：疑似 §4.4 二无译名保留拉丁名单人物（{en}）之自译形{zh}，译名以术语表核，人工判"})
    # R35 披露二：“拉丁串＋冒号”待判形（剔引号后；官方名与常见技术词剔除）
    seen_tok = set()
    for m in RE_COLON.finditer(strip_quotes(text)):
        tok = m.group(1)
        if not tok[0].isupper():
            continue
        if tok.lower() in COLON_EXCLUDE or tok in TEXTBOOK_LATIN or tok in seen_tok:
            continue
        seen_tok.add(tok)
        hits.append({"kind": "disc", "judge": "R35披露",
                     "note": f"披露：拉丁串{tok}后接冒号待判形（疑似人名双层或未收录专名），人工判"})
    # R36 机拦一：Research Unix 版次之阿拉伯序数（上下文同现才拦）
    ar_hits = RE_ARABIC_ED.findall(text)
    if ar_hits and RE_RU_CTX.search(text):
        hits.append({"kind": "block", "judge": "R36",
                     "note": "Research Unix 版次应作汉字序数（§4.4 三），阿拉伯序数版次检出 " +
                             "、".join(sorted(set(ar_hits)))})
    # R36 机拦二：-RELEASE 拼写非全大写
    bad_rel = [m.group() for m in RE_REL_ANY.finditer(strip_quotes(text))
               if not m.group().endswith("RELEASE")]
    if bad_rel:
        hits.append({"kind": "block", "judge": "R36",
                     "note": "-RELEASE 应全大写官方形（§4.4 三产品版本号官方形），拼写检出 " +
                             "、".join(sorted(set(bad_rel)))})
    # R36 披露一：阿拉伯序数版次（无 Research Unix 上下文者全量披露）
    if ar_hits and not RE_RU_CTX.search(text):
        hits.append({"kind": "disc", "judge": "R36披露",
                     "note": "披露：阿拉伯序数版次形检出 " + "、".join(sorted(set(ar_hits))) +
                             "，分流待人工判（Research Unix 版次应作汉字序数；规范／书籍版次不属此判）"})
    # R36 披露二：-RELEASE 与裸版本号两态并存
    if RE_REL_ANY.search(strip_quotes(text)) and RE_REL_BARE.search(strip_quotes(text)):
        hits.append({"kind": "disc", "judge": "R36披露",
                     "note": "披露：同面 -RELEASE 与裸版本号两态并存，分流待人工判"})
    # R36 披露三：拉丁序数版次形（剔引号后；元语言题不含序数不触及）
    if RE_LATIN_ORD.search(strip_quotes(text)):
        hits.append({"kind": "disc", "judge": "R36披露",
                     "note": "披露：拉丁序数版次形（如 First Edition／2nd Edition）待人工判；逐字引文已剔，元语言题不触及"})
    return hits

def scan():
    """全库扫描（题名 col5＋论题 col6）。返回结构化命中行列表（供 stdout 与 TSV 落盘）。"""
    variants = build_variants()
    files = sorted(TD.glob("V*.tsv"))
    assert files, "判据非空纪律：台账目录为空"
    rows = []
    for lp in files:
        for ln in lp.read_text(encoding="utf-8").splitlines():
            f = ln.split("\t")
            if len(f) < 6 or f[0] == "subsection_id":
                continue
            for col, colname in ((4, "题名"), (5, "论题")):
                cell = f[col]
                if not cell.strip():
                    continue
                for h in check_cell(cell, variants):
                    rows.append({"hit_id": f[0], "col_kind": colname,
                                 "text": cell, **h})
    return rows

def selftest():
    """判据非空＋三组新判据夹具：违例必命中、合法必不误报。"""
    v = build_variants()
    assert OFFICIAL, "自检失败：OFFICIAL 白名单为空"
    assert len(OFFICIAL) == 49, f"自检失败：白名单应为 49 项，实 {len(OFFICIAL)}"
    assert len(v) == 17, f"自检失败：斜杠官方名应为 17 项（与 2026-11-03 基线变体面一致），实 {len(v)}"
    assert "CP/M" in v and v["CP/M"] == "CP／M", "自检失败：CP/M 变体缺失"
    for noslash in ("IBM", "UFS", "System V", "SCO UNIX", "4.1BSD", "SunOS"):
        assert noslash not in v, f"自检失败：无斜杠官方名 {noslash} 不得产变体"
    # R29 夹具：全角变体必命中
    assert any(h["judge"] == "R29" for h in check_cell("CP／M 的微机路径", v)), \
        "自检失败：检测器未命中全角官方名夹具"
    # R35 机拦：教科书级拉丁形必命中
    assert any(h["kind"] == "block" for h in check_cell("McKusick 兼具创始参与者与史书作者双重身份", v)), \
        "自检失败：R35 未命中教科书级拉丁形"
    assert any(h["kind"] == "block" for h in check_cell("Raymond 文本在 1998 年 2 月改词", v)), \
        "自检失败：R35 未命中 Raymond"
    assert any(h["kind"] == "block" for h in check_cell("McKusick：麦库西克双层样例", v)), \
        "自检失败：R35 教科书姓与冒号连用形未命中（判据照 §4.4 二原文：教科书级人物应作中译）"
    # R35 合法双层不误报
    for legal in ("博斯蒂克与 Bradner 的通信", "Matt Dillon 与 Karels 的口述",
                  "汤普森与里奇的第六版风格", "Salus 文与 Gurwitz 章",
                  "Justin Gibbs 主导 CAM 的架构与实现"):
        assert not any(h["kind"] == "block" for h in check_cell(legal, v)), \
            f"自检失败：合法双层夹具误拦：{legal}"
    # R35 披露：自译形＋冒号待判形
    d = check_cell("乔利茨撤回认可后的分道", v)
    assert not any(x["kind"] == "block" for x in d) and any(x["judge"] == "R35披露" for x in d), \
        "自检失败：自译形未披露"
    d = check_cell("Sitecom：公司的渠道题样例", v)
    assert not d, "自检失败：剔除词冒号形误披露"
    d = check_cell("ddb：调试器的回归样例", v)
    assert not d, "自检失败：技术词冒号形误披露"
    d = check_cell("活动页逐项列 developer expenses for: 活动名与日期", v)
    assert not d, "自检失败：小写英文串冒号形误披露"
    d = check_cell("arXiv:1910.05798 与 arXiv:1907.x 在案", v)
    assert not d, "自检失败：混合大小写标识符冒号形误披露"
    # R36 机拦
    assert any(h["kind"] == "block" for h in check_cell("Research Unix 第6版的套件面世", v)), \
        "自检失败：R36 未命中 RU 上下文＋阿拉伯序数"
    assert any(h["kind"] == "block" for h in check_cell("FreeBSD 5.3-Release 光盘面世", v)), \
        "自检失败：R36 未命中 RELEASE 拼写错"
    # R36 合法不误报
    for legal in ("第六版手册的修订记", "FreeBSD 9.0-RELEASE 与 nginx 同装",
                  "4.1BSD 磁带交付", "Edition 与 Version 的用法", "SunOS 4.0 的发行"):
        assert not any(h["kind"] == "block" for h in check_cell(legal, v)), \
            f"自检失败：合法版次夹具误拦：{legal}"
    # R36 披露
    d = check_cell("简化网络时间协议第 4 版与第 3 版两套规范", v)
    assert not any(x["kind"] == "block" for x in d) and any(x["judge"] == "R36披露" for x in d), \
        "自检失败：阿拉伯序数版次未披露"
    d = check_cell("FreeBSD 9.0-RELEASE 与 FreeBSD 9.1 并行维护", v)
    assert not any(x["kind"] == "block" for x in d) and any(x["judge"] == "R36披露" for x in d), \
        "自检失败：两态并存未披露"
    d = check_cell("检出为 First Edition Unix 修复", v)
    assert any(x["judge"] == "R36披露" for x in d), "自检失败：拉丁序数版次未披露"
    d = check_cell("零售书目侧逐字“Absolute FreeBSD, 2nd Edition… November 2007”", v)
    assert not d, "自检失败：逐字引文内拉丁序数误披露"
    d = check_cell("逐字“FreeBSD 5.3-Release notes”在案", v)
    assert not d, "自检失败：逐字引文内 RELEASE 拼写照拦"
    print("[selftest] 夹具命中 ✓ 白名单 49 项非空 ✓ R35/R36 新判据夹具（违例必中、合法不误报）✓")
    return 0

def main():
    if "--selftest" in sys.argv:
        return selftest()
    try:
        rows = scan()
    except AssertionError as exc:
        print(f"[EXIT2] 依赖缺失：{exc}")
        return 2
    blocks = [r for r in rows if r["kind"] == "block"]
    discs = [r for r in rows if r["kind"] == "disc"]
    if blocks:
        by_judge = {}
        for r in blocks:
            by_judge[r["judge"]] = by_judge.get(r["judge"], 0) + 1
        stat = "＋".join(f"{k} {v2} 处" for k, v2 in sorted(by_judge.items()))
        print(f"[FAIL] 题名术语形态违例 {len(blocks)} 处（{stat}）：")
        for r in blocks[:10]:
            print(f"  {r['hit_id']} {r['col_kind']} {r['judge']} {r['note']}")
    else:
        print("[PASS] 官方名形态一致＋R35/R36 新判据零机拦（白名单 " + str(len(OFFICIAL)) +
              " 项，全库题名＋论题扫描）")
    if discs:
        print(f"[披露] 拿不准形态 {len(discs)} 处（不拦，人工判）：")
        for r in discs:
            print(f"  {r['hit_id']} {r['col_kind']} {r['judge']} {r['note']}")
    return 1 if blocks else 0

if __name__ == "__main__":
    sys.exit(main())
