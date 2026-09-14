# 72 【Linux社区】Link标签强制与git元数据终局

> 来源：ksummit-discuss p124（50 封全读，2019-07 补丁版本变更入 commit log 终局+stable 议题，夹杂 2014-05 档案信）
> 判定：48 CAND / 2 NV。主题分布：强制Link标签负担之争 1、提议git归档msgid 1、Link落地两步方案 1、归纳两项可行动作 1、git-am自动元数据 1、大系列才有价值论断 1、逻辑电源域扩展构想 1、偏好git原生记录 1、力挺git内建方案 1、lore收录捐赠渠道 1、列表归档映射设计 1、lorifier工具推荐 1、git已藏msgid功能 1、拒绝Message-ID 1、git上游难改兼容论 1、四步hook转换方案 1、Link标签沿革考 1、replace机制释疑 1、tglx背书Ted方案 1、正文元数据观察 1、有损映射钩子探 1、log端转换可行论 1、mbox转quilt流程 1、lore/r/免列表辨识 1、lore缺档404实证 1、贴出hook转换脚本 1、stable流程改进议题 1、pm域单一归属限制 1、TAB投票改革背书 1、全量纳入lore主张 1、msgid普适检索论 1、Greg采纳hook承诺 1、自写补丁回取质疑 1、恒从列表重做主张 1、rdma分支回灌实践 1、Link价值有限论 1、回溯移植查询需求 1、追加归档即修复论 1、QR议题提名补记 1、无条件加链成本论 1、全链优于摘要论 1、DRMdim强制先例 1、rebase版本史实践 1、Gmail脚本取补流程 1、Cc标签冗余之辩 1、盲抄Cc表之弊 1、tglx让步Cc冗余 1、Cc移线下机制提案 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p124 的逐封提取（48 CAND / 2 NV），全 48 块采用**单行摘要体例**（丙型）：每块由“## 72.x 【Linux社区】题名”与若干“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 72.1 【Linux社区】强制Link标签负担之争

- 【Linux社区】Bottomley 称多数邮件工具不显示 msgid、不少归档会损毁 msgid，且“linux-scsi isn't currently on lore”，故 Link 标签可接受为可选但不应强制，自动化即可免强制。 `<!-- ROW_MINE: ksummit-discuss.messages.350406 -->`

## 72.2 【Linux社区】提议git归档msgid

- 【Linux社区】Bottomley 提出可行动作：让 git 在提交时归档补丁 msgid，供脚本回溯补丁系列及其前身版本。 `<!-- ROW_MINE: ksummit-discuss.messages.350407 -->`

## 72.3 【Linux社区】Link落地两步方案

- 【Linux社区】tglx 分两层规划：提交内 Link 标签由应用补丁的维护者借 git/patchwork 工具补齐；封面信引导 msgid 链接靠文档教育，并称其 mbox 转 quilt 转换器已自动插入 Link。 `<!-- ROW_MINE: ksummit-discuss.messages.350408 -->`

## 72.4 【Linux社区】归纳两项可行动作

- 【Linux社区】Shuah Khan 将议题收敛为两项：改动史信息酌情入提交说明（--- 线下）并或更新提交指南文档；归档提交 msgid 需脚本辅助，二者并行不悖。 `<!-- ROW_MINE: ksummit-discuss.messages.350409 -->`

## 72.5 【Linux社区】git-am自动元数据

- 【Linux社区】Bottomley 同意提交内链标签可全工具化零手工，主张“engage the git people”使其成为 git-am 处理提交的自动元数据；封面信链接“optional but recommended”即可。 `<!-- ROW_MINE: ksummit-discuss.messages.350410 -->`

## 72.6 【Linux社区】大系列才有价值论断

- 【Linux社区】tglx 回应称不担心 drive-by 补丁缺失链接，“It mostly matters for larger patch series”——链接主要对大补丁系列有意义。 `<!-- ROW_MINE: ksummit-discuss.messages.350411 -->`

## 72.7 【Linux社区】逻辑电源域扩展构想

- 【Linux社区】2014 档案信：Shuah Khan 提议把 PM 域扩展为支持逻辑分组与依赖排序，以媒体 USB 设备为例，主驱动建域、其余驱动声明依赖并用 save_state/restore_state。 `<!-- ROW_MINE: ksummit-discuss.messages.350412 -->`

## 72.8 【Linux社区】偏好git原生记录

- 【Linux社区】Bottomley 主张“make git do it”：Message-Id 进 git 可选元数据优于各装 commit hook，但承认生态传导需数年；并认可版本信息置于 --- 永久史截断线下。 `<!-- ROW_MINE: ksummit-discuss.messages.350413 -->`

