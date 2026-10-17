# 21 【Linux社区】警告机制解读全文与AMD勘误提示

> 对应页面：linux-smp p29（pk 1572738-1572787，2002-2005 为主）
> 判定：48 CAND / 2 NV（024 纯附件转交、042 分区问题离题）
> 编号：DSLXC-4704..4751 | claim 已入库（48/48，dslinux_claims.duckdb）

## 21.1 【Linux社区】警告机制解读全文与 noapic 论战（2 例）

**要点（判定表逐字）**：**Earle R. Nietzel（2003-04-17）：“How does an UNEXPECTED_IO_APIC happen?”警告机制科普全文——三寄存器位段图解（#00 res1/ID/res2；#01 res1/entries/PRQ/version；#02 res1/arbitration/res2）+ entries 白名单（0x0f Neptune/0x17 ISA+PCI/0x1b Compaq Proliant/0x1f dual Xeon/0x22 bigger Xeon/0x2E/0x3F）+ version 白名单（0x01 82489DX/0x02 VIA/0x10/0x11 Pentium-Pro/0x13 Xeon/0x20 P64H 82806AA）+“allow kernel programmers (most likely Ingo Molnar) to see what types of hardware are out there and to create a known list”+ 自家 X5DAE（E7505）三 IO-APIC 转储**——警告机制的最权威社区解读（与 p27 002 Dunlap 研究互补，本库最重一手之一）；Matthias Kleine（2002-10-29）答 Ivanovic（CUV4X-DLS 可用 APIC 论）：**“Without noapic: my eth0 and ippp0 devices do not work, my NVIDIA driver does not work. With noapic everything works quite fine. I think you need a _very strong_ reason to convince me”**——noapic 派最强证词（CUV4X-D/DLS 分歧实证）

**史料**：`1572784`、`1572758`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572784 -->` `<!-- ROW_MINE: linux-smp.messages.1572758 -->` 

**史观**：动手者叙事（总纲第 10 条——动手者创造历史：以三寄存器位段图解与白名单逐值列举这一具体技术拆解为分析单位）；文化即形式主义（总纲第 15 条——文化即形式主义：known list 这一形式化清单成为判定标准）
**辨析**：Nietzel 的解读系社区侧最完整的一手科普，其白名单值与内核源码应对勘；Kleine 的 noapic 证词为个人机型经验，本块不据此裁定 CUV4X-D 的普适处方。
**文献**：DSLXC-4748、DSLXC-4724（`linux-smp.messages.1572784`、`linux-smp.messages.1572758`，2003-04-17、2002-10-29），全文见 `raw_source.raw_json`

## 21.2 【Linux社区】报料全景（UP/VIA 系 14 例）

**要点（判定表逐字）**：Pasquale Federico Zema（2002-12-16，意大利 Calabria 大学）：P4 2.4（HT flags）2.4.19 警告（cpuinfo 附）——报料样本；Giulivo Navigante（2003-04-15，意大利）：**Abit KX7-333 开 APIC+MPS 1.4** 2.4.20 警告——KX7 系样本（与 p25 048 同板）；Sebastian Frei（2002-12-17，德国）：**MSI KT4V-L + 2.5.52 开发内核** v3 警告（ACPI MADT）+ Via IRQ fixup 三连——2.5 系开发内核报料；countdown（2002-07-17）：GIGABYTE 7VRXP（同 p24 007 板）2.4.18 v2 警告转储——样本；David Vuorio（2002-11-16，瑞典）：VIA（KT266/VT5440B）XP 1800+ UP 2.4.19-16mdk v2 警告——“The computer boots up just fine though”正文含 dmesg——样本；Gary Buckmaster（2005-01-31）：警告转储片段（正文含 redirection table）——样本；Jimmy Wennlund（2002-10-06，瑞典）：KT3 Ultra2 XP 2000+ 2.4.20-ac 警告——“My motherbord wont work..I had a little luck with linux-2.4.20-ac kernel”——报料；Darrell Fixler（2002-10-14）：**2.5.42** MSI KT333 v2 警告——“the APIC interrupt assignments have no noticeable problem even with this 'unknown' APIC”+ 2.5 USB 坏——2.5 日报料；bl8n8r（2003-05-08）：2.4.19-16mdk XP 2000+ UP v3 警告——“dmesg said to send this mail :)”正文完整 dmesg——样本；Sythos（2003-02-13，意大利）：**MSI KT4V（KT400）Duron v3 警告转储**——样本；darshan（2005-06-17）：**全新 Compaq Presario R4000 笔记本（ATI chipset）2.4.31 双警告**——“But so is the computer.”——新机+旧内核并置；reaper@mindriot.as（2003-05-02）：**“As ordered by the kernel”——双 P3 1.13 2.4.20 v2 警告转储**——样本；Jürgen Kolk（2004-04-07，德国 Kiel）：**Tyan S5102 P4 2.8 Debian 2.4.25 警告**——报料点名；salparadiso（2003-02-23，autistici）：**MSI KT400 Ultra v3 警告——“that's what I'm doing!!!!”**——报料样本

**史料**：`1572740`、`1572741`、`1572743`、`1572745`、`1572746`、`1572748`、`1572755`、`1572757`、`1572764`、`1572765`、`1572766`、`1572769`、`1572775`、`1572780`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572740 -->` `<!-- ROW_MINE: linux-smp.messages.1572741 -->` `<!-- ROW_MINE: linux-smp.messages.1572743 -->` `<!-- ROW_MINE: linux-smp.messages.1572745 -->` `<!-- ROW_MINE: linux-smp.messages.1572746 -->` `<!-- ROW_MINE: linux-smp.messages.1572748 -->` `<!-- ROW_MINE: linux-smp.messages.1572755 -->` `<!-- ROW_MINE: linux-smp.messages.1572757 -->` `<!-- ROW_MINE: linux-smp.messages.1572764 -->` `<!-- ROW_MINE: linux-smp.messages.1572765 -->` `<!-- ROW_MINE: linux-smp.messages.1572766 -->` `<!-- ROW_MINE: linux-smp.messages.1572769 -->` `<!-- ROW_MINE: linux-smp.messages.1572775 -->` `<!-- ROW_MINE: linux-smp.messages.1572780 -->` 

