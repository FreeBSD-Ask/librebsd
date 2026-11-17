# FreeBSD xen(4) 手册页（新 ref）引用卡

- **性质**：FreeBSD 官方手册 xen(4)（man.freebsd.org，curl 直取 4,300 B，`format=ascii` 变体，逐字可靠）
- **数据库**：新建 ref（2026-11-18 G4-P2 批 b025；`man.freebsd.org/cgi/man.cgi?query=xen` 域内无同 URL 条目）
- **source_url**：<https://man.freebsd.org/cgi/man.cgi?query=xen&sektion=4>
- **quote（逐字，两句连读；行内多空格归一）**：

  > FreeBSD supports running both as a Xen guest and host on amd64 hardware. Guest support is limited to HVM and PVH modes, while host support is limited to PVH mode only.

- **考据注**：用于**Xen 以半虚拟化接口接入、接入层改变内核的启动与设备模型**（3.4.1）。官方手册定义 FreeBSD 对 Xen 的接入面：guest（被虚拟化侧）与 host（提供虚拟化侧）双角色，且 guest 限 HVM／PVH、host 限 PVH——**接入模式即接入层形态**，HVM（硬件辅助）与 PVH（含 PV 要素的硬件辅助）的分野决定内核启动路径与设备模型的适配面；PVH-only 的 host 侧自述亦载明接入面随代际收窄。
- **限度**：①手册载现时支持面（FreeBSD 15 语境），早期 Xen PV 接入的历史形态另有出处面；②“启动与设备模型适配面”的展开属编纂论旨，本句只证接入模式的官方定义。
- **本批落点**：V37.3.4.1
- **考据日期**：2026-11-18（Task 8.2 G4-P2 批 b025；official_doc／L3）
