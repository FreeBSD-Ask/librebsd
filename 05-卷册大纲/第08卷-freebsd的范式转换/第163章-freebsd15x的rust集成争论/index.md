---
chapter: 第 163 章
id: CH163
volume: 第08卷-freebsd的范式转换
---

# 第163章 freebsd15x的rust集成争论

## 史料

- [WEB:lists.freebsd.org/freebsd-hackers/2024-September/003601] Warner Losh 邮件（freebsd-hackers, 2024-09-03）：Rust 绑定使内核工作翻倍——C 与 Rust 双实现须同步演进，pkgbase 是 base 系统现代化正道；HardenedBSD 表态支持 userland Rust
- [WEB:vuink.com/2024-freebsd-developer-summit] 2024 FreeBSD Developer Summit 纪要：Rust 快速发布周期与 base 系统节奏冲突（"they just release too often, at least for our base system cadence"）；结论为评估前景、未做决定

## 要点

- 2024 年 1 月 20 日，开发者 Alan Somers（asomers@，Google 工程师、FreeBSD 文件系统与存储子系统长期贡献者）在 freebsd-hackers@ 邮件列表发布 “The Case for Rust (in the base system)” 一文，正式提出将 Rust 编程语言引入 FreeBSD 基础系统的方案；Somers 指出：Rust 的内存安全特性可以消除 C/C++ 代码中大量的内存安全漏洞（据 Google/MSRC 统计约 70% 的安全漏洞源于内存安全问题）；FreeBSD 已在 Ports 中支持 Rust，但 base system 中引入 Rust 工具链允许用 Rust 重写/新写安全关键组件（如用户态工具、新驱动、文件系统工具等）；Somers 承认主要缺点是构建时间将加倍（Rust 编译器编译较慢），但认为安全收益超过成本
- Somers 提案引发的社区争论持续超过两年（2024.1-2026.7），核心争议点包括：① 构建时间与资源——反对者（如 Warner Losh（沃纳·洛什） imp@、Baptiste Daroussin（巴蒂斯特·达鲁桑） bapt@ 等）指出 Rust 工具链本身体积庞大（数百 MB）、编译速度慢，将显著增加 base 系统构建时间与 CI 资源消耗，对资源有限的 Tier 2 平台（如 riscv64、armv7）尤其不利；② 编译器复杂性——Rust 编译器（rustc）使用 LLVM 后端（与 FreeBSD 默认 Clang 一致）但本身是用 Rust 编写的，这意味着构建 Rust 工具链需要先有一个可用的 Rust 二进制（“自举问题”），这与 C 编译器可通过系统 C 编译器从源码构建的传统不同；③ 许可证——Rust 本身采用 MIT/Apache 2.0 双许可，与 FreeBSD 许可证兼容，这一点争议不大；④ 维护负担——引入新语言意味着需要一批懂 Rust 的开发者维护相关代码，而 FreeBSD 核心开发者群体中 Rust 专业知识分布不均；⑤ 安全收益是否值得——支持者（如 Colin Percival cperciva@ 等）认为内存安全漏洞占比数据（70%）说明问题严重，Rust 是可行解决方案；反对者认为改进 C 代码（静态分析、形式化验证、Capsicum 沙箱）也能提高安全性
- 截至 2026.7，Rust 在 FreeBSD 生态中的实际状态是：Ports 中已有成熟的 Rust 工具链与大量 Rust 编写的第三方软件（如 ripgrep、exa、fd-find、rustc 本身、Firefox 部分组件等）；FreeBSD 内核中 **没有** Rust 代码；base system 中 **没有** Rust 组件；但社区讨论中逐渐形成一种可能的渐进路径：① 先在 ports 中持续维护 Rust 工具链的高质量支持；② 允许用 Rust 编写一些可选的用户态工具（如新的管理工具、测试工具）作为 ports 存在；③ 考虑引入 Rust 标准库到 base 以支持 Rust 编写的 base 组件（如果/当共识形成）；④ 内核 Rust 支持是非常远期的可能性（即使在 Linux 中也仍处于实验阶段）；16.0（预计 2027-2028）周期内是否会有 Rust 组件进入 base 仍是未知数
- Rust 入 base 争论时间线：2024.1.20 Alan Somers 发起初始提案；2024.1-3 第一轮邮件列表大讨论；2024.8 LWN 报道引发第二轮关注；2025 年 BSDCan/vDevCon 举办相关 BOF；2025-2026 年讨论持续但未形成决议；Core Team 截至 2026.7 未就 Rust 入 base 进行正式投票；关键参与者包括：支持者 Alan Somers、Colin Percival 等；反对者/质疑者 Warner Losh、Baptiste Daroussin、Poul-Henning Kamp 等；中间立场 Ed Maste（埃德·马斯特） 等——多数开发者不反对 Rust 本身，但对何时引入、如何引入、引入范围持审慎态度
- 自媒体《FreeBSD 大败局》2026-01-26 版（今日头条·灵巧光束，主库 id=2351）Rust 段论断——“Rust 重写内核模块这事，去年开始悄悄推进”“不是全换，是挑最老、最难动的几块先试”“提交记录里全是 fix typo/rename var”“但一年下来，已经有三个人在用新模块跑真业务”。逐句考据（见 78.7.6 段落 P9-1~P9-4）：① “去年（2024 末）悄悄推进”**有据**——FreeBSD Rust 内核 KPI 确于 2024 年末起实验（Ayrton Muñoz rust KPI 仓库、编程之夏 2025 项目），官方 Q4 2025 状态报告称 2026 年初“足够稳定供开发者尝试”（目前可用 QEMU 播放音乐、Apple 硬件驱动测试中）；② “挑最老最难动的先试/提交全是 fix typo”方向可信（实验阶段低调提交）；③ **“已有三个人在用新模块跑真业务”无据**——官方仅称“感兴趣开发者尝试”，无生产使用记录，不得采信。该文对 Rust 推进的**方向陈述准确、生产使用修辞无据**

