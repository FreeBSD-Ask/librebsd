# 4.4BSD ffs_vfsops.c（TUHS 收录）（新 ref）引用卡

- **性质**：TUHS 源码树收录的 4.4BSD `usr/src/sys/ufs/ffs/ffs_vfsops.c`（文件系统操作表实现；文件头 SCCS 标识 `@(#)ffs_vfsops.c 8.1 (Berkeley) 6/11/93`）；本机 Chrome UA urllib 直取，`<pre>` 块 22,622 字符
- **数据库**：新建 ref（2026-11-16 V31 P2 联网补证批 b002；source_url 四键查重：库内 tuhs.org 为 chroot.2 页（10743）与 pipermail／Wiki 语料，`sys/ufs/ffs/ffs_vfsops.c` 无重合）
- **source_url**：<https://www.tuhs.org/cgi-bin/utree.pl?file=4.4BSD/usr/src/sys/ufs/ffs/ffs_vfsops.c>
- **quote（逐字，一处）**：struct vfsops ufs_vfsops = {
- **考据注**：这一行把**名实交错**写死在代码里：操作表名作 `ufs_vfsops`，表中成员却是 `ffs_mount`、`ffs_unmount`、`ffs_start`、`ffs_statfs` 等——类型名取 ufs，实现函数取 ffs，两套词在同一结构体上并用。用于 2.2.3“与 FFS 的名实关系”最直接。**能证与不能证**：本行只能证**命名实践**（表名用 ufs、实现用 ffs），**不能证**命名动机或谁先提出“UFS”这一称法；动机类判断留待另取当事人记述。**载体说明**：TUHS 为 4.4BSD 源码树公开转录，按原文核对；SCCS 行与版权头一并可见。**未取**：同文件 `ffs_mount` 的详细流程，留待 2.3 节
- **本批落点**：V31.2.2.3 第 1 块
- **考据日期**：2026-11-16（Task 8.2 G4 V31 P2 批 b002；official_doc／L3）
