# 58 【Linux社区】CoC补丁决胜局Acked-by潮

> 来源：ksummit-discuss p110（50 封全读，2018-10-04/08，夹杂 KS2014 档案信 2014-05-15）。
> 判定：50 CAND / 0 NV。主题分布：coc 46、KS2014 4。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p110（pk 349706-349755）的逐封提取（50 CAND / 0 NV），全 6 块采用**导语＋带锚条目体例**：每块由“## 58.x 【Linux社区】题名”＋导语段＋“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——导语段承担“要点”职能、带锚条目承担“史料”与“史料锚”职能（ROW_MINE 坐标与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 58.1 【Linux社区】Bottomley [PATCH 0/2] 实发与 Acked-by 潮：CoC 修订进入补丁流程

2018-10-06/07 CoC 论战从口水转向补丁：Bottomley 双补丁实发（email 豁免+剥 enforcement）、Fixes: 8a104f8b5867 引用规范、Shuah/Geert/Roeck 的 Acked-by 潮与 Roeck“未被咨询”宣言。

- 【Linux社区】Bottomley [PATCH 0/2] 正式发布：“Mauro 是唯一真提补丁的人；为推进辩论我出两补丁——修 email 歧义+按 Shuah 建议剥 enforcement 节；我负责收集 tag 并在 4.19 final 前以签名 PR 提交” `<!-- ROW_MINE: ksummit-discuss.messages.349730 -->`
- 【Linux社区】[PATCH 1/2] 全文：email 歧义修复——“address not ordinarily collected by the project, without explicit permission” `<!-- ROW_MINE: ksummit-discuss.messages.349731 -->`
- 【Linux社区】[PATCH 2/2] 全文：剥 Enforcement 节 15 行（含 TAB 报告渠道+good faith 罚则） `<!-- ROW_MINE: ksummit-discuss.messages.349732 -->`
- 【Linux社区】Geert 校对 patch 1/2 + Fixes: 8a104f8b5867c682 + Acked-by `<!-- ROW_MINE: ksummit-discuss.messages.349737 -->`
- 【Linux社区】Shuah Acked-by patch 1/2 `<!-- ROW_MINE: ksummit-discuss.messages.349742 -->`
- 【Linux社区】Shuah 谢 Bottomley 发补丁 `<!-- ROW_MINE: ksummit-discuss.messages.349743 -->`
- 【Linux社区】Shuah Acked-by patch 2/2（假设 enforcement 细节后续版本社区讨论后补） `<!-- ROW_MINE: ksummit-discuss.messages.349746 -->`
- 【Linux社区】Roeck Acked-by patch 1/2 `<!-- ROW_MINE: ksummit-discuss.messages.349752 -->`
- 【Linux社区】Roeck Acked-by patch 2/2 + 理由：“TAB 未被选为执行机构；我作为维护者在我被决定负有执行 CoC 责任时未被咨询” `<!-- ROW_MINE: ksummit-discuss.messages.349753 -->`
- 【Linux社区】Geert patch 2/2：“Fixes: 8a104f8b5867c682 + Acked-by” `<!-- ROW_MINE: ksummit-discuss.messages.349754 -->`
- 【Linux社区】Bottomley：“我采纳你的建议发成具体补丁集看反响” `<!-- ROW_MINE: ksummit-discuss.messages.349733 -->`
- 【Linux社区】Shuah 先行建议：“Zephyr 版与 4.19-rc4 的 CoC 几乎全同只差 enforcement 节；我偏好 4.19 修订掉 enforcement 而非带着 v1 现文发布” `<!-- ROW_MINE: ksummit-discuss.messages.349727 -->`

## 58.2 【Linux社区】免责声明 vs revert：4.19 发布前的路线之争

4.19 final 倒计时的路线分歧：Vetter 的免责声明中间路线与“等 Linus 澄清”的克制立场、Bottomley 的“免责声明=什么都没有不如 revert”、hch 的“绝非假想”与 Geert 的寒蝉效应警告。

