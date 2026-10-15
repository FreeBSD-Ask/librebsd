---
chapter: 第 159 章
id: CH159
volume: 第08卷-freebsd的范式转换
---

# 第159章 计算机安全史的早期unix安全与morris蠕虫

## 要点

- 还原 1988 年 11 月之前互联网的整体安全图景——1980 年代末互联网约有 6 万台主机连接，主要分布在大学、科研机构和军方；安全防御呈散兵游勇状态，各机构自行管理、缺乏协调；漏洞信息通过 Usenet 新闻组（如 comp.security.unix）口耳相传，没有统一的漏洞编号或公告体系；系统管理员的安全实践高度依赖个人经验，弱密码、开放服务、默认配置是普遍问题；Morris 蠕虫的爆发并非凭空出现，而是这一时期安全状况的集中暴露
- 梳理 1960–1980 年代 Bell Labs 与 MIT 在计算机安全领域的奠基性工作——Multics 项目（1964–1969）的安全模型（分层保护环、强制访问控制）为后续 UNIX 安全提供了思想源头；丹尼斯·里奇（Dennis Ritchie）1970 年代初发明 setuid 机制（1973 年 Bell Labs 申请专利，1979 年授权，美国专利 4,135,240 “Protection of data file contents”）；MIT 的 Project Athena（1983 年启动）在分布式系统安全方面的探索；肯·汤普森（Ken Thompson）1983 年图灵奖演讲《Reflections on Trusting Trust》揭示编译器后门的哲学问题，影响深远
- 考察 UNIX 两大核心安全机制的起源与历史演化——setuid（设置用户标识符）由 丹尼斯·里奇 发明，最早出现在 UNIX V4/V5 时代，初衷是让特定程序（如 passwd）以文件所有者权限运行，从而实现最小权限原则；chroot（改变根目录）最早出现在 Unix V7（1979 年），比尔·乔伊（Bill Joy）于 1982 年 3 月 18 日将 chroot 系统调用加入 4.2BSD（早于 4.2BSD 正式发布约一年半），最初用于构建和测试发布环境，而非安全隔离；这两大机制既是 UNIX 安全的基石，也是无数漏洞的来源——setuid 程序的编写极其困难，chroot 并非为安全设计因而存在多种逃逸方式
- 还原 1980 年代黑客文化的社会语境与安全漏洞的传播生态——1983 年电影《WarGames》公映引发公众对黑客和网络安全的关注；同年 Telenet 商用数据网络发生一系列高调入侵事件，暴露了弱密码和开放访问的普遍性；Usenet 和 BBS 成为漏洞信息交换的主要渠道，黑客社区与安全社区界限模糊；Matt Bishop 1981–1983 年撰写的 UNIX 漏洞报告描述了 21 个漏洞、分为 6 大类（setuid 问题、配置问题、密码强度、信任关系、程序错误、物理安全），其中多数问题至今仍未根本解决；这一时期的漏洞披露没有固定规范，全披露（full disclosure）文化已在地下社区萌芽
- 考证 CERT/CC 成立的精确时间线——1988 年 11 月 2 日 Morris 蠕虫爆发，11 月 8 日 NCSC 召开蠕虫事后分析会议，11 月 17 日 DARPA 正式成立 CERT/CC 于卡内基梅隆大学软件工程研究所（CMU SEI），首任主任 Richard (Rich) D. Pethia；CERT 并非 “Computer Emergency Response Team” 的缩写，而是注册商标；CERT/CC 是全球第一个 CSIRT（计算机安全事件响应团队）

## 史观

- 总纲第 15 条——文化即形式主义（原“哲学思潮”系伪标签，按报告处方重挂）：Morris 蠕虫之前的安全状况是一种 “自然状态”——没有规则、没有机构、没有标准，每个人各自为战。这种状态的终结标志着安全从个人技艺走向制度化学科
  - 辨析：“1988 年之前没有安全研究” 是常见误解——实际上 Bell Labs、MIT、Purdue 等机构已有扎实的安全研究，但研究成果与工程实践之间存在巨大鸿沟；漏洞是已知的，但修补的激励和协调机制不存在
- 总纲第 15 条——文化即形式主义（原“形式主义膨胀”系伪标签，按报告处方重挂）：setuid 和 chroot 都是用极简的形式机制（一个比特位、一个系统调用）解决复杂的安全问题，它们的简洁性既是力量的源泉，也是问题的渊薮——形式化抽象越简洁，误用和被绕过的可能性就越大
  - 辨析：chroot 常被误认为是安全隔离机制，但它的设计初衷是构建环境，安全性只是 “副产品”；这一误解导致了大量基于 chroot 的不安全部署，直到 FreeBSD jail（2000 年）和 Linux namespaces 才真正从设计层面解决了隔离问题；setuid 机制则被反复证明是安全事故的重灾区，但至今仍无更优的普适替代方案
