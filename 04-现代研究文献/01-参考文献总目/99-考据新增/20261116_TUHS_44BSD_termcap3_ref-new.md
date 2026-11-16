# 4.4BSD termcap(3) 手册页（TUHS 收录）（新 ref）引用卡

- **性质**：TUHS 源码树收录的 4.4BSD `usr/src/lib/libterm/termcap.3`（终端能力库 tgetent／tgetnum／tgetflag／tgetstr／tgoto／tputs 手册页）；本机 Chrome UA urllib 直取，`<pre>` 块 6,354 字符
- **数据库**：新建 ref（2026-11-16 V31 P2 联网补证批 b005；source_url 四键查重：库内 termcap 无条目）
- **source_url**：<https://www.tuhs.org/cgi-bin/utree.pl?file=4.4BSD/usr/src/lib/libterm/termcap.3>
- **quote（逐字，两处；mroff 渲染后）**：
  1. terminal independent operation routines
  2. These functions extract and use capabilities from a terminal capability data base
- **考据注**：第 1 句是 NAME 行的自我定位（“与终端无关的操作例程”），第 2 句说明机制（从终端能力数据库提取并使用能力）。两句合读正是“抽象层”的定义：**差异挪进数据，代码只认能力名**。用于 6.3.6“抽象层的扩散影响”。**截引说明**：第 2 句原句续接“usually /usr/share/misc/termcap, the format of which is described in termcap(5).”，本块只取前半，属句中截引。**能证与不能证**：只证 4.4BSD 手册页的自述与接口形态，不证 termcap 的首创年代与在 BSD 外的扩散范围（后者须另取发行数据或应用侧证据）。**未取**：tputs 的填充字符（padding）细节与 curses(3) 更高层封装，留待 6.3.4
- **本批落点**：V31.6.3.6 第 1 块（第 1 句）、第 2 块（第 2 句）
- **考据日期**：2026-11-16（Task 8.2 G4 V31 P2 批 b005；official_doc／L3）
