# 192 【Linux社区】回归时效统计与rustc协调

> 来源：ksummit 独有 p56（50 封全读，2021-04 至 2026-08：Leemhuis 全页唯一带完整统计邮件 7.1 周期 39 起回归中位 20 天才修复远超 Linus 一周内法则并附 14 条高效子系统做法清单；Overstreet 2021 年 Folio 争论浓缩陈述极简仅页缓存与极大含匿名页两路线 Willy 拆解 struct page 策略及 Johannes 保留意见；Levin 用 git log 实测 v6.15..v6.16 共 14639 提交 2734 个修复约 20% 反驳对 AI 设更高门槛；Ralf Jung 披露 rustc 与内核协调机制实例 aarch64 FP 可靠性警告提前预警与 nightly 特性 CI 特别照顾；AI 补丁标注四封、cleanup.h 风格与 linus-next 争议各三封）
> 判定：40 CAND / 10 NV。主题分布：AI补丁标注 4、UMN实验争议 1、THE REST分流 2、C编译器警告 1、Rust架构定位 1、提交标记规范 3、AI提交治理 1、linus-next争议 2、cleanup.h风格 2、Rust panic语义 1、trivial树存废 1、Bugzilla困境 1、sashiko审查模型 2、unsafe Rust难度 1、邮件礼仪争论 1、Folio设计分歧 1、AI质量门槛 1、厂商开源策略 1、回归修复时效 1、Rust抽象维护 1、文档建设 1、维护者支持组 1、稳定版队列机制 1、列表平台迁移 1、Rust内存安全争论 1、LLM标签信号 1、Rust驱动安全机制 1、维护者倦怠 1、rustc兼容保障 1、UBSan生产应用 1、文档构建环境 1。

## 192.1 AI补丁标注

