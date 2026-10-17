---
chapter: 第 108 章
id: CH108
volume: 第05卷-freebsd的工程化奠基
---

# 第 108 章 cvs到subversion

## 要点

- 迁移史料疑点：(1) 迁移起始时间；(2) 主要推动者（Wemm vs 核心团队）；(3) 是否有厂商参与
- 工具更替史料疑点：(1) cvsup 开发时间（1998 vs 更早）；(2) Polstra 的角色；(3) svnup 开发者
- 模式变化史料疑点：(1) 变化的时间线；(2) 关键推动者；(3) 是否有社区讨论影响变化
- 争论史料疑点：(1) 争论起始时间（2000 vs 更早）；(2) 关键参与者；(3) Wemm 的动机
- Peter Wemm（彼得·韦姆） 等 2007-2008 年主导迁移方案。技术核心是 SVN 的原子提交与分支效率，反对来自习惯 CVS 的老 committer 与主张直跳 Git 的激进派。

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3658] 卷“第06卷-freebsd的核心技术革新”第 108 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_1139] 卷“第06卷-freebsd的核心技术革新”第 108 章，匹配置信度 0.5，原因：无匹配
- [DB:references_fulltext:chapter_matches:chmatch_1299] 卷“第06卷-freebsd的核心技术革新”第 108 章，匹配置信度 0.5，原因：无匹配
- [DB:bsdnow_podcast:outline_mappings:om_12821] BSD Now 第 307 期，匹配 CH108 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_10532] BSD Now 第 655 期，匹配 CH108 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10603] BSD Now 第 642 期，匹配 CH108 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10688] BSD Now 第 630 期，匹配 CH108 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10801] BSD Now 第 613 期，匹配 CH108 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10857] BSD Now 第 605 期，匹配 CH108 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11140] BSD Now 第 571 期，匹配 CH108 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11259] BSD Now 第 558 期，匹配 CH108 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11601] BSD Now 第 516 期，匹配 CH108 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11627] BSD Now 第 513 期，匹配 CH108 章，关联度 1.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 厂商参与在 freebsd.duckdb 中无直接 commit 证据——查询 freebsd-src 与 freebsd-doc 仓库 2007-2008 年间 message_subject LIKE ‘%sponsor%’ 与 ’%funded%’ 均无命中，说明若有厂商参与 SVN 迁移，其痕迹主要在 Foundation 内部文件与邮件列表而非 commit 中；**统计局限性标注**——统计显
- 开发者归属在 freebsd.duckdb 中可部分验证——cvsup 开发者 John Polstra（<polstra@FreeBSD.org>）在 freebsd-src 仓库 1995-2007 年活跃，与 “cvsup 1998 年开发” 叙事吻合；svnup 开发者归属在 commit 中无直接证据，须依赖 freebsd-announce svnup release 公告与 free
- 变化原因在 bsd_commits.duckdb 中无直接 commit 证据——SVN 迁移作为模式变化的触发器是技术驱动的，但文化变化的深层原因（committer 群体代际更替、企业受薪开发者比重上升）须依赖邮件列表讨论与 Foundation 年度报告交叉验证
- Wemm 动机在 freebsd.duckdb 中无直接 commit 证据，须依赖 Wemm 本人在 freebsd-hackers 与 freebsd-arch 邮件列表中的自述与 SVN 迁移公告交叉验证
- 反对者名单在 freebsd.duckdb 中不可得（邮件签名不反映在 commit 中），须依赖 freebsd-hackers 与 freebsd-arch 邮件列表 2007-2008 年存档逐帖核查发件人与签名

## 文献

