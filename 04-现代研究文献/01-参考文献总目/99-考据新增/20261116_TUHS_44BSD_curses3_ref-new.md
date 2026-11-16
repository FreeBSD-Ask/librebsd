# 4.4BSD `lib/libcurses/curses.3`（新 ref）引用卡

- **性质**：4.4BSD `usr/src/lib/libcurses/curses.3` 手册页源（roff），取自 TUHS utree（6,006 字节正文；`@(#)curses.3 8.1 (Berkeley) 6/4/93`，`.Dd June 4, 1993`，作者 Ken Arnold）
- **数据库**：新建 ref（2026-11-16 V31 P2 联网补证批 b016；source_url 四键查重：库内 TUHS 条目无 `curses.3`）
- **source_url**：<https://www.tuhs.org/cgi-bin/utree.pl?file=4.4BSD/usr/src/lib/libcurses/curses.3>
- **quote（逐字，两处，分落两块）**：
  1. These routines give the user a method of updating screens with reasonable optimization.  They keep an image of the current screen, and the user sets up an image of a new one.（DESCRIPTION 首两段）
  2. .Xr termcap 5（SEE ALSO 中的交叉引用行，roff 源原样）
- **考据注**：第 1 句同时供两处使用：前半句是 curses 的定位（更新屏幕并求合理优化），后半句是**窗口形态的记载方式**——“保存当前屏幕的一幅图像，用户另立一幅新图像”，屏幕以图像而非字符流为单位，6.4.6 据此。第 2 句是**叠层的书面痕迹**：手册页 SEE ALSO 只指向 `termcap 5`（终端描述文件的格式页），说明 curses 把终端差异下推给描述文件层，6.4.4 与 termcap.3 一块合看。**roff 披露**：第 2 句直接引 roff 源行（`.Xr termcap 5`），未作渲染改写；第 1 句按行序并句、双空格照录。**同页另载** Ken Arnold 的论文条目 “Screen Updating and Cursor Movement Optimization: A Library Package”，可作 6.4 诸节的文献线索。
- **本批落点**：V31.6.4.4 第 2 块（第 2 句）、V31.6.4.6 第 1 块（第 1 句后半两句子）
- **考据日期**：2026-11-16（Task 8.2 G4 V31 P2 批 b016；official_doc／L3）
