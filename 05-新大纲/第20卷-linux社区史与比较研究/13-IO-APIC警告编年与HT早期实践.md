# 13 【Linux社区】IO-APIC警告编年与HT早期实践

> 对应页面：linux-smp p21（pk 1572338-1572387，2002-2005 为主，2021 讨论 3 封）
> 判定：48 CAND / 2 NV（019 纯客套、021 纯引文）
> 编号：DSLXC-4329..4376 | claim 已入库（48/48，dslinux_claims.duckdb）

## 13.1 【Linux社区】unexpected IO-APIC 警告编年与维护者定调

**要点**：Randy Dunlap（2003-12-09）回 Pieter Rabe：报 unexpected IO-APIC 的方法——“寄 /var/log/messages 全文（至少含全部 IO-APIC 相关行），整 boot log 更好；标识 Linux 内核版本号而非 RH9 版本号”；MOTD“Always include version info”——版本号纪律的维护者口径；Randy Dunlap（2002-10-21）回 Spuds：贴 patch（2.5.43 已寄、可应用于 2.4.18 带 offset）——IO_APIC_reg_00 结构拆出 LTS/delivery_type 位段、__reserved_0 纳入 UNEXPECTED 检查、printk 加 Delivery Type/LTS 行；“WARNING is no big deal”——unexpected 警告的代码级处置（2.4/2.5 演进）；Pete de Zwart（2003-02-15）：Siemens-Nixdorf Primergy 700 四路 PentiumPro 定制硬件——unexpected IO-APIC 报告附 dmesg；Fujitsu-Siemens Linux 支持页查无所获——冷门 4 路 PPro 平台存档；Randy Dunlap（2005-03-15）回 Farnam：RH AS3.0U4 2.4.21-27.0.2.ELsmp 双 Opteron 844——“多条消息已在 2.4 后期版修复、2.6 消除；纯 informational 不影响运行；来自内核已知有效 IO APIC 设备列表未常更新（故 2.6 干脆移除该消息）”；附 8 个 IO-APIC（#2 24 寄存器+3-8 各 4 寄存器）完整转储——Opteron 多 IO-APIC 拓扑与警告生命周期定论；Vincent M Caruso（2004-03-16）：RHEL WS3 + ASUS P4P800——按指示报告 unexpected IO-APIC（error_logs.doc 附件）；问临时/永久修法或支持时间线——企业用户视角的警告处理；Malcolm Langille（2002-09-16）：linux 7.1 双 Intel——“testing the IO-APIC 消息后测完 CPU0 就崩”求助——警告后即崩的极端样本；rhfreeman（2003-06-18）：Opteron 双路（Rackable C2000-7/Rioworks R3122 板）RH7.2 32 位——Cox 传闻后试 2.4.21-ac1 同样信息（更多细节）、noapic 即消失；IO APIC #3 转储（max redirection 0003）——Opteron 平台 2.4.21-ac 的 first hand 验证；R. Lemos（2002-11-29）：2.4.19 开 IO-APIC 后 dmesg 见 APIC error 行——附 .config 主动求所需信息“愿助内核开发”——报料协作姿态样本；Pino/gialuig（2004-02-09）：Debian 2.4.18-bf2.4 Athlon XP 2000+——boot.msg 全文（VIA 3177 IRQ router、Via IRQ fixup ×3、Unknown VIA SouthBridge）；“若在添乱抱歉可丢垃圾桶”——自嘲式报料样本；Earle R. Nietzel（2003-06-21）回 Ricky：Intel D865PERL + P4 2.4 800FSB HT——register #02 疑为坏寄存器（00178020 应更像 02000000）；HT 开 SMP 2 CPU 出现但 /proc/interrupts 全走 CPU0——“这类板子中断全去 CPU0，有人知道为什么吗”——865 系列 IO-APIC 行为存疑帖；Vitezslav T. Se'm（2004-09-02）：2.4.20-30.7.legacysmp——IO APIC #13（version 0020、PRQ 1）register #02=00178020 触发 unexpected 警告——#02 寄存器残值样本（与 022 同型）；Brendan Davies（2003-05-19）：代转 crowsdev boot 日志——unexpected IO-APIC+TSC 同步 passed+mtrr 变量不一致（BIOS 未在所有 CPU 设置）——转发报料样本；Daniel Blueman（2003-07-31）：2.4.22-pre9 Gentoo P4 Xeon 2.0（SiS IRQ router 962/963 MuTIOL）——应 Cox 要求补 debug 全文：IO APIC #2 version 0014+PRQ 1+arbitration 02、全 IRQ redirection 表、PCI->APIC IRQ transform 列表——Cox 排障流程（要 dmesg>logfile）的配合样本；james.oden（2002-08-14）：E7500 芯片组系统 messages log 见警告——问“支持此 E7500 系统需要什么信息”——E7500 芯片组报料样本（主动列出所属芯片组）；Earle Nietzel（2005-04-26）回 Boulware（Dell 4700）：unexpected IO-APIC“不代表有问题、纯 informational”并给出 rhinobox.org/linux/IOAPIC.html 说明页；ide2: unexpected interrupt 才是真问题——根因 PCI_IDE: unknown IDE controller VID=8086 DID=266f（ICH6 未被 2.4 识别）建议 2.6 内核；lspci -vv 识别法——警告语义澄清+2.4/2.6 驱动代差的社区解答；Sven Wagner（2004-04-30）：Debian 2.4.18-1-k7——IO APIC #2（version 0003、PRQ 1）全 IRQ redirection 表寄存——主题即内核版本串的报料样本；Alan Cox（2003-02-11）回 Hesen：RH Advanced 2.1（2.4.9-e.3smp）警告——“古老内核不认识大多数现代 APIC，不该是问题”——企业内核警告定调；Peter Ruskin（2003-03-15）：IO APIC #2 version 0003 全 IRQ redirection 表+完整 boot log（VIA vt8235/PDC20276/6 块 Maxtor/AGP KT400/EHCI USB2.0/i2c 传感器阵列/acpi=off 命令行）——信息最全的报料样本之一；Karl Weigel（2002-12-11）：升 2.4.20 后分析日志发现提示——boot.msg 节选（IO APIC #2 version 0002）寄报；“看不出这 APIC 对我有任何问题”——预防性报料样本；Werner Schmidt（2002-07-17）：2.4.19-rc2 MSI KT3 ULTRA（VIA KT333+VT8233A）——boot.msg 全文（VT5440B MP 表、Athlon XP 1900+、Advanced speculative caching 禁用、IO APIC version 0002 触发警告、Via IRQ fixup）——VIA 平台警告存档；Lance Davis（2003-10-16）：RH kernel-smp-2.4.20-20.9 + Supermicro P4SCE——IO APIC #2 version 0020 register #02=00178020 触发 unexpected——#02 寄存器残值第三例（与 022/024 同型、E7520 平台）；ferdie（2003-03-25）：ccserver——IO APIC #8（version 0020）+TIMER pin1=-1 pin2=-1 经 8259A 失败后 Virtual Wire IRQ 成功——timer setup 降级路径的实况样本；Giulio Bottazzi（2002-05-03）：SuSE 2.4.10-4GB Athlon+enableapic——VIA VT5440B MP 表、IO APIC #2 version 0011 触发警告、全 IRQ redirection 表；enableapic 命令行参数使用样本

