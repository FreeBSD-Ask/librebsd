---
chapter: 第 221 章
id: CH221
volume: 第11卷-dragonflybsd的历史
---

# 第 221 章 DragonFly 2.x 的 HAMMER 1.0 设计与实现

## 要点

- 以项目史观总纲第 13 条 “法律与道德是利益分配”、第 19 条 “解释学循环是历史认识的根本条件”、第 21 条 “革命与改革是历史方法论的分歧” 审视 HAMMER 文件系统设计争议，可见争议的更深维度。**总纲第 13 条审视**：HAMMER 与 ZFS 的设计争议背后是许可证哲学与利益分配的差异——HAMMER 采用 BSD 许可证（与 DragonFly 整体许可证一致），ZFS 采用 CDDL（逐文件 Copyleft 许可证），两者在回馈义务上的利益分配取向相反
- DragonFly 2.4/2.6 的发布说明、commit log 与邮件列表讨论的交叉考据，确认关键特性的实际引入时间与作者归属
- 通过对 DragonFly 邮件列表中权限相关发言的考据，梳理权限授予、撤销、争议的实际过程

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4043] 卷“第11卷-dragonflybsd的历史”第 221 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_4044] 卷“第11卷-dragonflybsd的历史”第 221 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

(章级史观回填：HAMMER 的设计与 HAMMER/ZFS 争议分别映射总纲第 13 条——法律与道德是利益分配（许可证哲学与回馈义务之争）、第 19 条——解释学循环（release notes、commit log 与邮件列表三类证据的互证循环）、第 21 条——革命与改革是历史方法论的分歧（HAMMER 从零自研对 ZFS 引进的路线分歧），与各子节史观字段一致；其余主题详见子节文件史观/辨析字段)

## 辨析

- 考据过程留痕——【查证来源】项目史观总纲第 13、19、21 条经 据原文第 25 章 一手核验；DragonFly BSD 采用 BSD 许可证经 **dragonflybsd.org** 官方页面核验；ZFS 采用 CDDL 经 OpenSolaris ZFS 设计文档核验；【交叉验证方法】CDDL 与 BSD 许可证的兼容性须以法律文本而非社区陈述为依据——CDDL 与 BSD 许可证在文件级可并存（CDDL 系逐文件 Copyleft、BSD 系宽松许可），但 CDDL 组件的修改版仍须依 CDDL 回馈，整体兼容性结论须以 CDDL 官方文本与法律意见为准
- release notes 与 commit log 偶有不一致——release notes 可能为宣传目的省略部分变更或夸大某些特性，commit log 是更可靠的事实依据
- 邮件记录可能不完整——部分权限决策可能在私下邮件或 IRC 中进行，需结合 commit log 交叉验证

## 文献

- **02-sacred源材料/dagang.md**（总纲第 13、19、21 条，见其第二部分 25 条总纲）；DragonFly BSD 官方页面（**dragonflybsd.org**，BSD 许可证）；OpenSolaris ZFS 设计文档（CDDL 1.0）；FreeBSD 8.x release notes（ZFS 集成许可证兼容性）；Phoronix、OSNews 等技术媒体存档（ZFS 与 HAMMER 报道频率对比）［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］ ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2008-2022 年间：570,543 次提交。> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。
- DragonFly 2.4/2.6 release notes；DragonFly git 仓库；kernel@ 邮件列表档案 ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2009-2010 年间：6,829 次提交。> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。
- DragonFly 邮件列表档案；DragonFly commit log；committer 个人邮件 ［A］

## 史料考据补充（2026-08-04 任务3 联网核验）

