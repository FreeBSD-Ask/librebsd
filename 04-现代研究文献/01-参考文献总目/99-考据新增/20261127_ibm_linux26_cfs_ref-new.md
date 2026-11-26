# ref-new 考据登记（2026-11-27，V36 W1-5.13 研究稿）

- **标题**：Inside the Linux 2.6 Completely Fair Scheduler
- **作者**：M. Tim Jones
- **年份**：2009
- **来源 URL**：https://developer.ibm.com/tutorials/l-completely-fair-scheduler
- **抓取日期**：2026-11-27（快照见 dossier verification.snapshot）
- **用途**：V36.5.13.1（V36 补证）
- **源类型／等级**：academic_work／L3（IBM developerWorks 技术文，事后综述）
- **查重披露**：refdedup 预检后未见同 URL／同标题命中，本条新建。本文为 2009 年回顾性技术文章，非 2003 年同时代文本；用于 O(1) 调度器的技术描述，并与 2.6 版本断代相扣。

## 关键原文（逐字）

> The early 2.6 scheduler, called the O(1) scheduler, was designed to solve many of the problems with the 2.4 scheduler—namely, the scheduler was not required to iterate the entire task list to identify the next task to schedule (resulting in its name, O(1), which meant that it was much more efficient and much more scalable).

## 中文提要

IBM 技术文记 Linux 2.6 早期调度器即 O(1) 调度器，不需遍历整个任务表，因而更高效、更具可扩展性。
