# comp.unix.wizards csh 讨论贴（1981／1983，本地 Usenet 存档）引用卡

> 用途：V12.3.8 节（vi 与 csh 的设计选择：同时代用户的批评）内容补证（V12 补证批 b072）。Usenet 新闻组存档（一手过程材料，L4）。

## 一、著录

Usenet newsgroup comp.unix.wizards（1981—1983 三条讨论贴）[DB/OL]. 本地存档：`03-原始史料库/11-邮件列表史料/07-usenet/duckdb/usenet_mail.duckdb`（表 messages，list_id=23）；源文件 `raw/mbox/comp.unix.wizards/1981-09.mbox`／`1983-06.mbox`（TUHS pipermail 抓取，mbox 格式）[2026-11-27].

- 责任者：各贴作者（见下）；新闻组 comp.unix.wizards（经 ucbvax 等网关转发）
- 载体：本地 Usenet 存档数据库（usenet_mail.duckdb，234,573 条／43 列表；comp.unix.wizards 38,195 条，1969—2016）
- `source_tier=primary`（同时代讨论贴，过程性一手材料；L4）
- 访问日：2026-11-27（本地库直查）

## 二、逐字引文（英文，未翻译；贴内引号与拼写照录）

作业控制行为之批评（3.8.1A；1983-06-08，rusty at sdcarl.UUCP，message_id 4281@sdcarl.UUCP）：

> if you do a ps you will discover that both sleeps have been stopped. i would expect that only the 2nd one would be stopped.

便利与脚本控制的取舍（3.8.2A；1981-09-17，ihuxp!steffen at Berkeley，message_id ucbvax.3188）：

> People at BTL mainly use the interactive features of csh, not the shell script control structures.

批评的归因回应（3.8.3A；1983-06-10，dean at cornell.UUCP，message_id 4585@cornell.UUCP）：

> There is a bug in the exec routine in the 4.1c kernel. One manifestation of this bug is when the shell tries to execute a command file that does not have "#! /bin/csh" (or "#! /bin/sh") as its first line.

用户立场（3.8.4A，1981-12-27 Rich Wales at UCLA-Security，message_id 3189）：

> My motivation is basically that /bin/csh seems so much better than /bin/sh.

当事人（安装者）回应（3.8.5A，1981-09-17 Steffen 贴内转引 Greg Guthrie，1981-09-11）：

> Steve Sutphen at Univ. Alberta (used to be in uucp alberta!steve) was going to do exactly what you described, about a year ago.

言论渠道（3.8.6A，1981-09-17 Steffen 贴尾）：

> Please reply via unix-wizards due to Arpanet-Usenet communication problems.

早期用户之迁移需求（4.7.1A，1981-06-12 JMETZGER at USC）：

> Does anyone know of a way to restore a DD tape of a v6 file system to Vax Unix running 4bsd and convert it to the v7 file system format?

使用反馈之驱动问题（4.7.3A，1981-12-26 Alan S. Watt at ITT Programming Technology Center）：

> Several times now I have had occasion to write tapes just a little too large for a 2400 ft reel. Every time the tape simply came off the reel, a very unpleasant experience with a TU78

## 三、考据说明

1. 三条贴均出自 comp.unix.wizards 的 1981／1983 讨论：rusty 的“两个 sleep 都被停”是**用户对作业控制行为的批评**；Steffen 的“BTL 人主要用 csh 的交互特性、不用其脚本控制结构”是**用户分化的同时代实证**；dean 的“exec 例程的 bug 而非 csh”是**批评的技术归因回应**——三者恰对 3.8.1／3.8.2／3.8.3 三题。
2. 贴内拼写（小写 i）与引号（直引号）照录；Steffen 贴经 ucbvax 网关转发，from 字段为网关形。
3. **消息定位**：三条贴的 message_id 已录，可在库内以 `select * from messages where message_id=...` 复核全文；时间以库内 date 字段为准。
4. L4 纪律：同时代讨论为过程性证据，参与者身份（Berkeley／Cornell／sdcarl）按邮件头 as-is，不代为认定。
5. 禁引核查：TUHS 公开 pipermail 抓取的本地存档，`banned_source=0`。
