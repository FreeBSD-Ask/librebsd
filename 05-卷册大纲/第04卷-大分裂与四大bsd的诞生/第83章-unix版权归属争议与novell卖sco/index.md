---
chapter: 第 83 章
id: CH83
volume: 第04卷-大分裂与四大bsd的诞生
---

# 第83章 unix版权归属争议与novell卖sco

## 要点

- **1994 年** Windows NT 3.5 发布，定位企业市场，支持 x86、MIPS、Alpha、PowerPC 多架构，提供 Win32 API；与 4.4BSD-Lite 相比，NT 3.5 商业支持完善但开源程度为零，技术架构（微内核 vs 宏内核）与许可模式（专有 vs 开源）形成鲜明对比
- 1994 年 SunOS 5.4 (Solaris 2.4) 发布，基于 SVR4，支持 SPARC 与 x86，提供与企业 Unix 兼容的 ABI；与 4.4BSD-Lite 相比，Solaris 2.4 是商业 UNIX 的延续，BSD 与 SVR4 的分野在 1994 年已基本定型
- 1994 年 IBM OS/2 Warp 3.0 发布，定位桌面与小型企业市场，提供 32 位抢占式多任务；与 4.4BSD-Lite 相比，OS/2 Warp 定位桌面市场，4.4BSD-Lite 定位服务器市场，两者市场定位不同但都面临 Windows 95 的竞争压力
- 4.4BSD-Lite 与 Windows NT 3.5、Solaris 2.4、IBM OS/2 Warp 的比较辨析须区分 “技术架构”（微内核 vs 宏内核、SVR4 vs BSD、32 位抢占式多任务 vs 分时多任务）与 “市场定位”（企业 vs SPARC 工作站 vs 桌面 vs 服务器）——前者可技术对比，后者经各操作系统的发布档案与第三方市场份额统计（IDC、Gartner）场景化评估；单一维度的决定论（如仅以许可模式判断胜负）经 Windows NT 3.5 商业市场胜出但开源生态影响为零、4.4BSD-Lite 商业市场份额有限但开源生态影响深远的对照可证伪
- **1994 年 6 月** 4.4BSD-Lite 发布后，FreeBSD 2.0（**1994 年 11 月 22 日** 网络发布）与 NetBSD 1.0（**1994 年 10 月 26 日** release tag）均 rebase 至 4.4BSD-Lite，4.4BSD-Lite 取代 386BSD 成为 FreeBSD 与 NetBSD 的共同直接安全基线；FreeBSD 1.x（**1993-1995**）与 NetBSD 0.8/0.9（**1993**）先前直接基于 386BSD 0.1（**1992-07**）+ patch kit，其安全基线为 4.3BSD-Reno 安全机制在 80386 平台的移植——root/超级用户二元特权模型、文件权限 rwx、setuid/setgid、DES **crypt(3)** 密码散列、单文件 `/etc/passwd`、4.3BSD 网络栈远程漏洞面；4.4BSD-Lite rebase 后这一 386BSD 安全基线被 4.4BSD-Lite 的安全机制取代，386BSD 作为 FreeBSD 与 NetBSD 直接安全基线的历史地位在 **1994 年下半年** 终结；OpenBSD 项目于 **1995 年 10 月 18 日** 自 NetBSD 1.0 分叉（首个发行版 1.2 于 1996 年 7 月发布），经 NetBSD 1.0 间接继承 4.4BSD-Lite 新基线，386BSD 作为 OpenBSD 直接基线的地位更早在 **1994 年 10 月** NetBSD 1.0 rebase 时即被取代〔注：原“OpenBSD 1.0（1995.10.18 fork）”表述经核查报告核验改正——OpenBSD 无 1.0 发布版，1995 年 10 月系分叉时点；原稿两处悬空引导句“对照如下：”“时间线如下：”其后并无表格，已删〕

## 史料

- 本章章级史料著录暂缺：原自动匹配的数据库锚点原因字段指向“folder 第68章”，与本章第 70→83 章重排不符，属匹配元数据错配〔存疑脚注：待重跑 chapter_matches 匹配逻辑后回填〕；章级史料清单待依 83.8-83.11 各节史料字段按 GB/T 7714 复核回填

## 史观

