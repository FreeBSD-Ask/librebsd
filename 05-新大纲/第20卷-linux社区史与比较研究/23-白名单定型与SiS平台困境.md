# 23 【Linux社区】白名单定型与SiS平台困境

> 对应页面：linux-smp p31（pk 1572838-1572887，2002-2021 混排）
> 判定：48 CAND / 2 NV（019 招聘广告、031 分区问答离题）
> 编号：DSLXC-4799..4846 | claim 已入库（48/48，dslinux_claims.duckdb）

## 23.1 【Linux社区】白名单语义的终局定性（4 例）

**要点（判定表逐字）**：Randy Dunlap答Intel TME（p30 022之续）：2.4.9不识别E7500该芯片组而2.4.19应已识别并请Alan确认，另给syslog.conf加kern.*取全内核日志的方法；Earle Nietzel二次定性：意外IO-APIC不暗示任何故障，仅表示所用硬件不在白名单上，无实际问题即纯信息；并讨论Oracle认证下内核版本抉择；Randy Dunlap终局定性：2.6内核已不打印这些消息，多处在后续2.4修复并于2.6移除，根因是内核持有一份久未更新的known-valid IO APIC列表；引文为AMD员工咨询IBM x325 Opteron版本0x11三重定向；David McIlwraith民间定性称该警告一般无害，若出现OOPS或panic才值得讨论

**史料**：`1572851`、`1572864`、`1572875`、`1572876`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572851 -->` `<!-- ROW_MINE: linux-smp.messages.1572864 -->` `<!-- ROW_MINE: linux-smp.messages.1572875 -->` `<!-- ROW_MINE: linux-smp.messages.1572876 -->` 

**史观**：知识注定过时（总纲第 22 条——知识注定过时：known-valid IO APIC 列表久未更新，2.4 陆续修复并于 2.6 移除该消息）；多方平等（总纲第 8 条——本体论上各方平等：维护者终局定性、二次定性与民间定性三声部并置）
**辨析**：Dunlap 的“2.6 已不打印”为终局定性，落书须与 2.6 源码核对；McIlwraith 的民间定性为社区判断，非维护者口径。
**文献**：DSLXC-4812、DSLXC-4824、DSLXC-4834、DSLXC-4835（`linux-smp.messages.1572851`、`linux-smp.messages.1572864`、`linux-smp.messages.1572875`、`linux-smp.messages.1572876`，2002-08-15、2005-01-25、2005-03-15、2002-10-03），全文见 `raw_source.raw_json`

## 23.2 【Linux社区】SiS 平台困境四连（4 例）

**要点（判定表逐字）**：Alan Cox裁定2.4尚不支持SiS APIC且已从SiS拿到所需资料但尚未回移2.5的相关改动，处方为编译不启用apic或以noapic启动；Iain McFarlane报告Microstar 6719 SiS651平台2.4.21pre4-1mdk下版本0x14意外IO-APIC，并声明须以noapic或pci=noapic运行因APIC未获支持；brian报告SpaceShuttle SS50 SiS板：noapic则一切正常否则板载网卡不工作，Becker确认是中断问题非驱动，pirq调参两轮仍无效；Tim Lee报告SiS 648平台AOpen AX45-8XN：BIOS开APIC模式则全部PCI设备与板载网卡失效，关闭则一切正常警告消失，问关闭APIC的性能代价

**史料**：`1572850`、`1572859`、`1572871`、`1572884`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572850 -->` `<!-- ROW_MINE: linux-smp.messages.1572859 -->` `<!-- ROW_MINE: linux-smp.messages.1572871 -->` `<!-- ROW_MINE: linux-smp.messages.1572884 -->` 

