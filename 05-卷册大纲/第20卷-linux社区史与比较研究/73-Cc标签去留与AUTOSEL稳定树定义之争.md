# 73 【Linux社区】Cc标签去留与AUTOSEL稳定树定义之争

> 来源：ksummit-discuss p125（50 封全读，2019-07 MAINTAINERS SUMMIT 三线：Cc 去留/Keeping reviews meaningful/stable 定义，夹杂 2014-05 档案信）
> 判定：48 CAND / 2 NV。主题分布：内核文档格式校验之争 1、Cc标签历史价值之辩 1、脚本检查Cc噪音提议 1、cutoff下方Cc实测 1、Cc标签来源追查 1、tglx澄清mbox脚本 1、git-am不加Cc澄清 1、Cc入提交利弊权衡 1、DRM自取补丁实践 1、CMA史料与lore指针 1、gitnotes追踪回溯 1、DRM绘制oops方案 1、Fixes标签反查实践 1、列表讨论附注提案 1、AUTOSEL驱动覆盖忧 1、驱动回溯不可缓论 1、stable保守性之辩 1、以论文存设计演进 1、评审标签四论纲 1、Cc存档价值反证 1、stable只求Cc负担 1、ARM旧板DT收尾 1、Cc唯一存档例外 1、反对评审附说明 1、评审覆盖面不明弊 1、ELC演讲索引指南 1、空评审认知偏差 1、AUTOSEL回滚率辩护 1、Ack语义流变梳理 1、stable定义之争 1、I2C试行评审说明 1、重申Ack旧义 1、提交元数据附加层 1、安卓218例LTS佐证 1、回滚率指标质疑 1、承诺上报每回归 1、中央回归追踪缺位 1、消费电子不上报习性 1、正面评审偏少之因 1、gregkh宣讲承诺 1、回归追踪出资困局 1、单点负荷败因论 1、保密文化与多源更新 1、ACPI与DT属性对接 1、stable指运行时稳定 1、AUTOSEL移出规则 1、LF自资回归追踪议 1、do_on_cpu提案 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p125 的逐封提取（48 CAND / 2 NV），全 48 块采用**单行摘要体例**（丙型）：每块由“## 73.x 【Linux社区】题名”与若干“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 73.1 【Linux社区】内核文档格式校验之争

- 【Linux社区】Michal Simek 主张凡用 kernel-doc/Doxygen 皆应检查、有错即拒补丁，回应 Mauro “不愿仅因文档风格拒收”的立场 `<!-- ROW_MINE: ksummit-discuss.messages.350456 -->`

## 73.2 【Linux社区】Cc标签历史价值之辩

- 【Linux社区】Ellerman 引 submitting-patches 文档质疑 Cc 标签历史价值，附和 Bottomley “git artefact” 论并提议维护者提交时剥离多余 Cc `<!-- ROW_MINE: ksummit-discuss.messages.350457 -->`

## 73.3 【Linux社区】脚本检查Cc噪音提议

- 【Linux社区】Ellerman 提议写脚本自动检查 get_maintainer.pl 盲抄出的 Cc 列表，使维护者提交时无需费心甄别 `<!-- ROW_MINE: ksummit-discuss.messages.350458 -->`

## 73.4 【Linux社区】cutoff下方Cc实测

- 【Linux社区】Ellerman 实测 Cc 置 “---” cutoff 下方仍被 git send-email 读取，引测试提交 7dcbcaee15ac 佐证 Bottomley 方案可行 `<!-- ROW_MINE: ksummit-discuss.messages.350459 -->`

## 73.5 【Linux社区】Cc标签来源追查

- 【Linux社区】Ellerman 对比 lore 原提交与 tip-bot 回帖链接，指认是 tip bot 显式补加 Cc 标签 `<!-- ROW_MINE: ksummit-discuss.messages.350460 -->`

## 73.6 【Linux社区】tglx澄清mbox脚本

- 【Linux社区】tglx 澄清补加 Cc 的实为其 mbox→quilt 脚本，自称 “for hysterical raisins”，并疑 git-am 亦然 `<!-- ROW_MINE: ksummit-discuss.messages.350461 -->`

## 73.7 【Linux社区】git-am不加Cc澄清

- 【Linux社区】Geert 反证其所用版本 git-am 不会依 Cc 头补加标签，呼应 tglx 自承 “I might be wrong” `<!-- ROW_MINE: ksummit-discuss.messages.350462 -->`

