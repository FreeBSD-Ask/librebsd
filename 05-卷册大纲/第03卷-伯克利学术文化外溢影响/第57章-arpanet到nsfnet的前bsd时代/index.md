---
chapter: 第 57 章
id: CH57
volume: 第03卷-伯克利学术文化外溢影响
---

# 第 57 章 arpanet到nsfnet的前bsd时代

## 要点

- 互联网前 BSD 时代（1969-1983）的协议生态包括：（1）NCP（Network Control Program，ARPANET 1971-1983 使用）；（2）X.25（CCITT 1976 标准的分组交换协议，用于 Tymnet、Telenet 等公共网络）；（3）SNA（IBM 1974 发布的系统网络架构）；（4）DECnet（DEC 1975 发布的网络架构）；（5）〔待核：原文截断，后文待回源〕
- BSD 开发者参与 IETF 的关键事件包括：（1）Joy 与 Leffler 的 4.2BSD TCP/IP 实现影响 IETF TCP/IP 标准化；（2）Paul Mockapetris（ISI）的 DNS 设计（RFC 882/883 1983）由伯克利四研究生实现为 BIND；（3）Jonathan Postel（USC ISI，RFC 编辑）与 CSRG 的合作；（4）Allman 的
- BIND 的全球统治：1990 年代 BIND 运行全球约 90% 的 DNS 服务器，BIND 的统治地位带来安全责任，BIND 安全漏洞史包括：（1）BIND 4.9.x 1990 年代后期多个远程漏洞；（2）BIND 8.2.x 1999 年 NXT 记录等多个漏洞（CERT Advisory CA-1999-14）；（3）BIND 9 的多次 CVE；〔待核：原文截断，后文待回源〕
- Sendmail 的替代品：（1）Qmail 1995 年由 D. J. Bernstein 发布，强调安全性，Qmail 的安全设计（最小特权、沙箱）使 Sendmail 安全问题凸显，许可证：公有领域（Bernstein 本人于 cr.yp.to/qmail/dist.html 声明将 qmail 置于公有领域）[考据脚注：经 cr.yp.to/qmail/dist.html 一手来源确证。]

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3817] 卷“第03卷-伯克利学术文化外溢影响”第 57 章，匹配置信度 folder，原因：folder 第56章
- [DB:references_fulltext:chapter_matches:chmatch_3818] 卷“第03卷-伯克利学术文化外溢影响”第 57 章，匹配置信度 folder，原因：folder 第56章
- [DB:references_fulltext:chapter_matches:chmatch_3820] 卷“第03卷-伯克利学术文化外溢影响”第 57 章，匹配置信度 folder，原因：folder 第56章
- [DB:references_fulltext:chapter_matches:chmatch_3821] 卷“第03卷-伯克利学术文化外溢影响”第 57 章，匹配置信度 folder，原因：folder 第56章
- [DB:references_fulltext:chapter_matches:chmatch_3976] 卷“第03卷-伯克利学术文化外溢影响”第 57 章，匹配置信度 folder，原因：folder 第56章
- [DB:references_fulltext:chapter_matches:chmatch_3977] 卷“第03卷-伯克利学术文化外溢影响”第 57 章，匹配置信度 folder，原因：folder 第56章
- [DB:references_fulltext:chapter_matches:chmatch_3621] 卷“第03卷-伯克利学术文化外溢影响”第 57 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3622] 卷“第03卷-伯克利学术文化外溢影响”第 57 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3651] 卷“第03卷-伯克利学术文化外溢影响”第 57 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3663] 卷“第03卷-伯克利学术文化外溢影响”第 57 章，匹配置信度 curated，原因：curated token rule

## 史观

（章级史观/辨析按子节字段聚合回填——本卷 57 章；2026-09-11 整改将占位改为编排说明，完整聚合随正文阶段逐章完成。子节级映射详见各节史观字段。）

## 辨析

