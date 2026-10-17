---
chapter: 第 243 章
id: CH243
volume: 第12卷-macos的bsd遗产
---

# 第 243 章 Mac OS X 10.4 Tiger：UNIX 03 认证的奠基

## 要点

- Tiger 引入 **Dashboard**——基于 **WebKit**（Apple 自 KHTML/KJS 开源项目 fork 而来的网页渲染引擎，2003 年随 Safari 1.0 发布）的小部件运行环境，允许开发者使用 HTML/CSS/JavaScript 构建桌面小部件。Dashboard 与 BSD 层的关联体现于：小部件通过 BSD 层的 `mach_init`/`launchd` 进程管理机制加载运行——`launchd` 系 Tiger 首次引入的系统启动与服务管理守护进程，接管 `mach_init`、`init`、`xinetd` 等传统机制的既有职责 [存疑脚注] 原要点在“`launchd”处机械截断、后文佚失；`launchd` 于 Mac OS X 10.4 Tiger 首次引入并接管 `mach_init`/`init`/`xinetd` 职责以 Apple《Getting Started with launchd》等官方文档为据（2026-09-13 联网复核），完整原文待原始档案公开后补充确证。
- **Rosetta** 是 Apple 为 PowerPC→Intel 转换开发的动态二进制翻译层，随 **Mac OS X 10.4.4 Tiger Universal Binary**（**2006 年 1 月 10 日** 首批 Intel Mac 上市同步推出）一同发布。Rosetta 在用户态运行，将 PowerPC 二进制翻译为 Intel x86 代码执行，依赖 BSD 层的 `mmap`、`mprotect` 系统调用完成内存映射与权限管理 [存疑脚注] 原要点在“`mm”处机械截断、后文佚失；`mmap`/`mprotect` 补全与本文件辨析二“二者均依赖 BSD 层的 `mmap`、`mprotect` 系统调用”一致，完整原文待原始档案公开后补充确证。
- **2005 年** Tiger 对比 **FreeBSD 5.4**（**2005 年 5 月 9 日** 发布）、**Linux 2.6**（2003-2005 年）、**Solaris 10**（**2005 年 1 月 31 日** 发布，已获 **UNIX 03**）、**Windows XP x64**（**2005 年 3 月 28 日** 发布）——同期五者中仅 Solaris 10 已获 **UNIX 03** 认证，FreeBSD 与 Windows 均未参与该认证，Tiger 的认证准备工作进行中、至 2007 年 Leopard 方正式获证 [存疑脚注] 原要点在 OS 列举处机械截断、后文佚失，〔待核〕标记已删；补全句以 The Open Group 认证目录与各系统发布记录为据（2026-09-13 联网复核），完整原文待原始档案公开后补充确证。

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4123] 卷“第12卷-macos的bsd遗产”第 243 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充
- [DB:references_fulltext:chapter_matches:chmatch_4124] 卷“第12卷-macos的bsd遗产”第 243 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充
- [DB:historical_claims:claim] 关键词行级挖掘素材线索 243.4-关键词行级挖掘素材线索（1 条，CL-RM 段，见 243.4-关键词行级挖掘素材线索.md）

## 史观

总纲第 12 条——科学是形式主义：UNIX 03 认证是以测试套件与证书形式确认“UNIX”身份的形式化度量，Tiger 期的 POSIX 合规工程是形式准备而非 Unix 血统的改变（据要点 3、辨析 3）；总纲第 4 条——分离聚合是永恒规律：Dashboard 所依 **WebKit** 系 Apple 自 KDE 的 KHTML/KJS fork 而来，代码自 KDE 分离而聚合于 Apple 生态，构成开源代码分合循环的节点（据要点 1、辨析 1）；总纲第 10 条——动手者创造历史：Rosetta 的动态二进制翻译与 `launchd` 的服务管理统一均系工程师以代码逐项实现的动手成果（据要点 1、2）；总纲第 9 条——经验优先：与同时期操作系统的比较以发布日期与认证状态的公开记录为准，不以“认证＝正统”的抽象序列下判断（据要点 3、辨析 3）；总纲第 3 条——不存在进步，只有权力再分配：Tiger 与 FreeBSD 5.4、Solaris 10 等并世系统在认证时序上的消长是 Unix 市场权力格局的再分配，而非单一线性进步（据要点 3）。（2026-09-13 整改：史观字段按批次 C060 核查清单回填，映射依 25 条权威表）

## 辨析