## 72.9 【Linux社区】力挺git内建方案

- 【Linux社区】Shuah Khan 明确“having git do it is better way to go”，内建即成工作流一部分，免去再教育开发者额外脚本与流程。 `<!-- ROW_MINE: ksummit-discuss.messages.350414 -->`

## 72.10 【Linux社区】lore收录捐赠渠道

- 【Linux社区】Jiri Kosina 称把邮件列表加入 lore “is trivial”，已有合理格式档案还可捐赠补录，给出 korg.wiki 的 collecting_archive_donations 文档链接。 `<!-- ROW_MINE: ksummit-discuss.messages.350415 -->`

## 72.11 【Linux社区】列表归档映射设计

- 【Linux社区】Kees Cook 提议通用映射 list_email→archive_url：To/Cc 含列表地址时 git am 即插入归档链接，例 linux-kernel@vger.kernel.org→https://lkml.kernel.org/r/%s。 `<!-- ROW_MINE: ksummit-discuss.messages.350416 -->`

## 72.12 【Linux社区】lorifier工具推荐

- 【Linux社区】lore 负责人 Konstantin Ryabitsev 推荐 mutt 用户用 danrue 的 lorifier 工具，自动为来自 lore 归档列表的每封信显示规范链接。 `<!-- ROW_MINE: ksummit-discuss.messages.350417 -->`

## 72.13 【Linux社区】git已藏msgid功能

- 【Linux社区】Bottomley 披露 git 自 2014-11-25 Paolo Bonzini 提交 a078f732（--message-id，自 2.3.0）已可捕获 msgid，写入 Message-ID: 标签，当时未写入文档。 `<!-- ROW_MINE: ksummit-discuss.messages.350418 -->`

## 72.14 【Linux社区】拒绝Message-ID

- 【Linux社区】tglx 复“Please no”：因 git 有未文档化功能就放行 Message-ID 会开门揖盗，助长五花八门的变体标签，“The 'Link:' tag is documented and proven to be useful”。 `<!-- ROW_MINE: ksummit-discuss.messages.350419 -->`

## 72.15 【Linux社区】git上游难改兼容论

- 【Linux社区】Bottomley 称 git 2014 年即有该功能，五年后要求上游换格式将是“singularly unsuccessful”；支持 Kees 配置项思路，让 Message-Id 可转成任意 Link 形式。 `<!-- ROW_MINE: ksummit-discuss.messages.350420 -->`

## 72.16 【Linux社区】四步hook转换方案

- 【Linux社区】Ted Ts'o 提四步免改 git 方案：am.messageid=true、applypatch-msg 钩子把 Message-Id 变 Link trailer（lore 模板）、写入 Documentation/process、“Step 4) Profit”。 `<!-- ROW_MINE: ksummit-discuss.messages.350421 -->`

## 72.17 【Linux社区】Link标签沿革考

- 【Linux社区】tglx 述史：十余年前 LKML-Reference: 令 Linus 不满而明示要真链接，2011 年改定 Link: 并为此建 lkml.kernel.org/r/，2014 年 git 该改动作者对此知情。 `<!-- ROW_MINE: ksummit-discuss.messages.350422 -->`

## 72.18 【Linux社区】replace机制释疑

- 【Linux社区】2014 档案信：Christian Couder 释疑 git replace 默认不 fetch/push、可用 GIT_NO_REPLACE_OBJECTS 规避，并论及签名校验与替换对象的风险边界。 `<!-- ROW_MINE: ksummit-discuss.messages.350423 -->`

## 72.19 【Linux社区】tglx背书Ted方案

- 【Linux社区】tglx 复“Amen.”，明确支持 Ted 的钩子转换四步方案，了结对 Bottomley 沿用 git Message-ID 路线的“Please no”之争。 `<!-- ROW_MINE: ksummit-discuss.messages.350424 -->`

## 72.20 【Linux社区】正文元数据观察

- 【Linux社区】Bottomley 指出 Ted 方案中间环节可省——tglx 已有钩子可从邮件直取 Message-Id 转 Link；新信息是 git 把 msgid 写入正文而非元数据，提交流里直接可见。 `<!-- ROW_MINE: ksummit-discuss.messages.350425 -->`

## 72.21 【Linux社区】有损映射钩子探

- 【Linux社区】Kees Cook 指出 am.messageid 有损——不知 msgid 来自哪个列表；又称 lorifier.py 已含“90% of the step 2”逻辑，并疑 applypatch-msg 钩子里邮件头已被剥除。 `<!-- ROW_MINE: ksummit-discuss.messages.350426 -->`

## 72.22 【Linux社区】log端转换可行论

