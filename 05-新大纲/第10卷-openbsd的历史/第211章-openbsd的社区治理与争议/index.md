---
chapter: 第 211 章
id: CH211
volume: 第10卷-openbsd的历史
---

# 第 211 章 openbsd的社区治理与争议

## 要点

- OpenBSD Top 5 贡献者：ajacoutot(35528)、deraadt(31454)、sthen(30592)、espie(18328)、jasper(16649)。de Raadt 独裁治理模式下的贡献者集中度

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3908] 卷“第10卷-openbsd的历史”第 211 章，匹配置信度 folder，原因：folder 第209章〔2026-09-13 整改注：folder 兜底匹配噪声，按目录名误配第 209 章（本文件为第 211 章），待生成器侧关闭 folder 兜底〕

- [DB:code_repos:openbsd.duckdb] OpenBSD Top 5 贡献者：ajacoutot(35528)、deraadt(31454)、sthen(30592)、espie(18328)、jasper(16649)。de Raadt 独裁治理模式下的贡献者集中度

## 史观

- 总纲7 理论必须自反：de Raadt 的独裁治理模式是对‘开源社区民主’神话的自反性挑战

## 辨析

- 再批评的合理性在不同叙事中评估不一——部分视为有效质疑，部分视为过度推演；【0 信任原则·前瞻性风险的辨析】“前瞻性风险”论证须区分“理论推演”与“事实考据”——de Raadt 年龄增长是事实，但年龄不等于能力衰退；BDFL 继任机制缺位是事实，但缺位不等于危机必然发生——须以具体证据而非理论推演评估风险；【0 信任原则·回顾性判断的限度】“31 年未出现 succession 危机”是回顾性事〔待核：原文截断，后文待回源〕
- 再批评的合理性在不同叙事中评估不一——部分视为有效质疑，部分视为过度担忧；【0 信任原则·结构性脆弱的量化】“结构性脆弱”论证须提供具体案例——2014 年电费危机是事实，但危机后的全球募捐（超过 100,000 USD）证明社区应对能力；若 OpenBSD 在 2014-2026 年间未再发生类似危机，则“结构性脆弱”可能是历史事件而非持续状态；〔待核：原文截断，后文待回源〕
- 合图不寻求消除张力而寻求呈现张力——BDFL 模式的“效率”与“脆弱”、“安全至上”的“产出”与“代价”、排外性文化的“严谨”与“排斥”、商业支持缺位的“独立”与“脆弱”是同一治理结构/工程哲学/文化氛围/资金模式的共生效应，不可分割；【0 信任原则·合图的非终结性】合图并非辩证链的终结而是阶段性综合，随 OpenBSD 治理演进（如 de Raadt 退出后的继任机制建立、资金模式的可能变化、社〔待核：原文截断，后文待回源〕
- 综合审视不意味着否定单一总纲的审视——第 13、19、21 条的视角各有侧重，第 13 条审视利益分配，第 19 条审视解释学循环与权力知识共谋，第 21 条审视革命改革路径分歧，三者交织但不可混淆；【0 信任原则·许可证哲学的语境辨析】OpenBSD **policy.html** 对 GPL 的批评（"it usually ends up hindering free sharing and〔待核：原文截断，后文待回源〕
- OpenBSD Foundation 年度报告考据须遵循 0 信任原则并以三段式呈现——【查证来源】（1）OpenBSD Foundation 官网 <https://www.openbsdfoundation.org/> 经 2026-07-23 检索，载明基金会基本信息、治理文件与年度报告链接；（2）OpenBSD Foundation 年度报告页面 <https://www.openbsdf……〔待核：原文截断，后文待回源〕

## 文献

