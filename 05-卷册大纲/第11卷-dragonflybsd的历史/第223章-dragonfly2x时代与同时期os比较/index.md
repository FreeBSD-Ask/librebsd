---
chapter: 第 223 章
id: CH223
volume: 第11卷-dragonflybsd的历史
---

# 第 223 章 dragonfly2x时代与同时期os比较

## 要点

- 2003-2010 年间 BSD 各项目的发布频率、committer 数量、用户社区规模、市场份额数据考据，量化各项目的相对地位
- DragonFly 2.0（2008）发布 HAMMER 1.0 文件系统，但 2.x 周期 dragonfly.db 未见直接归因于 HAMMER 文件系统的 CVE——HAMMER 作为新文件系统在 2.x 周期部署规模有限，漏洞尚未充分暴露；HAMMER 的 B-tree 写时复制设计在理论上提供了崩溃一致性保障，但写时复制引入的新代码路径（B-tree 节点分裂、记录同步、undo/red
- dragonfly 代码仓库共 656,206 次提交（2003-06-17 至 2026-08-18），535 位贡献者

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4047] 卷“第11卷-dragonflybsd的历史”第 223 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 市场份额数据需谨慎采用——BSD 项目通常无商业销售数据，需结合镜像下载量、邮件列表活跃度、第三方调查等多源数据交叉验证。具体争议点：1) bsd_commits.db dragonfly-src 仓库 2003-2010 年间 contributor 数量（2003 年 10 位、2005 年峰值 22 位、2008 年 36 位）与 freebsd-src 同期数据对比须单独查询，commit
- HAMMER 1.0 在 2.x 周期无 CVE 的原因有二——其一，HAMMER 部署规模有限，漏洞未充分暴露；其二，HAMMER 作为新文件系统，安全研究社区的审计关注较少；HAMMER 写时复制设计的崩溃一致性保障不等于安全性——崩溃一致性保护的是数据完整性，不直接防御恶意构造的文件系统镜像攻击 [考据完成：2026-07-28 HAMMER 1.0 在 2.x 周期无 CVE 可能因部署规
- 贡献者高度集中——Top 1 贡献者 DPorts Builder 占比 88.0%，需考量'个人主导'与'社区协作'的叙事张力

## 文献

- 各项目 release notes 与官网；BSD 相关市场调研报告；邮件列表活跃度统计 ［A］<!-- DB_REF:netbsd.duckdb -->> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2003-2010 年间：771,745 次提交。> 仓库总览：1,999,412 次提交，4,754 位贡献者，1992-07-13 至 2026-08-24。
- bsd_commits.db dragonfly-src 仓库；DragonFly 2.0 Release Notes；Matt Dillon HAMMER 设计文档 ［A］<!-- DB_REF:dragonfly.duckdb -->> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,206 次提交。> 仓库总览：656,206 次提交，535 位贡献者，2003-06-17 至 2026-08-18。
