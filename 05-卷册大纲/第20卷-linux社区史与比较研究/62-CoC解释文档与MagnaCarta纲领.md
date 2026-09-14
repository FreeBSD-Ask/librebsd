# 62 【Linux社区】CoC解释文档与MagnaCarta纲领

> 来源：ksummit-discuss p114（50 封全读，2018-10-18/23 为主，夹杂 2014-05 档案信与回归追踪通讯）。
> 判定：49 CAND / 1 NV。主题分布：Greg解释文档系列 8、保密承诺与报案权 11、CallToAction 6、MagnaCarta纲领 10、GITPULL与冷却令 5、程序之辩与Samba先例 2、2014档案与回归追踪 6、email措辞收束 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p114（pk 349906-349955）的逐封提取（49 CAND / 1 NV），全 7 块采用**导语＋带锚条目体例**：每块由“## 62.x 【Linux社区】题名”＋导语段＋“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——导语段承担“要点”职能、带锚条目承担“史料”与“史料锚”职能（ROW_MINE 坐标与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 62.1 【Linux社区】Rowand 收束与 Greg KH [PATCH 0/7] CoC 解释文档系列

2018-10-20 CoC 争议的制度化出口：Greg KH 七补丁系列（Mason 删维护者责任段+90 人 Ack 名单+153 行 Interpretation 文档全文——执法仅最后手段/TAB 委员会/季度匿名报告）+Rowand 对 email 措辞之辩的收束确认。

- 【Linux社区】Rowand 接受 not 修正（“Yes, thank you”）；Bottomley 的 doxxing/房产记录澄清“帮助理解此前全部发言”；删“such as”方案“Looks good to me”——email 措辞之辩收束 `<!-- ROW_MINE: ksummit-discuss.messages.349906 -->`
- 【Linux社区】Greg KH [PATCH 0/7]：删困惑段+新增 CoC Interpretation 文档；前两补丁曾私下广泛征求意见（GPLv3 声明等政策文件传统）、因原 CoC 加入方式出乎意料被要求公开重发；公开致谢 Mishi Choudhary 出任调解人 `<!-- ROW_MINE: ksummit-discuss.messages.349907 -->`
- 【Linux社区】[PATCH 1/7] Mason 删维护者执行责任段 4 行：“发出错误信息——我们只是要维护者做解决方案的一部分而不自己违反”；90+ Acked 大名单（Linus/Morton/tglx/Ingo 全在） `<!-- ROW_MINE: ksummit-discuss.messages.349908 -->`
- 【Linux社区】[PATCH 2/7] interpretation 153 行全文：maintainer=MAINTAINERS 所列；lead by example 但无单边执法新要求；“不被视为违规报告除非你想如此”；enforcement 仅作最后手段；拒绝不合适贡献不违反 CoC；Scope=MAINTAINERS 列表全覆盖+bugzilla 遵循+不禁止保留名字邮箱评论；CoC 前既有内容不追责、不当语言视作 bug；Enforcement=CoC 委员会+TAB 2/3 票可推翻+季度匿名报告含投票细节 `<!-- ROW_MINE: ksummit-discuss.messages.349909 -->`
- 【Linux社区】[PATCH 3/7] TAB 缩写先定义后使用（Morimoto Reported-by） `<!-- ROW_MINE: ksummit-discuss.messages.349910 -->`
- 【Linux社区】[PATCH 4/7] 两文档互链 :ref:`code_of_conduct(_interpretation)` `<!-- ROW_MINE: ksummit-discuss.messages.349911 -->`
- 【Linux社区】[PATCH 5/7] 委员会 URL 补 kernel.org/code-of-conduct.html `<!-- ROW_MINE: ksummit-discuss.messages.349913 -->`
- 【Linux社区】[PATCH 6/7] 联系邮箱改为 CoC 委员会 conduct@kernel.org（不再整个 TAB） `<!-- ROW_MINE: ksummit-discuss.messages.349914 -->`
- 【Linux社区】[PATCH 7/7] Greg 自任 CoC 文件维护者（MAINTAINERS 条目 S: Supported）——“文件是我引入的、愿意维护” `<!-- ROW_MINE: ksummit-discuss.messages.349915 -->`

