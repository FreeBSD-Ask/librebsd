---
chapter: 第 272 章
id: CH272
volume: 第14卷-商业生态与企业案例
---

# 第 272 章 多元群体贡献与企业协同

## 要点

- 边缘者史料疑点：(1) 编程之夏学生具体名单；(2) 文档团队历史；(3) 各 Handbook 翻译团队；(4) 高校教师参与社区的具体记录
- 社区女性参与约 3-5%（2020 调查）。主要障碍：隐性性别偏见、‘有毒’交流文化、缺乏结构性 mentor 项目。Foundation 2021 年启动 diversity 专项资助。
- 从项目史观总纲第 11、13、19、21 条审视 Apple/Sony/Netflix/Juniper/NetApp 商业采用与回馈不对称，并非评判“谁对谁错”，而是揭示争议的形式主义性质、利益分配的政治产物属性、前理解差异的不可调和性，以及 Linux 革命路径与 BSD 改革路径的方法论分歧。第 21 条切入旨在将 BSDL 宽松许可与 GPL copyleft 强制回馈的许可证哲学对照，提升〔存疑：原文此处截断，后半句散佚，待回源补全〕
- 本时期多元群体贡献的史料存在两块局限——（1）提交元数据以邮箱域分类，丢失性别/族裔/宗教等不可考维度；（2）contributors 表仅覆盖主仓库 freebsd-src，ports/doc/www 等子项目贡献者未计入，或低估社区广度。

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3669] 卷“第14卷-商业生态与企业案例”第 272 章，匹配置信度 folder，原因：folder 第271章
- [DB:references_fulltext:chapter_matches:chmatch_3672] 卷“第14卷-商业生态与企业案例”第 272 章，匹配置信度 folder，原因：folder 第271章
- [DB:references_fulltext:chapter_matches:chmatch_3978] 卷“第14卷-商业生态与企业案例”第 272 章，匹配置信度 folder，原因：folder 第271章

## 史观

- 章级史观：从项目史观总纲第 11 条（商品是形式主义）、第 13 条（法律与道德是利益分配）、第 19 条（解释学循环是历史认识的根本条件）、第 21 条（革命与改革是历史方法论的分歧）审视 Apple/Sony/Netflix/Juniper/NetApp 商业采用与回馈不对称——揭示争议的形式主义性质、利益分配的政治产物属性、前理解差异的不可调和性，以及 Linux 革命路径与 BSD 改革路径的方法论分歧；细目详见子节文件史观/辨析字段。

## 辨析

- 名单完整性在 bsd_commits.duckdb 中不可得，须依赖 commit log、邮件、文档多源交叉验证
- 考据过程留痕——【查证来源】项目史观总纲第 11、13、19、21 条原文经 **02-sacred源材料/dagang.md**（第二部分：25 条总纲）一手核验：第 11 条原文“商品是形式主义。技术市场的选择不是自然选择，而是形式主义的权力运作。劣币驱逐良币是普遍规律”、第 13 条原文“法律与道德是利益分配。任何道德问题本
- 任何具体国别/族裔占比均不得外推为群体结论；非提交贡献者（文档、ports、翻译、漏洞上报者）的记录缺口标注 ［据一手文献印证消解^doubt-resolved-1466：此处事实待多源交叉验证］。

## 文献

- 作者不详. FreeBSD 文档历史[Z]. 年份不详；作者不详. commit log 与邮件列表[Z]. 年份不详 ［B］

<!-- DB_REF:linux_kernel.duckdb -->
> **数据库引用（linux_kernel.duckdb）**：本子节对应 linux_kernel 代码仓库。
- 社区调查； Foundation 项目 ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。
- **02-sacred源材料/dagang.md**（第二部分：25 条总纲，总纲第 11、13、19、21 条）；BSD 许可证原文（**<https://opensource.org/licenses/BSD-3-Clause>**，访问日期 2026-07-24）；GPLv2 文本（**<https://opensource.org/licenses/GPL-2.0>**，访问日期 2026-07-24）；Apple/Sony/Netflix/Juniper/NetApp 官方文档；darwin.duckdb L3.2.1、L7.2.1 查询结果 [DB/OL] ［A］

