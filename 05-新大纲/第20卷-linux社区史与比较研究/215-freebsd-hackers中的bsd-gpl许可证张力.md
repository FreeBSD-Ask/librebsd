# 215 【Linux社区】freebsd-hackers 中的 BSD/GPL 许可证张力与 BSD 维护者讨论

> 来源：freebsd-hackers（201,463 封，2015-2026 活跃），BSD 价值打分 147,686 条命中，GPL+BSD 许可双命中 OR BSD 变体/技术命中后 1,347 封，score≥30 后 191 封，subject 去重后 66 封，3 路并行读手逐封判定，48 条 outline_worthy（precision 72.7%）。
> 判定：48 CAND。主题分布：许可证 40、治理 5、BSD 谱系 2、人物 1。
> 全库去重：本次 48 条与 205-214 章 356 条 ROW_MINE 九处严格去重（freebsd-hackers source 独立，0 条完全重复）。

## 215.0 【Linux社区】体例说明
本文件系 freebsd-hackers 列表中 BSD/GPL 许可证张力讨论的逐封提取产物。与 205-210 章（基于 lkml tier A/B 分层的 BSD 技术承袭）、211 章（BSD 发展列表 BSD 侧视角）、213 章（systemd-devel BSD 张力）、214 章（ksummit BSD/Linux 张力）互补，构成《给我自由》第 20 卷 BSD 专题的完整图景。
**独特价值**：这 48 条是 FreeBSD 维护者在 freebsd-hackers 列表中讨论 GPL/BSD 许可证冲突、BSD 拒绝 GPL 化、BSD 移植 Linux 代码、BSD 高层批评 Linux 的**一手 BSD 维护者视角**，覆盖 1995-2024 近 30 年 BSD/GPL 张力史。
**叙事主线**：1995 Stacey 拒绝 GPL（FPE）、1998 Dyson“GPL license, or other restrictive terms”、1999 Doug 反 GNU GLOBAL、1999 Seth Leigh BSD→GPL relicense、2000 Sobral“GPL is brain-damaged”、2000 Pouzzner ALSA→newpcm、2001 Morin Apple MkLinux→BSD、2001 Craig“FreeGPL”、2004 Siddharthan GPL copyleft、2008 Maslan lguest IBM GPL、2011 Lock Linux DVB LGPL、2020 Paetzel open-vm-tools GPL、2024 obiwac LinuxKPI BATMAN GPL。
**ROW_MINE 格式**：`<!-- ROW_MINE: freebsd-hackers.messages.<N> -->`，N 为消息 id。

## 215.1 【Linux社区】GPL 与 BSD 许可证张力（40 条）

