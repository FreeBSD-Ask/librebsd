# 133 【Linux社区】kmap根因与栈保护安慰剂

> 来源：linux-kernel-announce 人工信 p20（10 封全读，2004-05 至 2007-08，-mm 发布五封（perfctr 移除转 perfmon/hrtimers 未修 Vaio 变慢/git-ixgbe 被 git-net 破坏/automounter 略坏与 Alpha coredump 异常/SCSI 开机告警风暴）、Morton 自报并定位 kmap_atomic async_tx 共用槽根因、stable 2.6.12.4 与 2.6.15.3（CVE-2006-0454）、loop-AES v2.1a、coredump 管道过滤与栈保护“安全安慰剂”评语）
> 判定：10 CAND / 0 NV。主题分布：stable 发布宣告 2、工具公告 1、mm 发布宣告 5、bug 回应 1、bug 报告 1。

> **体例说明（2026-09-14 整改）**：本页 10 块为“速览体例”——各块正文仅保留【Linux社区】条目行与 `<!-- ROW_MINE -->` 定位锚，五字段（要点/史料/史观/辨析/文献）不作逐块展开；块级要点与史观映射见下方“速览详表”，史料即各块 ROW_MINE 锚（`raw_source.raw_json` 可逐条反查），DSLXC claim 著录待 claim 库重跑时统一回填（DEFERRED）。

## 【Linux社区】速览详表（块级要点与史观映射）