- 【Linux社区】Bottomley 称新配置项须先过上游，但现可脚本化：git log 即可把 Message-Id 转成任意格式 Link；若上游接受 log 端转换，commit 端亦应可行。 `<!-- ROW_MINE: ksummit-discuss.messages.350427 -->`

## 72.23 【Linux社区】mbox转quilt流程

- 【Linux社区】tglx 详述自身流程：mbox 转 quilt 系列、从回帖拾取标签、git quiltimport 推出；允诺改造成 git-am 前置工具，并称 Ted 方案一次配置更省事。 `<!-- ROW_MINE: ksummit-discuss.messages.350428 -->`

## 72.24 【Linux社区】lore/r/免列表辨识

- 【Linux社区】Ted Ts'o 指出 lore.kernel.org/r/<message-id> 无需知道消息来自哪个列表即可用，并引文档断定 applypatch-msg 阶段邮件头已剥离，靠 am.messageid 写进正文可行。 `<!-- ROW_MINE: ksummit-discuss.messages.350429 -->`

## 72.25 【Linux社区】lore缺档404实证

- 【Linux社区】Bottomley 给出实例：其 2019-05 linux-scsi 信件 msgid 在 lore /r/ 返回 404，同一 msgid 在 marc.info 可用，证明未收录列表的链接失效风险。 `<!-- ROW_MINE: ksummit-discuss.messages.350431 -->`

## 72.26 【Linux社区】贴出hook转换脚本

- 【Linux社区】Kees Cook 贴出验证可用的脚本：git config am.messageid true 加 perl 单行把 Message-Id 改写为“Link: https://lore.kernel.org/r/$1”并转交 commit-msg。 `<!-- ROW_MINE: ksummit-discuss.messages.350432 -->`

## 72.27 【Linux社区】stable流程改进议题

- 【Linux社区】Sasha Levin 提 2019 维护者峰会议题：stable 流程自动化与改进，列去年痛点：作者不回“FAILED:”致丢提交、测试充分性、“fixes for fixes”漏收、AUTOSEL 更合理、丢弃跟踪。 `<!-- ROW_MINE: ksummit-discuss.messages.350433 -->`

## 72.28 【Linux社区】pm域单一归属限制

- 【Linux社区】2014 档案信：Geert 区分物理/逻辑/时钟电源域（pm_clk_notify），指出设备经 struct device.pm_domain 指针只能属一个域，问能否仿 RPM_GET_CALLBACK 栈扩展多重归属。 `<!-- ROW_MINE: ksummit-discuss.messages.350434 -->`

## 72.29 【Linux社区】TAB投票改革背书

- 【Linux社区】Matthew Wilcox 赞成 2019 TAB 选举改 CIVS 电子投票：自称现行制“originator”、原为会场举手设计且无法防重复投票，Condorcet 更优，缺席者可投票提升合法性。 `<!-- ROW_MINE: ksummit-discuss.messages.350435 -->`

## 72.30 【Linux社区】全量纳入lore主张

- 【Linux社区】Ted Ts'o 主张彻底解法是把全部内核邮件列表纳入 lore.kernel.org，裸 Message-Id 不足以解决 marc.info 之外的缺档问题。 `<!-- ROW_MINE: ksummit-discuss.messages.350436 -->`

## 72.31 【Linux社区】msgid普适检索论

- 【Linux社区】Bottomley 称 message-id 更具描述性，可喂给任何归档甚至 google 检索；仅弱反对纯 URL 方案——链接应可用，而总有补丁尚未入档。 `<!-- ROW_MINE: ksummit-discuss.messages.350437 -->`

## 72.32 【Linux社区】Greg采纳hook承诺

- 【Linux社区】Greg KH 实测 Kees 的钩子“works great!”，宣布将在自己的树上启用，并称这迫使自己“finally get the linux-usb tree into lore”。 `<!-- ROW_MINE: ksummit-discuss.messages.350438 -->`

## 72.33 【Linux社区】自写补丁回取质疑

- 【Linux社区】Laurent Pinchart 提工作流缺口：PR 作者自写补丁通常不从列表取回再发 PR，是否要走向维护者一律从列表或 patchwork 取补的模式？ `<!-- ROW_MINE: ksummit-discuss.messages.350439 -->`

## 72.34 【Linux社区】恒从列表重做主张

- 【Linux社区】tglx 答“Yes.”：只 commit 后发 PR 会丢 Reviewed-by/Acked-by/Tested-by 或需重做提交，恒从 mail/patchwork 重做统一工作流，自己整线程存 mbox 由工具处理。 `<!-- ROW_MINE: ksummit-discuss.messages.350440 -->`

## 72.35 【Linux社区】rdma分支回灌实践

