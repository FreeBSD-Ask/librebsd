---
chapter: 第 255 章
id: CH255
volume: 第13卷-bsd衍生操作系统
---

# 第 255 章 社区态度与 Linux 对比

## 要点

- 开源社区常以“绩优主义”（meritocracy）作为形式主义意识形态——贡献者地位由其贡献质量决定，而非身份、背景、关系。但实际开源社区中绩优主义的实质内容常受质疑——FreeBSD Core Team 选举虽以贡献为门槛，但参选须由现有 committer 提名，形成“内圈推荐”机制；Linux 内核 maintainer 任命虽以贡献为依据，但任命权在 Linus Torvalds 与上层
- BSD 社区对新人态度存在代际差异——CSRG 一代（McKusick、Karels、Bostic 等）在 1970-90 年代伯克利的学术环境中对研究生新人态度相对开放，通过学徒制吸纳新生代（如 Fabry 招收 Joy、Babaoğlu）；现代 BSD 社区（2000 年后）随着社区老龄化与项目成熟，对新人态度趋于保守——FreeBSD Core Team 选举门槛提高，OpenBSD 由 Theo de Raadt 个人主导、无正式 CoC，新人融入依赖 IRC 与邮件列表的直接互动〔2026-09-12 整改：句尾截断收束——批次 C100 问题 1〕
- 开源社区的“开放”与“封闭”张力须避免二元判断——开源社区在许可证上开放（任何人可使用、修改、分发），但在治理上常封闭（核心决策由小团体主导）；在贡献上开放（任何人可提交补丁），但在审查上常封闭（审查权在内圈手中）。这一张力是开源治理的根本问题——完全开放导致决策低效与质量失控，完全封闭导致社区萎缩与代际断层。（2026-09-12 整改：句意已完整，待核标记删除——批次 C100 问题 2）
- Linux 社区长期存在“泥潭”现象——LKML（Linux Kernel Mailing List）文化以 Linus Torvalds 的“直率”风格为标志，Torvalds 多次在 LKML 中公开辱骂开发者（如 2012 年称 NVIDIA 是“我们接触过的最糟糕的公司”，2018 年因 Toxic 行为暂离内核开发并发布道歉声明）。LKML 中的毒性行为包括人身攻击、技术霸凌、对新人冷漠
- Red Hat 对 Linux 的控制呈现逐步深化的过程——1990 年代 Red Hat Linux 是社区发行版之一，2000 年代 Red Hat 拆分为 Fedora（社区）与 RHEL（企业），2010 年代 Red Hat 成为 Linux 内核最大企业贡献者，2019 年 IBM 收购 Red Hat 后 Red Hat 对 Linux 的控制进一步巩固——Red Hat 控制下的 Linux 企业治理格局就此成形〔2026-09-12 整改：句尾截断收束——批次 C100 问题 3〕

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4085] 卷“第13卷-bsd衍生操作系统”第 255 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

总纲第 15 条——文化即形式主义：“绩优主义”作为开源社区的形式主义意识形态，其实质与宣称的落差是文化形式主义的典型样本（据要点 1）；总纲第 3 条——不存在进步，只有权力再分配：Red Hat 从社区发行版到企业主导的深化、Core Team 选举门槛的变化，均是社区权力的再分配而非“社区进化”（据要点 2/5）；总纲第 8 条——本体论上各方平等：BSD 与 Linux 两阵营的治理形态（共识/独裁、CoC 有无）地位平等，毒性行为差异须以数据比较而非立场裁断（据要点 4 与辨析）；总纲第 19 条——解释学循环是历史认识的根本条件：“泥潭”叙事与“绩优”叙事均受叙述者前理解塑造，须回溯原始帖子（据要点 4 与辨析）；总纲第 6 条——和解优于斗争：Torvalds 2018 年道歉与行为准则引入是社区冲突以和解方式处理的节点（据要点 4）。（2026-09-12 整改：史观字段按批次 C100 回填，映射依 25 条权威表）

## 辨析

- 外部贡献者补丁审查周期的具体数据须以邮件列表统计为准；“拒绝率高”的判断须有量化数据支持；“天然不信任”的判断须有具体案例支持；各项目具体审查表现归入文化治理批评章，本节不重复
- “开放”与“封闭”的判断须有具体维度支持；用户文章的论断须按 0 信任原则考据
- Torvalds 2018 年道歉声明的具体内容须以原文为准；Sarah Sharp 2015 年离开声明的具体内容须以原文为准；“BSD 社区相对而言毒性行为较少”的判断须有具体比较数据支持
- Red Hat 员工在内核 MAINTAINERS 中的比例须以 MAINTAINERS 文件统计为准；systemd 由 Lennart Poettering 主导的事实须考据；“Linux 内核方向由 Red Hat 商业利益塑造”的判断须有具体案例支持；systemd 的工程架构与 BSD init 的哲学分野详见第 171 章 systemd 与 BSD init（2026-09-12 整改：原“第 68B 章”字母章号系旧编号，按现行章号更正——批次 C100 问题 6）。**双方分歧点**：Li
- Linux CoC 的具体版本（Contributor Covenant 1.4）须考据；FreeBSD CoC 的 LLVM 渊源须考据；OpenBSD 无正式 CoC 的事实须以项目文档为准

## 文献

> （2026-09-12 整改：原文献区混入的旧章号 254.6.3-254.8.5 子节标题 8 处（含［A］［B］标记粘连）已剥离留痕，对应内容现属 255.6-255.9 节文件（本章自旧第 254 章拆分，255.1-255.5 缺口系拆分编号遗留）——批次 C100 问题 5。）


- BSD 与 Linux 邮件列表；外部贡献者声明；开源贡献者研究文献 ［A］
- 开源治理研究文献；BSD/Linux 治理文档；用户文章［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:bsd_derivatives.duckdb -->
> **数据库引用（bsd_derivatives.duckdb）**：本子节对应 bsd_derivatives 代码仓库。
> 1985-2026 年间：963,557 次提交。
- LKML 存档；Torvalds 道歉声明；Linux CoC 文档；Sarah Sharp 声明 ［A］
- Red Hat 年报；Linux MAINTAINERS 文件；systemd/cgroups/eBPF 档案 ［B］
- Linux CoC 公告与争议存档；Torvalds 道歉声明；FreeBSD CoC 公告；OpenBSD 治理文档 ［A］
- Linux/FreeBSD/OpenBSD 对比文档；用户文章［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:linux_kernel.duckdb -->
> **数据库引用（linux_kernel.duckdb）**：本子节对应 linux_kernel 代码仓库。
> 1991-2026 年间：1,474,340 次提交（口径注 2026-09-12：原“1985-2026”起算与“1,474,340 vs 1,474,341”差一为切片/总览两口径，非矛盾；“1970-01-01”系未解析 epoch 值，Linux 实际始于 1991）。
- LKML 存档；Linux 内核 ABI 文档；stable_api_nonsense.txt ［A］
- FreeBSD Release Engineering 文档；FreeBSD 升级指南［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- OpenBSD 升级指南；OpenBSD ABI 文档；Theo de Raadt 邮件［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- NetBSD ABI 文档；DragonFly BSD 升级指南；HAMMER 迁移文档［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

