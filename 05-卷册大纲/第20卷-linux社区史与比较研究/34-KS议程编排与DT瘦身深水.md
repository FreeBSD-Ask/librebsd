# 34 【Linux社区】KS议程编排与DT瘦身深水

> 对应页面：ksummit-discuss p86（pk 348506-348555，2017-07-10/12 议程编排期 + 2014 档案信）
> 判定：50 CAND / 0 NV
> 编号：DSLXC-5331..5380 | claim 已入库（50/50，dslinux_claims.duckdb）

## 34.1 【Linux社区】Devicetree 工作坊日程与 dtb 瘦身深水（13 例）

**要点（判定表逐字）**：Mark Brown 指出 U-Boot 存在一份与上游分歧的 devicetree binding 文档副本，认为 DT 若要跨项目协作须更妥善；并认同 Rob 关于推动统一的动议；Grant Likely 发布 Devicetree Workshop（10-26 Prague）完整日程草案，含 YAML 编码、DT Schema 两类方案、运行时内存占用、overlay 维护、ABI 稳定性、EBBR 等议题与主持人；Rob Herring 谈 dtb 瘦身：XiP 为当前重点，Nico 曾尝试收缩 tty 与调度器但遇阻力；介绍 devicetree-rebasing.git 公共仓库，并说明 dtc 已停止默认生成 phandle 与 linux,phandle；Frank Rowand 以 dtx_diff 实例说明 phandle 仅在被引用时生成，唯启用符号（dtc -@）以加载 overlay 时方为所有带标签节点生成 phandle 与__symbols__；Rob Herring 答 Alexandre Torgue：dtc 无法移除无 phandle 引用的节点（无引用不等于未用，`/memory` 即例），须加 `/delete-if-unused/` 注解或扩展 status，或后处理 dtb；Andre Przywara 提议内核树停止提供板级 dts，仅留 SoC dtsi 加一两个评估板示例，vendors 可将 dtb 置于 flash 或固件（如 U-Boot）；Andre Przywara 续论板级与 SoC dtsi 之分不应成 ABI；提及 Android Treble 将板级 specifics 作 overlay 叠加于公共 SoC dtb，并述 U-Boot 复用同 dtb 配置自身与内核（如 Pine64 用$fdtcontroladdr）；Andrew Turner 从 FreeBSD 视角呼吁各 devicetree 消费方共用仓库，去除 FreeBSD 专用属性，并与 NetBSD／OpenBSD 开发者交流，望五项目共用 dts 与 binding 以同步；Alexandre Torgue 代表 STMicro 表达对共用 DTS（Linux／U-Boot／ATF／Zephyr）的需求，关切 dtb 瘦身与 DT 文件存放位置，望 Prague 深入讨论；Alexandre Torgue 追问 dtc 是否有额外选项可剔除无用 phandle，指出 pinmux phandle 尤甚，stm32f4-pinctrl.dtsi 全量进入 dtb；Alexandre Torgue 进一步说明 ATF／U-Boot／内核共用 DT 时框架级 phandle 与 binding 差异，愿用外部仓库按组件叠加 dts 以原型化；David Gibson 答 Alexandre Torgue：phandle 仅在正常模式被引用时生成，唯加-@以载 overlay 时方为所有标签节点生成，反编译后整数无法回溯为 phandle；David Gibson 答 Rob Herring：愿合并为 dtc 加剥离 disabled 节点的选项，亦可用 libfdt（fdt_next_node／fdt_del_node）实现

