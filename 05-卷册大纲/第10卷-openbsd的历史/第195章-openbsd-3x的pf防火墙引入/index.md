---
chapter: 第 195 章
id: CH195
volume: 第10卷-openbsd的历史
---

# 第 195 章 openbsd-3x的pf防火墙引入

## 要点

- pf 2001 年原始公告与 CVS commit log 是研究 pf 诞生的核心史料；公告由 de Raadt 与 Hartmeier 发布至 OpenBSD 邮件列表；commit log 反映 Hartmeier 等的早期开发节奏；统计结论印证——openbsd.duckdb openbsd-src 仓库总 commit 数 246,535〔订正注：原 245,904 系 C-05 统计结论旧值，openbsd-src 现测 246,535，按 C-05 回填任务订正〕，3.x 时期（2001-2004）
- OpenBSD 3.1-3.6 安全特性（W^X、SSP、privilege separation、swap encryption）的 commit 记录是研究此时期安全演进的核心史料；Provos、Etoh、de Raadt 等的 commit 反映开发节奏；考据需对照 CVS commit log 与 Release Notes；统计结论印证——openbsd.duckdb openbsd-src 仓
- OpenBSD 提出“在默认安装中 6 年仅两个远程漏洞”口号，最初由 de Raadt 在 OpenBSD 网站上宣称；口号中的“远程漏洞”指默认安装下可被远程攻击者利用的漏洞；口号随时间演变，至 2000 年代中期改为“多年无远程漏洞”
- 批评者（如 CVE 数据库研究者、Linux 社区成员）指出 OpenBSD 口号依赖于严格定义——“默认安装”排除了 ports 与第三方软件，“远程漏洞”排除了本地漏洞与权限提升漏洞；批评者认为 OpenBSD 实际安全记录虽有改进，但口号夸大宣传
- OpenBSD 社区回应批评时强调“默认安装”的定义明确且一致——指基本系统安装后未启动第三方服务的状态；de Raadt 在邮件列表与演讲中多次反驳批评者；OpenBSD 社区认为批评者忽略了 OpenBSD 在安全文化上的贡献

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4023] 卷“第10卷-openbsd的历史”第 195 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

本章史观映射汇总：各子节共挂 9 条——总纲 10“动手者创造历史”×4、总纲 4“分离聚合是永恒规律”、总纲 6“和解优于斗争”、总纲 13“法律与道德是利益分配”、总纲 9“经验优先”、总纲 22“知识注定过时”，条目名均与权威表相符，详见子节文件史观/辨析字段〔订正注：原为“(待人工回填)”占位，按子节实测映射回填摘要〕

## 辨析

- pf 1.0 的具体发布日期存在 2001.12.1 与 2001.12.3 两种说法——需对照 OpenBSD 官方公告核验；openbsd.duckdb 查询 L1.1.1 局限：openbsd-src 为 GitHub 镜像，commit 量可能滞后于 OpenBSD CVS 主仓；L1.1.1 报告仅显示 23 仓库 572 行中的前 30 行（dragonfly 仓库），openbsd-src
- 安全特性 commit 的具体作者归属需考据——部分大型 commit 由多人协作，难以单一归属；commit log 中的安全相关 tag 需考据；**统计局限性标注**——C-10 Mann-Kendall 趋势检验基于 1993-2026 年全期月度 commit 量序列，slope = −0.24/月 是全期趋势，3.x 时期（2001-2004）的局部趋势须结合时间窗口切片分析，全期下降
- “两个远程漏洞”的具体指代在不同叙事中存在差异——部分资料称是 OpenBSD 2.6 之前的两个漏洞，部分称是历史漏洞，需对照 OpenBSD 官网核验
- 批评者的代表性需考据——单一批评者不等于社区共识；“严格定义”的具体范围（如是否包括本地漏洞）需对照 OpenBSD 官网核验
- OpenBSD 社区的回应是否具有说服力在不同观察者中存在分歧——需对照多源核验

## 文献

