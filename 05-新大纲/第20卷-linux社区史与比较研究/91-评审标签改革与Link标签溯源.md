# 91 【Linux社区】评审标签改革与Link标签溯源

> 来源：ksummit-discuss p143（50 封全读，2014-05-02 至 2014-05-28，Reviewed-by 语义改革、tglx Link 标签提案源头、changelog 之辩、LWN 统计灌水、ACPI/DT）
> 判定：47 CAND / 3 NV。主题分布：专职评审可行性之辩 1、KS 提名表更新确认 1、stable 测试分支共享 1、维护者是最后评审人 1、SCSI 驱动评审底线 1、changelog 施压论 1、评审标记重于签名 1、SoB 即 DCO 质询 1、SoB 隐含留场期待 1、企业厂商上游内情 1、提交说明缺质检 1、EAS 研讨会报名 1、ARM64 ACPI 缓议 1、邀发行商示范评审 1、无硬件难亲写反驳 1、专职评审稀缺再辩 1、付费评审扩容提议 1、i915 评审仍不足 1、找虫评审标签提议 1、补丁内修订日志惯例 1、make test 边界论 1、评审监督声明之重 1、轻量评审标签提案 1、ACPI 纳 DT 式追问 1、LWN 统计遗漏评审 1、分层评审责任观 1、修订日志噪音质疑 1、Acked-by 中间档 1、squash 归属论点 1、LWN 评审统计沿革 1、0day 性能二分实证 1、致谢与逐轮记事之别 1、文档修订日志规范 1、Juniper 转 DT 实践 1、make test 多年呼吁 1、R 标签强制评审案 1、Acked-by 歧义改革案 1、评审标签门槛论 1、废 Acked-by 过激质疑 1、带限定域评审标签 1、Acked-by 实况观察 1、责任分散机制批评 1、随意评审标记需求 1、总线怪癖既有先例 1、Link 标签提议溯源 1、烂补丁洪水根源论 1、修订日志入 commit 辩护 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p143（实锚 pk 351356-351405）的逐封提取（47 CAND / 3 NV），全 47 块采用**单行摘要体例**（丙型）：每块由“## 91.x 题名”与若干“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 91.1 专职评审可行性之辩

- 【Linux社区】Czerner 反对 Sang 付费专职评审提案，称“理解代码即可写代码”，主张 Reviewed-by 与 Signed-off-by 同等“尊重”。 `<!-- ROW_MINE: ksummit-discuss.messages.351356 -->`

## 91.2 KS 提名表更新确认

- 【Linux社区】Ted T'so 回复 Josh Triplett 称“已相应更新提名 spreadsheet”，记录 2014 Kernel Summit 提名流程由其维护电子表格。 `<!-- ROW_MINE: ksummit-discuss.messages.351357 -->`

## 91.3 stable 测试分支共享

- 【Linux社区】Roeck 提议将自建 stable 测试分支（随 quilt 历史需反复 rebase）发布至 kernel.org；另引 Ben 转述 0day 机器人疑按 author date 而非 commit date 排除旧提交。 `<!-- ROW_MINE: ksummit-discuss.messages.351358 -->`

## 91.4 维护者是最后评审人

- 【Linux社区】hpa 称维护者是“reviewer of last resort”且常为唯一可用评审人，须同时承担评审、架构、管理、导师诸职并兼顾本职工作。 `<!-- ROW_MINE: ksummit-discuss.messages.351359 -->`

## 91.5 SCSI 驱动评审底线

- 【Linux社区】Bottomley 自述驱动评审仅查 checkpatch、能否单独编译与有无显眼错误；单厂商驱动容忍度低，常自己代写 changelog。 `<!-- ROW_MINE: ksummit-discuss.messages.351360 -->`

## 91.6 changelog 施压论

- 【Linux社区】Kosina 称“星球上唯一能促成此事的力量”是维护者说“不，你得做得更好”，并质疑为何不敢以拒收逼厂商花 30 人分钟写好说明。 `<!-- ROW_MINE: ksummit-discuss.messages.351361 -->`

