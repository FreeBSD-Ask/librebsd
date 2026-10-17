# 93 【Linux社区】评审者稀缺与Acked-by论战收束

> 来源：ksummit-discuss p145（50 封全读，2014-05-02 至 2014-05-30，评审者稀缺与 cleanup 新人培养之辩、Acked-by 标签语义论战收束、stable 治理五问、kbuild 配置档、QR oops）
> 判定：43 CAND / 7 NV。主题分布：OpenStack贡献难度对照 1、stable治理五问落地细节 1、核心API不必开会论 1、厂商协作接口障碍 1、实验入上游找共性 1、维护者三职责界定 1、v3.15-rc7维护者清单 1、Acked-by改革提案全文 1、变更率指标之问 1、亚洲开发者评审参与五因 1、Link标签用于stable 1、用例profile与kbuild之惧 1、LTS时限与0day扩展 1、cleanup成产业之忧 1、自清一轮USB经验 1、评审求助开口论 1、cleanup阻断毕业论 1、评审带宽同速增长论 1、块层API归LSF论 1、KS邀请不算R标签 1、拆分评审后squash 1、cleanup评审剥离脚本 1、i915七成R标签实证 1、R标签计入KS邀请 1、修bug防回归激励 1、Foo-by标签信任论 1、Approved-by提案 1、Acked-by语义自述 1、维护者专属标签动机 1、KS遴选重参与度 1、Greg欢迎stable协助 1、评审换来晋升实证 1、新人培养两法 1、射击信使之辩 1、新人做stable回移提案 1、单一测试仓库论 1、QR oops首屏论 1、维护者愿望清单 1、评审新人回移更贵论 1、stable零回归铁律 1、selftests框架三需求 1、Fine-by之议 1、Acked-by无需改定调 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p145（实锚 pk 351456-351505）的逐封提取（43 CAND / 7 NV），全 43 块采用**单行摘要体例**（丙型）：每块由“## 93.x 题名”与若干“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 93.1 OpenStack贡献难度对照

- 【Linux社区】Greg KH 论断 OpenStack 按设计难参与（gerrit 每补丁约十分钟准备）将成其长期问题；全盘易接纳 cleanup 才让社区保持参与、新人易加入——内核不是那样，希望永远不是 `<!-- ROW_MINE: ksummit-discuss.messages.351456 -->`

## 93.2 stable治理五问落地细节

- 【Linux社区】Li Zefan 回 Josh：不能指望子系统维护者像 DaveM 供五线补丁，聚焦更少 LTS 或合理；设想 sub-maintainer 工作流（Greg 脚本发现补丁不能 apply 即通知其手动检查回移）；kernel/sched/rt.c 自 v3.4.. 22 提交仅 2 个 stable 标签；提议 known_issues.txt（举 nfs 容器 oops 数月未修）；指出 backport 缺失或不完整可致灾难故 Trinity/0day 跑 stable 有用 `<!-- ROW_MINE: ksummit-discuss.messages.351457 -->`

## 93.3 核心API不必开会论

- 【Linux社区】Greg KH 回 Phillips：核心 API 扩展照常发补丁等评审，“我们不必为了大型设计决策而开会” `<!-- ROW_MINE: ksummit-discuss.messages.351458 -->`

## 93.4 厂商协作接口障碍

- 【Linux社区】Petersen 指硬件厂商 FOO 不太可能与竞对 BAR 在共同接口上协作；友好协作对 Linux 圈行得通但在驱动空间罕见 `<!-- ROW_MINE: ksummit-discuss.messages.351459 -->`

## 93.5 实验入上游找共性

- 【Linux社区】Dan Williams 提议两家厂商都把“实验”放到上游，社区更有机会找到共性并上提为公共库 `<!-- ROW_MINE: ksummit-discuss.messages.351460 -->`

## 93.6 维护者三职责界定

- 【Linux社区】Walmsley 论维护者与评审者职责不同：批量化补丁解树间冲突发拉取请求、叶子维护者应基本测试发上游的一切、维护者须为其领域设定架构方向 `<!-- ROW_MINE: ksummit-discuss.messages.351461 -->`

## 93.7 v3.15-rc7维护者清单

- 【Linux社区】Walmsley 贴 v3.15-rc7 各子系统维护者数全表（约 470 行）：Intel 网卡驱动十人居首、DT bindings 五人等，以数据支撑评审带宽稀缺论 `<!-- ROW_MINE: ksummit-discuss.messages.351462 -->`