**史观**：偶然性优先（总纲第 5 条——没有必然性，只有偶然性：SiS 平台困境由 2.4 未回移 2.5 的相关改动这一时序差异造成）；动手者叙事（总纲第 10 条——动手者创造历史：以 noapic、pci=noapic 与 BIOS 开关等可操作处方为分析单位）
**辨析**：Cox 的处方（不启用 apic 或以 noapic 启动）为 2003 年时的权宜；Tim Lee 的“关闭 APIC 的性能代价”之问在本页未见答复。
**文献**：DSLXC-4811、DSLXC-4819、DSLXC-4830、DSLXC-4843（`linux-smp.messages.1572850`、`linux-smp.messages.1572859`、`linux-smp.messages.1572871`、`linux-smp.messages.1572884`，2002-12-30、2003-02-09、2002-08-29、2002-01-16），全文见 `raw_source.raw_json`

## 23.3 【Linux社区】报料全景与版本 0x20/0x14 家族（12 例）

**要点（判定表逐字）**：Justin Dale Coffman贴出IO APIC版本0x20的意外IO-APIC完整寄存器转储按新版信息要求上报；Aron Lentsch报告2.4.24出现意外IO-APIC且USB后置集线器不工作仅前置口可用，重编内核无效；charlie以是否真想知道自疑开场提交Mandrake 9.0下IO APIC版本0002警告，为报料者自我怀疑的行为样本；Hal Klingsporn贴出完整IRQ重定向表并问是否需补充更多信息，为标准报料版式样本；Trevor Lee的2.2.20加VIA VT3075双Coppermine日志证明2.2系同样触发unexpected IO-APIC，IRQ表呈Log Phy 0FF 0F特殊形态；Mattias Kregert报告Abit IC7上875P加ICH5R组合版本0x20完整启动日志，附硬件清单与IRQ变换序列；Jean-Louis Bach以三行极简报料称启动时硬盘作响随后映射问题，boot.msg按提示转介，为报料质量下限样本；Ross Johnson转贴7VRXP上2.4.20-k7的Athlon XP单核日志：ESR启动前值0x80、Via IRQ fixup四连、IO APIC Version 2字样；slaton报告双2.4G Xeon超线程RH8环境：寄存器0残值02008000、版本0x20、三IO APIC完整重定向表与四CPU APIC定时器校准；ratan贴出意外IO-APIC信息与完整IRQ重定向表，Log Phy 0FF 0F形态再现；BBaron贴出i875双P4 2.8 HT日志：ACPI路径Unknown CPU 15:3、版本0x20、cpu_sibling_map配对与2.4.20-8smp四CPU计数；Martin Bøjer报告catpipe双Xeon HT 2.4.20-13.8：指出内核已超三个月但仍无changelog修复线索并附rpm取证，为报料者自行查证行为样本

**史料**：`1572841`、`1572848`、`1572857`、`1572860`、`1572861`、`1572862`、`1572863`、`1572872`、`1572881`、`1572883`、`1572886`、`1572887`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572841 -->` `<!-- ROW_MINE: linux-smp.messages.1572848 -->` `<!-- ROW_MINE: linux-smp.messages.1572857 -->` `<!-- ROW_MINE: linux-smp.messages.1572860 -->` `<!-- ROW_MINE: linux-smp.messages.1572861 -->` `<!-- ROW_MINE: linux-smp.messages.1572862 -->` `<!-- ROW_MINE: linux-smp.messages.1572863 -->` `<!-- ROW_MINE: linux-smp.messages.1572872 -->` `<!-- ROW_MINE: linux-smp.messages.1572881 -->` `<!-- ROW_MINE: linux-smp.messages.1572883 -->` `<!-- ROW_MINE: linux-smp.messages.1572886 -->` `<!-- ROW_MINE: linux-smp.messages.1572887 -->` 

**史观**：多方平等（总纲第 8 条——本体论上各方平等：报料质量从极简三行到完整寄存器转储十二例并置）；经验优先（总纲第 9 条——经验优先：以 ESR 启动前值、寄存器 0 残值 02008000 等实测为判据）
**辨析**：十二例为报料行为样本，其质量差异本身即史料；Martin Bøjer 的“自行查证 rpm 取证”属报料者主动溯源，其“无 changelog 线索”须以当期 rpm 实况核对。
**文献**：DSLXC-4802、DSLXC-4809、DSLXC-4817、DSLXC-4820、DSLXC-4821、DSLXC-4822、DSLXC-4823、DSLXC-4831、DSLXC-4840、DSLXC-4842、DSLXC-4845、DSLXC-4846（`linux-smp.messages.1572841`、`linux-smp.messages.1572848`、`linux-smp.messages.1572857`、`linux-smp.messages.1572860`、`linux-smp.messages.1572861`、`linux-smp.messages.1572862`、`linux-smp.messages.1572863`、`linux-smp.messages.1572872`、`linux-smp.messages.1572881`、`linux-smp.messages.1572883`、`linux-smp.messages.1572886`、`linux-smp.messages.1572887`，2003-12-13、2004-02-03、2003-03-27、2003-10-28、2002-10-12、2003-05-27、2003-01-09、2003-02-15、2003-01-08、2003-09-02、2004-06-28、2003-05-23），全文见 `raw_source.raw_json`

## 23.4 【Linux社区】EBDA 语义解释与咨询（2 例）

**要点（判定表逐字）**：Bilal KINAY报告IBM 5500 M20四路RH8 2.4.14smp频繁崩溃，日志仅附EBDA不安全警告；Earle Nietzel给出EBDA语义解释：该消息仅提示EBDA或XBDA启动期可能被写入而MP表恰位于其处，系统启动后EBDA不再可用且MP表已被OS读取，能启动即一切正常，答BSNL Oracle夜间自重启之问

**史料**：`1572840`、`1572849`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572840 -->` `<!-- ROW_MINE: linux-smp.messages.1572849 -->` 

