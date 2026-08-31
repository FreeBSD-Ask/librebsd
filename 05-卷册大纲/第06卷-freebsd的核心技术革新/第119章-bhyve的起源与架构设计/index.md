---
chapter: 第 119 章
id: CH119
volume: 06
---

# 第119章 bhyve的起源与架构设计

## 要点

- bhyve 最初由 Neel Natu（nneul@）在 NetApp 工作期间开发，内部项目名为 "BSD Hypervisor"（缩写 BHyVe，发音 "bee hive"，后简化为 bhyve）；Peter Grehan（grehan@）后来成为项目主要维护者与核心贡献者，持续推动 bhyve 进入 FreeBSD 基础系统；在 bhyve 之前，FreeBSD 平台虚拟化方案主要依赖 Xen dom0/domU 移植与 QEMU/KVM 兼容层，缺乏原生的、BSD 许可的 Type-2 hypervisor 实现；bhyve 代码最初于 2011 年在 FreeBSD Perforce 仓库的 //depot/projects/bhyve/ 分支开发，后通过 SVN 导入 FreeBSD-CURRENT
- 在 bhyve 出现之前，FreeBSD 平台的硬件虚拟化方案主要依赖三条路径：第一是 Xen 的 dom0/domU 移植，FreeBSD 8.0 引入了 domU 支持（作为客户机运行），dom0 支持（作为宿主机）长期处于实验阶段，Xen 的 blkfront/netfront 驱动曾合入 FreeBSD 基础系统但维护成本高且与 FreeBSD SMP 子系统存在兼容性问题；第二是 QEMU 的 FreeBSD 移植，QEMU 作为用户态全系统模拟器可在 FreeBSD 上运行但性能极差，纯软件模拟无法利用 Intel VT-x/AMD-V 硬件虚拟化扩展；第三是 FreeBSD Jail 容器化方案，Jail 提供 OS 级虚拟化但仅支持 FreeBSD 客户机，无法运行 Linux 或 Windows；bhyve 填补了 “FreeBSD 原生硬件虚拟化” 这一空白，使 FreeBSD 首次拥有与 Linux KVM 对等的 Type-2 hypervisor
- bhyve 采用 FreeBSD License（Simplified BSD License / BSD 2-Clause License），这是一种宽松的 permissive 许可证，允许商业厂商在专有产品中集成 bhyve 而无需强制开源修改；bhyve 源码所有文件均包含标准的 FreeBSD 版权声明，版权归 FreeBSD Project 与各贡献者所有；NetApp 作为 bhyve 的初始开发方选择 BSD 许可证，使其可将 bhyve 集成到 NetApp 存储产品中而不必公开专有修改；iXsystems 基于 bhyve 构建了 TrueNAS/FreeNAS 的虚拟化功能；这与 Linux KVM（Kernel-based Virtual Machine）采用 GPLv2 许可证形成鲜明对比，KVM 的 GPL 许可证要求衍生作品必须以 GPL 发布
- bhyve 的 BSD 许可证在商业回馈模式上呈现 “双向流动” 特征：iXsystems 作为最重要的商业贡献者，将持续的工程投入回馈上游 FreeBSD——包括 bhyve 的 bug 修复、性能优化、新设备模型支持（如 NVMe 控制器模拟）、grub2-bhyve 维护等；NetApp 作为初始开发方贡献了 bhyve 的核心架构与早期代码，但后续的公开回馈较少，主要维持内部使用；Joyent 贡献了 illumos 移植相关的工程经验与部分上游补丁；这种回馈模式与 KVM 的 GPL 强制回馈形成对比——KVM 的 GPL 许可证确保所有分发修改必须开源，但也导致部分厂商选择不使用 KVM 以避免 GPL 义务（如 NetApp 选择自建 bhyve 而非使用 KVM）
- bhyve 随 FreeBSD 10.0-RELEASE 于 2014 年 1 月 20 日正式发布，首次成为 FreeBSD 基础系统的一部分（SVN revision r245652 标记为初始导入）；FreeBSD 10.0 中的 bhyve 初始版本仅支持 Intel VT-x（VMX）配合 Extended Page Tables（EPT）的硬件虚拟化扩展，要求 CPU 为 Intel Nehalem 及更新架构（不支持低端 Atom CPU），不支持 AMD SVM（AMD-V）；初始版本客户机操作系统支持有限，仅可运行 64 位 FreeBSD 与 Linux 客户机，不支持 Windows、OpenBSD/NetBSD 等其他客户机；bhyve 在 FreeBSD 10.0 中作为技术预览（technology preview）发布，标记为实验性功能

