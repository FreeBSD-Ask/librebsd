# 190 【Linux社区】拒收pull标准与AI文档争议

> 来源：ksummit 独有 p54（50 封全读，2021-04 至 2026-07：Linus 一手详述拒收 pull 的真实标准九成九构建失败在提交方与最常见拒绝理由是内容根本不喜欢；Howlett 把 LLM 用户分三类并称 Assisted-by 标签信噪比趋零 Corbet 提及新人几乎当上 lib 维护者；Levin 给出 v6.12-rc4 至 rc5 共 110 个提交绕过 linux-next 的直方图实测系 linus-next 提案关键量化证据；Koolstra 系统汇总 2026 年 AI 助手文档四项争议标签存废用途标注新人降级措辞强化一封即掌握全 thread 分歧图谱；AI 标签政策五封、Rust 系六封）
> 判定：47 CAND / 3 NV。主题分布：AI 审查工具 2、Sashiko AI 审查 2、补丁收件人策略 1、内核日志级别 1、selftests 集成 1、AI 标签政策 5、TAB 选举 1、LLM 缺陷定位 1、malloc API 之辩 1、堆栈行号调试 1、字符串 API 之争 1、Bugzilla 改革 2、文件系统维护信任 2、stable 标签规则 2、Rust 别名规则 1、Rust 补丁测试 1、linus-next 预检 1、lore 检索 1、Rust 内核政策 1、合并树层级 1、静态分析注记 1、工具生成内容规范 2、Link 标签改革 1、C 编译器行为 2、NVMe 拷贝卸载 1、峰会议题流程 1、Linus 拉取准则 1、设备直通开放性 1、Rust GPIO 驱动 1、C 风格改进 1、文档构建环境 1、Rust 安全论证 1、Rust LPC 提案 1、代码风格规则 1、pkeys ABI 1、LLM 审查负担 1。

## 190.1 AI 审查工具

- **要点**：Arnaldo 赞同 Lunn 主张审查自动化工具应面向全体开发者而非仅维护者，称竞争性工具多点使用更能在维护者介入前拦截问题，b4 预检可省去维护者步骤。Kozlowski 支持 Mason 的 AI 审查提示词已接入 BPF CI，介绍 Qualcomm 开源 PatchWise 并在内部对全部补丁发前预审，称可插拔多引擎缓解雇主要求顾虑，亦利新手学习提交规范。
- **史料**：`ksummit.messages.8380`（Arnaldo Carvalho de Melo，2025-10-08）、`ksummit.messages.8407`（Krzysztof Kozlowski，2025-10-10）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8380 -->` `<!-- ROW_MINE: ksummit.messages.8407 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 b4 预检、PatchWise 等可操作的预审工具为分析单位）；经验优先（总纲第 9 条——经验优先：以 Qualcomm 内部对全部补丁发前预审的实际做法为判据）
- **辨析**：两条分属 2025-10 同一议题的不同发言人，均为工具主张；“可插拔多引擎缓解雇主要求顾虑”系 Kozlowski 的推断，非已验结论。
- **文献**：DSLXC-11095、DSLXC-11103（`ksummit.messages.8380`、`ksummit.messages.8407`，2025-10-08、2025-10-10），全文见 `raw_source.raw_json`

## 190.2 Sashiko AI 审查

- **要点**：Gushchin 考虑建预存缺陷库使问题仅报一次并支持误报标记；Gunthorpe 想要 syzkaller 式看板与催办邮件；提示词入库受合并窗口节奏掣肘、需 Linus 支持，并拟依人工反馈半自动改进。Torokhov 支持预存缺陷库，并建议审查报告分两节：一节严格限于补丁本体（含 all clear），另一节冠以“分析中发现的预存问题、随意处理”集中列出，减少维护者噪音。
- **史料**：`ksummit.messages.8389`（Roman Gushchin，2026-07-15）、`ksummit.messages.8437`（Dmitry Torokhov，2026-07-15）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8389 -->` `<!-- ROW_MINE: ksummit.messages.8437 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以预存缺陷库、syzkaller 式看板与报告分节等具体工程方案为分析单位）；经验优先（总纲第 9 条——经验优先：以误报标记与人工反馈半自动改进的实操需求为判据）
- **辨析**：两条均为 AI 审查工具的改进提案；“提示词入库受合并窗口节奏掣肘、需 Linus 支持”为当事人自陈的约束，本页未见采纳记录。
- **文献**：DSLXC-11096、DSLXC-11115（`ksummit.messages.8389`、`ksummit.messages.8437`，2026-07-15、2026-07-15），全文见 `raw_source.raw_json`

## 190.3 补丁收件人策略

