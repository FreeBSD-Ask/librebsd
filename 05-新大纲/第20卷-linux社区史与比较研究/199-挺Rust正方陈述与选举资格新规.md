# 199 【Linux社区】挺Rust正方陈述与选举资格新规

> 来源：ksummit 独有 p63（50 封全读，2025-10 至 2026-08：Greg KH 以 15 年经手几乎所有 bugfix 与 CVE 的一手经验系统陈述支持 Rust 进入内核的理由多数缺陷源于 C 错误路径与 UAF 类低级错误系 2025 年 Rust 政策之争最有分量正方陈述；Christoph Hellwig 指控 Rust 政策文档不强制任何子系统被 Linus 私下越过维护者合并 Rust 证伪直接记录核心诚信争议与绑定蔓延论；Laura Abbott 公布 2021 TAB 选举新规投票资格与 Kernel Summit 脱钩改绑 3 枚提交标签合格选民扩至 4000 余人系治理里程碑；Bottomley 与 Levin 就稳定版 Improves 标签交锋含仅 stable 标签提交约 70% 修复旧版问题与 -rc 提交近 85% 处理合并窗口前问题量化数据；稳定版回迁五封）
> 判定：47 CAND / 3 NV。主题分布：峰会存废争论 2、Rust稳定性争论 1、Bugzilla邮件政策 2、设备直通争论 3、补丁基址标注 1、AI补丁审查 2、稳定版回迁 4、内核文档构建 2、提交溯源标签 3、静态分析 1、平凡补丁政策 2、C警告语义争论 1、背光控制API 1、涉密代码测试 2、审查文化 1、C内存语义 1、稳定版邮件 1、DRM面板API 1、驱动探测失败 1、Rust政策争论 2、回迁仪表盘 1、堆栈回溯术语 1、TAB选举 2、维护者支持小组 1、Rust引用计数 2、维护者分支管理 1、功能纳退机制 1、内核信任体系 1、邮件引用礼仪 1、Rust抽象布局 1、合并前测试 1。

## 199.1 峰会存废争论

- **要点**：Bottomley 指出 conclave.rst 应急预案已覆盖峰会停办情形：TAB 主席转任 $ORGANIZER，由 TAB 遴选继任会议与会者，无需新流程即可应对。Rostedt 估 AI 议题或成峰会赞助亮点，警告移赞助至 Plumbers 将现 10 万美元预算缺口，并入现有会议或恢复旧式 kernel summit 均为选项，关键在 Linus 取舍。
- **史料**：`ksummit.messages.9879`（James Bottomley，2026-08-07）、`ksummit.messages.9999`（Steven Rostedt，2026-08-06）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9879 -->` `<!-- ROW_MINE: ksummit.messages.9999 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 conclave.rst 应急预案、TAB 主席转任 $ORGANIZER 等具体制度安排为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：并入现有会议、恢复旧式 kernel summit 等停办选项并置）
- **辨析**：两条同属 2026-08 峰会存废线程；Bottomley 的应急预案为制度性一手，Rostedt 的 10 万美元赞助缺口为当事人估计，非审计数据。
- **文献**：DSLXC-11430、DSLXC-11463（`ksummit.messages.9879`、`ksummit.messages.9999`，2026-08-07、2026-08-06），全文见 `raw_source.raw_json`

## 199.2 Rust稳定性争论

- **要点**：Ventura Jack 引 time crate 破坏致 NixOS 大量协调成本及 GitHub 56 个差评，指出同一 RwLock 代码在 2021 与 2024 版下语义不同，质疑其“向后兼容承诺”。
- **史料**：`ksummit.messages.9880`（Ventura Jack，2025-02-28）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9880 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 time crate 破坏致 NixOS 协调成本、GitHub 56 个差评等实际案例为判据）；知识注定过时（总纲第 22 条——知识注定过时：同一 RwLock 代码在 2021 与 2024 版下语义不同）
- **辨析**：本块系 Ventura Jack 的质疑；“向后兼容承诺”之质问为对 Rust 官方表述的批评，其 56 个差评计数属可核的仓库快照。
- **文献**：DSLXC-11431（`ksummit.messages.9880`，2025-02-28），全文见 `raw_source.raw_json`

## 199.3 Bugzilla邮件政策

