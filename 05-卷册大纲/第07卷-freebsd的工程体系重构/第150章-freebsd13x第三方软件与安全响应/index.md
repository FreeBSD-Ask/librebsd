# 第 150 章 freebsd13x第三方软件与安全响应

---
chapter: 第 150 章
id: CH150
volume: 第07卷-freebsd的工程体系重构
---

## 史料

- [DB:research_notes:blocks:4490] 关键词“安全响应”命中（原文截断）　[存疑脚注] 该命中条目原文截断，回源后补全。
- [DB:research_notes:blocks:17647] 关键词“安全响应”命中：[p.4] 1 绪论 .................................................…
- [DB:research_notes:blocks:69677] 关键词“安全响应”命中：www.dragonflybsd.org；Dillon M. HAMMER File System Design[Z].…

## 要点

- FreeBSD 13.0-RELEASE（2021 年 4 月 13 日）将 GCC 4.2.1 从 base system 源码树中完全移除，结束 GCC 在 FreeBSD base 中长达 27 年的历史（自 FreeBSD 2.0 起）。GCC 移除由 Warner Losh（沃纳·洛什）（imp@）主导，是 FreeBSD 许可证纯洁化工程的最终里程碑。移除时间线：10.0（2014 年 1 月）Clang 成为 x86/arm 默认编译器，GCC 保留用于非 x86；12.0（2018 年 12 月）x86 不再默认安装 GCC 4.2.1 二进制；13.0（2021 年 4 月）完全移除 GCC 4.2.1 源码及相关的 libstdc++、libgomp、libssp 等库。所有架构（包括 powerpc、powerpc64、mips、riscv 等先前依赖 GCC 的架构）均完成 Clang 迁移，GCC 不再存在于 base 中。需使用 GCC 的用户可通过 ports 安装现代 GCC 版本（lang/gcc10-gcc13 等）。
- FreeBSD 13.0-RELEASE 将 LLD（LLVM Linker）设为所有架构的默认系统链接器，完成 LLD 从“部分架构默认”到“全架构默认”的迁移。12.0（2018）中 LLD 仅为 amd64/arm64 默认，13.0 扩展到 i386、armv7、powerpc、powerpc64、riscv64 等所有支持架构。GNU ld 和 GNU binutils 从 base 中移除（与 GCC 4.2.1 一同移除），LLD 成为 base 中唯一的链接器。LLD 的链接速度优势（大型 C++ 项目快 2-5 倍）、LTO 原生支持、Apache 2.0 许可证是其成为全架构默认的关键因素。
- FreeBSD 13.0-RELEASE 搭载 OpenSSL 1.1.1l（13.0）→ 1.1.1q（13.1）→ 1.1.1t（13.2）→ 1.1.1w（13.3），13.4 搭载 OpenSSL 3.0.16+。OpenSSL 1.1.1 支持 TLS 1.3，13.x 全程保持 1.1.1 系列的安全更新直到 13.3，13.4 升级至 OpenSSL 3.0 系列。OpenSSH 版本从 7.9p1（13.0）升级至 9.6p1（13.4），支持 sntrup761x25519 混合后量子密钥交换。sendmail 在 13.x 全系列中仍为默认 MTA（版本 8.16.1），DMA 不在 base 中——sendmail 的默认地位延续至 14.0 才被 DMA 替代。
- 13.0 是 FreeBSD 许可证纯洁化工程的“竣工”版本——GCC 4.2.1 完全移除、LLD 全架构默认、GNU binutils 移除，三项变更共同标志着 FreeBSD base 彻底摆脱了对 GPL（v2/v3）许可组件的依赖。这一工程自 2007 年 GPLv3 发布启动，历时 14 年，涉及编译器、链接器、汇编器、调试器、文本工具、构建系统、DNS 解析器、软件包管理器等数十个组件的替换。13.0 的第三方软件变更体现了“终结”多于“开始”——旧工具链的移除多于新工具链的引入，这是 12.0/13.0 作为“移除期”的特征。
- FreeBSD 13.x 对应的 Linux 内核 LTS 版本与同期 Linux 发行版如下表所示。FreeBSD 与 Linux 的差异不在“功能有无”而在设计哲学：Linux 追求快速迭代、新功能快速引入，FreeBSD 追求稳定性、保守性、设计一致性。

## 史观