**史料**：`1572338`、`1572339`、`1572344`、`1572345`、`1572346`、`1572347`、`1572351`、`1572352`、`1572355`、`1572359`、`1572361`、`1572362`、`1572369`、`1572371`、`1572373`、`1572374`、`1572375`、`1572379`、`1572381`、`1572383`、`1572384`、`1572386`、`1572354`

**史料锚**：`<!-- ROW_MINE: linux-smp.messages.1572338 -->` `<!-- ROW_MINE: linux-smp.messages.1572339 -->` `<!-- ROW_MINE: linux-smp.messages.1572344 -->` `<!-- ROW_MINE: linux-smp.messages.1572345 -->` `<!-- ROW_MINE: linux-smp.messages.1572346 -->` `<!-- ROW_MINE: linux-smp.messages.1572347 -->` `<!-- ROW_MINE: linux-smp.messages.1572351 -->` `<!-- ROW_MINE: linux-smp.messages.1572352 -->` `<!-- ROW_MINE: linux-smp.messages.1572355 -->` `<!-- ROW_MINE: linux-smp.messages.1572359 -->` `<!-- ROW_MINE: linux-smp.messages.1572361 -->` `<!-- ROW_MINE: linux-smp.messages.1572362 -->` `<!-- ROW_MINE: linux-smp.messages.1572369 -->` `<!-- ROW_MINE: linux-smp.messages.1572371 -->` `<!-- ROW_MINE: linux-smp.messages.1572373 -->` `<!-- ROW_MINE: linux-smp.messages.1572374 -->` `<!-- ROW_MINE: linux-smp.messages.1572375 -->` `<!-- ROW_MINE: linux-smp.messages.1572379 -->` `<!-- ROW_MINE: linux-smp.messages.1572381 -->` `<!-- ROW_MINE: linux-smp.messages.1572383 -->` `<!-- ROW_MINE: linux-smp.messages.1572384 -->` `<!-- ROW_MINE: linux-smp.messages.1572386 -->` `<!-- ROW_MINE: linux-smp.messages.1572354 -->`
- **史观**：动手者叙事（总纲 10：报料方法、代码处置与生命周期定论均由 Randy Dunlap 等维护者一手给出）；经验优先（总纲 9：以 /var/log/messages 全文、内核版本号与 IO-APIC 寄存器转储为判据）；知识注定过时（总纲 22：2.6 干脆移除该消息，警告本身被时间淘汰）
- **辨析**：“WARNING is no big deal / 纯 informational”系维护者口径，不等于该警告所指向的 硬件或固件问题不存在；本块 23 封以报料与定调为主，多数未闭环，落书不得据报料密度推断 unexpected IO-APIC 的实际故障率。
- **文献**：DSLXC-4329/4330/4335/4336/4337/4338/4342/4343/4346/4348/4350/4351/4358/4360/4362/4363/4364/4368/4370/4372/4373/4375/4345（`linux-smp.messages.1572338`、`.1572339`、`.1572344`、`.1572345`、`.1572346`、`.1572347`、`.1572351`、`.1572352`、`.1572355`、`.1572359`、`.1572361`、`.1572362`、`.1572369`、`.1572371`、`.1572373`、`.1572374`、`.1572375`、`.1572379`、`.1572381`、`.1572383`、`.1572384`、`.1572386`、`.1572354`，2002-09 至 2005-03），全文见 `raw_source.raw_json`

