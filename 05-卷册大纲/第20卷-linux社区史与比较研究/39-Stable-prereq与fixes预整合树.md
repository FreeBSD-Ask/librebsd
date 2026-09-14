# 39 【Linux社区】Stable-prereq与fixes预整合树

> 对应页面：ksummit-discuss p90（pk 348706-348755，2018 fixes 预整合树落地 + 2014 ACPI/DT 档案）
> 判定：50 CAND / 0 NV
> 编号：DSLXC-5581..5630 | claim 已入库（50/50，dslinux_claims.duckdb）

## 39.1 【Linux社区】Stable-prereq 标签与 Cc: stable 文档之辨（12 例）

**要点（判定表逐字）**：Sasha Levin 贴出 stable-tools 仓库的 stable-deps 工具链接，自动追踪 stable 回溯补丁的依赖链；对 Willy Tarreau 关于小补丁集依赖复杂的论点以笑脸回应；David Howells 要求 Sasha Levin 勿用 Cc: stable 加 commit-id 注释的写法，称其会破坏部分邮件地址解析工具；Jani Nikula 指出该用法自 Sebastian Siewior 于 v2.6.33 提交的 Doc/stable rules 文档起即有记载，工具方应有足够时间修正解析；Theodore Y. Ts'o 认为文档已过时、实际常用于标注适用内核版本，提议删除旧文并新增 Stable-prereq 头部显式列出回溯依赖（顺序有意义）；Greg KH 对 Ted Ts'o 的 Stable-prereq 提议表示不解，反问现有 Cc: stable 机制何处损坏；Ted Ts'o 澄清 Jani 所引文档与其实际用法不符，指 8e9b9362266d 引入的 prereq 写法非现行实践，主张删之并改用 Stable-prereq 显式依赖；James Bottomley 认同文档不反映现行实践，称 SCSI 侧若 cc 漏依赖则 Greg KH 退回补正即可，并指 Greg 现自跑脚本、自己已不涉其中；Sasha Levin 同意将 prereq 挪为独立 tag 以简化脚本，并举某 patch 在 ARMv7 特定 flavor 可编译却启动失败为例，证仅看 apply/build 不足恃；Ted Ts'o 强调问题在文档是谎言、须建新 tag 而非挪 tag，依赖声明交由 Sasha 与 Greg 等 stable 维护者定夺；Eric W. Biederman 说明自己只用 Cc: stable 与 Fixes: sha1 两头部，旧到 bitkeeper 前者用 Fixes: v2.0.1 或 History Tree 链接；Willy Tarreau 主张以自然语言写明回溯范围胜过复杂表达式；Sasha Levin 对 Ted 所谓文档不反映现状表示困惑，列出现行文档允许的三种标注方式（空 tag、带版本、带 prereq commit），称 prereq 用法罕见但本就预期；Greg KH 盛赞 Fixes: tag（谢 James Bottomley），称其脚本可据此追踪 fix 是否进入 stable 树，主张保持简单、文档若需清理欢迎发补丁

