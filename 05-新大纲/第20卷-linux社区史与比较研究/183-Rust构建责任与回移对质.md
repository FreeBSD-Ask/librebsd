# 183 【Linux社区】Rust构建责任与回移对质

> 来源：ksummit 独有 p47（50 封全读，2021-04 至 2026-08：Gunthorpe 对维护者发 PR 前须保证 CONFIG_RUST=y 构建通过给出最明确责任界定含 Andrew 扣补丁与 Andreas 修 block 绑定实例；Levin 与 Bottomley 就 stable 回移依据的具体 commit 37f1663c 与 Stable-dep-of 链条往返对质；Bottomley 从法律原理系统反驳 AI 文本与代码区别对待；Brauner 以 VFS 维护者身份详述 reiserfs 等无主文件系统维护负担与移除条件主张；bugzilla 整改二封、峰会遴选争议二封、回移与链接二封）
> 判定：41 CAND / 9 NV。主题分布：峰会改线上 1、Rust PR 构建责任 1、AI 版权之争 1、回移与链接 2、峰会遴选争议 2、HID-eBPF 可逆性 1、Rust 绑定术语 1、Link 尾注价值 1、文档检查入 CI 2、AI 审查政策 1、GitLab 流程质疑 1、Rust 稳定性 2、GPIO API 弃用 1、AI 提交责任 1、Link 语义分歧 1、旧列表停用 1、AI 标签争议 1、无主文件系统 2、回归处理指引 1、THE REST 迁移 1、Intersphinx 评估 1、别名模型之争 2、Rust GPIO 选型 1、加速器用户态政策 1、静态分析溢出 1、bugzilla 整改 2、Link 替代提案 1、UALink 驱动路径 1、合并质量标准 1、LLM 提交洪流 1、AI 指南范围 1、文档构建耗时 1、设备直通专利 1、并行驱动政策 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p47 的逐封提取（2021-04 至 2026-08，41 CAND / 9 NV），全 34 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 183.1 峰会改线上

- 【Linux社区】Tso 宣布 2021 维护者峰会与内核峰会随 LPC 全线上举行，不随 OSS 迁往西雅图，LPC 因美国场地防疫要求无法办线下微会议。 `<!-- ROW_MINE: ksummit.messages.7293 -->`

## 183.2 Rust PR 构建责任

- 【Linux社区】Gunthorpe 明确顶层维护者发 PR 前须保证 CONFIG_RUST=y x86-64 allmodconfig 构建通过，举 Andrew 扣下 Uros 六补丁、Andreas 为 block 修绑定为例，主张 Rust 不要求二分安全。 `<!-- ROW_MINE: ksummit.messages.7294 -->`

## 183.3 AI 版权之争

- 【Linux社区】Bottomley 反驳“AI 生成文本不算侵权而代码算”，指两者法律地位相同；若输出构成训练数据衍生，译文同样有侵权风险。 `<!-- ROW_MINE: ksummit.messages.7296 -->`

## 183.4 回移与链接

- 【Linux社区】Bonzini 接受 Torvalds 批评，在 applypatch-msg 钩子加 sed 把 Message-ID 转 lore 链接，并分享浏览器按 Message-ID 搜 lore 的插件技巧。 `<!-- ROW_MINE: ksummit.messages.7307 -->`
- 【Linux社区】Levin 追问 Bottomley 例证：37f1663c 回移因 Stable-dep-of c3408c4ae041，而后者所修的 527e9b704c3d 无 stable 标记也从未回移。 `<!-- ROW_MINE: ksummit.messages.7444 -->`

## 183.5 峰会遴选争议

- 【Linux社区】Corbet 称程序委员会一直有意引入首次与会者，建议可规定一定比例席位留给新人，但强调在座须有能处理议题的老手。 `<!-- ROW_MINE: ksummit.messages.7320 -->`
- 【Linux社区】Stoakes 批评 Tso 的与会说明含混：议题征集似 CFP 却与遴选脱节，质疑“最活跃”标准，认同 Airlie 峰会实为“Linus 的员工会议”之说。 `<!-- ROW_MINE: ksummit.messages.7400 -->`

## 183.6 HID-eBPF 可逆性

- 【Linux社区】Kosina 反驳 Hellwig“绑定如癌症扩散”：HID-eBPF 只是少量钩子，不健康可整体弃掉并转回普通 HID 驱动，与难回退的核心绑定不同。 `<!-- ROW_MINE: ksummit.messages.7325 -->`

## 183.7 Rust 绑定术语

- 【Linux社区】Ojeda 与 Bottomley 澄清“绑定”含抽象层与 bindgen 生成物；认同扩展 sparse 与 bindgen 从 C 注解生成绑定可降摩擦，C 侧注解本身亦有价值。 `<!-- ROW_MINE: ksummit.messages.7329 -->`

