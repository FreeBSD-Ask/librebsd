# 203 【Linux社区】文件系统威胁模型与RustAPI债

> 来源：ksummit 独有 p67（库尾页 35 封全读，2023-08 至 2024-06：Ted Ts'o 系统陈述文件系统威胁模型存储设备属可信计算基损坏镜像不算安全漏洞并揭露 syzbot 计数的黑暗模式操纵与云场景不适用性；Pinchart 以 V4L2/DRM 对象生命周期 API 无法安全使用为例论证 Rust 绑定须先重写底层 API 被斥过度刨毛点出维护者负担真实结构；Miguel Ojeda 确认 Rust 最低编译器版本政策跟随 Debian Stable 系维护者峰会公开决定；Dan Williams 概括 fwctl 三年会议共识与跨子系统 NAK 的信任赤字本质并援引 MGLRU 在 LSF/MM 2022 面对面破冰先例；Bugzilla 争议四封、设备直通争议三封）
> 判定：29 CAND / 6 NV。主题分布：安全披露流程 1、Bugzilla 争议 4、维护者负担分担 1、Rust 绑定与 API 债 1、C 聚合传递争论 2、维护者峰会筹备 1、稳定分支提交标签 2、设备直通争议 3、文件系统信任与维护 3、AI 代码版权与 DCO 1、内存分配 API 1、专家社区建设 1、Rust 与全树重构 1、API 弃用政策 1、补丁抄送流程 1、倦怠与社区支援 1、kernel.org 信任体系 1、AI 贡献标注 1、HIGHMEM 淘汰 1、stable 维护义务 1。

## 203.1 安全披露流程

- **要点**：Jiri Kosina 赞同 Linus 反对 linux-distros 强制共享 PoC；支持闭列表 distros@kernel.org 提案，愿征询 SUSE 安全团队意见，坚持发行版必须进入内核安全修复流程。
- **史料**：`ksummit.messages.10565`（Jiri Kosina，2023-08-15）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10565 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：赞同 Linus 反对 linux-distros 强制共享 PoC 与支持闭列表 distros@kernel.org 提案两方并置）；动手者叙事（总纲第 10 条——动手者创造历史：以“坚持发行版必须进入内核安全修复流程”这一具体制度要求为分析单位）
- **辨析**：本块系 Jiri Kosina 的立场；“愿征询 SUSE 安全团队意见”表明其企业身份与社区立场的交叠。
- **文献**：DSLXC-11357（`ksummit.messages.10565`，2023-08-15），全文见 `raw_source.raw_json`

## 203.2 Bugzilla 争议

- **要点**：Artem 以数据反驳“骚扰”论：Bugzilla 每周约 20 份报告、单人最坏每周不足 5 封；举 bug 204807 两年半 255 条评论为例，称邮件模式无法承载此类协作。Randy Dunlap 指 Bugzilla 大量组件无负责人、“我们主动让报告被忽视”；引 Stephen 称网络报告只能转 netdev、乐见其亡；Leemhuis 称三年无改善并附 LWN 链接。Steven Rostedt 称社区只为生存行动，Meltdown/Spectre 才迫使 -rc 末期大改；肯定发行版开发者代为分诊质量高，志愿者 Slade 可任 Bugzilla 与维护者间联络人。Konstantin Ryabitsev 直言“维护者要的是补丁，不是 bug 报告”，让资深工程师做一线 QA 必致双方皆怨；警告强制订阅只会令 Bugzilla 被全员拉黑。
- **史料**：`ksummit.messages.10569`（Artem S. Tashkinov，2022-10-02）、`ksummit.messages.10583`（Randy Dunlap，2025-12-12）、`ksummit.messages.10584`（Steven Rostedt，2022-10-02）、`ksummit.messages.10603`（Konstantin Ryabitsev，2022-10-02）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10569 -->` `<!-- ROW_MINE: ksummit.messages.10583 -->` `<!-- ROW_MINE: ksummit.messages.10584 -->` `<!-- ROW_MINE: ksummit.messages.10603 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“Bugzilla 每周约 20 份报告、单人最坏每周不足 5 封”“bug 204807 两年半 255 条评论”等数据为判据）；多方平等（总纲第 8 条——本体论上各方平等：以数据反驳“骚扰”论与“维护者要的是补丁，不是 bug 报告”两方并置）
- **辨析**：四条同属 Bugzilla 争议议题；Artem 的报告量与评论数为可核数据，Dunlap 的“我们主动让报告被忽视”为自承，Konstantin 的“强制订阅只会令 Bugzilla 被全员拉黑”为机制预判。
- **文献**：DSLXC-11358、DSLXC-11362、DSLXC-11363、DSLXC-11371（`ksummit.messages.10569`、`ksummit.messages.10583`、`ksummit.messages.10584`、`ksummit.messages.10603`，2022-10-02、2025-12-12、2022-10-02、2022-10-02），全文见 `raw_source.raw_json`

