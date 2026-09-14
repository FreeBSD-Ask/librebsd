# 195 【Linux社区】ext4弃bh与unsafe语义

> 来源：ksummit 独有 p59（50 封全读，2021-04 至 2026-08：Ts'o 一手详述 ext4 弃用 buffer_heads 三大动因及 folio 迁移破坏 bh_offset 回归案例兼论全树改动对 LTS 自动回移的阻碍；Ribalda 与 Pinchart 就 ISP 归 V4L2 还是 DRM 激辩含九成以上摄像头市场依赖树外驱动关键数据；Linus 对 unsafe 语义权威阐述程序员冒险与编译器冒险之别并与反 UB 优化立场构成 Rust 政策奠基性表述；Carpenter 复盘多起 AI 参与补丁真实案例含 grep FIXME 令 AI 实现与 AI 模糊测试戳穿不完整安全修复；Rust 未定义行为与 AI 代码审查双封、malloc 提案双封）
> 判定：45 CAND / 5 NV。主题分布：列表版面治理 1、缓冲缓存与大folio 1、THE REST收件分流 1、无符号警告之争 1、C++可行性论据 1、malloc提案 2、AI代码审查 2、旧文件系统用户态化 2、内核文档工具 1、Rust静态引用语义 1、Bugzilla改革 1、linux-next流程 2、C语言安全 1、Rust弱引用语义 1、UMN假补丁事件 1、项目延续文档 1、Link尾注替换 1、Rust文件布局 1、Rust抽象层生成 1、安全代码质检门槛 1、维护者峰会存废 1、TAB选举安排 1、Rust未定义行为 2、Rust补丁测试 1、安全披露渠道 1、ISP驱动框架之争 1、信任网重建 1、Folios之争 1、Sphinx构建依赖 1、UALink驱动布局 1、设备树绑定ABI 1、AI标注标签 1、文档构建性能 1、加速器用户态要求 1、AI政策讨论 1、缓冲缓存退役 1、回归追踪 1、评审激励机制 1、设备直通之争 1、补丁发送工具 1。

## 195.1 列表版面治理

- **要点**：Ryabitsev 叫停峰会筹备线程中的防疫药物争论，警告将在其可控基础设施上启用过滤屏蔽，体现新版 ksummit 列表早期的版面整顿立场。
- **史料**：`ksummit.messages.9186`（Konstantin Ryabitsev，2021-06-15）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9186 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以列表过滤屏蔽这一具体基础设施手段为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：防疫争论与版面治理的边界之争）
- **辨析**：本块系 Konstantin Ryabitsev 的单方叫停，属基础设施方的一手处置；“将在其可控基础设施上启用过滤屏蔽”为可执行的运维决定。
- **文献**：DSLXC-11007（`ksummit.messages.9186`，2021-06-15），全文见 `raw_source.raw_json`

## 195.2 缓冲缓存与大folio

- **要点**：Linus 评 Wilcox 设想：缓冲缓存理论上可为 256kB 大 folio 建非均匀 buffer_head，但从未实现与测试，也缺少相应 helper 函数。
- **史料**：`ksummit.messages.9190`（Linus Torvalds，2023-09-19）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9190 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以非均匀 buffer_head 与 helper 函数等具体实现条件为分析单位）；知识注定过时（总纲第 22 条——知识注定过时：256kB 大 folio 的缓冲缓存设想从未实现与测试）
- **辨析**：本块系 Linus Torvalds 对 Wilcox 设想的评断；“从未实现与测试”为对实现现状的陈述，非对设想价值的否定。
- **文献**：DSLXC-11008（`ksummit.messages.9190`，2023-09-19），全文见 `raw_source.raw_json`

## 195.3 THE REST收件分流

- **要点**：Bonzini 质疑把“THE REST”改投 patches@ 的效果：大量 LKML 流量实为 git-send-email 默认配置所致，patches@ 现仅稳定队列在用。
- **史料**：`ksummit.messages.9191`（Paolo Bonzini，2023-11-07）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9191 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“大量 LKML 流量实为 git-send-email 默认配置所致”这一实际归因为判据）；动手者叙事（总纲第 10 条——动手者创造历史：以 patches@ 现仅稳定队列在用这一实际状况为分析单位）
- **辨析**：本块系 Paolo Bonzini 的质疑；“patches@ 现仅稳定队列在用”为可核的列表实况，其分流效果之疑本页未见答复。
- **文献**：DSLXC-11009（`ksummit.messages.9191`，2023-11-07），全文见 `raw_source.raw_json`

## 195.4 无符号警告之争

