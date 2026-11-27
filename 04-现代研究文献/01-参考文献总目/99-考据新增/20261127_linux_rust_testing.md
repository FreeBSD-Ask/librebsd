# Linux 内核 Rust 文档《Testing》（新 ref）引用卡

- **性质**：Linux 内核官方文档 Rust 章“Testing”（Rust 测试种类与运行方式）
- **数据库**：新建 ref（2026-11-27 G4 全责线 V37 批 b029；库内无该测试文档条目）
- **source_url**：<https://docs.kernel.org/rust/testing.html>
- **quote（逐字）**：

  > There are three sorts of tests: The KUnit tests. The #[test] tests. The Kselftests.

- **考据注**：用于**语言准入的制度比较之测试面**（V37.13.4.5）。官方文档把内核 Rust 测试分为 KUnit、`#[test]` 与 Kselftest 三类，说明测试面有固定制度载体；与同项目政策页的评审／临时放行条款并置，可对照 FreeBSD 侧以树内测试起步、视数据扩大或关闭的试验条款。
- **限度**：①文档列测试种类，不保证覆盖面与通过率；②KUnit／Kselftest 的具体运行环境另见各文档；③页面随内核版本滚动，以访问日为准。
- **本批落点**：V37.13.4.5
- **考据日期**：2026-11-27（Task 8.2 G4 全责线 V37 批 b029；official_doc／L3）
