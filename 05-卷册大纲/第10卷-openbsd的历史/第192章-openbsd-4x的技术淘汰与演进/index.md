---
chapter: 第 192 章
id: CH192
volume: 第10卷-openbsd的历史
---

# 第 192 章 openbsd-4x的技术淘汰与演进

## 要点

- OpenBSD 3.0（2001.12）引入 vnd 块设备的加密模式 svnd，使用 Blowfish 算法；OpenBSD 4.x 时期持续改进加密栈——softraid 加密引入周期待考〔存疑：2007-11-27 commit f18dcc9c26b1 实为“split crypto functions out into their own file”重构拆分而非加密首次引入，且该日期晚于 4.2 发布（2007-11-01），属 4.3 开发周期；加密首次引入的确切 commit 待回源〕，2008-06-14 hshoexer commit 79cdc9424edb 完整启用（4.4 周期），支持 AES
- 2006-2009 防火墙格局：OpenBSD 4.x 的 pf 为 BSD 事实标准（流向 FreeBSD/NetBSD/DragonFly BSD），Linux 以 iptables/netfilter 主导，Windows 基础防火墙闭源；pf 的简洁锚点规则影响后续 BSD 防火墙设计，成为 OpenBSD 4.x 的工程标志
- gcc GPLv3 争议的合图层论点包含三个历史定位。第一是 GPLv3 与 ISC 的根本分歧是许可证哲学而非技术问题——FSF 的 copyleft 与 OpenBSD 的 ISC 是两种自由观的对立（FSF “用户自由” vs OpenBSD “采纳者自由”）〔待核：原文截断，后文待回源〕
- openbsd 代码仓库共 491,195 次提交（1995-10-18 至 2026-08-25），1,031 位贡献者
- OpenBSD 4.x 时期的本地漏洞与网络栈漏洞分散于 pf 规则拷贝、X11 转发、Apache 跨站脚本等组件——CVE-2008-1483 为 X11 转发连接劫持漏洞，markus 于 2008-04-02 通过回退 commit 1.183 修复（commit `39ff0b053b9574ba427fa40f29afcc8ceea31f3d`），技术机制类型为信息泄露，无 CVSS

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4093] 卷“第10卷-openbsd的历史”第 192 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充
- [DB:references_fulltext:chapter_matches:chmatch_4094] 卷“第10卷-openbsd的历史”第 192 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充
- [DB:bsdnow_podcast:outline_mappings:om_11440] BSD Now 第 536 期，匹配 CH192 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_12226] BSD Now 第 445 期，匹配 CH192 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_10479] BSD Now 第 665 期，匹配 CH192 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10544] BSD Now 第 654 期，匹配 CH192 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10581] BSD Now 第 646 期，匹配 CH192 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10642] BSD Now 第 637 期，匹配 CH192 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10773] BSD Now 第 617 期，匹配 CH192 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11147] BSD Now 第 571 期，匹配 CH192 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11211] BSD Now 第 563 期，匹配 CH192 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11363] BSD Now 第 546 期，匹配 CH192 章，关联度 1.0

## 史观

（章级史观不另设条号：本章史观映射详见各子节文件的“史观/辨析”字段与本章 index 史观映射段，避免与子节重复错挂）

## 辨析

- svnd 与 softraid 的关系以 bsd_commits.duckdb commit log 为准——softraid 首次 commit 为 2007-03-19 dlg commit 98855ba5cdbc “attach softraid to the root of the device tree”，是新的 RAID 框架，加密是其子功能；AES-XTS 支持的具体引入版本以 **sof**
- 防火墙选择受生态与许可影响——pf 的 BSD 许可促进跨 BSD 流动，iptables 的 GPL 许可限制其向 BSD 项目回流；OpenBSD 4.x 的 pf 创新源地位以 openbsd.duckdb openbsd-src 仓库 pf 相关 commit 的 author_date 与 freebsd-src 仓库 pf import commit 的 tagger_date 交叉确
- 考据过程留痕——【查证来源】FreeBSD、NetBSD、OpenBSD、DragonFly BSD 切换至 clang/LLVM 的具体时间以各自 Release Notes 为准——FreeBSD 10.0（2014.1）将 clang 作为默认编译器，OpenBSD 5.7（2015.5）完成切换，二者间隔约 17 个月；【交叉验证方法】OpenBSD pcc 导入与 clang/LLVM
- 数据库统计受 CVS-to-Git 迁移、镜像滞后等因素影响，commit 数量与贡献者统计存在系统性偏差，须结合一手史料交叉验证
- CVE-2008-1483 的 X11 转发劫持与被回退的 commit 1.183 之间的因果关系须考据——commit 1.183 引入了什么变更导致劫持风险；pf 规则拷贝漏洞无 CVE 编号的原因须考据——是未被分配 CVE 还是 OpenBSD 未在 commit 中引用；CVE-2011-2748/CVE-2011-2749 的“选项处理栈存储清零”具体涉及哪个程序须对照 commit

