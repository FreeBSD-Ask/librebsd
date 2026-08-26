---
chapter: 第 136 章
id: CH136
volume: 07
---

## 要点

- FreeBSD 的基础安全模型继承自传统 UNIX 自主访问控制（Discretionary Access Control, DAC），该模型由 丹尼斯·里奇（Dennis Ritchie）和 肯·汤普森（Ken Thompson）在 1970 年代初的 UNIX 第一版中设计；核心机制包括：每个文件/目录有 12 个权限位——owner（用户）读/写/执行、group（组）读/写/执行、other（其他）读/写/执行，加上 setuid（设置用户 ID）、setgid（设置组 ID）、sticky bit 三个特殊位；setuid/setgid 机制允许程序以文件所有者（通常是 root）的权限运行，这是 UNIX 权限提升的核心机制，但也是历史上大量本地提权漏洞的来源；root 用户（UID 0）在传统 DAC 模型下拥有对系统的完全控制权，绕过所有权限检查——"root  omnipotent" 是传统 UNIX 安全模型最显著的特征也是最大的安全弱点
- 在传统 UNIX DAC 模型中，UID 0（root）是 “超级用户”，内核中所有权限检查对 UID 0 直接放行；FreeBSD 历史上通过多种机制对 root 权限进行限制：**securelevel(7)** 机制（1980 年代 BSD 引入，通过 `kern.securelevel` sysctl 控制系统安全级别，高级别下 root 也无法执行某些操作如修改不可变文件、直接访问原始磁盘、加载内核模块等）；**jail(8)** 将 root 限制在 jail 内部；MAC 框架可进一步限制 root 操作；Capsicum 能力模式下即使是 root 也受能力描述符限制；FreeBSD 的 securelevel 有五个级别[存疑脚注：原文误作“四个级别”；FreeBSD Handbook 明确记载 'The kernel runs with five different security levels’，即 -1/0/1/2/3]：-1（完全禁用）、0（默认，不安全）、1（安全模式，不可修改不可变文件、不能加载模块）、2（高安全，进一步限制磁盘操作和原始套接字）、3（最高安全，与 2 类似但某些计时参数调整也被禁止）
- **jail(8)** 由 Poul-Henning Kamp（波尔-亨宁·坎普） 设计，首次出现在 FreeBSD 4.0-RELEASE（2000 年 3 月 14 日发布），是 FreeBSD 首个原生 OS 级虚拟化机制；原始 jail 通过 **chroot(2)** 增强实现，为监禁进程提供独立的主机名、IP 地址、文件系统根目录视图，但 jail 内 root 用户仍受诸多限制（如无法修改内核参数、无法加载模块、无法访问原始套接字等）；jail 的设计目标是作为安全隔离环境而非完整虚拟化方案，与传统 chroot 相比增加了对进程间通信、网络、系统 VIPC 等资源的隔离约束；FreeBSD 4.x 时代的 jail 存在若干已知逃逸漏洞（如通过特定 sysctl 或挂载点逃逸），后续版本持续加固
- Capsicum 能力模型由剑桥大学 罗伯特·N. M. 沃森 团队设计，核心论文发表于 USENIX Security 2010，FreeBSD 9.0-RELEASE（2012 年 1 月 12 日）首次在 GENERIC 内核中集成 Capsicum 框架（options CAPABILITIES 和 options CAPABILITY_MODE）；Pawel Jakub Dawidek 在 FreeBSD 基金会与 Google 开源计划办公室联合资助下（2013 年 4 月公告）完成了 Capsicum 从研究原型到产品级代码的工程化，开发了 **casperd(8)** 服务守护进程和 **libcapsicum(3)**/**libcasper(3)** 库；FreeBSD 基础系统中首批 Capsicum 化工具包括 **tcpdump(1)**、**dhclient(8)**、**kdump(1)**、**killall(1)**、**timeout(1)**、**dd(1)** 等；Capsicum 的核心创新是对象能力模型——进程通过 **cap_enter(2)** 进入能力模式后丧失所有全局命名空间访问权，仅能通过已持有的能力文件描述符访问资源
- CHERI（Capability Hardware Enhanced RISC Instructions）是剑桥大学与 SRI International 联合开发的硬件能力架构，为 Capsicum 类能力模型提供硬件级强制保护；CheriBSD 是基于 FreeBSD 的 CHERI 参考实现，扩展了 Capsicum 能力模型至硬件层面，通过能力指针（fat pointers）替代传统整数指针，在硬件层面强制执行内存安全和控制流完整性；CHERI-MIPS、CHERI-RISC-V、Arm Morello（2021 年 Arm 发布的 CHERI 原型 SoC）是 CHERI 架构的主要硬件实现；FreeBSD 基金会 2024 年资助了 Capsicum+bhyve 安全审计，由 Shawn Webb 与 Mariusz Zaborski 执行，部分审计结果为 CHERI 硬件能力与软件能力模型结合提供了实践依据

## 史观

- 总纲第 1 条——项目统摄史观：传统 UNIX DAC 是 FreeBSD 安全模型的 “源头时刻”——1970 年代初在 PDP-7/PDP-11 上设计的简单权限模型在五十多年后仍是 FreeBSD（以及所有类 UNIX 系统）安全的基础；这一模型的简单性（9 个基本权限位 +3 个特殊位）是其持久生命力的来源，但其 “root 万能” 的设计假设在网络时代成为严重安全缺陷；FreeBSD 后
- 总纲第 1 条——项目统摄史观：jail 的诞生是 FreeBSD 安全演进的第一个 “源头时刻”——Kamp 在 2000 年选择在单体内核中以 “强制隔离 + 资源限制” 方式实现进程监禁，而非采用当时新兴的虚拟化技术（如 VMware、Xen）或微内核方案，这一工程决策奠定了 FreeBSD 此后二十余年容器化技术的基础；jail 比 Solaris Zones（2004）、Linux VS
- 总纲第 21 条——密码学：MAC 框架是 FreeBSD 对 TCSEC（Orange Book，橘皮书）B 级安全要求的回应——橘皮书 B1 级要求强制访问控制（MAC）支持，MAC 框架的设计直接参考了 TCSEC B1/B2 级和 Common Criteria 的要求；但 FreeBSD 从未以获得 TCSEC/CC 认证为目标——框架提供机制（mechanism）而非策略（policy
- 总纲第 3 条——形式主义膨胀：安全审计是高安全等级操作系统（TCSEC C2 及以上、Common Criteria）的形式化要求——但与 MAC 框架类似，FreeBSD 提供审计机制但不追求认证；OpenBSM 的选择体现了 FreeBSD 对“复用成熟标准化技术”的偏好——BSM 审计格式自 1990 年代 Solaris C2 安全认证以来即为审计领域的事实标准，采用该格式便于与现有审计

## 辨析

- “FreeBSD 抛弃了传统 UNIX 权限模型” 说法错误——传统 DAC 仍是 FreeBSD 默认且最基础的安全机制，MAC、Capsicum、jail 等是叠加在 DAC 之上的可选安全层，不是替代；“setuid 本身是安全漏洞” 说法不准确——setuid 是一种机制，其安全性取决于 setuid 程序的实现质量；历史上 BSD 对 setuid 程序的安全审计比其他 UNIX 变体更
- 关于 “jail 是 chroot 的安全增强版” 说法需精确区分：**chroot(2)** 仅改变文件系统根目录，不限制进程系统调用访问，root 用户可轻易逃逸；**jail(8)** 从内核层面增加多层隔离，但 FreeBSD 4.x 时代的原始 jail 仍非完美——2000-2005 年间发现多个 jail 逃逸路径；“jail 与 Docker 技术等价” 说法不准确——Docker
- “TrustedBSD MAC 框架是 FreeBSD 版的 SELinux” 说法过于简化——SELinux 最初是 NSA 为 Linux 设计的 FLASK/TE 安全架构，移植到 FreeBSD 时作为 MAC 框架的一个策略模块（mac_flask），而非 MAC 框架本身；MAC 框架比 LSM（Linux Security Modules）更早起步（2000 年 vs LSM 200
- “FreeBSD audit 是 Sun 代码的直接移植”说法不完全准确——OpenBSM 是 BSM API 和审计格式的独立开源重新实现（clean-room reimplementation），并非从 Solaris 源码直接移植；这是为了避免 CDDL（Sun CDDL 许可证）与 BSD 许可证的兼容性问题；OpenBSM 与 Solaris BSM 在 API 和日志格式层面兼容，但实

## 文献

- Ritchie D M, Thompson K. The UNIX Time-Sharing System [J]. Communications of the ACM, 1974, 17(7): 365-375; Bach M J. The Design of the UNIX Operating System [M]. Prentice-Hall, 1986. ISBN 978-0-13-201799-2; FreeBSD Project. **chmod(1)**, **chown(8)**, **setuid(2)** Manual Pages. ［B］
    FreeBSD 社区论
- Kamp P H, Watson R N M. Jails: Confining the Omnipotent Root [C]. Proceedings of the 2nd International SANE Conference, 2000; FreeBSD Project. FreeBSD 4.0-RELEASE Release Notes (2000-03-14). freebsd.org; FreeBSD Project. **jail(8)**, **jail(2)** Manual Pages; McKusick M K, Neville-Neil G V, Watson R
- Watson R N M. New Approaches to Operating System Security Extensibility [D]. University of Cambridge Computer Laboratory, 2012 (UCAM-CL-TR-818); FreeBSD Project. FreeBSD 5.0-RELEASE Release Notes & Early Adopter's Guide (2003-01-19). freebsd.org; TrustedBSD Project. trustedbsd.org; FreeBSD Project. 
- TrustedBSD Project. OpenBSM. trustedbsd.org/openbsm/; FreeBSD Project. **audit(4)**, **auditd(8)**, **auditreduce(8)**, **praudit(8)**, **openbsm(3)** Manual Pages; FreeBSD Project. FreeBSD 6.2-RELEASE Release Notes (2007-01-15). freebsd.org; Watson R N M et al. OpenBSM: Open Source Implementation o

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。