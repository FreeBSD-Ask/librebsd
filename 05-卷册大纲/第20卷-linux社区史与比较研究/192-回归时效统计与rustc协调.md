# 192. 回归修复时效统计、Folio 两路线与 rustc 兼容协调机制（ks p56）

> 来源：ksummit 独有 p56（50 封全读，2021-04 至 2026-08：Leemhuis 全页唯一带完整统计邮件 7.1 周期 39 起回归中位 20 天才修复远超 Linus 一周内法则并附 14 条高效子系统做法清单；Overstreet 2021 年 Folio 争论浓缩陈述极简仅页缓存与极大含匿名页两路线 Willy 拆解 struct page 策略及 Johannes 保留意见；Levin 用 git log 实测 v6.15..v6.16 共 14639 提交 2734 个修复约 20% 反驳对 AI 设更高门槛；Ralf Jung 披露 rustc 与内核协调机制实例 aarch64 FP 可靠性警告提前预警与 nightly 特性 CI 特别照顾；AI 补丁标注四封、cleanup.h 风格与 linus-next 争议各三封）
> 判定：40 CAND / 10 NV。主题分布：AI补丁标注 4、UMN实验争议 1、THE REST分流 2、C编译器警告 1、Rust架构定位 1、提交标记规范 3、AI提交治理 1、linus-next争议 2、cleanup.h风格 2、Rust panic语义 1、trivial树存废 1、Bugzilla困境 1、sashiko审查模型 2、unsafe Rust难度 1、邮件礼仪争论 1、Folio设计分歧 1、AI质量门槛 1、厂商开源策略 1、回归修复时效 1、Rust抽象维护 1、文档建设 1、维护者支持组 1、稳定版队列机制 1、列表平台迁移 1、Rust内存安全争论 1、LLM标签信号 1、Rust驱动安全机制 1、维护者倦怠 1、rustc兼容保障 1、UBSan生产应用 1、文档构建环境 1。

## 192.1 AI补丁标注

- 【Linux社区】Alexandre Belloni指静态检查器生成的修补常无意义，如永不触发的返回值检查；建议贡献者明示用工具发现问题并生成补丁，便于维护者直接忽略。 `<!-- ROW_MINE: ksummit.messages.8658 -->`
- 【Linux社区】Steven Rostedt质疑AI代写代码时签署人是否有权加Signed-off-by，尤其不知训练数据来源；若AI用了专利算法，签署者是否担法律风险。 `<!-- ROW_MINE: ksummit.messages.8680 -->`
- 【Linux社区】Miguel Ojeda认为工具生成内容指南已够清晰：要求理解整个提交并回应评审，维护者可酌情直接拒绝无法解释的补丁系列。 `<!-- ROW_MINE: ksummit.messages.8687 -->`
- 【Linux社区】Paul McKenney称在版权诉讼落定前不对开源项目用AI生成物，引DCO“有权提交”条款，指在途诉讼或使AI代码构成侵权，误收只能剔除并净室重写。 `<!-- ROW_MINE: ksummit.messages.8766 -->`

## 192.2 UMN实验争议

- 【Linux社区】Al Viro指出UMN团队实验结束后至今未公布所涉补丁的SHA1清单，缺乏原始数据即“记者会式科学”，以此回应宽恕与严惩之争。 `<!-- ROW_MINE: ksummit.messages.8660 -->`

## 192.3 THE REST分流

- 【Linux社区】Mark Brown判断LKML流量主要源于get_maintainer.pl自动抄送lkml，而非用户显式配置git-send-email，故THE REST分流收效有限。 `<!-- ROW_MINE: ksummit.messages.8661 -->`
- 【Linux社区】Konstantin Ryabitsev认同收件应由工具决定，计划改造工具不再对所有补丁抄送linux-kernel@vger，仅无其他列表匹配时才加。 `<!-- ROW_MINE: ksummit.messages.8715 -->`

## 192.4 C编译器警告

- 【Linux社区】Martin Uecker指出GCC已有-Wtype-limits（-Wextra激活）可警告size_t接收负值的写法，回应Rostedt对无符号比较警告的需求。 `<!-- ROW_MINE: ksummit.messages.8670 -->`

## 192.5 Rust架构定位

- 【Linux社区】Miguel Ojeda澄清Rust for Linux并非替换C代码，而是把C API抽象为Rust API以静态保证不变式，红黑树等复用C API，Rust仅是C API又一消费者。 `<!-- ROW_MINE: ksummit.messages.8675 -->`

## 192.6 提交标记规范

