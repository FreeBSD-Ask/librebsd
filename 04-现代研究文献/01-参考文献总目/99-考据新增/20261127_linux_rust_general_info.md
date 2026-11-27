# Linux 内核 Rust 文档《General Information》（新 ref）引用卡

- **性质**：Linux 内核官方文档 Rust 章“General Information”（抽象层与绑定、no_std 等）
- **数据库**：新建 ref（2026-11-27 G4 全责线 V37 批 b029；库内无 docs.kernel.org Rust 章条目）
- **source_url**：<https://docs.kernel.org/rust/general-information.html>
- **quote（逐字，两段）**：

  > Abstractions are Rust code wrapping kernel functionality from the C side. In order to use functions and types from the C side, bindings are created.

  > Abstractions are not available for all the kernel internal APIs and concepts, but it is intended that coverage is expanded as time goes on. “Leaf” modules (e.g. drivers) should not use the C bindings directly. Instead, subsystems should provide as-safe-as-possible abstractions as needed.

- **考据注**：用于**两内核的编译器与接口抽象对照**（V37.13.4.2）与**内核 API 抽象负荷**（V37.13.4.3）。首段定义抽象层与绑定层的分工：绑定承接 C 侧函数与类型，抽象层包裹为安全接口；次段说明抽象覆盖未完成、叶模块不得直用 C 绑定、须由子系统补齐——覆盖缺口即持续维护负担。
- **限度**：①官方文档随内核版本滚动，本批以访问日 7.4.0-rc4 文本为准；②“as-safe-as-possible”为政策表述，具体安全性须逐抽象复核；③FreeBSD 侧对照引 ref10911（2025 Q4 状态报告），两文档口径不完全同构，只作制度面并置。
- **本批落点**：V37.13.4.2、V37.13.4.3
- **考据日期**：2026-11-27（Task 8.2 G4 全责线 V37 批 b029；official_doc／L3）
