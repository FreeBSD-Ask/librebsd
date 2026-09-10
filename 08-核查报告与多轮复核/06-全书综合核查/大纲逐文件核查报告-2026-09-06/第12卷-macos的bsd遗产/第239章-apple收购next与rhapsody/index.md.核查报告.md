# 核查报告：第12卷-macos的bsd遗产/第239章-apple收购next与rhapsody/index.md

- 源文件：d:\librebsd\05-卷册大纲\第12卷-macos的bsd遗产\第239章-apple收购next与rhapsody\index.md
- 批次：C164；检查日期：2026-09-11；检查方式：逐文件完整阅读人工核查
- SUMMARY.md 收录：未收录（summary_title 与 summary_line 均为 null；机械旗标 UNLISTED_NOT_IN_SUMMARY 经核对属实）
- A 占位符：发现 2 处（行 12 显式“待核/待回源”、行 22 史观“待人工回填”）
- B 内容完整性：发现 1 处（要点多句被截断为残句，行 11/13/14）
- C 编号与标题：发现 1 处（H1 节号格式与文件名空格不一致）
- D 格式规范：发现 1 处（bsd_commits.db 旧库名）
- E 学术规范：通过（史观主段为占位，播客段史观条号 5/22 与基线相符，无失配）
- F SUMMARY 一致性：未收录（旗标 UNLISTED 属实）
- 机械旗标复核：UNLISTED_NOT_IN_SUMMARY——属实，index 未列入 SUMMARY。
- 问题清单：
  1. 行 12 | “〔待核：原文截断，后文待回源〕” | 显式待核占位符，要点内容空缺 | A-占位符 | P1 | 回源补全 Yellow Box/Blue Box 架构要点
  2. 行 22 | “(待人工回填——详见子节文件史观/辨析字段)” | 史观字段空壳占位，未映射总纲 | A-占位符/E-学术规范 | P1 | 人工回填史观并映射 25 条总纲
  3. 行 11/13/14 | “成为 Apple 下一”“负责 Da”“32 位与” | 要点句被截断成残句，内容断裂 | B-内容完整性 | P1 | 回源补全三处句子
  4. 行 33/34/35/36 | “bsd_commits.db 查询 L7.5.1 结果” | 旧库名 bsd_commits.db（主存储已升格 DuckDB，应为 freebsd.duckdb 等） | D-格式 | P2 | 全局替换现行库名
  5. 行 7 | H1“第 239 章 apple收购next与rhapsody”与文件名“第239章-apple收购next与rhapsody”节号间空格/连字符不一致 | 标题格式与文件名不一致 | C-编号与标题 | P3 | 统一为“第239章”或统一加空格

- 结论：存在问题 5 项（P0 0、P1 3、P2 1、P3 1）

补充说明：
1. 行 18 史料仅一条自动注入的 DB:references_fulltext 匹配，无实质史料文本；因本章为目录页且指向子节文件，暂不作独立缺陷，仅提示史料偏薄。
2. 行 38-65 的 PODCAST_REVIEW（BSD Now EP591）主题与本章 Apple/NeXT/Rhapsody 相关，关联性可接受，未列为缺陷；其史观条号 5/22 与基线相符。
3. 行 11 末“成为 Apple 下一”截断，结合行 12 的“待核”标记，显示该要点整体未完成转录。
