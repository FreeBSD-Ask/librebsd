---
chapter: 第 246 章
id: CH246
volume: 第12卷-macos的bsd遗产
---

# 第 246 章 snowleopard的libdispatch史观审视

## 要点

- 项目史观总纲第 5 条“没有必然性，只有偶然性”为审视 libdispatch 流动史提供了根本框架。libdispatch 在 2009 年 9 月 10 日以 Apache 2.0 开源是多重偶然因素的交汇：Snow Leopard 的“无新功能、重工程质量”定位（为 GCD 工程投入创造了空间）、2009 年 Apple 与 Microsoft 在桌面 OS 市场的竞争压力（GCD 作为差异化竞争点）、Apple 与 FSF 在 APSL 历史争议后的关系修复需求（Apache 2.0 选择是对 FSF 的让步）、Stanislav Sedov 个人对并发抽象的兴趣（其 2009-09-23T15:02:29Z 的 FreeBSD 移植非 Apple 主动委托）——freebsd-src 仓库 `libdispatch` 关键词 0 条 commit，实际移植位于 freebsd-ports 仓库，libdispatch 未进入 FreeBSD 内核主线是偶然因素交汇的结果，非“历史必然”（详见 246.1.1）
- 项目史观总纲第 8 条“本体论上各方平等”为审视 libdispatch 流动史提供了去中心化视角。freebsd.duckdb 显示 2009-2015 年间 Apple、FreeBSD、Linux 三方在并发抽象上的关系不是“先进-落后”的等级关系，而是各自独立演化的本体论平等主体：Apple 的 GCD+libdispatch（任务队列抽象）、FreeBSD 的 pthread+kqueue/kevent（事件驱动）、Linux 的 NPTL+epoll——libdispatch 流向 FreeBSD 是对等交往而非等级臣服（详见 246.1.2）
- 项目史观总纲第 11 条“商品是形式主义”与第 19 条“解释学循环是历史认识的根本条件”为审视 libdispatch 流动史提供了双重透镜。形式主义层面：同一份 libdispatch 代码在 FreeBSD ports 树中被重组为 FreeBSD 用户空间工具，其“商品形式”（可移植的并发抽象 API）被剥离原有 Mac OS X 语境而保留功能形式；解释学循环层面：Apple、FreeBSD、Linux 与第三方观察者四方视角的循环对话构成 libdispatch 流动史的完整认识（详见 246.1.3）
- Mac OS X 10.6 Snow Leopard 时代（2009-2011）正值 BSD 社区对 Apple 使用 FreeBSD 代码但不回馈的批评集中爆发期。批判方以 FreeBSD 内核开发者 **John Baldwin（约翰·鲍德温）** 与 **Marshall Kirk McKusick（马歇尔·柯克·麦库西克）**（4.3BSD 与 4.4BSD 开发者，深度参与 FreeBSD）的公开访谈为主要论据，指出 Apple 长期从 FreeBSD 用户空间吸收代码而仅以 APSL 2.0 选择性发布 Darwin 源代码（详见 246.2.1）
- BSD 阵营与 Apple 工程师对“无薪员工”批判提出反驳，论证分三支。其一，许可证契约层面——BSD 许可证条款明确允许商业使用、修改、再发布而无强制回馈义务，**Marshall Kirk McKusick** 的公开表述“BSD 许可证就是一个复制中心，可以为所欲为，但我们不在乎”即此反驳的典型；其二，Apple 的实质性回馈——Darwin 源码公开与 libdispatch 以 Apache 2.0 开源；其三，Apple 聘用 Jordan Hubbard（2001 年）构成 BSD 与 Apple 的人才流动（详见 246.2.2）

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4058] 卷“第12卷-macos的bsd遗产”第 246 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_4060] 卷“第12卷-macos的bsd遗产”第 246 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_4069] 卷“第12卷-macos的bsd遗产”第 246 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

本章史观以 libdispatch 流动史与 Apple 使用 FreeBSD 代码但不回馈争议为双主题，依 246.1-246.3 三节史观字段汇总：总纲第 5 条（没有必然性，只有偶然性）——libdispatch 以 Apache 2.0 开源与 Sedov 2009-09-23 的 FreeBSD 移植是多重偶然因素的交汇，非历史必然；总纲第 8 条（本体论上各方平等）与第 6 条（和解优于斗争）——Apple、FreeBSD、Linux 等方在并发抽象上是对等交往的平等主体，非等级臣服；总纲第 11 条（商品是形式主义）与第 19 条（解释学循环是历史认识的根本条件）——libdispatch 代码流动呈“商品形式主义”，其历史认识须经四方视角的解释学循环，freebsd.duckdb 一手数据用于还原被二手叙事遮蔽的 Sedov 首条移植贡献；总纲第 13 条（法律与道德是利益分配）——“无薪员工”争议的实质是 BSD 许可证契约下利益分配的结构性失衡，而非 Apple 道德指控；总纲第 21 条（革命与改革是历史方法论的分歧）——GPL 革命式与 BSD 改革式方法论在 Apple 案例中显现为对结构性不对称的不同处理方式（详见 246.1-246.3 各节史观与辨析字段）。

