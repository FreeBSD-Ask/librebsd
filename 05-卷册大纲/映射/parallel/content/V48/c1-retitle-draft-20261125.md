# V48 第 1 章改题拟稿（c1，G5 线研究子代理，2026-11-25）

> **性质**：改题**拟稿**，非落账件。写库、写树、改三台账、`title.ok`／`approvals` 重签、装配与提交一律由主会话执行。本件仅供主会话拣选。
> **范围**：第 1 章“FreeBSD 路线分歧与 DragonFly BSD 的创建（2000–2004）”12 节 48 题全数逐题人判（41 题 `open`＋7 题 `filled`）。卷／章／节题不动。
> **拟题依据**：节题构式＋`title-design/V48.tsv` 的 thesis＋实义锚（Dillon、FreeBSD 4.8、5.0／5.1、1.0／1.0A、1.2、namecache、CAM、GCC 2.95／3.4、CCVER、kgdb、SACK、Linux 2.6）＋同期经典著作题名参照件 §二（实义锚作中心语、年代／版本锚定、题长有意拉开、“的”题压至半数以下）。
> **同批规则**（V75 第 1 章三稿六规则）：冒号 0｜设问 ≤3｜题长 8—19 字上下且同节极差 ≥6｜“的”字题同节 ≤半数｜禁默认三件套｜抽象动名词尾 0｜句式族每节 ≥3。
> **题长口径**：CJK 每字计 1，拉丁字母／数字串每串计 1，标点计 1，空格不计（与 V50 呈审件“字”口径同类）。

## 一、逐题对照（48 题）

### 1.1 分叉前的技术背景：Dillon 在 FreeBSD 的工作

| subsection_id | 旧题 | 判定 | 新题 | 实锚依据 | 题长 | 句式族 |
| --- | --- | --- | --- | --- | --- | --- |
| V48.1.1.1 | FreeBSD 4.x 内核的分工格局 | 改 | Dillon 参与 VM 与 NFS 子系统 | 团队页原文 “contributed code to The FreeBSD Project and the Linux kernel for subsystems such as VM and NFS” | 9 | 双锚并列 |
| V48.1.1.2 | 子系统改造经验的积累 | 改 | 子系统清理早于自主重构 | 史页 “simplification and general cleanup of the majority of the kernel subsystems”；论文 “cleanup in the existing code base of old assumptions” | 11 | 先后 |
| V48.1.1.3 | 单系统映像构想的萌芽 | 改 | 单系统映像曾是创立期的终极目标 | 史页 “The ultimate goal … at its inception was to provide native clustering support”；论文 “future plans for clustering and single system image (SSI) support” | 16 | 判断 |
| V48.1.1.4 | 分叉前技术判断的由来 | 改 | 集群目标虽退场却未退出设计 | 史页 “although no longer the primary goal … has influenced many of the design decisions” | 14 | 转折否定 |

### 1.2 FreeBSD 4.x 时代的 SMP 改进与内核发展背景

| subsection_id | 旧题 | 判定 | 新题 | 实锚依据 | 题长 | 句式族 |
| --- | --- | --- | --- | --- | --- | --- |
| V48.1.2.1 | 大锁内核的并发状况 | 改 | 全局大锁限制了 4.x 内核的多核并发 | SMPng 文档 “interrupt handlers will immediately block on Giant”；5.0 公告 “Fine-grained locking in the kernel paves the road …” | 15 | 主谓 |
| V48.1.2.2 | 网络栈线程化的先行 | 保留 | 网络栈线程化的先行 | 既有 `filled` 块（YouTube L1）与题面相合但内容薄；形态合规（无冒号、单“的”、9 字），改题须连带动论题与证据，超本批范围 | 9 | 名词短语 |
| V48.1.2.3 | namecache 重写的技术动因 | 改 | namecache 重写被列为首要前置 | 1.2.0 发行说明 “necessary precursor for our ultimate goal of creating a clusterable OS” | 10 | 被动 |
| V48.1.2.4 | 内核改造的先后次序 | 改 | 发行说明把网络进展列在首位 | 1.2.0 发行说明 “The greatest progress has been made in the network subsystem” | 13 | 处置 |

### 1.3 FreeBSD 5.x SMPng 路线与技术分歧

