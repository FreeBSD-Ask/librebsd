---
chapter: 第 18 章
id: CH18
volume: 第01卷-unix的起源
---

# 第 18 章 小型机的诞生与 DEC PDP 谱系

## 要点

DEC PDP 系列小型机（PDP-1至PDP-11）的诞生标志着计算从大型机向小型化的关键转折：PDP-7是UNIX的最初开发平台，PDP-11则是UNIX扩散与C语言移植的决定性硬件载体。DEC的模块化设计理念——以UNIBUS总线与PDP-11的MMU为代表——在技术层面为多用户分时系统提供了物质基础，但其“为 UNIX 而生”的叙事本身就是一种后见之明的形式主义重构。PDP-11的16位寻址空间限制（64KB直接寻址）在UNIX发展初期既构成了约束也激发了创新——如分离指令与数据空间（I/D space）的引入。

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3619] 卷“第01卷-unix的起源”第 18 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_1536] 卷“第01卷-unix的起源”第 18 章，匹配置信度 0.9，原因：关键词搜索下载文献，标题含章节主题
- [DB:bsdnow_podcast:outline_mappings:om_10434] BSD Now 第 675 期，匹配 CH18 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10449] BSD Now 第 671 期，匹配 CH18 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10476] BSD Now 第 665 期，匹配 CH18 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10496] BSD Now 第 663 期，匹配 CH18 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10508] BSD Now 第 661 期，匹配 CH18 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10519] BSD Now 第 659 期，匹配 CH18 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10531] BSD Now 第 655 期，匹配 CH18 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10573] BSD Now 第 648 期，匹配 CH18 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10597] BSD Now 第 644 期，匹配 CH18 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10614] BSD Now 第 641 期，匹配 CH18 章，关联度 1.0
- [DB:historical_claims:claim] 关键词行级挖掘素材线索 18.5-关键词行级挖掘素材线索（1 条，CL-RM 段，见 18.5-关键词行级挖掘素材线索.md）

## 史观

PDP-11 作为 UNIX 母机的地位存在叙事风险——将 PDP-11 与 UNIX 的共生关系本质化为“天作之合”可能掩盖了历史的偶然性。UNIX 最初是为 PDP-7 编写的，PDP-11 的引入是后来的升级；UNIX 在 PDP-11 上的成功部分源于 PDP-11 的内存管理单元（MMU）恰好支持 UNIX 的多用户需求，但这不是“设计”而是“巧合”。DEC 在 1990 年代被 Compaq 收购、最终消亡，其硬件遗产主要通过 PDP-11 模拟器（如 SIMH）和 UNIX 的持续发展得以保存。


总纲第 5 条——没有必然性，只有偶然性：DEC 小型机的崛起与 PDP-11 之于 UNIX 均系偶然（与 18.1/18.2 映射一致）；总纲第 4 条——分离聚合是永恒规律：小型机厂商群的兴衰与 BSD 在工作站平台上的扩散为分合循环（与 18.3/18.4 映射一致）。子节级映射详见 18.1-18.4 各节史观字段
## 辨析

PDP-11 与 UNIX 的共生关系常被简化为“天作之合”，但UNIX最初是为PDP-7编写的，PDP-11是后来的升级：PDP-11的MMU恰好支持UNIX的多用户需求，但这种“适配”是工程上的事后选择而非设计上的先见之明。DEC在1990年代被Compaq收购后的消亡与其未能及时转向RISC架构有关，将DEC的衰落简单归因于“小型机被微机取代”的线性叙事遮蔽了PDP谱系内部的技术演进逻辑（如VAX与Alpha的尝试）。PDP-11的硬件细节（如UNIBUS的DMA机制、内存映射I/O）对UNIX内核设计的具体影响程度，需要更精确的源代码考古证据。

## 文献