- 【Linux社区】Mark Brown反对废除Link标记：常见动机是他人从git回溯邮件列表，如二分出故障后报告并查重；dig工具靠启发式且需另装。 `<!-- ROW_MINE: ksummit.messages.8682 -->`
- 【Linux社区】Miguel Ojeda指base-commit尾标在补丁无法干净应用时非常有用，git format-patch --base也可生成该标与prerequisite-patch-id。 `<!-- ROW_MINE: ksummit.messages.8710 -->`
- 【Linux社区】Kees Cook解释改用Link:标是因checkpatch对长URL行报警；建议正式化时可考虑markdown脚注风格，只求内核统一一种写法。 `<!-- ROW_MINE: ksummit.messages.8777 -->`

## 192.7 AI提交治理

- 【Linux社区】Al Viro称AI幻觉式提交者应视同骗子，一旦抓到即按封禁处理，问题化为识别其马甲；反问是否要让此类人接近代码库。 `<!-- ROW_MINE: ksummit.messages.8683 -->`

## 192.8 linus-next争议

- 【Linux社区】Christoph Hellwig赞同Kees的PR健康检查机器人方案：报告补丁是否抄送列表、在next停留时长直方图、0day测试失败；称前两项易实现。 `<!-- ROW_MINE: ksummit.messages.8685 -->`
- 【Linux社区】Steven Rostedt解释因Linus要求改用主题分支致0day成功通知失效，并质疑推linux-next相比等0day机器人的收益，直指linus-next价值。 `<!-- ROW_MINE: ksummit.messages.8803 -->`

## 192.9 cleanup.h风格

- 【Linux社区】Steven Rostedt反对仅为声明而设显式作用域块，尤其变量用到函数末尾时在块内return，使函数主体错位、可读性差。 `<!-- ROW_MINE: ksummit.messages.8686 -->`
- 【Linux社区】Bart Van Assche引Google C++风格指南：仅在更清晰或更安全时用类型推导，质疑该原则是否适用于内核C与auto宏提议。 `<!-- ROW_MINE: ksummit.messages.8693 -->`

## 192.10 Rust panic语义

- 【Linux社区】Greg KH澄清内核Rust panic不展开栈，直接走BUG()路径，回溯信息与其他BUG()调用一致，回应Bottomley对诊断能力的疑问。 `<!-- ROW_MINE: ksummit.messages.8691 -->`

## 192.11 trivial树存废

- 【Linux社区】Thomas Gleixner主张彻底废除trivial@列表，称其不解决任何问题，新变体亦将同样衰亡，回应复兴trivial树的提议。 `<!-- ROW_MINE: ksummit.messages.8692 -->`

## 192.12 Bugzilla困境

- 【Linux社区】Ted Tso剖析Bugzilla困境：组件自动抄送靠手工魔改且上游零支持，无专人维护则库迅速失效；开发者普遍不跟进报告，原因存争议。 `<!-- ROW_MINE: ksummit.messages.8695 -->`

## 192.13 sashiko审查模型

- 【Linux社区】Steven Rostedt支持sashiko报告opt-in：误报可事后退出，漏报则安全问题无人察觉直至被利用，宁可忍受假阳性。 `<!-- ROW_MINE: ksummit.messages.8699 -->`
- 【Linux社区】James Bottomley披露多起AI补丁工具借sashiko提示向linux-scsi群发恶意硬件修复，他疲于答复“不在我威胁模型”，故提议从源头整治。 `<!-- ROW_MINE: ksummit.messages.8731 -->`

## 192.14 unsafe Rust难度

- 【Linux社区】Ventura Jack引AWS正式验证Rust标准库的众包项目与CVE-2024-27308，论证unsafe Rust实际很难；并称ADT与模式匹配是可加入C的低垂果实。 `<!-- ROW_MINE: ksummit.messages.8701 -->`

## 192.15 邮件礼仪争论

- 【Linux社区】James Bottomley以逆向驾驶比喻反驳NeilBrown，主张全引文本等问题应靠全局邮件礼仪解决，而非依赖个人能力兜底。 `<!-- ROW_MINE: ksummit.messages.8706 -->`

## 192.16 Folio设计分歧

- 【Linux社区】Kent Overstreet主张以沟通代替NACK规则，梳理Folio两路线（仅页缓存或兼含匿名页），称Willy拆解struct page的路线合理，匿名页Folio化仍存疑。 `<!-- ROW_MINE: ksummit.messages.8713 -->`

## 192.17 AI质量门槛

