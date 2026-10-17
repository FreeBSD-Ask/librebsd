# 76 【Linux社区】mb2q工具与Link定型

> 来源：ksummit-discuss p128（50 封全读，2019-08 Change-Id 辩论收束段，夹杂 2014-05 档案信）
> 判定：47 CAND / 3 NV。主题分布：Change-Id 折中两步走 1、集成者立场与钩子流 1、钩子够用与否之争 1、git 原生 UUID 设想 1、重写系列断链论 1、退守工具路线 1、kernel.org 服务征集 1、系列反查示例 1、k.org 钩子承诺 1、可弃区 ID 存档方案 1、提案澄清与既有脚本 1、社区不可强制定性 1、维护者层强制 MsgID 1、Link 优于 ID 之问 1、quilt 工作流长文 1、ASoC 时钟依赖经验 1、applypatch-msg 配方 1、TAB 测试投票揭晓 1、无 Gerrit 链接澄清 1、自行其是预告 1、Linus 定罪 UUID 1、MsgID 即本地 UUID 1、Ted 求购 quilt 脚本 1、gregkh 实践与定论 1、承诺清理公开脚本 1、Doug 答辩 Linus 1、钩子发信可行性问 1、Joel 驳论与劝收尾 1、KS 日程草案 1、Link 语法之问 1、点破揉进 MsgID 1、mb2q 工具发布 1、patman 编码计划 1、勿手搓 msgid 1、gitk 链接补丁流转 1、有用性三分法 1、编码本意澄清 1、James 附议钩子之痛 1、Tglx 松口 msgid 方案 1、syzbot 标识困境 1、Link 即 UUID 1、LTS 标记与 patch-id 1、git note 应用流程 1、统一工具缺位质疑 1、patch-id 局限论 1、gregkh 自动加 Link 1、Roeck 模糊匹配之苦 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p128 的逐封提取（47 CAND / 3 NV），全 47 块采用**单行摘要体例**（丙型）：每块由“## 76.x 【Linux社区】题名”与若干“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 76.1 【Linux社区】Change-Id 折中两步走

- 【Linux社区】Doug 回应 Tglx：接受“截断线后放机器可读 Change-Id”加“落地补丁注入 Link://lkml.kernel.org/r/$MSGID_PER_PATCH”组合，忧普通提交者不会记得移 Change-Id，建议教 git-send-email 代劳 `<!-- ROW_MINE: ksummit-discuss.messages.350606 -->`

## 76.2 【Linux社区】集成者立场与钩子流

- 【Linux社区】Doug 自称立场是系统集成员而非提交者，靠本地分支 amend 与 rebase -i 使 Change-Id 自动留存，“git 钩子对我完美可用”，仅整补丁重写时才需手动复制 `<!-- ROW_MINE: ksummit-discuss.messages.350607 -->`

## 76.3 【Linux社区】钩子够用与否之争

- 【Linux社区】Torokhov 调侃“Doug 在此不是提交者”，称其 post-commit 钩子见无 Change-Id 则自动补、“从未需要手动加过”，git 只管把 ID 记进提交信息 `<!-- ROW_MINE: ksummit-discuss.messages.350608 -->`

## 76.4 【Linux社区】git 原生 UUID 设想

- 【Linux社区】Andrew Lunn 提议首次 git commit 分配 UUID、commit --am 不动它、format-patch 把 UUID 放 --- 之后、由 send-email 据 UUID 生成 MSGID `<!-- ROW_MINE: ksummit-discuss.messages.350609 -->`

## 76.5 【Linux社区】重写系列断链论

- 【Linux社区】Joel 论断上游开发是演进的，v1 与 v2 可整组不同，“再多自动 ID 生成也链不起来”，须手动复制 Change-Id 的场景才是最值得追踪的 `<!-- ROW_MINE: ksummit-discuss.messages.350610 -->`

## 76.6 【Linux社区】退守工具路线

- 【Linux社区】Doug 表态若 Change-Id 不能随提交落地，给 git-send-email 与 git-format-patch 加智能“绝对是该走的路” `<!-- ROW_MINE: ksummit-discuss.messages.350611 -->`

## 76.7 【Linux社区】kernel.org 服务征集

- 【Linux社区】2014 档案：hpa 与 Linux Foundation 商议内核开发者需要哪些 IT 服务，kernel.org 整治后旧需求移往私有设备或云，提议提供托管或非托管 VM 减轻顶层开发者负担 `<!-- ROW_MINE: ksummit-discuss.messages.350612 -->`

## 76.8 【Linux社区】系列反查示例

- 【Linux社区】Doug 用 frob/larb/sneech 三补丁示例：工具见系列内任一 Change-Id 相同即可帮找回整个 v1 系列，全丢则“也许本就该算新系列” `<!-- ROW_MINE: ksummit-discuss.messages.350613 -->`

