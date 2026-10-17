# 14 【Linux社区】IO-APIC触发全景与警告治理

> 对应页面：linux-smp p22（pk 1572388-1572437，2002-2008 为主，含垃圾邮件 2 封 NV + 1 封客套）
> 判定：47 CAND / 3 NV（004/005 附件垃圾、031 征婚 spam）
> 编号：DSLXC-4377..4423 | claim 已入库（47/47，dslinux_claims.duckdb）

## 14.1 【Linux社区】unexpected IO-APIC 触发全景（21 例）

**要点**：MONARI/HP（2002-05-08）：hp x4000（HP_WOMBAT OEM）双 Xeon 2.2 + ATI FireGL2——双 IO-APIC #2/#3（version 32）、register #00=02008000 连触三条警告；问“是否致命、有无 patch”；附完整 dmesg（3GB 内存/2174MB HIGHMEM/sym53c1010-66 双通道/eepro100+PRO/1000）——HP 工作站平台警告样本；Thomas Björnell（2002-10-24）：2.4.20-pre11——IO APIC #2 version 0002+PRQ 1 触发警告、全 IRQ redirection 表；“希望我做对了”附 dmesg 节选愿补信息——标准报料样本；Sakari Aaltonen（2003-01-12）：2.4.20 + VIA KT400 + AthlonXP 1400——IO APIC #2 version 0003+PRQ 1 触发警告、全 IRQ redirection 表——KT400 平台警告存档；Travis Pinney（2003-08-07）：双 Xeon 2.0 五 IO-APIC（#2/#3/#4/#5/#8 全 version 0020）转储；PDC20270“too many IDE interfaces, no room in table”+Promise FastTrak RAID1+e1000 双网——五 IO-APIC 拓扑与 IDE 控制器表溢出并存样本；david@lownoisefloor（2003-02-06）：双 Xeon 2.8 7501 板（P4DMS）2.4.18-19.8.0smp（自称 Hyper-Thread Safe Kernel）——五 IO-APIC（#2/#3/#4/#5/#8）+4 处理器 sibling map 转储；问“IO APIC error 02 需解决还是可安全忽略”——HT-safe 内核标签与警告并存的求证；Bill Baker（2005-07-12）：Dell PowerEdge 700 内核升级 2.4.20-8→2.4.20-43.9.legacy（fedoralegacy）——register #02=00178020 触发警告；e1000 需自编通用驱动——legacy 内核升级后警告的报料；Steve Ripps（2003-01-30）：Gigabyte GA-7VAX + 2.4.20-ac2 Athlon XP 1800+——全 log 含三组 md RAID1 重建（not clean→background reconstruction、共享物理盘延迟 resync）+VIA vt8235+PnPBIOS 16 节点——警告与 RAID1 自愈并存的完整样本；Vincent M Caruso（2004-03-18）：ASUS P4P800-VM-UAY + P4 2.8 800FSB RHEL 2.4.21-9.0.1——“系统因这些冲突非常慢、必须修好”；问 Red Hat 与 linux-smp 是否同门、何时回复、有无建议内核——企业用户升级路径（直发 Red Hat 抄送列表）；Alex Orlov（2006-04-26）：oops 报告——ACPI ut_allocate 失败（\_SB_._INI Method execution failed）+ unexpected IO-APIC 同现——ACPI _INI 失败与警告并存的日志样本；Chris Kant（2004-08-06）：2.4.9-e.48smp RH7.2 双 P4 Xeon 2.8 HT（sibling map 0=1）——bad pte init.c:148、3ware 控制器 500GB+3×1.5TB（sdb/c/d 扇区数溢出报 -346513 MB）、unknown IDE controller DID=24db（ICH5 未识别）——企业备份服务器多重异常的全 log 存档（含 2TB 盘 32 位溢出现象）；Martin Slovacek（2005-01-25）：HP DL585R01 4×Opteron 2.4 + 2.4.21-27.ELsmp——问“是否该退回旧内核”欲跑 Oracle 9.2——Opteron 四路生产环境警告咨询；Ricky McInnes（2003-06-08）：看 /var/log/messages 发现启动日志“An unexpected IO-APIC was found…（release <3 months 请报）”，2.4.21 CK patchset P4 2.4GHz；抄录启动段（总 2 处理器激活/cpu_sibling_map/IO-APIC 使能/APIC timer 校时）铁证——“新版警告措辞”样本（含 IEC 199MHz 总线）；Toni Cerdà（2002-12-06）：debian 2.4.18 p4@2.8 d850mevr——dmesg register #00: 02008000 + 警告、register #01: 00178020 无正文——玉不琢不成器 D850 补充样本；Lanier, John（2003-05-21，HP）：Compaq Deskpro EN PIII + RH 7.1——messages 文件中连续两条 unexpected IO-APIC 警告，按提示抄送（自述 no problem 仅按提示报）——“无故障报料”类样本；Andrea Fedeli（2003-04-21）：Mandrake 9.1 自带 2.4.21-0.13mdk P4 2.4GHz——按 syslog 提示发报；cc 发版者 flepied@mandrakesoft；称“还需要啥就问，可打包寄送”——发行版默认内核警告转报；Christian Stapfer（2002-07-03）：2GHz P4 512KB/1GB、Giga-Byte GA-8IEX、SuSE 7.3 新装——boot.msg 有提示，附 boot.msg 报料（北欧瑞士 UZH 用户）；Dwaine Garden（2003-06-01）：Redhat 9.0 2.4.20-8 启动报 unexpected IO-APIC，附 boot 日志；Michael Frank（2003-07-23）：P4 **UP（单处理器）主板** 2.4.22-pre7 也报 unexpected IO-APIC 而 2.6.0-test 无此消息——UP 机器触发警告 + 2.4/2.6 行为对照（附 lspci、双 dmesg）；Agustín Ciciliani（2004-09-10）：Intel D865PERL P4 2.26 debian 2.4.19 双 SATA WD800 + 8139C——只问“是错还是照用”（D865PERL 的例行咨询）；Jordan Strassemeyer（2003-01-30）：MS-6533/G/EG（v1.X）MicroATX P4 2.53 + Realtek 8029(AS) 网卡、2.4.18-64GB-SMP——register #01 0017**8014**（version 16）、警告触发；ping 即 eth0 Tx timed out 循环丢失——IO-APIC version 014 + 网卡中断丢失的推理链（附完整 boot.log，SiS 芯片）；Bernd Schubert（2003-12-10）答 Dunlap：确认 i386（ia32）内建——x86_64 才期望 max redirection entries=03 的裁定适用到自己身上——用 i386/x86_64 区分“expected vs not”的方法论（成果）

