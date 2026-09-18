#!/usr/bin/env python3
"""将数据库调研发现写入大纲文件。
读取 db_deep_analysis.json，逐章更新 index.md 中的 要点、史料、史观、辨析、文献 字段。
"""

import json
import os
import re
from pathlib import Path

BASE = r"d:\librebsd"
OUTLINE_BASE = os.path.join(BASE, "05-卷册大纲")

# 读取深度分析结果
with open(os.path.join(BASE, "script", "db_deep_analysis.json"), "r", encoding="utf-8") as f:
    analysis = json.load(f)

chapter_mapping = {int(k): v for k, v in analysis["chapter_mapping"].items()}
code_repos = analysis["code_repos"]
func = analysis["functional"]

# 章节 slug 映射（从已有的目录结构获取）
chapter_slug_map = {}

for vol_dir in sorted(os.listdir(OUTLINE_BASE)):
    vol_path = os.path.join(OUTLINE_BASE, vol_dir)
    if not os.path.isdir(vol_path) or not vol_dir.startswith("第"):
        continue
    for ch_dir in sorted(os.listdir(vol_path)):
        ch_path = os.path.join(vol_path, ch_dir)
        if not os.path.isdir(ch_path) or not ch_dir.startswith("第"):
            continue
        idx_file = os.path.join(ch_path, "index.md")
        if not os.path.exists(idx_file):
            continue
        # 提取章号
        m = re.match(r"第(\d+)章", ch_dir)
        if m:
            ch_num = int(m.group(1))
            chapter_slug_map[ch_num] = {
                "dir": ch_dir,
                "path": ch_path,
                "index": idx_file,
                "volume": vol_dir
            }


# ============================================================
# 编写要点内容（基于数据库发现）
# ============================================================

def generate_yaodian(ch_num, findings):
    """从数据库发现生成 2-4 句核心史实"""
    lines = []
    for f in findings:
        if f["category"] == "史料":
            lines.append(f"- {f['content']}")
    return lines[:4] if lines else ["- （待从数据库提取）"]


def generate_shiliao(ch_num, findings):
    """从数据库发现生成史料字段"""
    lines = []
    for f in findings:
        if f["category"] == "史料":
            db_name = f["source_db"]
            lines.append(f"- [DB:code_repos:{db_name}] {f['content']}")
    return lines if lines else ["- （待从数据库提取）"]


def generate_shiguan(ch_num, findings):
    """从数据库发现生成史观字段"""
    # 基于章节内容映射 25 条总纲
    shiguan_principles = {
        # 第1卷: UNIX 起源
        1: "形式主义史观：UNIX 的起源是多重偶然性的产物，非必然进步",
        65: "多方平等：FreeBSD 的创建是 patchkit 协调人模式的产物，非单一英雄叙事",
        67: "经验优先：NetBSD 的可移植执念根植于对硬件多样性的经验性尊重",
        69: "和解优于斗争：OpenBSD 的起源虽源于冲突（de Raadt 被逐），但最终走向安全至上",
        78: "循环而非进步：Linux 与 BSD 的竞争不是谁胜谁负，而是分离聚合的循环",
        88: "动手者创造历史：FreeBSD 2.x 的稳定是无数默默贡献者的工程积累",
        109: "自反性：ZFS 的设计哲学本身就是对传统文件系统范式的一次自反性重构",
        127: "偶然性优先：FreeBSD 10.0 的大整合是多项技术路线偶然交汇的结果",
        172: "形式主义：NetBSD 的历史是'可移植性'这一形式主义概念在不同硬件平台上的物质化",
        193: "经验优先：OpenBSD 的代码审计文化是安全至上的经验性实践",
        206: "动手者创造历史：OpenSSH 的全球采纳是无数系统管理员默默部署的结果",
        214: "偶然性优先：DragonFly BSD 的诞生源于 Dillon 与 FreeBSD 5.x 技术路线的偶然分歧",
        225: "自反性：Dillon 的个人主导模式是对'开源社区民主'神话的自反性挑战",
        240: "形式主义：Darwin 的开源是 Apple 对开源社区的形式主义承诺",
        259: "多方平等：BSD 衍生项目群在本体论层面平等，不因规模大小而有高低",
        297: "循环而非进步：illumos 是 OpenSolaris 的循环性续命，非进步",
        347: "动手者创造历史：交叉索引库中的人物记录是对'伟大人物史观'的纠正",
        350: "自反性：sacred 源材料库是本书编纂方法论的自反性根源",
    }
    if ch_num in shiguan_principles:
        return [f"- {shiguan_principles[ch_num]}"]
    return ["- （待从数据库与 shigang.md 映射）"]


def generate_bianxi(ch_num, findings):
    """从数据库发现生成辨析字段"""
    lines = []
    for f in findings:
        if f["category"] == "辨析":
            lines.append(f"- {f['content']}")
    if not lines:
        lines.append("- （待从数据库考据记录提取）")
    return lines


def generate_wenxian(ch_num, findings):
    """从数据库发现生成文献字段"""
    # 从 references_fulltext 库中引用
    lines = []
    for f in findings:
        if f["category"] == "文献":
            lines.append(f"- {f['content']}")
    if not lines:
        # 自动生成数据库引用
        db_refs = set()
        for f in findings:
            db_refs.add(f["source_db"])
        for db in sorted(db_refs):
            lines.append(f"- [DB:references_fulltext] 参考文献全文数据库（4,077 篇全文，27,138 条时间线事件）")
            break
        if not lines:
            lines.append("- （待从参考文献总目提取）")
    return lines