- 【Linux社区】Leon Romanovsky 为确证“posted and reviewed patch equal to applied”，把自己的补丁经列表回灌到共享 rdma<->netdev 分支再应用。 `<!-- ROW_MINE: ksummit-discuss.messages.350441 -->`

## 72.36 【Linux社区】Link价值有限论

- 【Linux社区】Ted 自称“(Unpopular Puffin)”：99% 时间标签价值有限，拼写与编译警告类补丁无讨论可链；要链就配说明文字指向封面信，“technological solution to a social problem”。 `<!-- ROW_MINE: ksummit-discuss.messages.350442 -->`

## 72.37 【Linux社区】回溯移植查询需求

- 【Linux社区】Jan Kara 愿忍受多数无用的 Link：自己多次追列表找补丁最新版与同系列其余补丁以便一并回溯移植，Link 有助此甚至可自动化。 `<!-- ROW_MINE: ksummit-discuss.messages.350443 -->`

## 72.38 【Linux社区】追加归档即修复论

- 【Linux社区】Kees Cook 称 lore 方案是“one-time retro-active fix”：发现缺列表随时补录，引用该列表 msgid 的所有链接即刻生效。 `<!-- ROW_MINE: ksummit-discuss.messages.350444 -->`

## 72.39 【Linux社区】QR议题提名补记

- 【Linux社区】2014 档案信：Teodora Băluţă 为 QR/error reporting 专题补记提名人，称 QR 创意属 Dirk Hohndel 与 Peter Anvin，并列 PJ Waskiewicz、Konstantin Ryabitsev 等相关讨论者。 `<!-- ROW_MINE: ksummit-discuss.messages.350445 -->`

## 72.40 【Linux社区】无条件加链成本论

- 【Linux社区】Mark Brown：若能自动生成则 Link 不加白不加——“more effort to decide if it's useful than it is to just add it unconditionally”。 `<!-- ROW_MINE: ksummit-discuss.messages.350447 -->`

## 72.41 【Linux社区】全链优于摘要论

- 【Linux社区】Frank Rowand 宁要讨论全文链接不要人工摘要：写摘要者无法预知何细节对“five years later”的研究者是关键。 `<!-- ROW_MINE: ksummit-discuss.messages.350448 -->`

## 72.42 【Linux社区】DRMdim强制先例

- 【Linux社区】Laurent Pinchart 披露 DRM 子系统经 drm-misc 维护工具 dim 强制使用 Link: 标签；提议把回取补丁写成正式文档建议，并拟写脚本自动识别并回取补丁系列。 `<!-- ROW_MINE: ksummit-discuss.messages.350449 -->`

## 72.43 【Linux社区】rebase版本史实践

- 【Linux社区】Bottomley 自述恒从列表应用补丁：用 rebase 把版本信息累积在 --- 线下以便直接发信，从列表 am 应用是版本史不随补丁入树的唯一环节。 `<!-- ROW_MINE: ksummit-discuss.messages.350450 -->`

## 72.44 【Linux社区】Gmail脚本取补流程

- 【Linux社区】Geert 自述 cherry-pick 自开发分支、rebase -i 补 Reviewed-by；以自定义脚本按 Message-ID 从 Gmail 备份抽取补丁——自称可在该环节自动加 Link。 `<!-- ROW_MINE: ksummit-discuss.messages.350451 -->`

## 72.45 【Linux社区】Cc标签冗余之辩

- 【Linux社区】Michael Ellerman 质疑既有 Link 还需 Cc: 吗——Cc 只说明“didn't have time to review”，并举 tglx x86/stacktrace 提交（3599fe12）约三十行 Cc 为例。 `<!-- ROW_MINE: ksummit-discuss.messages.350452 -->`

## 72.46 【Linux社区】盲抄Cc表之弊

- 【Linux社区】Geert 附议 +1：尤其当 Cc 列表由 get_maintainer.pl 输出未经“common sense filter”盲抄生成时更无价值。 `<!-- ROW_MINE: ksummit-discuss.messages.350453 -->`

## 72.47 【Linux社区】tglx让步Cc冗余

- 【Linux社区】tglx 复“Probably not.”并调侃“And the maintainer then blindly picks it up”，就其本人被引提交默认 Cc 标签大概不必保留。 `<!-- ROW_MINE: ksummit-discuss.messages.350454 -->`

## 72.48 【Linux社区】Cc移线下机制提案

- 【Linux社区】Bottomley 定性 Cc: 为“git artefact”无内在历史价值，提议新惯例：全部 Cc 置于截断线下、cc: stable 等必要者留线上，git-am 时随线下内容清除。 `<!-- ROW_MINE: ksummit-discuss.messages.350455 -->`