**史料**：`348706`、`348709`、`348710`、`348711`、`348714`、`348715`、`348716`、`348717`、`348718`、`348719`、`348720`、`348721`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348706 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348709 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348710 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348711 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348714 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348715 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348716 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348717 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348718 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348719 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348720 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348721 -->` 

**史观**：权力再分配（总纲第 3 条——不存在进步，只有权力再分配：Cc: stable 与 Stable-prereq 两种标注法之争，实为依赖声明权与文档解释权的再分配）；经验优先（总纲第 9 条——经验优先：以 8e9b9362266d 引入的 prereq 写法非现行实践、某 patch 在 ARMv7 特定 flavor 可编译却启动失败等实例为判据）
**辨析**：Howells 与 Nikula 主张“文档早有记载、工具方应改”，Ts'o 与 Bottomley 则称“文档不反映现行实践、应删旧立新”，两造并置未作单方裁断；Ts'o 的“问题在文档是谎言、须建新 tag 而非挪 tag”为其立场；Greg KH 的“盛赞 Fixes: tag，主张保持简单、文档若需清理欢迎发补丁”为收束态度。
**文献**：DSLXC-5581、DSLXC-5584、DSLXC-5585、DSLXC-5586、DSLXC-5589、DSLXC-5590、DSLXC-5591、DSLXC-5592、DSLXC-5593、DSLXC-5594、DSLXC-5595、DSLXC-5596（`ksummit-discuss.messages.348706`、`ksummit-discuss.messages.348709`、`ksummit-discuss.messages.348710`、`ksummit-discuss.messages.348711`、`ksummit-discuss.messages.348714`、`ksummit-discuss.messages.348715`、`ksummit-discuss.messages.348716`、`ksummit-discuss.messages.348717`、`ksummit-discuss.messages.348718`、`ksummit-discuss.messages.348719`、`ksummit-discuss.messages.348720`、`ksummit-discuss.messages.348721`，2018-05-03、2018-05-04、2018-05-04、2018-05-04、2018-05-04、2018-05-04、2018-05-04、2018-05-04、2018-05-04、2018-05-05、2018-05-05、2018-05-05），全文见 `raw_source.raw_json`

## 39.2 【Linux社区】fixes 预整合树构想与 linux-next 落地（12 例）

**要点（判定表逐字）**：Ulf Hansson 提议设立专用于 fixes 的预整合树，使 fix 在合入 Linus 树前能与 new material 分开自动化测试，自承或此前已讨论过；Mark Brown 赞 Ulf Hansson 的 fixes 预整合树构想，抄送 Stephen Rothwell 征询，称休假归来愿先做试验性尝试；Daniel Vetter 指出 Stephen Rothwell 本就在合-next 前先合各-fixes 分支，只需把该中间态推为 linux-fixes 分支供测试 bot 消费即可；Geert Uytterhoeven 对 Daniel Vetter 之议+1 支持；Mark Brown 补正：当前仅有人单独请合的-fixes 分支占比不高，还需鼓励维护者把 fixes 分支单独列出（因与开发分支常合并不洁）；Stephen Rothwell 回应好主意愿试行，并说自己当前已持 44 个此类 fixes 分支、欢迎更多；Stephen Rothwell 答复 Vinod Koul：请维护者主动发 fixes 分支（已加 slave-dma/fixes），并问是否将其联系地址由 Intel 换 kernel.org；Mark Brown 称自己所有树皆配有 for-linus 分支伴随 for-next；Guenter Roeck 请 Stephen 加 groeck/linux-staging hwmon 为 fixes 分支；Dan Williams 请加 nvdimm/nvdimm libnvdimm-fixes，说明其与 libnvdimm-for-next 合并以解决冲突，建议-next 只拉 for-next、新 effort 拉 fixes；Stephen Rothwell 应 Guenter Roeck 已将 hwmon fixes 分支加入，并附 linux-next 参与须知（GPLv2、Signed-off-by、已发列表、已审、已单测、奔当前或下个合并窗口）；Stephen Rothwell 应 Dan Williams 已加 libnvdimm-fixes，称冲突通常由其合并不见更佳，并重述 linux-next 集成测试之目的与参与须知

**史料**：`348712`、`348734`、`348736`、`348737`、`348738`、`348739`、`348740`、`348741`、`348742`、`348743`、`348744`、`348745`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348712 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348734 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348736 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348737 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348738 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348739 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348740 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348741 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348742 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348743 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348744 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348745 -->` 