- **要点**：ARPANET 1969 年建立，由 ARPA（Advanced Research Projects Agency，1958 年成立）资助，Bolt Beranek and Newman（BBN）公司承建，1969 年 10 月 29 日首个节点（UCLA，Leonard Kleinrock 实验室）与第二节点（SRI，Douglas Engelbart 实验室）间发送首个消息 “lo”（本意 “login” 但系统崩溃），1969 年底四节点拓扑（UCLA、SRI、UC Santa Barbara、Utah），早期使用 NCP（Network Control Program）
- Mockapetris DNS RFC 882/883 发布时间确认为 1983 年 11 月（RFC 882“Domain Names: Concepts and Facilities”与 RFC 883“Domain Names: Implementation and Specification”，作者 Paul Mockapetris，USC ISI）；SMTP RFC 821 发布时间确认
- BIND 1990 年代市场份额（约 90%）——多源引用但缺乏权威统计来源（Netcraft 等统计机构 1990 年代后期的 DNS 服务器市场份额数据保留 ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］）；BIND 4.9.x 具体漏洞时间与版本——CERT/CC 安全公告档案为权威来源，具体漏洞编号与版本须以 CERT/CC 公告为准；BIND
- Qmail 发布时间确认为 1995 年（Daniel J. Bernstein 发布，强调安全性，许可证为公有领域——Bernstein 本人于 cr.yp.to/qmail/dist.html 声明将 qmail 置于公有领域）；Postfix 发布时间确认为 1998 年（原名 VMailer，IBM T.J. Watson 研究中心 Wietse Venema 开发，使用 IBM Publ

## 文献

