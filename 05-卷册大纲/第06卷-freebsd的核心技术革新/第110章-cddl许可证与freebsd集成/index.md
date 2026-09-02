---
chapter: 第 110 章
id: CH110
volume: 第06卷-freebsd的核心技术革新
---

# 第110章 cddl许可证与freebsd集成

# 第 110 章 cddl许可证与freebsd集成

## 要点

- CDDL 与 GPL 不兼容争议从 2005 年 CDDL 发布持续至今（2025 年），核心事件时间线为：2004 年 12 月 CDDL 提交 OSI；2005 年 1 月 OSI 批准 CDDL；2005 年 6 月 OpenSolaris 发布；2005 年 11 月 ZFS 源码发布；2006 年 FSF 在许可证列表中标注 CDDL 为 GPL 不兼容；2007-2008 年 Pawe
- OpenSolaris 时期（2005-2010 年）的 ZFS 一手史料面临严重的访问性问题：OpenSolaris 源码仓库（hg.opensolaris.org）于 2010 年 Oracle 收购后逐渐下线；Sun 官方文档站点（docs.sun.com）在 Oracle 收购后多次迁移，大量 ZFS 文档链接失效；OpenSolaris 邮件列表（opensolaris.org/os/c
- Dawidek 的 ZFS 移植工作主要在 <freebsd-current@freebsd.org> 和 <freebsd-arch@freebsd.org> 邮件列表上公开讨论，关键邮件包括：2006 年末 Dawidek 宣布启动 ZFS 移植的邮件；2007 年 4 月 ZFS 代码导入 Perforce 仓库的通知；2007 年 4 月 6 日 ZFS 主干导入 commit（经 bsd

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_543] 卷“第06卷-freebsd的核心技术革新”第 110 章，匹配置信度 0.6，原因：关键词重合 1 项
- [DB:bsdnow_podcast:outline_mappings:om_11222] BSD Now 第 562 期，匹配 CH110 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11357] BSD Now 第 546 期，匹配 CH110 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11944] BSD Now 第 474 期，匹配 CH110 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12219] BSD Now 第 445 期，匹配 CH110 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12237] BSD Now 第 444 期，匹配 CH110 章，关联度 1.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 需纠正一个常见误解：FreeBSD 之所以能集成 ZFS，并非因为 BSD 许可证 “比 GPL 更自由”，而是因为 BSD 许可证是 permissive（宽松许可）——它不对与之聚合分发的代码施加许可要求；GPL 是 copyleft 许可，要求衍生作品整体以 GPL 发布，因此与 CDDL 的文件级 copyleft 冲突；这不是 “自由程度” 的差异，而是 copyleft 边界设计的差异
- 原文 50.5 节标题写 “2007 年 ZFS 开源至 OpenSolaris” 有事实错误——ZFS 于 2005 年 11 月开源，OpenSolaris 本身于 2005 年 6 月发布，2007 年并非 ZFS 开源年份；Pawel Dawidek 的 FreeBSD ZFS 移植 commit hash 经 freebsd.db `commits` 表查询验证——FreeBSD src
- 经 freebsd.db `commits` 表与 `commit_files` 表交叉验证，Dawidek 的 ZFS 主干导入 commit 已确认为 `f0a75d274af375d15b97b830966b99a02b7db911`（author = committer = Pawel Jakub Dawidek，<pjd@FreeBSD.org>，author_date = commit

## 文献

