# -*- coding: utf-8 -*-
"""audit_data_integrity.py — 重构2026 目录页 DATA 数据完整性审计（固定脚本，规则引用）。

用途：
  目录页 `index.html` 内嵌压缩数据块 `opt-data-blob`（2026-09-13 O-2 起，gzip+base64 载体；
  历史载体 `var DATA = {...}` 保留回退兼容），含 persons 人名数组/refs 文献/revs 修订史。
  历史教训（2026-09-11 实测）：DATA 后处理曾把 persons[].n 数组元素污染为 JSON 残片
  （如 `"value": "Ken"}")`、邮箱残片（@public.gmane.org）与内部标识串
  （person_id_legacy:xxx / freebsd_account 等）。污染键不致命（页面有净化），
  但会在 AI 逐项审读时产生噪音并掩盖真实缺陷。本脚本在生成流水线出口拦截这类污染。

审计维度：
  1) n 数组 JSON 残片：元素同时含 `"value"` 与 `}`/`]` 或以 `{` 开头；
  2) n 数组邮箱残片：元素含 `@`；
  3) n 数组内部标识串：person_id_legacy:/person_id_new:/freebsd_account:/
     openbsd_account:/netbsd_account:/dragonflybsd_account: 前缀；
  4) 无人类可读姓名的人：整个 n 数组清洗后为空。

用法：python audit_data_integrity.py [index.html 路径]
输出：问题清单（0 问题即通过，exit 0；有问题 exit 1）。
"""
import base64
import gzip
import io
import json
import pathlib
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
DEFAULT = pathlib.Path(r"D:/librebsd/08-核查报告与多轮复核/重构2026/index.html")
path = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
html = path.read_text(encoding="utf-8")
# 常量：
IDENT_PAT = re.compile(r"^(person_id_(legacy|new):|freebsd_account|openbsd_account|netbsd_account|dragonflybsd_account|name_variant|nickname|other)\b")

issues = []

# 提取数据载荷（2026-09-13 O-2 起：优先压缩数据块 opt-data-blob，回退历史 var DATA 载体）
data = None
m_blob = re.search(r'<script[^>]*id="opt-data-blob"[^>]*>\n(.*?)\n</script>', html, re.S)
if m_blob:
    try:
        data = json.loads(gzip.decompress(base64.b64decode(re.sub(r"\s+", "", m_blob.group(1)))).decode("utf-8"))
    except Exception as e:
        issues.append(f"压缩数据块解码失败：{e}")
        data = None
else:
    m_data = re.search(r"var\s+DATA\s*=\s*(\{.*?\});\s*(?:\n\s*var\s+\w+\s*=|$)", html, re.S)
    if not m_data:
        issues.append("未找到数据载荷（压缩数据块 opt-data-blob 与历史 var DATA 载体均未命中）")
    else:
        raw = m_data.group(1)
        try:
            data = json.loads(raw)
        except json.JSONDecodeError as e:
            issues.append(f"DATA 段不是合法 JSON：{e}")
            data = None
    if data is not None:
        persons = data.get("persons") or []
        if len(persons) == 0:
            issues.append("persons 数组为空")
        # 形态检测：P2 枚举化/扁平同构双兼容
        enum_mode = any("names" in p for p in persons[:5]) if persons else False
        # 1) JSON 残片（枚举化：检查 names.zh / names.en；扁平：检查 n）
        candidates = []
        if enum_mode:
            for p in persons:
                c = []
                for t in (p.get("names", {}).get("zh") or []) + (p.get("names", {}).get("en") or []):
                    if isinstance(t, str):
                        c.append(t)
                candidates.append((p.get("id", "?"), c))
        else:
            for p in persons:
                c = [x for x in (p.get("n") or []) if isinstance(x, str)]
                candidates.append((p.get("r", "?"), c))
        for pid, items in candidates:
            for s0 in items:
                s = s0.strip()
                if (s.startswith("{") and '"value"' in s) or (s.endswith("}") and '"value"' in s):
                    issues.append(f"n 数组 JSON 残片：{s[:60]}（{pid}）")
        # 2) 邮箱条目提示（2026-09-11 收敛：BSD committer 邮箱系真实身份史料，
        #    如 terry@freebsd.org，非污染；仅提示不再判错，禁止按黑名单删除）
        email_hint = sum(1 for _pid, items in candidates for x in items if "@" in x)
        if email_hint:
            print(f"提示：n 数组含邮箱/账户形态条目 {email_hint} 个（committer 邮箱属有效身份史料，不判错、不删除）")
        # 3) 内部标识串
        for pid, items in candidates:
            for s0 in items:
                if IDENT_PAT.search(s0.strip()):
                    issues.append(f"n 数组内部标识串：{s0.strip()[:60]}（{pid}）")
        # 4) 无人名
        for pid, items in candidates:
            clean = [x for x in items if "@" not in x and not IDENT_PAT.search(x.strip()) and '"value"' not in x]
            has_human = any(re.search(r"[A-Za-z\u4e00-\u9fff]", x) for x in clean)
            if not has_human:
                issues.append(f"此人 n 数组全部污染无法识别：{pid}")
        # 数据规模提示（非问题，仅输出）
        total_names = sum(len(x[1]) for x in candidates)
        print(f"DATA 摘要：persons={len(persons)}，n 数组总元素={total_names}，形态={'枚举化' if enum_mode else '扁平同构'}，refs={len(data.get('refs') or {})}，revisions={len(data.get('revs') or [])}")

print(f"审计文件：{path}")
print(f"DATA 数据完整性审计问题：{len(issues)} 处")
for x in issues:
    print(" -", x)
sys.exit(1 if issues else 0)