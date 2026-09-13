# 199. Greg KH 挺 Rust 正方陈述、选举资格脱钩新规与回迁仪表盘（ks p63）

> 来源：ksummit 独有 p63（50 封全读，2025-10 至 2026-08：Greg KH 以 15 年经手几乎所有 bugfix 与 CVE 的一手经验系统陈述支持 Rust 进入内核的理由多数缺陷源于 C 错误路径与 UAF 类低级错误系 2025 年 Rust 政策之争最有分量正方陈述；Christoph Hellwig 指控 Rust 政策文档不强制任何子系统被 Linus 私下越过维护者合并 Rust 证伪直接记录核心诚信争议与绑定蔓延论；Laura Abbott 公布 2021 TAB 选举新规投票资格与 Kernel Summit 脱钩改绑 3 枚提交标签合格选民扩至 4000 余人系治理里程碑；Bottomley 与 Levin 就稳定版 Improves 标签交锋含仅 stable 标签提交约 70% 修复旧版问题与 -rc 提交近 85% 处理合并窗口前问题量化数据；稳定版回迁五封）
> 判定：47 CAND / 3 NV。主题分布：峰会存废争论 2、Rust稳定性争论 1、Bugzilla邮件政策 2、设备直通争论 3、补丁基址标注 1、AI补丁审查 2、稳定版回迁 4、内核文档构建 2、提交溯源标签 3、静态分析 1、平凡补丁政策 2、C警告语义争论 1、背光控制API 1、涉密代码测试 2、审查文化 1、C内存语义 1、稳定版邮件 1、DRM面板API 1、驱动探测失败 1、Rust政策争论 2、回迁仪表盘 1、堆栈回溯术语 1、TAB选举 2、维护者支持小组 1、Rust引用计数 2、维护者分支管理 1、功能纳退机制 1、内核信任体系 1、邮件引用礼仪 1、Rust抽象布局 1、合并前测试 1。

## 199.1 峰会存废争论

- 【Linux社区】Bottomley 指出 conclave.rst 应急预案已覆盖峰会停办情形：TAB 主席转任 $ORGANIZER，由 TAB 遴选继任会议与会者，无需新流程即可应对。 `<!-- ROW_MINE: ksummit.messages.9879 -->`
- 【Linux社区】Rostedt 估 AI 议题或成峰会赞助亮点，警告移赞助至 Plumbers 将现 10 万美元预算缺口，并入现有会议或恢复旧式 kernel summit 均为选项，关键在 Linus 取舍。 `<!-- ROW_MINE: ksummit.messages.9999 -->`

## 199.2 Rust稳定性争论

- 【Linux社区】Ventura Jack 引 time crate 破坏致 NixOS 大量协调成本及 GitHub 56 个差评，指出同一 RwLock 代码在 2021 与 2024 版下语义不同，质疑其“向后兼容承诺”。 `<!-- ROW_MINE: ksummit.messages.9880 -->`

## 199.3 Bugzilla邮件政策

- 【Linux社区】Viro 反驳“不喜欢就退订”论：linux-fsdevel 等列表作为收件方根本无从退订 bugzilla 邮件，指其结构性缺陷，该答复是死路。 `<!-- ROW_MINE: ksummit.messages.9884 -->`
- 【Linux社区】Tashkinov 总结困局：部分内核组件无对应邮件列表、群体邀约订阅难推行、收集 git log 公开邮箱或涉欧盟违法，称遭全员反对而放弃提案。 `<!-- ROW_MINE: ksummit.messages.9981 -->`

## 199.4 设备直通争论

- 【Linux社区】Leon Romanovsky 称“信任是双向的”，在大型子系统与复杂设备上“信任维护者”是空想；Pinchart 追问其论断范围，双方就跨子系统 NAK 信任交锋。 `<!-- ROW_MINE: ksummit.messages.9885 -->`
- 【Linux社区】Pinchart 质疑直通议题在维护者峰会闭门决策的正当性，主张相关子系统维护者与推动者等利益相关方应到场；自称观点偏摄像头领域。 `<!-- ROW_MINE: ksummit.messages.9933 -->`
- 【Linux社区】Ribalda 主张勿为 1% 高级用法牺牲 99% 标准流程，以 AMD 官方栈加 amdgpu-pro 私有用户态并存为例，呼吁共同定义“正常工作流”并给出厂商直通的通用准则。 `<!-- ROW_MINE: ksummit.messages.10050 -->`