| subsection_id | 旧题 | 判定 | 新题 | 实锚依据 | 题长 | 句式族 |
| --- | --- | --- | --- | --- | --- | --- |
| V48.1.3.1 | 分叉目标的自我修正 | 改 | 项目自述由 4.x 延续改为另立路线 | 史页 “originally billed as ‘the logical continuation of the FreeBSD 4.x series’ … long since become obsolete” | 14 | 主谓 |
| V48.1.3.2 | 5.x 路线的时间基准 | 改 | 5.0 与 5.1 在半年内相继发行 | 5.0 公告 2003-01-19；5.1 公告 2003-06-09 | 11 | 时点 |
| V48.1.3.3 | 并发路线的两种取向 | 改 | 锁与消息传递两路分道 | SMPng 文档细粒度锁；论文 “in place of … FreeBSD 5 branch, DragonFlyBSD uses … message passing system” | 10 | 并列 |
| V48.1.3.4 | 技术分歧的公开记载 | 改 | 分叉方公告把线程与软件包列为待办 | 公告正文仅存邮件列表（DOC_MINE 非邮件界线），题面保留公告这一实锚 | 17 | 主谓 |

### 1.4 DragonFly BSD 的开发起始与公开宣布（2003 年 6 月—7 月）

| subsection_id | 旧题 | 判定 | 新题 | 实锚依据 | 题长 | 句式族 |
| --- | --- | --- | --- | --- | --- | --- |
| V48.1.4.1 | 分叉时点的两说并存 | 改 | 分叉时点有 6 月与 7 月两说 | 史页 “forked from FreeBSD 4.8 in June of 2003”；论文 “forked off the RELENG_4 branch … on June 16, 2003” | 13 | 存在 |
| V48.1.4.2 | 周年公告的文本构成 | 改 | 周年公告走邮件列表正文 | 发布页列 1.0（2004-07-12）；OSNews 同日转引站方公告 | 11 | 主谓 |
| V48.1.4.3 | 周年自述的项目定位 | 改 | 首年自述把项目定位为成果汇报 | OSNews 引文 “One year after starting the project as a fork off the FreeBSD-4.x tree … announce our 1.0 release” | 15 | 处置 |
| V48.1.4.4 | 创建初期的工程条目 | 改 | 公告列举的工程条目构成工作面清单 | 公告正文仅存邮件列表；条目清单须以非邮件载体复核 | 17 | 的题主谓 |

### 1.5 DragonFly 创建期版本演进（2003–2004）

| subsection_id | 旧题 | 判定 | 新题 | 实锚依据 | 题长 | 句式族 |
| --- | --- | --- | --- | --- | --- | --- |
| V48.1.5.1 | 1.2 系列的后续补丁 | 改 | 1.2 系列以 SMP 修复与安全补丁为主 | 1.2.0 说明 “policy is to only commit bug fixes”；1.2.5／1.2.6 条目列 SMP 与安全修复 | 16 | 主谓 |
| V48.1.5.2 | 首个发行版的功能限度 | 改 | 1.0 仍沿用旧的线程模型 | 1.0 公告 “still using the old 4.x pthreads model”（邮件载体，待非邮件复核） | 10 | 主谓 |
| V48.1.5.3 | 1.0 与 1.0A 的次序 | 改 | 1.0A 紧随 1.0 两日发行 | 发布页 “1.0 (July 12, 2004)”／“1.0A (July 14, 2004)” | 12 | 时点 |
| V48.1.5.4 | 镜像补丁的交付手段 | 改 | 镜像以 xdelta 增量补丁交付 | 1.0A 交付细节仅存公告与镜像页（邮件载体），暂标待核 | 11 | 工具介词 |

### 1.6 创建期贡献者构成与 committer 变化（2003–2004）

| subsection_id | 旧题 | 判定 | 新题 | 实锚依据 | 题长 | 句式族 |
| --- | --- | --- | --- | --- | --- | --- |
| V48.1.6.1 | 创建期贡献者名单的构成 | 改 | 项目页公开列出创建期参与者名单 | 团队页 “Listed here are some of the people …”“Here's the list but it may be incomplete” | 16 | 主谓 |
| V48.1.6.2 | 核心贡献者的长期留存 | 保留 | 核心贡献者的长期留存 | 既有 `filled` 块（committer 名录与 DEEP 分析）承载留存读数；单“的”、10 字，形态合规 | 10 | 名词短语 |
| V48.1.6.3 | 提交者名录的署名惯例 | 改 | committer 名录以邮件前缀标示署名 | 团队页 “To send an email to one of the committers append dragonflybsd.org.” | 11 | 介词 |
| V48.1.6.4 | 分叉期人事的延续性 | 改 | 创建期人事在后续世代持续接力 | 团队页名录与史页 “intervening years” 的长期开发自述 | 14 | 主谓 |

### 1.7 分叉必要性的技术争论与外部批评、回应（2003–2004）

