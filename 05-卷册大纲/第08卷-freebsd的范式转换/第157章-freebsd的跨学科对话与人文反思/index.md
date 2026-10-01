---
chapter: 第 157 章
id: CH157
volume: 第08卷-freebsd的范式转换
---

# 第157章 freebsd的跨学科对话与人文反思

## 要点

- BSD 许可证的人文意义远超法律文本本身：(1) **BSD 许可证的历史演变**——最初的 4-clause BSD license（广告条款）源自 UC Berkeley 1980 年代，要求所有广告材料提及 “本产品包含由加州大学伯克利分校及其贡献者开发的软件”；1999 年 7 月 22 日，William Hoskins（UC Berkeley 技术许可办公室主任）正式宣布删除广告条款（第 3 条），形成 3-clause BSD license；2-clause BSD license（又称 FreeBSD license，简化版）进一步删除了 “不允许用贡献者名字背书” 条款；FreeBSD 自 2000 年代起采用 2-clause BSD license 作为新代码的默认许可证；(2) **“Trust the user” 哲学**——BSD 许可证的核心不是 copyleft 的 “强制保持开放”，而是 “信任用户会做正确的事”——你可以自由使用、修改、甚至闭源分发 BSD 代码，只要保留版权声明和免责声明；这种模式基于对人的信任，而非基于法律强制；(3) **与 GPL 的人文对比**——GPL 是 “自由的捍卫者”：通过 copyleft 确保代码永远保持自由；BSD 是 “自由的给予者”：我给你自由，你可以用它做任何事，包括闭源；这不是谁对谁错，而是两种不同的自由观——GPL 更接近积极自由（有权利做什么），BSD 更接近消极自由（不被干涉做什么）；(4) **BSD 许可的实际影响**——BSD 代码被融入了几乎所有现代操作系统：Linux（部分驱动和工具）、macOS/iOS（大量代码）、Windows（TCP/IP 栈历史上受 BSD 影响，现代 Windows 也包含 BSD 代码）、PlayStation、Juniper Junos、Netflix Open Connect 等等
- CSRG（Computer Systems Research Group）的科学精神通过代码和文化传承给了 FreeBSD：(1) **Keith Bostic（基思·博斯蒂克）**——CSRG 核心成员，主导了 Net/2 重写（1991 年为应对 USL 诉讼，带领团队重写了所有 AT&T 代码）、nvi 编辑器（原 vi 许可证问题的重写版）、Berkeley DB 等项目；Bostic 的工作体现了 “为了自由重写一切” 的决心；(2) **Mike Karels**——CSRG 技术领导（1983 年后与 McKusick 共同领导），4.2BSD/4.3BSD 主要架构师之一，后加入 BSDi；Karels 以对代码质量的苛刻要求和细致的代码审查著称；(3) **Sam Leffler**——4.2BSD 技术主管（1982-1983），TCP/IP 栈实现的主要作者之一；1983 年离开 CSRG 加入 Lucasfilm（John Lasseter 正是通过 Leffler 的关系为 4.3BSD 画了 daemon！），后创立 Silicon Graphics 的 BSD 部门，再后创建 Whistle Communications（嵌入式 BSD 产品）；Leffler 是典型的 “从学术到工业” 的桥梁人物；(4) **CSRG 的同行评审传统**——在互联网时代之前，CSRG 就已经在实施类似现代 code review 的实践——所有代码提交都要经过 Karels 或 McKusick 的审查；(5) **可重复实验精神**——CSRG 发布的不仅是代码，还有完整的文档、论文和设计说明（如 4.3BSD 设计书），使得其他人可以理解、复现、改进他们的工作
- FreeBSD 社区行为准则（Code of Conduct，CoC）的采纳是 2010-2020s BSD 社区与文化左翼思潮交锋的标志性事件。考据 FreeBSD 官方页面 freebsd.org/internal/code-of-conduct/ 注明 “Publication date: 2020-06-09”，互联网档案馆 2020 年 6 月 10 日存档与之一致，可双重交叉验证 CoC 首次发布日期为 2020 年 6 月 9 日——而非中文自媒体广泛流传的 “2018 年” 说法（该误传源自对 FreeBSD Foundation 2018 年治理讨论的混淆，须按 0 信任原则拒绝采信）。FreeBSD CoC 文本明确标注 "This text is based on the LLVM Project's draft CoC, which in turn is based on the Django Project Code of Conduct, which is in turn based on wording from the Speak Up! project"，即来源链为 Speak Up! → Django → LLVM → FreeBSD，体现 BSD 社区对成熟 CoC 模板的借鉴而非自创。CoC 核心条款包括 “be friendly and patient” “be welcoming” “be considerate” “be respectful” “be careful in the words that you choose” “when we disagree, try to understand why” 六条原则，并设立 <conduct@FreeBSD.org> 投诉邮箱与 Code of Conduct Committee 处理违规。CoC 适用范围涵盖邮件列表、IRC、bug 追踪器、FreeBSD 开发者会议等所有 FreeBSD 项目管理空间，并明示 "violations of this code outside these spaces may, in rare cases, affect a person's ability to participate within them, when the conduct amounts to an egregious violation of this code"——这一 “场外违规场内追责” 条款成为后续社区争论焦点之一
- Randi Harper（亦称 Randi Lee Harper、网名 freebsdgirl）是 FreeBSD src committer，其 FreeBSD 任期与 Gamergate 期间的社区立场构成了 BSD 社区与 2010s 美国科技文化战争交汇的一个典型案例。FreeBSD 官方 cgit 仓库（cgit.freebsd.org/src/log/?qt = author&q = Randi+Harper）一手提交记录显示 Harper 于 2010-04-21 首次提交 “Add myself to committers-src.dot.” 正式加入 FreeBSD src committer 行列，导师（mentor）为 Colin Percival（cperciva），活跃期集中在 2010 年 4-10 月，主要贡献包括：(1) **移除 sysinstall 升级功能**（2010-07-08 提交 r209787，理由是 "freebsd-update now provides a reasonable way to handle upgrades, so keeping this functionality in sysinstall only serves to mislead users"）；(2) **mfiutil/mptutil RAID 工具错误处理改进**（2010-10-10 提交 r213672、r213674）；(3) **install.cfg 网络配置增强**（2010-05-21 引入 `netDev=ANY` 支持，2010-07-07 添加远程 syslogd 日志支持）；(4) **libdialog 与 sysinstall WARNS = 2 清理**。Gamergate 争议爆发于 2014 年 8 月，Harper 在此期间开发了 GGAutoBlocker（又称 Good Game Auto Blocker）——一个自动屏蔽 Twitter 上 Gamergate 相关账号的脚本工具，公开立场是反对针对女性游戏开发者与评论者的网络骚扰。Harper 在 FreeBSD 社区的 committer 身份与她在 Gamergate 中的公开活动形成了独特的交叉身份——既是 BSD 技术贡献者，又是科技领域反骚扰运动的代表人物之一。FreeBSD 社区对 Harper 立场的官方回应：未发现 FreeBSD 项目以官方名义发表声明，自媒体文章中 “FreeBSD 社区驱逐 Harper” 或 “FreeBSD 社区支持 Harper” 的说法均缺乏一手证据 ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］。本节叙事严格基于一手提交记录与 Harper 本人公开发言，不对 Gamergate 本身作价值判断
- 2010-2020s 美国科技左派（tech left）的兴起有其深层哲学渊源与社会背景。哲学层面，斯坦福哲学百科全书（Stanford Encyclopedia of Philosophy，plato.stanford.edu）“Feminist Philosophy” 条目（2018 年首发，2023 年 7 月修订）系统阐述了女性主义哲学对传统哲学领域（美学、伦理学、哲学史、形而上学、政治哲学）的介入与重构，并明确将 “性别的社会建构” “身体政治” “再生产劳动” 等概念纳入哲学考据视野；斯坦福哲学百科 “Philosophy of Technology” 条目（2009 年首发，2026 年 7 月 10 日修订）区分了 Mitcham 1994 年提出的 “humanities philosophy of technology”（人文学科技术哲学，强调技术对社会的意义与冲击）与 “engineering philosophy of technology”（工程学技术哲学，关注技术设计与创造实践本身），这一二分法对理解 BSD 工程文化与科技左派人文学科视角的张力具有方法论意义。法律哲学层面，Lawrence Lessig（劳伦斯·莱斯格） 在《Code and Other Laws of Cyberspace》（Basic Books, 1999）中提出 “code is law”（代码即法律）命题——网络空间的架构（code）如同法律一样规制行为，这一命题成为科技左派思考 “技术架构与社会权力” 关系的奠基性论断。社会背景层面，2014 年 8 月 Ferguson 抗议（密苏里州弗格森警察枪杀 Michael Brown 事件引发的全国抗议）、2016 年 11 月 Trump 当选美国第 45 任总统、2017 年 10 月 #MeToo 运动爆发等三大事件构成了美国科技左派兴起的直接社会语境——这三大事件在科技领域引发了关于 “技术中立性神话” “平台责任” “算法偏见” “科技工作者政治责任” 的系统性反思，直接催生了 2017-2020 年间 Google 内部抗议（包括 James Damore 备忘录事件与 2018 年 Google 员工反对 Maven 项目）、Facebook 内容审查争议、GitHub ICE 合同抗议等一系列科技公司与科技左派冲突事件。这一波科技左派思潮与 BSD 社区的相遇，构成了本节前两个子子节所述 FreeBSD CoC 争论与 Gamergate 事件的宏观哲学与社会背景