> 主题：DragonFly committer 权限记录——本节正文在批量转换中佚失，仅存节题与主题行；补全须回源 2026-08-04 任务 3 联网核验记录〔存疑：正文佚失，暂以节题留痕，属史料回填专项〕。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP640、BSD Now EP229、BSD Now EP53、BSDTalk EP125（共 4 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- FreeBSD 在 OCI Runtime Specification 1.3 中被列为官方支持平台，路径包括 Samuel Karp 的 RunJ、Doug Rabson 的 Buildah 与 Podman 移植以及官方镜像。（BSD Now EP640，[106.30-305.54]，L2）
- Jim Salter 的 ZFS 灾难恢复文章以 Sanoid 与 Syncoid 实现快照、销毁与复制的自动化，并强调 RAID 不是备份、备份机应主动拉取而非被动接收。（BSD Now EP640，[339.80-818.48]，L1）
- Chris Siebenmann 通过阅读 DSL 源码说明 ZFS 的 written 与 written@ 属性即时计算，written 需回加已释放空间以避免负值。（BSD Now EP640，[849.96-1060.68]，L1）
- Justin Sherrill 提醒间歇运行的 DragonFly BSD 虚拟机与笔记本因 cron 不触发而无法自动执行 HAMMER 清理，须手动运行 cleanup 以防空间耗尽。（BSD Now EP640，[1070.44-1192.64]，L1）
- CHM 2024 年发布的 Ken Thompson 与 Doug McIlroy 口述史含转录与约四个半小时视频，回顾贝尔实验室与早期 Unix。（BSD Now EP640，[1218.68-1264.24]，L2）
- 1966 年 Joseph Weizenbaum 发表 ELIZA 一文，ELIZA 被视为最早聊天机器人之一，其引发的拟人化反应即 Eliza 效应，并推动作者转向人工智能批评。（BSD Now EP640，[1272.40-1486.48]，L2）
- David Gwynne 在 OpenBSD 引入 source 与 state limiters，以单一限流器跨多端口限制状态数与创建速率，缓解规则重载带来的状态计数重置问题。（BSD Now EP640，[1581.78-1846.92]，L1）
- 该期综述 OpenBSD、DragonFly BSD、NetBSD 对 Meltdown/Spectre 的响应：OpenBSD 引入微码更新工具，DragonFly 提交 MMU 隔离与 IBRS/IBPB，NetBSD 引入 Hot Patch 与 SVS 分离页表。（BSD Now EP229，[931.46-1482.64]，L2）
- IT Wire 报道 Theo de Raadt 的批评：仅一级厂商获得预先披露属选择性披露，并援引其 2007 年对 Intel 芯片设计问题的邮件。（BSD Now EP229，[695.8-835.26]，L2）
- 转述 Drew DeVault 的文章：追溯 1971 年 PDP-11 上 fork 的诞生、vfork 与 posix_spawn 的局限，以及 Plan 9 的 rfork 与 spawn 模型。（BSD Now EP229，[4297.5-4945.7]，L2）
- Ed Maste 提交使 LLD 成为 AMD64 默认引导链接器，标志 FreeBSD 用户态向非 GNU 工具链迁移的推进。（BSD Now EP229，[4975.44-5145.06]，L2）
- 采访 DragonFly BSD 用户：其因减少锁与高性能设计而选择 DragonFly，使用 HAMMER 的 undo 功能与快照、HAMMER2 的透明压缩。（BSD Now EP229，[2246.7-2489.82]，L1）
- HAMMER 是 Matthew Dillon 为 DragonFly BSD 设计的 64 位文件系统，以事务组实现逐文件历史、快照、镜像流与删除后恢复。（BSD Now EP53，[3556.02-3609.18]，L2）
- HAMMER 的镜像流模式类似持续运行的 ZFS send，可不断向备份目标复制数据；其快照被视为可访问的实时数据而非只读副本。（BSD Now EP53，[3978.66-4095.18]，L2）
- Reyk Floeter 在卢布尔雅那 OpenBSD hackathon 当天以 relayd 源码为基础拆出基本可用的 httpd，随后在 Bob Beck 与 Theo de Raadt 推动下提交进树，十四天后达到可接受状态。（BSD Now EP53，[945.18-1035.58]，L1）
- OpenBSD httpd 默认运行于 chroot、采用特权分离与 pre-fork 模型，并吸收 LibreSSL 对私有内存分配器遮蔽安全机制的教训，保持代码基精简。（BSD Now EP53，[866.38-958.10]，L1）
- DragonFly 1.10（2007 年发布）被 Dillon 概括为无大事件型版本：几乎系统各层面均为清理，包括新 AHCI SATA 驱动与磁盘抽象层、GPT 与 64 位磁盘标签的非引导支持、内核态轻量线程与两套线程库（默认沿用原 BSD 线程库，年末起转向基于轻量线程设施的一对一线程库）、大量新 USB/PCI 与无线驱动及应用、内核、编译器更新；发布同时使 VFS API 更为健壮，可热拔 USB 硬盘并事后卸载而不崩内核，此项工作直接构成用户态 VFS 的前提。（BSDTalk EP125，[63.54-246.44]，L1）
- 对分叉五年（2002-2007）的回顾与自评：1.10 之前的重写皆为设计意图或聚群前提——轻量级线程、内核线程调度器、可插拔用户调度器与调度掩码多出自 Dillon 本人构想，名字缓存拓扑与 VFS 操作改造为实现聚群所必经；组织层面开发者团队过去一年的增长超过此前两年之和，出现更多真正提交代码者，年初以来约一千五百次提交，pkgsrc 兼容性一年间显著改善。他同时坦承进展远慢于当初预期，主因是未能预见工作量之巨、内核内部重构耗时尤甚，且大量时间耗于管理开发者、管理提交与追踪缺陷等辅助事务；DragonFly 不再是实验性分叉——稳定性记录足以支撑生产系统，加上 pkgsrc 提供所需应用，在生产范式下与其他 BSD 及 Linux 大致等价，后续将以新文件系统为先，因为没有聚群文件系统就没有聚群。（BSDTalk EP125，[436.08-633.30]，L1）
- 新文件系统于访谈时刚过基本设计阶段（记录索引方案尚待定）并已开始编码，目标年底完成，定位为 BSD 与 Linux 竞争所急需的拼图。其设计原则：内部记录导向，使流式备份与活镜像的复制算法大为简化；文件系统原生维护全部变更历史，复制数据可直接取自文件系统本身而无需维护独立变更队列，从而可在慢速链路上复制、支持备份目标间歇离线（如周末上线续传）而不在主端积压数据；快照能力因记录结构而近乎免费，设计目标覆盖备份、活镜像、热切换与多主操作，且不因网络故障或慢链路拖慢生产系统。（BSDTalk EP125，[675.05-1058.56]，L1）
- vkernel 被评为开发过程中无价的基础设施：单处理器版早已可用，社区成员提议将其 SMP 化且实现不难，现有版本可构建为 SMP 虚拟内核；虽用于生产运行效率不高，却是调试内核代码与在安全环境中开发内核的利器。关于多处理器现状，Dillon 坦承 1.10 基准预计与 1.8 相当：系统调用路径在触及文件描述符之前已 MP safe（1.10 发布后关闭了两个相关 sysctl），但数据子系统仍受大内核锁保护；内核虽支持 31 个 CPU，大内核锁的串行化使其在四 CPU 以上难以扩展，除非将其彻底移除。（BSDTalk EP125，[284.84-428.52]，L1）

