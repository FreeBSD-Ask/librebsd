# 196 【Linux社区】THEREST分流与generatedcontent

> 来源：ksummit 独有 p60（50 封全读，2021-04 至 2026-07：Konstantin 提出 THE REST 分流 patches@ 的原始 RFC 含 LKML 占 vger 七成月帖 3.3 万日均 310 万封投递与 Gmail 积压 5-20 万封一手基础设施数据；Leemhuis 用 6.7.2/6.9.3 逐项统计 640 与 427 项变更用户测试窗不足 4 天量化回归修复未及时进 stable 漏洞；Dave Hansen 提交 TAB 集体起草 generated-content.rst v5 全文系内核应对 AI 生成内容首份正式准则文本含维护者可不经详审拒绝条款与 11 位维护者签署链；Greg KH 对以 b4 查询取代 Link 尾注系统反对书含保险税论与 LF 早年邮件溯源工具失败史；设备直通与 fwctl 六封）
> 判定：43 CAND / 7 NV。主题分布：Link尾注规范 2、签名信任体系 1、LKML流量分流 2、设备直通与fwctl 6、C字符串API清理 1、Rust政策争论 1、回归修复规则 2、AI审查实践 3、linus-next测试树 1、Rust别名模型争论 2、工具生成内容准则 2、Rust引进争论 2、回归追踪机器人 1、展开器可靠性 1、用户态开源要求 1、C标准饱和运算 1、Bugzilla改革 3、UMN假补丁清理 1、AI补丁标注责任 2、文档可读性改进 1、HIGHMEM淘汰风险 1、维护者支持小组 1、cleanup.h变量放置 1、峰会提问形式 1、TAB选举投票 1、原子内存序讨论 1、引用过多自动提醒 1。

## 196.1 Link尾注规范

- **要点**：Konstantin 解释 Link 尾注中“#”之后内容仅是注释约定，格式为“Trailer 名: 正文 # 注释”，回应 Kees 对文档新增“# [1]”写法的疑问。Greg KH 反对以 b4 查询取代 Link 尾注：增加维护者负担、离线无法应用补丁、用户不会装 b4；预言多数人会漏加，称这一行是“保险税”，曾在稳定分支工作省下大量时间。
- **史料**：`ksummit.messages.9387`（Konstantin Ryabitsev，2024-06-21）、`ksummit.messages.9404`（Greg KH，2025-10-16）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9387 -->` `<!-- ROW_MINE: ksummit.messages.9404 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 Link 尾注的注释约定与 b4 查询替代方案等具体机制为分析单位）；经验优先（总纲第 9 条——经验优先：以“曾在稳定分支工作省下大量时间”这一实际经验为判据）
- **辨析**：两条分属格式澄清与方案反对；“这一行是保险税”为 Greg KH 的比喻，其“预言多数人会漏加”属预测，本页未见统计。
- **文献**：DSLXC-11314、DSLXC-11318（`ksummit.messages.9387`、`ksummit.messages.9404`，2024-06-21、2025-10-16），全文见 `raw_source.raw_json`

## 196.2 签名信任体系

- **要点**：Chehab 对 kernel.org Web of Trust 新方案表态：须保持可选加入、可随时吊销换钥并保留 GPG 密钥链与密钥聚会作后备；指出并行维护新旧两套体系将加重基础设施负担。
- **史料**：`ksummit.messages.9392`（Mauro Carvalho Chehab，2026-01-23）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9392 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以可选加入、可吊销换钥、GPG 密钥链与密钥聚会等具体机制为分析单位）；经验优先（总纲第 9 条——经验优先：以“并行维护新旧两套体系将加重基础设施负担”这一运维判断为判据）
- **辨析**：本块系 Mauro Carvalho Chehab 的表态；“须保持可选加入”为其立场，非新方案文本。
- **文献**：DSLXC-11315（`ksummit.messages.9392`，2026-01-23），全文见 `raw_source.raw_json`

## 196.3 LKML流量分流

