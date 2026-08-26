---
chapter: 第 261 章
id: CH261
volume: 第13卷-bsd衍生操作系统
---

# 第 261 章 pfsense-opnsense

## 要点

- pfSense 由 Chris Buechler 与 Scott Ullrich 于 2004 年 9 月自 Manuel Kasper 的 m0n0wall（FreeBSD 嵌入式防火墙）分叉而来，目标是克服 m0n0wall 作为嵌入式系统的可扩展性局限——m0n0wall 功能强大但受限于嵌入式形态，pfSense 旨在提供更完整的 FreeBSD 防火墙发行版；pfSense 沿用 Fre
- pfSense/OPNsense 依赖 FreeBSD 网络栈贡献者与各自社区；Manuel Kasper（瑞士）、Deciso 团队（荷兰）属非英美贡献者。
- 对比 pfSense/OPNsense（FreeBSD）与 Linux 防火墙（如 IPFire、Untangle）、商用防火墙（Cisco ASA、Fortinet FortiGate），分析 BSD 在开源防火墙的统治。pfSense/OPNsense 在开源防火墙市场的统治地位体现于 SMB（中小企业）与 SOHO（小型办公室/家庭办公室）场景——这两类场景对成本敏感但要求企业级特性（VPN
- freebsd.db 查询显示 pfsense-src 仓库共 929 条 CVE 相关 commit、567 个去重 CVE，merge commit 比例在 2016 年为 2.3%（661/28,813）、2017 年 2.4%（629/26,654）、2022 年 1.3%（133/10,179），长期维持在 1-3% 水平，显著低于 hardenedbsd-src 同期 24.3% 的
- 2019 年 5 月 19 日，opnsense-core 仓库记录了 CVE-2019-11816 的修复 commit `03c75f71be88d4d2d930c217377b5ff23f0ecae7`（author Ad Schellevis，committer Franco Fichtner），subject 为 "system: address CVE-2019-11816 privl

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4137] 卷“第13卷-bsd衍生操作系统”第 261 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充
- [DB:references_fulltext:chapter_matches:chmatch_4138] 卷“第13卷-bsd衍生操作系统”第 261 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- pfSense 与 m0n0wall 的分支关系时间点（2004）须以项目历史核实；openbsd.db 查询 L7.1.1.pfsense-src 的 commit 量须警惕 fork 分歧识别局限——pfsense-src 仓库 1993 年起的 commit 是 fork 自 FreeBSD 继承的上游历史，非 pfSense 项目本地 commit，识别 pfSense 本地特有 comm
- 市场份额须以独立报告（一手来源）核实；“BSD 防火墙在开源市场统治”的判断须警惕社区叙事偏差——pfSense/OPNsense 的社区声誉可能被放大为市场份额优势，实际部署数据须以第三方调研为准；IPFire 与 Untangle 的技术细节（内核版本、过滤框架）须以其官方文档核实，不得仅凭一般认知推断。
- pfsense-src 的 567 个去重 CVE 须区分 “继承自 FreeBSD 上游的修复” 与 “pfSense 本地特有 commit”——fork 仓库的 commit 历史包含上游继承部分，识别本地特有 commit 须通过 merge commit 与 parent_hashes 交叉验证，不可仅凭时间戳判定；merge commit 比例低不必然意味着安全修复滞后，须与 Netg
- CVE-2019-11816 的具体技术细节（权限提升路径）须以 NVD 条目与 OPNsense 官方公告为据，commit subject 中的 "privlege" 为原 commit 中的拼写错误（应为 "privilege"），本节保留原始 subject 文本不篡改；opnsense-core 的 4 个去重 CVE（CVE-2019-11816、CVE-2026-49131、CVE-

## 文献

- pfSense 官方文档；m0n0wall 档案；bsd_commits.db 查询 L7.1.1.pfsense-src（pfsense-src 仓库 merge commit 比例时间序列，2004-2026）；bsd_commits.db 查询 L1.1.1（pfsense-src 仓库每年 commit 量时间序列）；原材料/研究/bsd 仓库分析/数据分析/衍生项目与跨项目对比分析.md §L7.1；原材料/研究/bsd 仓库分析/数据分析/宏观趋势统计.md §L1.1.1。 ［B］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2004-2014 年间：433,494 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- 项目档案；bsd_commits.db。 ［A］<!-- DB_REF:bsd_derivatives.duckdb -->> **数据库引用（bsd_derivatives.duckdb）**：本子节对应 bsd_derivatives 代码仓库。> 2014-2026 年间：484,691 次提交。> 仓库总览：963,557 次提交，14,109 位贡献者，1985-06-13 至 2026-08-24。
- 各防火墙厂商资料；IPFire 官方文档；Untangle 官方文档；Cisco ASA 文档；Fortinet FortiGate 文档。[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:bsd_derivatives.duckdb -->> **数据库引用（bsd_derivatives.duckdb）**：本子节对应 bsd_derivatives 代码仓库。> 1985-2026 年间：963,557 次提交。> 仓库总览：963,557 次提交，14,109 位贡献者，1985-06-13 至 2026-08-24。
- bsd_commits.db 查询 pfsense-src CVE commit（929 条，567 去重 CVE，2026-07-23）；bsd_commits.db 查询 L7.1.1.pfsense-src；`原材料/研究/bsd漏洞史/数据库提取/pfsense-src-cve-commits.md`；`原材料/研究/bsd仓库分析/数据分析/衍生项目与跨项目对比分析.md` §L7.1。 ［B］## 260.4.2 CVE-2019-11816 OPNsense 权限提升漏洞与 Web 界面安全
- bsd_commits.db 查询 opnsense-core CVE commit（8 条，4 去重 CVE，2026-07-23）；NVD. CVE-2019-11816 [EB/OL]. <https://nvd.nist.gov/vuln/detail/CVE-2019-11816>（访问日期 2026-07-23）；`原材料/研究/bsd漏洞史/数据库提取/opnsense-core-cve-commits.md`。 ［B］FreeBSD 社区论文：[FP-2020-021] How an Australian IaaS uses FreeBSD（Ruben Schade，2020）<https://papers.freebsd.org/2020/linux.conf.au/schade_how_an_australian_iaas_uses_freebsd/>FreeBSD 社区论文：[FP-2019-045] FreeBSD and the absurdities of security compliance（Eirik Øverby，2019）<https://papers.freebsd.org/2019/eurobsdcon/oeverby-freebsd_and_the_absurdities_of_security_compliance/>FreeBSD 社区论文：[FP-2019-076] FreeBSD at Work: Building Network and Storage Infrastructure with pfSense and FreeNAS（Conor Beh，2019）<https://papers.freebsd.org/2019/vbsdcon/beh-freebsd_at_work/>FreeBSD 社区论文：[FP-2018-010] Preparing your home router(s) for the future: A journey through Homenet and interconnected objects（Massimiliano Stucchi，2018）<https://papers.freebsd.org/2018/bsdcan/stucchi-preparing_your_home_routers_for_the_future/><!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1985-2026 年间：1,294,851 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
