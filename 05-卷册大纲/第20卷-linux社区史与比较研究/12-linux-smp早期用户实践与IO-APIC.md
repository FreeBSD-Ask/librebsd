# 12 【Linux社区】linux-smp早期用户实践与IO-APIC

> 对应页面：linux-smp p20（pk 1572288-1572337，2002-2007 为主，2021 讨论 2 封）
> 判定：48 CAND / 2 NV（007 纯附件引述、020 纯退订信）
> 编号：DSLXC-4281..4328 | claim 已入库（48/48，dslinux_claims.duckdb）

## 12.1 【Linux社区】unexpected IO-APIC 报料潮与警告闭环

**要点**：root@salbohomes（2002-06-12）：2.4.9-31smp 双 PIII Coppermine unexpected IO-APIC 报告——完整 dmesg（VIA vt82c686b、PDC20265 RAID 模式、Via external APIC routing）；mtrr 变量设置不一致=BIOS 未在所有 CPU 上设置；apm 以“非 SMP 安全”被禁；Clifford Thurber（2004-09-13）：HP DL760 8 Xeon、RH AS3 + 自制 2.6.7、BIOS 禁 HT——启动时反复 kernel BUG at include/asm-i386/mach-summit/mach_apic.h:63（setup_local_APIC+0x17f）+ panic 杀 idle task；CPU #4/6/8/10/12/14 依次 not responding、每次 Booting processor 4/N 循环；最终 Total of 4 processors activated——Summit 平台 mach_apic 硬编码断言崩在 8 路 DL760；William E. Butler（2003-04-08）：启动时见 APIC error 提示按内核指示寄全 dmesg，“大概已知问题、最新内核已修”FYI——unexpected IO-APIC 报料闭环的常规样本；franck Jolimay（2002-12-18）：RH7.2 服务器重启见“WARNING: unexpected IO-APIC, please mail”——按提示来函问含义与对策；生产 DBA 视角的警告处理流程；Bailey Bret（2003-09-16）：新购机（win2000+Mandrake 双系统 40GB）IO APIC #2 register 转储——physical APIC id 02、max redirection 0017、PRQ 1、version 0003 触发 unexpected 警告；按内核指示寄 syslog 全文求反馈；Milan Kerslager（2003-04-10）：RH9 kernel-smp-2.4.20-9（RHN 更新）Intel SE7500CW2 双 Xeon HT——三 IO-APIC（#2/#3/#4）完整转储：#3/#4 全 pin 未连接、IRQ redirection 表逐项寄出；lspci 证实 e7500 [Plumas] + 双 P64H2 I/OxAPIC（82870P2）——芯片组级三 IO-APIC 拓扑存档；Andy Figueroa（2003-02-18）：E-Machine 升 Mandrake 9.0 dmesg 提示寄 APIC 信息——完整 boot log（Athlon XP 1600+、Advanced speculative caching 禁用、VIA vt8233a UDMA133、警告 IO-APIC version 0002）；无 IRQ 重定向表的自述信；Thomas Römer（2003-02-28）：按内核提示寄 SuSE boot.msg 全文——2.4.18-64GB-SMP、VIA VT5440B MP 表、Athlon XP 1800+、unexpected IO-APIC 警告（version 0003）；附问 ac97 声卡不工作是否 ACPI 问题、自述从 MSI MS6341 换 MS6712 主板在测；Andreas Schenk（2006-03-18）：SuSE 9.0 内核 2.4.21-273-smp4G——“内核已超三月仍敢寄报”，自谦不懂细节但略知 APIC；IO APIC #2 register 转储（version 0020、arbitration 00）触发 unexpected 警告；求反馈与解释链接；Ian Brandt（2005-10-24）：Appro 1124s（Tyan Thunder K7 S2462、双 Athlon MP 1600、760MP、Adaptec 2100S）升 2.6.13 偶发启动挂死——挂点在“I/O APIC: AMD Errata #22 may be present. …try booting with noapic”但该行成功启动也有；问 noapic 实际性能损失、pirq= 手工构造 IRQ 是否值得、如何帮压 bug；附完整 dmesg（Dual Athlon MP stepping 02、TSC 同步 passed、balanced_irq）；David Boulware（2005-04-26）：Dell Dimension 4700 装 Debian 2.4.17/2.4.18 失败——PCI 设备全找不到；IO APIC #8 转储（physical APIC id 08、PRQ 0、version 0020）触发警告；每秒一次“ide2: unexpected interrupt, status=0xd0”；疑内核参数未设；Jeff Frost（2003-01-03）：IBM 服务器 unexpected IO-APIC 报告——IO APIC #14（physical APIC id 0E、max redirection 0032、version 0011、PRQ 0）+ IO APIC #13（0D）双转储与全 IRQ redirection 表；按警告指示寄达；Paul Hernandez（2002-10-09）：SuSE 8.0 Pro + Intel 服务器主板 SE7500CW2——按警告寄 dmesg（正文仅声明，无正文转储）——CW2 板 IO-APIC 报告的另一实例（与 022 Kerslager 同板对照）；Stephen Woodbridge（2004-05-19）：2.4.18-bf2.4 Debian SiS 板（SiS5513 IDE、8139too、3ware 400GB 阵列）完整 klogd 转储——“WARNING: unexpected IO-APIC, please mail”触发；hm page reserved twice ×4、IO APIC #2（version 0014、PRQ 1）全寄存器与 IRQ redirection 表、PCI->APIC IRQ transform 列表；信息完整的用户侧报料范本；Phillip Gardner（2003-09-02）：“Per a request from my kernel”按启动提示寄 IO APIC #2 转储（version 0003、PRQ 1）+ 全 IRQ redirection 表；报料闭环的自动化样本；Bernd Schubert（2003-12-09）：Tyan Thunder K8S（S2880）单 Opteron——2.4.23 报 unexpected IO-APIC，BIOS 升级前同样配置无此消息；“请 cc 我，未订阅本列表”——BIOS 升级改变 APIC 行为与旧内核检测的冲突样本

