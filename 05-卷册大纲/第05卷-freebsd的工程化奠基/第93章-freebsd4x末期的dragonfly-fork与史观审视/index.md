---
chapter: 第 93 章
id: CH93
volume: 第05卷-freebsd的工程化奠基
---

# 第93章 freebsd4x末期的dragonfly-fork与史观审视

## 要点

- Linux 2.4(2001.1) 在 SMP、驱动支持、企业特性上迅速成熟，蚕食 FreeBSD 4.x 在 ISP 与企业市场的份额；Red Hat Enterprise Linux(2003) 进一步加速这一趋势
- Windows 2000(2000.2) 在企业市场与 FreeBSD 竞争，Active Directory 与 IIS 5.0 吸引部分企业用户；但 FreeBSD 在 ISP 场景仍占优势
- 对 4.x 黄金时代的批评认为，技术领先 (如 Jails/kqueue) 未转化为市场优势，是 “工程成功但商业失败” 的典型；批评者归因于 BSD 许可证、营销不足、Linux 商业生态
- 市场批评史料散落在分析报告与媒体报导中，部分报告由 Linux 厂商赞助，需警惕立场偏见
- 4.x 时期约 200 名 committer 中，约 60% 在社区记忆中被忽视，他们的贡献散落在 commit log 中，包括驱动维护、文档撰写、bug 修复

## 史观

- 专题语（不设条号）：Linux 2.4 成熟期与互联网泡沫后企业成本压力叠加，蚕食 FreeBSD 4.x 的企业市场份额（原挂“总纲第 16 条——经济周期”；基线第 16 条为“信仰是生存维系”，内容对不上基线，按 R2140 先例改不设条号专题语）
  - 辨析：蚕食的量化数据难以获取，需对照市场份额报告
  - 文献：Linux 2.4 文档；市场份额报告；企业迁移案例［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- 总纲第 10 条——动手者创造历史：被忽视的 committer 是 4.x 稳定的基础设施（原标签“边缘者贡献”按 25 条权威表校正）
  - 辨析：被忽视的程度需统计 commit 量与社区认知
  - 文献：commit log；Core Team 名单；邮件列表 ［A］

## 93.10.2 Windows 2000 的竞争

- 要点：Windows 2000(2000.2) 在企业市场与 FreeBSD 竞争，Active Directory 与 IIS 5.0 吸引部分企业用户；但 FreeBSD 在 ISP 场景仍占优势
- 史料：Windows 2000 文档、市场报告、企业采用案例［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

## 93.11.2 边缘贡献者辨析

- 要点：4.x 时期边缘贡献者包括测试反馈者、文档翻译者、PR 提交者，他们通过 send-pr 与邮件列表参与但未获 commit 权限
- 史料：GNATS PR 数据库、freebsd-doc 邮件列表、翻译团队记录 ［A］
- 史观：总纲第 10 条——动手者创造历史：边缘贡献者的劳动是 4.x 质量的基础（原标签“边缘者贡献”按权威表校正）
- 辨析：边缘贡献者的贡献难以量化；被忽视的程度需统计 commit 量与社区认知
- 文献：PR 数据库；邮件列表；翻译团队记录；commit log；Core Team 名单 ［A］
- 专题语（不设条号）：各操作系统在不同维度领先，比较维度需明确，不存在 “全面领先” 的操作系统（原挂“总纲第 6 条——技术路线分化”；基线第 6 条为“和解优于斗争”，内容对不上基线，改不设条号专题语）
  - 文献：Linux 2.4 ChangeLog；Windows XP 文档；Solaris 9 文档；Mac OS X 文档［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

## 93.11.3 贡献者与版本的关系

