# 22 【Linux社区】未知IO-APIC的版本白名单报告浪潮

> 对应页面：linux-smp p30（pk 1572788-1572837，2002-2015 混排）
> 判定：47 CAND / 3 NV（024 印尼语诈骗信、041 附件缺失、044 单行补版本号）
> 编号：DSLXC-4752..4798 | claim 已入库（47/47，dslinux_claims.duckdb）

## 22.1 【Linux社区】权威定性：known list 与警告语义（3 例）

**要点（判定表逐字）**：Alan Cox裁定未知的APIC本身不应构成问题，并反问遭遇IDE冻结者所用内核版本以判断警告消息的新旧，属警告语义的重要定性；Randy Dunlap给出权威定性即可安全忽略，仅表示内核已知版本清单中没有IO APIC版本3，与Nietzel的机制长文互为印证；Toth Szabolcs在SE7500CW2双Xeon上把IO-APIC提示误读为ACPI故障征询，附录与内核配置随信，显示用户侧对提示语主体的混淆

**史料**：`1572802`、`1572816`、`1572817`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572802 -->` `<!-- ROW_MINE: linux-smp.messages.1572816 -->` `<!-- ROW_MINE: linux-smp.messages.1572817 -->` 

**史观**：多方平等（总纲第 8 条——本体论上各方平等：Cox 裁定、Dunlap 定性与用户误读三声部并置）；经验优先（总纲第 9 条——经验优先：以已知版本清单与内核提示语的实际语义为判据）
**辨析**：三条分属维护者裁定、维护者定性与用户提问三个层级；“可安全忽略”为 2003 年时的定性，落书须与后续内核行为对照。
**文献**：DSLXC-4766、DSLXC-4779、DSLXC-4780（`linux-smp.messages.1572802`、`linux-smp.messages.1572816`、`linux-smp.messages.1572817`，2002-12-04、2002-10-24、2003-07-12），全文见 `raw_source.raw_json`

## 22.2 【Linux社区】OEM 与企业支持链路中的报告（3 例）

**要点（判定表逐字）**：Intel技术市场工程师Eric Paul代客户问询十条unexpected IO-APIC警告的含义，显示该警告已进入OEM售前支持链路；联邦机构系统管理员Fred Schneider按提示提交x235 x345 x360 x365 x445机群在2.4.9-e.48smp下的syslog打包，显示报告请求触发的企业响应；AT&T分析师Joanne Christian转贴SunFire V20z双Opteron 252的dmesg，其IO APIC 3与4版本0x11仅三条重定向项触发意外IO-APIC信息，服务器挂起需远程控制台恢复，转贴中另留有同行批注

**史料**：`1572809`、`1572823`、`1572799`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572809 -->` `<!-- ROW_MINE: linux-smp.messages.1572823 -->` `<!-- ROW_MINE: linux-smp.messages.1572799 -->` 

**史观**：多方平等（总纲第 8 条——本体论上各方平等：OEM 售前、联邦机构与运营商三类报告者并置）；偶然性优先（总纲第 5 条——没有必然性，只有偶然性：企业响应由内核提示语要求回信这一偶然设计触发）
**辨析**：三例均为企业链路中的转述与打包，非维护者结论；AT&T 一例附有同行批注，落书须区分转贴者与原批注者。
**文献**：DSLXC-4773、DSLXC-4786、DSLXC-4763（`linux-smp.messages.1572809`、`linux-smp.messages.1572823`、`linux-smp.messages.1572799`，2002-08-14、2004-08-06、2007-02-09），全文见 `raw_source.raw_json`

## 22.3 【Linux社区】2.4.21 新版措辞与 0x20 白名单外（4 例）

**要点（判定表逐字）**：Marco Wertejuk记录P4超线程平台上2.4.20-18.9smp出现新版措辞的信息即发现意外IO-APIC且内核发布不足三个月请报告，并称未察觉系统行为变化；Frédéric CHUONG在Asus P4C800 Deluxe单P4 2.4G自编2.4.21后按新版信息要求附上完整内容，是2.4.21发布周内的新版消息报告；Marco Iannacone在SuSE 9.0的P4C800 Deluxe上以2.4.21-273-smp4G录得IO APIC版本0x20意外信息并附完整重定向表，ACPI解释器已启用；Red Hat销售工程师Brian Mikkelsen坦承不知答案并引导提工单，其引用内容保存了USGS用户P4P800-VM上IO APIC版本0x20超出白名单并致系统迟滞的唯一存档记录

