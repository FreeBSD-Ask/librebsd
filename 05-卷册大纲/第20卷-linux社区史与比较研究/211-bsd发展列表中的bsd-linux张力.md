# 211 【Linux社区】BSD 发展列表中的 BSD/Linux 张力（BSD 侧视角）
> 来源：freebsd-current（205,027 封）+ openbsd_mail（154,119 封）BSD 发展列表，1999-2024 年 Linux+GPL/license 讨论 1,293 封，硬过滤（GPL+BSD 许可双命中 OR Linux kernel 讨论）后 128 封，5 路并行读手逐封判定，79 条 outline_worthy（precision 61.7%）。
> 判定：79 CAND。主题分布：许可证 45、BSD 谱系 24、治理 6、人物 4。
> 全库去重：本次 79 条与 205/206/207/208/209/210 章 173 条 ROW_MINE 六处严格去重（BSD 列表 source 独立，0 条完全重复）。

## 211.0 【Linux社区】体例说明
本文件系 freebsd-current + openbsd_mail BSD 发展列表中 BSD/Linux 张力讨论的逐封提取产物。与 205-210 章（基于 lkml tier A/B 分层与 ZFS 专题的 BSD 技术承袭）互补，构成《给我自由》第 20 卷 lkml+BSD 列表 BSD 专题的完整图景。
**独特价值**：这 79 条是 BSD 维护者/开发者在 BSD 发展列表中主动讨论 BSD vs Linux、GPL/BSD 许可证冲突、BSD 移植到 Linux 的**一手 BSD 侧视角**，与 lkml 中的 Linux 侧视角形成对照。
**叙事主线**：GPL/BSD 许可证边界执法（webcamd 用户态包装、GPL'd code can swallow BSDL'd code 非对称法则）、BSD 拒绝 GPL 化（OpenBSD 拒绝 Linux ath 驱动、V4L2 跳过 GPL 头文件）、BSD 移植 Linux 代码（agp(4) 基于 Linux 驱动、video4bsd Linux V4L 移植、LinuxKPI 争议）、BSD 高层批评 Linux（Theo de Raadt 指控 Linux 含非自由 firmware）。
**ROW_MINE 格式**：`<!-- ROW_MINE: <source>.messages.<N> -->`，source 为 freebsd-current 或 openbsd_mail，N 为消息 id。

## 211.1 【Linux社区】GPL 与 BSD 许可证张力（45 条）

