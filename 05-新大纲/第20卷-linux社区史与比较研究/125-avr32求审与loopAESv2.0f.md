# 125 【Linux社区】avr32求审与loopAESv2.0f

> 来源：linux-kernel-announce 人工信 p14（10 封全读，2004-02 至 2007-02，-mm 发布四封（Atmel avr32 新架构求 review/anticipatory 调度器 SCSI TCQ 队列深度限制）、loop-AES v2.0f 与软件挂起兼容、lxdialog curses 依赖 revert 请求、-mm git 导入器故障自愈说明、退订斥责与玩笑 NV）
> 判定：8 CAND / 2 NV。主题分布：-mm 发布宣告 4、bug 报告实质回应 1、git 树同步状态说明 1、工具发布公告 1、bug 报告跟进 1。

> **体例说明（2026-09-14 整改）**：本页 5 块（条目 8 条）为“速览体例”——各块正文仅保留【Linux社区】条目行与 `<!-- ROW_MINE -->` 定位锚，五字段（要点/史料/史观/辨析/文献）不作逐块展开；块级要点与史观映射见下方“速览详表”，史料即各块 ROW_MINE 锚（`raw_source.raw_json` 可逐条反查），DSLXC claim 著录待 claim 库重跑时统一回填（DEFERRED）。

## 【Linux社区】速览详表（块级要点与史观映射）

| 块号 | 块题 | 要点（浓缩） | 史观映射 |
| --- | --- | --- | --- |
| 125.1 | -mm 发布宣告 | 四封 -mm 宣告合块：2.6.20-rc2-mm1（“目前相当平静…待子系统维护者醒来处理”，755 补丁）、2.6.17-rc5-mm3（PCI/USB 大量更新，lock validator 与 IRQ 问题正收敛）、2.6.18-rc1-mm2（新增 Atmel avr32 架构求 review，772 补丁）、2.6.12-rc2-mm3（Jens 补丁限制 anticipatory 调度器在 SCSI TCQ 磁盘上的挂起请求数，可经 /sys/block/hdX/queue/iosched/queue_depth 调优且未经性能测试，819 补丁） | 动手者叙事（总纲 10：四版取舍与自评均由 Morton 亲述）；经验优先（总纲 9：以补丁清单、调优路径与“未经性能测试”的声明为准）；没有必然性只有偶然性（总纲 5：avr32 新架构之纳入非规划所致） |
| 125.2 | bug 报告实质回应 | Uwe Bugla 回应 2.6.20-rc6 已知回归清单：确认 floppy bug 已消失，补充 IDE 硬件为 Intel 南北桥加标准 idecd 驱动，报告刻录设备在 rc6 完全不被识别并称将测试 Mike 的补丁 | 经验优先（总纲 9：以 floppy bug 消失与刻录设备不被识别的实测为准）；多方平等（总纲 8：用户复测结果与维护者清单并列登记，不以报告者身份分等） |
| 125.3 | git 树同步状态说明 | Matthias Urlichs 回应 2.6.16-rc5-mm3：说明 -mm git 导入器出故障漏掉了最近三个 -mm 内核，数小时内自愈，并告知通常发布公告后 2 小时内即可经 git 获取 | 自反性声明（总纲 7：主动披露自家导入器故障与漏掉的内核数）；经验优先（总纲 9：以“2 小时内可获取”的实际时延为口径）；知识注定过时（总纲 22：自愈式故障说明只对当期基础设施有效） |
| 125.4 | 工具发布公告 | Jari Ruusu 发布 loop-AES-v2.0f：initrd 在 2.6 内核按 .ko 加载 loop 模块、loop 代码兼容 Pavel Machek 软件挂起、`build-initrd.sh` 默认值改为 `USEGPGKEY=1`，并附 ciphers-v2.0f 变更与 tarball/md5 链接 | 动手者叙事（总纲 10：树外加密包由作者亲自维护并逐项列出变更）；经验优先（总纲 9：以模块加载方式与挂起兼容等具体技术变更为准）；多方平等（总纲 8：树外方案与主线 -mm 并列登记） |
| 125.5 | bug 报告跟进 | Steve Fox（IBM LTC）指出 2.6.18-rc5-mm1 仍存在 curses 开发库依赖：普通 make vmlinux 会尝试构建 menuconfig 目标致 curses.h 报错，随信附 Andy Whitcroft 对 Sam Ravnborg 的 git-lxdialog 相关 commit 的定位分析，请求 revert 或修复 | 经验优先（总纲 9：以 commit 级定位分析与可复现的构建报错为判据）；动手者叙事（总纲 10：缺陷定位由 IBM 开发者一手完成）；没有必然性只有偶然性（总纲 5：curses 依赖由一次 git-lxdialog 提交偶然引入） |

