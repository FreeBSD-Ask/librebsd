---
chapter: 第 289 章
id: CH289
volume: 第15卷-许可证哲学与法律分析
---

# 第289章 bsd代码双向流动与许可模式扩散

## 要点

- BSD 代码向其他开源项目的正向流出主要通过三种工程机制实现——（1）**基本系统采纳**：libarchive 自 Mac OS X 10.6 Snow Leopard 起作为 bsdtar 的底层库进入 macOS 基本系统，自 Debian/Ubuntu 起作为 bsdtar 软件包进入 Linux 发行版，自 Homebrew 起作为 bottles 打包工具进入 macOS 包管理器；jemalloc 自 2005 年 9 月〔存疑：通行记载系 2005 年 11 月由 Jason Evans 导入 -CURRENT、FreeBSD 7.0（2008-02）起为默认分配器，“2005 年 9 月即默认”待以 commit 史核订〕起作为 FreeBSD libc 默认分配器，后被 Facebook（Meta）、Mozilla Firefox 采用，Rust 早期版本曾以 jemalloc 为默认分配器（后随 Rust 1.28 全局分配器机制稳定化切换为系统分配器，但 jemalloc 仍通过 tikv-jemallocator crate 被大量 Rust 项目主动选用）；（2）**独立项目 fork 与移植**：OpenSSH 由 OpenBSD 项目于 1999 年 9 月从 Björn Grönvall 的 OSSH fork 而来，后以 portable 分支独立维护，进入几乎所有现代操作系统；LibreSSL 由 OpenBSD 项目于 2014 年 4 月 Heartbleed 漏洞后从 OpenSSL fork，后以 portable 版本进入 FreeBSD ports、Gentoo 等；（3）**跨项目代码同步**：OpenZFS 自 2013 年 9 月由 ZFS on Linux 与 illumos ZFS 团队合并成立 “OpenZFS 项目” 后，FreeBSD 的 ZFS 实现与 Linux 的 ZFS on Linux 实现通过共享代码库实现双向同步，FreeBSD ZFS 代码向 Linux 流出，Linux ZFS on Linux 代码向 FreeBSD 回流；bhyve 自 2013 年由 Pluribus Networks 移植到 illumos，2017 年末 Pluribus 将代码贡献给 illumos 社区，2021 年 7 月 Joyent 基于 FreeBSD-11.1 整合至其 illumos 分支并持续改进。BSD 代码正向流出的工程机制体现 BSD 许可证 “允许无回馈采用” 的设计意图——采用者无需贡献代码即可使用，但 BSD 阵营通过基本系统采纳、独立项目 fork、跨项目代码同步三种机制使代码扩散至全球软件基础设施
- BSD 代码的双向流动并非仅是 BSD→ 其他项目的单向流出，亦存在其他项目 →BSD 的反向回流——（1）**OpenZFS 反向回流**：ZFS 最初由 Sun Microsystems 于 2005 年 11 月随 Solaris 10 引入，2008 年 4 月由劳伦斯利弗莫尔国家实验室（LLNL）的 Brian Behlendorf（布莱恩·贝伦多夫） 等将 ZFS 移植到 Linux（ZFS on Linux，ZoL）〔订正注：原“LLVM 国家实验室”系专名错配（LLVM 为编译器项目），依核查报告订正〕，2013 年 9 月 ZFS on Linux 与 illumos ZFS 团队合并成立 OpenZFS 项目后，FreeBSD 的 ZFS 实现与 Linux 的 ZFS on Linux 实现通过共享代码库实现双向同步；freebsd.duckdb 查询 L7.2.1 显示：衍生项目贡献者在 freebsd-src 的回馈 commit 前 10 位中，<behlendorf1@llnl.gov>（LLNL，OpenZFS 核心开发者）2,603 次（2008-11-20 至 2026-06-06），<hutter2@llnl.gov>（LLNL）342 次（2016-02-29 至 2026-06-22），<mahrens@delphix.com>（Delphix）229 次（2012-08-24 至 2023-11-28），反映 LLNL/Delphix 等 OpenZFS 核心开发者向 FreeBSD 反向回流代码的事实；FreeBSD 与 OpenZFS 的双向同步使 FreeBSD ZFS 与 Linux ZFS on Linux 在功能上保持一致，但 FreeBSD ZFS 在 Capsicum 沙箱集成、jail 隔离等 BSD 特有功能上保留独立实现；（2）**CHERI 反向回流**：CHERI 项目由剑桥大学 Robert Watson 等主持，与 Arm、SRI International 合作开发 CHERI-MIPS 与 CHERI-RISC-V 架构，CHERI 代码进入 FreeBSD 作为 cheribsd 分支维护；CHERI 反向回流体现学术界向 BSD 项目的代码贡献；（3）**LLVM 反向回流**：FreeBSD 开发者 Roman Divacky、Brooks Davis、Ed Maste（埃德·马斯特）、David Chisnall（戴维·奇斯纳尔） 等长期贡献 Clang/LLVM 上游，FreeBSD 基金会赞助 LLVM 的 ARM64 后端、MIPS 后端开发；LLVM 上游的 BSD 开发者贡献反向回流至 FreeBSD 基本系统（FreeBSD 10.0 起 Clang 替代 GCC 成为默认编译器）；BSD 与 LLVM 的双向流动是 BSD 阵营 “去 GPL 化” 战略的关键组成部分。BSD 代码双向流动的反向回流机制体现 BSD 许可证的 “双向兼容性”——BSD 许可证允许其他项目（如 OpenZFS、LLVM）的代码以兼容许可证回流至 BSD 项目，而 GPL 项目的代码则受 copyleft 限制无法直接回流至 BSD 基本系统
- BSD 许可证作为最早的开源许可证之一，其条款结构被后续多个宽松许可证借鉴——（1）**MIT 许可证与 BSD-2-Clause 的关系**：MIT 许可证（又称 Expat 许可证）的条款结构与 BSD-2-Clause 极为相似，二者均包含 “版权声明” “许可授予” “按现状提供” “不承担担保责任” 四要素，主要差异在条款表述（MIT 更简洁，BSD-2-Clause 更明确）；OSI 许可证列表将二者均归为 “宽松许可证”，FSF 许可证注释亦称 “MIT 许可证与 BSD-2-Clause 实质等价”；BSD-2-Clause 成为现代 BSD 项目（FreeBSD、Nginx、Varnish 等）的主流选择，MIT 许可证则在 X Window System 与现代 JavaScript 生态（如 npm 包）中扩散；（2）**Apache 2.0 与 BSD 的演化关系**：Apache 2.0 许可证由 Apache 软件基金会于 2004 年 1 月发布，在 BSD/MIT 的 “版权声明 + 许可授予 + 不承担担保” 基础上增加了两项关键条款——专利反制条款（第 3 条）与贡献者协议（第 5 条）；Apache 2.0 的专利反制条款是 BSD/MIT 所无的，此条款旨在解决 BSD/MIT 在专利诉讼中的脆弱性；Apache 2.0 在 2000 年代后随 Apache 软件基金会项目扩散，成为 Hadoop、Spark、Kubernetes 等大型项目的首选许可证；（3）**BSD 许可证演化（4 条款 →3 条款 →2 条款）**：BSD 4-Clause（原版 BSD 许可证）包含 “版权声明” “许可授予” “不承担担保” “广告条款”（要求所有采用者在广告材料中注明 “本产品包含由加州大学伯克利分校及其贡献者开发的软件”）四要素；BSD 3-Clause（1999 年 7 月 22 日由 William Hoskins 在 ftp.cs.berkeley.edu 公告中宣布移除广告条款）移除广告条款，保留 “版权声明” “许可授予” “不承担担保” “未获背书” 四要素；BSD 2-Clause（Simplified BSD License 或 FreeBSD License）进一步移除 “未获背书” 条款，仅保留 “版权声明” “许可授予” “不承担担保” 三要素；BSD 许可证演化反映社区对广告条款与背书条款的反对，以及 BSD 许可证向 MIT 简洁性的靠拢。BSD 许可证作为模板被其他许可证借鉴体现 BSD 许可证在许可证谱系中的 “基础设施性”——其条款结构成为后续宽松许可证的基础，但 BSD 标签被 MIT/Apache 等后续许可证的 “品牌化” 掩盖
- BSD 项目的贡献者协议与版权治理呈现 “去中心化” 特征——（1）**FreeBSD 的贡献者协议**：FreeBSD 项目采用 “开发者原创证书”（Developer Certificate of Origin，DCO）作为贡献者协议基础，贡献者通过 `Signed-off-by` 行声明其贡献原创且有权提交〔存疑：通行记载 FreeBSD 无正式 CLA 亦无强制 Signed-off-by 体例，DCO 系 Linux 内核体例，本条宜以 FreeBSD 官方治理文档核限〕；FreeBSD 项目未采用 “贡献者许可协议”（Contributor License Agreement，CLA），与 Apache 软件基金会、Google 等要求 CLA 的项目形成对比；FreeBSD 项目的提交者权限授予由核心团队或 Ports 管理团队（portmgr）基于现有提交者提名决定，提名标准缺乏量化门槛（如最低 commit 数、最低贡献时长等）；（2）**版权归属演化**：BSD 代码的版权归属经历 CSRG（加州大学伯克利分校）→ FreeBSD 基金会 → 个人版权的演化——CSRG 时期（1980-1995）BSD 代码版权归属加州大学董事会；FreeBSD 项目早期（1993-2000）代码版权归属 FreeBSD 项目或个人开发者；FreeBSD 基金会成立后（2001 年起）部分代码版权归属 FreeBSD 基金会，但多数代码保留个人开发者版权；FreeBSD 源代码中可见 “The Regents of the University of California”（CSRG 时期遗留）、“The FreeBSD Project”（项目版权）、个人开发者姓名（个人版权）三类版权声明并存；OpenBSD 项目的版权治理更简单——多数代码版权归属个人开发者或 OpenBSD 项目，无基金会持有版权；（3）**与 Linux 的对比**：Linux 内核采用 DCO（与 FreeBSD 类似）但未采用 CLA，与 FreeBSD 的贡献者协议模式相似；但 Linux 内核的维护者层级制（maintainer hierarchy）与 FreeBSD 的 “信任即授予” 模型形成对比——Linux 要求贡献者通过补丁积累声誉后方能获得维护者地位，FreeBSD 的权限授予路径相对更短；（4）**与 Apache 的对比**：Apache 软件基金会要求所有贡献者签署 Apache ICLA（个人贡献者许可协议）与 Apache CCLA（企业贡献者许可协议），授予 Apache 软件基金会知识产权许可；Apache CLA 模式与 FreeBSD DCO 模式形成对比——Apache 模式集中版权治理，FreeBSD 模式分散版权治理。BSD 项目的贡献者协议与版权治理体现 BSD 阵营 “去中心化” 的治理哲学——通过 DCO 而非 CLA 实现贡献者协议，通过个人版权而非基金会版权实现版权归属，但此 “去中心化” 亦产生提交者权限授予标准模糊、版权归属分散等治理缺陷
- BSD 许可证与其他主流开源许可证的兼容性矩阵呈现 “单向兼容” 特征——（1）**BSD 与 GPL 的兼容性**：BSD-2-Clause 与 BSD-3-Clause 均与 GPLv2、GPLv3 兼容，BSD 代码可进入 GPL 项目（如 Linux 内核中保留的部分 BSD 代码），但 GPL 代码不可进入 BSD 项目（因 GPL 的 copyleft 条款要求衍生作品亦采用 GPL）；Linux 内核源代码中可 grep 到 “Regents of the University of California” 版权声明，证明 BSD 代码进入 Linux 内核；BSD 与 GPL 的单向兼容性是 BSD 阵营 “去 GPL 化” 战略的动因——FreeBSD 10.0 起 Clang 替代 GCC 成为默认编译器，部分原因是 GCC 在 GPLv3 转换后因下游消费者反对未能进入 FreeBSD 基本系统；（2）**BSD 与 Apache 2.0 的兼容性**：BSD-2-Clause 与 Apache 2.0 兼容，Apache 2.0 代码可进入 BSD 项目（如部分 Apache 软件基金会库被 FreeBSD 采用），BSD 代码亦可进入 Apache 项目；BSD 与 Apache 2.0 的双向兼容性源于二者均为宽松许可证且 Apache 2.0 的专利反制条款不与 BSD 冲突；（3）**BSD 与 MIT 的兼容性**：BSD 与 MIT 高度兼容，二者均为宽松许可证，可双向流通；MIT 许可证在 X Window System、JavaScript 生态中的扩散与 BSD 许可证在 UNIX 生态中的扩散形成互补；（4）**BSD 与 MPL 2.0 的兼容性**：BSD 与 MPL 2.0（Mozilla Public License 2.0）兼容，MPL 2.0 的弱 copyleft 条款（文件级 copyleft）不与 BSD 冲突，二者可双向流通；MPL 2.0 在 Mozilla Firefox、Redis（2024 年改为 RSALv2/SSPLv1 前曾考虑 MPL 2.0）等项目中应用；（5）**BSD 与 CDDL 的兼容性**：BSD 与 CDDL（Common Development and Distribution License，Sun Microsystems 基于 MPL 1.0 修改）兼容，CDDL 代码可进入 BSD 项目（如 OpenZFS 的 CDDL 代码进入 FreeBSD 基本系统），但 CDDL 与 GPL 不兼容（此为 Sun 选择 CDDL 而非 GPL 发布 OpenSolaris 的原因之一）；OpenZFS 在 FreeBSD 中以 CDDL 许可证保留，与 FreeBSD 基本系统的 BSD 许可证并存。BSD 许可证与其他许可证的兼容性矩阵体现 BSD 许可证的 “基础设施性”——BSD 代码可进入几乎所有其他许可证体系（GPL、Apache、MIT、MPL、CDDL），但其他许可证代码进入 BSD 受 copyleft 条款限制——此 “单向兼容” 是 BSD 阵营 “去 GPL 化” 战略的许可证层面动因

