# 56 【Linux社区】CoC评审线程与Zinc提案

> 来源：ksummit-discuss p108（50 封全读，2018-09-23/28，夹杂 KS2014 档案信 2014-05-15 与 MOXA 旧硬件证言）。
> 判定：49 CAND / 1 NV（349633 垃圾邮件）。主题分布：coc 34、security 4、KS2014 4、communication 3、hw-deprecation 2、wireguard-zinc 2、spam 1（NV）。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p108（pk 349606-349655）的逐封提取（49 CAND / 1 NV），全 7 块采用**导语＋带锚条目体例**：每块由“## 56.x 【Linux社区】题名”＋导语段＋“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——导语段承担“要点”职能、带锚条目承担“史料”与“史料锚”职能（ROW_MINE 坐标与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 56.1 【Linux社区】Shuah Khan 评审线程：程序性问责与 Debian 中间地带

2018-09-24/27 Shuah Khan 以 TECH-TOPIC 名义开启 CoC 正式评审线程：程序性问责（未经评审即替换获大量签署的 Code of Conflict）、反骚扰政策定性、Debian CoC 中间地带、“Code of Conflict 是否真失败”之问与 Fedora 先例。

- 【Linux社区】Shuah Khan 开启正式评审线程：认同精神但关切维护者新职责（对无控制力个人行为负责）；hurtful 主观、offensive 较清晰；程序性问责——大量开发者签署的 Code of Conflict 被少数人签字替换且未经评审；要求 v2 走流程；“峰会讨论不等于社区批准” `<!-- ROW_MINE: ksummit-discuss.messages.349616 -->`
- 【Linux社区】Morris：“不代表雇主：以上全部同意” `<!-- ROW_MINE: ksummit-discuss.messages.349617 -->`
- 【Linux社区】Linville +1：一些人间接感到被斥责或噤声、情绪真实；他们因受伤退出的可能性不亚于 Linus 式维护者的受害者；“最大化贡献者池须容纳不擅装好的人——给他们参与定规则的话语权” `<!-- ROW_MINE: ksummit-discuss.messages.349618 -->`
- 【Linux社区】Josh Triplett 驳 Linville：“愿意抱怨者与宁愿离开也不善待他人者是两群人、后者极少”；“不能同时容纳要求被善待者与拒绝善待他人者；可容纳嘟囔但照做者” `<!-- ROW_MINE: ksummit-discuss.messages.349620 -->`
- 【Linux社区】Bottomley：新 CoC 不覆盖真正想控的行为——“这不是行为准则、是反骚扰政策”；中间地带设想基于 Debian CoC、缺维护者职责部分恰是该补的；封禁须极克制；“信任 Jon 会为 lwn.net 整理全貌” `<!-- ROW_MINE: ksummit-discuss.messages.349624 -->`
- 【Linux社区】Perches 对 Bottomley 警察化自荐：“Good for you, but 那不是人人都愿做或该做的” `<!-- ROW_MINE: ksummit-discuss.messages.349638 -->`
- 【Linux社区】Jani：“支持变更本身但这也困扰我；Fire-and-forget 不是推广 CoC 的好方式” `<!-- ROW_MINE: ksummit-discuss.messages.349630 -->`
- 【Linux社区】Corbet：“当前 CoC 非刻在石头上——是起点，将如其他代码一样演进；怎么演进——讨论尚未开始” `<!-- ROW_MINE: ksummit-discuss.messages.349631 -->`
- 【Linux社区】Shuah：开线程目的=搞清下一步与社区参与演进计划；“应向全体维护者开放评审而非仅峰会小圈子”（仅代表自己） `<!-- ROW_MINE: ksummit-discuss.messages.349632 -->`
- 【Linux社区】Tim Bird：“Mauro 的 GitHub vs 邮件项目论点到位；email 地址歧义必须解决；峰会与 Plumbers 不代表全部受影响者” `<!-- ROW_MINE: ksummit-discuss.messages.349637 -->`
- 【Linux社区】Jani：“唯一可行是自上而下：维护者以身作则遵循并执行——这或许是 Code of Conflict 虽获大量 ack 仍失败的主因” `<!-- ROW_MINE: ksummit-discuss.messages.349640 -->`
- 【Linux社区】Abbott：Fedora 正修订 CoC——从 contributor covenant 起步+修改；Fedora 也是重邮件工作流——“说明修改可行” `<!-- ROW_MINE: ksummit-discuss.messages.349641 -->`
- 【Linux社区】Jan Kara：“Code of Conflict 真的失败了吗？文件系统领域相当文明、且 CoC 之前也如此” `<!-- ROW_MINE: ksummit-discuss.messages.349642 -->`
- 【Linux社区】Reinecke：“没见过文明大规模崩坏的证据；更该搞清 CoC 到底要解决哪个具体问题” `<!-- ROW_MINE: ksummit-discuss.messages.349643 -->`
- 【Linux社区】Shuah：“Debian CoC 言简意赅、正面措辞——Assume good faith 与 Be open 尤其亮眼；单独邮件列表 CoC 稍加定制即可用” `<!-- ROW_MINE: ksummit-discuss.messages.349648 -->`
- 【Linux社区】Ted：“Fedora 是否有人愿向 TAB 分享私下经验/教训？”（仅代表自己） `<!-- ROW_MINE: ksummit-discuss.messages.349649 -->`
- 【Linux社区】Brown 答“CoC 失败论”：Code of Conflict 之名不传达严肃性；“CoC 的一大目标是向社区外发认真信号——外部人没当回事” `<!-- ROW_MINE: ksummit-discuss.messages.349650 -->`
- 【Linux社区】Tim Bird：“用标准 CoC 作底本有价值；听 Greg KH 说人们误读 Code of Conflict 为鼓励冲突” `<!-- ROW_MINE: ksummit-discuss.messages.349651 -->`
- 【Linux社区】Abbott：“去联系 Fedora 参与者；pagure 公共 tracker+issue 105 总结” `<!-- ROW_MINE: ksummit-discuss.messages.349653 -->`
- 【Linux社区】Gorman：“不只是 email 地址——补丁与 SOB 一般要求真名而非假名” `<!-- ROW_MINE: ksummit-discuss.messages.349615 -->`
- 【Linux社区】Leon 答 Gorman：真名要求已由 DCO (d) 覆盖（附链接） `<!-- ROW_MINE: ksummit-discuss.messages.349626 -->`

