---
chapter: 第 348 章
id: CH348
volume: 第18卷-全球社区地区bsd史
---

# 第 348 章 openbsd核心贡献者人物传记

## 要点

OpenBSD 项目自 1995 年从 NetBSD 分叉以来，其核心贡献者群体形成了以 Theo de Raadt 为中心的独特技术社区。本章收录 OpenBSD 核心贡献者的人物传记，涵盖开发者（committer）、文档贡献者、发行工程与测试人员等角色。OpenBSD 的贡献者群体以安全至上哲学为共同纽带，在项目 30 年历史中维持了高度稳定的核心团队——其核心贡献者呈现长期留存的定性特征（跨项目更替率的精确比较须明示统计口径），这一稳定性反映出其 BDFL 治理模式下的社区凝聚力与潜在的单点故障风险。

## 史料

- OpenBSD 官方开发者列表（openbsd.org）—— 一手网络史料 ［A］
- OpenBSD 源代码仓库提交记录（openbsd.duckdb）—— 一手代码史料 ［A］
- OpenBSD 邮件列表 archives（marc.info）—— 一手网络史料 ［A］
- [DB:bsdnow_podcast:outline_mappings] BSD Now 播客多期涉及 OpenBSD 开发者访谈 —— 二手口述史料 ［B］
- [DB:references_fulltext:chapter_matches:chmatch_3633] 参考文献数据库匹配 —— 二手文献 ［B］
- OpenBSD 项目历史文档与 release announcements —— 一手网络史料 ［A］

## 史观

总纲第 15 条——文化即形式主义：安全至上哲学作为项目文化的具体形态，塑造贡献者群体的技术选择与社区文化；总纲第 7 条——动手者创造历史，OpenBSD 贡献者的技术实践（如代码审计、pledge/unveil 机制开发）是安全文化形成的物质基础；总纲第 5 条——经验优先，以提交记录与邮件列表为优先依据重建贡献者谱系；总纲第 3 条——不存在进步只有权力再分配：BDFL 治理模式下开源社区权力集中与分散的辩证关系。

## 辨析

OpenBSD 的贡献者谱系研究面临若干方法论挑战：其一，OpenBSD 项目以代码审查严格著称，大量外部贡献者的 patch 经核心开发者修改后合入，原始作者身份在提交记录中可能被稀释——这要求区分“代码作者”与“提交者”两个层面；其二，Theo de Raadt 的 BDFL 角色使贡献者传记的叙事天然倾向于中心化，容易忽视边缘贡献者（如端口维护者、文档翻译者）的贡献；其三，OpenBSD 社区对“贡献者”的定义与其他 BSD 项目不同——OpenBSD 更强调代码质量而非贡献数量，这使得跨项目贡献者比较存在口径差异。本章在编纂时以提交记录为客观基准，辅以邮件列表讨论与公开访谈交叉验证，但须承认量化指标（如提交次数）不能完全反映贡献者的实际影响力。

## 文献

