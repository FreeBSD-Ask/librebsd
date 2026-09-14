# 15 【Linux社区】IO-APIC警告语义定调与平台兼容咨询

> 对应页面：linux-smp p23（pk 1572438-1572487，2002-2008 为主 + 2021 热敏线程 1 封 + 垃圾邮件 1 封）
> 判定：45 CAND / 5 NV（003 无正文客套、018 诈骗 spam、020 纯知会、024 纯附件转交、034 离题救援帖）
> 编号：DSLXC-4424..4468 | claim 已入库（45/45，dslinux_claims.duckdb）

## 15.1 【Linux社区】unexpected IO-APIC 警告语义与报料实践（12 例）

**要点**：Randy Dunlap（2006-03-18，答 Schenk，SuSE 9.0 2.4.21-273-smp4G）：“This has been fixed for several years now”“register 2 is a duplicate of register 1 so it is skipped”“isn't causing any run-time problems”，并不受“三个月”限定约束——“已修复多年”裁定性回复；Pieter Rabe（2003-12-09，Rabe Consulting）：RH9 最新核心内核报 unexpected IO-APIC，问“How do I go about reporting this”——报料流程咨询样本；Mobile Penguins Support（2003-03-28）：MSI KT4VL（Athlon XP 1700+，APIC+MPS 1.4）编译 2.4.20 时 dmesg“interesting error”，附 syslog——标准报料；Vladimir G. Ivanovic（2002-07-02）答 Bogusta：**用 noapic 对于 SMP server 不推荐**——“in that case you DO want the interrupts being serviced by all the CPUS”；服务器需全负载分布（对照 Alan“性能影响轻微”）——noapic 服务器定位第一手；Florian G. Pflug（2002-07-18）：ASUS A7V333（KT333）+Athlon XP 1800+：**安装 acpi-20020709 后才检测到 IO-APIC**（2.4.18 纯版检测不到）；via-ide 无 IRQ 回落 IRQ14/15——ACPI 补丁后才发现 IO-APIC、IDE 中断回退的复合样本；Courtney Grimland 转贴 + **Randy“It's safe to ignore”定调**（VIA KT400/Athlon 2100+）：**仅因 kernel 不支持 IO-APIC version 3**；Courtney 自述“I don't even know what IO-APIC is”——IO-APIC v3 可忽略的官方判词；Jed S. Baer（2003-09-08）：**UP 单核（Biostar M7VIG Pro，AMD XP 2200，`# CONFIG_SMP is not set`）**也报 unexpected IOAPIC（v3），.config：CONFIG_X86_UP_IOAPIC=y——**“UP 内核也启用 IO-APIC”的正面对质样本**；David Weinehall（2002-07-11）答 Alan：VIA KT266A = **Gigabyte GA-7VTXH**，固件注意**勿升 F7 BIOS（抓 CD 音轨时 IDE 总线 flaky）**；IO-APIC 警告如实上报；Earle Nietzel（2002-05-23）答 StorageTek Dave Schmitz 4 台（P4DC6+/P4DCE+/P4DP6，全体 IRQ 仅去 CPU0）：该警告“与性能问题及中断集中无关”，**“make sure your MPS setting is set to 1.1 not 1.4”**；不要 boot noapic（此选项会使全部中断落 CPU0）——MPS 1.1 部署建议（附带 4 台全套 dmesg）；Erik Mouw（2008-01-08）答 Telefonica（马德里，ESX 3.02）：2.4.21-47.0.1.ELvmnix **是 2003-06-13 的四年老内核且后缀示厂商内核**，“There's nothing wrong，内核只是不认识这块 IO-APIC 仍照常工作”“老内核跑新硬件并不少见”；一切正常不必升级（安全更新除外）——VMware 虚拟化警告定位 + “四岁内核”判断法；Alan Cox（2003-09-04）答 Michael Sorrentino：**unexpected IO-APIC 与锁死无关**（“Unexpected IO-APIC isnt related to your lockups alas”），转而追问“锁死那台与另两台同硬件机器做的事有何不同”——警告良性判定的又一裁定（与 002/014 同判）；Piers Lauder（2004-04-23，悉尼）：Mandrake 9.1 2.4.21-0.29mdkenterprise **单 CPU**（Athlon XP 2000+，`Error: only one processor found`，acpi=off）也 unexpected IO-APIC（register #00:02000000、IO-APIC version 0003），IO-APIC 完整 dump 供测——UP 触发警告又一例

