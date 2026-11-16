# FreeBSD `usr.sbin/jail/jail.8`（新 ref）引用卡

- **性质**：FreeBSD 源码树 `usr.sbin/jail/jail.8` 手册页源（roff），取自 FreeBSD 官方 cgit plain 视图（48,741 字节）
- **数据库**：新建 ref（2026-11-16 V31 P2 联网补证批 b015；source_url 四键查重：库内无 cgit plain 视图条目）
- **source_url**：<https://cgit.freebsd.org/src/plain/usr.sbin/jail/jail.8>
- **quote（逐字，两处，分落两块）**：
  1. Some restrictions of the jail environment may be set on a per-jail basis.（`allow.*` 小节正文，原文跨两行，按行序并句）
  2. The jail utility appeared in FreeBSD 4.0.（HISTORY 节，原文以 `.Nm`／`.Fx` 宏写作）
- **考据注**：第 1 句证**局限后来成为可配项**（每 jail 各自设定），窗口内“名单式／单点式”的边界做法在此已换形态——用于 5.3.5（前夜材料的去向）。第 2 句是**时点与分驻依据**：`jail` 工具出现于 FreeBSD 4.0，晚于本卷窗口（1974—1995），故容器化与 Jail 局限归后续专题卷——用于 5.3.6。**年代披露**：本文件为现行文本，`.Dd` 晚近；所引两句（限制可配、HISTORY 4.0）属结构性陈述与版本时点，改动风险低，但仍不据此推称 1999 年初版文字一字相同。**roff 披露**：第 2 句的宏已解析为纯文本（`jail`／`FreeBSD`）。
- **本批落点**：V31.5.3.5 第 1 块（第 1 句）、V31.5.3.6 第 1 块（第 2 句）
- **考据日期**：2026-11-16（Task 8.2 G4 V31 P2 批 b015；official_doc／L3）