## 辨析

- 偶然性审视须避免滑向“虚无主义”——承认偶然性不等于否认 Apple 开源决策的工程合理性，GCD 在 2009 年的并发抽象领先性是客观事实，但这一领先性是具体语境下的领先性而非超越语境的“必然正确”；“偶然因素四”（Sedov 的个人兴趣）须辨析其性质——Sedov 作为 FreeBSD committer 的个人选择既是偶然的（取决于个人兴趣）又是结构性的（取决于 FreeBSD 的社区共建
- 本体论平等审视须避免滑向“相对主义”——承认四方本体论平等不等于否认工程差距（GCD 在 2009 年的任务队列抽象领先性是客观事实），但工程差距不构成本体论等级；“主体性”概念须辨析——FreeBSD 选择移植 libdispatch 是其主体性的显现（自主选择）而非主体性的丧失（被迫接受），关键在于选择过程的自主性；Apache 2.0 许可证在此本体论平等中扮演关键角色——其与 BSD 兼容
- 形式主义审视须避免滑向“代码虚无主义”——承认 libdispatch 代码的“商品形式主义”不等于否认其技术实质（并发抽象功能是真实的），但须辨析“功能形式”与“语境实质”的分离；解释学循环审视须避免滑向“视角相对主义”——承认多视角循环不等于否认事实客观性（freebsd.duckdb 数据是客观记录），但须辨析“事实”与“解释”的层次差异；“商品”概念在代码语境中须作广义理解——代码作为“商品”并非
- “无薪员工”叙事须避免滑向“Apple 道德指控”——Apple 的行为在 BSD 许可证框架内是合法的，批判指向结构性不对称而非个人或组织的道德缺陷；John Baldwin 2021 年访谈对 2009-2011 年的回溯性适用须辨析——访谈原文未明确指向 Snow Leopard 时代，本节采“回溯性判断”用法而非“同时代判断”；Apple UNIX 03 版税与 FreeBSD 项目的关系
- “BSD 许可证允许此模式”的反驳须避免滑向“许可证契约即正义”——承认法律层面的合法性不等于否认结构性不对称的存在；Apple 的“实质性回馈”须辨析其性质——Darwin 源码公开是 APSL 2.0 强制要求（Darwin 在 APSL 2.0 下发布即承诺开源），libdispatch 的 Apache 2.0 开源是 Apple 主动选择（Apache 2.0 选择性开源而非强制）；FS

## 文献