- 总纲第 3 条——不存在进步，只有权力再分配：NT 的微内核架构与 4.4BSD-Lite 的宏内核架构反映不同的技术政治选择；比较须区分 “市场份额” 与 “技术影响” 两维度，结论可以相反（据 70.4、83.10 先例）
- 专题语（不设条号，考据方法：0 信任原则）：比较辨析须对照各操作系统的发布档案（Windows NT 3.5 1994 微软公告、Solaris 2.4 1994 Sun 公告、OS/2 Warp 3.0 1994 IBM 公告、4.4BSD-Lite Release Notes 1994.6）与第三方市场份额统计交叉验证，市场份额数据须采信 IDC、Gartner 等权威机构报告而非厂商自述
- 总纲第 4 条——分离聚合是永恒规律：4.4BSD-Lite 取代 386BSD 是 BSD 安全基线从 386BSD 聚合至 4.4BSD-Lite 的关键转型；终结中的延续：386BSD 作为 FreeBSD 与 NetBSD 直接安全基线的历史地位终结，但其经 386BSD 0.1 → FreeBSD 1.0/NetBSD 0.8 路径传递的安全基因在两大 fork 主线延续
- 总纲第 13 条——法律与道德是利益分配：APA 作为法律结构直接塑造 BSD 后续法律环境，模糊条款埋下诉讼伏笔；APA 的具体条款在不同叙事中差异较大——部分称 Novell 保留版权，部分称版权转移给 SCO；经 APA Schedule 1.1(a) 原文与 Amendment No. 2（1996.10.16）核实，APA Schedule 1.1(a) 列出 “版权” 作为转移资产，但 Amendment No. 2 约定 Novell 保留版权（该约定的解释于 2003-2010 年诉讼中成为争点，终经法院裁决确认 Novell 保留），SCO 仅获得授权销售权
- 总纲第 13 条——法律与道德是利益分配（许可证维度）：BSD 许可证在 4.4BSD → 4.4BSD-Lite 演化中起决定性作用，4.4BSD-Lite 完全自由许可证使 BSD 消除法律风险；专题语（不设条号）：4.4BSD-Encumbered 的混合版权模式在诉讼后被放弃、4.4BSD-Lite 以法律洁净为目标，属许可证路径的代价取舍（原挂“第 24 条许可证”“第 6 条技术选择的代价”均非基线条目名，按权威表改写）
- 专题语（不设条号）：本章比较框架（基础设施持久性、生活直接影响、代码直接派生三维度）本身是人为建构的评价体系，须自反呈现（原挂“第 7 条理论必须自反”经核与本条主题语相符，保留于总纲第 7 条映射）〔总纲第 7 条——理论必须自反：本章比较框架本身是人为建构的评价体系（据 70.8）〕

## 辨析

- NT 3.5 与 4.4BSD-Lite 的比较须区分 “市场份额”（NT 3.5 经微软企业销售渠道在商业市场胜出）与 “技术影响”（4.4BSD-Lite 经 FreeBSD 2.0 1994.11.22、NetBSD 1.0 1994.10.26、OpenBSD 1995.10 fork 在开源生态影响深远）；技术影响的多维评估经 freebsd/netbsd/openbsd 各自项目库的首条 commit 与发布记录交叉验证
- 比较的解释力存在边界——部分学者过于强调单一维度（如许可模式），架构（微内核 vs 宏内核）、市场（企业 vs 桌面 vs 服务器）、生态（商业支持 vs 开源社区）多维因素须综合评估——Windows NT 3.5 在商业市场胜出但开源生态影响为零，4.4BSD-Lite 在商业市场份额有限但开源生态影响深远，二者经不同维度评估结论不同
- 4.4BSD-Lite 取代 386BSD 作为直接安全基线的时间点须严格区分——NetBSD 1.0（1994.10.26）与 FreeBSD 2.0（1994.11.22）几乎同期 rebase 至 4.4BSD-Lite，二者间隔不足一个月，386BSD 作为直接安全基线的地位在 1994 年下半年被 4.4BSD-Lite 几乎同时取代；【0 信任原则·release tag 验证局限】CVS-to-Git 转换可能重写 commit 日期，release tag 时间须与邮件列表存档交叉验证
- APA 的具体条款在不同叙事中差异较大——部分称 Novell 保留版权，部分称版权转移给 SCO；经 APA Schedule 1.1(a) 原文与 Amendment No. 2（1996.10.16）核实，APA Schedule 1.1(a) 列出 “版权” 作为转移资产，但 Amendment No. 2 约定 Novell 保留版权（该约定的解释于 2003-2010 年诉讼中成为争点，终经法院裁决确认 Novell 保留），SCO 仅获得授权销售权
- 4.4BSD-Encumbered 与 4.4BSD-Lite 的关系需严格区分——前者需 AT&T 源代码许可证，后者完全自由；争议文件数量需准确：“32 个争议文件” 说法无一手来源支持，McKusick 明确记载仅 3 个文件被完全删除、约 70 个文件添加 USL 版权声明（仍可自由再分发）；“4.4BSD（1993.11）” 正式发布日期〔考据注：2026-08-17 联网考据中断于此，待回源〕