- **要点**：Linus 强硬主张内核必须禁用“无符号小于 0”警告：该警告催生错误强转与删检查等真 bug，并非安全网，称此立场不可谈判。
- **史料**：`ksummit.messages.9193`（Linus Torvalds，2025-02-21）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9193 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“该警告催生错误强转与删检查等真 bug”这一实际后果为判据）；多方平等（总纲第 8 条——本体论上各方平等：警告作为安全网与作为 bug 来源两说并置）
- **辨析**：本块系 Linus Torvalds 的强硬定调；“此立场不可谈判”为明确的维护者终局表述，属本页高证据等级。
- **文献**：DSLXC-11010（`ksummit.messages.9193`，2025-02-21），全文见 `raw_source.raw_json`

## 195.5 C++可行性论据

- **要点**：Dobriyan 以实测否定 C++ 路线：g++ 要求 C99 初始化器按声明顺序且不支持 x86 的 __seg_gs；又指与 C 不源码兼容者（含 Rust）均非选项。
- **史料**：`ksummit.messages.9194`（Alexey Dobriyan，2025-02-20）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9194 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 g++ 对 C99 初始化器顺序、__seg_gs 支持等可实测的编译行为为分析单位）；经验优先（总纲第 9 条——经验优先：以实测否定 C++ 路线为判据）
- **辨析**：本块系 Alexey Dobriyan 的实测反证；“与 C 不源码兼容者（含 Rust）均非选项”为其推论，落书须与后续 Rust 入树事实对照。
- **文献**：DSLXC-11011（`ksummit.messages.9194`，2025-02-20），全文见 `raw_source.raw_json`

## 195.6 malloc提案

- **要点**：Ojeda 回击 hpa“剔除 Rust”威胁：Rust 已支持可插拔分配器，实现 malloc 类接口无障碍，是 Rust 政策之争中的事实澄清。Wilcox 澄清提案是实现 1970 年代标准接口而非立新标准，未来或删 kvmalloc；指出 kzalloc_obj 配 GFP_NOWAIT 时小分配仍会失败的张力。
- **史料**：`ksummit.messages.9196`（Miguel Ojeda，2026-07-09）、`ksummit.messages.9311`（Matthew Wilcox，2026-06-29）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9196 -->` `<!-- ROW_MINE: ksummit.messages.9311 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以可插拔分配器、malloc 类接口、kzalloc_obj 配 GFP_NOWAIT 等具体机制为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：事实澄清与提案澄清两方并置）
- **辨析**：Ojeda 的“Rust 已支持可插拔分配器”为可核事实；“剔除 Rust”之威胁系转述 hpa，落书须标明；Wilcox 的“未来或删 kvmalloc”为意向。
- **文献**：DSLXC-11012、DSLXC-11035（`ksummit.messages.9196`、`ksummit.messages.9311`，2026-07-09、2026-06-29），全文见 `raw_source.raw_json`

## 195.7 AI代码审查

- **要点**：Brown 赞同 Linus 对 AI 审查报告摩擦的担忧，但主张将 AI 发现集中建库，类比 Coverity 模式，并提议挖掘重复报告模式而非散落各评审。Carpenter 复盘 CVE 审读实例：有人 grep FIXME 后令 AI 实现即冒充溢出修复，AI 模糊测试发现安全补丁不完整，呼吁提交说明写明 AI 用法与流程。
- **史料**：`ksummit.messages.9198`（Mark Brown，2026-07-18）、`ksummit.messages.9230`（Dan Carpenter，2026-08-08）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9198 -->` `<!-- ROW_MINE: ksummit.messages.9230 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“集中建库类比 Coverity 模式、挖掘重复报告模式”等具体方案为分析单位）；经验优先（总纲第 9 条——经验优先：以“有人 grep FIXME 后令 AI 实现即冒充溢出修复”等真实案例为判据）
- **辨析**：Brown 的 Coverity 类比为设计建议；Carpenter 的两例（AI 模糊测试发现安全补丁不完整）为可核的一手复盘，属本页 AI 审查议题的关键证据。
- **文献**：DSLXC-11013、DSLXC-11020（`ksummit.messages.9198`、`ksummit.messages.9230`，2026-07-18、2026-08-08），全文见 `raw_source.raw_json`

## 195.8 旧文件系统用户态化

- **要点**：Overstreet 提出以 shim 层把旧文件系统整体搬入用户态 FUSE 运行，bcachefs 已实现约九成代码量用户态化，可免内核重构破坏并收窄安全面。Biederman 主张以 libguestfs 为起点运行旧文件系统：其已带 FUSE 支持并随主流发行版发布，可在 qemu 中跑内核挂载，关键在做到零摩擦可用。
- **史料**：`ksummit.messages.9205`（Kent Overstreet，2023-09-10）、`ksummit.messages.9213`（Eric W. Biederman，2023-09-26）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9205 -->` `<!-- ROW_MINE: ksummit.messages.9213 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 shim 层用户态 FUSE、libguestfs 起点等具体方案为分析单位）；经验优先（总纲第 9 条——经验优先：以“bcachefs 已实现约九成代码量用户态化”与“libguestfs 已带 FUSE 支持并随主流发行版发布”为判据）
- **辨析**：两条为并行方案，均属倡议；“可免内核重构破坏并收窄安全面”与“关键在做到零摩擦可用”分别为两方目标表述，本页未见采纳。
- **文献**：DSLXC-11014、DSLXC-11016（`ksummit.messages.9205`、`ksummit.messages.9213`，2023-09-10、2023-09-26），全文见 `raw_source.raw_json`