- OpenBSD 开发者列表（openbsd.org）
- OpenBSD 源代码仓库（cvsweb.openbsd.org）
- OpenBSD 邮件列表 archives
- BSD Now 播客相关期数（见史料字段 outline_mappings 映射）
- 参考文献数据库匹配记录（chmatch_3633）

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP435、BSD Now EP422、BSD Now EP623、BSDTalk EP200（共 4 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Suleen Rapin 从早期 Linux 与 PC-BSD 起步，工作中以 FreeBSD 替换 Linux 服务器，后转向 OpenBSD，因提交 ports 更新补丁而被邀请加入团队。（BSD Now EP435，[138.4-317.56]，L1）
- 她发起 OpenBSD Webzine，意图以面向非技术读者的月刊形式传播 OpenBSD 新闻、技巧与开发者访谈。（BSD Now EP435，[1434.94-1549.12]，L1）
- 其“旧电脑挑战”以 PowerPC 苹果笔记本运行 OpenBSD，并借助 Charlene Wendling 对 PowerPC 软件包的长期维护，展示 OpenBSD 对旧硬件的兼容。（BSD Now EP435，[530.8-929.72]，L1）
- Brian Callahan 自 2013 年成为 OpenBSD 开发者，在 Rensselaer Polytechnic Institute 任教，并已向 OpenBSD 移植约四五十个编译器与解释器。（BSD Now EP422，[72.2-123.8]，L1）[订正：原 [82.26-112.86]，2026-09-30 SenseAudio 重转核对]
- 他在信息安全课程中让学生登录其托管的 OpenBSD 机器，讲授 strlcpy、pledge 与 unveil 等机制，并以现代二进制利用课程反向印证这些安全设计的价值。（BSD Now EP422，[1140.2-1525.8]，L1）[订正：原 [1152.74-1504.02]，2026-09-30 SenseAudio 重转核对]
- NYC*BUG 是纽约 BSD 用户组，约于 2003 至 2004 年成立，自称最古老的 BSD 用户组之一，疫情后成功转为线上活动。（BSD Now EP422，[2076.1-2336.1]，L1）[订正：原 [2083.8-2321.72]，2026-09-30 SenseAudio 重转核对]
- FreeBSD Foundation 于 2025 年 4 月启动 SBOM 项目，目标是为整个源码树与软件包生成软件物料清单，服务于零信任构建与供应链合规需求。（BSD Now EP623，[309.72-553.78]，L2）
- Klara Systems 的夏季综述以自建 DNS、NTP、ZFS 存储与定制内核为主线，主张以开源标准摆脱厂商锁闭并降低长期成本。（BSD Now EP623，[557.22-1040.66]，L2）
- David Gwynne 自述通过 OpenBSD 的简短文档解决家庭拨号共享上网问题而入坑，后因 USB 2.0 备份需求开始向 OpenBSD 移植 NetBSD 的 USB 代码。（BSD Now EP623，[1122.34-1528.48]，L1）
- David Gwynne 主导的 sec(4) 把 IPsec 从流量窃取点改为可管理接口，使防火墙、队列、BPF 与 BGP 等常规工具可直接作用于隧道流量，服务于与 AWS 站点间 VPN 的对接。（BSD Now EP623，[2044.96-2309.56]，L1）
- David Gwynne 还实现 ERSpan 接口与 BPF 日志守护进程，以 GRE 封装远程端口镜像并支持 VMware 分布式虚拟交换机的监控会话。（BSD Now EP623，[2316.56-2663.62]，L1）
- OpenBSD hackathon 的社会维度被视为关键：面对面沟通能消除邮件与聊天中的误解，组织跨城市活动则面临资源协调的不确定性。（BSD Now EP623，[1544.20-1796.32]，L1）
- 维护者 Kjell Wooding 阐明 mg 的定位：这是一个极小的 Emacs 风格编辑器，与 Emacs 本质不同——后者是恰好附带编辑器的 Lisp 解释器，而 mg 首先是编辑文件的工具，不内嵌编程语言、不提供游戏或浏览器式扩展，只为满足 Emacs 用户的键位肌肉记忆；他并非原作者，而是在维护过程中偶然接手，mg 于 2000 年进入 OpenBSD 基本系统。（BSDTalk EP200，[60.04-157.16]，L1）
- mg 的历史与可移植性：Wooding 回忆该编辑器 1986 年即已问世、早于 OpenBSD 存在；多年来被社区自发移植至 Debian、Mac OS X 等环境，维护者至今仍收到 Debian 用户的 bug 报告；项目并无独立便携版仓库，获取最新源码的正规途径始终是 OpenBSD 源树。（BSDTalk EP200，[359.88-401.88]，L1）
- 许可证工程：mg 初入项目时约九成代码即属 public domain，团队随后逐个联系在树作者，将全部补丁释放进 public domain，如今仅 theo mode 一个文件仍持 BSD 许可——该模式仿照 Emacs 中 ELIZA 式对话实验，输出 Theo de Raadt 多年来的言论语录，属社区自嘲文化产物；Wooding 同时指出 public domain 在瑞典等法域仍有法律适用问题。（BSDTalk EP200，[691.08-751.56]，L1）
- Wooding 的参与路径与角色变迁：他曾经营安全公司 Code Talker Communications，与一巷之隔的 Secure Networks 公司一次喝啤酒闲谈中得知 OpenBSD 开发者住在自己的家乡 Calgary，遂联系并加入项目；最初职责是维护旧 IPF 防火墙代码并整合 Darren Reed 的改动，亲历该代码被整体移出源树、代之以 PF 的大分裂；此后其贡献呈游牧状，在 hackathon 间隙深入源码各处修 bug，如 pfsync 与冗余代码问题。（BSDTalk EP200，[412.48-526.32]，L1）
- 维护哲学与状态：Wooding 的长期目标是让代码行数越来越少，通过迭代清理与简化逼近；mg 仍存在积年未修的设计缺陷，修复通常依赖某份 bug 报告将维护者唤醒；他曾在 hackathon 中专门重写文档，如今手册页可能比源码本身更长，呼应 OpenBSD 对完整 man page 的自豪传统；另曾于愚人节发布可用的 vi 模式补丁。（BSDTalk EP200，[654.32-801.48]，L1）

