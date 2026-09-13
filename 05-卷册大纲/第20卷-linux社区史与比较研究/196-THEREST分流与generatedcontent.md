# 196. THE REST 分流原始 RFC、generated-content v5 准则与 Link 保险税论（ks p60）

> 来源：ksummit 独有 p60（50 封全读，2021-04 至 2026-07：Konstantin 提出 THE REST 分流 patches@ 的原始 RFC 含 LKML 占 vger 七成月帖 3.3 万日均 310 万封投递与 Gmail 积压 5-20 万封一手基础设施数据；Leemhuis 用 6.7.2/6.9.3 逐项统计 640 与 427 项变更用户测试窗不足 4 天量化回归修复未及时进 stable 漏洞；Dave Hansen 提交 TAB 集体起草 generated-content.rst v5 全文系内核应对 AI 生成内容首份正式准则文本含维护者可不经详审拒绝条款与 11 位维护者签署链；Greg KH 对以 b4 查询取代 Link 尾注系统反对书含保险税论与 LF 早年邮件溯源工具失败史；设备直通与 fwctl 六封）
> 判定：43 CAND / 7 NV。主题分布：Link尾注规范 2、签名信任体系 1、LKML流量分流 2、设备直通与fwctl 6、C字符串API清理 1、Rust政策争论 1、回归修复规则 2、AI审查实践 3、linus-next测试树 1、Rust别名模型争论 2、工具生成内容准则 2、Rust引进争论 2、回归追踪机器人 1、展开器可靠性 1、用户态开源要求 1、C标准饱和运算 1、Bugzilla改革 3、UMN假补丁清理 1、AI补丁标注责任 2、文档可读性改进 1、HIGHMEM淘汰风险 1、维护者支持小组 1、cleanup.h变量放置 1、峰会提问形式 1、TAB选举投票 1、原子内存序讨论 1、引用过多自动提醒 1。

## 196.1 Link尾注规范

- 【Linux社区】Konstantin 解释 Link 尾注中“#”之后内容仅是注释约定，格式为“Trailer 名: 正文 # 注释”，回应 Kees 对文档新增“# [1]”写法的疑问。 `<!-- ROW_MINE: ksummit.messages.9387 -->`
- 【Linux社区】Greg KH 反对以 b4 查询取代 Link 尾注：增加维护者负担、离线无法应用补丁、用户不会装 b4；预言多数人会漏加，称这一行是“保险税”，曾在稳定分支工作省下大量时间。 `<!-- ROW_MINE: ksummit.messages.9404 -->`

## 196.2 签名信任体系

- 【Linux社区】Chehab 对 kernel.org Web of Trust 新方案表态：须保持可选加入、可随时吊销换钥并保留 GPG 密钥链与密钥聚会作后备；指出并行维护新旧两套体系将加重基础设施负担。 `<!-- ROW_MINE: ksummit.messages.9392 -->`

## 196.3 LKML流量分流

- 【Linux社区】Brown 澄清分流提案不影响 MAINTAINERS 中显式列出子列表的子系统（如 linux-trace-kernel），问题仅在“THE REST”通配项让 LKML 自动出现在一切补丁抄送中。 `<!-- ROW_MINE: ksummit.messages.9396 -->`
- 【Linux社区】Konstantin 提议把 MAINTAINERS“THE REST”改指 patches@lists.linux.dev：LKML 占 vger 流量约七成、月帖 3.3 万、日均投递约 310 万封，Gmail 配额致 5 万至 20 万封积压；新列表仅预审机器人订阅。 `<!-- ROW_MINE: ksummit.messages.9415 -->`

## 196.4 设备直通与fwctl

