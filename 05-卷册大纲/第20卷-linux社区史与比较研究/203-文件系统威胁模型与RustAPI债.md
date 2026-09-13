# 203. 文件系统威胁模型、Rust 绑定 API 债与 fwctl 信任赤字（ks p67）

> 来源：ksummit 独有 p67（库尾页 35 封全读，2023-08 至 2024-06：Ted Ts'o 系统陈述文件系统威胁模型存储设备属可信计算基损坏镜像不算安全漏洞并揭露 syzbot 计数的黑暗模式操纵与云场景不适用性；Pinchart 以 V4L2/DRM 对象生命周期 API 无法安全使用为例论证 Rust 绑定须先重写底层 API 被斥过度刨毛点出维护者负担真实结构；Miguel Ojeda 确认 Rust 最低编译器版本政策跟随 Debian Stable 系维护者峰会公开决定；Dan Williams 概括 fwctl 三年会议共识与跨子系统 NAK 的信任赤字本质并援引 MGLRU 在 LSF/MM 2022 面对面破冰先例；Bugzilla 争议四封、设备直通争议三封）
> 判定：29 CAND / 6 NV。主题分布：安全披露流程 1、Bugzilla 争议 4、维护者负担分担 1、Rust 绑定与 API 债 1、C 聚合传递争论 2、维护者峰会筹备 1、稳定分支提交标签 2、设备直通争议 3、文件系统信任与维护 3、AI 代码版权与 DCO 1、内存分配 API 1、专家社区建设 1、Rust 与全树重构 1、API 弃用政策 1、补丁抄送流程 1、倦怠与社区支援 1、kernel.org 信任体系 1、AI 贡献标注 1、HIGHMEM 淘汰 1、stable 维护义务 1。

## 203.1 安全披露流程

- 【Linux社区】Jiri Kosina 赞同 Linus 反对 linux-distros 强制共享 PoC；支持闭列表 distros@kernel.org 提案，愿征询 SUSE 安全团队意见，坚持发行版必须进入内核安全修复流程。 `<!-- ROW_MINE: ksummit.messages.10565 -->`

## 203.2 Bugzilla 争议

- 【Linux社区】Artem 以数据反驳“骚扰”论：Bugzilla 每周约 20 份报告、单人最坏每周不足 5 封；举 bug 204807 两年半 255 条评论为例，称邮件模式无法承载此类协作。 `<!-- ROW_MINE: ksummit.messages.10569 -->`
- 【Linux社区】Randy Dunlap 指 Bugzilla 大量组件无负责人、“我们主动让报告被忽视”；引 Stephen 称网络报告只能转 netdev、乐见其亡；Leemhuis 称三年无改善并附 LWN 链接。 `<!-- ROW_MINE: ksummit.messages.10583 -->`
- 【Linux社区】Steven Rostedt 称社区只为生存行动，Meltdown/Spectre 才迫使 -rc 末期大改；肯定发行版开发者代为分诊质量高，志愿者 Slade 可任 Bugzilla 与维护者间联络人。 `<!-- ROW_MINE: ksummit.messages.10584 -->`
- 【Linux社区】Konstantin Ryabitsev 直言“维护者要的是补丁，不是 bug 报告”，让资深工程师做一线 QA 必致双方皆怨；警告强制订阅只会令 Bugzilla 被全员拉黑。 `<!-- ROW_MINE: ksummit.messages.10603 -->`

## 203.3 维护者负担分担

- 【Linux社区】Daniel Vetter 称网络子系统约 2020 年才改群体维护、值得向峰会介绍；GPU 流程自 2018 年未变，gitlab.freedesktop.org 的内核 CI 整合有望本合并窗口落地。 `<!-- ROW_MINE: ksummit.messages.10575 -->`

## 203.4 Rust 绑定与 API 债

