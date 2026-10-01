---
chapter: 第 95 章
id: CH95
volume: 第05卷-freebsd的工程化奠基
---

# 第95章 kqueue的设计与jonathan-lemon工程贡献

## 要点

- Jonathan Lemon 在 2000 年向 freebsd-hackers 提交 kqueue 提案，动机是 **select(2)**/**poll(2)** 在高并发连接下的 O(N) 扫描成本与状态丢失，无法支撑 Yahoo!/Hotmail 级别的事件驱动服务器；kqueue 首次 commit 于 2000 年 4 月 16 日（4.0-RELEASE 2000.3.20 之后，4.1-RELEASE 2000.7.26 之前）
- **kqueue(2)** 返回一个文件描述符，**kevent(2)** 通过 kevent 结构体 {ident, filter, flags, fflags, data, udata} 实现一次性注册与返回，filter 概念将事件源抽象为 EVFILT_READ/EVFILT_WRITE/EVFILT_AIO/EVFILT_VNODE/EVFILT_PROC/EVFILT_SIGNAL/EVFILT_TIMER 七类
- kqueue 在内核维护就绪事件列表，**kevent(2)** 调用仅返回已就绪事件，复杂度从 O(N) 降至 O(1)，且支持水平触发 (LT) 与边沿触发 (ET) 两种模式，stateful 设计避免每次重新注册
- kqueue 是 BSD 路线对 select/poll 性能瓶颈的回应，比 Linux epoll(2.5.44, 2002.10) 早 2 年，比 Solaris event ports(Solaris 10, 2005.1) 早 5 年，确立 BSD 在事件通知领域的先发优势
- kqueue 对 epoll 的具体影响体现在：(1) stateful 设计思想一致；(2) 内核维护就绪列表；(3) 但 epoll 拒绝 filter 抽象，改为 “任意 fd 即可挂载” 的 composable 模型，每新增一种资源不需改内核
- kqueue 设计史料的争议点包括：(1) Lemon 是否独立于 Banga 的 /dev/poll 工作；(2) 设计灵感是否部分来自 Solaris /dev/poll；(3) commit 时间与 BSDCon 论文时间的先后
- Jason Evans 2000 年 11 月 KSE 论文（Kernel-Scheduled Entities for FreeBSD）提及，将异步 I/O 集成进 libc_r 需先稳定 AIO 实现，再把基于 **poll(2)** 的事件循环切换为基于 **kqueue(2)** 的事件循环，以在同一循环中集成 I/O 完成通知（Evans, 2000）——显示 kqueue 在首次 commit（2000-04-16）后不足一年内，已被 FreeBSD 核心开发者视为替代 poll() 的事件通知接口，构成 kqueue 早期采用的同期证据

## 史料

- kqueue(2) 手册页 EV_CLEAR 标志说明、Lemon BSDCon 2000 论文第 4 节性能数据 ［A］
- Linux kernel 2.5.44
- Libenzi “Improving (network) I/O performance”(xmailserver.org, 2001-07-01 初稿，2002-10-30 更新)〔存疑：原文截断，引用形式经本章文献条回源补全，后文是否另有条目待回源〕

## 史观

- 总纲第 17 条——证明世界先于解释和改造世界：select/poll 的工程瓶颈催生 kqueue 设计而非理论驱动（原挂“总纲第 2 条——实践先于理论”，按权威表校正）
  - 辨析：经 freebsd.duckdb commits 表验证，kqueue 首次 commit 为 2000-04-16（非旧叙事 2000.7.5），属 4.1-CURRENT 开发周期内合入主干，4.1-RELEASE 2000.7.26 正式发布；经邮件列表库验证通过（fact-check 2026-08-14），Jonathan Lemon 2000-06-22《Re: tail after kqueue changes》（freebsd-current，Message-ID `<no-id-freebsd-current-798100dde2fde2f6>`）与 2000-10-25《Re: kqueue microbenchmark results》（freebsd-hackers，署名 <jlemon@flugsvamp.com>）两条一手邮件佐证 Lemon 于 2000 年作为 kqueue 作者的活跃期，与 commit 时间线一致；Lemon 的雇主关系存在争议，部分来源称其受 Yahoo! 工作驱动，需查 commit metadata 与邮件签名确认
- 总纲第 17 条——证明世界先于解释和改造世界：stateful 设计源于实际服务器场景需求（原挂“总纲第 2 条——实践先于理论”，按权威表校正；原文仅存“st”截断残迹，语句自本章 95.2 节同文回源补全）
- 总纲第 4 条——分离聚合是永恒规律：kqueue 用 filter 抽象取代多套 API 是抽象克制的典范（原挂“总纲第 6 条——形式主义膨胀与抽象克制”，按权威表改挂）
  - 辨析：filter 中心化设计与 epoll 的 composable 设计的优劣争议，Conill 2021 批评称 filter 中心化导致技术债务
  - 文献：Lemon BSDCon 2000 论文；Banga & Mogul “Scalable Kernel Performance for Internet Servers”(USENIX 1998) 作对比 ［B］
- 专题语（不设条号，技术债务与代码考古）：select/poll 的 1980s 设计在 2000 年代 Web 服务器场景下成为债务（原挂“总纲第 5 条——技术债务与代码考古”，该主题非权威表基线条目，改不设条号专题语）
  - 辨析：FD_SETSIZE 限制是否可通过内核 sysctl 调整，不同来源说法不一，需查 sys/select.h 与内核实现
  - 文献：Stevens《UNIX Network Programming》第 6 章；Banga USENIX 1998 ［B］
- 总纲第 4 条——分离聚合是永恒规律：Libenzi 选择 composable 而非 filter 路线导致后续 Linux 生态与 BSD 生态分野（原挂“总纲第 1 条——偶然性改写历史”，按权威表改挂）
  - 辨析：Libenzi 与 Lemon 的设计是否独立演化，需对比二者 2002 前的邮件往来
  - 文献：Libenzi “Improving (network) I/O performance”(xmailserver.org, 2001-07-01 初稿，2002-10-30 更新)；Lemon BSDCon 2000 论文 ［B］
- 专题语（不设条号，考据方法：0 信任原则）：对 Libenzi 自述的灵感来源须独立考据，**epoll(7)** 手册页与 Libenzi 论文 References 节的措辞选择本身即可视为形式主义权力分析的观察标记（分析框架表述，非既证结论。原挂“总纲第 4 条——0 信任原则”，0 信任非总纲基线条目，改考据方法专题语）
  - 辨析：**epoll(7)** 手册页将 kqueue 定性为“similar mechanism”而非“inspiration source”，这一措辞选择是否反映 Libenzi 的个人立场抑或 Linux man-pages 项目维护者的编辑决策，须区分二者；Libenzi 论文 References 节的文献选择则更直接反映 Libenzi 个人立场，因论文由 Libenzi 本人撰写，References 节的编辑权完全归属 Libenzi；但 References 节未列 kqueue 亦可能反映 Libenzi 的文献检索盲区而非刻意回避——2000-2001 年间 BSDCon 论文的传播范围有限，Libenzi 作为 Linux 内核开发者未必关注 BSD 学术会议，这一可能性须以 0 信任原则审慎对待
- 总纲第 19 条——解释学循环是历史认识的根本条件：Libenzi 通过在论文 References 节中系统性地不引用 kqueue，行使了“什么被记录、什么被遗忘”的权力——文献选择预先框定了后人的解释循环，对 epoll 与 kqueue 关系的认识须往返于 Libenzi 论文文本与 kqueue 一手文献之间，方能校正单一文献链的偏差（原挂“总纲第 19 条——权力与知识的共谋”，系第 14 章释读主题的错误归并，按权威表补全主题语并重写映射论述）

## 辨析

- 经 freebsd.duckdb commits 表验证，kqueue 首次 commit 为 2000-04-16（非旧叙事 2000.7.5），属 4.1-CURRENT 开发周期内合入主干，4.1-RELEASE 2000.7.26 正式发布；经邮件列表库验证通过（fact-check 2026-08-14），Jonathan Lemon 2000-06-22《Re: tail after kqueue changes》（freebsd-current，Message-ID `<no-id-freebsd-current-798100dde2fde2f6>`）与 2000-10-25《Re: kqueue microbenchmark results》（freebsd-hackers，署名 <jlemon@flugsvamp.com>）两条一手邮件佐证 Lemon 于 2000 年作为 kqueue 作者的活跃期，与 commit 时间线一致；Lemon 的雇主关系存在争议，部分来源称其受 Yahoo! 工作驱动，需查 commit metadata 与邮件签名确认
- filter 中心化设计与 epoll 的 composable 设计的优劣争议，Conill 2021 批评称 filter 中心化导致技术债务
  - 文献：Lemon BSDCon 2000 论文；Banga & Mogul “Scalable Kernel Performance for Internet Servers”(USENIX 1998) 作对比 ［B］

## 文献

- Lemon “Kqueue: A Generic and Scalable Event Notification Facility”(USENIX BSDCon 2000)；kqueue(2) 手册页；Jonathan Lemon. Introduce kqueue() and kevent(), a kernel event notification facility. freebsd-src [DB/OL]. 2000-04-16T18:53:38Z. cb679c385ef325d11f162e09b604df7532fc8009 ［A］
- [1] Stevens UNP Vol. I 2nd ed. 1998、[2] Stevens TCP/IP Illustrated Vol. 1 1994、[3] Banga & Mogul USENIX ATC 1998、[4] Banga Druschel Mogul SIGMETRICS 1998、[5] Banga & Druschel USENIX ITS 1997、[6] Provos & Lever “Scalable Network I/O in Linux” CITI techreport 2000、[7] Dan Kegel “The C10K problem” kegel.com/c10k.html、[8] Richard Gooch “IO Event Handling Under Linux”、[9] Chandra & Mosberger “Scalability of Linux Event-Dispatch Mechanisms” HPL-2000-174、[10] Provos & Lever “Analyzing the Overload Behaviour of a Simple Web Server” CITI techreport 2000
- Linux **epoll(7)** 手册页；Lemon BSDCon 2000 论文 ［A］
- freebsd.duckdb commits 表；Banga USENIX 1998 ［A］
- Linux man-pages project. epoll(7). man-pages-6.18. 2026-02-08 ［A］；Libenzi D. Improving (network) I/O performance. xmailserver.org/linux-patches/nio-improve.html. 2001-07-01 初稿，2002-10-30 更新 ［A］；Dan Kegel. The C10K problem. kegel.com/c10k.html ［A］；LKML 2001-2002 邮件存档［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。
