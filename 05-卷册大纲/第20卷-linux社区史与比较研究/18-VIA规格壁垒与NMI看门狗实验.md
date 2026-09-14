# 18 【Linux社区】VIA规格壁垒与NMI看门狗实验

> 对应页面：linux-smp p26（pk 1572588-1572637，2002-2006 为主 + 2021 三封）
> 判定：45 CAND / 5 NV（007/013 纯转交、008/017 纯附件转交、046 撤回信）
> 编号：DSLXC-4562..4606 | claim 已入库（45/45，dslinux_claims.duckdb）

## 18.1 【Linux社区】报料全景与 Unknown CPU/寄存器残值序列（11 例）

**要点（判定表逐字）**：root/Ralf（2003-01-21，creativeserver.de）：例行报料“so I'm doing what it says :)”附警告片段——样本；Ingo Claro（2003-11-14，智利）：2.4.18-3smp 警告“tell me if you need any more info”——样本；Bernard and Jennifer Cohen（2003-02-28，加拿大）：v3 警告转储（正文含）+“Should I be concerned? Bernie :)”——正文转储样本；Juan Pedro Paredes（2002-12-10）：IBM NetVista 6349 A22p 2.4.20-686（UP）——**“Processor #0 Unknown CPU [15:1] APIC version 16”**（P4 Willamette 未识别）+ IO-APIC #1 register #00: 01008000 残值——UP+Unknown CPU+#00 残值；Kevin D. Timm（2003-02-17）：“dmesg output, requested”2.4.19-16mdkcustom VIA（KT266 系）Athlon XP 2100+ UP v3 警告 + bttv——正文完整 dmesg；Pawel Niewiadomski（2003-11-25，波兰）：SE7500CW2 双 Xeon 2.4（三 IO-APIC，**#2 register #00: 02008000 残值**）+ ICH3 BIOS setup incomplete + Out of Memory Killed httpd——#00 残值与 OOM；A.J. Duijn（2003-11-12，荷兰）：2.4.19-16mdk VIA VT5440B v3 警告——正文含片段；Les Campbell（2003-08-30，加拿大）：v3 警告转储（正文含）——样本；Francis SOUYRI（2005-02-21，法国）：**Iwill DK8N 双 Opteron 2.4.29 警告**（syslog 附件）——x86-64 时代双 Opteron+2.4 样本；Fabio Moratti（2002-11-28，罗马 NEXSE）：2.4.2-2smp 双 Coppermine——v0011 警告 + MP 表 IRQ 47/46 重复条目 + MTRR 各 CPU 不一致 + nVidia Vanta 资源分配失败——完整 dmesg；Graham Wilson（2004-06-06，加拿大 telus）：ASUSTek **“Processor #0 Unknown CPU [15:3] APIC version 20”**（P4 Prescott 15:3 未识别）UP v20 + #02 残值——Unknown CPU 15:3 样本

