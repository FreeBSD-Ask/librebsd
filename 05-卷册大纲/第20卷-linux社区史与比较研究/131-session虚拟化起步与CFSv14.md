# 131 【Linux社区】session虚拟化起步与CFSv14

> 来源：linux-kernel-announce 人工信 p17（10 封全读，2005-02 至 2007-08，-mm 发布六封（containers v10 与 CFS v14 与 lockstat 与 Xen 核心实现/进程会话虚拟化起步/sem2mutex 大转换与 robust futex/git-nfsd 首纳与 e1000e 求测/generic boolean 与 kill wall_jiffies）、stable 2.6.15.5 与 .6 diff、伪造 3.0.0 玩笑 NV×2）
> 判定：8 CAND / 2 NV。主题分布：2.6.14-rc4-mm1 1、Re: Linux 2.6.15.6 1、2.6.19-rc2-mm2 1、2.6.16-mm2 1、Linux 2.6.15.5 1、2.6.23-rc2-mm1 1、2.6.18-rc4-mm3 1、2.6.22-rc3-mm1 1。

> **体例说明（2026-09-14 整改）**：本页 8 块为“速览体例”——各块正文仅保留【Linux社区】条目行与 `<!-- ROW_MINE -->` 定位锚，五字段（要点/史料/史观/辨析/文献）不作逐块展开；块级要点与史观映射见下方“速览详表”，史料即各块 ROW_MINE 锚（`raw_source.raw_json` 可逐条反查），DSLXC claim 著录待 claim 库重跑时统一回填（DEFERRED）。

## 【Linux社区】速览详表（块级要点与史观映射）

| 块号 | 块题 | 要点（浓缩） | 史观映射 |
| --- | --- | --- | --- |
| 131.1 | 2.6.14-rc4-mm1 | i2c/PCI/USB 大量更新、输入层改动态 input_dev 分配、x86_64 与 MD 更新、核心内存管理可扩展性重构，附逐补丁注语与 862 补丁清单 | 动手者叙事（总纲 10：更新主次与逐补丁注语由发布者给出）；经验优先（总纲 9：以 862 补丁清单为量化口径）；多方平等（总纲 8：总线、输入、架构、内存四条并置，不设主次） |
| 131.2 | Re: Linux 2.6.15.6 | Chris Wright 回帖附 2.6.15.5 至 2.6.15.6 完整 diff 本体：Makefile 版本号、ia64 unaligned 原型、NFS direct I/O mmap_sem 释放次序与 EFAULT 处理、request_sock 清理等 | 经验优先（总纲 9：以 diff 本体为唯一证据，无文字评语）；动手者叙事（总纲 10：修复本体即维护者行动留痕）；多方平等（总纲 8：stable 线与 -mm 线并列登记） |
| 131.3 | 2.6.19-rc2-mm2 | 新增 IOAT 树、搞通 wireless git 树、ktermios/tty 框架改造、进程会话虚拟化起步、bitrev 库，附 909 补丁清单 | 动手者叙事（总纲 10：新纳与改造由发布者列举）；没有必然性只有偶然性（总纲 5：进程会话虚拟化起步与 IOAT 同批入树，非规划所致）；多方平等（总纲 8：网络、tty、虚拟化三线并置） |
| 131.4 | 2.6.16-mm2 | 自称“It seems to compile”：sem2mutex 大规模转换、robust futex、PI futex/rt-mutex、RTC 子系统、swap prefetching，附 591 补丁清单 | 自反性声明（总纲 7：以“似乎能编译”自陈验证程度之低，不作过度保证）；动手者叙事（总纲 10：自评由发布者给出）；循环结构呈现（总纲 4：sem2mutex 与 swap prefetching 在多个版本反复出现） |
| 131.5 | Linux 2.6.15.5 | 以 -stable 团队名义发布：40 文件 diffstat 与逐人修复摘要，含 CVE-2006-0554 XFS ftruncate 暴露脏数据、CVE-2006-0741 恶意 ELF 入口地址、CVE-2006-0555 普通用户 direct I/O 可打挂 NFS 客户端 | 经验优先（总纲 9：以 diffstat 与逐条 CVE 为判据）；动手者叙事（总纲 10：修复清单由团队给出）；法律与道德是利益分配（总纲 13：CVE 编号与披露节奏属安全信息的分配机制） |
| 131.6 | 2.6.23-rc2-mm1 | 新增 git-nfsd 树、新 e1000e 驱动求测、因“各种灾难”弃 SSB 补丁，附 1162 补丁清单 | 动手者叙事（总纲 10：弃置理由由发布者自述）；经验优先（总纲 9：以“各种灾难”所指的实测故障为判据）；知识注定过时（总纲 22：“各种灾难”系未细究的阶段性归因） |
| 131.7 | 2.6.18-rc4-mm3 | 开头警示 autofs 挂 nfs 子挂载仍坏，含 generic boolean 化、kill wall_jiffies、reiserfs 提速、NFSD 更新，附 1658 补丁清单 | 动手者叙事（总纲 10：警示与更新内容由发布者给出）；经验优先（总纲 9：以 autofs 仍坏的实况为准）；时间是一种形式主义（总纲 18：wall_jiffies 之移除属计时抽象的形式重构） |
| 131.8 | 2.6.22-rc3-mm1 | 合并 containers v10 基础设施（可能推倒重来）、CFS v14、lockstat、Xen 核心实现、coredump 过滤，附 993 补丁清单 | 动手者叙事（总纲 10：合并内容与“可能推倒重来”的自评由发布者给出）；自反性声明（总纲 7：明示 containers v10 可能被推翻，不预设为定局）；没有必然性只有偶然性（总纲 5：CFS v14 与 Xen 核心实现同批入树） |

