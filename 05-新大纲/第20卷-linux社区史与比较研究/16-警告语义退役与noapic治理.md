# 16 【Linux社区】警告语义退役与noapic治理

> 对应页面：linux-smp p24（pk 1572488-1572537，2002-2007 为主）
> 判定：47 CAND / 3 NV（018/025 空正文、045 纯寒暄）
> 编号：DSLXC-4469..4515 | claim 已入库（47/47，dslinux_claims.duckdb）

## 16.1 【Linux社区】unexpected IO-APIC 报料全景（13 例）

**要点**：Debian User/Tarvo Kurm（2003-05-12，爱沙尼亚）：UP 单核 Athlon XP 1600+（Processors: 1）Debian 2.4.20-k7，IO-APIC version 0003 警告，正文完整 dmesg；“Computer seems to work normally otherwise”“Sorry for spamming if this is a resolved issue”——UP 触发警告又一例；Sofía Muñoz Vélez（2007-12-27，Telefónica 马德里）：ESX 3.02（2.4.21-47.0.1.ELvmnix、vmkernel 63195）unexpected IO-APIC 求助原帖——p23 043 Mouw 回复的原帖（跨页对）；Jan Taegert（2002-10-06）：MSI KT3 Ultra2（AMI BIOS 5.6）Athlon XP 1600+ UP（2.4.19）IO-APIC v0003 警告，完整 syslog——UP KT3 报料；Hans Wilmer（2002-10-12）：单 CPU Athlon XP 2000（MSI KT3 Ultra2）2.4.18 开 APIC/IO-APIC 后 v3 警告，附 lspci 与 /proc/interrupts——UP 报料；root（2003-01-03，hentschelit.de）：GIGABYTE 7VRXP Athlon XP 1900+（UP）2.4.19-16mdkcustom IO-APIC version 0002 警告，正文完整 dmesg（subject 为 unknown）——v2 转储样本；Eugene B. Prokhorenko（2003-09-21，亚美尼亚 YerPhI）：P4 2.4 HT（865PE）Slackware 9.0 2.4.20 编 SMP 后 unexpected IO-APIC，“Linux works normal. But what should I do with this message?”——HT 平台警告咨询；lk@trolloc.com（2003-04-16）：Supermicro X5DPE-G2（Intel 7502）2.4.21-pre7-ac1 首报——五 IO-APIC #2/#3/#4/#5/#8、双 Xeon 2.40、“WARNING: No sibling found for CPU 0/1”、“last message repeated 3 times”——p23 023 补全的原帖（跨页对）；Josh Wyatt（2004-02-28）：Shuttle XPC + hostap 0.1.3，2.4.25 IO-APIC version 0014 警告 + 当天两次 crash（2.4.22 同 config 稳定但同样有 v14 警告，“Probably safe to assume the unexpected APIC bit did not cause the crash”）——v14 警告与崩溃关联排除；bart alberti（2003-10-31）：Asus P4C800-E deluxe（P4 3.0 HT，cpu_sibling_map 0↔1）SuSE 8.1（APIC 未启用安装）——IO-APIC version 0020 + **register #02: 00178020（#02 非零）**——v20 寄存器#02 残值样本（与 p21 D865PERL 同族）；James Howsden（2002-12-18）：每次启动 /var/log/messages 出现警告，“asks that I mail this to you”附片段——例行报料样本；Robert Singleton（2002-05-09，Los Alamos 国家实验室）：Dell 620 Workstation RH7.2 警告，“Is this of concern?”附完整 boot message——国家实验室例行报料；Philipp Schulte（2002-06-11，杜伊斯堡大学）：Gigabyte GA-7VTXH+ Athlon XP 1600+ Debian 2.2 内核 2.4.18，IO-APIC version 0002 警告正文全 dump——GA-7VTXH+ v2 样本（与 p23 037 GA-7VTXH 同族板）；David Boulware（2005-04-26）：Dell Dimension 4700 Debian 2.4.17/2.4.18 安装失败——IO-APIC #8 version 0020 + **register #02: 00170020（PRQ=0）**警告 + ide2 unexpected interrupt status=0xd0 每秒刷屏——PCI 设备找不到与寄存器#02 残值样本（v20 #02 残值又一例）

