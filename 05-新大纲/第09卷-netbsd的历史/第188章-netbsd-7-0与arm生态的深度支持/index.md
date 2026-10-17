---
chapter: 第 188 章
id: CH188
volume: 第09卷-netbsd的历史
---

# 第 188 章 NetBSD 7.0 与 ARM 生态的深度支持

## 要点

- NetBSD 7.0（2015-09-25 发布）改进 ARM 多核支持，支持 Cortex-A15/A57 等多核 SoC；~~引入 big.LITTLE 架构支持~~（经 netbsd.duckdb netbsd-src 仓库 commits 表查询 `message_subject LIKE '%big.LITTLE%' OR '%big_little%' OR '%biglittle%'` 未命中，该说法在提交层面无据）
- NetBSD ARM 平台 commit 记录是研究 ARM 移植演进的核心史料；Jared McNeill、Ryo Shimizu 等是 ARM 移植主要贡献者；硬件文档考据需对照 ARM 架构参考手册与 SoC 厂商文档
- NetBSD 7.0（2015-09-25 发布）改进内核时间戳从 32-bit 到 64-bit 的迁移，应对 2038 年问题（Y2038）；旧 32-bit time_t 在文件系统、网络协议、用户态 ABI 中广泛存在，7.0 引入 64-bit time_t 内核支持；此改进早于 FreeBSD 与 OpenBSD 的类似迁移，体现 NetBSD 在 Y2038 准备上的前瞻性
- 2015 年 ARM 成为操作系统竞争焦点：Linux 4.x 以生态规模领先，NetBSD 7.0 以平台广度与 SMP 提升立足，FreeBSD 10/11 在嵌入式产品落地，OpenBSD 5.8 安全利基，Windows 10 试探 ARM；NetBSD 7.0 以 “多核 + ARM 深度” 强化可移植哲学。
- NetBSD 7.x 周期其余 High 级别 CVE 包括——CVE-2017-12836（CVSS v3 7.5 High，注入漏洞，commit `74e8c71cd1136230728133034816cf03b1f4af1f`，2017-08-22）、CVE-2018-5732（CVSS v3 7.5 High，ISC DHCP 缓冲区溢出，commit `097731dea099250bc460a975c393fc370c283a95`）。

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4002] 卷“第09卷-netbsd的历史”第 188 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:bsdnow_podcast:outline_mappings:om_10427] BSD Now 第 676 期，匹配 CH188 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10513] BSD Now 第 661 期，匹配 CH188 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10528] BSD Now 第 656 期，匹配 CH188 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10535] BSD Now 第 655 期，匹配 CH188 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10543] BSD Now 第 654 期，匹配 CH188 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10558] BSD Now 第 652 期，匹配 CH188 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10568] BSD Now 第 651 期，匹配 CH188 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10592] BSD Now 第 645 期，匹配 CH188 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10610] BSD Now 第 642 期，匹配 CH188 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10634] BSD Now 第 638 期，匹配 CH188 章，关联度 1.0

## 史观

- 总纲第 8 条——本体论上各方平等：本章将 NetBSD 7.0 与 Linux 4.x、FreeBSD 10/11、OpenBSD 5.8、Windows 10 的 ARM 布局并置考察，不以单一系统路线为叙事中心
- 总纲第 10 条——动手者创造历史：Jared McNeill、Ryo Shimizu 等移植一线贡献者的提交记录，构成本章 ARM 支持演进的核心史料
- 总纲第 5 条——没有必然性，只有偶然性：big.LITTLE 架构支持经提交检索考据未获支撑，ARM 多核支持的落地系于具体贡献者与具体硬件条件
- 总纲第 3 条——不存在进步，只有权力再分配：2015 年 ARM 竞争焦点下 NetBSD 7.0 以平台广度立足，呈现为竞争格局中的位置流转而非线性领先
- 总纲第 9 条——经验优先：本章论断以 netbsd.duckdb commits 表、NVD 条目与官方发布公告为据，优先采用当事人一手材料

## 辨析

- NetBSD ARM 多核支持与 Linux ARM 多核支持的成熟度对比缺乏权威基准——需对照同硬件测试核验。经 netbsd.duckdb netbsd-src 仓库 commits 表验证：aarch64 后端于 2013.2.4 由 joerg 首次引入（LLVM/Clang snapshot r174288），AARCH64 定义于 2013.10.29 由 matt 添加，latent ARM 支持代码的后续演进节点须按 commits 表时间线另行检索核验
- NetBSD ARM 平台支持列表在不同来源中可能略有出入——需对照 NetBSD/doc/PLATFORMS 文件核验；部分老 ARM 平台（如 StrongARM）是否仍在维护需考据
- 7.0 是否完整迁移到 64-bit time_t 在不同叙事中存在分歧——内核侧与用户态侧进度可能不同，需对照源码核验；与 FreeBSD/OpenBSD Y2038 准备的对比需考据；32-bit time_t 在 7.0 中是否仍可作为兼容选项保留需考据
- CVE-2017-12836 的 “注入漏洞” 机制须对照 NVD 条目核验具体注入类型（SQL 注入、命令注入、代码注入等）——netbsd.duckdb 仅标注 “注入” 而未细分，须对照 NVD CWE 分类核验；CVE-2018-5732 与 CVE-2018-5733 由同一 commit 修复的论断须对照 commit subject 核验——该 commit 可能同时修复 ISC DHCP

## 文献

- NetBSD CVS 仓库 arm 部分；ARM Architecture Reference Manual；tech-port-arm 邮件列表 ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2015-2015 年间：82,041 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- NetBSD 7.0 Release Notes；tech-kern 邮件列表；Y2038 问题文档 ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- NetBSD. 7.0 Release Notes [EB/OL]；NetBSD 7.0 官方发布公告（2015-09-25），**www.NetBSD.org/releases/formal-7/NetBSD-7.0.html**；ARM 生态史料。［B］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2015-2015 年间：82,041 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- netbsd.duckdb netbsd-src 仓库 commit `74e8c71cd1136230728133034816cf03b1f4af1f`、`097731dea099250bc460a975c393fc370c283a95`；NVD CVE-2017-12836、CVE-2018-5732、CVE-2018-5733 条目；ISC DHCP 安全公告 ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2017-2017 年间：52,858 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
