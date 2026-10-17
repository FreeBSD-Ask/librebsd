# 157 【Linux社区】linuxnext流程与Bugzilla存废

> 来源：ksummit 独有 p21（50 封全读，2021-07 至 2025-09：Leemhuis 完整重发 bugzilla.kernel.org 整改计划附 MAINTAINERS 约 2500 条目仅约 20 条指向 Bugzilla 实测；Kees Cook 给出 2018-2024 六年 TAB 选举投票率序列 2024 年 229/934=24.5%；Sasha Levin 以 80%/70%/85% 三组统计论证 Fixes/Stable 标签语义失灵并提出 Improves 标签；Chris Mason 披露维护者峰会年成本约 2.5 万美元与赞助断档；linux-next 流程六封、Rust 内核迁移、AI 评审与政策、HIGHMEM 淘汰争议、内核密钥管理与安全禁运流程）
> 判定：42 CAND / 8 NV。主题分布：linux-next流程 6、AI生成内容政策 2、贡献者信任 2、HIGHMEM淘汰争议 3、Bugzilla存废 4、Rust内核迁移 3、Link标签存废 1、AI评审与政策 4、文档工具链 3、TAB选举 2、安全禁运流程 1、峰会存续资金 1、社区健康资源 1、ISP框架争论 1、稳定分支标签 2、内核密钥管理 2、用户态开放要求 2、维护者列表改革 1、GitLab工作流 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p21 的逐封提取（2021-07 至 2025-09，42 CAND / 8 NV），全 19 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 157.1 linux-next流程

- 【Linux社区】Greg KH称DRM在分支间cherry-pick造成的重复提交混乱已被其多次指出，追踪stable回移令其抓狂；引Krzysztof例证Intel提交对象97b67847在linux-next中缺失。 `<!-- ROW_MINE: ksummit.messages.3198 -->`
- 【Linux社区】Roeck述实践：补丁先在-next停留数日再向Linus发PR以借外部测试；称linux-next问题太多无法全追、报告常被无视，Cc Linus响应更快，其fixes分支曾被Linus直接拉取。 `<!-- ROW_MINE: ksummit.messages.3224 -->`
- 【Linux社区】Levin写脚本核查PR补丁是否抄送列表及在-next的停留时长，首个样本即命中：KVM arm64提交afa9b48f327c从未上lore也未进-next，Linus仍照常拉取。 `<!-- ROW_MINE: ksummit.messages.3244 -->`
- 【Linux社区】Leemhuis提议为各-fixes树定“不rebase”政策并用脚本定期合并成树，可提前发现并解决冲突，但仅在合并窗口外有效，且Linus仍要求在PR时可见。 `<!-- ROW_MINE: ksummit.messages.3263 -->`
- 【Linux社区】Leitao提议维护者-next树保持稳定且只追加的历史，使linux-next用户与测试者可引用固定提交，避免history重写令已有commit消失。 `<!-- ROW_MINE: ksummit.messages.3287 -->`
- 【Linux社区】Pinchart追问Rostedt：多个topic分支是否各自向Linus发PR、聚合10人系列时merge还是cherry-pick；Rostedt称跨分支依赖时apply到一支再merge并详注原因，Linus未表异议。 `<!-- ROW_MINE: ksummit.messages.3335 -->`

## 157.2 AI生成内容政策

- 【Linux社区】Rostedt主张工具生成内容指南面向诚实贡献者而非垃圾发送者，反对语气强硬化，称若恶化可另立专门的AI文档；并引Phoronix与Register对Linus AI slop表态的报道。 `<!-- ROW_MINE: ksummit.messages.3199 -->`
- 【Linux社区】Torvalds回应Rapoport“AI能从零大规模生成代码”之说，称这只是程度变化而非根本变化，既有工具产出规则原样适用，是其AI政策的关键一手表态。 `<!-- ROW_MINE: ksummit.messages.3215 -->`

## 157.3 贡献者信任

- 【Linux社区】Petersen支持用lore等自动统计陌生贡献者历史以辅助判断，但反对把数字压成一维“信任等级”以免被刷分，并建议统计该人提交所获Fixes引用数量。 `<!-- ROW_MINE: ksummit.messages.3201 -->`
- 【Linux社区】Myklebust称最大问题不是补丁庞大，而是提交者不懂子系统并与AI一起夸大重要性，涌现大量夸大的“安全漏洞”抄送stable，侵占维护者日程并造成疲劳。 `<!-- ROW_MINE: ksummit.messages.3218 -->`

## 157.4 HIGHMEM淘汰争议