- 【Linux社区】Sasha Levin以v6.15..v6.16约20%提交（2734/14639）为修复的事实，反驳对AI设高于人类的质量门槛，称内核自身bug率已超1%。 `<!-- ROW_MINE: ksummit.messages.8721 -->`

## 192.18 厂商开源策略

- 【Linux社区】Jason Gunthorpe补充成功开源驱动项目需客户拉动力：若市场不同向推动开放，仅靠规则与厂商意愿参与则成功概率大降。 `<!-- ROW_MINE: ksummit.messages.8723 -->`

## 192.19 回归修复时效

- 【Linux社区】Thorsten Leemhuis统计7.1周期39起回归：中位20天修复，远超Linus“一周内”经验法则；修复多已就绪而卡在评审提交，并列出高效子系统做法与具体commit。 `<!-- ROW_MINE: ksummit.messages.8728 -->`

## 192.20 Rust抽象维护

- 【Linux社区】Sasha Levin强烈反对Ojeda：存在Rust抽象只说明曾有人做过，作者离开后即成孤儿抽象；反问改驱动API难道要Greg KH代写代码。 `<!-- ROW_MINE: ksummit.messages.8729 -->`

## 192.21 文档建设

- 【Linux社区】Vegard Nossum自述文档重构补丁搁置致弃坑，建议更积极合并文档补丁加增量修正，并倡议月度例会与docs路线图，指无专职文档岗位、LF资助实验失败。 `<!-- ROW_MINE: ksummit.messages.8733 -->`

## 192.22 维护者支持组

- 【Linux社区】Shuah以CoC委员身份反驳“只管维护者行为”论：多数报告属社区误解且幕后化解；认同维护者也是人，但质疑支持小组与CoC职责重叠。 `<!-- ROW_MINE: ksummit.messages.8742 -->`

## 192.23 稳定版队列机制

- 【Linux社区】Greg KH指stable-queue与linux-stable-rc树多年来持续收录稳定补丁，回应Rostedt关于合并窗口期连续稳定分支的提问。 `<!-- ROW_MINE: ksummit.messages.8755 -->`

## 192.24 列表平台迁移

- 【Linux社区】Jonathan Corbet应用Konstantin文档补丁：vger已从majordomo+zmailer迁移至mlmmj并统一为subspace平台，弃用lore的/r/子路径建议。 `<!-- ROW_MINE: ksummit.messages.8762 -->`

## 192.25 Rust内存安全争论

- 【Linux社区】Al Viro称其见过的ksmbd漏洞均与内存安全无关，即使全用Rust重写也会原样出现，反驳以ksmbd论证Rust必要性的说法。 `<!-- ROW_MINE: ksummit.messages.8770 -->`

## 192.26 LLM标签信号

- 【Linux社区】Johannes Weiner指二进制LLM标签信噪比差：AI参与度从起草到全代理、人工审查程度差异巨大，且标签已带污名，难以在提交元数据刻画分工。 `<!-- ROW_MINE: ksummit.messages.8779 -->`

## 192.27 Rust驱动安全机制

- 【Linux社区】Laurent Pinchart主张以对象生命周期为中心，remove后由子系统阻止整类API调用，而非Rust逐次运行时检查IO内存撤销，称后者是在解决不应存在的问题。 `<!-- ROW_MINE: ksummit.messages.8780 -->`

## 192.28 维护者倦怠

- 【Linux社区】Jonathan Cameron自述IIO评审触底时向大厂求助奏效，CXL等新领域仍缺评审人；称推动公司投入非本业务评审很难，华为内部亦在摸索。 `<!-- ROW_MINE: ksummit.messages.8783 -->`

## 192.29 rustc兼容保障

- 【Linux社区】Ralf Jung举例本月rustc对内核aarch64禁FP方式发出可靠性警告，内核在警告进稳定版前已备好补丁并回移；内核用nightly特性故有CI特别照顾，目标降至零。 `<!-- ROW_MINE: ksummit.messages.8791 -->`

## 192.30 UBSan生产应用

- 【Linux社区】Kees Cook反驳消毒器不能上生产的旧论：内核UBSan与HW-KASan已在Android、ChromeOS生产环境运行近五年，Ubuntu与Fedora默认开启边界消毒。 `<!-- ROW_MINE: ksummit.messages.8792 -->`

## 192.31 文档构建环境

- 【Linux社区】Mauro Carvalho Chehab解释LTS发行版Sphinx过旧是默认推荐venv的主因；RHEL9、SUSE 15 SP4、Ubuntu 22.04达标后可改荐发行版包，Debian bullseye仍2.5.0。 `<!-- ROW_MINE: ksummit.messages.8793 -->`
