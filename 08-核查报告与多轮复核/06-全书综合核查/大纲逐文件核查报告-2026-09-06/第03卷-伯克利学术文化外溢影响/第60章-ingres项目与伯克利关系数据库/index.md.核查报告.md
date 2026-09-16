# 核查报告：第03卷-伯克利学术文化外溢影响/第60章-ingres项目与伯克利关系数据库/index.md
- 源文件：d:\librebsd\05-卷册大纲\第03卷-伯克利学术文化外溢影响\第60章-ingres项目与伯克利关系数据库\index.md
- 批次：C077；检查日期：2026-09-09；复核日期：2026-09-16（内容级 P0 复核）；检查方式：逐文件完整阅读人工核查（复核为 Read 完整阅读）；另核对本章目录清单与 `05-卷册大纲\SUMMARY.md` 第 506-512 行；EnterpriseDB 创立年份经 EDB 官方材料（enterprisedb.com 公开演示稿“2004 EDB is founded”、trueup.io 公司条目“Founded March 2004”）联网复核
- SUMMARY.md 收录：未收录（flags 标 UNLISTED_NOT_IN_SUMMARY；SUMMARY.md 第 506 行收录的是本章 `概述.md`，本章 60.1-60.4 与 `媒体反响与社区舆论.md`、`采访录：Michael Stonebraker.md` 均单独收录，`index.md` 无对应条目）
- A 占位符：通过（0 处）。原报告判定的行 24“## 史观”下“(待人工回填……)”空槽已随 2026-09-11 整改改为编排说明“（章级史观/辨析按子节字段聚合回填——本卷 60 章；……完整聚合随正文阶段逐章完成）”
- B 内容完整性：发现 1 处（要点 4 条与辨析 4 条共 7 条仍机械截断于词中，见问题清单第 1 条）
- C 编号与标题：发现 1 处（轻微：H1 章名与 SUMMARY 收录标题大小写/空格不一致，见问题清单第 4 条）
- D 格式规范：发现 2 处（畸形 autolink、全角方括号标记体系不统一，见问题清单第 3、6 条；原报告判定的提交信息 ASCII 直引号已统一为弯引号，不再成立；手册页 **spamd(8)**、**spamdb(8)**、**db(3)** 与路径 **/var/db/spamd** 格式合规）
- E 学术规范：发现 3 处（EnterpriseDB 史实错误、脚注定义错乱且含无关 MARC 残片、判例存疑未标注 [存疑脚注]，见问题清单第 2、5、6 条）
- F SUMMARY 一致性：不一致（章入口双份：`index.md` 与 `概述.md` 并存，SUMMARY 仅指向后者）
- 机械旗标复核：`UNLISTED_NOT_IN_SUMMARY` 成立——经核对 SUMMARY.md 第 506-512 行，本章以 `概述.md` 为章入口收录，本文件 `index.md` 确未被任何行引用；旗标为真，非误报
- 问题清单：

