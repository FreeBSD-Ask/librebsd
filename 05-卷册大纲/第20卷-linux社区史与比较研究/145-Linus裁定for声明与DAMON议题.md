145 【Linux社区】Linus裁定for声明与DAMON议题

> 来源：ksummit 独有 p10（50 封全读，2021-04 至 2026-08，Linus 裁定 for 内声明允许而中部不鼓励与语义按行为定义、DAMON KS 议题四点（ABI 稳定化/扩展/精度/调优）、AI 政策按生成比例分档提案、Ralf Jung 澄清别名规则未绑定 LLVM、HCH 力挺 UMN 研究反对学术制裁、Sasha 数据反驳规则将挡 1700+ 人、UALink 英特尔提案 misc/ual 起步、1902 位单提交作者统计）
> 判定：47 CAND / 3 NV。主题分布：VLIW与乱序执行争论 1、UALink上游化议题提案 1、加速器驱动用户态要求 1、工具生成内容文档 4、b4工具链补丁 1、linus-next测试流程 1、稳定分支提交标签 1、Rust内核政策 1、std::string引用计数 1、Rust别名规则归属 1、AI补丁标注 2、Rust类型系统试探 1、Rust能否写全部驱动 1、C++替代路线争论 1、trivial补丁与UMN事件 1、设备直通与fwctl 1、AI评审提示词 1、trivial补丁政策 1、fwctl与netdev之争 1、AI回移补丁讨论 1、gccrs与FFI 1、工具生成内容文档v5 1、dt-bindings与ABI 1、加速器uAPI分层 1、Tree Borrows进展 1、sashiko提示词维护 1、AI线程摘要实验 1、稳定分支autosel 1、Posted/Reviewed标签 1、-next树治理 1、Bugzilla与回归文档 1、Link尾注记法 1、trivial补丁评审工具 1、变量声明位置规则 1、语言语义与优化 1、Message-ID改写之争 1、二分与警告错误 1、Link尾注机制 1、AI政策分档提案 1、Rust驱动争论 1、DAMON议题提案 1、pkeys ABI会议组织 1、bug报告礼节 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p10 的逐封提取（2021-04 至 2026-08，47 CAND / 3 NV），全 43 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 145.1 VLIW与乱序执行争论

- 【Linux社区】Linus 附议 hpa：VLIW 与 OoO 难以兼得，Itanium 是教训，VLIW 仅在 GPU 等可 JIT 的专用场景成立。 `<!-- ROW_MINE: ksummit.messages.1418 -->`

## 145.2 UALink上游化议题提案

- 【Linux社区】英特尔提案 UALink 驱动进内核：drivers/misc/ual 起步、内存语义（dma_buf/HMM/NUMA）、AUX 总线控制面、机密计算与渐进上游策略。 `<!-- ROW_MINE: ksummit.messages.1423 -->`

## 145.3 加速器驱动用户态要求

- 【Linux社区】Rostedt 提议新内核接口一律须附文档与测试套件（哪怕冒烟测试）才可接受，selftests 应随接口更新。 `<!-- ROW_MINE: ksummit.messages.1424 -->`

## 145.4 工具生成内容文档

- 【Linux社区】Lorenzo 反对“LLM 只是另一种工具”：mm 无负面评审即合流易被灌水，主张维护者可凭疑似 AI slop 直接拒收并写明于文档。 `<!-- ROW_MINE: ksummit.messages.1426 -->`
- 【Linux社区】Lorenzo 主张把对工具生成代码的期望集中在单一文档强调，便于向人引用，分散他处易被漏读。 `<!-- ROW_MINE: ksummit.messages.1460 -->`
- 【Linux社区】Rostedt 解释立场：文档应对 checkpatch、sed 与 LLM 一视同仁，担心过度聚焦 AI 致脚本类提交者误以为不适用。 `<!-- ROW_MINE: ksummit.messages.1521 -->`
- 【Linux社区】Hansen 称唯一保留意见是该点前文已覆盖，若众人坚持重复强调也可接受。 `<!-- ROW_MINE: ksummit.messages.1531 -->`

## 145.5 b4工具链补丁

- 【Linux社区】Dan Williams 为“链接尾注存为 git notes”提交 b4 代码补丁（抽取 git_get_rev_diff 复用），属内核流程工具开发记录。 `<!-- ROW_MINE: ksummit.messages.1430 -->`

## 145.6 linus-next测试流程

- 【Linux社区】Rostedt 称自跑 13 小时测试套件，进 rc 后 next 中冲突多与 Linus 树无关，质疑 pull request 再泡 next 一两天的价值。 `<!-- ROW_MINE: ksummit.messages.1435 -->`

## 145.7 稳定分支提交标签

- 【Linux社区】NeilBrown 区分“回归”与“bug”：新功能与文档不符即 bug，修正应打 Fixes，反驳 Carpenter 的“仅限回归”立场。 `<!-- ROW_MINE: ksummit.messages.1438 -->`

## 145.8 Rust内核政策

- 【Linux社区】hpa 提三点异议：Rust 编译器版本要求远松于 C 的十年旧 gcc 标准、目标平台覆盖存疑，并提议评估以 C++14/17 编译整个内核。 `<!-- ROW_MINE: ksummit.messages.1444 -->`

