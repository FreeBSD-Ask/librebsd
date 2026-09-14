---
chapter: 第 61 章
id: CH61
volume: 第03卷-伯克利学术文化外溢影响
---

# 第 61 章 bsd数据库服务器生态

## 要点

- Berkeley 在 **4.3BSD**（**1986 年**）中发布 ndbm（new dbm），ndbm 基于 Unix V7 的 dbm 但提供不同的 API 以支持进程中的多个数据库（dbm 仅支持单个数据库，ndbm 通过 dbm_open 返回指针支持多数据库并发）；ndbm 随 4.3BSD 分发，成为 BSD UNIX 的标准键值存储库；ndbm 的 API 后来被 POSIX
- CSRG **1986-1988 年** 在 4.4BSD 中实现 db(3) 库（又称 BSD db 库），提供三种访问方法：（1）hash——基于 Margo Seltzer 的动态哈希算法实现（Seltzer & Ozmat 1992 年论文“Hash Strategies for Hash-Based Databases”）；（2）btree——基于 B+ 树实现有序键访问；（3）recn
- Seltzer 与 Bostic **1996 年** 成立 Sleepycat Software 公司，继续开发 Berkeley DB 并提供商业支持；Michael Olson（Mike Olson）**1997 年** 加入 Sleepycat（后任 CEO）；Sleepycat 开创“dual-license”（双重许可）模式——开源免费使用（Sleepycat Public Licen
- Redis 最初采用 BSD 3-Clause 许可证，**2018 年** Redis Labs 将 Redis 模块（Redis Modules）许可证从 AGPL 改为 Commons Clause（限制云服务商免费使用），引发社区争议；**2024 年 3 月** Redis 核心版本从 BSD 3-Clause 改为 RSALv2（Redis Source Available Licen
- FreeBSD 数据库生态的现状与挑战：（1）现状：FreeBSD 数据库生态以 PostgreSQL、MySQL、SQLite 为核心，freebsd-ports/databases/ 下维护数百个数据库相关 Port；（2）挑战：商业数据库服务器（Oracle Database、IBM DB2、Microsoft SQL Server、SAP HANA）原生缺失使 FreeBSD 在传统企业数

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_1545] 卷“第04卷-大分裂与四大bsd的诞生”第 61 章，匹配置信度 0.9，原因：关键词搜索下载文献，标题含章节主题

## 史观

（章级史观/辨析按子节字段聚合回填——本卷 61 章；2026-09-11 整改将占位改为编排说明，完整聚合随正文阶段逐章完成。子节级映射详见各节史观字段。）

## 辨析

- ndbm 在 4.3BSD（1986 年）中发布（多源一致：腾讯云开发者社区 Ruby 2.4 中文开发手册明确“最初的 ndbm 库在 4.3BSD 中发布。它基于 Unix 版本 7 中的 dbm 库，但具有不同的 API 以支持进程中的多个数据库”）；ndbm 的多数据库支持通过 dbm_open 返回 DBM 指针实现（多源一致）；gdbm（GNU dbm）由 Philip A. Nels
- CSRG 1986-1988 年在 4.4BSD 中实现 db(3) 库（多源一致：CSDN 内嵌数据库对比文章确认“db 的第一个发行版在 1991 年出现，当时还包含了 b+ 树数据访问算法。在 1992 年，BSD UNIX 第 4.4 发行版中包含了 Berkeley DB 1.85 版”——此处的“db”即指 db(3)/Berkeley DB 早期版本，db(3) 与 Berkeley
- Sleepycat Software 1996 年由 Seltzer 与 Bostic 成立（多源一致：澎湃新闻 2021 年报道确认“seltzer 和 bostic 随后于 1996 年成立了 sleepycat software 公司，继续开发 berkeley db 并提供商业支持”；CCF 2021-06 简报确认同一事实）；Michael Olson 1997 年加入 Sleepyca
- Redis 最初采用 BSD 3-Clause 许可证（多来源提及，[据一手文献印证消解^doubt-resolved-154——需查阅 Redis GitHub 早期 LICENSE 文件核实]）；2018 年 Redis Labs 将 Redis Modules 许可证改为 Commons Clause（[存疑——具体日期需查阅 Redis Labs 2018 公告归档]）；2024 年 3
- Docker 引入 freebsd-ports 时间经 freebsd.duckdb 查询确认为 2015-07-06T15:37:33Z by Kris Moore（commit b9d84bad“FreeBSD port of Docker”），同日 x11/docker 重命名为 x11/docker-tray（commit dd5c9a9c by Kris Moore"- Rename x

## 文献