- 【Linux社区】Laurent Pinchart 称 V4L2/DRM 对象生命周期 API 坏到“无法安全使用”，Rust 绑定须先彻底重写底层却被斥“过度刨毛”；主张 C/Rust 两阵营合作还 API 债以换维护者支持。 `<!-- ROW_MINE: ksummit.messages.10577 -->`

## 203.5 C 聚合传递争论

- 【Linux社区】Rust 设计团队成员 Ralf Jung 阐明 union 语义：允许任意字节重解释、无“活跃变体”，但 bool 须为 0/1 否则 UB；反驳“语言须定义 bool 非法值行为”的指责。 `<!-- ROW_MINE: ksummit.messages.10582 -->`
- 【Linux社区】HUANG Zhaobin 以 godbolt 实测反驳“C++ 才有隐藏指针”论：C 与 C++ 均传隐藏指针，gcc 在 C 侧多一次拷贝、C++ 走 NRVO，clang 两语言代码相同。 `<!-- ROW_MINE: ksummit.messages.10622 -->`

## 203.6 维护者峰会筹备

- 【Linux社区】Linus 为峰会“Linus 环节”征集预备考题：请 Corbet 匿名代收维护流程痛点、只转交个人意见勿公开讨论；自称“大声者”，建议加强主持以免少数人垄断发言。 `<!-- ROW_MINE: ksummit.messages.10587 -->`

## 203.7 稳定分支提交标签

- 【Linux社区】James Bottomley 反对新增 not-stable 标签：Fixes 回答补丁来源、是否回传属事后可能推翻的判断，可另走 stable 通道兜底；该标签实为阻止非修复提交混入 stable。 `<!-- ROW_MINE: ksummit.messages.10589 -->`
- 【Linux社区】Mauro 建议 pre-git 修复以 Link 指向 tglx history 树（Bitkeeper 史前库）URL，而非 Fixes 引用其哈希，以免校验和冲突与异树误读；保留 Fixes: 1da177e4c3f4。 `<!-- ROW_MINE: ksummit.messages.10652 -->`

## 203.8 设备直通争议

- 【Linux社区】Ricardo Ribalda 引 linuxtv.org 声明：V4L2 不接受含未公开闭源特性的驱动，故“厂商获得 vendor 访问”无从谈起；否认有人提议向用户态开放 PCI 寄存器。 `<!-- ROW_MINE: ksummit.messages.10591 -->`
- 【Linux社区】Dan Williams 称 fwctl 历经三年会议已成多方共识，RDMA 与 netdev 的跨子系统 NAK 缺的是信任而非技术；引 MGLRU 在 LSF/MM 2022 面对面破冰为例，主张再试调解。 `<!-- ROW_MINE: ksummit.messages.10601 -->`
- 【Linux社区】Laurent Pinchart 回应专利论：OIN 保护伞理论有效，但专利恐慌多系大型 SoC 厂商自造，某公司“工程由律师管理”；不能既造专利乱局又以专利为由拒公开。 `<!-- ROW_MINE: ksummit.messages.10649 -->`

## 203.9 文件系统信任与维护

- 【Linux社区】Dave Chinner 提社区维护文件系统最低门槛：须有可用 mkfs/fsck 并入 fstests；建议以 fstype 标志而非配置项标记受支持、弃用、待移除状态；老盘数据可靠 VM 启动旧发行版读取。 `<!-- ROW_MINE: ksummit.messages.10593 -->`
- 【Linux社区】Ted Ts'o 实测列举 27 个支持 generic_file_mmap 的简单文件系统（fat、hfsplus、ntfs3、exfat 等），反驳“文档场景会回退 read/write”的假设，佐证 mmap 攻击面广。 `<!-- ROW_MINE: ksummit.messages.10613 -->`
- 【Linux社区】Ted Ts'o 论威胁模型：存储设备属可信计算基，损坏镜像不算安全漏洞；syzbot 计数互不可比、系“黑暗模式”操纵；云端本假定攻击者有 root，真险在 GNOME 自动挂载，e2fsprogs 将加 udev 规则缓解。 `<!-- ROW_MINE: ksummit.messages.10625 -->`