- NCP 协议文档；CCITT X.25（1976）；IBM SNA 文档；DEC DECnet 文档；Lesk, M. (1978) UUCP［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- RFC 882/883（1983）；RFC 821（1982）；Mockapetris DNS 档案；Postel 与 CSRG 合作档案［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- BIND 安全漏洞档案；CVE 数据库；PowerDNS/Unbound/NSD 项目档案［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- Bernstein, D. J. Qmail 档案；Venema, W. Postfix 档案；Hazel, P. Exim 档案；Sendmail 市场份额演变数据［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］[^doubt-resolved-121]: 据 en (1994) 消解〔存疑订正：作者名“据 en”疑讹，消解依据不可辨识，待回源核〕

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP558、BSD Now EP552、BSD Now EP507、BSD Now EP323、BSD Now EP197（共 5 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 主持人转述 Telnet 协议史：1972 年 John Postel 撰写的 RFC 奠定 Telnet 协议，Postel 在文中自嘲该文档未能兑现及时、清晰与简洁的承诺；1990 年代早期 Telnet 曾用于访问国会图书馆、NASA 新闻与最高法院判决。（BSD Now EP558，[1253.14-1360.36]，L2）
- 主持人介绍 towel.blinkenlights.nl 的 ASCII 版《星球大战》与 telehack.com 等项目，后者以 Telnet 重现 ARPANET 时代的 BBS、MUD 与文本冒险，构成对早期网络文化的保存。（BSD Now EP558，[956.74-1151.44]，L2）
- FreeBSD 基金会发布 SSDF 自证报告第一版，面向美国政府软件供应链合规（NIST SP 800-218 与 Executive Order 14028）；NetApp 与 RG Nets 等伙伴引用该报告支持其向政府客户供货。（BSD Now EP558，[483.30-730.50]，L2）
- BSDCan 组织委员会自述 Dan Langille 在主持二十年后交棒，委员会成立加拿大非营利组织 BSDCan Conferences Incorporated 以承接资金与赞助；当届白金赞助商为 Netflix，金级为 Apple 与 ARM。（BSD Now EP558，[2801.24-3400.76]，L1）
- 委员会回顾 BSDCan 票价自 2005 年起十五年间维持 199 美元未变，现调整为 256 美元；其拍卖传统所得捐给 Ottawa Mission 慈善机构。（BSD Now EP558，[3545.42-3667.88]，L1）
- 主持人转述 Liam Proven 在 The Register 的报道：iXsystems 将重心转向基于 Debian 的 TrueNAS SCALE，FreeBSD 基底的 TrueNAS CORE 进入维持工程阶段，计划推出基于 FreeBSD 13.3 的版本后不再规划 FreeBSD 14 基底。（BSD Now EP552，[806.14-1046.26]，L2）
- 文章追述 FreeNAS 与 iXsystems 的商业谱系：FreeNAS 始于 2005 年、基于 m0n0wall 与 PHP Web 界面；iXsystems 源自曾销售 BSD/386 的 Berkeley Software Design Inc.，经与 Walnut Creek CD-ROM 合并、向 Wind River 出售 OS 部门等转手后于 2007 年收购 FreeNAS。（BSD Now EP552，[919.74-1153.86]，L2）
- 主持人介绍 Jason Eckert 的博客：1997 年 Tadpole Technologies 的 SPARCbook 3000ST 搭载 Fujitsu TurboSPARC 170MHz 处理器、128MB 内存与 Solaris 2.5.1，售价约 21000 美元，是 1990 年代高端 Unix 笔记本电脑的代表。（BSD Now EP552，[1590.02-1751.82]，L2）
- 主持人转述 Hacker News 用户评论：Ford Aerospace 是早期商业 BSD Unix 站点之一，须先向 AT&T 购买 Unix 32V 许可，再从伯克利的 Bill Joy 处取得 BSD 磁带；BSD 当时无网络，站点购买 3Com 的 UNET（Greg Shaw 所写 TCP/IP）并处理 4.3BSD 与其他实现的互操作问题，最终与 Nagle 算法的出现相关。（BSD Now EP552，[2710.40-2874.60]，L2）
- Lucas 回顾 OpenBSD 文件系统：OpenBSD 沿用源自 4.4BSD 的 UFS1（约 1994 年稳定）并长期调试，随后在 2000 年代早期采用较早期版本的 UFS2；相较 ZFS、btrfs 等新文件系统，OpenBSD 的 UFS 哲学是把文件系统保持简单，认为功能即缺陷。（BSD Now EP507，[489.90-760.60]，L1）
- Lucas 以 PF 与 UFS 为例说明 BSD 各分支之间的代码双向流动：OpenBSD 的 PF 被 FreeBSD 移植并各自演进，反过来 FreeBSD UFS2 在 OpenBSD 移植之后才开发快照，形成方向相反的技术借取与债务。（BSD Now EP507，[583.98-612.94]，L1）
- Lucas 讲述其考证的 1978 年第一封垃圾邮件：DEC 的 Gary Thuerk 为推广新产品向数百名陌生用户群发邮件，五天后美国空军 ARPANET 管理分支负责人致电其上司警告，但该邮件仍促成约 1200 万美元计算机销售，埋下垃圾邮件经济动机的起点。（BSD Now EP507，[1351.12-1453.32]，L2）
- 关于生成式 AI，Lucas 认为 ChatGPT 只产出看似答案的文本而非答案，越长的内容越易失实；他援引美国国会图书馆已裁定 AI 生成文本不可版权，并主张作者与读者直接连接的重要性上升。（BSD Now EP507，[2281.44-2813.20]，L1）
- Lucas 介绍其邮件服务器写作计划，强调 SPF、DKIM、DMARC 等外围协议已成自建邮件的前提，DKIM 虽 2011 年即存在，其强制要求却是近年才出现。（BSD Now EP507，[1108.24-1277.00]，L1）
- 计算机历史博物馆发布“最早 Unix 代码”周年源码版，收录 PDP-7 汇编清单（Space Travel、moo、井字棋等），经 Warren Toomey 与 John Mashey 等鉴定可溯至 1970 至 1971 年初。（BSD Now EP323，[167.90-193.82]，L2）
- Leonard Kleinrock 受访回顾 1969 年 10 月 29 日 UCLA 发出的“LO”消息：他预见网络“始终在线、无处不在、不可见”，但未预见其社交化与国家安全化，并拒绝为创造互联网而后悔。（BSD Now EP323，[486.68-671.22]，L1）
- OpenBSD 自 1995 年 10 月 18 日起跨过 40 万提交，Theo de Raadt 提醒计数口径不一；主持人补充 FreeBSD 约 92.5 万、NetBSD 加 pkgsrc 约 60 万，强调跨项目比较不可靠。（BSD Now EP323，[1095.24-1167.46]，L2）
- Blacklistd 作为 fail2ban 替代，通过 libexec helper 与 NPF 联动按失败认证次数封锁 IP；教程演示 securelevel=1 下需把模块编入内核或经 modules.conf 预载。（BSD Now EP323，[685.00-1027.92]，L2）
- “OSI 七层墨西哥卷饼”作者自建 DoH 服务器与私有 CA，把 Firefox 的 TRR 指向本地，以对抗浏览器厂商对 DNS 的集中收编，而非简单禁用。（BSD Now EP323，[1862.22-2002.76]，L2）
- 长篇采访 Michael W. Lucas：他谈《Absolute FreeBSD》第三版写作计划（2018 年 BSDCan 前付印）、科幻与犯罪小说的跨体裁写作，以及 BSDCan、EuroBSDCon 等会议文化。（BSD Now EP197，[4089.38-4994.88]，L1）
- 该期讨论 OpenBSD relayd：可做应用层检查（如仅允许 HTTP GET、限制 HTTP 方法），其 socket splicing 把两端 socket 在内核直接拼接以提升转发性能，并与 LibreSSL/PF 配合。（BSD Now EP197，[450.90-675.00]，L2）
- Peter Hansteen（《The Book of PF》作者）的文章介绍用 OpenBSD spamd 与辅助 MX 搭建反垃圾邮件方案：确保主备 MX 均可收信、统一内容过滤、部署 spamd、同步灰名单与陷阱地址。（BSD Now EP197，[5136.50-5630.00]，L2）
- 报道 Google 为 Chrome 赞助的 Capsicum-on-Linux 进展：部分功能已合入，提供 autoconf 脚本使同一代码可在 Linux 与 FreeBSD 使用 Capsicum，并列出已被转换的工具清单。（BSD Now EP197，[5638.38-5715.14]，L2）
- 一篇“1979 年的网关如何搭建”文章显示 TCP/IP 的基本原理至今未变，是早期网络路由器技术的历史回溯。（BSD Now EP197，[5727.24-5790.82]，L2）

