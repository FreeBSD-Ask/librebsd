# 第 8 卷综述素材（T1 三源合一，2026-08-04 自动生成）

> 卷目录：第08卷-freebsd的范式转换｜章范围：ch155-ch170

## ① 现有研究（references_fulltext，39 条）

- [3] Unix浅说（David Fiedler，1984）
- [4] en（，1994）
- [5] Kernighan_Pike_UNIX_Programming_Environment_EN（，）
- [6] Kernighan_Ritchie_C_Programming_Language_EN（，）
- [7] 徐宝文_C程序设计语言（，）
- [8] Ritchie_C_Programming_Language（，）
- [9] UNIX_Network_Programming_Vol1_3rd（，）
- [203] Thompson-K-1978-UNIX-Implementation-Bell-System-Technical-Jo_v1（Thompson，1978）
- [250] Linux核心调度机制的实时性分析（黎宝华，1998）
- [263] 56（，）
- [276] UNIX环境下网络程序设计方法的分析和比较（李增智，1995）
- [279] UNIX服务器集中监控系统的设计与实现（李波，2013）
- [284] 基于LM3S8962的TCPIP协议栈的设计与实现（刘凯，2020）
- [299] 未知作者_Windows访问控制实施框架研究、设计与实现（，）
- [314] 基于ARM Cortex-M3_4指令集的新型嵌入式操作系统设计与实现（赵国飞，2022）
- [320] 69（，）
- [633] spinellis-unix_architecture_evolution-paper（fosdem，2018）
- [723] losh-hidden_early_history_of_unix-slides（fosdem，2020）
- [796] reading（Mead，1980）
- [803] reading（Leffler-et-al，1988）
- [804] the-design-and-implementation-of-the-4-3bsd-unix-operating（Leffler-et-al，1989）
- [810] a-quarter-century-of-unix-unix（Salus，1994）
- [838] daemon-gnu（Salus，2008）
- [839] reston-reed-media-services（Salus，2008）
- [873] bell-system-technical-journal（Thompson，1978）
- [874] communications-of-the-acm（Morris，1979）
- [878] The-Evolution-of-the-Unix-Time-sharing-System（Ritchie，1984）
- [881] proceedings-of-the-second-international-conference-on（Rashid-et-al，1987）
- [1160] Presotto_Thompson_Plan_9_Design（Pike，1990）
- [1163] Plan_9_from_Bell_Labs（Pike，1993）
- [1165] Presotto_Thompson_Plan_9_Programming_Environment（Pike，1995）
- [1205] RISC-V_ISA_Design_Philosophy（Waterman，2019）
- [1754] DTIC ADA240503（DTIC，）
- [1755] DTIC ADA240503（DTIC，）
- [1810] FreeBSD-Journal-MayJun-2022（FreeBSD-Journal-MayJun-2022，）
- [1811] FreeBSD-Journal-MayJun-2022（FreeBSD-Journal-MayJun-2022，）
- [1829] Image092317124900.facing text（Image092317124900.facing，）
- [1883] NASA NTRS Archive 19880009235（NASA，）
- [1981] designconsiderat00alle（designconsiderat00alle，）

## ② 研究缺口（doubts_to_resolve，61 条）

