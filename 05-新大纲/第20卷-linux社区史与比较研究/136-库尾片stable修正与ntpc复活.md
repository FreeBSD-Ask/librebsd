# 136 【Linux社区】库尾片stable修正与ntpc复活

> 来源：linux-kernel-announce 人工信 p23（5 封全读，2005-03 至 2007-04，库尾片：stable 2.6.13.1 修正 diff（i386 PCI 资源重做/crypto 溢出/aacraid 校验）、git-sas 首纳、reiser4 新代码投放、ntp/time 重构复活与 hot-fixes 目录、“比 rc7-mm1 稳定得多”）
> 判定：5 CAND / 0 NV。主题分布：stable 2.6.13.1 修正 diff 1、-mm 快照 2.6.14-rc2-mm1 发布 1、-mm 快照 2.6.12-rc1-mm4 发布 1、-mm 快照 2.6.16-rc1-mm5 发布 1、-mm 快照 2.6.21-rc7-mm2 发布 1。

> **体例说明（2026-09-14 整改）**：本页 5 块为“速览体例”——各块正文仅保留【Linux社区】条目行与 `<!-- ROW_MINE -->` 定位锚，五字段（要点/史料/史观/辨析/文献）不作逐块展开；块级要点与史观映射见下方“速览详表”，史料即各块 ROW_MINE 锚（`raw_source.raw_json` 可逐条反查），DSLXC claim 著录待 claim 库重跑时统一回填（DEFERRED）。

## 【Linux社区】速览详表（块级要点与史观映射）

| 块号 | 块题 | 要点（浓缩） | 史观映射 |
| --- | --- | --- | --- |
| 136.1 | stable 2.6.13.1 修正 diff | Chris Wright（osdl.org，stable@kernel.org）以“Re: Linux 2.6.13.1”发布 2.6.13.1 稳定版修复的完整 diff 本体：Makefile EXTRAVERSION 置 .1，含 i386 PCI 资源分配重做、crypto CBC/ECB 处理 nbytes 计数溢出修复、rtc 中断改 SA_SHIRQ 共享、saa7134 DVB 补 TDA1004X 依赖、pci_enable_rom 地址修正、CARDBUS IO 上限改 4K、aacraid fibsize 校验、32 位 compat cmsg 多重加固、BPF 越界与 IP 分片 pskb_trim_rcsum、raw sendmsg __get_user 改 get_user 等 | 经验优先（总纲 9：以完整 diff 本体为唯一证据）；动手者叙事（总纲 10：修复本体即维护者行动留痕）；多方平等（总纲 8：PCI、crypto、DVB、网络、安全多线并置） |
| 136.2 | -mm 快照 2.6.14-rc2-mm1 发布 | 新增 git-sas.patch 引入 Luben Tuikov 的 SAS 驱动及其支持、“其余零散改动无大项”，正文给出 git 子系统树清单与自 2.6.14-rc1-mm1 以来的增删补丁逐条注记（UMT/input 类层级化、x86_64 no-idle-tick、kdump、cs5535 新声卡驱动、USB 电源状态等），末尾附 484 补丁 patch-list 链接 | 动手者叙事（总纲 10：新增与注记由发布者列举）；经验优先（总纲 9：以逐条增删注记为量化口径）；分离聚合是永恒规律（总纲 4：git 子系统树的聚散与逐版重组） |
| 136.3 | -mm 快照 2.6.12-rc1-mm4 发布 | 评语核心为“reiser4 新代码投放”与“各种新修复与清理”，并征集 DRI 问题与 PM 恢复问题的反馈；正文列出 bk 子系统树、增删补丁逐条注记（sparsemem 预备、cpusets、kexec/kdump 重整、PCMCIA 设备匹配大系列、nfsd4 修复、FUSE 全套、inotify-43 等），统计 -mm 636 补丁、外部树 746 changeset、总计 1360 补丁 | 动手者叙事（总纲 10：投放与清理由发布者给出）；经验优先（总纲 9：以 636/746/1360 的量化口径为判据）；多方平等（总纲 8：内存、cpuset、kexec、PCMCIA、FUSE 多线并置） |
| 136.4 | -mm 快照 2.6.16-rc1-mm5 发布 | John Stultz 的 ntp/time 重构补丁复活并修复、新增 hot-fixes 目录提示；Known problems 一节详述 kbuild 新增重复 EXPORT_SYMBOL 检测的告警样例、为何修复并不平凡（generic/arch 双边约束）及把 EXPORT_SYMBOL 紧跟符号之后等提交规范，另有 -mm 二分排查与 bug 报告抄送维护者的 boilerplate；自 2.6.15-mm4 起增删补丁逐条注记（mempool 库化、kprobes booster、多核调度域、time/clocksource 基础设施等），共 869 补丁 | 动手者叙事（总纲 10：规范与注记由发布者给出）；经验优先（总纲 9：以重复 EXPORT_SYMBOL 检测告警样例为判据）；循环结构呈现（总纲 4：ntp/time 重构补丁复活，属反复回归的技术议题） |
| 136.5 | -mm 快照 2.6.21-rc7-mm2 发布 | 评语核心为“包含 2.6.21 全部内容并更多”、修复多个恶性 bug 而“应比 2.6.21-rc7-mm1 稳定得多”，提示 sysfs 相关问题可调 CONFIG_SYSFS_DEPRECATED 规避；因需重构而丢弃 64 位 futex 及 private-futex 补丁、非特权挂载代码待新补丁系列后再入、大量 fbdev 小 bug 已修（“fbdev bugstomp”系列）；附 git 取树、mm-commits 订阅、二分排查等 boilerplate，自 rc7-mm1 起增删逐条注记，共 1993 补丁 | 自反性声明（总纲 7：以“应比 rc7-mm1 稳定得多”自评本版相对状态）；动手者叙事（总纲 10：丢弃与待入由发布者交代）；知识注定过时（总纲 22：因需重构而丢弃 futex 补丁，属阶段性取舍） |

