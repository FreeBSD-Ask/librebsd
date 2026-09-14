# 96 【Linux社区】TAB选举包容术语与维护者支持

> 来源：tech-board-discuss p1（50 封全读，2007-08 至 2026-03，TAB 选举制度起源与历年提名结果、2020 包容术语 v1 补丁与反方、CoC 报告与维护者支持小组、xz 事件 TAB 层反思、LLM 重写清洁室之辩、unwind_user GPL 导出之争）
> 判定：37 CAND / 13 NV。主题分布：TAB2008自提名 1、CoC委员视角辩护 1、TAB2019自提名 1、包容术语v1补丁全文 1、语言警察伤效率论 1、TAB选举制起源 1、嵌入式长尾与GPL合规之忧 1、RISC-V系自提名 1、BPF系自提名 1、TAB2025自提名 1、TAB2020投票程序 1、2021电子投票实操困惑 1、TAB2014选举公告 1、Fixes标签日期之辩 1、IoT与精简议题自提名 1、SUSE系自提名 1、CoC报告透明度建议 1、TAB2024自提名 1、SPI路线否证 1、成熟度模型计量之难 1、LLM议题进TAB 1、TAB2019会议纪要 1、xz事件TAB层反思 1、树外追踪器ABI自治论 1、维护者支持小组提案 1、approval voting定性 1、LLM再许可法理分析 1、非公开讨论正当性 1、绩效考评条款之争 1、2016参选困境 1、TAB2014选举结果 1、TAB职能起源阐释 1、TAB2017选举公告 1、ftrace与LTTng关系定调 1、GoogleApps限额教训 1、TAB2020自提名 1、包容术语实操细分 1。

## 【Linux社区】零、体例说明

本文件系 tech-board-discuss p1（实锚 pk 9362592-9362639）的逐封提取（37 CAND / 13 NV），全 37 块采用**单行摘要体例**（丙型）：每块由“## 96.x 题名”与若干“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 96.1 TAB2008自提名

- 【Linux社区】Dave Jones 单行“Sign me up”响应 Bottomley 的 TAB 选举公告构成 2008 年自我提名记录 `<!-- ROW_MINE: tech-board-discuss.messages.9362592 -->`

## 96.2 CoC委员视角辩护

- 【Linux社区】Shuah 以 CoC 委员会成员身份反驳“CoC 只管维护者行为”论：多数报告源于对社区运作误解、幕后无声化解，两派批评皆不准确；忆 Linus“buffer cache is trivial”被 Chinner 公开指控的边缘案例；“以 CoC 处理分歧无益，但对真实违规视而不见亦无益；有 CoC 我们更好” `<!-- ROW_MINE: tech-board-discuss.messages.9362593 -->`

## 96.3 TAB2019自提名

- 【Linux社区】Greg KH 自我提名连任：列七年 TAB 履历（Linux Driver Statement、GPLv3 声明、Code of Conflict、Kernel Enforcement Statement、CoC 委员会创建、UEFI/ACPI 规格参与谈判） `<!-- ROW_MINE: tech-board-discuss.messages.9362594 -->`

## 96.4 包容术语v1补丁全文

- 【Linux社区】Dan Williams [PATCH] CodingStyle 全文：slave/blacklist 禁新增+替换词清单、inclusive-terminology.rst 64 行全文（“目标非修复过去而是最大化全球开发者参与效率”“etymological arguments do not scale”“Inclusion == global developer community efficiency”）、SoB Mason/Greg/Williams——2020 包容术语论战原始补丁 `<!-- ROW_MINE: tech-board-discuss.messages.9362595 -->`

## 96.5 语言警察伤效率论

- 【Linux社区】Willy Tarreau 反驳：非母语者已难找词、再过一层“语言警察”过滤更伤效率；若依此逻辑一切习语文化词皆当禁（blueprint 例）；建议正解＝“源于非技术世界、其义须凭历史或本地文化方能理解的词宜避免” `<!-- ROW_MINE: tech-board-discuss.messages.9362596 -->`