- **要点**：Alexandre Belloni指静态检查器生成的修补常无意义，如永不触发的返回值检查；建议贡献者明示用工具发现问题并生成补丁，便于维护者直接忽略。Steven Rostedt质疑AI代写代码时签署人是否有权加Signed-off-by，尤其不知训练数据来源；若AI用了专利算法，签署者是否担法律风险。Miguel Ojeda认为工具生成内容指南已够清晰：要求理解整个提交并回应评审，维护者可酌情直接拒绝无法解释的补丁系列。Paul McKenney称在版权诉讼落定前不对开源项目用AI生成物，引DCO“有权提交”条款，指在途诉讼或使AI代码构成侵权，误收只能剔除并净室重写。
- **史料**：`ksummit.messages.8658`（Alexandre Belloni，2025-08-05）、`ksummit.messages.8680`（Steven Rostedt，2025-08-12）、`ksummit.messages.8687`（Miguel Ojeda，2026-01-08）、`ksummit.messages.8766`（Paul E. McKenney，2025-08-12）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8658 -->` `<!-- ROW_MINE: ksummit.messages.8680 -->` `<!-- ROW_MINE: ksummit.messages.8687 -->` `<!-- ROW_MINE: ksummit.messages.8766 -->`
- **史观**：法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：Signed-off-by 的签署权与训练数据来源之争落在 DCO“有权提交”条款上）；多方平等（总纲第 8 条——本体论上各方平等：明示工具来源、签署权质疑、指南已够清晰与暂不用 AI 生成物四说并置）
- **辨析**：McKenney 的“版权诉讼落定前不对开源项目用 AI 生成物、误收只能剔除并净室重写”为个人风险策略，非法律意见；Ojeda 的“指南已够清晰”为维护者解读，与 Rostedt 的签署权质疑构成张力。
- **文献**：DSLXC-11142、DSLXC-11147、DSLXC-11152、DSLXC-11172（`ksummit.messages.8658`、`ksummit.messages.8680`、`ksummit.messages.8687`、`ksummit.messages.8766`，2025-08-05、2025-08-12、2026-01-08、2025-08-12），全文见 `raw_source.raw_json`

## 192.2 UMN实验争议

- **要点**：Al Viro指出UMN团队实验结束后至今未公布所涉补丁的SHA1清单，缺乏原始数据即“记者会式科学”，以此回应宽恕与严惩之争。
- **史料**：`ksummit.messages.8660`（Al Viro，2021-04-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8660 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“缺乏原始数据即记者会式科学”这一证据标准为判据）；多方平等（总纲第 8 条——本体论上各方平等：宽恕与严惩之争以证据缺失为切入）
- **辨析**：本块系 Al Viro 单方质疑，其“未公布 SHA1 清单”为可核查的缺失项；本页未见 UMN 团队回应。
- **文献**：DSLXC-11143（`ksummit.messages.8660`，2021-04-22），全文见 `raw_source.raw_json`

## 192.3 THE REST分流

- **要点**：Mark Brown判断LKML流量主要源于get_maintainer.pl自动抄送lkml，而非用户显式配置git-send-email，故THE REST分流收效有限。Konstantin Ryabitsev认同收件应由工具决定，计划改造工具不再对所有补丁抄送linux-kernel@vger，仅无其他列表匹配时才加。
- **史料**：`ksummit.messages.8661`（Mark Brown，2023-11-07）、`ksummit.messages.8715`（Konstantin Ryabitsev，2023-11-09）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8661 -->` `<!-- ROW_MINE: ksummit.messages.8715 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以改造 get_maintainer.pl 抄送逻辑这一具体工具手段为分析单位）；经验优先（总纲第 9 条——经验优先：以 LKML 流量主要源于自动抄送这一实际归因为判据）
- **辨析**：Brown 的归因与 Ryabitsev 的工具改造计划互为因果链；“收效有限”为当事人判断，本页未附流量实测。
- **文献**：DSLXC-11144、DSLXC-11162（`ksummit.messages.8661`、`ksummit.messages.8715`，2023-11-07、2023-11-09），全文见 `raw_source.raw_json`

## 192.4 C编译器警告

- **要点**：Martin Uecker指出GCC已有-Wtype-limits（-Wextra激活）可警告size_t接收负值的写法，回应Rostedt对无符号比较警告的需求。
- **史料**：`ksummit.messages.8670`（Martin Uecker，2025-02-21）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8670 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 GCC 已有 -Wtype-limits（-Wextra 激活）这一实际编译选项为判据）；知识注定过时（总纲第 22 条——知识注定过时：所求警告早已存在，唯需知其开关）
- **辨析**：本块系 Martin Uecker 对 Rostedt 需求的直接回应，属工具现状的一手说明；“可警告 size_t 接收负值的写法”须以当期 GCC 实测核对。
- **文献**：DSLXC-11145（`ksummit.messages.8670`，2025-02-21），全文见 `raw_source.raw_json`

## 192.5 Rust架构定位

- **要点**：Miguel Ojeda澄清Rust for Linux并非替换C代码，而是把C API抽象为Rust API以静态保证不变式，红黑树等复用C API，Rust仅是C API又一消费者。
- **史料**：`ksummit.messages.8675`（Miguel Ojeda，2021-07-06）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8675 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：Rust 为 C 之消费者的定位与替换论并置）；动手者叙事（总纲第 10 条——动手者创造历史：以红黑树等复用 C API 的具体做法为分析单位）
- **辨析**：本块系 Miguel Ojeda 的定位澄清，属政策级表述；“并非替换 C 代码”为当事人自陈，非政策文本。
- **文献**：DSLXC-11146（`ksummit.messages.8675`，2021-07-06），全文见 `raw_source.raw_json`

## 192.6 提交标记规范

- **要点**：Mark Brown反对废除Link标记：常见动机是他人从git回溯邮件列表，如二分出故障后报告并查重；dig工具靠启发式且需另装。Miguel Ojeda指base-commit尾标在补丁无法干净应用时非常有用，git format-patch --base也可生成该标与prerequisite-patch-id。Kees Cook解释改用Link:标是因checkpatch对长URL行报警；建议正式化时可考虑markdown脚注风格，只求内核统一一种写法。
- **史料**：`ksummit.messages.8682`（Mark Brown，2025-10-15）、`ksummit.messages.8710`（Miguel Ojeda，2026-08-07）、`ksummit.messages.8777`（Kees Cook，2024-06-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8682 -->` `<!-- ROW_MINE: ksummit.messages.8710 -->` `<!-- ROW_MINE: ksummit.messages.8777 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 Link 标记、base-commit 尾标、prerequisite-patch-id 等具体格式机制为分析单位）；经验优先（总纲第 9 条——经验优先：以“二分出故障后回溯邮件列表并查重”这一实际用法为判据）
- **辨析**：三条分属不同发言人，均属标记格式之争；Cook 的“checkpatch 对长 URL 行报警”为改用 Link 的起因，其 markdown 脚注风格属提议。
- **文献**：DSLXC-11148、DSLXC-11160、DSLXC-11174（`ksummit.messages.8682`、`ksummit.messages.8710`、`ksummit.messages.8777`，2025-10-15、2026-08-07、2024-06-22），全文见 `raw_source.raw_json`

## 192.7 AI提交治理

- **要点**：Al Viro称AI幻觉式提交者应视同骗子，一旦抓到即按封禁处理，问题化为识别其马甲；反问是否要让此类人接近代码库。
- **史料**：`ksummit.messages.8683`（Al Viro，2025-08-05）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8683 -->`
- **史观**：法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：AI 幻觉式提交者被明示为“骗子”并适用封禁，问题被化为身份识别）；多方平等（总纲第 8 条——本体论上各方平等：封禁主张与“是否让其接近代码库”的反问并置）
- **辨析**：本块系 Al Viro 单方主张，措辞激烈；“一旦抓到即按封禁处理”为其立场，非已生效的治理规则。
- **文献**：DSLXC-11149（`ksummit.messages.8683`，2025-08-05），全文见 `raw_source.raw_json`

