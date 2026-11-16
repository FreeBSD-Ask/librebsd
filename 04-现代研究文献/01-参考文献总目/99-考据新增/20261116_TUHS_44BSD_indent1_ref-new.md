# 4.4BSD `usr.bin/indent/indent.1`（新 ref）引用卡

- **性质**：4.4BSD `usr/src/usr.bin/indent/indent.1` 手册页源（roff），取自 TUHS utree（12,528 字节正文）
- **数据库**：新建 ref（2026-11-16 V31 P2 联网补证批 b015；source_url 四键查重：库内 TUHS 条目无 `indent.1`）
- **source_url**：<https://www.tuhs.org/cgi-bin/utree.pl?file=4.4BSD/usr/src/usr.bin/indent/indent.1>
- **quote（逐字，一处）**：
  1. Indent is a C program formatter.  It reformats the C program in the input-file according to the switches.
- **考据注**：本句是**工具定位与纪律载体**：缩排由 `indent` 承担，具体做法交给“开关”（switches），故“手工纪律”在 1993 年已有可执行的工具侧配置——用于 4.3.5。同页 NOTE 另述“只给一个输入文件即就地改写（in-place）并留备份副本”，属同一条纪律的另一面（未入本块引文）。**roff 披露**：原文以 `.Nm Indent`／`.Ar C`／`.Ar input-file` 等宏写作，本卡引文为宏解析后的纯文本，分词双空格照录；不作 roff 标记混排。
- **本批落点**：V31.4.3.5 第 1 块
- **考据日期**：2026-11-16（Task 8.2 G4 V31 P2 批 b015；official_doc／L3）