**史料**：`1572795`、`1572806`、`1572834`、`1572820`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572795 -->` `<!-- ROW_MINE: linux-smp.messages.1572806 -->` `<!-- ROW_MINE: linux-smp.messages.1572834 -->` `<!-- ROW_MINE: linux-smp.messages.1572820 -->` 

**史观**：知识注定过时（总纲第 22 条——知识注定过时：2.4.21 新版措辞与 0x20 白名单外随版本更替而变动）；经验优先（总纲第 9 条——经验优先：以各版本实测录得的版本号 0x20 与完整重定向表为判据）
**辨析**：四例均为 2.4.21 发布周内的报告；Brian Mikkelsen 的转引保存了 USGS 用户的唯一存档记录，其“系统迟滞”为当事人描述，未见量化。
**文献**：DSLXC-4759、DSLXC-4770、DSLXC-4795、DSLXC-4783（`linux-smp.messages.1572795`、`linux-smp.messages.1572806`、`linux-smp.messages.1572834`、`linux-smp.messages.1572820`，2003-06-27、2003-06-15、2005-02-01、2004-03-18），全文见 `raw_source.raw_json`

## 22.4 【Linux社区】寄存器与版本号标本（3 例）

**要点（判定表逐字）**：用户Und3rGr0und带随机死锁贴出VIA vt8233平台双PIII 1133完整dmesg，IO APIC版本0002触发警告，同机aic7xxx另报PCI数据奇偶错误；Andy Igoshin报告P4 3.06英特尔主板2.4.20下IO APIC寄存器0值为02008000即物理APIC ID 02带簇ID位触发WARNING unexpected IO-APIC；Carlos Madrid在P4 1.8 MSI 6524上录得IO APIC版本0x14意外警告并问是否与其eth0故障相关

**史料**：`1572791`、`1572800`、`1572827`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572791 -->` `<!-- ROW_MINE: linux-smp.messages.1572800 -->` `<!-- ROW_MINE: linux-smp.messages.1572827 -->` 

**史观**：经验优先（总纲第 9 条——经验优先：以版本 0002、寄存器 0 值 02008000、版本 0x14 三例实测为判据）；多方平等（总纲第 8 条——本体论上各方平等：警告与 aic7xxx 奇偶错误并置而不强作因果）
**辨析**：三例均为个别转储；Carlos Madrid 的“是否与 eth0 故障相关”为提问，本页无维护者裁定，落书须保留其未决。
**文献**：DSLXC-4755、DSLXC-4764、DSLXC-4790（`linux-smp.messages.1572791`、`linux-smp.messages.1572800`、`linux-smp.messages.1572827`，2002-09-16、2003-01-18、2002-12-19），全文见 `raw_source.raw_json`

## 22.5 【Linux社区】警告与真实中断回归同机绑定（2 例）

**要点（判定表逐字）**：Greg Norris报告i875P平台2.4.21-rc7启用IO-APIC即在IDE重负载下丢中断而禁用后稳定，把未知IO-APIC警告与真实功能回归绑定在同机；devik报告SiS 5513平台MSI 8533启用IO-APIC后RTL8139被指到IRQ18却收不到中断，pirq改指11仍无效，不启用则正常，并主动提供root权限配合排查

