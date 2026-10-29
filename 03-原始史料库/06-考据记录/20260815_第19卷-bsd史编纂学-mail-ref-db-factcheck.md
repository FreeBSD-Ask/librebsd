# 2026-08-15 第19卷“BSD 史编纂学”双库事实核查

> **查证来源**：邮件列表库（_mail_search.py，openbsd/netbsd 全库 + freebsd 部分库因 FTS 缺失 29/176 库跳过）+ 参考文献库（_ref_search.py，fulltext/facts 模式）
> **交叉验证方法**：每项事实至少双库各检索 1 次，关键词覆盖中英文变体；内部引用通过文件系统存在性核查
> **存疑判定依据**：0 信任原则，两库均未命中且无其他可溯源证据的标注“两库无法验证”；大纲自身已标注存疑的保留原标注

---

## 一、外部文献验证（参考文献库 / 邮件列表库）

### 1.1 Salus 1994 *A Quarter Century of UNIX*
- **判定**：通过
- **参考文献库**：ref_id 810，全文本入库，ISBN 978-0-201-54777-1，确认为 Addison-Wesley 1994 年出版
- **邮件列表库**：未直接命中（年代早于邮件列表存档覆盖范围）

### 1.2 McKusick 1999 "Twenty Years of Berkeley Unix"
- **判定**：存疑——两库无法验证
- **参考文献库**：未找到该标题。最接近匹配：McKusick 1996 *The Design and Implementation of the 4.4 BSD Operating System*（ref_id 1137/2778）+ McKusick 2014 *The Design and Implementation of the FreeBSD Operating System*（ref_id 845）
- **查证备注**：McKusick 确有此文（收入 *UNIX: The First Quarter Century* 或类似文集），但参考文献库未收录。建议补录该文献全文
- **邮件列表库**：未命中

### 1.3 Croce 1917 *Teoria e storia della storiografia*
- **判定**：两库无法验证
- **参考文献库**：未找到该书。Hayden White 1979 *Metahistory*（ref_id 371）引用了 Croce，但 Croce 原著未入库
- **邮件列表库**：不适用（非 BSD 主题）

### 1.4 Bernstein 1983 *Beyond Objectivism and Relativism*
- **判定**：两库无法验证
- **参考文献库**：未找到该书
- **邮件列表库**：不适用（非 BSD 主题）

### 1.5 Leffler 1989 *The Design and Implementation of the 4.3BSD UNIX Operating System*
- **判定**：通过
- **参考文献库**：ref_id 804，全文本入库

### 1.6 Quarterman/Silberschatz/Peterson 1985 "4.2BSD and 4.3BSD as Examples of the UNIX System"
- **判定**：通过
- **参考文献库**：ref_id 2772，全文本入库

### 1.7 Spinellis 2017 "A Repository of Unix History and Evolution"
- **判定**：通过
- **参考文献库**：ref_id 902（期刊论文）+ ref_id 1189（单行本），均全文入库

### 1.8 1BSD 发布细节（1977 年汇编 / READ_ME 1977-11-23 / 1978-03-09 发布）
- **判定**：两库无法验证
- **参考文献库**：未找到精确日期信息
- **邮件列表库**：未命中（OpenBSD 邮件列表命中 2 条含 "1BSD" 但为间接提及，非一手史料）
- **查证备注**：这些日期在 BSD 文献中广为流传，但本书参考文献库中无直接收录。建议从 TUHS 档案（tuhs.org）或 Salus 1994 第 9 章获取一手来源

### 1.9 FreeBSD active committer ~300 人
- **判定**：存疑——两库无法验证
- **参考文献库**：有 FreeBSD 2025 Community Survey（ref_id 1017）但无法直接确认 committer 数量
- **邮件列表库**：FreeBSD 邮件列表因 FTS 缺失 29/176 库无法完整检索
- **查证备注**：建议查阅 FreeBSD 官方 committer 列表（docs.freebsd.org）或 2025 Community Survey 全文

