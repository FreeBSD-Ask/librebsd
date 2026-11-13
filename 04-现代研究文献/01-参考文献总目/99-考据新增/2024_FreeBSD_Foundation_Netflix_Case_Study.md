# Maintaining the World’s Fastest Content Delivery Network at Netflix on FreeBSD（FreeBSD Foundation 案例）引用卡

> 用途：V71.3.1／3.2／3.5／3.6 内容补证（G8-S2 V71 b020 起）。

## 一、著录

FreeBSD Foundation. Maintaining the World’s Fastest Content Delivery Network at Netflix on FreeBSD[EB/OL]. FreeBSD Foundation, 2024-11-01[2026-11-13]. https://freebsdfoundation.org/end-user-stories/netflix-case-study/.

- 责任者：FreeBSD Foundation（项目基金会官方用户故事）
- 载体：HTML 案例页（含 Gallatin 受访引语）；`source_tier=primary`（基金会官方出版物）
- 访问日：2026-11-13
- 说明：案例记 Netflix 采用 FreeBSD-CURRENT 的动因、KTLS 改造与吞吐成果；引文照录。

## 二、逐字引文（英文，未翻译）

采用 CURRENT 的动因：

> Netflix adopted FreeBSD-CURRENT for its Open Connect CDN, aligning closely with the FreeBSD community and staying at the forefront of system development.

带宽瓶颈与成果（Gallatin 受访引语）：

> With sendfile and kernel TLS, we can eliminate many of these memory bandwidth bottlenecks, and now things become much more possible. By accounting for bandwidth and CPU utilization, we get about 375 gigs at about 53% busy CPU with FreeBSD.

首个 100G 生产 CDN 服务器：

> We had the first 100 gigabit per second production CDN server in the world

内核 TLS 的动机：

> We moved bulk crypto into the kernel (from nginx) to preserve the sendfile pipeline.

KTLS 后的吞吐口径：

> It allows for efficient data handling and has enabled Netflix to achieve 400 Gb/s throughput on its CDN servers.

## 三、考据说明

- “adopted FreeBSD-CURRENT”支撑 3.1.1／3.4：系统被纳入自建的发布节奏，而非外部发行版。
- Gallatin 引语为受访原话，属当事人一手材料（**L4**）；“375 gigs at about 53% busy CPU”“400 Gb/s”为厂商自述口径，不与 FTN 类第三方审计混用，“the first…in the world”属宣传性断言，不作事实引用。
- “moved bulk crypto into the kernel…to preserve the sendfile pipeline”是 3.6“性能优化与上游合并”的机制句。