**史料**：`1572797`、`1572826`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572797 -->` `<!-- ROW_MINE: linux-smp.messages.1572826 -->` 

**史观**：经验优先（总纲第 9 条——经验优先：以启用 IO-APIC 即丢中断、禁用即稳定这一可复现对照为判据）；动手者叙事（总纲第 10 条——动手者创造历史：以同机前后对照与 pirq 改指等操作为分析单位）
**辨析**：两条把警告与真实功能回归绑定在同一台机器上，属高价值反例；但因果仍止于当事人自证，落书不得写成警告导致故障。
**文献**：DSLXC-4761、DSLXC-4789（`linux-smp.messages.1572797`、`linux-smp.messages.1572826`，2003-06-04、2002-11-26），全文见 `raw_source.raw_json`

## 22.6 【Linux社区】EBDA 警告线与挂起案闭环（5 例）

**要点（判定表逐字）**：巴西坎皮纳斯大学用户Cristiano de Mello Gallep报告2003-03-25重装系统后首次启动即现unexpected IO-APIC警告随后系统停止不再继续，构成警告伴随启动挂起的又一实例；IBM工程师Scott Playle报告x235双Xeon DP四逻辑处理器在2.4.18-14上出现EBDA中MP表可能不安全警告且系统间歇性挂起需复位，属EBDA警告与真实故障并报的企业案例；Krajcsovits Gyorgy续报x230换用vanilla 2.4.20-pre5十二小时后干净自重启且打印了关机消息，Alan Cox指出EBDA警告仅适用于老旧引导器不太可能相关；x230自重启悬案告破即网页设计者误判死机请技术员重启机器，Alan Cox顺带讲出有人在cron埋重启命令被解雇的旧事；Bruce M Beach追问2.4.20-pre5在何处下载，间接记录x230挂起案的修复路径为升内核或换IBM ServeRAID固件，并暴露预补丁不在v2.4主目录造成的检索困惑

**史料**：`1572788`、`1572789`、`1572810`、`1572824`、`1572796`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572788 -->` `<!-- ROW_MINE: linux-smp.messages.1572789 -->` `<!-- ROW_MINE: linux-smp.messages.1572810 -->` `<!-- ROW_MINE: linux-smp.messages.1572824 -->` `<!-- ROW_MINE: linux-smp.messages.1572796 -->` 

**史观**：偶然性优先（总纲第 5 条——没有必然性，只有偶然性：挂起案闭环由“网页设计者误判死机”这一偶然人为因素告破）；经验优先（总纲第 9 条——经验优先：以换内核后十二小时干净自重启等实测为判据）
**辨析**：Cox 指 EBDA 警告仅适用老旧引导器，系 2006 年时的技术判断；末条“cron 埋重启命令被解雇”为当事人所述旧事，属轶事材料，只作存录。
**文献**：DSLXC-4752、DSLXC-4753、DSLXC-4774、DSLXC-4787、DSLXC-4760（`linux-smp.messages.1572788`、`linux-smp.messages.1572789`、`linux-smp.messages.1572810`、`linux-smp.messages.1572824`、`linux-smp.messages.1572796`，2003-03-25、2003-06-18、2002-08-30、2002-08-30、2002-09-07），全文见 `raw_source.raw_json`

## 22.7 【Linux社区】单 CPU 检出与老牌平台（4 例）

**要点（判定表逐字）**：J. Milgram的Micron双P-Pro只被认出一颗CPU且MP表Processors为1，跳线无针无法切换，1995年BIOS下MPS在1.1与1.4间调换无效，2.2.19还会自重启，syslog另报符号表版本号不正确；Antonio Weber的单Athlon XP 2100日志记录内核自动关闭AMD高级投机缓存特性并报仅找到一个处理器，IO APIC版本0002同触警告，VIA桥IRQ修正同现；Jurriaan在MSI Pro266TD-LR双Tualatin DDR的VIA266平台上以2.5.50录得IO APIC版本0002警告并附完整dmesg，为2.5开发线上少见的该型板报告；Joe Archibald的IBM PC Server 325双PPro 200时见双CPU时见单CPU并伴APIC错误信息，EBDA警告同现，RedHat Mandrake debian多发行版均复现

