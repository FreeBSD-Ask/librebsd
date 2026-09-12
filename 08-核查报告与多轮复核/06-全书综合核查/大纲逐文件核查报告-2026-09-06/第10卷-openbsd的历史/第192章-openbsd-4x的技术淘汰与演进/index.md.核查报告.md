# 核查报告：第10卷-openbsd的历史/第192章-openbsd-4x的技术淘汰与演进/index.md

- 源文件：d:\librebsd\05-卷册大纲\第10卷-openbsd的历史\第192章-openbsd-4x的技术淘汰与演进\index.md
- 批次：C282；检查日期：2026-09-12；检查方式：逐文件完整阅读人工核查；辅以 openbsd.duckdb 只读实查
- SUMMARY.md 收录：未收录——批次 JSON 无 summary_line；SUMMARY 行 1626 收录的是同章概述.md，index.md 与概述.md 并存且仅概述在册（概述.md H1 与 SUMMARY 章标题一致，index.md H1 不一致）
- A 占位符：通过
- B 内容完整性：发现 5 处（史观段空心 1 处；要点句自认截断 1 处；辨析句中断截断 3 类 4 处）
- C 编号与标题：发现 1 类（H1"openbsd-4x的技术淘汰与演进"与 SUMMARY 章标题"OpenBSD 4.x 的技术淘汰与 gcc GPLv3 争议"不一致，并入双文件族处理）
- D 格式规范：发现 3 类（巨型单行粘连 1 处；marc.info URL 断裂 ×2 处；模板占位 URL 1 处）
- E 学术规范：发现 3 类（史观伪标签 6 处；史观段"待人工回填"空心 1 处；节末文献主体脱节 1 类）
- F SUMMARY 一致性：不一致（未收录——批次 JSON 无 summary_line；SUMMARY 行 1626 收录的是同章概述.md，index.md 与概述.md 并存且仅概述在册；且 index.md H1 与章标题不一致）
- 机械旗标复核：批次 JSON flag UNLISTED_NOT_IN_SUMMARY 属实，已按双文件族记 P2 DEFERRED
- 问题清单：
  1. P1 | 行 46 | "### 史观映射OpenBSD 4.x 时期是…" | 巨型单行粘连：史观映射整段与 8 条 FreeBSD 论文文献条目、小节标题粘连为一行 | 拆分为标准列表与独立小节
  2. P1 | 行 46 | "总纲第 17 条——软件工程"等 ×6 处 | 史观伪标签：第 17 条→软件工程（应第 15 条）×2、第 12 条→法律结构（应第 13 条存疑）、第 10 条→边缘者贡献（描述符改"动手者创造历史"，编号不变）、第 21 条→密码学（按内容重挂）、第 23 条→社区治理（应第 15 条） | 按权威编号表逐条重挂
  3. P2 | 行 34 | "(待人工回填——详见子节文件史观/辨析字段)" | 史观段空心族 | 回填章级史观或显式改引子节
  4. P2 | 行 13 | "三个历史定位。第一是…〔待核：原文截断，后文待回源〕" | 要点句中断截断且自认回源未完成 | 回源补全第二、三定位
  5. P2 | 行 38/39/40/42 | "以 **sof""交叉确""clang/LLVM""对照 commit" | 辨析句中断截断 ×4 处 | 补全四句
  6. P2 | 行 14/49/53/57/61/65 | "3,352 位贡献者" ×6 处 | DB_REF 旧口径：openbsd.duckdb contributors 实测 1,031 | 全改 1,031
  7. P2 | 行 44-46 | "smart(8) Update""Australian NFP/NGO Health Sector"等 | 节末文献主体脱节：8 条 FreeBSD 社区论文约 5 条与 OpenBSD 4.x 主题零关联，且与史观映射粘连堆叠 | 按章主题重挂文献
  8. P2 | —（元数据） | SUMMARY 行 1626 收录概述.md | 双文件族 DEFERRED：index.md 未收录（批次 JSON 无 summary_line，flag UNLISTED_NOT_IN_SUMMARY），index.md 与概述.md 并存且仅概述在册，两者章题亦不一致 | 确定唯一在册文件并统一章题
  9. P2 | 行 54/62 | "?laccopenbsd-tech""?laccopenbsd-announce" ×2 处 | URL 断裂（应为 ?l=openbsd-tech 等） | 修正 marc.info 链接
  10. P2 | 行 11 | "softraid 加密于 2007-11-27 …首次引入（4.2 周期）" | 日期错配+语义不符：实测该 commit message 为"split crypto functions out into their own file"（重构拆分，加密功能此前已存在）；且 2007-11-27 在 4.2 发布（2007-11-01）之后，属 4.3 开发周期 | 另考加密引入 commit 并按 4.3 周期表述
  11. P3 | 行 62 | "openbsd.org/{40-49}.html" | 模板占位 URL（非实际可访问地址） | 逐页列实名 40.html-49.html 或改 plus.html
  12. P3 | 行 62 | "原材料/研究/考据记录/20260723_announcements-openbsd.md" | 断链（D:\librebsd\原材料 全项目不存在） | 改库内实际路径
- 结论：存在问题 12 项（P0 0、P1 2、P2 8、P3 2）

## 补充说明（正样本与复核留痕）

- DB 实查（openbsd.duckdb，read_only）：openbsd-src 246,535 + openbsd-ports 212,040 + openbsd-www 32,620 = 491,195，与文内总览一致；贡献者实测 1,031（文内 3,352 为旧口径）；区间计数 2005-2010=100,198、2006-2009=65,854、2006-2012=112,057 三处逐一实测吻合。
- 六个 commit 逐一实测（哈希/作者/日期全对，正样本）：`39ff0b053b95…`（markus 2008-04-02，"back out 1.183" CVE-2008-1483）、`98855ba5cdbc…`（dlg 2007-03-19，softraid attach，引文逐字吻合）、`79cdc9424edb…`（hshoexer 2008-06-14，"enable softraid crypto"）、`66e23c51…`（tedu 2006-10-24，malloc 加固）、`60b4da4bc641…`（otto 2007-09-15，PCC import）；唯 `f18dcc9c26b1` 的定性见问题 10。
- PODCAST_REVIEW（BSDTalk EP204 mandoc 访谈）与 192.3 gcc GPLv3/mandoc 替换主题衔接良好，"总纲4 分离聚合是永恒规律"挂标正确，转写音误（Chris Stapps/grof 等）自我标注——正样本。
- 史料节 12 条为 DB 机器映射留痕（chapter_matches"任务4第二批 缺口章补充"×2、BSD Now outline_mappings ×10），属编纂痕迹而非史实主张，不计缺陷。
- netbsd.duckdb/openbsd.duckdb 均无 tags 表（repos.tag_count=0），与"镜像不含 tag 信息"的库情一致。
- 编码合规：UTF-8 无 BOM、LF；弯引号正确。