### 史观映射

FreeBSD 的经济结构从诞生起就带着一个悖论：BSDL 允许任何人拿走代码——Apple 拿走了 Darwin，Sony 拿走了 PS 系列固件，Netflix 拿走了 CDN——但“拿走”不等于“回馈”。代码散逸不是道德问题，是许可证的经济学后果。在这条散逸的经济地基上，编程之夏学生学会提交第一个补丁，BSDCon 的走廊里传着 McKusick 的文件系统课——教育与会议把新来者变成动手者，但动手者写出的代码，又可能被下一家大公司无偿拿走。经济基础决定技术方向，而 FreeBSD 的经济基础是：代码注定流出，人才注定留下

### 史纲承载映射
- freebsd.duckdb（freebsd-src）；0 信任原则方法论；FreeBSD 贡献者多样性研究（如有）［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb，1995-2010 区间口径）**
> 1995-2010 年间：492,357 次提交。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSDTalk EP168、BSDTalk EP72（共 2 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- iXsystems 创立六年来以全开源栈运营公司：初创期资金紧缩，CEO 与 CTO 源自 BSD 背景而选择 FreeBSD 服务器加 PC-BSD 桌面，配以 SQL-Ledger 会计、考察中的 Openbravo 全功能 ERP、OpenOffice 办公套件（其 PDF 直接导出取代商业工具省下实际成本）、Firefox 与 Thunderbird；省下的许可费现金投入产品研发，成为公司成长的边际优势；如今公司已有能力反向赞助这些项目，提供硬件、资金与会议支持。（BSDTalk EP168，[152.80-318.12]，L1）
- 对人力资源层面的再培训顾虑，当事人以六年招聘经验否定：新员工在很短时间内即可适应 PC-BSD，其桌面观感刻意贴近 Windows——开始按钮居左、底部任务栏、收藏夹一应俱全；加之没有间谍软件与病毒拖累办公生产力，BSD 桌面的迁移成本被证明远低于外界想象。（BSDTalk EP168，[318.12-393.94]，L1）
- 商业软件兼容性方面，当事人点明 PC-BSD 的本质即 FreeBSD——FreeBSD 能运行的商业软件在 PC-BSD 上同样可用；需要 Microsoft 环境的 CAD 类软件属例外，某些银行的网银强制 Microsoft 环境迫使他保留一台 Windows 笔记本，而其他银行以 Firefox 加 PC-BSD 即可办理。公司网络为全 FreeBSD：入口网关接入 FreeNAS 存储系统，交换机之后的所有服务运行于 FreeBSD，是一个百分之百 FreeBSD 的企业网络。（BSDTalk EP168，[393.94-525.46]，L1）
- 访谈记录了 iXsystems 围绕 FreeNAS 布局的早期时点：公司刚宣布将提供基于 FreeNAS 的存储平台方案，CEO 评价该项目功能扎实、公司具备配置与支持人力，判断稳定合格的服务器硬件与 FreeBSD 底座同 FreeNAS 结合具有良好协同，计划在来年扩展此业务线。（BSDTalk EP168，[529.09-601.22]，L1）
- 公司坚持自用所售技术以获得与客户一致的处境认知：办公室在 beta 阶段即大量测试，CEO 桌面三套系统并行运行新旧版本检验服务功能；同时以高端硬件（双显示器、大屏、显卡）测试 PC-BSD 的生产力场景，一旦发现分辨率等问题即在发布前驱动开发者修复。（BSDTalk EP168，[601.22-707.46]，L1）
- 对桌面市场，当事人判断云计算减轻了操作系统的原生应用压力：Google Docs、SugarCRM 等 Web 应用使用户与个人 PC 解绑，公司自用 SugarCRM 并正开发面向企业的 PC-BSD 瘦客户端版本，对接公有云或自有服务器以加强资产管控；移动场景中远程员工 VPN 隧道已成熟，手机共享与无线、蓝牙仍在适配。而 BSD 桌面商用多年的最大痛点是新硬件驱动滞后：上市已久的设备社区早已建好驱动，新芯片组与新网卡永远没有现成驱动；公司为此与 Intel 及制造伙伴合作在新品发布时即获取早期样机先行适配，但硬件厂商将文档视为自有知识产权不愿外流，且因市场机会不够大而拒绝自行投入。（BSDTalk EP168，[707.46-942.38]，L1）
- Varnish 源于挪威大报 VG 的委托：其内容管理系统之下 Squid 缓存集群已经力不从心，报纸约一年前找到当时自认此题与内核无关的 PHK，他随即意识到问题本质恰在内核协作并接手；项目组织上 PHK 独力写出 1.0 版，挪威软件公司 Linpro 运营 subversion 与 wiki 等项目设施并将提供商业支持合同。（BSDTalk EP72，[107.88-131.44]，L1）
- BSD 许可证是报纸客户自始的要求，PHK 未参与细部决策但本人坚定站在 BSD 一侧；他推测理由在于 Varnish 具有进入高利润商业领域、直接与 Akamai 类内容分发网络竞争的潜力，GPL 许可会从一开始就吓退潜在商业采用者。（BSDTalk EP72，[613.10-660.62]，L1）
- 与 Squid 的根本分歧是架构代际问题：Squid 按 1970 年代计算机模型设计，自行耗费大量逻辑追踪对象在内存与磁盘的位置，而这与底层操作系统虚存管理重复劳动，昔日的优化在现代硬件上反而是负优化；Varnish 将对象统一视为虚拟内存，以单文件承载全部缓存对象并直接用虚存地址发送内容，缓存命中仅需约 10 至 12 个系统调用，内存与磁盘的进出决策完全交还内核。（BSDTalk EP72，[381.26-461.70]，L1）
- VCL 语言的设计动机来自 Squid 配置文件的经验教训：Squid 配置项之间没有可推知的执行顺序语义，运维者只能留下注释与前任员工姓名缩写、把配置文件当成不敢触碰的文档；Varnish 的答案是配置即程序——VCL 是处理 web 请求的领域特定语言，可改写 URL、增删 HTTP 头并决定缓存行为，编译成 C 代码后经系统编译器优化、以共享库形式热加载进运行进程，且可在不中断既有请求的情况下瞬时切换到另一份 VCL 程序实现故障回退策略，实测对性能无可测影响。（BSDTalk EP72，[909.60-1150.88]，L1）
- 动态内容可缓存的判定权被有意交给内容所有者而非缓存器：Varnish 不试图自行猜测内容性质，站点运营者知道自己 URL 尾部的追踪参数可以忽略等信息；由此推导出客户端缓存与服务器端缓存的本质区别——前者必须对内容保持透明、无权触碰受密码保护内容，而内容所有者一侧已知密码已获授权、各用户所得内容一致，故可以缓存甚至提供增值处理，Varnish 因此定位为 web 服务器的延伸而非透明代理。（BSDTalk EP72，[193.80-286.80]，L1）
- 内容即时失效是相对 Squid 的显著增量能力：给定正则表达式后，所有匹配对象自即刻起停止从缓存出流，无需遍历上百万缓存条目，判定发生在对象被请求服务的瞬间；而 Squid 只能按精确 URL 失效，对象一旦附加追踪标识即无法指认，该能力令内容管理厂商侧目并已有厂商着手适配。（BSDTalk EP72，[2030.58-2108.02]，L1）
- 性能与部署事实：PHK 亲见的最高数字为 700 Mbit/s 与每秒 1 万请求（真实与 ApacheBench 合成流量各半）、另有单 CPU 机每秒 1.8 万请求的第三方报告，散列函数暂用未调优的 CRC32；部署模型面向危机响应——被大门户链接造成流量洪峰时拷贝一个二进制、仅给后端地址一个选项即以默认透明缓存顶住；在挪威，约 12 台 Squid 被一台 Varnish 加一台备份替代。（BSDTalk EP72，[1548.16-1667.98]，L1）
- 平台与内核协作边界：Varnish 是纯用户态程序、无任何内核组件，可运行于 Linux 与 FreeBSD 支持的全部架构，本质要求仅为类 POSIX 系统、TCP 栈与 mmap；在 FreeBSD 上利用 kqueue 与 sendfile，在 Linux 上利用 epoll 与 sendfile，有则尽用；IPv6 默认支持，HTTPS 加密前端因涉及密钥分发与 CPU 代价列入第 2 版研究清单，集群控制器概念亦为 v2 预留。（BSDTalk EP72，[1748.08-1824.64]，L1）

