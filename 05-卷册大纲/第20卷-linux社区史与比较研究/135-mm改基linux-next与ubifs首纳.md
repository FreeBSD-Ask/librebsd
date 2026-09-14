# 135 【Linux社区】mm改基linux-next与ubifs首纳

> 来源：linux-kernel-announce 人工信 p21（10 封全读，2005-03 至 2008-05，-mm 发布八封（-mm 树改基于 linux-next 并新增 git-ubifs/regulator/logfs/orion 四树/Biederman procfs 大改入树/VMSPLIT 配置求测/git-kgdb-light 与 git-security-testing 首纳/git-chelsio 驱动树/“相当混乱”自评）、loop-AES v3.0c、stable 2.6.13.3）
> 判定：10 CAND / 0 NV。主题分布：2.6.25-rc8-mm1 1、2.6.16-rc5-mm1 1、2.6.15-mm3 1、2.6.23-rc4-mm1 1、2.6.26-rc2-mm1 1、Announce loop-AES-v3.0c 1、2.6.25-rc5-mm1 1、2.6.19-rc6-mm2 1、Linux 2.6.13.3 1、2.6.19-rc4-mm1 1。

> **体例说明（2026-09-14 整改）**：本页 10 块为“速览体例”——各块正文仅保留【Linux社区】条目行与 `<!-- ROW_MINE -->` 定位锚，五字段（要点/史料/史观/辨析/文献）不作逐块展开；块级要点与史观映射见下方“速览详表”，史料即各块 ROW_MINE 锚（`raw_source.raw_json` 可逐条反查），DSLXC claim 著录待 claim 库重跑时统一回填（DEFERRED）。

## 【Linux社区】速览详表（块级要点与史观映射）