## 195.9 内核文档工具

- **要点**：Mauro 介绍 kernel-doc 已可全树解析，实测 make mandocs 约 44 秒、报数千警告，支持 Nikula 提议的 --lint-rst 检查，媒体 CI 以 W=1 零警告为目标。
- **史料**：`ksummit.messages.9212`（Mauro Carvalho Chehab，2025-09-01）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9212 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“make mandocs 约 44 秒、报数千警告”这一实测为判据）；动手者叙事（总纲第 10 条——动手者创造历史：以 --lint-rst 检查与媒体 CI 以 W=1 零警告为目标等具体机制为分析单位）
- **辨析**：本块系 Mauro Carvalho Chehab 的工具进展汇报；“数千警告”为可复算的实测口径。
- **文献**：DSLXC-11015（`ksummit.messages.9212`，2025-09-01），全文见 `raw_source.raw_json`

## 195.10 Rust静态引用语义

- **要点**：Ventura Jack 引 Rust 2024 版文档指出全局可变 static 引用即使在 unsafe 中也被强烈劝阻，回应 Linus“读全局标志还要 unsafe”的批评。
- **史料**：`ksummit.messages.9217`（Ventura Jack，2025-03-06）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9217 -->`
- **史观**：知识注定过时（总纲第 22 条——知识注定过时：Rust 2024 版文档对全局可变 static 引用的强烈劝阻）；多方平等（总纲第 8 条——本体论上各方平等：文档规定与“读全局标志还要 unsafe”之批评的对话）
- **辨析**：本块系 Ventura Jack 引文档的回应，属对 Linus 批评的直接答复；“即使 unsafe 中也被强烈劝阻”为文档规定，非实现现状。
- **文献**：DSLXC-11017（`ksummit.messages.9217`，2025-03-06），全文见 `raw_source.raw_json`

## 195.11 Bugzilla改革

- **要点**：Leemhuis 澄清改革后的报告路径为按子系统邮件维护者，承认缺一级支持组并有意日后组建，但当前优先级较低。
- **史料**：`ksummit.messages.9220`（Thorsten Leemhuis，2022-10-01）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9220 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“按子系统邮件维护者”的报告路径为分析单位）；经验优先（总纲第 9 条——经验优先：以“承认缺一级支持组并有意日后组建”这一实际自评为判据）
- **辨析**：本块系 Thorsten Leemhuis 的澄清与自认；“当前优先级较低”表明该项为搁置中的待办。
- **文献**：DSLXC-11018（`ksummit.messages.9220`，2022-10-01），全文见 `raw_source.raw_json`

## 195.12 linux-next流程

- **要点**：Brown 指出子树修复若未进 -next，bug 会持续暴露至 PR 合入为止，子树孵化期与 PR 处理延迟都直接拉长问题在 -next 的可见时间。Roeck 指出 linux-next 及其 pending-fixes 分支的构建与测试失败基本无人理会，质疑以其作为 PR 健康信号的实际价值。
- **史料**：`ksummit.messages.9225`（Mark Brown，2025-09-11）、`ksummit.messages.9345`（Guenter Roeck，2024-10-23）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9225 -->` `<!-- ROW_MINE: ksummit.messages.9345 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“linux-next 及其 pending-fixes 分支的构建与测试失败基本无人理会”这一实际状况为判据）；动手者叙事（总纲第 10 条——动手者创造历史：以子树孵化期与 PR 处理延迟对可见时间的影响为分析单位）
- **辨析**：Brown 的时序分析为机制推断；Roeck 的“质疑以其作为 PR 健康信号的实际价值”为对既有做法的否定，两者本页未见回应。
- **文献**：DSLXC-11019、DSLXC-11043（`ksummit.messages.9225`、`ksummit.messages.9345`，2025-09-11、2024-10-23），全文见 `raw_source.raw_json`

## 195.13 C语言安全

- **要点**：Uecker 指出 C 安全化投入被低估：他业余修 GCC 无人跟进、内核未参与 ISO C 标准化，认为 C 有大量低成本安全改进空间且可建内存安全子集。
- **史料**：`ksummit.messages.9235`（Martin Uecker，2025-02-20）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9235 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“他业余修 GCC 无人跟进、内核未参与 ISO C 标准化”这一实际状况为判据）；多方平等（总纲第 8 条——本体论上各方平等：C 安全化投入被低估与可建内存安全子集的主张并置）
- **辨析**：本块系 Martin Uecker 的单方论断；“有大量低成本安全改进空间”为其估计，未附量化清单。
- **文献**：DSLXC-11021（`ksummit.messages.9235`，2025-02-20），全文见 `raw_source.raw_json`

## 195.14 Rust弱引用语义

- **要点**：Ojeda 以代码示例向 Geert 解释 Weak::upgrade 返回 Option：对象不存在时调用方根本无从访问成员，展示 Rust 所有权模型的安全保证。
- **史料**：`ksummit.messages.9238`（Miguel Ojeda，2021-07-08）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9238 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 Weak::upgrade 返回 Option 的代码示例为分析单位）；经验优先（总纲第 9 条——经验优先：以“对象不存在时调用方根本无从访问成员”这一语言层保证为判据）
- **辨析**：本块系 Miguel Ojeda 对 Geert 的解释，属语言机制的一手说明，非政策表述。
- **文献**：DSLXC-11022（`ksummit.messages.9238`，2021-07-08），全文见 `raw_source.raw_json`

## 195.15 UMN假补丁事件

- **要点**：Figa 赞同 Hellwig 对明尼苏达大学实验的评价，称评审量不足是多年顽疾，UMN 本应引入社区监督并负责事后清理，其否认态度更令人担忧。
- **史料**：`ksummit.messages.9249`（Tomasz Figa，2021-04-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9249 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：对 UMN 实验的批评与“本应引入社区监督并负责事后清理”的要求并置）；经验优先（总纲第 9 条——经验优先：以“评审量不足是多年顽疾”这一经验判断为判据）
- **辨析**：本块系 Tomasz Figa 的附议与批评；“其否认态度更令人担忧”为对当事人态度的评价，非事实陈述。
- **文献**：DSLXC-11023（`ksummit.messages.9249`，2021-04-22），全文见 `raw_source.raw_json`

## 195.16 项目延续文档

- **要点**：Linus 表示将绕过文档树亲自直接提交 Dan Williams 的“项目延续”流程文档，后续修订再走常规途径，属治理事件的当事人表态。
- **史料**：`ksummit.messages.9267`（Linus Torvalds，2026-01-24）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9267 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“绕过文档树亲自直接提交”这一具体处置为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：常规途径与例外处置被明确区分）
- **辨析**：本块系 Linus Torvalds 的一手表态，属治理事件的当事人记录；“后续修订再走常规途径”为程序性说明。
- **文献**：DSLXC-11024（`ksummit.messages.9267`，2026-01-24），全文见 `raw_source.raw_json`

## 195.17 Link尾注替换

- **要点**：Bottomley 反对集中 git notes 树承载子系统元数据：notes 设计上不适共享、需过滤且易污染本地用途，主张全局重要信息应写入提交树。
- **史料**：`ksummit.messages.9269`（James Bottomley，2025-10-15）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9269 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 git notes 的共享与过滤特性这一工具约束为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：集中 notes 树与写入提交树两说并置）
- **辨析**：本块系 James Bottomley 的反对意见；“notes 设计上不适共享、需过滤且易污染本地用途”为其技术判断。
- **文献**：DSLXC-11025（`ksummit.messages.9269`，2025-10-15），全文见 `raw_source.raw_json`

## 195.18 Rust文件布局

- **要点**：Ojeda 回应 Lunn 关于文件搬移影响稳定树回移的顾虑：可先定好路径不再搬，或宣布 Rust 支持前两三个版本不回移，给树内成熟留时间。
- **史料**：`ksummit.messages.9274`（Miguel Ojeda，2021-07-20）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9274 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“先定好路径不再搬”或“前两三个版本不回移”等具体折中为分析单位）；经验优先（总纲第 9 条——经验优先：以“给树内成熟留时间”这一工程考虑为判据）
- **辨析**：本块系 Miguel Ojeda 的回应与折中方案；“宣布 Rust 支持前两三个版本不回移”为提案，非既成政策。
- **文献**：DSLXC-11026（`ksummit.messages.9274`，2021-07-20），全文见 `raw_source.raw_json`

## 195.19 Rust抽象层生成

- **要点**：Bottomley 与 Ojeda 辨析自动 bindings 与手工抽象层之别，后者在 C API 变更时需人手维护；提出扩展 sparse 校验注记、bindgen 生成抽象以降摩擦。
- **史料**：`ksummit.messages.9278`（James Bottomley，2025-02-20）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9278 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以自动 bindings 与手工抽象层的分工、sparse 校验注记与 bindgen 生成等具体手段为分析单位）；经验优先（总纲第 9 条——经验优先：以“手工抽象层在 C API 变更时需人手维护”这一实际成本为判据）
- **辨析**：本块系 James Bottomley 与 Miguel Ojeda 的辨析；“扩展 sparse 校验注记、bindgen 生成抽象以降摩擦”为提案。
- **文献**：DSLXC-11027（`ksummit.messages.9278`，2025-02-20），全文见 `raw_source.raw_json`

## 195.20 安全代码质检门槛

- **要点**：Levin 为 embargo 代码提议硬性测试清单：多版本 GCC 与 Clang、x86 与 arm64 等平台、allmodconfig 等配置及近月 LTP，未过不得悄悄合入。
- **史料**：`ksummit.messages.9281`（Sasha Levin，2023-08-15）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9281 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“多版本 GCC 与 Clang、x86 与 arm64、allmodconfig、近月 LTP”等硬性清单为分析单位）；经验优先（总纲第 9 条——经验优先：以 embargo 代码需私密测试这一实际需求为判据）
- **辨析**：本块系 Sasha Levin 的测试清单提案；“未过不得悄悄合入”为强制性表述，本页未见采纳记录。
- **文献**：DSLXC-11028（`ksummit.messages.9281`，2023-08-15），全文见 `raw_source.raw_json`

## 195.21 维护者峰会存废

- **要点**：Bottomley 披露峰会经费困境：2024 年一家赞助、2025 年零赞助、2026 年仍无，LF 自付与会礼品；Pinchart 估算约 43 人、人均约 2500 美元。
- **史料**：`ksummit.messages.9282`（James Bottomley，2026-08-07）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9282 -->`
- **史观**：法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：峰会经费从一家赞助到零赞助被明示为 LF 与厂商的资助格局）；经验优先（总纲第 9 条——经验优先：以“2024 年一家赞助、2025 年零赞助、2026 年仍无”这一实际数据为判据）
- **辨析**：本块系 James Bottomley 的经费披露与 Pinchart 的估算（约 43 人、人均约 2500 美元）；估算为人均口径，落书须标明。
- **文献**：DSLXC-11029（`ksummit.messages.9282`，2026-08-07），全文见 `raw_source.raw_json`

