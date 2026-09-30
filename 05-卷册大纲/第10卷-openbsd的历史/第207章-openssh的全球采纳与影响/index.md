---
chapter: 第 207 章
id: CH207
volume: 第10卷-openbsd的历史
---

# 第 207 章 openssh的全球采纳与影响

## 要点

- OpenSSH 时间跨度（1999-10-27 至 2026-08-20），高峰期 2001年(1266次) 对应早期快速迭代
- 微软因在 Windows 中集成 OpenSSH 而向 OpenBSD 基金会捐赠并成为金牌赞助商；Oracle Solaris 以原生 OpenSSH 取代 Sun SSH，并自 OpenBSD 借入 getentropy、将 arc4random 并入 libc
- OpenSSH 8.1 修复 XMSS 私钥解析整数溢出，RSA 证书签名默认改用 SHA2-512

## 史料

- [DB:code_repos:openssh.duckdb] OpenSSH 时间跨度（1999-10-27 至 2026-08-20），高峰期 2001年(1266次) 对应早期快速迭代
- OpenSSH Project. OpenSSH History — The Birth of OpenSSH [EB/OL]. (1999)[2026-07-24]. <https://www.openssh.com/history.html>（Provos 赴加拿大移除加密与 GPL 组件、libgmp 移除时序等一手自述）

## 史观

- 总纲 12“科学是形式主义”：OpenSSH 全球采纳率“超过 90%”的说法缺口径与出处，仅是意见而非知识——把统计数字当作事物本身，正是形式主义化的简化。
- 章级史观：OpenSSH 的全球采纳呈现价值创造与利益分配的错位（总纲 13“法律与道德是利益分配”）：其代码内置于 Windows、Solaris、Cisco、AIX、OS X 等平台，使用者以百万计，却无一分收入回流项目——采纳的广度与项目经济基础的悬空并存，构成“OpenSSH 悖论”（详见 PODCAST_REVIEW 史观条）。

## 辨析

- 考据过程留痕——【查证来源】项目统摄史观审视的史料基础经以下核验：项目史观总纲第 15 条（“文化即形式主义”）、第 19 条（“解释学循环是历史认识的根本条件”）、第 21 条（“革命与改革是历史方法论的分歧”）原文经核验（原引 c:\Users\ykla\Documents\LibreBSD\原材料\哲学\项目统摄史观\第 25 章.md，2026-07-23 Read 工具一手核验；该库外路径已断链，2026-09-13 改引库内权威原文 **02-sacred源材料/dagang.md** 复核，三条总纲均与 25 条总纲原文一致）。
- 考据过程留痕——【查证来源】三类批评的具体诉求经以下一手史料核验：Provos 赴加拿大移除加密与 GPL 组件，经 OpenSSH 官方历史页面（<https://www.openssh.com/history.html>，2026-07-24 WebFetch 一手核验）确认原文“Niels Provos (GERMANY but living in USA) quickly removed the remaining cryptographic and GPL'd components by doing road trips to Canada”——三类批评所涉的移除事实与地理约束均获原文支持。（2026-09-13 补全截断句留痕）
- 考据过程留痕——【查证来源】OpenBSD 阵营反批评的三点论据经以下一手史料核验：第一点（Provos 移除 libgmp 是修复既有 GPL 违规），经 OpenSSH 官方历史页面（<https://www.openssh.com/history.html>，2026-07-24 WebFetch 一手核验）确认原文“Rapidly after Tatu's 1.2.12 release, newer versions bore successively more restrictive licenses.”——彼时 libgmp 仍随分发捆绑，反批评的版本前提成立。（2026-09-13 补全截断句留痕）
- 考据过程留痕——【查证来源】再回应三点的评估经以下一手史料核验：第一点（libgmp 移除时机由发布截止日期驱动），经 OpenSSH 官方历史页面（<https://www.openssh.com/history.html>，2026-07-24 WebFetch 一手核验）确认原文“OpenBSD project members became aware of Björn's work less than two months before the OpenBSD 2.6 release.”——移除 libgmp 的时机约束由此获原文支持。（2026-09-13 补全截断句留痕）
- 考据过程留痕——【查证来源】合图“成功”判定的各项事实经以下一手史料核验：Provos 移除 libgmp 的长期正确性，经 OpenSSH 官方历史页面（<https://www.openssh.com/history.html>，2026-07-24 WebFetch 一手核验）确认原文“that effectively made SSH a GPL violation”——移除 libgmp 系对既有 GPL 违规的修复，此判定的史料依据至此完整。（2026-09-13 补全截断句留痕）

