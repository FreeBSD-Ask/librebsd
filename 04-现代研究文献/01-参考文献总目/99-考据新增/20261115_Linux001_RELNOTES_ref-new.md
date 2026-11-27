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

## 批内追加引文（supp-V18-b001，2026-11-27）

以下五句逐字取自同一文件（行内折行按渲染口径归一为单空格）：

1. The linux kernel has been made under minix, and it was my original idea to make it binary compatible with minix. That was dropped, as the differences got bigger, but the system still resembles minix a great deal.
2. The main difference is in the fact that minix has a single-threaded file-system and linux hasn't.
3. This version is also meant mostly for reading - ie if you are interested in how the system looks like currently.
4. This kernel is (C) 1991 Linus Torvalds, but all or part of it may be redistributed provided you do the following:
5. Almost none of the support routines have yet been coded. Thus you currently need minix to bootstrap the system.

另有一句含 ASCII 引号，置于代码围栏以保逐字：

```
You may not distibute this for a fee, not even "handling" costs.
```

落点：V18.1.1.3／1.1.5／1.2.1／1.2.2／1.2.4／1.2.5（supp-V18-b001）；卡哈希由引擎 card_resync 回刷。