**史料**：`1572588`、`1572590`、`1572596`、`1572601`、`1572602`、`1572606`、`1572607`、`1572622`、`1572626`、`1572628`、`1572637`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572588 -->` `<!-- ROW_MINE: linux-smp.messages.1572590 -->` `<!-- ROW_MINE: linux-smp.messages.1572596 -->` `<!-- ROW_MINE: linux-smp.messages.1572601 -->` `<!-- ROW_MINE: linux-smp.messages.1572602 -->` `<!-- ROW_MINE: linux-smp.messages.1572606 -->` `<!-- ROW_MINE: linux-smp.messages.1572607 -->` `<!-- ROW_MINE: linux-smp.messages.1572622 -->` `<!-- ROW_MINE: linux-smp.messages.1572626 -->` `<!-- ROW_MINE: linux-smp.messages.1572628 -->` `<!-- ROW_MINE: linux-smp.messages.1572637 -->` 

- **史观**：经验优先（总纲第 9 条——经验优先：以 11 例用户 dmesg 与寄存器残值实测为判据）；动手者创造历史（总纲第 10 条——动手者创造历史：报料者自述机型与固件版本构成史料本体）；本体论上各方平等（总纲第 8 条——本体论上各方平等：UP 用户与双 Xeon 用户同列）
- **辨析**：11 例均为用户自述，未经维护者逐例裁定；“Should I be concerned?”一类提问保留原语气，落书不得据以断言该警告后果。
- **文献**：DSLXC-4562/4564/4568/4572/4573/4576/4577/4592/4596/4598/4606（`.1572588`、`.1572590`、`.1572596`、`.1572601`、`.1572602`、`.1572606`、`.1572607`、`.1572622`、`.1572626`、`.1572628`、`.1572637`，2002-11 至 2005-02），全文见 `raw_source.raw_json`

## 18.2 【Linux社区】维护者定调与供应商信息壁垒（4 例）

**要点（判定表逐字）**：Alan Cox（2002-12-10）答 uaca（VA Linux FullOn 2230 双 PIII 440GX“Possibly defective BIOS detected (irqtable)”）：**“If your box works you are ok, if not well Intel have been refusing for a long time to tell us how to handle it”**——440GX irqtable 缺陷与 Intel 拒供资料第一手；Alan Cox（2002-11-29）答 Erik Meusel：**“The SiS APIC is not yet supported. SiS have provided the needed info to fix that, and I'm testing a fix in 2.5 ready to backport once I'm sure it works properly. For now run with 'noapic'”**——SiS APIC 支持史关键一手；Alan Cox（2002-05-20）答 Moncada（Supermicro P4DC6+ Xeon 1.5 v20）：**“Its fine. Things should work happily. Its a version that tyour kenrel doesnt know but the APIC stuff is compatible”**（kenrel 原文如此）——v20 兼容定调；Randy Dunlap（2002-05-23）答 Nietzel：**“This particular IO APIC version and flag are handled (recognized) in 2.4.16 IIRC (maybe 2.4.17). We are seeing lots of these reports with VIA KT266 or KT333 chipsets...with IO APIC version 0x02. Since VIA doesn't release their chipset specs, we don't know how correct these are.”**——v0x02 识别版本点 + VIA 不公开规格的供应商信息壁垒第一手

**史料**：`1572593`、`1572599`、`1572631`、`1572634`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572593 -->` `<!-- ROW_MINE: linux-smp.messages.1572599 -->` `<!-- ROW_MINE: linux-smp.messages.1572631 -->` `<!-- ROW_MINE: linux-smp.messages.1572634 -->` 

- **史观**：不存在进步，只有权力再分配（总纲第 3 条——不存在进步，只有权力再分配：规格资料的有无决定厂商与社区之间的话语权）；经验优先（总纲第 9 条——经验优先：以 Cox 的 SiS/440GX 实测与 Dunlap 的 KT266/KT333 报告为判据）
- **辨析**：“Intel 长期拒供资料”与“VIA 不公开规格”系维护者当时陈述，构成供应商信息壁垒的第一手证据，但不可据此断言厂商永久立场。
- **文献**：DSLXC-4567/4571/4601/4603（`.1572593`、`.1572599`、`.1572631`、`.1572634`，2002-05 至 2002-12），全文见 `raw_source.raw_json`

## 18.3 【Linux社区】BIOS 归因与 CUV4X-D 处方链（4 例）

**要点（判定表逐字）**：Dr. Michael Weller（2002-10-29，埃森大学）：答 Kleine（CUV4X-D noapic 之问）——**“BIOS settings modify how the apic is setup and hence if linux needs noapic”“the (no)apic issue is generally a BIOS issue (since linux relies on a proper preconfigured apic/chipset)”**——noapic 根源论（BIOS 归因）；**Doug Ledford（2002-05-21，Red Hat aic7xxx 维护者）**答 Bunk：**“You are having IRQ routing problems. Evidently the smp kernel can not properly set up the apic IRQ routing on your machine. Try...MPS table to either version 1.1 or 1.4”**——aic7xxx noapic 案例与 MPS 切换处方；Vladimir（2002-07-08）答 Tumenbayar：**“I do not need to turn off IO-APIC if I backed down from MPS 1.4 to 1.1. Apparently some (all?) Xeon-based boards need to do both, but ASUS CUV4X boards do not...Please incorporate this advice into your FAQ.”**——CUV4X MPS-only 处方定型与入 FAQ 之请；Alan Cox（2002-04-15）答 u.milde（CUV4X-D）：**“What BIOS version do you have ? I've seen several reports of BIOS updates being needed. Specifying 'noapic' might also help”**——CUV4X-D BIOS 版本询问（p25 027/034 处方链的 Cox 原帖）