**史观**：经验优先（总纲第 9 条——经验优先：以 EBDA 与 MP 表的位置关系、OS 读取时序等机制说明为判据）；多方平等（总纲第 8 条——本体论上各方平等：机构报障者与维护者解释地位平等）
**辨析**：Nietzel 的语义解释为社区侧说明，非官方文档；Bilal KINAY 的“频繁崩溃”与 EBDA 警告的因果在本页未结。
**文献**：DSLXC-4801、DSLXC-4810（`linux-smp.messages.1572840`、`linux-smp.messages.1572849`，2003-02-12、2004-09-29），全文见 `raw_source.raw_json`

## 23.5 【Linux社区】CUV4X-D 处方链与 Netfinity 实效（3 例）

**要点（判定表逐字）**：Bill Davidsen自述曾改一批IBM Netfinity机器BIOS以求稳定性大改善结果一无所获且性能无可测变化，反问若noapic能用何必大动干戈，引Weller的(no)apic问题一般归BIOS的裁定；Jonathan Claxton对CUV4X-D姊妹板DLS开出处方：BIOS升到最新、MPS勿设1.4、并试noapic；Alan Cox对CUV4X-D双P3给出判词：该板会彻底挂死，BIOS须设Intel MP1.1而非1.4或升级新版，并指出崩溃时CPU紧循环不应致过热蜂鸣除非散热另有问题