- **要点**：Brown 澄清分流提案不影响 MAINTAINERS 中显式列出子列表的子系统（如 linux-trace-kernel），问题仅在“THE REST”通配项让 LKML 自动出现在一切补丁抄送中。Konstantin 提议把 MAINTAINERS“THE REST”改指 patches@lists.linux.dev：LKML 占 vger 流量约七成、月帖 3.3 万、日均投递约 310 万封，Gmail 配额致 5 万至 20 万封积压；新列表仅预审机器人订阅。
- **史料**：`ksummit.messages.9396`（Mark Brown，2023-11-09）、`ksummit.messages.9415`（Konstantin Ryabitsev，2023-11-06）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9396 -->` `<!-- ROW_MINE: ksummit.messages.9415 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 LKML 占 vger 流量约七成、月帖 3.3 万、日均投递约 310 万封、Gmail 积压 5 万至 20 万封这一组基础设施数据为判据）；动手者叙事（总纲第 10 条——动手者创造历史：以把 THE REST 改指 patches@lists.linux.dev 这一具体改动为分析单位）
- **辨析**：本块含 Mark Brown 的边界澄清与 Konstantin Ryabitsev 的原始 RFC 两方；四组数字为可核的基础设施实测，属本页最硬证据。
- **文献**：DSLXC-11316、DSLXC-11323（`ksummit.messages.9396`、`ksummit.messages.9415`，2023-11-09、2023-11-06），全文见 `raw_source.raw_json`

## 196.4 设备直通与fwctl

- **要点**：Bottomley 将直通争议拆为三题：跨子系统 NAK 裁决、厂商开源教育（称 LF 协助已中断，Greg 反驳其本人仍受 LF 资助做此事）、开放驱动标准；fwctl 宜留待 Plumbers 讨论。Greg KH 证实 nVidia 专有网关驱动经 misc 树时他作为维护者明确邀请网络子系统复审，并非“顺手 NAK”；支持 Kicinski 指争议实质是 nVidia 把专有网关做成可供各子系统调用的 misc 驱动。Gunthorpe 阐明 fwctl 非排他原则：固件接口须可共享或对 fwctl 阻断，以 mlx5 多用户固件为基线；fwctl 可与 EDAC 并发读计数器，但不得清零计数或独占全局清洗单元。Romanovsky 质疑“用户只关心常规工作流”论：高价购买小众硬件的用户难道就不配在自由软件中使用？挑战 Ribalda 对自由软件社区范围的界定，属直通辩论中的用户权利立场。Pinchart 举证某大型 SoC 厂商本拟开放相机栈主体，闻可经其他子系统以直通“空白支票”合入后临阵放弃；说明 V4L2 ISP 驱动允许用户态经数据缓冲传参，硬件功能须人人可用。Cameron 说明 CXL 命令可“意外移除”他机内存，破坏性控制面应由唯一实体 fabric manager 掌控、安全靠布线；同意用户态可经 VFIO 获同等权限，期望 fwctl 基础设施同样支持破坏性操作。
- **史料**：`ksummit.messages.9401`（James Bottomley，2024-07-31）、`ksummit.messages.9436`（Greg KH，2024-07-29）、`ksummit.messages.9466`（Jason Gunthorpe，2024-08-06）、`ksummit.messages.9471`（Leon Romanovsky，2024-07-25）、`ksummit.messages.9510`（Laurent Pinchart，2024-07-26）、`ksummit.messages.9519`（Jonathan Cameron，2024-07-11）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9401 -->` `<!-- ROW_MINE: ksummit.messages.9436 -->` `<!-- ROW_MINE: ksummit.messages.9466 -->` `<!-- ROW_MINE: ksummit.messages.9471 -->` `<!-- ROW_MINE: ksummit.messages.9510 -->` `<!-- ROW_MINE: ksummit.messages.9519 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：跨子系统 NAK 裁决、厂商开源教育、开放驱动标准与用户权利四题六方并置）；法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：直通之争落在厂商可独占控制面与用户可自由使用的边界上）
- **辨析**：六条分属 2024-07/08 同一激辩的多方；Greg KH 的“明确邀请网络子系统复审，并非顺手 NAK”为对指控的一手否认；Pinchart 的“某大型 SoC 厂商闻可经直通合入后临阵放弃”为匿名个案，落书须保留其不可核验性；Cameron 的 CXL 破坏性控制面归属属机制层论证。
- **文献**：DSLXC-11317、DSLXC-11327、DSLXC-11333、DSLXC-11337、DSLXC-11347、DSLXC-11351（`ksummit.messages.9401`、`ksummit.messages.9436`、`ksummit.messages.9466`、`ksummit.messages.9471`、`ksummit.messages.9510`、`ksummit.messages.9519`，2024-07-31、2024-07-29、2024-08-06、2024-07-25、2024-07-26、2024-07-11），全文见 `raw_source.raw_json`

