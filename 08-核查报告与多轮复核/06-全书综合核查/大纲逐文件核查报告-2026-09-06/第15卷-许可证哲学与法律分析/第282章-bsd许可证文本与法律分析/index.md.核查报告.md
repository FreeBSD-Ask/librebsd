# 核查报告：第15卷-许可证哲学与法律分析/第282章-bsd许可证文本与法律分析/index.md

- 源文件：d:\librebsd\05-卷册大纲\第15卷-许可证哲学与法律分析\第282章-bsd许可证文本与法律分析\index.md
- 批次：C255；检查日期：2026-09-12；检查方式：逐文件完整阅读人工核查
- SUMMARY.md 收录：未收录（index.md 不入 SUMMARY；章页面为概述.md，UNLISTED 为机械层预期）
- A 占位符：通过（“考据完成：2026-07-30 三次联网核查”为合规完成注记）
- B 内容完整性：发现 2 处（辨析段三处残 stub——行 32“文献：Free Software Foundation.”、行 34“文献：GCC Steering Commit”（应为“Steering Committee”）截断、行 37 空“文献：”；行 45“要点：**BSD** 许可证原”截断）
- C 编号与标题：发现 2 处（行 25 空“## 2”标题；“## 282.1.4 史料辨析”重复出现两轮，行 43 与行 57）
- D 格式规范：发现 1 处
- E 学术规范：发现 1 处（史观伪标签五处；无禁引来源，无禁用名称）
- F SUMMARY 一致性：机械层预期
- 机械旗标复核：UNLISTED_NOT_IN_SUMMARY——惯例豁免；无 SECTION_GAP 旗标
- 问题清单：
  1. P1 | 行 19、21、27、30、33（五处） | “总纲第 14 条——许可证约束” | 史观条号伪标签集群（282.7 同族）：权威表第 14 条为“苦难不值得被提倡”；许可证主题宜挂第 13 条“法律与道德是利益分配”（同章 282.7 已同款整改） | 五处统一改挂第 13 条
  2. P1 | 行 25、29-35、43-51 | 结构破损群：空“## 2”标题；“## 282.1.4 史料辨析”重复两轮且内容互异；多处截断（行 29“文献：C”、行 32/35“文献：OSI. The Open Sourc”“文献：Cre”、行 45“要点：**BSD** 许可证原”）；URL 与机构名混粘（行 47“creativecommons.org/share-your-work/licensing-types-examples/；SPDX>”、行 49“opensource.org/osd；FSF>”、行 51“…zero/1.0/；FSF>”、行 62“opensource.org/osd；FSF>”、行 63“…zero/1.0/；FSF>”、行 65“…license/isc/；SPDX>”、行 66“…/；OSI>”） | 字节截断族＋URL 与机构名混粘叠加，为全会话 URL 污染最重一例 | 回源重建；URL 逐条剥离机构名
  3. P2 | 行 20 vs 行 39 | “考据完成：2026-07-30 三次联网核查确认——William Hoskins 职务为 Director, Office of Technology Licensing…”完整段重复出现两轮（行 20 史观段内与行 39 辨析段内），且两轮均在“OTL 即 Office of Technology Licensing 的缩写疑问”处截断 | 同一考据完成注记重复并同点截断 | 去重并回源补全
  4. P3 | 行 31、48（重复） | “编号防错——FSD 四自由官方编号为 0–3，NC 违反自由0（不是‘第1条’），ND 违反自由1+自由3…” | 内容为全库罕见的标准化编号防错正样本（重复亦应去重后保留单份） | 去重保留
- 结论：存在问题 4 项（P0 0、P1 2、P2 1、P3 1）

## 补充说明（正样本与复核留痕）

- 行 15 的 CC 六协议四要素表述（BY/SA/NC/ND 排列＋CC0）与版本沿革（CC 1.0 美国法移植版→2.0-3.0 多司法辖区移植→4.0 国际版“不再以司法辖区移植”）准确且为全库罕见的 CC 体系叙述。
- 行 31/48 的“编号防错”条目为标准化引用的正样本：FSD 四自由官方编号 0-3、NC 违反自由 0、ND 违反自由 1+3、OSD 须用 §1/§3/§6 条款号——防“第 1 条”式口语错引；行 34 的“CC-BY-SA 与 GPL 同为 share-alike 但适用对象与传染边界不同，不得混同；CC0 含‘不得反悔’条款”辨析精确。
- 行 11-14 的 BSD 许可证谱系（4-Clause 广告条款→1999-07-22 Hoskins 公告弃用→3-Clause New BSD→2006 简化为 2-Clause；MIT 等价；Apache 2.0 专利授权）与同章 282.7 文件（C250 报告）的逐版本考据互证一致。
- PODCAST_REVIEW 双块与许可证章主题对位：EP232 的宽容 vs copyleft 辩证（“两阵营均自称捍卫自由，一者保护代码自由，一者保护使用者自由”）、ZFS/OpenZFS/Oracle ZFS 三分术语辨析；BSDTalk EP200 的 mg 编辑器 public domain 重构（逐个联系在树作者收束版权、“仅 theo mode 一个文件仍持 BSD 许可”——theo mode 系输出 de Raadt 语录的社区自嘲彩蛋）、Wooding 的 IPF→PF 大分裂亲历与 OpenBSD Foundation 创始董事身份——块内史观五条（总纲 6/4/10/13/10）与权威表逐字相符；Shell Wooding→Kjell Wooding、Theodore Atth→Theo de Raadt 音误校正挂 L4 存疑；行 83 “public domain 在瑞典等法域仍有法律适用问题”的法域 nuance 准确。
- 编码合规：UTF-8 无 BOM、LF；主体弯引号正确（截断与混粘处除外）。