## 192.8 linus-next争议

- **要点**：Christoph Hellwig赞同Kees的PR健康检查机器人方案：报告补丁是否抄送列表、在next停留时长直方图、0day测试失败；称前两项易实现。Steven Rostedt解释因Linus要求改用主题分支致0day成功通知失效，并质疑推linux-next相比等0day机器人的收益，直指linus-next价值。
- **史料**：`ksummit.messages.8685`（Christoph Hellwig，2024-10-22）、`ksummit.messages.8803`（Steven Rostedt，2024-10-24）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8685 -->` `<!-- ROW_MINE: ksummit.messages.8803 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 PR 健康检查机器人（抄送、停留直方图、0day 失败）等具体方案为分析单位）；经验优先（总纲第 9 条——经验优先：以“因改用主题分支致 0day 成功通知失效”这一实操后果为判据）
- **辨析**：Hellwig 的方案与 Rostedt 的价值质疑互为对立；“直指 linus-next 价值”属当事人设问，本页未见结论。
- **文献**：DSLXC-11150、DSLXC-11181（`ksummit.messages.8685`、`ksummit.messages.8803`，2024-10-22、2024-10-24），全文见 `raw_source.raw_json`

## 192.9 cleanup.h风格

- **要点**：Steven Rostedt反对仅为声明而设显式作用域块，尤其变量用到函数末尾时在块内return，使函数主体错位、可读性差。Bart Van Assche引Google C++风格指南：仅在更清晰或更安全时用类型推导，质疑该原则是否适用于内核C与auto宏提议。
- **史料**：`ksummit.messages.8686`（Steven Rostedt，2025-11-18）、`ksummit.messages.8693`（Bart Van Assche，2025-11-18）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8686 -->` `<!-- ROW_MINE: ksummit.messages.8693 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：反对显式作用域块与引 Google 风格指南质疑类型推导两说并置）；经验优先（总纲第 9 条——经验优先：以“变量用到函数末尾时在块内 return 使函数主体错位”这一可读性后果为判据）
- **辨析**：两条均属风格之争，无强制规范；“Google C++ 风格指南是否适用于内核 C”为 Assche 的开放设问。
- **文献**：DSLXC-11151、DSLXC-11155（`ksummit.messages.8686`、`ksummit.messages.8693`，2025-11-18、2025-11-18），全文见 `raw_source.raw_json`