## 史观

- 总纲第 2 条——实践先于理论：bhyve 源于 FreeBSD 缺乏原生虚拟化的实际工程需求，NetApp 作为存储厂商对高效虚拟化有内部需求，而非源于学术理论或预先规划的宏大设计；这是 BSD 工程文化中 “需求驱动开发” 的典型案例
  - 辨析：bhyve 的初始作者归属存在常见误传——部分资料称 Peter Grehan 为唯一创始人，但经 FreeBSD commit log 与 bh
- 总纲第 24 条——许可证选择直接决定商业采用模式与生态走向：BSD 许可证的宽松性使 bhyve 获得了 NetApp、iXsystems、Joyent（illumos/SmartOS）等商业厂商的采用，但也意味着商业厂商可不必回馈代码，这与 KVM 在 GPL 保护下形成的庞大 Linux 云生态形成路径分岔
  - 辨析：需纠正一个常见误解——“BSD 许可证促进商业采用而 GPL 阻碍商业
- 总纲第 19 条——信息技术标准演进与硬件进步同步：bhyve 的发布时机与 Intel VT-x/EPT 在服务器 CPU 中的普及高度同步——Nehalem 架构于 2008 年发布，到 2014 年 EPT 已成为服务器 CPU 标配；FreeBSD 选择在硬件虚拟化成熟后而非提前发布 hypervisor，体现了 BSD 工程文化中 “不抢跑、等硬件就绪” 的务实传统
  - 辨析：原文标
- 总纲第 3 条——形式主义膨胀的克制：bhyve 架构设计体现了典型的 BSD 极简主义哲学——KVM 架构中 QEMU 承担了复杂的设备模拟与跨平台兼容层，代码量庞大；bhyve 则刻意保持简洁，内核模块仅实现绝对必要的硬件辅助虚拟化核心逻辑，设备模拟保持最小集合，无遗留设备兼容包袱；bhyve 用户态代码量远小于 QEMU，体现了 “够用就好、最小实现” 的工程克制
  - 辨析：bhyve
- 总纲第 2 条——实践先于理论：引导链整合并非预先规划的架构组件，而是源于 “运行非 FreeBSD 客户机” 这一实际部署需求——bhyveload 解决 FreeBSD 引导、grub2-bhyve 解决多系统引导、UEFI 固件解决 Windows 引导，三者都是按需添加、逐步演进的，而非一开始就设计了统一的引导框架
  - 辨析：bhyve UEFI 固件与 Clover/OpenCore

## 辨析

