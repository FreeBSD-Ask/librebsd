# 170 【Linux社区】bugzilla改革与Rust别名之争

> 来源：ksummit 独有 p34（50 封全读，2025-08 至 2026-04：Pinchart 与 Bottomley 就用 LLM 解码 oops 堆栈正面交锋主张确定性解码服务并警告让用户运行网上下载的未签名内核；Greg KH 关键论断按数量计内核多数 bug 源于 C 的内存泄漏错误路径清理与返回值检查而这些在 Rust 中不存在；Dan Carpenter 与 Meta Chris Mason 商谈 AI 审查工具协作含 semcode 使 btrfs_search_slot 调用图从约 44.4 万 token 降至 2.5 万实测；UMN 事件当事方确认 media 被回退 29 补丁无恶意代码但 sp8870 确有 bug；bugzilla 改革六封、Rust 别名之争四封、新手洪流应对）
> 判定：47 CAND / 3 NV。主题分布：bugzilla退役 1、UMN补丁风波 1、NVMe拷贝卸载 1、MAINTAINERS分流 2、Rust内核政策 3、linus-next测试树 3、LLM解码堆栈 1、红帽GitLab流程 1、AI生成内容规范 2、bugzilla改革 6、维护者互助组 1、stable邮件精简 1、AI审查工具 1、平凡补丁政策 1、Rust别名之争 4、Link标签改进 1、UALink驱动 1、Rust学习曲线 1、新手洪流应对 1、变量声明规范 2、禁运代码质量 1、闪存低功耗策略 1、回归处理优先级 1、Rust早期讨论 1、Rust构建环境 1、TAB选举 1、设备直通争论 1、folio与mm治理 1、内核malloc提案 1、文件系统维护 1、用户态配套政策 1、AI补丁标注 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p34 的逐封提取（2025-08 至 2026-04，47 CAND / 3 NV），全 32 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 170.1 bugzilla退役

