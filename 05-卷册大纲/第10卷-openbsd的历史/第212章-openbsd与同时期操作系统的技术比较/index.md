---
chapter: 第 212 章
id: CH212
volume: 第10卷-openbsd的历史
---

# 第 212 章 OpenBSD 与同时期操作系统的技术比较

## 要点

- OpenBSD 采用 “默认安全 + 代码审计” 模型，FreeBSD 采用 “Security Officer + MAC Framework” 模型；FreeBSD 通过 TrustedBSD 项目（2000-2003 年由 Robert Watson、Poul-Henning Kamp（波尔-亨宁·坎普） 等推动）引入 MAC、Jails（1999 年由 Poul-Henning Kamp 开发）与 MAC Framework（随 FreeBSD 5.0，2003-01-19 合入）
- SELinux 由 NSA 主导开发，2000 年 12 月首次发布（基于 Flask 架构与 Type Enforcement），2003 年合入 Linux 2.6 内核主线，依赖 Linux Security Modules（LSM）框架；AppArmor 由 Immunix 公司开发（1998 起），2006 年随 SUSE Linux Enterprise 10 集成；pledge/unveil 由 OpenBSD 社区开发（pledge 随 5.9 引入，unveil 随 6.4 引入）
- Solaris 自 8（2000）起提供 RBAC（Role-Based Access Control），Solaris 10（2005-01）引入 Trusted Extensions 与 Zones；AIX 5L（2001）提供多级安全（MLS）与 Trusted Computing Base（TCB）评估；HP-UX 11i v2（2003）提供 Security Containment 等安全特性；Solaris/AIX/HP-UX 均持有 Common Criteria EAL4+ 认证，OpenBSD 从未申请
- macOS 基于 Darwin（含 BSD 用户空间，自 Mac OS X 10.0 起源自 FreeBSD 4.x 用户空间与 Mach 3.0 内核混合）；macOS 通过 Sandbox（10.5 Leopard 2007 引入 Seatbelt sandbox，基于 TrustedBSD MAC Framework），后续引入 Gatekeeper（10.8，2012）、SIP（10.11，2015）与 Apple Silicon PAC（A12 起，2018）
- OpenBSD pf 由 Daniel Hartmeier（丹尼尔·哈特迈尔） 主导开发，2001 年随 OpenBSD 3.0（2001-12-01 发布）引入——openbsd.duckdb openbsd-src 仓库 commit 148b55c022b1（2001-06-24 kjell 引入 sys/net/pf.c 与 sys/net/pfvar.h）证实代码引入时间早于 3.0 发布约 5 个月

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3909] 卷“第10卷-openbsd的历史”第 212 章，匹配置信度 folder，原因：folder 第210章

## 史观

- 总纲8 本体论上各方平等：OpenBSD 与 FreeBSD、Linux、商业 UNIX、macOS 的安全机制比较不预设孰优孰劣——默认安全＋代码审计、Security Officer＋MAC Framework、LSM 策略框架、CC 认证体系各有其生成语境与代价，比较以技术层级与粒度差异呈现而非排名。（汇总自 212.1-212.6 各节史观字段）
- 总纲9 经验优先：pledge/unveil、MAC Framework、SELinux 等机制的实际效果以部署经验与漏洞处置记录为准，认证与宣传不替代经验检验。
- 总纲5 没有必然性，只有偶然性：各系统安全路线的分岔源于具体的人、机构与时机（NSA 主导 SELinux、Hartmeier 重写 pf、de Raadt 拍板发布流程），而非抽象必然。
- 总纲4 分离聚合是永恒规律：pf 自 OpenBSD 分离后聚合于 FreeBSD/NetBSD，arc4random/strlcpy 自 OpenBSD 扩散至 POSIX.1-2024，代码在分离与聚合间循环流动。

## 辨析

- OpenBSD 与 FreeBSD 安全模型严格程度的对比缺乏权威评估；pledge/unveil 与 MAC Framework 的技术层级不同——pledge 是进程级 syscall 沙箱（用户态调用 pledge(2) 后内核拒绝非白名单 syscall），MAC Framework 是内核级策略框架（管理员加载模块如 mac_biba、mac_mls 后内核在 syscall 路径上调用
- SELinux 与 pledge/unveil 的功能并非完全等价——SELinux 提供内核级 MAC 策略（约 4000+ 类型、用户/角色/类型三元组），pledge 提供进程级 syscall 沙箱（约 30 个 promise 关键字、不区分用户角色），技术层级与粒度均不同；〔待核：原文截断，后文待回源〕
- 商业 UNIX 持有 Common Criteria 认证与 OpenBSD 无认证的实际安全水平对比缺乏权威评估——认证仅证明通过评估流程，不保证实际漏洞率更低；Common Criteria EAL4+ 评估证书在 commoncriteriaportal.org 数据库中可查 Solaris 10（认证 ID CEMC/VS-0003/2005）〔待核：原文截断，后文待回源〕
- macOS SIP 与 OpenBSD pledge/unveil 的技术层级不同——SIP 保护系统级完整性（限制 root 写入 /usr、/bin、/sbin 等系统目录），pledge 限制进程级 syscall（程序运行时声明所需 promise 类别），unveil 限制进程级文件路径访问；macOS 的 BSD 用户空间渊源与安全机制的关系是独立演进——Darwin 用户空间源自 F
- 三者性能对比缺乏权威基准——多数公开基准（Phoronix、Calomel.org）存在配置不等价问题（如未对齐规则数量、状态表大小、conntrack 模块）；FreeBSD 默认仍提供 IPFW/IPF/pf 三选项（编译时选择），NetBSD 自 7.0（2015-10）起 NPF 取代 pf 作为默认防火墙（<https://man.netbsd.org/npf.7>）

