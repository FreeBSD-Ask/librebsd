# 4.4BSD `sys/sys/mount.h`（新 ref）引用卡

- **性质**：4.4BSD 内核头文件 `sys/sys/mount.h` 全文，取自 TUHS utree 在线源码树浏览页（13,190 字节正文；文件内 `INITMOUNTNAMES` 名称表与 `MOUNT_*` 类型常量齐备）
- **数据库**：新建 ref（2026-11-16 V31 P2 联网补证批 b010；source_url 四键查重：库内 TUHS 源码条目无 `sys/sys/mount.h`）
- **source_url**：<https://www.tuhs.org/cgi-bin/utree.pl?file=4.4BSD/usr/src/sys/sys/mount.h>
- **quote（逐字，一处）**：第 81—91 行类型常量块原样（含制表符）：

  ```
  #define	MOUNT_UFS	1
  #define	MOUNT_NFS	2
  #define	MOUNT_MFS	3
  #define	MOUNT_PC	4
  #define	MOUNT_LFS	5
  #define	MOUNT_LOFS	6
  #define	MOUNT_FDESC	7
  #define	MOUNT_PORTAL	8
  #define MOUNT_NULL	9
  #define MOUNT_UMAP	10
  #define MOUNT_KERNFS	11
  ```

- **考据注**：本块是**文件系统类型的名义清单**——`MOUNT_UFS` 编号 1，其后依次为网络（nfs）、内存（mfs）、单机（pc）、日志结构（lfs）、回环（lofs／null／umap）、设备（fdesc）与内核伪文件系统（kernfs）。用于 2.2.5 的“分支时代沿革回溯”：1993 年的内核头把 UFS 写在这一族类型之首，名称与编号即是当时的名实秩序。**排印披露**：原文前 8 行以制表符对齐、后 3 行改用空格（`#define MOUNT_NULL` 起），上引代码块照录原样，未统一空白。同一文件的第 95—105 行 `INITMOUNTNAMES` 把这串常量映射为字符串名（`"ufs"` 等），供 2.2.6 的名实判定规程备用。**载体披露**：代码类引文按 `<pre>` 原样抄录，制表符保留；不取跨行拼接。
- **本批落点**：V31.2.2.5 第 1 块（2.2.6 另批取 `INITMOUNTNAMES` 段）
- **考据日期**：2026-11-16（Task 8.2 G4 V31 P2 批 b010；official_doc／L3）
