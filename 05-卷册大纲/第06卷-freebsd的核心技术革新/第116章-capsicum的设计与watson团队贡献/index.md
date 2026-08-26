---
chapter: 第 116 章
id: CH116
volume: 第06卷-freebsd的核心技术革新
---

# 第 116 章 capsicum的设计与watson团队贡献

## 要点

- Capsicum 一手史料主要包括：剑桥大学 Capsicum 项目页面 cl.cam.ac.uk/research/security/capsicum/（持续维护，含论文、演讲、代码、文档链接）；USENIX Security 2010 会议论文集（usenix.org 永久存档）；FreeBSD 源码仓库中 Capsicum 相关提交——经 **bsd_commits.db** `commit
- Capsicum 能力模型的理论溯源可至 1970 年代的能力系统研究：剑桥大学 CAP computer（1970s，世界首个能力计算机）、PSOS（Provably Secure Operating System，SRI International，Peter G. Neumann 参与）、Hydra（CMU）、KeyKOS（Key Logic，1980s）、EROS（Extremely Re
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

- 原大纲称 Capsicum 论文作者为 "Watson、Anderson、Laurie、Kenneally" 系名字讹误，第四作者经论文 PDF 核实为 Kris Kennaway（FreeBSD 长期 committer，Google 安全工程师），已修正；Capsicum 论文发表于 USENIX Security 2010，会议精确日期为 2010 年 8 月 11-13 日（USENIX 
- 原大纲文献列表多次错误列入"Lucas 2018 'FreeBSD Mastery: Storage Essentials’"——Storage Essentials 是存储主题书籍，与 Capsicum/CHERI 无关，属于模板复制时未清理的无关文献，已全部删除并替换为 Capsicum/CHERI 相关权威文献；原大纲还列入"Skorstengaard, Devriese, Birkedal
- 原大纲本节称“剑桥大学许可策略史料考证”但列入大量与 Capsicum 无关的文献（如 Lucas Storage Essentials、Skorstengaard CHERI 论文等），已修正为 Capsicum 许可策略专属史料；Capsicum 是否曾使用过其他许可证名称（如"BSD License""University of Cambridge License"）经剑桥项目页面核实均为 

## 文献

- University of Cambridge Computer Laboratory. Capsicum Project Documentation. cl.cam.ac.uk/research/security/capsicum/; USENIX Association. Proceedings of the 19th USENIX Security Symposium (2010). usenix.org; FreeBSD Project. FreeBSD 9.0-RELEASE Release Notes (2012-01-12). freebsd.org; Google. capsicum-linux Repository. github.com/google/capsicum-linux; FreeBSD Project. Commit `72c35fc69c9f26789b502ebaf9934c4a7a9a2b63` (Robert Watson, 2009-09-30). Capsicum 系统调用号首次预留； FreeBSD Project. Commit `96fcc75fdf74e8ecc798405021f9c9b3c8e01c0d` (Robert Watson, 2011-03-01). Capsicum Capability Mode 初始实现； FreeBSD Project. Commit `009d2032af44e1f71bd17cda89ace46a4df2d2cc` (Robert Watson, 2011-12-29). options CAPABILITY_MODE/CAPABILITIES 加入 GENERIC 内核配置（对应 SVN r219129） ［A］---## 史料登记与辩证校准（2026-08-08 追加）> **本卷命题**：24.3 长期主义（详见本卷 00-总览“编纂指导思想叙事参照”）### 史料文献
- Levy, H. M. (1984). Capability-Based Computer Systems. Digital Press; Miller, M. S., Yee, K.-P., & Shapiro, J. S. (2003). Capability Myths Demolished. SRL2003-02, Johns Hopkins University; Watson, R. N. M. et al. (2010). Capsicum: Practical Capabilities for UNIX (Section 7). USENIX Security '10; E Language Project. erights.org; Tahoe-LAFS Project. tahoe-lafs.org. ［B］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- University of Cambridge Computer Laboratory. Capsicum and CHERI Project Licensing Statements. cl.cam.ac.uk; cheribsd.org. CheriBSD License. github.com/CTSRD-CHERI/cheribsd.[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]**【本节文献综述】** 详见 [04-现代研究文献/05-参考文献全文数据库/references_fulltext.db](04-现代研究文献/05-参考文献全文数据库/references_fulltext.db) `chapter_reviews` 表（id=36）---**补充证据（基于全文数据库修订）**本次修订从全文数据库补充 1 篇新匹配文献的证据。**新增核心事实**文献 (201305-temporal-practical-capabilities, 年份不详, p.15) 指出：FreeBSD 9.0-RELEASE mentioned。文献 (201305-temporal-practical-capabilities, 年份不详, p.15) 指出：Watson, Robert N. M. mentioned (4 times)。**新增人物**文献 (201305-temporal-practical-capabilities, 年份不详) 提及 Watson, Robert N. M.，mesh Jha∗, Thomas Reps∗†, Jonathan Anderson‡, and Robert N. M. Watson‡ ∗{ wrharr……。**新增技术**文献 (201305-temporal-practical-capabilities, 年份不详) 讨论 Capsicum，d, UK Abstract—New operating systems, such as the Capsicum capability system, al……。文献 (201305-temporal-practical-capabilities, 年份不详) 讨论 LLVM，ribes capweave, a tool that takes as input (i) an LLVM program, and (ii) a decla……。**新增时间线事件**文献 (201305-temporal-practical-capabilities, 年份不详) 记录 1987：ial of discretionary trojan horses," in IEEE S&P, 1987. [24] A. Bittau, P. Marchenko, M. Handley, an。文献 (201305-temporal-practical-capabilities, 年份不详) 记录 1997：ction of abstract state graphs with PVS," in CAV, 1997. [19] W. R. Harris, S. Jha, T. Reps, J. Ander。<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