## 文献

- FreeBSD TrustedBSD 项目 [EB/OL]. <https://docs.freebsd.org/en/books/arch-handbook/mac/>；FreeBSD Jails 文档 [EB/OL]. <https://docs.freebsd.org/en/books/handbook/jails/>；OpenBSD pledge(2) 手册页 [EB/OL]. <https://man.openbsd.org/pledge.2>；OpenBSD unveil(2) 手册页 [EB/OL]. <https://man.openbsd.org/unveil.2>；OpenBSD commit df174574d401 [G/OL]. <https://github.com/openbsd/src/commit/df174574d401>；OpenBSD commit 8b23add8c74b [G/OL]. <https://github.com/openbsd/src/commit/8b23add8c74b>；统计分析报告：推断性统计.md Task 11 [R/OL]. 2026-07-27. 文件路径：**03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/推断性统计.md**；Python 统计脚本：`script/phase2_inferential.py`. Task 11 各卷 doubt_flag 卡方检验 + Cramer's V 效应量。执行日期：2026-07-27 ［A］

**OpenBSD pledge/unveil vs FreeBSD MAC Framework 对比**：

| 维度 | OpenBSD pledge/unveil | FreeBSD MAC Framework |
| --- | --- | --- |
| 引入版本 | pledge 5.9（2015-10-18）、unveil 6.4（2018-10-15） | 5.0（2003-01-19） |
| 关键 commit | `df174574d401`（2015-10-09 tame→pledge）、`8b23add8c74b`（2018-07-13 unveil） | TrustedBSD 项目（2000-2003） |
| 技术层级 | 进程级 syscall 沙箱 | 内核级策略框架 |
| 权限模型 | 白名单内建于程序代码 | 策略外置为可加载模块 |
| 管理员干预 | 无可关闭选项 | 可后置配置策略 |
| 时间差 | — | 早约 12 年 |
- NSA SELinux 项目 [EB/OL]. <https://www.nsa.gov/what-we-do/research/selinux/>；AppArmor 项目 [EB/OL]. <https://apparmor.net/>；Linux Kernel 2.6.0 Release Notes [EB/OL]. <https://kernelnewbies.org/LinuxChanges>；OpenBSD pledge(2) 手册页 [EB/OL]. <https://man.openbsd.org/pledge.2>；OpenBSD unveil(2) 手册页 [EB/OL]. <https://man.openbsd.org/unveil.2>；Red Hat SELinux 文档 [EB/OL]. <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/>；openbsd.duckdb 查询 L7.3.1（来源：原材料/研究/bsd 仓库分析/数据分析/衍生项目与跨项目对比分析.md §L7.3.1） ［A］

**SELinux/AppArmor/pledge/unveil 安全模块对比**：

| 维度 | SELinux | AppArmor | OpenBSD pledge/unveil |
| --- | --- | --- | --- |
| 主导方 | NSA | Immunix 公司 | OpenBSD 社区 |
| 首次发布 | 2000-12 | 1998 起 | pledge 5.9（2015-10-18） |
| 主线集成 | Linux 2.6（2003） | SUSE 10（2006） | OpenBSD 源码树内建 |
| 策略规模 | RHEL 默认约 4000+ 类型 | 路径前缀配置 | pledge 约 30 个 promise 关键字 |
| 路线 | 策略可配置 MAC | 策略可配置 MAC | 白名单沙箱默认 |
| 关键字示例 | 用户/角色/类型三元组 | 路径模式 | “stdio”、“rpath”、“wpath”、“inet”、“dns” |
- Solaris 10 Trusted Extensions 文档 [EB/OL]. <https://docs.oracle.com/cd/E19253-01/>；AIX Security Guide [EB/OL]. <https://www.ibm.com/docs/en/aix/>；HP-UX Security Features [EB/OL]. <https://docs.hp.com/>；Common Criteria 证书数据库 [EB/OL]. <https://www.commoncriteriaportal.org/>；OpenBSD 安全声明 [EB/OL]. <https://www.openbsd.org/> ［A］