**史观**：多方平等（总纲第 8 条——本体论上各方平等：意大利、德国、瑞典、南非等十四例并置）；偶然性优先（总纲第 5 条——没有必然性，只有偶然性：报料由内核提示语要求回信触发）
**辨析**：十四例均为用户自述，机型与版本以各自转储为准；本块只登记报料分布，不推断 VIA 系平台的共性缺陷。
**文献**：DSLXC-4706、DSLXC-4707、DSLXC-4709、DSLXC-4711、DSLXC-4712、DSLXC-4714、DSLXC-4721、DSLXC-4723、DSLXC-4729、DSLXC-4730、DSLXC-4731、DSLXC-4734、DSLXC-4740、DSLXC-4744（`linux-smp.messages.1572740`、`linux-smp.messages.1572741`、`linux-smp.messages.1572743`、`linux-smp.messages.1572745`、`linux-smp.messages.1572746`、`linux-smp.messages.1572748`、`linux-smp.messages.1572755`、`linux-smp.messages.1572757`、`linux-smp.messages.1572764`、`linux-smp.messages.1572765`、`linux-smp.messages.1572766`、`linux-smp.messages.1572769`、`linux-smp.messages.1572775`、`linux-smp.messages.1572780`，2002-12-16、2003-04-15、2002-12-17、2002-07-17、2002-11-16、2005-01-31、2002-10-06、2002-10-14、2003-05-08、2003-02-13、2005-06-17、2003-05-02、2004-04-07、2003-02-23），全文见 `raw_source.raw_json`

## 21.3 【Linux社区】寄存器 #02 残值序列（5 例）

**要点（判定表逐字）**：Daniel Stadnyckyj（2003-08-07）：**Intel D865GBF** 2.4.20-64GB-SMP 双 P4 3.0 HT——**register #02: 00178020** + onboard sound 装不上——D865GBF 系 #02 残值样本；Renee Trisberg（2003-11-20，爱沙尼亚）：**v20 + register #02: 00178020 + Promise FastTrak TX4000 RAID1**——#02 残值样本（正文完整 dmesg）；Bruno Barão（2003-06-21，葡萄牙）：2.4.21 报告——**IO-APIC #1 v20 + register #02: 00178020**（IO-APIC 编号 1 形态的 #02 残值）——残值序列样本；Russ McCallister（2004-01-11）：**SuSE 9.0 Pro 2.4.21-166-smp4G 在线更新后报料（双 P4 2.6 HT）**——v20 + #02 残值 +“I am keeping a copy in the event you should need it”——礼貌报料样本；Jacques Basson（2005-05-04，南非）：**SiS 661（v14 + register #02: 02000000）双 CPU**——v14 #02 残值样本（正文完整含 SiS900/USB 全套）