## 93.8 Acked-by改革提案全文

- 【Linux社区】Walmsley 阐明提案仅为澄清 Acked-by 语义：维护者放行改用 Maintainer-acked-by、随意评审并入 Reviewed-by；驳“多流程”质疑；指非维护者定期发 Acked-by 表随意评审是现状 `<!-- ROW_MINE: ksummit-discuss.messages.351464 -->`

## 93.9 变更率指标之问

- 【Linux社区】Walmsley 回 Greg：若“提高变更率”是部分人看重的首要指标，或可解释年复一年讨论增加评审带宽却收效甚微；核心问题是如何鼓励并认可认真评审者——无论爱好者或公司雇员，人都喜欢被正式认可 `<!-- ROW_MINE: ksummit-discuss.messages.351465 -->`

## 93.10 亚洲开发者评审参与五因

- 【Linux社区】Li Zefan 总结华为员工从 cleanup 起步转向 bug 修复但难进评审的五因：自信不足、语言障碍、亚洲文化不爱争论、评审成就感低、内部工作繁忙 `<!-- ROW_MINE: ksummit-discuss.messages.351466 -->`

## 93.11 Link标签用于stable

- 【Linux社区】Li Zefan 支持以 Link 标签指引补丁讨论史：比树外工具更可知晓；stable 提交亦可用以记录回移缘由——若早有此标签 3.4.x 回移工作会更容易 `<!-- ROW_MINE: ksummit-discuss.messages.351467 -->`

## 93.12 用例profile与kbuild之惧

- 【Linux社区】Rostedt 支持 CONFIG_SECURE_ROUTER 式用例配置档；讥 CONFIG_REDUCED_ATTACK_SURFACE 命名糟糕；忆 Linus 曾要 config profiles（CONFIG_FIREWALL/CONFIG_LAPTOP）而无下文，疑 kbuild 太吓人，提议重写或文档化——“每次看那代码都发毛” `<!-- ROW_MINE: ksummit-discuss.messages.351468 -->`

## 93.13 LTS时限与0day扩展

- 【Linux社区】Li Zefan 回 Ben Hutchings：认同 LTS 少于五年难称长期；3.4.x 缺失已补而 3.10.x 无力；提议 0day 框架扩展测试各新 stable 版并检测 LTS 性能回归 `<!-- ROW_MINE: ksummit-discuss.messages.351469 -->`

## 93.14 cleanup成产业之忧

- 【Linux社区】Bottomley 回 Greg：OpenStack 证明适度摩擦是有用的精炼器；cleanup 抢走评审周期的例子即本人；忧 cleanup 自成产业、有人视其为目的本身而非通向实质变更的前奏；接受“清理老驱动可以，条件是你来维护它” `<!-- ROW_MINE: ksummit-discuss.messages.351470 -->`

## 93.15 自清一轮USB经验

- 【Linux社区】Greg KH 回 Bottomley：那就直接拒绝 cleanup（部分维护者正是如此）或谈条件；无人强迫收补丁；建议维护者自己一轮 coding style cleanup 一次清干净——“USB 驱动当年我就这么干” `<!-- ROW_MINE: ksummit-discuss.messages.351471 -->`

## 93.16 评审求助开口论

- 【Linux社区】Greg KH 回 Walmsley：变更率非唯一指标但评审者一直没多也没拖慢开发；自述评审帮助部分自然形成部分主动请求所得，“需要帮助就开口，最坏被拒绝，没有损失” `<!-- ROW_MINE: ksummit-discuss.messages.351472 -->`

## 93.17 cleanup阻断毕业论

- 【Linux社区】Bottomley 论断未见证据表明数百 cleanup 后有人转向实质工作；以 kudos 激励补丁反使其滞留外围——“我们实际在阻止人们毕业”；bug 修复更好：须理解部分代码、小而隔离、引人深入；cleanup 只是推高补丁总量、加剧评审缺口 `<!-- ROW_MINE: ksummit-discuss.messages.351473 -->`

## 93.18 评审带宽同速增长论

- 【Linux社区】Bottomley：若信每补丁须评审，评审带宽须随提交同速增长否则积压；现状补丁数已大幅超过评审者，评审者在合并窗口间清积压但过程精疲力尽，预见倦怠致翻车之期不远 `<!-- ROW_MINE: ksummit-discuss.messages.351474 -->`