**史观**：动手者创造历史（总纲第 10 条——动手者创造历史：以 Hansson 提议 fixes 预整合树、Vetter 提议把中间态推为 linux-fixes 分支供测试 bot 消费为分析单位）；分离聚合是永恒规律（总纲第 4 条——分离聚合是永恒规律：for-next 与 for-linus 两分支并存，正是树间分合的相位）
**辨析**：Rothwell 的“当前已持 44 个此类 fixes 分支、欢迎更多”为实况；Brown 的“当前仅有人单独请合的 -fixes 分支占比不高，还需鼓励维护者把 fixes 分支单独列出”为推广之虑；Williams 的“建议 -next 只拉 for-next、新 effort 拉 fixes”为分支策略主张。
**文献**：DSLXC-5587、DSLXC-5609、DSLXC-5611、DSLXC-5612、DSLXC-5613、DSLXC-5614、DSLXC-5615、DSLXC-5616、DSLXC-5617、DSLXC-5618、DSLXC-5619、DSLXC-5620（`ksummit-discuss.messages.348712`、`ksummit-discuss.messages.348734`、`ksummit-discuss.messages.348736`、`ksummit-discuss.messages.348737`、`ksummit-discuss.messages.348738`、`ksummit-discuss.messages.348739`、`ksummit-discuss.messages.348740`、`ksummit-discuss.messages.348741`、`ksummit-discuss.messages.348742`、`ksummit-discuss.messages.348743`、`ksummit-discuss.messages.348744`、`ksummit-discuss.messages.348745`，2018-05-04、2018-05-09、2018-05-09、2018-05-09、2018-05-09、2018-05-09、2018-05-09、2018-05-09、2018-05-09、2018-05-09、2018-05-09、2018-05-09），全文见 `raw_source.raw_json`

## 39.3 【Linux社区】linux-next 测试动员与 -rc 质量之争（上半）（8 例）

**要点（判定表逐字）**：Mark Brown 对 Guenter Roeck 所言在 linux-next 报 bug 反被 flame 一事表示震惊，强调-next 存在意义即测试，质疑把树放进-next 却不愿被测试的动机；Tony Lindgren 认同 linux-next 测试至关重要，称其为合并窗口后拿到可用-rc1 的最佳途径，且-next 中 bug 往往比-rc 周期修得更快（因维护者知不修则无法合入）；Sasha Levin 问 Tony Lindgren 究竟多少用户真跑 Linus 树，称 Azure 所见皆基于-stable，质疑是否应以几乎无人跑 Linus 树为假设施策；Sasha Levin 反驳 Mark Brown 称-next 测试被 flame 之说，称 MSFT 测试线将直接把-next 问题报 LKML，0-day bot 已抓多数、唯 Hyper-V 少人测；Sasha Levin 追问 Tony Lindgren 究竟多少用户跑 Linus 树，称 Azure 上所见皆基于-stable，质疑是否应以几乎无人跑 Linus 树为假设施策；Tony Lindgren 认同 prosumer 一说，主张维护者常测 linux-next 以达无回归的-rc1，余下-rc 周期靠 prosumer 报告；自己仅-next 数周无回归才敢上笔记本；Sasha Levin 指无人会守住 vanilla 点发布版超一周，.0 发布反倒诱人塞入测试不足代码；提议 Linus 干脆不发点发布、常开合并窗口、-stable 每周发版以消除抢送动机；Matthew Wilcox 反驳称自己跑 Debian Testing 近乎紧跟 Linus 发布、Fedora rawhide 亦类似，指 Sasha 样本遗漏了这批人