## 192.10 Rust panic语义

- **要点**：Greg KH澄清内核Rust panic不展开栈，直接走BUG()路径，回溯信息与其他BUG()调用一致，回应Bottomley对诊断能力的疑问。
- **史料**：`ksummit.messages.8691`（Greg KH，2025-02-26）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8691 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 panic 直接走 BUG() 路径这一具体实现为分析单位）；经验优先（总纲第 9 条——经验优先：以“回溯信息与其他 BUG() 调用一致”这一实际行为为判据）
- **辨析**：本块系 Greg KH 对 Bottomley 疑问的澄清，属实现层一手说明，非设计讨论。
- **文献**：DSLXC-11153（`ksummit.messages.8691`，2025-02-26），全文见 `raw_source.raw_json`

## 192.11 trivial树存废

- **要点**：Thomas Gleixner主张彻底废除trivial@列表，称其不解决任何问题，新变体亦将同样衰亡，回应复兴trivial树的提议。
- **史料**：`ksummit.messages.8692`（Thomas Gleixner，2021-04-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8692 -->`
- **史观**：知识注定过时（总纲第 22 条——知识注定过时：trivial@ 列表“不解决任何问题”，新变体亦将同样衰亡）；多方平等（总纲第 8 条——本体论上各方平等：废除主张与复兴提议并置）
- **辨析**：本块系 Thomas Gleixner 的反对意见，其“新变体亦将同样衰亡”为历史推断，非既成事实。
- **文献**：DSLXC-11154（`ksummit.messages.8692`，2021-04-22），全文见 `raw_source.raw_json`

## 192.12 Bugzilla困境

- **要点**：Ted Tso剖析Bugzilla困境：组件自动抄送靠手工魔改且上游零支持，无专人维护则库迅速失效；开发者普遍不跟进报告，原因存争议。
- **史料**：`ksummit.messages.8695`（Theodore Ts'o，2022-10-02）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8695 -->`
- **史观**：知识注定过时（总纲第 22 条——知识注定过时：Bugzilla 组件自动抄送靠手工魔改、上游零支持，无专人维护则库迅速失效）；动手者叙事（总纲第 10 条——动手者创造历史：以组件抄送与专人维护等运维条件为分析单位）
- **辨析**：本块系 Theodore Ts'o 的机制剖析；“开发者普遍不跟进报告，原因存争议”为当事人明示的未决问题。
- **文献**：DSLXC-11156（`ksummit.messages.8695`，2022-10-02），全文见 `raw_source.raw_json`

## 192.13 sashiko审查模型

- **要点**：Steven Rostedt支持sashiko报告opt-in：误报可事后退出，漏报则安全问题无人察觉直至被利用，宁可忍受假阳性。James Bottomley披露多起AI补丁工具借sashiko提示向linux-scsi群发恶意硬件修复，他疲于答复“不在我威胁模型”，故提议从源头整治。
- **史料**：`ksummit.messages.8699`（Steven Rostedt，2026-07-22）、`ksummit.messages.8731`（James Bottomley，2026-07-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8699 -->` `<!-- ROW_MINE: ksummit.messages.8731 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：opt-in 与漏报风险的两难和恶意群发的实况并置）；经验优先（总纲第 9 条——经验优先：以“多起 AI 补丁工具借 sashiko 提示向 linux-scsi 群发恶意硬件修复”这一实际事态为判据）
- **辨析**：Rostedt 的“宁可忍受假阳性”为设计取舍；Bottomley 的群发事态属可核查的滥用实例，本页未附具体补丁清单。
- **文献**：DSLXC-11157、DSLXC-11167（`ksummit.messages.8699`、`ksummit.messages.8731`，2026-07-22、2026-07-22），全文见 `raw_source.raw_json`