## 73.8 【Linux社区】Cc入提交利弊权衡

- 【Linux社区】Geert 论证大系列逐补丁控 Cc 之利弊，支持 Cc 留在提交以免重跑 get_maintainer.pl，并探 git commit --allow-empty 存 cover letter 之险 `<!-- ROW_MINE: ksummit-discuss.messages.350463 -->`

## 73.9 【Linux社区】DRM自取补丁实践

- 【Linux社区】Walleij 自述 DRM 因要求 list ID 而从列表取回自己的补丁，认同 Laurent Pinchart 所指该流程不便 `<!-- ROW_MINE: ksummit-discuss.messages.350464 -->`

## 73.10 【Linux社区】CMA史料与lore指针

- 【Linux社区】Walleij 追溯 CMA 2012 年入主线前 24 轮迭代，指 gmane 旧链已死、Documentation/cma 近乎空置，建议补 lore 指针文档并提 ION destaging `<!-- ROW_MINE: ksummit-discuss.messages.350465 -->`

## 73.11 【Linux社区】gitnotes追踪回溯

- 【Linux社区】Ellerman 展示用 git notes 标 Fixed-by 双向链接（powerpc xmon SPR 例），提议扩展到 stable 树显示 v4.9.y 等各分支回溯状态 `<!-- ROW_MINE: ksummit-discuss.messages.350466 -->`

## 73.12 【Linux社区】DRM绘制oops方案

- 【Linux社区】Herrmann 详述应急日志设计：向各图形驱动逐级请求 framebuffer 回退渲染，核心拟设 drm_render_oops()，承诺 LPC14 展示原型 `<!-- ROW_MINE: ksummit-discuss.messages.350467 -->`

## 73.13 【Linux社区】Fixes标签反查实践

- 【Linux社区】Iwai 证实 SUSE 定期解析 Fixes 标签追踪上游修复，并引 Linus 对 git-notes 的定性 “git-notes is a hack” `<!-- ROW_MINE: ksummit-discuss.messages.350468 -->`

## 73.14 【Linux社区】列表讨论附注提案

- 【Linux社区】Sasha 自述 “fixes for fixes” 脚本可判修复是否已回溯旧 LTS，另提议把相关邮件列表讨论以 git notes 挂到对应 commit `<!-- ROW_MINE: ksummit-discuss.messages.350470 -->`

## 73.15 【Linux社区】AUTOSEL驱动覆盖忧

- 【Linux社区】Brown 担忧 AUTOSEL 常拉入驱动改动而驱动测试覆盖最弱，自动化徒增一层不确定性 `<!-- ROW_MINE: ksummit-discuss.messages.350471 -->`

## 73.16 【Linux社区】驱动回溯不可缓论

- 【Linux社区】Sasha 反对放缓 drivers/ 回溯，称上届 MS 已共识 stable 用户须自测负载，并抱怨某硬件厂商标注 stable 修复稀烂 `<!-- ROW_MINE: ksummit-discuss.messages.350473 -->`

## 73.17 【Linux社区】stable保守性之辩

- 【Linux社区】Brown 强调 stable 的契约是低风险保守更新，指出嵌入式厂商旧版支持属商业协议、树外补丁堆由此而生 `<!-- ROW_MINE: ksummit-discuss.messages.350474 -->`

## 73.18 【Linux社区】以论文存设计演进

- 【Linux社区】Ted 指 LWN 486301 可当 CMA 史料，举 2019 Usenix ATC 的 EROFS 论文为先例，主张以会议演讲与论文保存设计演进 `<!-- ROW_MINE: ksummit-discuss.messages.350475 -->`

## 73.19 【Linux社区】评审标签四论纲

- 【Linux社区】Wolfram 提四论纲：严分 Acked-by/Reviewed-by、Reviewed-by 附说明、trivial 只给 Ack、违规善意批评，宣布 I2C 子系统先行 `<!-- ROW_MINE: ksummit-discuss.messages.350476 -->`

## 73.20 【Linux社区】Cc存档价值反证

- 【Linux社区】Belloni 引 2017 年 James Hogan（MIPS）邮件，证明确有维护者认为 Cc 标签有存档价值 `<!-- ROW_MINE: ksummit-discuss.messages.350477 -->`

