---
chapter: 第 14 章
id: CH14
volume: 第01卷-unix的起源
---

# 第 14 章 unix习俗考据与都市传说辨析

## 要点

- V6 UNIX 内核中著名的注释 `/* You are not expected to understand this */` 位于进程上下文切换相关代码段（约第 2240-2243 行处，注释本身在第 2238 行），涉及交换标志 SSWAP 与进程切换的晦涩代码；该注释因作者对代码晦涩度的自我调侃而成为 UNIX 史上最著名的代码注释之一，是 UNIX 早期代码文化与“内核代码晦涩难懂”集体

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3599] 卷“第01卷-unix的起源”第 14 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3600] 卷“第01卷-unix的起源”第 14 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3602] 卷“第01卷-unix的起源”第 14 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3605] 卷“第01卷-unix的起源”第 14 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3607] 卷“第01卷-unix的起源”第 14 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3636] 卷“第01卷-unix的起源”第 14 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3652] 卷“第01卷-unix的起源”第 14 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3653] 卷“第01卷-unix的起源”第 14 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_1532] 卷“第01卷-unix的起源”第 14 章，匹配置信度 0.9，原因：关键词搜索下载文献，标题含章节主题
- [DB:references_fulltext:chapter_matches:chmatch_1172] 卷“第01卷-unix的起源”第 14 章，匹配置信度 0.6，原因：无匹配
- [DB:historical_claims:claim] 关键词行级挖掘素材线索 14.16-关键词行级挖掘素材线索（2 条，CL-RM 段，见 14.16-关键词行级挖掘素材线索.md）

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 该注释的具体作者存在争议——通常被归为 Dennis Ritchie 或 Ken Thompson，但无一手史料确证作者，二者本人均未在公开场合明确认领；注释的确切语义（SSWAP 交换标志与 u.u_eeav 错误处理的上下文）需结合 V6 内核进程调度源码考据；按 0 信任原则，将注释作者归为“Bell Labs 内核开发者群体”而非单一人物更稳妥

## 文献

- Salus P H. A Quarter Century of UNIX [M]. Reading: Addison-Wesley, 1994；UNIX V6 Source Code (TUHS Archive research/Dennis_v6)；McKusick M K, Bostic K, Karels M J, Quarterman J S. The Design and Implementation of the 4.4BSD Operating System [M]. Reading: Addison-Wesley, 1996 ［B］

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP509、BSD Now EP362、BSD Now EP209（共 3 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 该期转述 Rob Pike 关于 Unix 文件命名中 . 与 .. 及点开头文件起源的帖子：dot 与 dotdot 在文件系统层次化时加入，ls 程序中以名称首字符为点则跳过的简短判断省略了显式比较，这一偷懒写法意外创造了隐藏文件惯例。（BSD Now EP509，[1165.36-1285.62]，L2）
- Pike 指出该惯例带来双重后果：一是为后续程序员树立了错误先例，二是催生了点文件概念，导致大量程序将配置文件散落到用户主目录，数十年间造成 bug、CPU 周期浪费与人为困扰。（BSD Now EP509，[1236.02-1297.66]，L2）
- Pike 澄清点文件的价值来自文件本身而非命名惯例，Plan 9 即通过 $home/cfg 与 $home/lib 等目录替代点文件，说明这一 Unix 惯例并非必然。（BSD Now EP509，[1293.22-1312.32]，L2）
- 其余新闻包括 Clara 以 OpenZFS 构建存储设备的商用考量、OpenBSD 7.3 的 VirtualBox 安装、radicale CalDAV/CardDAV 自建服务、OpenBGPD 8.0 引入 FlowSpec 以及 OpenBSD VMD 转向多进程设备模拟模型。（BSD Now EP509，[78.38-372.82]，L2）
- Warner Losh 自述 2.11BSD 复原工程：因原始磁带由 Usenix 分发且早期母带重制，现仅存 patch level 195（约发布 18 个月后），他通过 2.10.1BSD、4.3BSD 等来源拼合出 patch level 0。（BSD Now EP362，[774.42-1103.02]，L1）
- 2.11BSD 的 patch 以 shell 脚本、uuencode 压缩 tar 等格式发布，部分指令破坏信息，无法简单用 patch -R 逆向。（BSD Now EP362，[884.78-912.34]，L1）
- Warner 自述曾因疫情失眠而以复原工程为消遣，最终重建出可启动的原始系统磁带，并计划把每个 patch 转为 git commit。（BSD Now EP362，[964.58-1472.50]，L1）
- 关于 sync：早期 Unix 没有 reboot 命令，靠 sync 后断电；连续三次 sync 是人为延时的误传，各 BSD 内核的 sync 只调度写盘而不等待完成。（BSD Now EP362，[2597.68-2885.24]，L1）
- FreeBSD 基金会执行董事 Deb Goodkin 2017 年 5 月访华，参加 LinuxCon China 与 KOPU（中国开源软件推进联盟）峰会并演讲介绍 FreeBSD 优势；此行促成 Kylie Liang（微软）加入董事会、华为捐赠，并推动中国社区与亚洲地区的拓展。（BSD Now EP209，[66.36-530.50]，L2）
- 该期介绍 Unix 信号机制：kill 命令、SIGKILL 与 SIGSTOP 不可被捕获或忽略、SIGHUP 传统上用于让守护进程重载配置；Linux 用 /proc 查看信号掩码，FreeBSD 用 procstat -i 输出更易读的捕获/忽略/阻塞状态。（BSD Now EP209，[546.70-855.66]，L2）
- Matthew Dillon 在 DragonFly BSD News 公告内核内置统计收集器：每 10 秒采样一次机器状态并写入内核 FIFO（约 8K 条、23 小时数据），用户态工具 kcollect 可配合 gnuplot 绘图。（BSD Now EP209，[1771.52-1922.38]，L2）
- SmartOS 开发者 Ryan Zezeski 用 DTrace 与 MDB 追踪非全局区域 IP 隧道重启后消失的回归，最终定位为自己早前为修另一缺陷所做的一行修改，误把区域内自建链路标记为从主机借入（on loan）。（BSD Now EP209，[874.34-1520.52]，L2）
- Ken Thompson 2009 年在 Go 语言早期提交中为 O_CREAT 增加拼写别名并附注“spell it with an E”，称这是 Unix 原始设计“去掉几个字母”的遗憾之一，属 Unix 历史的可追溯遗存。（BSD Now EP209，[4080.36-4160.92]，L2）

