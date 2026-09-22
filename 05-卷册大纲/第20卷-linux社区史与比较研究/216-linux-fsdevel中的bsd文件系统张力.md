# 216 【Linux社区】linux-fsdevel 中的 BSD 文件系统张力与 BSD 技术反向输出

> 来源：linux-fsdevel（360,374 封，2002-2026 活跃），BSD 价值打分 32,814 条命中，BSD 变体+技术+has_bsd 过滤后 912 封，score≥10 后 126 封，subject 去重后 126 封，6 路并行读手逐封判定，46 条 outline_worthy（precision 36.5%）。
> 判定：46 CAND。主题分布：技术 21、BSD 谱系 13、许可证 9、治理 3。
> 全库去重：本次 46 条与 205-215 章 372 条 ROW_MINE 十处严格去重（linux-fsdevel source 独立，0 条完全重复）。

## 216.0 【Linux社区】体例说明
本文件系 linux-fsdevel 列表中 BSD 文件系统张力与 BSD 技术反向输出的逐封提取产物。与 205-210 章（基于 lkml tier A/B 分层的 BSD 技术承袭）、211 章（BSD 发展列表 BSD 侧视角）、213 章（systemd-devel BSD 张力）、214 章（ksummit BSD/Linux 张力）、215 章（freebsd-hackers BSD/GPL 许可证张力）互补，构成《给我自由》第 20 卷 BSD 专题的完整图景。
**独特价值**：这 46 条是 Linux 文件系统开发者在 linux-fsdevel 列表中讨论 BSD 文件系统技术（UFS、HFS+、APFS）被 Linux 采用/移植、BSD 许可证（BSD-2/3-Clause、LGPL）在内核中的落地、BSD 安全沙箱（Capsicum、Pledge）对 Linux Landlock 的启发、BSD 文件系统语义（chflags、F_FULLFSYNC、fsync_range）对 Linux VFS 的补足。**Linux 文件系统开发者的一手视角**，覆盖 2002-2026 二十余年 BSD 技术流入 Linux 的完整链路。
**叙事主线**：2002 UFS 开源移植（Al Viro 从 OpenStep 移植）、2003 HFS+ 驱动公告（Brad Boyer）、2006-2017 UFS 持续维护（Dushistov、Zwink 系列）、2014 NetBSD fsync_range 移植（Hellwig）、2015 FreeBSD CLONE_FD（Ericson）、2019 Landlock LSM 启发（Mellor-Crummey 引 FreeBSD Capsicum/OpenBSD Pledge）、2022 freevxfs relicense to GPLv2、2022 Apple BSD-3-Clause LZFSE 移植进 staging/apfs、2026 BSD chflags 映射到 Linux S_IMMUTABLE。
**ROW_MINE 格式**：`<!-- ROW_MINE: linux-fsdevel.messages.<N> -->`，N 为消息 id。

## 216.1 【Linux社区】BSD 文件系统技术反向输出（21 条）

