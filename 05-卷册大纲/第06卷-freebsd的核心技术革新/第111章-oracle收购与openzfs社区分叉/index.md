---
chapter: 第 111 章
id: CH111
volume: 06
---

# 第111章 oracle收购与openzfs社区分叉

## 要点

- Oracle 于 2009 年 4 月 20 日宣布以 74 亿美元收购 Sun Microsystems，交易于 2010 年 1 月 27 日完成；Oracle 收购 Sun 的核心商业动机包括：获得 Java 编程语言和平台的控制权、获得 Solaris 操作系统及 SPARC 处理器技术、获得 MySQL 数据库（后续引发 MySQL 开源社区 fork 为 MariaDB）、获得 Sun 的硬件产品线和专利组合；收购后 Oracle CEO Larry Ellison 明确表示将以 “专有软件” 模式运营 Solaris，逐步关闭 OpenSolaris 项目；OpenSolaris 治理委员会（OGB, OpenSolaris Governing Board）于 2010 年 8 月在 Oracle 任命的新领导层下解散；2010 年 8 月 13 日，一份内部 Oracle 备忘录泄露，显示 Oracle 将不再以开源方式发布 Solaris 后续版本，而是改为封闭开发、仅发布二进制更新
- OpenSolaris 关闭对 ZFS 社区的直接冲击是：ZFS 上游开发从 “Sun 主导的开源项目” 变为 “Oracle 封闭开发”，社区无法再从 Solaris 获得 ZFS 新功能的开源代码；Bonwick、Ahrens 等 Sun/ZFS 核心工程师大多留在 Oracle（至少短期留任），但 Oracle ZFS 团队与社区沟通几乎中断；已有的 OpenSolaris ZFS 代码（截至 2010 年 8 月的 ON build）因 CDDL 许可是永久自由的，社区有权在其基础上 fork 并继续开发；受影响的不仅是 ZFS——整个 OpenSolaris 生态（包括 DTrace、Zones、Crossbow、SMF 等）都面临同样的断供危机；FreeBSD 的 ZFS 移植在 2010 年前已相对独立维护，因此受冲击小于 illumos 社区
- OpenSolaris 关闭后 ZFS 生态的 fork 路径：Garrett D'Amore（前 Sun 工程师，Nexenta Systems 员工）于 2010 年 8 月 3 日发起 illumos 项目作为 OpenSolaris 的社区 fork，illumos 成为 ZFS 开源开发的事实上的上游；illumos 初期由 Nexenta 赞助，后发展为独立的社区治理项目；除 illumos 外，ZFS On Linux（ZoL，Brian Behlendorf（布莱恩·贝伦多夫） 2008 年在 LLNL 发起）在 2010-2013 年间也发展为独立的 ZFS 实现；2013 年，Matt Ahrens 联合各平台 ZFS 开发者在首届 OpenZFS Developer Summit 上正式宣布成立 OpenZFS 项目作为跨平台 ZFS 协作的 umbrella 组织
- Oracle 收购 Sun 及 OpenSolaris 关闭的关键日期交叉验证：Oracle 宣布收购 Sun：2009 年 4 月 20 日（Oracle/Sun 新闻稿、SEC filing 均确认）；欧盟反垄断审查通过：2010 年 1 月 21 日；收购完成：2010 年 1 月 27 日（SEC filing 确认）；illumos 项目启动：2010 年 8 月 3 日（Garrett D'Amore 邮件确认）；OpenSolaris Governing Board 解散：2010 年 8 月（OGB 会议纪要）；Oracle 内部备忘录泄露：2010 年 8 月 13 日（多个来源存档）；Oracle Solaris 11 发布：2011 年 11 月（首个完全闭源开发的 Solaris 版本）；需注意：OpenSolaris 从未被 Oracle “正式关闭”，而是通过停止更新开源代码仓库、解散治理委员会、撤回对社区版的支持等方式被 “实质终止”
- OpenZFS 项目于 2013 年正式成立，首届 OpenZFS Developer Summit 于 2013 年 11 月 18-19 日在旧金山举行；OpenZFS 由 Matt Ahrens（Delphix）发起，联合各平台 ZFS 开发者共同建立跨平台治理结构；OpenZFS Bylaws 规定了项目治理结构：选举产生的指导委员会（Governing Board）、各平台代表席位（FreeBSD、Linux、illumos、macOS/Windows 等）、代码贡献流程、发布流程；OpenZFS 商标最初由 Matt Ahrens 个人持有，后转让至 OpenZFS 组织；OpenZFS 的核心目标是建立跨平台的共享 ZFS 代码库，减少各平台移植之间的代码分叉

