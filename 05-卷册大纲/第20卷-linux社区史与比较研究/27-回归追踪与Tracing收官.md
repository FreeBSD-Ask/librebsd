# 27 【Linux社区】回归追踪与Tracing收官

> 对应页面：ksummit-discuss p79（pk 348156-348205，2017-06-29/07-05 多线程并进 + 2014 档案信）
> 判定：50 CAND / 0 NV
> 编号：DSLXC-4982..5031 | claim 已入库（50/50，dslinux_claims.duckdb）

## 27.1 【Linux社区】Tracing ABI 收官：Linus 与 Rostedt 七轮对撞及 eBPF 之争（10 例）

**要点（判定表逐字）**：Rostedt驳Linus填零方案：填零解不了新增关键信息之需，SCHED_DEADLINE是新东西，其在Red Hat时曾自加tracepoint、Mathieu亦如此、SuSE或亦然，人人须打补丁取信息；并反讽Linus此言与社区一向担忧正相反——原怕tracepoint牵制内核开发，如今却是任其腐烂致用处受限；Linus：我也反对在sched_switch处设多个tracepoint；谁关心某一调度器就自己加动态tracepoint，别动既有的、把不再有意义的字段填零，别再鞭这匹死马——它已死了三年且不只是在发臭，还在以吓人的方式膨胀；静态tracepoint存在的唯一理由是powertop一类大工具，绝无可能关心只属某一调度器实现的字段；此事到此为止，尤其不想成为峰会议题；Rostedt反问Linus是否用过tracepoint，并指SCHED_DEADLINE信息非kprobes或eBPF所能轻易提取，世间用工具的亦非只有powertop；自陈一直尽力让tracing保持内聚、不让实现细节渗入内核其余部分，所谋方案皆以不扰动他处为第一要求，如今此议作罢，待需求沸腾到Linus眼前再说；Rostedt补正被删节的原文：PeterZ反对sched_switch设多tracepoint，偏好动态情形以免为得完整功能须全开tracepoint，因其惯用echo与cat操ftrace而不愿为sched_switch多开一个；并追问Linus所谓动态tracepoint是否即指此物——它尚不存在，既非kprobes亦非eBPF，原拟在ksummit讨论其实现；Linus：我不用tracepoint，但拒见此类无谓churn，更拒拿到ksummit讨论——tracing议题谈了数年未见可行成果；静态tracepoint只许generic内容，不许只对一个调度类有意义的随机内部字段，prio字段教训在前而如今又要加同类新字段；要挖调度器细节者自建私有tracepoint，别妄称通用；问何不把eBPF脚本挂到既有的那一个tracepoint上；Rostedt：eBPF方案同病——只能访问tracepoint已导出的字段，绕回哪些字段可见、不再有意义时怎么办的老问题，终须逐版改一次eBPF脚本；Linus：不会出席该讨论，维护者层面不当为ksummit议题，此属技术细节应与相关者谈或开BOF；自陈所指与PeterZ相近——把eBPF脚本挂kprobes动态取数，eBPF tracepoint已支持多年，究竟缺什么；并说这正是eBPF用于tracing当初被推销的承诺；Rostedt：原帖标TECH TOPIC本就只给感兴趣者，非为维护者峰会；厘清ksummit两层——Linus手点的Maintainer Summit与面向更众人的技术议题扩展，本列表借主题标签区分二者；指eBPF在tracing仍很局限、目下只实现于perf，把它接入ftrace亦在其待办与议程上，且eBPF尚缺易用的用户态工具；仍欲在Kernel Summit设TECH TOPIC；Linus：想不出除eBPF外如何使其动态，eBPF在网络侧显然跑得很好是显然解；但强调那是网络侧自己把它做成的，eBPF亦需基础设施方能稳妥取数；自承误以为eBPF已不限于perf，惊讶其未与ftrace互通而谓此似完美用例；Rostedt同意并允将eBPF入tracing提高优先级，指其亦可改善仍以树逻辑实现的过滤；并提醒如何把eBPF载入ftrace本身即是ABI问题，须一次做对否则数年后反噬