## 史观

- 总纲第 4 条——分离聚合是永恒规律（见 据原文第 4 章 4.1 节）：“UNIX 分裂出各种 BSD，BSD 又分裂出 FreeBSD、NetBSD、OpenBSD、DragonFly BSD，此乃分离；而各分支间的代码共享、ports 互通、社区人员的流动，此乃聚合”——BSD 代码正向流出至 macOS、Linux、illumos 等是 “聚合” 的具体显现〔订正注：原行末“；总纲第 24 条——应用于 B”系伪标签截断残尾，权威表第 24 条为“美是消解性的体验”，与本论旨不符，依核查报告删〕
- 总纲第 4 条（分离聚合是永恒规律）、总纲第 6 条（和解优于斗争）、总纲第 13 条（法律与道德是利益分配）、专题语“应用于 BSD 史编纂”（不设总纲条号〔订正注：原挂“总纲第 24 条”，权威表第 24 条为“美是消解性的体验”，与本论旨不符，依核查报告去条号〕）、总纲第 7 条（理论必须自反）。BSD 代码双向流动与许可模式扩散的核心即 “工程双向流动与许可证单向兼容的辩证统一”——BSD 代码在工程层面双向流动，但在许可证层面单向兼容，二者是同一 BSD 许可证的两面。〔订正注：原〔待核：原文截断，后文待回源〕销解——现存文句已自足，截断余文无法回源放弃〕
- 总纲第 4 条（分离聚合是永恒规律）、总纲第 6 条（和解优于斗争）、总纲第 13 条（法律与道德是利益分配）、总纲第 7 条（理论必须自反）。此四条总纲在 BSD 代码双向流动与许可模式扩散中形成四层审视：第一层（分离聚合）揭示代码双向流动是分离聚合的工程化显现；第二层（和解优于斗争）揭示 BSD 阵营通过代码双向流动实现与其他主体的和解，但此 “和解” 非 “投降”。〔订正注：原〔待核：原文截断，后文待回源〕销解——本条自第三层起截断且无法回源，按前两层收束，余两层论旨见上条与自反性声明〕