- 【Linux社区】2014年2月 Hin-Tak Leung(htl10@users.sourceforge.net) 在「Re: testing HFS+ journal replay against real Apple code」中建议 Vyacheslav Dubeyko 用 Apple 发行的 Darwin 内核（BSD 派生）作为 HFS+ 日志回放的真实参考实现进行对比测试。 `<!-- ROW_MINE: linux-fsdevel.messages.376702 -->`
- 【Linux社区】2026年6月 John Ericson(mail@johnericson.me) 在「exec: add spawn templates for repeated executable startup」讨论中建议 Li Chen 参考 FreeBSD/OpenBSD/XNU 的 P_INEXEC/PS_INEXEC/P_LINTRANSIT 标志设计 Linux 等价物。 `<!-- ROW_MINE: linux-fsdevel.messages.710802 -->`
- 【Linux社区】2008年5月 Jamie Lokier(jamie@shareable.org) 在「Re: [PATCH 0/4] (RESEND) ext3[34] barrier changes」中 引用 Darwin 的 F_FULLFSYNC 作为对照，「applications that require a strict ordering of writes should use F_FULLFSYNC」是 BSD 谱系补足 fsync 语义的例证 `<!-- ROW_MINE: linux-fsdevel.messages.293574 -->`
- 【Linux社区】2020年4月（针对 v5.5 重新测试） Ross Zwisler(zwisler@chromium.org) 在「[PATCH v4] Add a "nosymfollow" mount option.」中 提出 MNT_NOSYMFOLLOW 使特权进程解析路径时不跟随符号链接，在 fs/namei.c 加 3 行判断并把 BSD 实现（FreeBSD vfs_lookup.c 第 1040 行、mount(8) 手册）与 ChromeOS 的 200 余行 LSM 方案并列，「FreeBSD solves this with an equivalent flag」是 BSD 挂载语义被 Linux 采纳的直接证据。 `<!-- ROW_MINE: linux-fsdevel.messages.295995 -->`
- 【Linux社区】2020年 Mickael Salau(mic@digikod.net) 在「Landlock LSM v14」中 引入文件系统访问控制并明确以FreeBSD Capsicum和OpenBSD Pledge/Unveil为设计灵感，「FreeBSD Capsicum or OpenBSD Pledge/Unveil」是 BSD安全沙箱机制在Linux LSM层的谱系溯源 `<!-- ROW_MINE: linux-fsdevel.messages.303264 -->`
- 【Linux社区】2014年4月 Jamie Lokier(jamie@lkier.net) 在「Re: [PATCH] fsync_range, was: Re: munmap, msync: synchronization」中 核对 FreeBSD 8.2 是否带 fsync_range，「There is no FreeBSD implementation」是 BSD 各分支连 fsync_range 都不统一的对照。 `<!-- ROW_MINE: linux-fsdevel.messages.313470 -->`
- 【Linux社区】2020年6月 Kyle Evans(kevans@freebsd.org) 在「Re: [PATCH v5 1/3] open: add close_range()」中 回应 close_range 是否比 switch-to-cloexec 更安全，「innocuous on FreeBSD」表明 BSD 上该 syslog fd 竞争场景并不典型，构成跨系统语义对照。 `<!-- ROW_MINE: linux-fsdevel.messages.341331 -->`
- 【Linux社区】2020年5月 Mickaël Salaün(mic@digikod.net) 在「[PATCH v17 00/10] Landlock LSM」中 说明 Landlock 沙箱的谱系，「FreeBSD Capsicum or OpenBSD Pledge/Unveil」是 BSD 安全机制影响 Linux 文件系统访问控制的直接引文 `<!-- ROW_MINE: linux-fsdevel.messages.419383 -->`
- 【Linux社区】2020年7月 Mickaël Salaün(mic@digikod.net) 在「[PATCH v15 00/10] Landlock LSM」中 简化对象/规则/规则集管理（SLOC 1542→1273、Jann Horn 贡献更保守的内存释放）、引入规则层级防止嵌套沙箱越权，并公开列出 dentry 路径遍历与 UnionFS 两项限制，「FreeBSD Capsicum or OpenBSD Pledge/Unveil」在此首次进入内核提交流成为 BSD 沙箱设计来源的正式声明。 `<!-- ROW_MINE: linux-fsdevel.messages.509595 -->`
- 【Linux社区】2020年6月 Sargun Dhillon(sargun@sargun.me) 在「Re: [PATCH v3 1/4] fs, net: Standardize on file_receive helper to move fds across processes」中 讨论从 _IOC 宏读取结构体尺寸，「_IOC(dir,type,nr,size)」是 BSD ioctl 宏血统的一次顺带提及。 `<!-- ROW_MINE: linux-fsdevel.messages.513930 -->`
- 【Linux社区】2014年 Al Viro(viro@zeniv.linux.org.uk) 在「[RFC] dupfs semantics」中 论证 Linux vfs 无法提供 dup 语义的文件名，「FreeBSD got away with a horrible hack」是 FreeBSD 用内核 hack 绕过、Linux 却因接口僵化而绕不过去的对比 `<!-- ROW_MINE: linux-fsdevel.messages.537670 -->`
- 【Linux社区】2015年3月 Thiago Macieira(thiago.macieira@intel.com) 在「CLONE_FD任务退出通知via文件描述符」中 确认FreeBSD pdfork接口正是用户空间所需，「pdfork()」是 BSD进程描述符向Linux CLONE_FD移植的直接模板 `<!-- ROW_MINE: linux-fsdevel.messages.590719 -->`
- 【Linux社区】2014年2月 Hin-Tak Leung(htl10@users.sourceforge.net) 在「fsck对HFS+日志的影响」中 对比XNU内核日志重放行为发现JOURNAL_RESET标志，「xnu/bsd/vfs/vfs_journal.h」是 BSD派生代码在HFS+日志语义上的跨内核参考 `<!-- ROW_MINE: linux-fsdevel.messages.612212 -->`
- 【Linux社区】2025年 Ethan Carter Edwards(ethan@ethancedwards.com) 在「[PATCH RFC v2 1/8] staging: apfs: init lzfse compression library for APFS」中 把 Apple 的 LZFSE/LZVN 库移植进 staging/apfs，「SPDX-License-Identifier: BSD-3-Clause」是 BSD-3-Clause 被直接嵌进 Linux 内核文件系统驱动的证据 `<!-- ROW_MINE: linux-fsdevel.messages.613775 -->`
- 【Linux社区】2026年3月 Bernd Schubert(bschubert@ddn.com) 在「Re: [PATCH 09/19] Move mount flags to mount_i.h」中 把 libfuse 的挂载标志表迁到 mount_i.h 并从 lib/mount.c 删除 #ifdef __NetBSD__ 下的 MS_*→MNT_* 映射与 unmount2() 包装，「Hopefully the rest of the bsd stuff can go in its own files too?」是 Darrick J. Wong 对 BSD 兼容层继续外置的确认。 `<!-- ROW_MINE: linux-fsdevel.messages.697152 -->`
- 【Linux社区】2026年4月 Christian Brauner(brauner@kernel.org) 在「Re: [PATCH v6 1/4] openat2: new OPENAT2_REGULAR flag support」中 反向追问 Linux 为何不用 BSD 的 EFTYPE，「both the bsds and macos already use that is there a good reason to return ENOTTY」是 BSD 错误码进入 Linux 文件系统 API 的张力点 `<!-- ROW_MINE: linux-fsdevel.messages.697975 -->`
- 【Linux社区】2026年 Ali Ahmet Memis(ali@iusegentoo.com) 在「[PATCH 05/10] ufs: honour on-disk immutable and append-only flags」中 提交补丁把 BSD chflags 映射到 Linux S_IMMUTABLE/S_APPEND，「ui_flags holds the BSD chflags of the inode」是 BSD 权限位跨 OS 失效的直接证据。 `<!-- ROW_MINE: linux-fsdevel.messages.698189 -->`
- 【Linux社区】2026年3月 Darrick J. Wong(djwong@kernel.org) 在「Re: [PATCH v2 11/25] Move 'struct mount_flags' to util.h」中 讨论 Bernd Schubert 把 FUSE 挂载工具结构体抽到 util.h，「!defined(__NetBSD__) && !defined(__FreeBSD__) && !defined(__DragonFly__)」是 FUSE 用户态工具跨 BSD 平台编译的分层。 `<!-- ROW_MINE: linux-fsdevel.messages.699689 -->`
- 【Linux社区】2026年7月 Pedro Falcato(pfalcato@suse.de) 在「open*(2)的O_CREAT|O_DIRECTORY」中 指出Linux三种历史行为与FreeBSD/NetBSD/macOS各持异见，「5 different behaviors all across the FOSS UNIX landscape」是 BSD分叉导致Linux VFS语义反复修正的根本原因 `<!-- ROW_MINE: linux-fsdevel.messages.705411 -->`
- 【Linux社区】2026年3月 Bernd Schubert(bernd@bsbernd.com) 在「[PATCH v2 11/25] Move 'struct mount_flags' to util.h」中 把 FUSE 挂载标志结构体挪到 util.h 并扩到 FreeBSD/DragonFly 分支，「!defined(__NetBSD__) && !defined(__FreeBSD__)」是 FUSE 在 BSD 平台族上共享代码的证据。 `<!-- ROW_MINE: linux-fsdevel.messages.710849 -->`
- 【Linux社区】2026年 Ali Ahmet Memis(ali@iusegentoo.com) 在「[PATCH 04/10] ufs: do not inherit file flags from the parent directory」中 移除 ufs_new_inode 里的父目录 i_flags 继承，「These are BSD chflags, and they have no inheritance semantics.」是 BSD 语义被 Linux 误继承的补丁级修复。 `<!-- ROW_MINE: linux-fsdevel.messages.719005 -->`

