# Top Differences Between Junos OS Evolved and Junos OS（Juniper Networks 官方文档）引用卡

> 用途：V71.1.3.1／1.3.2／1.3.3／1.3.4 内容补证（G8-S2 V71 b001）。

## 一、著录

Juniper Networks. Top Differences Between Junos OS Evolved and Junos OS[EB/OL]. Juniper Networks, （日期不详）[2026-11-12]. https://www.juniper.net/documentation/us/en/software/junos/overview-evo/topics/concept/evo-top-differences.html.

- 责任者：Juniper Networks（厂商官方技术文档）
- 载体：HTML 页面；`source_tier=primary`（厂商官方文档，机构自述）
- 访问日：2026-11-12
- 说明：页面设“System Differences／Software Structure／State Model／Software Management／Management Interfaces”等对照小节；引文照录英文原文，折行按行合并。

## 二、逐字引文（英文，未翻译）

内核对界：

> Junos OS Evolved is built on top of a Linux kernel, while Junos OS operates on the FreeBSD kernel.

系统模型（路由引擎中心 vs 节点）：

> Junos OS uses a Routing Engine centric model, where system usually refers to a Routing Engine. However, Junos OS Evolved uses a node-based model, where system refers to all nodes, including Routing Engines, Flexible PIC Concentrators (FPCs), and more.

节点定义：

> In Junos OS Evolved, a node is any component that can run the Linux kernel and Junos OS Evolved applications, and all nodes are considered compute nodes.

状态模型：

> Junos OS Evolved uses a distributed state infrastructure. Applications publish or subscribe to state objects, which are stored in a state database called the Distributed Data Store (DDS) that is distributed across nodes. By comparison, Junos OS processes store state internally, exchanging state information and state changes with other processes through the kernel.

网络栈呈现差异：

> Junos OS Evolved runs on native Linux. There are some differences between the way Linux displays requested network topology information, such as interface and route data, and the way Junos OS displays this information. The Junos OS Evolved CLI is designed to overcome these differences.

Netfilter 限制：

> In Junos OS Evolved, management filtering uses Routing Engine filters based on Netfilter, a framework that the Linux kernel provides. As a result, only certain matches and actions are supported.

## 三、考据说明

- 本页是 1.3.2“架构分岔”与 1.3.3“节点模型”的主来源：系统单位、状态存放位置、应用管理方式三处均逐条对照。
- 1.3.4 的两条支撑分别取“CLI 克服 Linux 呈现差异”与“Netfilter 过滤器仅支持部分匹配与动作”，前者与《Managing Third-Party Applications》页的 intercept 机制互为两文献。
- 页面属厂商自述，按 L3 采信；“only certain matches and actions” 为官方明确的限制表述，可直引。