## 203.3 维护者负担分担

- **要点**：Daniel Vetter 称网络子系统约 2020 年才改群体维护、值得向峰会介绍；GPU 流程自 2018 年未变，gitlab.freedesktop.org 的内核 CI 整合有望本合并窗口落地。
- **史料**：`ksummit.messages.10575`（Daniel Vetter，2023-08-21）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10575 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以网络子系统约 2020 年改群体维护、GPU 流程自 2018 年未变、gitlab.freedesktop.org 的内核 CI 整合等具体实践为分析单位）；经验优先（总纲第 9 条——经验优先：以“网络子系统群体维护值得向峰会介绍”这一实际范例为判据）
- **辨析**：本块系 Daniel Vetter 的说明；“有望本合并窗口落地”为其对 CI 整合的时间预期。
- **文献**：DSLXC-11359（`ksummit.messages.10575`，2023-08-21），全文见 `raw_source.raw_json`

## 203.4 Rust 绑定与 API 债

- **要点**：Laurent Pinchart 称 V4L2/DRM 对象生命周期 API 坏到“无法安全使用”，Rust 绑定须先彻底重写底层却被斥“过度刨毛”；主张 C/Rust 两阵营合作还 API 债以换维护者支持。
- **史料**：`ksummit.messages.10577`（Laurent Pinchart，2025-02-19）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10577 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“Rust 绑定须先彻底重写底层”与“C/Rust 两阵营合作还 API 债”这一具体路径为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：主张还 API 债与“过度刨毛”之斥两方并置）
- **辨析**：本块系 Laurent Pinchart 的论点；“V4L2/DRM 对象生命周期 API 坏到无法安全使用”为其问题诊断。
- **文献**：DSLXC-11360（`ksummit.messages.10577`，2025-02-19），全文见 `raw_source.raw_json`

## 203.5 C 聚合传递争论

- **要点**：Rust 设计团队成员 Ralf Jung 阐明 union 语义：允许任意字节重解释、无“活跃变体”，但 bool 须为 0/1 否则 UB；反驳“语言须定义 bool 非法值行为”的指责。HUANG Zhaobin 以 godbolt 实测反驳“C++ 才有隐藏指针”论：C 与 C++ 均传隐藏指针，gcc 在 C 侧多一次拷贝、C++ 走 NRVO，clang 两语言代码相同。
- **史料**：`ksummit.messages.10582`（Ralf Jung，2025-02-27）、`ksummit.messages.10622`（HUANG Zhaobin，2025-02-21）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10582 -->` `<!-- ROW_MINE: ksummit.messages.10622 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“以 godbolt 实测反驳 C++ 才有隐藏指针论：gcc 在 C 侧多一次拷贝、C++ 走 NRVO”这一实测为判据）；知识注定过时（总纲第 22 条——知识注定过时：union 语义与 bool 须为 0/1 否则 UB 等语言规则随标准演进）
- **辨析**：两条同属 C 聚合传递争论议题；Jung 的 union 语义阐明为语言规范层，HUANG 的 godbolt 实测为可复算的编译器行为对照。
- **文献**：DSLXC-11361、DSLXC-11375（`ksummit.messages.10582`、`ksummit.messages.10622`，2025-02-27、2025-02-21），全文见 `raw_source.raw_json`