## 91.7 评审标记重于签名

- 【Linux社区】Wysocki 主张 Reviewed-by“应比 sign-off 更受重视”，并称不写代码的专职评审会随时间愈发不可靠。 `<!-- ROW_MINE: ksummit-discuss.messages.351362 -->`

## 91.8 SoB 即 DCO 质询

- 【Linux社区】Lutomirski 追问“SoB 与 DCO 声明如今还有何区别”，挑战 Reviewed-by 重于 SoB 之说。 `<!-- ROW_MINE: ksummit-discuss.messages.351363 -->`

## 91.9 SoB 隐含留场期待

- 【Linux社区】Wysocki 答称 SoB 形式上仅 DCO 声明，但实际期望签名者“至少留场一段时间”修复相关问题。 `<!-- ROW_MINE: ksummit-discuss.messages.351364 -->`

## 91.10 企业厂商上游内情

- 【Linux社区】Petersen 详述企业厂商上游驱动滞后内部树数月、补丁须过 IP/法务审查致说明被剥除、OEM tarball 驱动旧习，并称今春已面谈多家硬件厂商宣导新规。 `<!-- ROW_MINE: ksummit-discuss.messages.351365 -->`

## 91.11 提交说明缺质检

- 【Linux社区】NeilBrown 称写好 changelog 是门艺术且无 checkpatch 式工具把关，举曾遇标 -stable 的补丁说明不写 bug 本身。 `<!-- ROW_MINE: ksummit-discuss.messages.351367 -->`

## 91.12 EAS 研讨会报名

- 【Linux社区】Intel 的 Yuyang Du 报名能效调度研讨会，点名关注 CPU 利用率、负载均衡接口细化、异构调度与工具。 `<!-- ROW_MINE: ksummit-discuss.messages.351368 -->`

## 91.13 ARM64 ACPI 缓议

- 【Linux社区】Olof 称 ARM64 ACPI 议题仍在 NDA 与“传话游戏”阶段，主张聚焦已出货的 Intel 嵌入式平台 Minnowboard/Galileo。 `<!-- ROW_MINE: ksummit-discuss.messages.351369 -->`

## 91.14 邀发行商示范评审

- 【Linux社区】Bottomley 赞同“hell, yes”无法强逼硬件厂商，邀发行商评审少量厂商补丁并示范可行 changelog 作“训练轮”。 `<!-- ROW_MINE: ksummit-discuss.messages.351370 -->`

## 91.15 无硬件难亲写反驳

- 【Linux社区】Sang 反驳 Czerner：多数 I2C 驱动因无硬件而无法亲写，让驱动能跑与写得规范是两回事。 `<!-- ROW_MINE: ksummit-discuss.messages.351371 -->`

## 91.16 专职评审稀缺再辩

- 【Linux社区】Czerner 称愿专职评审者比偶发评审者更少，反问是否要现维护者停码或让位，主张鼓励开发者多评审。 `<!-- ROW_MINE: ksummit-discuss.messages.351372 -->`

## 91.17 付费评审扩容提议

- 【Linux社区】Sang 明确提议给少数人资金专做评审而非板卡 bringup，并称仅靠鼓励开发者“won't scale enough”。 `<!-- ROW_MINE: ksummit-discuss.messages.351373 -->`

## 91.18 i915 评审仍不足

- 【Linux社区】Vetter 称 drm/i915 全员同雇主尚可强令评审仍不够，警惕“半小时橡皮图章 20 个补丁”，提议以 LWN 统计提高评审者可见度。 `<!-- ROW_MINE: ksummit-discuss.messages.351374 -->`

## 91.19 找虫评审标签提议

- 【Linux社区】Carpenter 提议为发现真实 bug 的评审者设专用标签，称这类人才是“best sort of reviewer”。 `<!-- ROW_MINE: ksummit-discuss.messages.351375 -->`

## 91.20 补丁内修订日志惯例

- 【Linux社区】Vetter 坚持补丁内修订日志随 commit 收录并须致谢评审者，举 commit d978ef14456a38034f6c0e 为范例，称二元标签难体现评审耗时差异。 `<!-- ROW_MINE: ksummit-discuss.messages.351376 -->`