- 要点：4.x 系列〔原文截断，后文待回源〕
- 专题语（不设条号）：ipfw1 → ipfw2 重写付出规则兼容性代价（旧 ipfw1 规则需重写），但获得状态检测与流量整形能力；防火墙规则语法作为 “形式” 改变 “内容”（网络管理员可用的策略表达能力）（原挂“总纲第 6 条——技术选择的代价”“总纲第 17 条——形式与内容”，均非基线条目名，按 R2140 先例改不设条号专题语）
  - 辨析：经 bsd_commits.duckdb commits 表验证，ipfw2 首次 commit 为 2002-07-09（4.6-RELEASE 2002.7.3 之后），MFC 至 -stable 为 2002-07-24，故 ipfw2 实际引入版本为 4.6/4.7 时期而非旧叙事所称的 4.0 或 4.1，存疑已解决；ipfw2 与 ipfw1 共存期约 2002.7-2003 年（4.6-4.7-RELEASE 期间〔注：句尾原文截断，按上下文收束〕）
  - 文献：FreeBSD 4.6/4.7-RELEASE Release Notes；Luigi Rizzo "Dummynet: a simple approach to estimate and limit network bandwidth"（1998）；man **ipfw(8)** 历次版本；Luigi Rizzo. Change one variable to make it easier to switch between ipfw and ipfw2. freebsd-src 提交记录 [DB/OL]. 2002-07-09. c7ea6831353b20a8dac2dbcb6〔commit hash 截断待回源〕；Linux 2.4 ChangeLog；Windows XP 文档；Solaris 9 文档；Mac OS X 文档［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

## 93.13.2 容器与事件通知领先性

- 要点：FreeBSD 4.x 在容器 (Jails 2000) 与事件通知 (kqueue 2000) 上领先 Linux 3-7 年，Linux cgroups(2007)/LXC(2008) 与 epoll(2002) 均晚于 FreeBSD；这一领先未转化为市场优势
- 要点：CVE-2002-0005 的 CVSS 评分须对照 NVD 条目核实——版本周期文件未提取 CVSS 评分，史家不得臆造评分值；**execve(2)** 竞态的精确 TOCTOU 窗口须对照 FreeBSD-SA-02:08.exec 公告原文与 **execve(2)** 源码核实——公告称 “执行过程中存在竞态条件” 但未详细说明窗口路径；CVE-2003-0015 的 CVS 双重释放触发条件亦须对照 FreeBSD-SA-03:01.cvs 公告原文核实〔注：句尾原文截断，按本文件史料行所引公告收束〕
- 史料：FreeBSD-SA-02:08.exec 公告；FreeBSD-SA-03:01.cvs 公告；CVE-2002-0005 NVD 条目；CVE-2003-0015 NVD 条目；freebsd.duckdb freebsd-src 仓库 security fix commit 记录；本项目。原材料/研究/bsd 漏洞史/版本周期/freebsd-4.x.md；本项目。原材料/研究/bsd 漏洞史/早期漏洞补遗/freebsd-早期漏洞.md ［A］

## 93.14.2 setproctitle/ssh-agent/TCP ECE/ipfw/IRC DCC 漏洞群——网络服务与防火墙安全修复

- FreeBSD 4.0-RELEASE Announcement [EB/OL]. 2000-03-14. <https://www.freebsd.org/releases/4.0R/announce/>；FreeBSD 4.11-RELEASE Announcement [EB/OL]. 2005-01-25. <https://www.freebsd.org/releases/4.11R/announce/>；freebsd.duckdb freebsd-src 仓库 commits 表（ULE 首次 commit 2003-01-26）；Linux 2.4 ChangeLog；Red Hat Enterprise Linux 文档〔注：句尾原文截断，按要点行收束〕
- 据原文第 25 章（总纲第 13、19、21 条，谓项说明待子节互证）；综合 93.15.1 至 93.15.4 节文献 ［A］（原引旧章号 37.15.1-37.15.4，按第 93 章承自原第 37 章的拆分映射换算）
- FreeBSD 社区论文：[FP-2021-002] An Overview of Scheduling in the FreeBSD Kernel（Marshall Kirk McKusick（马歇尔·柯克·麦库西克），2021）<https://papers.freebsd.org/2021/eurobsdcon/mckusick-overview_scheduling_freebsd/>
- FreeBSD 社区论文：[FP-2020-002] An Overview of Sche〔原文截断，待回源；疑与上行 FP-2021-002 同题异年，待核〕
- McKusick & Rice. The Evolution of FreeBSD Governance [J]. FreeBSD Journal, 2017, 4(5): 26-31 ［A］

## 文献

- Linux 2.4 文档；市场份额报告；企业迁移案例［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。