## 辨析

- 考据过程留痕——【查证来源】libarchive 官网采用列表（libarchive.github.io）经一手核验明确列出 macOS、Debian/Ubuntu、Homebrew 等采用方；jemalloc 在 Rust 中的默认分配器地位经 Rust RFC 1974 与 Rust 1.28 release notes 核实，2018 年 8 月后默认分配器已切换为系统分配器，但 jemalloc 仍经由 tikv-jemallocator crate 被大量 Rust 项目主动选用〔订正注：原行自“但 jemal”截断，按本文件要点同款表述补全〕
- 考据过程留痕——【查证来源】openzfs.duckdb 查询 L3.2.1（商业实体 commit 占比长期低于 1.3% 但绝对值增长）与 L7.2.1（衍生项目贡献者回馈前 10 位）经 SQL 查询一手核验；OpenZFS 项目公告（2013 年 9 月成立）经 openzfs.org 一手核验；libarchive 官网采用列表经 libarchive.github.io 一手核验〔订正注：原行末“；je”起截断（疑为 jemalloc 条重起），无法回源，依核查报告删〕
- 考据过程留痕——【查证来源】项目史观总纲第 4、6、7、13 条经原材料/哲学/项目统摄史观/第 25 章.md 一手核验，原文分别为 “分离聚合是永恒规律。UNIX 与 BSD、BSD 各分支之间的分合循环，是历史的根本结构” “和解优于斗争。历史的动力不是对抗，而是各主体性的呈现与和解。和解是事物真正完整的状态” “法律与道德是利益分配。任何道德问题本质上是利益问题，社区治理亦是形式主义的政治”〔订正注：末句原至此截断，补闭合引号收束；“一刻”系禁用名称改中性“状态”〕

