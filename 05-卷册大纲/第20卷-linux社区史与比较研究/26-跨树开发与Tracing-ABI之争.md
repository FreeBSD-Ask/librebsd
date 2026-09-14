# 26 【Linux社区】跨树开发与Tracing-ABI之争

> 对应页面：ksummit-discuss p78（pk 348106-348155，2017-06-28/30 多线程并进 + 2014 档案信）
> 判定：50 CAND / 0 NV
> 编号：DSLXC-4932..4981 | claim 已入库（50/50，dslinux_claims.duckdb）

## 26.1 【Linux社区】Kconfig 余波：设备清单与媒体深水区（11 例）

**要点（判定表逐字）**：Serge E. Hallyn提议改用lspci与lsusb输出作设备清单来源以生成所需Kconfig符号；mcgrof披露Moraru GSoC本就评估过lspci与lsusb方案，因各库总线不同驱动映射各异而退求模块到kconfig符号一对一映射，顺带欲去hack化streamline_config.pl并留符号改名映射备回移；Linus认可本地回退，并主张热插拔设备应看历史udev事件日志而非仅当前插着什么；Linus指出localmodconfig今日已做模块映射；设备实为容易案例，真正最恶劣的是不启用驱动而只改行为的配置项；mcgrof认同元配置层可补localmodconfig的这一缺口；Stephen Hemminger举USB FAT优盘为例：从未插过则模块不载即不被纳入，属热插拔硬件通病；Dan Carpenter裁定depends与select各有其义：select藏用户不关心的基础设施、depend藏用户不能有的特性；Matthew Wilcox以parisc预编内核经验佐证网络选项同为难答之痛；Geert：DT系统易找驱动但子系统前置链难（媒体子系统尤甚）；忆Debian升级拉入systemd时翻Kconfig使系统重新可启动之苦；Mauro媒体子系统Kconfig深水区长文：同USB ID不同I2C芯片、同牌子不同洲不同解调器、select非递归故以逆波兰式转depends、问法从技术API改为用户功能、Autoselect ancillary drivers保开箱即用、展望按品牌菜单加SAT求解器与DT依赖转Kconfig脚本；Mauro提Kconfig开头加提示性问题（本机则查/proc/cpuinfo取默认；用途与发行版菜单加载预设），设想Kconfig方言在符号变更时跑脚本再重启

**史料**：`348106`、`348107`、`348108`、`348109`、`348110`、`348111`、`348116`、`348119`、`348128`、`348137`、`348138`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348106 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348107 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348108 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348109 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348110 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348111 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348116 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348119 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348128 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348137 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348138 -->` 

**史观**：知识注定过时（总纲第 22 条——知识注定过时：ISDN/ATM/PCCARD 已死不该再问，Kconfig 仍问无人能答的疯问题）；经验优先（总纲第 9 条——经验优先：以 lspci/lsusb 输出、udev 历史事件日志、/proc/cpuinfo 取默认等实测来源为判据）
**辨析**：Linus 的“我恨我们的 Kconfig”与“设备实为容易案例，真正最恶劣的是不启用驱动而只改行为的配置项”为顶层判词；Carpenter 的“select 藏用户不关心的基础设施、depend 藏用户不能有的特性”为语义定则；Mauro 的“SAT 求解器与 DT 依赖转 Kconfig 脚本”属展望，本页未见落地记录。
**文献**：DSLXC-4932、DSLXC-4933、DSLXC-4934、DSLXC-4935、DSLXC-4936、DSLXC-4937、DSLXC-4942、DSLXC-4945、DSLXC-4954、DSLXC-4963、DSLXC-4964（`ksummit-discuss.messages.348106`、`ksummit-discuss.messages.348107`、`ksummit-discuss.messages.348108`、`ksummit-discuss.messages.348109`、`ksummit-discuss.messages.348110`、`ksummit-discuss.messages.348111`、`ksummit-discuss.messages.348116`、`ksummit-discuss.messages.348119`、`ksummit-discuss.messages.348128`、`ksummit-discuss.messages.348137`、`ksummit-discuss.messages.348138`，2017-06-27、2017-06-28、2017-06-28、2017-06-28、2017-06-28、2017-06-28、2017-06-28、2017-06-28、2017-06-28、2017-06-29、2017-06-29），全文见 `raw_source.raw_json`

## 26.2 【Linux社区】Bug reporting feedback loop 收束（5 例）

**要点（判定表逐字）**：Takashi Iwai提议为KOTD与linux-next上更多CI（openQA或简化版），与QA谈过尚未落地；Daniel Vetter介绍drm-tip整合树：无单一维护者、冲突由推补丁者存rerere-cache解决、已扩至二十余人共笔，ubuntu有PPA；Mark Brown论-next失败率：关键是结果有人坐镇、个体失败寿命不长，到Linus树时主线编译启动失败率好得多；Jani Nikula提议至少用MAINTAINERS B:标签记录各子系统的上报渠道偏好；Takashi Iwai附议：眼下B:条目太少

**史料**：`348113`、`348114`、`348115`、`348117`、`348118`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348113 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348114 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348115 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348117 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348118 -->` 