**史料**：`1572488`、`1572491`、`1572492`、`1572493`、`1572494`、`1572495`、`1572499`、`1572504`、`1572517`、`1572527`、`1572530`、`1572531`、`1572536`

【Linux社区】**史料锚**：`<!-- ROW_MINE: linux-smp.messages.1572488 -->` `<!-- ROW_MINE: linux-smp.messages.1572491 -->` `<!-- ROW_MINE: linux-smp.messages.1572492 -->` `<!-- ROW_MINE: linux-smp.messages.1572493 -->` `<!-- ROW_MINE: linux-smp.messages.1572494 -->` `<!-- ROW_MINE: linux-smp.messages.1572495 -->` `<!-- ROW_MINE: linux-smp.messages.1572499 -->` `<!-- ROW_MINE: linux-smp.messages.1572504 -->` `<!-- ROW_MINE: linux-smp.messages.1572517 -->` `<!-- ROW_MINE: linux-smp.messages.1572527 -->` `<!-- ROW_MINE: linux-smp.messages.1572530 -->` `<!-- ROW_MINE: linux-smp.messages.1572531 -->` `<!-- ROW_MINE: linux-smp.messages.1572536 -->`

**史观**：经验优先（总纲第 9 条——经验优先：以 UP 触发四例、v20 register #02 残值与 v14 崩溃排除为判据）；本体论上各方平等（总纲第 8 条——本体论上各方平等：UP 家用用户、国家实验室与电信运营商企业报料并置）
**辨析**：v14 与崩溃的关联被当事人自行排除（原文作“Probably safe to assume…”），属推断而非实测；本块与 p23 023、043 为跨页对，不得重复计数。
**文献**：DSLXC-4469/4472/4473/4474/4475/4476/4480/4485/4496/4506/4509/4510/4514（`linux-smp.messages.1572488` 等 13 封，2002-05-09 至 2007-12-27），全文见 `raw_source.raw_json`

## 16.2 【Linux社区】警告语义定调与 UNEXPECTED_IO_APIC 退役之争

**要点**：Alan Cox（2002-07-10）答 Jim Crippen：**“Its ok. I really do need to update that message so it doesn't say WARNING in big letters”“Basically it found a chip rev it didnt know. Since the PIV apic seems to work ok its not actually a problem”**——警告措辞应改的裁定（警告语义史关键一手）；Len Brown（2003-11-07）：**IO APIC version 0080** 警告 + “I see that UNEXPECTED_IO_APIC() was made into a no-op in 2.6. Either it should be deleted from both 2.4 and 2.6, or the list should be updated, yes?”——警告机制退役裁定的 Intel 侧一手

**史料**：`1572500`、`1572520`

【Linux社区】**史料锚**：`<!-- ROW_MINE: linux-smp.messages.1572500 -->` `<!-- ROW_MINE: linux-smp.messages.1572520 -->`

**史观**：经验优先（总纲第 9 条——经验优先：以“应改措辞”裁定与 2.6 已作 no-op 的实查为判据）；知识注定过时（总纲第 22 条——知识注定过时：警告措辞与版本名单随内核演进须更新或删除）
**辨析**：“应改措辞”与“或删或更新名单”均为维护者建议；2.6 已作 no-op 属事实，2.4 侧处置未见结论。
**文献**：DSLXC-4481/4499（`linux-smp.messages.1572500`、`.1572520`，2002-07-10 至 2003-11-07），全文见 `raw_source.raw_json`

## 16.3 【Linux社区】noapic 治理：实测、处方与长期个案（6 例）