- **要点**：Viro 反驳“不喜欢就退订”论：linux-fsdevel 等列表作为收件方根本无从退订 bugzilla 邮件，指其结构性缺陷，该答复是死路。Tashkinov 总结困局：部分内核组件无对应邮件列表、群体邀约订阅难推行、收集 git log 公开邮箱或涉欧盟违法，称遭全员反对而放弃提案。
- **史料**：`ksummit.messages.9884`（Al Viro，2022-10-02）、`ksummit.messages.9981`（Artem S. Tashkinov，2022-10-02）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9884 -->` `<!-- ROW_MINE: ksummit.messages.9981 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：收件方无从退订的结构缺陷与提案遭全员反对两方并置）；法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：收集 git log 公开邮箱涉欧盟违法的合规边界）
- **辨析**：两条同属 bugzilla 邮件治理议题；Viro 指结构性缺陷为机制判断，Tashkinov 的“全员反对”系自述，其“涉欧盟违法”为推断而非法律意见。
- **文献**：DSLXC-11432、DSLXC-11459（`ksummit.messages.9884`、`ksummit.messages.9981`，2022-10-02、2022-10-02），全文见 `raw_source.raw_json`

## 199.4 设备直通争论

- **要点**：Leon Romanovsky 称“信任是双向的”，在大型子系统与复杂设备上“信任维护者”是空想；Pinchart 追问其论断范围，双方就跨子系统 NAK 信任交锋。Pinchart 质疑直通议题在维护者峰会闭门决策的正当性，主张相关子系统维护者与推动者等利益相关方应到场；自称观点偏摄像头领域。Ribalda 主张勿为 1% 高级用法牺牲 99% 标准流程，以 AMD 官方栈加 amdgpu-pro 私有用户态并存为例，呼吁共同定义“正常工作流”并给出厂商直通的通用准则。
- **史料**：`ksummit.messages.9885`（Laurent Pinchart，2024-07-22）、`ksummit.messages.9933`（Laurent Pinchart，2024-07-28）、`ksummit.messages.10050`（Ricardo Ribalda Delgado，2024-07-25）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9885 -->` `<!-- ROW_MINE: ksummit.messages.9933 -->` `<!-- ROW_MINE: ksummit.messages.10050 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：大型子系统“信任维护者”之疑与“勿为 1% 牺牲 99%”两方并置）；动手者叙事（总纲第 10 条——动手者创造历史：以 AMD 官方栈加 amdgpu-pro 私有用户态并存这一实际栈为分析单位）
- **辨析**：三条同属维护者峰会直通议题；Leon 的“信任是双向的”为立场表述，Ribalda 的“1%/99%”为当事人估计，Pinchart 自称观点偏摄像头领域属范围声明。
- **文献**：DSLXC-11433、DSLXC-11446、DSLXC-11474（`ksummit.messages.9885`、`ksummit.messages.9933`、`ksummit.messages.10050`，2024-07-22、2024-07-28、2024-07-25），全文见 `raw_source.raw_json`

## 199.5 补丁基址标注

- **要点**：Rafael 认同 base-commit 语义为“系列开发所基于的树”，可作 Sashiko 等机器人参考点；讨论 b4 基址 trailer 对自动回迁机器人的价值。
- **史料**：`ksummit.messages.9886`（Rafael J. Wysocki (Intel)，2026-08-07）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9886 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 b4 基址 trailer 供自动回迁机器人使用这一具体机制为分析单位）；经验优先（总纲第 9 条——经验优先：以 base-commit“系列开发所基于的树”这一实际语义为判据）
- **辨析**：本块系 Rafael 的认同表述；“可作 Sashiko 等机器人参考点”为对工具用途的判断，属提案性意见。
- **文献**：DSLXC-11434（`ksummit.messages.9886`，2026-08-07），全文见 `raw_source.raw_json`

## 199.6 AI补丁审查

- **要点**：Bart Van Assche 称用 30-40 行提示词让 ChatGPT/Gemini 扮演资深内核开发者即可产出补丁评审，同事的提示词因版权许可不明无法分享。Mason 赞同 Laurent：不得强制贡献者付费或运行专有 AI 工具，审查须在维护者侧运行；但认为供应商锁定现阶段非问题，提示词只是通用 AI 上的英文文本。
- **史料**：`ksummit.messages.9887`（Bart Van Assche，2025-10-08）、`ksummit.messages.10053`（Chris Mason，2025-10-09）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9887 -->` `<!-- ROW_MINE: ksummit.messages.10053 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 30-40 行提示词令 ChatGPT/Gemini 扮演资深内核开发者这一具体做法为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：审查须在维护者侧运行与“供应商锁定现阶段非问题”两方并置）
- **辨析**：两条同属 AI 辅助审查议题；Van Assche 的提示词因版权许可不明无法分享为其实践约束，Mason 的“提示词只是通用 AI 上的英文文本”为对锁定风险的判断。
- **文献**：DSLXC-11435、DSLXC-11476（`ksummit.messages.9887`、`ksummit.messages.10053`，2025-10-08、2025-10-09），全文见 `raw_source.raw_json`

