# 75 【Linux社区】ChangeId之争与Linus定调

> 来源：ksummit-discuss p127（50 封全读，2019-08 Change-Id/Link 之争主线+Acked-by 释义修订，夹杂 2014-05 档案信）
> 判定：49 CAND / 1 NV。主题分布：旧板卡 DT 转换收尾 1、fsnotify 模块导出共识 1、patchwork 归档链接落地 1、TAB 选举提名公告 1、seccomp 分层定案 1、seccomp 原型与 LSM 1、seccomp 过滤范围清单 1、seccomp 深过滤细化 1、clone3 入主线定论 1、Acked-by 释义修订 1、R: 强制门槛异议 1、QR oops 项目盘问 1、拒绝标签圈子化 1、轻量审阅标签之问 1、标签用途论断 1、Coccinelle 确认场景 1、R: 行定位澄清 1、R: 列名门槛偏高 1、加 R: 先征同意 1、强制审阅标记设想 1、Reviewed-by 语义裁定 1、Change-Id 提案 1、versatile QEMU 依赖 PCI 1、Linus 拒 Change-Id 1、gerrit 邮件汇入 lore 1、直链 gerrit 提案 1、反对 gerrit 长期链接 1、版本更迭断链论 1、X-Gerrit 头实证 1、Change-Id 去 Gerrit 化 1、拒绑 Gerrit 邮件头 1、指控反 Gerrit 偏见 1、Linus 接受 gerrit Link 1、列表抄送上限放宽 1、跨子系统补丁黑洞 1、Link 通用化主张 1、含 ID 折中链接 1、Change-Id 移出提交 1、Email2git 现状核查 1、Message-Id 链式主张 1、两种 Link 形式权衡 1、手工链接旧版实践 1、封面信链接链方案 1、无服务器链接反驳 1、PM 依赖建模路线 1、折中归档方案重申 1、弃用段规避公私争 1、提交者摩擦之争 1、git 钩子不够论 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p127 的逐封提取（49 CAND / 1 NV），全 49 块采用**单行摘要体例**（丙型）：每块由“## 75.x 【Linux社区】题名”与若干“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 75.1 【Linux社区】旧板卡 DT 转换收尾

- 【Linux社区】Arnd 赞同 Rob 将 versatile 全量转 DT（common clock、irq、PCI 一步到位），指出 mach-versatile 仅剩 plat/clcd.h 与 plat/sched_clock.h 依赖，可用 ccflags-y 解决 `<!-- ROW_MINE: ksummit-discuss.messages.350556 -->`

## 75.2 【Linux社区】fsnotify 模块导出共识

- 【Linux社区】Jan Kara 表态不反对向模块导出 fsnotify（kernel/audit_tree.c 已是外部使用者），承诺等 NFS 补丁接近合入时把导出补丁推进自己的树 `<!-- ROW_MINE: ksummit-discuss.messages.350557 -->`

## 75.3 【Linux社区】patchwork 归档链接落地

- 【Linux社区】Andrew Donnellan 报告已提交补丁：patchwork 网页界面与 REST API 增加每补丁的邮件归档链接，mbox 内嵌链接一项目尚未做 `<!-- ROW_MINE: ksummit-discuss.messages.350558 -->`

## 75.4 【Linux社区】TAB 选举提名公告

- 【Linux社区】Laura Abbott 公告 2019 里斯本内核峰会选举 5 席并首次启用电子投票，提名截止 9 月 9 日 9am GMT+1 硬时限，附 Corbet、Greg KH 等十人名单及届次 `<!-- ROW_MINE: ksummit-discuss.messages.350559 -->`

## 75.5 【Linux社区】seccomp 分层定案

- 【Linux社区】Luto 否定“读完参数再跑主过滤器”方案（EFAULT 与 SECCOMP_RET_TRACE/TRAP 竞态），改为独立深层过滤层，并要求可查询 syscall 是否可过滤 `<!-- ROW_MINE: ksummit-discuss.messages.350560 -->`

## 75.6 【Linux社区】seccomp 原型与 LSM

- 【Linux社区】Kees Cook 披露早期原型是 seccomp 触发的 LSM，认为需 Landlock 式进程自有 LSM，两大高频需求为路径检查与网络地址检查 `<!-- ROW_MINE: ksummit-discuss.messages.350561 -->`

## 75.7 【Linux社区】seccomp 过滤范围清单

- 【Linux社区】Luto 补充深过滤需求：clone() 标志、新 clone 提案不断加 struct、bpf() 过滤，并认可 LSM 式实现也是一条路 `<!-- ROW_MINE: ksummit-discuss.messages.350562 -->`

## 75.8 【Linux社区】seccomp 深过滤细化

