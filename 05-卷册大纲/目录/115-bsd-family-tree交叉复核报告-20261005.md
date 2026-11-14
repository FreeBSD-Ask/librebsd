# 115｜bsd-family-tree.txt 与本地大纲/数据库差异交叉复核报告（2026-10-05）

> **性质**：**分析报告**。本件不改内容层；发现差异供 ykla 裁定。
> **比对文件**：`bsd-family-tree.txt`（1028 行，含 ASCII 谱系图＋版本发行日期时间线＋文献目录）
> **现跑口径**：53 卷 447 章 3,635 节／@@ 825。

---

## 一、文件结构

| 区段 | 行 | 内容 |
| ---- | -- | ---- |
| ASCII 谱系图 | 1–~600 | V1→V10→1BSD→2BSD→3BSD→4.xBSD→Net/1→Net/2→386BSD/BSD/386→四大主干→2026 |
| 发行日期时间线 | ~600–~900 | 每一版本的精确发布日期（约 200+ 条） |
| 文献目录 | ~900—1028 | McKusick 等权威文献列表 |

---

## 二、重大差异（按严重度排序）

### ★1｜FreeBSD 1.0 日期矛盾（需订正本会话误改）

| 来源 | FreeBSD 1.0 日期 |
| ---- | ---------------- |
| bsd-family-tree.txt | **1993-11-01** [FBD] |
| 本会话 id=2199 修订 | ~~1993-12~~（**误改**） |
| CSDN Unix 简史 | 1993 年 12 月 |
| 铁证 | **FBD 标注来源为 FreeBSD 官方发布记录**——1993-11-01 可信度最高 |

**结论**：FreeBSD 1.0 发布日为 **1993-11-01**（本会话 id=2199 中将 1993-11 改为 1993-12 的"订正"本身是错误的——b-family-tree.txt [FBD] 标注来源优先级高于 CSDN 等二手来源）。需回改。

### ★2｜版本粒度差距（系统性差异）

| 主干 | bsd-family-tree.txt 记载的版本数 | 大纲中承载的版本数 |
| ---- | -------------------------------- | ------------------ |
| FreeBSD | 1.0→15.1 约 **70+ 个版本**（含全部 point release） | 约 **15 个主要里程碑**（卷 20/21） |
| NetBSD | 0.8→11.0 约 **40+ 个版本** | 约 **12 个主要里程碑**（卷 23/24） |
| OpenBSD | 2.0→7.9 约 **30+ 个版本** | 约 **10 个主要里程碑**（卷 26/27） |
| DragonFly | 1.0→6.4.2 约 **25+ 个版本** | 约 **8 个主要里程碑**（卷 29/30） |
| BSD/386→BSD/OS | 0.3.1→5.1 约 **18 个版本** | 约 **4 个主要里程碑**（卷 11 ch2） |
| 2BSD 线 | 2.79→2.11 rev#430 约 **10 个版本** | 卷 7 ch1 概述 |

**差异性质**：bs d-family-tree.txt 按 point release 级别完整列出；大纲按叙事里程碑概括——**不是错误，是体例差异**。大纲无需逐一列出 point release，但主要版本（x.0/x.1 级别）的日期可比照核证。

### ★3｜大纲中缺失的系统/版本（真缺口）

| 系统/版本 | bsd-family-tree.txt 记载 | 大纲承载 |
| --------- | ------------------------ | -------- |
| FreeBSD 1.0.2 | 1993-11-14 | ✗ 无 |
| FreeBSD 1.1.5.1 | 1994-07-05 | ✗ 无 |
| FreeBSD 2.1.7.1 | — | ✗ 无 |
| FreeBSD 2.2.9 → 3.0 | 1998-10→1998-10-27 | ✗ 无 |
| FreeBSD 4.11 → 5.0 | 2005→2006 | 承载于卷 20 但版本号未到 4.11 粒度 |
| NetBSD 1.3.1—1.3.3 | 1998 | ✗ 无 |
| NetBSD 1.4.1—1.4.3 | 1999—2000 | ✗ 无 |
| OpenBSD 2.1—2.9 | 1997—2001 | 承载于卷 26 但中间版本未逐版列出 |
| BSD/386 0.3.3 | 1992-06（首个 CDROM 版） | ✗ 无 |
| BSD/386 0.9.3/0.9.4 | 1992-10/12 | ✗ 无 |
| DragonFly 1.2—6.4.2 中间版 | 2004—2025 | 承载于卷 29/30 但中间版本未逐版列出 |

