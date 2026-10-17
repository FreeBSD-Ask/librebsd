# 54 【Linux社区】CoC法律定性之战与gerrit之争

> 来源：ksummit-discuss p106（50 封全读，2018-09-18/19，夹杂 KS2014 档案信 2014-05-15）。
> 判定：50 CAND / 0 NV。主题分布：coc 13、communication 23、distro-bugzilla 7、KS2014 4、next-discipline 2、governance 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p106（pk 349506-349555）的逐封提取（50 CAND / 0 NV），全 6 块采用**导语＋带锚条目体例**：每块由“## 54.x 【Linux社区】题名”＋导语段＋“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——导语段承担“要点”职能、带锚条目承担“史料”与“史料锚”职能（ROW_MINE 坐标与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 54.1 【Linux社区】CoC“私人信息”条款法律定性之战：从补丁标签到附合合同

2018-09-18/19 CoC 之战的法律深化：Mauro 的标签-条款冲突论与“附合合同”定性、Bottomley 的 DCO 解释与“non-public ⊃ private”思想实验、Pinchart 的意图澄清与 Josh 的 GPL FAQ 类比——新旧 CoC 文本对比首次全引。

- 【Linux社区】Mauro 新弹：CoC“publishing others' private information”条款与补丁标签冲突——SOB/Reviewed-by/Acked-by 均在发布电子地址；DCO 1.1 (d) 不覆盖其他标签；“维护者或须推迟拉取” `<!-- ROW_MINE: ksummit-discuss.messages.349519 -->`
- 【Linux社区】Josh Triplett：发过公开邮件即非私人信息、主动提供标签即许可；“从未公开的私人地址入 Acked-by 才有问题” `<!-- ROW_MINE: ksummit-discuss.messages.349521 -->`
- 【Linux社区】Mauro：条款明文“without explicit permission”必然多解；Requested-by/Suggested-by 常由维护者加；应明文排除公共社区渠道用过的电子地址 `<!-- ROW_MINE: ksummit-discuss.messages.349525 -->`
- 【Linux社区】Arnaldo 补刀：文档允许把“yep, looks good to me”手工转成 Acked-by——新 CoC 下这种手工转换须停 `<!-- ROW_MINE: ksummit-discuss.messages.349526 -->`
- 【Linux社区】Iwai：非强制标签“可去掉地址部分” `<!-- ROW_MINE: ksummit-discuss.messages.349530 -->`
- 【Linux社区】Josh Triplett 措辞之辩：应写在“如何适用的配随文”；类比“GPL FAQ 不是 GPL 的一部分” `<!-- ROW_MINE: ksummit-discuss.messages.349532 -->`
- 【Linux社区】Rostedt 自述 Reported-by 工作流：私下报告先征询、公开 CC 直接署名 `<!-- ROW_MINE: ksummit-discuss.messages.349536 -->`
- 【Linux社区】Pinchart 澄清条款意图：防人未经同意被置于聚光灯遭骚扰；建议“同一语境公开渠道已公开的信息不属私人信息”+“首次偶然披露不致即时惩戒” `<!-- ROW_MINE: ksummit-discuss.messages.349538 -->`
- 【Linux社区】Bottomley：“including all personal information I submit with it”覆盖所有标签；DCO (d) 为国家数据保护法而设、必覆盖 CoC 许可 `<!-- ROW_MINE: ksummit-discuss.messages.349550 -->`
- 【Linux社区】Mauro 定性：“一份写得很糟的附合合同（Contract of Adhesion）——给维护者创设大量新义务与违约罚则”；等美国法律意见、巴西法下几乎肯定是合同 `<!-- ROW_MINE: ksummit-discuss.messages.349551 -->`
- 【Linux社区】Mauro 补充更正：“I believe that this is a legal document”；仍等 US 法律意见中 `<!-- ROW_MINE: ksummit-discuss.messages.349552 -->`
- 【Linux社区】Bottomley 思想实验：“non-public”措辞可覆盖标签情形但 US 法上 non-public ⊃ private、原文义务更窄——标签用法不违反隐私义务 `<!-- ROW_MINE: ksummit-discuss.messages.349553 -->`
- 【Linux社区】Mauro 总攻：“可修则修、否则 revert”；“每读一遍更信它是 utter crap”；举 LF 隐私政策把 email 列为 Personal information；须由懂开源的律师准备；引旧 Code of Conflict 全文对比——旧文不阻止标签、不把维护者变保姆 `<!-- ROW_MINE: ksummit-discuss.messages.349554 -->`

## 54.2 【Linux社区】gerrit 之争与 vapor-git-thingy：kernel.org 补丁网关构想