## 文献

- OpenSSH Project. OpenSSH History — The Birth of OpenSSH [EB/OL]. (1999)[2026-07-24]. <https://www.openssh.com/history.html>.

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP322、BSD Now EP97、BSDTalk EP27（共 3 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Warner Losh 通过 Bell Labs 1968 年影片《The Incredible Machine》比对 DEC 目录与现场服务清单，论证片中 PDP-7 即 Ken Thompson 所用序列号 34：具备 340 显示器与 444B 纸带机、无 DECtape。（BSD Now EP322，[407.26-941.24]，L2）
- 影片中机器生成音乐、与视觉声学部门来源吻合，配置、日期、无磁带三条证据链共同支持其“Unix 之母机”身份，但 Warner 仍以弱证据与强证据区分，未作绝对断言。（BSD Now EP322，[936.56-977.82]，L2）
- OpenBSD 6.6 为第 47 个发布，unveil 已用于 77 个用户态程序，移除 bridge 输出快速路径内核锁，加入 Intel MDS 缓解与 malloc 隐蔽/清零 API，并更新 VMM 以透传 MSR 缓解位。（BSD Now EP322，[1059.96-1598.48]，L2）
- OpenSSH 8.1 修复 XMSS 私钥解析整数溢出，并在 RAM 中加密静态私钥以防 Spectre/Meltdown 类侧信道；RSA 证书签名默认改用 SHA2-512，不兼容 7.2 之前的客户端。（BSD Now EP322，[2107.02-2265.46]，L2）
- GhostBSD 澄清其基于 TrueOS/FreeBSD 12 stable，官方桌面为 MATE，其他桌面以社区版本维护，项目提供构建与托管支持并欢迎贡献。（BSD Now EP322，[1778.00-1862.98]，L2）
- SmallWall 的诞生系于一次突然的项目终结：2015 年 2 月 monoWall 作者 Manuel Kasper 以一封邮件宣布项目停止开发，长期依赖该精简防火墙的咨询者与用户在震惊中几乎同时注册域名、搭建基础设施，Lee Sharp 以连续的 beta 发布承接社区，并因 Slashdot 报道获得爆发性下载，项目由此复活。　[存疑脚注] 转写将发件人误作 a manual，依 monoWall 项目史推断为作者 Manuel Kasper（BSD Now EP97，[1031.14-1112.33]，L1）
- SmallWall 的产品立场是刻意求小：Lee Sharp 明言遵循 “do one thing and do it well”（1149.05-1153.09）的旧 Unix 哲学，拒绝大而全防火墙，专注低功耗嵌入式与虚拟化场景（早期即加入 VirtIO 驱动以适配 KVM 等开源虚拟机）；管理面以 Web 界面防呆、把多网段等危险操作刻意变难，配置为可任意编辑的扁平 XML 文件（1514.23-1539.05），固件更新经 RAM disk 中转以保护 CF 卡与 U 盘的写入寿命。（BSD Now EP97，[1144.38-1194.77]，L1）
- Docker 登陆 FreeBSD ports tree 由当期主持人亲自提交 port（其自述移植主体另有其人、自己只补 port 打包），实测 FreeBSD 容器原生运行于 Jail 子系统与 ZFS 之上、近全部子命令可用，在 -CURRENT 的 64 位 Linuxulator 上亦可尝试运行 Linux 容器；遗留缺口包括 resolv.conf 未自动复制与依赖 PF 做 NAT 转发的临时胶水，期望日后由 port 内部接管。（BSD Now EP97，[3383.60-3518.65]，L1）[订正：原 [3375.71-3518.65]，2026-09-30 SenseAudio 重转核对]
- 2015 年的两个外部靠拢信号由主持人转述：微软因决定在 Windows 中集成 OpenSSH 而向 OpenBSD 基金会捐赠、成为金牌赞助商，并在 OpenSSH 邮件列表发出合同工作邀约、承诺变更酌情上游回馈；同期 Oracle 的 Solaris 计划以原生 OpenSSH 取代 Sun SSH 分叉，并自 OpenBSD 借入 getentropy、将 arc4random 并入 libc（2545.47-2576.31）。（BSD Now EP97，[3630.00-3658.04]，L2）[订正：原 [3615.63-3658.04]，2026-09-30 SenseAudio 重转核对]
- 工作范围与个人部署：Marco Peereboom 在 OpenBSD 主要从事存储与 SCSI 中间层工作；3.9 周期中被岔去实现 IPMI（智能平台管理接口）——新型与高端服务器内置的传感器协议，跟踪风扇、温度、电压等状态并把信息呈现给用户空间，可配合 sensors 命令监控告警；i386 与 AMD64 平台均适用。其个人机器多台运行 OpenBSD：一台旧的工作站（转写含混，疑为 Alpha 或旧 SPARC64）、一台 i386 web 服务器（朋友网站亦托管其上）、一台 HPPA 防火墙（将升级 3.9 并使用 PF 新特性）。（BSDTalk EP27，[90.24-208.04]，L1）
- 资金困境与 hackathon 机制：项目已亏损运行一段时间；开销主要在基础设施——网络费用昂贵、电费极高，因为项目坚持所有平台全部本地原生构建（Zaurus 快照即在 Zaurus 上构建），地下室机器全天候运转；已收捐赠获致谢，同时呼吁企业级赞助——盼有公司愿意为 hackathon 买单。年度 hackathon 为开发者大聚会：多数人飞赴 Calgary 写代码、规划战略，邮件往返缓慢的事项在面谈中大大加速；其副作用是总能发现需要多人不同技能协作才能定位的重大 bug，产出大量好代码与想法进入下个发布；面对面建立信任，而这种开发模式极依赖信任。另有定向 hackathon：如前一年威尼斯的 ports hackathon，约 10 名专家使 ports 系统大幅进步；ports 与包工具近期升级体验显著改善且质量可直接测得。（BSDTalk EP27，[218.08-430.34]，L1）
- 开发哲学与安全记录：OpenBSD 开发模式不讲废话——永远做对的事，不适合操作系统的特性就不会发生，因此对社区有时显得生硬；对许可证绝不妥协并引以为豪，纵然承受社区与其他方面的压力，流程中保持理性，不合格的代码不会进入发布、甚至直接移出树——想在此协作就得守此规则。对保持默认安装无远程漏洞的纪录表示自信——正是这一点当初吸引他入坑（厌倦了隔三差五担心被入侵的日子），但他不能替全世界打包票。（BSDTalk EP27，[436.30-552.92]，L1）
- 升级流程与包工具评价：当事人认为 OpenBSD 的升级过程比 apt-get 更透明——他试装 Ubuntu 后觉得 apt-get 要求用户预先懂得太多；承认 OpenBSD 安装器对新用户略显生畏，但这只是习惯问题：图形安装器问的是同样的问题，打字与点击之别而已；升级复用与安装相同的安装器、识别现有系统、连按回车即开始，最难的一步是敲出二进制路径；ports 侧的工具已做到完全透明——一条命令即可升级全部 ports 并解析依赖；ports 升级与替换功能为 3.8 与 3.9 之间引入、随 3.9 发布；他本人不做 ports，靠定时任务自动升级。（BSDTalk EP27，[552.92-700.92]，L1）
- 在研项目：正与 Jordan Hargrave 合作重写 ACPI——工程巨大、代码要写要调、BIOS 环境充满敌意、进展缓慢；另在升级磁盘控制器驱动以支持即将到来的 SAS 技术；并循 Theo de Raadt 的指引为 bioctl 增加更多 RAID 控制器支持——bioctl 为 3.8 引入的通用 RAID 管理工具，理念是各家 RAID 控制器虽差异巨大、基本视角下功能相同，bioctl 以简单方式确保 RAID 栈完好，提供换盘与重建工具且全程无需重启——磁盘故障后不重启即可恢复；此工具面向硬件 RAID 而非软件 RAID，二者将来或合并但为时尚远。桌面方面用 Ion 或 Ratpoison 平铺窗口管理器，在高分辨率宽屏上并排三个全尺寸窗口，重度使用 screen 切换文本终端，编辑器只用 vi——唯一确定永远在场的编辑器。（BSDTalk EP27，[700.92-925.88]，L1）