## 13.2 【Linux社区】5.12 热敏中断与 soft lockup 排查（2021）

**要点**：Borislav Petkov（2021-05-20）回 Feeney：X86_THERMAL_VECTOR 禁用后仍锁死——“不可能是我的 patch 引起”；观察“*有时* CPU0 不响应 TLB flush IPI，很诡异”；猜 APIC_LVTTHMR 只在 BSP 读的问题；两条试验：①5.12 加 idle=nomwait ②lvtthmr_init 读取后移补丁（print 每核值看锁死时数值）——5.12 锁死排查的下一步设计；James Feeney（2021-05-20）：Arch 5.12-arch1 基本无补丁（仅 unprivileged_userns_clone+版本号）；X86_THERMAL_VECTOR 禁用后 No joy（同锁死+神秘延迟）；acpi_enforce_resources=lax 是访问 RAM SPD EEPROM 所需（eeprom 模块被 at24 取代）；5.11 同有 therm_throt.c 困惑——回归排查的环境澄清；James Feeney（2021-05-22）：10 次 boot 无 soft lockup 但 boot4 全启动有 73 秒神秘延迟（adding swap 后 Bluetooth 前）；lvtthmr 打点揭示 CPU0 lvtthmr_init=0x10200→“Thermal monitoring handled by SMI”（HP BIOS SMI 接管）；上一 patch 十次 boot CPU1 恒 0x10000 唯一差异是 apic_read 位置；引 _OSC native thermal 处理 commit（Skylake HWP 冻结根因=HWP 中断进 BIOS）与 2007 AMD Thermal Interrupt Support（lwn 262469）；pr_info 显示 mcheck_intel_therm_init() 原在 0.171s paravirtualized 行后运行、现 intel_init_thermal() 在 0.93-1.25s 运行——时序差关键证据，5 boot 中 3 种结局（正常/ACPI 表挂/rootfs 解包挂）——5.12 热敏中断时序回归的实证汇编