| 编号 | 行号 | 原文摘录（≤60字） | 问题类型 | 严重度 | 修改建议 |
| --- | --- | --- | --- | --- | --- |
| 1 | 12、13、14、28、29、30、31 | “（4）PostgreSQL”“推动 FreeBS”“使用 O”“后改名 Ingr”“Postgre”“Jordan K. Hu”“NetBSD pkgsrc 经 pkgsrc.org” | B 内容完整性：要点 4 条与辨析 4 条共 7 条在句中/词中被机械截断，无句号收尾，论证链条断裂，读者无法获知结论 | P0 | 从 `sacred_sources.duckdb`/`references_fulltext.duckdb` 或原生成记录回补完整句；同时排查同批生成脚本的固定长度截断缺陷（本卷其余章 index.md 需一并复查） |
| 2 | 12、29 | “BSD 许可证使 PostgreSQL 被 EnterpriseDB（2005 年创立）等公司商业化” | E 学术规范（史实）：EnterpriseDB 创立于 2004 年 3 月（EDB 官方材料“2004 EDB is founded”一致），正文两处写作“2005 年”，且未标注存疑 | P1 | 两处年份统一改为 2004；同时核验创始人姓名“Astyanax Kanavis、Andrzej Krawczyk、Edward Behrend”是否见于公司注册/SEC 档案，未确证前加 [存疑脚注] |
| 3 | 35、41 | “(<https://www.computerhistory.org/profile/michael-stonebraker/)；Relational> Technology Inc.”“（<https://www.sqlite.org/chronology.html，确>认 SQLite 1.0 …）” | D 格式规范：autolink 尖括号位置错乱，中文与分号被吞入 URL，链接渲染失效、正文出现游离 `>` 字符 | P1 | 改为 `<https://…>` 完整包裹纯 URL，中文说明置于尖括号之外，例如“Computer History Museum. *Michael Stonebraker Profile* [EB/OL]. <https://www.computerhistory.org/profile/michael-stonebraker/>” |
| 4 | 35 | “[据一手文献印证消解^doubt-resolved-134——具体创立日期需查阅 SEC EDGAR …]” | E/D 脚注与引用格式：脚注引用语法残缺（缺 `[^`），行内夹破折号解释；同行堆叠 7 条 `[^doubt-resolved-134]` 至 `[^doubt-resolved-141]` 定义，内含与本主题无关的 MARC 残片（“-- Meeker, Heather J_, 1959- -- … (1959)”“Mac OS X Internals …(未署名)”），135/136/137/138/139/141 在正文无对应引用（悬空定义） | P1 | 修正引用语法为 `[^doubt-resolved-134]`；脚注定义逐条换行移至文末；删除或重挂无关 MARC 残片与悬空定义；消解依据须与所支撑论断主题一致 |
| 5 | 全章（对照 SUMMARY.md 506） | 磁盘同时存在 `index.md` 与 `概述.md`，SUMMARY 仅收录后者 | F SUMMARY 一致性/结构：章入口重复，`index.md` 成孤儿文件，存在两份分叉的章级要点 | P1 | 二选一保留（建议保留被收录的 `概述.md`），把 `index.md` 中经考据修正的“辨析”内容合并入 `概述.md`，再删除 `index.md`；删除须按流程规则走备份与 changelog 登记 |
| 6 | 35、36、37、38 | “…Microsoft SQL Server 历史档案 ［B］”“^doubt-resolved-134 …… 消解” | D/E：文献条目尾全角方括号标记“［B］”与项目既有证据分级“〔L3 官方文档与公告〕”体系不统一，含义未记；脚注定义沿用自创形制，存疑未标 [存疑脚注] | P2 | 统一为〔…〕证据等级标注；存疑改用规范 [存疑脚注] 形制 |
| 7 | 7 | “# 第 60 章 ingres项目与伯克利关系数据库” | C 编号与标题：H1 章名与 SUMMARY 第 506 行“第 60 章 Ingres 项目与伯克利关系数据库”不一致（专有名词小写、拉丁-中文之间缺空格） | P2 | H1 改为“第 60 章 Ingres 项目与伯克利关系数据库”；目录名是否随之改名按流程规则“序号调整例外/命名规范”评估，勿径改 |
| 8 | 13、14 | “MySQL 与 FreeBSD Ports 的共生关系”“SQLite 在 BSD 嵌入式场景中的部署” | B 归属自洽：MySQL（Monty Widenius，非伯克利）、SQLite（D. Richard Hipp，非伯克利关系数据库谱系）超出章名“Ingres 项目与伯克利关系数据库”的承诺范围；同卷第 61 章“BSD 数据库服务器生态”已含 61.6 MySQL/PostgreSQL 谱系 | P2 | 或将 MySQL/SQLite 两条并入第 61 章，或改章名为“伯克利关系数据库传统与 BSD 数据库生态”，并同步 SUMMARY |

- 结论：存在问题 8 项（P0 1、P1 4、P2 3、P3 0）

补充说明：本报告为内容级 P0 复核更新。原报告（2026-09-09）判定 P0 2 项、P1 5 项、P2 3 项。经复核源文件当前实况（2026-09-11 整改）：①原 P0 史观“待人工回填”空槽已改编排说明，不再成立；②原 P1 提交信息 ASCII 直引号已统一为弯引号（现行行 37），不再成立。仍成立的问题为：要点/辨析 7 条机械截断（P0）、EnterpriseDB 2005 史实（P1）、autolink 畸形（P1）、脚注定义错乱含 MARC 残片（P1）、章入口双份（P1）、证据分级体系不统一（P2）、H1 大小写不一致（P2）、MySQL/SQLite 归属越界（P2），共 8 项，予以保留。复核后按当前实况更新为 P0 1、P1 4、P2 3、P3 0。

原报告结论行“存在问题 10 项（P0 2、P1 5、P2 3、P3 0）”与问题清单 10 行编号自洽，无条目-结论计数不一致；复核后调整为 8 项。EnterpriseDB 年份结论仍依据 EDB 自有公开材料与第三方公司条目一致，属可复核来源，未采信维基百科。