- 【Linux社区】2009年2月 Garrett Cooper(yanefbsd at gmail.com) 在“Alternatives to gcc”串中建议以BSD-licenced editline替代GPL的GNU readline，并比较“Same thing as NetBSD's libedit”的BSD跨项目同源 `<!-- ROW_MINE: fb-1028225 -->`
- 【Linux社区】2009年2月 Hans Petter Selasky(hselasky at c2i.net) 在“USB2 - libusb20 vs devel/libusb”串中指出ports中的libusb派生自Linux版本且非BSD许可，说明“the libusb code in ports is not BSD licensed”致UGEN支持无法直接搬入 `<!-- ROW_MINE: fb-1028343 -->`
- 【Linux社区】2009年10月 Daniel Gerzo(danger at FreeBSD.org) 在“FreeBSD Status Reports April - September, 2009”季报中总结Google Summer of Code 2009重写GPL版的FreeBSD ext2fs，说明“FreeBSD's ext2fs had some parts under GPL” `<!-- ROW_MINE: fb-1036823 -->`
- 【Linux社区】2010年1月 Hans Petter Selasky(hselasky at c2i.net) 在“[FreeBSD 8/9] USB webcamd and video4bsd: Call for testing”串中宣布在BSD内核中移植Linux V4L USB驱动形成video4bsd模块，公开标注“the webcamd userland program becomes GPL'ed due to the V4L USB drivers”的许可证分裂 `<!-- ROW_MINE: fb-1040883 -->`
- 【Linux社区】2011年12月 Rick Macklem (rmacklem@uoguelph.ca) 在“license question w.r.t. NFSv4.1 Layout drivers - calling all amateur lawyers”串中 请 FreeBSD core@ 判定是否可复用 Linux 布局驱动，是 BSD 项目面对 GPL 代码复用主动求助的罕见样本 ``For NFSv4.1 pNFS, there are layout drivers in Linux that I would like to reuse for the FreeBSD client` `<!-- ROW_MINE: fb-1048038 -->`
- 【Linux社区】2011年12月 Gary Jennejohn (gljennjohn@googlemail.com) 在“license question w.r.t. NFSv4.1 Layout drivers - calling all amateur lawyers”串中 发表大学版权声明优先于 MODULE_LICENSE("GPL") 声明的意见，是 BSD 项目社群对 GPL 声明优先级的民间法律解读样本 ``the university copyriught notice takes precedence over the MODULE_LICENSE("GPL")` `<!-- ROW_MINE: fb-1048074 -->`
- 【Linux社区】2012年5月 Daniel Gerzo (danger@freebsd.org) 在“FreeBSD Quarterly Status Report January-March, 2012”串中 汇总 GNU-Free C++11 栈、bsdsort 替代 GNU sort 与 linuxulator DTrace 探针工作，是 FreeBSD 系统性建立非 GPL 替代方案的项目化样本 ``Currently the BSD sort reached usable stable stage. It is stable, it is as fast as the GNU sort` `<!-- ROW_MINE: fb-1060148 -->`
- 【Linux社区】2017年2月 FreeBSD Core 团队季报(bjk@FreeBSD.org)披露 Plans to create a GPLv3 overlay for the base system were shelved，是 BSD 项目对 GPLv3 的明确治理否决 + 同期 Linux DRM 移植并存的季度实录 `<!-- ROW_MINE: fb-1089058 -->`
- 【Linux社区】2019年3月 FreeBSD Q4 2018 季报(trasz@freebsd.org) 记录 HardenedBSD 12-STABLE Released 项目段落中 PaX Team RAP 因 requires a GPLv3 toolchain and is patented 而无法为 HardenedBSD 采用，是 GPLv3 许可证直接限制 BSD 分支安全增强能力的季度实录 `<!-- ROW_MINE: fb-1097962 -->`
- 【Linux社区】2021年1月 FreeBSD Q4 2020 季报(debdrup@FreeBSD.org) 在 GPL in Base 段落披露 the base system to migrate to modern, copyfree or more permissively licensed components 并列出 gnugrep 被 bsdgrep 替换等，是 BSD 项目主动以 BSD 血统代码替换 GPL 血统工具 + 同期 Linuxulator 兼容 Linux 二进制并行推进的季度实录 `<!-- ROW_MINE: fb-1102840 -->`
- 【Linux社区】2000年5月 Thomas David Rivers(rivers@dignus.com) 在“Re: db 1.85 --> 2.x or 3.x?”串中 用 Linux 内核+FreeBSD 命令行组合追问 BSD 商业授权边界“a product came together that was the Linux kernel with the FreeBSD command set”，是 BSD 授权条款被放到 Linux 内核组合情境下检验、Sleepycat 商业授权的 BSD/Linux 参照记录 `<!-- ROW_MINE: fb-2617205 -->`
- 【Linux社区】2000年5月 Julian Elischer(julian@elischer.org) 在“Re: db 1.85 --> 2.x or 3.x?”串中 补充说明授权 grandfather 条款源自针对 Linux 内核+FreeBSD 命令行组合的确认“yes, because I recall that it was for precisely that reason”，是 FreeBSD 核心开发者在 GPL Linux 组合情境下确认 BSD 授权边界的许可证记录 `<!-- ROW_MINE: fb-2617209 -->`
- 【Linux社区】2000年10月 Mike Smith (msmith@freebsd.org) 在“Re: ACPI megapatch”串中 断言 ACPICA 的 Intel 许可与 4-clause BSD 相当并主张 FreeBSD 比 Linux 内核对 Intel 更友好，是 BSD 阵营借 ACPICA 公开评价 Linux 内核政策的关键发言 ``Given how much work the Intel people went through to get their code into the Linux kernel, I think they will find us much more` `<!-- ROW_MINE: fb-2622085 -->`
- 【Linux社区】2000年10月 Mitsuru IWASAKI (iwasaki@jp.FreeBSD.org) 在“Re: ACPI megapatch”串中 复述 ACPICA 许可证属 4-clause BSD 与 Linux 内核的 GPL 路径对比并欢迎 Intel 新贡献者，是 BSD 阵营对 Linux 内核政策的公开评价样本 ``Given how much work the Intel people went through to get their code into the Linux kernel, I think they will find us much more` `<!-- ROW_MINE: fb-2622094 -->`
- 【Linux社区】2000年10月 Mike Smith (msmith@freebsd.org) 在“Re: ACPI megapatch”串中 指出 Intel 代码使用四段 BSD 许可并断言 FreeBSD 比 Linux 内核对 Intel 贡献者更友好，是 BSD 阵营借 ACPICA 之争公开评价 Linux 内核开发政策的经典语句 ``The additional terms are just Intel's legal department trying to make the BSD license look big and scary` `<!-- ROW_MINE: fb-2622096 -->`
- 【Linux社区】2001年8月 Terry Lambert (tlambert2@mindspring.com) 在“Re: bash in /usr/local/bin?”串中 阐述 FreeBSD 通过 GPL 隔离区策略容纳 GPL 代码的机制，是 BSD 项目早期应对 GPL 传染的核心治理策略样本 ``We keep their source code in a ghetto, since we can't` `<!-- ROW_MINE: fb-2631156 -->`
- 【Linux社区】2001年8月 The Anarcat(anarcat@anarcat.dyndns.org) 在“Re: bash in /usr/local/bin?”串中反对以DOD采购为由把GPL shell搬进BSD基本系统，提出“bash is GPL, FBSD is BSD-licensed”的许可证分界 `<!-- ROW_MINE: fb-2631188 -->`
- 【Linux社区】2001年8月 Jim Bryant(kc5vdj@yahoo.com) 在“Re: bash in /usr/local/bin?”串中反驳称GPL bash不适合BSD代码树而DOD是FreeBSD唯一被认可的供应商，把许可证与DOD市场准入耦合论证 `<!-- ROW_MINE: fb-2631208 -->`
- 【Linux社区】2001年10月 Scot W. Hetzel(hetzels@westbend.net) 在“Re: Approach to integrate a driver into the kernel [winmodem]”串中核查Linux ltmodem驱动许可证以判断能否进入BSD基本系统，提出“the linux ltmodem driver was GPL'd”为关键障碍 `<!-- ROW_MINE: fb-2633004 -->`
- 【Linux社区】2002年2月 Matthew Emmerton(matt@gsicomp.on.ca) 在“Re: valgrind”串中警告FreeBSD黑客永远无法进入valgrind主发行版因该工具包含Linux内核与libc代码，形成“putting some BSD-licenced code into a GPL product”的冲突 `<!-- ROW_MINE: fb-2637035 -->`
- 【Linux社区】2002年2月 Michael Lucas(mwlucas@blackhelicopters.org) 在“Re: valgrind”串中反驳称许可证并非绝对阻碍，指出“GPL'd code can swallow BSDL'd code”的非对称性作为BSD与GPL互操作的经典判据 `<!-- ROW_MINE: fb-2637039 -->`
- 【Linux社区】2003年7月 Terry Lambert(tlambert2@mindspring.com) 在“Re: Support for XFS in FreeBSD?”串中解释GPL版XFS进入BSD基本系统的法律屏障，指出“Clause 6 of the GPL forbids including it compiled into a FreeBSD distribution kernel binary” `<!-- ROW_MINE: fb-2656044 -->`
- 【Linux社区】2010年1月 PseudoCylon(moonlightakkiy@yahoo.ca) 在“Calling for testers if_run rt3572 support”串中披露 webcamd userland program becomes GPL'ed due to the V4L USB drivers which are GPL licensed，是 BSD 用户态因链接 Linux 血统 GPL V4L 驱动而被迫整体转 GPL 的最直接技术证据 `<!-- ROW_MINE: fb-5358 -->`
- 【Linux社区】2010年8月 Doug Barton (dougb@freebsd.org) 在“Re: Official request: Please make GNU grep the default”串中 以基准数据论证 BSD grep 慢于 GNU grep 6 至 15 倍要求换默认工具，是 BSD 开发者用度量方式质疑 GNU 工具的样本 ``BSD grep is anywhere from 6 to 15 TIMES slower than GNU grep in all cases` `<!-- ROW_MINE: fb-5389 -->`
- 【Linux社区】2010年9月 Gordon Tetlow(gordon@freebsd.org) 在“Re: Difficulty playing DVDs under AHCI/CAM?”长串中援引 1. BSD licensed (old code is GPL)，是 BSD 系统以 BSD 血统代码替换被 GPL 化组件（man(1)）的许可证叙事实证 `<!-- ROW_MINE: fb-5392 -->`
- 【Linux社区】2010年11月 Daniel Nebdal 在“[head tinderbox] failure on powerpc64/powerpc”串中 将选择 BSD 许可编译器描述为优于 GPL 版本，是 BSD 阵营对 GPL 工具链的持续态度样本 ``The main thing is that it's BSD-licensed instead of GPL` `<!-- ROW_MINE: fb-5402 -->`
- 【Linux社区】2018年8月 Owen 在“Re: Sharing compiled builds between multiple 12-CURRENT boxes.”串中 批评 linuxkpi 方向应工程化 FreeBSD 内核而非变成 Linux 内核薄包装，是 BSD 内核开发者对 linuxkpi 路线的公开反对样本 ``instead of trying to turn the FreeBSD kernel into a thin wrapper around Linux kernel` `<!-- ROW_MINE: fb-6308 -->`
- 【Linux社区】2002年1月 Kjell Wooding(kjell@tash.pintday.org) 在“Re: UVM, UBC, and PF criticisms in comp.unix.solaris”串中列出 OpenBSD 未采纳 iptables 的四条理由，包括 GPL 许可不好以及 BSD 与 Linux IP 栈几乎没有共同点，为 BSD 防火墙谱系独立性的官方辩护 `<!-- ROW_MINE: ob-139346 -->`
- 【Linux社区】2004年8月 eric(eric-list-openbsd-misc@catastrophe.net) 在“[OT]: A Big Fly in the Open-Source Soup”串中转发 BusinessWeek 评论称 Apple 因许可条款更宽松拒绝 Linux 而选择 FreeBSD 作为 Mac OS X 底座，是 BSD/GPL 商业抉择最著名的一次媒体引用 `<!-- ROW_MINE: ob-172104 -->`
- 【Linux社区】2005年1月 Richard Welty(rwelty@averillpark.net) 在“Re: On first sight -Patents and IBM”串中判断 IBM 五百项专利许可与 GPL 相容但与 BSD 不相容因而不能进 OpenBSD，是 BSD 专利政策的一次技术判断 `<!-- ROW_MINE: ob-173765 -->`
- 【Linux社区】2007年10月 Karl Sjodahl - dunceor(dunceor@gmail.com) 在“Re: Wasting our Freedom”串中反驳 Toni Mueller 关于 Linux 把 BSD 代码改成 GPL 会引发大战的说法，强调 VMware 只以二进制分发而不改许可，为 GPL/BSD 法律分野的用户论战 `<!-- ROW_MINE: ob-186102 -->`
- 【Linux社区】2010年1月 Bret S. Lambert (bret.lambert@gmail.com) 在“Re: ath AR5424 support”串中 对拟从 Linux 移植的代码发出 GPL 拒绝通告，是 BSD 维护者执行 GPL 边界执法的直接样本 ``If it is GPL code, it's very unlikely to be commited` `<!-- ROW_MINE: ob-193967 -->`
- 【Linux社区】2010年3月 Gordon Grieder(grub@grub.net) 在“Re: ZFS in OpenBSD”串中 指出 BSD 阵营在放宽授权后接纳 ZFS、Linux 内核则因许可证不兼容只能走 FUSE“2 of the 3 main BSDs include ZFS with a bending of the rules, the Linux kernel does not”，是 GPL 与 CDDL 授权不兼容使 Linux 无法直接集成 ZFS、而 BSD 阵营选择放宽的许可证张力的典型叙事 `<!-- ROW_MINE: ob-194702 -->`
- 【Linux社区】2000年4月 John Wright(john@dryfish.org) 在“Re: integrating smbfs”串中追问能否把 GPL 的 smbfs 以内核模块形式并入 OpenBSD，试探 BSD 政策对 GPL 代码的实际边界 `<!-- ROW_MINE: ob-207113 -->`
- 【Linux社区】2000年5月 Theo de Raadt(deraadt@cvs.openbsd.org) 在“Re: integrating smbfs”中反问 smbfs 为何不如已内置的 GPL FP emulator 那样被接受，援引 gnu 子树作类例 `<!-- ROW_MINE: ob-207334 -->`
- 【Linux社区】2000年6月 Wes Peters(wes@dobox.com) 在“Re: RAID 1 configuration using RAIDFRAME”中披露 JFS 只能取到 OS/2 版源码且 IBM 拒改 BSD 许可因已 all-in Linux 阵营，是 GPL/BSD 生态分裂的一记实锤 `<!-- ROW_MINE: ob-207722 -->`
- 【Linux社区】2001年3月 Christopher Biggs(chris@stallion.oz.au) 在“Re: ePipe”中解释 Stallion 把 PC 版 ePipe 绑一个 mini-linux 发行版以规避 GPL 传染，为 BSD 技术商用绕开 GPL 的经典案例 `<!-- ROW_MINE: ob-213086 -->`
- 【Linux社区】2015年12月 Ingo Feinerer (feinerer@logic.at) 在“Update V4L2 API (sys/videoio.h)”串中 提交同步 Linux 视频 API 至 OpenBSD 的补丁并明示跳过 GPL2 头文件，是 BSD 项目处理 Linux 头文件时的 GPL 过滤惯例 ``which was reverted because of GPL2 considerations` `<!-- ROW_MINE: ob-233983 -->`
- 【Linux社区】2017年2月 Ingo Feinerer(feinerer@logic.at) 在“Re: Sync sys/videoio.h with recent Linux kernel”串中说明 Linux 上游同意把 v4l2-common.h 双许可为 GPL+BSD 以便 OpenBSD 完全同步 Linux 4.10-rc5 的 V4L2 API，是 Linux 上游为 BSD 用户放宽单许可的具体让步 `<!-- ROW_MINE: ob-236950 -->`
- 【Linux社区】2023年4月 Stefan Sperling(stsp@stsp.name) 在“Re: AX88179A fallback to cdce(4)”串中 指出厂商官网公开的 GPL Linux 驱动源码可作为 axen(4) 参考“There is public GPL source code for a Linux driver on the vendor page”，是 BSD 项目引用 GPL Linux 源码作参考、GPL/BSD 许可证边界被显式点出的许可证张力叙事 `<!-- ROW_MINE: ob-249763 -->`
- 【Linux社区】2001年8月 J.C. Roberts(unknown@abac.com) 在“Re: OpenBSD behavior when duplicate IP address is enabled”串中自述正在写 BSD 版 VRRP 以替换 GPL 的 Linux/FreeBSD 实现，是 BSD 血统项目回击 GPL 版本的原点帖 `<!-- ROW_MINE: ob-258992 -->`
- 【Linux社区】2000年4月 info@openbsd.org 以恶搞消息串在“OpenBSD to merge with RedHat”中虚构 Red Hat 收购 OpenBSD 并改采 Rad Hat Community Source License，戏谑 BSD/GPL 企业化融合 `<!-- ROW_MINE: ob-3067 -->`
- 【Linux社区】2001年12月 Todd C. Miller(todd.miller@courtesan.com) 在“OpenBSD 3.0 Released!”公告转述 4Front 声明 OSS 声卡驱动以 BSD 发布并被分入 Linux 与 FreeBSD 内核源码，是 BSD 声码技术向 Linux 外溢的官方口径 `<!-- ROW_MINE: ob-40 -->`
- 【Linux社区】2002年2月 Kaaren Shalom & Richard Gilligan(cosmodog@mediaone.net) 在“Text bug in http://www.openbsd.org/policy.html”串中贴出含 GPL 与 Linux 条款的 OpenBSD 版权政策页全文，其核心一句为 GPL 条款的软件不能进入 OpenBSD 内核或运行时，是 BSD 政策对 GPL 的权威定性 `<!-- ROW_MINE: ob-59588 -->`
- 【Linux社区】2024年2月 Dave Taht(dave.taht@gmail.com) 在“Re: FQ_Codel count capped at 400?”串中 指出 Linux 内核中的 fq_codel 实现本身是 BSD 许可“the linux code for this is BSD licensed”，是 BSD 技术作为实现被上游 Linux 内核纳入并保留 BSD 许可、BSD 技术流向 Linux 的许可证叙事 `<!-- ROW_MINE: ob-95277 -->`

## 211.2 【Linux社区】BSD 血统与 Linux 技术流向（24 条）

- 【Linux社区】2010年4月 Daniel Gerzo (danger@FreeBSD.org) 在“FreeBSD Status Report January-March, 2010”串中 记录 webcamd 项目让 Linux USB 设备驱动运行于 FreeBSD 而不违反 GPL，是 BSD 通过用户态包装合规复用 Linux 技术的里程碑表述 ``use the webcamd framework to make other Linux kernel USB devices work under the FreeBSD-8/9 operating system, without violating the GPL license` `<!-- ROW_MINE: fb-1038951 -->`
- 【Linux社区】2010年1月 Christof Schulze(christof.schulze at gmx.com) 在“[FreeBSD 8/9] USB webcamd and video4bsd: Call for testing”串中报告video4bsd加载失败并指出“The device is supported on linux by the gspca driver”作为覆盖度对照 `<!-- ROW_MINE: fb-1041097 -->`
- 【Linux社区】2010年10月 Daniel Gerzo(danger@freebsd.org) 在“FreeBSD Status Report July - September, 2010”中汇报 V4L support in the Linux emulator has been merged to 8-STABLE，是 FreeBSD 系统持续承接 Linux V4L 用户态技术的技术公告 `<!-- ROW_MINE: fb-1044953 -->`
- 【Linux社区】2010年9月 Doug Barton(dougb@FreeBSD.org) 在“DHCP server in base”串中反驳 Rybalko 关于 hostapd/dhcpd 入 base 的提议时主张 we can do this in a way that finds a middle ground between the linux model where literally everything is a package and the traditional BSD model of providing a "complete system"，是 FreeBSD 核心维护者直接援引 Linux 架构作为 base 边界折中参照的经典发言 `<!-- ROW_MINE: fb-1045290 -->`
- 【Linux社区】2011年12月 O. Hartmann(ohartman@zedat.fu-berlin.de) 在“Benchmark (Phoronix): FreeBSD 9.0-RC2 vs. Oracle Linux 6.1 Server”串中转述 Stefan Esser 关于 BSD 血统技术反向流入 Linux 内核的断言 many concepts were implemented in Linux based on BSD examples，是 FreeBSD 用户就 BSD 生态相对 Linux 定位的经典讨论 `<!-- ROW_MINE: fb-1047933 -->`
- 【Linux社区】2017年9月 Philip Paeps 在 Q2 2017 季报(bjk@FreeBSD.org) 中披露 I gave the "FreeBSD is not a Linux Distribution" presentation 面向 primarily Linux-oriented audience，是 BSD 项目主动在 Linux 主导场合以演讲界定自身定位的公开场合事件 `<!-- ROW_MINE: fb-1091815 -->`
- 【Linux社区】2019年9月 Kevin Oberman(rkoberman@gmail.com) 在“The support for AMD graphics and how freebsd hardware support”串中向用户解释 They are derived with minimal changes from the Linux code 且 These modules are not part of FreeBSD. They are GPL licensed, so are built as a port，是 FreeBSD 显卡驱动对 Linux 血统 + GPL 许可的最权威一手确认 `<!-- ROW_MINE: fb-1098900 -->`
- 【Linux社区】2019年9月 CSO(CSO@riseup.net) 在“The support for AMD graphics and how freebsd hardware support”串中追问 when will linux kernel 5.3 drivers arrive in freebsd，是 BSD 用户直接表达对 FreeBSD 跟进 Linux 上游驱动进度滞后的期待 `<!-- ROW_MINE: fb-1098905 -->`
- 【Linux社区】2019年9月 Johannes Lundberg(johalun@FreeBSD.org) 在“The support for AMD graphics and how freebsd hardware support”串中以 kernel drm drivers maintainer 身份声明 I would expect that 5.0 is the latest we'll support until at least early next year，是 FreeBSD 官方明确披露 Linux 上游驱动跟进滞后近半年的治理层实话实说 `<!-- ROW_MINE: fb-1098910 -->`
- 【Linux社区】2003年6月 Matt (matt@xtaz.co.uk) 在“Re: cardbus and xircom ethernet problem”串中 说明已开始基于发布的 Linux 驱动编写 FreeBSD agp(4) 驱动移植，是 BSD 系统直接引用 Linux 内核驱动代码的早期例证 ``I actually started writing a driver based on the released Linux one` `<!-- ROW_MINE: fb-12483 -->`
- 【Linux社区】2021年7月 Daniel Ebdrup Jensen(debdrup@FreeBSD.org) 在“FreeBSD Quarterly Status Report - Second Quarter 2021”中披露 the dual-licensed Intel driver ... the LinuxKPI compat framework allows us to use the driver directly，是 FreeBSD 通过 LinuxKPI 直接复用 Linux 血统驱动的季度实录 `<!-- ROW_MINE: fb-2543128 -->`
- 【Linux社区】1999年7月 Bill Paul (wpaul@skynet.ctr.columbia.edu) 在“Re: wi0 almost works with Wavelan Turbo card”串中 澄清 Linux 无线驱动基于专有 HCF 库而非真正的 Linux 驱动，是 BSD 开发者揭示 Linux 无线驱动并非开源的著名澄清 ``The full HCF is proprietary and Lucent will not release the source for it without an NDA` `<!-- ROW_MINE: fb-2602820 -->`
- 【Linux社区】2010年1月 Kohji Okuno(okuno.kohji@jp.panasonic.com) 在“Bug about sched_4bsd?”串中转述 V4L video support in the Linux emulator is now available，是 FreeBSD 系统作为 Linux V4L 应用容器持续演进的技术公告 `<!-- ROW_MINE: fb-5359 -->`
- 【Linux社区】2010年9月 Fabien Thomas(fabien.thomas@netasq.com) 在“Re: Experimental NFS server oddity”串中转述 It's now faster than on linux 并附言 This will maybe kill the long time debate about "my loopback is slow vs linux"，是 BSD 社区围绕 loopback 性能相对 Linux 优劣争论的经典用户发言 `<!-- ROW_MINE: fb-5393 -->`
- 【Linux社区】2010年10月 Hans Petter Selasky(hselasky@c2i.net) 在“FYI: ACPI buffer overflow”中 CC linux-acpi@vger.kernel.org 并明言 I belive you are using the same ACPI code like in FreeBSD，是 FreeBSD 与 Linux 上游共享同一份 ACPICA 内核代码的公开实证 `<!-- ROW_MINE: fb-5398 -->`
- 【Linux社区】2018年9月 Warner Losh(imp@bsdimp.com) 在“Re: UEFI Loader problems in CURRENT”长串中向用户说明 kstaring has ported many such changes from Linux to FreeBSD 并公开 GitHub PR 链接，是 FreeBSD snd_hda 驱动从 Linux 上游主动移植改动的维护者自述 `<!-- ROW_MINE: fb-6314 -->`
- 【Linux社区】2003年8月 Chuck Yerkes(chuck+obsd@2003.snew.com) 在“Re: Some Newbie Questions”串中 指出 OpenBSD 与所有 BSD 从源构建内核与用户空间、Linux 发行版则是内核加多源用户空间组合“OpenBSD (all BSDs) come with source for the kernel and the whole userland”，是 BSD 系统完整性相对 Linux 内核加多源用户空间组合的谱系对比、维护者视角评价 Linux 的 BSD/Linux 张力叙事 `<!-- ROW_MINE: ob-150099 -->`
- 【Linux社区】2008年7月 Travers Buda(traversbuda@gmail.com) 在“Re: atheros - just curious, ot”串中引述 Reyk Floeter 称 ath9k 不会存在若没有 OpenBSD ar5k 驱动先被 Atheros 改写为 ISC 引入 Linux ath5k 并让 Luis Rodriguez 得到 Atheros 工作，是 BSD 血统网络技术反向输入 Linux 内核的关键证据 `<!-- ROW_MINE: ob-189595 -->`
- 【Linux社区】2001年7月 Matt Evans(matt@mattevans.org) 在“Re: [linux VS openBSD]”串中评价 OpenBSD 因少而精更适合做 Web 服务器而 Linux 安全隐患多在以 root 运行的第三方包，是 BSD/Linux 对比的经典用户论辩 `<!-- ROW_MINE: ob-216086 -->`
- 【Linux社区】2001年9月 J.C. Roberts(unknown@abac.com) 在“Re Re: OpenBSD behavior when duplicate IP address is enabled”串中把 Linux/FreeBSD 的 VRRP 实现批为不合规的 hack，自证要另写 BSD 版 `<!-- ROW_MINE: ob-216367 -->`
- 【Linux社区】2016年5月 Stefan Sperling (stsp@stsp.name) 在“Re: Update iwm(4) to newer firmware”串中 移除基于 Linux iwlwifi 作为参考文档的版权声明行，是 OpenBSD 维护者逐步清理 GPL 代码引用痕迹的样本 ``Based on BSD-licensed source modules in the Linux iwlwifi driver, which were used as the reference documentation` `<!-- ROW_MINE: ob-235104 -->`
- 【Linux社区】2023年11月 Daniel Bolgheroni(daniel@bolgh.com) 在“Re: A20-OLinuXino-LIME”串中 指出厂商设备树在主线 Linux 中缺失、固件不可用“There isn't even a device tree in mainline linux for that machine”，是 OpenBSD 移植依赖主线 Linux 设备树的 BSD/Linux 谱系依赖记录 `<!-- ROW_MINE: ob-355 -->`
- 【Linux社区】2022年10月 Theo de Raadt(deraadt@openbsd.org) 在“OpenBSD 7.2 released: Oct 20, 2022”串中 在发布说明中以 Linux 上游版本号作同步基线“Updated drm(4) to Linux 5.15.69”，是 OpenBSD 内核以 Linux 上游驱动版本号作同步基线的 BSD/Linux 谱系坐标记录 `<!-- ROW_MINE: ob-3673 -->`
- 【Linux社区】2003年8月 Jon Schewe(jpschewe@mtu.net) 在“kernel/3401: Linux NFS server causes OpenBSD to hang and crash”报告里贴出 OpenBSD 挂载 Linux NFS 服务器后内核挂死与 tcpdump 现场，是 BSD 客户端直接踩到 Linux 服务端兼容性裂缝的第一手记录 `<!-- ROW_MINE: ob-78337 -->`

## 211.3 【Linux社区】BSD 治理智慧与 LinuxKPI 争议（6 条）

- 【Linux社区】2016年2月 Benjamin Kaduk (bjk@freebsd.org) 在“FreeBSD Quarterly Status Report - Fourth Quarter 2015”串中 记录 Core 团队审议是否将 GPLv3 许可代码纳入 src 主仓库，是 FreeBSD 治理层直接面对 GPL 边界的正式记录 ``the question of whether to import GPLv3 licensed code into the source repository` `<!-- ROW_MINE: fb-1084263 -->`
- 【Linux社区】2016年5月 Warren Block (wblock@wonkity.com) 在“FreeBSD Quarterly Status Report - First Quarter 2016 (fwd)”串中 披露 Core 与 John Baldwin 计划为 GPLv3 工具链组件建立独立仓库，是 BSD 治理层以仓库分离折中 GPL 合规的正式方案 ``Core, together with John Baldwin, are working on a plan to create a separate repository containing GPLv3 toolchain components` `<!-- ROW_MINE: fb-1086680 -->`
- 【Linux社区】2018年8月 Johannes Lundberg(johalun0@gmail.com) 在“drm / drm2 removal in 12”串中向用户 Owen 澄清 Linux is not "moving in to" the FreeBSD kernel，是 BSD 治理层正面回应 Linux 血统驱动是否侵蚀 FreeBSD 内核哲学的集中陈述 `<!-- ROW_MINE: fb-1092623 -->`
- 【Linux社区】2018年12月 Alexey Dokuchaev(danfe@FreeBSD.org) 在 John Baldwin 发起的“12.0 - (zpool upgrade) /bootpool”串中回复 I'm also worried if this would bring more Linuxish bits into our kernel (cf. LinuxKPI)，是 FreeBSD 维护者就 ZoL/OpenZFS 合并与 LinuxKPI 兼容代码是否渗入内核的治理层正面发声 `<!-- ROW_MINE: fb-6325 -->`
- 【Linux社区】2003年4月 Jason Hunt(leth@primus.ca) 在“Re: OpenBSD project support idea”串中反驳为 OpenBSD 编印带序列号的 BSD 许可证，认为 Red Hat 收企业 Linux 一千二百美元本质是在卖支持，把 BSD 自愿支持与 GPL 商业支持摆到了一起 `<!-- ROW_MINE: ob-148036 -->`
- 【Linux社区】2005年9月 Nick Holland(nick@holland-consulting.net) 在“Re: Any advice on Indemnification”串中列举 Red Hat 与 SuSE 提供开源免责但 BSD 项目不提供，并以 OpenBSD 维护 OpenSSH 反问，是 BSD 与 GPL 在商业治理口径的分水岭 `<!-- ROW_MINE: ob-176816 -->`

## 211.4 【Linux社区】BSD 人物在 BSD 发展列表的出场（4 条）

- 【Linux社区】2018年8月 Oliver Pinter(oliver.pinter@hardenedbsd.org) 在“Re: drm / drm2 removal in 12”串中论断 on the Linux side are the zillions of corporately paid kernel developers 与 on freebsd side, there are no corporately paid drm driver developer，是 BSD 用户直接批评 Linux 生态结构性优势与 BSD 生态人才空缺的集中陈述 `<!-- ROW_MINE: fb-6309 -->`
- 【Linux社区】2003年8月 Charles J. Fisher(cfisher@rhadmin.org) 在“Moved to misc@ RE: impressions of a new user”串中以 RedHat 转 OpenBSD 用户身份评价 BSD 许可相较 GPL 更自由并断言 Mac OS X 因 GPL 不可能存在而选了 FreeBSD，是 BSD 优于 GPL 用户口碑的集中陈述 `<!-- ROW_MINE: ob-150055 -->`
- 【Linux社区】2006年10月 Toni Mueller(openbsd-misc@oeko.net) 在“Re: GPL = BSD + DRM”串中转发 Theo de Raadt 关于 Linux 内核树充斥非自由 firmware 且版权法视之为被盗的批评并附 debian.vote 链接，是 BSD 高层对 Linux 内核合法性的直接指控 `<!-- ROW_MINE: ob-181906 -->`
- 【Linux社区】2002年3月 Christian Weisgerber(naddy@mips.inka.de) 在“RE: default shell”串中答复用户为何 OpenBSD 用 sh 而非 bash，理由是 pdksh 属公有领域而 bash 是 GPL 且更小更快，为 BSD 拒绝 GPL 血统工具的典型开发者口径 `<!-- ROW_MINE: ob-325 -->`

## 211.5 【Linux社区】附录：筛查与去重情况

- **来源**：freebsd-current（205,027 封）+ openbsd_mail（154,119 封）
- **Linux+GPL/license 讨论**：1,293 封（freebsd-current 802 + openbsd_mail 491）
- **硬过滤**：128 封（GPL+BSD 许可双命中 OR Linux kernel 讨论）
- **outline_worthy**：79 条（strong 54 + moderate 25）
- **precision**：79/128 = 61.7%

### 211.5.1 来源分布（79 条入纲）

- fb: 48
- ob: 31

### 211.5.2 年份分布（79 条入纲）

- None: 79

### 211.5.3 精度对比

| 分层 | precision | 样本 → 入纲 |
|---|---|---|
| BSD 发展列表硬过滤 | 61.7% | 128 → 79 |
| historical_claims 反向张力 | 68.4% | 19 → 13 |
| tier A 硬过滤精选 | 48.2% | 218 → 104 |
| ZFS on Linux 专题 | 19.0% | 21 → 4 |
| fig_B1 层 | 13.5% | 222 → 30 |
| tier B 硬过滤精选 | 11% | 200 → 22 |

### 211.5.4 已知盲区

- freebsd-hackers（201,463 封）未单独筛查，但与 freebsd-current 重叠
- netbsd-users（21 封）太小未纳入
- dragonflybsd 列表未检查
- P1-2（BSD 人物反向追溯 lkml 域名筛选）待执行
- P2（systemd-devel 接入）待确认数据源