## 史观

- 哲学思潮：BSD 许可的 “Trust the user” 是自由意志主义哲学在软件领域的体现——相信技术使用者的判断权，不预设他们会滥用自由；这与 1.md 项目统摄史观中 “信任个体体验” 的立场有深层共鸣：自由不是被授予的，而是被承认的
  - 辨析：常见误解称 “BSD 许可不保护自由”——这是用 GPL 的自由观来评判 BSD；BSD 认为真正的自由包括选择闭源的自由
- 终结与延续：CSRG 的科学精神没有随 CSRG 1995 年解散而消失——它通过 FreeBSD、NetBSD、OpenBSD、Darwin 等后代项目延续至今；FreeBSD 的 code review 流程、release engineering 纪律、文档传统都是 CSRG 精神的直接继承者
  - 辨析：需要区分 “CSRG 神话” 与历史真实——CSRG 不是完美的
- 开源运动；历史解释学与权力。CoC 的采纳是开源运动从 “代码优先” 向 “社区治理优先” 演化的标志性节点。FreeBSD CoC 文本明确将 “varied community, people from a wide range of backgrounds” 列为 “strength of FreeBSD”，这标志着 BSD 社区从早期 “纯技术精英主义” 向 “多元身份承认” 的话语转向。但 CoC 文本本身是基于 LLVM/Django 的衍生品而非 FreeBSD 社区原创，这一文本来源链揭示了开源社区治理模式的文化传播路径——大型开源项目间的 CoC 模板复用既是协作效率的体现，也带来 “模板与本地社区文化是否适配” 的根本张力
- 边缘者贡献；历史解释学与权力。Harper 案例揭示了 BSD 社区作为 “技术精英主义” 场域与 “性别平权运动” 交汇时的复杂张力——一个在 FreeBSD 代码仓库有实际贡献的女性开发者，在 Gamergate 期间成为公开的反骚扰活动家，这种双重身份挑战了 BSD 社区 “只看代码不看身份” 的传统叙事。考据视角须避免两种还原论：既不能因 Harper 的技术贡献而豁免其立场的考据核查，也不能因她在 Gamergate 中的立场而否定其 FreeBSD 代码贡献的真实性——这两种还原论都违反 0 信任原则。Harper 案例的深层意义在于揭示了 “代码贡献” 与 “社会立场” 在 BSD 社区治理框架中的不可通约性：2010 年的 FreeBSD 社区尚无 CoC，技术贡献是唯一可识别的社区资本；2020 年 CoC 通过后，场外行为成为社区参与资格的潜在考量因素，这种治理框架的转变在 Harper 案例中获得了具体的经验参照
- 哲学思潮；开源运动。科技左派的兴起不是凭空出现的政治现象，而是有其深厚的哲学基础——女性主义哲学对 “性别中立” 神话的解构、技术哲学对 “技术中立” 神话的解构、Lessig 对 “代码即法律” 的揭示，这三条哲学线索在 2010-2020s 汇聚为科技左派的核心论域。开源运动与科技左派的相遇是必然的——开源社区本身就是一个由代码架构规制的微型社会，CoC 争论本质上就是 “代码（架构）即法律（规制）” 命题在社区治理层面的具体演绎。BSD 社区作为开源运动中 “工程精英主义” 传统最浓厚的分支，与科技左派的张力也最为深刻——这不是对错之争，而是两种合理性叙事的交汇：BSD 强调 “代码质量是唯一标准”，科技左派强调 “代码质量标准的设定本身嵌入权力关系”

