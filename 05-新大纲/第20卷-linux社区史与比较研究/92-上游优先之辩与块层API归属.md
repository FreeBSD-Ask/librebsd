# 92 【Linux社区】上游优先之辩与块层API归属

> 来源：ksummit-discuss p144（50 封全读，2014-05-04 至 2014-05-29，树外 tarball 与上游优先、Acked-by 论战、块层 API 议题交锋、stable 测试）
> 判定：47 CAND / 3 NV。主题分布：临时审查是否入档 1、版本比对难自动化 1、记名为激励评审者 1、客户优先对上游优先 1、临时标签或为负值 1、补丁串问题三分法 1、ACPI纳DT信息三层 1、树外tarball坑客户 1、厂商两头经历佐证 1、企业冲LWN统计灌水 1、企业厂商提交内情 1、补丁集内应相关 1、文档早定义作佐证 1、评审者即共同维护 1、五维护者口径不一 1、树外更新害及支持 1、Juniper部分转DT 1、存量老驱动借口辩 1、上游接纳非先例 1、琐碎补丁稀释评审 1、仅真bug修复记名 1、Link标签指回讨论 1、逼公司内部辅导 1、跨子系统局部确认 1、局部Ack书写实践 1、topic分支分批收 1、标签之别在声誉 1、stable回归来源析 1、拆分squash存险 1、消费电子无视上游 1、雇主阻挠正式挂名 1、commit反查讨论工具 1、块层API议题提案 1、议题应去fs峰会 1、块层为何非议题 1、PM覆盖全树之辩 1、ext4保Acked原义 1、LF有通报联系名单 1、ARM农场测stable 1、块层波及不输PM 1、多Link串全版本 1、v2应Link回v1 1、30个Cc破LKML限 1、另立Supported标签 1、流程未坏勿添乱 1、索尼坚持贴主线 1、为未知问题造流程 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p144（实锚 pk 351406-351455）的逐封提取（47 CAND / 3 NV），全 47 块采用**单行摘要体例**（丙型）：每块由“## 92.x 题名”与若干“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 92.1 临时审查是否入档

- 【Linux社区】Laurent Pinchart 质疑临时评审是否值得记入 git 历史，自称略读后只回“looks good to me” `<!-- ROW_MINE: ksummit-discuss.messages.351406 -->`

## 92.2 版本比对难自动化

- 【Linux社区】Laurent Pinchart 称收 vN+1 须对照 vN 与旧批注逐条核实，问其他维护者如何自动化此流程 `<!-- ROW_MINE: ksummit-discuss.messages.351408 -->`

## 92.3 记名为激励评审者

- 【Linux社区】Dmitry Torokhov 称是否记录个人无所谓，但争论本意是“给评审者更多认可、让流程更有吸引力” `<!-- ROW_MINE: ksummit-discuss.messages.351409 -->`

## 92.4 客户优先对上游优先

- 【Linux社区】Dan Williams 将矛盾概括为“customer first vs upstream first”：社区不保证接纳时限，厂商便改发树外 tarball `<!-- ROW_MINE: ksummit-discuss.messages.351410 -->`

## 92.5 临时标签或为负值

- 【Linux社区】Laurent Pinchart 主张认可须有价值才有激励作用，“临时评审标签甚至可能是负价值” `<!-- ROW_MINE: ksummit-discuss.messages.351411 -->`

## 92.6 补丁串问题三分法

- 【Linux社区】Josh Triplett 拆三类：反馈未完勿发 v2（建议样板文）、基础错误靠提交前自动化、邮件补丁串需 git 工作流 `<!-- ROW_MINE: ksummit-discuss.messages.351412 -->`

## 92.7 ACPI纳DT信息三层

- 【Linux社区】Rafael 提出三层规划：ACPI 配置对象入规范、辅助规范文档、DT bindings；规则：用 ACPI PM 就不得直接操纵时钟/稳压器，决定不能由各驱动自作 `<!-- ROW_MINE: ksummit-discuss.messages.351413 -->`

