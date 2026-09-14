# 130 【Linux社区】mmotm站点与nilfs2引入

> 来源：linux-kernel-announce 人工信 p18（10 封全读，2004-10 至 2008-09，-mm 发布八封（mmotm“每分钟-mm”站点开张/nilfs2 日志文件系统引入/“必须采取行动”抱怨维护者乱改代码/写回问题“结果很丑”附调试代码/avr32 树与锁自测壮观爆炸）、stable 2.6.15.5 约 30 项 diff、管控调侃 NV）
> 判定：9 CAND / 1 NV。主题分布：2.6.24-rc8-mm1 发布宣告 1、2.6.24-rc2-mm1 发布宣告 1、2.6.21-mm2 发布宣告 1、2.6.27-rc5-mm1 发布宣告 1、2.6.11-mm4 发布宣告 1、stable 2.6.15.5 修复 diff 1、2.6.22-rc1-mm1 发布宣告 1、2.6.24-rc3-mm1 发布宣告 1、2.6.20-rc1-mm1 发布宣告 1。

> **体例说明（2026-09-14 整改）**：本页 9 块为“速览体例”——各块正文仅保留【Linux社区】条目行与 `<!-- ROW_MINE -->` 定位锚，五字段（要点/史料/史观/辨析/文献）不作逐块展开；块级要点与史观映射见下方“速览详表”，史料即各块 ROW_MINE 锚（`raw_source.raw_json` 可逐条反查），DSLXC claim 著录待 claim 库重跑时统一回填（DEFERRED）。

## 【Linux社区】速览详表（块级要点与史观映射）

| 块号 | 块题 | 要点（浓缩） | 史观映射 |
| --- | --- | --- | --- |
| 130.1 | 2.6.24-rc8-mm1 | selinux 在一台测试机上损坏、挂起（suspend-to-ram/disk）全坏需自行二分定位、六个 git 子树因冲突剔除，并抱怨“子系统维护者乱改他人代码导致冲突与构建错误失控，必须采取行动”；7933 commits/2056 补丁文件 | 动手者叙事（总纲 10：损坏与抱怨均由 Morton 亲述）；经验优先（总纲 9：以 7933 commits 与六树剔除等实况为判据）；权力再分配（总纲 3：“必须采取行动”系集成者对子系统自主权的公开施压） |
| 130.2 | 2.6.24-rc2-mm1 | 新建“每分钟 -mm”（mmotm）站点每日多次上传补丁队列、已知关机/重启 oops 归因于 kset 转换补丁、新增 pci hotplug quilt 树与 x86 开发树；2794 commits/1229 补丁文件 | 动手者叙事（总纲 10：交付模式变更由发布者自述）；时间是一种形式主义（总纲 18：mmotm 以“每分钟”为单位重排发布节奏）；偶然性优先（总纲 5：关机 oops 由 kset 转换补丁偶然引入） |
| 130.3 | 2.6.21-mm2 | git-acpi 与 git-kvm 因 git 冲突临时剔除、少量 IDE 补丁因编译失败剔除、自适应预读（adaptive readahead）补丁整体撤下等待更简的新版本；811 补丁 | 经验优先（总纲 9：以编译失败与 git 冲突实测为剔除判据）；循环结构呈现（总纲 4：adaptive readahead 撤下待新版，与 129.7 的简化版 readahead 首纳相呼应）；动手者叙事（总纲 10：撤下理由由发布者逐条给出） |
| 130.4 | 2.6.27-rc5-mm1 | selinux 启用时 /proc/net 损坏、挂起回归、并抱怨“大量补丁长期积压于众多子系统且已多次发送仍未获回应”；引入 nilfs2 连续快照日志文件系统；690 commits/682 补丁文件 | 动手者叙事（总纲 10：积压处境由当事人自陈）；权力再分配（总纲 3：“多次发送仍未获回应”揭示集成者与子系统维护者之间的权力落差）；经验优先（总纲 9：以 /proc/net 损坏与挂起回归为判据） |
| 130.5 | 2.6.11-mm4 | 部分 ia64 机器损坏（近期页表遍历整合补丁的余波仍在处理）；501 补丁含 kexec/kdump、FUSE、CacheFS、reiser4、kgdb、sparsemem 预备工作等 | 经验优先（总纲 9：以 ia64 机器损坏的余波实况为判据）；动手者叙事（总纲 10：损坏归因由发布者自述）；没有必然性只有偶然性（总纲 5：余波由一次页表遍历整合偶然引入） |
| 130.6 | stable 2.6.15.5 修复 diff | 正文即 diff 本体：skge PHY 访问与中断掩码竞态、sbp2 卸载死锁、sd MODE SENSE 缓冲越界、binfmt_elf 非法入口段错误、netlink attachskb 队列溢出等约 30 项修复 | 经验优先（总纲 9：以 diff 本体为唯一证据）；动手者叙事（总纲 10：修复本体即维护者行动留痕）；多方平等（总纲 8：stable 线与 -mm 线并列登记） |
| 130.7 | 2.6.22-rc1-mm1 | 深入研究 fs/fs-writeback.c 写回问题称“结果很丑”并附一批修复与可能高开销的调试代码（可经 `inode_debug` 关闭）、新增 H. Peter Anvin 的 i386 早期启动树 git-newsetup、找回遗失的 git-sas；706 补丁 | 自反性声明（总纲 7：以“结果很丑”直陈自身代码状态）；动手者叙事（总纲 10：调试代码的性能代价由发布者标注）；经验优先（总纲 9：以写回问题的实测与关闭开关为准） |
| 130.8 | 2.6.24-rc3-mm1 | 新增 git-lblnet 网络标记树、重新加入 Smack 安全模块、剔除破坏 scsi 构建的 git-kbuild、自述将离线至周日；3200 commits/1255 补丁文件 | 循环结构呈现（总纲 4：Smack 安全模块撤而复入）；动手者叙事（总纲 10：增删与离线安排由发布者自述）；经验优先（总纲 9：以破坏 scsi 构建的实测为剔除判据） |
| 130.9 | 2.6.20-rc1-mm1 | 新增 avr32 开发树（Haavard Skinnemoen）、powerpc 上禁用锁 API 自测因其“会以壮观方式爆炸”；含 dynticks/hrtimers 高精度时钟队列整体刷新与 tty 层 struct pid 重构；693 补丁 | 动手者叙事（总纲 10：禁用理由与“壮观方式爆炸”系发布者原话）；经验优先（总纲 9：以 powerpc 上自测爆炸的实测为判据）；偶然性优先（总纲 5：avr32 开发树之纳入非规划所致） |