## 辨析

- 常见误解称 “BSD 许可不保护自由”——这是用 GPL 的自由观来评判 BSD；BSD 认为真正的自由包括选择闭源的自由——如果我只能以特定方式使用代码，那不是真自由；当然，这也意味着 BSD 代码可能被 “夺走” 并变成专有软件，但 BSD 社区认为这是自由的代价，而且从长期看，开放协作的价值会胜出（这一点已被 40 年历史部分验证）
  - 文献：Regents of the University of California. BSD License（4-clause 原始文本；广告条款于 1999-07-22 由 William Hoskins 宣布删除）〔存疑：原引截断，按本章要点复原，待回源核验〕
- 需要区分 “CSRG 神话” 与历史真实——CSRG 不是完美的理想国，他们也有代码 bug、内部政治、截止日期压力、人为错误；但他们确实建立了一套在当时非常先进的工程实践，为后来的开源运动提供了参考模型
  - 文献：McKusick, M. K. (1999). Twenty Years of Berkeley Unix. In *Open Sources: Voices from the Open Source Revolution*. Sebastopol: O'Reilly & Associates, 1999.
- **关键日期精确考证**：① FreeBSD CoC 发布年份——FreeBSD 官方页面与互联网档案馆存档双重验证为 2020-06-09；自媒体中文文章广泛流传的 “2018 年” 说法 ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP633、EP631（共 2 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Ed Brayden 的《Magical Systems Thinking》以 Forrester 的世界模型与啤酒游戏为例，论证复杂系统会反抗自上而下设计，成功来自从小处起步的简单可用系统。（BSD Now EP633，[897.06-1603.88]，L2）
- Broadcom 收购 VMware 后背负约 610 亿美元交易与债务，Bitnami 于 2025 年 8 月终止免费镜像并转向每年数万美元的付费服务，引发开发者迁移潮。（BSD Now EP633，[1612.96-2123.00]，L2）
- OpenSSH 10.1 于 2025 年 10 月 6 日发布，修复用户名控制字符注入问题，并新增 SIGINFO 通道日志、PKCS#11 ED25519 支持与 refuse connection 配置项。（BSD Now EP633，[2126.22-2590.12]，L2）
- Brian Kernighan 在 VCF East 2025 表示只写过一次 Rust 且体验不佳，认为其 crate 与编译链庞大缓慢，同时坦言对 NixOS 与多数发行版并不熟悉。（BSD Now EP633，[2757.82-3220.12]，L1）
- GhostBSD 25.02 基于 FreeBSD 14.3，新增以 GNUstep 组件与 XFCE 面板组合的 Gershwin 桌面，提供类 macOS 体验。（BSD Now EP633，[3371.86-3563.32]，L2）
- Raymond Chen 复述复杂系统的基本失效模式定理：任何复杂系统都处于某种失效模式，局部补偿使问题潜伏，改变只会带来更复杂的反制。（BSD Now EP631，[130.8-228.1]，L1）[订正：原 [138.14-224.48]，2026-10-01 SenseAudio 重转核对]
- Dr. Brian Robert Callahan 为 QBE 的 ARM64 后端编写窥孔优化，消除冗余寄存器拷贝与可即时数化的算术指令，说明 ARM64 定长指令下只能通过删除指令获利。（BSD Now EP631，[280.3-735.8]，L1）[订正：原 [286.40-737.76]，2026-10-01 SenseAudio 重转核对]
- FreeBSD 笔记本作者发现 Nvidia 驱动会覆盖 Xorg 与 DRM 模块的文件，导致 GL 支持判定错乱，移除 Nvidia 驱动并重装 Intel 与 DRM 驱动后恢复正常。（BSD Now EP631，[763.9-910.2]，L1）[订正：原 [765.84-908.32]，2026-09-30 SenseAudio 重转核对]
- 以 devd 规则按 USB 厂商与产品 ID 建立符号链接，并把链接置于 jail 根目录而非 /dev，可将设备以稳定名称传入 FreeBSD jail。（BSD Now EP631，[918.0-1323.8]，L1）[订正：原 [921.84-1316.76]，2026-10-01 SenseAudio 重转核对]
- Chris Siebenmann 澄清 ZFS 快照并非完全不可变，快照元数据会随独有空间统计、快照删除与重命名而更新，只有文件系统状态被冻结。（BSD Now EP631，[1302.1-1408.2]，L1）[订正：原 [1321.58-1407.46]，2026-10-01 SenseAudio 重转核对]
- 将 PeerTube 从 Debian 迁移到 FreeBSD 的过程以 UFS 而非 ZFS 作为客户机文件系统，以避免在 OmniOS 的 ZFS 上嵌套 ZFS。（BSD Now EP631，[1414.3-1794.6]，L1）[订正：原 [1417.28-1794.48]，2026-09-30 SenseAudio 重转核对]

