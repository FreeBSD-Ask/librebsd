# 184 【Linux社区】GKI争议与AI政策共识梳理

> 来源：ksummit 独有 p48（50 封全读，2021-06 至 2026-06：Sony 的 Tim Bird 以一手厂商视角批评 Android GKI 与 Google 合同式安排堪称违反 GPL 且 GKI 阻碍运营商认证整改致 Sony 被迫用怪异变通；Sasha Levin 为 2025 维护者峰会系统梳理 AI 政策共识五条分歧四条含一周期约 20% 提交是修复数据；Paul McKenney 披露 rcutorture 对 -next 实测上月一次压出近十个 bug 与 CPU 热插拔间隔 50ms 复现；Pinchart 回应 133 枚积压提交统计自曝漏察 DT 绑定并以 drm-misc 线性历史为反例；AI 补丁文档四封、linux-next 集成四封）
> 判定：44 CAND / 6 NV。主题分布：MAINTAINERS工具 1、Bugzilla退役 1、Rust GPIO绑定 2、Rust内核政策 2、Rust试点驱动 1、静态分析注解 1、Rust部署范围 1、linux-next集成 4、文档工具链 1、Android GKI争议 1、AI补丁文档 4、代码风格之争 1、Rust语言谱系 1、设备直通安全 1、Bugzilla邮件之争 2、回归追踪困境 1、cleanup锁守卫 1、邮件认证方案 1、Rust推广动因 1、机器人审阅设计 1、Rust稳定回移 1、VSOCK性能 1、AI帮忙分诊 1、AI政策共识 1、kallsyms行号压缩 1、checkpatch误报 1、CoC争议 1、维护者所有权 1、MAINTAINERS抄送 1、AWS CVE分诊 1、面板驱动困境 1、栈回溯解码 1、引用与lore 1、C内存模型 1、文件系统维护 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p48 的逐封提取（2021-06 至 2026-06，44 CAND / 6 NV），全 35 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 184.1 MAINTAINERS工具

- 【Linux社区】Lee Jones 拟改 get_maintainer.pl 默认 --git-min-percent 由 5 提至 75%，并采纳 Rob Herring 建议提高 --git-min-signatures，以减少陈年贡献者被误抄送。 `<!-- ROW_MINE: ksummit.messages.7461 -->`

## 184.2 Bugzilla退役

- 【Linux社区】Konstantin 提出以 git-bug/b4 bugs 替代 Bugzilla 并让 LLM 预筛报告；Laurent 质疑是否仍收无 LLM 工具的报告，指缺陷散落 lore、GitHub 等处难检索，并厘清与 regzbot、bugspray 分工。 `<!-- ROW_MINE: ksummit.messages.7462 -->`

## 184.3 Rust GPIO绑定

- 【Linux社区】Linus Walleij 审阅 Wedson 的 PL061 Rust 绑定：主张包装器散布各使用处而非集中 rust 目录（引 OF 教训）；指出用户态接口仍留 C，攻击面未减，Rust 须覆盖内核攻击面才有安全价值。 `<!-- ROW_MINE: ksummit.messages.7470 -->`
- 【Linux社区】Miguel Ojeda 澄清 PL061 绑定中 try_writeb 的运行期检查仅因偏移参数非编译期常量；GPIOIE 等编译期已知处可改用非 try 版本，约三处可简化，体现 Rust API 安全检查取舍。 `<!-- ROW_MINE: ksummit.messages.7569 -->`

## 184.4 Rust内核政策

- 【Linux社区】Askar Safin 回应 hpa：C++ 存在“Safe C++”提案且已在 Circle 编译器实现，但似难被标准接纳；若采用则内核代码将脱离标准 C++，且几乎需重写整个内核。 `<!-- ROW_MINE: ksummit.messages.7473 -->`
- 【Linux社区】Jarkko Sakkinen：Rust 难在运行环境而非语言，文档只讲 dnf/apt 未及 BuildRoot/Yocto/NixOS 交叉编译实战，BuildRoot 缺支持已令其无法贡献；写码仅占内核开发 5%，编辑-编译-运行占 95%。 `<!-- ROW_MINE: ksummit.messages.7584 -->`

## 184.5 Rust试点驱动

- 【Linux社区】Mark Brown 建议除 GPIO 外以 SPI 作 Rust 试点：qemu 已模拟部分 SPI 控制器便于测试，且框架并发场景更多。 `<!-- ROW_MINE: ksummit.messages.7476 -->`