| subsection_id | 旧题 | 判定 | 新题 | 实锚依据 | 题长 | 句式族 |
| --- | --- | --- | --- | --- | --- | --- |
| V48.1.7.1 | 分叉成果的技术论点 | 改 | 公告把线程与网络基础设施列为首要成果 | 1.0 公告 “replaced nearly all of the core threading, process, interrupt, and network infrastructure”（邮件载体） | 19 | 处置 |
| V48.1.7.2 | 首版稳定性的外部压力 | 改 | 首版稳定性的落差被发行说明承认 | 1.2.0 说明 “far more stable then our 1.0A release” | 16 | 被动 |
| V48.1.7.3 | 待完成事项的公开列表 | 改 | 待办事项在发行说明中公开 | 1.4.0 说明 “We do not always get every last little fix into a release” | 12 | 介词 |
| V48.1.7.4 | 自评与外部评价的落差 | 改 | 早期自述已被官方史页判为过时 | 史页 “this description has long since become obsolete” | 15 | 主谓 |

### 1.8 技术继承与自主重构：FreeBSD 基础代码、BSD 用户空间、自主内核改造

| subsection_id | 旧题 | 判定 | 新题 | 实锚依据 | 题长 | 句式族 |
| --- | --- | --- | --- | --- | --- | --- |
| V48.1.8.1 | FreeBSD 基础代码的沿用 | 改 | 基础代码沿用 FreeBSD 4.x 分支 | 论文 “source base was forked off the RELENG_4 branch of FreeBSD” | 10 | 主谓 |
| V48.1.8.2 | BSD 用户空间的取材 | 保留 | BSD 用户空间的取材 | 既有 `filled` 块（pkgsrc／NetBSD 取材）与题面相合；单“的”、8 字，形态合规 | 8 | 名词短语 |
| V48.1.8.3 | 内核自主改造的覆盖面 | 改 | 改造覆盖文件系统接口与内核核心 | 史页 “great deal of work in nearly every subsystem, particularly the filesystem APIs and kernel core” | 16 | 主谓 |
| V48.1.8.4 | 工具链来源的更替 | 改 | 编译器默认值经 CCVER 过渡 | 1.2.0 说明 “CCVER environment variable (‘gcc2’ or ‘gcc34’)”；1.4.0 说明 “GCC 3.4 is now the default compiler” | 10 | 介词 |

### 1.9 创建期安全维护机制与漏洞通报渠道（2003–2004）

| subsection_id | 旧题 | 判定 | 新题 | 实锚依据 | 题长 | 句式族 |
| --- | --- | --- | --- | --- | --- | --- |
| V48.1.9.1 | 安全修复的分支策略 | 改 | 发行分支只回合并兼容性修复 | 1.2.0／1.4.0 说明 “policy is to only commit bug fixes to release branches” | 14 | 主谓 |
| V48.1.9.2 | 通报渠道的邮件载体 | 改 | 缺陷与提交两类邮件列表联动缺陷库 | 团队页“邮件前缀”惯例＋史页“mailing list…bug submission system”（论文） | 18 | 双锚并列 |
| V48.1.9.3 | 安全补丁的随版发布 | 改 | 补丁版逐条列出所修安全漏洞 | 1.2.5 “security fix for a libz overflow”；1.2.6 列 tcp 序列号漏洞 | 14 | 主谓 |
| V48.1.9.4 | 漏洞信息的公开节奏 | 改 | 漏洞信息以版本为披露节拍 | 1.2.0 说明逐版列安全条目，披露依附版本 | 13 | 介词框架 |

### 1.10 创建期的代码继承与工具来源（2003–2004）

| subsection_id | 旧题 | 判定 | 新题 | 实锚依据 | 题长 | 句式族 |
| --- | --- | --- | --- | --- | --- | --- |
| V48.1.10.1 | 编译器默认值的更替 | 保留 | 编译器默认值的更替 | 既有 `filled` 块（CCVER 并存两代 GCC）承担该题；单“的”、9 字，形态合规 | 9 | 名词短语 |
| V48.1.10.2 | 外部工具的引入渠道 | 改 | 调试器由 gdb -k 改为独立 kgdb | 项目日记 “Get rid of gdb -k, replace with a separately built kgdb” | 16 | 转换 |
| V48.1.10.3 | 基础工具的版本更新 | 改 | OpenSSH 与 ncurses 随版本整体更新 | 1.2.0 说明 “OpenSSH updated to 3.9p1”“ncurses updated to 5.4”“dhcp udpated to 3.0” | 12 | 双锚主谓 |
| V48.1.10.4 | 源码树的版本管理 | 保留 | 源码树的版本管理 | 既有 `filled` 块（cvsup 取源码重建）与题面相合；单“的”、8 字，形态合规 | 8 | 名词短语 |

### 1.11 创建期与 FreeBSD 的关系（2003–2004）