## 183.8 Link 尾注价值

- 【Linux社区】Tsai 强调 Link 尾注由 b4 自动添加近乎零成本，受益者是追查回归与回移植的开发者，认为 Torvalds 的 git hook 方案过繁不可行。 `<!-- ROW_MINE: ksummit.messages.7334 -->`

## 183.9 文档检查入 CI

- 【Linux社区】Brauner 支持把 kernel-doc 检查接入 build bot，自述为非平凡代码写 kernel-doc 但多版本迭代常出复制粘贴错误，曾靠 Andrew 指出。 `<!-- ROW_MINE: ksummit.messages.7341 -->`
- 【Linux社区】Luck 通报已催促 zero-day 机器人跟进文档检查，欢迎通过他或 Dave Hansen 提覆盖建议。 `<!-- ROW_MINE: ksummit.messages.7391 -->`

## 183.10 AI 审查政策

- 【Linux社区】Roeck 主张按子系统配置 Sashiko 而非提示词；举例 350 行驱动补丁被报 9 个问题，作者须处理新增问题，既有问题可豁免。 `<!-- ROW_MINE: ksummit.messages.7344 -->`

## 183.11 GitLab 流程质疑

- 【Linux社区】Pinchart 质疑 Red Hat GitLab 议题：若 GitLab 只是供 CLI 工具处理结构化数据的传输层，何不改用去中心化、非专有的传输机制。 `<!-- ROW_MINE: ksummit.messages.7347 -->`

## 183.12 Rust 稳定性

- 【Linux社区】Overstreet 认为如今打破兼容的代价低于 20 年前——开源与版本控制普及、可借 crates.io 评估影响，审慎演进即好事。 `<!-- ROW_MINE: ksummit.messages.7350 -->`
- 【Linux社区】Jung 澄清 Rust time crate 大破坏属意外：流程曾预测重大生态破坏却因责任分散无人行动，常规小破坏机制运转良好。 `<!-- ROW_MINE: ksummit.messages.7443 -->`

## 183.13 GPIO API 弃用

- 【Linux社区】Golaszewski 说明全局 GPIO 编号转描述符涉及 providers、consumers 与固件节点，无法 coccinelle 自动化需功能测试，已耗时数年。 `<!-- ROW_MINE: ksummit.messages.7351 -->`

## 183.14 AI 提交责任

- 【Linux社区】Rostedt 主张 Signed-off-by 即声明有权提交该代码，AI 生成内容若侵权由提交者担责，最终靠法院判例而非律师预判。 `<!-- ROW_MINE: ksummit.messages.7353 -->`

## 183.15 Link 语义分歧

- 【Linux社区】Kosina 指出 Link 尾注已混入 bugzilla、GitHub 等异质链接：维护者视为补丁源线程引用，提交者当作“另见”杂记，双方常鸡同鸭讲。 `<!-- ROW_MINE: ksummit.messages.7354 -->`

## 183.16 旧列表停用

- 【Linux社区】Ryabitsev 宣布旧 ksummit-discuss 列表停用：紧急 moderation、自动退信提示新址，讨论回填 lore.kernel.org/ksummit 归档。 `<!-- ROW_MINE: ksummit.messages.7356 -->`

## 183.17 AI 标签争议

- 【Linux社区】Kozlowski 讽刺提议以“Legal-risk-by”等标签替代 Assisted-by，暗示 AI 生成补丁的专利版权风险应由添加 Signed-off-by 者自担。 `<!-- ROW_MINE: ksummit.messages.7358 -->`

## 183.18 无主文件系统

- 【Linux社区】Brauner 称 reiserfs bug 清单惊人且无维护者，主张讨论移除条件并更积极告知发行版，无主文件系统应作“僵尸”处理，未接入 xfstests 前挂载如赌博。 `<!-- ROW_MINE: ksummit.messages.7363 -->`
- 【Linux社区】Rostedt 提议把只读化作为移除无主文件系统前的过渡阶段：数年无人抱怨即视为无人使用，可手工改 #ifdef 恢复可写供测试。 `<!-- ROW_MINE: ksummit.messages.7406 -->`

## 183.19 回归处理指引

- 【Linux社区】Leemhuis 认为更深维护者树拖慢补丁且远离 Linus 者不懂其回归要求，私下提醒不可扩展，主张成文回归指引并援引官方文档。 `<!-- ROW_MINE: ksummit.messages.7365 -->`

## 183.20 THE REST 迁移

- 【Linux社区】Perches 质疑补丁与讨论分列两表：get_maintainer 如何适配、讨论与补丁靠主题匹配或 Link 关联均难奏效。 `<!-- ROW_MINE: ksummit.messages.7369 -->`

