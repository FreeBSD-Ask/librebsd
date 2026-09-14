---
chapter: 第 16 章
id: CH16
volume: 第01卷-unix的起源
---

# 第 16 章 C++ Shell 家族与脚本语言生态

## 要点

- FreeBSD Ports 提供 GCC（g++）与 Clang/LLVM（clang++）两大 C++ 编译器；FreeBSD 10.0（2014 年 1 月）起 i386/amd64/arm 等平台默认使用 Clang/LLVM 3.3，GCC 4.2.1 不再默认构建（仅 pc98 等少数平台仍保留）；C++ 生态在 FreeBSD 用户态中稳定
- BSD 系统启动脚本（rc.d）、Ports 系统、大量系统工具均使用 Bourne shell 语法（sh）编写；csh 因编程特性缺陷（变量处理、语法不一致）不适合脚本编程，主要用于交互式使用；sh 作为 POSIX 标准 shell 保证脚本可移植性；FreeBSD 基础系统中的 sh 为 Almquist shell 衍生物，轻量且符合 POSIX，不包含 bash 特有扩展
- Sun 2006 年 GPL 化 Java（OpenJDK），2007 年开源；FreeBSD OpenJDK 移植由社区推动，2010 年起稳定；OpenJDK 6/7/8/11/17 均有 FreeBSD 移植；**OpenJDK BSD Port 项目**（openjdk.java.net/projects/bsd-port/，2026-07-28 WebFetch 核实）——由 OpenJDK Porters Group 赞助、以 BSD 授权许可工具链构建，为 2008-2013 年间 FreeBSD 上 OpenJDK 6/7 的主构建渠道，后被 openjdk6/openjdk7 Ports 移植取代
- FreeBSD Ports 系统本身用 shell 与 Makefile 实现，但管理脚本语言包；Ports 提供分发渠道，脚本语言丰富 Ports 内容，二者相互促进

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_1534] 卷“第01卷-unix的起源”第 16 章，匹配置信度 0.9，原因：关键词搜索下载文献，标题含章节主题

## 史观

总纲第 8 条——本体论上各方平等：GCC 与 Clang/LLVM 两大编译器、各脚本语言实现（sh/csh/perl/python/ruby）在 FreeBSD 生态中平等参与，取舍依任务而定（与 16.5/16.6/16.8 映射一致）；总纲第 5 条——没有必然性，只有偶然性：Java 免费发行与 GPL 化、OpenJDK 移植的启动均系偶然事件（与 16.7 映射一致）；总纲第 4 条——分离聚合是永恒规律：csh 与 sh 两大 shell 谱系分化、perl/python/ruby 与 Ports 的共生聚合（与 16.6/16.8 映射一致）；总纲第 9 条——经验优先：脚本语言取舍以工程实践经验为准，社区对 csh 脚本缺陷的认知源于长期运维经验（与 16.6 映射一致）。子节级映射详见 16.5-16.8 各节史观字段

## 辨析

- FreeBSD 切换至 Clang 的具体时间线——FreeBSD 9.0（2012 年 1 月）已默认安装 Clang 3.0 但默认编译器仍为 GCC 4.2.1，需设置 WITH_CLANG_IS_CC 选项方可切换；FreeBSD 10.0（2014 年 1 月）i386/amd64/arm 等平台正式以 Clang 为默认系统编译器，GCC 4.2.1 仅在 pc98 等平台保留；GCC 自基础系统的最终移除在 FreeBSD 12/13 时期完成（12.0 起 default 工具链无 GCC），用户须经 Ports 安装 lang/gcc；引用版本决策时须以 src commit 与 release notes 为准
- csh 不适合脚本编程——这是 UNIX 社区长期共识，经典论文《Csh Programming Considered Harmful》有详述 [存疑脚注：该文通行版本为 Paul W. Abrahams 与 Larsen 的 1996 年起流传版，年份存疑，引用时以能核验的在线版本为准]；系统脚本坚持使用 POSIX sh 是工程与可移植性的选择
- OpenJDK FreeBSD 移植的版本覆盖——并非所有 LTS 版本均完整移植；OpenJDK BSD Port 项目覆盖 FreeBSD、OpenBSD、NetBSD、Mac OS X 四个 BSD 系平台，但各平台的版本覆盖与维护程度不一，FreeBSD 与 Mac OS X 为主要维护目标，OpenBSD 与 NetBSD 的版本更新存在滞后；[考据完成：2026-07-28 该处存疑标注经 BSD Port 项目页（openjdk.java.net/projects/bsd-port/）与 BSDPort Wiki（wiki.openjdk.org/display/BSDPort/Main，最后更新 2013-02-19）交叉核验，项目于 2011 年 7 月正式启动、2013 年后并入官方 openjdk6/7 Ports 移植路线，此判读属合理推断而非一手确证，引用时须注明]
- FreeBSD src/etc/rc.d/ 脚本源码；POSIX 1003.1-2008 Shell Command Language；FreeBSD Porter's Handbook ［A］
- Sun 2006 Announcement；OpenJDK BSD Port Project (openjdk.java.net/projects/bsd-port/，2026-07-28 WebFetch 核实)；OpenJDK BSD Port Wiki (wiki.openjdk.org/display/BSDPort/Main，2026-07-28 WebFetch 核实，Dalibor Topic 创建，Brian Beck 2013-02-19 最后更新)；FreeBSD Ports (openjdk6: freshports.org/java/openjdk6/；openjdk7: freshports.org/java/openjdk7/)；OpenJDK Documentation；FreeBSD OpenJDK Porting Guide；wiki.freebsd.org/Java（2026-07-28 WebFetch 核实） ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。

