# 49 【Linux社区】峰会议程TAB选举与端序标注

> 对应页面：ksummit-discuss p87（pk 348556-348605，2017-10 峰会排期与治理页 + 2014 档案信）
> 判定：50 CAND / 0 NV
> 编号：DSLXC-6079..6128 | claim 已入库（50/50，dslinux_claims.duckdb）

## 49.1 【Linux社区】峰会议程排期与 unconference 协调（13 例）

**要点（判定表逐字）**：Theodore Ts'o 发布 Kernel Summit 与 Maintainer Summit 完整议程（含 tracing ABI quicksand、printk 重设计、Restartable Sequences、回归追踪、Kselftest、内核安全等场次），标注 Linus 否决 ABI feature gates，另有 unconference 机制；Jonathan Corbet 更正议程——OSS Kernel Panel 实际在 14:55 而非 14:05，对文档分会时间提出修正；Theodore Ts'o 反问 Corbet 既称文档分会 14:05 有问题、是否因须早退接 Kernel Panel 连线，延续议程时间协调；Jonathan Corbet 确认正是须早退接 Kernel Panel 故 14:05 文档分会时间冲突，证成此前异议；Theodore Ts'o 提议将 Rafael 的电源管理分会提前至 14:05、14:55 留作 TBA，并指出其与 Kernel Panel（Vlastimil Babka、Arnd Bergmann、Thomas Gleixner、Narcisa Vasile）撞场；Rafael J. Wysocki 同意电源管理分会提前至 14:05；Megan Phillips 告知 unconference 房间为 Barcelona、紧邻 Athens 主会场，附 Linux Foundation 会议策划签名档；Randy Dunlap 以玩笑回应 Rafael——若改到周四便可占那 12:00 的空档，属议程闲笔；Rafael J. Wysocki 回 Randy——周四观众或更少，仍倾向提前；Theodore Ts'o 确认已将 Rafael 电源管理分会移至 14:05，请 Megan 在 sched.org 更新；Megan Phillips 回 Ted——房间已调整、sched 全更新，请其同步 Google 文档；Rafael J. Wysocki 指 sched 主页仍显示 14:55、点进才见 14:05，存在显示错位瑕疵；Greg KH 问维护者峰会（周四）所在房间

**史料**：`348558`、`348559`、`348560`、`348561`、`348562`、`348563`、`348564`、`348565`、`348566`、`348570`、`348571`、`348572`、`348602`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348558 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348559 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348560 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348561 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348562 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348563 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348564 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348565 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348566 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348570 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348571 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348572 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348602 -->` 

**史观**：动手者创造历史（总纲第 10 条——动手者创造历史：以 Theodore Ts'o 的议程发布与 14:05 改排、Megan Phillips 的房间与 sched.org 更新、Rafael J. Wysocki 的显示错位指摘为分析单位）；历史地理塑造思想土壤（总纲第 20 条——历史地理塑造思想土壤：Megan Phillips 告知 unconference 房间为 Barcelona、紧邻 Athens 主会场，会场空间安排直接约束议程可达性）
**辨析**：Jonathan Corbet 的“更正议程——OSS Kernel Panel 实际在 14:55 而非 14:05”与 Theodore Ts'o 的“反问是否因须早退接 Kernel Panel 连线”往复后经 Corbet 确认，属事实层澄清；Rafael 的“指 sched 主页仍显示 14:55、点进才见 14:05，存在显示错位瑕疵”为可核之工具实况；Randy Dunlap 的“以玩笑回应 Rafael——若改到周四便可占那 12:00 的空档”与 Rafael 的“周四观众或更少，仍倾向提前”为议程闲笔，非史家判断。本块为事务性协调，未涉裁断。
**文献**：DSLXC-6081、DSLXC-6082、DSLXC-6083、DSLXC-6084、DSLXC-6085、DSLXC-6086、DSLXC-6087、DSLXC-6088、DSLXC-6089、DSLXC-6093、DSLXC-6094、DSLXC-6095、DSLXC-6125（`ksummit-discuss.messages.348558`、`ksummit-discuss.messages.348559`、`ksummit-discuss.messages.348560`、`ksummit-discuss.messages.348561`、`ksummit-discuss.messages.348562`、`ksummit-discuss.messages.348563`、`ksummit-discuss.messages.348564`、`ksummit-discuss.messages.348565`、`ksummit-discuss.messages.348566`、`ksummit-discuss.messages.348570`、`ksummit-discuss.messages.348571`、`ksummit-discuss.messages.348572`、`ksummit-discuss.messages.348602`，2017-10-23、2017-10-23、2017-10-23、2017-10-23、2017-10-23、2017-10-23、2017-10-23、2017-10-23、2017-10-23、2017-10-24、2017-10-24、2017-10-24、2017-10-25），全文见 `raw_source.raw_json`

## 49.2 【Linux社区】TAB 选举与治理（3 例）

**要点（判定表逐字）**：Frank Rowand 就 TAB 选举追问——要求公布任期将满与留任成员以利选民判断，并询 TAB 近年纪要去向（wiki 仅至 2010），点名现任五名未换届者；Steven Rostedt 提醒当日（10-25）TAB 选举于 Athens 厅投票、五席待选，附候选人文档链接；H. Peter Anvin 公布 2017 TAB 选举结果——73 票、前五 Rostedt 58、Corbet 57、Greg KH 57、Tim Bird 39、Ted Ts'o 37，计票由 SDAPS 开源项目加自定义脚本自动完成并经人工复核

**史料**：`348569`、`348580`、`348605`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348569 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348580 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348605 -->` 