**要点**：E. Robert Bogusta（2002-07-07）答 Ivanovic：4×Xeon noapic 后 uptime 从 1-4 天跳到 54 天+，“it is keeping up with load so the effect has to be down in the noise. The system only get about 3000-3500 int/sec, one CPU is happy to do that”——noapic 长稳与中断率实测；Bill Davidsen（2002-10-31）：全国 ISP 六州新闻服务器 vmstat2 实测数据，“I can measure no difference between noapic and apic except by looking at /proc/interrupts”并向 Alan Cox 求证——noapic 无差异实测；Neil Robst（2003-02-19）：按网上建议 **noapic 启动两台后 20+ 小时稳定**，问 noapic 对服务器的影响——noapic 缓解实证（p23 047 同线程续）；Russ W. Knize（2004-02-17）：Tyan Tiger 100（S1832DL）双 PII 333 Deschutes——历来只有 noapic 可启动，IDE lost interrupts on /dev/hda，2.4.ancient~2.4.24 同果，BIOS PnP/MPS/PCI/IRQ 全试并拔光 PCI 卡无效，“Is my APIC toast?”——noapic 必需的长期个案；Earle Nietzel（2005-05-05）答 Tim Day（6VXDC7 悬案）：“Have you tried using 'noapic'?”——同线程跨页首回应；Tim Day（2005-05-09）答 Nietzel：MP 1.1/1.4 BIOS 选项“Tried that too. Makes no noticeable difference unfortunately”——6VXDC7 悬案又一排除项（与 p23 001 连成完整排除链：BIOS/boot/memcheck/PSU/MP 版本全试尽）

**史料**：`1572489`、`1572490`、`1572503`、`1572515`、`1572516`、`1572528`

【Linux社区】**史料锚**：`<!-- ROW_MINE: linux-smp.messages.1572489 -->` `<!-- ROW_MINE: linux-smp.messages.1572490 -->` `<!-- ROW_MINE: linux-smp.messages.1572503 -->` `<!-- ROW_MINE: linux-smp.messages.1572515 -->` `<!-- ROW_MINE: linux-smp.messages.1572516 -->` `<!-- ROW_MINE: linux-smp.messages.1572528 -->`

**史观**：经验优先（总纲第 9 条——经验优先：以 54 天长稳、六州 vmstat2 无差异实测与 Tiger 100 长期个案为判据）；没有必然性，只有偶然性（总纲第 5 条——没有必然性，只有偶然性：noapic 是否必需由具体板卡与 BIOS 偶然决定）
**辨析**：“看不出差异”限于该新闻服务器的负载形态，不可外推；Tiger 100 个案原文自问“Is my APIC toast?”，无确诊结论。
**文献**：DSLXC-4470/4471/4484/4494/4495/4507（`linux-smp.messages.1572489` 等 6 封，2002-07-07 至 2005-05-09），全文见 `raw_source.raw_json`

## 16.4 【Linux社区】多路平台兼容与 BIOS 处方（10 例）

**要点**：Kees-Jan van den Bogaard（2003-03-20，FLUCON 荷兰）：MS-6368 + SuSE 7.1 2.4.0-64GB-SMP 单 Celeron 1300（“Error: only one processor found”），IO-APIC v0011 警告 + Moxa CI123 ISA 双 16550 串口卡 mxser 驱动故障关联疑问 + activating NMI Watchdog——老内核与 ISA 卡咨询；joe.dev@uku.co.uk（2005-12-06）：双 P3 Debian sarge 2.6.8-2-smp——UP 内核硬件 modem 可用、SMP 内核找不到，求方向——SMP 内核设备探测差异咨询；Eyal Lebedinsky（2002-08-03）：Epox D3VA 最快 PIII 选型咨询（SMP 模式）——主板选型样本；Alan Cox（2002-09-18）答 Joao Almeida（x440 4×Xeon 1.4 RH7.1 只认 3 CPU）：**“Red Hat 7.1 kernels are way too old to support the x440. Currently the IBM summit chipset requires Red Hat Advanced server 2.1, a 2.4-ac kernel, or 2.4.20-pre6/7 with the final summit patch from IBM (which is pending merge)”**——summit 支持谱系权威裁定；Ramom Flores d'as Seixas（2002-11-27，USC）：P4 Mandrake 9.0 警告 + 显示器不唤醒（送修换显卡后复现、Windows 下消失、RedHat 8.0 无问题）三 OS 对照排障 + 4 附件清单——跨 OS 排障实录；Vladimir Ivanovic（2002-05-01）答 Gordon Gray（CUV4X-D BIOS 1004 双 Coppermine SMP 挂在 IO-APIC 测试后）：**“Upgrade your BIOS (at least to 1010) and set MPS to 1.1. These recommendations have been repeated many times and are easily found by searching the archives.”**——MPS 1.1+BIOS 1010 标准处方与档案检索文化；Alan Cox（2002-08-17）答 Mark Wigzell（A7M266D BIOS 1006 NIC 无 IRQ）：**“BIOS1004 seems to solve this problem on the A7M266D. I gave up on 1006 pretty fast”**——A7M266D BIOS 版本回退处方（与 p22 A7M266D 块呼应）；Erik Mouw（2006-10-25）答 Matt Brei（双 Athlon MP 1800+ 2.6.18.1）：开 SMP 后 nbd closed socket/LVM No volume groups found 启动失败——“Nope. Please supply more information. Boot log from SMP and non-SMP, kernel config, distribution, compiler version etc.”并指引 REPORTING-BUGS——SMP 启动失败分诊；Maxwell Spangler（2002-04-22）：Tyan S2466N Tiger MPX（AMD 768）双 Athlon 1800+ MP——SCSI CD 刻录 loss of streaming（HP 9600si+2940AU/BT948 同败、UP KT266A 板正常、Windows 2000 同败）——MPX 板 PCI 重负载流式丢失疑案；Randy Dunlap（2003-04-03）答 Pekka Hellén（IBM PC Server 330 PPro 200 RH7.3 只认 1 CPU 而 NT4 认 2）：MP 表只有 1 处理器条目，“Perhaps NT 4 knows about this BIOS/MP table as a problem and has a workaround for it”；求 Linux 侧 MP quirk 强制第二处理器——MP 表缺陷与 OS workaround 差异

