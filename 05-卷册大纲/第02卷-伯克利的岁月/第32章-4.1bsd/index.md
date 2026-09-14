---
chapter: 第 32 章
id: CH32
volume: 第02卷-伯克利的岁月
---

# 第 32 章 4.1BSD

## 要点

- 4.1BSD 命名妥协确立了 BSD 4.x 版本序列，延续至 4.4BSD-Lite，同时命名争议预示了后续 AT&T 与 BSD 的商标与版权冲突
- 4.1BSD 正式发布（1981 年 6 月）后存在多个 interim 测试磁带版本用于 4.2BSD 开发，各版本精确时间线经 McKusick 1999 当事人一手叙述确认：4.1a（1982 年 4 月，含 BBN TCP/IP 早期集成与 IPC 原型，供伯克利本地使用，盗版流传）、4.1b（1982 年 6 月，含 McKusick FFS 完整原型，仅伯克利少数开发机器运行）、4.1c（1983 年 4 月，4.2BSD 前最后一个 interim 测试版本）〔2026-09-12 整改：句尾截断按辨析字段考据（McKusick 1999 时间线）收束〕
- Coherent 是 Mark Williams Company 从零实现、与 UNIX 高度兼容的操作系统，先支持 PDP-11、后支持 Intel 386，作为商业克隆销售；它不与 AT&T 或 BSD 共享代码，却能提供近似 UNIX 的用户体验，反映了当时对平价 UNIX 类系统的真实需求。
- 4.1BSD（1981 年 6 月）继承 4BSD（1980 年 10 月）引入的 `setuid` 检查机制与 **chroot(2)** 系统调用[存疑脚注：经 FreeBSD 14.1 / OpenBSD / NetBSD chroot(2) man page HISTORY 交叉核验，chroot(2) 系统调用源自 V7 AT&T UNIX（1979），首次进入 BSD 家族系 4.2BSD]〔2026-09-12 整改：句尾截断补全并闭合存疑脚注括号〕
- 4.1BSD 版本碎片化导致用户困惑与 bug 报告困难，促使 CSRG 在 4.2BSD 后改进版本管理，最终引入 CVS 等正式版本控制工具

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3674] 卷“第02卷-伯克利的岁月”第 32 章，匹配置信度 folder，原因：folder 第32章
- [DB:references_fulltext:chapter_matches:chmatch_3714] 卷“第02卷-伯克利的岁月”第 32 章，匹配置信度 folder，原因：folder 第32章
- [DB:references_fulltext:chapter_matches:chmatch_3726] 卷“第02卷-伯克利的岁月”第 32 章，匹配置信度 folder，原因：folder 第32章
- [DB:references_fulltext:chapter_matches:chmatch_3728] 卷“第02卷-伯克利的岁月”第 32 章，匹配置信度 folder，原因：folder 第32章
- [DB:references_fulltext:chapter_matches:chmatch_3737] 卷“第02卷-伯克利的岁月”第 32 章，匹配置信度 folder，原因：folder 第32章
- [DB:references_fulltext:chapter_matches:chmatch_3740] 卷“第02卷-伯克利的岁月”第 32 章，匹配置信度 folder，原因：folder 第32章
- [DB:references_fulltext:chapter_matches:chmatch_3741] 卷“第02卷-伯克利的岁月”第 32 章，匹配置信度 folder，原因：folder 第32章
- [DB:references_fulltext:chapter_matches:chmatch_3742] 卷“第02卷-伯克利的岁月”第 32 章，匹配置信度 folder，原因：folder 第32章
- [DB:references_fulltext:chapter_matches:chmatch_3758] 卷“第02卷-伯克利的岁月”第 32 章，匹配置信度 folder，原因：folder 第32章
- [DB:references_fulltext:chapter_matches:chmatch_3760] 卷“第02卷-伯克利的岁月”第 32 章，匹配置信度 folder，原因：folder 第32章
- [DB:historical_claims:claim] 关键词行级挖掘素材线索 32.13-关键词行级挖掘素材线索（1 条，CL-RM 段，见 32.13-关键词行级挖掘素材线索.md）

## 史观