# ============================================================
# 读取并更新章节文件
# ============================================================
print("=" * 80)
print("开始写入大纲文件...")
print("=" * 80)

updated_count = 0
skipped_count = 0

for ch_num, findings in sorted(chapter_mapping.items()):
    if ch_num not in chapter_slug_map:
        print(f"  [跳过] 第{ch_num}章：目录不存在")
        skipped_count += 1
        continue

    ch_info = chapter_slug_map[ch_num]
    idx_path = ch_info["index"]

    with open(idx_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 生成各字段内容
    yaodian = generate_yaodian(ch_num, findings)
    shiliao = generate_shiliao(ch_num, findings)
    shiguan = generate_shiguan(ch_num, findings)
    bianxi = generate_bianxi(ch_num, findings)
    wenxian = generate_wenxian(ch_num, findings)

    # 检查是否已有内容（非占位符）
    has_yaodian = "（待从概述提取）" not in content and "（待从数据库提取）" not in content
    has_shiguan = "（待补）" not in content
    has_bianxi = "（待补）" not in content
    has_wenxian = "（待补）" not in content

    # 更新 要点
    if not has_yaodian:
        new_yaodian = "## 要点\n\n" + "\n".join(yaodian)
        content = re.sub(r"## 要点\n\n（待从概述提取）", new_yaodian, content)

    # 更新 史料（追加新条目）
    shiliao_section = re.search(r"## 史料\n\n", content)
    if shiliao_section:
        # 在史料段末尾追加新条目
        new_shiliao_entries = []
        for line in shiliao:
            if line not in content:
                new_shiliao_entries.append(line)
        if new_shiliao_entries:
            # 找到史料段末尾（下一个 ## 之前）
            shiliao_end = content.find("\n## ", shiliao_section.end())
            if shiliao_end == -1:
                shiliao_end = len(content)
            insert_pos = shiliao_end
            content = content[:insert_pos] + "\n" + "\n".join(new_shiliao_entries) + content[insert_pos:]

    # 更新 史观
    if not has_shiguan:
        new_shiguan = "## 史观\n\n" + "\n".join(shiguan)
        content = re.sub(r"## 史观\n\n（待补）", new_shiguan, content)

    # 更新 辨析
    if not has_bianxi:
        new_bianxi = "## 辨析\n\n" + "\n".join(bianxi)
        content = re.sub(r"## 辨析\n\n（待补）", new_bianxi, content)

    # 更新 文献
    if not has_wenxian:
        new_wenxian = "## 文献\n\n" + "\n".join(wenxian)
        content = re.sub(r"## 文献\n\n（待补）", new_wenxian, content)

    with open(idx_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

    print(f"  [已更新] 第{ch_num}章 ({ch_info['volume']}/{ch_info['dir']})")
    updated_count += 1

print(f"\n更新完成: {updated_count} 章已更新, {skipped_count} 章跳过")
print(f"共 {len(chapter_mapping)} 章有待写入的数据库发现")


# ============================================================
# 创建 00-总览.md 更新（为每卷添加数据库调研摘要）
# ============================================================
print("\n" + "=" * 80)
print("更新卷总览（数据库调研摘要）...")
print("=" * 80)

# 按卷分组
vol_chapters = defaultdict(list)
for ch_num, ch_info in chapter_slug_map.items():
    vol = ch_info["volume"]
    vol_chapters[vol].append(ch_num)

vol_updated = 0
for vol_dir, chapters in sorted(vol_chapters.items()):
    overview_path = os.path.join(OUTLINE_BASE, vol_dir, "00-总览.md")
    if not os.path.exists(overview_path):
        continue

    # 检查该卷下是否有章节被更新
    updated_chapters = [ch for ch in chapters if ch in chapter_mapping]
    if not updated_chapters:
        continue

    with open(overview_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 检查是否已有数据库调研摘要
    if "## 数据库调研摘要" in content:
        continue

    # 生成摘要
    summary_lines = []
    summary_lines.append("\n## 数据库调研摘要\n")
    summary_lines.append(f"本卷共 {len(updated_chapters)} 章有数据库调研发现，覆盖代码仓库、功能数据库等维度。\n")

    for ch_num in sorted(updated_chapters):
        findings = chapter_mapping.get(ch_num, [])
        dbs = set(f["source_db"] for f in findings)
        summary_lines.append(f"- 第{ch_num}章：涉及数据库 {', '.join(sorted(dbs))}")

    # 追加到文件末尾
    content = content.rstrip() + "\n" + "\n".join(summary_lines) + "\n"

    with open(overview_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

    print(f"  [已更新] {vol_dir}/00-总览.md")
    vol_updated += 1

print(f"\n卷总览更新完成: {vol_updated} 卷")

# ============================================================
# 输出统计
# ============================================================
print("\n" + "=" * 80)
print("写入统计")
print("=" * 80)
print(f"已更新章节: {updated_count}")
print(f"已更新卷总览: {vol_updated}")
print(f"数据库发现总数: {sum(len(v) for v in chapter_mapping.values())}")
print(f"涉及章节: {len(chapter_mapping)}")
print(f"涉及卷: {len(set(chapter_slug_map[ch]['volume'] for ch in chapter_mapping if ch in chapter_slug_map))}")