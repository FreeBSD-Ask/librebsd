# 59 【Linux社区】CoC补丁战终局Cox法理重磅

> 来源：ksummit-discuss p111（50 封全读，2018-10-07/09，夹杂 KS2014 档案信 2014-05-15）。
> 判定：50 CAND / 0 NV。主题分布：coc 43、KS2014 5、zufs 2。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p111（pk 349756-349805）的逐封提取（50 CAND / 0 NV），全 9 块采用**导语＋带锚条目体例**：每块由“## 59.x 【Linux社区】题名”＋导语段＋“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——导语段承担“要点”职能、带锚条目承担“史料”与“史料锚”职能（ROW_MINE 坐标与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 59.1 【Linux社区】Alan Cox 法理重磅：TAB 隐私承诺与现实的三重不兼容

2018-10-08 CoC 论战的法律纵深：Alan Cox 的 EUCD/强制报告/快通道三重不兼容推演与法庭五问、Viro 的“upstream 不适配”社区结构论与 Airlie 的“CoC 维护者是谁”之问。

- 【Linux社区】Cox：“TAB 反正处理不了——报告隐私承诺与现实不兼容：1) EUCD 可强制披露（TAB 无法律特权）2) 许多法域某些指控必须报执法 3) 天主教会灾难表明严重指控须快通道送法律系统”；剧场场景：A 投诉 B→B 雇主解雇 B→B 以 EUCD 迫 TAB 交投诉细节→B 起诉 A/TAB/LF/雇主——法庭五问“书面政策？谁批准？资质？完整记录？谁为竞争公司工作？”——“我们没有、没人、没有、呃我想有个邮件线程可不太好看”；双 Reviewed-by `<!-- ROW_MINE: ksummit-discuss.messages.349777 -->`
- 【Linux社区】Cox 驳“不是合适场所”：“GPLv2/v3 讨论在内核列表、syscall 澄清在列表、EXPORT_SYMBOL(_GPL) 也在列表讨论过” `<!-- ROW_MINE: ksummit-discuss.messages.349779 -->`
- 【Linux社区】Al Viro 讽 Airlie 被动语态“Considered appropriate by whom?”；“upstream 显然不适合 Linus 内核社区结构——开放列表/子项目量/入主线传输链长度/贡献者总量/偶入者数量；CoC 上游自己都说不适配” `<!-- ROW_MINE: ksummit-discuss.messages.349757 -->`
- 【Linux社区】Viro 自嘲更正 explanations→clarifications——“或任何你偏好的训诂委婉语” `<!-- ROW_MINE: ksummit-discuss.messages.349758 -->`
- 【Linux社区】Airlie：“好问题：我们有 CoC 维护者吗？Linus？Greg？TAB？第一步是找到能改内核 CoC 的人”；“修上游值得——省得大家各自分叉”；GPL 类比“GPLv2 only+syscall 例外” `<!-- ROW_MINE: ksummit-discuss.messages.349759 -->`

## 59.2 【Linux社区】Mauro 替代补丁与 GitHub 源流论

Mauro 的第三版 CoC 补丁（may remove+Reports 节最小化）与 GitHub 源流论的完整阐述：X.400 历史旁注、A/B/C 责任错位解构、邮件/Bugzilla/Mediawiki 三工作流不可执行性证明。

- 【Linux社区】Mauro 自拟替代补丁：“‘right and responsibility to remove’→‘may remove’（原文太法律腔）；Enforcement 节改 Reports 节、只留可联系 TAB 一句、其余全删；其余保持隐含、讨论后再议” `<!-- ROW_MINE: ksummit-discuss.messages.349794 -->`
- 【Linux社区】Mauro A/B/C 解构致 Vivi：“CoC 字面：A 侮辱 B、维护者 C 有责任对 B 采取行动；C 不行动 B 可向 TAB 投诉 C（而非 A）；被问责的不是失礼者、而是没能教育 A 的别人；善意维护者也无法执行——邮件工作流不可能删除公开列表及镜像上的邮件” `<!-- ROW_MINE: ksummit-discuss.messages.349795 -->`
- 【Linux社区】Mauro GitHub 源流论：“该怪互联网基础设施不允许编辑已发邮件（八十年代 X.400 就允许）；CoC 无任何说 TAB 会处置 Developer A 的内容——唯一会被罚的是维护者；此 CoC 为 Github 而生——作者与维护者都有全权编辑/删除、GitHub 背后有公司需要防诉讼；用于邮件行不通、Bugzilla/Trac 不行、Mediawiki 不完全行；要么修它、要么工作流改成只用 Github 类系统” `<!-- ROW_MINE: ksummit-discuss.messages.349797 -->`
- 【Linux社区】Mauro Reviewed-by patch 1/2 `<!-- ROW_MINE: ksummit-discuss.messages.349790 -->`
- 【Linux社区】Mauro：“加入 MAINTAINERS 则请加 R: 条目——它在我国的立法下可能有法律价值、我想被通知变更”（呼应 CoC 维护者之问） `<!-- ROW_MINE: ksummit-discuss.messages.349791 -->`
- 【Linux社区】Mauro：“报 bug/回补丁时邮件会被看见并可能用于修复补丁——不想如此须明确声明；此类特例适合 FAQ 而非正文” `<!-- ROW_MINE: ksummit-discuss.messages.349792 -->`

