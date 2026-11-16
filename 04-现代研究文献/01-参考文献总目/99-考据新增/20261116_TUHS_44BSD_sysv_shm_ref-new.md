# 4.4BSD `sys/kern/sysv_shm.c`（新 ref）引用卡

- **性质**：4.4BSD 内核源码 `sys/kern/sysv_shm.c` 全文，取自 TUHS utree 在线源码树浏览页（13,449 字节正文；文件头 SCCS 标识 `@(#)sysv_shm.c 8.1 (Berkeley) 6/10/93`，另有 `from: Utah $Hdr: uvcp_shm.c 1.11 92/04/23$` 一行，实作 `uipc_shm.c`）
- **数据库**：新建 ref（2026-11-16 V31 P2 联网补证批 b010；source_url 四键查重：库内 TUHS 源码条目为 chroot.2／ffs_vfsops.c／kern_synch.c／vm_pageout.c／inetd.8／pc.1 等，无 `sysv_shm.c`）
- **source_url**：<https://www.tuhs.org/cgi-bin/utree.pl?file=4.4BSD/usr/src/sys/kern/sysv_shm.c>
- **quote（逐字，一处）**：
  1. System V shared memory routines. TEMPORARY, until mmap is in place; needed now for HP-UX compatibility and X server (yech!).
- **考据注**：本段是文件头部的设计注释，原文为三行注释体（`System V shared memory routines.` / `TEMPORARY, until mmap is in place;` / `needed now for HP-UX compatibility and X server (yech!).`），本卡与入库引文**按行序并句、未改字**，行首 ` * ` 注释符不计入引文。**载体披露**：utree 页以 `<pre>` 呈现源码，本卡只取注释文字，不取代码类引文（HTML 转义可能吞字符，代码类逐字性不作保证——见 `20261116_TUHS_44BSD_pc1_ref-new.md` 同类披露）。**文件头另记**：`This code is derived from software contributed to Berkeley by the Systems Programming Group of the University of Utah Computer Science Department. Originally from University of Wisconsin.`——即 System V 共享内存这条支线的入树路径为“威斯康星→犹他→柏克莱”，用于 1.3.3 的动因与来源辨析。**括注披露**：原文末尾 `（yech!）` 为作者语气词，照录不改，不作“美化”。
- **本批落点**：V31.1.3.3 第 1 块
- **考据日期**：2026-11-16（Task 8.2 G4 V31 P2 批 b010；official_doc／L3）