## 199.5 补丁基址标注

- 【Linux社区】Rafael 认同 base-commit 语义为“系列开发所基于的树”，可作 Sashiko 等机器人参考点；讨论 b4 基址 trailer 对自动回迁机器人的价值。 `<!-- ROW_MINE: ksummit.messages.9886 -->`

## 199.6 AI补丁审查

- 【Linux社区】Bart Van Assche 称用 30-40 行提示词让 ChatGPT/Gemini 扮演资深内核开发者即可产出补丁评审，同事的提示词因版权许可不明无法分享。 `<!-- ROW_MINE: ksummit.messages.9887 -->`
- 【Linux社区】Mason 赞同 Laurent：不得强制贡献者付费或运行专有 AI 工具，审查须在维护者侧运行；但认为供应商锁定现阶段非问题，提示词只是通用 AI 上的英文文本。 `<!-- ROW_MINE: ksummit.messages.10053 -->`

## 199.7 稳定版回迁

- 【Linux社区】Greg KH 重申 stable 发布的第一原则是不给任何维护者增加额外工作，反对 Leemhuis 要求主线上游跟进稳定版修复的提案。 `<!-- ROW_MINE: ksummit.messages.9890 -->`
- 【Linux社区】Rafael 回应 Kara 疑问：全树同类清理型系列各补丁间无依赖，可借此判断 Fixes 补丁是否依赖系列内前序补丁。 `<!-- ROW_MINE: ksummit.messages.9986 -->`
- 【Linux社区】Levin 提“Improves”标签并引数据：仅 stable 标签提交约 70% 修复旧版问题，-rc 提交近 85% 处理合并窗口前问题；Bottomley 反对，主张 Fixes 语义更清晰并以 regzbot 式自动化处理事后回迁。 `<!-- ROW_MINE: ksummit.messages.10004 -->`
- 【Linux社区】Babka 追问回迁异常：37f1663c919 以 Stable-dep-of c3408c4ae041 被回迁，而该依赖本身无 cc:stable 且未回迁，涉 strlcpy 转 strscpy 系列。 `<!-- ROW_MINE: ksummit.messages.10017 -->`

## 199.8 内核文档构建

- 【Linux社区】Mauro 列出 make htmldocs 报错的 4 个来源，发出修复系列后交叉引用警告降至 3 条，指出未合入文档导致悬空引用的跨子系统合并问题。 `<!-- ROW_MINE: ksummit.messages.9892 -->`
- 【Linux社区】Mauro 实测 next-20220627 有 32 条交叉引用、4 个重复 ABI 符号、60 条 kernel-doc 警告，三系列后仅剩 3 条；建议 CONFIG_WERROR 并入常规构建，脚本约 8 秒。 `<!-- ROW_MINE: ksummit.messages.9942 -->`

## 199.9 提交溯源标签

- 【Linux社区】Geert 主张提交记录为众多读者而非单个作者优化，批 patchwork 链接多一跳；Jani 称超 99% 的 freedesktop patchwork Link 标签含 Message-ID。 `<!-- ROW_MINE: ksummit.messages.9896 -->`
- 【Linux社区】Williams 为 b4 shazam 新增 --add-link-note 选项，用 git notes 本地记录提交的 Link: trailer 而不污染上游；注明初稿由 Claude Sonnet 4 协助。 `<!-- ROW_MINE: ksummit.messages.9952 -->`
- 【Linux社区】Ryabitsev 指出 patch-id 匹配不可靠（差分算法与上下文行数不同即失配），建议以 Message-Id: trailer 取代 Link: 标注来源；Jones 展示 git am --message-id 脚本。 `<!-- ROW_MINE: ksummit.messages.9957 -->`

## 199.10 静态分析

- 【Linux社区】Carpenter 的 Smatch 已积累近 2 千条用户可触发整数溢出警告，主张按子系统加严规则；Paul 指出内核依赖 fwrapv，全核有符号溢出检查噪声大。 `<!-- ROW_MINE: ksummit.messages.9907 -->`

## 199.11 平凡补丁政策