**史料**：

- Klara Systems 的 OpenZFS 2.4 路线图文章。（BSD Now EP633，[379.98-706.22]，L2）
- Ed Brayden 于 worksinprogress 的《Magical Systems Thinking》。（BSD Now EP633，[897.06-1603.88]，L2）
- fastcode.io 关于 VMware 收购与 Bitnami 收费的报道。（BSD Now EP633，[1612.96-2123.00]，L2）
- OpenSSH 10.1 官方发布说明。（BSD Now EP633，[2126.22-2590.12]，L2）
- The New Stack 对 Brian Kernighan 在 VCF East 2025 问答的报道。（BSD Now EP633，[2749.04-3342.34]，L2）
- Raymond Chen 于 devblogs.microsoft.com 的《The fundamental failure mode theorem》。（BSD Now EP631，[130.8-228.1]，L1）[订正：原 [138.14-224.48]，2026-10-01 SenseAudio 重转核对]
- Dr. Brian Robert Callahan 博客 QBE ARM64 窥孔优化系列。（BSD Now EP631，[280.3-735.8]，L1）[订正：原 [286.40-737.76]，2026-10-01 SenseAudio 重转核对]
- Chris Siebenmann 博客 ZFS snapshots aren't as immutable as I thought。（BSD Now EP631，[1302.1-1408.2]，L1）[订正：原 [1321.58-1407.46]，2026-10-01 SenseAudio 重转核对]
- 关于 FreeBSD jail 设备稳定名称与 PeerTube 迁移的两篇博客。（BSD Now EP631，[918.0-1794.6]，L1）[订正：原 [921.84-1794.48]，2026-09-30 SenseAudio 重转核对]

