# 137. bugzilla 迁移之辩、AI 标注规则与 Rust 正反（ks p1）（ks p1）

> 来源：ksummit 独有 p1（50 封全读，2021-04 至 2026-08，bugzilla Harmony 迁 Postgres 提议、Luck AI 两条规则（禁 AI 直接署名/人类负全责）、Rust for Linux 正反（rustc_codegen_gcc/测试矩阵翻倍）、文件系统 RO 信任之辩（Wilcox ext4 一周修 vs HFS+ 潜伏多年）、HIGHMEM 退场与 VMSPLIT_3G_OPT、Linus 批 C 聚合 UB、峰会停办成本核算 2500 美元/人/天）
> 判定：44 CAND / 6 NV。主题分布：bugzilla Blues 讨论 3、cdev/devm_* 问题（Rust 话题） 1、强制 API 弃用 1、文件系统信任与维护 4、设备直通有害论 2、TAB 选举投票程序 1、CONFIG_HIGHMEM 退场共识 1、MAINTAINERS 条目校验 1、NVMe SCC 拷贝卸载议题 1、Rust for Linux 2、C 聚合值传递（Rust 政策） 3、AI 辅助代码补丁标注 2、替换 Link 尾注 1、trivial 补丁接收政策 2、安全 embargo 处理 1、应对新开发者洪流 2、LLM 相关议题：标签与新丁 1、拒收补丁的透明度 1、扩展安全流程 1、内核文档能做什么 1、功能纳入与移除的形式化 2、2021 峰会筹备 1、维护者峰会是否停办 1、“THE REST”迁出 LKML 1、回归跟踪机器人提案 1、UALink 驱动上游化 1、trivial 补丁接收政策（umn 事件） 1、cleanup.h 变量声明位置 1、驱动 probe 失败仍注册 1、维护者倦怠 1、回归治理四提案共同场景 1。

## 137.1 bugzilla Blues 讨论

- 【Linux社区】Geert 反驳 bugzilla 拥趸：MAINTAINERS 文件才是权威指引，优先 B 条目否则退回 M/L 条目，邮件列表经 lore 存档可追溯而 IRC 等渠道无溯源。 `<!-- ROW_MINE: ksummit.messages.2 -->`
- 【Linux社区】Tarreau 论证邮件可回应旧信并保留全部参与者而 issue 状态反藏信息，并指出 Artem 拒绝听取论点、建议停止争论。 `<!-- ROW_MINE: ksummit.messages.95 -->`
- 【Linux社区】Konstantin 答复 Bugzilla Harmony 缺乏势头，kernel.org 方案是把数据库迁移到 Postgres 以绕开 MySQL 老旧问题。 `<!-- ROW_MINE: ksummit.messages.102 -->`

## 137.2 cdev/devm_* 问题（Rust 话题）

- 【Linux社区】Dan Carpenter 称对细节不熟，但只要给出有 bug 的代码样例与期望告警输出，他就能写出对应静态检查，属具体承接承诺。 `<!-- ROW_MINE: ksummit.messages.27 -->`

## 137.3 强制 API 弃用

- 【Linux社区】Bartosz 反驳 Linus“全有或全无”立场：主张以提示告知旧 API 正被替代，支持愿意做重活的新开发者引导后续开发而不指责。 `<!-- ROW_MINE: ksummit.messages.28 -->`

## 137.4 文件系统信任与维护

- 【Linux社区】Sandeen 反对把濒死文件系统改只读：反增开发与测试负担，syzbot 照样能打崩只读文件系统，建议按惯例用 Kconfig/printk 标注弃用。 `<!-- ROW_MINE: ksummit.messages.32 -->`
- 【Linux社区】Wilcox 强调文件系统开发者极怕吃掉用户数据，以 ext4 1KB 块 bug 一周内发现修复为例，对比 HFS+ 无测试套件时 bug 可能潜伏多年。 `<!-- ROW_MINE: ksummit.messages.50 -->`
- 【Linux社区】Chinner 论证旧文件系统与 ia64 同理应可 EOL：零星用户不值维护开销、VM 跑旧发行版即可取数据，难题在 VFS/块层等接口债务而非仅 buffer cache。 `<!-- ROW_MINE: ksummit.messages.161 -->`
- 【Linux社区】Rostedt 补充旧内核难编译、旧 OS 难获取的现实约束，主张以只读为最低支持形态（如当年 NTFS）作为弃用中间站。 `<!-- ROW_MINE: ksummit.messages.168 -->`

## 137.5 设备直通有害论

- 【Linux社区】Ribalda 主张 ISP 数十万参数中仅需文档化运行时用到的数百个，以“可用开源相机栈”为底线；专利流氓风险使厂商不敢公开内部实现。 `<!-- ROW_MINE: ksummit.messages.40 -->`
- 【Linux社区】Gunthorpe 反驳 JJB：DPDK 并非小众且承载大量互联网流量，部署改用 RDMA raw queue pairs 大幅降低负担，证明并非一切都该收进内核。 `<!-- ROW_MINE: ksummit.messages.51 -->`