**史料**：

- FreeBSD Foundation 博客 FreeBSD Officially Supported in the OCI Runtime Specification 1.3。（BSD Now EP640，[106.30-305.54]，L2）
- Jim Salter 于 Klara Systems 的 ZFS 灾难恢复文章。（BSD Now EP640，[339.80-818.48]，L1）
- Chris Siebenmann 关于 OpenZFS written 与 written@ 属性的博客。（BSD Now EP640，[849.96-1060.68]，L1）
- Justin Sherrill 的 DragonFly BSD Digest。（BSD Now EP640，[1070.44-1192.64]，L1）
- David Gwynne 的 Undeadly 文章 source and state limiters in PF。（BSD Now EP640，[1581.78-1846.92]，L1）
- DragonFly BSD 的 Matthew Dillon 1 月 5 日关于 Meltdown 为 Intel 专属缺陷、AMD 免疫的帖子。（BSD Now EP229，[1015.3-1056.54]，L2）
- Theo de Raadt 2007 年 6 月 27 日的邮件线索（IT Wire 报道所引），涉及对 Intel x86 设计问题的早期批评。（BSD Now EP229，[807.38-835.26]，L2）
- Drew DeVault 的 fork 批评文章，以 1971 年贝尔实验室的 PDP-11 语境叙述 fork 的诞生。（BSD Now EP229，[4299.5-4438.76]，L2）
- FreeBSD 的 LLD bootstrap 链接器提交（Ed Maste 的提交信息，LLVM PR 23214 与 85 个依赖 issue）。（BSD Now EP229，[5056.46-5134.62]，L2）
- Reyk Floeter 访谈（OpenBSD httpd 作者当事人自述）。（BSD Now EP53，[540.14-1854.84]，L1）
- 主持人片头新闻记载 NetBSD 宣布 2007 年筹款活动，希望至年底至少募集五万美元，为 NetBSD Foundation 当年财务运作的独立旁证史料。（BSDTalk EP125，[31.40-41.64]，L2）

