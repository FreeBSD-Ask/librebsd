# 71 【Linux社区】commit版本史与lore归档大讨论

> 来源：ksummit-discuss p123（50 封全读，2019-06/07 Patch version changes 大讨论，夹杂 2014-05 档案信）
> 判定：47 CAND / 3 NV。主题分布：git元数据补记提案 1、Sphinx自动链接诉求 1、Corbet已有链接补丁 1、W=1按树选项评估 1、commit版本史议题 1、Luck斥版本史无意义 1、Cook论变更日志取舍 1、Shuah忧日志膨胀 1、维持现状不收版本史 1、cregit作讨论归档 1、syscall文档测试绑定 1、GPIO固件绑定乱象 1、澄清版本史立场 1、版本史改链接提案 1、tglx定型变更格式 1、Link标签自动插入 1、未文档化标签盘点 1、引用节文档化倡议 1、patchwork加链接 1、文档漏lore域名之疑 1、归档重定向沿革 1、media自建实例缘由 1、反对git replace 1、lore等价性澄清 1、承诺改patchwork 1、斥lore界面丑陋 1、驳peterz硬编码说 1、裸msgid链接提案 1、拟为git-am加选项 1、git am可附msgid 1、重定向跨列表之谜 1、任一归档链接即可 1、ACPI索引键困境 1、版本史置于封面信 1、逐补丁变更史之辩 1、双层变更日志主张 1、Link标签不必强制 1、实证跨列表重定向 1、逐补丁评审效率论 1、认跨列表为新功能 1、质疑是否既成惯例 1、主张不入commit 1、投票反对存版本史 1、认可ACPI属性标准化 1、强制Link增负担 1、追问强制之负担 1、TAB选举电子投票 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p123 的逐封提取（47 CAND / 3 NV），全 47 块采用**单行摘要体例**（丙型）：每块由“## 71.x 【Linux社区】题名”与若干“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 71.1 【Linux社区】git元数据补记提案

- Couder 回应 Iwai 的 commit 元数据议题，提议用“git notes”“git replace”给已提交补丁补记事后信息，并预告 replace 将有“--edit”选项。 `<!-- ROW_MINE: ksummit-discuss.messages.350356 -->`

## 71.2 【Linux社区】Sphinx自动链接诉求

- Kees Cook 记录复发性需求：让 Sphinx 自动链接 function() 与结构体名，免写“:c:func:`iounmap()`”式显式标记。 `<!-- ROW_MINE: ksummit-discuss.messages.350357 -->`

## 71.3 【Linux社区】Corbet已有链接补丁

- Corbet 称已有实现自动链接的补丁（2019-04-25 发 linux-doc 列表，附 lwn.net 链接），并承诺“Soon, I promise”尽快收尾。 `<!-- ROW_MINE: ksummit-discuss.messages.350358 -->`

## 71.4 【Linux社区】W=1按树选项评估

- Intel 0-day 的 Philip Li 回应 Dan Carpenter 提议，称可考虑让 kbuild 将 W=1 设为按仓库选项“at least for specific repos”。 `<!-- ROW_MINE: ksummit-discuss.messages.350359 -->`

## 71.5 【Linux社区】commit版本史议题

- Shuah Khan 发起 MAINTAINERS SUMMIT 议题：git 日志近期出现“Changes since”版本信息，成维护者偏好与新趋势，问是否应规范化。 `<!-- ROW_MINE: ksummit-discuss.messages.350360 -->`

## 71.6 【Linux社区】Luck斥版本史无意义

- Tony Luck 断言版本琐碎变更“somewhat pointless”，主张 commit 只记“因 Y 人说 X 方案有 Z 问题而弃用”式实质取舍。 `<!-- ROW_MINE: ksummit-discuss.messages.350361 -->`

## 71.7 【Linux社区】Cook论变更日志取舍

- Kees Cook 称维护者（含自己）想看的是理由与既有思路，“little details tend not to be very important”。 `<!-- ROW_MINE: ksummit-discuss.messages.350362 -->`

