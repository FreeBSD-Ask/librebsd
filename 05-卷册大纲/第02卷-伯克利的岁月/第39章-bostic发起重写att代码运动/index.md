---
chapter: 第 39 章
id: CH39
volume: 第02卷-伯克利的岁月
---

# 第 39 章 bostic发起重写att代码运动

## 要点

- 重写运动的目标为：移除所有 AT&T 衍生代码，使 BSD 在 BSD 许可证下完全自由发布；策略为：逐文件核对版权、优先重写用户工具（法律风险低）、保留内核代码原貌（法律风险高）、社区志愿重写、CSRG 审查合并，1991 年 Net/2 实现目标
- Net/2 的历史意义：首个完全自由的 BSD 完整代码发布、为 386BSD（1992）与后续 FreeBSD/NetBSD（1993）提供基础、为 Linux 早期发展提供对比与刺激、触发 USL v. BSDi 诉讼（1992）、最终通过和解确认 BSD 完全自由地位
- 社区贡献者的历史意义：展示开源协作方法论在 1989-1991 年的可行性、为后续 FreeBSD/NetBSD 社区协作奠基、展示 BSD 社区的凝聚力、为 1998 年“开源”概念提供历史先例，社区贡献者集体劳动是 Net/2 成功的关键
- 法律风险预判的后续影响包括：1992-1994 年 USL 诉讼中 CSRG 文件保留政策提供关键证据、1994 年和解后 Net/2 法律地位确认、1994 年后 4.4BSD-Lite 完全自由发布、为后续 FreeBSD/NetBSD/OpenBSD 提供法律安全保障
- Net/2 发行渠道的历史意义包括：① **首次完全自由 BSD 完整代码的正式发行**——Net/2 是首个不含 AT&T 专有代码（除 6 个争议文件外）的 BSD 完整代码发行，标志着 BSD 从“AT&T 混合版权”向“完全自由 BSD 许可证”演化的关键节点；② **多渠道分发模式的奠基**——Net/2 通过 CSRG 直接销售、UUNET 匿名 FTP、386/BSD 自由再分发、B

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3712] 卷“第02卷-伯克利的岁月”第 39 章，匹配置信度 folder，原因：folder 第39章
- [DB:references_fulltext:chapter_matches:chmatch_3832] 卷“第02卷-伯克利的岁月”第 39 章，匹配置信度 folder，原因：folder 第39章
- [DB:references_fulltext:chapter_matches:chmatch_3880] 卷“第02卷-伯克利的岁月”第 39 章，匹配置信度 folder，原因：folder 第39章
- [DB:references_fulltext:chapter_matches:chmatch_3892] 卷“第02卷-伯克利的岁月”第 39 章，匹配置信度 folder，原因：folder 第39章
- [DB:references_fulltext:chapter_matches:chmatch_3957] 卷“第02卷-伯克利的岁月”第 39 章，匹配置信度 folder，原因：folder 第39章

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 重写策略的“优先用户工具”判断需核对，部分史料称优先重写网络代码，需核对 CSRG 内部备忘录
- Net/2 的“历史意义”叙述需避免事后进步史观，需核对 1991-1993 年 Net/2 的实际使用情况与影响
- 社区贡献者的“历史意义”叙述需避免事后进步史观，需核对 1989-1993 年社区贡献的实际影响
- 法律风险预判与 4.4BSD-Lite 发布的因果关系需谨慎判断，避免线性因果，USL 诉讼亦是关键因素
- Net/2 发行渠道的“历史意义”叙述需避免事后进步史观，需核对 1991-1993 年 Net/2 各渠道的实际使用情况与影响——UUNET 分发规模“以万计”来自 Bostic 宣誓书在 Justia 法院意见书中的引用，而 386/BSD 与 BSDi 的下游用户规模需核对各自发布记录；Net/2 发行渠道的“首次”地位需谨慎判断——Net/1（1989.6）已是首个自由 BSD 代码发行，

## 文献