**商业 UNIX 安全机制与 OpenBSD 路线对比**：

| 系统 | 关键安全机制 | 引入版本 | Common Criteria 认证 | OpenBSD 对应路线 |
| --- | --- | --- | --- | --- |
| Solaris | RBAC、Trusted Extensions、Zones | Solaris 8（2000）/10（2005-01） | EAL4+ | 无对应，OpenBSD 走 jail(8) + pledge |
| AIX | MLS、Trusted Computing Base | AIX 5L（2001） | EAL4+ | 无对应 |
| HP-UX | Security Containment | HP-UX 11i v2（2003） | EAL4+ | 无对应 |
| OpenBSD | 代码审计、pledge/unveil | 自 1995-10-18 fork | 从未申请 | 纯社区审计驱动 |

注：EAL4+ 证书随版本与评估期限更新，表中认证以各系统对应版本的评估时点证书为准，避免过期误读。
- Apple Platform Security 白皮书 [EB/OL]. <https://support.apple.com/guide/security/welcome/web>；Darwin/XNU 开源代码 [EB/OL]. <https://opensource.apple.com/projects/xnu/>；OpenBSD pledge(2) 手册页 [EB/OL]. <https://man.openbsd.org/pledge.2>；OpenBSD unveil(2) 手册页 [EB/OL]. <https://man.openbsd.org/unveil.2> ［A］

**macOS 安全机制演进与 OpenBSD 对应**：

| macOS 机制 | 引入版本 | 时间 | 技术层级 | OpenBSD 对应 |
| --- | --- | --- | --- | --- |
| Sandbox（Seatbelt） | 10.5 Leopard | 2007 | 基于 TrustedBSD MAC Framework | pledge（5.9，2015） |
| Gatekeeper | 10.8 Mountain Lion | 2012 | 代码签名验证 | 无对应 |
| SIP | 10.11 El Capitan | 2015 | 系统目录保护 | 无对应（root 权限边界由程序源码声明） |
| Apple Silicon PAC | A12 起 | 2018 | 硬件级控制流完整性 | OpenBSD 7.6（2024-10）arm64 部分支持 |
- Daniel Hartmeier pf 历史 [EB/OL]. <https://www.benzedrine.ch/pf.html>；OpenBSD 3.0 Release Notes [EB/OL]. <https://www.openbsd.org/30.html>；FreeBSD IPFW 手册页 **ipfw(8)** [EB/OL]. <https://www.freebsd.org/cgi/man.cgi?ipfw(8)>；Linux nftables 项目 [EB/OL]. <https://www.netfilter.org/projects/nftables/>；NetBSD NPF 手册页 **npf(7)** [EB/OL]. <https://man.netbsd.org/npf.7> ［A］

**pf 关键 commit 时间线**：

| 日期 | 事件 | commit | 关键人物 |
| --- | --- | --- | --- |
| 2001-05-30 | 删除 sbin/ipf/ | `345de70aec27` | deraadt |
| 2001-06-24 | 引入 sys/net/pf.c 与 sys/net/pfvar.h | `148b55c022b1` | kjell |
| 2001-12-01 | pf 随 OpenBSD 3.0 发布 | — | Daniel Hartmeier |
| 2003 | pf 随 FreeBSD 5.3 移植 | — | Hartmeier 本人提交 |
| 2007-12 | pf 随 NetBSD 4.0 集成 | — | — |
- OpenBSD “Only two remote holes” 声明 [EB/OL]. <https://www.openbsd.org/>；OpenBSD Security Advisories [EB/OL]. <https://www.openbsd.org/security.html>；CVE 数据库 [EB/OL]. <https://cve.mitre.org/>；W3Techs OS 市场占有率 [EB/OL]. <https://w3techs.com/technologies/overview/operating_system>；OpenBSD strlcpy(3) 手册页 [EB/OL]. <https://man.openbsd.org/strlcpy.3>；OpenSSH 项目 [EB/OL]. <https://www.openssh.com/>；freebsd.duckdb 查询 L1.1.2（来源：原材料/研究/bsd 仓库分析/数据分析/宏观趋势统计.md §L1.1.2） ［A］

**OpenBSD 安全成果扩散时间线**：