## 文献

- openbsd.duckdb openbsd-src 仓库 commit 98855ba5cdbc、f18dcc9c26b1、79cdc9424edb；OpenBSD Release Notes [EB/OL]. <https://www.openbsd.org/plus.html>；OpenBSD **softraid(4)** 手册页 [EB/OL]. <https://man.openbsd.org/softraid.4> ［A］FreeBSD 社区论文：[FP-2022-001] Refining FreeBSD's Kernel Crypto Framework（John Baldwin（约翰·鲍德温），2022）<https://papers.freebsd.org/2022/bsdcan/baldwin-refining_freebsds_kernel_crypto_framework/>FreeBSD 社区论文：[FP-2021-008] smart(8) Update: A Permissively-Licensed Alternative to smartctl(8)（Michael Dexter（迈克尔·德克斯特）; Chuck Tuffli，2021）<https://papers.freebsd.org/2021/eurobsdcon/dexter-tuffli-update_on_smart/>FreeBSD 社区论文：[FP-2019-076] FreeBSD at Work: Building Network and Storage Infrastructure with pfSense and FreeNAS（Conor Beh，2019）<https://papers.freebsd.org/2019/vbsdcon/beh-freebsd_at_work/>FreeBSD 社区论文：[FP-2019-002] BSD Unix Solutions in the Australian NFP/NGO Health Sector（Jason Tubnor，2019）<https://papers.freebsd.org/2019/asiabsdcon/tubnor-bsd_unix_solutions_in_the_australian_nfp_ngo_health_sector/>FreeBSD 社区论文：[FP-2019-014] LLVM and the state of sanitizers on BSD（David Carlier，2019）<https://papers.freebsd.org/2019/asiabsdcon/carlier-llvm_and_the_state_of_sanitizers_on_bsd/>FreeBSD 社区论文：[FP-2018-010] Preparing your home router(s) for the future: A journey through Homenet and interconnected objects（Massimiliano Stucchi，2018）<https://papers.freebsd.org/2018/bsdcan/stucchi-preparing_your_home_routers_for_the_future/>FreeBSD 社区论文：[FP-2017-014] Isolated BSD build environments using virtual and hardware machines（Michael Dexter，2017）<https://papers.freebsd.org/2017/vbsdcon/dexter-isolated_bsd_build_environments_using_virtual_and_hardware_machines/>FreeBSD 社区论文：[FP-2017-009] My BSD sucks less than yours（Baptiste Daroussin（巴蒂斯特·达鲁桑） Antoine Jacoutot（安托万·雅库托），2017）<https://papers.freebsd.org/2017/fosdem/bapt-my_bsd_suck_less_than_yours/>

### 史观映射