**史料**：`348156`、`348158`、`348159`、`348160`、`348161`、`348162`、`348163`、`348164`、`348165`、`348166`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348156 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348158 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348159 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348160 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348161 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348162 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348163 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348164 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348165 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348166 -->` 

**史观**：知识注定过时（总纲第 22 条——知识注定过时：静态 tracepoint 字段随调度器实现而失义，Linus 谓“把不再有意义的字段填零”）；多方平等（总纲第 8 条——本体论上各方平等：Linus 的“此事到此为止”与 Rostedt 的逐轮反驳、PeterZ 偏好单一静态 tracepoint 三方并列）
**辨析**：Linus 的“别再鞭这匹死马——它已死了三年”“静态 tracepoint 只许 generic 内容”为顶层裁定；Rostedt 的“eBPF 只能访问 tracepoint 已导出的字段，终须逐版改脚本”为技术反驳，其“eBPF 在 tracing 仍很局限、目下只实现于 perf”为状态自陈；PeterZ 偏好动态情形系 Rostedt 补正之转述。
**文献**：DSLXC-4982、DSLXC-4984、DSLXC-4985、DSLXC-4986、DSLXC-4987、DSLXC-4988、DSLXC-4989、DSLXC-4990、DSLXC-4991、DSLXC-4992（`ksummit-discuss.messages.348156`、`ksummit-discuss.messages.348158`、`ksummit-discuss.messages.348159`、`ksummit-discuss.messages.348160`、`ksummit-discuss.messages.348161`、`ksummit-discuss.messages.348162`、`ksummit-discuss.messages.348163`、`ksummit-discuss.messages.348164`、`ksummit-discuss.messages.348165`、`ksummit-discuss.messages.348166`，2017-06-30、2017-06-30、2017-06-30、2017-06-30、2017-06-30、2017-06-30、2017-06-30、2017-06-30、2017-06-30、2017-06-30），全文见 `raw_source.raw_json`

## 27.2 【Linux社区】Tracing：Alexei 的 perf＋bpf 抗辩与 PeterZ 自述（8 例）

**要点（判定表逐字）**：Alexei Starovoitov：若Steven有用例则不反对为ftrace加bpf，但看不出价值，perf_events加bpf脚本已能看想看的一切；举bcc的runqlen.py直方图与biosnoop.py因struct request反复变更而用条件编译适配为例，谓想看内核内部结构就该准备逐版改脚本，此事众所周知；并谓重读Mathieu原信不解其欲解者为何；声明不为tracing讨论飞布拉格，netdev2.2与九月plumbers的tracing microconf更合宜；Rostedt提醒LPC Tracing Microconf的WIKI久已停滞，若要被接受须尽快有提案；Rostedt补注：Mathieu已声明不出席Plumbers，Peter亦可能不出席，因有更小的事要照料；Rostedt答Bacik：不该用talk一词，此处全为讨论，若需多于一张幻灯片便已太多；可就trace event问题起头，但PeterZ与Mathieu不在则无意义；动态字段设想与Zanussi最新histogram工作皆值一谈；并申明自己身兼LPC程序委员会，不愿再揽过多责任；Rostedt因漏将Tom Zanussi加入抄送而重发上封，内容为021全文引用，仅补Cc与一行说明；Josef Bacik：允开始催人提交提案（先催Rostedt），自己一两日内交提案，并谓Brendan有内容可讲；Josef Bacik：Plumbers对tracing是怪场地，本期望Brendan一类sysadmin到场直说tracing哪里糟然后去修，实际并不如此，而tracing ABI这类讨论房间里没有对的人；自嘲提案不过是些让自己省事的清单，不值一整个microconf听他抱怨一小时；若无人可谈则干脆宣布tracing功能完备改谈别的；PeterZ：Yay, tracing fight；两点诉求——代码里只要一个静态tracepoint、用户态只关联一个event，若同地出sched_switch_fair／rt／deadline三事件必生混乱（人忘开其一而困惑于trace有洞）；此约束在其看来并不苛刻，难在实现；自陈可接受在既有一点上添字段而Steve嫌贵；坦言只用tracefs接口，不会也不想学perf、trace-cmd与eBPF，改内核重建重启远比弄懂eBPF省事（类比宁用sysvinit），结以婴儿吐奶也比此话题有趣

**史料**：`348167`、`348169`、`348170`、`348176`、`348177`、`348182`、`348183`、`348195`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348167 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348169 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348170 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348176 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348177 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348182 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348183 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348195 -->` 