- 【Linux社区】Luto 指 clone3 已进 5.3 主线“evil has been done”，提议向主 seccomp 过滤器传标志声明 FILTERABLE 与 Landlock 钩子启用情况，警告 LSM 钩子变更易开安全洞 `<!-- ROW_MINE: ksummit-discuss.messages.350563 -->`

## 75.9 【Linux社区】clone3 入主线定论

- 【Linux社区】Brauner 宣告 clone3 “不再是提案”，已随 5.3 合并窗口进入主线，成为 seccomp 指针过滤设计的既成约束 `<!-- ROW_MINE: ksummit-discuss.messages.350564 -->`

## 75.10 【Linux社区】Acked-by 释义修订

- 【Linux社区】Paul Walmsley 支持 Ted 把 Acked-by 释义改为“维护者或 reviewer 同意合入”，并主张 reviewer 应限定为 MAINTAINERS 中 R: 行所列者 `<!-- ROW_MINE: ksummit-discuss.messages.350565 -->`

## 75.11 【Linux社区】R: 强制门槛异议

- 【Linux社区】Jan Kara 称要求 R: 条目是“不必要的官僚主义”，会吓退非核心开发者，Reviewed-by 采纳与否应留给维护者裁量 `<!-- ROW_MINE: ksummit-discuss.messages.350566 -->`

## 75.12 【Linux社区】QR oops 项目盘问

- 【Linux社区】Ted 确认 QR 编码 oops 工作团队为大学生 Levente Kurusa 与 Teodora，追问重心是二维码生成还是配套 web 后端收集分析 `<!-- ROW_MINE: ksummit-discuss.messages.350567 -->`

## 75.13 【Linux社区】拒绝标签圈子化

- 【Linux社区】Jiri Kosina 附和 Jan Kara：标签确有人滥用于“在 changelog 刷名”，但把 review 限入“MAINTAINERS 俱乐部”只会阻止新审阅者参与 `<!-- ROW_MINE: ksummit-discuss.messages.350568 -->`

## 75.14 【Linux社区】轻量审阅标签之问

- 【Linux社区】Julia Lawall 追问有无表达“我懂行且看过、觉得没问题”的中间级标签，并指出 Ted 拟议文本中重复 “the” 笔误 `<!-- ROW_MINE: ksummit-discuss.messages.350569 -->`

## 75.15 【Linux社区】标签用途论断

- 【Linux社区】Jan Kara 论断 changelog 标签仅有记功与“多一个可被怪罪的人（bug 抄送）”两个用途，审阅置信度写进邮件即可，无须记入日志 `<!-- ROW_MINE: ksummit-discuss.messages.350570 -->`

## 75.16 【Linux社区】Coccinelle 确认场景

- 【Linux社区】Julia Lawall 举例：0-day 转来 Coccinelle 发现的 bug 修复补丁，想要简洁无歧义地表示“看过、像修了该 bug”而不背书测试 `<!-- ROW_MINE: ksummit-discuss.messages.350571 -->`

## 75.17 【Linux社区】R: 行定位澄清

- 【Linux社区】Thomas Gleixner 定性：MAINTAINERS 的 R: 行只为确保相关补丁抄送到这些人，并不意味着别人不被允许或不鼓励审阅 `<!-- ROW_MINE: ksummit-discuss.messages.350572 -->`

## 75.18 【Linux社区】R: 列名门槛偏高

- 【Linux社区】Christian Brauner 认为只认 R: 者的 ack 过严且打击参与，很多人怕显得自大不愿主动申请列为 R:，建议维护者更放心添人 `<!-- ROW_MINE: ksummit-discuss.messages.350573 -->`

## 75.19 【Linux社区】加 R: 先征同意

- 【Linux社区】tglx 认同“过严”并披露实务：加 R: 会先询问开发者本人且“相当多的人拒绝”，Brauner 随即承认各自经验印证 R: 限制不可取 `<!-- ROW_MINE: ksummit-discuss.messages.350574 -->`

## 75.20 【Linux社区】强制审阅标记设想

- 【Linux社区】Brauner 提出比 Cc 更强的 “Requires-Review-by” 设想：标记某补丁必须先获指定人审阅才可考虑合入，且不必列于 MAINTAINERS `<!-- ROW_MINE: ksummit-discuss.messages.350575 -->`

## 75.21 【Linux社区】Reviewed-by 语义裁定

- 【Linux社区】James Bottomley 裁定该场景就用 Reviewed-by，实测过可加 “#the bits I understand or care about” 注释，采纳与否纯属维护者决定 `<!-- ROW_MINE: ksummit-discuss.messages.350576 -->`

## 75.22 【Linux社区】Change-Id 提案