**史料**：`348707`、`348708`、`348722`、`348723`、`348725`、`348726`、`348727`、`348728`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348707 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348708 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348722 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348723 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348725 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348726 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348727 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348728 -->` 

**史观**：本体论上各方平等（总纲第 8 条——本体论上各方平等：Levin 的“Azure 所见皆基于 -stable，质疑以几乎无人跑 Linus 树为假设施策”与 Lindgren 的“维护者常测 linux-next 以达无回归的 -rc1”并置）；经验优先（总纲第 9 条——经验优先：以 -next 中 bug 往往比 -rc 周期修得更快、自己仅 -next 数周无回归才敢上笔记本等经验为判据）
**辨析**：Brown 的“质疑把树放进 -next 却不愿被测试的动机”为动机之问；Levin 的“指无人会守住 vanilla 点发布版超一周”为其核心假设，Wilcox 以“自己跑 Debian Testing 近乎紧跟 Linus 发布、Fedora rawhide 亦类似”反驳，指出样本遗漏；Levin 的“提议 Linus 干脆不发点发布、常开合并窗口”为激进提案，本页未见采纳。
**文献**：DSLXC-5582、DSLXC-5583、DSLXC-5597、DSLXC-5598、DSLXC-5600、DSLXC-5601、DSLXC-5602、DSLXC-5603（`ksummit-discuss.messages.348707`、`ksummit-discuss.messages.348708`、`ksummit-discuss.messages.348722`、`ksummit-discuss.messages.348723`、`ksummit-discuss.messages.348725`、`ksummit-discuss.messages.348726`、`ksummit-discuss.messages.348727`、`ksummit-discuss.messages.348728`，2018-05-03、2018-05-03、2018-05-08、2018-05-08、2018-05-08、2018-05-08、2018-05-08、2018-05-08），全文见 `raw_source.raw_json`

## 39.4 【Linux社区】-rc 质量之争（下半）与 .0 发布之辩（6 例）

**要点（判定表逐字）**：Sasha Levin 辩称 Debian testing 实为跟随当前-stable 树、约一周后转下一版，rawhide 则是 Linus 树每日构建；重申无人守住某发布版超一周；Sasha Levin 回应 David Lang：重点非无人用 Linus 内核，而是无人计划守住某.0 版三月至下一版；.0 发布令人在意却无意义，反致抢送测试不足提交；Dan Williams 反对贬低.0 发布，称维护者若于晚期-rc 塞入破坏应得反馈而非被淡化，并问是否应抬高晚期 fix 门槛；James Bottomley 指自己笔记本正跑 v4.16 tag（非本意只为缺 Round Tuit），称.0 作为一切节奏之源极关键，轻视-rc 将殃及 stable；Mark Brown 补充另有一类人：拟用 stable 出货却在产品开发期跟踪上游，以便量产时落到最新 stable；Tony Lindgren 指人人应常测 linux-next，因-regressions 常源于他人分支或完全未测的 clean-up，最终在-rc1 被合入

**史料**：`348729`、`348730`、`348731`、`348732`、`348733`、`348751`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348729 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348730 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348731 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348732 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348733 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348751 -->` 

**史观**：本体论上各方平等（总纲第 8 条——本体论上各方平等：Williams 的“反对贬低 .0 发布、晚期 -rc 塞入破坏应得反馈”与 Bottomley 的“.0 作为一切节奏之源极关键”同向，与 Levin 的“.0 发布令人在意却无意义”对撞）；经验优先（总纲第 9 条——经验优先：以 Bottomley 自陈笔记本正跑 v4.16 tag、Brown 的“拟用 stable 出货却在产品开发期跟踪上游”一类用户等实例为判据）
**辨析**：Levin 的“辩称 Debian testing 实为跟随当前 -stable 树、约一周后转下一版，rawhide 则是 Linus 树每日构建”为对其自身假设的补正；Brown 的“补充另有一类人：拟用 stable 出货却在产品开发期跟踪上游”为样本补全；Lindgren 的“因 -regressions 常源于他人分支或完全未测的 clean-up，最终在 -rc1 被合入”为机制归因。
**文献**：DSLXC-5604、DSLXC-5605、DSLXC-5606、DSLXC-5607、DSLXC-5608、DSLXC-5626（`ksummit-discuss.messages.348729`、`ksummit-discuss.messages.348730`、`ksummit-discuss.messages.348731`、`ksummit-discuss.messages.348732`、`ksummit-discuss.messages.348733`、`ksummit-discuss.messages.348751`，2018-05-08、2018-05-08、2018-05-08、2018-05-08、2018-05-09、2018-05-10），全文见 `raw_source.raw_json`

## 39.5 【Linux社区】各树 fixes 分支并入与 2014 档案四封（12 例）

