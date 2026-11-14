"""文档校对形式门禁（第四十四件，2026-11-14 立）。

依据：GB/T 15834-2011（标点）、GB/T 15835-2011（数字）、GB 3100-1993 §6.2.4
（数值与单位符号间留空隙）、GB/T 3101-1993 §3.3.1（千分空）、
《图书校对工作基本规程》§6（标点、数字、量和单位差错）。

判据：
  P1 数值与单位符号之间缺一个半角空格（°／′／″ 例外）
  P2 多位数使用千分撇（应为千分空）
  P3 年份／数值区间使用 U+2013（应为一字线 U+2014）
  P4 “、以及”（“以及”前应为逗号）
  P5 省略号与“等／等等”并用
  P6 同形括号套用（只报告，不计 FAIL）

用法：
    python audit_proofread_forms.py            # 0 通过 / 1 有 FAIL / 2 依赖或路径错误
    python audit_proofread_forms.py --all      # 含 P6 明细
    python audit_proofread_forms.py --root D:/librebsd   # 默认只扫规则／治理文档（约 110 件），--root 另指根
    python audit_proofread_forms.py --selftest
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
import tempfile

UNITS = (
    "PB/s|TB/s|GB/s|MB/s|KB/s|PB|TB|GB|MB|KB|kW|MW|GW|W|mA|kV|mV|kJ|MJ"
    "|ms|µs|us|ns|kg|mg|MHz|GHz|kHz|Hz|mm|cm|km|mL"  # 不收单字母 B：与第68B章、3B 线标识等编号形难分
)
P1 = re.compile(r"(?<![\w/#._-])(?<!U\+)(\d+(?:\.\d+)?)(" + UNITS + r")(?![\w./-])")
P2 = re.compile(r"(?<![\w.])\d{1,3}(?:,\d{3})+(?![\w])")
P3 = re.compile(r"[0-9A-Za-z一-鿿]\s*–\s*[0-9A-Za-z一-鿿]")  # 区间／起止／并列用 U+2014；ASCII 连字符年份区间不判（与标准号 GB/T 7714-2015 等无法区分，标题层由第三十九件 B7 管）
P4 = re.compile(r"、以及")
P5 = re.compile(r"……等")
P6 = re.compile(r"（[^（）\n]*（[^（）\n]*）[^（）\n]*）")

EXCLUDE_PARTS = (
    "旧大纲-20261023",
    "12-重构大纲书目述评",
    "03-文献下载",
    ".trae",
    "script",
    "node_modules",
    ".git",
)


def default_files(root: pathlib.Path) -> list[pathlib.Path]:
    files = [root / "AGENTS.md"]
    for sub in (
        "00-编纂规则与格式规范/01-规则",
        "00-编纂规则与格式规范/02-操作手册",
        "01-项目管理/02-工程决策与技术债",
    ):
        d = root / sub
        if d.exists():
            files.extend(sorted(d.rglob("*.md")))
    out = []
    for f in files:
        if not f.exists():
            continue
        rel = f.as_posix()
        if any(part in rel for part in EXCLUDE_PARTS):
            continue
        out.append(f)
    return out


def mask(text: str) -> list[str]:
    """把围栏代码、行内代码、URL 与 frontmatter 行替换为空行，保持行号。"""
    lines = text.split("\n")
    out: list[str] = []
    in_fence = False
    in_front = False
    for i, line in enumerate(lines):
        if i == 0 and line.strip() == "---":
            in_front = True
            out.append("")
            continue
        if in_front:
            out.append("")
            if line.strip() == "---":
                in_front = False
            continue
        if re.match(r"^\s*(```+|~~~+)", line):
            in_fence = not in_fence
            out.append("")
            continue
        if in_fence:
            out.append("")
            continue
        line = re.sub(r"`[^`]*`", "", line)
        line = re.sub(r"“[^”]*”", "", line)
        line = re.sub(r"《[^》]*》", "", line)
        line = re.sub(r"「[^」]*」", "", line)
        line = re.sub(r"『[^』]*』", "", line)
        line = re.sub(r"https?://\S+", "", line)
        out.append(line)
    return out


def scan_file(path: pathlib.Path) -> list[dict]:
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return []
    findings: list[dict] = []
    for no, line in enumerate(mask(text), 1):
        for code, rx, msg in (
            ("P1", P1, "数值与单位符号之间应留一个半角空格"),
            ("P2", P2, "多位数应使用千分空，不用千分撇"),
            ("P3", P3, "连接号（区间／起止／并列）应使用一字线 U+2014，不用 U+2013；引文保真除外"),
            ("P4", P4, "“以及”前应使用逗号，不用顿号"),
            ("P5", P5, "省略号不应与“等／等等”并用"),
            ("P6", P6, "同形括号套用（宜改用不同形式）"),
        ):
            for m in rx.finditer(line):
                findings.append(
                    {
                        "file": str(path),
                        "line": no,
                        "col": m.start() + 1,
                        "rule": code,
                        "message": msg,
                        "text": m.group(0)[:60],
                    }
                )
    return findings


def selftest() -> int:
    ok = True
    en = "\u2013"
    with tempfile.TemporaryDirectory(prefix="proofread_") as td:
        base = pathlib.Path(td)
        bad = base / "bad.md"
        bad.write_text(
            "打开 5MB 文件，统计 19,468 条。\n"
            "`3,954` 与 `5MB` 与 `1993" + en + "2026` 与「19,468」。\n"
            "区间 1993" + en + "2026 年；卷段 V51" + en + "V56。\n"
            "名单：甲、乙、以及丙。\n"
            "列表……等。\n"
            "嵌套（外层（内层）外层）。\n"
            "```\n5MB 19,468 1993" + en + "2026 、以及 ……等\n```\n",
            encoding="utf-8",
            newline="\n",
        )
        fs = scan_file(bad)
        hits = {f["rule"] for f in fs}
        for code in ("P1", "P2", "P3", "P4", "P5", "P6"):
            if code not in hits:
                print(f"[selftest] FAIL：{code} 未命中")
                ok = False
        # code/inline code 必须豁免
        in_code = [f for f in fs if f["line"] in (2, 7, 8)]
        if in_code:
            print(f"[selftest] FAIL：代码／行内代码未被豁免：{in_code}")
            ok = False
        # P3 须覆盖字母区间（V51–V56），不只数字区间
        p3 = [f for f in fs if f["rule"] == "P3"]
        if len(p3) < 2:
            print(f"[selftest] FAIL：P3 未覆盖字母区间（命中 {len(p3)} 处）")
            ok = False
        good = base / "good.md"
        good.write_text(
            "打开 5 MB 文件，统计 19 468 条。\n"
            "区间 1993\u20142026 年；卷段 V51\u2014V56；角度 30°；单位 20 ℃。\n"
            "名单：甲、乙，以及丙。\n"
            "列表等。\n"
            "文件名 5MB.txt 与版本 2.0.0、编号 1975-2026。\n",
            encoding="utf-8",
            newline="\n",
        )
        gf = scan_file(good)
        if gf:
            print(f"[selftest] FAIL：正样本误报：{gf}")
            ok = False
    print("[selftest] PASS" if ok else "[selftest] FAIL")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=None)
    ap.add_argument("--all", action="store_true", help="打印 P6 明细")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    root = pathlib.Path(args.root).resolve() if args.root else pathlib.Path(__file__).resolve().parents[3]
    files = default_files(root)
    if not files:
        print("未找到待审文件", file=sys.stderr)
        return 2
    findings: list[dict] = []
    for f in files:
        findings.extend(scan_file(f))
    fail = [f for f in findings if f["rule"] != "P6"]
    info = [f for f in findings if f["rule"] == "P6"]
    if args.json:
        print(json.dumps({"files": len(files), "fail": fail, "info": info}, ensure_ascii=False, indent=2))
    else:
        print("文档校对形式门禁（第四十四件）")
        print("=" * 60)
        print(f"扫描 {len(files)} 件；FAIL {len(fail)} 条；P6 只报告 {len(info)} 条")
        for f in fail[:80]:
            print(f"  [{f['rule']}] {f['file']}:{f['line']}:{f['col']} {f['message']} → {f['text']}")
        if args.all:
            for f in info[:80]:
                print(f"  [P6] {f['file']}:{f['line']}:{f['col']} {f['message']}")
    return 0 if not fail else 1


if __name__ == "__main__":
    sys.exit(main())