| 成果 | 引入日期 | commit hash | 关键人物 | 跨项目采纳情况 |
| --- | --- | --- | --- | --- |
| arc4random(3) | OpenBSD 2.1（1996-12） | `af7d239111f9`（1996-12-28） | dm | FreeBSD/macOS 采纳 |
| strlcpy(3)/strlcat(3) | OpenBSD 2.4（1998-12） | `1dc0268a4106`（1998-07-01） | millert | 进入 POSIX.1-2024 标准 |
| OpenSSH | 1999-10-01 | `bf74e864c129` | deraadt | Linux/macOS/Windows 默认 SSH 事实标准 |
| pledge/unveil | OpenBSD 5.9/6.4（2015/2018） | `df174574d401`、`8b23add8c74b` | deraadt/beck | 启发 Linux landlock 与 FreeBSD capsicum |
<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP324（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Dan Langille 记录把 ZFS 池从 Dell R710 迁至 R720 的过程：停止应用、导出池、换盘、导入即可，且 ZFS 能跨端序（如 amd64 到 sparc64）处理，远超依赖同型 RAID 控制器的传统迁移。（BSD Now EP324，[261.86-321.34]，L2）
- 《OpenBSD in 2019》体验帖列举其优点（安全优先、base 与 /usr/local 分离、高质量 man page、clang 支持 C++17）与缺点（升级需手动清理、RAM 耗尽死机、find/du/tar 等工具差异），结论是仍愿继续使用。（BSD Now EP324，[501.72-909.04]，L2）
- Hammer2 增加紧急空间模式，允许在无空间写历史时继续磁盘操作，但会牺牲断电保护并可能损坏快照，与 ZFS 预留 slop 空间、UFS 超 100% 的策略形成对照。（BSD Now EP324，[1526.06-1671.52]，L2）
- ICCCM 选择机制的吐槽揭示 X11 规范以 atom 表达一切、缺少目标类型与属性类型的显式关联，实现者各自解读导致兼容性 creep 与增量传输的脆弱。（BSD Now EP324，[1304.40-1519.02]，L2）
- DragonFly BSD 更新 zlib 至 1.2.11、导入 dhcpcd 8.1.1，并把 PAM SSH/TacPlus/Radius 模块移出 base 改由 ports 提供，以换取更频繁的更新节奏。（BSD Now EP324，[923.76-987.80]，L2）

**史料**：

- Dan Langille 博客的 ZFS 迁移记录，含 zpool status 快照、驱动托盘与 ICY Dock 适配器换装细节。（BSD Now EP324，[133.60-235.80]，L2）
- 用户体验帖《OpenBSD in 2019》及其对 GNU cpio 1994 年遗留 bug 的对照检查。（BSD Now EP324，[388.92-402.52]，L2）
- DragonFly BSD 关于 Hammer2 emergency mode 的提交说明，及 zlib、dhcpcd、PAM 模块调整的维护记录。（BSD Now EP324，[937.08-993.00]，L2）
- Brian Kernighan《Unix: A History and a Memoir》由 Princeton 于 2019 年 10 月出版的信息。（BSD Now EP324，[1938.08-1996.44]，L2）

**史观**：

- 总纲9 经验优先：ZFS 迁移与 OpenBSD 评估都来自动手记录与亲身使用，而非厂商宣传或抽象判断。（BSD Now EP324，[106.52-115.00]，L2）
- 总纲8 本体论上各方平等：OpenBSD 的优点被承认、缺点被具体列出，不神话也不贬低任何一方。（BSD Now EP324，[501.72-909.04]，L2）
- 总纲4 分离聚合是永恒规律：ZFS 数据可从一台机器分离、在另一台聚合，硬件代际更替体现分离聚合的循环。（BSD Now EP324，[263.66-301.54]，L2）
- 总纲12 科学是形式主义：写时复制、紧急模式、slop 空间是文件系统对空间与安全的形式化约定。（BSD Now EP324，[1542.42-1671.52]，L2）
- 总纲22 知识注定过时：OpenBSD 体验帖中列出的坏项可能已被修复，工具行为随版本变化，知识需持续更新。（BSD Now EP324，[898.80-921.40]，L2）
- 总纲5 没有必然性，只有偶然性：能否顺利迁移取决于托盘规格、热插拔适配等偶然硬件条件，而非抽象必然。（BSD Now EP324，[142.44-153.60]，L2）

**辨析**：

- Hammer2 紧急模式的“损坏快照”风险与 ZFS 预留空间对比为二手转述，未读 DragonFly 源码验证其具体实现边界。　[存疑脚注] 需对照 DragonFly 提交与手册核实危险程度（BSD Now EP324，[1557.86-1562.90]，L4）
- OpenBSD 体验帖的 RAM 耗尽死机成因不确定是 OpenBSD 本身还是 Vultr 虚拟化环境，作者本人未下定论。　[考据脚注] 环境变量未隔离，因果归属存疑（BSD Now EP324，[691.12-706.72]，L4）

**文献**：

- [BSD Now EP324] Pennington J. BSD Now: 324: Emergency Space Mode[EB/OL]. (2019-11-14)[2026-08-15]. <https://www.bsdnow.tv/324>.

<!-- /PODCAST_REVIEW -->

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