**史料**：`1572742`、`1572750`、`1572770`、`1572774`、`1572783`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572742 -->` `<!-- ROW_MINE: linux-smp.messages.1572750 -->` `<!-- ROW_MINE: linux-smp.messages.1572770 -->` `<!-- ROW_MINE: linux-smp.messages.1572774 -->` `<!-- ROW_MINE: linux-smp.messages.1572783 -->` 

**史观**：经验优先（总纲第 9 条——经验优先：以 D865GBF、SiS 661 等机型的 #02 实测残值（00178020／02000000）为判据）
**辨析**：五例残值同值者众，但均为个别转储，不构成 #02 语义的充分证据；本块保留“残值序列”的登记性质。
**文献**：DSLXC-4708、DSLXC-4716、DSLXC-4735、DSLXC-4739、DSLXC-4747（`linux-smp.messages.1572742`、`linux-smp.messages.1572750`、`linux-smp.messages.1572770`、`linux-smp.messages.1572774`、`linux-smp.messages.1572783`，2003-08-07、2003-11-20、2003-06-21、2004-01-11、2005-05-04），全文见 `raw_source.raw_json`

## 21.4 【Linux社区】大平台与机构报料（5 例）

**要点（判定表逐字）**：Adam Thomas（2003-10-06，NIH/NIMH 功能 MRI 设施）：**Qualstar 5433 磁带库**接入后 SMP 内核（2.4.18-2.4.20）警告——设备关联报料（国家卫生研究院样本）；Bob Schuknecht（2003-03-10，Hilton）：**IBM CRUSADER SMP 4×Xeon MP 1.5（2.4.9-e.3smp）——IO-APIC #14 51 redirection entries + Unknown CPU [15:2] + EBDA 警告 + bad pte 7f0ef163**——Xeon MP 大平台完整转储；root@swri（2002-08-23，西南研究院）：**Dell WS 530 双 Xeon 1.8（2.4.7-10enterprise）Unknown CPU [15:2] 双警告**——机构报料样本；Do Duc Huy（2003-10-31，越南河内 CDiT）：**IBM Netfinity 5500 RH7.3 2.4.20 EBDA 警告**——“Is this kernel OK for my system? Can you give me some advise about what kernel should use”——EBDA 求安心咨询；Craig Nelson（2003-09-13，加拿大 Cameo Systems）：报料+**onboard sound 故障是否与警告关联之问**（dmesg 附件）——“this looks like CPU stuff to me”——关联误判样本

**史料**：`1572738`、`1572776`、`1572777`、`1572778`、`1572782`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572738 -->` `<!-- ROW_MINE: linux-smp.messages.1572776 -->` `<!-- ROW_MINE: linux-smp.messages.1572777 -->` `<!-- ROW_MINE: linux-smp.messages.1572778 -->` `<!-- ROW_MINE: linux-smp.messages.1572782 -->` 

**史观**：经验优先（总纲第 9 条——经验优先：以 NIH、西南研究院、Hilton 等机构的完整转储为判据）；多方平等（总纲第 8 条——本体论上各方平等：机构报料者与维护者的问答地位平等）
**辨析**：五例中“onboard sound 故障是否与警告关联”系用户猜测，本页无维护者闭环；落书须保留其误判可能。
**文献**：DSLXC-4704、DSLXC-4741、DSLXC-4742、DSLXC-4743、DSLXC-4746（`linux-smp.messages.1572738`、`linux-smp.messages.1572776`、`linux-smp.messages.1572777`、`linux-smp.messages.1572778`、`linux-smp.messages.1572782`，2003-10-06、2003-03-10、2002-08-23、2003-10-31、2003-09-13），全文见 `raw_source.raw_json`

## 21.5 【Linux社区】平台兼容与民间 hack（7 例）