## 96.6 TAB选举制起源

- 【Linux社区】Bottomley 论 2007 选举方法：SPI 贡献会员制负担重（会员委员会审定程序）；择 KS 现场投票因“与会者天然满足重大贡献标准而无需争议性认定”；“我们要简单透明的过程” `<!-- ROW_MINE: tech-board-discuss.messages.9362597 -->`

## 96.7 嵌入式长尾与GPL合规之忧

- 【Linux社区】Dave Taht（2023）：曾参选 TAB 得票寥寥；LF 应重顾嵌入式 Linux 长尾、GPL 合规恶化（cambium vs ubnt“elevate”案）、FCC 网络安全标签与 title-ii 监管；“太多人信软件开发靠魔法——发 spec 就有无限免费程序员”“昔日双向契约不再被提及”；“讲真话与 show me the code 胜过与人为善” `<!-- ROW_MINE: tech-board-discuss.messages.9362598 -->`

## 96.8 RISC-V系自提名

- 【Linux社区】Palmer Dabbelt（2019）自提名：SiFive 软件团队 lead、RISC-V SW WG vice-chair、UNIX-class 平台规格 WG chair、Zephyr LF 银牌 board 代表、Embench co-chair；TAB 目标＝降低芯片厂商 SOC 上游支持门槛（boot image 共享、DT 动态化） `<!-- ROW_MINE: tech-board-discuss.messages.9362599 -->`

## 96.9 BPF系自提名

- 【Linux社区】Alexei Starovoitov（2016）自提名：1998 起 hack 内核、Facebook 内核团队、IO Visor TSC 关键成员、bcc 维护者、BPF 子系统维护者、LLVM BPF backend 维护者 `<!-- ROW_MINE: tech-board-discuss.messages.9362600 -->`

## 96.10 TAB2025自提名

- 【Linux社区】Ted Ts'o（2025-12）自提名连任：1991 起内核工作（tty/serial/dev/random/ext3）、Free Standards Group 创始 board 成员（LF 前身）、组织 Kernel Summit——“面见面包共餐的魔力邮件 IRC 无法复制”、Linux Kernel Contribution Model 主笔 `<!-- ROW_MINE: tech-board-discuss.messages.9362601 -->`

## 96.11 TAB2020投票程序

- 【Linux社区】Laura Abbott 公告 2020 选举：选民池＝LPC 与会者+三项 2019/2020 提交带 SoB/Tested/Reported/Reviewed/Acked 标签者；CIVS Condorcet 电子投票 FAQ 全文（排序选择制、选举监督员 tab-elections 列表、改票不可、练习票） `<!-- ROW_MINE: tech-board-discuss.messages.9362602 -->`

## 96.12 2021电子投票实操困惑

- 【Linux社区】Johannes Berg 问收“look for your ballot”邮件是否即在名单、与 Pinchart 同感困惑——不知该请求还是等待自动发送（2021 电子投票流程实操混乱实录） `<!-- ROW_MINE: tech-board-discuss.messages.9362603 -->`

## 96.13 TAB2014选举公告

- 【Linux社区】Bottomley 公告 2014 选举：KS Chicago 联合活动、五席三提名人（Mason/Bottomley/Linville）、提名截止至选举开始 `<!-- ROW_MINE: tech-board-discuss.messages.9362604 -->`

## 96.14 Fixes标签日期之辩

- 【Linux社区】Alejandro Colomar（2026-02）论 Fixes 标签加作者日期：日期帮人决定是否值得查（可关联同期 series）、定宽不扰目、可省哈希字符换日期；Greg 持简式立场后“我不坚持了” `<!-- ROW_MINE: tech-board-discuss.messages.9362605 -->`

## 96.15 IoT与精简议题自提名

- 【Linux社区】Josh Triplett（2016）：打算自提名、IoT 与 tinification 是主要关切、请投一票 `<!-- ROW_MINE: tech-board-discuss.messages.9362606 -->`