- **要点**：明尼苏达事件后 trivial 补丁政策讨论中，Romanovsky 批评精心筛选 To/Cc 使反馈割裂成孤岛，Chehab 辩称收件人差异源于 get_maintainer.pl，Leon 回应 b4 重构线程仍解不了孤岛问题。
- **史料**：`ksummit.messages.8393`（Leon Romanovsky，2021-04-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8393 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：收件人筛选的批评方与辩称方并置）；经验优先（总纲第 9 条——经验优先：以 get_maintainer.pl 与 b4 重构线程的实际效果为判据）
- **辨析**：块内 Romanovsky、Chehab 与 Leon 三方互有反驳，属同一线程的一手交锋；“反馈割裂成孤岛”为当事人定性，非量化结论。
- **文献**：DSLXC-11097（`ksummit.messages.8393`，2021-04-22），全文见 `raw_source.raw_json`

## 190.4 内核日志级别

- **要点**：Iwai 回应 dmesg 密语式报错之惑：内核无法判定缺陷最终影响是两难根源，ACPI 日志过吵、部分 err 可降级，主张为 KERN_ERR 级别制定更清晰准则。
- **史料**：`ksummit.messages.8395`（Takashi Iwai，2022-10-02）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8395 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 ACPI 日志过吵、部分 err 可降级等实际观感为判据）；多方平等（总纲第 8 条——本体论上各方平等：用户对密语式报错之惑与维护者的两难自陈并置）
- **辨析**：本块系 Takashi Iwai 单方回应；“内核无法判定缺陷最终影响”为维护者自陈的机制性两难，非政策结论。
- **文献**：DSLXC-11098（`ksummit.messages.8395`，2022-10-02），全文见 `raw_source.raw_json`

## 190.5 selftests 集成

- **要点**：Pinchart 指出 Mesa 与 libcamera 对所支持设备已有成套测试，就其能否及如何与内核 selftests 集成提出疑问，坦言尚无成熟做法。
- **史料**：`ksummit.messages.8396`（Laurent Pinchart，2021-09-11）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8396 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 Mesa 与 libcamera 已有成套设备测试这一实际先例为判据）；偶然性优先（总纲第 5 条——没有必然性，只有偶然性：集成路径尚属开放疑问）
- **辨析**：本块系 Laurent Pinchart 的开放提问，当事人坦言“尚无成熟做法”，落书不得读作已定方案。
- **文献**：DSLXC-11099（`ksummit.messages.8396`，2021-09-11），全文见 `raw_source.raw_json`

## 190.6 AI 标签政策

