# Migrating from CORE（TrueNAS 官方文档）引用卡

> 用途：V71.2.7.4／2.7.5 内容补证（G8-S2 V71 b005）。

## 一、著录

TrueNAS. Migrating from CORE[EB/OL]. TrueNAS Documentation Hub, 2025-05-27[2026-11-13]. https://www.truenas.com/docs/scale/gettingstarted/migrate/.

- 责任者：TrueNAS（iXsystems 官方文档）
- 载体：HTML 文档页；`source_tier=primary`（厂商官方文档）
- 访问日：2026-11-13
- 说明：页面记 CORE 进入 sustaining engineering 与迁移路径；引文照录。

## 二、逐字引文（英文，未翻译）

维护期起点：

> On March 20, 2024, the TrueNAS team announced that the FreeBSD-based TrueNAS CORE platform has entered “sustaining engineering phase within the TrueNAS project.” With this transition, TrueNAS 13.0 continues to receive bug fixes related to stability and security. New feature development and component improvement continues on Linux-based TrueNAS versions.

末版：

> TrueNAS 13.3-U1.2, released April 29, 2025, is the final release for the TrueNAS CORE 13.3 software train.

侧移以数据保留为前提：

> Users looking for new feature development can sidegrade to the Linux-based TrueNAS platform at any time, preserving data and essential NAS functionality.

迁移路径与净装要求：

> TrueNAS users wanting to migrate from the latest FreeBSD-based 13.0 or 13.3 CORE release to the Linux-based TrueNAS version 24.10 or later can migrate to 24.04 and earlier using the UI update process, but must clean install if migrating to later releases. Attempting to migrate directly to 24.10 or later using the UI is not supported.

## 三、考据说明

- 维护期起点与末版两句是 2.7.5“CORE 维护期的收束”的直接证据（只保留稳定性与安全修复、13.3 系列终止）。
- 迁移路径句是 2.7.4 的操作侧证据：UI 更新仅到 24.04 及更早，24.10 及以后须净装，直接 UI 迁移不受支持。
- 按 L3 采信；官方文档。
