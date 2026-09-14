# 核查报告：第20卷-linux社区史与比较研究/66-SubsystemProfile评审与可信名单之争.md

- 源文件：d:\librebsd\05-卷册大纲\第20卷-linux社区史与比较研究\66-SubsystemProfile评审与可信名单之争.md（196 行，一次完整通读）
- 批次：L2004；检查日期：2026-09-14；检查方式：逐文件完整阅读人工核查（辅以 SUMMARY.md 实测第 3555/3635 行、字符级引号计数、48 个 ROW_MINE 锚与 2 条 NV 逐条清点及主题分布数字对账）
- SUMMARY.md 收录：实测第 3555 行“66 【Linux社区】SubsystemProfile评审与可信名单之争”；同卷第 3635 行重复登记同一路径
- A 占位符：通过（全文无 TODO/FIXME/待补/占位一类空缺标记）
- B 内容完整性：发现 1 处（全 48 块五字段整体缺失，块沦为单条目标题行）
- C 编号与标题：发现 2 处（H1 自拟标题与 SUMMARY 收录标题不一致；H1 括注缺 pk 区间，与同批各页体例不齐）
- D 格式规范：发现 1 处（路径与脚本文件名多处未加粗；引号体例合规，无禁用符号与 ASCII 直引号）
- E 学术规范：通过（48 个锚与 48 条 CAND 一一对应，无孤锚漏锚，2 条 NV 已如实计入页头；主题分布数字自洽；无禁引来源与禁用名称；史观字段整体缺失已在 B 项登记）
- F SUMMARY 一致性：不一致（同一文件在 SUMMARY.md 出现两次：第 3555 行与第 3635 行）
- 机械旗标复核：DUP_SUMMARY_ENTRY x2 经 SUMMARY.md 实测属实（第 3555 行与第 3635 行路径与标题逐字相同，均为“66 【Linux社区】SubsystemProfile评审与可信名单之争”）；无 UNLISTED_NOT_IN_SUMMARY、无 SECTION_GAP

## 问题清单

1. P1 | 行 6-196（全 48 块） | 各块为“## 66.N 【Linux社区】题名”＋单条“- 【Linux社区】… <!-- ROW_MINE: … -->”，无导语段亦无任何字段行，如行 6-8 的 66.1 仅一句即收束 | 内容实质缺陷（丙型）：48 块五字段（要点/史料/史观/辨析/文献）整体缺失致块沦为单行，仅为标题加一条判定摘要，远低于 00-总览 §一.2 五字段标准 | 按标准体例补 要点/史料/史观/辨析/文献 五字段，或经卷级确认后明示本页采用单行摘要体例并登记为例外
2. P2 | 行 1 | “# 66. Subsystem Profile 评审与可信名单之争（ksd p118）” | H1 与 SUMMARY 收录标题“66 【Linux社区】SubsystemProfile评审与可信名单之争”不一致（H1 词形与空格不同且无【Linux社区】标注） | 使 H1 与 SUMMARY 标题逐字一致
3. P3 | 行 1 | H1 括注仅“（ksd p118）” | 体例不齐：同批 52 至 62 号各页 H1 括注均为“ksd pNNN，pk XXXXXX-XXXXXX”格式，本页缺 pk 区间，不利下游反查 | 补记 pk 区间 350106-350155
4. P3 | 行 12、36、60、92、148 | “新增 Documentation/maintainer/subsystem-profile.rst”“补丁教 get_maintainers.pl 打印”“在 index.rst 加指针”“scripts/get_maintainer.pl 采集”“仿 spdxcheck.py 独立成脚本” | 路径与脚本文件名未按 D 项要求加粗（该条要求路径、IP、文件名加粗且不篡改） | 分别改为加粗的 **Documentation/maintainer/subsystem-profile.rst**、**get_maintainers.pl**、**index.rst**、**scripts/get_maintainer.pl**、**spdxcheck.py**
5. P2 | SUMMARY.md 行 3555、3635 | 同一路径“第20卷-linux社区史与比较研究/66-SubsystemProfile评审与可信名单之争.md”两次登记 | SUMMARY 重复收录（本卷 80 份同族，属卷级目录缺陷） | 删除其中一处重复条目

- 结论：存在问题 5 项（P0 0、P1 1、P2 2、P3 2）

## 补充说明（正样本与复核留痕）

- 引号体例为本批正样本：全文中文弯引号 18 对，ASCII 双引号 0 处、全角直角引号 0 处，体例统一，可作为本卷引号规范的整改范本。
- 锚点与条数完全自洽：全文 ROW_MINE 锚计 48 个，与页头“48 CAND / 2 NV”相符，2 条 NV 已如实标注；页头主题分布逐项列出 48 个主题各 1 条，合计恰为 48，与 48 个块一一对应，无孤锚漏锚。
- 卷级规定标记合规：块标题与每条条目均带【Linux社区】强制前缀，方头括号不在禁用符号之列；ROW_MINE 属数据库自动增补块标记，按纪律只登记不改写。
- 完整评审链留痕为正样本：本页保留 Dan Williams 的 RFC 补丁、14 项维护政策模板、libnvdimm 首个样例与 media 样例 Profile 的全文评审链，从 P: 标签回收提案到 v2 改进承诺、受众改写承诺与 media 样例补正，逐轮回应可反查，属动手者叙事正样本，契合总纲 10。
- 名单存废的多方对读留痕：66.18、66.21、66.42 保留 Leon Romanovsky 与 Rodrigo Vivi 关于可信评审人名单弊大于利、小圈子不可扩展的主张，66.20、66.31、66.32、66.44 保留 Mauro 的改名折中与量化入列标准、Dan Williams 的名单辩护与“未顾及不幸解读”自认，66.33 保留 Jan Kara 对名单如何帮新人的追问，66.47 保留 NeilBrown 关于被授头衔后心态由 someone should 转为 I should 的第一人称证言，未以单方立场收束，属多方平等与经验优先的编纂正样本，契合总纲 8 与总纲 9。
- 档案信与当期议题区分明确：66.7、66.17、66.28、66.38、66.39 均以“2014 年档案信”起首标注时间域，与 2018-11 当期评审链区分清楚，避免时间混淆，属编纂规范的正样本。
- 技术标识原样保留未篡改：P:/M:/E:/R: 标签、SOB、MAINTAINERS、get_maintainer.pl、patchwork、-rc5/-rc7、dev_get_property()、get_of_pdata()/get_acpi_pdata()、_DSM、ASL Package、sched_getattr/sched_setattr、fallocate、cgroup、user ns、man7.org/tlpi/api_changes、Olson 命名、videobuf2、V4L2/CEC 等均按原文著录，符合 D 项不篡改条款。
- 行 112 的 ASCII 单引号出现在人名“Ted Ts'o”中，属姓名原拼写，按 D 项豁免条款不记问题。
- 复核留痕：行数 196、块数 48、中文弯引号 18 对、ASCII 双引号 0 处、ASCII 单引号 1 处（人名内）、全角直角引号 0 处、ROW_MINE 锚 48 个、SUMMARY 行号 3555/3635，均为 2026-09-14 实测。
