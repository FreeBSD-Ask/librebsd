# 163 【Linux社区】linusnext树创建与trivial政策

> 来源：ksummit 独有 p27（50 封全读，2021-04 至 2026-08：Sasha Levin 宣布创建 linus-next 树只收发往 Linus 的 PR 连续树便于二分且 LKFT/KernelCI 已接入；Greg KH 一手叙述 security@ 改组成效与至少 6 个月专职资助到位及保密限制下只能用本地 LLM 起草补丁；Linus 阐述 API 废弃原则新 API 必须是旧 API 真超集且可自动化转换并举 VFS shared 迭代 2016 引入 2023 才删除；2025 LF TAB 选举行政细节 5 席改选 CIVS 投票 3/50 commit 门槛；trivial 补丁政策四封、设备直通争论三封、UMN 事件反思、UALink 上游路径）
> 判定：47 CAND / 3 NV。主题分布：合并与拣选冲突 1、维护者支持组 1、Rust 补丁评审 1、设备直通争论 3、Bugzilla 报告渠道 1、Fixes 标签语义 2、linus-next 树 4、C 聚合传参 1、文档构建性能 1、trivial 补丁政策 4、Rust 内核政策 2、静态分析指针注解 1、TAB 选举 1、驱动资源生命周期 1、HIGHMEM 退场 1、清理宏政策 2、邮件引用礼仪 1、C 标准化参与 1、devm_kzalloc 危害 1、lei 工具 1、安全流程与AI 1、UMN 事件反思 1、UALink 上游路径 1、禁运代码质量 1、API 废弃强制 1、栈回溯行号 1、stable 邮件减量 1、kernel-doc 工具 1、Rust 驱动安全 1、补丁抄送范围 1、-Werror 争论 1、Bugzilla 退役 1、lore 回复技巧 1、Sashiko 审查 1、2021 峰会议题 1、pkeys ABI 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p27 的逐封提取（2021-04 至 2026-08，47 CAND / 3 NV），全 36 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 163.1 合并与拣选冲突

- 【Linux社区】Brown 批评 DRM 的 cherry-pick 流造成每周多次巨型冲突，是其见过最难跟进的合并区；建议 DRM 的 -next 分支预先合并各 -fixes 与 Linus 树，可用 dim 生成 drm-for-next。 `<!-- ROW_MINE: ksummit.messages.4213 -->`

## 163.2 维护者支持组

- 【Linux社区】Brauner 反对 Rostedt“像有吸毒成员的家庭”类比，称职业环境不宜情绪化比喻；主张支持组只能是 CoC 的补充，两者须明确分开。 `<!-- ROW_MINE: ksummit.messages.4214 -->`

## 163.3 Rust 补丁评审

- 【Linux社区】针对 Rust DMA 补丁“无用户难评审”僵局，Geert 认可两步法：先按现状发系列，再给出含 QEMU 可模拟驱动等测试材料的 git 分支；Airlie 解释跨子系统系列先发无用户版本的无奈。 `<!-- ROW_MINE: ksummit.messages.4216 -->`

## 163.4 设备直通争论

- 【Linux社区】Leon 质疑 Greg KH“网络维护者评审意见被忽视”的说法，要求举出被忽视的技术性评审意见，称自己与 LWN 深度文章均未见此类意见。 `<!-- ROW_MINE: ksummit.messages.4222 -->`
- 【Linux社区】Gunthorpe 解释 fwctl 分歧是哲学性而非政治性：内核应强制多少通用性无共识；配置 flash 与调试固件对开源社区价值甚微。 `<!-- ROW_MINE: ksummit.messages.4245 -->`
- 【Linux社区】Bottomley 引 hidraw 与 FIDO 令牌为例：整类设备无内核驱动，靠 CTAP 规范统一浏览器与 libfido2 用户态实现，证明全新设备类型可免内核驱动。 `<!-- ROW_MINE: ksummit.messages.4268 -->`

## 163.5 Bugzilla 报告渠道

- 【Linux社区】Slade 评 Bugzilla 改版争论：邮件适合讨论不适合报 bug，网页更易导航；任何系统都会有信息遗漏，目标不应是取悦所有人。 `<!-- ROW_MINE: ksummit.messages.4231 -->`

## 163.6 Fixes 标签语义

