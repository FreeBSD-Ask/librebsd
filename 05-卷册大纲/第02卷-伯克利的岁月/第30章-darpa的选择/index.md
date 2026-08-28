---
chapter: 第 30 章
id: CH30
volume: 第02卷-伯克利的岁月
---

# 第 30 章 darpa的选择

## 要点

- DARPA 与伯克利的合同于 1980 年 4 月开始，为期 18 个月；Bob Fabry 于 1979 年秋撰写提案，1979 年 12 月 3BSD 发布打消 DARPA 疑虑；初始合同覆盖 4BSD（1980 年 10 月）至 4.1BSD（1981 年 6 月）开发；**Fabry 提案原始文档归档**——Fabry 1980 年提案 "Proposal for Configuratio
- UNIX V6/V7 早期信号机制（signals）为 “不可靠信号”——信号处理后系统会重置信号处理函数为默认值（SIG_DFL），导致应用程序若需重复捕获同一信号须在处理函数内重新调用 **signal(2)** 安装处理函数，存在竞争窗口（race condition）：信号可能在处理函数重置与重新安装之间到达而被默认处理（通常为终止进程）；4BSD（1980 年 10 月）引入 “可靠信号
- BSD 在 DARPA 资助项目中占据基础性地位——Mach 基于 BSD 代码、Athena 使用 BSD 工作站，BSD 成为 DARPA 操作系统研究的公共基础设施
- DARPA 对伯克利 BSD 的评审过程并非单一时点的评标，而是贯穿 1979 年至 1985 年的多阶段过程，涉及 DARPA IPTO、伯克利 CSRG、BBN 三方的立场差异与利益博弈；评审过程可划分为五个阶段——(1) **1979 年秋招标语境评审**：DARPA 决定统一操作系统并选择 UNIX，基于其 "proven portability"（已验证的可移植性），此决策由 DARPA
- CSRG 作为 BSD 的核心组织，从 1980 年代至 1990 年代初推动了 4BSD 到 4.4BSD 的全部主要版本，是开源软件史上最成功的学术研究小组之一

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3869] 卷“第02卷-伯克利的岁月”第 30 章，匹配置信度 folder，原因：folder 第30章
- [DB:references_fulltext:chapter_matches:chmatch_3885] 卷“第02卷-伯克利的岁月”第 30 章，匹配置信度 folder，原因：folder 第30章
- [DB:references_fulltext:chapter_matches:chmatch_3955] 卷“第02卷-伯克利的岁月”第 30 章，匹配置信度 folder，原因：folder 第30章
- [DB:references_fulltext:chapter_matches:chmatch_4162] 卷“第02卷-伯克利的岁月”第 30 章，匹配置信度 1.0，原因：Leffler 61MB（BSD C 编译器奠基）+ Shannon 47.5MB（请求分页 UNIX）；清单#32 论文源头
- [DB:references_fulltext:chapter_matches:chmatch_4164] 卷“第02卷-伯克利的岁月”第 30 章，匹配置信度 1.0，原因：Berkeley_Unix_History.pdf(2.2MB)+unixreview 1984dec(24.8MB)/1985jan(34.5MB)
- [DB:references_fulltext:chapter_matches:chmatch_4168] 卷“第02卷-伯克利的岁月”第 30 章，匹配置信度 1.0，原因：22.5MB 整期杂志
- [DB:references_fulltext:chapter_matches:chmatch_4169] 卷“第02卷-伯克利的岁月”第 30 章，匹配置信度 1.0，原因：top_level_names 显示 disk1 含 1BSD 至 4.3BSD 全部源码；Bancroft CSRG Records(#100) 数字化索引线索；非 ISO
- [DB:references_fulltext:chapter_matches:chmatch_4184] 卷“第02卷-伯克利的岁月”第 30 章，匹配置信度 1.0，原因：PSD:5 伯克利软件架构手册
- [DB:references_fulltext:chapter_matches:chmatch_4188] 卷“第02卷-伯克利的岁月”第 30 章，匹配置信度 1.0，原因：PSD:18 gprof 性能剖析
- [DB:references_fulltext:chapter_matches:chmatch_4199] 卷“第02卷-伯克利的岁月”第 30 章，匹配置信度 1.0，原因：SMM:1 系统安装
- [DB:bsdnow_podcast:outline_mappings:om_11801] BSD Now 第 487 期，匹配 CH30 章，关联度 1.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 合同开始日期确认为 1980 年 4 月（McKusick 1999 明确记载）；初始合同期限为 18 个月；4.1BSD 发布于 1981 年 6 月而非 1981 年 4 月；初始合同号 F19628-80-C-0002 与后续合同 N00039-82-C-0235（1981-1983）需区分，具体初始合同号 据一手文献印证消解^doubt-resolved-174：此处事实待多源交叉验证 ］
- reliable signals 并未立即 “淘汰” unreliable signals——**signal(2)** 接口在 BSD 中长期保留作为兼容层，调用 **signal(2)** 内部转换为 **sigaction(2)**，须区分 “API 接口淘汰” 与 “实现机制淘汰”；System V 采纳 reliable signals 的时间为 SVR3（1987 年前后），非 SVR
- BSD 在 DARPA 项目中的 “基础” 地位是否被高估存在争议，需核对各项目实际代码依赖
- [考据完成：2026-07-28 该处辨析所涉存疑点经穷尽联网考据，属史料缺口，详见上下文分析] 本节缺口建议中提及 “DARPA IPTO（如 Saal 视角）”，但 McKusick 1999 一手原文中未提及名为 "Saal" 的 DARPA IPTO 项目经理——McKusick 1999 明确记载的 DARPA 代表为 Duane Adams（合同监督人，contract monitor
- CSRG 解散时间确认为 1995 年 6 月（4.4BSD-Lite Release 2 发布后解散，McKusick 1999 明确记载），非 1992 年

## 文献

- McKusick, M. K. (1999) "Twenty Years of Berkeley Unix: From AT&T-Owned to Freely Redistributable", in Open Sources: Voices from the Open Source Revolution, O'Reilly, ISBN 978-1-56592-582-3；Fabry, R. S. (1980) "Proposal for Configuration Control for the ARPA Standard Version of the UNIX Operating System", DTIC ADA094691（<https://apps.dtic.mil/sti/tr/pdf/ADA094691.pdf>，元数据页面 <https://apps.dtic.mil/sti/citations/ADA094691>，访问日期 2026-07-28） ［B］
- 4BSD Release Notes (1980.10)；4BSD sigblock(2) 手册页；POSIX.1 (1988) IEEE Std 1003.1；Bach, M. J. (1986) "The Design of the UNIX Operating System", Prentice-Hall, ISBN 0-13-201799-7；Stevens, W. R. (1992) "Advanced Programming in the UNIX Environment", Addison-Wesley, ISBN 0-201-56317-7；McKusick, M. K. et al. (1996) "The Design and Implementation of the 4.4BSD Operating System", Addison-Wesley, ISBN 0-201-54979-4 ［A］
- Rashid, R. et al. (1988) "Mach Architecture"；MIT Athena 项目技术报告[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- McKusick, M. K. (1999) "Twenty Years of Berkeley Unix"；CSRG (1995) "4.4BSD-Lite Release 2 Final Report" ［B］
- Cerf, V. & Kahn, R. (1974) "A Protocol for Packet Network Intercommunication"；4.2BSD Networking Manual[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- TUHS 存档； McKusick 1999 ‘Twenty Years of Berkeley Unix’ ［B］
- FOIA 申请获取的 DARPA 档案；学术界对 DARPA 决策的二手研究[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- FOIA 请求档案；BBN 历史档案（部分公开）[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- BSD License (1988) 原文；McKusick, M. K. (1999) "Twenty Years of Berkeley Unix" ［B］
- McKusick, M. K. (1999) "Twenty Years of Berkeley Unix"；Quarterman, J. S. et al. (1985) "4.2BSD and 4.3BSD as examples of the Unix system", ACM Computing Surveys 17(4): 379-418, DOI: 10.1145/6041.6043；统计分析报告：文献计量学分析.md Task 22 [R/OL]. 2026-07-27. 文件路径：**c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\统计分析\文献计量学分析.md**；统计分析报告：描述性统计.md SubTask 2.1 [R/OL]. 2026-07-27. 文件路径：**c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\统计分析\描述性统计.md**；SQL 查询：`SELECT id, gbt7714 FROM "references"` 与 `SELECT COUNT(*) FROM commits WHERE repo_name='freebsd-src'`. 资料数据库.db 与 bsd_commits.db [DB/OL]. 查询日期：2026-07-27；Python 统计脚本：`script/phase6_bibliometrics.py` Task 22 与 `script/phase1_descriptive.py` SubTask 2.1. 执行日期：2026-07-27 ［B］

<!-- PODCAST_MINE v20260827 -->
<!-- 章节主题过滤：第30章-darpa的选择 第 30 章 darpa的选择（实体评分 ≥2 命中才入选） -->
<!-- 匹配期数：1 期，扫描 segments：1552 条 -->

### 要点（播客口述史提取）
- （该章节匹配播客中未提取到高置信度核心史实，需人工深挖）

### 史料（播客当事人陈述）
- （待人工提取）

### 史观（播客当事人观点与总纲映射）
- （该章节匹配播客中未提取到当事人观点性陈述）

### 辨析（播客争议与存疑点）
- （该章节匹配播客中未提取到争议性陈述）

### 文献（播客参考条目）
- [BSD Now EP190] Pennington J. BSD Now: 190: The Moore You Know[EB/OL]. (2017-04-19)[2026-08-15]. https://www.bsdnow.tv/190.

<!-- /PODCAST_MINE -->