## 196.5 C字符串API清理

- **要点**：Kees 赞同复杂拼接用 seq_buf（兼具长度计数与 NUL 终止），但认为剩余 strncpy 用例由 strscpy、strtomem、kmemdup_nul、memcpy 覆盖更省开销，回应 Hellwig“替换助手引入更多 bug”之虑。
- **史料**：`ksummit.messages.9407`（Kees Cook，2023-10-19）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9407 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 seq_buf、strscpy、strtomem、kmemdup_nul、memcpy 等具体 API 的取舍为分析单位）；经验优先（总纲第 9 条——经验优先：以“复杂拼接兼具长度计数与 NUL 终止”这一技术特性为判据）
- **辨析**：本块系 Kees Cook 对 Hellwig“替换助手引入更多 bug”之虑的回应；“更省开销”为其技术判断，非基准实测。
- **文献**：DSLXC-11319（`ksummit.messages.9407`，2023-10-19），全文见 `raw_source.raw_json`

## 196.6 Rust政策争论

- **要点**：Ojeda 驳斥 Anvin“Rust 独占代码推迟至 2034”论：引 Clang 起步仅支持单一版本后逐步放宽的先例（2020 Plumbers 表决），Android 与 Asahi 已可用，约束在“删 C”而非“加 Rust”。
- **史料**：`ksummit.messages.9408`（Miguel Ojeda，2025-02-19）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9408 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：Rust 独占代码推迟至 2034 之说与 Clang 逐步放宽的先例并置）；经验优先（总纲第 9 条——经验优先：以 2020 Plumbers 表决、Android 与 Asahi 已可用等可核事实为判据）
- **辨析**：本块系 Miguel Ojeda 的驳斥；“约束在删 C 而非加 Rust”为其核心澄清，属对既有争论的定位订正。
- **文献**：DSLXC-11320（`ksummit.messages.9408`，2025-02-19），全文见 `raw_source.raw_json`

## 196.7 回归修复规则

- **要点**：Pinchart 支持提醒补丁标注 Fixes 与 Cc:stable，但反对把回移 stable 设为维护者强制义务，理由是维护者倦怠已重；主张先查清修复未及时进入 stable 的原因并以工具降负。Leemhuis 给出实测：6.7.2 含 640 项变更而用户仅约 4 天测试窗（94 个带 stable 标签、630 个带 Fixes:），6.9.3 的 427 项同样不足 4 天；称 6.9 起已延后回移但执行不齐。
- **史料**：`ksummit.messages.9410`（Laurent Pinchart，2024-06-13）、`ksummit.messages.9454`（Thorsten Leemhuis，2024-06-20）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9410 -->` `<!-- ROW_MINE: ksummit.messages.9454 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“6.7.2 含 640 项变更而用户仅约 4 天测试窗（94 个带 stable 标签、630 个带 Fixes:）、6.9.3 的 427 项同样不足 4 天”这一实测为判据）；苦难不值得被提倡（总纲第 14 条——苦难不值得被提倡：反对把回移 stable 设为强制义务，理由是维护者倦怠已重）
- **辨析**：Leemhuis 的两组统计为可复算的量化证据，属本块核心；Pinchart 的“先查清原因并以工具降负”为方法论主张。
- **文献**：DSLXC-11321、DSLXC-11329（`ksummit.messages.9410`、`ksummit.messages.9454`，2024-06-13、2024-06-20），全文见 `raw_source.raw_json`

## 196.8 AI审查实践

