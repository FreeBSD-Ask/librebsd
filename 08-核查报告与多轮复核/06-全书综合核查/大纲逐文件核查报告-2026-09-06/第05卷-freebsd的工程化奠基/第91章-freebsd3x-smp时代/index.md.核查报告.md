# 核查报告：第05卷-freebsd的工程化奠基/第91章-freebsd3x-smp时代/index.md

- 源文件：d:\librebsd\05-卷册大纲\第05卷-freebsd的工程化奠基\第91章-freebsd3x-smp时代\index.md
- 批次：C214；检查日期：2026-09-11；检查方式：逐文件完整阅读人工核查（无降级）
- SUMMARY.md 收录：未收录（旗标 UNLISTED_NOT_IN_SUMMARY 复验属实：SUMMARY.md 行 779 以“第 91 章 FreeBSD 3.x：SMP 时代”收录概述.md 为章入口，行 780-794 收录 91.1-91.4、91.6-91.13 与媒体反响、采访录两个辅助文件；index.md 本体不在 SUMMARY 任何行）
- A 占位符：发现 4 处（条 1、2、3、13）
- B 内容完整性：发现 6 处（条 2、3、4、5、7、14）
- C 编号与标题：发现 3 处（条 5、10、11）
- D 格式规范：发现 1 处（条 12）
- E 学术规范：发现 3 处（条 6、8、9）
- F SUMMARY 一致性：未收录（index.md 本体未在 SUMMARY；章在案、入口为概述.md；收录标题“第 91 章 FreeBSD 3.x：SMP 时代”与本文件 H1“第 91 章 freebsd3x-smp时代”措辞不同，因收录对象为概述.md，不算本文件标题错误）
- 机械旗标复核：kind=chapterfile 属实（章入口文件）；章号 91 属实（frontmatter chapter=第 91 章、id=CH91、H1、文件名、SUMMARY 路径五处一致）；UNLISTED_NOT_IN_SUMMARY 经实测 SUMMARY.md 复验属实，只读复核未改动任何文件
- 问题清单：
1. P1 | **行 15** | “依赖 Giant Lock 粗粒度锁）〔待核：原文截断，后文待回源〕” | A 占位符＋要点条目截断 | 回源补全该要点第 5 条，删除待核待回源标记
2. P1 | **行 25** | “(待人工回填——详见子节文件史观/辨析字段)” | A 占位符＋史观字段空壳，未映射总纲 | 按五字段规范回填史观并映射至少 5 条总纲
3. P1 | **行 31** | “记录缺口标注 据一手文献印证消解^doubt-resolved-415：此处事实待多源交叉验证” | B 文本损坏（破碎句、句末孤悬一个无配对的全角右方括号、脚注引用错位，且内嵌待验证标记） | 重写为通顺中文，脚注引用与行 49 定义对齐，改用规范的 [存疑脚注] 标注
4. P1 | **行 32** | “ELF 切换对安全基线的具体影响须对照 FreeBS” | B 文本截断（句末戛然而止，FreeBS 疑为 FreeBSD 之截） | 回源补全句尾
5. P1 | **行 49** | “### 史观映射> McKusick 选择 soft updates……## 第 36.14……## 第 36.15……” | B 他章内容错置于文献字段＋C 残留旧章号 36.x（含脚注定义 414/415 与采访录、媒体反响两小节引言） | 删除或改写错置的旧模板残段，更新小节编号；删脚注定义前须先理顺行 31 引用
6. P2 | **行 49** | “FP-2023-006 Implementing NVMe over Fabrics……FP-2002-002 Locking in the Multithreaded FreeBSD Kernel” | E 文献低相关堆砌（16 篇 2002-2023 年 Baldwin/Losh 论文与本章 1998-2000 主题相关性极低，仅 SMPng 一篇直接相关） | 仅保留与本章直接相关者，其余删除
7. P2 | **行 65** | “## 史料考据补充（2026-08-04 任务3 联网核验）> 主题：PXE 引导” | B 格式损坏（条目行内嵌 markdown 标题，考据补充正文缺失截断） | 补全或删除该残块，恢复条目行结构
8. P1 | **行 70** | “Jørgensen. Incremental and Decentralized Integration in FreeBSD [C]. Boston: Springer, 2005: 227-240” | E 文献著录错误（实为 Feller 等编《Perspectives on Free and Open Source Software》，MIT Press，Cambridge MA，2005，页 227-243） | 按实测更正出版者、出版地与页码
9. P2 | **行 12** | “a.out → ELF 迁移、soft updates、Alpha 移植均由工程需求而非学术研究驱动” | E 史实疑点（soft updates 系 Ganger/McKusick 学术研究谱系产物，1998 年被 FreeBSD 采纳；与行 49 拼入段“学术耐心”说自相矛盾） | 修正定性表述或标 [存疑脚注]，并消解与行 49 残段的矛盾
10. P2 | **行 19-21** | “匹配置信度 folder，原因：folder 第89章” | C 数据库匹配疑点（第 91 章的三条 chapter_matches 记录原因字段均指向第 89 章，疑匹配错位或旧章号残留） | 核对 references_fulltext 库 chapter_matches 记录，必要时重建匹配
11. P2 | **行 69** | “2009-2009 年间：34,864 次提交” | C 数据库增补块时段疑点（本章为 1998-2000，该块却统计 2009 单年） | 核对 freebsd.duckdb 增补脚本取数区间
12. P3 | **行 25** | “(待人工回填——详见子节文件史观/辨析字段)” | D 中文语境使用半角括号 | 改全角括号
13. P3 | **行 45** | “FreeBSD 贡献者多样性研究（如有）” | A 轻微占位语（“如有”未定） | 落实文献后删除“（如有）”
14. P3 | **行 12** | “需警惕将 FreeBSD 3.x 叙事为 ‘现代 BSD 起点’ 的回溯性” | B 疑似截断（句意未完，“的回溯性”后疑缺“叙事/倾向”等语） | 回源核对补全
- 结论：存在问题 14 项（P0 0、P1 6、P2 5、P3 3）
- 补充说明（正样本与联网复核留痕，不计入问题清单）：
  1. H1 章号与文件名一致；frontmatter 三字段齐备；五字段形式上齐备（要点 5 条、史料 3 条数据库匹配记录、辨析 5 条、文献 9 组），缺陷集中在实质内容与拼接质量。
  2. 全文未出现“一刻哲学”“构造哲学”等禁用名称；未引用维基百科、百度百科等禁引来源；未出现全角直角引号；pxeboot(8) 手册页引用保持原始格式；行 37 两处文件路径均加粗且 SQL 查询、Python 脚本名以行间代码呈现未篡改。
  3. 联网复核（0 信任原则，2026-09-11，共 4 次检索）：FreeBSD 3.0-RELEASE 于 1998-10-16 发布，为 i386 带来最初 SMP 支持（官方 Release Notes 原文称内核“mostly non-reentrant”，即粗粒度锁）、默认启用 CAM SCSI 子系统、提供 aout-to-elf 迁移目标——与要点行 15、行 12 相符；a.out→ELF 与 Alpha 移植动因链条与 Doug Rabson《Early FreeBSD Ports》（FreeBSD Foundation）回忆文相符（Alpha 移植 1997 年 5 月启动，1998 年初完成 ELF 转换）；Lehey 2001 文献经 USENIX ATC 2001 FREENIX Track 官方页确证（Boston，页 155-164），源文件著录年份无误；Jørgensen 2005 出处经 MIT Press 官方页与 ACM 引文确证为 MIT Press 页 227-243（条 8 依据）；McKusick《Journaled Soft-updates》明言 soft updates 依赖追踪系统 1998 年被 FreeBSD 采纳（条 9 依据）。4.3BSD-Reno（1990 年 6 月）与 Solaris 8（2000 年 2 月 GA）按学界通识核验未见矛盾，未单独联网复核。
  4. 交叉观察（属其他文件核查范围，仅记录）：SUMMARY.md 行 783（91.4）与行 785（91.6）之间无 91.5 条目，疑 91.5 未收录，待 91.5 文件核查时复验；本章目录残留 9 个 .bak_wo002/wo004/wo005/olddb_20260911 修复备份文件（非源文件，未计入核查）；行 37 所引“Core Team 会议纪要”属通常不公开史料，落卷时须给出可核实的获取途径。
  5. 文件内 9 处 <!-- DB_REF:freebsd.duckdb --> 数据库引用块属自动增补豁免范围，未计入问题清单，但其时段疑点已以条 10、11 登记。
