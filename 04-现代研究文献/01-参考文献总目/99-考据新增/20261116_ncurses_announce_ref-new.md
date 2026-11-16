# ncurses 公告与总览页（新 ref）引用卡

- **性质**：ncurses 项目官方公告／总览页 `announce.html`（48,630 字节，invisible-island.net），含库的定位声明、1995 年交接事件、跨系统采用面与作者分工
- **数据库**：新建 ref（2026-11-16 V35 P2 联网补证批 b010；source_url 四键查重：库内 `ncurses` 仅有 ref5817（DKC 迁移件、无 `source_url`），与本 URL 不同源可核，故新建）
- **source_url**：<https://invisible-island.net/ncurses/announce.html>
- **quote（逐字，两处，分落两块；另附一处备用引文，本批未落块）**：
  1. The ncurses (new curses) library is a free software emulation of curses in System V Release 4.0 (SVr4), and more. It uses terminfo format, supports pads and color and multiple highlights and forms characters and function-key mapping, and has all the other SVr4-curses enhancements over BSD curses.
  2. In mid-June 1995, the maintainer of 4.4BSD curses declared that he considered 4.4BSD curses obsolete, and encouraged the keepers of unix releases such as BSD/OS, FreeBSD and NetBSD to switch over to ncurses.
  3.（备用，未落块）Zeyd Ben-Halim started ncurses from a previous package pcurses, written by Pavel Curtis. Eric S. Raymond continued development. Jürgen Pfeifer wrote most of the form and menu libraries. Ongoing development work is done by Thomas E. Dickey. Thomas E. Dickey has acted as the maintainer for the Free Software Foundation, which held a copyright on ncurses for releases 4.2 through 6.1.
- **考据注**：第 1 句是**双源结构的 SVr4 侧自述**（3.5.1）：仿效对象明写 SVr4，并以“BSD curses 的增强”为参照。第 2 句是**交接声明**（3.5.3）：时间（1995 年 6 月中）、主体（4.4BSD curses 的维护者）、动作（自认过时并劝三家改用）三要素俱全，但**未点维护者姓名**——姓名须另核（列待补）。第 3 处（备用）为**作者分工链**：Ben-Halim／Curtis／Raymond／Pfeifer／Dickey 与 FSF 版权归属逐条列出，本批未落块，留待 3.5.5 的另一问（现代项目页的逐人分工）时启用。**立场披露（要紧）**：本页是 ncurses 项目**自述**，其“SVr4 优先”的定位与“BSD curses 已过时”的判断均出自承接方一侧，不当中立第三方评估；BSD 侧的对应文书另见 ref2696、ref10821 与本批新建的 4.4BSD curses.h（ref10859）。**载体披露**：页面为活文档，抓取时点 2026-11-16，措辞与姓名表可能随版本更新。
- **文本处理披露**：HTML 抽取后连续空白与换行并作单空格，链接边界造成的句内多余空格（如 “switch over to ncurses .”）已并拢；此外逐字未改。
- **本批落点**：V35.3.5.1（第 1 句）、V35.3.5.3（第 2 句）
- **考据日期**：2026-11-16（Task 8.2 G4 V35 P2 批 b010；official_doc／L3）
