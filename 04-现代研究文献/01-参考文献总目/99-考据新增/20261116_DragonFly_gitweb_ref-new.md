# gitweb.dragonflybsd.org 项目列表页（新 ref）引用卡

- **性质**：gitweb 项目总列表（List all projects，各库一行：描述／Owner／Last Change）；curl 实抓 2026-11-16（HTTP 200，8 396 B）
- **数据库**：新建 ref（supp-V75-b016；四键查重：库内该 URL 0 条）
- **source_url**：<https://gitweb.dragonflybsd.org/>
- **quote（逐字四处）**：
  1. List all projects Project Description Owner Last Change
  2. dragonfly.git DragonFly Project Source Fred
  3. freebsd.git FreeBSD Project Source
  4. linux.git Linux Project Source (from...
- **考据注**：第 1 处为全列表的列头；第 2 处为主源库（dragonfly.git，描述 DragonFly Project Source，Owner Fred）；第 3—4 处为上游镜像库（freebsd.git、linux.git）——仓库构成全貌不止本项目源，镜像库与 ports 系（dports.git／deltaports.git／ravenports.git）同列一表。库内 dragonfly.duckdb 现算 commits 656,207（2003-06-17→2026-08-18）作量侧互证。
- **本批落点**：V75.2.5.1 两块（D2 ref-new#url／#2）
- **考据日期**：2026-11-16（supp-V75-b016；official_doc／L3）

## supp-V75-b021 追加（2.10.2 一块）

- **追加引文（逐字两处）**：
  1. dragonfly.git DragonFly Project Source Fred
  2. dports.git DragonFly DPorts Source Fred
- **追加考据注**：项目总表每库一行四格（库名／描述／Owner／Last Change），第 1—2 处为主源库与 DPorts 包库两行——同一 gitweb 服务下分库管理，包库不入源库树。Last Change 列为相对时间（抓取时为 3 days ago），不入引。库内 dragonfly.duckdb 三库（src 49,379／dports 606,813／docs 15）与表列之名一一对应，可互校。
- **本批落点**：V75.2.10.2 一块（#url）
- **考据日期**：2026-11-16（supp-V75-b021）
