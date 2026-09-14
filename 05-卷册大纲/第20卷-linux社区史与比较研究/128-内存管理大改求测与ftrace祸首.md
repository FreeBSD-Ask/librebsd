# 128 【Linux社区】内存管理大改求测与ftrace祸首

> 来源：linux-kernel-announce 人工信 p16（10 封全读，2005-03 至 2008-10，-mm 发布七封（快速 GUP 与无锁页缓存与页回收重写求测/git-x86 开机 oops 自曝/重拉 git 树致损坏/git-davej-x86 首纳/megaraid SAS 与 open-iscsi 首纳）、stable 2.6.15.3/.4 diff、vgacon 残留 printk 用户报告）
> 判定：10 CAND / 0 NV。主题分布：2.6.23-rc8-mm1 1、Re: Linux 2.6.15.3 1、Re: 2.6.16-rc1-mm4 1、2.6.26-rc5-mm1 1、Re: Linux 2.6.15.4 1、2.6.28-rc2-mm1 1、2.6.11-mm2 1、2.6.16-rc1-mm4 1、2.6.24-rc6-mm1 1、2.6.17-mm6 1。

> **体例说明（2026-09-14 整改）**：本页 10 块为“速览体例”——各块正文仅保留【Linux社区】条目行与 `<!-- ROW_MINE -->` 定位锚，五字段（要点/史料/史观/辨析/文献）不作逐块展开；块级要点与史观映射见下方“速览详表”，史料即各块 ROW_MINE 锚（`raw_source.raw_json` 可逐条反查），DSLXC claim 著录待 claim 库重跑时统一回填（DEFERRED）。

## 【Linux社区】速览详表（块级要点与史观映射）

| 块号 | 块题 | 要点（浓缩） | 史观映射 |
| --- | --- | --- | --- |
| 128.1 | 2.6.23-rc8-mm1 | 对 2.6.23-rc7-mm1 的多项修复，自述重拉子系统 git 树致大范围损坏、git-sched 补丁损坏被丢弃、cpuidle 代码未回归，附逐条注释补丁清单（5381 commits） | 自反性声明（总纲 7：主动自曝重拉子树致大范围损坏）；动手者叙事（总纲 10：损坏与丢弃由发布者逐条自述）；经验优先（总纲 9：以 5381 commits 与逐条注释为量化口径） |
| 128.2 | Re: Linux 2.6.15.3 | 发布 2.6.15.3 stable 修复说明的 diff 本体：Makefile 版本跳版，以及 net/ipv4/icmp.c 中 ip_options_echo 失败时改跳 out_unlock 的修复 | 经验优先（总纲 9：以 diff 本体为唯一证据，无文字评语）；动手者叙事（总纲 10：修复本体即维护者行动留痕）；多方平等（总纲 8：stable 线与 -mm 线并列登记） |
| 128.3 | Re: 2.6.16-rc1-mm4 | Jindrich Makovicka 对 -mm 宣告的实质技术回应：报告 vgacon.c 残留调试 printk“vgacon delta”致 VGA 控制台回滚缓冲失效，删除该行即修复 | 经验优先（总纲 9：以“删除该行即修复”的可复现结论为判据）；多方平等（总纲 8：普通用户的技术回应与维护者公告并列登记，不以身份分等） |
| 128.4 | 2.6.26-rc5-mm1 | git-block 继续被弃，新收入 Miklos Szeredi 非特权挂载树，重点评语为内存管理大改（快速 get_user_pages、无锁页缓存、页回收基本重写）亟需测试与评审，附完整补丁注释（1364 commits） | 动手者叙事（总纲 10：求测重点由发布者指明）；经验优先（总纲 9：以“亟需测试与评审”的未验证状态为准，不预判成败）；没有必然性只有偶然性（总纲 5：页回收重写等大改由当期集成需要偶然带出） |
| 128.5 | Re: Linux 2.6.15.4 | 发布 2.6.15.4 stable 修复说明的 diff 本体：ACPI 只登记已启用 CPU、sparc64 clock_settime 兼容修正、x86_64 NUMA 过小节点剔除、手柄与 iforce 等输入驱动修复 | 经验优先（总纲 9：以 diff 本体为唯一证据）；多方平等（总纲 8：架构、NUMA 与输入驱动修复并置，不设主次）；动手者叙事（总纲 10：修复本体即行动留痕） |
| 128.6 | 2.6.28-rc2-mm1 | 自评 ia64、alpha、s390、arm 编译不佳（ftrace 为祸首）但六台测试机运行正常，附整版带说明补丁清单（nilfs2 入列、reiser4 大宗维护、quota 重构等） | 自反性声明（总纲 7：主动指认 ftrace 为四架构编译不佳的祸首）；经验优先（总纲 9：以四架构编译失败与六台测试机运行的分裂实测为准）；多方平等（总纲 8：编译侧与运行侧两种结论并置，不取平均） |
| 128.7 | 2.6.11-mm2 | UML、fbdev、nfs4 服务器更新，新增 megaraid SAS 与 open-iscsi 驱动及 fatfs 大改，因篇幅原因全补丁列表仅给 FTP 链接（共 1663 补丁） | 动手者叙事（总纲 10：更新内容与篇幅取舍由发布者说明）；经验优先（总纲 9：以 1663 补丁数与 FTP 链接等可核信息为准）；知识注定过时（总纲 22：FTP 链接形态本身即被后续工具链淘汰） |
| 128.8 | 2.6.16-rc1-mm4 | 新增 git-davej-x86 树，大量 USB 更新并请受影响者抄送 linux-usb-devel，自评近期活动平缓，并提醒想进 2.6.16 的补丁可催他 | 动手者叙事（总纲 10：“活动平缓”与“可催他”均由发布者自陈）；经验优先（总纲 9：以抄送列表与合并窗口时点等具体流程为准）；权力再分配（总纲 3：合并窗口的准入节奏实际由维护者个人掌握） |
| 128.9 | 2.6.24-rc6-mm1 | 自曝 i386 因 git-x86 提交 e3c1b141 开机 oops 且不可回退，git-block、git-perfmon、git-kgdb、git-newsetup 等四树因与 git-x86 冲突被弃，t61p 睡眠再坏，附逐条注释补丁清单（6223 commits） | 自反性声明（总纲 7：主动自曝具体提交号导致的不可回退 oops）；经验优先（总纲 9：以 e3c1b141 与四树冲突等可核事实为判据）；拒绝进步叙事（总纲 1/3：开机 oops 与树被弃不写作演进叙事） |
| 128.10 | 2.6.17-mm6 | 主打 e1000 驱动大更新与 1394 子系统更新，附逐条注释补丁清单（704 patches），含 inode-diet、lockdep、genirq 等大宗改动说明 | 动手者叙事（总纲 10：更新主次与改动说明由发布者给出）；经验优先（总纲 9：以 704 patches 与逐条注释为量化口径）；循环结构呈现（总纲 4：lockdep 与 genirq 在多个版本反复出现，呈持续迭代） |