**要点（判定表逐字）**：German Gomez Garcia（2003-03-19，piraos）：Tyan S2460 + PCI-PCMCIA 适配器“Probably buggy MP table”无 IRQ——**“I/O APIC: AMD Errata #22 may be present. In the event of instability try: booting with the 'noapic' option”内核提示语第一手**；**Andrew Grover（2003-05-22，Intel ACPI 维护者）**答 Gantner（A7M266-D BIOS 1010，2.5.69-mm5）：**“Small ACPI AML error. I wouldn't worry about it.”**——ACPI 维护者一手定调；henk（2003-06-14，荷兰）：**“If ACPI is enabled the USB drivers don't get an interrupt line assigned”**——ACPI 启用下 USB IRQ 缺失（v3 警告+Duron）；Lists/Cosmin（2002-07-09，罗马尼亚 LAPD）：**Tyan Tiger 200T 双 Coppermine——MPS1.1+noapic 仍有 APIC errors 致网卡掉线（Intel 82559+Tulip）**；且“after 3 days of tests it seems that the one CPU it was broken”——坏 CPU 定位（p23 013 同线程续）；Nils Boysen（2003-04-16，德国）：**Elitegroup L7VTA——板载硬件全不工作疑中断分配**（非 SMP，dmesg 附件）——主板点名咨询；Mauricio Girardi（2002-09-11）：**“a short circuit in the L5 jumper of the XP Polomino processors that made then recognizable as MP processor”传说 +“Duron processors also can works with SMP”**——XP→MP 跳线 hack 民间传闻一手；Frank von Daak（2006-04-05）：**Abit NI8 SLI（nForce4）双核只认 1 核原帖**——`append="pci=noacpi pci=routeirq noapic acpi=off"` 才见双核但不稳（glxgears 必崩）——p28 006 的原帖（跨页对）

**史料**：`1572744`、`1572747`、`1572760`、`1572771`、`1572772`、`1572773`、`1572785`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572744 -->` `<!-- ROW_MINE: linux-smp.messages.1572747 -->` `<!-- ROW_MINE: linux-smp.messages.1572760 -->` `<!-- ROW_MINE: linux-smp.messages.1572771 -->` `<!-- ROW_MINE: linux-smp.messages.1572772 -->` `<!-- ROW_MINE: linux-smp.messages.1572773 -->` `<!-- ROW_MINE: linux-smp.messages.1572785 -->` 

**史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 noapic、MPS1.1 与跳线 hack 等实际操作路径为分析单位）；偶然性优先（总纲第 5 条——没有必然性，只有偶然性：兼容性结论由各板具体布线差异反推）
**辨析**：XP→MP 跳线传闻系当事人转述，本页无电气层面佐证；AMD Errata #22 提示语为内核原文，落书须与源码核对。
**文献**：DSLXC-4710、DSLXC-4713、DSLXC-4726、DSLXC-4736、DSLXC-4737、DSLXC-4738、DSLXC-4749（`linux-smp.messages.1572744`、`linux-smp.messages.1572747`、`linux-smp.messages.1572760`、`linux-smp.messages.1572771`、`linux-smp.messages.1572772`、`linux-smp.messages.1572773`、`linux-smp.messages.1572785`，2003-03-19、2003-05-22、2003-06-14、2002-07-09、2003-04-16、2002-09-11、2006-04-05），全文见 `raw_source.raw_json`

## 21.6 【Linux社区】HT 支持演进（3 例）

**要点（判定表逐字）**：Mihai Burcea（2002-10-02，多伦多大学）：**PE6600 8 Xeon HT——2.4.18-4smp 识别 8 CPU，2.5.38 只识别 4 CPU + 每 CPU“Sibling not found”警告**——2.5 早期 HT 支持缺失实录（与 p22 PE6600 块同族）；Mihai Burcea（2002-11-25）答 Cox：**“The scheduler doesnt have good awareness of HT handling right now. There were some test patches in 2.4-ac but I pulled them due to crashes”**（Cox 语）→ 问 2.5（2.5.38/39/41 均不正常）——HT 调度器意识演进（2.4-ac 测试补丁被撤一手）；Barry Gamblin（2003-03-07，UCAR/HAO）：**P4DC6 双 Xeon 1.7 开 HT 之问——“The closest BIOS setting I can find is 'CPU FastStrings'...hyperthreading is disabled and only two CPUs show up”**——HT 启用 BIOS 谜题

**史料**：`1572753`、`1572759`、`1572768`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572753 -->` `<!-- ROW_MINE: linux-smp.messages.1572759 -->` `<!-- ROW_MINE: linux-smp.messages.1572768 -->` 