**史料**：

- Warner Losh 博客《Hunting Down Ken's PDP-7》及 Bell Labs《The Incredible Machine》1968 年影片。（BSD Now EP322，[400.18-402.92]，L2）
- DEC PDP-7 销售目录与 Bitsavers 现场服务清单（序列号 34/149 的选件记录）。（BSD Now EP322，[685.26-707.24]，L2）
- OpenBSD 6.6 发布页与升级说明（unveil、MDS 缓解、预编译包数量等）。（BSD Now EP322，[1063.56-1068.82]，L2）
- OpenSSH 8.1 发布公告，含 Adam Zabrocki 报告的 XMSS 私钥解析漏洞。（BSD Now EP322，[2125.36-2172.60]，L2）
- 该期提及的一手史料包括：BSDCan 2015 演讲视频（Stephen Bourne 关于 UNIX 早期岁月与 shell 设计的主旨报告、Nigel Williams 之 FreeBSD 多路径 TCP、John Criswell 之安全虚拟架构、John-Mark Gurney 之 AES-ICM/GCM 加入 open crypto、会议闭幕实录）；EuroBSDCon 2015 瑞典会议初步议程与四场教程（含 Kirk McKusick 的 BSD 快速文件系统简史与 FreeBSD 导论、mandoc 教程、Peter Hansteen 的 PF 教程）；2015 冲绳开源会议之 NetBSD 展示；monoWall 停更邮件与 SmallWall 文件系统 tarball；Oracle 开发者关于 Sun SSH 的系列博文。　[存疑脚注] 人名与专名多依音近转写辨识（如 Steve born、Ted Uninks、Ed Shoutman、Peter Handstein、Poojrear 分别推断为 Stephen Bourne、Ted Unangst、Ed Schouten、Peter Hansteen、poudriere），拼写待与会议议程原件核对（BSD Now EP97，[71.91-122.18]，L2）
- OpenBSD 开发者 Marco Peereboom 一手访谈：存储与 SCSI 中间层工作、IPMI 传感器框架实现、个人多平台部署（工作站、web 服务器、HPPA 防火墙）、项目亏损与基础设施成本结构（网络费用、全平台本地原生构建的电费）、hackathon 年会与威尼斯定向 ports hackathon、no nonsense 开发哲学与许可证不妥协、对 apt-get 与 OpenBSD 升级流程的对比评价、ports 升级替换功能的时间点（3.8-3.9 之间）、ACPI 重写与 Jordan Hargrave 合作、SAS 驱动计划、bioctl 通用 RAID 工具理念、桌面环境（Ion/Ratpoison、screen、vi）、OpenSSH 使用广度与零收入的悖论陈述。（BSDTalk EP27，[35.96-1001.24]，L1）