- 【Linux社区】Geert 介绍让全系列收件人都收到 cover letter 的做法：手工在 format-patch 输出加 Cc 行，或借 format.thread 生成最终 Message-ID 并附 lore 链接。 `<!-- ROW_MINE: ksummit.messages.9916 -->`
- 【Linux社区】Brown 列举 MFD 与新 SoC 系列中存在构建依赖但评审无重叠的正当合并场景；Leon 称 netdev、RDMA、PCI、MM 仍需整系列送达。 `<!-- ROW_MINE: ksummit.messages.9968 -->`

## 199.12 C警告语义争论

- 【Linux社区】Linus 痛斥对“x<0 且 x≥10”双边界检查告警危险且错误，称符号可见性受架构、typedef、位域影响，绝不启用；Uecker 澄清并非他提议该警告。 `<!-- ROW_MINE: ksummit.messages.9921 -->`

## 199.13 背光控制API

- 【Linux社区】Hans 重发 LPC 背光 uAPI 提案：/sys/class/backlight 无法映射面板、多设备并存、需 root、刻度与 0 值语义不明，并认可 Jani 指出的无法在同一 KMS atomic 提交中调 gamma 与亮度。 `<!-- ROW_MINE: ksummit.messages.9922 -->`

## 199.14 涉密代码测试

- 【Linux社区】Hansen 透露 Intel 对涉密补丁跑内部 0day 但结果未随代码提交，承诺改进；与 Levin 讨论修订 embargoed-hardware 文档以便纳入测试者而无需律师。 `<!-- ROW_MINE: ksummit.messages.9923 -->`
- 【Linux社区】Brown 建议以自由软件为基础提供可选的私有测试系统或脚本作基线，仅列要求清单易被误用；提及 Linaro lkft 曾有私有实例但基础设施未开源。 `<!-- ROW_MINE: ksummit.messages.9944 -->`

## 199.15 审查文化

- 【Linux社区】Brauner 认为推动高质量审查靠共同责任感，但非技术阻挠指控使此事如赫拉克勒斯之任；需要安全环境与共享所有权模型，各子系统皆有欠缺。 `<!-- ROW_MINE: ksummit.messages.9931 -->`

## 199.16 C内存语义

- 【Linux社区】McKenney 举例 x=1 可被优化为 if(x!=1) x=1，读检查写可能重排到 smp_wmb 之前，讨论 C 标准允许但对并发代码意外的写变换。 `<!-- ROW_MINE: ksummit.messages.9932 -->`

## 199.17 稳定版邮件

- 【Linux社区】Brown 支持把各稳定版回迁汇总为单封摘要（“补丁 A 已回迁至 X-Y”），更易发现回迁深度不足；现需翻六个线程逐一核对每封补丁。 `<!-- ROW_MINE: ksummit.messages.9937 -->`

## 199.18 DRM面板API

- 【Linux社区】Armstrong 称 panel API 缺原子接口致上下游碎片化，面板厂商 fire-and-forget 无上游动力；Ripard 提“面板即 bridge”及仿 HID-BPF 用 eBPF 承载怪癖。 `<!-- ROW_MINE: ksummit.messages.9940 -->`

## 199.19 驱动探测失败

- 【Linux社区】Torokhov 结论：异步探针、热插拔与 sysfs new_id 场景下接口驱动无法可靠注销，单例平台设备的探测失败处理只能由驱动自身负责。 `<!-- ROW_MINE: ksummit.messages.9941 -->`

## 199.20 Rust政策争论

- 【Linux社区】Hellwig 指政策文档“不强制任何子系统”已被 Linus 私下越过维护者合并 Rust 证伪，斥其沟通不诚实；警告绑定蔓延终将波及所有非叶子系统。 `<!-- ROW_MINE: ksummit.messages.9945 -->`
- 【Linux社区】Greg KH 以 15 年经手几乎所有 bugfix 与 CVE 的经验断言多数缺陷源于 C 错误路径、漏检返回值与 UAF，Rust 可消之；支持新驱动用 Rust，并称绑定倒逼 API 清理惠及 C 用户。 `<!-- ROW_MINE: ksummit.messages.10044 -->`

## 199.21 回迁仪表盘