**史观**：经验优先（总纲第 9 条——经验优先：以 linux-next 失败率与 drm-tip 整合树、ubuntu PPA 等运行实例为判据）；动手者创造历史（总纲第 10 条——动手者创造历史：以无单一维护者、二十余人共笔的 drm-tip 树为分析单位）
**辨析**：Brown 的“关键是结果有人坐镇、个体失败寿命不长”为维护者经验判词，非量化结论；Nikula 的“至少用 MAINTAINERS B:标签记录各子系统上报渠道偏好”为提案，Iwai 附议“眼下 B:条目太少”，本页未见定论。
**文献**：DSLXC-4939、DSLXC-4940、DSLXC-4941、DSLXC-4943、DSLXC-4944（`ksummit-discuss.messages.348113`、`ksummit-discuss.messages.348114`、`ksummit-discuss.messages.348115`、`ksummit-discuss.messages.348117`、`ksummit-discuss.messages.348118`，2017-06-28、2017-06-28、2017-06-28、2017-06-28、2017-06-28），全文见 `raw_source.raw_json`

## 26.3 【Linux社区】跨树开发机制十连（10 例）

**要点（判定表逐字）**：Kees Cook跨树开发议题全文：hardened usercopy自持树加逐个Ack、refcount_t逐维护者转换跨发布低效、randstruct树依赖地狱（gcc插件树须最后合、ACPICA树外先改）、fortify被提前拾入-mm致数日混乱、-mm隐式最后合并依赖、多阶段合并伤0-day与sfr；Christoph Hellwig：跨树事找牵头子系统、无则自创（uuid与dma-mapping即新例）；ACPICA树外先改该停——每个子系统必须接受公开邮件列表上的合格补丁，ACPICA按常规则可减码五成；James Bottomley：refcount_t节奏教科书级正确，若一次全树并入而性能崩了到处回滚代价更大；Kees反驳效率论：API与转换波次错开纯因树依赖，btrfs无法以tip树上的API编译只好等发布——原本可API一与波一同入4.11、API二与波二同入4.12；Bottomley立规则：API入R-1、转换经各受影响树入R，唯足够琐碎者例外；经维护者树得评审方显性能顾虑；Kees：这正是-next的用途，可惜没有体面的基于-next开树之法；自嘲去喝闷酒；mcgrof：API可先以测试驱动为首用户免成裸API；忆Linus言跨树协同演化可交脚本执行；提linux-oven构想——每日基于linux-next重置、自动跑API转换工具集；Linus论跨树：脚本化清扫照收（极而言之直接把脚本发我）；但视为末选——稳定回移痛苦、跨树往往庞大侵入；偏好经tip或akpm；真问题是跨树更新全然无维护者认领而烂尾；Kees fortify历险记：修复被各维护者提前拾走致树无法入-next（sfr见重复提交）、akpm拾入-mm却漏了未收修复、两树皆编不过；解法是akpm补拾余量；自问是否该声明自持并请Ack（randstruct尾件即由hch劝其请Linus收）；sfr定机制：共享commit无碍、共享异commit同补丁碍事；新API置不可变树或分支供各树合并，合并者登记在册以便后续变更知会

