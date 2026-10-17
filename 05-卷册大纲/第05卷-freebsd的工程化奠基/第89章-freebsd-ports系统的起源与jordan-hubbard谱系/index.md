---
chapter: 第 89 章
id: CH89
volume: 第05卷-freebsd的工程化奠基
---

# 第 89 章 freebsd-ports系统的起源与jordan-hubbard谱系

## 要点

- FreeBSD 仓库构成（按提交量）：freebsd-ports(788411)、freebsd-src(445203)、freebsd-doc(61237)。Ports 树提交量占比最大，反映第三方软件生态的工程规模

## 史料

- [DB:bsdnow_podcast:outline_mappings:om_10489] BSD Now 第 664 期，匹配 CH89 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10799] BSD Now 第 613 期，匹配 CH89 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10875] BSD Now 第 603 期，匹配 CH89 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11125] BSD Now 第 573 期，匹配 CH89 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11132] BSD Now 第 572 期，匹配 CH89 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11198] BSD Now 第 564 期，匹配 CH89 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11752] BSD Now 第 493 期，匹配 CH89 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12548] BSD Now 第 416 期，匹配 CH89 章，关联度 1.0

- [DB:code_repos:freebsd.duckdb] FreeBSD 仓库构成（按提交量）：freebsd-ports(788411)、freebsd-src(445203)、freebsd-doc(61237)。Ports 树提交量占比最大，反映第三方软件生态的工程规模

## 史观

- 总纲第 11 条“商品是形式主义”〔订正：原作自撰标签“形式主义”无权威条号，依核查报告挂总纲 11 并用权威全称〕：Ports 系统是“软件包管理”这一形式主义概念在 FreeBSD 生态中的物质化

## 辨析

- 部分 bsd.port.mk 的大改未在 commit message 中标注版本号，需以功能为分界；**统计局限性标注**——统计显著 ≠ 实际显著，C-12 变点 p < 0.001 仅反映 freebsd-src commit 时序存在结构性断点，不直接等同于 Ports 系统同期发生同步变点；E-14 FreeBSD ports 784,191 commits 包含 Ports 系统全生命〔存疑：原文截断，待回源补全；E-14 数值系旧快照，实测 freebsd-ports 788,411，依核查报告注明漂移〕
- 40,000+（2022）与 34,000+（2024）两组数字可能分别对应“仓库中全部 port 条目数”与“可构建/活跃 port 数”，须在正文中明确标注口径，避免引用冲突；Mingrone 所载 SVN 接管日期（2012-07-15）与本卷 87.8 节 ports 仓库迁移首 commit 日期（2012-07-14）相差一日，须以 SVN 转换日志为准交叉核验
- CVSup 废弃的精确时间存在 2008(SVN 迁移) 与 2012(最后镜像关闭) 两种说法
- pkgng 是否“解决”了分歧存在争议，Ports 仍保留编译选项
- 考据过程留痕——【查证来源】pkg(8) 手册页经 FreeBSD 官方文档一手核验，pkg(8) 命令行工具与子命令集（install/upgrade/delete/query/info 等）在手册页中完整描述；freebsd-pkg 邮件列表 2011-2016 归档经 <https://lists.freebsd.org/archives/freebsd-pkg/> 一手核验，覆盖 pkgn〔存疑：原文截断，待回源补全〕

## 文献

