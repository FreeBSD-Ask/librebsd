---
chapter: 第 124 章
id: CH124
volume: 第06卷-freebsd的核心技术革新
---

# 第 124 章 freebsd9x图形架构与社区治理

## 要点

- 9.1-RELEASE 新增 Intel GPU 驱动支持 GEM（Graphics Execution Manager）与 KMS（Kernel Mode Setting），这是 FreeBSD 图形栈现代化的重要一步；KMS 将显示模式设置从用户态 X 服务器移入内核，支持更快的 VT 切换、更稳定的图形性能和 suspend/resume；Radeon KMS 支持在 9.x 尚未完成，10.x 之后才引入
- 9.x 系列新增大量网卡驱动：9.0 新增 **bxe(4)**（Broadcom NetXtreme II 10GbE）、**cxgbe(4)**（Chelsio T4 10Gb/1Gb）、**vte(4)**（RDC R6040）、**vxge(4)**（Neterion X3100 10GbE）；**em(4)** 更新至 7.3.2、**igb(4)** 至 2.2.5、**ixgbe(4)** 至 2.3.8，新增 Intel I350 支持；9.1 新增 **oce(4)**（Emulex OneConnect 10GbE）、**sfxge(4)**（Solarflare SFC9000）、**hpt27xx(4)**（HighPoint RocketRAID 27xx SAS 6Gb/s）
- 9.0-RELEASE 中 FreeBSD/powerpc 支持 Sony PlayStation 3 主机的 OtherOS 功能（固件 3.15 及更早版本）；Nathan Whitehorn 是 PS3 支持的主要开发者，他同时也是 bsdinstall 作者和 powerpc64 release builder；Sony 于 2010-04-01 通过固件更新 3.21 移除 OtherOS 功能（2010-03-28/29 为公告日，2026-08-05 联网复核更正），因此该支持仅对未升级固件的旧款 PS3（“OtherOS 脂肪机”）有意义，PS3 Slim 出厂即无 OtherOS
- 9.0-RELEASE 支持架构：amd64、i386、ia64（Itanium）、powerpc、powerpc64、sparc64；9.1-RELEASE 初始仅发布 amd64、i386、powerpc64、sparc64（ia64/powerpc 因构建资源受限后补）；9.2/9.3 恢复支持 amd64、i386、ia64、powerpc、powerpc64、sparc64；FreeBSD/arm 在 9.x 时期持续改进但未列入 RELEASE Tier 1 架构；FreeBSD/mips 在 9.x 时期主要用于嵌入式场景，不发布标准安装镜像
- Sony 于 2013 年 11 月 15 日（北美）/11 月 29 日（欧洲）发布 PlayStation 4（PS4），其操作系统 Orbis OS 基于 **FreeBSD 9.0** 内核修改（原文件错误为 10.0——PS4 2013.11 发布时 10.0 尚未发布（10.0 2014.1.20 才发布），时间线上不可能基于 10.0）；PS4 选择 FreeBSD 而非 Linux 的核心原因是 BSD 许可证允许闭源修改——Sony 无需像 GPL 那样公开其内核修改；Orbis OS 在 FreeBSD 9.0 基础上新增了定制的图形栈（基于 AMD GCN GPU）、安全 hypervisor、定制系统服务等

## 史观

- 总纲第 10 条——动手者创造历史：FreeBSD 图形驱动开发长期依赖少数志愿者（如 Konstantin Belousov（康斯坦丁·别洛乌索夫）、Konrad Witaszczyk 等）从 Linux 移植 DRM/KMS 代码，是项目中资源相对匮乏但需求广泛的领域；图形栈的延迟成熟是 FreeBSD 桌面体验落后于 Linux 的重要原因
  - 辨析：9.1 Intel KMS 仅支持较旧的〔存疑：原文截断，待回源补全〕