**史料**：`1572838`、`1572855`、`1572858`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572838 -->` `<!-- ROW_MINE: linux-smp.messages.1572855 -->` `<!-- ROW_MINE: linux-smp.messages.1572858 -->` 

**史观**：经验优先（总纲第 9 条——经验优先：以改 BIOS 后一无所获、性能无可测变化、CUV4X-D 彻底挂死等实测为判据）；多方平等（总纲第 8 条——本体论上各方平等：noapic 派与 BIOS 派两说并置）
**辨析**：Cox 的判词（该板会彻底挂死、须设 Intel MP1.1）为具体机型裁定；Davidsen 的反问为个人批量经验，不构成普适处方。
**文献**：DSLXC-4799、DSLXC-4816、DSLXC-4818（`linux-smp.messages.1572838`、`linux-smp.messages.1572855`、`linux-smp.messages.1572858`，2002-10-30、2002-04-15、2002-08-07），全文见 `raw_source.raw_json`

## 23.6 【Linux社区】平台风险框架与双核个案（4 例）

**要点（判定表逐字）**：Mike Dresser纠正称P4 2.66GHz stepping 07不支持超线程不必担心，反映2003年社区对P4步进与HT能力对应关系的困惑；Michal Szymanski报告三台Supermicro AS1020A-T双核Opteron 280在FC4 x86_64上负载即machine check或复位，以IDE盘加非SMP内核五十小时对照排除SATA驱动与内存，三台顶级机器只能跑25%算力；Lee Trager报告AMD X2 4400双核升级后系统时钟走快，notsc与no_timer_check仅部分缓解，编译游戏等CPU负载下加剧，2.6.14与2.6.15均在；Jakob Oestergaard给出非MP处理器上SMP板的风险框架即可能正常可能近乎正常也可能彻底失败，自陈Tyan Tiger双非MP无恙纯因运气

**史料**：`1572842`、`1572844`、`1572846`、`1572854`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572842 -->` `<!-- ROW_MINE: linux-smp.messages.1572844 -->` `<!-- ROW_MINE: linux-smp.messages.1572846 -->` `<!-- ROW_MINE: linux-smp.messages.1572854 -->` 

**史观**：经验优先（总纲第 9 条——经验优先：以 IDE 盘加非 SMP 内核五十小时对照、三台机器只能跑 25% 算力等实测为判据）；偶然性优先（总纲第 5 条——没有必然性，只有偶然性：非 MP 处理器上 SMP 板的风险三态被明示为“纯因运气”）
**辨析**：Oestergaard 的风险框架明示结果不可预测，落书不得写成必然成功或必然失败；Szymanski 的对照实验排除了 SATA 与内存，但根因未定。
**文献**：DSLXC-4803、DSLXC-4805、DSLXC-4807、DSLXC-4815（`linux-smp.messages.1572842`、`linux-smp.messages.1572844`、`linux-smp.messages.1572846`、`linux-smp.messages.1572854`，2003-06-02、2006-04-18、2006-01-05、2002-09-30），全文见 `raw_source.raw_json`

## 23.7 【Linux社区】x440/Summit 与 ACPI 诊断个案（4 例）

**要点（判定表逐字）**：Patrick R. McManus报告p4dpe-g2 E7500双Xeon在2.4.20-rc2-ac3上No sibling found两连、五个IO APIC、MTRR设置不一致、buggy MP table提示齐现；Frank von Daak在Abit NI8双核上开ACPI调试定位到processor_get_info报Error getting cpuindex for acpiid 0x1，为SMP问题溯源线索；Zwane Mwaikambo裁定x440 Summit/EXA支持需CONFIG_X86_SUMMIT且在2.4中藏于Multi-node NUMA支持的CONFIG_X86_NUMA之下；Tom Crystal报告ASL六台1U双Xeon机群中一台规律重启，查明为UPS失效致电源毛刺，恢复后每次启动日志仍含报告消息

**史料**：`1572852`、`1572867`、`1572869`、`1572880`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572852 -->` `<!-- ROW_MINE: linux-smp.messages.1572867 -->` `<!-- ROW_MINE: linux-smp.messages.1572869 -->` `<!-- ROW_MINE: linux-smp.messages.1572880 -->` 

**史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 ACPI 调试定位 processor_get_info 与 CONFIG_X86_NUMA 下的 SUMMIT 支持为分析单位）；经验优先（总纲第 9 条——经验优先：以 UPS 失效致电源毛刺这一查明结论为判据）
**辨析**：Zwane 的配置裁定为 2.4 时期的选项路径；Tom Crystal 的机群重启案已查明为电源问题，属闭环正样本，落书须保留其“日志仍含报告消息”的无关性。
**文献**：DSLXC-4813、DSLXC-4827、DSLXC-4828、DSLXC-4839（`linux-smp.messages.1572852`、`linux-smp.messages.1572867`、`linux-smp.messages.1572869`、`linux-smp.messages.1572880`，2002-11-27、2006-04-06、2003-12-05、2003-04-01），全文见 `raw_source.raw_json`

## 23.8 【Linux社区】E7500 完整档案（1 例）

**要点（判定表逐字）**：ainman报告Supermicro 6012P-6 E7500双Xeon HT：寄存器0残值02008000、版本0x20、三IO APIC含双82870P2 P64H2 I/OxAPIC完整转储

**史料**：`1572870`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572870 -->` 