## 195.22 TAB选举安排

- **要点**：Corbet 解释 TAB 章程把投票绑在内核峰会即 LPC 期间，Babka 因会期漏看 CIVS 邮件错过投票，Corbet 称可修章程把选举移至年内平静时段。
- **史料**：`ksummit.messages.9287`（Jonathan Corbet，2022-09-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9287 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“把选举移至年内平静时段”这一章程修订提议为分析单位）；偶然性优先（总纲第 5 条——没有必然性，只有偶然性：Babka 因会期漏看 CIVS 邮件错过投票）
- **辨析**：本块系 Jonathan Corbet 的章程解释与修订提议；“可修章程”为意向，非已生效改动。
- **文献**：DSLXC-11030（`ksummit.messages.9287`，2022-09-22），全文见 `raw_source.raw_json`

## 195.23 Rust未定义行为

- **要点**：Linus 请 Rust 社区避免 C 式 UB 优化模型：要么朴素代码生成要么明确警告，举 WG14 N3203 收紧未定义行为为例，称潜在优化不值得代价。Linus 阐明 unsafe 的本义是让源码有意绕过规则而非授权编译器重排访问，以分配器指针运算为例，要求编译器不能证明不别名就不要假设。
- **史料**：`ksummit.messages.9288`（Linus Torvalds，2025-02-25）、`ksummit.messages.9363`（Linus Torvalds，2025-02-25）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9288 -->` `<!-- ROW_MINE: ksummit.messages.9363 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 WG14 N3203、分配器指针运算等具体规范与代码为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：朴素代码生成与明确警告两条路线并置）
- **辨析**：两条均系 Linus Torvalds 的一手权威阐述，属本页 Rust 政策奠基性表述；“unsafe 的本义是让源码有意绕过规则而非授权编译器重排访问”为其核心界定，落书须逐字保留。
- **文献**：DSLXC-11031、DSLXC-11044（`ksummit.messages.9288`、`ksummit.messages.9363`，2025-02-25、2025-02-25），全文见 `raw_source.raw_json`