**史观**：经验优先（总纲第 9 条——经验优先：以 bcc 的 runqlen.py 直方图与 biosnoop.py 因 struct request 反复变更而条件编译适配等实测为判据）；多方平等（总纲第 8 条——本体论上各方平等：Starovoitov 的 perf＋bpf 抗辩与 Bacik 的“房间里没有对的人”、PeterZ 的“不会也不想学 eBPF”并置）
**辨析**：Starovoitov 的“perf_events 加 bpf 脚本已能看想看的一切”为 eBPF 侧主张，与 Rostedt 的“eBPF 只能访问已导出字段”构成两说，本页未见收敛；Bacik 的“若无人可谈则干脆宣布 tracing 功能完备”为激将之语，非结论；PeterZ 的“改内核重建重启远比弄懂 eBPF 省事”为个人取舍自陈。
**文献**：DSLXC-4993、DSLXC-4995、DSLXC-4996、DSLXC-5002、DSLXC-5003、DSLXC-5008、DSLXC-5009、DSLXC-5021（`ksummit-discuss.messages.348167`、`ksummit-discuss.messages.348169`、`ksummit-discuss.messages.348170`、`ksummit-discuss.messages.348176`、`ksummit-discuss.messages.348177`、`ksummit-discuss.messages.348182`、`ksummit-discuss.messages.348183`、`ksummit-discuss.messages.348195`，2017-06-30、2017-06-30、2017-06-30、2017-06-30、2017-06-30、2017-06-30、2017-06-30、2017-07-04），全文见 `raw_source.raw_json`

## 27.3 【Linux社区】回归追踪新线程十二连（12 例）