**史料**：`1572835`、`1572829`、`1572836`、`1572814`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572835 -->` `<!-- ROW_MINE: linux-smp.messages.1572829 -->` `<!-- ROW_MINE: linux-smp.messages.1572836 -->` `<!-- ROW_MINE: linux-smp.messages.1572814 -->` 

**史观**：经验优先（总纲第 9 条——经验优先：以 MP 表 Processors 计数、跳线无针可调等硬件实况为判据）；知识注定过时（总纲第 22 条——知识注定过时：1995 年 BIOS 与 MPS 1.1／1.4 的兼容已成旧知）
**辨析**：四例为老牌平台的单 CPU 检出与警告并报；Milgram 与 Archibald 的多发行版复现提升了可重复性，但根因在本页未见裁定。
**文献**：DSLXC-4796、DSLXC-4791、DSLXC-4797、DSLXC-4777（`linux-smp.messages.1572835`、`linux-smp.messages.1572829`、`linux-smp.messages.1572836`、`linux-smp.messages.1572814`，2002-04-21、2002-12-16、2002-12-25、2003-10-19），全文见 `raw_source.raw_json`

## 22.8 【Linux社区】HT 启用困惑与 noht 性能语义（4 例）

**要点（判定表逐字）**：Bill Davidsen与Eff Norwood问答确认单颗P4无BIOS超线程开关而内核报hyperthread disabled，追问如何命令内核开启，反映2002年HT无任何用户级接口；Alan Cox总结SMP机器不比单机快的两大常见原因即内存带宽受限进程拖垮扩展性，以及双Xeon HT跑四个吃内存任务反而更慢建议noht并疑为缓存抖动；Urs Thuermann问双核与双CPU之别，指出HT仅复制程序状态而共享执行逻辑常致性能损失，并推断双核共享总线接口，代表2006年社区对片上多核的认知水平；Ole Lindbjerg称在DELL上开启超线程后Mandrake发现错误而XP驱动正常，日志随附件，提示开启HT本身即可诱发该报告

**史料**：`1572804`、`1572812`、`1572813`、`1572819`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572804 -->` `<!-- ROW_MINE: linux-smp.messages.1572812 -->` `<!-- ROW_MINE: linux-smp.messages.1572813 -->` `<!-- ROW_MINE: linux-smp.messages.1572819 -->` 

**史观**：知识注定过时（总纲第 22 条——知识注定过时：2002 年 HT 无任何用户级接口、2006 年社区对片上多核的认知均属阶段性知识）；经验优先（总纲第 9 条——经验优先：以 noht 后反而更慢、内存带宽受限等实测为判据）
**辨析**：Cox 的“两大常见原因”为经验归纳；Thuermann 的双核推断为当时认知，落书须标明其为 2006 年的社区认识水平而非结论。
**文献**：DSLXC-4768、DSLXC-4775、DSLXC-4776、DSLXC-4782（`linux-smp.messages.1572804`、`linux-smp.messages.1572812`、`linux-smp.messages.1572813`、`linux-smp.messages.1572819`，2002-11-18、2002-08-28、2006-04-23、2003-11-06），全文见 `raw_source.raw_json`

## 22.9 【Linux社区】每 CPU 语义、线程上限与调度争论（6 例）

**要点（判定表逐字）**：Mark Hapke发现get/put_user在ISR与用户进程分处不同CPU时返回EFAULT而同CPU正常，怀疑current取自每CPU栈所致，是2.4内核每CPU语义的用户侧观察；Earle R. Nietzel实测Java虚拟机线程上限在RH9 2.4.20-9smp约3660个才OutOfMemory而RH8 2.4.18-27smp约1400个，并提示须考虑内核用户态与内核态内存划分；Mike Galbraith裁定rt_nr_running非零而活跃位图无有效位的状态必然意味着内核已坏，建议剔除专有模块并审计futex修复，指出3.2比3.1多一批futex修复；Robert M. Hyatt以多处理器执行内核代码如何自保反问mutex与缓存一致性协议之争，引文中Xu Yang论证单核多线程下仅靠缓存一致性协议不足以保护共享资源；Bill Davidsen参与调度器procfs可调项之争，引Con Kolivas论无人能理解的导出项并无助益，补充低HZ与swappiness对低端机2.6体验的影响；Lars Michael Jogbäck发现2.6.8.1在双PIII 500的P2B-D上中断几乎全部落在CPU0而2.4则分布均匀，附/proc/interrupts逐行计数，CONFIG_IRQBALANCE已开