kernel.org 补丁网关构想的全景：Konstantin 八步草案与 vapor-git-thingy CLI、Greg 的 feedback loop 质疑、gerrit 三种立场（Ted 喜欢/Torokhov 反感/Pinchart 判死刑“会杀死内核社区”）、CI 归位之争与 Fuego 接口。

- 【Linux社区】Tim Bird 回 Linus：MAINTAINERS 列前端邮件接收地址做补丁预处理（含 CI）再转官方列表；子系统可选择性加入 `<!-- ROW_MINE: ksummit-discuss.messages.349506 -->`
- 【Linux社区】Tim Bird 对八步草案惊呼 re-converged；自认 GREAT thing、须维护者 buy-in `<!-- ROW_MINE: ksummit-discuss.messages.349507 -->`
- 【Linux社区】Geert：赞成+github 集成可从分支发系列；须防 v2.6.12-rc2 全系列垃圾；奇怪 git send-email 至今没出过这种事故 `<!-- ROW_MINE: ksummit-discuss.messages.349508 -->`
- 【Linux社区】Greg KH 质疑代发：冒充 sony.com 发不出去；munging 后成中间人转发；“feedback loop 才是崩坏处——我只收 1/3 补丁”；“那我们发明了 gerrit！好主意但别 gerrit” `<!-- ROW_MINE: ksummit-discuss.messages.349509 -->`
- 【Linux社区】Konstantin 追加想象功能：账户挂远程 git 树别名+CLI vapor-git-thingy 自动生成补丁；“我能凑到资金” `<!-- ROW_MINE: ksummit-discuss.messages.349510 -->`
- 【Linux社区】Konstantin 答 Greg：SRS0 envelope-sender 已在用、可过 DKIM/SPF；“叫 ging——ging is not gerrit” `<!-- ROW_MINE: ksummit-discuss.messages.349511 -->`
- 【Linux社区】Torokhov “Seconded no gerrit”：Chrome OS 评审 75% 时间耗在点 UI `<!-- ROW_MINE: ksummit-discuss.messages.349513 -->`
- 【Linux社区】Sasha：不必冒充原作者——From: 字段 git 自会做对、Cc 原作者问答直达 `<!-- ROW_MINE: ksummit-discuss.messages.349514 -->`
- 【Linux社区】Tim Bird 特别关注第 5 步测试插槽——愿以 Fuego 维护者身份参与 `<!-- ROW_MINE: ksummit-discuss.messages.349515 -->`
- 【Linux社区】Ted 异端立场：“I actually like Gerrit”；小改动 web 上下文/行内评论/版本 diff 皆佳、大系列下载本地 git；“不应全盘否定” `<!-- ROW_MINE: ksummit-discuss.messages.349516 -->`
- 【Linux社区】Konstantin：CI 应留范围之外——0daybot/syzbot 已 hone 于邮件列表；坚持先测则拉 kernelci 入局；将在温哥华 KS 与 Kevin 面谈 `<!-- ROW_MINE: ksummit-discuss.messages.349518 -->`
- 【Linux社区】Pinchart：能否用（未认证）git push 作第 3/4 步？ `<!-- ROW_MINE: ksummit-discuss.messages.349535 -->`
- 【Linux社区】Belloni：问 SRS0 munging 会不会破坏 patchwork（作者名被按邮箱旧名改写的前科） `<!-- ROW_MINE: ksummit-discuss.messages.349533 -->`

## 54.3 【Linux社区】附件补丁攻防收束与 Outlook/Exchange 强制用例

附件补丁之辩的工具层收束：claws-mail/mutt/hch 证言、reply-as-inline 构想、2FA 与 EWS OAuth2 出路。

- 【Linux社区】Woodhouse 反问：被强制用 Exchange 可以、“但 Outlook？”；format-patch→Evolution Drafts 法几乎人人可用 `<!-- ROW_MINE: ksummit-discuss.messages.349517 -->`
- 【Linux社区】Sasha：公司政策强制 Exchange 2FA 时无 non-outlook 应用支持 `<!-- ROW_MINE: ksummit-discuss.messages.349520 -->`
- 【Linux社区】Josh Triplett：“那不如别用那个邮箱账户发补丁” `<!-- ROW_MINE: ksummit-discuss.messages.349522 -->`
- 【Linux社区】Woodhouse：Evolution EWS OAuth2 wiki+GNOME bugzilla 775690；“比应有难度大但据说对某些人可用” `<!-- ROW_MINE: ksummit-discuss.messages.349524 -->`
- 【Linux社区】Iwai：附件法是最后手段；“展开附件回复有点痛，但嘿，我用 Emacs，伟大的 OS 本身” `<!-- ROW_MINE: ksummit-discuss.messages.349529 -->`
- 【Linux社区】Rostedt claws-mail 技巧：附件全选→回复即如正文、可行内评论 `<!-- ROW_MINE: ksummit-discuss.messages.349531 -->`
- 【Linux社区】Pinchart：愿支持附件补丁若能“reply-as-inline”一键内联引述开评；单客户端易、补齐所有流行客户端难 `<!-- ROW_MINE: ksummit-discuss.messages.349537 -->`
- 【Linux社区】Brown：mutt 更佳——text MIME 附件默认内联进回复；发件方 MIME 标错则破 `<!-- ROW_MINE: ksummit-discuss.messages.349539 -->`
- 【Linux社区】hch：“近来附件补丁鲜有问题、mutt 回复透明处理” `<!-- ROW_MINE: ksummit-discuss.messages.349541 -->`
- 【Linux社区】Bottomley：SCSI 早收 exchange 人附件补丁（空白损伤无解时）；“若这是补丁出公司的唯一通道，痛可接受” `<!-- ROW_MINE: ksummit-discuss.messages.349549 -->`

