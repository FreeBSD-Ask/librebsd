# Dell PowerScale OneFS: Technical Overview — Overview（Dell Info Hub）引用卡

> 用途：V71.2.1.1／2.1.2／2.1.3／2.2.x 内容补证（G8-S2 V71 b016 起）。

## 一、著录

Dell Technologies. Dell PowerScale OneFS: Technical Overview — Overview[EB/OL]. Dell Technologies Info Hub, （日期不详）[2026-11-13]. https://infohub.delltechnologies.com/en-us/l/dell-powerscale-onefs-technical-overview/overview-3166/.

- 责任者：Dell Technologies（厂商官方技术文档库）
- 载体：HTML 技术概述页（同名白皮书的信息枢纽版）；`source_tier=primary`（厂商官方，机构自述）
- 访问日：2026-11-13
- 说明：页面逐版次更新（1.0 版 2013-11 至 15.0 版 2021-04，对应 OneFS 7.1–9.2）；引文照录。

## 二、逐字引文（英文，未翻译）

BSD 基底与语义支持：

> OneFS is built on a BSD-based UNIX operating system foundation. It supports both Linux/UNIX and Windows semantics natively, including hard links, delete-on-close, atomic rename, ACLs, and extended attributes.

选型理由：

> It uses BSD as its base operating system because it is a mature and proven operating system, and the open-source community can be leveraged for innovation.

底层系统版本对齐：

> From OneFS 8.2 onwards, the underlying operating system version is FreeBSD 11.

三层合一与底座的关系：

> OneFS combines the three layers of traditional storage architectures—file system, volume manager, and data protection—into one unified software layer, creating a single intelligent distributed file system that runs on a OneFS powered storage cluster.

操作系统与文件系统一体：

> OneFS is not only the operating system but also the underlying file system that drives and stores data in the cluster.

集群通信依赖后端网络（b017 补录）：

> All intra-node communication in a cluster is performed across a dedicated backend network, consisting of either 10 Gb, 40 Gb, 100 Gb, or 200 Gb Ethernet, or low-latency QDR Infiniband (IB).

维护窗口内的滚动升级（b017 补录）：

> For periodic system maintenance and software updates, this functionality allows for per-node rolling upgrades affording full-availability throughout the duration of the maintenance window.

## 三、考据说明

- “built on a BSD-based UNIX operating system foundation”＋“From OneFS 8.2 onwards… FreeBSD 11”直接支撑 2.1.1／2.1.2／2.2.3。
- 选型理由句（成熟、经检验、开源社区可借力）是 2.1.3“许可与成熟度”的厂商自述依据；该句未直接提“许可”二字，许可侧证据用 NetApp 案例互证。
- “三层合一”是功能层合并，运行在 BSD 基底之上——落块不得写成“BSD 被替换”。
- 白皮书 PDF 原件（cdn-prod.scdn6…a748.pdf）直连失败（276 字节），以 Info Hub 版文本为准。
- 按 L3 采信；厂商技术文档。