## 92.8 树外tarball坑客户

- 【Linux社区】Jiri Kosina 称 OS 厂商不会支持树外“随机”版本驱动，预期客户将向硬件厂商追问 `<!-- ROW_MINE: ksummit-discuss.messages.351414 -->`

## 92.9 厂商两头经历佐证

- 【Linux社区】Dan Williams 自述两侧经历：企业存储驱动依赖核心库反成负债，客户夹在 OS 厂商不同更新节奏间施压 `<!-- ROW_MINE: ksummit-discuss.messages.351415 -->`

## 92.10 企业冲LWN统计灌水

- 【Linux社区】tglx 称亲见企业目标写明冲 lwn 统计前 X 名，因统计是经理眼中的“客观指标”；拒 git 工具论：“Crap stays crap”，邮件一键可删，质量才是问题 `<!-- ROW_MINE: ksummit-discuss.messages.351416 -->`

## 92.11 企业厂商提交内情

- 【Linux社区】Ben Hutchings 忆某 OEM 明文要求除显卡外全部 in-tree 驱动且另要树外包；David Miller 对“差异化接口”最严；内部提交信息含代号须重写 `<!-- ROW_MINE: ksummit-discuss.messages.351417 -->`

## 92.12 补丁集内应相关

- 【Linux社区】Mimi Zohar 称大补丁集有时不可拆分，下一步应保证集内补丁彼此相关 `<!-- ROW_MINE: ksummit-discuss.messages.351418 -->`

## 92.13 文档早定义作佐证

- 【Linux社区】Randy Dunlap 引 SubmittingPatches“patch series=有序多个相关补丁”定义，讥“Not that anyone reads documentation” `<!-- ROW_MINE: ksummit-discuss.messages.351419 -->`

## 92.14 评审者即共同维护

- 【Linux社区】Rob Herring 称机制今已有：DT bindings 设 5 名维护者几乎纯评审；反问“信任其评审何不信其为共同维护者” `<!-- ROW_MINE: ksummit-discuss.messages.351421 -->`

## 92.15 五维护者口径不一

- 【Linux社区】Olof 称 5 名 DT 维护者反馈之并集令投稿者无所适从；评审者与维护者之别在共享 git 树与 linux-next 预期，非信任问题 `<!-- ROW_MINE: ksummit-discuss.messages.351422 -->`

## 92.16 树外更新害及支持

- 【Linux社区】MKP 区分“驱动 bug 修复”与“太丑的价值增强”，称树外 tarball 迫使客户放弃 distro 支持 `<!-- ROW_MINE: ksummit-discuss.messages.351423 -->`

## 92.17 Juniper部分转DT

- 【Linux社区】引 Guenter：Juniper 正部分 ACPI 转 DT 以便 x86 用 DT overlay，建议邀 Pantelis Antoniou、Georgi Vlaev；Rafael 追问 overlay 如何引用 ACPI 命名空间对象 `<!-- ROW_MINE: ksummit-discuss.messages.351424 -->`

## 92.18 存量老驱动借口辩

- 【Linux社区】MKP 称老企业驱动已烂到按今日标准进不了内核，厂商“在 2.6.15 i386 测过故兼容一切内核”论调“completely meaningless” `<!-- ROW_MINE: ksummit-discuss.messages.351425 -->`

## 92.19 上游接纳非先例

- 【Linux社区】Dan Williams 主张缺“试验而不永久背书”的机制，“上游接纳不应成为先例事件”；非企业 OSV 场景厂商只能填空或让竞争对手填 `<!-- ROW_MINE: ksummit-discuss.messages.351426 -->`

## 92.20 琐碎补丁稀释评审

- 【Linux社区】JBottomley 称 Parallels 计功能不计补丁；OpenStack gerrit 每补丁约十分钟准备成本压低琐碎量；语义补丁逐文件改千处须先约定模式“必要则一次大爆炸改” `<!-- ROW_MINE: ksummit-discuss.messages.351427 -->`

## 92.21 仅真bug修复记名

