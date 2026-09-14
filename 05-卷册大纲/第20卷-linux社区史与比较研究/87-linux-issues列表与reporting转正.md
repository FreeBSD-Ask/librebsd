# 87 【Linux社区】linux-issues列表与reporting转正

> 来源：ksummit-discuss p139（50 封全读，2020-12 折叠修复署名+2021-03 linux-issues 列表与 reporting-issues 文档转正，夹杂 2014 档案信）
> 判定：47 CAND / 3 NV。主题分布：预生产驱动门控之争 1、折叠修复署名之争 1、署名标签堆叠之弊 1、lore透明日志归档提案 1、归档方案与notes取舍 1、折叠原则与Link足矣 1、补丁迭代与评审计量 1、反对固定署名规则 1、Adjusted-by标签提案 1、新标签命名与价值质疑 1、Fixes-from标签主张 1、Mason驳btrfs上游论 1、折叠场景Reported歧义 1、Postel定律宽放标签 1、折叠评论致谢标签 1、stable回移定署名标准 1、Reported-by现状辩护 1、linux-issues列表提案 1、issue定义之问 1、lore统一检索预告 1、在此即bug报告定位 1、Linus属意回归列表 1、staging拖慢开发论 1、s:Bug主题词检索 1、改主题不如CC列表 1、bugtracker转feed方案 1、回归列表覆盖之辩 1、issue范围圈定 1、结构化报告表提议 1、报告去向定位构想 1、kdevops公开基线 1、bugzilla首页引流提示 1、用户问题多为回归论 1、no-rebase修复分散论 1、虚拟回归列表构想 1、回归占比因人而异 1、reporting-issues宜转正 1、文档转正待办清单 1、拒绝过度承诺表态 1、lei标签与JMAP规划 1、文档转正RFC公告 1、转正文[1/5]TLDR 1、转正文[2/5]步骤指南 1、PM依赖IOMMU相机争锋 1、转正文[4/5]stable参考 1、转正文[5/5]附录释因 1、转正文[3a/5]参考主节 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p139（实锚 pk 351156-351205）的逐封提取（47 CAND / 3 NV），全 47 块采用**单行摘要体例**（丙型）：每块由“## 87.x 【Linux社区】题名”与若干“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 87.1 【Linux社区】预生产驱动门控之争

- 【Linux社区】Dan Williams 2014 转引 Dave Chinner 论断 btrfs 合入主线“reduces the speed”，警示合入实验易向用户“leaking promises”不欲兑现的承诺。 `<!-- ROW_MINE: ksummit-discuss.messages.351156 -->`

## 87.2 【Linux社区】折叠修复署名之争

- 【Linux社区】Wilcox 称诉求非“clean history”而是“don't leave landmines for git bisect”，回应 Bottomley 的干净历史论。 `<!-- ROW_MINE: ksummit-discuss.messages.351157 -->`

## 87.3 【Linux社区】署名标签堆叠之弊

- 【Linux社区】Leon 举 commit 71cc849b7093（KVM split-irqchip）需“Reported-Analyzed-Reviewed-Tested-by:”，指“Reviewed-Signed-by:”令人误以为他人合码未审。 `<!-- ROW_MINE: ksummit-discuss.messages.351158 -->`

## 87.4 【Linux社区】lore透明日志归档提案

- 【Linux社区】Konstantin 提议 kernel.org 将 PR 拆解入 public-inbox 透明日志，并抓取 commit 内 Link:/Message-Id: 线程存档以求 lore 失效后可重建。 `<!-- ROW_MINE: ksummit-discuss.messages.351159 -->`

## 87.5 【Linux社区】归档方案与notes取舍

- 【Linux社区】Perches 认同透明日志方案并称届时新增 -by 签名标签“become unnecessary”，建议 pull 时标准抓取 refs/notes。 `<!-- ROW_MINE: ksummit-discuss.messages.351160 -->`

## 87.6 【Linux社区】折叠原则与Link足矣

- 【Linux社区】Bottomley 同意破坏构建/bisect 的评审反馈应折叠，坚持“I fall back to my link is enough”，并指只跟踪次要以增偏倚。 `<!-- ROW_MINE: ksummit-discuss.messages.351161 -->`

## 87.7 【Linux社区】补丁迭代与评审计量

- 【Linux社区】Bottomley 追问 v2→v3 换 msgid 后如何取全历史，建议把“被接受补丁的回复数”计入 reviewer 统计并为此 cc Jon。 `<!-- ROW_MINE: ksummit-discuss.messages.351162 -->`