- **要点**：Koolstra 汇总 AI 助手文档争议供峰会讨论：Layton 提议废除 Assisted-by 而 Greg KH 反对，Hildenbrand 建议标注 LLM 具体用途，Stoakes 质疑新人疑似 LLM 深度改动可否降级处理。Kozlowski 提议以 Legal-risk-by 类标签明示 AI 补丁的法律风险，McKenney 建议带此类标签的补丁干脆不要合入，因多起 AI 训练版权诉讼未决、各国立法走向难料。Bottomley 以版权溯源立论：Signed-off-by 本为防 SCO 式指控而设，美国版权局对生成式 AI 的立场使 AI 使用影响补丁版权状态，git 树须留永久记录，且只需标 AI 写码而非 AI 审查。Howlett 分 LLM 用户为三类并称 Assisted-by 信噪比趋零，冒用 LLM 者反复重发使他想设超时禁投规则；预言工具由圈地转向变现时社区生产力下滑；Corbet 提及有新人几乎当上 lib/ 维护者。Luck 提议两条规则：禁止 AI 代理直接提交、From 必须为真人且对内容负全责；McKenney 指若要求训练集许可兼容则现有主流 AI 无一合格；Anvin 认为须寻求正式法律意见。
- **史料**：`ksummit.messages.8398`（Jori Koolstra，2026-07-16）、`ksummit.messages.8414`（Paul E. McKenney，2025-08-12）、`ksummit.messages.8430`（James Bottomley，2026-07-17）、`ksummit.messages.8488`（Liam R. Howlett，2026-07-16）、`ksummit.messages.8499`（Paul E. McKenney，2025-08-11）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8398 -->` `<!-- ROW_MINE: ksummit.messages.8414 -->` `<!-- ROW_MINE: ksummit.messages.8430 -->` `<!-- ROW_MINE: ksummit.messages.8488 -->` `<!-- ROW_MINE: ksummit.messages.8499 -->`
- **史观**：法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：Assisted-by 存废与 AI 补丁版权状态之争落在 Signed-off-by 的法律功能上）；多方平等（总纲第 8 条——本体论上各方平等：废除标签、标注用途、降级处理与禁止代理提交五说并置）
- **辨析**：Bottomley 的“Signed-off-by 本为防 SCO 式指控而设”为法律史解释，须与当期 DCO 文本核对；McKenney 的“主流 AI 无一合格”与 Anvin 的“须求正式法律意见”均非法律意见，本块只登记为议题。
- **文献**：DSLXC-11100、DSLXC-11107、DSLXC-11111、DSLXC-11135、DSLXC-11139（`ksummit.messages.8398`、`ksummit.messages.8414`、`ksummit.messages.8430`、`ksummit.messages.8488`、`ksummit.messages.8499`，2026-07-16、2025-08-12、2026-07-17、2026-07-16、2025-08-11），全文见 `raw_source.raw_json`

## 190.7 TAB 选举

- **要点**：Corbet 公告 2024 年 TAB 选举：9 月 20 至 27 日经 CIVS 改选 5 席，Brauner、Cook、Hansen、Kicinski、Williams 任期届满；资格为 2023 年起 3 个带 tag 提交，满 50 个自动寄票。
- **史料**：`ksummit.messages.8401`（Jonathan Corbet，2024-09-11）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8401 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 2024 年选举的席位、日期与资格门槛等可核事实为准）；动手者叙事（总纲第 10 条——动手者创造历史：以“3 个带 tag 提交、满 50 个自动寄票”这一具体参与门槛为分析单位）
- **辨析**：本块系 Jonathan Corbet 的选举公告，属程序性一手；其中 CIVS 改选 5 席与任期届满名单为事实陈述，非评价。
- **文献**：DSLXC-11101（`ksummit.messages.8401`，2024-09-11），全文见 `raw_source.raw_json`

## 190.8 LLM 缺陷定位

- **要点**：Levin 详述其 LLM 堆栈分析：读源码、翻 git 历史定位肇事提交、搜 lore 找旧报告并自动抄送相关开发者，主张与确定性工具并用；Pinchart 忧虑非确定方法产出貌似合理的错误结果。
- **史料**：`ksummit.messages.8406`（Sasha Levin，2026-03-07）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8406 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以读源码、翻 git 历史、搜 lore 的具体定位流程为分析单位）；经验优先（总纲第 9 条——经验优先：以确定性工具与 LLM 并用的主张为判据）
- **辨析**：本块含 Levin 的自述与 Pinchart 的忧虑两方；“貌似合理的错误结果”为 Pinchart 的担忧，非对 LLM 能力的实测结论。
- **文献**：DSLXC-11102（`ksummit.messages.8406`，2026-03-07），全文见 `raw_source.raw_json`

## 190.9 malloc API 之辩

- **要点**：Carpenter 反驳 Wilcox 对 GFP 参数的批评，指如今多数开发者已改用 kzmalloc_obj() 无需再传 GFP_KERNEL，佐证语义化分配接口已被广泛采用。
- **史料**：`ksummit.messages.8411`（Dan Carpenter，2026-07-09）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8411 -->`
- **史观**：知识注定过时（总纲第 22 条——知识注定过时：GFP 参数之争以多数开发者已改用 kzmalloc_obj() 收束）；经验优先（总纲第 9 条——经验优先：以语义化分配接口被广泛采用这一实际状况为判据）
- **辨析**：本块系 Dan Carpenter 单方反驳；“多数开发者已改用”为当事人估计，本页未附采用率统计。
- **文献**：DSLXC-11104（`ksummit.messages.8411`，2026-07-09），全文见 `raw_source.raw_json`

## 190.10 堆栈行号调试

- **要点**：Deller 实测 CONFIG_KALLSYMS_LINEINFO 在 parisc 架构正常工作并望合入，Levin 随即提交加入模块支持与他人建议内存优化的正式补丁系列。
- **史料**：`ksummit.messages.8412`（Sasha Levin，2026-03-03）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8412 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 CONFIG_KALLSYMS_LINEINFO 在 parisc 的实测与随后的补丁系列为分析单位）；经验优先（总纲第 9 条——经验优先：以 parisc 架构实际正常工作为判据）
- **辨析**：本块系 Sasha Levin 的实测陈述与后续动作；其“望合入”与“提交正式补丁系列”属进行中事态，落书须以合入记录为准。
- **文献**：DSLXC-11105（`ksummit.messages.8412`，2026-03-03），全文见 `raw_source.raw_json`

## 190.11 字符串 API 之争

- **要点**：Tarreau 支持指针加长度字符串，实测把 strcmp 链改为 isteq 后 -O3 提速约 10 倍、-O2 约 5 倍，长度已知可免去中间检查，赞同 Hellwig 推崇的 seq_buf 路线。
- **史料**：`ksummit.messages.8413`（Willy Tarreau，2023-10-19）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8413 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 strcmp 链改 isteq 后 -O3 提速约 10 倍、-O2 约 5 倍的实测为判据）；动手者叙事（总纲第 10 条——动手者创造历史：以指针加长度字符串与 seq_buf 路线为分析单位）
- **辨析**：提速倍数为当事人自测，测试条件本页未附，落书引用须标明口径；Hellwig 的 seq_buf 路线为被赞同方，非本块发言人。
- **文献**：DSLXC-11106（`ksummit.messages.8413`，2023-10-19），全文见 `raw_source.raw_json`

## 190.12 Bugzilla 改革

