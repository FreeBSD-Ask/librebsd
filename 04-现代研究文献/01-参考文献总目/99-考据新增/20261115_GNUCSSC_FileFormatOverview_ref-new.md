# GNU CSSC 手册“File Format Overview”页（新 ref）引用卡

- **性质**：gnu.org 上 GNU CSSC（CSSC: Compatibly Stupid Source Control）手册 5.1 节 “File Format Overview”；本机 Chrome UA curl 200、1.6 KB 级页面
- **数据库**：新建 ref（2026-11-15 V34 P2 联网补证批 b002；source_url 四键查重无重合，库内 gnu.org/software/cssc 零命中）
- **source_url**：https://www.gnu.org/software/cssc/manual/File-Format-Overview.html
- **quote（逐字，一处）**：
  1. An sccs file contains two parts, the header and the body. The header contains information about both the file as a whole and also information about each version stored in the file. After this comes the body itself, which is a stream of fragments from the controlled file interspersed with control information which indicates which versions these fragments appear in.
- **考据注**：**口径提醒**：CSSC 手册 “File Format” 章开篇自我声明 “It is not authoritative, and may not match some of the peculiarities of your vendor's implementation.”，且 The Body 一节公开承认作者对 ‘^AI’／‘^AE’／‘^AD’ 控制行的交互“no clear understanding”。故该 ref 只用于**结构层描述**（头／体二分、片段＋控制行），不用于判例级断言；具体字节格式须回核原始 SCCS 实现或 POSIX 文本
- **本批落点**：V34.2.7.1 第 1 块
- **考据日期**：2026-11-15（Task 8.2 G4 V34 P2 批 b002；official_doc／L3）