## 文献

- FreeBSD 2.0 Release Announcement 1994.11.22；NetBSD 1.0 Release Announcement 1994.10.26；4.4BSD-Lite Release Notes 1994.6；USL v. BSDi 和解协议 1994.1；**freebsd.duckdb** `tags` 表（release/2.0_cvs）与 `commits` 表（4.4BSD-Lite 导入 commit `59deaec541ae8baaa58daf6c5a2196ea7de180c3`） ［A］
- Novell-SCO APA 原文；UNIX 版权归属史研究；McKusick M K. Twenty Years of Berkeley Unix [M]//Open Sources, 1999；4.4BSD-Lite/Lite2 Release Notes；USL v. BSDi 和解协议 1994.1；FreeBSD 2.0/NetBSD 1.0 Release Announcements ［B］
- Mike Karels 告别邮件；Bancroft CU-551 全宗；McKusick CD-ROM 套装；SCCS/CVS/SVN/Git 文档；CSRG Archive CD-ROM #4；FreeBSD/NetBSD/OpenBSD CVS 仓库档案；**cvsup** 发布记录；FreeBSD SVN/Git 迁移公告 ［A］
- FreeBSD 社区论文：[FP-2021-002] An Overview of Scheduling in the FreeBSD Kernel（Marshall Kirk McKusick（马歇尔·柯克·麦库西克），2021）<https://papers.freebsd.org/2021/eurobsdcon/mckusick-overview_scheduling_freebsd/>〔注：原混入本文件的调度论文与本章主题弱关联，保留登记待归属核验〕

## 史观映射

> 本章体现项目统摄史观中“没有必然性，只有偶然性”与“分离聚合是永恒规律”的双重运作——de Raadt 被 NetBSD Core Team 逐出是具体的个人决定，但直接催生 OpenBSD 这一 BSD 家族的安全堡垒；fork 是“分离”的极端形式，但分离后的“聚合”（加密代码集成、代码审计文化建立）才是 OpenBSD 真正的创造性贡献；“安全至上”作为差异化定位是“技术选择即政治选择”的典型——de Raadt 选择安全而非可移植性或性能，这一选择反映了 OpenBSD 对 BSD 哲学的不同理解；Core Team 的驱逐决议则体现了“组织结构塑造技术路径”——NetBSD 的精英决策结构直接改变了 BSD 家族的格局

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP51（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Eric LeBlanc 自述 Xinuos 在约十八个月调研后选择 FreeBSD 作为新增支持的开源操作系统，理由包括与 OpenServer 相近的代码树、BSD 许可证及 FreeBSD Foundation 的存在。（BSD Now EP51，[1014.92-1082.10]，L1）
- Xinuos 以 BSD 许可证允许转售商与客户开发专有环境为关键考量，并计划对 FreeBSD 稳定分支提供最长十五年的支持与回溯移植。（BSD Now EP51，[1163.86-1335.46]，L1）
- Xinuos 计划将 OpenServer 与 UnixWare 等遗留应用运行于 bhyve 虚拟化之上，以迁移无源码的旧应用。（BSD Now EP51，[1465.72-1508.64]，L1）

**史料**：

- Eric LeBlanc 访谈（Xinuos 董事长兼 CEO 当事人自述）。（BSD Now EP51，[992.22-1870.22]，L1）

**史观**：

- 总纲13 法律与道德是利益分配：Xinuos 选择 BSD 许可证的本质是转售商与专有业务利益的分配安排。（BSD Now EP51，[1163.86-1179.76]，L1）
- 总纲3 不存在进步，只有权力再分配：Xinuos 由专有 System V 转向参与 FreeBSD，是商业权力格局的再分配而非线性技术进步。（BSD Now EP51，[1014.92-1128.06]，L1）
- 总纲11 商品是形式主义：访谈将操作系统视为可支持、可转售的商品，并以支持周期与许可证作为商品属性展开叙述。（BSD Now EP51，[1322.60-1363.72]，L1）

**辨析**：

- Xinuos 与 SCO 的历史关联及其 UNIX 版权诉讼前史在本期仅被一带而过，其与 FreeBSD 关系的长期后果未在本期展开。　[存疑脚注] SCO 前史仅凭主持人转述与当事人简短开场，未经多源交叉核验（BSD Now EP51，[1015.90-1019.40]，L4）

**文献**：

- [BSD Now EP51] Pennington J. BSD Now: 51: Engineering Nginx[EB/OL]. (2014-08-20)[2026-08-15]. <https://www.bsdnow.tv/51>.

<!-- /PODCAST_REVIEW -->