## 62.2 【Linux社区】保密承诺、执法报案权与 LF 律师审查

PATCH 6/7 保密条款引出的法理交锋：Cox 的数据保护法/天主教会对比例证与报案权主张、Trond 的法域管辖与 terms-of-use 替代方案、Tim Bird 的在线范围论、Bottomley 合并方案与受害者保密意愿论、LF 律师审查的 Ted-Greg 双重确认。

- 【Linux社区】Alan Cox 炮轰保密承诺：委员会保不了密——数据保护法/报告法之下“指望事件对被举报者保密的人活在梦乡”；至少加 (except where required by law)；严重事件应报执法——“你在设立让天主教会陷入麻烦的政策”；否则“二十年后向媒体解释为何什么都没做” `<!-- ROW_MINE: ksummit-discuss.messages.349916 -->`
- 【Linux社区】Geert 纠错：URL 只指向 CoC 而非 TAB 成员名单 `<!-- ROW_MINE: ksummit-discuss.messages.349917 -->`
- 【Linux社区】Trond Myklebust：委员会如何应对执法查询、向哪个法域报告？“为何要走处理严重事件的路——这超出 CoC 仲裁的范围；甚至建议别人是否报告在世界上很多地方都会惹麻烦” `<!-- ROW_MINE: ksummit-discuss.messages.349918 -->`
- 【Linux社区】jonsmirl：律师须过审文档但未见他们发声；Mauro 担心此文写法在巴西构成约束性合同 `<!-- ROW_MINE: ksummit-discuss.messages.349919 -->`
- 【Linux社区】Tim Bird 反驳 Cox：过去 TAB 对公众保密大多成功、季度匿名报告即为此设；被举报者可知指控多在法律领域——多数违规报告不在其中；CoC 范围只覆盖在线交互（列表/git/bugzilla）“很难实施人身伤害且留有持久公开痕迹——类比不当” `<!-- ROW_MINE: ksummit-discuss.messages.349920 -->`
- 【Linux社区】Trond terms-of-use 论：若范围只是在线交互、为何要进内核树？列表/git/bugzilla 都可用使用条款页明确行为规范与仲裁机制（含法律管辖地）——“把 CoC 塞进内核代码需要比规范在线行为更强的理由” `<!-- ROW_MINE: ksummit-discuss.messages.349921 -->`
- 【Linux社区】Bottomley 合并方案：其策展补丁同改该节（Enforcement 节+CoC 委员会+法定例外+Interpretation 链接）；策展系列只是起点、辩论后可作终集；“多数法系尊重受害者保密意愿、自动报案对弱势群体是重大威慑” `<!-- ROW_MINE: ksummit-discuss.messages.349922 -->`
- 【Linux社区】Cox 回 Tim Bird：“谁说的”一般安全但 accused 可依数据保护法请求个人数据（含 scrubbed 邮件）；“我看不出它明确写了‘有人若在 kernel summit 冒犯我们就拒听’——真的吗？” `<!-- ROW_MINE: ksummit-discuss.messages.349926 -->`
- 【Linux社区】tglx：Kernel summit/Maintainer summit 属于所附会议的 CoC 管辖 `<!-- ROW_MINE: ksummit-discuss.messages.349927 -->`
- 【Linux社区】Ted：LF 律师已审 CoC 与本补丁集、发送之前 `<!-- ROW_MINE: ksummit-discuss.messages.349929 -->`
- 【Linux社区】Greg 确认：“That is correct.”（LF 律师审查属实） `<!-- ROW_MINE: ksummit-discuss.messages.349931 -->`

## 62.3 【Linux社区】NeilBrown Call to Action 与 Ted 权威回应

NeilBrown 的四 hashtag 宣言（#Iobject/#Iforgive/#Iapologise/#Isupportreversion）与各方回应：Triplett 的“文档就在树里”反问、Perches-Dunlap 的进程反对、Ted 的权威叙事（Linus 指令+git 统计咨询+Greg 义务承担+Gamergate 恐惧渲染）。