**史观**：

- 总纲10 动手者创造历史：OCI 支持由 Samuel Karp、Doug Rabson 等志愿者的多年内核与工具链工作累积而成。（BSD Now EP640，[227.38-305.54]，L2）
- 总纲9 经验优先：Jim Salter 以亲身经历过的断电、火灾、失窃等故障说明为何 RAID 不等于备份。（BSD Now EP640，[630.76-692.68]，L1）
- 总纲22 知识注定过时：HAMMER 清理依赖 cron 定时触发的假设在笔记本关机场景下失效，反映旧运维假设随硬件使用方式变化而过时。（BSD Now EP640，[1081.24-1215.64]，L1）
- 总纲8 本体论上各方平等：各 BSD 在 Meltdown/Spectre 面前的独立响应路径显示本体论上的多方平等，没有单一正确解。（BSD Now EP229，[1460.82-1482.64]，L2）
- 总纲13 法律与道德是利益分配：Theo 对 Intel 的批评强调选择性披露使大厂之外者受损，呈现披露秩序中的利益分配而非技术中立。（BSD Now EP229，[706.42-720.42]，L2）
- 总纲22 知识注定过时：对 fork 的批评把近 50 年的设计选择与内存过量承诺、OOM killer 等后果联系起来，呈现旧有设计在当下的历史惯性。（BSD Now EP229，[4516.04-4624.68]，L2）
- 总纲10 动手者创造历史：Reyk Floeter 以一天内动手拆出 httpd 并持续迭代的方式直接塑造 OpenBSD 基础系统工具。（BSD Now EP53，[945.18-1035.58]，L1）
- 总纲22 知识注定过时：OpenBSD 以更简单、更贴合自身安全模型的新工具替换日益膨胀的 nginx，体现既有技术方案的持续失效与重写。（BSD Now EP53，[837.46-945.18]，L1）
- 总纲4 分离聚合是永恒规律：httpd 自 relayd 分离、其协议改进又回流 relayd，展示 BSD 工程中持续的分离与聚合循环。（BSD Now EP53，[1169.46-1196.62]，L1）
- 总纲5 没有必然性，只有偶然性：Dillon 的五年回顾把项目形态的偏离归于不可预见的具体负担：内核重构的真实工作量、管理开发者与追踪缺陷等辅助事务对核心目标的挤占，均非五年前规划所能预料；聚群目标的实现路径（先基础设施、再文件系统、后网络聚群）也是逐年应对中重新排定的次序，而非初始蓝图，技术项目的历史进程由偶然负担与具体条件塑造。（BSDTalk EP125，[551.44-621.14]，L1）
- 总纲10 动手者创造历史：vkernel 的 SMP 化起于社区成员一句“为何不做成 SMP”的即兴提议，实现后即成为多人使用的调试利器；开发者团队的增长亦以“真正动手提交的人”为准绳而非名义成员数——DragonFly 的演进由动手者的具体行动与即兴尝试驱动，而非自上而下的规划。（BSDTalk EP125，[296.84-316.58]，L1）

