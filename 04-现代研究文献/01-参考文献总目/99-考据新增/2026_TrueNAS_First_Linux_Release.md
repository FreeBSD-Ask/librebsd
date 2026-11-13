# First Official RELEASE of TrueNAS on Linux（iXsystems 官方博客）引用卡

> 用途：V71.2.6.5 内容补证（G8-S2 V71 b005）；b007 补录 2.8.1／2.8.2／2.8.3／2.8.5 引文段。

## 一、著录

Soteros, Will. First Official RELEASE of TrueNAS on Linux![EB/OL]. iXsystems, 2022-02-22[2026-11-13]. https://www.truenas.com/blog/first-release-of-truenas-on-linux/.

- 责任者：Will Soteros（iXsystems 官方博客）
- 载体：HTML 博客；`source_tier=primary`（厂商官方博客）
- 访问日：2026-11-13
- 说明：博客宣布 SCALE 22.02.0 首发，记双底座与 OpenZFS 2.0；引文照录。

## 二、逐字引文（英文，未翻译）

双底座与开源定位：

> For the first time, TrueNAS, the most widely deployed Open Source Software-Defined Storage, is now officially available on both FreeBSD (TrueNAS CORE & TrueNAS Enterprise) and Linux with TrueNAS SCALE.

OpenZFS 2.0 与数据迁移：

> OpenZFS 2.0: The inclusion of FreeBSD and Linux as a thoroughly tested peer in OpenZFS enabled the migration of data between TrueNAS CORE to TrueNAS SCALE. Both the development and testing processes were contributed by iXsystems.

中间件跨底座移植：

> This allowed the TrueNAS middleware to be ported between both OS’s, with the goal of eventually supporting existing TrueNAS features atop a Linux base to unlock several Linux-specific capabilities, including Docker Containers, Kubernetes, KVM, and also Scale-out ZFS through the gluster file system.

全套工具随两底座提供（b007 补录）：

> All of the excellent TrueNAS tools like OpenZFS, Snapshots, Replication, REST APIs, WebUI, Samba with Windows ACLs, High Availability, Enclosure Management, and Single-click software updates are now joined by the standard Linux toolchain and a familiar Debian Linux system environment.

OpenZFS 2.0 双主 OS 起点（b007 补录）：

> The journey started with iXsystems contributions in promoting the combination of both Linux and FreeBSD as the primary OSes for OpenZFS 2.0.

数百开发年的集体投入（b007 补录）：

> While many applications port easily from FreeBSD to Linux, TrueNAS leverages many OS tools to provide an appliance-like experience. Adding a new OS, integrating it effectively, and then making sure it is rock solid and reliable is no small feat. The iXsystems engineering team and the many TrueNAS Community contributors and testers have collectively spent hundreds of development years making this release possible.

## 三、考据说明

- “most widely deployed Open Source Software-Defined Storage… on both FreeBSD… and Linux”是 2.6.5“许可／开源取向”的第二来源（与 Multi-OS 博客的“preferred BSD license”互证）。
- 末句“enabled the migration of data between CORE to SCALE”是 2.8.3“数据池迁移技术前提”的预备证据，留后续批使用。
- 按 L3 采信；厂商博客，宣传口径。
- b007 补录：“All of the excellent TrueNAS tools…”印证共用面覆盖核心功能清单（2.8.1-B）；“The journey started with…primary OSes for OpenZFS 2.0”是中间件移植的工程起点（2.8.2-B）；“hundreds of development years”是底座更换代价的厂商与社区分担口径（2.8.5-A）。