## 216.2 【Linux社区】BSD 文件系统血统与 Linux 技术流向（13 条）

- 【Linux社区】2008年10月 Alexander Larsson(alexl@redhat.com) 在「Re: interface to ask is a file is hidden」中反驳 Theodore Tso 关于 Linux 文件系统无隐藏文件概念的说法，指出 UFS、HFS/HFS+、ZFS、AFP 都支持 BSD 的 UF_HIDDEN 标志，说明 BSD 派生文件系统对 Linux VFS 抽象的反例。 `<!-- ROW_MINE: linux-fsdevel.messages.323126 -->`
- 【Linux社区】2014年4月 Christoph Hellwig(hch@infradead.org) 在「fsync_range, was: Re: munmap, msync: synchronization」中提交 fsync_range VFS 调用补丁，以 NetBSD 命名空间为蓝本移植 BSD 的范围同步 API 到 Linux。 `<!-- ROW_MINE: linux-fsdevel.messages.594797 -->`
- 【Linux社区】2020年12月 Mickaël Salaün(mic@digikod.net) 在「Landlock LSM」v22 系列中把 Landlock 与 FreeBSD Capsicum、OpenBSD pledge 等 BSD 沙箱机制并列，作为 Linux 侧文件层级 MAC 的谱系参照。 `<!-- ROW_MINE: linux-fsdevel.messages.262099 -->`
- 【Linux社区】2017年11月 Richard Narron(comet.berkeley@gmail.com) 在「msdos分区:无法挂载UFS 44bsd分区」中 提交补丁修复FreeBSD 10/11相对子分区偏移识别，「FreeBSD has relative offset if C partition offset is zero」是 BSD MBR子分区在Linux msdos分区表上的解析关键 `<!-- ROW_MINE: linux-fsdevel.messages.277074 -->`
- 【Linux社区】2006年5月 Evgeniy Dushistov(dushistov@mail.ru) 在「Re: [PATCH 2/2] ufs: directory and page cache: from blocks to pages」中 回应 Andrew Morton 关于 Linux 上如何创建 UFS 的疑问，「had a go at porting BSD ufsutils ... and nearly died」是 BSD 工具链进入 Linux 生态阻力的一处实证。 `<!-- ROW_MINE: linux-fsdevel.messages.303503 -->`
- 【Linux社区】2017年6月 Al Viro(viro@zeniv.linux.org.uk) 在「Re: UFS s_maxbytes bogosity」中 给出按 BSD 树深度计算 s_maxbytes 的实现，「for UFS2 the function I'd posted would do the right thing」是 Linux 对 FreeBSD/44BSD 位宽的定向兼容。 `<!-- ROW_MINE: linux-fsdevel.messages.408787 -->`
- 【Linux社区】2025年7月 Mickaël Salaün(mic@digikod.net) 在「Re: [PATCH v3 2/4] landlock: Fix handling of disconnected directories」中 归纳断连目录会破坏访问检查一致性，「(object) capabilities」是把已打开目录当作能力凭据的思路，正是 FreeBSD Capsicum 谱系与 Linux Landlock 的分界。 `<!-- ROW_MINE: linux-fsdevel.messages.492276 -->`
- 【Linux社区】2017年6月 Richard Narron(comet.berkeley@gmail.com) 在「Re: [git pull] first batch of ufs fixes」中 讨论 Al Viro 对 44BSD 统计位偏移的修复，「44bsd fs_maxbsize != block size => not converted」是 Linux 兼容 44BSD 磁盘格式判据。 `<!-- ROW_MINE: linux-fsdevel.messages.538754 -->`
- 【Linux社区】2003年5月 Brad Boyer(flar@pants.nu) 在「Re: [ANNOUNCE] HFS+ driver」中 就 HFS+ 长文件名与 UFS 互操作答复，「Linux UFS 读取 osx 上的 UFS」是 BSD 文件系统血统在 Mac 与 Linux 间互操作的关键检验点。 `<!-- ROW_MINE: linux-fsdevel.messages.638144 -->`
- 【Linux社区】2006年5月 Evgeniy Dushistov(dushistov@mail.ru) 在「[PATCH 2/2]: ufs: not usual amounts of fragments per block」中 提交块/片段搜索修补，「The idea is stolen from BSD code.」是 Linux UFS 直接移植 FreeBSD scanc 的自白。 `<!-- ROW_MINE: linux-fsdevel.messages.642048 -->`
- 【Linux社区】2007年6月 Evgeniy Dushistov(dushistov@mail.ru) 在「[PATCH]: ufs: restore back support of openstep」中 提交 UFS 目录 chunk 大小参数化补丁，「common UFSes (BSD and Solaris UFS)」是 Linux UFS 驱动必须兼容 BSD 磁盘变体的直接证据。 `<!-- ROW_MINE: linux-fsdevel.messages.676676 -->`
- 【Linux社区】2026年8月 Ali Ahmet Memis(ali@iusegentoo.com) 在「UFS文件系统维护者申请」中 阐明UFS驱动的跨平台定位即读取FreeBSD/NetBSD/OpenBSD/Solaris磁盘，「the only in-tree way to do it」是 BSD文件系统生态在Linux中的唯一入口 `<!-- ROW_MINE: linux-fsdevel.messages.702748 -->`
- 【Linux社区】2026年8月 Luis Henriques(luis@igalia.com) 在「ufs缓冲区容器释放」中 确认2018年泄漏修复补丁因fs/ufs无维护者未合并，「each BSD has its own thing」是 BSD变体繁多导致Linux UFS驱动被迫只读化的核心原因 `<!-- ROW_MINE: linux-fsdevel.messages.706450 -->`