## 59.3 【Linux社区】反剥同盟：Mason、Triplett 与 Williams

剥 enforcement 的最强反对声：Mason 的“社区整体不承诺帮助”定性、Triplett 的“专职受训团队优于技术决策机构”、Williams 的“求助即合理参与”——与 Bottomley/Shuah 剥除派的形成对照。

- 【Linux社区】Chris Mason 反剥 enforcement：“我热爱我们在讨论它；剥掉 enforcement 基本回到过去——等于承认问题存在、却明确声明严重事件发生时社区整体不承诺帮助；执行节给了继续讨论的空间” `<!-- ROW_MINE: ksummit-discuss.messages.349785 -->`
- 【Linux社区】Triplett：“Emphatically seconded；绝对同意应随时间完善执行节——专职团队（最好受过培训）优于交给技术决策机构；但不该整体删除；4.19 发布与 -rc/git HEAD 无特殊区别” `<!-- ROW_MINE: ksummit-discuss.messages.349787 -->`
- 【Linux社区】Mason：“CoC 请维护者参与维护文化以及代码；后果大概率是努力让事情变好、不行再试”（常识应用论） `<!-- ROW_MINE: ksummit-discuss.messages.349801 -->`
- 【Linux社区】Triplett 答 Rainer Fiebig（28 行 vs 81 行还要 FAQ）：“事实证明这比之前被过度简化的更复杂——人们不会自动共享共同理解” `<!-- ROW_MINE: ksummit-discuss.messages.349802 -->`
- 【Linux社区】Dan Williams：“这些情形可能很乱、维护者可能没能力或没情绪资源随时应对——合理方式是求助；需要可信赖的人愿意帮助贡献者与维护者 alike、TAB 的任务就是提供帮助；旧 CoC 即此情形、新 CoC 更显式” `<!-- ROW_MINE: ksummit-discuss.messages.349805 -->`

## 59.4 【Linux社区】上游 FAQ 实测与“他人控制的文档”之辩

Contributor Covenant 上游互动实录：Tim Bird 的 FAQ 实测报告（Coraline 支持/issue 590/575/610）、Bottomley-Mauro 的“他人控制文档”反对论、Triplett 的 FAQ 已 merge 回执与 Brown 的“长得像法律文档”观察。

