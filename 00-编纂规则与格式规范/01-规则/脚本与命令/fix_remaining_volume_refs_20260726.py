"""
修复脚本：处理剩余的旧卷名路径引用（2026-07-26）

问题：原脚本使用了负向回顾断言 (?<![： \n，\"'（(])，导致"："后紧跟"第N卷/"的路径
形式没有被替换（如"明确拆分对象：第二卷/第22章"）。

修复策略：
- 直接替换"第N卷/"（带斜杠）为"第NN卷-slug/"
- 不使用负向回顾断言，因为"第N卷/"带斜杠就一定是路径形式
- 标题形式"第N卷："或"第N卷 "不会被误替换（因为后面不是"/"）

同时处理待复核清单.md 中的"第七卷/00-总览.md"引用。
"""

import re
from pathlib import Path

PROJECT_ROOT = Path(r"c:\Users\ykla\Documents\hibsd")

RENAME_MAP = {
    "第一卷": "第01卷-unix的起源",
    "第二卷": "第02卷-伯克利的岁月",
    "第三卷": "第03卷-大分裂与四大bsd的诞生",
    "第四卷": "第04卷-扎根与深耕",
    "第五卷": "第05卷-freebsd技术现代化",
    "第六卷": "第06卷-netbsd的历史",
    "第七卷": "第07卷-openbsd的历史",
    "第八卷": "第08卷-dragonflybsd的历史",
    "第九卷": "第09卷-macos的bsd遗产",
    "第十卷": "第10卷-bsd衍生操作系统",
    "第十一卷": "第11卷-商业生态与许可证哲学",
    "第十二卷": "第12卷-全球社区与合规治理",
}


def fix_remaining_references() -> dict:
    """修复剩余的旧卷名路径引用"""
    stats = {"modified_files": 0, "total_replacements": 0, "details": []}

    # 按卷号长度降序排列，避免“第十卷”被“第一卷”部分匹配
    sorted_volumes = sorted(RENAME_MAP.items(), key=lambda x: len(x[0]), reverse=True)

    # 扫描所有 .md 文件
    exclude_dirs = {".trae", "script", ".git", "node_modules"}
    md_files = []
    for p in PROJECT_ROOT.rglob("*.md"):
        rel = p.relative_to(PROJECT_ROOT)
        if any(part in exclude_dirs for part in rel.parts):
            continue
        md_files.append(p)

    for md_file in md_files:
        try:
            content = md_file.read_text(encoding="utf-8")
        except Exception as e:
            stats["details"].append(f"读取失败 {md_file.relative_to(PROJECT_ROOT)}: {e}")
            continue

        original_content = content
        file_replacements = 0

        for old_vol, new_vol in sorted_volumes:
            # 直接替换“第N卷/”（带斜杠），不使用负向回顾断言
            pattern = rf"{re.escape(old_vol)}/"
            replacement = f"{new_vol}/"
            new_content, count = re.subn(pattern, replacement, content)
            if count > 0:
                content = new_content
                file_replacements += count
                stats["details"].append(
                    f"  {md_file.relative_to(PROJECT_ROOT)}: {old_vol}/ → {new_vol}/ x{count}"
                )

        if content != original_content:
            md_file.write_text(content, encoding="utf-8")
            stats["modified_files"] += 1
            stats["total_replacements"] += file_replacements

    return stats


def main():
    print("=" * 70)
    print("修复剩余旧卷名路径引用")
    print("=" * 70)

    stats = fix_remaining_references()
    print(f"\n修改文件数：{stats['modified_files']}")
    print(f"总替换次数：{stats['total_replacements']}")
    print(f"\n替换明细：")
    for detail in stats["details"]:
        print(detail)

    print("\n" + "=" * 70)
    print("修复完成")
    print("=" * 70)


if __name__ == "__main__":
    main()