- 【Linux社区】NeilBrown Call to Action：“我拒绝此 CoC 及其‘制定’进程为非法”（#Iobject）；呼吁反对者发声；“我们不需要 CoC 而需要 Leadership in conduct——没有领导力任何代码都像笑话”；呼吁 Linus 从忏悔走向悔改、社区报以宽恕与恢复（#Iforgive+代表社区道歉 #Iapologise）；呼吁 Greg 放弃强制、revert 8a104f8b5867c68（#Isupportreversion） `<!-- ROW_MINE: ksummit-discuss.messages.349932 -->`
- 【Linux社区】Triplett 反问：“我想读的文档已在 **Documentation/process/code-of-conduct.rst**”；追问 Neil 实际关切；“我确实想丢掉该系列大部分——一半削弱文档本意；但原 commit 值得庆祝” `<!-- ROW_MINE: ksummit-discuss.messages.349933 -->`
- 【Linux社区】Perches：“描述愉快互动愿望合法有用、但拒绝这一进程、以私人非公开方式改革充其量 poor form”；Dunlap 双 Agree `<!-- ROW_MINE: ksummit-discuss.messages.349934 -->`
- 【Linux社区】Perches 正式立场重申（怪异换行格式原文如此）——拒绝进程与私下改革方式 `<!-- ROW_MINE: ksummit-discuss.messages.349936 -->`
- 【Linux社区】Ted 权威长文：CoC 非 Greg 强加——指令/签署/时点皆 Linus、初始 commit 极少评审正因 Linus -rc4 休假前不愿被认为背后搞鬼；本系列大量 Ack 因事前以 git 统计与 top contributors 巨量咨询；Greg 出于义务感接下吃了很多 flak——“我感谢他做这不讨好的任务”；Gamergate 般外部恐惧渲染促成 interpretation 文档；技术理由拒码不会被影子委员会二次猜测、Netfilter 版权流氓先例仍在；最终目标是文化变革——Neil 说得对重要的不是文档而是行为 `<!-- ROW_MINE: ksummit-discuss.messages.349937 -->`
- 【Linux社区】Pavel Acked Geert 删列表：“更想回旧 code of conflict。但即便如此也是改进” `<!-- ROW_MINE: ksummit-discuss.messages.349941 -->`

## 62.4 【Linux社区】Magna Carta 纲领与无力感之辩

NeilBrown 的权力结构分析与 Magna Carta 替代纲领：无力感作为伤害主因的核心命题、Ted 的技术质量论驳斥、Viro 的 petition 现实主义与双头制质问、团队维护者制辩护与 Carpenter 的羞辱式拒绝两案实证——CoC 时代关于权力与无力的最深一轮辩论。

