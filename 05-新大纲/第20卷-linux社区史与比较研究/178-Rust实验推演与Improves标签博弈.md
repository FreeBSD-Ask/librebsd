# 178 【Linux社区】Rust实验推演与Improves标签博弈

> 来源：ksummit 独有 p42（50 封全读，2021-07 至 2026-07：Pinchart 强烈反对 LLM 缺陷分诊却全文引录 Levin 的 LLM 分析实战自建 vmlinux 字节级核对定位 iptfs skb_put 崩溃及引入提交；Ts'o 公布 2021 维护者峰会候选议程全文含 UMN 复盘加速器门槛 folio 接受标准 Rust 与 29 人邀请名单；Mauro 对 Rust 实验三分结局推演失败留 C 安全化成果成功则 C 渐退评价分裂致碎片化；Levin 以逾 80% Fixes 补丁入 stable 数据提案 Improves 标签遭 Torvalds 当场拒绝；Rust 入内核争议六封、Sashiko 审码四封、AI 审码利弊三封）
> 判定：48 CAND / 2 NV。主题分布：Rust入内核争议 6、Rust别名规则 3、Link标签流程 3、API弃用执行 1、trivial补丁政策 2、MAINTAINERS校验 1、设备直通之争 2、LLM缺陷处理 2、AI审码利弊 3、峰会议程拟定 1、Sashiko审码 4、linux-next流程 2、安全披露政策 1、补丁CC惯例 1、pkeys ABI讨论 1、用户态配套要求 2、密钥信任网改造 2、静态分析设想 1、HIGHMEM淘汰 1、stable邮件治理 1、Bugzilla存废 1、文档索引工具 1、编译器警告争论 1、stable标签提案 2、AI生成内容规范 2、malloc与GFP之争 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p42 的逐封提取（2021-07 至 2026-07，48 CAND / 2 NV），全 26 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 178.1 Rust入内核争议

- 【Linux社区】Bottomley 认可内存安全为 Rust 主打优势，但指驱动绕不开 unsafe、编译器与 fuzzer 已能查错；并举跨子系统重构更难、测试矩阵翻倍、懂 Rust 者少致审稿弱化三点劣势。 `<!-- ROW_MINE: ksummit.messages.6503 -->`
- 【Linux社区】Bart Van Assche 质询：引入 Rust 驱动后，相关子系统维护者是否须为每个被 Rust 使用的头文件同时维护 C 与 Rust 两个版本。 `<!-- ROW_MINE: ksummit.messages.6520 -->`
- 【Linux社区】Arnd 认可 Wedson 方案：dev_ 变体与 raw_spinlock 支持暂缺但无根本障碍；CONFIG_PM 相关代码拟用 cfg! 包裹移入核心库，交编译器裁剪。 `<!-- ROW_MINE: ksummit.messages.6526 -->`
- 【Linux社区】Brown 纠正 Dreier：devres 在内核应用极广、新驱动应尽量用；但过度热心会致中断处理器存活超期访问已释放资源。 `<!-- ROW_MINE: ksummit.messages.6550 -->`
- 【Linux社区】Romanovsky 提议过渡期放宽 Rust 代码“你弄坏你修”规则：外部重构可暂留破损交维护者善后，并引 staging/Lustre 时期先例。 `<!-- ROW_MINE: ksummit.messages.6590 -->`
- 【Linux社区】Mauro 系统推演：safe Rust 须先改造 mm/VFS/devm/PCI/USB 等核心 C 接口；实验结局三分——失败则 C 安全化成果留存、成功则 C 渐退、评价分裂恐致子系统碎片化。 `<!-- ROW_MINE: ksummit.messages.6617 -->`

## 178.2 Rust别名规则

- 【Linux社区】Gary Guo 澄清：C 常被诟病的是基于类型的别名规则，Rust 并无类型别名限制，仅按可变性约束别名，且可在更细粒度上按需关闭。 `<!-- ROW_MINE: ksummit.messages.6504 -->`
- 【Linux社区】Overstreet 与 Torvalds 论定：基于来源的别名规则可行，生命周期标注即跨函数来源表达，treeborrow 已并入 Miri；类型别名与 restrict 则被证明不可行。 `<!-- ROW_MINE: ksummit.messages.6539 -->`
- 【Linux社区】Ojeda 讲解 unsafe 不改变别名规则：&mut 等同 restrict/noalias，裸指针无别名约束；Rust 向 LLVM 传递大量别名信息，曾逼出须修的 LLVM bug。 `<!-- ROW_MINE: ksummit.messages.6629 -->`