- 总纲第 13 条——法律与道德是利益分配：GCC 4.2.1 完全移除标志着 FreeBSD 许可证纯洁化工程在编译器层面的最终完成——自 2007 年 GPLv3 发布以来，FreeBSD 项目用 14 年时间完成了从 GPL 编译器到 BSD 许可编译器的全面迁移，这是操作系统史上规模最大的编译器迁移之一。
- 总纲第 4 条——分离聚合是永恒规律：到 2020 年代，Linux 已成为绝对主导的通用操作系统内核，但 FreeBSD 在特定场景（如 Netflix CDN、pfSense/OPNsense 防火墙、TrueNAS 存储、嵌入式网络设备）仍保持优势，这是 30 年技术路线分离演进的结果。
- 专题语（不设总纲条号）——安全响应的被动模式：13.x 周期 SA 节奏相对平缓反映 Security Team 工作模式仍处于“被动响应外界报告”阶段——Security Officer Team 在 Gordon Tetlow（戈登·泰特洛）（Security Officer）、Ed Maste（埃德·马斯特）（Deputy）主导下保持稳定延续，但未开展 14.x 周期那样的系统性主动审计；这种被动响应模式既是资源约束的产物，也为后续周期的主动审计积累了案例基础。
- 专题语（不设总纲条号）——稳定分支的保守升级原则：OpenSSL 1.1.1 是 LTS（长期支持）版本，FreeBSD 选择在 stable/13 全周期保持 1.1.1 系列而不升级到 3.0，体现了“稳定分支不引入大版本升级”的保守工程原则；这种保守性带来双重效应：一方面避免了 OpenSSL 3.0 引入的新 CVE 与 API 兼容性问题，另一方面使 13.x 周期内的 OpenSSL CVE 都是 1.1.1 系列的修复版本，不涉及 3.0 的新 API 迁移成本。
- 专题语（不设总纲条号）——虚拟化边界的零星审计：bhyve 3 个 SA 跨度两年反映 13.x 周期虚拟化边界审计处于“零星发现”阶段——外界报告或代码审查发现问题后逐个修复，未开展系统性审计；jail 3 个 SA 集中于 2021-02-24 与 2021-04-06 两个发布批次，均涉及 jail 配置与权限边界，是 **jail(2)** 系统调用与 `jail_remove`、`jail_mount` 等管理接口的边界问题。

## 辨析

- GCC 4.2.1 的移除不等同于“GCC 在 FreeBSD 上不可用”——ports 中的 lang/gcc 系列持续提供现代 GCC 版本（GCC 10/11/12/13 等），用户可自由安装；构建 ports 中的某些软件（如需要 OpenMP 的 C++ 程序、使用 GCC 特定扩展的 Fortran 程序）仍需要 ports GCC；GCC 移除仅影响 base system，不影响 ports 生态中的 GCC 使用自由。
- “Linux 比 FreeBSD 功能多/性能好/支持硬件多”是一个笼统的说法，需要看具体场景——在网络转发性能、ZFS 集成、内核 API 稳定性、许可证纯净度等方面 FreeBSD 有自身优势；反之 Linux 在新硬件支持、容器生态、eBPF 可编程性等方面优势明显
  - 文献：Kernel Newbies. *Linux Kernel Release Notes*. kernelnewb
- 39 个 SA 的统计口径需精确说明：以 SA 公告发布日期在 **2021-04-01** 至 **2023-11-01** 之间为准；SA-23:15 至 SA-23:19（2023-11-08 至 2023-12-19）虽属 13.3-RELEASE 修复范围但发布日期超出周期边界，未计入 39 个；SA-21:07.openssl（2021-03-25）发布于 13.0-RELEASE 前
- **需严格区分**：① 13.x 版本周期文件（2021-04 至 2023-11）查询结果中出现的 OpenSSL 3.0 commits（如 2023-08-10 `aa7957345732816fb0ba8308798d2f79f45597f9` “OpenSSL: update to 3.0.10”、2023-09-22 `315108b81694de474bbc273c0050b1950”（hash 于原文截断，对应 OpenSSL 3.0 系列更新提交，全 hash 与提交说明以 **freebsd.duckdb** commits 表复核为准）——此类 3.0 commits 属 stable/13 后期的 OpenSSL 版本升级准备，非 13.x 周期本身的 SA 修复，统计 39 个 SA 时应剔除。
- **需精确说明**：① **SA-21:13.bhyve** 涉及 virtqueue 处理（**vq_getchain()** 函数）的多个设备模型错误，影响 bhyve 运行时设备模拟，攻击向量是恶意 guest 操作触发 host 内核漏洞；② **SA-22:05.bhyve** 涉及 e82545 网卡模拟器的校验和偏移字段验证，是单个设备模型的特定漏洞；③ **SA-23:07.bhy；③ **SA-23:07.bhyve** 的攻击向量细节以安全公告原文为准　[存疑脚注] 原文于此截断，回源补全。**

## 文献

- FreeBSD 13.0-RELEASE Release Notes [Z]. 2021-04-13；FreeBSD 10.0/12.0 Release Notes [Z]. 2014/2018；Warner Losh GCC retirement announcement [EB/OL]. freebsd-arch mailing list, 2020-2021 ［A］


<!-- dangan-20260908 消解回写 -->
- HardenedBSD. Project. HardenedBSD Features Documentation [EB/OL]. [2026-07-22]. <https://hardenedbsd.org/>[EB/OL]. 2026. ［DKC-2251→fulltext:6123］
<!-- /dangan-20260908 -->
## 存目（原 149.12.2/149.13.2 抢救残片）

- 上述两节为本 150 章主题（13.x 第三方软件变更与同期 OS）的旧章号抢救残片，其正本体对应磁盘节文件 150.12（GCC 移除与 LLD 全架构默认）、150.13（同期操作系统横向比较）——残片均截断，已按正本体删除。
## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-500 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-500`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者 Thomas Munro 口述：举例说明曾运行大规模 illumos ZFS 上 PostgreSQL 数据库集群的团队经验（YouTube EPfdbO5Jpopbg，[445.12-452.55]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1205 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1205`；w172 YouTube 章节路由采纳）

据讲者 Matthias Wolf 口述：Chromium 移植到 FreeBSD 后已能无缝进行网络会议。（YouTube EPzHKn-56nxRE，[112-117.99]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->
