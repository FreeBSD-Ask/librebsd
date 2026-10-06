---
chapter: 第 8 章
id: CH8
volume: 第01卷-unix的起源
---

# 第 8 章 贝尔实验室的黄金时代

## 要点

- V6 是首个广泛流通的研究版本，通过学术许可证进入大学；John Lions 于 1976 年 5 月完成 V6 源代码注释本的讲义形式（新南威尔士大学课程 6.602B 与 6.657G 教材），1977 年 3 月 UNIX News 宣布注释本对 UNIX 许可证持有者可用，版权页标“Copyright 1977 J. Lions”[考据脚注]；注释本成为 UNIX 教学的奠基性文献；注释本
- V6/V7 PDP-11 版本采用 swapping 而非 demand paging；32V (1978) 移植至 VAX-11/780 后仍未利用 VAX 虚拟内存硬件；3BSD (1979 年底) 才首次实现 demand paging，落后 TENEX 约 10 年 [考据脚注]
- setuid/setgid 机制与 9 位 rwx 权限模型在 V6（1975 年）完整后，成为 BSD 软件包管理的核心安全机制。**pkg_add(8)**、**chown(8)** 等命令依赖 setuid 实现特权操作，**chmod(1)**、**chown(1)** 等命令依赖 rwx 模型进行权限管理。〔待核：原文截断，后文待回源〕
- V7 伴随 VAX-11/780 移植 32V，标志 UNIX 进入 32 位时代；32V 为后续 3BSD 与 4BSD 在 VAX 上的发展奠定基础；VAX 移植推动 UNIX 从 PDP-11 向更广泛硬件平台扩散
- V6/V7 内核模块边界的清晰化为 Berkeley 改造提供接口基础；setuid/setgid、文件锁、信号机制等 V6/V7 特性被 BSD 8.0 (1977) 与后续 BSD 版本继承与发展；V6/V7 至 BSD 的延续性是 UNIX 谱系的关键节点

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4159] 卷“第01卷-unix的起源”第 8 章，匹配置信度 8.0，原因：22 篇（bstj57-6-1897~2289），Ritchie&Thompson 序言至 UNIX 各子系统论文
- [DB:references_fulltext:chapter_matches:chmatch_1529] 卷“第01卷-unix的起源”第 8 章，匹配置信度 0.9，原因：关键词搜索下载文献，标题含章节主题

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- [考据脚注] 注释本时间线经 Lions 1977 注释本版权页与 UNIX News 1977 年 3 月通告两方独立来源交叉印证——注释本最初于 1976 年 5 月作为新南威尔士大学课程 6.602B/6.657G 讲义产生，1977 年 3 月 UNIX News 宣布对 UNIX 许可证持有者可用，版权页标“Copyright 1977 J. Lions”；早期表述“1977 年完成”丢
- [考据脚注] 3BSD demand paging 年份经 UCI 教材、CMU 论文、McKusick“A Berkeley Odyssey” (Unix Review 1985-01)、McKusick“A Berkeley Odyssey” (Unix Review 1985-01) 四方独立来源交叉印证——Bill Joy 与 Ozalp Babaoglu 1978 年开始 VAX UNI
- setuid 机制的“受控特权”理念是否为后世 capability 安全模型的史源存在学术讨论——Capsicum 论文（Watson et al. 2010）将 capability 定位为 setuid 的替代而非延续，但二者在“细粒度特权”理念上有承继关系；setuid 程序的安全风险是否在 V6 引入时已被预见需考据——Ritchie 1984 BLTJ 论文未明确提及安全风险，可能为后
- 32V 与 V7 的关系是并行还是派生存在叙事分歧；VAX 移植的技术难点需考据
- V6/V7 至 BSD 的具体改造接口需逐项考据；Berkeley 改造的工程边界需明确

## 文献