**史料**：`1572792`、`1572808`、`1572793`、`1572832`、`1572833`、`1572815`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572792 -->` `<!-- ROW_MINE: linux-smp.messages.1572808 -->` `<!-- ROW_MINE: linux-smp.messages.1572793 -->` `<!-- ROW_MINE: linux-smp.messages.1572832 -->` `<!-- ROW_MINE: linux-smp.messages.1572833 -->` `<!-- ROW_MINE: linux-smp.messages.1572815 -->` 

**史观**：经验优先（总纲第 9 条——经验优先：以 get/put_user 跨 CPU 返回 EFAULT、JVM 线程上限 3660／1400 等实测为判据）；动手者叙事（总纲第 10 条——动手者创造历史：以 /proc/interrupts 逐行计数为分析单位）
**辨析**：六例跨 2002-2004，涉及每 CPU 语义、线程上限与调度器导出项三个层面；Galbraith 的“内核已坏”为排错判据，非缺陷定论。
**文献**：DSLXC-4756、DSLXC-4772、DSLXC-4757、DSLXC-4793、DSLXC-4794、DSLXC-4778（`linux-smp.messages.1572792`、`linux-smp.messages.1572808`、`linux-smp.messages.1572793`、`linux-smp.messages.1572832`、`linux-smp.messages.1572833`、`linux-smp.messages.1572815`，2002-05-23、2003-04-17、2015-09-07、2007-09-03、2006-04-07、2004-10-29），全文见 `raw_source.raw_json`

## 22.10 【Linux社区】大机架 Summit/SRAT 标本与文档线（4 例）

**要点（判定表逐字）**：S.K.Goel转贴IBM VIGIL SMP的16路Xeon MP 1.5G开机日志含SRAT表启用16CPU、Summit芯片组Cyclone计数器、ACPI表与CPU MSR值关于CPU数不匹配提示、IO APIC版本0x11两次意外信息及runqueue向兄弟队列映射，是RHEL 2.4.21-15.0.3.ELsmp大机架启动的完整标本；Alan Cox裁定x440并非寻常PC需IBM未并入主线的内核补丁，Bill Davidsen追问sibling map与应见四CPU，记录Summit平台支持缺口与HT预期；SMP HOWTO维护者Enkh确认将Randy Dunlap更新的MP规范1.1对1.4对照文档并入HOWTO，为该对照资料进入官方文档链路的直接证据；Cisco工程师Jarrett L. Redd求APIC IO-APIC与local APIC三者区别的系统读物，直言散落数据表令人困惑，反映入门文档缺口

**史料**：`1572825`、`1572818`、`1572794`、`1572830`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572825 -->` `<!-- ROW_MINE: linux-smp.messages.1572818 -->` `<!-- ROW_MINE: linux-smp.messages.1572794 -->` `<!-- ROW_MINE: linux-smp.messages.1572830 -->` 

**史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 16 路机架的完整启动日志为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：厂商补丁缺口与用户预期落差并置）
**辨析**：Cox 裁定 x440 需 IBM 未并入主线的补丁，属厂商支持缺口的一手；HOWTO 并档一条为文档链路的直接证据，落书须与 HOWTO 版本核对。
**文献**：DSLXC-4788、DSLXC-4781、DSLXC-4758、DSLXC-4792（`linux-smp.messages.1572825`、`linux-smp.messages.1572818`、`linux-smp.messages.1572794`、`linux-smp.messages.1572830`，2004-07-08、2002-12-03、2002-06-10、2002-07-18），全文见 `raw_source.raw_json`

## 22.11 【Linux社区】驱动替代、APM 关机与 noapic 反方证词（3 例）

**要点（判定表逐字）**：Kosta以自身经历建议以e100替换eepro100解决Supermicro P4DC6超线程平台的网卡问题；Dieter Jurzitza的Tyan 2460双Athlon MP在shutdown后不关电源且偶发自行重启，研读apm.c后询问realmode_power_off与power_off两参数的关系；E. Robert Bogusta以Netfinity 8658实证反驳MPS 1.1建议称改设后内核摆弄板载SCSI近一小时后锁死，并主张noapic在Netfinity BP6与Intel板上换来稳定，性能损失测不出而锁死代价实在