**要点（判定表逐字）**：Thorsten Leemhuis提案全文（迟到的新人自陈）：拟设维护者峰会与技术议题两场；维护者场三题——bugzilla.kernel.org后续（报告者仍被困于此）、如何让子系统维护者更多参与回归追踪、如何让回归追踪事业不再中断；技术场三题——峰会结论简报与遗留、如何拉发行版参与（点名Arch、Debian、Fedora、Tumbleweed并望Ubuntu）、如何自动追踪每条回归的状态与进展；详陈bugzilla静态页方案（依MAINTAINERS的B:字段或无则指邮件列表，并释get_maintainers.pl；仅ACPI与PM等少数子系统保留）、regressions@leemhuis.info的CC与转寄机制、Linux-Regression关键词与回归ID（如Corrects: Linux-Regression-d2afd）构想及据此写脚本监视邮件列表与git树填入数据库的远景；另列留待后议诸项（kerneloops现状、stable回归、统计、扩大测试者、流程文档、半自动催办、报告格式、社区与倦怠、使发行版停止内核fork的Firefox式设想）；Rostedt：三项议题的答案都是selftests——复现测试应尽入selftests，如此一望即知尚存哪些回归（自承亦时有遗忘而自勉）；以What is selftests作Jeopardy式答复；并断言发行版不会停内核fork（著名的遗言），因发行版要的是带新特性的stable而stable非此义；Dan Williams同意Rostedt并补充：写驱动回归测试未必需要特定硬件，举tools/testing/nvdimm为例；以测试兜住回归亦有助于缓解追踪者的倦怠，因造工具与测试比纯bug追踪更有成就感；Leemhuis：写跑selftests固然好，但如Rostedt自己所言于需特定硬件或稀有复杂配置者无助，而近期报告多数正属此类；且能被selftest抓到的回归多在子系统维护者处即被处理，从未到他手上故无从要求其写测试——若得知情则既可防遗忘、亦可在日后公开质问；并戏辩stable一词可解作毫无变化亦可解作坚如磐石，举Firefox ESR与Linus十三年前的开发模式为例；Rostedt：断定大量复现代码从未进入测试，建议有人专盯LKML寻我这样做就出bug、这是可触发的测试用例之迹并转为selftests；特殊硬件虽难亦应存入以供有此硬件者用，特殊配置则可设config test段（自己用ktest构建）；并澄清stable与Red Hat所谓stable的口径差异——stable创建时准入甚严，历年虽变，二者之别方是其谓不会改变处；Rostedt答Carlos O'Donell：内核没有好用的bug编号系统，多数内核开发者（含Linus）讨厌bugzilla，除非Linus造一个否则无从强制；虽盼每修一bug皆带测试，然每版上万改动而多属修复，至多只能靠荣誉制与适度羞辱（促人加Fixes标签同时附回归测试），须在促成改变与把人惹到反其道而行之间把握分寸；Greg KH：绝大多数修复系针对特定硬件或为其workaround，写测试纵非不可能（i915开发者即有其例）亦极难，尤在基础设施缺失时；以4.12-rc1后并入drivers/usb/host的十四条shortlog为证（ASMedia quirk、USB 3.1协议解析、xhci命令环停止回归、锁倒置等）反问此类如何写测试；谓内核约七成五为硬件与架构支持，故相应约七成五的改动与修复涉硬件；戏言若我管的子系统不必碰硬件该多好；Rostedt：若确为特定硬件，是否写测试当由维护者定，因多为应付硬件的怪癖与非标准；转而追问Thorsten硬件上真回归占比——自来如此的bug不是回归而是feature，回归是曾经好用如今不行；主张针对USB、显卡、网卡等的通用功能测试而非为单一硬件写测试，若众人跑通用测试触发失败则更易上报与修复；并对Greg戏言回以smack；Mark Brown：于Greg所述之外补一类——并发与锁问题的修复同样难以稳定复现；Rostedt：所有测试都应在lockdep开启下运行，而肯如此做的开发者少得惊人；James Bottomley：lockdep检验锁层级并对其作假设后加以验证，并不告诉你想保护的数据是否在锁外被访问，而后者才是并发问题的常见源；故lockdep有用而非万灵药；Mark Brown：常见情形是本就为bug、却需外部条件方显形——如有人以稍有不同方式使用设备、做更细致测试，或某子系统发生变更

