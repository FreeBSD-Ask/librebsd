# 157. linux-arch 邮件列表 BSD 价值反推（larc p209）

> 来源：linux-arch 邮件列表 b2/b3/b4/b5 判读产物
> 判定：21 CAND / 0 NV。主题分布：杂项 2、BSD谱系 18、许可证 1。

## 157.1 杂项

- 【Linux社区】讨论 close(2) 语义时明确指出 Linux 与 Solaris 在并发线程中 close 是否中断 IO 上不同  "unlike Solaris we do NOT close(2) abort IO on the same descriptor from another thread" `<!-- ROW_MINE: linux-arch.messages.9701416 -->`
- 【Linux社区】Linux ELF core dump 引入扩展编号时显式对齐 AMD64-ABI 与 Solaris 的既有实现,体现与 Sun 系谱系在 ABI 层面的衔接。This is supported by AMD64-ABI and Solaris `<!-- ROW_MINE: linux-arch.messages.9712389 -->`

## 157.2 BSD谱系

- 【Linux社区】作者介绍 Linux Kernel Library 计划时点名 NetBSD rump kernel，称其曾关注该机制以备集成 libguestfs  "keeping an eye on libos (and on the NetBSD rump kernel stuff before)" `<!-- ROW_MINE: linux-arch.messages.9702013 -->`
- 【Linux社区】Kees Cook 回复 execveat 补丁时说明该 syscall 用于把 FreeBSD 的 Capsicum 沙箱模型移植到 Linux  "this patch is needed as a (small) part of implementing Capsicum in the Linux kernel" `<!-- ROW_MINE: linux-arch.messages.9702104 -->`
- 【Linux社区】讨论 preadv pwritev syscall 时指出 NetBSD FreeBSD OpenBSD 均已有该接口 反映 BSD 阵营对 POSIX I/O API 的先导作用  "Free- and OpenBSD have it too. For Solaris I've found a feature request only" `<!-- ROW_MINE: linux-arch.messages.9704210 -->`
- 【Linux社区】Rob Landley 讨论移除 arch/sh 时提到合作者早年做过 BSD 移植 反映 BSD 与 Linux 移植社区的人员交集  "the project before that was some sort of BSD I think" `<!-- ROW_MINE: linux-arch.messages.9704324 -->`
- 【Linux社区】Alan Cox 就 copyleft-next 许可证能否进内核展开治理与许可论证 明确指出内核社区刻意不提供 BSD 标签 改用 GPL with additional rights 防模块滥用：It's the same reason we don't have a BSD tag but use `<!-- ROW_MINE: linux-arch.messages.9704650 -->`
- 【Linux社区】Linux 新增 execveat 系统调用的动机直接引自 FreeBSD Capsicum 能力模式 属 BSD 特性向 Linux 移植的谱系信号：Capsicum is a security framework that has been present in FreeBSD since version 9.0 `<!-- ROW_MINE: linux-arch.messages.9705287 -->`
- 【Linux社区】sparc64 siginfo_t 结构体字段布局变更的讨论中出现 BSD 同源证据 Debian 代码搜索显示 sparc 与 BSD 都引用 si_trapno：Debian codesearch only turns up sparc (and BSD) references to si_trapno `<!-- ROW_MINE: linux-arch.messages.9706189 -->`
- 【Linux社区】开发者为裁定 pselect 语义实际到 NetBSD 与 Solaris 做行为对照 以判断哪项才符合 POSIX 规范：I tested NetBSD last night pselect() always calls the signal handlers even when an fd is ready `<!-- ROW_MINE: linux-arch.messages.9706220 -->`
- 【Linux社区】位操作头文件重构讨论触及 Minix 血统遗留命名 minix-le.h 与 ext2-non-atomic.h 并指出本系列将其整体消解：completely eliminate the the minix and ext2 definitions `<!-- ROW_MINE: linux-arch.messages.9706823 -->`
- 【Linux社区】FreeBSD与Solaris在系统调用审计场景下的信任边界粒度可细化到进程乃至64KB环境,与Linux通用审计思路形成对照。In the case of FreeBSD or Solaris, these can be smaller than a single machine `<!-- ROW_MINE: linux-arch.messages.9707679 -->`
- 【Linux社区】POSIX体系下flock与EWOULDBLOCK属BSD遗产,EAGAIN源自System V,二者数值同构的根源被认为是HP-UX在BSD与System V之间的历史妥协。EWOULDBLOCK originated on BSD, and was returned by (flock()) file locking `<!-- ROW_MINE: linux-arch.messages.9708173 -->`
- 【Linux社区】MADV_FREE统一值之争牵出dietlibc定义Solaris的MADV_FREE 0x5,且该值曾存在于内核sparc的mman.h直到2.6.25,反映sparc体系承袭SunOS传统。dietlibc has a Solaris #define MADV_FREE 0x5 in its mman.h `<!-- ROW_MINE: linux-arch.messages.9709822 -->`
- 【Linux社区】m68knommu 与 m68k 在大端小端 minix 文件系统位图索引上语义不一致需特殊处理以保持兼容,触及 Minix 谱系的字节序差异。m68knommu is big-endian minixfs but m68k (mmu) is little-endian minixfs `<!-- ROW_MINE: linux-arch.messages.9712449 -->`
- 【Linux社区】flock 接口非 POSIX 而是源自 4.2BSD,glibc 曾以 fcntl 模拟,同时为兼容 HPUX 把 EAGAIN 映射为 EWOULDBLOCK,直接牵涉 BSD 谱系与 HPUX ABI。flock is not POSIX, it's an interface invented by 4.2BSD `<!-- ROW_MINE: linux-arch.messages.9712996 -->`
- 【Linux社区】arm64 兼容层 statfs 结构体注释中直接引用 SunOS 对 f_namelen 字段的行为,Arnd Bergmann 据此考虑抽象 asm-generic/compat.h 统一各架构定义,BSD 系注释在 Linux 代码中留存。SunOS ignores this field `<!-- ROW_MINE: linux-arch.messages.9713364 -->`
- 【Linux社区】讨论将 minix 位操作从 asm/bitops.h 迁入 minix 文件系统独立代码,并为 m68k 等架构区分大端 16 位索引与原生字节序位图,深入 Minix 文件系统兼容。minix bit operations are only used by minix filesystem `<!-- ROW_MINE: linux-arch.messages.9713804 -->`
- 【Linux社区】Russell King 质询为何不直接用 asm-generic/bitops/minix.h 等既有头文件而新增一层间接,讨论触及 Minix 位操作抽象在 ARM 移植中的位置。using asm-generic/bitops/le.h, asm-generic/bitops/minix.h and asm-generic/bitops/ext2-non-atomic.h `<!-- ROW_MINE: linux-arch.messages.9714501 -->`
- 【Linux社区】讨论 preadv pwritev 系统调用时 Gerd Hoffmann 强调用户可见 API 必须与 BSD 家族现有实现一致以便应用移植,直接涉及 BSD API 谱系。want the user-visible API being identical to the existing ones in the BSD family `<!-- ROW_MINE: linux-arch.messages.9714851 -->`

