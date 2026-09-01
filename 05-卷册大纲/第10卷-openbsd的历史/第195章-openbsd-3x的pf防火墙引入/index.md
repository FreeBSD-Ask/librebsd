---
chapter: 第 195 章
id: CH195
volume: 第10卷-openbsd的历史
---

# 第 195 章 openbsd-3x的pf防火墙引入

## 要点

- pf 2001 年原始公告与 CVS commit log 是研究 pf 诞生的核心史料；公告由 de Raadt 与 Hartmeier 发布至 OpenBSD 邮件列表；commit log 反映 Hartmeier 等的早期开发节奏；统计结论印证——openbsd.db openbsd-src 仓库总 commit 数 245,904（统计结论 C-05），3.x 时期（2001-2004）
- OpenBSD 3.1-3.6 安全特性（W^X、SSP、privilege separation、swap encryption）的 commit 记录是研究此时期安全演进的核心史料；Provos、Etoh、de Raadt 等的 commit 反映开发节奏；考据需对照 CVS commit log 与 Release Notes；统计结论印证——openbsd.db openbsd-src 仓
- OpenBSD 提出“在默认安装中 6 年仅两个远程漏洞”口号，最初由 de Raadt 在 OpenBSD 网站上宣称；口号中的“远程漏洞”指默认安装下可被远程攻击者利用的漏洞；口号随时间演变，至 2000 年代中期改为“多年无远程漏洞”
- 批评者（如 CVE 数据库研究者、Linux 社区成员）指出 OpenBSD 口号依赖于严格定义——“默认安装”排除了 ports 与第三方软件，“远程漏洞”排除了本地漏洞与权限提升漏洞；批评者认为 OpenBSD 实际安全记录虽有改进，但口号夸大宣传
- OpenBSD 社区回应批评时强调“默认安装”的定义明确且一致——指基本系统安装后未启动第三方服务的状态；de Raadt 在邮件列表与演讲中多次反驳批评者；OpenBSD 社区认为批评者忽略了 OpenBSD 在安全文化上的贡献

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4023] 卷“第10卷-openbsd的历史”第 195 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- pf 1.0 的具体发布日期存在 2001.12.1 与 2001.12.3 两种说法——需对照 OpenBSD 官方公告核验；openbsd.db 查询 L1.1.1 局限：openbsd-src 为 GitHub 镜像，commit 量可能滞后于 OpenBSD CVS 主仓；L1.1.1 报告仅显示 23 仓库 572 行中的前 30 行（dragonfly 仓库），openbsd-src
- 安全特性 commit 的具体作者归属需考据——部分大型 commit 由多人协作，难以单一归属；commit log 中的安全相关 tag 需考据；**统计局限性标注**——C-10 Mann-Kendall 趋势检验基于 1993-2026 年全期月度 commit 量序列，slope = −0.24/月 是全期趋势，3.x 时期（2001-2004）的局部趋势须结合时间窗口切片分析，全期下降
- “两个远程漏洞”的具体指代在不同叙事中存在差异——部分资料称是 OpenBSD 2.6 之前的两个漏洞，部分称是历史漏洞，需对照 OpenBSD 官网核验
- 批评者的代表性需考据——单一批评者不等于社区共识；“严格定义”的具体范围（如是否包括本地漏洞）需对照 OpenBSD 官网核验
- OpenBSD 社区的回应是否具有说服力在不同观察者中存在分歧——需对照多源核验

## 文献