**史料**：`1572388`、`1572389`、`1572393`、`1572395`、`1572397`、`1572398`、`1572399`、`1572403`、`1572405`、`1572406`、`1572407`、`1572413`、`1572414`、`1572416`、`1572417`、`1572420`、`1572422`、`1572426`、`1572429`、`1572433`、`1572434`

【Linux社区】**史料锚**：`<!-- ROW_MINE: linux-smp.messages.1572388 -->` `<!-- ROW_MINE: linux-smp.messages.1572389 -->` `<!-- ROW_MINE: linux-smp.messages.1572393 -->` `<!-- ROW_MINE: linux-smp.messages.1572395 -->` `<!-- ROW_MINE: linux-smp.messages.1572397 -->` `<!-- ROW_MINE: linux-smp.messages.1572398 -->` `<!-- ROW_MINE: linux-smp.messages.1572399 -->` `<!-- ROW_MINE: linux-smp.messages.1572403 -->` `<!-- ROW_MINE: linux-smp.messages.1572405 -->` `<!-- ROW_MINE: linux-smp.messages.1572406 -->` `<!-- ROW_MINE: linux-smp.messages.1572407 -->` `<!-- ROW_MINE: linux-smp.messages.1572413 -->` `<!-- ROW_MINE: linux-smp.messages.1572414 -->` `<!-- ROW_MINE: linux-smp.messages.1572416 -->` `<!-- ROW_MINE: linux-smp.messages.1572417 -->` `<!-- ROW_MINE: linux-smp.messages.1572420 -->` `<!-- ROW_MINE: linux-smp.messages.1572422 -->` `<!-- ROW_MINE: linux-smp.messages.1572426 -->` `<!-- ROW_MINE: linux-smp.messages.1572429 -->` `<!-- ROW_MINE: linux-smp.messages.1572433 -->` `<!-- ROW_MINE: linux-smp.messages.1572434 -->`

