# 120 【Linux社区】fault-injection纳入与stable185

> 来源：linux-kernel-announce 人工信 p9（10 封全读，2005-04 至 2008-07，-mm 发布七封（fault-injection 补丁集/unionfs 与 AIO/e1000e 设备 ID 迁移/G5 全挂待 bisect）、stable 2.6.18.5、kmap_atomic 作者 Dan Williams 回应承诺修法、空洞评语格式化公告 NV）
> 判定：9 CAND / 1 NV。主题分布：2.6.17-rc5-mm2 1、2.6.19-rc5-mm2 1、2.6.18-mm3 1、2.6.20-rc4-mm1 1、Linux 2.6.18.5 1、2.6.13-rc2-mm2 1、Re: kmap_atomic() oopses in current mainline 1、2.6.26-rc8-mm1 1、2.6.24-rc4-mm1 1。

> **体例说明（2026-09-14 整改）**：本页 9 块为“速览体例”——各块正文仅保留【Linux社区】条目行与 `<!-- ROW_MINE -->` 定位锚，五字段（要点/史料/史观/辨析/文献）不作逐块展开；块级要点与史观映射见下方“速览详表”，史料即各块 ROW_MINE 锚（`raw_source.raw_json` 可逐条反查），DSLXC claim 著录待 claim 库重跑时统一回填（DEFERRED）。

## 【Linux社区】速览详表（块级要点与史观映射）

| 块号 | 块题 | 要点（浓缩） | 史观映射 |
| --- | --- | --- | --- |
| 120.1 | 2.6.17-rc5-mm2 | cfq 已在主线修复故恢复 git-cfq 树，新增 lock-validator 与 genirq 修复，自曝漏更新 PCI 树，已在多平台 stress-test 通过 | 动手者叙事（总纲 10：恢复理由与自曝漏更新均由 Morton 亲述）；经验优先（总纲 9：以多平台 stress-test 实况为判据）；自反性声明（总纲 7：主动承认漏更新 PCI 树） |
| 120.2 | 2.6.19-rc5-mm2 | 纳入 fault-injection 补丁集并称“cool stuff”请众人试用，git-gfs2-nmw 致 Kconfig 警告，rc5-mm1 测试后丢弃数个坏补丁 | 动手者叙事（总纲 10：新补丁集由发布者推介并说明已知告警）；经验优先（总纲 9：以 rc5-mm1 实测后丢弃坏补丁为准）；没有必然性只有偶然性（总纲 5：Kconfig 告警由树合并偶然引入） |
| 120.3 | 2.6.18-mm3 | 新增 Jeff 的消警告树 git-gccbug 与 Romieu 的 git-qla3xxx，称无线崩溃与 x86_64 IRQ 分配崩溃“有望已修复”，MSI 处理现称“稳如磐石” | 动手者叙事（总纲 10：修复状态由发布者自评）；经验优先（总纲 9：以新增树与已修状态为准）；知识注定过时（总纲 22：“有望/稳如磐石”系阶段性自评，非终局结论） |
| 120.4 | 2.6.20-rc4-mm1 | 新增 e1000（Auke Kok）与 HID（Jiri Kosina）两个 git 树及 unionfs 文件系统，并合并文件系统 AIO 补丁组 | 动手者叙事（总纲 10：新纳树与文件系统由发布者列举）；多方平等（总纲 8：网络、输入、文件系统三线并置，不设主次） |
| 120.5 | Linux 2.6.18.5 | Chris Wright 代表 -stable 团队发布 2.6.18.5：附 diffstat 与逐条修复清单，核心为 netfilter compat 层权限/引用计数修复、fuse lookup Oops、蓝牙未对齐访问等，并回帖附完整补丁 | 动手者叙事（总纲 10：stable 发布与补丁本体由团队一手给出）；经验优先（总纲 9：以 diffstat 与逐条清单为判据）；多方平等（总纲 8：stable 线与 -mm 线并列登记） |
| 120.6 | 2.6.13-rc2-mm2 | 评语极简仅三条（MM 更新、video4linux 更新、Infiniband 特性工作），正文按组列补丁说明 | 动手者叙事（总纲 10：极简评语系当事人原话）；经验优先（总纲 9：以按组补丁说明为实据，不以评语篇幅论价值） |
| 120.7 | Re: kmap_atomic() oopses in current mainline | async_tx 作者 Dan Williams 回应 kmap_atomic 槽位冲突：认可 Morton 的无条件 kmap 建议，将去掉 ASYNC_TX_KMAP 标志并提交补丁，自承今后更小心 kmap 用法 | 动手者叙事（总纲 10：作者自认缺陷并承诺修法）；自反性声明（总纲 7：主动承认用法不当并接受他人建议）；经验优先（总纲 9：以槽位冲突机制为判据） |
| 120.8 | 2.6.26-rc8-mm1 | x86 测试机可用但持有 mlock 的应用退出时有 sleeping-while-atomic 警告（已知问题），powerpc Mac G5 上完全无法启动待 bisect | 经验优先（总纲 9：以 x86 可用与 G5 无法启动的分平台实测为准）；动手者叙事（总纲 10：已知问题与待 bisect 状态由发布者自陈）；多方平等（总纲 8：x86 与 powerpc 两平台结论并置，不取平均） |
| 120.9 | 2.6.24-rc4-mm1 | 大量设备 ID 从 e1000 移往 e1000e，提醒需开 CONFIG_E1000E 否则网卡失灵；s390 构建仍坏 | 动手者叙事（总纲 10：设备 ID 迁移与提醒由发布者给出）；经验优先（总纲 9：以具体配置项与构建失败实况为判据）；没有必然性只有偶然性（总纲 5：网卡失灵系迁移配置未同步的偶然后果） |

---

## 120.1 2.6.17-rc5-mm2

- 【Linux社区】Morton 发布 -mm 补丁集：cfq 已在主线修复故恢复 git-cfq 树，新增 lock-validator 与 genirq 修复，自曝漏更新 PCI 树，已在多平台 stress-test 通过。 `<!-- ROW_MINE: linux-kernel-announce.messages.721383 -->`

## 120.2 2.6.19-rc5-mm2

- 【Linux社区】Morton 发布 -mm 补丁集：纳入 fault-injection 补丁集并称“cool stuff”请众人试用，git-gfs2-nmw 致 Kconfig 警告，rc5-mm1 测试后丢弃数个坏补丁。 `<!-- ROW_MINE: linux-kernel-announce.messages.721399 -->`

## 120.3 2.6.18-mm3

- 【Linux社区】Morton 发布 -mm 补丁集：新增 Jeff 的消警告树 git-gccbug 与 Romieu 的 git-qla3xxx，称无线崩溃与 x86_64 IRQ 分配崩溃“有望已修复”（原文 hopefully），MSI 处理现称“稳如磐石”（原文 rock-solid）。 `<!-- ROW_MINE: linux-kernel-announce.messages.721425 -->`

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