## 137.6 TAB 选举投票程序

- 【Linux社区】Laura 公布投票与提名资格认定同用的 Kees identity-canonicalizer 脚本及 git log/awk 命令，属 2021 TAB 选举流程记录。 `<!-- ROW_MINE: ksummit.messages.45 -->`

## 137.7 CONFIG_HIGHMEM 退场共识

- 【Linux社区】Arnd 建议 SAMA7D65 这类 1GB 机型长期默认 VMSPLIT_3G_OPT 并关闭 highmem，指出小 highmem 区更易耗尽，并追问 AT91RM9200 实际用户量。 `<!-- ROW_MINE: ksummit.messages.48 -->`

## 137.8 MAINTAINERS 条目校验

- 【Linux社区】Lee Jones 肯定 .get_maintainer.ignore 思路，追问能否表达“对我非维护者的文件不再 CC 我”，以摆脱历年改过文件的琐碎 review。 `<!-- ROW_MINE: ksummit.messages.52 -->`

## 137.9 NVMe SCC 拷贝卸载议题

- 【Linux社区】JJB 判定该议题的 plumbing 部分更适合 LSF/MM 的 IO 轨道而非 Plumbers 的 kernel summit 轨道，属议题安排建议。 `<!-- ROW_MINE: ksummit.messages.77 -->`

## 137.10 Rust for Linux

- 【Linux社区】Walleij 确认 rustc_codegen_gcc 证明可行，但认为部分因许可问题仍需为 GCC 从零编写 Rust 前端。 `<!-- ROW_MINE: ksummit.messages.92 -->`
- 【Linux社区】Leon 提出两点反方论据：多语言妨碍跨子系统重构（如 DMA/SG 改动），编译与验证测试矩阵翻倍且成本高、不如投入覆盖率。 `<!-- ROW_MINE: ksummit.messages.117 -->`

## 137.11 C 聚合值传递（Rust 政策）

- 【Linux社区】Pinchart 以 std::string 移动语义示例论证按值传聚合有时更高效，并指出 return std::move 妨碍 NRVO 与 C++17 强制拷贝消除的关系。 `<!-- ROW_MINE: ksummit.messages.94 -->`
- 【Linux社区】Linus 强调谈的是普通无注解访问：内核被迫加大量 READ_ONCE 只为应付 UBSAN，属悲观代码生成并浪费人力，根子在坏 C 标准。 `<!-- ROW_MINE: ksummit.messages.150 -->`
- 【Linux社区】Linus 长文批评 C 标准拥抱 UB：strict aliasing 与整数溢出对实际代码生成影响甚微却引入安全隐患，内核尽量关闭，VLIW 不会实用。 `<!-- ROW_MINE: ksummit.messages.198 -->`

## 137.12 AI 辅助代码补丁标注

- 【Linux社区】Greg KH 以封闭系统团队不把代码喂给公开模型、也不让公开模型产出进入闭源库为佐证，主张在法律问题明朗前认真对待风险。 `<!-- ROW_MINE: ksummit.messages.96 -->`
- 【Linux社区】Luck 提议两条规则：禁止 AI 代理直接署名提交，From 行的人类须对补丁内容负全责、不得以“AI 写的”开脱。 `<!-- ROW_MINE: ksummit.messages.158 -->`

## 137.13 替换 Link 尾注

- 【Linux社区】Dan Williams 提出以 git notes 作元数据存放处并设想 b4 dig 沿 Link 找源树、patch-id 匹配兜底，回应 Greg 的跨子系统检索难题。 `<!-- ROW_MINE: ksummit.messages.106 -->`

## 137.14 trivial 补丁接收政策

- 【Linux社区】Pinchart 提议基于 lore 与 b4 做工具，让被漏 CC 者能快速取回整个补丁系列的完整上下文。 `<!-- ROW_MINE: ksummit.messages.107 -->`
- 【Linux社区】Konstantin 反对 karma 系统：易被滥用与冒充（典型 From 伪造手法），主张仅限子维护者层级内使用，理想前提是密码学补丁证明。 `<!-- ROW_MINE: ksummit.messages.135 -->`

## 137.15 安全 embargo 处理

- 【Linux社区】Buczek 以研究院 456 用户、6PB、长任务难重启的环境自述，说明依赖 oss-security/linux-distros 公告做热修补，呼吁鼓励报送并可放宽期限。 `<!-- ROW_MINE: ksummit.messages.111 -->`

## 137.16 应对新开发者洪流

