# ref-new 考据登记（2026-11-27，V36 W1-6.2 研究稿）

- **标题**：FreeBSD 6.0-RELEASE Release Notes (i386)
- **作者**：The FreeBSD Project
- **年份**：2005
- **来源 URL**：https://www.freebsd.org/releases/6.0R/relnotes-i386/
- **抓取日期**：2026-11-27（快照见 dossier verification.snapshot）
- **用途**：V36.6.2.2（V36 补证）
- **源类型／等级**：official_doc／L3
- **查重披露**：refdedup 预检后未见同 URL／同标题命中，本条新建。

## 关键原文（逐字）

> Fine-grained locking to allow much of the VFS stack to run without the Giant lock has been added. This is enabled by default on the alpha, amd64, and i386 architectures, and can be disabled by setting the loader tunable (and sysctl variable) debug.mpsafevfs to 0 .

> Ongoing work is reducing the use of the Giant lock by the network protocol stack and improving the locking strategies.

## 中文提要

6.0 发行说明表明 VFS 栈仅大部分移出 Giant 锁，网络协议栈的巨锁退出仍在进行。