**史观**：经验优先（总纲第 9 条——经验优先：以 21 例用户 dmesg 与寄存器转储为判据）；动手者创造历史（总纲第 10 条——动手者创造历史：报料者自述机型、固件与转储构成史料本体）；本体论上各方平等（总纲第 8 条——本体论上各方平等：HP 工作站、KT400 家用板、五 IO-APIC 服务器与 IDE 表溢出样本并置）
**辨析**：本块 21 例均为用户单方报料，除少数维护者回复外多无官方结论；机型与寄存器值可反查 dmesg 原文，但“是否致命”的判断不在本层给出。本页 3 封 NV（004/005 附件垃圾、031 征婚 spam）未入块。
**文献**：DSLXC-4377/4378/4380/4382/4384/4385/4386/4390/4392/4393/4394/4400/4401/4403/4404/4406/4408/4412/4415/4419/4420（`linux-smp.messages.1572388` 等 21 封，2002-05-08 至 2006-04-26），全文见 `raw_source.raw_json`

## 14.2 【Linux社区】SMP 硬件兼容与 BIOS 选项实战

**要点**：C. Henry（2002-11-30）续 enable SMP：双内核已装、只有 linux-up 可用（SMP 内核起不来）、/proc/cpuinfo 只 1 CPU；引答者步骤（uname -v 看 SMP 标记/rpm -qa grep kernel 看内核包）——SMP 内核不启动问题的对话存档；E. Robert Bogusta（2002-06-18）回 hamhey：CUV4X-D+Celeron PIII 800（注：原文如此）BIOS 10.14→10.10→1.14 折腾无果——triage 反问“是不能启动运行、还是只收到警告？”——警告语义分诊的标准问题；Bill Szkotnicki（2002-11-07）：科研服务器采购——Intel SC450NX 4×Xeon 成功经验；问 Linux SMP 能否跑 Itanium 2（SR870BN4 平台）与替代推荐——IA64 迁移期的选型问询；Eli（2003-02-09）：双 P4 Xeon SE7500CW2 2.4.20+iptables 补丁——PAE 开（HIGHMEM 64GB）时启动冻结+键盘怪错；限 4GB（PAE 关）即正常；内核认 4 CPU（HT）实际 2 颗；机器托管未见 BIOS——PAE 不稳与 HT CPU 计数双记录；Christian HOFFMANN（2002-04-14）：Asus A7M266D（760 MPX）+ 双 Athlon MP1900+ 于 Gentoo 2.4.18 SMP-XFS 跑满一个月一切正常——A7M266D/760MPX 的首份正式“running fine”实证（回 Emmanuel 的征集帖，配置清单完整）；Robert White（2003-06-03）：RE: Hyper-threading——美国消费者维权长文（FTC 投诉、Visa 拒付三步骤、留凭证），起因转贴 Richard B. Johnson 被欺诈购“Hyper-thread”板（标称千兆口未焊、$275+$635 不退款）；HT 时代初期受骗案例与维权路线图（附于 linux-smp 列表）；Frank von Daak（2006-04-05，Abit NI8 SLI 前传）：nForce4-F4 socket 775 Pentium-D 2.8 + 双 GF7800GTX——/proc/cpuinfo 只认 1 核；加 `pci=noacpi pci=routeioq noapic acpi=off` 后才双核可见但系统不稳（glxgears 即挂）；自编 SMP 内核 + debian-smp 内核同病（cerise 怀疑非 SMP 内核被证伪）——NI8 双核被 ACPI/APIC 压住的完整案情（与 p21 038 结案同源）；Mihai Burcea（2002-10-09，补附件道歉）：Intel Xeon 双芯 PowerEdge 6600——2.4.18 能认 4 芯（含 HT 亲缘），2.5.38 只认 2 真核——HT 亲缘识别差异（2.4/2.5 内核对照），Dunlap 追问后补料；Reigo Küngas（2002-10-14，爱沙尼亚）：IBM Netfinity 5000 双 PIII **650M+700M 非同频**（另两台同频无虞）——RH7.3 + mysql 客户端随机连不上 `error: ''`，2.2 好、2.4 坏、换 mysql 版本没用——异频双 CPU 平台不稳的“非对称频率”可复现报告