## 195.24 Rust补丁测试

- **要点**：Airlie 坦言 Rust DMA 补丁两难：跨子系统完整系列无人肯审、无用户系列遭拒，故先走后者；Sakkinen 接受以含测试的 git 分支自行验证。
- **史料**：`ksummit.messages.9302`（Jarkko Sakkinen，2025-02-19）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9302 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“含测试的 git 分支自行验证”这一具体替代路径为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：跨子系统完整系列无人肯审与无用户系列遭拒的两难并置）
- **辨析**：本块含 Dave Airlie 的两难自述与 Jarkko Sakkinen 的接受两方；“先走后者”为当事人在两难中的取舍。
- **文献**：DSLXC-11032（`ksummit.messages.9302`，2025-02-19），全文见 `raw_source.raw_json`

## 195.25 安全披露渠道

- **要点**：Kosina 反驳以用户数论 Android 主导：证交所、空管、NASA 等企业级部署经由 Red Hat、SUSE 等供养内核开发，且 Fedora 与 openSUSE 并不用 LTS 基线。
- **史料**：`ksummit.messages.9303`（Jiri Kosina，2023-08-15）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9303 -->`
- **史观**：法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：以用户数论 Android 主导之争被还原为企业级部署与 LTS 基线的利益分布）；经验优先（总纲第 9 条——经验优先：以“Fedora 与 openSUSE 并不用 LTS 基线”这一实际状况为判据）
- **辨析**：本块系 Jiri Kosina 的反驳；“证交所、空管、NASA 等企业级部署经由 Red Hat、SUSE 等供养内核开发”为可核的产业事实。
- **文献**：DSLXC-11033（`ksummit.messages.9303`，2023-08-15），全文见 `raw_source.raw_json`

## 195.26 ISP驱动框架之争

- **要点**：Ribalda 力主 ISP 归 DRM：指 V4L2 路线致九成以上摄像头市场依赖树外驱动、用户仅剩 Android；Pinchart 坚持开放用户态覆盖要求，双方激辩命令缓冲与文档义务。
- **史料**：`ksummit.messages.9304`（Ricardo Ribalda Delgado，2024-07-26）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9304 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：ISP 归 DRM 的主张与开放用户态覆盖要求两方激辩并置）；经验优先（总纲第 9 条——经验优先：以“九成以上摄像头市场依赖树外驱动、用户仅剩 Android”这一关键数据为判据）
- **辨析**：本块含 Ricardo Ribalda 与 Laurent Pinchart 的正面激辩；“九成以上”为可核的量化论断，双方就命令缓冲与文档义务的争点本页未见收敛。
- **文献**：DSLXC-11034（`ksummit.messages.9304`，2024-07-26），全文见 `raw_source.raw_json`

## 195.27 信任网重建

- **要点**：Greg 证实 kernel.org 正与 OpenSSF 合作替换自研 PGP 信任网：旧方案有瓶颈与扩展性局限，新框架预计二月会议公布，工作仍在进行。
- **史料**：`ksummit.messages.9320`（Greg KH，2026-01-23）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9320 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“与 OpenSSF 合作替换自研 PGP 信任网”这一具体工程为分析单位）；知识注定过时（总纲第 22 条——知识注定过时：旧方案有瓶颈与扩展性局限）
- **辨析**：本块系 Greg KH 的实况披露；“新框架预计二月会议公布”为时间性预告，落书须以实际公布为准。
- **文献**：DSLXC-11036（`ksummit.messages.9320`，2026-01-23），全文见 `raw_source.raw_json`

## 195.28 Folios之争

- **要点**：Overstreet 评 folios 争论走偏：Willy 阐述不力、部分 MM 反对无理，澄清 folios 面向文件系统页而非 slab，与 Johannes 讨论出拆分 struct page 思路并等其撤 NACK。
- **史料**：`ksummit.messages.9321`（Kent Overstreet，2021-09-16）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9321 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：Willy 阐述不力、部分 MM 反对无理与“等其撤 NACK”三方立场并置）；动手者叙事（总纲第 10 条——动手者创造历史：以“拆分 struct page 思路”这一具体方案为分析单位）
- **辨析**：本块系 Kent Overstreet 的单方评断；“Willy 阐述不力、部分 MM 反对无理”为对他人立场的评价，落书须标明系当事人判断。
- **文献**：DSLXC-11037（`ksummit.messages.9321`，2021-09-16），全文见 `raw_source.raw_json`

## 195.29 Sphinx构建依赖

- **要点**：Yokosawa 实测发现 openSUSE Leap 15.4 的 Sphinx LaTeX 包缺 Sphinx 4.0 起必需的 tex-gyre 字体，Fedora 36 与 RHEL 9 均覆盖，拟向 openSUSE 报 bug。
- **史料**：`ksummit.messages.9322`（Akira Yokosawa，2022-07-06）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9322 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“openSUSE Leap 15.4 的 Sphinx LaTeX 包缺 tex-gyre 字体、Fedora 36 与 RHEL 9 均覆盖”这一实测为判据）；动手者叙事（总纲第 10 条——动手者创造历史：以“拟向 openSUSE 报 bug”这一具体行动为分析单位）
- **辨析**：本块系 Akira Yokosawa 的实测发现，属可复现的发行版差异；“Sphinx 4.0 起必需”为版本要求陈述。
- **文献**：DSLXC-11038（`ksummit.messages.9322`，2022-07-06），全文见 `raw_source.raw_json`

## 195.30 UALink驱动布局

- **要点**：Intel 的 Sinyuk 确定 UALink 驱动落位：先入 drivers/accel/ual 而非 misc，长期独立为 drivers/ual；Greg 说明 staging 不适合有活跃社区的新子系统。
- **史料**：`ksummit.messages.9328`（Konstantin Sinyuk，2025-09-12）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9328 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“先入 drivers/accel/ual 而非 misc，长期独立为 drivers/ual”这一具体布局为分析单位）；经验优先（总纲第 9 条——经验优先：以“staging 不适合有活跃社区的新子系统”这一维护者判断为判据）
- **辨析**：本块含 Intel 的 Konstantin Sinyuk 的落位决定与 Greg KH 的理由说明两方，属可核的目录决策。
- **文献**：DSLXC-11039（`ksummit.messages.9328`，2025-09-12），全文见 `raw_source.raw_json`

## 195.31 设备树绑定ABI

- **要点**：ÜNAL 主张设备树绑定文档修改不必连带驱动改动，Herring 反驳需同改两侧即已破坏 ABI 且顺序不可二分；ÜNAL 转而接受先修驱动的次序。
- **史料**：`ksummit.messages.9329`（Arınç ÜNAL，2024-09-20）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9329 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：绑定文档不必连带驱动改动的主张与“需同改两侧即已破坏 ABI”的反驳并置）；经验优先（总纲第 9 条——经验优先：以“顺序不可二分”这一机制后果为判据）
- **辨析**：本块含 Arınç ÜNAL 与 Rob Herring 的两方，且记“ÜNAL 转而接受先修驱动的次序”，属本页少见的立场收敛记录。
- **文献**：DSLXC-11040（`ksummit.messages.9329`，2024-09-20），全文见 `raw_source.raw_json`

## 195.32 AI标注标签

- **要点**：Howlett 赞同 Assisted-by 标签改记 AI 使用方式而非模型名，认为随使用普及原标签价值趋零，知名开发者更该用 RFC 标签请求重点审查。
- **史料**：`ksummit.messages.9339`（Liam R. Howlett，2026-07-17）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9339 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“Assisted-by 改记 AI 使用方式而非模型名”这一具体格式主张为分析单位）；知识注定过时（总纲第 22 条——知识注定过时：随使用普及原标签价值趋零）
- **辨析**：本块系 Liam R. Howlett 的标签主张；“知名开发者更该用 RFC 标签请求重点审查”为其配套建议。
- **文献**：DSLXC-11041（`ksummit.messages.9339`，2026-07-17），全文见 `raw_source.raw_json`

## 195.33 文档构建性能

- **要点**：Corbet 剖析 Sphinx C 域符号树约七亿次迭代调用的 O(n²) 行为，改字典查找使 htmldocs 提速约 20%，叠加 automarkup 优化合计约 27%。
- **史料**：`ksummit.messages.9342`（Mauro Carvalho Chehab，2022-06-25）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9342 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“改字典查找使 htmldocs 提速约 20%、叠加 automarkup 优化合计约 27%”这一实测为判据）；动手者叙事（总纲第 10 条——动手者创造历史：以 Sphinx C 域符号树约七亿次迭代调用的 O(n²) 行为这一具体性能缺陷为分析单位）
- **辨析**：本块系 Mauro Carvalho Chehab 的性能剖析，属带数字的可复算实测。
- **文献**：DSLXC-11042（`ksummit.messages.9342`，2022-06-25），全文见 `raw_source.raw_json`

## 195.34 加速器用户态要求

- **要点**：Airlie 阐述 DRM 开源用户态要求：加速器 uAPI 复杂多线程绝非小测试程序可覆盖，社区靠拒绝与教育建成，正起草跨子系统通用文档分支。
- **史料**：`ksummit.messages.9364`（Dave Airlie，2021-09-13）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9364 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“起草跨子系统通用文档分支”这一具体产物为分析单位）；经验优先（总纲第 9 条——经验优先：以“加速器 uAPI 复杂多线程绝非小测试程序可覆盖”这一技术判断为判据）
- **辨析**：本块系 Dave Airlie 的机制阐述；“社区靠拒绝与教育建成”为历史经验表述，其通用文档分支为进行中工作。
- **文献**：DSLXC-11045（`ksummit.messages.9364`，2021-09-13），全文见 `raw_source.raw_json`

## 195.35 AI政策讨论

- **要点**：Stoakes 点出 AI 生成与人工审查成本严重不对称是核心矛盾，故主张 AI 辅助补丁必须自愿加入，并赋权各维护者自行决定取舍。
- **史料**：`ksummit.messages.9367`（Lorenzo Stoakes，2025-08-06）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9367 -->`
- **史观**：法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：AI 生成与人工审查成本严重不对称被点为核心矛盾，落在负担分配上）；多方平等（总纲第 8 条——本体论上各方平等：自愿加入与赋权维护者自行决定取舍并置）
- **辨析**：本块系 Lorenzo Stoakes 的矛盾分析与主张；“必须自愿加入”为其立场，非成文政策。
- **文献**：DSLXC-11046（`ksummit.messages.9367`，2025-08-06），全文见 `raw_source.raw_json`