> 1995-1995 年间：9,812 次提交。


- FreeBSD Porter's Handbook；FreeBSD Ports Tree；FreeBSD Documentation ［B］

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP523、BSD Now EP406、BSD Now EP321（共 3 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 该期转述 Thomas Scoville 1998 年《The Elements of Style: Unix as Literature》一文，将 Unix 内核视为少数思维同步者的共同创作，主张 Unix 传统根植于以文本、命令行为核心的文字文化，并与 Windows NT 的点选式图像文化形成对照；作者以文学修养解释 Unix 从业者中人文背景者比例偏高的现象。（BSD Now EP523，[568.60-865.28]，L2）
- 节目借 shell 隐式按空白分词导致文件名与参数被错误拆分的问题，回溯约 1979 年 Steve Bourne 引入 $* 后因其实用性不足而增补 $@ 特殊情形的实现史，并称这一未纠正的设计缺陷长期困扰 shell 编程，rc shell 因规避此问题而受到推荐。（BSD Now EP523，[882.48-1382.28]，L2）
- 节目摘录 Theo de Raadt 在 OpenBSD tech 邮件列表对 Zenbleed 漏洞的评估：OpenBSD 基础系统很少使用 AVX 指令，影响远小于依赖 glibc AVX 优化的 Linux；OpenBSD 已通过 current 快照与后续 errata 修复，并提醒用户必须手工安装引导块以加载 CPU 固件更新。（BSD Now EP523，[1393.64-1582.44]，L1）
- 其余新闻包括 OPNsense 23.7 以 FreeBSD 13.2 为基础内核发布、Brian Robert Callahan 将 PCC 可移植 C 编译器移植到 illumos，以及用户因 ThinkPad BIOS 白名单和 Linux 无线驱动 GPL 兼容性限制而通过更换网卡修复 FreeBSD 无线支持。（BSD Now EP523，[1586.96-2244.58]，L2）
- 一篇教程记述在 FreeBSD jail 中以 easyjail 部署 Gemini 服务器 Molly Brown 的过程，包括克隆接口、SSL 证书、rc.d 服务脚本与 jail 内 SSH 访问，展示 jail 作为轻量隔离环境承载新协议的实践路径。（BSD Now EP406，[273.92-470.8]，L2）
- FreeBSD 2021 年第一季度状态报告显示，doc、src、ports 三仓库已切换至 Git，CI 作业与文档工具链随之迁移至 Git 与 AsciiDoc/Hugo，并记录 13.0 发布与 Linux 兼容层支持 Firefox Widevine 的进展。（BSD Now EP406，[476.4-1461.2]，L2）
- Michael W Lucas 在采访中自述，1995 年美国国家科学基金会全面商业化互联网后，其管理的客户端域名服务器频繁崩溃，直至安装 FreeBSD 名称服务器才获得整夜睡眠，由此转向 OpenBSD 与 FreeBSD 世界并最终成为全职技术作者。（BSD Now EP406，[1721.98-1828.6]，L1）
- 主持人说明 BSD grep 的重写源于编程之夏（Google Summer of Code），采用现代搜索算法后仍存在边缘情况慢于 GNU grep，最终修复并成为 FreeBSD 默认，GNU grep 保留为编译期选项。（BSD Now EP406，[2820.16-2956.14]，L2）
- Trenton Schultz 在明尼苏达读本科时因实验室游戏夜初识 FreeBSD 2.2.5，后以 Qt 小程序与纯文本简历入职 Trolltech，参与 Qt Embedded 与 Cocoa 移植，其第一个 Qt 提交是把 Qt 虚拟帧缓冲从 Linux 专用信号量改为 FreeBSD 兼容实现。（BSD Now EP321，[120.62-445.88]，L1）
- ROS 是发布/订阅式机器人中间件，节点以话题通信、可跨机分布，默认跟随 Ubuntu LTS；Schultz 2017 年移植因 OpenCV 版本与 Python Qt 绑定混乱受阻，2019 年借 jails 的干净环境重试成功基础通信与可视化。（BSD Now EP321，[882.08-1217.88]，L1）
- FreeBSD jails 让 ROS 构建与桌面 Qt 版本隔离，避免依赖冲突；Schultz 强调读 Michael W. Lucas 的 jails 书后才理解 nullfs、devfs 等前置知识，并首次成功搭出 CUPS jail。（BSD Now EP321，[1193.60-1367.12]，L1）
- Schultz 的博士研究关注家庭机器人隐私框架与人机交互动画，指出 ROS1 无安全设计（动态 UDP 端口、需 VPN 或封闭网络），摄像头数据是否外传决定隐私风险等级。（BSD Now EP321，[632.94-690.32]，L1）
- 对 BSD 新手的建议：与朋友结伴、用虚拟机试错、尽早配置 ZFS 自动快照与引导环境以获得回滚能力，从而敢于动手。（BSD Now EP321，[2071.72-2250.44]，L1）

