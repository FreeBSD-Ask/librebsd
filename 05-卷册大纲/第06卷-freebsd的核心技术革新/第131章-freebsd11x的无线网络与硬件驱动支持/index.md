---
chapter: 第 131 章
id: CH131
volume: 第06卷-freebsd的核心技术革新
---

# 第 131 章 freebsd11x的无线网络与硬件驱动支持

## 要点

- 11.x 时期虚拟化平台驱动持续改进：VMware 方面——**vmx(4)** VMXNET3 网络驱动在 10.0 从 OpenBSD 移植后 11.x 持续改进性能与稳定性；**vmblock(4)**/**vmmouse(4)**/**vmhgfs(4)** 等 VMware guest 驱动持续更新；VMware SVGA 图形驱动配合 Xorg 可实现自适应分辨率。Xen 方面——Do
- FreeBSD 11.x 五个版本的架构支持变化精确时间线见下表，stable/11 EOL 日期为 **2021-09-30**。对比：stable/10 支持 8 种架构（含 ia64，无 aarch64）；stable/12 将移除 sparc64、引入 RISCV 正式支持、arm64 持续向 Tier 1 迈进。11.x 标志着 FreeBSD 架构支持从“传统 RISC 架构（Powe
- 11.x 时期 FreeBSD 活跃贡献者群体数百人，核心贡献者包括（不限于）：①Release Engineering：Glen Barber（gjb@，Release Engineering Lead 贯穿 11.x 全系列）、Marius Strobl（Deputy Lead）、Konstantin Belousov（kib@）、Bryan Drewery（布莱恩·德鲁里）（bdrewery
- 外部安全研究者系统审计 FreeBSD 无线网络栈，发现多个 WPA2 缺陷（含 KRACK 相关）。促使 FreeBSD 安全团队建立无线专项审计流程。
- 11.x 时期第三方软件变更的特点是“稳定升级、无激进取代”——Clang 持续升级但无新的编译器迁移，OpenSSL 保持 1.0.2 系列、sendmail 保持默认地位、GCC 继续保留用于非 x86 架构。与 10.0 的“集中换代”和 12.0/13.0 的“GCC 移除”相比，11.x 是三个版本周期中的“稳定期”——10.0 引入新工具链，11.x 稳定使用，12.0/13.0 完成

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_1305] 卷“第06卷-freebsd的核心技术革新”第 131 章，匹配置信度 0.6，原因：关键词匹配: poul-henning kamp
- [DB:references_fulltext:chapter_matches:chmatch_1306] 卷“第06卷-freebsd的核心技术革新”第 131 章，匹配置信度 0.6，原因：关键词匹配: nanobsd
- [DB:references_fulltext:chapter_matches:chmatch_1307] 卷“第06卷-freebsd的核心技术革新”第 131 章，匹配置信度 0.6，原因：关键词匹配: poul-henning kamp

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- Xen Dom0 在 11.x 确实有改进但 FreeBSD 11.x Release Notes 未将其列为 production-ready 特性；VMware 的 open-vm-tools 通过 ports 提供（emulators/open-vm-tools）而非 base 系统组件；VirtualBox 兼容在 11.x 时期存在已知的 panic 问题（11.1 Announceme
- FreeBSD 11.x 全系列均未提供 MIPS 发布镜像（MIPS 为 Tier 3/嵌入式支持，主要用于路由器等定制固件），这一点与 OpenWrt 等嵌入式 Linux 发行版不同——FreeBSD/MIPS 主要用于特定嵌入式项目而非通用发布。
- 上述贡献者列表不可避免地存在遗漏——任何简短名单都无法覆盖所有重要贡献者。需强调，FreeBSD 是“贡献者决定地位”的精英制（meritocracy），代码质量、持续贡献、社区声誉是获得 committer 权限与影响力的主要途径，雇主身份（是否受雇于大公司）不直接决定社区地位。
- 不应将 11.x 的“无重大第三方软件变更”视为“缺乏创新”——11.x 时期 FreeBSD 在 arm64 支持、bhyve 成熟、UEFI 完善、网络栈优化（Netflix 驱动）、虚拟化支持等方面有大量创新，只是这些创新不直接涉及第三方软件的替换
- 不应神化或贬低 11.x 系列——它继承了 10.0 的一些迁移期问题（早期版本仍有少量工具链与驱动 bug），且不包含 12.x/13.x 的众多新特性（WireGuard、ZFS 加密、OpenSSL 1.1、arm64 Tier 1、git 迁移等），但 11.3/11.4 是 FreeBSD 历史上最稳定可靠的版本系列之一，适合对稳定性要求极高的生产环境使用。11.x 时期也是 FreeB

## 文献

- FreeBSD vmx(4)/ena(4) Manual Pages [Z]；FreeBSD 11.1-RELEASE Announcement（Hyper-V Gen2）[Z]. 2017.[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- FreeBSD 11.0-11.4 RELEASE Announcements [Z]. 2016-2020；FreeBSD Security Information page support timeline [Z].[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- FreeBSD 11.x RELEASE Announcements Acknowledgments/Dedication sections [Z]；FreeBSD Developer Information [EB/OL]. freebsd.org/doc/en_US.ISO8859-1/articles/contributors/.[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- SA-17:07; Vanhoef 2017 ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- FreeBSD 11.x Release Notes [Z]. 2016-2020[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]---<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- Lucas M W. Absolute FreeBSD [M]. 3rd ed. San Francisco: No Starch Press, 2018（基于 FreeBSD 11.x 体验）；FreeBSD 11.x RELEASE Announcements/Release Notes [Z]. 2016-2020；FreeBSD Foundation Annual Reports 2016-2020 [R].[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]---<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
