# 130. mmotm 站点、nilfs2 引入与写回修复（ann p18）（ann p18）

> 来源：linux-kernel-announce 人工信 p18（10 封全读，2004-10 至 2008-09，-mm 发布八封（mmotm“每分钟-mm”站点开张/nilfs2 日志文件系统引入/“必须采取行动”抱怨维护者乱改代码/写回问题“结果很丑”附调试代码/avr32 树与锁自测壮观爆炸）、stable 2.6.15.5 约 30 项 diff、管控调侃 NV）
> 判定：9 CAND / 1 NV。主题分布：2.6.24-rc8-mm1 发布宣告 1、2.6.24-rc2-mm1 发布宣告 1、2.6.21-mm2 发布宣告 1、2.6.27-rc5-mm1 发布宣告 1、2.6.11-mm4 发布宣告 1、stable 2.6.15.5 修复 diff 1、2.6.22-rc1-mm1 发布宣告 1、2.6.24-rc3-mm1 发布宣告 1、2.6.20-rc1-mm1 发布宣告 1。

## 130.1 2.6.24-rc8-mm1 发布宣告

- 【Linux社区】akpm（Andrew Morton）发布 -mm 树 2.6.24-rc8-mm1，评语：selinux 在一台测试机上损坏、挂起（suspend-to-ram/disk）全坏需自行二分定位、六个 git 子树因冲突剔除，并抱怨“子系统维护者乱改他人代码导致冲突与构建错误失控，必须采取行动”；7933 commits/2056 补丁文件 `<!-- ROW_MINE: linux-kernel-announce.messages.723731 -->`

## 130.2 2.6.24-rc2-mm1 发布宣告

- 【Linux社区】akpm 发布 2.6.24-rc2-mm1，评语：新建“每分钟 -mm”（mmotm）站点每日多次上传补丁队列、已知关机/重启 oops 归因于 kset 转换补丁、新增 pci hotplug quilt 树与 x86 开发树；2794 commits/1229 补丁文件 `<!-- ROW_MINE: linux-kernel-announce.messages.723766 -->`

## 130.3 2.6.21-mm2 发布宣告

- 【Linux社区】akpm 发布 2.6.21-mm2，评语：git-acpi 与 git-kvm 因 git 冲突临时剔除、少量 IDE 补丁因编译失败剔除、自适应预读（adaptive readahead）补丁整体撤下等待更简的新版本；811 补丁 `<!-- ROW_MINE: linux-kernel-announce.messages.723771 -->`

## 130.4 2.6.27-rc5-mm1 发布宣告

- 【Linux社区】akpm 发布 2.6.27-rc5-mm1，评语：selinux 启用时 /proc/net 损坏、挂起回归、并抱怨“大量补丁长期积压于众多子系统且已多次发送仍未获回应”；引入 nilfs2 连续快照日志文件系统；690 commits/682 补丁文件 `<!-- ROW_MINE: linux-kernel-announce.messages.723785 -->`

## 130.5 2.6.11-mm4 发布宣告

- 【Linux社区】akpm 发布 2.6.11-mm4，评语：部分 ia64 机器损坏（近期页表遍历整合补丁的余波仍在处理）；501 补丁含 kexec/kdump、FUSE、CacheFS、reiser4、kgdb、sparsemem 预备工作等 `<!-- ROW_MINE: linux-kernel-announce.messages.723882 -->`

## 130.6 stable 2.6.15.5 修复 diff

- 【Linux社区】stable 维护者 Chris Wright 发布 2.6.15.5 修复内容，正文即 diff 本体：skge PHY 访问与中断掩码竞态、sbp2 卸载死锁、sd MODE SENSE 缓冲越界、binfmt_elf 非法入口段错误、netlink attachskb 队列溢出等约 30 项修复 `<!-- ROW_MINE: linux-kernel-announce.messages.723948 -->`

## 130.7 2.6.22-rc1-mm1 发布宣告

- 【Linux社区】akpm 发布 2.6.22-rc1-mm1，评语：深入研究 fs/fs-writeback.c 写回问题称“结果很丑”并附一批修复与可能高开销的调试代码（可经 inode_debug 关闭）、新增 H. Peter Anvin 的 i386 早期启动树 git-newsetup、找回遗失的 git-sas；706 补丁 `<!-- ROW_MINE: linux-kernel-announce.messages.723958 -->`

## 130.8 2.6.24-rc3-mm1 发布宣告

- 【Linux社区】akpm 发布 2.6.24-rc3-mm1，评语：新增 git-lblnet 网络标记树、重新加入 Smack 安全模块、剔除破坏 scsi 构建的 git-kbuild、自述将离线至周日；3200 commits/1255 补丁文件 `<!-- ROW_MINE: linux-kernel-announce.messages.724035 -->`

## 130.9 2.6.20-rc1-mm1 发布宣告

- 【Linux社区】akpm 发布 2.6.20-rc1-mm1，评语：新增 avr32 开发树（Haavard Skinnemoen）、powerpc 上禁用锁 API 自测因其“会以壮观方式爆炸”；含 dynticks/hrtimers 高精度时钟队列整体刷新与 tty 层 struct pid 重构；693 补丁 `<!-- ROW_MINE: linux-kernel-announce.messages.724045 -->`