- [DB:references_fulltext] 参考文献全文数据库（4077 篇全文，27138 条时间线事件）—— 对应 freebsd.duckdb

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP499、BSD Now EP312、BSD Now EP283、BSD Now EP223、BSD Now EP13、BSDTalk EP55（共 6 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Dan Langille 自述 FreshPorts 迁移史：该服务原运行于 New Jersey 由 IAC Systems 捐赠的主机，主机突然失效后回退 Austin 旧主机，随后借重写机会迁移至 AWS，并将提交处理、Web 请求与数据库拆分为独立 jail；他称 FreshPorts 已运行约 20 年，希望未来由 FreeBSD 项目接手维护。（BSD Now EP499，[2093.20-2320.00]，L1）
- 其家庭实验室以一台从电子废弃物中回收的 Dell R730 取代两台旧主机，运行约 40 个 FreeBSD jail，主要用于 FreshPorts 的 dev、test、stage 环境及多种服务；迁移通过 Syncoid 的 ZFS 发送接收完成，并带来约 25% 的功耗下降。（BSD Now EP499，[139.80-530.00]，L1）
- Langille 以 BSDCan 组织者身份回顾会议史：其自 2004 年举办第一届 BC camp，至 2023 年已连续办会 20 年；疫情后会议以严格口罩政策线下重启，并招募志愿者分担会议包、场地与演讲者事务。（BSD Now EP499，[1442.02-2093.20]，L1）
- 节目还讨论 jail 管理器因难以适配特定场景被弃用，转而使用自维护的 MakeJail 脚本，显示 jails 生态中用户为适应具体需求而回归手工脚本。（BSD Now EP499，[1666.86-1734.30]，L1）
- 本期转述 WWIT Pro 上的一场 Unix 哲学报告，将一切皆文件、单功能小工具、管道组合、模块化、分离、简洁、透明、失败、多样性、可扩展与简约性重新表述为 2019 年的十条原则。（BSD Now EP312，[389.36-592.56]，L2）
- 威斯康星大学密尔沃基 HPC 实验室文章论证包管理器价值：避免手工安装的重复劳动与不可复现，并比较 ports、pkgsrc、MacPorts 等源码与二进制管理路径，强调科研可复现性。（BSD Now EP312，[601.24-1049.34]，L2）
- Joshua Stein 记述 OpenBSD 触控板两年中断缺失问题，最终定位为 ACPI 节点遍历顺序与 ACPICA 不同，通过改写遍历算法修复并弃用强制轮询。（BSD Now EP312，[1061.82-1661.96]，L2）
- 受访者自述 FreeBSD 图形栈在其设备上基本可用、可作为日常驱动，但承认体验仍不如 Windows 与 macOS，且特定硬件组合仍会出现挂起与交换分区交互导致的偶发冻结。（BSD Now EP283，[427.99-548.20]，L1）[订正：原 [427.99-503.62]，2026-09-30 SenseAudio 重转核对]
- FreeBSD 图形栈在 2018 年底已大体跟进上游：输入栈与 Mesa 已更新，libinput 补丁位于开发仓库，X server 本体则是最滞后的待移植与待推送部分。（BSD Now EP283，[600.70-674.48]，L1）
- FreeBSD 图形团队规模极小：Johannes Lundberg 负责从 Linux 移植 DRM 驱动并更新 Linux KPI，另一名 Johannes Dietrich 维护 ports 中的图形驱动，Warner Losh 担任与 core 团队的联络，Matt Macy 尝试让 Linux KPI 在 PowerPC64 上运行。（BSD Now EP283，[676.78-944.60]，L1）
- 受访者自 2012 年起维护 FreeBSD ports，长期以 Poudriere 教程作为新人参与入口，认为从维护小型 port 开始逐步深入是降低参与门槛的有效方式。（BSD Now EP283，[998.48-1210.88]，L1）
- 受访者创办面向所有 BSD 的斯德哥尔摩用户组，借助雇主 B3Init 提供的场地举办聚会，规模约二十余人，并总结出首次活动容易高估到场人数等组织经验。（BSD Now EP283，[1222.98-1600.00]，L1）
- 受访者自 2019 年起获得雇主 B3Init 每周两小时带薪 FreeBSD 开发时间，并计划在上半年结束后与雇主共同评估延续方式。（BSD Now EP283，[2014.46-2064.04]，L1）
- backtrace.io 文章比较 GCC 与 Clang 在优化下的 DWARF 调试信息质量，指出 Clang 对部分优化变量可能给出错误值而非“已优化”提示。（BSD Now EP223，[82.36-97.84]，L2）
- 该期讲解 Rust 应用移植到 FreeBSD ports 的流程：ports 以 Makefile 描述构建安装，portlint 检查顺序，make makepatch 生成补丁，约 30,000 个 ports 依赖 POSIX 可移植性。（BSD Now EP223，[916.48-1100.46]，L2）
- 该期辨析 Docker 在 FreeBSD/Solaris 的意义：Docker 是 Linux 与 Windows 隔离问题的解决方案，FreeBSD 以 jails 实现隔离，Docker 的移植依赖 Linux 模拟与 ZFS。（BSD Now EP223，[3109.0-3269.08]，L2）
- FreeBSD 基金会 11 月更新：Matt Ahrens 推进 RAID-Z 扩容（由 FreeBSD 基金会、Delphix、iXsystems 合办），预计 2018 年合入并赶上 FreeBSD 12。（BSD Now EP223，[5082.36-5176.8]，L2）
- Jordan Hubbard 自述早期 Unix 因 AT&T 源码许可昂贵且排他，386BSD 由 Bill Jolitz 补齐 Intel 架构缺件后首次让普通 PC 运行 BSD；他与 Nate Williams、Rod Grimes 共同维护 386BSD patch kit，最终另立 FreeBSD。（BSD Now EP13，[800.4-1148.2]，L1）
- FreeBSD 之名由 David Greenman 提出；1.0 发布后，Hubbard 联系 Walnut Creek CD-ROM 出版发行版，并获得 John Lasseter 与 Kirk McKusick 协助解决 Beastie 封面版权。（BSD Now EP13，[1109.0-1292.6]，L1）
- 他先后编写包管理工具与 ports 集合，把约 300 个 port 交由 Satoshi Asami 维护后转向 sysinstall 与发布工程；未料 ports 日后增至约 25,000。（BSD Now EP13，[1500.5-1562.3]，L1）[订正：原 [1502.6-1547.3]，2026-09-30 SenseAudio 重转核对]
- 2001 年他离开 FreeBSD 加入 Apple，组建 BSD Technology Group，以 FreeBSD 3.2 为参考平台持续向 OS X 回灌新版 FreeBSD 代码，直至 2013 年出任 iXsystems CTO。（BSD Now EP13，[1609.6-1826.9]，L1）[订正：原 [1609.7-1837.5]，2026-09-30 SenseAudio 重转核对]
- 新闻部分报道 DragonFly BSD 3.6 发布、dports 默认化，以及 FreeBSD CURRENT 中 ZFS 在 SSD 上启用 TRIM 时的数据损坏风险警告。（BSD Now EP13，[566.2-737.9]，L2）
- Vinum 起源于真实故障而非规划：Lehey 在中国为 Tandem 讲学时接触 Veritas 卷管理器颇为赞赏；其后加州的 Nicole Harrington 因公司磁盘崩溃无法恢复而求助，其系统运行 FreeBSD 的 CCD 串联磁盘驱动，而 CCD 当时本就不善处理磁盘失败；Lehey 判断 FreeBSD 需要类似 Veritas 的卷管理器，以拉丁语双关命名为 vinum（意为酒）；恰逢 CyberNet 公司寻求 RAID5 实现并支付费用，成果于 1998 年底进入 FreeBSD 源码树。（BSDTalk EP55，[397.8-462.52]，L1）
- 至 2006 年访谈时，Vinum 已被多个 GEOM 类取代，但 Lehey 认为部分 GEOM 类仍未具备 Vinum 五年前已有的特性，希望社区将其吸收进传统 GEOM 类，显示替代并非完整的功能接续。（BSDTalk EP55，[462.52-483.24]，L1）
- SMPNG 的直接诱因是 1999 年 Mindcraft 基准：微软展示 Windows 在部分网络场景胜过 Linux，BSD 方面自知成绩亦不会好看而选择沉默；约一年后社区聚议，认定真正问题在于 Linux 与 BSD 处理多处理器的方式，遂于 2000 年 6 月在 Yahoo 园区开会确立 SMPNG（新一代 SMP 支持）；Lehey 从头参与并先做了约六个月中断处理程序，其后主要由 John Baldwin 接手；项目启动时预计约两年，最终五年后才正式宣告结束。 [考据脚注] 转写将 Mindcraft 误作 Minecraft、将 SMPNG 会址写作 Yahoo complex，本条按通行名称重写，细节以当期录音与 SMPNG 设计文档复核为准。（BSDTalk EP55，[558.88-625.44]，L1）
- Lehey 的职业生涯呈连续跨界：1982 年起在 Tandem 十年，从专有操作系统转到 UNIX；1992 年认定大公司不知去向而转做顾问，由此获得写书时间；1999 年底经 Dan Shearer 召集加入 LinuxCare 澳洲分部任“BSD 专员”，但公司不知如何使用 BSD，他自述大半年未做实际工作；.com 泡沫破灭后澳洲分部关闭，多数同事转往 IBM 从事 Linux，他因居家办公方式不合 IBM 文化而离开，此后在阿德莱德一家存储系统公司任职（因保密协议不能详述），约 2005 年转投 MySQL。（BSDTalk EP55，[78.96-660.16]，L1）
- 在 MySQL 任在线备份方向高级软件工程师，重点工作之一是确保 MySQL 在 FreeBSD 上良好运行，同时也是 NetBSD 开发者；其自述旨趣是防止 BSD 碎片化、推广所有 BSD 项目，认为 2006 年碎片化正在改善——跨项目沟通增多、个人恩怨减少；其经手的大型 FreeBSD 安装上存在仅在线上复现的竞态类崩溃（MySQL bug 12187，追踪逾半年、无法在测试环境重现），公开向听众征集相似案例。（BSDTalk EP55，[683.4-876.16]，L1）
- 著述经历：O‘Reilly 的 Porting UNIX Software 于 1995 年底出版（Tim O’Reilly 曾断言此类书只有两年好卖）；The Complete FreeBSD 起于与 Jack Velte 等 FreeBSD 人士在德国书展的会面，原约化为 50 页安装手册、成书 200 页，历经五版并相当成功；因无暇更新，他选择将全书放入公有领域而非任其消亡，并希望组建团队维护。（BSDTalk EP55，[222.32-331.0]，L1）

