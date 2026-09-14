# 140 【Linux社区】embargo小灶与Folios僵局

> 来源：ksummit 独有 p5（50 封全读，2021-04 至 2026-08，安全 embargo 流程（Android 全合入反对发行版小灶/security@ 独立集体）、Wither Folios BOF 提议请 Linus 裁决、AI 生成内容“无法解释就别提交”两度立场、eBPF 非用户 API 边界声明、Greg 承认举不出被忽略评审意见、fs/buffer.c 254→3152 行实测、lklfuse 全走内核 VFS 隔离、Link 标签 lore 格式更正）
> 判定：46 CAND / 4 NV。主题分布：维护者倦怠与评审责任 1、安全embargo流程 3、峰会议题分诊 1、背光亮度用户空间API 1、trivial补丁政策 1、C语义与UB 1、静态分析错误约定 1、设备直通争议 1、Rust内核政策 4、eBPF边界 1、设备直通 1、内核malloc提案 1、内核文档 1、维护者峰会存废与next树 1、KTODO与引文过滤 1、回归防回退与Link标签 1、stable标签政策 1、AI补丁评审 1、变量声明位置规则 1、trivial补丁与信任体系 1、KTODO工具化 1、Rust for Linux 1、文档构建Python版本 1、Folios进程僵局 1、linux-next合并策略 1、Fixes标签语义 1、AI生成内容准则 3、C聚合传递与VLIW 1、文件系统维护信任 2、linus-next测试工具 1、C聚合传递与Rust别名模型 1、文件系统用户态化 1、Link标签价值 1、内核文档工具链 1、维护者支持小组 1、AI与LLM披露 1、bugzilla退役与AI工具 1、THE REST邮件列表迁移 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p5 的逐封提取（2021-04 至 2026-08，46 CAND / 4 NV），全 38 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 140.1 维护者倦怠与评审责任

- 【Linux社区】认为部分维护者对子系统所有权过强、导致缺乏信任，共同责任制无从建立，回应评审激励讨论。 `<!-- ROW_MINE: ksummit.messages.623 -->`

## 140.2 安全embargo流程

- 【Linux社区】说明security@k.o是独立“集体”不接受雇主指派人员，且其漏洞仅占实际修复的极小部分，敦促发行版解决不更新的根因。 `<!-- ROW_MINE: ksummit.messages.625 -->`
- 【Linux社区】指出大量驱动安全修复从未报security@k.o且作者未必自知，并援引RH/Canonical安全队列积压3个月以上的实例反对“先报发行版”路径。 `<!-- ROW_MINE: ksummit.messages.675 -->`
- 【Linux社区】重申Android等大批用户已正确合入全部修复，反对给少数发行版开“安全子集”小灶制造虚假安全感。 `<!-- ROW_MINE: ksummit.messages.750 -->`

## 140.3 峰会议题分诊

- 【Linux社区】答复Coly Li：richACL属技术议题不适合维护者峰会，建议改投LPC技术track或明春LSFMM，属议题征集引导记录。 `<!-- ROW_MINE: ksummit.messages.627 -->`

## 140.4 背光亮度用户空间API

- 【Linux社区】主张背光子系统仿照thermal在内核内做策略编排（复合背光与环境光传感器），自认突破“策略留在用户空间”教条。 `<!-- ROW_MINE: ksummit.messages.631 -->`

## 140.5 trivial补丁政策

- 【Linux社区】反问可信静态检查器白名单如何扩充，指出新检查器补丁不会被采纳的死锁，属对提案的实质质疑。 `<!-- ROW_MINE: ksummit.messages.634 -->`

## 140.6 C语义与UB

- 【Linux社区】论证C标准不少未定义行为源于兼容奇特CPU（饱和运算、无算术右移、字寻址、NULL非全零），批评UB语义涵盖“抹盘”过宽。 `<!-- ROW_MINE: ksummit.messages.641 -->`

## 140.7 静态分析错误约定

- 【Linux社区】不认同NULL与ERR_PTR混用返回，主张统一用errno并配错误语义文档，属明确技术立场。 `<!-- ROW_MINE: ksummit.messages.642 -->`

## 140.8 设备直通争议

- 【Linux社区】面对Leon“请举出被忽略的技术评审意见”的质问，承认记不得具体内容，记录网络维护者反对直通的争议细节。 `<!-- ROW_MINE: ksummit.messages.645 -->`

## 140.9 Rust内核政策