## 195.36 缓冲缓存退役

- **要点**：Ts'o 详述 ext4 拟弃用 buffer_heads 三因：元数据缓存控制、写回失败无回调、内存开销；folio 改动破坏 bh_offset 被测试抓获属正常，全树改动还阻碍 LTS 回移。
- **史料**：`ksummit.messages.9370`（Theodore Ts'o，2023-09-17）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9370 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以元数据缓存控制、写回失败回调、内存开销三大动因与 bh_offset 回归为分析单位）；经验优先（总纲第 9 条——经验优先：以“folio 改动破坏 bh_offset 被测试抓获”这一实际回归为判据）
- **辨析**：本块系 Theodore Ts'o 的一手详述；“属正常”为其对回归性质的判断，其“全树改动还阻碍 LTS 回移”为治理层论断。
- **文献**：DSLXC-11047（`ksummit.messages.9370`，2023-09-17），全文见 `raw_source.raw_json`

## 195.37 回归追踪

- **要点**：Leemhuis 申请在维护者峰会作约五分钟回归追踪现状报告，含优秀子系统经验与 regzbot 进展，并讨论 bugzilla+bugbot+bugspray 下 regzbot 的去留。
- **史料**：`ksummit.messages.9375`（Thorsten Leemhuis，2024-06-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9375 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“约五分钟回归追踪现状报告”这一具体议程为分析单位）；经验优先（总纲第 9 条——经验优先：以“优秀子系统经验与 regzbot 进展”这一实际积累为判据）
- **辨析**：本块系 Thorsten Leemhuis 的议程申请；“讨论 bugzilla+bugbot+bugspray 下 regzbot 的去留”为待议项。
- **文献**：DSLXC-11048（`ksummit.messages.9375`，2024-06-22），全文见 `raw_source.raw_json`

