# 205 【Linux社区】LKML 中的 BSD：技术承袭、许可证冲突与人物出场

> 来源：lkml 邮件列表 6,437,908 封全库中 BSD 高价值反推 460,981 封打分候选，取 fig_B1 层（跨谱系 BSD 人物在 lkml 的独立发言）233 封，去重后 222 封（剔除 11 封与 dslinux_keywords.hits 8141 lkml 基座重复的邮件），12 路并行读手 222 封逐封读正文判定，产出 30 条入纲条目（其中 2 条 relay dup 标注保留）、4 节按 BSD 谱系/许可证/人物/治理分组。
> 判定：30 CAND / 0 NV。主题分布：BSD 谱系 21、许可证 7、人物 1、治理 1（含 relay dup 2 条冗余标注：ath10k 6448850/6420111、Vadot drm 0/2 覆盖信 v1/v2）。
> 全库去重：本次 30 条与 historical_claims 已入库 19 条 lkml、dslinux_keywords.hits 8141 lkml 基座、05-卷册大纲既有 896 message_id 引用（全部属 comp.unix.bsd 系非 lkml）三处严格去重，无一条重复。

## 205.0 【Linux社区】体例说明

本文件系 lkml 邮件列表 fig_B1 层（跨谱系 BSD 人物 222 封）的逐封提取，全 30 块采用**单行摘要体例**（丙型）：每块由“## 205.x 主题”与若干“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

**锚点归属**：本层所有条目挂 **205 【Linux社区】lkml 中的 BSD**（LKML BSD 反推专项章），不再分散到第 15 卷 284/285 章（BSD vs GPL 哲学辩论已在 284 章覆盖 BSD 授权条款与哲学层面）、289 章（BSD 代码双向流动已在 289 章覆盖 OpenZFS/libarchive/jemalloc 等跨项目机制层面）、第 20 卷 204 章（linux-man BSD 讨论已在 204 章覆盖手册页与 man-pages 层 BSD 讨论），本层聚焦 **LKML 单一讨论场域**内 BSD 技术向 Linux 的内核采纳证据、跨阵营工程师的对话、许可证冲突事件与人物出场，与既有章不重复。

**去重与已知盲区声明**：
1. **去重**：本次读手判定的 30 条已剔除 historical_claims 已入库 19 条 lkml、dslinux_keywords.hits 8141 lkml 基座、05-卷册大纲 896 message_id 中命中 lkml 的 0 条（大纲 message_id 全部来自 comp.unix.bsd 系，无一属 lkml）。
2. **relay dup 标注**：30 条中 2 条被标 relay dup（row 18 与 row 5 正文重复、row 6420111 与 row 6448850 同 thread 重复），保留以留档追溯完整讨论链，但内容主线以最早那条为准。
3. **盲区**：本次仅筛 fig_B1 层（222 封），tier A 27,100 封与 tier B 19,038 封尚未启动分拣；fig_B1 之外 anchor 主类为 bsd_variant_core（BSD 家族名直接命中）的子集尚未纳入。若 tier A 排序后仍有 BSD 主线，需另立 206/207 章。

---

## 205.1 【Linux社区】BSD 谱系：BSD 技术采纳与对照

本组共 21 条（含 1 条 relay dup），主线为 Linux 内核讨论中直接引用 BSD 代码/API 作为参考、对照或移植来源的一手史料，按年份+主题聚类：

