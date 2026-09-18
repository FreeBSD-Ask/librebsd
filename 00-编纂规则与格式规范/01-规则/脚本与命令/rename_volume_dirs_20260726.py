"""
卷文件夹重命名脚本（2026-07-26）

功能：
1. 将 05-卷册大纲/ 下的 12 个卷文件夹从"第N卷/"重命名为"第NN卷-中文slug/"格式
2. 更新所有 .md 文件中对卷文件夹的路径引用
3. 不修改标题文本中的卷名（如"第一卷：UNIX 的起源"保持不变）

替换规则：
- 路径形式 "第N卷/" → "第NN卷-slug/"
- 旧路径形式 "../大纲/第N卷/" → "../第NN卷-slug/"
- 标题形式 "第N卷：" 或 "第N卷 " 保持不变（不替换）

注意：
- 属于"序号调整例外"中的"文件名与编号同步调整"，允许使用脚本
- 脚本输出修改日志，便于手动复核
- 修改前后均需复核
"""

import re
import shutil
from pathlib import Path

PROJECT_ROOT = Path(r"c:\Users\ykla\Documents\hibsd")
OUTLINE_DIR = PROJECT_ROOT / "05-卷册大纲"

# 卷文件夹重命名映射：原名 → 新名
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


def rename_volume_dirs() -> list[str]:
    """重命名 12 个卷文件夹"""
    actions = []
    for old_name, new_name in RENAME_MAP.items():
        old_path = OUTLINE_DIR / old_name
        new_path = OUTLINE_DIR / new_name
        if not old_path.exists():
            actions.append(f"跳过（不存在）：{old_name}/")
            continue
        if new_path.exists():
            actions.append(f"跳过（目标已存在）：{new_name}/")
            continue
        old_path.rename(new_path)
        actions.append(f"重命名：{old_name}/ → {new_name}/")
    return actions


def update_references() -> dict:
    """更新所有 .md 文件中的卷文件夹路径引用

    替换规则（按优先级）：
    1. "../大纲/第N卷/" → "../第NN卷-slug/"（旧路径形式，vol-1.md/vol-2.md）
    2. "第N卷/" → "第NN卷-slug/"（标准路径形式）

    不替换：
    - "第N卷："（标题形式）
    - "第N卷 "（标题形式带空格）
    - "第N卷，"（标题形式带逗号）
    - "第N卷\n"（行尾，可能是标题）
    """
    stats = {"modified_files": 0, "total_replacements": 0, "details": []}

    # 构建替换模式：按卷号长度降序排列，避免“第十卷”被“第一卷”部分匹配
    sorted_volumes = sorted(RENAME_MAP.items(), key=lambda x: len(x[0]), reverse=True)

    # 扫描所有 .md 文件（排除 .trae/specs/ 和 script/ 目录）
    exclude_dirs = {".trae", "script", ".git", "node_modules"}
    md_files = []
    for p in PROJECT_ROOT.rglob("*.md"):
        # 排除指定目录
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
            # 模式 1: “../大纲/第N卷/” → “../第NN卷-slug/”
            # 这种旧路径形式主要在 vol-1.md 和 vol-2.md 中
            pattern1 = rf"\.\./大纲/{re.escape(old_vol)}/"
            replacement1 = f"../{new_vol}/"
            new_content, count1 = re.subn(pattern1, replacement1, content)
            if count1 > 0:
                content = new_content
                file_replacements += count1
                stats["details"].append(
                    f"  {md_file.relative_to(PROJECT_ROOT)}: 模式1(旧路径) {old_vol}/ → {new_vol}/ x{count1}"
                )

            # 模式 2: “第N卷/” → “第NN卷-slug/”
            # 标准路径形式，需确保前面不是“：”或“ ”或“\n”（避免标题）
            # 使用负向回顾断言：前面不能是 ：、空格、换行、引号、，
            pattern2 = rf"(?<![： \n，\"'（(]){re.escape(old_vol)}/"
            replacement2 = f"{new_vol}/"
            new_content, count2 = re.subn(pattern2, replacement2, content)
            if count2 > 0:
                content = new_content
                file_replacements += count2
                stats["details"].append(
                    f"  {md_file.relative_to(PROJECT_ROOT)}: 模式2(路径) {old_vol}/ → {new_vol}/ x{count2}"
                )

        if content != original_content:
            md_file.write_text(content, encoding="utf-8")
            stats["modified_files"] += 1
            stats["total_replacements"] += file_replacements

    return stats


def main():
    print("=" * 70)
    print("卷文件夹重命名脚本")
    print("=" * 70)

    print("\n[1/2] 重命名卷文件夹")
    print(f"  目录：05-卷册大纲/")
    for line in rename_volume_dirs():
        print(f"  {line}")

    print("\n[2/2] 更新 .md 文件中的路径引用")
    stats = update_references()
    print(f"  修改文件数：{stats['modified_files']}")
    print(f"  总替换次数：{stats['total_replacements']}")
    print(f"\n  替换明细（前 50 条）：")
    for detail in stats["details"][:50]:
        print(detail)
    if len(stats["details"]) > 50:
        print(f"  ... 还有 {len(stats['details']) - 50} 条明细")

    print("\n" + "=" * 70)
    print("重命名完成。请手动复核修改明细。")
    print("=" * 70)


if __name__ == "__main__":
    main()
