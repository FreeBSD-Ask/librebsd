# 4.4BSD `sys/net/radix.c`（新 ref）引用卡

- **性质**：4.4BSD 内核 `sys/net/radix.c` 全文，取自 TUHS utree（19,591 字节正文；文件头 SCCS 标识 `@(#)radix.c 8.1 (Berkeley) 6/10/93`）
- **数据库**：新建 ref（2026-11-16 V31 P2 联网补证批 b017；source_url 四键查重：库内 TUHS 条目无 `radix.c`）
- **source_url**：<https://www.tuhs.org/cgi-bin/utree.pl?file=4.4BSD/usr/src/sys/net/radix.c>
- **quote（逐字，一处）**：
  1. Routines to build and maintain radix trees for routing lookups.
- **考据注**：本句是**版本侧的方法自述**：路由查找的基数为树由该文件负责建维，7.4.6 的“版本”一侧以此为凭。**待补披露（要紧）**：与该方法对应的论文（Sklower 1991 年 USENIX 文，常被引作 radix 树出处）本批**未取得原文**，故“论文与版本互证”只做到“版本侧与当年发行公告并置”，不推称“代码依该论文写成”，论文原文列待补。**载体披露**：引文为代码块内注释原样，行首 ` * ` 不计入；同文件另有 `@(#)radix.c 8.1 (Berkeley) 6/10/93` 修订戳可作档案侧参照。
- **本批落点**：V31.7.4.6 第 1 块
- **考据日期**：2026-11-16（Task 8.2 G4 V31 P2 批 b017；official_doc／L3）
