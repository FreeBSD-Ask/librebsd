---
chapter: 第 240 章
id: CH240
volume: 第12卷-macos的bsd遗产
---

# 第 240 章 darwin的开放核心apsl许可证与开源

## 要点

- Darwin 仓库共 2016 次提交（2001-04-10 至 2026-04-13）；commits 表按 author_name 计仅 1 个发布账号（Apple OSS Distributions），contributors 表则计 43 位贡献者——单一发布账号口径源于 Apple 官方源码转储镜像的导入方式，与 Apple 开放核心模式的封闭开发流程相印证，但不等于实际开发者人数

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4056] 卷“第12卷-macos的bsd遗产”第 240 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_4057] 卷“第12卷-macos的bsd遗产”第 240 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

- [DB:code_repos:darwin.duckdb] Darwin 仓库共 2016 次提交（2001-04-10 至 2026-04-13）；commits 表按 author_name 计仅 1 个发布账号（Apple OSS Distributions），contributors 表则计 43 位贡献者，单一发布账号口径源于 Apple 官方源码转储镜像的导入方式
- [DB:historical_claims:claim] 关键词行级挖掘素材线索 240.4-关键词行级挖掘素材线索（2 条，CL-RM 段，见 240.4-关键词行级挖掘素材线索.md）

## 史观

- 形式主义：Darwin 的开源是 Apple 对开源社区的形式主义承诺，其实际开源投入有限

## 辨析

- APSL 1.1 与 1.2 的具体变更条款——以 FSF 的逐版评价为准，APSL 1.1 的 “暂停条款” 实质上仍为 “终止条款” 的变体，未消除原有恶果；APSL 1.2 修复两项缺陷但 “部署即发布” 条款仍存。采信 “APSL 1.1 未实质性改善，APSL 1.2 修复两项缺陷但仍差最后一步” 的判断，标注 ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- 参考文献全文数据库（4077 篇全文，27138 条时间线事件）——对应 **darwin.duckdb** 镜像仓库的统计口径须辨析：commits 表 2016 次提交全部署名发布账号 Apple OSS Distributions，contributors 表却计 43 位贡献者，两表口径不一；以 commit 作者推断 Darwin 开发结构会得出“单作者”误判，该库实为 Apple 官方源码转储镜像，可能因 macOS 12 周期内 [存疑脚注] 原辨析二在“可能因 macOS 12 周期内”处机械截断、后文佚失无法回源，残句保留待原始档案公开后补充确证；口径数据经 **darwin.duckdb** 2026-09-13 查证。