## 192.14 unsafe Rust难度

- **要点**：Ventura Jack引AWS正式验证Rust标准库的众包项目与CVE-2024-27308，论证unsafe Rust实际很难；并称ADT与模式匹配是可加入C的低垂果实。
- **史料**：`ksummit.messages.8701`（Ventura Jack，2025-02-26）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8701 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 AWS 正式验证 Rust 标准库的众包项目与 CVE-2024-27308 两个可查实例为判据）；多方平等（总纲第 8 条——本体论上各方平等：unsafe Rust 之难与“ADT 与模式匹配是可加入 C 的低垂果实”并置）
- **辨析**：本块系 Ventura Jack 的单方论证；CVE-2024-27308 为可反查编号，其“低垂果实”为当事人判断。
- **文献**：DSLXC-11158（`ksummit.messages.8701`，2025-02-26），全文见 `raw_source.raw_json`

## 192.15 邮件礼仪争论

- **要点**：James Bottomley以逆向驾驶比喻反驳NeilBrown，主张全引文本等问题应靠全局邮件礼仪解决，而非依赖个人能力兜底。
- **史料**：`ksummit.messages.8706`（James Bottomley，2023-10-25）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8706 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：全局邮件礼仪与个人能力兜底两说并置）；经验优先（总纲第 9 条——经验优先：以逆向驾驶比喻这一经验类比为论证方式）
- **辨析**：本块系 James Bottomley 对 NeilBrown 的反驳；比喻为修辞，落书须还原其“靠全局礼仪解决”的实质主张。
- **文献**：DSLXC-11159（`ksummit.messages.8706`，2023-10-25），全文见 `raw_source.raw_json`

## 192.16 Folio设计分歧

- **要点**：Kent Overstreet主张以沟通代替NACK规则，梳理Folio两路线（仅页缓存或兼含匿名页），称Willy拆解struct page的路线合理，匿名页Folio化仍存疑。
- **史料**：`ksummit.messages.8713`（Kent Overstreet，2021-09-16）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8713 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“仅页缓存”与“兼含匿名页”两条技术路线为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：Willy 拆解 struct page 的路线与匿名页 Folio 化存疑并置）
- **辨析**：本块系 Kent Overstreet 的梳理；“以沟通代替 NACK 规则”为其主张，“匿名页 Folio 化仍存疑”为保留意见，本页未见裁决。
- **文献**：DSLXC-11161（`ksummit.messages.8713`，2021-09-16），全文见 `raw_source.raw_json`

## 192.17 AI质量门槛

- **要点**：Sasha Levin以v6.15..v6.16约20%提交（2734/14639）为修复的事实，反驳对AI设高于人类的质量门槛，称内核自身bug率已超1%。
- **史料**：`ksummit.messages.8721`（Sasha Levin，2025-08-06）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8721 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 v6.15..v6.16 共 14639 提交中 2734 个修复（约 20%）这一实测为判据）；多方平等（总纲第 8 条——本体论上各方平等：对 AI 设更高门槛的主张与“内核自身 bug 率已超 1%”的反驳并置）
- **辨析**：14639 与 2734 为可复算的 git 统计口径；“内核自身 bug 率已超 1%”为当事人推论，落书须标明其估算性质。
- **文献**：DSLXC-11163（`ksummit.messages.8721`，2025-08-06），全文见 `raw_source.raw_json`

## 192.18 厂商开源策略

