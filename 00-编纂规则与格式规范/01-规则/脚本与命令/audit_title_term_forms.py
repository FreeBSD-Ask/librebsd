# -*- coding: utf-8 -*-
"""audit_title_term_forms.py —— 第四十一件：题名术语形态门禁（2026-11-03 立）。
    判据：《小节建制与题名规则》§4.4 形态附表——官方名内部斜杠半角（白名单全库比对题名列＋论题列）。
    用法：
        python audit_title_term_forms.py            # 0 一致 / 1 不一致 / 2 依赖缺失
        python audit_title_term_forms.py --selftest # 判据非空：造夹具须 FAIL
    范围：05-卷册大纲/映射/title-design/*.tsv 全卷（题名 col5＋论题 col6）。
    纪律：判据非空（OFFICIAL 为空即退出码 2）；白名单外拉丁专名不拦（披露面留给人工）。
"""
import sys
from pathlib import Path

ROOT = Path(r"D:/librebsd")
TD = ROOT / "05-卷册大纲/映射/title-design"

# §4.4 附表一：官方名（半角为唯一合法形态；全角变体出现即 FAIL）
OFFICIAL = [
    "CP/M", "Net/1", "Net/2", "System/360", "VAX-11/750", "TCP/IP",
    "BSD/386", "BSD/OS", "GNU/Linux", "GNU/kFreeBSD", "Power 6/32",
    "MI/MD", "AIEE/IRE", "Darwin/XNU", "BSD/Mach", "V6/PWB", "macOS/Darwin",
]

def build_variants():
    """官方名 → 全角变体（/ → ／）。判据非空纪律：OFFICIAL 为空即失败。"""
    assert OFFICIAL, "判据非空纪律：OFFICIAL 白名单不得为空"
    return {name: name.replace("/", "／") for name in OFFICIAL}

def scan():
    variants = build_variants()
    hits = []
    files = sorted(TD.glob("V*.tsv"))
    assert files, "判据非空纪律：台账目录为空"
    for lp in files:
        for ln_i, ln in enumerate(lp.read_text(encoding="utf-8").splitlines()):
            f = ln.split("\t")
            if len(f) < 6 or f[0] == "subsection_id":
                continue
            for col, colname in ((4, "题名"), (5, "论题")):
                for name, var in variants.items():
                    if var in f[col]:
                        hits.append(f"{lp.name} {f[0]} {colname}「{var}」应为「{name}」")
    return hits

def selftest():
    """判据非空：以全角 CP／M 样本验证检测器必命中。"""
    v = build_variants()
    sample = "CP／M 的微机路径"
    ok = any(var in sample for var in v.values())
    assert ok, "自检失败：检测器未命中全角官方名夹具"
    assert "CP/M" in v, "自检失败：白名单缺 CP/M"
    print("[selftest] 夹具命中 ✓ 白名单非空 ✓")
    return 0

def main():
    if "--selftest" in sys.argv:
        return selftest()
    hits = scan()
    if hits:
        print(f"[FAIL] 官方名全角残留 {len(hits)} 处：")
        for h in hits[:10]:
            print("  " + h)
        return 1
    print("[PASS] 官方名形态一致（白名单 " + str(len(OFFICIAL)) + " 项，全库题名＋论题扫描）")
    return 0

if __name__ == "__main__":
    sys.exit(main())