## 184.6 静态分析注解

- 【Linux社区】与 Geert 讨论 optional 资源接口的返回值约定（有效指针、NULL、错误指针）：Arnd 认为运行期由 DTB 决定者无法用注解表达，幸而 struct clk 定义私有、调用方无法解引用。 `<!-- ROW_MINE: ksummit.messages.7477 -->`

## 184.7 Rust部署范围

- 【Linux社区】Ted Tso 称直面攻击面须全内核重写 Rust；驱动因 fuzz 难覆盖、作者资历浅而更值得 Rust 化；ksmbd 改写需大量 unsafe 调 C，其方案是“坚决不用”，重安全者可用 Samba/Ganesha。 `<!-- ROW_MINE: ksummit.messages.7481 -->`

## 184.8 linux-next集成

- 【Linux社区】Michael Ellerman 力挺 linux-next：停留一两天可获数千项覆盖几乎全部架构的编译测试与数百次启动测试，#ifdef 中一个字符的笔误也会被拦下。 `<!-- ROW_MINE: ksummit.messages.7484 -->`
- 【Linux社区】Sasha Levin：维护者常提前一两周发下一周期 PR，6.13 的 PR 已入 linus-next，有人未过本地测试即推 -next；但 Linus 一贯拉取未曝光补丁且反对强制 linux-next，预检机器人难有实效。 `<!-- ROW_MINE: ksummit.messages.7516 -->`
- 【Linux社区】Paul McKenney：Linus 曾在 ARM 峰会要求抄送 -next 失败但自动化只通知树主；rcutorture 压测 -next 平日通过，上月一次揪出近十个 bug 含两枚 heisenbug；一 RCU 主线 bug 需 CPU 热插拔间隔 50 毫秒复现。 `<!-- ROW_MINE: ksummit.messages.7535 -->`
- 【Linux社区】回应 Kozlowski 的 133 枚积压提交统计：Laurent 承认曾因此漏察 DT 绑定集成问题；转述 Linus 不喜子系统树多合并之说，以 drm-misc 线性历史为反例；愿树入 next 但忧媒体子系统 cherry-pick 其 PR。 `<!-- ROW_MINE: ksummit.messages.7599 -->`

## 184.9 文档工具链

- 【Linux社区】Mauro 提议 kernel-doc 在 Python<3.11 时自动改用 PATH 中更新版本：make htmldocs 需 ≥3.7 否则失败，OpenSUSE Leap 与 RHEL8 依赖 python311-sphinx；重跑近零成本，可提速 55%-60%。 `<!-- ROW_MINE: ksummit.messages.7492 -->`

## 184.10 Android GKI争议

- 【Linux社区】Sony 的 Tim Bird 反对 GKI：与 Google 的合同式安排堪称违反 GPL；GKI 令索尼无法改内核代码应对运营商认证，致延期与怪异变通；Google 对非头部厂商冷淡，削弱开源可改源码的价值。 `<!-- ROW_MINE: ksummit.messages.7494 -->`

## 184.11 AI补丁文档

- 【Linux社区】工具生成内容指南 v5 讨论：Dave Hansen 认为 Dan Carpenter 的温和措辞是泛泛建议、缺针对性，主张写明维护者可对工具生成内容要求额外测试，已纳入其 v6 草稿。 `<!-- ROW_MINE: ksummit.messages.7495 -->`
- 【Linux社区】Dan Carpenter 自述曾质询提交者“你如何知道这是真的”，对方 v2 竟以引用 AI 幻觉出的规格说明作长篇答复；支持 Dave 的指南，但主张首段直书“勿发 AI 垃圾”。 `<!-- ROW_MINE: ksummit.messages.7532 -->`
- 【Linux社区】James Bottomley：让提交者声明假设与取舍是参与流程的必要条件，但不足以化解 AI 顾虑——历史上不乏一人接管他人补丁集并代为上游辩护的先例。 `<!-- ROW_MINE: ksummit.messages.7573 -->`
- 【Linux社区】Kees Cook 反对现阶段引入 AI 参与度标签：LLM 介入深浅跨度极大，标签必致误导或不准；当前共识是“展示推演”写入提交说明，待实践沉淀出模式后再设标签。 `<!-- ROW_MINE: ksummit.messages.7601 -->`

## 184.12 代码风格之争

- 【Linux社区】James Bottomley 反对把圣诞树变量排序等维护者个人癖好写入通用风格文档：众维护者连排序方向都无共识，不具普适性。 `<!-- ROW_MINE: ksummit.messages.7499 -->`