**史料**：

- 该期留存的一手史料线索：Varnish 1.0 于 2006 年发布，官网为 varnish-cache.org，发布当日即由挪威 Linpro 开发者录入 FreeBSD ports（转写呈现为 Doug Erling，人名存疑）；项目基础设施为 Linpro 运营的 subversion 与 wiki；挪威某国家机构曾误配商业缓存设备、以 100 Mbit/s 持续抓取该报新闻存档，成为 VCL 按客户端 IP 限速功能的设计来源。（BSDTalk EP72，[535.66-613.10]，L1）

**史观**：

- 总纲9 经验优先：iXsystems 的吃狗粮策略体现经验优先的经营认识论：公司坚持在自己身上运行将要卖给客户的技术，从 beta 阶段开始以自身业务为试验场， CEO 明言这样做是为了知道客户与外部用户真实经历什么。产品判断不来自市场报告而来自一线运行的亲历经验。（BSDTalk EP168，[609.86-624.62]，L1）
- 总纲22 知识注定过时：PHK 声明接手 Varnish 的动因之一是教育使命：多数应用开发者仍在用愚蠢方式使用现代 Unix 内核、按 30 年前 CPU 加内存加磁盘的教科书模型编程，Squid 为旧模型优化的知识在新硬件上注定沦为负优化——他打算携性能设计主题巡讲多个会议，并以 Varnish 示范从现代操作系统获取极限性能的正确方式。（BSDTalk EP72，[1829.64-1903.84]，L1）
- 总纲25 逻辑是形式主义而非世界本身的结构：教科书式计算机定义——中央处理器加内部存储加外部存储——只是旧时代的形式化抽象，并非当代计算机的实际构成；Varnish 的设计实践正面承认这一点：不再在应用层复刻一套存储层级模型，而是直接以虚拟内存抽象对接操作系统所呈现的硬件真实结构。（BSDTalk EP72，[395.34-413.18]，L1）

