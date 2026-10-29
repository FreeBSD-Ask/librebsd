# 2026-08-14 第01卷“unix的起源”双库事实核查与释疑考据记录

## 一、核查说明

- **核查范围**：`05-卷册大纲\第01卷-unix的起源\` 下第 1-26 章全部章节（26 章，含各章概述与子节文件的“要点”字段，以及“史料/辨析”字段中出现的可核查事实）。
- **核查工具**（仅限两库检索脚本，禁止联网）：
  1. 邮件列表库 `python script\_mail_search.py`（freebsd 1994- / netbsd 1994- / openbsd 1996- / dragonfly / other-bsd / usenet 1981-）
  2. 参考文献库 `python script\_ref_search.py`（references_fulltext.db，mode=fulltext/facts/people/tech/timeline）
- **0 信任原则**：证据均为真实检索所得；单一弱证据不消解存疑；早于两库覆盖范围者一律标注“两库无法验证”并注明覆盖范围。
- **检索时间**：2026-08-14。

## 二、覆盖范围与总体判定原则

第01卷主体为 1960-1970 年代 UNIX/Multics 前史与 19-20 世纪数学、物理、哲学背景，**绝大多数事实早于邮件列表库覆盖范围**（usenet 1981-，FreeBSD 1994-，NetBSD 1994-，OpenBSD 1996-），参考文献库虽含 Kernighan《UNIX 传奇》（ref 55）、PDP-7 Users Handbook（ref 2763）、Thompson《Reflections on Trusting Trust》（ref 22）、UNIX-HATERS Handbook（ref 4）、Ritchie《The Development of the C Language》（ref 1531）、Corbató 1965 设计论文（ref 861）、Pike UTF-8 短文（ref 1539）、Plan 9 系列论文（ref 1160/1163/1165）等，但对 1960 年代前史、哲学、数学、物理、硬件产业事实无覆盖。因此本卷双库核查的主要产出为：**命中且一致者追加验证来源；命中但不一致者修正；其余标注两库无法验证并注明覆盖范围**。

## 三、核查结果汇总

| 判定 | 数量 |
| --- | --- |
| 通过（命中且一致） | 6 |
| 修正（命中但不一致/需补注） | 1 |
| 存疑（双库无法消解，保留） | 0 |
| 两库无法验证（未命中且早于覆盖范围） | 9 |
| 合计 | 16 |

## 四、逐条核查记录

### 1. 子节 2.10.5 — Thompson 1984 图灵奖演讲《Reflections on Trusting Trust》

- **核查事实**：Thompson 1984 年图灵奖演讲《Reflections on Trusting Trust》发表于 Communications of the ACM 27(8), 761-763。
- **检索库**：参考文献库。
- **检索词**：`Trusting Trust`（facts，0 命中）；`Multics`（fulltext，命中 ref 22）。
- **证据**：reference_id=22（Thompson 1984，题名 ReflectionsOnTrustingTrust，全文库含其 ACM 图灵奖演讲全文）；reference_id=1158（同题名著录）。
- **判定**：通过。
- **修正内容**：无；已在 `2.10-与同时期操作系统的比较ctssibmos360dectops10george3.md` 辨析字段追加“经参考文献库验证通过（reference_id=22 / reference_id=1158）”。

### 2. 子节 5.1.2 — B 语言为 BCPL 简化、Thompson 于 PDP-7 实现

- **核查事实**：C 语言的直接前身是 Thompson 为 PDP-7 编写的 B 语言，B 又是 BCPL（Martin Richards）的简化。
- **检索库**：参考文献库。
- **检索词**：`PDP-7`（facts）；`Thompson`（facts）。
- **证据**：fact_id=7290，reference_id=1531（Ritchie 1993《The Development of the C Language》），fact_text=“C 语言的直接前身是 Thompson 为 PDP-7 编写的 B 语言，而 B 又是 BCPL（Martin Richards）的简化”，confidence=0.8。
- **判定**：通过。
- **修正内容**：无；已在 `5.1-从bcpl到b语言martinrichards与kenthompson的语言谱系.md` 辨析字段追加“经参考文献库验证通过（fact_id=7290，reference_id=1531）”。

### 3. 子节 8.4.2 — Pike 1983 年夏季多伦多 USENIX 演讲《cat -v Considered Harmful》

- **核查事实**：Rob Pike 1983 年夏季 USENIX 会议（多伦多）演讲批评 `cat -v`。
- **检索库**：邮件列表库（usenet）。
- **检索词**：`cat -v`（limit 8）。
- **证据**：Message-ID `432@hcr.UUCP`（1983-06-09，“Toronto USENIX Conference Schedule (tentative)”，comp.org.usenix）确认 1983 年 7 月多伦多夏季 USENIX 会议；另有 `136@cbosgd.UUCP`、`5520@watmath.UUCP` 等“On the floor of summer USENIX 83”帖转述 Rob Pike 对 UNIX 不一致性的批评。
- **判定**：通过（会议地点与年份获证；`cat -v` 演讲原文本身不在库内）。
- **修正内容**：无；已在 `8.4-catv争议joy编写的catv命令被robpike与kernighan.md` 辨析字段追加验证来源。

### 4. 子节 15.7.3 — FreeBSD Foundation 2004-12-21 SCSL 撤销与 2005-01 报道

- **核查事实**：Sun 2004-12-21 向 FreeBSD Foundation 发出 SCSL 撤销通知；2005-01 InfoWorld Paul Krill 询问。
- **检索库**：邮件列表库（freebsd-java）。
- **检索词**：`Sun revokes`（year 2004-2005）。
- **证据**：Message-ID `LOBBIFDAGNMAMLGJJCKNEEPBEPAA.tedm@toybox.placo.com`（2005-01-05，“FW: Sun revokes FreeBSD license for Java”，freebsd-java），正文含 InfoWorld Paul Krill 询问转发与 Foundation 2004-12-21 newsletter 链接。
- **判定**：通过。
- **修正内容**：无；已在 `15.7-java与虚拟机革命freebsdjava移植史java1995年sun.md` 辨析字段追加验证来源。

### 5. 子节 25.7 — UTF-8 由 Pike 与 Thompson 设计、Plan 9 最早系统级采用

- **核查事实**：UTF-8 由 Rob Pike 与 Ken Thompson 设计；Plan 9 是最早在系统层面采用 UTF-8 的操作系统之一；UTF-8 设计目标含与 ASCII 兼容、不含 NUL 与 / 等特殊字节（文件系统安全）、无字节序依赖。
- **检索库**：参考文献库。
- **检索词**：`UTF-8`（facts）。
- **证据**：fact_id=7311/7312/7313，reference_id=1539（Pike 1993《Hello World or Kalimera Kosme (UTF-8 Plan 9)》）。
- **判定**：通过。
- **修正内容**：无；已在 `25.7-Plan-9-的关键概念史-UTF-8-命名空间-9P-rio.md` 辨析字段追加验证来源。

### 6. 子节 24.1 / 25.x — Plan 9 from Bell Labs 系列论文

- **核查事实**：Pike 等《Plan 9 from Bell Labs》论文（1990 UKUUG / 1993 / 1995 BLTJ）与 Presotto & Thompson《Plan 9 Design》等一手论文存在。
- **检索库**：参考文献库。
- **检索词**：`Thompson`（facts）。
- **证据**：reference_id=1160（Presotto_Thompson_Plan_9_Design，1990）、1163（Plan_9_from_Bell_Labs，1993）、1165（Presotto_Thompson_Plan_9_Programming_Environment，1995）。
- **判定**：通过。
- **修正内容**：无（仅作库内著录核验，未逐字改写入文件）。

### 7. 子节 1.9.1 — Multics ring 0“约 157,000 字”的出处

- **核查事实**：ring 0 在 1973 年约 157,000 字（36 位字长，可执行代码与只读数据），本节归源为 MIT LCS RFC 37（1973）。
- **检索库**：参考文献库。
- **检索词**：`Multics`（facts）。
- **证据**：fact_id=8310，reference_id=861（Corbató 1965《preliminary-discussion-of-the-design-of-a-multics-system》），source_quote=“about 157,000 words 0f text section (executable code and read only data)”。该值在 Corbató 1965 设计论文中已出现。
- **判定**：修正（补注）。
- **修正内容**：本节将“157,000 字”仅归于 RFC 37（1973）的著录需复核——该数字在 Corbató 1965 设计论文（reference_id=861）中已出现；两库无法进一步确证 RFC 37 原文，保留存疑。已在 `1.9-belllabs退出1969年的成本超支与设计过度.md` 辨析字段追加此补注。

### 8. 子节 1.8.1 — CTSS 1961 年 11 月在 IBM 709 首次演示

- **核查事实**：Corbató 1961 年 11 月在 IBM 709 上首次演示 CTSS，为世界首个可用分时系统。
- **检索库**：两库均检索。
- **检索词**：`Corbató`（people，0 命中）；`Multics`（facts）；`CTSS`（facts，0 命中）。
- **证据**：未命中。
- **判定**：两库无法验证（早于邮件列表覆盖范围 usenet 1981-；参考文献库无 CTSS 全文条目）。

### 9. 子节 1.9.1 — Multics 至 1969 年累计投入约 1000 万美元

- **核查事实**：Multics 至 1969 年累计投入约 1000 万美元。
- **检索库**：两库均检索。
- **检索词**：`Multics`（facts/fulltext）。
- **证据**：未命中该金额。
- **判定**：两库无法验证（贝尔实验室内部财报不在两库范围内）。

### 10. 子节 1.11.3 — Multics 2000-10-30 17:08 UTC 关闭最后实例

- **核查事实**：2000 年 10 月 30 日加拿大国防部 DND-H 执行最后关机（部分来源作 10 月 31 日），17:08 UTC。
- **检索库**：邮件列表库（usenet，year 2000）。
- **检索词**：`Multics`（year-from 2000 year-to 2000）。
- **证据**：命中 5 条 usenet 2000 年 Multics 讨论（unix.bsd.misc、unix.bsd.openbsd.misc 等，主题为 BSD & Linux、text editors、Orange Book），均无 DND-H 关闭记录。
- **判定**：两库无法验证（关闭事件属 2000 年 web 档案，非邮件列表内容；原存疑脚注保留）。

### 11. 子节 1.15.14.4 — setuid 专利 US 4,135,240（1979 授予）

- **核查事实**：setuid 机制由 Dennis Ritchie 发明，AT&T 1972 年申请专利，1979 年授予 US 4,135,240。
- **检索库**：参考文献库。
- **检索词**：`4,135,240`（facts，0 命中）；`setuid`（fulltext 命中 ref 55 Kernighan《UNIX 传奇》，facts 仅命中 ref 606 setuid=off 挂载选项）。
- **证据**：未命中专利号原文。
- **判定**：两库无法验证（专利属 1972-1979 年，早于邮件库覆盖范围；参考文献库全文含 setuid 词但未及专利号）。已在 `1.15-时代语境…md` 辨析字段追加。

### 12. 子节 3.2.2 — PDP-7 1964 年 12 月首次出货、最大 32K 字

- **核查事实**：PDP-7 为 DEC 1964 年 12 月首次出货，18 位字长，4K 字内存可扩至 32K 字。
- **检索库**：参考文献库。
- **检索词**：`PDP-7`（facts，命中 ref 1531；fulltext 命中 ref 2763 PDP-7 Users Handbook 1965）。
- **证据**：reference_id=2763（PDP-7 Users Handbook，DEC 1965）全文存在，但检索返回的 snippet 为首页，未含 1964 首出货与 32K 规格细节。
- **判定**：两库无法验证（PDP-7 Users Handbook 在库，但检索脚本仅返回首页 snippet，无法逐规格核验；1964 年早于邮件库覆盖范围）。

### 13. 子节 7.6.1 — “Do one thing well”最早文字记录出自 McIlroy 1978 BSTJ 57:6 Foreword

- **核查事实**：“Do one thing well”最早文字记录出自 McIlroy 1978 年 BSTJ 57:6 Foreword（与 Pinson、Tague 合著）。
- **检索库**：两库均检索。
- **检索词**：`McIlroy`（facts，命中 ref 879 Bentley 1986《Little Languages》）；`do one thing well`（facts/fulltext，0 命中）。
- **证据**：reference_id=879 source_quote 述 McIlroy 以六行 UNIX shell 实现词频统计，未及 1978 BSTJ 57:6 Foreword 原文。
- **判定**：两库无法验证（BSTJ 1978 期刊文献不在两库全文范围内）。已在 `7.6-mcilroy与组件化doonethingwell的最早表述.md` 辨析字段追加。

### 14. 子节 10.3.2 — Informix 需为超过 100 种 UNIX 开发超过 1000 个产品版本

- **核查事实**：Informix 1980 年代末至 1990 年代初需为超过 100 种 UNIX 变体开发超过 1000 个产品版本。
- **检索库**：两库均检索。
- **检索词**：`Informix`（facts/fulltext，0 命中）；usenet `Informix`（year 1988-1992，0 相关命中）。
- **证据**：未命中“100/1000”原始出处。
- **判定**：两库无法验证（早于 FreeBSD 邮件库覆盖范围 1994-；usenet 1981- 亦无此商业数据）。已在 `10.3-unix碎片化…md` 辨析字段追加。

### 15. 子节 10.4.1 — Miller 1990 模糊测试“almost 90”工具、“25-33%”崩溃率

- **核查事实**：Miller, Fredriksen & So 1990 CACM 论文对 7 个 UNIX 版本约 90 个工具测试，25%-33% 可被随机输入致崩溃。
- **检索库**：两库均检索。
- **检索词**：`2533`（fulltext，命中 ref 2763/3397/3742 均无关）；`fuzz`（usenet 1989-1991，命中 perl/sun 等无关帖）；`Miller`（facts，未命中该论文）。
- **证据**：未命中该论文全文或原始表述。
- **判定**：两库无法验证（CACM 1990 期刊文献不在两库覆盖范围内）。已在 `10.4-代码质量下降…md` 辨析字段追加。

### 16. 子节 16.9.2 — 2024-01-20 freebsd-hackers“The Case for Rust (in the base system)”讨论线程

- **核查事实**：Alan Somers 2024-01-20 在 freebsd-hackers 发起“The Case for Rust (in the base system)”，Warner Losh 回复 002830。
- **检索库**：邮件列表库（freebsd）。
- **检索词**：`The Case for Rust`（hackers 列表，year 2024，0 命中）；`Rust`（year 2024，仅命中 `cu` 列表无关帖）。
- **证据**：未命中该线程；仅见 Warner Losh `5A74E928-2F4A-4BD6-8B77-837B793055C3@karels.net` 等无关主题。
- **判定**：两库无法验证（该 2024-01-20 freebsd-hackers 线程未见于本地邮件库索引，或在采集范围之外）。已在 `16.9-rust与系统编程的未来…md` 辨析字段追加。

## 五、辅助检索证据（未计入主表，供编纂引用参考）

- 参考文献库含 Ritchie & Thompson 1978 BSTJ 复刊《The UNIX Time-Sharing System》（reference_id=1279）与 Morris-Thompson 1978 BSTJ 密码一文（reference_id=1276），可作 6.1/6.2 节与 9.10 节密码散列演化的库内著录依据。
- 参考文献库含《UNIX-HATERS Handbook》（reference_id=4，Garfinkel 等 1994）全文，可作第 12/13 章 UNIX 审美批评的库内全文依据。
- 参考文献库含 Kernighan《UNIX 传奇：历史与回忆》（reference_id=55）全文，可作第 1-7 章 UNIX 起源叙事的库内全文依据。
- 参考文献库含 Ritchie《The Development of the C Language》（reference_id=1531）与 Lions《The Second Pass of the Portable C Compiler》（reference_id=3742），可作第 5/6 章 C 语言史依据。
- 邮件列表库 usenet 1989 年 comp.sources.unix 存有 Larry Wall 提交 Perl 3.0 的分发帖（Message-ID `2122@papaya.bbn.com`、`2129@papaya.bbn.com`），佐证 Perl 经 usenet 分发的事实，但 Perl 1.0（1987-12-18）早于 usenet 库覆盖起始，无法直接验证。

## 六、释疑结论

- 本卷无因双库检索而**新增消解**的存疑点（既有存疑脚注多依赖联网考据，双库覆盖范围不支撑消解）。
- 双库核查未能验证的条目（第 8-16 条）均系早于两库覆盖范围或为期刊/专利/网页档案类文献，非双库可及，按 0 信任原则统一标注“两库无法验证”并保留原存疑脚注。
- 唯一需提醒编纂复核者为第 7 条（1.9.1“157,000 字”的出处著录）。
