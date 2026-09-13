# 134. git-sparc64 首纳与 procfs 重构（ann p22）（ann p22）

> 来源：linux-kernel-announce 人工信 p22（10 封全读，2005-08 至 2007-01，-mm 发布六封（git-sparc64 首纳与 split ptlock 与 swap 迁移与 slob/git-klibc 因并行 make 被弃/CONFIG_BLOCK=n 直陈已坏/procfs 重构进行中/*at pselect ppoll 赶 2.6.16）、stable 2.6.12.4/.6 全量 diff（IPSEC_POLICY 加 CAP_NET_ADMIN）、vgacon 修复补 Signed-off-by 要求、CD 刻录回归分诊）
> 判定：10 CAND / 0 NV。主题分布：stable 2.6.12.4 补丁 diff 1、vgacon 滚动问题修复回应 1、-mm 2.6.16-rc1-mm1 发布 1、-mm 2.6.16-rc3-mm1 发布 1、-mm 2.6.18-rc2-mm1 发布 1、-mm 2.6.14-mm1 发布 1、stable 2.6.12.6 补丁 diff 1、2.6.20-rc6 回归回应 1、-mm 2.6.18-rc5-mm1 发布 1、-mm 2.6.16-rc5-mm2 发布 1。

## 134.1 stable 2.6.12.4 补丁 diff

- 【Linux社区】Chris Wright 发 stable 2.6.12.4 全量 diff：修 powernow-k8 多核数据共享、get_thread_area 未清零、syscall32 错误路径泄漏、bio 克隆漏 bi_idx、skb_header_pointer 下溢、vlan carrier 同步、conntrack 泄引用与 NAT 静态端口竞争、xfrm_user 策略 dir 越界等。 `<!-- ROW_MINE: linux-kernel-announce.messages.724837 -->`

## 134.2 vgacon 滚动问题修复回应

- 【Linux社区】Jiri Slaby 回应 vgacon 回滚 bug 的修复补丁（删杂散 printk）：认可方向但要求补 Signed-off-by（引 SubmittingPatches）并保留 CC，方可代为推送合入。 `<!-- ROW_MINE: linux-kernel-announce.messages.724872 -->`

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

- 【Linux社区】Andrew Morton 发布 -mm：直陈已知问题——CONFIG_BLOCK=n 已坏、nfs 子目录自动挂载仍坏、iio_dummy 致 depmod 失败、sparc32 无法编译；附 1713 补丁清单。 `<!-- ROW_MINE: linux-kernel-announce.messages.725007 -->`

## 134.10 -mm 2.6.16-rc5-mm2 发布

- 【Linux社区】Andrew Morton 发布 -mm：自评“比 rc5-mm1 好些但仍修了一堆才编译启动，我们不够小心”；procfs 重构进行中、initcall 失败将有新告警、audit 树回归；附 1346 补丁清单。 `<!-- ROW_MINE: linux-kernel-announce.messages.725025 -->`
