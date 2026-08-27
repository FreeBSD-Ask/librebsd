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
