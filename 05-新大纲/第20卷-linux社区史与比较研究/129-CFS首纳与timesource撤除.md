# 129 【Linux社区】CFS首纳与timesource撤除

> 来源：linux-kernel-announce 人工信 p13（10 封全读，2004-10 至 2007-08，-mm 发布九封（Ingo CFS CPU 调度器首次收入/timesource 通用时间管理整体撤除/hrtimers 与 dynticks 重新加入/自曝手握约 140 个 bug 待修/git-ubi 闪存类 LVM 树/“与 Vaio 的分歧”续撤 git-block）、灌水回怼 NV）
> 判定：9 CAND / 1 NV。主题分布：2.6.20-rc6-mm2 1、2.6.17-rc5-mm1 1、2.6.23-rc1-mm2 1、2.6.16-rc1-mm3 1、2.6.13-rc6-mm2 1、2.6.12-rc1-mm1 1、2.6.22-rc2-mm1 1、2.6.19-mm1 1、2.6.13-rc5-mm1 1。

> **体例说明（2026-09-14 整改）**：本页 9 块为“速览体例”——各块正文仅保留【Linux社区】条目行与 `<!-- ROW_MINE -->` 定位锚，五字段（要点/史料/史观/辨析/文献）不作逐块展开；块级要点与史观映射见下方“速览详表”，史料即各块 ROW_MINE 锚（`raw_source.raw_json` 可逐条反查），DSLXC claim 著录待 claim 库重跑时统一回填（DEFERRED）。

## 【Linux社区】速览详表（块级要点与史观映射）

| 块号 | 块题 | 要点（浓缩） | 史观映射 |
| --- | --- | --- | --- |
| 129.1 | 2.6.20-rc6-mm2 | 因 CFQ 破坏撤除 git-block 树并连带暂撤依赖它的 fsaio 异步 AIO 补丁，重新加入 hrtimers/dynticks 补丁（2.6.20-rc4-mm1 版的更新，“现在看来已修复”） | 循环结构呈现（总纲 4：git-block 与 hrtimers 撤而复入，呈反复拉锯）；动手者叙事（总纲 10：撤除与重入由发布者自述）；经验优先（总纲 9：以 CFQ 破坏实况与“现在看来已修复”的实测为准） |
| 129.2 | 2.6.17-rc5-mm1 | git-cfq 树因致 oops 被撤，合并 generic-IRQ 中断处理层与运行时锁验证器（警告开启后机器会跑得慢），并称并入新 reiser4 代码、新 readahead 代码与通用统计基础设施，同时提醒 ia64 等架构构建已损坏需查看 hot-fixes 目录 | 动手者叙事（总纲 10：撤树与性能代价说明由发布者给出）；经验优先（总纲 9：以 oops 与构建损坏实测为判据）；苦难不值得被提倡（总纲 14：如实记录锁验证器的性能代价，不将调试负担美化为贡献） |
| 129.3 | 2.6.23-rc1-mm2 | git-block 因“与 Vaio 的分歧”继续撤除，git-e1000new 被作者自行撤回，git-wireless 回归（超 3MB 的 diff 且“似乎可编译”），并质询“这里还有人在测 kgdb 代码吗” | 动手者叙事（总纲 10：撤除理由与质询均由发布者给出）；自反性声明（总纲 7：以“还有人在测吗”公开质疑自身集成代码的测试覆盖）；偶然性优先（总纲 5：树之撤除由与个人硬件（Vaio）的分歧偶然决定） |
| 129.4 | 2.6.16-rc1-mm3 | 因复杂的 timesource 选择 bug 整体撤除 timekeeping 通用时间管理补丁系列，另含各种修复与更新 | 经验优先（总纲 9：以 timesource 选择 bug 的实际复杂度为撤除判据）；循环结构呈现（总纲 4：timekeeping 系列在此整体撤除，后又重新加入，呈反复）；动手者叙事（总纲 10：撤除由发布者自述） |
| 129.5 | 2.6.13-rc6-mm2 | 自评“各种更新，没什么特别值得一提”，但警告该内核仍会从 SCSI 代码喷出大量 scheduling-while-atomic 警告、请测试者忽略 | 动手者叙事（总纲 10：平淡自评与告警说明均由当事人给出）；拒绝进步叙事（总纲 1/3：“没什么特别值得一提”即拒绝为常规更新加叙事光环）；经验优先（总纲 9：以警告噪音的实况为判据） |
| 129.6 | 2.6.12-rc1-mm1 | 称可能已修复近期 AGP/DRM 问题并请受影响者测试报告，另有 hfs/hfsplus 文件系统更新与大量 PCMCIA 变更，并透露 Linus 外出一周、自己手握约 140 个 bug（多为 2.6.10 后回归）待修 | 动手者叙事（总纲 10：待修 bug 数与处境由当事人自陈）；经验优先（总纲 9：以约 140 个 bug 与“多为回归”为量化判据）；苦难不值得被提倡（总纲 14：如实记录 140 bug 的积压，不写作个人奉献叙事） |
| 129.7 | 2.6.22-rc2-mm1 | 首次收入 Ingo 的 CFS CPU 调度器，加入新的简化版 readahead 补丁系列并请求认真评审与性能测试，同时称 Xen dom-U 支持已进入 x86 树 | 动手者叙事（总纲 10：首纳与求测由发布者给出）；经验优先（总纲 9：以“请求性能测试”的未验证状态为准，不预判 CFS 成败）；没有必然性只有偶然性（总纲 5：CFS 首纳与 Xen dom-U 同批入树，非规划所致） |
| 129.8 | 2.6.19-mm1 | 新增 kmap_atomic() 运行时调试（已抓到 `ata_scsi_rbuf_get()` 一处小缺陷（原文 buglet）、太吵可撤该补丁），承认 reiser4 构建被自己改的 VFS 变更弄坏，介绍新 git-ubi 树（闪存设备上的“类 LVM”层），并恢复 write() 死锁修复补丁 | 自反性声明（总纲 7：承认 reiser4 构建被自己改动弄坏）；动手者叙事（总纲 10：调试收益与噪音代价由发布者自述）；经验优先（总纲 9：以抓到的具体缺陷与“太吵可撤”的取舍为准） |
| 129.9 | 2.6.13-rc5-mm1 | 新增 James Bottomley 的 git-scsi-iscsi 树（iSCSI 驱动），警告该内核在 ia64 上已坏（spinlock 整合补丁待修），ACPI 开发树回归 -mm，并因妨碍内存管理测试且将重做而撤除 cachefs 与 cachefs-for-AFS 补丁 | 动手者叙事（总纲 10：新增、警告与撤除由发布者逐条自述）；经验优先（总纲 9：以 ia64 已坏与妨碍测试等实况为判据）；循环结构呈现（总纲 4：ACPI 树回归 -mm，呈分合往复） |