## 91.21 make test 边界论

- 【Linux社区】Gorman 称其自动化性能测试单核 4-5 天、永不适用 make test；支持以 make test 包功能验证与 LTP，反对强制统一“标准测试方法”。 `<!-- ROW_MINE: ksummit-discuss.messages.351377 -->`

## 91.22 评审监督声明之重

- 【Linux社区】Roeck 警告若人人忽视 SubmittingPatches 的“Reviewer's statement of oversight”将很可怕，自陈不轻用 Reviewed-by。 `<!-- ROW_MINE: ksummit-discuss.messages.351378 -->`

## 91.23 轻量评审标签提案

- 【Linux社区】Zohar 提议以“Commented-by”替代责任过重的 Reviewed-by，并建议在大会演讲统计中曝光以促参与。 `<!-- ROW_MINE: ksummit-discuss.messages.351379 -->`

## 91.24 ACPI 纳 DT 式追问

- 【Linux社区】Olof 就 Rafael 扩展 ACPI 纳入 DT 式信息的三层方案追问电源管理、时钟/稳压器引用与 pin control 归属，Catalin 忧厂商自创 ACPI+DT 混搭。 `<!-- ROW_MINE: ksummit-discuss.messages.351380 -->`

## 91.25 LWN 统计遗漏评审

- 【Linux社区】Triplett 指 LWN 统计只聚焦 Signed-off-by 而“完全不提 Reviewed-by”。 `<!-- ROW_MINE: ksummit-discuss.messages.351381 -->`

## 91.26 分层评审责任观

- 【Linux社区】Zohar 称通用、跨子系统的评审不需底层知识但耗时，做此类评审者无人愿背 Reviewed-by 责任。 `<!-- ROW_MINE: ksummit-discuss.messages.351382 -->`

## 91.27 修订日志噪音质疑

- 【Linux社区】Brown 反对修订日志入 commit，称其令 changelog“large and noisy”且依赖提交者自律，多数情况价值甚微。 `<!-- ROW_MINE: ksummit-discuss.messages.351383 -->`

## 91.28 Acked-by 中间档

- 【Linux社区】Roeck 自述 Acked-by 用法为“看起来不错，但要子系统维护者或有深入了解者再看”，充当 Reviewed-by 之外的缓冲档。 `<!-- ROW_MINE: ksummit-discuss.messages.351384 -->`

## 91.29 squash 归属论点

- 【Linux社区】Zohar 主张压缩补丁时“至少须认录谁贡献了什么”，回击修订日志无价值说。 `<!-- ROW_MINE: ksummit-discuss.messages.351385 -->`

## 91.30 LWN 评审统计沿革

- 【Linux社区】Corbet 称 LWN 偶发刊出 Reviewed-by 与 Reported-by 统计表，但绝对数小、兴趣低，承诺“应该重访”该题。 `<!-- ROW_MINE: ksummit-discuss.messages.351386 -->`

## 91.31 0day 性能二分实证

- 【Linux社区】McKenney 证实常收 Fengguang 0day 邮件且性能变化“已方便地二分到具体 commit”，支持将基准工作负载接入该自动检查系统。 `<!-- ROW_MINE: ksummit-discuss.messages.351387 -->`

## 91.32 致谢与逐轮记事之别

- 【Linux社区】Brown 称“感谢评审”与逐轮详记每次改动“有天壤之别”，反对修订日志全面入 commit。 `<!-- ROW_MINE: ksummit-discuss.messages.351388 -->`

## 91.33 文档修订日志规范

- 【Linux社区】Luck 引 Documentation/SubmittingPatches 585-592 行，指 v1 与 v2 差异等“patch changelogs”应置于 --- 之后、不入永久 changelog。 `<!-- ROW_MINE: ksummit-discuss.messages.351389 -->`

## 91.34 Juniper 转 DT 实践