## 文献

- libarchive. Official Website [EB/OL]. <https://libarchive.github.io/>; jemalloc.net [EB/OL]. <https://jemalloc.net/>; Rust RFC 1974. Global Allocator API [S/OL]. 2017; OpenSSH. Official History [EB/OL]. <https://openssh.org/history.html>; OpenZFS Project Announcement [EB/OL]. 2013-09, <https://openzfs.org/>〔订正注：原“<<https://openz>”系双左尖括号＋截断，按同文件下条同款著录回填完整 URL〕
- openzfs.duckdb L3.2.1 查询报告（深层信息挖掘.md §L3.2.1）; openzfs.duckdb L7.2.1 查询报告（衍生项目与跨项目对比分析.md §L7.2.1）; OpenZFS Project. Announcement [EB/OL]. 2013-09, <https://openzfs.org/>; libarchive. Official Website [EB/OL]. <https://libarchive.github.io/>; jemalloc.net [EB/OL]. <https://jemalloc.net/>〔订正注：原行末“; Joyent. Re”起截断，无法回源，依核查报告删〕
- 项目史观总纲第 4、6、7、13 条 [Z]. 原材料/哲学/项目统摄史观/第 25 章.md; 项目史观总纲第四章 “循环与否定” [Z]. 原材料/哲学/项目统摄史观/第 04 章.md; 项目史观总纲第六章 “主体性与和解” [Z]. 原材料/哲学/项目统摄史观/第 06 章.md; 项目史观总纲第十一章 “法哲学与政治历史哲学” [Z]. 原材料/哲学/项目统摄史观/第 11 章.md; 项目史观总纲第二十七章 “自反：对理论困境的回应” [Z]. 原材料/哲学/项目统摄史观/第 27 章.md; bsd_commits.duckdb L3.2.1 查询报告〔订正注：原行末另起“; bsd_commits.duckdb L”即断，系截断残尾，依核查报告删〕

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP507（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Lucas 回顾 OpenBSD 文件系统：OpenBSD 沿用源自 4.4BSD 的 UFS1（约 1994 年稳定）并长期调试，随后在 2000 年代早期采用较早期版本的 UFS2；相较 ZFS、btrfs 等新文件系统，OpenBSD 的 UFS 哲学是把文件系统保持简单，认为功能即缺陷。（BSD Now EP507，[489.90-760.60]，L1）
- Lucas 以 PF 与 UFS 为例说明 BSD 各分支之间的代码双向流动：OpenBSD 的 PF 被 FreeBSD 移植并各自演进，反过来 FreeBSD UFS2 在 OpenBSD 移植之后才开发快照，形成方向相反的技术借取与债务。（BSD Now EP507，[583.98-612.94]，L1）
- Lucas 讲述其考证的 1978 年第一封垃圾邮件：DEC 的 Gary Thuerk 为推广新产品向数百名陌生用户群发邮件，五天后美国空军 ARPANET 管理分支负责人致电其上司警告，但该邮件仍促成约 1200 万美元计算机销售，埋下垃圾邮件经济动机的起点。（BSD Now EP507，[1351.12-1453.32]，L2）
- 关于生成式 AI，Lucas 认为 ChatGPT 只产出看似答案的文本而非答案，越长的内容越易失实；他援引美国国会图书馆已裁定 AI 生成文本不可版权，并主张作者与读者直接连接的重要性上升。（BSD Now EP507，[2281.44-2813.20]，L1）
- Lucas 介绍其邮件服务器写作计划，强调 SPF、DKIM、DMARC 等外围协议已成自建邮件的前提，DKIM 虽 2011 年即存在，其强制要求却是近年才出现。（BSD Now EP507，[1108.24-1277.00]，L1）