---

## 129.1 2.6.20-rc6-mm2

- 【Linux社区】akpm 发布 2.6.20-rc6-mm2，因 CFQ 破坏撤除 git-block 树并连带暂撤依赖它的 fsaio 异步 AIO 补丁，重新加入 hrtimers/dynticks 补丁（2.6.20-rc4-mm1 版的更新，“现在看来已修复”）。 `<!-- ROW_MINE: linux-kernel-announce.messages.722252 -->`

## 129.2 2.6.17-rc5-mm1

- 【Linux社区】akpm 发布 2.6.17-rc5-mm1，git-cfq 树因致 oops 被撤，合并 generic-IRQ 中断处理层与运行时锁验证器（警告开启后机器会跑得慢），并称并入新 reiser4 代码、新 readahead 代码与通用统计基础设施，同时提醒 ia64 等架构构建已损坏需查看 hot-fixes 目录。 `<!-- ROW_MINE: linux-kernel-announce.messages.722286 -->`

## 129.3 2.6.23-rc1-mm2

- 【Linux社区】akpm 发布 2.6.23-rc1-mm2，git-block 因“与 Vaio 的分歧”继续撤除，git-e1000new 被作者自行撤回，git-wireless 回归（超 3MB 的 diff 且“似乎可编译”），并质询“这里还有人在测 kgdb 代码吗”。 `<!-- ROW_MINE: linux-kernel-announce.messages.722287 -->`

## 129.4 2.6.16-rc1-mm3

- 【Linux社区】akpm 发布 2.6.16-rc1-mm3，因复杂的 timesource 选择 bug 整体撤除 timekeeping 通用时间管理补丁系列，另含各种修复与更新。 `<!-- ROW_MINE: linux-kernel-announce.messages.722290 -->`

## 129.5 2.6.13-rc6-mm2

- 【Linux社区】akpm 发布 2.6.13-rc6-mm2，自评“各种更新，没什么特别值得一提”，但警告该内核仍会从 SCSI 代码喷出大量 scheduling-while-atomic 警告、请测试者忽略。 `<!-- ROW_MINE: linux-kernel-announce.messages.722297 -->`

## 129.6 2.6.12-rc1-mm1

- 【Linux社区】akpm 发布 2.6.12-rc1-mm1，称可能已修复近期 AGP/DRM 问题并请受影响者测试报告，另有 hfs/hfsplus 文件系统更新与大量 PCMCIA 变更，并透露 Linus 外出一周、自己手握约 140 个 bug（多为 2.6.10 后回归）待修。 `<!-- ROW_MINE: linux-kernel-announce.messages.722370 -->`

## 129.7 2.6.22-rc2-mm1

- 【Linux社区】akpm 发布 2.6.22-rc2-mm1，首次收入 Ingo 的 CFS CPU 调度器，加入新的简化版 readahead 补丁系列并请求认真评审与性能测试，同时称 Xen dom-U 支持已进入 x86 树。 `<!-- ROW_MINE: linux-kernel-announce.messages.722461 -->`

## 129.8 2.6.19-mm1

- 【Linux社区】akpm 发布 2.6.19-mm1，新增 kmap_atomic() 运行时调试（已抓到 `ata_scsi_rbuf_get()` 一处小缺陷（原文 buglet）、太吵可撤该补丁），承认 reiser4 构建被自己改的 VFS 变更弄坏，介绍新 git-ubi 树（闪存设备上的“类 LVM”层，附 MTD 站点文档链接），并恢复 write() 死锁修复补丁。 `<!-- ROW_MINE: linux-kernel-announce.messages.722467 -->`

## 129.9 2.6.13-rc5-mm1

- 【Linux社区】akpm 发布 2.6.13-rc5-mm1，新增 James Bottomley 的 git-scsi-iscsi 树（iSCSI 驱动），警告该内核在 ia64 上已坏（spinlock 整合补丁待修），ACPI 开发树回归 -mm，并因妨碍内存管理测试且将重做而撤除 cachefs 与 cachefs-for-AFS 补丁。 `<!-- ROW_MINE: linux-kernel-announce.messages.722515 -->`
