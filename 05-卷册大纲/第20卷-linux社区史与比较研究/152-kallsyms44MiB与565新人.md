152 【Linux社区】kallsyms44MiB与565新人

> 来源：ksummit 独有 p16（50 封全读，2021-04 至 2026-08，kallsyms 行号 RFC 全文（+44MiB/崩溃路径免分配免 IO）、GPU merge criteria 作大棒阻断 dump-and-run、7.2 创纪录 565 首次贡献者与迎新机制提案、韦氏年度词汇 slop 论证、Linus OSS 峰会 eBPF 表态转述、相机 ISP 换子系统逃避文档义务举证、Wine/VMware 曾受 PAGE_OFFSET 影响）
> 判定：45 CAND / 5 NV。主题分布：Rust policy 2、LLM 与审查 1、cdev 生命周期竞态 1、Bugzilla 与邮件 7、设备直通 3、kallsyms 行号信息 1、C 聚合传参 2、内核可持续性 1、Rust for Linux 4、LLM 标签 1、stable 邮件量 1、工具生成内容文档 5、AI 与 LLM 角色 1、regzbot RFC 回应 1、内核文档工具链 1、eBPF 边界 1、stable 标签 1、TAB 选举 1、HIGHMEM 淘汰 2、LLM 与维护者 1、kernel.org 工具 1、AI 标注 1、Link 标签 1、THE REST 列表 2、内核 malloc 1、新贡献者洪峰 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p16 的逐封提取（2021-04 至 2026-08，45 CAND / 5 NV），全 26 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 152.1 Rust 内核政策

- 【Linux社区】技术反驳 C++ 路线：g++ 要求 C99 初始化器按声明序且不支持 __seg_gs，采用会致代码质量倒退。 `<!-- ROW_MINE: ksummit.messages.2417 -->`
- 【Linux社区】限定 Kees 的“新代码用 Rust”为“新驱动”，强调 guard() 等 C 语言增强依旧重要。 `<!-- ROW_MINE: ksummit.messages.2567 -->`

## 152.2 LLM 与审查

- 【Linux社区】实测 16GB 显卡上 Qwen-3.6 35B 等小模型可查出真实回移植缺陷，附审查 agent 与渲染工具仓库链接。 `<!-- ROW_MINE: ksummit.messages.2419 -->`

## 152.3 cdev 生命周期竞态

- 【Linux社区】说明 USB GPIO 扩展器热拔时并发 ioctl 可在 gpio_chip 置空前漏过的竞态场景。 `<!-- ROW_MINE: ksummit.messages.2425 -->`

## 152.4 Bugzilla 与邮件

- 【Linux社区】立场：opt-out 类通知形同垃圾邮件，tracker 或更便利用户但不可强制开发者使用。 `<!-- ROW_MINE: ksummit.messages.2432 -->`
- 【Linux社区】主张 bugzilla 应默认 opt-out，用邮件量数据对比驳斥对通知量的夸大担忧。 `<!-- ROW_MINE: ksummit.messages.2447 -->`
- 【Linux社区】系统论证 bugzilla 在加入讨论、大附件、检索、定向回复上全面优于邮件线程。 `<!-- ROW_MINE: ksummit.messages.2460 -->`
- 【Linux社区】提出报告辅助应用、报告文档改进、内核测试者社区与社区经理等优先于联络员的路线。 `<!-- ROW_MINE: ksummit.messages.2489 -->`
- 【Linux社区】事实反驳：Linus 系因 bugzilla CC 邮件相助而非通过邮件列表，重申邮件模式难以为继。 `<!-- ROW_MINE: ksummit.messages.2533 -->`
- 【Linux社区】论证多数用户不会读 reporting-issues 文档，LKML 高音量必然淹没求助信息。 `<!-- ROW_MINE: ksummit.messages.2552 -->`
- 【Linux社区】论证邮件核心缺陷在无法追踪状态，主张先建流程再谈工具，bugzilla 可作过渡载体。 `<!-- ROW_MINE: ksummit.messages.2560 -->`

