# OpenBSD FAQ: Introduction to OpenBSD（FAQ 第 1 章）（新 ref）引用卡

- **性质**：openbsd.org FAQ 第 1 章（About OpenBSD 等问答）；curl 实抓 2026-11-16（HTTP 200，11 788 B，纯文本提取）
- **数据库**：新建 ref（supp-V75-b013；四键查重：库内该 URL 0 条）
- **source_url**：<https://www.openbsd.org/faq/faq1.html>
- **quote（逐字三处）**：
  1. OpenBSD is all free. The binaries are free. The source is free. All parts of OpenBSD have reasonable copyright terms permitting free redistribution.
  2. OpenBSD is distributed with a number of third-party software products, including
  3. Much home-grown software is also included. Additional applications are available as packages .
- **考据注**：第 1 处为“全免费”的三重并列（二进制、源码、可自由再分发）；第 2—3 处为 base 系统构成的自述——先列第三方件（X.org、LLVM/Clang、GCC、Perl、NSD/Unbound、ncurses、binutils、gdb、libfido2、Expat、zlib），再言自研件亦在内、其余走 packages。故“完整系统”指 base 自带第三方件与自研件为一体，包只是补充，不属 base。
- **本批落点**：V75.2.2.3 两块（D2 ref-new#url／#2）
- **考据日期**：2026-11-16（supp-V75-b013；official_doc／L3）