- id=555 [resolved] - 辨析：**需严格区分**：① 15.x 周期 freebsd-src 仓库中的 CVE commit 不等于 "15.x 特有漏洞"——许多 CVE 是上游
- id=556 [resolved] - 辨析：**需精确说明 -CURRENT 与 stable 的区别**：① -CURRENT（main 分支）是开发分支，无 ABI 稳定性保证，用户群体为开
- id=557 [resolved] - 辨析：**统计局限性标注**——(1) 统计显著 ≠ 实际显著：Mann-Kendall 趋势检验 p < 0.001 表明 freebsd-src com
- id=558 [resolved] - 辨析：考据过程留痕——【查证来源】(1) Linuxiac 2026-07-17 博文经 linuxiac.com 一手核验，确认 dialog 移除事件首
- id=559 [resolved] - 要点：GPL/GNU 阵营对 BSD 许可证纯洁化工程的批评可归纳为三点。**其一，法律必要性存疑**：GPLv2 允许与 BSD 许可证代码共存，dial
- id=560 [resolved] - 史观：总纲第 13 条——法律与道德是利益分配：GPL/GNU 阵营“法律必要性存疑”批评背后是 GPL 生态不被边缘化的利益诉求——dialog 移除不仅
- id=561 [resolved] - 辨析：考据过程留痕——【查证来源】(1) FreeBSD Licensing Policy 经 docs.freebsd.org/en/articles/l
- id=562 [resolved] - 辨析：考据过程留痕——【查证来源】(1) FreeBSD Licensing Policy 经 docs.freebsd.org/en/articles/l
- id=563 [resolved] - 辨析：考据过程留痕——【查证来源】(1) FreeBSD Foundation 2024 Annual Report 经 freebsdfoundation
- id=564 [resolved] - 辨析：考据过程留痕——【查证来源】(1) FreeBSD Ports 中 misc/dialog port 经 freshports.org/misc/di
- id=565 [resolved] - 要点：FreeBSD 16.0-CURRENT 将采用[考据完成：2026-07-28 经穷尽联网考据，该要点所引数据已交叉验证，部分精确数字须待原始档案公
- id=566 [resolved] - 辨析：地域仅以邮箱 ccTLD 作弱推断，个人/免费邮箱志愿者（2,070 次）地域难定，相关占比一律标 ［ 存疑脚注：此处事实待多源交叉验证 ］；绝不按姓
- id=567 [resolved] - 辨析：任何具体国别/族裔占比均不得外推为群体结论；非提交贡献者（文档、ports、翻译、漏洞上报者）的记录缺口标注 ［ 存疑脚注：此处事实待多源交叉验证 ］
- id=568 [resolved] - 文献：bsd_commits.db（freebsd-src）；0 信任原则方法论；FreeBSD 贡献者多样性研究（如有）［ 存疑脚注：此文献待 0 信任原
- id=569 [resolved] - 辨析：考据过程留痕——【查证来源】(1) 项目史观总纲第 13 条原文经 `原材料/哲学/一刻哲学/第25章.md` 第 17 行一手核验，原文表述“法律与
- id=570 [resolved] - 辨析：考据过程留痕——【查证来源】(1) 项目史观总纲第 11 条原文经 `原材料/哲学/一刻哲学/第25章.md` 第 15 行一手核验，原文表述与本章审
- id=571 [resolved] - 辨析：考据过程留痕——【查证来源】(1) 项目史观总纲第 19 条原文经 `原材料/哲学/一刻哲学/第25章.md` 第 23 行一手核验，原文表述与本章审
- id=572 [resolved] - 辨析：考据过程留痕——【查证来源】(1) 项目史观总纲第 23 条原文经 `原材料/哲学/一刻哲学/第25章.md` 第 27 行一手核验，原文表述与本章审
- id=573 [resolved] - 辨析：**统计局限性标注**——(1) 统计显著 ≠ 实际显著：Mann-Kendall 趋势检验 p < 0.001 表明 freebsd-src com
- id=574 [resolved] - 史料：FreeBSD Wiki GitTransition Src Schedule；freebsd-current 邮件列表 src 迁移公告；SVN r
- id=575 [resolved] - 辨析：考据过程留痕——【查证来源】(1) freebsd-announce 邮件列表 mailman 存档经 lists.freebsd.org/piper
- id=576 [resolved] - 辨析：部分争议点可能永远没有完全清晰的答案——例如 Core Team 内部讨论的细节、某些决策的真实考量、个别 committer 退役的真实原因等；史笔
- id=577 [unresolvable] - 66.6.4 贡献者考据与史料存疑
- id=578 [resolved] - 要点：Git 迁移贡献者考据的主要存疑事项：(1) **完整贡献者名单**——Git 工作组没有官方发布完整的“感谢名单”，部分贡献者（如早期测试者、文档编
- id=579 [resolved] - 史观：总纲第 3 条——形式主义膨胀：历史考据的边界就是史料的边界——对于没有可靠史料支撑的细节，史学家应当诚实地存疑，而不是用推测填补空白；不完整的真相好
- id=580 [resolved] - 辨析：存疑事项不是缺陷而是诚实的表现——历史书写不可能还原所有细节，承认未知比强行编造更符合学术规范；本章对关键日期、核心成员、主要事件的考据已有至少两个独
- id=581 [resolved] - 辨析：**统计局限性标注**——(1) 统计显著 ≠ 实际显著：Mann-Kendall 趋势检验 p < 0.001 表明 freebsd-src com
- id=582 [resolved] - 要点：经 McKusick 官方网站（mckusick.com/beastie/）一手资料交叉验证，BSD Daemon 的视觉演变精确史实如下：(1) *
- id=583 [resolved] | 1976 | 原始设计 | Phil Foglio（委托者 Mike O'Brien） | 手持三叉戟（象征 fork），站在管道上；报酬传说为开保险箱 ［
- id=584 [resolved] - 辨析：**关键日期精确考证（≥2 源交叉验证）**：① John Lasseter 绘制 BSD daemon 的年份——McKusick 版权声明明确写 
- id=585 [resolved] - 要点：FreeBSD 和 BSD 在影视作品中的出现案例经考据如下：(1) **《虎胆龙威》（Die Hard, 1988）与 "Nakatomi Socr
- id=586 [resolved] - 文献：FreeBSD stable/9 mailing list. (2013, September). Nakatomi Socrates easter 
- id=587 [resolved] - 辨析：**关键辨析点精确考证**：① **总纲第 6 条 "和解优于斗争" 的哲学内涵**——经查 c:\Users\ykla\Documents\hibs
- id=588 [resolved] - 辨析：地域仅以邮箱 ccTLD 作弱推断，个人/免费邮箱志愿者（3,801 次）地域难定，相关占比一律标 ［ 存疑脚注：此处事实待多源交叉验证 ］；绝不按姓
- id=589 [resolved] - 辨析：任何具体国别/族裔占比均不得外推为群体结论；非提交贡献者（文档、ports、翻译、漏洞上报者）的记录缺口标注 ［ 存疑脚注：此处事实待多源交叉验证 ］
- id=590 [resolved] - 文献：bsd_commits.db（freebsd-src）；0 信任原则方法论；FreeBSD 贡献者多样性研究（如有）［ 存疑脚注：此文献待 0 信任原
- id=591 [resolved] - 辨析：考据过程留痕——【查证来源】BSD daemon 1988 年 John Lasseter 绘制经 McKusick 官方网站 mckusick.co
- id=592 [resolved] - 辨析：16 条传言逐条考据最早可考源头、流传路径、考证结论、考证依据；考证结论分布为真伪混杂 7 条、史实属实 3 条、史实失实 4 条、无法确证 2 条；
- id=593 [resolved] Poettering 公告博客的精确发布日期存在考据存疑：任务描述与多源中文描述给出 2010-03-30，但 0pointer.de 博客页面 HTML 元数
- id=594 [resolved] Fedora 15 release 日期 2011-05-24 经 Fedora Project 官方与多源中文描述交叉印证；任务描述中“fedoraproje
- id=595 [resolved] RHEL 7 GA 日期 2014-06-10 经 Red Hat 官方与多源中文描述交叉印证；任务描述中“access.redhat.com 的 RHEL 7
- id=596 [resolved] openSUSE 12.2（2012）、Arch Linux（2012）采纳 systemd 经多源中文描述印证，一手 release notes 未抓取，加 
- id=597 [resolved] 拒绝 systemd 的发行版：Alpine Linux 长期坚持 musl libc + BusyBox + OpenRC 路线，与 systemd（依赖 g
- id=598 [resolved] Fedora 15、RHEL 7、openSUSE 12.2、Ubuntu 15.04、Arch Linux 的一手 release notes 均未在 202
- id=599 [resolved] Debian CTTE 投票证据链完整且经一手邮件列表存档印证，是本节史实最强部分。须注意“4:4 平局后 Bdale Garbee 投决定性票”的表述须以 `
- id=600 [resolved] Poettering 历年直接回应可考的有：2013 年《The Biggest Myths》博客（URL `https://0pointer.de/blog/
- id=601 [resolved] **[考据完成：2026-07-28 该处存疑标注属史料缺口，须待原始档案公开后方可补充确证] “Unix Monoculture”博客未能验证存在**：已尝试
- id=602 [resolved] **[考据完成：2026-07-28 该处存疑标注属史料缺口，须待原始档案公开后方可补充确证] FOSDEM 2017 Poettering 具体演讲页面未定位
- id=603 [resolved] **[考据完成：2026-07-28 该处存疑标注属史料缺口，须待原始档案公开后方可补充确证] Poettering 对 Devuan fork 回应原文未抓取
- id=604 [resolved] **[考据完成：2026-07-28 该处存疑标注属史料缺口，须待原始档案公开后方可补充确证]** “rcNG”是社区俗称，FreeBSD 5.0 releas
- id=605 [resolved] init 系统谱系呈现多元路径：大一统路径（systemd / macOS launchd / Solaris SMF）vs 极简路径（runit / s6）v
- id=606 [resolved] macOS launchd 一手来源：Apple Developer 官方文档 `https://developer.apple.com/library/arc
- id=607 [resolved] Solaris SMF 一手来源：**[考据完成：2026-07-28 该处存疑标注属史料缺口，须待原始档案公开后方可补充确证]** 尝试 URL `https
- id=608 [resolved] launchd 引入时间（2005 Mac OS X 10.4 Tiger）须以 Apple 文档为准——Apple Developer 文档 `develop
- id=609 [resolved] Solaris SMF 引入时间（2005 Solaris 10）须以 Oracle 文档为准——Oracle 文档站点 `docs.oracle.com/cd
- id=610 [resolved] [2] Oracle Corporation. Solaris 10 Service Management Facility Documentation [EB
- id=611 [resolved] - 辨析：**统计局限性标注**——(1) 统计显著 ≠ 实际显著：Mann-Kendall 趋势检验 p < 0.001 表明 freebsd-src com
- id=612 [resolved] [41] Oracle Corporation. Solaris 10 Service Management Facility Documentation [E
- id=613 [resolved] - 辨析：首任 Security Officer 的具体人选和上任时间存疑——早期资料中 Jordan Hubbard 曾负责安全相关事务，但正式 Securi
- id=614 [resolved] - 辨析：**统计局限性标注**——(1) 统计显著 ≠ 实际显著：Mann-Kendall 趋势检验 p < 0.001 表明 freebsd-src com
- id=615 [resolved] - 辨析：**统计局限性标注**——(1) 统计显著 ≠ 实际显著：Mann-Kendall 趋势检验 p < 0.001 表明 freebsd-src com

## ③ 一手史料（original_sources.kaoju_records，0 条）

（无）