## 87.8 【Linux社区】反对固定署名规则

- 【Linux社区】Ts'o 四点反对成文规则：msgid 罗列膨胀、trivial 无需署名、维护者裁量、固定规则致“counting attributions”被灌水游戏化。 `<!-- ROW_MINE: ksummit-discuss.messages.351163 -->`

## 87.9 【Linux社区】Adjusted-by标签提案

- 【Linux社区】Kees Cook 提议“Adjusted-by”致谢 Colin Ian King、Dan Carpenter 类“tiny fix”，另列 Tweaked-by/Helped-by/Corrected-by 备选。 `<!-- ROW_MINE: ksummit-discuss.messages.351164 -->`

## 87.10 【Linux社区】新标签命名与价值质疑

- 【Linux社区】Perches 补“Improved-by:/Enhanced-by:/Revisions-by:”并质询这些标签“what actual value these things have and to whom”。 `<!-- ROW_MINE: ksummit-discuss.messages.351165 -->`

## 87.11 【Linux社区】Fixes-from标签主张

- 【Linux社区】Dan Carpenter 称只给修复记功“Complaining about style is its own reward”，重申多年主张 Fixes-from: 标签并引 zero day bot 惯例。 `<!-- ROW_MINE: ksummit-discuss.messages.351166 -->`

## 87.12 【Linux社区】Mason驳btrfs上游论

- 【Linux社区】Chris Mason 2014 反驳 Chinner：提前上游化“increases community ownership”并减少私有代码孤岛，btrfs 有瑕仍是 Linux 文件系统。 `<!-- ROW_MINE: ksummit-discuss.messages.351167 -->`

## 87.13 【Linux社区】折叠场景Reported歧义

- 【Linux社区】Babka 支持标准化 Fixes-from:，指折叠后 Reported-by 语义不清，另提“Fixes-reported-by:”以同前缀消歧。 `<!-- ROW_MINE: ksummit-discuss.messages.351168 -->`

## 87.14 【Linux社区】Postel定律宽放标签

- 【Linux社区】Perches 主张让人自造 <whatever>-by: 标签（“Postel's law”），逻辑/缺陷削减改进应记名而风格意见不记。 `<!-- ROW_MINE: ksummit-discuss.messages.351169 -->`

## 87.15 【Linux社区】折叠评论致谢标签

- 【Linux社区】Geert 提议“Taken-into-account-comments-from:”类标签致谢折叠评论，并问有无更简英文词。 `<!-- ROW_MINE: ksummit-discuss.messages.351170 -->`

## 87.16 【Linux社区】stable回移定署名标准

- 【Linux社区】Carpenter 提议以“Would this fix be backported to stable?”为界，举 signedness 两修法与 commit f026d8ca2904（igc 自测）实例。 `<!-- ROW_MINE: ksummit-discuss.messages.351171 -->`

## 87.17 【Linux社区】Reported-by现状辩护

- 【Linux社区】Dan Williams 称 kbuild robot 与其子系统已用 Reported-by 记 fixup，“I fail to perceive a benefit”再分化标签。 `<!-- ROW_MINE: ksummit-discuss.messages.351172 -->`

## 87.18 【Linux社区】linux-issues列表提案

- 【Linux社区】Leemhuis 提议 linux-issues@lists.linux.dev 集中 bug/回归检索，忆 2017 维护者峰会决议（LWN 738216）与 linux-regressions@vger 未竟请求。 `<!-- ROW_MINE: ksummit-discuss.messages.351173 -->`

## 87.19 【Linux社区】issue定义之问

- 【Linux社区】Bulwahn 支持倡议但追问定义边界：linux-next 警告、kernel test robot、kernelci 汇总、syzbot 报告是否算 issue。 `<!-- ROW_MINE: ksummit-discuss.messages.351174 -->`

## 87.20 【Linux社区】lore统一检索预告

- 【Linux社区】Konstantin 预告 public-inbox 全源统一检索与查询式订阅（按文件/函数/设备名入收件箱），并拟接 bugzilla.kernel.org 变更 feed。 `<!-- ROW_MINE: ksummit-discuss.messages.351175 -->`

## 87.21 【Linux社区】在此即bug报告定位

