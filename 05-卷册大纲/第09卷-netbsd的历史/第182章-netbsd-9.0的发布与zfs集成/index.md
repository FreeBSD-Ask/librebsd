---
chapter: 第 182 章
id: CH182
volume: 第09卷-netbsd的历史
---

# 第 182 章 netbsd-9.0的发布与zfs集成

## 要点

- NetBSD 9.0（**2020.2.14**）引入实验性 ZFS 支持，源于 OpenZFS 移植；工程挑战包括 SPL（Solaris Porting Layer）适配、内存管理（NetBSD UVM vs Solaris VM）、并发原语转换；ZFS 在 NetBSD 上的稳定性与性能不及 FreeBSD OpenZFS
- NetBSD 9.0 Release Notes 与 CVS commit log 是研究 9.0 开发的核心史料；9.0 发布周期约 1 年 7 个月（8.0 于 2018.7.17 发布，9.0 于 2020.2.14 发布，后续 9.1/9.2/9.3/9.4 持续维护）；commit 记录反映 ZFS、GPU、网络协议栈的开发节奏
- NetBSD 9.0（**2020.2.14**）改进文件系统支持，ext2fs 的进一步改进支持更多 ext4 特性；旧 FFS 作为默认文件系统延续，新文件系统作为可选；此改进让 NetBSD 在现代 Linux 文件系统互操作上获得能力。~~原叙事中“NetBSD 9.0 引入对 F2FS（Flash-Friendly File System）的实验性支持”声明未得到代码级确认~~——bsd
- 2020 年 CoW 文件系统格局：FreeBSD 12/13 与 NetBSD 9.0 深度整合 OpenZFS，Linux 经 ZoL 树外提供，illumos/Solaris 持 ZFS 原创，OpenBSD 坚持 FFS/softraid，Windows 用 ReFS；NetBSD 9.0 的 ZFS 补齐使其存储能力与 FreeBSD 对齐。
- 9.x 周期 NetBSD Security Officer Team 的 18 个 SA 在数量、节奏、覆盖面三个维度均显著低于 FreeBSD 14.x 周期同时段——9.x 周期约 5 年（2020.2 至 2024+）18 个 SA，FreeBSD 14.x 周期不足 3 年（2023.11 至 2026.7）80 个 SA，年化速率 NetBSD 约 3.6 SA/年、FreeBSD 约

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4090] 卷“第09卷-netbsd的历史”第 182 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- NetBSD ZFS 与 FreeBSD OpenZFS 的关系存在叙事分歧——部分资料称 NetBSD 直接移植 FreeBSD OpenZFS，部分称通过 OpenZFS 仓库共享代码，需对照源码核验。经 netbsd.db netbsd-src 仓库 commits 表验证：NetBSD ZFS 代码由 chs（Chuck Silvers）于 2018-05-28 从 FreeBSD SVN
- 先前叙事中称“9.0 发布日期 2020.5”系误传——NetBSD 官方发布页面（netbsd.org/releases/formal-9/NetBSD-9.0.html）明确为 2020.2.14；9.0 发布周期实际约 1 年 7 个月而非 2.5 年；9.0 的实际功能完整性需对照 release tarball 核验 [考据完成：2026-07-28 该处存疑标注属史料缺口，须待原始档案
- 9.0 ext2fs 改进支持更多 ext4 特性的具体范围需对照源码核验。重要修正：经 bsd_commits.db netbsd-src 仓库 commits 表验证：查询 `message_subject LIKE '%f2fs%' OR message_subject LIKE '%F2FS%'` 结果为空，原叙事中“NetBSD 9.0 引入对 F2FS 的实验性支持”声明暂未得到代码级
- ZFS 的 BSD 整合度高，证明 BSD 许可对大型存储栈的友好。
- *数量对比的辨析**：9.x 周期 18 个 SA 与 FreeBSD 14.x 周期 80 个 SA 的对比须考虑四个因素：其一，NetBSD base 中贡献组件显著少于 FreeBSD base（无 Heimdal、libarchive、xz、sendmail→dma 等），贡献组件漏洞面更小；其二，NetBSD 9.x 周期 OpenSSL 仍使用 1.1.1 系列（保守策略未跟随 Ope

## 文献

- NetBSD 9.0 史料分析；tech-release 邮件列表；NetBSD 官方发布历史页面（<https://www.netbsd.org/releases/formal.html>） ［A］<!-- DB_REF:netbsd.duckdb -->> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2020-2020 年间：34,930 次提交。> 仓库总览：1,999,412 次提交，4,754 位贡献者，1992-07-13 至 2026-08-24。
- NetBSD 9.0 Release Notes；tech-file-system 邮件列表；ext2fs/ext4 设计文档 ［A］<!-- DB_REF:netbsd.duckdb -->> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，4,754 位贡献者，1992-07-13 至 2026-08-24。
- McKusick M K, Neville-Neil G. The Design and Implementation of the FreeBSD Operating System [M]. 2nd ed. Addison-Wesley, 2015. ［B］<!-- DB_REF:netbsd.duckdb -->> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2020-2020 年间：34,930 次提交。> 仓库总览：1,999,412 次提交，4,754 位贡献者，1992-07-13 至 2026-08-24。
- NetBSD Project. NetBSD Security Advisories Archive [EB/OL]. (2020-2024)[2026-07-22]. <https://www.netbsd.org/support/security/advisory.html>; NetBSD Project. NetBSD Security Officer Team — SA Release Process [EB/OL]. [2026-07-22]. <https://www.netbsd.org/support/security/>; FreeBSD Security Team. FreeBSD Security Advisories Archive [EB/OL]. (2023-2026)[2026-07-22]. <https://www.freebsd.org/security/advisories/>; OpenBSD Project. OpenBSD Errata Patches [EB/OL]. [2026-07-22]. <https://www.openbsd.org/errata.html>; NetBSD Project. bsd_commits.db — netbsd-src SA pull-up commits [DB/OL]. 2026-07-22. `SQL: SELECT commit_hash, author_date, author_name, message_subject FROM commits WHERE repo_name='netbsd-src' AND author_date>='2020-02-14' AND author_date<'2024-12-31' AND (message_subject LIKE '%SA%' OR message_subject LIKE '%pull-up%' OR message_subject LIKE '%ticket%') ORDER BY author_date ASC` ［A］<!-- DB_REF:netbsd.duckdb -->> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，4,754 位贡献者，1992-07-13 至 2026-08-24。
