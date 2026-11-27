# Linux 0.01 源码包（kernel.org Historic）（新 ref）引用卡

- **性质**：kernel.org `/pub/linux/kernel/Historic/linux-0.01.tar.gz`（gzip tar，73,091 B；Chrome UA curl 200，2026-11-27 实抓）；包内 100 项，62 个文件 mtime=1991-09-17，最早源文件 mtime=1991-06-15。
- **数据库**：新建 ref（supp-V18-b001；source_url 四键查重：库内 kernel.org 现有 RELNOTES-0.01（10682）、早期帖汇编（10683）、Historic 目录页（10880）三件，本 tar URL 0 条）。
- **source_url**：https://www.kernel.org/pub/linux/kernel/Historic/linux-0.01.tar.gz
- **quote（逐字／实测，六处）**：

1. `(C) 1991 Linus Torvalds`（linux/include/string.h 第 23 行注释）
2. `(same as minix, so we can use the minix`（linux/include/linux/fs.h 第 10 行注释，下接 file system…）
3. `#define MINIX_HEADER 32`（linux/tools/build.c 第 6 行）
4. `62 个文件 mtime=1991-09-17（本机解包实测，2026-11-27）`
5. `包内 100 项、73,091 B（本机实测，2026-11-27）`
6. `最早源文件 mtime=1991-06-15（linux/boot/boot.s 等，本机解包实测）`

- **考据注**：包体为 1991-09-17 打包、1993-10-30 归档于 kernel.org Historic 的 0.01 源码（100 项、73,091 B）。四条源码引文分工：`string.h` 版权行供许可史（1.4.x）；`fs.h` 设备号注记供新旧系统边界（1.2.5）；`build.c` 的 MINIX_HEADER 供引导兼容（后续批次）；mtime 组供首发时点（1.1.2／1.3.1）与存世档案（1.3.5）。**mtime 语义限定**：tar 内时间戳是打包时源文件的修改时间，不等于各文件写作时点；本批只以 1991-09-17 作为“打包／首发日”的物证，最早 1991-06-15 只作“年内已有源码”的下界，不推具体起笔日。包内无 COPYING／README 文件，许可条件以 RELNOTES-0.01 与源码零星版权行为据。
- **证据等级**：源码本体属当事人一手（L4），宿主为 kernel.org 官方归档。
- **本批落点**：V18.1.1.1／1.1.2／1.2.5／1.3.1／1.3.5（supp-V18-b001）
- **考据日期**：2026-11-27（supp-V18-b001；primary／L4）

## 批内追加实测（supp-V18-b002，2026-11-27）

1. `包内源文件合计 10,239 行（本机统计：C 5,929／H 2,484／汇编 1,464／其他 362）`
2. `顶层目录：boot、fs、include、init、kernel、lib、mm、tools 与 Makefile（本机列包实测）`

落点：V18.1.3.2（supp-V18-b002）。