- Apple Inc. Mac OS X 10.6 Snow Leopard Release Notes [EB/OL]. (2009-08-28). Apple Developer；freebsd.duckdb freebsd-src 仓库 commits 表（libdispatch 关键词 0 条，GCD/Grand Central 关键词 24 条均非 GCD 本体）[DB/OL]. script/query_ch113_libdispatch_commits.py, 2026-07-23；freebsd.duckdb freebsd-ports 仓库 commits 表（libdispatch 13 条，首条 2009-09-23 Sedov commit_hash `fdd841f9197f1910059414771324205d30d93a2a`）[DB/OL]. script/query_ch113_libdispatch_commits.py, 2026-07-23；freebsd.duckdb freebsd-ports 仓库 von Appen 972 commits 中 0 条 libdispatch 相关 [DB/OL]. script/query_ch113_von_appen_libdispatch.py, 2026-07-23；FreeBSD Ports. devel/libdispatch [EB/OL]. <https://www.freshports.org/devel/libdispatch/>；Apple Inc. Swift Open Source [EB/OL]. (2015-12-03). <https://www.swift.org/>；02-sacred源材料/sacred_sources.duckdb（第 25 章）（总纲第 5 条、第 1 条与第 19 条）
## 246.1.2 总纲第 8 条映射——libdispatch 流动中的本体论平等审视
- freebsd.duckdb freebsd-src 仓库 commits 表（pthread/kqueue/epoll 关键词统计）；Apple Inc. libdispatch Source Code [EB/OL]. (2009-09-10). <https://github.com/apple/swift-corelibs-libdispatch>；Linux Kernel Archives. Linux 2.6.30 Release Notes [EB/OL]. (2009-06-09). <https://www.kernel.org/>；Microsoft. .NET 4.0 TPL Documentation [EB/OL]. (2010). Microsoft Developer Network；02-sacred源材料/sacred_sources.duckdb（第 25 章）（总纲第 8 条与第 6 条）
## 246.1.3 总纲第 11 条与第 19 条映射——libdispatch 作为商品形式主义与解释学循环
- freebsd.duckdb freebsd-src 仓库 commits 表（libdispatch 关键词 0 条，GCD/Grand Central 关键词 24 条均非 GCD 本体）[DB/OL]. script/query_ch113_libdispatch_commits.py, 2026-07-23；freebsd.duckdb freebsd-ports 仓库 commits 表（libdispatch 13 条，首条 2009-09-23 Sedov commit_hash `fdd841f9197f1910059414771324205d30d93a2a`）[DB/OL]. script/query_ch113_libdispatch_commits.py, 2026-07-23；freebsd.duckdb freebsd-ports 仓库 von Appen 972 commits 中 0 条 libdispatch 相关 [DB/OL]. script/query_ch113_von_appen_libdispatch.py, 2026-07-23；Apple Inc. libdispatch Source Code [EB/OL]. (2009-09-10). <https://github.com/apple/swift-corelibs-libdispatch>；FreeBSD Ports. devel/libdispatch [EB/OL]. <https://www.freshports.org/devel/libdispatch/>；FreeBSD 邮件列表档案 [EB/OL]. <https://lists.freebsd.org/>；Linux kernel 邮件列表档案 [EB/OL]. <https://lkml.org/>；02-sacred源材料/sacred_sources.duckdb（第 25 章）（总纲第 11 条、第 19 条与第 25 条）