**史料**：`348188`、`348191`、`348192`、`348196`、`348197`、`348198`、`348199`、`348200`、`348202`、`348203`、`348204`、`348205`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348188 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348191 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348192 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348196 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348197 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348198 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348199 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348200 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348202 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348203 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348204 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348205 -->` 

**史观**：动手者创造历史（总纲第 10 条——动手者创造历史：以复现测试尽入 selftests、tools/testing/nvdimm 例与 lockdep 全员开启的主张为分析单位）；经验优先（总纲第 9 条——经验优先：以 Greg KH 十四条 shortlog 反证、内核约七成五为硬件与架构支持等实数为判据）
**辨析**：Rostedt 的“三项议题的答案都是 selftests”与“发行版不会停内核 fork（著名的遗言）”为维护者判词；Greg KH 的“约七成五改动与修复涉硬件”为结构性归因；Bottomley 对 lockdep 能力边界的界定（只验锁层级假设、不告数据是否在锁外被访问）为工具定性，非否定。
**文献**：DSLXC-5014、DSLXC-5017、DSLXC-5018、DSLXC-5022、DSLXC-5023、DSLXC-5024、DSLXC-5025、DSLXC-5026、DSLXC-5028、DSLXC-5029、DSLXC-5030、DSLXC-5031（`ksummit-discuss.messages.348188`、`ksummit-discuss.messages.348191`、`ksummit-discuss.messages.348192`、`ksummit-discuss.messages.348196`、`ksummit-discuss.messages.348197`、`ksummit-discuss.messages.348198`、`ksummit-discuss.messages.348199`、`ksummit-discuss.messages.348200`、`ksummit-discuss.messages.348202`、`ksummit-discuss.messages.348203`、`ksummit-discuss.messages.348204`、`ksummit-discuss.messages.348205`，2017-07-02、2017-07-03、2017-07-03、2017-07-04、2017-07-05、2017-07-05、2017-07-05、2017-07-05、2017-07-05、2017-07-05、2017-07-05、2017-07-05），全文见 `raw_source.raw_json`

## 27.4 【Linux社区】Kconfig 余波：profileconfig 与片段分片（4 例）

**要点（判定表逐字）**：Rostedt提make profileconfig之想：在menuconfig顶部加Profiles菜单，只列虚拟化（KVM下Intel／AMD／两者、Paravirt）、网络（防火墙等）、电源管理、文件系统等常人会问的人类可读项；这些profile不生成CONFIG_定义、内核代码不得依赖，只负责select所需全部选项，可能多于所求但足以起步；并举Big Bang thermal governor为例讽现配置项无人能懂；Darren Hart：配置片段与merge_config.sh本即为此而设，举例make defconfig pdx86.config；坦言pdx86.config须脚本刮Kconfig生成，另欲加efi.config而未知众意；承Linus之叹而喜见非独我受Kconfig过度细碎之苦；并指片段与Kconfig同步是难题，可加configcheck目标审计；Darren Hart：宜有片段嵌套，可造simpleconfig再含若干更专门片段；并建议在make *config界面提供简单配置视图，枚举全部片段附元数据自描述，保存时执行make minconfig foo.config bar.config kvm.config efi.config dell.config；Hannes Reinecke：更妙者是默认即分片——不用巨型.config而按目录存放、与对应Kconfig同处；如此既易查某项该死的配置从何而来，又易为多机提供并校验配置（保留公共部分只改机器专属），且Kconfig变更时一眼可见须改哪份配置，同步问题自解

**史料**：`348173`、`348174`、`348175`、`348184`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348173 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348174 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348175 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348184 -->` 

**史观**：动手者创造历史（总纲第 10 条——动手者创造历史：以 make profileconfig 设想、merge_config.sh 与按目录分片的默认方案为分析单位）；知识注定过时（总纲第 22 条——知识注定过时：以 Big Bang thermal governor 为例讽现配置项无人能懂）
**辨析**：Rostedt 的“profile 不生成 CONFIG_ 定义、内核代码不得依赖”为设计约束；Hart 的“片段与 Kconfig 同步是难题，可加 configcheck 目标审计”为工具侧提议；Reinecke 的“默认即分片”为方案主张，本页未见采纳记录。
**文献**：DSLXC-4999、DSLXC-5000、DSLXC-5001、DSLXC-5010（`ksummit-discuss.messages.348173`、`ksummit-discuss.messages.348174`、`ksummit-discuss.messages.348175`、`ksummit-discuss.messages.348184`，2017-06-30、2017-06-30、2017-06-30、2017-07-01），全文见 `raw_source.raw_json`

## 27.5 【Linux社区】mobile：N900 音频特例与 430 毫欧之问（6 例）

**要点（判定表逐字）**：Reichel：音频非普遍问题而仅Nokia手机如此——其把原始音频数据送CPU，由Maemo用户态在DSP上后处理再经pulseaudio播放，故需约二十毫秒低延迟；其余手机基本都提供标准数字音频接口，只须正确配声卡即可出声；且现代4G基本走VoIP，厂商若再从modem去掉音频处理亦可在用户态以VoIP应用完成；Reichel：ofono有qmi插件但自己只用过qmi utils；GSM音频以数字音频接口连至codec，数据通常不过CPU（但可按需路由过去），故CPU侧无需低延迟处理，只须正确配置modem与codec；并评主线支持度——Droid4与N950大致相当，N900相机补丁落地后除GPU几近百分之百，然其慢且仅256MB内存；Reichel就Pavel电池补丁追问430毫欧内阻之值的来源，并顺带记Nokia亦为N900提供二进制驱动（已被逆向），N950另有一个且至今未逆向；Reichel：remoteproc只负责启停与固件加载，实际通信走rpmsg而后者尚无用户态API；且TI DSP目前没有开源工具链；故即便勉力为之，于N900收益亦微；Reichel答Pavel：Pyra提供的是普通PCM接口（引其原理图PDF第十一页），Nokia手机在这一点上确实特殊；Pavel：430毫欧是对其中一块电池的估算，真值随温度与电池老化等而变，但已显著优于假设内阻为零；自陈另有两块电池，并指Nokia二进制驱动是保留N900的又一理由