**史料**：`1572496`、`1572508`、`1572514`、`1572518`、`1572522`、`1572524`、`1572525`、`1572529`、`1572534`、`1572535`

【Linux社区】**史料锚**：`<!-- ROW_MINE: linux-smp.messages.1572496 -->` `<!-- ROW_MINE: linux-smp.messages.1572508 -->` `<!-- ROW_MINE: linux-smp.messages.1572514 -->` `<!-- ROW_MINE: linux-smp.messages.1572518 -->` `<!-- ROW_MINE: linux-smp.messages.1572522 -->` `<!-- ROW_MINE: linux-smp.messages.1572524 -->` `<!-- ROW_MINE: linux-smp.messages.1572525 -->` `<!-- ROW_MINE: linux-smp.messages.1572529 -->` `<!-- ROW_MINE: linux-smp.messages.1572534 -->` `<!-- ROW_MINE: linux-smp.messages.1572535 -->`

**史观**：经验优先（总纲第 9 条——经验优先：以 x440 summit 支持谱系、A7M266D BIOS 回退与 MPS 1.1+BIOS 1010 处方为判据）；动手者创造历史（总纲第 10 条——动手者创造历史：处方出自维护者与长期用户的实机经验）
**辨析**：两处维护者口径（x440 需 RH AS 2.1/2.4-ac/带 summit 补丁内核；BIOS 1004 解 A7M266D）均为时点性处方，版本谱系会随时间失效；MPX 流式丢失疑案无结论。
**文献**：DSLXC-4477/4488/4493/4497/4501/4503/4504/4508/4512/4513（`linux-smp.messages.1572496` 等 10 封，2002-04-22 至 2006-10-25），全文见 `raw_source.raw_json`

## 16.5 【Linux社区】双核与 HT 语义、性能权衡

**要点**：Alan Cox（2003-04-01）答 David Gaya（IBM xSeries 345 单 CPU 检出 2）：“The newer CPU's have hyperthreading which makes each CPU appear as two”——HT 一句定义再现（与 p23 030 Hyatt 呼应）；Bill Davidsen（2006-04-24）答 Urs Thuermann：双核 vs 双 CPU——“The bad part is that the cores share a bus connection, the good part is that it appears that some IPC can be done on chip”；HT 处理器重线程任务“20-30% drop in clock time”疑内存带宽；求 955（双核+HT）实测——双核/HT 性能权衡第一手；Robert Hyatt（2005-09-18）答 Peter Fein（双路双核 x86-64 集群选型）：**“A dual-core is two separate processors, on a single NUMA node”**；AMD quad 875 双核=8 CPU“runs like a bat out of Egypt”；crafty 双核 2x nodes/s 而实际加速 1.7-1.8X 与双路单核 Opteron 相当；gcc 3.3 足够——双核语义与加速比第一手