## 216.3 【Linux社区】BSD 许可证在 Linux 文件系统中的落地（9 条）

- 【Linux社区】2024年 Daniel Rosenberg(drosen@google.com) 在「[RFC PATCH v4 34/36] tools: Add FUSE, update bpf includes」中 把 tools/include/uapi/linux/fuse.h 补进来，「This -- and only this -- header file may also be distributed under the terms of the BSD Licence」是 FUSE 用户态接口为 BSD 而生的许可证据 `<!-- ROW_MINE: linux-fsdevel.messages.249037 -->`
- 【Linux社区】2019年2月 Boaz Harrosh(boaz@plexistor.com) 在「[RFC PATCH 01/17] fs: Add the ZUF filesystem to the build + License」中 主张接口头文件不受许可约束，「a pure API header is not governed by ANY license」把 BSD-3-Clause 双许可的必要性放到 Linus 观点的对照上。 `<!-- ROW_MINE: linux-fsdevel.messages.304865 -->`
- 【Linux社区】2022年5月 Krzysztof Błaszkowski(kb@sysmikro.com.pl) 在「Re: [PATCH] freevxfs: relicense to GPLv2 only」中 附议 Christoph Hellwig 去掉 freevxfs 头部 BSD 风格广告许可，「an odd BSD-ish licensense with advertising clause」是 BSD 广告子句被 Linux 社区否定的样本。 `<!-- ROW_MINE: linux-fsdevel.messages.361723 -->`
- 【Linux社区】2019年3月 Boaz Harrosh(boaz@plexistor.com) 在「[PATCH 01/16] fs: Add the ZUF filesystem to the build + License」中 引入 ZUF 时明确划分双许可，「the ZUS user mode Server is a BSD-3-Clause licensed project」是 BSD-3-Clause 直接写进 Linux fs/ 的样本。 `<!-- ROW_MINE: linux-fsdevel.messages.376969 -->`
- 【Linux社区】2023年 Daniel Rosenberg(drosen@google.com) 在「[RFC PATCH v3 35/37] tools: Add FUSE, update bpf includes」中 将 FUSE UAPI 头文件随 fuse-bpf 系列补丁同步到 tools/include，「BSD-2-Clause」是 FUSE 内核接头的可选用户态双许可。 `<!-- ROW_MINE: linux-fsdevel.messages.479157 -->`
- 【Linux社区】2022年5月 Christoph Hellwig(hch@lst.de) 在「[PATCH] freevxfs: relicense to GPLv2 only」中 提交把 freevxfs 全线切换为 GPL-2.0-only 的补丁，「and drop the bogus BSD license」是 BSD 广告子句被明确否定的原文。 `<!-- ROW_MINE: linux-fsdevel.messages.525505 -->`
- 【Linux社区】2019年3月 Anna Schumaker(anna.schumaker@netapp.com) 在「Re: [RFC PATCH 01/17] fs: Add the ZUF filesystem to the build + License」中 转发并复核 BSD-3-Clause 双许可说明，「separately Licensed as BSD-3-Clause」是 BSD 许可进入 fs/ 前内部流程的落点。 `<!-- ROW_MINE: linux-fsdevel.messages.530442 -->`
- 【Linux社区】2005年12月 Steven Rostedt(rostedt@goodmis.org) 在「Re: blatant GPL violation of ext2 and reiserfs filesystem drivers」中 指出 GPL 只规约分发、BSD 内核上跑 GPL 模块属灰色地带，「BSD-licensed kernel (or library) is illegal?」是 GPL/BSD 张力的经典诘问 `<!-- ROW_MINE: linux-fsdevel.messages.556563 -->`
- 【Linux社区】2018年 Boaz Harrosh(boazh@netapp.com) 在「ZUF文件系统构建与许可」中 为NetApp的ZUF零拷贝用户态供给文件系统采用GPL-2.0或BSD-3-Clause双许可，「GPL-2.0 OR BSD-3-Clause」是 BSD许可证进入Linux新文件系统提交的标准范式 `<!-- ROW_MINE: linux-fsdevel.messages.560469 -->`

