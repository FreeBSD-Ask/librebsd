# 190. Linus 拒收 pull 真实标准、LLM 用户三类论与 AI 助手文档争议图谱（ks p54）

> 来源：ksummit 独有 p54（50 封全读，2021-04 至 2026-07：Linus 一手详述拒收 pull 的真实标准九成九构建失败在提交方与最常见拒绝理由是内容根本不喜欢；Howlett 把 LLM 用户分三类并称 Assisted-by 标签信噪比趋零 Corbet 提及新人几乎当上 lib 维护者；Levin 给出 v6.12-rc4 至 rc5 共 110 个提交绕过 linux-next 的直方图实测系 linus-next 提案关键量化证据；Koolstra 系统汇总 2026 年 AI 助手文档四项争议标签存废用途标注新人降级措辞强化一封即掌握全 thread 分歧图谱；AI 标签政策五封、Rust 系六封）
> 判定：47 CAND / 3 NV。主题分布：AI 审查工具 2、Sashiko AI 审查 2、补丁收件人策略 1、内核日志级别 1、selftests 集成 1、AI 标签政策 5、TAB 选举 1、LLM 缺陷定位 1、malloc API 之辩 1、堆栈行号调试 1、字符串 API 之争 1、Bugzilla 改革 2、文件系统维护信任 2、stable 标签规则 2、Rust 别名规则 1、Rust 补丁测试 1、linus-next 预检 1、lore 检索 1、Rust 内核政策 1、合并树层级 1、静态分析注记 1、工具生成内容规范 2、Link 标签改革 1、C 编译器行为 2、NVMe 拷贝卸载 1、峰会议题流程 1、Linus 拉取准则 1、设备直通开放性 1、Rust GPIO 驱动 1、C 风格改进 1、文档构建环境 1、Rust 安全论证 1、Rust LPC 提案 1、代码风格规则 1、pkeys ABI 1、LLM 审查负担 1。

## 190.1 AI 审查工具

- 【Linux社区】Arnaldo 赞同 Lunn 主张审查自动化工具应面向全体开发者而非仅维护者，称竞争性工具多点使用更能在维护者介入前拦截问题，b4 预检可省去维护者步骤。 `<!-- ROW_MINE: ksummit.messages.8380 -->`
- 【Linux社区】Kozlowski 支持 Mason 的 AI 审查提示词已接入 BPF CI，介绍 Qualcomm 开源 PatchWise 并在内部对全部补丁发前预审，称可插拔多引擎缓解雇主要求顾虑，亦利新手学习提交规范。 `<!-- ROW_MINE: ksummit.messages.8407 -->`

## 190.2 Sashiko AI 审查

- 【Linux社区】Gushchin 考虑建预存缺陷库使问题仅报一次并支持误报标记；Gunthorpe 想要 syzkaller 式看板与催办邮件；提示词入库受合并窗口节奏掣肘、需 Linus 支持，并拟依人工反馈半自动改进。 `<!-- ROW_MINE: ksummit.messages.8389 -->`
- 【Linux社区】Torokhov 支持预存缺陷库，并建议审查报告分两节：一节严格限于补丁本体（含 all clear），另一节冠以“分析中发现的预存问题、随意处理”集中列出，减少维护者噪音。 `<!-- ROW_MINE: ksummit.messages.8437 -->`

## 190.3 补丁收件人策略

- 【Linux社区】明尼苏达事件后 trivial 补丁政策讨论中，Romanovsky 批评精心筛选 To/Cc 使反馈割裂成孤岛，Chehab 辩称收件人差异源于 get_maintainer.pl，Leon 回应 b4 重构线程仍解不了孤岛问题。 `<!-- ROW_MINE: ksummit.messages.8393 -->`

## 190.4 内核日志级别

- 【Linux社区】Iwai 回应 dmesg 密语式报错之惑：内核无法判定缺陷最终影响是两难根源，ACPI 日志过吵、部分 err 可降级，主张为 KERN_ERR 级别制定更清晰准则。 `<!-- ROW_MINE: ksummit.messages.8395 -->`

## 190.5 selftests 集成

- 【Linux社区】Pinchart 指出 Mesa 与 libcamera 对所支持设备已有成套测试，就其能否及如何与内核 selftests 集成提出疑问，坦言尚无成熟做法。 `<!-- ROW_MINE: ksummit.messages.8396 -->`

## 190.6 AI 标签政策

