---
chapter: 第 243 章
id: CH243
volume: 第12卷-macos的bsd遗产
---

# 第 243 章 macosx-104-tiger的unix03认证奠基

## 要点

- Tiger 引入 **Dashboard**——基于 **WebKit**（Apple 自 KHTML/KJS 开源项目 fork 而来的网页渲染引擎，2003 年随 Safari 1.0 发布）的小部件运行环境，允许开发者使用 HTML/CSS/JavaScript 构建桌面小部件。Dashboard 与 BSD 层的关联体现于：小部件通过 BSD 层的 `mach_init`/`launchd
- **Rosetta** 是 Apple 为 PowerPC→Intel 转换开发的动态二进制翻译层，随 **Mac OS X 10.4.4 Tiger Universal Binary**（**2006 年 1 月 10 日** 首批 Intel Mac 上市同步推出）一同发布。Rosetta 在用户态运行，将 PowerPC 二进制翻译为 Intel x86 代码执行，依赖 BSD 层的 `mm
- **2005 年** Tiger 对比 **FreeBSD 5.4**（**2005 年 5 月 9 日** 发布）、**Linux 2.6**（2003-2005 年）、**Solaris 10**（**2005 年 1 月 31 日** 发布，已获 **UNIX 03**）、**Windows XP x64**（**2005 年 3 月 28 日** 发布），其 ACL 与 Spotlight

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4123] 卷“第12卷-macos的bsd遗产”第 243 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充
- [DB:references_fulltext:chapter_matches:chmatch_4124] 卷“第12卷-macos的bsd遗产”第 243 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- Dashboard 的设计理念是否 “借鉴” Konfabulator——此争议须以双方公开声明为准，避免单方叙事。Konfabulator 团队的批评反映 Apple 与第三方开发者之间的设计理念张力，但 Dashboard 基于 WebKit 的技术实现与 Konfabulator 的独立运行环境在工程层面独立。采信 “Dashboard 与 Konfabulator 共享小部件设计理念但技术
- Rosetta（2006）与 Rosetta 2（2020）的工程差异——Rosetta 为 PowerPC→Intel 翻译，Rosetta 2 为 Intel→ARM 翻译，二者均依赖 BSD 层的 `mmap`、`mprotect` 系统调用但翻译方向相反。Rosetta 的性能损耗约 40%-60%（Apple 官方数据，针对 PowerPC 应用在 Intel 上的运行效率），Roset
- Solaris 10 的 UNIX 03 认证与 Apple later 认证的路径差异须厘清——Solaris 10 在 2005 年 1 月发布时即获 UNIX 03 认证（Sun Microsystems 作为 Unix 传统厂商，认证是其商业策略一部分），Apple 在 2007 年 Leopard 才获得认证（Apple 作为非传统 Unix 厂商，认证是其从消费设备向开发者生态扩展的策

## 文献

- Apple Inc. Mac OS X 10.4 Tiger Release Notes [EB/OL]. (2005-04-29). Apple Developer; Apple Inc. WWDC 2005 Session: Dashboard [EB/OL]. (2005-06-06). Apple Developer.<!-- DB_REF:darwin.duckdb -->> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。> 2005-2005 年间：92 次提交。> 仓库总览：2,016 次提交，27 位贡献者，2001-04-10 至 2106-02-07。
- Apple Inc. Macworld San Francisco 2006: Intel Macs [EB/OL]. (2006-01-10). Apple Press Release; Apple Inc. Rosetta Technical Overview [Z]. Apple Developer Documentation, 2006; bsd_commits.db 查询结果 [EB/OL]. script/query_xnu_tags.py, 2026-07-23; 原材料/研究/考据记录/20260723_announcements-macos.md [EB/OL]. 2026-07-23.<!-- DB_REF:darwin.duckdb -->> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。> 2004-2005 年间：154 次提交。> 仓库总览：2,016 次提交，27 位贡献者，2001-04-10 至 2106-02-07。
- FreeBSD Project. FreeBSD 5.4 Release Notes [EB/OL]. (2005-05-09). <https://www.freebsd.org/releases/>; Linux Kernel Archives. Linux 2.6 Release Notes [EB/OL]. (2003-2005). <https://www.kernel.org/>; Sun Microsystems. Solaris 10 Launch [EB/OL]. (2005-01-31). Sun Press Release.FreeBSD 社区论文：[FP-2008-003] Mac OS X - From the server room to your pocket（Jordan K. Hubbard（乔丹·哈伯德），2008）<https://papers.freebsd.org/2008/lisa08/hubbard-macosx_from_the_server_room_to_your_pocket/><!-- DB_REF:darwin.duckdb -->> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。> 1985-2026 年间：2,012 次提交。> 仓库总览：2,016 次提交，27 位贡献者，2001-04-10 至 2106-02-07。
