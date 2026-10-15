---
chapter: 第 178 章
id: CH178
volume: 第09卷-netbsd的历史
---

# 第 178 章 netbsd-4.0的发布与嵌入式生态

## 要点

- NetBSD 提交高峰期：2004年(121291次)，对应 4.0 嵌入式生态扩展期

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3997] 卷“第09卷-netbsd的历史”第 178 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_4008] 卷“第09卷-netbsd的历史”第 178 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

- [DB:code_repos:netbsd.duckdb] NetBSD 提交高峰期：2004年(121291次)，对应 4.0 嵌入式生态扩展期

## 史观

- 循环而非进步：NetBSD 4.0 的嵌入式生态扩展不是线性进步，而是对早期可移植理想的循环性回归

## 辨析

- SMP 锁设计的具体实现需考据——细粒度锁的具体范围需对照源码 diff 核实。经 netbsd.duckdb netbsd-src 仓库 branches 表验证：origin/netbsd-4-0 branch commit_date = 2012-11-14T20:26:54Z，远晚于 NetBSD 官方公告 4.0 发布日期 2007.12.19（约 4 年 11 个月），印证 branches
- NetBSD 官方“Where NetBSD is used”列表的完整性存疑——部分早期部署已停止维护或厂商已倒闭；列表更新滞后，部分 2010 年代仍在运行的部署未及时记录
- 公告数量在不同来源中存在差异——NetBSD 官方页面与 security mailing list archive 的统计可能略有出入；部分公告涉及第三方软件（如 Apache、OpenSSH）而非 NetBSD 本身，需区分
- USPTO TESS 与 WIPO 记录在商标类别描述上可能略有差异——需对照原始申请文件核验；NetBSD 商标在多国注册的具体清单在 Foundation 文档中可能不完整
- NetBSD 蓝牙栈与 FreeBSD Netgraph-based Bluetooth 在设计上类似（均采用节点图抽象）但代码独立；与 Linux BlueZ 的关键差异——BlueZ 采用传统协议栈实现，NetBSD 蓝牙栈采用 Netgraph 节点图；macOS IOBluetooth 是 Apple 私有框架，与 BSD/Linux 蓝牙栈无源码关系；〔待核：原文截断，后文待回源〕

## 文献

- [DB:references_fulltext] 参考文献全文数据库（4077 篇全文，27138 条时间线事件）—— 对应 netbsd.duckdb

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-231 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-231`；w172 YouTube 章节路由采纳）

据〔Rump Device Drivers 演讲〕讲者口述：讲者指出 rump 在内核设备驱动场景并非总能适用，而他自己工作站的实际运行版本是 NetBSD 5。（YouTube EP3AJNxa33pzk，[409.8-413.95]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->