**史料**：

- FreshPorts 项目迁移经历为 Dan Langille 本人一手自述，涉及 New Jersey、Austin 与 AWS 三代主机及 jail 拆分。（BSD Now EP499，[2093.20-2320.00]，L1）
- BSDCan 会议组织史为 Dan Langille 本人一手自述，涉及 2004 年首届 BC camp 与 2023 年第二十届办会。（BSD Now EP499，[1442.02-2093.20]，L1）
- Syncoid 与 ZFS 快照在 jail 迁移中的应用，为 Dan Langille 本人一手实践叙述。（BSD Now EP499，[911.54-1104.46]，L1）
- WWIT Pro 的 Unix 哲学报告，作者在 SPARCBook 上用 PostScript 演示。（BSD Now EP312，[80.64-91.24]，L2）
- UWM HPC 实验室的为何使用包管理器文章，含 pkgsrc 增长图与自建二进制包的说明。（BSD Now EP312，[603.28-998.46]，L2）
- Joshua Stein 的 OpenBSD 触控板中断调试长文，含 ACPI AML、ACPICA 与 IOAPIC 细节。（BSD Now EP312，[1061.82-1661.96]，L2）
- 受访者提及 EuroBSDCon 2015 在斯德哥尔摩举办、开发者峰会曾借其旧办公室进行，以及 FreeBSD 季度状态报告将恢复发布图形栈条目。（BSD Now EP283，[354.72-2111.10]，L1）[订正：原 [354.72-379.54]，2026-09-30 SenseAudio 重转核对]
- 提及图形栈相关代码与仓库：libinput、Mesa 的上游同步、Linux KPI 移植以及待推送至 FreeBSD ports 的 X server 端口。（BSD Now EP283，[600.70-674.48]，L1）
- backtrace.io 的编译器可调试性文章，以 DWARF 状态机解释优化后变量的取值恢复。（BSD Now EP223，[72.32-97.84]，L2）
- Andrew Cherkashin 的 Rust 移植 Medium 文章（以 fd 工具为例说明 port 的 Makefile 结构）。（BSD Now EP223，[923.72-1010.84]，L2）
- FreeBSD 基金会 2017 年 11 月开发项目更新，含 RAID-Z 扩容、Broadcom Wi-Fi、ARM bhyve 与 LLD。（BSD Now EP223，[5033.72-5513.96]，L2）
- 该期含多条早期 BSD 一手线索：在德国以 1,000 美元购得 BSD Unix 源码使用权（对比此前 System V 单份授权高达 5 万美元），由此接触 BSDi 的 BSD/386 并长期使用；Jordan Hubbard 曾寄来 FreeBSD 0.9 磁带，其评价为“几乎与 BSD/386 一样好”；1996-1998 年间因 BSDI 更新不断涨价而逐步转向 FreeBSD；为 Novell System V/Unixware 移植约 150 个自由软件并制成 CD，他称之为 ports 集合的前身。 [考据脚注] 转写将 Jack Velte 误作 Veltie/Volte、将 LinuxCare 误作 Limitscare，人名与公司名已按通行拼写重写。（BSDTalk EP55，[122.92-227.32]，L1）

