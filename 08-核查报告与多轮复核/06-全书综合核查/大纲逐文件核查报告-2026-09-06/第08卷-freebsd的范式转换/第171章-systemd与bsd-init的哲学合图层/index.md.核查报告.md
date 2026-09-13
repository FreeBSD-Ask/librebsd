# 核查报告：第08卷-freebsd的范式转换/第171章-systemd与bsd-init的哲学合图层/index.md

- 源文件：d:\librebsd\05-卷册大纲\第08卷-freebsd的范式转换\第171章-systemd与bsd-init的哲学合图层\index.md
- 批次：C329；检查日期：2026-09-13；检查方式：逐文件完整阅读人工核查（辅以 SUMMARY/章目录实测）
- SUMMARY.md 收录：未收录（UNLISTED 实测确认：SUMMARY 第 1446 行章头指向概述.md、第 1447 行起收录 171.7；本 index.md 未收录；批次 JSON 记 null）
- A 占位符：发现 1 处（行 31 史观字段“(待人工回填——详见子节文件史观/辨析字段)”）
- B 内容完整性：发现 2 处戛然截断（行 11 要点“Pettitt 与 BUISHAND R 双变点检验一致判定 freebsd-src”断、行 35 辨析“(2) 变”断）
- C 编号与标题：通过（双头结构见清单 2）
- D 格式规范：发现 2 处（行 40-42 巨行拼接塌陷；“*统计局限性标注**”星号错配）
- E 学术规范：发现 4 处（旧章号 68B 内容误植为最重）
- F SUMMARY 一致性：未收录（双头结构组成部分）
- 机械旗标复核：SECTION_GAP 实测确认（171.1-171.6 无文件、171.7-171.10 在盘）；UNLISTED_NOT_IN_SUMMARY 实测确认
- 问题清单：
  1. P2 | 行 31 | “## 史观”下仅“(待人工回填——详见子节文件史观/辨析字段)” | 史观字段显式占位待回填（169index 同族） | 按 171 章主题回填史观
  2. P2 | 行 40-42 | “## 第 68B.12 不同时期人员的采访录”“## 第 68B.13 节 媒体反响与社区舆论”“第五卷第 68B 章映射” | 旧章号 68B 内容误植：68B 系第 169 章（SVN→Git 迁移）旧号，其采访录/媒体反响链接块误植入本 171 章文件；同段文献 49 条、文献综述、补充证据自动块、DB_REF 全部无换行连排成巨行（排版塌陷） | 链接块按 171 章重挂或删除并恢复换行
  3. P2 | 行 11、35 | 统计印证要点与统计局限辨析两处戛然截断 | index 类截断族 | 回源补全
  4. P3 | 行 16-17 | 2 条 chmatch“卷‘第09卷-netbsd的历史’……置信度 folder，原因：folder 第169章” | folder 噪声双错：卷与章均错配（本文件属第 08 卷第 171 章） | 关闭 folder 兜底匹配
  5. P3 | 行 40 | “Hibsd Project”×3＋引用路径“01-数据库本体/freebsd.duckdb” | 机构名疑讹＋路径断链（实测位于 02-FreeBSD/db/duckdb/；122.8/169.6 同族） | 统一订正
  6. P3 | 行 40-42 | “补充证据（基于全文数据库修订）”自动块 | 空值引用噪声（“(45, 年份不详)”“(standalone, 1997)”）＋“1991 年……王波《FreeBSD 使用大全》出版”纪年疑讹（C319 324.4 同族噪声形态） | 清理噪声行
  7. P3 | 行 74-76 | PODCAST 史观三条标签前缀双写（总纲 20/9/4） | 模板重复粘贴（124index/211index 同族） | 去重前缀
- 结论：存在问题 7 项（P0 0、P1 0、P2 3、P3 4）

## 补充说明（正样本与复核留痕）

- 文献 [1]-[49] 为章题完美契合的 GB/T 7714 著录群（systemd 与 BSD init 主题）：Poettering《Rethinking PID 1》与《The Biggest Myths》原文、Debian CTTE 投票档案与票决分析、Devuan 公告、NIST CVE 系列（含 [22] 标注“证伪：实为 Perl Module::Signature 漏洞”的自证伪条目——考据纪律 rare sample）、TUHS 的 UNIX V6 init.c/4BSD rc/4.2BSD rc.local 原始史料、Mewburn rc.d USENIX 2001 论文、OpenBSD rc.d/rc.subr 手册、Solaris SMF、OpenRC/runit/s6/daemontools 谱系——整章文献底座扎实。
- PODCAST_REVIEW 史观七条全对（总纲 10/21 革命与改革/9×2/4×2/20 历史地理塑造思想土壤——全部权威全称）；EP71（System Disaster）Ian Sutton 的 GSoC systemd 四组件 shim 辨析精准：“GNOME 硬依赖的兼容包装并非把 systemd 移植到 OpenBSD”——依赖兼容与本体移植之分为本章合图层核心材料；EP370 Losh 迁移动因三分与 rcorder D25389 并行化（15-20 秒）；EP55 Chadd 无线栈一手自述；转写失真密集标注（bhyve→Beehive、LibreSSL→Libra SSL、GSoC→G-Sog、Daroussin→Darosun）。
- 实测留痕：章目录 SECTION_GAP 与 SUMMARY 第 1446-1447 行吻合；DB_REF 2024-2026 168,386 与 169.6 同口径。