**史料**：`1572507`、`1572509`、`1572533`

【Linux社区】**史料锚**：`<!-- ROW_MINE: linux-smp.messages.1572507 -->` `<!-- ROW_MINE: linux-smp.messages.1572509 -->` `<!-- ROW_MINE: linux-smp.messages.1572533 -->`

**史观**：经验优先（总纲第 9 条——经验优先：以 crafty 双核加速比 1.7-1.8X 与 20-30% 掉速观察为判据）；知识注定过时（总纲第 22 条——知识注定过时：“HT 使一 CPU 视作两个”的定义随双核/多核出现而须重述）
**辨析**：“双核=单 NUMA 节点上的两个独立处理器”为当事人个人表述，与厂商语义口径不完全一致；加速比数据限于 crafty 单一负载。
**文献**：DSLXC-4487/4489/4511（`linux-smp.messages.1572507`、`.1572509`、`.1572533`，2003-04-01 至 2006-04-24），全文见 `raw_source.raw_json`

## 16.6 【Linux社区】崩溃、驱动故障与 EBDA 死机（5 例）

**要点**：Maurice（2004-08-10）答 Vlasenko：2.6.6-1.435.2.3smp 内核 FA311 NIC IPv4 失效（DHCP 拿不到、静态地址 ping 不通 Destination Host Unreachable），非 SMP 内核同卡正常——SMP 内核 NIC 故障实录；Evan Stevens（2002-10-30，National Safty Associations）：IBM x360 4×Xeon RH7.3 2.4.18-3smp 数天 uptime 后 **kernel BUG at commit.c:535**（jbd journal_commit_transaction buffer_jdirty 断言，CPU4）；8 logical（HT sibling_map 配对）、IO-APIC #14（51 redirection entries）、EBDA 警告、TSC skew CPU#6 2 usecs FIXED——x360 大平台崩溃档案；Anton Cook（2003-06-11，澳洲）：双 Xeon 2.0（Intel SE7500CW）2.4.18 生产 web/db 服务器周级 hang——**Divide error:0000 in smp_local_timer_interrupt（__setup_APIC_LVTT(calibration_result/prof_counter[cpu])）Kernel panic: Aiee, killing interrupt handler**，rsync 备份高发，手抄 console dump——APIC 定时器除零 panic 一手记录；koprivam/Michal（2005-07-25，army.cz）：IBM Netfinity 5100 双 P RH9 EBDA MP table 警告 + “once a day, it simply dies... no response to anything”求补丁——EBDA 关联死机咨询（对照 p23 014 Cox“只关乎老 bootloader”）；Pedro Pla（2002-11-05）答 Doug Ledford：GDT/SCSI + 双 P3 SCB2 + Intel RAID——SMP 下 segfault/signal 11/mem_alloc:89 oops（非 SMP 正常）；memtest86 v3 无错而 v2.8 在 8 条 SIMM/两块主板报错存疑——SMP RAM 争议实证链

**史料**：`1572498`、`1572502`、`1572510`、`1572511`、`1572513`

【Linux社区】**史料锚**：`<!-- ROW_MINE: linux-smp.messages.1572498 -->` `<!-- ROW_MINE: linux-smp.messages.1572502 -->` `<!-- ROW_MINE: linux-smp.messages.1572510 -->` `<!-- ROW_MINE: linux-smp.messages.1572511 -->` `<!-- ROW_MINE: linux-smp.messages.1572513 -->`

**史观**：经验优先（总纲第 9 条——经验优先：以 commit.c:535 断言、smp_local_timer_interrupt 除零 panic 与 memtest 版本对照为判据）；没有必然性，只有偶然性（总纲第 5 条——没有必然性，只有偶然性：SMP 内核 NIC 失效与 EBDA 日死机均由具体平台偶然触发）
**辨析**：memtest86 v2.8 报错与 v3 无错的矛盾原文未解，本块仅登记不结论；EBDA 死机一例与 p23 014“只关乎老 bootloader”口径存在张力，两说并录。
**文献**：DSLXC-4479/4483/4490/4491/4492（`linux-smp.messages.1572498` 等 5 封，2002-10-30 至 2005-07-25），全文见 `raw_source.raw_json`

