# 33 【Linux社区】DT工作坊与跨项目DT治理

> 对应页面：ksummit-discuss p85（pk 348456-348505，2017-07-06/10 多线程并进 + 2014 档案信）
> 判定：50 CAND / 0 NV
> 编号：DSLXC-5281..5330 | claim 已入库（50/50，dslinux_claims.duckdb）

## 33.1 【Linux社区】DT 工作坊议程与 DT 仓库共用（12 例）

**要点（判定表逐字）**：Heiko Stübner 指 DT 数量问题重现于内核大量 .dts 源文件，并给出内核外 DT 仓库 devicetree-rebasing.git 链接，称其虽非权威但可体验树外仓库之感；Rob Herring 论 AArch32 基于 arm64 dts 之支持，称 RPi3 已有但跨 arch 包含文件略 hacky，理想是构建 dts 不依赖 `$ARCH` 与交叉编译器，dtb 应与 32 位或 64 位无关；Rob Herring 称问题不在内核含板文件而在各家族各自扩展难以规模化，ARM 树 DT 转换之初约 400 板、今 arm/arm64 约 1100 板且仍有 264 板未转 DT，并质疑搬出内核外仓库能解何题；Grant Likely 将 Thomas Petazzoni 提出的避免重复描述 IP 聚合（如 Marvell armada-cp110 主从几乎相同）并入 overlay 维护议题，称二者密切相关；Grant Likely 将 Michal Simek 提的 AArch32 与新增 DTS 板文件标准两题并入议程，前者与 Thomas 重复描述题合并；Grant Likely 将 Ben Dooks 提的 device-tree 总览与旧板文件问题是否解决并入 DT health check 议题，戏言盼望别沦为抱怨 DT；Grant Likely 答 Rob，称固件提供 .dtb 时树外仓库不错、且 DT 格式简单、由 DTB 回 DTS 不难，并谓绑定与 schema 应与工具同维护；Grant Likely 将 Boris 关于绑定在他项目先定义之题列入议程，称己有主张但宜在会场讨论因涉维护者；Rob Herring 答 Ian Lepore，称乐收绑定、澄清无 Linux 驱动亦可提交、dts 较复杂一般由他不全收，并促非 Linux 开发者提 dts 变更否则不会收；Ian Lepore 述 FreeBSD 周期自 Linux 树导入绑定与 dts 用于现代 arm 板，并遇小器件（如 i2c RTC）无 Linux 驱动时能否回提绑定 dts 不明；Kumar Gala 主张绑定与 .dts 文件分离、设各项目共用绑定处，并指 Zephyr 以结构化绑定规范由 .dts 生成代码（无运行时 dtb），需更多眼睛审绑定；Tim Bird 呼应由 .dts 生成（作尺寸优化），留 PS 称任人解读此为玩笑与否