- **要点**：Tashkinov 力主保留 bugzilla：多数开发者从未注册致报告无人看，提议组件与 Kconfig 同步、amdgpu/i915 等自动转投自有追踪器、默认加入可退订，并批评邮件列表同样失灵。Ryabitsev 透露 bugzilla 平台近死：开发停滞、不兼容新 MySQL、靠迁 Postgres 勉强撑过 2022，LF 非开发机构且 bugmaster 易倦怠；Tashkinov 提议 git.kernel.org 等合并为 gitlab.kernel.org。
- **史料**：`ksummit.messages.8418`（Artem S. Tashkinov，2022-09-29）、`ksummit.messages.8434`（Artem S. Tashkinov，2022-09-29）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8418 -->` `<!-- ROW_MINE: ksummit.messages.8434 -->`
- **史观**：知识注定过时（总纲第 22 条——知识注定过时：bugzilla 平台“近死”、不兼容新 MySQL 而靠迁 Postgres 勉强撑过 2022）；多方平等（总纲第 8 条——本体论上各方平等：保留 bugzilla 的主张与平台近死的实况并置）
- **辨析**：Ryabitsev 的平台状况陈述与 Tashkinov 的改革主张分属两方；其“多数开发者从未注册致报告无人看”为当事人判断，本页未附注册数据。
- **文献**：DSLXC-11108、DSLXC-11113（`ksummit.messages.8418`、`ksummit.messages.8434`，2022-09-29、2022-09-29），全文见 `raw_source.raw_json`

## 190.13 文件系统维护信任

- **要点**：Hellwig 反对以只读保留无人维护的文件系统，称现有测试设施对只读完全失效，还需测试框架、公开共享镜像或镜像生成工具，成本相当可观。Roeck 给出 ntfs3 可靠损坏复现：qemu 快照内 64M 镜像反复 cp、rm 序列，rm 报目录非空、umount 触发回溯或崩溃；镜像 md5 校验、只读保存以排除干扰，回应 Sanjaya 质疑。
- **史料**：`ksummit.messages.8420`（Christoph Hellwig，2023-09-08）、`ksummit.messages.8453`（Guenter Roeck，2023-09-07）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8420 -->` `<!-- ROW_MINE: ksummit.messages.8453 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 ntfs3 的 qemu 快照 64M 镜像反复 cp、rm 可靠复现与 md5 校验为判据）；多方平等（总纲第 8 条——本体论上各方平等：反对只读保留的维护者立场与提供复现的质疑回应并置）
- **辨析**：Roeck 的复现步骤为可执行的一手证据，属本块最强证据；Hellwig 的“测试设施对只读完全失效”为维护者判断，成本估计未附细目。
- **文献**：DSLXC-11109、DSLXC-11124（`ksummit.messages.8420`、`ksummit.messages.8453`，2023-09-08、2023-09-07），全文见 `raw_source.raw_json`

## 190.14 stable 标签规则

- **要点**：前 git 时代 Fixes 标注之争：Bottomley 主张引 tglx history 树哈希，Carpenter 称会令众人困惑，Greg KH 附和说此类哈希使其回溯脚本报错跳过，殃及 stable 回移植判断。Belloni 反驳以奖惩促开发者标 Cc: stable：多数贡献者与维护者根本不关心 stable，行为无关好坏，惩罚框架不成立。
- **史料**：`ksummit.messages.8429`（Greg KH，2024-07-16）、`ksummit.messages.8444`（Alexandre Belloni，2024-07-15）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8429 -->` `<!-- ROW_MINE: ksummit.messages.8444 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 Greg KH 回溯脚本因哈希报错跳过这一实际后果为判据）；多方平等（总纲第 8 条——本体论上各方平等：引 history 树哈希的主张与“多数贡献者根本不关心 stable”的反驳并置）
- **辨析**：两条分属 2024-07 同一规则讨论的两方；Belloni 的“行为无关好坏、惩罚框架不成立”为对激励设计的否定判断，非统计结论。
- **文献**：DSLXC-11110、DSLXC-11120（`ksummit.messages.8429`、`ksummit.messages.8444`，2024-07-16、2024-07-15），全文见 `raw_source.raw_json`

## 190.15 Rust 别名规则

- **要点**：Jack 担忧 Rust 别名规则官方绑定 LLVM、缺独立规范，恐妨碍 gccrs 实现一致行为；并引文档指出原子操作沿袭 C++20 内存模型、panic 底层近乎 C++ 异常，加大 unsafe 难度。
- **史料**：`ksummit.messages.8433`（Ventura Jack，2025-02-26）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8433 -->`
- **史观**：知识注定过时（总纲第 22 条——知识注定过时：Rust 别名规则官方绑定 LLVM、缺独立规范，gccrs 一致性隐忧）；多方平等（总纲第 8 条——本体论上各方平等：LLVM 绑定现状与 gccrs 实现诉求并置）
- **辨析**：本块系 Ventura Jack 单方担忧，所引文档为间接证据；“恐妨碍 gccrs 一致行为”为预测，非已发生的实现分歧。
- **文献**：DSLXC-11112（`ksummit.messages.8433`，2025-02-26），全文见 `raw_source.raw_json`

## 190.16 Rust 补丁测试

