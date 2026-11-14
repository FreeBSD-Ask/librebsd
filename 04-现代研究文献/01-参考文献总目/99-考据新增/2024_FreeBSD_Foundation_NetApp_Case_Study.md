# FreeBSD provides Flexibility and Performance for NetApp’s ONTAP（FreeBSD Foundation 案例研究）引用卡

> 用途：V71.2.1.3／2.3.5 内容补证（G8-S2 V71 b016 起）。

## 一、著录

FreeBSD Foundation. FreeBSD provides Flexibility and Performance for NetApp’s ONTAP Data Management System[R/OL]. FreeBSD Foundation, 2024-03[2026-11-13]. https://freebsdfoundation.org/wp-content/uploads/2024/03/NetApp-CASE-STUDY-1-1.pdf.

- 责任者：FreeBSD Foundation（项目基金会官方案例研究）
- 载体：PDF 案例研究（3 页）；`source_tier=primary`（基金会官方出版物，含 NetApp 受访者引语）
- 访问日：2026-11-13
- 说明：案例研究记 NetApp 自 2004 年起以 FreeBSD 为 ONTAP 底座、许可考量、跟踪策略与上游贡献；引文照录，PDF 分栏断行按空白归一处理。

## 二、逐字引文（英文，未翻译）

许可模型考量：

> NetApp needed a licensing model to incorporate its proprietary technology into their new data management system without worrying about potential software licensing issues.

跟踪策略：

> In the past, NetApp used an older version of FreeBSD, but now it tracks closer to the current release (also known as “tracking head” within the FreeBSD Community).

上游贡献规模：

> NetApp has upstreamed nearly 300 changes

经第三方上游（b019 补录）：

> NetApp has partnered with Klara Systems for their commercial support and upstreams through Klara, as well.

上优先（upstream-first）纪律：

> Limit private customizations to business critical IP and upstream-first everything else.

版本沿革：

> from version 6.0 in 2004 to version 14.0 today, FreeBSD has remained a constant and up-to-date component in NetApp.

回馈渠道列举（b027 补录）：

> NetApp contributes to FreeBSD in many ways, including periodically hosting FreeBSD Foundation events, making regular bug fixes and enhancements, and providing financial support to the FreeBSD Foundation.

工程师上游回送新技术（b027 补录）：

> NetApp’s engineers have also upstreamed new technology to FreeBSD in the past, like bhyve, the BSD-licensed hypervisor

缺陷经 Klara 转报上游（b027 补录）：

> When the test encounters issues with FreeBSD, NetApp reports them through Klara, and Klara changes upstream.

选型声明与理由（b030 补录）：

> NetApp chose to base ONTAP on FreeBSD for its performance-focused BSD distribution and trust their use of FreeBSD due to inherent stability of FreeBSD releases along with support from other commercial FreeBSD users.

## 三、考据说明

- 许可考量句支撑 2.1.3“厂商选择 BSD 因许可与成熟度”的 NetApp 侧；“mature and proven”句由 OneFS 文档承担 Isilon 侧，两源互证。
- “tracks closer to the current release”与“upstream-first”是 2.3.5“厂商 fork 与主线选择性合并”的直接表述。
- 案例研究为基金会出版物，含受访者引语；按 L3 采信，受访者引语按当事人自述处理（非 L4 现场）。
- PDF 双栏断行处（“performance-driven”“A huge factor in that…decision”）不作整句引用，仅取跨行完好的句子。
- **现行入口（2026-11-14 实测）**：原 PDF 路径已 404，案例改以 HTML 活页载于 `https://freebsdfoundation.org/end-user-stories/netapp-case-study/`（200），b027 补录三条引文在新页逐字命中；库内 ref 10447 仍按原著录 URL 保留，不再另行改库。
