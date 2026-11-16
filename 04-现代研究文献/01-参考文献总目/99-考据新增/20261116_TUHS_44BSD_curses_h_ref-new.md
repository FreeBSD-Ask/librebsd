# 4.4BSD `lib/libcurses/curses.h`（新 ref）引用卡

- **性质**：4.4BSD 源码树 `usr/src/lib/libcurses/curses.h`（19,028 字节，TUHS 收录），curses 库的公开头文件
- **数据库**：新建 ref（2026-11-16 V35 P2 联网补证批 b010；source_url 查重：库内 `curses` 项下有 curses.3（ref10821）与 44doc 两件，但无 curses.h 本文件）
- **source_url**：<https://www.tuhs.org/cgi-bin/utree.pl?file=4.4BSD/usr/src/lib/libcurses/curses.h>
- **quote（逐字，文件头三行）**：

  ```text
  /*
   * Copyright (c) 1981, 1993
   *	The Regents of the University of California.  All rights reserved.
  ```

- **考据注**：本卡只用于一题——**库作者署名在各类文献中的可见程度**（3.5.5）的**档案侧下限**：4.4BSD 的 curses 头文件只有机构版权行（1981、1993 两个年份），无个人作者名。与 ref2696（Arnold 论文的标题页与“Ken Arnold 16 April 1986”手签）对置，可证同一库的署名在**文书层**与**代码档案层**并不一致：前者具名，后者只留机构。**不可证者**：本条不证“个人署名被有意抹去”——版权行归机构是当时 BSD 档案的通行格式，须与同类文件（同为 Regents 版权的其他 4.4BSD 文件）横向比较后方可推断制度性做法；本批只做单文件取样，制度性判断列待补。
- **载体披露**：TUHS 的 `utree.pl` 呈现页，正文取自 `<pre>` 段；源树原文件与呈现页内容一致（b013 批已就 curses.3 等同法核对路径）。
- **本批落点**：V35.3.5.5（第 2 行年份与机构名）
- **考据日期**：2026-11-16（Task 8.2 G4 V35 P2 批 b010；official_doc／L3）
