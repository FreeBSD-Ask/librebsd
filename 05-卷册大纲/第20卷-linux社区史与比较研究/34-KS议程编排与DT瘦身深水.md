# 34-KS议程编排与DT瘦身深水.md

> 对应页面：ksummit-discuss p86（pk 348506-348555，2017-07-10/12 议程编排期 + 2014 档案信）
> 判定：50 CAND / 0 NV
> 编号：DSLXC-5331..5380 | claim 已入库（50/50，dslinux_claims.duckdb）

## 34.1 Devicetree 工作坊日程与 dtb 瘦身深水（13 例）

**要点（判定表逐字）**：Mark Brown指出u-boot存在一份与上游分歧的devicetree binding文档副本，认为DT若要跨项目协作须更妥善；并认同Rob关于推动统一的动议；Grant Likely发布Devicetree Workshop（10-26 Prague）完整日程草案，含YAML编码、DT Schema两类方案、运行时内存占用、overlay维护、ABI稳定性、EBBR等议题与主持人；Rob Herring谈dtb瘦身：XiP为当前重点，Nico曾尝试收缩tty与调度器但遇阻力；介绍devicetree-rebasing.git公共仓库，并说明dtc已停止默认生成phandle与linux,phandle；Frank Rowand以dtx_diff实例说明phandle仅在被引用时生成，唯启用符号（dtc -@）以加载overlay时方为所有带标签节点生成phandle与__symbols__；Rob Herring答Alexandre Torgue：dtc无法移除无phandle引用的节点（无引用不等于未用，／memory即例），须加／delete-if-unused／注解或扩展status，或后处理dtb；Andre Przywara提议内核树停止提供板级dts，仅留SoC dtsi加一两个评估板示例，vendors可将dtb置于flash或固件（如U-Boot）；Andre Przywara续论板级与SoC dtsi之分不应成ABI；提及Android Treble将板级specifics作overlay叠加于公共SoC dtb，并述U-Boot复用同dtb配置自身与内核（如Pine64用$fdtcontroladdr）；Andrew Turner从FreeBSD视角呼吁各devicetree消费方共用仓库，去除FreeBSD专用属性，并与NetBSD／OpenBSD开发者交流，望五项目共用dts与binding以同步；Alexandre Torgue代表STMicro表达对共用DTS（Linux／U-boot／ATF／Zephyr）的需求，关切dtb瘦身与DT文件存放位置，望Prague深入讨论；Alexandre Torgue追问dtc是否有额外选项可剔除无用phandle，指出pinmux phandle尤甚，stm32f4-pinctrl.dtsi全量进入dtb；Alexandre Torgue进一步说明ATF／U-Boot／内核共用DT时框架级phandle与binding差异，愿用外部仓库按组件叠加dts以原型化；David Gibson答Alexandre Torgue：phandle仅在正常模式被引用时生成，唯加-@以载overlay时方为所有标签节点生成，反编译后整数无法回溯为phandle；David Gibson答Rob Herring：愿合并为dtc加剥离disabled节点的选项，亦可用libfdt（fdt_next_node／fdt_del_node）实现

**史料**：`348506、`348508、`348510、`348511、`348521、`348527、`348528、`348529、`348530、`348531、`348532、`348547、`348548

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.348506 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348508 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348510 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348511 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348521 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348527 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348528 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348529 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348530 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348531 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348532 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348547 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348548 -->` 

## 34.2 设备电源管理（PM）议题细化（8 例）

**要点（判定表逐字）**：Ulf Hansson回复Rafael，表态支持将设备电源管理（runtime PM与系统级PM交互）列入KS议程，并称自己同样感兴趣；Rafael向Ted重申设备PM议题：runtime PM与系统级PM交互的三类常见模式，以及清理遗留电源管理回调，并贴出相应补丁集链接；Ted向Rafael确认将电源管理议题加入KS议程；Rafael向Ted确认PM议题已加入议程，致谢；Linus Walleij回应Rafael的PM议题，以I2C／SPI的force*回调实例说明runtime PM复用，指出慢速外设仍会在系统恢复时唤醒，并认为这是固件范式与内核全控之争；Bart Van Assche提议在PM时段加入存储栈有序冻结议题（md RAID1上XFS的内核线程冻结顺序），并引Luis R. Rodriguez的fs freeze／thaw RFC；Rafael回应Linus Walleij：force*回调并非普适，分歧在于中间层是否介入PM及其预期，以及设备能否唤醒系统；Rafael回应Bart：存储栈有序冻结可纳入PM时段讨论，并指Luis R. Rodriguez的kthread freezing替换方案相关