- [DB:references_fulltext] 参考文献全文数据库（4077 篇全文，27138 条时间线事件）—— 对应 openbsd.duckdb

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP323、BSD Now EP273、BSD Now EP229、BSD Now EP623、BSDTalk EP123（共 5 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 计算机历史博物馆发布“最早 Unix 代码”周年源码版，收录 PDP-7 汇编清单（Space Travel、moo、井字棋等），经 Warren Toomey 与 John Mashey 等鉴定可溯至 1970 至 1971 年初。（BSD Now EP323，[167.90-366.7]，L2）[订正：原 [167.90-193.82]，2026-09-30 SenseAudio 重转核对]
- Leonard Kleinrock 受访回顾 1969 年 10 月 29 日 UCLA 发出的“LO”消息：他预见网络“始终在线、无处不在、不可见”，但未预见其社交化与国家安全化，并拒绝为创造互联网而后悔。（BSD Now EP323，[401.7-671.22]，L1）[订正：原 [486.68-671.22]，2026-09-30 SenseAudio 重转核对]
- OpenBSD 自 1995 年 10 月 18 日起跨过 40 万提交，Theo de Raadt 提醒计数口径不一；主持人补充 FreeBSD 约 92.5 万、NetBSD 加 pkgsrc 约 60 万，强调跨项目比较不可靠。（BSD Now EP323，[1095.24-1199.2]，L2）[订正：原 [1095.24-1167.46]，2026-09-30 SenseAudio 重转核对]
- Blacklistd 作为 fail2ban 替代，通过 libexec helper 与 NPF 联动按失败认证次数封锁 IP；教程演示 securelevel=1 下需把模块编入内核或经 modules.conf 预载。（BSD Now EP323，[685.00-1027.92]，L2）
- “OSI 七层墨西哥卷饼”作者自建 DoH 服务器与私有 CA，把 Firefox 的 TRR 指向本地，以对抗浏览器厂商对 DNS 的集中收编，而非简单禁用。（BSD Now EP323，[1862.22-2002.76]，L2）
- 文章追溯 cat 的源码史：Ken Thompson 与 Dennis Ritchie 于 1969 年在 PDP-7 上以汇编实现首版 cat，其中 getc 与 putc 的命名早于 C 标准库。（BSD Now EP273，[1440.78-1605.80]，L2）
- cat 的 C 实现迟至第七版 UNIX 才出现，4BSD 增加了一组沿用至今的命令行标志；最终由 Kevin Fall 在 1989 年为 Net/2 完成最后一次重写。（BSD Now EP273，[1651.48-1837.74]，L2）
- CSRG 将仍含 AT&T 代码的工具清单贴在墙上，供成员认领重写；Kevin Fall 认领 cat 与 mknod，其 1989 年版本成为 macOS 与 FreeBSD 现行 cat 的近源。（BSD Now EP273，[1800.70-1864.50]，L2）
- Xorg 服务器存在 CVE-2018-14665 提权漏洞，因命令行参数校验不当可覆盖任意文件；de Raadt 批评 X 维护者未提前告知 OpenBSD，致 6.4 发布即受波及。（BSD Now EP273，[2293.74-2489.74]，L2）
- 该期综述 OpenBSD、DragonFly BSD、NetBSD 对 Meltdown/Spectre 的响应：OpenBSD 引入微码更新工具，DragonFly 提交 MMU 隔离与 IBRS/IBPB，NetBSD 引入 Hot Patch 与 SVS 分离页表。（BSD Now EP229，[931.46-1482.64]，L2）
- IT Wire 报道 Theo de Raadt 的批评：仅一级厂商获得预先披露属选择性披露，并援引其 2007 年对 Intel 芯片设计问题的邮件。（BSD Now EP229，[695.8-835.26]，L2）
- 转述 Drew DeVault 的文章：追溯 1971 年 PDP-11 上 fork 的诞生、vfork 与 posix_spawn 的局限，以及 Plan 9 的 rfork 与 spawn 模型。（BSD Now EP229，[4297.5-4945.7]，L2）
- Ed Maste 提交使 LLD 成为 AMD64 默认引导链接器，标志 FreeBSD 用户态向非 GNU 工具链迁移的推进。（BSD Now EP229，[4975.44-5145.06]，L2）
- 采访 DragonFly BSD 用户：其因减少锁与高性能设计而选择 DragonFly，使用 HAMMER 的 undo 功能与快照、HAMMER2 的透明压缩。（BSD Now EP229，[2246.7-2489.82]，L1）
- FreeBSD Foundation 于 2025 年 4 月启动 SBOM 项目，目标是为整个源码树与软件包生成软件物料清单，服务于零信任构建与供应链合规需求。（BSD Now EP623，[309.72-553.78]，L2）
- Klara Systems 的夏季综述以自建 DNS、NTP、ZFS 存储与定制内核为主线，主张以开源标准摆脱厂商锁闭并降低长期成本。（BSD Now EP623，[557.22-1040.66]，L2）
- David Gwynne 自述通过 OpenBSD 的简短文档解决家庭拨号共享上网问题而入坑，后因 USB 2.0 备份需求开始向 OpenBSD 移植 NetBSD 的 USB 代码。（BSD Now EP623，[1122.34-1528.48]，L1）
- David Gwynne 主导的 sec(4) 把 IPsec 从流量窃取点改为可管理接口，使防火墙、队列、BPF 与 BGP 等常规工具可直接作用于隧道流量，服务于与 AWS 站点间 VPN 的对接。（BSD Now EP623，[2044.96-2309.56]，L1）
- David Gwynne 还实现 ERSpan 接口与 BPF 日志守护进程，以 GRE 封装远程端口镜像并支持 VMware 分布式虚拟交换机的监控会话。（BSD Now EP623，[2316.56-2663.62]，L1）
- OpenBSD hackathon 的社会维度被视为关键：面对面沟通能消除邮件与聊天中的误解，组织跨城市活动则面临资源协调的不确定性。（BSD Now EP623，[1544.20-1796.32]，L1）
- whurley 自述其受聘背景：此前在一家集群系统公司主导开源系统管理项目 OpenQRM，自称该项目为当时最成功的开源系统管理项目；又与他人共同创建 Open Management Consortium，推动各开源系统管理项目按用户需求协作而非以小团队对抗大厂商，统一代理模型等议题对 HP、IBM、CA 与 Nagios、Hyperic 等公司同等开放。BMC 管理层以此前工作为据，于 2007 年中聘其为开源战略首席架构师，要求他把开源做进商业模式而非营销点缀。（BSDTalk EP123，[220.66-308.98]，L1）
- BMC Developer Network 于本期采访当周（2007 年 7 月底）公布，定位为超越单纯发布压缩包（tarball）的用户沟通层：当周发布的集成产品均由用户参与完成；站内集成面向合作伙伴、用户与工程团队的跨越层（spanning layer），设有投票与直接反馈渠道，收录 Talk BMC 的博客与播客、下载区、集成引擎与权威软件库，并提供白皮书、文档与 API 技术资料。上线时未设公共源码仓库（无 Subversion 服务），代码完全自由下载，用户可提交修改；whurley 称社区尚未强烈要求设立仓库，是否自建仓库将由社区需求决定。（BSDTalk EP123，[453.3-826.3]，L1） [订正：原 首批四个集成项目与五个资源中心（Atrium、Foundation 等）细节及 [471.80-797.04]，2026-09-29 SenseAudio 重转核对]
- 关于 BMC 内部开源文化，whurley 评估称开发者的心态转变并非障碍：开发者如撰写 Adventures in Linux 博客的 Steve Carl 长期参与开源项目，公司历史上亦曾发布 CMFS、SQ log MD、MidWatch 等开源软件而不事声张；真正的挑战在于把这些既有贡献向外部社区公示并积累可信度。他援引 Karl Fogel 所著《Producing Open Source Software》中开放会引来公开批评的论述，并以自己在前雇主开放旧有专有代码时资深开发者被年轻学生公开指摘的经历，说明企业开源须正视此类社会性摩擦。（BSDTalk EP123，[884.04-1122.86]，L1） [订正：原 CMSFS、logMV，2026-09-29 SenseAudio 重转核对]