**史料**：`1572299`、`1572300`、`1572301`、`1572305`、`1572308`、`1572309`、`1572311`、`1572313`、`1572314`、`1572315`、`1572317`、`1572320`、`1572322`、`1572324`、`1572325`、`1572334`

**史料锚**：`<!-- ROW_MINE: linux-smp.messages.1572299 -->` `<!-- ROW_MINE: linux-smp.messages.1572300 -->` `<!-- ROW_MINE: linux-smp.messages.1572301 -->` `<!-- ROW_MINE: linux-smp.messages.1572305 -->` `<!-- ROW_MINE: linux-smp.messages.1572308 -->` `<!-- ROW_MINE: linux-smp.messages.1572309 -->` `<!-- ROW_MINE: linux-smp.messages.1572311 -->` `<!-- ROW_MINE: linux-smp.messages.1572313 -->` `<!-- ROW_MINE: linux-smp.messages.1572314 -->` `<!-- ROW_MINE: linux-smp.messages.1572315 -->` `<!-- ROW_MINE: linux-smp.messages.1572317 -->` `<!-- ROW_MINE: linux-smp.messages.1572320 -->` `<!-- ROW_MINE: linux-smp.messages.1572322 -->` `<!-- ROW_MINE: linux-smp.messages.1572324 -->` `<!-- ROW_MINE: linux-smp.messages.1572325 -->` `<!-- ROW_MINE: linux-smp.messages.1572334 -->`
- **史观**：动手者叙事（总纲 10：报料、转储与处置均由用户与维护者一手记录）；经验优先（总纲 9：以完整 dmesg 与 APIC 寄存器转储为唯一判据）；循环结构呈现（总纲 4：同一警告在 2002-2007 年反复报料，形成长期闭环）
- **辨析**：本块 16 封多为用户自寄 dmesg 的未闭环案例，除 HP DL760 的 Summit 平台 `mach_apic.h` 硬编码断言崩溃（8 路 Xeon 上必崩）外，其余多被答为“已知问题/无害”；落书不得据报料数量推断该警告的实际危害面，警告文本本身也不等于缺陷确认。
- **文献**：DSLXC-4291/4292/4293/4297/4299/4300/4302/4304/4305/4306/4308/4311/4313/4315/4316/4325（`linux-smp.messages.1572299`、`.1572300`、`.1572301`、`.1572305`、`.1572308`、`.1572309`、`.1572311`、`.1572313`、`.1572314`、`.1572315`、`.1572317`、`.1572320`、`.1572322`、`.1572324`、`.1572325`、`.1572334`，2002-06 至 2007-09），全文见 `raw_source.raw_json`

