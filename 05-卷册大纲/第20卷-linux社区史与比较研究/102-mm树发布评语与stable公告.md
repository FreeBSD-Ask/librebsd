# 102 【Linux社区】mm树发布评语与stable公告

> 来源：linux-kernel-announce 人工信 p1（10 封全读，2004-09 至 2008-06，-mm 发布评语五封（SCHED_BATCH/hrtimers 更名/PCI MSI/USB autosuspend）、stable 2.6.13.2/.3、loop-AES v2.2a、Bug 8885 实质回应）
> 体例说明：本页 10 块采用**速览体例**——块下仅存单行摘记（主题陈述＋史料锚），要点、史观、辨析、文献四字段另立详表承载；五字段完整体例见 00-总览 §一.2。本页卷头未登记 claim 编号区间，文献著录与史观映射待详表单独立卷时补录。
> 判定：10 CAND / 0 NV。主题分布：-mm 发布 2.6.15-rc5-mm2 1、-mm 发布 2.6.18-rc6-mm1 1、loop-AES v2.2a 工具公告 1、-mm 发布 2.6.17-mm4 1、stable 发布 2.6.13.2 1、bug 回应 Bug 8885 读卡器失效 1、-mm 发布 2.6.26-rc5-mm2 1、-mm 发布 2.6.16-rc6-mm1 1、-mm 发布 2.6.15-rc2-mm1 1、stable 2.6.13.3 补丁全文 1。

## 102.1 -mm 发布 2.6.15-rc5-mm2

- 【Linux社区】Andrew Morton 发布 2.6.15-rc5-mm2，共 1164 个补丁；亮点为新 CPU 调度策略 SCHED_BATCH、新版 hrtimers 代码（由 ktimers 更名而来）与大量驱动/架构更新；附逐补丁评语与 patch-list 链接。 `<!-- ROW_MINE: linux-kernel-announce.messages.719772 -->`

## 102.2 -mm 发布 2.6.18-rc6-mm1

- 【Linux社区】Andrew Morton 发布 2.6.18-rc6-mm1，共 1835 个补丁；警告“autofs4 mounting of NFS is still sick”；含 PCI MSI 代码清理、USB 自动挂起（autosuspend）基础设施、tmpfs ACL 与 /proc 清理等内容。 `<!-- ROW_MINE: linux-kernel-announce.messages.719777 -->`

## 102.3 loop-AES v2.2a 工具公告

- 【Linux社区】Jari Ruusu 发布 loop-AES v2.2a 文件/交换分区加密包；修复 sparc64 64 位内核配 32 位用户态的多密钥 ioctl 不兼容，新增 AES 密钥擦洗（KEYSCRUB，默认关闭，因密钥存储翻倍）与 I/O barrier 支持；附 tarball 地址与 md5。 `<!-- ROW_MINE: linux-kernel-announce.messages.719840 -->`

## 102.4 -mm 发布 2.6.17-mm4

- 【Linux社区】Andrew Morton 发布 2.6.17-mm4，共 819 个补丁；说明 RAID 补丁因在 -mm3 测试失败而被弃、git-sas 树恢复；新增 mmap(MAP_SHARED) 共享脏页跟踪与只读 bind mount（ro-bind-mounts）系列。 `<!-- ROW_MINE: linux-kernel-announce.messages.719859 -->`

## 102.5 stable 发布 2.6.13.2

- 【Linux社区】Chris Wright（-stable 团队）发布 2.6.13.2，附 diffstat 与修复摘要：x86-64 32 位 ioctl 丢 fput、DHCP+MASQUERADE 问题、jfs 需调 clear_inode、hpt366/sungem/sunhme PCI ROM 映射等，13 个文件改动；注明 master.kernel.org 宕机期间改用 developer.osdl.org 临时地址。 `<!-- ROW_MINE: linux-kernel-announce.messages.719935 -->`

## 102.6 bug 回应 Bug 8885 读卡器失效

- 【Linux社区】Pierre Ossman 实质回应 bugme Bug 8885（存储卡读卡器无法访问）：查看 dmesg 认为与 MMC 无关，实为 USB 读卡器（“Generic Flash R/W” 的 scsi 设备），将排查范围缩小到 USB/SCSI 一侧。 `<!-- ROW_MINE: linux-kernel-announce.messages.719938 -->`

## 102.7 -mm 发布 2.6.26-rc5-mm2

- 【Linux社区】Andrew Morton 发布 2.6.26-rc5-mm2，1354 commits 对应 931 个补丁文件；说明这是 -mm1 的修复版，主要修 vmscan.c bug，以免妨碍其余 vmscan 改动的测试；jbd/ext3 journal abort 系列补丁被弃。 `<!-- ROW_MINE: linux-kernel-announce.messages.719941 -->`

## 102.8 -mm 发布 2.6.16-rc6-mm1

- 【Linux社区】Andrew Morton 发布 2.6.16-rc6-mm1，共 1487 个补丁；新增 git-wireless（Linville，暂为空）与 git-scsi-target 树、linus.patch 更名 origin.patch、新 slab 泄漏调试设施（CONFIG_DEBUG_SLAB_LEAK）；警告 NFS 树有恙（“busy inodes - self destruct in five seconds”）。 `<!-- ROW_MINE: linux-kernel-announce.messages.719944 -->`

## 102.9 -mm 发布 2.6.15-rc2-mm1

- 【Linux社区】Andrew Morton 发布 2.6.15-rc2-mm1，共 693 个补丁；新增 git-sym2 树（Matthew Wilcox）、纳入 git-powerpc；警告 JSM tty 驱动仍无法编译；含 swap migration 与大量 MM 更新。 `<!-- ROW_MINE: linux-kernel-announce.messages.719949 -->`

## 102.10 stable 2.6.13.3 补丁全文

- 【Linux社区】Chris Wright 以回帖形式贴出 2.6.13.2 到 2.6.13.3 的补丁全文（无文字评语，diff 即修复内容）：UML 三级页表修复、skge MAC 地址设置竞态、yenta 总线号检查、IPVS 连接模板处理、TCP 窗口钳制与 UDPv6 多播修复。 `<!-- ROW_MINE: linux-kernel-announce.messages.719970 -->`
