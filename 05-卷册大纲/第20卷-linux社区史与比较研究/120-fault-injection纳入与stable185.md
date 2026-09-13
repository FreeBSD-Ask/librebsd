# 120. fault-injection 纳入与 stable 2.6.18.5（ann p9）（ann p9）

> 来源：linux-kernel-announce 人工信 p9（10 封全读，2005-04 至 2008-07，-mm 发布七封（fault-injection 补丁集/unionfs 与 AIO/e1000e 设备 ID 迁移/G5 全挂待 bisect）、stable 2.6.18.5、kmap_atomic 作者 Dan Williams 回应承诺修法、空洞评语格式化公告 NV）
> 判定：9 CAND / 1 NV。主题分布：2.6.17-rc5-mm2 1、2.6.19-rc5-mm2 1、2.6.18-mm3 1、2.6.20-rc4-mm1 1、Linux 2.6.18.5 1、2.6.13-rc2-mm2 1、Re: kmap_atomic() oopses in current mainline 1、2.6.26-rc8-mm1 1、2.6.24-rc4-mm1 1。

## 120.1 2.6.17-rc5-mm2

- 【Linux社区】Morton 发布 -mm 补丁集：cfq 已在主线修复故恢复 git-cfq 树，新增 lock-validator 与 genirq 修复，自曝漏更新 PCI 树，已在多平台 stress-test 通过。 `<!-- ROW_MINE: linux-kernel-announce.messages.721383 -->`

## 120.2 2.6.19-rc5-mm2

- 【Linux社区】Morton 发布 -mm 补丁集：纳入 fault-injection 补丁集并称“cool stuff”请众人试用，git-gfs2-nmw 致 Kconfig 警告，rc5-mm1 测试后丢弃数个坏补丁。 `<!-- ROW_MINE: linux-kernel-announce.messages.721399 -->`

## 120.3 2.6.18-mm3

- 【Linux社区】Morton 发布 -mm 补丁集：新增 Jeff 的消警告树 git-gccbug 与 Romieu 的 git-qla3xxx，称无线崩溃与 x86_64 IRQ 分配崩溃 hopefully 已修复，MSI 处理现称 rock-solid。 `<!-- ROW_MINE: linux-kernel-announce.messages.721425 -->`

## 120.4 2.6.20-rc4-mm1

- 【Linux社区】Morton 发布 -mm 补丁集：新增 e1000（Auke Kok）与 HID（Jiri Kosina）两个 git 树及 unionfs 文件系统，并合并文件系统 AIO 补丁组。 `<!-- ROW_MINE: linux-kernel-announce.messages.721426 -->`

## 120.5 Linux 2.6.18.5

- 【Linux社区】Chris Wright 代表 -stable 团队发布 2.6.18.5：附 diffstat 与逐条修复清单，核心为 netfilter compat 层权限/引用计数修复、fuse lookup Oops、蓝牙未对齐访问等，并回帖附完整补丁。 `<!-- ROW_MINE: linux-kernel-announce.messages.721427 -->`

## 120.6 2.6.13-rc2-mm2

- 【Linux社区】Morton 发布 -mm 补丁集：评语极简仅三条（MM 更新、video4linux 更新、Infiniband 特性工作），正文按组列补丁说明。 `<!-- ROW_MINE: linux-kernel-announce.messages.721454 -->`

## 120.7 Re: kmap_atomic() oopses in current mainline

- 【Linux社区】async_tx 作者 Dan Williams 回应 kmap_atomic 槽位冲突 bug 讨论：认可 Morton 的无条件 kmap 建议，将去掉 ASYNC_TX_KMAP 标志并提交补丁，自承今后更小心 kmap 用法。 `<!-- ROW_MINE: linux-kernel-announce.messages.721536 -->`

## 120.8 2.6.26-rc8-mm1

- 【Linux社区】Morton 发布 -mm 补丁集：x86 测试机可用但持有 mlock 的应用退出时有 sleeping-while-atomic 警告（已知问题），powerpc Mac G5 上完全无法启动待 bisect。 `<!-- ROW_MINE: linux-kernel-announce.messages.721545 -->`

## 120.9 2.6.24-rc4-mm1

- 【Linux社区】Morton 发布 -mm 补丁集：大量设备 ID 从 e1000 移往 e1000e，提醒需开 CONFIG_E1000E 否则网卡失灵；s390 构建仍坏。 `<!-- ROW_MINE: linux-kernel-announce.messages.721548 -->`