（待补：Bell C G, Mudge J C, McNamara J E. Computer Engineering: A DEC View of Hardware Systems Design[M]. Digital Press, 1978；Ceruzzi P E. A History of Modern Computing[M]. 2nd ed. MIT Press, 2003；[DB:references_fulltext:chapter_matches:chmatch_3619]；[DB:references_fulltext:chapter_matches:chmatch_1536]）

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP322、BSD Now EP308、BSD Now EP225（共 3 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Warner Losh 通过 Bell Labs 1968 年影片《The Incredible Machine》比对 DEC 目录与现场服务清单，论证片中 PDP-7 即 Ken Thompson 所用序列号 34：具备 340 显示器与 444B 纸带机、无 DECtape。（BSD Now EP322，[407.26-941.24]，L2）
- 影片中机器生成音乐、与视觉声学部门来源吻合，配置、日期、无磁带三条证据链共同支持其“Unix 之母机”身份，但 Warner 仍以弱证据与强证据区分，未作绝对断言。（BSD Now EP322，[936.56-977.82]，L2）
- OpenBSD 6.6 为第 47 个发布，unveil 已用于 77 个用户态程序，移除 bridge 输出快速路径内核锁，加入 Intel MDS 缓解与 malloc 隐蔽/清零 API，并更新 VMM 以透传 MSR 缓解位。（BSD Now EP322，[1059.96-1598.48]，L2）
- OpenSSH 8.1 修复 XMSS 私钥解析整数溢出，并在 RAM 中加密静态私钥以防 Spectre/Meltdown 类侧信道；RSA 证书签名默认改用 SHA2-512，不兼容 7.2 之前的客户端。（BSD Now EP322，[2107.02-2265.46]，L2）
- GhostBSD 澄清其基于 TrueOS/FreeBSD 12 stable，官方桌面为 MATE，其他桌面以社区版本维护，项目提供构建与托管支持并欢迎贡献。（BSD Now EP322，[1778.00-1862.98]，L2）
- 主持人以个人 FreeNAS 磁盘 AHCI 超时报错为例，演示用 smartctl 判断磁盘将坏、gpart backup/restore 复制分区表、zpool replace 建立临时镜像直至离线盘被自动移除的完整流程。（BSD Now EP308，[95.42-320.46]，L1）
- Warner Losh 通过 DEC 服务清单考据 PDP-7 序列号 34 为首台运行 Unix 的机器，并指出 99 台 PDP-7 中仅两台带硬盘，移植到 PDP-11 是 Unix 得以延续的关键。（BSD Now EP308，[1066.06-1305.06]，L2）
- 本期介绍在 OpenBSD 上以 umurmur/mumble 自建低延迟 VoIP，证书绑定昵称防止冒名，并提及 OpenBSD 默认禁用音频输入的安全设定。（BSD Now EP308，[710.98-889.42]，L2）
- TrueOS 17.12 稳定版发布，含 OpenRC 服务定义更新、Lumina 改进，并基于 FreeBSD current 以提前获取图形与 Wi-Fi 驱动。（BSD Now EP225，[73.68-83.2]，L2）
- PDP-11 回顾引述 C Gordon Bell 等人的论文，梳理 DEC 1957 年创立、以“Programmed Data Processor”避讳“计算机”一词，以及 PDP-11 在地址位、寄存器、栈、中断、字符处理上的设计取舍。（BSD Now EP225，[1844.12-1885.92]，L2）
- 该回顾点明 UNIX 1974 年由 Ken Thompson 携磁带抵达伯克利，演化出 BSD 与 Sun Microsystems；C 的 16 位 int 亦源自 PDP-11。（BSD Now EP225，[2883.82-2958.5]，L2）
- FreeBSD 2017 发布工程回顾：Glen Barber 全职工负责发布工程，11.1 于 7 月 21 日发布，10.4 由另一名发布工程师领衔并作为 stable 10 分支的最终版本。（BSD Now EP225，[3334.96-3475.08]，L2）

**史料**：

- Warner Losh 博客《Hunting Down Ken's PDP-7》及 Bell Labs《The Incredible Machine》1968 年影片。（BSD Now EP322，[400.18-979.3]，L2）[订正：原 [400.18-402.92]，2026-09-30 SenseAudio 重转核对]
- DEC PDP-7 销售目录与 Bitsavers 现场服务清单（序列号 34/149 的选件记录）。（BSD Now EP322，[545.0-707.24]，L2）[订正：原 [685.26-707.24]，2026-09-30 SenseAudio 重转核对]
- OpenBSD 6.6 发布页与升级说明（unveil、MDS 缓解、预编译包数量等）。（BSD Now EP322，[1063.56-1528.5]，L2）[订正：原 [1063.56-1068.82]，2026-09-30 SenseAudio 重转核对]
- OpenSSH 8.1 发布公告，含 Adam Zabrocki 报告的 XMSS 私钥解析漏洞。（BSD Now EP322，[2125.36-2172.60]，L2）
- Warner Losh 博客关于 PDP-7 序列号 34 的考据，引 DEC 服务清单与 Bob Supnik 提供的 18 位服务列表。（BSD Now EP308，[1066.06-1305.06]，L2）
- OpenBSD Foundation 2019 年度个人捐款突破 5 万加元、社区成白金捐赠者的公告。（BSD Now EP308，[1900.42-2027.46]，L2）
- C Gordon Bell 等人论文（“What have we learned from the PDP-11?” 等四篇）的转述，含 1957 年 DEC 创立与 PDP-11 设计回顾。（BSD Now EP225，[1940.36-1968.48]，L2）
- 转述的 OpenBSD 工作站指南，含用户动作即时完成、极简工具、硬件隐私等设计目标。（BSD Now EP225，[542.34-652.4]，L2）
- FreeBSD 基金会 2017 发布工程回顾（Glen Barber 的 VBSDCon 演讲与问答）。（BSD Now EP225，[3334.96-3771.04]，L2）

