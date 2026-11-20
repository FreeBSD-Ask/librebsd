# FreeBSD 2.0.5-RELEASE `INSTALL` 引用卡

- **性质**：FreeBSD 2.0.5-RELEASE 发行树顶层 `INSTALL` 纯文本（20,020 字节），取自 FreeBSD 官方档案 archive.freebsd.org（安装指南；内含目录节 2.1—2.5.2 介质清单与 §3 Installing FreeBSD 排障段）
- **数据库**：新建 ref（2026-11-21 V36 P2 联网补证批 b013；source_url 四键查重：库内无 2.0.5-RELEASE INSTALL 条目）
- **source_url**：<https://archive.freebsd.org/old-releases/i386/2.0.5-RELEASE/INSTALL>
- **quote（逐字两处；原文缩进与行断按原样保留）**：
  1. `        2.1     Before installing from CDROM`…`                2.5.2   Preparing for FTP Installation`（目录节介质清单七行连续：CDROM／Floppy／DOS 分区／QIC/SCSI tape／网络（NFS/FTP））
  2. “If you're having hardware trouble, or FreeBSD refuses to boot at all, read the Hardware Guide provided on the boot floppy for a list of possible solutions.”（§3 排障段；原文跨行断词按原样保留）
- **考据注**：第 1 处是**安装介质路径的官方清单**：磁带（QIC/SCSI）／光盘／软盘／DOS 分区／网络（NFS、FTP）五路介质并列——介质路径决定部署场景，发行层自述。第 2 处是**引导盘排障设计**：硬件故障或无法引导时“读引导软盘内附的 Hardware Guide 求可能解”——安装失败的自助处置被纳入发行件本体（引导盘附文档）。**年代披露**：随 2.0.5-RELEASE（1995-06）发行，2.x 时代原生文档。
- **本批落点**：V36.2.5.1 第 1 块（第 1 处）、V36.2.5.3 第 1 块（第 2 处）
- **考据日期**：2026-11-21（Task 8.2 G4 全责线 V36 P2 批 b013；official_doc／L3）
