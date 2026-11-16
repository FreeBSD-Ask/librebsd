# 4.4BSD pc(1) 手册页（TUHS 收录）（新 ref）引用卡

- **性质**：TUHS 源码树收录的 4.4BSD `usr/src/usr.bin/pascal/pc/pc.1`（伯克利 Pascal 编译器手册页，正文提及《Berkeley Pascal User's Manual》）；本机 Chrome UA urllib 直取，`<pre>` 块 7,027 字符
- **数据库**：新建 ref（2026-11-16 V31 P2 联网补证批 b006；source_url 四键查重：库内 pc(1)／pascal 无该路径）
- **source_url**：<https://www.tuhs.org/cgi-bin/utree.pl?file=4.4BSD/usr/src/usr.bin/pascal/pc/pc.1>
- **quote（逐字，两处；mroff 渲染后）**：
  1. If given an argument file ending with .p, it will compile the file and load it into an executable file called, by default, a.out.
  2. A program may be separated into more than one .p file.
- **考据注**：两句说明这套教学语言系统是**成套供给**：编译即装入 a.out（第 1 句），程序可拆多个 .p 分文件编译（第 2 句）——学生不必自建工具链，作业可分文件组织。用于 4.1.3“系统软件教育的示范案例”。**能证与不能证**：只证 4.4BSD 发行内该编译器的接口形态，不证其在课程中的实际用法与开设年份（课程记载须另取）。**同目录配套**：`USD.doc/` 下有成组的示例程序与期望输出（如 bigger.p、kat.p 与对应 *out），本批仅作旁证，未引其代码——**代码类引文未经转义校验，本批不取**。**载体说明**：TUHS 转录，按原文核对
- **本批落点**：V31.4.1.3 第 1 块（第 1 句）、第 2 块（第 2 句）
- **考据日期**：2026-11-16（Task 8.2 G4 V31 P2 批 b006；official_doc／L3）