## 71.8 【Linux社区】Shuah忧日志膨胀

- Shuah Khan 赞同剔除琐碎变更史，担心不设准则接受版本信息会使 commit 日志越来越长而难读。 `<!-- ROW_MINE: ksummit-discuss.messages.350363 -->`

## 71.9 【Linux社区】维持现状不收版本史

- James Bottomley 定性“向来是多数维护者的政策”不入版本史，怕其脱离语境成干扰、又挤占正题 changelog 更新。 `<!-- ROW_MINE: ksummit-discuss.messages.350364 -->`

## 71.10 【Linux社区】cregit作讨论归档

- Bottomley 举 cregit 项目（cregit.linuxsources.org，数据仅至 4.20）已把邮件讨论指针挂到源码语义单元，主张 changelog 精简、全史查 cregit。 `<!-- ROW_MINE: ksummit-discuss.messages.350366 -->`

## 71.11 【Linux社区】syscall文档测试绑定

- man-pages 维护者 Kerrisk 主张测试用例与文档“hand in glove”，称新 syscall 门槛之争“almost”值得重上 KS 议题。 `<!-- ROW_MINE: ksummit-discuss.messages.350367 -->`

## 71.12 【Linux社区】GPIO固件绑定乱象

- Linus Walleij 举 DT/ACPI GPIO 命名与索引互不兼容实例，指 rfkill-gpio.c 以“RESET 索引0、SHUTDOWN 索引1”双固件统一为正确范例。 `<!-- ROW_MINE: ksummit-discuss.messages.350368 -->`

## 71.13 【Linux社区】澄清版本史立场

- Shuah Khan 披露自己用 cregit 做变更研究，澄清并不主张把版本史写入 commit 日志，要求正式讨论以免其未经思量成惯例。 `<!-- ROW_MINE: ksummit-discuss.messages.350369 -->`

## 71.14 【Linux社区】版本史改链接提案

- Takashi Iwai 提议统一用邮件归档引用 URL 替代 changelog 中的版本变更细节，让读者循链追踪。 `<!-- ROW_MINE: ksummit-discuss.messages.350370 -->`

## 71.15 【Linux社区】tglx定型变更格式

- Thomas Gleixner 提出完整格式：commit 带 lore Link，V(N) 封信链 V(N-1)，版本史置于 --- 分隔符后供工具剥离，并呼吁“make it mandatory”。 `<!-- ROW_MINE: ksummit-discuss.messages.350371 -->`

## 71.16 【Linux社区】Link标签自动插入

- Gleixner 指 Link 标签已存在，其“grab patches from list”脚本自动插入并随 commit 入 git，主张强制化形成修订链。 `<!-- ROW_MINE: ksummit-discuss.messages.350372 -->`

## 71.17 【Linux社区】未文档化标签盘点

- Iwai 指出其用过“Reference”“BugLink”标签均不见文档，建议统一定义推荐标签并规范文档，又问 patchwork 能否直达该 URL。 `<!-- ROW_MINE: ksummit-discuss.messages.350373 -->`

## 71.18 【Linux社区】引用节文档化倡议

- Christian Brauner 赞成 tglx 方案并展示自身实践：commit 末 DCO 前设“References”节列多条 lore 链接，盼写入内核文档。 `<!-- ROW_MINE: ksummit-discuss.messages.350374 -->`

## 71.19 【Linux社区】patchwork加链接

- Mark Brown 建议 patchwork 直接把 lore 链接加进下载的 mbox 与 ack，称现有 message ID 已可构造 LKML 链接。 `<!-- ROW_MINE: ksummit-discuss.messages.350375 -->`

## 71.20 【Linux社区】文档漏lore域名之疑

- Andrea Parri 指出 submitting-patches.rst 只写 lkml.kernel.org 重定向器未提 lore.kernel.org，问文档是否需更新。 `<!-- ROW_MINE: ksummit-discuss.messages.350376 -->`

## 71.21 【Linux社区】归档重定向沿革