**史观**：

- 总纲10 动手者创造历史：个人长期维护公共服务并组织社区会议，构成 BSD 生态的隐性基础设施。：Dan Langille 长期独自维护 FreshPorts 与组织 BSDCan，是默默做事的动手者。（BSD Now EP499，[2093.20-2320.00]，L1）
- 总纲9 经验优先：以实际部署需要为准绳选择 jail 管理方式，而非盲从现成管理器。：其 jails 实践由具体场景推动，弃用管理器回归脚本，显示经验优先于既有工具的教条。（BSD Now EP499，[1666.86-1734.30]，L1）
- 总纲4 分离聚合是永恒规律：服务组件在单主机聚合与多 jail 分离之间重组，架构随需求循环演进。：FreshPorts 由单主机聚合拆分为多 jail 分离，服务架构在分离聚合中演化。（BSD Now EP499，[2093.20-2320.00]，L1）
- 总纲9 经验优先：包管理器文章以 1999 年以来的科研支持经验论证重复手工编译的浪费，强调实践优先。（BSD Now EP312，[639.56-702.0]，L2）
- 总纲10 动手者创造历史：OpenBSD 触控板驱动由 Joshua Stein 持续两年动手调试修复，而非依赖硬件厂商。（BSD Now EP312，[1061.82-1661.96]，L2）
- 总纲22 知识注定过时：Unix 哲学需随开源协作与 2019 语境修订，旧原则因环境变化而更新。（BSD Now EP312，[480.36-497.04]，L2）
- 总纲10 动手者创造历史：图形栈这一基础设施长期由少数动手者维持，其工作依赖社区测试反馈与硬件样本的缓慢积累，属于被主流叙事边缘化的劳动。（BSD Now EP283，[690.18-747.68]，L1）
- 总纲15 文化即形式主义：用户组、会议、教程与雇主赞助共同构成社区再生产的社会形式；受访者特别指出参加一次会议即可让人意识到自己的工作被他人实际使用。（BSD Now EP283，[386.88-424.68]，L1）
- 总纲10 动手者创造历史：ports 生态以“志愿者为主、任何人均可提交 port”的机制让无数贡献者入门，节目强调 25 人以上因写 port 进入 FreeBSD。（BSD Now EP223，[1699.6-1719.64]，L2）
- 总纲5 没有必然性，只有偶然性：对 Docker 的辨析指出便利性常战胜效率，技术采纳受偶然性与习惯支配而非纯理性。（BSD Now EP223，[3344.12-3346.44]，L2）
- 总纲4 分离聚合是永恒规律：FreeBSD 的创立是 386BSD 社区在 patch kit 难以为继时的一次分离，而非预先规划的必然结果。（BSD Now EP13，[1042.0-1148.2]，L1）
- 总纲13 法律与道德是利益分配：Hubbard 称 BSD 许可证只有两句话且逐年变短，开发者以代码被使用的广度而非金钱衡量成就，体现与 GPL 扩张相反的法律简省取向。（BSD Now EP13，[2209.6-2362.5]，L1）
- 总纲10 动手者创造历史：Vinum 的成史显示关键存储技术并非源自宏观规划，而是动手者对具体故障求助的回应：一通来自加州的磁盘崩溃求助电话加上企业对 RAID5 的临时出资，才使卷管理器进入 FreeBSD 源码树。（BSDTalk EP55，[397.8-462.52]，L1）

