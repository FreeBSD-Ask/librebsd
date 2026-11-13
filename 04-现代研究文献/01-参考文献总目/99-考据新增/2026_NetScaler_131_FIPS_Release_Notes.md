# Release Notes for NetScaler 13.1-37.232 FIPS Build 引用卡

> 用途：V71.1.5.4“内核接口在设备内的约束”内容补证（G8-S2 V71 b003）。

## 一、著录

Citrix Systems. Release Notes for NetScaler 13.1-37.232 FIPS Build[EB/OL]. Citrix Systems, （日期不详）[2026-11-12]. https://www.citrix.com/content/dam/citrix/en_us/documents/downloads/netscaler-adc/release-notes-13-1-37-232.html.

- 责任者：Citrix Systems（厂商发行说明）
- 载体：HTML 发行说明；`source_tier=primary`（厂商官方发行说明）
- 访问日：2026-11-12
- 说明：Platform 小节记内核时钟与定时器行为的对齐；引文照录原文（含原文语法）。

## 二、逐字引文（英文，未翻译）

Platform 小节条目 NSPLAT-26973：

> Synchronize timer behavior in FreeBSD 11.4 and FreeBSD 8.4 The kernel clock and timer events in FreeBSD 11.4 is made similar to that of the FreeBSD 8.4 to achieve stability in the NetScaler VPX platform.

## 三、考据说明

- 该条说明设备把 FreeBSD 11.4 的内核时钟与定时器行为回改为接近 8.4，以维持平台稳定性——即“内核接口在设备内的约束”的实证：内核行为被设备需求反向固定。
- 条目限定 “NetScaler VPX platform”，不外推到 MPX 或其他形态。
- 按 L3 采信；发行说明为厂商自述。
