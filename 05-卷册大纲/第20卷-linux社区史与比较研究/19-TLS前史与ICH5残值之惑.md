# 19-TLS前史与ICH5残值之惑.md

> 对应页面：linux-smp p27（pk 1572638-1572687，2002-2008 为主 + 2015 一封）
> 判定：48 CAND / 2 NV（006 dmesg 附件转交、031 空正文）
> 编号：DSLXC-4607..4654 | claim 已入库（48/48，dslinux_claims.duckdb）

## 19.1 【Linux社区】ICH5 残值之惑与寄存器序列研究（5 例）

**要点（判定表逐字）**：Randy Dunlap（2003-05-27）答 Mattias Kregert（Abit IC7 875P+ICH5R 单 P4 2.4）：**「The Intel 82801EB (ICH5) datasheet does not specify that this chipset has a register 2 for the IO APIC. We need to find a way to recognize this and ignore reg. 02 (a way other than register 1's IO APIC version value, which is currently being used).」**——ICH5 #01=#02=00178020 之惑的研究一手（寄存器#02 残值序列的方法论线索）；M. J. Blom（2003-07-18，荷兰）：v20 + **register #02: 00178020**——「I bet you want the IO APIC#2 stuff (I, unfortunally, have no clue what all this is)」——#02 残值样本；Gregory McLean（2003-08-20，gxsnmp.org）：**Intel D865PERL** boot log——**register #02: 00178020**——D865PERL #02 残值样本（p21 三例之后的又一例）；Eric C. Cooper（2003-08-26，CMU）：ASUS P4S8X 2.4.22——**IO-APIC version 0080 + register #03 Boot DT: 1**（ACPI MADT version 128）——v0x80 样本再添（与 p25 001 同族）；William Tuynman（2008-02-06，NASA JSC）：**HP Proliant DL585 双核 Opteron 跑 32 位 2.4.36.SMPx**——unexpected IO-APIC（2.4.34 亦有），messages 正文完整（多 IO-APIC/ACPI XSDT+SRAT/LAPIC disabled 项）——NASA 机构与 32 位内核跑 Opteron 样本

**史料**：`1572639、`1572652、`1572655、`1572662、`1572679

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572639 -->` `<!-- ROW_MINE: linux-smp.messages.1572652 -->` `<!-- ROW_MINE: linux-smp.messages.1572655 -->` `<!-- ROW_MINE: linux-smp.messages.1572662 -->` `<!-- ROW_MINE: linux-smp.messages.1572679 -->` 

## 19.2 【Linux社区】报料全景（12 例）

**要点（判定表逐字）**：Dayanand Patil（2003-03-27，Cadence 印度）：RH7.2 2.4.9-34smp IO-APIC #3 v20 警告 + agpgart 2531 不支持 + mtrr type mismatch——报料样本；Ross Dickson（2002-11-18，澳洲）：ASUS A7V333（KT333+VT8233A，BIOS 1014）单 XP2100+ 2.4.19-SUSE v2 警告 + ACPI IOAPIC 路由 +「PCI BIOS passed nonexistent PCI bus 0!」十一连——**「I am a programmer and can patch my source tree to test」**志愿样本；Marc Dierikx（2002-12-27，荷兰）：**2.5.50** 单 P4 2.66（SiS648）——v14 警告（register #02: 02000000）+「CPU#0: Thermal monitoring enabled」——2.5 系早期样本；Craig O'Shannessy（2003-06-14，澳洲）：ABit IC7-G 2.8 HT P4 警告——「Should I turn of APIC?...it's hard to even figure out what linux APIC even does」——APIC 教育缺口之叹；Vladimir（2002-05-09）答 Singleton（p24 043 的回复）：**「Allegedly not. It merely means that your motherboard is not recognized as being OK.」**+ 双 CPU interrupts 均衡范例表——警告非致命定调（跨页对）；Alan Cox（2002-07-10）答 Weinehall：**「What chipset is this beast ?」**——著名芯片组问句的源头（p23 037 答 VIA KT266A/GA-7VTXH 之问，跨页对）；a.mintgen（2005-07-12，德国）：警告报料（VIA 3177）——只贴警告下方日志（正与 p24 034 Dunlap「应贴上方日志」回复对应）——报料位次标本；Chris McGinlay（2002-08-10，苏格兰）：v20 警告转储（正文含，双 WARNING）——样本；Colin Bayer（2002-12-17）：Athlon MP 2100+/Albatron KX400-8X（KT400）2.4.20-ac2 警告（dmesg 附件）——报料点名；Alan Cox（2003-04-29）答 Rahul Patel（Lehman，AS2.1 e12）：**「AS 2.1 is based on Linux 2.4.9. It doesn't know a lot of the newer APIC identifiers. Talk to Red Hat.」**——发行版内核 APIC 识别滞后定调与厂商转介；Daniel Bergman（2003-04-19，瑞典）：gentoo 2.4.20-r2 v3 警告转储（正文含）——样本；Eskil Heyn Olsen（2002-07-26，Neoteris）：E7500 双 Xeon 2.4.18 警告——**「the kernel seems to work fine」**自答——良性自证样本

**史料**：`1572638、`1572640、`1572647、`1572650、`1572651、`1572653、`1572656、`1572670、`1572677、`1572682、`1572683、`1572685

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572638 -->` `<!-- ROW_MINE: linux-smp.messages.1572640 -->` `<!-- ROW_MINE: linux-smp.messages.1572647 -->` `<!-- ROW_MINE: linux-smp.messages.1572650 -->` `<!-- ROW_MINE: linux-smp.messages.1572651 -->` `<!-- ROW_MINE: linux-smp.messages.1572653 -->` `<!-- ROW_MINE: linux-smp.messages.1572656 -->` `<!-- ROW_MINE: linux-smp.messages.1572670 -->` `<!-- ROW_MINE: linux-smp.messages.1572677 -->` `<!-- ROW_MINE: linux-smp.messages.1572682 -->` `<!-- ROW_MINE: linux-smp.messages.1572683 -->` `<!-- ROW_MINE: linux-smp.messages.1572685 -->` 

## 19.3 【Linux社区】TLS 设计前史三部曲（Hyatt-Cox-Magallon）

**要点（判定表逐字）**：Robert Hyatt（2002-07-12）答 Magallon（per-thread global variables/IRIX PRDA 之问）：**crafty 方案——每线程一结构 + clone()（「since the glibc guys broke pthreads a while back」）**——TLS 前史一手；Alan Cox（2002-07-13）：**IRIX PRDA 批判——「A single unshared page means two separate mm structs, two sets of page tables and switches causing TLB flushes. All because movl %esp, %eax; andl $ffff8000, %eax and casting that is 'hard'」**——TLS 设计哲学一手（栈位与运算的优雅 vs 固定页）；Robert Hyatt（2002-07-13）答 Magallon（PRDA 之问续）：**「In the 'master thread' I define an array of structures, one per thread...Each thread _must_ have a stack (mine is 1mb per thread) and you have to (on intel) pass the _end_ address since stacks go backward」**——crafty 线程私数据实现细节（TLS 三部曲之二）

**史料**：`1572658、`1572659、`1572687

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572658 -->` `<!-- ROW_MINE: linux-smp.messages.1572659 -->` `<!-- ROW_MINE: linux-smp.messages.1572687 -->` 

## 19.4 【Linux社区】中断均衡与亲和性接口（2 例）

**要点（判定表逐字）**：Peter H. Koenig（2002-05-18，帕德博恩大学）：Hounschell irq_balance 补丁（疑 Ingo 作）实测——**eth0 IRQ 双 CPU 分配成功（502144/505080）但 timer/ide 仍全 CPU0**，求均衡方法——补丁效果与残余不均衡实录（与 p25 004 成对）；Arjan van de Ven（2008-07-20）答 Emil Medve（Freescale）[PATCH] Export irq_set_affinity()：**「how much of this is already covered by the 'don't balance' IRQ flag already?」**+ 要求示例驱动随补丁——导出补丁的评审质疑（与 p22 1572429 同线程）

**史料**：`1572648、`1572649

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572648 -->` `<!-- ROW_MINE: linux-smp.messages.1572649 -->` 

## 19.5 【Linux社区】崩溃与锁死（8 例）

**要点（判定表逐字）**：Ian Jackson（2003-05-12，chiark/Debian 著名开发者）：**2.4.20 双 PIII CUV-D 生产系统挂在 APIC timer 校准后**（CPU0<...> 行后数分钟），2.2.25 正常且同有警告；serial console+remote power cycler+完整两份 config——知名人物生产升级挂起档案；Robert Hyatt（2006-05-05）答 Davidsen/Szymanski（FC4 双核 Opteron 反复崩）：quad 875 双核 8 处理器跑 SuSE「running perfectly reliable」而 FC4 有问题（双 Xeon 机 FC4 正常）——发行版对比证词；Barry Gamblin（2003-02-10，UCAR/HAO）：**kernel BUG at page_alloc.c:130（__free_pages_ok）+「Page has mapping still set...if you are using the NVidia binary only module please report this bug to NVidia」提示语 + CPU1 + 周末多次锁死**——page_alloc BUG 二连与 NVidia 闭源提示语第一手（与 p23 033 :145 同族）；damo@nipponpaint.com.my（2003-03-28，马来西亚）：**IBM Xseries 335 RH8.0 冻结须重启**（messages 附件）——X335 冻结报料；Rolf Nigbur（2002-11-27，德国 IKK）：**2 台 Fujitsu-Siemens LT100 2.2.18-SMP 一台经常挂且 syslog 无痕，唯一差异 boot.msg APIC 错误**（boot.msg 附件）——同型机对照样本；Matt King（2003-02-03，Kietra）：**「My machine is randomly locking up (HARD...required power cycle)...could this be a problem?」**——警告与硬锁死关联之问；Joachim Wickman（2002-06-03，芬兰）：**ABIT-BP6 双 Celeron 433 2.4.18——约 3/4 概率启动崩在「udf: registering filesystem」**——BP6 启动崩样本（与 p26 037 BP6 呼应）；Lyle Worthington（2004-02-24，skylist）：**RH7.3 双 P4 3.2 Xeon 6GB bigmem——唯一报此问题的机 + 6 天崩 4 次**——三 IO-APIC、**#2 register #00: 02008000 残值** + buggy MP table——残值与崩溃并存

**史料**：`1572641、`1572642、`1572644、`1572665、`1572667、`1572672、`1572676、`1572684

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572641 -->` `<!-- ROW_MINE: linux-smp.messages.1572642 -->` `<!-- ROW_MINE: linux-smp.messages.1572644 -->` `<!-- ROW_MINE: linux-smp.messages.1572665 -->` `<!-- ROW_MINE: linux-smp.messages.1572667 -->` `<!-- ROW_MINE: linux-smp.messages.1572672 -->` `<!-- ROW_MINE: linux-smp.messages.1572676 -->` `<!-- ROW_MINE: linux-smp.messages.1572684 -->` 

## 19.6 【Linux社区】HT 定调与 noapic 结案（3 例）

**要点（判定表逐字）**：Alan Cox（2002-07-15）答 François Primeau（UCI，4 处理器实为 2 + 大矩阵求逆冻结无视频信号）：**「If your machine is a P4 Xeon then both the apic warning and the 4 processors are right」「The lack of video signal points more to hardware than software」**——HT 确认与硬件归因二连；Bernhard Lummer（2004-08-26，highyag.de）答 Urs Thuermann：**HT disabled（cpuid smp_num_siblings=1，「CPU: Hyper-Threading is disabled」）之问 + 转 LKML 2002/Dec/3261 链接**——HT 被禁（BIOS 层）诊断样本；Maurice（2004-08-10）：**「noapic 启动后 SMP 内核 IPv4 正常工作！！！」**（fedora-legacy 列表指点）——p25 011 IPv4 失效的 noapic 结案（跨页对）

**史料**：`1572669、`1572678、`1572680

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572669 -->` `<!-- ROW_MINE: linux-smp.messages.1572678 -->` `<!-- ROW_MINE: linux-smp.messages.1572680 -->` 

## 19.7 【Linux社区】平台兼容与硬件定位（7 例）

**要点（判定表逐字）**：Michal Szymanski（2006-05-09）：**换 Kingston 1GB 后 72 小时不崩**（Patriot 2GB 崩且在 Supermicro 推荐名单上），「I do not understand why the same memory crashes the machine in SMP and does not in non-SMP」——内存替换定位与 SMP/UP 内存敏感性悖论；Bill Davidsen（2006-09-04）答 Jigar Raval（IBM x365 NMI 面板错误+自动重启）：**「I had 38 of these machines, sounds like a hardware issue, not software. Look at the diagnostic logs at boot, run T&D」**——38 台 x365 运维经验一手；Matt Brei（2006-10-25）：**双 Athlon MP 1800+ 2.6.18.1 开 SMP 后 nbd closed socket/LVM No volume groups found 启动失败**——p24 042 Mouw 分诊的原帖（跨页对）；Bogusta（2002-07-09）反例：**「Some IBM Netfinity machines will have problems initializing the onboard SCSI controller if MPS 1.1 is selected. Each possible LUB of each possible device on each possible bus will be queried with a timeout. Booting takes a uselessly long time.」**——MPS 1.1 的 Netfinity 启动代价（与 CUV4X MPS-only 处方对照）；Frank von Daak（2006-04-05）：**Abit NI8 双核 + 双 nVidia PCIe SLI 桥（不用 SLI）三显示器**——IRQ7 XT-PIC 共享（ohci_hcd+nvidia+nvidia）、「I can use just on one cpu-core :-(」「whats my problem? SMP or Nvidia?」——SLI 桥 IRQ 共享单核可用之惑；John Birck（2003-09-12，Baader 银行）：**IBM x445 8870-1RX 4×Xeon 2G 16GB——自结「one of the qla was defect」**（QLogic 2312 缺陷硬件）——大平台警告的硬件结案（与 p26 045 T850 呼应）；Alan Cox（2003-05-17）答 blondel（Athlon-MP 问题）：**「This still all sounds like an overheating machine」+ ACPI 与 amd76x_pm 同跑「They fall over each other」+ 760MP/MPX「all very much of the same thing」+ MTRR 不一致与 cpuinfo 双名系 BIOS 无害**——四连裁定合集

**史料**：`1572645、`1572661、`1572663、`1572666、`1572673、`1572674、`1572686

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572645 -->` `<!-- ROW_MINE: linux-smp.messages.1572661 -->` `<!-- ROW_MINE: linux-smp.messages.1572663 -->` `<!-- ROW_MINE: linux-smp.messages.1572666 -->` `<!-- ROW_MINE: linux-smp.messages.1572673 -->` `<!-- ROW_MINE: linux-smp.messages.1572674 -->` `<!-- ROW_MINE: linux-smp.messages.1572686 -->` 

## 19.8 【Linux社区】调度与社区机制（4 例）

**要点（判定表逐字）**：Maxwell Spangler（2002-04-14）答 Michon：**「The linux-smp list was active when SMP issues needed discussion because the code and the hardware was less mature. These days both code and hardware have matured and most notable issues effecting SMP are discussed here (LKML)」**——列表演进史关键一手 + Tyan S2466N 760MPX 配置与 Athlon MP retail 建议；Chinmay V S（2015-09-07）：**RT Scheduler BUG_ON (idx >= MAX_RT_PRIO)** 复现需 2 天——3.2 RT 树 futex 17 补丁缺失审计 + CONFIG_CC_STACKPROTECTOR/STRICT_DEVMEM 排除 + 求 debug 机制建议——RT 调度器长跑复现方法论；Randy Dunlap（2006-02-16）答 chekuri（Toshiba L25-S119 新手）：**「The message and your network card not working are not related.」**+ 转介 linux-pcmcia + lspci/dmesg 要素——脱钩分诊与跨列表转介；Bruce M Beach（2002-08-11，中山大学）：答 Horwitt（p23 027 SMP puzzle）：**「I have been using system builds as fodder to feed the CPU's and have seen increases from 10% to 58% depending how the jobs are scheduled」**——内核编译基准缩放数据

**史料**：`1572646、`1572657、`1572671、`1572681

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572646 -->` `<!-- ROW_MINE: linux-smp.messages.1572657 -->` `<!-- ROW_MINE: linux-smp.messages.1572671 -->` `<!-- ROW_MINE: linux-smp.messages.1572681 -->` 

## 19.9 【Linux社区】文档与驱动（3 例）

**要点（判定表逐字）**：Simon Oliver（2002-07-03）：**User address space size 语义之问**（3.5GB/0.5GB vs 3GB/1GB vs 2GB/2GB split，引 kernel help 原文逐段求证 2GB 机的 high/user 分布）——内核/user 内存切分配置教学样本（p23 004 后续）；karl wettin（2004-07-13，瑞典）：**madwifi 不支持 SMP**——「iwconfig can't find any wireless extentions on athX when SMP is running. This is a known problem rather than a hardware incompabillity」——madwifi SMP 已知问题一手；Matthew Singer（2005-05-14）：**SMP 双路 2GB mem=1984M + ioremap(0x7c000000, 0x4000000) 后访问 OOPS，UP 正常**——「is this an SMP issue regarding how memory in each node is mapped?」——ioremap 大 DMA 缓冲 SMP 映射之问

**史料**：`1572660、`1572654、`1572675

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572660 -->` `<!-- ROW_MINE: linux-smp.messages.1572654 -->` `<!-- ROW_MINE: linux-smp.messages.1572675 -->` 

## 19.10 【Linux社区】EBDA 关联咨询

**要点（判定表逐字）**：D.Krishna Rao（2003-12-18，NIC Hyderabad）：2.4.9-e.3enterprise 双 P4 Xeon（4 logical 检出）+ **EBDA 警告 + 系统 hang** 求解——EBDA 关联挂起咨询（印度政府机构样本）

**史料**：`1572664

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572664 -->` 

---
注：本文件由判定表程序化生成（19.1-19.10 共 10 块，覆盖 48/48 CAND，两遍计数核对通过）；要点逐字取自判定表「要点」列（主代理全读审读实录，含 MSG 042 大转储段补读），史料锚与 CAND 一一对应，全文以 raw_source.raw_json 为准。
