---
chapter: 第 29 章
id: CH29
volume: 第02卷-伯克利的岁月
---

# 第 29 章 对vi与cshell的批评

## 要点

- 1BSD 时期（1978）伯克利校内计算机互联依赖早期点对点拨号与 ARPANET，缺乏本地批量邮件传输机制；Eric Schmidt 1978 年在伯克利硕士论文中开发 Berknet（Berkeley Network），通过串行电话线连接伯克利校内多台 PDP-11，实现邮件转发、文件传输与远程执行功能，是 BSD 谱系最早的本地网络协议实现之一；Berknet 随 2BSD（1978 年中）
- **1979 年** 同期编辑器路径——vi（学术磁带分发，模态固定）、emacs（学术/MIT，Lisp 可扩展）、TECO EDT（MIT/商业，可编程）、VMS EDT（商业，keypad 全屏）展现编辑器设计的多元分化| 编辑器 | 发布年份 | 作者/机构 | 范式 | 扩展性 | 分发渠道

| --- | --- | --- | --- | --- | --- |
| --- | --- | --- | --- | --- | --- |
| vi | 197 |  |  |  |  |

- 对 vi 与 csh 的批评部分存在形式主义倾向——以 “优雅” 或 “一致性” 等先验标准评判实践驱动的工具，忽视了工具的实践合理性
- vi 与 csh 的边缘贡献者史料散见于邮件列表、文档署名与会议记录，缺乏系统化档案，这是 BSD 史学研究的重要空白
- vi 与 csh 自 1978 年 2BSD 发布以来已延续 **47 年**（截至 2026 年），其影响力体现于三个层面——(1) 直接谱系延续：vi 谱系经 vim（1991）、elvis（1990）、nvi（1994）、Neovim（2015）持续演化，csh 谱系经 tcsh（1981）延续；(2) 功能扩散：vi 模态被 emacs（viper-mode/evil-mode）、VS C

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3720] 卷“第02卷-伯克利的岁月”第 29 章，匹配置信度 folder，原因：folder 第29章
- [DB:references_fulltext:chapter_matches:chmatch_3735] 卷“第02卷-伯克利的岁月”第 29 章，匹配置信度 folder，原因：folder 第29章
- [DB:references_fulltext:chapter_matches:chmatch_3916] 卷“第02卷-伯克利的岁月”第 29 章，匹配置信度 folder，原因：folder 第29章
- [DB:references_fulltext:chapter_matches:chmatch_3930] 卷“第02卷-伯克利的岁月”第 29 章，匹配置信度 folder，原因：folder 第29章
- [DB:references_fulltext:chapter_matches:chmatch_3932] 卷“第02卷-伯克利的岁月”第 29 章，匹配置信度 folder，原因：folder 第29章
- [DB:references_fulltext:chapter_matches:chmatch_3938] 卷“第02卷-伯克利的岁月”第 29 章，匹配置信度 folder，原因：folder 第29章
- [DB:references_fulltext:chapter_matches:chmatch_4165] 卷“第02卷-伯克利的岁月”第 29 章，匹配置信度 1.0，原因：8 卷 PDF（合计约 100MB）；V7 时代 32V 手册，BSD 前身系统
- [DB:references_fulltext:chapter_matches:chmatch_1542] 卷“第02卷-伯克利的岁月”第 29 章，匹配置信度 0.9，原因：关键词搜索下载文献，标题含章节主题

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- Berknet 与 UUCP 的关系需严格区分——UUCP 由 Bell Labs Nowitz 1978 年开发，是 Bell Labs 谱系，Berknet 是伯克利 Schmidt 1978 年独立开发，二者同期但独立；Berknet 被 “取代” 的精确时间节点在不同史料中不一致，须区分校内遗留使用（持续到 1980 年代中期）与主邮件路径退场（4.3BSD 1986）；Schmidt 后
- 形式主义批评与非形式主义批评的边界需个案分析，避免将所有批评都归为形式主义
- [自反性声明] 本小节的 “跨时代评估” 本身即是一种事后建构——将 vi/csh 的持续使用追溯为 “实践设计的胜利” 是史家的叙事框架，而非历史参与者（Joy、Moolenaar、De Arruda 等）的自觉意图；按项目史观总纲第 5 章 5.3 节 “记忆将许多偶然性认识为一种必然性”，“vi 模态的持久生命力” 这一判断可能将偶然的路径依赖（vim 取代 vi 成为事实标准、VS Cod

## 文献

- Schmidt, E. (1978) 伯克利硕士论文 Berknet 设计文档；Joy, W. (1978) "2BSD Release Notes"；Allman, E. (1983) "Sendmail Installation and Operation Guide"；Postel, J. (1982) RFC 821 "Simple Mail Transfer Protocol"；Nowitz, M. (1978) UUCP Documentation Bell Labs；McKusick, K. (1999) "Twenty Years of Berkeley Unix"；统计分析报告：文献计量学分析.md Task 22 [R/OL]. 2026-07-27. 文件路径：**c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\统计分析\文献计量学分析.md**；SQL 查询：`SELECT id, gbt7714 FROM "references"`. 资料数据库.db [DB/OL]. 查询日期：2026-07-27；Python 统计脚本：`script/phase6_bibliometrics.py`. Task 22 参考文献增长曲线与 Price 指数。执行日期：2026-07-27 ［B］
- Raymond, E. S. (1996) "The Art of Unix Programming"；USENIX 1979 年会议论文集 ［B］
- Dewey, J. (1929) "Experience and Nature"；Rorty, R. (1979) "Philosophy and the Mirror of Nature"[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- USENIX Association 会议论文集（1978-1985）；伯克利 CSRG 邮件列表存档 ［A］
- 综合 11.8.1（Neovim/vim/elvis/nvi）、11.8.2（viper-mode/evil-mode/VS Code Vim/IdeaVim）、11.8.3（tcsh/bash vi-mode/zsh vi-mode）各小节文献 ［A］
- Christiansen 1995; GNU bash 文档； tcsh/zsh 发行说明 ［A］