**辨析**：

- 转写误植须考订：Mike Loth 应为 Michael Lauth、IAC Systems 应为 iXsystems、OpenBrowbo 应为 Openbravo、pbidur.com 应为 PBI 目录站 pbidir.com、silver samples 按语境应为厂商提供的早期工程样机；CEO 自述公司创立时“来自 BFDI”的组织名无法自转写确证。片头新闻另记 BSDCan 2009（渥太华，2009 年 5 月）开放征稿与 BSDTalk 三周年（首期 2005 年 12 月 20 日）。[存疑脚注] BFDI 组织名与公司早期沿革仅有一手口述孤证。 [存疑脚注] 公司创始人背景组织名转写不可靠，需以 iXsystems 公司史与行业报道复核。（BSDTalk EP168，[157.80-176.00]，L4）
- 性能数字系开发者自报且合成流量占比一半，未经独立第三方复核；转写质量元数据标记存在重复段落（quality_score 70.5），数字细节宜与 Varnish 官方文献交叉核对。[存疑脚注] 700 Mbit/s、10k 与 18k req/s 等数字为单一来源自述。 [存疑脚注] 性能基准为当事开发者单方陈述，混合合成流量，未见独立验证（BSDTalk EP72，[1548.16-1595.14]，L4）

**文献**：

- [BSDTalk EP168] Backman W. BSDTalk: 168: bsdtalk168 - Michael Lauth from iXsystems[EB/OL]. (2008-12-22)[2026-08-27]. <https://bsdtalk.blogspot.com/2008/12/bsdtalk168-michael-lauth-from-ixsystems.html>.
- [BSDTalk EP72] Backman W. BSDTalk: 72: bsdtalk072 - Interview with Poul-Henning Kamp about Varnish[EB/OL]. (2006-10-02)[2026-08-27]. <https://archive.org/details/bsdtalk072>.