- bhyve 的初始作者归属存在常见误传——部分资料称 Peter Grehan 为唯一创始人，但经 FreeBSD commit log 与 bhyve 源码版权头交叉验证，Neel Natu 是 bhyve 内核 vmm 模块与早期用户态代码的主要初始作者，Peter Grehan 在项目导入 FreeBSD 后承担了长期维护与功能扩展工作；"bhyve" 名称的由来：BHyVe 最初为 "BS
- 需纠正一个常见误解——“BSD 许可证促进商业采用而 GPL 阻碍商业采用” 是过度简化的叙事：KVM 采用 GPLv2 许可证，但因其随 Linux 内核主线集成而获得了 AWS、Google Cloud、Azure、阿里云等几乎所有主流云厂商的大规模采用，市场份额远超 bhyve；bhyve 的 BSD 许可证确实降低了商业集成门槛，但未能形成规模生态的根本原因并非许可证，而是 FreeBSD
- 原文标题 “2014.1 FreeBSD 11.0 正式发布 bhyve” 存在严重事实错误——bhyve 首次随 FreeBSD 10.0-RELEASE（非 11.0）发布，FreeBSD 11.0 直到 2016 年 10 月才发布；FreeBSD 10.0-RELEASE 的 `release/10.0.0` tag 经 `freebsd.db` `tags` 表验证 tagger_dat
- bhyve 与 KVM/QEMU 的架构差异常被简化为 “bhyve 更简洁、KVM 更复杂”，这种比较需要放在具体语境中：KVM 作为 Linux 内核主线组件，需支持极广泛的硬件平台、客户机操作系统、向后兼容旧设备、实时迁移、内存 ballooning 等大量企业级功能，代码量庞大是功能广度的结果；bhyve 初始版本功能有限、仅支持 x86-64、仅支持现代硬件辅助虚拟化，代码简洁是范围限制
- bhyve UEFI 固件与 Clover/OpenCore 的关系需要澄清——uefi-edk2-bhyve 是标准的 TianoCore EDK II 固件移植，用于运行标准 UEFI 操作系统（如 Windows、Linux）；Clover 与 OpenCore 是 Hackintosh 社区的引导器，用于在非 Apple 硬件上启动 macOS，并非 bhyve 官方 UEFI 固件的组成

## 文献