- 总纲第 13 条——法律与道德是利益分配（原“开源运动”系伪标签，按报告处方重挂）：CERT/CC 的成立标志着互联网安全从个人自发应对转向制度化协作，这与开源运动从个人黑客到社区协作的演进路径同构
  - 辨析：CERT/CC 成立的精确日期存在多种说法（11 月中旬、11 月底、12 月初），经交叉验证应以 11 月 17 日 DARPA 正式批准日为准；“CERT 是缩写” 的说法是常见误解，官方明确说明 CERT 是注册商标而非首字母缩写

- 总纲第 13 条——法律与道德是利益分配（原“密码学”系伪标签，挂靠存疑，按报告处方重挂）：RSA 算法的发明与专利化体现了密码学从军事机密向民用技术转变过程中的法律与经济张力，BSD 系统在这一张力中寻求技术可能性与法律合规的平衡
  - 辨析：RSA 专利的到期日（2000 年 9 月）是加密软件生态的重要转折点，先前 BSD 系统需通过 RSAREF 等受限实现绕开专利，此后 OpenSSL 等自由实现得以完整包含 RSA；但专利只是制约因素之一，出口管制的影响更为深远
- 总纲第 3 条——不存在进步，只有权力再分配（原“终结与延续”系伪标签，挂靠存疑，按报告处方重挂）：SSL/TLS 从 Netscape 的商业产品演变为 IETF 开放标准，从早期脆弱的 SSL 2.0 发展到高度优化的 TLS 1.3，既是加密技术的延续，也是安全工程实践不断进化的结果
  - 辨析：LibreSSL fork 事件（2014 年 Heartbleed 后）是安全工程路线分歧的典型案例——OpenBSD 团队认为 OpenSSL 代码质量差、过度工程化，选择 fork 并大规模清理；FreeBSD 选择继续使用 OpenSSL 但加强本地安全加固；不同选择反映了不同项目的风险偏好和工程哲学

## 辨析

- “1988 年之前没有安全研究” 是常见误解——实际上 Bell Labs、MIT、Purdue 等机构已有扎实的安全研究，但研究成果与工程实践之间存在巨大鸿沟；漏洞是已知的，但修补的激励和协调机制不存在；Morris 蠕虫的真正历史意义不在于发现了新漏洞，而在于证明了互联系统的系统性风险
  - 文献：Bishop, M. (2009). *Reflections on UNIX Vulnerabilities*. ACSAC '09
- chroot 常被误认为是安全隔离机制，但它的设计初衷是构建环境，安全性只是 “副产品”；这一误解导致了大量基于 chroot 的不安全部署，直到 FreeBSD jail（2000 年）和 Linux namespaces 才真正从设计层面解决了隔离问题；setuid 机制则被反复证明是安全事故的重灾区，但至今仍无更优的普适替代方案
  - 文献：Chen, H., Wagner, D., & Dean, D. (2002). *Setuid Demystified*. USENIX Security Symposium; McKusick, M. K. (2000). *Jails: Confining the Omnipotent Root*. BSDCon 2000; FreeBSD Project. **jail(8)** 手册页（4.4BSD 历史注释）
- CERT/CC 成立的精确日期存在多种说法（11 月中旬、11 月底、12 月初），经交叉验证应以 11 月 17 日 DARPA 正式批准日为准；“CERT 是缩写” 的说法是常见误解，官方明确说明 CERT 是注册商标而非首字母缩写
  - 文献：Carnegie Mellon University. (2016, Sep 1). *CERT Director Richard Pethia Retires*. sei.cmu.edu; FIRST Organization. (2025). *Richard (Rich) D. Pethia - Hall of Fame*. first.org/hof/inductees; CERT/CC. *Frequently Asked Questions*. cert.org/faq
- RSA 专利的到期日（2000 年 9 月）是加密软件生态的重要转折点，先前 BSD 系统需通过 RSAREF 等受限实现绕开专利，此后 OpenSSL 等自由实现得以完整包含 RSA；但专利只是制约因素之一，出口管制的影响更为深远
  - 文献：Rivest, R. L., Shamir, A., & Adleman, L. (1978). *A Method for Obtaining Digital Signatures and Public-Key Cryptosystems*. Communications of the ACM, 21(2), 120-126