## 178.3 Link标签流程

- 【Linux社区】Dan Williams 提交 b4 补丁，将 linktrailer 从 LoreSeries 内联逻辑重构为 LoreMessage 属性，为把 Link: 尾注写入 git notes 做准备。 `<!-- ROW_MINE: ksummit.messages.6506 -->`
- 【Linux社区】Desnoyers 提议新增 Link-Origin/Origin 标签，把命名空间从 URL 内隐语义提升到标签层；Geert 指 patch.msgid.link 与 lore 域名之分正为此设计。 `<!-- ROW_MINE: ksummit.messages.6554 -->`
- 【Linux社区】Williams 为 b4 shazam 新增 --add-link-note：按 patch-id 匹配新提交后以 git notes 记录 Link 尾注，遵循 b4.linkmask；注明初稿曾用 Claude Sonnet 4、提交行皆自撰。 `<!-- ROW_MINE: ksummit.messages.6556 -->`

## 178.4 API弃用执行

- 【Linux社区】Kosina 认同 Torvalds“改 API 就要修完所有现有用户，否则新旧 API 永久自担”的原则，但指出涉冷门驱动时几乎无法做有效功能测试，只能靠破坏后有人发声。 `<!-- ROW_MINE: ksummit.messages.6507 -->`

## 178.5 trivial补丁政策

- 【Linux社区】Mauro 核查：media 被 revert 的 29 个补丁无恶意代码；Leon 指 467a37fba93f 对 sp8870 的错误检查反而致损；Mauro 主张连同 1999 年的 av7110 一并移除。 `<!-- ROW_MINE: ksummit.messages.6510 -->`
- 【Linux社区】Kosina 认为 UMN 事件与 trivial 政策并无直接关联：多数问题补丁属实质性功能改动，本就不符合 Documentation/process/submitting-patches.rst 的 trivial 定义。 `<!-- ROW_MINE: ksummit.messages.6511 -->`

## 178.6 MAINTAINERS校验

- 【Linux社区】Rob Herring 认为发件端教育无解，应靠收件端过滤与 lei；建议提交补丁调高 get_maintainer.pl 的 --git-min-percent 默认值并提高 --git-min-signatures。 `<!-- ROW_MINE: ksummit.messages.6515 -->`

## 178.7 设备直通之争

- 【Linux社区】Ribalda 力主 DRM 更适合复杂 ISP：厂商 IOCTL 加类 Mesa 方案；称社区抵制致 99% 以上市场依赖树外驱动，提议开源基座加厂商闭源差异的混合模型。 `<!-- ROW_MINE: ksummit.messages.6519 -->`
- 【Linux社区】Pinchart 以媒体业反证 Gunthorpe：曾见 BSP 驱动把用户态物理地址未加过滤直交 DMA 引擎；质问闭源固件对直通命令副作用的文档能否信任。 `<!-- ROW_MINE: ksummit.messages.6575 -->`

## 178.8 LLM缺陷处理

- 【Linux社区】Mauro 实测 LLM 直接产出补丁开箱不可用，宜提示生成代码、编译验证循环后再以 diff 出补丁；其 .po 翻译试验靠 from/to 表成功，但技术词条与大小写欠准。 `<!-- ROW_MINE: ksummit.messages.6525 -->`
- 【Linux社区】Pinchart 强烈反对 LLM 缺陷分诊：“错工具，请停”；但引 Levin 演示：LLM 自建 vmlinux 复现 iptfs skb_put 非线性崩溃，定位引入提交 5f2b6a9095743（Hopps）。 `<!-- ROW_MINE: ksummit.messages.6573 -->`

## 178.9 AI审码利弊