---

## 136.1 stable 2.6.13.1 修正 diff

- 【Linux社区】Chris Wright（osdl.org，stable@kernel.org）以“Re: Linux 2.6.13.1”发布 2.6.13.1 稳定版修复的完整 diff 本体：Makefile EXTRAVERSION 置 .1，含 i386 PCI 资源分配重做（恢复 pci_assign_unassigned_resources）、crypto CBC/ECB 处理 nbytes 计数溢出修复、rtc 中断改 SA_SHIRQ 共享、saa7134 DVB 补 TDA1004X 依赖、pci_enable_rom 地址修正、CARDBUS IO 上限改 4K、aacraid fibsize 校验改用 dev->max_fib_size、32 位 compat cmsg 多重加固（sock_kmalloc 与长度校验）、BPF 越界与 IP 分片 pskb_trim_rcsum、raw sendmsg __get_user 改 get_user 等修复内容。 `<!-- ROW_MINE: linux-kernel-announce.messages.725041 -->`

## 136.2 -mm 快照 2.6.14-rc2-mm1 发布

- 【Linux社区】Andrew Morton 发布 2.6.14-rc2-mm1（FTP 链接），评语核心为新增 git-sas.patch 引入 Luben Tuikov 的 SAS 驱动及其支持、“其余零散改动无大项”，正文给出 git 子系统树清单与自 2.6.14-rc1-mm1 以来的增删补丁逐条注记（UMT/input 类层级化、x86_64 no-idle-tick、kdump、cs5535 新声卡驱动、USB 电源状态等），末尾附 484 补丁 patch-list 链接。 `<!-- ROW_MINE: linux-kernel-announce.messages.725050 -->`

## 136.3 -mm 快照 2.6.12-rc1-mm4 发布

- 【Linux社区】Andrew Morton 发布 2.6.12-rc1-mm4（FTP 链接），评语核心为“reiser4 新代码投放”与“各种新修复与清理”，并征集 DRI 问题与 PM 恢复问题的反馈；正文列出 bk 子系统树、增删补丁逐条注记（sparsemem 预备、cpusets、kexec/kdump 重整、PCMCIA 设备匹配大系列、nfsd4 修复、FUSE 全套、inotify-43 等），统计 -mm 636 补丁、外部树 746 changeset、总计 1360 补丁。 `<!-- ROW_MINE: linux-kernel-announce.messages.725075 -->`

## 136.4 -mm 快照 2.6.16-rc1-mm5 发布

- 【Linux社区】Andrew Morton 发布 2.6.16-rc1-mm5（FTP 链接），评语核心为 John Stultz 的 ntp/time 重构补丁复活并修复、新增 hot-fixes 目录提示；Known problems 一节详述 kbuild 新增重复 EXPORT_SYMBOL 检测的告警样例、为何修复并不平凡（generic/arch 双边约束）及把 EXPORT_SYMBOL 紧跟符号之后等提交规范，另有 -mm 二分排查与 bug 报告抄送维护者的 boilerplate；自 2.6.15-mm4 起增删补丁逐条注记（mempool 库化、kprobes booster、多核调度域、time/clocksource 基础设施等），共 869 补丁。 `<!-- ROW_MINE: linux-kernel-announce.messages.725154 -->`

## 136.5 -mm 快照 2.6.21-rc7-mm2 发布

- 【Linux社区】Andrew Morton（linux-foundation.org）发布 2.6.21-rc7-mm2（FTP 链接），评语核心为“包含 2.6.21 全部内容并更多”、修复多个恶性 bug 而“应比 2.6.21-rc7-mm1 稳定得多”，提示 sysfs 相关问题可调 CONFIG_SYSFS_DEPRECATED 规避；说明因需重构而丢弃 64 位 futex 及 private-futex 补丁、非特权挂载代码待新补丁系列后再入、大量 fbdev 小 bug 已修（“fbdev bugstomp”系列）；附 git 取树、mm-commits 订阅、二分排查等 boilerplate，自 rc7-mm1 起增删逐条注记，共 1993 补丁。 `<!-- ROW_MINE: linux-kernel-announce.messages.725156 -->`