- **要点**：Sakkinen 指 Rust DMA 补丁无测试载荷应自动 NAK，Feng 核实其仅有一个不会执行的函数定义式 doc test，说明 Rust 代码本可用 kunit 跑 doctest，同意必须补测试。
- **史料**：`ksummit.messages.8436`（Boqun Feng，2025-02-18）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8436 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 doc test 是否会被执行这一可核验的测试事实为分析单位）；经验优先（总纲第 9 条——经验优先：以 Rust DMA 补丁无测试载荷这一实际状况为判据）
- **辨析**：本块含 Sakkinen 的 NAK 主张与 Feng 的核实两方；“仅有一个不会执行的函数定义式 doc test”为 Feng 的核查结果，属一手事实。
- **文献**：DSLXC-11114（`ksummit.messages.8436`，2025-02-18），全文见 `raw_source.raw_json`

## 190.17 linus-next 预检

- **要点**：Levin 公布 v6.12-rc4 至 rc5 提交在 linux-next 停留直方图：89 个 0 天、21 个不足 1 天，即 110 个提交未经 -next 直入 Linus 树，主张 linus-next 补上绕过测试的漏洞。
- **史料**：`ksummit.messages.8439`（Sasha Levin，2024-10-28）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8439 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 v6.12-rc4 至 rc5 的 89 个 0 天、21 个不足 1 天这一直方图实测为判据）；偶然性优先（总纲第 5 条——没有必然性，只有偶然性：绕过测试由合并窗口末段的提交时序暴露）
- **辨析**：直方图系 Sasha Levin 制作的一手统计；本页未附原始脚本，落书引用须标明其自述口径。
- **文献**：DSLXC-11116（`ksummit.messages.8439`，2024-10-28），全文见 `raw_source.raw_json`

## 190.18 lore 检索

- **要点**：Ryabitsev 答复 Lawall：lkml.kernel.org/r/<msgid> 仅重定向至 lore.kernel.org/all/ 聚合检索，THE REST 改投新列表不影响按 message_id 或主题追溯补丁讨论。
- **史料**：`ksummit.messages.8441`（Konstantin Ryabitsev，2023-11-07）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8441 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 lkml.kernel.org/r/<msgid> 的实际重定向行为为判据）；知识注定过时（总纲第 22 条——知识注定过时：THE REST 改投新列表后按 message_id 追溯的老路径仍须说明）
- **辨析**：本块系 Konstantin Ryabitsev 对 Julia Lawall 的答复，属基础设施方的一手说明；“不影响追溯”为其技术判断，须以实际检索验证。
- **文献**：DSLXC-11117（`ksummit.messages.8441`，2023-11-07），全文见 `raw_source.raw_json`

## 190.19 Rust 内核政策

- **要点**：Anvin 拆分四议题：Rust 与 C 成熟度差距拖累 C 维护者、政策文件“无并行代码”说法需引证；主张用 C++ 等成熟工具立即改进 3500 万行既有代码，并赌 2050 年内核仍有大量 C。
- **史料**：`ksummit.messages.8442`（H. Peter Anvin，2025-02-19）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8442 -->`
- **史观**：知识注定过时（总纲第 22 条——知识注定过时：3500 万行既有 C 代码与“2050 年内核仍有大量 C”的长期判断）；多方平等（总纲第 8 条——本体论上各方平等：Rust 与 C 成熟度差距的两端并置）
- **辨析**：本块系 H. Peter Anvin 单方拆分四议题；“政策文件‘无并行代码’说法需引证”为其对既有文本的质疑，落书须回原文核对。
- **文献**：DSLXC-11118（`ksummit.messages.8442`，2025-02-19），全文见 `raw_source.raw_json`

## 190.20 合并树层级

- **要点**：Rostedt 以 rtla 为例：让 Bristot 自管分支并直接写 pull request，自己只审总体思路、快进合并后转发 Linus，以此反驳 Kosina “不减少上层工作量”之说。
- **史料**：`ksummit.messages.8443`（Steven Rostedt，2024-06-04）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8443 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 rtla 分支自管、直接写 pull request 的具体做法为分析单位）；经验优先（总纲第 9 条——经验优先：以快进合并后转发 Linus 这一实际流程为判据）
- **辨析**：本块系 Steven Rostedt 以自身实践反驳 Kosina 之说；“不减少上层工作量”之争本页以单例回应，未成通则。
- **文献**：DSLXC-11119（`ksummit.messages.8443`，2024-06-04），全文见 `raw_source.raw_json`

## 190.21 静态分析注记

- **要点**：指针返回值注记讨论：Bergmann 归纳四类返回约定，Geert 补 optional 第五类；Lawall 质疑“调用者之错”论，统计逾 230 个文件存在同返 NULL 与 ERR_PTR 的函数并举例 ovl_lookup_inode。
- **史料**：`ksummit.messages.8450`（Julia Lawall，2021-07-26）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8450 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以逾 230 个文件存在同返 NULL 与 ERR_PTR 的统计为判据）；动手者叙事（总纲第 10 条——动手者创造历史：以指针返回值注记的返回约定分类为分析单位）
- **辨析**：“逾 230 个文件”系 Julia Lawall 的统计口径，本页未附检索式；Bergmann 四类与 Geert 第五类为归纳性约定，非强制规范。
- **文献**：DSLXC-11121（`ksummit.messages.8450`，2021-07-26），全文见 `raw_source.raw_json`

## 190.22 工具生成内容规范

- **要点**：Bottomley 与 Stoakes 就 slop 措辞妥协，改写为“结果可能有误，提交者须理解并能为其辩护，否则维护者可整包拒绝”；Stoakes 承认该文档因 Linus 立场恐难合入。Lawall 称维护者凭经验即可识别 checkpatch、Coccinelle、smatch 驱动的补丁并据既往工具经验调整审查，质疑对 AI 生成补丁是否同样奏效。
- **史料**：`ksummit.messages.8451`（James Bottomley，2026-01-08）、`ksummit.messages.8510`（Julia Lawall，2026-01-08）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8451 -->` `<!-- ROW_MINE: ksummit.messages.8510 -->`
- **史观**：法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：工具生成内容规范的措辞之争落在“维护者可整包拒绝”这一权力边界上）；多方平等（总纲第 8 条——本体论上各方平等：slop 措辞的妥协方与质疑 AI 审查是否同样奏效方并置）
- **辨析**：妥协后的表述“提交者须理解并能为其辩护，否则维护者可整包拒绝”为文本结果，属一手；Stoakes 的“因 Linus 立场恐难合入”为预测，非既成事实。
- **文献**：DSLXC-11122、DSLXC-11141（`ksummit.messages.8451`、`ksummit.messages.8510`，2026-01-08、2026-01-08），全文见 `raw_source.raw_json`