**要点（判定表逐字）**：Stephen Rothwell 应 Boris Brezillon 将 mtd-fixes 加入 linux-next，并移除重复的 mtd 旧项、把 l2-mtd 改名为 mtd；Stephen Rothwell 指 regmap 与 regulator 树暂无 for-linus 分支，当日加 sound-asoc-fixes 与 spi-fixes，并重述参与须知；Sasha Levin 对 next-fixes 兴致浓厚，建议比较未过此树、短停与久停此树的补丁统计，并列出 tip、block、s390、fuse、iwlwifi、scsi、hid、ftrace 等大量*-urgent/for-linus 分支待征询维护者；Mark Brown 回 Stephen 称 regmap/regulator 推送异常、已删后重推，盼解决；Tony Lindgren 请 Stephen 加 tmlind/linux-omap fixes 分支；Jiri Kosina 述自己把当前周期将送 Linus 的-fixes 分支也并入 for-next，以获-next 覆盖并早察合冲突，问他人是否可行；Sasha Levin 回 Jiri Kosina：说明-rc1 后 next 充斥下个窗口提交而极不稳，next-fixes 专收当前窗口 fixes 以提供更稳可跑可验之树，单独提供 fixes 分支可多得覆盖；Stephen Rothwell 应 Mark Brown 已加 regmap-fixes 与 regulator-fixes；Rafael J. Wysocki 论 ACPI/DT 驱动模型：指出现有 ACPI 缺乏编码时钟、电压调节器、PWM、pin control 乃至 GPIO 的能力，若扩展使信息入表则 fw_get_something 接口可与 of_趋同；Olof Johansson 以 PCI(e) host bridge 为例，指 DT 嵌入式系统须经历检测、上电时钟、设 MMIO/PIO 窗口、全总线扫描等步骤，与 ACPI/server OF 假设固件已初始化全然不同，倡保持代码分离；Rafael 回应 Olof：struct device 下 device_node 与 acpi_node.companion 互斥、此路不通，设备引用亦因 phandle 与 ACPI 命名空间路径而异，认为 Arnd Bergmann 所提方案最简；Olof 再驳 Rafael：其建议仍假设 device node 与 struct device 一一对应（实情不然），并问 Rafael 约何时能试出避免驱动懂两种固件界面之法

**史料**：`348747`、`348748`、`348749`、`348750`、`348752`、`348753`、`348754`、`348755`、`348713`、`348724`、`348735`、`348746`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348747 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348748 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348749 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348750 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348752 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348753 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348754 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348755 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348713 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348724 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348735 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348746 -->` 

**史观**：分离聚合是永恒规律（总纲第 4 条——分离聚合是永恒规律：各子系统 -fixes 分支并入 linux-next、next-fixes 专收当前窗口 fixes，正是树间分合的相位）；经验优先（总纲第 9 条——经验优先：以 Johansson 的 PCI(e) host bridge 须经检测、上电时钟、设 MMIO/PIO 窗口、全总线扫描等步骤为判据）
**辨析**：Wysocki 的“若扩展使信息入表则 fw_get_something 接口可与 of_ 趋同”为路径主张，Johansson 以“与 ACPI/server OF 假设固件已初始化全然不同，倡保持代码分离”反驳，两说对撞；Wysocki 的“struct device 下 device_node 与 acpi_node.companion 互斥、此路不通”为技术约束；Johansson 的“其建议仍假设 device node 与 struct device 一一对应（实情不然）”为纠正。
**文献**：DSLXC-5622、DSLXC-5623、DSLXC-5624、DSLXC-5625、DSLXC-5627、DSLXC-5628、DSLXC-5629、DSLXC-5630、DSLXC-5588、DSLXC-5599、DSLXC-5610、DSLXC-5621（`ksummit-discuss.messages.348747`、`ksummit-discuss.messages.348748`、`ksummit-discuss.messages.348749`、`ksummit-discuss.messages.348750`、`ksummit-discuss.messages.348752`、`ksummit-discuss.messages.348753`、`ksummit-discuss.messages.348754`、`ksummit-discuss.messages.348755`、`ksummit-discuss.messages.348713`、`ksummit-discuss.messages.348724`、`ksummit-discuss.messages.348735`、`ksummit-discuss.messages.348746`，2018-05-09、2018-05-09、2018-05-10、2018-05-10、2018-05-10、2018-05-10、2018-05-10、2018-05-10、2014-05-13、2014-05-13、2014-05-13、2014-05-13），全文见 `raw_source.raw_json`

---
注：本文件由判定表程序化生成（5 块，覆盖 50/50 CAND，两遍计数核对通过）；要点逐字取自判定表“要点”列（主代理全读审读实录），史料锚与 CAND 一一对应，全文以 raw_source.raw_json 为准。