OpenBSD 4.x 时期是项目统摄史观中 “形式主义化” 与 “修道度人” 在网络安全领域的双重实践。6 个月发布周期作为形式主义化结构（总纲第 15 条——文化即形式主义），将时间固化为不可动摇的规则——krw@ 与 espie@ 的 release engineering 工作严格遵循 5 月与 11 月的节奏，这一形式化结构带来稳定性与可预测性，但也限制了单周期内的重大架构重构。pf 的持续演进是 “修道度人” 的工程实践（总纲第 15 条——文化即形式主义）——claudio@ 与 henning@ 在 2005-2010 年间持续改进 pf，让 pf 守护着无数网络的边界，但 pf 的作者们很少在公众视野中出现。CARP 冗余协议的开发是对法律结构障碍的重新设计（总纲第 13 条——法律与道德是利益分配）——当 VRRP 协议的 Cisco 专利 US 5,473,599 成为障碍时，OpenBSD 选择重新设计协议（CARP）而非寻求专利授权，这一选择是法律结构对技术实现的直接塑造。malloc 替代（tedu@ 2006-10-24 commit 66e23c51）是 “边缘者承担安全关键基础设施” 的具体显现（总纲第 10 条——动手者创造历史）——OpenBSD 的 malloc 安全替代由单一开发者响应安全研究社区的漏洞披露而实现，非由大厂商团队推动。softraid 加密的引入（tedu@ 2007-11-27 commit f18dcc9c26b1 至 hshoexer@ 2008-06-14 commit 79cdc9424edb）是密码学标准演进对操作系统实现的具体塑造（总纲第 22 条——知识注定过时）——AES-XTS 作为 NIST SP 800-38E 推荐模式取代 Blowfish。de Raadt 的个人主导模式是 “动手者” 存在主义的体现——一个人在不被理解中坚持自己的工程哲学，BDFL 治理（总纲第 15 条——文化即形式主义）使 OpenBSD 在 4.x 时期保持技术方向一致性。

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 2005-2010 年间：100,198 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。
- OpenBSD pf 指南 [EB/OL]. <https://www.openbsd.org/faq/pf/>；freebsd.duckdb freebsd-src 仓库 pf import commit；BSD 防火墙比较文档 ［B］

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 2006-2009 年间：65,854 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。
- de Raadt、espie@ 邮件列表发言 [EB/OL]. <https://marc.info/?l=openbsd-tech>；otto. Import ragge's version of PCC. openbsd-src [DB/OL]. 2007-09-15T18:12:23Z. 60b4da4bc6418e6654a995e733a66436798b5bc0；openbsd.duckdb openbsd-src 仓库 clang/LLVM 相关 commit；FreeBSD 10.0 Release Notes [EB/OL]. <https://www.freebsd.org/releases/10.0R/relnotes/>；OpenBSD 5.7 Release Notes [EB/OL]. <https://www.openbsd.org/57.html>；Linux 发行版编译器文档；FSF 与 OpenBSD 许可证文档 ［A］

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。
- openbsd.duckdb openbsd-src 仓库；NVD CVE-2008-1483/CVE-2006-5752/CVE-2007-3304/CVE-2007-5000/CVE-2007-6388/CVE-2011-2748/CVE-2011-2749；OpenBSD 4.x errata patches [EB/OL]. **<https://www.openbsd.org/errata.html>** ［A］

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 2006-2012 年间：112,057 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。
- OpenBSD 官网 release 页面 ［EB/OL］. <https://www.openbsd.org/40.html> 至 <https://www.openbsd.org/49.html>；<announce@openbsd.org> 邮件列表存档 ［EB/OL］. <https://marc.info/?l=openbsd-announce>；**03-原始史料库/06-考据记录**（原引“**原材料/研究/考据记录/20260723_announcements-openbsd.md**”，该路径全库未检出〔存疑〕）；openbsd.duckdb openbsd-src 仓库 ［A］

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSDTalk EP204（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- mandoc（mdocml）起源与分工：Kristaps Dzonsons 因不满 grohtml 丑陋输出与直接转储 ASCII 去转义字符的做法、希望以 CSS 自定义手册外观，自 2008 年 11 月前后着手编写 mandoc，2009 年应 Theo de Raadt 邀请提交进入 OpenBSD，并于 AsiaBSDCon 2010 春发表；此后 Kristaps 主理上游 bsd.lv 仓库，Ingo Schwarze 接掌 OpenBSD 下游、先整合 Kristaps 补丁、逐渐成为这一复杂代码库的权威，两人自此协作推进。（BSDTalk EP204，[134.60-259.34]，L1）
- 语义立场：mdoc 是语义标记语言——如同 Web 设计中指定强调而非斜体——可用文本编辑器徒手书写，紧凑而信息丰富；groff 本质是强大的文本排版工具，只关心呈现；mandoc 则把 mdoc 视为语言本身，编译手册时保留全部语义信息并依语义行事；旧 man 格式与多数 Linux 手册不含语义内容、只是呈现块，而 mdoc 手册对函数、变量、头文件等要素均有结构标注。（BSDTalk EP204，[446.77-537.22]，L1）
- 输出与检索能力：mandoc 的 XHTML/HTML 输出附丰富 CSS 注释、可经少量适配纳入 EPUB 供小屏阅读；其 PDF 与 PostScript 输出仍臃肿、有待专人改进；makewhatis 工具从手册抽取语义内容建库，支撑按函数名、头文件、标准与作者等维度检索与挖掘，并已有演示搜索引擎——手册的语义化利用由此从长期设想变为可操作现实。（BSDTalk EP204，[571.58-733.10]，L1）
- OpenBSD 集成动机：树中 groff 1.15 已逾十年且多 bug，手册维护者 Jason McIntyre 被迫设计大量技巧绕过其缺陷；升级到新版 groff 不可行，因其已是 GPLv3 许可；手册格式化必须迅速，groff 方案依赖预格式化安装而丧失全部结构；OpenBSD 因此计划改为安装未格式化手册，以期在数月至一年内提供大幅改善的 apropos 与 man -k 结构化检索。（BSDTalk EP204，[275.42-414.46]，L1）
- BSD 文档文化比较与批评：OpenBSD 尽量把文档集中于一处手册、仅 FAQ 为例外；FreeBSD 文档散布于书籍、网页等多种媒介，虽自称重视文档，但其 developer summit 的文档议程全然围绕书籍而不提手册；FreeBSD 手册的语法错误在各 BSD 中最多，经语法校验器即可发现；FreeBSD 官方已宣布把文档迁往 SGML/XML（DocBook），但手册仍以 man 与 mdoc 维护——一步未完成已规划下一步；且一旦真迁移，格式化工具为 GPLv3 而无法进入基本系统，工具链迟早断裂，出路之一正是坚持 mdoc 这样简单可靠的手册格式。（BSDTalk EP204，[736.58-968.18]，L1）
- 语言哲学与治理：mdoc 的价值在于好不是因为老、而是尽管老仍然好——新格式标榜的语义注释、机器可解析性与跨文档链接它都能干净实现，改用更复杂的格式只会平添复杂；GNU info 在文档内层次链接上占优，但手册页通常不至太长、页间链接大体够用；语言演进宜先在 OpenBSD 完成整合并补齐初学者教程（现有 mdoc 参考手册已优于既有样本但仍需教程），且文档语言必须保持简单；Kristaps 立场更硬线，认为不认真学习文档语言的程序员应重新考虑自身资格，Ingo 则强调简单性是不可让渡的前提。（BSDTalk EP204，[969.70-1421.00]，L1）
- 兼容性与可移植性：mandoc 的手册明确记录 mdoc 与 groff 之间不兼容的语言构造，解除了历史 groff 每行九参数的限制，与既有 groff 手册完全兼容是项目设计目标之一，并提供 mdoc 减 T lint 校验；工具可移植至各类 Unix——NetBSD、旧 Solaris 与 OpenSolaris、AIX 等均有反馈，可用 PCC、LLVM/clang 与 GCC 编译，稍加改动即可运行于 Windows，makewhatis 依赖 Berkeley DB；OpenBSD 已原生以 mandoc 格式化全部手册。（BSDTalk EP204，[1431.76-1747.22]，L1）