**史料**：

- Suleen Rapin 本人博客、OpenBSD Webzine（website.puffy.kfh）、dataswamp.org shell 社区及其旧电脑挑战记录。（BSD Now EP435，[112.04-127.56]，L1）
- Brian Callahan 本人访谈、D 语言社区、Tiny C compiler 与 Modula 2 移植记录、NYC*BUG 用户组活动。（BSD Now EP422，[379.4-752.7]，L1）[订正：原 [384.1-735.94]，2026-09-30 SenseAudio 重转核对]
- FreeBSD Foundation SBOM 项目公告。（BSD Now EP623，[309.72-553.78]，L2）
- Klara Systems 的 FreeBSD Summer 2025 Roundup。（BSD Now EP623，[557.22-1040.66]，L2）
- David Gwynne 访谈（University of Queensland，2025 年 5 月 29 日）。（BSD Now EP623，[1064.42-3319.38]，L1）
- 一手史料以 Wooding 口述为主：mg 的 1986 年起源记忆、public domain 授权重构过程、theo mode 的由来、IPF 至 PF 更替的亲历叙述、OpenBSD Foundation 创始董事身份自述；开场栏目由主持人转述 netstat 命令最早出现于 4.2BSD。（BSDTalk EP200，[373.88-526.32]，L1）

**史观**：

- 总纲10 动手者创造历史：Suleen 通过维护 ports、撰写教程与创办 Webzine 参与 OpenBSD，体现社区边缘动手者对项目生态的持续塑造。（BSD Now EP435，[353.76-384.0]，L1）
- 总纲10 动手者创造历史：Callahan 以持续移植编译器、教学与组织用户组的具体劳动扩展 OpenBSD 生态，体现动手者的长期积累。（BSD Now EP422，[379.4-752.7]，L1）[订正：原 [384.1-735.94]，2026-09-30 SenseAudio 重转核对]
- 总纲10 动手者创造历史：David Gwynne 以大学系统管理员身份亲手修复基础设施问题并回馈 OpenBSD，体现一线操作者推动协议与工具演进。（BSD Now EP623，[1806.76-1946.58]，L1）
- 总纲6 和解优于斗争：OpenBSD hackathon 以面对面沟通消解邮件分歧，强调协作而非对抗的社区机制。（BSD Now EP623，[1580.48-1651.24]，L1）
- 总纲4 分离聚合是永恒规律：sec(4) 将 IPsec 从网络栈中窃取流量的分离点改造为可聚合进接口体系的组件。（BSD Now EP623，[2049.28-2316.56]，L1）
- 总纲13 法律与道德是利益分配：mg 的授权重构过程——逐个接洽在树作者、把分散的版权利益统一收束为 public domain——显示许可证选择在开源工程中本质上是围绕项目利益的法律形式安排，而非抽象的道德立场。（BSDTalk EP200，[116.68-137.44]，L1）
- 总纲10 动手者创造历史：Wooding 自述数年间漫游源码树、依 bug 报告唤醒注意、以 hackathon 间隙零星修复的维护方式，表明 OpenBSD 的日常演化由大量此类默默动手的个体贡献累积而成。（BSDTalk EP200，[493.80-521.64]，L1）