- LibreSSL fork 事件（2014 年 Heartbleed 后）是安全工程路线分歧的典型案例——OpenBSD 团队认为 OpenSSL 代码质量差、过度工程化，选择 fork 并大规模清理；FreeBSD 选择继续使用 OpenSSL 但加强本地安全加固；不同选择反映了不同项目的风险偏好和工程哲学
  - 文献：IETF. (2018). *RFC 8446 - The Transport Layer Security (TLS) Protocol Version 1.3*

## 文献

- Bishop, M. (2009). *Reflections on UNIX Vulnerabilities*. ACSAC '09; Vagts, B. K. (2024). Telenet, the 1983 Hacking Incidents, and the Construction of Network Security. IEEE Annals of the History of Computing, 46(1); Spafford, E. H. (1989). *The Internet Worm: Crisis and Aftermath*. Communications of the ACM, 32(6), 678-702
- Chen, H., Wagner, D., & Dean, D. (2002). *Setuid Demystified*. USENIX Security Symposium; McKusick, M. K. (2000). *Jails: Confining the Omnipotent Root*. BSDCon 2000; FreeBSD Project. **jail(8)** 手册页（4.4BSD 历史注释） ［A］

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP325、BSD Now EP281（共 2 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- FreeBSD 12.1 是首个以 open ZFS 端口支撑原生 ZFS 加密所需密码学原语的版本，同时导入 BearSSL 为 Juniper 的验证引导装载器提供轻量 TLS，并纳入 MLX5 固件更新工具与 FUSE 驱动重写。（BSD Now EP325，[63.84-68.92]，L2）
- 12.1 预告 i386 默认 CPU 类型将由 486 升至 686（自 13 起），因 486 缺 64 位原子操作且用户态无法模拟；CTM 与 timed 等工具被标记废弃。（BSD Now EP325，[543.78-594.94]，L2）
- 重刊的《Unix Evolution 1975–1984》一文梳理 research Unix v6/v7/v8 的文本格式化、编译器与开发工具流变，并记述 Ritchie 关于 man page BUGS 节以公开羞辱促修复的自述。（BSD Now EP325，[723.74-1018.28]，L2）
- OpenBSD 在 base unbound 默认启用 DNSSEC 验证，并以 Quad9 的 9.9.9.9 做约束验证绕开 NTP 与 DNSSEC 的时钟引导死锁；2018 年曾因时钟问题回滚后于此次重开。（BSD Now EP325，[2062.14-2169.84]，L2）
- Rainbow Crack 的 OpenBSD 编译补丁引出彩虹表原理：加盐与多轮散列（bcrypt 可至百万轮、SHA-512 crypt 默认万轮）使针对字典的预计算表失效，凸显密码存储需抗彩虹表算法。（BSD Now EP325，[2632.88-2909.48]，L2）
- 美国国家发明家名人堂在 CES 上公布 2019 届入选者，追授 Dennis Ritchie、表彰 Ken Thompson，称 Unix 操作系统与 C 语言是计算机科学进展中的关键发展。（BSD Now EP281，[1211.92-1305.92]，L2）
- SCP 客户端系列漏洞由 F-Secure 的 Harry Sintonen 发现：多个客户端未校验服务器返回的文件名，源于 1983 年 rcp 的实现传统，可导致任意文件写入与输出欺骗。（BSD Now EP281，[104.44-140.16]，L2）
- Phoronix 在 AMD EPYC 7601 服务器上对比 FreeBSD 11.2、12.0、DragonFly BSD 5.4.1、TrueOS 18.12 与多款 Linux 发行版，主持人强调基准测试须追问“为什么”并自行验证。（BSD Now EP281，[762.00-1204.20]，L2）

**史料**：

- FreeBSD 12.1 发布公告与 releng 说明，列明 open ZFS、BearSSL、MLX5、FUSE 重写及废弃项。（BSD Now EP325，[128.32-148.56]，L2）
- Microsystems Magazine 1984 年 11 月号《Unix Evolution》文章（Daemon News 1999 重刊），为节目重读的历史文本。（BSD Now EP325，[740.14-756.02]，L2）
- Dennis Ritchie 关于 man page BUGS 节政策的引文，属当事人一手表述。（BSD Now EP325，[1012.82-1027.82]，L1）
- OpenBSD unbound.conf 默认 DNSSEC 与 aggressive NSEC 的提交说明，及与 Quad9 的约束验证讨论。（BSD Now EP325，[2077.00-2124.28]，L2）
- 提及 CVE-2018-20685、CVE-2019-6111 等 SCP 相关编号，以及 CVE-2000-0992（2000 年 SCP 任意文件覆盖漏洞）作为同类漏洞的历史对照。（BSD Now EP281，[641.76-654.40]，L2）
- 提及 BSD 社区通过自定义内核配置关闭 IPv4 栈（option INET 移除）并以 IPv6 单栈运行的记录，以及 IPv5 仅停留于想法的历史细节。（BSD Now EP281，[1605.04-1803.76]，L2）