## 184.13 Rust语言谱系

- 【Linux社区】Linus Walleij 考据：1962 年 Atlas 系统以 ALGOL 方言实现，C 属 ALGOL 一脉；Rust 首个编译器以 OCaml 写就，语法融合工程师偏爱的 ALGOL 族与函数式族，mut 即折中。 `<!-- ROW_MINE: ksummit.messages.7500 -->`

## 184.14 设备直通安全

- 【Linux社区】Jason Gunthorpe 表态：企业今有内部安全激励，鲁莽部署会被研究者以 CVE 与“响亮命名网站”曝光；但内核须向厂商更清晰阐明 Linux 安全模型，因不少做设备侧者不懂基础。 `<!-- ROW_MINE: ksummit.messages.7504 -->`

## 184.15 Bugzilla邮件之争

- 【Linux社区】Willy Tarreau：邮件列表靠数千人集体过滤，重要补丁终会被注意；缺陷跟踪器反给报告者“已受理”错觉；强制 opt-out 订阅必遭拉黑；Bugzilla 每周约 24 份报告，LKML 日均百封多为扫描。 `<!-- ROW_MINE: ksummit.messages.7512 -->`
- 【Linux社区】Greg KH 反对自动订阅开发者收 Bugzilla 通知：必然招致愤怒与过滤拉黑；愿分诊者请自行出工，替他人“报名”绝不可行。 `<!-- ROW_MINE: ksummit.messages.7604 -->`

## 184.16 回归追踪困境

- 【Linux社区】Thorsten 承认无硬数据：大量回归他无从知晓，commit 无法判定是否修回归；DRM 用外部跟踪器致漏报，regzbot 刚可监控；峰会拟只表扬做得好的子系统，差评须先征得当事方同意。 `<!-- ROW_MINE: ksummit.messages.7513 -->`

## 184.17 cleanup锁守卫

- 【Linux社区】Laurent 以 gpio_mockup 代码示例演示 scoped_guard 与 guard(mutex) 精确控制锁作用域，回应 Willy 对“返回时解锁”致锁持有时长失控的担忧。 `<!-- ROW_MINE: ksummit.messages.7514 -->`

## 184.18 邮件认证方案

- 【Linux社区】Konstantin 提出以 DKIM 签名加高随机 Message-Id 加 References 校验让 forge 信任邮件补丁；其 patatt 端到端签名方案受限于普通邮件客户端（尤其网页端）难以采用。 `<!-- ROW_MINE: ksummit.messages.7515 -->`

## 184.19 Rust推广动因

- 【Linux社区】Linus Walleij 阐释 Rust 支持者的隐含前提：新生开发者将更熟 Rust 而视 C 过时（据 StackOverflow“最受喜爱语言”调查），并称新技术推进本靠信念与热情，Unix、C、Linux 皆然。 `<!-- ROW_MINE: ksummit.messages.7519 -->`

## 184.20 机器人审阅设计

- 【Linux社区】Miguel Ojeda 设计审阅机器人：只客观报告问题而不评判是否值得复审，维护者凭报告长度与问题重要性分流；可设“一票否决”项（无 SoB、无许可证、提交说明缺失、格式与编译错误）令其直接要求改版。 `<!-- ROW_MINE: ksummit.messages.7522 -->`

## 184.21 Rust稳定回移

- 【Linux社区】Andrew Lunn 警告 Rust 文件在树内移动会破坏 -stable 的 cherry-pick 回移；不回移则安全修复无法单独提出，unsafe 代码中的漏洞将长期滞留，故文件位置须自始确定。 `<!-- ROW_MINE: ksummit.messages.7531 -->`

## 184.22 VSOCK性能

- 【Linux社区】LPC2023 议题摘要：VSOCK 新增数据报支持，与 virtio 上的 UDP 对比展示高吞吐点对点优势；集成 sockmap 使 eBPF 可动态管理 VSOCK 套接字。 `<!-- ROW_MINE: ksummit.messages.7537 -->`

## 184.23 AI帮忙分诊

- 【Linux社区】James Bottomley：常有 AI 团队问他 AI 如何助 Linux，他首推缺陷报告分诊分类，对方皆以“太难”退缩、怕误分类遭开发者嘲笑；呼吁社区施压促成尝试。 `<!-- ROW_MINE: ksummit.messages.7542 -->`

## 184.24 AI政策共识