- 【Linux社区】Koolstra 汇总 AI 助手文档争议供峰会讨论：Layton 提议废除 Assisted-by 而 Greg KH 反对，Hildenbrand 建议标注 LLM 具体用途，Stoakes 质疑新人疑似 LLM 深度改动可否降级处理。 `<!-- ROW_MINE: ksummit.messages.8398 -->`
- 【Linux社区】Kozlowski 提议以 Legal-risk-by 类标签明示 AI 补丁的法律风险，McKenney 建议带此类标签的补丁干脆不要合入，因多起 AI 训练版权诉讼未决、各国立法走向难料。 `<!-- ROW_MINE: ksummit.messages.8414 -->`
- 【Linux社区】Bottomley 以版权溯源立论：Signed-off-by 本为防 SCO 式指控而设，美国版权局对生成式 AI 的立场使 AI 使用影响补丁版权状态，git 树须留永久记录，且只需标 AI 写码而非 AI 审查。 `<!-- ROW_MINE: ksummit.messages.8430 -->`
- 【Linux社区】Howlett 分 LLM 用户为三类并称 Assisted-by 信噪比趋零，冒用 LLM 者反复重发使他想设超时禁投规则；预言工具由圈地转向变现时社区生产力下滑；Corbet 提及有新人几乎当上 lib/ 维护者。 `<!-- ROW_MINE: ksummit.messages.8488 -->`
- 【Linux社区】Luck 提议两条规则：禁止 AI 代理直接提交、From 必须为真人且对内容负全责；McKenney 指若要求训练集许可兼容则现有主流 AI 无一合格；Anvin 认为须寻求正式法律意见。 `<!-- ROW_MINE: ksummit.messages.8499 -->`

## 190.7 TAB 选举

- 【Linux社区】Corbet 公告 2024 年 TAB 选举：9 月 20 至 27 日经 CIVS 改选 5 席，Brauner、Cook、Hansen、Kicinski、Williams 任期届满；资格为 2023 年起 3 个带 tag 提交，满 50 个自动寄票。 `<!-- ROW_MINE: ksummit.messages.8401 -->`

## 190.8 LLM 缺陷定位

- 【Linux社区】Levin 详述其 LLM 堆栈分析：读源码、翻 git 历史定位肇事提交、搜 lore 找旧报告并自动抄送相关开发者，主张与确定性工具并用；Pinchart 忧虑非确定方法产出貌似合理的错误结果。 `<!-- ROW_MINE: ksummit.messages.8406 -->`

## 190.9 malloc API 之辩

- 【Linux社区】Carpenter 反驳 Wilcox 对 GFP 参数的批评，指如今多数开发者已改用 kzmalloc_obj() 无需再传 GFP_KERNEL，佐证语义化分配接口已被广泛采用。 `<!-- ROW_MINE: ksummit.messages.8411 -->`

## 190.10 堆栈行号调试

- 【Linux社区】Deller 实测 CONFIG_KALLSYMS_LINEINFO 在 parisc 架构正常工作并望合入，Levin 随即提交加入模块支持与他人建议内存优化的正式补丁系列。 `<!-- ROW_MINE: ksummit.messages.8412 -->`

## 190.11 字符串 API 之争

- 【Linux社区】Tarreau 支持指针加长度字符串，实测把 strcmp 链改为 isteq 后 -O3 提速约 10 倍、-O2 约 5 倍，长度已知可免去中间检查，赞同 Hellwig 推崇的 seq_buf 路线。 `<!-- ROW_MINE: ksummit.messages.8413 -->`

## 190.12 Bugzilla 改革

- 【Linux社区】Tashkinov 力主保留 bugzilla：多数开发者从未注册致报告无人看，提议组件与 Kconfig 同步、amdgpu/i915 等自动转投自有追踪器、默认加入可退订，并批评邮件列表同样失灵。 `<!-- ROW_MINE: ksummit.messages.8418 -->`
- 【Linux社区】Ryabitsev 透露 bugzilla 平台近死：开发停滞、不兼容新 MySQL、靠迁 Postgres 勉强撑过 2022，LF 非开发机构且 bugmaster 易倦怠；Tashkinov 提议 git.kernel.org 等合并为 gitlab.kernel.org。 `<!-- ROW_MINE: ksummit.messages.8434 -->`

## 190.13 文件系统维护信任

- 【Linux社区】Hellwig 反对以只读保留无人维护的文件系统，称现有测试设施对只读完全失效，还需测试框架、公开共享镜像或镜像生成工具，成本相当可观。 `<!-- ROW_MINE: ksummit.messages.8420 -->`
- 【Linux社区】Roeck 给出 ntfs3 可靠损坏复现：qemu 快照内 64M 镜像反复 cp、rm 序列，rm 报目录非空、umount 触发回溯或崩溃；镜像 md5 校验、只读保存以排除干扰，回应 Sanjaya 质疑。 `<!-- ROW_MINE: ksummit.messages.8453 -->`

## 190.14 stable 标签规则

