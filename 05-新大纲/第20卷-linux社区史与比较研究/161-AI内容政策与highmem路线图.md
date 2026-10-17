# 161 【Linux社区】AI内容政策与highmem路线图

> 来源：ksummit 独有 p25（50 封全读，2021-07 至 2026-08：Arnd 提出 highmem 分阶段退役路线图先删 HIGHPTE 按类别 Kconfig 细分与 ASI 复用 kmap；Dave Chinner 一手立场 syzbot 模糊测试不等于可安全解析不可信镜像并系统批评内核缺功能 EOL 流程；Miguel Ojeda 阐明 Rust 内核政策核心立场安全抽象包裹不安全代码；Mauro 对 Sashiko AI 审查最完整一手回应附 77k kernel-doc 警告 AI 清理提案；AI 内容政策五封、Link 标签改革五封、C 内存模型语义三封）
> 判定：43 CAND / 7 NV。主题分布：HIGHMEM 退役 3、维护者峰会定位 2、AI 内容政策 4、驱动 probe 语义 2、Link 标签改革 5、C 内存模型语义 3、文档构建噪声 2、维护者倦怠 1、AI 代码审查 4、DRM 面板现代化 1、Bugzilla 存废 1、文件系统维护信任 3、字符串函数文档 1、内核 malloc 提案 1、项目决策惯性 1、文档工具链改进 1、AI bug 分诊 2、Rust 内核政策 1、稳定分支标签 1、静态分析检查 1、相机 ISP 争论 1、pkeys ABI 讨论 1、文档组织与读者 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p25 的逐封提取（2021-07 至 2026-08，43 CAND / 7 NV），全 23 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 161.1 HIGHMEM 退役

- 【Linux社区】Andreas Larsson 称 Gaisler 即将推出支持最高 16GiB DRAM 的新 SoC，LEON sparc32 配置用 36 位物理寻址，若移除 CONFIG_HIGHMEM 将成重大限制。 `<!-- ROW_MINE: ksummit.messages.3849 -->`
- 【Linux社区】Arnd 赞同先删 HIGHPTE（x86 已删仅剩 ARM），提议按类别用 Kconfig 细分 highmem 用户并统计用量，__GFP 位已用 26/32，还关注 kmap 复用做 Spectre 防护的 ASI 工作。 `<!-- ROW_MINE: ksummit.messages.3902 -->`
- 【Linux社区】Linus Walleij 自述 ARM32 4G/4G 分裂原型：把内核编进 VMALLOC 区、仅留 0xf0000000 起 256MB 映射，再借 LPAE 两条翻译表基址寄存器分离内核与用户映射，第二步尚未成功。 `<!-- ROW_MINE: ksummit.messages.3998 -->`

## 161.2 维护者峰会定位

- 【Linux社区】Lorenzo 认同 Airlie 把峰会定性为“Linus 的员工会议”，批评 CFP 宣传与实际不符，建议参会与议题征集分离，并另建全年维护者邮件列表。 `<!-- ROW_MINE: ksummit.messages.3852 -->`
- 【Linux社区】Bottomley 称 MM 须协调约 22 位架构维护者就内部抽象达成共识，且靠 LSF/MM 三天会与 Plumbers MC 疏解，反驳 Rostedt 的 MM“小土豆”说法。 `<!-- ROW_MINE: ksummit.messages.3880 -->`

## 161.3 AI 内容政策