## 93.19 块层API归LSF论

- 【Linux社区】Czerner 证言块层 API 讨论已在 LSF 展开（Dave Chinner 提出、尚早期），主张此类讨论属 LSF 而非内核峰会 `<!-- ROW_MINE: ksummit-discuss.messages.351475 -->`

## 93.20 KS邀请不算R标签

- 【Linux社区】Czerner 指评审者在上游社区亦缺认可：KS 邀请预选名单计入 s-o-b 却不计入 reviewed-by `<!-- ROW_MINE: ksummit-discuss.messages.351476 -->`

## 93.21 拆分评审后squash

- 【Linux社区】Pinchart 自述把多驱动简单改动拆为每驱动一补丁的系列、评审后 squash 再发拉取请求的工作流；仅适用于非循环依赖，部分维护者偏好单补丁 `<!-- ROW_MINE: ksummit-discuss.messages.351477 -->`

## 93.22 cleanup评审剥离脚本

- 【Linux社区】Dan Carpenter 公布评审 cleanup 的脚本：剥离空白、注释、括号变更；变量重命名可用 rename_rev.pl 旧名换新名后再比对 `<!-- ROW_MINE: ksummit-discuss.messages.351478 -->`

## 93.23 i915七成R标签实证

- 【Linux社区】Vetter 自报年合并逾千补丁；drm/i915 的 Reviewed-by 覆盖约七成且因“我是个苛刻的人”而攀升，全内核约一成五；“要求评审，评审就会发生” `<!-- ROW_MINE: ksummit-discuss.messages.351479 -->`

## 93.24 R标签计入KS邀请

- 【Linux社区】Jan Kara 澄清 Reviewed-by 在 KS 邀请遴选中被计入，权重甚至高于 s-o-b `<!-- ROW_MINE: ksummit-discuss.messages.351482 -->`

## 93.25 修bug防回归激励

- 【Linux社区】Linville 认可修 bug 令人有动力阻止新 bug；但刷补丁数者或乐于放行小瑕疵再发补丁修正以增计数 `<!-- ROW_MINE: ksummit-discuss.messages.351484 -->`

## 93.26 Foo-by标签信任论

- 【Linux社区】Linville 自述年千补丁维护者；“各种新而区分模糊的 Foo-by 标签让我反胃”，收集合并前贴出的标签很痛苦；标签终究归结为信任——不认识其人则无保证 `<!-- ROW_MINE: ksummit-discuss.messages.351485 -->`

## 93.27 Approved-by提案

- 【Linux社区】Rostedt 提议以 Approved-by 专供维护者，替代打字太长的 Maintainer-acked-by `<!-- ROW_MINE: ksummit-discuss.messages.351486 -->`

## 93.28 Acked-by语义自述

- 【Linux社区】Rostedt 自述以非维护者身份对涉及 tracing 等其涉猎领域的补丁发 Acked-by；Acked-by 不限于维护者而是“与代码打交道并同意者”；Supported-by 易被读成资助；Approved-by 意为“我批准此变更可经他人树合入” `<!-- ROW_MINE: ksummit-discuss.messages.351487 -->`

## 93.29 维护者专属标签动机

- 【Linux社区】Rostedt 阐明提案动机：被 Cc 至仅用其 tracing 基础设施的他子系统补丁时只想确认 tracing 部分正确、不愿被误认该系统维护者；单一 Approved-by 亦便于 Linus 快速核对维护者放行 `<!-- ROW_MINE: ksummit-discuss.messages.351489 -->`

## 93.30 KS遴选重参与度

- 【Linux社区】Rostedt 证言 KS 邀请考量所有社区活动：在自己小子系统交千补丁而不评审他人、不参与内核其余部分者极难受邀 `<!-- ROW_MINE: ksummit-discuss.messages.351490 -->`

## 93.31 Greg欢迎stable协助

- 【Linux社区】Greg KH 正面回应 sub-maintainer 提议：素来欢迎帮助、过去也公开求援；3.4 补丁工作是好例子而自己因出差落后致歉；“若有人想出其他帮助我的方式，我全都支持” `<!-- ROW_MINE: ksummit-discuss.messages.351491 -->`

## 93.32 评审换来晋升实证

