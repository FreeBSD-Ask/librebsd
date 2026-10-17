---
chapter: 第 139 章
id: CH139
volume: 第07卷-freebsd的工程体系重构
---

# 第 139 章 FreeBSD 网络栈的 TCP/IP 谱系与 KAME IPv6

## 要点

- BSD TCP/IP 实现的一手史料包括 CSRG 发布的 4.2BSD（1983）、4.3BSD（1986）、4.4BSD-Lite（1994）磁带和源码光盘（部分可在 TUHS 档案馆获取）；FreeBSD 源码仓库（cgit.freebsd.org）完整记录了从 1994 年至今的每一次网络栈代码变更，是研究网络栈演进的一手史料；二手史料中 McKusick 等人的两版 *The Design and Implementation* 系权威参考，但需注意第一版（1996）描述 4.4BSD，第二版（2014）描述 FreeBSD 8/9 时代架构。
- netgraph 早期设计史料包括 Julian Elischer 和 Archie Cobbs 在 freebsd-current 和 freebsd-net 邮件列表上的设计讨论（1997-1999 年）、初始 commit 日志、两人在 BSDCon 1999/2000 的演讲；netgraph 最初设计目的之一是替代当时繁琐的 PPP 和拨号网络配置，为 Whistle InterJet 路由器产品提供灵活的协议扩展框架，而非通用可编程数据面——ISP 和防火墙用户后来发现了 netgraph 更多用途。
- if_bridge 从 NetBSD 移植的精确时间——FreeBSD 5.2（2004 年 1 月）是首个包含 if_bridge 的版本，但代码导入时间约为 2003 年下半年；if_lagg 初始开发者——Mykola Dzham 完成了初始实现，Andrew Thompson 做了大量代码审查和 LACP 完善；早期 FreeBSD 网桥历史的一手资料较为分散——FreeBSD 2.x-4.x 时代没有原生网桥，用户使用 Luigi Rizzo 的 dummynet 网桥或用户态解决方案。
- VNET 开发的一手史料包括 TrustedBSD 项目的技术报告（2006-2009）、罗伯特·N. M. 沃森 和 Bjoern Zeeb 在 freebsd-jail 和 freebsd-net 邮件列表的设计讨论、FreeBSD 源码仓库 sys/net/vnet.c 的提交历史；VNET 从实验性到稳定经历了约 7 年（2009-2016），核心挑战包括：① 将内核中数百个全局网络变量标记为 VNET_PUBLIC 或 VNET_PRIVATE。

## 史料

- [DB:bsdnow_podcast:outline_mappings:om_11515] BSD Now 第 528 期，匹配 CH139 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_12363] BSD Now 第 435 期，匹配 CH139 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_12614] BSD Now 第 404 期，匹配 CH139 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_12635] BSD Now 第 401 期，匹配 CH139 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_10424] BSD Now 第 676 期，匹配 CH139 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10441] BSD Now 第 674 期，匹配 CH139 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10631] BSD Now 第 638 期，匹配 CH139 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10690] BSD Now 第 630 期，匹配 CH139 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10729] BSD Now 第 624 期，匹配 CH139 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10763] BSD Now 第 618 期，匹配 CH139 章，关联度 1.0
- [DB:historical_claims:claim] 关键词行级挖掘素材线索 139.5-关键词行级挖掘素材线索（1 条，CL-RM 段，见 139.5-关键词行级挖掘素材线索.md）

## 史观

- 总纲 8“本体论上各方平等”——KAME 作为 IPv6 参考实现被各 BSD 各自演化吸收，多实现并行演化、提供选择并保障互操作性，在本体论层面平等看待各 BSD 分支的独立道路（详见概述与子节史观字段及本章采访史料）。
- 总纲 10“动手者创造历史”——从 netgraph 的 Elischer 与 Cobbs 到 VNET 的 Watson 与 Zeeb，网络栈各子系统均由一线实现者以代码直接推进；一线实现者将一手工程经验整理为教材与文档，属技术共同体的知识再生产。
- 总纲 13“法律与道德是利益分配”——IPv6 当事人口述中，版权与专利制度被指已从促进创造的初衷扭转为利益分配工具（itojun 以迪士尼版权延期为例的批评）。
- 总纲 4“分离聚合是永恒规律”——网络栈谱系自身即分合循环的具现：if_bridge 系 FreeBSD 5.2 自 NetBSD 移植回流，KAME 代码汇入各 BSD 后各自演化、偶尔回流对齐。