## 54.4 【Linux社区】SCSI patch-id 之辩收束：distro 自动化 95%

SCSI/distro 排序之辩的技术收束：git patch-id 概念教学（HID redragon 实例）、“95% rebase 自动化”共识与 topic 分支短命数之争。

- 【Linux社区】Iwai：topic 分支法若更频繁合回主干更好；merge“fixate”topic、未合的坏分支仍可扔 `<!-- ROW_MINE: ksummit-discuss.messages.349527 -->`
- 【Linux社区】Iwai 问“什么是 git patch id”；答 Petersen：“upstream enough”=git topo 排序+合入后挪移；rebase 后旧 commit ID 消失可用 tag/命名分支保留；“像是缺乏沟通” `<!-- ROW_MINE: ksummit-discuss.messages.349528 -->`
- 【Linux社区】Brown：频繁合回=更多 merge；trunk 无 commit 时长串 merge 亦被视 antipattern；冷门子系统“难以确信已毕” `<!-- ROW_MINE: ksummit-discuss.messages.349540 -->`
- 【Linux社区】Geert 教 git patch-id：不含依赖的补丁哈希、git cherry/rebase 用之；v4.18.y HID redragon 实例（两 commit 同 patch-id） `<!-- ROW_MINE: ksummit-discuss.messages.349542 -->`
- 【Linux社区】Iwai：patch-id 给不出补丁顺序（“两万补丁时反查太重”） `<!-- ROW_MINE: ksummit-discuss.messages.349544 -->`
- 【Linux社区】Jan Kara：patch-id 定位 rebase 后新 commit id 再推排序——“可自动化解决 SCSI 树 95% rebase” `<!-- ROW_MINE: ksummit-discuss.messages.349547 -->`
- 【Linux社区】Iwai 与同事核过可行：“patch-id 作 commit-id 补充信息，谢妙策” `<!-- ROW_MINE: ksummit-discuss.messages.349548 -->`

## 54.5 【Linux社区】linux-next 纪律与维护者特权续论

linux-next 通报机制与维护者特权之辩的续篇：Pinchart 评审被无视案例的完整叙述。

- 【Linux社区】sfr（Bug-introducing patches 线程）：每晚在 linux-next 列表收 Brown 总结；“disruptive 问题我该知道” `<!-- ROW_MINE: ksummit-discuss.messages.349543 -->`
- 【Linux社区】Brown 答 sfr：“都在列表上、不每件 CC 你除非急、你要的话可以” `<!-- ROW_MINE: ksummit-discuss.messages.349555 -->`
- 【Linux社区】Pinchart 回 tglx：维护者特权=绕过正常流程；亲身案例“评审数小时求改动仍原样合入、两次回复原评无答”；曾为客户谈成评审预算之例外 `<!-- ROW_MINE: ksummit-discuss.messages.349546 -->`

## 54.6 【Linux社区】KS2014 档案四封

页内夹杂的 KS2014 档案信（2014-05-15）：QR oops 线程的 what/who 之辩与 kerneloops 基础设施细节。

- 【Linux社区】Kurusa：kerneloops 三改进与 QR 屏占比之辩；URL+baseXX 路线失用户最少；bugzilla xml-rpc 认证问题 `<!-- ROW_MINE: ksummit-discuss.messages.349512 -->`
- 【Linux社区】PJ Waskiewicz 反驳 Ted“先做后谈”：“how 不难 what 难”——QR 进内核却无配套框架是失机 `<!-- ROW_MINE: ksummit-discuss.messages.349523 -->`
- 【Linux社区】Ted：“我追问的是 who——谁来干这一切？” `<!-- ROW_MINE: ksummit-discuss.messages.349534 -->`
- 【Linux社区】Teodora Băluţă：bugzilla 认证难、xml-rpc+REST 层之议、“X-times 自动 bugzilla”设想 `<!-- ROW_MINE: ksummit-discuss.messages.349545 -->`