## 145.9 std::string引用计数

- 【Linux社区】Bart 引 LLM 解释并反驳 Laight：std::string 不用引用计数，C++11 已明禁 CoW，属事实纠正。 `<!-- ROW_MINE: ksummit.messages.1452 -->`

## 145.10 Rust别名规则归属

- 【Linux社区】Ralf Jung（Rust 语言组）澄清别名规则并未官方绑定 LLVM，reference 链接只是占位，考虑删除以免显得更依赖 LLVM。 `<!-- ROW_MINE: ksummit.messages.1453 -->`

## 145.11 AI补丁标注

- 【Linux社区】Mark Brown 支持标注所用的 AI 工具（循静态检查器惯例），便于识别有效工具与追踪同一工具的错误模式。 `<!-- ROW_MINE: ksummit.messages.1456 -->`
- 【Linux社区】Dooks 补充建议：标注还应说明 AI 的使用方式并考虑保留输入，便于事后追查。 `<!-- ROW_MINE: ksummit.messages.1514 -->`

## 145.12 Rust类型系统试探

- 【Linux社区】Geert 以代码追问“若无视 Option 直接 let Some(content) 会怎样”，检验 Rust 对解包检查的强制力，自认新手问题。 `<!-- ROW_MINE: ksummit.messages.1457 -->`

## 145.13 Rust能否写全部驱动

- 【Linux社区】Felipe 以黑天鹅谬误反驳 Boqun：已有个别 Rust 驱动不等于全部驱动皆可，社区在未验证的假设下推进。 `<!-- ROW_MINE: ksummit.messages.1458 -->`

## 145.14 C++替代路线争论

- 【Linux社区】Dobriyan 主张 C 弱类型迫使开发者退用更弱的预处理器，模板等更强语言能力正是引入新语言的意义。 `<!-- ROW_MINE: ksummit.messages.1459 -->`

## 145.15 trivial补丁与UMN事件

- 【Linux社区】Hellwig 力挺 UMN 研究：恶意与无能几乎难辨，此“攻击”早该有人做并引发重要讨论，反对学术制裁。 `<!-- ROW_MINE: ksummit.messages.1461 -->`

## 145.16 设备直通与fwctl

- 【Linux社区】Greg KH 强调控制面/慢路径正是内核执行安全与统一抽象之处，反对厂商绕过，网络子系统异议不可无视。 `<!-- ROW_MINE: ksummit.messages.1463 -->`

## 145.17 AI评审提示词

- 【Linux社区】Hemminger 提问是否有人试过让 AI 读历史邮件列表评审来生成未来提示词，属方法试验设想。 `<!-- ROW_MINE: ksummit.messages.1465 -->`

## 145.18 trivial补丁政策

- 【Linux社区】Borntraeger 主张也应接受能清楚解释 bug 成因的修复，条件是经正经评审，不必苦等实际踩雷。 `<!-- ROW_MINE: ksummit.messages.1466 -->`

## 145.19 fwctl与netdev之争

- 【Linux社区】Gunthorpe 反驳：netdev 确在 NAK RDMA/DPDK 所需功能；开放代码非专有，fwctl 管理整设备，拒走 RDMA 后门。 `<!-- ROW_MINE: ksummit.messages.1470 -->`

## 145.20 AI回移补丁讨论

- 【Linux社区】Lorenzo 对 AI 做 stable 回移存疑，称是审查度与错误类别对时间收益的权衡，并邀 Sasha 峰会当面联合讨论。 `<!-- ROW_MINE: ksummit.messages.1473 -->`

## 145.21 gccrs与FFI

- 【Linux社区】Overstreet：若 gccrs 解决架构覆盖问题，Rust 在下的 FFI 更不易错；FFI 边界生命周期陷阱编译器无法告警。 `<!-- ROW_MINE: ksummit.messages.1476 -->`

## 145.22 工具生成内容文档v5

- 【Linux社区】Sasha 用数据反驳拟议规则：v6.12..v6.18 有 1902 位单提交作者（占三分之一）仅 177 人获过 Reviewed-by，规则将挡掉 1700+ 人。 `<!-- ROW_MINE: ksummit.messages.1477 -->`

## 145.23 dt-bindings与ABI

- 【Linux社区】Conor 明确：ack 前须有人完成 ABI 破坏的用户侧适配且不破坏 U-Boot 等 dt-rebasing 用户，解耦内核也不放宽。 `<!-- ROW_MINE: ksummit.messages.1479 -->`

## 145.24 加速器uAPI分层

- 【Linux社区】Vetter 主张按编程模型设计 uAPI：MMIO 型走 drm/sched，嵌入式固定功能走 media 式接口，批评 misc 下 accel 驱动绕过两个子系统评审。 `<!-- ROW_MINE: ksummit.messages.1482 -->`

## 145.25 Tree Borrows进展

- 【Linux社区】Overstreet 评 Tree Borrows 论文远超此前进展，关注是否已推进到 LLVM 兑现优化机会，想看生成代码，并追问 C 侧内存来源工作的下文。 `<!-- ROW_MINE: ksummit.messages.1483 -->`