## 12.2 【Linux社区】EBDA MP table 警告与维护者定调

**要点**：Alan Cox（2003-08-05）回 Federico Saizar：IBM x232 双 CPU 2.4.18-14smp 随机冻结 + “MP table in the EBDA can be UNSAFE”警告——“这条消息本身没问题（RH8 的 LILO/GRUB 已够新），先升到当前 errata 内核”；EBDA 警告的定调处置；khaled fawzy（2004-03-29）：IBM Netfinity 5600 双 CPU RH8→RH9 升级后随机挂死——三症状：①“MP table in the EBDA can be UNSAFE”②有时只用单处理器（面板 LED 可见）③“mtrr: Serverworks LE detected. Write-combining disabled / processor doesn't support write-combining”④“eth0: Bus master arbitration failure, status ffff”（pcnet32）——生产服务器求援，ServerWorks 平台三重警告并存样本；MRV Sastry（2004-09-29）：BSNL-Eluru Oracle9i on linux 2.1AS 夜间无负载自动重启——dmesg 见“MP table in the EBDA can be UNSAFE”求解释与解法；生产 Oracle 双机 EBDA 警告的实际影响案例；uaca@alumni.uv.es（2002-12-10）：VALinux FullOn 2230 双 PIII + Intel 440GX——irqtable“possibly defective BIOS detected”；Cox 答“能跑就行；跑不了 Intel 长期拒告诉怎么处理”；用户致谢并称“知道该向 valinux 和 intel 哪边投诉了”——厂商支持死角的存档

**史料**：`1572310`、`1572316`、`1572323`、`1572333`

**史料锚**：`<!-- ROW_MINE: linux-smp.messages.1572310 -->` `<!-- ROW_MINE: linux-smp.messages.1572316 -->` `<!-- ROW_MINE: linux-smp.messages.1572323 -->` `<!-- ROW_MINE: linux-smp.messages.1572333 -->`
- **史观**：动手者叙事（总纲 10：警告定调由 Alan Cox 等维护者以一句话给出）；经验优先（总纲 9：以“能跑就行”“先升 errata 内核”等可执行判据为准）；知识注定过时（总纲 22：Cox 自陈该 EBDA 警告文本“真该删了”，属被时间淘汰的旧提示）
- **辨析**：“MP table in the EBDA can be UNSAFE”在 Cox 口中已是应删的过时文本，但 2004 年仍在生产服务器上被当作求援线索；三症状并存的 ServerWorks 平台案例（EBDA 警告 + 单处理器回退 + write-combining 禁用 + 总线仲裁失败）不得径判为单一根因。
- **文献**：DSLXC-4301/4307/4314/4324（`linux-smp.messages.1572310`、`.1572316`、`.1572323`、`.1572333`，2002-12 至 2004-09），全文见 `raw_source.raw_json`

## 12.3 【Linux社区】SMP 硬件兼容性实战（板/CPU/芯片组）

