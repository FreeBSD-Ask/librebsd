# 第 136 章 freebsd安全模型的unix-dac与权限机制

---
chapter: 第 136 章
id: CH136
volume: 第07卷-freebsd的工程体系重构
---

## 要点

- FreeBSD 的基础安全模型继承自传统 UNIX 自主访问控制（Discretionary Access Control, DAC），该模型由 丹尼斯·里奇（Dennis Ritchie）和 肯·汤普森（Ken Thompson）在 1970 年代初的 UNIX 第一版中设计；核心机制包括：每个文件/目录有 12 个权限位——owner（用户）读/写/执行、group（组）读/写/执行、other（其他）读/写/执行，加上 setuid（设置用户 ID）、setgid（设置组 ID）、sticky bit 三个特殊位；setuid/setgid 机制允许程序以文件所有者（通常是 root）的权限运行，这是 UNIX 权限提升的核心机制，但也是历史上大量本地提权漏洞的来源；root 用户（UID 0）在传统 DAC 模型下拥有对系统的完全控制权，绕过所有权限检查——“root  omnipotent” 是传统 UNIX 安全模型最显著的特征也是最大的安全弱点
- 在传统 UNIX DAC 模型中，UID 0（root）是 “超级用户”，内核中所有权限检查对 UID 0 直接放行；FreeBSD 历史上通过多种机制对 root 权限进行限制：**securelevel(7)** 机制（1980 年代 BSD 引入，通过 `kern.securelevel` sysctl 控制系统安全级别，高级别下 root 也无法执行某些操作如修改不可变文件、直接访问原始磁盘、加载内核模块等）；**jail(8)** 将 root 限制在 jail 内部；MAC 框架可进一步限制 root 操作；Capsicum 能力模式下即使是 root 也受能力描述符限制；FreeBSD 的 securelevel 有五个级别[存疑脚注：原文误作“四个级别”；FreeBSD Handbook 明确记载 'The kernel runs with five different security levels’，即 -1/0/1/2/3]：-1（完全禁用）、0（默认，不安全）、1（安全模式，不可修改不可变文件、不能加载模块）、2（高安全，进一步限制磁盘操作和原始套接字）、3（最高安全，与 2 类似但某些计时参数调整也被禁止）
- **jail(8)** 由 Poul-Henning Kamp（波尔-亨宁·坎普） 设计，首次出现在 FreeBSD 4.0-RELEASE（2000 年 3 月 14 日发布），是 FreeBSD 首个原生 OS 级虚拟化机制；原始 jail 通过 **chroot(2)** 增强实现，为监禁进程提供独立的主机名、IP 地址、文件系统根目录视图，但 jail 内 root 用户仍受诸多限制（如无法修改内核参数、无法加载模块、无法访问原始套接字等）；jail 的设计目标是作为安全隔离环境而非完整虚拟化方案，与传统 chroot 相比增加了对进程间通信、网络、系统 VIPC 等资源的隔离约束；FreeBSD 4.x 时代的 jail 存在若干已知逃逸漏洞（如通过特定 sysctl 或挂载点逃逸），后续版本持续加固
- Capsicum 能力模型由剑桥大学 罗伯特·N. M. 沃森 团队设计，核心论文发表于 USENIX Security 2010，FreeBSD 9.0-RELEASE（2012 年 1 月 12 日）首次在 GENERIC 内核中集成 Capsicum 框架（options CAPABILITIES 和 options CAPABILITY_MODE）；Pawel Jakub Dawidek 在 FreeBSD 基金会与 Google 开源计划办公室联合资助下（2013 年 4 月公告）完成了 Capsicum 从研究原型到产品级代码的工程化，开发了 **casperd(8)** 服务守护进程和 **libcapsicum(3)**/**libcasper(3)** 库；FreeBSD 基本系统中首批 Capsicum 化工具包括 **tcpdump(1)**、**dhclient(8)**、**kdump(1)**、**killall(1)**、**timeout(1)**、**dd(1)** 等；Capsicum 的核心创新是对象能力模型——进程通过 **cap_enter(2)** 进入能力模式后丧失所有全局命名空间访问权，仅能通过已持有的能力文件描述符访问资源
- CHERI（Capability Hardware Enhanced RISC Instructions）是剑桥大学与 SRI International 联合开发的硬件能力架构，为 Capsicum 类能力模型提供硬件级强制保护；CheriBSD 是基于 FreeBSD 的 CHERI 参考实现，扩展了 Capsicum 能力模型至硬件层面，通过能力指针（fat pointers）替代传统整数指针，在硬件层面强制执行内存安全和控制流完整性；CHERI-MIPS、CHERI-RISC-V、Arm Morello（2021 年 Arm 发布的 CHERI 原型 SoC）是 CHERI 架构的主要硬件实现；FreeBSD 基金会 2024 年资助了 Capsicum+bhyve 安全审计，由 Shawn Webb 与 Mariusz Zaborski 执行，部分审计结果为 CHERI 硬件能力与软件能力模型结合提供了实践依据

## 史观

- 总纲第 1 条——一切真历史都是古代史：传统 UNIX DAC 是 FreeBSD 安全模型的 “源头时刻”——1970 年代初在 PDP-7/PDP-11 上设计的简单权限模型在五十多年后仍是 FreeBSD（以及所有类 UNIX 系统）安全的基础；这一模型的简单性（9 个基本权限位 +3 个特殊位）是其持久生命力的来源，但其 “root 万能” 的设计假设在网络时代成为严重安全缺陷；FreeBSD 后（原“项目统摄史观”非基线名目，基线第 1 条为“一切真历史都是古代史”，按权威表改挂——批次 C362 问题 2）
- 总纲第 1 条——一切真历史都是古代史：jail 的诞生是 FreeBSD 安全演进的第一个 “源头时刻”——Kamp 在 2000 年选择在单体内核中以 “强制隔离 + 资源限制” 方式实现进程监禁，而非采用当时新兴的虚拟化技术（如 VMware、Xen）或微内核方案，这一工程决策奠定了 FreeBSD 此后二十余年容器化技术的基础；jail 比 Solaris Zones（2004）、Linux VS（原“项目统摄史观”非基线名目，基线第 1 条为“一切真历史都是古代史”，按权威表改挂——批次 C362 问题 2）
- 专题语（不设条号）——安全标准与认证：MAC 框架是 FreeBSD 对 TCSEC（Orange Book，橘皮书）B 级安全要求的回应——橘皮书 B1 级要求强制访问控制（MAC）支持，MAC 框架的设计直接参考了 TCSEC B1/B2 级和 Common Criteria 的要求；但 FreeBSD 从未以获得 TCSEC/CC 认证为目标——框架提供机制（mechanism）〔待核：原文截断，后文待回源〕（原“总纲第 21 条——密码学”与基线第 21 条“革命与改革是历史方法论的分歧”不符，按 R2140 先例改不设条号专题语——批次 C362 问题 2）
- 专题语（不设条号）——安全审计与标准复用：安全审计是高安全等级操作系统（TCSEC C2 及以上、Common Criteria）的形式化要求——但与 MAC 框架类似，FreeBSD 提供审计机制但不追求认证；OpenBSM 的选择体现了 FreeBSD 对“复用成熟标准化技术”的偏好——BSM 审计格式自 1990 年代 Solaris C2 安全认证以来即为审计领域的事实标准，采用该格式便于与现有审计（原“总纲第 3 条——形式主义膨胀”与基线第 3 条“不存在进步，只有权力再分配”不符，按 R2140 先例改不设条号专题语——批次 C362 问题 2）

## 辨析

- “FreeBSD 抛弃了传统 UNIX 权限模型” 说法错误——传统 DAC 仍是 FreeBSD 默认且最基础的安全机制，MAC、Capsicum、jail 等是叠加在 DAC 之上的可选安全层，不是替代；“setuid 本身是安全漏洞” 说法不准确——setuid 是一种机制，其安全性取决于 setuid 程序的实现质量；历史上 BSD 对 setuid 程序的安全审计比其他 UNIX 变体更
- 关于 “jail 是 chroot 的安全增强版” 说法需精确区分：**chroot(2)** 仅改变文件系统根目录，不限制进程系统调用访问，root 用户可轻易逃逸；**jail(8)** 从内核层面增加多层隔离，但 FreeBSD 4.x 时代的原始 jail 仍非完美——2000-2005 年间发现多个 jail 逃逸路径；〔待核：原文截断，后文待回源〕
- “TrustedBSD MAC 框架是 FreeBSD 版的 SELinux” 说法过于简化——SELinux 最初是 NSA 为 Linux 设计的 FLASK/TE 安全架构，移植到 FreeBSD 时作为 MAC 框架的一个策略模块（mac_flask），而非 MAC 框架本身；MAC 框架比 LSM（Linux Security Modules）更早起步（2000 年 vs LSM 200
- “FreeBSD audit 是 Sun 代码的直接移植”说法不完全准确——OpenBSM 是 BSM API 和审计格式的独立开源重新实现（clean-room reimplementation），并非从 Solaris 源码直接移植；这是为了避免 CDDL（Sun CDDL 许可证）与 BSD 许可证的兼容性问题；OpenBSM 与 Solaris BSM 在 API 和日志格式层面兼容，但实

## 文献

- Ritchie D M, Thompson K. The UNIX Time-Sharing System [J]. Communications of the ACM, 1974, 17(7): 365-375; Bach M J. The Design of the UNIX Operating System [M]. Prentice-Hall, 1986. ISBN 978-0-13-201799-2; FreeBSD Project. **chmod(1)**, **chown(8)**, **setuid(2)** Manual Pages. ［B］
    FreeBSD 社区论
- Kamp P H, Watson R N M. Jails: Confining the Omnipotent Root [C]. Proceedings of the 2nd International SANE Conference, 2000; FreeBSD Project. FreeBSD 4.0-RELEASE Release Notes (2000-03-14). freebsd.org; FreeBSD Project. **jail(8)**, **jail(2)** Manual Pages; McKusick M K, Neville-Neil G V, Watson R
- Watson R N M. New Approaches to Operating System Security Extensibility [D]. University of Cambridge Computer Laboratory, 2012 (UCAM-CL-TR-818); FreeBSD Project. FreeBSD 5.0-RELEASE Release Notes & Early Adopter's Guide (2003-01-19). freebsd.org; TrustedBSD Project. trustedbsd.org; FreeBSD Project.
- TrustedBSD Project. OpenBSM. trustedbsd.org/openbsm/; FreeBSD Project. **audit(4)**, **auditd(8)**, **auditreduce(8)**, **praudit(8)**, **openbsm(3)** Manual Pages; FreeBSD Project. FreeBSD 6.2-RELEASE Release Notes (2007-01-15). freebsd.org; Watson R N M et al. OpenBSM: Open Source Implementation o

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP194、BSD Now EP88、YouTube EPE04LxKiu79I（共 3 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- FreeBSD 2017 年第一季度状态报告记录 core team、基金会、ports（接近三万端口）、release engineering（11.1 排期）等团队动态，基金会赞助 168 个提交并资助多个项目。（BSD Now EP194，[98.3-164.34]，L2）
- Colin Percival 提出一种介于 Patreon 与 Bugzilla 之间的开源维护资助模型，主张以持续收入支持软件维护而非一次性赏金，从而缓解开源软件维护不足的问题。（BSD Now EP194，[878.98-1386.52]，L2）
- Chris Siebenmann 追溯 FreeBSD 目录组继承行为至 4.1cBSD 引入 mkdir 系统调用与多组进程的时期，指出新对象继承父目录组是传统 BSD 行为而非 FreeBSD 的新发明。（BSD Now EP194，[2332.28-2964.74]，L2）
- OpenBSD 变更集移除 SSHv1 协议代码，从 FreeBSD 移植 witness 锁顺序校验工具，并引入 BearSSL 常数时间 AES 实现。（BSD Now EP194，[1925.44-2328.28]，L2）
- Ed Schouten 在分布式存储服务实验中尝试用 Capsicum 加固代码时发现：过早调用 cap_enter 后，加密库首次使用时会因沙箱限制打开 /dev/urandom 失败，从而“回退到弱熵”（2098.10-2114.58），暴露出 Capsicum 把纯能力计算叠加在 Unix 之上时，依赖全局命名空间的第三方库会产生隐蔽缺陷。他由此判断需要一个纯能力运行时环境，并于 2014 年 9 月前后开始全职开发 CloudABI。（BSD Now EP88，[2042.37-2159.94]，L1）
- CloudABI 被设计为一个“虚构操作系统”：Ed 向 SCO 的继任组织 The UXSG 注册了专属 ELF OSABI 编号 17，使同一二进制无需重编译即可在 FreeBSD、NetBSD 及开发中的 Linux 上运行；接口仅保留约 60 个系统调用，CloudLibc 刻意不提供 open() 等依赖全局命名空间的函数，迫使代码在编译期暴露能力不兼容问题；NetBSD 移植启动两周内 650 项单元测试约 95% 通过。（BSD Now EP88，[2810.72-2846.80]，L1）
- 不可变与只可追加文件标志可上溯至 1980 年代 CSRG 的真实安全困境：当时具有登录权限的协作者凭证外流、木马式代码混入代码库，促使开发组将 setuid-root 二进制标记为不可变、将日志文件标记为只可追加；据 McKusick 回忆，攻入者既无法替换关键程序，也无法抹去记录其操作与来源的日志，多数人就此放弃并不再返回，他还追述了循线索追踪一名荷兰入侵者至其住所、由荷兰合作者上门探访后入侵骤然停止的轶事。（YouTube EPE04LxKiu79I，[786.67-941.12]，L1）[订正：原"木马代码险些混入代码库"→"木马式代码混入代码库"（转写为 sometimes they were like even committing stuff into the repository…because they were more or less Trojan horses，系既成混入而非未遂），内容复核]
- jails 为一组进程提供带独立根环境与独立 IP 的受限执行世界：本质上是不可逃逸的 chroot，每个 jail 获得自己的虚拟网络栈与成对虚拟接口，从内部视角自认为独占整机；jail 内 root 可管理本 jail 的进程、文件与端口绑定，却无法看见或向 jail 外进程发信号、无法变更内核变量、无法挂卸文件系统、无法关闭物理网卡或重启系统；随着 ZFS 委派与虚拟网络栈的引入，jail 可行事项持续扩充，其资源占用远低于完整虚拟机，单台服务器可承载数以百计乃至千计的实例。（YouTube EPE04LxKiu79I，[1259.79-1550.19]，L1）[订正："其资源占用远低于完整虚拟机，单台服务器可承载数以百计乃至千计的实例"不在所引区间内，该述出自演讲开头 jails 引入段 [431.8-510.1]（转写为 the footprint…the amount of memory they consume…is far far less than a full-on virtual machine…you're not going to run hundreds or thousands of full-on virtual machines on a single box whereas you can do that with jails），内容复核]
- 随机数体系由 Mark Murray 在 FreeBSD 5.3（2004 年）引入的 /dev/random 奠定：因中断时序、键盘节奏等熵源采集缓慢且总量稀少，系统以真实熵为种子驱动 Yarrow 密码学伪随机数发生器持续输出，并在新熵到达时重置密钥；Yarrow 由熵采集框架、熵累加器、重置密钥机制与生成机制四部分组成，刻意复用经公开文献充分检验的密码学原语而非自行设计；硬件熵源历经 VIA 专用芯片直通输出（早期嵌入式 CPU 跑 Yarrow 需占约两成算力）、Intel RdRand 直通（FreeBSD 9.2 起）到维基解密等事件后改为与其它熵源一并经 Yarrow 混合（FreeBSD 11 引入并回移植至 10.0 及以后）且可被管理员关闭的演进；McKusick 并指出 Fortuna 将以自动化的熵源估计取代 Yarrow 的固定算法，而开机与装机时最需要强随机数却熵源最少的矛盾在其看来仍无良解。　[存疑脚注] Intel RdRand 是否实际被掺假设施并无公开确证，演讲所述属防御性信任决策；Fortuna 替换在演讲时点仍是讨论中的方案而非树内现实。（YouTube EPE04LxKiu79I，[1554.43-2381.76]，L1）[订正：原"维基解密与斯诺登事件"→"维基解密等事件"（转写仅作 all of this stuff coming out with Wikileaks and so on，未提斯诺登），内容复核]
- 访问控制列表的标准史在当事人口中是一部标准政治史：POSIX 1003.1e 草案完成约九成时，委员会内反对者刻意拖延六个月令其越过十八个月的制定期限而死亡，各厂商只得自行补齐剩余一成，造成互不兼容的 ACL 实现，Windows 更另立一套；ACL 早在 1990 年代前中期即已存在，却因各系统实现各异而长期无人使用；此后厂商群体补完 POSIX 草案，另一路与 Windows 兼容的语义进入 NFSv4 规范；FreeBSD 在 UFS 上以挂载选项择一启用，两种语义共用同一套 getfacl 与 setfacl 工具，McKusick 建议新部署采用可跨 UFS、ZFS 与 NFS 且与 Windows 互通的 NFSv4 语义。（YouTube EPE04LxKiu79I，[2677.83-2905.76]，L1）
- 审计以问责与入侵检测为目标，围绕 OpenBSM 建立记录体系，须能回答谁在何时对谁做了什么；McKusick 以美国零售商 Target 数据泄露后数周乃至数月才被发觉、四千万客户信息外流六周的事故说明无人查看的审计日志形同虚设，而 FreeBSD 每夜对全系统 setuid 程序清单做差分、只报告二十四小时内新增或变动条目的做法，被视为让报告短到有人真会去看的实践范例；auditd 守护进程负责筛收与分发审计记录，可应对以填满磁盘来压制审计的攻击手法，记录详尽程度被比作强化版 ktrace，数据亦可外送异地保存；他并透露 FreeBSD 基础设施在约一年半前遭入侵后全面重建，二十年未更新的组件被替换。（YouTube EPE04LxKiu79I，[3413.23-3868.19]，L1）
- capsicum 被演讲者称为 FreeBSD 最新加入的安全机制，由 Robert Watson 与剑桥大学计算机实验室团队设计，大量实现工作出自此前将 ZFS 移植入 FreeBSD 的开发者 pav（Pawel Jakub Dawidek）；其思路是把不受信任的大型库从特权程序中拆出、置于能力模式的子进程中运行，仅凭主进程授予的文件描述符与能力行事——cap_enter 之后的进程如入不可逆的 chroot，无法打开绝对路径、无法访问全局名字空间、无法外联网络或落盘藏匿数据，描述符权利可细分至读、写、定位、监听等单项；名字服务器与 tcpdump 等组件已被沙箱化或在推进中，将大库整体置入能力模块只需付出边界穿越的小代价，即可对未经审计的第三方代码获得实质信心；答问中 McKusick 强调 capsicum 能力与 root 特权列表虽形似而目标迥异：前者隔离不可信组件，后者把 root 权限更精细地授予可信主体。（YouTube EPE04LxKiu79I，[3871.39-4365.60]，L1）

**史料**：

- FreeBSD Quarterly Status Report（2017 年第一季度，官网发布）（BSD Now EP194，[67.52-222.56]，L1）
- Colin Percival 于 daemonology.net 发表的开源软件维护方案博客原文（BSD Now EP194，[872.66-1467.2]，L1）
- Chris Siebenmann（University of Toronto）关于 BSD 目录组继承语义的考据博客（BSD Now EP194，[2332.28-2964.74]，L1）
- OpenBSD changes of note 621（tedu 发布的变更综述）（BSD Now EP194，[1925.44-2332.28]，L1）
- 本期涉及的一手史料包括：Ed Schouten 口述访谈本身（2015 年 5 月 6 日录制，其自述此为首次公开谈论 CloudABI）；2007 年末 FreeBSD 邮件列表流传的 SMP 安全待办清单（含 Robert Watson 等人推动、始终无人认领的 TTY 层条目）；Colin Percival 发至 Tarsnap 邮件列表的 2015 年 3-4 月性能问题事后分析；FreeBSD 基金会博客 from the trenches 系列中 Glenn Barber 的笔记本 ZFS 与 GELI 加密布局自述；FreeBSD 2015 年第二季度状态报告征稿公告；OpenBSD 5.7 发布公告与变更日志。（BSD Now EP88，[4249.66-4305.46]，L3）

**史观**：

- 总纲10 动手者创造历史：状态报告显示基金会资助与普通提交者的日常维护共同推进系统细节，历史由大量默默动手者累积而成。（BSD Now EP194，[98.3-164.34]，L2）
- 总纲13 法律与道德是利益分配：开源维护资助之争的实质是贡献者劳动如何获得回报的利益分配问题，而非单纯的技术或道德问题。（BSD Now EP194，[907.04-1249.4]，L2）
- 总纲5 没有必然性，只有偶然性：BSD 目录组继承语义是 4.1cBSD 多组进程引入时的偶然工程选择，随后沉淀为传统，并非预先设计的必然。（BSD Now EP194，[2486.68-2686.36]，L2）
- 总纲10 动手者创造历史：Ed Schouten 的入坑路径由一连串偶然咬合：13 岁安装 SUSE Linux 因 ISDN 调制解调器与 Voodoo 显卡驱动失败而厌恶 Linux，大学为蹭免费 Wi-Fi 加入 Unix 用户组，2007 年末在 FreeBSD 邮件列表的 SMP 待办清单上认领了表中唯一从未被更新的条目——TTY 层，借学士论文在 Snow 公司资助下完成并上游化，随后获资助赴 BSDCan（1759.64-1987.02）。核心开发者不是被制度培养出来的，而是动手者与无人认领的代码相遇的产物。（BSD Now EP88，[1759.64-1987.02]，L1）
- 总纲3 不存在进步，只有权力再分配：OpenBSD 5.7 发布段呈现的删除并非中性的工程进步：可加载内核模块、PROCFS、Sendmail、SSLv3 与 bind、nginx 相继移出基本系统，主持人的解释是代码被挪出内核做成模块本就因为用的人不多，“那干脆整个扔掉”（729.72-738.12）。代码的存废由维护者对使用与审美的决断而定，系统形态是权力行使的结果，而非技术必然性的展开。（BSD Now EP88，[664.30-738.12]，L2）
- 总纲8 本体论上各方平等：Tor 中继操作系统多样性倡议把 FreeBSD、NetBSD、OpenBSD、DragonFly BSD 并列为对等承载平台，其引文称“自然界中的单一栽培是危险的，因为脆弱性为整个谱系共有；多样性意味着单一漏洞不太可能伤害整个生态系统”（1016.74-1026.42），并以 Verisign 在 Linux、Solaris、BSD 三系间分摊 .com 与 .net 基础设施为旁证。四大分支在本体论层面被平等对待，安全被重构为生态多样性问题而非单一系统的优越性问题。（BSD Now EP88，[943.66-1045.46]，L2）
- 总纲3 不存在进步，只有权力再分配：从全有或全无的超级用户到可分配的权限束，构成 McKusick 叙述 FreeBSD 权限机制演进的内在逻辑：开发组遍历内核找出近二百处超级用户检查，将其转化为 priv_check 特权点并逐一辨析语义，每项特权兼具允许与否、可否继承、可否即时开关三种属性——不可继承可令栈溢出获得的 shell 失去特权，开关式生效可避免误用；强制访问控制框架则允许以标签与策略模块实施系统级信息流控制，其原型由美国国防部资助、脱胎于橙皮书与红皮书的多级安全想象，而商业用户真正在意的是完整性而非机密等级，故可构建取向不同的策略模块；安全史在此呈现为权限的再分配而非单向的功能进步。（YouTube EPE04LxKiu79I，[2923.20-3413.23]，L1）

**辨析**：

- [存疑脚注] Colin Percival 的开源资助方案当时仅为其个人提案，尚未落地实施，能否被社区采纳与商业化可行仍待验证。　[存疑脚注] 该方案属单一来源的个人设想，未形成实施记录。（BSD Now EP194，[1367.52-1440.28]，L4）
- 听众来信引发的 jail 管理讨论揭示生态碎片化：官方手册仍只记录 10.x 已弃用、计划 11.x 移除的 rc.d 风格，jail.conf 采用难以解析的自创格式，easyjail 与 iocage 等框架各自为政，主持人以乐高积木作比——“我们各自拼出略不相同的飞船”（5291.44-5296.68）。这是理解容器化前夜 FreeBSD 治理困境的典型切口；但 rc.d 方式将于 11.x 移除仅系来信者与主持人的当时预期，属待核断言。　[存疑脚注] jail.conf 格式批评与 easyjail、iocage 评价仅出自本期听众来信与主持人对谈（单一对话来源）；rc.d 方式是否于 11.x 移除为当时预期，后续未如期发生，须以 FreeBSD src 与 release notes 核实。（BSD Now EP88，[5139.64-5306.40]，L2）
- DragonFly BSD 抢先完成 Intel Broadwell 图形驱动移植（据称基于 Linux 3.14 drm 更新），一度领先 FreeBSD（当时目标 3.8）与 OpenBSD（止步 Haswell）；主持人转述贡献者名为 Francois Tegjou，并半开玩笑地呼吁 FreeBSD 接受来自 DragonFly 的补丁。该案例显示各 BSD 图形栈围绕上游 Linux drm 形成的非零和追赶关系：分支排名随时翻转，移植源共享削弱了分支间的技术鸿沟。　[存疑脚注] 转写将贡献者名失真记作 Francois Tegjou，据上下文推断为 DragonFly 图形驱动开发者 François Tigeot；所涉 drm 版本数字亦经转写噪声，须以 DragonFly 提交记录核实。（BSD Now EP88，[4099.58-4166.40]，L2）[订正：原 贡献者名失真记作 Francois Toujour，2026-09-30 SenseAudio 重转核对]
- 该机制的强制力由系统安全级别保障：多用户模式下唯一能把级别从高调低的只有 init 进程，级别为一时不可变标志真正无法解除，同时禁止写入内核内存与已挂载磁盘的原始设备；但 McKusick 坦承其结构性缺陷在于系统启动时运行于单用户态、启动脚本可预先解除标志，攻击者只需篡改启动脚本并诱发内核恐慌重启即可绕过全部防护，而补救须锁定启动链上的全部脚本、目录、二进制与配置文件，将使系统难以使用——securelevels 因此被后续机制取代，是安全机制因偶然缺口而兴废的典型个案。（YouTube EPE04LxKiu79I，[1002.56-1259.79]，L1）[订正：原 [1142.67-1259.79]→[1002.56-1259.79]，init 调级、级别一不可变与禁写内核内存/已挂载盘原始设备诸句出自 1002.56-1142.67（转写为 the only binary…allowed to change this level from a higher to a lower level is process one…prevented from writing to Dev km or Dev M…open the raw disc），内容复核]

**文献**：

- [BSD Now EP194] Pennington J. BSD Now: 194: Daemonic plans[EB/OL]. (2017-05-17)[2026-08-15]. <https://www.bsdnow.tv/194>.
- [BSD Now EP88] Pennington J. BSD Now: 88: Below the Clouds[EB/OL]. (2015-05-06)[2026-08-15]. <https://www.bsdnow.tv/88>.
- [YouTube EPE04LxKiu79I] YouTube. YouTube: Dr. Marshall Kirk McKusick, An Overview of Security in the FreeBSD Kernel[EB/OL]. ()[2026-08-15]. <https://www.youtube.com/watch?v=E04LxKiu79I>.

<!-- /PODCAST_REVIEW -->

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