### ★4｜日期精确性核证（bsd-family-tree.txt vs 大纲中已有记载）

| 系统/版本 | family-tree 日期 | 大纲当前 | 状态 |
| --------- | ---------------- | -------- | ---- |
| 386BSD 0.0 | 1992-02 | 两说并陈（2 月/3-17/3-12） | ✓ 一致（三说） |
| 386BSD 0.1 | 1992-07-28 | 1992-07-14（实际是 0.1） | ⚠ 需核（0.1 日期两说：07-14 vs 07-28） |
| NetBSD 0.8 | 1993-04-20 | 1993-04 | ✓ 一致 |
| FreeBSD 1.0 | 1993-11-01 | ~~1993-12~~（本会话误改） | ❌ 需回改 1993-11 |
| 4.4BSD | 1993-06-01 | 1994-06 | ⚠ 差异——tree 载 1993-06-01，但 4.4BSD 一般认为 1994 年发布；可能 tree 载的是 Alpha 版 |
| 4.4BSD-Lite | 1994-03-01 | 1994（两说 4 月/6 月） | ✓ 大体一致 |
| FreeBSD 2.0 | 1994-11-23 | — | 本卷卷 14/20 承载 |
| 4.4BSD-Lite Release 2 | 1995-06 | 1995-06 | ✓ 一致 |
| NetBSD 1.0 | 1994-10-26 | 1994-10 | ✓ 一致 |
| OpenBSD 2.0 | 1996-10-18 | 1995-10-18（分叉日）/ 1996-07（首版 1.2） | ⚠ 需分清：分叉日 vs 首版日 |
| macOS 26 | 2025-09-15 | — | 本卷卷 36 承载 |

### ★5｜2BSD 线（PDP-11）版本年表

| 版本 | 年 | 大纲承载 |
| ---- | -- | -------- |
| 2.79BSD | 1980 | 卷 7 ch1 |
| 2.8BSD | 1983 | 卷 7 ch1 |
| 2.9BSD | 1983 | 卷 7 ch1 |
| 2.9BSD-Seismo | 1984 | ✗ |
| 2.10BSD | 1987 | 卷 7 ch1 |
| 2.10.1BSD | 1987 | ✗ |
| 2.11BSD | 1988 | 卷 7 ch1 |
| 2.11BSD rev #430 | 1992 | ✗ |

### ★6｜大纲未覆盖的 bsd-family-tree.txt 中其他项目

| 项目 | 备注 |
| ---- | ---- |
| PicoBSD | FreeBSD 软盘精简版 |
| FreeSBIE | FreeBSD Live CD |
| ClosedBSD | 防火墙/NAT |
| m0n0wall | FreeBSD 防火墙（→ pfSense 前身） |
| Debian GNU/kFreeBSD | Debian × FreeBSD 内核 |
| Debian GNU/NetBSD | Debian × NetBSD |
| Gentoo/FreeBSD、Gentoo/OpenBSD、Gentoo/NetBSD | Gentoo 框架移植 |
| Nokia IPSO | FreeBSD 基防火墙设备 |
| Isilon OneFS | FreeBSD 基集群存储 |
| NetApp Data ONTAP | FreeBSD 基存储 |
| Force10 FTOS / Dell DNOS9 | FreeBSD 基网络交换 |
| Coyote Point EQ/OS | FreeBSD 基负载均衡 |
| Netflix Open Connect | FreeBSD 基 CDN |
| ravynOS（原 airyxOS） | FreeBSD 基 macOS 风格 |
| ULBSD | FreeBSD 基桌面 |
| FuryBSD | FreeBSD 基桌面 |
| helloSystem | FreeBSD 基桌面 |
| ClonOS | FreeBSD Jail/bhyve Web UI |
| Zrouter | FreeBSD 嵌入式 |
| OS108 | NetBSD 基桌面 |
| PolyBSD | NetBSD 嵌入式 |
| smolBSD | NetBSD 轻量 VM |
| irBSD | NetBSD 数字取证 |
| Jibbed | NetBSD Live CD |
| Gentoo/NetBSD | Gentoo × NetBSD |
| OliveBSD | OpenBSD Live CD |
| Anonym.OS | OpenBSD 匿名浏览 |
| ekkoBSD | OpenBSD 衍生（已停） |
| MicroBSD | OpenBSD 衍生（已停） |
| MirOS BSD | OpenBSD 衍生 |
| kFreeBSD | Debian GNU/kFreeBSD |

---

## 三、建议（待 ykla 裁定）