**史观**：经验优先（总纲第 9 条——经验优先：以寄存器 0 残值 02008000、版本 0x20 与三 IO APIC 完整转储为判据）
**辨析**：本块为单例完整档案，属 E7500 平台的标本级记录；其寄存器值只对该机有效，不得外推为芯片组通例。
**文献**：DSLXC-4829（`linux-smp.messages.1572870`，2002-08-05），全文见 `raw_source.raw_json`

## 23.9 【Linux社区】调度 tunables 之争与并发语义（5 例）

**要点（判定表逐字）**：William Tambe于2021年问Linux在任务迁移到不同CPU时是否调用local_flush_tlb_mm及在代码库何处发生，为遗留列表上的现代TLB语义咨询；Raz公告SOS服务导向调度器平台旨在把服务指派给卸载处理器，称Rik van Riel已表态并已在sourceforge建库提交微秒定时器示例；Con Kolivas原文裁定现有tunables与cpu/mem/ctxt性能间并无有意义的关联，导出无人理解的旋钮并无助益，为p30 Davidsen引文的引用源；Michael Andrescavage在P4DPE双Xeon四逻辑CPU上给出定量对照：SMP内核60秒约400万事务且每秒17万次上下文切换，单CPU内核60秒约900万事务仅3.3万次切换；Mike Galbraith裁定调度旋钮效果微妙以致不宜导出，即使仔细研读代码也难以预测微调的全效果

**史料**：`1572839`、`1572843`、`1572845`、`1572853`、`1572874`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572839 -->` `<!-- ROW_MINE: linux-smp.messages.1572843 -->` `<!-- ROW_MINE: linux-smp.messages.1572845 -->` `<!-- ROW_MINE: linux-smp.messages.1572853 -->` `<!-- ROW_MINE: linux-smp.messages.1572874 -->` 

**史观**：经验优先（总纲第 9 条——经验优先：以 SMP 与单 CPU 内核的事务量（400 万／900 万）与上下文切换（17 万／3.3 万）定量对照为判据）；知识注定过时（总纲第 22 条——知识注定过时：2021 年的 TLB 语义咨询属遗留列表上的现代问题）
**辨析**：Kolivas 与 Galbraith 的“不宜导出旋钮”为维护者判词；SOS 调度器公告为项目自述，其“Rik van Riel 已表态”系转述，落书须与原话核对。
**文献**：DSLXC-4800、DSLXC-4804、DSLXC-4806、DSLXC-4814、DSLXC-4833（`linux-smp.messages.1572839`、`linux-smp.messages.1572843`、`linux-smp.messages.1572845`、`linux-smp.messages.1572853`、`linux-smp.messages.1572874`，2021-09-21、2008-09-06、2006-04-03、2002-08-29、2006-04-03），全文见 `raw_source.raw_json`

## 23.10 【Linux社区】内核语义与 TLS 前史（3 例）

**要点（判定表逐字）**：Srinivas G.报告同一驱动在2.4.18-3编译通过而在-3smp下hw_irq.h:202报current未声明，暴露UP与SMP头文件差异的编译门槛；Andrew Perepechko求内存屏障判读规则：wake_up隐含写屏障却未见于文档，问哪些内核例程提供屏障并求Unreliable Guide之外更可靠指南；J.A. Magallon求不用pthreads的per-thread全局变量方案：拟以clone直用模拟get与setspecific，提及__thread修饰符与IRIX的PRDA，为TLS设计前史第四声部

**史料**：`1572865`、`1572866`、`1572879`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572865 -->` `<!-- ROW_MINE: linux-smp.messages.1572866 -->` `<!-- ROW_MINE: linux-smp.messages.1572879 -->` 

