# 144 【Linux社区】Linus表态与AI诉讼进行时

> 来源：ksummit 独有 p6（50 封全读，2021-04 至 2026-08，Linus 表态维护者峰会圈层化认同讨论存废与 cleanup.h 不加硬规则、mkfs.hfsplus 可用实测反驳不可测试说、AI 生成物法律地位多起诉讼进行时、GitLab reply+uuid 反馈回流机制、Rust 工具链一周一变致二分不可能之限、libmount 全局允许/拒绝列表提议、CREDITS 与 .get_maintainer.ignore 既有覆盖论）
> 判定：42 CAND / 8 NV。主题分布：TAB 选举 CIVS 投票流程 1、stable 提交标记与 AUTOSEL 1、维护者峰会存废 1、trivial 补丁接收政策 1、内核文档方向 1、kernel.org 工具与 Bugzilla 去留 1、linus-next 功能测试 3、回归防止与 Message-id 哲学 1、Link: trailer 文档补丁 1、Rust for Linux 3、文件系统信任与维护 2、内核文档形态 1、Bugzilla 改革与 opt-out 1、AI 辅助代码标注 1、Link: trailer 替换方案 1、Bugzilla 改革与用户报告 1、GitLab 与邮件工作流整合 1、per-cgroup swap 议题归属 1、回归处理时限文档 1、MAINTAINERS 条目校验 1、峰会筹备与疫情讨论边界 1、C 聚合传参（Rust） 5、加速器驱动的用户态要求 1、设备直通之害与跨子系统 NAK 1、Rust 工具链要求 1、AI 补丁审查工具 1、cleanup.h 与变量声明位置 1、TAB 选举流程 1、Rust 内核策略与测试可用性 1、项目延续性文档 1、回归防止四提案 1、稳定树回归预防 1、静态分析想法 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p6 的逐封提取（2021-04 至 2026-08，42 CAND / 8 NV），全 33 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 144.1 TAB 选举 CIVS 投票流程

- 【Linux社区】反馈选举流程痛点：已 opt-in 但未察觉投票已开放，询问是否会再发投票提醒邮件，暴露 opt-in 与投票通知脱节问题。 `<!-- ROW_MINE: ksummit.messages.829 -->`

## 144.2 stable 提交标记与 AUTOSEL

- 【Linux社区】说明自己基本不再手工加 CC，因 AUTOSEL 拾取面更广；婉拒 Greg 将其子系统列入“免跑 AUTOSEL/Fixes”名单的提议，理由是 stable 整体已趋宽松。 `<!-- ROW_MINE: ksummit.messages.831 -->`

## 144.3 维护者峰会存废

- 【Linux社区】Linus 系统表态：早期峰会技术议题普适，如今讨论圈层化；维护者峰会保住了纯维护话题但年年同一批“圈内人”，感觉沉闷，认同把存废作为本届议题讨论。 `<!-- ROW_MINE: ksummit.messages.833 -->`

## 144.4 trivial 补丁接收政策

- 【Linux社区】提出 treewide 补丁抄送难题的可行方案：cover letter 对个人 bcc、对列表 cc，并指出代价是个人回复只会进列表。 `<!-- ROW_MINE: ksummit.messages.841 -->`

## 144.5 内核文档方向

- 【Linux社区】主张按教程、操作、解释、参考四类组织文档，内核文档几乎全是参考型；指出无人专职做文档，LF 资助付费写文档的实验未成。 `<!-- ROW_MINE: ksummit.messages.844 -->`

## 144.6 kernel.org 工具与 Bugzilla 去留

- 【Linux社区】反对轻率弃用 Bugzilla：PCI 子系统重度依赖其收 dmesg/lspci 并回传测试补丁；要求至少在 kernel.org 自有设施提供文件交换，历史条目须永久保留以维持 commit 中 Link: 可用。 `<!-- ROW_MINE: ksummit.messages.847 -->`

## 144.7 linus-next 功能测试

- 【Linux社区】提供事实信息：0-day bot 仍在运行，配置在 github lkp-tests 可自查并 PR 更新；指出 notify_build_success_branch 仅一处设置，故部分分支构建成功不会通知。 `<!-- ROW_MINE: ksummit.messages.853 -->`
- 【Linux社区】区分场景：-rc1 后修复与合并窗口代码不同；自述发送前跑 8-13 小时测试套件；质疑单行修复也须先进 linux-next 的收益。 `<!-- ROW_MINE: ksummit.messages.860 -->`
- 【Linux社区】立场：没有 Linus 在意就理不顺流程；质疑新树延迟未必优于 linux-next，解决不了根本问题。 `<!-- ROW_MINE: ksummit.messages.886 -->`

## 144.8 回归防止与 Message-id 哲学

- 【Linux社区】阐释优先 Message-id 而非 Link 的理由：Message-id 永久不变，lore 若消失仍可检索，而外部 Link 会失效。 `<!-- ROW_MINE: ksummit.messages.856 -->`