**史料**：`1572394`、`1572400`、`1572402`、`1572411`、`1572419`、`1572421`、`1572425`、`1572432`、`1572435`

【Linux社区】**史料锚**：`<!-- ROW_MINE: linux-smp.messages.1572394 -->` `<!-- ROW_MINE: linux-smp.messages.1572400 -->` `<!-- ROW_MINE: linux-smp.messages.1572402 -->` `<!-- ROW_MINE: linux-smp.messages.1572411 -->` `<!-- ROW_MINE: linux-smp.messages.1572419 -->` `<!-- ROW_MINE: linux-smp.messages.1572421 -->` `<!-- ROW_MINE: linux-smp.messages.1572425 -->` `<!-- ROW_MINE: linux-smp.messages.1572432 -->` `<!-- ROW_MINE: linux-smp.messages.1572435 -->`

**史观**：经验优先（总纲第 9 条——经验优先：以 A7M266D 满月稳定、SE7500CW2 PAE 冻结等实机报告为判据）；没有必然性，只有偶然性（总纲第 5 条——没有必然性，只有偶然性：NI8 双核被 ACPI/APIC 压住、异频 PIII 随机断连均由具体固件与配置偶然触发）；本体论上各方平等（总纲第 8 条——本体论上各方平等：科研服务器选型、消费者维权长文与家用板卡实证并置）
**辨析**：CUV4X-D 与 Celeron PIII 800 的组合原文自相矛盾（原稿已标“注：原文如此”）；HT 时代初期的消费者维权长文属旁支材料，仅作时代切片登记，不作为技术判据。
**文献**：DSLXC-4381/4387/4389/4398/4405/4407/4411/4418/4421（`linux-smp.messages.1572394` 等 9 封，2002-04-14 至 2006-04-05），全文见 `raw_source.raw_json`

## 14.3 【Linux社区】锁死、崩溃与深层故障