- 【Linux社区】Vetter 答 [PATCH 0/2]：“对仓促引入完全不高兴（至今不明白为何）；不该在 4.19 前几天仓促改；盼峰会讨论后更清晰；但也理解不想带中间态发版——建议顶部加免责声明——无争议到足以集齐广泛支持；愿 ack” `<!-- ROW_MINE: ksummit-discuss.messages.349747 -->`
- 【Linux社区】Tim Bird 答 patch 2/2：“报告渠道节（TAB 邮箱+保密）不是 enforcement、只是报告指引——建议不删；若删下段则该节或须改名” `<!-- ROW_MINE: ksummit-discuss.messages.349735 -->`
- 【Linux社区】Bottomley：“两段都删后现状≈status quo：各子系统自理+Our Responsibilities 形式化；中央报告/执行渠道是否要、是什么也应入辩；TAB 是为向 LF 输送技术意见而设——要做对就该辩论其职责与权力扩张；TAB 无法强迫只能说服是体系的巨大优点——没有可被颠覆的权力结构（我写了 TAB 章故有偏见）” `<!-- ROW_MINE: ksummit-discuss.messages.349736 -->`
- 【Linux社区】Bottomley 答：“废旧 CoC 换一个自加免责声明怀疑的新 CoC=什么都没有——更糟；那种情况下 revert 8a104f8b5867 重启替代流程更好；我偏好修现有的但意愿不强” `<!-- ROW_MINE: ksummit-discuss.messages.349749 -->`
- 【Linux社区】Vetter：“加旧 Code of Conflict 暂行有效已有社论之嫌、可能阻碍 ack 山；本人不愿 ack/nack 任何具体变更——只要 Linus 还没澄清为何仓促、为何觉得必要；搞清什么是对需要更长时间（即便延一周，见 -rc7 公告）” `<!-- ROW_MINE: ksummit-discuss.messages.349751 -->`
- 【Linux社区】jonsmirl：“据我所知没有一个开源友好律师评审过；怀疑这文档法律地位不稳；CoC 到底是指导还是法律合同？” `<!-- ROW_MINE: ksummit-discuss.messages.349750 -->`
- 【Linux社区】Geert：“享受不可 rebase git 的 append-only 本性吧 ;)；提议发补丁修 CoC——寒蝉效应恐怕已在发生” `<!-- ROW_MINE: ksummit-discuss.messages.349707 -->`
- 【Linux社区】hch 驳“假想情形论”：“鉴于安全社区里某些非常聪明但 abusive 的人，这绝非假想” `<!-- ROW_MINE: ksummit-discuss.messages.349706 -->`

## 58.3 【Linux社区】封禁 Alice 续辩：剥名版权论与 netfilter 先例

“封禁 Alice”思想实验的深化：Geert 的剥名=版权违反新论、Ted 的 netfilter 集体拒收先例（25 年一遇、无诉无祸）与 Bottomley 的房产记录类比。

- 【Linux社区】Geert 答 Triplett 失效邮箱类比：“地址失效时可自己修+加 Reported-by 而不违规则” `<!-- ROW_MINE: ksummit-discuss.messages.349708 -->`
- 【Linux社区】Geert 追问：“关键修复补丁不合标准+提交者跑路——你怎么办？被禁者的名字不能发布？剥名是故意的版权违反”；“封禁人 contributing 打开新的一罐虫” `<!-- ROW_MINE: ksummit-discuss.messages.349713 -->`
- 【Linux社区】Triplett：“取决于你是否愿意自己修——可 rework+based on a patch from；没理由因不受欢迎就剥名——只是别 CC 他” `<!-- ROW_MINE: ksummit-discuss.messages.349714 -->`
- 【Linux社区】Ted 揭 netfilter 先例：核心团队集体决定不接受版权恶棍补丁——Linus/TAB/LF 均未参与；“天没塌、没人被诉百万；25 年只发生一次、在重大伤害后、非随意为之”；若其提交安全补丁“建议 clean room 换方式重写” `<!-- ROW_MINE: ksummit-discuss.messages.349726 -->`
- 【Linux社区】Geert 答 Vivi：“你这么表述就容易回答了；可惜现实并非如此黑白分明” `<!-- ROW_MINE: ksummit-discuss.messages.349709 -->`
- 【Linux社区】Bottomley：“讨论过但未达共识——问题在把 email address 明文列为 private information；房产记录类比：physical address 对自有房者也是公共记录——措辞没覆盖日常流程用的东西” `<!-- ROW_MINE: ksummit-discuss.messages.349725 -->`

## 58.4 【Linux社区】CoC fork 之辩与公司实体适用性

CoC 治理结构层之争：fork 权与“标签效应”的镜像论证（Pinchart vs Jani）、公司实体适用性新问（Google 中国假设案）与 Zephyr PR 采信纠错。

