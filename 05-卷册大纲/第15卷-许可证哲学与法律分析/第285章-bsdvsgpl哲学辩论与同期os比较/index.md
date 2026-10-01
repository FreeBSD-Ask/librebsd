---
chapter: 第 285 章
id: CH285
volume: 第15卷-许可证哲学与法律分析
---

# 第 285 章 bsdvsgpl哲学辩论与同期os比较

## 要点

- 许可哲学光谱：“义务自由（GPL）←→ 信任自由（BSD/宽松）←→ 闭源保护（Windows）”；BSD vs GPL 辩论的本质是“自由如何保障”的分歧，BSD 以信任、GPL 以约束，二者共同定义开源运动的哲学边界。
- Committer’s Big List of Rules 的沉默反映分层设计——治理程序处理“谁有权提交”，许可证哲学通过社区讨论与工程实践处理“提交什么”。BSD 化工程未通过修订 committer 规则实现，而是通过构建 BSD 许可证替代品逐步完成，证明规则的程序中立未阻碍许可证纯化，反而为工程替代争取了时间——若规则在早期即被修订，BSD 化进程或更早启动，但也可能因规则争议而扩大社区分裂〔截断据 285.11/285.12 论旨补全〕强制禁绝 GPL 代码，FreeBSD 将因缺乏可用编译器而无法
- Committer’s Big List of Rules 争议映射出革命与改革的方法论分歧。革命路径主张直接修订规则——禁止 GPL 代码进入 base 系统、强制许可证审查、将 BSD 化写入治理章程；改革路径则在不修订规则的前提下，通过工程替代（Clang、LibreSSL、mandoc）逐步实现许可证纯化。FreeBSD 选择的是改革路径——改革虽难而可行，且不以社区分裂为代价〔截断据子节论旨补全〕了改革路径，其困难远高于革命——须先构建功能对等的 BSD 替代
- 中文技术圈普遍以“病毒/传染”描述 GPL copyleft 机制，此隐喻**在法律意义上具有系统性误导**。词源可考：1990 年即出现 “General Public Virus”（GPV）贬称；2001 年 Microsoft 高管 Craig Mundie 称 GPL “viral aspect”，Steve Ballmer 2001 年称 Linux 为 “a cancer that attaches itself, in an intellectual property sense, to everything it touches”——“传染”隐喻由此进入大众话语，但该比喻在版权法上并不成立〔截断据 Ballmer 2001 Chicago Sun-Times 采访通行引文补全；后文见要点下条〕更称 GPL 代码是 "a cancer that attach
- GPL 义务的触发条件是**分发（distribute，GPLv2）/传播（convey，GPLv3）**，而非“使用”或“修改”。中文圈“只要用了 GPL 代码就必须开源”的表述是核心误读之一。FSF GPL FAQ 明确：①**内部使用修改版不触发开源义务**——“GPL 不要求你发布修改版……你有自由修改并自用，而不必发布。这个规则也适用于机构（包括公司）”；②**分发/传播方触发义务**——GPLv2 以“分发”、GPLv3 以“传播”（convey）为触发点，SaaS 内部服务在 GPLv2 下不触发（AGPL 另计）〔原句尾部截断，据 FSF GPL FAQ 论旨补全〕

## 史料

- [DB:bsdnow_podcast:outline_mappings:om_10483] BSD Now 第 665 期，匹配 CH285 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10547] BSD Now 第 654 期，匹配 CH285 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10584] BSD Now 第 646 期，匹配 CH285 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10645] BSD Now 第 637 期，匹配 CH285 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10778] BSD Now 第 617 期，匹配 CH285 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11152] BSD Now 第 571 期，匹配 CH285 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11215] BSD Now 第 563 期，匹配 CH285 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11366] BSD Now 第 546 期，匹配 CH285 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11444] BSD Now 第 536 期，匹配 CH285 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11544] BSD Now 第 526 期，匹配 CH285 章，关联度 1.0

## 史观

- 章级史观（依 285.10-285.13 子节史观字段汇总）：BSD 与 GPL 的辩论是两种自由观——信任自由与义务自由——的长期共存而非胜负关系（总纲4 分离聚合是永恒规律）；Committer's Big List of Rules 的沉默与工程替代路径印证革命与改革的方法论分歧——BSD 靠改革、Linux 靠革命（总纲21 革命与改革是历史方法论的分歧）；“病毒/传染”隐喻在中文圈的流行是话语权力对许可证法律事实的形式主义重构（总纲15 文化即形式主义）；各法域判例（Jacobsen、最高法 51 号、南京、广州）显示许可证义务的利益分配本质（总纲13 法律与道德是利益分配）。

## 辨析

- 辩论无终局——两种自由观各服务不同目标，BSD 的务实人文在光谱中独特定位。
- 【查证来源】FreeBSD Committer’s Guide 第 20 章经 docs.freebsd.org/en/articles/committers-guide/#rules WebFetch 一手核验目录条目存在；FreeBSD Core Bylaws 2000.8.28 版经 freebsd.org/internal/bylaws/ 一手核验〔后文截断，查证链路待回源补全〕ylaws/ WebFetch 一手核验，规定 active c
- 【查证来源】项目史观总纲第 21 条原文经 据原文第 25 章 第 25 行 Read 一手核验：“革命与改革是历史方法论的分歧。Linux 靠革命，BSD 靠改革。改革的困难远高于革命。破山中贼易，破心中贼难”；BSD 化工程时间线经 135.8 节史料（OpenBSD LibreSSL 公告、FreeBSD LLVM 迁移文档、openbsd.com/papers/ 等一手来源交叉核验〔后文截断待回源〕penbsd.duckdb L3.6.1 查询报告）交叉核验；FreeB
- 【查证来源】GPLv2 §5 原文：“如果可识别的作品部分不是派生自本程序，且可合理视为独立的分离作品，则本许可证及其条款不适用于那些部分”（WebFetch gnu.org/licenses/gpl-3.0.txt 一手核验〔后文截断待回源〕g/licenses/old-licenses/gpl-2.0.txt 一手核验）；GPLv3 §5 聚合定义“aggregate”（WebFetch gnu.org/licenses/gpl-3.0.txt 一手核验〔后文截断待回源〕g/licenses/gpl-3.0.txt 一手核验）；Sta
- 【查证来源】FSF GPL FAQ 中文版（gnu.org/licenses/old-licenses/gpl-2.0-faq.zh-cn.html）WebFetch 一手核验上述问答原文；GPLv3 §0 “传播”（to convey）定义（gnu.org/licenses/gpl-3.0.txt）一手核验。【交叉验证方法】（1）GPL 条款比对（2）commit log 时间线（3）官方 FAQ 原文〔后文截断待回源补全〕FSF FAQ 内部一致性核验：修改版自用问答与 SaaS 问答

