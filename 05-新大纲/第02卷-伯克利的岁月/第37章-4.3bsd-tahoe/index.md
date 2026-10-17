---
chapter: 第 37 章
id: CH37
volume: 第02卷-伯克利的岁月
---

# 第 37 章 4.3bsd-tahoe

## 要点

- **CCI Power 6/32 硬件规格**（经 gunkies.org Computer History Wiki 与 4.3BSD-Reno/src/share/doc/smm/01.setup/tahoe/1.t 一手 setup 文档交叉验证）：① **CPU 架构**——TTL（晶体管-晶体管逻辑）离散实现，非微处理器；32 位寄存器组（r0—r13 通用寄存器、r14 栈指针 sp、
- **缺口 2ah 原标题 “Tahoe 的虚拟内存重写” 存在前提错误**——4.3BSD-Tahoe（1988.6）**并未进行虚拟内存重写**，Tahoe 时期虚拟内存方面的工作仅为机器相关虚拟内存代码的分离（`tahoe/vm_machdep.c` 9969 字节，将 VAX 特有的虚拟内存机器相关部分从 `sys/` 分离到 `tahoe/`），而非虚拟内存子系统的架构重写；4.3BSD-
- 4.2BSD/4.3BSD 早期 TCP/IP 实现采用简单窗口控制——发送方按接收方通告窗口大小发送数据，未考虑网络中间路由器的拥塞状态，导致网络拥塞时大量数据包丢失与重传（即“congestion collapse”现象，**1986 年 10 月** 互联网首次大规模拥塞崩溃事件发生，**LBL Lawrence Berkeley Laboratory 至 UC Berkeley 间 32**
- OS/2 是 IBM 与微软为 80286/386 平台开发的“下一代”PC 操作系统，1.0（1987）为文本模式、1.1（1988）引入 Presentation Manager 图形界面与保护模式多任务；它面向比 MS-DOS 更强的硬件，却在与 Windows 3.0（1990）的竞争中失利，未能取代 DOS 成为 PC 标准。
- 4.3BSD-Tahoe（1988 年 6 月发布）早于 Morris 蠕虫（1988 年 11 月 2 日晚 8:30 EST）约 5 个月，Tahoe 发布时 **sendmail(8)** DEBUG 命令后门、**fingerd(8)** 缓冲区溢出、**rshd(8)** 信任传递三类漏洞仍以 4.3BSD 时期的形态存在，Tahoe 未包含任何蠕虫修复补丁；Morris 蠕虫爆发后 C

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_1550] 卷“第02卷-伯克利的岁月”第 37 章，匹配置信度 0.9，原因：关键词搜索下载文献，标题含章节主题

## 史观

总纲第 5 条——没有必然性，只有偶然性：Tahoe 硬件（CCI Power 6/32）的商业失败使 4.3BSD-Tahoe 成为短命移植（与 37.2 映射一致）；总纲第 9 条——经验优先：Tahoe 组的网络栈演进以 CSRG 工程师当事人叙述为据（与 37.4/37.9 映射一致）；总纲第 4 条——分离聚合是永恒规律：Tahoe/Reno 双线发布为 BSD 内部的分合（与 37.6 映射一致）；总纲第 22 条——知识注定过时：Tahoe 移植经验为后续平台移植方法论奠基（与 37.10 映射一致）。子节级映射详见 37.1-37.10 各节史观字段

## 辨析

- 分离工作与多分支形成的因果关系需谨慎判断，避免线性因果，386BSD 的 Bill Jolitz 个人努力亦是关键因素
- ① **“Tahoe 虚拟内存重写” 表述的前提错误**——经 McKusick 1999 一手记载与 TUHS 源代码目录结构交叉验证，4.3BSD-Tahoe 未进行虚拟内存重写，Tahoe 时期 VM 工作仅为机器相关代码分离（`tahoe/vm_machdep.c` 与 `tahoe/vmparam.h`），虚拟内存子系统架构与 4.3BSD 无本质差异；② **“重写前后架构对比” 的请**
- Van Jacobson 1988 年 SIGCOMM 论文与 4.3BSD-Tahoe 集成的时间关系——论文 1988 年 8 月 26-30 日 SIGCOMM 发表（论文 PDF 版本为 1988 年 11 月修订版）〔待核：原文截断，后文待回源〕
- OS/2 与 BSD 无直接竞争——OS/2 瞄准 286/386 PC 的企业市场，BSD 固守 VAX/科研；OS/2 真正的对手是 Windows 与 DOS，而非 UNIX 变体。
- Tahoe 与 Morris 蠕虫的时序关系须严格区分“Tahoe 发布时漏洞存在”与“Tahoe 引入漏洞”——三类漏洞源自 4.2BSD（1983）网络栈引入，Tahoe 仅继承而非引入，须避免将漏洞归咎于 Tahoe；蠕虫修复补丁以独立补丁形式分发而非集成入 Tahoe 版本，须区分“补丁分发”与“版本集成”——Tahoe 本身作为已发布版本未回溯集成补丁，用户需手动应用；Net/1 发布时