- 【Linux社区】Pinchart：“先评估是否选对上游、上游目标是否与你相同；软件有正当 fork 理由、CoC 为何不能有；措辞层与本质层关切分开处理后才决定 fork 或上游；民主胜于独裁，CoC 亦然” `<!-- ROW_MINE: ksummit-discuss.messages.349716 -->`
- 【Linux社区】Jani：“不 fork 的理由同不自制许可证：读熟悉的标签就知道盒子里是什么；同文本共享经验与最佳实践；选一个经过考验的并坚持” `<!-- ROW_MINE: ksummit-discuss.messages.349719 -->`
- 【Linux社区】Pinchart 承认笔误；“fork 一般生成痛苦但仔细做有时仍有意义；偏好=选经过考验的+加 FAQ 澄清灰区” `<!-- ROW_MINE: ksummit-discuss.messages.349720 -->`
- 【Linux社区】Perches：“不必然二选一、也轮不到 downstream 替 upstream 决定” `<!-- ROW_MINE: ksummit-discuss.messages.349718 -->`
- 【Linux社区】Pinchart 答：“与上游讨论拟议变更能带来有价值反馈（即使不被接受）” `<!-- ROW_MINE: ksummit-discuss.messages.349717 -->`
- 【Linux社区】Triplett：“补丁该去上游；适用澄清该放单独的 **code-of-conduct-process.rst**” `<!-- ROW_MINE: ksummit-discuss.messages.349710 -->`
- 【Linux社区】Triplett：“情形与提案不完全同（补丁已写好）；邮件地址附于公开发布的补丁 hardly private information” `<!-- ROW_MINE: ksummit-discuss.messages.349711 -->`
- 【Linux社区】Jani：“听到 horse's mouth 指示前改本地 rst 多半徒劳；不阻止直接向上游提改进” `<!-- ROW_MINE: ksummit-discuss.messages.349715 -->`
- 【Linux社区】jonsmirl 新问：CoC 能适用于公司实体吗？“Google 在中国被指控违规、然后所有 Google 开发者被封？” `<!-- ROW_MINE: ksummit-discuss.messages.349721 -->`
- 【Linux社区】Tim Bird：“No——scope 条款限于 project spaces 与代表项目的个人；有疑虑请建议措辞修改” `<!-- ROW_MINE: ksummit-discuss.messages.349722 -->`
- 【Linux社区】Bottomley：“CoC 不是 one size fits all、可做不上游的本地补丁——上游专注 github 社区” `<!-- ROW_MINE: ksummit-discuss.messages.349724 -->`
- 【Linux社区】Triplett 纠正：“Zephyr 没采纳——只是有人提议未 merge”；“上游会欢迎澄清邮件列表社区适用的补丁” `<!-- ROW_MINE: ksummit-discuss.messages.349728 -->`
- 【Linux社区】Bottomley：“‘someone’恰好是 Zephyr 社区经理；路线应是先让它为我们工作、再看上游要不要” `<!-- ROW_MINE: ksummit-discuss.messages.349729 -->`

## 58.5 【Linux社区】discrimination 列表与 doxxing 边界

Geert 的 discrimination 列表删除补丁与 Triplett 的“显式指南”辩护、Vetter/Bottomley 的 doxxing 边界之辩与 Airlie 的上游同步顾虑——CoC 修订的方法论之争。

- 【Linux社区】Geert 新补丁：删歧视因素显式列表——“显式列表可能给人错觉：基于未列因素的歧视被允许”（附 UNESCO race 声明注） `<!-- ROW_MINE: ksummit-discuss.messages.349738 -->`
- 【Linux社区】Triplett 答：“显式列表正是其目的（Explicit guidelines have demonstrated success）——删了适得其反；这不是合适场所，正如不是给 GPL 打补丁的场所” `<!-- ROW_MINE: ksummit-discuss.messages.349741 -->`
- 【Linux社区】Pinchart：“那什么才是让我们共同决定修改并提上游的场所？反复说此处不对不会让关切消失——只有讨论问题才能得出解决方案” `<!-- ROW_MINE: ksummit-discuss.messages.349748 -->`
- 【Linux社区】Vetter 答 patch 1/2：fd.o 结论=未经同意挂 Reported-by 确是问题；Bugzilla 表面保护实则邮件可取——退役换 gitlab 的原因之一；“私下渠道报告须明确同意才能发布” `<!-- ROW_MINE: ksummit-discuss.messages.349739 -->`
- 【Linux社区】Bottomley：“维护者搞错不应等同于 doxxing；准法律文档放 examples 的问题：可争辩未提及者皆可接受；维护者失误加 Reported-by 该算 CoC 违规吗？多数维护者会答 no” `<!-- ROW_MINE: ksummit-discuss.messages.349744 -->`
- 【Linux社区】Reinecke：“我的解读相同；**submitting-patches.rst** 本就写了——不必再澄清” `<!-- ROW_MINE: ksummit-discuss.messages.349740 -->`
- 【Linux社区】Airlie：“同意要类似的东西；问题是改上游 CoC 文本还是单独节澄清——偏离上游措辞会让将来合并上游新版本更棘手” `<!-- ROW_MINE: ksummit-discuss.messages.349755 -->`

## 58.6 【Linux社区】KS2014 档案四封

页内夹杂的 KS2014 档案信（2014-05-15）：kerneloops 衰落实录、ARM legacy TODO 文件设想、tinification 谱系论与摩斯码 oops 前史。

- 【Linux社区】hpa：kerneloops.org 因 Fedora 等停止参与而“基本失去用处”（2014-05-15 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349712 -->`
- 【Linux社区】Jason Cooper：**arch/arm/*/TODO** 文件 helpful；LinuxCon 临近可获发行版反馈；ixp4xx/NSLU2 实例（2014-05-15 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349723 -->`
- 【Linux社区】hpa：tinification 与 mainline 目标/非目标会是极好 KS 议题；“把 Linux 尽可能拉伸过整个计算谱系”（2014-05-15 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349734 -->`
- 【Linux社区】Kosina：忆键盘 LED/PC 喇叭摩斯码发 oops 旧补丁集；“手机 app 解码摩斯回 oops 即可”（2014-05-15 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349745 -->`