## 辨析

- 需纠正几个常见史实错误：① “FreeBSD 网络栈来自 386BSD”——386BSD 0.1（1992）确实包含网络栈，但 FreeBSD 在 1994 年 2.0 版本就完整迁移到了 4.4BSD-Lite 代码基，此后网络栈直接演进自 CSRG 代码而非 Jolitz 的 386BSD 代码；② “**sendfile(2)** 是 Linux 发明”——错误，**sendfile(2)** 由 David Greenman 于 FreeBSD 2.2（1997 年）首创，Linux 在 2.2 内核（1999 年）才引入类似系统调用。
- netgraph 引入版本先前多处误写为 FreeBSD 3.0（1998-10），经 FreeBSD 3.4 Release Notes 一手核验，正确版本为 FreeBSD 3.4（1999-12）；先前误将 Archie Cobbs 记为唯一设计者，实际是 Julian Elischer 与 Archie Cobbs 两人共同设计，Elischer 是长期主要维护者；Cobbs 在 2000 年代初减少 netgraph 活跃维护后，netgraph 由 Julian Elischer、Ruslan Ermilov、Gleb Smirnoff 等人持续维护。
- FreeBSD 网桥历史常被简化为“if_bridge 一直存在”——实际上在 5.2 之前 FreeBSD 缺少原生内核网桥，这是一个重要的史实修正；**brconfig(8)** 命令在 FreeBSD 8 之后被 ifconfig bridge 取代，成为历史遗留命令；部分文档提到的“if_trunk”是 OpenBSD 的链路聚合接口名，不是 FreeBSD 的
- VIMAGE 选项改名——VNET 框架在内核配置中最初名为 options VIMAGE，后来虽框架改名 VNET 但内核选项名保留为 VIMAGE 以避免破坏现有配置，这是一个“历史遗留命名”的小案例；Bjoern Zeeb 在 VNET 开发中的角色常被低估——Watson 是项目领导者，但 Zeeb 完成了大量实际代码实现和 vnet 化改造工作；VNET 第一个正式生产就绪声明是在 FreeBSD 11.0 Release Notes 中。

## 文献