**辨析**：

- FreshPorts 约二十年历史的起止年份与三代主机迁移时间线为当事人回忆，具体年份需以项目档案与邮件列表核验。 [存疑脚注] 项目起止与迁移年份为口述概数，需以 FreshPorts 档案或公告交叉验证。（BSD Now EP499，[2093.20-2320.00]，L4）
- BSDCan 自 2004 年起连续办会二十年的说法为口述概数，需以会议档案确认是否存在中断或纯线上年份。 [存疑脚注] 办会连续年数为口述表述，需以会议历年记录核验是否含线上或中断年份。（BSD Now EP499，[1442.02-2093.20]，L4）
- [存疑脚注] 转写中讲座作者姓名与报告出处存在拼写噪音，且观点为节目转述，未与 WWIT Pro 原报告逐条核对。 [存疑脚注] 报告出处与人名未经原报告核对（BSD Now EP312，[68.72-74.16]，L4）
- 转写将受访者姓名记为 Niklas Seising 与 Nicholas Seizing 两种拼法，且分段时间戳明显乱序；依据上下文应为 FreeBSD 图形团队成员 Niclas Zeising，但本卡片保留转写原拼写。 [存疑脚注] 受访者姓名拼写未经一手核对，且该期转写质量较差、时间戳乱序。（BSD Now EP283，[52.96-57.04]，L4）
- 受访者关于图形栈“基本可用”的自我评估带有当事人立场，且其承认与 Windows、macOS 存在差距、挂起与交换分区交互存在偶发冻结，须与版本发布记录与社区测试报告交叉验证。 [存疑脚注] 具体故障复现与修复状态未能从本期转写确认。（BSD Now EP283，[451.52-557.74]，L3）
- 编译器的可调试性结论基于特定版本（GCC 5.2、Clang 3.6 等）的示例，随版本演进可能改变，且文章作者所属公司售卖崩溃报告产品，存在利益关联。 [存疑脚注] 结论依赖具体编译器版本且作者存在商业利益关联（BSD Now EP223，[803.04-822.92]，L4）
- 本卡片所据转写文本实际存放于 663.txt（其内部标为第 13 期），而 664.txt 为第 12 期内容之重复，转写文件与期号存在错位。 [存疑脚注] 转写文件错位：664.txt 实为第 12 期，第 13 期内容见于 663.txt。（BSD Now EP13，[57.6-66.7]，L4）