## 史观

- 总纲第 24 条——许可证：Oracle 收购 Sun 是开源史上最具争议的商业事件之一，它直接证明了单一商业实体控制开源项目的风险——尽管 OpenSolaris 以 CDDL 开源，Oracle 作为版权持有者可以选择不再发布新版本的开源代码，社区无法强迫 Oracle 继续开源贡献；这是 CDDL/MPL 类文件级 copyleft 许可证相对于 GPL 的一个弱点
  - 辨析：Oracl
- 总纲第 25 条——终结与延续：OpenZFS 的成立标志着 ZFS 从 “Sun/Oracle 的项目” 彻底转变为 “社区拥有的项目”——这是一个历史终结与新生的节点：Sun 时代的 ZFS 终结了，社区自治的 ZFS 诞生了；Bylaws 这一形式化治理文件的制定，体现了开源项目从 “仁慈独裁者” 模式向制度化治理的转变
  - 辨析：OpenZFS 成立的精确时间：第一届 OpenZFS
- 总纲第 6 条——技术路线分化：ZoL 的模块加载策略是法律约束下的工程妥协——ZFS 无法进入主线内核，因此通过 DKMS/LKM 方式在主线外分发；这种 “核外生存” 模式虽然有性能和维护成本，但在法律灰区中开辟了一条可行路径
  - 辨析：需澄清：Linux 内核的 GPL 许可范围问题——Linux 内核 COPYING 文件明确指出 "kernel modules are conside

## 辨析

- Oracle 收购 Sun 的精确日期：宣布日为 2009 年 4 月 20 日，完成日（交易交割）为 2010 年 1 月 27 日，两者常被混淆；OpenSolaris 的 “关闭” 是一个渐进过程而非单一事件——2010 年 8 月的泄露备忘录确认了封闭政策，但 OpenSolaris 源代码在 2010 年 8 月后仍可访问一段时间，直到 Oracle 将其从公开仓库中移除
  - 文献：
- OpenZFS 成立的精确时间：第一届 OpenZFS Developer Summit 于 2013 年 11 月举行，但 OpenZFS 作为协作项目的筹备始于 2012-2013 年，Matt Ahrens 等人在多个会议上提出了跨平台 ZFS 统一的构想；OpenZFS 不是从零创建 ZFS 的 fork，而是一个协调已有 ZFS 实现（illumos ZFS、ZoL、FreeBSD ZF
- 需澄清：Linux 内核的 GPL 许可范围问题——Linux 内核 COPYING 文件明确指出 "kernel modules are considered derivative works"，但内核社区实际上长期容忍非 GPL 模块（NVIDIA、VMware 等闭源驱动，以及 OpenAFS 等 CDDL 模块），这形成了事实上的 “模块例外” 实践；ZoL 的法律地位在理论上有争议，但在

## 文献

- Oracle Corporation. (2009-04-20). *Oracle to Buy Sun Microsystems*. Press Release; SEC. *Oracle-Sun Merger Filings*. sec.gov; OpenSolaris Governing Board. (2010-08). *Meeting Minutes and Resignation Letter*. opensolaris.org (archived); LWN.net (2010-08-16). *What's Next for OpenSolaris*. lwn.net.[考据
- OpenZFS Project. *Bylaws*. openzfs.org/wiki/Bylaws; Ahrens, M. (2013). *The OpenZFS Project*. LinuxCon North America 2013; OpenZFS Developer Summit 2013 Schedule. openzfs.org; Behlendorf B. zfs-0.4.1. openzfs-zfs 仓库 tag [DB/OL]. 2009-01-21T12:25:52-08:00. tag: zfs-0.4.1; commit: a66e5effd5c81f504fca
- Behlendorf, B. (2008). *ZFS on Linux Launch*. zfsonlinux.org; ZFS on Linux Project. *SPL: Solaris Porting Layer*. github.com/openzfs/spl; Linux Kernel Project. *COPYING File* (module licensing note). kernel.org.[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
    Fr

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。