- FreeBSD Project. **bhyve(8)** Manual Page [EB/OL]. [2026-07-19]. <https://www.freebsd.org/cgi/man.cgi?query=bhyve&sektion=8>; Grehan P. Bhyve: The BSD Hypervisor [C]//BSDCan 2012. Ottawa, 2012; FreeBSD Project. FreeBSD 10.0-RELEASE Release Notes [EB/OL]. (2014-01-20)[2026-07-19]. <<https://www.freebs>
- FreeBSD Project. FreeBSD License [EB/OL]. [2026-07-19]. <https://www.freebsd.org/copyright/freebsd-license/>; Kivity A, Kamay Y, Laor D, et al. kvm: the Linux Virtual Machine Monitor [C]//Proceedings of the Linux Symposium. 2007, 1: 225-230; bhyve source tree copyright headers. github.com/freebsd/fr
- FreeBSD Project. FreeBSD 10.0-RELEASE Release Notes [EB/OL]. (2014-01-20)[2026-07-19]. <https://www.freebsd.org/releases/10.0R/relnotes/>; FreeBSD Project. **bhyve(8)**, **vmm(4)**, **vmx(4)**, **virtio(4)** Manual Pages; Kerner S M. Open Source FreeBSD 10 Takes on Virtualization [EB/OL]. ServerWatc
- FreeBSD Project. **bhyve(8)**, **bhyveload(8)**, **bhyvectl(8)**, **vmm(4)**, **libvmmapi(3)** Manual Pages; Grehan P, Natu N. bhyve: The BSD Hypervisor Architecture [EB/OL]. BSDCan 2012 Slides; Dexter M. BHyVe: The BSD HyperVisor In Depth [C]//EuroBSDCon 2012. 2012; FreeBSD Handbook. Virtualization
- FreeBSD Project. **bhyveload(8)** Manual Page; FreeBSD Wiki. bhyve/Windows [EB/OL]. [2026-07-19]. <https://wiki.freebsd.org/bhyve/Windows>; Petersson L. Porting UEFI to bhyve [C]//BSDCan 2015. Ottawa, 2015; Grehan P. grub2-bhyve GitHub repository [EB/OL]. [2026-07-19]. <<https://github.com/grehan-fre>
- iXsystems. TrueNAS CORE Documentation: Virtual Machines [EB/OL]. [2026-07-19]. <https://www.truenas.com/docs/core/>; iXsystems. FreeNAS 11.3-U5 User Guide: Virtual Machines [EB/OL]. [2026-07-19]. <https://www.ixsystems.com/documentation/freenas/11.3-U5/virtualmachines.html>; TrueNAS Project. TrueNAS

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP194、BSD Now EP193、BSD Now EP186、BSD Now EP20（共 4 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- FreeBSD 2017 年第一季度状态报告记录 core team、基金会、ports（接近三万端口）、release engineering（11.1 排期）等团队动态，基金会赞助 168 个提交并资助多个项目。（BSD Now EP194，[98.3-164.34]，L2）
- Colin Percival 提出一种介于 Patreon 与 Bugzilla 之间的开源维护资助模型，主张以持续收入支持软件维护而非一次性赏金，从而缓解开源软件维护不足的问题。（BSD Now EP194，[878.98-1386.52]，L2）
- Chris Siebenmann 追溯 FreeBSD 目录组继承行为至 4.1cBSD 引入 mkdir 系统调用与多组进程的时期，指出新对象继承父目录组是传统 BSD 行为而非 FreeBSD 的新发明。（BSD Now EP194，[2332.28-2964.74]，L2）
- OpenBSD 变更集移除 SSHv1 协议代码，从 FreeBSD 移植 witness 锁顺序校验工具，并引入 BearSSL 常数时间 AES 实现。（BSD Now EP194，[1925.44-2328.28]，L2）
- Adrian Chadd 在 FreeBSD 802.11 栈中启动 802.11ac 支持，先针对 Atheros QCA 10K 芯片，加入 VHT 通道与 20/40/80/160MHz 模式，并说明现有栈在多虚拟接入点上的局限。（BSD Now EP193，[147.78-631.0]，L2）
- Delphix 的 Matt Ahrens 等在 OpenZFS 开发者峰会原型基础上实现 zpool checkpoint，允许管理员在执行破坏性操作前为整个池建立可回滚检查点。（BSD Now EP193，[1810.2-2535.42]，L2）
- TrueOS（原 PC-BSD）改为基于 FreeBSD current 的滚动发布，默认 Lumina 桌面；DistroWatch 评测肯定其 ZFS 集成与安装流程，但指出硬件兼容与稳定更新方面的不足。（BSD Now EP193，[2605.18-3020.76]，L2）
- LibreSSL 2.5.4 修复证书验证回调一致性与 Linux getrandom 阻塞等问题；Michael Hendricks 因 Heartbleed 后 OpenBSD 分叉 LibreSSL 的经历由 macOS 转投 OpenBSD。（BSD Now EP193，[1277.66-1583.66]，L2）
- AsiaBSDCon 2017 在东京举行，议题覆盖 FreeBSD 上的 Xen Dom0、bhyve 向 ARM 移植、OpenBSD VMM/VMD 更新与 pledge 对 capsicum 的沙箱比较。（BSD Now EP186，[432.94-560.68]，L2）
- Philipp（OpenBSD 前提交者）回顾 2002 年 Karlsruhe hackathon 参与 PF 测试与文档工作，实现接口分组并拆分 pf.c 中的 IOCTL 代码。（BSD Now EP186，[3969.0-4226.0]，L1）
- Philipp 描述 OpenBSD 路由域（rdomain）为单机上的多个虚拟路由器，可用于多租户防火墙与相同 IP 复用的隔离测试。（BSD Now EP186，[4381.84-4761.18]，L1）
- 2004 年 PF hackathon 曾发现用户态 32 位与内核 8 位规则编号溢出导致的隐蔽错误，需超过约 256 条规则才触发。（BSD Now EP186，[4227.0-4285.88]，L1）
- Neel Natu 与 Peter Grehan 在 NetApp 期间受 KVM 先例启发，思考为何 FreeBSD 没有 hypervisor；2010 年 11 月 MeetBSD 上提出构想，获 NetApp 支持后逐步开源。（BSD Now EP20，[1080.00-1205.18]，L1）
- bhyve 名称意为 BSD Hypervisor，由 Joe Catterdon 命名；初期目标是资源分区型 hypervisor，vCPU 绑定整核、内存不做虚拟化，后演进为支持虚拟化 CPU、内存与 virtio 设备的通用实现。（BSD Now EP20，[1184.42-1301.34]，L1）
- 截至访谈，bhyve 可运行 FreeBSD（回溯至 7.0）、Linux 与 OpenBSD，Illumos 因实时钟与时间戳计数器的紧校准问题尚未完成；AMD 支持在项目分支中并计划于 10.1 合并。（BSD Now EP20，[1332.70-1553.78]，L1）
- 后续目标包括 UEFI 与 VGA 以运行 Windows（拟支持 Server 2008 及以后版本）、快照与活迁移、ARM（Cortex A15）支持及作为 OpenStack 计算节点。（BSD Now EP20，[1834.62-2035.86]，L1）
- CPU 性能经 OpenSSL 基准测试几乎与宿主一致，网络因 virtio 后端缺少无状态卸载特性而仍耗用较多 CPU；控制台后端曾被改造为可指向任意字符设备。（BSD Now EP20，[1684.86-1825.34]，L1）