- 【Linux社区】Roeck 披露 Juniper 在 x86 平台做部分 ACPI 转 DT 以支持 DT overlay，建议邀 Pantelis Antoniou 与 Georgi Vlaev 与会讨论。 `<!-- ROW_MINE: ksummit-discuss.messages.351391 -->`

## 91.35 make test 多年呼吁

- 【Linux社区】gregkh 称功能测试进 make test 是其“多年来一直要求的”，性能测试则至少要文档化运行方法。 `<!-- ROW_MINE: ksummit-discuss.messages.351392 -->`

## 91.36 R 标签强制评审案

- 【Linux社区】Walmsley 提议 MAINTAINERS 增“R:”标注优质评审、每补丁合并前须有独立 Reviewed-by，并将优质评审逐步转为共同维护者。 `<!-- ROW_MINE: ksummit-discuss.messages.351393 -->`

## 91.37 Acked-by 歧义改革案

- 【Linux社区】Walmsley 指其混用维护者放行与随意评审两种互斥用途，提议新设“Maintainer-acked-by”并废除 Acked-by。 `<!-- ROW_MINE: ksummit-discuss.messages.351394 -->`

## 91.38 评审标签门槛论

- 【Linux社区】Zohar 附议歧义说，称“Reviewed-by 对常人责任太重不敢用”，主张仿 Maintainer-acked-by 限定其范围。 `<!-- ROW_MINE: ksummit-discuss.messages.351395 -->`

## 91.39 废 Acked-by 过激质疑

- 【Linux社区】Roeck 引文档定义“记录 acker 至少已评审并表接受”，称禁止普通评审者表达接受“有点极端”。 `<!-- ROW_MINE: ksummit-discuss.messages.351397 -->`

## 91.40 带限定域评审标签

- 【Linux社区】Zohar 提议“Reviewed-by [option]:”附 style、logic、syntax 等可选限定域，以降低评审责任门槛。 `<!-- ROW_MINE: ksummit-discuss.messages.351398 -->`

## 91.41 Acked-by 实况观察

- 【Linux社区】Triplett 依实践称随意评审已大多改用 Reviewed-by，Acked-by 实际只剩“维护者放行但不经己树”用途。 `<!-- ROW_MINE: ksummit-discuss.messages.351399 -->`

## 91.42 责任分散机制批评

- 【Linux社区】Triplett 支持把 MAINTAINERS 泛化为“给该子系统的补丁抄送这些人”名单并经 get_maintainer.pl 投递，指邮件列表有“diffusion of responsibility”之弊。 `<!-- ROW_MINE: ksummit-discuss.messages.351400 -->`

## 91.43 随意评审标记需求

- 【Linux社区】Torokhov 称不做首过与修正后复审的完整评审就不会盖 Reviewed-by，戏提“Nitpicked-by”。 `<!-- ROW_MINE: ksummit-discuss.messages.351401 -->`

## 91.44 总线怪癖既有先例

- 【Linux社区】Wysocki 指 PCI 与 PNP 总线“早已有此类怪癖钩子”，回应 Olof 将绑定知识收进驱动的主张。 `<!-- ROW_MINE: ksummit-discuss.messages.351402 -->`

## 91.45 Link 标签提议溯源

- 【Linux社区】tglx 提出以“Link: https://lkml.kernel.org/r/MESSAGE_ID_OF_PATCH”取代 v1-n 修订记述，称后者多为浪费电子。 `<!-- ROW_MINE: ksummit-discuss.messages.351403 -->`

## 91.46 烂补丁洪水根源论

- 【Linux社区】tglx 批判 LWN 统计将催生竞赛式烂评审，指一些机构为冲“top X 贡献者”放出自审缺失的“works for me”补丁，自述晨收 30+ 补丁系列轰炸。 `<!-- ROW_MINE: ksummit-discuss.messages.351404 -->`

## 91.47 修订日志入 commit 辩护

- 【Linux社区】Vetter 称修订日志随 SoB 置底不碍事且偶有助理解补丁演化，更是追责作者未落实评审意见的工具，入 commit 显其受重视。 `<!-- ROW_MINE: ksummit-discuss.messages.351405 -->`