## 史观

- 专题语（不设总纲条号）——工程权衡：Rust 进入 base 的争论本质上是 “工程安全性” 与 “工程简洁性” 的权衡——C 语言是 FreeBSD 30 多年来的基石，C 编译器与工具链相对简单、构建快速、跨平台支持好；Rust 带来内存安全但增加工具链复杂度与构建时间；Linux 内核自 6.1（2022.12）开始接受 Rust 代码但标记为实验性，为 BSD 社区提供了参考案例
  - 辨析：
- 总纲第 21 条——革命与改革是历史方法论的分歧：Rust 争论反映了 BSD 社区中 “保守演进” 与 “革新进步” 两种哲学的张力——FreeBSD 历史上对新技术的引入一贯持审慎态度（如 ZFS 移植经历多年实验才正式进入 base、WireGuard 2021 年争议后经过两年重写才进入 14.0）；Rust 作为可能改变 base 系统语言构成的重大变更，自然需要更长时间的讨论与验证
  - 辨析：“Rust 全面取代 C”与“Rust 永不进入 base”两种极端叙事均须警惕——争论走向将取决于构建资源、维护人力与安全收益的长期权衡〔截断据上下文补全〕
- 总纲第 4 条——分离聚合是永恒规律：C 语言与 Rust 在操作系统开发中的争论是 2020 年代最重大的编程语言路线分化——Linux 选择 “实验性支持 Rust 驱动” 路径，OpenBSD 选择 “明确拒绝 Rust” 路径，FreeBSD 选择 “长期讨论、渐进探索” 路径，三种路径各有其哲学基础与工程逻辑；这种分化不是 “谁对谁错” 的问题，而是不同社区在同一技术变革面前基于自身历史与价值取向的审慎选择〔截断据上下文补全〕
- 总纲第 8 条——本体论上各方平等：Rust 争论的 “漫长但有序” 本身就是 FreeBSD 社区治理成熟的标志——没有 Core Team 强行推进或禁止，而是通过公开邮件列表讨论、会议 BOF、代码实验（如果有人做原型）形成共识；这与 1990-2000 年代 GCC vs EGCS、sendmail vs postfix、SysV init vs rc.d 等历史争论的处理方式一致
  - 辨析
- 总纲第 3 条——不存在进步，只有权力再分配：committer 自愿退役事件是开源社区治理中的常态，但资深开发者公开批评 Core Team 并以 “retiring” 作为抗议形式相对罕见；这一事件反映了 FreeBSD 松散治理模式下的张力——Core Team 作为民选机构（每两年选举一次）的决策透明度与问责性始终是社区关注议题
  - **辨析**：**必须严格区分 “committer 权限撤销” 与 “自愿退役/停止贡献”**——前者是 Core Team 正式决议剥夺某人的 commit 权限（历史上极为罕见）

## 辨析