**史料**：

- 计算机历史博物馆“Earliest Unix Code”目录与 PDF，含 PDP-7 汇编、Space Travel 1970 源码页。（BSD Now EP323，[214.28-234.20]，L2）
- CBC《The Current》对 Leonard Kleinrock 的半小时访谈节选（首条消息“LO”及网络阴暗面）。（BSD Now EP323，[387.08-657.0]，L1）[订正：原 [387.08-402.72]，2026-09-30 SenseAudio 重转核对]
- Theo de Raadt 致 tech@ 的“OpenBSD 跨 40 万提交”邮件，说明计数困难与仓库历史歧义。（BSD Now EP323，[1100.92-1161.2]，L2）[订正：原 [1100.92-1113.56]，2026-09-30 SenseAudio 重转核对]
- unitedbsd.com 的 Blacklistd 与 NPF 教程，及 NetBSD securelevel 与 bpf-jit 配置说明。（BSD Now EP323，[693.04-812.78]，L2）
- 文章依赖 Unix History 仓库追踪 cat 自 1969 年以来的演进，并提及 macOS 10.0 从 NetBSD 引入 Kevin Fall 版 cat、10.5 起改用 FreeBSD 版 cat。（BSD Now EP273，[1459.66-2016.50]，L2）
- 提及 DistroWatch 的 NetBSD 8.0 评测：NetBSD 以高可移植性见长，文档分散于 FAQ、指南、手册页与 wiki，软件管理工具 pkg_add、pkgin、pkgsrc 并存易致新手困惑。（BSD Now EP273，[111.12-127.88]，L2）
- DragonFly BSD 的 Matthew Dillon 1 月 5 日关于 Meltdown 为 Intel 专属缺陷、AMD 免疫的帖子。（BSD Now EP229，[1015.3-1056.54]，L2）
- Theo de Raadt 2007 年 6 月 27 日的邮件线索（IT Wire 报道所引），涉及对 Intel x86 设计问题的早期批评。（BSD Now EP229，[807.38-835.26]，L2）
- Drew DeVault 的 fork 批评文章，以 1971 年贝尔实验室的 PDP-11 语境叙述 fork 的诞生。（BSD Now EP229，[4299.5-4438.76]，L2）
- FreeBSD 的 LLD bootstrap 链接器提交（Ed Maste 的提交信息，LLVM PR 23214 与 85 个依赖 issue）。（BSD Now EP229，[5056.46-5134.62]，L2）
- FreeBSD Foundation SBOM 项目公告。（BSD Now EP623，[309.72-553.78]，L2）
- Klara Systems 的 FreeBSD Summer 2025 Roundup。（BSD Now EP623，[557.22-1040.66]，L2）
- David Gwynne 访谈（University of Queensland，2025 年 5 月 29 日）。（BSD Now EP623，[1064.42-3319.38]，L1）
- 主持人片头新闻播报 OpenBSD Foundation 创建，宗旨为支持 OpenBSD 及相关项目；报道称大额捐赠经由新设渠道进行，小额个人捐赠仍沿用既有方式。此为该基金会 2007 年成立之初的当代播客记载。（BSDTalk EP123，[31.56-44.12]，L2）