---

## 125.1 -mm 发布宣告

- 【Linux社区】Andrew Morton 发布 2.6.20-rc2-mm1，评语“目前相当平静，其中不少补丁是 2.6.20 所需、待子系统维护者醒来处理”，附相对 2.6.20-rc1-mm1 的补丁增删清单及全量 755 补丁列表。 `<!-- ROW_MINE: linux-kernel-announce.messages.722551 -->`
- 【Linux社区】Andrew Morton 发布 2.6.17-rc5-mm3，评语“大量 PCI 与 USB 更新；lock validator、栈回溯与 IRQ 管理各类问题正收敛但尚未到位”，附相对 2.6.17-rc5-mm2 的变更清单。 `<!-- ROW_MINE: linux-kernel-announce.messages.722604 -->`
- 【Linux社区】Andrew Morton 发布 2.6.18-rc1-mm2，评语“补丁有并有删，无特别亮点；新增 Atmel avr32 架构，求 review”，附相对 2.6.18-rc1-mm1 的补丁变更说明与全量 772 补丁列表。 `<!-- ROW_MINE: linux-kernel-announce.messages.722651 -->`
- 【Linux社区】Andrew Morton 发布 2.6.12-rc2-mm3，评语重点：Jens 补丁限制预期（anticipatory）I/O 调度器在 SCSI TCQ 磁盘上的挂起请求数（默认 1，可经 /sys/block/hdX/queue/iosched/queue_depth 调优，未经性能测试），另含 CPU 调度器推进与全量 819 补丁列表。 `<!-- ROW_MINE: linux-kernel-announce.messages.722791 -->`

## 125.2 bug 报告实质回应

- 【Linux社区】Uwe Bugla 回应 2.6.20-rc6 已知回归清单：确认 floppy bug 已消失，补充 IDE 硬件为 Intel 南北桥加标准 idecd 驱动，报告刻录设备在 rc6 完全不被识别并称将测试 Mike 的补丁。 `<!-- ROW_MINE: linux-kernel-announce.messages.722609 -->`

## 125.3 git 树同步状态说明

- 【Linux社区】Matthias Urlichs 回应 2.6.16-rc5-mm3：说明 -mm git 导入器出故障漏掉了最近三个 -mm 内核，数小时内自愈，并告知通常发布公告后 2 小时内即可经 git 获取。 `<!-- ROW_MINE: linux-kernel-announce.messages.722643 -->`

## 125.4 工具发布公告

- 【Linux社区】Jari Ruusu 发布 loop-AES-v2.0f 文件/swap 加密包，实质变更：initrd 在 2.6 内核按 .ko 加载 loop 模块、loop 代码兼容 Pavel Machek 软件挂起、`build-initrd.sh` 默认值改为 `USEGPGKEY=1` 等，并附 ciphers-v2.0f 变更与 tarball/md5 链接。 `<!-- ROW_MINE: linux-kernel-announce.messages.722665 -->`

## 125.5 bug 报告跟进

- 【Linux社区】Steve Fox（IBM LTC）指出 2.6.18-rc5-mm1 仍存在 curses 开发库依赖：普通 make vmlinux 会尝试构建 menuconfig 目标致 curses.h 报错，随信附 Andy Whitcroft 对 Sam Ravnborg 的 git-lxdialog 相关 commit 的定位分析，请求 revert 或修复。 `<!-- ROW_MINE: linux-kernel-announce.messages.722666 -->`
