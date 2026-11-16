# usched_set(2)（DragonFly 在线手册页）（新 ref）引用卡

- **性质**：man.dragonflybsd.org 手册页 usched_set(2)；curl 实抓 2026-11-16（HTTP 200，4 879 B；HTML 内斜体标记使函数名渲染为 usched _ set，引文照页面提取文本）
- **数据库**：新建 ref（supp-V75-b018；四键查重：库内 man.dragonflybsd.org 域 0 条）
- **source_url**：<https://man.dragonflybsd.org/?command=usched_set&section=2>
- **quote（逐字两处）**：
  1. These tasks include: setting the user scheduler, assigning an LWP to a specific CPU, adding a CPU to the available CPUs for an LWP, and removing a CPU from the list of available CPUs for an LWP.
  2. The usched _ set () function requires superuser privileges for all commands except USCHED_GET_CPU and USCHED_GET_CPUMASK.
- **考据注**：手册页把用户调度器的可操作面写成四项任务（设调度器、绑核、加核、删核），并明示权限边界（除两枚 GET 外须超级用户）；实现在源树 sys/kern（如 usched_dfly.c，击穿 82 492 B），语义读手册、行为读源码，即“文档与源码对读”的官定分工。
- **本批落点**：V75.2.7.2 两块（D2 ref-new#url／#2）
- **考据日期**：2026-11-16（supp-V75-b018；official_doc／L3）
