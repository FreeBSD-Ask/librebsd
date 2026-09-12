# 核查报告：第06卷-freebsd的核心技术革新/第116章-capsicum的设计与watson团队贡献/index.md

- 源文件：d:\librebsd\05-卷册大纲\第06卷-freebsd的核心技术革新\第116章-capsicum的设计与watson团队贡献\index.md
- 批次：C248；检查日期：2026-09-12；检查方式：逐文件完整阅读人工核查（辅以 freebsd.duckdb 只读实查，3 枚 Watson commit 哈希核验）
- SUMMARY.md 收录：未收录（index.md 不入 SUMMARY；章页面为概述.md，UNLISTED 为机械层预期）
- A 占位符：发现 3 处（行 12“〔待核：原文截断，后文待回源〕”、行 34 同款、行 30 史观段“(待人工回填…)”）
- B 内容完整性：发现 2 处（要点三条中两条截断；辨析三条中三条截断——行 34/35/36 均止于词中）
- C 编号与标题：通过（H1 节号 116 与章号一致；无旧章号残留）
- D 格式规范：发现 2 处
- E 学术规范：通过（无总纲伪标签——PODCAST 块五条史观条目名与权威表逐字相符，唯前缀重复；无禁引来源，无禁用名称）
- F SUMMARY 一致性：机械层预期
- 机械旗标复核：UNLISTED_NOT_IN_SUMMARY——惯例豁免；无 SECTION_GAP 旗标
- 问题清单：
  1. P1 | 行 30 | 史观段“(待人工回填——详见子节文件史观/辨析字段)” | 章级史观空心（42/114/246 同款第四例） | 依章内子节史观字段汇总回填
  2. P1 | 行 11-13、34-36 | 要点三条中两条截断（行 11 止于“commit”、行 12 止于〔待核〕、行 13 止于“剑桥大学在”），辨析三条全部截断（行 34 止于〔待核〕、行 35 止于“Birkedal”、行 36 止于“均为”） | 截断损坏覆盖要点与辨析两段六处（字节截断族） | 回源重建两段
  3. P1 | 行 17-26 | 史料段 10 条 outline_mappings 行“BSD Now 第 609-676 期，关联度 1.0” | 自动映射噪声：十期不同节目对同一章“关联度 1.0”不合常理，且本文件 PODCAST_REVIEW 块仅覆盖 EP50/EP7，十期映射无对应复核块支撑 | 库侧复核映射质量；编纂引用前逐期抽查
  4. P2 | 行 40、45 | 文献条目尾部粘入“---## 史料登记与辩证校准（2026-08-08 追加）> **本卷命题**：24.3 长期主义…”与“**【本节文献综述】**…---**补充证据**…”两段 | 追加块/综述指引粘入文献行致层级塌陷（300/42 章同族），且“24.3 长期主义”系源文本章序引用（300 章报告同款处方：加源文本括注） | 拆出独立段落；行 53 DB_REF 塌行随修
  5. P2 | 行 80-86 | PODCAST 块史观五条前缀重复（“总纲10 动手者创造历史：总纲10 动手者创造历史：”等） | 前缀重复残留（113 章 index 同款），条目名本身与权威表逐字相符不计伪标签 | 去重前缀
  6. P3 | 行 45 | “【本节文献综述】详见 …references_fulltext.db（id=36）” | 旧库名后缀残留（WO-001 族） | 改 .duckdb
- 结论：存在问题 6 项（P0 0、P1 3、P2 2、P3 1）

## 补充说明（正样本与复核留痕）

- **3 枚 Robert Watson Capsicum commit 哈希全量实查逐字命中**（freebsd.duckdb 只读，哈希＋作者＋日期＋主题四字段全符）：72c35fc6＝2009-09-30“Reserve system call numbers for Capsicum security…”、96fcc75f＝2011-03-01“Add initial support for Capsicum's Capability Mode”、009d2032＝2011-12-29“Add options CAPABILITY_MODE…”——Capsicum 落地时间线（系统调用号预留→能力模式→GENERIC 入核）的 commit 级证据链完整。
- 辨析段的自纠质量高：作者名讹误修正（第四作者 Kris Kennaway 经论文 PDF 核实）、Lucas《Storage Essentials》等无关文献的模板复制清除、“Skorstengaard CHERI 论文”错位列入的修正——唯三条均被截断致修正内容不完整（问题清单 2）。
- PODCAST_REVIEW 双块（EP50 Watson／EP7 PHK）为顶级当事人史料：Capsicum 设计起点、Google Linux 移植、FreeBSD 10 工具沙箱化（tcpdump/gzip）；jail 起源口述（南卡托管商资助约定、与 Watson 合写 BSDCon 2000 论文）、MD5 crypt $1$ 前缀与“保护约五成互联网”当事人估计、GEOM/GBDE/GELI 谱系；四处 ASR 失真（Kamp 姓名三变体、GBD→GBDE、Pappel→Pawel Dawidek）与 jail 会议年份口述犹豫均挂 L4 存疑脚注——不臆造纪律最佳实践。
- 行 41 能力模型理论溯源（CAP computer/PSOS/Hydra/KeyKOS→Levy 1984→Capability Myths Demolished）学术谱系准确。
- 编码合规：UTF-8 无 BOM、LF；弯引号正确。
