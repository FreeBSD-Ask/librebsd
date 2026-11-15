# 4.4BSD kern_synch.c（TUHS 收录）（新 ref）引用卡

- **性质**：TUHS 源码树收录的 4.4BSD `usr/src/sys/kern/kern_synch.c`（调度、睡眠唤醒与 CPU 估价衰减参数所在文件）；本机 Chrome UA urllib 直取，`<pre>` 块 17,086 字符
- **数据库**：新建 ref（2026-11-16 V31 P2 联网补证批 b002；source_url 四键查重：库内 kern_synch.c 无条目）
- **source_url**：<https://www.tuhs.org/cgi-bin/utree.pl?file=4.4BSD/usr/src/sys/kern/kern_synch.c>
- **quote（逐字，一处）**：We wish to decay away 90% of p_cpu in (5 * loadavg) seconds.
- **考据注**：该句位于文件内“constants for digital decay and forget”注释段，说明 CPU 使用估价 `p_cpu` 的**衰减目标**：在 5 倍负载均值秒内衰减 90%。用于 1.2.2“优先级递减的负反馈”——负反馈不是口号，而是带时窗与比例的衰减规则。**体裁披露**：这是**设计意图的注释**（作者自述的算法目标），不是行为测试；实际效果须由实现与实测另行确认，本块只记“他们这样定义衰减”。**同段另有** `p_cpu *= decay` 与经验式的推导，本批未逐一引。**载体说明**：TUHS 转录，按原文核对
- **本批落点**：V31.1.2.2 第 1 块
- **考据日期**：2026-11-16（Task 8.2 G4 V31 P2 批 b002；official_doc／L3）
