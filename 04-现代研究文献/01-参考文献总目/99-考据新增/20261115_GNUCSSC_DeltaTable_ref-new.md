# GNU CSSC 手册“Delta Table”页（新 ref）引用卡

- **性质**：gnu.org 上 GNU CSSC 手册 5.2.2 节 “The Delta Table”；本机 Chrome UA curl 200
- **数据库**：新建 ref（2026-11-15 V34 P2 联网补证批 b002；source_url 四键查重无重合）
- **source_url**：https://www.gnu.org/software/cssc/manual/Delta-Table.html
- **quote（逐字，一处）**：
  1. The three numbers represent the numbers of lines inserted, deleted and unchanged in this version (with respect to its predecessor).
- **考据注**：该句解释 delta 表首行三个五位数字（形如 `^As 00001/00000/00010`）的含义——相对前一版的插入／删除／未改行数；**引文只取这一句**，前一句 “The first line introduces a new delta table entry and has the form…” 与前文 “Each entry describes one version stored in the history file…” 未取（若取，会把代码形态 `^As` 一并纳入，须逐字处理控制字符，风险高于收益）。与 File Format Overview 同一手册，故同样受 “It is not authoritative” 的口径限制
- **本批落点**：V34.2.7.1 第 2 块
- **考据日期**：2026-11-15（Task 8.2 G4 V34 P2 批 b002；official_doc／L3）