## 文献

- McKusick M K, Neville-Neil G. The Design and Implementation of the FreeBSD Operating System [M]. 2nd ed. Addison-Wesley, 2015. ［B］
- Committer’s Big List of Rules（docs.freebsd.org/en/articles/committers-guide/#rules）；FreeBSD Core Bylaws 2000.8.28 版（freebsd.org/internal/bylaws/）；BSD 化 commit log；Core Team 选举记录（freebsd.org/administration/）［A］
- 项目史观总纲第 21 条（据原文第 25 章 第 25 行）；BSD 化工程时间线（详见 135.8 节）；FreeBSD Core Bylaws 2000.8.28 版第 9 条（freebsd.org/internal/bylaws/）［A］
- GPLv2/GPLv3 全文（gnu.org）；FSF GPL FAQ（gnu.org/licenses/gpl-faq.html）；中文自媒体《开源许可证教程》（ref 2377，kaoju_unreliable 系列，被考据对象——仅作“个人观点”元引用，其史实断言须独立核验）
- FSF GPL FAQ 中文版；GPLv2/GPLv3 全文；AGPL 文本［A］
- GPLv2/GPLv3 全文；FSF GPL FAQ；最高法（2021）最高法知民终51号判决；HBuilder 案判决；康达律师事务所开源协议分析文 ［A］
- Jacobsen v. Katzer（535 F.3d 1373, Fed. Cir. 2008）；Creative Commons 声明；Artifex v. Hancom（2017）；济宁网络科技案；广州知识产权法院典型案例；最高法（2021）最高法知民终51号 ［A］
- 南京中院（2021）苏01民初3229号；FSF v. Cisco 记录；广州知识产权法院典型案例；济宁网络科技案（2021）；中文自媒体《开源许可证教程》（ref 2377，kaoju_unreliable 系列，被考据对象——其“GPL 病毒”与“法官只会判停止使用”断言已按判例逐条纠正，结论以 FSF 官方 + 判例原文为准）［A］

〔订正注：原九列破损对照表与判例附录系 284.13 旧章号碎片胶合，与 285.13 行 85 同表重复，已整块删除；正表见 285.13〕