**史料**：`1572340`、`1572341`、`1572353`

**史料锚**：`<!-- ROW_MINE: linux-smp.messages.1572340 -->` `<!-- ROW_MINE: linux-smp.messages.1572341 -->` `<!-- ROW_MINE: linux-smp.messages.1572353 -->`
- **史观**：动手者叙事（总纲 10：打点试验与 CPU0 不响应 IPI 的观察均由当事开发者自述）；经验优先（总纲 9：以 lvtthmr_init 打点值、intel_init_thermal() 运行时刻与 10 次 boot 统计为判据）；偶然性优先（总纲 5：5 boot 中 3 种结局，时序差由 HP BIOS 以 SMI 接管热监控这一外因造成）
- **辨析**：本块系 5.12 热敏中断回归的排查过程记录，2021-05-20/22 两封均为阶段结论（“不可能是我的 patch 引起”属当事人判断，非定论）；intel_init_thermal() 由 0.171s 后移至 0.93-1.25s 的时序差是实证，但根因归责须另据后续主线结论。
- **文献**：DSLXC-4331/4332/4344（`linux-smp.messages.1572340`、`.1572341`、`.1572353`，2021-05-20 至 05-22），全文见 `raw_source.raw_json`

## 13.3 【Linux社区】SMP 硬件兼容与 BIOS 选项实战

**要点**：Alan Cox（2002-12-08）回 Gerald：APM 未为 SMP 系统定义；2.4.20-ac 有 A7M266-D 原生电源管理模块（idle 省 90W）——SMP/PM 关系与 ac 补丁树功能；Ivanovic（2004-04-22）回 Bobby Hitt：ASUS CUV4X-DLS 双核三年经验——grub.conf 全文（2.4.22-1.2179.nptlsmp + ide2/ide3 手工指定）；“Linux SMP 能跑须 BIOS 关 MPS 1.4 支持+关自动 IDE 检测再开 Primary IDE 通道”——CUV4X 系列的第二份配置实录；Bobby Hitt（2004-04-22）SMP Woes 全文：ASUS CUV4XD 双核 W2K 两年正常→Linux SMP 内核启动锁死（Total of 2 processors activated 后）；Cox 建议 noapic pci=usepirqmask 无效；自解：BIOS 关“MPS 1/4 Support”即好；连带问题：raidstart 报 cannot determine md version: 6；2.4.26 开 SMP+vga=791 黑屏锁死、关 SMP 编译反报 num_cpus 处处——只能存 .config 清目录重装源码树再编——MPS 1.4 定调+内核构建损坏样本；Alan Cox（2002-08-12）回 Malkowski：IBM xSeries 360 4×Xeon 2.2.21 行为如中断完全不发生——“可 noapic 启动；注意 2.2 内核不支持 PIV SMP/HT/PIV APIC IRQ 负载平衡等，不工作不奇怪”——2.2 时代支持边界定调；Steve Keith（2002-06-28）：CUV4X-D 双 PIII RH7.2 2.4.7-10 SMP 失败——自省帖：LILO `append="noapic"` 与 GRUB kernel 行尾 `noapic` 的完整配置实录（勿忘重跑 lilo）；建议升 BIOS+关 MPS 1.4+noapic——noapic 配置文档化样本（042 Ivanovic 引用的原始帖）；Eric Malkowski（2002-08-22）回 Nerijus：IBM X220 RH 2.4.18-5/2.4.19 SMP 起不来（aic7xxx 探不到盘=无中断）——建议 noapic（中断全走第一处理器、进程仍用全部核）+console=ttyS0,57600 串口抓 boot 消息再寄列表——串口调试法在 SMP 排障中的实操指南；Sanjay Londhe（2002-08-12）答 Cox 问：CUV4XDLS（Award BIOS v6.0/ASUS ACPI 1014/Delta）+双 PIII 1G 133FSB——Enterprise/SMP 选项都不启动的硬件清单——CUV4X 系列第三份故障记录；Iago Sineiro（2002-04-08）：RH7.2 smp 2.4.10 + ASUSTEK CUV4X-D 双 PIII 1G——Booting processor 1/0 后 unexpected IO-APIC 警告全文（含 SCSI/Ethernet 配置清单）——CUV4X 系列第四份记录；Alan Cox（2002-08-11）回 Grødem：A7M266-D 双 Athlon——“板档要求双 CPU 用 400W PSU、自己带盘阵需 550W”；性能上双 Athlon 已输 2.4GHz PIV 但稳定性优先；“PIV 板才玩两周、太早下可靠性结论”——SMP 选机功率与可靠性评估的维护者口径；Richard B. Johnson（2003-06-02）回 Dresser：P4 2.66 Xeon“本该支持 HT，不支持则 CPU 或主板坏，我赌主板”——HT 硬件排障的口语化判断（016 同日同 thread 前半）；Niall Dalton（2002-04-26）：Dell PW530 双 2.2 Xeon HT + i860——BIOS 禁 HT 双物理核性能优秀；开 HT 后 4 逻辑核 sibling map 正常但性能暴跌（boot 8-9 分钟、拖窗 20 秒、X 不稳崩两次）；bad pte 消息与 RSDP 位置警告；问该用 2.5 内核还是 affinity/调度/抢占补丁——SMT 初期性能悬崖的第一手记录（作者为 SMT 编译优化实验者）

