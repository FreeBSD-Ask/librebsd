# FreeBSD `share/man/man9/style.9`（新 ref）引用卡

- **性质**：FreeBSD 源码树 `share/man/man9/style.9`（内核源码风格指南）纯文本，取自 FreeBSD 官方 cgit 的 plain 视图（29,073 字节；文件头版权 “Copyright (c) 1995-2025 The FreeBSD Project”，`.Dd July 28, 2025`）
- **数据库**：新建 ref（2026-11-16 V31 P2 联网补证批 b014；source_url 四键查重：库内无 cgit plain 视图条目）
- **source_url**：<https://cgit.freebsd.org/src/plain/share/man/man9/style.9>
- **quote（逐字，三处，分落三块）**：
  1. This file specifies the preferred style for kernel source files in the FreeBSD source tree.（DESCRIPTION 首句）
  2. Style guide for FreeBSD.  Based on the CSRG's KNF (Kernel Normal Form).（示例代码块内的注释，原文为双空格分词）
  3. Many of the style rules are implicit in the examples.  Be careful to check the examples before assuming that style is silent on an issue.（真值段落，原文为双空格分词）
- **考据注**：第 1 句是**归属自述**：现存 style(9) 是 FreeBSD 树的文件，故其成文不在 4.4BSD（1993）之内——4.3.2 据此与“4.4BSD 树无 man9”互证。第 2 句是**承继表述的关键句**：FreeBSD 风格指南自认“Based on the CSRG's KNF”，承继关系由文件自己写明——4.3.3 用。第 3 句是**体例自述**：规则多隐含于示例，读示例先于猜条文——4.3.4 用。**年代披露（要紧）**：本文件 `.Dd` 为 2025 年、版权上限亦 2025，所引三句属现行文本；它证明“承继声明与体例写法存在”，**不证明 1990 年代的原句一字未改**，逐字史须取早年版本另考。**载体披露**：man 源文件为 roff，本卡引文取自 cgit plain 文本的 roff 源码行，未做 roff 渲染。
- **本批落点**：V31.4.3.2 第 2 块（第 1 句）、V31.4.3.3 第 1 块（第 2 句）、V31.4.3.4 第 1 块（第 3 句，下批落）
- **考据日期**：2026-11-16（Task 8.2 G4 V31 P2 批 b014；official_doc／L3）
