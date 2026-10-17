# 115 【Linux社区】tty大改写与git-slub

> 来源：linux-kernel-announce 人工信 p7（10 封全读，2005-03 至 2008-02，-mm 发布八封（Alan Cox tty 缓冲大改写/SATA Kconfig 全改名警告与二分指引/git-slub 树首纳/rbtree 缩节点/四树换 gregkh patch 系）、stable 2.6.14.3 修复摘要、2.6.15.1 补丁全文）
> 判定：10 CAND / 0 NV。主题分布：mm 树发布宣告 8、stable 发布宣告 1、stable 补丁跟帖 1。

> **体例说明（2026-09-14 整改）**：本页 3 块为“速览体例”——各块正文仅保留【Linux社区】条目行与 `<!-- ROW_MINE -->` 定位锚（115.1 收纳八封 -mm 宣告），五字段（要点/史料/史观/辨析/文献）不作逐块展开；块级要点与史观映射见下方“速览详表”，史料即各块 ROW_MINE 锚（`raw_source.raw_json` 可逐条反查），DSLXC claim 著录待 claim 库重跑时统一回填（DEFERRED）。

## 【Linux社区】速览详表（块级要点与史观映射）

| 块号 | 块题 | 要点（浓缩） | 史观映射 |
| --- | --- | --- | --- |
| 115.1 | mm 树发布宣告 | 八封 -mm 宣告合块：2.6.12-rc1-mm3（DRM/USB 恢复与 sata_sil 修复求测）、2.6.13-mm1（收入 Alan Cox tty 层缓冲大改写致冷门字符驱动编译失败）、2.6.18-rc4-mm1（SATA Kconfig 全改名、盲 make oldconfig 会“没有磁盘”并附二分指引）、2.6.16-rc5-mm3（各 git 树 diff 达 9MB）、2.6.25-rc2-mm1（git-xfs 冲突与 git-x86 非 x86 改动过大被剔除、新增 git-slub）、2.6.12-rc2-mm2（bk 弃用换 gregkh-*.patch、自曝 bk-acpi 致 ia64 挂起）、2.6.14-rc2-mm2（内存管理大批更新、pcmcia 暂弃、告知离线期关键修复直发 Linus）、2.6.17-rc3-mm1（新纳 git-rbtree/git-sas/git-supertrak） | 动手者叙事（总纲 10：八版取舍与自曝故障均由 Morton 亲述）；经验优先（总纲 9：以编译失败、挂起与 diff 体量实测为准）；偶然性优先（总纲 5：树之纳入与剔除随当期冲突而定） |
| 115.2 | stable 发布宣告 | Chris Wright 代表 -stable 团队发布 2.6.14.3：附 diffstat 与完整修复摘要，32 个文件 177 处插入，含 PPTP NAT 字节序、conntrack 高端口助手、早期 Nocona MTRR、ALSA rtc 软锁死等修复 | 动手者叙事（总纲 10：stable 分支维护由团队亲述并给出逐项清单）；经验优先（总纲 9：以文件数与插入数等可核数据为准）；多方平等（总纲 8：stable 分支与 -mm 主线并列登记，不预设主从） |
| 115.3 | stable 补丁跟帖 | Chris Wright 跟帖贴出 2.6.15 至 2.6.15.1 完整补丁：moxa 驱动补 CAP_SYS_RAWIO 权限检查、skge 多处修复、workqueue 单线程 CPU 取址修复、netlink 消息长度检查 | 经验优先（总纲 9：以补丁本体为唯一证据，无文字评语）；动手者叙事（总纲 10：修复本体即维护者行动留痕）；自反性声明（总纲 7：公告与补丁本体成对留存，可被逐行复核） |

---

## 115.1 mm 树发布宣告

- 【Linux社区】Andrew Morton 发布 2.6.12-rc1-mm3，称相对上一版主要是一批修复，请遇 DRM 与 USB 恢复问题的用户测试报告，并请 Silicon Image SATA 用户验证随附的 sata_sil 损坏与锁死修复补丁。 `<!-- ROW_MINE: linux-kernel-announce.messages.720989 -->`
- 【Linux社区】Andrew Morton 发布 2.6.13-mm1，核心评语为收入 Alan Cox 的 tty 层缓冲大改写，导致多个冷门字符设备驱动编译失败，欢迎补丁并请抄送 Alan。 `<!-- ROW_MINE: linux-kernel-announce.messages.721020 -->`
- 【Linux社区】Andrew Morton 发布 2.6.18-rc4-mm1，警告全部 SATA Kconfig 选项已改名，盲目 make oldconfig 会“没有磁盘”，并附 -mm 二分定位 bug 的操作指引等使用说明。 `<!-- ROW_MINE: linux-kernel-announce.messages.721077 -->`
- 【Linux社区】Andrew Morton 发布 2.6.16-rc5-mm3，称相对变化不多但各 git 子系统树 diff 已达 9MB，列出来自四十余个 git 树的合并、修复与剔除清单。 `<!-- ROW_MINE: linux-kernel-announce.messages.721088 -->`
- 【Linux社区】Andrew Morton 发布 2.6.25-rc2-mm1，说明 git-xfs 因冲突、git-x86 因非 x86 改动过大被剔除，新增 Christoph Lameter 的 slab/slub 树 git-slub。 `<!-- ROW_MINE: linux-kernel-announce.messages.721107 -->`
- 【Linux社区】Andrew Morton 发布 2.6.12-rc2-mm2，说明 bk-audit 因与其他树冲突暂弃、Greg 弃用 bk 后 bk-pci/i2c/driver-core/usb 换为 gregkh-*.patch，并自曝 bk-acpi 使其 ia64 测试机启动挂起。 `<!-- ROW_MINE: linux-kernel-announce.messages.721128 -->`
- 【Linux社区】Andrew Morton 发布 2.6.14-rc2-mm2，称有大批内存管理更新、pcmcia 大改因 Dominik 建树有问题暂弃、多个冷门 tty 驱动仍编译不过，并告知 10 月 9 日前离线、关键修复请直发 Linus。 `<!-- ROW_MINE: linux-kernel-announce.messages.721143 -->`
- 【Linux社区】Andrew Morton 发布 2.6.17-rc3-mm1，说明新纳入 git-rbtree（缩小 rb 树节点）、git-sas（aic94xx 串行 attached storage 驱动）与 git-supertrak（Promise SuperTrak 控制器驱动）三个树。 `<!-- ROW_MINE: linux-kernel-announce.messages.721214 -->`

## 115.2 stable 发布宣告

- 【Linux社区】Chris Wright 代表 -stable 团队发布 Linux 2.6.14.3，附 diffstat 与完整修复摘要，32 个文件 177 处插入，含 PPTP NAT 字节序、conntrack 高端口助手、早期 Nocona MTRR、ALSA rtc 软锁死等修复。 `<!-- ROW_MINE: linux-kernel-announce.messages.721141 -->`

## 115.3 stable 补丁跟帖

- 【Linux社区】Chris Wright 跟帖回复 Linux 2.6.15.1 宣告，正文无评语、直接贴出 2.6.15 至 2.6.15.1 完整补丁，实质内容含 moxa 驱动补 CAP_SYS_RAWIO 权限检查、skge 多处修复、workqueue 单线程 CPU 取址修复与 netlink 消息长度检查等 stable 修复本体。 `<!-- ROW_MINE: linux-kernel-announce.messages.721155 -->`
