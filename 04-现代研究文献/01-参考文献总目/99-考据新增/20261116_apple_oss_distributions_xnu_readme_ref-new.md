# XNU kernel README（apple-oss-distributions/xnu）（新 ref）引用卡

- **性质**：GitHub 官方镜像 apple-oss-distributions/xnu 的 README.md（raw 取原文）；curl 实抓 2026-11-16（HTTP 200，22 122 B）
- **数据库**：新建 ref（supp-V75-b020；四键查重：库内该 URL 0 条）
- **source_url**：<https://raw.githubusercontent.com/apple-oss-distributions/xnu/main/README.md>
- **quote（逐字五处）**：
  1. XNU kernel is part of the Darwin operating system for use in macOS and iOS operating systems. XNU is an acronym for X is Not Unix.
  2. XNU is a hybrid kernel combining the Mach kernel developed at Carnegie Mellon University with components from FreeBSD and a C++ API for writing drivers called IOKit.
  3. `bsd` - BSD subsystems code
  4. `osfmk` - Mach kernel based subsystems
  5. `EXTERNAL_HEADERS` - Headers sourced from other projects to avoid dependency cycles when building. These headers should be regularly synced when source is updated.
- **考据注**：第 1 处为题下首段（XNU 属 Darwin、用于 macOS 与 iOS，名称缩写 X is Not Unix）；第 2 处同段给出成分指认（CMU 的 Mach＋FreeBSD 组件＋IOKit 的 C++ 驱动 API）；第 3—4 处为 The XNU Source Tree 表的 bsd 与 osfmk 两行（目录与职责对照）；第 5 处为同表 EXTERNAL_HEADERS 行（外部项目头文件与定期同步要求）。库内存疑 1317（resolved，第 12 卷语境）曾以 github.com/apple-oss-distributions/xnu 一手核验同一“combining … with components from FreeBSD”措辞，并附 touch.c／ls.c／top.c 含 FreeBSD 版权头与 __FBSDID 的证据——本批抓取原文入卡，与既有考据互证。README 另载构建（DEVELOPMENT 内核）、版本与许可各节。
- **本批落点**：V75.2.9.3 两块（#url／#2）＋V75.2.9.4 两块（#url／#2）
- **考据日期**：2026-11-16（supp-V75-b020；official_doc／L3）
