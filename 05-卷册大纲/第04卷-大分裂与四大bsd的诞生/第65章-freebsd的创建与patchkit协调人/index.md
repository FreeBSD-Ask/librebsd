---
chapter: 第 65 章
id: CH65
volume: 第04卷-大分裂与四大bsd的诞生
---

# 第 65 章 freebsd的创建与patchkit协调人

## 要点

- FreeBSD 仓库共 1294851 次提交（1993-06-12 至 2026-08-25），3720 位贡献者（口径未注明，疑为去重 author 口径；freebsd.duckdb contributors 表 DB_REF 口径实测 5671 行），是从 386BSD patchkit 协调人模式演化而来的核心代码库

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3679] 卷“第04卷-大分裂与四大bsd的诞生”第 65 章，匹配置信度 folder，原因：folder 第64章
- [DB:references_fulltext:chapter_matches:chmatch_3704] 卷“第04卷-大分裂与四大bsd的诞生”第 65 章，匹配置信度 folder，原因：folder 第64章
- [DB:references_fulltext:chapter_matches:chmatch_3782] 卷“第04卷-大分裂与四大bsd的诞生”第 65 章，匹配置信度 folder，原因：folder 第64章
- [DB:references_fulltext:chapter_matches:chmatch_3783] 卷“第04卷-大分裂与四大bsd的诞生”第 65 章，匹配置信度 folder，原因：folder 第64章
- [DB:references_fulltext:chapter_matches:chmatch_3792] 卷“第04卷-大分裂与四大bsd的诞生”第 65 章，匹配置信度 folder，原因：folder 第64章
- [DB:references_fulltext:chapter_matches:chmatch_3807] 卷“第04卷-大分裂与四大bsd的诞生”第 65 章，匹配置信度 folder，原因：folder 第64章
- [DB:references_fulltext:chapter_matches:chmatch_3829] 卷“第04卷-大分裂与四大bsd的诞生”第 65 章，匹配置信度 folder，原因：folder 第64章
- [DB:references_fulltext:chapter_matches:chmatch_3966] 卷“第04卷-大分裂与四大bsd的诞生”第 65 章，匹配置信度 folder，原因：folder 第64章

- [DB:code_repos:freebsd.duckdb] FreeBSD 仓库共 1294851 次提交（1993-06-12 至 2026-08-25），3720 位贡献者，是从 386BSD patchkit 协调人模式演化而来的核心代码库

## 史观

- 第 8 条本体论上各方平等：FreeBSD 的创建是 patchkit 协调人模式的产物，非单一英雄叙事；第 10 条动手者创造历史：默默贡献的 patchkit 提交者才是真正的奠基人

## 辨析

- FreeBSD Handbook 原文明确记载 1.0 "based on the 4.3BSD-Lite (‘Net/2’) tape from U.C. Berkeley, with many components also provided by 386BSD and the Free Software Foundation“；~~原 ”4.3BSD-Reno" 说法错误~~，Net/2 与
- Handbook 仅记载提供 “a machine to work on and a fast Internet connection”，具体服务器规格（486）、带宽速率（T1）、Core Team 成员是否在 Walnut Creek 兼职等细节需对照合同邮件核验，避免夸大或简化；〔待核：原文截断，后文待回源〕
- Walnut Creek 提供的服务器具体规格与带宽速率需对照 1994 年邮件列表核验；FreeBSD 1.0 公告中 FTP 站点为 freebsd.cdrom.com，证实 Walnut Creek 从一开始就托管 FTP 分发
- GEOM 存储框架由 Poul-Henning Kamp 开发，但 GEOM 首次随 FreeBSD 5.0（2003 年 1 月）引入，不属于 1.0-2.0（1993-1994）时期的贡献；PHK 在 1994 年已是 FreeBSD 2.0 的 release engineer，早期贡献包括发布工程、内存分配器（malloc）、NTP 等，非 SCSI/GEOM 子系统
- 具体贡献者的具体技术工作需对照源码 commit message 核验（GEOM 时期辨析已见上一条，不重复）

## 文献