## 152.5 设备直通

- 【Linux社区】反驳“正常工作流”可以定义，支持 UAPI 暴露的一切须有开源对应实现的要求。 `<!-- ROW_MINE: ksummit.messages.2433 -->`
- 【Linux社区】主张默认信任子系统维护者把关，举证相机 ISP 厂商换子系统以逃避固件接口文档义务。 `<!-- ROW_MINE: ksummit.messages.2504 -->`
- 【Linux社区】论胡萝卜优于大棒：permissive 生态亦获回馈，市场力量自筛选值得逆向工程的设备。 `<!-- ROW_MINE: ksummit.messages.2565 -->`

## 152.6 kallsyms 行号信息

- 【Linux社区】完整 RFC 补丁：构建期从 DWARF 生成地址到 file:line 查找表，栈回溯直接带行号，实测镜像增 44MiB。 `<!-- ROW_MINE: ksummit.messages.2439 -->`

## 152.7 C 聚合传参

- 【Linux社区】补充 C 标准语义论点：编译器可合法把写入替换为读-检查-写序列，呼应 WRITE_ONCE 讨论。 `<!-- ROW_MINE: ksummit.messages.2440 -->`
- 【Linux社区】长文论证 time crate 破坏源于 stdlib 而非语言、内核无递归依赖之痛，并以 C23 对比 editions。 `<!-- ROW_MINE: ksummit.messages.2529 -->`

## 152.8 内核可持续性

- 【Linux社区】论述 GPU merge criteria 以开源用户空间要求为大棒阻断厂商 dump-and-run，属集体性可持续机制。 `<!-- ROW_MINE: ksummit.messages.2442 -->`

## 152.9 Rust for Linux

- 【Linux社区】提议以 virtio 设备作 Rust 驱动示范，阐述 TDX/SEV 等机密虚拟化防恶意设备的真实需求。 `<!-- ROW_MINE: ksummit.messages.2455 -->`
- 【Linux社区】评价 PL061 Rust 驱动直观易维护，追问 gpio 类封装与 RAII guard、下划线惯用法细节。 `<!-- ROW_MINE: ksummit.messages.2485 -->`
- 【Linux社区】报告 GCC Rust 前端项目已启动并采用 LLVM 加 GCC 混合方案，m68k 等架构支持在途。 `<!-- ROW_MINE: ksummit.messages.2502 -->`
- 【Linux社区】答疑：dev_* 打印设施暂缺将补齐，CamelCase 遵循 Rust 官方命名指南且当前强制。 `<!-- ROW_MINE: ksummit.messages.2564 -->`

## 152.10 LLM 标签

- 【Linux社区】提案 assisted-by 作为补丁脚注（同 base-commit 模式），承诺在 b4 落地并写入 AGENTS.md。 `<!-- ROW_MINE: ksummit.messages.2458 -->`

## 152.11 stable 邮件量

- 【Linux社区】提案合并逐版本 stable 通知为摘要邮件，指出 AUTOSEL、排队、rc 测试多批冗余。 `<!-- ROW_MINE: ksummit.messages.2461 -->`

## 152.12 工具生成内容文档

- 【Linux社区】审查记录：nit 指出句号缺失并给出正式 Reviewed-by 标签。 `<!-- ROW_MINE: ksummit.messages.2463 -->`
- 【Linux社区】主张疑似 AI slop 的补丁集应整体即刻拒收，核心要求是每补丁发出前必经人审。 `<!-- ROW_MINE: ksummit.messages.2477 -->`
- 【Linux社区】引韦氏词典 2025 年度词汇与主流媒体报道，论证“slop”一词广为人知可用。 `<!-- ROW_MINE: ksummit.messages.2490 -->`
- 【Linux社区】质疑 AI 输出属非人类创作不可版权的定论，指出其依赖人类作品训练不同于猴子自拍案。 `<!-- ROW_MINE: ksummit.messages.2511 -->`
- 【Linux社区】论证社区须明确表态而非暧昧措辞，引 Phoronix 与 Register 报道说明立场的社会影响。 `<!-- ROW_MINE: ksummit.messages.2528 -->`