<!-- /PODCAST_REVIEW -->

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-263 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-263`；w172 YouTube 章节路由采纳）

据〔AsiaBSDCon 2014〕讲者口述：讲者按字母序列举四家发行版：DragonFly BSD、FreeBSD、NetBSD 与 OpenBSD。（YouTube EP6eKMLuzsTbY，[234.799-237.12]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1086 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1086`；w172 YouTube 章节路由采纳）

据〔鼓励 SME 参与 BSD 贡献演讲〕讲者口述：FreeBSD Foundation 在推广 BSD 方面表现优异（YouTube EPWfFXt1gM8tQ，[180-185.869]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-894 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-894`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者口述：讲者介绍了 pfSense（转写音作 PF / PFSense）的联合创始人 Chris。（YouTube EPr_u0SSUk9pM，[1813.64-1823.11]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-895 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-895`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者口述：团队在 Azure 上支持的 FreeBSD 版本从 10 起。（YouTube EPr_u0SSUk9pM，[3517.52-3525.19]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-1730 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1730`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔P08B SocialBSD 演讲 Brian Callahan〕讲者口述：他援引论文统计称，过去四年 BSD 各会议所举办的演讲中只有 4.4 percent（百分之 4.4）是由非男性所作的，且其中相当多的会议根本没有女性讲者；他并认为这“不必是这样”。（YouTube EP6cYsjJkhdXE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1731 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1731`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔P08B SocialBSD 演讲 Brian Callahan〕讲者口述：他不满意 FreeBSD 的代码行为准则（code of conduct）被“14”当作一次性定案呈现，称“14”只有九名男性、没有女性、几乎肯定也没有种族少数族裔，因此这九个人“绝无可能”真正了解 FreeBSD 社区的实质。（YouTube EP6cYsjJkhdXE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1732 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1732`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔P08B SocialBSD 演讲 Brian Callahan〕讲者口述：问答环节中有人追问 FreeBSD 宪章删去“FreeBSD is a meritocracy”一语的原因，称这是其所知最早的几处修改之一；对 meritocracy 一问的答辞援引了关于“种族与性别无色盲叙事”（colorblind narrative）的讨论，认为就客观情形而言社区并不真是精英制。（YouTube EP6cYsjJkhdXE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1733 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1733`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔P08B SocialBSD 演讲 Brian Callahan〕讲者口述：就其所知 FreeBSD 已有代码行为准则（codes of conduct），而其余 BSD 项目则都没有，他认为这“大概是个问题”。（YouTube EP6cYsjJkhdXE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2070 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2070`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔EuroBSDcon 2023“Encouraging SMEs to contribute to Development of BSD”讲者 TomSmyth〕讲者口述：讲者自述其经营的是一家在爱尔兰的小型 ISP（转写音作 Wireless connect），公司以自身资源向 BSD Foundation 捐赠，金额自认微薄。（YouTube EPZF7ZVP7qX70，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2071 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2071`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔EuroBSDcon 2023“Encouraging SMEs to contribute to Development of BSD”讲者 TomSmyth〕讲者口述：讲者举例其公司出资定制的一项特性：请 MPI 做的 bridgeports，功能是像厂商设备那样的受保护端口分组，用于把客户端彼此隔离；这项特性由该公司小额出资推动。（YouTube EPZF7ZVP7qX70，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2072 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2072`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔EuroBSDcon 2023“Encouraging SMEs to contribute to Development of BSD”讲者 TomSmyth〕讲者口述：讲者提出多家企业联合出资的模式：例如若某项 bridge 相关特性是 ISPs 普遍需要的，可以让大约五家 ISP 一起出资完成这个小而非颠覆性的改动，这样既给开发者带来经费，也让 BSD 向其用户群体推进。（YouTube EPZF7ZVP7qX70，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2073 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2073`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔EuroBSDcon 2023“Encouraging SMEs to contribute to Development of BSD”讲者 TomSmyth〕讲者口述：讨论转向出资带来的治理问题：应向基金会支付多大比例的款项——讲者认为应当支付一部分，因为把代码纳入各项目主干存在管理开销；向中小企业收取款项也是他提出的一个待议问题。（YouTube EPZF7ZVP7qX70，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