## 203.6 维护者峰会筹备

- **要点**：Linus 为峰会“Linus 环节”征集预备考题：请 Corbet 匿名代收维护流程痛点、只转交个人意见勿公开讨论；自称“大声者”，建议加强主持以免少数人垄断发言。
- **史料**：`ksummit.messages.10587`（Linus Torvalds，2023-11-13）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10587 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“请 Corbet 匿名代收维护流程痛点、只转交个人意见勿公开讨论”“建议加强主持以免少数人垄断发言”等具体筹备安排为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：自称“大声者”与加强主持之建议并置）
- **辨析**：本块系 Linus Torvalds 的征集；“匿名代收”为保护发言者的程序设计。
- **文献**：DSLXC-11364（`ksummit.messages.10587`，2023-11-13），全文见 `raw_source.raw_json`

## 203.7 稳定分支提交标签

- **要点**：James Bottomley 反对新增 not-stable 标签：Fixes 回答补丁来源、是否回传属事后可能推翻的判断，可另走 stable 通道兜底；该标签实为阻止非修复提交混入 stable。Mauro 建议 pre-git 修复以 Link 指向 tglx history 树（Bitkeeper 史前库）URL，而非 Fixes 引用其哈希，以免校验和冲突与异树误读；保留 Fixes: 1da177e4c3f4。
- **史料**：`ksummit.messages.10589`（James Bottomley，2024-07-14）、`ksummit.messages.10652`（Mauro Carvalho Chehab，2024-07-15）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10589 -->` `<!-- ROW_MINE: ksummit.messages.10652 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：反对新增 not-stable 标签与建议 pre-git 修复以 Link 指向 history 树两方并置）；动手者叙事（总纲第 10 条——动手者创造历史：以“保留 Fixes: 1da177e4c3f4”这一具体标注为分析单位）
- **辨析**：两条同属稳定分支提交标签议题；Bottomley 的“是否回传属事后可能推翻的判断”为机制分析，Mauro 的“以免校验和冲突与异树误读”为技术理由。
- **文献**：DSLXC-11365、DSLXC-11384（`ksummit.messages.10589`、`ksummit.messages.10652`，2024-07-14、2024-07-15），全文见 `raw_source.raw_json`

## 203.8 设备直通争议

- **要点**：Ricardo Ribalda 引 linuxtv.org 声明：V4L2 不接受含未公开闭源特性的驱动，故“厂商获得 vendor 访问”无从谈起；否认有人提议向用户态开放 PCI 寄存器。Dan Williams 称 fwctl 历经三年会议已成多方共识，RDMA 与 netdev 的跨子系统 NAK 缺的是信任而非技术；引 MGLRU 在 LSF/MM 2022 面对面破冰为例，主张再试调解。Laurent Pinchart 回应专利论：OIN 保护伞理论有效，但专利恐慌多系大型 SoC 厂商自造，某公司“工程由律师管理”；不能既造专利乱局又以专利为由拒公开。
- **史料**：`ksummit.messages.10591`（Ricardo Ribalda Delgado，2024-07-26）、`ksummit.messages.10601`（Dan Williams，2024-08-07）、`ksummit.messages.10649`（Laurent Pinchart，2024-07-26）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10591 -->` `<!-- ROW_MINE: ksummit.messages.10601 -->` `<!-- ROW_MINE: ksummit.messages.10649 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 fwctl 三年会议共识、引 MGLRU 在 LSF/MM 2022 面对面破冰为例、主张再试调解等具体方案为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：RDMA 与 netdev 的跨子系统 NAK 缺的是信任而非技术与“专利恐慌多系大型 SoC 厂商自造”两方并置）
- **辨析**：三条同属设备直通争议议题；Dan Williams 的“缺的是信任而非技术”为本页信任赤字论的核心，Ribalda 引 linuxtv.org 声明为可反查依据。
- **文献**：DSLXC-11366、DSLXC-11370、DSLXC-11383（`ksummit.messages.10591`、`ksummit.messages.10601`、`ksummit.messages.10649`，2024-07-26、2024-08-07、2024-07-26），全文见 `raw_source.raw_json`