- 【Linux社区】1998年6月 Ada(ada@noether.lab.usyd.edu.au) 在“2.2.6 CD-ROM : Package dependencies up the creek ?”串中 拒斥 bash 引入 contrib 树并推荐 zsh 替代，“bash is A) huge B) GPL”，是 BSD 社区早期以许可证为由排除 GPL 组件的社区共识样本 `<!-- ROW_MINE: freebsd-hackers.messages.16621 -->`
- 【Linux社区】2003年12月 omestre(omestre@freeshell.org) 在“sis 7018”串中 询问是否可将Linux GPL驱动的sis7018声卡移植到Solaris，“the driver license is GPL, and i do not know if i can do that (LGPL)”是 用户在BSD/Linux驱动间权衡GPL兼容性的典型问讯 `<!-- ROW_MINE: freebsd-hackers.messages.1274172 -->`
- 【Linux社区】2003年12月 Joe Warner(rootman22@comcast.net) 在“Nvidia Licensing Question”串中 追问Nvidia NIC驱动非GPL却可供Linux使用的原因，“FreeBSD constrains itself somewhat by taking the GPL/BSD license only philosophical stand”是 FreeBSD因GPL/BSD许可哲学拒收厂商非GPL驱动的早期代表 `<!-- ROW_MINE: freebsd-hackers.messages.1274540 -->`
- 【Linux社区】2004年 Rahul Siddharthan (rsidd at online.fr) 在“Copyrights (was: Where is FreeBSD going?)”串中论证版权转让并非必需并比较“the GPL explicitly exempts mere aggregation”与 BSD 版权治理逻辑，是 BSD 社区在许可证治理层面正面解构 GPL 传染性论的经典辩护 `<!-- ROW_MINE: freebsd-hackers.messages.1279222 -->`
- 【Linux社区】2005年2月 Edward Smith III(ed.smithiii@us.army.mil) 在“Star & FreeBSD”串中 追问Jörg Schilling将star从GPL改为CDDL后是否可入FreeBSD，“you may have a program that behaves 98% like gnu tar but is not based on the GPL”是 工具方主动从GPL切换到CDDL以兼容BSD的具体案例 `<!-- ROW_MINE: freebsd-hackers.messages.1283917 -->`
- 【Linux社区】2007年 Julian H. Stacey (jhs at berklix.org) 在“Wine compatibility and performance on FreeBSD 7 ”串中讨论 Wine“work as of March 2002 has used the LGPL”并设想为“a wine user who doesnt like GPL”提供 wine-rewind 端口，是 BSD 用户在 GPL/LGPL 葡萄酒兼容性议题上的边缘技术讨论 `<!-- ROW_MINE: freebsd-hackers.messages.1292377 -->`
- 【Linux社区】2008年 Robert Watson (rwatson at FreeBSD.org) 在“licensing question APSL”串中阐述 FreeBSD 立场“on-going efforts to identify and replace non-BSD licensed code with BSD licensed code”并列举 ZFS/DTrace 的 CDDL 隔离实践，是 BSD 治理层制度化处理非 BSD 许可证代码的纲领性表述 `<!-- ROW_MINE: freebsd-hackers.messages.1296665 -->`
- 【Linux社区】2008年7月 Alexander Leidinger(Alexander@Leidinger.net) 在“TET and other testing framework for FreeBSD”串中 就LTP测试框架BSD/GPL双授权提议表态，“here the license matters”是 FreeBSD测试体系引入GPL来源框架时的许可权衡 `<!-- ROW_MINE: freebsd-hackers.messages.1297677 -->`
- 【Linux社区】2008年 Maslan (maslanbsd at gmail.com) 在“vkernel & GSoC, some questions”串中引证 Kip Macy 的警告“It is called lguest, is GPL, IBM has the rights to it and has no interest in changing the license”，是 FreeBSD 试图复刻 Linux KVM 虚拟化技术时撞上 IBM 独家 GPL 权利的标志性挫败 `<!-- ROW_MINE: freebsd-hackers.messages.1298420 -->`
- 【Linux社区】2011年 Juergen Lock (nox at jelal.kn-bremen.de) 在“Does this Linuxolaotor DVB wrapper port look good now?”串中将 Linux DVB 兼容层从内核拆为端口原因是“one of the header contains lgpl'd parts out of the Linux dvb headers”，是 BSD/Linux 兼容层内核边界因 GPL/LGPL 传染性被迫收缩的实证 `<!-- ROW_MINE: freebsd-hackers.messages.1306916 -->`
- 【Linux社区】2011年4月 Nathan Whitehorn(nwhitehorn@freebsd.org) 在“dialog(1) changed in RELENG_9”串中 说明以cdialog替换dialog(1)的许可理由，“has a better license (LGPL instead of GPL)”是 FreeBSD以GPL到LGPL为动因替换GNU工具的案例 `<!-- ROW_MINE: freebsd-hackers.messages.1306935 -->`
- 【Linux社区】2013年 Isabell Long(issyl0 at FreeBSD.org) 在“FreeBSD Quarterly Status Report, July-September 2012.”报告 记录 Cambridge 峰会推动 clang 切换进程，“bring us one big step closer to a GPL-free FreeBSD 10”，是 BSD 社区以工具链迁移摆脱 GPL 依赖的官方叙事证据 `<!-- ROW_MINE: freebsd-hackers.messages.1315779 -->`
- 【Linux社区】2015年 Chris H (bsd-lists at bsdforge.com) 在“GSoC 2015 Task: Unifying ping and ping6”串中透露 liboping 作者愿意从“LGPL/GPLv2 licensed”重释为“BSD/MIT”，是 BSD 社区借 GSoC 机制尝试驯化 GPL 生态工具进入基线的边缘案例 `<!-- ROW_MINE: freebsd-hackers.messages.1320661 -->`
- 【Linux社区】2015年9月 Jack Vogel(jfvogel at gmail.com) 在“GPL issues around OFED code in FreeBSD 9.1”串中 追问 Mellanox OFED 代码为何未被多许可证发布，“they should have released the code somewhere without any GPL license in it”，是 GPL 代码进入 FreeBSD 基础的当代 OFED 争议样本 `<!-- ROW_MINE: freebsd-hackers.messages.1321512 -->`
- 【Linux社区】2020年 Josh Paetzel (jpaetzel at FreeBSD.org) 在“open-vm-tools in base”串中提议将 VMware 工具并入 base 引发争议“the vmmemctl driver for FreeBSD is GPL'd, and vmblock is under 2-clause BSDL. Do we accept GPL'd kernel modules?”，是 FreeBSD 治理层就 GPL 内核模块入基线展开的历史性辩论 `<!-- ROW_MINE: freebsd-hackers.messages.1328806 -->`
- 【Linux社区】1995 年 2 月 21 日 Jordan K. Hubbard（jkh () violet ! berkeley ! edu）在“Re: Linux vs. BSD?!”串中回应 Larry McVoy 关于 NetBSD 与 FreeBSD 虽为自由源码、却没有公司提供商业支持因而对企业不是好选择的论断，认为 BSDI 的核心贡献是支持与稳定性，"Nothing that the GPL or BSD copyrights have much effect over"，技术如今已成易事，并公开质疑 FSF 阵营的商业分量：“unless the FSF becomes the "Free Support Foundation", I can't see them as having that large an impact”。`<!-- ROW_MINE: freebsd-hackers.messages.2515805 -->`
- 【Linux社区】1998年2月 Sean Eric Fagan(sef@kithrup.com) 在“Re: kirk's soft-update integration..”串中 类比 Kirk soft-update 许可证与 GPL 第四条款的相似性，“If you read the fourth clause, it requires, like the GPL, that the entire program's source be included”，是 BSD 维护者对 BSD 许可证与 GPL 义务等同性的早期法律论证 `<!-- ROW_MINE: freebsd-hackers.messages.2525989 -->`
- 【Linux社区】2023年5月 Lorenzo Salvadore(developer@lorenzosalvadore.it) 在“Re: freebsd on an ebook ereader ?”串中 解释BSD许可对厂商的吸引力，“many companies love the BSD license. The fact that it is more open than the GPL”是 BSD与GPL许可哲学的现代对照陈述 `<!-- ROW_MINE: freebsd-hackers.messages.2536253 -->`
- 【Linux社区】2023年 Lorenzo Salvadore(developer@lorenzosalvadore.it) 在“Re: FreeBSD mobile phone port”串中 回应质疑者对 BSD 许可证商业可持续性的怀疑，“the fact that it is more open than the GPL allow them to keep their sources closed”，是 BSD 许可证相对 GPL 商业友好性的当代官方反驳 `<!-- ROW_MINE: freebsd-hackers.messages.2536255 -->`
- 【Linux社区】2024年 obiwac (obiwac@freebsd.org) 在“Re: Questions about best practices w.r.t. writing a kernel module port which modified LinuxKPI (BATMAN)”串中询问 FreeBSD 政策“the kernel module for batman can't be shipped with FreeBSD as it's GPL”，是 BSD 维护者在 LinuxKPI 移植 Linux 内核模块时直面 GPL 传染性约束的实证 `<!-- ROW_MINE: freebsd-hackers.messages.2536711 -->`
- 【Linux社区】2024年 Cy Schubert(Cy.Schubert@cschubert.com) 在“Re: Help wanted on porting a wifi library from Linux to FreeBSD”串中 阻止 GPL 代码移植 FreeBSD，“Porting GPL code to FreeBSD is not a good idea. A rewrite under a BSD license would work though”，是 BSD 社区以许可证为由拒绝 Linux 代码移植的当代明确表态 `<!-- ROW_MINE: freebsd-hackers.messages.2537558 -->`
- 【Linux社区】1995年5月 Justin T. Gibbs(gibbs@estienne.CS.Berkeley.EDU) 在“Re: SVNET Meeting?”串中 记述SVNET会议被问GPL为何邪恶并辩护FreeBSD保留GPLd内核片段，“so long as the GPLd portions are clearly marked and easily removed, it is foolish to keep these features out”是 FreeBSD在BSD与GPL分裂期对混入GPL代码政策的系统表态 `<!-- ROW_MINE: freebsd-hackers.messages.2544114 -->`
- 【Linux社区】1995年 Julian Howard Stacey (jhs@freebsd.org) 在“Re: i can help ”串中转述 FreeBSD 拒绝替换 FPE 的立场“the only reason we haven't taken the Linux version is the fact that the damn thing's GPL'd”，是 BSD 阵营因 GPL 传染性拒绝吸收 Linux 成熟组件的原始档案 `<!-- ROW_MINE: freebsd-hackers.messages.2545410 -->`
- 【Linux社区】1995年6月 Peter Wemm(peter@haywire.DIALix.COM) 在“GPL code in freebsd?”串中 就Alan Cox指控FreeBSD含GPL ISDN代码发帖回应，“FreeBSD is already internally in violation of its own licenses”是 GPL执法者对FreeBSD的早期版权指控 `<!-- ROW_MINE: freebsd-hackers.messages.2550137 -->`
- 【Linux社区】1997年 Rodney W. Grimes(rgrimes@gndrsh.aac.dev.com) 在“Re: GPL code in freebsd?”串中 回应 Alan Cox 对 FreeBSD 内嵌 GPL 代码的指控，“they don't have a leg to stand on”，是 BSD 社区最早硬刚 GPL 污染指控的防御立场存档 `<!-- ROW_MINE: freebsd-hackers.messages.2550138 -->`
- 【Linux社区】1997年 Terry Lambert(terry@lambert.org) 在“Re: Porting device drivers...”串中 论证 UCB 许可证与 GPL 的冲突根源，“the UCB license conflicts with the GPL. Therefore code can only be GPL or UCBL, not both simultaneously”，是 BSD 维护者首次系统性论证 Linux GPL 代码无法合入 BSD 内核的法律基础 `<!-- ROW_MINE: freebsd-hackers.messages.2582943 -->`
- 【Linux社区】1997年 John S. Dyson(toor@dyson.iquest.net) 在“Re: Commercial vendors registry”串中 解释FreeBSD因Kermit非GPL未纳入发行版的原因，“That is the only reason that we don't have Kermit on our distribution”是 BSD阵营GPL/BSD-only许可立场的具体执行 `<!-- ROW_MINE: freebsd-hackers.messages.2585200 -->`
- 【Linux社区】1998年 John S. Dyson (dyson@FreeBSD.ORG) 在“Re: The BSD License”串中为 FreeBSD 立场定调“There are components that come with FreeBSD, not necessary for a basic runtime, that come under a GPL license”，是 BSD 社区明确划定 GPL 组件边界并声明不背锅的历史宣言 `<!-- ROW_MINE: freebsd-hackers.messages.2600915 -->`
- 【Linux社区】1999年 Seth Leigh (seth@pengar.com) 在“Not so sinister. Was:(Re: Attempt to relicense BSD code under the GPL)”串中平复争议并澄清“they are not attempting to relicense stuff they have used from other, BSD-licensed sources”，是 BSD 社区首次大规模遭遇并平息 GPL 强加 BSD 代码事件的档案记录 `<!-- ROW_MINE: freebsd-hackers.messages.2614907 -->`
- 【Linux社区】1999年 Doug (Doug@gorean.org) 在“Re: GNU GLOBAL”串中强烈反对 Shigio Yamaguchi 的转向“It means that it will be released under GPL instead of BSD license”并断言“The GNU license interferes with the goals of the FreeBSD project”，是 BSD 社区在软件许可证战线上公开发难 GPL 意识形态的关键檄文 `<!-- ROW_MINE: freebsd-hackers.messages.2623784 -->`
- 【Linux社区】2000年 Daniel C. Sobral (dcs@newsguy.com) 在“Re: Motif goes open source”串中评点 OpenMotif 许可证并直言“GPL is brain-damaged. It is, essentially, incompatible with anything but GPL”以及 BSD 许可证“had to have a clause removed”，是 BSD 老将对 GPL 传染性公开宣战且承认 BSD 许可证已为此改造的历史性表态 `<!-- ROW_MINE: freebsd-hackers.messages.2630670 -->`
- 【Linux社区】2000年 Daniel Pouzzner (douzzer@mega.nu) 在“Re: new device drivers for RME soundcard and G400-TV”串中主张将 ALSA 驱动移植到 newpcm“morphed into a newpcm driver”以规避“GPL'd driver”风险，是 BSD 维护者主动改造 Linux 技术绕开 GPL 传染性的经典策略示范 `<!-- ROW_MINE: freebsd-hackers.messages.2630935 -->`
- 【Linux社区】2001年 Andrew Hesford(ajh3@chmod.ath.cx) 在“Re: Should I switch? [was Re: A novel idea....]”串中 解释 FreeBSD 相比 Linux 的自由度差异，“the license FreeBSD is distributed under is so free (much more so than the GPL)”，是 BSD/GPL 双许可证商业自由度对比的普及化叙事 `<!-- ROW_MINE: freebsd-hackers.messages.2640164 -->`
- 【Linux社区】2001年6月 Peter(fbsdq@yahoo.com) 在“Re: Query:  How to tell if Microsoft is using BSD TCP/IP code?”串中 分析Bill Gates反GPL立场，“Microsoft isn't anti open-source, it's anti GPL”是 BSD与GPL在企业软件战略层面的张力代表 `<!-- ROW_MINE: freebsd-hackers.messages.2642525 -->`
- 【Linux社区】2001年 Craig R (craigery13@hotmail.com) 在“Re: Framebuffer device under FreeBSD?”串中反对直接吸收 Linux fbdev 代码并警告“Just picture having tons of GPL code and changing the name to FreeGPL”，是 BSD 社区以 GPL 传染为由拒绝吸收 Linux 成熟图形技术从而保持独立性的经典立场 `<!-- ROW_MINE: freebsd-hackers.messages.2647618 -->`
- 【Linux社区】2001年12月 Hiten Pandya(hitmaster2k@yahoo.com) 在“Re: [SUGGESTION] - JFS for FreeBSD”串中 主张通过src/gnu目录接纳GPL的IBM JFS，“we have an src/gnu directory... that's what it is for... dumping GPL'ed stuff”是 FreeBSD引入GPL文件系统的早期实践方案 `<!-- ROW_MINE: freebsd-hackers.messages.2648438 -->`
- 【Linux社区】2002年1月 Ashutosh S. Rajekar(asr@max-t.com) 在“Re: The Hurd”串中 反对FreeBSD吸纳Hurd代码，“GPL conflicts with FreeBSD's artistic license”是 BSD与GNU/Hurd许可冲突的具体表态 `<!-- ROW_MINE: freebsd-hackers.messages.2649151 -->`
- 【Linux社区】2002年 Robert Watson(rwatson@FreeBSD.org) 在“FreeBSD Development Status Report: May, 2002 - June, 2002”发布 BSDCon 2003 论文征集，“Comparison with non-BSD operating systems; technical, practical, licensing (GPL vs. BSD)”，是 BSD 会议议程将 GPL/BSD 对比确立为核心议题的证据 `<!-- ROW_MINE: freebsd-hackers.messages.2655284 -->`
- 【Linux社区】2002年 Terry Lambert(tlambert2@mindspring.com) 在“Re: intermezzo?”串中 解释GPL InterMezzo不能成为FreeBSD启动FS的原因，“It's illegal to distribute a binary FreeBSD distribution with GPL'ed components linked into the kernel because of clause 6 of the GPL”是 GPL第6条对FreeBSD内核分发的实质限制 `<!-- ROW_MINE: freebsd-hackers.messages.2655897 -->`
- 【Linux社区】2002年 Terry Lambert(terry@lambert.org) 在“RE: intermezzo?”串中 解释 GPL 组件无法静态链接进 FreeBSD 内核的法律边界，“it is illegal to distribute a binary FreeBSD distribution with GPL'ed components linked into the kernel because of clause 6 of the GPL”，是 BSD 社区最早对 GPL 内核链接禁忌的公开法律分析 `<!-- ROW_MINE: freebsd-hackers.messages.2655933 -->`