**史料**：`1572342`、`1572343`、`1572350`、`1572360`、`1572363`、`1572364`、`1572366`、`1572367`、`1572370`、`1572376`、`1572385`

**史料锚**：`<!-- ROW_MINE: linux-smp.messages.1572342 -->` `<!-- ROW_MINE: linux-smp.messages.1572343 -->` `<!-- ROW_MINE: linux-smp.messages.1572350 -->` `<!-- ROW_MINE: linux-smp.messages.1572360 -->` `<!-- ROW_MINE: linux-smp.messages.1572363 -->` `<!-- ROW_MINE: linux-smp.messages.1572364 -->` `<!-- ROW_MINE: linux-smp.messages.1572366 -->` `<!-- ROW_MINE: linux-smp.messages.1572367 -->` `<!-- ROW_MINE: linux-smp.messages.1572370 -->` `<!-- ROW_MINE: linux-smp.messages.1572376 -->` `<!-- ROW_MINE: linux-smp.messages.1572385 -->`
- **史观**：动手者叙事（总纲 10：BIOS 选项与配置实录均由装机者与维护者逐例给出）；经验优先（总纲 9：以 grub.conf 全文、MPS 1.4 开关实测与 boot 日志为判据）；偶然性优先（总纲 5：同型号主板成败取决于 BIOS 版本与选项组合，非设计必然）
- **辨析**：本块多例的结论是“BIOS 关 MPS 1.4 支持即好”，属固件配置层面的规避而非内核修复；Bobby Hitt 自解的“内核构建损坏”系反复编译导致，与 SMP 缺陷须分开登记；Niall Dalton 的 SMT 性能悬崖记录为第一手实测，不得径推为 HT 技术本身不可用。
- **文献**：DSLXC-4333/4334/4341/4349/4352/4353/4355/4356/4359/4365/4374（`linux-smp.messages.1572342`、`.1572343`、`.1572350`、`.1572360`、`.1572363`、`.1572364`、`.1572366`、`.1572367`、`.1572370`、`.1572376`、`.1572385`，2002-04 至 2004-04），全文见 `raw_source.raw_json`

## 13.4 【Linux社区】锁死、崩溃与深层故障