**史料**：`348136`、`348139`、`348140`、`348141`、`348142`、`348143`、`348144`、`348147`、`348148`、`348149`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348136 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348139 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348140 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348141 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348142 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348143 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348144 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348147 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348148 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348149 -->` 

**史观**：分离聚合是永恒规律（总纲第 4 条——分离聚合是永恒规律：API 入 R-1、转换经各受影响树入 R 的波次错开，正是树间分合的相位）；动手者创造历史（总纲第 10 条——动手者创造历史：以 linux-oven 每日基于 linux-next 重置并自动跑 API 转换工具集的构想为分析单位）
**辨析**：Bottomley 的“API 入 R-1、转换经各受影响树入 R”为跨树协同定则，唯“足够琐碎者例外”；Cook 的 fortify 历险记为当事人自陈，涉 akpm 拾取与漏收，落书须与当期 -mm 树核对；Hellwig 的“每个子系统必须接受公开邮件列表上的合格补丁”为立场主张。
**文献**：DSLXC-4962、DSLXC-4965、DSLXC-4966、DSLXC-4967、DSLXC-4968、DSLXC-4969、DSLXC-4970、DSLXC-4973、DSLXC-4974、DSLXC-4975（`ksummit-discuss.messages.348136`、`ksummit-discuss.messages.348139`、`ksummit-discuss.messages.348140`、`ksummit-discuss.messages.348141`、`ksummit-discuss.messages.348142`、`ksummit-discuss.messages.348143`、`ksummit-discuss.messages.348144`、`ksummit-discuss.messages.348147`、`ksummit-discuss.messages.348148`、`ksummit-discuss.messages.348149`，2017-06-28、2017-06-29、2017-06-29、2017-06-29、2017-06-29、2017-06-29、2017-06-29、2017-06-29、2017-06-29、2017-06-29），全文见 `raw_source.raw_json`

## 26.4 【Linux社区】Tracing ABI 流沙与 Linus 零填裁决（6 例）

**要点（判定表逐字）**：Mathieu Desnoyers提tracing ABI流沙议题：扩展调度tracepoint至rt与deadline遇DebugFS ABI之墙；两问——ABI该为人手echo设计还是为脚本与库设计、事件字段（如内部细节prio）如何废弃移除或改用途；Rostedt：不能破坏sched_switch的既有用户trace-cmd与perf及powertop；先修工具送进发行版再动字段；聚焦扩展与叠加overlay（一处钩子多种展示）；Linus全大写裁定：把那该死的字段留着填零——零、一、随便填什么，别删、别拿它当无所作为的借口；此话已在至少三届峰会说过，再讨论就退场；Rostedt陈旧案与真议题：曾修powertop等进Debian stable数年后删字段无人察觉（每tracepoint省4字节乘400万即省4MB）；本次不同——sched_switch遇SCHED_DEADLINE致prio无用而欲加remaining runtime与next deadline及next period，但不想为小众类让所有事件膨胀；设想overlay一址多tracepoint按需展开；附sched_switch完整format转储；Linus终裁：内部细节不存在了就填零；也别加更专门的新字段；别再纠结此事；Rostedt揭内情：PeterZ反对给sched_switch设多tracepoint（偏好动态单点，惯用echo与cat手动操ftrace）；真正想要的是动态tracepoint按调度进出情形变化记录内容，且不破坏既有工具

**史料**：`348150`、`348151`、`348152`、`348153`、`348154`、`348155`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348150 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348151 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348152 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348153 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348154 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348155 -->` 