- 【Linux社区】Bottomley 指 Fixes 标签按 5.Posting 与 stable 规则文档并非可选，但 Linus“随机改进不该引用旧提交”的解读与之冲突，出路或在澄清文档并强制执行。 `<!-- ROW_MINE: ksummit.messages.4244 -->`
- 【Linux社区】Rostedt 统计 git 历史：指向 1da177e4c3f4（Linux-2.6.12-rc2）的 Fixes 标签达 528 次居首，支持 pre-git 补丁也标 Fixes。 `<!-- ROW_MINE: ksummit.messages.4304 -->`

## 163.7 linus-next 树

- 【Linux社区】Levin 宣布创建 linus-next 树：只收发往 Linus 的 PR、连续树便于二分，LKFT 与 KernelCI 已接入测试；回应维护者峰会上 Linus 对拉取前测试质量的担忧。 `<!-- ROW_MINE: ksummit.messages.4248 -->`
- 【Linux社区】Leemhuis 谢绝协助 auto-pending-fixes：自述回归追踪数月无薪、资金无着落；愿写“-fixes 分支永不 rebase”文档并游说维护者建立此类分支。 `<!-- ROW_MINE: ksummit.messages.4258 -->`
- 【Linux社区】Shuah 表示 PR 必先在 linux-next 浸泡两三天，借其发现架构与配置破坏及合并冲突，反驳 Rostedt“在 next 放一两天无价值”论。 `<!-- ROW_MINE: ksummit.messages.4262 -->`
- 【Linux社区】McKenney 表态测试优先级为 RCU、-next、主线；新增 linus-next 树要么无人测试，要么挤占 -next 与主线测试，直指新树的资源代价。 `<!-- ROW_MINE: ksummit.messages.4327 -->`

## 163.8 C 聚合传参

- 【Linux社区】Engelhardt 反驳 Laight 对 C++ 的批评：按值传聚合需深拷贝与析构故各语言都不用；std::move 可避免深拷贝，struct stat x={} 能初始化全部标量成员。 `<!-- ROW_MINE: ksummit.messages.4250 -->`

## 163.9 文档构建性能

- 【Linux社区】Brown 实测 make -j56 htmldocs 耗时 26 分 14 秒（Sphinx 5.3）；Corbet 称 Sphinx 8 修复性能问题后约 3 分钟，建议 venv 安装新版。 `<!-- ROW_MINE: ksummit.messages.4252 -->`

## 163.10 trivial 补丁政策

- 【Linux社区】针对 UMN 事件与媒体子系统 29 补丁回滚，Leon 给出 __pm_runtime_resume 失败时自动递减 usage_count 的补丁，欲根治 57cc666d36ad 一类引用计数错误。 `<!-- ROW_MINE: ksummit.messages.4254 -->`
- 【Linux社区】Brown 称 MFD 与新 SoC 上游常把核心驱动与看似无关的驱动补丁放同一系列，存在构建依赖但评审无重叠，不能一律要求拆分。 `<!-- ROW_MINE: ksummit.messages.4271 -->`
- 【Linux社区】Bottomley 把 UMN 后讨论拆为三题：信任如何生成、bug 修复须附 Fixes 与说明、恢复 trivial 树；认同 Shuah 对抬高新人门槛的担忧。 `<!-- ROW_MINE: ksummit.messages.4291 -->`
- 【Linux社区】Brown 解释 runtime PM API 因合理原因难以用对，Kconfig 关闭会出意外，问题多年已知但在 API 层面不易修复，回应 Leon 对 29 个媒体补丁的质疑。 `<!-- ROW_MINE: ksummit.messages.4344 -->`

## 163.11 Rust 内核政策

- 【Linux社区】Ojeda 否认政策文件含“禁止并行代码”，引 Greg 2023 年“一设备一驱动、勿走回头路”邮件为据，说明其 Rust 参考驱动框架已用于 PHY。 `<!-- ROW_MINE: ksummit.messages.4255 -->`
- 【Linux社区】Ojeda 阐明初期只与愿意维护 Rust 抽象的子系统合作，API 变更只需改抽象层；透露 CONFIG_RUST 终将移除、GCC 构建属权宜，反驳 Leon 的成本论。 `<!-- ROW_MINE: ksummit.messages.4367 -->`

## 163.12 静态分析指针注解

