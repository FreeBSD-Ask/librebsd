---
chapter: 第 255 章
id: CH255
volume: 第13卷-bsd衍生操作系统
---

# 第 255 章 社区态度与linux对比

## 要点

- 开源社区常以“绩优主义”（meritocracy）作为形式主义意识形态——贡献者地位由其贡献质量决定，而非身份、背景、关系。但实际开源社区中绩优主义的实质内容常受质疑——FreeBSD Core Team 选举虽以贡献为门槛，但参选须由现有 committer 提名，形成“内圈推荐”机制；Linux 内核 maintainer 任命虽以贡献为依据，但任命权在 Linus Torvalds 与上层
- BSD 社区对新人态度存在代际差异——CSRG 一代（McKusick、Karels、Bostic 等）在 1970-90 年代伯克利的学术环境中对研究生新人态度相对开放，通过学徒制吸纳新生代（如 Fabry 招收 Joy、Babaoğlu）；现代 BSD 社区（2000 年后）随着社区老龄化与项目成熟，对新人态度趋于保守——FreeBSD Core Team 选举门槛提高，OpenBSD 由 T
- 开源社区的“开放”与“封闭”张力须避免二元判断——开源社区在许可证上开放（任何人可使用、修改、分发），但在治理上常封闭（核心决策由小团体主导）；在贡献上开放（任何人可提交补丁），但在审查上常封闭（审查权在内圈手中）。这一张力是开源治理的根本问题——完全开放导致决策低效与质量失控，完全封闭导致社区萎缩与代际断层。〔待核：原文截断，后文待回源〕
- Linux 社区长期存在“泥潭”现象——LKML（Linux Kernel Mailing List）文化以 Linus Torvalds 的“直率”风格为标志，Torvalds 多次在 LKML 中公开辱骂开发者（如 2012 年称 NVIDIA 是“我们接触过的最糟糕的公司”，2018 年因 Toxic 行为暂离内核开发并发布道歉声明）。LKML 中的毒性行为包括人身攻击、技术霸凌、对新人冷漠
- Red Hat 对 Linux 的控制呈现逐步深化的过程——1990 年代 Red Hat Linux 是社区发行版之一，2000 年代 Red Hat 拆分为 Fedora（社区）与 RHEL（企业），2010 年代 Red Hat 成为 Linux 内核最大企业贡献者，2019 年 IBM 收购 Red Hat 后 Red Hat 对 Linux 的控制进一步巩固。Red Hat 控制下的 L

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4085] 卷“第13卷-bsd衍生操作系统”第 255 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 外部贡献者补丁审查周期的具体数据须以邮件列表统计为准；“拒绝率高”的判断须有量化数据支持；“天然不信任”的判断须有具体案例支持；各项目具体审查表现归入文化治理批评章，本节不重复
- “开放”与“封闭”的判断须有具体维度支持；用户文章的论断须按 0 信任原则考据
- Torvalds 2018 年道歉声明的具体内容须以原文为准；Sarah Sharp 2015 年离开声明的具体内容须以原文为准；“BSD 社区相对而言毒性行为较少”的判断须有具体比较数据支持
- Red Hat 员工在内核 MAINTAINERS 中的比例须以 MAINTAINERS 文件统计为准；systemd 由 Lennart Poettering 主导的事实须考据；“Linux 内核方向由 Red Hat 商业利益塑造”的判断须有具体案例支持；systemd 的工程架构与 BSD init 的哲学分野详见第 68B 章 systemd 与 BSD init。**双方分歧点**：Li
- Linux CoC 的具体版本（Contributor Covenant 1.4）须考据；FreeBSD CoC 的 LLVM 渊源须考据；OpenBSD 无正式 CoC 的事实须以项目文档为准

## 文献

- BSD 与 Linux 邮件列表；外部贡献者声明；开源贡献者研究文献 ［A］## 254.6.3 社区对新人态度的代际差异：CSRG 一代与现代 BSD 社区
- 开源治理研究文献；BSD/Linux 治理文档；用户文章［考据注：2026-07-28 联网考据留痕，模板句式已按 0 信任原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:bsd_derivatives.duckdb -->
> **数据库引用（bsd_derivatives.duckdb）**：本子节对应 bsd_derivatives 代码仓库。> 1985-2026 年间：963,557 次提交。> 仓库总览：963,557 次提交，9,744 位贡献者（contributors 表行数，1985-06-13 至 2026-08-24）。
- LKML 存档；Torvalds 道歉声明；Linux CoC 文档；Sarah Sharp 声明 ［A］## 254.7.2 红帽（Red Hat）控制下的 Linux：从社区项目到企业主导
- Red Hat 年报；Linux MAINTAINERS 文件；systemd/cgroups/eBPF 档案 ［B］## 254.7.3 Linux 内核 CoC 争议：2018 年的行为准则引入与社区分裂
- Linux CoC 公告与争议存档；Torvalds 道歉声明；FreeBSD CoC 公告；OpenBSD 治理文档 ［A］## 254.7.4 BSD 与 Linux 的 Kernel 治理对比：独裁与共识的工程后果
- Linux/FreeBSD/OpenBSD 对比文档；用户文章［考据注：2026-07-28 联网考据留痕，模板句式已按 0 信任原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:linux_kernel.duckdb -->
> **数据库引用（linux_kernel.duckdb）**：本子节对应 linux_kernel 代码仓库。> 1985-2026 年间：1,474,340 次提交。> 仓库总览：1,474,341 次提交，39,865 位贡献者（contributors 表行数，1970-01-01 至 2026-08-24）。
- LKML 存档；Linux 内核 ABI 文档；stable_api_nonsense.txt ［A］## 254.8.2 FreeBSD 内核 ABI 政策：大版本内稳定，跨大版本不保证
- FreeBSD Release Engineering 文档；FreeBSD 升级指南［考据注：2026-07-28 联网考据留痕，模板句式已按 0 信任原则精简（WO-004）；语义以正文与所引来源为准］## 254.8.3 OpenBSD ABI 政策：每版本可破坏 ABI
- OpenBSD 升级指南；OpenBSD ABI 文档；Theo de Raadt 邮件［考据注：2026-07-28 联网考据留痕，模板句式已按 0 信任原则精简（WO-004）；语义以正文与所引来源为准］## 254.8.4 NetBSD ABI 政策与 DragonFly BSD ABI 政策
- NetBSD ABI 文档；DragonFly BSD 升级指南；HAMMER 迁移文档［考据注：2026-07-28 联网考据留痕，模板句式已按 0 信任原则精简（WO-004）；语义以正文与所引来源为准］## 254.8.5 ABI 稳定问题的史观辨析：用户便利与代码清洁的根本张力