- 【Linux社区】Luis 称 AI 代码已大量合入且无法阻止，法律担忧难持久，预期基础模型终将声明只用宽松许可代码训练；他用 Generated-by 标签是为向维护者明示。 `<!-- ROW_MINE: ksummit.messages.3857 -->`
- 【Linux社区】Lorenzo 提出 LLM 造成提交者与维护者不对称：可批量生成貌似合理的补丁系列，维护者必须能成批拒绝，提交者必须理解补丁每一部分，“我们不收 slop”。 `<!-- ROW_MINE: ksummit.messages.3925 -->`
- 【Linux社区】Dave Hansen 反对把标签设计与政策文档绑定：标签类似 ABI，需生产者与消费者契约且难以撤回，仓促定标签若返工危害更大。 `<!-- ROW_MINE: ksummit.messages.3970 -->`
- 【Linux社区】Lorenzo 与 Hohndel 共识：LLM 使端到端提交无需专业门槛成为可能，社区 slop 明显增多，文档应明确“疑似 AI slop 可径行拒绝”，这是全新局面。 `<!-- ROW_MINE: ksummit.messages.4006 -->`

## 161.4 驱动 probe 语义

- 【Linux社区】Greg KH 主张 probe 失败不应阻止驱动注册，单例设备的失败检查也不应写进驱动，module_init 应只调用子系统注册宏。 `<!-- ROW_MINE: ksummit.messages.3858 -->`
- 【Linux社区】Pinchart 解释 probe 失败只意味着某设备绑定出错而非驱动有错，不应阻止注册，否则一个故障设备会让多实例系统全体失效，此为预期行为。 `<!-- ROW_MINE: ksummit.messages.3950 -->`

## 161.5 Link 标签改革

- 【Linux社区】Leemhuis 发 RFC v2 补丁，提议新增 Reported: 与 Posted: 标签补充 Link:，区分 bug 报告、背景链接与补丁投稿，并改 git 钩子与提交文档。 `<!-- ROW_MINE: ksummit.messages.3859 -->`
- 【Linux社区】Rostedt 展示个人实践：把说明补丁动机的 Link 放在标签区外供人读，标签区内的 Link 由工具自动指向投稿帖，以此区分两类链接。 `<!-- ROW_MINE: ksummit.messages.3889 -->`
- 【Linux社区】Rostedt 为自动添加的 Link 辩护：全有或全无的自动化更实用，封面信逐版链接便于回溯；回应 Linus 对 syzbot Closes 标签的批评，称有些标签本就给机器读。 `<!-- ROW_MINE: ksummit.messages.3914 -->`
- 【Linux社区】Pinchart 主张 trailer 首先为解决问题提供数据，人类可读格式居次；赞成 Rostedt 恢复用链接，提议以 Pulled-from: 标记补丁来源、与讨论链接分开。 `<!-- ROW_MINE: ksummit.messages.3952 -->`
- 【Linux社区】Kees Cook 提议用 git notes 保存 b4 am 来源 URL，在 commit-msg 钩子里跑 b4 dig 比对，不一致时自动补 Link 标签与 FIXME 说明差异原因。 `<!-- ROW_MINE: ksummit.messages.3963 -->`

## 161.6 C 内存模型语义

- 【Linux社区】Linus 回应 Rostedt：合并多次读是安全的（CPU 实际也如此），把一次读拆成多次则不安全；MMIO 例外，这正是 volatile 特殊之处。 `<!-- ROW_MINE: ksummit.messages.3866 -->`
- 【Linux社区】Rostedt 区分两种写法：有锁时读两次无碍；无锁下 if(global>1000) 后再读 global 很可能是 bug，编译器可合法改写为先 READ_ONCE 存寄存器。 `<!-- ROW_MINE: ksummit.messages.3879 -->`
- 【Linux社区】Uecker 认同把数据竞争从 UB 改为“可见旧值或新值”的语义强化，称若编译器已如此行为则标准可改，但须有人提案，且难离 C++ 记忆模型另起炉灶，优化器历史包袱重。 `<!-- ROW_MINE: ksummit.messages.4013 -->`

## 161.7 文档构建噪声

