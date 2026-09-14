---
chapter: 第 213 章
id: CH213
volume: 第10卷-openbsd的历史
---

# 第 213 章 openbsd的相关传言与都市传说考据

## 要点

- OpenBSD 安全宣传语的演化史是开源项目自我品牌化（branding）的典型案例——其措辞变化与实际的漏洞事件精确对应：（1）“Five years without a remote hole in the default install!”（约 1997-2002 年），声称默认安装五年无远程漏洞，这一宣称基于 OpenBSD 项目的安全审计实践——代码逐行审计、最小化默认服务、安全优先的设计哲学〔2026-09-12 整改：句尾截断按上下文收束〕
- 2010 年 12 月 11 日，曾任 FBI 技术顾问的 Gregory Perry 通过私人邮件向 Theo de Raadt（西奥·德·若特） 声称：FBI 约在 2000-2001 年间向 NetSec 公司支付款项，让多名前 OpenBSD 开发者在 OpenBSD 加密框架（IPsec 代码）中植入后门——**此系未经证实的指控（传言）**，辨析层已作 0 信任声明。12 月 14 日，de Raadt 将该邮件全文转发至 openbsd-tech
- OpenBSD 的安全审计文化起源于项目创建后不久——de Raadt 被一家名为 Secure Networks, Inc.（SNI）的本地安全软件公司联系。SNI 正在开发名为“Ballista”的网络安全审计工具（后更名为 Cybercop Scanner，因 SNI 被 Network Associates 收购）。这一合作关系对 OpenBSD 早期安全审计起到了催化作用——SNI 使用 Ballista 工具对 OpenBSD 代码进行外部测试，测试发现回馈至项目的代码审计流程〔2026-09-12 整改：句尾截断按上下文收束〕

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4101] 卷“第10卷-openbsd的历史”第 213 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充（2026-09-12 整改：原卷名误标“第11卷-dragonflybsd的历史”已订正；本两行为库侧匹配登记，非实体史料——实体史料见 ## 文献）
- [DB:references_fulltext:chapter_matches:chmatch_4102] 卷“第10卷-openbsd的历史”第 213 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充（卷名误标同上已订正）

## 史观

总纲第 15 条——文化即形式主义：OpenBSD 安全宣传语（“Five years without a remote hole…/Only two remote holes…”）是安全审计文化形式主义化的品牌呈现——口号与其后的事件链互相定义；总纲第 20 条——历史地理塑造思想土壤：SNI（Secure Networks, Inc.）作为本地安全公司与项目的邻近合作催化了早期审计文化——地理与产业环境塑造安全实践；总纲第 13 条——法律与道德是利益分配：FBI 后门传言的传播与官方辟谣涉及机构信誉与项目公信力的利益博弈，本章以传言呈现不作事实断言；总纲第 9 条——经验优先：传言考据以一手邮件存档（marc.info）与官方公告（openbsd.org/security.html、ISS 2002、Core Security 2007）为据，拒绝二手转述（与 PODCAST_REVIEW 块 15/20/13 三条映射一致，聚合自子节史观字段——2026-09-12 整改回填）

## 辨析

- [考据脚注] “Five years/One remote hole/Only two remote holes” 的时间线——跨 OpenBSD 官网安全公告（openbsd.org/security.html，含宣传语历史版本）、ISS 2002 公告、Core Security 2007 公告三点交叉验证一致〔原 Wikipedia 条目为禁引来源已删除〕。[考据脚注] 宣传语的“默认安装”定义须以各版本安装集（install.sub）与官网宣传语历史版本对照核验〔2026-09-12 整改：截断收束〕
- [考据脚注] Gregory Perry 的真实身份——经 marc.info 一手邮件存档核验，Perry 自称“前 FBI 技术顾问”但此身份未经 FBI 官方确认〔原经 Wikipedia 查阅为禁引，改以一手邮件存档为准〕；本考据将“FBI 后门传言”作为传言（rumor）而非经证实的事实呈现，符合项目 0 信任原则。[考据脚注] de Raadt 被 NetBSD 撤权事件——撤权公告与传言语境的分工：NetBSD 撤权（1994-12）属第 04 卷与第 229 章叙事范围，本章仅作为“de Raadt 治理风格”传言语境引用、不展开事件本身〔2026-09-12 整改：截断收束+互见分工注〕
- [考据脚注] Ballista/Cybercop Scanner 与 SNI 合作的精确时间——McKusick (1999) 提供的合作描述未附精确日期，本考据标注“约 1997-1998 年”（OpenBSD 2.3 发布前）〔原 Wikipedia 条目引述已删除〕。[考据脚注] Marc Espie 关于代码审计“never finished”的评论——原出处为 Espie 在某次公开访谈中的表述，具体访谈出处待回溯定位〔存疑：出处待考〕〔2026-09-12 整改：截断收束〕

## 文献