- 总纲第 10 条——动手者创造历史：PS3 支持是 FreeBSD 支持游戏主机的罕见案例——它与 PS4 Orbis OS（见本章 124.12）形成有趣对照：前者是 hobbyist 级的非官方支持，后者是 Sony 官方基于 FreeBSD 的产品级派生；Sony 移除 OtherOS 的决定引发了集体诉讼，最终以赔偿和解告终
  - 辨析：PS3 OtherOS 支持仅在 3.15 及更早固件有效，〔存疑：原文截断，待回源补全〕
- 总纲第 13 条——法律与道德是利益分配：PS4 是 BSD 许可证商业友好性的标志性案例——它与 Apple macOS/Darwin（基于 FreeBSD 5.x 时期）、Netflix Open Connect、Juniper Junos、pfSense/OPNsense、Blue Coat、NetApp 等共同构成 BSD 许可证商业模式的实证；GPL 许可证要求公开派生作品源代码，这使得商业公司在闭源
- 总纲第 3 条——不存在进步，只有权力再分配：Security Officer 是 FreeBSD 最关键的角色之一，掌握安全公告发布、漏洞协调、基础设施安全等核心权力；Colin Percival 长达 7 年（2005-2012）的任期塑造了 FreeBSD 安全响应的文化与流程，其继任者延续了严格、保守、透明的安全公告风格
- 124.13.1 Security Officer 交接

**要点**：FreeBSD Security Officer 在 9.x 时期经历有序交接：9.0-RELEASE 时期 Security Officer 为 Colin Percival（cperciva@）
- 专题语（不设总纲条号）——知识管理的制度化。
- 文献：安全团队报告 ［A］

## 辨析

- 9.1 Intel KMS 仅支持较旧的 Intel GPU（Ironlake/Sandy Bridge 时期），Ivy Bridge 及更新 GPU 支持在后续版本添加；Radeon/NVIDIA KMS 在 9.x 不可用
  - 文献：FreeBSD 9.1-RELEASE Release Notes（Graphics Drivers 章节）；**drm(4)**、**i915kms(4)**〔存疑：原文截断，待回源补全〕
- PS3 OtherOS 支持仅在 3.15 及更早固件有效，绝大多数 PS3 用户因在线游戏和 PSN 需求早已升级固件，因此该支持的实用价值有限，但作为 FreeBSD 支持非传统硬件平台的案例具有历史意义
  - 辨析（2026-08-05 一手原件补充，ref 2632-2637/2647）：**In re Sony PS3 “OtherOS” Litigation**（N.D. Cal.,〔存疑：原文截断，待回源补全〕
- **重要事实纠正——Orbis OS 基于 FreeBSD 9.0 而非 10.0**：时间线证据是决定性的——PS4 2013.11.15 发售，FreeBSD 10.0 2014.1.20 才发布；PS4 开发周期中 10.0 尚未发布，Sony 不可能基于未发布的版本；CTurt 等 PS4 越狱者的逆向分析也确认内核基于 9.0；部分媒体可能因 PS4 生命周期中后续升级包含 10.x 代
- Security Officer 交接在 9.x 密集发生（9.0 cperciva→9.1 simon→9.2 des，9.3 新增 delphij），部分源于 Colin Percival 在 Tarsnap 等商业项目上的精力分配，也与 2012 年入侵事件后安全团队扩充有关；从 9.2 开始采用 “Security Officer + Emeritus” 双轨制，保留前任经验；这种有序的权〔存疑：原文截断，待回源补全〕
- 谱系叙述中须区分两个层次——技术源头是 Larry Wall 原始 **patch(1)**，许可证源头是 OpenBSD 替换 GPL 文件为 PD/无限制版本；DragonFly 的 “进一步增强” 具体内容须对照 DragonFly commit log 核实；pfg “反向移植 FreeBSD 原有增强” 表明 FreeBSD 版本与 DragonFly 版本并非简单复制关系，而是双向融合

## 文献

- FreeBSD 9.1-RELEASE Release Notes（Graphics Drivers 章节）；**drm(4)**、**i915kms(4)** man pages（9.1 版本） ［B］