**史观**：知识注定过时（总纲第 22 条——知识注定过时：SCHED_DEADLINE 使 prio 无用而欲加 remaining runtime 等字段，旧字段面临废弃）；多方平等（总纲第 8 条——本体论上各方平等：Linus 的“填零”终裁与 PeterZ 偏好动态单点、Rostedt 欲保既有工具三方并置）
**辨析**：Linus 的“把那该死的字段留着填零”“内部细节不存在了就填零”为 ABI 硬裁定，属顶层判词；Rostedt 的“每 tracepoint 省 4 字节乘 400 万即省 4MB”为量级估算，非实测；PeterZ 反对设多 tracepoint 之内情系 Rostedt 转述。
**文献**：DSLXC-4976、DSLXC-4977、DSLXC-4978、DSLXC-4979、DSLXC-4980、DSLXC-4981（`ksummit-discuss.messages.348150`、`ksummit-discuss.messages.348151`、`ksummit-discuss.messages.348152`、`ksummit-discuss.messages.348153`、`ksummit-discuss.messages.348154`、`ksummit-discuss.messages.348155`，2017-06-29、2017-06-29、2017-06-30、2017-06-30、2017-06-30、2017-06-30），全文见 `raw_source.raw_json`

## 26.5 【Linux社区】mobile：GPU 版图与 Qualcomm 旧板（12 例）

**要点（判定表逐字）**：Linus Walleij长文：Qualcomm原版DragonBoard五年即被视作古董、安卓业当学苹果以最新OS配旧机、上游驱动加内核ABI作HAL是正途、GPU供应商僵局寄望Freedreno与etnaviv、Intel IIO HAL安卓版无人拾取、电池框架软件充电无人维护、runtime PM在I2C/SPI外设已可用（bh1780例）、愿为N900上AOSP接受树外GPU驱动；Arnd Bergmann绘GPU版图：Nvidia/Vivante/Broadcom已有开源驱动却已退出手机、PowerVR式微、ARM Mali是高通之外唯一要紧的手机GPU，出路唯ARM换帅或有人逆向Midgard与Bifrost，且须有资格有能力且不受NDA约束者；Sebastian Reichel指N900 DSP可走OMAP_REMOTEPROC框架（多媒体卸载），引Nokia人言DSP算力有限CPU亦可代劳；droid4蓝牙补丁已在-next；Laurent Pinchart提Mali逆向撮合方案：一边找有资格不受NDA的开发者、一边找愿出资者，牵线合流；Pavel断言问题名叫Qualcomm，TI等才在意主线（自用2009年TI硬件）；Android已有ABI抽象层Jolla等chroot用之但非正途，Google不会帮、社区须先行；N900跑Debian唯音质太差；Reichel补NoLo充电哲学与droid4三GPS实现（WL1285/MDM6600/LTE，美规modem须具GPS，Motorola为WL1285专写驱动而用户态闭源）；审Pavel补丁质疑430毫欧内阻与open circuit voltage命名；Pavel向Walleij推荐droid4：尚有LineageOS支持、主线硬件支持颇完整，比N900与N950容易；Brown纠正：非独Qualcomm，常规市场外嵌入式与垂直领域才在意长寿命；Android ABI层并不算稳定ABI；Pavel认错2010年说（实为2015），自陈曾试转ALSA未成；现优先通话音质，欲知Pyra手持机如何处理；Tony Lindgren定调：自己动手做出可用之物，等企业方案已证是浪费光阴；Pavel论DSP支持链复杂度：remoteproc无用户态接口、需交叉编译器、须拆mpg123跨CPU与DSP，改动遍布系统；Pavel自认电池老化（一块差到GSM失败）、主张内核默认充电以支撑fsck；确认430毫欧、允诺改open circuit voltage；戏言三GPS可做公平横评并讥Motorola闭源