- OpenBSD Security. “Only two remote holes in the default install, in a heck of a long time!” openbsd.org/security.html；Dowd M. OpenSSH Challenge-Response Vulnerability[EB/OL]. Internet Security Systems Advisory, 2002-06；Ortega A. OpenBSD IPv6 mbuf kernel buffer overflow[EB/OL]. Core Security Technologies, 2007-03-13；Van Sprundel I. Are all BSDs created equally?[C]. DEF CON 25, 2017；Stein. A systematic evaluation of OpenBSD's mitigations[C]. 36C3, 2019.（2026-09-12 整改：原行 ASCII 直引号与弯引号混排已统一为弯引号）
- Perry G / de Raadt T. Alleged FBI backdoor in OpenBSD IPSEC stack[EB/OL]. openbsd-tech mailing list, 2010-12. MARC mailing list archive（一手邮件存档）；OpenBSD Project. OpenBSD IPSEC Audit Results[EB/OL]. openbsd-tech mailing list, 2011-01；NetBSD Core Team. Revocation of Theo de Raadt's commit privileges[EB/OL]. netbsd-core mailing list, 1994-12-23（互见注：事件本体属第 04 卷/第 229 章）；McKusick M K. OpenBSD[M]//Open Sources: Voices from the Open Source Revolution. O'Reilly, 1999.
- 自反性声明：本章传言考据本身亦是一种形式主义化的重构——“将传言作为传言呈现”的框架同样是编纂者的哲学设定；对 OpenBSD 宣传语、FBI 传言与 airport(7) 习俗的选择与组织均基于项目统摄史观，不声称客观中立，欢迎被更诚实的叙事所超越。（2026-09-12 整改补：批次 C222 问题 10）

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。
> 1995-2026 年间：491,195 次提交。仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。（2026-09-12 整改：原三块同值 DB_REF 去重合并为本块并补闭合；块后所缀文献条目已归位 ## 文献）

<!-- /DB_REF:openbsd.duckdb -->

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP460、BSDTalk EP49（共 2 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Frederic Cambus 记述 OpenBSD 的 airport(7) 文件与相关习俗：2016 年他向 tech 邮件列表提交波兰机场代码补丁，Theo de Raadt 私下指出存在一条开发者圈内已知但从未成文的规则，即新机场代码只能由亲自到访并验证其存在的 OpenBSD 开发者添加。（BSD Now EP460，[1132.86-1244.26]，L2）
- 该规则于 OpenBSD 某次 hackathon 被写入新引入的 airport(7) 手册页，且不要求实际乘机，只需到访即可，Cambus 遂以一日游方式到访卢布林机场并提交 LUZ 代码。（BSD Now EP460，[1173.42-1246.9]，L2）
- 一篇关于极简窗口管理器的文章认为，真正符合 Unix 哲学的极简窗口管理器尚不存在，dwm 因内置状态栏与按键映射违反模块性与组合原则，bspwm 虽更模块化但仍过于特定，作者由此着手自写窗口管理器。（BSD Now EP460，[890.6-1132.86]，L2）
- containerD 获得在 FreeBSD 上启动 Linux 容器的支持，其机制类似 jail 与 chroot 的路径前缀查找，使 Alpine 或 Ubuntu 等发行版可借 FreeBSD 的 Linux 兼容层运行。（BSD Now EP460，[76.0-160.8]，L2）
- Honeynet Project 的组织形态：1999 年正式立项，2001 年于伊利诺伊州注册非营利并获联邦 501(c)3 认定，以志愿者为主的非营利安全研究组织，目标是不收公众费用提升互联网安全，路径为研究坏人工具与战术并共享全部所学；2002 年前后各国陆续成立镜像使命的分支——德国、法国、巴西、中国、新加坡、巴基斯坦等 honeynet 项目——赋予其全球互联网视角。（BSDTalk EP49，[56.56-134.08]，L1）
- 高交互 honeynet 的架构与工具链：honeynet 只是高交互 honeypot——由真实计算机与应用组成、供坏人与恶意软件入侵以观察全程的网络；部署核心是 HoneyWall 网关这一进出流量访问控制设备，约半小时可建成，配合 HoneyWall CD-ROM（基于 Fedora）将整套数据捕获与数据控制功能集成；主机侧数据捕获由内核态的 Sebek 完成、设计同时支持 SPARC 与 Intel 平台并以四条款 BSD 许可发布，分析界面 Walleye 亦出自印第安纳大学团队；部署耗时已从数日缩至约一小时，而组织的研究重心已整体转向数据分析。（BSDTalk EP49，[186.64-258.50]，L1）
- 开放悖论的自觉承担：项目全面开源、与社区共享一切，坏人因此可以下载其工具、逆向并发展反制——如同一场向对手亮出底牌的扑克；但 Spitzner 明言不愿改变，因为要开放、没有秘密，开放本身放大了创意共享与研究能力。（BSDTalk EP49，[317.02-345.34]，L1）
- 部署策略与攻击自动化的转折：过去部署默认老旧未打补丁的系统以观察入侵并捕获 botnet、IRC 命令控制信道等恶意软件，如今开始向金融部门试水更现代、加固到位的高价值 honeynet；手工攻击早在三五年前已被自动化取代——按键犯错与藏匿踪迹的时代过去，有组织者自设研发部门开发新工具，一切复归投资回报逻辑，连隐藏行踪都常属多余；而月度扫描分析挑战的停办本身即是趋势证据——四五年来入侵手法并无新意，创新全部集中于 botnet 与恶意软件的工具能力增强。（BSDTalk EP49，[355.54-393.78]，L1）
- 自身风险模型与下线原则：honeypot 唯一目的是收集信息，而坏人通常不在乎被观察——他们拥有数千台肉鸡、也不自认有被追查的风险，真正招致报复的是直接影响其收入的行为，如被分布式拒绝服务攻击打垮的反垃圾邮件公司；每个 honeynet 均配数据控制机制（出站连接计数、IPS）以缓解而非消除对外危害；在线与否的判据是学习价值——尚有新东西可学就保持在线，否则拔线，有时人与活动依旧、新的只是恶意代码样本。（BSDTalk EP49，[565.30-624.94]，L1）

