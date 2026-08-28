---
chapter: 第 188 章
id: CH188
volume: 第09卷-netbsd的历史
---

# 第 188 章 netbsd-7-0与arm生态的深度支持

## 要点

- NetBSD 7.0（**2015.9**）改进 ARM 多核支持，支持 Cortex-A15/A57 等多核 SoC；~~引入 big.LITTLE 架构支持~~（经 bsd_commits.db netbsd-src 仓库 commits 表查询 `message_subject LIKE '%big.LITTLE%' OR '%big_little%' OR '%biglittle%'` 未
- NetBSD ARM 平台 commit 记录是研究 ARM 移植演进的核心史料；Jared McNeill、Ryo Shimizu 等是 ARM 移植主要贡献者；硬件文档考据需对照 ARM 架构参考手册与 SoC 厂商文档
- NetBSD 7.0（2015.10）改进内核时间戳从 32-bit 到 64-bit 的迁移，应对 2038 年问题（Y2038）；旧 32-bit time_t 在文件系统、网络协议、用户态 ABI 中广泛存在，7.0 引入 64-bit time_t 内核支持；此改进早于 FreeBSD 与 OpenBSD 的类似迁移，体现 NetBSD 在 Y2038 准备上的前瞻性
- 2015 年 ARM 成为操作系统竞争焦点：Linux 4.x 以生态规模领先，NetBSD 7.0 以平台广度与 SMP 提升立足，FreeBSD 10/11 在嵌入式产品落地，OpenBSD 5.8 安全利基，Windows 10 试探 ARM；NetBSD 7.0 以 “多核 + ARM 深度” 强化可移植哲学。
- NetBSD 7.x 周期其余 High 级别 CVE 包括——CVE-2017-12836（CVSS v3 7.5 High，注入漏洞，commit `74e8c71cd1136230728133034816cf03b1f4af1f`，2017-08-22）、CVE-2018-5732（CVSS v3 7.5 High，ISC DHCP 缓冲区溢出，commit `097731dea099250

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

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- NetBSD ARM 多核支持与 Linux ARM 多核支持的成熟度对比缺乏权威基准——需对照同硬件测试核验。经 netbsd.db netbsd-src 仓库 commits 表验证：aarch64 后端于 2013.2.4 由 joerg 首次引入（LLVM/Clang snapshot r174288），AARCH64 定义于 2013.10.29 由 matt 添加，latent AAr
- NetBSD ARM 平台支持列表在不同来源中可能略有出入——需对照 NetBSD/doc/PLATFORMS 文件核验；部分老 ARM 平台（如 StrongARM）是否仍在维护需考据
- 7.0 是否完整迁移到 64-bit time_t 在不同叙事中存在分歧——内核侧与用户态侧进度可能不同，需对照源码核验；与 FreeBSD/OpenBSD Y2038 准备的对比需考据；32-bit time_t 在 7.0 中是否仍可作为兼容选项保留需考据
- CVE-2017-12836 的 “注入漏洞” 机制须对照 NVD 条目核验具体注入类型（SQL 注入、命令注入、代码注入等）——netbsd.db 仅标注 “注入” 而未细分，须对照 NVD CWE 分类核验；CVE-2018-5732 与 CVE-2018-5733 由同一 commit 修复的论断须对照 commit subject 核验——该 commit 可能同时修复 ISC DHCP

## 文献

- NetBSD CVS 仓库 arm 部分；ARM Architecture Reference Manual；tech-port-arm 邮件列表 ［A］<!-- DB_REF:netbsd.duckdb -->> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2015-2015 年间：82,041 次提交。> 仓库总览：1,999,412 次提交，4,754 位贡献者，1992-07-13 至 2026-08-24。
- NetBSD 7.0 Release Notes；tech-kern 邮件列表；Y2038 问题文档 ［A］<!-- DB_REF:netbsd.duckdb -->> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，4,754 位贡献者，1992-07-13 至 2026-08-24。
- NetBSD. 7.0 Release Notes [EB/OL]；ARM 生态史料。［B］<!-- DB_REF:netbsd.duckdb -->> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2015-2015 年间：82,041 次提交。> 仓库总览：1,999,412 次提交，4,754 位贡献者，1992-07-13 至 2026-08-24。
- netbsd.db netbsd-src 仓库 commit `74e8c71cd1136230728133034816cf03b1f4af1f`、`097731dea099250bc460a975c393fc370c283a95`；NVD CVE-2017-12836、CVE-2018-5732、CVE-2018-5733 条目；ISC DHCP 安全公告 ［A］<!-- DB_REF:netbsd.duckdb -->> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2017-2017 年间：52,858 次提交。> 仓库总览：1,999,412 次提交，4,754 位贡献者，1992-07-13 至 2026-08-24。

<!-- PODCAST_MINE v20260827 -->
<!-- Chapter: 第188章-netbsd-7-0与arm生态的深度支持 -->

## 要点（播客口述史提取）
- Oh, exactly. And I was also happy to do a couple of Google Summary of Code programs. So actually, the first one I applied as a student, I was still enrolled as a student, and I applied to do something with FreeBSD.
- But when he switched to FreeBSD, he didn't have a single failure for like a year.
- I think it built on the engineering culture and excellence that was also present in the FreeBSD project.
- And I started giving talks at conferences in Russia about what FreeBSD is, but also what my workflow as a sysadmin is.
- And talking about our solutions, our view towards how systems engineering in relation to FreeBSD should probably be evolved.
- How did you first get introduced to and get involved with the BSDs?
- and currently they only support open bsd as a guest well that's that's how we started on the
- and so of course we're back a couple versions of freebsd he was trying to boot freebsd 11 stable

## 史料（播客提及）
- [BSD Now EP108 @ 1184.3199462890625] Oh, exactly. And I was also happy to do a couple of Google Summary of Code programs. So actually, the first one I applied as a student, I was still enrolled as a student, and I applied to do something with FreeBSD.
- [BSD Now EP108 @ 1517.9400634765625] One was, I think, to Brooks Davis, who was running a big FreeBSD cluster at Aerospace Corporation in America.
- [BSD Now EP108 @ 1590.0399169921875] He didn't need InfiniBand that much, which wasn't present in FreeBSD at the time.
- [BSD Now EP108 @ 1680.8800048828125] I think it built on the engineering culture and excellence that was also present in the FreeBSD project.
- [BSD Now EP108 @ 2726.239990234375] I think he's currently a NetBSD package source committer.

## 史观（播客当事人观点与总纲映射）
- [BSD Now EP108 @ 1184.3199462890625] Oh, exactly. And I was also happy to do a couple of Google Summary of Code programs. So actually, the first one I applied as a student, I was still enrolled as a student, and I applied to do something with FreeBSD.
- [BSD Now EP108 @ 1517.9400634765625] One was, I think, to Brooks Davis, who was running a big FreeBSD cluster at Aerospace Corporation in America.
  → 史观映射：总纲20——历史地理塑造思想土壤
- [BSD Now EP108 @ 1590.0399169921875] He didn't need InfiniBand that much, which wasn't present in FreeBSD at the time.
  → 史观映射：总纲18——时间是一种形式主义
- [BSD Now EP108 @ 1680.8800048828125] I think it built on the engineering culture and excellence that was also present in the FreeBSD project.
- [BSD Now EP108 @ 2726.239990234375] I think he's currently a NetBSD package source committer.
- [BSD Now EP108 @ 2764.579833984375] That was one of the reasons for me really diving deep into going to BSD days and EuroBSDCon for a few years in succession and BSDCAN.
- [BSD Now EP108 @ 2990.31982421875] and server providers to actually get support for FreeBSD
- [BSD Now EP108 @ 3793.239990234375] And it turned out that every one of them was perfectly mountable and readable under FreeBSD.

## 辨析（播客争议与存疑点）
- [存疑脚注] [BSD Now EP164 @ 4212.77978515625] on the other free bsd machine on the other side coming through um and you know so it is possible
- [存疑脚注] [BSD Now EP131 @ 1509.5999755859375] FreeBSD split apart from OpenBSD and NetBSD
- [存疑脚注] [BSD Now EP131 @ 1589.8798828125] Mind you, they said them back in 2009, but on the other hand, I can't imagine OpenBSD would have dropped what they were doing,
- [存疑脚注] [BSD Now EP428 @ 135.739990234375] starting back in October of 1995 as a fork of NetBSD.

## 文献（播客参考条目）
- [BSD Now EP108] Pennington J. BSD Now: 108: ServeUp BSD[EB/OL]. (2015-09-23)[2026-08-15]. https://www.bsdnow.tv/108.
- [BSD Now EP164] Pennington J. BSD Now: 164: Virtualized COW / PI?[EB/OL]. (2016-10-19)[2026-08-15]. https://www.bsdnow.tv/164.
- [BSD Now EP131] Pennington J. BSD Now: 131: BSD behind the chalkboard[EB/OL]. (2016-03-02)[2026-08-15]. https://www.bsdnow.tv/131.
- [BSD Now EP47] Pennington J. BSD Now: 47: DES Challenge IV[EB/OL]. (2014-07-23)[2026-08-15]. https://www.bsdnow.tv/47.
- [BSD Now EP201] Pennington J. BSD Now: 201: Skip grep, use awk[EB/OL]. (2017-07-05)[2026-08-15]. https://www.bsdnow.tv/201.
- [BSD Now EP83] Pennington J. BSD Now: 83: woN DSB[EB/OL]. (2015-04-01)[2026-08-15]. https://www.bsdnow.tv/83.
- [BSD Now EP127] Pennington J. BSD Now: 127: DNS, Black Holes & Willem[EB/OL]. (2016-02-03)[2026-08-15]. https://www.bsdnow.tv/127.
- [BSD Now EP428] Pennington J. BSD Now: 428: Cult of BSD[EB/OL]. (2021-11-11)[2026-08-15]. https://www.bsdnow.tv/428.

<!-- /PODCAST_MINE -->