- **要点**：Levin 披露已用 AI 审查发往 stable 的回移植补丁，拦下多起本会混入 LTS 的问题；尚缺判断 cherry-pick 到旧树是否正确，正缓慢扩展 Sashiko 工具并给出示例站点。Hemminger 以自用 AI 补写测试的体会支持 Bottomley 的判断：AI 代码错误并不隐蔽，多因缺乏上下文而完全不可用，跨环境移植尤甚；引文并含 AI 置信度评分提议与微软三成代码由 AI 编写的报道。Bottomley 说明 SCSI 出现 Sashiko AI 审查后因无专列而抄送 ksummit 征集驱动维护者反馈，愿保留 workflows 抄送但担心其覆盖面不足。
- **史料**：`ksummit.messages.9413`（Sasha Levin，2026-07-16）、`ksummit.messages.9423`（Stephen Hemminger，2025-08-05）、`ksummit.messages.9533`（James Bottomley，2026-07-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9413 -->` `<!-- ROW_MINE: ksummit.messages.9423 -->` `<!-- ROW_MINE: ksummit.messages.9533 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 AI 审查回移植补丁、Sashiko 工具扩展、置信度评分提议等具体实践为分析单位）；经验优先（总纲第 9 条——经验优先：以“已拦下多起本会混入 LTS 的问题”与“AI 代码多因缺乏上下文而完全不可用”等实际经验为判据）
- **辨析**：三条为不同发言人的 AI 审查实践；“微软三成代码由 AI 编写”系报道转引，落书须标明来源；Bottomley 的 workflows 抄送覆盖面之虑本页未见答复。
- **文献**：DSLXC-11322、DSLXC-11324、DSLXC-11356（`ksummit.messages.9413`、`ksummit.messages.9423`、`ksummit.messages.9533`，2026-07-16、2025-08-05、2026-07-22），全文见 `raw_source.raw_json`

## 196.9 linus-next测试树

- **要点**：Leemhuis 赞同 Kees“改进 linux-next 而非另立 linus-next”，披露 CI 人员希望 regzbot 监控发往 Linus 的 PR 并自动通报未修复回归，他认可但优先级不高，另拟补 -next 二分指南。
- **史料**：`ksummit.messages.9430`（Thorsten Leemhuis，2024-10-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9430 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 regzbot 监控发往 Linus 的 PR 并自动通报、补 -next 二分指南等具体机制为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：改进 linux-next 与另立 linus-next 两条路线并置）
- **辨析**：本块系 Thorsten Leemhuis 的附议与披露；“优先级不高”表明该动议为搁置中的待办。
- **文献**：DSLXC-11325（`ksummit.messages.9430`，2024-10-22），全文见 `raw_source.raw_json`

## 196.10 Rust别名模型争论

- **要点**：Overstreet 回应 Torvalds“避免 unsafe UB”请求：unsafe 本用于编译器无法检查处，禁用别名优化将拖累 vec、链表等底层结构；认为 tree borrows 提供可行模型，FFI 边界默认关闭别名优化。Ryhl 认为对 Rust 未定别名模型的担忧夸大：unsafe 别名操作仅三类——确定允许、确定 UB、尚未决定；完整模型只是消除第三类，实践守住第一类即可，回应 Ventura Jack 的质疑。
- **史料**：`ksummit.messages.9432`（Kent Overstreet，2025-02-25）、`ksummit.messages.9503`（Alice Ryhl，2025-02-25）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9432 -->` `<!-- ROW_MINE: ksummit.messages.9503 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：禁用别名优化将拖累底层结构的顾虑与“三类 unsafe 别名操作”的模型划界并置）；动手者叙事（总纲第 10 条——动手者创造历史：以 tree borrows 与 FFI 边界默认关闭别名优化等具体机制为分析单位）
- **辨析**：两条均系对 Torvalds 请求的回应；Ryhl 的“完整模型只是消除第三类”为对担忧程度的定量化界定，属本页模型讨论的关键澄清。
- **文献**：DSLXC-11326、DSLXC-11343（`ksummit.messages.9432`、`ksummit.messages.9503`，2025-02-25、2025-02-25），全文见 `raw_source.raw_json`

## 196.11 工具生成内容准则

- **要点**：Hansen 提交 TAB 集体起草的 generated-content.rst v5：要求透明披露所用工具与提示词，提交者须能捍卫全部内容，维护者可不经详审拒绝；v4 增补 Lorenzo 的“AI slop”条款，获多位维护者签署。Pinchart 支持 Stoakes 的强硬措辞：AI 垃圾补丁已被多人目击且不会自行消失；文档价值在约束善意者并为维护者撑腰，另观察到维护者担心被强制或架空，疑为信任侵蚀。
- **史料**：`ksummit.messages.9447`（Dave Hansen，2026-01-13）、`ksummit.messages.9518`（Laurent Pinchart，2026-01-09）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9447 -->` `<!-- ROW_MINE: ksummit.messages.9518 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 generated-content.rst v5 的透明披露、提交者须能捍卫、维护者可不经详审拒绝等条款为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：强硬措辞与“维护者担心被强制或架空”的顾虑并置）
- **辨析**：Hansen 提交的 v5 全文为内核应对 AI 生成内容的首份正式准则文本，属核心一手；Pinchart 的“疑为信任侵蚀”为其观察判断，非结论。
- **文献**：DSLXC-11328、DSLXC-11350（`ksummit.messages.9447`、`ksummit.messages.9518`，2026-01-13、2026-01-09），全文见 `raw_source.raw_json`