## 195.38 评审激励机制

- **要点**：Kara 回应 Nossum 的评审激励错位分析：根本动力是共同责任感，避免劣质代码进入自己所在子系统；激励与互审只是辅助，公地悲剧需靠认同化解。
- **史料**：`ksummit.messages.9381`（Jan Kara，2023-08-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9381 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：共同责任感与激励互审两种机制并置）；经验优先（总纲第 9 条——经验优先：以“避免劣质代码进入自己所在子系统”这一实际动力为判据）
- **辨析**：本块系 Jan Kara 对 Nossum 分析的回应；“公地悲剧需靠认同化解”为其主张，属价值判断。
- **文献**：DSLXC-11049（`ksummit.messages.9381`，2023-08-22），全文见 `raw_source.raw_json`

## 195.39 设备直通之争

- **要点**：Bottomley 以史立论：Oracle 曾索要 SCSI 裸设备终被 direct I/O 化解，SPDK/DPDK 仍属小众，USB 令牌统一为 CTAP；够大的用例终被内核吸收，fwctl 宜定位慢速配置面。
- **史料**：`ksummit.messages.9383`（James Bottomley，2024-07-09）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9383 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：Oracle SCSI 裸设备、SPDK/DPDK、USB CTAP 等历史用例并置）；经验优先（总纲第 9 条——经验优先：以“够大的用例终被内核吸收”这一历史规律为判据）
- **辨析**：本块系 James Bottomley 以史立论；“SPDK/DPDK 仍属小众”为其判断，其“fwctl 宜定位慢速配置面”为提案性定位。
- **文献**：DSLXC-11050（`ksummit.messages.9383`，2024-07-09），全文见 `raw_source.raw_json`

## 195.40 补丁发送工具

- **要点**：Glass 介绍 patman 可为每版补丁维护变更日志并一键发送、欢迎功能补丁；Romanovsky 自述另有包装 git format-patch 按目标树自动设收件人的脚本。
- **史料**：`ksummit.messages.9385`（Simon Glass，2021-04-26）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9385 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 patman 的变更日志维护与一键发送、包装 git format-patch 的自动收件人脚本等具体工具为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：现成工具与自建脚本两条路径并置）
- **辨析**：本块含 Simon Glass 的工具介绍与 Leon Romanovsky 的自述脚本两方；“欢迎功能补丁”表明 patman 为开放项目。
- **文献**：DSLXC-11051（`ksummit.messages.9385`，2021-04-26），全文见 `raw_source.raw_json`