## 56.2 【Linux社区】行为哲学之辩：tglx 私下关怀 vs codify 强制

2018-09-24/25 CoC 战线最深的哲学层：tglx 的失态者自白与 John Stultz 关怀案例、Olof 的 Popper 悖论与“朋友之事非社区义务”边界、Vetter 的“codify 反对”与零余量平衡论、Dan Williams 的双向共情。

- 【Linux社区】Olof：Popper 悖论——对不宽容者的宽容非无限；CoC 是“从今往后”既往不咎；最坏情形恐惧无根据、不降质量门槛；“旧 Code of Conflict 说 be excellent 但人们没做到” `<!-- ROW_MINE: ksummit-discuss.messages.349621 -->`
- 【Linux社区】tglx：“我们都是人——包括偶尔失态者（终身与脾气搏斗）”；把人摁回原位绝对正确且必要、多数人立即道歉；但更进一步私下问一句“怎么了”——真正关心失败者——比把 CoC 当单刃剑更深的改变 `<!-- ROW_MINE: ksummit-discuss.messages.349622 -->`
- 【Linux社区】Vetter 回 tglx：“CoC 要求的只是别把自己放第一位、考虑他人；而非发泄后还要收件人处理后果”；tglx 设想“单向而非相互” `<!-- ROW_MINE: ksummit-discuss.messages.349625 -->`
- 【Linux社区】Olof 细注：“put in place”可解为对已激动者更大声吼——不应如此；向失态者伸手是朋友之事而非社区义务——“须先关照受端” `<!-- ROW_MINE: ksummit-discuss.messages.349627 -->`
- 【Linux社区】Dan Williams（仅代表自己）：“共情是双向车道，须有问责与宽恕的空间，否则对话无法前进” `<!-- ROW_MINE: ksummit-discuss.messages.349628 -->`
- 【Linux社区】tglx 澄清：失态者须伸手；“John Stultz 曾对我如此、影响巨大、助我看见自己防线的裂缝”；“东欧或压制性国家长大者对思想警察极敏感——压制不会让人性之失消失” `<!-- ROW_MINE: ksummit-discuss.messages.349629 -->`
- 【Linux社区】Vetter：同意私下关怀但“codify 进 CoC 不是好主意——爆炸后清理已是巨量工作；精心措辞回复是零余量平衡”；“crack down 过头；共情有底线” `<!-- ROW_MINE: ksummit-discuss.messages.349636 -->`
- 【Linux社区】Shuah：“受端者以中性语气回应很难但我做过几次”；“担心受端者退场停更”；“小心不过度反应于被感知的冒犯——一个人的玩笑是另一个人的侮辱” `<!-- ROW_MINE: ksummit-discuss.messages.349639 -->`