## 190.23 Link 标签改革

- **要点**：Bottomley 主张把 Link 之争拆成自动化追踪与人工背景两层；Rostedt 说明自己用脚本把链接放 tags 区供工具用，人类语境链接放 tags 外，且仅当补丁源自另一场讨论时才添加。
- **史料**：`ksummit.messages.8452`（Steven Rostedt，2025-10-16）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8452 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以脚本把链接放 tags 区供工具用、人类语境链接放 tags 外这一具体做法为分析单位）；经验优先（总纲第 9 条——经验优先：以“仅当补丁源自另一场讨论时才添加”这一实操规则为判据）
- **辨析**：本块含 Bottomley 的两层拆分主张与 Rostedt 的自述做法两方；后者为个人惯例，非全局规范。
- **文献**：DSLXC-11123（`ksummit.messages.8452`，2025-10-16），全文见 `raw_source.raw_json`

## 190.24 C 编译器行为

- **要点**：Laight 声援 Torvalds：编译器对必然成立仍被要求检查的范围判断照样告警，疑对编译期即死的短路条件也告警，且 _Generic 各分支均须编译，无法规避类型相关误报。Rostedt 概括规则：编译器不得超出代码字面多读全局变量，但可缓存既有的多次读；Laight 补充标准允许编译器先向该内存写无关值（如寄存器溢出）再写预期值，gcc 尚未这么做。
- **史料**：`ksummit.messages.8454`（David Laight，2025-02-23）、`ksummit.messages.8473`（David Laight，2025-02-27）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8454 -->` `<!-- ROW_MINE: ksummit.messages.8473 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 _Generic 各分支均须编译、短路条件告警等编译器实际行为为判据）；动手者叙事（总纲第 10 条——动手者创造历史：以“编译器不得超出代码字面多读全局变量”这一可操作规则为分析单位）
- **辨析**：两条均系 David Laight 的技术陈述；“gcc 尚未这么做”为对编译器现状的观察，落书须以当期版本核对。
- **文献**：DSLXC-11125、DSLXC-11132（`ksummit.messages.8454`、`ksummit.messages.8473`，2025-02-23、2025-02-27），全文见 `raw_source.raw_json`

## 190.25 NVMe 拷贝卸载

- **要点**：Selva 提出 LPC 技术议题：NVMe 简单拷贝命令 SCC 的上游实现，待议用户接口取 ioctl、io_uring 操作码还是 copy_file_range，块层用空 bio 链还是带载荷，及 SCSI XCOPY 兼容性。
- **史料**：`ksummit.messages.8455`（Selva Jove，2021-06-25）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8455 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 NVMe SCC 的用户接口与块层实现路径为分析单位）；偶然性优先（总纲第 5 条——没有必然性，只有偶然性：接口取 ioctl、io_uring 还是 copy_file_range 尚属开放）
- **辨析**：本块系 Selva Jove 提交的 LPC 议题，四问均为待议项，本页无结论。
- **文献**：DSLXC-11126（`ksummit.messages.8455`，2021-06-25），全文见 `raw_source.raw_json`

## 190.26 峰会议题流程

