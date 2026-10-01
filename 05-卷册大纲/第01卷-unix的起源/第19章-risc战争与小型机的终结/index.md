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

- RISC-V 的伯克利起源与专利动机为文章转述，具体时间节点与参与者需与原始论文、基金会档案核对。　[存疑脚注] RISC-V 起源细节为二手转述，宜以伯克利原始论文与基金会材料校正。（BSD Now EP425，[72.68-155.2]，L4）

**文献**：

- [BSD Now EP425] Pennington J. BSD Now: 425: Releases galore[EB/OL]. (2021-10-21)[2026-08-15]. <https://www.bsdnow.tv/425>.

<!-- /PODCAST_REVIEW -->