## 215.2 【Linux社区】BSD 血统与 Linux 技术流向（2 条）

- 【Linux社区】2012年6月 Richard Yao(ryao@gentoo.org) 在“Replacing rc(8)”串中 提议Gentoo/OpenRC反哺FreeBSD基座init系统，“Adoption of OpenRC in FreeBSD init system would enable us to pool our resources”是 BSD变体间(Gentoo到FreeBSD)init技术协作的尝试 `<!-- ROW_MINE: freebsd-hackers.messages.1312494 -->`
- 【Linux社区】1996年8月 Ollivier Robert(ollivier.robert@eurocontrol.fr) 在“List of OpenBSD changes”串中 转发Theo de Raadt列出的OpenBSD吸收FreeBSD成果清单，“The FreeBSD ports subsystem was integrated and is usable by you!”是 BSD分支间(FreeBSD到OpenBSD)技术双向流动的例证 `<!-- ROW_MINE: freebsd-hackers.messages.2571834 -->`

## 215.3 【Linux社区】BSD 治理智慧与 Linux 移植争议（5 条）

- 【Linux社区】2014年4月 Tyler Littlefield(tyler@tysdomain.com) 在“Leaving the Desktop Market”串中 反驳Eitan Adler放弃桌面市场提案，“anything that lets me rely less and less on GNU and the GPL is a bonus”是 BSD桌面战略中对GNU/GPL依赖的回避表态 `<!-- ROW_MINE: freebsd-hackers.messages.1316818 -->`
- 【Linux社区】1995年 Jordan K. Hubbard（jkh@violet.berkeley.edu）在 freebsd-hackers 的“ISPs and other commercial interests”串中提出由 ISP 联合开发驱动并以不受限版权授权的思路，属 FreeBSD 对 GPL 替代激励路径的早期探索；原始邮件不在本库，所涉原文引句已删除，待日后取得 freebsd-hackers 原帖后再行补证。`<!-- ROW_MINE: freebsd-hackers.messages.2551533 -->`
- 【Linux社区】1997年 Terry Lambert(tlambert@primenet.com) 在“Re: SUID-Directories patch”串中 对比GPL与BSD激励商业捐赠的差异，“Linux has the GPL to encourage commercial vendors to donate back; FreeBSD has a lot of hackers pushing fast enough”是 BSD与GPL治理激励模型的直接对照 `<!-- ROW_MINE: freebsd-hackers.messages.2597241 -->`
- 【Linux社区】2001年 Rich Morin (rdm@cfcl.com) 在“Re: so where is our press-release about MacOS X ?”串中回顾 Apple 的抉择“they created and distributed MkLinux, a Mach-based version of Linux”最终“chose BSD”，是 BSD 凭借许可证优势击败 Linux 阵营的历史关键时刻 `<!-- ROW_MINE: freebsd-hackers.messages.2639800 -->`
- 【Linux社区】2001年 MurrayTaylor(taylorm@bytecraftsystems.com) 在“Re: FYI”串中 追问厂商驱动能否以非 GPL 非 NDA 形式进入 FreeBSD，“Is there any way to get some of this - NOT under GPL and NOT under NDA?”，是 BSD 社区以许可证为筛选门槛讨论 Linux 驱动治理的历史节点 `<!-- ROW_MINE: freebsd-hackers.messages.2647023 -->`