## 124.10 网络驱动更新

- 要点：9.x 系列新增大量网卡驱动：9.0 新增 **bxe(4)**（Broadcom NetXtreme II 10GbE）、**cxgbe(4)**（Chelsio T4 10Gb/1Gb）、**vte(4)**（RDC R6040）、**vxge(4)**（Neterion X3100 10GbE）；**em(4)** 更新至 7.3.2
- FreeBSD 9.0-RELEASE Release Notes（Architectures 章节）；svn commit r217044；Sony Computer Entertainment. PS3 System Software Update 3.21 [Z]. 2010-03-28 ［A］

## 124.11 9.x 支持架构与状态

- powerpc64、sparc64；9.1-RELEASE 初始仅发布 amd64、i386、powerpc64、sparc64（ia64/powerpc 因构建资源受限后补）
- Sony Computer Entertainment. PlayStation 4 Developer Documentation（Orbis OS 章节）；CTurt. PS4 Kernel Exploitation Analysis [Z]. 2015-2017；多家技术媒体 2013.6 E3 报道（确认 Orbis OS 基于 FreeBSD 9.0）；Rosen L. Open Source Licensing: Software Freedom and Intellectual Property Law [M]. Upper Saddle River: Prentice Hall
- FreeBSD 9.0/9.1/9.2/9.3-RELEASE Announcement Acknowledgments 章节 [Z]. 2012-2014；FreeBSD Security Team 页面（security.freebsd.org）［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

## 124.13 Release Engineering 团队构成

- 要点：9.0 Release Engineering Team 由 Ken Smith（kensmit〔存疑：原文截断，待回源补全〕
- 安全团队报告 ［A］
- Pedro Giffuni 2013.1.29 [CFT] WITH_BSD_PATCH（freebsd-current 邮件列表 archives/2013-January/039367.html）；FreeBSD Bugzilla PR 99173（bugs.freebsd.org/bugzilla/show_bug.cgi?id = 99173）；Kohn A. 2006.6.19 lwpatch 提案附件 ［A］

## 124.15 r246074 首次导入与 WITH_BSD_PATCH 构建选项

- 要点：2013 年 1 月 29 日 17:03 由 Gabor Kove〔存疑：原文截断，待回源补全〕
- Pedro Giffuni. [CFT] WITH_BSD_PATCH [EB/OL]. freebsd-current mailing list, 2013-01-29; Free Software Foundation. Various Licenses and Comments about Them [EB/OL]. gnu.org/licenses/license-list.html（#ModifiedBSD、#FreeBSD 条目，2026-07-22 核实）.［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

## 124.16 被忽视的边缘贡献者