**要点**：Ivanovic（2002-08-20）回 Quanta T52 双 2G-Xeon：noapic 下中断路由正确、不开则 PCI 中断错乱——建议 BIOS 把 MPS 设回 1.1（对 ASUS CUV4X-Dxx 板有效的老技巧）；引 Hileman 完整三 IO-APIC（#8/#9/#10）转储与 mptscsih 超时复位日志；Mitarotondo（2003-09-13）：双 Athlon MP 2200（stepping 0/1 不同）GA-7DPXDW-P（AMD760MPX）——约 50% 开机第二 CPU 启用成功（岩石稳定）、另 50% 只用单核且极不稳；附两种情况 dmesg；Markus Schorer（2002-10-23）：同款 Gigabyte 586dx 双 P200MMX——SMP 与 noapic 双重问题；最后配置较稳；USB 与 Adaptec 同 IRQ、APIC 试图分离永不成功、只能硬编码 USB 中断；C. Henry（2002-11-30）：RedHat 7.3 内核 2.4.18-3 双 PIII 无法用 SMP（只有 linux-up 可用、SMP 内核起不来）、怀疑主板；寄 lspci 信息求助；Pasianot（2002-08-22）：2.4.19 配置 bonding 接口瞬间整机冻住（boot 或手动皆然）、2.4.10 时正常；Tyan S2462 Thunder K7 + RH7.1 + 双 3COM 3c920；Frank von Daak（2006-04-07）结案信：Abit 官方确认 NI8 SLI 主板不支持 FSB800 低于 3.0GHz 的 CPU——“昂贵的板子 + 昂贵的 2.8GHz Pentium-D 无法正确配对”；下一步买 3.0GHz 碰运气；原问题（ACPI 开启只认单核、关 ACPI 则 OpenGL/随机冻结）归因硬件规格；Alan Cox（2002-08-22）回 Jon Zobrist：IBM x440（4P4 1.4G 4GB RAID）——“非同寻常的机型”；基线内核到 2.4.19-ac（计划进 2.4.20 正式版）才完全支持；2.4.9 时代只有 RH Advanced Server 树里的丑补丁；2.4.19 基线应能启动、依配置可能只起部分处理器——x440 支持史的维护者口径；Eric Webber（2002-08-13）：IBM X Series 230 eServer Model 61Y（Teton SMP 双 PIII Coppermine 996MHz）偶发系统锁死——问 dmesg 中 SMP 线索是否影响自己、选 non-smp 启动有何后果、SMP 问题挂死有何清晰症状；dmesg 亮 IBMachine detected/Enabling interrupts during APM calls、双 IO-APIC #14/#15、MP-BIOS bug 8254 timer not connected（经 8259A pin0 绕通）、IO-APIC#1 ID 15 in MPC fixed up（tell your hw vendor）；Troels Riis（2003-02-15）：Asus A7V333-X（VIA vt8235）——RedHat 8.0/Phoebe 装完 fdisk 后 beep 三声冻死；SuSE 8.1（2.4.19 无 vt8235 支持）大量 IO/irq 错误；Mandrake 8.1Beta3（2.4.21pre4）最好仍偶挂；问 vt8235 支持水平、2.5.60 是否有益、“丢板还是耐心”（Mandrake 2.4.20rc1→rc2 加入支持之说）——VIA 南桥支持线编年切片

**史料**：`1572289`、`1572291`、`1572293`、`1572296`、`1572297`、`1572312`、`1572321`、`1572326`、`1572327`

**史料锚**：`<!-- ROW_MINE: linux-smp.messages.1572289 -->` `<!-- ROW_MINE: linux-smp.messages.1572291 -->` `<!-- ROW_MINE: linux-smp.messages.1572293 -->` `<!-- ROW_MINE: linux-smp.messages.1572296 -->` `<!-- ROW_MINE: linux-smp.messages.1572297 -->` `<!-- ROW_MINE: linux-smp.messages.1572312 -->` `<!-- ROW_MINE: linux-smp.messages.1572321 -->` `<!-- ROW_MINE: linux-smp.messages.1572326 -->` `<!-- ROW_MINE: linux-smp.messages.1572327 -->`
- **史观**：动手者叙事（总纲 10：兼容性实战均由装机者与维护者逐例自述）；经验优先（总纲 9：以主板型号、芯片组、MPS 版本与 dmesg 为判据）；偶然性优先（总纲 5：双 CPU 识别成败取决于 BIOS 版本与主板规格等外因，非设计必然）
- **辨析**：本块多数案例的结论是硬件规格或 BIOS 限制（如 Abit 官方确认 NI8 SLI 不支持 FSB800 低于 3.0GHz 的 CPU），属厂商支持死角而非内核缺陷；XP→MP 跳线等民间说法未经厂商证实，只作传闻登记。
- **文献**：DSLXC-4282/4284/4286/4288/4289/4303/4312/4317/4318（`linux-smp.messages.1572289`、`.1572291`、`.1572293`、`.1572296`、`.1572297`、`.1572312`、`.1572321`、`.1572326`、`.1572327`，2002-08 至 2006-04），全文见 `raw_source.raw_json`

## 12.4 【Linux社区】APIC 错误与中断分配现象