**要点**：Thomas Porter（2002-08-19）：双 Xeon 2.0 Compaq EVO W6000（I860 板）RH7.3 6-48 小时锁死——HT BIOS 开但内核报禁用（boot 报 4 处理器而 /proc/cpuinfo 只 2）；X 冻死 SSH 可入 killall -9 X 无效；锁死前 syslog ---MARK--- 停止+系统钟慢 2 小时（锁死前 2-6 小时开始）；RPM -Va 校验错=磁盘损坏（重装两次+Win2K 重映像复现）；Compaq BIOS 无 OS 相关选项——I860+HT 早期平台的多重故障实录；Rudy Klinksiek（2003-02-20）：Synergy Quad/Dual G4 Altivec PPC beowulf 集群——SMP 内核客户端 boot 见 Illegal instruction 陷阱（syslogd/crond/sshd 等守护启动失败、rsh/rlogin 同）UP 内核无恙、SMP 服务器正常； suspect 内核/NFS 的 SMP 问题——x86 页表释放与 TLB flush 顺序修复（Sunil Saxena）未达 ppc；2.5.16 起才修——问如何把 2.5.60 的 page/tlb shutdown 修法移植回 2.4.19（VMS/Solaris 驱动开发者背景）——PPC SMP TLB 一致性的用户移植计划；Hernan Coronel（2002-06-05）：IBM Netfinity 5000 SQL 中重载时 NMI received for unknown reason 34→Dazed and confused→重启；boot 另见 EBDA 警告；IBM HW Support 断言非硬件问题——NMI 34 与 EBDA 警告并存的生产故障样本；Steve Wanzong（2002-10-10）：Dell PW530 双 Xeon 2.4 RH7.2 2.4.7-10smp 崩溃——禁 CDROM 电源后频率降低仍发生；messages 仅两条 unexpected IO-APIC——崩溃与警告并存的求助样本；Mike Bubel（2002-07-16，IBM GPFS 开发）：SuSE 2.4.18.64G-SMP 双路 Netfinity 跑 GPFS——/proc/pid/statm 部分任务读不出致 ps/top 挂死，>800M 内存才现；lkcd 强制 dump 栈：schedule→kmap_high→unprotectKernelMemory→error_code；boot 亮 EBDA 警告——GPFS/kmap_high/EBDA 三者交错的深层故障报告（IBM 内部开发者直接来函）

**史料**：`1572349`、`1572368`、`1572378`、`1572382`、`1572387`

**史料锚**：`<!-- ROW_MINE: linux-smp.messages.1572349 -->` `<!-- ROW_MINE: linux-smp.messages.1572368 -->` `<!-- ROW_MINE: linux-smp.messages.1572378 -->` `<!-- ROW_MINE: linux-smp.messages.1572382 -->` `<!-- ROW_MINE: linux-smp.messages.1572387 -->`
- **史观**：经验优先（总纲 9：以 NMI 原因码、lkcd 强制 dump 栈与 RPM -Va 校验结果为判据）；动手者叙事（总纲 10：深层故障由装机者与 IBM 内部开发者一手报告）；知识注定过时（总纲 22：PPC SMP TLB 修法仅在 2.5.16 起生效，2.4 线移植计划未成）
- **辨析**：本块五例均为多重症状并存（NMI 34 与 EBDA 警告、崩溃与 unexpected IO-APIC、GPFS 与 kmap_high 与 EBDA 三者交错），不得把并存症状径判为同一根因；Rudy Klinksiek 的 PPC 移植计划在本线程未见落地结论。
- **文献**：DSLXC-4340/4357/4367/4371/4376（`linux-smp.messages.1572349`、`.1572368`、`.1572378`、`.1572382`、`.1572387`，2002-06 至 2003-02），全文见 `raw_source.raw_json`

## 13.5 【Linux社区】调度、绑定与 SMP 概念问答

**要点**：Robert M. Hyatt（2002-07-23）回 VanCampen：双 PIII 跑 3 个 SETI 反而略快——SETI 有 I/O、第三份意味着 3 进程抢 2 处理器、一个堵 I/O 仍有两个就绪；自己 4 路机 make -j 16 编译更快（让 CPU 更忙）——负载超核数策略的实践解释（Crafty 作者/CPU 绑定话题）；Shreyas Kejariwal（2003-06-18）SMP 五问：①ASMP 系统还有吗②如何把 App1 线程钉在 P1、App2 钉在 P2（处理器绑定）③处理器间如何互访内存/地址空间④除 RR/FIFO 还有何调度策略⑤L2 共享缓存是否须买共享缓存板——SMP 入门概念问答（2003）；Gaspar Bakos（2004-01-16）确认：Mark Hahn 诊断“BIOS 给 CPU 编号不连续”——重编内核 MAX_NR_CPUS=8 即好——非连续 APIC ID 与内核最大 CPU 数配置的经典案例（结案帖）

