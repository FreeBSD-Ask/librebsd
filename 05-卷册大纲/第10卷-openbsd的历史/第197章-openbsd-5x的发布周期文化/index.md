---
chapter: 第 197 章
id: CH197
volume: 第10卷-openbsd的历史
---

# 第 197 章 openbsd-5x的发布周期文化

## 要点

- OpenBSD 提交高峰期：2015年(22014次)，对应 5.x 发布周期文化确立期

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4013] 卷“第10卷-openbsd的历史”第 197 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

- [DB:code_repos:openbsd.duckdb] OpenBSD 提交高峰期：2015年(22014次)，对应 5.x 发布周期文化确立期

## 史观

- 循环而非进步：OpenBSD 5.x 的发布周期文化不是进步，而是对'稳定发布'这一承诺的循环性履行

## 辨析

- Release Notes 的完整性以 plus.html 页面为准——该页面仅记录“重要的和用户可见的变更”，部分内部代码重构（如 guenther 的 NOLOCK 标记）可能未在 Release Notes 中记录但可在 commit log 中定位；OpenBSD 仓库无 release tag（OpenBSD 使用 CVS 而非 git tag 标记 release），故 release
- de Raadt 发言的语义以 marc.info 存档原始帖子为准——部分帖子被社区解读为“粗暴”，但原始语境中多为技术论证；邮件列表档案的完整性以 marc.info 与 OpenBSD 官方存档为准——早期档案（1995-2000）可能存在缺失 [考据完成：2026-07-28 OpenBSD 邮件列表 1995-2000 年存档的完整性未经验证，marc.info 的 openbsd-mi
- 邮件列表档案的完整性以 marc.info 存档为准——部分权限撤销讨论可能在私有列表进行，公开档案无法覆盖全部讨论；个别权限撤销事件的具体细节以多源交叉验证为准——邮件列表、hackathons 记录、contributors 表三者交叉
- 批评的具体语境以原始邮件列表帖子为准——OSNews、Slashdot 等技术媒体的报道常简化邮件列表讨论的完整语境；de Raadt 回应的语义以 marc.info 存档原始帖子为准——部分回应被解读为“粗暴”但在原始语境中多为技术论证
- commit 记录的归属以 bsd_commits.db openbsd-src 仓库 commits 表 author_name 与 commit_files 表 file_path 交叉验证为准——部分 patch 由多人协作但仅一人 commit，commit_files 表可定位实际代码变更者；邮件列表档案的完整性以 marc.info 存档为准

## 文献

- [DB:references_fulltext] 参考文献全文数据库（4077 篇全文，27138 条时间线事件）—— 对应 openbsd.duckdb