**史料**：`348459`、`348462`、`348463`、`348466`、`348468`、`348469`、`348470`、`348471`、`348474`、`348475`、`348476`、`348477`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348459 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348462 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348463 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348466 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348468 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348469 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348470 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348471 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348474 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348475 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348476 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348477 -->` 

**史观**：分离聚合是永恒规律（总纲第 4 条——分离聚合是永恒规律：DT 仓库在 linux、三 BSD、u-boot、barebox、zephyr 等消费方间共用与分置，正是形式主义载体的分合）；历史地理塑造思想土壤（总纲第 20 条——历史地理塑造思想土壤：ARM 树 DT 转换之初约 400 板、今 arm/arm64 约 1100 板且仍有 264 板未转 DT，规模由生态地形塑造）
**辨析**：Herring 的“问题不在内核含板文件而在各家族各自扩展难以规模化”为归因，Likely 的“固件提供 .dtb 时树外仓库不错、绑定与 schema 应与工具同维护”为对案；Lepore 的“FreeBSD 周期自 Linux 树导入绑定与 dts”为跨项目实务一手；Bird 的“任人解读此为玩笑与否”为自陈，不得据以立论。
**文献**：DSLXC-5284、DSLXC-5287、DSLXC-5288、DSLXC-5291、DSLXC-5293、DSLXC-5294、DSLXC-5295、DSLXC-5296、DSLXC-5299、DSLXC-5300、DSLXC-5301、DSLXC-5302（`ksummit-discuss.messages.348459`、`ksummit-discuss.messages.348462`、`ksummit-discuss.messages.348463`、`ksummit-discuss.messages.348466`、`ksummit-discuss.messages.348468`、`ksummit-discuss.messages.348469`、`ksummit-discuss.messages.348470`、`ksummit-discuss.messages.348471`、`ksummit-discuss.messages.348474`、`ksummit-discuss.messages.348475`、`ksummit-discuss.messages.348476`、`ksummit-discuss.messages.348477`，2017-10-16、2017-10-16、2017-10-16、2017-10-17、2017-10-17、2017-10-17、2017-10-17、2017-10-17、2017-10-17、2017-10-17、2017-10-17、2017-10-17），全文见 `raw_source.raw_json`

## 33.2 【Linux社区】DTS 板文件膨胀与 dtb 瘦身（12 例）

**要点（判定表逐字）**：Frank Rowand 反驳 Rob 称 DTB 回可用 DTS 不难，指厂商 boot 镜像中 DTB 难提取、反编译失 phandle 引用与 label、且绝大多数会场反对将 DTS 移出内核树；Grant Likely 答 Tim Bird，让其与 Nicolas Pitre 及 Rob Herring 谈，二人已在缩减内存足迹上进展颇多；Pantelis Antoniou 称用 YAML 绑定（C 结构定义由 DT 自动填充）虽疯狂但可行，好坏另论；Alexandre Belloni 指 Pantelis 之法不作用于用 of_property_read_* 解析自定义属性的驱动，想看启动时间改善几何；Geert Uytterhoeven 问 Belloni 可否重载 of_property_read_* 以作用于稠密 C 结构；Michal Simek 称 ZynqMP 亦见 RPi3 类情形，提议将全部 DTS 移出 arch 按 SoC 厂排序、并需 Kconfig.platforms 包含，认同 arch/arm/boot/dts 文件过多；Kumar Gala 澄清 Zephyr 非生成板文件而是平台数据（IRQ、MMIO 地址之类）；Rob Herring 详述缩减未展平树：跳过禁用节点展平、去 kobject（!SYSFS），于 stm32 板将 RAM 由 120K 降至 11K，并设想构建期跑展平代码嵌入 const 数据以兼做校验；Rob Herring 答 Andre Przywara 与 Michal，区分板 dts 移出与按厂分子目录两题，指 Android Treble 使板级全为 SoC 基础 dtb 之 overlay 从而令拆分成 ABI，主线程欲处理须使板文件成 overlay 并于构建期应用；Pantelis Antoniou 答 Andre，称 YAML 输出保留引用与锚但不还原含宏与预处理器之原源，近矣未中；Tim Bird 答 Geert 与 Belloni，称可将属性读转宏内联为常量声明、失运行时配置弹性，此即嵌入式常见取舍；Tim Bird 答 Rob，称应读完线程再回、错失 Nicolas 在 LC 的演讲、将去看视频，确认尺寸议题已有人在搞

**史料**：`348480`、`348487`、`348488`、`348489`、`348491`、`348492`、`348493`、`348494`、`348495`、`348497`、`348498`、`348499`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348480 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348487 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348488 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348489 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348491 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348492 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348493 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348494 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348495 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348497 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348498 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348499 -->` 