- The Unix Heritage Society. *BSD Source Archives*. tuhs.org; FreeBSD Project. *Source Repository*. cgit.freebsd.org; Greenman, D. (1997). *sendfile(2) System Call Commit*. svn.freebsd.org revision history; Salus, P. H. (1994). *A Quarter Century of UNIX*. Addison-Wesley. ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2020-2024 年间：291,070 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- FreeBSD Net Mailing List Archives. (1997-1999). *Netgraph Design Threads*. freebsd.org; Elischer, J., & Cobbs, A. L. (1999). *Netgraph: A Network Graphing Subsystem for FreeBSD*. BSDCon '99 Proceedings; FreeBSD Project. *sys/netgraph/ Source Code History*. cgit.freebsd.org. ［D］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1999-1999 年间：23,839 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- FreeBSD Project. *sys/net/if_bridge.c, sys/net/if_lagg.c Commit History*. cgit.freebsd.org; Thompson, A. (2007). *if_lagg Link Aggregation Driver Commit*. svn.freebsd.org; FreeBSD Net Mailing List. (2003-2008). *Bridge and LAGG Discussions*. freebsd.org. ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2020-2024 年间：291,070 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- Watson, R. N. M., & Zeeb, B. (2006-2016). *VNET Commit History*. svn.freebsd.org/cgit.freebsd.org; TrustedBSD Project. (2009). *VNET Technical Report*. trustedbsd.org; FreeBSD 相关记录（详情见存疑库）。文献 (UNIX 传奇：历史与回忆 ([美]布莱恩·W.克尼汉（BrianW.Kernighan）) (年份不详) 提及 McKusick, Marshall Kirk，作为 BSD 的核心人物，其撰写的 BSD 历史与 Unix 传奇是该领域的重要参考文献。**新增技术**文献 (06771908, 年份不详) 讨论 swap，该论文讨论了 Unix 早期进程间通过显式交换（swap）传递数据的机制，为理解 BSD 内存管理演进提供了历史背景。文献 (06771908, 年份不详) 讨论 UFS，该论文追溯了 PDP-7 Unix 文件系统的结构，为理解 BSD UFS 文件系统的设计起源提供了历史视角。文献 (UNIX 传奇：历史与回忆 ([美]布莱恩·W.克尼汉（BrianW.Kernighan）) (年份不详) 讨论 TCP/IP，Bill Joy 为 Unix 添加了 vi 编辑器和 csh，并引入了改变世界的 TCP/IP 协议 socket 接口，这些贡献是 BSD 对互联网基础设施的奠基性工作。文献 (UNIX 传奇：历史与回忆 ([美]布莱恩·W.克尼汉（BrianW.Kernighan）) (年份不详) 讨论 macOS，Unix 核心命令在 Linux、macOS 和 Windows Subsystem for Linux 中仍然广泛使用，体现了 BSD/Unix 技术的跨平台生命力。文献 (eurobsdcon2015-portroach, 年份不详) 讨论 OpenBSD，Jasper Lievisse Adriaanse 开发的 Portroach 是 OpenBSD 的 distfile 扫描工具，用于监控上游软件版本更新。文献 (eurobsdcon2015-portroach, 年份不详) 讨论 Ports Collection，Portroach 工具的设计灵感来自 FreeBSD 的 portscout，用于追踪 Ports Collection 中软件包的上游版本变化。**新增时间线事件**文献 (06771908, 年份不详) 记录 1980：Springer-Verlag 于 1980 年出版了关于设计与编程方法论的著作，为 Unix 系统设计提供了理论基础。文献 (06771908, 年份不详) 记录 1980：该文献引用了 1980 年关于 Unix 系统演进的学术出版物。文献 (UNIX 传奇：历史与回忆 ([美]布莱恩·W.克尼汉（BrianW.Kernighan）) (年份不详) 记录 1980：Bjarne Stroustrup 于 1980 年将 Simula 的面向对象特性与 C 语言融合，诞生了“带类的 C 语言”，即 C++ 的前身。文献 (UNIX 传奇：历史与回忆 ([美]布莱恩·W.克尼汉（BrianW.Kernighan）) (年份不详) 记录 1980：贝尔实验室 1127 中心于 1980 年开设了为期 3 周的集成电路设计速成课程，由加州理工学院的 Carver Mead 授课。文献 (eurobsdcon2015-portroach, 年份不详) 记录 2006：Jasper Lievisse Adriaanse 自 2006 年起成为 OpenBSD 开发者，专注于 GNOME 移植和 Puppet 配置管理。文献 (eurobsdcon2015-portroach, 年份不详) 记录 2012：FreeBSD 的 portscout 工具于 2012 年引起 OpenBSD 开发者的关注，启发了 Portroach 的开发。
<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2020-2024 年间：291,070 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSDTalk EP112、BSDTalk EP115（共 2 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Jinmei Tatuya 自述其 KAME 项目共同开发者身份：项目 1998 年启动、2006 年 3 月结束；虽已不再活跃开发，其代码已成为各 BSD 变体的固有组成部分。KAME 定位为 IPv6 参考实现，以开源形态拥有庞大且能干的开发者群体，这正是 Wind River 为 VxWorks 6.0 选定 KAME 作为核心 IPv6 代码的依据。（BSDTalk EP112，[56.92-70.64, 114.76-123.0, 391.28-417.88]，L1）
- Qing Li 完整叙述了书籍工程的起源与经过：2000 年初其在 Wind River Systems 完成 KAME 向 VxWorks 的移植（后发布于 VxWorks 6.0），积累了关于 KAME 实现、数据结构、图示与函数关系的海量笔记，遂决意为 KAME 写一部 Stevens《TCP/IP Illustrated》第二卷式的书，动机兼有自用与自我保存笔记之意；经 itojun 引荐 Jinmei、再由 Jinmei 引荐 Keiichi Shima 组成三人作者团队。项目原计划九个月，因覆盖范围不断扩展，最终耗时近三年半，单卷计划扩为两卷：《IPv6 Core Protocols Implementation》于 2006 年 10 月出版，《IPv6 Advanced Protocols Implementation》于 2007 年 4 月出版，均由 Morgan Kaufmann 发行，英文版之外日文版已在制作中。 [存疑脚注] 转写将引荐人记作“Yuto Jin”，按语境应为 itojun（Jun-ichiro Itoh Hagino）；“two bees at the time”疑为其时任职公司的误转（BSDTalk EP112，[127.66-199.16, 168.04-199.16, 254.86-283.98]，L1）
- 关于书籍定位，两位作者说明其差异化设计：全书面向开发者、以逐行代码注释为主体，每章固定三节——RFC 与规范摘要、带注释与图解的实现剖析（体例类比 Stevens 著作）、KAME 工具用法；成书前的市场调研发现市面已有四五种 IPv6 书均偏规范描述、仅一本偏运维，故有意放弃运维与网络管理员市场而专注开发者；卷二涵盖 DHCPv6（用户态实现并已移植 Linux）、DNS 与移动 IPv6 等 OS 无关内容，对 Linux 侧 USAGI 项目的开发者亦有价值，卷一则更专于 FreeBSD/KAME 实现。（BSDTalk EP112，[199.16-273.74, 707.08-767.72, 785.1-811.06, 925.82-991.54]，L1）
- itojun 自述其个人史：小学时代（1980 年前后）即接触计算机，Unix 类系统之路经日本本土的 MS-DOS 系实现、CP/M、Minix 而至 4.2BSD 系（约 1988 年）；自认当时已成为日本知名的黑客与程序员。其公共身份包括：IETF 活跃成员、2003 至 2005 年任 IAB 成员——自述为继村井純（Jun Murai，1992 至 1994 在任，被称互联网武士）之后第二位亚洲 IAB 成员；受访时 36 岁。其自述现负责包括 Apple Mac OS X 与 Juniper JunOS 等商业实现在内的所有 BSD 变体的 IPv6 代码，并称这实现了他本人的梦想。 [存疑脚注] 音频为免提电话转录，转写质量低：其 BSD 初遇平台转写作“from Tony and called MuseOS”，疑为 Sony News-OS 类 4.2BSD 衍生系统的误转，待核（BSDTalk EP115，[55.68-117.4, 165.02-180.94]，L1）
- itojun 对 IPv6 必要性的论证自成体系：IPv4 理论上限为 2 的 32 次方约四十亿地址，但因分配效率低下实际可用仅约一亿至四亿；人类人口已逾六十亿，且发达国家人均持有十台以上联网设备（手机、黑莓、带 GPS 导航并可下载地图的新车）；若要给包括中国、印度在内的所有人平等接入机会，至少需要六百亿地址，IPv6 是唯一可行方案。其预测 IPv4 将于 2009 或 2010 年终结；并自 1992 年 INET 神户会议起即投入 IPv6 工程，当年已察觉协议服务化的问题并开始动手。 [存疑脚注] 其预测依据转写作“Epinix guide”，所指预测来源无法从转写确认（BSDTalk EP115，[352.98-426.54, 436.86-463.58]，L1）
- itojun 特别澄清 2007 年 4 月 20 日的一起安全事件：法国研究者在加拿大 CanSecWest 安全会议披露的缺陷存在于 IPv6 规范而非任何实现，被他称为整个互联网历史上最大的规范级缺陷——攻击者可借此令路由服务器完全瘫痪（届时须手工逐一录入全部 IPv4 与 IPv6 地址），并以简单的命令行工具击落传输链路。其对用户的忠告具有强制意味：无论使用何种系统，向所有厂商索要补丁并逐台部署，若厂商拒绝修补即更换厂商。 [存疑脚注] 该缺陷即 2007 年披露的 IPv6 路由头类问题之说系按事件特征推断，转写中的会议名（CanSecWest）、日期与所指网站均以原貌存疑；其建议针对的具体协议细节无法从转写确认（BSDTalk EP115，[528.74-618.58]，L1）

