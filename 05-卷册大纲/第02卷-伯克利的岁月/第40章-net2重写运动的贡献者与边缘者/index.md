---
chapter: 第 40 章
id: CH40
volume: 第02卷-伯克利的岁月
---

# 第 40 章 net2重写运动的贡献者与边缘者

## 要点

- 在诉讼期间继续 4.4BSD 开发；**1994 年 2 月** Novell-UC Berkeley 达成和解后，CSRG 于 **1994 年 6 月** **同时发布** 两个版本：4.4BSD-Lite（完全自由版，不含 AT&T 衍生代码，是 Net/2 完全自由路径的继承与巩固）
- BSD 重写运动的独特性包括：基于成熟 BSD 代码基础（4.3BSD Reno）、社区志愿重写模式（早于现代开源协作 10 年）、法律风险预判与文件保留、BSD 许可证的宽松性（允许商业封闭）、与 USL 诉讼的法律博弈，这些独特性使 BSD 路线与 Linux 路线在 1990 年代分化
- shadow password（密码散列分离存储）在 BSD 与 System V 的分野源于 **1980 年代** 两者的安全哲学差异——System V **R3.2**（**1987 年**）引入 `/etc/shadow` 文件将密码散列从 `/etc/passwd` 移至仅 root 可读的 `/etc/shadow`，降低字典攻击风险，反映 System V 优先考虑商用客户的密码安全诉求
- 边缘贡献者的史料散见于源代码注释、邮件列表、新闻组与 CSRG 内部档案，缺乏系统化传记，需通过多源交叉核对恢复身份，特别是使用用户名的匿名贡献者与一次性补丁提交者
- Net/2 重写采用‘逐文件替换’策略：对每一个包含 AT&T 版权代码的文件，CSRG 安排独立程序员（未见过 AT&T 源码者）根据公开发布的文档与接口描述重写实现。这一‘洁净室’方法的法学依据是 Reverse Engineering 原则（Sony v. Connectix, 2000 年的判决确认，但 CSRG 在 1989 年即已实践）。

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3715] 卷“第02卷-伯克利的岁月”第 40 章，匹配置信度 folder，原因：folder 第40章
- [DB:references_fulltext:chapter_matches:chmatch_3765] 卷“第02卷-伯克利的岁月”第 40 章，匹配置信度 folder，原因：folder 第40章
- [DB:references_fulltext:chapter_matches:chmatch_3767] 卷“第02卷-伯克利的岁月”第 40 章，匹配置信度 folder，原因：folder 第40章
- [DB:references_fulltext:chapter_matches:chmatch_3769] 卷“第02卷-伯克利的岁月”第 40 章，匹配置信度 folder，原因：folder 第40章
- [DB:references_fulltext:chapter_matches:chmatch_3814] 卷“第02卷-伯克利的岁月”第 40 章，匹配置信度 folder，原因：folder 第40章
- [DB:references_fulltext:chapter_matches:chmatch_3936] 卷“第02卷-伯克利的岁月”第 40 章，匹配置信度 folder，原因：folder 第40章
- [DB:references_fulltext:chapter_matches:chmatch_3942] 卷“第02卷-伯克利的岁月”第 40 章，匹配置信度 folder，原因：folder 第40章
- [DB:references_fulltext:chapter_matches:chmatch_3954] 卷“第02卷-伯克利的岁月”第 40 章，匹配置信度 folder，原因：folder 第40章
- [DB:references_fulltext:chapter_matches:chmatch_1544] 卷“第02卷-伯克利的岁月”第 40 章，匹配置信度 0.9，原因：关键词搜索下载文献，标题含章节主题
- [DB:references_fulltext:chapter_matches:chmatch_978] 卷“第02卷-伯克利的岁月”第 40 章，匹配置信度 0.8，原因：关键词重合 2 项 + 加分 1
- [DB:bsdnow_podcast:outline_mappings:om_11526] BSD Now 第 527 期，匹配 CH40 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11939] BSD Now 第 474 期，匹配 CH40 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12605] BSD Now 第 404 期，匹配 CH40 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12677] BSD Now 第 379 期，匹配 CH40 章，关联度 1.0
- [DB:historical_claims:claim] 关键词行级挖掘素材线索 40.13-关键词行级挖掘素材线索（1 条，CL-RM 段，见 40.13-关键词行级挖掘素材线索.md）