- 【Linux社区】指出cleanup.h的“类”与锁guard可处理比kfree更复杂的析构场景，反驳goto展开更易读的说法。 `<!-- ROW_MINE: ksummit.messages.653 -->`
- 【Linux社区】赞成采用_cleanup_注解并附cleanup.h链接，同时警告忘记调用no_free_ptr()会带来新一类错误。 `<!-- ROW_MINE: ksummit.messages.672 -->`
- 【Linux社区】逐条反驳hpa：编译器基线收紧是成熟度问题、目标支持暂非阻塞、C++安全化路线已被拒属死路。 `<!-- ROW_MINE: ksummit.messages.746 -->`
- 【Linux社区】建议以树内Documentation/SubmittingRustPatches取代网站“政策”，并举DMA补丁零调用方、无测试负载应自动NAK为例。 `<!-- ROW_MINE: ksummit.messages.800 -->`

## 140.10 eBPF边界

- 【Linux社区】主张eBPF不是用户空间API、不适用“不破坏用户空间”承诺：配置用途可支持，完整设备功能须严审，闭源BPF程序损坏概不负责。 `<!-- ROW_MINE: ksummit.messages.658 -->`

## 140.11 设备直通

- 【Linux社区】纠正“ISP最接近视频编解码”的说法：DRM支持多种编解码，靠命令提交设计把复杂格式解析留在用户空间，内核因此更稳。 `<!-- ROW_MINE: ksummit.messages.674 -->`

## 140.12 内核malloc提案

- 【Linux社区】修正提案焦点：真正主张是GFP标志糟糕、应重设计使绝大多数分配无需GFP，也担忧Rust被迫适配GFP，愿改写议题表述。 `<!-- ROW_MINE: ksummit.messages.676 -->`

## 140.13 内核文档

- 【Linux社区】主张文档若难以在源码树内定位就是设计出了问题，反对依赖构建系统HTML或特定网站查文档。 `<!-- ROW_MINE: ksummit.messages.678 -->`

## 140.14 维护者峰会存废与next树

- 【Linux社区】与Airlie商定恢复cherry-pick加-x，并探讨用dim与rerere缓存为next构建合并fixes的分支、按pending-fixes方式分支出栈。 `<!-- ROW_MINE: ksummit.messages.680 -->`

## 140.15 KTODO与引文过滤

- 【Linux社区】对Linus“引文过多就退信”规则提出边界情况：为补抄送漏抄者需大量引文会被误伤，属对提案的实质追问。 `<!-- ROW_MINE: ksummit.messages.689 -->`

## 140.16 回归防回退与Link标签

- 【Linux社区】更正Link标签格式：整个message-id填入patch.msgid.link与lore链接，属流程规范记录。 `<!-- ROW_MINE: ksummit.messages.691 -->`

## 140.17 stable标签政策

- 【Linux社区】澄清文档化政策：Fixes:非可选、cc:stable仅适用选择加入stable流程的树，未打标的回移请求走stable列表并将改进自动化。 `<!-- ROW_MINE: ksummit.messages.696 -->`

## 140.18 AI补丁评审

- 【Linux社区】主张把AI评审纳入贡献者工具（b4或构建目标）既保留中央管控又降低学习门槛，以“构建-反馈-修复”周期替代“提交-反馈-修复”循环。 `<!-- ROW_MINE: ksummit.messages.700 -->`

## 140.19 变量声明位置规则

- 【Linux社区】主张声明下推到首次初始化可隐式缩小变量作用域、捕捉严重错误，回应cleanup.h变量放置之争。 `<!-- ROW_MINE: ksummit.messages.704 -->`

## 140.20 trivial补丁与信任体系

- 【Linux社区】主张karma在维护者层级内纵横皆有意义（资深子系统维护者跨子系统也更可信），并支持GPG签名补丁交叉签名方向。 `<!-- ROW_MINE: ksummit.messages.705 -->`

## 140.21 KTODO工具化

- 【Linux社区】提议由bugbot把KTODO条目转成bugzilla工单（以社区共识为前提），属具体工具链提案。 `<!-- ROW_MINE: ksummit.messages.707 -->`

## 140.22 Rust for Linux

- 【Linux社区】以PL061 Rust驱动为例连问try_writeb错误处理、resources失败语义与RAII析构时机等实质技术问题。 `<!-- ROW_MINE: ksummit.messages.733 -->`

## 140.23 文档构建Python版本

- 【Linux社区】反对迁就旧Python与多版本探测：只认python3与python3-sphinx、过旧就让它失败，减少移动部件。 `<!-- ROW_MINE: ksummit.messages.738 -->`

## 140.24 Folios进程僵局