- OpenBSD 3.0 公告；OpenBSD CVS 仓库；Hartmeier pf 历史文章；openbsd.duckdb 查询 L1.1.1 与 L1.1.2（来源：原材料/研究/bsd 仓库分析/数据分析/宏观趋势统计.md §L1.1.1、§L1.1.2）；统计分析报告：描述性统计.md SubTask 2.1 [R/OL]. 2026-07-27. 文件路径：**03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/描述性统计.md**；SQL 查询：`SELECT COUNT(*) FROM commits WHERE repo_name='openbsd-src'`. openbsd.duckdb [DB/OL]. 查询日期：2026-07-27［考据注：2026-07-28 联网考据留痕，模板句式已按 0 信任原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 2001-2001 年间：18,985 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
- OpenBSD CVS 仓库；OpenBSD 邮件列表；统计分析报告：推断性统计.md Task 5 + Task 10 [R/OL]. 2026-07-27. 文件路径：**03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/推断性统计.md**；描述性统计.md SubTask 2.3 [R/OL]. 2026-07-27. 文件路径：**03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/描述性统计.md**；Python 统计脚本：`script/phase2_inferential.py`. Task 5 Mann-Kendall 趋势检验 + Task 10 Gini 系数 Bootstrap. 执行日期：2026-07-27 ［A］
**195.4（口号主题子目）**“默认安装仅两个远程漏洞”口号的演变——〔订正注：原文以 H4 标题混入文献列表且章号误作 194.3（off-by-one），改挂第 195 章并移出文献列表体例〕OpenBSD 提出“在默认安装中 6 年仅两个远程漏洞”的口号，该口号长期受批评，批评者认为计数依赖于严格定义
- OpenBSD 官网 Security 页面；Wayback Machine 快照；de Raadt 演讲［考据注：2026-07-28 联网考据留痕，模板句式已按 0 信任原则精简（WO-004）；语义以正文与所引来源为准］
- CVE 数据库；Bugtraq/Full Disclosure 邮件列表；OpenBSD Security 页面 ［A］
- OpenBSD 邮件列表；de Raadt 演讲；OpenBSD FAQ ［A］
- OpenBSD 邮件列表存档；OpenBSD 官网；Wayback Machine ［A］

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 2002-2004 年间：48,812 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
- OpenBSD 邮件列表；OpenBSD 官网；Wayback Machine ［A］

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1996-2004 年间：112,478 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
- 02-sacred源材料/sacred_sources.duckdb 第 25 章（总纲第 6 条与第 8 条原文）〔订正注：原引 原材料/哲学/项目统摄史观/第 25 章.md 系库外断链路径，改挂库内规范出处〕；OpenBSD CVS 仓库；FreeBSD CVS/Git 仓库（PF 相关）；OpenBSD 邮件列表存档 ［A］

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1996-2004 年间：112,478 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
- 02-sacred源材料/sacred_sources.duckdb 第 25 章（总纲第 8 条与第 13 条原文）〔订正注：原引 原材料/哲学/项目统摄史观/第 25 章.md 系库外断链路径，改挂库内规范出处〕；OpenBSD 邮件列表存档 [EB/OL]. **<https://marc.info/?laccopenbsd-misc**>；FreeBSD CVS/Git 仓库（`sys/netpfil/pf/`）；OpenBSD security.html [EB/OL].** <https://www.openbsd.org/security/**>；FreeBSD TrustedBSD 项目文档；NSA SELinux 项目文档 ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1995-2026 年间：1,289,123 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP186、BSDTalk EP200、BSDTalk EP220、BSDTalk EP229（共 4 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

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
- 受访者 Eric Oyen 居于亚利桑那州凤凰城，约 2007 年经朋友寄赠 OpenBSD 4.2 官方购买版而开始使用 OpenBSD；此前他已是 Linux 防火墙配置的准专家，比较后认为 OpenBSD 的防火墙能力更强，遂尽量坚持使用 OpenBSD。约 2010 年他完全失明，访谈时（2012 年 11 月）在一台 900 MHz AMD Athlon 旧机上运行 OpenBSD 5.0 作家用防火墙。（BSDTalk EP220，[95.00-133.34]，L1）
- 他向本地 Linux 社区推介 OpenBSD 时给出的核心理由是防火墙脚本编写体验：iptables 编写繁琐复杂，而 PF 有专门的规则布局、条目顺序明确，理解与维护成本低；OpenBSD 亦可配置为对多数 IP 流量不可见的桥接式防火墙，在更低协议层过滤，与常规路由防火墙互为补充。（BSDTalk EP220，[554.32-589.74]，L1）
- 他认为 OpenBSD 坚持命令行配置与极简配置文件对屏幕阅读器用户格外友好，并特别称赞 afterboot 等手册页逐步引导的写法；其日常工作流是在 Mac 上用 VoiceOver 经 SSH 操作 OpenBSD，并开两个 SSH 会话交叉阅读文档与编辑配置，以绕开终端重读行等屏幕阅读器通病。（BSDTalk EP220，[509.34-543.22]，L1）
- 无障碍工具链方面：终端环境的 SpeakUp 以截取送往屏幕的文本的方式朗读，仅需标准 105 键键盘；图形桌面则依赖 GNOME 或启用无障碍特性的 GTK 桌面（如 XFCE）配 Orca，但在未知硬件上启动 X 并配置屏幕阅读器仍不可靠。完全失明后他安装 OpenBSD 需视觉辅助或自定义脚本，期待安装镜像能像 live DVD 一样检测驱动并在启动时提供语音接口。（BSDTalk EP220，[178.50-368.06]，L1）
- 关于无障碍的远程系统管理：他描述了两类途径——串口控制台（启动阶段仅需他人敲入重定向命令，之后可从终端经 screen 会话接入串口设备）与“屏幕抓取”专用卡（对系统表现为文本图形显示，实际将文本经串口或网络输出，不依赖操作系统驱动），后者还包括服务器级主板的板载管理子板，可经 SSH 进入固件设置，从而在开机全程不看屏幕。（BSDTalk EP220，[741.94-902.68]，L1）
- Cappuccio 幼年从叔叔处得到一台可运行 CP/M 或 Microsoft Xenix 的 TRS-80 Model 16B，九十年代初转入 386BSD 与 Linux，1995 年因 Theo 在 FTP 站点放出首个 SPARC 内核而开始使用 OpenBSD 并沿用至访谈时近二十年；早期记忆包括修复后的 SCSI 驱动将传输速率从每秒一百千字节提升到一兆字节。（BSDTalk EP229，[66.47-135.72]，L1）
- FlashRD 是把 OpenBSD 封装为只读系统的脚本：以 RAM disk 引导、经 CrunchGen 压缩工具集、装入完整通用内核而非功能受限的精简系统，把运行中系统封装为 VND 文件并支持换文件升级；其动机是闪存介质固有不可靠，当事人引 USENIX 会议实验称十五块受测闪存盘有十三块在写入断电时发生中度以上数据丢失乃至整体故障。（BSDTalk EP229，[190.13-246.25]，L1）
- 项目谱系：flashdist 需手工指定命令清单与闪存几何参数，在引导器仅支持 CHS 的年代以伪造几何参数立足；当 OpenBSD 引导器转向 LBA 且内核不再接受外部几何后其存在理由消失，flashboot 引入 RAM disk 使系统可整体升级，2009 年 flashrd 成型；作者同时观察到小型项目呈博客或邮件列表提及后热度与贡献短暂聚集、随后冷却的周期。（BSDTalk EP229，[574.35-754.16]，L1）
- NSH 源起于 2001 年作者用 WI 网卡搭建无线网络、面对熟悉 Cisco 命令行的同事需要降低 OpenBSD 路由器门槛的实操场景；它取材 telnet、ftp、ifconfig、route、arp 等常用工具思路，以单一简洁语法封装 PF、BGPD、SNMPD、OSPFD、DHCPd、smtpd 等守护进程配置，并用 SQLite 数据库区分内核自动状态与用户显式意图，写出单一 rc 风格配置文件。（BSDTalk EP229，[313.98-419.14]，L1）
- 设计哲学上作者曾计划把 pfctl 重写为共享库，因 PF 持续快速变动而放弃；NSH 改为只封装不重写既有配置语法，懂 PF 的用户无需学习第二套方言；后续方向是 Web 界面与 relayd URL 过滤文档，总目标是让不熟悉 vi 与文件系统细节的人也能使用 OpenBSD。（BSDTalk EP229，[1169.21-1263.43]，L1）
- 生产环境层面，作者长期在约二十余台异构机器（PC Engines ALIX、Super Micro Core 2 等）上运行 FlashRD，坚持最少可动部件原则，称 FlashRD 加 NSH 的组合可长期无人值守运行。（BSDTalk EP229，[769.16-815.33]，L1）