## 203.9 文件系统信任与维护

- **要点**：Dave Chinner 提社区维护文件系统最低门槛：须有可用 mkfs/fsck 并入 fstests；建议以 fstype 标志而非配置项标记受支持、弃用、待移除状态；老盘数据可靠 VM 启动旧发行版读取。Ted Ts'o 实测列举 27 个支持 generic_file_mmap 的简单文件系统（fat、hfsplus、ntfs3、exfat 等），反驳“文档场景会回退 read/write”的假设，佐证 mmap 攻击面广。Ted Ts'o 论威胁模型：存储设备属可信计算基，损坏镜像不算安全漏洞；syzbot 计数互不可比、系“黑暗模式”操纵；云端本假定攻击者有 root，真险在 GNOME 自动挂载，e2fsprogs 将加 udev 规则缓解。
- **史料**：`ksummit.messages.10593`（Dave Chinner，2023-09-06）、`ksummit.messages.10613`（Theodore Ts'o，2023-09-18）、`ksummit.messages.10625`（Theodore Ts'o，2023-09-11）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10593 -->` `<!-- ROW_MINE: ksummit.messages.10613 -->` `<!-- ROW_MINE: ksummit.messages.10625 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“实测列举 27 个支持 generic_file_mmap 的简单文件系统”“syzbot 计数互不可比”等实测与判断为判据）；多方平等（总纲第 8 条——本体论上各方平等：Chinner 的社区维护最低门槛与 Ts'o 的威胁模型三点主张并置）
- **辨析**：三条同属文件系统信任与维护议题；Ts'o 的威胁模型（存储设备属可信计算基、损坏镜像不算安全漏洞）为本页正样本核心，“黑暗模式”之评为其判断。
- **文献**：DSLXC-11367、DSLXC-11374、DSLXC-11377（`ksummit.messages.10593`、`ksummit.messages.10613`、`ksummit.messages.10625`，2023-09-06、2023-09-18、2023-09-11），全文见 `raw_source.raw_json`

## 203.10 AI 代码版权与 DCO