**史观**：

- 总纲5 没有必然性，只有偶然性：总纲5 没有必然性，只有偶然性：Ed Brayden 论证世界模型与预测的失败，强调复杂系统走向并非规划者所能必然掌控。（BSD Now EP633，[1084.22-1603.88]，L2）
- 总纲11 商品是形式主义：总纲11 商品是形式主义：Broadcom 将 Bitnami 免费镜像改造为定价商品，展示开源资产在资本收购后的形式主义化。（BSD Now EP633，[1645.84-2123.00]，L2）
- 总纲22 知识注定过时：总纲22 知识注定过时：Brian Kernighan 以 C 语言长期推广者身份面对 Rust 崛起，反映技术知识随生态更替而过时的处境。（BSD Now EP633，[2863.88-2966.64]，L1）
- 总纲5 没有必然性，只有偶然性：总纲5 没有必然性，只有偶然性：基本失效模式定理强调复杂系统运行状态由具体故障与补偿关系决定，而非设计意图的必然实现。（BSD Now EP631，[130.8-228.1]，L1）[订正：原 [138.14-224.48]，2026-10-01 SenseAudio 重转核对]
- 总纲10 动手者创造历史：总纲10 动手者创造历史：笔记本作者通过动手排查定位 Nvidia 与 DRM 驱动文件覆盖问题，而非依赖文档结论。（BSD Now EP631，[871.5-910.2]，L1）[订正：原 [874.40-908.32]，2026-09-30 SenseAudio 重转核对]
- 总纲25 逻辑是形式主义而非世界本身的结构：总纲25 逻辑是形式主义而非世界本身的结构：ZFS 快照的不可变是概念化标签，其元数据实现仍随操作可变，说明概念与实现之间的形式主义距离。（BSD Now EP631，[1324.2-1408.2]，L1）[订正：原 [1324.62-1407.46]，2026-09-30 SenseAudio 重转核对]

