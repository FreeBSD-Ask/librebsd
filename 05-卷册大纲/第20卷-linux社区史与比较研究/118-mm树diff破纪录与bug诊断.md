# 118. mm 树 diff 破纪录与 Bug 8885 诊断接力（ann p11）（ann p11）

> 来源：linux-kernel-announce 人工信 p11（10 封全读，2005-11 至 2019-04，-mm 发布六封（1915 补丁破纪录/32MB diff/PCI 广度优先排序副作用/Viro bird 树/每任务 I/O 计量 netlink 与 /proc/pid/io）、Bug 8885 Morton 与 Bottomley 两轮诊断、stable 2.6.14.3 diff、Kerrisk 单句回绝 NV）
> 判定：9 CAND / 1 NV。主题分布：2.6.23-rc8-mm2 发布宣告 1、2.6.15-rc1-mm1 发布宣告 1、2.6.18-rc6-mm2 发布宣告 1、Bug 8885 内存卡读取器失效回应 1、2.6.17-rc6-mm1 发布宣告 1、Linux 2.6.14.3 stable 修复内容 1、2.6.16-rc4-mm1 发布宣告 1、2.6.19-rc6-mm1 发布宣告 1、Bug 8885 内存卡读取器诊断回应 1。

## 118.1 2.6.23-rc8-mm2 发布宣告

- 【Linux社区】Andrew Morton 发布 -mm 补丁集，评语：调度器 devel 树已恢复、driver 树损坏回退至 2.6.23-rc8-mm1 版本、diff 近 32MB，共 5631 commits/2124 补丁文件 `<!-- ROW_MINE: linux-kernel-announce.messages.721754 -->`

## 118.2 2.6.15-rc1-mm1 发布宣告

- 【Linux社区】Andrew Morton 发布 -mm 树，评语“reiser4 大幅更新”，附逐组补丁说明（relayfs、spufs、tiny 伸缩项等），共 598 补丁 `<!-- ROW_MINE: linux-kernel-announce.messages.721767 -->`

## 118.3 2.6.18-rc6-mm2 发布宣告

- 【Linux社区】Andrew Morton 发布，评语：autofs4 挂载仍损坏、CONFIG_BLOCK=n 不完全可用、CONFIG_MSI=y 可能损坏、1915 补丁破纪录约多 200、警示 PCI 广度优先排序或改变设备节点 `<!-- ROW_MINE: linux-kernel-announce.messages.721779 -->`

## 118.4 Bug 8885 内存卡读取器失效回应

- 【Linux社区】Andrew Morton 回应 bug 报告：尚难判定属 SCSI/USB/MMC 哪个子系统，请 Michal 跟踪为 2.6.22 后回归并请他人分析 dmesg 定位新失效子系统 `<!-- ROW_MINE: linux-kernel-announce.messages.721840 -->`

## 118.5 2.6.17-rc6-mm1 发布宣告

- 【Linux社区】Andrew Morton 发布，评语“更多 lockdep 更新”，附逐组补丁说明（lockdep v3、fbcon 可分离、多核/SMT 调度策略等），共 1526 补丁 `<!-- ROW_MINE: linux-kernel-announce.messages.721845 -->`

## 118.6 Linux 2.6.14.3 stable 修复内容

- 【Linux社区】Chris Wright 回发 2.6.14.3 stable 版 git diff 展示修复内容：Intel 0F33/0F34 CPUID 物理地址位数规避、RTC 中断锁修正、netfilter conntrack 多项修复、IPv6 发送选项修正 `<!-- ROW_MINE: linux-kernel-announce.messages.721858 -->`

## 118.7 2.6.16-rc4-mm1 发布宣告

- 【Linux社区】Andrew Morton 发布，评语：git-jfs 因 git 问题弃用、新增 Al Viro“bird”树、ia64 因 kbuild 用 Elf_Rela 无法编译、链接期 section mismatch 警告勿报，共 1012 补丁 `<!-- ROW_MINE: linux-kernel-announce.messages.721946 -->`

## 118.8 2.6.19-rc6-mm1 发布宣告

- 【Linux社区】Andrew Morton 发布，评语：新增基于 netlink 与 /proc/pid/io 的每任务 I/O 计量，暂放 userweb.kernel.org，共 1524 补丁 `<!-- ROW_MINE: linux-kernel-announce.messages.722005 -->`

## 118.9 Bug 8885 内存卡读取器诊断回应

- 【Linux社区】James Bottomley 回应 Morton：dmesg 信息不足，需在 blockdev --rereadpt 与 fdisk 失败时抓取 dmesg，若全无输出则疑为介质变更传播问题 `<!-- ROW_MINE: linux-kernel-announce.messages.722011 -->`