**史观**：经验优先（总纲第 9 条——经验优先：以 stm32 板跳过禁用节点展平并去 kobject 后 RAM 由 120K 降至 11K、DTB 反编译失 phandle 引用与 label 等实测为判据）；动手者创造历史（总纲第 10 条——动手者创造历史：以构建期跑展平代码嵌入 const 数据以兼做校验的设想为分析单位）
**辨析**：Rowand 的“绝大多数会场反对将 DTS 移出内核树”为现场意见汇总，属会议记录；Antoniou 的“YAML 输出保留引用与锚但不还原含宏与预处理器之原源，近矣未中”为自评；Bird 的“可将属性读转宏内联为常量声明、失运行时配置弹性，此即嵌入式常见取舍”为取舍陈述。
**文献**：DSLXC-5305、DSLXC-5312、DSLXC-5313、DSLXC-5314、DSLXC-5316、DSLXC-5317、DSLXC-5318、DSLXC-5319、DSLXC-5320、DSLXC-5322、DSLXC-5323、DSLXC-5324（`ksummit-discuss.messages.348480`、`ksummit-discuss.messages.348487`、`ksummit-discuss.messages.348488`、`ksummit-discuss.messages.348489`、`ksummit-discuss.messages.348491`、`ksummit-discuss.messages.348492`、`ksummit-discuss.messages.348493`、`ksummit-discuss.messages.348494`、`ksummit-discuss.messages.348495`、`ksummit-discuss.messages.348497`、`ksummit-discuss.messages.348498`、`ksummit-discuss.messages.348499`，2017-10-17、2017-10-18、2017-10-18、2017-10-18、2017-10-18、2017-10-18、2017-10-18、2017-10-18、2017-10-18、2017-10-18、2017-10-18、2017-10-18），全文见 `raw_source.raw_json`

## 33.3 【Linux社区】绑定分离、YAML 与各项目分歧（12 例）

**要点（判定表逐字）**：Boris Brezillon 问当 DT 绑定先于 Linux 在他项目（补丁 810275）中定义时策略为何，应加指向外部文档的文件、复制文档还是留白；Tom Rini 盼 Android 8 拥抱 devicetree 能派人到场，因 Boris 所问类问题将浮现；Geert Uytterhoeven 问 Kumar Gala 是否用结构化绑定规范由 .dts 生成代码（Zephyr 做法，因其无运行时 dtb），戏称 closing the loop 由 .dts 生成板文件；Chen-Yu Tsai 提非 Linux 项目分歧：U-Boot 借 regulator-name 属性作驱动实例绑定（补丁 823158），恐致 DT 文件分歧，且自承未能劝退作者、workshop 已满无法出席；Mark Brown 指元问题是 U-Boot 人有自己分歧的绑定文档副本；Tom Rini 戴 U-Boot 帽称分歧多为无意、一般以 u-boot 前缀标曾被拒或不适合上游之绑定，盼借 Rob 等言再推统一；Rob Herring 答 Tim Bird，称即 Grant 所提将属性字符串转数字 ID 直引原始 FDT 数据免存属性结构，并指 XIP SPI flash 时代代码尺寸非首要、指 Nicolas 在 Connect 演讲；Alexandre Belloni 答 Tim Bird，称除非确定每设备仅一实例或属性全同，否则将属性读转宏内联不易行；Rob Herring 答 Andrew Turner，指 devicetree-rebasing.git 即供各消费方共用绑定与 dts 之仓（git-filter-branch 自内核生成、勿须附 Linux 驱动），并数消费方逾五：linux、三 BSD、u-boot、barebox、zephyr、ARM TF、UEFI；Thomas Petazzoni 回 Grant，称 AArch32 基于 arm64 dts 与重复描述 IP 聚合是截然不同问题、解法多半不同；Thomas Petazzoni 答 Ian，称提交绑定不必附驱动，举 esp8089、arm mali-utgard、mali-midgard 等无上游驱动的绑定为例；David Woodhouse 纠 Belloni，称其所谓 of_property_read_* 应是指 device_property_read_* 之类