<!-- DB_REF:darwin.duckdb -->
> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。> 1985-2026 年间：2,012 次提交。> 仓库总览：2,016 次提交，42 个 Apple 开源镜像仓库（contributors 表 43 行），2001-04-10 至 2026-04-13。
- freebsd.duckdb freebsd-src 仓库 commits 表（2009-2011 年 `@apple.com` 域名 commit 数量统计）[DB/OL]. script/query_ch113_apple_freebsd_commits.py, 2026-07-24；Apple Inc. Mac OS X 10.6 Snow Leopard Release Notes [EB/OL]. (2009-08-28). Apple Developer；Apple Inc. Darwin Source Releases [EB/OL]. opensource.apple.com（xnu-1504 系列）；开源中国。FreeBSD 大败局 [EB/OL]. 2023（John Baldwin 与 McKusick 访谈引述）；The Open Group. UNIX 03 Program [EB/OL]. <https://www.opengroup.org/certification/unix>；FreeBSD Foundation. FreeBSD Project and Apple Inc.[EB/OL]. <https://www.freebsdfoundation.org/>
## 246.2.2 反批评层——BSD 许可证允许此模式与 Apple 的实质性回馈
- Apple Inc. Apple Releases Darwin 1.0 Open Source [EB/OL]. (2000-04-05). <https://www.apple.com/newsroom/2000/04/05apple-releases-darwin-1-0-open-source/>；Apple Inc. Darwin Source Releases [EB/OL]. opensource.apple.com（xnu-1504 系列）；Free Software Foundation. FSF's Opinion of the APSL 2.0 [EB/OL]. <https://www.gnu.org/philosophy/apsl.html>；开源中国. FreeBSD 大败局 [EB/OL]. 2023（Hubbard、McKusick、Baldwin 访谈引述）；Jordan Hubbard. Resignation from FreeBSD Core Team [EB/OL]. (2001). FreeBSD 邮件列表档案；freebsd.duckdb freebsd-src 仓库 Hubbard 在 2001 年后 commit 记录 [DB/OL]. script/query_ch113_hubbard_apple_commits.py, 2026-07-24
## 246.2.3 再回应层——结构性不对称未消解与许可证哲学的张力
- Free Software Foundation. FSF's Opinion of the APSL 2.0 [EB/OL]. <https://www.gnu.org/philosophy/apsl.html>；Jordan Hubbard. Resignation from FreeBSD Core Team [EB/OL]. (2001). FreeBSD 邮件列表档案；freebsd.duckdb freebsd-src 仓库 Hubbard 在 2001 年后 commit 记录 [DB/OL]. script/query_ch113_hubbard_apple_commits.py, 2026-07-24；开源中国。FreeBSD 大败局 [EB/OL]. 2023（Hubbard 辞职信引述）；Apple Inc. Darwin Source Releases [EB/OL]. opensource.apple.com（xnu-1504 系列 APSL 2.0）
## 246.2.4 合图层——许可证哲学与商业模式的不可调和性及阶段性妥协
- 02-sacred源材料/sacred_sources.duckdb（第 24 章）（24.2 节“劣币驱逐良币”）；02-sacred源材料/sacred_sources.duckdb（第 25 章）（总纲第 13 条）；Free Software Foundation. FSF's Opinion of the APSL 2.0 [EB/OL]. <https://www.gnu.org/philosophy/apsl.html>；freebsd.duckdb freebsd-src 仓库 commits 表（2009-2011 年 `@apple.com` 域名 commit 数量统计）[DB/OL]. script/query_ch113_apple_freebsd_commits.py, 2026-07-24；freebsd.duckdb freebsd-ports 仓库 commits 表（libdispatch 13 条，首条 2009-09-23 Sedov commit_hash `fdd841f9197f1910059414771324205d30d93a2a`）[DB/OL]. script/query_ch113_libdispatch_commits.py, 2026-07-23；Apple Inc. Darwin Source Releases [EB/OL]. opensource.apple.com（xnu-1504 系列）；Apple Inc. libdispatch Source Code [EB/OL]. (2009-09-10). <https://github.com/apple/swift-corelibs-libdispatch> ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2009-2011 年间：102,147 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数），1993-06-12 至 2026-08-25。
- 原材料/哲学/项目统摄史观/第 25 章.md（总纲第 13 条）；原材料/哲学/项目统摄史观/第 24 章.md（24.2 节“劣币驱逐良币”）；开源中国。FreeBSD 大败局 [EB/OL]. 2023（McKusick 与 Baldwin 访谈引述）；freebsd.duckdb freebsd-src 仓库 commits 表（2009-2011 年 `@apple.com` 域名 commit 数量统计）[DB/OL]. script/query_ch113_apple_freebsd_commits.py, 2026-07-24；freebsd.duckdb freebsd-ports 仓库 commits 表（libdispatch 13 条，首条 2009-09-23 Sedov commit_hash `fdd841f9197f1910059414771324205d30d93a2a`）[DB/OL]. script/query_ch113_libdispatch_commits.py, 2026-07-23
## 246.3.2 总纲第 19 条映射——解释学循环与权力知识共谋在 Apple-FreeBSD 争议中的显现
- 02-sacred源材料/sacred_sources.duckdb（第 25 章）（总纲第 19 条）；02-sacred源材料/sacred_sources.duckdb（第 19 章）（19.3 节“权力与知识的共谋”）；Apple Inc. Darwin Source Releases [EB/OL]. opensource.apple.com（xnu-1504 系列）；Apple Inc. libdispatch Source Code [EB/OL]. (2009-09-10). <https://github.com/apple/swift-corelibs-libdispatch>；Free Software Foundation. FSF's Opinion of the APSL 2.0 [EB/OL]. <https://www.gnu.org/philosophy/apsl.html>；开源中国. FreeBSD 大败局 [EB/OL]. 2023；freebsd.duckdb freebsd-src 仓库 commits 表（2009-2011 年 `@apple.com` 域名 commit 数量统计）[DB/OL]. script/query_ch113_apple_freebsd_commits.py, 2026-07-24
## 246.3.3 总纲第 21 条映射——革命与改革方法论在 BSD-GPL 许可证分歧中的显现
- 02-sacred源材料/sacred_sources.duckdb（第 25 章）（总纲第 21 条）；02-sacred源材料/sacred_sources.duckdb（第 21 章）（21.1 节“革命与改革的分歧”、21.2 节“破山中贼易，破心中贼难”）；02-sacred源材料/sacred_sources.duckdb（第 24 章）（24.2 节“劣币驱逐良币”）；开源中国。FreeBSD 大败局 [EB/OL]. 2023（Linus Torvalds 关于 BSD 许可证表述引述）；freebsd.duckdb freebsd-src 仓库 commits 表（2009-2011 年 `@apple.com` 域名 commit 数量统计）[DB/OL]. script/query_ch113_apple_freebsd_commits.py, 2026-07-24 ［A］FreeBSD 社区论文：[FP-2008-003] Mac OS X - From the server room to your pocket（Jordan K. Hubbard（乔丹·哈伯德），2008）<https://papers.freebsd.org/2008/lisa08/hubbard-macosx_from_the_server_room_to_your_pocket/>

<!-- DB_REF:darwin.duckdb -->
> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。> 2009-2011 年间：229 次提交。> 仓库总览：2,016 次提交，42 个 Apple 开源镜像仓库（contributors 表 43 行），2001-04-10 至 2026-04-13。