| 块号 | 块题 | 要点（浓缩） | 史观映射 |
| --- | --- | --- | --- |
| 135.1 | 2.6.25-rc8-mm1 | 新增 wm97xx 触摸屏驱动树 git-wm97xx（Mark Brown）与 Al Viro 的 VFS git 树，git-drm 因构建错误剔除、git-xfs 因大量 git 冲突剔除，git-alsa 更名 git-alsa-tiwai、git-md-accel 更名 git-async_tx，规模 5011 commits/1542 patches | 动手者叙事（总纲 10：新增与剔除由发布者列举）；分离聚合是永恒规律（总纲 4：git 树的增删改名，属子系统树的聚散重组）；多方平等（总纲 8：触摸屏、VFS、DRM、XFS、ALSA 多线并置） |
| 135.2 | 2.6.16-rc5-mm1 | Eric Biederman 的 procfs 大改入树、swap prefetching 补丁回归，kgdb 桩“有点烂”先清理再修（kgdboe 与 x86_64 支持已坏剔除），规模 1259 patches | 自反性声明（总纲 7：以“有点烂”直陈 kgdb 桩现状，不掩饰）；动手者叙事（总纲 10：入树与剔除由发布者给出）；循环结构呈现（总纲 4：swap prefetching 补丁在多个版本反复回归） |
| 135.3 | 2.6.15-mm3 | 新增 VMSPLIT_* 配置项支持 x86 非标准用户/内核地址划分并求测试、ext3 多块分配提速（目前仅 direct-IO 使用）、mutex 子系统与 hrtimer 全套入树，并提醒 USB/PCI/driver/I2C 树大量更新“通常令人担忧”，规模 737 patches | 动手者叙事（总纲 10：新增与提醒由发布者给出）；经验优先（总纲 9：以“通常令人担忧”的历史实测为判据）；时间是一种形式主义（总纲 18：VMSPLIT 属地址空间的形式划分） |
| 135.4 | 2.6.23-rc4-mm1 | git-kbuild、git-ixgb（被 git-net 破坏）、git-md-accel 均剔除，git-v9fs 破坏所有非 x86 构建故禁用该文件系统，x86_64 dynticks 回归，规模 1628 patches | 动手者叙事（总纲 10：剔除与禁用由发布者自述）；经验优先（总纲 9：以非 x86 构建被破坏的实测为准）；没有必然性只有偶然性（总纲 5：git 树互相破坏致剔除，属工具链偶发耦合） |
| 135.5 | 2.6.26-rc2-mm1 | -mm 树改基于 linux-next（并偶尔后拉个别树补新料），新增 git-ubifs、git-regulator、git-logfs、git-orion 四个 git 树，规模 1300 commits/534 patches | 动手者叙事（总纲 10：改基与新增由发布者给出）；分离聚合是永恒规律（总纲 4：-mm 树改基 linux-next 并新增四树，属集成中枢的聚合重组）；没有必然性只有偶然性（总纲 5：改基 linux-next 属集成模式的一次偶发转向） |
| 135.6 | Announce loop-AES-v3.0c | Jari Ruusu 发布文件/交换分区加密包：losetup/mount 的 gpg 管道改用 `--no-options`（Lars Packschies 修复）、对未知密钥数据格式告警、适配 2.6.11-rc3-mm1 移除 QUEUE_FLAG_ORDERED 的变通、修 gcc 参数顺序导致的 Xen 误编译，另发布 ciphers-v3.0b，附 md5 与签名 | 动手者叙事（总纲 10：变更由作者逐条列出）；多方平等（总纲 8：不同作者修复与多平台适配并置）；没有必然性只有偶然性（总纲 5：QUEUE_FLAG_ORDERED 移除与 gcc 参数顺序致误编译，属外部变更带来的偶发适配） |
| 135.7 | 2.6.25-rc5-mm1 | 新增 kgdb 树 git-kgdb-light（Jason Wessel、Ingo Molnar）与 git-security-testing 树（James Morris），自报 x86_64 t61p 上 suspend-to-disk 仍坏（疑 git-x86 所致），规模 3393 commits/1196 patches | 自反性声明（总纲 7：自报 suspend-to-disk 仍坏并保留归因存疑）；动手者叙事（总纲 10：新增与自报由发布者给出）；知识注定过时（总纲 22：“疑 git-x86 所致”系未定的阶段性归因） |
| 135.8 | 2.6.19-rc6-mm2 | 新增 Francois Romieu 的 Chelsio 驱动树 git-chelsio，因镜像暂坏临时存放于 userweb.kernel.org，规模 1641 patches | 动手者叙事（总纲 10：新增与临时存放由发布者给出）；没有必然性只有偶然性（总纲 5：镜像暂坏致临时迁址，属基础设施偶发故障）；分离聚合是永恒规律（总纲 4：新驱动树纳入集成流程） |
| 135.9 | Linux 2.6.13.3 | stable 团队 Chris Wright 发布 2.6.13.3，附 15 文件 diffstat 与修复 shortlog：de_thread() BUG_ON（Alexander Nyberg）、tcp_clamp_window 过度钳制（Alexey Kuznetsov）、yenta oops（Ivan Kokshaysky）、ipvs persistence 连接损坏、UML x86_64 页泄漏、skge mac 地址 bonding oops 与 tcp 默认拥塞控制等，并预告随后跟贴完整补丁及 git 树地址 | 经验优先（总纲 9：以 diffstat 与 shortlog 逐条为判据）；动手者叙事（总纲 10：修复归属由团队点名）；多方平等（总纲 8：线程、网络、驱动、虚拟化多线并置） |
| 135.10 | 2.6.19-rc4-mm1 | 自评 2.6.19-rc3-mm1 相当混乱、本版主要为修复，ACPI 树因 Rafael 测试失败剔除、driver 树因各种问题剔除并连带暂移一批补丁，quilt 树未重拉而 git 树数小时前已重拉，规模 1026 patches | 自反性声明（总纲 7：自评上一版“相当混乱”并明示本版为修复）；动手者叙事（总纲 10：剔除与重拉由发布者自述）；没有必然性只有偶然性（总纲 5：测试失败与各种问题致剔除，属偶发故障） |

---

## 135.1 2.6.25-rc8-mm1

- 【Linux社区】Andrew Morton 发布，评语核心：新增 wm97xx 触摸屏驱动树 git-wm97xx（Mark Brown）与 Al Viro 的 VFS git 树，git-drm 因构建错误剔除、git-xfs 因大量 git 冲突剔除，git-alsa 更名 git-alsa-tiwai、git-md-accel 更名 git-async_tx，规模 5011 commits/1542 patches。 `<!-- ROW_MINE: linux-kernel-announce.messages.724606 -->`