**史观**：

- 总纲1 一切真历史都是古代史：50 年前的机器被当作文物考据，当下的档案即未来的历史。（BSD Now EP322，[985.90-1007.10]，L2）
- 总纲17 证明世界先于解释和改造世界：先有 PDP-7 实物与影片证据，再谈 Unix 起源解释。（BSD Now EP322，[461.82-466.08]，L2）
- 总纲19 解释学循环是历史认识的根本条件：影片截图与目录照片互为印证，逐项比对构成循环解释。（BSD Now EP322，[558.72-631.14]，L2）
- 总纲22 知识注定过时：SSH 旧客户端与 RSA-SHA1 证书兼容性被新默认淘汰，知识随版本更替失效。（BSD Now EP322，[2236.64-2265.46]，L2）
- 总纲8 本体论上各方平等：OpenBSD 6.6 与 OPNsense、GhostBSD 同屏，各项目如实呈现。（BSD Now EP322，[1608.32-1616.96]，L2）
- 总纲10 动手者创造历史：总纲10 动手者创造历史：Warner Losh 逐帧考证、OpenBSD 开发者逐锁解锁，动手者推动认识与系统演进。（BSD Now EP322，[982.99-1036.46]，L2）
- 总纲10 动手者创造历史：SmallWall 的谱系由动手者而非明星人物书写：Lee Sharp 自述当年受教于 monoWall 周边的实践者——Chris 后执掌 pfSense 与 BSD Perimeter，写文档者独立门户，做网络架构者遍及全球——如今他刻意降低开发门槛、把工具与文档摆出来，请有想法的人跳进来，以日常劳动的传递续写项目，而非依赖英雄叙事。　[存疑脚注] 转写将相关人名误作 Michael Adema、Escozia、Jonathan DeGraves 等，准确拼写待核（BSD Now EP97，[1986.33-2023.69]，L1）
- 总纲5 没有必然性，只有偶然性：项目的存在本身即偶然性的产物：没有那份宣布停更的邮件便没有 SmallWall，Lee Sharp 强调少数人 “had the same idea at the same time”（1078.33-1083.33），复活不是历史必然，而是几个用户在同一周内的应急反应；其早期声势亦系于 Slashdot 曝光这类无法规划的事件。（BSD Now EP97，[1031.14-1090.33]，L1）
- 总纲13 法律与道德是利益分配：OpenSSH 悖论呈现了价值创造与利益分配的错位：OpenSSH 内置于 Cisco 交换机、AIX、OS X 等无处不在的平台，使用者以百万计，却无一分收入回流项目，连自身运转账单都难以支付；企业把公共品内化为基础设施而不承担其维护成本，公共品的存续被迫仰赖个人捐赠与偶发的企业善举——技术上的巨大成功与经济上的悬空并存。（BSDTalk EP27，[945.60-998.24]，L1）