## 76.9 【Linux社区】k.org 钩子承诺

- 【Linux社区】kernel.org 的 Konstantin Ryabitsev 答复 Linus：可用简单钩子给 Link: 与 Message-ID 做超链接，“我会把它记到清单上” `<!-- ROW_MINE: ksummit-discuss.messages.350614 -->`

## 76.10 【Linux社区】可弃区 ID 存档方案

- 【Linux社区】Joel 提议发送程序把唯一 ID 写进补丁可弃部分、归档仍在，由 email2git 或 patchwork 关联归档与提交，称“大家还需被说服接受往提交信息插唯一 ID” `<!-- ROW_MINE: ksummit-discuss.messages.350615 -->`

## 76.11 【Linux社区】提案澄清与既有脚本

- 【Linux社区】Joel 澄清本意是“非 message-id 的唯一 ID”不进提交、由发送程序写入可弃区，并自述已有脚本把提交信息中的元数据移入可弃部分作附加注记 `<!-- ROW_MINE: ksummit-discuss.messages.350616 -->`

## 76.12 【Linux社区】社区不可强制定性

- 【Linux社区】Tglx 定性“社区无法强制 changeid，Google 只能内部强制”，只求公开可访问的 Link，否则放封面信或可弃区 `<!-- ROW_MINE: ksummit-discuss.messages.350617 -->`

## 76.13 【Linux社区】维护者层强制 MsgID

- 【Linux社区】Tglx 提出若社区同意可对维护者强制 Message-ID 链接，“git 已有某种形式的支持”，给自研工具加此“并非难事” `<!-- ROW_MINE: ksummit-discuss.messages.350618 -->`

## 76.14 【Linux社区】Link 优于 ID 之问

- 【Linux社区】Brauner 称“链接肯定比 change-id 更有用”、不少维护者已在用各站链接，追问终极目标是否 Gerrit 与 LKML 同时评审、如何保证评审都见诸 LKML `<!-- ROW_MINE: ksummit-discuss.messages.350621 -->`

## 76.15 【Linux社区】quilt 工作流长文

- 【Linux社区】Tglx 详述二十年 quilt 流水线：发信脚本提取上一版封面信 MSGID 注入模板，收信脚本由 mbox 建 quilt 系列并自动收集 R-b/A-b/T-b、加“Link: https://lkml.kernel.org/r/$MSGID”，另有回移植用 git 转 quilt 导出 `<!-- ROW_MINE: ksummit-discuss.messages.350622 -->`

## 76.16 【Linux社区】ASoC 时钟依赖经验

- 【Linux社区】2014 档案：Mark Brown 称 ASoC 同有此题，DT 化设备照 Kevin Hilman 建议让设备自持时钟，“理想是靠 common clock API 把整棵时钟树放进去” `<!-- ROW_MINE: ksummit-discuss.messages.350623 -->`

## 76.17 【Linux社区】applypatch-msg 配方

- 【Linux社区】Mark Brown 给出钩子配方：在 .git/hooks/applypatch-msg 用 perl 正则把 Message-Id 行改写为“Link: https://lore.kernel.org/r/$1” `<!-- ROW_MINE: ksummit-discuss.messages.350624 -->`

## 76.18 【Linux社区】TAB 测试投票揭晓

- 【Linux社区】Laura Abbott 公布 TAB 投票流程测试结果：为 Greg KH 的 LPC 里斯本 T 恤选出的胜出口号是“Applied, Thanks!”与“This doesn't apply to my tree :(”，附 CIVS run-off 结果链接，正式投票信息随后再发 `<!-- ROW_MINE: ksummit-discuss.messages.350625 -->`

## 76.19 【Linux社区】无 Gerrit 链接澄清

- 【Linux社区】Doug 强调上游优先流程“根本没有 Gerrit 链接”，陈述终极目标（让工具识别新旧版本、或日后 Gerrit 与邮件列表整合）与短期目标（文本搜索找回 v1） `<!-- ROW_MINE: ksummit-discuss.messages.350626 -->`

## 76.20 【Linux社区】自行其是预告

- 【Linux社区】Doug 称若本议题无结论将自行把 Change-Id 放可弃区并引本帖自辩，称“补丁提交者极难训练”，否认有推广 Gerrit 的隐藏议程 `<!-- ROW_MINE: ksummit-discuss.messages.350627 -->`

## 76.21 【Linux社区】Linus 定罪 UUID

- 【Linux社区】Linus 断言“停止为 UUID 辩论，它们根本是坏主意”，唯一“有效”用途是藏进厂商私有数据库、“与开放开发的全部意义背道而驰”，应改用公开链接乃至 ISBN 类可查实物编号 `<!-- ROW_MINE: ksummit-discuss.messages.350628 -->`