## 199.7 稳定版回迁

- **要点**：Greg KH 重申 stable 发布的第一原则是不给任何维护者增加额外工作，反对 Leemhuis 要求主线上游跟进稳定版修复的提案。Rafael 回应 Kara 疑问：全树同类清理型系列各补丁间无依赖，可借此判断 Fixes 补丁是否依赖系列内前序补丁。Levin 提“Improves”标签并引数据：仅 stable 标签提交约 70% 修复旧版问题，-rc 提交近 85% 处理合并窗口前问题；Bottomley 反对，主张 Fixes 语义更清晰并以 regzbot 式自动化处理事后回迁。Babka 追问回迁异常：37f1663c919 以 Stable-dep-of c3408c4ae041 被回迁，而该依赖本身无 cc:stable 且未回迁，涉 strlcpy 转 strscpy 系列。
- **史料**：`ksummit.messages.9890`（Greg KH，2024-06-13）、`ksummit.messages.9986`（Rafael J. Wysocki，2024-06-14）、`ksummit.messages.10004`（James Bottomley，2024-07-14）、`ksummit.messages.10017`（Vlastimil Babka，2024-06-17）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9890 -->` `<!-- ROW_MINE: ksummit.messages.9986 -->` `<!-- ROW_MINE: ksummit.messages.10004 -->` `<!-- ROW_MINE: ksummit.messages.10017 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以仅 stable 标签提交约 70% 修复旧版问题、-rc 提交近 85% 处理合并窗口前问题这一量化数据为判据）；多方平等（总纲第 8 条——本体论上各方平等：Levin 的 Improves 标签提议与 Bottomley 的 Fixes 语义更清晰主张并置）
- **辨析**：四条同属稳定版回迁议题；Greg KH 的“第一原则是不给任何维护者增加额外工作”为政策宣示，70%/85% 与 37f1663c919 回迁异常均可反查，属一手。
- **文献**：DSLXC-11436、DSLXC-11460、DSLXC-11465、DSLXC-11468（`ksummit.messages.9890`、`ksummit.messages.9986`、`ksummit.messages.10004`、`ksummit.messages.10017`，2024-06-13、2024-06-14、2024-07-14、2024-06-17），全文见 `raw_source.raw_json`

## 199.8 内核文档构建

- **要点**：Mauro 列出 make htmldocs 报错的 4 个来源，发出修复系列后交叉引用警告降至 3 条，指出未合入文档导致悬空引用的跨子系统合并问题。Mauro 实测 next-20220627 有 32 条交叉引用、4 个重复 ABI 符号、60 条 kernel-doc 警告，三系列后仅剩 3 条；建议 CONFIG_WERROR 并入常规构建，脚本约 8 秒。
- **史料**：`ksummit.messages.9892`（Mauro Carvalho Chehab，2022-06-26）、`ksummit.messages.9942`（Mauro Carvalho Chehab，2022-06-28）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9892 -->` `<!-- ROW_MINE: ksummit.messages.9942 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 next-20220627 实测 32 条交叉引用、4 个重复 ABI 符号、60 条 kernel-doc 警告降至此 3 条等数据为判据）；动手者叙事（总纲第 10 条——动手者创造历史：以 CONFIG_WERROR 并入常规构建、脚本约 8 秒等具体机制为分析单位）
- **辨析**：两条均为 Mauro 的实测记录，属文档构建史可复算的一手；“跨子系统合并致悬空引用”为其机制归因。
- **文献**：DSLXC-11437、DSLXC-11450（`ksummit.messages.9892`、`ksummit.messages.9942`，2022-06-26、2022-06-28），全文见 `raw_source.raw_json`

## 199.9 提交溯源标签