- 要点：9.x 时期核心技术的知名贡献者（McKusick、Watson、Motin、Selasky、Grehan、Percival、Whitehorn、Dawidek 等）常被历史记录，但大量 ports 维护者、文档翻译者、bug 报告者、测试者的贡献被主流叙事忽视；FreeBSD 9.x 时期 ports 数量从约 22,000 增长至超过 24,000，背后是数百名 ports c〔存疑：原文截断，待回源补全〕

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP283、BSD Now EP631、BSD Now EP120（共 3 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 受访者自述 FreeBSD 图形栈在其设备上基本可用、可作为日常驱动，但承认体验仍不如 Windows 与 macOS，且特定硬件组合仍会出现挂起与交换分区交互导致的偶发冻结。（BSD Now EP283，[427.99-503.62]，L1）
- FreeBSD 图形栈在 2018 年底已大体跟进上游：输入栈与 Mesa 已更新，libinput 补丁位于开发仓库，X server 本体则是最滞后的待移植与待推送部分。（BSD Now EP283，[600.70-674.48]，L1）
- FreeBSD 图形团队规模极小：Johannes Lundberg 负责从 Linux 移植 DRM 驱动并更新 Linux KPI，另一名 Johannes Dietrich 维护 ports 中的图形驱动，Warner Losh 担任与 core 团队的联络，Matt Macy 尝试让 Linux KPI 在 PowerPC64 上运行。（BSD Now EP283，[676.78-944.60]，L1）
- 受访者自 2012 年起维护 FreeBSD ports，长期以 Poudriere 教程作为新人参与入口，认为从维护小型 port 开始逐步深入是降低参与门槛的有效方式。（BSD Now EP283，[998.48-1210.88]，L1）
- 受访者创办面向所有 BSD 的斯德哥尔摩用户组，借助雇主 B3Init 提供的场地举办聚会，规模约二十余人，并总结出首次活动容易高估到场人数等组织经验。（BSD Now EP283，[1222.98-1600.00]，L1）
- 受访者自 2019 年起获得雇主 B3Init 每周两小时带薪 FreeBSD 开发时间，并计划在上半年结束后与雇主共同评估延续方式。（BSD Now EP283，[2014.46-2064.04]，L1）
- Raymond Chen 复述复杂系统的基本失效模式定理：任何复杂系统都处于某种失效模式，局部补偿使问题潜伏，改变只会带来更复杂的反制。（BSD Now EP631，[138.14-224.48]，L1）
- Dr. Brian Robert Callahan 为 QBE 的 ARM64 后端编写窥孔优化，消除冗余寄存器拷贝与可即时数化的算术指令，说明 ARM64 定长指令下只能通过删除指令获利。（BSD Now EP631，[286.40-737.76]，L1）
- FreeBSD 笔记本作者发现 Nvidia 驱动会覆盖 Xorg 与 DRM 模块的文件，导致 GL 支持判定错乱，移除 Nvidia 驱动并重装 Intel 与 DRM 驱动后恢复正常。（BSD Now EP631，[765.84-908.32]，L1）
- 以 devd 规则按 USB 厂商与产品 ID 建立符号链接，并把链接置于 jail 根目录而非 /dev，可将设备以稳定名称传入 FreeBSD jail。（BSD Now EP631，[921.84-1316.76]，L1）
- Chris Siebenmann 澄清 ZFS 快照并非完全不可变，快照元数据会随独有空间统计、快照删除与重命名而更新，只有文件系统状态被冻结。（BSD Now EP631，[1321.58-1407.46]，L1）
- 将 PeerTube 从 Debian 迁移到 FreeBSD 的过程以 UFS 而非 ZFS 作为客户机文件系统，以避免在 OmniOS 的 ZFS 上嵌套 ZFS。（BSD Now EP631，[1417.28-1794.48]，L1）
- 本期核心为对 FreeBSD committer Pawel Jakub Dawidek（转写作 Pavel Davidek）的专访：其公司以 FreeBSD 为基座打造两款安全设备——FUDO 面向特权用户会话的录制与审计，Lynx 面向企业 TLS/SSL 流量的解密卸载；他自述设计哲学“信任开始之处即安全终结之处”（1827.17-1833.98），并指出近年重大安全事件多出自雇员与承包商，内部威胁的监控由此成为产品定位的核心。（BSD Now EP120，[1600.47-1742.97]，L1）
- FUDO 的技术栈揭示 FreeBSD 内核安全特性进入商业生产的深度：geli 承担全盘加密，Capsicum 承担会话沙箱，嘉宾称其设备“是比 FreeBSD 本体更大的 Capsicum 消费者”（1927.59-1934.81），认证前进程仅获一秒 CPU 配额与三个文件描述符；加密代价因客户端、服务端、落盘三方向而三倍叠加，图形会话另需 OCR 以支持文本检索，多主集群则依赖 ZFS 增量快照复制完成节点间同步。（BSD Now EP120，[1917.11-2234.32]，L1）

**史料**：