**史观**：经验优先（总纲第 9 条——经验优先：以 UP 与 SMP 头文件差异致 current 未声明这一可复现编译门槛为判据）；知识注定过时（总纲第 22 条——知识注定过时：内存屏障与 PRDA 方案均属旧知，文档缺口至今可见）
**辨析**：三条分属编译门槛、内存屏障与 TLS 前史三个议题；Perepechko 所求“更可靠指南”在本页未见答复。
**文献**：DSLXC-4825、DSLXC-4826、DSLXC-4838（`linux-smp.messages.1572865`、`linux-smp.messages.1572866`、`linux-smp.messages.1572879`，2004-03-19、2004-11-22、2002-07-12），全文见 `raw_source.raw_json`

## 23.11 【Linux社区】崩溃与老平台三态（3 例）

**要点（判定表逐字）**：Diego报告Supermicro 6022P-6在2.2.26-rpd上出现wait_on_bh CPU6的irq与bh计数转储，为2.2时代SMP下半部处理故障样本；Aaron Tokhy报告PS3 Cell/PPC64上2.6.27软锁死61秒，调用栈停在csd_flag_wait与smp_call_function_single，背景为ps3vram补丁将显存MTD设备作swap；Richard Weinberger报告GA-586DX双MMX 200在2.4.18上大量APIC错误十二小时内崩溃，noapic则不报错但数日后仍崩，2.2.19一切正常

**史料**：`1572847`、`1572877`、`1572878`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572847 -->` `<!-- ROW_MINE: linux-smp.messages.1572877 -->` `<!-- ROW_MINE: linux-smp.messages.1572878 -->` 

**史观**：经验优先（总纲第 9 条——经验优先：以软锁死 61 秒调用栈、noapic 后不报错但仍崩等实测为判据）；偶然性优先（总纲第 5 条——没有必然性，只有偶然性：同板在 2.2.19 正常而 2.4.18 崩溃）
**辨析**：三例均未见闭环；Aaron Tokhy 的 PS3 案例涉背景补丁（ps3vram 将显存作 swap），本块按当事人自述保留该背景，不作因果裁断。
**文献**：DSLXC-4808、DSLXC-4836、DSLXC-4837（`linux-smp.messages.1572847`、`linux-smp.messages.1572877`、`linux-smp.messages.1572878`，2004-08-21、2008-10-13、2002-10-22），全文见 `raw_source.raw_json`

## 23.12 【Linux社区】责任归属与处置建议（3 例）

**要点（判定表逐字）**：Alan Cox对RH 2.4.18-3smp报障者只答一句先升级到勘误内核，为发行版勘误内核治理的直接表述；Alan Cox对双Athlon XP tar挂起案裁定Promise二进制RAID模块的问题应找Promise解决，为闭源模块责任归属句；peter.gantner答Intel员工求2.6.8-2 smp内核镜像：给出Debian包检索URL与trendmicro厂商模块页，为发行版包检索求助样本

**史料**：`1572873`、`1572882`、`1572885`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572873 -->` `<!-- ROW_MINE: linux-smp.messages.1572882 -->` `<!-- ROW_MINE: linux-smp.messages.1572885 -->` 

**史观**：法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：闭源模块责任被明确推回原厂）；多方平等（总纲第 8 条——本体论上各方平等：维护者裁定与用户自助检索并置）
**辨析**：Cox 的“先升级到勘误内核”为发行版治理的直接表述；“Promise 模块问题应找 Promise”为责任归属句，非技术诊断。
**文献**：DSLXC-4832、DSLXC-4841、DSLXC-4844（`linux-smp.messages.1572873`、`linux-smp.messages.1572882`、`linux-smp.messages.1572885`，2002-09-06、2002-09-05、2005-06-22），全文见 `raw_source.raw_json`

---
注：本文件由判定表程序化生成（23.1-23.12 共 12 块，覆盖 48/48 CAND，两遍计数核对通过）；要点逐字取自判定表“要点”列（主代理全读审读实录），史料锚与 CAND 一一对应，全文以 raw_source.raw_json 为准。
