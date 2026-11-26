# ref-new 考据登记（2026-11-26，V36 W1-3.10 研究稿）

- **标题**：Linux 2.2.26 源码树（include/asm-i386/smplock.h、kernel/sched.c）
- **作者**：Linux Kernel Archives
- **年份**：2004
- **来源 URL**：https://cdn.kernel.org/pub/linux/kernel/v2.2/linux-2.2.26.tar.gz
- **抓取日期**：2026-11-26（快照见 dossier verification.snapshot）
- **用途**：V36.3.10.1（V36 补证）
- **源类型／等级**：official_doc／L3
- **查重披露**：refdedup 预检后未见同 URL／同标题命中，本条新建。

## 关键原文（逐字）

> Getting the big kernel lock.

> spinlock_t runqueue_lock = SPIN_LOCK_UNLOCKED;  /* second */

## 中文提要

2.2 系列的 i386 SMP 头文件以注释与 lock_kernel() 内联函数实现全局大内核锁。
