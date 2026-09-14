---
chapter: 第 179 章
id: CH179
volume: 第09卷-netbsd的历史
---

# 第 179 章 netbsd-5.0架构重构与社区演进

## 要点

- NetBSD 5.0（**2009.4.29**）引入由 Andrew Doran（安德鲁·多兰） 设计的新 SMP 调度器，采用每 CPU 运行队列与工作窃取算法，取代 4.x 的全局锁机制；新调度器支持多核负载均衡与优先级继承，使 NetBSD 在 4 核至 32 核机器上获得显著性能提升
- NetBSD 5.0 的架构设计文档散布于 tech-kern 邮件列表、CVS commit 信息与 NetBSD Foundation 年度报告；Andrew Doran、YAMAMOTO Takashi、Joerg Sonnenberger 等开发者的设计帖是核心一手史料；源码考据需对照 CVS 历史与 commit log 的署名、时间戳
- pkgsrc commit 记录是研究 2005-2009 年 pkgsrc 演进的核心一手史料；Joerg Sonnenberger 作为 pkgsrc 长期维护者提交数千次 commit；季度发布说明（pkgsrc-2008Q1 等）记录每季度的软件包数量增长与重要变更
- NetBSD Foundation 2005-2009 年度报告记录了 Foundation 治理、资金收支、项目进展与 committer 变更；编程之夏导师分配、学生项目列表、最终评估是编程之夏史料核心；两类文档需对照原始 PDF 与邮件列表通知核验
- NetBSD Core Team 决议记录是研究 2005-2009 年社区治理的核心史料；core 邮件列表存档（部分公开，部分私密）；Core Team 决议涉及新 committer 加入、自动退休、技术路线争议等；考据需对照 core 邮件列表与公开宣布

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4086] 卷“第09卷-netbsd的历史”第 179 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充
- [DB:references_fulltext:chapter_matches:chmatch_4087] 卷“第09卷-netbsd的历史”第 179 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- Doran 新调度器与 FreeBSD Jeff Roberson 的 ULE 2.0（2007.5 引入 FreeBSD 7.0）的关系存在叙事分歧——Doran 在邮件列表中提及参考 ULE 但强调独立性，需对照源码 diff 核验；新调度器的性能基准数据在第三方测试中差异较大，需查 Phoronix/BSD Insights 等早期基准。经 netbsd.duckdb netbsd-src 仓库 b
- CVS 与后续 Git 迁移过程中的元数据保真度问题——部分早期 commit 在迁移后丢失 author 字段；邮件列表存档在 mail-index.netbsd.org 与 MaraRepos 等多镜像中存在版本差异
- pkgsrc 软件包数量统计在不同来源中差异较大——2005Q1 与 2009Q4 的具体数字需对照原始 release tarball 核验；Sonnenberger 的 commit 量在统计工具中可能被低估（部分 commit 以 typos 或 docs 形式提交）
- NetBSD Foundation 2005-2009 年度报告的连续性存在缺口——部分年份的报告未公开发布，需对照邮件列表年度总结补全；编程之夏 2005 年首届的学生项目记录在 Google 官方档案中部分缺失
- Core Team 决议的私密性使考据困难——部分决议未公开宣布，需对照 CVS commit 的 author 变化推断；Core Team 成员名单在不同来源中可能略有出入

## 文献

- NetBSD CVS 仓库归档；mail-index.netbsd.org；NetBSD Foundation 年度报告 2008/2009 ［B］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2009-2009 年间：93,511 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- pkgsrc CVS 仓库；pkgsrc 季度发布说明；tech-pkg 邮件列表年度总结 ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2005-2009 年间：468,780 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- NetBSD Foundation 年度报告 2005-2009；Google 编程之夏 官方档案；NetBSD Foundation 邮件列表 ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2005-2009 年间：468,780 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- NetBSD core 邮件列表；Core Team 决议记录；NetBSD Foundation 年度报告 ［A］## 史料考据补充（2026-08-04 任务3 联网核验）> 主题：NetBSD Core Team 与 committer
- Linux Weekly News 档案；Slashdot BSD 相关帖；OSNews NetBSD 评论［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- NetBSD CVS 仓库统计；邮件列表存档；BSDCan 演讲视频档案 ［A］## 史料考据补充（2026-08-04 任务3 联网核验）> 主题：NetBSD 发布工程（Manuel Bouyer 等）
- NetBSD 5.0 Release Notes；Kengo NAKAHARA MPLS 设计邮件；BSD MPLS 实现比较研究［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- Netcraft Web Server Survey 2005-2009；IDC 服务器操作系统市场报告；Distrowatch 统计页面［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2005-2009 年间：183,657 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- netbsd.duckdb netbsd-src 仓库 commits 表；CVE-2011-0014、CVE-2011-0539 NVD 条目 ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP210（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 该期报道 NetBSD 微内核式重实现的进展：底层是仅约 1.3 万行代码的微内核，只处理中断、消息传递、低级调度与硬件细节；内存管理、文件系统、分页交换与设备驱动几乎全部作为用户态进程运行，并受 MMU 保护，被认为是一个可能真正可用的微内核。（BSD Now EP210，[136.60-353.82]，L2）
- 关于 Mac 快速联网的分析指出，Mac 通过记住已知网络、假设旧 IP 仍有效并先自行配置再后台完成 DHCP 握手，可在链路建立后约 10 毫秒开始联网，远快于依赖用户态 DHCP 客户端的 Android 设备。（BSD Now EP210，[379.94-963.36]，L2）

**史观**：

- 总纲4 分离聚合是永恒规律：NetBSD 微内核重实现把整块内核拆分为用户态进程并经由消息传递聚合，是分离与聚合在操作系统架构层面的体现。（BSD Now EP210，[136.60-353.82]，L2）

**文献**：

- [BSD Now EP210] Pennington J. BSD Now: 210: Your questions, part I[EB/OL]. (2017-09-06)[2026-08-15]. <https://www.bsdnow.tv/210>.

<!-- /PODCAST_REVIEW -->