## 73.21 【Linux社区】stable只求Cc负担

- 【Linux社区】gregkh 申明 stable 只求维护者加 Cc、愿接信任子系统的 pull（如 David Miller mbox），称维护者是最稀缺资源、绝不加负 `<!-- ROW_MINE: ksummit-discuss.messages.350478 -->`

## 73.22 【Linux社区】ARM旧板DT收尾

- 【Linux社区】Arnd 称 versatile 入 multiplatform 只差 common clock 支持，提议启用 pre-ARMv7 的 ARCH_VIRT 引 QEMU 用户迁移 `<!-- ROW_MINE: ksummit-discuss.messages.350479 -->`

## 73.23 【Linux社区】Cc唯一存档例外

- 【Linux社区】Bottomley 认 Cc 唯一例外价值：借他树补丁求 Ack 未果时，向 Linus 证明 “at least we tried” `<!-- ROW_MINE: ksummit-discuss.messages.350480 -->`

## 73.24 【Linux社区】反对评审附说明

- 【Linux社区】Leon 反对 Reviewed-by 附描述，称增加工作量只会减少评审，信任机制不因多一句话而增进 `<!-- ROW_MINE: ksummit-discuss.messages.350481 -->`

## 73.25 【Linux社区】评审覆盖面不明弊

- 【Linux社区】Wolfram 澄清默认信任新评审者，症结在不知评审覆盖了哪些部分，引 “I did check <xy> but not the media parts” 式说明之别 `<!-- ROW_MINE: ksummit-discuss.messages.350482 -->`

## 73.26 【Linux社区】ELC演讲索引指南

- 【Linux社区】Rowand 介绍 elinux.org 的 ELC_Presentations 各年索引与 devicetree 演讲论文专页，作为检索设计史料的入口 `<!-- ROW_MINE: ksummit-discuss.messages.350483 -->`

## 73.27 【Linux社区】空评审认知偏差

- 【Linux社区】Kara 称评审自评受认知偏差制约、说明无法强制，举证 Ted Tso 直接无视无信誉者的空洞 Reviewed-by `<!-- ROW_MINE: ksummit-discuss.messages.350484 -->`

## 73.28 【Linux社区】AUTOSEL回滚率辩护

- 【Linux社区】Sasha 披露已把维护者自愿回溯的子系统移出 AUTOSEL，并称 AUTOSEL 提交回滚率低于显式 stable 标签提交 `<!-- ROW_MINE: ksummit-discuss.messages.350485 -->`

## 73.29 【Linux社区】Ack语义流变梳理

- 【Linux社区】Geert 梳理标签流变：Acked-by 本义 “looks OK to me”，如今维护者 Ack 即放行他树；另提第五论纲指大量评审未留痕 `<!-- ROW_MINE: ksummit-discuss.messages.350486 -->`

## 73.30 【Linux社区】stable定义之争

- 【Linux社区】Kosina 质问 Sasha 把 stable 从 “维持稳定所需最小改动” 改写为 “贴近上游降低升级成本”，称发行版正因此渐弃 stable 树 `<!-- ROW_MINE: ksummit-discuss.messages.350487 -->`

## 73.31 【Linux社区】I2C试行评审说明

- 【Linux社区】Wolfram 不求强制，援引 commit message 文化改善之先例，称最低形式 “checked everything, all good” 即可，I2C 将试行 `<!-- ROW_MINE: ksummit-discuss.messages.350488 -->`

## 73.32 【Linux社区】重申Ack旧义

- 【Linux社区】Wolfram 重申 Acked-by 旧义 “looks OK to me”，反对仅维护者可用或维护者/非维护者双义并存 `<!-- ROW_MINE: ksummit-discuss.messages.350489 -->`

## 73.33 【Linux社区】提交元数据附加层

- 【Linux社区】Iwai 坚持不改动历史、以普通 pull 共享的提交后附加元数据，称 Linus 不喜 git-notes，自曝曾以 $SHAID 文本文件分支变通 `<!-- ROW_MINE: ksummit-discuss.messages.350490 -->`

## 73.34 【Linux社区】安卓218例LTS佐证

- 【Linux社区】gregkh 引安卓安全团队 2018 统计：218 项回溯请求中 201 项已先在 LTS 树，余者缘于树外代码或回溯补丁自身缺陷 `<!-- ROW_MINE: ksummit-discuss.messages.350491 -->`

