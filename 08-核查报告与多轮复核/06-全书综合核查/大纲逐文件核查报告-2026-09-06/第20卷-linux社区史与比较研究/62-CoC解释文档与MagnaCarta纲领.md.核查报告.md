# 核查报告：第20卷-linux社区史与比较研究/62-CoC解释文档与MagnaCarta纲领.md

- 源文件：d:\librebsd\05-卷册大纲\第20卷-linux社区史与比较研究\62-CoC解释文档与MagnaCarta纲领.md（88 行，一次完整通读）
- 批次：L2004；检查日期：2026-09-14；检查方式：逐文件完整阅读人工核查（辅以 SUMMARY.md 实测第 3551/3631 行、字符级引号计数、49 个 ROW_MINE 锚与 1 条 NV 逐条清点及主题分布数字对账）
- SUMMARY.md 收录：实测第 3551 行“62 【Linux社区】CoC解释文档与MagnaCarta纲领”；同卷第 3631 行重复登记同一路径
- A 占位符：通过（词表命中 2 处经实读为误报：行 81、88 的 TODO 系内核源码树内 TODO 文件与 ARM legacy DT 实务用语，非内容空缺标记）
- B 内容完整性：发现 2 处（全 7 块五字段整体缺失；行 4 主题分布分类合计与判定条数差 1）
- C 编号与标题：发现 1 处（H1 自拟标题与 SUMMARY 收录标题不一致，且缺【Linux社区】显式标注）
- D 格式规范：发现 1 处（路径与文件名 3 处未加粗；引号体例合规，无禁用符号与 ASCII 直引号）
- E 学术规范：通过（49 个锚与 49 条 CAND 一一对应，无孤锚漏锚，1 条 NV 已如实计入页头；无禁引来源与禁用名称；史观字段整体缺失已在 B 项登记）
- F SUMMARY 一致性：不一致（同一文件在 SUMMARY.md 出现两次：第 3551 行与第 3631 行）
- 机械旗标复核：DUP_SUMMARY_ENTRY x2 经 SUMMARY.md 实测属实（第 3551 行与第 3631 行路径与标题逐字相同，均为“62 【Linux社区】CoC解释文档与MagnaCarta纲领”）；无 UNLISTED_NOT_IN_SUMMARY、无 SECTION_GAP

## 问题清单

1. P2 | 行 6-88（全 7 块） | 各块为“## 62.N 【Linux社区】题名”＋导语段＋“- 【Linux社区】… <!-- ROW_MINE: … -->”条目式，通篇无 要点/史料/史观/辨析/文献 字段标签 | 五字段体例整体缺失：00-总览 §一.2 定五字段为标准体例，本文件 7 块五项全缺；块内保有导语与带锚条目等实质内容，非单行空壳，故按体例系统性问题登记 | 按标准体例补五字段，或经卷级确认后明示本页采用“导语＋带锚条目”替代体例并登记为例外
2. P2 | 行 1 | “# 62. CoC 解释文档系列、Magna Carta 纲领与冷却令（ksd p114，pk 349906-349955）” | H1 与 SUMMARY 收录标题“62 【Linux社区】CoC解释文档与MagnaCarta纲领”不一致（H1 多出冷却令一节且无【Linux社区】标注） | 使 H1 与 SUMMARY 标题逐字一致
3. P3 | 行 4 | “判定：49 CAND / 1 NV。主题分布：Greg解释文档系列 8、保密承诺与报案权 11、CallToAction 5、MagnaCarta纲领 10、GITPULL与冷却令 5、程序之辩与Samba先例 2、2014档案与回归追踪 6、email措辞收束 1” | 对账数字不自洽：主题分布各项相加为 48，与同页判定 49 CAND 差 1 条（62.3 第 6 条 Pavel Acked Geert 删列表未归入任何分类） | 补记该条主题归属或修正分类计数，使分类合计等于 49
4. P3 | 行 41、66、87 | “已在 Documentation/process/code-of-conduct.rst”“jejb/linux-coc.git”“git.zytor.com/linux/tip-bot.git” | 路径与文件名未按 D 项要求加粗（该条要求路径、IP、文件名加粗且不篡改） | 分别改为加粗的 **Documentation/process/code-of-conduct.rst**、**jejb/linux-coc.git**、**git.zytor.com/linux/tip-bot.git**
5. P2 | SUMMARY.md 行 3551、3631 | 同一路径“第20卷-linux社区史与比较研究/62-CoC解释文档与MagnaCarta纲领.md”两次登记 | SUMMARY 重复收录（本卷 80 份同族，属卷级目录缺陷） | 删除其中一处重复条目

- 结论：存在问题 5 项（P0 0、P1 0、P2 3、P3 2）

## 补充说明（正样本与复核留痕）

- 引号体例为本批正样本：全文中文弯引号 60 对、中文单弯引号 8 处，ASCII 双引号 0 处、ASCII 单引号 0 处、全角直角引号 0 处，体例统一，可作为本卷引号规范的整改范本。
- 锚点与条数自洽（除主题分布一处差 1 已在问题清单登记）：全文 ROW_MINE 锚计 49 个，与页头“49 CAND / 1 NV”及 H1 括注的 pk 349906-349955 区间（共 50 号）相符，1 条 NV 已如实标注；7 个块的实际条目数（9/11/6/10/5/2/6）与锚数逐块对应，无孤锚漏锚。
- 卷级规定标记合规：块标题与每条条目均带【Linux社区】强制前缀，方头括号不在禁用符号之列；ROW_MINE 属数据库自动增补块标记，按纪律只登记不改写。
- 权力结构辩论两造长文并置为正样本：62.4 完整保留 NeilBrown 的 Magna Carta 纲领（现行文档 upside down、伤害不在虐待而在无力感、三条件）与 Ted 的技术质量论驳斥、Viro 的 petition 现实主义与双头制质问、Dan Carpenter 的两案自述（含十年前“女人懂什么编程”式羞辱案例），未以单方立场收束，属多方平等与经验优先的编纂正样本，契合总纲 8 与总纲 9。
- 指令链与责任归属留痕可反查：62.3 保留 Ted 关于指令、签署、时点皆出自 Linus、初始 commit 极少评审系因 -rc4 休假前不愿被认为背后搞鬼的权威叙事，与 62.6 Bottomley 自认“又在最后一分钟硬塞”的程序自省互证，属理论自反正样本，契合总纲 7。
- 权威审查与禁引来源核查：62.2 明载 LF 律师已审 CoC 与本补丁集（Ted 陈述、Greg 确认），全文未引用维基百科、百度百科一类禁引来源，未出现面向读者文本的禁用名称。
- 技术标识与文档标识原样保留未篡改：code_of_conduct(_interpretation)、:ref:、MAINTAINERS、conduct@kernel.org、kernel.org/code-of-conduct.html、coc-fixes for 4.19-rc8、8e630c31a3df、Fixes: 12 字符哈希、Link: lkml.kernel.org/r/<Message-Id>、Coverletter: 等均按原文著录，符合 D 项不篡改条款。
- 复核留痕：行数 88、中文弯引号 60 对、中文单弯引号 8 处、ASCII 双引号 0 处、ASCII 单引号 0 处、全角直角引号 0 处、ROW_MINE 锚 49 个、SUMMARY 行号 3551/3631，均为 2026-09-14 实测。
