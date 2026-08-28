---
chapter: 第 307 章
id: CH307
volume: 第16卷-开源运动与合规治理
---

# 第 307 章 freebsd社区演进史-comitter留存

## 要点

- committer 活跃度统计可通过 src commit log 分析，但需区分“提交”与“审查”两种贡献
- FUSE 项目从 2012 年编程之夏引入到 2019 年更新的具体 commit 时间线需通过 src/sys/fs/fusefs 仓库 commit log 考据
- Bugzilla PR 统计是衡量外部贡献的重要依据，但需区分“提交 PR”与“合并入树”两种结果
- 企业赞助与基金会预算数据是评估 FreeBSD 商业生态的关键，需交叉验证
- 基金会年报与捐赠记录是评估资金结构的关键，需交叉验证

## 史料

- [DB:bsdnow_podcast:outline_mappings:om_10429] BSD Now 第 676 期，匹配 CH307 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10438] BSD Now 第 675 期，匹配 CH307 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10443] BSD Now 第 674 期，匹配 CH307 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10455] BSD Now 第 671 期，匹配 CH307 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10458] BSD Now 第 670 期，匹配 CH307 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10463] BSD Now 第 668 期，匹配 CH307 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10467] BSD Now 第 667 期，匹配 CH307 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10473] BSD Now 第 666 期，匹配 CH307 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10485] BSD Now 第 665 期，匹配 CH307 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10491] BSD Now 第 664 期，匹配 CH307 章，关联度 1.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- commit log 是否能完整反映贡献需评估；emeritus 状态的 committer 是否计入需明确
- 2012 年编程之夏 FUSE 项目的具体学生与导师需查编程之夏 archive；2019 年更新的具体 commit hash 需考据
- Bugzilla PR 是否完整保留需查；合并率统计方法需明确
- Foundation 990 表是否完整公开需查；企业赞助的具体金额需核实
- 考据过程留痕——【查证来源】外部批评来源包括 LKML Archive、Reddit r/freebsd 与 r/linux 讨论、freebsd-hackers 邮件列表争论串、Hacker News 评论等；社区回应包括 Core Team 公告、freebsd-announce 邮件列表声明、Foundation 年报中关于社区治理的章节；本次考据以 FreeBSD 官方页面（CoC、Cor

## 文献

- FreeBSD src commit log；Core Team Activity Reports ［A］
- 编程之夏 2012 FreeBSD Project Page；FreeBSD src/sys/fs/fusefs history[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- FreeBSD Bugzilla Statistics；freebsd-hackers 讨论 ［A］
- FreeBSD Foundation 990 Forms；freebsd-foundation 邮件列表 ［A］
- FreeBSD Foundation 990 Forms；Annual Reports 2014-2024[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- FreeBSD src/access 历史；Core Team Reports ［A］## 史料考据补充（2026-08-04 任务3 联网核验）> 主题：开源治理
- freebsd-hackers Archive；Majordomo Logs ［A］
- Core Team Meeting Minutes；freebsd-core Archive ［A］## 史料考据补充（2026-08-04 任务3 联网核验）> 主题：开源治理
- FreeBSD Security Advisories Archive；ERRATA Notices[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- FreeBSD doc Repository History；Handbook Archives ［B］## 史料考据补充（2026-08-04 任务3 联网核验）> 主题：开源治理

<!-- PODCAST_MINE v20260827 -->
<!-- 章节主题过滤：第307章-freebsd社区演进史-comitter留存 第 307 章 freebsd社区演进史-comitter留存（实体评分 ≥2 命中才入选） -->
<!-- 匹配期数：15 期，扫描 segments：13485 条 -->

### 要点（播客口述史提取）
- upgrading the craft referencing and search tools that are built into FreeBSD.（BSD Now EP1 @ 1858.719）
- The first problem with that is with the way FreeBSD Update works, you need a version（BSD Now EP2 @ 4003.22）
- So he switched over from Linux to FreeBSD and he writes about the 10 things he likes most now that he switched（BSD Now EP2 @ 5008.08）
- That's right, they can. So next we're looking at GCC is officially by-by on current, no longer being built by default on a freeBSD instrument.（BSD Now EP2 @ 543.86）
- their stable version of XORG. Apparently FreeBSD is working on some driver support issues first（BSD Now EP2 @ 761.14）

### 史料（播客当事人陈述）
- where they were talking about how FreeBSD was dying because they hadn't met their donation goal yet,（BSD Now EP1 @ 1178.880）
- Yeah, just about every GUI we have, there's some kind of shell or back end behind it that's just running standard FreeBSD commands.（BSD Now EP1 @ 1574.040）
- and actually just have them be put into as articles in not the handbook, but in the FreeBSD documentation tree.（BSD Now EP1 @ 1785.939）
- the FreeBSD documentation is mostly written in DocBook（BSD Now EP1 @ 1809.139）

### 史观（播客当事人观点与总纲映射）
- And I think it's actually, you know, it's very heartening that we started the FreeBSD project talking very much about the BSD license.（BSD Now EP14 @ 2209.619）
  → 史观映射：总纲10——动手者创造历史; 总纲13——法律与道德是利益分配
- I think I wrote one of the original, you know, about pages on the FreeBSD.org website that said, you know,（BSD Now EP14 @ 2220.339）
  → 史观映射：总纲10——动手者创造历史

### 辨析（播客争议与存疑点）
- [存疑脚注] Not TrueOS specifically. The stats come in, they look the same for both. So I just see it as FreeBSD（BSD Now EP6 @ 2498.63）
- [存疑脚注] otherwise there's performance problems. That's not true on FreeBSD. You can use a partition and（BSD Now EP15 @ 2889.639）

### 文献（播客参考条目）
- [BSD Now EP1] Pennington J. BSD Now: 1: BGP & BSD[EB/OL]. (2013-09-04)[2026-08-15]. https://www.bsdnow.tv/1.
- [BSD Now EP2] Pennington J. BSD Now: 2: Engineering and Powder Kegs[EB/OL]. (2013-09-11)[2026-08-15]. https://www.bsdnow.tv/2.
- [BSD Now EP3] Pennington J. BSD Now: 3: MX with TTX[EB/OL]. (2013-09-18)[2026-08-15]. https://www.bsdnow.tv/3.
- [BSD Now EP6] Pennington J. BSD Now: 6: Doing It de Raadt Way[EB/OL]. (2013-10-09)[2026-08-15]. https://www.bsdnow.tv/6.
- [BSD Now EP7] Pennington J. BSD Now: 7: Go Directly to Jail(8)[EB/OL]. (2013-10-16)[2026-08-15]. https://www.bsdnow.tv/7.
- [BSD Now EP9] Pennington J. BSD Now: 9: CURRENT Events[EB/OL]. (2013-10-30)[2026-08-15]. https://www.bsdnow.tv/9.
- [BSD Now EP10] Pennington J. BSD Now: 10: Year of the BSD Desktop[EB/OL]. (2013-11-06)[2026-08-15]. https://www.bsdnow.tv/10.
- [BSD Now EP11] Pennington J. BSD Now: 11: The Gateway Drug[EB/OL]. (2013-11-13)[2026-08-15]. https://www.bsdnow.tv/11.

<!-- /PODCAST_MINE -->