**辨析**：

- 转录将 Klara Systems 记作 Clara、将 Brian Kernighan 记作 Koenigan 或 Kernigan，人名与机构名存在语音转写偏差。　[存疑脚注] 机构与人物名称存在转写偏差，须以原文核验（BSD Now EP633，[2753.12-2784.64]，L4）
- Bitnami 定价在转录中出现 600 亿、60 万与 7.2 万等不一致数字，具体金额须以 AWS Marketplace 与官方公告核验。　[存疑脚注] 价格数字存在转写歧义，未与官方定价页核验（BSD Now EP633，[1666.68-2041.44]，L4）
- 转录将 Raymond Chen 所属微软博客名称与若干命令参数出现错词，具体规则与命令须以原文核验。　[存疑脚注] 命令与规则细节存在转写歧义，须以原文核验（BSD Now EP631，[130.8-147.6]，L4）[订正：原 [132.46-143.76]，2026-09-30 SenseAudio 重转核对]
- PeerTube 迁移文章作者在转录中记作 Tom Fatigue，疑为主持人 Tom Jones 或他人，署名须以原文核验。　[存疑脚注] 作者署名存在转写歧义（BSD Now EP631，[1414.3-1450.9]，L4）[订正：原 [1417.28-1432.32]，2026-10-01 SenseAudio 重转核对]

**文献**：

- [BSD Now EP633] Pennington J. BSD Now: 633: Magical Systems Thinking[EB/OL]. (2025-10-16)[2026-08-15]. <https://www.bsdnow.tv/633>.
- [BSD Now EP631] Pennington J. BSD Now: 631: Endorphin Rush[EB/OL]. (2025-09-25)[2026-08-15]. <https://www.bsdnow.tv/631>.

<!-- /PODCAST_REVIEW -->