## 56.3 【Linux社区】单一 CoC vs 子系统 A/B 与既有文档冲突

2018-09-26 治理结构层之争：Jason Cooper 的子系统自选 CoC+默认回退 A/B 提案、Mauro 的 Debian 邮件列表 CoC 移植与 VGER 过滤设想、全局 CoC 与既有隐私政策/子文档的冲突面。

- 【Linux社区】Jason Cooper：内核历史多点多法可验证“说了就赖不掉”、CoC 不会实质改变行为只会赶走稀缺人才；全社区单一 CoC 徒劳（drm 已有自己的）；A/B 测试：子系统可选自己的 CoC（MAINTAINERS/列表脚注）、默认 Code of Conflict `<!-- ROW_MINE: ksummit-discuss.messages.349619 -->`
- 【Linux社区】Mauro：Debian 有单独邮件列表 CoC+葡语翻译——“欢迎非英语者的好方式”；“坏行为处置因子系统而异；media ML 经验：静默无视比回复有效——人们要的只是关注”；VGER CoC-aware 反垃圾启发式过滤设想；“troll 会换号复活” `<!-- ROW_MINE: ksummit-discuss.messages.349644 -->`
- 【Linux社区】Mauro 答 Reinecke +1：“media ML 近来无大患、感觉在改善；LKML 是另一头野兽——但如今谁真的读全部消息” `<!-- ROW_MINE: ksummit-discuss.messages.349646 -->`
- 【Linux社区】Geert 调侃 Mauro 过滤设想：“至少维护者不必再手动处理请从源码注释中移除冒犯性词语的补丁了” `<!-- ROW_MINE: ksummit-discuss.messages.349647 -->`
- 【Linux社区】Mauro 答 Cooper A/B 提议：media 隐私政策（EU 驱动）确有交集——“发布到 wiki 或列表的信息就是公开的”；“可能与既有 CoC 类文档冲突” `<!-- ROW_MINE: ksummit-discuss.messages.349652 -->`

## 56.4 【Linux社区】安全公开列表之辩：CRD 与 security@ 定位

Carpenter 公开安全列表倡议的续辩：Kosina 引入 CRD（协调发布日期）概念与 security@ 的双重定位澄清（联络点 vs 全局严重 bug 处理）。