| 块号 | 块题 | 要点（浓缩） | 史观映射 |
| --- | --- | --- | --- |
| 133.1-1 | stable 发布宣告（Linux 2.6.12.4） | Chris Wright 发布 Linux 2.6.12.4，附 diffstat 与 14 文件修复摘要（powernow 双核 oops、vlan 早期添加失效、conntrack 卸载死锁、NAT 内存破坏、恶意 32 位 ELF 泄漏等），并预告回帖附完整补丁与 2.6.12.y git 树 | 经验优先（总纲 9：以 diffstat 与逐条修复为判据）；动手者叙事（总纲 10：修复清单由维护者给出）；多方平等（总纲 8：电源、网络、内存、安全四线并置） |
| 133.1-2 | stable 发布宣告（Linux 2.6.15.3） | Chris Wright 发布 Linux 2.6.15.3，仅含一个安全修复 CVE-2006-0454 可被用作远程 DoS，附 diffstat 与 Herbert Xu 的 ip_options_echo 失败时多余 dst 释放修复摘要，预告回帖附补丁 | 经验优先（总纲 9：以 diffstat 与 CVE 编号为判据）；法律与道德是利益分配（总纲 13：CVE 编号与披露节奏属安全信息的分配机制）；动手者叙事（总纲 10：修复归属由发布者点名） |
| 133.2-1 | 工具公告（loop-AES-v2.1a） | Jari Ruusu 发布 loop-AES-v2.1a 文件/交换加密包，逐条列实质变更：安全修复限 passphrase 最长 4094 字节、大端机免字节交换提速、64 位 ioctl32 兼容、build-initrd.sh 省 40KB 内核内存，并附 ciphers-v2.0g 与 md5/签名 | 动手者叙事（总纲 10：变更由作者逐条列出）；经验优先（总纲 9：以内存占用与兼容性实测为准）；没有必然性只有偶然性（总纲 5：大端机与 64 位兼容属外部平台演进带来的偶发适配） |
| 133.3-1 | mm 发布宣告（2.6.13-mm3） | perfctr 因作者停止开发而移除转推 perfmon、收录多项性能调优补丁（预读后即退出的 AS 修复、页分配器 per-cpu magazine 增容与高阶分配）、撤下全部虚拟化准备补丁待 chrisw git 树、预计 30-50 补丁进 2.6.14，共 473 补丁 | 动手者叙事（总纲 10：移除与收录由发布者自述）；没有必然性只有偶然性（总纲 5：perfctr 因作者停摆而移除，非技术必然）；时间是一种形式主义（总纲 18：以“预计 30-50 补丁进 2.6.14”作版本切分预期） |
| 133.3-2 | mm 发布宣告（2.6.19-rc4-mm2） | 赶工主要为测试驱动树更新、hrtimers 与 dynticks 大更新实测未修 Vaio 变慢问题、大量 fbdev 更新、make headers_check 在 i386 已知损坏，共 1113 补丁 | 经验优先（总纲 9：以 Vaio 变慢与 headers_check 损坏的实测为准）；自反性声明（总纲 7：明示大更新未解决目标问题，不掩饰）；知识注定过时（总纲 22：hrtimers 与 dynticks 的“未修”属阶段性结论） |
| 133.3-3 | mm 发布宣告（2.6.13-rc6-mm1） | 开场评语简短但含实质警示：开启相应调试选项后 SCSI 代码开机将产生睡眠原子上下文告警风暴且正在处理；changelog 注明 libata 与 netdev 已换成合并 git 树，共 940 补丁 | 动手者叙事（总纲 10：警示与变更由发布者给出）；经验优先（总纲 9：以调试选项下的告警风暴实况为判据）；分离聚合是永恒规律（总纲 4：libata 与 netdev 换用合并 git 树，属子系统树的聚合重组） |
| 133.3-4 | mm 发布宣告（2.6.23-rc3-mm1） | git-ixgbe 被 git-net 破坏而丢弃、git-net 因不可用整体撤下、-mm 的 import-to-git 引擎仍故障，共 1396 补丁 | 动手者叙事（总纲 10：丢弃与撤下由发布者自述）；自反性声明（总纲 7：公开承认自身工具链仍故障）；没有必然性只有偶然性（总纲 5：git 树互相破坏致整线撤下，属工具链偶发耦合） |
| 133.3-5 | mm 发布宣告（2.6.18-rc4-mm2） | 因 git 问题未拉 Greg 的 rc4 后驱动树、automounter 已知略坏、Alpha coredump 不正常；changelog 含 core_pattern 管道过滤 coredump、栈保护补丁（作者自称“安全安慰剂”）等，共 1544 补丁 | 自反性声明（总纲 7：以“安全安慰剂”自陈补丁效用存疑，当事人自述与史家判断可分离）；动手者叙事（总纲 10：未拉树与已知问题由发布者交代） |
| 133.4-1 | bug 回应（kmap_atomic oops） | Andrew Morton 回应 Evgeniy Polyakov 的 kmap_atomic oops 讨论，确认 async_tx 在 ASYNC_TX_KMAP_SRC 与 DST 同设时会复用同一 kmap 槽致数据损坏或 BUG，并说明无条件 kmap_atomic 对非 highmem 页基本无开销 | 经验优先（总纲 9：以复现路径与槽位复用事实为判据）；动手者叙事（总纲 10：根因确认由维护者给出）；和解优于斗争（总纲 6：以技术确认回应异议，不作人身争辩） |
| 133.5-1 | bug 报告（主线 kmap_atomic 随机 oops） | Andrew Morton 报告主线 kmap_atomic 随机 oops，定位到 BUG_ON(!pte_none(...)) 提示 km_type 收到野值，并指认 async_tx 条件 kmap 代码在 src 与 dst 同时映射时共用槽位会损坏数据，请近期网络相关改动者自查 | 经验优先（总纲 9：以 oops 现场与 BUG_ON 断言为唯一判据）；动手者叙事（总纲 10：报告者即定位者）；没有必然性只有偶然性（总纲 5：随机 oops 属低概率偶发，需条件同时满足方触发） |

---

## 133.1 stable 发布宣告