**史料**：`348465`、`348472`、`348473`、`348484`、`348485`、`348500`、`348502`、`348504`、`348505`、`348481`、`348482`、`348496`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348465 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348472 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348473 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348484 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348485 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348500 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348502 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348504 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348505 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348481 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348482 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348496 -->` 

**史观**：本体论上各方平等（总纲第 8 条——本体论上各方平等：Tsai 的 U-Boot regulator-name 分歧与 Brown 的“元问题是 U-Boot 人有自己分歧的绑定文档副本”并置，Rini 戴 U-Boot 帽再陈）；分离聚合是永恒规律（总纲第 4 条——分离聚合是永恒规律：devicetree-rebasing.git 供各消费方共用绑定与 dts，消费方逾五）
**辨析**：Petazzoni 的“AArch32 基于 arm64 dts 与重复描述 IP 聚合是截然不同问题、解法多半不同”为纠正 Grant 的合并之议；Rini 的“U-Boot 分歧多为无意、一般以 u-boot 前缀标曾被拒或不适合上游之绑定”为澄清；Woodhouse 的“其所谓 of_property_read_* 应是指 device_property_read_* 之类”为术语纠正。
**文献**：DSLXC-5290、DSLXC-5297、DSLXC-5298、DSLXC-5309、DSLXC-5310、DSLXC-5325、DSLXC-5327、DSLXC-5329、DSLXC-5330、DSLXC-5306、DSLXC-5307、DSLXC-5321（`ksummit-discuss.messages.348465`、`ksummit-discuss.messages.348472`、`ksummit-discuss.messages.348473`、`ksummit-discuss.messages.348484`、`ksummit-discuss.messages.348485`、`ksummit-discuss.messages.348500`、`ksummit-discuss.messages.348502`、`ksummit-discuss.messages.348504`、`ksummit-discuss.messages.348505`、`ksummit-discuss.messages.348481`、`ksummit-discuss.messages.348482`、`ksummit-discuss.messages.348496`，2017-10-17、2017-10-17、2017-10-17、2017-10-18、2017-10-18、2017-10-18、2017-10-18、2017-10-18、2017-10-18、2017-10-18、2017-10-18、2017-10-18），全文见 `raw_source.raw_json`

## 33.4 【Linux社区】TAB 选举与 2014 档案六封（8 例）

**要点（判定表逐字）**：Stephen Warren 提议在 MAINTAINERS 增标记，使维护者能声明不希望被抄送、只发列表即可，并由 get_maintainers.pl 输出该信息，以解新人向新子系统投补丁时难觅各维护者偏好的问题；Chris Mason 发布 2017 TAB 选举召集，列出五位提名人 Jon Corbet、Greg KH、Shuah Khan、Steve Rostedt、Ted Tso，并说明选举于布拉格内核峰会周三举行、任期两年、每年改选五席；Steven Rostedt 自荐连任 TAB，自陈自 2001 年从事内核、维护 tracing 子系统与 PREEMPT_RT、创 make localmodconfig 与 ktest.pl，并推动 TAB 选举陈述集中公开、使 Plumbers 与内核峰会更耦合；Sarah Sharp 论 QR oops 之社会面，指 Bjorn 等维护者用 bugzilla、他人要邮件列表，报告者在哪报告很乱，建议 MAINTAINERS 列明 bugzilla 或邮件入口、手机应用据之决定投 bugzilla 或建邮件，主张此类社区议题方宜上峰会；Josh Boyer 谈内核精简（tinification）与 secure boot 补丁集，指 objectionable 的签名部分不在 Matthew 已贴集，若提案大改此法会惊讶（或欣然），并及 UEFI 论坛机密提案将 Linux secure boot 策略与微软二进制签名脱钩；Levente Kurusa 评 QR oops 编码，指 base32 比 base64 省约两成空间待算、其 Android 2.3.7 不支持 HTML Media Capture 免 app 方案；Josh Boyer 应 Sarah 指 Fedora 亦陷 Red Hat bugzilla 无人看之困，戏言可爬刮 RHBZ 倒灌 LKML 但无益，愿谈如何何处报告问题；Greg KH 答 Sarah，称 kerneloops.org 能聚同 oops、bugzilla 不能合并须人工去重，主张加 MAINTAINERS 字段，并断言此类技术讨论留邮件更佳、KS 易沦为实现细节

**史料**：`348456`、`348457`、`348461`、`348467`、`348478`、`348479`、`348490`、`348501`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348456 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348457 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348461 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348467 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348478 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348479 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348490 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348501 -->` 