- 【Linux社区】Kosina 补第 3 缺点：内核需要 CRD（协调发布日期）流程、security@ 正承担此职——公开化须另立 CRD 流程 `<!-- ROW_MINE: ksummit-discuss.messages.349606 -->`
- 【Linux社区】Ted 问 CRD 为何缩写 `<!-- ROW_MINE: ksummit-discuss.messages.349607 -->`
- 【Linux社区】Kosina：CRD=“Coordinated release date across the various affected vendors” `<!-- ROW_MINE: ksummit-discuss.messages.349608 -->`
- 【Linux社区】Carpenter 答：非消灭 security@（也不替其答每个 suspicious code）；协调响应用 linux-distros、security@ 不做；security@ 两大职能——报告联络点（半数直转维护者）+核心开发者处理 ptrace 类全局严重 bug `<!-- ROW_MINE: ksummit-discuss.messages.349614 -->`

## 56.5 【Linux社区】WireGuard/Zinc 提案与邮件丢失插曲与补丁 bot 续

Zinc 密码 API 议题立项（提案全文入档）与 LF 邮件服务器静默丢信实录（250 queued 三次仍未见档）；附件补丁 bot 的 MIME/重复解析缺陷补论。

- 【Linux社区】Donenfeld：WireGuard talk 已被 Plumbers 主评审轨道接收、撤回 ksummit 提交；请关注 Zinc `<!-- ROW_MINE: ksummit-discuss.messages.349609 -->`
- 【Linux社区】Bottomley 告知 Jason：列表与档案只见其一封——“出站服务器可能有问题” `<!-- ROW_MINE: ksummit-discuss.messages.349610 -->`
- 【Linux社区】Donenfeld：非出站问题——日志显示 lists.linuxfoundation.org 三次返回 250 queued；拉 Konstantin 查 `<!-- ROW_MINE: ksummit-discuss.messages.349611 -->`
- 【Linux社区】Donenfeld 重发 Zinc 提案全文（原信被静默拒收）：极简内核密码 API——非抽象框架而是简单函数；实现选择与 fuzzing、形式化验证实现、SIMD from kernel space 成本 `<!-- ROW_MINE: ksummit-discuss.messages.349613 -->`
- 【Linux社区】Mauro 答 Olof bot：可行但有坑——MIME 误标/服务器判 evil 拒收/企业只许 webmail；bot 收两遍会引多机器人重复回复——“加 meta-tags 防其他机器人重复解析” `<!-- ROW_MINE: ksummit-discuss.messages.349635 -->`

## 56.6 【Linux社区】MOXA 旧硬件证言与 CIP 僵尸论

硬件弃用之辩的厂商第一手证言与最强反驳同页：Moxa 的 CIP 加入理由 vs tglx 的“僵尸内核”论与“最新内核+厂商负责”主张。

- 【Linux社区】SZ Lin（Moxa，个人观点）：ART SoC 由 Faraday 顾问团供 IP；EM-1240（ARMv4）与 EP93xx（ARMv4T）仍活跃部署甚至推荐新项目；Moxart 加了工业专用 IP；“长期维护内核对工业应用极重要——Moxa 因此加入 CIP” `<!-- ROW_MINE: ksummit-discuss.messages.349654 -->`
- 【Linux社区】tglx 驳：问题不在保活旧内核而在“如何在最新内核中保住旧硬件支持、谁负责”；“CIP 是把死内核维持僵尸状态——speculation mess 证明回移侵入式安全修复危险”；“Meltdown/Spectre/L1TF 正解是在旧硬件上换新内核；bitrotting 不如移除；要保住就得厂商站出来” `<!-- ROW_MINE: ksummit-discuss.messages.349655 -->`

## 56.7 【Linux社区】KS2014 档案四封

页内夹杂的 KS2014 档案信（2014-05-15）：per topic people 提名名录的增补与勘误。

- 【Linux社区】Bueso 自提名：stable issues, application performance（2014-05-15 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349612 -->`
- 【Linux社区】Ted 问 Kosina：Joey 还是 Chun-Yi？（2014-05-15 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349623 -->`
- 【Linux社区】Boyer 道歉忘附邮箱+补充更正多个邮箱（2014-05-15 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349634 -->`
- 【Linux社区】Kosina：Joey/Chun-Yi 两种都用、不知偏好（2014-05-15 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349645 -->`