- Gleixner 确认“lkml.kernel.org/r was the initial redirector”且该重定向已从 marc.info 切换至 lore。 `<!-- ROW_MINE: ksummit-discuss.messages.350377 -->`

## 71.22 【Linux社区】media自建实例缘由

- Mauro 主张 patchwork 改动须可定制列表 URL，披露 media 用自有实例 patchwork.linuxtv.org，因 kernel.org 早期主镜像不保 ID，且该实例兼管 VDR。 `<!-- ROW_MINE: ksummit-discuss.messages.350378 -->`

## 71.23 【Linux社区】反对git replace

- Jason Cooper 明言不喜欢 git replace 路线、望其默认禁用，并追问历史含替换提交时签名标签 PGP 校验失败属密码学还是逻辑错误。 `<!-- ROW_MINE: ksummit-discuss.messages.350379 -->`

## 71.24 【Linux社区】lore等价性澄清

- lore 维护者 Ryabitsev 确认“lkml.kernel.org == lore.kernel.org in all respects”，r/ 可匹配任何归档列表，偏好 lore 因名不限于 LKML。 `<!-- ROW_MINE: ksummit-discuss.messages.350380 -->`

## 71.25 【Linux社区】承诺改patchwork

- Andrew Donnellan 抄送 patchwork 列表并承诺实现项目级归档前缀并在网页界面暴露；mbox 加链接须独立选项，因同一补丁可经多列表多次入站。 `<!-- ROW_MINE: ksummit-discuss.messages.350381 -->`

## 71.26 【Linux社区】斥lore界面丑陋

- Peter Zijlstra 偏好 lkml.kernel.org/r 因可一键改 marc.info，斥 lore“horrible horrible ugly site”，并以 URL 长度立论。 `<!-- ROW_MINE: ksummit-discuss.messages.350382 -->`

## 71.27 【Linux社区】驳peterz硬编码说

- Gleixner 反驳称 lore 可引用其全部归档列表而 lkml.k.org“hardcoded to lkml”，讥 strlen 论据“Come on”。 `<!-- ROW_MINE: ksummit-discuss.messages.350383 -->`

## 71.28 【Linux社区】裸msgid链接提案

- Iwai 提出若嫌 URL 太长可直接写“Link: <message-id>”形式。 `<!-- ROW_MINE: ksummit-discuss.messages.350384 -->`

## 71.29 【Linux社区】拟为git-am加选项

- Jiri Kosina 称 Link 标签“super-userful”，问 git-am 能否自动生成，否则愿查 git 源码添加选项。 `<!-- ROW_MINE: ksummit-discuss.messages.350385 -->`

## 71.30 【Linux社区】git am可附msgid

- Senozhatsky 解答：“git am -m”会把补丁 Message-ID 附加进 commit 信息（am.messageid 可配默认），但不新生成。 `<!-- ROW_MINE: ksummit-discuss.messages.350386 -->`

## 71.31 【Linux社区】重定向跨列表之谜

- Andrea Parri 举 2019-01 的 ast 补丁讨论未抄 LKML 而 lkml.kernel.org/r 链接仍可用（附链接），请教重定向机制。 `<!-- ROW_MINE: ksummit-discuss.messages.350387 -->`

## 71.32 【Linux社区】任一归档链接即可

- Mark Brown 指出“lore.kernel.org/r/msgid”与列表无关，认为用哪个归档不重要，有链接即可。 `<!-- ROW_MINE: ksummit-discuss.messages.350389 -->`

## 71.33 【Linux社区】ACPI索引键困境

- Wysocki 论证字符串 key 在 ACPI 行不通，acpi_find_gpio() 实际只用索引；直呼直调 of_get_X() 的驱动只得写 of_node/ACPI/“black magic”分支。 `<!-- ROW_MINE: ksummit-discuss.messages.350390 -->`

## 71.34 【Linux社区】版本史置于封面信

- David Howells 称其把 changelog 放封面信（patch 0），因改动常跨多补丁，可由合并者并入合并描述。 `<!-- ROW_MINE: ksummit-discuss.messages.350391 -->`

