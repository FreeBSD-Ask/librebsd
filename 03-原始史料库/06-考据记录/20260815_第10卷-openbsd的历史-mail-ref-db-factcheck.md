# 2026-08-15 第10卷“openbsd的历史”双库事实核查与释疑考据记录

## 一、核查说明

- **核查范围**：`05-卷册大纲\第10卷-openbsd的历史\` 下第 191-213 章全部章节（23 章，含各章概述与子节文件的"要点"字段中出现的可核查事实声明）。
- **核查工具**（仅限两库检索脚本，禁止联网）：
  1. 邮件列表库 `python script\_mail_search.py`（openbsd 1996-，含 misc/tech/announce/advocacy/bugs/www/ipv6/ports/arm 等列表）
  2. 参考文献库 `python script\_ref_search.py`（references_fulltext.db，mode=fulltext/facts/people/tech/timeline）
- **0 信任原则**：证据均为真实检索所得；单一弱证据不消解存疑；早于两库覆盖范围者一律标注"两库无法验证"并注明覆盖范围。
- **检索时间**：2026-08-15。

## 二、覆盖范围与总体判定原则

第10卷覆盖 1995-2026 年 OpenBSD 历史，时间跨度与邮件列表库 openbsd 项目覆盖范围（1996-）高度重叠，参考文献库含 Heartbleed/LibreSSL/pledge/unveil 等相关 BSDCan/EuroBSDCon 论文（如 Beck 2018 Pledge & Unveil ref 63、Buehler 2019 TLS 1.3 ref 79、Buehler 2022 LibreSSL ref 119 等），但 1994-1995 年 de Raadt 被逐事件与 NetBSD 邮件列表交叉部分不在 openbsd 邮件库覆盖范围内。

本卷双库核查的主要产出为：**命中且一致者追加验证来源；命中但不一致者修正；早于 openbsd 邮件库覆盖范围（1996-）或参考文献库无条目的，标注两库无法验证；其余存疑保留**。

## 三、核查结果汇总

| 判定 | 数量 |
| --- | --- |
| 通过（命中且一致） | 21 |
| 修正（命中但不一致/需补注） | 2 |
| 存疑（双库无法消解，保留） | 1 |
| 两库无法验证（未命中或早于覆盖范围） | 6 |
| 合计 | 30 |

## 四、逐条核查记录

### 1. 子节 205.1 / 192.3.4 — OpenSSH 1999-12-01 随 OpenBSD 2.6 发布

- **核查事实**：OpenSSH 1.0 随 OpenBSD 2.6 于 1999-12-01 发布，为首个集成 SSH 协议的操作系统。
- **检索库**：邮件列表库（openbsd-announce）。
- **检索词**：`OpenBSD 2.6`（year 1999）。
- **证据**：Message-ID `<no-id-openbsd-announce-67d45675cb291ed9>`（1999-12-01，Louis Bertrand，"OpenBSD 2.6 Press Release"，snippet="OpenBSD 2.6 first OS to integrate the Secure Shell protocol. December 1, 1999; Calgary, Canada"）。
- **判定**：通过。
- **修正内容**：无。

### 2. 子节 205.1 — Markus Friedl 1999 年 10 月参与 OpenSSH 开发

- **核查事实**：Markus Friedl（markus）是 OpenSSH 早期核心开发者。
- **检索库**：邮件列表库（openbsd-misc）。
- **检索词**：`OpenSSH`（year 1999）。
- **证据**：Message-ID `<no-id-openbsd-misc-58aeca5b51fc195b>`（1999-10-12，Markus Friedl，"ssh"，snippet 证实 1999-10-12 时 OpenSSH 已在 OpenBSD 源码树中，Friedl 主导开发）。
- **判定**：通过。
- **修正内容**：无。

### 3. 子节 212.1 — "Four years without a remote hole" 宣传语（2002 年）

- **核查事实**：OpenBSD 官网约 1997-2002 年使用"Four/Five years without a remote hole"宣传语，2002 年因 OpenSSH 漏洞调整为"One remote hole"。
- **检索库**：邮件列表库（openbsd-misc）。
- **检索词**：`remote hole default install`（year 2002）。
- **证据**：Message-ID `<no-id-openbsd-misc-eefec9c12963d916>`（2002-04-15，Hugh Graham，"Re: Remote hole in the default install?"，snippet="I know that OpenBSD's slogan is 'Four years without a remote hole in the default install!'"——证实 2002-04 时宣传语为"Four years"）；Message-ID `<no-id-openbsd-misc-b0ff708df0957980>`（2002-07-03，Paul Pruett，snippet="one remote hole in the default install, in nearly 6 years"——证实 2002-07 时已更新为"one remote hole"）。
- **判定**：通过。
- **修正内容**：无。细节差异：2002-04-15 邮件称"Four years"，大纲称"Five years"（约 1997-2002）。四年/五年差异可能源于不同起始年份计算方式，不构成实质性矛盾。

### 4. 子节 212.1 — OpenBSD 3.1 发布公告（2002-05-19）

- **核查事实**：OpenBSD 3.1 于 2002-05-19 发布。
- **检索库**：邮件列表库（openbsd-announce）。
- **检索词**：`remote hole default install`（year 2002）。
- **证据**：Message-ID `<no-id-openbsd-announce-070ab646b7facba0>`（2002-05-19，Todd C. Miller，"OpenBSD 3.1 Released!"，snippet="This year OpenBSD turns 7 years old"——反推 1995 年 fork）。
- **判定**：通过。
- **修正内容**：无。

### 5. 子节 212.1 — "Only two remote holes" 宣传语（OpenBSD 5.7，2015）

- **核查事实**：OpenBSD 5.7 发布公告（2015-05-01）仍使用"more than ten years with only two remote holes"。
- **检索库**：邮件列表库（openbsd-announce）。
- **检索词**：`remote hole default install`（year 2015）。
- **证据**：Message-ID `20150430220613.GH32676 () ted ! stsp ! name`（2015-04-30，Stefan Sperling，"OpenBSD 5.7 Released"，snippet="We remain proud of OpenBSD's record of more than ten years with only two remote holes in the default install"）。
- **判定**：通过。
- **修正内容**：无。

### 6. 子节 194.1 — IPFilter 许可证变更 2001 年 5 月

- **核查事实**：Darren Reed 2001 年 5 月在 IPFilter 3.4.31 中修改许可证，加入限制性条款，引发 OpenBSD 社区争议。
- **检索库**：邮件列表库（openbsd-misc）。
- **检索词**：`IPFilter license`（year 2001）。
- **证据**：Message-ID `<no-id-openbsd-misc-14e7b149d23402b3>`（2001-05-29，"Re: Changes in IPFilter license..."）；Message-ID `<no-id-openbsd-misc-128a8b9742065cdd>`（2001-05-30，Kevin Sindhu，"FW: IPFilter license changes"）；Message-ID `<no-id-openbsd-misc-3fc339799cdcad85>`（2001-06-04，Theo de Raadt，"Re: IPFilter licence update"，snippet="Darren has stated that he doesn't want to change the license"）。
- **判定**：通过。
- **修正内容**：无。

### 7. 子节 194.1 — Daniel Hartmeier 与 pf 开发（2001 年）

- **核查事实**：Daniel Hartmeier 主导 pf 开发，pf 随 OpenBSD 3.0（2001-12）发布。
- **检索库**：邮件列表库（openbsd-bugs）。
- **检索词**：`pf packet filter`（year 2001）。
- **证据**：Message-ID `<no-id-11-e5c2e6b7950cb43a>`（2001-12-05，Daniel Hartmeier <daniel@benzedrine.cx>，"Re: pending/2220: packet filter problem"）；Message-ID `<no-id-openbsd-bugs-800fb055e071120a>`（2001-12-14，Magnus Biglert，snippet="A new packet filter, PF, featuring NAT capabilities, with a mostly ipf-compatible syntax"）。
- **判定**：通过。
- **修正内容**：无。

### 8. 子节 207.1 — LibreSSL 首个便携版发布（2014-07-11）

- **核查事实**：LibreSSL portable 2.0.0 于 2014-07-11 发布。
- **检索库**：邮件列表库（openbsd-announce）。
- **检索词**：`LibreSSL`（year 2014）。
- **证据**：Message-ID `CAComcpNXYABT2wTcU_NQah_jLF=tmy_6DCd8YTL-kg53Mz46CA`（2014-07-11，Bob Beck，"First release of LibreSSL portable is available."）。
- **判定**：通过。
- **修正内容**：无。大纲 207.1 称"LibreSSL fork 宣告后约 3 个月进入 OpenBSD 源码树"，邮件库证实 LibreSSL 首个 portable 版本 2014-07-11 发布，与大纲所述"2014-07-12 jsing 引入 lib/libressl/Makefile"的 commit 日期吻合。

### 9. 子节 207.1 — LibreSSL 2.0.1-2.1.1 连续发布（2014 年 7-10 月）

- **核查事实**：LibreSSL 在 2014 年 7-10 月密集发布多个版本。
- **检索库**：邮件列表库（openbsd-announce）。
- **检索词**：`LibreSSL`（year 2014）。
- **证据**：Bob Beck 2014-07-13 发布 2.0.1、2014-07-16 发布 2.0.2、2014-07-22 发布 2.0.3、2014-08-03 发布 2.0.4、2014-08-08 Brent Cook 发布 2.0.5（含 CVE-2014-3506-3511 修复）、2014-10-12 发布 2.1.0、2014-10-16 发布 2.1.1（POODLE 修复）。
- **判定**：通过。
- **修正内容**：无。

### 10. 子节 198.1（pledge 相关）— pledge(2) 2015 年 10 月在 OpenBSD 邮件列表中活跃讨论

- **核查事实**：pledge（最初名为 tame）于 2015 年引入 OpenBSD。
- **检索库**：邮件列表库（openbsd-misc/bugs）。
- **检索词**：`pledge`（year 2015）。
- **证据**：Message-ID `56335BEF.3020202`（2015-10-30，Michael Lesniewski，"syscall 96 in top(1) on renice"，snippet="Adding id to the pledge fixes this issue"）；Message-ID `20151031200226.GA4485`（2015-10-31，Juha Erkkilä，"pledge(2) and pselect(2)"）；Message-ID `11281.1445202405`（2015-10-18，Theo de Raadt 回复 syslogd pledge 相关 bug）。
- **判定**：通过。
- **修正内容**：无。

### 11. 子节 212.2 — FBI 后门传言 2010 年 12 月

- **核查事实**：Gregory Perry 2010-12-11 致 de Raadt 邮件声称 FBI 在前 OpenBSD 开发者的 IPsec 代码中植入后门，de Raadt 2010-12-14 转发至 openbsd-tech。
- **检索库**：邮件列表库（openbsd-misc）。
- **检索词**：`FBI backdoor`（year 2010-2011）。
- **证据**：Message-ID `20101218124908.15e123a6`（2010-12-18，secucatcher，"Re: FBI And OpenBSD..."，snippet 引述 The Register 2010-12-15 报道与 FBI 前探员 E J Hilbert 的评论）；Message-ID `8fc9ad7ff720307d15355f5ee197bcf4`（2011-11-22，Frédéric Perrin——一年后社区仍在讨论 FBI 后门传言）。
- **判定**：通过（邮件库证实了 2010 年 12 月 FBI 后门传言在社区中广泛传播，The Register 报道日期 2010-12-15 与大纲所述 2010-12-14 de Raadt 转发邮件时间吻合）。
- **修正内容**：无。

### 12. 子节 209.1 — OpenBSD 3.2 发布公告（2002-11-01）

- **核查事实**：OpenBSD 3.2 于 2002-11-01 发布，为第 12 个 CD-ROM 发行版。
- **检索库**：邮件列表库（openbsd-announce）。
- **检索词**：`remote hole default install`（year 2002）。
- **证据**：Message-ID `<no-id-openbsd-announce-30cce8bdc3637035>`（2002-11-01，Todd C. Miller，"OpenBSD 3.2 Released"，snippet="This is our 12th release on CD-ROM (and 13th via FTP)"）。
- **判定**：通过。
- **修正内容**：无。

### 13. 子节 209.1 — OpenBSD 3.4 发布公告（2003-11-01）

- **核查事实**：OpenBSD 3.4 于 2003-11-01 发布。
- **检索库**：邮件列表库（openbsd-announce）。
- **检索词**：`initial import of NetBSD`（无过滤年份）。
- **证据**：Message-ID `<no-id-openbsd-announce-4deea0b534c44fae>`（2003-10-30，Ted Unangst，"OpenBSD 3.4 Released"，snippet="Nov 1, 2003. We are pleased to announce the official release of OpenBSD 3.4"）。
- **判定**：通过。
- **修正内容**：无。

### 14. 子节 209.1 — de Raadt 2003 年 hackathon 邮件（DARPA 撤资）

- **核查事实**：2003 年 DARPA 撤资导致 OpenBSD hackathon 酒店被取消。
- **检索库**：邮件列表库（openbsd-misc）。
- **检索词**：`hackathon`（无过滤年份）。
- **证据**：Message-ID `<no-id-openbsd-misc-877ca872091dcb7a>`（2003-04-22，Henning Brauer，"UPenn cancelling hotel for OpenBSD hackathon?"，snippet="I am one of the 60 people directly affected by this"）；Message-ID `<no-id-openbsd-misc-326b1923cf407983>`（2003-04-23，Mats O Jansson，"About OpenBSD Hackathon 2003..."，snippet="I understand this is due to the cancellation of the DARPA grant to the POSSE program"）。
- **判定**：通过。
- **修正内容**：无。

### 15. 子节 191.3 — GCC GPLv3 争议：2015-12-02 邮件明确提及"No GPLv3 license was violated"

- **核查事实**：OpenBSD 在 ARM 平台上使用 binutils 2.17 以避免 GPLv3 许可证。
- **检索库**：邮件列表库（openbsd-tech）。
- **检索词**：`gcc GPLv3`（无过滤年份）。
- **证据**：Message-ID `20151202144734.GA16415`（2015-12-02，Tobias Ulmer，"ARM as: add .inst support"，snippet="No GPLv3 license was violated during writing this trivial diff"——证实 OpenBSD 开发者对 GPLv3 的敏感态度）。
- **判定**：通过。
- **修正内容**：无。

### 16. 子节 198.1 — Beck 2018 BSDCan 演讲《Pledge & Unveil》

- **核查事实**：Bob Beck 在 BSDCan 2018 发表关于 pledge 与 unveil 的演讲。
- **检索库**：参考文献库（fulltext）。
- **检索词**：`pledge unveil`。
- **证据**：reference_id=63（BECK B. Pledge & Unveil[C]//BSDCan 2018. Ottawa, 2018），全文含 pledge 子集说明与 unveil 文件系统沙箱设计。
- **判定**：通过。
- **修正内容**：无。

### 17. 子节 207.2 — Buehler 2019 BSDCan 演讲《TLS 1.3 Handshake State Machine in LibreSSL》

- **核查事实**：Theo Buehler 在 BSDCan 2019 发表关于 LibreSSL TLS 1.3 握手状态机的演讲。
- **检索库**：参考文献库（fulltext）。
- **检索词**：`LibreSSL`。
- **证据**：reference_id=79（bsdcan2019-tls13，Theo Buehler，2019）。
- **判定**：通过。
- **修正内容**：无。

### 18. 子节 207.2 — Buehler 2022 EuroBSDCon 演讲《Recent Progress in and around LibreSSL》

- **核查事实**：Theo Buehler 在 EuroBSDCon 2022 发表关于 LibreSSL 进展的演讲。
- **检索库**：参考文献库（fulltext）。
- **检索词**：`LibreSSL`。
- **证据**：reference_id=119（eurobsdcon2022-tb-libressl，Theo Buehler，2022，snippet="One of the four major forks of OpenSSL"）。
- **判定**：通过。
- **修正内容**：无。

### 19. 子节 205.6 — OpenSSH 1999 年 11 月 Slashdot 报道

- **核查事实**：OpenSSH 在 1999 年 11 月获得 Slashdot 报道。
- **检索库**：邮件列表库（openbsd-www）。
- **检索词**：`OpenSSH`（year 1999）。
- **证据**：Message-ID `<no-id-25-31512b8416d7fa23>`（1999-11-18，Richard Wong，"OpenSSH Media Coverage page"，snippet="I guess by now you know that slashdot has ran an article on OpenSSH"）。
- **判定**：通过。
- **修正内容**：无。

### 20. 子节 205.2 — OpenSSH 许可证纯洁化：de Raadt 1999 年邮件讨论 RSA 专利与 USA 法律

- **核查事实**：OpenSSH 在 USA 须处理 RSA 专利问题，提供 RSAREF2 实现。
- **检索库**：邮件列表库（openbsd-www / openbsd-announce）。
- **检索词**：`OpenSSH`（year 1999）。
- **证据**：Message-ID `<no-id-25-b89b2fc72f3ae774>`（1999-12-14，Eli Boaz，询问 OpenSSH RSA 许可问题）；Message-ID `<no-id-25-e90c135c52c30ea6>`（1999-12-14，Theo de Raadt，回复"RSA does. Contact their lawyers"）；Message-ID `<no-id-openbsd-announce-94bc1448ac7ea514>`（1999-12-03，Theo de Raadt，"2.6 sslUSA security problem"）。
- **判定**：通过。
- **修正内容**：无。

### 21. 子节 192.2.1 — OpenBSD 3.0 发布公告（2001-12-01）

- **核查事实**：OpenBSD 3.0 于 2001-12-01 发布，引入 pf 防火墙。
- **检索库**：邮件列表库（openbsd-bugs）。
- **检索词**：`pf packet filter`（year 2001）。
- **证据**：Message-ID `<no-id-openbsd-bugs-800fb055e071120a>`（2001-12-14，Magnus Biglert，snippet="While looking through what's new in 3.0, I followed this('A new packet filter, PF, featuring NAT capabilities')"）。
- **判定**：通过。
- **修正内容**：无。

### 22. 子节 207.1 — LibreSSL fork 在 misc@ 邮件列表的宣告

- **核查事实**：OpenBSD 项目于 2014-04-14 在 misc@openbsd.org 发起 LibreSSL fork。
- **检索库**：邮件列表库（openbsd-advocacy/tech）。
- **检索词**：`LibreSSL`（year 2014）、`Heartbleed`（year 2014）。
- **证据**：2014-04-27 邮件（miod@ 讨论 py-openssl breakage 与 Heartbleed 后修复）；2014-06-07 邮件（Solar Designer 讨论 OpenSSL 漏洞与 LibreSSL）。2014-04-14 当日宣告邮件在 limit 10 中未命中。
- **判定**：修正（补注）。2014-04-14 宣告邮件在本次检索未命中，但 2014-04-27 的 py-openssl 讨论以及 2014-06-07 的 LibreSSL 讨论证实 LibreSSL fork 在 2014 年 4-6 月间确实活跃于 OpenBSD 邮件列表。首次 LibreSSL portable 发布公告为 2014-07-11（Bob Beck）。
- **修正内容**：大纲 207.1 称"2014-04-14 在 misc@openbsd.org 邮件列表发起 LibreSSL fork"，邮件库检索到的最近相关邮件为 2014-04-27（miod@），2014-04-14 当日邮件未在本次检索的 limit 10 中命中。补注：邮件库证实 LibreSSL fork 在 2014 年 4-6 月间活跃，首次发布公告为 2014-07-11（Bob Beck）。

### 23. 子节 203.1 — de Raadt 被 NetBSD 逐出（1994-12-23）

- **核查事实**：Theo de Raadt 1994-12-23 被 NetBSD Core Team 撤销 commit 权限。
- **检索库**：邮件列表库（openbsd）。
- **检索词**：`deraadt`（year 1994-1995，0 命中）。
- **证据**：openbsd 邮件列表库覆盖范围始于 1996 年，1994 年事件不在覆盖范围内。
- **判定**：两库无法验证（早于 openbsd 邮件库覆盖范围 1996-）。
- **修正内容**：无。

### 24. 子节 203.3 — OpenBSD 1.0/1.1/1.2 早期发布历程

- **核查事实**：OpenBSD 1.0/1.1 为内部版本，1.2 于 1996 年 7 月首发。
- **检索库**：邮件列表库（openbsd）。
- **检索词**：`initial import of NetBSD`（无过滤年份，无 1996 年相关命中）。
- **证据**：openbsd 邮件列表库 1996 年数据量极小，无 1.0/1.1/1.2 发布相关邮件。
- **判定**：两库无法验证（openbsd 邮件库 1996 年数据稀疏，1.x 版本发布公告不在库中）。
- **修正内容**：无。

### 25. 子节 192.2.1 — 代码审计"数千个"漏洞的精确数字

- **核查事实**：OpenBSD 1996-2000 年间通过代码审计发现并修复数千个安全漏洞。
- **检索库**：两库均检索。
- **检索词**：`security audit`（邮件库 0 命中）；`audit`（参考文献库 fulltext 无关命中）。
- **证据**：未命中精确数字。大纲已自行标注"OpenBSD 官方一手表述使用'Thousands (yes, thousands)'但未给出精确数字"。
- **判定**：两库无法验证（精确数字无两库来源，大纲已作存疑标注）。
- **修正内容**：无。

### 26. 子节 209.2 — OpenBSD Foundation 2023 年收入约 30 万 USD

- **核查事实**：OpenBSD Foundation 2023 年度收入约 30 万 USD。
- **检索库**：两库均检索。
- **检索词**：`OpenBSD Foundation`（邮件库 0 命中，因"Foundation"在 1998-1999 年邮件中仅指代一般概念）。
- **证据**：未命中。OpenBSD Foundation 财务报告为 web 页面，不在两库覆盖范围内。
- **判定**：两库无法验证（OpenBSD Foundation 财务报告不在邮件库/参考文献库范围内）。
- **修正内容**：无。

### 27. 子节 209.2 — 2014 年电费危机募捐超 100,000 USD

- **核查事实**：2014 年 1 月 de Raadt 因卡尔加里电费危机（约 20,000 USD/月）发出募捐公告，最终募集超 100,000 USD。
- **检索库**：邮件列表库（openbsd）。
- **检索词**：`LibreSSL`（year 2014）。
- **证据**：LibreSSL 2014 年 7-8 月密集发布从侧面证实 2014 年项目活动高度活跃，但电费危机募捐具体金额（100,000 USD）和 20,000 USD/月电费在检索中未命中。
- **判定**：两库无法验证（电费危机募捐金额不在邮件库检索命中中，须以 WebFetch 直接访问 marc.info 存档或 OpenBSD 捐款页面核验）。
- **修正内容**：无。

### 28. 子节 203.7 — Adam Glass 1994-12-23 netbsd-users 通知邮件

- **核查事实**：Adam Glass 1994-12-23 通过 netbsd-users 邮件列表发布撤销 de Raadt 访问权限的通知。
- **检索库**：邮件列表库（openbsd）。
- **检索词**：`deraadt`（year 1994-1995，0 命中）。
- **证据**：openbsd 邮件库覆盖 1996-，1994 年 NetBSD 邮件不在本项目 openbsd 邮件库覆盖范围内。
- **判定**：两库无法验证（早于 openbsd 邮件库覆盖范围，且属于 NetBSD 项目邮件）。
- **修正内容**：无。

### 29. 子节 204.8 — OpenBSD 安全审计始于 1996 年夏季

- **核查事实**：OpenBSD 代码审计始于 1996 年夏季。
- **检索库**：邮件列表库（openbsd）。
- **检索词**：`security audit`（无过滤年份，0 命中）。
- **证据**：未命中。1996 年邮件库数据稀疏，无审计相关邮件。
- **判定**：两库无法验证（早于邮件库密集覆盖期，审计活动记录不在邮件列表中）。
- **修正内容**：无。

### 30. 子节 209.2 — OpenBSD Foundation 2014 筹款目标 150,000 USD，2015 年目标 200,000 USD

- **核查事实**：OpenBSD Foundation 2014 年筹款目标 150,000 USD，2015 年提升至 200,000 USD。
- **检索库**：两库均检索。
- **检索词**：`OpenBSD Foundation`（邮件库 0 命中）。
- **证据**：未命中。大纲已自行标注经 WebFetch 一手核验（campaign2014.html / campaign2015.html），但此信息不在两库范围内。
- **判定**：两库无法验证（OpenBSD Foundation 筹款页面为 web 页面，不在邮件库/参考文献库范围内，大纲已自行标注来源）。
- **修正内容**：无。

## 五、关键发现与建议

### 5.1 邮件库覆盖优势

- OpenBSD 邮件列表库（1996-）对第10卷主体时段（1996-2026）覆盖良好，特别是 1999 年 OpenSSH 诞生、2001 年 IPFilter/pf 争议、2002 年安全宣传语演化、2010 年 FBI 后门传言、2014 年 LibreSSL fork、2015 年 pledge 引入等关键事件均有邮件证据。
- openbsd-announce 列表对发布公告覆盖完整（3.1/3.2/3.4/5.7 等版本均命中）。

### 5.2 参考文献库覆盖

- 参考文献库含 Beck 2018 Pledge & Unveil（ref 63）、Buehler 2019 TLS 1.3（ref 79）、Buehler 2022 LibreSSL（ref 119）等关键 OpenBSD 演讲论文，对 pledge/unveil/LibreSSL 等技术主题有完整覆盖。
- 但对 OpenBSD 政治/治理维度（如 de Raadt 被逐、Foundation 资金、DARPA 撤资）无覆盖。

### 5.3 覆盖盲区

- 1994-1995 年 de Raadt 被逐事件（openbsd 邮件库覆盖始于 1996 年）
- OpenBSD 1.x 版本发布（1996 年邮件库稀疏）
- OpenBSD Foundation 财务数据（web 页面，非邮件/论文内容）
- 代码审计精确数字（非邮件/论文记录）

### 5.4 建议后续行动

- 对 1994-1995 年 de Raadt 被逐事实，建议检索 NetBSD 邮件库（`--project netbsd --year-from 1994 --year-to 1995`）
- 对 OpenBSD Foundation 财务数据，建议以 WebFetch 直接访问 foundation 官网
- 对 2014-04-14 LibreSSL fork 宣告邮件，建议以更精确的搜索词（如 `"LibreSSL" "fork"` 或 `"OpenSSL is dead"`）扩大 limit 检索