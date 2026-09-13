# 116. mm 树发布评语续与 swap prefetch 弃用（ann p8）（ann p8）

> 来源：linux-kernel-announce 人工信 p8（10 封全读，2005-07 至 2008-12，-mm 发布八封（2.6.15-rc1-mm1 reiser4 大幅更新/KVM 并入需新 binutils/7 个疑似未修严重 bug 清单/swap prefetching 弃用说明/kgdb 统一树）、mmotm git 镜像公告、Bug 8966 回归判定）
> 判定：10 CAND / 0 NV。主题分布：mm 发布宣告 8、工具/项目公告 1、bug 报告回应 1。

## 116.1 mm 发布宣告

- 【Linux社区】Andrew Morton 发布 2.6.15-rc1-mm1，评语称 reiser4 大幅更新，并入 spufs（POWER Cell 处理器文件系统）、tiny 内核体积缩减、relayfs 重构等，逐补丁附一句评注。 `<!-- ROW_MINE: linux-kernel-announce.messages.721272 -->`
- 【Linux社区】Andrew Morton 发布 2.6.19-rc5-mm1，评语称合并 KVM 内核级虚拟机补丁（需较新 binutils），并指出 hrtimer+dynticks 在低功耗停 TSC 机器上仍工作不正常。 `<!-- ROW_MINE: linux-kernel-announce.messages.721323 -->`
- 【Linux社区】Andrew Morton 发布 2.6.13-rc3-mm2，评语称“可能超过 100 个补丁需要进 2.6.13”，含 autofs 卸载后顽固忙 inode 修复、zlib 安全漏洞封堵等逐补丁评注。 `<!-- ROW_MINE: linux-kernel-announce.messages.721325 -->`
- 【Linux社区】Andrew Morton 发布 2.6.17-rc4-mm2，评语称 libata 大改并请求 SATA 出过问题者测试，坦承 reiser4 无法编译、klibc 补丁与 RH FC5 用户态交互致 resume-from-disk 找不到恢复分区。 `<!-- ROW_MINE: linux-kernel-announce.messages.721328 -->`
- 【Linux社区】Andrew Morton 发布 2.6.21-mm1，评语称新增 git-battery 树（Anton Vorontsov，暂会报神秘 depmod 错误）、staircase CPU 调度器被弃用。 `<!-- ROW_MINE: linux-kernel-announce.messages.721329 -->`
- 【Linux社区】Andrew Morton 发布 2.6.22-rc6-mm1，以大写 NOTE 警告 menuconfig 改动严重破坏 make oldconfig（会丢 CONFIG_BLK_DEV 与整个 SCSI），新增 kgdb 统一树（目标 2.6.24）、git-ixgbe 万兆网卡树、x86_64 dynticks 与动态命令行长度补丁。 `<!-- ROW_MINE: linux-kernel-announce.messages.721331 -->`
- 【Linux社区】Andrew Morton 发布 2.6.17-mm3，评语称新增 x86 Geode 开发树 git-geode（Jordan Crouse），锁定校验器（lockdep）补丁以重制系列形式回归。 `<!-- ROW_MINE: linux-kernel-announce.messages.721348 -->`
- 【Linux社区】Andrew Morton 发布 2.6.15-rc5-mm3，要求 gcc-3.2.x 以上，列出 rc5-mm1/mm2 疑似未修的 7 个严重 bug（usb_set_configuration oops、kexec 失败、ehci_hcd 崩溃、pci_call_probe panic 等），并说明弃用 swap prefetching 的理由。 `<!-- ROW_MINE: linux-kernel-announce.messages.721364 -->`

## 116.2 工具/项目公告

- 【Linux社区】Andrew Morton 介绍 mmotm（-mm tree of the moment）新增 git 镜像，感谢 jT 提供转换脚本，给出 git clone 与浏览地址，并坦言补丁标题混乱、更新延迟未知。 `<!-- ROW_MINE: linux-kernel-announce.messages.721285 -->`

## 116.3 bug 报告回应

- 【Linux社区】Andrew Morton 回应 Bug 8966（NFSv3 READDIRPLUS 后 LOOKUP 返回 NFS3ERR_NOENT），仅一句“A post-2.6.2 regression.”判定为回归并抄送 Trond Myklebust，属实质但极简的分类回应。 `<!-- ROW_MINE: linux-kernel-announce.messages.721372 -->`