- Lions 1977“Lions' Commentary on UNIX 6th Edition”（版权页 Copyright 1977 J. Lions）；UNIX News 1977 年 3 月通告；Toomey 2009；Salus 1994 第 8 章 [考据脚注：Lions 1977 注释本最初为内部教程、非正式出版等核心事实经 Salus 1994 与 Toomey 2009 交叉验证确证。]---## 史料登记与辩证校准（2026-08-08 追加）> **本卷命题**：24.1 少数与多数（详见本卷 00-总览“编纂指导思想叙事参照”）### 史料文献
- Kashtan 1980 RSI report“UNIX and VMS: Some Performance Comparisons”；McKusick et al. 1996；3BSD Release Notes (1979)；McKusick“A Berkeley Odyssey” (Unix Review, January 1985)；UCI 教材对 3BSD 的记载；统计分析报告：文献计量学分析.md Task 22 [R/OL]. 2026-07-27. 文件路径：**03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/文献计量学分析.md**；SQL 查询：`SELECT id, gbt7714 FROM "references"`. 资料数据库.duckdb [DB/OL]. 查询日期：2026-07-27；Python 统计脚本：`script/phase6_bibliometrics.py`. Task 22 参考文献增长曲线与 Price 指数。执行日期：2026-07-27 [考据脚注：references 表 16,867 条、年份提取率 44.42%、1978 年 118 条、1979 年 58 条等统计结论经 `script/phase6_bibliometrics.py` 执行结果与 `phase6_results.json` 结构化结果交叉验证。]
- research-unix-security-1969-1979.md 研究底稿；4.4BSD SMM: 16《On the Security of UNIX》；Watson, Anderson, Laurie, Kennaway 2010“Capsicum: Practical Capabilities for UNIX” (USENIX Security 2010)；freebsd.duckdb：freebsd-src commit `5b81b6b301437eb9a6df491c829475bd29ae5d6c`（1993-06-12，Initial import 含 setuid 程序与 rwx 代码）；freebsd.duckdb：freebsd-src commit `26f9a76710a312a951848542b9ca1f44100450e2`（1994-05-25，4.4BSD-Lite import） ［A］
- Ritchie 1984 BLTJ BLTJ；Salus 1994；32V 源代码 (TUHS) ［A］
- McKusick et al. 1996 第 1 章；Lions 1977；BSD 8.0 源码 ［A］
- Organick 1972“The Multics System”；Pike 1983 USENIX“Cat -v Considered Harmful?”；Kernighan 2019 ［B］
- Kernighan & Plauger 1976“Software Tools”；Pike & Kernighan 1984“Program Design in the UNIX Environment” (BYTE) [考据脚注：Kernighan & Plauger 1976 与 Pike & Kernighan 1984 为 UNIX 编程环境经典文献，核心事实经计算机科学史公认。]
- Kernighan & Plauger 1976“Software Tools”；Gamma et al. 1994“Design Patterns”；Pike & Kernighan 1984 BYTE [考据脚注：Kernighan & Plauger 1976 与 Gamma et al. 1994 为软件设计经典文献，核心事实经计算机科学史公认。]
- Ritchie, 1978 BLTJ; TUHS 存档中的 V7 发布前邮件与备忘录； Salus, 1994 ［B］
- Salus 1994；Kernighan 2019；Toomey 2009；Spinellis 2006 [考据脚注：Salus 1994、Kernighan 2019、Toomey 2009、Spinellis 2006 为 UNIX 历史经典文献，核心事实经计算机科学史公认。]

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP487、BSD Now EP325、BSD Now EP173（共 3 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 主持人 Benedict Reuschling 独自主持本期（Tom 与 Alan 休假），回顾上周已发布的 EuroBSDCon 2022 采访并预告本期压轴的对长期 committer John Baldwin 的采访，称 Michael W Lucas 曾誉其为“the big committer”。（BSD Now EP487，[64.9-133.1]，L2）[订正：原 “OpenBSD 6.1 于 2017 年发布，是该项目第 42 个版本；该版本引入 Clang 作为基础编译器，动因是既有 GCC 的 GPLv2 版本无法支持 ARM64 平台。（BSD Now EP487，[72.92-129.86]，L2）”，2026-09-30 SenseAudio 重转核对]
- 主持人逐段解读 FreeBSD Foundation 网站上 Patrick McEvoy 的 EuroBSDCon 2022 维也纳会议 trip report 前半：7 月起向董事会询问场地详情并租赁设备，抵达当日即与租赁商核对装备清单，以 Blackmagic Windows 客户端与改写 XML 流媒体配置做前期调试，又制作含《蓝色多瑙河》改编的预流音乐视频，并依靠其多年自建的“streaming system in a backpack”装备集支撑各 dev room 流媒体。（BSD Now EP487，[178.0-324.5]，L2）[订正：原 “主持人逐段解读 Ritchie《The Evolution of the Unix Time-sharing System》，指出该论文回顾 UNIX 自 1969 年诞生、经 PDP-7 至 PDP-11 移植的早期史，依次讲述文件系统、进程控制、I/O 重定向与管道发明。（BSD Now EP487，[1048.88-1308.52]，L2）”，2026-09-30 SenseAudio 重转核对]
- 主持人解读 trip report 后半：FreeBSD 与 NetBSD 峰会日的流媒体被他当作主会前的演练并顺利完成；周五晚接连遭遇双重意外——流媒体团队另一成员临时取消行程、captive portal 同时覆盖 Wi-Fi 与以太网致原定方案作废——在妻子“这是社区，去求助”的点拨下转向 OBS 网络摄像头方案，Christophe（DCH）连夜提供备份 Windows 笔记本配合 Ventoy 盘重装 Windows 10 ISO，社区响应其所有求助，最终在十二小时内搭起三套以本地与 scaleengine.com 双路录制的流媒体系统，并于凌晨三点半就绪。（BSD Now EP487，[326.4-589.5]，L2）[订正：原 “Ping 程序由 Mike Muuss 于 1983 年在 4.2a BSD 上编写，直接动因是同年 7 月 Dave Mills 在 DARPA 会议上关于以定时 ICMP 回显请求测量路径延迟的评论；Muuss 为此补全了内核的 raw ICMP socket 支持。（BSD Now EP487，[4653.46-4790.7]，L2）”，2026-09-30 SenseAudio 重转核对]
- John Baldwin 自述近年工作：与 Netflix 合作将其为自身场景开发的内核 TLS（KTLS）框架修整后上游化并合入 FreeBSD 主线，同时推动 OpenSSL 补丁向上合并，并把此前仅支持软件加速的框架扩展到部分智能网卡上的 NIC TLS 卸载；此外多年来从事设备驱动与基础设施工作，改进 ACPI 与 PCI 支持及热插拔。（BSD Now EP487，[888.1-948.3]，L2）[订正：原 “FreeBSD 将 ZFS 压缩发送接收功能导入 vendor branch，该功能依赖此前的 compressed ARC，使 ZFS send 可跨网络直接传输压缩数据，避免先解压再压缩的低效路径。（BSD Now EP487，[3892.42-4264.2]，L2）”，2026-09-30 SenseAudio 重转核对]
- John Baldwin 回顾 Alpha 架构上的 SMP 工程：SMP 工作起步于源自 BSD/OS 的大型代码导入，其中相关代码当时几乎全为 i386 专属，Alpha 是第一个在其上 bring up SMP 的非 i386 架构——Doug Rabson 已完成早期工作，Baldwin 将 SMP 世界带入 ithread 等机制并让 Alpha 跑通 ithread 与 SMP；过程中他整理干净的抽象、为 IA-64 的内存屏障原子操作作规划，使大部分 mutex 代码改为机器无关，Alpha SMP 尤其倒逼 SMP 代码迁出 sys/i386 并清理多处硬编码。（BSD Now EP487，[1003.7-1131.3]，L2）[订正：原 “FreeBSD MAC 强制访问控制框架源自 DARPA 资助的 TrustedBSD 项目，允许以细粒度策略替代传统 root 特权；以 portacl 为例，可让非 root 用户绑定 1024 以下的特权端口。（BSD Now EP487，[4264.2-4648.22]，L2）”，2026-09-30 SenseAudio 重转核对]
- FreeBSD 12.1 是首个以 open ZFS 端口支撑原生 ZFS 加密所需密码学原语的版本，同时导入 BearSSL 为 Juniper 的验证引导装载器提供轻量 TLS，并纳入 MLX5 固件更新工具与 FUSE 驱动重写。（BSD Now EP325，[63.84-68.92]，L2）
- 12.1 预告 i386 默认 CPU 类型将由 486 升至 686（自 13 起），因 486 缺 64 位原子操作且用户态无法模拟；CTM 与 timed 等工具被标记废弃。（BSD Now EP325，[543.78-594.94]，L2）
- 重刊的《Unix Evolution 1975–1984》一文梳理 research Unix v6/v7/v8 的文本格式化、编译器与开发工具流变，并记述 Ritchie 关于 man page BUGS 节以公开羞辱促修复的自述。（BSD Now EP325，[723.74-1018.28]，L2）
- OpenBSD 在 base unbound 默认启用 DNSSEC 验证，并以 Quad9 的 9.9.9.9 做约束验证绕开 NTP 与 DNSSEC 的时钟引导死锁；2018 年曾因时钟问题回滚后于此次重开。（BSD Now EP325，[2062.14-2169.84]，L2）
- Rainbow Crack 的 OpenBSD 编译补丁引出彩虹表原理：加盐与多轮散列（bcrypt 可至百万轮、SHA-512 crypt 默认万轮）使针对字典的预计算表失效，凸显密码存储需抗彩虹表算法。（BSD Now EP325，[2632.88-2909.48]，L2）
- Johannes Lundberg 向 FreeBSD 邮件列表提交 Wayland 移植进度报告：Wayland 1.12.0 与 Weston 1.12.0 已可在 FreeBSD 上运行，Weston 自带客户端工作正常，xWayland 可承载未移植的 X11 应用（仅手动启动且最大化窗口时正常，疑为 Weston IPC 问题），GTK3 应用如 gedit、Gnumeric 与 XFCE4 终端均可运行，XFCE 桌面则不支持 GTK3，SDL2 的 Wayland 后端经游戏简测通过，i3 兼容合成器 Sway 亦可用；现代 Intel 显卡需 Matt Macy 的新图形驱动工作，并以自维护 ports 树配合 Poudriere 重建图形栈乃至全树；gdm 因依赖 Linux 的 logind 而搁置，社区有意改以 Qt 系的 PCDM 承接。（BSD Now EP173，[279.52-419.90]，L2）[订正：原 Wayland 8.12.0 与 Weston 8.12.0、原 XFCE 桌面均可运行、原 [279.52-327.5]，2026-09-30 SenseAudio 重转核对]
- Antoine Jacoutot 向 OpenBSD 邮件列表公告 syspatch：面向 -stable 发行版的二进制补丁工具，与 bspatch 式二进制差分不同，它下载经签名的完整文件 tarball 并按安装器方式替换；测试补丁未经 OpenBSD 项目背书且不应信任，反馈须直达其个人邮箱而非污染邮件列表；此前升级 -stable 只能源码重建或重装新快照，syspatch 提供了中间道路，作者期望其随 OpenBSD 6.1 落地，并明确需要使用人数与统计反馈来评估可靠性。（BSD Now EP173，[105.04-229.3]，L2）[订正：原 [105.04-203.7]，2026-09-30 SenseAudio 重转核对]
- Dennis Ritchie 撰文追述 Unix 源码中的趣味史：V6 彩蛋“values of B may give rise to DOM”出自 1970 年代初专利打字员打断 ed 打印输出时纸带上的残句，原是物理专利申请中‘贝塔值变化引起畴壁移动’的片段，经 McIlroy 的文语转换实验念出 doom 与 dominance 的谐音而成为实验室的共享珍宝，后被写入 V6 源码——里奇推测大概率出自 Bob Morris，也可能是 Ken；他并澄清“你不会被期望理解这段注释”本意是‘这不会考’式的善意提示而非傲慢挑衅，将其引为贝尔实验室注释质量的 slur 属不公正引申，见过原文者多为 1975 年前后第六版用户或 John Lions 注释书的读者。（BSD Now EP173，[2332.96-2512.8]，L1）
- Beastie bits 一束：iocell 2.0 发布——一位 FreeBSD 开发者因偏爱 shell 脚本版而分叉原 iocage 并继续演进，Python 重写版则临近发布，两者存储监牢配置的方式相近或可兼容；Ted Unangst 追问 link_ntoa() 究竟谁在调用——该函数缺陷自 1970 年代引入并波及所有 BSD，OpenBSD libc 中已标记弃用，全库检索仅 route 与 netstat 三处引用，或可直接移除；Trent 用其 bhyve 管理框架 iohyve 在 ThinkPad 上的 TrueOS 中启动 Android x86 并公开配置 gist。（BSD Now EP173，[2795.08-3015.90]，L2）[订正：原 [2795.08-2949.74]，2026-09-30 SenseAudio 重转核对]