- **要点**：Kara 认为 richACLs 属技术议题宜投 LSFMM；Rostedt 引 Ted 规则说明 ksummit track 须同时发 [TECH TOPIC] 邮件并在 LPC 网站立项，截止 2025-09-10，CfP 周三关闭。
- **史料**：`ksummit.messages.8456`（Steven Rostedt，2025-09-08）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8456 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 ksummit track 须同时发 [TECH TOPIC] 邮件并在 LPC 网站立项、截止 2025-09-10 等程序事实为判据）；动手者叙事（总纲第 10 条——动手者创造历史：以议题该投 LSFMM 还是 ksummit 的归类为分析单位）
- **辨析**：本块含 Kara 的归类意见与 Rostedt 引 Ted 规则的说明两方；程序细节属一手，落书须以当期 CfP 为准。
- **文献**：DSLXC-11127（`ksummit.messages.8456`，2025-09-08），全文见 `raw_source.raw_json`

## 190.27 Linus 拉取准则

- **要点**：Torvalds 详述拒收实情：构建失败九成九在提交方（未进 linux-next 或无视已报问题），bindgen 仅意外一次；运行期问题常是测试场没有的 GPU、无线硬件；最常见拒绝理由是内容根本不喜欢。
- **史料**：`ksummit.messages.8460`（Linus Torvalds，2025-02-26）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8460 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“构建失败九成九在提交方”这一维护者长期观察为判据）；多方平等（总纲第 8 条——本体论上各方平等：构建失败、运行期硬件缺失与“内容根本不喜欢”三类拒收理由并列）
- **辨析**：本块系 Linus Torvalds 的一手自述，属本页最高证据等级；“九成九”为当事人估计而非统计，落书须标明其自述口径。
- **文献**：DSLXC-11128（`ksummit.messages.8460`，2025-02-26），全文见 `raw_source.raw_json`

## 190.28 设备直通开放性

- **要点**：Gunthorpe 以 mlx5 为例：1.2 万行 mlx5_ifc.h、公开编程手册、内核内实现与 DPDK 等开源栈覆盖绝大多数用例，反问为堵一成假想专有用例而在内核加校验、损害技术方案是否值得。
- **史料**：`ksummit.messages.8464`（Jason Gunthorpe，2024-07-26）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8464 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 mlx5_ifc.h 行数、公开编程手册与 DPDK 等开源栈为分析单位）；经验优先（总纲第 9 条——经验优先：以现有开源栈覆盖绝大多数用例这一实际状况为判据）
- **辨析**：本块系 Jason Gunthorpe 的设问式反驳；“一成假想专有用例”为当事人估数，非实测。
- **文献**：DSLXC-11129（`ksummit.messages.8464`，2024-07-26），全文见 `raw_source.raw_json`

## 190.29 Rust GPIO 驱动

- **要点**：Walleij 以 GPIO 维护者身份表态愿意尝试 Rust 驱动并引荐搭档 Bartosz，Ojeda 请其挑选带 QEMU 支持或测试套件的型号以便验证，是 Rust 驱动落地最早的维护者互动之一。
- **史料**：`ksummit.messages.8465`（Miguel Ojeda，2021-07-08）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8465 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 GPIO 维护者引荐搭档、挑选带 QEMU 支持型号等具体互动为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：Rust 驱动尝试方与验证方地位平等）
- **辨析**：本块系维护者与提案者的双向互动；“Rust 驱动落地最早的维护者互动之一”为史家定位，属编注而非原始结论。
- **文献**：DSLXC-11130（`ksummit.messages.8465`，2021-07-08），全文见 `raw_source.raw_json`

## 190.30 C 风格改进

- **要点**：Greg KH 称内核多数低级错误源自 C 角落案例而在 Rust 中消失；Anvin 主张宏化 alloc、memcpy 的显式尺寸（如其 nasm_new），并多用 C90 起合法的结构体赋值以减少此类错误。
- **史料**：`ksummit.messages.8469`（H. Peter Anvin，2025-02-20）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8469 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以宏化 alloc、memcpy 显式尺寸与结构体赋值等具体手法为分析单位）；经验优先（总纲第 9 条——经验优先：以“多数低级错误源自 C 角落案例”这一经验判断为判据）
- **辨析**：本块含 Greg KH 的判断与 Anvin 的具体建议两方；“在 Rust 中消失”为当事人对比论断，非实测对照。
- **文献**：DSLXC-11131（`ksummit.messages.8469`，2025-02-20），全文见 `raw_source.raw_json`

## 190.31 文档构建环境

