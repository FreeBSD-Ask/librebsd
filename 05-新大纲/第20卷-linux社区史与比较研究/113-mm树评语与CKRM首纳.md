# 113 【Linux社区】mm树评语与CKRM首纳

> 来源：linux-kernel-announce 人工信 p5（10 封全读，2004-05 至 2008-03，-mm 发布七封（CKRM 仅供围观首纳/mutex 子系统引入/openat 等 *at() 调用/unshare 撤销/udev 旧版检测吐槽/ext4 禁用）、stable 2.6.13.2 diff 全文与 2.6.15.4、loop-AES v2.1b）
> 体例说明：本页 10 块采用**速览体例**——块下仅存单行摘记（主题陈述＋史料锚），要点、史观、辨析、文献四字段另立详表承载；五字段完整体例见 00-总览 §一.2。本页卷头未登记 claim 编号区间，文献著录与史观映射待详表单独立卷时补录。
> 判定：10 CAND / 0 NV。主题分布：-mm 发布 2.6.15-mm1 1、stable 2.6.13.2 补丁全文 1、-mm 发布 2.6.19-rc3-mm1 1、loop-AES v2.1b 工具公告 1、-mm 发布 2.6.25-rc3-mm1 1、-mm 发布 2.6.14-rc1-mm1 1、-mm 发布 2.6.13-rc3-mm1 1、stable 发布 2.6.15.4 1、-mm 发布 2.6.15-mm2 1、-mm 发布 2.6.17-rc1-mm3 1。

## 113.1 -mm 发布 2.6.15-mm1

- 【Linux社区】Andrew Morton 发布 2.6.15-mm1，共 1455 个补丁；警告 ppc32 编译损坏；新增 CONFIG_DEBUG_SHIRQ 调试选项（在驱动 request_irq 后立即模拟共享中断，已搞坏一个驱动，请 testers 尝试并回报）；逐补丁评语含 menuconfig 配色修复、AMD Geode GX/LX 支持、John Stultz 新时间管理代码、fuse 与 SPI 更新等。 `<!-- ROW_MINE: linux-kernel-announce.messages.720611 -->`

## 113.2 stable 2.6.13.2 补丁全文

- 【Linux社区】Chris Wright 以回帖形式贴出 2.6.13.1 到 2.6.13.2 的补丁全文（无文字评语，diff 即修复内容）：x86_64 ia32 tiocgdev 补 fput_light、cmd64x/hpt34x/hpt366 PCI ROM 改用 dword 访问、sungem/sunhme 改用 pci_map_rom 读 MAC、forcedeth 强制重估链路速度、ftdi_sio baud_base 修正、jfs delete_inode 重构、MASQUERADE 跳过 0.0.0.0 源地址包。 `<!-- ROW_MINE: linux-kernel-announce.messages.720621 -->`

## 113.3 -mm 发布 2.6.19-rc3-mm1

- 【Linux社区】Andrew Morton 发布 2.6.19-rc3-mm1，共 1028 个补丁；警告 ia64 因 acpi 改进而无法编译（“已经修了一大串编译错误，该轮到别人了”）；吐槽 Greg 恢复 udev 旧版检测补丁是“为旧 udev 惩罚用户”，驱动树“明知会弄坏旧 udev 仍照发”，并回退 tty 一项以让自己机器可用；称 struct path 转换 102 个补丁是“做点无意义的事”。 `<!-- ROW_MINE: linux-kernel-announce.messages.720633 -->`

## 113.4 loop-AES v2.1b 工具公告

- 【Linux社区】Jari Ruusu 发布 loop-AES v2.1b 文件/交换分区加密包：适配 2.6.7-rc1-mm1 内核、修复 md-raid0/md-linear 上层 loop 的 bio vec merge bug（仅影响 2.6 内核）、启用 2.6 内核 bio write barrier（QUEUE_FLAG_ORDERED）；同时更新附加加密包 ciphers v2.0h（仅适配内核），附 tarball 地址、md5 与签名。 `<!-- ROW_MINE: linux-kernel-announce.messages.720634 -->`

## 113.5 -mm 发布 2.6.25-rc3-mm1

- 【Linux社区】Andrew Morton 发布 2.6.25-rc3-mm1，2993 commits 对应 1101 个补丁文件；调侃 IDE 树“一如既往的活跃”；因 ext4 使用 -mm 已删除的旧接口而整体禁用 ext4；收录其趁 Dmitry Torokhov 缺席期间积攒的输入子系统补丁；介绍 mmotm 快照（“几乎肯定无法编译”）与二分查找指引。 `<!-- ROW_MINE: linux-kernel-announce.messages.720637 -->`

## 113.6 -mm 发布 2.6.14-rc1-mm1

- 【Linux社区】Andrew Morton 发布 2.6.14-rc1-mm1，共 440 个补丁；称 reiser4 大更新“据说回应了全部评审意见”；引入 Dmitry Torokhov 的 sysfs/input 大改造第一版（动态 input_dev 分配等）；警告大量 tty 驱动仍无法编译；新增 oops 报告脚本并征求“这有用吗”。 `<!-- ROW_MINE: linux-kernel-announce.messages.720677 -->`

## 113.7 -mm 发布 2.6.13-rc3-mm1

- 【Linux社区】Andrew Morton 发布 2.6.13-rc3-mm1，共 591 个补丁；首次纳入 CKRM（类内核资源管理）补丁集，注明“仅供大家围观”；完成 pm_message_t 向结构体转换的第三次尝试，“现在看起来没问题”；自嘲头文件清理“浪费不少时间”；新增 /proc/pid/numa_maps。 `<!-- ROW_MINE: linux-kernel-announce.messages.720681 -->`

## 113.8 stable 发布 2.6.15.4

- 【Linux社区】Chris Wright（-stable 团队）发布 2.6.15.4，29 个文件改动，附 diffstat 与按作者修复摘要：桥接 netfilter 设备移除竞争与 RCU 竞争、dm-crypt 释放前清零密钥、SELinux size-128 slab 泄漏、grip/db9/iforce/sidewinder 等输入驱动崩溃修复、x86_64 SRAT/MADT 修复、keyctl strnlen_user 修复等；附 2.6.15.y git 树地址，并预告随后回帖贴出补丁全文。 `<!-- ROW_MINE: linux-kernel-announce.messages.720698 -->`

## 113.9 -mm 发布 2.6.15-mm2

- 【Linux社区】Andrew Morton 发布 2.6.15-mm2，共 1179 个补丁，称“应比 2.6.15-mm1 少些 bug”；引入 mutex 子系统（核心、文档、调试与大量信号量转换）；新增 openat 等 *at() 文件系统系统调用并引其手册说明；撤销 unshare 系统调用系列（“引发了 oops”）；time 补丁出新版，撤销 preadv/pwritev。 `<!-- ROW_MINE: linux-kernel-announce.messages.720734 -->`

## 113.10 -mm 发布 2.6.17-rc1-mm3

- 【Linux社区】Andrew Morton 发布 2.6.17-rc1-mm3，共 650 个补丁；临时丢弃 netdev 开发树（内含会致崩溃的大 e1000 更新）与 git-sas-jg 树（编译失败且来源存疑）；称“这里相当多东西是 2.6.17 所需”；audit 树改为 broken-out 补丁、升级内核内 zlib、新增 acpi dock 驱动与 I2C 虚拟适配器支持。 `<!-- ROW_MINE: linux-kernel-announce.messages.720742 -->`
