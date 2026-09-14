# 63 【Linux社区】CoC收尾大辩论与撤销许可论战

> 来源：ksummit-discuss p115（50 封全读，2018-10-23/11-03 主线 CoC 大辩论收束+多时间域议题，夹杂 2014-05 档案信）
> 判定：47 CAND / 3 NV。主题分布：女程序员案追问 2、2014档案与回归追踪 5、DebianCoC之辩 3、code大于people之辩 15、Fiebig自拟CoC 6、撤销许可论战 8、Viro匿名巨魔风波 5、多时间域议题 3。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p115（pk 349956-350005）的逐封提取（47 CAND / 3 NV），全 8 块采用**单行摘要体例**（丙型）：每块由“## 63.x 【Linux社区】题名”与若干“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 63.1 【Linux社区】女程序员案追问

- 【Linux社区】Viro 追问 Carpenter“F*** you 女人懂什么编程”案 URL：“我真心想知道是谁、在哪说的——十年前若在公开内核列表早该引发大规模且完全应得的风暴” `<!-- ROW_MINE: ksummit-discuss.messages.349956 -->`
- 【Linux社区】Carpenter：那是私人邮件、不知维护者是谁；从当事女性在 Linux 会议听说——她是称职程序员、bug 当时仍在 `<!-- ROW_MINE: ksummit-discuss.messages.349958 -->`

## 63.2 【Linux社区】2014档案与回归追踪

