# 4.4BSD ex(1) 手册页（TUHS 收录）（新 ref）引用卡

- **性质**：TUHS 源码树收录的 4.4BSD `usr/src/usr.bin/ex/ex.1`（ex／edit／vi 编辑器家族手册页，日期 June 21, 1993）；本机 Chrome UA urllib 直取，`<pre>` 块 5,236 字符
- **数据库**：新建 ref（2026-11-16 V31 P2 联网补证批 b004；source_url 四键查重：库内 ex(1)／vi(1) 无该路径）
- **source_url**：<https://www.tuhs.org/cgi-bin/utree.pl?file=4.4BSD/usr/src/usr.bin/ex/ex.1>
- **quote（逐字，一处；mroff 渲染后）**：Ex is a superset of ed, with the most notable extension being a display editing facility. Display based editing is the focus of vi and requires a CRT.
- **考据注**：两句合读才是“转向”的准确说法：ex **是 ed 的超集**（行编辑的血统未断），最显著的扩展是**显示编辑**；显示编辑才是 vi 的重点，并且**需要 CRT**——技术转向同时是硬件条件（终端）的转向。用于 6.1.2“vi 的显示编辑转向”。**能证与不能证**：只证 4.4BSD 手册页的自我描述与硬件前提，不证 vi 的成文年代与作者（另见 6.1.x 其余小节）。**渲染记账**：原文 `\&Ex` 转义仅影响排版，引文作 “Ex”；`.Xr ed 1`／`.Xr vi 1` 渲染为 ed(1)／vi——本句引文未含手册交叉引用标记。**未取**：SYNOPSIS 的 `-v` 选项与 `edit` 变体差别，留待 6.1.6
- **本批落点**：V31.6.1.2 第 1 块
- **考据日期**：2026-11-16（Task 8.2 G4 V31 P2 批 b004；official_doc／L3）
