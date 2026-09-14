---
chapter: 第 218 章
id: CH218
volume: 第11卷-dragonflybsd的历史
---

# 第 218 章 dragonflybsd早期演进的vkernel虚拟内核

## 要点

- Linux User Mode Linux (UML) 自 Linux 2.6.0（2003-12）起进入主线，与 vkernel 设计理念相似但实现不同——UML 通过 ptrace 拦截实现用户态内核，vkernel 基于 LWKT 消息传递架构实现。UML 在 Linux 2.6 系列后维护逐渐停滞（Linux 内核复杂度提升导致 UML 同步困难），vkernel 在 DragonFly
- userland 分化使 DragonFly 与 FreeBSD 之间的用户迁移成本增加——dragonfly.duckdb 显示两仓库 userland 目录 2010-2026 年间独立演进，用户迁移须重新学习命令行为与配置文件格式。但差异小于 FreeBSD 与 OpenBSD 之间的差异（OpenBSD 移除 config 语法、独立维护 openssl 替代品 LibreSSL 等），Dra
- dragonfly.duckdb 提供 DragonFly/FreeBSD/NetBSD/OpenBSD 四仓库同口径 commits/contributors/tags 表统计（dragonfly-src/freebsd-src/netbsd-src/openbsd-src），是跨项目比较的可靠数据来源。Linux 内核与 illumos 不在 openbsd.duckdb 范围内，须以各自官方仓库
- 要点**：DragonFly 2003 年 fork 事件的历史意义须以多元史观综合审视——以总纲第 5 条（偶然性）审视，fork 事件的偶然性体现于时点选择、跟帖措辞、基线选择等多个环节，但偶然性不否定 fork 事件的历史必然性（5.x 路线分歧已积累至临界点）；以总纲第 8 条（本体论平等）审视，Stacey/Kennaway 的负面话语、Core Team 的沉默、Dillon 的反批评、再批评的质疑，各方在本体论上地位平等，争议无须以“对错”二元裁决；以总纲第 13 条（法律与道德是利益分配）

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4035] 卷“第11卷-dragonflybsd的历史”第 218 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_4036] 卷“第11卷-dragonflybsd的历史”第 218 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- UML 与 vkernel 的比较须考虑内核架构差异——Linux 内核代码量数倍于 DragonFly 内核，UML 维护难度高于 vkernel 是客观事实；vkernel 在 DragonFly 中“更实用”的判断须以具体使用场景为准（开发调试 vs 生产部署），不得简单优劣判断；vkernel 性能与真硬件的具体差距 ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］. <https://kernelnewbies.org/LinuxVersions>；DragonFly vkernel 文档 [EB/OL]. <https://www.dragonflybsd.org/docs/>；UML 文档 [EB/OL]. <http://user-mode-linux.sourceforge.net/> ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,207 次提交。> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。
- dragonfly.duckdb dragonfly-src/freebsd-src/openbsd-src 仓库 commit_files 表（userland 目录文件变更对照）；DragonFly BSD mailing lists [EB/OL]. <https://www.dragonflybsd.org/mailinglists/>；FreeBSD mailing lists [EB/OL]. <https://lists.freebsd.org/archives/> ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2003-2026 年间：1,102,265 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- freebsd.duckdb dragonfly-src/freebsd-src/netbsd-src/openbsd-src 仓库 commits/contributors/tags 表（同口径统计对照）；Linux kernel repository [EB/OL]. <https://git.kernel.org/>；illumos repository [EB/OL]. <https://github.com/illumos/illumos-gate>；FreeBSD Foundation. Annual Reports [EB/OL]. <https://www.freebsdfoundation.org/our-donors/> ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,207 次提交。> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。
- 原材料/哲学/项目统摄史观/第 25 章.md（总纲第 13、19、21 条原文）；dragonfly.duckdb commits/contributors/tags/commit_files 表；DragonFly BSD Project. DragonFly BSD history [EB/OL]. <https://www.dragonflybsd.org/history/>；Dillon M. Annoucning DragonFly BSD! [EB/OL]. 2003-07-16. lists.freebsd.org/pipermail/freebsd-current/2003-July/006889.html ［A］FreeBSD 社区论文：[FP-2004-001] The Challenges of Dynamic Network Interfaces（Brooks Davis，2004）<https://papers.freebsd.org/2004/eurobsdcon/davis-challenges_of_dynamic_network_interfaces/>### 史观映射> Dillon 的 fork 是分离聚合律的又一次上演——从 FreeBSD 的躯体中分裂出去，带着 4.x 的基因走上一条独立的演化道路；DragonFly 在技术上令人尊敬，却始终无法撼动 FreeBSD 主线的惯性，技术优秀并不足以逆转生态的向心力；而 DragonFly 沿用 BSD 许可证这一事实，与其说是哲学选择不如说是法律基础的惯性延续——分裂可以改变代码的走向，却改变不了许可证的形式主义约束---

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,207 次提交。> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP93（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 受访的 DragonFly BSD 开发者（转写作 Sefi）自述其网络栈不以锁而以消息与线程串行化网络操作：每个 CPU 各有一个网络线程，路由表等数据按 CPU 复制，TCP 与 UDP 控制块分区存放，协议统计每 CPU 独立；用户态发包先送消息给本 CPU 网络线程完成协议处理再进入网卡，收包则按哈希选定线程处理，全路径避免锁争用。　[存疑脚注] 受访者姓名转写失真（写作 Sefi），依语义当为 DragonFly 网络栈开发者 Sepherosa Ziehau，引用前须核对节目页与会议日程。（BSD Now EP93，[1420.88-1501.40]，L1）
- 同一受访者将早期文献称线程串行化网络栈慢于锁方案的论断作了改判式溯源：DragonFly 曾观察到的高调度成本，其根因在同步消息的使用而与网络栈模型无关，改用异步消息后整个网络路径的流水线效应大增；同时承认该设计的代价是复制数据带来的内存占用，例如完整 BGP 路由表在 DragonFly 中更耗内存，但在内存廉价的时代此项代价已不关键。（BSD Now EP93，[1513.16-1650.48]，L1）
- 受访者介绍其对 SO_REUSEPORT 的扩展：允许各进程或线程在同一端口各自创建监听套接字，消除 accept 队列争用，并以与网络数据分区相同的哈希函数分发连接、顺带解决分布不均；dports 内打补丁的 nginx 由此获得显著性能提升，该补丁随后被 nginx 上游 1.9.1 版本接受。（BSD Now EP93，[1879.16-1964.95]，L1）
- 受访者报出一组实测基准：四千兆口下 IPv4 转发双向各约每秒五百万包、接近理论极限；双万兆口 TCP 吞吐双向 18 Gbps；启用 SO_REUSEPORT 后单万兆口 TCP 连接建立率由每秒约十万升至三十八万；UDP 请求响应每秒一百三十九万笔；nginx HTTP 测试受限于测试机数量，服务端 CPU 尚有大量空闲，留下扩展余量。（BSD Now EP93，[2080.92-2159.04]，L1）