**史料**：

- AsiaBSDCon 2017 演讲幻灯片与日程（BSD Now EP186，[432.94-560.68]，L1）
- Philipp 访谈自述（BSD Now EP186，[3969.0-5733.62]，L1）
- OpenBSD PF 邮件列表与 CVS 历史（BSD Now EP186，[3969.0-4285.88]，L1）
- 一手史料以 Wooding 口述为主：mg 的 1986 年起源记忆、public domain 授权重构过程、theo mode 的由来、IPF 至 PF 更替的亲历叙述、OpenBSD Foundation 创始董事身份自述；开场栏目由主持人转述 netstat 命令最早出现于 4.2BSD。（BSDTalk EP200，[373.88-526.32]，L1）
- 一手口述史料：BSDTalk 第 220 期对视障用户 Eric Oyen 的 Skype 访谈录音（2012-11-30 发布，主持人 Will Backman，存档于 bsdtalk.blogspot.com），含其 OpenBSD 使用史、防火墙实践与无障碍工具链的自述。（BSDTalk EP220，[23.02-43.68]，L2）
- 邮件列表史料线索：受访者转述 Theo de Raadt 在 OpenBSD 邮件列表中就用户对厂商预装系统发牢骚的回应（大意“你疯了吗，那是厂商预装的，别来向我抱怨”），并描述 OpenBSD 分发材料中的免责声明与“附带源码、按原样提供”的软件包形态；该邮件未给出消息 ID，待查证。　[存疑脚注] 受访者凭记忆转述邮件列表往来，无消息 ID 与原文佐证，仅作线索。（BSDTalk EP220，[924.22-973.04]，L2）
- 当事人一手口述的 OpenBSD 入坑节点：1995 年 Theo 在 FTP 站点发布首个 SPARC 内核；同期并行接触 386BSD 与 Linux 的个人编年，可作项目早期传播路径的私人证词。（BSDTalk EP229，[101.89-135.72]，L1）
- 当事人转述的学术证据：某届 USENIX 会议论文以自制断电电路测试闪存盘写入可靠性，得出十五盘中十三盘受损或失效的结论；论文未给出题名与作者，需回溯检索原文献。　[存疑脚注] 当事人转述未提供论文题名作者与年份，引用前须检索 USENIX 原文核验（BSDTalk EP229，[219.77-241.69]，L2）
- flashdist、flashboot、flashrd 三代工具的演进序列与 flashrd 2009 年发布时点，及 NSH 的 SQLite 状态库设计细节，均为开发者本人自述的一手项目史。（BSDTalk EP229，[580.65-728.39]，L1）

