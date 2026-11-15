# POSIX `cmp` 规范页（新 ref）引用卡

- **性质**：pubs.opengroup.org 的 POSIX.1-2017（Issue 7）`cmp` 工具页；本机 Chrome UA curl 200、13,994 B
- **数据库**：新建 ref（2026-11-15 V34 P2 联网补证批 b014；source_url 四键查重：库内 pubs.opengroup.org 有 2018 版根地址与 `utilities/diff.html`，`utilities/cmp.html` 无重合）
- **source_url**：https://pubs.opengroup.org/onlinepubs/9699919799/utilities/cmp.html
- **quote（逐字，三处；行内 `<i>` 标记不计，折行按单空格）**：
  1. The cmp utility shall compare two files. The cmp utility shall write no output if the files are the same.
  2. Under default options, if they differ, it shall write to standard output the byte and line number at which the first difference occurred.
  3. The input files can be any file type.
- **考据注**：第 1 句给二值阈值（相同即无输出），第 2 句给差异定位（报首个差异所在的字节号与行号），两句合起来是 2.3.1“逐字相同的判定阈值”的规范依据；第 3 句（INPUT FILES 段）给适用范围——**输入可以是任何文件类型**，与 diff 的行语义相对，用于 2.3.6。**与 2.2.x 的分工**：diff 页（ref10684）管“行级变更清单与最小性”，cmp 页管“字节级全同与首个差异”，两页不可互替
- **本批落点**：V34.2.3.1 第 1、2 块；V34.2.3.6 第 1 块
- **考据日期**：2026-11-15（Task 8.2 G4 V34 P2 批 b014；official_doc／L3）