<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP335、BSD Now EP74、BSD Now EP27、BSDTalk EP7、BSDTalk EP123、BSDTalk EP9、BSDTalk EP161、BSDTalk EP166、BSDTalk EP183（共 9 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Deb Goodkin 与 FreeBSD Foundation 在 Linux Conf AU 内组织首个 FreeBSD mini-conf，Ben Woods、Peter Grehan 等演讲者出席。（BSD Now EP335，[1272.54-1399.32]，L2）
- Hyperbola 联合创始人 Andre 解释弃 Linux 内核的原因：HDCP 等 DRM、GRSecurity 停止公开补丁、Rust 商标限制，并计划 fork OpenBSD 内核。（BSD Now EP335，[419.28-605.24]，L2）
- JT 对‘从 Linux 迁移到 BSD’一文四个论点逐条反驳：Linux 碎片化被高估、商业介入非坏事、社区优劣是比例问题、许可证争论难有定论。（BSD Now EP335，[1941.52-2505.94]，L2）
- Tanenbaum 回溯 MINIX 起源：阿姆斯特丹自由大学是荷兰第二个使用 Version 6 Unix 的站点，AT&T 律师因 Lions 讲义流传而认定学生广泛研习其产品不可容忍，遂在 Version 7 许可证写入“不得在课堂讲授 Unix、不得出书”（1332.74-1338.48）类条款，大学教学被迫中断；他由此决意以自有代码重写一个不受 AT&T 许可证约束的 Unix 克隆，MINIX 因教学之需而生，初始目标即保持代码简单直白以适配操作系统课堂，而非追逐功能齐备。（BSD Now EP74，[1288.40-1367.16]，L1）
- 因社区长期苦于应用软件匮乏、无包可用而致用户流失，MINIX 数年前决意整体引入 NetBSD 的库、头文件与包管理基础设施，访谈时已有约 4000 个包可运行，X11 适配修复后预计再增约 3000 个；在诸 BSD 中选中 NetBSD，一因其许可证与 MINIX 兼容，二因其可移植性纪律杜绝硬件专属技巧，与 MINIX 面向 BeagleBoard 系列等嵌入式高可用场景的方向契合。（BSD Now EP74，[1592.86-1669.48]，L1）
- Tanenbaum 阐明 MINIX 3 的安全设计：文件系统、VFS、内存管理等以独立进程存在并由 MMU 硬件隔离，各进程仅能按微内核中的授权表发起内核调用，故攻陷音频驱动者尝试创建进程只会得到无权限错误（1886.76-1896.74），缺陷被天然限制在单个服务内；计划于 3.3.1 落地的 live update 可在系统运行中以约 200 毫秒热替换组件，持续变更内存布局与代码数据结构，使依赖精确布局知识的 return-to-libc 类攻击难以命中，将高可用机制转化为安全机制。（BSD Now EP74，[1854.20-2022.84]，L1）
- Will Backman作为早期BSD播客BSDTalk的主持人，在访谈中表示BSD Now等新音频资源分担了BSD社区的声音传播压力，使更多人以音频形式接触BSD。（BSD Now EP27，[3735.70-3797.78]，L1）
- Backman认为GPL3的转向曾让包括Apple在内的公司产生顾虑，而BSD许可虽早已存在，却在人们观念中重新浮现，Android等平台内核之上亦采用BSD式许可。（BSD Now EP27，[3572.44-3610.86]，L1）
- 访谈双方以ZFS进入FreeBSD安装器、bhyve即将可用等标志，表达2014年前后BSD社区从追赶Linux转向出现自身新特性的感知。（BSD Now EP27，[3613.56-3645.20]，L1）
- Alan Jude与TJ曾邀请Will Backman共同主持BSD Now，因其无法投入固定时间而未成行，这段口述记录了BSD Now节目创建初期的主持人选过程。（BSD Now EP27，[3835.86-3858.86]，L1）
- 当期教程展示NetBSD可通过build.sh在几乎任何支持编译器的系统上交叉编译，且可用非root用户完成构建，适合在快速服务器上为嵌入式平台生成系统与ISO镜像。（BSD Now EP27，[3927.86-4385.62]，L2）
- DragonFly BSD 1.4 于 2006 年 1 月 7 日发布；主持人补记此前遗漏，并说明该项目由一群围绕 FreeBSD 5 系内核希望作出重大改动的人分叉而来，旨在验证其在多处理性能上的理论，若理论成立则成果可惠及全部 BSD。（BSDTalk EP7，[20.38-79.16]，L2）
- GPL 正酝酿第三版：Richard Stallman 主导的修订拟纳入争议性反 DRM 条款，即 GPLv3 软件不得被改造用于对不自愿用户强制数字版权管理（如 TiVo 式设备限制用户复制与媒介转移的合理使用）。因 BSD 生态大量依赖 GNU 工具、尤其 GCC 编译器（Apple 亦曾长期为 PowerPC 改进 GCC），主持人推演其后果：并非所有软件都会升级到 v3，若 GCC 随 v3 发布可能出现以 v2 末版为基的分叉编译器，商业公司转向 Intel 平台后也可能改用 Intel 编译器；而 BSD 许可证仅有数行、几乎无限制（只要求署名与免于诉讼），GPLv3 的争议或促使商业公司重新审视 BSD 许可证与 BSD 系统，成为 BSD 的转折点。（BSDTalk EP7，[84.90-361.82]，L2）
- 主持人选取五款 BSD live CD 实测：FreeSBIE（FreeBSD 基）、Anonymous（OpenBSD 基）、DragonFly 安装盘（自述兼作 live CD 但极简）、NetBSD 官方 live CD（定位救援盘兼 KDE 桌面）、Newbee（NetBSD 基，主打全功能图形桌面）；测试硬件为 233 MHz/128 MB 旧笔记本、自制 AMD 2600 台式机、仅 USB 外设的 Dell GX280 与新款 Centrino 笔记本 Dell Latitude D610。（BSDTalk EP7，[376.02-517.04]，L1）
- 实测结果：除 Dell GX280 上 NetBSD live CD 不识别 USB 键盘致无法继续外，其余组合均可启动联网；DragonFly 盘仅文本模式、实用价值低但足以验证硬件支持；NetBSD 盘因缺 libqt 而无法启动 KDE，但 X 与轻量窗口管理器可用；Newbee 启动 Fluxbox 或 Blackbox 并预装浏览器邮件聊天工具；FreeSBIE 允许启动时选择轻量或重量级图形界面，基于 FreeBSD 5.3（2004 年 11 月发布，tagger_date 2004-11-04、公告日 11-06），虽技术偏旧仍被主持人评为最佳 BSD live CD 桌面。横向对照：BSD live CD 资源占用普遍不高，但与 Linux 系 live CD 参照物（转写作 Canopix）相比浏览器启动明显偏慢，当事人将差距归因于后者更成熟、优化投入更多。（BSDTalk EP7，[549.84-843.56]，L1）
- whurley 自述其受聘背景：此前在一家集群系统公司主导开源系统管理项目 OpenQRM，自称该项目为当时最成功的开源系统管理项目；又与他人共同创建 Open Management Consortium，推动各开源系统管理项目按用户需求协作而非以小团队对抗大厂商，统一代理模型等议题对 HP、IBM、CA 与 Nagios、Hyperic 等公司同等开放。BMC 管理层以此前工作为据，于 2007 年中聘其为开源战略首席架构师，要求他把开源做进商业模式而非营销点缀。（BSDTalk EP123，[220.66-308.98]，L1）
- BMC Developer Network 于本期采访当周（2007 年 7 月底）公布，定位为超越单纯发布压缩包（tarball）的用户沟通层：当周发布的集成产品均由用户参与完成；站内集成面向合作伙伴、用户与工程团队的跨越层（spanning layer），设有投票与直接反馈渠道，收录 Talk BMC 的博客与播客、下载区、集成引擎与权威软件库，并提供白皮书、文档与 API 技术资料。上线时未设公共源码仓库（无 Subversion 服务），代码完全自由下载，用户可提交修改；whurley 称社区尚未强烈要求设立仓库，是否自建仓库将由社区需求决定。（BSDTalk EP123，[453.3-826.3]，L1） [订正：原 首批四个集成项目与五个资源中心（Atrium、Foundation 等）细节及 [471.80-797.04]，2026-09-29 SenseAudio 重转核对]
- 关于 BMC 内部开源文化，whurley 评估称开发者的心态转变并非障碍：开发者如撰写 Adventures in Linux 博客的 Steve Carl 长期参与开源项目，公司历史上亦曾发布 CMFS、SQ log MD、MidWatch 等开源软件而不事声张；真正的挑战在于把这些既有贡献向外部社区公示并积累可信度。他援引 Karl Fogel 所著《Producing Open Source Software》中开放会引来公开批评的论述，并以自己在前雇主开放旧有专有代码时资深开发者被年轻学生公开指摘的经历，说明企业开源须正视此类社会性摩擦。（BSDTalk EP123，[884.04-1122.86]，L1） [订正：原 CMSFS、logMV，2026-09-29 SenseAudio 重转核对]
- Webmin 起源于作者任系统管理员时解决自身痛点的受限 Web 界面：为让非管理员安全变更 DNS 记录、避免手改配置文件破坏服务而写，随后逐步扩展出用户与组、Samba、Apache、NFS 导出等模块，长成覆盖多数类 UNIX 系统的管理框架。项目赞助历经多家公司：Caldera 于 2000 年赞助约一年，此后有 MSC Software，访谈时由 OpenCountry 赞助，但作者强调项目始终是自由软件、未被任何公司接管。（BSDTalk EP9，[277.26-383.38]，L1）
- 跨平台支持是 Webmin 的立项目标也是最重负担：各 UNIX 的基本概念（用户、组、文件）一致，但 NFS、cron 等服务的配置方式差异大，Apache 等常见软件在不同发行版中安装位置各异，Webmin 必须逐一掌握安装路径与版本。当事人的分化判断是：UNIX 家族之间未见进一步分化或收敛、大体稳定，而 Linux 发行版数量爆炸且各自发明打包方法与配置文件布局，未测试的发行版上不能贸然安装；支持最好的平台为 Red Hat/Fedora、Debian、Solaris、FreeBSD，即作者本人常用的系统，其中他偏好 Debian 的 apt 包管理之无痛安装，Red Hat/Fedora 的优势则在第三方商业软件商支持。（BSDTalk EP9，[392.60-560.38]，L1）
- 当事人解释弃 GPL 取 BSD 许可证的理由：GPL 虽好，但其源码共享义务限制了将 Webmin 改造进商业产品或设备（appliance）的用途；BSD 许可证允许任何人以任意方式使用与改造，在其看来才是真正的更自由。（BSDTalk EP9，[560.38-620.12]，L1）
- 衍生项目 Virtualmin 是 Webmin 的虚拟主机模块，对标 cPanel 与 Plesk，用于单机托管多虚拟网站、邮件域、DNS 域与 FTP；采用双版本策略：GPL 许可的免费版与功能增强的商业版并行，呈现了开源基础加商业增值的典型商业模式。（BSDTalk EP9，[775.82-811.34]，L1）
- NYCBSDCon 2008 周日现场：因周六日程延误，组织方压缩午休以追赶进度；OpenBSD 摊位预售 11 月 1 日正式发布的 4.4 版 CD 与 T 恤，旧 T 恤以十美元折扣出售，摊位负责人 Austin Hook 自述 T 恤与 CD 销售构成 OpenBSD 项目的重要资金来源；现场有五六位以上 OpenBSD 开发者，Joshua Stein 与 Sun 的 David Lawler 等亦在场；PC-BSD 主题的 BoF 场由 Chris Morris 主持，约八人参加、面向所有感兴趣者，话题涉及在虚拟机中运行等。（BSDTalk EP161，[242.42-358.05]，L1）
- DataPipe 的 Unix 部门受访者 Mark Satt 自述：该公司为托管主机与主机托管服务商，1998 年创立、约三百名员工，办公地点遍布硅谷、纽约、伦敦、香港与上海；自创立起即以 BSD 为公司操作系统，内部系统与大量客户系统均运行 BSD，纽约周边客户全部为 BSD 客户，服务涵盖 VPN、防火墙、入侵检测与应用管理；此次为其首次赞助 BSD 会议，动机即纽约地区客户群的实际使用。（BSDTalk EP161，[120.58-218.42]，L1）
- Theo Schlossnagle 的 Reconnoiter 网络监控系统演讲综述：定位与 Zenoss、Nagios 类似但设计思路迥异，面向数千台机器规模的监控问题，彼时尚处 alpha 阶段；其 web 界面绘图表现出色，并提供类似 Cisco 命令行界面的管理接口，明确以系统管理员的可用性为设计目标；主持人判断其值得跟踪但尚不宜投入生产。（BSDTalk EP161，[581.85-667.38]，L2）
- Pavel 的 ZFS 演讲及其维护者瓶颈自述：演讲分两场合一，前半以作者自绘卡通动画轻松介绍 ZFS 的文件系统特性与 UFS 等早期文件系统的局限，后半面向开发者展开实现组件的技术讨论、无现场建池演示；他自述自己是 FreeBSD 上极少数从事 ZFS 的开发者之一，人手瓶颈使其不愿宣称生产可用——用户规模一旦扩大，问题报告将超出其个人处理能力，故呼吁更多开发者参与分担；Matthew Dillon 在场，会后两人就 ZFS 与 HAMMER 两个文件系统的设计交谈，主持人评论这种平日仅靠邮件列表往来的跨项目开发者面对面交流正是此类会议的核心价值。（BSDTalk EP161，[660.38-783.58]，L1）
- Kurt Miller 的 OpenBSD PIE 演讲综述：位置无关可执行文件技术旨在使应用对特定类型的缓冲区溢出攻击更具抵抗力，项目拟在性能与其他副作用可接受的前提下将其加入默认构建，作为纵深防御的又一层次。（BSDTalk EP161，[784.70-825.02]，L2）
- 周六技术讲座的转述综述：Adrian Chadd 讲 FreeBSD 高吞吐并发磁盘 IO，议题源于 squid 的经验教训并含 squid 与 varnish 的对比及 POSIX 同步异步 IO 概述与规模扩展性讨论；Jason Wright 讲硬件出错时，揭示硬件缺陷之普遍、以幽默幻灯呈现；Matthew Dillon 讲 HAMMER 文件系统，技术性强、面向开发者；Anders 讲 PCC 复兴进展并公开寻求资助以投入更多时间，PCC 尚需证明可用性与速度；另一场报告指出只要目标 CPU 有文档，PCC 移植到新架构约一周即可完成。（BSDTalk EP161，[825.02-1018.66]，L2）
- 周六另外两场讲座的转述综述：Julio 讲 ATF 自动化测试框架——虽列于 NetBSD 名下但强调其通用定位、无开发工具依赖，源自 Summer of Code 项目，NetBSD 拟借其统一基系统中现有测试，易用且自动化的框架比完善却需手动使用的框架更具实效，跨平台可移植性有望吸引更多开发者；Jeremy Reed 讲 DNSSec——在近月 DNS 欺骗事件频发、DNS 协议事务 ID 与源端口随机化薄弱的背景下，演示以 ISC BIND 实施 DNSSEC 签名的步骤，并寄望大型 ISP 在上游部署以防缓存投毒。（BSDTalk EP161，[1018.66-1152.98]，L2）
- Jason Dixon 的 BSD versus GPL 演讲综述：延续其此前 BSD is dying 演讲的轻松幽默风格，以笑话包裹许可证议题——讨论人们对各许可证自由程度的假设与哪种更自由的持久争论，并强调正试探涉足开源的企业有必要了解各许可证在可为与不可为、担保与自由保障上的差异。（BSDTalk EP161，[1152.98-1223.62]，L2）
- Asterisk 的架构由当事人澄清为两个分离的包：Asterisk 本体是呼叫控制与脚本系统，在 BSD 上运行良好——他在访谈中即经由两个 OpenBSD 系统通话；而 Zaptel（后更名为 DAHDI）电话卡内核驱动更为挑剔，旧版仅有 FreeBSD 与 OpenBSD 移植（由 handle 为 Gonzo 的贡献者等人完成），FreeBSD 的 package 版本偏旧。Digium 与开源开发者近月正推动把单体化的 Zaptel 组件拆分以降低耦合，目标使 Solaris 与 BSD 的移植更容易；BSD 社区对开发列表上报的兼容性问题通常能在 24 至 48 小时内修复。（BSDTalk EP166，[205.56-360.16]，L1）
- Digium 的商业模式建立在 GPL with exception 授权之上：代码以 GPL 发布，但回馈补丁的编码者须声明权利并允许 Digium 在极有限情形下于 GPL 之外商业授权，这一例外授权收入是 Digium 生存并持续向开源项目投入的基础。此外 Zaptel 驱动的计时功能长期支撑会议桥、呼叫等待音乐与 IAX2 中继等特性，纯 IP 部署则完全无需内核模块。（BSDTalk EP166，[437.92-464.70]，L1）
- Digium 不为 Linux 之外的系统提供官方支持，当事人坦承这并非技术问题而是专业人力与市场结构问题：BSD 社区虽然根基深厚，但其用户多为清楚自身需求的资深系统管理员，问题习惯在社区内部解决，商业支持需求远少于 Linux；辅以 BSD 系统管理员难觅且价格偏高的劳动力市场现实，企业自然倾向 Linux。Digium 设有专门的 asterisk-bsd 邮件列表（lists.digium.com）维持问答。（BSDTalk EP166，[681.96-946.40]，L1）
- 当事人自述其平台选择史：远自查旧 SunOS 时代学习 Unix，经历 Sun 与 NeXT 的迁移，90 年代中期接触 OpenBSD 预发布版本；虽认为 FreeBSD 与 NetBSD 特性推进更快，仍选择 OpenBSD 作为全部生产系统的默认平台，理由是其默认安全使部署后无需熬夜担忧；其个人网络几乎全为 OpenBSD（4.2 与 4.4 并行渐进升级），Mac 仅作前端，Linux 只用于测试经由 AMI、AGI 接口触达 Asterisk 的无 BSD 移植的第三方组件。（BSDTalk EP166，[743.68-826.16]，L1）
- Asterisk 的 BSD 支持改善被当事人归因于 Apple 的间接效应：大量开发者以 BSD 系的 Mac 为前端，在终端直接编译，一旦代码在 Mac 上失效便群起抱怨，迫使修复级联惠及其他 BSD 版本。规模方面，他个人在 BSD 上测过数百通道；他引述的最重负载案例——十天处理八百万呼叫、于 SIP、IAX 与 SS7 间桥接且无崩溃——运行于 Linux 衍生系统；他不知晓大型企业级 BSD 部署，但认为 BSD 与 Linux 在稳定性与性能上不存在值得评论的显著差异。（BSDTalk EP166，[841.56-1084.84]，L1）
- 当事人在Tektronix Walker Road厂区亲历了企业环境向BSD的迁移：约1981年在VAX 11/780上以2.8BSD替换原主力系统RSTS/E，过渡数月间白天运行RSTS/E、夜间运行Unix并由其负责数据搬运；次年增购VAX后依次运行4.0BSD、4.1BSD直至4.3BSD，构成企业自RSTS/E转向BSD的一线口述。（BSDTalk EP183，[279.02-337.02]，L1）
- 其公司Stonehenge.com的主机曾运行Linux约六年，因管理员疏于跟进安全更新而遭rootkit入侵，商业机密暴露的风险促使其经AltaVista检索转向OpenBSD早期版本（2.7或2.8前后）；此后他自述对OpenBSD服务器建立“可离场一周不必逐日盯防安全公告”的信任，而对任何Linux发行版均无同等信心，显示安全事件是用户平台迁移的直接动因。（BSDTalk EP183，[350.62-436.46]，L1）
- 其Geek Cruises与InsightCruises网站于访谈前约三个月迁入Amazon EC2并以OpenSolaris运行：EC2发布初期仅支持Linux，当事人拒绝回归Linux，转以具BSD渊源且自认较Linux更安全的OpenSolaris替代；他转述EC2虚拟层为Xen衍生框架且做了本地改动，BSD若要获得支持须自最底层虚拟硬件向上打通——呈现2009年末BSD在公有云平台的缺席状态与技术门槛。（BSDTalk EP183，[447.14-607.3]，L1）[订正：原 [447.14-518.98]，2026-10-01 交叉核验订正]
- 当事人口头辨正SunOS与Solaris的谱系混淆：SunOS 4及更早版本为纯BSD系（SunOS 4实即Solaris 1），SunOS 5改宗System V并对应Solaris 2；SunOS始终是内核操作系统之名，Solaris始终是发行版之名，版本号交叠系厂商命名所致，为商业UNIX版本谱系的一手澄清。（BSDTalk EP183，[619.02-667.82]，L1）

