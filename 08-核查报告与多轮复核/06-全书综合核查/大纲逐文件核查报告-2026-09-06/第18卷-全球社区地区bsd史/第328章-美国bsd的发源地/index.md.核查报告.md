# 核查报告：第18卷-全球社区地区bsd史/第328章-美国bsd的发源地/index.md

- 源文件：d:\librebsd\05-卷册大纲\第18卷-全球社区地区bsd史\第328章-美国bsd的发源地\index.md
- 批次：C265；检查日期：2026-09-12；检查方式：逐文件完整阅读人工核查（粘连行逐段判读；chapter_matches 错挂判读；PODCAST 三期主题契合度核对）
- SUMMARY.md 收录：未收录——批次 JSON 无 summary_line（chapterfile）；SUMMARY 行 2774 收录的是同章概述.md（“第 328 章 美国：BSD 的发源地——伯克利 CSRG 的地缘遗产”），index.md 与概述.md 并存且仅概述在册（110/294/230/180 同族）
- A 占位符：通过（考据注为合规 WO-004 留痕）
- B 内容完整性：发现 1 处（史观段空心）
- C 编号与标题：通过（frontmatter CH328 与 H1 一致）
- D 格式规范：发现 1 类（文献行内嵌标题标记的粘连）
- E 学术规范：发现 2 处（chapter_matches 错挂；CIA 素材错配）
- F SUMMARY 一致性：不一致（本文件未收录，见问题清单第 4 项）
- 机械旗标复核：无（flags 为空）
- 问题清单：
  1. P1 | 行 35、41、44 | 文献行内嵌“---## 史料登记与辩证校准（2026-08-08 追加）> **本卷命题**：24.1 少数与多数……### 史料文献”“## 史料考据补充（2026-08-04 任务3 联网核验）> 主题：美国社区内部矛盾与排外……” | 结构粘连 ×3 处：章内小节标题（##/>/###）、“---”分隔线与本卷节号“24.1”引用全部挤入“## 文献”列表行内，标题不再成节（230/180 index 单行粘连同族，本文件为标题标记变体） | 将“史料登记与辩证校准”“史料考据补充”独立成节，行内“24.1”引用按本卷总览实际节号核正
  2. P2 | 行 19 | “匹配置信度 1.0，原因：澳大利亚 UNIX 社区史一手史料” | chapter_matches 错挂：本章为“美国：BSD 的发源地”，匹配原因却是“澳大利亚 UNIX 社区史”——素材库行错配至美国章（第 18 卷第 328 章 vs 澳大利亚章） | 重跑 chapter_matches 或删除该史料行
  3. P2 | 行 26 | “## 史观”段为“(待人工回填——详见子节文件史观/辨析字段)” | 史观段空心族（110/180 index 同族） | 按第 346 章先例从子节汇总回填；回填属整改线任务，登记不阻塞
  4. P2 | 行 31 | 辨析层“CIA 资助 MIT AI Lab 的具体金额与渠道……Church Committee 1976 年报告披露 CIA 在大学校园的资助网络” | 主题错配：CIA/MIT AI Lab 素材与“美国 BSD 发源地（伯克利 CSRG 地缘遗产）”章主题错位（更契合 DARPA 资助与伯克利 CSRG 的既有辨析线或第 3 卷）——同段“Bernstein 诉讼 1995-2002 与出口管制修订”尚可关联 | CIA 素材移至契合章或标注跨章背景
  5. P2 | 全文 | 章级双文件并存：index.md 未收录于 SUMMARY，在册者为概述.md | 结构族（110/294/230/180 同族）：保留/合并/迁移须主理人裁断 | DEFERRED 登记（P2-9 结构项），不阻塞循环
  6. P3 | 全文 | 章级 index 未列子节索引（325概述/87概述有“本章节索引”先例） | 索引缺失：读者无法从本章入口发现子节结构 | 补子节索引
- 结论：存在问题 6 项（P0 0、P1 1、P2 4、P3 1）

## 补充说明（正样本与复核留痕）

- **PODCAST 三期为美国社区史强证据群**：①EP261 FreeBSDCon 1999 回放（1999-10-17 伯克利首届、300 余人超预期约半、McKusick 教程讲两遍、六轨设置、Hubbard/Allison/Behlendorf keynotes、Wilfredo Sanshez 谈 Darwin——行 85 考据脚注明示“未与一手会议档案交叉核验”）；②EP270 MeetBSD 2018（Intel 圣克拉拉总部、首次独立程序委员会公开征稿、FreeBSD 25 周年庆典——行 75 总纲 18“二十五年才能成为二十五年项目”释读准确）；③BSDTalk EP21 的 SDF 谱系（Ted Uelman 1987 Apple II BBS→Operation Sun Devil 查封 killer.dallas.tx.us 转折→1991 LoneStar.org→2000 NetBSD/Alpha 全迁→pwd_mkdb/Berkeley DB 密码库瓶颈→两万活跃用户治理与 ARPA 会员级）——Operation Sun Devil 与 killer 站查封为真实事件，SDF 官方史可回源，是地区社区史采访的范本。
- **行 86 的转写讹误清单为全会话最详**（Ted Uelman 拼写、Texas Mitronet→Metronet、PWMICDB→pwd_mkdb、sdf.loanstar.org→lonestar.org、Kodak Interactive 存疑、System 5 Genics 噪音、MDG/MOU、BSD 1.1 所指待核）——八项逐一列出并给复核路径。
- 行 84 对 Hotmail/Yahoo 部署数字的年代语境存疑脚注（“1999 年报道数据……不宜当作现时部署规模”）规范。
- PODCAST 史观五条（总纲 18/10×2/6/8）条目名与权威表逐字全符；行 79 对 Alpha+NetBSD“边缘性作为生存策略”的本体论平等释读为总纲 8 的出色应用。
- OpenBSD 6.4（unveil/RETGUARD/QCOW2）与 OpenSSH 7.9（DSA CA 禁用、SHA-256 撤销）条目与 2018-10-25 发布日一致。
- 编码合规：UTF-8 无 BOM、LF；弯引号正确。