## 196.12 Rust引进争论

- **要点**：Van Assche 指出 Hemminger 的 GCC cleanup 属性示例有误——传给 free 的是局部变量指针而非其值，必然崩溃；并主张引入 C++：RAII、lambda、std::span 与类型安全回调是 C 宏无法实现的。Pinchart 认为 Rust 顾虑多为建设性反馈而非“惰性”：建议设支持渠道由 rust-in-linux 维护者协助受全树重构影响者，既回应关切又展示能力；认同 Rust 有助吸引不同背景开发者。
- **史料**：`ksummit.messages.9457`（Bart Van Assche，2021-07-07）、`ksummit.messages.9507`（Laurent Pinchart，2022-06-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9457 -->` `<!-- ROW_MINE: ksummit.messages.9507 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 cleanup 属性示例的错误定位、RAII/lambda/std::span 等 C++ 特性为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：引入 C++ 的主张与“Rust 顾虑多为建设性反馈”的判断并置）
- **辨析**：Van Assche 的“传给 free 的是局部变量指针而非其值，必然崩溃”为可核的代码事实；Pinchart 的“建议设支持渠道由 rust-in-linux 维护者协助”为提案。
- **文献**：DSLXC-11330、DSLXC-11346（`ksummit.messages.9457`、`ksummit.messages.9507`，2021-07-07、2022-06-22），全文见 `raw_source.raw_json`

## 196.13 回归追踪机器人

- **要点**：Brown 就回归机器人设计提醒：自动化系统捕捉的问题常因上报流程竞态被重复报告，去重可能成为麻烦，部分或可自动化；系对 Leemhuis regzbot 方案的早期反馈。
- **史料**：`ksummit.messages.9458`（Mark Brown，2021-04-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9458 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以自动化系统去重与竞态处理这一具体设计问题为分析单位）；经验优先（总纲第 9 条——经验优先：以“自动化系统捕捉的问题常因上报流程竞态被重复报告”这一经验为判据）
- **辨析**：本块系 Mark Brown 对 regzbot 方案的早期反馈；“去重可能成为麻烦”为其预判，本页未见实现验证。
- **文献**：DSLXC-11331（`ksummit.messages.9458`，2021-04-22），全文见 `raw_source.raw_json`

## 196.14 展开器可靠性

- **要点**：Overstreet 以自用经验称 ORC 展开器仍不可靠，需可靠调试时须把测试环境与用户切回帧指针；引文中 Rostedt 澄清内核所谓“展开”即编译器界的栈回溯。
- **史料**：`ksummit.messages.9465`（Kent Overstreet，2025-02-26）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9465 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“需可靠调试时须把测试环境与用户切回帧指针”这一自用经验为判据）；动手者叙事（总纲第 10 条——动手者创造历史：以 ORC 展开器与帧指针的对照为分析单位）
- **辨析**：本块系 Kent Overstreet 的自用经验；“ORC 展开器仍不可靠”为其判断；Rostedt 的术语澄清属转引。
- **文献**：DSLXC-11332（`ksummit.messages.9465`，2025-02-26），全文见 `raw_source.raw_json`

## 196.15 用户态开源要求

- **要点**：Chehab 反对强制驱动配开源用户态：媒体子系统若如此将阻碍 Linux 视频会议软件，许多编解码硬件仅存于本已依赖专有软件的嵌入式设备；媒体以完整文档化 uAPI 加合规工具取代强制开源。
- **史料**：`ksummit.messages.9467`（Mauro Carvalho Chehab，2021-09-10）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9467 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：强制驱动配开源用户态与媒体子系统的现实约束并置）；法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：编解码硬件仅存于依赖专有软件的嵌入式设备这一产业现实）
- **辨析**：本块系 Mauro Carvalho Chehab 的反对意见；“媒体以完整文档化 uAPI 加合规工具取代强制开源”为其替代方案，属本页用户态门槛议题的对立一方。
- **文献**：DSLXC-11334（`ksummit.messages.9467`，2021-09-10），全文见 `raw_source.raw_json`