## 96.16 SUSE系自提名

- 【Linux社区】Jiri Kosina（2024）自提名：HID/livepatching/软驱维护者、SUSE 工程总监+distinguished engineer 主管全部 SUSE 内核开发、1996 起贡献 `<!-- ROW_MINE: tech-board-discuss.messages.9362607 -->`

## 96.17 CoC报告透明度建议

- 【Linux社区】Corbet（2024）评审 2023H2-2024Q1 CoC 报告：“Looks fine to me”；建议报告列明委员会成员以稍减不透明感 `<!-- ROW_MINE: tech-board-discuss.messages.9362610 -->`

## 96.18 TAB2024自提名

- 【Linux社区】Dan Williams 自提名连任：TAB 双重角色（向 LF 倡导内核+社区 steward）、CXL 共同维护、TEE I/O/TDISP 社区响应协调、现任 TAB 主席 `<!-- ROW_MINE: tech-board-discuss.messages.9362611 -->`

## 96.19 SPI路线否证

- 【Linux社区】Greg KH（2007）：因个人原因拒绝成为 SPI 会员——SPI 会员制选举方案的现实阻力证词 `<!-- ROW_MINE: tech-board-discuss.messages.9362612 -->`

## 96.20 成熟度模型计量之难

- 【Linux社区】Finn Thain（2023）：从没想过内核会“phone home”；私有计数执行事件亦偏快处理器/集群/快路径——贡献计量方法学不可行论证 `<!-- ROW_MINE: tech-board-discuss.messages.9362613 -->`

## 96.21 LLM议题进TAB

- 【Linux社区】Rostedt（2026-03）回应 Brauner 的 LLM 重写/清洁室再许可之问：将列入 TAB 下次会议议题——2026 TAB 议程记录 `<!-- ROW_MINE: tech-board-discuss.messages.9362614 -->`

## 96.22 TAB2019会议纪要

- 【Linux社区】Tim Bird 公开 2019-03-07 TAB 电话会议摘要：CoC 委员会五人（含 Greg KH 与 Mishi Choudhary、不与 TAB 重叠）、电子投票（Condorcet 样票成功、不宜同时换计票与投票法、缺席投票目标）、主席选举四月、维护项目资助缺口 `<!-- ROW_MINE: tech-board-discuss.messages.9362615 -->`

## 96.23 xz事件TAB层反思

- 【Linux社区】Bottomley（2024）：Lasse Collin 已获支持重返开发；三教训——信任非安全度量（须每 commit 独立评审）、内核构建产物透明度无碍（make+tarball 签名）、间接库依赖问题不适用；TAB 能做＝OpenSSF 彻底改造、主动支持面临维护者倦怠攻击的项目 `<!-- ROW_MINE: tech-board-discuss.messages.9362616 -->`

## 96.24 树外追踪器ABI自治论

- 【Linux社区】Mathieu Desnoyers（2025）：追踪器树外反有优势（只监控内核、双侧自控可实验）；但 2015 LTTng 2.7 起政策永不破坏 userspace ABI（append-only+渐进弃用）为发行版计；对齐发布周期使弃用快于内核 ABI `<!-- ROW_MINE: tech-board-discuss.messages.9362617 -->`

## 96.25 维护者支持小组提案

- 【Linux社区】Rostedt（2023）Maintainers Summit 提案全文：CoC 防了 rant 却没给维护者泄压替代；提议志愿支持名单+[MAINTAINER SUPPORT] 主题+保密准则+外部视角调解——“理想状态是 CoC 委员闲得无聊”；防预性非 CoC 替代 `<!-- ROW_MINE: tech-board-discuss.messages.9362618 -->`

## 96.26 approval voting定性

- 【Linux社区】Josh Triplett（2015）单句定性 TAB 投票规则：“this is approval voting, not range voting”——制度本质记录 `<!-- ROW_MINE: tech-board-discuss.messages.9362622 -->`

## 96.27 LLM再许可法理分析