- 【Linux社区】Olof 回 Grant Likely ARM minisprint：疑实操性——legacy 平台需随机硬件测试、拖去芝加哥别扭；需 todo 清单+在场人名单；建议与秋季 Linaro Connect California 同址（2014-05-16 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349957 -->`
- 【Linux社区】Jason Cooper 回 Greg KH：kernel-history 统计公开于 github.com/gregkh/kernel-history 含生成脚本（合并补丁口径、连续 8 年上升）；初次发帖者应答率量化计划：主列表首帖过滤+数据决定调整（2014-05-16 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349968 -->`
- 【Linux社区】Jason Cooper ARM DT 收尾：mvebu 最后两个 legacy 平台（dove/mv78xx0）下周期或并入 mach-mvebu、之后可问 Debian/OpenWRT 哪些 legacy 平台在用或腐烂（2014-05-16 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349979 -->`
- 【Linux社区】Christian Couder git metadata：git interpret-trailers 新命令（帮助加 trailer 行）；git replace+fixed up branches 用于含不可测提交的 bisect（LinuxTag Berlin 演讲、LKMS 2013 决议源头）（2014-05-16 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349990 -->`
- 【Linux社区】Linus Walleij 提名：Catalin Marinas/Will Deacon（唯一既部署 ACPI 又部署 DT 的架构维护者）+Rafael J. Wysocki（“ACPI 混沌领航员”）——driver model/ACPI-DT 组（2014-05-16 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.350001 -->`

## 63.3 【Linux社区】DebianCoC之辩

- 【Linux社区】Triplett 反驳 Perches：Debian CoC 处理问题远不完善（采纳时此类文件还不成熟）；Debian 内部许多人（含支持者）有意改进或换更成熟的 `<!-- ROW_MINE: ksummit-discuss.messages.349959 -->`
- 【Linux社区】Brown：Debian CoC 不算旧、当时批评已存在、差异多是深思熟虑——针对 Debian 社区的 rules lawyering 倾向（有人试图钻空子非理论担忧） `<!-- ROW_MINE: ksummit-discuss.messages.349961 -->`
- 【Linux社区】Bottomley 接受现状：“拒绝我的 pull 改用你的补丁是程序错误；但多数人能接受现状、我不再反对（感谢 MS 承诺下次更透明真正遵循流程）”；“加 interpretation 段是最重大变化之一——圈住未稀释 CC 的潜在效应”；“推向 upstream 是红鲱鱼：无承诺跟进后续版本+两文档交互是冲突源；也是社会性错误——想让社区拥有 CoC 就不能总说它是别人的文档” `<!-- ROW_MINE: ksummit-discuss.messages.349962 -->`

## 63.4 【Linux社区】code大于people之辩

- 【Linux社区】Ted 回 Neil：“问题从来不是 Linus 如何对待核心维护者以外的人——MS 会上无人抱怨 Linus 近期行为、普遍认同其行为近年一直变好”；新人的“已注意到差别”多因 CoC 缓解恐惧而非四周内真变化；“CoC 将更像社区规范的承诺”；Samba/GNU Kind 换名现象——CoC 一词对某些人是触发语 `<!-- ROW_MINE: ksummit-discuss.messages.349960 -->`
- 【Linux社区】Neil 声誉论：“当然关乎‘如何’——一种拒绝给你前路、另一种让你受伤离开”；“Linus 行为改善只是故事一半——声誉比行为更糟（他直到最近都没纠正声誉）”；引非公开列表：“未解决的 bug 是 Linus 的行为、更糟的是那些不那么巧妙模仿他爆发的人离 Linus 自己声明的待人理想越来越远——榜样正被复制、明确的反例很重要”；“我们的 code 加两倍半长的 interpretation，与 Samba/GNU Kind 并排看不笨拙吗？” `<!-- ROW_MINE: ksummit-discuss.messages.349967 -->`
- 【Linux社区】Laura Abbott 自白（较新加入者）：“刚入门时可能不想要 CoC——年轻时说过后悔的话；年轻的我也忍受了今天不能忍的行为；firm feedback 帮我留下”；“今天认为 CoC 是重要补充：更强宣示社区致力于抬高行为标准；多数议题私信一句‘你或许该重新考虑措辞’即可解决；CoC 提供对 patch review 之外骚扰议题能被处理的信心——社区靠信任运作；希望永远不必报告骚扰但庆幸有程序在” `<!-- ROW_MINE: ksummit-discuss.messages.349969 -->`
- 【Linux社区】Triplett 回 Neil 读 CoC 会获得什么：“少一些‘一个错就被当典型喂进别人语录集’的弥漫感”；引 HBR 心理安全研究文章 `<!-- ROW_MINE: ksummit-discuss.messages.349970 -->`
- 【Linux社区】Neil 引旧 code of conflict：“任何人对该流程感到被虐待/威胁/不适都是不可接受的——这难道不足以驱散弥漫感？”（code>people 之争的引信） `<!-- ROW_MINE: ksummit-discuss.messages.349974 -->`
- 【Linux社区】Neil 反馈机制提案：Linus 请大家盯着他邮件在接近边缘时提醒（LWN 769117）“意义在告诉更广社区：关于行为的反馈明确受欢迎”；反对私信解决（不让社区知道已解决、不树立范例）；“该给弱者权力而非限制强者”；草拟反馈引导文档（“我觉得有帮助”/“这让我受伤”标准句式+不润色不解释+一人一票） `<!-- ROW_MINE: ksummit-discuss.messages.349975 -->`
- 【Linux社区】Triplett：“旧 code of conflict 那句不足——那文档开头就在精致地说 code>people（且更重要的是社区实际行为是否一致）”；“Our Standards 与 Enforcement 节同样重要——更关键是实际执行的例子而非空话” `<!-- ROW_MINE: ksummit-discuss.messages.349983 -->`
- 【Linux社区】Neil 调和经验迁移：“你特别看重 Enforcement 节、我恰好最厌恶——好斗而非调和、第一步就是标记报告”；技术分歧经验迁移：标准（no regressions/maintainable）+code talks（写码者决策、出力者多被听见）——翻译到社会面：有标准（Be helpful. Don't be harmful）+见认同就发声+确保做过有价值工作的人有被听见的去处；“伤害人的人自己受伤——回击只会加深、不如侧身避开” `<!-- ROW_MINE: ksummit-discuss.messages.349989 -->`
- 【Linux社区】Paul McKenney 首度加入：“好奇 code>people 从何而来”；“内核用户（直接间接）也重要——‘有史以来最健壮内核’正是服务他们；因此我必须拒绝任何导致 RCU grace period 过短的补丁——提交者的需求被众多用户压倒；技术要求其实是用户需要的代理”；代码风格约束服务读码人、可维护性服务未来用户 `<!-- ROW_MINE: ksummit-discuss.messages.349993 -->`
- 【Linux社区】Triplett 澄清：“没人建议改变代码接受标准——拒你该拒的、收你该收的；这一切只影响 communication” `<!-- ROW_MINE: ksummit-discuss.messages.349996 -->`
- 【Linux社区】Neil 回 Paul：“你对情感观察作分析回应、分析虽对但无关——这不关乎人们怎么感觉”；“code of conflict 并没消失——大部分保存在 interpretation；第二段价值 squarely 在 code、人只在被批评的语境出现——价值体系就是 code>people”；“Linus 现在确认每个 pull request 是 brilliant——不帮流程不帮代码但告诉人们 Linus 看得见他们；code-of-conflict 只在你被虐待时才承认你重要” `<!-- ROW_MINE: ksummit-discuss.messages.349997 -->`
- 【Linux社区】Paul 坚持：“强烈建议坚持代码接受标准不降低的立场”；“Communication is inherently difficult——就像我们俩刚才演示的 ;-)” `<!-- ROW_MINE: ksummit-discuss.messages.349998 -->`
- 【Linux社区】Paul users need us：“同意 Linus 确认 pull request 是好事——激励人是被低估的艺术…但我仍没在 interpretation 里看到 code>people——对我全关乎人；70 年代我的软件只有两个用户我常与他们聊——Linux 不可能；我以需求形式抽象用户需要——需求是用户需要的代理；总之不是 code>people 而是 our users need us” `<!-- ROW_MINE: ksummit-discuss.messages.349999 -->`
- 【Linux社区】Bottomley 稻草人论：“整个 code vs people 之辩是稻草人且本质不利于讨论——新旧两套都没有允许对人相对代码作价值判断的陈述；技术质量 paramount 与尊重他人是两条并行的陈述——可以聚焦质量做纯技术评审同时尊重对方” `<!-- ROW_MINE: ksummit-discuss.messages.350000 -->`
- 【Linux社区】Neil users>developers 精修：“用户受产品影响、开发者受流程影响；那段谈满足用户几乎不谈开发者——或许不等式是 users>developers；社区其实珍视开发者但行文不 welcome；这凸显沟通之难——为何建议干脆不要 CoC：写什么人们都会理解不同；我们只需 good conduct 并在看到时鼓励——conduct 从成员 conduct 有机涌现如同 Linux 从开发者工作涌现” `<!-- ROW_MINE: ksummit-discuss.messages.350004 -->`

## 63.5 【Linux社区】Fiebig自拟CoC

- 【Linux社区】Rainer Fiebig（rc 内核用户+少量贡献）+1 支持 Neil 并发布自拟完整 CoC：No bias（歧视与偏袒皆禁、唯一标准=贡献与目标一致）/黄金法则+“有时你可能是错的”；不可接受行为含 Promoting political agendas、断章取义构陷；维护者有权暂时或永久 ban；TAB 仲裁节 `<!-- ROW_MINE: ksummit-discuss.messages.349963 -->`
- 【Linux社区】Fiebig 回 Ted：“为解决‘如何拒绝’引入极富争议的 CoC 已开始分裂社区——小题大做”；“感知即现实——Linux 被感知为支持随附议程；疏远了多数忠诚用户——坏选择坏时机（桌面正要起飞）”；“不是 CoC 一词而是具体选择与措辞引发反感、替代方案都被无视”；“这就是极端政治正确——Tim Hunt 五例链接；女巫审判回来了——伽利略至少可选忏悔或火刑柱，今天忏悔了照样公开烧死” `<!-- ROW_MINE: ksummit-discuss.messages.349964 -->`
- 【Linux社区】Ted 驳 Fiebig：“Citation Needed——多数用户被疏远的证据何在”；感知双向：“删三行 Josh 不满、保留 CC 你觉得袋鼠法庭——你俩方向相反都不满，提示我们大体做对了”；0day bot 欢迎语被德国与会者解读为更不欢迎（欧洲文化过度礼貌=视你为蠢）——文化差异不可预测；“女巫审判论正是 FUD——Go 同用 CC 你见过女巫审判吗？一年内无维护者被弹劾你愿改观点吗？” `<!-- ROW_MINE: ksummit-discuss.messages.349965 -->`
- 【Linux社区】Neil 两原则回 Viro：“真实分歧的处理不是我（非团队成员）的问题——维护者团队运转正常即存在证明；团队内部协议基于：成员称职不轻率提交争议（选择信任）+我们常提交坏补丁发现就修（devfs/cgroups 大错世界也没完）——接受不完美是 Linus 实用主义关键；一致认为无可救药就礼貌说明理由——right-of-review 不是 right-of-success”；承认脑叶切除系虚构例子 `<!-- ROW_MINE: ksummit-discuss.messages.349966 -->`
- 【Linux社区】Fiebig 提“人人有被冒犯的权利”（引 John Cleese）入 Our Pledge；Neil：“给社区某些权利是好的：告诉任何人其言语伤人+第三方补丁评审权；被冒犯权不必给——我自己放弃被冒犯权、不值得费劲” `<!-- ROW_MINE: ksummit-discuss.messages.349977 -->`
- 【Linux社区】Fiebig 收尾长怨：“constructive criticism 也不 helpful——唯一给出完整替代方案的人被无视；这更像长城或朝鲜而非开源项目；用 Monty Python 反咬批评是 People's Front 之耻”；Neil：“Engage in discussion、让我想读你的文档；感谢参与” `<!-- ROW_MINE: ksummit-discuss.messages.349982 -->`

## 63.6 【Linux社区】撤销许可论战

- 【Linux社区】Pavel：同意 Neil 全部（拒绝 CoC+revert）；“希望更多人 gpg-sign 邮件——我曾以为 Linus 的 rc4 公告是伪造的” `<!-- ROW_MINE: ksummit-discuss.messages.349971 -->`
- 【Linux社区】匿名 visionsofalice@redchan.it（8chan）：“linux devs 可撤销许可授予”；Greg 斥：“不、他们不能，请别再传播虚假信息”（CC rms/moglen/Perens/Kuhn/LWN 编辑——法律权威圈全部入席） `<!-- ROW_MINE: ksummit-discuss.messages.349972 -->`
- 【Linux社区】Ted 驳 ESR：ESR 引 Jacobsen v. Katzer（535 F.3d 1373 Fed. Cir. 2008）称 GPL 作者有救济权含禁令救济、声誉损害明确可诉；Ted：“我读过法律简报、它们说的和你主张的不符——我不是律师但你也不是”；“绝大多数推进此论的异见者在内核几乎没有版权——是社区外巨魔、带自己的议程”；建议“回应前先 git log 看是否真贡献过” `<!-- ROW_MINE: ksummit-discuss.messages.349973 -->`
- 【Linux社区】Neil 区分两类人：“推进撤销许可论的比不喜欢 CoC 的 camp 小得多、限缩到实际版权持有人更小；我反 CoC 但撤销许可这种过度反应可笑” `<!-- ROW_MINE: ksummit-discuss.messages.349976 -->`
- 【Linux社区】Neil fork 论回 ESR：“若真有事威胁我的投资价值、会有很多人同样认为——我们可以 fork 社区”；“程序失败我同意——立即强加没必要且有害” `<!-- ROW_MINE: ksummit-discuss.messages.349978 -->`
- 【Linux社区】Viro 立场声明：“CoC 与社区结构极不匹配；Linus 休假前往茅厕扔了颗手雷、后果完全可预测——各路屎食动物闻风而来包括 NANAE 时代的卡通式人物”；“‘撤销我的贡献许可逼他们撤销 CoC’这种狡猾计划我任何语言都写不出连贯描述”；“我不玩这种把戏——我彻底鄙视 RMS 一伙在 GPLv3 玩的杠杆游戏，绝不自降到他们水平” `<!-- ROW_MINE: ksummit-discuss.messages.349980 -->`
- 【Linux社区】Viro 回 ESR“连 Al Viro 都认为你们搞砸了流程就别把反对者当巨魔”：“请停止把对 CoC 的反对与那种愚蠢混为一谈” `<!-- ROW_MINE: ksummit-discuss.messages.349981 -->`
- 【Linux社区】Bradley Kuhn（SFC）：同意 Greg“不能撤销”+补链接 sfconservancy.org GPLv2-irrevocability——SFC 律师为 Copyleft Guide 新写的 GPLv2 不可撤销性章节 `<!-- ROW_MINE: ksummit-discuss.messages.349991 -->`

## 63.7 【Linux社区】Viro匿名巨魔风波

- 【Linux社区】匿名者再谈 GPL v3 论；Viro：“Anonymous wankstain: 滚回去学会正确地巨魔——那是门艺术你不配；D- for effort……*plonk*” `<!-- ROW_MINE: ksummit-discuss.messages.349984 -->`
- 【Linux社区】Tim Bird 劝 civility：“请保持文明——称人 wankstain 不专业、我们在努力抬高话语水平；plonk 部分足够传达不认真对待——对坏 faith 者去升级比接战好” `<!-- ROW_MINE: ksummit-discuss.messages.349985 -->`
- 【Linux社区】Kosina：“匿名通信也不符合我的‘高度专业’标准；CoC 要求对线另一端的人 reasonably nice 是高尚目标——但你至少得知道另一端是谁否则沟通失败难免” `<!-- ROW_MINE: ksummit-discuss.messages.349986 -->`
- 【Linux社区】Viro 回 Perens（匿名者一般认为是 MikeeUSA、有记录在案的厌女史）：“你误读了——那成员的行为完全由其被注意的绝望需要控制；可悲但这就是社交媒体世代” `<!-- ROW_MINE: ksummit-discuss.messages.349987 -->`
- 【Linux社区】Neil 反用 CoC：“我同意 Tim：无论对方是谁、重要的是语境；提升标准意味着所有通信”；“既然你玩这游戏：1/**code-of-conduct.rst** 里根本没有 human 一词 2/interpretation 明说 We know everyone is human——可解读为即使对方不表现得像人也须当人对待；你真想用 CoC 支持你的立场吗？” `<!-- ROW_MINE: ksummit-discuss.messages.349988 -->`

## 63.8 【Linux社区】多时间域议题

- 【Linux社区】tglx [TECH-TOPIC] Multiple time domains：时间命名空间讨论引出的问题+TSN 汽车/自动化 grand clock master 需求；LPC 期间技术专场提案（CC 时间/容器/CRIU 众人） `<!-- ROW_MINE: ksummit-discuss.messages.349992 -->`
- 【Linux社区】Biederman：“我肯定到；请排在与 LPC 重叠的日子——让所有 CRIU 与容器的人有机会到场；理想是不与 CRIU/Container minisummit 撞期” `<!-- ROW_MINE: ksummit-discuss.messages.349995 -->`
- 【Linux社区】Brauner：“能到场同意 Eric：LPC 重叠但不撞 containers/CRIU 微峰会；约束：14 日 2:30pm 有 15 分钟演讲” `<!-- ROW_MINE: ksummit-discuss.messages.350003 -->`
