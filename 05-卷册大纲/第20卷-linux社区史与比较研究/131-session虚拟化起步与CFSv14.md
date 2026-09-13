# 131. 进程会话虚拟化起步、CFS v14 与 containers v10（ann p17）（ann p17）

> 来源：linux-kernel-announce 人工信 p17（10 封全读，2005-02 至 2007-08，-mm 发布六封（containers v10 与 CFS v14 与 lockstat 与 Xen 核心实现/进程会话虚拟化起步/sem2mutex 大转换与 robust futex/git-nfsd 首纳与 e1000e 求测/generic boolean 与 kill wall_jiffies）、stable 2.6.15.5 与 .6 diff、伪造 3.0.0 玩笑 NV×2）
> 判定：8 CAND / 2 NV。主题分布：2.6.14-rc4-mm1 1、Re: Linux 2.6.15.6 1、2.6.19-rc2-mm2 1、2.6.16-mm2 1、Linux 2.6.15.5 1、2.6.23-rc2-mm1 1、2.6.18-rc4-mm3 1、2.6.22-rc3-mm1 1。

## 131.1 2.6.14-rc4-mm1

- 【Linux社区】Andrew Morton 发布 -mm 补丁集：i2c/PCI/USB 大量更新、输入层改动态 input_dev 分配、x86_64 与 MD 更新、核心内存管理可扩展性重构，附逐补丁注语与 862 补丁清单 `<!-- ROW_MINE: linux-kernel-announce.messages.723361 -->`

## 131.2 Re: Linux 2.6.15.6

- 【Linux社区】Chris Wright 回帖附 2.6.15.5 至 2.6.15.6 完整 diff 本体：Makefile 版本号、ia64 unaligned 原型、NFS direct I/O mmap_sem 释放次序与 EFAULT 处理、request_sock 清理等 `<!-- ROW_MINE: linux-kernel-announce.messages.723375 -->`

## 131.3 2.6.19-rc2-mm2

- 【Linux社区】Andrew Morton 发布 -mm：新增 IOAT 树、搞通 wireless git 树、ktermios/tty 框架改造、进程会话虚拟化起步、bitrev 库，附 909 补丁清单 `<!-- ROW_MINE: linux-kernel-announce.messages.723381 -->`

## 131.4 2.6.16-mm2

- 【Linux社区】Andrew Morton 发布 -mm（自称“It seems to compile”）：sem2mutex 大规模转换、robust futex、PI futex/rt-mutex、RTC 子系统、swap prefetching，附 591 补丁清单 `<!-- ROW_MINE: linux-kernel-announce.messages.723415 -->`

## 131.5 Linux 2.6.15.5

- 【Linux社区】Chris Wright 以 -stable 团队名义发布 2.6.15.5：40 文件 diffstat 与逐人修复摘要，含 CVE-2006-0554 XFS ftruncate 暴露脏数据、CVE-2006-0741 恶意 ELF 入口地址、CVE-2006-0555 普通用户 direct I/O 可打挂 NFS 客户端 `<!-- ROW_MINE: linux-kernel-announce.messages.723460 -->`

## 131.6 2.6.23-rc2-mm1

- 【Linux社区】Andrew Morton 发布 -mm：新增 git-nfsd 树、新 e1000e 驱动求测、因“各种灾难”弃 SSB 补丁，附 1162 补丁清单 `<!-- ROW_MINE: linux-kernel-announce.messages.723466 -->`

## 131.7 2.6.18-rc4-mm3

- 【Linux社区】Andrew Morton 发布 -mm：开头警示 autofs 挂 nfs 子挂载仍坏，含 generic boolean 化、kill wall_jiffies、reiserfs 提速、NFSD 更新，附 1658 补丁清单 `<!-- ROW_MINE: linux-kernel-announce.messages.723477 -->`

## 131.8 2.6.22-rc3-mm1

- 【Linux社区】Andrew Morton 发布 -mm：合并 containers v10 基础设施（可能推倒重来）、CFS v14、lockstat、Xen 核心实现、coredump 过滤，附 993 补丁清单 `<!-- ROW_MINE: linux-kernel-announce.messages.723644 -->`
