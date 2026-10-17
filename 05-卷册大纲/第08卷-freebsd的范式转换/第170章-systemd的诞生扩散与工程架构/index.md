---
chapter: 第 170 章
id: CH170
volume: 第08卷-freebsd的范式转换
---

# 第 170 章 systemd的诞生扩散与工程架构

## 要点

- freebsd 代码仓库共 1,294,851 次提交（1993-06-12 至 2026-08-25），5,671 位贡献者（contributors 表行数）

## 史料

- [DB:bsdnow_podcast:outline_mappings:om_10607] BSD Now 第 642 期，匹配 CH170 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10739] BSD Now 第 623 期，匹配 CH170 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10746] BSD Now 第 622 期，匹配 CH170 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10771] BSD Now 第 617 期，匹配 CH170 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10822] BSD Now 第 610 期，匹配 CH170 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10850] BSD Now 第 606 期，匹配 CH170 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10865] BSD Now 第 604 期，匹配 CH170 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10899] BSD Now 第 601 期，匹配 CH170 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11017] BSD Now 第 585 期，匹配 CH170 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11050] BSD Now 第 581 期，匹配 CH170 章，关联度 1.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 数据库统计受 CVS-to-Git 迁移、镜像滞后等因素影响，commit 数量与贡献者统计存在系统性偏差，须结合一手史料交叉验证

## 文献

（待补）

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP416、BSD Now EP580（共 2 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- William Blankenship 记录其迁移至 FreeBSD 后，依据 FreeBSD 手册发现网络打印机通常接受 9100 端口作业，用 netcat 加端口与重定向即可直接打印，不必依赖 CUPS 的复杂驱动栈。（BSD Now EP416，[1136.6-1289.6]，L2）[订正：原 [1142.84-1261.9]，2026-09-30 SenseAudio 重转核对]
- OpenZFS 快照讨论指出，快照数量超过每数据集约千个会显著拖慢列出、创建、复制与销毁操作，性能影响与单数据集快照数相关，而非系统快照总数，因此应滚动修剪旧快照。（BSD Now EP416，[174.9-244.3]，L2）[订正：原 [196.1-237.24]，2026-09-30 SenseAudio 重转核对]
- Multics 在 2021 年前后发布 12.7 版本，新增卷池支持层级备份、信息段历史注释与 mBuild 子系统，延续其作为 Unix 前身之一的后续维护。（BSD Now EP416，[2007.9-2183.1]，L2）[订正：原 [2023.6-2167.9]，2026-09-30 SenseAudio 重转核对]
- initware 是 systemd 的 fork，已可在 FreeBSD 13 与 NetBSD 9 上运行大部分功能，目标还包括 macOS 与 Illumos，因上游仅面向 systemd 的应用需求而出现。（BSD Now EP416，[1863.8-2027.8]，L2）[订正：原 [1884.3-2022.7]，2026-09-30 SenseAudio 重转核对]
- Colin Percival 自述 FreeBSD 发布工程长期处于由发布工程师即兴决定的临时状态，他接任后引入按季度排布、覆盖未来五年的发布日历，使 minor 版本节奏可预期。（BSD Now EP580，[466.0-571.0]，L1）[订正：原 [476.24-547.40]，2026-10-01 SenseAudio 重转核对]
- Colin 将 FreeBSD 主版本支持期由五年缩减为四年，以对齐每两年一次的主版本节奏，避免同时维护三个稳定分支带来的上游 OpenSSL、编译器与 ports 兼容负担。（BSD Now EP580，[617.0-769.1]，L1）[订正：原 [630.52-756.16]，2026-10-01 SenseAudio 重转核对]
- Colin 回顾 freebsd-update 工具源于 2003 年他为简化系统补丁更新而编写，并为此创造了 bsdiff 二进制差分工具，后者后来被广泛用于各处的增量更新。（BSD Now EP580，[192.7-235.5]，L1）[订正：原 [210.06-229.42]，2026-10-01 SenseAudio 重转核对]
- Andrew Hewus 自述约 2003 年在亚利桑那州一家小型 ISP 从 OpenBSD 3.5 或 3.6 开始，将 DNS、邮件与路由逐步替换为 OpenBSD，后经邮件列表接手 OpenBSD 基本系统中的 Perl 维护。（BSD Now EP580，[1455.1-1578.3]，L1）[订正：原 [1455.12-1565.32]，2026-10-01 SenseAudio 重转核对]
- Liam Proven 梳理商业 Unix 的当代存续：Xinuos 继承 SCO 的 Xenix 与 UnixWare 业务并提供基于 FreeBSD 的清理版本；AIX 开发团队迁往印度；Solaris 不再出新版本但仍获安全修复；illumos 与 Oxide Computer 延续 OpenSolaris 谱系。（BSD Now EP580，[2905.8-3025.7]，L2）[订正：原 [2915.18-3022.62]，2026-10-01 SenseAudio 重转核对]
- Liam Proven 以其亲历的 FreeBSD 13 升级 14 后桌面环境损坏为例，指出 BSD 桌面在升级平滑度与新手进入门槛上的短板，并批评 systemd 及其安全启动方向正在收窄用户对系统的控制。（BSD Now EP580，[3037.3-3352.6]，L1）[订正：原 [3043.30-3344.86]，2026-10-01 SenseAudio 重转核对]

**史料**：