**史料**：`348506`、`348508`、`348510`、`348511`、`348521`、`348527`、`348528`、`348529`、`348530`、`348531`、`348532`、`348547`、`348548`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348506 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348508 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348510 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348511 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348521 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348527 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348528 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348529 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348530 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348531 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348532 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348547 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348548 -->` 

**史观**：分离聚合是永恒规律（总纲第 4 条——分离聚合是永恒规律：devicetree-rebasing.git 公共仓库与各消费方（Linux、U-Boot、ATF、Zephyr、FreeBSD、NetBSD、OpenBSD）共用 dts 与 binding，正是分合相位）；经验优先（总纲第 9 条——经验优先：以 phandle 仅在被引用时生成、唯加 -@ 载 overlay 时方为所有带标签节点生成等实测机制为判据）
**辨析**：Gibson 的“反编译后整数无法回溯为 phandle”为机制界定；Przywara 的“内核树停止提供板级 dts，仅留 SoC dtsi 加一两个评估板示例”为方案主张，与 Torgue 的“望 Prague 深入讨论”同属未决；Rowand 的“无引用不等于未用，/memory 即例”为反例，纠正 dtc 移除之可行性。
**文献**：DSLXC-5331、DSLXC-5333、DSLXC-5335、DSLXC-5336、DSLXC-5346、DSLXC-5352、DSLXC-5353、DSLXC-5354、DSLXC-5355、DSLXC-5356、DSLXC-5357、DSLXC-5372、DSLXC-5373（`ksummit-discuss.messages.348506`、`ksummit-discuss.messages.348508`、`ksummit-discuss.messages.348510`、`ksummit-discuss.messages.348511`、`ksummit-discuss.messages.348521`、`ksummit-discuss.messages.348527`、`ksummit-discuss.messages.348528`、`ksummit-discuss.messages.348529`、`ksummit-discuss.messages.348530`、`ksummit-discuss.messages.348531`、`ksummit-discuss.messages.348532`、`ksummit-discuss.messages.348547`、`ksummit-discuss.messages.348548`，2017-10-19、2017-10-19、2017-10-19、2017-10-19、2017-10-20、2017-10-18、2017-10-18、2017-10-18、2017-10-19、2017-10-20、2017-10-20、2017-10-20、2017-10-22），全文见 `raw_source.raw_json`

## 34.2 【Linux社区】设备电源管理（PM）议题细化（8 例）

**要点（判定表逐字）**：Ulf Hansson 回复 Rafael，表态支持将设备电源管理（runtime PM 与系统级 PM 交互）列入 KS 议程，并称自己同样感兴趣；Rafael 向 Ted 重申设备 PM 议题：runtime PM 与系统级 PM 交互的三类常见模式，以及清理遗留电源管理回调，并贴出相应补丁集链接；Ted 向 Rafael 确认将电源管理议题加入 KS 议程；Rafael 向 Ted 确认 PM 议题已加入议程，致谢；Linus Walleij 回应 Rafael 的 PM 议题，以 I2C／SPI 的 force*回调实例说明 runtime PM 复用，指出慢速外设仍会在系统恢复时唤醒，并认为这是固件范式与内核全控之争；Bart Van Assche 提议在 PM 时段加入存储栈有序冻结议题（md RAID1 上 XFS 的内核线程冻结顺序），并引 Luis R. Rodriguez 的 fs freeze／thaw RFC；Rafael 回应 Linus Walleij：force*回调并非普适，分歧在于中间层是否介入 PM 及其预期，以及设备能否唤醒系统；Rafael 回应 Bart：存储栈有序冻结可纳入 PM 时段讨论，并指 Luis R. Rodriguez 的 kthread freezing 替换方案相关

**史料**：`348507`、`348516`、`348535`、`348539`、`348541`、`348542`、`348543`、`348544`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348507 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348516 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348535 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348539 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348541 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348542 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348543 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348544 -->` 

