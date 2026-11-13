# General architecture | About NetScaler BLX（官方文档）引用卡

> 用途：V71.1.4.2“应用交付控制器的系统层”内容补证（G8-S2 V71 b002）。

## 一、著录

NetScaler (Cloud Software Group). General architecture | About NetScaler BLX[EB/OL]. NetScaler Docs, 2026[2026-11-12]. https://docs.netscaler.com/us/en/blx/current-release/about-netscaler-blx/architecture-blx.html.

- 责任者：NetScaler（Cloud Software Group 产品文档）
- 载体：HTML 技术文档；`source_tier=primary`（厂商官方文档）
- 访问日：2026-11-12
- 说明：页面记 BLX 在 Linux 主机上的运行形态、驱动与接口使用；引文照录英文原文。

## 二、逐字引文（英文，未翻译）

用户空间应用与主机驱动：

> NetScaler BLX is a software form factor of NetScaler and provides the same functionality as other form factors. It runs as a user space application on a Linux host.

> NetScaler BLX uses the Linux drivers for Rx/Tx of packets and for managing the NIC ports.

日志经主机 syslog：

> Virtual Ethernet (veths) interfaces blx0 and blx1, created during the boot‑up phase, are used for communication between the Linux host and NetScaler BLX. For example, NetScaler BLX uses veths to send log information to the syslog daemon on a Linux Host.

自带协议栈、绕过内核栈：

> It has a full-fledged TCP/IP stack to process the packets, bypassing the TCP/IP stack of the Linux kernel. NetScaler BLX interacts directly with the Linux kernel driver to pick the raw packets from the NIC ports.

## 三、考据说明

- “日志／网卡管理交由主机 OS 承担、应用本体只处理业务功能”构成 1.4.2 题面“系统层与功能层分开”的技术依据。
- “自带 TCP/IP 栈、绕过 Linux 内核栈”说明功能层并未整体交给主机——题面“分开”不等于“全托管”，落块时保留此边界。
- 按 L3 采信；厂商文档。