**史料**：

- Thomas Scoville《The Elements of Style: Unix as Literature》（1998 年网络文章，作者自述 1983 年起使用 Unix，时任 Expert Support Inc 工程师），为当期主持人转述的二手文本。（BSD Now EP523，[568.60-868.00]，L2）
- OpenBSD tech 邮件列表存档中 Theo de Raadt 关于 Zenbleed 的帖子，当期节目摘录了其原文段落，属于当事人一手陈述。（BSD Now EP523，[1393.64-1582.44]，L1）
- Steve Bourne 约 1979 年对 shell 参数展开加入 $@ 补丁的实现史线索，经节目口头转述，需以原始 shell 源码与历史手册进一步核验。　[存疑脚注] 该时间与补丁细节为单一博客转述，未见节目提供原始提交或文档编号，须交叉验证。（BSD Now EP523，[1110.76-1299.52]，L4）
- Michael W Lucas 关于 1995 年以 33.6k 拨号管理名称服务器、试用 Linux 与 Windows NT 未果、最终依赖 FreeBSD 获得稳定运行的叙述，属当事人一手口述史料。（BSD Now EP406，[1772.42-1822.78]，L1）
- FreeBSD 2021 年第一季度状态报告记载 doc 迁移于 2021 年 1 月 23 日完成，由 Sergio Carlavilla 等维护文档基础设施，属可核对的一手工程记录。（BSD Now EP406，[1070.12-1096.9]，L2）
- Trenton Schultz 本人访谈自述（Trolltech 七年与 Nokia 一年经历、ROS 移植、博士研究）。（BSD Now EP321，[105.18-119.16]，L1）
- Michael W. Lucas《FreeBSD Mastery: Jails》及配套六书（Schultz 转述其阅读体验与前置知识结构）。（BSD Now EP321，[1259.36-1339.12]，L2）
- EuroBSDCon 2019 Lillehammer 的 ROS on FreeBSD 演讲，为 Schultz 本人报告。（BSD Now EP321，[1459.40-1468.78]，L1）

**史观**：

