# DragonFly BSD `standards(7)`（新 ref）引用卡

- **性质**：DragonFly 源码树 `share/man/man7/standards.7`（roff 源，4,838 B）；本机 sparse checkout 副本与上游 blob 逐字节相同（`gitweb.dragonflybsd.org` blob_plain 取回 4,656 B 经比对 `== True`；Anubis 只放行 `Wget/1.21` UA，Chrome UA 得“not a bot”页）
- **数据库**：新建 ref（2026-11-15 V34 P2 联网补证批 b017；source_url 四键查重：库内 `gitweb.dragonflybsd.org` 0 条，man 页类现有条目均为本机仓库路径或 PDF，`standards.7` 无重合）
- **source_url**：<https://gitweb.dragonflybsd.org/dragonfly.git/blob_plain/HEAD:/share/man/man7/standards.7>
- **quote（逐字一处）**：The value of the _POSIX_C_SOURCE macro determines which POSIX standard the programming environment conforms to.
- **考据注**：此句在 `Ss POSIX Standards (_POSIX_C_SOURCE)` 节，说的是实现侧的机制——由特性测试宏取值决定“编程环境符合哪个 POSIX 标准”。**逐字按渲染形记**：源文件用 `.Dv _POSIX_C_SOURCE` 与 `.Tn POSIX` 两个 roff 宏，渲染后即上引文字，宏本身不计入引文。用于 1.7.5 的后半档“标准又反过来约束各实现”——这是实现方（BSD 系统）自己的文档对依循方式的陈述，不是标准方的要求
- **本批落点**：V34.1.7.5 第 3 块
- **考据日期**：2026-11-15（Task 8.2 G4 V34 P2 批 b017；official_doc／L3）