**史料**：

- 本期史料包括 Telnet 历史的二手文章、FreeBSD 基金会 SSDF 公告，以及 BSDCan 组织委员会 Michael Lucas、Patrick 与 Peter Hansteen 的一手自述。（BSD Now EP558，[483.30-3400.76]，L1）
- 本期史料包括 Liam Proven 的记者综述、Jason Eckert 的设备拆解记录，以及 Hacker News 上 Ford Aerospace 亲历者的自述评论；后两者经节目主持人口头转述。（BSD Now EP552，[806.14-2874.60]，L2）
- Michael W. Lucas《OpenBSD Mastery: Filesystems》一书，为当期采访对象本人撰写的文件系统专著，属于当事人一手出版物。（BSD Now EP507，[126.18-172.34]，L1）
- 1978 年 Gary Thuerk 垃圾邮件事件为 Lucas 写作邮件书籍时考证的历史线索，经当期采访口头转述。（BSD Now EP507，[1351.12-1453.32]，L2）
- BSD 各分支在 PF 与 UFS 上的双向代码流动，为 Lucas 作为长期 BSD 作者与使用者的工程观察，属二手叙述。（BSD Now EP507，[583.98-612.94]，L2）
- 计算机历史博物馆“Earliest Unix Code”目录与 PDF，含 PDP-7 汇编、Space Travel 1970 源码页。（BSD Now EP323，[214.28-234.20]，L2）
- CBC《The Current》对 Leonard Kleinrock 的半小时访谈节选（首条消息“LO”及网络阴暗面）。（BSD Now EP323，[387.08-402.72]，L1）
- Theo de Raadt 致 tech@ 的“OpenBSD 跨 40 万提交”邮件，说明计数困难与仓库历史歧义。（BSD Now EP323，[1100.92-1113.56]，L2）
- unitedbsd.com 的 Blacklistd 与 NPF 教程，及 NetBSD securelevel 与 bpf-jit 配置说明。（BSD Now EP323，[693.04-812.78]，L2）
- Peter Hansteen 的 spamd 配置文章；Google Capsicum-on-Linux 状态页；1979 年 TCP/IP 网关文章。（BSD Now EP197，[5136.50-5790.82]，L2）