- 【Linux社区】Tim Bird 上游实测报告：向 Contributor Covenant 提出 email 澄清——维护者 Coraline Ada Ehmke 友善支持、FAQ 正在创建、决定不改正文（不想稀释私人信息需许可表述）；其 FAQ 建议全文（公共列表自愿发布信息不属私人信息）；issue 590/575 `<!-- ROW_MINE: ksummit-discuss.messages.349770 -->`
- 【Linux社区】Pinchart 问 Tim：“如果我们有自己的 FAQ、须与主文档合读才能理解——这不产生与 fork 相同的碎片化问题吗？” `<!-- ROW_MINE: ksummit-discuss.messages.349771 -->`
- 【Linux社区】Geert：“今晨发现这已包含在上游 FAQ；FTR 我今天也提交了补丁（issue 610）” `<!-- ROW_MINE: ksummit-discuss.messages.349772 -->`
- 【Linux社区】Triplett：“上游现已采用 FAQ 解决此与诸多问题；建议在文档底部加链接” `<!-- ROW_MINE: ksummit-discuss.messages.349775 -->`
- 【Linux社区】Bottomley：“永远不该指向一个由他人控制的、关于我们社区如何执行自己 CoC 的外部文档” `<!-- ROW_MINE: ksummit-discuss.messages.349776 -->`
- 【Linux社区】Geert 引 Coraline：“任何采纳项目可依许可证自由修改文档；将在（Linux 外部）FAQ 澄清” `<!-- ROW_MINE: ksummit-discuss.messages.349780 -->`
- 【Linux社区】Triplett：“讨论可在列表上、补丁不该在此；顺带：我提的 FAQ 修改已 merge（PR 612）” `<!-- ROW_MINE: ksummit-discuss.messages.349781 -->`
- 【Linux社区】Mauro：“完全同意不该指向他人控制的外部文档；GPL 2 only 同理——锁定具体版本；FAQ 里有 social contract 字样——至少在巴西 social contract 与 contract 同等法律效力” `<!-- ROW_MINE: ksummit-discuss.messages.349788 -->`
- 【Linux社区】Triplett：“链接 FAQ 不使其 binding——这不是法律协议” `<!-- ROW_MINE: ksummit-discuss.messages.349793 -->`
- 【Linux社区】Brown：“人们把 contributor covenant 当法律文件解读不算不合理——它明确列出行为、指定后果，看起来就像法律文档；对非母语者尤甚；若大家宁过于严肃对待 CoC，也不算最坏” `<!-- ROW_MINE: ksummit-discuss.messages.349798 -->`
- 【Linux社区】Tim Bird：“不为修改 CoC 论所动：我们已经改了措辞/与上游不会太冲突/上游不会剧变到难以采纳；不担心 fork——上游重大变更采纳前应有内核社区辩论（类似 GPL v3 的辩论与最终拒绝）” `<!-- ROW_MINE: ksummit-discuss.messages.349773 -->`

## 59.5 【Linux社区】fork 之辩与上游同步成本

fork 成本与同步模型之争：Geert 的 ABI 类比 revert 论、Bottomley 的 vendor driver 流程移植、Brown 的 Debian rules-lawyer 经验与 Luck 的 500 词反讽。

- 【Linux社区】Triplett 区分场所：“讨论可在 ksummit-discuss（不理想但暂无更好）；补丁该去上游——公共列表地址非私人信息的澄清其他项目也受益” `<!-- ROW_MINE: ksummit-discuss.messages.349760 -->`
- 【Linux社区】Geert：“commit message 第一段（why）正是我们等澄清的；(至少)该把列表标为示例；**COPYING** 曾是 GPL 逐字拷贝+顶部澄清；若本地修订不可行——plain revert 是唯一选项，如其他破坏用户空间 ABI 的提交一样” `<!-- ROW_MINE: ksummit-discuss.messages.349762 -->`
- 【Linux社区】Brown 辨 GPL 类比：“许可证行得通因读者本来就逐字抠——读 CoC 求安心的人未必；值得想一想” `<!-- ROW_MINE: ksummit-discuss.messages.349763 -->`
- 【Linux社区】Brown：“Debian CoC 也省略因素显式列表——有意为之：真怕人 rules lawyer；社区足够相似值得考虑、Debian 有处理严重问题的经验” `<!-- ROW_MINE: ksummit-discuss.messages.349764 -->`
- 【Linux社区】Bottomley 答 Airlie：“CoC 应清晰、不该被脚注和解释包围；vendor driver 类比——先为我们自己改好、再看源怎么处理；共识定形后我保证尝试推回” `<!-- ROW_MINE: ksummit-discuss.messages.349768 -->`
- 【Linux社区】Tony Luck：“整个文档不足 500 词——我们能 merge 数万行代码、这容易得多；难 merge 新上游版本也可视为好事” `<!-- ROW_MINE: ksummit-discuss.messages.349782 -->`

## 59.6 【Linux社区】剥 enforcement 节之辩：起点还是回归

剥除派与保留派的细部拉锯：Tim Bird 的“中央报告=Code of Conflict 已有”论与“十年三封禁”统计、Bottomley 的“不预判结果”程序原则与 v2 承诺。