| subsection_id | 旧题 | 判定 | 新题 | 实锚依据 | 题长 | 句式族 |
| --- | --- | --- | --- | --- | --- | --- |
| V48.1.11.1 | 上游依赖的具体面向 | 改 | 基础能力自 FreeBSD 引入 | 项目日记 “Bring in SHA256 support from FreeBSD.” | 8 | 介词 |
| V48.1.11.2 | 同步式引入的子系统 | 改 | CAM 子系统整块同步并附本地修补 | CAM 同步见项目日记与提交记录（待逐条核锚） | 12 | 主谓 |
| V48.1.11.3 | 差异化的内核路线 | 改 | BSD 基座向另一方向生长 | 论文 “maintain the high quality and performance of the FreeBSD 4 branch, while exploring new concepts” | 9 | 主谓 |
| V48.1.11.4 | 分叉关系的长期读法 | 改 | 分叉是长期分化而非一次性事件 | 史页 “rapid and ever increasing development since the fork”“intervening years” | 15 | 判断否定 |

### 1.12 与同时期操作系统的比较：FreeBSD 5.x 与 Linux 2.4–2.6

| subsection_id | 旧题 | 判定 | 新题 | 实锚依据 | 题长 | 句式族 |
| --- | --- | --- | --- | --- | --- | --- |
| V48.1.12.1 | 比较窗口的时间基准 | 保留 | 比较窗口的时间基准 | 既有 `filled` 块（FreeBSD 5.1，2003-06）承担该题；单“的”、9 字，形态合规 | 9 | 名词短语 |
| V48.1.12.2 | 并发模型的两条分野 | 改 | 两方分别深推大锁与另立令牌层 | SMPng 细粒度锁＋论文“partitioning and replication … message passing”；史页“the token” | 15 | 并列 |
| V48.1.12.3 | SACK 与千兆网性能调优 | 保留 | SACK 与千兆网性能调优 | 既有 `filled` 块（SACK／GigE）与题面相合；双锚名词题、10 字，形态合规 | 10 | 双锚名词 |
| V48.1.12.4 | Linux 2.6 的参照位置 | 改 | Linux 在 2.6 之后改标 rc 后缀 | kernel.org 2.6 归档与 LWN 版本方案记载（待逐条核锚） | 10 | 主谓 |

## 二、分布自检（48 题）

- **冒号**：0（全章）。
- **设问**：0（配额 ≤3，未用）。
- **“的”字题**：11/48（22.9%）；逐节 0—2/4，均 ≤ 半数（1.2、1.10 各 2/4 为上限）。
- **题长**：8—19；逐节极差：1.1＝7（9—16）｜1.2＝6（9—15）｜1.3＝7（10—17）｜1.4＝6（11—17）｜1.5＝6（10—16）｜1.6＝6（10—16）｜1.7＝7（12—19）｜1.8＝8（8—16）｜1.9＝6（12—18）｜1.10＝8（8—16）｜1.11＝7（8—15）｜1.12＝6（9—15）。
- **句式族**：双锚并列／先后／判断／转折否定／主谓／被动／处置／存在／时点／介词／工具介词／转换／名词短语／并列——逐节 ≥3。
- **抽象动名词尾**：0（题尾均为具体名词、动词或专名，无“的实现／的引入／的演变”类收尾）。
- **默认三件套**：0（全章不套“背景—过程—影响”或“概况／特点／意义”同名三段式）。

## 三、保留题说明（7 题 `filled`）

7 题 `filled`（1.2.2、1.6.2、1.8.2、1.10.1、1.10.4、1.12.1、1.12.3）**全数保留**，不列入改题面。保留理由统一为：树内既有块（ROW_MINE／DEEP）承载的论题与旧题相合，改题须同批改 `thesis` 与证据行（《小节建制与题名规则》§8.1“改题同批三件套”），超出本拟稿范围；且七题形态均无冒号、单“的”、长度 8—10，符合六规则。若主会话决定连带动论题，建议按上表“新题”列同批改账。

## 四、需主会话裁定项

1. **`filled` 七题是否连带动 `thesis`／证据行**：本稿一律保留，仅拟稿层面合规；若要求全章题面风格统一，须另开内容批（涉及块内容，不得由子代理动）。
2. **1.9.2／1.11.2／1.12.4 三题的实锚**：题面已锚到“两类邮件列表＋缺陷库”“CAM 整块同步”“rc 后缀”，但当前证据仅够线索级，落账前应补一手锚或改题面。
3. **1.1.1 的“参与／分担”措辞**：团队页只记“contributed code … for subsystems such as VM and NFS”，未记“维护者”身份；本稿用“参与”，若主会话另有访谈可证“维护”，可升级措辞。