- **要点**：Geert 主张提交记录为众多读者而非单个作者优化，批 patchwork 链接多一跳；Jani 称超 99% 的 freedesktop patchwork Link 标签含 Message-ID。Williams 为 b4 shazam 新增 --add-link-note 选项，用 git notes 本地记录提交的 Link: trailer 而不污染上游；注明初稿由 Claude Sonnet 4 协助。Ryabitsev 指出 patch-id 匹配不可靠（差分算法与上下文行数不同即失配），建议以 Message-Id: trailer 取代 Link: 标注来源；Jones 展示 git am --message-id 脚本。
- **史料**：`ksummit.messages.9896`（Geert Uytterhoeven，2024-06-17）、`ksummit.messages.9952`（Dan Williams，2025-10-14）、`ksummit.messages.9957`（Lee Jones，2024-06-14）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9896 -->` `<!-- ROW_MINE: ksummit.messages.9952 -->` `<!-- ROW_MINE: ksummit.messages.9957 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 b4 shazam 的 --add-link-note 用 git notes 本地记录 Link: trailer、git am --message-id 脚本等具体工具为分析单位）；知识注定过时（总纲第 22 条——知识注定过时：patch-id 匹配因差分算法与上下文行数不同即失配，宜以 Message-Id: 取代 Link:）
- **辨析**：三条同属提交溯源标签议题；Williams 注明初稿由 Claude Sonnet 4 协助，Ryabitsev 的 patch-id 不可靠为机制判断，Jani 的“超 99% freedesktop patchwork Link 含 Message-ID”为估计。
- **文献**：DSLXC-11438、DSLXC-11453、DSLXC-11455（`ksummit.messages.9896`、`ksummit.messages.9952`、`ksummit.messages.9957`，2024-06-17、2025-10-14、2024-06-14），全文见 `raw_source.raw_json`

## 199.10 静态分析

- **要点**：Carpenter 的 Smatch 已积累近 2 千条用户可触发整数溢出警告，主张按子系统加严规则；Paul 指出内核依赖 fwrapv，全核有符号溢出检查噪声大。
- **史料**：`ksummit.messages.9907`（Paul E. McKenney，2021-07-27）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9907 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 Smatch 已积累近 2 千条用户可触发整数溢出警告这一实测为判据）；多方平等（总纲第 8 条——本体论上各方平等：按子系统加严规则与内核依赖 fwrapv 致全核有符号溢出检查噪声大两方并置）
- **辨析**：本块含 Dan Carpenter 的加严主张与 Paul 的噪声之评两方；“近 2 千条”为其工具快照计数。
- **文献**：DSLXC-11439（`ksummit.messages.9907`，2021-07-27），全文见 `raw_source.raw_json`

## 199.11 平凡补丁政策

- **要点**：Geert 介绍让全系列收件人都收到 cover letter 的做法：手工在 format-patch 输出加 Cc 行，或借 format.thread 生成最终 Message-ID 并附 lore 链接。Brown 列举 MFD 与新 SoC 系列中存在构建依赖但评审无重叠的正当合并场景；Leon 称 netdev、RDMA、PCI、MM 仍需整系列送达。
- **史料**：`ksummit.messages.9916`（Geert Uytterhoeven，2021-04-23）、`ksummit.messages.9968`（Leon Romanovsky，2021-04-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9916 -->` `<!-- ROW_MINE: ksummit.messages.9968 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以手工在 format-patch 输出加 Cc 行、借 format.thread 生成最终 Message-ID 等具体做法为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：MFD 与新 SoC 系列的正当合并场景与 netdev、RDMA、PCI、MM 仍需整系列送达两方并置）
- **辨析**：两条同属系列送达议题；Geert 的收件人做法与 Brown、Leon 的合并场景均为维护者经验陈述。
- **文献**：DSLXC-11440、DSLXC-11457（`ksummit.messages.9916`、`ksummit.messages.9968`，2021-04-23、2021-04-22），全文见 `raw_source.raw_json`

## 199.12 C警告语义争论

- **要点**：Linus 痛斥对“x<0 且 x≥10”双边界检查告警危险且错误，称符号可见性受架构、typedef、位域影响，绝不启用；Uecker 澄清并非他提议该警告。
- **史料**：`ksummit.messages.9921`（Martin Uecker，2025-02-21）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9921 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：Linus 痛斥双边界检查告警与 Uecker 澄清并非其提议该警告两方并置）；经验优先（总纲第 9 条——经验优先：以符号可见性受架构、typedef、位域影响这一实际语义为判据）
- **辨析**：本块含 Linus 的否决与 Uecker 的澄清两方；“绝不启用”为顶层判断，其“危险且错误”系对告警假设的批评。
- **文献**：DSLXC-11441（`ksummit.messages.9921`，2025-02-21），全文见 `raw_source.raw_json`

## 199.13 背光控制API

