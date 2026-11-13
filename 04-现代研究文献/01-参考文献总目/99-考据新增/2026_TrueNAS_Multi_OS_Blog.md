# TrueNAS is Multi-OS（iXsystems 官方博客）引用卡

> 用途：V71.2.6.1／2.6.2／2.6.5 内容补证（G8-S2 V71 b005）；b007 补录 2.8.1／2.8.2／2.8.3／2.8.5 引文段。

## 一、著录

TrueNAS Team. TrueNAS is Multi-OS[EB/OL]. iXsystems, 2020-06-09[2026-11-13]. https://www.truenas.com/blog/truenas-multi-os/.

- 责任者：TrueNAS Team（iXsystems 官方博客）
- 载体：HTML 博客；`source_tier=primary`（厂商官方博客，机构自述）
- 访问日：2026-11-13
- 说明：博客交代 FreeNAS→TrueNAS 更名、FreeBSD 12.0 基线与 SCALE 立项；引文照录。

## 二、逐字引文（英文，未翻译）

更名与两档结构：

> we have decided to unify FreeNAS & TrueNAS into a single software image and brand: TrueNAS Open Storage. With the release of Version 12.0, what was previously called FreeNAS will now be TrueNAS CORE. What was formerly TrueNAS will now be TrueNAS Enterprise.

FreeBSD 12.0 基线与后续路线：

> Both of these TrueNAS editions use FreeBSD 12.0 as the base OS and it has been performing very well. Future development for these editions will continue on FreeBSD.

许可取向：

> FreeBSD is a well-structured OS with our preferred BSD license. It integrates well with ZFS and is well suited to the Open Storage business model that TrueNAS uses.

SCALE 的立项理由：

> The goals of this project include running Linux containers and building scale-out clustered storage. Because of these project goals, we chose Linux (Debian) as the base OS so that we had access to all of these container and clustering tools and could deliver a well-integrated user experience in a reasonable timeframe.

多 OS 宣告：

> So, TrueNAS is now officially multi-OS.

三版共用比例（b007 补录）：

> What developers will find is that apart from the OS, over 90% of TrueNAS software is shared between the CORE, Enterprise, and SCALE editions.

中间件系统无关化（b007 补录）：

> Middleware was updated to be OS independent and have clean REST and Web sockets APIs.

OpenZFS 2.0 整合与池迁移（b007 补录）：

> OpenZFS 2.0 integration of FreeBSD and Linux so that data and pools could be migrated easily between OSes.

上游组件协作（b007 补录）：

> Collaboration with Open Source component projects like Samba and rclone to ensure we would have portability of key components.

## 三、考据说明

- “preferred BSD license”是 2.6.5“许可取向”的直接表述；厂商自述，按 L3 采信。
- “Both of these TrueNAS editions use FreeBSD 12.0”把 CORE／Enterprise 两档与同一基线绑定，支撑 2.6.1、2.6.2。
- “chose Linux (Debian) as the base OS”是 2.7.2 底座重选的动机原文；本批仅取 2.6 线，2.7.2 留后续批。
- b007 补录：“over 90%…is shared”是 2.8.1“软件共用比例”的直接原文；“Middleware…OS independent”是 2.8.2“系统无关层”的原文；“OpenZFS 2.0 integration…migrated easily between OSes”是 2.8.3“池迁移前提”的前提句；“Collaboration with Open Source component projects”是 2.8.5“上游分担”的原文。