## 196.16 C标准饱和运算

- **要点**：Overstreet 向 C 标准委员会的 Uecker 解释饱和运算用例：引用计数溢出时应饱和并保持，因不知正确值时永不释放对象最安全；回应 C23 已纳入检查算术、C2Y 或增饱和运算的讨论。
- **史料**：`ksummit.messages.9468`（Kent Overstreet，2025-02-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9468 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以引用计数溢出时应饱和并保持这一具体语义为分析单位）；经验优先（总纲第 9 条——经验优先：以“因不知正确值时永不释放对象最安全”这一安全推理为判据）
- **辨析**：本块系 Kent Overstreet 向 Uecker 的用例解释；“C23 已纳入检查算术、C2Y 或增饱和运算”为标准化进程陈述，落书须以当期标准草案核对。
- **文献**：DSLXC-11335（`ksummit.messages.9468`，2025-02-22），全文见 `raw_source.raw_json`

## 196.17 Bugzilla改革

- **要点**：Leemhuis 追问 Bugzilla 改革结论：Konstantin 反案含统一入口产品、MAINTAINERS 映射、分诊团队与“triaged”标记、后端机器人汇总通知并联动 lore；担心两案僵持致 Bugzilla 再荒废 11 个月。实际关闭者 Tashkinov 披露：每周仅约 24 份报告，其中 amdgpu 与 i915 类（各有独立追踪器）被他半自动关闭致总量近乎减半；称撰写合格报告需要经验，赞成转向邮件列表。Tashkinov 主张企业雇员维护者应处理 bug 报告；Greg 答维护者难获管理层批准、LF 仅托管不涉内容且只赞助少数开发者；Artem 指组件十余年未更新、报告常落 Other/Other 无人知晓。
- **史料**：`ksummit.messages.9469`（Thorsten Leemhuis，2022-10-17）、`ksummit.messages.9482`（Artem S. Tashkinov，2022-10-02）、`ksummit.messages.9514`（Artem S. Tashkinov，2022-09-29）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9469 -->` `<!-- ROW_MINE: ksummit.messages.9482 -->` `<!-- ROW_MINE: ksummit.messages.9514 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“每周仅约 24 份报告、amdgpu 与 i915 类被他半自动关闭致总量近乎减半”这一实际数据为判据）；法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：企业雇员维护者应否处理 bug 报告被还原为管理层批准与 LF 资助边界）
- **辨析**：三条分属 2022-09/10 同一改革讨论；Tashkinov 作为“实际关闭者”的一手披露与“组件十余年未更新、报告常落 Other/Other”为可核实况；Greg 的“维护者难获管理层批准、LF 仅托管不涉内容”为治理层说明。
- **文献**：DSLXC-11336、DSLXC-11340、DSLXC-11349（`ksummit.messages.9469`、`ksummit.messages.9482`、`ksummit.messages.9514`，2022-10-17、2022-10-02、2022-09-29），全文见 `raw_source.raw_json`

## 196.18 UMN假补丁清理

- **要点**：Romanovsky 以 sp8870 补丁 467a37fba93f 为证反驳“被回退的 29 个 media 补丁多有效”：err 检查写成 if(err) 而应为 if(err<0)，破坏寄存器读取；主张逐个检出 umn 补丁引入时点核查。
- **史料**：`ksummit.messages.9474`（Leon Romanovsky，2021-04-23）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9474 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 sp8870 补丁 467a37fba93f 中 err 检查写成 if(err) 而应为 if(err<0) 这一可核代码缺陷为判据）；动手者叙事（总纲第 10 条——动手者创造历史：以“逐个检出 umn 补丁引入时点核查”这一具体清理方法为分析单位）
- **辨析**：本块系 Leon Romanovsky 的举证与主张；467a37fba93f 为可反查的具体提交，属对“被回退的 29 个 media 补丁多有效”之说的直接反驳。
- **文献**：DSLXC-11338（`ksummit.messages.9474`，2021-04-23），全文见 `raw_source.raw_json`

