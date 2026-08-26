---
chapter: 第 177 章
id: CH177
volume: 第09卷-netbsd的历史
---

# 第 177 章 netbsd嵌入式市场与外部批评

## 要点

- 嵌入式部署记录与硬件文档考据——NetBSD 嵌入式部署记录（ports/* 目录）与硬件文档是研究嵌入式应用的一手史料；考据需对照多源档案交叉验证
- 批评原始发言与邮件列表考据——批评 NetBSD 的原始发言与邮件列表讨论是研究外部批评的一手史料；考据需对照多源档案交叉验证
- NetBSD 缺乏商业支持体系是嵌入式市场应用的障碍；2000 年 Wasabi Systems 成立，提供 NetBSD 商业支持、定制开发、咨询与培训；Wasabi 模式借鉴 Red Hat 商业模式但规模较小，主要客户为嵌入式设备厂商；Wasabi 贡献了 NetBSD ARM 移植、嵌入式优化等代码；Wasabi 模式是 NetBSD 早期商业-社区平衡的尝试，但因规模有限未能持续
- 各项目发布数据与市场份额考据——NetBSD、FreeBSD、OpenBSD、Linux 在 1994-2004 年的发布数据与市场份额；考据需对照多源档案交叉验证
- NetBSD 1.x 时期内核权限边界缺陷在嵌入式场景下具有特殊影响——NetBSD-SA1998-005（**mmap(2)** 设备驱动权限检查缺陷，本地用户可映射设备内存访问任意物理内存）、NetBSD-SA2000-001（**procfs(5)** 权限检查缺陷，本地用户可读取其他进程内存映射）、NetBSD-SA2001-009（SUID 程序执行与 **ptrace(2)** 竞态条

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3996] 卷“第09卷-netbsd的历史”第 177 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 部署记录的完整性需考据——部分部署可能未被完整记录；需对照多源档案核实
- Wasabi 成立的具体时间存在叙事分歧——部分资料称 2000 年，部分称 1999 年，需对照公司注册档案核验；Wasabi 衰退的具体时间与原因需考据。经 bsd_commits.db netbsd-src 仓库 commits 表验证：Wasabi 相关 commit 最早可追溯至 2000-10-24（thorpej 性能计数器工具，署名 From Frank），2001-11-24 j
- 市场份额数据的具体口径需考据——不同统计口径可能差异较大；需对照多源档案核实
- 嵌入式设备是否普遍以 root 运行单一应用须考据——Dreamcast、Zaurus 等设备的具体权限配置须对照设备文档核验；“远程 → 本地 → 内核” 攻击链在嵌入式场景下的实际案例须考据——公开攻击案例可能有限，须对照安全研究报告核验；he 的 procfs 修复 commit `a685050c3f4b3919cc804eea7792397efc311b4e` 标注 "Fix a cri

## 文献

- NetBSD 嵌入式史料分析[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:netbsd.duckdb -->> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1998-2004 年间：549,070 次提交。> 仓库总览：1,999,412 次提交，4,754 位贡献者，1992-07-13 至 2026-08-24。
- NetBSD 外部批评史料分析[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:netbsd.duckdb -->> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，4,754 位贡献者，1992-07-13 至 2026-08-24。
- Wasabi Systems 公司档案；NetBSD Foundation 与 Wasabi 合作记录；Wasabi 贡献的 NetBSD commit log；thorpej. A program for reading performance counters. netbsd-src 仓库 [DB/OL]. 2000-10-24T23:54:31Z；simonb. Add a port to IBM's PPC405GP Reference Board. netbsd-src 仓库 [DB/OL]. 2001-06-13T06:01:44Z；jhawk. Wasabi copyright notice update. netbsd-src 仓库 [DB/OL]. 2001-11-24T23:53:18Z；origin/netbsd-1-5. netbsd-src 仓库 branch [DB/OL]. 2004-12-10T23:08:26Z. commit: 1c43a6ba5391；origin/netbsd-1-6. netbsd-src 仓库 branch [DB/OL]. 2006-06-01T06:03:17Z. commit: e5a9a0024746 ［A］---<!-- DB_REF:netbsd.duckdb -->> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，4,754 位贡献者，1992-07-13 至 2026-08-24。
- BSD 与 Linux 市场份额史料分析[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1994-2004 年间：279,033 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- NetBSD-SA1998-005、NetBSD-SA2000-001、NetBSD-SA2001-009 公告原文；bsd_commits.db netbsd-src 仓库 he procfs 修复 commit ［A］<!-- DB_REF:netbsd.duckdb -->> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，4,754 位贡献者，1992-07-13 至 2026-08-24。
