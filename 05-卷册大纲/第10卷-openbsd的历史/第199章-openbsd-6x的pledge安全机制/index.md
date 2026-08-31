---
chapter: 第 199 章
id: CH199
volume: 第10卷-openbsd的历史
---

# 第 199 章 openbsd-6x的pledge安全机制

## 要点

- pledge 的 CVS commit log 与 **pledge(2)** 手册页历次版本是研究 pledge 演进的核心史料；openbsd.db openbsd-src 仓库中 pledge 相关 commit 自 2015-10-09 起（deraadt"Rename tame() to pledge()"），后续 semarie、benno、millert 等 committer 持续
- LibreSSL fork 的辩证合图——fork 既是 OpenBSD 对 OpenSSL 工程失败的必要回应（反批评层）也是 TLS 库碎片化的加剧因素（批评层与再批评层），二者并非非此即彼；LibreSSL 在 OpenBSD 生态内具有工程合理性（代码精简、攻击面缩减、ISC 许可证纯洁性、年均低 CVE 频率），但在全球 TLS 生态内具有外部性（碎片化、API 不兼容、维护成本由生态承
- pledge/unveil 设计争议的项目统摄史观审视须从总纲三条切入——其一，总纲第 13 条“法律与道德是利益分配”映射：pledge/unveil 的“简洁正确性”叙事不仅是技术论证也是 OpenBSD 项目身份建构的政治产物，社区对 pledge 的辩护中混合了技术判断（粗粒度降低配置错误）与道德判断（“正确使用简单机制优于错误使用复杂机制”），后者本质是将 OpenBSD 工程哲学包装为

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3898] 卷“第10卷-openbsd的历史”第 199 章，匹配置信度 folder，原因：folder 第197章
- [DB:references_fulltext:chapter_matches:chmatch_4014] 卷“第10卷-openbsd的历史”第 199 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:bsdnow_podcast:outline_mappings:om_11196] BSD Now 第 565 期，匹配 CH199 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11238] BSD Now 第 561 期，匹配 CH199 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11308] BSD Now 第 553 期，匹配 CH199 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11387] BSD Now 第 543 期，匹配 CH199 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11396] BSD Now 第 542 期，匹配 CH199 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11415] BSD Now 第 539 期，匹配 CH199 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11432] BSD Now 第 537 期，匹配 CH199 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11462] BSD Now 第 534 期，匹配 CH199 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11471] BSD Now 第 533 期，匹配 CH199 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11540] BSD Now 第 526 期，匹配 CH199 章，关联度 1.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- pledge 演进的具体里程碑以 Release Notes 与 commit log 交叉验证为准——Release Notes 记录用户可见的 pledge 覆盖扩展，commit log 记录具体代码变更；commit log 中的 pledge 相关 commit 以 file_path 含"pledge"或 message_subject 含"pledge"为筛选条件，bsd_commi
- 合图不寻求消除张力而寻求呈现张力——LibreSSL 的“自主”与“孤立”是同一决策的共生效应，不可分割；【0 信任原则·合图的非终结性】合图并非辩证链的终结而是阶段性综合，随 LibreSSL 与 OpenSSL 演进（如 OpenSSL 3.0 与 LibreSSL 的进一步分化）须重新展开；【0 信任原则·合图的非折中主义】合图不是“LibreSSL 在 OpenBSD 内合理、在生态外不合
- 哲学审视的合理性须以三个层面交叉验证——【0 信任原则·道德包装论证的辨析】“pledge 辩护混合技术判断与道德判断”论证须对照 misc@ 邮件列表原文核实——若辩护文本仅含技术论证（如“粗粒度降低配置错误率”），不得人为添加道德判断成分，须以具体文本为据；【0 信任原则·权力-知识共谋的可证伪性】“pledge 被塑造为正确方向、seccomp 被叙述为包袱”论证须对照 OpenBSD 官方

## 文献