## 216.4 【Linux社区】BSD 治理智慧与 Linux 移植争议（3 条）

- 【Linux社区】2022年5月 Greg KH(gregkh@linuxfoundation.org) 在「Re: [PATCH v9 3/6] selftests: add tests_sysfs module」中 回应 Thomas Gleixner 关于 MIT/BSD 双许可的辩论，「we have enough code in the kernel which is licensed MIT/BSD」是 BSD 代码在内核中调 GPL-v2-only API 的现状陈述。 `<!-- ROW_MINE: linux-fsdevel.messages.446540 -->`
- 【Linux社区】2022年5月 Tim Bird(tim.bird@sony.com) 在「RE: [PATCH v9 1/6] LICENSES: Add the copyleft-next-0.3.1 license」中 反对把 copyleft-next 引入内核，「Dual-licensing in the Linux kernel was originally introduced because code was being taken from BSD and placed into Linux」是 BSD 代码流入 Linux 的历史性复盘。 `<!-- ROW_MINE: linux-fsdevel.messages.603727 -->`
- 【Linux社区】2025年 Aditya Garg(gargaditya08@live.com) 在「Re: [RFC] apfs: thoughts on upstreaming an out-of-tree module」中 质疑 BSD3 许可的 LZFSE/LZVN 能否进内核，「GPL-compatible, but what is the kernel's policy on external algorithms being included」是 BSD 许可进入 Linux 内核的治理争议 `<!-- ROW_MINE: linux-fsdevel.messages.667371 -->`