**史料**：

- Rob Pike 关于 dot 文件命名起源的 Google+ 帖子，为当事人对 Unix 早期实现的一手回忆，经当期节目转述。（BSD Now EP509，[1165.36-1312.32]，L2）
- OpenBGPD 8.0 发布公告，涉及 RPKI ASPA、FlowSpec 支持与便携版可运行平台列表，为官方公告线索，经节目转述。（BSD Now EP509，[1908.46-2010.06]，L2）
- Clara Systems 关于以 OpenZFS 构建自有存储设备的文章，含数据保护、快照、压缩与商用许可等要点，为经节目转述的二手技术文本。（BSD Now EP509，[78.38-372.82]，L2）
- Warner Losh 本人口述及博客、Twitter 记录，涉及 Usenix 磁带分发、TUHS 档案与 patch 链。（BSD Now EP362，[774.42-1826.06]，L1）
- Unix Heritage Society（TUHS）由 William Toomey 创立，保存代码、二进制、论文扫描件与早期商业发行的私有档案。（BSD Now EP362，[2022.96-2260.64]，L1）
- Deb Goodkin 中国行报告；DragonFly BSD News 中 Matthew Dillon 的统计收集器公告；SmartOS GitHub issue 737 及 Ryan Zezeski 的调试分析；Go 语言中 Ken Thompson 的 O_CREAT 提交。（BSD Now EP209，[66.36-4160.92]，L2）

**史观**：

- 总纲5 没有必然性，只有偶然性：点文件惯例出自实现细节的偶然简化，并非历史必然。：隐藏文件惯例源于 ls 的一次偷懒简化，而非有意的设计选择。（BSD Now EP509，[1209.90-1285.62]，L2）
- 总纲10 动手者创造历史：点文件惯例由早期实现者的一行判断形塑，体现动手者决策的历史权重。：一个具体实现者的简化判断塑造了长达数十年的文件组织惯例，动手者的偶然决策成为历史惯例。（BSD Now EP509，[1209.90-1285.62]，L2）
- 总纲22 知识注定过时：点文件惯例被 Plan 9 重新设计所替代，既有技术惯例随新系统而失效。：Pike 本人亦反思该早期决策，Plan 9 以不同方案替代，显示既定知识可被重新审视。（BSD Now EP509，[1293.22-1312.32]，L2）
- 总纲19 解释学循环是历史认识的根本条件：复原工程通过现存 patch 链与早期二进制格式博客互相印证，构成解释学循环的认识过程。（BSD Now EP362，[1076.58-1268.54]，L2）
- 总纲22 知识注定过时：早期二进制格式与工具链需借助旧模拟器与二进制工件才能重建，说明工具知识会随代际过时。（BSD Now EP362，[678.42-758.62]，L1）
- 总纲10 动手者创造历史：中国社区的拓展由 Deb、Kylie 等具体个人与组织接触逐步推动，而非抽象的市场力量，体现动手者与偶然性在社区史中的直接作用。（BSD Now EP209，[66.36-530.50]，L2）

**辨析**：

- 该 dot 文件起源叙述来自 Rob Pike 的事后回忆，其细节（如 dotdot 是否于版本 2 重写时加入）作者本人亦标注并非确定，需结合 Unix 早期源码与历史文档核验。 [存疑脚注] dot 与 dotdot 引入版本为作者模糊回忆，需以 Unix V1/V2 文件系统源码考据确认。（BSD Now EP509，[1184.70-1209.90]，L4）
- 关于该惯例已存在四十年或五十年的时间表述在节目转述中并不精确，且与 Unix 文件系统层次化时间线可能冲突，须以文件系统源码与历史文献为准。 [存疑脚注] 时间跨度表述存在口语化波动，须以源码时间线重新核算。（BSD Now EP509，[1348.32-1361.48]，L4）
- 2BSD 系列早期版本号（2.8 至 2.11）与缺失版本（如 2.6/2.7）的编号逻辑，Warner 亦无法确证，仅推测与磁带编号相关。 [存疑脚注] 版本号缺口原因待原始档案确认（BSD Now EP362，[802.42-826.70]，L4）

**文献**：

- [BSD Now EP509] Pennington J. BSD Now: 509: Dot File Naming[EB/OL]. (2023-06-01)[2026-08-15]. <https://www.bsdnow.tv/509>.
- [BSD Now EP362] Pennington J. BSD Now: 362: 2.11-BSD restoration[EB/OL]. (2020-08-06)[2026-08-15]. <https://www.bsdnow.tv/362>.
- [BSD Now EP209] Pennington J. BSD Now: 209: Signals: gotta catch ‘em all[EB/OL]. (2017-08-30)[2026-08-15]. <https://www.bsdnow.tv/209>.

<!-- /PODCAST_REVIEW -->

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