## 76.22 【Linux社区】MsgID 即本地 UUID

- 【Linux社区】Ted 指出 Message-Id 由 git send-email 本地生成、与 UUID 同样易得，可写工具自动存下供 v2 引用，“Message-Id 与 Link 都严格优于 16 字节随机 Change-Id UUID” `<!-- ROW_MINE: ksummit-discuss.messages.350629 -->`

## 76.23 【Linux社区】Ted 求购 quilt 脚本

- 【Linux社区】Ted 自述 ext4 收件同样用 quilt，请 Tglx 分享其脚本，直接催生 mb2q 发布 `<!-- ROW_MINE: ksummit-discuss.messages.350630 -->`

## 76.24 【Linux社区】gregkh 实践与定论

- 【Linux社区】Greg 自述多年用脚本自造 message-id（疑源自 akpm 的 bash 脚本），现改在提交里生成“Link: https://lore.kernel.org/r/...”，并称“message-id 所含信息远多于 change-id”，笑称结果不出其所料 `<!-- ROW_MINE: ksummit-discuss.messages.350631 -->`

## 76.25 【Linux社区】承诺清理公开脚本

- 【Linux社区】Tglx 承诺“给我一两天去掉多年长的胶带”后公开脚本，即下封 mb2q 之由来 `<!-- ROW_MINE: ksummit-discuss.messages.350632 -->`

## 76.26 【Linux社区】Doug 答辩 Linus

- 【Linux社区】Doug 称 Linus 方案需提交者手动查询、“采用率会趋近于零”，辩 UUID 格式规整便于机器解析，并试拟把 Change-Id 编码进 Message-Id `<!-- ROW_MINE: ksummit-discuss.messages.350633 -->`

## 76.27 【Linux社区】钩子发信可行性问

- 【Linux社区】2014 档案：Josh Triplett 问 kernel.org 能否既支持 git 钩子大量收发邮件、又保住现行仓库安全与沙箱 `<!-- ROW_MINE: ksummit-discuss.messages.350634 -->`

## 76.28 【Linux社区】Joel 驳论与劝收尾

- 【Linux社区】Joel 驳“链接可指向任何东西”：lore.kernel.org/r/<message-id> 只指一处，提醒“社区层面强制不可能”，劝 Doug“放可弃区然后翻篇” `<!-- ROW_MINE: ksummit-discuss.messages.350635 -->`

## 76.29 【Linux社区】KS 日程草案

- 【Linux社区】Ted 发布 2019-09-09 至 11 Kernel Summit 轨道日程草案：KVA 分配器、Maple Tree、mmap_sem 两讲、KUnit、内联加密，周一 18:30 TAB 选举，并留开放时段 `<!-- ROW_MINE: ksummit-discuss.messages.350636 -->`

## 76.30 【Linux社区】Link 语法之问

- 【Linux社区】Doug 追问 v3 该用什么标签指回 v2（Link 还是 Link-prev-version），并给三理由主张编入 Message-Id：可弃区方案需新工具无人采用、自身预计仍会挨骂、可弃区 ID 终究也是 UUID `<!-- ROW_MINE: ksummit-discuss.messages.350637 -->`

## 76.31 【Linux社区】点破揉进 MsgID

- 【Linux社区】Tglx 问“什么阻止你把 change-id 揉进 message-id”：只要 v1..vn 的 msgid 保持唯一，lore 链接与 change-id 追踪两全，“多数人根本不会察觉” `<!-- ROW_MINE: ksummit-discuss.messages.350638 -->`

## 76.32 【Linux社区】mb2q 工具发布

- 【Linux社区】Tglx 发布 python3 版 mb2q（仅依赖 python3-yaml）：mbox 转 quilt 系列、自动收集标签并加 Link:，另有直接产出 git-am 可用 mailbox 的选项，暂以 git bundle 分发待 k.org 建仓 `<!-- ROW_MINE: ksummit-discuss.messages.350639 -->`

## 76.33 【Linux社区】patman 编码计划

- 【Linux社区】Doug 重申两条路：若 Change-Id 入提交如预期“保持 NAKed”，就改自己用的 patman 以“Message-Id: ChangeId-YYYY-MMDD-HHMMSS-PatchNum”编码并倡议同好跟进 `<!-- ROW_MINE: ksummit-discuss.messages.350640 -->`

## 76.34 【Linux社区】勿手搓 msgid

- 【Linux社区】Tglx 警告“用你所选语言的库函数，别自己拼”，给出 email.utils.make_msgid(changeid) 示例，自嘲格式不良邮件头的痛苦已经够多 `<!-- ROW_MINE: ksummit-discuss.messages.350641 -->`

