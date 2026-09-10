# 核查报告：第11卷-dragonflybsd的历史/第222章-dragonfly2x时代fork必要性的外部批评/index.md

- 源文件：d:\librebsd\05-卷册大纲\第11卷-dragonflybsd的历史\第222章-dragonfly2x时代fork必要性的外部批评\index.md
- 批次：C028；检查日期：2026-09-08；检查方式：逐文件完整阅读人工核查
- SUMMARY.md 收录：未收录（SUMMARY 第 1897 行以概述.md 收录第 222 章，本 index.md 不在 SUMMARY 中）
- A 占位符：发现 1 处（第 22 行史观字段整节为“(待人工回填——详见子节文件史观/辨析字段)”，属待填类空缺标记，不在数据库自动增补豁免范围）
- B 内容完整性：发现 2 处（要点第 1 条句末“DragonFly 从 F”戛然而止、第 3 条“bsd_commits.db drago”截断；辨析第 1 条“回移停止时间节点”后无结句、第 3 条“contribut”截断，均为文本截断空壳化；五字段框架齐备，frontmatter 编号 chapter/id/volume 与目录一致）
- C 编号与标题：通过（H1“第 222 章 dragonfly2x时代fork必要性的外部批评”与目录名一致；frontmatter 旗标自洽；章题与 SUMMARY 概述条目“第 222 章 DragonFly 2.x 时代 fork 必要性的外部批评”语义一致，仅空格/大小写风格差异）
- D 格式规范：发现 2 处（第 32、33、35 行数据库增补块与“## 史料考据补充”标题、“---”分隔线整体塌缩进文献条目行内，Markdown 结构失效；bsd_commits.db、dragonfly.db 等文件名多处未加粗）
- E 学术规范：发现 1 处（史观字段未映射总纲，仅以占位指向子节文件；正文无禁引来源、无禁用名称；引文等级标记［A］使用规范）
- F SUMMARY 一致性：未收录（flags 含 UNLISTED_NOT_IN_SUMMARY，核实属实：SUMMARY 以概述.md 为该章入口，本 index.md 与概述.md 并存，属章入口双轨）
- 机械旗标复核：UNLISTED_NOT_IN_SUMMARY——核实为“未收录”，属实；建议明确 index.md 与概述.md 的分工或合并入口，避免章入口二义

- 问题清单：
  1. 行 22 | “(待人工回填——详见子节文件史观/辨析字段)” | 史观字段占位待填 | P1 | 回填总纲映射（至少覆盖要点中已引用的第 6、8 条），或删除占位行并显式声明字段挂靠子节
  2. 行 11、13、26、28 | “DragonFly 从 F”“bsd_commits.db drago”“回移停止时间节点”“contribut” | 句子中途截断，内容不完整 | P1 | 补全被截断语句或重写该条目
  3. 行 32、33、35 | “［A］<!-- DB_REF:dragonfly.duckdb -->> **数据库引用…” | 数据库增补块、标题、分隔线塌缩进行内文本，渲染结构失效 | P1 | 将 DB_REF 块、史料考据补充小节、--- 分隔线各自独立成段
  4. 行 11、13、26、28 等 | “bsd_commits.db”“dragonfly.db” | 文件名未按规则加粗 | P2 | 统一加粗为 **bsd_commits.db** 等（不篡改名称）

- 结论：存在问题 4 项（P0 0、P1 3、P2 1、P3 0）
