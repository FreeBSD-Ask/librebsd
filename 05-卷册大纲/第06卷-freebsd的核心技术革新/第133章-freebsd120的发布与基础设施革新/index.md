---
chapter: 第 133 章
id: CH133
volume: 第06卷-freebsd的核心技术革新
---

# 第 133 章 freebsd120的发布与基础设施革新

## 要点

- FreeBSD 12.0 将 OpenSSL 升级至 1.1.1a 版本（r340711），这是 OpenSSL 项目于 2018 年 9 月发布的 LTS（长期支持）版本，首次正式支持 TLS 1.3 协议（RFC 8446）。TLS 1.3 相比 TLS 1.2 具有显著改进：握手延迟从 2-RTT 减少至 1-RTT（0-RTT 可选）、移除了大量老旧不安全的密码套件（如 RSA 密钥交换、
- Meltdown/Spectre 对 FreeBSD 工程实践产生了深远影响：① 安全响应流程成熟化——FreeBSD Security Team 在此事件中展现了与 Intel、AMD、Linux/Windows/macOS 安全团队协调响应的能力，Security Officer Gordon Tetlow（戈登·泰特洛） 主导了披露前的协调工作；② 性能退化与优化权衡——KPTI 对系统调用
- 12.0 引入 **netdump(4)** 驱动与功能，允许内核崩溃（panic）时将 crash dump 通过网络传输到远程主机，而非仅写入本地交换分区。这对无本地存储的磁盘 less 系统、云环境虚拟机、嵌入式设备的内核调试具有重要意义。**netdump(4)** 由 John Baldwin（约翰·鲍德温）（jhb@）等人开发，FreeBSD Foundation 赞助。**netma
- FreeBSD 12.4-RELEASE 于 2022 年 12 月 5 日发布，是 stable/12 第五个也是最后一个版本（"fifth release"，12.x 系列终版）。核心更新：LLVM 工具链套件升级至 13.0.0（跨度极大——从 12.3 使用的 10.x 直接跳到 13.0.0）；OpenSSL 1.1.1q；OpenSSH 9.1p1；**ena(4)** Amazon
- FreeBSD 12.0-RELEASE 正式移除 PC98（NEC PC-9801/9821）与 armeb（32 位 big-endian ARM）架构支持。PC98 由 John Baldwin（约翰·鲍德温） 在 commit r312910（2017.2.1）从 -CURRENT 中移除，12.0 生效，结束了自 FreeBSD 2.2-RELEASE（1995）起 23 年的支持。PC

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_59] 卷“第06卷-freebsd的核心技术革新”第 133 章，匹配置信度 0.8，原因：关键词重合 2 项 + 加分 1
- [DB:references_fulltext:chapter_matches:chmatch_60] 卷“第06卷-freebsd的核心技术革新”第 133 章，匹配置信度 0.8，原因：关键词重合 2 项 + 加分 1
- [DB:references_fulltext:chapter_matches:chmatch_61] 卷“第06卷-freebsd的核心技术革新”第 133 章，匹配置信度 0.8，原因：关键词重合 2 项 + 加分 1
- [DB:references_fulltext:chapter_matches:chmatch_198] 卷“第06卷-freebsd的核心技术革新”第 133 章，匹配置信度 0.8，原因：关键词重合 2 项 + 加分 1
- [DB:references_fulltext:chapter_matches:chmatch_226] 卷“第06卷-freebsd的核心技术革新”第 133 章，匹配置信度 0.8，原因：关键词重合 2 项 + 加分 1
- [DB:references_fulltext:chapter_matches:chmatch_227] 卷“第06卷-freebsd的核心技术革新”第 133 章，匹配置信度 0.8，原因：关键词重合 2 项 + 加分 1
- [DB:references_fulltext:chapter_matches:chmatch_228] 卷“第06卷-freebsd的核心技术革新”第 133 章，匹配置信度 0.8，原因：关键词重合 2 项 + 加分 1
- [DB:references_fulltext:chapter_matches:chmatch_229] 卷“第06卷-freebsd的核心技术革新”第 133 章，匹配置信度 0.8，原因：关键词重合 2 项 + 加分 1
- [DB:references_fulltext:chapter_matches:chmatch_230] 卷“第06卷-freebsd的核心技术革新”第 133 章，匹配置信度 0.8，原因：关键词重合 2 项 + 加分 1
- [DB:references_fulltext:chapter_matches:chmatch_231] 卷“第06卷-freebsd的核心技术革新”第 133 章，匹配置信度 0.8，原因：关键词重合 2 项 + 加分 1

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- OpenSSL 1.1.1a 中的"a"后缀表示这是 1.1.1 系列的首个补丁版本（修复了 1.1.1 初始发布后的问题），不是预发布版本。TLS 1.3 在 12.0 发布时已获 IETF 批准（RFC 8446 于 2018 年 8 月发布），但浏览器与服务器生态系统的完全迁移花费了数年时间。FreeBSD 12.0 中 Kernel TLS（kTLS，TLS 加密/解密在内核中进行以降低 
- 部分评论认为“FreeBSD 的侧信道缓解不如 Linux 及时”——这一说法有一定道理，Linux 因商业发行版（Red Hat、Canonical 等）和大型云厂商（AWS、Google）的迫切需求而更快合入缓解补丁；FreeBSD 社区规模较小，合入时间相对晚数周但代码质量经过更充分审查。两者最终都实现了等效的缓解覆盖。微码更新加载在 FreeBSD 中需手动启用（通过 rc.conf 的 
- *netdump(4)** 在 12.0 为初始支持，支持的网卡驱动有一定限制（主要支持 **msk(4)**、**bnxt(4)**、**cxgbe(4)** 等部分驱动），并非所有网卡都可用于 netdump；netdump 使用 UDP 协议传输 dump 数据，依赖特定的 netdumpd 守护进程接收。
- 12.4 的 Clang 版本从 10.0.1（12.3）直接跳到 13.0.0，是 12.x 系列中跨度最大的编译器升级，因 stable/12 采用 MFC（Merge From Current）策略选择性合并重要更新；**dma(8)** 在 12.4 更新但 dma 并非默认 MTA——sendmail 仍是 12.x 默认邮件传输代理，dma 作为轻量级替代通过 mta = mailer
- PC98 退役 commit r312910 时间为 2017.2.1，生效于 2018.12.11（12.0 发布），间隔近两年因 12.0 多次延期。armeb 移除的具体 commit 号未在 Release Notes 中显式标注，但源码树中相关代码与 PC98 同期清理。