- 【Linux社区】提议在维护者峰会时段安排“Wither Folios”LPC BOF并让维护者移场参与，请Linus到场裁决合并前提，属峰会组织提案。 `<!-- ROW_MINE: ksummit.messages.741 -->`

## 140.25 linux-next合并策略

- 【Linux社区】支持子树成对两两合并的提议并建议把最易冲突的树归同组，反馈对linux-next做git bisect时merge base测试点偏多的观察。 `<!-- ROW_MINE: ksummit.messages.753 -->`

## 140.26 Fixes标签语义

- 【Linux社区】论证Fixes指向前驱补丁虽“不公平”但利于评审与回移依赖，无回归就不该打Fixes，回应iwai对git前修复标注的疑虑。 `<!-- ROW_MINE: ksummit.messages.761 -->`

## 140.27 AI生成内容准则

- 【Linux社区】附和Axboe“无法解释就别提交”，并指出提交者大概率会让AI代答，答辩式要求防不住这类提交。 `<!-- ROW_MINE: ksummit.messages.762 -->`
- 【Linux社区】主张维护者本有按带宽拒绝系列的裁量权（无论是否AI生成），社区应允许其随形势调整并可诉诸ksummit。 `<!-- ROW_MINE: ksummit.messages.783 -->`
- 【Linux社区】主张“无法解释就别提交”，明确零兴趣接收提交者自己不理解的代码，属准则立场表达。 `<!-- ROW_MINE: ksummit.messages.798 -->`

## 140.28 C聚合传递与VLIW

- 【Linux社区】应Kent之请补充VLIW历史背景：Transmeta TM5x00以微码把x86转译为内部表示，解释VLIW效率论战由来。 `<!-- ROW_MINE: ksummit.messages.767 -->`

## 140.29 文件系统维护信任

- 【Linux社区】以fs/buffer.c从0.01时代254行增长到今日3152行的实测数据回应“它很小”论，属历史数据点。 `<!-- ROW_MINE: ksummit.messages.768 -->`
- 【Linux社区】解释buffer head保留per-bh b_size的原因在非iomap O_DIRECT路径，若该路径消失即可简化同folio块大小一致的假设。 `<!-- ROW_MINE: ksummit.messages.825 -->`

## 140.30 linus-next测试工具

- 【Linux社区】确认next-analysis直方图可用于回答“补丁在next停留多久”以决定撤出PR或向Linus说明，并追问脚本用法与自建DB之别。 `<!-- ROW_MINE: ksummit.messages.769 -->`

## 140.31 C聚合传递与Rust别名模型

- 【Linux社区】澄清Ventura Jack混用两种“false positives”含义，引Ralf Jung说明Rust无意绑定LLVM别名规则且reference尚非规范。 `<!-- ROW_MINE: ksummit.messages.771 -->`

## 140.32 文件系统用户态化

- 【Linux社区】澄清lklfuse完整重定向到内核VFS路径、近乎零改造即可隔离不可信文件系统镜像，反对每个文件系统各自维护FUSE移植。 `<!-- ROW_MINE: ksummit.messages.773 -->`

## 140.33 Link标签价值

- 【Linux社区】反驳Linus“Link浪费时间”：bisect后循链接可找到提交时还不存在的同类报告与修复，封面信应附讨论与前版链接。 `<!-- ROW_MINE: ksummit.messages.775 -->`

## 140.34 内核文档工具链

- 【Linux社区】拒绝virtualenv要求：文档工具必须来自较新发行版软件包否则一票否决，理由是文档应面向最广泛贡献者。 `<!-- ROW_MINE: ksummit.messages.780 -->`

## 140.35 维护者支持小组

- 【Linux社区】建议压力大的维护者或更愿用视频/IRC而非会被存档的邮件，点出隐私顾虑，属对支持小组方案的实质反馈。 `<!-- ROW_MINE: ksummit.messages.788 -->`

## 140.36 AI与LLM披露

- 【Linux社区】赞同Brown的“written by/translated by”措辞与工具中立表述，主张规则从简、务实、后续再完善。 `<!-- ROW_MINE: ksummit.messages.790 -->`

## 140.37 bugzilla退役与AI工具

- 【Linux社区】反驳“AI会错所以弃用”：人的猜测同样充满看似正确实则错误的推断，主张好猜测可取但须标注，批评“是AI就坏”论调。 `<!-- ROW_MINE: ksummit.messages.803 -->`

## 140.38 THE REST邮件列表迁移

- 【Linux社区】提供镜像public-inbox仓库的具体方法：每日用lore的manifest.js.gz检查新增仓库，配合l2md或自写脚本。 `<!-- ROW_MINE: ksummit.messages.805 -->`