- 【Linux社区】Bottomley解析git-bug架构：bug存于主仓refs/bugs/*、每个bug为独立断链提交树，b4已在用；bridge仅为可移植性（现只有jira）；bug拉取信任模型同代码PR，json风险可控。 `<!-- ROW_MINE: ksummit.messages.5272 -->`

## 170.2 UMN补丁风波

- 【Linux社区】Shuah证实Leon指出的sp8870补丁确有bug（应判err<0而非err），并确认media被回退的29个UMN补丁无恶意代码、多为有效修复。 `<!-- ROW_MINE: ksummit.messages.5275 -->`

## 170.3 NVMe拷贝卸载

- 【Linux社区】三星Selva与Nitesh回应Bottomley：因疫情线下不确定、12月LSF/MM太远而改投LPC推进NVMe SCC拷贝卸载，提案含用户接口、bio链、XCOPY兼容等四问。 `<!-- ROW_MINE: ksummit.messages.5276 -->`

## 170.4 MAINTAINERS分流

- 【Linux社区】Rob Herring回应Kicinski：lei已支持IMAP注入收信，问题在由谁运维服务器；仍有人坚持SMTP直投邮箱，制约“THE REST”分流方案落地。 `<!-- ROW_MINE: ksummit.messages.5284 -->`
- 【Linux社区】Perches自述已退订LKML、几乎不参与讨论，改用lore关键词检索并手动下载线程，佐证“THE REST”改道的现实基础。 `<!-- ROW_MINE: ksummit.messages.5306 -->`

## 170.5 Rust内核政策

- 【Linux社区】Sakkinen称Rust“不难学但难跑”，文档应讲BuildRoot/Yocto/NixOS而非dnf/apt-get；自述收到Rust补丁无法进QA流程，只能“NAK因为无法测试”。 `<!-- ROW_MINE: ksummit.messages.5291 -->`
- 【Linux社区】Greg KH澄清立场：按数量计内核多数bug源于C的内存泄漏、错误路径清理、返回值检查等，Rust中不存在；并承认Rust将来会有自己的新坑。 `<!-- ROW_MINE: ksummit.messages.5338 -->`
- 【Linux社区】Uecker辩护#pragma用于区域属性合理并质疑其影响sparse之因；认同UB“编译警告或运行时陷阱二选一”目标，但应容许static calls等有意利用UB，C23已废旧式声明。 `<!-- ROW_MINE: ksummit.messages.5372 -->`

## 170.6 linus-next测试树

- 【Linux社区】Baerts欢迎linus-next树并追问：PR被Linus拒收后如何处理、抓取是否自动、LKFT与KernelCI结果由谁盯防、误报与flaky测试负担归谁。 `<!-- ROW_MINE: ksummit.messages.5296 -->`
- 【Linux社区】Babka指linux-next已有pending-fixes分支专收维护者热修复，称峰会拟推广此用法；支持Rostedt的PR健康检查机器人设想。 `<!-- ROW_MINE: ksummit.messages.5303 -->`
- 【Linux社区】Levin展示next-analysis机器人输出：McKenney三个RCU提交在linux-next停留6天（直方图3笔），演示PR“烘焙时长”量化方法。 `<!-- ROW_MINE: ksummit.messages.5316 -->`

## 170.7 LLM解码堆栈

- 【Linux社区】Pinchart反驳用LLM解码oops：非确定性工具会产出貌似正确实则无用的回溯，主张与发行版共建确定性解码服务；警告让用户运行网上下载的未签名内核比curl管道sudo更危险。 `<!-- ROW_MINE: ksummit.messages.5299 -->`

## 170.8 红帽GitLab流程

- 【Linux社区】Don Zickus议题（第89号提案）：RHEL流程由PatchWork迁至GitLab，集成CKI强制CI门禁，用webhook自动化并减少邮件、改用CLI工具，附演示。 `<!-- ROW_MINE: ksummit.messages.5302 -->`

## 170.9 AI生成内容规范

- 【Linux社区】Carpenter定义“slop”为量产补丁来不及自查即发出，类比clang-format整驱动重排无人细看；自曝其批量bug报告同样无人阅读。 `<!-- ROW_MINE: ksummit.messages.5304 -->`
- 【Linux社区】Hansen赞同文档考虑Generated-by（其用于Coccinelle与kdevops多年以追踪AI占比）；评估git notes存prompt仍受amend/rebase丢notes之困。 `<!-- ROW_MINE: ksummit.messages.5399 -->`

## 170.10 bugzilla改革

- 【Linux社区】Leemhuis引Red Hat公告：RHEL 9后将仅用issues.redhat.com（Jira），借此反驳继续加大对上游已弃养Bugzilla投入的主张。 `<!-- ROW_MINE: ksummit.messages.5311 -->`
- 【Linux社区】Viro估LKML日流量远超800封，自己仅约1-2%不被未读即删；认为私密邮件仅适用于疑似广泛部署的安全洞，平时应Cc维护者加公开列表。 `<!-- ROW_MINE: ksummit.messages.5352 -->`
- 【Linux社区】Pinchart斥责Tashkinov“讨论纯属浪费时间”之说侮辱义务维护者，称想推进就应亲自领做，折射Bugzilla用户期望与志愿投入的冲突。 `<!-- ROW_MINE: ksummit.messages.5355 -->`
- 【Linux社区】Ryabitsev公布路线：先为bugzilla评论建public-inbox订阅源，再架双向桥替换原生邮件桥；自任前期铺路，后续另议。 `<!-- ROW_MINE: ksummit.messages.5377 -->`
- 【Linux社区】Leemhuis请愿报告者Cc regressions列表并多用Link:标签以减其lei扫描误报；提出仿Debian reportbug的引导式报告应用，并改进bisection与localmodconfig文档。 `<!-- ROW_MINE: ksummit.messages.5382 -->`
- 【Linux社区】Geert逐条以“lore.kernel.org”回应Tashkinov对邮件式bug报告的质疑（加入、搜索、回复皆可解决），称缺的是产出好报告的技能。 `<!-- ROW_MINE: ksummit.messages.5383 -->`

## 170.11 维护者互助组

- 【Linux社区】Rostedt与CoC委员Shuah商榷维护者支持组：不设新邮件列表而是志愿者名单、一对一私密沟通、TAB定准则，旨在防escalation到CoC；并忆CoC缘起与Linus休假。 `<!-- ROW_MINE: ksummit.messages.5318 -->`

## 170.12 stable邮件精简

- 【Linux社区】Rostedt回Iwai：stable误应用罕见且自己从不复查，建议改摘要式通知，希望砍掉“已干净应用”邮件，佐证stable邮件量争议。 `<!-- ROW_MINE: ksummit.messages.5320 -->`

## 170.13 AI审查工具

- 【Linux社区】Carpenter与Mason商谈AI审查工具协作：重复报告是痛点，报Smatch警告前先搜lore；称Smatch跨函数库调用树最佳，semcode使btrfs_search_slot调用图从44万token降至2.5万。 `<!-- ROW_MINE: ksummit.messages.5322 -->`

## 170.14 平凡补丁政策

- 【Linux社区】Mauro论跨子系统kAPI改动应成组合并、各维护者只ack本域部分；并以UMN 190补丁回退系列为例，说明勿打扰无关子系统维护者。 `<!-- ROW_MINE: ksummit.messages.5323 -->`

## 170.15 Rust别名之争

- 【Linux社区】Overstreet回应Torvalds的TOCTOU双读担忧：W^X引用下重新读取只在unsafe中可能出现，届时代码已错并有UB。 `<!-- ROW_MINE: ksummit.messages.5330 -->`
- 【Linux社区】Laight详解C strict aliasing语义与内核no-strict-aliasing缘由，举int拷贝重排double写入、restrict内联失效、同值索引双静态数组等编译器行为实例。 `<!-- ROW_MINE: ksummit.messages.5337 -->`
- 【Linux社区】Lutomirski以C++实践主张用atomic<int>取代volatile表达共享数据意图，已批量迁移旧代码，并荐atomic_ref作类READ_ONCE原语。 `<!-- ROW_MINE: ksummit.messages.5365 -->`
- 【Linux社区】Ventura Jack引Rustonomicon指unsafe Rust别名模型（stacked/tree borrows）仍未定义、处于实验阶段，多来源称其比C更难推理，回应Gary Guo的“更易推”说。 `<!-- ROW_MINE: ksummit.messages.5390 -->`

## 170.16 Link标签改进

- 【Linux社区】Leemhuis提议commit新增Posted:/Reported:标签以消除Link:歧义，服务其regzbot回归机器人；记录Konstantin的井号标注替代案与DRM误用References:等乱象。 `<!-- ROW_MINE: ksummit.messages.5331 -->`

## 170.17 UALink驱动

- 【Linux社区】Zohar要求UALink核心驱动从第一天就在各处布好LSM钩子以做完整性保障（如签名验证），回应Intel的drivers/misc/ual提案。 `<!-- ROW_MINE: ksummit.messages.5332 -->`

## 170.18 Rust学习曲线

- 【Linux社区】Bottomley论Rust的“反C偏见”（类型、调用、可变性皆刻意异于C）抬高学习曲线但可逾越，主张不必等更C-like的安全语言，先做Rust实验。 `<!-- ROW_MINE: ksummit.messages.5335 -->`

## 170.19 新手洪流应对

- 【Linux社区】Shuah支持Ryabitsev把新手欢迎机器人做成全项目服务，认可纯确定性检查清单：base-commit、Signed-off-by、可应用、非LTS基线。 `<!-- ROW_MINE: ksummit.messages.5336 -->`

## 170.20 变量声明规范

- 【Linux社区】Anvin与Torvalds敲定变量声明cleanup.h补丁集在合并窗口提交，Linus认可其为改进并接受，唯一非机械转换系维护者要求。 `<!-- ROW_MINE: ksummit.messages.5340 -->`
- 【Linux社区】Anvin指宏中typeof(x)极易写错变量而危险，支持“更清晰或更安全才用类型推导”准则，呼应Torvalds拟以#define auto启用__auto_type。 `<!-- ROW_MINE: ksummit.messages.5369 -->`

## 170.21 禁运代码质量

- 【Linux社区】Hansen认同禁运代码开发如“绑着一只手”，披露Intel内部经0day测试但结果未入合并材料、承诺改进；指硬件安全团队文档已允许吸纳测试者。 `<!-- ROW_MINE: ksummit.messages.5342 -->`

## 170.22 闪存低功耗策略

- 【Linux社区】Hansson议题：NVMe/UFS/eMMC/SD闪存设备能耗占比高，但各子系统低功耗策略不一（最深省电与全程供电并存），呼吁寻找共同政策。 `<!-- ROW_MINE: ksummit.messages.5346 -->`

## 170.23 回归处理优先级

- 【Linux社区】Leemhuis解释“下个周日主线修复”目标源于Linus周日发-rc：修复合入宜在周中而非周一，以免Arch、openSUSE Tumbleweed等滚动发行版多带一周回归。 `<!-- ROW_MINE: ksummit.messages.5361 -->`

## 170.24 Rust早期讨论

- 【Linux社区】Ojeda反驳Greg的kref需锁论：维护引用计数本身无需锁，可用顺序一致性原子变量构造（低效）反例，属2021年Rust for Linux峰会争论。 `<!-- ROW_MINE: ksummit.messages.5367 -->`

## 170.25 Rust构建环境

- 【Linux社区】Sakkinen发布codeberg的linux-tpmdd-nixos环境，用nix-prefetch-git与podman-compose构建，拟扩展支持Rust内核，称内核文档中QA指引为零。 `<!-- ROW_MINE: ksummit.messages.5368 -->`

## 170.26 TAB选举

- 【Linux社区】Berg就TAB选举质询计票口径：提交数分散在多个邮箱者难以自判；Laura Abbott承认3-49票区间才申请纸质选票的说明易混淆并承诺改进。 `<!-- ROW_MINE: ksummit.messages.5370 -->`

## 170.27 设备直通争论

- 【Linux社区】Gunthorpe论CXL fabric manager“安全靠接线”不可靠，Linux获得物理硬件即应有权操作；以IB的umad容器类比，主张为fabric管理划清fwctl边界。 `<!-- ROW_MINE: ksummit.messages.5379 -->`

## 170.28 folio与mm治理

- 【Linux社区】Morton回应Ts'o：承认偶尔学Dave Miller强推补丁，但folio之争各方论据均属实质、尚未到强推地步，折射mm子系统宽松治理风格。 `<!-- ROW_MINE: ksummit.messages.5384 -->`

## 170.29 内核malloc提案

- 【Linux社区】Anvin反对Wilcox“实现malloc”议题：写内核必须懂GFP标志与内存分配，称“内核先是内存管理器，其次才是调度器，其余皆注脚”。 `<!-- ROW_MINE: ksummit.messages.5387 -->`

## 170.30 文件系统维护

- 【Linux社区】Sanjaya称无人维护的文件系统处于悬置状态，追问是否为少数用户无限保留弃用API、如何把用户转化为开发者维护者、是否需akpm介入。 `<!-- ROW_MINE: ksummit.messages.5389 -->`

## 170.31 用户态配套政策

- 【Linux社区】Mauro论新内核API政策：若要求发行版先收用户态包将死锁（其身为Fedora维护者会拒绝未定API），支持Pinchart按子系统定多重准入标准，以CAN与ASIL为例。 `<!-- ROW_MINE: ksummit.messages.5394 -->`

## 170.32 AI补丁标注

- 【Linux社区】Mauro与Rostedt辩AI代码版权：引Berne公约与fair use，指“The quick brown fox”约1885年已过保护期，K&R一代人重复书中代码模式实难主张侵权。 `<!-- ROW_MINE: ksummit.messages.5404 -->`