- 【Linux社区】Pinchart 论证 AI 预检后旧 v1 不再上列表、v2 起点即新 v1；并指可抱怨贡献者不跑 checkpatch，却不能强迫其使用专有 AI 工具。 `<!-- ROW_MINE: ksummit.messages.6533 -->`
- 【Linux社区】Carpenter 观察到 AI 生成的锁文档自信却含糊略有错误，生成快而审稿慢；Lawall 设想“注释质量 0-day”督促内存屏障等必注处。 `<!-- ROW_MINE: ksummit.messages.6555 -->`
- 【Linux社区】Lunn 指维护者重跑测试只为确认开发者跑过、多看退出码；checkpatch/sparse/kdoc/Coccinelle 结果可复现，质询 AI 工具能否同样可复现。 `<!-- ROW_MINE: ksummit.messages.6592 -->`

## 178.10 峰会议程拟定

- 【Linux社区】Ts'o 公布 2021 维护者峰会候选议程：复盘 UMN 事件、加速器驱动用户态门槛、补丁接受标准（folio/ntfs3/ksmbd）、Rust 反馈、Linus 对流程满意度，并列 29 人邀请名单。 `<!-- ROW_MINE: ksummit.messages.6538 -->`

## 178.11 Sashiko审码

- 【Linux社区】Bart 回应 Corbet 对企业资助终止的担忧：Sashiko 开源且支持多 LLM，但不确定是否支持开放权重模型，请 Roman 指正。 `<!-- ROW_MINE: ksummit.messages.6541 -->`
- 【Linux社区】Greg KH 指 Sashiko 对 mpt3sas 的 TOCTOU 高危告警有误：硬件不得假定恶意；根因在审稿提示词，拟按子系统补 drivers.md 并写入内核 threat model 文档。 `<!-- ROW_MINE: ksummit.messages.6549 -->`
- 【Linux社区】Gushchin 赞同 Kozlowski：内核知识应写给开发者的文档而非 LLM 专用提示；并称正试验 Sashiko 依人工邮件反馈自动生成提示词，初步见效。 `<!-- ROW_MINE: ksummit.messages.6582 -->`
- 【Linux社区】Berg 反对默认信任硬件：WiFi 固件可被空口攻击，漏报风险不对称；指 Bottomley 的默认信任方案本身即反向 opt-out 一例，后者称 144 个驱动子系统仅 3 家退出。 `<!-- ROW_MINE: ksummit.messages.6585 -->`

## 178.12 linux-next流程

- 【Linux社区】Tissoires 主张把 linus-next 定位为仅面向 Linus 的 pre-merge 门禁：测试不过的 PR 自动搁置、由维护者自理；赞同 Kees 设 bot 报告抄送、烘焙时长与测试失败。 `<!-- ROW_MINE: ksummit.messages.6544 -->`
- 【Linux社区】Pinchart 愿入 linux-next 但忧 media 子系统以 cherry-pick 而非合并其 PR；Berg 称双树不同 commit id 会触发告警邮件，Pinchart 认为不应成为常规做法。 `<!-- ROW_MINE: ksummit.messages.6569 -->`

## 178.13 安全披露政策

- 【Linux社区】Rostedt 追问仅向 distros 名单披露应取提交 SHA 是否可行；并载 Greg KH 立场：政府与公司多年索取 security@ 访问均被拒，开放只会提前泄露漏洞。 `<!-- ROW_MINE: ksummit.messages.6559 -->`

## 178.14 补丁CC惯例

- 【Linux社区】Rapoport 称最难忍的是收到系列中段散件；主张至少向所有相关者发送 cover letter 以便了解全局，认为邮件流偏好因人而异。 `<!-- ROW_MINE: ksummit.messages.6571 -->`

## 178.15 pkeys ABI讨论

- 【Linux社区】Brodsky 拟报 LPC：pkeys ABI 对信号、rseq、io_uring 线程等异步内核交互欠规范且跨架构不一，Gleixner 断言“全坏了”；Bottomley 建议 BoF 或工作坊形式。 `<!-- ROW_MINE: ksummit.messages.6572 -->`

## 178.16 用户态配套要求

- 【Linux社区】Pinchart 论证 GPU/ISP 无法靠 selftest 验证：其向用户态暴露大量命令缓冲式自定义 API，须有完整自由用户态栈方能有意义地测试驱动。 `<!-- ROW_MINE: ksummit.messages.6586 -->`
- 【Linux社区】Bottomley 认可 DRM/KMS 式互锁：新 KMS 属性须先提交 Weston/Xorg 等用法补丁并获架构认可；机密计算同样依赖 QEMU/edk2 联动，迟来异议按 bug 修复处理。 `<!-- ROW_MINE: ksummit.messages.6618 -->`