- 【Linux社区】Doug Anderson 提议内核提交允许 Change-Id 以串联同一逻辑补丁各版本，解决 Message-Id 只能链到末版、旧版讨论难回溯的问题 `<!-- ROW_MINE: ksummit-discuss.messages.350577 -->`

## 75.23 【Linux社区】versatile QEMU 依赖 PCI

- 【Linux社区】Peter Maydell 指出用户滞留 QEMU versatilepb 主因是它有 PCI，建议先合入通用 DT 驱动 PCI 补丁，再为 QEMU virt 板加 PCI `<!-- ROW_MINE: ksummit-discuss.messages.350578 -->`

## 75.24 【Linux社区】Linus 拒 Change-Id

- 【Linux社区】Linus 直答 “No. Not without some ground rules.”，称不可查询的 UUID 是“无意义的垃圾”，推崇 Link: https://lore.kernel.org/r/ 形式并称会亲自删除噪音 `<!-- ROW_MINE: ksummit-discuss.messages.350579 -->`

## 75.25 【Linux社区】gerrit 邮件汇入 lore

- 【Linux社区】Olof 提出 gerrit 实例可向邮件列表发出补丁与评论、进 lore 归档，但强调 Change-Id URL 无永久归档保证，反向映射旧版仍无好解 `<!-- ROW_MINE: ksummit-discuss.messages.350580 -->`

## 75.26 【Linux社区】直链 gerrit 提案

- 【Linux社区】Guenter Roeck 举 chromium-review.googlesource.com 的 Link 与 Change-Id 同指一例（+/1759334），主张直接链接即可免去查询 `<!-- ROW_MINE: ksummit-discuss.messages.350581 -->`

## 75.27 【Linux社区】反对 gerrit 长期链接

- 【Linux社区】Olof 以 Reader、Google+ 等产品被 EOL 为例拒绝依赖公司 URL，称 URL 会无重定向地失效，lore 才是外部永久归档 `<!-- ROW_MINE: ksummit-discuss.messages.350582 -->`

## 75.28 【Linux社区】版本更迭断链论

- 【Linux社区】Dmitry Torokhov 指出 v2/v3/v4 换新 Message-Id 致与旧讨论断链，而 Change-Id 任何人都能 google 到 LKML 结果，期待 patchwork 学会用它 `<!-- ROW_MINE: ksummit-discuss.messages.350583 -->`

## 75.29 【Linux社区】X-Gerrit 头实证

- 【Linux社区】Olof 抽查 chromium 邮件原文，列 X-Gerrit-Change-Id、Change-Number、ChangeURL、Commit 四个邮件头，断言无需不透明 Change-Id `<!-- ROW_MINE: ksummit-discuss.messages.350584 -->`

## 75.30 【Linux社区】Change-Id 去 Gerrit 化

- 【Linux社区】Doug 澄清提案全程不碰 gerrit 服务器，靠公开归档搜索 Change-Id 字符串串联 v1/v2/v3，并引 git hash 作为“可接受非 URL 标识”先例 `<!-- ROW_MINE: ksummit-discuss.messages.350585 -->`

## 75.31 【Linux社区】拒绑 Gerrit 邮件头

- 【Linux社区】Dmitry 指出 X-Gerrit-* 头是 Gerrit 专属，主张应能在不涉及任何 Gerrit 的情况下给外发补丁打统一标签 `<!-- ROW_MINE: ksummit-discuss.messages.350586 -->`

## 75.32 【Linux社区】指控反 Gerrit 偏见

- 【Linux社区】Ted 称 Red Hat bugzilla、launchpad、patchwork 链接早已进 commit 日志却无人要求存续承诺，禁 gerrit 链接纯属 “anti-Gerrit bias” `<!-- ROW_MINE: ksummit-discuss.messages.350587 -->`

## 75.33 【Linux社区】Linus 接受 gerrit Link

- 【Linux社区】Linus 表态公开 gerrit 库的 Link: 今天即可用且远胜 Change-Id，顺带讥 “amend” 拼写（单写 m），并追问 c/1158 是否长期稳定 `<!-- ROW_MINE: ksummit-discuss.messages.350588 -->`

## 75.34 【Linux社区】列表抄送上限放宽

- 【Linux社区】应 Michael Kerrisk（man-pages）请求，Ted 将 ksummit-discuss 付 moderation 前的抄送人数上限从更低值升至 50 `<!-- ROW_MINE: ksummit-discuss.messages.350589 -->`

## 75.35 【Linux社区】跨子系统补丁黑洞

- 【Linux社区】Josh 描述 50 补丁只换来 10 ack、3 nak、37 沉默，提议 git.kernel.org 通知提交者的 git 钩子，Mauro 表示愿共享 media 树钩子代码 `<!-- ROW_MINE: ksummit-discuss.messages.350590 -->`

