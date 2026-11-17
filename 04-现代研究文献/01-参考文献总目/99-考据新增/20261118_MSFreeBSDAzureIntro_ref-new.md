# 《Introduction to FreeBSD on Azure》（新 ref）引用卡

- **性质**：Microsoft Learn 官方文档（learn.microsoft.com）Azure Virtual Machines 之 FreeBSD 简介页；web_reader 实取 2026-11-18，页面 updated_at 2025-07-02（ms.date 2017-09-13）
- **数据库**：新建 ref（2026-11-18 Task 8.2 V71—V75 线 supp-V71-b032；source_url 四键查重无重合）
- **source_url**：https://learn.microsoft.com/en-us/azure/virtual-machines/linux/freebsd-intro-on-azure
- **quote（逐字）**：Microsoft is making images of FreeBSD available on Azure with the Azure VM Guest Agent preconfigured. Currently, the following FreeBSD versions are offered as images by Microsoft: FreeBSD 10.4 in Azure Marketplace / FreeBSD 11.2 in Azure Marketplace / FreeBSD 11.3 in Azure Marketplace / FreeBSD 12.0 in Azure Marketplace。另句：They're offered as images by the FreeBSD Foundation: FreeBSD 11.4 in Azure Marketplace / FreeBSD 12.2 in Azure Marketplace / FreeBSD 13.0 in Azure Marketplace。另句：As for future versions of FreeBSD, the strategy is to stay current and make the latest releases available shortly after they're published by the FreeBSD release engineering team.
- **考据注**：三句分别支撑 V71.3.10.1（同一 Marketplace 内 Microsoft 自制镜像与 FreeBSD Foundation 发布镜像两渠道并存）、V71.3.10.4（维护责任在厂商与项目方之间按版本分配：10.4—12.0 归 Microsoft、11.4—13.0 归 Foundation）、V71.3.10.5（跟进策略句；该页版本清单止于 13.0，页面 2025-07 更新时仍未列 14.x／15.x，滞后现状两页对照见 ref10986 的 15.1 在列）。Agent 负责 VM 首次启用的 provisioning（用户名、密码或 SSH key、主机名），可作 3.10.2 初始化方式的旁证，本批未取
- **本批落点**：V71.3.10.1 第 1 块／V71.3.10.4 第 2 块／V71.3.10.5 第 1 块
- **考据日期**：2026-11-18（Task 8.2 V71—V75 线 supp-V71-b032；official_doc／L3）
