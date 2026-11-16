# 4.4BSD `bin/csh/csh.1`（新 ref）引用卡

- **性质**：4.4BSD `usr/src/bin/csh/csh.1` 手册页源（roff），取自 TUHS utree（67,937 字节正文）
- **数据库**：新建 ref（2026-11-16 V31 P2 联网补证批 b016；source_url 四键查重：库内 TUHS 条目无 `csh.1`）
- **source_url**：<https://www.tuhs.org/cgi-bin/utree.pl?file=4.4BSD/usr/src/bin/csh/csh.1>
- **quote（逐字，一处）**：
  1. Use of the internal hash table to speed location of executed programs is disabled.（`unhash` 内建命令条目）
- **考据注**：本句是**路径散列的用意书证**：内部散列表的用途被写明为“加速定位可执行程序”，`unhash` 一命令正是把这项加速关掉——用意与开关同页可对。同页另有 `hashstat` 条目（打印散表命中统计，并对每个路径分量尝试 exec），与 `rehash`／`unhash` 并列，构成 6.6.4 的完整证据面（本块只取最直接一句）。**roff 披露**：引文自 `.It Ic unhash` 条目的两行正文按行序并句，未改字。**年代披露**：4.4BSD 树内文本（1993），窗口内；csh 本身的更早版本不在本块举证范围。
- **本批落点**：V31.6.6.4 第 1 块
- **考据日期**：2026-11-16（Task 8.2 G4 V31 P2 批 b016；official_doc／L3）
