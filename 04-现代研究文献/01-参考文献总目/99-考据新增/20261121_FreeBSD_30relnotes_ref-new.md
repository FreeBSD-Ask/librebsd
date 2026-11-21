# FreeBSD 3.0-RELEASE `RELNOTES.TXT`（a.out→ELF 段）引用卡

- **性质**：FreeBSD 3.0-RELEASE 发行树顶层 `RELNOTES.TXT` 纯文本（33,515 字节），取自 FreeBSD 官方档案 archive.freebsd.org（3.0 发行注记）
- **数据库**：新建 ref（2026-11-21 V36 P2 联网补证批 b014；source_url 四键查重：库内无 3.0-RELEASE RELNOTES 条目）
- **source_url**：<https://archive.freebsd.org/old-releases/i386/3.0-RELEASE/RELNOTES.TXT>
- **quote（逐字一处；原文跨行断词按原样保留）**：
  1. “The default binary type (and compiler toolchain) has been switched from a.out to ELF. This gives us access to much newer compiler technology (much of which didn't support a.out), allows for smaller executables and provides much better support for languages like C++, among many other advantages. Older a.out libraries and binaries will, of course, continue to work and provisions have been made for having both varieties installed if and as necessary for transitional purposes.”（原文八行连续段）
- **考据注**：此段是**a.out 延续到 3.0 才改 ELF 的官方自述**：默认二进制类型与编译工具链在 3.0 才从 a.out 切换到 ELF（动机＝新编译器技术对 a.out 缺乏支持、更小可执行体、更好 C++ 支持），且旧 a.out 库与二进制“continue to work”、双格式并存作为过渡安排——2.x 期的 a.out 格式惯性与切换成本由官方写明。**年代披露**：随 3.0-RELEASE（1998-10）发行；所述切换时点（3.0）与其 2.x 延续面可对读。
- **本批落点**：V36.2.6.3 第 1 块
- **考据日期**：2026-11-21（Task 8.2 G4 全责线 V36 P2 批 b014；official_doc／L3）