**史料**：`1572439`、`1572442`、`1572447`、`1572453`、`1572458`、`1572466`、`1572469`、`1572474`、`1572475`、`1572480`、`1572483`、`1572486`

【Linux社区】**史料锚**：`<!-- ROW_MINE: linux-smp.messages.1572439 -->` `<!-- ROW_MINE: linux-smp.messages.1572442 -->` `<!-- ROW_MINE: linux-smp.messages.1572447 -->` `<!-- ROW_MINE: linux-smp.messages.1572453 -->` `<!-- ROW_MINE: linux-smp.messages.1572458 -->` `<!-- ROW_MINE: linux-smp.messages.1572466 -->` `<!-- ROW_MINE: linux-smp.messages.1572469 -->` `<!-- ROW_MINE: linux-smp.messages.1572474 -->` `<!-- ROW_MINE: linux-smp.messages.1572475 -->` `<!-- ROW_MINE: linux-smp.messages.1572480 -->` `<!-- ROW_MINE: linux-smp.messages.1572483 -->` `<!-- ROW_MINE: linux-smp.messages.1572486 -->`

**史观**：经验优先（总纲第 9 条——经验优先：以“已修复多年”“可安全忽略”与“与锁死无关”三裁定为判据）；本体论上各方平等（总纲第 8 条——本体论上各方平等：UP 用户、虚拟化用户、企业四台机群与厂商内核用户并置）
**辨析**：三处“可忽略/无关”均为当事维护者针对具体机型与版本的答复，不构成对所有 IO-APIC 警告的普遍裁定；UP 内核亦触发一例，构成“UP 内核也启用 IO-APIC”的正面反证。
**文献**：DSLXC-4425/4427/4432/4438/4441/4448/4451/4455/4456/4461/4464/4467（`linux-smp.messages.1572439` 等 12 封，2002-05-23 至 2008-01-08），全文见 `raw_source.raw_json`

## 15.2 【Linux社区】IO-APIC 寄存器位段与多 IO-APIC 拓扑档案

**要点**：MONARI, ANDI（2002-05-08，HP-Austria）：hp x4000（ATI FireGL2）——`register #00: 02008000` 三次触发警告、IO APIC version 0020；“Is this warning critical, does a patch exists?”——HP 工作站 IO-APIC 警告样本；Randy Dunlap（2002-10-18）回应 Maciej W. Rozycki：补丁（arch/i386/kernel/io_apic.c + include/asm-i386/io_apic.h）把 reg_00 的 reserved 拆成 **DT（delivery type）+ LTS 位**并打印，参照 Intel 82806AA（P64H）datasheet——IO-APIC 寄存器位语义补丁全文链；trolloc（2003-04-17）补全 **Supermicro X5DPE-G2（Intel 7502）**日志：**五个 IO-APIC（#2/#3/#4/#5/#8）全 register 转储、IRQ→pin 映射 + `WARNING: No sibling found for CPU 0/1`**（双 Xeon 2.40GHz 2.4.21-pre7-ac1）——多 IO-APIC 拓扑完整档案

**史料**：`1572443`、`1572448`、`1572460`

【Linux社区】**史料锚**：`<!-- ROW_MINE: linux-smp.messages.1572443 -->` `<!-- ROW_MINE: linux-smp.messages.1572448 -->` `<!-- ROW_MINE: linux-smp.messages.1572460 -->`

**史观**：经验优先（总纲第 9 条——经验优先：以 reg_00 位段补丁与 X5DPE-G2 五 IO-APIC 全转储为判据）；动手者创造历史（总纲第 10 条——动手者创造历史：位段语义补丁由维护者依 Intel 82806AA datasheet 实作）
**辨析**：本块三条分属寄存器位语义、多 IO-APIC 拓扑与 HP 平台样本，主题相近而线程各异；“WARNING: No sibling found”与 p24 016 首报为跨页对，不得重复计数。
**文献**：DSLXC-4428/4433/4443（`linux-smp.messages.1572443`、`.1572448`、`.1572460`，2002-05-08 至 2003-04-17），全文见 `raw_source.raw_json`

## 15.3 【Linux社区】APIC error 与锁死崩溃（6 例）