**文献**：

- [BSD Now EP499] Pennington J. BSD Now: 499: Dan Langille Interview[EB/OL]. (2023-03-23)[2026-08-15]. <https://www.bsdnow.tv/499>.
- [BSD Now EP312] Pennington J. BSD Now: 312: Why Package Managers[EB/OL]. (2019-08-22)[2026-08-15]. <https://www.bsdnow.tv/312>.
- [BSD Now EP283] Pennington J. BSD Now: 283: Graphical Interface-View[EB/OL]. (2019-01-31)[2026-08-15]. <https://www.bsdnow.tv/283>.
- [BSD Now EP223] Pennington J. BSD Now: 223: Compile once, debug twice[EB/OL]. (2017-12-06)[2026-08-15]. <https://www.bsdnow.tv/223>.
- [BSD Now EP13] Pennington J. BSD Now: 13: Bridging the Gap[EB/OL]. (2013-11-27)[2026-08-15]. <https://www.bsdnow.tv/13>.
- [BSDTalk EP55] Backman W. BSDTalk: 55: bsdtalk055 - Interview with Greg Lehey[EB/OL]. (2006-07-18)[2026-08-27]. <https://archive.org/details/bsdtalk055>.

<!-- /PODCAST_REVIEW -->

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-221 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-221`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者口述：Bitrig 在 2014 年发布了 1.0 版本。（YouTube EP0wy8ZLDtyLE，[259.299-262.5]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-765 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-765`；w172 YouTube 章节路由采纳）

据来源不详讲者口述：Baptiste Daroussin 说明 FreeBSD 移植树已同时认识 ARMv6 与 MIPS64 架构，为跨平台构建 ports tree 提供架构层起点。（YouTube EPMt_EYfIHx9M，[67.56-75.51]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-741 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-741`；w172 YouTube 章节路由采纳）

据〔Installing a Port on FreeBSD 教程（来源不详）〕讲者口述：ports 集合取自 get.freebsd.org 的 ports.git 仓库（转写音作 ports.get）。（YouTube EPlywkQkTXMEY，[77.42-86.69]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-2511 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2511`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔EuroBSDCon（场合见正文开场介绍）〕讲者口述：约二十年前 OpenBSD 的这部分——ports／打包体系——一切承自 FreeBSD。（YouTube EPaw2Gezj-Nkw，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2512 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2512`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔EuroBSDCon（正文开场语所示）〕讲者口述：最早一代 packing-list 生成工具不过一百五十来行 Perl，做法是扫描本地文件系统、找出哪些文件是新装出来的，据此生成 packing list。（YouTube EPaw2Gezj-Nkw，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2513 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2513`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔EuroBSDCon（正文开场语所示）〕讲者口述：他们把打包改为 staged install——先把内容装进系统上一个与运行系统无关的暂存位置，再从那里制作包；当时他们叫它 fake，讲者说或许 stage 才是更好的名字，但因为是 OpenBSD 最先做的，所以由他们定了这个名字。（YouTube EPaw2Gezj-Nkw，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2514 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2514`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔EuroBSDCon（正文开场语所示）〕讲者口述：他决定最终替换承自 FreeBSD 的旧包工具，主要是出于安全原因——让本应保证安全的操作去处理大量字符串近乎疯狂。（YouTube EPaw2Gezj-Nkw，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