- **要点**：Jason Gunthorpe补充成功开源驱动项目需客户拉动力：若市场不同向推动开放，仅靠规则与厂商意愿参与则成功概率大降。
- **史料**：`ksummit.messages.8723`（Jason Gunthorpe，2024-07-29）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8723 -->`
- **史观**：法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：开源驱动项目的成败被归因于客户拉动这一市场利益格局）；经验优先（总纲第 9 条——经验优先：以“仅靠规则与厂商意愿参与则成功概率大降”这一经验判断为判据）
- **辨析**：本块系 Jason Gunthorpe 的补充论断，属结构性判断；“成功概率大降”为定性估计，未附案例统计。
- **文献**：DSLXC-11164（`ksummit.messages.8723`，2024-07-29），全文见 `raw_source.raw_json`

## 192.19 回归修复时效

- **要点**：Thorsten Leemhuis统计7.1周期39起回归：中位20天修复，远超Linus“一周内”经验法则；修复多已就绪而卡在评审提交，并列出高效子系统做法与具体commit。
- **史料**：`ksummit.messages.8728`（Thorsten Leemhuis，2026-07-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8728 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 7.1 周期 39 起回归、中位 20 天修复这一带数字的统计为判据）；知识注定过时（总纲第 22 条——知识注定过时：远超 Linus“一周内”经验法则，且修复多已就绪而卡在评审提交）
- **辨析**：本块系 Thorsten Leemhuis 的全页唯一完整统计，属本页最高证据等级；其“高效子系统做法与具体 commit”为可反查清单，落书须与原表核对。
- **文献**：DSLXC-11165（`ksummit.messages.8728`，2026-07-22），全文见 `raw_source.raw_json`

## 192.20 Rust抽象维护

- **要点**：Sasha Levin强烈反对Ojeda：存在Rust抽象只说明曾有人做过，作者离开后即成孤儿抽象；反问改驱动API难道要Greg KH代写代码。
- **史料**：`ksummit.messages.8729`（Sasha Levin，2021-07-06）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8729 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“作者离开后即成孤儿抽象”这一维护现实为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：抽象存在与抽象可维护性两说并置）
- **辨析**：本块系 Sasha Levin 对 Ojeda 的强烈反对；“反问改驱动 API 难道要 Greg KH 代写代码”为修辞性设问，属立场表达。
- **文献**：DSLXC-11166（`ksummit.messages.8729`，2021-07-06），全文见 `raw_source.raw_json`

## 192.21 文档建设

- **要点**：Vegard Nossum自述文档重构补丁搁置致弃坑，建议更积极合并文档补丁加增量修正，并倡议月度例会与docs路线图，指无专职文档岗位、LF资助实验失败。
- **史料**：`ksummit.messages.8733`（Vegard Nossum，2025-08-30）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8733 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“更积极合并文档补丁加增量修正、月度例会与 docs 路线图”等具体机制为分析单位）；经验优先（总纲第 9 条——经验优先：以“文档重构补丁搁置致弃坑、LF 资助实验失败”等实际结果为判据）
- **辨析**：本块系 Vegard Nossum 的自述与倡议；“无专职文档岗位”为组织实况判断，其倡议本页未见采纳。
- **文献**：DSLXC-11168（`ksummit.messages.8733`，2025-08-30），全文见 `raw_source.raw_json`

## 192.22 维护者支持组

- **要点**：Shuah以CoC委员身份反驳“只管维护者行为”论：多数报告属社区误解且幕后化解；认同维护者也是人，但质疑支持小组与CoC职责重叠。
- **史料**：`ksummit.messages.8742`（Shuah，2023-09-19）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8742 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：CoC 委员的职责说明与支持小组提案并置）；经验优先（总纲第 9 条——经验优先：以“多数报告属社区误解且幕后化解”这一实际处理记录为判据）
- **辨析**：本块系 Shuah 以 CoC 委员身份的反驳；“支持小组与 CoC 职责重叠”为其质疑，非定论。
- **文献**：DSLXC-11169（`ksummit.messages.8742`，2023-09-19），全文见 `raw_source.raw_json`

## 192.23 稳定版队列机制

- **要点**：Greg KH指stable-queue与linux-stable-rc树多年来持续收录稳定补丁，回应Rostedt关于合并窗口期连续稳定分支的提问。
- **史料**：`ksummit.messages.8755`（Greg KH，2024-06-26）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8755 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 stable-queue 与 linux-stable-rc 树多年来持续收录这一既存事实为判据）；知识注定过时（总纲第 22 条——知识注定过时：所问机制早已存在）
- **辨析**：本块系 Greg KH 对 Rostedt 提问的直接回应，属机制现状的一手说明。
- **文献**：DSLXC-11170（`ksummit.messages.8755`，2024-06-26），全文见 `raw_source.raw_json`

## 192.24 列表平台迁移

- **要点**：Jonathan Corbet应用Konstantin文档补丁：vger已从majordomo+zmailer迁移至mlmmj并统一为subspace平台，弃用lore的/r/子路径建议。
- **史料**：`ksummit.messages.8762`（Jonathan Corbet，2024-07-03）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8762 -->`
- **史观**：知识注定过时（总纲第 22 条——知识注定过时：vger 已从 majordomo+zmailer 迁移至 mlmmj 并统一为 subspace 平台）；动手者叙事（总纲第 10 条——动手者创造历史：以平台迁移与弃用 lore 的 /r/ 子路径建议为分析单位）
- **辨析**：本块系 Jonathan Corbet 应用 Konstantin 文档补丁的落地记录，属基础设施一手；“弃用 /r/ 子路径建议”为建议，非强制。
- **文献**：DSLXC-11171（`ksummit.messages.8762`，2024-07-03），全文见 `raw_source.raw_json`

