# ESR《The Art of UNIX Programming》第 2 章 History（新 ref）引用卡

- **性质**：Eric S. Raymond, *The Art of UNIX Programming*（O'Reilly, 2003）在线全文第 2 章 “History” 单页 `ch02s01.html`（49,407 字节；抓取正文 37,775 字符）
- **数据库**：新建 ref（2026-11-16 V35 P2 联网补证批 b017；查重：catb.org 域内本批仅取此页，库内另有 ref10697 GNU 页等非本页）
- **source_url**：<http://www.catb.org/esr/writings/taoup/html/ch02s01.html>
- **计数（抓取正文实测）**：`BSD` 25 次、`AT&T` 23 次、`Berkeley` 16 次、`Linux` 13 次、`4.2` 1 次
- **quote（逐字，两处，分落两块）**：
  1. Serious standardization efforts aimed at reconciling the System V and Berkeley APIs also began in 1983 with the /usr/group standard. This was followed in 1985 by the POSIX standards, an effort backed by the IEEE. These described the intersection set of the BSD and SVR3 (System V Release 3) calls, with the superior Berkeley signal handling and job control but with SVR3 terminal control. All later Unix standards would incorporate POSIX at their core, and later Unixes would adhere to it closely. The only major addition to the modern Unix kernel API to come afterwards was BSD sockets.
  2. The first BSD release had been in 1977 from a lab run by a then-unknown grad student named Bill Joy.
- **考据注**：第 1 处用于**POSIX 接口吸收 BSD 惯例的标准化路径**（1.3.1）：文中把 1983 年 `/usr/group`、1985 年 POSIX（IEEE  backing）写作“取交集”的过程——信号处理与作业控制取柏克莱、终端控制取 SVR3，并断言此后标准皆以 POSIX 为核、“唯一后补的内核 API 大项是 BSD sockets”。**这正是归名转换的机制句**：BSD 的贡献被写进“交集”与注语，接口本身此后不再带 BSD 名。第 2 处用于**自述文体的选材偏好与盲区**（1.7.4）：“then-unknown grad student”的创业叙事把机构背景（CSRG／DARPA 资助）压缩为个人出身。
- **立场披露（要紧）**：本书是 **BSD 阵营内部人（Raymond）的自述史**，同时是本书要分析的对象（1.7.4 的“自述文体”样本），不宜作为中立旁证；其年份与判断（如 “superior Berkeley signal handling”“only major addition … was BSD sockets”）是**评价性论断**，本批只用于证“该叙述如此写”，不据以断定技术优劣或标准化史的全部事实。另：同页的 longhairs／shorthairs 与 X 翼海报一段，与 ref3900（Kelty 转引 Raymond）为**同源二传**，本批不再落块。
- **文本处理披露**：HTML 抽取后连续空白并作单空格；链接锚文本（如 `Bill Joy`、`/usr/group standard`）两侧多余空格已并拢；此外逐字未改。
- **本批落点**：V35.1.3.1（第 1 处）、V35.1.7.4（第 2 处）
- **考据日期**：2026-11-16（Task 8.2 G4 V35 P2 批 b017；academic_work／L3，retrospective=1）