**史观**：

- 总纲1 一切真历史都是古代史：50 年前的“LO”消息与 PDP-7 汇编被当作当下仍须考据的古代对象。（BSD Now EP323，[120.92-436.4]，L2）[订正：原 [120.92-125.14]，2026-09-30 SenseAudio 重转核对]
- 总纲5 没有必然性，只有偶然性：ARPANET 首条消息因机器崩溃停在“LO”而非“LOGIN”，是偶然事件。（BSD Now EP323，[421.34-425.12]，L1）
- 总纲19 解释学循环是历史认识的根本条件：源码断代依赖 Toomey、Mashey 等当事人回忆与目录残迹的循环解释。（BSD Now EP323，[167.90-193.82]，L2）
- 总纲8 本体论上各方平等：OpenBSD、FreeBSD、NetBSD 提交数被并置比较时，主持人强调口径差异，避免以数量定高下。（BSD Now EP323，[1161.86-1189.66]，L2）
- 总纲6 和解优于斗争：DoH 作者不以禁用对抗，而以自建本地 DoH 把集中化化解为自托管。（BSD Now EP323，[1972.26-1999.44]，L2）
- 总纲14 苦难不值得被提倡：Kleinrock 对网络阴暗面的回顾不美化早期“全员良善”的叙事，也不为创造互联网而后悔。（BSD Now EP323，[587.28-671.22]，L1）
- 总纲22 知识注定过时：cat 这种微小工具历经五十年、多次重写仍保持原始语义，说明计算机系统由层层叠叠的历史构件累积而成，而非不断推倒重建。（BSD Now EP273，[1369.22-1420.10]，L2）
- 总纲13 法律与道德是利益分配：为规避许可证而重写 cat 等基础工具，使“重写”成为法律边界塑造代码形态的例证，工具的功能未变而版权身份被替换。（BSD Now EP273，[1800.70-1853.22]，L2）
- 总纲8 本体论上各方平等：各 BSD 在 Meltdown/Spectre 面前的独立响应路径显示本体论上的多方平等，没有单一正确解。（BSD Now EP229，[1460.82-1482.64]，L2）
- 总纲13 法律与道德是利益分配：Theo 对 Intel 的批评强调选择性披露使大厂之外者受损，呈现披露秩序中的利益分配而非技术中立。（BSD Now EP229，[706.42-720.42]，L2）
- 总纲22 知识注定过时：对 fork 的批评把近 50 年的设计选择与内存过量承诺、OOM killer 等后果联系起来，呈现旧有设计在当下的历史惯性。（BSD Now EP229，[4516.04-4624.68]，L2）
- 总纲10 动手者创造历史：David Gwynne 以大学系统管理员身份亲手修复基础设施问题并回馈 OpenBSD，体现一线操作者推动协议与工具演进。（BSD Now EP623，[1806.76-1946.58]，L1）
- 总纲6 和解优于斗争：OpenBSD hackathon 以面对面沟通消解邮件分歧，强调协作而非对抗的社区机制。（BSD Now EP623，[1580.48-1651.24]，L1）
- 总纲4 分离聚合是永恒规律：sec(4) 将 IPsec 从网络栈中窃取流量的分离点改造为可聚合进接口体系的组件。（BSD Now EP623，[2049.28-2316.56]，L1）
- 总纲13 法律与道德是利益分配：whurley 将许可证选择表述为利益分配安排：BMC 实行单一宽松许可证政策，一律采用 BSD 许可证，理由是多项目多许可证并存会令集成者陷入法律泥潭；他认为 GPL 附加的限制越多，与日益追求自由的开发者社区越处于对立，而 MPL 的署名条款为 BSD 版权声明所天然涵盖，并无必要。其论证把许可证从技术授权文件还原为权利在作者、用户与商业再利用者之间的分配方案。（BSDTalk EP123，[1122.86-1320.06]，L1）
- 总纲3 不存在进步，只有权力再分配：whurley 提出“开放是开关状态，不能半开”：真正的开放须允许合作伙伴以 BSD 代码构建商业产品出售且不必回馈变更，回馈义务只存在于其与更大社区之间。他以此区分“控制”与“影响”——BMC 求影响而不求控制社区，并指其他限制性许可证难以围绕项目形成可持续生态。这是企业主动放弃代码控制权、换取社区影响力的权力关系再安排。（BSDTalk EP123，[1293.84-1407.58]，L1）
- 总纲15 文化即形式主义：whurley 断言专有软件与开源软件在代码本体上并无差别——都需许可证、代码与编译——差别全在社区与互动方式，即如何从用户收集信息、如何支持用户、如何促成联结；他引 Henry Louis Gates 语“收集数据只是走向智慧的第一步，分享数据才是走向社区的第一步”，指出企业以为开源代码即可坐等社区前来，是误置了共同体的位置。（BSDTalk EP123，[1514.58-1546.38]，L1）

