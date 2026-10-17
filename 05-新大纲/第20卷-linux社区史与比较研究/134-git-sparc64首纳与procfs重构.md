# 134 【Linux社区】git-sparc64首纳与procfs重构

> 来源：linux-kernel-announce 人工信 p22（10 封全读，2005-08 至 2007-01，-mm 发布六封（git-sparc64 首纳与 split ptlock 与 swap 迁移与 slob/git-klibc 因并行 make 被弃/CONFIG_BLOCK=n 直陈已坏/procfs 重构进行中/*at pselect ppoll 赶 2.6.16）、stable 2.6.12.4/.6 全量 diff（IPSEC_POLICY 加 CAP_NET_ADMIN）、vgacon 修复补 Signed-off-by 要求、CD 刻录回归分诊）
> 判定：10 CAND / 0 NV。主题分布：stable 2.6.12.4 补丁 diff 1、vgacon 滚动问题修复回应 1、-mm 2.6.16-rc1-mm1 发布 1、-mm 2.6.16-rc3-mm1 发布 1、-mm 2.6.18-rc2-mm1 发布 1、-mm 2.6.14-mm1 发布 1、stable 2.6.12.6 补丁 diff 1、2.6.20-rc6 回归回应 1、-mm 2.6.18-rc5-mm1 发布 1、-mm 2.6.16-rc5-mm2 发布 1。

> **体例说明（2026-09-14 整改）**：本页 10 块为“速览体例”——各块正文仅保留【Linux社区】条目行与 `<!-- ROW_MINE -->` 定位锚，五字段（要点/史料/史观/辨析/文献）不作逐块展开；块级要点与史观映射见下方“速览详表”，史料即各块 ROW_MINE 锚（`raw_source.raw_json` 可逐条反查），DSLXC claim 著录待 claim 库重跑时统一回填（DEFERRED）。

## 【Linux社区】速览详表（块级要点与史观映射）

| 块号 | 块题 | 要点（浓缩） | 史观映射 |
| --- | --- | --- | --- |
| 134.1 | stable 2.6.12.4 补丁 diff | Chris Wright 发 stable 2.6.12.4 全量 diff：修 powernow-k8 多核数据共享、get_thread_area 未清零、syscall32 错误路径泄漏、bio 克隆漏 bi_idx、skb_header_pointer 下溢、vlan carrier 同步、conntrack 泄引用与 NAT 静态端口竞争、xfrm_user 策略 dir 越界等 | 经验优先（总纲 9：以全量 diff 本体为唯一证据）；动手者叙事（总纲 10：修复本体即维护者行动留痕）；多方平等（总纲 8：电源、内存、网络、安全多线并置） |
| 134.2 | vgacon 滚动问题修复回应 | Jiri Slaby 回应 vgacon 回滚 bug 的修复补丁（删杂散 printk）：认可方向但要求补 Signed-off-by（引 SubmittingPatches）并保留 CC，方可代为推送合入 | 法律与道德是利益分配（总纲 13：Signed-off-by 与 SubmittingPatches 构成社区准入门禁，属贡献权责的分配机制）；动手者叙事（总纲 10：合入条件由维护者给出）；和解优于斗争（总纲 6：认可方向后提出流程补正，不作否定） |
| 134.3 | -mm 2.6.16-rc1-mm1 发布 | 提示大量 reiser3 修复需谨慎测试；拟赶 2.6.16 收入 *at 函数与 pselect/ppoll，unshare 因缺审查难定；附 703 补丁清单 | 动手者叙事（总纲 10：收录与难定由发布者自述）；经验优先（总纲 9：以“需谨慎测试”的实测诉求为判据）；时间是一种形式主义（总纲 18：以 2.6.16 合并窗口为切分依据） |
| 134.4 | -mm 2.6.16-rc3-mm1 发布 | 自称“无甚亮点，除非你花大量时间等 msync()”，请众人帮忙圈定 2.6.16 候选；附 831 补丁注释清单（tty 竞态、JBD 回退等） | 自反性声明（总纲 7：以“无甚亮点”自评当期发布价值）；动手者叙事（总纲 10：候选圈定由发布者发起）；和解优于斗争（总纲 6：以请众人帮忙圈定的协作姿态推进） |
| 134.5 | -mm 2.6.18-rc2-mm1 发布 | git-klibc 因并行 make 问题被弃、新增 git-lxdialog（“看 menuconfig 不必再戴 X 光镜”）、并入延迟记账等，欢迎提醒 2.6.18 候选；附 909 补丁清单 | 动手者叙事（总纲 10：弃置与新增由发布者列举）；没有必然性只有偶然性（总纲 5：git-klibc 因并行 make 偶发问题被弃）；文化即形式主义（总纲 15：以“不必再戴 X 光镜”的诙谐语评述界面改进） |
| 134.6 | -mm 2.6.14-mm1 发布 | 列入 git-ieee1394、恢复 git-drvmodel、新增 git-sparc64 及 v4l/dvb 大批更新；补丁注释含 split page table lock、swap 迁移、slob 分配器、ppc64 64k 页等；附 908 补丁清单 | 动手者叙事（总纲 10：新增与恢复由发布者列举）；分离聚合是永恒规律（总纲 4：git-sparc64 首纳与 git-drvmodel 恢复，属子系统树的聚散重组）；多方平等（总纲 8：架构、分配器、页表、交换多线并置） |
| 134.7 | stable 2.6.12.6 补丁 diff | Chris Wright 发 stable 2.6.12.6 全量 diff：修 sg proc 迭代器释放、usbnet genelink 误用 skb、SIGNAL_GROUP_EXIT 判错字段、zlib inftrees 错误返回、ICMP 失败清理，并为 IP_IPSEC_POLICY 与 IPV6_XFRM_POLICY 加 CAP_NET_ADMIN 检查（安全修复） | 经验优先（总纲 9：以全量 diff 本体为唯一证据）；法律与道德是利益分配（总纲 13：CAP_NET_ADMIN 检查属安全权责的分配）；动手者叙事（总纲 10：修复本体即维护者行动留痕） |
| 134.8 | 2.6.20-rc6 回归回应 | Andrew Morton 回应 Uwe Bugla 的 CD 刻录回归报告：初判为 IDE 驱动故障，请其提供硬件与所用驱动细节，并追问软盘 bug 是否仍在 | 经验优先（总纲 9：以回归报告与硬件细节为判据）；和解优于斗争（总纲 6：以索要细节代替归责）；自反性声明（总纲 7：“初判”明示结论未定，留待复现） |
| 134.9 | -mm 2.6.18-rc5-mm1 发布 | 直陈已知问题——`CONFIG_BLOCK=n` 已坏、nfs 子目录自动挂载仍坏、iio_dummy 致 depmod 失败、sparc32 无法编译；附 1713 补丁清单 | 自反性声明（总纲 7：开篇直陈四项已知问题，不掩饰发布质量）；经验优先（总纲 9：以编译失败与挂载仍坏的实测为准）；多方平等（总纲 8：配置、文件系统、模块、架构四线并置） |
| 134.10 | -mm 2.6.16-rc5-mm2 发布 | 自评“比 rc5-mm1 好些但仍修了一堆才编译启动，我们不够小心”；procfs 重构进行中、initcall 失败将有新告警、audit 树回归；附 1346 补丁清单 | 自反性声明（总纲 7：以“我们不够小心”自陈，并明示 procfs 重构仍在进行）；动手者叙事（总纲 10：自评与进度由发布者给出）；知识注定过时（总纲 22：“重构进行中”属阶段性状态） |

---

## 134.1 stable 2.6.12.4 补丁 diff

- 【Linux社区】Chris Wright 发 stable 2.6.12.4 全量 diff：修 powernow-k8 多核数据共享、get_thread_area 未清零、syscall32 错误路径泄漏、bio 克隆漏 bi_idx、skb_header_pointer 下溢、vlan carrier 同步、conntrack 泄引用与 NAT 静态端口竞争、xfrm_user 策略 dir 越界等。 `<!-- ROW_MINE: linux-kernel-announce.messages.724837 -->`

## 134.2 vgacon 滚动问题修复回应

- 【Linux社区】Jiri Slaby 回应 vgacon 回滚 bug 的修复补丁（删杂散 printk）：认可方向但要求补 Signed-off-by（引 `SubmittingPatches`）并保留 CC，方可代为推送合入。 `<!-- ROW_MINE: linux-kernel-announce.messages.724872 -->`

## 134.3 -mm 2.6.16-rc1-mm1 发布

- 【Linux社区】Andrew Morton 发布 -mm：提示大量 reiser3 修复需谨慎测试；拟赶 2.6.16 收入 *at 函数与 pselect/ppoll，unshare 因缺审查难定；附 703 补丁清单。 `<!-- ROW_MINE: linux-kernel-announce.messages.724873 -->`

## 134.4 -mm 2.6.16-rc3-mm1 发布

- 【Linux社区】Andrew Morton 发布 -mm：自称“无甚亮点，除非你花大量时间等 msync()”，请众人帮忙圈定 2.6.16 候选；附 831 补丁注释清单（tty 竞态、JBD 回退等）。 `<!-- ROW_MINE: linux-kernel-announce.messages.724917 -->`

## 134.5 -mm 2.6.18-rc2-mm1 发布

- 【Linux社区】Andrew Morton 发布 -mm：git-klibc 因并行 make 问题被弃、新增 git-lxdialog（“看 menuconfig 不必再戴 X 光镜”）、并入延迟记账等，欢迎提醒 2.6.18 候选；附 909 补丁清单。 `<!-- ROW_MINE: linux-kernel-announce.messages.724938 -->`

## 134.6 -mm 2.6.14-mm1 发布

- 【Linux社区】Andrew Morton 发布 -mm：列入 git-ieee1394、恢复 git-drvmodel、新增 git-sparc64 及 v4l/dvb 大批更新；补丁注释含 split page table lock、swap 迁移、slob 分配器、ppc64 64k 页等；附 908 补丁清单。 `<!-- ROW_MINE: linux-kernel-announce.messages.724948 -->`

## 134.7 stable 2.6.12.6 补丁 diff

- 【Linux社区】Chris Wright 发 stable 2.6.12.6 全量 diff：修 sg proc 迭代器释放、usbnet genelink 误用 skb、SIGNAL_GROUP_EXIT 判错字段、zlib inftrees 错误返回、ICMP 失败清理，并为 IP_IPSEC_POLICY 与 IPV6_XFRM_POLICY 加 CAP_NET_ADMIN 检查（安全修复）。 `<!-- ROW_MINE: linux-kernel-announce.messages.724965 -->`

## 134.8 2.6.20-rc6 回归回应

- 【Linux社区】Andrew Morton 回应 Uwe Bugla 的 CD 刻录回归报告：初判为 IDE 驱动故障，请其提供硬件与所用驱动细节，并追问软盘 bug 是否仍在。 `<!-- ROW_MINE: linux-kernel-announce.messages.724971 -->`

## 134.9 -mm 2.6.18-rc5-mm1 发布

- 【Linux社区】Andrew Morton 发布 -mm：直陈已知问题——`CONFIG_BLOCK=n` 已坏、nfs 子目录自动挂载仍坏、iio_dummy 致 depmod 失败、sparc32 无法编译；附 1713 补丁清单。 `<!-- ROW_MINE: linux-kernel-announce.messages.725007 -->`

## 134.10 -mm 2.6.16-rc5-mm2 发布

- 【Linux社区】Andrew Morton 发布 -mm：自评“比 rc5-mm1 好些但仍修了一堆才编译启动，我们不够小心”；procfs 重构进行中、initcall 失败将有新告警、audit 树回归；附 1346 补丁清单。 `<!-- ROW_MINE: linux-kernel-announce.messages.725025 -->`
