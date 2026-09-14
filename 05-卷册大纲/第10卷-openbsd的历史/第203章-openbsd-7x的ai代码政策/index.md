---
chapter: 第 203 章
id: CH203
volume: 第10卷-openbsd的历史
---

# 第 203 章 openbsd-7x的ai代码政策

## 要点

- 2013-2026 年间各 BSD 项目与 Linux 的发布数据与市场份额是研究 BSD 边缘化的核心史料；OpenBSD 6 个月周期、FreeBSD 约 2 年周期、NetBSD 不规律；Linux 容器生态占据数据中心垄断地位，BSD 在边缘市场存在
- 7.x 周期 OpenBSD 对 CPU 与 GPU 硬件漏洞的响应体现 “快速跟进—不等待上游” 的工程态度——**2024 年 3 月 17 日** guenther 提交 `6651c3e51fb0` 使用 VERW 指令缓解 RFDS（Register File Data Sampling）漏洞，针对 Intel Atom CPU；**2023 年 11 月 30 日** jsg 提交 `
- 从项目史观总纲第 19 条 “解释学循环是历史认识的根本条件” 审视，OpenBSD committer 权限管理与 AI 代码政策的评估受前理解差异制约——OpenBSD 阵营以 “治理效率” 与 “安全至上” 为前理解，批评者以 “继承风险” 与 “政策透明度” 为前理解，被疏远贡献者以 “个人经历” 为前理解，外部观察者以 “治理多样性” 为前理解，四者难以通约；解释学循环意味着 OpenB
- OpenBSD 7.x 时期共发布 10 次 release（7.0 至 7.9）；7.x 时期发布周期稳定为 4 月/10 月节奏（7.0 为 2021-11-01 属调整，7.1 起严格遵循 4 月/10 月），7.9（2026-05-19）为最新 release（截至 2026-07-23 考据时点）；〔待核：原文截断，后文待回源〕
- OpenBSD 7.x 时期（含 7.4 末段至 7.9 全段，重点考据范围 2024-2026）共发布 162 条 Errata 公告，分布于 6 个 release 版本——7.4（22 条，2023-10-16 发布）、7.5（25 条，2024-04-22 发布）、7.6（23 条，2024-10-28 发布）、7.7（42 条，2025-04-28 发布）〔待核：原文截断，后文待回源〕

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3902] 卷“第10卷-openbsd的历史”第 203 章，匹配置信度 folder，原因：folder 第201章

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 市场份额统计无权威数据源——DistroWatch 等仅反映桌面用户关注度，不反映服务器部署；BSD 实际部署规模以云服务商公开数据与企业调查为准 ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- **须精确说明 RFDS 漏洞的技术背景**：RFDS（Register File Data Sampling）是 Intel Atom 系列处理器的侧信道漏洞，CVE 编号为 CVE-2023-28646 ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］，guenther 使用 VERW 指令（Verify User Write）作为缓解——VE
- 解释学循环不意味着相对主义——史家仍须以多源交叉验证逼近史实，但须自觉呈现前理解；【0 信任原则·叙事权力的自觉】本节作为项目统摄史观审视，自身亦嵌入项目统摄史观的前理解，须自觉呈现这一前理解而非伪装中立；【0 信任原则·辩证链的非终结性】辩证链四层（批评-反批评-再批评-合图）不是史家认识的终结而是阶段性综合——合图本身嵌入特定前理解，随 OpenBSD 治理演进与被疏远贡献者视角的史料公开须重
- RELEASE 公告日期与 release song 标题的考据须遵循 0 信任原则并以三段式呈现——【查证来源】（1）OpenBSD 官网各版本 release 页面（如 <https://www.openbsd.org/70.html> 至 79.html）经 2026-07-23 检索，7.0-7.6 release song 标题确证，7.7-7.9 release 页面抓取超时；（2）<
- Errata 公告考据须遵循 0 信任原则并以三段式呈现——【查证来源】（1）OpenBSD 官网 errata 汇总页面 <https://www.openbsd.org/errata.html> 与各版本 errata 子页面 <https://www.openbsd.org/errata{74-79}.html> 经 2026-07-23 检索，逐版本 Errata 计数经网页内容核对；〔待核：原文截断，后文待回源〕

## 文献

- 各 BSD 项目 Release Notes；Linux 发行版统计；BSD 相关调查报告［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］---

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2013-2026 年间：649,962 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- OpenBSD Project. openbsd.duckdb — openbsd-src hardware security commits [DB/OL]. 2026-07-22. SQL: SELECT commit_hash, author_date, author_name, message_subject FROM commits WHERE repo_name =‘openbsd-src’ AND author_date >=‘2021-10-14’ AND author_date <‘2026-07-22’ AND (message_subject LIKE ‘%spectre%’ OR message_subject LIKE ’%RFDS%’ OR message_subject LIKE ‘%VERW%’ OR message_subject LIKE ’%TLB%’ OR message_subject LIKE '%drm/%’) ORDER BY author_date ASC; Intel. Register File Data Sampling Security Advisory[EB/OL]. (2024)[2026-07-22]. <https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00898.html>; OpenBSD Project. drm(4) Manual Page [EB/OL]. [2026-07-22]. <https://man.openbsd.org/drm.4>; MITRE. CVE-2025-10263: TLB invalidation vulnerability [EB/OL]. (2025)[2026-07-22]. <https://www.cve.org/CVERecord?id=CVE-2025-10263> ［A］---

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。
- 项目史观总纲第 19 条与第 15 条；OpenBSD 官方叙事文档；批评者叙事文档；第 89.3.5-89.3.7 节辩证链补足；参见 LibreSSL fork 与 RETGUARD 的项目统摄史观审视相关章节 ［A］

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。
- OpenBSD 官网 release 页面 ［EB/OL］. <https://www.openbsd.org/{70-79}.html>；<announce@openbsd.org> 邮件列表存档 ［EB/OL］. <https://marc.info/?laccopenbsd-announce>；openbsd.org.cn；原材料/研究/考据记录/20260723_announcements-openbsd.md § 二.2；openbsd.duckdb openbsd-src 仓库 ［A］

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。
- OpenBSD errata 汇总页面 ［EB/OL］. <https://www.openbsd.org/errata.html>；OpenBSD 各版本 errata 子页面 ［EB/OL］. <https://www.openbsd.org/errata{74-79}.html>；**signify(1) ** 手册页；** syspatch(8)** 手册页；OpenBSD 各版本发布公钥 ［EB/OL］. `https://www.openbsd.org/pubkey_{74-79}.txt`；<announce@openbsd.org> 邮件列表存档 ［EB/OL］. <https://marc.info/?laccopenbsd-announce>；原材料/研究/考据记录/20260723_announcements-openbsd.md § 二.3；openbsd.duckdb openbsd-src 仓库 commits 表 ［A］FreeBSD 社区论文：[FP-2022-001] Refining FreeBSD's Kernel Crypto Framework（John Baldwin（约翰·鲍德温），2022）<https://papers.freebsd.org/2022/bsdcan/baldwin-refining_freebsds_kernel_crypto_framework/>FreeBSD 社区论文：[FP-2021-008] smart(8) Update: A Permissively-Licensed Alternative to smartctl(8)（Michael Dexter（迈克尔·德克斯特）; Chuck Tuffli，2021）<https://papers.freebsd.org/2021/eurobsdcon/dexter-tuffli-update_on_smart/>FreeBSD 社区论文：[FP-2019-076] FreeBSD at Work: Building Network and Storage Infrastructure with pfSense and FreeNAS（Conor Beh，2019）<https://papers.freebsd.org/2019/vbsdcon/beh-freebsd_at_work/>FreeBSD 社区论文：[FP-2019-002] BSD Unix Solutions in the Australian NFP/NGO Health Sector（Jason Tubnor，2019）<https://papers.freebsd.org/2019/asiabsdcon/tubnor-bsd_unix_solutions_in_the_australian_nfp_ngo_health_sector/>FreeBSD 社区论文：[FP-2019-014] LLVM and the state of sanitizers on BSD（David Carlier，2019）<https://papers.freebsd.org/2019/asiabsdcon/carlier-llvm_and_the_state_of_sanitizers_on_bsd/>FreeBSD 社区论文：[FP-2018-010] Preparing your home router(s) for the future: A journey through Homenet and interconnected objects（Massimiliano Stucchi，2018）<https://papers.freebsd.org/2018/bsdcan/stucchi-preparing_your_home_routers_for_the_future/>FreeBSD 社区论文：[FP-2017-014] Isolated BSD build environments using virtual and hardware machines（Michael Dexter，2017）<https://papers.freebsd.org/2017/vbsdcon/dexter-isolated_bsd_build_environments_using_virtual_and_hardware_machines/>FreeBSD 社区论文：[FP-2017-009] My BSD sucks less than yours（Baptiste Daroussin（巴蒂斯特·达鲁桑） Antoine Jacoutot（安托万·雅库托），2017）<https://papers.freebsd.org/2017/fosdem/bapt-my_bsd_suck_less_than_yours/>

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 2024-2026 年间：45,424 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。
