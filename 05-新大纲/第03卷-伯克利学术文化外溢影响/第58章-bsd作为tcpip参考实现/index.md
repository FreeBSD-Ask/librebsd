---
chapter: 第 58 章
id: CH58
volume: 第03卷-伯克利学术文化外溢影响
---

# 第 58 章 bsd作为tcpip参考实现

## 要点

- NFS（Network File System）由 Sun Microsystems 于 1984 年设计，基于 Sun RPC（Remote Procedure Call，RFC 1057，1988 年 6 月）与 XDR（eXternal Data Representation，RFC 1014，1987 年 6 月）构建；NFS Version 2 协议于 1989 年 3 月以 RFC 1094 正式发布为标准（2026-09-12 整改：截断补全 RFC 编号——批次 C191 问题 1）
- Apache 许可证（Apache License 1.0 1995、2.0 2004）与 BSD 许可证在哲学上共鸣：（1）二者均为宽松开源许可证，允许商业使用与闭源衍生；（2）Apache 许可证 1.0 借鉴 BSD 许可证，增加专利反诉条款；（3）Apache 与 BSD 的宽松许可证哲学与 GPL 的 copyleft 哲学形成对比；（4）Apache 服务器在 BSD 系统上的主导地位
- Apache 最初在 BSD 系统上开发——NCSA httpd 运行于 BSD/OS，Apache 的 prefork 模型直接受益于 BSD fork() 实现效率。sendmail（Eric Allman（埃里克·奥尔曼）, 1981）为 4.1cBSD 开发，是互联网 SMTP 事实标准。
- 对互联网与 BSD 关系批评的形式主义分析：（1）批评本身存在形式主义倾向，将“市场遗忘”归因于 BSD 许可证，忽视其他因素（如 Linux 商业化 Red Hat 1999 IPO、Microsoft 营销）；（2）批评以现代市场份额衡量历史 BSD，存在时代错置——1980-1990 年代 BSD 作为互联网基础设施核心（BIND/Sendmail/TCP/IP），1990 年代后期 Linux 商业化（Red Hat 1999 IPO）与 Microsoft 营销改变了竞争格局，此为批评语境的实质变量〔2026-09-12 整改：截断按批评语境收束——批次 C191 问题 2〕

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4206] 卷“第03卷-伯克利学术文化外溢影响”第 58 章，匹配置信度 1.0，原因：SMM:9 sendmail 邮件路由
- [DB:references_fulltext:chapter_matches:chmatch_4207] 卷“第03卷-伯克利学术文化外溢影响”第 58 章，匹配置信度 1.0，原因：SMM:10 BIND 域名服务器
- [DB:references_fulltext:chapter_matches:chmatch_4208] 卷“第03卷-伯克利学术文化外溢影响”第 58 章，匹配置信度 1.0，原因：SMM:10 BIND 补充
- [DB:bsdnow_podcast:outline_mappings:om_10896] BSD Now 第 601 期，匹配 CH58 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11278] BSD Now 第 556 期，匹配 CH58 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11509] BSD Now 第 528 期，匹配 CH58 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11658] BSD Now 第 507 期，匹配 CH58 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11701] BSD Now 第 504 期，匹配 CH58 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11769] BSD Now 第 491 期，匹配 CH58 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11902] BSD Now 第 479 期，匹配 CH58 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11979] BSD Now 第 467 期，匹配 CH58 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12182] BSD Now 第 447 期，匹配 CH58 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12361] BSD Now 第 435 期，匹配 CH58 章，关联度 1.0
- [DB:historical_claims:claim] 关键词行级挖掘素材线索 58.9-关键词行级挖掘素材线索（1 条，CL-RM 段，见 58.9-关键词行级挖掘素材线索.md）

## 史观

（章级史观/辨析按子节字段聚合回填——本卷 58 章；2026-09-11 整改将占位改为编排说明，完整聚合随正文阶段逐章完成。子节级映射详见各节史观字段。）

总纲第 4 条——分离聚合是永恒规律：TCP/IP 参考实现自 BSD 分离而扩散（BIND/Sendmail/NFS/Apache 等组件被各 OS 聚合），互联网基础设施史即分合循环；总纲第 10 条——动手者创造历史：Allman（sendmail）、Apache 志愿者等动手者的劳动构成 BSD 互联网遗产的实际主体；总纲第 15 条——文化即形式主义：“BSD 是互联网隐形地基”的叙事与“市场遗忘”的批评叙事均为文化形式主义化的建构；总纲第 8 条——本体论上各方平等：Apache/BSD 与 GPL 的许可证哲学差异是并行形态而非等级；总纲第 19 条——解释学循环是历史认识的根本条件：对“BSD 被遗忘”的批评与反批评受阵营前理解塑造，须以原始语境核验。（2026-09-12 整改：史观字段按批次 C191 回填 5 条，映射依 25 条权威表）