## 178.17 密钥信任网改造

- 【Linux社区】Bottomley 批评 LF 联合 OpenSSF 闭门研发 WoT 替代方案违背开源惯例；自述用 DANE/DNSSEC 分发密钥，而 kernel.org 未启用 DNSSEC，忧方案罔顾此类路径。 `<!-- ROW_MINE: ksummit.messages.6593 -->`
- 【Linux社区】Mauro 发现 LFMS26 议程“First Person credentials”称将从 Linux 内核项目起步，追问改造何时波及自身职责；Greg 称二月会议后公开。 `<!-- ROW_MINE: ksummit.messages.6622 -->`

## 178.18 静态分析设想

- 【Linux社区】Geert 与 Arnd 厘清 devm_*_get_optional 语义：返回合法指针、NULL 或错误指针且依 DTB 运行期而定；clk API 允许以 NULL 续调操作，struct clk 不透明防解引用。 `<!-- ROW_MINE: ksummit.messages.6599 -->`

## 178.19 HIGHMEM淘汰

- 【Linux社区】Arnd 就 Gaisler 16GiB sparc32 新 SoC 算账：16GB 仅 mem_map[] 即占约 160MB lowmem；在产 LEON 最高 2GiB，结论 4GB 以上应改用 64 位内核。 `<!-- ROW_MINE: ksummit.messages.6603 -->`

## 178.20 stable邮件治理

- 【Linux社区】Ryabitsev 建议把“已入 stable 树”通知改写入 public-inbox 供 lore 检索而不再经 SMTP 投递；Levin 自认该邮件纯属垃圾。 `<!-- ROW_MINE: ksummit.messages.6611 -->`

## 178.21 Bugzilla存废

- 【Linux社区】用户 Tashkinov 力挺 Bugzilla：引 Rostedt 语“LKML 日入 800 封无人读”；自述两次私邮 Linus 均获响应，指邮件列表作缺陷追踪须反复重述。 `<!-- ROW_MINE: ksummit.messages.6614 -->`

## 178.22 文档索引工具

- 【Linux社区】Dobriyan 批评 ctags 过时：“make tags”单线程且忽略正则持续膨胀；实测 QT Creator/clangd 需 allmodconfig 配置并把头文件声明为 C 方可用。 `<!-- ROW_MINE: ksummit.messages.6623 -->`

## 178.23 编译器警告争论

- 【Linux社区】Torvalds 痛斥 -Wtype-limits 对范围检查宏“绝不可告警”却两端皆误报；Overstreet 反驳：改写范围检查写法比模式匹配更容易。 `<!-- ROW_MINE: ksummit.messages.6633 -->`

## 178.24 stable标签提案

- 【Linux社区】Levin 提案：逾 80% Fixes 补丁终入 stable 致标签被省略滥用，故新增 Improves 标签、Fixes 改视同 Stable，逐步弃用 Cc: stable，保留 stable+noautosel。 `<!-- ROW_MINE: ksummit.messages.6634 -->`
- 【Linux社区】Torvalds 拒绝 Improves 标签：“我不会用这种奇怪无谓的标签”；一切提交皆改进，真修复才引 Fixes，现实并非黑白，标签改变不了。 `<!-- ROW_MINE: ksummit.messages.6641 -->`

## 178.25 AI生成内容规范

- 【Linux社区】Stoakes 区分 LLM 与 checkpatch 垃圾：前者能产出全新难驳的系列；mm 等领域维护者资源与补丁流入失衡已临临界，再激增将成大患。 `<!-- ROW_MINE: ksummit.messages.6642 -->`
- 【Linux社区】Bottomley 审 Lorenzo 增补：删“slop”一词（新近俚语且无可操作信息）；规范应适用于任何工具生成内容，不限于 AI。 `<!-- ROW_MINE: ksummit.messages.6649 -->`

## 178.26 malloc与GFP之争

- 【Linux社区】Anvin 放话：若 Rust 连不同内存分配器都应付不了，“Rust 进 Linux 就是大错，趁早拔除”；上文 Wilcox 已改述提案为“GFP 标志该废”，Kees 力主按类型分配。 `<!-- ROW_MINE: ksummit.messages.6651 -->`
