# Junos OS Evolved Overview（Juniper Networks 官方文档）引用卡

> 用途：V71.1.3.1“Junos OS Evolved 的 Linux 底座”、V71.1.3.3“节点模型对路由引擎模型的替代”内容补证（G8-S2 V71 b001）。

## 一、著录

Juniper Networks. Junos OS Evolved Overview[EB/OL]. Juniper Networks, （日期不详）[2026-11-12]. https://www.juniper.net/documentation/us/en/software/junos/junos-install-upgrade-evo/overview-evo/topics/concept/evo-overview.html.

- 责任者：Juniper Networks（厂商官方技术文档）
- 载体：HTML 页面；`source_tier=primary`（厂商官方文档，机构自述）
- 访问日：2026-11-12
- 说明：页面随产品版本滚动更新，无固定出版日期；引文照录英文原文，折行按行合并为单空格，未改词。

## 二、逐字引文（英文，未翻译）

原生 Linux 底座：

> Whereas Junos OS runs over an instance of the FreeBSD operating system on a specific hardware element (for example, the CPU on the Routing Engine), Junos OS Evolved runs over a native Linux system.

横向软件层与算力资源池：

> The Junos OS Evolved infrastructure is a horizontal software layer that decouples the application processes from the hardware on which the processes run.

> Effectively, this decoupling creates a general-purpose software infrastructure spanning all the different compute resources on the system (Routing Engine CPUs, line card CPUs, and possibly others).

状态数据库与组件化：

> In Junos OS Evolved, state can be held in a database called the Distributed Data Store (DDS).

> Junos OS Evolved is composed of components with well-defined interfaces. Applications can be individually restarted without requiring a system reboot.

## 三、考据说明

- 该页在“Native Linux Base”小节直接对照两代系统基底，是 1.3.1 题面的第一来源。
- “横向软件层跨越路由引擎 CPU 与线卡 CPU”为 1.3.3 节点模型的官方表述来源之一；与《Top Differences》页的 node-based model 表述互为两文献。
- DDS 与组件化表述用于 1.3.2 架构分岔的状态模型一侧。
- 页面为厂商自述，按 L3 采信；涉及“更优／更快”一类评价性措辞不入 claim。
