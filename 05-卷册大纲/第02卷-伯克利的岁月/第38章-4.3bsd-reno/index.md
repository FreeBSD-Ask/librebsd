---
chapter: 第 38 章
id: CH38
volume: 第02卷-伯克利的岁月
---

# 第 38 章 4.3bsd-reno

## 要点

- 4.3BSD-Reno（**1990 年 6 月** 磁带、**7 月 6 日** 正式公告）是明确标注为"test release"的过渡版本（"NOT intended to be used on production systems"），是 4.4BSD 开发过程中的中间快照而非终态版本；经 Keith Bostic 1990.7.6 原始公告逐段核实，Reno **实际包含的主要特性**
- Reno 在网络层引入了 SLIP 压缩（CSLIP, Van Jacobson（范·雅各布森） 实现）、NFS 性能改进、以及对 OSI 协议栈的实验性支持（受 NIST 资助）。OSI 支持虽未成为主流，但为 BSD 网络栈的多协议扩展提供了架构基石。
- 边缘贡献者的史料散见于源代码注释、邮件列表、USENIX 会议记录与公司内部档案，缺乏系统化传记，需通过多源交叉核对恢复身份，特别是 CCI 工程师与外部补丁提交者；[考据脚注] 4.3BSD-Reno 完整源代码树已由 Rick Copeland 与 Kirk McKusick 捐赠至 TUHS Unix Archive（www.tuhs.org/Archive/4BSD/Distributio
- Reno 时期的技术淘汰具有“过渡测试与生产淘汰并行”的特征——CSRG 在 Reno 中引入了 POSIX 兼容、NFS、OSI 网络、Kerberos 等生产可用特性，而新 VM 系统（Mach-derived）、LFS 等研究性组件在 Reno 时期处于开发中但实际集成至 4.4BSD；同期 SCCS 在 RCS 竞争下逐步退出学术场景主导地位，Tahoe 平台因 CCI 商业失败（STC/
- 1986-1990 年网络栈成熟度比较：4.3BSD > DEC Ultrix（直接基于 BSD） > HP-UX（BSD/SysV 混合） > AIX（SysV 为主） > System V Release 3（无 TCP/IP），BSD 在 TCP/IP 实现成熟度上领先，TCP/IP 在 **1990 年** SVR4 才成为标准| 操作系统 | 网络栈来源 | TCP/IP 成熟度 | S

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3713] 卷“第02卷-伯克利的岁月”第 38 章，匹配置信度 folder，原因：folder 第38章
- [DB:references_fulltext:chapter_matches:chmatch_3723] 卷“第02卷-伯克利的岁月”第 38 章，匹配置信度 folder，原因：folder 第38章
- [DB:references_fulltext:chapter_matches:chmatch_3813] 卷“第02卷-伯克利的岁月”第 38 章，匹配置信度 folder，原因：folder 第38章
- [DB:references_fulltext:chapter_matches:chmatch_3868] 卷“第02卷-伯克利的岁月”第 38 章，匹配置信度 folder，原因：folder 第38章
- [DB:references_fulltext:chapter_matches:chmatch_3910] 卷“第02卷-伯克利的岁月”第 38 章，匹配置信度 folder，原因：folder 第38章

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- Reno 是明确的"test release"而非 beta 或正式 release——公告原文"NOT intended to be used on production systems"、"interfaces in this release will change before 4.4BSD"、"do not expect applications ported to this releas
- 关于 Reno 的 OSI 支持需辨析——OSI 协议栈支持受 NIST 资助、以实验性姿态进入 Reno，最终未成主流，其“为 BSD 网络栈多协议扩展提供架构基石”的长期效应与“标准之战失败”的短期叙事构成张力；CSLIP 由 Van Jacobson 实现的时间与 4.3BSD-Tahoe/Reno 的归属须以发行说明为准。
- 部分贡献者使用用户名而非真名，需交叉核对以恢复身份，避免误归；TUHS Unix Archive 虽引用 Wikipedia 作为版本简介，但源代码树本身由 McKusick 一手捐赠，作为源代码档案可信
- Reno 是否真正“成功”在史料中评价不一——作为 test release 它成功获取了社区反馈并推动了 POSIX/NFS/OSI 等接口的稳定，但作为产品它不适合生产使用；原辨析中“LFS、Reno VM 等研究性组件”在 Reno 时期实际处于开发中而非“引入”，需精确区分开发时期与发布包含；Reno 时期（1990 年初）CSRG 正同步推进 Keith Bostic 主导的 AT&T 
- 成熟度比较需基于具体指标（吞吐量、延迟、稳定性），避免主观判断，需核对第三方基准测试

## 文献

- Bostic, K. (1990.7.6) "V1.90 (4.3BSD-Reno)"comp.archives 公告（gunkies.org 存档，一手发布文档，逐字段核对特性列表）；McKusick, M. K., Karels, M. J., Sklower, K., Fall, K., Teitelbaum, M., Bostic, K. (1989) "Current Research by The Computer Systems Research Group of Berkeley"Proc. European UNIX Users Group (beyond43.pdf)；McKusick, M. K., Bostic, K., Karels, M. J., Quarterman, J. S. (1996) 《The Design and Implementation of the 4.4BSD Operating System》Addison-Wesley, ISBN 0-201-54979-4（4.4BSD 权威参考，确认新 VM 在 4.4BSD 中引入）；CSRG 贡献者名单（netbsd.org/people/CSRG-contrib.html） ［A］
- Reno 发行说明； CSRG OSI 文档 ［A］## 史料考据补充（2026-08-04 任务3 联网核验）> 主题：4.3BSD Reno 的网络改进与 OSI 协议栈探索
- 4.3BSD Tahoe/Reno 源代码注释（TUHS Unix Archive，www.tuhs.org/Archive/4BSD/Distributions/4.3BSD-Reno/，Rick Copeland 与 Kirk McKusick 捐赠）；CSRG 邮件列表存档（伯克利 Bancroft 图书馆）；USENIX 会议论文集（1986-1990） ［A］
- Bostic, K. (1990.7.6) "V1.90 (4.3BSD-Reno)"comp.archives 公告；McKusick, M. K. (1999) "Twenty Years of Berkeley Unix"；McKusick et al. (1996) 《The Design and Implementation of the 4.4BSD Operating System》ISBN 0-201-54979-4；CSRG 1990 年度技术报告 ［B］；资料数据库.db 文献计量学分析报告（`03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/文献计量学分析.md` Task 22，2026-07-27）；卷章数据映射表（`03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/卷章数据映射.md` 第二卷第 19 章）---
- CSRG 网络栈性能报告（1988）；各厂商 TCP/IP 性能基准测试（1986-1990）；Salus, P. (1994) "A Quarter Century of UNIX"[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- 4.4BSD/4.4BSD-Lite Release Notes (1994)；FreeBSD 1.0-3.x Release Notes；NetBSD 早期版本 Release Notes；Ylönen, T. (1995) SSH 1.0 发布记录；Kohl, J. & Neuman, C. (1993) RFC 1510"The Kerberos Network Authentication Service (V5)"；OpenSSH 发布记录；FreeBSD 5.x Release Notes (2003) ［A］