**史料**：`1572617`、`1572618`、`1572620`、`1572630`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572617 -->` `<!-- ROW_MINE: linux-smp.messages.1572618 -->` `<!-- ROW_MINE: linux-smp.messages.1572620 -->` `<!-- ROW_MINE: linux-smp.messages.1572630 -->` 

- **史观**：经验优先（总纲第 9 条——经验优先：以 MPS 1.4→1.1 回退实测与 BIOS 版本询问为判据）；本体论上各方平等（总纲第 8 条——本体论上各方平等：Weller 的 BIOS 归因、Ledford 的 MPS 处方与 Cox 的版本询问并置）
- **辨析**：“noapic 根源在 BIOS”为 Weller 的归因判断，Cox 与 Ledford 的处方与之部分重叠而非同一结论，落书须并列而不合并。
- **文献**：DSLXC-4587/4588/4590/4600（`.1572617`、`.1572618`、`.1572620`、`.1572630`，2002-04 至 2002-10），全文见 `raw_source.raw_json`

## 18.4 【Linux社区】平台兼容个案（5 例）

**要点（判定表逐字）**：Alan Cox（2003-05-14）答 Ivars Strazdins（Compaq）：**“Looks like their BIOS has some errors right now”“ACPI: Too big length in RSDT: 132”“that or we are being too aggressive in our testing ?”**——RSDT 长度缺陷与测试激进自省；Javier Ramos（2004-07-22，西班牙 parsec.es）：RHEL3 **kernel-hugemem 只认 1 CPU**（RH9 双 CPU 正常）——“xAPIC support is not present”+ mapped 4G/4G trampoline + v20 #02 残值 + No sibling——hugemem 单 CPU 回归；Alan Cox（2003-03-03）答 Huhn（ICH3 BIOS setup incomplete）：**“No the kernel cleaned that one up for you”**——ICH3 一句裁定；Francisco Arroyo Mora（2004-02-17，哥斯达黎加）：**Fujitsu-Siemens Primergy T850 4×Xeon 1.4（IBM SERVIGIL OEM）**——**“Processor #17/#33/#49 INVALID - (Max ID: 16)”+“We modify a little the kernel source (btw this became a patch in the next releases) to modify the maximun APIC id available”**——Max APIC ID 16 上限补丁一手（用户改动成为后续 release 补丁）；Basheer Ahamed/Mansoor Ahamed（2005-06-22，Intel 员工）：求“linux 2.6.8-2 SMP for Intel architecture”旧版下载（评估板测试版本对齐，“That version was tested on our evaluation board”）——Intel 内部旧内核版本对齐需求切片

**史料**：`1572598`、`1572612`、`1572625`、`1572632`、`1572635`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572598 -->` `<!-- ROW_MINE: linux-smp.messages.1572612 -->` `<!-- ROW_MINE: linux-smp.messages.1572625 -->` `<!-- ROW_MINE: linux-smp.messages.1572632 -->` `<!-- ROW_MINE: linux-smp.messages.1572635 -->` 

- **史观**：经验优先（总纲第 9 条——经验优先：以 hugemem 单 CPU 回归与 Max APIC ID 16 上限补丁为判据）；没有必然性，只有偶然性（总纲第 5 条——没有必然性，只有偶然性：个案由具体 BIOS/固件缺陷偶然触发）
- **辨析**：“用户改动成为后续 release 补丁”一例属当事人自述，须以当时提交记录复核；Intel 员工求旧版内核一例属版本对齐需求，非技术缺陷。
- **文献**：DSLXC-4570/4582/4595/4602/4604（`.1572598`、`.1572612`、`.1572625`、`.1572632`、`.1572635`，2003-03 至 2005-06），全文见 `raw_source.raw_json`

## 18.5 【Linux社区】NMI 看门狗实验三连