## 文献

- Jolitz, B. (1991) “Porting UNIX to the 386”；NetBSD/FreeBSD/OpenBSD Release Notes；McKusick, K. (1999) “Twenty Years of Berkeley Unix” ［B］## 36.1.5 CCI Power 6/32 硬件规格与 Tahoe 适配代码规模
- McKusick, M. K. (1999) “Twenty Years of Berkeley Unix” O'Reilly Open Sources；4.3BSD-Tahoe/usr/src/sys/tahoe/vm_machdep.c（TUHS）；4.3BSD-Tahoe/usr/src/sys/tahoe/vmparam.h（TUHS）；4.3BSD-Tahoe/usr/src/sys/vax/vm_machdep.c（TUHS，对比基准）；4.3BSD-Tahoe/usr/src/sys/sys/vm_*.c（TUHS，机器无关 VM 代码） ［A］
- Jacobson, V. & Karels, M. J. (1988) “Congestion Avoidance and Control”SIGCOMM（Stanford 1988.8.26-30, DOI: 10.1145/52325.52356）；4.2BSD/4.3BSD TCP/IP 源代码；4.3BSD-Tahoe TCP/IP 源代码；RFC 1122 (1989)；RFC 2581 (1999)；Karels, M., McKusick, K., Bostic, K. (1988-06) 4.3BSD-Tahoe 公告（tuhs.org 一手）；McKusick, K. (1999) “Twenty Years of Berkeley Unix”；统计分析报告 `03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/文献计量学分析.md` Task 22；卷章数据映射 `03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/卷章数据映射.md` 第二卷第 18 章 ［A］
- IBM. OS/2 1.1 Technical Reference [Z]. 1988；Dunn R. The OS/2 War [M]. 1994. ［C］
- 4.3BSD-Tahoe Release Notes (1988.6)；BSD 修复补丁（1988.11.8）；Spafford, E. (1988/1989) “The Internet Worm Program”Purdue CSD-TR-823；CERT/CC CA-1988:01；Bostic, K. (1988.12.7) Net/1 USENET 公告（gunkies.org 存档）；Net/1 源代码；McKusick, K. (1999) “Twenty Years of Berkeley Unix” ［A］
- 4.3BSD Tahoe Release Notes（1988.6）；Jacobson, V. & Karels, M. J. (1988) “Congestion Avoidance and Control”；Karels, M., McKusick, K., Bostic, K. (1988-06) 4.3BSD-Tahoe Release 公告（tuhs.org/Usenet/comp.sys.tahoe/1988-June/000067.html）；CSRG 年度报告（1988）；McKusick, M. K. (1999) "Twenty Years of Berkeley Unix: From AT&T-Owned to Freely Redistributable“, in DiBona C, Ockman S, Stone M (eds.) ”Open Sources: Voices from the Open Source Revolution“[M]. Sebastopol: O'Reilly, 1999（原文”released as 4.3BSD-Tahoe in June 1988"）［A］
- Net/2 Release Notes（1991）；Jolitz, B. (1991) “Porting UNIX to the 386”；McKusick, K. (1999) “Twenty Years of Berkeley Unix” ［B］
- CCI 手册； CSRG Tahoe 报告 ［A］## 史料考据补充（2026-08-04 任务3 联网核验）> 主题：4.3BSD Tahoe 的性能特征与 Tahoe 架构约束
- Bostic, K. (1988-06-16) 4.3BSD-Tahoe Release Announcement（tuhs.org/Usenet/comp.sys.tahoe/1988-June/000067.html）；McKusick, M. K. (1999) “Twenty Years of Berkeley Unix”；4.3BSD Release Notes（1986.6）；4.3BSD Tahoe Release Notes（1988.6）；4.3BSD-Reno Release Notes（1990 年初） ［A］
- 作者不详. USENET comp.unix.bsd 讨论存档[EB/OL]. 1988 ［B］
