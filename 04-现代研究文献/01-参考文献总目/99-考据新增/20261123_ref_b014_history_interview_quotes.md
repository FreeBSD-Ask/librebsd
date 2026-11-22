# ref-b014 复用追加卡（V50 b014：ref10249 history 页五句＋ref10251 访谈两句，纯复用批零新建）

## 1. ref10249（复用）＝DragonFly BSD — History——b014 追加引文池

- **来源**：DragonFly BSD Project. DragonFly BSD — History[EB/OL]. https://www.dragonflybsd.org/history/ [2026-11-23].（既有 ref，b014 经 curl 实抓现行页 5 358 B 存 script/_g5_b011_src/dfly_history.txt；页脚 Last edited 2019-01-17）
- **b014 追加引文**（逐字，直撇照录）：
  1. [2.3.3 用] The project was originally billed as "the logical continuation of the FreeBSD 4.x series", as quoted in the announcement, but this description has long since become obsolete.
  2. [2.3.4 用] the DragonFly project focused on rewriting most of the major kernel subsystems to implement required abstractions and to support mechanics for the second phase of the project（工作遍及几乎每个子系统、官方明言 particularly the filesystem APIs and kernel core）
  3. [2.3.5 用] At around the same time there was also a concerted effort to upgrade the sound system with a major HDA port from FreeBSD.
  4. [2.3.5 用] This resulted in the adoption of the pkgsrc framework for management of all non-base-system third-party applications in order to pool our resources with other BSD projects using this framework.
  5. [备用（2.3.3 定位变迁面）] From a performance perspective DragonFly's only real competitor these days is Linux.

## 2. ref10251（复用）＝OSNews 6338 访谈——b014 追加引文池

- **来源**：LOLI E. Interview with Matthew Dillon of DragonFly BSD[EB/OL]. (2004-03-13). https://www.osnews.com/story/6338/interview-with-matthew-dillon-of-dragonfly-bsd/ [2026-11-23].（既有 ref，b014 经 curl 实抓）
- **b014 追加引文**（逐字，原文拼写照录）：
  1. [2.3.3 用] But the FreeBSD-4 codebase is of strictly limited utility as a source of new code and maintainance updates.（maintainance 照录）
  2. [2.3.4 用] DragonFly began as a fork off of FreeBSD-4, because that was the most reliable starting point and because we wanted to do major core pieces of the system quite differently from the direction FreeBSD-5 took. For example, we are focused on more of a compartmentalized threading model to scale to SMP rather then the mutex model that FreeBSD-5 has chosen to use.（rather then 照录）
- **tier 依据**：10249＝官方文档／L3；10251＝当事人一手访谈／L4（块头“事后追述”按表定 talk_interview）。

## 界线与查重

- 纯复用批零新建 ref；四键查重面＝既有 ref 另取锚不重引（b011—b013 未引过 history 页正文句与访谈 Q2/Q3 句）。
- freebsd-current 跟帖面（2.3.5 敌意叙述一手）仍属邮件来源，按 DOC_MINE 非邮件界线不落块，本批以官方正面叙述（回流＋共池）承担题面协作面，“敌意”面由 2.3.3 无缓和叙事与 2.1.2 分歧题跨题合成。
