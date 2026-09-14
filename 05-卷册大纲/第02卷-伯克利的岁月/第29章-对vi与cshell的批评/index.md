---
chapter: 第 29 章
id: CH29
volume: 第02卷-伯克利的岁月
---

# 第 29 章 对 vi 与 C Shell 的批评

## 要点

（2026-09-12 整改：原首条 Berknet 要点（Schmidt 1978 硕士论文、2BSD 分发，句尾并截断）经复核与本章“对 vi 与 C Shell 的批评”主题无关，系网络主题章误聚合（批次 B042 问题 5/6），整条移除留痕，随 2BSD 分发细节见网络主题对应章）
- **1979 年** 同期编辑器路径——vi（学术磁带分发，模态固定）、emacs（学术/MIT，Lisp 可扩展）、TECO EDT（MIT/商业，可编程）、VMS EDT（商业，keypad 全屏）展现编辑器设计的多元分化

| 编辑器 | 发布年份 | 作者/机构 | 范式 | 扩展性 | 分发渠道 |
| --- | --- | --- | --- | --- | --- |
| vi | 1978（2BSD） | Bill Joy（伯克利） | 模态固定 | 不可扩展 | 学术磁带邮寄 |
| emacs | 1976 | Stallman（MIT） | 无模态 | Emacs Lisp 无限可编程 | MIT AI Lab |
| TECO EDT | 1962/1978 | Dan Murphy（MIT）/ DEC | 可编程 | TECO 宏 | MIT/商业 |
| VMS EDT | 1977 | DEC | keypad 全屏 | 不可扩展 | DEC 商业销售 |
- 对 vi 与 csh 的批评部分存在形式主义倾向——以 “优雅” 或 “一致性” 等先验标准评判实践驱动的工具，忽视了工具的实践合理性
- vi 与 csh 的边缘贡献者史料散见于邮件列表、文档署名与会议记录，缺乏系统化档案，这是 BSD 史学研究的重要空白
- vi 与 csh 自 1978 年 2BSD 发布以来已延续 **47 年**（截至 2026 年），其影响力体现于三个层面——(1) 直接谱系延续：vi 谱系经 vim（1991）、elvis（1990）、nvi（1994）、Neovim（2015）持续演化，csh 谱系经 tcsh（1981）延续；(2) 功能扩散：vi 模态被 emacs（viper-mode/evil-mode）、VS Code（Vim 扩展）等编辑器吸纳〔2026-09-12 整改：句尾截断按批次 B042 指引补全〕

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3720] 卷“第02卷-伯克利的岁月”第 29 章，匹配置信度 folder，原因：folder 第29章
- [DB:references_fulltext:chapter_matches:chmatch_3735] 卷“第02卷-伯克利的岁月”第 29 章，匹配置信度 folder，原因：folder 第29章
- [DB:references_fulltext:chapter_matches:chmatch_3916] 卷“第02卷-伯克利的岁月”第 29 章，匹配置信度 folder，原因：folder 第29章
- [DB:references_fulltext:chapter_matches:chmatch_3930] 卷“第02卷-伯克利的岁月”第 29 章，匹配置信度 folder，原因：folder 第29章
- [DB:references_fulltext:chapter_matches:chmatch_3932] 卷“第02卷-伯克利的岁月”第 29 章，匹配置信度 folder，原因：folder 第29章
- [DB:references_fulltext:chapter_matches:chmatch_3938] 卷“第02卷-伯克利的岁月”第 29 章，匹配置信度 folder，原因：folder 第29章
- [DB:references_fulltext:chapter_matches:chmatch_4165] 卷“第02卷-伯克利的岁月”第 29 章，匹配置信度 1.0，原因：8 卷 PDF（合计约 100MB）；V7 时代 32V 手册，BSD 前身系统
- [DB:references_fulltext:chapter_matches:chmatch_1542] 卷“第02卷-伯克利的岁月”第 29 章，匹配置信度 0.9，原因：关键词搜索下载文献，标题含章节主题

