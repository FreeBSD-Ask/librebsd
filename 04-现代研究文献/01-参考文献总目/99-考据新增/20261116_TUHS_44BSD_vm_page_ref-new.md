# 4.4BSD `sys/vm/vm_page.c`（新 ref）引用卡

- **性质**：4.4BSD 内核 `sys/vm/vm_page.c` 全文，取自 TUHS utree 在线源码树浏览页（17,110 字节正文；文件头 SCCS 标识 `@(#)vm_page.c 8.1 (Berkeley) 6/11/93`，另含 CMU Mach 版权段与作者署名 “Avadis Tevanian, Jr., Michael Wayne Young”）
- **数据库**：新建 ref（2026-11-16 V31 P2 联网补证批 b012；source_url 四键查重：库内 TUHS 源码条目无 `vm_page.c`）
- **source_url**：<https://www.tuhs.org/cgi-bin/utree.pl?file=4.4BSD/usr/src/sys/vm/vm_page.c>
- **quote（逐字，一处）**：
  1. `/* perhaps iomem needs it's own type, or dev pager? */`（原文第 265 行，位于 `#ifdef i386` 的 `pmap_isvalidphys` 失败分支内）
- **考据注**：本行是**硬件约束的书面痕迹**——VAX 式“物理页连续可入自由队列”的假定在 i386 上不成立（PC 有内存空洞与设备内存），代码只能对无效物理地址另作处置，作者在注释里承认“也许 iomem 该有自己的类型或设备 pager”。用于 3.1.6。**异体字披露**：注释原文作 `it's`（应为 its），引文照录，不改字。**载体披露**：代码类引文自 `<pre>` 原样抄录，行首制表符不计入引文（注释文字本身）；不取跨语句拼接。
- **本批落点**：V31.3.1.6 第 1 块
- **考据日期**：2026-11-16（Task 8.2 G4 V31 P2 批 b012；official_doc／L3）
