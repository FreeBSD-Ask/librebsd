# ncurses FAQ（新 ref）引用卡

- **性质**：ncurses 项目 FAQ 页 `ncurses.faq.html`（341,915 字节，invisible-island.net），含 pcurses→ncurses 源流、库名由来与维护者自述
- **数据库**：新建 ref（2026-11-16 V35 P2 联网补证批 b010；source_url 查重：库内无该 URL，`ncurses` 项下仅 ref5817 迁移件）
- **source_url**：<https://invisible-island.net/ncurses/ncurses.faq.html>
- **quote（逐字，两处，分落两块）**：
  1. While the name of the library itself comes from “pcurses”, it had a different connotation to Curtis. His makefile built libncurses.a (normal) and libdcurses.a (debugging). In the documentation, Curtis referred to his package as “the new curses” like this, in changes.ms:
  2. Rather than being at the start a replacement for AT&T curses, initially it was an extension of BSD curses. Later, supplanting AT&T curses became more important, with different developers.
- **考据注**：第 1 处是**命名惯例的实物线索**（3.5.4）：库名“ncurses”可追到 pcurses 的 `libncurses.a`／`libdcurses.a` 两个构建目标，Curtis 自用“the new curses”一称——归名不在宣言中，而在构建产物与文档标题里。第 2 处是**承接时序与意图的自述**（3.5.3）：起初是 BSD curses 的扩展，后转为取代 AT&T curses，且“换了开发者”。**立场披露**：FAQ 由现任维护者撰写并含大量第一人称追述（“I've done most of the configuration work”），属**事后自述**；本卡两处引文所载事件（1993—1995）与撰述时点相隔近三十年，须与同期文书（announce 页、4.4BSD 源码）分判。**异说并列**：本页称 pcurses “apparently developed on a 4.3BSD system, at Cornell”，用语为推测（apparently），本批不据此断言其开发环境。
- **文本处理披露**：HTML 抽取后连续空白并作单空格；行内链接造成的空格（如 “pcurses , written”）已并拢；此外逐字未改。
- **本批落点**：V35.3.5.3（第 2 处）、V35.3.5.4（第 1 处）
- **考据日期**：2026-11-16（Task 8.2 G4 V35 P2 批 b010；official_doc／L3，retrospective=1）