## 144.9 Link: trailer 文档补丁

- 【Linux社区】文档维护者询问系列争议焦点“# 注释写法”是否已有结论，并表态可先合入再继续打磨。 `<!-- ROW_MINE: ksummit.messages.859 -->`

## 144.10 Rust for Linux

- 【Linux社区】针对 GPIO irqchip 提出两个具体竞态与清理问题：irq chip 移除时 irq_set_irq_wake 计数如何递减；irq_domain_remove 前如何防止新映射再被加入。 `<!-- ROW_MINE: ksummit.messages.867 -->`
- 【Linux社区】回应 kref 问题：列举 kref_put_mutex、kref_put_lock、klist 与驱动核心持锁调用 kref_put 的实例，解释查找返回引用计数对象为何需外部锁。 `<!-- ROW_MINE: ksummit.messages.925 -->`
- 【Linux社区】质疑驱动先行战略：若收益不在该子系统本身而在试点，须把策略定位与可整体退出的机制讲明并形成共识。 `<!-- ROW_MINE: ksummit.messages.953 -->`

## 144.11 文件系统信任与维护

- 【Linux社区】报告 util-linux 已实现 X-mount.auto-fstypes 白名单；提议给 libmount 增加全局允许/拒绝列表，借用户空间逐步收敛发行版启用的文件系统集合。 `<!-- ROW_MINE: ksummit.messages.872 -->`
- 【Linux社区】用 hfsprogs 实测反驳 hfsplus 在 Linux 上无 mkfs 不可测试的说法：mkfs.hfsplus 可用；另指出 ntfs3 崩溃源自 commit a4f64a300a29。 `<!-- ROW_MINE: ksummit.messages.929 -->`

## 144.12 内核文档形态

- 【Linux社区】提议给代码注释加“设计文档”标记并抽入 Sphinx 文档，或从文档反向引用代码中的标记；理由是贴代码注释比 Documentation/ 下文档更易随设计更新。 `<!-- ROW_MINE: ksummit.messages.879 -->`

## 144.13 Bugzilla 改革与 opt-out

- 【Linux社区】驳斥发件人：定位维护者应查 MAINTAINERS 文件；强烈抨击 opt-out 邮件模式不可接受，类比垃圾邮件与营销部门话术。 `<!-- ROW_MINE: ksummit.messages.885 -->`

## 144.14 AI 辅助代码标注

- 【Linux社区】反驳“法律风险很小”：多起关于 AI 生成材料法律地位的诉讼正在进行。 `<!-- ROW_MINE: ksummit.messages.890 -->`

## 144.15 Link: trailer 替换方案

- 【Linux社区】提出三步收尾计划：维持现状含 patch.msgid.link 自动链接；推动 git 在 commit 头部加入来源信息；峰会再议残余分歧。 `<!-- ROW_MINE: ksummit.messages.891 -->`

## 144.16 Bugzilla 改革与用户报告

- 【Linux社区】认为报告意愿取决于 bug 对报告者的影响程度：致命问题自然有人追，边缘问题沉没无妨；以自己提交显示控制器补丁、其余问题仅进维护者待办为例。 `<!-- ROW_MINE: ksummit.messages.893 -->`

## 144.17 GitLab 与邮件工作流整合

- 【Linux社区】澄清关注点不在验证邮件补丁而在反馈邮件如何回流 forge；介绍 GitLab reply+uuid 个人地址认证机制，愿配合 DKIM 方向解决未认证邮件进 forge 的问题。 `<!-- ROW_MINE: ksummit.messages.896 -->`

## 144.18 per-cgroup swap 议题归属

- 【Linux社区】引用 Ted 的 Kernel Summit 主题征集规则，论证该 MM 提案按规则属 KS 范畴，反驳 Wilcox 应去 LPC/LSFMM 的意见，已补抄 linux-mm。 `<!-- ROW_MINE: ksummit.messages.898 -->`

## 144.19 回归处理时限文档

- 【Linux社区】回应 Jiri 反对强时限：文档刻意用“aim for”弱措辞；目标是把 Linus 帖子背后的规则与相互矛盾过时的文档统一成共识，而非消除拖延。 `<!-- ROW_MINE: ksummit.messages.900 -->`

## 144.20 MAINTAINERS 条目校验

- 【Linux社区】指出既有机制即可覆盖提议：退休者归 CREDITS，免被打扰用 .get_maintainer.ignore，无需新建 RETIRED 文件。 `<!-- ROW_MINE: ksummit.messages.906 -->`

## 144.21 峰会筹备与疫情讨论边界

- 【Linux社区】提请遵守 Konstantin 早先要求：本列表 COVID 讨论仅限对会议差旅的影响，药物争论请自开列表或 IRC。 `<!-- ROW_MINE: ksummit.messages.907 -->`