**史观**：

- 总纲10 动手者创造历史：PF 由测试者、文档者与提交者共同打磨，历史由大量动手协作的人推动。（BSD Now EP186，[4016.52-4285.88]，L1）
- 总纲4 分离聚合是永恒规律：路由域把一台物理路由器分离为多个逻辑路由器，体现分离聚合的循环。（BSD Now EP186，[4381.84-4761.18]，L1）
- 总纲6 和解优于斗争：OpenBSD 社区“批评即受邀修复”的协作方式，强调和解与共建而非对抗。（BSD Now EP186，[4016.52-4050.66]，L1）
- 总纲13 法律与道德是利益分配：mg 的授权重构过程——逐个接洽在树作者、把分散的版权利益统一收束为 public domain——显示许可证选择在开源工程中本质上是围绕项目利益的法律形式安排，而非抽象的道德立场。（BSDTalk EP200，[116.68-137.44]，L1）
- 总纲10 动手者创造历史：Wooding 自述数年间漫游源码树、依 bug 报告唤醒注意、以 hackathon 间隙零星修复的维护方式，表明 OpenBSD 的日常演化由大量此类默默动手的个体贡献累积而成。（BSDTalk EP200，[493.80-521.64]，L1）
- 总纲9 经验优先：受访者的全部论据来自自身长期操作经验而非厂商宣传：以视障者的实际使用流程（SSH、串口、屏幕阅读器）检验系统设计的实际可及性，正是把当事人一手经验置于判断中心的路径。（BSDTalk EP220，[509.34-543.22]，L1）
- 总纲10 动手者创造历史：家用防火墙这类长期运转的基础设施由普通动手者搭建：受访者以一台将被淘汰的旧 Athlon 主机承担全家封包路由与过滤，并在 VMware 宿主内以 OpenBSD 虚机做单盒防火墙实验；这类沉默的实践者及其技艺传承（从 Linux iptables 到 PF）构成基础设施史的真实底层。（BSDTalk EP220，[1030.56-1069.10]，L1）
- 总纲10 动手者创造历史：作者的全部工具均从自身运维需求中长出——无线网络、无盘防火墙、面向同事的可用性——而非自上而下的项目规划；FlashRD 与 NSH 二十余年由其在职维护、服务真实机器，恰是动手者而非舞台人物书写技术史的一手素材。（BSDTalk EP229，[769.16-815.33]，L1）
- 总纲22 知识注定过时：flashdist 的衰落不是失败而是环境变迁：引导器 CHS 到 LBA 的转换、内核几何探测的强制化、八吉字节闪存跌至数美元，共同使手工几何管理的存在前提消失，作者自认继续维护是愚蠢的；技术方案的合理性随其所依附的物质条件一同过时。（BSDTalk EP229，[598.14-727.85]，L1）

