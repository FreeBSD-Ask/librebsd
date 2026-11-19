# FreeBSD 1.0-RELEASE `xfree86/README.BSD` 引用卡

- **性质**：FreeBSD 1.0-RELEASE 光盘发行树 `tarballs/xfree86/README.BSD` 纯文本（19,497 字节），取自 FreeBSD 官方档案 archive.freebsd.org 的 old-releases/i386/1.0-RELEASE/ 目录（发行物内文档，标题行自述 “README for XFree86 2.0 on FreeBSD 1.0 and NetBSD 0.9”）
- **数据库**：新建 ref（2026-11-20 V36 P2 联网补证批 b005；source_url 四键查重：库内无 xfree86 相关 URL）
- **source_url**：<https://archive.freebsd.org/old-releases/i386/1.0-RELEASE/tarballs/xfree86/README.BSD>
- **quote（逐字，两处）**：
  1. “XFree86 is a port of X11R5 that supports several versions of Intel-based Unix. It is derived from X386 1.2, which was the X server distributed with X11R5.”（§1 What and Where is XFree86? 首两句，移植来源链）
  2. “A binary distribution is not available for 386BSD 0.1. The XFree86 2.0 source code supports 386BSD 0.1, but future version probably will not.”（§0 Notes，386BSD 可用面披露）
- **考据注**：第 1 处是**图形栈移植来源链**：PC 化 BSD 的显示栈由 X11R5→X386 1.2→XFree86 2.0 的移植链补齐，且同文件标题行并列 FreeBSD 1.0 与 NetBSD 0.9 两宿主——移植件（而非自研图形栈）是 1.x 显示栈的实际来源。第 2 处是**386BSD 可用面披露**：386BSD 0.1 无 XFree86 二进制发行（源码暂支持、后续不再保证）——显示栈补齐实际发生于 FreeBSD／NetBSD 分流之后，而非 386BSD 原生提供。**年代披露**：该 README 随 1.0-RELEASE（1993-12）发行、自述针对 XFree86 2.0——是 1.x 时代发行物的原生文档，非当代回溯。**载体披露**：发行物归档页以 nginx 目录列出，README.BSD 为纯文本原样抓取。
- **本批落点**：V36.1.5.1 第 1 块（第 1 处；第 2 处随批注披露，不单独落块）
- **考据日期**：2026-11-20（Task 8.2 G4 全责线 V36 P2 批 b005；official_doc／L3）