**辨析**：

- OpenBSD 的 40 万提交仅为一种测量口径，仓库历史久、有缺失 changelog 与不可转换分支，任何计数都可能高估或低估。 [考据脚注] Theo 本人与主持人双重提示计数不可靠（BSD Now EP323，[1131.88-1154.46]，L3）
- PDP-7 源码断代“1970 至 1971 初”依赖两位早期贡献者与馆方编目，属多源交叉但仍非绝对定年。 [存疑脚注] 定年证据链为多源交叉，非单一权威结论（BSD Now EP323，[167.90-193.82]，L3）
- 文章称 cat 的首版 C 实现“迟至第七版 UNIX 才出现”与“4BSD 标志集 38 年未变”等细节系二手转述，须与 TUHS 归档的早期 cat 源码逐版核对。 [存疑脚注] 各版本 cat 的实现时间线未经一手源码逐版核验。（BSD Now EP273，[1651.48-1800.70]，L4）
- de Raadt 对 X 安全团队协调不力的批评属当事人立场，其“提前一小时才通知”的表述须与 X 安全团队与 OpenBSD 的往来记录交叉核实。 [存疑脚注] 披露时间线仅来自 OpenBSD 一方叙述。（BSD Now EP273，[2430.02-2489.74]，L4）
- 对 fork 的批评系博客作者个人立场，节目主持人在结尾补充“无法改变应用使用习惯”的采纳难题，替代方案在 FreeBSD 仅停留在讨论阶段。 [存疑脚注] 系单一来源的个人技术立场（BSD Now EP229，[4888.6-4949.3]，L4）
- Theo de Raadt 对 Intel 的指控（“被告知忽略风险”）系其个人推断，无直接证据，节目亦未提供 Intel 回应。 [存疑脚注] 系个人推断，无直接证据（BSD Now EP229，[763.4-807.38]，L4）
- 转录将 David Gwynne 记作 David Gwynn 或 David Gwendt，标题 Two‘s interview 疑为 Gwynne’s interview 的转写偏差，人名以 OpenBSD 官方为准。 [存疑脚注] 人名与标题存在语音转写偏差，须以 OpenBSD 官方资料核验（BSD Now EP623，[1068.26-1075.34]，L4）
- sec(4) 相关表述中 IPsec 接口在转录混用 sec 与 sec4，具体版本与接口名须以 OpenBSD 手册页核验。 [考据脚注] 接口名称存在转写混用，须以 sec(4) 手册页为准（BSD Now EP623，[1971.80-2235.62]，L4）
- 转写中的若干专名存疑：whurley 所自述的原雇主转写作 Clusters，与通行记载（OpenQRM 源自 Qlusters 公司）存在疑似转写误差，采用前须以邮件列表档案与企业传记材料交叉核对；新转写中 Nagios 创始人作 Ethan Galstad、另提及前雇主转写作 Symantec（并涉 OpenSense 安全基础设施管理系统与 Jim Nasby、Decibel 等合作者），与通行记载一致；另其关于 GPL 与开发者社区相悖的判断系单方立场陈述，历史评价应与 GPL 阵营当事人论述对读。 [存疑脚注] 转写专名 Clusters 疑为语音识别误差，未经外部来源确证；whurley 的反 GPL 论断属单一来源立场推断。（BSDTalk EP123，[1429.02-1460.30]，L4） [订正：原 Symbia 与 Ethan Volstead 名目，2026-09-29 SenseAudio 重转核对]

**文献**：

- [BSD Now EP323] Pennington J. BSD Now: 323: OSI Burrito Guy[EB/OL]. (2019-11-07)[2026-08-15]. <https://www.bsdnow.tv/323>.
- [BSD Now EP273] Pennington J. BSD Now: Episode 273: A Thoughtful Episode | BSD Now 273[EB/OL]. (2018-11-23)[2026-08-15]. <https://www.bsdnow.tv/273>.
- [BSD Now EP229] Pennington J. BSD Now: 229: The Meltdown of Spectre[EB/OL]. (2018-01-17)[2026-08-15]. <https://www.bsdnow.tv/229>.
- [BSD Now EP623] Pennington J. BSD Now: 623: Two's interview[EB/OL]. (2025-08-07)[2026-08-15]. <https://www.bsdnow.tv/623>.
- [BSDTalk EP123] Backman W. BSDTalk: 123: bsdtalk123 - William “whurley” Hurley, Chief Architect of Open Source Strategy at BMC Software, Inc.[EB/OL]. (2007-07-30)[2026-08-27]. <https://bsdtalk.blogspot.com/2007/07/bsdtalk123-william-whurley-hurley-chief.html>.

<!-- /PODCAST_REVIEW -->