**史料**：

- Ruben 撰写的澳大利亚 FreeBSD mini-conf 回顾，含演讲者名单与议题。（BSD Now EP335，[1272.54-1438.44]，L2）
- It's FOSS 的 John Paul 对 Hyperbola 联合创始人 Andre 的访谈。（BSD Now EP335，[419.28-426.72]，L2）
- Kamil Rytarowski 的 NetBSD 博客：改进 ptrace API 并为 LLVM 10 做准备。（BSD Now EP335，[935.22-964.18]，L2）
- 本期可据的一手材料包括：Andrew Tanenbaum 的当事人自述（EuroBSDCon 2014 演讲翌周接受访谈）、其转述的 John Lions 对 Version 6 Unix 逐行讲解讲义在各国大学间成为“地下经典”（1308.04-1310.62）的史实、AT&T 于 Version 7 许可证中加入教学与出书禁令的条款文本、MINIX 官方下载统计页 server.minix3.org/stats 的 2014 年 9 月 CD 镜像 15605 次下载记录与用户问卷调查、NetBSD 回归测试套件 81% 符合度的实测数据，以及 FreeBSD 邮件列表上 Michael Lucas 为撰 jails 专著征求工具意见的讨论串与凭邮件头 IP 识破 QJail 作者化名攻击的原帖。（BSD Now EP74，[1274.98-1316.58]，L2）
- 当事人Will Backman自述其BSD播客经历、对BSD Now的评价，以及BSD Now主持团队最初向其发出的联合主持邀请。（BSD Now EP27，[3735.70-3858.86]，L1）
- 当期新闻与教程覆盖OpenBSD X server无需root运行的改进、OpenSSH 6.6测试呼吁、NetBSD build.sh交叉编译流程及PC-BSD的Life Preserver备份工具更新。（BSD Now EP27，[3881.50-4990.90]，L2） [订正：原 [4417.34-4990.40]，2026-09-30 SenseAudio 重转核对]
- 当事人一手实测记录：五款 BSD live CD 在四类硬件上的启动、网卡与键盘图形检测、失败案例（GX280 USB 键盘不识别、NetBSD 盘 libqt 缺失）与逐盘评述，为 2006 年初 BSD 桌面化程度的一手横截面；另含经主持人转述的 DragonFly 1.4 发布公告及其分叉动机表述、GPLv3 起草阶段 FSF 与 Stallman 反 DRM 立场的公开信息。（BSDTalk EP7，[20.38-843.56]，L1）
- 主持人片头新闻播报 OpenBSD Foundation 创建，宗旨为支持 OpenBSD 及相关项目；报道称大额捐赠经由新设渠道进行，小额个人捐赠仍沿用既有方式。此为该基金会 2007 年成立之初的当代播客记载。（BSDTalk EP123，[31.56-44.12]，L2）
- Webmin 作者 Jamie Cameron 的一手访谈自述：项目起源、模块化扩展过程、Caldera、MSC Software、OpenCountry 的赞助史、跨平台适配经验、对 Linux 发行版碎片化的判断、BSD 许可证选择理由与 Virtualmin 双许可模式；另涉及其 Prentice Hall 出版的著作《Managing Linux Systems with Webmin》——为 Webmin 1.0 而写，此后变化多为新增功能、书中内容仍有效，可免费下载亦可购买。（BSDTalk EP9，[277.26-811.34]，L1）
- BSD daemon 吉祥物的口述史材料（经主持人转述）：daemon 拼写区别于 demon、义为后台无人值守进程，源自古希腊语中守护精灵之义而无撒旦关联；现有形象由 John Lasseter 绘制；版权由 Marshall Kirk McKusick 持有，以确保该形象仅用于代表 BSD 软件及相关服务。（BSDTalk EP9，[78.52-150.64]，L2）
- 本期留存的会议一手与二手记录包括：DataPipe 自 1998 年创立即全面使用 BSD 并拥有纽约地区 BSD 客户群的运营自述；OpenBSD 4.4 于 2008 年 11 月 1 日发布的日程及会议现场预售实况；Pavel 关于 FreeBSD ZFS 维护者稀缺与生产可用宣称瓶颈的自述；Theo Schlossnagle 的 Reconnoiter 监控系统 alpha 状态；OpenBSD PIE 拟纳入默认构建的动向；PCC 复兴与资助呼吁；ATF 测试框架的 NetBSD 采用计划。（BSDTalk EP161，[120.58-1152.98]，L1）
- 本期一手口述可稽的史料要点包括：Tektronix VAX 11/780双系统过渡与2.8BSD至4.3BSD升级序列、Stonehenge.com遭rootkit攻击与迁OpenBSD事件、InsightCruises网站在EC2上运行OpenSolaris的部署（约2009年9月上线）、Linux Fund亲和信用卡十年捐款逾70万美元及其与BSD Fund卡的资金池合并、Squeak许可清理征集约500名贡献者签名以期整体转入BSD许可证、其主持FLOSS Weekly至第100期的节目本身。（BSDTalk EP183，[270.62-981.99]，L1）