| # | 事项 | 建议 |
| - | ---- | ---- |
| ★1 | FreeBSD 1.0 日期回改 | 本会话 id=2199 的"订正"（11→12 月）本身有误——FBD 来源（FreeBSD 官方记录）优先于 CSDN 二手来源；**回改为 1993-11** |
| ★2 | 版本粒度差异定性 | 大纲按叙事里程碑概括与 bsd-family-tree.txt 按 point release 完整列出为**体例差异而非错误**——不建议逐 point release 补入大纲；建议在卷 20/23/26/29 的各卷技术专题史卷中设置“版本发行时间线”概述节引用 bsd-family-tree.txt 作为一手参照 |
| 3 | 2BSD 线补遗 | 卷 7 ch1 可增补 2.9BSD-Seismo（1984）与 2.10.1BSD（1987）两节 |
| 4 | 旧号引用残留 | 12 处“第三十四卷”分工注引用——经甄别后逐项修正（部分可能指旧卷 33/34，需读上下文） |
| 5 | 386/ix、Microport、COHERENT | 非 BSD 基，已在 114 §三·附·C 列为比较资源，不重复入谱系 |
| 6 | PicoBSD/FreeSBIE/m0n0wall/ClosedBSD 等停更衍生 | 归入 114 卷 ch2（FreeBSD 系衍生）——阶段二逐项另批 |

## 四、参考文献入库计划（ykla 令“入库入大纲”）

| 文献 | 入库（claim） | 入大纲 |
| ---- | ------------- | ------ |
| Leffler/McKusick/Karels/Quarterman 1989《4.3BSD OS Design》 | 已有（ref 5438 等） | 卷 6 |
| Salus 1994《A Quarter Century of UNIX》 | 已有（ref 5446 等） | 多卷引用 |
| McKusick/Bostic/Karels/Quarterman 1996《4.4BSD OS Design》 | 已有（ref 5445 等） | 卷 13 |
| McKusick/Neville-Neil 2004《FreeBSD OS Design》 | 已有 | 卷 21 |
| McKusick/Neville-Neil/Watson 2014《FreeBSD OS Design 2e》 | 已有 | 卷 21 |
| McIlroy《Research Unix Reader》 | 待核 | 卷 3 |

## 五、补记：复核后落实（2026-10-05，ykla“复核后全部批准”）

**★5 表年份订正（一手复核）**：本报告 §二 ★5 表所载年份经一手复核有误，现订正如次——

| 版本 | 本报告原载 | 一手定谳 | 依据 |
| ---- | ---------- | -------- | ---- |
| 2.9BSD-Seismo | ~~1984~~ | **1985-08** | bsd-family-tree.txt [SMS]；TUHS 存档 Keith Bostic 1985-07-17 于 seismo.UUCP 公告（comp.bugs.2bsd，1985-07 起供 tape） |
| 2.10.1BSD | ~~1987~~ | **1989-01** | bsd-family-tree.txt [SMS]（Steven M. Schultz 维护）；edm2 BSD 谱系页亦载 Jan 1989 |
| 2.11BSD | ~~1988~~ | **1991-03-14**（另说 1992-02，tree 历史版本） | bsd-family-tree.txt [SMS]；edm2／Software fandom 载 1992 两说并存 |

**★4 之 386BSD 0.1 定谳**：**1992-07-28**（bsd-family-tree.txt [DOC] 一手；edm2 载 Jul 1992）；大纲原载 1992-07-14 无源，已订正。

**★4 之 4.4BSD（tree 载 1993-06-01）**：经一手核对，tree 区分“4.4BSD Alpha（1992-07-07）”与“4.4BSD（1993-06-01，[USE]）”——后者系 4.4BSD（Encumbered）发行日，已由卷 13 ch1（Alpha／Encumbered 节）实质承载；本报告“可能载的是 Alpha 版”之推断予以撤回。

**落卷登记**：卷 7 ch1 补 2 节（Seismo 1985-08／2.10.1BSD 1989-01，章题时段扩 1983—1989）；卷 14 1.3 日期订正；卷 22／25／28／31 各补“版本发行时间线”节（★2 配套；落点按“技术专题史卷”语义校正为本报告原载卷号 20/23/26/29 之外的现行 22/25/28/31）；McIlroy《Research Unix Reader》ref 著录补全。口径 53 卷 447 章 **3,641 节／注 831**。执行记录见 `review_logs/115a-115号补办与台账补录执行记录-20261005.md`。

---

*编制：二旺（WorkBuddy），2026-10-05。本件为分析报告，未执行任何内容层变更；§三 待 ykla 裁定；§五 为补办落实补记。*