## 216.5 【Linux社区】附录：筛查与去重情况

- **来源**：linux-fsdevel（360,374 封）
- **BSD 价值打分**：32,814 条命中
- **BSD 变体+技术+has_bsd**：912 封
- **score≥10**：126 封
- **subject 去重后**：126 封
- **outline_worthy**：46 条（strong 19 + moderate 27）
- **precision**：46/126 = 36.5%

### 216.5.1 年份分布（46 条入纲）

- 2008: 1
- 2014: 2
- 2020: 1
- 2026: 1
- None: 41

### 216.5.2 判定分布

- moderate: 26
- strong: 19
- false: 1

### 216.5.3 精度对比

| 分层 | precision | 样本 → 入纲 |
|---|---|---|
| linux-fsdevel BSD 变体+技术 | 36.5% | 126 → 46 |
| freebsd-hackers GPL+BSD 许可 | 72.7% | 66 → 48 |
| BSD 发展列表硬过滤 | 61.7% | 128 → 79 |
| historical_claims 反向张力 | 68.4% | 19 → 13 |
| tier A 硬过滤精选 | 48.2% | 218 → 104 |
| systemd-devel BSD 硬过滤 | 40.4% | 78 → 32 |
| BSD 人物反向追溯 | 35.9% | 184 → 66 |
| ksummit BSD 相关演讲 | 25.6% | 43 → 11 |
| ZFS on Linux 专题 | 19.0% | 21 → 4 |
| fig_B1 层 | 13.5% | 222 → 30 |
| tier B 硬过滤精选 | 11% | 200 → 22 |

### 216.5.4 已知盲区

- linux-fsdevel 中 BSD 技术移植（UFS、HFS+、APFS、Landlock）的部分讨论在 score≥10 阈值下被过滤
- netdev（1,254,852 封）BSD 反向输出待执行
- BSD 安全创新反向输出专题（kqueue、jail、Capsicum、Pledge、pledge）待执行
- BSD 系统调用接口（sysctl、devfs、jails）待覆盖