**史料**：

- Patrick McEvoy 的 EuroBSDCon 2022 维也纳会议 trip report（载于 FreeBSD Foundation 网站），主持人逐段宣读其峰会日与主会前准备部分。（BSD Now EP487，[192.4-605.8]，L2）[订正：原 “Ritchie, D. M.《The Evolution of the Unix Time-sharing System》论文原文，主持人在节目中引述其结构与结论。（BSD Now EP487，[1048.88-1308.52]，L2）”，2026-09-30 SenseAudio 重转核对]
- John Baldwin 受访自述其 BSD 履历：高中时与朋友打算为 386 写自己的操作系统与编译器，大学因本校以 FreeBSD 作为本科生的 Unix 而转向正经使用 FreeBSD（pf 路由器、用户态 PPP、坚持在 FreeBSD 上完成 Java 作业），毕业前经写文档“后门”进入社区并于 1999 年 8 月获 commit bit，随 Mike Smith 在引导装载器写汇编，其后受雇于 Walnut Creek CDROM。（BSD Now EP487，[647.6-878.7]，L2）[订正：原 “Mike Muuss 个人主页自述：Ping 是他在一个晚上写出的约一千行 hack，命名取自声呐回波定位原理；该主页还记载 Dave Mills 1983 年 7 月 DARPA 会议评论的缘起。（BSD Now EP487，[4653.46-4790.7]，L2）”，2026-09-30 SenseAudio 重转核对]
- 本期开头宣读的赞助信息：Tarsnap 在线备份（tarsnap.com/bsdnow）与节目 Patreon 页面（patreon.com/bsdnow），为节目官方资助线索。（BSD Now EP487，[36.7-64.6]，L2）[订正：原 “OpenBSD 6.1 发布新闻与 Release Notes，涉及第 42 个版本、Clang 基础编译器引入与 ARM64 平台支持。（BSD Now EP487，[72.92-129.86]，L2）”，2026-09-30 SenseAudio 重转核对]
- FreeBSD 12.1 发布公告与 releng 说明，列明 open ZFS、BearSSL、MLX5、FUSE 重写及废弃项。（BSD Now EP325，[128.32-148.56]，L2）
- Microsystems Magazine 1984 年 11 月号《Unix Evolution》文章（Daemon News 1999 重刊），为节目重读的历史文本。（BSD Now EP325，[740.14-756.02]，L2）
- Dennis Ritchie 关于 man page BUGS 节政策的引文，属当事人一手表述。（BSD Now EP325，[1012.82-1027.82]，L1）
- OpenBSD unbound.conf 默认 DNSSEC 与 aggressive NSEC 的提交说明，及与 Quad9 的约束验证讨论。（BSD Now EP325，[2077.00-2124.28]，L2）
- 本期涉及的一手史料包括：Doug McIlroy 邮件列表文章（Unix 如何走出实验室直达 AT&T 高层的亲历记）、Dennis Ritchie 的 Unix 彩蛋史话与 John Lions 的 UNIX 第六版注释书、Johannes Lundberg 的 Wayland 进度报告、Antoine Jacoutot 的 syspatch 公告信、Ed Maste 的可复现构建报告及 Phabricator 评审、Mark Felder 的 FreeBSD 加 ZFS 仿 Time Capsule 教程（NetATalk 3 与 Avahi）、Olivier Cochard-Labbe 的 NetBenches 网络基准仓库（含 FreeBSD IPsec 性能分支的 AES-NI 实测数据）、Brian 的 OpenBSD/Arch 双系统博客、Ted Unangst 关于 link_ntoa() 的调用面分析、Trent 的 iohyve 配置 gist，以及 BSDCan 2017 征文启事。（BSD Now EP173，[2191.18-2200.26]，L2）