## 196.19 AI补丁标注责任

- **要点**：McKenney 表态个人开发将持续回避 AI 生成产物，直至 DCO 1.1 条款 a“有权按开源许可提交”对特定模型训练来源的争议澄清；对 Generated-by 标签是否可取尚无把握。Ts'o 以非律师身份分析：维护者一贯依赖 Signed-off-by 与善意假定提交者有权提交，AI 前后皆然；个人相信责任在提交者，且从责任角度宁不知是否用 LLM。
- **史料**：`ksummit.messages.9480`（Paul E. McKenney，2025-08-11）、`ksummit.messages.9520`（Theodore Ts'o，2025-11-10）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9480 -->` `<!-- ROW_MINE: ksummit.messages.9520 -->`
- **史观**：法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：DCO 1.1 条款 a“有权按开源许可提交”与模型训练来源之争被明确为责任归属问题）；多方平等（总纲第 8 条——本体论上各方平等：持续回避 AI 生成产物与“责任在提交者”的个人判断并置）
- **辨析**：McKenney 的“直至争议澄清”与“对 Generated-by 标签是否可取尚无把握”为条件性立场；Ts'o 明示“以非律师身份分析”，其“宁不知是否用 LLM”为个人偏好，非法律意见。
- **文献**：DSLXC-11339、DSLXC-11352（`ksummit.messages.9480`、`ksummit.messages.9520`，2025-08-11、2025-11-10），全文见 `raw_source.raw_json`

## 196.20 文档可读性改进

- **要点**：Pinchart 指文档有机生长致概念先用后释、新手阅读困难，主张面向不熟读者的文档采用线性叙事；认为兼具兴趣与时间的新人重构文档可能比资深开发者更合适。
- **史料**：`ksummit.messages.9484`（Laurent Pinchart，2025-08-28）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9484 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“面向不熟读者的文档采用线性叙事”这一具体写法主张为分析单位）；经验优先（总纲第 9 条——经验优先：以“文档有机生长致概念先用后释、新手阅读困难”这一实际观察为判据）
- **辨析**：本块系 Laurent Pinchart 的主张；“新人重构文档可能比资深开发者更合适”为其判断，属人事建议。
- **文献**：DSLXC-11341（`ksummit.messages.9484`，2025-08-28），全文见 `raw_source.raw_json`

## 196.21 HIGHMEM淘汰风险

- **要点**：Walleij 回忆老 Marvell NAS 的 HIGHMEM 故障疑因 DMA 地址限制——lowmem 分配超硬件上限即数据损坏；又指 Kirkwood MMC 驱动在 !DMA 下手工遍历 sglist 而非 sg_miter()，安全性存疑。
- **史料**：`ksummit.messages.9500`（Linus Walleij，2025-09-12）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9500 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以老 Marvell NAS 的 HIGHMEM 故障疑因 DMA 地址限制、Kirkwood MMC 驱动在 !DMA 下手工遍历 sglist 等实际案例为判据）；偶然性优先（总纲第 5 条——没有必然性，只有偶然性：lowmem 分配超硬件上限即数据损坏）
- **辨析**：本块系 Linus Walleij 的回忆与存疑；“疑因 DMA 地址限制”为当事人措辞，落书不得写成已定根因；其“安全性存疑”属待查项。
- **文献**：DSLXC-11342（`ksummit.messages.9500`，2025-09-12），全文见 `raw_source.raw_json`

## 196.22 维护者支持小组