**要点（判定表逐字）**：Andrew Erickson（2002-04-23，emji）：IBM Netfinity 7100 随机锁死——**“MP-BIOS bug: 8254 timer not connected to IO-APIC→Virtual Wire IRQ works”+“nmi_watchdog=0”后锁死消失（17 天 uptime）**——NMI watchdog 关联的一手排除实验；Christophe A. Gevaudan（2003-02-01）：GA-6BXDU 双 Coppermine 450（440BX）2.4.19 SMP 挂在 PCI probing，**移除 nmi_watchdog=1 后“this switches the complete hardware off”**；nosmp 正常——NMI watchdog+440BX 案例；**Lars Marowsky-Bree（2002-08-29，SuSE HA 架构师）**：“If the kernel asks me to send mail, I sure do ;-) Everything seems to work fine though.”——ABIT KX7-333 单 XP 1800+ UP + nmi_watchdog=1“activating/testing NMI Watchdog...OK”+ v2 警告——知名人物对照样本

**史料**：`1572603`、`1572614`、`1572629`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572603 -->` `<!-- ROW_MINE: linux-smp.messages.1572614 -->` `<!-- ROW_MINE: linux-smp.messages.1572629 -->` 

- **史观**：经验优先（总纲第 9 条——经验优先：以 17 天 uptime 与硬件关闭实测为判据）；动手者创造历史（总纲第 10 条——动手者创造历史：nmi_watchdog 排除实验由用户自行完成）
- **辨析**：三例均为用户侧排除实验，nmi_watchdog 与锁死的因果仅在第一例由 uptime 支持，其余两例仍属相关而非定因。
- **文献**：DSLXC-4574/4584/4599（`.1572603`、`.1572614`、`.1572629`，2002-04 至 2003-02），全文见 `raw_source.raw_json`

## 18.6 【Linux社区】崩溃与锁死（3 例）

**要点（判定表逐字）**：Philippe Lewicki（2002-11-14）：**kernel NULL pointer（2.2.19-7.0.16smp RH7.0 生产服务器）**+ AMI 840_CARMEL 双 IO-APIC（#2 v20、#3 v20 + **register #02: 0D000000**）+“Error: only one processor found”——2.2+双 IO-APIC+NULL pointer 复合；Nikolay Datchev（2002-06-26，保加利亚 varna.net）：**双 Klamath 450 + 2.2.20 SMP 后 fork(): unable to allocate memory（768MB RAM 充裕）**——2.2 时代 SMP fork 内存分配故障；Nathan Dehnel（2021-08-26）：Framework 笔记本（Tiger Lake，i915/proc_thermal）mpv soft lockup——**“it only happens when mpv is run without pulseaudio running”**——2021 现代样本

**史料**：`1572597`、`1572619`、`1572623`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572597 -->` `<!-- ROW_MINE: linux-smp.messages.1572619 -->` `<!-- ROW_MINE: linux-smp.messages.1572623 -->` 

- **史观**：经验优先（总纲第 9 条——经验优先：以 NULL pointer、fork 内存分配失败与 soft lockup 实测为据）；历史地理塑造思想土壤（总纲第 20 条——历史地理塑造思想土壤：2.2 时代硬件与 2021 笔记本平台构成不同技术土壤）
- **辨析**：2.2 时代两例与 2021 现代样本跨近二十年，平台条件不可通约，落书须分叙；mpv 一例当事人已给出复现条件（无 pulseaudio 运行）。
- **文献**：DSLXC-4569/4589/4593（`.1572597`、`.1572619`、`.1572623`，2002-06 至 2021-08），全文见 `raw_source.raw_json`

## 18.7 【Linux社区】2021 热敏线（根源定位与下游追问）

**要点（判定表逐字）**：James Feeney（2021-05-31）答 Petkov（2021 热敏线程）：**“Has the patch that resolves - or at least pacifies - this issue been forwarded downstream to GKH for mainline yet? I'd like to be able to upgrade with stock kernels again.”**——下游合并追问；**James Feeney（2021-05-17）**：**git bisect 定位 4f432e8bb15b（Petkov“x86/mce: Get rid of mcheck_intel_therm_init()”2021-01-07）为 first bad commit**——5.12 soft lockup CPU#0 stuck 23s（smp_call_function_single，trace 见 __flush_tlb_all/tlbflush_read_file）——2021 热敏回归根源 bisect 一手