- [DB:references_fulltext] 参考文献全文数据库（4077 篇全文，27138 条时间线事件）—— 对应 freebsd.duckdb

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP566、BSD Now EP172、BSD Now EP13、YouTube EPnwbqBdghh6E（共 4 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 主持人介绍 FreeBSD Day 的 31 周年庆祝，并转述一篇综述文章对 FreeBSD 历史的阶段划分：1993 年 1.0 首发，2.0 与 2.1 引入 ports 集合，3.0 引入 GEOM 框架与对称多处理改进，4.x 以稳定著称，6.x 引入 jails，8.x 与 9.x 引入 ZFS 与 DTrace，后续版本扩展 ARM 架构支持。（BSD Now EP566，[367.60-589.20]，L2）
- Tom Jones 自述受 FreeBSD 基金会与 RG Nets 共同资助，将基于 DPDK 的高性能用户态转发框架 VPP 移植到 FreeBSD 并回馈上游，产生逾百项变更，约 20% 已合并，移植工作还促使 VPP 核心基础设施变得更灵活。（BSD Now EP566，[1513.74-1930.24]，L1）
- 主持人评述 Rust 的 crates.io 依赖注册表存在供应链安全隐患，并对比 OpenBSD 与 FreeBSD 基本系统自带经审查工具、无需海量外部依赖的路径。（BSD Now EP566，[2342.36-2831.24]，L2）
- Rod Grimes 自述 1970 年代初在 Oregon Museum of Science and Industry 的 PDP-11/45 上，利用夜间时段重新引导系统运行早期 AT&T Research Unix，白天机器则运行博物馆业务用的分时系统，并使用 Tektronix 4000 系列图形终端。（BSD Now EP172，[1331.76-1442.94]，L1）
- FreeBSD 创建时期，Rod Grimes 主要用 386BSD 做 SLIP 路由器以避开拨号 BBS 的 shell 上网方式，并借此获取 SPICE 等电子工程软件，时间约为 1992 年。（BSD Now EP172，[1487.16-1557.9]，L1）
- Rod Grimes 用 dd 反复读取坏块做磁盘数据恢复，指出 FreeBSD 在 ATA 或 SCSI 设备被卡住时不像其他系统那样锁死，因此长期用于路由器、LAMP 服务器与批量邮件系统。（BSD Now EP172，[1600.96-1667.48]，L1）
- FreeBSD 创始团队并未以竞争产品心态出发，只是出于必要与愿望；当时担心的并非被击垮，而是与 386BSD、BSDI、NetBSD 的关系，Linux 仅被视为另一份开源软件。（BSD Now EP172，[1807.66-1906.68]，L1）
- Rod Grimes 自认不适合仁慈独裁者角色，因自己观点强硬且无法掌握操作系统全部细节，并认为独裁模式长期会分裂团队，FreeBSD 实际采用接近 CSRG 伯克利团队的合作模式。（BSD Now EP172，[1900.99-2003.26]，L1）
- Rod Grimes 认为 FreeBSD 做得正确的包括系统性能、网络栈、ports collection，以及开源带来的可观察性，使系统状态易于查看。（BSD Now EP172，[2184.6-2295.72]，L1）
- Rod Grimes 认为项目早期过度锁定 x86 架构，使后来支持 MIPS 与 ARM 更困难；同时宣传不足，FreeBSD 虽很早运行于 Raspberry Pi 3，但快照未公开、网络与图形缺失，削弱了在 ARM64 嵌入式市场的影响。（BSD Now EP172，[2303.2-2494.7]，L1）
- Rod Grimes 希望 2017 年推进 GPL 代码移除（GPL clean release 为 12.0 目标）、ARM 与 MIPS 升至 Tier 1，并推进 bhyve 的 hypervisor 能力与 GPU passthrough。（BSD Now EP172，[2640.04-2725.56]，L1）
- Rod Grimes 与 Michael Dexter 合作推进 bhyve GPU passthrough，已能在 bhyve 内看到 PCI GPU 设备的 probe 与 I/O 映射，但内存块尚缺失，预期 2017 年初可见工作原型。（BSD Now EP172，[2726.62-2836.32]，L1）
- OpenSSH 7.4 由 Damien Miller 发起公开测试，移除 SSH v1 服务器支持与 3DES-CBC 默认密码，禁用预认证压缩与 UseLogin，并新增受 PuTTY 启发的 proxy multiplexing 与 curve25519-sha256 密钥交换。（BSD Now EP172，[94.39-364.48]，L2）
- Ingo Schwarze 在 Toulouse 的 LibreSSL hackathon 中完成 libcrypto 剩余 130 页手册的 pod2mdoc 转换，使全部文档可用 mdoc 检索，并回顾了 2014 年以来 Anthony Bentley 等人的转换史。（BSD Now EP172，[3495.94-3681.4]，L2）
- Matthew Garrett 批评 Canonical 的 IP 政策：若按政策理解，分发基于 Ubuntu 的作品即使不称 Ubuntu 也可能需向 Canonical 付费，这超出商标保护范围，故 Ubuntu 不是自由软件。（BSD Now EP172，[3872.04-4203.14]，L2）
- DEMOS 是 1982 年诞生于莫斯科原子能研究所的 Unix 类操作系统，源自 MNOS 对 Unix v6 的克隆，1986 至 1990 年各版本合并为 DEMOS 2，运行于 SM4、SM1600 及 VAX 克隆与 Motorola 6820 微机，后转向 Relcom。（BSD Now EP172，[4550.66-4645.46]，L2）
- Jordan Hubbard 自述早期 Unix 因 AT&T 源码许可昂贵且排他，386BSD 由 Bill Jolitz 补齐 Intel 架构缺件后首次让普通 PC 运行 BSD；他与 Nate Williams、Rod Grimes 共同维护 386BSD patch kit，最终另立 FreeBSD。（BSD Now EP13，[800.4-1148.2]，L1）
- FreeBSD 之名由 David Greenman 提出；1.0 发布后，Hubbard 联系 Walnut Creek CD-ROM 出版发行版，并获得 John Lasseter 与 Kirk McKusick 协助解决 Beastie 封面版权。（BSD Now EP13，[1109.0-1292.6]，L1）
- 他先后编写包管理工具与 ports 集合，把约 300 个 port 交由 Satoshi Asami 维护后转向 sysinstall 与发布工程；未料 ports 日后增至约 25,000。（BSD Now EP13，[1500.5-1562.3]，L1）[订正：原 [1502.6-1547.3]，2026-09-30 SenseAudio 重转核对]
- 2001 年他离开 FreeBSD 加入 Apple，组建 BSD Technology Group，以 FreeBSD 3.2 为参考平台持续向 OS X 回灌新版 FreeBSD 代码，直至 2013 年出任 iXsystems CTO。（BSD Now EP13，[1609.6-1826.9]，L1）[订正：原 [1609.7-1837.5]，2026-09-30 SenseAudio 重转核对]
- 新闻部分报道 DragonFly BSD 3.6 发布、dports 默认化，以及 FreeBSD CURRENT 中 ZFS 在 SSD 上启用 TRIM 时的数据损坏风险警告。（BSD Now EP13，[566.2-737.9]，L2）
- McKusick 以当事人视角浓缩 BSD 全史：Ken Thompson 身为伯克利校友，1975 年学术休假时把 UNIX 带回校园，一年内吸引了一批研究生；1976 年他离开时 Bill Joy 已接管系统并继续开发，随后把伯克利开发的软件打包，以 Berkeley Software Distributions 之名发行，年度发行延续近十五年，先后由 Joy 与包括 McKusick 本人在内的后来者主持；1980 年代末自由再分发软件的兴趣渐起，伯克利同人着手把 AT&T 专有部分从 BSD 中剥离，到伯克利的最终发行版（转写作 1992 年）整个发行已可自由再分发；此后两支力量接续支撑 BSD——NetBSD 以支持尽可能多的硬件架构为目标，从微波炉到 Cray XMP 皆在其列，其口述时点已支持近六十种架构，FreeBSD 则以在 PC 架构上运行 BSD、支持尽可能广的设备并把系统做得尽量易装以吸引广大开发者为目标；他本人选择主要跟随 FreeBSD 群体，一面做软件，一面与 George Neville-Neil 合著 The Design and Implementation of the FreeBSD Operating System。（YouTube EPnwbqBdghh6E，[39.9-171.069]，L1）
- McKusick 叙述 UNIX 的诞生语境：UNIX 之前的主角是 Multics（他按读音称 Multix），由 Honeywell、AT&T 贝尔实验室与 MIT 三方合力建造分时系统，项目愈益宏伟却始终未能进入生产，每学会做一件事便又推倒重构去做下一件；贝尔实验室撤出后，已经习惯坐在 ASR33 电传终端前交互编程的 Ken Thompson 与 Dennis Ritchie 不愿退回打卡片的作业流，从角落里翻出一台废弃的小型机（转写作 PDP-8），写出一个极小的系统即 UNIX，其后迁往 PDP-11；鉴于 Multics 万事求全的教训，两人确立“找出做事的那一种方式”的极简哲学，标识符只保留进程号、用户号与组号寥寥数种，并让同一组标识符兼作计数、保护判定与调度决策之用。[订正：原区间终点 1994.2→1997.41，原终点止于转写“used for counting, used for making”段，“protection decisions, used for scheduling decisions”（保护判定与调度决策）落转写 [1994.2-1997.41] 段，内容复核]（YouTube EPnwbqBdghh6E，[1864.49-1997.41]，L1）
- McKusick 把统一描述符空间列为 UNIX 的两大关键观念之一：给定一个描述符即可引用终端、文件、磁盘、管道或套接字等任何 I/O 通道，使用者无须知道它背后是什么便能读写且行为正确；此前各设备各配一套打开、读、写、关闭调用，像 cat 这样的程序必须自行判别输入类型并分派调用，统一之后程序只管读写，新增描述符类型亦不破坏既有程序；他称此后几乎每个操作系统都采纳了这一构造，唯太平洋西北岸一家大公司的系统至今未完全统一，并打趣说 Longhorn 会解决这个问题。（YouTube EPnwbqBdghh6E，[2019.74-2143.939]，L1）
- McKusick 把进程即商品列为另一关键观念：UNIX 之前的系统里进程是重型的贵重资源，IBM MVS 由系统管理员在引导时决定多重处理度数并预先创建定数进程，用户以 JCL 把编译各步写成一叠卡片作业——他称 JCL 是“六十年代的 sendmail 配置文件”，多一个空格或丢一个逗号整个作业即被吐回，且须经操作员换卡重交、等待数小时才能看到结果；UNIX 让这类记账性工作交给机器，按需即时创建进程、以管道相连、用毕即弃——一次编译即把预处理器、多趟编译器、优化器与装载器等七个进程经管道流水串联；他强调这并非进程创建变得廉价（以运行 ls 为例，九成以上成本仍在创建与销毁进程本身），而是省下的编程人力值得付出这份开销；早期内存不足时管道在底层实为文件，今则全在内存中流转。（YouTube EPnwbqBdghh6E，[2195.819-2539.239]，L1）