- 【Linux社区】Tim Bird：“Code of Conflict 三年前已建中央报告机制——保留该段更接近 status quo；绝大多数情况 TAB 将扮演调解人；封禁将继续极少——过去十年我只想到 3 次” `<!-- ROW_MINE: ksummit-discuss.messages.349765 -->`
- 【Linux社区】Bottomley：“若要回 status quo 那 plain revert 才是我该提的补丁集；这次完全透明要求不预判结果——可预见把 CoC 执行授予非 TAB 机构、甚至非正式维护者名单” `<!-- ROW_MINE: ksummit-discuss.messages.349769 -->`
- 【Linux社区】Tim Bird 澄清：“我不想回 status quo；保留文档但去掉中央报告机制=大偏离；ombudsman 类角色有益；新 CoC 部分优于旧、偏好保留+逐步调整” `<!-- ROW_MINE: ksummit-discuss.messages.349783 -->`
- 【Linux社区】Bottomley：“补丁目的是 Shuah 峰会 CoC 辩论的有用起点（v2 将澄清）；不预判结果” `<!-- ROW_MINE: ksummit-discuss.messages.349784 -->`
- 【Linux社区】Tim Bird：“第二个 hunk 可作起点、第一个不行——第一 hunk 是回归、接近 Code of Conflict 已有内容” `<!-- ROW_MINE: ksummit-discuss.messages.349786 -->`

## 59.7 【Linux社区】Eich 领导层攻击论与“房间里的大象”

CoC 论战的目标层分歧：jonsmirl 的“领导层攻击才是真问题”、Vivi 的“角落案例拆关键条款”批评与“加法而非减法”主张、Pinchart 的共同目标之问与 Bottomley 的 GPLv2 式回应。

- 【Linux社区】jonsmirl：“问题会出现在前五号人物之一被指控——会上主流媒体、大钱与公司力量入场；CoC 须设计成能应对 Brendan Eich 局面——他最初是被外部攻击的；坚持法律界应在成为正式政策前发声” `<!-- ROW_MINE: ksummit-discuss.messages.349774 -->`
- 【Linux社区】Vivi：“谢谢解释——也许我现在明白为何有人 freak out；公司会因维护者纵容骚扰而解雇他吧？永久封禁只应重复发生+明显纵容时；也许该扩写加 TAB 建议程序；但我目前看到的补丁都在用不太可能的角落案例来论证删除关键部分——比如强调种族主义不可接受的部分” `<!-- ROW_MINE: ksummit-discuss.messages.349796 -->`
- 【Linux社区】Vivi：“那就改写成 if possible 时编辑或拒绝——能编辑而不行动就是纵容；我的建议是做加法使程序更清晰，而不是删除关键部分；另一个更快迁移 Gitlab 的理由？” `<!-- ROW_MINE: ksummit-discuss.messages.349799 -->`
- 【Linux社区】Pinchart：“房间里的大象：我们一直小心避免讨论人们是否共享共同目标 :-/” `<!-- ROW_MINE: ksummit-discuss.messages.349803 -->`
- 【Linux社区】Bottomley：“我们不需要共享共同目标；只需按其本身价值发现文档有用——正如我们是 mostly GPLv2 项目而不接受多数 FSF 哲学；也因此要把自己的解释与澄清留在内部” `<!-- ROW_MINE: ksummit-discuss.messages.349804 -->`

## 59.8 【Linux社区】ZUFS 轨道问答二则

ZUFS 议题的程序性尾声：议题定案时程不明与订机票现实。

- 【Linux社区】Boaz 问 Kernel sub-tracks [TECH TOPIC] 何时定案——“我要订机票” `<!-- ROW_MINE: ksummit-discuss.messages.349761 -->`
- 【Linux社区】Greg：“不知道何时定案，抱歉” `<!-- ROW_MINE: ksummit-discuss.messages.349766 -->`

## 59.9 【Linux社区】KS2014 档案五封

页内夹杂的 KS2014 档案信（2014-05-15）：tinification 三连附议、QR 线程转 LKML、kerneloops 数据实况与 printk softlockups 议题立项。

- 【Linux社区】Greg KH 附议 tinification：“既是有效议题、也是 Linux 应达成的目标”（2014-05-15 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349756 -->`
- 【Linux社区】Roeck 附议 tinification（2014-05-15 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349767 -->`
- 【Linux社区】Kurusa：“把技术讨论整理后发 LKML RFC 线程”（2014-05-15 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349778 -->`
- 【Linux社区】Kurusa：oops.kernel.org 5 月已有 ~4K oopses、Fedora 仍在发；“问题是维护者几乎不看它；我们是愿意做错误报告收集核心工作的人”（2014-05-15 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349789 -->`
- 【Linux社区】Jan Kara 新议题 Printk softlockups：大机器串口控制台 console_unlock() 数十秒→softlockup/RCU stall/系统死；8 轮补丁迭代受挫；求 printk 保证与复杂度共识的当面会议（2014-05-15 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349800 -->`