- **要点**：Shuah 称维护工作意味着情绪劳动、是倦怠风险因素，支持以 Bottomley 提案为起点，主张峰会前先开公开会议征求未获邀请者（含自己）意见，并认可 TAB 起草沟通风格文档。
- **史料**：`ksummit.messages.9504`（Shuah，2023-09-20）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9504 -->`
- **史观**：苦难不值得被提倡（总纲第 14 条——苦难不值得被提倡：维护工作意味着情绪劳动、是倦怠风险因素）；动手者叙事（总纲第 10 条——动手者创造历史：以“峰会前先开公开会议征求未获邀请者意见”这一具体程序为分析单位）
- **辨析**：本块系 Shuah 的表态；“含自己”表明其属未获邀请者；其认可 TAB 起草沟通风格文档为附议。
- **文献**：DSLXC-11344（`ksummit.messages.9504`，2023-09-20），全文见 `raw_source.raw_json`

## 196.23 cleanup.h变量放置

- **要点**：Rostedt 响应 Torvalds 对 __free 变量顶部声明后远处赋值的批评：承认自己惯用此式并愿改为在分配处声明，猜测后者可让提前退出免于对 NULL 调用 __free、优化更好。
- **史料**：`ksummit.messages.9505`（Steven Rostedt，2025-11-18）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9505 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“在分配处声明”这一具体写法改动为分析单位）；经验优先（总纲第 9 条——经验优先：以“可让提前退出免于对 NULL 调用 __free、优化更好”这一技术推测为判据）
- **辨析**：本块系 Steven Rostedt 的自我修正；“猜测后者……优化更好”明示为推测，落书不得写成已验证结论。
- **文献**：DSLXC-11345（`ksummit.messages.9505`，2025-11-18），全文见 `raw_source.raw_json`

## 196.24 峰会提问形式

- **要点**：Rostedt 支持 Wilcox 提议演讲环节由主持人从官方聊天平台遴选提问，认为不适用于 BoF 与微会议，并建议为未带设备者设公共笔记本提交问题，属 2021 峰会形式讨论。
- **史料**：`ksummit.messages.9511`（Steven Rostedt，2021-06-10）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9511 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“由主持人从官方聊天平台遴选提问”“为未带设备者设公共笔记本”等具体安排为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：演讲环节与 BoF、微会议的适用差异被明确区分）
- **辨析**：本块系 Steven Rostedt 的附议与补充，属 2021 峰会形式讨论，本页未见最终采纳。
- **文献**：DSLXC-11348（`ksummit.messages.9511`，2021-06-10），全文见 `raw_source.raw_json`

## 196.25 TAB选举投票

- **要点**：Abbott 解释 TAB 选举 CIVS 投票问题：曾向全体投票人名单补发说明，Hansen 未收选票或因垃圾邮件过滤或 Gmail 限流所致，记录 TAB 选举送达故障与补救。
- **史料**：`ksummit.messages.9521`（Laura Abbott，2021-09-20）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9521 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“Hansen 未收选票或因垃圾邮件过滤或 Gmail 限流所致”这一实际故障为判据）；动手者叙事（总纲第 10 条——动手者创造历史：以“向全体投票人名单补发说明”这一补救措施为分析单位）
- **辨析**：本块系 Laura Abbott 的故障解释；“或因”表明成因为推测，落书须保留其未定性质。
- **文献**：DSLXC-11353（`ksummit.messages.9521`，2021-09-20），全文见 `raw_source.raw_json`

## 196.26 原子内存序讨论

- **要点**：Torvalds 断言编译器内存序支持几乎必有 bug；内核可在包装器中修正遗漏，编译器出错时仍将依赖包装器，回应依赖显式屏障还是编译器原子语义之争。
- **史料**：`ksummit.messages.9525`（Linus Torvalds，2025-02-27）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9525 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“编译器内存序支持几乎必有 bug”这一长期观察为判据）；动手者叙事（总纲第 10 条——动手者创造历史：以“内核可在包装器中修正遗漏”这一具体兜底机制为分析单位）
- **辨析**：本块系 Linus Torvalds 的断言；“几乎必有 bug”为经验判断，其“编译器出错时仍将依赖包装器”为条件性结论。
- **文献**：DSLXC-11354（`ksummit.messages.9525`，2025-02-27），全文见 `raw_source.raw_json`

## 196.27 引用过多自动提醒

- **要点**：Morton 倡议机器人自动提醒过度引用邮件：因拒收会误伤合法邮件而选择“提醒发件人”并附礼节链接；自述厌倦逐封私下劝导，请 Konstantin 在 subspace.kernel.org 增设礼节页。
- **史料**：`ksummit.messages.9530`（Andrew Morton，2023-10-24）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9530 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“机器人自动提醒并附礼节链接”这一具体机制为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：拒收会误伤合法邮件与提醒发件人两法之间被明确权衡）
- **辨析**：本块系 Andrew Morton 的倡议；“自述厌倦逐封私下劝导”为一手动因，其请 Konstantin 增设礼节页为具体请求。
- **文献**：DSLXC-11355（`ksummit.messages.9530`，2023-10-24），全文见 `raw_source.raw_json`