**要点**：Tim Day（2005-05-06）：Gigabyte 6VXDC7（Via 694X）双 P3-933——nosmp 岩石稳定、SMP 下成对 APIC error 几分钟一次、终必硬锁死；noapic 也不行（中断退回 XT-PIC 走 CPU0 而错误依旧）；问能否构建完全无视 APIC 硬件的 SMP 内核（APIC 是 inter-CPU 通信关键？）；NOULARD（2004-11-07）：2.6.9 + CONFIG_IRQBALANCE=y 中断仍几乎全走 CPU0（smp_affinity 全 ffffffff、不知为何）；SideNote：先前 IRQ 共享麻烦在 BIOS 从 MPS 1.1 切 1.4 后消失；前信载 SCHED_FIFO 最高优先级线程测试法（单核启动则整机冻住直到线程结束）；Richard B. Johnson（2003-06-02）与 Mike Dresser 对谈：P4 2.66 + IC7-G 板“Hyper-thread technology”盒装承诺落空——第二 CPU 被 Intel 禁（HT 只在新 Xeon P4/800FSB 型号）；Johnson 怒指买空板（千兆口未焊、金属胶带盖孔）$275 板 + $635 CPU 被坑；自述 SMP 时代起一直双 CPU、想试“单 CPU SMP 架构”；Udo A. Steinberg（2003-05-29）：2.5.70 双 Xeon + HT——无 IRQ affinity 设置、按理所有 CPU 可接所有中断，但常规中断全走第一 CPU（timer/acpi/ide 全 CPU0 计数）；17 分钟 75M 次 ACPI 中断（远超正常）；问何故——SMP 中断分配不均的典型案例；Michal Sajdak（2002-05-05）回 Randy Dunlap：unexpected IO-APIC 报告被答“带内核版本号/2.4.16 已识别/无害可忽略或升级”——用户纠正“其实是 2.2.20”并问 2.2.21 有无机会——版本判定教训（Randy 误猜 2.4.N）与 2.2 时代长尾

**史料**：`1572290`、`1572295`、`1572303`、`1572304`、`1572337`

**史料锚**：`<!-- ROW_MINE: linux-smp.messages.1572290 -->` `<!-- ROW_MINE: linux-smp.messages.1572295 -->` `<!-- ROW_MINE: linux-smp.messages.1572303 -->` `<!-- ROW_MINE: linux-smp.messages.1572304 -->` `<!-- ROW_MINE: linux-smp.messages.1572337 -->`
- **史观**：经验优先（总纲 9：以 /proc/interrupts 计数与 APIC error 频次等实测为准）；动手者叙事（总纲 10：中断分配不均现象由用户与维护者现场记录）；自反性声明（总纲 7：Randy Dunlap 误判内核版本号后由用户当场纠正，教训一并入录）
- **辨析**：用户以 /proc/interrupts 全走 CPU0 推断“APIC 失效”属工具误用，维护者的解释（新中断平衡代码刻意集中以保 cache 局部性）与之并存；本块只并列两方口径，不裁断中断分配策略的优劣。
- **文献**：DSLXC-4283/4287/4295/4296/4328（`linux-smp.messages.1572290`、`.1572295`、`.1572303`、`.1572304`、`.1572337`，2002-05 至 2005-05），全文见 `raw_source.raw_json`

## 12.5 【Linux社区】调度器、性能与观测工具

**要点**：Nick Piggin（2004-01-29）回 Catalin：2.6.2-rc2 双 P4 HT + soft RAID1 + postgres/apache 低负载下控制台冻 3-4 秒（test11 同、2.6.1-rc2 好但两天崩）；Piggin：近期调度器改动不多、恐非调度问题，建议试最新 -mm（含 Hyperthreading 工作，须开 CONFIG_SCHED_SMT）；Alexander Rauth（2005-12-28）回 Satchidananda：top 只显示一行 CPU 是全 CPU 平均值——按 1 键切逐 CPU 显示、h 看全部命令；“下次先看 man 页”；Al Boldi（2006-04-03）续 Con Kolivas 桌面调度 RFC：Boldi——Linux 主要按服务器场景调优，导出 sched.c tunables 到 procfs 让用户按环境调是否更灵活；Kolivas——现有 tunables 无易懂启发式、导出没人懂的参数无益；Boldi 问按 cpu/mem/ctxt 性能做 autotuning 模块？Galbraith——小小 knob 的全效应都难预测、不够通用不宜暴露；Boldi 追问“代码是围绕这些 tunables 建的还是真在用它们？”；Alan Cox（2003-07-24）回 Anders：load average 3.39 但 CPU 99% idle——load average 也计 disk-wait 进程数，磁盘子系统被淹没 + 一堆 D 态进程时 load 会虚高——负载语义的权威科普；Ugama（2003-02-24）确认：SMP 性能测试“不可伸缩”根因是 rand() 非可重入——多线程竞争 rand() 串行化全部调用；移除后“everything become real-looking”；记录 _REENTRANT 在本例无可视影响但同意循 Leroy 建议——库函数可重入性与多核基准陷阱的直接实证