- 【Linux社区】2001 年 8 月 Jan Harkes（CMU，FreeBSD Coda/AFS 维护者）在 LKML ext3-2.4-0.9.4 线程中，围绕 sendmail MTA 持久化语义转述 Lawrence Greenfield 的原话：“BSD softupdates allows you to call fsync() on the file, and this will sync the directories all the way up to the root if necessary… Thus BSD fsync() actually guarantees that when it returns, the file (and all of it's filenames) will survive a reboot”，以 BSD softupdates 的目录级 fsync 保证为参照，说明 Linux ext3 在 unlink+fsync 路径上存在与 BSD 语义不同的行为差异，构成 Linux 文件系统对 BSD 可靠性语义的直接技术参照 `<!-- ROW_MINE: lkml.messages.1871378 -->`
- 【Linux社区】2001 年 Jan Harkes 就 UML 跨平台构建问题回复 Alan Cox：Ryan Cumming 称 FreeBSD 原生 gcc 未定义 __linux__，Harkes 指出真正障碍是“the same coda.h header is also used as part of the FreeBSD kernel to build a Coda kernel module”，Linux 与 FreeBSD 内核的 include/typedef 要求不同，同一份 coda.h 无法识别自身归属，故主张在 arch/uml/Makefile 加入 -D__linux__ 作为跨平台共享源码的通用方案，并列举所有为多平台开发的驱动和文件系统都可能受影响，是 BSD 与 Linux 共享头文件的直接证据 `<!-- ROW_MINE: lkml.messages.1752340 -->`
- 【Linux社区】2001 年 Jan Harkes 回应 Rik van Riel 的 reverse mapping 补丁，直接引“the balancing FreeBSD does (up aging +3, down aging -1, inactive list in LRU order as extra stage)”作为 Linux 页老化改进参照，并建议匿名页在 do_nopage 即时入 active-list，是 BSD pmap 算法反向滋养 Linux 2.4 VM 的一手证据 `<!-- ROW_MINE: lkml.messages.1983190 -->`
- 【Linux社区】2001 年 Jan Harkes 在同一 page_launder 串中继续就 Rik van Riel 的 2.4.8-ac12-pmap3 补丁作评论，肯定其“completely removes the vm crawling swap_out path”并指出“aging more sanely”，其评价前提仍是 Rik 引的“the balancing FreeBSD does”，形成 Linux VM 在 2.4 周期吸纳 BSD 老化策略的双向串证 `<!-- ROW_MINE: lkml.messages.2060978 -->`
- 【Linux社区】2003 年 Andries Brouwer（TU Eindhoven）在 2.6.0-testX 磁盘几何报告串中回顾 BSD 磁盘布局历史，“BSD used to use an entirely different partition table scheme. And it was not uncommon to run a whole-disk BSD system, without any partitioning”，并举“I recall that certain Thinkpads would not boot FreeBSD even with a DOS-type partition table because the BIOS did not like the a5 partition ID”，是 BSD 分区表在 PC BIOS 生态受挫的罕见亲历陈述 `<!-- ROW_MINE: lkml.messages.2107675 -->`
- 【Linux社区】2003 年 Andries Brouwer 回应 Matti Aarnio 对 O_DIRECT 行为的疑问，Aarnio 指出“Unlike Linux, FreeBSD (where this flag originates, apparently) does not require that read()/write() happens from page aligned memory areas”，明确把 O_DIRECT 追溯到 FreeBSD 源流；Brouwer 以 Linux man page 原文对照“Transfer sizes, and the alignment of user buffer and file offset must all be multiples of the logical block size”，坐实 Linux 采纳 BSD 接口后本地化的语义收紧 `<!-- ROW_MINE: lkml.messages.1649285 -->`
- 【Linux社区】2003 年 Andries Brouwer 在 strlcpy 补丁讨论中反驳 Petr Vandrovec“kernel strlcpy implementation is crap”的批评，援引 OpenBSD 原实现 ftp://ftp.openbsd.org/pub/OpenBSD/src/lib/libc/string/strlcpy.c 和 Todd Moore 的安全分析，指出“*BSD version accesses the source past the size-1 characters that are copied: while (*s++) ;”因此用 strlcpy 替换 strncpy 处理非零终止字符数组是错的，是 Linux strlcpy 移植自 OpenBSD 后语义错配的教科书案例 `<!-- ROW_MINE: lkml.messages.1672577 -->`
- 【Linux社区】2003 年 Kris Kennaway 以 FreeBSD 工程师身份在 LKML 发出 NFS 协议分歧告警，指出 Linux 2.6.0-test7 的 lockd/xdr.h 把 NLM cookie 固化为 8 字节，而“FreeBSD 5.x's rpc.lockd uses a 16 byte cookie, and therefore FreeBSD 5.x NFS clients cannot interoperate with Linux when NFS locking is enabled”，并援引 freebsd.org PR kern/56461 作证，主张修 Linux 才是合规方向，是 NFS 协议在 Linux 与 BSD 家系间的典型不兼容证据 `<!-- ROW_MINE: lkml.messages.1693799 -->`
- 【Linux社区】2005 年 1 月 Dmitry Torokhov 向 Andries Brouwer 提交 i8042 访问时序补丁时明确写道“I peeked into FreeBSD code and they use delays to access both registers and I wonder if that's the piece that makes i8042 mysteriously fail on some boards”，把 FreeBSD i8042 驱动实现作为 Linux 2.6 输入子系统故障定位的对照基准，是 BSD 驱动代码进入 Linux 内核开发对话的直接证据 `<!-- ROW_MINE: lkml.messages.1782605 -->`
- 【Linux社区】2006 年 1 月 Suleiman Souhlal（FreeBSD 组织）在 LKML“soft update vs journaling?”线程中反驳 Diego Calleja 断言 FreeBSD“getting rid of softupdates”的说法，公开回应“You read the message wrong: We're not getting rid of softupdates”，为 BSD softupdate 策略在 Linux 社区留下明确立场——FreeBSD 在 UFS 上引入 journaling 的同时仍保留 softupdate 机制，展示 BSD 文件系统策略演进的公开锚点 `<!-- ROW_MINE: lkml.messages.1648407 -->`
- 【Linux社区】2006 年 Suleiman Souhlal 在 mad vise MADV_FREE/MADV_DONTNEED 语义讨论中援引 FreeBSD 行为作对照，“in FreeBSD, MADV_DONTNEED is not destructive, and just makes pages (including anonymous ones) more likely to get swapped out”，并支持 Andrea Arcangeli“bring Linux's behavior more in line with what other systems do”的建议，为 Linux 后续采纳 MADV_FREE 提供 BSD 语义锚点 `<!-- ROW_MINE: lkml.messages.1952032 -->`
- 【Linux社区】2009 年 FreeBSD TTY 工程师 Ed Schouten 向 LKML 报告 POSIX 伪终端 read() 返回值分歧，指出“On at least Solaris 7 to 10, Mac OS X 10.5 and FreeBSD 6 to HEAD, this code just prints 0”，而“Linux (at least 2.6.22-2.6.28)”返回 -1 EIO，并引 POSIX 标准无明确规定，是从 FreeBSD 端反向审视 Linux PTY 语义的罕见跨系统兼容证据 `<!-- ROW_MINE: lkml.messages.2613781 -->`
- 【Linux社区】2010 年 Adrian Chadd（FreeBSD ath 驱动工程师）在 LKML 回复 Luis R. Rodriguez“过去每次 multi-OS 驱动都失败”的质疑，自陈“Being involved atm in the "re-multi-OS'ing" of ath code (ie, merging some ath9k bits and pieces back into FreeBSD's HAL)”，报告 FreeBSD net80211 栈通过 HAL flags 间接调用 ath9k 位片的移植经验，是 Linux 到 FreeBSD 反向移植 ath 代码链的一手叙述 `<!-- ROW_MINE: lkml.messages.5479906 -->`
- 【Linux社区】2012 年 3 月 Adrian Chadd 回应 Joe Perches 关于 ath5k printk 宏的疑问时明确指出：“The FreeBSD HAL used to be like this. I changed it so it didn't evaluate the arguments before it figured out whether or not to do the (k)printf()”，公开说明 ath5k 的调试宏源自 FreeBSD HAL 的实践并被改良后移植到 Linux ath5k 驱动，是 BSD 无线硬件抽象层代码实践进入 Linux 内核无线栈的直接证据 `<!-- ROW_MINE: lkml.messages.5130606 -->`
- 【Linux社区】2014 年 FreeBSD 工程师 Nathan Whitehorn 反对 Rickard Strandqvist 删除 ps3_repository_write_highmem_info 的补丁，转述 Geoff Levand“These ps3_repository_write_highmem routines are also the only documentation the freeBSD port has as to how the highmem info is (should be) saved in the repository”，并自陈“we really need this for FreeBSD since that port uses the repository directly instead of FDT”，坐实 Linux 内核 PS3 子系统的代码成为 FreeBSD PowerPC 移植的隐性文档 `<!-- ROW_MINE: lkml.messages.5590345 -->`
- 【Linux社区】2017 年 Adrian Chadd 在 ath10k vif_to_arvif 补丁串中的原始发端声明“Removing this method makes the diff to FreeBSD larger, as "vif" in FreeBSD is a different pointer”，并附“Yes, I have ath10k on freebsd working and I'd like to find a way to reduce the diff moving forward”，是 FreeBSD 驱动工程师自报 Linux 上游改动对移植成本影响的一手叙述 `<!-- ROW_MINE: lkml.messages.6448850 -->`
- 【Linux社区】2017 年 Adrian Chadd 就 ath10k 驱动 vif 接口重构提出跨 OS 移植阻力，直言“Removing this method makes the diff to FreeBSD larger, as "vif" in FreeBSD is a different pointer”并自陈已在 FreeBSD 跑通 ath10k；Valo 反对因驱动分叉否决上游补丁、建议走 backports 路线，Chadd 回以“That's what you're suggesting”讥讽重命名 vif->drv_priv 的难度，反映无线驱动层 Linux/BSD 同构代码的持续拉扯〔注：与上一条同 thread 讨论链，标 relay dup 保留追溯〕 `<!-- ROW_MINE: lkml.messages.6420111 -->`
- 【Linux社区】2017 年 12 月 Edward Napierala 在 MAP_FIXED_SAFE 补丁讨论中提议采纳 FreeBSD API 命名，直接引用 FreeBSD mmap(2) 手册：“Regarding the name - how about adopting MAP_EXCL? It was introduced in FreeBSD… MAP_FIXED Do not permit the system to select a different address than the one specified… if MAP_EXCL is specified, the request will fail if a mapping already exists within the range”；Michal Hocko 以 Linux 实现方式不同为由拒绝同名复用，但明确承认 FreeBSD 先行引入该语义，形成 BSD 系统调用向 Linux 社区迁移的完整讨论链 `<!-- ROW_MINE: lkml.messages.6704486 -->`
- 【Linux社区】2014 年 FreeBSD 工程师 Ed Schouten 就 PTY read() 返回值不一致讨论回复 Alan Cox：Cox 断言“BSD sees it as EOF, Linux as hangup”，Schouten 追问二者语义差异“Would you mind explaining me the difference? I thought a modem disconnect implies an end-of-file condition?”并复现关闭 master 设备后读 TTY 返回 0，与 Linux hangup 语义不符，是 BSD 工程师在 lkml 就 Linux TTY 行为与 BSD 对照发问的一手证据 `<!-- ROW_MINE: lkml.messages.2321591 -->`
- 【Linux社区】2019 年 7 月 Emmanuel Vadot（FreeBSD 贡献者）在 LKML 提交 AM335x UART 长度修复补丁的 0/1 覆盖信，明确指出 AM335x TRM 规定 UART 寄存器区大小为 0x1000 而 DTS 误设为 0x2000，原话“I guess this is not a problem on Linux but for FreeBSD the resource manager will not allow the mapping when the region declared in the parents is less that the one declared in the child”——以 FreeBSD 资源管理器对父子区域大小严格校验的约束为动因，在 Linux 侧修正 DTS 以便 FreeBSD 内核可复用，构成 Linux DTS 为容纳 FreeBSD 内核约束而修正的跨系统设备树一致性案例 `<!-- ROW_MINE: lkml.messages.7254720 -->`
- 【Linux社区】2020 年 6 月 FreeBSD 的 ACPICA 维护者 Jung-uk Kim（jkim@freebsd.org）在 LKML 回复 Nick Desaulniers 关于 ACPICA UBSAN 空指针修复的讨论，Intel 的 Kaneda 在原回复串中主动 `+JKim (for FreeBSD's perspective)` 征询 BSD 视角；原补丁用 __builtin_offsetof 替代 ACPI_OFFSET 宏以避免 UBSAN 警告，Kaneda 指出 __builtin_offsetof 是编译器扩展，提议将 ACPI_OFFSET 改为标准 offsetof() 以便“a host OS project project to use their own definitions of offsetof in place of ACPICA's”，形成 ACPICA 跨 Linux/FreeBSD 等宿主 OS 可移植性的设计讨论 `<!-- ROW_MINE: lkml.messages.7478431 -->`

---

## 205.2 【Linux社区】BSD 与 GPL：许可证冲突与双许可辩论

本组共 7 条（含 1 条 relay dup），主线为 BSD 阵营工程师在 lkml 上直接参与 GPL 与 BSD 许可证冲突辩论、双许可实践、许可证立场自陈，与第 15 卷 284/285 章（BSD vs GPL 哲学辩论）形成一手 LKML 讨论场域互补。

- 【Linux社区】2007 年 6 月 13 日 Jan Harkes 在 Dual-Licensing Linux Kernel with GPL V2 and GPL V3 线程首次阐述 Linux 内核授权链观点：“The kernel is explicitly licensed as GPLv2, any contributions (source files/parts of the work) that wish to grant additional rights have to specify so explicitly”，并明确列出“Some authors have granted additional rights, such as dual BSD/GPL or GPLv2 and later”，以 fs/inode.c 为例说明单独分发即侵权；BSD/GPL 作为 GPL 法律解释中的一个例证，非主线但确为 BSD 在 GPLv3 争议中出现的直接文本 `<!-- ROW_MINE: lkml.messages.2522356 -->`
- 【Linux社区】2007 年 9 月 1 日 FreeBSD 内核架构师 Sam Leffler（sam@errno.com）在 lkml 转发邮件中直面 Adrian Bunk 关于 FreeBSD 移除双许可中 GPL 选项、Theo de Raadt 指控“breaking the law”的说法，以版权所有者身份为 BSD 立场辩护：“I am speaking up as the author of the code that set the dual license in place. I have the definitive say”，并交代与 onoe-san 商量 FreeBSD 树内由 dual-bsd/gpl 转为 bsd-only 的经过，重申 BSD 双许可的哲学——“I dual-licensed the code so folks could adopt and use it however they saw fit. I don't care what people do with the work I give away so long as they don't claim it's their own”——这是 BSD 阵营在 GPL/BSD 许可证冲突中最直接的原版权人发声，是 BSD vs GPL 哲学辩论在 lkml 的原声锚点 `<!-- ROW_MINE: lkml.messages.2188147 -->`
- 【Linux社区】2017 年 12 月 23 日 FreeBSD 贡献者 Emmanuel Vadot（manu@freebsd.org）向 lkml 提交 [PATCH] clk: rockchip: Switch dt-binding headers for rk3328 to GPL/X11，把 include/dt-bindings/clock/rk3328-cru.h 等 dt-binding 头从纯 GPL 改为 GPL/X11 双许可，理由明确：“Since those files are also needed kernel side, switch their licences to GPL/X11 so it can be used in BSD kernels”；补丁保留 Rockchip Electronics 的原始版权，但将 SPDX 标识从 GPL-2.0+ 改为 GPL or X11，为 BSD 内核（含 OpenBSD）纳入 Rockchip RK3328 SoC 铺路，是 BSD 生态在 Linux 内核中推动双许可以打破 GPL exclusivism 的直接技术行动 `<!-- ROW_MINE: lkml.messages.6457462 -->`
- 【Linux社区】2020 年 2 月 FreeBSD 贡献者 Emmanuel Vadot（manu@freebsd.org）向 lkml 发出 [PATCH 0/2] Dual licence some files in GPL-2.0 and MIT，直击 GPL-2.0-only 授权对 BSD 系发行版的排他壁垒，原话“Those files are a problem with BSDs as we cannot include them”，主张与 drm_client.c 主要贡献者 Noralf Trønnes、Thomas Zimmermann 及 drm_format_helper.c 贡献者 Gerd Hoffmann 协商，将两个文件从纯 GPL-2.0 改为 GPL-2.0 与 MIT 双许可，是 BSD 生态对抗 GPL exclusivism 的典型案例 `<!-- ROW_MINE: lkml.messages.7312963 -->`
- 【Linux社区】2020 年 2 月 10 日 Emmanuel Vadot 提交 [PATCH 1/2] drm/client: Dual licence the file in GPL-2 and MIT，把 drivers/gpu/drm/drm_client.c 的 SPDX 标识从 'GPL-2.0' 改为 'GPL-2.0 or MIT'，理由直白：“Change the licence to a dual one with MIT so BSDs could use this file”；该文件原始版权属于 Noralf Trønnes（2018），是 BSD 生态绕过 GPL exclusivism 的第一波系统性行动 `<!-- ROW_MINE: lkml.messages.7312964 -->`
- 【Linux社区】2020 年 2 月 10 日 Emmanuel Vadot 与 drm/client 补丁同日提交 [PATCH 2/2] drm/format_helper: Dual licence the file in GPL 2 and MIT，把 drivers/gpu/drm/drm_format_helper.c 的 SPDX 由 'GPL-2.0' 改为 'GPL-2.0 or MIT'，正文与上一条同原话“Change the licence to a dual one with MIT so BSDs could use this file”；该文件版权归 Noralf Trønnes（2016）与 Gerd Hoffmann，与前一条构成 BSD 阵营进入 Linux DRM 子系统的完整双许可改造案例 `<!-- ROW_MINE: lkml.messages.7312965 -->`
- 【Linux社区】2020 年 2 月 15 日 Emmanuel Vadot 提交 [PATCH v2 0/2] Dual licence some files in GPL-2.0 and MIT，正文与 2020 年 2 月那条 [PATCH 0/2] 完全一致（is_dup_body=1，标 relay dup），仍主张将 drm_client.c 与 drm_format_helper.c 改为 GPL-2.0/MIT 双许可以解除 BSD 无法纳入的困境，原文引用“Those files are a problem with BSDs as we cannot include them”〔注：v2 版本与 v1 正文重复，保留追溯〕 `<!-- ROW_MINE: lkml.messages.7328574 -->`

---

## 205.3 【Linux社区】BSD 人物在 LKML 的出场

本组 1 条，BSD 阵营工程师在 lkml 上以技术身份参与的独立事件，非技术承袭或许可证辩论，反映 BSD 人物在 lkml 的存在感与身份张力。

- 【Linux社区】2006 年 1 月 16 日 BSD 网络传奇人物 Sam Leffler（errno.com）回复无线配置争议，就 bg scanning 与 power save 交互展开技术辩论，原文“The way you implement bg scanning is to notify the ap you are going into power save mode before you leave the channel (in sta mode). Hence bg scanning and power save operation interact”，并澄清“If you do not have an association you are not doing bg scanning”；这是 4.4BSD 网络协议栈作者（Linux net/ipv4 大量承袭其代码）在 lkml 的直接参与，是 BSD 人物现身 lkml 的教科书样本，BSD 词本身在正文 0 提及，BSD 相关仅体现在作者身份 `<!-- ROW_MINE: lkml.messages.2290842 -->`

---

## 205.4 【Linux社区】BSD 治理智慧反哺 Linux

本组 1 条，BSD 社区治理经验被引入 lkml 讨论作为政策对照，反映 BSD→Linux 双向治理知识流动。

- 【Linux社区】2012 年 4 月 Adrian Chadd 就 Greg KH 对 3.3.2-stable 审核政策的严格把关表态：“Greg is doing the right thing here. We face the same deal in FreeBSD - people want fixes to go into a release branch first, but if you do that you break the development flow… Once you open that particular flood gate, it's hard to close. We had this problem with Squid… We over in the BSD world know just how painful that is”，把 BSD 社区与 Squid 版本流的历史教训直接作为 Linux 稳定分支工程方法论的支撑依据，展示 BSD 社区治理智慧对 Linux 的横向借鉴 `<!-- ROW_MINE: lkml.messages.5415460 -->`

---

## 205.5 【Linux社区】附录：读手判定与已知盲区

### 205.5.1 已入纲 30 条明细

| 节段 | 条数 | 主题聚类 |
|---|---|---|
| 205.1 BSD 谱系 | 21 | FreeBSD 内存管理 / 无线驱动移植 / O_DIRECT 与 strlcpy 移植 / PTY 语义 / softupdates / madvise / AM335x DTS / ACPICA / 分区表与 BIOS |
| 205.2 BSD 与 GPL 许可证 | 7 | BSD/GPL 双许可立场（Leffler）/ GPL v2/v3 授权链 / GPL-2/MIT 双许可补丁（Vadot）/ RK3328 GPL-X11 双许可 |
| 205.3 BSD 人物 | 1 | Sam Leffler 4.4BSD 网络栈作者在 lkml 无线配置争议出场 |
| 205.4 BSD 治理 | 1 | FreeBSD 治理智慧反哺 Linux stable 政策（Chadd） |

### 205.5.2 剔除情况

- **fig_B1 dedup 剔除**：233 候选 → 222 保留（11 条被 dslinux_keywords.hits 已挖掘的 8141 lkml 基座剔除）
- **historical_claims 交叉验证**：222 条中 0 条落在 historical_claims.raw_source 已入库 19 条 lkml 集合内（无重合）
- **大纲 msg_id 交叉验证**：222 条中 0 条 message_id 出现在 05-卷册大纲既有 896 message_id 中（大纲 message_id 全部属 comp.unix.bsd 系非 lkml）
- **读手判定剔除**：222 条中 192 条 spurious（BSD 仅在邮箱域名/CC 抄送/LICENSE 头/偶然提及，主线无关），30 条 outline_worthy

### 205.5.3 系统性误配模式（192 条 spurious 归纳）

1. **BSD 阵营工程师身份误命中**（约 90 条）：Andries Brouwer（TU Eindhoven）、Jan Harkes（CMU AFS/Coda）、David Wagner（UC Berkeley 安全）三类“Unix 邻域”学者因邮箱域名（win.tue.nl / cs.cmu.edu / cs.berkeley.edu）或 fig_on 分类器命中 BSD 邻域，但正文完全无 BSD 参与。这些条目反映的是 Linux 内核社区内部技术讨论，不属 BSD 主线。
2. **GPL 内部争论被误标 GPL_BSD_lic**（约 45 条）：BitKeeper 争论、GPLv2/GPLv3 兼容、TiVoization、二进制模块争论、SCO 诉讼考古等，hits 中“bsdi”由“BitKeeper”缩写误命中或“sco”由 SCO 命中但正文无 BSD 代码引用。
3. **BSD 阵营工程师提交 Linux DTS 补丁**（约 25 条）：Emmanuel Vadot（manu@freebsd.org）Allwinner SoC 设备树、Adrian Chadd（adrian@freebsd.org）ath10k 内存讨论、Jung-uk Kim（jkim@freebsd.org）ACPICA UBSAN 回复——仅因 FreeBSD 邮箱域名命中锚点，正文全为纯 Linux 内核 DTS / 内存 / ACPICA 讨论。
4. **邮件主题词偶然命中**（约 25 条）：tcpdump / sendmail / disklabel / bsd: hde 分区标签名等 Linux 内部技术词汇偶然触发 BSD 关键字。
5. **纯 Linux 内部技术讨论**（约 7 条）：Coda 编译、LILO 分区、Coda 模块平台、kexec_file_load efi=noruntime 等，BSD 词只作枚举项或转发捕获。

### 205.5.4 已知盲区与后续工作

1. **fig_B1 之外 460,981 打分池未挖**：本次仅筛 fig_B1 层 222 封，anchor 主类为 `bsd_variant_core`（BSD 家族名直接命中）与 `usl_sco_litigation`（SCO 诉讼涉 BSD 代码）的 tier A/B 尚未启动分拣，估计仍有 50-200 条 BSD 主线史料。
2. **tier A 精度低风险**：TierA top-100 抽样验证 precision 仅 10%，主要噪声模式与本次 fig_B1 spurious 一致（GPL 内部争论 28%、Alan Cox -ac 25%、补丁 LICENSE 头 17%）；tier A 分拣需引入“正文 BSD 命中数 ≥ 3 且非 LICENSE 头”硬过滤后再派读手。
3. **relay dup 未完全去重**：本层 30 条中 2 条 relay dup（row 18 与 row 5；row 6420111 与 row 6448850），保留以留档追溯完整讨论链；若最终成稿去重可再删 2 条。
4. **人物身份未交叉验证**：本层 30 条叙述中的 BSD 人物身份（Sam Leffler / Emmanuel Vadot / Adrian Chadd / Jan Harkes / Ed Schouten / Suleiman Souhlal / Edward Napierala / Jung-uk Kim / Nathan Whitehorn 等）均按邮件签名和邮箱域名推定，未做独立事实核查；正式入卷块撰写前应经术语审阅与三审交叉核对。
5. **未做正文全量抽取**：本层叙述句均从 body[:1500] 至 body[:3000] 截取，未回源抽取完整正文做全文本证据链；如需在正式入卷块中引用长段落原文，须回源至 lkml.duckdb 抽完整 body 字段。

---

## 数据核验与统计（自动增补 · 0-信任）

> **来源库**：`03-原始史料库/11-邮件列表史料/05-linux-kernel/mining/05b-lkml专题/05-数据库/lkml_value_scores.duckdb`（460,981 打分行）、`03-原始史料库/11-邮件列表史料/05-linux-kernel/mining/05b-lkml专题/03-候选/lkml_candidates_figB1.jsonl`（233 候选）、`06-入纲/prepped/figB1_dedup.jsonl`（222 保留）、`06-入纲/subagents/chunk_01..12.jsonl`（222 判定）
> **方法**：DuckDB 全量打分 + Python 6 层去重 + 12 路并行读手逐封读正文回检索关键字
> **生成时间**：2026-09-22 ｜ **复现**：`03-原始史料库/11-邮件列表史料/05-linux-kernel/mining/05b-lkml专题/06-入纲/_prep_dedup.py` + `_prep_chunks.py`

| 指标 | 数值 |
| --- | --- |
| lkml 全库消息数 | 6,437,908 |
| 打分池（BSD 相关候选） | 460,981 |
| fig_B1 层候选 | 233 |
| fig_B1 dedup 后 | 222 |
| 读手判定 outline_worthy | 30 |
| spurious | 192 |
| 精确率（outline_worthy / dedup 后） | 13.5% |

**数据质量备注**：本层精确率 13.5% 显著高于 tier A top-100 抽样验证的 10%（因 fig_B1 层已按 fig_cls 严格筛选），但仍低于 204 章（linux-man 280/1467 = 19%）；后续 tier A 分拣需引入正文 BSD 命中硬过滤才能提升至 20%+。
