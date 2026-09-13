# 23-白名单定型与SiS平台困境.md

> 对应页面：linux-smp p31（pk 1572838-1572887，2002-2021 混排）
> 判定：48 CAND / 2 NV（019 招聘广告、031 分区问答离题）
> 编号：DSLXC-4799..4846 | claim 已入库（48/48，dslinux_claims.duckdb）

## 23.1 白名单语义的终局定性（4 例）

**要点（判定表逐字）**：Randy Dunlap答Intel TME（p30 022之续）：2.4.9不识别E7500该芯片组而2.4.19应已识别并请Alan确认，另给syslog.conf加kern.*取全内核日志的方法；Earle Nietzel二次定性：意外IO-APIC不暗示任何故障，仅表示所用硬件不在白名单上，无实际问题即纯信息；并讨论Oracle认证下内核版本抉择；Randy Dunlap终局定性：2.6内核已不打印这些消息，多处在后续2.4修复并于2.6移除，根因是内核持有一份久未更新的known-valid IO APIC列表；引文为AMD员工咨询IBM x325 Opteron版本0x11三重定向；David McIlwraith民间定性称该警告一般无害，若出现OOPS或panic才值得讨论

**史料**：`1572851、`1572864、`1572875、`1572876

**史料锚**：

`<!-- ROW_MINE: linux-smp.messages.1572851 -->` `<!-- ROW_MINE: linux-smp.messages.1572864 -->` `<!-- ROW_MINE: linux-smp.messages.1572875 -->` `<!-- ROW_MINE: linux-smp.messages.1572876 -->` 

## 23.2 SiS 平台困境四连（4 例）

**要点（判定表逐字）**：Alan Cox裁定2.4尚不支持SiS APIC且已从SiS拿到所需资料但尚未回移2.5的相关改动，处方为编译不启用apic或以noapic启动；Iain McFarlane报告Microstar 6719 SiS651平台2.4.21pre4-1mdk下版本0x14意外IO-APIC，并声明须以noapic或pci=noapic运行因APIC未获支持；brian报告SpaceShuttle SS50 SiS板：noapic则一切正常否则板载网卡不工作，Becker确认是中断问题非驱动，pirq调参两轮仍无效；Tim Lee报告SiS 648平台AOpen AX45-8XN：BIOS开APIC模式则全部PCI设备与板载网卡失效，关闭则一切正常警告消失，问关闭APIC的性能代价

**史料**：`1572850、`1572859、`1572871、`1572884

**史料锚**：

`<!-- ROW_MINE: linux-smp.messages.1572850 -->` `<!-- ROW_MINE: linux-smp.messages.1572859 -->` `<!-- ROW_MINE: linux-smp.messages.1572871 -->` `<!-- ROW_MINE: linux-smp.messages.1572884 -->` 

## 23.3 报料全景与版本 0x20/0x14 家族（12 例）

**要点（判定表逐字）**：Justin Dale Coffman贴出IO APIC版本0x20的意外IO-APIC完整寄存器转储按新版信息要求上报；Aron Lentsch报告2.4.24出现意外IO-APIC且USB后置集线器不工作仅前置口可用，重编内核无效；charlie以是否真想知道自疑开场提交Mandrake 9.0下IO APIC版本0002警告，为报料者自我怀疑的行为样本；Hal Klingsporn贴出完整IRQ重定向表并问是否需补充更多信息，为标准报料版式样本；Trevor Lee的2.2.20加VIA VT3075双Coppermine日志证明2.2系同样触发unexpected IO-APIC，IRQ表呈Log Phy 0FF 0F特殊形态；Mattias Kregert报告Abit IC7上875P加ICH5R组合版本0x20完整启动日志，附硬件清单与IRQ变换序列；Jean-Louis Bach以三行极简报料称启动时硬盘作响随后映射问题，boot.msg按提示转介，为报料质量下限样本；Ross Johnson转贴7VRXP上2.4.20-k7的Athlon XP单核日志：ESR启动前值0x80、Via IRQ fixup四连、IO APIC Version 2字样；slaton报告双2.4G Xeon超线程RH8环境：寄存器0残值02008000、版本0x20、三IO APIC完整重定向表与四CPU APIC定时器校准；ratan贴出意外IO-APIC信息与完整IRQ重定向表，Log Phy 0FF 0F形态再现；BBaron贴出i875双P4 2.8 HT日志：ACPI路径Unknown CPU 15:3、版本0x20、cpu_sibling_map配对与2.4.20-8smp四CPU计数；Martin Bøjer报告catpipe双Xeon HT 2.4.20-13.8：指出内核已超三个月但仍无changelog修复线索并附rpm取证，为报料者自行查证行为样本

**史料**：`1572841、`1572848、`1572857、`1572860、`1572861、`1572862、`1572863、`1572872、`1572881、`1572883、`1572886、`1572887

**史料锚**：