- 总纲第 15 条——文化即形式主义：Unix 文字文化与 NT 图像文化均为形式化构造，界面传统是习惯与权力的形式主义表达。：Unix 与 NT 的文字/图像文化对立，显示界面传统本身即形式主义构造，两种文化形态是各自权力与习惯的形式化表达。（BSD Now EP523，[568.60-865.28]，L2）
- 总纲第 9 条——经验优先：以当事人长期使用经验作为判断系统的依据，而非先行的抽象标准——Scoville 以十多年使用经验而非抽象标准评判系统，Unix 社区的知识权威来自长期动手经验。（BSD Now EP523，[568.60-865.28]，L2）
- 总纲第 10 条——动手者创造历史：shell 惯例由具体实现者的补丁与妥协形塑，而非出自抽象设计蓝图——shell 空白分词与 $@ 补丁由 Bourne 等具体实现者的工程决策沉淀为长期惯例，动手者的选择塑造了后续数十年的编程实践。（BSD Now EP523，[1110.76-1299.52]，L2）
- 总纲第 9 条——经验优先：Michael W Lucas 以一线系统管理员身份在崩溃与抢修中验证 FreeBSD 的稳定性，其写作生涯源于实际运维经验，属经验优先与动手者创造历史的例证。（BSD Now EP406，[1772.42-1825.98]，L1）
- 总纲第 4 条——分离聚合是永恒规律：FreeBSD 从 Subversion 到 Git 的迁移及文档从 SGML/XML 到 AsciiDoc 的切换，是工具链层面的分离聚合重组，旧基础设施被分阶段替代而非一次性革命。（BSD Now EP406，[776.52-1096.9]，L2）
- 总纲第 10 条——动手者创造历史：Schultz 以一天搭通通信层、亲手改信号量调用等动手移植推动 ROS 进入 FreeBSD。（BSD Now EP321，[1052.42-1067.84]，L1）
- 总纲第 9 条——经验优先：因不想网络跳转的实际需求驱动移植，经验场景优先于宏大目标。（BSD Now EP321，[1002.64-1021.60]，L1）
- 总纲第 7 条——理论必须自反：机器人隐私研究要求自问“谁还能看到这段影像”，对技术后果保持反思。（BSD Now EP321，[2751.92-2778.28]，L1）
- 总纲第 5 条——没有必然性，只有偶然性：能否移植取决于 OpenCV 恰好入 ports、Qt 恰好现代化等偶然条件。（BSD Now EP321，[1178.12-1193.60]，L1）
- 总纲第 22 条——知识注定过时：2017 年失败到 2019 年成功，只因 ports 生态与工具链随时间变化。（BSD Now EP321，[1180.52-1186.20]，L1）
- 总纲第 8 条——本体论上各方平等：FreeBSD 作为副业与 ROS/Ubuntu 研究主线的并存被平等叙述，不贬低任何工具。（BSD Now EP321，[786.20-794.40]，L1）

**辨析**：

- Scoville 一文的文化判断以个人见闻为主，作者自述其证据粗略且轶事化，因此其文字文化与图像文化的概括应视为个人观察而非统计结论。　[存疑脚注] 该判断来自单一作者的事后文化观察，未见系统抽样或多源数据支撑。（BSD Now EP523，[568.60-865.28]，L4）
- Zenbleed 影响评估来自 OpenBSD 一方，称基础系统少用 AVX，但浏览器等第三方程序仍可能触发泄漏，需结合 AMD 官方披露与独立复现实验交叉验证。　[存疑脚注] OpenBSD 视角的评估需与 AMD 官方技术通报及独立测试结果交叉验证后方可采信。（BSD Now EP523，[1393.64-1582.44]，L4）
- 转写对 BSD grep 重写的编程之夏（GSoC）年份与算法细节语焉不详，其引入时间与性能争议需与 FreeBSD 提交记录对照。　[考据脚注] BSD grep 重写的编程之夏（GSoC）项目年份与合入版本需查 FreeBSD 提交历史。（BSD Now EP406，[2820.16-2879.38]，L4）
- ROS1 安全缺陷为 Schultz 的口头概括，具体攻击面与 ROS2 改进需以官方文档核对。　[存疑脚注] 当事人经验性总结，未给出版本与漏洞编号（BSD Now EP321，[2607.66-2634.28]，L4）
- 访谈转写存在大量口语断句，人名与版本号（如 FreeBSD 2.2.5）为当事人记忆，可能与档案有出入。　[考据脚注] 早期版本号系回忆，宜以发布记录核对（BSD Now EP321，[218.92-221.50]，L4）

**文献**：

- [BSD Now EP523] Pennington J. BSD Now: 523: Literally Unix[EB/OL]. (2023-09-07)[2026-08-15]. <https://www.bsdnow.tv/523>.
- [BSD Now EP406] Pennington J. BSD Now: 406: Jailed Gemini Capsule[EB/OL]. (2021-06-10)[2026-08-15]. <https://www.bsdnow.tv/406>.
- [BSD Now EP321] Pennington J. BSD Now: 321: The Robot OS[EB/OL]. (2019-10-24)[2026-08-15]. <https://www.bsdnow.tv/321>.

<!-- /PODCAST_REVIEW -->

<!-- dangan-20260908 消解回写 -->
- Greer. K. tcsh: The TENEX C Shell [EB/OL]. [2026-07-19]. <https://www.tcsh.org/>[EB/OL]. 2026. ［待核·needs_fix］［DKC-0860→fulltext:5689］
- Korn. D G. ksh: The KornShell [EB/OL]. [2026-07-19]. <http://www.kornshell.com/>[EB/OL]. 2026. ［待核·needs_fix］［DKC-0861→fulltext:5690］
<!-- /dangan-20260908 -->
