---
chapter: 第 280 章
id: CH280
volume: 第14卷-商业生态与企业案例
---

# 第 280 章 bsdl与gpl反批评的再批评

## 要点

- 专利授权（GPLv3 明确，BSDL 默示）、合规成本（GPL copyleft 触发需评审，BSDL 零成本）、Google v. Oracle (2021) 确认接口不受版权保护，缩小了两者法律风险差距。
- **要点**：从项目史观总纲第 13 条 “法律与道德是利益分配”、第 19 条 “解释学循环是历史认识的根本条件”、第 21 条 “革命与改革是历史方法论的分歧” 切入，**BSD** 商业化模式争议的本质是利益分配的法律形式主义、前理解差异的不可调和、改革方法论的整体呈现——其一，从总纲第 13 条切入，**BSD** 商业化模式的批评与反批评本质是利益分配的法律形式主义——**BSDL** 的 “无回馈条款”、`committer` 权限平等原则、**FreeBSD Foundation** 的 **IRS** **501(c)**

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3872] 卷“第14卷-商业生态与企业案例”第 280 章，匹配置信度 folder，原因：folder 第279章
- [DB:references_fulltext:chapter_matches:chmatch_3982] 卷“第14卷-商业生态与企业案例”第 280 章，匹配置信度 folder，原因：folder 第279章
- [DB:references_fulltext:chapter_matches:chmatch_3983] 卷“第14卷-商业生态与企业案例”第 280 章，匹配置信度 folder，原因：folder 第279章
- [DB:bsdnow_podcast:outline_mappings:om_10481] BSD Now 第 665 期，匹配 CH280 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10545] BSD Now 第 654 期，匹配 CH280 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10582] BSD Now 第 646 期，匹配 CH280 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10643] BSD Now 第 637 期，匹配 CH280 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10776] BSD Now 第 617 期，匹配 CH280 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11150] BSD Now 第 571 期，匹配 CH280 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11213] BSD Now 第 563 期，匹配 CH280 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11364] BSD Now 第 546 期，匹配 CH280 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11442] BSD Now 第 536 期，匹配 CH280 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11542] BSD Now 第 526 期，匹配 CH280 章，关联度 1.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 考据过程留痕——【查证来源】项目史观总纲第 13、19、21 条原文经 据原文第 25 章 第 13、19、21 行 Read 一手核验（2026-07-23）；**BSD 2-Clause** 原文经 **<https://www.freebsd.org/copyright/freebsd-license/>** 一手核验（2026-07-23）；**Linux** 内核 **COPYING**

## 文献

- Google v. Oracle; FSF 指南 ［A］## 史料考据补充（2026-08-04 任务3 联网核验）> 主题：BSD 许可/商业
- 项目史观总纲第 13、19、21 条（见 据原文第 25 章）；**BSD 2-Clause** 原文；**GPL** 原文；**Linux** 内核 **COPYING** 文件（torvalds/linux 仓库）；**Committer‘s Big List of Rules**；**FreeBSD Committer’s Guide**；**FreeBSD Foundation** **IRS** **990** 表；freebsd.duckdb L3.2.1/L3.2.2 查询报告；**Berlin** I. “Two Concepts of Liberty”（1958）；**TrueNAS** 2025 迁移公告；上述 278.38.1-279.38.5 引用的综合文献 ［A］

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSDTalk EP146（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Cornell 的多系统履历与 OpenSolaris 评价：2002 年自 Linux 入 Unix 之门，Solaris 9 曾免费下载（付 20 美元媒体费）但驱动支持贫弱而搁置，至 Solaris 10 渐趋稳定方回归 OpenSolaris；FreeBSD 使用更久，另试过至少 20 个 Linux 发行版、三大 BSD、DragonFly、Mac 与桌下的 SGI Irix 工作站。OpenSolaris 包管理仍是 SVR4 体系、无 ports 对应物、包可得性不及 FreeBSD，开发模式仍偏整体式，GNOME（JDS）以 tar 包加升级脚本发行被他评为主旧；Sun 营销与专利相关的许可证对部分开发者有诱惑，但 Linux 用户基数更大、开发更稳，他不认为 OpenSolaris 会威胁 Linux 或 BSD。（BSDTalk EP146，[152.16-403.44]，L1）
- NVIDIA 驱动的平台差异：Solaris 与 OpenSolaris 因 NVIDIA 与 Sun 的协议随系统附带驱动（其 Quadro FX 1500 开箱即用），FreeBSD i386 则须经 ports 或厂商文件手动安装，性能上 OpenSolaris 与 FreeBSD 相当、略逊于开发主力所在的 Linux；OpenSolaris X11 团队移植的 DRI 仅覆盖驱动全开的 Intel 卡，NVIDIA 走自有 DRI 与 GLX 实现；FreeBSD 7 对他的桌面拦路虎是 AMD64 平台缺 NVIDIA 驱动——他引 2006 年 FreeBSD 邮件档案中 NVIDIA 团队来信：系统缺少若干内核接口，致其无法对 FreeBSD 驱动执行质量管控，原称 FreeBSD 7 应予解决但此后再无音讯。 [存疑脚注] 转写作 curl interfaces，据语境应为 kernel interfaces（内核接口），待以原始邮件核证（BSDTalk EP146，[488.12-593.14]，L1）
- 编解码与专有依赖的桌面张力：MP3、MPEG 等专利编解码非自由，部分发行商付费授权却受 GPL 链接要求牵制，须手动取用或启用（如 GStreamer 前端）；VirtualBox 有与 VMware 竞争之势但当时无 64 位支持；他自认非纯粹主义者（采访需要时会用 Skype），最盼望的专有软件是 Adobe Flash、VMware Workstation/Server 与 Skype；Java 侧 FreeBSD Foundation 提供略旧的 Sun Java 版本、OpenJDK 则是获得新版之路；Gnash 兼容性尚不足生产使用；Skype 即便在 OpenSolaris 也依赖其专有中转服务器，SIP 路线则需软电话与企业级 SIP 支撑而显凌乱；Solaris 发行版自带 Flash 且 Mozilla Firefox 可用（FreeBSD 仅限 Opera），用户基数是厂商是否开放支持的关键变量。（BSDTalk EP146，[603.84-817.64]，L1）
- 流行度辩证与统计困难：BSD 没有 Linux Counter 一类可比统计（后者还混入服务器与高校实验室工作站），只能依赖 web 统计，OpenSolaris 数字只能听 Sun 的而营销另有说辞不可尽信；流行度仅在指望厂商递交专有软件时才重要，若不依赖厂商之“礼”，开发者是两人还是千人并不影响开发延续；开源替代品如 Gnash 已尽力但未达标，而 Adobe 专有 Flash 持续变异、如 Wine 对付 Windows 二进制般是移动目标；专有依赖在换平台时暴露无遗——开源系统几乎能跑任何古怪硬件，SGI 已掐死 Irix 平台，开源软件却仍能在其上编译，NetBSD 反倒在 2001 年的“新”板卡上犯难。（BSDTalk EP146，[843.12-1000.80]，L1）
- 协议标准化的先例与反事实：Will 感慨开源与其追赶专有规格不如自提灵活而流行的替代规格，然而这系于流行度，而流行度是“恶”的；他举 SMTP 先例——各厂商专有邮件系统互不兼容，最终人人臣服于处处可用的协议；Cornell 则给出反事实：1981 年 BSD TCP/IP 因自由（无 GPL 式负担）而被普遍采纳，若当年 BSD TCP/IP 栈是 GPL，将无人采纳，互联网也不会如此互联；两人随即征集开源设定标准的例子，Cornell 举 Evince（遍及 BSD 与类 Unix、新增表单编辑）、Adobe 开放 PDF 规格之举，并评 ODF 进展有限。（BSDTalk EP146，[1050.44-1182.26]，L1）