- **要点**：Hans 重发 LPC 背光 uAPI 提案：/sys/class/backlight 无法映射面板、多设备并存、需 root、刻度与 0 值语义不明，并认可 Jani 指出的无法在同一 KMS atomic 提交中调 gamma 与亮度。
- **史料**：`ksummit.messages.9922`（Hans de Goede，2022-06-29）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9922 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 LPC 背光 uAPI 提案对 /sys/class/backlight 无法映射面板、刻度与 0 值语义不明等具体缺陷的列举为分析单位）
- **辨析**：本块系 Hans 重发提案；“无法在同一 KMS atomic 提交中调 gamma 与亮度”系其认可 Jani 之指，属技术约束。
- **文献**：DSLXC-11442（`ksummit.messages.9922`，2022-06-29），全文见 `raw_source.raw_json`

## 199.14 涉密代码测试

- **要点**：Hansen 透露 Intel 对涉密补丁跑内部 0day 但结果未随代码提交，承诺改进；与 Levin 讨论修订 embargoed-hardware 文档以便纳入测试者而无需律师。Brown 建议以自由软件为基础提供可选的私有测试系统或脚本作基线，仅列要求清单易被误用；提及 Linaro lkft 曾有私有实例但基础设施未开源。
- **史料**：`ksummit.messages.9923`（Dave Hansen，2023-08-15）、`ksummit.messages.9944`（Mark Brown，2023-08-15）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9923 -->` `<!-- ROW_MINE: ksummit.messages.9944 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 Intel 内部 0day 对涉密补丁测试、Linaro lkft 私有实例等具体实践为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：改进 embargoed-hardware 文档以便纳入测试者与“仅列要求清单易被误用”两方并置）
- **辨析**：两条同属涉密测试议题；Hansen 的“结果未随代码提交”为自承缺陷，Brown 的“基础设施未开源”为对私有实例的说明。
- **文献**：DSLXC-11443、DSLXC-11451（`ksummit.messages.9923`、`ksummit.messages.9944`，2023-08-15、2023-08-15），全文见 `raw_source.raw_json`

## 199.15 审查文化

- **要点**：Brauner 认为推动高质量审查靠共同责任感，但非技术阻挠指控使此事如赫拉克勒斯之任；需要安全环境与共享所有权模型，各子系统皆有欠缺。
- **史料**：`ksummit.messages.9931`（Christian Brauner，2023-08-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9931 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：共同责任感推动高质量审查与非技术阻挠指控使此事如赫拉克勒斯之任并置）；动手者叙事（总纲第 10 条——动手者创造历史：以安全环境与共享所有权模型这一具体诉求为分析单位）
- **辨析**：本块系 Brauner 的判断；“各子系统皆有欠缺”为其对现状的评估，属开放问题。
- **文献**：DSLXC-11444（`ksummit.messages.9931`，2023-08-22），全文见 `raw_source.raw_json`

## 199.16 C内存语义

- **要点**：McKenney 举例 x=1 可被优化为 if(x!=1) x=1，读检查写可能重排到 smp_wmb 之前，讨论 C 标准允许但对并发代码意外的写变换。
- **史料**：`ksummit.messages.9932`（Paul E. McKenney，2025-02-27）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9932 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 x=1 可被优化为 if(x!=1) x=1、读检查写可能重排到 smp_wmb 之前这一实际变换为判据）；知识注定过时（总纲第 22 条——知识注定过时：C 标准允许的写变换对并发代码意外，属随标准演进的议题）
- **辨析**：本块系 Paul E. McKenney 的举例，属内存模型层一手；“对并发代码意外”为其机制判断。
- **文献**：DSLXC-11445（`ksummit.messages.9932`，2025-02-27），全文见 `raw_source.raw_json`

## 199.17 稳定版邮件

- **要点**：Brown 支持把各稳定版回迁汇总为单封摘要（“补丁 A 已回迁至 X-Y”），更易发现回迁深度不足；现需翻六个线程逐一核对每封补丁。
- **史料**：`ksummit.messages.9937`（Mark Brown，2025-08-06）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9937 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以把各稳定版回迁汇总为单封摘要这一具体方案为分析单位）；经验优先（总纲第 9 条——经验优先：以“现需翻六个线程逐一核对每封补丁”这一实际工作流为判据）
- **辨析**：本块系 Brown 的改进主张；“更易发现回迁深度不足”为其目标表述，属提案。
- **文献**：DSLXC-11447（`ksummit.messages.9937`，2025-08-06），全文见 `raw_source.raw_json`

## 199.18 DRM面板API