**史观**：知识注定过时（总纲第 22 条——知识注定过时：2.4-ac 的 HT 测试补丁因崩溃被撤，支持状态随版本更替）；经验优先（总纲第 9 条——经验优先：以 2.4.18 识别 8 CPU 而 2.5.38 只识别 4 CPU 等实测对照为判据）
**辨析**：Cox 语系当事人转述（“I pulled them due to crashes”）；本块不据此断言 HT 支持的时间线，须以各版本实际行为为准。
**文献**：DSLXC-4719、DSLXC-4725、DSLXC-4733（`linux-smp.messages.1572753`、`linux-smp.messages.1572759`、`linux-smp.messages.1572768`，2002-10-02、2002-11-25、2003-03-07），全文见 `raw_source.raw_json`

## 21.7 【Linux社区】本地定时器单核化实验

**要点（判定表逐字）**：Klaas Zweck（2002-04-17，不来梅）：**“timer on just one cpu”实验——ServerWorks 双 PIII，在 setup_local_APIC() 对非 boot CPU 置 APIC_LVT_MASKED 无效，clear_local_APIC() 亦无效**——本地定时器单核化代码级实验

**史料**：`1572756`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572756 -->` 

**史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 setup_local_APIC 与 clear_local_APIC 的代码级实验为唯一证据源）；经验优先（总纲第 9 条——经验优先：以两处置位均无效这一实测结果为判据）
**辨析**：本块为单例代码实验，其失败结论仅限所述 ServerWorks 双 PIII 环境；未附补丁或上游结论。
**文献**：DSLXC-4722（`linux-smp.messages.1572756`，2002-04-17），全文见 `raw_source.raw_json`

## 21.8 【Linux社区】驱动与同步（5 例）

**要点（判定表逐字）**：Pedro Pla（2002-10-30）：**GDT 线程原帖——Intel SCB2 + SCRMR RAID5 + 1-2GB RAM，signal 11/mem_alloc.c:89 oops（2.4.17-2.4.20-pre11 全系列+2.2.22），换板同症；“memtest86 v3 无错而 2.8 报错”**——p24 026/p26 034 的原帖（跨页三部曲之首）；Tony Battersby（2003-05-27）：**flush_tlb_all_ipi() SMP lockup 结案——驱动持 io_request_lock 调 ioremap/iounmap**（Cox：“error path freeing an io mapping with a lock held...a scsi driver bug not an SMP bug”）——锁内 ioremap 定位结案；Pedro Pla（2002-10-30）：GDT 线程续——**vanilla 2.4.19 无 SMP 可启动；SMP 内核+nosmp/disableapic 冻结 oops 内存分配错（加载 SCSI 时）**——GDT/SMP 线索定位；**David Brownell（2002-08-24，USB 子系统维护者）**：**2.5.31-bk6 VIA KT333/VT8235——“an earlier SMP config didn't handle any of the USB IRQs right; they seem to have been routed wrong (to irq5+irq11, not irq19+irq21)”+“the BIOS says it's a not-for-sale demo”+ 批评单 CPU 无 mp flag 也标 SMP tainted（“I just want spinlock bugs to get reported”）**——USB IRQ 路由错位与 tainted 语义批评；Pedro Pla（2002-11-07）：GDT 线程续——**Ishikawa 建议试 RedHat 认证版/减内存/换 OS 诊断（Solaris x86/NT）；“I think the problem is in the dma, since it only occurs when moving files from disk. I know the serverworks ide dma is flakey...how could that affect the gdt (scrmr) scsi? Or is it related?”**——ServerWorks DMA 怀疑（GDT 线程诊断方法论）

**史料**：`1572752`、`1572754`、`1572767`、`1572786`、`1572787`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572752 -->` `<!-- ROW_MINE: linux-smp.messages.1572754 -->` `<!-- ROW_MINE: linux-smp.messages.1572767 -->` `<!-- ROW_MINE: linux-smp.messages.1572786 -->` `<!-- ROW_MINE: linux-smp.messages.1572787 -->` 

