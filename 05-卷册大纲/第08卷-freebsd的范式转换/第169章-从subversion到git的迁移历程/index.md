---
chapter: 第 169 章
id: CH169
volume: 第08卷-freebsd的范式转换
---

# 第 169 章 从subversion到git的迁移历程

## 要点

- FreeBSD 社区关于迁移到分布式版本控制系统的讨论始于 **2010 年代初期**，几乎与 Git 在 Linux 内核成功后开始流行同步；社区评估了多种分布式 VCS 选项，包括 Git、Mercurial（hg）、Bazaar（bzr）等；Git 之所以最终胜出而非 Mercurial 等其他 DVCS，原因包括：(1) Linux 内核采用 Git 产生的网络效应；(2) GitHub
- Git 工作组决策过程的一手史料主要包括：(1) freebsd-git@ 邮件列表的公开讨论存档（最完整、最权威）；(2) Git Transition Wiki 页面的历史版本（记录了方案演变）；(3) Ed Maste、Warner Losh 等人的会议演讲和博客文章；(4) Core Team 的公开状态报告；Core Team 内部讨论和投票细节未完全公开，部分决策理由只能从公开信息推断
- FreeBSD-doc Subversion to Git 迁移公告邮件经 freebsd-announce 邮件列表存档一手核验，发信人为 Warner Losh 与 Ed Maste（代表 git conversion working group），邮件正文明确"We will begin the migration sometime on December 5th and hope to b
- Git 迁移为 FreeBSD 带来的最显著长期变化是 CI/CD（持续集成/持续交付）能力的提升和外部贡献门槛的降低：(1) **CI/CD**：基于 GitLab CI 和 Cirrus CI 的自动化构建和测试管道在 Git 迁移后逐步建立，每次提交都会触发多架构构建和测试，这在 SVN 时代难以实现；(2) **外部贡献**：虽然 GitHub 不接受直接 PR，但开发者可以更容易地在 G
- Git 迁移争议相关一手史料的可靠性需分级评估：(1) **最高可信度**：官方 Wiki 时间表、freebsd-git 邮件列表原始帖子、版本控制系统中的 commit 记录——这些是当时形成的一手文档，可信度最高；(2) **高可信度**：Ed Maste（埃德·马斯特）、Warner Losh（沃纳·洛什） 等核心成员的会议演讲和博客文章——作者是亲历者，但事后回忆可能存在细节偏差；(3)

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3748] 卷“第08卷-freebsd的范式转换”第 169 章，匹配置信度 folder，原因：folder 第167章
- [DB:references_fulltext:chapter_matches:chmatch_3963] 卷“第08卷-freebsd的范式转换”第 169 章，匹配置信度 folder，原因：folder 第167章
- [DB:bsdnow_podcast:outline_mappings:om_11886] BSD Now 第 481 期，匹配 CH169 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_12157] BSD Now 第 452 期，匹配 CH169 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_12260] BSD Now 第 443 期，匹配 CH169 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_12823] BSD Now 第 307 期，匹配 CH169 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_10435] BSD Now 第 675 期，匹配 CH169 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10576] BSD Now 第 647 期，匹配 CH169 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10599] BSD Now 第 644 期，匹配 CH169 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10632] BSD Now 第 638 期，匹配 CH169 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10708] BSD Now 第 627 期，匹配 CH169 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10745] BSD Now 第 622 期，匹配 CH169 章，关联度 1.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 经邮件列表库验证通过（来源：freebsd-git 列表，Message-ID <CAPyFy2CKdHW_KkOOQozPW04jBDz8ZaNWSJLqFWAdzKcaDfSzcA@mail.gmail.com>，2017-02-21，Ed Maste 发起"Reconsider switching from svn to git?"，Warner Losh 回复）；经邮件列表库验证通过——2
- 部分评论称“Git 迁移是基金会强行推动的”——这一说法不准确：基金会提供了资金支持，但技术决策由 Git 工作组（由资深 committer 组成）做出，Core Team 保留最终批准权；基金会资助使迁移工作能够更快推进，但并未改变社区决策流程
- 考据过程留痕——【查证来源】(1) freebsd-announce 邮件列表 mailman 存档经 lists.freebsd.org/pipermail/freebsd-announce/2020-December/002002.html 一手核验，确认邮件标题"[FreeBSD-Announce] FreeBSD-doc Subversion to Git migration"、发信人 W
- “Git 迁移使 FreeBSD 开发速度大幅提升”这一说法需辩证看待——单个提交的合入速度不一定更快（因为审查流程可能更规范），但整体开发吞吐量确实因更好的工具链、更多外部贡献和 CI 自动化而提升；开发质量也因自动化测试而提高
- 部分争议点可能永远没有完全清晰的答案——例如 Core Team 内部讨论的细节、某些决策的真实考量、个别 committer 退役的真实原因等；史笔至此须存疑，不可为了叙事完整性而编造或推断

## 文献