- FreeBSD Project. *FreeBSD 7.0 Release Notes* (2008-02-27). freebsd.org; OpenZFS Project. *OpenZFS 2.0.0 Release Notes* (2020-11-30). github.com/openzfs/zfs/releases; Ubuntu Technical Board (2016-02). *Meeting Minutes*. lists.ubuntu.com; LWN.net. *ZFS Coverage Timeline*. lwn.net.[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- Internet Archive. *opensolaris.org Archive*. web.archive.org/web/*/<https://opensolaris.org>; illumos Project.* illumos-gate Repository *. github.com/illumos/illumos-gate; FreeBSD Project.* Vendor Import of OpenSolaris Code *. svn.freebsd.org/base/vendor/opensolaris/; genunix.org. * OpenSolaris Community Archive*. genunix.org; Dawidek P J. Please welcome ZFS - The last word in file systems. freebsd-src [DB/OL]. 2007-04-06T01:09:06Z. f0a75d274af375d15b97b830966b99a02b7db911. ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2005-2005 年间：42,570 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- FreeBSD Project. *Mailing List Archives*. lists.freebsd.org/pipermail/; FreeBSD Project. *Git Repository*. git.freebsd.org/src.git; Dawidek, P. J. (2007). *Porting ZFS to FreeBSD*. BSDCan 2007; FreeBSD Project. *Subversion to Git Migration Notes* (2020); Dawidek P J. Please welcome ZFS - The last word in file systems. freebsd-src [DB/OL]. 2007-04-06T01:09:06Z. f0a75d274af375d15b97b830966b99a02b7db911. ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSDTalk EP30（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 受访者转述 DTrace 的技术特性：可对系统中任意函数（库或可执行文件内）单独画像、聚合函数调用次数与耗时、语言支持线程局部存储以设条件变量；与 FreeBSD 的 ktrace、truss 等须持续读取内核内存并拖慢全局的工具不同，DTrace 关闭时零开销——它在内核中内置反汇编器、启用时改写指令、只影响被跟踪程序的运行性能；并转述 Bryan Cantrill 的演示：GNOME Terminal 打开一个新窗口竟发起约两千次系统调用。（BSDTalk EP30，[944.34-1076.12]，L1）
- 2006 年 BSD 阵营对脱离 GCC 的可能路径已有零星讨论：受访者借 OpenBSD 3.9 发布与 Theo 不妥协立场的调侃承认当下编译仍离不开 GPL 编译器这一妥协，随即列举替代选项——TinyCC、Intel C 编译器、以 MIT 许可开源的 Plan 9 C 编译器（Ken Thompson 作品，DragonFly 开发者一度关注但须改动内核以支持其目标格式）、以及在研的 TenDRA——结论是未来存在希望。（BSDTalk EP30，[1156.1-1245.58]，L1）
- LinuxWorld 2006 波士顿展会的 BSD 生态见闻：参观者普遍认知匮乏，有人径直询问“这是哪个版本的 Linux”，同时也有大量老用户与挑战者；BitDefender 起初称支持 OpenBSD 随即改口只有 FreeBSD；Coyote Point 为其网络负载均衡设备招募 FreeBSD 开发者；Cluster Resources 的开源自动部署软件希望支持 BSD；嵌入式方向对 NetBSD 兴趣可观。（BSDTalk EP30，[195.34-395.6]，L1）
- 受访者回忆在 Skycache（卫星 Usenet 服务商）的生产部署史：公司先以 NetBSD on SPARC 为上游，经由卫星每日吞吐约 250GB Usenet 流量，其后迁移到 Alpha DS10 上的 FreeBSD，原因是其 TCP 栈在当时表现卓越；受访者本人由此接触 BSD，并因转向安全领域而自然迁移至 OpenBSD。　[存疑脚注] 该段说话人因转写混叠难以确定归属 Dixon 或 O'Dell，公司部署事实本身为受访者一手自述（BSDTalk EP30，[778.04-815.88]，L1）

**史料**：

- Devon O'Dell 一手自述 DTrace 移植 FreeBSD 的缘起：2005 年 OSCON 上经 Santa Clara OpenSolaris 用户组结识的 Sun 内核工程师 Bryan Cantrill 与 Keith Wesolowski 午餐相劝，他先以移植步骤复杂为由拒绝，后于会后聚会上见到 DTrace 经 PHP 扩展挂钩 PHP 脚本、从函数调用一路追踪进内核再返回的演示，遂动心启动移植；此为 FreeBSD 集成 DTrace 之前最早的移植意向口述之一。（BSDTalk EP30，[851.38-920.82]，L1）
- Jason Dixon 一手自述 OSCON 演示与 Jordan Hubbard 轶事：其防火墙故障切换演讲配三台 Dell 与大屏液晶做 PF 加 CARP 拔线演示，观众惊讶、有风险投资人当场递名片，Astaro 等 iptables 方案因无对应故障切换能力无可竞争；交谈 CARP 与 PF 时发现听众多为 Jordan Hubbard 本人，后者透露 Apple 正尝试将 CARP 集成进 OS X，此后未见后续结果。　[存疑脚注] Apple 集成 CARP 一说系 Dixon 转述 Hubbard 口述，仅此一处，须与 Apple/FreeBSD 邮件档案交叉验证（BSDTalk EP30，[420.8-572.88]，L1）
- 主持人开场转述的新闻：FreeBSD 已与 Sun Microsystems 达成协议获准再分发 Java 1.5，此前用户须到 Sun 网站接受许可条款后另行下载安装，此后可如常规软件包一样直接安装，降低 FreeBSD 用户使用门槛。（BSDTalk EP30，[88.5-115.3]，L2）

**辨析**：

- 受访者对 CDDL 的专利条款作三层风险评估：顶层是两名贡献代码的开发者，中层是接受 CDDL 并对部分代码主张专利的厂商，底层是运行该厂商 OpenSolaris 的客户；一旦厂商起诉贡献者，贡献者有六十天通知期撤销其许可，厂商客户随即陷入危险；由此判断 CDDL 从 BSD 许可证立场并不友好，DTrace 不会进入 FreeBSD base 系统，只能作为后启用组件。　[存疑脚注] 对 CDDL 专利终止机制的六十天期限与后果系受访者口头解读，须对照 CDDL 原文条文核验（BSDTalk EP30，[1078.7-1156.1]，L1）

**文献**：

- [BSDTalk EP30] Backman W. BSDTalk: 30: bsdtalk030 - Interview with Devon O'Dell and Jason Dixon[EB/OL]. (2006-04-07)[2026-08-27]. https://archive.org/details/bsdtalk030.

<!-- /PODCAST_REVIEW -->