**史料**：

- FreeBSD Quarterly Status Report（2017 年第一季度，官网发布）（BSD Now EP194，[67.52-222.56]，L1）
- Colin Percival 于 daemonology.net 发表的开源软件维护方案博客原文（BSD Now EP194，[872.66-1467.2]，L1）
- Chris Siebenmann（University of Toronto）关于 BSD 目录组继承语义的考据博客（BSD Now EP194，[2332.28-2964.74]，L1）
- OpenBSD changes of note 621（tedu 发布的变更综述）（BSD Now EP194，[1925.44-2332.28]，L1）
- Adrian Chadd 关于 802.11ac bring-up 的博客（BSD Now EP193，[81.22-648.52]，L1）
- Delphix 关于 zpool checkpoint 的设计说明博客（BSD Now EP193，[1810.2-2600.06]，L1）
- DistroWatch 对 TrueOS 的评测文章（BSD Now EP193，[2605.18-3031.58]，L1）
- LibreSSL 2.5.4 发布说明（BSD Now EP193，[5057.4-5151.86]，L1）
- AsiaBSDCon 2017 演讲幻灯片与日程（BSD Now EP186，[432.94-560.68]，L1）
- Philipp 访谈自述（BSD Now EP186，[3969.0-5733.62]，L1）
- OpenBSD PF 邮件列表与 CVS 历史（BSD Now EP186，[3969.0-4285.88]，L1）
- 本期史料为 Neel Natu 与 Peter Grehan 访谈（当事人自述），涉及 MeetBSD 2010 演示、bhyve 项目分支、grub2-bhyve 及 FreeBSD 状态报告中的 OpenStack 合作信息。（BSD Now EP20，[1102.50-1205.18]，L1）

**史观**：