- 【Linux社区】Bottomley（2026-03）：美国版权衍生定义推定接触即衍生、举证责任倒置极难故有清洁室双团队分离制度；LLM 难以提供分离证明、除非重现清洁室流程而成本随复杂度暴涨 `<!-- ROW_MINE: tech-board-discuss.messages.9362624 -->`

## 96.28 非公开讨论正当性

- 【Linux社区】Jason Cooper（2018）认同 Mason：此前不知“社区但非公开”讨论的主因之一是给反对者自由发言的场合——“tremendously valuable aspect，此前从未被清楚传达” `<!-- ROW_MINE: tech-board-discuss.messages.9362627 -->`

## 96.29 绩效考评条款之争

- 【Linux社区】Kees Cook（2023）评成熟度模型补丁：Level 3 措辞 fine；Level 5 删“社区反馈入绩效考评”不可——“公司必须把上游工作计入绩效考评否则将被视为自由时间、员工上游贡献不被认可” `<!-- ROW_MINE: tech-board-discuss.messages.9362630 -->`

## 96.30 2016参选困境

- 【Linux社区】Dave Taht（2016）：曾参选 TAB 因嵌入式/bufferbloat 圈外不知名得票寥寥不愿再选；望 TAB 有 IoT 成员 `<!-- ROW_MINE: tech-board-discuss.messages.9362631 -->`

## 96.31 TAB2014选举结果

- 【Linux社区】Bottomley 公告：13 人参选、五人当选——Chris Mason/John Linville/hpa/Grant Likely/Kristen Accardi `<!-- ROW_MINE: tech-board-discuss.messages.9362632 -->`

## 96.32 TAB职能起源阐释

- 【Linux社区】Bottomley（2007）：TAB＝社区与 LF 对话的信任代表；初建时从 OSDL 取得具体目标（Doc Fellowship/差旅基金/NDA 计划/硬件借阅库）；现役例＝PCI SIG 会员资格（虚拟化 vendor ID）；程序＝KS BOF 先陈述后投票 `<!-- ROW_MINE: tech-board-discuss.messages.9362633 -->`

## 96.33 TAB2017选举公告

- 【Linux社区】Chris Mason reminder v2：六提名人（Corbet/Greg/Shuah/Rostedt/Ted/Tim Bird）、布拉格 KS 10 月 25 日选举、提名声明编译在线文档 `<!-- ROW_MINE: tech-board-discuss.messages.9362634 -->`

## 96.34 ftrace与LTTng关系定调

- 【Linux社区】Rostedt（2025）：重申 unwind_user GPL 导出 draconian 立场；“不是 Mathieu 不想与上游合作而是上游不想与 Mathieu 合作”；自省曾视 LTTng 为烦扰、多年合作发现受众不同少重叠——“That's called, collaboration.” `<!-- ROW_MINE: tech-board-discuss.messages.9362635 -->`

## 96.35 GoogleApps限额教训

- 【Linux社区】Laura Abbott（2021）：3-49 commits 范围者应立即请求选票；自述发现 Google Apps 邮件限额、bcc 过多致 >50 commits 者通知或被吞——承诺明年自动化选举流程 `<!-- ROW_MINE: tech-board-discuss.messages.9362636 -->`

## 96.36 TAB2020自提名

- 【Linux社区】Olof Johansson 自提名连任：四年 TAB 经历、PowerPC/SoC 维护者、Zephyr 参与；“最骄傲时刻是把孤立工作的公司拉进社区”；主张嵌入式视角代表性 `<!-- ROW_MINE: tech-board-discuss.messages.9362637 -->`

## 96.37 包容术语实操细分

- 【Linux社区】Andy Lutomirski（2020-07-17）：whitelisted/blacklisted 句式替换难题与头脑风暴清单（quirked off/known-good list/known bad/too old/disable_autoload）；论点“blacklist/whitelist 承载多种含义、不该发明一对新万能词、替换时机恰可催生更好描述” `<!-- ROW_MINE: tech-board-discuss.messages.9362639 -->`