- freebsd-hackers mailing list 2007-2008 SVN migration archives；Wemm, P. SVN conversion project status (2008)；freebsd-arch mailing list VCS migration proposal (2008) ［A］；统计分析报告：描述性统计.md SubTask 2.1 [R/OL]. 2026-07-27. 文件路径：**03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/描述性统计.md**；统计分析报告：推断性统计.md Task 6 [R/OL]. 2026-07-27. 文件路径：**03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/推断性统计.md**；SQL 查询：`SELECT COUNT(*) FROM commits WHERE repo_name='freebsd-src'`. freebsd.duckdb [DB/OL]. 查询日期：2026-07-27；Python 统计脚本：`script/phase2_inferential.py`. Task 6 变点检测（Pettitt + BUISHAND）. 执行日期：2026-07-27 [考据脚注：C-03 freebsd-src 444,203 commits 与 C-12 变点 1999-08 经 `script/phase2_inferential.py` 执行结果与 `phase2_results.json` 结构化结果交叉验证；变点判定非迁移伪变点已通过距 2020-01 SVN-to-Git 迁移 245 个月的时间间距排除。]---## 史料登记与辩证校准（2026-08-08 追加）> **本卷命题**：24.2 劣币驱逐良币（详见本卷 00-总览“编纂指导思想叙事参照”）### 史料文献
- freebsd-hackers mailing list cvsup/svnup discussions (2008-2009)；Polstra, J. CVSup documentation (freebsd.org)；freebsd-announce svnup release (2009) ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- freebsd-hackers mailing list 2000-2008 VCS migration discussions；freebsd-arch mailing list VCS selection threads；FreeBSD Committer's Guide ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- freebsd-hackers mailing list 2000-2008 VCS debate archives；Wemm, P. SVN migration final decision (2008)；freebsd-arch mailing list 2008 VCS selection ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2008-2008 年间：32,755 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- Wemm 2008; 峰会纪要 ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- freebsd-hackers mailing list archives；FreeBSD Quarterly Status Reports；The FreeBSD Foundation Annual Reports ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- freebsd-hackers mailing list 2008-2010 SVN migration archives；Wemm, P. SVN migration report (2008)；freebsd-doc mailing list documentation migration (2008-2009) ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- 各项目官方文档 ［B］FreeBSD 社区论文：[FP-2019-049] Poudriere for Port Maintenance（Matthew Seaman，2019）<https://papers.freebsd.org/2019/eurobsdcon/matthew-poudriere_for_port_maintenance/>FreeBSD 社区论文：[FP-2017-004] Continuous Integration of the FreeBSD Project（Li-Wen Hsu（许立文），2017）<https://papers.freebsd.org/2017/bsdcan/lwhsu-continuous_integration_of_the_freebsd_project/>FreeBSD 社区论文：[FP-2017-002] Continuous Integration of the FreeBSD Project（Li-Wen Hsu，2017）<https://papers.freebsd.org/2017/asiabsdcon/lwhsu-continuous_integration_of_the_freebsd_project/>FreeBSD 社区论文：[FP-2016-013] Continuous Integration of the FreeBSD Project（Li-Wen Hsu，2016）<https://papers.freebsd.org/2016/eurobsdcon/lwhsu-continuous_integration_of_the_freebsd_project/>### 史观映射> 从 CVS 到 SVN 的迁移花了八年争论——不是因为技术难，而是因为选择版本控制工具就是在选择如何记忆开发史。CVS 的每一次提交、每一个分支、每一句日志都是开发记忆的载体，迁移意味着这些记忆要从一条无法重渡的河流搬到另一条——水还是那些水，但河床换了。而当 SVN 本身在 Git 面前也开始过时时，讽刺就完成了：用来对抗遗忘的工具，自己也会被遗忘### 史纲承载映射

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-1368 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1368`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Subversion for FreeBSD developers - Stefan Sperling〕讲者口述：Subversion 从一开始就是作为替换 CVS 的项目而设想的，整套设计基本建立在人们不喜欢的 CVS 缺陷之上；不是要造一个无所不能的版本控制系统，而是先找出 CVS 日常使用中不够好的部分再逐个修正。（YouTube EP3yGfXBCtXvE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1369 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1369`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Subversion for FreeBSD developers - Stefan Sperling〕讲者口述：在 CVS 中用标准用户界面重命名文件（不借助 repo copy 之类的变通手法），结果是留下一个已死的旧版本与一个全新文件，二者之间没有任何历史关联，除非在提交日志里手工写明该文件被移动。（YouTube EP3yGfXBCtXvE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1370 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1370`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Subversion for FreeBSD developers - Stefan Sperling〕讲者口述：讲者转述一家用 Subversion 管理代码、且所造 CT 扫描设备须取得 FCC 认证的机构的意见——如果这类改动会在流程中被无声丢掉，该机构便不能使用此工具，因为监管机构不会批准这样做。他自述此事发生在他本人参与项目之际，其公司随后接到一份小合同，与 Subversion 项目以及制造这些设备的厂商一起决定对策，最终让 Subversion 显示为冲突而非问号，并强制用户主动标记已解决才允许提交。（YouTube EP3yGfXBCtXvE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1371 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1371`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Subversion for FreeBSD developers - Stefan Sperling〕讲者口述：他据印象描述 FreeBSD 分支模型的层次——先由 head 复制出 stable，再由其中创建 releases，复出一条 release 用分支，最后才打出实际发布标签；这些分支与标签在 Subversion 数据模型里都只是 copy，区别仅在于分支会继续被改动而标签不再改动，模型本身不区分，因此可以拿一个标签继续当作分支使用。（YouTube EP3yGfXBCtXvE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
