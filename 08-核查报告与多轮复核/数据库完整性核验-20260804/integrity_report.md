# 数据库完整性校验报告（前复核基线）

> 生成时间：2026-08-04 ｜ 校验对象：七库 + 18 卷 348 章大纲 ｜ 原则：0-信任 / 卷章对应 / 前后复核


## 一、总体结论

- 章节宇宙：**348** 章 / **18** 卷，全局编号 1–348。
- `chapter_metadata` ↔ 大纲目录一致性：**0 缺失 / 0 多余**（前序重排已校验，本次复验通过）。
- 待处理问题：**高 1 项 / 中 5 项 / 低 3 项**。
- 数据规模：素材 15033（已映射 15008，未映射 25）、交叉引用 667、参考文献匹配 1660（未映射 128）、存疑点 1707、章节述评 71、资料库参考文献 16879。

## 二、关键一致性核查

| 核查项 | 结果 | 说明 |
| --- | --- | --- |
| 章号连续 1–348 | 通过 | 缺失 0 / 重复 0 |
| 元数据↔大纲目录 | 通过 | 仅元数据 0 / 仅目录 0 |
| 概述.md 齐备 | 通过 | 缺 0 章 |
| materials 卷-章范围 | 通过 | 不符 0 |
| chapter_matches 外键 | 通过 | 断键 0 |
| doubts outline_path | 异常 | 断链 1 |
| chapter_reviews outline_path | 通过 | 断链 0 |
| 交叉引用章节越界 | 通过 | 越界 0 |

## 三、问题清单（按严重度）

| 严重度 | 数据库 | 表 | 范围 | 说明 | 计数 |
| --- | --- | --- | --- | --- | --- |
| 高 | doubts_standalone | doubts_to_resolve | outline_path 断链 | 指向不存在的文件；示例：05-卷册大纲/第03卷-伯克利学术文化外溢影响/附录/附录-采访录：Michael Stonebraker.md | 1 |
| 中 | 资料数据库 | materials | 未映射章节(ch=0) | 素材未分配至具体章 | 25 |
| 中 | references_fulltext | chapter_matches | 未映射章节(primary=0) | 参考文献未分配至章 | 128 |
| 中 | references_fulltext | chapter_matches | primary_volume 缺失(=0) | 有 primary_chapter 但 volume 未记录，须由章号推导补全 | 148 |
| 中 | references_fulltext | chapter_matches | primary_volume 与章号不符(陈旧) | primary_volume 与 primary_chapter 推导卷不符，疑似重排前旧值 | 339 |
| 中 | doubts_standalone | doubts_to_resolve | 章节无法解析 | 路径无法映射到有效章号；示例：05-卷册大纲/第10卷-openbsd的历史/卷末书目述评.md | 05-卷册大纲/第11卷-dragonflybsd的历史/卷末书目述评.md | 05-卷册大纲/第11卷-dragonflybsd的历史/卷末书目述评.md | 4 |
| 低 | 07-事实核查记录/fact_checks.db | cross_references | 本地链接断链 | markdown_link 指向不存在本地文件 (pending=17) | 7 |
| 低 | 08-核查报告与多轮复核/review_reports.db | cross_references | 本地链接断链 | markdown_link 指向不存在本地文件 (pending=16) | 1 |
| 低 | 10-交叉索引/cross_indexes.db | cross_references | 本地链接断链 | markdown_link 指向不存在本地文件 (pending=15) | 15 |

## 四、各库行数快照

| 数据库 | 关键表 | 行数 |
| --- | --- | --- |
| metadata_interfaces | chapter_metadata | 348 |
| 资料数据库 | materials | 15033 |
| 资料数据库 | material_cross_references | 667 |
| 资料数据库 | references | 16879 |
| references_fulltext | chapter_matches | 1660 |
| references_fulltext | chapter_reviews | 71 |
| doubts_standalone | doubts_to_resolve | 1707 |