## 75.36 【Linux社区】Link 通用化主张

- 【Linux社区】Linus 建议给 gitk 与 git.kernel.org（cgit）加 Link: 超链接直接开浏览器，称通用 Link: 标签整体上胜过专用 Change-Id `<!-- ROW_MINE: ksummit-discuss.messages.350591 -->`

## 75.37 【Linux社区】含 ID 折中链接

- 【Linux社区】Vlastimil Babka 发现 /q/I3268f9... 形式链接可重定向到短链，兼顾可点击与跨站可搜索，“the best of both worlds”，类同 lore 的 message-id `<!-- ROW_MINE: ksummit-discuss.messages.350592 -->`

## 75.38 【Linux社区】Change-Id 移出提交

- 【Linux社区】Sean Paul 建议把 Change-Id 放邮件 “---” 之下供 patchwork 之类工具跨版本追踪，成熟后再以 patchwork 链接形式进 commit `<!-- ROW_MINE: ksummit-discuss.messages.350594 -->`

## 75.39 【Linux社区】Email2git 现状核查

- 【Linux社区】Brendan Higgins 指出问题一已由 cregit 的 Email2git 覆盖（启发式非保证），问题二未覆盖，建议先验证 Email2git 可行性再定方案 `<!-- ROW_MINE: ksummit-discuss.messages.350595 -->`

## 75.40 【Linux社区】Message-Id 链式主张

- 【Linux社区】Joel Fernandes 提议每版补丁附上一版 Message-Id 供 email2git 串联，认为强制所有贡献者改用 Change-Id 不现实 `<!-- ROW_MINE: ksummit-discuss.messages.350596 -->`

## 75.41 【Linux社区】两种 Link 形式权衡

- 【Linux社区】Ted 主张 /c/1158 或 /q/I<id> 两种 Link 形式，“I3268...” 部分丑陋纯属观感问题，bugzilla.kernel.org 链接先例已为人们接受 `<!-- ROW_MINE: ksummit-discuss.messages.350597 -->`

## 75.42 【Linux社区】手工链接旧版实践

- 【Linux社区】Sean Paul 亮出 commit 1452c25b0e60 例证其在新版补丁中手工罗列全部旧版链接的做法，盼有更省力机制 `<!-- ROW_MINE: ksummit-discuss.messages.350598 -->`

## 75.43 【Linux社区】封面信链接链方案

- 【Linux社区】tglx 给出 “This is version X of this series...” 封面信链式模板与 “---” 段 V2/V3 链接排布，并称自己按补丁自动加 Link 已做了多年 `<!-- ROW_MINE: ksummit-discuss.messages.350599 -->`

## 75.44 【Linux社区】无服务器链接反驳

- 【Linux社区】Doug 强调发 v1 时 “THERE IS NO GERRIT LINK”，现场演示用 lore 搜索 Change-Id 找回 v1/v2 及落库 commit，反证 ID 本身可用 `<!-- ROW_MINE: ksummit-discuss.messages.350600 -->`

## 75.45 【Linux社区】PM 依赖建模路线

- 【Linux社区】Kevin Hilman 主张 IOMMU/摄像头类依赖用 runtime PM 引用计数解决，静态依赖可用 DT phandle 建模，I2C 按需激活可规避恢复次序问题 `<!-- ROW_MINE: ksummit-discuss.messages.350601 -->`

## 75.46 【Linux社区】折中归档方案重申

- 【Linux社区】tglx 重申把 Change-Id 放封面信或 “---” 弃用段进归档，commit 内只放 Link: //lkml.kernel.org/r/$MSGID，“Linus is happy” `<!-- ROW_MINE: ksummit-discuss.messages.350602 -->`

## 75.47 【Linux社区】弃用段规避公私争

- 【Linux社区】tglx 补充：封面信与弃用段不进入 commit 消息，可一并避免公共/私有引用之争 `<!-- ROW_MINE: ksummit-discuss.messages.350603 -->`

## 75.48 【Linux社区】提交者摩擦之争

- 【Linux社区】Dmitry 反驳 tglx：提交者不在乎追溯，受益者是系统集成者与维护者，手工收集 Message-Id 摩擦过大，git 钩子更可行 `<!-- ROW_MINE: ksummit-discuss.messages.350604 -->`

## 75.49 【Linux社区】git 钩子不够论

- 【Linux社区】Joel 以自身 Gerrit 经验反驳：新补丁须手工补旧 Change-Id 才能关联，钩子只管初次生成，元数据终究离不开人工 `<!-- ROW_MINE: ksummit-discuss.messages.350605 -->`