**要点**：Tim Day（2005-05-04）：Gigabyte 6VXDC7（Via 694X）双 PIII 933M、Debian Sarge 的 686-smp（2.4/2.6.8）——`nosmp` 或 UP 内核“rock solid”；SMP 下偶发 `APIC error on CPUx: 0y(0z)`（成对出现，每几分钟一次，2.6.8 无 noapic 时更频繁），uptime 数分钟至数天后必然无预警硬锁；试遍 BIOS/boot 组合、memcheck、重排 PCI 卡与换 PSU 均无效；检索到有人靠 BIOS 降压缓解的同型报告、无确诊——“芯片坏还是 boot/编译窍门”的经典悬案；Jose Vicente Nunez Zuleta（2002-08-15，答 LAPD）：Tyan Thunder LE-T S2518 + 694D Pro（MS-6321）多台 RH7.2 2.4.7-10smp——`APIC error on CPU0: 01(01)`/CPU1 02(02)，有机器死掉有自愈；/proc/interrupts 分布均匀（IRQ0 两 CPU 均分）——多程度 APIC error 的对照样本；Pau Montero Parés（2002-08-14）：双 Athlon 1400（Tyan 2460）**高负载/关机即挂**——拆网卡/显卡无改善（Adaptec 2100s RAID 无法拔除）、noapic+mem=nopentium 无效、单 CPU 支持编译即稳；perl rand() 死循环几秒内 SEGV 并死机；启动后 IO-APIC 2-0..not connected，/proc/interrupts 全落 CPU0（XT-PIC）；MPS 1.1/1.4 均挂——双 Athlon 高负载锁死完整报料；Barry Gamblin（2003-04-03）：Supermicro p4dc6 双 Xeon 1.7G RH7.3 2.4.18-19.7.xsmp，messages 见 **`kernel BUG at page_alloc.c:145`**（附件）——内存分配器 BUG 报障，问软硬错误归属；Sand Man/Martti（2002-10-18，奥卢）Tyan Tiger 133 自答结案：APIC errors 持续但无害；鼠标口被 IRQ12 抢走（BIOS PCI conf 将 IRQ12 设为 legacy ISA 后解决）；**切换 BIOS MP1.4 后共享 IRQ 整批恢复**（网卡 1 小时稳定）、USB 接口也恢复——MP1.4 效应实证（与 038 的 1.1 建议并存构成 1.1 vs 1.4 谱系，配合 026）；Neil Robst（2003-02-18，IBM 英国 IGS）：多台双 Xeon 2.0 / 2.4.18-18.7.xsmp——**SMP 模式启动数分钟后挂、UP 模式完全稳定，关闭 HT 无效**——SMP-only 死锁的企业案例

**史料**：`1572438`、`1572450`、`1572456`、`1572470`、`1572477`、`1572484`

【Linux社区】**史料锚**：`<!-- ROW_MINE: linux-smp.messages.1572438 -->` `<!-- ROW_MINE: linux-smp.messages.1572450 -->` `<!-- ROW_MINE: linux-smp.messages.1572456 -->` `<!-- ROW_MINE: linux-smp.messages.1572470 -->` `<!-- ROW_MINE: linux-smp.messages.1572477 -->` `<!-- ROW_MINE: linux-smp.messages.1572484 -->`

**史观**：经验优先（总纲第 9 条——经验优先：以 6VXDC7 排除链、S2518 自愈对照与 page_alloc.c:145 BUG 现场为判据）；没有必然性，只有偶然性（总纲第 5 条——没有必然性，只有偶然性：SMP 挂而 UP 稳的差异由具体板卡与固件偶然决定）
**辨析**：6VXDC7 悬案原文未确诊，本块仅登记其排除项；Tim Day 与 Robst 两例同型（SMP 挂、UP 稳）而板卡不同，不得合并为同一故障。
**文献**：DSLXC-4424/4435/4440/4452/4458/4465（`linux-smp.messages.1572438` 等 6 封，2002-08-14 至 2005-05-04），全文见 `raw_source.raw_json`

## 15.4 【Linux社区】多路平台兼容与 BIOS 选项咨询（9 例）