- 【Linux社区】Bottomley 将直通争议拆为三题：跨子系统 NAK 裁决、厂商开源教育（称 LF 协助已中断，Greg 反驳其本人仍受 LF 资助做此事）、开放驱动标准；fwctl 宜留待 Plumbers 讨论。 `<!-- ROW_MINE: ksummit.messages.9401 -->`
- 【Linux社区】Greg KH 证实 nVidia 专有网关驱动经 misc 树时他作为维护者明确邀请网络子系统复审，并非“顺手 NAK”；支持 Kicinski 指争议实质是 nVidia 把专有网关做成可供各子系统调用的 misc 驱动。 `<!-- ROW_MINE: ksummit.messages.9436 -->`
- 【Linux社区】Gunthorpe 阐明 fwctl 非排他原则：固件接口须可共享或对 fwctl 阻断，以 mlx5 多用户固件为基线；fwctl 可与 EDAC 并发读计数器，但不得清零计数或独占全局清洗单元。 `<!-- ROW_MINE: ksummit.messages.9466 -->`
- 【Linux社区】Romanovsky 质疑“用户只关心常规工作流”论：高价购买小众硬件的用户难道就不配在自由软件中使用？挑战 Ribalda 对自由软件社区范围的界定，属直通辩论中的用户权利立场。 `<!-- ROW_MINE: ksummit.messages.9471 -->`
- 【Linux社区】Pinchart 举证某大型 SoC 厂商本拟开放相机栈主体，闻可经其他子系统以直通“空白支票”合入后临阵放弃；说明 V4L2 ISP 驱动允许用户态经数据缓冲传参，硬件功能须人人可用。 `<!-- ROW_MINE: ksummit.messages.9510 -->`
- 【Linux社区】Cameron 说明 CXL 命令可“意外移除”他机内存，破坏性控制面应由唯一实体 fabric manager 掌控、安全靠布线；同意用户态可经 VFIO 获同等权限，期望 fwctl 基础设施同样支持破坏性操作。 `<!-- ROW_MINE: ksummit.messages.9519 -->`

## 196.5 C字符串API清理

- 【Linux社区】Kees 赞同复杂拼接用 seq_buf（兼具长度计数与 NUL 终止），但认为剩余 strncpy 用例由 strscpy、strtomem、kmemdup_nul、memcpy 覆盖更省开销，回应 Hellwig“替换助手引入更多 bug”之虑。 `<!-- ROW_MINE: ksummit.messages.9407 -->`

## 196.6 Rust政策争论

- 【Linux社区】Ojeda 驳斥 Anvin“Rust 独占代码推迟至 2034”论：引 Clang 起步仅支持单一版本后逐步放宽的先例（2020 Plumbers 表决），Android 与 Asahi 已可用，约束在“删 C”而非“加 Rust”。 `<!-- ROW_MINE: ksummit.messages.9408 -->`

## 196.7 回归修复规则

- 【Linux社区】Pinchart 支持提醒补丁标注 Fixes 与 Cc:stable，但反对把回移 stable 设为维护者强制义务，理由是维护者倦怠已重；主张先查清修复未及时进入 stable 的原因并以工具降负。 `<!-- ROW_MINE: ksummit.messages.9410 -->`
- 【Linux社区】Leemhuis 给出实测：6.7.2 含 640 项变更而用户仅约 4 天测试窗（94 个带 stable 标签、630 个带 Fixes:），6.9.3 的 427 项同样不足 4 天；称 6.9 起已延后回移但执行不齐。 `<!-- ROW_MINE: ksummit.messages.9454 -->`

## 196.8 AI审查实践

- 【Linux社区】Levin 披露已用 AI 审查发往 stable 的回移植补丁，拦下多起本会混入 LTS 的问题；尚缺判断 cherry-pick 到旧树是否正确，正缓慢扩展 Sashiko 工具并给出示例站点。 `<!-- ROW_MINE: ksummit.messages.9413 -->`
- 【Linux社区】Hemminger 以自用 AI 补写测试的体会支持 Bottomley 的判断：AI 代码错误并不隐蔽，多因缺乏上下文而完全不可用，跨环境移植尤甚；引文并含 AI 置信度评分提议与微软三成代码由 AI 编写的报道。 `<!-- ROW_MINE: ksummit.messages.9423 -->`
- 【Linux社区】Bottomley 说明 SCSI 出现 Sashiko AI 审查后因无专列而抄送 ksummit 征集驱动维护者反馈，愿保留 workflows 抄送但担心其覆盖面不足。 `<!-- ROW_MINE: ksummit.messages.9533 -->`

## 196.9 linus-next测试树

- 【Linux社区】Leemhuis 赞同 Kees“改进 linux-next 而非另立 linus-next”，披露 CI 人员希望 regzbot 监控发往 Linus 的 PR 并自动通报未修复回归，他认可但优先级不高，另拟补 -next 二分指南。 `<!-- ROW_MINE: ksummit.messages.9430 -->`

## 196.10 Rust别名模型争论