- 【Linux社区】Sasha Levin 为维护者峰会梳理 AI 政策：共识含 From 行须人类担责、须披露 AI 参与、子系统自定政策、语言润色不歧视；分歧含错误性质、门槛高低、DCO 法律风险与审阅不对称。 `<!-- ROW_MINE: ksummit.messages.7543 -->`

## 184.25 kallsyms行号压缩

- 【Linux社区】针对 kallsyms 内嵌行号表 +44MiB 开销，Jürgen Groß 提出压缩：按 1000 条分块、块首存起始地址、条目以 lsb128 编码相对偏移与行号，多数仅 1-2 字节，约省一半空间。 `<!-- ROW_MINE: ksummit.messages.7548 -->`

## 184.26 checkpatch误报

- 【Linux社区】Tim Bird：checkpatch.pl 误报多且因维护者口味标准不一，难以强制；主张把无误报检查并入构建，让问题在编码时即暴露而非事后自动化处理返工；改进方案拟东京峰会讨论。 `<!-- ROW_MINE: ksummit.messages.7552 -->`

## 184.27 CoC争议

- 【Linux社区】身为 CoC 委员的 Shuah：多数举报源于对社区讨论方式的误解，皆幕后化解；承认 Linus“buffer cache 很琐碎”言论被 Dave Chinner 公开指违 CoC 属边缘案例；认同借 CoC 压分歧无益。 `<!-- ROW_MINE: ksummit.messages.7558 -->`

## 184.28 维护者所有权

- 【Linux社区】Leon Romanovsky：部分维护者对子系统所有权感过强，致他人缺乏信任、共同责任无从建立；回应“教维护者放手权力”工作坊的玩笑，称须先厘清维护者对公司、社区、开发者各为何义。 `<!-- ROW_MINE: ksummit.messages.7560 -->`

## 184.29 MAINTAINERS抄送

- 【Linux社区】Konstantin 就“THE REST”改指 patches@lists.linux.dev 的 RFC 表态：接受区分“THE REST”（仅无 L: 匹配时触发）与“ALWAYS CC”（全量追加）两种语义的方案。 `<!-- ROW_MINE: ksummit.messages.7562 -->`

## 184.30 AWS CVE分诊

- 【Linux社区】AWS 提案 LPC2026 演讲：内核 2024 年 2 月成为 CNA 后定制内核组织面临 CVE 洪流，将分享两年仓库级分诊经验、NVD/CVSS 与内部评级相关性、回移致回归，及 LTS 补丁速度数据。 `<!-- ROW_MINE: ksummit.messages.7563 -->`

## 184.31 面板驱动困境

- 【Linux社区】Linus Walleij：面板 IC 厂商（Novatek、Ilitek、三星面板部门等）不发数据手册或仅限 NDA，质疑是否有过其直接提交；其 nt35510 伽马驱动仅基于代码投放，无手册无法调曲线，并疑厂商树多为魔法十六进制堆砌。 `<!-- ROW_MINE: ksummit.messages.7585 -->`

## 184.32 栈回溯解码

- 【Linux社区】Linus Torvalds：解析栈回溯无需新设施，debug-info 构建加 scripts/decode_stacktrace.sh 即可把 uart_write+0x1ec/0x240 译为源文件、行号与内联信息，并给出 caif 串口实例，惜知晓者少。 `<!-- ROW_MINE: ksummit.messages.7590 -->`

## 184.33 引用与lore

- 【Linux社区】Linus Torvalds 主张给遗漏者补抄送时用不引用原文的干净回复并附 lore 链接补背景：lore 快而可靠，足以作上下文载体；认同 Andrew 所指“长篇多为引用”之风不可取。 `<!-- ROW_MINE: ksummit.messages.7596 -->`

## 184.34 C内存模型

- 【Linux社区】David Laight 补充 Torvalds 对 C 标准的批评：早期 READ_ONCE 确因生成代码问题而设；volatile 读常致额外寄存器搬运，屏障可阻止读重化；arm32 的 16 位访问偏移受限，恐被拆成两次字节写。 `<!-- ROW_MINE: ksummit.messages.7607 -->`

## 184.35 文件系统维护

- 【Linux社区】Christoph Hellwig 认同无主文件系统政策草案：至少须有可用 mkfs/fsck 并过 fstests，无 mkfs 则无从验证；此类 fs 无需 syzbot 覆盖；支持以 fstype 标志而非配置项标注支持与弃用状态，但承认为之更难。 `<!-- ROW_MINE: ksummit.messages.7609 -->`