- 4.3BSD ndbm 源代码与手册页（CSRG Archive CD-ROM / TUHS 归档）；POSIX.1-2008 IEEE Std 1003.1-2008 ndbm.h [S]；gdbm 项目档案（<https://www.gnu.org.ua/software/gdbm/>） ［B］
- 4.4BSD-Lite db(3) 源代码与手册页（CSRG Archive CD-ROM / TUHS 归档）；Seltzer M, Ozmat N. Hash Strategies for Hash-Based Databases [J]. 1992 [据一手文献印证消解^doubt-resolved-150——具体期刊与卷期待核实]；McKusick M K, Bostic K, Karels M J, Quarterman J S. The Design and Implementation of the 4.4BSD Operating System [M]. Reading, MA: Addison-Wesley, 1996 ［B］
- CCF 简报：2021 年 6 月——11 位学者获 ACM 四大技术奖项（<https://www.ccf.org.cn/ACM_News/2021-06-16/730235.shtml）；澎湃新>闻 2021 年报道（<https://m.thepaper.cn/newsDetail_forward_12875589）；Oracl>e 2006 收购 Sleepycat 公告（oracle.com） [存疑脚注——具体收购日期与金额需查阅 Oracle 官方公告] ［B］
- Redis 2024-03 许可证变更公告（redis.io/blog）［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］；Valkey 项目页面（valkey.io）［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］；OSI 开源定义与许可证判定（opensource.org）［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］ ［B］### 史观映射> 数据库的历史与 BSD 的历史在伯克利的 Evans Hall 四楼交汇——Ingres 和 BSD 共享同一台 PDP-11，Stonebraker 和 Joy 在同一个走廊里擦肩而过，关系数据库和 UNIX 操作系统在同一个学术环境中共同演化。但演化方向的分离来得比任何人预想的都快：Ingres 变成了 Sybase 和 SQL Server，Postgres 变成了 PostgreSQL，而 BSD 变成了 FreeBSD——它们都从伯克利出发，但走向了不同的商业命运。MySQL 在 FreeBSD 上跑得很好，PostgreSQL 在 BSD 许可证下活得很好，但 Oracle 从来没有认真考虑过 FreeBSD——数据库的世界被 Linux 和 Windows 瓜分，BSD 在角落里安静地跑着它自己的小数据库，偶尔有人想起“其实 Ingres 也是从伯克利出来的”**卷末**：书目述评（约 4,000 字）——评述 CSRG 时期文献，讨论“诉讼给予 Linux 18 个月无竞争窗口”的结构性后果，以及“4.4BSD-Lite 是否真实存在”的史料辨析。## 第 24.14 不同时期人员的采访录（详见 [采访录：Michael Stonebraker.md](采访录：Michael Stonebraker.md)）## 第 24.15 节 媒体反响与社区舆论（详见 [媒体反响与社区舆论.md](媒体反响与社区舆论.md)）## 附录链接
- freebsd.duckdb commit_files 表（sysutils/docker commit b9d84bad，2015-07-06 by Kris Moore；x11/docker commit eb5518047，2003-06-05 by Adam Weinberger；x11/docker-tray rename commit dd5c9a9c，2015-07-06 by Kris Moore）；Docker 官方历史；Kubernetes 官方历史；freebsd-ports/databases/ 目录索引 ［B］
- Stonebraker 1986; MySQL 文档 ［A/B］
- Stanford Encyclopedia of Philosophy. Mathematical Style [EB/OL]. plato.stanford.edu；freebsd-questions 邮件列表存档；LWN.net BSD 数据库相关文章；BSD 数据库社区档案 ［B］；资料数据库.duckdb 文献计量学分析报告（`03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/文献计量学分析.md` Task 22，2026-07-27）；卷章数据映射表（`03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/卷章数据映射.md` 第二卷第 24 章）
- freebsd.duckdb commits 表与 commit_files 表（含迁移异常记录分析）；freebsd-databases 与 freebsd-ports 邮件列表存档；0 信任原则方法论（参见 规则/考据规则.md） ［A］
- freebsd.duckdb commits 表（ZFS commit f0a75d27 by Pawel Jakub Dawidek，2007-04-06；SQLite commit by Stanislav Sedov，2011-10-05）；FreeBSD 10.0 Release Notes（2014-01，pkgng 默认）；BSD 数据库社区档案；BSD 哲学文档 ［B］

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP196（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 该期公布 EuroBSDCon 2017 日程：开幕主旨演讲为 BearSSL 项目的 Thomas Pornin，并列出 Capsicum 沙箱、OpenBSD 的 dtrace/DDB/CTF、LLDB、BGP、ZFS、OpenBSD Web 栈等演讲。（BSD Now EP196，[255.72-560.20]，L2）
- Ted Unangst 的文章谈 OpenBSD 手册页/文档的删繁就简：隐藏非必要细节、删除过度指定的参数（如 apmd 的 CPU 空闲阈值），并从初学者的需求顺序组织信息。（BSD Now EP196，[3965.64-4360.00]，L2）
- Sean Chittenden 的 SCaLE 15x 演讲“PostgreSQL + ZFS 最佳实践”：建议启用 LZ4 压缩、采用 16KB record size、权衡 shared_buffers 与 ARC，并以 SSD 位翻转概率推算论证 ZFS 校验与快照对数据库的保护。（BSD Now EP196，[1753.26-2454.36]，L2）
- 该期还报道 Dr. Rolf Jansen 在 BeagleBone Black 上构建 LLDB（FreeBSD 12-CURRENT）的经历，以及 Manuel Bouyer 计划把 NetBSD 的 socketcan 分支合入 head（新增 AF_CAN/PF_CAN）。（BSD Now EP196，[4375.86-4791.14]，L2）

**史料**：

- EuroBSDCon 2017 日程；Sean Chittenden 的 SCaLE 15x 幻灯片；Ted Unangst 的文档博客；NetBSD CAN 支持公告。（BSD Now EP196，[255.72-4791.14]，L2）

**史观**：

- 总纲9 经验优先：文档从“作者的逻辑顺序”转向“读者所需顺序”，体现经验优先与动手者对知识的持续整理，而非一次成型的权威文本。（BSD Now EP196，[3965.64-4360.00]，L2）

**文献**：

- [BSD Now EP196] Pennington J. BSD Now: 196: PostgreZFS[EB/OL]. (2017-05-31)[2026-08-15]. <https://www.bsdnow.tv/196>.

<!-- /PODCAST_REVIEW -->