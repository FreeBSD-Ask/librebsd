---
chapter: 第 233 章
id: CH233
volume: 第11卷-dragonflybsd的历史
---

# 第 233 章 dragonflybsd的技术遗产lwkthammer与vkernels

## 要点

- LWKT 的并行化核心依赖两大机制——每 CPU 独立调度队列与 IPI（Inter-Processor Interrupt）消息传递。每 CPU 独立调度队列让每个 CPU 拥有自己的 LWKT 线程队列与调度器，线程默认在本地 CPU 上调度执行，避免跨 CPU 的锁竞争；IPI 消息传递让 CPU 间通信通过中断消息而非共享变量完成，发送方 CPU 向目标 CPU 发送 IPI 消息，目标 CPU 收到消息后将其投入本地队列处理
- HAMMER1 的核心差异化特性是细粒度历史保留与近实时镜像——文件系统状态可按 30-60 秒边界在线访问而无需显式快照（可达配置的细粒度保留时间），粗粒度历史由快照控制（系统 cron 默认每日生成一个快照并保留 60 天）。DragonFly 官方 HAMMER 设计页面（dragonflybsd.org/hammer/）明确记载 HAMMER1 提供“即时崩溃恢复（无 fsck）、多卷文件系统、即时快照与历史版本保留”等特性
- vkernel 是 DragonFly 独有的“用户态运行完整内核”机制——允许在用户空间运行一个完整的 DragonFly 内核实例，基于 LWKT 的消息传递架构实现，是 Dillon“内核即进程”理念的工程化产物。vkernel 不模拟硬件设备（直接复用宿主机 syscall 接口）、不运行其他操作系统（仅运行 DragonFly）、不依赖硬件虚拟化扩展（VT-x/AMD-V），与同期 Xen 等虚拟化方案走的是不同的技术路线
- **dragonfly.duckdb** dragonfly-src 仓库 contributors 表显示 DragonFly 核心贡献者谱系——Matthew Dillon（马修·狄龙）（合并 <dillon@dragonflybsd.org>/dillon@apollo.backplane.com/dillon@backplane.com 等邮箱，10666 条 commit，2003-06-17 至 2026-06-10，创始人与单一决策核心）
- **dragonfly.duckdb** dragonfly-src 仓库 contributors 表显示 DragonFly 核心贡献者高度国际化——德国：Sascha Wildner（<saw@online.de>，10846 条，2004-12-17 至 2026-05-21）、Joerg Sonnenberger（<joerg@dragonflybsd.org>，2038 条，2004-01-07 至 2008-08-19，早期 release engineer，2008 年后转向 NetBSD）等

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4116] 卷“第11卷-dragonflybsd的历史”第 233 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充

## 史观

- 多方平等：DragonFly 的 ports 维护者与内核开发者在本体论层面平等

## 辨析

- DragonFly 160 位贡献者中，dports 提交量（606813）远超 src（49379），需区分‘ports 维护者’与‘内核开发者’

## 文献

- [DB:references_fulltext] 参考文献全文数据库（4077 篇全文，27138 条时间线事件）—— 对应 **dragonfly.duckdb**