- 【Linux社区】Chris Wright 发布 Linux 2.6.12.4，附 diffstat 与 14 文件修复摘要（powernow 双核 oops、vlan 早期添加失效、conntrack 卸载死锁、NAT 内存破坏、恶意 32 位 ELF 泄漏等），并预告回帖附完整补丁与 2.6.12.y git 树。 `<!-- ROW_MINE: linux-kernel-announce.messages.724390 -->`
- 【Linux社区】Chris Wright 发布 Linux 2.6.15.3，仅含一个安全修复 CVE-2006-0454 可被用作远程 DoS，附 diffstat 与 Herbert Xu 的 ip_options_echo 失败时多余 dst 释放修复摘要，预告回帖附补丁。 `<!-- ROW_MINE: linux-kernel-announce.messages.724601 -->`

## 133.2 工具公告

- 【Linux社区】Jari Ruusu 发布 loop-AES-v2.1a 文件/交换加密包，逐条列实质变更：安全修复限 passphrase 最长 4094 字节、大端机免字节交换提速、64 位 ioctl32 兼容、build-initrd.sh 省 40KB 内核内存，并附 ciphers-v2.0g 与 md5/签名。 `<!-- ROW_MINE: linux-kernel-announce.messages.724411 -->`

## 133.3 mm 发布宣告

- 【Linux社区】Andrew Morton 发布 2.6.13-mm3，评语：perfctr 因作者停止开发而移除转推 perfmon、收录多项性能调优补丁（预读后即退出的 AS 修复、页分配器 per-cpu magazine 增容与高阶分配）、撤下全部虚拟化准备补丁待 chrisw git 树、预计 30-50 补丁进 2.6.14，共 473 补丁。 `<!-- ROW_MINE: linux-kernel-announce.messages.724428 -->`
- 【Linux社区】Andrew Morton 发布 2.6.19-rc4-mm2，评语：赶工主要为测试驱动树更新、hrtimers 与 dynticks 大更新实测未修 Vaio 变慢问题、大量 fbdev 更新、make headers_check 在 i386 已知损坏，共 1113 补丁。 `<!-- ROW_MINE: linux-kernel-announce.messages.724460 -->`
- 【Linux社区】Andrew Morton 发布 2.6.13-rc6-mm1，开场评语简短但含实质警示：开启相应调试选项后 SCSI 代码开机将产生睡眠原子上下文告警风暴且正在处理；changelog 注明 libata 与 netdev 已换成合并 git 树，共 940 补丁。 `<!-- ROW_MINE: linux-kernel-announce.messages.724508 -->`
- 【Linux社区】Andrew Morton 发布 2.6.23-rc3-mm1，评语：git-ixgbe 被 git-net 破坏而丢弃、git-net 因不可用整体撤下、-mm 的 import-to-git 引擎仍故障，共 1396 补丁。 `<!-- ROW_MINE: linux-kernel-announce.messages.724543 -->`
- 【Linux社区】Andrew Morton 发布 2.6.18-rc4-mm2，评语：因 git 问题未拉 Greg 的 rc4 后驱动树、automounter 已知略坏、Alpha coredump 不正常；changelog 含 core_pattern 管道过滤 coredump、栈保护补丁（作者自称“安全安慰剂”）等，共 1544 补丁。 `<!-- ROW_MINE: linux-kernel-announce.messages.724605 -->`

## 133.4 bug 回应

- 【Linux社区】Andrew Morton 回应 Evgeniy Polyakov 的 kmap_atomic oops 讨论，确认 async_tx 在 ASYNC_TX_KMAP_SRC 与 DST 同设时会复用同一 kmap 槽致数据损坏或 BUG，并说明无条件 kmap_atomic 对非 highmem 页基本无开销。 `<!-- ROW_MINE: linux-kernel-announce.messages.724442 -->`

## 133.5 bug 报告

- 【Linux社区】Andrew Morton 报告主线 kmap_atomic 随机 oops，定位到 BUG_ON(!pte_none(...)) 提示 km_type 收到野值，并指认 async_tx 条件 kmap 代码在 src 与 dst 同时映射时共用槽位会损坏数据，请近期网络相关改动者自查。 `<!-- ROW_MINE: linux-kernel-announce.messages.724505 -->`