---

## 131.1 2.6.14-rc4-mm1

- 【Linux社区】Andrew Morton 发布 -mm 补丁集：i2c/PCI/USB 大量更新、输入层改动态 input_dev 分配、x86_64 与 MD 更新、核心内存管理可扩展性重构，附逐补丁注语与 862 补丁清单。 `<!-- ROW_MINE: linux-kernel-announce.messages.723361 -->`

## 131.2 Re: Linux 2.6.15.6

- 【Linux社区】Chris Wright 回帖附 2.6.15.5 至 2.6.15.6 完整 diff 本体：Makefile 版本号、ia64 unaligned 原型、NFS direct I/O mmap_sem 释放次序与 EFAULT 处理、request_sock 清理等。 `<!-- ROW_MINE: linux-kernel-announce.messages.723375 -->`

## 131.3 2.6.19-rc2-mm2

- 【Linux社区】Andrew Morton 发布 -mm：新增 IOAT 树、搞通 wireless git 树、ktermios/tty 框架改造、进程会话虚拟化起步、bitrev 库，附 909 补丁清单。 `<!-- ROW_MINE: linux-kernel-announce.messages.723381 -->`

## 131.4 2.6.16-mm2

- 【Linux社区】Andrew Morton 发布 -mm（自称“It seems to compile”）：sem2mutex 大规模转换、robust futex、PI futex/rt-mutex、RTC 子系统、swap prefetching，附 591 补丁清单。 `<!-- ROW_MINE: linux-kernel-announce.messages.723415 -->`

## 131.5 Linux 2.6.15.5

- 【Linux社区】Chris Wright 以 -stable 团队名义发布 2.6.15.5：40 文件 diffstat 与逐人修复摘要，含 CVE-2006-0554 XFS ftruncate 暴露脏数据、CVE-2006-0741 恶意 ELF 入口地址、CVE-2006-0555 普通用户 direct I/O 可打挂 NFS 客户端。 `<!-- ROW_MINE: linux-kernel-announce.messages.723460 -->`

## 131.6 2.6.23-rc2-mm1

- 【Linux社区】Andrew Morton 发布 -mm：新增 git-nfsd 树、新 e1000e 驱动求测、因“各种灾难”弃 SSB 补丁，附 1162 补丁清单。 `<!-- ROW_MINE: linux-kernel-announce.messages.723466 -->`

## 131.7 2.6.18-rc4-mm3

- 【Linux社区】Andrew Morton 发布 -mm：开头警示 autofs 挂 nfs 子挂载仍坏，含 generic boolean 化、kill wall_jiffies、reiserfs 提速、NFSD 更新，附 1658 补丁清单。 `<!-- ROW_MINE: linux-kernel-announce.messages.723477 -->`

## 131.8 2.6.22-rc3-mm1

- 【Linux社区】Andrew Morton 发布 -mm：合并 containers v10 基础设施（可能推倒重来）、CFS v14、lockstat、Xen 核心实现、coredump 过滤，附 993 补丁清单。 `<!-- ROW_MINE: linux-kernel-announce.messages.723644 -->`