## 145.26 sashiko提示词维护

- 【Linux社区】Arnaldo 记录 review-prompts 与 sashiko 的提示词同步流程（有 sync 提交为证），并指出 sashiko 已有改动绕过前者。 `<!-- ROW_MINE: ksummit.messages.1492 -->`

## 145.27 AI线程摘要实验

- 【Linux社区】Mauro 分享本地 ollama 摘要实验：提示词设计、线程分组与 VRAM 瓶颈，主张 AI 逐封摘要再以非 AI 方式聚类的混合路线。 `<!-- ROW_MINE: ksummit.messages.1496 -->`

## 145.28 稳定分支autosel

- 【Linux社区】Sasha 引旧统计反驳：autosel 补丁回归率低于带 cc:stable 者，autosel 已延迟三四周，并要求给出具体实例。 `<!-- ROW_MINE: ksummit.messages.1497 -->`

## 145.29 Posted/Reviewed标签

- 【Linux社区】Carpenter 附议 b4 时代 message-id 有用，建议 patchwork 自动补加该链接。 `<!-- ROW_MINE: ksummit.messages.1499 -->`

## 145.30 -next树治理

- 【Linux社区】Reding 提议把 linux-next 经验固化为 git 钩子/脚本（pre-push 自动检查）与文档，兜底请 Linus 合并时把关。 `<!-- ROW_MINE: ksummit.messages.1505 -->`

## 145.31 Bugzilla与回归文档

- 【Linux社区】Leemhuis 支持做 bisect 包装器，并要求覆盖 localmodconfig、稳定树二分与浅克隆指引。 `<!-- ROW_MINE: ksummit.messages.1506 -->`

## 145.32 Link尾注记法

- 【Linux社区】Kees 用 git log 统计反驳“# ”记法：1687 条带方括号链接中 1546 条无“# ”，仅 83 条采用。 `<!-- ROW_MINE: ksummit.messages.1507 -->`

## 145.33 trivial补丁评审工具

- 【Linux社区】Mauro 推荐用 wdiff 评审重命名类补丁，补 rename_rev.pl 之外的实用经验。 `<!-- ROW_MINE: ksummit.messages.1508 -->`

## 145.34 变量声明位置规则

- 【Linux社区】Linus 裁定 for 循环内声明已广泛使用（3k+ 处）应允许，中部声明原则上不鼓励，唯 cleanup 与 __auto_type 等场景例外。 `<!-- ROW_MINE: ksummit.messages.1511 -->`

## 145.35 语言语义与优化

- 【Linux社区】Linus 主张语言语义应按“行为”而非“语法/类型”定义，痛陈 C 标准背离 volatile 传统，指内存访问重物化是安全与正确性大患。 `<!-- ROW_MINE: ksummit.messages.1512 -->`

## 145.36 Message-ID改写之争

- 【Linux社区】Linus 否决 Paolo 用 sed 钩子把 Message-ID 改写为 Link：应改用 git am -l 从源头修正，防脚本捏造不存在的链接。 `<!-- ROW_MINE: ksummit.messages.1525 -->`

## 145.37 二分与警告错误

- 【Linux社区】Segher 以 KCFLAGS 纠正 Rostedt：二分旧内核加 -Wno-error 无需大改构建系统。 `<!-- ROW_MINE: ksummit.messages.1534 -->`

## 145.38 Link尾注机制

- 【Linux社区】Bottomley 说明 --pretty=raw 加 grep 即可脚本化提取 message-id，主张机制改造与内容增补分开讨论。 `<!-- ROW_MINE: ksummit.messages.1536 -->`

## 145.39 AI政策分档提案

- 【Linux社区】Lorenzo 提案按 LLM 生成比例（90%/30%）分档加标签、MAINTAINERS 逐条 opt-in、豁免日常辅助用法，并警示勿借此批量灌补丁。 `<!-- ROW_MINE: ksummit.messages.1538 -->`

## 145.40 Rust驱动争论

- 【Linux社区】Airlie 反驳：称“并非所有驱动能用 C 写”同样荒谬，除非限定 100% safe Rust，而那并非目标。 `<!-- ROW_MINE: ksummit.messages.1540 -->`

## 145.41 DAMON议题提案

- 【Linux社区】SeongJae 提交 Kernel Summit 议题：DAMON ABI 稳定化、扩展用法、精度改进、内核/用户态调优策略等子题。 `<!-- ROW_MINE: ksummit.messages.1542 -->`

## 145.42 pkeys ABI会议组织

- 【Linux社区】Bottomley 指导 pkeys 议题改投 BoF：提交入口轨道选择、两阶段录取与 A/V 安排，属会议组织记录。 `<!-- ROW_MINE: ksummit.messages.1551 -->`

## 145.43 bug报告礼节

- 【Linux社区】Ted Ts'o 阐述 bug 跟踪礼节：分开立 bug、事实与猜想分离（有本事就交补丁）、网页表单用户缺乏经验过滤，狗堆式跟帖坑维护者。 `<!-- ROW_MINE: ksummit.messages.1555 -->`
