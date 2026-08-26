---
chapter: 第 75 章
id: CH75
volume: 第04卷-大分裂与四大bsd的诞生
---

# 第 75 章 openbsd的加密与固件开放政策

## 要点

- OpenBSD 对固件许可证持严格立场——厂商为节省成本不再在芯片内固化固件、改由操作系统加载后，固件分发许可证冲突显现；OpenBSD 把可自由再分发的固件纳入 base 系统，许可证不兼容的固件经 `fw_update(8)` 从端口单独分发，多数为 WiFi、显卡与 Intel 芯片组（afresh1, 2024）。
- Linux、Windows NT 4.0、Solaris 2.5 与 OpenBSD 的安全比较需辨析——不同项目的安全目标、用户基数、商业模型差异较大；辨析需对照多方原始文档交叉验证；freebsd.db 统计结论 C-05 显示：openbsd-src 总 commit 数 245,904（SQL 查询 `SELECT COUNT(*) FROM commits WHERE repo_name
- OpenBSD 2.6/2.7/2.8/2.9 时期（1999-2001）的漏洞响应模型呈现 errata 机制成熟化特征——errata 条目从 2.0/2.1 时期的纯补丁发布演化为 2.7 时期的密集安全修复期（2000 年 10 月多条 SECURITY FIX 条目）与 2.9 时期的末条 errata（2002 年 6 月 25 日第 027 条）；hackathon 文化（首次 19
- 从项目史观总纲第 5 条 “没有必然性，只有偶然性”、第 6 条 “和解优于斗争”、第 21 条 “革命与改革是历史方法论的分歧” 三条切入审视，de Raadt 独裁模式、代码审计团队与被疏远贡献者并非 “独裁必然产生安全至上” 或 “独裁必然排斥贡献者” 的目的论结果，而是 1996 年夏天 OpenBSD 启动全代码审计（security.html 一手记载 "We have been au

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3826] 卷“第04卷-大分裂与四大bsd的诞生”第 75 章，匹配置信度 folder，原因：folder 第73章

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- OpenBSD 的严格许可证立场与硬件厂商的省钱考量构成持续冲突——rtwn(4)/urtwn(4) 固件经 kevlo 联系 Realtek 去除专利条款后移入 base，是许可证谈判成功的少数案例；多数不兼容固件仍须经 `fw_update(8)` 分发（afresh1, 2024）。
- 比较的具体维度在不同叙事中略有差异——需对照多方原始文档交叉验证；【0 信任原则·commit 量不等于质量】C-05 openbsd-src 245,904 与 C-03 freebsd-src 444,203 的量级差异不等于两项目代码质量或安全性的差异——OpenBSD 的安全审计文化（自 1996 年夏天起全代码审计）使单次 commit 可能包含更密集的审计修正，commit 量与安全质
- errata 机制从 2.0 至 2.9 的成熟化路径须逐版本对照 errata 页面核实——2.0 时期 errata 为纯补丁发布，2.7 时期出现密集安全修复期，2.9 末条 errata 为收尾，3.x 起引入架构性防御，各阶段边界须以 errata 条目数量与内容为据而非史家主观分期；hackathon 对漏洞响应的具体贡献须对照 hackathons.html 记录与 errata 时
- 考据过程留痕——【查证来源】项目史观总纲第 5 条原文经 据原文第 25 章 第 11 行 Read 一手核验，第 6 条原文经第 13 行 Read 一手核验，第 21 条原文经第 25 行 Read 一手核验；OpenBSD security.html 经 <https://www.openbsd.org/security.html> WebFetch 一手核验，"We have been a

## 文献

- afresh1, 2024《Why rewrite fw_update(8)?》BSDCan 2024 演讲<!-- DB_REF:openbsd.duckdb -->> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1992-1995 年间：770 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
- 四个项目 1995-1996 年安全文档；安全对比研究[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]；本项目。freebsd.db 数据分析报告：描述性统计与推断性统计 [R/OL]. 2026.（统计结论 C-05 openbsd-src 总 commit 数 245,904，SQL 查询 `SELECT COUNT(*) FROM commits WHERE repo_name='openbsd-src'`；统计结论 C-03 freebsd-src 总 commit 数 444,203；统计结论 C-14 openbsd-src 变点 Pettitt 2001-01 / BUISHAND 2017-09，Python 脚本自实现 Pettitt + BUISHAND R 检验 10,000 次 Monte Carlo；统计结论 C-12 freebsd-src 变点 1999-08 双检验一致 p < 0.001） ［A］
- OpenBSD 2.6/2.7/2.8/2.9 errata 页面；OpenBSD hackathons.html；OpenBSD security.html；OpenBSD 3.x errata 页面；本项目。原材料/研究/bsd 漏洞史/版本周期/openbsd-2.x.md；本项目。bsd_commits.db 数据分析报告：宏观趋势统计 [R/OL]. 2026. ［A］
- 项目史观总纲第 5 条、第 6 条、第 21 条（据原文第 25 章）；OpenBSD security.html [EB/OL]. <https://www.openbsd.org/security.html>；OpenBSD hackathons.html [EB/OL]. <https://www.openbsd.org/hackathons.html>；OpenBSD goals.html [EB/OL]. <https://www.openbsd.org/goals.html>；bsd_commits.db openbsd-src 仓库 deraadt 首 commit 与累计 commit 量 ［A］### 史观映射> de Raadt 被逐出 NetBSD——一封邮件通知，没有上诉，没有告别。分离从来不是和平的，但分离之后必有新的聚合：OpenBSD 从 NetBSD 的废墟中诞生，以代码审计为旗帜。de Raadt 的天才加速了 OpenBSD 的崛起——PF、OpenSSH、全代码审计方法论，每一项都是他驱动下的产物。但同一种不妥协的气质，既是他创造的动力，也是他冲突的根源：与 NetBSD 的决裂只是开始，此后与 FreeBSD 的隔阂、与 DARPA 的冲突、与社区新人的摩擦，都是同一种结构的反复。天才不总是灾厄，但天才的边界往往就是灾厄的起点---## 第 29.15 不同时期人员的采访录（详见 [采访录.md](采访录.md)）> 第 29 章采访录子节，覆盖 1996-2001 年 OpenBSD 安全文化奠基的当事人陈述，含 Theo de Raadt（西奥·德·若特） OpenBSD 安全文化奠基演讲、Bob Beck OpenBSD 安全响应工程两则，每则采访按 5 字段深化，考据过程另见 原材料/研究/考据记录/ 下对应文件。## 第 29.16 节 媒体反响与社区舆论（详见 [媒体反响与社区舆论.md](媒体反响与社区舆论.md)）