## 16.7 【Linux社区】调度、亲和性、报料规范化与文档

**要点**：Dimitri Puzin（2005-11-05）：**2.6.14 smp_affinity 写不回**（2.6.13.4 可写 1→2，2.6.14 echo 2 后仍读 1），CONFIG_IRQBALANCE y/n 无关，P4 HT，/proc/interrupts 全落 CPU0——亲和性接口回归实录（与 p22 2.6.15 案同族）；Con Kolivas（2006-04-01）答 Al Boldi：反对导出 sched.c tunables 到 procfs——“None of the current tunables have easily understandable heuristics”“exporting tunables that noone understands is not really helpful”“parts of the scheduler know about the default tuning values and they'd be broken by modifying them”并指出导出成本——调度器可调参数哲学；john.fioroni（2003-08-04）：双 P3 1000 RH7.2 启动 WARNING，问“What would you like me to mail to you?”——报料流程咨询样本；Earle Nietzel（2002-04-17）答 Dunlap：uruk.org MPS 链接失效 + TUM acpi 链接；引述 **Randy Dunlap《MultiProcessor Specification Support in Linux 2.4》（2002-04-15）全文**（Linux 支持 MPS 1.1/1.4 而非全部 1.4、经验表明 BIOS 配 1.1 通常最佳、扩展表条目跳过不用）——MPS 对比文档全文留档；randy_dunlap（2005-07-12）答 a.mintgen：“It's actually the kernel log info _above_ these lines that should be mailed”——报料方法学（要警告上方日志）；Robert Hyatt（2003-05-27）：RH9 双 2.8 Xeon HT 负载升高时鼠标/键入迟滞，“I once saw this in older SMP kernels, but Mingo did something to tune things to behave better. Has this been broken”——RH9 交互性回归咨询；Erik Mouw（2005-01-14）答 Tobias Kranz（德国 BKA）：转储缺内核版本号，“so it's unclear if this is already been fixed in recent kernels”——报料要素缺失的分诊反馈；Bill Davidsen（2007-10-18）答 Alan Cox（Bamakhrama 求 Flynn Taxonomy 原始论文扫描件）：Cox“Please don't ask on this list for people to abuse copyright law”；Davidsen“he is allowed a personal copy under 'fair use' doctrine”+ 美英版权法溯及力评论——列表版权文化切片

**史料**：`1572497`、`1572501`、`1572506`、`1572519`、`1572521`、`1572523`、`1572526`、`1572537`

【Linux社区】**史料锚**：`<!-- ROW_MINE: linux-smp.messages.1572497 -->` `<!-- ROW_MINE: linux-smp.messages.1572501 -->` `<!-- ROW_MINE: linux-smp.messages.1572506 -->` `<!-- ROW_MINE: linux-smp.messages.1572519 -->` `<!-- ROW_MINE: linux-smp.messages.1572521 -->` `<!-- ROW_MINE: linux-smp.messages.1572523 -->` `<!-- ROW_MINE: linux-smp.messages.1572526 -->` `<!-- ROW_MINE: linux-smp.messages.1572537 -->`

**史观**：经验优先（总纲第 9 条——经验优先：以 2.6.14 smp_affinity 写不回实测、MPS 对比文全文与“要警告上方日志”报料方法学为判据）；理论必须自反（总纲第 7 条——理论必须自反：列表版权文化的自我约束由当事人当场提出并争论）
**辨析**：反对导出调度器可调参数属维护者立场，非技术结论；版权“合理使用”一例为列表内法律观点交换，落书不得作为法律判断。
**文献**：DSLXC-4478/4482/4486/4498/4500/4502/4505/4515（`linux-smp.messages.1572497` 等 8 封，2002-04-17 至 2007-10-18），全文见 `raw_source.raw_json`

---
注：本文件由判定表程序化生成（16.1-16.7 共 7 块，覆盖 47/47 CAND，两遍计数核对通过）；要点逐字取自判定表“要点”列（主代理全读审读实录），史料锚与 CAND 一一对应，全文以 raw_source.raw_json 为准。