**史料**：

- 口述可考的一手物件：2006 年 FreeBSD 邮件档案（Piper Mail）中 NVIDIA 团队说明 AMD64 驱动受阻于缺失内核接口的信件（受访者引述）；FreeBSD Foundation 发行的 Sun Java 旧版与 OpenJDK 途径；Solaris 9 的 20 美元媒体费下载；主持人自述在波士顿 Micro Center 见证 PC-BSD 与该连锁达成的零售上架协议（当场未寻得货品）并购得 FreeBSD 6.2 CD 套装。 [存疑脚注] PC-BSD 零售协议仅见主持人口述，属单一来源，待以其他史料核证（BSDTalk EP146，[573.32-593.14]，L1）

**史观**：

- 总纲4 分离聚合是永恒规律：SMTP 先例与 BSD TCP/IP 的普遍采纳被两人共同读作分而后合的过程：各专有邮件孤岛最终聚合于通用协议，1981 年的自由 TCP/IP 使异构系统聚合为一张互联网——分离聚合在协议史与网络史中反复显形。（BSDTalk EP146，[1076.92-1091.30]，L1）
- 总纲3 不存在进步，只有权力再分配：流行度被两位参与者共同辨认为一种权力分配而非价值优劣：用户基数决定厂商向谁递交专有软件之“礼”，BSD 侧统计阙如、声量弱势，其回应之道是不依赖此礼而以开发者自足延续——竞争语境中的份额差异由此被还原为权力布局而非技术高下。（BSDTalk EP146，[887.94-915.14]，L1）

**辨析**：

- 多处转写须校正：OpenCeleris、Slarice、open-stolaris 均应作 OpenSolaris/Solaris，curl interfaces 应为 kernel interfaces，muscle fire foxes 应为 Mozilla Firefox，opair 应为 Opera，nepiosity 应为 NetBSD，Evans Reader 应为 Evince，Neville 应为 Novell；BSD TCP/IP 若为 GPL 的反事实属民间历史假设，无当年采纳决策文档佐证，只可作观点引用而不可作史实；PC-BSD 的 Micro Center 上架协议为单源口述，2008 年 4 月时点的 NVIDIA 驱动状态亦须以后续 FreeBSD 发行说明复核。 [存疑脚注] 反事实陈述与零售协议均为单一来源；转写名物辨识待核（BSDTalk EP146，[1105.18-1120.72]，L4）

**文献**：

- [BSDTalk EP146] Backman W. BSDTalk: 146: bsdtalk146 - James Cornell[EB/OL]. (2008-04-07)[2026-08-27]. <https://bsdtalk.blogspot.com/2008/04/bsdtalkalk146-james-cornell.html>.

<!-- /PODCAST_REVIEW -->