`<!-- ROW_MINE: linux-smp.messages.1572841 -->` `<!-- ROW_MINE: linux-smp.messages.1572848 -->` `<!-- ROW_MINE: linux-smp.messages.1572857 -->` `<!-- ROW_MINE: linux-smp.messages.1572860 -->` `<!-- ROW_MINE: linux-smp.messages.1572861 -->` `<!-- ROW_MINE: linux-smp.messages.1572862 -->` `<!-- ROW_MINE: linux-smp.messages.1572863 -->` `<!-- ROW_MINE: linux-smp.messages.1572872 -->` `<!-- ROW_MINE: linux-smp.messages.1572881 -->` `<!-- ROW_MINE: linux-smp.messages.1572883 -->` `<!-- ROW_MINE: linux-smp.messages.1572886 -->` `<!-- ROW_MINE: linux-smp.messages.1572887 -->` 

## 23.4 EBDA 语义解释与咨询（2 例）

**要点（判定表逐字）**：Bilal KINAY报告IBM 5500 M20四路RH8 2.4.14smp频繁崩溃，日志仅附EBDA不安全警告；Earle Nietzel给出EBDA语义解释：该消息仅提示EBDA或XBDA启动期可能被写入而MP表恰位于其处，系统启动后EBDA不再可用且MP表已被OS读取，能启动即一切正常，答BSNL Oracle夜间自重启之问

**史料**：`1572840、`1572849

**史料锚**：

`<!-- ROW_MINE: linux-smp.messages.1572840 -->` `<!-- ROW_MINE: linux-smp.messages.1572849 -->` 

## 23.5 CUV4X-D 处方链与 Netfinity 实效（3 例）

**要点（判定表逐字）**：Bill Davidsen自述曾改一批IBM Netfinity机器BIOS以求稳定性大改善结果一无所获且性能无可测变化，反问若noapic能用何必大动干戈，引Weller的(no)apic问题一般归BIOS的裁定；Jonathan Claxton对CUV4X-D姊妹板DLS开出处方：BIOS升到最新、MPS勿设1.4、并试noapic；Alan Cox对CUV4X-D双P3给出判词：该板会彻底挂死，BIOS须设Intel MP1.1而非1.4或升级新版，并指出崩溃时CPU紧循环不应致过热蜂鸣除非散热另有问题

**史料**：`1572838、`1572855、`1572858

**史料锚**：

`<!-- ROW_MINE: linux-smp.messages.1572838 -->` `<!-- ROW_MINE: linux-smp.messages.1572855 -->` `<!-- ROW_MINE: linux-smp.messages.1572858 -->` 

## 23.6 平台风险框架与双核个案（4 例）

**要点（判定表逐字）**：Mike Dresser纠正称P4 2.66GHz stepping 07不支持超线程不必担心，反映2003年社区对P4步进与HT能力对应关系的困惑；Michal Szymanski报告三台Supermicro AS1020A-T双核Opteron 280在FC4 x86_64上负载即machine check或复位，以IDE盘加非SMP内核五十小时对照排除SATA驱动与内存，三台顶级机器只能跑25%算力；Lee Trager报告AMD X2 4400双核升级后系统时钟走快，notsc与no_timer_check仅部分缓解，编译游戏等CPU负载下加剧，2.6.14与2.6.15均在；Jakob Oestergaard给出非MP处理器上SMP板的风险框架即可能正常可能近乎正常也可能彻底失败，自陈Tyan Tiger双非MP无恙纯因运气

**史料**：`1572842、`1572844、`1572846、`1572854

**史料锚**：

`<!-- ROW_MINE: linux-smp.messages.1572842 -->` `<!-- ROW_MINE: linux-smp.messages.1572844 -->` `<!-- ROW_MINE: linux-smp.messages.1572846 -->` `<!-- ROW_MINE: linux-smp.messages.1572854 -->` 

## 23.7 x440/Summit 与 ACPI 诊断个案（4 例）

**要点（判定表逐字）**：Patrick R. McManus报告p4dpe-g2 E7500双Xeon在2.4.20-rc2-ac3上No sibling found两连、五个IO APIC、MTRR设置不一致、buggy MP table提示齐现；Frank von Daak在Abit NI8双核上开ACPI调试定位到processor_get_info报Error getting cpuindex for acpiid 0x1，为SMP问题溯源线索；Zwane Mwaikambo裁定x440 Summit/EXA支持需CONFIG_X86_SUMMIT且在2.4中藏于Multi-node NUMA支持的CONFIG_X86_NUMA之下；Tom Crystal报告ASL六台1U双Xeon机群中一台规律重启，查明为UPS失效致电源毛刺，恢复后每次启动日志仍含报告消息

**史料**：`1572852、`1572867、`1572869、`1572880

**史料锚**：

`<!-- ROW_MINE: linux-smp.messages.1572852 -->` `<!-- ROW_MINE: linux-smp.messages.1572867 -->` `<!-- ROW_MINE: linux-smp.messages.1572869 -->` `<!-- ROW_MINE: linux-smp.messages.1572880 -->` 

## 23.8 E7500 完整档案（1 例）

**要点（判定表逐字）**：ainman报告Supermicro 6012P-6 E7500双Xeon HT：寄存器0残值02008000、版本0x20、三IO APIC含双82870P2 P64H2 I/OxAPIC完整转储

**史料**：`1572870