**史料**：`348120`、`348121`、`348122`、`348124`、`348125`、`348126`、`348127`、`348129`、`348130`、`348131`、`348133`、`348135`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348120 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348121 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348122 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348124 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348125 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348126 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348127 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348129 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348130 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348131 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348133 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348135 -->` 

**史观**：历史地理塑造思想土壤（总纲第 20 条——历史地理塑造思想土壤：中心与边缘之别使常规市场外的嵌入式与垂直领域才在意长寿命主线支持）；经验优先（总纲第 9 条——经验优先：以 N900 续航一天、430 毫欧内阻、droid4 三 GPS 实现等实测与实例为判据）
**辨析**：Pavel 自陈“认错 2010 年说（实为 2015）”属当事人史实订正；Bergmann 的 GPU 版图判断（Mali 是高通之外唯一要紧的手机 GPU）为行业观察，非厂商声明；Reichel 的 droid4 蓝牙补丁“已在 -next”为状态记录，落书须与当期树核对。
**文献**：DSLXC-4946、DSLXC-4947、DSLXC-4948、DSLXC-4950、DSLXC-4951、DSLXC-4952、DSLXC-4953、DSLXC-4955、DSLXC-4956、DSLXC-4957、DSLXC-4959、DSLXC-4961（`ksummit-discuss.messages.348120`、`ksummit-discuss.messages.348121`、`ksummit-discuss.messages.348122`、`ksummit-discuss.messages.348124`、`ksummit-discuss.messages.348125`、`ksummit-discuss.messages.348126`、`ksummit-discuss.messages.348127`、`ksummit-discuss.messages.348129`、`ksummit-discuss.messages.348130`、`ksummit-discuss.messages.348131`、`ksummit-discuss.messages.348133`、`ksummit-discuss.messages.348135`，2017-06-28、2017-06-28、2017-06-28、2017-06-28、2017-06-28、2017-06-28、2017-06-28、2017-06-28、2017-06-28、2017-06-28、2017-06-28、2017-06-28），全文见 `raw_source.raw_json`

## 26.6 【Linux社区】性能回归与 KS2014 档案（6 例）

**要点（判定表逐字）**：Greg KH档案信：新人清扫多在staging；其追踪唯一贡献者数八年持续上升，数据与脚本公开于github.com/gregkh/kernel-history；新人当与众人同礼；Josh Triplett（2014档案）：问Mason基准自动化程度与运行一致性，提议纳入Fengguang Wu自动补丁检查器，逐补丁反馈x%减速比版本间对照更可行动；Geert答Corbet：文档特殊在外链多、凡人读者多，此点多限于SubmittingPatches与CodingStyle（恰为顶层仅有的CamelCase两文件）；Davidlohr Bueso（2014档案）：Fengguang脚本覆盖不了专有工具（Oracle与Hadoop）与非x86架构微变，aim7亦可绕过自动检查，建议增perf-bench负载；Bottomley档案信：正与发行版商议重构Linux安全启动，细节系UEFI论坛保密提案（可向Peter Jones了解），若成将把Linux安全启动策略与微软二进制签名要求解耦；Chris Mason（2014档案）：Intel听进了且影响巨大；但生产负载升级仍几乎必撞大回归，有时仅几个config有时靠别处改进掩盖；只能承诺提炼新基准常跑

**史料**：`348112`、`348123`、`348132`、`348134`、`348145`、`348146`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348112 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348123 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348132 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348134 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348145 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348146 -->` 

**史观**：动手者创造历史（总纲第 10 条——动手者创造历史：以追踪唯一贡献者数八年持续上升的数据与公开脚本为分析单位）；苦难不值得被提倡（总纲第 14 条——苦难不值得被提倡：新人当与众人同礼，不将无偿贡献美化为道德勋章）
**辨析**：Greg KH 的“新人清扫多在 staging”“新人当与众人同礼”为维护者指导；Triplett 的“逐补丁反馈 x% 减速比版本间对照更可行动”为方法论提议；Bueso 的“Fengguang 脚本覆盖不了专有工具与非 x86 架构微变”为覆盖面评估，两者并置。
**文献**：DSLXC-4938、DSLXC-4949、DSLXC-4958、DSLXC-4960、DSLXC-4971、DSLXC-4972（`ksummit-discuss.messages.348112`、`ksummit-discuss.messages.348123`、`ksummit-discuss.messages.348132`、`ksummit-discuss.messages.348134`、`ksummit-discuss.messages.348145`、`ksummit-discuss.messages.348146`，2014-05-12、2014-05-12、2017-06-28、2014-05-13、2014-05-02、2014-05-13），全文见 `raw_source.raw_json`

---
注：本文件由判定表程序化生成（26.1-26.6 共 6 块，覆盖 50/50 CAND，两遍计数核对通过）；要点逐字取自判定表“要点”列（主代理全读审读实录），史料锚与 CAND 一一对应，全文以 raw_source.raw_json 为准。
