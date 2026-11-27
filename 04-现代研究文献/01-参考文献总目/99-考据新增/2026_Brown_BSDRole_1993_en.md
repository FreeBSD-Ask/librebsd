# The Role of BSD in the Development of Unix（Brown 1993）引用卡

> 用途：V12.5.1.1（作业控制机制扩展）／5.5.2（许可条款延续与调整）内容补证（V12 补证批 b067）。学术演讲论文（二手权威，L3）。

## 一、著录

Brown, Michael G. The Role of BSD in the Development of Unix[C/OL]. Presented to the Tasmanian Unix Special Interest Group of the Australian Computer Society, Hobart, August 1993[2026-11-27]. https://wolfram.schneider.org/bsd/ftp/article/bsdrole.html.

- 责任者：Michael G. Brown（Department of Premier and Cabinet, Tasmania）
- 载体：演讲论文网页（tvly extract raw 16,773 字符存 `script/_g2_bsdrole.txt`；Wolfram Schneider 镜像）
- `source_tier=secondary_authoritative`（1993 年学术演讲综述；L3 公开文献记载）
- 访问日：2026-11-27（tvly extract）

## 二、逐字引文（英文，未翻译；原文瑕疵照录）

AT&T 源码许可的低价（5.5.2A，早期源码许可约 100 美元）：

> Many researchers at universities worldwide had taken advantage of AT&T's generous offer to furnish source for Unix at negligible cost - early source licences cost of the order of US$100.

4.1BSD 引入作业控制（5.1.1A；原文 “maintanance” 拼写瑕疵照录）：

> The end of 1980 saw the release of 4.1BSD. Although primarily a maintanance release, 4.1 introduced job control, a system of run-time autoconfiguration and provided for longer identifiers in the symbol table of object files.

PDP-11 内存对早期内核的约束（备选，内核体积面）：

> The limited memory space of the PDP-11 machines constrained the early works, although many small efficiences were made in the kernel, and some programs were added, including Bill Joy's now legendary visual text editor, vi, in 2BSD.

## 三、考据说明

1. Brown 1993 演讲综述 BSD 史，其“4.1BSD（1980 末）引入 job control”句是作业控制时点的**第三方学术记述**；与 Wikipedia“4BSD（1980-11）的 csh 已有 job control”并存——两说的差异（csh 的用户态作业控制 vs 内核的 job control 支持）正是“版本线索断裂处标存疑”的实例，claim 须并置两源而非取一。
2. AT&T 源码许可约 100 美元句，是 5.5.2“许可条款延续与调整”的基线面（学术系统的许可成本），与 ref1575“4BSD per-institution 许可”形成“源头低价—发行按机构”的两段。
3. 原文瑕疵：“maintanance”（maintenance 拼写错误）、“efficiences”（efficiencies）照录不代改。
4. L3 纪律：1993 年综述距事件十余年，具体时点须与当事人记述（ref1575）交叉。
5. 禁引核查：公开镜像学术演讲文，`banned_source=0`。