**史观**：

- 总纲23 一切历史写作都是基于哲学设定的历史小说：John Baldwin 自述高中时把“内核黑客”设定为软件能力的巅峰、最难之事，甚至立志“爬过碎玻璃”也要做到，如今则认为内核“不过是一个大 C 程序”、其实并不太难——同一段职业史在当事人不同人生阶段的设定下被写成不同的故事。（BSD Now EP487，[1691.0-1764.2]，L2）[订正：原 “总纲23 一切历史写作都是基于哲学设定的历史小说：主持人引述 Ritchie 论文结论，指出早期 UNIX 编程环境虽以今日标准显得严酷原始，但当事人当时并不觉得如此，记忆只留住美好与持存之物。（BSD Now EP487，[1261.84-1298.56]，L2）”，2026-09-30 SenseAudio 重转核对]
- 总纲5 没有必然性，只有偶然性：John Baldwin 本为编写新安装器与 IA-64 引导装载器而受雇于 Walnut Creek CDROM，到岗后却“阴差阳错”转向 SMP 工作并被继续留任——他自嘲“受雇要做的工作几乎没做”，其从 doc committer 到内核黑客的路径系于机缘而非计划。（BSD Now EP487，[846.0-878.7]，L2）[订正：原 “总纲5 没有必然性，只有偶然性：主持人指出论文显示 UNIX 早期已萌生虚拟化、容器与能力等思想，只因当时机器不够强大而无法实现，表明技术形态受物质条件制约而非线性进步。（BSD Now EP487，[1139.58-1162.48]，L2）”，2026-09-30 SenseAudio 重转核对]
- 总纲10 动手者创造历史：Patrick McEvoy 在流媒体团队临时取消、captive portal 覆盖全场的困境中，靠 OBS 网络摄像头方案、社区连夜提供的 Windows 笔记本与 Ventoy 盘重装，十二小时内亲手拼出三套流媒体系统，使 EuroBSDCon 2022 的报告得以录制直播——会议基础设施史由动手者在具体困境中造就。（BSD Now EP487，[425.2-589.5]，L2）[订正：原 “总纲10 动手者创造历史：Mike Muuss 自述 Ping 为一晚写成的千行 hack，并感慨若早知它会成为一生最著名的成就便会再多打磨，体现动手者在具体机缘中的创造。（BSD Now EP487，[4780.22-4790.7]，L2）”，2026-09-30 SenseAudio 重转核对]
- 总纲3 不存在进步，只有权力再分配：总纲3 不存在进步，只有权力再分配：i386 486→686、GCC 4.2 弃用、CTM 与 timed 废弃不是进步，而是支持资源在不同架构间的再分配。（BSD Now EP325，[567.10-625.50]，L2）
- 总纲8 本体论上各方平等：总纲8 本体论上各方平等：FreeBSD、OpenBSD、HardenedBSD、OPNsense 同屏报道，各分支地位平等，不以体量定优劣。（BSD Now EP325，[1698.58-1805.42]，L2）
- 总纲10 动手者创造历史：总纲10 动手者创造历史：Tom Jones 以 git worktree、tmux、cscope、bhyve 的动手流程呈现 FreeBSD 开发者的真实工作方式。（BSD Now EP325，[1317.46-1484.78]，L2）
- 总纲22 知识注定过时：总纲22 知识注定过时：1984 年文章自承需源许可并签血誓方可读源码，而 V7 源码迟至 2002 年由 Caldera 释放，知识条件随时间失效。（BSD Now EP325，[923.02-977.30]，L2）
- 总纲12 科学是形式主义：总纲12 科学是形式主义：密码学的“安全”依赖加盐与轮数的形式约定，彩虹表攻击揭示其相对性而非绝对真理。（BSD Now EP325，[2864.92-2909.48]，L2）
- 总纲5 没有必然性，只有偶然性：总纲5 没有必然性，只有偶然性：OpenBSD 2018 年曾默认开 DNSSEC 后回滚、2019 年再启用，取决于时钟引导问题被偶然解决。（BSD Now EP325，[2124.78-2143.00]，L2）
- 总纲5 没有必然性，只有偶然性：McIlroy 亲述的 Unix 采纳史拒绝任何必然性叙事：贝尔实验室法律部门成为第一个研究外用户，只因新购的独立文字处理系统应付不了美国专利局要求的行数，而 Joe Ossanna 承诺次日为 troff 加上行号；AT&T 总裁办公室购入 Unix，只因总裁不愿戴眼镜读讲稿、而实验室的照排中心能以大号字排版讲稿；他以‘正如人们因杯架买车’作结——Unix 的扩散系于行号与虚荣这类琐碎偶然条件，技术优劣的理性论证反倒是后来追加的解释。（BSD Now EP173，[2200.94-2310.2]，L1）
- 总纲17 证明世界先于解释和改造世界：Ed Maste 宣布 FreeBSD 基本系统可复现构建达到 100%，经 Phabricator 评审但暂需显式设置构建变量，因不少开发者珍视 uname -a 中的构建日期与 SVN 版本号；主持人追溯 2013 年前后 AsiaBSDCon 上的可复现构建演讲，期待发布版 ISO 能被第三方以相同旗标重建出逐比特一致的二进制——以可证明的一致性取代对发行者的信任承诺，是工程文化从解释走向证明的一个节点。（BSD Now EP173，[2589.52-2698.72]，L2）