**辨析**：

- [存疑脚注] 访谈中 2002 年 hackathon 地点、PF 实现细节系当事人十余年后回忆，需与 OpenBSD 邮件列表与 CVS 记录核验。　[存疑脚注] 当事人回忆性细节，缺乏独立档案印证。（BSD Now EP186，[3969.0-4285.88]，L4）
- mg 1986 年首发的说法为当事人回忆，其源自 MicroEMACS 谱系的精确传承（含原始作者与年份）须以源码历史与既存考据交叉验证；转写人名存在音误——受访者记作 Shell Wooding 应为 Kjell Wooding，Theo de Raadt 被记作 Theodore Atth——引用前须回查原音频。　[存疑脚注] 起源年份系当事人口述回忆，且转写人名音误，采信前须复核（BSDTalk EP200，[365.84-377.28]，L4）
- 无障碍需求与 OpenBSD 安装器极简主义之间的张力：受访者期望启动即朗读的安装镜像（需驱动检测），而项目现状是安装期依赖他人辅助或串口设备；他本人也承认不确定开发者是否会接受该特性，此判断仅为用户单方推测。　[存疑脚注] 对 OpenBSD 是否引入无障碍安装镜像的前景判断出自受访者个人推测，非项目方表态。（BSDTalk EP220，[178.50-211.66]，L4）
- 受访者对“预装 OpenBSD 的第三方设备出了问题是否归责于项目”的讨论，实际触及按原样分发、免责声明与社区支持边界的问题；其所转述的 Theo 回应立场强硬，但仅凭本期转写无法还原完整语境与邮件原文。　[存疑脚注] 邮件列表回应仅经受访者转述，需检索 OpenBSD misc 邮件列表存档核实原文后再采信。（BSDTalk EP220，[941.58-973.04]，L5）
- 转写将叔叔的机器记为 Triss 80 model 16B 并称可运行 CP/M 或 Xenix，机型拼写系转写噪音，TRS-80 Model 16B 的操作系统组合与购入年代需按机型史料核对，不得径直引用。[存疑脚注] 转写模糊，机型与操作系统组合待核。　[存疑脚注] 机型名与操作系统组合由受损转写推断，须与 Tandy 产品文献交叉核验后方可引用（BSDTalk EP229，[88.43-100.97]，L5）

**文献**：

- [BSD Now EP186] Pennington J. BSD Now: 186: The Fast And the Firewall: Tokyo Drift[EB/OL]. (2017-03-22)[2026-08-15]. <https://www.bsdnow.tv/186>.
- [BSDTalk EP200] Backman W. BSDTalk: 200: bsdtalk200 - The mg text editor with Kjell Wooding[EB/OL]. (2010-10-13)[2026-08-27]. <https://bsdtalk.blogspot.com/2010/10/bsdtalk200-mg-text-editor-with-kjell.html>.
- [BSDTalk EP220] Backman W. BSDTalk: 220: bsdtalk220 - Eric Oyen[EB/OL]. (2012-11-30)[2026-08-27]. <https://bsdtalk.blogspot.com/2012/11/bsdtalk220-eric-oyen.html>.
- [BSDTalk EP229] Backman W. BSDTalk: 229: bsdtalk229 - Chris Cappuccio[EB/OL]. (2013-08-07)[2026-08-27]. <https://bsdtalk.blogspot.com/2013/08/bsdtalk229-chris-cappuccio.html>.

<!-- /PODCAST_REVIEW -->

<!-- dangan-20260908 消解回写 -->
- OpenBSD. Canada Not-For-Profit Corporations Act S.C. 2009, c. 23[EB/OL]. 2009. ［待核·needs_fix］［DKC-0036→fulltext:5460］
<!-- /dangan-20260908 -->