- 【Linux社区】hpa反问Andreas：“SPARC32是4:4地址空间，还在用HIGHMEM？”，指其方案技术前提反常，为HIGHMEM淘汰争论中针锋相对的一手立场。 `<!-- ROW_MINE: ksummit.messages.3202 -->`
- 【Linux社区】Weinberger举实例：嵌入式2G/2G地址划分曾致JRE触及地址空间上限，改回3G/1G即恢复，正面回答Hansen对非标准PAGE_OFFSET实际用户问题的追问。 `<!-- ROW_MINE: ksummit.messages.3275 -->`
- 【Linux社区】Bergmann考据Microchip旧SoC续命：SAM9x60（2020）提频600MHz但内存上限128MB，SAM9X7（2023）加DDR3至256MB，并称32位DDR3总线本可支持1GB。 `<!-- ROW_MINE: ksummit.messages.3289 -->`

## 157.5 Bugzilla存废

- 【Linux社区】Tarreau用bug 204807数据反驳：255条评论拖2.5年、首个回复18个月后才来且核心讨论集中于3天；并举自己19年未进展的GCC bug 11873，称邮件列表未必更慢。 `<!-- ROW_MINE: ksummit.messages.3203 -->`
- 【Linux社区】Leemhuis重发Bugzilla整改计划全文：设“可能无人看”的catch-all产品、隐藏未承诺跟进的组件、首页明示多数报告应走邮件；称MAINTAINERS约2500条目仅约20条指向Bugzilla，ACPI/PM的Len Brown依赖它。 `<!-- ROW_MINE: ksummit.messages.3307 -->`
- 【Linux社区】Levin介绍用LLM在服务端解码oops：据内核版本串推断发行版与包版本、拉取debuginfo后运行decode_stacktrace.sh；Pinchart斥其非确定性，Levin反问有何确定性替代方案。 `<!-- ROW_MINE: ksummit.messages.3316 -->`
- 【Linux社区】Torvalds强硬回击Artem：Bugzilla不合内核工作流也不值得投入，若你在意就该自己去花时间，“请走开，照照镜子”，是Bugzilla之争的关键一手表态。 `<!-- ROW_MINE: ksummit.messages.3324 -->`

## 157.6 Rust内核迁移

- 【Linux社区】Ojeda反驳Bottomley“Rc引用计数下Rust不比C有优势”论：即便共享所有权，Rust仍阻止UB与数据竞争，例如防止把Rc误共享给其他线程。 `<!-- ROW_MINE: ksummit.messages.3217 -->`
- 【Linux社区】Walleij称GPIO子系统已有remove后阻止消费者调用API的机制，但由其本人用C实现，Miguel已指出其中存在缺陷，回应“应由子系统而非驱动负责”之争。 `<!-- ROW_MINE: ksummit.messages.3248 -->`
- 【Linux社区】Wedson逐条回应Arnd对Rust版PL061驱动之问：dev_级pr_debug未实现故暂失设备信息、锁用spinlock_t未覆盖PREEMPT_RT、CONFIG_PM经if cfg!包裹由编译器剔除死代码。 `<!-- ROW_MINE: ksummit.messages.3272 -->`

## 157.7 Link标签存废

- 【Linux社区】hpa认可Bottomley的lore服务端dig链接或可在内核语境可行，但主张目标应是git通用工具，Message-ID本身所含信息不足以支撑。 `<!-- ROW_MINE: ksummit.messages.3231 -->`

## 157.8 AI评审与政策

- 【Linux社区】Ojeda就Sashiko提出：LTS回移评审可定制prompt且噪声更低；建议邀第二家AI公司捐token以降低单一供应商风险；称prompt开发是黑箱，交互模式宜限Gitolite权限并限流。 `<!-- ROW_MINE: ksummit.messages.3235 -->`
- 【Linux社区】Stoakes称维护者带宽本已吃紧，生成与评审能力呈不对称关系，无法承受不受控的涌入，主张赋权各子系统自行决定可接受的AI使用方式。 `<!-- ROW_MINE: ksummit.messages.3300 -->`
- 【Linux社区】Bird提议以提交注记标明补丁经过哪些工具检查，设想未来缺少“Reviewed-by: checkpatch.pl与AI评审”即可要求先补机器审再进入人工评审。 `<!-- ROW_MINE: ksummit.messages.3306 -->`
- 【Linux社区】Brown权衡Sashiko威胁模型默认值：多数子系统设备焊死在SoC且无固件，信任硬件的代码多于不信任者，默认信任方向难有两全，回应Berg与Bottomley之争。 `<!-- ROW_MINE: ksummit.messages.3309 -->`

## 157.9 文档工具链

- 【Linux社区】Ojeda认为rustdoc转ReST嵌入内核文档会丧失Rust专属导航视图等优点，或可用Sphinx插件与Rust domain复刻，但对HTML输出而言未必值得。 `<!-- ROW_MINE: ksummit.messages.3237 -->`
- 【Linux社区】Corbet指scripts/find-unused-docs.sh正是为发现未挂接kernel-doc标注而写，并重申拟将文档工具移入独立目录以提升可发现性。 `<!-- ROW_MINE: ksummit.messages.3323 -->`
- 【Linux社区】Corbet称希望尽量多开发者能自建文档，有老贡献者仍用Sphinx 1.8.5，收窄支持版本恐将人排除；承认kernel-doc正则无文档且大量重复，欢迎Heiser回归。 `<!-- ROW_MINE: ksummit.messages.3331 -->`