**史料**：`1572288`、`1572292`、`1572298`、`1572302`、`1572332`

**史料锚**：`<!-- ROW_MINE: linux-smp.messages.1572288 -->` `<!-- ROW_MINE: linux-smp.messages.1572292 -->` `<!-- ROW_MINE: linux-smp.messages.1572298 -->` `<!-- ROW_MINE: linux-smp.messages.1572302 -->` `<!-- ROW_MINE: linux-smp.messages.1572332 -->`
- **史观**：经验优先（总纲 9：以基准测试与 /proc/interrupts 实测为准，Ugama 的 rand() 不可重入根因即为实证）；动手者叙事（总纲 10：load average 语义由 Alan Cox 权威科普）；知识注定过时（总纲 22：sched.c tunables 是否导出之争以“没人懂”被否决，属阶段性结论）
- **辨析**：Ugama 的“不可伸缩”结论在移除 rand() 竞争后即消失，说明基准结论必须先排除库函数不可重入等非内核因素；load average 计入 disk-wait 的语义澄清系对常见误读的纠正，不得据此把 load 高读作 CPU 繁忙。
- **文献**：DSLXC-4281/4285/4290/4294/4323（`linux-smp.messages.1572288`、`.1572292`、`.1572298`、`.1572302`、`.1572332`，2003-02 至 2006-04），全文见 `raw_source.raw_json`

## 12.6 【Linux社区】线程原语与内存模型讨论

**要点**：J.A. Magallon（2002-07-13）续 per-thread 变量设计：IRIX PRDA 固定地址（0x00200000L）方案 vs Linux 技巧——clone() 谎报栈起点、栈顶留 32K 对齐私有区，getpriv 用 movl %esp + andl $ffff8000 + addl 32K 定位私有区首址（含 ASCII 图）；问 Alan Cox 这样是否正确；Cox 前答“单页不可共享→两个 mm→两套页表→TLB flush，IRIX 根本没为 clone 性能打算；而两条指令就够难了？”——TLS 实现的 2002 年设计讨论；Klaas Zweck（2002-04-21）自答：local timer mask 掉其实一直有效——/proc/interrupts 只显外部 timer IRQ 是错误的验证工具；top/xosview 显示被 mask CPU 100% idle 是因 timer 停更 kstat；“早给个提示就好了”——local APIC timer 语义的用户侧探索；Xu Yang（2007-09-04）mutex vs cache coherency 提问续：两者都能保护共享内存资源、是否都必要？有 mutex 无 coherency 明显出问题；只有 coherency 无 mutex 时多线程处理器（单核跑多线程共享 cache）coherency 失效仍会撞；追问纯单线程处理器+coherency 是否够；Mohamed Bamakhrama 推荐 Schimmel《UNIX Systems for Modern Architectures》（1994）；Yang 已下单——SMP 内存模型基础件的用户向讨论

**史料**：`1572328`、`1572318`、`1572335`

**史料锚**：`<!-- ROW_MINE: linux-smp.messages.1572328 -->` `<!-- ROW_MINE: linux-smp.messages.1572318 -->` `<!-- ROW_MINE: linux-smp.messages.1572335 -->`
- **史观**：动手者叙事（总纲 10：TLS 实现技巧与 local APIC timer 语义均由当事开发者自述）；经验优先（总纲 9：以 /proc/interrupts 是否可靠、指令序列是否可行等可验证点为判据）；知识注定过时（总纲 22：2002 年的 PRDA 方案与 2007 年的内存模型提问均属阶段性认知）
- **辨析**：Klaas Zweck 自陈“/proc/interrupts 只显外部 timer IRQ 是错误的验证工具”，属工具误用被当事人自行收回；Xu Yang 的“单核跑多线程是否仍需 coherency”之问在本线程未获定论，只登记为开放问题。
- **文献**：DSLXC-4319/4309/4326（`linux-smp.messages.1572328`、`.1572318`、`.1572335`，2002-04 至 2007-09），全文见 `raw_source.raw_json`