**要点**：Simon Oliver（2002-07-01，曼大 UMIST）：E7500（Plumas）双 P4-Xeon 2.2 1/2GB 编译咨询——“无 Xeon 选项就选 Pentium-4”“HIGHMEM 2GB/是否 4GB”“用户地址空间尺寸”；软件供应商测试建议**关掉 HyperThreading**（对计算密集任务降低性能），常规用途机考虑开 HT——E7500 平台编译与 HT 的供应商建议实录；Phil White（2004-02-26）答 Len Brown：**关掉 PAE 后 2.6.3 成功认到第 2 CPU**（Brown 早先提示“PAE 对 1GB 系统反而更慢，也许这就是坏的”）——PAE 与 CPU 发现互相干扰的实证；John W. Sopko Jr.（2004-03-10，北卡）：**单 P4 2.8 HT** 跑 smp 内核（RHEL AS 2.4.21-9.0.1.ELsmp）休眠 lock；`cpu_sibling_map[0] = 1`（HT 镜像）+ mapping CPU#0→CPU#1 runqueue——单芯 HT 跑 SMP 内核的锁死案例；Alan Cox（2002-08-26）答 IBM xseries 230 EBDA 警告：“That only applies to old old boot loaders”、hence unlikely related；反问 custom/旧版稳定性——EBDA 前提条件裁定；Snehasis Sinha（2002-09-30）答 Alan Cox：ASUS 主板 RealTek RTL-8029，`PCI: No IRQ known for interrupt pin A` + **probably buggy MP table**；网卡 loaded 但无法使用，求 workaround——MP table 缺陷导致 0 IRQ 的故障链；Zwane Mwaikambo（2003-12-08）答 Paul Rolland：**开启 `CONFIG_X86_NUMA` 后机器终于看见全部 CPU**（Paul 原话“That was it!”），但 BogoMips（200/2.4GHz）异常；Zwane 疑 timesource artifact 求 bootlog——NUMA 支持与多路可见度的直接实证；Vladimir G. Ivanovic（2004-05-20）答 Corin Langosch（双 Opteron 244）：**“老的双 PIII（ASUS CUV4X-DLS）必须关 MPS 1.4 才能启动；MPS 1.1 与 1.4 差异不大，最坏费两次 reboot”**——MPS 1.1/1.4 经验从 PIII 迁移到 Opteron；Riivo Lepp（2002-12-02，爱沙尼亚系统集成商 AS Cell Network）：**RH AS 2.1 + IBM eSeries x440**（按 IBM 支持站点指南安装、RHN 补丁全装），求中断诊断（暂无重载/附启动 dump）——企业环境部署咨询；Alan Cox（2002-12-03）：**x440（8687-1RX）不是普通 PC，需 IBM 尚未并入主线内核的补丁**——x440 专项裁定

**史料**：`1572441`、`1572445`、`1572449`、`1572451`、`1572454`、`1572462`、`1572463`、`1572468`、`1572476`

【Linux社区】**史料锚**：`<!-- ROW_MINE: linux-smp.messages.1572441 -->` `<!-- ROW_MINE: linux-smp.messages.1572445 -->` `<!-- ROW_MINE: linux-smp.messages.1572449 -->` `<!-- ROW_MINE: linux-smp.messages.1572451 -->` `<!-- ROW_MINE: linux-smp.messages.1572454 -->` `<!-- ROW_MINE: linux-smp.messages.1572462 -->` `<!-- ROW_MINE: linux-smp.messages.1572463 -->` `<!-- ROW_MINE: linux-smp.messages.1572468 -->` `<!-- ROW_MINE: linux-smp.messages.1572476 -->`

**史观**：经验优先（总纲第 9 条——经验优先：以“关 PAE 即认到第 2 CPU”、CONFIG_X86_NUMA 开关见 CPU 与 CUV4X-DLS 关 MPS 1.4 可启动为判据）；没有必然性，只有偶然性（总纲第 5 条——没有必然性，只有偶然性：x440 需 IBM 未并主线的补丁、MP table 缺陷致 0 IRQ 均由具体固件偶然造成）
**辨析**：x440 与 MPS 1.1/1.4 谱系两处均为维护者口径，属经验处方而非规格裁定；“供应商建议关 HT”出自厂商侧建议，不具普遍性。
**文献**：DSLXC-4426/4430/4434/4436/4439/4444/4445/4450/4457（`linux-smp.messages.1572441` 等 9 封，2002-07-01 至 2004-05-20），全文见 `raw_source.raw_json`

## 15.5 【Linux社区】调度、亲和性与中断分发（9 例）