**史观**：动手者创造历史（总纲第 10 条——动手者创造历史：以 Warren 提议在 MAINTAINERS 增标记使维护者能声明抄送偏好、Rostedt 自荐连任 TAB 并陈具体工具贡献为分析单位）；苦难不值得被提倡（总纲第 14 条——苦难不值得被提倡：Sharp 指报告者在哪报告很乱属社区议题，Greg KH 断言此类讨论留邮件更佳、KS 易沦为实现细节）
**辨析**：Rostedt 的自荐陈述（自 2001 年从事内核、维护 tracing 与 PREEMPT_RT、创 make localmodconfig 与 ktest.pl）为候选人自陈，属选举材料；Greg KH 的“kerneloops.org 能聚同 oops、bugzilla 不能合并须人工去重”为工具比较；Boyer 的“可爬刮 RHBZ 倒灌 LKML 但无益”为戏言。
**文献**：DSLXC-5281、DSLXC-5282、DSLXC-5286、DSLXC-5292、DSLXC-5303、DSLXC-5304、DSLXC-5315、DSLXC-5326（`ksummit-discuss.messages.348456`、`ksummit-discuss.messages.348457`、`ksummit-discuss.messages.348461`、`ksummit-discuss.messages.348467`、`ksummit-discuss.messages.348478`、`ksummit-discuss.messages.348479`、`ksummit-discuss.messages.348490`、`ksummit-discuss.messages.348501`，2014-05-13、2017-10-16、2017-10-16、2014-05-13、2014-05-02、2014-05-13、2014-05-13、2014-05-13），全文见 `raw_source.raw_json`

## 33.5 【Linux社区】树级补丁之痛与 PM 议题（6 例）

**要点（判定表逐字）**：Joe Perches 就树级语义补丁的排程与接受率发难，指出部分脚本补丁（如 API 变更）需整树应用，不能仅按子系统分别处理；Mark Brown 指 git 难以识别两处相同改动，经维护者树合入仍会冲突，主张改动尽量走维护者树以减少冲突；Jani Nikula 引 LWN 735468 称英特尔 drm 已有庞大 CI、合入前必过绿灯、反对绕过各自仓库的树级补丁，断言在 1500 万行分级代码库中搞 flag day 整树改动是错的；Jani Nikula 答 Joe Perches，坚称代码库规模相关（关乎子系统人数与痛苦），罕见离群案例不足改常程，易做整树改动反会鼓励添乱；Joe Perches 答 Jani，称代码库规模不特别相关、且并非总能不走整树改动；Rafael Wysocki 提设备电源管理 tech topic：runtime PM 与系统级 PM 交互（设备先于系统挂起处挂起、恢复时能否留挂起、能否复用 runtime 回调），指 PCI/ACPI 与无之两套不兼容、IP 块跨厂商共用后需通用法，并欲弃遗留 PM 回调

**史料**：`348458`、`348460`、`348464`、`348483`、`348503`、`348486`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348458 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348460 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348464 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348483 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348503 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348486 -->` 

**史观**：分离聚合是永恒规律（总纲第 4 条——分离聚合是永恒规律：整树脚本补丁与经维护者树合入之争，正是集中与分散两种相位的对撞）；经验优先（总纲第 9 条——经验优先：以英特尔 drm 庞大 CI 合入前必过绿灯、1500 万行分级代码库等实况为判据）
**辨析**：Nikula 的“在 1500 万行分级代码库中搞 flag day 整树改动是错的”为工程判断，Perches 的“代码库规模不特别相关、且并非总能不走整树改动”为反驳，两说对撞；Brown 的“git 难以识别两处相同改动，经维护者树合入仍会冲突”为机制说明；Wysocki 的“指 PCI/ACPI 与无之两套不兼容”为现状陈述。
**文献**：DSLXC-5283、DSLXC-5285、DSLXC-5289、DSLXC-5308、DSLXC-5328、DSLXC-5311（`ksummit-discuss.messages.348458`、`ksummit-discuss.messages.348460`、`ksummit-discuss.messages.348464`、`ksummit-discuss.messages.348483`、`ksummit-discuss.messages.348503`、`ksummit-discuss.messages.348486`，2017-10-16、2017-10-16、2017-10-17、2017-10-18、2017-10-18、2017-10-18），全文见 `raw_source.raw_json`

---
注：本文件由判定表程序化生成（5 块，覆盖 50/50 CAND，两遍计数核对通过）；要点逐字取自判定表“要点”列（主代理全读审读实录），史料锚与 CAND 一一对应，全文以 raw_source.raw_json 为准。
