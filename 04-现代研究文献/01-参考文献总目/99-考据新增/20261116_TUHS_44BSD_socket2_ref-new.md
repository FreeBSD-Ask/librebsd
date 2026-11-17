# 4.4BSD `lib/libc/sys/socket.2`（新 ref）引用卡

- **性质**：4.4BSD `usr/src/lib/libc/sys/socket.2` 手册页源（roff），取自 TUHS utree（7,760 字节正文）
- **数据库**：新建 ref（2026-11-16 V35 P2 联网补证批 b004；source_url 四键查重＋规范化 URL：库内无该文件）
- **source_url**：<https://www.tuhs.org/cgi-bin/utree.pl?file=4.4BSD/usr/src/lib/libc/sys/socket.2>
- **quote（逐字，两处）**：
  1. The socket function call appeared in 4.2BSD.（HISTORY 节，原文 `.Nm function call appeared in .Bx 4.2 .`）
  2. Socket creates an endpoint for communication and returns a descriptor.（DESCRIPTION 段，原文 `.Fn Socket creates an endpoint for communication and returns a descriptor.`，`.Fn` 宏解析为纯文本，同“宏已解析”先例）
- **考据注**：这是**接口起点的手册记载**：4.4BSD 的 socket(2) 自己把该调用的首见版本定为 4.2BSD——V35 3.3.1“socket 接口的 4.2BSD 起点”以此为基准。**对照披露（要紧）**：The Open Group 的 `<sys/socket.h>` 页（ref10840）溯源只提 XNS、不提 BSD；同一接口在“发行版手册”与“标准文本”两处得到**不同的来路叙述**，这正是 3.3.2“渊源脱嵌”的比对样本，两卡互见。**roff 披露**：宏已解析为纯文本（socket／4.2BSD）。
- **本批落点**：V35.3.3.1 第 1 块；V08.9.4.1 第 2 块（2026-11-17 V08 b001 追加 quote 2）
- **考据日期**：2026-11-16（Task 8.2 G4 V35 P2 批 b004；official_doc／L3）