## 71.35 【Linux社区】逐补丁变更史之辩

- Gleixner 反驳 Howells：版本信息须在补丁内方能显该补丁改动范围，“It's about convenience for the reviewer/maintainer”，直发邮件的系列无合并描述可依。 `<!-- ROW_MINE: ksummit-discuss.messages.350392 -->`

## 71.36 【Linux社区】双层变更日志主张

- Laurent Pinchart 赞成逐补丁 changelog（曾多次要求提交者下移），但自留系列级重要变更概述于封面信以便评审总览。 `<!-- ROW_MINE: ksummit-discuss.messages.350393 -->`

## 71.37 【Linux社区】Link标签不必强制

- James Bottomley 称 Link 标签只是历史档案、cregit 已覆盖历史需求、当时评审者本在邮件串上，对强制化“definitely wouldn't require it”。 `<!-- ROW_MINE: ksummit-discuss.messages.350394 -->`

## 71.38 【Linux社区】实证跨列表重定向

- Steven Rostedt 以 linux-rt-users 列表链接实证 lkml.kernel.org/r 并非仅限 LKML，驳 tglx“hardcoded”说。 `<!-- ROW_MINE: ksummit-discuss.messages.350395 -->`

## 71.39 【Linux社区】逐补丁评审效率论

- Gleixner 图示逐补丁版本史使评审可跳过仅修 typo 的补丁聚焦实质，并称曾因封面信主题微调找旧版“wasting an hour”。 `<!-- ROW_MINE: ksummit-discuss.messages.350396 -->`

## 71.40 【Linux社区】认跨列表为新功能

- Gleixner 以“That must be a recent enhancement”承认 lkml.kernel.org/r 支持非 LKML 列表系新近增强，收束与 Rostedt 之争。 `<!-- ROW_MINE: ksummit-discuss.messages.350397 -->`

## 71.41 【Linux社区】质疑是否既成惯例

- Leon Romanovsky 问 tglx 该格式“isn't it already standard way to write patches with changelogs”，暗指 git 时代以来已通行。 `<!-- ROW_MINE: ksummit-discuss.messages.350398 -->`

## 71.42 【Linux社区】主张不入commit

- Geert Uytterhoeven 澄清争论在于 changelog 是否入 git 史，主张“doesn't matter for eternity”者不进 commit 描述，重要取舍写进补丁正文。 `<!-- ROW_MINE: ksummit-discuss.messages.350399 -->`

## 71.43 【Linux社区】投票反对存版本史

- Leon Romanovsky 明言“I'll vote against storing changelogs in git”，却盛赞 git am 自动加“Link:”标签的想法极具价值。 `<!-- ROW_MINE: ksummit-discuss.messages.350400 -->`

## 71.44 【Linux社区】认可ACPI属性标准化

- Rafael 认同 Darren Hart 所述 ACPI 下 _DSM 与命名对象泛滥、板级文件回潮，需 ACPI 标准属性机制以省重复代码，称“I obviously agree”。 `<!-- ROW_MINE: ksummit-discuss.messages.350401 -->`

## 71.45 【Linux社区】强制Link增负担

- Bottomley 不反对 --- 之下的逐补丁 changelog 且视为评审最佳实践，但称强制 Link 会给无收益的子系统添执法负担，可为可选项。 `<!-- ROW_MINE: ksummit-discuss.messages.350402 -->`

## 71.46 【Linux社区】追问强制之负担

- Gleixner 质询“What's the burden exactly”，称现用者皆以自写脚本自动加链，并入 git 或 patchwork 并非难事。 `<!-- ROW_MINE: ksummit-discuss.messages.350403 -->`

## 71.47 【Linux社区】TAB选举电子投票

- Laura Abbott 代表 TAB 公告 2019 选举改用康奈尔 CIVS 电子投票与 Condorcet-IRV 排序制，投票池为 Plumbers 注册者，先演练、失败则回纸票。 `<!-- ROW_MINE: ksummit-discuss.messages.350404 -->`
