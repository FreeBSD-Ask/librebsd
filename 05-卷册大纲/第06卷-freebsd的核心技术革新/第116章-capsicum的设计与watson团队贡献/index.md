---
chapter: 第 116 章
id: CH116
volume: 第06卷-freebsd的核心技术革新
---

# 第 116 章 capsicum的设计与watson团队贡献

## 要点

- Capsicum 一手史料主要包括：剑桥大学 Capsicum 项目页面 cl.cam.ac.uk/research/security/capsicum/（持续维护，含论文、演讲、代码、文档链接）；USENIX Security 2010 会议论文集（usenix.org 永久存档）；FreeBSD 源码仓库中 Capsicum 相关提交——经 **freebsd.duckdb** `commit
- Capsicum 能力模型的理论溯源可至 1970 年代的能力系统研究：剑桥大学 CAP computer（1970s，世界首个能力计算机）、PSOS（Provably Secure Operating System，SRI International，Peter G. Neumann 参与）、Hydra（CMU）、KeyKOS（Key Logic，1980s）〔待核：原文截断，后文待回源〕
- 剑桥大学在安全研究领域长期采用 BSD 风格的开放许可策略，这一策略贯穿 Capsicum（2010）至 CHERI（2014+）系列项目：Capsicum 以 BSD 2-Clause 发布、CHERI ISA 规范以 BSD 风格许可证发布、CheriBSD 以 BSD 许可发布；这一策略的代表性先例包括剑桥大学 X Window System（1984，MIT/BSD 风格许可）、剑桥大学在

## 史料

- [DB:bsdnow_podcast:outline_mappings:om_10421] BSD Now 第 676 期，匹配 CH116 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10461] BSD Now 第 669 期，匹配 CH116 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10465] BSD Now 第 667 期，匹配 CH116 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10564] BSD Now 第 651 期，匹配 CH116 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10604] BSD Now 第 642 期，匹配 CH116 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10623] BSD Now 第 639 期，匹配 CH116 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10628] BSD Now 第 638 期，匹配 CH116 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10699] BSD Now 第 629 期，匹配 CH116 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10788] BSD Now 第 615 期，匹配 CH116 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10829] BSD Now 第 609 期，匹配 CH116 章，关联度 1.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 原大纲称 Capsicum 论文作者为 “Watson、Anderson、Laurie、Kenneally” 系名字讹误，第四作者经论文 PDF 核实为 Kris Kennaway（FreeBSD 长期 committer，Google 安全工程师），已修正；〔待核：原文截断，后文待回源〕
- 原大纲文献列表多次错误列入“Lucas 2018 'FreeBSD Mastery: Storage Essentials’”——Storage Essentials 是存储主题书籍，与 Capsicum/CHERI 无关，属于模板复制时未清理的无关文献，已全部删除并替换为 Capsicum/CHERI 相关权威文献；原大纲还列入"Skorstengaard, Devriese, Birkedal
- 原大纲本节称“剑桥大学许可策略史料考证”但列入大量与 Capsicum 无关的文献（如 Lucas Storage Essentials、Skorstengaard CHERI 论文等），已修正为 Capsicum 许可策略专属史料；Capsicum 是否曾使用过其他许可证名称（如“BSD License”“University of Cambridge License”）经剑桥项目页面核实均为

## 文献

- University of Cambridge Computer Laboratory. Capsicum Project Documentation. cl.cam.ac.uk/research/security/capsicum/; USENIX Association. Proceedings of the 19th USENIX Security Symposium (2010). usenix.org; FreeBSD Project. FreeBSD 9.0-RELEASE Release Notes (2012-01-12). freebsd.org; Google. capsicum-linux Repository. github.com/google/capsicum-linux; FreeBSD Project. Commit `72c35fc69c9f26789b502ebaf9934c4a7a9a2b63` (Robert Watson, 2009-09-30). Capsicum 系统调用号首次预留； FreeBSD Project. Commit `96fcc75fdf74e8ecc798405021f9c9b3c8e01c0d` (Robert Watson, 2011-03-01). Capsicum Capability Mode 初始实现； FreeBSD Project. Commit `009d2032af44e1f71bd17cda89ace46a4df2d2cc` (Robert Watson, 2011-12-29). options CAPABILITY_MODE/CAPABILITIES 加入 GENERIC 内核配置（对应 SVN r219129） ［A］---## 史料登记与辩证校准（2026-08-08 追加）> **本卷命题**：24.3 长期主义（详见本卷 00-总览“编纂指导思想叙事参照”）### 史料文献
- Levy, H. M. (1984). Capability-Based Computer Systems. Digital Press; Miller, M. S., Yee, K.-P., & Shapiro, J. S. (2003). Capability Myths Demolished. SRL2003-02, Johns Hopkins University; Watson, R. N. M. et al. (2010). Capsicum: Practical Capabilities for UNIX (Section 7). USENIX Security '10; E Language Project. erights.org; Tahoe-LAFS Project. tahoe-lafs.org. ［B］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- University of Cambridge Computer Laboratory. Capsicum and CHERI Project Licensing Statements. cl.cam.ac.uk; cheribsd.org. CheriBSD License. github.com/CTSRD-CHERI/cheribsd.［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］**【本节文献综述】** 详见 [04-现代研究文献/05-参考文献全文数据库/references_fulltext.duckdb](04-现代研究文献/05-参考文献全文数据库/references_fulltext.duckdb) `chapter_reviews` 表（id=36）---**补充证据（基于全文数据库修订）**本次修订从全文数据库补充 1 篇新匹配文献的证据。**新增核心事实**
文献 (201305-temporal-practical-capabilities, 年份不详, p.15) 指出：FreeBSD 作为 Capsicum 能力系统的实现平台，该论文以 FreeBSD 为基础讨论了时间性能力的安全应用。
**新增技术**
文献 (201305-temporal-practical-capabilities, 年份不详) 讨论 Capsicum，该论文探讨了 Capsicum 能力系统在时间性安全策略中的应用，为操作系统安全研究提供了新方向。
文献 (201305-temporal-practical-capabilities, 年份不详) 讨论 LLVM，该论文介绍了 capweave 工具，该工具以 LLVM 程序和声明为输入，实现了编译时能力安全检查。
**新增时间线事件**
文献 (201305-temporal-practical-capabilities, 年份不详) 记录 1987：IEEE S&P 会议于 1987 年发表了关于自主型特洛伊木马的经典论文，为后续能力安全研究奠定了基础。
文献 (201305-temporal-practical-capabilities, 年份不详) 记录 1997：CAV 会议于 1997 年发表了关于使用 PVS 进行抽象状态图构造的论文，为形式化验证在安全领域的应用提供了参考。
<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP50、BSD Now EP7（共 2 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Robert Watson 自述其进入 BSD 的起点是高中时期学校获赠的运行 BSD/OS 的 UNIX 服务器，并由此转向操作系统安全研究。（BSD Now EP50，[1309.66-1351.62]，L1）
- Capsicum 能力沙箱设计约始于八年前，其内核接口已随 FreeBSD 发布，Google 亦将其移植至 Linux 并首次向内核邮件列表提交补丁。（BSD Now EP50，[1462.14-1489.42]，L1）
- FreeBSD 10 已将 tcpdump、gzip 等基础工具纳入 Capsicum 沙箱，以降低以 root 运行、处理不可信输入程序被利用后的影响。（BSD Now EP50，[1565.14-1606.06]，L1）
- OpenSSL 于 2014 年 8 月发布修复九个漏洞的新版本，LibreSSL 对其中五项完全受影响、一项部分受影响、三项因移除相关代码而不受影响。（BSD Now EP50，[897.62-988.06]，L2）
- Poul-Henning Kamp 自述其在 1990 年代初于丹麦公司使用 Unix 工作，386BSD 由 Bill Jolitz 将伯克利内核移植到标准 PC 硬件后开始接触；FreeBSD 项目从 386BSD 的生长中形成，他因时区原因未参与发起，但在项目启动约六小时内加入并自始参与。（BSD Now EP7，[765.12-827.62]，L1）
- Jails 的起源据 Poul-Henning Kamp 口述：chroot 最初是伯克利为构建 release 而作，他将其打磨并添加特性后未用于发布；后因南卡罗来纳州一位托管商希望在同一服务器运行多个 Apache 与 MySQL 版本而提出资助开发，约定一年后提交入 FreeBSD，最终他与 Robert Watson 合写论文《Confining the Omnipotent Root》并在 Maastricht 的 2000 年会议上发表。（BSD Now EP7，[968.64-1077.26]，L1）
- Poul-Henning Kamp 将 jail 描述为单向镜：主机管理员可以站在 jail 之外向内观察而不被 jail 内进程察觉，这一特性被安全研究者用于蜜罐，也被用于 CDN 计费系统等场景；jail 后续又获得虚拟网络栈，使单一内核可启动多个隔离环境。（BSD Now EP7，[1095.10-1257.20]，L1）
- MD5 crypt 诞生于 FreeBSD 2.0 时期：因美国加密出口管制，FreeBSD 无法随发行版附带基于 DES 的标准密码扰码器，secure 发行版改从南非分发；Poul-Henning Kamp 用一个下午写出 MD5 crypt 并以 $1$ 前缀预留算法升级机制，该代码后来广泛扩散至 Cisco 设备、glibc、Flash、JavaScript 与 COBOL 实现，他估计一度保护约五成互联网的完整性。（BSD Now EP7，[1481.56-1750.10]，L1）
- Poul-Henning Kamp 在 DARPA 合同背景下开发 GEOM 可插拔磁盘 I/O 框架，并实现面向全分区加密的 GBDE；GELI 则由 Pawel 编写，二者共同构成 FreeBSD 磁盘加密层。他亦以吃自己的狗粮形容其笔记本自 1992 年起运行 FreeBSD 且分区以 GBDE 加密。（BSD Now EP7，[1756.80-1900.42]，L1）

**史料**：

- Robert Watson 访谈（当事人自述，FreeBSD 核心团队成员与剑桥大学讲师）。（BSD Now EP50，[1294.82-2231.72]，L1）
- OpenSSL 0.9.8zb、1.0.0n、1.0.1i 安全公告与 LibreSSL 2.0.5 发布信息（主持人口头转述）。（BSD Now EP50，[897.62-983.42]，L2）
- 本期对 Poul-Henning Kamp 的当事人访谈自述，他是 FreeBSD 项目早期成员，也是 jail、GEOM、GBDE 与 MD5 crypt 的亲历者。（BSD Now EP7，[707.32-2296.90]，L1）
- Kamp 与 Robert Watson 合著论文《Jails: Confining the Omnipotent Root》（BSDCon 2000），是对 jail 的系统化表述。（BSD Now EP7，[1052.26-1077.26]，L3）
- jail(2)、gbde(8)、geli(8) 手册页及 FreeBSD 源码仓库中对应提交记录，可作为交叉验证来源。（BSD Now EP7，L3）

**史观**：

- 总纲10 动手者创造历史：Robert Watson 团队以编写并落地 Capsicum、BERI/CHERI 的方式实际推动操作系统安全演进。（BSD Now EP50，[1380.46-1462.14]，L1）
- 总纲9 经验优先：访谈以当事人对代码、硬件与漏洞的一手经验为叙述依据，而非抽象安全口号。（BSD Now EP50，[1451.54-1571.28]，L1）
- 总纲22 知识注定过时：OpenSSL 与 LibreSSL 的持续修补显示安全知识处于不断失效与重写的循环之中。（BSD Now EP50，[957.56-988.06]，L2）
- 总纲5 没有必然性，只有偶然性：jail 并非源自宏大规划，而是由一个南卡罗来纳州托管商的具体商业需求偶然催生。（BSD Now EP7，[968.64-1052.26]，L1）
- 总纲10 动手者创造历史：Poul-Henning Kamp 为具体托管需求动手实现 jail，而非在抽象层面提出容器概念。（BSD Now EP7，[968.64-1052.26]，L1）
- 总纲13 法律与道德是利益分配：美国加密出口管制直接塑造了 FreeBSD 密码扰码器的技术路径，使 MD5 crypt 与南非 secure 发行版成为法律约束下的工程选择。（BSD Now EP7，[1481.56-1534.78]，L1）
- 总纲8 本体论上各方平等：jail 与完整虚拟化各有价值，Poul-Henning Kamp 不将 jail 宣称为唯一正确的虚拟化方案，而是强调其单向镜等独特优势。（BSD Now EP7，[1095.10-1257.20]，L1）

**辨析**：

- Watson 自述尚不清楚 FreeBSD 10 发布以来沙箱化基础工具实际缓解了多少已公开漏洞，量化效果存疑。　[存疑脚注] 沙箱缓解漏洞的量化结论缺乏公开统计数据支撑（BSD Now EP50，[1578.68-1585.78]，L4）
- [存疑脚注] 转写文本对 Poul-Henning Kamp 的姓名拼写前后不一（Paul Henningkamp、Paul Heinkamp、Paul Henningham），经上下文与 FreeBSD 史实判断指 Poul-Henning Kamp，引用时须以原始音频复核。　[存疑脚注] 人名转写拼写不一致，须以原始音频复核（BSD Now EP7，[732.60-736.24]，L4）
- [存疑脚注] Poul-Henning Kamp 口述 jail 论文发表会议时在 1998 与 2000 之间犹豫，最终自定为 2000；本卡片采信其最终自述，并与既有考据相互印证，但精确会议年份仍须以论文原文与会议议程核实。　[存疑脚注] 会议年份口述有反复，须以论文原文核实（BSD Now EP7，[1066.26-1077.26]，L4）
- [存疑脚注] 转写将 GBDE 识别为 GBD，将 GELI 作者 Pawel 转写为 Pappel；本卡片据 FreeBSD 磁盘加密技术史判定为 GBDE 与 Pawel Jakub Dawidek，须以原始音频复核。　[存疑脚注] 磁盘加密术语与人名转写错误（BSD Now EP7，[1826.94-1836.94]，L4）

**文献**：

- [BSD Now EP50] Pennington J. BSD Now: 50: VPN, My Dear Watson[EB/OL]. (2014-08-13)[2026-08-15]. <https://www.bsdnow.tv/50>.
- [BSD Now EP7] Pennington J. BSD Now: 7: Go Directly to Jail(8)[EB/OL]. (2013-10-16)[2026-08-15]. <https://www.bsdnow.tv/7>.

<!-- /PODCAST_REVIEW -->