**史料**：`1572592`、`1572605`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572592 -->` `<!-- ROW_MINE: linux-smp.messages.1572605 -->` 

- **史观**：动手者创造历史（总纲第 10 条——动手者创造历史：git bisect 由报告者自行定位 first bad commit）；经验优先（总纲第 9 条——经验优先：以 4f432e8bb15b 与 23 秒 stuck 实测为判据）
- **辨析**：bisect 结论指向 Petkov 2021-01-07 提交，属报告者单方定位；下游追问（是否已 forward 给 GKH）表明修复尚未闭环。
- **文献**：DSLXC-4566/4575（`.1572592`、`.1572605`，2021-05），全文见 `raw_source.raw_json`

## 18.8 【Linux社区】HT 语义四问（4 例）

**要点（判定表逐字）**：Robert Hyatt（2003-05-14）答 John Lloyd（布里斯托市政 IBM x345 双 2G Xeon 检出 4）：“Yes that is the explanation...”（HT）——HT 确认简复（bigmem 内核完整 ACPI/MADT 转储）；Robert Hyatt（2002-11-22）：**“Does the current kernel know anything about hyper-threading, beyond the fact that it sees an extra cpu for each real cpu installed?...might it schedule both on one physical cpu since it looks like two to the kernel?”**——HT 调度感知之问（SCHED_SMT 前史）；Peter Hemström（2004-10-03，瑞典）：**“Should i use the SMP kernal with an INTEL HT-Tech CPU?”**——新手 HT/SMP 关系咨询；Ray Taft（2002-11-26，XFR Networks）：**RH7.2 只见 2 Xeon（RH8.0 可见 4 HT）**——“Is their anyway of patching the 7.2 kernal to support hyperthreaded XEON servers?”——发行版 HT 支持代差

**史料**：`1572589`、`1572610`、`1572615`、`1572627`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572589 -->` `<!-- ROW_MINE: linux-smp.messages.1572610 -->` `<!-- ROW_MINE: linux-smp.messages.1572615 -->` `<!-- ROW_MINE: linux-smp.messages.1572627 -->` 

- **史观**：经验优先（总纲第 9 条——经验优先：以 RH7.2 与 RH8.0 的 HT 检出差异为判据）；知识注定过时（总纲第 22 条——知识注定过时：SCHED_SMT 之前的 HT 调度感知之问）
- **辨析**：Hyatt 的调度感知之问属 SCHED_SMT 前史，非结论；发行版代差一例系具体版本行为，不可外推为内核通用能力。
- **文献**：DSLXC-4563/4580/4585/4597（`.1572589`、`.1572610`、`.1572615`、`.1572627`，2002-11 至 2004-10），全文见 `raw_source.raw_json`

## 18.9 【Linux社区】调度分裂观察

**要点（判定表逐字）**：Simon Oliver（2002-07-23，UMIST）：关 HT 后 perl 进程在双 CPU 间跳跃甚至 **50/50、25/75 split**（top 监测）——“binding of a process to a cpu is 'loose' under linux (as apposed to Irix say)”——调度分裂观察

**史料**：`1572613`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572613 -->` 

- **史观**：经验优先（总纲第 9 条——经验优先：以 top 监测的 50/50、25/75 分裂为判据）；没有必然性，只有偶然性（总纲第 5 条——没有必然性，只有偶然性：进程迁移由当时调度器实现偶然决定）
- **辨析**：“binding 是 loose 的”系当事人跨系统比较（对照 Irix）之判断，属观察记录而非内核保证。
- **文献**：DSLXC-4583（`linux-smp.messages.1572613`，2002-07-23），全文见 `raw_source.raw_json`

## 18.10 【Linux社区】APIC error 与驱动诊断（3 例）

**要点（判定表逐字）**：Chema（2002-06-05，马德里理工）：**Gigabyte GA586DX 双 Pentium MMX 166 极限测试两天 100% 负载表现优秀但连续“APIC error on processor 0 (02:00)”/“processor 1 (08:00)”**问含义——老平台 APIC error 罕见样本；Pedro Pla（2002-11-06）GDT 线程续：**换 CPU 插槽 UP 依旧完美、全部 SIMM 在 MP 下失败 UP 下完美**；Ledford 论 UP→SMP 硬件变化（功耗/第二 CPU/内存吞吐）；intel SCB2 无法切 MP 1.1（BIOS 无选项）——UP/SMP 硬件诊断方法论；Earle R. Nietzel（2002-08-15）：ABIT BP6 APIC error 00(08)/00(04)/04(04)/04(08)——**“Though this box has been solid even with these errors, it has never crashed. Linus also mentioned to me that if I didn't have any trouble I could disregard these errors.”**（Cox：“The long stream of 8/4 is something odder going on”）——Linus 无害定调转述

**史料**：`1572609`、`1572621`、`1572624`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572609 -->` `<!-- ROW_MINE: linux-smp.messages.1572621 -->` `<!-- ROW_MINE: linux-smp.messages.1572624 -->` 