**辨析**：

- 新转写时间戳有序，但仍存在较多专名识别错误，如 BSD Now 被识别为“BST Now”、ddb 被识别为“GDB”、bhyve 被识别为“Beihai”或“beehive”、FreeBSD 被识别为“Freiburg's”或“FreePBX”、Walnut Creek CDROM 被识别为“Walnut Creek City ROM”、SMP 被识别为“S and P”或“SMP E G”（应为 SMP/SMPNG）、FDT 被识别为“FTT”、EuroBSDCon 被识别为“Euro BST Con”“Eurpeasticon”或“EuroVSEC Con”，引用时须回查原音频或官方文本。　[存疑脚注] 转写专名需人工复核（BSD Now EP487，[36.7-2044.0]，L4）[订正：原 “本册转写时间戳乱序，且存在多处专名识别错误，如 FreeNAS 被识别为 Freenaz、illumos 被识别为 Alumos 或 Olimo，引用时须回查原音频或官方文本。　[存疑脚注] 转写质量存疑，专名与时间戳需人工复核（BSD Now EP487，[3299.74-3425.06]，L4）”，2026-09-30 SenseAudio 重转核对]
- 主持人只宣读 trip report 至 FreeBSD/NetBSD 峰会日与周五晚双重意外为止，对主会三天流媒体最终是否顺利未加转述，仅以“留待读者自读”收束；引用 EuroBSDCon 2022 主会流媒体成败的结论时不能以本期为据。　[存疑脚注] 主会流媒体结果不在本期宣读范围内（BSD Now EP487，[590.7-605.8]，L4）[订正：原 “OpenBSD 6.1 以 Clang 取代 GCC 的动因被表述为 GCC 的 GPLv2 版本无法支持 ARM64，此说来自主持人转述，须以 OpenBSD 官方公告或开发者邮件交叉验证。　[存疑脚注] 单一播客来源，需 OpenBSD 官方公告交叉验证（BSD Now EP487，[104.7-129.86]，L4）”，2026-09-30 SenseAudio 重转核对]
- Rainbow Crack 网站自 2007 年后基本未更新，教程提及的某域名已被劫持为垃圾页，该工具的可用性与教程安全性存疑。　[考据脚注] 站点域名易主，链接与补丁来源需重新核实（BSD Now EP325，[2683.40-2706.96]，L4）
- 12.1 的 open ZFS 与原生加密支持为发布说明转述，具体实现路径与加密原语宜以 FreeBSD 源码树核对。　[存疑脚注] 转写对“首个支持 open ZFS 端口的正式版”表述较口语化（BSD Now EP325，[68.92-90.80]，L4）
- OpenBSD 与 Arch Linux 双系统互毁 GPT 备份头的辨析：读者在 gdisk 中连报磁盘尺寸与主头不符、备份头无效、主备分区表不一致、CRC 失配四重警告，先按提示以主表重建备份表仍反复复现，最终以 MBR 加 LUKS 与 LVM 的非常规组合绕过；主持人推断两系统对该盘一个按 4K 扇区、一个按 512 字节扇区定位盘尾备份头，导致互相覆盖后无法互认，并可能只是特定硬盘的 quirk；主持人借此事强调详细记录、多次复现并投递邮件列表的边界用例报告文化。　[存疑脚注] 4K 与 512 字节扇区判定差异仅系主持人远程假设，最终根因取决于读者后续向 tech 邮件列表的报告，转写中未见定论。（BSD Now EP173，[679.70-901.68]，L4）[订正：原 [811.82-901.68]，2026-09-30 SenseAudio 重转核对]

**文献**：

- [BSD Now EP487] Pennington J. BSD Now: 487: EuroBSDcon Interviews Pt. 2[EB/OL]. (2022-12-29)[2026-08-15]. <https://www.bsdnow.tv/487>.
- [BSD Now EP325] Pennington J. BSD Now: 325: Cracking Rainbows[EB/OL]. (2019-11-21)[2026-08-15]. <https://www.bsdnow.tv/325>.
- [BSD Now EP173] Pennington J. BSD Now: 173: Carry on my Wayland son[EB/OL]. (2016-12-21)[2026-08-15]. <https://www.bsdnow.tv/173>.

<!-- /PODCAST_REVIEW -->

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