**要点**：Randy Dunlap（2004-11-07）回 Lenherr（自认发现 smp 与文件缓存竞态）：路由指引——2.4 找 Marcelo Tosatti、2.6 找 Andrew Morton、或按文件系统找对应维护者——维护者路由的口径样本；Krajcsovits Gyorgy（2002-09-06）EBDA UNSAFE 结案：升 2.4.20-pre5 或 IBM ServeRAID 固件二选一后修复、6+ 天 uptime；引 Cox 轶事“ infamous 案例：不喜欢 Linux 的同事在 cron 里放 reboot 命令——被开除了 8)”——EBDA 警告机器自愈记录与运维轶事；Alan Cox（2002-11-27）：Nigbur 2.2.18-SMP+Promise FastTrak（二进制模块）问题——“含 binary only 模块的内核问题请找模块厂商：他们有我们的源码、我们没有他们的，只有他们能真正帮你”——二进制模块支持边界的政策口径；huba（2002-12-02）：双 Xeon 2.4 SE7500CW2 + 2.4.20——11 天运行后神秘锁死（原因未知）；register #00=02008000 警告、附全 boot log——CW2 平台长周期锁死报告；Kacper Wysocki（2003-02-20）：MSI k7d Master-L + 单颗 2400 MP——`APIC error on CPU0: 04(04)` 洪水刷屏直至硬重起；debian boot-floppies 2.4/2.2 内核可启、自己编的 smp 与否全炸；noapic/disableapic、CONFIG_APIC_GOOD/IO_APIC/APIC_LOCAL=n 全无效——APIC error 洪水的 MSI 平台诊治长报告（检索到 Abit BP6 同类 defective APIC 先例）；karl wettin（2003-08-23）：ABit BP6 双 400M Celeron QQ/RU BIOS——SMP 内核起 X 时 Gnome splash 不显现，约 5 分钟后冷启必须；其它程序正常、非 SMP 内核无此问题——“仅 X 触发”的 BP6 SMP lockup 案例（附 XF86Config 日志）

**史料**：`1572401`、`1572404`、`1572408`、`1572410`、`1572415`、`1572436`

【Linux社区】**史料锚**：`<!-- ROW_MINE: linux-smp.messages.1572401 -->` `<!-- ROW_MINE: linux-smp.messages.1572404 -->` `<!-- ROW_MINE: linux-smp.messages.1572408 -->` `<!-- ROW_MINE: linux-smp.messages.1572410 -->` `<!-- ROW_MINE: linux-smp.messages.1572415 -->` `<!-- ROW_MINE: linux-smp.messages.1572436 -->`

**史观**：经验优先（总纲第 9 条——经验优先：以 CW2 11 天锁死、MSI k7d APIC error 洪水与 BP6 仅 X 触发三例为判据）；知识注定过时（总纲第 22 条——知识注定过时：EBDA UNSAFE 经升内核或升固件即自愈，二进制模块支持边界亦随厂商策略变动）；动手者创造历史（总纲第 10 条——动手者创造历史：排除实验由报料者自行完成）
**辨析**：Cox 的“二进制模块问题请找厂商”是支持边界的政策口径而非技术裁定；BP6“仅 X 触发”与 k7d APIC error 洪水均无确诊结论，落书不得据以断言硬件缺陷。
**文献**：DSLXC-4388/4391/4395/4397/4402/4422（`linux-smp.messages.1572401` 等 6 封，2002-09-06 至 2004-11-07），全文见 `raw_source.raw_json`

## 14.4 【Linux社区】亲和性、调度与接口导出

**要点**：J.A. Magallon（2002-07-12）续 per-thread 设计：问“如何从线程内拿到栈起点”；Cox 前答“栈同尺寸可用内核栈算术藏线程全局”；另问 Linux 有无 barrier() syscall（semaphore -N 洞实现设想）+ man sem_init 揭 LinuxThreads 不支持进程共享信号量（pshared≠0 恒 ENOSYS）——TLS 与同步原语缺口双记录；Gaspar Bakos（2004-01-15）：E7505 SE7505VB2 双 Xeon 2.66 HT——dmesg 揭“Error: only one processor found”+“WARNING: No sibling found for CPU 0”；ACPI LAPIC 条目 lapic_id 0x00 与 0x06（非连续编号）——p21/043 MAX_NR_CPUS=8 结案的诊断前半（BIOS 编号不连续实据）；JaniD++（2005-12-07）：双 Xeon HT 2.6.15-rc3（2.6.14.2 同）——`echo 1 > 217/smp_affinity` 后读仍是 f（Xeon+HT 四核）；/proc/interrupts 显示 eth1 494M 中断全挤在 CPU3——IRQ 亲和性写不入的问题（附 config，目击者视阈值）；Emil Medve（2008-07-20，Freescale）：[PATCH] 导出 `irq_set_affinity()` —— kernel/irq/manage.c +EXPORT_SYMBOL，为 SMP 上模块化驱动设置初始/默认显式 IRQ 负载均衡，checkpatch 0 错——irq 亲和力 API 导出的实现路径