## 文献

- FreeBSD 12.0-RELEASE Release Notes Security/Contributed Software sections [Z]. 2018；Rescorla E. RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3 [S]. IETF, 2018；OpenSSL Project. OpenSSL 1.1.1 Release Notes [EB/OL]. openssl.org, 2018；commit r340711, r331279 [Z]. svn.freebsd.org. ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2018-2018 年间：47,408 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- FreeBSD Foundation Annual Report 2018 [R]；FreeBSD **cpucontrol(8)** Manual Page [Z]；FreeBSD Quarterly Status Reports 2018 [R].[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- FreeBSD **netdump(4)**/**netmap(4)** Manual Pages [Z]；FreeBSD 12.0-RELEASE Release Notes Userland/Kernel sections [Z]. 2018.[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- FreeBSD Release Engineering Team. FreeBSD 12.4-RELEASE Announcement [Z]. 2022-12-05；FreeBSD 12.4-RELEASE Release Notes [Z]. 2022；FreeBSD Security Information Unsupported Releases page [EB/OL]. freebsd.org/security/unsupported/；FreeBSD Project. release/12.4.0. freebsd-src 仓库 tag [DB/OL]. 2022-12-05T14:35:22-05:00. tag: release/12.4.0; commit: f2877ac4fb03265070b1cf97a07eb0e265bcaff9 ［A］FreeBSD 12.x 系列 release tag 间隔与发布偏差数据库验证（基于 **bsd_commits.db** `tags` 表）见下表。| 版本 | tag 日期 | 公告日期 | 偏差（日） | 间隔（日） | tagger | commit hash | 版本控制时代 || --- | --- | --- | --- | --- | --- | --- | --- || 12.0.0 | 2018-12-07 | 2018-12-11 | 4 | —— | Glen Barber | `4ba619efbdd2` | SVN || 12.1.0 | 2019-11-04 | 2019-11-04 | 0 | 332 | Glen Barber | `cc807f9e55c2` | SVN || 12.2.0 | 2020-10-27 | 2020-11-12 | 16 | 358 | Glen Barber | `1d21fe9cea3f` | SVN || 12.3.0 | 2021-12-03 | 2021-12-08 | 5 | 402 | Glen Barber | `70cb68e7a00a` | Git || 12.4.0 | 2022-12-05 | 2022-12-05 | 0 | 367 | Glen Barber | `f2877ac4fb03` | Git |12.x 系列平均 release 间隔约 365 日（约 12 个月），较 11.x 系列（平均约 340 日）略长，反映发布周期趋于年度化稳定节奏；12.2→12.3 间隔 402 日为系列最长，与 COVID-19 疫情影响及 12.3 献词 Ian Lepore 逝世事件相关；12.2 偏差 16 日为系列最大，反映发布前可能发生镜像重建；12.0-12.2 在 SVN 时代发布（tagger_date 由 2020 年 SVN-to-Git 迁移脚本回填），12.3-12.4 在 Git 时代发布（tagger_date 为 Git 原生元数据，可信度更高）。<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- commit r312910 [Z]. svn.freebsd.org, 2017；FreeBSD 12.0-RELEASE Release Notes Removed Features section [Z]. 2018. ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
