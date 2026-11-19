# FreeBSD 1.0-RELEASE `packages/README` 引用卡

- **性质**：FreeBSD 1.0-RELEASE 发行树 `packages/README` 纯文本（2,139 字节），取自 FreeBSD 官方档案 archive.freebsd.org（预打包应用集说明，头部标注 pkg_install.tgz 最后更改 1993-10-10）
- **数据库**：新建 ref（2026-11-20 V36 P2 联网补证批 b006；source_url 四键查重：库内无 1.0-RELEASE packages/README 条目）
- **source_url**：<https://archive.freebsd.org/old-releases/i386/1.0-RELEASE/packages/README>
- **quote（逐字两处）**：
  1. “This directory contains pre-packaged software for use with FreeBSD.”（首句）
  2. “Package names ending in *_bin.tgz are prebuilt binary packages, and generally install into /usr/local or /usr/gnu by default.  Package names ending in *_src.tgz are full source releases, which will install in /usr/ports by default.”（双轨说明；原文跨行断词按原样保留）
- **考据注**：第 1 处是**应用包体系自述**：1.0 发行树原生含预打包应用目录（bin／src 双轨＋pkg_add 安装套件）——1.x 的应用供给层形态自证。第 2 处的 **/usr/ports 安装点**是 ports 体系的发行层雏形记述（1.0 时代 packages 体系内）；1.1 版沿此形态扩张的逐项增量清单因 1.1-RELEASE 未入官方归档（archive.freebsd.org i386 目录仅存 1.0）暂缺一手逐字证，本块证“应用清单层存在与双轨形态”，1.1 增量面留待一手发现后另批补证（不以没查到写不存在）。
- **本批落点**：V36.1.6.3 第 1 块（两处连用）
- **考据日期**：2026-11-20（Task 8.2 G4 全责线 V36 P2 批 b006；official_doc／L3）