- **要点**：Paul McKenney 讨论纯 AI 代码版权：美国版权局认定非人类作者无版权、纯 AI 代码近乎公有领域；但他强调美国是判例法域、解释可回溯变更，且内核须顾及美国以外法域。
- **史料**：`ksummit.messages.10597`（Paul E. McKenney，2025-08-19）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10597 -->`
- **史观**：法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：美国版权局认定非人类作者无版权、纯 AI 代码近乎公有领域，且内核须顾及美国以外法域）；经验优先（总纲第 9 条——经验优先：以“美国是判例法域、解释可回溯变更”这一实际法律状况为判据）
- **辨析**：本块系 Paul McKenney 的讨论；“强调须顾及美国以外法域”为其对单一法域结论的限定。
- **文献**：DSLXC-11368（`ksummit.messages.10597`，2025-08-19），全文见 `raw_source.raw_json`

## 203.11 内存分配 API

- **要点**：Miguel Ojeda 澄清 Rust 最低编译器版本政策为跟随 Debian Stable，系维护者峰会公开决定；辩称等待上游分配器无果后才转向，本可更早行动。
- **史料**：`ksummit.messages.10600`（Miguel Ojeda，2026-07-09）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10600 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“Rust 最低编译器版本政策跟随 Debian Stable”这一具体政策为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：澄清政策系维护者峰会公开决定与“本可更早行动”的自省并置）
- **辨析**：本块系 Miguel Ojeda 的澄清；“辩称等待上游分配器无果后才转向”为其动机说明。
- **文献**：DSLXC-11369（`ksummit.messages.10600`，2026-07-09），全文见 `raw_source.raw_json`

## 203.12 专家社区建设

- **要点**：Dave Airlie 主张培育跨厂商专家社区：habanalabs 编译器后端是 LLVM 分叉应上游化；“只有本公司懂自家硬件”是保留控制权的借口；倡议共享运行库仓库与上游优先流程。
- **史料**：`ksummit.messages.10610`（Dave Airlie，2021-09-12）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10610 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“habanalabs 编译器后端是 LLVM 分叉应上游化”“倡议共享运行库仓库与上游优先流程”等具体主张为分析单位）；法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：“只有本公司懂自家硬件”是保留控制权的借口）
- **辨析**：本块系 Dave Airlie 的主张；“培育跨厂商专家社区”为其诉求。
- **文献**：DSLXC-11372（`ksummit.messages.10610`，2021-09-12），全文见 `raw_source.raw_json`

## 203.13 Rust 与全树重构

- **要点**：Mike Rapoport 指核心 API 一旦有 Rust 抽象，全树重构者即须懂 Rust 并协调抽象维护者；而大型重构多由非维护者完成，维护者未必有空协助，扩展性堪忧。
- **史料**：`ksummit.messages.10612`（Mike Rapoport，2021-07-06）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10612 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：全树重构者须懂 Rust 并协调抽象维护者与“大型重构多由非维护者完成、维护者未必有空协助”两方并置）；知识注定过时（总纲第 22 条——知识注定过时：核心 API 一旦有 Rust 抽象即引入跨语言协调负担）
- **辨析**：本块系 Mike Rapoport 的顾虑；“扩展性堪忧”为其结论。
- **文献**：DSLXC-11373（`ksummit.messages.10612`，2021-07-06），全文见 `raw_source.raw_json`

## 203.14 API 弃用政策

- **要点**：Linus 表态并行 API 并存完全正常，devm_xyz 与 xyz 将永远共存；反对“弃用”话术与指责旧接口用户：“懒得不转换全部用户者，无权要求他人代劳”。
- **史料**：`ksummit.messages.10623`（Linus Torvalds，2025-08-27）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10623 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：并行 API 并存完全正常与反对“弃用”话术两方并置）；经验优先（总纲第 9 条——经验优先：以“devm_xyz 与 xyz 将永远共存”这一实际判断为判据）
- **辨析**：本块系 Linus Torvalds 的表态；“懒得不转换全部用户者，无权要求他人代劳”为其对旧接口用户的反诘。
- **文献**：DSLXC-11376（`ksummit.messages.10623`，2025-08-27），全文见 `raw_source.raw_json`

## 203.15 补丁抄送流程

- **要点**：Steven Rostedt 主张只抄送触及自身代码的单个补丁而非 20 封整系列，整系列反而易漏审；lore.kernel.org/r/<message-id> 可一键取回全线程，lore 已化解“信息孤岛”。
- **史料**：`ksummit.messages.10627`（Steven Rostedt，2021-04-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10627 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“只抄送触及自身代码的单个补丁而非 20 封整系列”“lore.kernel.org/r/<message-id> 可一键取回全线程”等具体机制为分析单位）；经验优先（总纲第 9 条——经验优先：以“整系列反而易漏审”这一实际经验为判据）
- **辨析**：本块系 Steven Rostedt 的主张；“lore 已化解信息孤岛”为其对现状的判断。
- **文献**：DSLXC-11378（`ksummit.messages.10627`，2021-04-22），全文见 `raw_source.raw_json`

## 203.16 倦怠与社区支援

- **要点**：Dan Williams 详述倦怠支援：自述参加 LPC 圆桌后 Dr. Chance 一对一随访；支持设志愿名单，认为子系统例会、聊天频道与非正式聚会可减压；追问 LF 赞助咨询实际使用率。
- **史料**：`ksummit.messages.10634`（Dan Williams，2025-09-23）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10634 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“自述参加 LPC 圆桌后 Dr. Chance 一对一随访”“支持设志愿名单”等具体支援安排为分析单位）；经验优先（总纲第 9 条——经验优先：以“子系统例会、聊天频道与非正式聚会可减压”这一实际经验为判据）
- **辨析**：本块系 Dan Williams 的详述；“追问 LF 赞助咨询实际使用率”为其对支援实效的追问。
- **文献**：DSLXC-11379（`ksummit.messages.10634`，2025-09-23），全文见 `raw_source.raw_json`

## 203.17 kernel.org 信任体系

- **要点**：Greg KH 披露 kernel.org 正与 OpenSSF 合作设计分布式信任框架以替代自研 Web of Trust，二月会议公布；确认需“重建”信任网，理想是对现有 gpg 用法透明替换。
- **史料**：`ksummit.messages.10638`（Greg KH，2026-01-23）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10638 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“与 OpenSSF 合作设计分布式信任框架以替代自研 Web of Trust”这一具体项目为分析单位）；知识注定过时（总纲第 22 条——知识注定过时：确认需“重建”信任网，理想是对现有 gpg 用法透明替换）
- **辨析**：本块系 Greg KH 的披露；“二月会议公布”为其给出的时间节点。
- **文献**：DSLXC-11380（`ksummit.messages.10638`，2026-01-23），全文见 `raw_source.raw_json`

## 203.18 AI 贡献标注

- **要点**：Mark Brown 提议以“written by / translated by”区分 AI 撰写与翻译润色，主张统一谈“工具”而非仅针对 LLM，避免纠缠工具实现细节的规则博弈。
- **史料**：`ksummit.messages.10644`（Mark Brown，2025-08-07）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10644 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“以 written by / translated by 区分 AI 撰写与翻译润色”这一具体标注方案为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：统一谈“工具”而非仅针对 LLM 与“避免纠缠工具实现细节的规则博弈”并置）
- **辨析**：本块系 Mark Brown 的提议；“主张统一谈工具”为其对规则可扩展性的考虑。
- **文献**：DSLXC-11381（`ksummit.messages.10644`，2025-08-07），全文见 `raw_source.raw_json`

## 203.19 HIGHMEM 淘汰

- **要点**：Richard Weinberger 举证 PAGE_OFFSET 影响：客户设备 2G/2G 分割令 JRE 地址空间受限，改回 3G/1G 解决；自称顾问仍时遇 Java 工作负载。
- **史料**：`ksummit.messages.10647`（Richard Weinberger，2025-10-06）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10647 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“客户设备 2G/2G 分割令 JRE 地址空间受限，改回 3G/1G 解决”这一实际案例为判据）；动手者叙事（总纲第 10 条——动手者创造历史：以 PAGE_OFFSET 影响这一具体机制为分析单位）
- **辨析**：本块系 Richard Weinberger 的举证；“自称顾问仍时遇 Java 工作负载”表明其为一线经验。
- **文献**：DSLXC-11382（`ksummit.messages.10647`，2025-10-06），全文见 `raw_source.raw_json`

## 203.20 stable 维护义务

- **要点**：Sasha Levin 反对将 stable 义务强加主线开发者：重申 stable 首条规则是不给未参与者增负，拒当执法者并反问“违规者是否要禁止上游提交”。
- **史料**：`ksummit.messages.10663`（Sasha Levin，2024-06-13）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10663 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：反对将 stable 义务强加主线开发者与“拒当执法者”并置）；经验优先（总纲第 9 条——经验优先：以“stable 首条规则是不给未参与者增负”这一实际规则为判据）
- **辨析**：本块系 Sasha Levin 的反对；“反问违规者是否要禁止上游提交”为其反诘。
- **文献**：DSLXC-11385（`ksummit.messages.10663`，2024-06-13），全文见 `raw_source.raw_json`
