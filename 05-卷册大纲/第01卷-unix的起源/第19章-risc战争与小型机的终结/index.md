---
chapter: 第 19 章
id: CH19
volume: 第01卷-unix的起源
---

# 第 19 章 risc战争与小型机的终结

## 要点

1980年代RISC（精简指令集计算机）与CISC（复杂指令集计算机）之间的架构之争决定性地终结了以DEC PDP/VAX谱系为代表的小型机时代。MIPS、SPARC、PowerPC、ARM等RISC架构的兴起与x86 CISC路线的持续演进形成两条并行轨迹，最终以RISC设计理念渗透进现代处理器微架构（现代x86内部实为RISC核）而告终。这场"战争"不仅改变了硬件格局，也重塑了UNIX工作站的市场生态——Sun SPARC、SGI MIPS、DEC Alpha等RISC工作站在1990年代成为BSD与UNIX的主要运行平台。

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_1537] 卷“第01卷-unix的起源”第 19 章，匹配置信度 0.9，原因：关键词搜索下载文献，标题含章节主题

## 史观

总纲第3条——偶然性优先：RISC的胜利并非技术必然，而是市场选择、软件生态（UNIX工作站对RISC的原生支持）与商业策略（如Sun的SPARC垂直整合）共同作用的结果。总纲第4条——循环结构呈现：CISC与RISC并非线性替代关系，而是形式主义曲线的流转，现代x86处理器内部译码为RISC-like微操作、ARM向服务器领域渗透，均呈现分离聚合的循环。总纲第6条——动手者创造历史：RISC理念的源头可追溯至John Cocke在IBM 801项目中的工程实践与David Patterson在伯克利的RISC-I/RISC-II教学芯片，两者均以动手实验而非理论推导为核心。

## 辨析

"RISC战胜CISC"的简化叙事遮蔽了x86在PC市场的持续主导地位：Intel凭借工艺优势与向后兼容性，以CISC外观实现了RISC内核的微架构，实质上消解了RISC/CISC的二元对立。DEC Alpha的过早退出（1998年Compaq终止Alpha开发）是否为技术判断失误还是商业决策失误，学界仍有争议。ARM架构在嵌入式与移动设备中的崛起（2000年代）与Apple Silicon在桌面/服务器市场的回归（2020年代）构成了RISC理念的辩证回归，但这一叙事本身需要警惕将"ARM的胜利"本质化为"RISC的必然胜利"。

## 文献

（待补：Patterson D A, Hennessy J L. Computer Architecture: A Quantitative Approach[M]. 6th ed. Morgan Kaufmann, 2017；Colwell R P. The Pentium Chronicles: The People, Passion, and Politics Behind Intel's Landmark Chips[M]. Wiley, 2005；[DB:references_fulltext:chapter_matches:chmatch_1537]）