**史观**：不存在进步，只有权力再分配（总纲第 3 条——不存在进步，只有权力再分配：Frank Rowand 的“要求公布任期将满与留任成员以利选民判断，并询 TAB 近年纪要去向（wiki 仅至 2010）”正是席位与信息权的再分配之争）；本体论上各方平等（总纲第 8 条——本体论上各方平等：H. Peter Anvin 公布的 2017 TAB 选举结果（73 票、前五 Rostedt 58、Corbet 57、Greg KH 57、Tim Bird 39、Ted Ts'o 37）为可核之量化实况，与 Frank Rowand 的程序性质问并置，未替任一方定论）
**辨析**：Frank Rowand 的“点名现任五名未换届者”为其追问之实；Steven Rostedt 的“提醒当日（10-25）TAB 选举于 Athens 厅投票、五席待选，附候选人文档链接”为程序通告；H. Peter Anvin 的“计票由 SDAPS 开源项目加自定义脚本自动完成并经人工复核”为计票方法自陈。本块为选举留痕，与第 35 号文件的选举结果互为跨文件互证。
**文献**：DSLXC-6092、DSLXC-6103、DSLXC-6128（`ksummit-discuss.messages.348569`、`ksummit-discuss.messages.348580`、`ksummit-discuss.messages.348605`，2017-10-24、2017-10-25、2017-10-25），全文见 `raw_source.raw_json`

## 49.3 【Linux社区】跨树改动 tree-wide changes 大讨论（12 例）

**要点（判定表逐字）**：Kees Cook 由 trivial patches 引申——提议设 tree-wide changes 专场，述及做定时器转换时频踩跨树改动坑，盼理顺跨多子系统开发；Joe Perches 附和——跨树改动像陈年林堡干酪、亟待讨论，直言当前没有好的跨树改动办法；Kees Cook 列八点补丁流工作流痛点——区分 ack 与 apply 的标注、200+ 系列投递难、MAINTAINERS 增 U: 上游条目与批量上限、依赖补丁沉默阻塞、外部树改动预期，倡议补 TreewideChanges 文档；Julia Lawall 述无个人树、依赖收件维护者收补丁，补问系列如何切分（按文件或按维护者），指 MAINTAINERS 的 T: 条目不全；Julia Lawall 续与 Joe Perches——皆只发一次系列、按二级目录（drivers/net 三级）切分树级补丁，认同设树级维护者更利微不足道改动；Martin K. Petersen 谈审阅负担——批大小 10 至 15 为宜、依赖他人审阅、patchwork 队列久置即无人理、须重发并附完整 cover letter；Frank Rowand 补正——发往列表的补丁不只给维护者、亦供他人审阅，按周分批反令本周有空者错过；Kees Cook 附和 Martin——盼 patchwork 捕获 cover letter 且能整系列成包一键选取，而非逐补丁点击；Martin K. Petersen 回 Kees——整系列成包功能在 pipeline 中、盼尽早落地；Mark Brown 谈 MAINTAINERS 匹配——用全部匹配条目多能找到上游（arm-soc 例外未入 MAINTAINERS），外部树改动宜先协调；Joe Perches 续 Julia——树级补丁按二级目录切分、重叠归属时 MAINTAINERS 既不全亦不完整；Laurent Pinchart 述收系列补丁时常误判上游树、每封询 ack 与否浪费带宽，主张文档化树级改动默认上游路径