- 【Linux社区】前 git 时代 Fixes 标注之争：Bottomley 主张引 tglx history 树哈希，Carpenter 称会令众人困惑，Greg KH 附和说此类哈希使其回溯脚本报错跳过，殃及 stable 回移植判断。 `<!-- ROW_MINE: ksummit.messages.8429 -->`
- 【Linux社区】Belloni 反驳以奖惩促开发者标 Cc: stable：多数贡献者与维护者根本不关心 stable，行为无关好坏，惩罚框架不成立。 `<!-- ROW_MINE: ksummit.messages.8444 -->`

## 190.15 Rust 别名规则

- 【Linux社区】Jack 担忧 Rust 别名规则官方绑定 LLVM、缺独立规范，恐妨碍 gccrs 实现一致行为；并引文档指出原子操作沿袭 C++20 内存模型、panic 底层近乎 C++ 异常，加大 unsafe 难度。 `<!-- ROW_MINE: ksummit.messages.8433 -->`

## 190.16 Rust 补丁测试

- 【Linux社区】Sakkinen 指 Rust DMA 补丁无测试载荷应自动 NAK，Feng 核实其仅有一个不会执行的函数定义式 doc test，说明 Rust 代码本可用 kunit 跑 doctest，同意必须补测试。 `<!-- ROW_MINE: ksummit.messages.8436 -->`

## 190.17 linus-next 预检

- 【Linux社区】Levin 公布 v6.12-rc4 至 rc5 提交在 linux-next 停留直方图：89 个 0 天、21 个不足 1 天，即 110 个提交未经 -next 直入 Linus 树，主张 linus-next 补上绕过测试的漏洞。 `<!-- ROW_MINE: ksummit.messages.8439 -->`

## 190.18 lore 检索

- 【Linux社区】Ryabitsev 答复 Lawall：lkml.kernel.org/r/<msgid> 仅重定向至 lore.kernel.org/all/ 聚合检索，THE REST 改投新列表不影响按 message_id 或主题追溯补丁讨论。 `<!-- ROW_MINE: ksummit.messages.8441 -->`

## 190.19 Rust 内核政策

- 【Linux社区】Anvin 拆分四议题：Rust 与 C 成熟度差距拖累 C 维护者、政策文件“无并行代码”说法需引证；主张用 C++ 等成熟工具立即改进 3500 万行既有代码，并赌 2050 年内核仍有大量 C。 `<!-- ROW_MINE: ksummit.messages.8442 -->`

## 190.20 合并树层级

- 【Linux社区】Rostedt 以 rtla 为例：让 Bristot 自管分支并直接写 pull request，自己只审总体思路、快进合并后转发 Linus，以此反驳 Kosina “不减少上层工作量”之说。 `<!-- ROW_MINE: ksummit.messages.8443 -->`

## 190.21 静态分析注记

- 【Linux社区】指针返回值注记讨论：Bergmann 归纳四类返回约定，Geert 补 optional 第五类；Lawall 质疑“调用者之错”论，统计逾 230 个文件存在同返 NULL 与 ERR_PTR 的函数并举例 ovl_lookup_inode。 `<!-- ROW_MINE: ksummit.messages.8450 -->`

## 190.22 工具生成内容规范

- 【Linux社区】Bottomley 与 Stoakes 就 slop 措辞妥协，改写为“结果可能有误，提交者须理解并能为其辩护，否则维护者可整包拒绝”；Stoakes 承认该文档因 Linus 立场恐难合入。 `<!-- ROW_MINE: ksummit.messages.8451 -->`
- 【Linux社区】Lawall 称维护者凭经验即可识别 checkpatch、Coccinelle、smatch 驱动的补丁并据既往工具经验调整审查，质疑对 AI 生成补丁是否同样奏效。 `<!-- ROW_MINE: ksummit.messages.8510 -->`

## 190.23 Link 标签改革

- 【Linux社区】Bottomley 主张把 Link 之争拆成自动化追踪与人工背景两层；Rostedt 说明自己用脚本把链接放 tags 区供工具用，人类语境链接放 tags 外，且仅当补丁源自另一场讨论时才添加。 `<!-- ROW_MINE: ksummit.messages.8452 -->`

## 190.24 C 编译器行为

- 【Linux社区】Laight 声援 Torvalds：编译器对必然成立仍被要求检查的范围判断照样告警，疑对编译期即死的短路条件也告警，且 _Generic 各分支均须编译，无法规避类型相关误报。 `<!-- ROW_MINE: ksummit.messages.8454 -->`
- 【Linux社区】Rostedt 概括规则：编译器不得超出代码字面多读全局变量，但可缓存既有的多次读；Laight 补充标准允许编译器先向该内存写无关值（如寄存器溢出）再写预期值，gcc 尚未这么做。 `<!-- ROW_MINE: ksummit.messages.8473 -->`