**史料**：

- 本期核心史料为 hemradio.mi 的 FreeBSD 历史综述文章与 Tom Jones 的 VPP 移植技术文章；后者为当事人一手工程记录。（BSD Now EP566，[367.60-589.20]，L2）
- Rod Grimes 访谈自述（FreeBSD 创始成员、BSD janitor），覆盖 1970 年代初 Unix 接触与 FreeBSD 创建史。（BSD Now EP172，[1315.96-3158.28]，L1）
- Damien Miller 发布的 OpenSSH 7.4 公开测试说明与变更清单。（BSD Now EP172，[94.39-393.72]，L2）
- Ingo Schwarze 的 LibreSSL 手册转换 hackathon 报告（含 pod2mdoc 转换时间线）。（BSD Now EP172，[3495.94-3681.4]，L2）
- Matthew Garrett 对 Canonical IP 政策的博客批评与 Mark Shuttleworth 的官方立场博客。（BSD Now EP172，[3872.04-4203.14]，L2）
- 本期为 McKusick 内核课程宣传片与第一讲选段的一手口述：当事人自述其浓缩伯克利全史的三小时半录像与十二讲、约三十小时课程均发布于个人网站 www.mckusick.com，教科书为其与 George Neville-Neil 合著的 The Design and Implementation of the FreeBSD Operating System；讲义附录另载一篇约五年至八年前发表的 journalling 与 soft updates 比较论文，其结论为两种一致性方案性能相当，可作文件系统技术史线索。[订正：原考据脚注“本流转写被系统标记 severe_repetition，宣传片引言、第一讲开讲与第一讲正文三条音轨交错混排”之缺陷经滚动重叠重建后已不存在，新转写为单轨顺排]　[已核备注] 新转写已为单轨顺排，多音轨交错缺陷不再存在；人名与机器型号转写音变（如 PDP-8）仍见于自动转写，引用前仍须按通行记载核对。（YouTube EPnwbqBdghh6E，[103.62-191.139]，L3）

