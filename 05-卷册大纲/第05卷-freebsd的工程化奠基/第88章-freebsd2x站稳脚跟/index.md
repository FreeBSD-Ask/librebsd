---
chapter: 第 88 章
id: CH88
volume: 第05卷-freebsd的工程化奠基
---

# 第 88 章 freebsd2x站稳脚跟

## 要点

- FreeBSD 代码仓库时间跨度（1993-06-12 至 2026-08-25），覆盖 2.x 至今 30 余年持续开发

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3965] 卷“第05卷-freebsd的工程化奠基”第 88 章，匹配置信度 folder，原因：folder 第86章

- [DB:code_repos:freebsd.duckdb] FreeBSD 代码仓库时间跨度（1993-06-12 至 2026-08-25），覆盖 2.x 至今 30 余年持续开发

## 史观

- 动手者创造历史：FreeBSD 2.x 的稳定是无数默默贡献者的工程积累，非少数明星开发者之功

## 辨析

- 2.x 时期部分 commit log 在迁移中丢失作者信息，需对照 freebsd-committers 邮件列表人工修复；2.2.8 与 2.2.8-STABLE 的区别常被混淆；**统计局限性标注**——统计显著 ≠ 实际显著，C-12 变点 p < 0.001 仅反映 commit 时序存在结构性断点，不等于 2.x 至 3.x 转型在工程上 “必然” 发生；C-12 双检验一致性（Pet
- Mindcraft 测试引发的争议 (1999) 显示操作系统性能比较的政治性，需警惕厂商赞助测试的偏见
- ipfw 防火墙对 LAND/smurf 攻击的实际防御效果须对照 ipfw 规则语法与 FreeBSD 2.2.x 默认配置核实——ipfw 提供过滤能力但默认配置可能未启用，史家须区分 “防火墙能力存在” 与 “默认启用” 两个维度；MFC 回溯机制的覆盖率须逐 SA 核实——部分 SA 的修复可能未 MFC 回溯至所有受影响稳定分支，史家不得以 “MFC 机制存在” 推论 “所有漏洞均已回溯
- ipfw 1 与 ipfw 2 的分界点存在 1996 与 1998 两种说法，需查 commit log 中 ip_fw.c 的大改记录
- Ports 在 1994 与 1995 的版本号体系不清晰，"Ports 1.0" 从未被官方命名，需以 bsd.port.mk 版本号为准

## 文献

- [DB:references_fulltext] 参考文献全文数据库（4077 篇全文，27138 条时间线事件）—— 对应 freebsd.duckdb