- 【Linux社区】Overstreet 回应 Torvalds“避免 unsafe UB”请求：unsafe 本用于编译器无法检查处，禁用别名优化将拖累 vec、链表等底层结构；认为 tree borrows 提供可行模型，FFI 边界默认关闭别名优化。 `<!-- ROW_MINE: ksummit.messages.9432 -->`
- 【Linux社区】Ryhl 认为对 Rust 未定别名模型的担忧夸大：unsafe 别名操作仅三类——确定允许、确定 UB、尚未决定；完整模型只是消除第三类，实践守住第一类即可，回应 Ventura Jack 的质疑。 `<!-- ROW_MINE: ksummit.messages.9503 -->`

## 196.11 工具生成内容准则

- 【Linux社区】Hansen 提交 TAB 集体起草的 generated-content.rst v5：要求透明披露所用工具与提示词，提交者须能捍卫全部内容，维护者可不经详审拒绝；v4 增补 Lorenzo 的“AI slop”条款，获多位维护者签署。 `<!-- ROW_MINE: ksummit.messages.9447 -->`
- 【Linux社区】Pinchart 支持 Stoakes 的强硬措辞：AI 垃圾补丁已被多人目击且不会自行消失；文档价值在约束善意者并为维护者撑腰，另观察到维护者担心被强制或架空，疑为信任侵蚀。 `<!-- ROW_MINE: ksummit.messages.9518 -->`

## 196.12 Rust引进争论

- 【Linux社区】Van Assche 指出 Hemminger 的 GCC cleanup 属性示例有误——传给 free 的是局部变量指针而非其值，必然崩溃；并主张引入 C++：RAII、lambda、std::span 与类型安全回调是 C 宏无法实现的。 `<!-- ROW_MINE: ksummit.messages.9457 -->`
- 【Linux社区】Pinchart 认为 Rust 顾虑多为建设性反馈而非“惰性”：建议设支持渠道由 rust-in-linux 维护者协助受全树重构影响者，既回应关切又展示能力；认同 Rust 有助吸引不同背景开发者。 `<!-- ROW_MINE: ksummit.messages.9507 -->`

## 196.13 回归追踪机器人

- 【Linux社区】Brown 就回归机器人设计提醒：自动化系统捕捉的问题常因上报流程竞态被重复报告，去重可能成为麻烦，部分或可自动化；系对 Leemhuis regzbot 方案的早期反馈。 `<!-- ROW_MINE: ksummit.messages.9458 -->`

## 196.14 展开器可靠性

- 【Linux社区】Overstreet 以自用经验称 ORC 展开器仍不可靠，需可靠调试时须把测试环境与用户切回帧指针；引文中 Rostedt 澄清内核所谓“展开”即编译器界的栈回溯。 `<!-- ROW_MINE: ksummit.messages.9465 -->`

## 196.15 用户态开源要求

- 【Linux社区】Chehab 反对强制驱动配开源用户态：媒体子系统若如此将阻碍 Linux 视频会议软件，许多编解码硬件仅存于本已依赖专有软件的嵌入式设备；媒体以完整文档化 uAPI 加合规工具取代强制开源。 `<!-- ROW_MINE: ksummit.messages.9467 -->`

## 196.16 C标准饱和运算

- 【Linux社区】Overstreet 向 C 标准委员会的 Uecker 解释饱和运算用例：引用计数溢出时应饱和并保持，因不知正确值时永不释放对象最安全；回应 C23 已纳入检查算术、C2Y 或增饱和运算的讨论。 `<!-- ROW_MINE: ksummit.messages.9468 -->`

## 196.17 Bugzilla改革

- 【Linux社区】Leemhuis 追问 Bugzilla 改革结论：Konstantin 反案含统一入口产品、MAINTAINERS 映射、分诊团队与“triaged”标记、后端机器人汇总通知并联动 lore；担心两案僵持致 Bugzilla 再荒废 11 个月。 `<!-- ROW_MINE: ksummit.messages.9469 -->`
- 【Linux社区】实际关闭者 Tashkinov 披露：每周仅约 24 份报告，其中 amdgpu 与 i915 类（各有独立追踪器）被他半自动关闭致总量近乎减半；称撰写合格报告需要经验，赞成转向邮件列表。 `<!-- ROW_MINE: ksummit.messages.9482 -->`
- 【Linux社区】Tashkinov 主张企业雇员维护者应处理 bug 报告；Greg 答维护者难获管理层批准、LF 仅托管不涉内容且只赞助少数开发者；Artem 指组件十余年未更新、报告常落 Other/Other 无人知晓。 `<!-- ROW_MINE: ksummit.messages.9514 -->`