**史料**：`348507、`348516、`348535、`348539、`348541、`348542、`348543、`348544

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.348507 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348516 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348535 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348539 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348541 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348542 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348543 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348544 -->` 

## 34.3 文档、回归追踪与 kselftest 场次编排（11 例）

**要点（判定表逐字）**：Mauro Carvalho Chehab提议在KS技术环节开设文档会话，论驱动文档归类（uAPI／core kAPI／实现／用户向）与Documentation到ReST的统一转换，主张清理旧txt并归入书籍；Jonathan Corbet回应Mauro：媒体几乎是唯一把uAPI置入DocBook的子系统；主张按受众分离文档（UAPI与模块参数不同于内核接口），对以强制力推行ReST存疑；Ted确认将原Media Summit时段改为Mauro主导的文档技术讨论，移除媒体议题；Ted就改进回归追踪议题征询Thorsten Leemhuis是否仍合适及其是否领衔；Ted就Kselftest用例议题征询Shuah Khan是否仍合适及其是否领衔；Thorsten Leemhuis认为回归追踪仍必要，列举列表讨论与历年峰会关注；自陈新人，邀请Rafael同台，亦愿让出领衔；Rafael认为回归追踪应是Thorsten的场次，但愿协助内容；Shuah Khan回复Ted称未见原帖多少回应，不确定议题价值，若需让位他人亦无异议；James Bottomley认为面向树维护者概览可用测试资源很有用，提及linux-next、0day定制测试与邮件失败报告，以及基于kselftest或xfstests的自建CI；Shuah Khan回应James Bottomley，愿讲解kselftest用例及其用于stable发布测试的方式；Ted因Jon Corbet须在OSS主持内核panel，将Kernel Documentation时段移至周二16:55 TBA

**史料**：`348509、`348513、`348515、`348517、`348518、`348519、`348520、`348524、`348525、`348533、`348552

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.348509 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348513 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348515 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348517 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348518 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348519 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348520 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348524 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348525 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348533 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348552 -->` 

## 34.4 rseq／printk 场次插入与直播之争（7 例）

**要点（判定表逐字）**：Mathieu Desnoyers请求为Restartable Sequences在KS加slot，称已解决单步执行难题，并附LKML讨论链接；Steve Rostedt提醒Printk redesign（Petr Mladek与其）场次亦须Sergey参与；Ted回复Joe Perches：技术议题不提供直播，主因是成本；Joe Perches在Printk redesign子线程中询问是否对这些讨论进行直播；Ted确认已为Restartable Sequences安排在周二下午的slot；Mathieu Desnoyers请求将Restartable Sequences移至16:55 slot，因x86开发者周二下午聚首（房间至17:00），以免与rseq关注者冲突；Ted确认调整：16:05 Kernel Documentation（Mauro、Jon Corbet），16:55 Restartable Sequences（Mathieu）

**史料**：`348522、`348526、`348536、`348537、`348538、`348553、`348554

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.348522 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348526 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348536 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348537 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348538 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348553 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348554 -->` 

## 34.5 TAB 选举与议程地点（6 例）

**要点（判定表逐字）**：Ted发布Kernel Summit v2草案议程：含tracing ABI、printk、文档、PM、rseq、回归追踪、kselftest、安全等时段，并列出未定焦点（mobile、Kconfig、maintainer summit技术议题）；Chris Mason发布TAB选举提醒v2：已有六名提名（Corbet、Greg KH、Shuah、Rostedt、Tso、Bird），并介绍TAB职责与10-25选举安排；Frank Rowand向Chris Mason询问TAB现任成员及哪些任期届满；Greg KH回复Frank Rowand：TAB现任成员见linuxfoundation.org专页；Mark Brown询问v2议程中各场次的物理地点，称官网未见KS或OSS Europe信息；Chris Mason回复Frank Rowand：Greg已给TAB链接，列出届满任期者（Corbet、Greg KH、Shuah、Rostedt、Tso）

**史料**：`348540、`348546、`348549、`348550、`348551、`348555

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.348540 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348546 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348549 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348550 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348551 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348555 -->` 

## 34.6 开发者工作站安全与 2014 档案四封（5 例）

**要点（判定表逐字）**：Ted确认采纳Konstantin Ryabitsev关于开发者工作站安全卫生的四十分钟时段，内容含PGP／ssh密钥实践、Git与PGP签名、firefox加firejail、Wayland安全收益；Ted（2014档案）论bug报告：主张需要专人改进kerneloops.org、挖掘规律并自动化转发开发者，质疑是否值得单设技术议题，警惕沦为无果空谈；Josh Triplett（2014档案）论跨子系统维护工作流：以tiny树按topic而非子系统收补丁，并提议kernel.org提供类似Andrew与Greg的git钩子自动通知提交者合入；Tim Bird（2014档案）回应Josh的tinification议题，主张以自动化缩减内核（如DT静态化以常量传播与死代码消除），并荐linux-embedded列表与elinux wiki；Olof Johansson（2014档案）回应Josh：arm-soc以topic分支作基底并早抓冲突，认可按topic而非子系统维护树，但要求知情且经评审、非绕开异议维护者

**史料**：`348514、`348512、`348523、`348534、`348545

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.348514 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348512 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348523 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348534 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348545 -->` 

---
注：本文件由判定表程序化生成（6 块，覆盖 50/50 CAND，两遍计数核对通过）；要点逐字取自判定表「要点」列（主代理全读审读实录），史料锚与 CAND 一一对应，全文以 raw_source.raw_json 为准。