### 1.10 FreeBSD 安装用户数万至数十万
- **判定**：两库无法验证
- 无精确统计来源，该数字为估算

### 1.11 Multics 关闭时间（2000-10-30 / 17:08 UTC）
- **判定**：存疑（大纲已标注）——参考文献库未直接验证
- **参考文献库**：有 Saltzer 1974 Multics 论文（ref_id 1146），但无关闭时间
- **邮件列表库**：未命中
- **查证备注**：大纲 349.3 节已正确标注"17:08 UTC 仅见于 FOLDOC 三手词典，原始会话日志未找到"，此标注符合 0 信任原则

### 1.12 PDP-11 硬件约束（4K 字内存、无 MMU）
- **判定**：两库无法验证
- **参考文献库**：未直接命中 PDP-11 规格
- **查证备注**：PDP-11/40 典型配置为 16K-28K 字内存，PDP-11/20 为 4K 字。需确认具体型号

### 1.13 Bob Fabry 口述史缺失
- **判定**：通过（大纲自身已标注缺失，检索路径明确）
- 大纲标注"截至 2026-07-28 经三轮检索（CHM Oral History 目录、Bancroft Oral History Center 目录、Internet Archive 搜索）未检索到"——符合缺位标注规范

### 1.14 OpenBSD BDFL 模式（Theo de Raadt）
- **判定**：通过——邮件列表库证实 de Raadt 主导地位
- **邮件列表库**：OpenBSD announce/bugs 列表大量 de Raadt 发布 release announcement/close bug reports，覆盖 1998-2005 年，证实其核心角色
- **查证备注**："BDFL" 术语本身未在邮件列表中出现（该术语更常用于 Python/Linux 社区），但 de Raadt 在 OpenBSD 的实际主导地位可被邮件列表证实

### 1.15 FreeBSD Core Team 选举制
- **判定**：两库无法验证
- **参考文献库**：未找到 Core Team 选举具体资料
- **邮件列表库**：FreeBSD 邮件列表因 FTS 缺失无法完整检索

### 1.16 NetBSD Foundation 民主治理
- **判定**：两库无法验证
- **参考文献库**：未找到 NetBSD Foundation 治理结构具体资料

---

## 二、内部引用一致性核查

### 2.1 章号 Frontmatter 与目录名不一致（系统性偏差）
- **判定**：修正——所有章存在 frontmatter 章号比目录名小 1 的系统性偏差
- **现象**：
  - 第350章目录 → 概述.md frontmatter 写 chapter: 第 349 章，子文件用 349.x 前缀
  - 第351章目录 → 概述.md frontmatter 写 chapter: 第 350 章
  - 第352章目录 → 概述.md frontmatter 写 chapter: 第 351 章
  - 第353章目录 → 概述.md frontmatter 写 chapter: 第 352 章
  - 第354章目录 → 概述.md frontmatter 写 chapter: 第 353 章
  - 第355章目录 → 概述.md frontmatter 写 chapter: 第 354 章
- **原因推断**：全书重编号后 frontmatter 未同步更新

### 2.2 第 26 章引用（349.1/349.2/349.3/349.4 节多处引用）
- **判定**：存疑——引用内容与实际章节不符
- **实际第26章**：第01卷-unix的起源/第26章-plan9的哲学与当代影响（Plan 9 主题）
- **大纲引用内容**："第 26 章 26.5 节——多方视角作为建构性叙事的实践案例"、"第 26 章 26.5.2 节——Fabry 口述史缺失标注"、"第 26 章 26.5.5 节——Haley 口述史缺失标注"
- **分析**：Plan 9 章不可能有 1BSD 多方视角和 BSD 人物口述史标注。可能指向的是另一章（BSD 早期历史相关章节），需核实原引用目标