**要点**：Lapo TIN 8×bttv IRQ 共享崩溃（PentiumD945 2.6.19smp，两个 4 路采集卡 IRQ 18-21 共享）；Davidsen（2007-02-02）：**并非 IRQ 冲突而是 PCI 总线带宽耗尽**，需多总线 /66MHz/64bit server 板验证——“共享冲突 vs 总线饱和”的判别方法；David Horwitt（2002-08-08，UCSD/Scripps 海洋所）：Supermicro **PC4DCE+（Intel 860）** 双 Xeon 2.2 2GB RDRAM——2 任务 SMP **8m40s≈2×4m40s**、4 任务 user=real=4×；UP real 略超 4×而 user 与单任务相近；试遍 MPS 1.1/1.4、HT、ECC、idle=poll、noapic、acpi=off 无变化且中断全落 CPU0——“SMP 不缩放”的测量报告；NOULARD Eric（2004-11-08）：2.6.9 IRQ 仍集中 CPU0——**CONFIG_IRQBALANCE 只是内核开启，还须用户态 irqbalance 工具**（people.redhat.com/arjanv）结合；转述其“为何要用户态工具做均衡”之问 + Johan Kullstam 答案：内核默认（smp_affinity 全 1）倾向把 IRQ 留在同一 CPU——irqbalance 用户态时代；Robert M. Hyatt（2002-09-11）：**“hyper-threading makes a single cpu look like two”**——HT 双逻辑导致 CPU 计数翻倍的权威一句（答 Boeing Randy Watson 的 P4DC6 四 CPU 之惑）；Ugama（2003-02-23）：SE7500CW2 双 Xeon HT 4 logical——**fork 1/2/4 进程 6s/6s/11s；pthread 版 12min31s（real），user 4min31s+sys 4min43s，作者自述“aproximatelly 50 (!!!!!) times slower”**并附全套 benchmark C 代码（fork 模式+pthread 单/四线程）；怀疑“pthread 由 clone() 创建故调度方式不同，但不确定”——fork 快而 pthread 慢两个数量级的调度奇异证据包；Matthew Faulkner（2007-06-15）：**内核如何决定硬件中断由哪颗 CPU/core 处理？**——中断分发机制的基础之问；E. Robert Bogusta（2002-05-23）答 Alan：认可 noapic“Performance impact close to nil”——**但无 APIC 则无法用 nmi_watchdog（且自己有误报经历），考虑购置真硬件看门狗卡**——noapic 衍生代价讨论；Earle R. Nietzel（2003-06-19）答 Hyatt“OS 应正确处理”：承认 OS 应尽力，但当重要进程被其他进程挤占 CPU 时须维持其性能水准——“This might be unacceptable which is why processor affinity is required”；并称 affinity 工具在 scale-up（纵向扩展）机器上比 scale-out 更有价值——进程绑定的运维必要性论据；Robert M. Hyatt（2003-06-19）posix threads：国际象棋引擎 crafty——**RH 9 的 stock 2.4.20-8/2.4.29-9 内核（原文如此，疑 2.4.20-9 之笔误）上 pthread 正常，vanilla 2.4.20/2.4.21 自编译则“fails miserably”**；曾因 pthread 故障“rolled my own”改用 clone() 自实现（可移植性变差）——发行版补丁 vs vanilla 内核线程差异报告

**史料**：`1572446`、`1572464`、`1572465`、`1572467`、`1572472`、`1572473`、`1572481`、`1572485`、`1572487`

【Linux社区】**史料锚**：`<!-- ROW_MINE: linux-smp.messages.1572446 -->` `<!-- ROW_MINE: linux-smp.messages.1572464 -->` `<!-- ROW_MINE: linux-smp.messages.1572465 -->` `<!-- ROW_MINE: linux-smp.messages.1572467 -->` `<!-- ROW_MINE: linux-smp.messages.1572472 -->` `<!-- ROW_MINE: linux-smp.messages.1572473 -->` `<!-- ROW_MINE: linux-smp.messages.1572481 -->` `<!-- ROW_MINE: linux-smp.messages.1572485 -->` `<!-- ROW_MINE: linux-smp.messages.1572487 -->`

**史观**：经验优先（总纲第 9 条——经验优先：以 PC4DCE+ 的 8m40s≈2×4m40s 测量、fork 与 pthread 两个数量级之差与 bttv 总线饱和判别为判据）；动手者创造历史（总纲第 10 条——动手者创造历史：benchmark 代码与用户态 irqbalance 工具均由当事人实发）
**辨析**：pthread 慢两个数量级一例原文自陈“不确定”（怀疑 clone 调度方式不同），落书不得据此断言内核缺陷；“2.4.29-9”原稿自注疑为笔误（原文如此）。
**文献**：DSLXC-4431/4446/4447/4449/4453/4454/4462/4466/4468（`linux-smp.messages.1572446` 等 9 封，2002-05-23 至 2007-06-15），全文见 `raw_source.raw_json`