- Dashboard 的设计理念是否 “借鉴” Konfabulator——此争议须以双方公开声明为准，避免单方叙事。Konfabulator 团队的批评反映 Apple 与第三方开发者之间的设计理念张力，但 Dashboard 基于 WebKit 的技术实现与 Konfabulator 的独立运行环境在工程层面独立。采信 “Dashboard 与 Konfabulator 共享小部件设计理念但技术实现相互独立” 的判断，标注 ［考据注：本条按上下文补全句末截断（2026-09-13）；语义以正文与所引来源为准］
- Rosetta（2006）与 Rosetta 2（2020）的工程差异——Rosetta 为 PowerPC→Intel 翻译，Rosetta 2 为 Intel→ARM 翻译，二者均依赖 BSD 层的 `mmap`、`mprotect` 系统调用但翻译方向相反。Rosetta 的性能损耗约 40%-60%（Apple 官方数据，针对 PowerPC 应用在 Intel 上的运行效率），Rosetta 2 则在 Apple Silicon（2020 年起）上以 AOT（安装时预翻译）与 JIT（运行时翻译）相结合的方式转换 x86_64 代码 [存疑脚注] 原辨析二在“，Roset”处机械截断、后文佚失；Rosetta 2 双路翻译机制以 Apple 官方平台安全指南与公开资料为据（2026-09-13 联网复核），完整原文待原始档案公开后补充确证。
- Solaris 10 的 UNIX 03 认证与 Apple 后来的认证的路径差异须厘清——Solaris 10 在 2005 年 1 月发布时即获 UNIX 03 认证（Sun Microsystems 作为 Unix 传统厂商，认证是其商业策略一部分），Apple 在 2007 年 Leopard 才获得认证（Apple 作为非传统 Unix 厂商，认证是其从消费设备向开发者生态扩展的策略）。

## 文献

- Apple Inc. Mac OS X 10.4 Tiger Release Notes [EB/OL]. (2005-04-29). Apple Developer; Apple Inc. WWDC 2005 Session: Dashboard [EB/OL]. (2005-06-06). Apple Developer.

<!-- DB_REF:darwin.duckdb -->
> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。> 2005-2005 年间：92 次提交。> 仓库总览：2,016 次提交，时间跨度 2001-04-10 至 2026-04-13；contributors 表 43 行（42 个镜像仓库 + 1 行 dependabot，全部经 Apple OSS Distributions 自动化账号导入）。
- Apple Inc. Macworld San Francisco 2006: Intel Macs [EB/OL]. (2006-01-10). Apple Press Release; Apple Inc. Rosetta Technical Overview [Z]. Apple Developer Documentation, 2006; darwin.duckdb 查询结果 [EB/OL]. **script/query_xnu_tags.py**, 2026-07-23; **03-原始史料库/06-考据记录/20260723_announcements-macos.md** [EB/OL]. 2026-07-23. [存疑脚注] 20260723_announcements-macos.md 现未见于 03-原始史料库/06-考据记录/ 目录（现存 142 个文件，最早为 20260801），原“原材料/研究/考据记录/”路径已失效，该考据文件下落待库方核实。

<!-- DB_REF:darwin.duckdb -->
> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。> 2004-2005 年间：154 次提交。> 仓库总览：2,016 次提交，时间跨度 2001-04-10 至 2026-04-13；contributors 表 43 行（42 个镜像仓库 + 1 行 dependabot，全部经 Apple OSS Distributions 自动化账号导入）。
- FreeBSD Project. FreeBSD 5.4 Release Notes [EB/OL]. (2005-05-09). <https://www.freebsd.org/releases/>; Linux Kernel Archives. Linux 2.6 Release Notes [EB/OL]. (2003-2005). <https://www.kernel.org/>; Sun Microsystems. Solaris 10 Launch [EB/OL]. (2005-01-31). Sun Press Release.FreeBSD 社区论文：[FP-2008-003] Mac OS X - From the server room to your pocket（Jordan K. Hubbard（乔丹·哈伯德），2008）<https://papers.freebsd.org/2008/lisa08/hubbard-macosx_from_the_server_room_to_your_pocket/>

<!-- DB_REF:darwin.duckdb -->
> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。> 1985-2026 年间：2,012 次提交。> 仓库总览：2,016 次提交，时间跨度 2001-04-10 至 2026-04-13；contributors 表 43 行（42 个镜像仓库 + 1 行 dependabot，全部经 Apple OSS Distributions 自动化账号导入）。
