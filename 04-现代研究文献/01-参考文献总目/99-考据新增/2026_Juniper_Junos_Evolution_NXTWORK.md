# Junos Evolution（Juniper NXTWORK 会议材料）引用卡

> 用途：V71.1.3.2“两代 Junos 的架构分岔”、V71.1.3.5“控制平面基底的更替代价”内容补证（G8-S2 V71 b001）。

## 一、著录

Wright, Allison. Junos Evolution[EB/OL]. Juniper Networks, （日期不详）[2026-11-12]. https://www.juniper.net/assets/us/en/local/pdf/nxtwork/junos-evo.pdf.

- 责任者：Allison Wright（Juniper Networks；NXTWORK 会议材料署名页）
- 载体：PDF（会议演示文稿，14 页）；`source_tier=primary`（厂商一线架构材料）
- 访问日：2026-11-12
- 说明：幻灯片为要点体，引文按页内要点逐行照录；无固定出版日期（NXTWORK 年度会议材料）。

## 二、逐字引文（英文，未翻译）

“Linux as base OS”要点列：

> Linux as base OS • Leverage wide support and vast developer base. • Use open source tools wherever possible. • Support standard Linux tools • Native Linux applications

“Remove state from kernel”要点列：

> Remove state from kernel • No kernel state repository and state propagation. • Minimize changes to kernel. • Separate logic from state

“Modularity”要点列：

> Modularity • Formalized interfaces between components. • Pub-sub communication between components • Clear separation / fault isolation between components. • Lego blocks to support different use cases. • Support component upgrade without system reboot.

架构图构件：

> Key Constructs • Linux Kernel • Pub-sub state system • RPD • MGD • Fabric • Platform • PFE • ASIC

## 三、考据说明

- “Remove state from kernel”与“Minimize changes to kernel”直接对应 1.3.5“更替代价”官方一侧：收益（生态与工具）明示，代价以“尽量少改内核”反向可见——该页是唯一把设计取向写成要点的官方材料。
- “Lego blocks／Support component upgrade without system reboot”对应 1.3.2 的组件化与不停机升级表述，与 Overview 页“Applications can be individually restarted without requiring a system reboot”互为两文献。
- 会议材料属厂商宣传口径，按 L3 采信；“Lego blocks”一类比喻不进入 claim 正文。