**史料**：`1572357`、`1572365`、`1572380`

**史料锚**：`<!-- ROW_MINE: linux-smp.messages.1572357 -->` `<!-- ROW_MINE: linux-smp.messages.1572365 -->` `<!-- ROW_MINE: linux-smp.messages.1572380 -->`
- **史观**：经验优先（总纲 9：以 SETI 与 make -j 的实测、BIOS CPU 编号与 MAX_NR_CPUS 配置为判据）；动手者叙事（总纲 10：负载超核数策略由当事人以自身机器实测解释）；多方平等（总纲 8：概念问答与结案确认并列登记，不因提问者入门而降低收录）
- **辨析**：Shreyas Kejariwal 的五问属 2003 年的入门认知，其中“是否须买共享缓存板”等问法已过时，只作时代切片登记；Gaspar Bakos 的结案（重编 MAX_NR_CPUS=8）系配置修正，非内核缺陷修复。
- **文献**：DSLXC-4347/4354/4369（`linux-smp.messages.1572357`、`.1572365`、`.1572380`，2002-07 至 2004-01），全文见 `raw_source.raw_json`

## 13.6 【Linux社区】中断触发模式与 APIC error

**要点**：Ed ZCane（2003-06-19）：SMC9462SX 千兆卡 2.4 SMP 下 IO-APIC-EDGE 0 计数不工作（UP 内核 XT-PIC >0 正常）——卡手册要求 level triggered；问如何把 IO-APIC-EDGE 改配 IO-APIC-LEVEL——SMP 中断触发模式与驱动需求的错配；Tabris（2002-07-29）：ABIT KX7-333（VIA KT333）BIOS 开 APIC 即 APIC Error CPU0: 02(02)，2.4.19-rc1-mjc1——补内核版本号的追加帖——UP 平台 APIC error 样本

**史料**：`1572348`、`1572377`

**史料锚**：`<!-- ROW_MINE: linux-smp.messages.1572348 -->` `<!-- ROW_MINE: linux-smp.messages.1572377 -->`
- **史观**：经验优先（总纲 9：以 IO-APIC-EDGE 计数、APIC Error 代码与内核版本号为判据）；动手者叙事（总纲 10：触发模式错配与追加帖均由当事人一手记录）；偶然性优先（总纲 5：触发模式由卡手册要求与主板默认配置的偶然错配决定）
- **辨析**：Ed ZCane 的 IO-APIC-EDGE 计数为 0 是否即为故障，本线程未获维护者定论，只登记为错配现象；Tabris 的 APIC Error CPU0: 02(02) 属 UP 平台样本，不得与 SMP 场景的 APIC error 混叙。
- **文献**：DSLXC-4339/4366（`linux-smp.messages.1572348`、`.1572377`，2002-07 至 2003-06），全文见 `raw_source.raw_json`

## 13.7 【Linux社区】文档维护

**要点**：Lists (lst)（2002-07-12）回 Tumenbayar：SMP HOWTO v1.4 发布——PSET patch 链接已断（isunix.it.ilstu.edu 连接超时）——SMP HOWTO 文档维护与链接失效的早期反馈

**史料**：`1572372`

**史料锚**：`<!-- ROW_MINE: linux-smp.messages.1572372 -->`
- **史观**：动手者叙事（总纲 10：文档维护反馈由 SMP HOWTO 读者一手给出）；知识注定过时（总纲 22：SMP HOWTO v1.4 的 PSET patch 链接失效，文档随工具链变迁而失效）
- **辨析**：本块仅一封链接失效反馈，属文档维护类杂讯，不构成技术史节点；登记以保留“文档—链接”腐化的早期样本，不得据以评价 SMP HOWTO 的内容质量。
- **文献**：DSLXC-4361（`linux-smp.messages.1572372`，2002-07-12），全文见 `raw_source.raw_json`

---
注：本文件由判定表程序化生成（13.1-13.7 共 7 块，覆盖 48/48 CAND）；要点逐字取自判定表“要点”列（审读实录），史料锚与 CAND 一一对应。