## 157.10 TAB选举

- 【Linux社区】Cook列出线上投票以来历年TAB投票率：2024年229/934为24.5%，2023年20.5%，2022年27.8%，2021年23.4%，2020年24.6%，2018年最后一年线下为95/95。 `<!-- ROW_MINE: ksummit.messages.3241 -->`
- 【Linux社区】Ojeda发布2025 LF TAB选举最后提醒：12月13至20日经CIVS投票，五席候选人七人为Colomar、Cong Wang、Hildenbrand、Greg KH、Kosina、Lawall、Rostedt。 `<!-- ROW_MINE: ksummit.messages.3346 -->`

## 157.11 安全禁运流程

- 【Linux社区】Levin提议要求常用禁运机制的组织提供可验证测试环境并设常设可信测试者组；Hansen称Intel内部已跑0-day但结果未并入合入材料、承诺改进；Levin指文档需律师解读。 `<!-- ROW_MINE: ksummit.messages.3253 -->`

## 157.12 峰会存续资金

- 【Linux社区】Mason向LF的Angela Brown求证：维护者峰会年成本约2.5万美元，LF无需结构调整即可继续支持；2024年仅一家赞助商、2025年无；称峰会是解决长期分歧的同步点。 `<!-- ROW_MINE: ksummit.messages.3264 -->`

## 157.13 社区健康资源

- 【Linux社区】Bottomley由Hans演讲发现维护者倦怠多靠雇主纾解而社区竟无可调用资源，提议建立志愿者邮件列表与wiki，或请LF提供定期辅导及一对一视频心理咨询。 `<!-- ROW_MINE: ksummit.messages.3270 -->`

## 157.14 ISP框架争论

- 【Linux社区】Ailus主张ISP多为专用管线、最接近使用V4L2的视频编解码器，直连传感器带来时序约束，应改进V4L2/MC或另立UAPI而非转DRM；引Pinchart指厂商借道DRM规避文档义务。 `<!-- ROW_MINE: ksummit.messages.3271 -->`

## 157.15 稳定分支标签

- 【Linux社区】Levin为“Improves标签”提案辩护：超80%带Fixes的提交终入stable；约70%有stable无Fixes的提交修旧版问题，-rc中近85%提交针对合并窗口前问题；“事后发现”模式曾压垮流程。 `<!-- ROW_MINE: ksummit.messages.3274 -->`
- 【Linux社区】Greg KH说明stable实践：仅cc:stable时尽力回移至当前stable/LTS，见“Fixes: 1da177e4c3f4 (Linux-2.6.12-rc2)”即知应更老并发FAILED邮件促成补修，故pre-git Fixes标签有价值。 `<!-- ROW_MINE: ksummit.messages.3321 -->`

## 157.16 内核密钥管理

- 【Linux社区】Bottomley反对Uwe提出的将PGP密钥有效期限制在3年内的建议，援引Linus对密钥有效期的既有批评，并称自己因此改用更长的有效期。 `<!-- ROW_MINE: ksummit.messages.3280 -->`
- 【Linux社区】Ryabitsev披露内核密钥环约600个密钥，新增常因签名缺失或离Linus信任链过远而反复沟通，扩至数千将不可维护；PGP仍为推荐签名证明机制，ssh/minisign是其他项目的高频需求。 `<!-- ROW_MINE: ksummit.messages.3282 -->`

## 157.17 用户态开放要求

- 【Linux社区】Chehab主张媒体子系统以完整文档化uAPI替代强制开源用户态，称EXPORT_SYMBOL_USERSPACE_GPL会波及普通应用；回顾OMAP3 ISP在MeeGo终止后凭公开文档合入，赞成IPU3出staging前须有libcamera支持。 `<!-- ROW_MINE: ksummit.messages.3281 -->`
- 【Linux社区】Uytterhoeven认同Jani观点：私有栈可复现而开放栈不能的缺陷不会获修，并将其归结为“先加测试用例再修bug”的老原则，即须在开放栈上增强复现能力。 `<!-- ROW_MINE: ksummit.messages.3342 -->`

## 157.18 维护者列表改革

- 【Linux社区】Raynal讨论将MAINTAINERS“THE REST”迁出LKML，指出众多无显式列表的条目并非核心子系统，建议get_maintainers.pl在无列表时回退到LKML。 `<!-- ROW_MINE: ksummit.messages.3295 -->`

## 157.19 GitLab工作流

- 【Linux社区】Zickus介绍Red Hat GitLab工作流：邮件桥统计显示极少数人用邮件、多数已迁CLI工具；已向GitLab反映无法在commit message上inline评论的短板；另有连接GitLab API的public-inbox原型。 `<!-- ROW_MINE: ksummit.messages.3333 -->`
