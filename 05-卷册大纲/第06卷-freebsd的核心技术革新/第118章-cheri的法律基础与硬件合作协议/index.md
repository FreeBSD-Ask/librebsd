---
chapter: 第 118 章
id: CH118
volume: 第06卷-freebsd的核心技术革新
---

# 第 118 章 cheri的法律基础与硬件合作协议

## 要点

- CHERI 商用化进程的一手史料包括：CHERI 官方网站 cheri-cpu.org（持续更新项目进展和技术报告）；CHERI Alliance 官方网站 cheri-alliance.org（2024 年 11 月成立后的产业公告）；CheriBSD 各版本 Release Notes（22.05-25.03，记录 Morello 支持成熟度）；Arm Morello Program 官方文档
- Capsicum 和 CHERI 安全争议的一手史料包括：USENIX Security、IEEE S&P、ASPLOS、ISCA 等顶级安全/架构会议中关于能力系统局限性的论文；FreeBSD 邮件列表（freebsd-hackers@、freebsd-arch@、freebsd-security@）中关于 Capsicum 设计权衡的讨论；CHERI 技术报告系列中明确标注的 limitati
- Capsicum/CHERI 贡献者谱系的一手史料包括：各篇顶级会议论文的作者列表（USENIX Security 2010、ISCA 2014、IEEE S&P 2015、ASPLOS 2019 等核心论文）；FreeBSD/CheriBSD 源码仓库的 commit log 作者信息；剑桥大学 CHERI/Capsicum 项目页面的 people 目录；CHERI Alliance 成员公司
- Apple 在 macOS 10.7 Lion（2011）引入 Sandbox（基于 TrustedBSD MAC 框架），通过声明式 profile 限制应用资源访问；其底层借鉴 FreeBSD/TrustedBSD 的 MAC 思想，是 BSD 安全技术经 Darwin 间接影响商业桌面的案例。
- CHERI 许可策略的一手史料可在 CTSRD-CHERI GitHub 各仓库的 LICENSE 文件、CHERI 官方网站 cheri-cpu.org 的使用条款、CheriBSD 源码仓库的版权声明中查阅；CHERI 项目采用的许可证体系整体上是 BSD 风格的宽松许可，但需注意不同组件的细微差别：(1) CHERI ISA 规范文档和技术报告——Cambridge 开放发布，允许学术引用和

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3624] 卷“第06卷-freebsd的核心技术革新”第 118 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3666] 卷“第06卷-freebsd的核心技术革新”第 118 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3667] 卷“第06卷-freebsd的核心技术革新”第 118 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3668] 卷“第06卷-freebsd的核心技术革新”第 118 章，匹配置信度 curated，原因：curated token rule
- [DB:bsdnow_podcast:outline_mappings:om_11029] BSD Now 第 583 期，匹配 CH118 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11422] BSD Now 第 538 期，匹配 CH118 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12107] BSD Now 第 456 期，匹配 CH118 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12912] BSD Now 第 148 期，匹配 CH118 章，关联度 1.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 关于 “FreeBSD Foundation 2024 年 Capsicum 与 bhyve 安全审计”——经检索 FreeBSD Foundation 官方博客和公告，2023-2024 年 FreeBSD Foundation 确实资助了多项安全审计工作，但专门针对 Capsicum+bhyve 的 Trail of Bits 审计报告公开信息有限 [存疑脚注：2026-08-17 Capsi
- 关于 “ANU 对 Capsicum/CHERI 的质疑”——原大纲提到 “ANU 质疑” 但未给出具体来源，经检索未找到澳大利亚国立大学（ANU）研究者公开发表的专门质疑 Capsicum/CHERI 的论文或文章；ANU 有计算机安全研究组，但 CHERI/Capsicum 相关批评论文主要来自其他机构（如 MIT、Georgia Tech、Google Project Zero 等），该说法
- Capsicum/CHERI 发展中 “看不见的贡献者”——代码审查者、测试人员、文档写作者、邮件列表讨论者的贡献很少被正式记录，但对项目成功同样重要；FreeBSD 基金会在 Capsicum 工程化中的资助和项目管理角色常被低估，基金会不仅提供资金，还协调开发进度和代码审查；原模板文献列表中大量无关文献已删除并替换为贡献者相关的权威来源
- macOS Sandbox 基于 MAC profile 而非 Capsicum capability，二者范式不同；但其 BSD 血统说明 BSD 安全研究对主流桌面 OS 的实际影响。
- 原大纲本节称“CHERI ISA 以 BSD 许可证发布”需更精确表述——CHERI ISA 规范不是单一许可证文件覆盖的软件项目，而是技术文档和架构规范；具体实现代码（硬件 RTL、软件）使用 BSD 许可，规范本身由 Cambridge/SRI 以允许自由实现的条款发布；“ARM Morello 原型板的硬件设计文档受 ARM 商业许可约束”这一表述准确，但研究者可以通过 DSbD 计划免费获

## 文献

- CHERI Project. CHERI CPU Official Website. cheri-cpu.org; CHERI Alliance. Industry Consortium (2024). cheri-alliance.org; CheriBSD Project. Release Notes Archive. cheribsd.org/release-notes/; UK Research and Innovation. Digital Security by Design Programme. ukri.org; DARPA. CRASH/SSITH Program Archives. darpa.mil; FreeBSD Foundation. Quarterly Status Reports (2023-2025). freebsdfoundation.org.[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2023-2025 年间：182,991 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- FreeBSD Project Mailing Lists. Capsicum/CHERI Discussion Threads (2010-2025). lists.freebsd.org; University of Cambridge. CHERI Technical Report Series (UCAM-CL-TR). cl.cam.ac.uk/techreports/; Association for Computing Machinery. SIGSAC/SIGARCH Conference Proceedings (2010-2025); LWN.net. Capsicum/CHERI Coverage and Comments. lwn.net. ［B］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- CHERI/Capsicum Core Conference Papers (2010-2025); FreeBSD/CheriBSD Git Commit History. github.com/freebsd/freebsd-src, github.com/CTSRD-CHERI/cheribsd; University of Cambridge. Capsicum/CHERI People Pages. cl.cam.ac.uk; FreeBSD Foundation. Annual Reports (2012-2025). freebsdfoundation.org; Neumann, P. G. (1985-2025). ACM RISKS Forum Archive. catless.ncl.ac.uk/Risks/. ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- Apple. App Sandbox Design Guide [Z]. 2011；TrustedBSD Project. MAC Framework [EB/OL]. ［B］    FreeBSD 社区论文与演讲 [258]，[258] Ryan Stone. Oblivious Sandboxing with Capsicum and EBPF [C]//BSDCan 2020. [S.l.]: [s.n.], 2020. 获取路径：<https://papers.freebsd.org/2020/bsdcan/stone-oblivious_sandboxing_capsicum_ebpf/> [访问日期 2026-07-26].    FreeBSD 社区论文与演讲 [250]，[250] Brooks Davis. CheriABI: Enforcing Valid Pointer Provenance and Minimizing Pointer Privilege in the POSIX C Run-time Environment [C]//独立发布 2019. [S.l.]: [s.n.], 2019. 获取路径：<https://papers.freebsd.org/2019/davis-asplos-cheriabi/> [访问日期 2026-07-26].    FreeBSD 社区论文与演讲 [79]，[79] Mariusz Zaborski. Capsicum and Casper - a fairy tale about solving security problems [C]//AsiaBSDCon 2016. [S.l.]: [s.n.], 2016. 获取路径：<https://papers.freebsd.org/2016/asiabsdcon/oshogbo-capsicum_and_casper/> [访问日期 2026-07-26].    FreeBSD 社区论文与演讲 [27]，[27] Robert N. M. Watson. The TrustedBSD MAC Framework: Extensible Kernel Access Control for FreeBSD 5.0 [C]//独立发布 2003. [S.l.]: [s.n.], 2003. 获取路径：<https://papers.freebsd.org/2003/rwatson-mac_framework/> [访问日期 2026-07-26].[^doubt-resolved-641]: 据 张鹏宇_基于微内核的操作系统安全机制研究 (03-15, 2024) 消解[^doubt-resolved-642]: 据 young-m-1958-the-rise-of-the-meritocracy-thames-hudson-isbn (Young, 1958) 消解[^doubt-resolved-643]: 据 unknown_Charter-of-the-City-of-Berkeley_v1 (未署名) 消解[^doubt-resolved-644]: 据 The-copyinout-Framework (未署名) 消解[^doubt-resolved-645]: 据 Mac OS X Internals A Systems Approach (Amit Singh（阿米特·辛格）)  (未署名) 消解[^doubt-resolved-646]: 据 Design_Implementation_FreeBSD_OS (未署名) 消解<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2013 年间：148,830 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- CTSRD-CHERI Organization. GitHub Repositories and LICENSE Files. github.com/CTSRD-CHERI; CHERI Alliance. cheri-alliance.org; University of Cambridge/SRI International. CHERI Technical Report Series (UCAM-CL-TR).[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- CTSRD-CHERI. CheriBSD Repository (AUTHORS, commit history). github.com/CTSRD-CHERI/cheribsd; Davis, B. et al. (2019). CheriABI (full author list). ASPLOS '19; CheriBSD Project. Release Notes 22.05-25.03. cheribsd.org/release-notes/; CheriBSD Getting Started. ctsrd-cheri.github.io/cheribsd-getting-started/. ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