- 【Linux社区】NeilBrown Magna Carta 纲领：现行文档 upside down——此类文档意义在限制强者；普通参与者几乎无权力（lkml 噪声洪流/bugzilla 鬼城）、唯一力量=贡献价值×被倾听；Linus 拥有全部权力——patches 是通货；范本该是 Magna Carta——“我们不需要维护者告诉参与者如何行为、可能需要维护者告诉 Linus 如何行为”；替代补丁通道（“无法共事时 Linus/Andrew 直接考虑”）；“伤害不在虐待而在无力感”（petition to caesar 比喻）；若 Linus 不守住新敏感可设 Greg 共同维护者通道；三条件：限制强者/自愿采纳/替代补丁流 `<!-- ROW_MINE: ksummit-discuss.messages.349940 -->`
- 【Linux社区】Ted 驳 Neil 框架：“不同意你的框架/分析/方案”；补丁不因粗鲁被拒、因技术质量不足被拒；刷屏+无视改进建议者可被拉黑——“把烂补丁提交者拉黑不是 CoC 违规”；真实案例：新人刷不编译未经测试补丁终被 LKML 封禁；“以为人们想权力之旅拒绝健康代码是完全误诊” `<!-- ROW_MINE: ksummit-discuss.messages.349943 -->`
- 【Linux社区】Neil 反问：“正确。补丁不会因维护者粗鲁而投递、不投递就不会被接受”；“你不同意伤害主因是无力感吗？没有这一点我们可能在不同的星球” `<!-- ROW_MINE: ksummit-discuss.messages.349944 -->`
- 【Linux社区】Neil 驳 Ted：对“被告知去做+出于义务”两句加着重号——“被告知去做和出于义务不是做错事的借口；我真心惊讶你会觉得这相关——我错过了什么？” `<!-- ROW_MINE: ksummit-discuss.messages.349945 -->`
- 【Linux社区】Viro Bollocks：你总是可以把补丁拿给 Linus——即使维护者像 Miss Manners；不能也不应能把垃圾补丁强行塞树（因维护者对你的补丁粗鲁）；0.5KLoC spaghetti+interns 反讽；“终极权力是对补丁说不、没人该有？Are you fucking serious？”+Every Patch is Sacred filk 诗 `<!-- ROW_MINE: ksummit-discuss.messages.349947 -->`
- 【Linux社区】Neil 回 Viro：可以拿给 Linus——“但如果行为不当的是 Linus 呢？这就是为何我认为代码应首先是 Linus 对自己行为的公开声明”；坏补丁该拒、但首个补丁遭恶评后“一次被咬”很难再试；“有多少人知道 petition 权利或用过？也许该写进 CoC” `<!-- ROW_MINE: ksummit-discuss.messages.349949 -->`
- 【Linux社区】Viro 追问：“你提议什么？双头制？真分歧怎么办？Fork？Revert 战？”“CoC 现状已是很糟的主意极易滥用、但你的提议感觉更不连贯” `<!-- ROW_MINE: ksummit-discuss.messages.349950 -->`
- 【Linux社区】Neil 团队维护者制：“我们已有团队维护者安排——顶层照做不难想象”；同结论不同说法——一个“该被脑叶切除”、另一个“我明白你想做什么但方案行不通”；坏日子里人们应有机会找另一位；“知道咆哮对象可以绕过你会促使许多人重新考虑行为（也许我乐观）” `<!-- ROW_MINE: ksummit-discuss.messages.349951 -->`
- 【Linux社区】Viro 二问：“真分歧怎么办——‘交给 Linus 最终决定’在这里显然不管用；他们一致认为补丁无可救药时怎么办？”；BTW 何时有人建议过脑叶切除——NANAE 98 年 SGI sendmail 轶闻注 `<!-- ROW_MINE: ksummit-discuss.messages.349952 -->`
- 【Linux社区】Dan Carpenter 两案自述：曾发 bugfix 被维护者羞辱式拒绝——只因主题不用祈使语气+“NULL dereference”少写 pointer；“十年前有个补丁被拒因为‘F*** you, 女人懂什么编程？’——现在无法想象但当时我也震惊” `<!-- ROW_MINE: ksummit-discuss.messages.349955 -->`**

## 62.5 【Linux社区】GIT PULL、冷却令与 Debian CoC 之议

Bottomley 的 coc-fixes GIT PULL 与 Greg 的 MS 冷却令（文本冻结+假设情境搁置）、Perches 的 Debian CoC 采纳主张与 Dunlap 的“单方面合并”批评、cabal like 之讥——补丁治理的最终路线分歧。