**辨析**：

- OpenBSD Webzine 创办始末及加入团队细节仅来自当事人自述，需与网站存档、邮件列表记录交叉验证。　[存疑脚注] 加入团队与 Webzine 创办细节为单一当事人自述，尚需邮件列表与站点存档旁证。（BSD Now EP435，[1483.2-1522.08]，L4）
- NYC*BUG 的成立年份与“最古老用户组之一”的说法为当事人估计，需与用户组档案及其他 BSD 用户组成立记录交叉核对。　[存疑脚注] 用户组成立年份为当事人记忆性表述，宜与其他地区 BSD 用户组史料比对。（BSD Now EP422，[2090.4-2120.4]，L4）[订正：原 [2090.58-2102.08]，2026-09-30 SenseAudio 重转核对]
- 转录将 David Gwynne 记作 David Gwynn 或 David Gwendt，标题 Two‘s interview 疑为 Gwynne’s interview 的转写偏差，人名以 OpenBSD 官方为准。　[存疑脚注] 人名与标题存在语音转写偏差，须以 OpenBSD 官方资料核验（BSD Now EP623，[1068.26-1075.34]，L4）
- sec(4) 相关表述中 IPsec 接口在转录混用 sec 与 sec4，具体版本与接口名须以 OpenBSD 手册页核验。　[考据脚注] 接口名称存在转写混用，须以 sec(4) 手册页为准（BSD Now EP623，[1971.80-2235.62]，L4）
- mg 1986 年首发的说法为当事人回忆，其源自 MicroEMACS 谱系的精确传承（含原始作者与年份）须以源码历史与既存考据交叉验证；转写人名存在音误——受访者记作 Shell Wooding 应为 Kjell Wooding，Theo de Raadt 被记作 Theodore Atth——引用前须回查原音频。　[存疑脚注] 起源年份系当事人口述回忆，且转写人名音误，采信前须复核（BSDTalk EP200，[365.84-377.28]，L4）

**文献**：

- [BSD Now EP435] Pennington J. BSD Now: 435: Year End Interview[EB/OL]. (2021-12-30)[2026-08-15]. <https://www.bsdnow.tv/435>.
- [BSD Now EP422] Pennington J. BSD Now: 422: The Brian Callahan Interview[EB/OL]. (2021-09-30)[2026-08-15]. <https://www.bsdnow.tv/422>.
- [BSD Now EP623] Pennington J. BSD Now: 623: Two's interview[EB/OL]. (2025-08-07)[2026-08-15]. <https://www.bsdnow.tv/623>.
- [BSDTalk EP200] Backman W. BSDTalk: 200: bsdtalk200 - The mg text editor with Kjell Wooding[EB/OL]. (2010-10-13)[2026-08-27]. <https://bsdtalk.blogspot.com/2010/10/bsdtalk200-mg-text-editor-with-kjell.html>.

<!-- /PODCAST_REVIEW -->

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-18-067 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-18-067`；login 逐条遍历判定采纳）

2000年前后，家用用户已可用NetBSD在旧PC上构建低成本、免维护的NAT防火墙；作者主张该配置安全性优于部分商业防火墙，并因BSD/Linux在旧硬件上表现良好而被选为家用网关平台。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