**史料锚**：

`<!-- ROW_MINE: linux-smp.messages.1572870 -->` 

## 23.9 调度 tunables 之争与并发语义（5 例）

**要点（判定表逐字）**：William Tambe于2021年问Linux在任务迁移到不同CPU时是否调用local_flush_tlb_mm及在代码库何处发生，为遗留列表上的现代TLB语义咨询；Raz公告SOS服务导向调度器平台旨在把服务指派给卸载处理器，称Rik van Riel已表态并已在sourceforge建库提交微秒定时器示例；Con Kolivas原文裁定现有tunables与cpu/mem/ctxt性能间并无有意义的关联，导出无人理解的旋钮并无助益，为p30 Davidsen引文的引用源；Michael Andrescavage在P4DPE双Xeon四逻辑CPU上给出定量对照：SMP内核60秒约400万事务且每秒17万次上下文切换，单CPU内核60秒约900万事务仅3.3万次切换；Mike Galbraith裁定调度旋钮效果微妙以致不宜导出，即使仔细研读代码也难以预测微调的全效果

**史料**：`1572839、`1572843、`1572845、`1572853、`1572874

**史料锚**：

`<!-- ROW_MINE: linux-smp.messages.1572839 -->` `<!-- ROW_MINE: linux-smp.messages.1572843 -->` `<!-- ROW_MINE: linux-smp.messages.1572845 -->` `<!-- ROW_MINE: linux-smp.messages.1572853 -->` `<!-- ROW_MINE: linux-smp.messages.1572874 -->` 

## 23.10 内核语义与 TLS 前史（3 例）

**要点（判定表逐字）**：Srinivas G.报告同一驱动在2.4.18-3编译通过而在-3smp下hw_irq.h:202报current未声明，暴露UP与SMP头文件差异的编译门槛；Andrew Perepechko求内存屏障判读规则：wake_up隐含写屏障却未见于文档，问哪些内核例程提供屏障并求Unreliable Guide之外更可靠指南；J.A. Magallon求不用pthreads的per-thread全局变量方案：拟以clone直用模拟get与setspecific，提及__thread修饰符与IRIX的PRDA，为TLS设计前史第四声部

**史料**：`1572865、`1572866、`1572879

**史料锚**：

`<!-- ROW_MINE: linux-smp.messages.1572865 -->` `<!-- ROW_MINE: linux-smp.messages.1572866 -->` `<!-- ROW_MINE: linux-smp.messages.1572879 -->` 

## 23.11 崩溃与老平台三态（3 例）

**要点（判定表逐字）**：Diego报告Supermicro 6022P-6在2.2.26-rpd上出现wait_on_bh CPU6的irq与bh计数转储，为2.2时代SMP下半部处理故障样本；Aaron Tokhy报告PS3 Cell/PPC64上2.6.27软锁死61秒，调用栈停在csd_flag_wait与smp_call_function_single，背景为ps3vram补丁将显存MTD设备作swap；Richard Weinberger报告GA-586DX双MMX 200在2.4.18上大量APIC错误十二小时内崩溃，noapic则不报错但数日后仍崩，2.2.19一切正常

**史料**：`1572847、`1572877、`1572878

**史料锚**：

`<!-- ROW_MINE: linux-smp.messages.1572847 -->` `<!-- ROW_MINE: linux-smp.messages.1572877 -->` `<!-- ROW_MINE: linux-smp.messages.1572878 -->` 

## 23.12 责任归属与处置建议（3 例）

**要点（判定表逐字）**：Alan Cox对RH 2.4.18-3smp报障者只答一句先升级到勘误内核，为发行版勘误内核治理的直接表述；Alan Cox对双Athlon XP tar挂起案裁定Promise二进制RAID模块的问题应找Promise解决，为闭源模块责任归属句；peter.gantner答Intel员工求2.6.8-2 smp内核镜像：给出Debian包检索URL与trendmicro厂商模块页，为发行版包检索求助样本

**史料**：`1572873、`1572882、`1572885

**史料锚**：

`<!-- ROW_MINE: linux-smp.messages.1572873 -->` `<!-- ROW_MINE: linux-smp.messages.1572882 -->` `<!-- ROW_MINE: linux-smp.messages.1572885 -->` 

---
注：本文件由判定表程序化生成（23.1-23.12 共 12 块，覆盖 48/48 CAND，两遍计数核对通过）；要点逐字取自判定表「要点」列（主代理全读审读实录），史料锚与 CAND 一一对应，全文以 raw_source.raw_json 为准。
