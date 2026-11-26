# ref-new 考据登记（2026-11-26，V36 W1-3.5 研究稿）

- **标题**：kld(4) — dynamic kernel linker facility（FreeBSD 3.x stable 分支）
- **作者**：The FreeBSD Project
- **年份**：1998
- **来源 URL**：https://cgit.freebsd.org/src/plain/share/man/man4/kld.4?h=stable/3
- **抓取日期**：2026-11-26（快照见 dossier verification.snapshot）
- **用途**：V36.3.5.1／V36.3.5.2（V36 补证）
- **源类型／等级**：official_doc／L3
- **查重披露**：refdedup 预检后未见同 URL／同标题命中，本条新建。

## 关键原文（逐字）

> This interface, like its predecessor, allows the system administrator to dynamically add and remove functionality from a running system. This ability also helps software developers to develop new parts of the kernel without constantly rebooting to test their changes.

> New block and character device drivers may be loaded into the system with KLD .

> The FreeBSD system makes extensive use of loadable kernel modules, and provides loadable versions of most filesystems, the NFS client and server, all the screen-savers, and the iBCS2 and Linux emulators.

## 中文提要

kld(4) 记该接口允许管理员在运行中的系统上动态增删功能，开发者无需反复重启即可测试内核改动。