**史观**：分离聚合是永恒规律（总纲第 4 条——分离聚合是永恒规律：runtime PM 与系统级 PM 的交互、中间层是否介入 PM，见固件范式与内核全控之争）；经验优先（总纲第 9 条——经验优先：以 I2C／SPI 的 force* 回调实例、慢速外设仍会在系统恢复时唤醒等机制为判据）
**辨析**：Walleij 的“这是固件范式与内核全控之争”为定性；Wysocki 的“force* 回调并非普适，分歧在于中间层是否介入 PM 及其预期”为其回应，两说并置；Assche 的“存储栈有序冻结（md RAID1 上 XFS 的内核线程冻结顺序）”为新增议题，Wysocki 认可纳入。
**文献**：DSLXC-5332、DSLXC-5341、DSLXC-5360、DSLXC-5364、DSLXC-5366、DSLXC-5367、DSLXC-5368、DSLXC-5369（`ksummit-discuss.messages.348507`、`ksummit-discuss.messages.348516`、`ksummit-discuss.messages.348535`、`ksummit-discuss.messages.348539`、`ksummit-discuss.messages.348541`、`ksummit-discuss.messages.348542`、`ksummit-discuss.messages.348543`、`ksummit-discuss.messages.348544`，2017-10-19、2017-10-20、2017-10-20、2017-10-21、2017-10-21、2017-10-21、2017-10-21、2017-10-21），全文见 `raw_source.raw_json`

## 34.3 【Linux社区】文档、回归追踪与 kselftest 场次编排（11 例）

**要点（判定表逐字）**：Mauro Carvalho Chehab 提议在 KS 技术环节开设文档会话，论驱动文档归类（uAPI／core kAPI／实现／用户向）与 Documentation 到 ReST 的统一转换，主张清理旧 txt 并归入书籍；Jonathan Corbet 回应 Mauro：媒体几乎是唯一把 uAPI 置入 DocBook 的子系统；主张按受众分离文档（UAPI 与模块参数不同于内核接口），对以强制力推行 ReST 存疑；Ted 确认将原 Media Summit 时段改为 Mauro 主导的文档技术讨论，移除媒体议题；Ted 就改进回归追踪议题征询 Thorsten Leemhuis 是否仍合适及其是否领衔；Ted 就 Kselftest 用例议题征询 Shuah Khan 是否仍合适及其是否领衔；Thorsten Leemhuis 认为回归追踪仍必要，列举列表讨论与历年峰会关注；自陈新人，邀请 Rafael 同台，亦愿让出领衔；Rafael 认为回归追踪应是 Thorsten 的场次，但愿协助内容；Shuah Khan 回复 Ted 称未见原帖多少回应，不确定议题价值，若需让位他人亦无异议；James Bottomley 认为面向树维护者概览可用测试资源很有用，提及 linux-next、0day 定制测试与邮件失败报告，以及基于 kselftest 或 xfstests 的自建 CI；Shuah Khan 回应 James Bottomley，愿讲解 kselftest 用例及其用于 stable 发布测试的方式；Ted 因 Jon Corbet 须在 OSS 主持内核 panel，将 Kernel Documentation 时段移至周二 16:55 TBA