- 【Linux社区】讨论指针返回五类注解（NULL 与 ERR_PTR 组合）；Geert 认同 ovl_lookup_inode 混用属编码错误，但坚持可选资源返回 NULL 能简化时钟、GPIO、复位等处理。 `<!-- ROW_MINE: ksummit.messages.4264 -->`

## 163.13 TAB 选举

- 【Linux社区】Ojeda 发布 2025 TAB 选举更新：改选 5 席，提名至 12 月 13 日，13 至 20 日用 CIVS 投票；2024 年后 3 commit 可投票、50 commit 自动获票，列到期成员名单。 `<!-- ROW_MINE: ksummit.messages.4267 -->`

## 163.14 驱动资源生命周期

- 【Linux社区】Golaszewski 澄清议题聚焦对象所有权与热拔插 use-after-free，将讲 C 自动指针加引用计数的编码模式；cleanup.h 不在本次讨论范围。 `<!-- ROW_MINE: ksummit.messages.4269 -->`

## 163.15 HIGHMEM 退场

- 【Linux社区】Arnd 记述老 Marvell NAS 因 DMA 地址限制低内存分配致数据损坏，树莓派靠 dma-ranges 加 SWIOTLB 加 GFP_DMA 变通；2G/2G 分割曾令 JRE 与浏览器出错。 `<!-- ROW_MINE: ksummit.messages.4273 -->`

## 163.16 清理宏政策

- 【Linux社区】Lunn 透露网络子系统现行政策只允许 scoped_guard，更“魔法”的 cleanup.h 构造被强烈劝阻，数年后视其他子系统成效再评估。 `<!-- ROW_MINE: ksummit.messages.4274 -->`
- 【Linux社区】Tarreau 担心 cleanup 注解易致双重释放与 use-after-free；Bottomley 以 systemd 成功实践反驳，称注解可自动放引用与锁，不应预设失败。 `<!-- ROW_MINE: ksummit.messages.4302 -->`

## 163.17 邮件引用礼仪

- 【Linux社区】回应 Morton 的“引用超 95% 就发 nastygram 机器人”提案，NeilBrown 主张让 MUA 自动压缩引用乃至翻译语言，用工具而非训诫解决礼仪问题。 `<!-- ROW_MINE: ksummit.messages.4279 -->`

## 163.18 C 标准化参与

- 【Linux社区】Uecker 指 ISO C 工作组现无内核开发者积极参与，自述业余修 GCC 无人理；McKenney 称须精挑战场，欢迎更多内核人参与标准工作。 `<!-- ROW_MINE: ksummit.messages.4281 -->`

## 163.19 devm_kzalloc 危害

- 【Linux社区】Pinchart 峰会提案：devm_kzalloc 15 年来逾 6000 处调用，把资源寿命绑到设备绑定，字符设备私有数据会在 release 处理器运行前被释放，拟议技术与流程层对策。 `<!-- ROW_MINE: ksummit.messages.4284 -->`

## 163.20 lei 工具

- 【Linux社区】Ryabitsev 透露计划在 kernel.org 端集中运行 lei 过滤，经只读邮箱向维护者提供预筛数据，绕过 Debian stable 无 lei 的问题。 `<!-- ROW_MINE: ksummit.messages.4285 -->`

## 163.21 安全流程与AI

- 【Linux社区】Greg KH 称 security@ 改组后运转顺畅，将获至少 6 个月资助设专职联系人；因法律限制只能用本地 LLM 起草初版补丁，LLM 分诊无效，真问题是无响应报告者与中间商。 `<!-- ROW_MINE: ksummit.messages.4286 -->`

## 163.22 UMN 事件反思

- 【Linux社区】Pinchart 附议 Gleixner 对内核长期缺人、业界重功能轻正确性的批评，补充驱动层沦为 BSP 倾倒场的问题，主张借鉴 DRM/KMS 机制提高贡献激励。 `<!-- ROW_MINE: ksummit.messages.4295 -->`

## 163.23 UALink 上游路径

- 【Linux社区】Walleij 对 Intel UALink 驱动选址给出意见：试水走 staging，有专注团队则直接 drivers/accel/ual；Sinyuk 认同长期如 CXL 独立成 drivers/ual。 `<!-- ROW_MINE: ksummit.messages.4298 -->`

## 163.24 禁运代码质量