（2026-09-12 整改注：上列 6 条“匹配置信度 folder”行系库侧匹配生成异常（"folder" 非数值，批次 B042 问题 9），待库侧提高阈值重跑；本组行仅作检索登记，不作证据采信依据）

## 史观

总纲第 15 条——文化即形式主义：以“优雅”“一致性”等先验美学标准评判 vi 与 csh 的批评，是 BSD 社区文化形式主义的典型运作——批评的对象（工具的实践合理性）被形式化的美学判据遮蔽（据要点“对 vi 与 csh 的批评部分存在形式主义倾向”）；总纲第 9 条——经验优先：vi 与 csh 自 1978 年 2BSD 发布延续 47 年（截至 2026 年）的生命力以实际使用经验为据，而非设计美学论证（据要点延续性条目）；总纲第 10 条——动手者创造历史：vi/csh 的边缘贡献者（脚本作者、终端适配者、vim/nvi 演化者）的劳动散见于邮件列表、文档署名与会议记录，须以多重史料交叉还原（据要点史料空白条目）；总纲第 5 条——没有必然性，只有偶然性：vim 取代 vi 成为事实标准、tcsh 延续 csh 谱系系偶然路径依赖，非“实践设计必然胜利”（据辨析自反性声明）。（2026-09-12 整改：史观字段按批次 B042 自 29.6-29.11 各节史观聚合回填，映射依 25 条权威表）

## 辨析

（2026-09-12 整改：原 Berknet/UUCP 辨析条（Nowitz 1978、4.3BSD 1986 等，句尾并截断于“Schmidt 后”）系网络主题误聚合内容（批次 B042 问题 6），移除留痕，相关辨析随网络主题章处置）
- 形式主义批评与非形式主义批评的边界需个案分析，避免将所有批评都归为形式主义
- [自反性声明] 本小节的 “跨时代评估” 本身即是一种事后建构——将 vi/csh 的持续使用追溯为 “实践设计的胜利” 是史家的叙事框架，而非历史参与者（Joy、Moolenaar、De Arruda 等）的自觉意图；按项目史观总纲第 5 章 5.3 节 “记忆将许多偶然性认识为一种必然性”，“vi 模态的持久生命力” 这一判断可能将偶然的路径依赖（vim 取代 vi 成为事实标准、VS Code Vim 扩展成为现代宿主）追认为必然〔2026-09-12 整改：句尾截断按上下文收束〕

## 文献

- Joy, W. (1978) “2BSD Release Notes”；McKusick, K. (1999) “Twenty Years of Berkeley Unix”（2026-09-12 整改：原行混入的 Berknet 硕士论文、sendmail 安装指南、RFC 821、UUCP 文档与文献计量学分析 Task 22 工作留痕（含本机绝对路径与 SQL 查询记录）经复核与本章主题无关（批次 B042 问题 6/9 同源），移除留痕）
- Raymond, E. S. (1996) “The Art of Unix Programming”；USENIX 1979 年会议论文集 ［B］
- Dewey, J. (1929) “Experience and Nature”；Rorty, R. (1979) “Philosophy and the Mirror of Nature”［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- USENIX Association 会议论文集（1978-1985）；伯克利 CSRG 邮件列表存档 ［A］
- 综合 11.8.1（Neovim/vim/elvis/nvi）、11.8.2（viper-mode/evil-mode/VS Code Vim/IdeaVim）、11.8.3（tcsh/bash vi-mode/zsh vi-mode）各小节文献 ［A］
- Christiansen 1995; GNU bash 文档； tcsh/zsh 发行说明 ［A］

<!-- dangan-20260908 消解回写 -->
- Neovim. GitHub 仓库 v0.1.0 Release（<https://github.com/neovim/neovim/releases/tag/v0.1.0>，2015-11-01）[EB/OL]. 2015. ［DKC-1154→fulltext:5820］
- GNU. Viper[EB/OL]. 无年份. ［DKC-1157→fulltext:5821］
<!-- /dangan-20260908 -->
