# ref-new 考据登记（2026-11-27，supp-V73-b002）

- **标题**：4.2BSD distribution tape FORMAT（TUHS 档案，磁带条目清单）
- **作者**：UC Berkeley CSRG（发行方；档案页由 TUHS 维护）
- **年份**：1983（4.2BSD 发行）
- **来源 URL**：https://www.tuhs.org/Archive/Distributions/UCB/4BSD/4.2BSD/FORMAT
- **载体**：TUHS Unix Archive 存档文件（纯文本，开放获取）
- **抓取日期**：2026-11-27（curl -A Mozilla 实取，519 B 级纯文本）
- **用途**：supp-V73-b002／V73.1.2.2（磁带条目即最小记录单位）
- **查重披露**：URL 库内零命中新建；与 ref5803（4.1BSD 重建 README）分属不同发行档。

## 关键原文（逐字）

> 1. stand (199 512 byte records) 2. miniroot (205 10240 byte records) 3. rootdump (383 10240 byte records) 4. srcsys.tar (441 10240 byte records) 5. usr.tar (2148 10240 byte records) 6. vfont.tar (575 10240 byte records) 7. src.tar (2091 10240 byte records) 8. new.tar (592 10240 byte records) 9. ingres.tar (380 10240 byte records)

（原文为逐行编号清单；此处按页面换行归一为一段，条目词序与记录数逐字保留。）

**PL500readme 对照句（同日实取，TUHS 2.11BSD patch 目录，另建卡）**：

> 500: the patchkit that will convert a Patch #499 system to PL500.

## 中文提要

4.2BSD 发行磁带的 FORMAT 文件以九个编号条目界定带面内容，每条目标注记录数与记录长度（512／10240 字节）——带面即可核的最小记录单位；2.11BSD 的 PL500 补丁带则以 patch level 编号累积（#499→PL500），每级同样是一个可核单位。