**史观**：

- 总纲13 法律与道德是利益分配：总纲13 法律与道德是利益分配：Hyperbola 的 fork 决策围绕 GPL、四条款 BSD 与 CDDL 的兼容性展开，许可证成为利益与自由的分配工具。（BSD Now EP335，[672.14-806.78]，L2）
- 总纲6 和解优于斗争：总纲6 和解优于斗争：JT 主张以正面理由论证 BSD 而非贬低 Linux，正面论证优于负面论证。（BSD Now EP335，[1971.68-1991.92]，L2）
- 总纲13 法律与道德是利益分配：AT&T 以许可条款而非技术优劣决定了谁能讲授 Unix、谁必须另起炉灶：法律文本成为大学与公司之间利益分配的界面，MINIX、BSD 系与 GNU 在此约束下各自占据生态位的分化并非技术“进步”的自然结果，而是许可权力再分配的产物；Tanenbaum 的动机自述为操作系统史上的许可证权力结构提供了一手注脚。（BSD Now EP74，[1321.38-1367.16]，L2）
- 总纲10 动手者创造历史：Tanenbaum 对比 EuroBSDCon 与 ACM 学术会议的受众：前者聚集因热情而非职称压力而来的实践者，后者系统方向的评价氛围被他概括为“把 Linux 性能提高 2%”（2444.50-2455.74），真正新颖而未经基准检验的构想反遭冷落；他以自身两代系统的工程取舍佐证系统演化由动手者的实践经验推动，而非仅由学术发表体制塑造。（BSD Now EP74，[2418.70-2478.98]，L1）
- 总纲13 法律与道德是利益分配：总纲13 法律与道德是利益分配：BSD许可与GPL的此消彼长被当事人置于企业采纳与规避风险的框架中解释，许可首先表现为利益分配工具。（BSD Now EP27，[3572.44-3610.86]，L3）
- 总纲8 本体论上各方平等：总纲8 本体论上各方平等：访谈以BSD许可重新浮现而非线性胜利的视角，同时呈现Linux技术优势与BSD许可吸引力，避免把某一方置于本体论优先位置。（BSD Now EP27，[3552.14-3645.20]，L3）
- 总纲10 动手者创造历史：总纲10 动手者创造历史：播客主持、教程制作与NetBSD交叉编译的演示都强调实际操作者对知识传播与技术工具的推动。（BSD Now EP27，[3927.86-4385.62]，L3）
- 总纲13 法律与道德是利益分配：主持人对 GPLv3 反 DRM 条款的解读呈现了许可证作为利益分配机制的本质：Stallman 试图以许可证条款强制商业公司放弃对用户设备的 DRM 控制，将权利再分配给终端用户，而商业公司是否愿意接受尚属疑问；与之相对，BSD 许可证以近乎零限制的条款把选择权交还使用者和商业方，两种许可证哲学在 DRM 议题上正面相遇。（BSDTalk EP7，[132.54-355.32]，L2）
- 总纲4 分离聚合是永恒规律：主持人预测若 GCC 随 GPLv3 发布，可能出现以 v2 末版为基的分叉编译器：许可证条款变更触发项目分叉，正是开源谱系以分离应对分歧、以聚合延续成果的常态机制。（BSDTalk EP7，[314.34-334.28]，L2）
- 总纲13 法律与道德是利益分配：whurley 将许可证选择表述为利益分配安排：BMC 实行单一宽松许可证政策，一律采用 BSD 许可证，理由是多项目多许可证并存会令集成者陷入法律泥潭；他认为 GPL 附加的限制越多，与日益追求自由的开发者社区越处于对立，而 MPL 的署名条款为 BSD 版权声明所天然涵盖，并无必要。其论证把许可证从技术授权文件还原为权利在作者、用户与商业再利用者之间的分配方案。（BSDTalk EP123，[1122.86-1320.06]，L1）
- 总纲3 不存在进步，只有权力再分配：whurley 提出“开放是开关状态，不能半开”：真正的开放须允许合作伙伴以 BSD 代码构建商业产品出售且不必回馈变更，回馈义务只存在于其与更大社区之间。他以此区分“控制”与“影响”——BMC 求影响而不求控制社区，并指其他限制性许可证难以围绕项目形成可持续生态。这是企业主动放弃代码控制权、换取社区影响力的权力关系再安排。（BSDTalk EP123，[1293.84-1407.58]，L1）
- 总纲15 文化即形式主义：whurley 断言专有软件与开源软件在代码本体上并无差别——都需许可证、代码与编译——差别全在社区与互动方式，即如何从用户收集信息、如何支持用户、如何促成联结；他引 Henry Louis Gates 语“收集数据只是走向智慧的第一步，分享数据才是走向社区的第一步”，指出企业以为开源代码即可坐等社区前来，是误置了共同体的位置。（BSDTalk EP123，[1514.58-1546.38]，L1）
- 总纲10 动手者创造历史：Webmin 由一线系统管理员解决自己日常痛点的脚本生长为跨平台管理框架，再借企业赞助与社区协作扩张——项目的形态由动手者面临的实际运维问题而非顶层设计决定，体现了动手者在日常实践中创造技术历史。（BSDTalk EP9，[277.26-346.42]，L1）
- 总纲8 本体论上各方平等：当事人代表 Digium 表态要“比过去更平台无关”，BSD 是其中一部分；面对 BSD 与 Linux 的比较，他明确拒绝高下叙事——操作系统选择取决于使用者的场景与理由，稳定性与性能差异不值得评论。在生产者层面，各操作系统被当作并列的部署选项而非进步序列中的先后位置。（BSDTalk EP166，[1079.28-1084.84]，L1）
- 总纲13 法律与道德是利益分配：GPL with exception 机制揭示许可证安排的利益分配本质：贡献者让渡部分权利换取项目存续与公司投入，公司以例外授权收入反哺开源开发。当事人对此不作道德表述而直陈其商业功能——授权设计即利益分配设计，BSD 与 GPL 之争在此呈现为两种可运行的分配机制而非善恶对错。（BSDTalk EP166，[437.92-464.70]，L1）
- 总纲13 法律与道德是利益分配：当事人以Perl Artistic License的长期观察为据陈述许可证哲学：Artistic License不区分原作者与后继作者的权利、鼓励分享而不强制，Perl因之被采纳的场合多于假设采用严格GPL的情形，Apache与BSD亦然；他将BSD许可证理解为对下一个修改者的信任机制，并自认无法理解“GPL狂热者”除非对方认为唯有强制方能促成共享。许可证在此呈现为不同利益分配规则的设计抉择而非道德高下。（BSDTalk EP183，[831.54-928.24]，L1）
- 总纲4 分离聚合是永恒规律：Linux Fund与BSD Fund两种亲和信用卡仅卡面吉祥物不同（Tux与Beastie），资金先入同一池再按比例大致分配，两会进而合并行政以消除双重开销；对立阵营的资助基础设施走向汇聚与共管，展示了 BSD 与 Linux 社区在资源层面的分离聚合，而非此消彼长的零和竞争。（BSDTalk EP183，[1188.06-1341.54]，L1）