- 【Linux社区】Dan Carpenter 提议只有真 bug 修复才获致谢标签（举 Imre 两例对比），“nitpicking 本身即回报” `<!-- ROW_MINE: ksummit-discuss.messages.351428 -->`

## 92.22 Link标签指回讨论

- 【Linux社区】Li Zefan 转述 QA 疑问：讨论要点常不入 changelog，主张维护者更广泛采用 Link: 标签指回邮件讨论 `<!-- ROW_MINE: ksummit-discuss.messages.351429 -->`

## 92.23 逼公司内部辅导

- 【Linux社区】Daniel Vetter 称 checkpatch 造出“漂亮但仍垃圾”补丁，应向惯交垃圾的公司施压内训或出钱请 LF/Linaro；gerrit“有评审流程一切表象却不得要领”；对失控者找经理升级 `<!-- ROW_MINE: ksummit-discuss.messages.351430 -->`

## 92.24 跨子系统局部确认

- 【Linux社区】Christoph Lameter 提议需要标记跨子系统补丁中“slab 部分已认可”之类的局部确认机制，自述常以 slab 维护者身份 ack `<!-- ROW_MINE: ksummit-discuss.messages.351431 -->`

## 92.25 局部Ack书写实践

- 【Linux社区】Laurent 自述回复“For driver/subsystem xyz, Acked-by”；多驱动小改动先拆系列逐个评审再 squash 发 pull request `<!-- ROW_MINE: ksummit-discuss.messages.351432 -->`

## 92.26 topic分支分批收

- 【Linux社区】Tony Luck 提议建 git topic 分支推 kernel.org，先收前 5 个补丁，下轮只审余 25 个；分支可 rebase 但须各方知情 `<!-- ROW_MINE: ksummit-discuss.messages.351433 -->`

## 92.27 标签之别在声誉

- 【Linux社区】hpa 一句定调：Acked-by 语义区分“在冒号右侧”，“It's a matter of reputation” `<!-- ROW_MINE: ksummit-discuss.messages.351434 -->`

## 92.28 stable回归来源析

- 【Linux社区】Josh Boyer 称 stable 回归多来自 trinity/0day 覆盖不到的补丁（背光、设备异常），加测收益有限，“Simply setting expectations” `<!-- ROW_MINE: ksummit-discuss.messages.351435 -->`

## 92.29 拆分squash存险

- 【Linux社区】Christoph Lameter 指“拆分评审后 squash”若只合部分文件会致破坏，相互独立的改动应一开始就分开提交 `<!-- ROW_MINE: ksummit-discuss.messages.351436 -->`

## 92.30 消费电子无视上游

- 【Linux社区】Mark Brown 称消费电子“几乎没人在乎上游”，多沿用 SoC 年代的 Android 内核；仅部分懂行系统集成商施压上游化 `<!-- ROW_MINE: ksummit-discuss.messages.351437 -->`

## 92.31 雇主阻挠正式挂名

- 【Linux社区】Jonathan Cameron 称有人实际承担评审/共同维护职责却因雇主层层管理层不许正式挂名，本人曾亲历 `<!-- ROW_MINE: ksummit-discuss.messages.351438 -->`

## 92.32 commit反查讨论工具

- 【Linux社区】gregkh 指引某研究组约半年前发到 lkml 的工具：可由给定 git commit 反查该补丁的邮件列表讨论 `<!-- ROW_MINE: ksummit-discuss.messages.351439 -->`

## 92.33 块层API议题提案

- 【Linux社区】Daniel Phillips 年度提案讨论“更丰富的块层内部 API”回应 ZFS 派“必破坏 fs/raid 分层”论；自曝动机是为 Tux3 加 Raidz 等价物而不重造 LVM `<!-- ROW_MINE: ksummit-discuss.messages.351440 -->`

## 92.34 议题应去fs峰会

- 【Linux社区】gregkh 反问为何不提给数月前的 filesystem summit，称那才是最佳场合而非 kernel summit；讥“Like btrfs is doing?” `<!-- ROW_MINE: ksummit-discuss.messages.351441 -->`