- 【Linux社区】mark gross 自述因大量内部代码评审在 Intel 获重要晋升；评审者成为设定优先级与质量度量的领导者、对组织有全局影响——“从世界统治视角这是我推荐给想变得重要者的路径”；斥 Roeck 论点可悲、利润动机失控 `<!-- ROW_MINE: ksummit-discuss.messages.351492 -->`

## 93.33 新人培养两法

- 【Linux社区】Ted Ts'o 自述带新人最有效的两项活动：bug 修复与把补丁前移到新上游内核的 rebase；关键使能是每个提交标注所用自动化测试或手工测试说明；新人从不做空白拼写修复——在做真实价值工作中学工具 `<!-- ROW_MINE: ksummit-discuss.messages.351493 -->`

## 93.34 射击信使之辩

- 【Linux社区】Roeck 回 gross：并未主张不奖励评审，恰恰强烈反对；所述只是观察——许多公司存在不认可评审者的管理问题，须先改变；“报告问题存在”与“问题可悲”是两回事 `<!-- ROW_MINE: ksummit-discuss.messages.351495 -->`

## 93.35 新人做stable回移提案

- 【Linux社区】Ted Ts'o 提议让新人协助手动回移不能自动 apply 的补丁到 stable：单独列表由 patchwork 监控、回移后经子系统批准再入长稳树；宁评审此类真需求补丁也不评审空白补丁；进阶新人可排查未标 cc:stable 的修复 `<!-- ROW_MINE: ksummit-discuss.messages.351496 -->`

## 93.36 单一测试仓库论

- 【Linux社区】Rostedt 赞同不强推统一框架：有一个集中放置测试之处即巨大改进——想跑 ext4 测试应能复刻 Ted 的环境、ftrace 测试应公开并欢迎他人增补；非“make tests”而是标准化与单一仓库展示内核各部分如何被测；不同测试要求不同（root）无一刀切 `<!-- ROW_MINE: ksummit-discuss.messages.351498 -->`

## 93.37 QR oops首屏论

- 【Linux社区】Rostedt 论 QR oops 应记录首个 oops 并忽略后续 dmesg——重要内容滚出控制台；所收截图几乎皆为前序 oops 引发的连带 oops、被判无用 `<!-- ROW_MINE: ksummit-discuss.messages.351499 -->`

## 93.38 维护者愿望清单

- 【Linux社区】Shuah Khan 提议在 kernelnewbies 网站维护维护者与子维护者愿望清单——列出想做而没时间做的任务，为新人指引入门方向 `<!-- ROW_MINE: ksummit-discuss.messages.351500 -->`

## 93.39 评审新人回移更贵论

- 【Linux社区】David Woodhouse 反驳 Ted：评审新人回移常比自做更费工——回移的“明显”答案之后须以代码知识、git 历史核对正确性，新人难做后半；三人合并式复审等于自做一遍 `<!-- ROW_MINE: ksummit-discuss.messages.351501 -->`

## 93.40 stable零回归铁律

- 【Linux社区】Guenter Roeck：对 stable 的预期远高于基线发布，qemu 多架构启动冒烟外仍须运行时测试；“stable 不应引入新 bug，句号”；自述工作环境从不更新内核、每个新 bug 皆成反对更新的弹药（含性能回归），故盼 Fengguang 性能测试覆盖 stable 以证无回归 `<!-- ROW_MINE: ksummit-discuss.messages.351502 -->`

## 93.41 selftests框架三需求

- 【Linux社区】Kees Cook 列接入框架所需：通用报告与退出码处理（如今 make run_tests 靠人读不行）、通用初始状态文档（CONFIG、sysctl、uid 等格式化描述）；预告把 GitHub 上的 seccomp-bpf 测试套件纳入 selftests 树 `<!-- ROW_MINE: ksummit-discuss.messages.351503 -->`

## 93.42 Fine-by之议

- 【Linux社区】Rafael Wysocki 定性非维护者的 Acked-by 近似社交“+1”，望新标签更直白，戏议 Fine-by `<!-- ROW_MINE: ksummit-discuss.messages.351504 -->`

## 93.43 Acked-by无需改定调

- 【Linux社区】Bottomley 以 Bikeshedded-by 等自嘲式戏谑收束标签论战，定调“Acked-by 语义完全清楚，我们不需要新标签” `<!-- ROW_MINE: ksummit-discuss.messages.351505 -->`