- 【Linux社区】Bottomley [GIT PULL] coc-fixes for 4.19-rc8：**jejb/linux-coc.git**；三补丁合并效果（email 修复+Enforcement 节 CoC 委员会 conduct@kernel.org+except where required by law+Interpretation 链接+删维护者责任段）；“可 rebase 到 Greg 系列不动已收集 tags” `<!-- ROW_MINE: ksummit-discuss.messages.349925 -->`
- 【Linux社区】Greg 冷却令：“让我们让事情冷却、别担心假设性情境——辩论那种事我们能无穷无尽（好技能但不总可迁移）”；CoC 文本与 upstream 一致（除删一段）；真问题出现时再处理、随时可改 `<!-- ROW_MINE: ksummit-discuss.messages.349942 -->`
- 【Linux社区】Perches 回冷却令：“开发模式不同、论据不 compelling”；“如 Bottomley 多次建议、我更愿内核原样采用 Debian CoC 而非这个修改版” `<!-- ROW_MINE: ksummit-discuss.messages.349948 -->`
- 【Linux社区】Dunlap：Debian/Samba URL 都好；“失望的是 James 的补丁在列表被 ack/review 后基本被无视（直到 MS）而其他补丁合入主线 git 树——似乎很单方面” `<!-- ROW_MINE: ksummit-discuss.messages.349953 -->`
- 【Linux社区】Perches：“或许恰当的描述是 cabal like（小集团作派）” `<!-- ROW_MINE: ksummit-discuss.messages.349954 -->`

## 62.6 【Linux社区】程序之辩与 TAB 选举

Bottomley 的程序自省（最后一分钟硬塞 commit 自认）与 Samba 先例（同路径终点是量身定制文档）、Mason 的 TAB 五席改选公告（书面陈述取代演讲）——治理程序的两个现场坐标。

- 【Linux社区】Bottomley：“我们真会搞砸进程——又在最后一分钟硬塞（8e630c31a3df commit）——我反对我们无法遵循公开进程”；但需要文档因为感知问题（对外部多于内部）；Edinburgh 与 Jeremy Allison 谈话：Samba 经历几乎相同（先强推 Contributor Covenant 后私下激辩）、终点 How to do Samba: Nicely——量身定制的价值观声明、最终全员包括最初强推者都同意 `<!-- ROW_MINE: ksummit-discuss.messages.349938 -->`
- 【Linux社区】Mason TAB 选举公告：LF TAB 十人、一人入 LF 董事会；温哥华 KS 11 月 13 日 5:30pm 选五席（2016 席到期）；今年弃演讲改书面陈述 slideshow+公共 google doc；现役名单与届年全列 `<!-- ROW_MINE: ksummit-discuss.messages.349939 -->`

## 62.7 【Linux社区】2014 档案与回归追踪六封

页内夹杂的档案信：Move Fast 的并行度质疑、stable workflow 的 for-stable 拒绝、git metadata 标签实践（Fixes/Link/Coverletter）、Leemhuis 回归追踪暂搁声明、tip-bot 合并通知参照、ARM legacy DT 的 TODO 实务。

- 【Linux社区】NeilBrown 回 Dan Williams Move Fast：质疑“除合格工程时间外还有什么拖慢 Linux 进度”——概念化到发布至少一个发布周期的下限之外、并行度真有上限吗（2014-05-16 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349912 -->`
- 【Linux社区】Greg KH 2014 stable workflow 回 Kosina for-stable 分支提案：“把额外工作压给子系统维护者而非 stable 维护者不可接受”；去年 KS 面谈过、意见未变（2014-05-03 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349923 -->`
- 【Linux社区】Jason Cooper git metadata：自加 Fixes: 12 字符哈希+主题；Link: lkml.kernel.org/r/<Message-Id> 自动生成；设想 Coverletter: 标签供大型系列（2014-05-16 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349924 -->`
- 【Linux社区】Thorsten Leemhuis：回归追踪未死——本职与生活占满、旧法繁琐；11 月有闲、拟推进 Prague KS/MS 讨论的回归追踪题目（2018-10-21，正文夹邮件列表损坏字符） `<!-- ROW_MINE: ksummit-discuss.messages.349930 -->`
- 【Linux社区】Jason Cooper 指引 tip-bot 起点：**git.zytor.com/linux/tip-bot.git** 作合并通知 git hooks 参照（回应 Triplett 自动化工具提案）（2014-05-16 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349935 -->`
- 【Linux社区】Olof ARM legacy board DT：TODO 文件随时可加、elinux wiki 亦可；ixp4xx NSLU2“我父亲还在用”轶事；LinuxCon 难答“这 SoC 安静无补丁但活跃使用”（2014-05-16 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349946 -->`