**辨析**：

- 转录将 Doug Rabson 记作 Doug Rapson、将 Dave Cottlehuber 记作 Dave Cossel-Huber，人名拼写存在转写歧义。　[存疑脚注] 贡献者姓名存在语音转写偏差，须以 FreeBSD Foundation 公告核验（BSD Now EP640，[227.38-290.18]，L4）
- ELIZA 作者名在转录中拼作 Weisenbaum 或 Weisenbalm，通行写法为 Joseph Weizenbaum，须以原始论文核验。　[考据脚注] 人名拼写存在转写偏差，以 Communications of the ACM 1966 年原文为准（BSD Now EP640，[1279.84-1342.08]，L4）
- 对 fork 的批评系博客作者个人立场，节目主持人在结尾补充“无法改变应用使用习惯”的采纳难题，替代方案在 FreeBSD 仅停留在讨论阶段。　[存疑脚注] 系单一来源的个人技术立场（BSD Now EP229，[4888.6-4949.3]，L4）
- Theo de Raadt 对 Intel 的指控（“被告知忽略风险”）系其个人推断，无直接证据，节目亦未提供 Intel 回应。　[存疑脚注] 系个人推断，无直接证据（BSD Now EP229，[763.4-807.38]，L4）
- HAMMER 在转录中被转写为多处以 ZFS 类比，其最大容量等参数属主持人转述，未能直接核对 DragonFly 官方文档。　[存疑脚注] HAMMER 技术参数为二手转述，未经官方手册交叉核验（BSD Now EP53，[3556.02-3609.18]，L4）
- 转写专名存在系统性误差：线程库名转写作 LibCR 与 LibThreadZoo（通行作 libc_r 与 libthread_xu），pkgsrc 转写作 package source，userland 转写作 user LAN 与 Usulam，sysctl 转写作 SysControls，ATA 驱动转写作 DATA driver；另新文件系统“与 Linux 竞争”的定位系 Dillon 单方目标陈述，其对复制文件系统优于队列复制的论证亦属设计意图而非实测结论，采用时须与 HAMMER 后续实现及性能文献对勘。　[存疑脚注] 转写专名 LibCR、LibThreadZoo、package source、user LAN、Usulam、SysControls、DATA driver 均疑为语音识别误差；文件系统性能主张为设计意图陈述，未经实测验证。（BSDTalk EP125，[111.08-126.68]，L4）

**文献**：

- [BSD Now EP640] Pennington J. BSD Now: 640: Cleaning up Hammer[EB/OL]. (2025-12-04)[2026-08-15]. <https://www.bsdnow.tv/640>.
- [BSD Now EP229] Pennington J. BSD Now: 229: The Meltdown of Spectre[EB/OL]. (2018-01-17)[2026-08-15]. <https://www.bsdnow.tv/229>.
- [BSD Now EP53] Pennington J. BSD Now: 53: It's HAMMER Time[EB/OL]. (2014-09-03)[2026-08-15]. <https://www.bsdnow.tv/53>.
- [BSDTalk EP125] Backman W. BSDTalk: 125: bsdtalk125 - Matthew Dillon[EB/OL]. (2007-08-15)[2026-08-27]. <https://bsdtalk.blogspot.com/2007/08/bsdtalk125-matthew-dillon.html>.

<!-- /PODCAST_REVIEW -->
