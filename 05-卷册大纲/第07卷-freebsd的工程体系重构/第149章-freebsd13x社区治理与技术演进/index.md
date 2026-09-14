# 第 149 章 freebsd13x社区治理与技术演进

---
chapter: 第 149 章
id: CH149
volume: 第07卷-freebsd的工程体系重构
---

## 史料

- [DB:research_notes:blocks:1204] 关键词“技术演进”命中：史实考据：Marshall Kirk McKusick、George V. Neville-Neil、Robert N.…
- [DB:research_notes:blocks:6115] 关键词“技术演进”〔待核：原文截断，后文待回源〕
- [DB:research_notes:blocks:6141] 关键词“技术演进”命中：法律限制：技术演进的法律边界（第 138 章）…

## 要点

- Google LLC v. Oracle America, Inc.（593 U.S. 1, Docket No. 18-956）是美国最高法院关于 API 版权的里程碑案件，判决于 **2021 年 4 月 5 日** 下达（距 FreeBSD 13.0 发布仅 8 天）：(1) 案件起因：Google 在 Android 中使用了 Java 的 37 个 API 包（约 11,500 行声明代码），Oracle（收购 Sun Microsystems 后）起诉 Google 侵犯版权；(2) 联邦巡回上诉法院先前判决 API 受版权保护且 Google 使用不构成 fair use；(3) 最高法院 6-2 判决（Justice Breyer 主笔，Roberts、Sotomayor、Kagan、Gorsuch、Kavanaugh 加入；Thomas、Alito 异议；Barrett 未参与）：Google 对 Java API 的重新实现构成 **fair use（合理使用）**；(4) 判决理由：API 是“调用系统”，其重新实现属于 transformative use（转换性使用），符合 fair use 四要素分析
- Google v. Oracle 判决对 BSD 和开源生态的重要意义：(1) **历史平反**：BSD 从 1980 年代开始重新实现 AT&T UNIX API，导致 1992-1994 年 USL v. BSDi 诉讼（ch14 详述），该诉讼以和解结案，API 版权问题未在最高法院层面解决；2021 年判决从法律上认可了 API 重新实现的合法性；(2) **互操作性保障**：判决确认了软件行业长期实践——重新实现 API 以实现互操作性是合法的，这对开源生态至关重要；(3) **FreeBSD 直接受益**：FreeBSD 核心由大量重新实现的 UNIX API 构成，还有 Linux ABI 兼容层等重新实现，判决降低了相关法律风险；(4) 但判决也有局限性——它是美国最高法院判决，仅在美国具有约束力，且基于 fair use 四要素具体分析，并非绝对规则
- Google v. Oracle 判决（2021-04-05）、Git 迁移完成（2021-04-06）、FreeBSD 13.0 发布（2021-04-13）三件大事在短短八天内相继发生，构成了一个极具象征意义的历史时刻：(1) 法律层面：API 重新实现的合法性得到最高法院确认；(2) 工具层面：开发基础设施从 svn 迁移到 Git，与当代开源生态接轨；(3) 版本层面：13.0-RELEASE 作为新阶段的第一个版本正式发布；这三件事在时间上的接近虽是巧合，但共同标志着 FreeBSD 进入了一个新阶段
- Google v. Oracle 案的一手史料包括：(1) 美国最高法院官方判决书（supremecourt.gov）；(2) 下级法院判决和案卷；(3) 双方律师的口头辩论记录和答辩状；(4) 各大法律数据库（Oyez、Justia、SCOTUSblog）的案件摘要；需注意：法律判决是复杂的法律文件，媒体标题和二手报道经常简化或误读判决理由，应直接阅读判决书原文
- FreeBSD 13.0-RELEASE 将 MIPS 架构（包括 mips、mipsel、mips64、mips64el、mipsn32、mipselhf、mipshf、mips64elhf、mips64hf 等多种变种）从 Tier-2 降级，标志着 FreeBSD 对 MIPS 架构支持的终结过程开始；MIPS 自 FreeBSD 8.0（2009-11）起由 Oleksandr Tymoshenko、Jung-uk Kim 等开发者移植，主要用于嵌入式路由器（Atheros/Qualcomm Wi-Fi 路由器、Lantiq DSL 调制解调器）、SGI 工作站、龙芯（Loongson）处理器；MIPS 退役原因：(1) 市场份额被 ARM 大幅取代——路由器厂商逐步转向 ARM 架构；(2) 龙芯自 2020 年代起转向自主指令集 LoongArch，不再使用 MIPS；(3) Clang/LLVM 对 MIPS 后端支持长期滞后于 GCC；(4) 活跃维护者持续减少；(5) MIPS 存在多种 ABI（o32/n32/n64）和字节序变种，维护复杂度极高；FreeBSD 13.x 期间 MIPS 支持持续降级，13.4 是最后一个包含 MIPS 支持的稳定分支之一