**史料**：

- Michael W. Lucas《OpenBSD Mastery: Filesystems》一书，为当期采访对象本人撰写的文件系统专著，属于当事人一手出版物。（BSD Now EP507，[126.18-172.34]，L1）
- 1978 年 Gary Thuerk 垃圾邮件事件为 Lucas 写作邮件书籍时考证的历史线索，经当期采访口头转述。（BSD Now EP507，[1351.12-1453.32]，L2）
- BSD 各分支在 PF 与 UFS 上的双向代码流动，为 Lucas 作为长期 BSD 作者与使用者的工程观察，属二手叙述。（BSD Now EP507，[583.98-612.94]，L2）

**史观**：

- 总纲4 分离聚合是永恒规律：各 BSD 分支不断分离又借取聚合，代码流动呈现双向循环而非线性派生。：BSD 各分支在 PF 与 UFS 上相互分离又聚合，代码双向流动而非单向派生。（BSD Now EP507，[583.98-612.94]，L1）
- 总纲10 动手者创造历史：作者以专著记录长期维护与调试的工程细节，凸显沉默维护者的历史作用。：Lucas 以文件系统著作为动手者记录维护者的工程现实，而非只写台前叙事。（BSD Now EP507，[489.90-760.60]，L1）
- 总纲13 法律与道德是利益分配：SPF、DKIM、DMARC 等协议是邮件生态围绕送达与信任利益形成的规范分配。：垃圾邮件的持续源于首次群发所揭示的经济收益，反垃圾协议是围绕邮件送达利益而演化的规范分配。（BSD Now EP507，[1351.12-1453.32]，L2）