## 192.25 Rust内存安全争论

- **要点**：Al Viro称其见过的ksmbd漏洞均与内存安全无关，即使全用Rust重写也会原样出现，反驳以ksmbd论证Rust必要性的说法。
- **史料**：`ksummit.messages.8770`（Al Viro，2022-06-26）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8770 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：以 ksmbd 论证 Rust 必要性与“漏洞均与内存安全无关”的反驳并置）；经验优先（总纲第 9 条——经验优先：以“其见过的 ksmbd 漏洞”这一经验清单为判据）
- **辨析**：本块系 Al Viro 的反驳；“即使全用 Rust 重写也会原样出现”为当事人判断，属反事实论断。
- **文献**：DSLXC-11173（`ksummit.messages.8770`，2022-06-26），全文见 `raw_source.raw_json`

## 192.26 LLM标签信号

- **要点**：Johannes Weiner指二进制LLM标签信噪比差：AI参与度从起草到全代理、人工审查程度差异巨大，且标签已带污名，难以在提交元数据刻画分工。
- **史料**：`ksummit.messages.8779`（Johannes Weiner，2026-07-17）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8779 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“AI 参与度从起草到全代理、人工审查程度差异巨大”这一实际谱系为判据）；多方平等（总纲第 8 条——本体论上各方平等：二进制标签与提交元数据刻画分工的诉求并置）
- **辨析**：本块系 Johannes Weiner 的分析；“标签已带污名”为社区观感判断，非统计结论。
- **文献**：DSLXC-11175（`ksummit.messages.8779`，2026-07-17），全文见 `raw_source.raw_json`

## 192.27 Rust驱动安全机制

- **要点**：Laurent Pinchart主张以对象生命周期为中心，remove后由子系统阻止整类API调用，而非Rust逐次运行时检查IO内存撤销，称后者是在解决不应存在的问题。
- **史料**：`ksummit.messages.8780`（Laurent Pinchart，2021-07-21）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8780 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“remove 后由子系统阻止整类 API 调用”这一以对象生命周期为中心的机制为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：子系统级阻断与 Rust 逐次运行时检查两路线并置）
- **辨析**：本块系 Laurent Pinchart 的主张；“称后者是在解决不应存在的问题”为对既有方案的价值判断。
- **文献**：DSLXC-11176（`ksummit.messages.8780`，2021-07-21），全文见 `raw_source.raw_json`

