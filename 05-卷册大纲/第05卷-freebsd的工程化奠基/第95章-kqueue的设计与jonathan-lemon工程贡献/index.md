---
chapter: 第 95 章
id: CH95
volume: 05
---

# 第95章 kqueue的设计与jonathan-lemon工程贡献

## 要点

- Jonathan Lemon 在 2000 年向 freebsd-hackers 提交 kqueue 提案，动机是 **select(2)**/**poll(2)** 在高并发连接下的 O(N) 扫描成本与状态丢失，无法支撑 Yahoo!/Hotmail 级别的事件驱动服务器；kqueue 首次 commit 于 2000 年 4 月 16 日（4.0-RELEASE 2000.3.20 之后，4.1-RELEASE 2000.7.26 之前）
- **kqueue(2)** 返回一个文件描述符，**kevent(2)** 通过 kevent 结构体 {ident, filter, flags, fflags, data, udata} 实现一次性注册与返回，filter 概念将事件源抽象为 EVFILT_READ/EVFILT_WRITE/EVFILT_AIO/EVFILT_VNODE/EVFILT_PROC/EVFILT_SIGNAL/EVFILT_TIMER 七类
- kqueue 是 BSD 路线对 select/poll 性能瓶颈的回应，比 Linux epoll(2.5.44, 2002.10) 早 2 年，比 Solaris event ports(Solaris 10, 2005.1) 早 5 年，确立 BSD 在事件通知领域的先发优势
- kqueue 设计史料的争议点包括：(1) Lemon 是否独立于 Banga 的 /dev/poll 工作；(2) 设计灵感是否部分来自 Solaris /dev/poll；(3) commit 时间与 BSDCon 论文时间的先后
- Jason Evans 2000 年 11 月 KSE 论文（Kernel-Scheduled Entities for FreeBSD）提及，将异步 I/O 集成进 libc_r 需先稳定 AIO 实现，再把基于 **poll(2)** 的事件循环切换为基于 **kqueue(2)** 的事件循环，以在同一循环中集成 I/O 完成通知（Evans, 2000）——显示 kqueue 在首次 commit（2000-04-16）后不足一年内，已被 FreeBSD 核心开发者视为替代 poll() 的事件通知接口，构成 kqueue 早期采用的同期证据

## 史观

- 总纲第 2 条——实践先于理论，select/poll 的工程瓶颈催生 kqueue 设计而非理论驱动
  - 辨析：经 bsd_commits.db commits 表验证，kqueue 首次 commit 为 2000-04-16（非旧叙事 2000.7.5），属 4.1-CURRENT 开发周期内合入主干，4.1-RELEASE 2000.7.26 正式发布；经邮件列表库验证通过（fact-
- 总纲第 6 条——形式主义膨胀与抽象克制，kqueue 用 filter 抽象取代多套 API 是抽象克制的典范
  - 辨析：filter 中心化设计与 epoll 的 composable 设计的优劣争议，Conill 2021 批评称 filter 中心化导致技术债务
  - 文献：Lemon BSDCon 2000 论文；Banga & Mogul "Scalable Kernel Per
- 总纲第 5 条——技术债务与代码考古，select/poll 的 1980s 设计在 2000 年代 Web 服务器场景下成为债务
  - 辨析：FD_SETSIZE 限制是否可通过内核 sysctl 调整，不同来源说法不一，需查 sys/select.h 与内核实现
  - 文献：Stevens《UNIX Network Programming》第 6 章；Banga USENIX 1998 ［
- 总纲第 1 条——偶然性改写历史，Libenzi 选择 composable 而非 filter 路线导致后续 Linux 生态与 BSD 生态分野
  - 辨析：Libenzi 与 Lemon 的设计是否独立演化，需对比二者 2002 前的邮件往来
  - 文献：Libenzi "Improving (network) I/O performance"(xmailserver.org, 2001
- 总纲第 4 条——0 信任原则，对 Libenzi 自述的灵感来源须独立考据，**epoll(7)** 手册页与 Libenzi 论文 References 节的措辞选择本身即是形式主义的权力标记；总纲第 19 条——权力与知识的共谋，Libenzi 通过在论文 References 节中系统性地不引用 kqueue，行使了“什么被记录、什么被遗忘”的权力
  - 辨析：**epoll(7)**

## 辨析

- 经 bsd_commits.db commits 表验证，kqueue 首次 commit 为 2000-04-16（非旧叙事 2000.7.5），属 4.1-CURRENT 开发周期内合入主干，4.1-RELEASE 2000.7.26 正式发布；经邮件列表库验证通过（fact-check 2026-08-14），Jonathan Lemon 2000-06-22《Re: tail after
- filter 中心化设计与 epoll 的 composable 设计的优劣争议，Conill 2021 批评称 filter 中心化导致技术债务
  - 文献：Lemon BSDCon 2000 论文；Banga & Mogul "Scalable Kernel Performance for Internet Servers"(USENIX 1998) 作对比 ［B］

## 94.1.3 设计

- FD_SETSIZE 限制是否可通过内核 sysctl 调整，不同来源说法不一，需查 sys/select.h 与内核实现
  - 文献：Stevens《UNIX Network Programming》第 6 章；Banga USENIX 1998 ［B］

## 94.2.2 kqueue 的 O(1) 优势

- 要点：kqueue 在内核维护就绪事件列表，**kevent(2)** 调用仅
- Libenzi 与 Lemon 的设计是否独立演化，需对比二者 2002 前的邮件往来
  - 文献：Libenzi "Improving (network) I/O performance"(xmailserver.org, 2001-07-01 初稿，2002-10-30 更新)；Lemon BSDCon 2000 论文 ［B］

## 94.3.2 kqueue 对 epoll 的效应

-
- **epoll(7)** 手册页将 kqueue 定性为"similar mechanism"而非"inspiration source"，这一措辞选择是否反映 Libenzi 的个人立场抑或 Linux man-pages 项目维护者的编辑决策，须区分二者；Libenzi 论文 References 节的文献选择则更直接反映 Libenzi 个人立场，因论文由 Libenzi 本人撰写，Refe

## 文献

- Lemon "Kqueue: A Generic and Scalable Event Notification Facility"(USENIX BSDCon 2000)；kqueue(2) 手册页；Jonathan Lemon. Introduce kqueue() and kevent(), a kernel event notification facility. freebsd-src [DB/OL]. 2000-04-16T18:53:38Z. cb679c385ef325d11f162e09b604df7532fc8009 ［A］

## 94.1.2 kevent 的系统调用设计

- Lemon BSDCon 2000 论文；Banga & Mogul "Scalable Kernel Performance for Internet Servers"(USENIX 1998) 作对比 ［B］

## 94.1.3 设计意义分析

- 要点：kqueue 是 BSD 路线对 select/poll 性能瓶颈的回应，比 Linux epoll(2.5.44, 2002.10) 早 2 年，比 Solaris event ports(Solaris 10, 2005.1) 早 5 年，确立 BSD 在事件通知领域的先发优势
- 史料：Linux kernel 2.5.44
- Stevens《UNIX Network Programming》第 6 章；Banga USENIX 1998 ［B］

## 94.2.2 kqueue 的 O(1) 优势

- 要点：kqueue 在内核维护就绪事件列表，**kevent(2)** 调用仅返回已就绪事件，复杂度从 O(N) 降至 O(1)，且支持水平触发 (LT) 与边沿触发 (ET) 两种模式，stateful 设计避免每次重新注册
- 史料：kqueue(2) 手册页 EV_CLEAR 标志说明、Lemon BSDCon 2000 论文第 4 节性能数据 ［A］
- 史观：总纲第 2 条——实践先于理论，st
- Libenzi "Improving (network) I/O performance"(xmailserver.org, 2001-07-01 初稿，2002-10-30 更新)；Lemon BSDCon 2000 论文 ［B］

## 94.3.2 kqueue 对 epoll 的效应

- 要点：kqueue 对 epoll 的具体影响体现在：(1) stateful 设计思想一致；(2) 内核维护就绪列表；(3) 但 epoll 拒绝 filter 抽象，改为 “任意 fd 即可挂载” 的 composable 模型，每新增一种资源不需改内核
- 史料：Libenzi "Impr
- [1] Stevens UNP Vol. I 2nd ed. 1998、[2] Stevens TCP/IP Illustrated Vol. 1 1994、[3] Banga & Mogul USENIX ATC 1998、[4] Banga Druschel Mogul SIGMETRICS 1998、[5] Banga & Druschel USENIX ITS 1997、[6] Provos & Lever "Scalable Network I/O in Linux" CITI techreport 2000、[7] Dan Kegel "The C10K problem" kege
- Linux **epoll(7)** 手册页；Lemon BSDCon 2000 论文 ［A］
- bsd_commits.db commits 表；Banga USENIX 1998 ［A］
- Linux man-pages project. epoll(7). man-pages-6.18. 2026-02-08 ［A］；Libenzi D. Improving (network) I/O performance. xmailserver.org/linux-patches/nio-improve.html. 2001-07-01 初稿，2002-10-30 更新 ［A］；Dan Kegel. The C10K problem. kegel.com/c10k.html ［A］；LKML 2001-2002 邮件存档[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP142（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 主持人细读 NSA 面向通用操作系统的 W^X（write XOR execute）安全功能要求：内存页要么可执行、要么可写、决不可兼得，以防攻击者把写入的数据当作程序执行（288.04-330.38）；并对照 Intel 的 NX 位与 DEP 机制、即时编译等例外情形（344.10-362.82），以及 SPARC 与 ARM 处理器在这类 RISC 平台上的原生支持差异（362.82-369.38），与本期标题的 RISC 主题相呼应。（BSD Now EP142，[288.04-369.38]，L2）
- Perlstein 回顾入坑史：少年时代在 MS-DOS 上写汇编自学编程，进大学被计算机系同学讥笑“MS-Dog”，恰逢学校以 FreeBSD 为教学平台，其多任务与内存管理令他感到这是一个真正完整的操作环境；1998 至 1999 年间他在邮件列表提问文件系统问题，收到详尽而易懂的长篇技术答复，自此被社区吸引而留下。（BSD Now EP142，[1536.28-1617.20]，L1）
- Perlstein 自述其 FreeBSD 内核工程履历：2000 年前后参与 SMP 项目，完成 select 与 poll 的初始 SMP 锁定、SIGIO 锁定与 System V 资源锁等叶区锁；USB2 大型代码库合入时充当“牧羊人”，协调在真空中工作的外部开发者与社区的磨合；又改造大于 4GB 内存机器的默认参数，使插电即得足够 mbuf 支撑万兆网卡，承认短期引入破坏但认为长期值得。（BSD Now EP142，[1706.00-1839.22]，L1）
- FreeBSD 成为 Perlstein 的立身之本：1999 年经 Paul Saab 引导将 Yahoo 的 accept filters 推入系统，配合当时新出现的 kqueue，在单颗 Pentium 400 上实现每秒 1500 连接的 web 追踪服务；受雇 Apple 内核团队解决 NFS 断连导致系统挂起的问题；在 Juniper 把 Junos（FreeBSD 改版）部署到高速线卡并做粗粒度线程化；任 OkCupid CTO 期间全栈运行 FreeBSD；后来还赞助 libuinet 用户态网络栈用于安全设备并期望其合回主线。（BSD Now EP142，[1923.76-2127.04]，L1）

**史料**：

- 本期提及的一手与二手材料：Damien Miller 在 OpenSSH 开发邮件列表发布的协议 1 弃用公告，称该协议已处于各阶段弃用近十年、编译期禁用约一年，计划 2016 年 8 月 SSH 7.4 发布后先移除服务器端、2017 年 6 月全部删除（4403.08-4493.32）；荷兰高校关于 SROP（信号返回导向编程）的学术论文及 OpenBSD 的缓解补丁草案，采用 kbind 技巧、魔术 cookie 与信号蹦床页随机化（4093.44-4302.98）；GitHub 上 .NET CoreCLR 对 NetBSD 的移植 pull request（3986.98-4076.00）；2000 年 Salon 杂志的 BSD 起源长文（1021.42-1060.26）；iX Systems 为客户交付约 360 台服务器、合计约 10PB 存储的部署订单（1352.26-1433.92）。（BSD Now EP142，[4403.08-4493.32]，L2）

**史观**：

- 总纲10 动手者创造历史：主持人转述的 2000 年 Salon 文章给出与英雄史观相反的判断：对 Bill Joy 的过度聚焦是一种圣徒传式叙事，遮蔽了更大的图景——“伯克利最重要的贡献不是软件本身，而是创造软件的方式”（1076.64-1104.68）——一个任何时刻不超过四人的核心小组，把不断扩张的远方志愿程序员网络协调成渐进发布、稳步改进的流水线。技术史的真正主角是协作结构的发明，而非站在台前的个人。（BSD Now EP142，[1045.86-1104.68]，L2）
- 总纲5 没有必然性，只有偶然性：Perlstein 走向 FreeBSD 开发者的每一步都系于偶然：恰好在 MS-DOS 时代自学汇编，恰好被同学讥讽而另寻出路，恰好学校采用 FreeBSD 作教学平台，恰好邮件列表给出令他折服的长篇答复。没有哪一环是历史必然，一个行动者的转向由一连串具体偶然事件串联而成。（BSD Now EP142，[1561.38-1617.20]，L1）

**辨析**：

- Perlstein 对 FreeBSD 上手体验提出一组可检验的批评：pkg install Django 直接报无包，而真实包名是 py27-django 这类带版本前缀的命名；学会 Subversion 与 Phabricator 的技能难以外溢到 Git/GitHub 主流生态；仓库过大令新手克隆即卡壳。他主张举办“反向安装马拉松”——不给新手帮助，只记录他们在何处卡住——甚至公开抛出为项目改名的争议建议（3051.12-3136.92），理由是连大会讲者与他的母亲都念错 FreeBSD。这些均为当事人单一来源立场，尚待社区实践检验。（BSD Now EP142，[2686.14-2922.74]，L1）

**文献**：

- [BSD Now EP142] Pennington J. BSD Now: 142: Diving for BSD Perls[EB/OL]. (2016-05-18)[2026-08-15]. https://www.bsdnow.tv/142.

<!-- /PODCAST_REVIEW -->