**史观**：

- 总纲18 时间是一种形式主义：Telnet 从主流远程访问工具变为小众怀旧文化，呈现技术生命周期随时代需求而更替的形式化进程。（BSD Now EP558，[1253.14-1412.28]，L2）
- 总纲10 动手者创造历史：Dan Langille 与历届志愿者持续二十年操办 BSDCan，其交棒与新机构设立延续了社区会议，体现动手者对社区基础的长期投入。（BSD Now EP558，[2801.24-3108.48]，L1）
- 总纲13 法律与道德是利益分配：SSDF 自证是软件供应商满足政府采购合规的制度安排，反映安全标准背后的法律与利益分配。（BSD Now EP558，[483.30-730.50]，L2）
- 总纲10 动手者创造历史：Ford Aerospace 工程师为网络互操作重写 UDP、ICMP 与 TCP，Nagle 算法源于一线工程实践而非纯理论推演，体现动手者创造历史。（BSD Now EP552，[2814.88-2857.92]，L2）
- 总纲3 不存在进步，只有权力再分配：iXsystems 从 BSDi 谱系转向 Linux 基底，是存储商业生态中资源与权力在平台间的重新分配。（BSD Now EP552，[806.14-1046.26]，L2）
- 总纲11 商品是形式主义：SPARCbook 以 21000 美元的高价与军事级镁合金机身成为小众商品，与廉价 PC 开放架构的对照呈现技术商品化的不同形态。（BSD Now EP552，[1647.86-1751.82]，L2）
- 总纲4 分离聚合是永恒规律：各 BSD 分支不断分离又借取聚合，代码流动呈现双向循环而非线性派生。：BSD 各分支在 PF 与 UFS 上相互分离又聚合，代码双向流动而非单向派生。（BSD Now EP507，[583.98-612.94]，L1）
- 总纲10 动手者创造历史：作者以专著记录长期维护与调试的工程细节，凸显沉默维护者的历史作用。：Lucas 以文件系统著作为动手者记录维护者的工程现实，而非只写台前叙事。（BSD Now EP507，[489.90-760.60]，L1）
- 总纲13 法律与道德是利益分配：SPF、DKIM、DMARC 等协议是邮件生态围绕送达与信任利益形成的规范分配。：垃圾邮件的持续源于首次群发所揭示的经济收益，反垃圾协议是围绕邮件送达利益而演化的规范分配。（BSD Now EP507，[1351.12-1453.32]，L2）
- 总纲1 一切真历史都是古代史：50 年前的“LO”消息与 PDP-7 汇编被当作当下仍须考据的古代对象。（BSD Now EP323，[120.92-125.14]，L2）
- 总纲5 没有必然性，只有偶然性：ARPANET 首条消息因机器崩溃停在“LO”而非“LOGIN”，是偶然事件。（BSD Now EP323，[421.34-425.12]，L1）
- 总纲19 解释学循环是历史认识的根本条件：源码断代依赖 Toomey、Mashey 等当事人回忆与目录残迹的循环解释。（BSD Now EP323，[167.90-193.82]，L2）
- 总纲8 本体论上各方平等：OpenBSD、FreeBSD、NetBSD 提交数被并置比较时，主持人强调口径差异，避免以数量定高下。（BSD Now EP323，[1161.86-1189.66]，L2）
- 总纲6 和解优于斗争：DoH 作者不以禁用对抗，而以自建本地 DoH 把集中化化解为自托管。（BSD Now EP323，[1972.26-1999.44]，L2）
- 总纲14 苦难不值得被提倡：Kleinrock 对网络阴暗面的回顾不美化早期“全员良善”的叙事，也不为创造互联网而后悔。（BSD Now EP323，[587.28-671.22]，L1）
- 总纲6 和解优于斗争：Capsicum 从 FreeBSD 向 Linux 的扩散显示技术传承跨阵营流动，而非单向竞争，呈现生态之间的和解与相互借鉴。（BSD Now EP197，[5638.38-5715.14]，L2）

**辨析**：