- 【Linux社区】Brown 表态 base-commit 平时用不上但难应用时很有用、宜由工具提供；要求 cover letter 写前置系列的 lore 链接加标题便于直接阅读。 `<!-- ROW_MINE: ksummit.messages.112 -->`
- 【Linux社区】Pinchart 提出用前置系列 message-id 表达依赖，指出 prerequisite-message-id trailer 已有实例并追问 lore patch-id 检索可行性。 `<!-- ROW_MINE: ksummit.messages.154 -->`

## 137.17 LLM 相关议题：标签与新丁

- 【Linux社区】Sasha 主张按 merits 而非工具审查补丁，认为维护者短缺是历届峰会老问题，应补工具与测试而非封堵使用 LLM 的开发者。 `<!-- ROW_MINE: ksummit.messages.121 -->`

## 137.18 拒收补丁的透明度

- 【Linux社区】Linus 拒绝讨论假设情形：俄罗斯事件式拒收国家支持者的补丁已有先例，未来情形无法预测，不值得争论。 `<!-- ROW_MINE: ksummit.messages.126 -->`

## 137.19 扩展安全流程

- 【Linux社区】Sasha 提出峰会议题五问：security@ 拆分 AI 分诊与人工修复、stable 回移缺位、发行版联合 backport 列表、CVE 状态标注、AI 报告政策。 `<!-- ROW_MINE: ksummit.messages.127 -->`

## 137.20 内核文档能做什么

- 【Linux社区】Brown 指出 -next 新增文档警告已有报告，建议把文档检查纳入 0day 等构建机器人以扩大覆盖面。 `<!-- ROW_MINE: ksummit.messages.139 -->`

## 137.21 功能纳入与移除的形式化

- 【Linux社区】Ted 质疑 JJB 的矛盾：保留现行拉取体系则决策自然归于上层维护者单人，要求澄清“多人决策”如何落地。 `<!-- ROW_MINE: ksummit.messages.140 -->`
- 【Linux社区】Mauro 提案：由接受功能的子系统维护者宣布移除、知会范围扩至发行版与 TAB，并以多 SOB 的移除补丁作为文档载体。 `<!-- ROW_MINE: ksummit.messages.155 -->`

## 137.22 2021 峰会筹备

- 【Linux社区】Rostedt 响应分组主持设想：可由其他子系统志愿者主持，并自荐主持 GPU 分组且保持克制，属峰会组织讨论记录。 `<!-- ROW_MINE: ksummit.messages.151 -->`

## 137.23 维护者峰会是否停办

- 【Linux社区】Pinchart 核算 43 人约 2500 美元每人每天，并提议峰会为独立邀请制活动，可另择附近低成本场地办会。 `<!-- ROW_MINE: ksummit.messages.152 -->`

## 137.24 “THE REST”迁出 LKML

- 【Linux社区】Greg KH 展示 get_maintainer.pl 默认给 USB 子系统补丁追加 LKML 的问题，支持改默认让工具不再自动指向 LKML。 `<!-- ROW_MINE: ksummit.messages.157 -->`

## 137.25 回归跟踪机器人提案

- 【Linux社区】Iwai 支持 CC regressions@ 使回归集中可见，并追问 regzbot 能否引用发行版 bug tracker 的报告。 `<!-- ROW_MINE: ksummit.messages.160 -->`

## 137.26 UALink 驱动上游化

- 【Linux社区】Dan Williams 建议将 UALink 议题同时提交 LPC 设备内存微会议，该房间有 CXL、HMM、NUMA 等相关经验人群。 `<!-- ROW_MINE: ksummit.messages.163 -->`

## 137.27 trivial 补丁接收政策（umn 事件）

- 【Linux社区】Leon 反问 Mauro：29 个 media 补丁多属有效时，是否该反思正确修法应在 pm_runtime_get_sync 层，直指评审盲点。 `<!-- ROW_MINE: ksummit.messages.164 -->`

## 137.28 cleanup.h 变量声明位置

- 【Linux社区】Linus 表态不鼓励但不禁止自动类型：分配场景重复类型无价值、中部声明合理，helper 宏内最适合。 `<!-- ROW_MINE: ksummit.messages.172 -->`

## 137.29 驱动 probe 失败仍注册

- 【Linux社区】Greg KH 解释 2.5 时代驱动模型设计意图：probe 与模块注册相互独立、probe 失败不应阻止加载，判定无需列为 tech topic。 `<!-- ROW_MINE: ksummit.messages.183 -->`

## 137.30 维护者倦怠

- 【Linux社区】Pinchart 提出匿名反馈方法论：多源汇总、只报要点、过滤非建设性意见，但依赖足够大的样本池。 `<!-- ROW_MINE: ksummit.messages.194 -->`

## 137.31 回归治理四提案共同场景

- 【Linux社区】JJB 论证 stable 兼具修复发布与回归发现双重角色，故 stable 零回归不可能，建议强化 stable 回归定位工具并讨论 -rc stable 扩容。 `<!-- ROW_MINE: ksummit.messages.199 -->`