**史料**：

- 一手史料包括 Kristaps 对 mandoc 最早提交与 2009 年受 Theo 邀请入 OpenBSD 时间线的口述、其在 BSDCan 2011 的 mandoc 演进报告指引、Jason McIntyre 绕过 groff 缺陷的技巧叙述，以及 Ingo 对 FreeBSD developer summit 文档议程的现场观察；本访谈录于 BSDCan 2011 会议期间，本身即该会议一手记录。（BSDTalk EP204，[134.60-259.34]，L1）

**史观**：

- 总纲4 分离聚合是永恒规律：mandoc 自 groff 生态中分离而出，却以兼容 groff 既有手册语料为设计目标并与之互通校验，显示工具替代并非简单断裂，而是新实现与旧语料之间的再度聚合。（BSDTalk EP204，[1431.76-1507.66]，L1）

**辨析**：

- mandoc 起始时间的口述在对话中经两人反复修正（2008 年 11 月、2009 年、春季），精确时间线须以仓库提交历史为准；转写人名与术语音误密集——Kristaps Dzonsons 误作 Chris Stapps、groff 音化作 grof 或 grow、apropos 误作 up-hopal、base 误作 Bayes、ports tree 误作 POTS tree——引用前须回查原音频与项目存档。 [存疑脚注] 时间线系口述回忆且对话中自我修正，须以版本库提交记录复核；转写音误密集，术语引用须校正（BSDTalk EP204，[134.60-210.74]，L4）

**文献**：

- [BSDTalk EP204] Backman W. BSDTalk: 204: bsdtalk204 - mdocml mit Ingo Schwarze and Kristaps Dzonsons[EB/OL]. (2011-06-01)[2026-08-27]. <https://bsdtalk.blogspot.com/2011/05/bsdtalk204-mdocml-mit-ingo-schwartze.html>.

<!-- /PODCAST_REVIEW -->