- 【Linux社区】Mauro 列出 htmldocs 四类报错来源，建议 CONFIG_WERROR 时在常规构建跑三个文档检查脚本，实测 i5 笔记本约 8 秒，可消掉 linux-next 约 100 条警告。 `<!-- ROW_MINE: ksummit.messages.3876 -->`
- 【Linux社区】Mauro 实测 kernel-doc -Wall 全树约 33 秒、36965 条警告，allmodconfig 另有约 450 条；提议把现有警告存成基线文件，默认只报新增并按 WERROR 使构建失败。 `<!-- ROW_MINE: ksummit.messages.3990 -->`

## 161.8 维护者倦怠

- 【Linux社区】Jiri Kosina 反对用匿名调查收集子系统反馈，认为被拒稿者天然倾向给负面评价，即使拒得对，匿名结果也难反映真实。 `<!-- ROW_MINE: ksummit.messages.3878 -->`

## 161.9 AI 代码审查

- 【Linux社区】Bottomley 指出 Sashiko 依赖的企业慷慨不是开源代码而是免费 token，一旦断供将“有代码却跑不起”，回应 Bart 关于支持多个 LLM 的说法。 `<!-- ROW_MINE: ksummit.messages.3884 -->`
- 【Linux社区】Mauro 逐条回应 Sashiko 议题：赞成 LTS 评审但先从错误路径检查入手，建议 Coverity 式问题导航界面与开源模型本地化，另提议用 AI 清理 kernel-doc 警告以启用 -Wall。 `<!-- ROW_MINE: ksummit.messages.3886 -->`
- 【Linux社区】Paul McKenney 建议让 AI 读 tools/memory-model 与内存屏障文档以理解 .bell/.cat 文件，称 AI 需要大量背景知识；Mason 的审查提示词已被 BPF CI 采用。 `<!-- ROW_MINE: ksummit.messages.3916 -->`
- 【Linux社区】Bottomley 认为靠提交者自觉跑工具不现实，主张让 0day bot 抓取列表上的 [PATCH] 统一跑 checkpatch 与约定的 AI 审查，但指出推理算力终须有人买单。 `<!-- ROW_MINE: ksummit.messages.3948 -->`

## 161.10 DRM 面板现代化

- 【Linux社区】Armstrong 称面板 IC 厂不出数据手册、驱动靠“一串不透明十六进制命令”，最先进的是他为 SM8550/SM8650 上游的 visionox-vtdr6130，需 SoC、面板、DDIC、整机全链配合。 `<!-- ROW_MINE: ksummit.messages.3895 -->`

## 161.11 Bugzilla 存废

- 【Linux社区】Artem 主张保留 Bugzilla，列三项期望（可 CC 任何人、邮件接口、按组件分类），举 KDE/GCC/Wine 仍在用，自荐做专职 Bugzilla 维护者。 `<!-- ROW_MINE: ksummit.messages.3898 -->`

## 161.12 文件系统维护信任

- 【Linux社区】Jan Kara 称 JFS 维护者 Shaggy 愿废弃且不知有用户；reiserfs 除凶案外还有技术原因：特殊行为易碎、无测试，公告废弃后仅有的两名用户均选择迁移。 `<!-- ROW_MINE: ksummit.messages.3908 -->`
- 【Linux社区】Kent Overstreet 提出借 bcachefs 的 shim 层把约九成代码量的文件系统跑在用户态，目标是让老文件系统（如 reiserfs）以 FUSE 续命，摆脱内核重构破坏并缓解安全问题。 `<!-- ROW_MINE: ksummit.messages.3909 -->`
- 【Linux社区】Chinner 强调 syzbot 模糊测试不能证明文件系统能安全解析不可信镜像，自述 15 年前设计的元数据校验可击败随机位变异，拒绝让 XFS 承担该风险，并指内核缺功能 EOL 流程。 `<!-- ROW_MINE: ksummit.messages.3944 -->`

## 161.13 字符串函数文档

- 【Linux社区】Hellwig 详述找 strscpy 文档失败的过程：lib/string.c 无 kerneldoc、Documentation 仅 deprecated.rst 提及，最终发现文档藏在 fortify-string.h，批评其晦涩。 `<!-- ROW_MINE: ksummit.messages.3911 -->`