- Bostic, K. (1991) "Net/2 Release Notes"；CSRG 法律评估文件（1990-1991）；McKusick, K. (1999) "Twenty Years of Berkeley Unix" ［B］
- Jolitz, B. (1991) "Porting UNIX to the 386"；FreeBSD/NetBSD Release Notes（1993）；McKusick, K. (1999) "Twenty Years of Berkeley Unix" ［B］
- Net/2 贡献者名单；Raymond, E. (1997) "The Cathedral and the Bazaar"；McKusick, K. (1999) "Twenty Years of Berkeley Unix" ［B］
- USL v. BSDi 案卷；Novell-UC Berkeley 和解协议（1994）；4.4BSD-Lite Release Notes（1994.6）[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- NEWREF:2527 --><!-- NEWREF:2528 --><!-- NEWREF:2529 --><!-- NEWREF:2530 --><!-- NEWREF:2531 --><!-- NEWREF:2532 --><!-- NEWREF:2533 --><!-- NEWREF:2534 --><!-- NEWREF:2535 --><!-- NEWREF:2536 --><!-- NEWREF:2537 --><!-- NEWREF:2538 -->
- McKusick, M. K. (1999) "Twenty Years of Berkeley Unix"；*Unix System Laboratories v. Berkeley Software*, 832 F. Supp. 790 (D.N.J. 1993)；TUHS Net2 目录归档（tuhs.org/Archive/Distributions/UCB/Net2/）；Jolitz, B. (1991) "Porting UNIX to the 386" ［B］
- CSRG 内部档案（伯克利 Bancroft 图书馆）；USL v. BSDi 案卷；1992-1994 年媒体报道集 ［C］[^doubt-resolved-230]: 据 Handbook (未署名) 消解<!-- NEWREF:2527 --><!-- NEWREF:2528 --><!-- NEWREF:2529 --><!-- NEWREF:2530 --><!-- NEWREF:2531 --><!-- NEWREF:2532 --><!-- NEWREF:2533 --><!-- NEWREF:2534 --><!-- NEWREF:2535 --><!-- NEWREF:2536 --><!-- NEWREF:2537 --><!-- NEWREF:2538 -->

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP273（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 文章追溯 cat 的源码史：Ken Thompson 与 Dennis Ritchie 于 1969 年在 PDP-7 上以汇编实现首版 cat，其中 getc 与 putc 的命名早于 C 标准库。（BSD Now EP273，[1440.78-1605.80]，L2）
- cat 的 C 实现迟至第七版 UNIX 才出现，4BSD 增加了一组沿用至今的命令行标志；最终由 Kevin Fall 在 1989 年为 Net/2 完成最后一次重写。（BSD Now EP273，[1651.48-1837.74]，L2）
- CSRG 将仍含 AT&T 代码的工具清单贴在墙上，供成员认领重写；Kevin Fall 认领 cat 与 mknod，其 1989 年版本成为 macOS 与 FreeBSD 现行 cat 的近源。（BSD Now EP273，[1800.70-1864.50]，L2）
- Xorg 服务器存在 CVE-2018-14665 提权漏洞，因命令行参数校验不当可覆盖任意文件；de Raadt 批评 X 维护者未提前告知 OpenBSD，致 6.4 发布即受波及。（BSD Now EP273，[2293.74-2489.74]，L2）

**史料**：

- 文章依赖 Unix History 仓库追踪 cat 自 1969 年以来的演进，并提及 macOS 10.0 从 NetBSD 引入 Kevin Fall 版 cat、10.5 起改用 FreeBSD 版 cat。（BSD Now EP273，[1459.66-2016.50]，L2）
- 提及 DistroWatch 的 NetBSD 8.0 评测：NetBSD 以高可移植性见长，文档分散于 FAQ、指南、手册页与 wiki，软件管理工具 pkg_add、pkgin、pkgsrc 并存易致新手困惑。（BSD Now EP273，[111.12-127.88]，L2）

**史观**：

- 总纲22 知识注定过时：cat 这种微小工具历经五十年、多次重写仍保持原始语义，说明计算机系统由层层叠叠的历史构件累积而成，而非不断推倒重建。（BSD Now EP273，[1369.22-1420.10]，L2）
- 总纲13 法律与道德是利益分配：为规避许可证而重写 cat 等基础工具，使“重写”成为法律边界塑造代码形态的例证，工具的功能未变而版权身份被替换。（BSD Now EP273，[1800.70-1853.22]，L2）

**辨析**：

- 文章称 cat 的首版 C 实现“迟至第七版 UNIX 才出现”与“4BSD 标志集 38 年未变”等细节系二手转述，须与 TUHS 归档的早期 cat 源码逐版核对。　[存疑脚注] 各版本 cat 的实现时间线未经一手源码逐版核验。（BSD Now EP273，[1651.48-1800.70]，L4）
- de Raadt 对 X 安全团队协调不力的批评属当事人立场，其“提前一小时才通知”的表述须与 X 安全团队与 OpenBSD 的往来记录交叉核实。　[存疑脚注] 披露时间线仅来自 OpenBSD 一方叙述。（BSD Now EP273，[2430.02-2489.74]，L4）

**文献**：

- [BSD Now EP273] Pennington J. BSD Now: Episode 273: A Thoughtful Episode | BSD Now 273[EB/OL]. (2018-11-23)[2026-08-15]. https://www.bsdnow.tv/273.

<!-- /PODCAST_REVIEW -->