- JT Pennington 在 Twitter 发布的 PDP-11 工程图纸，展示早期整机级布线文档，属小型机物质文化的一手图像史料。（BSD Now EP416，[2183.1-2315.8]，L1）[订正：原 [2207.6-2289.3]，2026-09-30 SenseAudio 重转核对]
- Edward Napierala 提交的 FreeBSD 非特权 chroot 改动，以 no-new-privs 标志允许非 root 进程在 chroot 内禁用 setuid，属源码级一手史料。（BSD Now EP416，[1746.6-1893.8]，L2）[订正：原 [1772.2-1884.3]，2026-09-30 SenseAudio 重转核对]
- 本期为 EuroBSDcon 2024 现场采访；Colin Percival 与 Andrew Hewus 为一手自述，Liam Proven 为 The Register 记者的一手见闻与二手综述。（BSD Now EP580，[40.2-1294.1]，L1）[订正：原 [59.28-1293.58]，2026-10-01 SenseAudio 重转核对]

**史观**：

- 总纲9 经验优先：netcat 打印以极简工具替代 CUPS 复杂栈，体现 Unix 经验优先与工具可组合的传统，用户直接与协议端口交互即可完成任务。（BSD Now EP416，[1240.5-1289.6]，L2）[订正：原 [1244.04-1261.9]，2026-09-30 SenseAudio 重转核对]
- 总纲20 历史地理塑造思想土壤：PDP-11 工程图纸显示早期计算机以整机接线图为物质载体，其尺寸与可读性受硬件形态制约，呼应历史地理与物质文化塑造技术认知。（BSD Now EP416，[2213.1-2263.6]，L2）[订正：原 [2231.78-2256.2]，2026-09-30 SenseAudio 重转核对]
- 总纲10 动手者创造历史：Colin 因自身补丁更新需求编写 freebsd-update 与 bsdiff，其工具后来成为 FreeBSD 更新基础设施的一部分，体现动手者为解决具体问题而塑造系统历史。（BSD Now EP580，[192.7-235.5]，L1）[订正：原 [210.06-229.42]，2026-10-01 SenseAudio 重转核对]
- 总纲3 不存在进步，只有权力再分配：FreeBSD 发布工程从即兴决策到日历化、支持期从五年缩为四年的过程，是工程与治理权力在项目内部的重新配置。（BSD Now EP580，[617.0-769.1]，L1）[订正：原 [630.52-756.16]，2026-10-01 SenseAudio 重转核对]
- 总纲21 革命与改革是历史方法论的分歧：Liam 对 systemd 与安全启动方向的批评，呈现开源生态中激进变革与保守续存两种方法论之间的持续张力。（BSD Now EP580，[3037.3-3166.5]，L2）[订正：原 [3043.30-3164.96]，2026-10-01 SenseAudio 重转核对]

**辨析**：

- 转写称 Multics 12.7 为最新版本，其发布时间与维护状态需与 Multics wiki 及 DPS-8/M 模拟器资料核对。 [考据脚注] Multics 12.7 的发布时间与维护主体需查 multicians.org 与相关 wiki。（BSD Now EP416，[2027.8-2123.1]，L4）[订正：原 [2030.2-2116.8]，2026-09-30 SenseAudio 重转核对]
- Liam Proven 关于 Xinuos 产品形态、AIX 团队迁移地等描述属记者二手综述，具体时点与细节须以厂商公告核实。 [存疑脚注] 商业 Unix 厂商现状为记者综述，未逐一核对厂商一手公告。（BSD Now EP580，[2905.8-3025.7]，L4）[订正：原 [2915.18-3022.62]，2026-10-01 SenseAudio 重转核对]
- FreeBSD 桌面升级损坏为 Liam Proven 的个案经验，不能据以推断该升级路径具有普遍失败率。 [存疑脚注] 桌面升级问题为单一用户个案经验，未经系统复现或统计验证。（BSD Now EP580，[3252.5-3322.9]，L4）[订正：原 [3252.54-3318.12]，2026-09-30 SenseAudio 重转核对]

**文献**：

- [BSD Now EP416] Pennington J. BSD Now: 416: netcat printing[EB/OL]. (2021-08-19)[2026-08-15]. <https://www.bsdnow.tv/416>.
- [BSD Now EP580] Pennington J. BSD Now: 580: EuroBSDcon 2024 - Part 2[EB/OL]. (2024-10-10)[2026-08-15]. <https://www.bsdnow.tv/580>.

<!-- /PODCAST_REVIEW -->

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-2464 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2464`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan 2018 讲者 Benno Rice〕讲者口述：systemd 在概念上其实是 2010 年 Lennart Poettering 重做服务管理时的产物，其形态基本等同于苹果的 launchd——讲者说很多人谈 systemd 却不谈 launchd，这让他觉得好笑。（YouTube EP6AeWu1fZ7bY，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2465 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2465`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan 2018 讲者 Benno Rice〕讲者口述：cgroups 只是把进程分组，其功能大致相当于 FreeBSD jail 的进程分组部分，在它之上可以挂接 jail 式隔离与资源限制。（YouTube EP6AeWu1fZ7bY，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2466 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2466`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan 2018 讲者 Benno Rice〕讲者口述：Debian 就 systemd 的漫长争论最终以采用 systemd 收场，而围绕那次投票的争议使不少参与者辞职。（YouTube EP6AeWu1fZ7bY，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2467 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2467`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan 2018 讲者 Benno Rice〕讲者口述：BSD 的 rc 结构把系统配置与服务引导搅在一起——配置网络接口、配置运行时链接器等被算作同一类“整理”工作，于是用同一套隐喻和进程去管两类并不相同的东西，容易造成混淆。（YouTube EP6AeWu1fZ7bY，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