---

## 130.1 2.6.24-rc8-mm1 发布宣告

- 【Linux社区】akpm（Andrew Morton）发布 -mm 树 2.6.24-rc8-mm1，评语：selinux 在一台测试机上损坏、挂起（suspend-to-ram/disk）全坏需自行二分定位、六个 git 子树因冲突剔除，并抱怨“子系统维护者乱改他人代码导致冲突与构建错误失控，必须采取行动”；7933 commits/2056 补丁文件。 `<!-- ROW_MINE: linux-kernel-announce.messages.723731 -->`

## 130.2 2.6.24-rc2-mm1 发布宣告

- 【Linux社区】akpm 发布 2.6.24-rc2-mm1，评语：新建“每分钟 -mm”（mmotm）站点每日多次上传补丁队列、已知关机/重启 oops 归因于 kset 转换补丁、新增 pci hotplug quilt 树与 x86 开发树；2794 commits/1229 补丁文件。 `<!-- ROW_MINE: linux-kernel-announce.messages.723766 -->`

## 130.3 2.6.21-mm2 发布宣告

- 【Linux社区】akpm 发布 2.6.21-mm2，评语：git-acpi 与 git-kvm 因 git 冲突临时剔除、少量 IDE 补丁因编译失败剔除、自适应预读（adaptive readahead）补丁整体撤下等待更简的新版本；811 补丁。 `<!-- ROW_MINE: linux-kernel-announce.messages.723771 -->`

## 130.4 2.6.27-rc5-mm1 发布宣告

- 【Linux社区】akpm 发布 2.6.27-rc5-mm1，评语：selinux 启用时 /proc/net 损坏、挂起回归、并抱怨“大量补丁长期积压于众多子系统且已多次发送仍未获回应”；引入 nilfs2 连续快照日志文件系统；690 commits/682 补丁文件。 `<!-- ROW_MINE: linux-kernel-announce.messages.723785 -->`

## 130.5 2.6.11-mm4 发布宣告

- 【Linux社区】akpm 发布 2.6.11-mm4，评语：部分 ia64 机器损坏（近期页表遍历整合补丁的余波仍在处理）；501 补丁含 kexec/kdump、FUSE、CacheFS、reiser4、kgdb、sparsemem 预备工作等。 `<!-- ROW_MINE: linux-kernel-announce.messages.723882 -->`

## 130.6 stable 2.6.15.5 修复 diff

- 【Linux社区】stable 维护者 Chris Wright 发布 2.6.15.5 修复内容，正文即 diff 本体：skge PHY 访问与中断掩码竞态、sbp2 卸载死锁、sd MODE SENSE 缓冲越界、binfmt_elf 非法入口段错误、netlink attachskb 队列溢出等约 30 项修复。 `<!-- ROW_MINE: linux-kernel-announce.messages.723948 -->`

## 130.7 2.6.22-rc1-mm1 发布宣告

- 【Linux社区】akpm 发布 2.6.22-rc1-mm1，评语：深入研究 fs/fs-writeback.c 写回问题称“结果很丑”并附一批修复与可能高开销的调试代码（可经 `inode_debug` 关闭）、新增 H. Peter Anvin 的 i386 早期启动树 git-newsetup、找回遗失的 git-sas；706 补丁。 `<!-- ROW_MINE: linux-kernel-announce.messages.723958 -->`

## 130.8 2.6.24-rc3-mm1 发布宣告

- 【Linux社区】akpm 发布 2.6.24-rc3-mm1，评语：新增 git-lblnet 网络标记树、重新加入 Smack 安全模块、剔除破坏 scsi 构建的 git-kbuild、自述将离线至周日；3200 commits/1255 补丁文件。 `<!-- ROW_MINE: linux-kernel-announce.messages.724035 -->`

## 130.9 2.6.20-rc1-mm1 发布宣告

- 【Linux社区】akpm 发布 2.6.20-rc1-mm1，评语：新增 avr32 开发树（Haavard Skinnemoen）、powerpc 上禁用锁 API 自测因其“会以壮观方式爆炸”；含 dynticks/hrtimers 高精度时钟队列整体刷新与 tty 层 struct pid 重构；693 补丁。 `<!-- ROW_MINE: linux-kernel-announce.messages.724045 -->`