- Telnet 1972 年 RFC 的作者归属与 John Postel 的自嘲引文来自二手文章，须以 RFC 原文核实。　[存疑脚注] RFC 作者与引文为二手转述，未经 RFC 原文核实。（BSD Now EP558，[1253.14-1319.76]，L4）
- BSDCan 票价自 2005 年起十五年未变的说法为委员口述，须以历年会议档案核实。　[存疑脚注] 票价历史为委员口述，未经历年会议档案核实。（BSD Now EP558，[3545.42-3563.30]，L4）
- Hacker News 评论为匿名用户自述，Ford Aerospace、3Com UNET 与 Nagle 算法的具体关联须以更多独立来源交叉验证。　[存疑脚注] 早期 TCP/IP 口述为匿名评论经节目转述，未经多源交叉验证。（BSD Now EP552，[2710.40-2874.60]，L4）
- iXsystems 转向 Linux 的时间线与版本计划来自记者报道与 Reddit 上 Chris Moore 的帖子，须以官方公告核实。　[存疑脚注] TrueNAS 路线信息来自记者报道与社区帖文，未经官方公告核实。（BSD Now EP552，[948.50-1000.66]，L4）
- 1978 年第一封垃圾邮件的约 1200 万美元销售额及军方联系人姓名为 Lucas 口头转述，需以 ARPANET 原始记录与既有垃圾邮件史研究交叉验证。　[存疑脚注] 金额与军方联系人姓名拼写为单一来源口头叙述，须以原始档案核验。（BSD Now EP507，[1351.12-1453.32]，L4）
- Lucas 对 OpenBSD UFS2 缺乏快照、FreeBSD 在 OpenBSD 移植后才开发快照的时间先后判断为当事人概括，须以两分支 UFS2 提交史核验。　[存疑脚注] 快照特性的先后次序为当事人口头判断，需以 FreeBSD 与 OpenBSD 的 UFS2 提交记录核验。（BSD Now EP507，[583.98-612.94]，L4）
- OpenBSD 的 40 万提交仅为一种测量口径，仓库历史久、有缺失 changelog 与不可转换分支，任何计数都可能高估或低估。　[考据脚注] Theo 本人与主持人双重提示计数不可靠（BSD Now EP323，[1131.88-1154.46]，L3）
- PDP-7 源码断代“1970 至 1971 初”依赖两位早期贡献者与馆方编目，属多源交叉但仍非绝对定年。　[存疑脚注] 定年证据链为多源交叉，非单一权威结论（BSD Now EP323，[167.90-193.82]，L3）

**文献**：

- [BSD Now EP558] Pennington J. BSD Now: 558: Worlds of telnet[EB/OL]. (2024-05-09)[2026-08-15]. <https://www.bsdnow.tv/558>.
- [BSD Now EP552] Pennington J. BSD Now: 552: The Laptop Sparc[EB/OL]. (2024-03-28)[2026-08-15]. <https://www.bsdnow.tv/552>.
- [BSD Now EP507] Pennington J. BSD Now: 507: Michael W. Lucas Interview[EB/OL]. (2023-05-18)[2026-08-15]. <https://www.bsdnow.tv/507>.
- [BSD Now EP323] Pennington J. BSD Now: 323: OSI Burrito Guy[EB/OL]. (2019-11-07)[2026-08-15]. <https://www.bsdnow.tv/323>.
- [BSD Now EP197] Pennington J. BSD Now: 197: Relaying the good news[EB/OL]. (2017-06-07)[2026-08-15]. <https://www.bsdnow.tv/197>.

<!-- /PODCAST_REVIEW -->

<!-- dangan-20260908 消解回写 -->
- Kleinrock. L. (2009/2011). The Day the Infant Internet Uttered its First Words [个人官方网站档案，基于 UCLA IMP Log 原始记录]. <https://www.lk.cs.ucla.edu/internet_first_words.html>[EB/OL]. 2009. ［DKC-1469→fulltext:5908］
- Living. The ARPANET was retired in 1990[EB/OL]. 1990. ［DKC-1478→fulltext:5910］
- Mockapetris. P. (1983) RFC 882/883[Z]. 1983. ［DKC-1485→fulltext:5914］
<!-- /dangan-20260908 -->