## 92.35 块层为何非议题

- 【Linux社区】Daniel Phillips 称今年没空参加 fs summit，质疑“电源管理算峰会议题而块层核心不算”；澄清与 btrfs 恰相反 `<!-- ROW_MINE: ksummit-discuss.messages.351442 -->`

## 92.36 PM覆盖全树之辩

- 【Linux社区】gregkh 论断“power management covers the whole tree, the block layer is ‘just’ the block layer”，并促“post patches then” `<!-- ROW_MINE: ksummit-discuss.messages.351443 -->`

## 92.37 ext4保Acked原义

- 【Linux社区】Ted Ts'o 主张保留 Acked-by 原义；ext4 不把临时性 ack 记入 s-o-b 区；Jan、Eric、Lukas 等资深评审的 Reviewed-by 才真正减负 `<!-- ROW_MINE: ksummit-discuss.messages.351444 -->`

## 92.38 LF有通报联系名单

- 【Linux社区】gregkh 称 LF 确有“公司管好自家失控者”的联系名单，找他或 LF 技术委员会即可，“We've done it in the past” `<!-- ROW_MINE: ksummit-discuss.messages.351445 -->`

## 92.39 ARM农场测stable

- 【Linux社区】Olof 称将 Greg 的 stable 队列过自家 ARM 构建器并启动于他与 Kevin Hilman 的 ARM 板场，覆盖有限但保基本 `<!-- ROW_MINE: ksummit-discuss.messages.351446 -->`

## 92.40 块层波及不输PM

- 【Linux社区】Daniel Phillips：块层+内存管理+文件系统+VFS 波及面不小于 PM 且牵动用户可见 API；问“难道要在真空中开发核心 API 扩展？” `<!-- ROW_MINE: ksummit-discuss.messages.351447 -->`

## 92.41 多Link串全版本

- 【Linux社区】Steven Rostedt 赞同 Link: 标签，指版本补丁另起新线程丢上下文，自加多个 Link 指向促成修改的讨论，建议 v5 挂 4 个 Link 链全版本 `<!-- ROW_MINE: ksummit-discuss.messages.351448 -->`

## 92.42 v2应Link回v1

- 【Linux社区】Steven Rostedt 建议 v2 补丁附指向 v1 帖的 Link 标签，便于评审者回查旧批注（答 Laurent 比对自动化之问） `<!-- ROW_MINE: ksummit-discuss.messages.351449 -->`

## 92.43 30个Cc破LKML限

- 【Linux社区】Steven Rostedt 解释横切改动被迫拆 30 个补丁之因：单补丁 30 个 Cc 超过 LKML Cc 上限会被丢弃，拆分仅为每维护者一个 Cc `<!-- ROW_MINE: ksummit-discuss.messages.351450 -->`

## 92.44 另立Supported标签

- 【Linux社区】Rafael Wysocki 提议 Acked-by 保留给维护者，第二义（临时认可）另立“Supported-by”标签 `<!-- ROW_MINE: ksummit-discuss.messages.351451 -->`

## 92.45 流程未坏勿添乱

- 【Linux社区】Olof 质问“到底要修什么”，arm-soc 依 MAINTAINERS 判断求 Ack 对象；改标签名不减尽职调查，也不担心临时 ack 冲突 `<!-- ROW_MINE: ksummit-discuss.messages.351452 -->`

## 92.46 索尼坚持贴主线

- 【Linux社区】Frank Rowand 反驳“消费电子没人在乎上游”：Sony 多年以 -rc1 作新品开发起点，鼓励 SoC 厂商在 mainline 工作 `<!-- ROW_MINE: ksummit-discuss.messages.351453 -->`

## 92.47 为未知问题造流程

- 【Linux社区】gregkh 定性为“为未知问题制造新流程”，质疑年处理 1000+ 补丁的维护者是否真在求援，“我不认为如此” `<!-- ROW_MINE: ksummit-discuss.messages.351455 -->`