**史观**：

- 总纲3 不存在进步，只有权力再分配：总纲3 不存在进步，只有权力再分配：i386 486→686、GCC 4.2 弃用、CTM 与 timed 废弃不是进步，而是支持资源在不同架构间的再分配。（BSD Now EP325，[567.10-625.50]，L2）
- 总纲8 本体论上各方平等：总纲8 本体论上各方平等：FreeBSD、OpenBSD、HardenedBSD、OPNsense 同屏报道，各分支地位平等，不以体量定优劣。（BSD Now EP325，[1698.58-1805.42]，L2）
- 总纲10 动手者创造历史：总纲10 动手者创造历史：Tom Jones 以 git worktree、tmux、cscope、bhyve 的动手流程呈现 FreeBSD 开发者的真实工作方式。（BSD Now EP325，[1317.46-1484.78]，L2）
- 总纲22 知识注定过时：总纲22 知识注定过时：1984 年文章自承需源许可并签血誓方可读源码，而 V7 源码迟至 2002 年由 Caldera 释放，知识条件随时间失效。（BSD Now EP325，[923.02-977.30]，L2）
- 总纲12 科学是形式主义：总纲12 科学是形式主义：密码学的“安全”依赖加盐与轮数的形式约定，彩虹表攻击揭示其相对性而非绝对真理。（BSD Now EP325，[2864.92-2909.48]，L2）
- 总纲5 没有必然性，只有偶然性：总纲5 没有必然性，只有偶然性：OpenBSD 2018 年曾默认开 DNSSEC 后回滚、2019 年再启用，取决于时钟引导问题被偶然解决。（BSD Now EP325，[2124.78-2143.00]，L2）
- 总纲22 知识注定过时：Unix 与 C 在诞生五十年后被纳入国家发明家名人堂，与手持电钻、降压药、含氟牙膏并列，显示基础设施性的技术创造被事后追认为“一直存在”的常识。（BSD Now EP281，[1423.56-1454.40]，L2）
- 总纲2 历史是形式主义化的非存在：从 1983 年 rcp 延续到 2019 年 SCP 客户端漏洞，早期协议的实现假设在数十年后成为安全隐患，说明技术决策的历史惯性远超其原初语境。（BSD Now EP281，[140.16-182.68]，L2）

**辨析**：

- Rainbow Crack 网站自 2007 年后基本未更新，教程提及的某域名已被劫持为垃圾页，该工具的可用性与教程安全性存疑。　[考据脚注] 站点域名易主，链接与补丁来源需重新核实（BSD Now EP325，[2683.40-2706.96]，L4）
- 12.1 的 open ZFS 与原生加密支持为发布说明转述，具体实现路径与加密原语宜以 FreeBSD 源码树核对。　[存疑脚注] 转写对“首个支持 open ZFS 端口的正式版”表述较口语化（BSD Now EP325，[68.92-90.80]，L4）
- 主持人指出部分基准差异可能源于 Clang 版本、ZFS 缓存与编译选项而非操作系统本身，强调不追问“为什么”的基准结果不可信，此类比较不宜直接作为性能结论。（BSD Now EP281，[1144.52-1204.20]，L3）

**文献**：

- [BSD Now EP325] Pennington J. BSD Now: 325: Cracking Rainbows[EB/OL]. (2019-11-21)[2026-08-15]. <https://www.bsdnow.tv/325>.
- [BSD Now EP281] Pennington J. BSD Now: 281: EPYC Server Battle[EB/OL]. (2019-01-17)[2026-08-15]. <https://www.bsdnow.tv/281>.

<!-- /PODCAST_REVIEW -->

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-1269 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1269`；w172 YouTube 章节路由采纳）

据〔EuroBSDcon 2022〕讲者 Samuel Aubertin 口述：本议题涉及 Ken Thompson 的论文《Trusting Trust》，讲者口述年份为 1974（紧随的转写另出现 84，年份存疑）。（YouTube EPikAbK9HFwkI，[205.58-215.509]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->