## 183.21 Intersphinx 评估

- 【Linux社区】Corbet 实测拆分文档用 intersphinx 需两次完整构建以生成 objects.inv，速度不划算，判定其不适合内核而不如 make SPHINXDIRS。 `<!-- ROW_MINE: ksummit.messages.7373 -->`

## 183.22 别名模型之争

- 【Linux社区】Uecker 指正 Jung：bug 21725 中 GCC 的 TBBA 比 LLVM 更正确、能处理类型变更存储；C 中读填充字节非 UB，未初始化仅限未取址自动变量。 `<!-- ROW_MINE: ksummit.messages.7376 -->`
- 【Linux社区】Guo 说明 Rust 无类型别名：union 与指针 transmute 合法且有 zerocopy 库，严格溯源 API 已稳定，别名规则同样约束 unsafe 代码。 `<!-- ROW_MINE: ksummit.messages.7452 -->`

## 183.23 Rust GPIO 选型

- 【Linux社区】Uytterhoeven 指出 QEMU 的 PL061 仿真不完整、连闪灯都做不到，建议选无驱动的 I2C/SPI 扩展器或 USB 接口 MCP2210 作 Rust GPIO 试点。 `<!-- ROW_MINE: ksummit.messages.7385 -->`

## 183.24 加速器用户态政策

- 【Linux社区】Pinchart 主张要求开源用户态实现不排斥厂商并行闭源优化，GPU 惯例即上游驱动须配基本全功能开源用户态，拟推广至相机 ISP 与 AI 加速器。 `<!-- ROW_MINE: ksummit.messages.7387 -->`

## 183.25 静态分析溢出

- 【Linux社区】McKenney 表态无需无符号溢出检查；因内核依赖 fwrapv，全局有符号溢出检查会很嘈杂，仅符号整数或值得做。 `<!-- ROW_MINE: ksummit.messages.7396 -->`

## 183.26 bugzilla 整改

- 【Linux社区】Leemhuis 指出仅为维护者自动建号不够：二分回归常需抄送肇事补丁作者，要覆盖就得为所有贡献者建账户。 `<!-- ROW_MINE: ksummit.messages.7417 -->`
- 【Linux社区】Leemhuis 宣布推进 bugzilla 减痛方案：设 catch-all 产品、隐藏未承诺维护组件、首页注明多数报告应走邮件，核心开发者无异议。 `<!-- ROW_MINE: ksummit.messages.7453 -->`

## 183.27 Link 替代提案

- 【Linux社区】Bottomley 提议 git am 直接把 message-id 写入提交头，b4 生成提交自动携带，语义无争议且人人可用，免去 Link 尾注人为负担。 `<!-- ROW_MINE: ksummit.messages.7427 -->`

## 183.28 UALink 驱动路径

- 【Linux社区】Walleij 建议 UALink 因需自建总线应设独立子系统，可放 drivers/accel/ual 或 drivers/ual，而非 drivers/misc/ual。 `<!-- ROW_MINE: ksummit.messages.7431 -->`

## 183.29 合并质量标准

- 【Linux社区】Brown 解释 Linus 介意的是合并质量而非数量：合并提交须有实质信息，自动化产生的默认信息合并才是问题。 `<!-- ROW_MINE: ksummit.messages.7434 -->`

## 183.30 LLM 提交洪流

- 【Linux社区】Brown 认为 AI 提交与人类超载性质不同：行为不可预测难建信任、常规反压失效，并提工具自费成本与外部性治理问题。 `<!-- ROW_MINE: ksummit.messages.7436 -->`

## 183.31 AI 指南范围

- 【Linux社区】Rostedt 回应 Gleixner：工具生成内容指南暂不定义新标签，待 submitting-patches 定案后再更新文档，属有意延后。 `<!-- ROW_MINE: ksummit.messages.7438 -->`

## 183.32 文档构建耗时

- 【Linux社区】Dunlap 实测 16GB i7 笔记本 make -j8 htmldocs 约 6 分钟，对比 Brown 的 56 核 26 分钟，并比较两者 allmodconfig 耗时悬殊。 `<!-- ROW_MINE: ksummit.messages.7441 -->`

## 183.33 设备直通专利

- 【Linux社区】Bottomley 论证 OIN 专利护盾足以让贡献者无视多数专利顾虑，专利须公开技术故自持专利无碍开源，OIN 亦可应对专利流氓。 `<!-- ROW_MINE: ksummit.messages.7451 -->`

## 183.34 并行驱动政策

- 【Linux社区】Overstreet 主张比“一设备一驱动”更细的规则：大型 Rust 重写应并行发布数个周期再删旧码，如 nvme 原型与 blk-mq 渐进推广。 `<!-- ROW_MINE: ksummit.messages.7455 -->`