## 215.4 【Linux社区】BSD 人物在 freebsd-hackers 的出场（1 条）

- 【Linux社区】1996年 John S. Dyson(toor@dyson.iquest.net) 在“Re: TCP/IP bandwidth bragging”串中 自陈保留源代码的自由立场，“These are my kind-of part of my anti-GPL sentiments”是 BSD早期核心人物反GPL立场的直接自白 `<!-- ROW_MINE: freebsd-hackers.messages.2578033 -->`

## 215.5 【Linux社区】附录：筛查与去重情况

- **来源**：freebsd-hackers（201,463 封）
- **BSD 价值打分**：147,686 条命中
- **GPL+BSD 许可双命中 OR BSD 变体/技术命中**：1,347 封
- **score≥30**：191 封
- **subject 去重后**：66 封
- **outline_worthy**：48 条（strong 27 + moderate 21）
- **precision**：48/66 = 72.7%

### 215.5.1 年份分布（48 条入纲）

- None: 48

### 215.5.2 判定分布

- strong: 27
- moderate: 21

### 215.5.3 精度对比

| 分层 | precision | 样本 → 入纲 |
|---|---|---|
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

### 215.5.4 已知盲区

- freebsd-hackers 中 BSD 技术移植讨论（LinuxKPI、agp(4)、video4bsd）未全部覆盖
- freebsd-current（205,027 封）与 openbsd_mail（154,119 封）已在 211 章覆盖
- netdev（1,254,852 封）BSD 反向输出待执行
- linux-fsdevel（360,374 封）BSD 文件系统张力待执行
- dragonflybsd 列表未检查