## 15.6 【Linux社区】厂商驱动卸载 oops：arcmsr 现场

**要点**：Kevin Wang / Areca Support（2006-12-27）答 Gaspar Bakos：arcmsr 模块移除触发 oops 是否“仅在 archttp64（用户态监控 daemon）运行时”——厂商侧针对性提问（与 045 同一现场）；Gaspar Bakos（2006-12-26）——**移除 arcmsr 模块时两连 oops（do_ioctl+36 / filp_close+57）**：`Unable to handle kernel paging request` **+ `BUG: sleeping function called from invalid context (rwsem.h:43)` `irqs_disabled():1` `Fixing recursive fault but reboot is needed`**；自述用户态 areca_archttp64 daemon 确在运行但内核 oops 仍不应发生（2.6.17.6 kernel.org，4×双核 Opteron，附 config URL）——厂商驱动卸载典型 oops 全景

**史料**：`1572444`、`1572482`

【Linux社区】**史料锚**：`<!-- ROW_MINE: linux-smp.messages.1572444 -->` `<!-- ROW_MINE: linux-smp.messages.1572482 -->`

**史观**：经验优先（总纲第 9 条——经验优先：以两连 oops 的调用栈与 irqs_disabled() 现场为判据）；动手者创造历史（总纲第 10 条——动手者创造历史：厂商与用户双方在同一线程内对质）
**辨析**：厂商侧提问“是否仅在 daemon 运行时”属针对性反问，非根因认定；用户自述 oops 不应发生，本块不含修复结论。
**文献**：DSLXC-4429/4463（`linux-smp.messages.1572444`、`.1572482`，2006-12-26 至 2006-12-27），全文见 `raw_source.raw_json`

## 15.7 【Linux社区】报告规范化、文档与 2021 热敏收尾

**要点**：Randy Dunlap（2002-06-02）与 Vladimir Ivanovic 推进：**请求所有报料者附主板 URL + 手册链接**；仍缺 VIA chipset spec 向列表求 URL——报告规范化进程；Zwane Mwaikambo（2003-03-03）答 Christopher Huhn：NFS 空指针 oops 先确认是否为 first oops，建议“run a newer 2.4 and we can debug from there”——oops 报告分诊法；Vladimir G. Ivanovic（2002-11-02）答：I/O APIC 分配机制引 **Intel Architecture Software Developer's Manual Vol.3（1999）p 7-13**、内核 `Documentation/i386/IO-APIC.txt`、Randy Dunlap 的“Linux 与 MPS 1.4 规格差异”文（xenotime.net mp-spec-1x.txt）——“查证路线”三件套；Borislav Petkov（2021-05-28）答 Gleixner：禁用 CPU_SUP_INTEL 后若 `intel_init_thermal()` 真是给滞留 SMM 的核心解套，则“might not even boot successfully”；**“When is it not when SMM is involved?”**；SMM“stinking goo”须开源替换成 small and sane，BIOS 厂商总爱乱动架构组件——SMM/热敏 2021 之争、开源 SMM 主张

**史料**：`1572452`、`1572459`、`1572478`、`1572479`

【Linux社区】**史料锚**：`<!-- ROW_MINE: linux-smp.messages.1572452 -->` `<!-- ROW_MINE: linux-smp.messages.1572459 -->` `<!-- ROW_MINE: linux-smp.messages.1572478 -->` `<!-- ROW_MINE: linux-smp.messages.1572479 -->`

**史观**：经验优先（总纲第 9 条——经验优先：以“报料附主板 URL 与手册链接”、oops 分诊法与查证三件套为判据）；循环结构呈现（总纲第 4 条——循环结构呈现：2002 年 IO-APIC 分配机制查证与 2021 年 SMM 热敏之争跨 19 年同题回归）
**辨析**：2021 年“可能连启动都不成功”为条件句假说，非实测结论；SMM 开源主张属立场陈述，落书须与机制确认区分。
**文献**：DSLXC-4437/4442/4459/4460（`linux-smp.messages.1572452` 等 4 封，2002-06-02 至 2021-05-28），全文见 `raw_source.raw_json`

---
注：本文件由判定表程序化生成（15.1-15.7 共 7 块，覆盖 45/45 CAND，两遍计数核对通过）；要点逐字取自判定表“要点”列（主代理全读审读实录，2026-09-12 复核校订 13 处讹误），史料锚与 CAND 一一对应，全文以 raw_source.raw_json 为准。
