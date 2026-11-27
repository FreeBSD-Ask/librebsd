# An Introduction to the C shell（Joy，USD:4）引用卡

> 用途：V12.3.5 节（C Shell 的设计：交互式 Shell 的新模式）内容补证（V12 补证批 b070）。设计者技术文档（一手技术文献，L3）。

## 一、著录

Joy, William. An Introduction to the C shell[Z/OL]. Revised for 4.3BSD by Mark Seiden. Berkeley: Computer Science Division, Department of EECS, University of California, Berkeley. UNIX System Development（USD:4）[2026-11-27]. https://docs-archive.freebsd.org/44doc/usd/04.csh/paper.pdf.

- 责任者：William Joy（原作者）；Mark Seiden（4.3BSD 修订）
- 载体：PDF（117,797 B；pdftotext -layout 抽文 145,082 字符，存 `script/_g2_csh_paper.txt`）
- `source_tier=primary`（设计者文档，一手技术文献；L3 公开文献记载）
- 访问日：2026-11-27（curl 直取 FreeBSD docs-archive 44doc）

## 二、逐字引文（英文，未翻译）

交互为中心的设计（3.5.1A，Abstract）：

> While incorporating many features of other shells which make writing shell programs (shell scripts) easier, most of the features unique to csh are designed more for the interactive UNIX user.

类 C 语法（3.5.2A，glossary 的 switch/default 条）：

> The label default: is used within shell switch statements, as it is in the C language to label the code to be executed if none of the case labels matches the value switched on (3.7).

与传统解释器的分野（3.5.5A，1.1 节）：

> The shell is thus distinguished from the command interpreters of other systems both by the fact that it is just a user program, and by the fact that it is used almost exclusively as a mechanism for invoking other programs.

设计取舍的协作者（3.5.6A，Acknowledgements，Allman 的取舍意见）：

> Eric Allman has also provided a large number of useful comments on the shell, helping to unify those concepts which are present and to identify and eliminate useless and marginally useful features.

## 三、考据说明

1. 本文档（USD:4）为 csh 的**设计者说明书**：Abstract 明言“csh 独有的特性多为交互式用户而设计”（交互为中心的设计意图）；1.1 节给出与传统系统命令解释器的分野（用户程序、专用于调用其他程序）；glossary 的 default 条给出类 C 语法的自我类比；Acknowledgements 记 Allman 等协作者的取舍意见——四段逐题对应 3.5.1／3.5.2／3.5.5／3.5.6。
2. **贡献者署名**：Acknowledgements 另记 Michael Ubell（历史机制原型）、Mike O'Brien（路径名哈希）、Jim Kulp（作业控制与目录栈原语）——为 3.9.2 附随文档署名的直接实例（另批可用）。
3. **版本说明**：4.3BSD 修订版（Seiden）比 1979 年 csh 初版晚；文档的“设计意图”叙述按 L3 引用，具体实现时点须与 2BSD 树件（1980-02-18）交叉。
4. 禁引核查：FreeBSD 官方文档存档（44doc），`banned_source=0`。