## 史观

- 总纲第 12 条——法律结构：这一判决对 BSD 社区具有特殊历史意义——BSD 从诞生之日起就在重新实现 UNIX API（从 BSD 4.x 到 386BSD 到 FreeBSD），API 重新实现的法律地位长期处于灰色地带；最高法院的判决为“重新实现 API 构成 fair use”提供了法律确定性，这是 BSD 社区 40 年实践的法律背书
  - 辨析：判决并未直接裁定“API 不受版权保护”——多数意见回避了这一宪法问题，而是基于 fair use 作出判决，这是司法最小主义（judicial minimalism）的体现；判决对软件行业影响深远，但具体边界仍需后续案件澄清
- 总纲第 7 条——BSD 与 UNIX 谱系的连续性：MIPS 是 RISC 处理器的先驱，SGI IRIX 是重要的商业 UNIX 平台；FreeBSD 对 MIPS 的支持延续了 BSD 在非 x86 架构上的传统，但市场和技术的变化使其退役成为必然
  - 辨析：13.0 是 MIPS 降级而非完全移除——MIPS 代码在 13.x 源码树中仍存在但不再作为正式支持架构；MIPS 完全移除发生在 FreeBSD 14.0；与 sparc64、PC98、armv6 等退役架构类似，MIPS 退役是架构生态演化的自然结果
- 总纲第 23 条——社区治理：Core Team 两年一次的选举制度是 FreeBSD 治理形式化的体现——定期换届防止权力固化，选举过程向所有 committer 开放，这一制度自 FreeBSD 项目早期延续至今
  - 辨析：Core Team 成员名单随选举变动，具体成员列表需查阅对应年份的官方公告，本书记载的是制度层面的延续性而非特定个人；Core Team 决策通常采用协商一致（consensus）原则，而非投票表决，这是 BSD 社区的传统治理风格
- 总纲第 4 条——分离与聚合：ZFS 从 illumos/FreeBSD/Linux 三端分叉（分离）到 OpenZFS 统一代码库（聚合），是开源项目“分久必合”的典型案例——分叉让各平台快速适配，统一后共享维护成本
  - 辨析：OpenZFS 2.0 统一发生在 13.0 发布前（2020-11），13.0 是首个包含统一 OpenZFS 的 FreeBSD 大版本；13.0 之前 FreeBSD ZFS 维护独立分支，与 ZoL（ZFS on Linux）、illumos ZFS 存在代码分叉，这一分叉状态持续了约 13 年（2007-2020）
- 总纲第 6 条——和解优于斗争：Linux ABI 兼容层体现了 FreeBSD 的实用主义哲学——不做宗教式的“Not Invented Here”排斥，而是承认 Linux 软件生态的主导地位，提供兼容层让用户能够运行需要的软件，同时保留 FreeBSD 内核和用户态的优势
  - 辨析：Linux ABI 层不是“Linux 虚拟机”——它直接在 FreeBSD 内核上运行 Linux 二进制，没有硬件虚拟化开销，但也并非 100% 兼容；某些 Linux 特定内核功能、驱动、cgroups 深度依赖的程序可能无法正常运行；支持的 Linux 发行版版本有特定范围，不是所有 Debian/Ubuntu 版本都支持