**史料**：`348573`、`348574`、`348575`、`348576`、`348577`、`348579`、`348581`、`348582`、`348583`、`348584`、`348585`、`348586`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348573 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348574 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348575 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348576 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348577 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348579 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348581 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348582 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348583 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348584 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348585 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348586 -->` 

**史观**：分离聚合是永恒规律（总纲第 4 条——分离聚合是永恒规律：Julia Lawall 的“按二级目录（drivers/net 三级）切分树级补丁”、Joe Perches 的“重叠归属时 MAINTAINERS 既不全亦不完整”、Laurent Pinchart 的“主张文档化树级改动默认上游路径”并置，正是跨树改动在子系统边界上的分合相位）；经验优先（总纲第 9 条——经验优先：以 Kees Cook 的“做定时器转换时频踩跨树改动坑”、Martin K. Petersen 的“批大小 10 至 15 为宜、patchwork 队列久置即无人理”为判据）
**辨析**：Joe Perches 的“跨树改动像陈年林堡干酪、亟待讨论，直言当前没有好的跨树改动办法”为其判断；Kees Cook 的“列八点补丁流工作流痛点，倡议补 TreewideChanges 文档”为提案；Frank Rowand 的“补正——发往列表的补丁不只给维护者、亦供他人审阅，按周分批反令本周有空者错过”为对 Martin 分批之议的反驳；Mark Brown 的“用全部匹配条目多能找到上游（arm-soc 例外未入 MAINTAINERS）”为可核之实况。各说并置，未见决议。
**文献**：DSLXC-6096、DSLXC-6097、DSLXC-6098、DSLXC-6099、DSLXC-6100、DSLXC-6102、DSLXC-6104、DSLXC-6105、DSLXC-6106、DSLXC-6107、DSLXC-6108、DSLXC-6109（`ksummit-discuss.messages.348573`、`ksummit-discuss.messages.348574`、`ksummit-discuss.messages.348575`、`ksummit-discuss.messages.348576`、`ksummit-discuss.messages.348577`、`ksummit-discuss.messages.348579`、`ksummit-discuss.messages.348581`、`ksummit-discuss.messages.348582`、`ksummit-discuss.messages.348583`、`ksummit-discuss.messages.348584`、`ksummit-discuss.messages.348585`、`ksummit-discuss.messages.348586`，2017-10-24、2017-10-24、2017-10-25、2017-10-25、2017-10-25、2017-10-25、2017-10-25、2017-10-25、2017-10-25、2017-10-25、2017-10-25、2017-10-25），全文见 `raw_source.raw_json`

## 49.4 【Linux社区】设备端序标注与 sparse/GCC 议题（13 例）

**要点（判定表逐字）**：Bart Van Assche 提技术议题——倡以 sparse 校验 __be32 等端序标注、借 zero-day 测试基础设施督促驱动作者关注端序，请列入议程；Greg KH 回 Bart——子系统维护者本应知晓、sparse 易跑，遇无视者请直接报维护者并提补丁；Bart Van Assche 回 Greg——qla2xxx、infiniband nes 等端序标注极难改、仅原作者能清，举单变量混存 cpu 与 big endian、固件文档缺失或 NDA 三难；Greg KH 回 Bart——作者不修则于 Kconfig 标记禁在大端构建，端序问题二十年如一日，且维护者峰会已过半、日程已满；Mark Brown 补——16:15 尚有一 TBA 空档，可排入端序议题；Leon Romanovsky 论端序——不涉作者难清、非活跃驱动尤不可行，须作者合作；Greg KH 回 Leon——sparse 端序支持已逾十年、作者不做则禁该端构建，非新问题；Bart Van Assche 澄清——关切的是固件寄存器与 CPU 端序不同、须转换的驱动，端序标注即便单端亦有益；Alexey Dobriyan 论 sparse 之弊——非编译强制、不破编译，举 typedef 包装 __le32 之巧；Leon Romanovsky 回 Greg——今昔差异在工具演进，并指尚有一开放 TBD 空档；Theodore Ts'o 准 Bart 端序议题入 16:15 空档、已写入议程表；David Woodhouse 忆 JFFS2 早年手做端序包装、盼编译器原生支持大小端整数（已半途于 __builtin_bswap32），自动加载存储转换极有用；Josh Triplett 引 GCC bugzilla 59852——提议将 sparse 的 __attribute__((bitwise)) 落地 GCC，开发者乐见、待有人写补丁

**史料**：`348587`、`348588`、`348591`、`348592`、`348593`、`348594`、`348595`、`348596`、`348597`、`348598`、`348599`、`348600`、`348604`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348587 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348588 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348591 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348592 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348593 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348594 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348595 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348596 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348597 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348598 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348599 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348600 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348604 -->` 

