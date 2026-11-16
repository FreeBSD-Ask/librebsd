# 4.4BSD `sys/vm/vm_object.c`（新 ref）引用卡

- **性质**：4.4BSD 内核 `sys/vm/vm_object.c` 全文，取自 TUHS utree 在线源码树浏览页（36,402 字节正文；文件头 SCCS 标识 `@(#)vm_object.c 8.1 (Berkeley) 6/11/93`，另含 “Copyright (c) 1987, 1990 Carnegie-Mellon University” 与作者署名 “Avadis Tevanian, Jr., Michael Wayne Young”）
- **数据库**：新建 ref（2026-11-16 V31 P2 联网补证批 b012；source_url 四键查重：库内 TUHS 源码条目无 `vm_object.c`）
- **source_url**：<https://www.tuhs.org/cgi-bin/utree.pl?file=4.4BSD/usr/src/sys/vm/vm_object.c>
- **quote（逐字，两处，分落两块）**：
  1. Each object also records a "pager" routine which is used to retrieve (and store) pages to the proper backing storage. In addition, objects may be backed by other objects from which they were virtual-copied.（模块说明注释，原文第 91—94 行）
  2. Object starts out read-write, with no pager.（初始化注释，原文第 176 行；其下即 `object->pager = NULL;`）
- **考据注**：第 1 句是**对象与文件层的接口**：对象自己不保管介质，存取交给 pager 例程，故“对象层衔接文件层”在代码上落在 pager 这个钩子上——用于 3.4.2。第 2 句是**匿名页的位置**：新对象无 pager、读写缺省，说明匿名内存就是“没有后继存储的对象”，并非另立一类——用于 3.4.3。**属性披露**：两处引文均属 CMU Mach 血统的模块注释（文件头版权为 CMU，1987／1990），进入 4.4BSD 时保留原注，故引文所证是 Mach 对象模型的语义，不能直接当作柏克莱自创。**载体披露**：注释按行并句、未改字；行首 ` * ` 与制表符不计入引文。
- **本批落点**：V31.3.4.2 第 1 块（第 1 句）、V31.3.4.3 第 1 块（第 2 句）
- **考据日期**：2026-11-16（Task 8.2 G4 V31 P2 批 b012；official_doc／L3）
