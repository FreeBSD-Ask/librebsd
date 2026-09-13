# 39-Stable-prereq与fixes预整合树.md

> 对应页面：ksummit-discuss p90（pk 348706-348755，2018 fixes 预整合树落地 + 2014 ACPI/DT 档案）
> 判定：50 CAND / 0 NV
> 编号：DSLXC-5581..5630 | claim 已入库（50/50，dslinux_claims.duckdb）

## 39.1 【Linux社区】Stable-prereq 标签与 Cc: stable 文档之辨（12 例）

**要点（判定表逐字）**：Sasha Levin贴出stable-tools仓库的stable-deps工具链接，自动追踪stable回溯补丁的依赖链；对Willy Tarreau关于小补丁集依赖复杂的论点以笑脸回应；David Howells要求Sasha Levin勿用Cc: stable加commit-id注释的写法，称其会破坏部分邮件地址解析工具；Jani Nikula指出该用法自Sebastian Siewior于v2.6.33提交的Doc/stable rules文档起即有记载，工具方应有足够时间修正解析；Theodore Y. Ts'o认为文档已过时、实际常用于标注适用内核版本，提议删除旧文并新增Stable-prereq头部显式列出回溯依赖（顺序有意义）；Greg KH对Ted Ts'o的Stable-prereq提议表示不解，反问现有Cc: stable机制何处损坏；Ted Ts'o澄清Jani所引文档与其实际用法不符，指8e9b9362266d引入的prereq写法非现行实践，主张删之并改用Stable-prereq显式依赖；James Bottomley认同文档不反映现行实践，称SCSI侧若cc漏依赖则Greg KH退回补正即可，并指Greg现自跑脚本、自己已不涉其中；Sasha Levin同意将prereq挪为独立tag以简化脚本，并举某patch在ARMv7特定flavor可编译却启动失败为例，证仅看apply/build不足恃；Ted Ts'o强调问题在文档是谎言、须建新tag而非挪tag，依赖声明交由Sasha与Greg等stable维护者定夺；Eric W. Biederman说明自己只用Cc: stable与Fixes: sha1两头部，旧到bitkeeper前者用Fixes: v2.0.1或History Tree链接；Willy Tarreau主张以自然语言写明回溯范围胜过复杂表达式；Sasha Levin对Ted所谓文档不反映现状表示困惑，列出现行文档允许的三种标注方式（空tag、带版本、带prereq commit），称prereq用法罕见但本就预期；Greg KH盛赞Fixes: tag（谢James Bottomley），称其脚本可据此追踪fix是否进入stable树，主张保持简单、文档若需清理欢迎发补丁

**史料**：`348706、`348709、`348710、`348711、`348714、`348715、`348716、`348717、`348718、`348719、`348720、`348721

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348706 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348709 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348710 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348711 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348714 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348715 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348716 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348717 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348718 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348719 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348720 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348721 -->` 

## 39.2 【Linux社区】fixes 预整合树构想与 linux-next 落地（12 例）

**要点（判定表逐字）**：Ulf Hansson提议设立专用于fixes的预整合树，使fix在合入Linus树前能与new material分开自动化测试，自承或此前已讨论过；Mark Brown赞Ulf Hansson的fixes预整合树构想，抄送Stephen Rothwell征询，称休假归来愿先做试验性尝试；Daniel Vetter指出Stephen Rothwell本就在合-next前先合各-fixes分支，只需把该中间态推为linux-fixes分支供测试bot消费即可；Geert Uytterhoeven对Daniel Vetter之议+1支持；Mark Brown补正：当前仅有人单独请合的-fixes分支占比不高，还需鼓励维护者把fixes分支单独列出（因与开发分支常合并不洁）；Stephen Rothwell回应好主意愿试行，并说自己当前已持44个此类fixes分支、欢迎更多；Stephen Rothwell答复Vinod Koul：请维护者主动发fixes分支（已加slave-dma/fixes），并问是否将其联系地址由Intel换kernel.org；Mark Brown称自己所有树皆配有for-linus分支伴随for-next；Guenter Roeck请Stephen加groeck/linux-staging hwmon为fixes分支；Dan Williams请加nvdimm/nvdimm libnvdimm-fixes，说明其与libnvdimm-for-next合并以解决冲突，建议-next只拉for-next、新effort拉fixes；Stephen Rothwell应Guenter Roeck已将hwmon fixes分支加入，并附linux-next参与须知（GPLv2、Signed-off-by、已发列表、已审、已单测、奔当前或下个合并窗口）；Stephen Rothwell应Dan Williams已加libnvdimm-fixes，称冲突通常由其合并不见更佳，并重述linux-next集成测试之目的与参与须知

**史料**：`348712、`348734、`348736、`348737、`348738、`348739、`348740、`348741、`348742、`348743、`348744、`348745

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348712 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348734 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348736 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348737 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348738 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348739 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348740 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348741 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348742 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348743 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348744 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348745 -->` 

## 39.3 【Linux社区】linux-next 测试动员与 -rc 质量之争（上半）（8 例）