**史料**：`348178`、`348180`、`348185`、`348186`、`348187`、`348189`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348178 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348180 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348185 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348186 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348187 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348189 -->` 

**史观**：经验优先（总纲第 9 条——经验优先：以 N900 需约二十毫秒低延迟、Droid4 与 N950 主线支持度大致相当、430 毫欧为对一块电池的估算等实测为判据）；历史地理塑造思想土壤（总纲第 20 条——历史地理塑造思想土壤：Nokia 手机把原始音频送 CPU 由 Maemo 用户态后处理，属厂商路径依赖之特例）
**辨析**：Reichel 的“音频非普遍问题而仅 Nokia 手机如此”为机型特例判定，不得外推为通例；Pavel 的“430 毫欧是估算，真值随温度与电池老化而变”为自陈；Reichel 的“TI DSP 目前没有开源工具链”为状态陈述，落书须与当期工具链核对。
**文献**：DSLXC-5004、DSLXC-5006、DSLXC-5011、DSLXC-5012、DSLXC-5013、DSLXC-5015（`ksummit-discuss.messages.348178`、`ksummit-discuss.messages.348180`、`ksummit-discuss.messages.348185`、`ksummit-discuss.messages.348186`、`ksummit-discuss.messages.348187`、`ksummit-discuss.messages.348189`，2017-06-27、2017-06-27、2017-07-02、2017-07-02、2017-07-02、2017-07-02），全文见 `raw_source.raw_json`

## 27.6 【Linux社区】版本号三连与跨树补遗（4 例）

**要点（判定表逐字）**：Daniel Vetter：自己只做过涉及两三个子系统的驱动类跨子系统工作，其法为主题分支置于牵头子系统、他子系统坚持则另发pull请求，drm已将此流程全部脚本化故易行；大规模跨子系统API改动总需跨多个发布周期，若嫌节奏慢可考虑缩短发布周期以便各树更常同步；Darren Hart：无stable ABI则驱动非独立，其版本不难证明无法独立于内核版本或发行版包版本；转而提出版本号本欲解决的问题——确知某实例驱动含何物，分bug修复、性能增强、新特性三类，第一类可经stable流程管，性能回归大补丁与性能增强须脱离内核版本独立追踪，新特性亦然；并问feature mask有无确定机制，眼下多见sysfs键值对；Jiri Kosina：加sysfs属性恰是最易被遗忘之事，因无真实功能依赖它们；怀疑描述驱动状态者无出顶端commit的SHA加其所属之树之右；Darren Hart认同Kosina：此正其对内一贯说法，此处只为确证无遗漏；sysfs属性于具体事项或有用，然如Kosina所言仅供告知

**史料**：`348171`、`348172`、`348193`、`348194`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348171 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348172 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348193 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348194 -->` 

**史观**：法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：无 stable ABI 则驱动非独立，版本号之争实为“确知某实例驱动含何物”的责任边界）；经验优先（总纲第 9 条——经验优先：以 drm 已把跨子系统流程全部脚本化、sysfs 键值对为现状为判据）
**辨析**：Vetter 的“大规模跨子系统 API 改动总需跨多个发布周期，可考虑缩短发布周期”为流程主张；Hart 的“无 stable ABI 则驱动非独立”为结构性判断；Kosina 的“加 sysfs 属性恰是最易被遗忘之事，因无真实功能依赖它们”为观察，Hart 附议并称“仅供告知”。
**文献**：DSLXC-4997、DSLXC-4998、DSLXC-5019、DSLXC-5020（`ksummit-discuss.messages.348171`、`ksummit-discuss.messages.348172`、`ksummit-discuss.messages.348193`、`ksummit-discuss.messages.348194`，2017-06-30、2017-06-30、2017-07-03、2017-07-03），全文见 `raw_source.raw_json`