## 190.25 NVMe 拷贝卸载

- 【Linux社区】Selva 提出 LPC 技术议题：NVMe 简单拷贝命令 SCC 的上游实现，待议用户接口取 ioctl、io_uring 操作码还是 copy_file_range，块层用空 bio 链还是带载荷，及 SCSI XCOPY 兼容性。 `<!-- ROW_MINE: ksummit.messages.8455 -->`

## 190.26 峰会议题流程

- 【Linux社区】Kara 认为 richACLs 属技术议题宜投 LSFMM；Rostedt 引 Ted 规则说明 ksummit track 须同时发 [TECH TOPIC] 邮件并在 LPC 网站立项，截止 2025-09-10，CfP 周三关闭。 `<!-- ROW_MINE: ksummit.messages.8456 -->`

## 190.27 Linus 拉取准则

- 【Linux社区】Torvalds 详述拒收实情：构建失败九成九在提交方（未进 linux-next 或无视已报问题），bindgen 仅意外一次；运行期问题常是测试场没有的 GPU、无线硬件；最常见拒绝理由是内容根本不喜欢。 `<!-- ROW_MINE: ksummit.messages.8460 -->`

## 190.28 设备直通开放性

- 【Linux社区】Gunthorpe 以 mlx5 为例：1.2 万行 mlx5_ifc.h、公开编程手册、内核内实现与 DPDK 等开源栈覆盖绝大多数用例，反问为堵一成假想专有用例而在内核加校验、损害技术方案是否值得。 `<!-- ROW_MINE: ksummit.messages.8464 -->`

## 190.29 Rust GPIO 驱动

- 【Linux社区】Walleij 以 GPIO 维护者身份表态愿意尝试 Rust 驱动并引荐搭档 Bartosz，Ojeda 请其挑选带 QEMU 支持或测试套件的型号以便验证，是 Rust 驱动落地最早的维护者互动之一。 `<!-- ROW_MINE: ksummit.messages.8465 -->`

## 190.30 C 风格改进

- 【Linux社区】Greg KH 称内核多数低级错误源自 C 角落案例而在 Rust 中消失；Anvin 主张宏化 alloc、memcpy 的显式尺寸（如其 nasm_new），并多用 C90 起合法的结构体赋值以减少此类错误。 `<!-- ROW_MINE: ksummit.messages.8469 -->`

## 190.31 文档构建环境

- 【Linux社区】Chehab 与 Berg 论文档构建 Python 依赖：openSUSE Leap 的 python3-Sphinx 仅配 Python 3.6、Sphinx 2.3 过旧，RHEL8 同病；Berg 主张只用 python3、过旧即失败，最终交 Corbet 裁决。 `<!-- ROW_MINE: ksummit.messages.8476 -->`

## 190.32 Rust 安全论证

- 【Linux社区】Overstreet 以 Rice 定理解释借用检查器之必然，称消除安全代码 UB 是超越 C 的根本前提，并以 fuse 模块 UAF 迫使 bcachefs fsck 扩展性测试中断一周为例，凸显 C 难复现缺陷的隐性成本。 `<!-- ROW_MINE: ksummit.messages.8486 -->`

## 190.33 Rust LPC 提案

- 【Linux社区】Ojeda 提交 LPC 2023 议题：Rust 支持已随 v6.1 入树，汇报 pinned-init、KUnit doctest 集成、klint 编译期锁规则检查等进展，及稳定版不健全处理与 Rust 版本升级政策，征询维护者接受之道。 `<!-- ROW_MINE: ksummit.messages.8489 -->`

## 190.34 代码风格规则

- 【Linux社区】Laight 反对头文件按字母排序，主张系统、子系统、本地分组，变量声明以易读为先；Bird 指出排序规则本为减少 patch、quilt 应用补丁时的上下文冲突。 `<!-- ROW_MINE: ksummit.messages.8492 -->`

## 190.35 pkeys ABI

- 【Linux社区】Brodsky 指 pkeys ABI 对信号送达、rseq、io_uring 工作线程等异步内核交互严重欠规范、各架构处理不一，引 Gleixner “全都坏了”之评，拟借 LPC Refereed BoF 汇总现状并探求解法。 `<!-- ROW_MINE: ksummit.messages.8498 -->`

## 190.36 LLM 审查负担

- 【Linux社区】Kosina 称曾见 ChatGPT 全写的 GPIO 驱动功能正常却缺错误处理；Reinecke 指内核代码即训练素材、LLM 同样轻视错误处理，九成合格的产物仍须人审，而审查人力本已不足。 `<!-- ROW_MINE: ksummit.messages.8508 -->`
