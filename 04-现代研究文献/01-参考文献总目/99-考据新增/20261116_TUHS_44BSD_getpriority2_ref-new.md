# 4.4BSD getpriority(2) 手册页（TUHS 收录）（新 ref）引用卡

- **性质**：TUHS 源码树收录的 4.4BSD `usr/src/lib/libc/sys/getpriority.2`（getpriority／setpriority 手册页，SCCS 行 `@(#)getpriority.2 8.1 (Berkeley) 6/4/93`）；本机 Chrome UA urllib 直取，`<pre>` 块 4,127 字符
- **数据库**：新建 ref（2026-11-16 V31 P2 联网补证批 b004；source_url 四键查重：库内 getpriority 无条目）
- **source_url**：<https://www.tuhs.org/cgi-bin/utree.pl?file=4.4BSD/usr/src/lib/libc/sys/getpriority.2>
- **quote（逐字，两处；mroff 渲染后）**：
  1. Prio is a value in the range -20 to 20.  The default priority is 0; lower priorities cause more favorable scheduling.
  2. Only the super-user may lower priorities.
- **考据注**：第 1 句给**数值轴**（-20 到 20、默认 0、越低越有利），第 2 句给**单向门**（只有超级用户能把优先级调得更优）——两者合起来才是“nice 与用户让渡”：普通用户只能自减优待，让渡是默认选项而非请求项。**渲染记账**：第 1 句原文在两句之间有双空格（mroff 排版），照录为两个空格；`.Fa`／`.Dv` 等宏标记不入引文。**能证与不能证**：只证接口语义与权限，不证该系统调用的引入年代（HISTORY 节另有说明，本批未取）。**未取**：PRIO_PROCESS／PRIO_PGRP／PRIO_USER 三选一的细节，留待 1.2.4 复核
- **本批落点**：V31.1.2.5 第 1 块（第 1 句）、第 2 块（第 2 句）
- **考据日期**：2026-11-16（Task 8.2 G4 V31 P2 批 b004；official_doc／L3）