- **要点**：Chehab 与 Berg 论文档构建 Python 依赖：openSUSE Leap 的 python3-Sphinx 仅配 Python 3.6、Sphinx 2.3 过旧，RHEL8 同病；Berg 主张只用 python3、过旧即失败，最终交 Corbet 裁决。
- **史料**：`ksummit.messages.8476`（Mauro Carvalho Chehab，2025-09-03）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8476 -->`
- **史观**：知识注定过时（总纲第 22 条——知识注定过时：openSUSE Leap 的 python3-Sphinx 仅配 Python 3.6、Sphinx 2.3 过旧，RHEL8 同病）；动手者叙事（总纲第 10 条——动手者创造历史：以“只用 python3、过旧即失败”的构建规则为分析单位）
- **辨析**：本块系 Mauro Carvalho Chehab 与 Berg 的构建环境讨论；“最终交 Corbet 裁决”表明本页未见结论。
- **文献**：DSLXC-11133（`ksummit.messages.8476`，2025-09-03），全文见 `raw_source.raw_json`

## 190.32 Rust 安全论证

- **要点**：Overstreet 以 Rice 定理解释借用检查器之必然，称消除安全代码 UB 是超越 C 的根本前提，并以 fuse 模块 UAF 迫使 bcachefs fsck 扩展性测试中断一周为例，凸显 C 难复现缺陷的隐性成本。
- **史料**：`ksummit.messages.8486`（Kent Overstreet，2025-02-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8486 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 fuse 模块 UAF 迫使 bcachefs fsck 扩展性测试中断一周这一实际代价为判据）；动手者叙事（总纲第 10 条——动手者创造历史：以借用检查器消除安全代码 UB 这一机制前提为分析单位）
- **辨析**：本块系 Kent Overstreet 单方论证；“Rice 定理”为其理论依据，其“隐性成本”估值为单例，落书不得外推。
- **文献**：DSLXC-11134（`ksummit.messages.8486`，2025-02-22），全文见 `raw_source.raw_json`

## 190.33 Rust LPC 提案

- **要点**：Ojeda 提交 LPC 2023 议题：Rust 支持已随 v6.1 入树，汇报 pinned-init、KUnit doctest 集成、klint 编译期锁规则检查等进展，及稳定版不健全处理与 Rust 版本升级政策，征询维护者接受之道。
- **史料**：`ksummit.messages.8489`（Miguel Ojeda，2023-08-07）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8489 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 pinned-init、KUnit doctest 集成、klint 编译期锁规则检查等具体进展为分析单位）；知识注定过时（总纲第 22 条——知识注定过时：稳定版不健全处理与 Rust 版本升级政策属随版本演进的议题）
- **辨析**：本块系 Miguel Ojeda 提交的 LPC 2023 议题；“征询维护者接受之道”表明其定位为求共识而非既成政策。
- **文献**：DSLXC-11136（`ksummit.messages.8489`，2023-08-07），全文见 `raw_source.raw_json`

## 190.34 代码风格规则

- **要点**：Laight 反对头文件按字母排序，主张系统、子系统、本地分组，变量声明以易读为先；Bird 指出排序规则本为减少 patch、quilt 应用补丁时的上下文冲突。
- **史料**：`ksummit.messages.8492`（David Laight，2026-01-17）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8492 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：字母排序与系统／子系统／本地分组两种风格并置）；经验优先（总纲第 9 条——经验优先：以排序规则本为减少 patch、quilt 上下文冲突这一历史成因定优劣）
- **辨析**：本块含 Laight 的反对与 Bird 的成因说明两方；排序规则的原始动机为历史解释，落书须与早期提交实践核对。
- **文献**：DSLXC-11137（`ksummit.messages.8492`，2026-01-17），全文见 `raw_source.raw_json`

## 190.35 pkeys ABI

- **要点**：Brodsky 指 pkeys ABI 对信号送达、rseq、io_uring 工作线程等异步内核交互严重欠规范、各架构处理不一，引 Gleixner “全都坏了”之评，拟借 LPC Refereed BoF 汇总现状并探求解法。
- **史料**：`ksummit.messages.8498`（Kevin Brodsky，2026-06-17）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8498 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 pkeys 对信号送达、rseq、io_uring 工作线程等异步交互的实际欠规范为判据）；多方平等（总纲第 8 条——本体论上各方平等：各架构处理不一的多方现状与 Gleixner 的“全都坏了”之评并置）
- **辨析**：本块系 Kevin Brodsky 的现状汇总与 LPC BoF 计划；“全都坏了”系引 Gleixner 之评，落书须与原话核对。
- **文献**：DSLXC-11138（`ksummit.messages.8498`，2026-06-17），全文见 `raw_source.raw_json`

## 190.36 LLM 审查负担

- **要点**：Kosina 称曾见 ChatGPT 全写的 GPIO 驱动功能正常却缺错误处理；Reinecke 指内核代码即训练素材、LLM 同样轻视错误处理，九成合格的产物仍须人审，而审查人力本已不足。
- **史料**：`ksummit.messages.8508`（Hannes Reinecke，2025-08-06）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8508 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“九成合格的产物仍须人审而审查人力本已不足”这一实际负担为判据）；多方平等（总纲第 8 条——本体论上各方平等：Kosina 的个例观察与 Reinecke 的结构性判断并置）
- **辨析**：本块含 Hannes Reinecke 的转述（ChatGPT 全写 GPIO 驱动）与判断两方；“内核代码即训练素材”为其论断，非法律或技术定论。
- **文献**：DSLXC-11140（`ksummit.messages.8508`，2025-08-06），全文见 `raw_source.raw_json`