## 203.10 AI 代码版权与 DCO

- 【Linux社区】Paul McKenney 讨论纯 AI 代码版权：美国版权局认定非人类作者无版权、纯 AI 代码近乎公有领域；但他强调美国是判例法域、解释可回溯变更，且内核须顾及美国以外法域。 `<!-- ROW_MINE: ksummit.messages.10597 -->`

## 203.11 内存分配 API

- 【Linux社区】Miguel Ojeda 澄清 Rust 最低编译器版本政策为跟随 Debian Stable，系维护者峰会公开决定；辩称等待上游分配器无果后才转向，本可更早行动。 `<!-- ROW_MINE: ksummit.messages.10600 -->`

## 203.12 专家社区建设

- 【Linux社区】Dave Airlie 主张培育跨厂商专家社区：habanalabs 编译器后端是 LLVM 分叉应上游化；“只有本公司懂自家硬件”是保留控制权的借口；倡议共享运行库仓库与上游优先流程。 `<!-- ROW_MINE: ksummit.messages.10610 -->`

## 203.13 Rust 与全树重构

- 【Linux社区】Mike Rapoport 指核心 API 一旦有 Rust 抽象，全树重构者即须懂 Rust 并协调抽象维护者；而大型重构多由非维护者完成，维护者未必有空协助，扩展性堪忧。 `<!-- ROW_MINE: ksummit.messages.10612 -->`

## 203.14 API 弃用政策

- 【Linux社区】Linus 表态并行 API 并存完全正常，devm_xyz 与 xyz 将永远共存；反对“弃用”话术与指责旧接口用户：“懒得不转换全部用户者，无权要求他人代劳”。 `<!-- ROW_MINE: ksummit.messages.10623 -->`

## 203.15 补丁抄送流程

- 【Linux社区】Steven Rostedt 主张只抄送触及自身代码的单个补丁而非 20 封整系列，整系列反而易漏审；lore.kernel.org/r/<message-id> 可一键取回全线程，lore 已化解“信息孤岛”。 `<!-- ROW_MINE: ksummit.messages.10627 -->`

## 203.16 倦怠与社区支援

- 【Linux社区】Dan Williams 详述倦怠支援：自述参加 LPC 圆桌后 Dr. Chance 一对一随访；支持设志愿名单，认为子系统例会、聊天频道与非正式聚会可减压；追问 LF 赞助咨询实际使用率。 `<!-- ROW_MINE: ksummit.messages.10634 -->`

## 203.17 kernel.org 信任体系

- 【Linux社区】Greg KH 披露 kernel.org 正与 OpenSSF 合作设计分布式信任框架以替代自研 Web of Trust，二月会议公布；确认需“重建”信任网，理想是对现有 gpg 用法透明替换。 `<!-- ROW_MINE: ksummit.messages.10638 -->`

## 203.18 AI 贡献标注

- 【Linux社区】Mark Brown 提议以“written by / translated by”区分 AI 撰写与翻译润色，主张统一谈“工具”而非仅针对 LLM，避免纠缠工具实现细节的规则博弈。 `<!-- ROW_MINE: ksummit.messages.10644 -->`

## 203.19 HIGHMEM 淘汰

- 【Linux社区】Richard Weinberger 举证 PAGE_OFFSET 影响：客户设备 2G/2G 分割令 JRE 地址空间受限，改回 3G/1G 解决；自称顾问仍时遇 Java 工作负载。 `<!-- ROW_MINE: ksummit.messages.10647 -->`

## 203.20 stable 维护义务

- 【Linux社区】Sasha Levin 反对将 stable 义务强加主线开发者：重申 stable 首条规则是不给未参与者增负，拒当执法者并反问“违规者是否要禁止上游提交”。 `<!-- ROW_MINE: ksummit.messages.10663 -->`
