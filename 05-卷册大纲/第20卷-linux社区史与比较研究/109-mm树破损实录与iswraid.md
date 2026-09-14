# 109 【Linux社区】mm树破损实录与iswraid

> 来源：linux-kernel-announce 人工信 p4（10 封全读，2004-07 至 2019-04，-mm 发布评语五封（2.6.18-rc7-mm1 十小时勉强可登录、CONFIG_BROKEN 大面积、bk 转 git、USB 电源管理恢复编译）、iswraid 0.1.4、kmap_atomic 修法、glibc 手册 bug 归因）
> 体例说明：本页 9 块采用**速览体例**——块下仅存单行摘记（主题陈述＋史料锚），要点、史观、辨析、文献四字段另立详表承载；五字段完整体例见 00-总览 §一.2。本页卷头未登记 claim 编号区间，文献著录与史观映射待详表单独立卷时补录。
> 判定：9 CAND / 1 NV。主题分布：2.6.18-mm1 1、Re: bug#35275: spelling mistake manual pages 1、2.6.14-rc5-mm1 1、2.6.22-rc4-mm1 1、[Announce] “iswraid” (ICH5R/ICH6R ataraid sub-driver) for 2.4.26 1、Re: kmap_atomic() oopses in current mainline 1、2.6.27-rc1-mm1 1、2.6.12-rc3-mm1 1、2.6.18-rc7-mm1 1。

## 109.1 2.6.18-mm1

- 【Linux社区】Andrew Morton 发布 -mm 树；评语称 -rc7-mm1 因驱动树改动问题多、相关补丁全数撤下；逐补丁注明合并、丢弃或修复，共 2040 个补丁 `<!-- ROW_MINE: linux-kernel-announce.messages.720439 -->`

## 109.2 Re: bug#35275: spelling mistake manual pages

- 【Linux社区】Paul Eggert 实质回应拼写错误 bug 报告；判定该报告实属 glibc 手册并给出 glibc bug 报告流程链接，且要求以纯文本而非截图描述 bug `<!-- ROW_MINE: linux-kernel-announce.messages.720448 -->`

## 109.3 2.6.14-rc5-mm1

- 【Linux社区】Morton 发布 -mm 树；新增 git-blktrace、git-block、git-mips 树，USB 开发树恢复编译启动以改进电源管理，Hugh 的分页表锁 SMP 扩展性与 hugetlb 按需调页待测，共 1059 补丁 `<!-- ROW_MINE: linux-kernel-announce.messages.720460 -->`

## 109.4 2.6.22-rc4-mm1

- 【Linux社区】Morton 发布 -mm 树；Nick 系列补丁修 pagefault 与缓冲写死锁、大量文件系统含 reiser4 被标 CONFIG_BROKEN 禁用，命令行长度限制补丁破坏 nommu 构建，共 119 补丁 `<!-- ROW_MINE: linux-kernel-announce.messages.720474 -->`

## 109.5 [Announce] “iswraid” (ICH5R/ICH6R ataraid sub-driver) for 2.4.26

- 【Linux社区】Intel 的 Martins Krikis 发布 iswraid 0.1.4；实质介绍其 as ataraid 子驱动、依赖 libata 与 ata_piix，并列出 HIGHMEM 修复、RAID1 降级 I/O 成功、slab 缓存、新增文档等变更 `<!-- ROW_MINE: linux-kernel-announce.messages.720542 -->`

## 109.6 Re: kmap_atomic() oopses in current mainline

- 【Linux社区】Evgeniy Polyakov 对 kmap_atomic 崩溃问题实质回应；解释 async_tx 同一时刻仅允许单操作故 src 与 dst 不会同槽，给出 KM_USER0 改 KM_USER1 的 diff 并讨论无条件 kmap_atomic 的开销权衡 `<!-- ROW_MINE: linux-kernel-announce.messages.720577 -->`

## 109.7 2.6.27-rc1-mm1

- 【Linux社区】Morton 发布 -mm 树；评语称 linux-next 弄坏其 X server、建议 x86 补丁多测一两周并提醒假期减负；799 commits 计 416 补丁文件并逐组评注去向 `<!-- ROW_MINE: linux-kernel-announce.messages.720584 -->`

## 109.8 2.6.12-rc3-mm1

- 【Linux社区】Morton 发布 -mm 树；警告新定时器代码有 bug 并附 revert 指引、mpt-fusion 改配置名易致无盘、ia64 断电崩溃，指 bk 树无人维护已枯萎、改拾 git 树，共 963 补丁 `<!-- ROW_MINE: linux-kernel-announce.messages.720590 -->`

## 109.9 2.6.18-rc7-mm1

- 【Linux社区】Morton 发布 -mm 树；详列已知破损：git-input 与 git-alsa 撤下、ia64 不编译、旧 udev 不可用、CONFIG_BLOCK=n 与 headers_check 坏、因 MSI bug 禁 4k stacks，称花十小时才勉强可登录，共 1979 补丁 `<!-- ROW_MINE: linux-kernel-announce.messages.720601 -->`