## 辨析

- 判决并未直接裁定“API 不受版权保护”——多数意见回避了这一宪法问题，而是基于 fair use 作出判决，这是司法最小主义（judicial minimalism）的体现；判决对软件行业影响深远，但具体边界仍需后续案件澄清
  - 文献：Supreme Court of the United States. (2021-04-05). *Google LLC v. Oracle America, Inc., 593 U.S. 1*; Electronic Frontier Foundation. (2021). *Supreme Court Rules API Copying Is Fair Use*. eff.org.
- 13.0 是 MIPS 降级而非完全移除——MIPS 代码在 13.x 源码树中仍存在但不再作为正式支持架构；MIPS 完全移除发生在 FreeBSD 14.0；与 sparc64、PC98、armv6 等退役架构类似，MIPS 退役是架构生态演化的自然结果
  - 文献：FreeBSD Project. (2021). *13.0 Release Notes* (Architectures section); Tymoshenko, O. (2020-2021). freebsd-mips mailing list posts on MIPS support status.
- Core Team 成员名单随选举变动，具体成员列表需查阅对应年份的官方公告，本书记载的是制度层面的延续性而非特定个人；Core Team 决策通常采用协商一致（consensus）原则，而非投票表决，这是 BSD 社区的传统治理风格
  - 文献：FreeBSD Project. *Core Team Information*. freebsd.org/core/; FreeBSD Project. *Core Team Election Results* (2020, 2022, 2024). freebsd.org.
- OpenZFS 2.0 统一发生在 13.0 发布前（2020-11），13.0 是首个包含统一 OpenZFS 的 FreeBSD 大版本；13.0 之前 FreeBSD ZFS 维护独立分支，与 ZoL（ZFS on Linux）、illumos ZFS 存在代码分叉，这一分叉状态持续了约 13 年（2007-2020）；ZFS 文件系统本身的历史详见相关章节，本节仅讨论 13.x 时期（2021-2024）的 OpenZFS 代码库合并与版本演进，不重复 ZFS 起源叙事
- Linux ABI 层不是“Linux 虚拟机”——它直接在 FreeBSD 内核上运行 Linux 二进制，没有硬件虚拟化开销，但也并非 100% 兼容；某些 Linux 特定内核功能、驱动、cgroups 深度依赖的程序可能无法正常运行；支持的 Linux 发行版版本有特定范围，不是所有 Debian/Ubuntu 版本都支持
  - 文献：FreeBSD Project. **linux(4)** Manual Page; FreeBSD Project. *Linux Emulation* wiki page; freebsd-emulation mailing list.

## 文献

- Supreme Court of the United States. (2021-04-05). *Google LLC v. Oracle America, Inc., 593 U.S. 1*; Electronic Frontier Foundation. (2021). *Supreme Court Rules API Copying Is Fair Use*. eff.org.［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

## 149.10.2 判决对 BSD 与开源生态的意义

- FreeBSD Project. (2021). *13.0 Release Notes* (Architectures section); Tymoshenko, O. (2020-2021). freebsd-mips mailing list posts on MIPS support status.

## 149.11.2 riscv64sf（软浮点 RISC-V）退役与 riscv64 演进

- 要点：FreeBSD 13.0 移除了 riscv64sf（64 位 RISC-V 软浮点变体）架构支持，仅保留 riscv64（hard-float）作为 Tier-2 支持；riscv64 与 riscv64sf 最初由 Ruslan Bukin、Mitchell Horne（米切尔·霍恩） 等于 FreeBSD 12.0 时期移植；riscv64sf 退役原因：(1) RISC-V 规范明确 hard-float 为标准配置，软浮点仅用于早期 FPGA 原型和模拟器；(2) 主流 RISC-V 硬件（SiFive U74、Allwinner D1、StarFive JH7110 等）均使用 hard-float；(3) 维护两个 ABI 变体成本高于收益；(4) riscv64sf 实际用户基数极小；riscv64 在 13.x 期间持续改进，但仍保持 Tier-2 地位，13.x 发布 RISC-V 虚拟机镜像但不提供 RELEASE 级别的阻塞保证
- FreeBSD Project. *Core Team Information*. freebsd.org/core/; FreeBSD Project. *Core Team Election Results* (2020, 2022, 2024). freebsd.org.