## 161.14 内核 malloc 提案

- 【Linux社区】Dobriyan 反对 Wilcox 实现 malloc 的提案：返回 void* 而非 T*，且多用独立 kmemcache 更利于调试。 `<!-- ROW_MINE: ksummit.messages.3933 -->`

## 161.15 项目决策惯性

- 【Linux社区】Bottomley 认为 Linux 决策瘫痪非因体量过大，用户空间 ABI 并非完全不可变，关键是管理变更保兼容，要给 ABI 演进通道而非压制创新。 `<!-- ROW_MINE: ksummit.messages.3934 -->`

## 161.16 文档工具链改进

- 【Linux社区】Corbet 支持把 kernel-doc 移植成带缓存的 Python Sphinx 扩展，自述对文档构建做性能分析，发现 C 域符号列表迭代器被调近 7 亿次，是构建慢的根源之一。 `<!-- ROW_MINE: ksummit.messages.3946 -->`

## 161.17 AI bug 分诊

- 【Linux社区】Bottomley 力挺用 LLM 解码 oops 栈回溯并按内核版本拉取发行版 debuginfo，称 bug 分诊正是 AI 擅长替代的琐事，回击“非确定性”批评，主张先试再下结论。 `<!-- ROW_MINE: ksummit.messages.3951 -->`
- 【Linux社区】Bottomley 建议让 LLM 对定位到的提交构造 revert 或补丁请报告者验证，承认算力付费问题，并提出用 ksymoops 式确定性方法先筛 oops 再交 AI。 `<!-- ROW_MINE: ksummit.messages.3979 -->`

## 161.18 Rust 内核政策

- 【Linux社区】Ojeda 回应 C 委员会的“区域禁 UB”方案：内核需要 Rust 式记忆安全与“安全抽象包裹不安全代码”的能力，这正是 Rust 成功之处，C++ 应学 Safe C++ 而非 Profiles。 `<!-- ROW_MINE: ksummit.messages.3966 -->`

## 161.19 稳定分支标签

- 【Linux社区】Bottomley 反对新增 Improves 标签，指其语义更模糊；提出三条规则：修复必带 Fixes、仅 cc:stable 自动回传、其余事后可申请，并提醒 -rc 合并窗回归例外。 `<!-- ROW_MINE: ksummit.messages.3983 -->`

## 161.20 静态分析检查

- 【Linux社区】Carpenter 展示 ret=frob(); if(!ret) return ret; 的反转条件 bug 模式，称每年仅数个但大型重构补丁无法在每个硬件上测试，此类检查仍有价值。 `<!-- ROW_MINE: ksummit.messages.3985 -->`

## 161.21 相机 ISP 争论

- 【Linux社区】Pinchart 质疑“新 ISP 有数十万参数”的说法，区分 ISP 处理块与控制算法，称专利论利好大厂，并认同“UAPI 暴露者须有开源对应实现”的要求。 `<!-- ROW_MINE: ksummit.messages.3997 -->`

## 161.22 pkeys ABI 讨论

- 【Linux社区】Brodsky 指出 pkeys ABI 对信号、rseq、io_uring worker 等异步内核交互严重欠定义且跨架构不一致，引 Gleixner“全坏了”之语，拟在 LPC 办 BoF 并倾向带 A/V 的正式场次。 `<!-- ROW_MINE: ksummit.messages.4002 -->`

## 161.23 文档组织与读者

- 【Linux社区】Pinchart 称文档对新人不友好，引 Corbet 的教程/操作/解释/参考四分类说现存多为参考型；LF 资助付费写文档的实验已失败，提议月度线上会、IRC 频道等社区建设并劝贡献者多催促。 `<!-- ROW_MINE: ksummit.messages.4007 -->`