- 受访者提及 EuroBSDCon 2015 在斯德哥尔摩举办、开发者峰会曾借其旧办公室进行，以及 FreeBSD 季度状态报告将恢复发布图形栈条目。（BSD Now EP283，[354.72-379.54]，L1）
- 提及图形栈相关代码与仓库：libinput、Mesa 的上游同步、Linux KPI 移植以及待推送至 FreeBSD ports 的 X server 端口。（BSD Now EP283，[600.70-674.48]，L1）
- Raymond Chen 于 devblogs.microsoft.com 的《The fundamental failure mode theorem》。（BSD Now EP631，[138.14-224.48]，L1）
- Dr. Brian Robert Callahan 博客 QBE ARM64 窥孔优化系列。（BSD Now EP631，[286.40-737.76]，L1）
- Chris Siebenmann 博客 ZFS snapshots aren't as immutable as I thought。（BSD Now EP631，[1321.58-1407.46]，L1）
- 关于 FreeBSD jail 设备稳定名称与 PeerTube 迁移的两篇博客。（BSD Now EP631，[921.84-1794.48]，L1）
- 本期一手史料以嘉宾第一人称口述为主：FUDO 与 Lynx 的架构决策、geli 开发史（XTS 模式缺席年代实现 CBC 不可预测初始化向量、4K 扇区时代放弃块级认证）与 open crypto 框架改造及厂商补丁处境；辅以主持人转述的公开材料——PS4 越狱开发者发布的 GitHub 信息与推文、OpenBSD 运行于 EC2 T2 Micro 的实测帖、AsiaBSDCon 与 BSDCan 2016 征稿公告、2002 与 2015 两版开发者桌面截图页、OpenSSH 历史提权漏洞（二进制仅差一比特）与 TrueCrypt 重现构建事例，以及两封读者来信（大学集群迁移事故、帐篷公司 FreeNAS 改造）。（BSD Now EP120，[1600.47-1742.97]，L2）

**史观**：

- 总纲10 动手者创造历史：图形栈这一基础设施长期由少数动手者维持，其工作依赖社区测试反馈与硬件样本的缓慢积累，属于被主流叙事边缘化的劳动。（BSD Now EP283，[690.18-747.68]，L1）
- 总纲15 文化即形式主义：用户组、会议、教程与雇主赞助共同构成社区再生产的社会形式；受访者特别指出参加一次会议即可让人意识到自己的工作被他人实际使用。（BSD Now EP283，[386.88-424.68]，L1）
- 总纲5 没有必然性，只有偶然性：基本失效模式定理强调复杂系统运行状态由具体故障与补偿关系决定，而非设计意图的必然实现。（BSD Now EP631，[138.14-224.48]，L1）
- 总纲10 动手者创造历史：笔记本作者通过动手排查定位 Nvidia 与 DRM 驱动文件覆盖问题，而非依赖文档结论。（BSD Now EP631，[874.40-908.32]，L1）
- 总纲25 逻辑是形式主义而非世界本身的结构：ZFS 快照的不可变是概念化标签，其元数据实现仍随操作可变，说明概念与实现之间的形式主义距离。（BSD Now EP631，[1324.62-1407.46]，L1）
- 总纲10 动手者创造历史：嘉宾从昔日高产 committer 转向培养新一代动手者——推动 Mariusz Zaborski 成为 committer 从事 Capsicum 与 Casper、Konrad Witaszczyk 打磨加密内核转储补丁历时两年；他以 vendor 视角点出生态症结：厂商补丁常有九成就绪而最后一步永无余力完成者（3919.84-3932.04），故寄望基金会雇用专人收尾入库。BSD 史的推进动力在此显形为具体人手的持续劳动与“加入 FreeBSD 项目是我技术生涯最大的加速器”（4290.64-4303.08）式的代际传承，而非路线图或宣言。（BSD Now EP120，[3892.59-4303.08]，L2）
- 总纲5 没有必然性，只有偶然性：geli 开发史成为偶然性优先的注脚：当年可预测初始化向量的 CBC 模式被普遍视为安全，嘉宾凭超出共识的直觉实现不可预测初始化向量（3764.35-3772.27），日后该共识方案确被证明不安全，一次未按主流走的工程选择意外成为先见；与之呼应，OpenSSH 历史提权漏洞仅系一个比较运算符之差、修复前后二进制只差一比特，安全史的走向悬于这类无必然性的微小偶然。（BSD Now EP120，[3736.59-3778.55]，L1）