**辨析**：

- Hyperbola 拟 fork OpenBSD 内核的计划被主持人质疑为工作量巨大、可持续性存疑，属开放性争议而非定论。　[存疑脚注] Hyperbola BSD 计划可行性存疑（BSD Now EP335，[829.34-903.78]，L3）
- 回应 Colin Percival 提问时，Tanenbaum 划清虚拟化与微内核的界限：MINIX 式多服务器系统由仅做消息传递的极小内核与相互独立的子系统进程构成，而 Xen 或 VMware 客户机内一个音频驱动缺陷仍会拖垮整个虚拟机，与裸机运行同样糟糕，仅因微内核仍存活而重启更快（1553.28-1556.08），故虚拟机隔离并不产生微内核所许诺的可靠性；此辨析有助于澄清 2010 年代将虚拟机隔离与微内核故障隔离混为一谈的流行认知。（BSD Now EP74，[1506.32-1563.92]，L1）
- Tanenbaum 称选 BSD 系的重要理由是许可证兼容，并转述某未具名大型公司投入数百万美元开发 Linux、却因 GPL 须把修改交给竞争对手而深陷困扰（1624.94-1641.72）；该说法无具名主体与文件佐证，属单一来源的当事人转述，仅可视为其对 BSD 宽松许可与 GPL 拷左义务企业接受度的个人判断，不宜径引为实证结论。　[存疑脚注] “某大型公司”未具名，其 GPL 困扰无从核证，须与企业 GPL 相关公开记录交叉验证后方可引用（BSD Now EP74，[1620.90-1644.72]，L4）
- 转写文本将嘉宾姓名拼写为Will Vochtmann、Will Bachman等多种形式，据语境应指BSD播客BSDTalk主持人Will Backman，引用时需以BSDTalk主持人的正式姓名为准。　[存疑脚注] 语音转写对嘉宾姓名拼写不一致，需以BSDTalk主持人的正式姓名Will Backman交叉核对。（BSD Now EP27，[0.0-12.52]，L5） [订正：原 "Will Vokman、Will Bachman"，2026-09-30 SenseAudio 重转核对]
- 当事人自我限定：其四台测试机不代表全部硬件生态，个别失败可能只是特定硬件组合的偶然不兼容，不能据此否定某张 live CD 的整体质量，引用本期的硬件兼容性结论时须保留这一适用范围限定。另转写将 Linux 参照 live CD 记作 Canopix 或 Nopix，所指发行版名称待考，引用其性能对比前须核实项目实名。[存疑脚注] 转写中的项目名 Canopix/Nopix 无法确证，待与 2006 年 live CD 发行版名录核对。　[存疑脚注] 转写中的 Linux live CD 项目名 Canopix/Nopix 无法确证，待与 2006 年 live CD 发行版名录核对。（BSDTalk EP7，[392.64-843.56]，L5）
- 转写中的若干专名存疑：whurley 所自述的原雇主转写作 Clusters，与通行记载（OpenQRM 源自 Qlusters 公司）存在疑似转写误差，采用前须以邮件列表档案与企业传记材料交叉核对；新转写中 Nagios 创始人作 Ethan Galstad、另提及前雇主转写作 Symantec（并涉 OpenSense 安全基础设施管理系统与 Jim Nasby、Decibel 等合作者），与通行记载一致；另其关于 GPL 与开发者社区相悖的判断系单方立场陈述，历史评价应与 GPL 阵营当事人论述对读。　[存疑脚注] 转写专名 Clusters 疑为语音识别误差，未经外部来源确证；whurley 的反 GPL 论断属单一来源立场推断。（BSDTalk EP123，[1429.02-1460.30]，L4） [订正：原 Symbia 与 Ethan Volstead 名目，2026-09-29 SenseAudio 重转核对]
- BSD daemon 图像出自 John Lasseter、版权由 Marshall Kirk McKusick 持有之说在本期为主持人转述，与公开记录相符，但节目本身未给出处；引用时应回溯 McKusick 的官方表述与相关版权页面核实。[考据脚注] 转述内容与已知公开记录一致，仍需一手来源复核。　[考据脚注] 图像作者与版权持有人信息需与 McKusick 官方版权声明核对。（BSDTalk EP9，[125.04-150.64]，L2）
- 转写专名失真较多：Theo Schlossnagle 转写作 Theo 加 Schloss-Nagel、监控系统 Zenoss 转写作 Xenos、Adrian Chadd 转写作 Adrian Chad、PCC 全称转写作 portable sieve andpiler、受访者姓名 Mark Satt 拼写存疑、演讲者 Anders 与 Julio 的姓氏未在转写中出现。引用人名与项目名时须回溯原始音频或会议议程核对。　[存疑脚注] 多处专名转写失真，校正依据为上下文语义与同期外部史料，须以原始音频复核（BSDTalk EP161，[581.85-1159.98]，L4）
- 讲座综述部分均系主持人的会后口头转述，其自承非开发者、部分技术内容超出其理解范围；转述的技术细节与论断须以各讲座的幻灯、录音或后续论文等一手材料复核，不可径直采信。　[存疑脚注] 转述者的理解深度有限，技术结论存在失真风险（BSDTalk EP161，[575.85-1223.62]，L4）
- quality 元数据提示 repetition_detected，通读确认重复主要源于现场直播的信号重试与主持人的填场独白，实质访谈与综述内容完整可读；本卡片全部观点取自语义完整的片段。　[存疑脚注] 直播信号中断与重复段落的成因判断基于转写文本特征推断，须回听原始录音核对现场实况。（BSDTalk EP161，[0.00-1510.88]，L4）
- 转写误植须考订：Dottie 应为 DAHDI（Zaptel 的更名）、VSD 应为 BSD、Astrus 应为 Asterisk、bidgium 与 didgium 应为 Digium、GraphQL user interface 应为 graphical user interface；贡献者 Gonzo 仅为社区 handle 而非本名。当事人称“原初 ZAP 驱动可能开发于 BSD 但当时 BSD 用户甚少”，其自述即为不确定回忆，且未给出可核验细节。[存疑脚注] ZAP 驱动的 BSD 起源说系单一来源含混回忆，需以 Digium 早期版本库历史与邮件列表复核。　[存疑脚注] ZAP 驱动 BSD 起源说与 Gonzo 真实身份均为单一口述来源，待 Digium 仓库史与社区存档交叉验证。（BSDTalk EP166，[194.56-204.56]，L4）
- 当事人称迁入OpenSolaris为“BSD又回来了”，其身份认同建立在对SunOS早期BSD血统的记忆上，而其运行的Solaris系谱系内核实为System V一脉，血统认同与实际技术谱系在此错位，提示用户迁移决策中的谱系想象与工程现实之别；另转写中“PURL.org”（1081.56秒处，疑为perl.org）与“Randy Harper/FreeBSDGirl”（1390.38秒处，疑为Randi Harper）两处人名站名依语音转写存疑，[存疑脚注] 须对照FLOSS Weekly节目原始信息核正。　[存疑脚注] PURL.org与Randy Harper两处专名系语音转写，未能与原始节目信息交叉验证。（BSDTalk EP183，[457.86-462.90]，L1）