**辨析**：

- PDP-7 影片鉴定为“强烈支持而非确证”，Warner 本人承认对序列号 149 的排除仅属弱证据。　[存疑脚注] 三线证据均非决定性，结论保持开放（BSD Now EP322，[770.24-808.78]，L3）
- GhostBSD 路线为项目方单方声明，TrueOS 后续变动可能使其再调整，不宜作长期定论。　[考据脚注] 上游 TrueOS 路线变动风险未计入（BSD Now EP322，[1802.90-1822.78]，L4）
- 旧基线之辩是本期最有张力的技术判断：SmallWall 坚守 FreeBSD 8.4，主张 “Old is good”（1380.53-1383.13）——基线更久经测试，因 Shellshock 与 Heartbleed 均未波及（无 shell、无受影响特性），但 8.4 安全支持数月内终止，向 FreeBSD 10 迁移牵动大量代码；且历史上 monoWall 曾因 FreeBSD 6 网络性能不济而自 4 直接跳 8——稳定与前沿的取舍并非单向进步，而是按自身负载场景的权衡。（BSD Now EP97，[1374.01-1478.79]，L1）
- 转写讹误提示（该期质量标记为重复检测，经通读主线完整但专名讹误多）：受访者名讹作 Perebum（通行拼写为 Marco Peereboom），bioctl 讹作 BioCuttle，apt-get 讹作 AppGet，OpenSSH 讹作 OpenXSage，ports 讹作 porch，Ratpoison 讹作 Redpoison，Jordan Hargrave 讹作 Jordan Hardraith，SAS 讹作 SaaS，AMD64 讹作 A&B64，mpi 驱动讹作 empty key driver，Calgary 一处转写含混；引用本访谈的专名、地名与人名前须逐一对音核实。[存疑脚注] 专名讹误密集，需系统核对。　[存疑脚注] 人名、工具名与术语讹误密集，引用前需系统对音核实。（BSDTalk EP27，[35.96-1001.24]，L5）

**文献**：

- [BSD Now EP322] Pennington J. BSD Now: 322: Happy Birthday, Unix[EB/OL]. (2019-10-31)[2026-08-15]. <https://www.bsdnow.tv/322>.
- [BSD Now EP97] Pennington J. BSD Now: 97: Big Network, SmallWall[EB/OL]. (2015-07-08)[2026-08-15]. <https://www.bsdnow.tv/97>.
- [BSDTalk EP27] Backman W. BSDTalk: 27: bsdtalk027 - Interview with OpenBSD developer Marco Peereboom[EB/OL]. (2006-03-23)[2026-08-27]. <https://archive.org/details/bsdtalk027>.

<!-- /PODCAST_REVIEW -->
