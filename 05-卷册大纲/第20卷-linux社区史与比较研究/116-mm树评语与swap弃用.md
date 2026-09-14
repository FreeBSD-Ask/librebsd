# 116 【Linux社区】mm树评语与swap弃用

> 来源：linux-kernel-announce 人工信 p8（10 封全读，2005-07 至 2008-12，-mm 发布八封（2.6.15-rc1-mm1 reiser4 大幅更新/KVM 并入需新 binutils/7 个疑似未修严重 bug 清单/swap prefetching 弃用说明/kgdb 统一树）、mmotm git 镜像公告、Bug 8966 回归判定）
> 判定：10 CAND / 0 NV。主题分布：mm 发布宣告 8、工具/项目公告 1、bug 报告回应 1。

> **体例说明（2026-09-14 整改）**：本页 3 块为“速览体例”——各块正文仅保留【Linux社区】条目行与 `<!-- ROW_MINE -->` 定位锚（116.1 收纳八封 -mm 宣告），五字段（要点/史料/史观/辨析/文献）不作逐块展开；块级要点与史观映射见下方“速览详表”，史料即各块 ROW_MINE 锚（`raw_source.raw_json` 可逐条反查），DSLXC claim 著录待 claim 库重跑时统一回填（DEFERRED）。

## 【Linux社区】速览详表（块级要点与史观映射）

| 块号 | 块题 | 要点（浓缩） | 史观映射 |
| --- | --- | --- | --- |
| 116.1 | mm 发布宣告 | 八封 -mm 宣告合块：2.6.15-rc1-mm1（reiser4 大幅更新、并入 spufs 与 relayfs 重构）、2.6.19-rc5-mm1（并入 KVM，需较新 binutils；hrtimer+dynticks 在停 TSC 低功耗机上仍不正常）、2.6.13-rc3-mm2（“可能超过 100 个补丁需要进 2.6.13”）、2.6.17-rc4-mm2（libata 大改求测；坦承 reiser4 无法编译、klibc 与 FC5 交互致 resume 找不到恢复分区）、2.6.21-mm1（新增 git-battery、弃用 staircase 调度器）、2.6.22-rc6-mm1（大写 NOTE 警告 menuconfig 改动破坏 make oldconfig 会丢 CONFIG_BLK_DEV 与整个 SCSI；新增 kgdb 统一树与 git-ixgbe）、2.6.17-mm3（新增 git-geode、lockdep 补丁以重制系列回归）、2.6.15-rc5-mm3（要求 gcc-3.2.x 以上，列 7 个疑似未修严重 bug 并说明弃用 swap prefetching 理由） | 动手者叙事（总纲 10：功能弃用与自曝编译失败均由 Morton 亲述）；经验优先（总纲 9：以停 TSC 机器实测、无法编译与 oops 清单为判据）；拒绝进步叙事（总纲 1/3：swap prefetching 之弃用只作决策留痕，不写作功能“演进”的反面注脚） |
| 116.2 | 工具/项目公告 | 介绍 mmotm（-mm tree of the moment）新增 git 镜像，感谢 jT 提供转换脚本并给出 git clone 与浏览地址，坦言补丁标题混乱、更新延迟未知 | 动手者叙事（总纲 10：工具由当事人自建并自陈缺陷）；经验优先（总纲 9：以“标题混乱、延迟未知”的实况为准而不加修饰）；自反性声明（总纲 7：发布者主动标注自身工具的不可靠处） |
| 116.3 | bug 报告回应 | 回应 Bug 8966（NFSv3 READDIRPLUS 后 LOOKUP 返回 NFS3ERR_NOENT），仅一句“A post-2.6.2 regression.”判定为回归并抄送 Trond Myklebust | 动手者叙事（总纲 10：分类判定由维护者以一句原文给出）；经验优先（总纲 9：以回归区间 2.6.2 之后为唯一判据，不附推测）；知识注定过时（总纲 22：极简回应保留判定时的认知边界，不追补后见之明） |

---

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
