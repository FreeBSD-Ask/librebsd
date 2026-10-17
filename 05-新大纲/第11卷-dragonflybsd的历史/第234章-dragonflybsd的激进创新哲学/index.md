---
chapter: 第 234 章
id: CH234
volume: 第11卷-dragonflybsd的历史
---

# 第 234 章 dragonflybsd的激进创新哲学

## 要点

- DragonFly BSD 于 2003 年 6 月 17 日自 FreeBSD 4.8 分叉，commit `984263bcb83a`（author_date = 2003-06-17T02:57:24Z，作者 Matthew Dillon）标题“Initial import from FreeBSD RELENG_4”标志仓库起点；Dillon 在 2003 年 7 月发布的 fork 公告
- DragonFly BSD 项目不设独立的 Vulnerability Security Announcement（VSA）公告系列，与 FreeBSD（FreeBSD-SA 系列）、OpenBSD（errata 公告系列配合 **signify(1)** 签名与 **syspatch(8)** 二进制更新）、NetBSD（NetBSD-SA 系列）形成鲜明对比。据 2026-07-23 公告考据
- dragonfly.duckdb dragonfly-src 仓库 contributors 表显示 DragonFly 核心贡献者高度国际化——德国：Sascha Wildner（<saw@online.de>，10846 条 commit，2004-12-17 至 2026-05-21）、Joerg Sonnenberger（<corecode@dragonflybsd.org>，2038 条，2
- DragonFly BSD 于 2003 年 6 月自 FreeBSD 4.8 分叉，7 月 Dillon 在 freebsd-current 邮件列表发布 fork 公告（lists.freebsd.org/pipermail/freebsd-current/2003-July/006889.html），公告称项目为"the logical continuation of the FreeBSD
- dragonfly.duckdb dragonfly-src 仓库 contributors 表显示除 Dillon（10666 条）外的核心贡献者谱系——Sascha Wildner（萨沙·维尔德纳）（<saw@online.de> 与 <swildner@dragonflybsd.org>，合并 10846 条，2004-12-17 至 2026-05-21，负责内核维护、驱动更新、release

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4117] 卷“第11卷-dragonflybsd的历史”第 234 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 部分二手叙事将 Dillon 哲学概括为“chip away everything that gets in the way”（凿除一切阻碍），但经检索 dragonflybsd.org 官方页面与 fork 公告均无此精确措辞，官网最接近的表述为"no reservation about cutting ties with legacy when it makes sense“——该”chip
- 无 VSA 系统不等于无安全响应——DragonFly 通过 commit message 与 kernel@/commits@ 邮件列表通知用户安全修复，regreSSHion（CVE-2024-6387）3 天内响应即为案例；但无 VSA 系统意味着用户难以系统跟踪安全修复状态，须自行监控 dragonfly-src 仓库 commit log 或订阅 commits@ 邮件列表；errata
- 贡献者国籍判定以邮箱域名（.de/.fr/.jp/.cn 等）与姓名拼写为初步线索，但邮箱域名不等于国籍（如 Dillon 使用 @dragonflybsd.org 而非美国域名）——上述归属以 commits 表 author_email 与 author_name 为依据，正式撰写时须以邮件列表自我介绍或公开简历交叉验证；Sepherosa Ziehau 的地理归属 [考据完成：2026-07
- 关于 2003 年 Dillon 提交权限被撤销的具体经过，不同当事人叙事存在差异——dragonflybsd.org 官方 history 仅称“forked from FreeBSD 4.8 in June of 2003 by Matthew Dillon（马修·狄龙）”而未提及权限撤销，FreeBSD 官方文档对 fork 事件着墨亦少 ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］. <https://www.dragonflybsd.org/history/> (last edited 2019-01-17)；Dillon M. Initial import from FreeBSD RELENG_4 [DB/OL]. dragonfly-src 仓库 commit 984263bcb83a, 2003-06-17T02:57:24Z；Dillon M. thread stage 7: Implement basic LWKTs [DB/OL]. dragonfly-src 仓库 commit 8ad65e080342, 2003-06-20T02:09:59Z；Dillon M. DragonFly BSD fork announcement [EB/OL]. <https://lists.freebsd.org/pipermail/freebsd-current/2003-July/006889.html>, 2003-07；深层信息挖掘.md §L3.1.1（数据补充：dragonfly-src 仓库 2004-2022 年共 12 条 innovat/radical commit） ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,207 次提交。> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。
- DragonFly BSD Project. Homepage [EB/OL]. <https://www.dragonflybsd.org/> (last edited 2025-10-03)；DragonFly BSD errata pages [EB/OL]. **dragonflybsd.org/release{version}/errata{major}_{minor}.shtml**；FreeBSD Security Advisories [EB/OL]. <https://www.freebsd.org/security/advisories/>；OpenBSD Errata [EB/OL]. <https://www.openbsd.org/errata.html>；NetBSD Security Advisories [EB/OL]. <https://www.netbsd.org/security/advisories/>；`原材料/研究/考据记录/20260723_announcements-dragonfly.md` ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,207 次提交。> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。
- dragonfly.duckdb dragonfly-src 仓库 contributors 表（7173 条贡献者记录）；dragonfly.duckdb dragonfly-src 仓库 commits 表（按 author_email 分组统计）；DragonFly BSD mailing lists [EB/OL]. <https://www.dragonflybsd.org/mailinglists/> ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,207 次提交。> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。
- Dillon M. DragonFly BSD fork announcement [EB/OL]. <https://lists.freebsd.org/pipermail/freebsd-current/2003-July/006889.html>, 2003-07；DragonFly BSD Project. DragonFly BSD history [EB/OL]. <https://www.dragonflybsd.org/history/>；FreeBSD Project. FreeBSD mailing list archives [EB/OL]. <https://lists.freebsd.org/archives/> ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,207 次提交。> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。
- dragonfly.duckdb dragonfly-src 仓库 contributors 表；dragonfly.duckdb dragonfly-src 仓库 tags 表（tagger_name 字段）；DragonFly BSD Digest [EB/OL]. <https://www.dragonflydigest.com/> ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,207 次提交。> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。
- dragonfly.duckdb dragonfly-src 与 freebsd-src 仓库 commits 表（按年统计对照）；freebsd.duckdb 查询 L3.7.1（changelog.db 项目编纂活动日条目数趋势 2026-07-16 至 07-25）；深层信息挖掘.md §L3.7.1；FreeBSD Foundation. Annual Reports [EB/OL]. <https://www.freebsdfoundation.org/our-donors/>；NetBSD Foundation. Bylaws [EB/OL]. <https://www.netbsd.org/foundation/>；DragonFly BSD Project. DragonFly BSD homepage [EB/OL]. <https://www.dragonflybsd.org/> (last edited 2025-10-03) ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,207 次提交。> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。
- dragonfly.duckdb dragonfly-src 仓库 commits 表与 tags 表；dragonfly.duckdb dragonfly-src/openbsd-src/netbsd-src/freebsd-src 仓库 commits 表（同口径对照）；DragonFly BSD Project. Releases [EB/OL]. <https://www.dragonflybsd.org/release/>；OpenBSD Foundation [EB/OL]. <https://www.openbsdfoundation.org/>；NetBSD Foundation [EB/OL]. <https://www.netbsd.org/foundation/>；统计分析报告：推断性统计.md Task 9 + 时间序列分析.md Task 15 [R/OL]. 2026-07-27. 文件路径：**03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/**；SQL 查询：`SELECT repo_name, strftime('%Y-%m', committer_date) AS month, COUNT(*) AS commit_count FROM commits WHERE repo_name = 'dragonfly-src' AND committer_date IS NOT NULL GROUP BY repo_name, month`. dragonfly.duckdb [DB/OL]. 查询日期：2026-07-27 [考据脚注：dragonfly-src GSoC 季节性 Wilcoxon W = 132.0 p = 0.6071 r = 0.1050、ARIMA(3,1,3) AIC = 233.80 MAPE = 70.88% RMSE = 127.03 coverage = 42.11%、2026-01 月 commit 异常激增至 503 次等统计结论经推断性统计.md Task 9 与时间序列分析.md Task 15 交叉验证。] ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,207 次提交。> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。