- bsd_commits.db openbsd-src 仓库 pledge 相关 commit；OpenBSD **pledge(2)** 手册页 [EB/OL]. <https://man.openbsd.org/pledge.2>；OpenBSD Release Notes [EB/OL]. <https://www.openbsd.org/plus.html>；bsd_commits.db 查询 L1.1.1 与 L1.1.2（来源：原材料/研究/bsd 仓库分析/数据分析/宏观趋势统计.md §L1.1.1、§L1.1.2）；bsd_commits.db 查询 L2.3.1.pledge 与 L2.3.1.unveil（来源：原材料/研究/bsd 仓库分析/数据分析/中观模式挖掘.md §L2.3.1，数据缺口）；统计分析报告：时间序列分析.md Task 14 [R/OL]. 2026-07-27. 文件路径：`c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\统计分析\时间序列分析.md`；Python 统计脚本：`script/phase4_time_series.py`. Task 14 ARIMA 建模 + Task 15 MAPE/RMSE 预测精度。执行日期：2026-07-27 ［A］<!-- DB_REF:openbsd.duckdb -->> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 2015-2016 年间：41,347 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
- LibreSSL 与 OpenSSL 综合对比研究；TLS 库生态演进史；openbsd.db openbsd-src 仓库 LibreSSL/OpenSSL CVE commit 对比 ［A］<!-- DB_REF:openbsd.duckdb -->> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 2014-2014 年间：20,651 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
- 项目史观总纲第 13、19、21 条原文；de Raadt 邮件列表发言 [EB/OL]. <https://marc.info/?laccopenbsd-misc>；OpenBSD **pledge(2)** 手册页 [EB/OL]. <https://man.openbsd.org/pledge.2>；Linux seccomp-bpf 文档 [EB/OL]. <https://www.kernel.org/doc/html/latest/userspace-api/seccomp_filter.html>；Linux landlock 文档 [EB/OL]. <https://docs.kernel.org/userspace-api/landlock.html>；bsd_commits.db openbsd-src 仓库 pledge 覆盖扩展 commit ［A］<!-- DB_REF:openbsd.duckdb -->> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 2018-2018 年间：16,734 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP498（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Florian Obser 阐述 OpenBSD 三类利用缓解：降权、权限分离与受限服务操作模式，作为攻击者达成任意代码执行后的最后防线；降权是最弱但最古老的缓解，权限分离将不可信数据解析移入低权限进程，受限模式则以 pledge 限制进程能力。（BSD Now EP498，[514.74-603.96]，L2）
- Obser 回溯 ping 降权的历史：Theo de Raadt 逾 26 年前重构 ping，使其先打开原始套接字再丢弃 root 权限，以防本地用户借 ping 缺陷提权；二十年后又发现以 root 调用 ping 时只是从 root 降到 root，遂改为降级到专用用户。（BSD Now EP498，[598.70-632.26]，L2）
- Obser 叙述 pledge 的由来：systrace 由 Niels Provos 开发但因基于系统调用参数而难用，OpenBSD 基础系统中长期仅 sshd 使用；2015 年 Theo 诱使 Nicholas Marriott 用 systrace 沙箱 file 却只坚持半年，成为压垮性体验，Theo 遂开发 tame（后改名 pledge）。（BSD Now EP498，[784.74-861.42]，L2）
- pledge 通过对 OpenBSD 基础程序的需求归类而成，程序违规即被内核以不可捕获的 SIGABRT 终止；当约 50 个程序加入 pledge 后被认为成熟并合入主线，半年内几乎所有基础程序均使用 pledge。（BSD Now EP498，[861.42-931.54]，L2）
- 其余新闻包括 OPNsense 23.1.1 发布、Ansible Clone 工具、NetBSD 在 FOSDEM 2023 的 BSD dev room 报告、FreeBSD Foundation 的 BSDCan 旅行资助，以及 Game of Trees 0.81 与 x-only PKU、pinsyscall 等 OpenBSD 新进展。（BSD Now EP498，[1156.64-2330.00]，L2）

**史料**：

- Florian Obser《Privilege drop, privilege separation and restricted service operating mode in OpenBSD》（sha256.net 博客），为 OpenBSD 开发者本人的一手技术文章，经节目转述。（BSD Now EP498，[508.82-1144.64]，L1）
- OpenBSD tech 邮件列表中 Theo de Raadt 关于 pinsyscall 的帖子，涉及 ExecVE 与 ROP pivot，为当事人一手陈述，经节目转述。（BSD Now EP498，[2272.22-2304.38]，L1）
- Game of Trees 0.81 发布与 Stefan Sperling 在 FOSDEM 2023 的演讲及幻灯片，为官方发布线索，经节目转述。（BSD Now EP498，[1823.68-1923.94]，L2）

**史观**：

- 总纲10 动手者创造历史：安全机制由开发者逐个程序地审计与归类累积而成，而非一次性顶层设计。：Theo 与 Obser 等通过逐个程序的重构与需求归类塑造 OpenBSD 安全机制。（BSD Now EP498，[861.42-931.54]，L2）
- 总纲9 经验优先：以基础系统中真实程序的可用性经验为标准，淘汰难以使用的 systrace。：systrace 因难用而被 pledge 取代，设计取舍来自真实程序的实践经验。（BSD Now EP498，[784.74-861.42]，L2）
- 总纲5 没有必然性，只有偶然性：pledge 的诞生由 systrace 实践中的偶然挫败触发，而非预先规划。：file 沙箱半年即弃的偶然失败促成 tame 与 pledge 的诞生。（BSD Now EP498，[784.74-861.42]，L2）

**辨析**：

- Obser 所述 Theo 逾 26 年前重构 ping 的具体年份需与 OpenBSD 提交史核验，节目转述未给出提交编号。　[存疑脚注] ping 重构年份为口述概数，须以 OpenBSD 提交记录与变更日志核验。（BSD Now EP498，[598.70-632.26]，L4）
- pledge 从 tame 更名的具体时间与 5.8、5.9 版本对应关系为概略叙述，需以 OpenBSD 发布说明与 man 页核验。　[存疑脚注] tame 更名 pledge 及对应版本为概略叙述，需以 pledge(2) 手册与发布说明确认。（BSD Now EP498，[861.42-931.54]，L4）

**文献**：

- [BSD Now EP498] Pennington J. BSD Now: 498: Dropping Privileges[EB/OL]. (2023-03-16)[2026-08-15]. https://www.bsdnow.tv/498.

<!-- /PODCAST_REVIEW -->
