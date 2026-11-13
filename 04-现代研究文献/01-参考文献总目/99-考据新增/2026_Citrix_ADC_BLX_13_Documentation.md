# Citrix ADC BLX 13.0 产品文档（官方）引用卡

> 用途：V71.1.4.2“应用交付控制器的系统层”内容补证（G8-S2 V71 b002）。

## 一、著录

Citrix Systems. Citrix ADC BLX 13.0: Product Documentation[R/OL]. Citrix Systems, 2025-03-10[2026-11-12]. https://docs.netscaler.com/content/dam/netscaler/us/en/legacy-archive/downloads/citrix-adc-blx-13.pdf.

- 责任者：Citrix Systems（厂商产品文档）
- 载体：PDF（产品文档汇编）；`source_tier=primary`（厂商官方文档）
- 访问日：2026-11-12
- 说明：PDF 抽取文本保留原有断词连字符（如 inter‑faces）；引文只取不断词的完整句段。

## 二、逐字引文（英文，未翻译）

用户空间应用与主机驱动：

> A BLX appliance runs as a user space application in a Linux system. The BLX appliance uses the Linux drivers for Rx/Tx of packets and managing the NIC ports.

内核与应用间的虚拟接口：

> which are created during the BLX boot up phase, are used for communication between the kernel and the BLX appliance.

## 三、考据说明

- 与 14.1 的《General architecture》页构成同一命题的两份独立产品文档（13.0 与 14.1），用于 1.4.2 的双源互证。
- 该 PDF 明确“user space application＋Linux 驱动管收发与网卡”，与“系统层由主机承担”的判断一致；同时保留“自带协议栈”的边界（见 14.1 架构页）。
- 按 L3 采信。
