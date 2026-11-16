# 源树顶层 README（dragonfly.git README）（新 ref）引用卡

- **性质**：dragonfly.git 顶层 README 原文（blob_plain）；curl 实抓 2026-11-16（HTTP 200，2 569 B）
- **数据库**：新建 ref（supp-V75-b018；四键查重：库内该 URL 0 条）
- **source_url**：<https://gitweb.dragonflybsd.org/dragonfly.git/blob_plain/HEAD:/README>
- **quote（逐字四处）**：
  1. This is the top level of the DragonFly source directory.
  2. Source Roadmap:
  3. sys Kernel sources.
  4. The file LINT64 contains entries for all possible devices, not just those commonly used, and is meant more as a general reference than an actual kernel configuration file
- **考据注**：README 自述为源树顶层并给构建目标（buildworld／installworld 等），后列 Source Roadmap 逐目录职责（第 3 处取 sys 行：内核源码）；第 4 处为 LINT64 的定位——只作通用参考、非可运行配置，故读 README 即可知“哪些文件是配置、哪些只是参考”。原文 LINT64 句后半有括注（a kernel built from it wouldn…），含直撇号，引文截取其前段。
- **本批落点**：V75.2.7.4 两块（D2 ref-new#url／#2）
- **考据日期**：2026-11-16（supp-V75-b018；official_doc／L3）