## 196.18 UMN假补丁清理

- 【Linux社区】Romanovsky 以 sp8870 补丁 467a37fba93f 为证反驳“被回退的 29 个 media 补丁多有效”：err 检查写成 if(err) 而应为 if(err<0)，破坏寄存器读取；主张逐个检出 umn 补丁引入时点核查。 `<!-- ROW_MINE: ksummit.messages.9474 -->`

## 196.19 AI补丁标注责任

- 【Linux社区】McKenney 表态个人开发将持续回避 AI 生成产物，直至 DCO 1.1 条款 a“有权按开源许可提交”对特定模型训练来源的争议澄清；对 Generated-by 标签是否可取尚无把握。 `<!-- ROW_MINE: ksummit.messages.9480 -->`
- 【Linux社区】Ts'o 以非律师身份分析：维护者一贯依赖 Signed-off-by 与善意假定提交者有权提交，AI 前后皆然；个人相信责任在提交者，且从责任角度宁不知是否用 LLM。 `<!-- ROW_MINE: ksummit.messages.9520 -->`

## 196.20 文档可读性改进

- 【Linux社区】Pinchart 指文档有机生长致概念先用后释、新手阅读困难，主张面向不熟读者的文档采用线性叙事；认为兼具兴趣与时间的新人重构文档可能比资深开发者更合适。 `<!-- ROW_MINE: ksummit.messages.9484 -->`

## 196.21 HIGHMEM淘汰风险

- 【Linux社区】Walleij 回忆老 Marvell NAS 的 HIGHMEM 故障疑因 DMA 地址限制——lowmem 分配超硬件上限即数据损坏；又指 Kirkwood MMC 驱动在 !DMA 下手工遍历 sglist 而非 sg_miter()，安全性存疑。 `<!-- ROW_MINE: ksummit.messages.9500 -->`

## 196.22 维护者支持小组

- 【Linux社区】Shuah 称维护工作意味着情绪劳动、是倦怠风险因素，支持以 Bottomley 提案为起点，主张峰会前先开公开会议征求未获邀请者（含自己）意见，并认可 TAB 起草沟通风格文档。 `<!-- ROW_MINE: ksummit.messages.9504 -->`

## 196.23 cleanup.h变量放置

- 【Linux社区】Rostedt 响应 Torvalds 对 __free 变量顶部声明后远处赋值的批评：承认自己惯用此式并愿改为在分配处声明，猜测后者可让提前退出免于对 NULL 调用 __free、优化更好。 `<!-- ROW_MINE: ksummit.messages.9505 -->`

## 196.24 峰会提问形式

- 【Linux社区】Rostedt 支持 Wilcox 提议演讲环节由主持人从官方聊天平台遴选提问，认为不适用于 BoF 与微会议，并建议为未带设备者设公共笔记本提交问题，属 2021 峰会形式讨论。 `<!-- ROW_MINE: ksummit.messages.9511 -->`

## 196.25 TAB选举投票

- 【Linux社区】Abbott 解释 TAB 选举 CIVS 投票问题：曾向全体投票人名单补发说明，Hansen 未收选票或因垃圾邮件过滤或 Gmail 限流所致，记录 TAB 选举送达故障与补救。 `<!-- ROW_MINE: ksummit.messages.9521 -->`

## 196.26 原子内存序讨论

- 【Linux社区】Torvalds 断言编译器内存序支持几乎必有 bug；内核可在包装器中修正遗漏，编译器出错时仍将依赖包装器，回应依赖显式屏障还是编译器原子语义之争。 `<!-- ROW_MINE: ksummit.messages.9525 -->`

## 196.27 引用过多自动提醒

- 【Linux社区】Morton 倡议机器人自动提醒过度引用邮件：因拒收会误伤合法邮件而选择“提醒发件人”并附礼节链接；自述厌倦逐封私下劝导，请 Konstantin 在 subspace.kernel.org 增设礼节页。 `<!-- ROW_MINE: ksummit.messages.9530 -->`