- **史观**：经验优先（总纲第 9 条——经验优先：以两天满负载实测与 UP/SMP 对照为判据）；本体论上各方平等（总纲第 8 条——本体论上各方平等：Chema、Pla、Nietzel 三方与 Cox 裁定并置）
- **辨析**：“Linus 无害定调”系 Nietzel 转述，非 Linus 原文，落书须标转述；Cox 的“8/4 流更古怪”表明该现象未获完整解释。
- **文献**：DSLXC-4579/4591/4594（`.1572609`、`.1572621`、`.1572624`，2002-06 至 2002-11），全文见 `raw_source.raw_json`

## 18.11 【Linux社区】社区机制切片（5 例）

**要点（判定表逐字）**：Mohamed Bamakhrama（2007-07-05）：**SMP 移植到自定义双核 MIPS（非 Intel MPS 1.4）求指南**——“Is there any guideline or tutorial for porting SMP kernel into a new hardware architecture”——非 x86 SMP 移植开发之问；Scott Bronson（2002-08-22）：**“Interested in an ss40g APIC issue? It will take me maybe 1/2 day to...figure out exactly what is broken and how. Is anybody out there interested in the results?”**——自费排障意愿询问（社区动员切片）；Erik Mouw（2006-09-05）答 Jigar Raval：top-posting 教训 + **“Matti and Davem have installed Bogofilter on it (a spam filter)”**——vger 垃圾过滤史一手；Bernd Strebel（2005-05-27，digitec.de）转述 Dunlap：**“There are some lines missing in the kernel message log above...kern.* -/var/log/kern.log”“BTW, this isn't a critical message (unexpected IO-APIC).”**——syslog 补全法与非致命定调再一手；Randy Dunlap（2006-04-06）答 Frank von Daak（Abit NI8 双核 ACPI 调试）：**“I suggest that you ping the acpi development list...You'll probably need to provide the ACPI firmware tables...Use pmtools (acpidump)”**——ACPI 表转储工具指引（跨列表转介）

**史料**：`1572591`、`1572608`、`1572611`、`1572616`、`1572636`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572591 -->` `<!-- ROW_MINE: linux-smp.messages.1572608 -->` `<!-- ROW_MINE: linux-smp.messages.1572611 -->` `<!-- ROW_MINE: linux-smp.messages.1572616 -->` `<!-- ROW_MINE: linux-smp.messages.1572636 -->` 

- **史观**：动手者创造历史（总纲第 10 条——动手者创造历史：Bronson 自费排障意愿与 Mouw 的 vger 过滤史）；经验优先（总纲第 9 条——经验优先：以 syslog 补全法与 acpidump 指引为判据）
- **辨析**：“非致命”定调经 Strebel 转述 Dunlap，须标转述；vger 垃圾过滤与 pmtools 指引属工具史留痕，非技术结论。
- **文献**：DSLXC-4565/4578/4581/4586/4605（`.1572591`、`.1572608`、`.1572611`、`.1572616`、`.1572636`，2002-08 至 2007-07），全文见 `raw_source.raw_json`

---
注：本文件由判定表程序化生成（18.1-18.11 共 11 块，覆盖 45/45 CAND，两遍计数核对通过）；要点逐字取自判定表“要点”列（主代理全读审读实录），史料锚与 CAND 一一对应，全文以 raw_source.raw_json 为准。
