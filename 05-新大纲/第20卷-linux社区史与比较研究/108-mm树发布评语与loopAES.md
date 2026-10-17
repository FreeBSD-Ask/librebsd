# 108 【Linux社区】mm树发布评语与loopAES

> 来源：linux-kernel-announce 人工信 p3（10 封全读，2005-01 至 2008-04，-mm 发布评语八封（git-xfs 恢复/git-selinux 弃置/pselect/ppoll 与 unshare() 新系统调用/section-mismatch alpha 358 错、“凌晨 5:41 懒得逐一描述”）、vgacon scrollback 修复、loop-AES v3.0b）
> 体例说明：本页 10 块采用**速览体例**——块下仅存单行摘记（主题陈述＋史料锚），要点、史观、辨析、文献四字段另立详表承载；五字段完整体例见 00-总览 §一.2。本页卷头未登记 claim 编号区间，文献著录与史观映射待详表单独立卷时补录。
> 判定：10 CAND / 0 NV。主题分布：-mm 发布 2.6.25-mm1 1、-mm 发布 2.6.15-rc5-mm1 1、-mm 发布 2.6.12-rc4-mm1 1、-mm 发布 2.6.13-rc3-mm3 1、vgacon printk scrolling fix（补丁提交） 1、-mm 发布 2.6.15-mm4 1、-mm 发布 2.6.16-rc4-mm2 1、-mm 发布 2.6.18-rc3-mm2 1、-mm 发布 2.6.24-rc5-mm1 1、loop-AES v3.0b 加密包公告 1。

## 108.1 -mm 发布 2.6.25-mm1

- 【Linux社区】Andrew Morton 发布 2.6.25-mm1；评语核心：git-xfs 因与 git-vfs 冲突已修复而恢复收录，git-selinux 因内存损坏回归新弃置，git-nfs 因内容并入 git-nfsd 弃置，git-drm 因构建失败仍回退，并预告次日发 -mm 合并计划邮件（约两百个补丁、15% 合并率）；统计 6045 commits/1878 个补丁文件。 `<!-- ROW_MINE: linux-kernel-announce.messages.720143 -->`

## 108.2 -mm 发布 2.6.15-rc5-mm1

- 【Linux社区】Andrew Morton 发布 2.6.15-rc5-mm1，共 950 个补丁；附逐组补丁评语，核心有：闭源助手模块 ndiswrapper/driverloader 将使内核打上 taint 标记、JSM 驱动因 tty 缓冲重构标为 broken、perfmon2 因需先行评审讨论而弃置，并对 timer_list 更名 ktimeout 留下“仍不明白为何必要”的评语。 `<!-- ROW_MINE: linux-kernel-announce.messages.720153 -->`

## 108.3 -mm 发布 2.6.12-rc4-mm1

- 【Linux社区】Andrew Morton 发布 2.6.12-rc4-mm1；评语核心：新增 Herbert Xu 的 ipsec 树（git-ipsec.patch）、Anton 的 NTFS 树迁往 git、sparsemem 内存模型推进、kprobes 函数返回探针与 fork connector 等功能说明；统计 -mm 补丁 1042、外部 changeset 388、总计 1421。 `<!-- ROW_MINE: linux-kernel-announce.messages.720176 -->`

## 108.4 -mm 发布 2.6.13-rc3-mm3

- 【Linux社区】Andrew Morton 发布 2.6.13-rc3-mm3，共 633 个补丁；评语核心：新增匿名缺页可扩展性补丁但自称“仍相当怀疑”，某“淘气维护者”急于赶进 2.6.13 的大型 x86_64 更新请多测，因疑似 TCP 挂死弃置 davem 的 git-net 树；并提示 bio_clone 修复或与部分 MD 数据损坏相关。 `<!-- ROW_MINE: linux-kernel-announce.messages.720184 -->`

## 108.5 vgacon printk scrolling fix（补丁提交）

- 【Linux社区】Jiri Slaby 向 Morton 提交基于 2.6.16-rc1-mm4 的单行补丁；实质说明：vgacon.c 中遗留的 printk（vgacon delta）会使 vga 控制台回滚 scrollback 失效，删除该行即修复，获 Daplas Acked，抄送 announce 列表。 `<!-- ROW_MINE: linux-kernel-announce.messages.720223 -->`

## 108.6 -mm 发布 2.6.15-mm4

- 【Linux社区】Andrew Morton 发布 2.6.15-mm4，共 730 个补丁；评语核心：大量 sem2mutex 转换、FUSE 异步请求大更新、nfsd（主要为 nfs4）更新、CPU 调度器更新，新增 pselect/ppoll 与 unshare() 系统调用，默认启用 i386 4K 栈；并留有“凌晨 5:41 懒得逐一描述”的评语。 `<!-- ROW_MINE: linux-kernel-announce.messages.720232 -->`

## 108.7 -mm 发布 2.6.16-rc4-mm2

- 【Linux社区】Andrew Morton 发布 2.6.16-rc4-mm2，共 1149 个补丁；评语核心：Sam 的新 section-mismatch 警告代码在其 alpha 构建检出 358 个错误且抽查属实，git-blktrace 树因与 relayfs 重构冲突弃置，-mm1 中若干有 bug 的补丁已移除；另收 relayfs 并入内核与 rtc 子系统重构。 `<!-- ROW_MINE: linux-kernel-announce.messages.720262 -->`

## 108.8 -mm 发布 2.6.18-rc3-mm2

- 【Linux社区】Andrew Morton 发布 2.6.18-rc3-mm2，共 1136 个补丁；评语核心：说明上一版 rc3-mm1 出现 udev 启动超时与 NFS 崩溃两个已知问题，本版回退引发问题的两个补丁（i386 lock section 与 NUMA-aware RPC 线程池）。 `<!-- ROW_MINE: linux-kernel-announce.messages.720323 -->`

## 108.9 -mm 发布 2.6.24-rc5-mm1

- 【Linux社区】Andrew Morton 发布 2.6.24-rc5-mm1，统计 5041 commits/1616 个补丁文件；评语核心：PCI BAR sizing 补丁若致探测失败可先行回退，git-sched 因破坏 suspend-to-RAM 弃置，git-block 恢复收录，git-newsetup/kgdb/perfmon 因与 git-x86 冲突弃置，并称自己被 bug 淹没、请抄送正确开发者与列表。 `<!-- ROW_MINE: linux-kernel-announce.messages.720410 -->`

## 108.10 loop-AES v3.0b 加密包公告

- 【Linux社区】Jari Ruusu 发布 loop-AES v3.0b 文件/交换分区加密包；changelog 两项：修复 64 位内核配 32 位用户态下外部编译模块 multi-key-v3 ioctl 不兼容，修复无 LO_FLAGS_DO_BMAP 的 2.6 内核上 v3 盘上格式误走 file backed 路径（无数据丢失但非日志文件系统安全）；附 tarball、md5 与签名链接。 `<!-- ROW_MINE: linux-kernel-announce.messages.720413 -->`