## 192.28 维护者倦怠

- **要点**：Jonathan Cameron自述IIO评审触底时向大厂求助奏效，CXL等新领域仍缺评审人；称推动公司投入非本业务评审很难，华为内部亦在摸索。
- **史料**：`ksummit.messages.8783`（Jonathan Cameron，2023-08-24）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8783 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“IIO 评审触底时向大厂求助奏效、CXL 等新领域仍缺评审人”这一实际经历为判据）；法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：推动公司投入非本业务评审难，被还原为雇主利益问题）
- **辨析**：本块系 Jonathan Cameron 的自述；“华为内部亦在摸索”为组织实况转述，本页未附内部方案。
- **文献**：DSLXC-11177（`ksummit.messages.8783`，2023-08-24），全文见 `raw_source.raw_json`

## 192.29 rustc兼容保障

- **要点**：Ralf Jung举例本月rustc对内核aarch64禁FP方式发出可靠性警告，内核在警告进稳定版前已备好补丁并回移；内核用nightly特性故有CI特别照顾，目标降至零。
- **史料**：`ksummit.messages.8791`（Ralf Jung，2025-02-28）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8791 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 rustc 可靠性警告与内核提前回移这一双向协调机制为分析单位）；经验优先（总纲第 9 条——经验优先：以“内核在警告进稳定版前已备好补丁并回移”这一实际时间线为判据）
- **辨析**：本块系 Ralf Jung 披露的协调实例，属机制级一手；“目标降至零”为团队目标，非既成结果。
- **文献**：DSLXC-11178（`ksummit.messages.8791`，2025-02-28），全文见 `raw_source.raw_json`

## 192.30 UBSan生产应用

- **要点**：Kees Cook反驳消毒器不能上生产的旧论：内核UBSan与HW-KASan已在Android、ChromeOS生产环境运行近五年，Ubuntu与Fedora默认开启边界消毒。
- **史料**：`ksummit.messages.8792`（Kees Cook，2025-03-02）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8792 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以内核 UBSan 与 HW-KASan 已在 Android、ChromeOS 生产环境运行近五年这一实测为判据）；知识注定过时（总纲第 22 条——知识注定过时：消毒器不能上生产的旧论已被实际部署推翻）
- **辨析**：本块系 Kees Cook 的反驳；“近五年”与“Ubuntu 与 Fedora 默认开启”为可核事实，落书须标明版本口径。
- **文献**：DSLXC-11179（`ksummit.messages.8792`，2025-03-02），全文见 `raw_source.raw_json`

## 192.31 文档构建环境

- **要点**：Mauro Carvalho Chehab解释LTS发行版Sphinx过旧是默认推荐venv的主因；RHEL9、SUSE 15 SP4、Ubuntu 22.04达标后可改荐发行版包，Debian bullseye仍2.5.0。
- **史料**：`ksummit.messages.8793`（Mauro Carvalho Chehab，2022-06-28）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8793 -->`
- **史观**：知识注定过时（总纲第 22 条——知识注定过时：LTS 发行版 Sphinx 过旧是默认推荐 venv 的主因，Debian bullseye 仍 2.5.0）；动手者叙事（总纲第 10 条——动手者创造历史：以“达标后可改荐发行版包”这一条件性切换为分析单位）
- **辨析**：本块系 Mauro Carvalho Chehab 的现状说明；达标发行版清单与版本号为可核事实，落笔须注明时点。
- **文献**：DSLXC-11180（`ksummit.messages.8793`，2022-06-28），全文见 `raw_source.raw_json`