## 史观

- 总纲第 5 条——没有必然性，只有偶然性：Net/2 的历史关口显示偶然决策如何改写法律格局——面对仅余六个待清理文件的内核，团队选择宣布内核不完整、以存根填充发布，这一临时的发布策略日后成为 386BSD 及其后的 FreeBSD 赖以合法起步的直接基础（整合自本章 PODCAST_REVIEW 史观段）；其余子节史观详见各子节史观/辨析字段

## 辨析

- 4.4BSD-Encumbered 与 4.4BSD-Lite 均于 1994 年 6 月同时发布（McKusick 当事人原文"Simultaneously, the complete system was released as 4.4BSD-Encumbered"），非 1993 年 11 月——1993 年仅发布过 4.4BSD-Alpha 测试版给 AT&T 许可持有者；4.4BSD-Lite 与 4.4BSD-Encumbered 同发的具体记载须以两套 Release Notes 原文复核
- BSD 与 Linux 的“独特性”对比需谨慎，避免事后判断，1991 年两者均处于早期阶段
- shadow password 分野的“安全哲学差异”叙述需避免简化为“BSD 不重视安全”——BSD 选择单文件格式是基于 NIS 工程约束的实践判断，而非忽视密码安全，须区分“安全哲学差异”与“安全意识差异”；BSD 直至 **4.4BSD-Lite** 仍坚持 `/etc/passwd` 单文件格式的判断需核对——4.4BSD-Lite Release Notes 与 4.4BSD 系统管理员手册（SMM）
- Net/2 历史意义的辨析须遵循 0 信任原则——即使 McKusick 1999 当事人叙述亦须与 Justia 法院意见书、FreeBSD Handbook、NetBSD 官方历史页面等独立来源交叉验证；CSRG 的发布意图（“完全自由 BSD”）与 USL 的诉讼视角（“盗用 AT&T 代码”）存在根本分歧，须区分双方视角而不预设一方正确；Net/2 的“历史意义”在不同史料中有不同表述，需逐条对照原始出处比较

## 文献

- Net/2 Release Notes (1991.6)；4.4BSD-Lite/4.4BSD-Encumbered Release Notes (1994.6)；4.4BSD-Lite 2 Release Notes (1995.6)；Novell-UC Berkeley 和解协议（1994.2）；FreeBSD/NetBSD/OpenBSD Release Notes；McKusick, M. K. (1999) “Twenty Years of Berkeley Unix”；McKusick M K, Bostic K, Karels M J, Quarterman J S. The Design and Implementation of the 4.4BSD Operating System [M]. Reading: Addison-Wesley, 1996. ISBN: 0-201-54979-4 ［B］；资料数据库.duckdb 文献计量学分析报告（`03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/文献计量学分析.md` Task 22，2026-07-27）；外部基准报告（`03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/外部基准-Academic-CVE.md` 第 1.2 节，E-19，2026-07-27）；卷章数据映射表（`03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/卷章数据映射.md` 第二卷第 20 章）
- Bostic, K. (1991) “Net/2 Release Notes”；McKusick, K. (1999) “Twenty Years of Berkeley Unix”；Moody, G. (2001) “Rebel Code” ［B］

<!-- DB_REF:linux_kernel.duckdb -->
> **数据库引用（linux_kernel.duckdb）**：本子节对应 linux_kernel 代码仓库。> 1991-1991 年间：0 次提交。> 仓库总览：1,474,341 次提交，39,865 位贡献者（contributors 表行数，1970-01-01 至 2026-08-24）。
- **4.2BSD** `/etc/passwd` 文件格式规范；System V **R3.2** `/etc/shadow` 文件规范 (**1987**)；**4.4BSD-Lite** Release Notes (**1994.6**)；4.4BSD 系统管理员手册（SMM）；**FreeBSD 4.0** Release Notes (**2000.3**)；Salus, P. H. (1994) “A Quarter Century of UNIX”；Leffler, S. J. et al. (1989) "The Design and Implementation of the 4.3BSD UNIX Operating System" ［A］（考据留痕：[^doubt-resolved-235] 与 [^doubt-resolved-238] 两处疑点据 Design_Implementation_FreeBSD_OS（未署名）消解）
- Net/2 源代码注释；CSRG 邮件列表存档（伯克利 Bancroft 图书馆）；comp.unix.bsd 新闻组存档 ［A］