**史观**：经验优先（总纲第 9 条——经验优先：以 memtest86 两版结果差异、io_request_lock 内 ioremap 定位、USB IRQ 路由错位等实测为判据）；动手者叙事（总纲第 10 条——动手者创造历史：以 GDT 线程的多轮诊断路径为分析单位）
**辨析**：GDT 线程三封为同一用户的连续诊断，其 DMA 怀疑未获闭环；Brownell 的 tainted 语义批评为维护者立场，非规则文本。
**文献**：DSLXC-4718、DSLXC-4720、DSLXC-4732、DSLXC-4750、DSLXC-4751（`linux-smp.messages.1572752`、`linux-smp.messages.1572754`、`linux-smp.messages.1572767`、`linux-smp.messages.1572786`、`linux-smp.messages.1572787`，2002-10-30、2003-05-27、2002-10-30、2002-08-24、2002-11-07），全文见 `raw_source.raw_json`

## 21.9 【Linux社区】崩溃与硬件怀疑（3 例）

**要点（判定表逐字）**：Zwane（2003-03-07）答 Huhn（spinlock 线程续）：**“Some of these are a bit worrying seeing as they are bit flips, also they all appear to come from a UP machine(?)”+ NFS soft 选项之问**——位翻转硬件归因；Hector M Sanchez M（2003-06-12，智利）：**IBM 双 Xeon 2G 2GB RAM 2.4.18-686-smp 邮件服务器无故 hang（连 ls 都不响应）**——生产服务器锁死（机翻英语信）；Phil White（2004-02-25）：**Tyan Thunderbolt（440GX）双 Coppermine——2.4.22/2.6.3/2.6.3-gentoo 均在 booting CPU 1 时 bad paging request（do_page_fault），noapic 有改善（变为 spurious interrupts）**——引导期 oops 对照实验（与 p23 008 同人）

**史料**：`1572749`、`1572762`、`1572781`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572749 -->` `<!-- ROW_MINE: linux-smp.messages.1572762 -->` `<!-- ROW_MINE: linux-smp.messages.1572781 -->` 

**史观**：经验优先（总纲第 9 条——经验优先：以位翻转观察、noapic 后症状变化等实测为判据）；多方平等（总纲第 8 条——本体论上各方平等：软件归因与硬件归因两说并置）
**辨析**：位翻转归因与引导期 oops 均未见最终裁定；本块只登记现象与对照实验，不写成因果结论。
**文献**：DSLXC-4715、DSLXC-4727、DSLXC-4745（`linux-smp.messages.1572749`、`linux-smp.messages.1572762`、`linux-smp.messages.1572781`，2003-03-07、2003-06-12、2004-02-25），全文见 `raw_source.raw_json`

## 21.10 【Linux社区】社区机制与热敏（3 例）

**要点（判定表逐字）**：Deepak Kumar Gupta（2003-02-17，HCL Tech 印度）：**NMI watchdog 是否需专用硬件卡之问**+引“回形针短接 ISA 总线 A1-B1 生成 NMI”传说链接——NMI 硬件认知误区样本；Jigar Raval（2006-09-05）：**“I received your mail but ONLY with the message which I have sent. NOT YOUR REPLY. I have also got the returned mail...user unknown”**——Davidsen 回复被 vger 退信——邮件基础设施故障样本（与 Bogofilter 误杀疑云呼应）；cerise/Phil White（2006-05-05）答 Hyatt（FC4 vs SuSE 差异）：**“That might be because SuSE's compiled kernel doesn't use mce...looking for CONFIG_X86_MCE=y. That would nicely explain the discrepancy. 8)”**——MCE 配置差异假说

**史料**：`1572739`、`1572751`、`1572763`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572739 -->` `<!-- ROW_MINE: linux-smp.messages.1572751 -->` `<!-- ROW_MINE: linux-smp.messages.1572763 -->` 

**史观**：偶然性优先（总纲第 5 条——没有必然性，只有偶然性：vger 退信与 MCE 配置差异均由具体故障暴露）；多方平等（总纲第 8 条——本体论上各方平等：社区机制故障与硬件认知误区并置）
**辨析**：“回形针短接生成 NMI”为当事人转引的传说链接，本块只作存录；MCE 配置差异系假说，须以发行版内核 config 核对。
**文献**：DSLXC-4705、DSLXC-4717、DSLXC-4728（`linux-smp.messages.1572739`、`linux-smp.messages.1572751`、`linux-smp.messages.1572763`，2003-02-17、2006-09-05、2006-05-05），全文见 `raw_source.raw_json`

---
注：本文件由判定表程序化生成（21.1-21.10 共 10 块，覆盖 48/48 CAND，两遍计数核对通过）；要点逐字取自判定表“要点”列（主代理全读审读实录），史料锚与 CAND 一一对应，全文以 raw_source.raw_json 为准。
