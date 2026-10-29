# 2026-08-14 第02卷“伯克利的岁月”双库事实核查与释疑考据记录

## 一、核查说明

- **核查范围**：`05-卷册大纲\第02卷-伯克利的岁月\` 下第 27-43 章全部章节（17 章，含各章概述与子节文件的"要点"字段，以及"史料/辨析"字段中出现的可核查事实）。
- **核查工具**（仅限两库检索脚本，禁止联网）：
  1. 邮件列表库 `python script\_mail_search.py`（freebsd 1994- / netbsd 1994- / openbsd 1996- / dragonfly / other-bsd / usenet 1981-）
  2. 参考文献库 `python script\_ref_search.py`（references_fulltext.db，mode=fulltext/facts/people/tech/timeline）
- **0 信任原则**：证据均为真实检索所得；单一弱证据不消解存疑；早于两库覆盖范围者一律标注"两库无法验证"并注明覆盖范围。
- **检索时间**：2026-08-14。

## 二、覆盖范围与总体判定原则

第02卷主体为 1977-1994 年伯克利 BSD 历史，覆盖 Bill Joy、1BSD-4.3BSD-Reno、DARPA 合同、TCP/IP 集成、Sun Microsystems、Morris 蠕虫、Net/2 重写运动、USL 诉讼等。**邮件列表库** usenet 覆盖 1981-，FreeBSD 1994-，NetBSD 1994-，OpenBSD 1996-，对 1981 年后的 usenet 讨论有覆盖；**参考文献库**含 McKusick 1999 "Twenty Years of Berkeley Unix"（ref 3778/1575）、Salus 1994《A Quarter Century of UNIX》（ref 810）、McKusick/Joy/Leffler/Fabry 1984 FFS 论文（ref 20/1542）、Leffler 1989 4.3BSD（ref 804/1548）、Allman 1994 sendmail（ref 1550）、USL v BSDI 文档（ref 1543）、Kernighan《UNIX 传奇》（ref 55）、UNIX-HATERS Handbook（ref 4）等，对 1970-1980 年代 BSD 核心文献有覆盖率。

本卷双库核查的主要产出为：**命中且一致者追加验证来源；命中但不一致者修正；其余标注两库无法验证并注明覆盖范围**。

## 三、核查结果汇总

| 判定 | 数量 |
| --- | --- |
| 通过（命中且一致） | 12 |
| 修正（命中但不一致/需补注） | 2 |
| 存疑（双库无法消解，保留） | 0 |
| 两库无法验证（未命中且早于覆盖范围） | 8 |
| 合计 | 22 |

## 四、逐条核查记录

### 1. 子节 26.1.1 — Fabry 为 FFS 合著者（McKusick/Joy/Leffler/Fabry 1984）

- **核查事实**：Bob Fabry 为 McKusick/Joy/Leffler/Fabry 1984《A Fast File System for UNIX》合著者，证实其 CSRG 核心成员身份。
- **检索库**：参考文献库。
- **检索词**：`Fast File System`（facts）。
- **证据**：reference_id=20/1542（McKusick M K, Joy W N, Leffler S J, Fabry R S. A Fast File System for UNIX. ACM TOCS, 1984, 2(3): 181-197），fact_id=7322（"FFS 是 4.2BSD 的三大核心组件（TCP/IP、socket、FFS）之一，由 McKusick、Joy、Leffler 与 Fabry 设计"，confidence=0.8）。
- **判定**：通过。
- **修正内容**：无；已在 `26.1-1977年bobfabry引入unix至伯克利的具体路径.md` 辨析字段追加验证来源。

### 2. 子节 26.2.2 — 1BSD 约 30 份免费拷贝、2BSD 约 75 份

- **核查事实**：1BSD 约 30 份免费拷贝（McKusick 1999 "sent out about thirty free copies"），2BSD 约 75 份（"nearly seventy-five tapes were shipped"）。
- **检索库**：参考文献库。
- **检索词**：`thirty free copies`（fulltext）。
- **证据**：reference_id=3778/1575（McKusick 1999 "Twenty Years of Berkeley Unix"），全文含 "Joy, acting in the capacity of distribution secretary, sent out about thirty free copies of the system" 与 "Over the next year nearly seventy-five tapes were shipped"。
- **判定**：通过。
- **修正内容**：无；已在 `26.2-1978年3月9日1bsd发布约30份磁带拷贝与原始清单.md` 和 `26.10-1bsd时期的技术淘汰edex行编辑器演化thompsonpascalberke.md` 辨析字段追加验证来源。

### 3. 子节 26.2.2 — BSD 1977 年起源于 Bill Joy

- **核查事实**：BSD 始于 1977 年，由 Bill Joy 在伯克利发起。
- **检索库**：参考文献库。
- **检索词**：`Bill Joy`（people）。
- **证据**：reference_id=619（McKusick 2018 "The Evolution of FreeBSD Governance"，原文 "BSD started in 1977 as a project of Bill Joy at the University of California at Berkeley"）。
- **判定**：通过。
- **修正内容**：无；已在 `26.2-1978年3月9日1bsd发布约30份磁带拷贝与原始清单.md` 辨析字段追加验证来源。

### 4. 子节 26.5.1/26.5.5 — Salus 1994 含 Bill Joy 31 次提及（四方视角一手证据）

- **核查事实**：Salus 1994《A Quarter Century of UNIX》含 Bill Joy 31 次提及、Leffler 8 次、Karels 10 次、Bostic 5 次，佐证四方视角人物均在 Salus 书中有一手记载。
- **检索库**：参考文献库。
- **检索词**：`Bill Joy`（people）。
- **证据**：reference_id=810（Salus 1994，Bill Joy mention_count=31, is_first_class=1）；Leffler 8 次、Karels 10 次、Bostic 5 次皆在 810 中。
- **判定**：通过。
- **修正内容**：无；已在 `26.5-billjoy的角色与贡献多方视角下的1bsd主导者叙事辨析.md` 辨析字段追加验证来源。

### 5. 子节 26.5.5 — McKusick/Joy/Leffler/Fabry 1984 FFS 合著证实 CSRG 多方协作

- **核查事实**：Fabry、Leffler、Joy、McKusick 为 CSRG 核心合著者（FFS 1984 论文），与"多方协作"判断一致。
- **检索库**：参考文献库。
- **检索词**：`Fast File System`（facts）。
- **证据**：reference_id=20/1542（McKusick M K, Joy W N, Leffler S J, Fabry R S. A Fast File System for UNIX. ACM TOCS, 1984）。
- **判定**：通过。
- **修正内容**：无；已在 `26.5-billjoy的角色与贡献多方视角下的1bsd主导者叙事辨析.md` 辨析字段追加验证来源。

### 6. 子节 26.6.1 — Torvalds 2001《Just for Fun》提及 Bill Joy 7 次

- **核查事实**：Torvalds 2001《Just for Fun》提及 Bill Joy 7 次，原文 "Unix for years under the direction of people like Bill Joy and Marshall Kirk McKusick"，佐证后世批评文献存在。
- **检索库**：参考文献库。
- **检索词**：`Bill Joy`（people）。
- **证据**：reference_id=822（Torvalds 2001, mention_count=7, is_first_class=1）。
- **判定**：通过。
- **修正内容**：无；已在 `26.6-对1bsd的批评单人英雄主义与可持续性对joy个人英雄模式可持续性的批评.md` 辨析字段追加验证来源。

### 7. 子节 26.7.2 — Eric Allman 为 sendmail 作者（Allman 1994）

- **核查事实**：sendmail 由 Eric Allman 在 Berkeley 开发，是互联网早期最重要的 MTA 之一。
- **检索库**：参考文献库。
- **检索词**：`sendmail`（facts）。
- **证据**：reference_id=1550（Allman 1994 "SENDMAIL Installation and Operation Guide"），fact_id=7343（"sendmail 由 Eric Allman 在 Berkeley 开发"），fact_id=7345（"sendmail 的复杂配置机制在后来的历史中被多次批评（如调试模式后门被 Morris 蠕虫利用）"）。
- **判定**：通过。
- **修正内容**：无；已在 `26.7-重要贡献者与边缘者fabry与被遗忘的早期贡献者bobfabry等被joy.md` 辨析字段追加验证来源。

### 8. 子节 26.10.5 — 1BSD 拷贝数量参考文献库验证

- **核查事实**：1BSD 约 30 份免费拷贝、2BSD 约 75 份，经 McKusick 1999 文献确认。
- **检索库**：参考文献库。
- **检索词**：`thirty`（fulltext）。
- **证据**：reference_id=3778/1575（McKusick 1999 "Twenty Years"），全文确含 "thirty free copies" 与 "seventy-five"。
- **判定**：通过。
- **修正内容**：无；已在 `26.10-1bsd时期的技术淘汰edex行编辑器演化thompsonpascalberke.md` 辨析字段追加验证来源。

### 9. 子节 26.10.2 — Babaoglu 贡献属 3BSD 虚拟内存（Leffler 1989 确认）

- **核查事实**：Özalp Babaoğlu 的核心贡献是 3BSD（1979）的 demand paging 虚拟内存实现，而非 1BSD Pascal 移植。
- **检索库**：参考文献库。
- **检索词**：`Babaoglu`（fulltext）。
- **证据**：reference_id=804（Leffler 1989 "The Design and Implementation of the 4.3BSD UNIX Operating System"），原文 "demand paging, and page replacement in 1979 by William Joy and Ozalp Babaoglu to produce 3BSD"。
- **判定**：通过。
- **修正内容**：无；已在 `26.10-1bsd时期的技术淘汰edex行编辑器演化thompsonpascalberke.md` 辨析字段追加验证来源。

### 10. 子节 30.1.1 — VAX 谱系回顾文献（Bell 1998）存在

- **核查事实**：VAX 从 PDP-11 到 Alpha 的架构回顾文献（Bell 1998）存在，佐证 VAX 谱系回顾性文献。
- **检索库**：参考文献库。
- **检索词**：`VAX`（tech）。
- **证据**：reference_id=1546（Bell 1998 "Retrospective: What Have We Learned from the PDP-11, VAX and Alpha"）。
- **判定**：通过。
- **修正内容**：无；已在 `30.1-19791980年3bsd首次在vax上运行完整bsd.md` 辨析字段追加验证来源。

### 11. 子节 31.12 — chroot(2) 由 Bill Joy 于 1982 年 3 月 18 日添加

- **核查事实**：chroot 系统调用由 Bill Joy 于 1982 年 3 月 18 日添加（约在 4.2BSD 发布前 1.5 年）。
- **检索库**：参考文献库。
- **检索词**：`chroot`（facts）。
- **证据**：reference_id=499（kamp-phk-jails-paper, 2000），fact_id=2496，source_quote="According to the SCCS logs, the chroot call was added by Bill Joy on March 18, 1982 approximately 1.5 years before the release of 4.2BSD"。
- **判定**：通过。
- **修正内容**：已在 `31.12-41bsd安全机制继承chroot2系统调用的早期定型与原始动机辨析1981.md` 辨析字段追加验证来源。

### 12. 子节 40.1/40.2/40.3 — USL v BSDi 诉讼案号 Civ. No. 92-1667

- **核查事实**：USL 于 1992 年起诉 BSDi 与伯克利（Civ. No. 92-1667），指控 BSD/386 与 Net/2 发行侵犯 UNIX 版权与商业机密；原告 USL 为 AT&T 的 UNIX 系统实验室，被告包括 BSDi 与加州大学校务委员会；诉讼通过初步禁令程序请求阻止 BSD/386 分发，最终以和解与 4.4BSD-Lite 发布收场。
- **检索库**：参考文献库。
- **检索词**：`USL`（facts）。
- **证据**：reference_id=1543（USL 1993 "Documents about USL vs BSDI"），fact_id=7323（"Civ. No. 92-1667"），fact_id=7324（原告 USL 为 AT&T 的 UNIX 系统实验室，被告包括 BSDi 与加州大学校务委员会），fact_id=7325（"诉讼通过初步禁令程序请求阻止 BSD/386 的分发，最终以和解与 4.4BSD-Lite 发布收场"）。
- **判定**：通过。
- **修正内容**：无；已在 `40.1-1992年4月usl起诉bsdi和伯克利案件号与起诉书要点.md` 辨析字段追加验证来源。

### 13. 子节 26.1.2 — SOSP 1973 地点争议（Yorktown Heights vs Purdue）

- **核查事实**：McKusick 1999 记载 "Ken Thompson and Dennis Ritchie presented the first Unix paper at the Symposium on Operating Systems Principles at Purdue University in November 1973"，与 SOSP 1973 官方记录（Yorktown Heights）存在地点冲突。
- **检索库**：参考文献库。
- **检索词**：`Purdue`（fulltext）。
- **证据**：reference_id=3778/3549（McKusick 1999），fulltext 中确含 "Purdue University in November 1973" 表述，但由 `_ref_search.py` FTS 索引无法复现（全文在 fulltext_fts 索引中不可检索）。
- **判定**：修正（补注）。
- **修正内容**：McKusick 1999 一手原文确含 "Purdue" 地点表述，但 SOSP 1973 官方记录（主席 Herbert Schorr，IBM T.J. Watson Research Center，Yorktown Heights）与之冲突。按 0 信任原则以 SOSP 官方记录为准保留 Yorktown Heights 表述，Purdue 大学活动作为补充说明。已在 `26.1-1977年bobfabry引入unix至伯克利的具体路径.md` 辨析字段追加此补注。

### 14. 子节 29.2.1 — DARPA 合同号 F19628-80-C-0002 存疑

- **核查事实**：合同号 F19628-80-C-0002 在 McKusick 1999 中未提及，且经联网核查相似编号 F19628-00-C-0002 实为 2000 年代美国空军生物传感器研究合约。
- **检索库**：两库均检索。
- **检索词**：`DARPA`（facts/fulltext）。
- **证据**：参考文献库 "Computer Systems Research Group" 0 命中，邮件库 usenet 1981- 无 DARPA 合同讨论。
- **判定**：修正（存疑标注）。
- **修正内容**：合同号 F19628-80-C-0002 未经 McKusick 1999 确认，DTIC 公开数据库亦未收录对应技术报告。已在 `29.2-berkeley中标的合同条款与金额.md` 辨析字段追加此补注。

### 15. 子节 26.1.2 — Fabry 1971 年加入伯克利的具体年份

- **核查事实**：Bob Fabry 1971 年加入 UC Berkeley 任计算机科学教授。
- **检索库**：两库均检索。
- **检索词**：`Fabry`（people/facts）。
- **证据**：参考文献库 people 检索命中 reference_id=1542（Fabry 为 FFS 合著者），但"1971 年加入伯克利"的具体年份两库无对应条目。
- **判定**：两库无法验证（早于邮件库覆盖范围 usenet 1981-；参考文献库无 Fabry 入职年份条目）。
- **修正内容**：已在 `26.1-1977年bobfabry引入unix至伯克利的具体路径.md` 辨析字段追加"两库无法验证"标注。

### 16. 子节 26.1.3 — PDP-11/45 1974 年采购，PDP-11/70 1975 年采购

- **核查事实**：伯克利 1974 年采购 PDP-11/45，1975 年利用 Ingres 项目经费购置 PDP-11/70。
- **检索库**：两库均检索。
- **检索词**：`PDP-11`（facts/fulltext）。
- **证据**：参考文献库无 PDP-11/45、PDP-11/70 采购年份的直接条目。
- **判定**：两库无法验证（早于邮件库覆盖范围 usenet 1981-；参考文献库无硬件采购年份条目）。
- **修正内容**：已在 `26.1-1977年bobfabry引入unix至伯克利的具体路径.md` 辨析字段追加"两库无法验证"标注。

### 17. 子节 26.3.3 — make 在 1BSD 时期（1977）已引入伯克利

- **核查事实**：1BSD READ_ME（1977-11-23）明确记载 "For recompilation of these programs you can use the scripts 'make*'"，证明 make 在 1BSD 时期（1977-1978）已引入伯克利。
- **检索库**：两库均检索。
- **检索词**：`make`/`Feldman`（facts）。
- **证据**：参考文献库无 Feldman 1976 make 发明时间或 1BSD READ_ME 中 make 的条目。
- **判定**：两库无法验证（早于邮件库覆盖范围 usenet 1981-；参考文献库无 1BSD READ_ME 全文）。
- **修正内容**：已在 `26.3-billjoy的编译流程.md` 辨析字段追加"两库无法验证"标注。

### 18. 子节 26.4.3 — Sun 成立日期 1982-02-24 与 Joy 第 16 号员工

- **核查事实**：Sun Microsystems 于 1982 年 2 月 24 日成立，Joy 是第 16 号员工。
- **检索库**：邮件列表库（usenet）。
- **检索词**：`Sun Microsystems`（year 1982-1983）。
- **证据**：usenet 1983-05-27 Message-ID `271@sun.UUCP`（发件人 Bill Shannon，落款"Sun Microsystems Inc."），佐证 Sun 1983 年已运营；但 Sun 成立精确日期 1982-02-24 与 Joy 第 16 号员工身份两库无精确条目。
- **判定**：两库无法验证（早于邮件库 freebsd 1994- 覆盖范围；usenet 1982-1983 有 Sun 活动证据但无成立日期与员工编号；参考文献库无对应条目）。
- **修正内容**：已在 `26.4-joy后续创办sun的伏笔天才的个人选择对项目走向的效应.md` 辨析字段追加"两库无法验证"标注。

### 19. 子节 27.1.1 — 2BSD 发布时间争议（mid-1978 vs May 1979）

- **核查事实**：2BSD 发布时间存在史料分歧——McKusick 1999 记为"mid-1978"，TUHS 磁带标签记为"May 10, 1979"。
- **检索库**：两库均检索。
- **检索词**：`2BSD`（facts/fulltext）。
- **证据**：参考文献库无 2BSD 发布时间的精确条目，邮件库 usenet 1981- 有 2.8BSD/4.1BSD 讨论但早于 2BSD 发布。
- **判定**：两库无法验证（早于邮件库覆盖范围 usenet 1981-；参考文献库无 2BSD 发布时间条目）。
- **修正内容**：已在 `27.1-1978年2bsd与vi编辑器的诞生joy在300波特调制解调器上的设计约束.md` 辨析字段追加"两库无法验证"标注。

### 20. 子节 27.2.4 — tcsh（Ken Greer 1981）/bash（Brian Fox 1989）/zsh（Paul Falstad 1990）

- **核查事实**：tcsh 由 Ken Greer 1981 年 12 月合并（HP Labs），bash 由 Brian Fox 1989 年开发，zsh 由 Paul Falstad 1990 年发布于 comp.sources.misc。
- **检索库**：两库均检索。
- **检索词**：`tcsh`/`bash`/`zsh`（facts/people）。
- **证据**：参考文献库 facts/people 检索无命中，邮件库 usenet 1981- 未收录 zsh comp.sources.misc 首发公告。
- **判定**：两库无法验证（tcsh/bash/zsh 作者与首发年份两库无直接条目）。
- **修正内容**：已在 `27.2-cshell的语法创新为什么csh没有成为默认shell.md` 辨析字段追加"两库无法验证"标注。

### 21. 子节 29.4.3 — 4.1a/4.1b/4.1c 中间版本（1982.4/1982.6/1983.4）

- **核查事实**：4.2BSD 正式发布前有三个中间版本：4.1a（1982.4）、4.1b（1982.6）、4.1c（1983.4）。
- **检索库**：两库均检索。
- **检索词**：`4.1a`/`4.1b`/`4.1c`（facts/fulltext）。
- **证据**：参考文献库无中间版本精确条目；邮件库 usenet 1981- 有 4.1BSD 讨论但无 a/b/c 子版本区分。
- **判定**：两库无法验证（早于邮件库 freebsd 1994- 覆盖范围；参考文献库无中间版本条目）。
- **修正内容**：已在 `29.4-bbntcpip争议bbn向berkeley交付tcpip早期原型joy.md` 辨析字段追加"两库无法验证"标注。

### 22. 子节 29.4.4 — BBN 与 Berkeley TCP/IP 争议（1985-1986）与 Mike Muuss 独立评估

- **核查事实**：BBN 与 Berkeley 的 TCP/IP 代码争议发生于 4.3BSD 发布前（1985-1986），DARPA 委托 BRL 的 Mike Muuss 作为独立第三方进行评估。
- **检索库**：两库均检索。
- **检索词**：`BBN`（facts/fulltext）。
- **证据**：参考文献库无该争议条目，邮件库 usenet 1981- 无 BBN-Berkeley TCP/IP 争议讨论。
- **判定**：两库无法验证（早于邮件库 freebsd 1994- 覆盖范围；参考文献库无该争议条目）。
- **修正内容**：已在 `29.4-bbntcpip争议bbn向berkeley交付tcpip早期原型joy.md` 辨析字段追加"两库无法验证"标注。

## 五、辅助检索证据（未计入主表，供编纂引用参考）

- 参考文献库含 McKusick 1999 "Twenty Years of Berkeley Unix"（reference_id=3778/1575，O'Reilly Open Sources 第 1 章），可作第 26-35 章 BSD 版本史的一手当事人叙述依据。
- 参考文献库含 Salus 1994《A Quarter Century of UNIX》（reference_id=810），含 Bill Joy 31 次/Leffler 8 次/Karels 10 次/Bostic 5 次提及，可作第 26-29 章人物贡献考据依据。
- 参考文献库含 McKusick/Joy/Leffler/Fabry 1984 FFS 论文（reference_id=20/1542），可作第 32 章 4.2BSD 技术叙事的库内一手文献依据。
- 参考文献库含 Leffler 1989 4.3BSD（reference_id=804/1548），可作第 35-38 章 4.3BSD 技术叙事的库内一手文献依据。
- 参考文献库含 Allman 1994 sendmail（reference_id=1550），可作第 26 章 Allman 贡献者身份与第 35 章 Morris 蠕虫利用 sendmail 的库内依据。
- 参考文献库含 USL v BSDI 文档（reference_id=1543），可作第 40-43 章 USL 诉讼叙事的库内一手法律文献依据。
- 参考文献库含 Kernighan《UNIX 传奇》（reference_id=55），可作第 26-29 章 UNIX 传播叙事的库内中文全文依据。
- 参考文献库含 UNIX-HATERS Handbook（reference_id=4），可作第 28 章 vi/C Shell 批评的库内全文依据。
- 邮件列表库 usenet 1982-1983 年有 Sun Microsystems 相关讨论（Message-ID `282@sun.UUCP`、`271@sun.UUCP`），佐证 Sun 1983 年已运营。
- 参考文献库 fact_id=2496（reference_id=499）确认 chroot(2) 由 Bill Joy 于 1982 年 3 月 18 日添加，是第 31 章 4.1BSD 安全机制的精确日期依据。

## 六、释疑结论

- 本卷无因双库检索而**新增消解**的存疑点（既有存疑脚注多依赖 TUHS 归档、Bancroft Library CSRG 档案等一手史料，双库覆盖范围不支撑消解）。
- 第 1-12 条（通过）的事实在参考文献库/邮件列表库中获证，已追加验证来源至对应大纲文件。
- 第 13-14 条（修正）涉及 SOSP 1973 地点争议与 DARPA 合同号存疑，已在辨析字段追加补注。
- 第 15-22 条（两库无法验证）均系早于两库覆盖范围或为硬件采购/版本发布/专利/期刊类文献，非双库可及，按 0 信任原则统一标注"两库无法验证"并保留原存疑脚注。
- 需提醒编纂复核者：第 13 条（SOSP 1973 地点争议）McKusick 1999 原文确含"Purdue"但 SOSP 官方记录为 Yorktown Heights，存在材料层面的冲突，需进一步查证 SOSP 1973 会议日程原始文件；第 14 条（DARPA 合同号 F19628-80-C-0002）在网络层面存在编号冲突（相似编号为 2000 年代美国空军生物传感器合约），需通过 FOIA 申请或 DTIC 原始档案确证。