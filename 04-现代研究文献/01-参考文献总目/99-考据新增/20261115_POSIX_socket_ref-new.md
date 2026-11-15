# POSIX.1-2017 `socket()` 函数页（新 ref）引用卡

- **性质**：pubs.opengroup.org 的 POSIX.1-2017（Issue 7）`socket()` 函数页；本机 Chrome UA curl 200、9,905 B（HTML），去标签后 4,656 字符
- **数据库**：新建 ref（2026-11-15 V34 P2 联网补证批 b017；source_url 四键查重：库内 pubs.opengroup.org 仅 `utilities/diff.html`（ref10684）与 `utilities/cmp.html`（ref10693）两页，另有 opengroup.org 根域与 `/unix`、`/trademarks` 三页；`functions/socket.html` 无重合）
- **source_url**：<https://pubs.opengroup.org/onlinepubs/9699919799/functions/socket.html>
- **quote（逐字，两处；行内 `<i>` 标记不计，折行按单空格）**：
  1. First released in Issue 6. Derived from the XNS, Issue 5.2 specification.
  2. The address families supported by the system are implementation-defined.
- **考据注**：第 1 句在 CHANGE HISTORY 段，是标准侧自陈的来处——`socket()` 迟至 Issue 6 才进入 POSIX 文本，且文本“取自 XNS, Issue 5.2 规范”，不是标准委员会自撰；用于 1.7.5 的“接口实践经既有规范进入标准文本”一档。**该页全文不出现 BSD 字样**（本地 grep `bsd` 命中 0），故标准文本不能直接证明 BSD 参与起草——文本缺席不可引，此点须在辨析中写明。第 2 句在 DESCRIPTION 段，给“接口固定、实现在后”的证据：地址族由各实现自定，故共同参考（标准）不承担来源归属的举证功能，用于 1.6.6
- **本批落点**：V34.1.6.6 第 1 块（第 2 句）；V34.1.7.5 第 2 块（第 1 句）
- **考据日期**：2026-11-15（Task 8.2 G4 V34 P2 批 b017；official_doc／L3）