**史料**：

- 该期保存多条一手史料线索：Apple 高级工程师读者为两卷书撰写书评，称将书与源码对照后发现两个参考实现的不同修订间高度相似，佐证 darwin 对 KAME 代码的继承；Qing Li 自 2000 年起多次将 KAME 移植至多种平台、最后一次为 VxWorks，现于 Blue Coat Systems 从事 IPv6 代理工作；Jinmei 在 Toshiba 任职十二年，以个人 IPv6 原型实现起步，经 WIDE 项目（日本多所大学与 IT 企业组成的大型研究组织）进入 IPv6 开发圈；两位作者在 BSDCan 2007 现场受访， Qing Li 评价其共同作者是“最优秀的 IPv6 程序员”，并忆及二人近乎全天候的写作投入。 [存疑脚注] 转写将公司名记作“Tosiva”“BlueCo Systems”，按史实应为 Toshiba 与 Blue Coat Systems；人名“Jin Mei Tatsuya”应为 Jinmei Tatuya（神明達哉），“Jimmy/Jimi Song”疑为对 Jinmei 的称呼误转，均以存疑待核（BSDTalk EP112，[649.44-682.44, 93.76-118.56, 283.98-348.5, 1112.26-1144.02]，L1）
- 该期保存数条一手生态事实：BSD 系统是当时多数商业 IPv6 实现的交付基础；Mac OS X 的 IPv6 栈源自 KAME 项目（kame.net）；itojun 保有 FreeBSD、NetBSD 与 Darwin 的提交权但平时不常用，其与 BSD 社区的广泛人脉正是修改 IPv6 问题的协作渠道；其主力开发平台与日常控制台为 Mac OS X，理由之一正是其内置 KAME 系 IPv6。 [存疑脚注] 转写作“Pamela.net”“OpenVC”，前者按语境应为 kame.net，后者所指项目无法从转写确认（BSDTalk EP115，[231.5-290.62, 254.5-287.7]，L1）

