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
