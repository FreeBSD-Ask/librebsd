# Rust for Linux 版本政策页（新 ref）引用卡

- **性质**：Rust for Linux 官方站“Rust version policy”页（最低支持版本政策）
- **数据库**：新建 ref（2026-11-27 G4 全责线 V37 批 b029；库内无该政策页条目）
- **source_url**：<https://rust-for-linux.com/rust-version-policy>
- **quote（逐字）**：

  > Since early 2026, our current policy is to follow Debian Stable's Rust version as the minimum supported version. For instance, Debian 13 (Trixie)'s Rust version is 1.85.0 at the time of writing. Thus, some months after Debian's release (to give time for developers to upgrade), it became the Rust minimum in Linux v7.1.

- **考据注**：用于**两项目编译器版本要求不同**（V37.13.4.4）。政策页把最低 Rust 版本锚定 Debian Stable 的版本，并给出 1.85.0 成为 Linux v7.1 下限的实例；与 FreeBSD 侧“不依赖不稳定特性、升级工具链不致破坏”的自述并置，可见两项目在编译器版本策略上的取向差异（发行版锚定 vs 稳定子集）。
- **限度**：①政策自 2026 年初生效，早于此时的版本要求另见历史页；②“最低支持版本”为政策下限，实际构建仍可能要求更高；③页面随 Debian 发行节奏更新，以访问日为准。
- **本批落点**：V37.13.4.4
- **考据日期**：2026-11-27（Task 8.2 G4 全责线 V37 批 b029；official_doc／L3）
