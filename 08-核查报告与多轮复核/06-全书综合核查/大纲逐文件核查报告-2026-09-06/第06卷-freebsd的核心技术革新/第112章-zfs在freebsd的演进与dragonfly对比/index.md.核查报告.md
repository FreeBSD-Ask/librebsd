# 核查报告：第06卷-freebsd的核心技术革新/第112章-zfs在freebsd的演进与dragonfly对比/index.md

- 源文件：d:\librebsd\05-卷册大纲\第06卷-freebsd的核心技术革新\第112章-zfs在freebsd的演进与dragonfly对比\index.md（355 行，分次完整通读：要点/史料/史观/辨析/文献与 PODCAST 要点区逐行精读）
- 批次：C613；检查日期：2026-09-13；检查方式：逐文件完整阅读人工核查（辅以与 112.10 报告互证及 SUMMARY 实测）
- SUMMARY.md 收录：实测第 1136 行（本章索引条目），批次 UNLISTED 旗标失效
- A 占位符：史观节为 (待人工回填——详见子节文件史观/辨析字段) 显式占位（见清单条目 1）
- B 内容完整性：要点三条齐备（第三条截断）；SECTION_GAP 112.1-112.9 缺号系章级拆分假阳性（磁盘仅存 112.10-112.12 三节与概述）
- C 编号与标题：通过（章索引体例）
- D 格式规范：通过
- E 学术规范：发现 2 处（见清单条目 2/3）
- F SUMMARY 一致性：通过

## 问题清单

1. P3 | 行 21 | 史观节为 (待人工回填) 显式占位——与 97index 同款；章索引的史观综合缺位 | 原文实测 | 回填或改指引
2. P3 | 行 31 | 统计报告路径 01-数据库本体 错挂第 3 例（推断性统计.md/卷章数据映射.md/phase3_inferential_stats.py——C620/97index/136index 同族）＋Hibsd Project 著者名残留 | ls 实测 | 更正路径
3. P3 | 行 12-13 | 要点第二条与第三条句中截断（不适合 DragonFly BSD 的〔断〕/精〔断〕）——章索引要点区截断族；行 25 辨析第一条亦截断（变点归因存疑：1999-08 变点距 2020-01 SVN-to-Git 迁移〔断〕） | 逐行可见 | 回源补全

- 结论：存在问题 3 项（P0 0、P1 0、P2 0、P3 3）

## 补充说明（正样本与复核留痕）

- 要点区三条均为高质量考据的截断残存：Mann-Kendall 统计印证（与 132.10 的 C-03 口径一致）；HAMMER 归因纠正（Dillon 从未将许可证列为不移植 ZFS 的原因——实为 VFS/内存管理架构差异与 ZFS 复杂性的工程选择，纠正 CDDL 流行误传并引 CDDL §3.5 允许聚合的条文依据）；Torvalds 2020-01-06 RealWorldTech 帖子的一手定位（Spectre/Meltdown Fixes 主题下回复）——三条均须回源补全。
- 辨析区的误读纠正清单价值高：误称 Torvalds 说 ZFS 是邪恶的（原话为 buzzword 与 non-starter）、误作 Linux 官方立场（实为个人身份）、忽略 out-of-tree 模块兼容性上下文——三重误读逐条辨正；CDDL §3.5 允许聚合的条文核查纠正 中文技术社区 CDDL 不兼容 误传。
- PODCAST 23 期（BSD Now 2013-2025 全跨度）主题契合：ZFS/Jail/HAMMER/容器生态（EP651 GeoIP PF 表、EP373 Kyle Evans bsdgrep-flua-bectl-certctl 四工具线、EP354 ZFS 复制 8 秒 vs rsync 2.5 小时、EP324 Hammer2 紧急空间模式与 ZFS slop 对照、EP640 RunJ/Buildah/Podman OCI 1.3、EP300 OpenZFS 单一上游切换预告——与 111.8 的 2.0 治理史互证）。
- 文献 23 条著录规范；dangan-20260908 消解回写块（Feature Flags Documentation，DKC-1987→fulltext:6029）无 needs_fix 标记——消解完成态。
- SECTION_GAP 112.1-112.9 系章级拆分假阳性：磁盘实测仅 112.10-112.12 三节加概述（112.1-112.9 内容未建或在别处），与 136index 的真缺口不同——拆分计划说明宜补。