- 【Linux社区】Bottomley 主张列表核心价值是“if it's on here, it's a bug report”，triage 团队分派并请维护者补 cc。 `<!-- ROW_MINE: ksummit-discuss.messages.351176 -->`

## 87.22 【Linux社区】Linus属意回归列表

- 【Linux社区】Torvalds 称更取“linux-regressions”之名因其更聚焦，“The more clear-cut the list is, the better”。 `<!-- ROW_MINE: ksummit-discuss.messages.351177 -->`

## 87.23 【Linux社区】staging拖慢开发论

- 【Linux社区】Dan Carpenter 2014 称 staging“in many cases it is a slow down”，主张开发者“better off just working like mad”在树外修好再进树。 `<!-- ROW_MINE: ksummit-discuss.messages.351178 -->`

## 87.24 【Linux社区】s:Bug主题词检索

- 【Linux社区】Eric Wong 展示 lore 现可用“s:Regression”/“s:Bug”按主题词快速查询 bug 报告并给出查询 URL。 `<!-- ROW_MINE: ksummit-discuss.messages.351179 -->`

## 87.25 【Linux社区】改主题不如CC列表

- 【Linux社区】Leemhuis 称改 Subject 不合日常习惯而“adding people and appropriate mailing lists to the CC”是日常，仍主独立列表并接受标签共识。 `<!-- ROW_MINE: ksummit-discuss.messages.351180 -->`

## 87.26 【Linux社区】bugtracker转feed方案

- 【Linux社区】Konstantin 答复：凡可轮询的 API（含 drm 的 gitlab）皆可转成 public-inbox RFC2822 消息入库供索引查询，同 bugzilla 计划。 `<!-- ROW_MINE: ksummit-discuss.messages.351181 -->`

## 87.27 【Linux社区】回归列表覆盖之辩

- 【Linux社区】Leemhuis 向 Linus 解释 linux-regressions 只解一半问题：用户仍无从查非回归既有报告（曾用/从未用过皆不知）。 `<!-- ROW_MINE: ksummit-discuss.messages.351182 -->`

## 87.28 【Linux社区】issue范围圈定

- 【Linux社区】Leemhuis 答 Bulwahn：robot 报告仅回归类收，CI/机器人报告因噪声暂排除，圈定面向单人用户报告为佳策略。 `<!-- ROW_MINE: ksummit-discuss.messages.351183 -->`

## 87.29 【Linux社区】结构化报告表提议

- 【Linux社区】Ts'o 建议用户填表式报告便于结构化/解析/提醒硬件配置，正文放“LINUX KERNEL BUG REPORTER TEMPLATE”标识利 lore 检索。 `<!-- ROW_MINE: ksummit-discuss.messages.351184 -->`

## 87.30 【Linux社区】报告去向定位构想

- 【Linux社区】Leemhuis 喜纳填表建议，拟先等 reporting-issues.rst 转正再做脚本/网页助解码 MAINTAINERS 定报告去向，称此事对老手亦难。 `<!-- ROW_MINE: ksummit-discuss.messages.351185 -->`

## 87.31 【Linux社区】kdevops公开基线

- 【Linux社区】Luis Chamberlain 展示 failures.txt 记 korg#212305 失败率 1/669，定“steady state goal”（blktests 1000、fstests 100），倡 OpenSUSE 公开发行版基线。 `<!-- ROW_MINE: ksummit-discuss.messages.351186 -->`

## 87.32 【Linux社区】bugzilla首页引流提示

- 【Linux社区】Konstantin 称已在 bugzilla.kernel.org 首页加醒目提示引导用户先走 distro tracker，并荐 git 项目 git-bugreport 工具可仿。 `<!-- ROW_MINE: ksummit-discuss.messages.351187 -->`

## 87.33 【Linux社区】用户问题多为回归论

- 【Linux社区】Rostedt 以旧 distro 测试机（fedora 13）经验断言“bulk of user issues are going to be regressions”，表态支持 linux-regressions 列表。 `<!-- ROW_MINE: ksummit-discuss.messages.351188 -->`

## 87.34 【Linux社区】no-rebase修复分散论

- 【Linux社区】Geert 2014 反驳 Carpenter：因“no rebase”规则等，修复多已作独立 commit 落各子系统树而非重做整系列。 `<!-- ROW_MINE: ksummit-discuss.messages.351189 -->`

## 87.35 【Linux社区】虚拟回归列表构想

