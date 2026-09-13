# 135. mm 树改基 linux-next 与 ubifs 首纳（ann p21）（ann p21）

> 来源：linux-kernel-announce 人工信 p21（10 封全读，2005-03 至 2008-05，-mm 发布八封（-mm 树改基于 linux-next 并新增 git-ubifs/regulator/logfs/orion 四树/Biederman procfs 大改入树/VMSPLIT 配置求测/git-kgdb-light 与 git-security-testing 首纳/git-chelsio 驱动树/“相当混乱”自评）、loop-AES v3.0c、stable 2.6.13.3）
> 判定：10 CAND / 0 NV。主题分布：2.6.25-rc8-mm1 1、2.6.16-rc5-mm1 1、2.6.15-mm3 1、2.6.23-rc4-mm1 1、2.6.26-rc2-mm1 1、Announce loop-AES-v3.0c 1、2.6.25-rc5-mm1 1、2.6.19-rc6-mm2 1、Linux 2.6.13.3 1、2.6.19-rc4-mm1 1。

## 135.1 2.6.25-rc8-mm1

- 【Linux社区】Andrew Morton 发布，评语核心：新增 wm97xx 触摸屏驱动树 git-wm97xx（Mark Brown）与 Al Viro 的 VFS git 树，git-drm 因构建错误剔除、git-xfs 因大量 git 冲突剔除，git-alsa 更名 git-alsa-tiwai、git-md-accel 更名 git-async_tx，规模 5011 commits/1542 patches `<!-- ROW_MINE: linux-kernel-announce.messages.724606 -->`

## 135.2 2.6.16-rc5-mm1

- 【Linux社区】Andrew Morton 发布，评语核心：Eric Biederman 的 procfs 大改入树、swap prefetching 补丁回归，kgdb 桩“有点烂”先清理再修（kgdboe 与 x86_64 支持已坏剔除），规模 1259 patches `<!-- ROW_MINE: linux-kernel-announce.messages.724625 -->`

## 135.3 2.6.15-mm3

- 【Linux社区】Andrew Morton 发布，评语核心：新增 VMSPLIT_* 配置项支持 x86 非标准用户/内核地址划分并求测试、ext3 多块分配提速（目前仅 direct-IO 使用）、mutex 子系统与 hrtimer 全套入树，并提醒 USB/PCI/driver/I2C 树大量更新“通常令人担忧”，规模 737 patches `<!-- ROW_MINE: linux-kernel-announce.messages.724635 -->`

## 135.4 2.6.23-rc4-mm1

- 【Linux社区】Andrew Morton 发布，评语核心：git-kbuild、git-ixgb（被 git-net 破坏）、git-md-accel 均剔除，git-v9fs 破坏所有非 x86 构建故禁用该文件系统，x86_64 dynticks 回归，规模 1628 patches `<!-- ROW_MINE: linux-kernel-announce.messages.724641 -->`

## 135.5 2.6.26-rc2-mm1

- 【Linux社区】Andrew Morton 发布，评语核心：-mm 树改基于 linux-next（并偶尔后拉个别树补新料），新增 git-ubifs、git-regulator、git-logfs、git-orion 四个 git 树，规模 1300 commits/534 patches `<!-- ROW_MINE: linux-kernel-announce.messages.724644 -->`

## 135.6 Announce loop-AES-v3.0c

- 【Linux社区】Jari Ruusu 发布文件/交换分区加密包，评语核心：losetup/mount 的 gpg 管道改用 --no-options（Lars Packschies 修复）、对未知密钥数据格式告警、适配 2.6.11-rc3-mm1 移除 QUEUE_FLAG_ORDERED 的变通、修 gcc 参数顺序导致的 Xen 误编译，另发布 ciphers-v3.0b，附 md5 与签名 `<!-- ROW_MINE: linux-kernel-announce.messages.724655 -->`

## 135.7 2.6.25-rc5-mm1

- 【Linux社区】Andrew Morton 发布，评语核心：新增 kgdb 树 git-kgdb-light（Jason Wessel、Ingo Molnar）与 git-security-testing 树（James Morris），自报 x86_64 t61p 上 suspend-to-disk 仍坏（疑 git-x86 所致），规模 3393 commits/1196 patches `<!-- ROW_MINE: linux-kernel-announce.messages.724674 -->`

## 135.8 2.6.19-rc6-mm2

- 【Linux社区】Andrew Morton 发布，评语核心：新增 Francois Romieu 的 Chelsio 驱动树 git-chelsio，因镜像暂坏临时存放于 userweb.kernel.org，规模 1641 patches `<!-- ROW_MINE: linux-kernel-announce.messages.724687 -->`

## 135.9 Linux 2.6.13.3

- 【Linux社区】stable 团队 Chris Wright 发布 2.6.13.3，附 15 文件 diffstat 与修复 shortlog：de_thread() BUG_ON（Alexander Nyberg）、tcp_clamp_window 过度钳制（Alexey Kuznetsov）、yenta oops（Ivan Kokshaysky）、ipvs persistence 连接损坏、UML x86_64 页泄漏、skge mac 地址 bonding oops 与 tcp 默认拥塞控制等，并预告随后跟贴完整补丁及 git 树地址 `<!-- ROW_MINE: linux-kernel-announce.messages.724730 -->`

## 135.10 2.6.19-rc4-mm1

- 【Linux社区】Andrew Morton 发布，评语核心：自评 2.6.19-rc3-mm1 相当混乱、本版主要为修复，ACPI 树因 Rafael 测试失败剔除、driver 树因各种问题剔除并连带暂移一批补丁，quilt 树未重拉而 git 树数小时前已重拉，规模 1026 patches `<!-- ROW_MINE: linux-kernel-announce.messages.724763 -->`