**史料**：

- Frederic Cambus 的博客与 OpenBSD airport(7) 手册页共同构成 airport 文件习俗的一手记载，其补丁与 Theo de Raadt 的私下回复均可溯源。（BSD Now EP460，[1136.02-1184.7]，L2）
- HardenedBSD 2022 年 5 月状态报告与 DragonFly BSD 6.2.2 变更日志，记录 chroot 限制、无调试内核更新、HAMMER2 修复等版本级工程事实。（BSD Now EP460，[1444.3-1739.18]，L2）
- 该期留存的一手威胁情报方法论：以国别文化画像取代个体画像——罗马尼亚识字率高于美国、东欧数学训练深厚而经济凋敝、高教育者失业，构成经济性黑客的温床，同一框架可解释尼日利亚；IRC 在 2006 年仍是数字地下的首要通信渠道且因犯罪动机而日趋私密化；观测到的攻击错配实例包括投递预编译 Linux 二进制至非 Linux 系统、以 Solaris x86 exploit 打 Solaris SPARC 机器；OS 检测所获多为跳板肉鸡（印度、韩国、巴西等受害者系统）而非攻击者本体。（BSDTalk EP49，[753.96-876.92]，L1）

**史观**：

- 总纲15 文化即形式主义：airport(7) 规则本为开发者圈内默契，经一次补丁触发才被成文固化，显示社区文化以非正式实践维系并最终形式化，属文化即形式主义的例证。（BSD Now EP460，[1143.58-1184.7]，L2）
- 总纲20 历史地理塑造思想土壤：airport 文件要求开发者亲访机场验证存在，把地理经验与代码贡献绑定，体现历史地理与社区实践的相互塑造。（BSD Now EP460，[1184.7-1244.26]，L2）
- 总纲13 法律与道德是利益分配：威胁的经济学转型：五年间安全社区的技术进步，坏人大约五分钟即可绕过——系统与应用愈发安全，攻击便转向人这一最弱链路（钓鱼、即时消息诱饵）；动机从扬名立万转为投资回报，坏人变得安静、高效、只做最赚钱的事；互联网犯罪兼具极高利润与极低风险——归因困难、即便锁定个人亦难在法庭证明并跨国追诉（中国、罗马尼亚、巴西）；故其断言要解决的不是 hacking 而是 crime，犯罪已存续千年、无从根除只能威慑。（BSDTalk EP49，[394.78-541.98]，L1）

**辨析**：

- airport(7) 规则在转写中被归于 OpenBSD hackathon 写入，但具体是哪一次 hackathon 及成文时间需查手册页修订记录与邮件列表。　[考据脚注] airport(7) 手册页引入的具体时间与 hackathon 场次需查 OpenBSD CVS 与 Undeadly 记录。（BSD Now EP460，[1173.42-1184.7]，L4）
- 对 OpenBSD 传言的辨析与个人实践：关于黑客检测到 OpenBSD 便退走的说法，Spitzner 的观测结论是并非因其强而退，而是因其非所期——坏人只携带已知平台（Linux、Windows）的 exploit 与恶意软件，遇到预期之外的系统便径直跳过，近乎借助隐蔽求安全；其个人规则为凡联互联网的机器必用 OpenBSD，理由是其安全与他对 de Raadt 安全狂热的个人信任，私人桌面则选 Mac OS 纯为易用；另据 NetCraft 观察该组织网站多年托管于 OpenBSD 或 NetBSD、近期转 Linux，他解释纯因 HoneyWall CD-ROM 基于 RPM、网站需承担自建 RPM 的构建与分发，就 web 平台而言仍偏好 OpenBSD。（BSDTalk EP49，[1282.50-1519.84]，L1）

**文献**：

- [BSD Now EP460] Pennington J. BSD Now: 460: OpenBSD airport folklore[EB/OL]. (2022-06-23)[2026-08-15]. <https://www.bsdnow.tv/460>.
- [BSDTalk EP49] Backman W. BSDTalk: 49: bsdtalk049 - Interview with Honeynet.org President Lance Spitzner[EB/OL]. (2006-06-01)[2026-08-27]. <https://archive.org/details/bsdtalk049>.

<!-- /PODCAST_REVIEW -->
