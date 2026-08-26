---
chapter: 第 270 章
id: CH270
volume: 第13卷-bsd衍生操作系统
---

# 第 270 章 pc-bsd-trueos

## 要点

- PC-BSD（2005）由 Kris Moore（克里斯·摩尔） 发起，提供图形安装器、PBI 软件包系统、预配置桌面，目标是 “开箱即用 FreeBSD 桌面”；其存在反映社区对消费桌面的长期诉求。
- 2018 年 PC-BSD 更名为 TrueOS，转向服务端/嵌入式定位（延续 FreeBSD 基底），桌面努力由 Project Trident（基于 TrueOS）承接；2020 年前后 TrueOS/Trident 项目渐止，标志一轮桌面 BSD 实验的落幕。具体时间须以项目公告核实。
- PC-BSD/TrueOS 依赖 Kris Moore（美国）与小型志愿者团队；项目体现个人驱动力在 BSD 衍生中的关键作用。
- 对比 PC-BSD/TrueOS（FreeBSD）与 Linux 桌面（Ubuntu 等）、其他桌面 BSD（参见相关章节桌面 BSD 部分），分析桌面 BSD 实验的共性教训（生态/硬件/应用）。
- bsd_commits.db 查询显示 trueos-src 仓库共 273 条 CVE 相关 commit、377 个去重 CVE，commit 数（273）低于去重 CVE 数（377），表明 TrueOS 存在单次 commit 合并多个 CVE 修复的批量化安全维护模式；trueos-src 的 CVE commit 跨越 2005 至 2020 年，2020 年后无新增 CVE comm

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3779] 卷“第14卷-商业生态与企业案例”第 270 章，匹配置信度 folder，原因：folder 第269章
- [DB:references_fulltext:chapter_matches:chmatch_3781] 卷“第14卷-商业生态与企业案例”第 270 章，匹配置信度 folder，原因：folder 第269章
- [DB:references_fulltext:chapter_matches:chmatch_3789] 卷“第14卷-商业生态与企业案例”第 270 章，匹配置信度 folder，原因：folder 第269章
- [DB:references_fulltext:chapter_matches:chmatch_3799] 卷“第14卷-商业生态与企业案例”第 270 章，匹配置信度 folder，原因：folder 第269章
- [DB:references_fulltext:chapter_matches:chmatch_3803] 卷“第14卷-商业生态与企业案例”第 270 章，匹配置信度 folder，原因：folder 第269章
- [DB:references_fulltext:chapter_matches:chmatch_3805] 卷“第14卷-商业生态与企业案例”第 270 章，匹配置信度 folder，原因：folder 第269章
- [DB:references_fulltext:chapter_matches:chmatch_3806] 卷“第14卷-商业生态与企业案例”第 270 章，匹配置信度 folder，原因：folder 第269章
- [DB:references_fulltext:chapter_matches:chmatch_3863] 卷“第14卷-商业生态与企业案例”第 270 章，匹配置信度 folder，原因：folder 第269章
- [DB:references_fulltext:chapter_matches:chmatch_3964] 卷“第14卷-商业生态与企业案例”第 270 章，匹配置信度 folder，原因：folder 第269章

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- PC-BSD 各版本对应 FreeBSD 基底须以项目 Release Notes 核实；freebsd.db 查询 L1.1.1 的 commit 量仅反映开发活跃度，须结合 commit 规模（additions/deletions）与 message 质量综合判断，且 GitHub 镜像仓库 commit 量可能滞后于主仓，trueos-src 仓库 2016 年的 commit 量峰值须与
- trueos-src 的 273 条 CVE commit 与 377 个去重 CVE 的数量差异（commit 数 < CVE 数）表明部分 commit 引用多个 CVE 编号，此批量化模式须以具体 commit message 核实，不得仅凭数量差异推断安全维护质量；2020 年后无新增 CVE commit 可能有多种原因——项目终止、仓库归档、镜像同步停止——须与 Project Tri
- PC-BSD 时期 “安全维护投入高于纯社区 fork” 的判断须以 iXsystems 员工 commit 量、安全公告频率等量化指标为据，不得仅凭定性判断；参照第 122 章 122.2.3 节已考据的 iXsystems 员工 freebsd-src 上游回馈 commit 前 4 名表——ryan@iXsystems.com 329 次、rob.norris@truenas.com 137

## 文献

- PC-BSD 官方文档；freebsd.db 查询 L1.1.1（trueos-src 仓库 2005-2020 年每年 commit 量时间序列）；原材料/研究/bsd 仓库分析/数据分析/宏观趋势统计.md §L1.1.1。 ［B］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2005-2018 年间：571,244 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- 项目档案。[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:bsd_derivatives.duckdb -->> **数据库引用（bsd_derivatives.duckdb）**：本子节对应 bsd_derivatives 代码仓库。> 2018-2020 年间：126,447 次提交。> 仓库总览：963,557 次提交，14,109 位贡献者，1985-06-13 至 2026-08-24。
- 各桌面 OS 官方资料。[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:bsd_derivatives.duckdb -->> **数据库引用（bsd_derivatives.duckdb）**：本子节对应 bsd_derivatives 代码仓库。> 1985-2026 年间：963,557 次提交。> 仓库总览：963,557 次提交，14,109 位贡献者，1985-06-13 至 2026-08-24。
- bsd_commits.db 查询 trueos-src CVE commit（273 条，377 去重 CVE，2026-07-23）；bsd_commits.db 查询 L7.1.1.trueos-src；`原材料/研究/bsd漏洞史/数据库提取/trueos-src-cve-commits.md`；`原材料/研究/bsd仓库分析/数据分析/衍生项目与跨项目对比分析.md` §L7.1。 ［B］## 269.4.2 PC-BSD 时期 CVE 处置与 iXsystems 商业安全维护投入
- bsd_commits.db 查询 L1.1.1（trueos-src 每年 commit 量）；bsd_commits.db 查询 L7.1.1.trueos-src；PC-BSD 官方文档；iXsystems 年度报告。 ［B］FreeBSD 社区论文：[FP-2018-035] The TrueOS Difference: Changing Methodologies for Changing Times（Ken Moore，2018）<https://papers.freebsd.org/2018/bsdcan/moore-the_trueos_difference/><!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1985-2026 年间：1,294,851 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