## 152.13 AI 与 LLM 角色

- 【Linux社区】反驳 hpa：文档与代码同等需要严谨，AI 生成的隐晦错误文档同样有害。 `<!-- ROW_MINE: ksummit.messages.2493 -->`

## 152.14 regzbot RFC 回应

- 【Linux社区】提出 regzbot 保持自治并作为 KCIDB 邮件提交接口的协作架构，避免工具重复建设。 `<!-- ROW_MINE: ksummit.messages.2495 -->`

## 152.15 内核文档工具链

- 【Linux社区】交代 python 3.6 兼容补丁系列取舍，Leap15 与 RHEL8 受影响，决定权交 Corbet。 `<!-- ROW_MINE: ksummit.messages.2508 -->`

## 152.16 eBPF 边界

- 【Linux社区】转述 Linus 在 OSS 峰会对 eBPF 的表态，论证 eBPF 非用户 API 及维护者被动担责的风险。 `<!-- ROW_MINE: ksummit.messages.2519 -->`

## 152.17 stable 标签

- 【Linux社区】单句事实反驳：Ted 提议的主动询问维护者正是 AUTOSEL 现行做法。 `<!-- ROW_MINE: ksummit.messages.2522 -->`

## 152.18 TAB 选举

- 【Linux社区】治理流程记录：2022 TAB 选举提名截止、投票资格与 CIVS 投票方式通知。 `<!-- ROW_MINE: ksummit.messages.2531 -->`

## 152.19 HIGHMEM 淘汰

- 【Linux社区】主题提案：盘点各架构遗留 highmem 用户并给出两年七步分阶段淘汰时间表。 `<!-- ROW_MINE: ksummit.messages.2535 -->`
- 【Linux社区】提供历史佐证：x86 上 Wine 与 VMware 曾受 PAGE_OFFSET 非常规取值影响但早已修复。 `<!-- ROW_MINE: ksummit.messages.2559 -->`

## 152.20 LLM 与维护者

- 【Linux社区】澄清与 Laurent 的“矛盾”质疑：AI 是工具非依赖，举证 CVE 流程基础设施大量由 AI 构建。 `<!-- ROW_MINE: ksummit.messages.2540 -->`

## 152.21 kernel.org 工具

- 【Linux社区】提案以 lore URL 关联状态标记实现 bug 追踪与 patchwork 替代的轻量方案。 `<!-- ROW_MINE: ksummit.messages.2543 -->`

## 152.22 AI 标注

- 【Linux社区】反驳 AI 标注或反招讹诈式商业化，同时认可其提前审查与未来法律风险处置价值。 `<!-- ROW_MINE: ksummit.messages.2545 -->`

## 152.23 Link 标签

- 【Linux社区】指出 maintainer-tip.rst 已载明 patch.msgid.link 规范，建议提升为通用文档。 `<!-- ROW_MINE: ksummit.messages.2549 -->`

## 152.24 THE REST 列表

- 【Linux社区】反驳 LKML 无用论：自己日常浏览 LKML，否则须订阅数百个子系统列表。 `<!-- ROW_MINE: ksummit.messages.2550 -->`
- 【Linux社区】说明双列表并行实践：LKML 保讨论可见性，子系统列表保证 patchwork 收录，附 MAINTAINERS 示例。 `<!-- ROW_MINE: ksummit.messages.2554 -->`

## 152.25 内核 malloc

- 【Linux社区】指向自己提交的 devm_ 改造补丁系列，作为“devm 不会永远隐带 GFP_KERNEL”的证据。 `<!-- ROW_MINE: ksummit.messages.2563 -->`

## 152.26 新贡献者洪峰

- 【Linux社区】主题提案：7.2 达 565 名首次贡献者创纪录，提议迎新机器人或专职引导团队。 `<!-- ROW_MINE: ksummit.messages.2566 -->`
