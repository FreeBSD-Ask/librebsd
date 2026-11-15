# POSIX `diff` 规范页（新 ref）引用卡

- **性质**：pubs.opengroup.org 的 POSIX.1-2017（Issue 7, 2018 edition）`diff` 工具页；本机 Chrome UA curl 200、33,988 B
- **数据库**：新建 ref（2026-11-15 V34 P2 联网补证批 b006；source_url 四键查重：库内 pubs.opengroup.org 仅 `SRC-mat:9181`（整套 2018 版根地址），本页 `/utilities/diff.html` 无重合）
- **source_url**：https://pubs.opengroup.org/onlinepubs/9699919799/utilities/diff.html
- **quote（逐字，三处；行内 `<i>`／`<b>` 标记不计入，折行按单空格）**：
  1. The diff utility shall compare the contents of file1 and file2 and write to standard output a list of changes necessary to convert file1 into file2.
  2. This list should be minimal.
  3. Cause any amount of white space at the end of a line to be treated as a single <newline> (that is, the white-space characters preceding the <newline> are ignored) and other strings of white-space characters, not including <newline> characters, to compare equal.
- **考据注**：第 1、2 句给“输出定义＋最小性”，是 2.2.2 度量口径的制度源头（相似＝最少变更量）；第 3 句是 `-b` 选项说明，露出的比对单位是“行＋换行”而非字节流，用于 2.2.1。**格式提醒**：第 1 句原文在 `file2` 与句号之间无空格（`<i>file2</i>.`），标签替换为空格再读会造出“file2 .”的伪空格，校验时须按渲染文本比对；`<newline>` 在原文是 `&lt;newline&gt;` 转义，渲染后为尖括号形态，照录。第 2 句、第 3 句未在库内其他批次用过
- **本批落点**：V34.2.2.1 第 1、2 块；V34.2.2.2 第 1、2 块
- **考据日期**：2026-11-15（Task 8.2 G4 V34 P2 批 b006；official_doc／L3）