**要点（判定表逐字）**：Mark Brown对Guenter Roeck所言在linux-next报bug反被flame一事表示震惊，强调-next存在意义即测试，质疑把树放进-next却不愿被测试的动机；Tony Lindgren认同linux-next测试至关重要，称其为合并窗口后拿到可用-rc1的最佳途径，且-next中bug往往比-rc周期修得更快（因维护者知不修则无法合入）；Sasha Levin问Tony Lindgren究竟多少用户真跑Linus树，称Azure所见皆基于-stable，质疑是否应以几乎无人跑Linus树为假设施策；Sasha Levin反驳Mark Brown称-next测试被flame之说，称MSFT测试线将直接把-next问题报LKML，0-day bot已抓多数、唯Hyper-V少人测；Sasha Levin追问Tony Lindgren究竟多少用户跑Linus树，称Azure上所见皆基于-stable，质疑是否应以几乎无人跑Linus树为假设施策；Tony Lindgren认同prosumer一说，主张维护者常测linux-next以达无回归的-rc1，余下-rc周期靠prosumer报告；自己仅-next数周无回归才敢上笔记本；Sasha Levin指无人会守住vanilla点发布版超一周，.0发布反倒诱人塞入测试不足代码；提议Linus干脆不发点发布、常开合并窗口、-stable每周发版以消除抢送动机；Matthew Wilcox反驳称自己跑Debian Testing近乎紧跟Linus发布、Fedora rawhide亦类似，指Sasha样本遗漏了这批人

**史料**：`348707、`348708、`348722、`348723、`348725、`348726、`348727、`348728

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348707 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348708 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348722 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348723 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348725 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348726 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348727 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348728 -->` 

## 39.4 【Linux社区】-rc 质量之争（下半）与 .0 发布之辩（6 例）

**要点（判定表逐字）**：Sasha Levin辩称Debian testing实为跟随当前-stable树、约一周后转下一版，rawhide则是Linus树每日构建；重申无人守住某发布版超一周；Sasha Levin回应David Lang：重点非无人用Linus内核，而是无人计划守住某.0版三月至下一版；.0发布令人在意却无意义，反致抢送测试不足提交；Dan Williams反对贬低.0发布，称维护者若于晚期-rc塞入破坏应得反馈而非被淡化，并问是否应抬高晚期fix门槛；James Bottomley指自己笔记本正跑v4.16 tag（非本意只为缺Round Tuit），称.0作为一切节奏之源极关键，轻视-rc将殃及stable；Mark Brown补充另有一类人：拟用stable出货却在产品开发期跟踪上游，以便量产时落到最新stable；Tony Lindgren指人人应常测linux-next，因-regressions常源于他人分支或完全未测的clean-up，最终在-rc1被合入

**史料**：`348729、`348730、`348731、`348732、`348733、`348751

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348729 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348730 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348731 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348732 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348733 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348751 -->` 

## 39.5 【Linux社区】各树 fixes 分支并入与 2014 档案四封（12 例）

**要点（判定表逐字）**：Stephen Rothwell应Boris Brezillon将mtd-fixes加入linux-next，并移除重复的mtd旧项、把l2-mtd改名为mtd；Stephen Rothwell指regmap与regulator树暂无for-linus分支，当日加sound-asoc-fixes与spi-fixes，并重述参与须知；Sasha Levin对next-fixes兴致浓厚，建议比较未过此树、短停与久停此树的补丁统计，并列出tip、block、s390、fuse、iwlwifi、scsi、hid、ftrace等大量*-urgent/for-linus分支待征询维护者；Mark Brown回Stephen称regmap/regulator推送异常、已删后重推，盼解决；Tony Lindgren请Stephen加tmlind/linux-omap fixes分支；Jiri Kosina述自己把当前周期将送Linus的-fixes分支也并入for-next，以获-next覆盖并早察合冲突，问他人是否可行；Sasha Levin回Jiri Kosina：说明-rc1后next充斥下个窗口提交而极不稳，next-fixes专收当前窗口fixes以提供更稳可跑可验之树，单独提供fixes分支可多得覆盖；Stephen Rothwell应Mark Brown已加regmap-fixes与regulator-fixes；Rafael J. Wysocki论ACPI/DT驱动模型：指出现有ACPI缺乏编码时钟、电压调节器、PWM、pin control乃至GPIO的能力，若扩展使信息入表则fw_get_something接口可与of_趋同；Olof Johansson以PCI(e) host bridge为例，指DT嵌入式系统须经历检测、上电时钟、设MMIO/PIO窗口、全总线扫描等步骤，与ACPI/server OF假设固件已初始化全然不同，倡保持代码分离；Rafael回应Olof：struct device下device_node与acpi_node.companion互斥、此路不通，设备引用亦因phandle与ACPI命名空间路径而异，认为Arnd Bergmann所提方案最简；Olof再驳Rafael：其建议仍假设device node与struct device一一对应（实情不然），并问Rafael约何时能试出避免驱动懂两种固件界面之法

**史料**：`348747、`348748、`348749、`348750、`348752、`348753、`348754、`348755、`348713、`348724、`348735、`348746

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348747 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348748 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348749 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348750 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348752 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348753 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348754 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348755 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348713 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348724 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348735 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348746 -->` 

---
注：本文件由判定表程序化生成（5 块，覆盖 50/50 CAND，两遍计数核对通过）；要点逐字取自判定表「要点」列（主代理全读审读实录），史料锚与 CAND 一一对应，全文以 raw_source.raw_json 为准。