- Maste, E. (2018). *Git for FreeBSD*. MeetBSD 2018 presentation; BSD Now. (2019-09-18). *Episode 316: git commit FreeBSD*; OpenBSD Project. *Why OpenBSD Developers Use CVS*. openbsd.org/anoncvs.html; Torvalds, L. (2005). *Git initial release announcement*. Linux Kernel Mailing List. ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1993-2008 年间：428,694 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- FreeBSD Project. *freebsd-git Mailing List Archives*. lists.freebsd.org; FreeBSD Wiki. *GitTransition* (page history); FreeBSD Foundation. (2019-2021). *Quarterly Status Reports*. ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2018-2019 年间：95,408 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- Losh W, Maste E. [FreeBSD-Announce] FreeBSD-doc Subversion to Git migration [EB/OL]. (2020-12)[2026-07-23]. <https://lists.freebsd.org/pipermail/freebsd-announce/2020-December/002002.html>; Losh W. FreeBSD Git Docs — Doc Cutover Schedule [EB/OL]. [2026-07-23]. <https://github.com/bsdimp/freebsd-git-docs/blob/main/doc-cutover-schedule.md>; FreeBSD Project. freebsd-git Mailing List Archives [DB/OL]. [2026-07-23]. <https://lists.freebsd.org/pipermail/freebsd-git/> ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2020-2021 年间：114,212 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- FreeBSD Project. *CI/CD Documentation*. ci.freebsd.org; FreeBSD Foundation. (2021-2024). *Annual Reports* (contributor growth statistics); Cirrus CI. *FreeBSD CI Configuration*. github.com/freebsd/freebsd-src/tree/main/.cirrus.yml. ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2024-2026 年间：168,386 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- FreeBSD Project. *freebsd-git and freebsd-hackers mailing list archives*. lists.freebsd.org; Wayback Machine. *FreeBSD Wiki historical snapshots*. web.archive.org; FreeBSD Foundation. (2021). *Git Migration Retrospective*. ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2024-2026 年间：168,386 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- FreeBSD Project. freebsd.db freebsd-src 仓库 commit 数据库 [DB/OL]. 2026-07-27. `c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\freebsd.db`; Hibsd Project. 推断性统计.md [R/OL]. 2026-07-27. `c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\统计分析\推断性统计.md` Task 5-6; Hibsd Project. 时间序列分析.md [R/OL]. 2026-07-27. `c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\统计分析\时间序列分析.md` Task 14-15; Hibsd Project. 卷章数据映射.md [R/OL]. 2026-07-27. `c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\统计分析\卷章数据映射.md` 第五卷第 66 章映射; Hibsd Project. 外部基准-GitHub-CHAOSS.md [R/OL]. 2026-07-27. `c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\统计分析\外部基准-GitHub-CHAOSS.md` 第 1.1 节（E-06、E-08 数据来源与三次复查留痕）; GitHub. Octoverse 2025: A new developer joins GitHub every second as AI leads TypeScript to #1 [R/OL]. 2025. URL: `https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/`（三次复查：2026-07-27）; Internet Archive. GitHub Octoverse 2014-2017 历年存档 [DB/OL]. `https://web.archive.org/web/2014-2017/https://octoverse.github.com/`（三次复查：2026-07-27）. ［A］FreeBSD 社区论文：[FP-2019-049] Poudriere for Port Maintenance（Matthew Seaman，2019）<https://papers.freebsd.org/2019/eurobsdcon/matthew-poudriere_for_port_maintenance/>FreeBSD 社区论文：[FP-2017-004] Continuous Integration of the FreeBSD Project（Li-Wen Hsu，2017）<https://papers.freebsd.org/2017/bsdcan/lwhsu-continuous_integration_of_the_freebsd_project/>FreeBSD 社区论文：[FP-2017-002] Continuous Integration of the FreeBSD Project（Li-Wen Hsu，2017）<https://papers.freebsd.org/2017/asiabsdcon/lwhsu-continuous_integration_of_the_freebsd_project/>FreeBSD 社区论文：[FP-2016-013] Continuous Integration of the FreeBSD Project（Li-Wen Hsu，2016）<https://papers.freebsd.org/2016/eurobsdcon/lwhsu-continuous_integration_of_the_freebsd_project/>FreeBSD 社区论文：[FP-2015-008] Supporting a BSD Project（Ed Maste，2015）<https://papers.freebsd.org/2015/vbsdcon/maste-supporting_a_bsd_project/>### 史观映射> 版本控制工具的更替不是进步的阶梯，而是技术债务的循环——每一代工具都承诺永久保存，又在下一代到来时沦为需要迁移的遗产；Git 迁移既是数字档案的重建机遇，也是历史保存的潜在威胁，因为每一次格式转换都意味着某些沉默的上下文永远丢失；从 CVS 到 SVN 再到 Git，这条迁移链印证了分离聚合的宿命——工具不断分裂又不断聚合，而代码始终是那个被搬来搬去的客体；但 FreeBSD 28 年开发史在三次工具更替中完整保留，这本身就是对 BSD 社区珍视历史、尊重传承精神的最好证明---> ## 第 66.12 不同时期人员的采访录（详见 [采访录.md](采访录.md)）## 第 66.13 节 媒体反响与社区舆论（详见 [媒体反响与社区舆论.md](媒体反响与社区舆论.md)）<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2024-2026 年间：168,386 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