**辨析**：

- 转写将受访者姓名记为 Niklas Seising 与 Nicholas Seizing 两种拼法，且分段时间戳明显乱序；依据上下文应为 FreeBSD 图形团队成员 Niclas Zeising，但本卡片保留转写原拼写。　[存疑脚注] 受访者姓名拼写未经一手核对，且该期转写质量较差、时间戳乱序。（BSD Now EP283，[52.96-57.04]，L4）
- 受访者关于图形栈“基本可用”的自我评估带有当事人立场，且其承认与 Windows、macOS 存在差距、挂起与交换分区交互存在偶发冻结，须与版本发布记录与社区测试报告交叉验证。　[存疑脚注] 具体故障复现与修复状态未能从本期转写确认。（BSD Now EP283，[451.52-557.74]，L3）
- 转录将 Raymond Chen 所属微软博客名称与若干命令参数出现错词，具体规则与命令须以原文核验。　[存疑脚注] 命令与规则细节存在转写歧义，须以原文核验（BSD Now EP631，[132.46-143.76]，L4）
- PeerTube 迁移文章作者在转录中记作 Tom Fatigue，疑为主持人 Tom Jones 或他人，署名须以原文核验。　[存疑脚注] 作者署名存在转写歧义（BSD Now EP631，[1417.28-1432.32]，L4）
- PS4 越狱条目需谨慎使用：越狱者经由 WebKit 进程取得内核执行权，与 FreeBSD jail 机制无关，越狱一词仅借自 iPhone 语境；Orbis OS 基于 FreeBSD 9.0，但 Sony 版本号不披露其回移了哪些 FreeBSD 补丁，主持人的“该漏洞可能早已在 FreeBSD 修复”属无法判定的推测；开发者公开 PID 列表与根文件系统转储并声明不为盗版服务，其身份、动机与操作细节均系单一来源。　[存疑脚注] 转写将越狱开发者记作“C-Chert”（疑为 CTurt），Orbis OS 补丁回移状态无公开可核记录，主持人推断未经多源验证（BSD Now EP120，[4538.64-4651.02]，L4）
- Zero Trust 倡议暴露开源承诺与二进制分发之间的结构性落差：发布源码无法证明用户安装的二进制由其构建——Signal 的 App Store 二进制不可验证，TrueCrypt 的重现构建需穷举编译环境且工作量浩大；嘉宾强调该倡议“不想让人们信任 zero trust initiative 本身”（3522.06-3530.33），拒绝自任受信第三方，转而设想以基于 geli 的可移植磁盘加密项目先行示范；同期听众事故（OpenSSL 升级致 openldap 二进制失配、无人可登录）与 FreeBSD 侧 Ed Maste（转写作 Ed Mass）参加可重现构建会议，说明可重现构建在 2015 年仍属前沿工程而非成熟机制。（BSD Now EP120，[2893.17-3045.95]，L2）

**文献**：

- [BSD Now EP283] Pennington J. BSD Now: 283: Graphical Interface-View[EB/OL]. (2019-01-31)[2026-08-15]. <https://www.bsdnow.tv/283>.
- [BSD Now EP631] Pennington J. BSD Now: 631: Endorphin Rush[EB/OL]. (2025-09-25)[2026-08-15]. <https://www.bsdnow.tv/631>.
- [BSD Now EP120] Pennington J. BSD Now: 120: I’m talking about the man in the middle[EB/OL]. (2015-12-16)[2026-08-15]. <https://www.bsdnow.tv/120>.

<!-- /PODCAST_REVIEW -->