**史观**：

- 总纲8 本体论上各方平等：面对 KAME 代码被各操作系统吸收并各自改进是否分叉的提问，Jinmei 给出了明确的多实现肯定论：这并非 KAME 特有问题，各 BSD 本就各有特性，IPv6 栈在各系统内按自身道路演化是应然之事，偶尔协同对齐即可；多种实现提供选择并保障互操作性，是好事而非坏事。这一态度在本体论层面平等看待各 BSD 分支的独立演化。（BSDTalk EP112，[557.08-642.44]，L1）
- 总纲10 动手者创造历史：Jinmei 自述参与写书的动机是知识传承的自我意识：其入行时对网络近乎一无所知，几乎所有网络知识习自 Stevens 的著作并深受其启发，故当受邀参与时，希望能为下一代工程师做 Stevens 曾为他做的事；Qing Li 则称 Stevens 的 TCP/IP 系列是网络开发者的“圣经”、承接其衣钵是“要填的大鞋”，二人明确以向社区回馈经验为目标。一线实现者将一手工程经验整理为教材，正是技术共同体知识再生产的方式。（BSDTalk EP112，[1012.54-1104.3]，L1）
- 总纲13 法律与道德是利益分配：itojun 的自由软件伦理表达直接而具体：技术的根本原则是对所有人可得；他公开反对专利与 API 主张的滥用，并以迪士尼为例批评版权法被利益集团改写——为保护米老鼠，版权保护期自 Walt Disney 死后五十年延长至七十年；他进一步指《狮子王》基本是手冢治虫《森林大帝》的翻版，因而即便东京有迪士尼乐园也拒绝前往，以个人消费选择作抗议。在他看来，版权与专利制度已被从促进创造的初衷扭转为利益分配工具。（BSDTalk EP115，[182.02-231.5]，L1）

**辨析**：

- 关于 IPv6 推广的阻碍，itojun 的判断是：厂商端已无障碍——Windows Vista、Mac OS X 与各路由器厂商均已支持 IPv6，且 Juniper 的实现即源自其阵营代码；唯一的阻碍是 IP 从业者与公众缺乏理解，而普通用户只输入 URL 与邮件地址，完全可在无感知中完成 IPv4 到 IPv6 的过渡。其本人的极端实践佐证可行性：日常完全不用 IPv4，访问 Google、Amazon 等 IPv4-only 服务时经 RFC 3142 所述的传输中继转换完成；并指出 APNIC 管辖的亚洲区域地址分配政策远较北美严苛（北美易得整段 B、C 类地址），其自费高额月费的光纤接入仍无原生 IPv6，正持续向 ISP 施压。 [存疑脚注] 其光纤资费与带宽表述转写混乱（“100 million of VPS fiber... only get just $29”），具体数字不可确证（BSDTalk EP115，[290.62-343.42, 467.42-517.22]，L1）

**文献**：

- [BSDTalk EP112] Backman W. BSDTalk: 112: bsdtalk112 - Qing Li and Tatuya Jinmei[EB/OL]. (2007-05-18)[2026-08-27]. <https://archive.org/details/bsdtalk112>.
- [BSDTalk EP115] Backman W. BSDTalk: 115: bsdtalk115 - Jun-ichiro “itojun” Itoh Hagino[EB/OL]. (2007-06-01)[2026-08-27]. <https://archive.org/details/bsdtalk115>.

<!-- /PODCAST_REVIEW -->

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-656 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-656`；w172 YouTube 章节路由采纳）

据 John Baldwin 讲者口述：OpenSSL 主分支已合入 TLS 1.1 与 1.2 的 kTLS 支持（转写音作 tls1.1.2），这部分改动将在 OpenSSL 3.0 版本发布时一并交付给用户使用。（YouTube EPJdgOQi6lX5M，[1886.679-1892.71]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-655 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-655`；w172 YouTube 章节路由采纳）

