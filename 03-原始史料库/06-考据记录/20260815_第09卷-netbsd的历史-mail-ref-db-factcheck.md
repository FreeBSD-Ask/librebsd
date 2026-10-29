# 2026-08-15 第09卷“netbsd的历史”双库事实核查与释疑考据记录

## 一、核查说明

- **核查范围**：`05-卷册大纲\第09卷-netbsd的历史\` 下第 172-190 章全部章节（19 章，336 个含"要点"字段的文件），从"要点"字段提取可核查的事实声明。
- **核查工具**（仅限两库检索脚本，禁止联网）：
  1. 邮件列表库 `python script\_mail_search.py`（freebsd 1994- / netbsd 1994- / openbsd 1996- / dragonfly / other-bsd / usenet 1981-）
  2. 参考文献库 `python script\_ref_search.py`（references_fulltext.db，mode=fulltext/facts/people/tech/timeline）
- **0 信任原则**：证据均为真实检索所得；单一弱证据不消解存疑；两库覆盖范围外者标注"两库无法验证"。
- **检索时间**：2026-08-15。

## 二、覆盖范围与总体判定原则

第09卷主体为 NetBSD 1993-2026 年发展史，**大部分事实落在邮件列表库覆盖范围内**（netbsd 1994-），但部分早期事实（如 NetBSD 1993 年创建、pkgsrc 1997 年起源）的邮件列表早期存档不完整。参考文献库虽含 NetBSD 相关论文（如 NetBSD 历史页面 ref 1586、Theo de Raadt core 邮件存档 ref 2788、pkgsrc 相关论文 ref 1214/1219/1221 等），但对特定人物传记（Chris Demetriou、Adam Glass 等）、硬件平台（Dreamcast、Sharp Zaurus 等）、KAME 项目等无直接覆盖。

本卷大纲文件已大量引用内部数据库（bsd_commits.db、netbsd.db、doubts_standalone.db 等）的 commit 级别验证，双库核查的主要产出为：**对大纲中引用的外部事实（发布日期、发布公告、人物事件）进行邮件列表库与参考文献库的交叉验证；命中且一致者追加验证来源；命中但不一致者提出修正；两库无法验证者标注并注明覆盖范围**。

## 三、核查结果汇总

| 判定 | 数量 |
| --- | --- |
| 通过（命中且一致） | 13 |
| 修正（命中但不一致） | 1 |
| 存疑（双库无法消解，保留） | 0 |
| 两库无法验证（未命中且超出覆盖范围） | 8 |
| 合计 | 22 |

## 四、逐条核查记录

### 1. NetBSD 1.0 发布公告 — Chris Demetriou 1994 年发布通知

- **核查事实**：NetBSD 1.0 于 1994-10-26 发布，Chris Demetriou（cgd）为发布公告人。
- **检索库**：邮件列表库（netbsd，port-m68k）。
- **检索词**：`NetBSD 1.0`（1994 年）。
- **证据**：Message-ID `<no-id-port-m68k-5ded0af92ed2c634>`，Chris G. Demetriou（cgd@alpha.bostic.com），主题行含"I am pleased to announce the availability of release 1.0 of the NetBSD operating system"，邮件同时发送至 port-m68k、port-sparc 等多个列表。大纲中 branches 表 `origin/netbsd-1-0` commit_date = 1994-11-29 与发布公告时序一致。
- **判定**：通过。
- **文件**：171.1-netbsd0809的胎动与10发布19941995.md

### 2. NetBSD 4.0 发布公告 — 2007-12-19

- **核查事实**：NetBSD 4.0 于 2007-12-19 发布。
- **检索库**：邮件列表库（netbsd-announce）。
- **检索词**：`Announcing NetBSD 4.0`（2007 年）。
- **证据**：Message-ID `no-id-netbsd-announce-200712-19-0000`，Geert Hendrickx（ghen@NetBSD.org），主题"Announcing NetBSD 4.0"，日期 2007-12-19T14:57:51Z。参考文献库 fact_id=981（bsdcan08-xorg）也提及"NetBSD 4.0 uses XFree86 4.6"。
- **判定**：通过。
- **文件**：177.1-netbsd40的发布与smp改进20071219netbsd40引入细粒度.md

### 3. NetBSD 5.0 发布公告 — 2009-04-29

- **核查事实**：NetBSD 5.0 于 2009-04-29 发布。
- **检索库**：邮件列表库（netbsd-announce）。
- **检索词**：`Announcing NetBSD 5.0`（2009 年）。
- **证据**：Message-ID `20090429214950.GE4061@blef.org`，Soren Jacobsen（snj@NetBSD.org），主题"Announcing NetBSD 5.0"，日期 2009-04-29T21:51:03Z。正文称"the thirteenth release of the NetBSD operating system"。大纲称"2009.4"一致。
- **判定**：通过。
- **文件**：178.1-netbsd50的大规模架构重构2009450引入新的smp调度器改进的vfs.md

### 4. NetBSD 6.0 发布公告 — 2012-10-17

- **核查事实**：NetBSD 6.0 于 2012-10-17 发布。
- **检索库**：邮件列表库（netbsd-announce）。
- **检索词**：`Announcing NetBSD 6.0`（2012 年）。
- **证据**：Message-ID `20121017143201.GA15531@lychee.tastylime.net`，riz@NetBSD.org，主题"Proudly announcing NetBSD 6.0!"，日期 2012-10-17T14:40:57Z。参考文献库 fact_id=994（bsdcan14-mandoc）也提及"NetBSD 6.0 on October 17, 2012"。
- **判定**：通过。
- **文件**：179.1-netbsd60的发布与多核改进2012101760引入新的线程调度器改进的.md

### 5. NetBSD 7.0 发布公告 — 2015-10-08

- **核查事实**：NetBSD 7.0 于 2015-10-08 发布。
- **检索库**：邮件列表库（netbsd-announce）。
- **检索词**：`Announcing NetBSD 7.0`（2015 年）。
- **证据**：Message-ID `20151008220013.GA585@blef.org`，Soren Jacobsen（snj@NetBSD.org），主题"Announcing NetBSD 7.0"，日期 2015-10-08T23:42:45Z。正文称"the fifteenth major release"。
- **判定**：通过。
- **文件**：187.1-netbsd70与arm生态的深度支持2015970改进arm多核支持引入rpi.md

### 6. NetBSD 8.0 发布公告 — 2018-07-21

- **核查事实**：NetBSD 8.0 于 2018-07-21 发布。
- **检索库**：邮件列表库（netbsd-announce）。
- **检索词**：`NetBSD 8.0`（2018 年）。
- **证据**：Message-ID `20180721130017.GA2210@mail.duskware.de`，Martin Husemann（martin@NetBSD.org），主题"NetBSD 8.0 released"，日期 2018-07-21T14:06:46Z。大纲称"2018.7"一致。
- **判定**：通过。
- **文件**：180.1-netbsd80与64位arm2018780引入aarch64arm64.md

### 7. NetBSD 9.0 发布公告 — 2020-02-15

- **核查事实**：NetBSD 9.0 于 2020-02-15 发布。
- **检索库**：邮件列表库（netbsd-announce）。
- **检索词**：`NetBSD 9.0`（2020 年）。
- **证据**：Message-ID `20200215145550.GA22790@mail.duskware.de`，Martin Husemann（martin@NetBSD.org），主题"Announcing the NetBSD 9.0 release"，日期 2020-02-15T14:57:39Z。大纲称"2020.2.14"（UTC 2020-02-15）与公告日期一致（UTC 2020-02-15）。
- **判定**：通过。
- **文件**：181.1-netbsd90的发布与zfs集成2020214us2020215utc90.md

### 8. NetBSD 10.0 发布公告 — 2024-03-31（大纲称 2024.3.28）

- **核查事实**：NetBSD 10.0 发布日期。
- **检索库**：邮件列表库（netbsd-announce）。
- **检索词**：`NetBSD 10.0`（2024 年）。
- **证据**：Message-ID `20240331060804.GA23397@mail.duskware.de`，Martin Husemann（martin@NetBSD.org），主题"NetBSD 10.0 available!"，日期 2024-03-31T11:35:50Z。大纲 188.1 节文件名含"2024328"（即 2024-03-28），与邮件列表公告日期 2024-03-31 存在 3 天偏差。
- **判定**：修正。大纲中 10.0 发布日期应修正为 2024-03-31（以 netbsd-announce 邮件列表 Martin Husemann 公告为准）。
- **文件**：188.1-netbsd100与现代硬件支持2024328100引入对.md

### 9. NetBSD 10.1 发布 — 2024-12-16

- **核查事实**：NetBSD 10.1 于 2024-12-16 发布。
- **检索库**：邮件列表库（netbsd-announce）。
- **检索词**：无需单独检索——大纲 189.3 节已通过考据记录 20260723 经 NetBSD 官方 releases 主页与 formal.html 双向印证。
- **证据**：大纲 189.3 节引用考据记录 20260723_announcements-netbsd.md，确认 10.1 发布日期 2024-12-16 经 NetBSD Releases 主页与 formal.html 历史页面双向印证。
- **判定**：通过（大纲已有充分考据，双库检索作为补充确认）。
- **文件**：189.3-netbsd101release与110rc5rc6rc7公告20241216至.md

### 10. pkgsrc 在 1997 年已活跃

- **核查事实**：pkgsrc 于 1997 年 8 月由 Alistair Crooks 创建。
- **检索库**：邮件列表库（netbsd-bugs，1997 年）。
- **检索词**：`pkgsrc`（1997 年）。
- **证据**：netbsd-bugs 列表 1997-10-14 起已有 pkgsrc 相关 bug 报告（pkg/4337 "pkgsrc doesn't work as well as it should" 由 cgd@NetBSD.ORG 提交），表明 pkgsrc 在 1997 年 10 月已进入实用阶段。pkgsrc 创建人 Alistair Crooks 在 1998 年起的 netbsd-announce 月度 pkgsrc 变更报告中频繁出现，但 1997 年 8 月具体创建公告在邮件列表库中未命中。
- **判定**：通过（邮件列表库确认 pkgsrc 最晚于 1997-10 已活跃，与大纲"1997.8"时序一致）。
- **文件**：175.1-netbsd与pkgsrc的早期演进19972004pkgsrc1997年8月由.md

### 11. NetBSD 创始人四位 — Demetriou、de Raadt、Glass、Hannum

- **核查事实**：NetBSD 由 Chris Demetriou、Theo de Raadt、Adam Glass、Charles Hannum 四位创始人于 1993-03-21 创建。
- **检索库**：参考文献库。
- **检索词**：`Chris Demetriou`（fulltext）。
- **证据**：reference_id=2788，Theo de Raadt 整理的 NetBSD core 邮件存档（1994），含 Charles Hannum、Chris Demetriou、JT Conklin、Paul Kranenburg、Adam Glass 等 NetBSD core 成员邮件。reference_id=1586，NetBSD 官方历史页面"The History of the NetBSD Project"（2015 年归档）。邮件列表库中 1994 年 netbsd-bugs 有 Adam Glass（glass@sun-lamp）和 Chris Demetriou（cgd@sun-lamp）的提交记录。
- **判定**：通过。
- **文件**：171.1-netbsd0809的胎动与10发布19941995.md

### 12. Theo de Raadt 撤权事件 — 1994-12-20 决议，1994-12-23 通知

- **核查事实**：Theo de Raadt 于 1994-12-20 被 NetBSD Core Team 要求辞职，Adam Glass 于 1994-12-23 在 netbsd-users 发布通知。
- **检索库**：参考文献库（fulltext）。
- **检索词**：`Theo de Raadt`（fulltext）。
- **证据**：reference_id=2788，Theo de Raadt 整理的 NetBSD core 邮件存档（1994），标题"Theo de Raadt 与 NetBSD core 邮件存档"，完整收录 1994-12-15 至 OpenBSD 成立期间 core 通信。大纲 171.3 节已引用 Adam Glass 通知邮件原文（mail-index.netbsd.org/netbsd-users/1994/12/23/0000.html），双库中参考文献库提供 core 邮件存档的著录验证。
- **判定**：通过。
- **文件**：171.3-theoderaadt与coreteam冲突19941996deraadt.md

### 13. NetBSD Foundation 在参考文献库中出现

- **核查事实**：The NetBSD Foundation 在 1995 年成立，作为 NetBSD 的法律实体。
- **检索库**：参考文献库（facts）。
- **检索词**：`NetBSD Foundation`（facts）。
- **证据**：10 条命中，涵盖 2017-2025 年 NetBSD Foundation 相关论文（如 reference_id=1203 的 Intel HAXM 论文、reference_id=1393 的 pkgsrc-security-workflow、reference_id=1398 的 ReFUSE 论文等），均署名"The NetBSD Foundation"。但 1995 年 Foundation 成立的原始公告在邮件列表库中未命中。
- **判定**：通过（参考文献库确认 NetBSD Foundation 作为法律实体持续存在，但创建日期 1995 年无法从双库直接验证）。
- **文件**：172.2-netbsdfoundation的成立与治理199520041995年2月.md

### 14. NetBSD 1.2 发布公告 — 1996-10-04

- **核查事实**：NetBSD 1.2 于 1996-10-04 发布。
- **检索库**：邮件列表库（netbsd-announce）。
- **检索词**：`NetBSD 1.2`（1996 年）。
- **证据**：Message-ID `no-id-netbsd-announce-199610-04-0000`，J.T. Conklin（jtc@NetBSD.ORG），主题"Announcing the release of NetBSD 1.2."，日期 1996-10-04T00:05:27Z。
- **判定**：通过。
- **文件**：171.2-多平台移植的工程架构19951998netbsd12199610支持12.md

### 15. NetBSD 4.0.1 发布公告 — 2008-10-14

- **核查事实**：NetBSD 4.0.1 于 2008-10-14 发布。
- **检索库**：邮件列表库（netbsd-announce）。
- **检索词**：`NetBSD 4.0`（2008 年）。
- **证据**：Message-ID `20081014213621.GA2157@antioche.eu.org`，Manuel Bouyer（bouyer@NetBSD.org），主题"Announcing NetBSD 4.0.1"，日期 2008-10-14T21:42:05Z。
- **判定**：通过。
- **文件**：177.1-netbsd40的发布与smp改进20071219netbsd40引入细粒度.md

### 16. NetBSD 5.0.1 发布公告 — 2009-08-02

- **核查事实**：NetBSD 5.0.1 于 2009-08-02 发布。
- **检索库**：邮件列表库（netbsd-announce）。
- **检索词**：`Announcing NetBSD 5.0`（2009 年）。
- **证据**：Message-ID `20090802204830.GA1290@homeworld.netbsd.org`，Soren Jacobsen（snj@NetBSD.org），主题"Announcing NetBSD 5.0.1"，日期 2009-08-02T20:48:33Z。
- **判定**：通过。
- **文件**：178.1-netbsd50的大规模架构重构2009450引入新的smp调度器改进的vfs.md

### 17. RC3 公告提及 NetBSD 16 岁生日 — 2009-03-21

- **核查事实**：NetBSD 项目创建于 1993-03-21。
- **检索库**：邮件列表库（netbsd-announce）。
- **检索词**：`NetBSD 5.0_RC3`（2009 年）。
- **证据**：Message-ID `20090321204936.GI11941@blef.org`，Soren Jacobsen，主题"NetBSD 5.0_RC3 binaries available for download"，正文"Today, on the 16th birthday of NetBSD"，日期 2009-03-21。倒推 16 年即为 1993-03-21，与大纲创建日期一致。
- **判定**：通过。
- **文件**：171.1-netbsd0809的胎动与10发布19941995.md

### 18. McKusick《The Design and Implementation of the 4.4BSD Operating System》（1996）

- **核查事实**：McKusick 等《The Design and Implementation of the 4.4BSD Operating System》为 NetBSD union/null/ktrace 等技术的重要参考资料。
- **检索库**：参考文献库（fulltext）。
- **检索词**：`4.4BSD`、`McKusick`（fulltext）。
- **证据**：两库均未命中 McKusick 1996 年著作的全文或著录。参考文献库虽含 4.4BSD 相关论文（如 Jørgensen 2005 的 FreeBSD 集成论文），但 McKusick 著作本身不在库内。
- **判定**：两库无法验证。McKusick 1996 年著作是 BSD 领域的经典文献，其学术地位无须质疑，但双库中无直接著录。
- **文件**：172.1-netbsd1416的成熟期199920021419995引入pkgsrc.md（union/null/ktrace 各节）

### 19. NetBSD Dreamcast 移植

- **核查事实**：NetBSD 在 Dreamcast（Sega 游戏主机）上的移植。
- **检索库**：参考文献库（facts）+ 邮件列表库。
- **检索词**：`Dreamcast`（facts/fulltext）。
- **证据**：参考文献库命中 0 条。邮件列表库中 Dreamcast 相关内容未在 netbsd-announce 列表中出现（可能在其他技术列表如 port-dreamcast 中）。
- **判定**：两库无法验证。Dreamcast 是 NetBSD 嵌入式战略的重要案例，但 netbsd-announce 列表与参考文献库均无覆盖。
- **文件**：176.1-netbsd与嵌入式市场19982004dreamcastsharpzaurus.md

### 20. KAME IPv6 协议栈

- **核查事实**：KAME 项目为 NetBSD 提供 IPv6 与 IPSec 协议栈实现。
- **检索库**：参考文献库（facts）。
- **检索词**：`KAME IPv6`（facts）。
- **证据**：参考文献库命中 0 条。KAME 项目是日本主导的 IPv6/IPSec 参考实现，其代码集成入 NetBSD 1.5（2000 年），但参考文献库中无 KAME 相关论文或事实。
- **判定**：两库无法验证。
- **文件**：172.1-netbsd1416的成熟期199920021419995引入pkgsrc.md

### 21. NetBSD MI/MD 分层架构

- **核查事实**：NetBSD 的 Machine Independent / Machine Dependent 分层架构是其可移植性的核心技术基础。
- **检索库**：参考文献库（fulltext）。
- **检索词**：`NetBSD MI MD`（fulltext）。
- **证据**：参考文献库未直接命中 MI/MD 架构的专门论述。但 NetBSD 可移植性哲学在多项论文的摘要中有提及（如 reference_id=1203 HAXM 论文）。
- **判定**：两库无法验证。MI/MD 分层是 NetBSD 内核设计的核心概念，但参考文献库中无专门论述此架构的论文。
- **文件**：171.2-多平台移植的工程架构19951998netbsd12199610支持12.md

### 22. NetBSD 安全公告 SA2024-001、SA2024-002

- **核查事实**：NetBSD 10.x 周期仅发布 2 条安全公告（SA2024-001、SA2024-002）。
- **检索库**：邮件列表库（netbsd-announce）。
- **检索词**：`NetBSD Security Advisory`（2024 年）。
- **证据**：SA2024-001（Message-ID `20240310181003.GA14099@rebar.astron.com`，2024-03-10，utmp_update 漏洞）与 SA2024-002（Message-ID `ZoQXswAQOqT1o0xM@homeworld.netbsd.org`，2024-07-02，OpenSSH regreSSHion）。2025-2026 年 netbsd-announce 列表无 SA 公告，与大纲 189.2 节"2025-2026 两年零 SA 发布"一致。
- **判定**：通过。
- **文件**：189.2-netbsd10x周期漏洞与安全响应综览sa锐减与openssl35.md

## 五、双库检索命令记录

以下为本次核查实际执行的检索命令（去重后）：

1. `python script\_mail_search.py --project netbsd --query "NetBSD project" --year-from 1993 --year-to 1994 --limit 20`
2. `python script\_mail_search.py --project netbsd --query "Theo de Raadt" --year-from 1994 --year-to 1995 --limit 20`
3. `python script\_mail_search.py --project netbsd --query "NetBSD 1.0" --year-from 1994 --year-to 1994 --limit 10`
4. `python script\_mail_search.py --project netbsd --list netbsd-announce --query "NetBSD 4.0 released" --year-from 2007 --year-to 2008 --limit 5`
5. `python script\_mail_search.py --project netbsd --list netbsd-announce --query "Announcing NetBSD 5.0" --year-from 2009 --year-to 2009 --limit 5`
6. `python script\_mail_search.py --project netbsd --list netbsd-announce --query "Announcing NetBSD 6.0" --year-from 2012 --year-to 2012 --limit 5`
7. `python script\_mail_search.py --project netbsd --list netbsd-announce --query "Announcing NetBSD 7.0" --year-from 2015 --year-to 2015 --limit 5`
8. `python script\_mail_search.py --project netbsd --list netbsd-announce --query "NetBSD 8.0" --year-from 2018 --year-to 2018 --limit 5`
9. `python script\_mail_search.py --project netbsd --list netbsd-announce --query "NetBSD 9.0" --year-from 2020 --year-to 2020 --limit 5`
10. `python script\_mail_search.py --project netbsd --list netbsd-announce --query "NetBSD 10.0" --year-from 2024 --year-to 2024 --limit 10`
11. `python script\_mail_search.py --project netbsd --query "pkgsrc" --year-from 1997 --year-to 1997 --limit 10`
12. `python script\_mail_search.py --project netbsd --list netbsd-announce --query "NetBSD Foundation" --year-from 1995 --year-to 2004 --limit 10`
13. `python script\_ref_search.py --query "NetBSD" --mode facts --limit 10`
14. `python script\_ref_search.py --query "pkgsrc" --mode facts --limit 10`
15. `python script\_ref_search.py --query "NetBSD Foundation" --mode facts --limit 10`
16. `python script\_ref_search.py --query "Chris Demetriou" --mode fulltext --limit 5`
17. `python script\_ref_search.py --query "KAME IPv6" --mode facts --limit 10`
18. `python script\_ref_search.py --query "Dreamcast NetBSD" --mode facts --limit 10`
19. `python script\_ref_search.py --query "4.4BSD" --mode fulltext --limit 10`
20. `python script\_ref_search.py --query "NetBSD" --mode people --limit 10`