## 76.35 【Linux社区】gitk 链接补丁流转

- 【Linux社区】Paul Mackerras 已把 gitk 识别 Link: 并开浏览器的补丁发到 git 列表（附 marc.info 链接），承诺待链接检测正则与各平台浏览器命令定论后提交 `<!-- ROW_MINE: ksummit-discuss.messages.350642 -->`

## 76.36 【Linux社区】有用性三分法

- 【Linux社区】Ted 解析 Change-Id 因 Gerrit 工具而生、服务器多藏防火墙后且有 robots.txt 故“大多无用”，预言钻规则空子的 Message-Id 连补丁一起被 NACK，给 RFC-5322 合法式样并以 linux-review.googlesource.com/c/1158 实例对照 `<!-- ROW_MINE: ksummit-discuss.messages.350643 -->`

## 76.37 【Linux社区】编码本意澄清

- 【Linux社区】Doug 澄清并非把 Message-Id 写入提交，而是发布脚本剥离本地 Change-Id 用以构造 Message-Id、并保证格式合法，谢 Tglx 与 Ted 指正 RFC-5322 `<!-- ROW_MINE: ksummit-discuss.messages.350644 -->`

## 76.38 【Linux社区】James 附议钩子之痛

- 【Linux社区】2014 档案：James Bottomley 附议 Josh，称被迫在另一台机器跑 commit 钩子，“尤其邮件被配置成从 kernel.org 发出” `<!-- ROW_MINE: ksummit-discuss.messages.350645 -->`

## 76.39 【Linux社区】Tglx 松口 msgid 方案

- 【Linux社区】Tglx 表态“其实不是最坏主意”：只要 RFC 合规没人拦你往 message-id 编信息，make_msgid(ChangeId) 后再加“Link: https://lore.kernel.org/lkml/$id”，社区得链接、Doug 得可 grep 的 ID `<!-- ROW_MINE: ksummit-discuss.messages.350646 -->`

## 76.40 【Linux社区】syzbot 标识困境

- 【Linux社区】Vyukov 详列 syzbot 关联 bug 与修复之难：commit hash 在 linux-next 会变、改动尚未提交时无从指认、LTS 回移植后 hash 不同；改用 commit subject 又有非唯一与回移植加前缀之弊 `<!-- ROW_MINE: ksummit-discuss.messages.350647 -->`

## 76.41 【Linux社区】Link 即 UUID

- 【Linux社区】Tglx 单句定性：“若广泛采用 Link: …/$MSG 标签，你就有了 UUID” `<!-- ROW_MINE: ksummit-discuss.messages.350648 -->`

## 76.42 【Linux社区】LTS 标记与 patch-id

- 【Linux社区】Geert 指出 LTS 提交描述带“commit <sha1> upstream”可解回移植指认，另荐“git patch-id --stable”并称快速查询需定期生成与追加索引 `<!-- ROW_MINE: ksummit-discuss.messages.350650 -->`

## 76.43 【Linux社区】git note 应用流程

- 【Linux社区】Mark Brown 自述应用补丁时把 message-id 等存进 git note，推送并生成“applied, thanks”回信时取用，脚本可回退查 patchwork 但非百发百中且网络开销大增 `<!-- ROW_MINE: ksummit-discuss.messages.350651 -->`

## 76.44 【Linux社区】统一工具缺位质疑

- 【Linux社区】Vyukov 质疑现行工具无法保证人人生成正确 ID 并把规范链接带进提交：各维护者指向不同归档站、Link 亦常指 bug 报告，且链接须由每位开发者在提交前自加 `<!-- ROW_MINE: ksummit-discuss.messages.350652 -->`

## 76.45 【Linux社区】patch-id 局限论

- 【Linux社区】Vyukov 依 git 帮助称 patch-id“处理不了多于一个版本的变更”，且要求维护者提交时不改补丁；未提交状态的变更对一切基于 hash 的方案都难办 `<!-- ROW_MINE: ksummit-discuss.messages.350653 -->`

## 76.46 【Linux社区】gregkh 自动加 Link

- 【Linux社区】Greg 称其子系统已由脚本自动加“指向 lore.kernel.org 含 message id 的 Link:”，并称每年 4000+ 开发者“大事尚难达成一致，何况这类花活” `<!-- ROW_MINE: ksummit-discuss.messages.350654 -->`

## 76.47 【Linux社区】Roeck 模糊匹配之苦

- 【Linux社区】Guenter Roeck 称须综合主题分析、补丁内容模糊字符串比较与描述分析才能答“此补丁上游了吗、上游 SHA 是什么”，有 UUID 标签则一步到位，“疯狂的正是这套分析” `<!-- ROW_MINE: ksummit-discuss.messages.350655 -->`
