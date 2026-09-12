# 核查报告：第06卷-freebsd的核心技术革新/第129章-freebsd10x的贡献者管理与社区治理/index.md

- 源文件：d:\librebsd\05-卷册大纲\第06卷-freebsd的核心技术革新\第129章-freebsd10x的贡献者管理与社区治理\index.md
- 批次：C293；检查日期：2026-09-12；检查方式：逐文件完整阅读人工核查，辅以 freebsd.duckdb 只读实查
- SUMMARY.md 收录：未收录——批次 JSON 无 summary_line；SUMMARY 行 1136 收录的是同章概述.md，index.md 与概述.md 并存且仅概述在册
- A 占位符：发现 2 处（行 87、88“［待核·needs_fix］”消解回写挂起标记）
- B 内容完整性：通过（要点/史料/史观/辨析/文献与 PODCAST_REVIEW 三期齐全）
- C 编号与标题：通过（H1 与章名一致，YAML frontmatter chapter/id/volume 规范）
- D 格式规范：发现 2 类（行 33 加粗标记错位“*Xin LI 角色的辨析**”；行 87-88 文献级别标识 [Z]/[EB/OL] 重复错位 ×2 处）
- E 学术规范：发现 3 类（行 15 chmatch 记录旧章号残留；行 25 裸专题语“多方平等”未挂权威表条目；行 67-69 史观标签文本重复 ×3 处）
- F SUMMARY 一致性：不一致（未收录，双文件族）
- 机械旗标复核：批次 flags 非空——UNLISTED_NOT_IN_SUMMARY（index.md 未收录）+ SECTION_GAP{"gaps":[1..10],"min":11,"max":15,"count":5}（SUMMARY 中本章仅录 129.11-129.15 与采访录，129.1-129.10 缺收录）；对应双文件族 DEFERRED，归主线程处置
- 问题清单：
  1. P2 | 行 15 | “匹配置信度 folder，原因：folder 第127章” | 旧章号残留：第 129 章 index 引用的 DB 匹配记录章号为 127 | 核 references_fulltext 源记录，更正章号或标注为匹配噪声
  2. P2 | 行 33 | “10.x 周期 Security Officer 仅 Martin Matuska 一人” | 人物归属存疑：通行记载 10.x 期 Security Officer 为 Philip Paeps（2013 起继任），Matuska 为 ZFS/libarchive ports 维护者；同句“约 60% 的 CVE 修复”无出处 | 核 freebsd.org 安全团队名录后更正归属；60% 降为“大量”级估算表述
  3. P2 | 行 32 | “Darwin/PS4/Xbox（均基于 BSD 派生内核）” | 平台谱系错置：Xbox 系主机内核为 NT（Windows）派生，非 BSD 派生 | 改为“Darwin/PS4（均基于 BSD 派生内核）”并核对 Xbox 表述
  4. P2 | 行 — | index.md 未收录而在册为概述.md | 双文件族：index.md 与概述.md 并存且仅概述在册；SECTION_GAP 另示 SUMMARY 缺 129.1-129.10 收录 | DEFERRED 主线程处置（统一在册文件、补全子节收录）
  5. P3 | 行 25 | “多方平等：贡献者无论提交量多少…” | 裸专题语未挂权威表条目（内容对应第 8 条“本体论上各方平等”） | 改挂“总纲第 8 条——本体论上各方平等”
  6. P3 | 行 67-69 | “总纲10 动手者创造历史：总纲10 动手者创造历史：”等 ×3 处 | 史观标签文本重复（行 67 总纲10、行 68 总纲6、行 69 总纲9 均双写） | 去重；标签语义本身（10/8/6/9）均与权威表对位
  7. P3 | 行 87-88 | “［待核·needs_fix］” ×2 处 | dangan-20260908 消解回写挂起标记未清（CVSS v3.0 spec、NTP 4.2.8p 安全通告两条） | 核毕后消除标记或落定著录
  8. P3 | 行 33 | “*Xin LI 角色的辨析**” | 加粗标记错位（单星开头双星结尾） | 改为“**Xin LI 角色的辨析**”
  9. P3 | 行 87-88 | “Specification Document [Z]. …<URL>[EB/OL]. 2015.” ×2 处 | 文献级别标识 [Z]/[EB/OL] 重出且与 URL 错位 | 规范著录（一级标识二选一）
- 结论：存在问题 9 项（P0 0、P1 0、P2 4、P3 5）

## 补充说明（正样本与复核留痕）

- DB 实查正样本：freebsd.duckdb author_name 口径 top5 = Po-Chuan Hsieh 68,595 / Sunpoet Po-Chuan Hsieh 51,033 / Yuri Victorovich 29,759 / Jan Beich 22,360 / Martin Wilke 20,341，与行 11、21 逐项一致（committer_name 口径为 68,449/51,033/30,208/22,504/20,341——正文数字系 author 口径，非漂移）。
- 口径提示（不计缺陷）：“Po-Chuan Hsieh”与“Sunpoet Po-Chuan Hsieh”疑为同一开发者双署名（sunpoet@），“Top 5 贡献者”非五个自然人；行 11“贡献者集中度反映精英化”论断受双计影响，建议加口径脚注。
- PODCAST_REVIEW 三期（EP134/57/36）均紧扣“贡献者管理与社区治理”主题：ports 导师制评估周期、core team“放牧猫群”职责当事人界定（Chisnall）、defaults 之争与“总有人不高兴”（Allan）、mentoring 渐进路径（Steve Wills），转写失真（Seve→Sepherosa Ziehau、NT4 47 天→49.7 天）均有存疑脚注——方法论扎实。
- 史观标签总纲10/8/6/9 语义均与权威表对位（仅行 25 裸专题语与文本重复问题，已入清单）。
- 双文件留痕：章目录 ls 实证 index.md 与 概述.md（含 .bak 备份）并存；129.11-129.15 五个子节文件在盘，与 SUMMARY 收录一致。
- 编码合规：UTF-8 无 BOM、LF；弯引号正确。