**史料**：`1572821`、`1572805`、`1572822`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572821 -->` `<!-- ROW_MINE: linux-smp.messages.1572805 -->` `<!-- ROW_MINE: linux-smp.messages.1572822 -->` 

**史观**：经验优先（总纲第 9 条——经验优先：以换用 e100 后网卡问题消失、MPS 1.1 改设后锁死等实测为判据）；多方平等（总纲第 8 条——本体论上各方平等：noapic 反方证词与主流建议并置）
**辨析**：Bogusta 的反驳系 Netfinity 8658 单机实证，其“性能损失测不出”为个人测量；本块保留其反方立场，不写作普适处方。
**文献**：DSLXC-4784、DSLXC-4769、DSLXC-4785（`linux-smp.messages.1572821`、`linux-smp.messages.1572805`、`linux-smp.messages.1572822`，2003-02-28、2002-06-12、2002-06-18），全文见 `raw_source.raw_json`

## 22.12 【Linux社区】消费级平台报告流与 4GB 停滞（6 例）

**要点（判定表逐字）**：sara sodagar报告双PIII 1000装RedHat 7.1后启动即见unexpected IO-APIC无法进入系统，为伊朗用户侧的安装阻断案例；Hiroaki Munakata报告ASUS CU4X-D双CPU装RH7.1启动失败并出现WARNING unexpected IO-APIC，附文档随信；Ruediger Otte在Gigabyte GA-7VTXH与Athlon XP上以2.4.20rc1录得WARNING unexpected IO-APIC并按提示上报；James W. Laferriere自标OFF TOPIC报告Tyan Thunder 2567配四条1G内存自检在3998848KB处停滞于Wait提示并发出一长三短蜂鸣，任意两条却稳定，附全lspci，为ServerWorks CNB20HE平台大内存BIOS卡死实例；karl wettin的BP6双Celeron 400启动X即五分钟后锁死需冷启动，重编译全系统无效，换用Gentoo stage 3后SMP与XFree均正常，属发行版切换自愈案例；Ben Osborne在RHAS 2.1双Xeon HT服务器上录得三连unexpected IO-APIC警告并附完整启动日志与cpu_sibling_map配对输出，问是否真问题

**史料**：`1572801`、`1572803`、`1572807`、`1572837`、`1572798`、`1572790`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: linux-smp.messages.1572801 -->` `<!-- ROW_MINE: linux-smp.messages.1572803 -->` `<!-- ROW_MINE: linux-smp.messages.1572807 -->` `<!-- ROW_MINE: linux-smp.messages.1572837 -->` `<!-- ROW_MINE: linux-smp.messages.1572798 -->` `<!-- ROW_MINE: linux-smp.messages.1572790 -->` 

**史观**：经验优先（总纲第 9 条——经验优先：以启动即阻断、自检停滞 3998848KB、换 Gentoo 后自愈等实测为判据）；偶然性优先（总纲第 5 条——没有必然性，只有偶然性：同一硬件在不同发行版下结局相异）
**辨析**：六例中 Laferriere 自标 OFF TOPIC，属大内存 BIOS 问题而非 IO-APIC 议题，本块按其自标保留该界限；发行版切换自愈一例未见根因。
**文献**：DSLXC-4765、DSLXC-4767、DSLXC-4771、DSLXC-4798、DSLXC-4762、DSLXC-4754（`linux-smp.messages.1572801`、`linux-smp.messages.1572803`、`linux-smp.messages.1572807`、`linux-smp.messages.1572837`、`linux-smp.messages.1572798`、`linux-smp.messages.1572790`，2002-06-11、2002-04-11、2002-11-14、2002-08-20、2003-09-21、2003-05-23），全文见 `raw_source.raw_json`

---
注：本文件由判定表程序化生成（22.1-22.12 共 12 块，覆盖 47/47 CAND，两遍计数核对通过）；要点逐字取自判定表“要点”列（主代理全读审读实录），史料锚与 CAND 一一对应，全文以 raw_source.raw_json 为准。