**史料**：

- 本期可作史料线索者包括：BSDCan 2015 主题演讲预告中 Steven Bourne（转写作 Steven born）将亲述原始 sh 的编写与移植（SBRK、无字符串库时代）、其 Algol 68 移植并劝说 Dennis Ritchie 在 C 中引入 void、环境变量的发明缘由、Bill Joy 为何另写 C shell，并点评 Shellshock 类缺陷自 1990 年代初即潜伏而长期无人发现；另有 Brooks Davis 的 CherryBSD 报告（将 Capsicum 思想下沉至处理器硬件强制）、Robert Watson 与 George Neville-Neil 宣布开源其 FreeBSD 高级操作系统课程材料、以及 MeetBSD 上文件系统开发者当众销毁硬盘的录像。　[存疑脚注] 人名与专名转写多处失真（Steven born、Alargh 68、Matthew Dylan 等），引用前须比对 BSDCan 2015 官方日程与会议实录。（BSD Now EP93，[145.94-252.12]，L2）

**史观**：

- 总纲4 分离聚合是永恒规律：讨论段把权限分离、chroot、jail 与 Capsicum 排成一条递进谱系：目录围栏式的 chroot 聚合出带独立命名空间的 jail，jail 的整机级隔离又分离出按二进制收权的能力沙箱；每一代手段既修补前代的漏洞，也被下一代重新拆解，呈现分离与聚合的循环往复，而非单向的安全进步。（BSD Now EP93，[2762.20-2816.42]，L2）
- 总纲10 动手者创造历史：受访开发者的自述工作清单——从其他 BSD 移植网络设备驱动、亲手编写驱动、三年内向 DragonFly 移植多项 TCP 相关 RFC 并改进网络栈并发，兼及 ACPI、电源管理与中断路由——显示 BSD 的技术史主要由这类动手者的连续劳作累积而成，而非仅由标志性发布与名人决断构成。（BSD Now EP93，[1364.00-1410.64]，L1）

**辨析**：

- 主持人口称 chroot 自 1970 年代末即已存在、最初为发行版构建流程而写，又称 jail 可自 FreeBSD 6 或 7 起嵌套、VIMAGE 提供独立网络栈，均属无出处的口头概括；且本转写为双音轨交错，受访者与多位演讲者姓名被打碎，凡涉年代、版本号与人名者，引用前须以手册页、提交记录与会议日程核验。　[存疑脚注] 上述 chroot 年代与 jail 嵌套版本表述为单一来源口头推断，且转写专名失真（Sefi、Matthew Dylan、rake floydr 等）须逐条核对。（BSD Now EP93，[2571.60-2602.40]，L4）

**文献**：

- [BSD Now EP93] Pennington J. BSD Now: 93: Stacked in Our Favor[EB/OL]. (2015-06-10)[2026-08-15]. <https://www.bsdnow.tv/93>.

<!-- /PODCAST_REVIEW -->