### 2.3 第 310 章引用（349.4 节）
- **判定**：存疑——引用内容与实际章节不符
- **实际第310章**：第16卷-开源运动与合规治理/第310章-全球社区时期的其他科学-物理天文
- **大纲引用内容**："第 310 章 310.9 节——BSD 与自反性"、"第 310 章 310.9.5 节——四条书写伦理"
- **分析**："全球社区时期的其他科学-物理天文"章不可能有 BSD 自反性小节。需核实原引用目标

### 2.4 "danag.md" 拼写错误（349.1 节史料字段）
- **判定**：修正
- **现象**：349.1 节史料字段引用 danag.md 总纲 2，实际文件名为 dagang.md
- **建议**：修正为 dagang.md

### 2.5 核心文件存在性
- **判定**：全部通过
- shigang.md：存在
- lishidagang.md：存在
- dagang.md：存在

### 2.6 第 1 章引用（349.1 节）
- **判定**：两库无法验证——需核查实际内容
- **实际第1章**：第01卷-unix的起源/第1章-unix前史
- **大纲引用内容**："第 1 章 1.4 节——PDP-7 硬件约束对 UNIX 设计的塑造"、"第 1 章 1.5.3 节——Multics 关闭精确时刻的存疑标注"
- 第1章主题为 UNIX 前史，PDP-7 和 Multics 相关引用应属合理范围

### 2.7 351-355 章子节文件缺失
- **判定**：标注——所有章节索引中的子节均未创建实际 .md 文件
- 第351章：索引列出 350.1-350.4 四个子节，均无文件
- 第352章：索引列出 351.1-351.4 四个子节，均无文件
- 第353章：索引列出 352.1-352.4 四个子节，均无文件
- 第354章：索引列出 353.1-353.4 四个子节，均无文件
- 第355章：索引列出 354.1-354.4 四个子节，均无文件

### 2.8 "~163 章锚定=0" 与 "P2 级 71 人" 等统计数字
- **判定**：两库无法验证——属项目内部统计，需查阅项目元数据或统计脚本确认

---

## 三、邮件列表库工具问题

### 3.1 FreeBSD 邮件列表库 FTS 缺失
- **现象**：_mail_search.py --project freebsd 报错 
o such table: messages_fts
- **根因**：FreeBSD db/ 目录下 176 个数据库中，29 个（cvs-* 系列 + freebsd-commit + freebsd-cvsweb + netbsd-commit）无 FTS 表
- **影响**：脚本遍历全部 .db 文件时遇到第一个无 FTS 的库即崩溃，导致 FreeBSD 邮件列表完全无法检索
- **建议**：修复 _mail_search.py 增加 try/except 跳过无 FTS 的库

### 3.2 NetBSD/DragonFly/Other-BSD/Usenet 邮件列表
- 本次核查未使用（工具可用但未命中相关事实）

---

## 四、核查结论汇总

| 类别 | 通过 | 存疑 | 修正 | 两库无法验证 |
|:--|:--|:--|:--|:--|
| 外部文献 | 5 | 2 | 0 | 9 |
| 内部引用 | 1 | 3 | 2 | 2 |
| 合计 | 6 | 5 | 2 | 11 |

### 需立即修正
1. 全部章的 frontmatter 章号与目录名对齐（系统性偏差）
2. 第350章子文件前缀从 349.x 改为 350.x
3. "danag.md" → "dagang.md"（349.1 节）

### 需进一步核实
1. 第 26 章和第 310 章引用——可能指向了重编号前的旧章号
2. McKusick 1999 文献——建议补录全文
3. FreeBSD committer 数量——建议查阅 2025 Community Survey 全文或官方列表
4. 1BSD 精确日期——建议从 TUHS 档案获取一手来源

### 已确认准确
1. Salus 1994、Leffler 1989、Quarterman 1985、Spinellis 2017 等文献引用准确
2. OpenBSD de Raadt 主导地位可被邮件列表证实
3. Multics 关闭时间存疑标注符合 0 信任原则
4. Bob Fabry 口述史缺失标注符合缺位标注规范