**史料**：`1572390`、`1572396`、`1572428`、`1572430`

【Linux社区】**史料锚**：`<!-- ROW_MINE: linux-smp.messages.1572390 -->` `<!-- ROW_MINE: linux-smp.messages.1572396 -->` `<!-- ROW_MINE: linux-smp.messages.1572428 -->` `<!-- ROW_MINE: linux-smp.messages.1572430 -->`

**史观**：经验优先（总纲第 9 条——经验优先：以 smp_affinity 写不入、E7505 LAPIC 编号不连续与 eth1 中断全挤 CPU3 的实测为判据）；动手者创造历史（总纲第 10 条——动手者创造历史：irq_set_affinity() 导出补丁由 Freescale 开发者实发）；不存在进步，只有权力再分配（总纲第 3 条——不存在进步，只有权力再分配：中断处置权在 CPU 与模块之间重新分配）
**辨析**：TLS 设计前史两问（线程栈起点、barrier() 系统调用）与本块其余三例主题不同，仅因同属“亲和性/调度/接口”而并置；irq_set_affinity() 导出系补丁提案，落书不得写作已入主线。
**文献**：DSLXC-4379/4383/4414/4416（`linux-smp.messages.1572390` 等 4 封，2002-07-12 至 2008-07-20），全文见 `raw_source.raw_json`

## 14.5 【Linux社区】X 窗口、MTRR 与热敏回归（2021 收尾）

**要点**：Srinivas Pandruvada（2021-05-27，Intel）答 Petkov：确认 SMM 会用热中断（Yoga 系统 HWP 相关 SMM 热中断处理曾致硬挂）；同意 lvtthmr 后读会复制错值（软禁 APIC 后核等中断锁死）、将下周在 Yoga 上强制复制错值验证；“IPI 远程 TLB flush 锁死——我想是另一核没退出 SMM 模式”——5.12 热敏回归的 Intel 侧机制确认（另一核滞留 SMM 假说）；Kline, Larry（2005-04-25，RE: IO_APIC 线索）：X windows 起不来（红屏 5 秒回终端）——Dunlap 两连问“什么变了？”；此前加了 IBM MULTIBURNER PLUS（RAMBO IV）光驱后 3 cdrom 7 dvd、插拔 Super dvd 互斥丢 cdrom；SuSE 8.0 + CTX CPG1772E sax2“Signal out of range 79.8kHz 74.9Hz”改 XF86Config 无效——X/设备探测疑难链（SMP 列表上旁支）；Thomas Ernet（2004-04-04）：Dell Dimension P4 2.8 HT SuSE 9.0 2.4.19smp——register #00 02000000（非常见 02008000）、时冻结（不受外部访问）——HT 主机 + 冻结 + IO-APIC 的实例；David Gjerdrum（2002-05-30，Supermicro P4DP6 双 Xeon e7500 6GB）：NVIDIA GeForce4 MX 420——`mtrr: type mismatch for F8000000 4000000 old: uncachable new: write-combining` 循环报 + NVIDIA: Failed to set up write-combining range（同理地址）、/proc/mtrr 手工改写无效（Gooch 方法 `>`/`>>` 均试）——MTRR 与 IO-APIC 双症状（boot.msg 里同见 02008000 警告）互认平台（板上线程名超长被截）

**史料**：`1572409`、`1572423`、`1572427`、`1572437`

【Linux社区】**史料锚**：`<!-- ROW_MINE: linux-smp.messages.1572409 -->` `<!-- ROW_MINE: linux-smp.messages.1572423 -->` `<!-- ROW_MINE: linux-smp.messages.1572427 -->` `<!-- ROW_MINE: linux-smp.messages.1572437 -->`

