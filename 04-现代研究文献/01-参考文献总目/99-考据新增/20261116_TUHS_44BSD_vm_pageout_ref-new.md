# 4.4BSD vm_pageout.c（TUHS 收录）（新 ref）引用卡

- **性质**：TUHS 源码树收录的 4.4BSD `usr/src/sys/vm/vm_pageout.c`（换页进程与活动／非活动队列扫描）；本机 Chrome UA urllib 直取，`<pre>` 块 10,130 字符
- **数据库**：新建 ref（2026-11-16 V31 P2 联网补证批 b002；source_url 四键查重：库内 vm_pageout.c 无条目）
- **source_url**：<https://www.tuhs.org/cgi-bin/utree.pl?file=4.4BSD/usr/src/sys/vm/vm_pageout.c>
- **quote（逐字，一处）**：If the page has been referenced, move it back to the active queue.
- **考据注**：该句是**非活动队列扫描**的分支注释：页被引用过就搬回活动队列，回收因此不是一次判决，而带“二次机会”。用于 3.2.1“全局时钟置换算法”时须**说清对应关系**：4.4BSD 用活动／非活动两条队列＋引用位实现近似的时钟行为，代码里没有名为 “clock hand” 的变量；文献里“clock”的称法另有所本。**能证与不能证**：本句证**二次机会的实现方式**（搬队），不证“全局时钟”这一名目；名目与算法谱系留待 3.2.2 复核。**未取**：同文件的 `vm_pageout_scan` 参数与 `VM_PAGEOUT_*` 常量
- **本批落点**：V31.3.2.1 第 1 块
- **考据日期**：2026-11-16（Task 8.2 G4 V31 P2 批 b002；official_doc／L3）