**文献**：

- [BSD Now EP335] Pennington J. BSD Now: 335: FreeBSD Down Under[EB/OL]. (2020-01-30)[2026-08-15]. <https://www.bsdnow.tv/335>.
- [BSD Now EP74] Pennington J. BSD Now: 74: That Sly MINIX[EB/OL]. (2015-01-28)[2026-08-15]. <https://www.bsdnow.tv/74>.
- [BSD Now EP27] Pennington J. BSD Now: 27: BSD Now vs. BSDTalk[EB/OL]. (2014-03-05)[2026-08-15]. <https://www.bsdnow.tv/27>.
- [BSDTalk EP7] Backman W. BSDTalk: Live BSD CDs[EB/OL]. (2006-01-18)[2026-08-15]. <https://archive.org/download/bsdtalk007/bsdtalk007.ogg>.
- [BSDTalk EP123] Backman W. BSDTalk: 123: bsdtalk123 - William “whurley” Hurley, Chief Architect of Open Source Strategy at BMC Software, Inc.[EB/OL]. (2007-07-30)[2026-08-27]. <https://bsdtalk.blogspot.com/2007/07/bsdtalk123-william-whurley-hurley-chief.html>.
- [BSDTalk EP9] Backman W. BSDTalk: Interview with Webmin Author Jamie Cameron[EB/OL]. (2006-01-24)[2026-08-15]. <https://archive.org/download/bsdtalk009/bsdtalk009.ogg>.
- [BSDTalk EP161] Backman W. BSDTalk: 161: bsdtalk161 - Live from NYCBSDCon Sunday[EB/OL]. (2008-10-12)[2026-08-27]. <https://bsdtalk.blogspot.com/2008/10/bsdtalk161-live-from-nycbsdcon-sunday.html>.
- [BSDTalk EP166] Backman W. BSDTalk: 166: bsdtalk166 - Asterisk Open Source Community Director John Todd[EB/OL]. (2008-11-25)[2026-08-27]. <https://bsdtalk.blogspot.com/2008/11/bsdtalk166-asterisk-open-source.html>.
- [BSDTalk EP183] Backman W. BSDTalk: 183: bsdtalk183 - Randal L. Schwartz[EB/OL]. (2009-12-23)[2026-08-27]. <https://bsdtalk.blogspot.com/2009/12/bsdtalk183-randal-l-schwartz.html>.

<!-- /PODCAST_REVIEW -->
