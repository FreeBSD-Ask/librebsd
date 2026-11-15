# Linux 0.01 发布说明“RELNOTES-0.01”（新 ref）引用卡

- **性质**：kernel.org 的 `Historic/old-versions/RELNOTES-0.01` 纯文本（Linux 0.01 发布说明，作者自撰）；本机 Chrome UA curl 200、10,823 B
- **数据库**：新建 ref（2026-11-15 V34 P2 联网补证批 b004；source_url 四键查重：库内 kernel.org 无此件命中）
- **source_url**：https://www.kernel.org/pub/linux/kernel/Historic/old-versions/RELNOTES-0.01
- **quote（逐字，三处，硬折行与制表符按渲染口径归一为单空格）**：
  1. This is a free minix-like kernel for i386(+) based AT-machines.
  2. Minix was written on a 8088, and later ported to other machines - linux takes full advantage of the 386 (which is nice if you /have/ a 386, but makes porting very difficult)
  3. Currently only a subset of AT-hardware is supported (hard-disk, screen, keyboard and serial lines), and some of the system calls are not yet fully implemented (notably mount/umount aren't even implemented).
- **考据注**：三句分工——第 1 句是作者对自身作品的定性（“minix-like”，面向 i386(+) 的 AT 机器），可作 1.5.5“声明”一侧；第 2 句把 Minix 与 Linux 的机器世代与移植代价摊开（Minix 起于 8088 再移植，Linux 直接吃满 386），可作 1.6.1 的架构层面；第 3 句给 0.01 的硬件与系统调用覆盖面（仅支持 AT 硬件子集、mount/umount 未实现），本批未用，留给 1.5.x 其余题。**格式说明**：原文为纯文本、按 76 列硬折行并含制表符缩进，引文按渲染口径把折行与制表符归一为单空格；`/have/` 的斜杠强调为原文所有，照录。**证据等级**：作者自撰发布说明属当事人一手（L4），宿主为 kernel.org 官方归档
- **本批落点**：V34.1.5.5 第 1 块；V34.1.6.1 第 1 块
- **考据日期**：2026-11-15（Task 8.2 G4 V34 P2 批 b004；official_doc／L4）