**史观**：

- 总纲1 一切真历史都是古代史：50 年前的机器被当作文物考据，当下的档案即未来的历史。（BSD Now EP322，[985.90-1007.10]，L2）[订正：原 标签重复两遍，2026-10-01 排版修整]
- 总纲17 证明世界先于解释和改造世界：先有 PDP-7 实物与影片证据，再谈 Unix 起源解释。（BSD Now EP322，[461.82-466.08]，L2）[订正：原 标签重复两遍，2026-10-01 排版修整]
- 总纲19 解释学循环是历史认识的根本条件：影片截图与目录照片互为印证，逐项比对构成循环解释。（BSD Now EP322，[558.72-631.14]，L2）[订正：原 标签重复两遍，2026-10-01 排版修整]
- 总纲22 知识注定过时：SSH 旧客户端与 RSA-SHA1 证书兼容性被新默认淘汰，知识随版本更替失效。（BSD Now EP322，[2236.64-2265.46]，L2）[订正：原 标签重复两遍，2026-10-01 排版修整]
- 总纲8 本体论上各方平等：OpenBSD 6.6 与 OPNsense、GhostBSD 同屏，各项目如实呈现。（BSD Now EP322，[1608.32-1905.7]，L2）[订正：原 [1608.32-1616.96]，2026-09-30 SenseAudio 重转核对][订正：原 标签重复两遍，2026-10-01 排版修整]
- 总纲10 动手者创造历史：Warner Losh 逐帧考证、OpenBSD 开发者逐锁解锁，动手者推动认识与系统演进。（BSD Now EP322，[982.99-1165.6]，L2）[订正：原 [982.99-1036.46]，2026-09-30 SenseAudio 重转核对][订正：原 标签重复两遍，2026-10-01 排版修整]
- 总纲5 没有必然性，只有偶然性：Unix 在 99 台 PDP-7 中仅两台带硬盘的偶然条件下诞生，并因 PDP-11 移植而延续。（BSD Now EP308，[1236.88-1271.3]，L2）
- 总纲9 经验优先：主持人以亲身动手替换故障磁盘的经验记录运维史，而非停留在理论推演。（BSD Now EP308，[95.42-320.46]，L1）
- 总纲10 动手者创造历史：Warner Losh 以逐台机器核对服务清单的动手考据方式确证首台 Unix 机器。（BSD Now EP308，[1066.06-1305.06]，L2）
- 总纲9 经验优先：贝尔的回顾强调计算机是“总体设计环境”的产物，成功在于为当下造出正确的机器，呼应经验优先的取向。（BSD Now EP225，[2066.0-2101.76]，L2）
- 总纲4 分离聚合是永恒规律：PDP-11 的开放架构使任何按规范实现者皆可称 PDP-11，DEC 内部形成快慢两条实现路线，体现分离聚合的规律。（BSD Now EP225，[2184.72-2209.84]，L2）
- 总纲10 动手者创造历史：发布工程回顾强调除 Glen Barber 外还有大量不在聚光灯下的人协作，凸显动手者叙事。（BSD Now EP225，[3746.94-3769.1]，L2）

**辨析**：

- PDP-7 影片鉴定为“强烈支持而非确证”，Warner 本人承认对序列号 149 的排除仅属弱证据。　[存疑脚注] 三线证据均非决定性，结论保持开放（BSD Now EP322，[770.24-808.78]，L3）
- GhostBSD 路线为项目方单方声明，TrueOS 后续变动可能使其再调整，不宜作长期定论。　[考据脚注] 上游 TrueOS 路线变动风险未计入（BSD Now EP322，[1802.90-1822.78]，L4）
- [存疑脚注] 转写中上一期引述与若干人名拼写（如 Kurt Mojic 等）存在 ASR 噪音，未与 Undeadly 原文核对。　[存疑脚注] 人名拼写与上一期引述未经原文核对（BSD Now EP308，[704.02-710.98]，L4）
- PDP-11 回顾系博客作者对贝尔论文的二手转述，且转写将“Maria Strobel”等专名误转，人名与具体数字须核对原文。　[存疑脚注] 专名与数字须以贝尔论文原文核实（BSD Now EP225，[1927.8-1965.5]，L4）

**文献**：

- [BSD Now EP322] Pennington J. BSD Now: 322: Happy Birthday, Unix[EB/OL]. (2019-10-31)[2026-08-15]. <https://www.bsdnow.tv/322>.
- [BSD Now EP308] Pennington J. BSD Now: 308: Mumbling with OpenBSD[EB/OL]. (2019-07-25)[2026-08-15]. <https://www.bsdnow.tv/308>.
- [BSD Now EP225] Pennington J. BSD Now: 225: The one true OS[EB/OL]. (2017-12-20)[2026-08-15]. <https://www.bsdnow.tv/225>.

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