**史料**：`348509`、`348513`、`348515`、`348517`、`348518`、`348519`、`348520`、`348524`、`348525`、`348533`、`348552`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348509 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348513 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348515 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348517 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348518 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348519 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348520 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348524 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348525 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348533 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348552 -->` 

**史观**：动手者创造历史（总纲第 10 条——动手者创造历史：以 Mauro 提议开文档会话并清理旧 txt 归入书籍、Bottomley 提议用测试资源概览为分析单位）；本体论上各方平等（总纲第 8 条——本体论上各方平等：Leemhuis 的“自陈新人，邀请 Rafael 同台，亦愿让出领衔”与 Khan 的“不确定议题价值，若需让位他人亦无异议”并置）
**辨析**：Corbet 的“主张按受众分离文档，对以强制力推行 ReST 存疑”为方法主张；Leemhuis 的“认为回归追踪仍必要”与 Khan 的“未见原帖多少回应，不确定议题价值”构成两说；Bottomley 的“提及 linux-next、0day 定制测试与邮件失败报告，以及基于 kselftest 或 xfstests 的自建 CI”为资源清单。
**文献**：DSLXC-5334、DSLXC-5338、DSLXC-5340、DSLXC-5342、DSLXC-5343、DSLXC-5344、DSLXC-5345、DSLXC-5349、DSLXC-5350、DSLXC-5358、DSLXC-5377（`ksummit-discuss.messages.348509`、`ksummit-discuss.messages.348513`、`ksummit-discuss.messages.348515`、`ksummit-discuss.messages.348517`、`ksummit-discuss.messages.348518`、`ksummit-discuss.messages.348519`、`ksummit-discuss.messages.348520`、`ksummit-discuss.messages.348524`、`ksummit-discuss.messages.348525`、`ksummit-discuss.messages.348533`、`ksummit-discuss.messages.348552`，2017-10-19、2017-10-19、2017-10-20、2017-10-20、2017-10-20、2017-10-20、2017-10-20、2017-10-20、2017-10-20、2017-10-20、2017-10-23），全文见 `raw_source.raw_json`

## 34.4 【Linux社区】rseq／printk 场次插入与直播之争（7 例）

**要点（判定表逐字）**：Mathieu Desnoyers 请求为 Restartable Sequences 在 KS 加 slot，称已解决单步执行难题，并附 LKML 讨论链接；Steve Rostedt 提醒 Printk redesign（Petr Mladek 与其）场次亦须 Sergey 参与；Ted 回复 Joe Perches：技术议题不提供直播，主因是成本；Joe Perches 在 Printk redesign 子线程中询问是否对这些讨论进行直播；Ted 确认已为 Restartable Sequences 安排在周二下午的 slot；Mathieu Desnoyers 请求将 Restartable Sequences 移至 16:55 slot，因 x86 开发者周二下午聚首（房间至 17:00），以免与 rseq 关注者冲突；Ted 确认调整：16:05 Kernel Documentation（Mauro、Jon Corbet），16:55 Restartable Sequences（Mathieu）

**史料**：`348522`、`348526`、`348536`、`348537`、`348538`、`348553`、`348554`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348522 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348526 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348536 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348537 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348538 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348553 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348554 -->` 

**史观**：动手者创造历史（总纲第 10 条——动手者创造历史：以 Desnoyers 为 Restartable Sequences 争取 slot 并因 x86 开发者周二下午聚首而请移至 16:55 为分析单位）；经验优先（总纲第 9 条——经验优先：以技术议题不提供直播主因是成本、房间至 17:00 等实况为判据）
**辨析**：Ted 的“技术议题不提供直播，主因是成本”为明确答复；Desnoyers 的“已解决单步执行难题”为自陈，落书须与当期 rseq 补丁集核对；Rostedt 的“Printk redesign 场次亦须 Sergey 参与”为议程提醒。
**文献**：DSLXC-5347、DSLXC-5351、DSLXC-5361、DSLXC-5362、DSLXC-5363、DSLXC-5378、DSLXC-5379（`ksummit-discuss.messages.348522`、`ksummit-discuss.messages.348526`、`ksummit-discuss.messages.348536`、`ksummit-discuss.messages.348537`、`ksummit-discuss.messages.348538`、`ksummit-discuss.messages.348553`、`ksummit-discuss.messages.348554`，2017-10-20、2017-10-20、2017-10-20、2017-10-20、2017-10-20、2017-10-23、2017-10-23），全文见 `raw_source.raw_json`

## 34.5 【Linux社区】TAB 选举与议程地点（6 例）

**要点（判定表逐字）**：Ted 发布 Kernel Summit v2 草案议程：含 tracing ABI、printk、文档、PM、rseq、回归追踪、kselftest、安全等时段，并列出未定焦点（mobile、Kconfig、maintainer summit 技术议题）；Chris Mason 发布 TAB 选举提醒 v2：已有六名提名（Corbet、Greg KH、Shuah、Rostedt、Ts'o、Bird），并介绍 TAB 职责与 10-25 选举安排；Frank Rowand 向 Chris Mason 询问 TAB 现任成员及哪些任期届满；Greg KH 回复 Frank Rowand：TAB 现任成员见 linuxfoundation.org 专页；Mark Brown 询问 v2 议程中各场次的物理地点，称官网未见 KS 或 OSS Europe 信息；Chris Mason 回复 Frank Rowand：Greg 已给 TAB 链接，列出届满任期者（Corbet、Greg KH、Shuah、Rostedt、Ts'o）

