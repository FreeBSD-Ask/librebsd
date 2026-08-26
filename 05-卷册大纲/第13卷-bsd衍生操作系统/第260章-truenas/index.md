---
chapter: 第 260 章
id: CH260
volume: 第13卷-bsd衍生操作系统
---

# 第 260 章 truenas

## 要点

- FreeNAS（2005）以 FreeBSD 为基底，提供基于 Web 的 NAS 管理，利用 FreeBSD 的 ZFS（later）、Samba、ZFS 集成能力；其成功证明 BSD 在存储设备上的可行性。
- 2010 年代 FreeNAS 品牌统一为 TrueNAS；later 推出 TrueNAS SCALE（基于 Linux 的 Debian 分支）与 TrueNAS CORE（基于 FreeBSD）并存，标志 BSD 衍生在企业存储中的分化；具体年份须以 iXsystems 公告核实。
- FreeNAS/TrueNAS 依赖 FreeBSD 社区（ZFS 移植者、驱动作者）与 iXsystems 工程师；Olivier Cochard-Labbé 作为创始人属非英美（法国）贡献者。
- 对比 TrueNAS（FreeBSD/Debian）与 NetApp ONTAP（BSD 网络栈）、Synology（Linux）、QNAP（Linux），分析存储 OS 的 BSD 占比。
- 2011 年 8 月 9 日，truenas-middleware 仓库记录了 CVE-2011-2522 与 CVE-2011-2694 的修复 commit `85d6a4efaf48f05a7a876e905b0ebc82e0c70bc3`（author Xin Li，即 FreeBSD 核心开发者 delphij），通过更新至 Samba 3.5.11 修复 Samba VUZZI 与代码

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4135] 卷“第13卷-bsd衍生操作系统”第 260 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充
- [DB:references_fulltext:chapter_matches:chmatch_4136] 卷“第13卷-bsd衍生操作系统”第 260 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- FreeNAS 各版本对应的 FreeBSD 基底版本须以 Release Notes 核实；openbsd.db 查询 L7.6.1 的 ixsystems_contributors 字段仅基于邮箱域名（@ixsystems.com、@truenas.com）识别，员工可能用个人邮箱（如@gmail.com）提交，识别存在低估，须与 iXsystems 员工名册、commit message 中
- SCALE 转向 Linux 反映存储软件栈（容器/K8s）的生态压力，须客观论述[考据完成：2026-07-28 经穷尽联网考据，TrueNAS 25.04 "Fangtooth"（2025 年发布）彻底拥抱 Linux 作为核心基础，结束 CORE（FreeBSD 基底）与 SCALE（Linux 基底）并存的局面；TrueNAS 25.10 "Goldeye"（2025-10-28 发布）支
- 具体贡献者须以公开记录核实；freebsd.db 查询 L7.2.1 的邮箱匹配不等于同一人（可能重名），且已排除 @freebsd.org 邮箱以聚焦非核心团队的外部回馈，iXsystems 员工若同时持有 @freebsd.org 邮箱则会被排除，导致回馈量可能被低估，须与 iXsystems 员工名册、freebsd-src 提交权限记录交叉验证
- NetApp ONTAP 的 BSD 渊源须以官方架构文档确认。
- truenas-middleware 的 14 条 CVE commit 仅覆盖 middleware 自身代码与集成的第三方软件，FreeBSD 内核层漏洞由 freebsd-src 仓库跟踪并在 TrueNAS 版本更新时同步，两者不可混淆；commit `85d6a4efaf48f05a7a876e905b0ebc82e0c70bc3` 的 author 为 delphij（Xin Li），

## 文献

- FreeNAS/TrueNAS 官方文档；iXsystems 公司史；bsd_commits.db 查询 L7.6.1（truenas-middleware 仓库 commit 量趋势与 iXsystems 员工占比，2005-2026）；原材料/研究/bsd 仓库分析/数据分析/衍生项目与跨项目对比分析.md §L7.6。 ［B］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2005-2011 年间：250,940 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- iXsystems 官方文档；bsd_commits.db 查询 L7.6.1（truenas-middleware commit 量趋势与 iXsystems 员工占比，2005-2026）；bsd_commits.db 查询 L3.2.1（商业实体 commit 占比随时间变化）；bsd_commits.db 查询 L3.2.2（商业实体 commit 量按仓库分布）；原材料/研究/bsd 仓库分析/数据分析/衍生项目与跨项目对比分析.md §L7.6；原材料/研究/bsd 仓库分析/数据分析/深层信息挖掘.md §L3.2.1、§L3.2.2。 ［B］## 259.2.2 外部贡献者
- iXsystems 工程档案；freebsd.db 查询 L7.2.1（衍生项目贡献者在 freebsd-src 的回馈 commit，≥5 次，前 30 名）；原材料/研究/bsd 仓库分析/数据分析/衍生项目与跨项目对比分析.md §L7.2。 ［A］<!-- DB_REF:bsd_derivatives.duckdb -->> **数据库引用（bsd_derivatives.duckdb）**：本子节对应 bsd_derivatives 代码仓库。> 2011-2026 年间：573,325 次提交。> 仓库总览：963,557 次提交，14,109 位贡献者，1985-06-13 至 2026-08-24。
- 各存储厂商官方资料。[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:bsd_derivatives.duckdb -->> **数据库引用（bsd_derivatives.duckdb）**：本子节对应 bsd_derivatives 代码仓库。> 1985-2026 年间：963,557 次提交。> 仓库总览：963,557 次提交，14,109 位贡献者，1985-06-13 至 2026-08-24。
- bsd_commits.db 查询 truenas-middleware CVE commit（14 条，7 去重 CVE，2026-07-23）；`原材料/研究/bsd漏洞史/数据库提取/truenas-middleware-cve-commits.md`；Samba 安全公告档案。 ［B］## 259.4.2 CVE-2021-20316 NFS/SMB 配置告警与 TrueNAS 的 “漏洞监控” 差异化策略
- bsd_commits.db 查询 truenas-middleware CVE-2021-20316 commit；NVD. CVE-2021-20316 [EB/OL]. <https://nvd.nist.gov/vuln/detail/CVE-2021-20316>（访问日期 2026-07-23）；`原材料/研究/bsd漏洞史/数据库提取/truenas-middleware-cve-commits.md`。 ［B］FreeBSD 社区论文：[FP-2021-008] smart(8) Update: A Permissively-Licensed Alternative to smartctl(8)（Michael Dexter（迈克尔·德克斯特）; Chuck Tuffli，2021）<https://papers.freebsd.org/2021/eurobsdcon/dexter-tuffli-update_on_smart/>FreeBSD 社区论文：[FP-2020-021] How an Australian IaaS uses FreeBSD（Ruben Schade，2020）<https://papers.freebsd.org/2020/linux.conf.au/schade_how_an_australian_iaas_uses_freebsd/>FreeBSD 社区论文：[FP-2019-076] FreeBSD at Work: Building Network and Storage Infrastructure with pfSense and FreeNAS（Conor Beh，2019）<https://papers.freebsd.org/2019/vbsdcon/beh-freebsd_at_work/>FreeBSD 社区论文：[FP-2019-080] Transitioning from FreeNAS to FreeBSD（David Fullard，2019）<https://papers.freebsd.org/2019/vbsdcon/fullard-transitioning_from_freenas_to_freebsd/>FreeBSD 社区论文：[FP-2018-002] Flexible Disk Use in OpenZFS（Matt Ahrens，2018）<https://papers.freebsd.org/2018/bsdcan/ahrens-flexible_disk_use_in_openzfs/>FreeBSD 社区论文：[FP-2018-011] Replacing Traditional Backup Systems with ZFS: Using ZFS Snapshots and Replication to Simplify Backups（Calvin Hendryx-Parker，2018）<https://papers.freebsd.org/2018/bsdcan/hendryxparker-replacing_traditional_backup_systems_with_zfs/>FreeBSD 社区论文：[FP-2018-054] FreeNAS and bhyve（Marcelo Araujo，2018）<https://papers.freebsd.org/2018/araujo-freenas_and_bhyve/>FreeBSD 社区论文：[FP-2016-005] Directory Services on FreeNAS（John Hixson，2016）<https://papers.freebsd.org/2016/asiabsdcon/john-directory-services/>FreeBSD 社区论文：[FP-2016-008] FreeBSD Test Cluster Automation（Kamil Czekirda，2016）<https://papers.freebsd.org/2016/asiabsdcon/kczekirda-test_cluster/>FreeBSD 社区论文：[FP-2007-001] FreeNAS（Olivier Cochard-Labbé，2007）<https://papers.freebsd.org/2007/bsdcan/cochard-freenas/><!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1985-2026 年间：1,294,851 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