**史观**：

- 总纲10 动手者创造历史：Tom Jones 以受资助的工程工作完成 VPP 移植并推动上游改进，体现动手者通过具体技术贡献塑造系统生态。（BSD Now EP566，[1513.74-1930.24]，L1）
- 总纲13 法律与道德是利益分配：VPP 移植由基金会与商业公司共同出资，显示开源工程背后持续存在的资金与利益安排。（BSD Now EP566，[1557.02-1567.42]，L1）
- 总纲5 没有必然性，只有偶然性：Rod Grimes 强调 FreeBSD 的诞生出于必要与愿望而非与对手竞争，具体起点由当时的人和需求决定，而非历史必然。（BSD Now EP172，[1807.66-1906.68]，L3）
- 总纲6 和解优于斗争：Rod Grimes 认为独裁会分裂团队，合作环境更能避免分裂，治理选择倾向于和解而非斗争。（BSD Now EP172，[1945.54-2003.26]，L3）
- 总纲9 经验优先：ports collection 让“别人已完成的移植”成为可复用经验，使个体不必重复劳动，工程效率建立在经验累积之上。（BSD Now EP172，[2210.38-2247.96]，L3）
- 总纲10 动手者创造历史：Rod Grimes 以修复旧物、做数据恢复与移植为乐，历史由具体动手者而非抽象方案推进。（BSD Now EP172，[1600.96-1667.48]，L3）
- 总纲4 分离聚合是永恒规律：早期聚焦单一 x86 架构导致机独立代码不够架构中立，后期向 ARM/MIPS 迁移困难，单点聚焦与多架构分散之间存在结构张力。（BSD Now EP172，[2321.18-2399.88]，L3）
- 总纲4 分离聚合是永恒规律：FreeBSD 的创立是 386BSD 社区在 patch kit 难以为继时的一次分离，而非预先规划的必然结果。（BSD Now EP13，[1042.0-1148.2]，L1）
- 总纲13 法律与道德是利益分配：Hubbard 称 BSD 许可证只有两句话且逐年变短，开发者以代码被使用的广度而非金钱衡量成就，体现与 GPL 扩张相反的法律简省取向。（BSD Now EP13，[2209.6-2362.5]，L1）
- 总纲4 分离聚合是永恒规律：McKusick 指出虚拟机并非新物：1960 年代计算机以冰箱大小的机柜与洗衣机大小的磁盘机组成，造价数百万美元的机器每秒仅约千万条指令，人人直接对裸硬件编程，IBM 以 VM 系统在一台十 MIPS 巨机上克隆出多台一模一样的裸机，各自引导数据库、工资单或分时作业；UNIX 借用其“独立可操作之物”的观念却把界面抬升到进程层，而授课时 VMware 一类产品又让用户回到引导原生操作系统——他称之为“关于正确层次为何的钟摆”往返摆动；抽象的聚拢与拆散在裸机、进程诸层之间循环往复，而非沿单一直线推进。（YouTube EPnwbqBdghh6E，[2151.559-2178.89]，L1）
- 总纲5 没有必然性，只有偶然性：McKusick 的 Multics—UNIX 叙事把操作系统的分野落在偶然条件而非必然规律上：三方合作的宏伟计划因不断加码而自我瓦解，UNIX 之所以存在，系于贝尔实验室一次撤出、两位研究者对交互式终端的眷恋，以及角落里恰好闲置的一台旧机器；课程亦以“一切从最顶层宽笔刷讲起、再逐层下探”的三遍式结构自反地承认听者知识水平参差，不预设任何单线的技术进步叙事。（YouTube EPnwbqBdghh6E，[336.28-403.759]，L1）