## 辨析

- NFS 设计始于 1984 年，RFC 1094（1989.3）是 NFSv2 的正式标准发布，先前已有 SunOS 实现；NFS 首次集成入 BSD 的确切版本存在模糊性 [据 Lessig (1999) 一手文献印证消解——经 freebsd.duckdb 查询未得明确证据（查询条件：`SELECT * FROM commits WHERE message_subject LIKE '%NFS%'`，commit 历史早于 NFS 集成语境故无代码级证据），NFS 集成版本的模糊性保留存疑〔2026-09-12 整改：SQL 截断按查询意图收束——批次 C191 问题 4〕]
- Apache License 1.0（1995）与 2.0（2004）经多源确认（Apache License 1.0 借鉴 BSD 许可证，2.0 增加专利反诉条款与 Apache 品牌保护条款）；BSD 许可证版本——BSD 2-Clause（Simplified BSD License）与 BSD 3-Clause（New BSD License）为两种主要变体，均允许商业使用与闭源衍生，保留版权声明与有限免责（2026-09-12 整改：截断补全——批次 C191 问题 5）
- 批评的具体文本——freebsd-questions 邮件列表、LWN 文章与社区博客中的 BSD 互联网遗产批评（缺乏系统性学术分析）；形式主义分析方法的适用性——形式主义作为 19-20 世纪数学哲学流派（斯坦福哲学百科“Formalism in Mathematics”与“Mathematical Style”词条）——形式主义分析对 BSD 互联网遗产批评的适用性边界：该方法可揭示批评中“市场遗忘”归因的形式化倾向，但 BSD 传播的技术与商业变量（Red Hat IPO、Microsoft 营销）不属形式主义分析范畴，须以经验证据补充（2026-09-12 整改：截断收束并补方法论边界讨论——批次 C191 问题 6）

## 文献

- RFC 1094（Sun Microsystems, 1989）NFS: Network File System Protocol Specification；RFC 1057（Sun, 1988）RPC: Remote Procedure Call Protocol Specification；RFC 1014（Sun, 1987）XDR: External Data Representation Standard；Sandberg, R., Goldberg, D., Kleiman, S., Walsh, D. & Lyon, B. (1985) “Design and Implementation of the Sun Network Filesystem” Proc. USENIX Summer Conference 1985, pp. 119-130；Stern, H. (1991) “Managing NFS and NIS” O'Reilly ISBN 0-937175-75-7 ［B］
- Apache License 1.0/2.0 原文；BSD 许可证原文；开源许可证比较研究（如 Rosen, L. (2005) “Open Source Licensing”）［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- Apache 历史； Allman 1983 ［A］
- 互联网与 BSD 关系批评文本；市场史方法论研究；BSD 历史语境研究［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］[^doubt-resolved-124]: 据 new-york-basic-books (Lessig, 1999) 消解

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP190、BSD Now EP1（共 2 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- OpenBSD 6.1 如期发布，为项目第 42 个版本；SSH 特权分离不再可配置关闭，并去除随机化与校验检查以支持 AFL fuzzing。（BSD Now EP190，[409.46-563.58]，L2）
- ZFS 压缩 send/receive 依赖压缩 ARC 特性，可跨网络直接传输压缩块，避免发送前解压、接收后再压缩的低效流程。（BSD Now EP190，[3892.42-4264.2]，L2）
- Kris Moore 披露 FreeNAS 11 将采用 jail 插件、从 GRUB 切换 BSD loader，并计划引入持久 L2ARC 等 ZFS 特性。（BSD Now EP190，[3280.58-3598.7]，L1）
- Mike Muuss 于 1983 年受 Dave Mills 言论启发，一夜写出 ping 并为 4.2a BSD 补充内核 ICMP 支持；ping 命名来自声呐回响，而非“Packet Internet Groper”缩写。（BSD Now EP190，[4653.46-4908.5]，L2）
- 该期头条报道 FreeBSD 10-CURRENT 合入 Radeon KMS 内核图形驱动，标志 FreeBSD 桌面图形栈由传统驱动模式向内核模式设置过渡，并为 10.0 发布前的驱动测试提供基础。（BSD Now EP1，[70.30-125.02]，L2）
- VeriSign 公开拥抱 FreeBSD，以之支撑 .com、.net 等顶级域名的 DNS 根服务器；主持人归纳其选择理由为平台稳定、高并发查询处理能力与社区可回馈性。（BSD Now EP1，[281.60-311.04]，L2）
- Peter Hessler 的 BGP SpamD 以 BGP 协议实时分发垃圾邮件黑名单与白名单：黑名单社区属性为 666、白名单为 42，运营于私有自治系统 AS65066，并以 OpenBGPD 为基础。（BSD Now EP1，[4554.19-4919.96]，L1）
- FreeBSD 基金会 2013 年春季筹款募集 219806 美元，来自 12 家企业与 365 名个人捐赠者；为维持 501(c)(3) 免税地位，个体小额捐赠被视为关键支撑。（BSD Now EP1，[1879.13-1939.54]，L2）