## 文献增补与辩证校准（2026-08-08 追加）

> - **文献增补（ref 3778）**：McKusick《Twenty Years of Berkeley Unix》(1999) 确认“约一百个工具”18 个月内由社区志愿者完成——40.7 匿名贡献者考据的直接一手依据
> - **文献增补（ref 3780）**：4.4BSD 设计书作者简介（Bostic GWU 背景/CSRG 400+ 工具管理）可补充 40.7 人物档案
> - **辩证校准（总纲第 10 条——动手者创造历史；总纲第 5 条——没有必然性，只有偶然性）**：40.7 “需主动恢复其历史可见性”的表述，应以“如实记录”替代“主动恢复”——匿名贡献者的价值按其实际贡献记录即可，不须以“被亏欠”姿态写作
- CSRG Net/2 档案； McKusick 1999 ［A］
- McKusick, M. K. (1999) “Twenty Years of Berkeley Unix”；FreeBSD Handbook 第 1 章（docs.freebsd.org/en/books/handbook/introduction/#history）；NetBSD 官方历史页面（netbsd.org/about/history.html）；*Unix System Laboratories v. Berkeley Software*, 832 F. Supp. 790 (D.N.J. 1993) ［B］

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：YouTube EP7d7fwAE-2Aw（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 讲者首先为 BSD Daemon 正名：他不是 demon（恶魔）而是 daemon，词义为半人半神的良善守护精灵、站在人的一边。这个形象从未有过正式名字，社区不断为它起名——早年甚至有一件 T 恤依讲者高中时期一位讨厌同学的玩笑把它标作 Chuck the demon；日后通行的 Beastie 之名，讲者翻查笔记仍无法确定命名者，只能承认不可考。已知最早的 daemon 图像出自 Mike O'Brien 委托的一幅画，讲者曾向 O'Brien 借四件特制 T 恤之一拍照后归还，原作留存于一家家庭印刷店，店主歇业后由 DEC 的 Armando Stettner 取去用于 PDP-11 Unix 的宣传；1985 年 6 月 USENIX 十周年纪念 T 恤复制该图像时抹去了艺术家签名——艺术品被使用时爱被抹去署名，成为贯穿全讲反复出现的母题。（YouTube EP7d7fwAE-2Aw，[44.879-283.0]，L1）[订正：原“讲者曾借原作拍照”→“讲者曾向 O'Brien 借四件特制 T 恤之一拍照后归还”，内容复核：新转写载借拍对象系袖口下摆缀花边的四件特制 T 恤之一（[228.2-236.9]），原作始终留存于家庭印花店（[234.1-243.7]）]
- 第一幅 John Lasseter daemon 源于一段偶然的职业史：Lasseter 时为迪士尼顶级动画师——他向听者解释迪士尼画师的三个层级，顶层画师只画间隔一帧的关键帧，其下是补足中间帧的画师与上色师——依例休半年带薪假，选择去 Lucasfilm 参与动画师工作站项目，为计算机图形工程师补上动画师真正需要的界面视角。返回迪士尼后他力推动画计算机化遭拒——迪士尼自恃全手工品质、称任何人都能买计算机——遂辞职重回 Lucasfilm；彼时 CSRG 正收尾 4.2BSD，同在 Lucasfilm 的 Sam Leffler 牵线，并出示早期 daemon 图请他参照，为 BSD 手册封面绘成第一幅黑白 daemon。因当时须持 AT&T 许可证方可持有 Unix，手册由 USENIX 代印以确保仅售予持证者；画中发光球上印有 Unix TM 字样，日后成为争议点，后续版本的光球上再无任何文字。（YouTube EP7d7fwAE-2Aw，[286.0-603.44]，L1）[订正：原“讲者拿早期 daemon 图请他参照”→“由 Sam 出示早期 daemon 图请他参照”，内容复核：新转写载系当时已在 Lucasfilm 的 Sam 向 Lasseter 出示旧 daemon 图并称“我们需要类似这样的图”（[529.4-546.9]），非讲者亲自出示]
- 第二幅 daemon 与 BSD 教科书出版史交织：CSRG 自 1983 年起就想写 BSD 教科书，Addison-Wesley 要求先获 AT&T 授权，而 AT&T 刚关停逐行注释 Unix 源码的 John Lions 之书——讲者承认在代码尚无版权保护、全凭商业秘密维系的年代，那并非无理——于是要求教科书写完再送审，合作就此搁浅。1986 年 Maurice Bach 的书出版且只记载到函数级接口，讲者据此说服出版社：本书绝不会涉及那样的细节深度，两年后 1988 年 4.3BSD 教科书出版，附有答问集并译成日语，讲者特别称赞在场监督翻译的译者。封面彩图是 Lasseter 已在 Pixar 时应 Sam Leffler 之请所绘：从垃圾桶抽出蓝色纸板、拿粉笔在约二十分钟内画成，迪士尼画风肉眼可辨；出版社先以严肃教科书不登卡通为由拒绝，被作者援引作者权利坚持收录，该书卖出五万册创纪录，内布拉斯加州学区一度以封面有恶魔为由拒其入馆。第三幅为 4.4BSD 教科书封面而作，讲者要求比前两幅更富动感；Lasseter 正忙于《玩具总动员》收尾，讲者以巧克力疏通其秘书才推动进度，画师铺纸研墨后自陈五年未动笔恐已生疏，随即在十分钟内完成；出版社又以发光球看起来太像精子细胞为由，把光球从封面与封底一并移除，只留签名。（YouTube EP7d7fwAE-2Aw，[871.0-1947.48]，L1）
- 讲者以亲历者身份补全 Net/2 重写运动的内幕：Net/2 最初只含 TCP/IP 代码与工具，社区不断要求更多，Keith Bostic 便在 USENIX 会议上以“让你的名字亮起来”号召重写 AT&T 的工具与库；投稿大多业余，Bostic 几乎从头重写却不署己名，一律保留贡献者姓名。内核侧由 Mike Karels 与讲者负责且进度滞后，被 Bostic 以“库与工具已过半，内核如何了”当面催问后，二人依其建议从 32V 原始源码出发，先用 C 美化器统一格式、为每一行建立数据库，再与自家内核逐行比对，忽略花括号独占一行之类的排版差异，连续数行相同即视为需要重写——例如把按进程 ID 的线性查找改为哈希查找，既清除 AT&T 代码又顺带更快。清理到最后仅剩六个文件存在显著匹配，Mike Karels 主张发布完整系统只会招来更多法律红旗，不如宣布内核不完整、只发布可发布部分，六个文件以模板存根形式放入——是为 Networking Release 2；定价一千美元，原本预计售出三份即会被放上网免费传播，实际售出约千份、入账约百万美元——买主看重的是加州大学那张自由再分发许可的纸，甚至嘱咐不必寄磁带。（YouTube EP7d7fwAE-2Aw，[1994.279-2243.119]，L1）
- USL 诉讼的亲历叙述补足正史细节：BSDi 创办后即被 AT&T 一方起诉，一审抗辩指出余下六个文件系洁净室重写、完全干净，法官已倾向驳回；原告遂转而追加起诉加州大学，大学立即停止分发——但这无关紧要，拷贝早已散布四方——继而质疑自己不从中获利、为何要出钱辩护。辩护经费正来自 Net/2 销售所得的约百万美元；面对对方的世界级专家证人，加州大学无力聘请对等的专家，讲者便自任专家证人（其细节他留作另讲）。诉讼期间讲者委托一位从未画过此类题材的肖像画家朋友创作反抗 T 恤：一幅 daemon 把被谑称为死星的 AT&T 新标志扣进篮筐，另一幅 daemon 脚踩 Birkenstock 凉鞋立于地球之上以矛刺穿死星。Dennis Ritchie 为此亲自来电：他理解并支持讲者的立场，但所用的标志属于 AT&T 而非起诉方 USL，恳请改用 USL 标志——讲者重印了 USL 标志版本，并至今珍藏一张 Ritchie 购买 T 恤而未兑现的支票。　[存疑脚注] 转写把扣篮 T 恤下方铭文记作 net2 USL Z，具体文字与史实铭文写法待与实物照片核证（YouTube EP7d7fwAE-2Aw，[2243.119-2434.72]，L1）
- daemon 图像的扩散与退场同样由当事人勾勒：Walnut Creek 时期流行的恶魔推着 CD 前行的 T 恤是 FreeBSD 常见形象，但 FreeBSD 最早的 T 恤只是在 daemon 前方添上 Free 字样；早期 NetBSD 与 OpenBSD 也曾沿用 daemon，FreeBSD Foundation 亦用过穿西装的 daemon 形象；此后各发行版与基金会相继弃用——因为恶魔形象在世界部分地区的公众观感不佳——转而启用各自的标志。法律一端，Lasseter 以雇用作品条款把画作著作权转让给讲者个人，转让书由讲者签署、Lasseter 会签，1988 年经版权局登记；经人提醒三十五年续展期已至，讲者正在办理续展。（YouTube EP7d7fwAE-2Aw，[2440.72-2531.4]，L1）[订正：原“把三幅画著作权转让给讲者个人并罕见地在画面正面签名”→“把画作著作权转让给讲者个人，转让书由讲者签署、Lasseter 会签”，内容复核：新转写仅载单一转让书、未言明涵盖三幅（[2504.2-2520.3]）；“罕见地在画面正面签名”实为肖像画家朋友之事（[2424.6-2445.1]），Lasseter 签名上 4.4 书封面系因其已成名人（[1797.0-1807.1]）]

**史料**：

- 该期口述自证的一手史料：Mike O'Brien 委托绘制的最早 daemon 原画（讲者借 O'Brien 藏的四件特制 T 恤之一拍照留影，原作后经 Armando Stettner 入 DEC 作 PDP-11 Unix 宣传）；1985 年 6 月 USENIX 十周年纪念 T 恤；4.2BSD 手册黑白封面原画、4.3BSD 教科书封面蓝色纸板粉笔画与 4.4BSD 教科书封面原画（均由 John Lasseter 绘制并署名）；John Lasseter 签署的著作权转让书（1988 年版权局登记，讲者正办理续展）；讲者收藏的 Dennis Ritchie 购买 T 恤的未兑现支票；限量刺绣版 daemon T 恤（仅授予对伯克利机器有提交权限或贡献过代码者）。（YouTube EP7d7fwAE-2Aw，[236.879-2531.4]，L1）[订正：原“讲者借拍留影”→“讲者借 O'Brien 藏的四件特制 T 恤之一拍照留影”，内容复核：新转写载借拍对象系特制 T 恤而非原画（[228.2-236.9]），原作始终留存于家庭印花店（[236.9-243.7]）]

**史观**：

- 总纲5 没有必然性，只有偶然性：Net/2 的历史关口显示偶然决策如何改写法律格局：面对仅余六个待清理文件的内核，团队没有选择完成清理后发布完整系统，而是为免招致更多法律红旗宣布内核不完整、以存根填充——这一临时的发布策略造就了 Networking Release 2，其约百万美元销售收入日后恰为 BSDi 应诉提供经费。历史的走向不取决于清理工作的完成度，而取决于一次关于如何讲述自身不完整性的措辞选择。（YouTube EP7d7fwAE-2Aw，[2185.72-2243.119]，L1）[订正：原“出于避免引人注目的公关考虑……日后却成为 386BSD 及其后的 FreeBSD 赖以合法起步的直接基础”→“为免招致更多法律红旗……造就了 Networking Release 2，其约百万美元销售收入日后恰为 BSDi 应诉提供经费”，内容复核：新转写载 Mike 之考量系避免招致更多红旗（[2185.7-2196.7]），后续仅述售出约千份、入账约百万美元与 BSDi 创办被诉（[2211.1-2243.1]），未提及 386BSD 或 FreeBSD]

**文献**：

- [YouTube EP7d7fwAE-2Aw] YouTube. YouTube: Fall 2024 FreeBSD Summit - The History of the BSD Daemon[EB/OL]. ()[2026-08-15]. <https://www.youtube.com/watch?v=7d7fwAE-2Aw>.

<!-- /PODCAST_REVIEW -->