**辨析**：

- 综述文章对 FreeBSD 各版本与特性年份的归属存在简化乃至偏差，例如将 APT 误作 FreeBSD 包工具，具体里程碑须以官方发布说明核实。　[存疑脚注] 综述文章的版本与特性对应关系存在简化或偏差，未经官方发布说明逐项核实。（BSD Now EP566，[468.76-493.60]，L4）
- [存疑脚注] 转写将 OMSI 白天运行的分时系统记作“RISC-C”，疑为 DEC RSTS/E 的误转；Rod Grimes 首次接触 Unix 的具体年份与机型须以一手采访或档案复核。　[存疑脚注] 分时系统名与年份须核验一手资料。（BSD Now EP172，[1452.7-1463.98]，L4）
- [存疑脚注] OpenBSD Foundation 首笔铱金捐赠方转写为“smartizan/smartian”，疑指 Smartisan（锤子科技），280,000 加元金额与币种须核验官方公告。　[存疑脚注] 捐赠方名称与金额须核验。（BSD Now EP172，[4417.12-4457.48]，L4）
- [考据脚注] DEMOS 全称在转写中变形严重，应为俄语“Диалоговая Единая Мобильная Операционная Система”的英译，引用时须以俄文一手资料核验。　[考据脚注] 俄文全称须核验一手资料。（BSD Now EP172，[4557.02-4586.12]，L4）
- 本卡片所据转写文本实际存放于 663.txt（其内部标为第 13 期），而 664.txt 为第 12 期内容之重复，转写文件与期号存在错位。　[存疑脚注] 转写文件错位：664.txt 实为第 12 期，第 13 期内容见于 663.txt。（BSD Now EP13，[57.6-66.7]，L4）
- 转写中 Thompson 与 Ritchie 起家所用机器记作 PDP-8（新转写逐字证实演讲原话即为 PDP-8），与通行记载的 PDP-7 不符，疑为口误或转写之误；同段称伯克利“最终发行版”年份为 1992 年，而通行纪年为 4.4BSD 于 1993 年发布、4.4BSD-Lite 于 1994 年发布，McKusick 所述或指代码清理完成之时点；两处纪年均属单一来源口述，引用前须另行核验。[订正：原存疑脚注“本流转写为多音轨交错合并”之转写缺陷经滚动重叠重建后已不存在，新转写为单轨顺排]　[已核备注] 新转写已为单轨顺排；PDP-8 机型与 1992 年末版年份两处纪年仍系单一来源口述且与通行记载存在出入，未经与 McKusick 出版著作及 CSRG 发行记录交叉核对前不宜直接引用。（YouTube EPnwbqBdghh6E，[1933.44-1946.549]，L4）

**文献**：

- [BSD Now EP566] Pennington J. BSD Now: 566: Open Source Excellence[EB/OL]. (2024-07-04)[2026-08-15]. <https://www.bsdnow.tv/566>.
- [BSD Now EP172] Pennington J. BSD Now: 172: A tale of BSD from yore[EB/OL]. (2016-12-14)[2026-08-15]. <https://www.bsdnow.tv/172>.
- [BSD Now EP13] Pennington J. BSD Now: 13: Bridging the Gap[EB/OL]. (2013-11-27)[2026-08-15]. <https://www.bsdnow.tv/13>.
- [YouTube EPnwbqBdghh6E] YouTube. YouTube: FreeBSD Kernel Internals, Dr. Marshall Kirk McKusick[EB/OL]. ()[2026-08-15]. <https://www.youtube.com/watch?v=nwbqBdghh6E>.

<!-- /PODCAST_REVIEW -->