- 【Linux社区】Bottomley 提用 public-inbox 虚拟列表按 imap 标志聚合 lore 全索引范围内被标回归的信件以兼得两全。 `<!-- ROW_MINE: ksummit-discuss.messages.351190 -->`

## 87.36 【Linux社区】回归占比因人而异

- 【Linux社区】Ts'o 以 ext4 大量 Ubuntu 16.04 内核“bug reports”为例指占比取决于用户与子系统，倡更重宣传 reporting-issues 文档。 `<!-- ROW_MINE: ksummit-discuss.messages.351191 -->`

## 87.37 【Linux社区】reporting-issues宜转正

- 【Linux社区】Ts'o 评新文档“strictly better than the older reporting-bugs doc”，主张既已链自 bugzilla 首页即应即刻官方化并在 kernel.org 加链接。 `<!-- ROW_MINE: ksummit-discuss.messages.351192 -->`

## 87.38 【Linux社区】文档转正待办清单

- 【Linux社区】Leemhuis 列四步：patchset 先合入、请 Greg/Sasha 稳定视角审、清 bugzilla 与 CC LKML 两 FIXME、删 WIP 框并除 reporting-bugs.rst。 `<!-- ROW_MINE: ksummit-discuss.messages.351193 -->`

## 87.39 【Linux社区】拒绝过度承诺表态

- 【Linux社区】Konstantin 拒就虚拟列表站队：“for the fear of over-promising”，并区分公开 lore 服务/kernel.org 账户/开发者本地三档。 `<!-- ROW_MINE: ksummit-discuss.messages.351195 -->`

## 87.40 【Linux社区】lei标签与JMAP规划

- 【Linux社区】Eric Wong 详述 lei 数据模型“labels”（JMAP 术语）与静态 HTML/Atom/JSON feed 发布、读写 JMAP 及虚拟用户系统设想。 `<!-- ROW_MINE: ksummit-discuss.messages.351196 -->`

## 87.41 【Linux社区】文档转正RFC公告

- 【Linux社区】Leemhuis 宣告下个合并窗删 reporting-bugs.rst 并去 WIP 框转正，要点含“always CC LKML”、vanilla mainline 优先、linux-regressions 列表将申请创建。 `<!-- ROW_MINE: ksummit-discuss.messages.351197 -->`

## 87.42 【Linux社区】转正文[1/5]TLDR

- 【Linux社区】转正评审贴出 reporting-issues.rst 第 1/5 段：TL;DR 含分立报告、bisect 找回归 commit、每个 rc1 回访附状态更新等流程。 `<!-- ROW_MINE: ksummit-discuss.messages.351198 -->`

## 87.43 【Linux社区】转正文[2/5]步骤指南

- 【Linux社区】第 2/5 段 step-by-step 指南：vendor 内核先找 vendor、5.10.4→5.10.5 型 stable 回归走简报流程、高优先级议题特殊处理。 `<!-- ROW_MINE: ksummit-discuss.messages.351199 -->`

## 87.44 【Linux社区】PM依赖IOMMU相机争锋

- 【Linux社区】Laurent Pinchart 2014 答 Kevin Hilman：DMA mapping API 非 request-based 故 IOMMU 取电难，举 OMAP3 ISP/传感器恢复次序例，主张 sensor 经 clocks 属性取钟。 `<!-- ROW_MINE: ksummit-discuss.messages.351200 -->`

## 87.45 【Linux社区】转正文[4/5]stable参考

- 【Linux社区】第 4/5 段参考章节：stable tag“Cc: <stable@vger.kernel.org> # 5.4+”通常两周内回移、以 5.10.5-5.10.9 为例手工粗 bisect 定位引入版。 `<!-- ROW_MINE: ksummit-discuss.messages.351201 -->`

## 87.46 【Linux社区】转正文[5/5]附录释因

- 【Linux社区】第 5/5 段释因部分报告无响应：业余维护者自愿不可强求、硬件文档缺失、弃养驱动留树防回归、付费开发者亦会弃码或设优先级。 `<!-- ROW_MINE: ksummit-discuss.messages.351202 -->`

## 87.47 【Linux社区】转正文[3a/5]参考主节

- 【Linux社区】第 3a/5 段（Part 3 因超限拆半）：vendor 内核受理差异（Debian Sid/Fedora Rawhide、Arch/Tumbleweed）、清除 DKMS/akmods、taint 三因排查。 `<!-- ROW_MINE: ksummit-discuss.messages.351205 -->`
