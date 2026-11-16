# What Have We Learned from the PDP-11?（Bell 1977，新 ref）引用卡

- **性质**：C. Gordon Bell 回顾论文，32 页 PDF（1,616,632 B），bitsavers 实抓；书目经 Springer DOI 页核验
- **数据库**：新建 ref（2026-11-16 supp-V03-b001；四键查重：URL 0 条、三元组 0 条、sha 0 条；库内 ref1546 为 1998 年同名回顾，非本篇）
- **source_url**：<https://www.bitsavers.org/pdf/dec/pdp11/articles/Bell1977_WhatHaveWeLearnedFromThePDP-11.pdf>
- **DOI**：10.1007/978-94-010-1226-3_1（Springer：In: Boulaye G G, Lewin D W (eds). *Computer Architecture*. NATO ASI Series, vol 32. Dordrecht: D. Reidel, 1977: 1-38）
- **全文**：已入 `fulltext`＋`fulltext_blocks`（8 节；pdftotext 文本层提取，cp1252→UTF-8）

## quote（逐字；折行按单空格归一，省略号跳过中断段）

1. Many microprocessor designs incorporate the UNIBUS notion of mapping I/O and control registers into the memory address space, eliminating the need for I/O instructions without complicating the I/O control logic.
2. Another common minicomputer weakness was the lack of system range. … there were often no larger and smaller models with the same architecture.
3. First, it should be asynchronous, and thereby capable of accepting different configurations of memory that operate at different speeds. … the UNIBUS width should be relatively large, to get as much performance as possible

## 考据注

1. 第 1 处（§2 BACKGROUND）：UNIBUS 把 I/O 与控制寄存器映射入内存地址空间，免设 I/O 指令而不复杂化控制逻辑——指令集不另立 I/O 类的设计根据。
2. 第 2 处（§2 BACKGROUND）：设计前史所列小型机通病之一为缺乏系统谱系，扩容或廉价化时无同架构机型可选——向下兼容与机型分档的动因。
3. 第 3 处（§3 TECHNOLOGY）：四条设计态度之首为异步总线，可容纳不同速度的内存配置；并明言 UNIBUS 位宽取较大值以换取性能。

作者为 PDP-11 设计主持人，属当事人一手回顾（L4）；其对机器结构的描述可与 DEC 手册（L3）互证。

## 本批落点

- V03.1.1.2 第 2 块（D1 #3）
- V03.1.1.3 第 2 块（D1 #1）
- V03.1.1.4 第 2 块（D1 #2）

**考据日期**：2026-11-16（supp-V03-b001；academic_work／L4）