**史观**：知识注定过时（总纲第 22 条——知识注定过时：David Woodhouse 的“忆 JFFS2 早年手做端序包装、盼编译器原生支持大小端整数”、Josh Triplett 的“引 GCC bugzilla 59852，提议将 sparse 的 __attribute__((bitwise)) 落地 GCC”并置，正是工具知识在代际间迁移之议）；本体论上各方平等（总纲第 8 条——本体论上各方平等：Greg KH 的“子系统维护者本应知晓、sparse 易跑，遇无视者请直接报维护者并提补丁”“作者不修则于 Kconfig 标记禁在大端构建”与 Bart Van Assche 的“qla2xxx、infiniband nes 等端序标注极难改、仅原作者能清，举单变量混存 cpu 与 big endian、固件文档缺失或 NDA 三难”对撞，未替任一方定论）
**辨析**：Bart 的“澄清——关切的是固件寄存器与 CPU 端序不同、须转换的驱动，端序标注即便单端亦有益”为其自我限界；Alexey Dobriyan 的“论 sparse 之弊——非编译强制、不破编译，举 typedef 包装 __le32 之巧”为技术性质疑；Leon Romanovsky 的“不涉作者难清、非活跃驱动尤不可行，须作者合作”“今昔差异在工具演进”为其立场之陈；Theodore Ts'o 的“准 Bart 端序议题入 16:15 空档、已写入议程表”为议程裁决之留痕。
**文献**：DSLXC-6110、DSLXC-6111、DSLXC-6114、DSLXC-6115、DSLXC-6116、DSLXC-6117、DSLXC-6118、DSLXC-6119、DSLXC-6120、DSLXC-6121、DSLXC-6122、DSLXC-6123、DSLXC-6127（`ksummit-discuss.messages.348587`、`ksummit-discuss.messages.348588`、`ksummit-discuss.messages.348591`、`ksummit-discuss.messages.348592`、`ksummit-discuss.messages.348593`、`ksummit-discuss.messages.348594`、`ksummit-discuss.messages.348595`、`ksummit-discuss.messages.348596`、`ksummit-discuss.messages.348597`、`ksummit-discuss.messages.348598`、`ksummit-discuss.messages.348599`、`ksummit-discuss.messages.348600`、`ksummit-discuss.messages.348604`，2017-10-25、2017-10-25、2017-10-25、2017-10-25、2017-10-25、2017-10-25、2017-10-25、2017-10-25、2017-10-25、2017-10-25、2017-10-25、2017-10-25、2017-10-25），全文见 `raw_source.raw_json`

## 49.5 【Linux社区】Devicetree 工作坊（2 例）

**要点（判定表逐字）**：Boris Brezillon 虽不出席 Devicetree 工作坊，但全文转引 Grant Likely 草案日程（DT YAML 编码、schema 两方案、运行时内存、overlay 维护、ABI 稳定性、EBBR 等），信息量极高；Maxime Ripard 代 Boris 在 Devicetree 工作坊谈 foreign bindings 议题——其与 Boris 近期皆遇此问题，愿顶上

**史料**：`348568`、`348603`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348568 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348603 -->` 

**史观**：历史地理塑造思想土壤（总纲第 20 条——历史地理塑造思想土壤：Devicetree 工作坊的草案日程（DT YAML 编码、schema 两方案、运行时内存、overlay 维护、ABI 稳定性、EBBR）正见嵌入式硬件生态对技术议题的塑造）；本体论上各方平等（总纲第 8 条——本体论上各方平等：Boris Brezillon 的“虽不出席但全文转引 Grant Likely 草案日程”与 Maxime Ripard 的“代 Boris 谈 foreign bindings 议题——其与 Boris 近期皆遇此问题，愿顶上”并置，未替任一方定论）
**辨析**：本块仅两例，为同一工作坊的两种参与方式（转引与代讲）；Boris 的“信息量极高”为其对草案的评价；Maxime 的“愿顶上”为其自陈。未涉裁断。
**文献**：DSLXC-6091、DSLXC-6126（`ksummit-discuss.messages.348568`、`ksummit-discuss.messages.348603`，2017-10-24、2017-10-25），全文见 `raw_source.raw_json`

## 49.6 【Linux社区】文档分会提议（1 例）

**要点（判定表逐字）**：Mauro Carvalho Chehab 提出文档分会——按受众分群、驱动文档按子系统归并（media 曾独将 uAPI 放进 DocBook），推动 Documentation/*.txt 转 ReST、考虑 checkpatch.pl 调 Sphinx 校验并愿清理 USB 与核心驱动 API 文档

**史料**：`348557`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348557 -->` 