## 12.7 【Linux社区】内核开发进程与 2021 现代回归

**要点**：Borislav Petkov（2021-05-27）回 Srinivas：确认 lvtthmr_init 向 AP 复制是否 SMI 热机必需——BIOS 把 thermal 中断接管为 SMI 模式时按 BSP 保存值恢复 AP；自己把读取后移会复制错值（软禁 APIC 后核锁死等中断）；另一线索：核总在 IPI 远程 TLB flush 时锁死——5.12 热敏中断回归的关键分析；Earle R. Nietzel（2003-06-14）：引 Andrew Morton 解释（新中断平衡代码故意低速率中断集中单 CPU 保 cache 局部性、忙不过来才让别的 CPU 参与，“听起来有理且基准表现好”）并问是否进 2.4——自己在 2.4.20-13.9smp 上中断也全走 CPU0；附 /proc/interrupts 佐证；Vladimir G. Ivanovic（2002-07-01）：服务器不建议 noapic——SMP 机器正要众多中断分给所有 CPU 处理；引 Steve Keith 的 LILO（`append="noapic"`）与 GRUB（kernel 行尾 `noapic`）配置实录与“升级 BIOS/关 MPS 1.4”建议——noapic 用法的正反两面存档；Alan Cox（2002-12-06）回 Eric Benoit：“MP table in the EBDA can be UNSAFE”——“这条消息我们真该删了；非常老的内核加载器有时会踩 MP 表，约三四年前已修复”——过时警告文本的维护者清扫观点；Thomas HERAULT（2002-07-19）误报收回：前报 2.4.18 SMP 高负载 TCP 丢包疑案（对端不重发、连接悬挂）——实为坏 IDE 盘：丢包后 mmap 也出问题、内核开始 Oops、盘彻底死；“网络 + SMP 疑案先查硬件”的经典教训帖；James Feeney（2021-05-14）：linux 5.12 soft lockup CPU#0 stuck 23s @ smp_call_function_single——5.12.4 Arnd“smp: Fix smp_call_function_single_async prototype”补丁无效（栈顶换成 text_poke_loc_init/on_each_cpu 无限重复）；自认 bisect 可能失准（须“运动”系统才现形）；引 ArchLinux bug 70663 Markus bisect：7a800a20ae6 表现问题、f007a3d66c5 完好、中间 6 commits 黑屏死（Alt+SysRq/电源键无响应需硬关）；8 commits 皆 Christoph Hellwig 2021-02-02；warm reboot 常在 bootloader 后即冻、需完全断电重启——2021 现代回归实录与 bisect 方法论

**史料**：`1572306`、`1572319`、`1572329`、`1572330`、`1572331`、`1572336`

**史料锚**：`<!-- ROW_MINE: linux-smp.messages.1572306 -->` `<!-- ROW_MINE: linux-smp.messages.1572319 -->` `<!-- ROW_MINE: linux-smp.messages.1572329 -->` `<!-- ROW_MINE: linux-smp.messages.1572330 -->` `<!-- ROW_MINE: linux-smp.messages.1572331 -->` `<!-- ROW_MINE: linux-smp.messages.1572336 -->`
- **史观**：经验优先（总纲 9：以 bisect 区间、soft lockup 栈顶与 /proc/interrupts 为判据）；循环结构呈现（总纲 4：同一“中断全走 CPU0”现象自 2002 至 2021 反复出现）；自反性声明（总纲 7：当事人自认 bisect 可能失准，误报案例主动收回）
- **辨析**：2021 年 5.12 回归的 bisect 结论由当事人自认“可能失准（须系统处于运动状态才现形）”，落书不得据以锁定单一 commit；Thomas HERAULT 的 TCP 丢包疑案最终归因坏 IDE 盘，是“网络 + SMP 疑案先查硬件”的方法论教训，与内核缺陷须分开登记。
- **文献**：DSLXC-4298/4310/4320/4321/4322/4327（`linux-smp.messages.1572306`、`.1572319`、`.1572329`、`.1572330`、`.1572331`、`.1572336`，2002-07 至 2021-05），全文见 `raw_source.raw_json`

---
注：本文件由判定表程序化生成（12.1-12.7 共 7 块，覆盖 48/48 CAND）；要点逐字取自判定表“要点”列（审读实录），史料锚与 CAND 一一对应。
