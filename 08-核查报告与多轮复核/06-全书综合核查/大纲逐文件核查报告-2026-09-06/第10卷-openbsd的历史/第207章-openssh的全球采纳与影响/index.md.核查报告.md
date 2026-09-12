# 核查报告：第10卷-openbsd的历史/第207章-openssh的全球采纳与影响/index.md

- 源文件：d:\librebsd\05-卷册大纲\第10卷-openbsd的历史\第207章-openssh的全球采纳与影响\index.md
- 批次：C289；检查日期：2026-09-12；检查方式：逐文件完整阅读人工核查（辅以 openssh.duckdb 只读实查）
- SUMMARY.md 收录：未收录——批次 JSON 无 summary_line；SUMMARY 行 1765 收录的是同章概述.md，index.md 与概述.md 并存且仅概述在册（概述题名“OpenSSH 的全球采纳与影响”与 H1“openssh的全球采纳与影响”仅大小写之差）
- A 占位符：通过
- B 内容完整性：发现 2 类（辨析节五条全部句段截断 P1；要点/史料空心与 DB 注入残块 P2）
- C 编号与标题：通过（H1 与章目录一致；史料残块内“第205章”章号错乱已并入 B 计）
- D 格式规范：发现 1 类（史观标签文本重复 ×5 处）
- E 学术规范：发现 2 类（史观裸标签单句 P3；PODCAST_REVIEW 主体跑题 P2）
- F SUMMARY 一致性：不一致（index.md 未收录，在册者为概述.md——双文件族 DEFERRED）
- 机械旗标复核：UNLISTED_NOT_IN_SUMMARY——已复核属实
- 问题清单：
  1. P1 | 行 25-29 | “……三条总纲均”／“…quickly removed” | 辨析节仅有的五条考据留痕全部句段中断截断（“三条总纲均”“quickly removed”“1.2.12 release,”“work les”“——移除 libgmp”），引文与结论双双缺失，且为该节全部内容，承重、无完整孪生 | 回源 openssh.com/history.html 与项目统摄史观原件补全引文与结论
  2. P2 | 行 11/15/17/33 | “……chmatch_3905……原因：folder 第205章” | 要点/史料主体为 DB 注入残行：要点仅 1 行快照；史料首条为自动匹配残块且章号错乱（207 误作 205）；文献行为 [DB:references_fulltext] 泛引（4077 篇/27138 条，无对应关系说明） | 重写章级要点与史料，清除 chmatch 残块与泛引行
  3. P2 | 行 25 | “c:\Users\ykla\Documents\hibsd\原材料\哲学\项目统摄史观\第 25 章.md” | 项目外绝对路径断链（实测该目录不存在；属原材料断链族） | 改引库内实际路径并留存证记录
  4. P2 | 行 40-53 | “Warner Losh 通过 Bell Labs 1968 年影片…” | PODCAST_REVIEW 注入块主体跑题：PDP-7 影片考据（3 条）、SmallWall（4 条）、GhostBSD、Docker on FreeBSD、Marco Peereboom 个人桌面/ACPI/bioctl 等与“OpenSSH 全球采纳”脱节（仅 OpenSSH 8.1、微软捐赠与集成、Solaris 弃 Sun SSH 改用 OpenSSH、总纲 13“OpenSSH 悖论”数条切题） | 抽取切题条目成节，其余移出本章
  5. P2 | （SUMMARY 未收录） | index.md | 双文件族：在册者为概述.md（SUMMARY 行 1765），index.md 未收录 | DEFERRED（沿用主线程双文件裁决）
  6. P3 | 行 21 | “形式主义：OpenSSH 的全球采纳率超过 90%…” | 史观仅单句且为裸专题语（无“总纲第 N 条”编号，未挂权威表条目），“超过 90%”亦无口径与出处 | 按内容重挂（建议第 12 或 15 条）并补写章级史观段
  7. P3 | 行 66-70 | “总纲1 一切真历史都是古代史：总纲1 …” | 史观标签文本重复 ×5 处（行 72-74 未重复） | 删除重复标签
- 结论：存在问题 7 项（P0 0、P1 1、P2 4、P3 2）

## 补充说明（正样本与复核留痕）

- DB 实查（openssh.duckdb 只读，D:\librebsd\03-原始史料库\01-代码仓库史料\08-跨项目对比\db\duckdb\openssh.duckdb）：仓库时间跨度实测 1999-10-27 至 2026-08-20、共 14,372 次提交，与行 11/17 著录逐字一致；2001 年实测 1,266 次提交且确为峰值年（2002 年 878、2003 年 757），“高峰期 2001年(1266次)”数字与口径双双吻合——本文件全部 DB 主张实测通过。
- 正样本：PODCAST_REVIEW 块内 9 条史观标签（总纲 1/17/19/22/8/10/10/5/13）全部与权威编号表相符；切题条目史实无误——OpenSSH 8.1 修复 XMSS 整数溢出、RSA 证书默认改 SHA2-512，微软因 Windows 集成 OpenSSH 向 OpenBSD 基金会捐赠，Oracle Solaris 以原生 OpenSSH 取代 Sun SSH 并借入 getentropy/arc4random，均与通行记载相符；SmallWall 一条对转写讹误（monoWall 作者邮件）已带存疑脚注。
- 行 61 对 BSDTalk EP27 转写讹误（Perebum/BioCuttle/AppGet 等）逐项列出并加双重存疑脚注，是全批次少见的规范留痕，值得肯定（正文引用前须对音核实）。
- 机械旗标复核留痕：flags=[UNLISTED_NOT_IN_SUMMARY]，经 grep SUMMARY.md 证实第 207 章条目族自概述.md 起（行 1765-1772），无 index.md 行。
- 编码合规：UTF-8 无 BOM、LF；弯引号正确。