## 157.3 许可证

- 【Linux社区】内核构建解耦用户态头文件,起因之一即用户态头可能处于不兼容许可证,并提议从GPL 2版stdarg.h抽取最小实现,触及GPL与非GPL用户态之间的许可边界。GPL 2 version of <stdarg.h> can be extracted from http://archive.debian.org `<!-- ROW_MINE: linux-arch.messages.9708270 -->`
- 【Linux社区】Thomas Gleixner 在 time_t 64 位改造讨论中直接对标 BSD 的 flag day 强制切换模式 指出 Linux 无法照搬该做法 这也是 y2038 议题反复被推迟的结构性原因 `<!-- ROW_MINE: linux-arch.messages.9716314 -->`
- 【Linux社区】Gerd Hoffmann 提交 preadv/pwritev 补丁时明确引用 BSD 生态先例 说明这两个系统调用已在 BSD 系统存在多年 Linux 只是补上通用接口缺口 `<!-- ROW_MINE: linux-arch.messages.9717677 -->`
- 【Linux社区】Akinobu Mita 在 bitops 头文件重构中提到 asm-generic/bitops 下保留 minix-le.h 用于 minix 位图操作 与 ext2 非原子实现并列作为通用位运算抽象层的历史产物 `<!-- ROW_MINE: linux-arch.messages.9717822 -->`
- 【Linux社区】ARM64 compat 补丁中 compat_statfs 的 f_namelen 字段沿用注释 SunOS ignores this field 引发 Pavel Machek 质疑该注释是否恰当 暴露 BSD/Sun 派系 statfs 语义与 Linux 实现的历史分歧 `<!-- ROW_MINE: linux-arch.messages.9717897 -->`
- 【Linux社区】Arnd Bergmann 转发并回复了一组关于在多种架构上测试 BSD 会计信息格式的记录，他在帖中只给出了 s390 上的测试结果。BSD accounting format 源自经典 BSD 内核的 acct 接口，说明这一内核数据结构在 Linux 移植语境中仍被当作 BSD 血统参照使用 testing BSD accounting format on different archs `<!-- ROW_MINE: linux-arch.messages.9730318 -->`
- 【Linux社区】Edward Napierala 为引入 MAP_FIXED_SAFE 讨论命名，提议直接沿用 FreeBSD 已引入的 MAP_EXCL，并引用 FreeBSD mmap 手册页说明其语义，Michal Hocko 认为 Linux 的实现方式不同、复用同名会造成混淆。这是一次明确的 BSD 接口命名溯源 MAP_EXCL? It was introduced in FreeBSD `<!-- ROW_MINE: linux-arch.messages.9732327 -->`
- 【Linux社区】Luis Rodriguez 在泛化段与链接器表 RFC 的讨论中坚持使用 copyleft-next 作为后续内核开发的授权，并称 copyleft-next 对 GPLv2 的兼容性已经过三名律师审查，James Bottomley 反驳称模块与内核合并后 GPLv2 仍是主导许可证。讨论落在 copyleft 与 GPL 的许可谱系之争 copyleft-next is the license of choice for ongoing kernel development `<!-- ROW_MINE: linux-arch.messages.9732370 -->`
- 【Linux社区】Thiago Macieira 提议让 CPU 特性探测库作为 freedesktop.org 下的跨平台协作项目，明确把 FreeBSD 列为与 macOS、Windows 并列的支持目标，Enrico Weigelt 认为在大组织中很难找到愿意长期承担维护责任的人。FreeBSD 在此作为 BSD 家族成员被纳入跨平台兼容目标 so long as it is cross-platform to at least macOS, FreeBSD and Windows `<!-- ROW_MINE: linux-arch.messages.9732572 -->`
- 【Linux社区】Carlos O'Donell 在 flock 与 FAGAIN、FWOULDBLOCK 的讨论中指出 flock 并非 POSIX，而是 4.2BSD 发明的接口，此前由 glibc 用 fcntl 模拟；Geert Uytterhoeven 拒绝在通用代码里加入兼容 HPUX 差异的变通。该表述直接给出了 flock 的 BSD 谱系来源 flock is not POSIX, it's an interface invented by 4.2BSD `<!-- ROW_MINE: linux-arch.messages.9733218 -->`
- 【Linux社区】Linus Torvalds 在审阅 fsid_t 时逐一对比 Solaris、SunOS、HP-UX、4.4BSD 与 FreeBSD 的 statfs 接口约定，证明 Linux 用户态 ABI 沿用 BSD 谱系命名 Linux, SunOS, HP-UX, 4.4BSD and FreeBSD all have a statfs() system call `<!-- ROW_MINE: linux-arch.messages.9719013 -->`
- 【Linux社区】Linus Torvalds 把小端位操作称为 minix 位操作，承认 Linux 内核位操作的历史类型约定可追溯至 Minix 时代little-endian (aka "minix") bitops historically `<!-- ROW_MINE: linux-arch.messages.9719232 -->`
- 【Linux社区】Jann Horn 指出 glibc 的 sys/sysctl.h 会转引 Linux 头文件，因为绝大多数命中是 BSD 系统的条件包含，可见 Linux 内核头文件被 BSD 系统依赖almost all of those hits are conditional includes for BSD systems `<!-- ROW_MINE: linux-arch.messages.9719817 -->`
- 【Linux社区】NetBSD 的 Xen PV DomU 在同一 HPE 平台持续稳定运行，而新内核 Linux 却因拓扑检查误判而关闭 SMP，形成 BSD 与 Linux 的直接对照other OS (current NetBSD PV DomU) still work fully `<!-- ROW_MINE: linux-arch.messages.9720212 -->`
- 【Linux社区】Russell King 反对随意重排 preadv 系统调用参数序，以 BSD 约定为标尺要求至少到用户态保持一致，以免日后标准化付出代价Follow the BSD one at least to user space `<!-- ROW_MINE: linux-arch.messages.9720508 -->`
- 【Linux社区】James Bottomley 与 Alan Cox 就 BSD 许可内核模块能否仅分发二进制展开争论，讨论 BSD 与 GPL 兼容及双许可在衍生作品条款下的边界 I can produce a Linux kernel module under a pure BSD licence because BSD is compatible with GPL `<!-- ROW_MINE: linux-arch.messages.9720747 -->`
- 【Linux社区】Linux内核openat新增O_EMPTY_PATH标志，作者直接对标FreeBSD同名API，认为可让容器通过fd重开文件免开/proc权限 it is very similar to the FreeBSD O_EMPTY_PATH flag `<!-- ROW_MINE: linux-arch.messages.9722868 -->`
- 【Linux社区】手册页维护者Colomar就ISO C命名与Linus Torvalds正面交锋，Linus以UAPI命名空间为由要求停止提交 the kernel doesn't use the standard names, and cannot use them for namespace reasons `<!-- ROW_MINE: linux-arch.messages.9723499 -->`
- 【Linux社区】系列补丁拟用asm/bitops.h中的小端位运算替代minix位运算以支持ext2等文件系统的字节序统一 minix bit operations are only used by minix filesystem and useless by other modules `<!-- ROW_MINE: linux-arch.messages.9724462 -->`
- 【Linux社区】Russell King在preadv与pwritev讨论中坚持用户可见API应与BSD标准保持一致，反对偏离导致OS可移植性倒退 the user visible API should be changed from the BSD standard `<!-- ROW_MINE: linux-arch.messages.9724469 -->`
- 【Linux社区】Geert质疑m68k为何采用小端minix文件系统，梳理minix位运算在各架构遗留的字节序错配问题 any architecture that defines minix bitops as little-endian is broken `<!-- ROW_MINE: linux-arch.messages.9726504 -->`
- 【Linux社区】讨论 flock 与 EAGAIN/EWOULDBLOCK 时确认该接口源自 4.2BSD，且以 OpenBSD 手册页与 HPUX 行为作横向对照，主张按文档返回码检查的应用不能算错 "flock is not POSIX, it's an interface invented by 4.2BSD, and was" `<!-- ROW_MINE: linux-arch.messages.9697117 -->`
- 【Linux社区】Al Viro 亲自翻查 FreeBSD、NetBSD、OpenBSD 三家内核源码，否证了 AIX 与 BSD 和 MacOS 已有 close-on-fork 的说法，判定该部分属于都市传说 "I have checked the source of FreeBSD, NetBSD and OpenBSD." `<!-- ROW_MINE: linux-arch.messages.9697201 -->`
- 【Linux社区】移植 O_BENEATH 到 Linux openat 时说明该能力原是 FreeBSD 10.x Capsicum 安全框架的内部机制，FreeBSD 侧同期也在提案对外暴露这一变体 "the internals of the Capsicum security framework, which is available in FreeBSD 10.x" `<!-- ROW_MINE: linux-arch.messages.9698147 -->`
- 【Linux社区】为 SIGINFO 争取依据时援引 GNU make 在各 BSD 发行版上早已支持该信号的事实，指出用户群确实存在只是不在内核邮件列表发声 "As far as I recall, GNU make on *BSD does support SIGINFO" `<!-- ROW_MINE: linux-arch.messages.9698183 -->`
- 【Linux社区】讨论 MAP_FIXED_SAFE 命名时转引 FreeBSD 已引入的 MAP_EXCL 语义，并因其在 FreeBSD 中只是 MAP_FIXED 修饰符而明确拒绝沿用同名标志 "it looks like MAP_EXCL is a MAP_FIXED mofifier which is not how we are" `<!-- ROW_MINE: linux-arch.messages.9699569 -->`
- 【Linux社区】针对 netfilter 把 BSD 整型换成 Linux 严格整型的补丁，H. Peter Anvin 强烈反对，认为此举引入对 linux/types.h 的依赖且标准类型本应是 uint8_t "Netfilter traditionally uses BSD integer types in its interface headers" `<!-- ROW_MINE: linux-arch.messages.9700230 -->`
- 【Linux社区】Linus 指出 BSD 惯用单下划线 _BYTE_ORDER 而 glibc 用双下划线 __BYTE_ORDER，决定让内核改用 CONFIG 宏、仅修 uapi 头部避免把这套混乱搬进内核 "the standard under BSD seems to be single-underscore "_BYTE_ORDER"" `<!-- ROW_MINE: linux-arch.messages.9700357 -->`
- 【Linux社区】netfilter 接口头文件沿用 BSD 整数类型，Arnd Bergmann 提议改用 Linux 严格类型，David Miller 反驳称本就该早做。这是 BSD 用户态接口惯例渗入 Linux ABI 层的直接证据。 `<!-- ROW_MINE: linux-arch.messages.9726766 -->`
- 【Linux社区】Horst H. von Brand 请求把 _syscallX 宏层改为 BSD 或 LGPL 授权，以便构建非 GPL libc；Arnd Bergmann 回复 klibc 已有 BSD 授权版本。属许可证争议与 BSD 授权的直接证据。 `<!-- ROW_MINE: linux-arch.messages.9728288 -->`
- 【Linux社区】讨论 preadv 与 pwritev 系统调用时，对比 FreeBSD 与 OpenBSD 已实现而 Solaris 仅有 1994 年的功能请求单。属 Linux 与 BSD 及 Solaris 的 API 横向对比证据。 `<!-- ROW_MINE: linux-arch.messages.9728687 -->`
- 【Linux社区】execveat(2) 讨论中 Andy Lutomirski 指出 *BSD 的 /dev/stdin 具备 dup() 式语义，并说明代价是其 VFS 代码极复杂，与 Linux 行为形成对照。 `<!-- ROW_MINE: linux-arch.messages.9728739 -->`
