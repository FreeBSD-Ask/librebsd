# Juniper Junos 官方页与 HardenedBSD 状态报告引用卡（ref 新建四件）

- **性质**：Juniper 官方文档两页（Junos 架构与概述）、Juniper Day One 官方书 PDF、HardenedBSD 2026 年 5 月状态报告——4.4.3 信任链双源补强与 5.1 节 Junos 面的一手表述
- **取件**（curl 直取 2026-11-23）：https://www.juniper.net/documentation/us/en/software/junos/junos-install-upgrade/topics/topic-map/junos-os-overview.html（18 718 B）＋https://www.juniper.net/documentation/us/en/software/junos/junos-overview/topics/concept/junos-software-architecture.html（12 124 B）＋https://hardenedbsd.org/article/shawn-webb/2026-06-01/hardenedbsd-may-2026-status-report（24 698 B）＋https://www.juniper.net/documentation/us/en/internal/day-one-books-archive/DayOne_vMX.pdf（PDF 文本层经 exa 抓取，卡式 D2 引用）
- **overview 句（V57.5.1.1 A 块）**：Junos OS FreeBSD 10 or later on bare metal. This is Junos OS based on an upgraded FreeBSD kernel. Most Junos OS-based hardware platforms run Junos OS with upgraded FreeBSD.
- **vMX Day One 句（V57.5.1.1 B 块；PDF 文本层"Free BSD"空格照录、卡注披露）**：As Junos is based on FreeBSD, the VCP VM is actually running Free BSD. The VCP is analogous to the RE in the physical MX.
- **architecture 句一（V57.5.1.2 A 块）**：Because this architecture separates control operations such as routing updates and system management from packet forwarding, the router can deliver superior performance and highly reliable Internet operation.
- **vMX Day One 句二（V57.5.1.2 B 块）**：Junos OS was the first network OS to introduce a clear separation between control and forwarding planes.
- **HardenedBSD May 2026 report 句（V57.4.4.3 B 块）**：I am working on a candidate patch to our build scripts to perform this export. The archives exported by our builder VMs will be signed with our normal ssh key-based signing method.
- **口径**：Juniper 两页为厂商官方文档（L3 official）；Day One 书为 Juniper 官方出版物（PDF 文本层抽取、vMX 面"Free BSD"空格系 PDF 文本层形态照录）；HardenedBSD May 2026 状态报告与 README Verifying Build Artifacts 节为**异文**（前者谈 Radicle 导出签名方法、后者谈构建产物验证步骤）——4.4.3 双源自此成立（J52 同发布者两份文档双源对照）。
- **考据日期**：2026-11-23