## 149.5.2 Security Officer 与安全团队

- 要点：FreeBSD 13.0-RELEASE 时 Security Officer 为 Gordon Tetlow（戈登·泰特洛），Ed Maste（埃德·马斯特） 担任 Security Officer Deputy；Security Officer Team 负责安全漏洞处理、安全公告发布、安全更新协调；13.x 期间 FreeBSD 处理了多个安全漏洞，包括但不限于：CPU 侧信道漏洞（Spectre/Meltdown 系列后续变种）、网络栈漏洞、加密库问题等；WireGuard 争议也促使 Security Team 更早介入新安全功能的审查；FreeBSD 安全公告通过 freebsd-security-notify@ 邮件列表发布
- OpenZFS Project. (2020-11-30). *OpenZFS 2.0.0 Release Notes*. github.com/openzfs/zfs/releases; FreeBSD Release Engineering Team. (2021-2024). 13.x Release Notes ZFS sections.［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

## 149.6.2 OpenZFS 2.1 核心特性：zstd 压缩、Persistent L2ARC、Sequential Resilver、dRAID

- FreeBSD Project. **linux(4)** Manual Page; FreeBSD Project. *Linux Emulation* wiki page; freebsd-emulation mailing list.

## 149.7.2 bhyve 虚拟化改进

- 要点：bhyve（BSD Hypervisor）是 FreeBSD 原生虚拟化管理器，13.x 期间持续改进：(1) **13.2 起支持超过 16 个 vCPU**：bhyve 客户机之前限制最多 16 个 vCPU，13.2 解除此限制，支持更多 vCPU 以适配高性能工作负载；(2) AMD-V（AMD-Vi/AMD IOMMU）和 Intel VT-d（IOMMU）改进，包括 PCI passthrough 稳定性提升；(3) 更多外设模拟改进：NVMe 控制器模拟、virtio 设备性能改进；(4) UEFI 固件改进；(5) 快照/迁移功能持续完善；(6) 对 Linux、Windows、其他 BSD 客户机的兼容性改进；bhyve 是 FreeBSD 基金会持续资助的项目之一，iXsystems、Netgate 等公司在产品中使用 bhyve
- **bhyve(4)**、**bhyve(8)** 手册页；FreeBSD 13.2 Release Notes bhyve 章节；Peter Grehan（彼得·格雷汉）、Conrad Meyer 等 bhyve 开发者的演讲；bhyve 官网（bhyve.org）
- FreeBSD Project. src/conf/COMMITTERS; FreeBSD Release Engineering Team. (2022-05-16). 13.1-RELEASE Dedication to Bill Jolitz; FreeBSD Foundation. Annual Reports contributor lists.

## 149.9.2 Git 迁移后新贡献者路径

- 要点：Git 迁移完成后，新贡献者参与 FreeBSD 的路径更加清晰：(1) 在 GitHub 镜像（github.com/freebsd/freebsd-src）提交 Pull Request，或在 reviews.freebsd.org 提交 Gerrit 审查；(2) 经过 committer 审查后代码可被合入；(3) 多次高质量贡献后可申请 committer 权限，由现有 committer 推荐、Core Team 投票；(4) FreeBSD 基金会举办“FreeBSD Friday”等线上活动指导新贡献者；(5) Google 编程之夏（编程之夏）每年接收学生为 FreeBSD 贡献功能；与 svn 时代相比，Git 降低了参与门槛，但 committer 标准并未降低——仍需要展示对 FreeBSD 代码风格、工程文化的理解

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。