- 【Linux社区】Levin 展示自建 stable 回迁仪表盘原型 sashalevin.github.io，称 AI 使其无需 LF 资助即得九成价值，已吸收 Tso 的子系统过滤、CVE 与日期筛选建议，拟在 LPC 展示。 `<!-- ROW_MINE: ksummit.messages.9956 -->`

## 199.22 堆栈回溯术语

- 【Linux社区】Rostedt 记 GNU Cauldron 教训：编译器社区的 unwinding 指完整展开，内核所指实为 stack walking，与 ORC 作者 Josh 同 GCC 争论后遂解；Kent 称 ORC 曾无法生成回溯而改用帧指针。 `<!-- ROW_MINE: ksummit.messages.9967 -->`

## 199.23 TAB选举

- 【Linux社区】Babka 披露 2022 TAB 选举 960 名合格选民仅 267 投票，Kees Cook、Brauner、Kicinski、Williams、Hansen 当选；因 CIVS 邀请邮件淹没于 LPC 期间，建议投票提前一周。 `<!-- ROW_MINE: ksummit.messages.9980 -->`
- 【Linux社区】Abbott 公布 2021 TAB 选举新规：投票资格与 kernel summit 脱钩，改绑 2020-21 年 3 枚主/稳定线提交标签，合格人群扩至 4000 余人，50+ 提交者自动收选票。 `<!-- ROW_MINE: ksummit.messages.10020 -->`

## 199.24 维护者支持小组

- 【Linux社区】Rostedt 详述支持小组设计：不设邮件列表以保护倾诉者选择可见对象，志愿者保密承诺不覆盖暴力威胁等非法内容，允许上报而不违约。 `<!-- ROW_MINE: ksummit.messages.9987 -->`

## 199.25 Rust引用计数

- 【Linux社区】Wedson 解释 Rust weak 指针惯用法：强/弱双计数，析构同时自链表摘除即可双双归零，可零成本抽象避免 0 到 1 竞态，回应 Kara 对引用回收建模的疑问。 `<!-- ROW_MINE: ksummit.messages.9994 -->`
- 【Linux社区】Wedson 逐行回应 Greg 对 Ref<T> 的质疑：drop 时引用数必非零系类型不变式，kref 的 release 回调编译期即知无需经 C；无需加锁，弱引用因额外开销暂未纳入。 `<!-- ROW_MINE: ksummit.messages.10043 -->`

## 199.26 维护者分支管理

- 【Linux社区】Babka 问能否以两主题分支共享基座替代合并；Rostedt 述其做法：补丁先入一支再带详细说明合入另一支，Linus 未表异议。 `<!-- ROW_MINE: ksummit.messages.10003 -->`

## 199.27 功能纳退机制

- 【Linux社区】Greg KH 反对为功能纳退立法化：此类事件 35 年仅一见且各具情境，无流程文档结果亦同；称澄清网络猜测非其职，私下已有决定。 `<!-- ROW_MINE: ksummit.messages.10006 -->`

## 199.28 内核信任体系

- 【Linux社区】Ryabitsev 剖析 kernel.org 信任网瓶颈：密钥更新均经其手工校验，扩展至数千开发者不可持续且仅限 PGP；正试验自助 DID 方案，条件是可选、不强制重签、无中央服务。 `<!-- ROW_MINE: ksummit.messages.10011 -->`

## 199.29 邮件引用礼仪

- 【Linux社区】Linus 主张列表上过度引用应如 HTML 般一票否决：其 MUA 隐藏冗余引用后，lore 上数百行补丁引用令翻阅线程举步维艰。 `<!-- ROW_MINE: ksummit.messages.10018 -->`

## 199.30 Rust抽象布局

- 【Linux社区】Ojeda 解释 rust/ 目录集中存放全内核共享抽象：可用 C 绑定与不稳特性而普通模块受限；crate 编译模型异于 C 无头文件；不排除按子系统拆分 gpio crate。 `<!-- ROW_MINE: ksummit.messages.10049 -->`

## 199.31 合并前测试

- 【Linux社区】Levin 说明 linus-next 不自建测试，交由 LKFT、KernelCI 等既有 CI 执行，并称 KernelCI 正在接入 blktests。 `<!-- ROW_MINE: ksummit.messages.10051 -->`