据 John Baldwin 讲者口述：FreeBSD 已合入 kTLS 的传输端支持，覆盖 TLS 1.0 至 1.3 全部版本，相关代码已进入 FreeBSD 13 的开发分支（转写音作 de-13）。（YouTube EPJdgOQi6lX5M，[1795.12-1802.549]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1202 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1202`；w172 YouTube 章节路由采纳）

据〔BSDCan 2017 IPv6 演讲〕讲者 Massimiliano Stucchi 口述：IPv6 于 1995 年启动。（YouTube EPZFpdrAb14Hc，[404.729-415.67]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-288 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-288`；w172 YouTube 章节路由采纳）

据〔FreeBSD VXLAN 演讲〕讲者口述：VXLAN 使用 UDP 端口 4789。（YouTube EP_1Ne_TgF3MQ，[1049.76-1053.909]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-287 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-287`；w172 YouTube 章节路由采纳）

据〔FreeBSD VXLAN 演讲〕讲者口述：FreeBSD 10.2 于上年加入 VXLAN 支持。（YouTube EP_1Ne_TgF3MQ，[863.92-871.03]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-362 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-362`；w172 YouTube 章节路由采纳）

据〔TCP-to-SCTP 网关讲座〕讲者 Ryan Bickhart 口述：相关代码原置于 FreeBSD 4.10，现正移植到 FreeBSD 7，需补充锁与 SMP 相关适配。（YouTube EPbWiPOhkUQJs，[284.36-292.18]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-829 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-829`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者口述：内核 TLS 代码当前主干只支持到 TLS 1.2，TLS 1.3 补丁已可工作。（YouTube EPp9fbofDUUr4，[2451.1-2458.8]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-916 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-916`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者 Massimiliano Stucchi 口述：他用一台运行 FreeBSD 的 Raspberry Pi 连到一个与另一家 ISP 共用的交换机。（YouTube EPrOahvokPtrs，[2490.4-2498.87]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-914 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-914`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者 Massimiliano Stucchi 口述：他目前在这些设备上运行 FreeBSD 14.0。（YouTube EPrOahvokPtrs，[1110.8-1116.91]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-915 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-915`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者 Massimiliano Stucchi 口述：他主要使用 BIRD 搭配 OSPFv2、OSPFv3、BGP 与 BFD。（YouTube EPrOahvokPtrs，[1134.64-1144.43]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1011 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1011`；w172 YouTube 章节路由采纳）

据〔BSD networking BoF〕讲者 Tom Smyth 口述：对 OpenBSD 路由器而言该议题重要，因为 OpenBSD 仍未充分利用 SMP 多核并行能力（YouTube EPupfkXx0u5WY，[779.839-784.949]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-1531 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1531`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan '19 Network Transport Group 讨论会〕讲者口述：网络传输工作涉及的一组特性在 FreeBSD 11 期间属实验性质、无一达到可称正式支持的程度，到 FreeBSD 12 本应脱离实验状态转为正式特性。（YouTube EPKerJvwqOsbg，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1532 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1532`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan '19 Network Transport Group 讨论会〕讲者口述：rack TCP 不覆盖全部功能，但在判定当前请求无法处理时会回退到默认 TCP 栈，因此多数部署场景相对安全；该特性当时仍被视为实验性质。（YouTube EPKerJvwqOsbg，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1533 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1533`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan '19 Network Transport Group 讨论会〕讲者口述：FreeBSD 的 TCP 栈模块化方案保留一份内置于内核、不可移除的 TCP 栈作为系统启动基线，其上再以模块方式追加 TCP 栈实现。（YouTube EPKerJvwqOsbg，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1534 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1534`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan '19 Network Transport Group 讨论会〕讲者口述：其既定目标是让内核同时驻留多个版本的 TCP 栈并可择一选用，难点在于 Juniper 自身是否投入工时资源，讲者自述无法确定。（YouTube EPKerJvwqOsbg，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1960 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1960`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Do you remember legacy IP?  What happened to FreeBSD's IPv6?〕讲者口述：1999 年 11 月 2 日，KAME 的第一个提交进入 FreeBSD，内容基本只是头文件。（YouTube EPkTTXbZnHMFE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1961 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1961`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Do you remember legacy IP?  What happened to FreeBSD's IPv6?〕讲者口述：把 KAME 快照并入 FreeBSD 后，最早的用者请求是打开 IPv4/IPv6 双栈；讲者称那条提交说明写的是“requested by many”，而双栈至今仍是 FreeBSD 的默认配置。（YouTube EPkTTXbZnHMFE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1962 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1962`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Do you remember legacy IP?  What happened to FreeBSD's IPv6?〕讲者口述：有人注意到 IPv6 的源路由扩展头使单包能在链路两端两个路由器之间往返约 200 次，据此可放大流量做放大攻击；因此 FreeBSD 关闭了源路由的处理。（YouTube EPkTTXbZnHMFE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1963 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1963`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Do you remember legacy IP?  What happened to FreeBSD's IPv6?〕讲者口述：在 IPv6-only 试验那天的回顾里，讲者称自己与基金会都发了新闻稿，但对 FreeBSD 来说那是个相当平淡的日子，网页至今仍留有一部，而且当天运行大体正常。（YouTube EPkTTXbZnHMFE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1993 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1993`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔P07A: Through the Wire: Measurement and Improvement of IPSec - George Neville-Neil〕讲者口述：自 IPSec 引入 FreeBSD 以来，FreeBSD 一直带有一个 null（空）加密／解密方法，方法体里什么都不做；讲者要用这些 null 方法做基线，以确立“仅仅把 ipsec 框架引入系统”本身究竟带来多大开销。（YouTube EP513OLCfwJUA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1994 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1994`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔P07A: Through the Wire: Measurement and Improvement of IPSec - George Neville-Neil〕讲者口述：以千兆位每秒计跑了十组测量，讲者发现仅仅打开 ipsec 框架就会吃掉约 50% 的带宽：在 10 吉比特的链路上不再是 10 吉，而是略低于 5 吉；他说这既表明还有大量工作要做，也决定了随后重新引入加解密算法时看到的数字基准。（YouTube EP513OLCfwJUA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1995 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1995`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔P07A: Through the Wire: Measurement and Improvement of IPSec - George Neville-Neil〕讲者口述：讲者把 FreeBSD 网络栈的性能开销追溯回内核锁的演化史：这套系统承袭自单处理器内核演化出的多处理器内核，最初的做法是把一把 giant lock 整个罩在内核周围；到 FreeBSD 5 才开始把内核一点一点切开。（YouTube EP513OLCfwJUA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1996 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1996`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔P07A: Through the Wire: Measurement and Improvement of IPSec - George Neville-Neil〕讲者口述：FreeBSD 网络栈过去有两条转发路径，一条叫 fast path 且默认是关闭的，另一条是常规路径；讲者认为“快路径默认关闭”地把系统发出去不对，于是重写相关代码，使系统总是先尝试 fast path，失败才回退。（YouTube EP513OLCfwJUA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2054 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2054`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔EuroBSDcon 2024 讲者 Gregor Haywood《In-Kernel End-System Multihoming with ILNP》〕讲者口述：讲者在 FreeBSD 内核内推进 ILNP（标识符-定位符网络协议）端到端多归属实现时，自述 FreeBSD 的 IPv6 扩展头代码“本来都在那儿”，填入正确的头布局后会自动附加到每个发送的报文上；讲者又自述其此前曾在内核中检索过使用该功能的他处代码而未能找到，故推测该标准化能力“正好直到此前从未被使用过”（原文为‘I don't know if there was other functionality and it got removed or if this was just written into the operating system because it's standardized and it just happens to never be used until now’的不确定表述）。此系讲者单人检索内核后的推测，未与源码提交记录交叉验证，不得写作已核证结论。（YouTube EPuQ9dKbKtEaQ，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2137 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2137`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Henning Brauer 于 AsiaBSDCon 2013 P7B 演讲〕讲者口述：自己已在网络栈上工作了十年，但校验和的触须纠缠之深仍超出预期，真正读代码时才发现远比想象复杂。（YouTube EPmrFud9ySkB0，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2138 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2138`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Henning Brauer 于 AsiaBSDCon 2013 P7B 演讲〕讲者口述：模板 PCB（转写音‘template PC’）在建连时复制对端信息后就地沿用原有校验和，该值只覆盖少量头部字段而不覆盖整个载荷，故称伪头校验和，实际上毫无用处。（YouTube EPmrFud9ySkB0，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2139 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2139`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Henning Brauer 于 AsiaBSDCon 2013 P7B 演讲〕讲者口述：增量子校验和更新这种 hack 也许只对那种极慢的老旧 HP 300 系统有帮助，在现代大缓存系统上反而适得其反：增量更新会打碎缓存行，而那些系统缓存都很小。（YouTube EPmrFud9ySkB0，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2140 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2140`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Henning Brauer 于 AsiaBSDCon 2013 P7B 演讲〕讲者口述：为桥情形写下的校验和相关代码大多无用，这个问题十年前就该在桥代码里修掉，而不是任由各种特例判断向协议层扩散。（YouTube EPmrFud9ySkB0，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2141 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2141`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔A. Kantee“Environmental Independence: BSD Kernel TCP/IP”演讲〕讲者口述：这套让内核 TCP/IP 栈跑在用户态的东西最初导入时最难的是取名，David Holland 建议叫 rum，取 runnable user space module 之意以对应 loadable module，讲者当时觉得是好主意。（YouTube EPRxFctq8A0WI，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2142 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2142`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔A. Kantee“Environmental Independence: BSD Kernel TCP/IP”演讲〕讲者口述：但树里已有一个同名驱动叫 rum，计划因此被打乱；讲者反复推敲后决定改以食物命名，即 rump。（YouTube EPRxFctq8A0WI，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2143 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2143`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔A. Kantee“Environmental Independence: BSD Kernel TCP/IP”演讲〕讲者口述：用户态里本就有现成的锁接口 pthread mutex，与内核锁接口只是名字不同、作用完全一致，因此不必自行实现一套符合内核锁语义的锁，直接借用 pthread 的锁与线程机制即可。（YouTube EPRxFctq8A0WI，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2144 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2144`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔A. Kantee“Environmental Independence: BSD Kernel TCP/IP”演讲〕讲者口述：理论上可以在 FreeBSD 上运行 NetBSD 的网络栈，为此需要在 FreeBSD 里补上类似支持；工作量不大但琐碎繁多，且一般情形下无法顺利对接，因为两边结构体布局不同。（YouTube EPRxFctq8A0WI，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2566 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2566`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Ana Kukec: Native SeND kernel API for *BSD〕讲者口述：讲者自述供职于克罗地亚萨格勒布大学，本次报告主题是面向 BSD 的原生 SeND（安全邻居发现协议）内核 API，该项目是她 2009 年的谷歌编程之夏（GSoC）项目。（YouTube EP3ATCw_03jf8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2567 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2567`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Ana Kukec: Native SeND kernel API for *BSD〕讲者口述：她指出既有 SeND 用户态实现的两大缺陷之一，是经由内核过滤框架加 bpf 过滤器把邻居发现消息送交用户态守护进程，IPv6 的所有报文都须经过 bpf 过滤器，开销过大。（YouTube EP3ATCw_03jf8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2568 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2568`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Ana Kukec: Native SeND kernel API for *BSD〕讲者口述：除开销之外，旧实现所依赖的内核过滤框架并不被整个 BSD 家族支持，因此她希望做出可移植到其他 BSD 系的方案。（YouTube EP3ATCw_03jf8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2569 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2569`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Ana Kukec: Native SeND kernel API for *BSD〕讲者口述：截至本次报告时，她已让代码跑起来的是原生的 SeND socket，她描述其形态与 divert socket 很相似。（YouTube EP3ATCw_03jf8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2636 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2636`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔AsiaBSDCon 2013 演讲：Olivier Van Acker〕讲者口述：他选用 FreeBSD 是因为 SCTP 的参考实现主要在 FreeBSD 上完成，而他自己的服务器原本就跑该系统。（YouTube EPPLCaUtArADA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2637 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2637`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔AsiaBSDCon 2013 演讲：Olivier Van Acker〕讲者口述：论文进行到一半时，编写 SCTP 规范的人更新了 SCTP API，使他原先那套（已不再需要的）做法作废，只得把实现从头重写。（YouTube EPPLCaUtArADA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2638 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2638`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔AsiaBSDCon 2013 演讲：Olivier Van Acker〕讲者口述：SCTP 参考实现（转写作 drive，即 driver）可供取用；若要在 Mac 上运行可到参考实现处，其中有一个 Xcode 工程可直接打开编译，如今还另有安装包可装。（YouTube EPPLCaUtArADA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2639 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2639`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔AsiaBSDCon 2013 演讲：Olivier Van Acker〕讲者口述：在 FreeBSD 的情形下，Go 的 syscall 目录里脚本会取用该系统调用号主文件（转写作 cisco master file），据此生成一圈相关的系统调用封装函数。（YouTube EPPLCaUtArADA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
