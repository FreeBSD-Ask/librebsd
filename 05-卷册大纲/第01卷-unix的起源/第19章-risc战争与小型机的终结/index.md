---
chapter: 第 19 章
id: CH19
volume: 第01卷-unix的起源
---

# 第 19 章 RISC 战争与小型机的终结

## 要点

1980 年代 RISC（精简指令集计算机）与CISC（复杂指令集计算机）之间的架构之争决定性地终结了以DEC PDP/VAX 谱系为代表的小型机时代。MIPS、SPARC、PowerPC、ARM等RISC架构的兴起与x86 CISC路线的持续演进形成两条并行轨迹，最终以RISC设计理念渗透进现代处理器微架构（现代x86内部实为RISC核）而告终。这场“战争”不仅改变了硬件格局，也重塑了UNIX工作站的市场生态——Sun SPARC、SGI MIPS、DEC Alpha等RISC工作站在1990年代成为BSD与UNIX的主要运行平台。

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_1537] 卷“第01卷-unix的起源”第 19 章，匹配置信度 0.9，原因：关键词搜索下载文献，标题含章节主题

## 史观

总纲第 5 条——没有必然性，只有偶然性：RISC的胜利并非技术必然，而是市场选择、软件生态（UNIX工作站对RISC的原生支持）与商业策略（如Sun的SPARC垂直整合）共同作用的结果。总纲第 4 条——分离聚合是永恒规律：CISC与RISC并非线性替代关系，而是形式主义曲线的流转，现代x86处理器内部译码为RISC-like微操作、ARM向服务器领域渗透，均呈现分离聚合的循环。总纲第 10 条——动手者创造历史：RISC理念的源头可追溯至John Cocke在IBM 801项目中的工程实践与David Patterson在伯克利的RISC-I/RISC-II教学芯片，两者均以动手实验而非理论推导为核心。

## 辨析

“RISC战胜CISC”的简化叙事遮蔽了x86在PC市场的持续主导地位：Intel凭借工艺优势与向后兼容性，以CISC外观实现了RISC内核的微架构，实质上消解了RISC/CISC的二元对立。DEC Alpha 的退场（2001 年 Compaq 宣布转向 Itanium，2004 年路线图终止、2007 年 4 月停产）是否为技术判断失误还是商业决策失误，学界仍有争议。ARM架构在嵌入式与移动设备中的崛起（2000年代）与Apple Silicon在桌面/服务器市场的回归（2020年代）构成了RISC理念的辩证回归，但这一叙事本身需要警惕将“ARM的胜利”本质化为“RISC的必然胜利”。

## 文献

（待补：Patterson D A, Hennessy J L. Computer Architecture: A Quantitative Approach[M]. 6th ed. Morgan Kaufmann, 2017；Colwell R P. The Pentium Chronicles: The People, Passion, and Politics Behind Intel's Landmark Chips[M]. Wiley, 2005；[DB:references_fulltext:chapter_matches:chmatch_1537]）

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP425（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- RISC-V 诞生于加州大学伯克利分校的并行计算实验室，规格于 2011 年公开发布，以开放指令集摆脱专利限制。（BSD Now EP425，[72.68-155.2]，L2）
- FreeBSD 11 将 RISC-V 作为 tier 3 平台引入，至 FreeBSD 13 提升为 tier 2，反映其硬件与软件生态的逐步成熟。（BSD Now EP425，[261.34-289.84]，L2）
- OpenBSD 的一种漏洞缓解措施是在每次启动时随机重链接内核库，使内存偏移在每次启动间不断变化。（BSD Now EP425，[347.28-368.9]，L2）

**史料**：

- Clara Systems 的 RISC-V 架构介绍文章、JT 对 RISC-V International 首席技术官 Mark Himelstein 的采访、Frederick Cambus 关于 NetBSD 运行于 Vortex86DX 的记录。（BSD Now EP425，[65.5-344.5]，L2）[订正：原 [65.54-72.34]，2026-10-01 SenseAudio 重转核对]

**史观**：