**史料**：`348540`、`348546`、`348549`、`348550`、`348551`、`348555`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348540 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348546 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348549 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348550 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348551 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348555 -->` 

**史观**：权力再分配（总纲第 3 条——不存在进步，只有权力再分配：TAB 五席改选与任期届满更替，正是话语权与席位的形式主义再分配）；本体论上各方平等（总纲第 8 条——本体论上各方平等：现任成员查询与届满名单公开并列，无优劣预设）
**辨析**：Mason 的“已有六名提名”与“列出届满任期者”为选举事务记录；Rowand 的“询问 TAB 现任成员及哪些任期届满”为程序之问；Brown 的“官网未见 KS 或 OSS Europe 信息”为信息缺位之实况，非结论。
**文献**：DSLXC-5365、DSLXC-5371、DSLXC-5374、DSLXC-5375、DSLXC-5376、DSLXC-5380（`ksummit-discuss.messages.348540`、`ksummit-discuss.messages.348546`、`ksummit-discuss.messages.348549`、`ksummit-discuss.messages.348550`、`ksummit-discuss.messages.348551`、`ksummit-discuss.messages.348555`，2017-10-21、2017-10-22、2017-10-23、2017-10-23、2017-10-23、2017-10-23），全文见 `raw_source.raw_json`

## 34.6 【Linux社区】开发者工作站安全与 2014 档案四封（5 例）

**要点（判定表逐字）**：Ted 确认采纳 Konstantin Ryabitsev 关于开发者工作站安全卫生的四十分钟时段，内容含 PGP／ssh 密钥实践、Git 与 PGP 签名、firefox 加 firejail、Wayland 安全收益；Ted（2014 档案）论 bug 报告：主张需要专人改进 kerneloops.org、挖掘规律并自动化转发开发者，质疑是否值得单设技术议题，警惕沦为无果空谈；Josh Triplett（2014 档案）论跨子系统维护工作流：以 tiny 树按 topic 而非子系统收补丁，并提议 kernel.org 提供类似 Andrew 与 Greg 的 git 钩子自动通知提交者合入；Tim Bird（2014 档案）回应 Josh 的 tinification 议题，主张以自动化缩减内核（如 DT 静态化以常量传播与死代码消除），并荐 linux-embedded 列表与 elinux wiki；Olof Johansson（2014 档案）回应 Josh：arm-soc 以 topic 分支作基底并早抓冲突，认可按 topic 而非子系统维护树，但要求知情且经评审、非绕开异议维护者

**史料**：`348514`、`348512`、`348523`、`348534`、`348545`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348514 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348512 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348523 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348534 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348545 -->` 

**史观**：动手者创造历史（总纲第 10 条——动手者创造历史：以 Triplett 提议 kernel.org 提供 git 钩子自动通知提交者合入、Bird 主张以自动化缩减内核为分析单位）；知识注定过时（总纲第 22 条——知识注定过时：DT 静态化以常量传播与死代码消除，即令配置知识在构建期固化）
**辨析**：Ted 的“质疑是否值得单设技术议题，警惕沦为无果空谈”为开放之疑；Johansson 的“认可按 topic 而非子系统维护树，但要求知情且经评审、非绕开异议维护者”为条件性支持；Bird 的“荐 linux-embedded 列表与 elinux wiki”为资料指引。
**文献**：DSLXC-5339、DSLXC-5337、DSLXC-5348、DSLXC-5359、DSLXC-5370（`ksummit-discuss.messages.348514`、`ksummit-discuss.messages.348512`、`ksummit-discuss.messages.348523`、`ksummit-discuss.messages.348534`、`ksummit-discuss.messages.348545`，2017-10-20、2014-05-13、2014-05-13、2014-05-13、2014-05-13），全文见 `raw_source.raw_json`

---
注：本文件由判定表程序化生成（6 块，覆盖 50/50 CAND，两遍计数核对通过）；要点逐字取自判定表“要点”列（主代理全读审读实录），史料锚与 CAND 一一对应，全文以 raw_source.raw_json 为准。