**辨析**：

- 1978 年第一封垃圾邮件的约 1200 万美元销售额及军方联系人姓名为 Lucas 口头转述，需以 ARPANET 原始记录与既有垃圾邮件史研究交叉验证。　[存疑脚注] 金额与军方联系人姓名拼写为单一来源口头叙述，须以原始档案核验。（BSD Now EP507，[1351.12-1453.32]，L4）
- Lucas 对 OpenBSD UFS2 缺乏快照、FreeBSD 在 OpenBSD 移植后才开发快照的时间先后判断为当事人概括，须以两分支 UFS2 提交史核验。　[存疑脚注] 快照特性的先后次序为当事人口头判断，需以 FreeBSD 与 OpenBSD 的 UFS2 提交记录核验。（BSD Now EP507，[583.98-612.94]，L4）

**文献**：

- [BSD Now EP507] Pennington J. BSD Now: 507: Michael W. Lucas Interview[EB/OL]. (2023-05-18)[2026-08-15]. <https://www.bsdnow.tv/507>.

<!-- /PODCAST_REVIEW -->

## 史料

- [DB:historical_claims:claim] 关键词行级挖掘素材线索 289.9-关键词行级挖掘素材线索（5 条，CL-RM 段，见 289.9-关键词行级挖掘素材线索.md）

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-573 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-573`；w172 YouTube 章节路由采纳）

据〔November 2023 FreeBSD Vendor Summit〕讲者 Alan Jude 口述：ZFS 需支持 Linux 内核 3.6 至 6.6 的跨版本工作（YouTube EPh5C97dwIjM8，[1422.88-1432.669]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-571 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-571`；w172 YouTube 章节路由采纳）

据〔November 2023 FreeBSD Vendor Summit〕讲者 Alan Jude 口述：Alan Jude 为 Clara 的 CTO 与联合创始人，使用 FreeBSD 逾 20 年（YouTube EPh5C97dwIjM8，[72.04-79.63]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-572 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-572`；w172 YouTube 章节路由采纳）

据〔November 2023 FreeBSD Vendor Summit〕讲者 Alan Jude 口述：为客户在 0.7 分支上开发特性时面临诸多挑战，首要是 OpenZFS 0.7 时期 Solaris 移植层与 ZFS 本体分属两个 git 仓库（0.8 起已合并），回移植相关修复困难。（YouTube EPh5C97dwIjM8，[1204.28-1212.99]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1175 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1175`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者口述：讲者接触到的嵌入式产品中，操作系统几乎都是 Linux，而非 FreeBSD、OpenBSD、NetBSD、HardenedBSD、DragonFlyBSD 等 BSD 各系。（YouTube EPyUY09ocwiUQ，[2433-2449.8]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1176 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1176`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者口述：NetBSD 与 FreeBSD 的 sys 代码行数几乎相同但 CVE 数量不同；NetBSD 在日本 IIJ 的路由器上被广泛部署，讲者未能找到两者完整的用户列表。（YouTube EPyUY09ocwiUQ，[585.2-617.9]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->