## 135.2 2.6.16-rc5-mm1

- 【Linux社区】Andrew Morton 发布，评语核心：Eric Biederman 的 procfs 大改入树、swap prefetching 补丁回归，kgdb 桩“有点烂”先清理再修（kgdboe 与 x86_64 支持已坏剔除），规模 1259 patches。 `<!-- ROW_MINE: linux-kernel-announce.messages.724625 -->`

## 135.3 2.6.15-mm3

- 【Linux社区】Andrew Morton 发布，评语核心：新增 VMSPLIT_* 配置项支持 x86 非标准用户/内核地址划分并求测试、ext3 多块分配提速（目前仅 direct-IO 使用）、mutex 子系统与 hrtimer 全套入树，并提醒 USB/PCI/driver/I2C 树大量更新“通常令人担忧”，规模 737 patches。 `<!-- ROW_MINE: linux-kernel-announce.messages.724635 -->`

## 135.4 2.6.23-rc4-mm1

- 【Linux社区】Andrew Morton 发布，评语核心：git-kbuild、git-ixgb（被 git-net 破坏）、git-md-accel 均剔除，git-v9fs 破坏所有非 x86 构建故禁用该文件系统，x86_64 dynticks 回归，规模 1628 patches。 `<!-- ROW_MINE: linux-kernel-announce.messages.724641 -->`

## 135.5 2.6.26-rc2-mm1

- 【Linux社区】Andrew Morton 发布，评语核心：-mm 树改基于 linux-next（并偶尔后拉个别树补新料），新增 git-ubifs、git-regulator、git-logfs、git-orion 四个 git 树，规模 1300 commits/534 patches。 `<!-- ROW_MINE: linux-kernel-announce.messages.724644 -->`

## 135.6 Announce loop-AES-v3.0c

- 【Linux社区】Jari Ruusu 发布文件/交换分区加密包，评语核心：losetup/mount 的 gpg 管道改用 `--no-options`（Lars Packschies 修复）、对未知密钥数据格式告警、适配 2.6.11-rc3-mm1 移除 QUEUE_FLAG_ORDERED 的变通、修 gcc 参数顺序导致的 Xen 误编译，另发布 ciphers-v3.0b，附 md5 与签名。 `<!-- ROW_MINE: linux-kernel-announce.messages.724655 -->`

## 135.7 2.6.25-rc5-mm1

- 【Linux社区】Andrew Morton 发布，评语核心：新增 kgdb 树 git-kgdb-light（Jason Wessel、Ingo Molnar）与 git-security-testing 树（James Morris），自报 x86_64 t61p 上 suspend-to-disk 仍坏（疑 git-x86 所致），规模 3393 commits/1196 patches。 `<!-- ROW_MINE: linux-kernel-announce.messages.724674 -->`

## 135.8 2.6.19-rc6-mm2

- 【Linux社区】Andrew Morton 发布，评语核心：新增 Francois Romieu 的 Chelsio 驱动树 git-chelsio，因镜像暂坏临时存放于 userweb.kernel.org，规模 1641 patches。 `<!-- ROW_MINE: linux-kernel-announce.messages.724687 -->`

## 135.9 Linux 2.6.13.3

- 【Linux社区】stable 团队 Chris Wright 发布 2.6.13.3，附 15 文件 diffstat 与修复 shortlog：de_thread() BUG_ON（Alexander Nyberg）、tcp_clamp_window 过度钳制（Alexey Kuznetsov）、yenta oops（Ivan Kokshaysky）、ipvs persistence 连接损坏、UML x86_64 页泄漏、skge mac 地址 bonding oops 与 tcp 默认拥塞控制等，并预告随后跟贴完整补丁及 git 树地址。 `<!-- ROW_MINE: linux-kernel-announce.messages.724730 -->`

## 135.10 2.6.19-rc4-mm1

- 【Linux社区】Andrew Morton 发布，评语核心：自评 2.6.19-rc3-mm1 相当混乱、本版主要为修复，ACPI 树因 Rafael 测试失败剔除、driver 树因各种问题剔除并连带暂移一批补丁，quilt 树未重拉而 git 树数小时前已重拉，规模 1026 patches。 `<!-- ROW_MINE: linux-kernel-announce.messages.724763 -->`