## 73.35 【Linux社区】回滚率指标质疑

- 【Linux社区】Brown 质疑 AUTOSEL 回滚率指标失真——本地私修者多不上报，并指企业用户实际从发行版而非裸 LTS 取 stable `<!-- ROW_MINE: ksummit-discuss.messages.350492 -->`

## 73.36 【Linux社区】承诺上报每回归

- 【Linux社区】Roeck 承诺上报 stable 每一个回归，因任何回归都会被援引为反对合并 stable 版本的论据 `<!-- ROW_MINE: ksummit-discuss.messages.350493 -->`

## 73.37 【Linux社区】中央回归追踪缺位

- 【Linux社区】Iwai 点题内核现无中央回归追踪，称是 “another big missing piece”，主张列入 KS 议程 `<!-- ROW_MINE: ksummit-discuss.messages.350494 -->`

## 73.38 【Linux社区】消费电子不上报习性

- 【Linux社区】Brown 以消费电子产品团队经验补证回归极少上报：多数产品团队 “would never even consider” 向上游报告 `<!-- ROW_MINE: ksummit-discuss.messages.350495 -->`

## 73.39 【Linux社区】正面评审偏少之因

- 【Linux社区】Brown 指出挑错式评审远易于背书式评审（“I found a problem!”），正面确认因此系统性偏少 `<!-- ROW_MINE: ksummit-discuss.messages.350496 -->`

## 73.40 【Linux社区】gregkh宣讲承诺

- 【Linux社区】gregkh 提出可赴消费电子团队讲 “all the ways your kernel is insecure and trivial to break”，称数月前已对某大公司讲过 `<!-- ROW_MINE: ksummit-discuss.messages.350497 -->`

## 73.41 【Linux社区】回归追踪出资困局

- 【Linux社区】gregkh 预言回归追踪讨论将重演 “求赞助后 crickets” 剧本，称有能者已备却无公司出资，类比五年前测试投入困局 `<!-- ROW_MINE: ksummit-discuss.messages.350498 -->`

## 73.42 【Linux社区】单点负荷败因论

- 【Linux社区】Iwai 总结历次回归追踪皆败于单点故障——负担压于一人终至放弃，盼自动化分布式方案破局 `<!-- ROW_MINE: ksummit-discuss.messages.350499 -->`

## 73.43 【Linux社区】保密文化与多源更新

- 【Linux社区】Brown 解释消费电子团队不上报缘由：保密心态叠加 LTS 与芯片厂商多源更新，报障归责 “more trouble than it's worth” `<!-- ROW_MINE: ksummit-discuss.messages.350500 -->`

## 73.44 【Linux社区】ACPI与DT属性对接

- 【Linux社区】Hart 剖析 ACPI/DT 属性两问题：机制等价与参数化；指 ACPI 5.0 GpioIO 列表 ACPICA 未实现，举 rfkill-gpio.c 为正例 `<!-- ROW_MINE: ksummit-discuss.messages.350501 -->`

## 73.45 【Linux社区】stable指运行时稳定

- 【Linux社区】Sasha 正面定义 stable 为 “stable runtime rather than a stable codebase”，称规则只要求补丁上游约一周即可回溯，发行版用户在增不减 `<!-- ROW_MINE: ksummit-discuss.messages.350502 -->`

## 73.46 【Linux社区】AUTOSEL移出规则

- 【Linux社区】Sasha 说明移出 AUTOSEL 须维护者主动申请、亦可逐补丁回 NAK；称驱动测试少故更忧驱动而非核心代码 `<!-- ROW_MINE: ksummit-discuss.messages.350503 -->`

## 73.47 【Linux社区】LF自资回归追踪议

- 【Linux社区】Sasha 质疑 LF 何不自资回归追踪项目，称逐项目筹款模式失灵（举 KernelCI 为例）且难向管理层兜售价值 `<!-- ROW_MINE: ksummit-discuss.messages.350504 -->`

## 73.48 【Linux社区】do_on_cpu提案

- 【Linux社区】Desnoyers 提 do_on_cpu 系统调用：以 IPI 上下文字节码解释器补 rseq（Linux 4.18 入主线）之短，向 mm 社区征询页故障等并发风险对策 `<!-- ROW_MINE: ksummit-discuss.messages.350505 -->`
