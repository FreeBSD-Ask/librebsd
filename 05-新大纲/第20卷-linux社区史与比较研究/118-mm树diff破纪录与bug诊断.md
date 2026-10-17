# 118 【Linux社区】mm树diff破纪录与bug诊断

> 来源：linux-kernel-announce 人工信 p11（10 封全读，2005-11 至 2019-04，-mm 发布六封（1915 补丁破纪录/32MB diff/PCI 广度优先排序副作用/Viro bird 树/每任务 I/O 计量 netlink 与 /proc/pid/io）、Bug 8885 Morton 与 Bottomley 两轮诊断、stable 2.6.14.3 diff、Kerrisk 单句回绝 NV）
> 判定：9 CAND / 1 NV。主题分布：2.6.23-rc8-mm2 发布宣告 1、2.6.15-rc1-mm1 发布宣告 1、2.6.18-rc6-mm2 发布宣告 1、Bug 8885 内存卡读取器失效回应 1、2.6.17-rc6-mm1 发布宣告 1、Linux 2.6.14.3 stable 修复内容 1、2.6.16-rc4-mm1 发布宣告 1、2.6.19-rc6-mm1 发布宣告 1、Bug 8885 内存卡读取器诊断回应 1。

> **体例说明（2026-09-14 整改）**：本页 9 块为“速览体例”——各块正文仅保留【Linux社区】条目行与 `<!-- ROW_MINE -->` 定位锚，五字段（要点/史料/史观/辨析/文献）不作逐块展开；块级要点与史观映射见下方“速览详表”，史料即各块 ROW_MINE 锚（`raw_source.raw_json` 可逐条反查），DSLXC claim 著录待 claim 库重跑时统一回填（DEFERRED）。

## 【Linux社区】速览详表（块级要点与史观映射）

| 块号 | 块题 | 要点（浓缩） | 史观映射 |
| --- | --- | --- | --- |
| 118.1 | 2.6.23-rc8-mm2 发布宣告 | 调度器 devel 树已恢复、driver 树损坏回退至 -mm1 版本、diff 近 32MB，共 5631 commits/2124 补丁文件 | 动手者叙事（总纲 10：规模与回退由 Morton 自述）；经验优先（总纲 9：以 diff 体量与提交数为量化判据）；拒绝进步叙事（总纲 1/3：diff 破纪录只作量化留痕，不写作集成能力“进步”） |
| 118.2 | 2.6.15-rc1-mm1 发布宣告 | 评语“reiser4 大幅更新”，附逐组补丁说明（relayfs、spufs、tiny 伸缩项），共 598 补丁 | 动手者叙事（总纲 10：评语与分组说明由发布者给出）；经验优先（总纲 9：以补丁数与分组为可核口径） |
| 118.3 | 2.6.18-rc6-mm2 发布宣告 | autofs4 挂载仍损坏、CONFIG_BLOCK=n 不完全可用、CONFIG_MSI=y 可能损坏、1915 补丁破纪录约多 200、警示 PCI 广度优先排序或改变设备节点 | 经验优先（总纲 9：以逐项缺陷与补丁计数为准）；动手者叙事（总纲 10：自曝三处不可用并预警副作用）；偶然性优先（总纲 5：设备节点变化系排序策略带来的非预期后果） |
| 118.4 | Bug 8885 内存卡读取器失效回应 | 尚难判定属 SCSI/USB/MMC 哪个子系统，请 Michal 跟踪为 2.6.22 后回归并请他人分析 dmesg 定位新失效子系统 | 经验优先（总纲 9：以 dmesg 与回归区间为判据，不作推测）；多方平等（总纲 8：把判定权开放给子系统维护者与他人，不独占结论） |
| 118.5 | 2.6.17-rc6-mm1 发布宣告 | 评语“更多 lockdep 更新”，附逐组补丁说明（lockdep v3、fbcon 可分离、多核/SMT 调度策略），共 1526 补丁 | 动手者叙事（总纲 10：更新内容由发布者分组自述）；循环结构呈现（总纲 4：lockdep 反复更新，呈持续迭代而非一次性完成） |
| 118.6 | Linux 2.6.14.3 stable 修复内容 | Chris Wright 回发 2.6.14.3 stable 版 git diff：Intel 0F33/0F34 CPUID 物理地址位数规避、RTC 中断锁修正、netfilter conntrack 多项修复、IPv6 发送选项修正 | 经验优先（总纲 9：以 diff 本体为唯一证据）；动手者叙事（总纲 10：修复本体即维护者行动留痕）；多方平等（总纲 8：stable 与 -mm 两线并列登记） |
| 118.7 | 2.6.16-rc4-mm1 发布宣告 | git-jfs 因 git 问题弃用、新增 Al Viro“bird”树、ia64 因 kbuild 用 Elf_Rela 无法编译、链接期 section mismatch 警告勿报，共 1012 补丁 | 动手者叙事（总纲 10：弃树与新纳由发布者自述）；经验优先（总纲 9：以编译失败实测为准）；拒绝进步叙事（总纲 1/3：编译失败与告警只作状态留痕） |
| 118.8 | 2.6.19-rc6-mm1 发布宣告 | 新增基于 netlink 与 /proc/pid/io 的每任务 I/O 计量，暂放 userweb.kernel.org，共 1524 补丁 | 动手者叙事（总纲 10：新机制由发布者自陈并说明托管位置）；经验优先（总纲 9：以接口路径与托管地址等具体信息为准） |
| 118.9 | Bug 8885 内存卡读取器诊断回应 | James Bottomley 回应 Morton：dmesg 信息不足，需在 blockdev --rereadpt 与 fdisk 失败时抓取 dmesg，若全无输出则疑为介质变更传播问题 | 经验优先（总纲 9：以可复现操作与 dmesg 输出为判据）；多方平等（总纲 8：诊断接力由两名维护者往复完成，无单一裁决者） |

---

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