总纲第 3 条——不存在进步，只有权力再分配：4.1BSD 的命名妥协确立 4.x 版本序列，同时预示 AT&T 与 BSD 之间商标与版权话语权的首次再分配（据要点命名妥协条目）；总纲第 5 条——没有必然性，只有偶然性：4.1a/b/c 三个 interim 版本的碎片化系 4.2BSD 开发中 TCP/IP 集成与 FFS 原型推进的偶然节奏产物，碎片化倒逼 4.2BSD 后的版本管理改进（CVS 引入）属偶然积累的教训而非必然路线（据要点 interim 与版本管理条目）；总纲第 4 条——分离聚合是永恒规律：Coherent 等“无 AT&T 代码的干净实现”与 BSD/AT&T 谱系相分离，又在“UNIX 类使用体验”层面聚合，预示 Minix、Linux 的同类路线（据要点 Coherent 条目）。（2026-09-12 整改：史观字段按批次 B049 回填，映射依 25 条权威表；细节见子节文件史观/辨析字段）

## 辨析

- 先前版本时间线记载有误——4.1a 非 “1981 年中” 而为 1982 年 4 月，4.1b 非 “1981 年末 -1982 年初” 而为 1982 年 6 月，4.1c 非 “1982 年中 -1983 年初” 而为 1983 年 4 月，时间线已据 McKusick 1999 原文修正；4.1a/b/c 是 4.2BSD 的前置开发版本而非 4.1BSD 的 “碎片化补丁”，须严格区分（2026-09-12 整改：本行直引号改弯引号）
- Coherent 与 BSD 无代码渊源，不应混为一谈；其市场影响有限（主要面向教育/爱好者），但作为 “无 AT&T 代码的 UNIX 兼容系统” 具有象征意义，预示了后来 Minix、Linux 的 “干净实现” 路线。
- **史料**：CSRG 命名讨论邮件、AT&T 抗议信、伯克利-AT&T 通信档案 ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］（2026-09-12 整改：原“- 史料**：”畸形标记规范为“- **史料**：”）

**史观**：总纲第 13 条——法律与道德是利益分配：命名争议反映了 AT&T 对 UNIX 商标的法律意识与对 BSD 的竞争警惕——商标法律工具即利益分配工具（原挂“第 12 条法律结构”，基线第 12 条为“科学是形式主义”，按权威表改挂——2026-09-12 整改）

**辨析**：5BSD 命名计划的具体提出时间在不同史料中不一致，需核对 CSRG 内部记录

**文献**：McKusick, K. (1999)
（2026-09-12 整改：原 Diehr/State Street/Bilski/Alice 软件专利辨析块（含畸形标记“*关键辨析**”）与本章 4.1BSD 主题无涉，系软件专利主题章拼接残留（批次 B049 问题 4），整块移除留痕；同族文献条“8 份判决全文（ref 2593-2600）；Chisum”一并移除）
- 4.1BSD 约 400 份、4.2BSD 18 个月内超过 1000 份许可证，增长趋势明确

## 文献

- Salus, P. (1994) “A Quarter Century of UNIX”；USL v. BSDi 诉讼档案 ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- McKusick, K. (1999) “Twenty Years of Berkeley Unix”（当事人一手叙述，4.1a/4.1b/4.1c 精确月份、分发范围、Joy 离职交接）；4.1a/b/c 磁带存档；4.2BSD Release Notes (1983.8) ［A］；文献计量学分析.md Task 22（参考文献增长曲线与历史分期分布）；卷章数据映射.md 第二卷第 14 章映射条目；SQL 与 Python 查询清单.md Phase 6 文献计量学查询清单（2026-09-12 整改：行尾“---”残片删除）
- Mark Williams Co. Coherent User's Guide [Z]. 1983；Computer History Museum. Coherent artifacts [EB/OL]. ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- 4.1BSD Release Notes (1981.6)；4.4BSD SMM: 1《Installing and Operating 4.4BSD》；McKusick M K, Bostic K, Karels M J, Quarterman J S. The Design and Implementation of the 4.4BSD Operating System [M]. Reading: Addison-Wesley, 1996. ISBN 0-201-54979-4；Salus P H. A Quarter Century of UNIX [M]. Addison-Wesley, 1994. ISBN 0-201-54777-5 ［B］
- CSRG 邮件列表存档；4.2BSD Release Notes ［A］
- McKusick, K. (1999) “Twenty Years of Berkeley Unix”（当事人一手发行数据） ［B］
- McKusick, K. (1999) “Twenty Years of Berkeley Unix”（当事人一手完整列举 4BSD 特性清单）；4BSD Release Notes (1980.10) ［B］
- 4BSD Release Notes (1980.10)；4.1BSD Release Notes (1981.6)；TUHS Unix Tree 4BSD 条目（<https://www.tuhs.org/cgi-bin/utree.pl?file=4BSD>，CSRG Archives Kirk McKusick 捐赠）（2026-09-12 整改：URL 内全角逗号移出链接）
- McKusick, K. (1999) “Twenty Years of Berkeley Unix”（当事人一手完整列举 12 人委员会名单） ［B］