- **要点**：Armstrong 称 panel API 缺原子接口致上下游碎片化，面板厂商 fire-and-forget 无上游动力；Ripard 提“面板即 bridge”及仿 HID-BPF 用 eBPF 承载怪癖。
- **史料**：`ksummit.messages.9940`（Neil Armstrong，2026-06-04）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9940 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“面板即 bridge”及仿 HID-BPF 用 eBPF 承载怪癖等具体机制为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：panel API 缺原子接口致碎片化与厂商 fire-and-forget 无上游动力两方并置）
- **辨析**：本块含 Armstrong 的批评与 Ripard 的方案两方；“上下游碎片化”为机制归因。
- **文献**：DSLXC-11448（`ksummit.messages.9940`，2026-06-04），全文见 `raw_source.raw_json`

## 199.19 驱动探测失败

- **要点**：Torokhov 结论：异步探针、热插拔与 sysfs new_id 场景下接口驱动无法可靠注销，单例平台设备的探测失败处理只能由驱动自身负责。
- **史料**：`ksummit.messages.9941`（Dmitry Torokhov，2022-06-24）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9941 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以异步探针、热插拔与 sysfs new_id 场景下接口驱动无法可靠注销这一实际状况为判据）；动手者叙事（总纲第 10 条——动手者创造历史：以单例平台设备的探测失败处理只能由驱动自身负责这一具体边界为分析单位）
- **辨析**：本块系 Dmitry Torokhov 的结论；“只能由驱动自身负责”为其对接口边界的判断。
- **文献**：DSLXC-11449（`ksummit.messages.9941`，2022-06-24），全文见 `raw_source.raw_json`

## 199.20 Rust政策争论

- **要点**：Hellwig 指政策文档“不强制任何子系统”已被 Linus 私下越过维护者合并 Rust 证伪，斥其沟通不诚实；警告绑定蔓延终将波及所有非叶子系统。Greg KH 以 15 年经手几乎所有 bugfix 与 CVE 的经验断言多数缺陷源于 C 错误路径、漏检返回值与 UAF，Rust 可消之；支持新驱动用 Rust，并称绑定倒逼 API 清理惠及 C 用户。
- **史料**：`ksummit.messages.9945`（Christoph Hellwig，2025-02-20）、`ksummit.messages.10044`（Greg KH，2025-02-19）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9945 -->` `<!-- ROW_MINE: ksummit.messages.10044 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：Hellwig 斥政策文档已被私下强并证伪与 Greg KH 以 15 年经验挺 Rust 两方并置）；经验优先（总纲第 9 条——经验优先：以“多数缺陷源于 C 错误路径、漏检返回值与 UAF”这一 15 年经手经验为判据）
- **辨析**：本块系本页正反双方陈述并列；“绑定蔓延终将波及所有非叶子系统”为 Hellwig 的预判，Greg KH 的“绑定倒逼 API 清理惠及 C 用户”为其主张。
- **文献**：DSLXC-11452、DSLXC-11472（`ksummit.messages.9945`、`ksummit.messages.10044`，2025-02-20、2025-02-19），全文见 `raw_source.raw_json`

## 199.21 回迁仪表盘

- **要点**：Levin 展示自建 stable 回迁仪表盘原型 sashalevin.github.io，称 AI 使其无需 LF 资助即得九成价值，已吸收 Tso 的子系统过滤、CVE 与日期筛选建议，拟在 LPC 展示。
- **史料**：`ksummit.messages.9956`（Sasha Levin，2025-08-06）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9956 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以自建 stable 回迁仪表盘原型 sashalevin.github.io 这一具体工具为分析单位）；经验优先（总纲第 9 条——经验优先：以“AI 使其无需 LF 资助即得九成价值”这一实际效果为判据）
- **辨析**：本块系 Sasha Levin 的自述；“九成价值”为其估计，已吸收 Tso 的子系统过滤等建议，拟在 LPC 展示。
- **文献**：DSLXC-11454（`ksummit.messages.9956`，2025-08-06），全文见 `raw_source.raw_json`

## 199.22 堆栈回溯术语

