# 核查报告：第10卷-openbsd的历史/第211章-openbsd的社区治理与争议/index.md

- 源文件：d:\librebsd\05-卷册大纲\第10卷-openbsd的历史\第211章-openbsd的社区治理与争议\index.md
- 批次：C328；检查日期：2026-09-13；检查方式：逐文件完整阅读人工核查（辅以 SUMMARY 实测）
- SUMMARY.md 收录：未收录（UNLISTED 实测确认：SUMMARY 第 1805 行章头指向概述.md、第 1806 行起收录 211.1；本 index.md 未收录；批次 JSON 记 null）
- A 占位符：发现 1 处（行 26 显式“〔待核：原文截断，后文待回源〕”）
- B 内容完整性：发现 4 处戛然截断（行 25 尾“回顾性事”、行 27 尾“资金模式的可能变化、社”、行 28 尾“free sharing and”、行 29 尾“<<https://www.openbsdf>”含双左尖括号残段）；要点区单条为最小骨架（PODCAST_REVIEW 五期充实，登记观察）
- C 编号与标题：通过（双头结构见清单 1）
- D 格式规范：通过
- E 学术规范：发现 3 处（自撰史观标签；folder 噪声；PODCAST 标签前缀双写）
- F SUMMARY 一致性：未收录（双头结构组成部分）
- 机械旗标复核：UNLISTED_NOT_IN_SUMMARY 实测确认（章头指向概述.md）
- 问题清单：
  1. P2 | 全文件 | index.md 与概述.md 双头并存：概述.md 系 SUMMARY 第 1805 行章头，本 index.md 未收录（双头族第五例） | 章级结构待修
  2. P2 | 行 25-29 | 四处戛然截断＋一处显式占位＋“<<”双括号残段 | index 类截断损坏族：辩证链合图/综合审视/基金会考据三段的查证体中途截断，0 信任论证不完整 | 回源补全
  3. P3 | 行 21 | “自反性：de Raadt 的独裁治理模式是对‘开源社区民主’神话的自反性挑战” | 自撰史观标签且无条号：论旨对应权威 7“理论必须自反” | 补条号并用权威全称
  4. P3 | 行 15 | chmatch 史料行“匹配置信度 folder，原因：folder 第209章” | folder 噪声族：按目录名错配第 209 章（65index“folder 第64章”同族） | 关闭 folder 兜底匹配
  5. P3 | 行 83-88、94-96 | PODCAST 史观九条标签前缀双写（“总纲1 一切真历史都是古代史：总纲1 一切真历史都是古代史：”等） | 模板重复粘贴（124index 同族） | 去重前缀
- 结论：存在问题 5 项（P0 0、P1 0、P2 2、P3 3）

## 补充说明（正样本与复核留痕）

- PODCAST_REVIEW 五期史观 17 条全对（总纲 1/5/19/8×2/6×2/14/22×2/13×3/10/4/3/15——全部权威全称，其中总纲 14“苦难不值得被提倡”为 C323 勘误后首见正确用例），正确率与 89index 并列最高档。
- 辨析存疑/考据脚注完备度极高：提交计数口径不可靠（de Raadt 与主持人双重提示）、PDP-7 源码断代多源非定论、cat 版本时间线未经逐版核验、X 披露时间线单源、fork 批评与 Intel 指控系个人推断无直接证据、Gwynne 人名三写（Gwynn/Gwendt）、sec/sec4 混用、whurley 专名与通行记载对读（OpenQRM 源自 Qlusters、Nagios 创始人 Ethan Galstad 对转写 Clusters/Symbia/Volstead）。
- EP123（whurley/BMC 2007）为企业开源治理一手口述：BSD 单一许可证政策的利益分配论证、BMC Developer Network 上线形态、“开放是开关状态”与“求影响不求控制”的权力关系再安排、Gates“分享数据才是走向社区的第一步”引语——与本章社区治理主题契合；行 79 OpenBSD Foundation 2007 成立的当代播客记载为该章直接史料。
- Top 5 贡献者数据（ajacoutot/deraadt/sthen/espie/jasper）与 openbsd.duckdb DEEP_ANALYSIS 完全一致。
- 实测留痕：SUMMARY 第 1805-1806 行。
