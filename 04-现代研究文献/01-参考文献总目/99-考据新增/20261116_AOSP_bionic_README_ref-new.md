# Android bionic `README.md`（新 ref）引用卡

- **性质**：Android C 库 bionic 的维护者总览 `README.md`（21,546 字节），取自 GitHub 上的 AOSP 镜像 `aosp-mirror/platform_bionic`（原生 `android.googlesource.com` 本机不可达，连接超时）
- **数据库**：新建 ref（2026-11-16 V35 P2 联网补证批 b005；source_url 四键查重＋规范化 URL：库内无该文件）
- **source_url**：<https://raw.githubusercontent.com/aosp-mirror/platform_bionic/main/README.md>
- **quote（逐字，四处，分落四块）**：
  1. dns/ … Contains the DNS resolver (originates from NetBSD code).
  2. These directories contain upstream source with no local changes.  Any time we can just use a BSD implementation of something unmodified, we should.
  3. upstream-freebsd/ / upstream-netbsd/ / upstream-openbsd/（目录清单，原文分行）
  4. The C++ files are files we own, typically because the Linux kernel interface is sufficiently different that we can't use any of the BSD implementations.
- **考据注**：第 1 句是**混合渊源的具体例**：DNS 解析器“源自 NetBSD 代码”而存于 Linux 系统的 C 库内——2.2.1。第 2 句是**上游留存政策**：这些目录“存无本地改动的上游源码”“能用未经改动的 BSD 实现就用”——2.2.2。第 3 处是**目录学证据**：三个上游目录并置，把“三大 BSD 源流”写进路径——2.2.5。第 4 句是**归名边界**：自研部分（C++ 文件）以“内核接口差异”为理由，不借 BSD 实现——2.2.6 的个案参照意义据此。**载体披露（要紧）**：原生 googlesource 不可达，本卡用 AOSP 的 GitHub 镜像**同文件**；镜像与原生若有版本差，须以提交哈希另核（本轮未取哈希，列待补）。**同源披露**：四块同出一份 README，各问不同（例证／政策／目录／边界），互为同调而非独立佐证。**许可披露**：本卡不据 README 论断 bionic 的许可隔离层设计（2.2.3），该题须另取 NOTICE 与 build 规则文件。
- **本批落点**：V35.2.2.1（第 1 句）、V35.2.2.2（第 2 句）、V35.2.2.5（第 3 处）、V35.2.2.6（第 4 句）
- **考据日期**：2026-11-16（Task 8.2 G4 V35 P2 批 b005；official_doc／L3）