## 27.7 【Linux社区】文档与 2014 档案五封（6 例）

**要点（判定表逐字）**：Tim Bird：Documentation下文件比源码更常被树外链接引用，elinux.org即有大量直指git树的引用，SubmittingPatches是其例，其内的此文件已移动一行足以把人引到新处，优于符号链接；并赞Iwai新旧分离之议——新文档置docs/*尚可短期内移动，旧文档与符号链接占位留Documentation，则ls docs得清爽列表而ls Documentation见遗留杂物；Amit Kucheria（2014档案）：举任务打包、禁超频强制深睡与强制浅睡等五项运行时可调技术为例，说明它们混杂性能与功耗目标、彼此冲突却非对立，无法归入max performance／balanced／powersave三档；主张这些技术屈指可数应直接暴露给系统，由中间件与各子系统按现状切换；并假定cpufreq与cpuidle终将并入调度器核心；Amit Kucheria（2014档案）：就Preeti U Murthy所提高层profile分类再申反对——手头优化技术无法整齐装入balanced／performance／powersave三筐，且其数无几，主张直接暴露；Teodora Băluță（2014档案）：就QR编码oops提案陈三点异议——base64增约三成开销而QR容量本就有限（故先做压缩）、在已出问题的内核里再添base64编码、仍需带摄像头的设备扫描framebuffer即等于要app，质疑内核内做URL校验的意义；并指能扫framebuffer者本就不多，oops多落在console或dmesg，目标人群本就是geek；Josh Triplett（2014档案）：base64置于每字符八位的二进制QR确属浪费，改用base32配alphanumeric模式（每字符五点五位）则几乎不浪费，或更省而不便的base40；多数用户本就装有QR扫描app且必支持打开URL；另一可能是借HTML Media Capture API加少量Javascript在网页内直接调摄像头取oops图像，从而免app；Arnd Bergmann（2014档案）：Open Firmware本有多种自固件执行代码之法（client calls、RTAS、FCODE）且常用，而嵌入式的FDT子集是刻意不允许；ACPI于嵌入式亦当同理可行，SFI似曾试图为此却不知何故被弃

**史料**：`348181`、`348157`、`348168`、`348179`、`348190`、`348201`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348181 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348157 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348168 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348179 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348190 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348201 -->` 

**史观**：知识注定过时（总纲第 22 条——知识注定过时：新文档置 docs/*、旧文档与符号链接占位留 Documentation 的迁移之议，正是知识载体重构）；经验优先（总纲第 9 条——经验优先：以 elinux.org 大量直指 git 树的引用、QR 容量有限而 base64 增约三成开销等实数为判据）
**辨析**：Bird 的“其内的此文件已移动一行足以把人引到新处，优于符号链接”为文档治理主张；Băluță 的三点异议与 Triplett 的 base32 替代构成同题两说；Bergmann 的“FDT 子集是刻意不允许而 ACPI 于嵌入式同理可行”为规范解释。
**文献**：DSLXC-5007、DSLXC-4983、DSLXC-4994、DSLXC-5005、DSLXC-5016、DSLXC-5027（`ksummit-discuss.messages.348181`、`ksummit-discuss.messages.348157`、`ksummit-discuss.messages.348168`、`ksummit-discuss.messages.348179`、`ksummit-discuss.messages.348190`、`ksummit-discuss.messages.348201`，2017-06-27、2014-05-13、2014-05-13、2014-05-13、2014-05-13、2014-05-13），全文见 `raw_source.raw_json`

---
注：本文件由判定表程序化生成（27.1-27.7 共 7 块，覆盖 50/50 CAND，两遍计数核对通过）；要点逐字取自判定表“要点”列（主代理全读审读实录），史料锚与 CAND 一一对应，全文以 raw_source.raw_json 为准。
