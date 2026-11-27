# Rust for Linux 内核政策页（新 ref）引用卡

- **性质**：Rust for Linux 官方站“Rust kernel policy”页（维护者、评审与重复驱动政策）
- **数据库**：新建 ref（2026-11-27 G4 全责线 V37 批 b029；库内无该政策页条目）
- **source_url**：<https://rust-for-linux.com/rust-kernel-policy>
- **quote（逐字，两段）**：

  > Some subsystems prefer to get a new co-maintainer, sub-maintainer, reviewer, etc. to split the workload, letting them take care of the Rust side.

  > Are duplicated C/Rust drivers allowed? The usual kernel policy applies. So, by default, no. However, subsystems may decide to allow it, temporarily, to get Rust bootstrapped — please see Rust reference drivers.

- **考据注**：用于**语言准入的制度比较**（V37.13.4.5）。首段记评审人力按子系统配置（共同维护者／子维护者／评审者）；次段记重复 C/Rust 驱动默认不允许、子系统可临时放行以完成引导。两条合并呈现“评审责任人＋临时放行＋默认回收”的准入结构。
- **限度**：①政策页为项目自述，具体子系统实践须以 MAINTAINERS 与邮件列表复核；②“temporarily”无固定期限，退出时点由子系统掌握；③页面随项目治理更新，以访问日为准。
- **本批落点**：V37.13.4.5
- **考据日期**：2026-11-27（Task 8.2 G4 全责线 V37 批 b029；official_doc／L3）