## 144.22 C 聚合传参（Rust）

- 【Linux社区】论证线程可见性应纳入语言“可观察”语义：重物化加载是 bug；指出 gcc 不重物化 mem 操作、C 标准已禁加宽存储，safe Rust 可因此更激进优化。 `<!-- ROW_MINE: ksummit.messages.910 -->`
- 【Linux社区】深化别名模型讨论：追问能否给出保守的部分规范（stacked/tree borrows 是否只含假阳或假阴），以 Java happens-before 简化模型类比，并对照 C restrict 的实践难度。 `<!-- ROW_MINE: ksummit.messages.926 -->`
- 【Linux社区】以 Stacked/Tree Borrows 监督人身份作答：C 侧 pnvi-ae-udi 模型难成标准；Rust strict provenance 无需后端改动；原始指针可整体退出别名约束；Miri 原理上可查全部 UB，内核代码入 Miri 是合作方向。 `<!-- ROW_MINE: ksummit.messages.935 -->`
- 【Linux社区】反驳 Rust 社区敌视 gccrs 的说法：存在对语言分裂的合理担忧，gccrs 承诺不引入自造扩展以保持与 rustc 兼容，担忧已消解。 `<!-- ROW_MINE: ksummit.messages.985 -->`
- 【Linux社区】澄清约束本质：不能丢的是无替代用例的 C 代码；Rust 抽象层可先行实现；新子系统纯 Rust 化会让缺工具链架构沦为二等公民，宜待 GCC 后端成熟。 `<!-- ROW_MINE: ksummit.messages.991 -->`

## 144.23 加速器驱动的用户态要求

- 【Linux社区】主张考虑内核级政策：无开源用户态则不加内核接口；认为部分厂商不上游的代价可接受且利大于弊；指出“敷衍式开源项目”不算合格用户态。 `<!-- ROW_MINE: ksummit.messages.912 -->`

## 144.24 设备直通之害与跨子系统 NAK

- 【Linux社区】反驳 James 对 LF 产业教育的悲观：LF 持续资助其向各公司（含 James 现雇主）做开放性教育，只是低调；重问跨子系统 NAK 议题应有谁参与。 `<!-- ROW_MINE: ksummit.messages.917 -->`

## 144.25 Rust 工具链要求

- 【Linux社区】以自身 C/Rust 混合项目为例：工具链一周一变使二分近乎不可能；建议明确“十年允许几次要求升级 rust 工具链”的硬性预期。 `<!-- ROW_MINE: ksummit.messages.918 -->`

## 144.26 AI 补丁审查工具

- 【Linux社区】立场：强制贡献者付费或运行专有工具不可接受，专有工具链须在维护者侧运行；警惕 AI 厂商短期赞助导致供应商锁定。 `<!-- ROW_MINE: ksummit.messages.921 -->`

## 144.27 cleanup.h 与变量声明位置

- 【Linux社区】表态：不加硬性规则但倾向在分配处声明 __free 变量；反对无脑批量转换，认可示例中下移声明确实更清晰，关键在 taste。 `<!-- ROW_MINE: ksummit.messages.938 -->`

## 144.28 TAB 选举流程

- 【Linux社区】说明选票 9 月 20 日 9:00 后发出；自曝 Google Apps 群发限额致部分通知可能丢失，明年拟自动化处理阈值判定与通知。 `<!-- ROW_MINE: ksummit.messages.950 -->`

## 144.29 Rust 内核策略与测试可用性

- 【Linux社区】针对跨子系统系列无用户难评审问题，提出发补丁集并附 git 分支（含 QEMU 可模拟驱动等用户）的工作流建议。 `<!-- ROW_MINE: ksummit.messages.958 -->`

## 144.30 项目延续性文档

- 【Linux社区】治理立场：不必穷尽所有坏场景，关键是白纸黑字写明“存在计划”，以破除 LF 藏有秘密遗嘱的猜疑。 `<!-- ROW_MINE: ksummit.messages.970 -->`

## 144.31 回归防止四提案

- 【Linux社区】讨论测试与二分时滞：即便测试快，定位 commit 的二分也常超一天；-next 偶有 rebase 致测试成本高；主张说服 stable 用户群转测 .0 版本。 `<!-- ROW_MINE: ksummit.messages.974 -->`

## 144.32 稳定树回归预防

- 【Linux社区】提出工具化改进：git send-email 知道补丁属于某系列，应在系列内补丁间加交叉引用，便于 stable 识别带 Fixes: 的系列依赖补丁。 `<!-- ROW_MINE: ksummit.messages.975 -->`

## 144.33 静态分析想法

- 【Linux社区】归纳指针返回值四类注记（可空、错误指针、恒有效、编译期禁用时返回不透明 NULL），指出最后一类为内核特有且最易被误用，宜入静态检查器。 `<!-- ROW_MINE: ksummit.messages.982 -->`