**史观**：经验优先（总纲第 9 条——经验优先：以 Yoga 平台 SMM 热中断实测与 mtrr 循环报为判据）；循环结构呈现（总纲第 4 条——循环结构呈现：2002 年 IO-APIC/MTRR 症状与 2021 年 SMM 热敏回归跨 19 年同题回归）；动手者创造历史（总纲第 10 条——动手者创造历史：Intel 侧机制确认由当事人亲答）
**辨析**：Intel 侧“另一核滞留 SMM”系假说（原文作“I think”），尚未验证；Kline 的 X 起不来一例属设备探测旁支，仅登记不引申。
**文献**：DSLXC-4396/4409/4413/4423（`linux-smp.messages.1572409` 等 4 封，2002-05-30 至 2021-05-27），全文见 `raw_source.raw_json`

## 14.6 【Linux社区】Cox 定调与维护者方法论

**要点**：Alan Cox（2002-11-22）答 Craig Anderson（RH7.2 直装盘报料）：“Start by applying the latest errata. You actually need that for SMP PIV to be totally solid”——SMP P4 须先打勘误补丁（默认盘带旧内核）的定调回复；Alan Cox（2002-08-22）答 Jon Zobrist（2.4.19 四核全用、有 APIC error 但正常）：“Should be no need then——我们的 19-ac 不用打。Special handling kicks in if you have enough cpus that the numa parts of the chipset kick in”——**CPU 数量足够触发 chipset 的 NUMA 部分才走特殊处理**的定调

**史料**：`1572424`、`1572431`

【Linux社区】**史料锚**：`<!-- ROW_MINE: linux-smp.messages.1572424 -->` `<!-- ROW_MINE: linux-smp.messages.1572431 -->`

**史观**：经验优先（总纲第 9 条——经验优先：以“SMP P4 须先打勘误补丁”与“CPU 足够多才触发 chipset NUMA 部分”两条实践口径为判据）；动手者创造历史（总纲第 10 条——动手者创造历史：定调出自内核维护者本人答复）
**辨析**：两条均为 Cox 个人答复口径，非文档化规范；“19-ac 不用打”限定于其自维护分支，落书须保留分支与版本限定。
**文献**：DSLXC-4410/4417（`linux-smp.messages.1572424`、`.1572431`，2002-08-22 至 2002-11-22），全文见 `raw_source.raw_json`

## 14.7 【Linux社区】文档与学习路径

**要点**：Randy Dunlap（2002-07-18）答 Redd（MIPS 转 x86）APIC/IO-APIC/local APIC 术语之别：推荐 IA-32 Intel Architecture SDM 三卷（Vol.3 最佳：Ch7 多处理器管理/Ch8 处理器管理与初始化/App D LINT0/1 编程/App F APIC 总线消息格式）；“找到好资源请回帖”——APIC 学习路径的权威指引

**史料**：`1572412`

【Linux社区】**史料锚**：`<!-- ROW_MINE: linux-smp.messages.1572412 -->`

**史观**：经验优先（总纲第 9 条——经验优先：以维护者指定的 IA-32 SDM 三卷及具体章节为查证路径）；动手者创造历史（总纲第 10 条——动手者创造历史：指引出自维护者本人答复）
**辨析**：本块仅一条问答，“找到好资源请回帖”属社区协作呼吁；章节号以 Intel SDM 1999 版为准，新版可能重编。
**文献**：DSLXC-4399（`linux-smp.messages.1572412`，2002-07-18），全文见 `raw_source.raw_json`

---
注：本文件由判定表程序化生成（14.1-14.7 共 7 块，覆盖 47/47 CAND）；要点逐字取自判定表“要点”列（审读实录），史料锚与 CAND 一一对应，全文以 raw_source.raw_json 为准。