- Somers 提案并非要求 “用 Rust 重写整个 FreeBSD” 或 “内核立即接受 Rust 代码”——提案范围非常渐进：首先引入 Rust 工具链到 base（作为 ports 之外的基础系统组件），然后允许用 Rust 编写新的用户态工具（如 nfsd、bhyve userspace 组件等），内核 Rust 支持是更遥远的可能性；截至 2026.7，**Rust 尚未进入 FreeBSD base**（内核与基础系统均无 Rust 代码），Ports 生态成熟但 base 集成仍在讨论〔截断据上下文补全〕
- “Rust 进入 FreeBSD base” 与 “Linux 内核 Rust for Linux” 需区别看待——Linux Rust 支持主要限于内核驱动（特别是新驱动可选使用 Rust），FreeBSD 提案起步是用户态工具而非内核；截至 2026.7，OpenBSD 明确拒绝 Rust（Ted Unangst 等公开反对），NetBSD 未正式讨论 Rust 入 base，DragonFly BSD 亦未见正式动议〔截断据上下文补全〕
- 需警惕两种极端叙事——一种是 “Rust 会立刻取代 C 成为 FreeBSD 主要语言”（不现实，30 多年 C 代码不可能重写），另一种是 “Rust 永远不会进入 FreeBSD base”（过于绝对，技术演进往往超出预期）；合理预期是：未来数年内 Rust 可能以有限方式进入 FreeBSD 生态（如某些可选工具、测试基础设施），但 C 语言仍将是 FreeBSD 内核与 base 系统的
- 需要区分 “邮件列表讨论热度” 与 “实际工程进展”——Rust 争论在邮件列表中持续了两年多，但这期间没有任何 Rust 代码被提交到 base，也没有 Core Team 决议要求或禁止 Rust；这种 “多讨论、少行动” 的模式在 FreeBSD 历史上并不罕见（如 ZFS 从讨论到正式进入 base 也经历了多年）
  - 文献：FreeBSD Project. Mailing List
- **必须严格区分 “committer 权限撤销” 与 “自愿退役/停止贡献”**——前者是 Core Team 正式决议剥夺某人的 commit 权限（历史上极为罕见），后者是 committer 自愿停止提交代码（较常见，原因包括工作变动、兴趣转移、对社区方向不满等）；trasz@ 事件属于后者——他的 commit bit 仍然存在，只是本人宣布不再活跃贡献；关于声明中提到的 “某事件” 具体所指，因声明语焉不详、社区解读不一〔截断留痕，细节据 163.5 节 Napierała 退役事件考据〕

## 文献

- Somers A. The Case for Rust (in the base system)[EB/OL]. (2024-01-20)[2026-07-19]. <https://lists.freebsd.org/archives/freebsd-hackers/2024-January/002823.html>; LWN.net. FreeBSD considers Rust in the base system [EB/OL]. (2024-08-19)[2026-07-19]. <https://lwn.net/Articles/985210/>. ［A］
- FreeBSD Project. freebsd-hackers@ Mailing List Archives [EB/OL]. [2026-07-19]. <https://lists.freebsd.org/archives/freebsd-hackers/>; Rust for Linux Project [EB/OL]. [2026-07-19]. <https://rust-for-linux.com/>（互联网档案馆存档，2026-07-04）
- FreeBSD Ports Collection. lang/rust [EB/OL]. [2026-07-19]. <https://cgit.freebsd.org/ports/tree/lang/rust>; Evans S, et al. Is It Time to Rewrite the Operating System in Rust?[C]. USENIX HotOS 2021.
- FreeBSD Project. FreeBSD 14.2-RELEASE Announcement (Dedication to Mike Karels)[EB/OL]. (2024-12-02)[2026-07-19]. <https://www.freebsd.org/releases/14.2R/announce/>; McKusick M K, Karels M J, Quarterman J S. The Design and Implementation of the 4.3BSD UNIX Operating System [M]. Addison-Wesley, 1989.
- FreeBSD Foundation. 2025 Annual Report [R]. Boulder: FreeBSD Foundation, 2026; FreeBSD Foundation. Sponsored Projects Blog Series [EB/OL]. [2026-07-19]. <https://freebsdfoundation.org/blog/>. ［C］

> **整改重构说明（2026-09-13）**：原“## 162.4.2 社”（截断标题）、“## 162.5.2 Karels 纪念”“## 162.5.4 Foundation 资助”三节系 163.4/163.5 拆分搬运残片，标题截断或与本 index Rust 主题无关，残片删除、文献行并入本区，内容由 163.4/163.5 节文件承载；“162.4.4”重号两节分别改挂 163.4.4/163.4.5；SECTION_GAP gaps[1-3]（163.1-163.3 无节文件）登记全库编号缺口专项。


## 163.4.4 Rust 争论史料辨析

- 要点：Rust 入 base 争论时间线：2024.1.20 Alan Somers 发起初始提案；2024.1-3 第一轮邮件列表大讨论；2024
- FreeBSD Project. Mailing List Archives [EB/OL]. [2026-07-19]. <https://lists.freebsd.org/>.［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

## 163.4.5 当代中文舆论标本——《FreeBSD 大败局》2026 版（今日头条·灵巧光束）的 Rust 论断句级考据

- 要点：自媒体《FreeBSD 大败局》2026-01-26 版（今日头条·灵巧光束，主库 id=2351）Rust
- Napierała E T. Why I am retiring from contributing to FreeBSD [EB/OL]. (2025-12-30)[2026-07-19]. <https://lists.freebsd.org/archives/freebsd-hackers/2025-December/005383.html>. ［A］


## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。