**史料**：

- OpenBSD 6.1 发布公告（BSD Now EP190，[72.92-87.54]，L1）
- FreeBSD ZFS vendor 分支导入提交（BSD Now EP190，[3892.42-4264.2]，L1）
- Kris Moore 访谈自述（BSD Now EP190，[3280.58-3714.9]，L1）
- Mike Muuss 的 ping 主页自述（BSD Now EP190，[4653.46-4908.5]，L1）
- Dennis Ritchie《The Evolution of the Unix Time-sharing System》（BSD Now EP190，[8.0-13.36]，L1）
- 当事人 Peter Hessler 自述其为 OpenBSD 用户与开发者：2000 年起使用、2008 年起成为开发者，早期从事 ports 移植，后加入 Vantronics 从事 OpenBSD 防火墙与路由器相关工作，并曾运行约 50 个路由域。（BSD Now EP1，[2946.18-3109.14]，L1）
- 当事人自述其 BGP SpamD 聚合阿尔伯塔大学与《The Book of PF》作者 Peter Hanstein 的 SpamD 黑名单，并以 24 小时内命中蜜罐邮箱地址作为黑名单收录口径。（BSD Now EP1，[3984.50-4100.90]，L1）

**史观**：

- 总纲10 动手者创造历史：Mike Muuss 一夜写就 ping 并补齐内核支持，说明关键工具常由具体动手者直接造就。（BSD Now EP190，[4653.46-4908.5]，L2）
- 总纲9 经验优先：OpenZFS 以特性在生产环境运行六个月作为接纳前提，经验验证先于理论采纳。（BSD Now EP190，[3415.94-3437.3]，L2）
- 总纲4 分离聚合是永恒规律：OpenZFS 特性先在 FreeBSD、illumos 等系统落地测试，再聚合回上游，体现分离聚合循环。（BSD Now EP190，[3396.02-3430.0]，L2）
- 总纲4 分离聚合是永恒规律：BGP SpamD 将阿尔伯塔大学与 Peter Hanstein 各自维护的黑名单聚合为统一的 BGP 分发列表，以本地复制取代中心网站下载与实时 DNS 查询，是分散源向聚合结构流转的具体实践。（BSD Now EP1，[4411.69-4474.51]，L1）
- 总纲8 本体论上各方平等：该期将 FreeBSD 图形驱动、OpenBSD BGP SpamD、NetBSD 6.1.1 等并列报道，未以单一分支为中心，呈现多方平等的叙事格局。（BSD Now EP1，[0.00-125.02]，L2）
- 总纲10 动手者创造历史：BGP SpamD 由 Peter Hessler 个人搭建并维护，访谈记录的是具体动手者对垃圾邮件防御工具的工程选择，而非抽象的项目叙事。（BSD Now EP1，[2946.18-3109.14]，L1）

**辨析**：

- [存疑脚注] ping“一晚写成”与 4.2a BSD 内核 ICMP 支持的时间线系作者自述，需与 4.2BSD 源码与 DARPA 会议记录交叉核验。 [存疑脚注] 单一来源自述，缺少独立档案印证。（BSD Now EP190，[4708.38-4780.22]，L4）
- VeriSign 同时使用 BSD、Linux、Solaris 等操作系统作多样性冗余的说法为主持人转述，其根服务器内部各系统的具体比例未获官方资料核验。 [存疑脚注] VeriSign 各操作系统在根服务器中的具体占比属单一播客转述，须以官方资料交叉验证。（BSD Now EP1，[460.01-478.53]，L4）

**文献**：

- [BSD Now EP190] Pennington J. BSD Now: 190: The Moore You Know[EB/OL]. (2017-04-19)[2026-08-15]. <https://www.bsdnow.tv/190>.
- [BSD Now EP1] Pennington J. BSD Now: 1: BGP & BSD[EB/OL]. (2013-09-04)[2026-08-15]. <https://www.bsdnow.tv/1>.

<!-- /PODCAST_REVIEW -->

<!-- dangan-20260908 消解回写 -->
- Jacobson. Congestion Avoidance and Control[C]. 1988. ［DKC-1059→fulltext:5783］
<!-- /dangan-20260908 -->