- OpenBSD 3.0 公告；OpenBSD CVS 仓库；Hartmeier pf 历史文章；openbsd.db 查询 L1.1.1 与 L1.1.2（来源：原材料/研究/bsd 仓库分析/数据分析/宏观趋势统计.md §L1.1.1、§L1.1.2）；统计分析报告：描述性统计.md SubTask 2.1 [R/OL]. 2026-07-27. 文件路径：`c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\统计分析\描述性统计.md`；SQL 查询：`SELECT COUNT(*) FROM commits WHERE repo_name='openbsd-src'`. openbsd.db [DB/OL]. 查询日期：2026-07-27[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:openbsd.duckdb -->> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 2001-2001 年间：18,985 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
- OpenBSD CVS 仓库；OpenBSD 邮件列表；统计分析报告：推断性统计.md Task 5 + Task 10 [R/OL]. 2026-07-27. 文件路径：`c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\统计分析\推断性统计.md`；描述性统计.md SubTask 2.3 [R/OL]. 2026-07-27. 文件路径：`c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\统计分析\描述性统计.md`；Python 统计脚本：`script/phase2_inferential.py`. Task 5 Mann-Kendall 趋势检验 + Task 10 Gini 系数 Bootstrap. 执行日期：2026-07-27 ［A］#### 194.3“默认安装仅两个远程漏洞”口号的演变——OpenBSD 提出“在默认安装中 6 年仅两个远程漏洞”的口号，该口号长期受批评，批评者认为计数依赖于严格定义
- OpenBSD 官网 Security 页面；Wayback Machine 快照；de Raadt 演讲[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- CVE 数据库；Bugtraq/Full Disclosure 邮件列表；OpenBSD Security 页面 ［A］
- OpenBSD 邮件列表；de Raadt 演讲；OpenBSD FAQ ［A］
- OpenBSD 邮件列表存档；OpenBSD 官网；Wayback Machine ［A］<!-- DB_REF:openbsd.duckdb -->> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 2002-2004 年间：48,812 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
- OpenBSD 邮件列表；OpenBSD 官网；Wayback Machine ［A］<!-- DB_REF:openbsd.duckdb -->> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1996-2004 年间：112,478 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
- 原材料/哲学/项目统摄史观/第 25 章.md（总纲第 6 条与第 8 条原文）；OpenBSD CVS 仓库；FreeBSD CVS/Git 仓库（PF 相关）；OpenBSD 邮件列表存档 ［A］<!-- DB_REF:openbsd.duckdb -->> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1996-2004 年间：112,478 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
- 原材料/哲学/项目统摄史观/第 25 章.md（总纲第 8 条与第 13 条原文）；OpenBSD 邮件列表存档 [EB/OL]. **<https://marc.info/?laccopenbsd-misc**>；FreeBSD CVS/Git 仓库（`sys/netpfil/pf/`）；OpenBSD security.html [EB/OL].** <https://www.openbsd.org/security/**>；FreeBSD TrustedBSD 项目文档；NSA SELinux 项目文档 ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1995-2026 年间：1,289,123 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP186、BSDTalk EP200（共 2 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- AsiaBSDCon 2017 在东京举行，议题覆盖 FreeBSD 上的 Xen Dom0、bhyve 向 ARM 移植、OpenBSD VMM/VMD 更新与 pledge 对 capsicum 的沙箱比较。（BSD Now EP186，[432.94-560.68]，L2）
- Philipp（OpenBSD 前提交者）回顾 2002 年 Karlsruhe hackathon 参与 PF 测试与文档工作，实现接口分组并拆分 pf.c 中的 IOCTL 代码。（BSD Now EP186，[3969.0-4226.0]，L1）
- Philipp 描述 OpenBSD 路由域（rdomain）为单机上的多个虚拟路由器，可用于多租户防火墙与相同 IP 复用的隔离测试。（BSD Now EP186，[4381.84-4761.18]，L1）
- 2004 年 PF hackathon 曾发现用户态 32 位与内核 8 位规则编号溢出导致的隐蔽错误，需超过约 256 条规则才触发。（BSD Now EP186，[4227.0-4285.88]，L1）
- 维护者 Kjell Wooding 阐明 mg 的定位：这是一个极小的 Emacs 风格编辑器，与 Emacs 本质不同——后者是恰好附带编辑器的 Lisp 解释器，而 mg 首先是编辑文件的工具，不内嵌编程语言、不提供游戏或浏览器式扩展，只为满足 Emacs 用户的键位肌肉记忆；他并非原作者，而是在维护过程中偶然接手，mg 于 2000 年进入 OpenBSD 基本系统。（BSDTalk EP200，[60.04-157.16]，L1）
- mg 的历史与可移植性：Wooding 回忆该编辑器 1986 年即已问世、早于 OpenBSD 存在；多年来被社区自发移植至 Debian、Mac OS X 等环境，维护者至今仍收到 Debian 用户的 bug 报告；项目并无独立便携版仓库，获取最新源码的正规途径始终是 OpenBSD 源树。（BSDTalk EP200，[359.88-401.88]，L1）
- 许可证工程：mg 初入项目时约九成代码即属 public domain，团队随后逐个联系在树作者，将全部补丁释放进 public domain，如今仅 theo mode 一个文件仍持 BSD 许可——该模式仿照 Emacs 中 ELIZA 式对话实验，输出 Theo de Raadt 多年来的言论语录，属社区自嘲文化产物；Wooding 同时指出 public domain 在瑞典等法域仍有法律适用问题。（BSDTalk EP200，[691.08-751.56]，L1）
- Wooding 的参与路径与角色变迁：他曾经营安全公司 Code Talker Communications，与一巷之隔的 Secure Networks 公司一次喝啤酒闲谈中得知 OpenBSD 开发者住在自己的家乡 Calgary，遂联系并加入项目；最初职责是维护旧 IPF 防火墙代码并整合 Darren Reed 的改动，亲历该代码被整体移出源树、代之以 PF 的大分裂；此后其贡献呈游牧状，在 hackathon 间隙深入源码各处修 bug，如 pfsync 与冗余代码问题。（BSDTalk EP200，[412.48-526.32]，L1）
- 维护哲学与状态：Wooding 的长期目标是让代码行数越来越少，通过迭代清理与简化逼近；mg 仍存在积年未修的设计缺陷，修复通常依赖某份 bug 报告将维护者唤醒；他曾在 hackathon 中专门重写文档，如今手册页可能比源码本身更长，呼应 OpenBSD 对完整 man page 的自豪传统；另曾于愚人节发布可用的 vi 模式补丁。（BSDTalk EP200，[654.32-801.48]，L1）

**史料**：

- AsiaBSDCon 2017 演讲幻灯片与日程（BSD Now EP186，[432.94-560.68]，L1）
- Philipp 访谈自述（BSD Now EP186，[3969.0-5733.62]，L1）
- OpenBSD PF 邮件列表与 CVS 历史（BSD Now EP186，[3969.0-4285.88]，L1）
- 一手史料以 Wooding 口述为主：mg 的 1986 年起源记忆、public domain 授权重构过程、theo mode 的由来、IPF 至 PF 更替的亲历叙述、OpenBSD Foundation 创始董事身份自述；开场栏目由主持人转述 netstat 命令最早出现于 4.2BSD。（BSDTalk EP200，[373.88-526.32]，L1）

**史观**：

- 总纲10 动手者创造历史：PF 由测试者、文档者与提交者共同打磨，历史由大量动手协作的人推动。（BSD Now EP186，[4016.52-4285.88]，L1）
- 总纲4 分离聚合是永恒规律：路由域把一台物理路由器分离为多个逻辑路由器，体现分离聚合的循环。（BSD Now EP186，[4381.84-4761.18]，L1）
- 总纲6 和解优于斗争：OpenBSD 社区“批评即受邀修复”的协作方式，强调和解与共建而非对抗。（BSD Now EP186，[4016.52-4050.66]，L1）
- 总纲13 法律与道德是利益分配：mg 的授权重构过程——逐个接洽在树作者、把分散的版权利益统一收束为 public domain——显示许可证选择在开源工程中本质上是围绕项目利益的法律形式安排，而非抽象的道德立场。（BSDTalk EP200，[116.68-137.44]，L1）
- 总纲10 动手者创造历史：Wooding 自述数年间漫游源码树、依 bug 报告唤醒注意、以 hackathon 间隙零星修复的维护方式，表明 OpenBSD 的日常演化由大量此类默默动手的个体贡献累积而成。（BSDTalk EP200，[493.80-521.64]，L1）

**辨析**：

- [存疑脚注] 访谈中 2002 年 hackathon 地点、PF 实现细节系当事人十余年后回忆，需与 OpenBSD 邮件列表与 CVS 记录核验。　[存疑脚注] 当事人回忆性细节，缺乏独立档案印证。（BSD Now EP186，[3969.0-4285.88]，L4）
- mg 1986 年首发的说法为当事人回忆，其源自 MicroEMACS 谱系的精确传承（含原始作者与年份）须以源码历史与既存考据交叉验证；转写人名存在音误——受访者记作 Shell Wooding 应为 Kjell Wooding，Theo de Raadt 被记作 Theodore Atth——引用前须回查原音频。　[存疑脚注] 起源年份系当事人口述回忆，且转写人名音误，采信前须复核（BSDTalk EP200，[365.84-377.28]，L4）

**文献**：

- [BSD Now EP186] Pennington J. BSD Now: 186: The Fast And the Firewall: Tokyo Drift[EB/OL]. (2017-03-22)[2026-08-15]. https://www.bsdnow.tv/186.
- [BSDTalk EP200] Backman W. BSDTalk: 200: bsdtalk200 - The mg text editor with Kjell Wooding[EB/OL]. (2010-10-13)[2026-08-27]. https://bsdtalk.blogspot.com/2010/10/bsdtalk200-mg-text-editor-with-kjell.html.

<!-- /PODCAST_REVIEW -->