- **要点**：Rostedt 记 GNU Cauldron 教训：编译器社区的 unwinding 指完整展开，内核所指实为 stack walking，与 ORC 作者 Josh 同 GCC 争论后遂解；Kent 称 ORC 曾无法生成回溯而改用帧指针。
- **史料**：`ksummit.messages.9967`（Kent Overstreet，2025-02-26）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9967 -->`
- **史观**：知识注定过时（总纲第 22 条——知识注定过时：编译器社区 unwinding 与内核 stack walking 术语错位经与 GCC 争论后方解）；动手者叙事（总纲第 10 条——动手者创造历史：以 ORC 曾无法生成回溯而改用帧指针这一具体工程取舍为分析单位）
- **辨析**：本块系 Rostedt 的会议记录；“与 ORC 作者 Josh 同 GCC 争论后遂解”为术语沿革一手，Kent 的改用帧指针为工程应对。
- **文献**：DSLXC-11456（`ksummit.messages.9967`，2025-02-26），全文见 `raw_source.raw_json`

## 199.23 TAB选举

- **要点**：Babka 披露 2022 TAB 选举 960 名合格选民仅 267 投票，Kees Cook、Brauner、Kicinski、Williams、Hansen 当选；因 CIVS 邀请邮件淹没于 LPC 期间，建议投票提前一周。Abbott 公布 2021 TAB 选举新规：投票资格与 kernel summit 脱钩，改绑 2020-21 年 3 枚主/稳定线提交标签，合格人群扩至 4000 余人，50+ 提交者自动收选票。
- **史料**：`ksummit.messages.9980`（Vlastimil Babka，2022-09-18）、`ksummit.messages.10020`（Laura Abbott，2021-08-25）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9980 -->` `<!-- ROW_MINE: ksummit.messages.10020 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 2021 TAB 选举资格改绑 3 枚提交标签、合格人群扩至 4000 余人这一具体制度变更为分析单位）；经验优先（总纲第 9 条——经验优先：以 2022 年 960 名合格选民仅 267 投票、CIVS 邀请邮件淹没于 LPC 期间这一实测为判据）
- **辨析**：两条分属 2022 与 2021 选举；Babka 的投票率与建议投票提前一周为程序性意见，Abbott 的新规为治理里程碑一手。
- **文献**：DSLXC-11458、DSLXC-11470（`ksummit.messages.9980`、`ksummit.messages.10020`，2022-09-18、2021-08-25），全文见 `raw_source.raw_json`

## 199.24 维护者支持小组

- **要点**：Rostedt 详述支持小组设计：不设邮件列表以保护倾诉者选择可见对象，志愿者保密承诺不覆盖暴力威胁等非法内容，允许上报而不违约。
- **史料**：`ksummit.messages.9987`（Steven Rostedt，2023-09-19）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9987 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以不设邮件列表以保护倾诉者选择可见对象这一具体设计为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：志愿者保密承诺与不覆盖暴力威胁等非法内容的边界并置）
- **辨析**：本块系 Rostedt 的设计详述；“允许上报而不违约”为其对保密承诺边界的说明。
- **文献**：DSLXC-11461（`ksummit.messages.9987`，2023-09-19），全文见 `raw_source.raw_json`

## 199.25 Rust引用计数

- **要点**：Wedson 解释 Rust weak 指针惯用法：强/弱双计数，析构同时自链表摘除即可双双归零，可零成本抽象避免 0 到 1 竞态，回应 Kara 对引用回收建模的疑问。Wedson 逐行回应 Greg 对 Ref<T> 的质疑：drop 时引用数必非零系类型不变式，kref 的 release 回调编译期即知无需经 C；无需加锁，弱引用因额外开销暂未纳入。
- **史料**：`ksummit.messages.9994`（Wedson Almeida Filho，2021-07-07）、`ksummit.messages.10043`（Wedson Almeida Filho，2021-07-07）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9994 -->` `<!-- ROW_MINE: ksummit.messages.10043 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以强/弱双计数、析构同时自链表摘除即可双双归零这一具体机制为分析单位）；经验优先（总纲第 9 条——经验优先：以“drop 时引用数必非零系类型不变式”这一实际约束为判据）
- **辨析**：两条均为 Wedson Almeida Filho 的技术回应；“可零成本抽象避免 0 到 1 竞态”为其主张，弱引用因额外开销暂未纳入。
- **文献**：DSLXC-11462、DSLXC-11471（`ksummit.messages.9994`、`ksummit.messages.10043`，2021-07-07、2021-07-07），全文见 `raw_source.raw_json`

## 199.26 维护者分支管理

- **要点**：Babka 问能否以两主题分支共享基座替代合并；Rostedt 述其做法：补丁先入一支再带详细说明合入另一支，Linus 未表异议。
- **史料**：`ksummit.messages.10003`（Vlastimil Babka，2025-09-12）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10003 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以补丁先入一支再带详细说明合入另一支这一具体做法为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：两主题分支共享基座之问与 Rostedt 的分支做法并置）
- **辨析**：本块含 Babka 的提问与 Rostedt 的做法两方；“Linus 未表异议”为 Rostedt 的转述。
- **文献**：DSLXC-11464（`ksummit.messages.10003`，2025-09-12），全文见 `raw_source.raw_json`

## 199.27 功能纳退机制

- **要点**：Greg KH 反对为功能纳退立法化：此类事件 35 年仅一见且各具情境，无流程文档结果亦同；称澄清网络猜测非其职，私下已有决定。
- **史料**：`ksummit.messages.10006`（Greg KH，2025-08-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10006 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：反对为功能纳退立法化与澄清网络猜测非其职两方并置）；经验优先（总纲第 9 条——经验优先：以“此类事件 35 年仅一见且各具情境”这一历史经验为判据）
- **辨析**：本块系 Greg KH 的立场；“无流程文档结果亦同”为其判断，“私下已有决定”表明决策已定。
- **文献**：DSLXC-11466（`ksummit.messages.10006`，2025-08-22），全文见 `raw_source.raw_json`

## 199.28 内核信任体系

- **要点**：Ryabitsev 剖析 kernel.org 信任网瓶颈：密钥更新均经其手工校验，扩展至数千开发者不可持续且仅限 PGP；正试验自助 DID 方案，条件是可选、不强制重签、无中央服务。
- **史料**：`ksummit.messages.10011`（Konstantin Ryabitsev，2026-01-23）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10011 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以正试验自助 DID 方案、密钥更新均经其手工校验这一具体机制为分析单位）；知识注定过时（总纲第 22 条——知识注定过时：仅限 PGP 的信任网扩展至数千开发者不可持续）
- **辨析**：本块系 Konstantin Ryabitsev 的剖析；“手工校验不可持续”为其判断，DID 方案的条件“可选、不强制重签、无中央服务”为设计约束。
- **文献**：DSLXC-11467（`ksummit.messages.10011`，2026-01-23），全文见 `raw_source.raw_json`

## 199.29 邮件引用礼仪

- **要点**：Linus 主张列表上过度引用应如 HTML 般一票否决：其 MUA 隐藏冗余引用后，lore 上数百行补丁引用令翻阅线程举步维艰。
- **史料**：`ksummit.messages.10018`（Linus Torvalds，2023-10-25）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10018 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：列表过度引用应如 HTML 般一票否决与 lore 上数百行补丁引用令翻阅线程举步维艰并置）；经验优先（总纲第 9 条——经验优先：以其 MUA 隐藏冗余引用后这一实际体验为判据）
- **辨析**：本块系 Linus 的主张；“一票否决”为修辞性表述，属开放的风格之争。
- **文献**：DSLXC-11469（`ksummit.messages.10018`，2023-10-25），全文见 `raw_source.raw_json`

## 199.30 Rust抽象布局

- **要点**：Ojeda 解释 rust/ 目录集中存放全内核共享抽象：可用 C 绑定与不稳特性而普通模块受限；crate 编译模型异于 C 无头文件；不排除按子系统拆分 gpio crate。
- **史料**：`ksummit.messages.10049`（Miguel Ojeda，2021-07-20）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10049 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 rust/ 目录集中存放全内核共享抽象、crate 编译模型异于 C 无头文件等具体机制为分析单位）；知识注定过时（总纲第 22 条——知识注定过时：不排除按子系统拆分 gpio crate，目录布局随版本演进）
- **辨析**：本块系 Miguel Ojeda 的说明；“可用 C 绑定与不稳特性而普通模块受限”为当前约束，属一手。
- **文献**：DSLXC-11473（`ksummit.messages.10049`，2021-07-20），全文见 `raw_source.raw_json`

## 199.31 合并前测试

- **要点**：Levin 说明 linus-next 不自建测试，交由 LKFT、KernelCI 等既有 CI 执行，并称 KernelCI 正在接入 blktests。
- **史料**：`ksummit.messages.10051`（Sasha Levin，2024-10-21）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10051 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 linus-next 不自建测试、交由 LKFT、KernelCI 等既有 CI 执行这一具体分工为分析单位）；经验优先（总纲第 9 条——经验优先：以 KernelCI 正在接入 blktests 这一实际进展为判据）
- **辨析**：本块系 Sasha Levin 的说明；“不自建测试”为其对职责边界的界定，属一手。
- **文献**：DSLXC-11475（`ksummit.messages.10051`，2024-10-21），全文见 `raw_source.raw_json`