---

## 128.1 2.6.23-rc8-mm1

- 【Linux社区】Andrew Morton 发布 -mm 快照宣告：对 2.6.23-rc7-mm1 的多项修复，自述重拉子系统 git 树致大范围损坏、git-sched 补丁损坏被丢弃、cpuidle 代码未回归，附逐条注释补丁清单（5381 commits）。 `<!-- ROW_MINE: linux-kernel-announce.messages.723112 -->`

## 128.2 Re: Linux 2.6.15.3

- 【Linux社区】Chris Wright 发布 2.6.15.3 stable 修复说明的 diff 本体：Makefile 版本跳版，以及 net/ipv4/icmp.c 中 ip_options_echo 失败时改跳 out_unlock 的修复。 `<!-- ROW_MINE: linux-kernel-announce.messages.723137 -->`

## 128.3 Re: 2.6.16-rc1-mm4

- 【Linux社区】Jindrich Makovicka 对 -mm 宣告的实质技术回应：报告 vgacon.c 残留调试 printk“vgacon delta”致 VGA 控制台回滚缓冲失效，删除该行即修复。 `<!-- ROW_MINE: linux-kernel-announce.messages.723142 -->`

## 128.4 2.6.26-rc5-mm1

- 【Linux社区】Andrew Morton 发布 -mm 快照宣告：git-block 继续被弃，新收入 Miklos Szeredi 非特权挂载树，重点评语为内存管理大改（快速 get_user_pages、无锁页缓存、页回收基本重写）亟需测试与评审，附完整补丁注释（1364 commits）。 `<!-- ROW_MINE: linux-kernel-announce.messages.723154 -->`

## 128.5 Re: Linux 2.6.15.4

- 【Linux社区】Chris Wright 发布 2.6.15.4 stable 修复说明的 diff 本体：ACPI 只登记已启用 CPU、sparc64 clock_settime 兼容修正、x86_64 NUMA 过小节点剔除、手柄与 iforce 等输入驱动修复。 `<!-- ROW_MINE: linux-kernel-announce.messages.723166 -->`

## 128.6 2.6.28-rc2-mm1

- 【Linux社区】Andrew Morton 发布 -mm 快照宣告：自评 ia64、alpha、s390、arm 编译不佳（ftrace 为祸首）但六台测试机运行正常，附整版带说明补丁清单（nilfs2 入列、reiser4 大宗维护、quota 重构等）。 `<!-- ROW_MINE: linux-kernel-announce.messages.723184 -->`

## 128.7 2.6.11-mm2

- 【Linux社区】Andrew Morton 发布 -mm 快照宣告：UML、fbdev、nfs4 服务器更新，新增 megaraid SAS 与 open-iscsi 驱动及 fatfs 大改，因篇幅原因全补丁列表仅给 FTP 链接（共 1663 补丁）。 `<!-- ROW_MINE: linux-kernel-announce.messages.723204 -->`

## 128.8 2.6.16-rc1-mm4

- 【Linux社区】Andrew Morton 发布 -mm 快照宣告：新增 git-davej-x86 树，大量 USB 更新并请受影响者抄送 linux-usb-devel，自评近期活动平缓，并提醒想进 2.6.16 的补丁可催他。 `<!-- ROW_MINE: linux-kernel-announce.messages.723277 -->`

## 128.9 2.6.24-rc6-mm1

- 【Linux社区】Andrew Morton 发布 -mm 快照宣告：自曝 i386 因 git-x86 提交 e3c1b141 开机 oops 且不可回退，git-block、git-perfmon、git-kgdb、git-newsetup 等四树因与 git-x86 冲突被弃，t61p 睡眠再坏，附逐条注释补丁清单（6223 commits）。 `<!-- ROW_MINE: linux-kernel-announce.messages.723284 -->`

## 128.10 2.6.17-mm6

- 【Linux社区】Andrew Morton 发布 -mm 快照宣告：主打 e1000 驱动大更新与 1394 子系统更新，附逐条注释补丁清单（704 patches），含 inode-diet、lockdep、genirq 等大宗改动说明。 `<!-- ROW_MINE: linux-kernel-announce.messages.723335 -->`