- 【Linux社区】Brown 补充 Sasha 提出的禁运代码准入测试清单：增加 QEMU 平台与固件启动、高质量 kselftest 及 Guenter 的测试，核心是至少冒烟测试。 `<!-- ROW_MINE: ksummit.messages.4310 -->`

## 163.25 API 废弃强制

- 【Linux社区】Torvalds 主张新 API 必须是旧 API 的真超集且可自动化转换，否则“就是垃圾”；举例 VFS shared 迭代 2016 年引入、2023 年才删旧版历时七年多，称 GPIO 改动本可用 coccinelle。 `<!-- ROW_MINE: ksummit.messages.4318 -->`

## 163.26 栈回溯行号

- 【Linux社区】Deller 实测 CONFIG_KALLSYMS_LINEINFO 在 parisc 架构工作良好，栈回溯可直接打印源文件行号，支持在内存优化后合入上游。 `<!-- ROW_MINE: ksummit.messages.4325 -->`

## 163.27 stable 邮件减量

- 【Linux社区】Levin 称当日已把 AUTOSEL 改为按版本范围合并的摘要邮件、主题标注适用树；赞成停发“已入 stable”通知，视其为纯垃圾邮件。 `<!-- ROW_MINE: ksummit.messages.4335 -->`

## 163.28 kernel-doc 工具

- 【Linux社区】Mauro 演示 kernel-doc -Wall 列出 audit.c 十余处缺失返回值文档，建议把 Randy 的 kerndoc-export-search.pl 并入 Python 版 kernel-doc 复用解析数据。 `<!-- ROW_MINE: ksummit.messages.4336 -->`

## 163.29 Rust 驱动安全

- 【Linux社区】Wedson 以 Rust 版 PL061 驱动解释 try_writeb 编译期越界检查、类型安全 drvdata 与可撤销资源加 RCU 守护，消除设备移除后的 use-after-free 竞态。 `<!-- ROW_MINE: ksummit.messages.4338 -->`

## 163.30 补丁抄送范围

- 【Linux社区】Romanovsky 反对“精心筛选收件人”的做法，主张 60 补丁系列即便仅 4 个属 arch 目录也应整系列抄送，以便看到全貌并统一反馈。 `<!-- ROW_MINE: ksummit.messages.4340 -->`

## 163.31 -Werror 争论

- 【Linux社区】Rostedt 反驳 Segher“去改你的程序”：二分旧内核需数百处构建改动，一次二分至少 13 次迭代，只能全局压制 -Werror。 `<!-- ROW_MINE: ksummit.messages.4342 -->`

## 163.32 Bugzilla 退役

- 【Linux社区】Ryabitsev 主张先定明确出路再弃用 bugzilla；LLM 预筛垃圾与发行版内核报告，报告进 lore 结构化 feed 替代 SMTP；难点是大附件的长期存储。 `<!-- ROW_MINE: ksummit.messages.4347 -->`

## 163.33 lore 回复技巧

- 【Linux社区】Berg 补充未订阅回复列表两法：lore 的 reply 链接可生成正确 In-Reply-To；或下载 raw 单邮 mbox 导入本地客户端后回复。 `<!-- ROW_MINE: ksummit.messages.4351 -->`

## 163.34 Sashiko 审查

- 【Linux社区】Roeck 指 Sashiko 将共享 DMA 内存 TOCTOU 列为高危，违背“硬件默认不恶意”原则；赞同按子系统定制提示词，指 sashiko 仓库 prompts 目录可提交修改。 `<!-- ROW_MINE: ksummit.messages.4352 -->`

## 163.35 2021 峰会议题

- 【Linux社区】回应 Ts'o 拟定的 2021 维护者峰会议题清单（UMN 复盘、加速器用户态要求、folio 与 ntfs3/ksmbd 接受标准、Rust），Pinchart 自荐分享 Linux 相机栈与 SoC 厂商沟通经验。 `<!-- ROW_MINE: ksummit.messages.4353 -->`

## 163.36 pkeys ABI

- 【Linux社区】Brodsky 拟在 LPC 讲 pkeys ABI 在信号、rseq、io_uring 等异步内核交互下规格不一致，Gleixner 称“全是坏的”；Babka 建议改投 Kernel Summit 技术议题。 `<!-- ROW_MINE: ksummit.messages.4368 -->`