- 总纲第 3 条——不存在进步，只有权力再分配：RISC-V 以开放指令集回应既有指令集的专利壁垒，展示技术路线的开放与封闭之争如何在权力与利益格局中展开。（BSD Now EP425，[125.88-143.06]，L2）

**辨析**：

- RISC-V 的伯克利起源与专利动机为文章转述，具体时间节点与参与者需与原始论文、基金会档案核对。 [存疑脚注] RISC-V 起源细节为二手转述，宜以伯克利原始论文与基金会材料校正。（BSD Now EP425，[72.68-155.2]，L4）

**文献**：

- [BSD Now EP425] Pennington J. BSD Now: 425: Releases galore[EB/OL]. (2021-10-21)[2026-08-15]. <https://www.bsdnow.tv/425>.

<!-- /PODCAST_REVIEW -->

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-084 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-084`；w172 YouTube 章节路由采纳）

据〔普林斯顿大学 Brian Kernighan 口述历史访谈（续）〕讲者口述：他逐项验收 Go 的目标：编译"very very fast"，且产出静态二进制，依赖地狱由此根除；并发模型源自 Tony Hoare 上世纪 70 年代的通信顺序进程（CSP）思想，"very very well and efficiently implemented"，这也是他自认掌握最好的部分〔59:07〕。他阐释 goroutine 与带类型 channel 的所有权语义：我的数据经 channel 送出，"now you've got it and I don't have it anymore"，思维层面不存在共享的中间态，无意共享数据结构的一类问题在该层级无从发生；运行时自然要在底层替你保证一致性，但传统锁与互斥量因此用得少得多；据他亲手做的几个小实验，爬网络、遍历分布式文件系统这类活计用 Go 写等价代码，比 Python 或 Java 的线程模型快约三分之一〔59:31〕。有人称 Go 是"21 世纪的 C"：表面语法足够像 C，同样推崇最小机制；但它又在 C 的松散处反其道而行——各类型的位宽被明确写死、表达式里不许夹带赋值等副作用，还有标准排版程序让所有 Go 代码形态如一，括号位置之争的"religious wars"就此消失；类型错误大多在编译期而非运行期暴露，这比 Python 的动态类型可靠，于是 Go 一边蚕食 C++ 一边蚕食 Python，写爬虫或分布式服务时是"really good choice"〔61:32〕。（YouTube EPbTWv-l0JhAc）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-083 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-083`；w172 YouTube 章节路由采纳）

据〔普林斯顿大学 Brian Kernighan 口述历史访谈〕讲者口述：话题转入 Go：Kernighan 常年在纽约的 Google 过夏天，自嘲"kind of like an intern in many respects"，某年恰被安排坐进 Go 团组，"in effect I was his intern for the summer"，学到够用的 Go，并结识了此前素不相识的 Alan Donovan；两人都不满意市面上已有的 Go 书，遂花约一年时间打磨合写 The Go Programming Language，他直言书中工作"at least 90% his"，因为 Donovan 对包括 Go 在内的各门语言从里到外了如指掌〔55:27〕。随后他把 Go 放进语言谱系：从 CPL 到 Martin Richards 的 BCPL，再到贝尔实验室 Ken Thompson 的 B、Dennis Ritchie 的 C，其后是 C++ 与 Java——"many of these are reactions to the language that went before"，新语言多是对上一代语言不满的回应；而硬件演进让处理速度与内存更充裕，加之"我们对要做什么、怎么做的理解也在改进"，重起炉灶遂变得可行〔56:58〕。按他的归纳，Java 部分是对 C++ 体量的反应，且得益于十年摩尔定律才可改用解释器代替编译器；Go 则"explicitly a reaction to the complexity of C++"，由 Robert Griesemer、Rob Pike 与 Ken Thompson 在 Google 开发，指导原则就是干脆不做 C++，转而解决 Google 写超大规模代码的现实难题——编译时间太长、可移植性问题，以及"dependency hell"（不一致的库版本酿祸）；项目 2007 年启动，数年后开源，如今已是彻底的开源项目〔58:08〕。（YouTube EPbTWv-l0JhAc）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->