**史观**：知识注定过时（总纲第 22 条——知识注定过时：Mauro 的“推动 Documentation/*.txt 转 ReST、考虑 checkpatch.pl 调 Sphinx 校验并愿清理 USB 与核心驱动 API 文档”，正是文档知识随代码演进须重整之证）；分离聚合是永恒规律（总纲第 4 条——分离聚合是永恒规律：Mauro 的“按受众分群、驱动文档按子系统归并（media 曾独将 uAPI 放进 DocBook）”，正是文档归属的聚合与分离）
**辨析**：本块仅一例，为 Mauro Carvalho Chehab 的单方提案，本页未见他人回应或决议；其“愿清理 USB 与核心驱动 API 文档”为当事人自陈。
**文献**：DSLXC-6080（`ksummit-discuss.messages.348557`，2017-10-23），全文见 `raw_source.raw_json`

## 49.7 【Linux社区】KS2014 档案六封（6 例）

**要点（判定表逐字）**：Daniel Vetter（2014 档案）论设备错误隔离与上报——IOMMU 故障风暴后重新启用、i915 在风暴时阻断命令提交以减损，主张驱动与 IOMMU 子系统出错时协调、优先损伤控制而非彻底隔离故障设备；Levente Kurusa（2014 档案）就 QR oops 议题延展至通用错误上报——建议 oops 超 X 次自动送维护者、为 RC 增统计、清理 bugzilla 与 oops.kernel.org，并质疑 QR 码占用屏幕是否值得；Josh Triplett（2014 档案）论内核瘦身——赞同 Tim Bird 自动化裁剪、谈 LTO、DT 静态化常量传播、命令行列全局变量转 const、自动 syscall 消除，并考虑新设 tiny 树；Olof Johansson（2014 档案）提技术议题 Driver model／resources、ACPI、DT——Intel 平台 ACPI 与嵌入式模型错配，拟建统一资源管理 API、给驱动加 ACPI 与 DT 双探针，点名 Darren Hart、Rafael、Grant Likely、Greg、David Woodhouse 共室商议；Jiri Kosina（2014 档案）就维护者指引议题——赞 Josh 在 git.kernel.org 加 git 钩子自动通知补丁被合并，愿以分支名正则触发邮件，盼 kernel.org 提供；Teodora Baluta（2014 档案）续 QR oops——同遇 oops.kernel.org 503、建议加 REST API 与服务器端聚合分析、愿牵头讨论并已有原型与人员（Levente 与其）

**史料**：`348556`、`348567`、`348578`、`348589`、`348590`、`348601`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348556 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348567 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348578 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348589 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348590 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348601 -->` 

**史观**：一切真历史都是古代史（总纲第 1 条——一切真历史都是古代史：2014 年的设备错误隔离、QR oops、内核瘦身、driver model/resources、维护者指引五线档案被 2017 年峰会筹备重提，正见旧议题的当代性）；经验优先（总纲第 9 条——经验优先：以 Levente Kurusa 的“同遇 oops.kernel.org 503”、Daniel Vetter 的“i915 在风暴时阻断命令提交以减损”为判据）
**辨析**：Daniel Vetter 的“主张驱动与 IOMMU 子系统出错时协调、优先损伤控制而非彻底隔离故障设备”为其设计判词；Levente Kurusa 的“建议 oops 超 X 次自动送维护者、为 RC 增统计、清理 bugzilla 与 oops.kernel.org，并质疑 QR 码占用屏幕是否值得”为提案兼质疑；Olof Johansson 的“拟建统一资源管理 API、给驱动加 ACPI 与 DT 双探针”为其设计主张；Jiri Kosina 的“愿以分支名正则触发邮件，盼 kernel.org 提供”为工具诉求；Teodora Baluta 的“建议加 REST API 与服务器端聚合分析、愿牵头讨论并已有原型与人员”为当事人自陈。本块六封皆 2014 年档案，与 2017 年主线不同期，属跨期并置。
**文献**：DSLXC-6079、DSLXC-6090、DSLXC-6101、DSLXC-6112、DSLXC-6113、DSLXC-6124（`ksummit-discuss.messages.348556`、`ksummit-discuss.messages.348567`、`ksummit-discuss.messages.348578`、`ksummit-discuss.messages.348589`、`ksummit-discuss.messages.348590`、`ksummit-discuss.messages.348601`，2014-05-13、2014-05-13、2014-05-13、2014-05-02、2014-05-13、2014-05-13），全文见 `raw_source.raw_json`

---
注：本文件由判定表程序化生成（49.1-49.7 共 7 块，覆盖 50/50 CAND，两遍计数核对通过）；要点逐字取自判定表“要点”列（并行会话全读审读实录，主代理补派管线），史料锚与 CAND 一一对应，全文以 raw_source.raw_json 为准。
