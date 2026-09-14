# 核查报告：05-卷册大纲/第10卷-openbsd的历史/第208章-libressl的fork与早期发展/index.md

- 源文件：D:\librebsd\05-卷册大纲\第10卷-openbsd的历史\第208章-libressl的fork与早期发展\index.md（187 行，一次完整通读）
- 批次：C370（第 43 块第 1/3）；检查日期：2026-09-15；检查方式：逐文件完整阅读人工核对（LibreSSL fork 章目录）
- SUMMARY.md 收录：在档（208 index）
- 检查项速览：A 占位符——〔待核：原文截断〕见条 2；B 内容完整性——要点/史料/史观/辨析/文献＋PODCAST；C 编号与标题——旧章号残留见条 2；D 格式规范——文献栏混排见条 1；E 学术规范——表复制错乱见条 1；F SUMMARY 一致性——在档

## 问题清单

1. P2 | 文献栏混排大量时间线/对比/回应线索表＋两表完全重复 | 行 37-113 文献栏混入“**LibreSSL fork 关键事件时间线**”“**各系统采用情况对比**”“**OpenNTPD/OpenSMTPD 关键事件时间线**”“**OpenBSD 四大安全工具概览**”“**OpenSSL 阵营四条回应线索**”等大量表格（时间线/对比/回应线索应属正文要点，错位入文献栏）；且行 103-107“ntpd 阵营对 OpenNTPD 的三条回应线索”表与行 110-114 完全重复（复制错乱——三条内容为 milter 不支持/CVE-2020-8794/portable 采用率 1%，实为 OpenSMTPD 回应线索误植为 ntpd） | 表格移回正文要点；纠正 ntpd/OpenSMTPD 回应线索复制错乱
2. P3 | 旧章号 93 残留＋绝对路径＋DB_REF 年份异常＋待核/史观占位 | 行 12/30/46 引“93.7-93.9 节”（现 208）；行 46“c:\Users\ykla\Documents\...”绝对路径；行 49 DB_REF“openbsd.duckdb 1921-1921 年间：0 次提交”（年份异常，应为 1995-2026）；行 14/29“〔待核：原文截断，后文待回源〕”、行 25 史观“(待人工回填...)” | 93 改 208、路径改相对、DB_REF 年份校正、待核/史观回填

- 结论：存在问题 2 项（P0 0、P1 0、P2 1、P3 1）

## 补充说明（正样本与复核留痕）

- LibreSSL fork 时间线一手：2014-04-07 Heartbleed（CVE-2014-0160，tls1_process_heartbeat 缺边界检查）→04-14 misc 发起 fork→07-11 2.0→07-12 b6553af36068（jsing 引入 lib/libressl）→11-01 OpenBSD 5.6 默认——timeline 完整
- 采用情况表一手准确：OpenBSD 唯一默认 LibreSSL 主流 OS、FreeBSD 基础从未引入（14.0 OpenSSL 3.0.12）、macOS 10.11 起附带并存、Alpine 3.5 切 3.9 切回——采用格局清晰
- OpenSSH/OpenNTPD/OpenSMTPD/LibreSSL 四工具谱系（引入日期/commit hash/替代对象/类型）一手（OpenSSH 1999-10-01 bf74e864c129/OpenNTPD 2004-06-18 a66b0f8292c9 早于 3.6 约 5 个月/OpenSMTPD 2009-11）
- OpenSSL 阵营四条回应线索（Marquess 反思/路线图承认 5 问题/CII 资助重构/Andrew Ayer LibreSSL PRNG 隐性批评）——回应方视角完整
- PODCAST Brent Cook portable LibreSSL 一手（arc4random 陈旧/FreeBSD 非受支持平台、musl issetugid 上游修复、getentropy(2) 新系统调用、C 版块密码比 OpenSSL 快近两倍）——正配
- 交办提示：条 1 的文献栏表格混排与两表复制错乱同批全库扫（多 index 生成管线混排）