- 总纲10 动手者创造历史：状态报告显示基金会资助与普通提交者的日常维护共同推进系统细节，历史由大量默默动手者累积而成。（BSD Now EP194，[98.3-164.34]，L2）
- 总纲13 法律与道德是利益分配：开源维护资助之争的实质是贡献者劳动如何获得回报的利益分配问题，而非单纯的技术或道德问题。（BSD Now EP194，[907.04-1249.4]，L2）
- 总纲5 没有必然性，只有偶然性：BSD 目录组继承语义是 4.1cBSD 多组进程引入时的偶然工程选择，随后沉淀为传统，并非预先设计的必然。（BSD Now EP194，[2486.68-2686.36]，L2）
- 总纲10 动手者创造历史：个人开发者因自身需要推进无线与存储特性，特性落地依赖具体动手者的持续投入。（BSD Now EP193，[147.78-648.52]，L2）
- 总纲5 没有必然性，只有偶然性：OpenBSD 停止发行 CD 与 LibreSSL 分叉均由 Heartbleed、GPLv3 等具体事件触发，而非抽象规划。（BSD Now EP193，[1277.66-1583.66]，L2）
- 总纲4 分离聚合是永恒规律：OpenZFS 各发行版分叉后又聚合，zpool checkpoint 等特性先经 hackathon 快速原型，再逐步回上游。（BSD Now EP193，[1810.2-2535.42]，L2）
- 总纲10 动手者创造历史：PF 由测试者、文档者与提交者共同打磨，历史由大量动手协作的人推动。（BSD Now EP186，[4016.52-4285.88]，L1）
- 总纲4 分离聚合是永恒规律：路由域把一台物理路由器分离为多个逻辑路由器，体现分离聚合的循环。（BSD Now EP186，[4381.84-4761.18]，L1）
- 总纲6 和解优于斗争：OpenBSD 社区“批评即受邀修复”的协作方式，强调和解与共建而非对抗。（BSD Now EP186，[4016.52-4050.66]，L1）
- 总纲10 动手者创造历史：总纲10 动手者创造历史：两名开发者以业余项目推动 FreeBSD 获得原生 hypervisor，展现动手者以工程实践塑造系统能力。（BSD Now EP20，[1129.50-1205.18]，L1）
- 总纲5 没有必然性，只有偶然性：总纲5 没有必然性，只有偶然性：bhyve 由 NetApp 内部对 hypervisor 的讨论与 KVM 先例偶然触发，而非既有路线图的必然结果。（BSD Now EP20，[1080.00-1205.18]，L1）
- 总纲22 知识注定过时：总纲22 知识注定过时：初期分区型设计被后续完整虚拟化取代，说明技术路线随条件与认知演进而变更。（BSD Now EP20，[1206.02-1301.34]，L1）

**辨析**：

- [存疑脚注] Colin Percival 的开源资助方案当时仅为其个人提案，尚未落地实施，能否被社区采纳与商业化可行仍待验证。　[存疑脚注] 该方案属单一来源的个人设想，未形成实施记录。（BSD Now EP194，[1367.52-1440.28]，L4）
- [存疑脚注] DistroWatch 评测中遇到的硬件问题可能由评测者特定的 AMD APU 环境所致，未必能推广为 TrueOS 的普遍缺陷。　[存疑脚注] 单一评测者的硬件结论，需多源交叉验证。（BSD Now EP193，[2963.24-3020.76]，L4）
- [存疑脚注] 访谈中 2002 年 hackathon 地点、PF 实现细节系当事人十余年后回忆，需与 OpenBSD 邮件列表与 CVS 记录核验。　[存疑脚注] 当事人回忆性细节，缺乏独立档案印证。（BSD Now EP186，[3969.0-4285.88]，L4）
- 访谈中 Illumos 支持、AMD 合并于 10.1 及 Windows 支持时间表均为当时计划，实际落地时间与 FreeBSD 版本需核对；bhyve 早期定位为 Type 2 hypervisor 的表述与后续发展存在语境差异。　[存疑脚注] 各客户机与特性落地时间以 FreeBSD 官方发布记录为准，需交叉验证。（BSD Now EP20，[1493.70-1553.78]，L4）

**文献**：

- [BSD Now EP194] Pennington J. BSD Now: 194: Daemonic plans[EB/OL]. (2017-05-17)[2026-08-15]. https://www.bsdnow.tv/194.
- [BSD Now EP193] Pennington J. BSD Now: 193: Fire up the 802.11 AC[EB/OL]. (2017-05-10)[2026-08-15]. https://www.bsdnow.tv/193.
- [BSD Now EP186] Pennington J. BSD Now: 186: The Fast And the Firewall: Tokyo Drift[EB/OL]. (2017-03-22)[2026-08-15]. https://www.bsdnow.tv/186.
- [BSD Now EP20] Pennington J. BSD Now: 20: Bhyve Mind[EB/OL]. (2014-01-15)[2026-08-15]. https://www.bsdnow.tv/20.

<!-- /PODCAST_REVIEW -->
