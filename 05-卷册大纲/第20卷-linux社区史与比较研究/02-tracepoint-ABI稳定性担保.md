# 02 【Linux社区】tracepoint-ABI稳定性担保

> **性质**：13-deepseek-linux 战线 P4 大纲增补（ksummit-discuss 主题审读产物）
> **来源线程**：[topic proposal] tracepoints and ABI stability warranties（2016-09，p64，pk 347406–347455 区间）
> **建立**：2026-09-10 首建；2026-09-11 依 claim 库重建（原文件丢失，以 `dslinux_claims.duckdb` 为唯一反查源）
> **关联**：claim 均坐落在 `dslinux_claims.duckdb` claim 表，每条以 `<!-- ROW_MINE: ... -->` 锚定

## 【Linux社区】零、自反性声明

本增补块是对 ksummit-discuss 2016 年 9 月 tracepoint ABI 议题邮件的形式化提取，为“Linux 内核用户态 ABI 哲学”提供当事人一手语料；不声称该讨论即“ABI 史”全貌，“永不稳定”等主张系讨论内立场而非本书结论。

---

## 2.1 【Linux社区】tracepoint 是否属用户态 ABI：分歧起点

- **要点**：Shuah Khan 投出 patch 引出议题，提出“何类内核信息该不该经 tracepoint/调试机制暴露”；Rostedt 以“仅在内核命令行加 this-kernel-is-broken 才启用某组 tracepoint + 大横幅警告”为折中方案定义“只有破坏现有工具才成问题”，并引 Linus 2012-12-23 名言“破坏用户态是内核 bug，绝不怪用户程序”。
- **史料**：`347406/347411/347417`（Rostedt）、`347408`（Shuah 自陈）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347406 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347411 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347417 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347408 -->`
- **史观**：经验优先（总纲 9：当事人自陈写 tracepoint 经历）；拒绝进步叙事（总纲 1/3：“从未把 tracepoint 当 ABI”乃历史偶然、非必然进程）
- **辨析**：Linus 名言系 2012-12-23 邮件（非 ksummit）——本块只引其被转述句，落书时应回溯原始邮件核实原文
- **文献**：`ksummit-discuss.messages.347406/347408/347411/347417`（2016-09“[topic proposal] tracepoints and ABI stability warranties”线程，Rostedt/Shuah Khan 两组邮件），全文见 `raw_source.raw_json`

## 2.2 【Linux社区】支持“永不稳定”的修正派（Dobriyan / Viro / Lutomirski）

- **要点**：Alexey Dobriyan 以 `TRACE_EVENT(sched_switch).prev_state` 为 long（历史遗留、本可 int）证明字段已事实成 ABI，并引 RHEL“Scope of Compatibility”四档（Level 4 = No compatibility）主张“制胜之道是不入场、让发行版自己解决”；Al Viro 给出“坏 API → 大量 box 依赖丑形态 → 内核改 → 守护进程作者抱怨 → Linus 骂你”五步反例；Andy Lutomirski 主张“tracepoint 永不稳定”、甚至周期性故意改动以点明，类比 Windows 下生产程序调用 WinDbg 接口日后的下场。
- **史料**：`347409/347410`（Dobriyan）、`347421`（Viro）、`347422/347424`（Lutomirski / Vlastimil Babka 支持）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347409 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347410 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347421 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347422 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347424 -->`
- **史观**：动手者叙事（总纲 10）——争论双方都是动手者，Dobriyan 的 gfp_t 重排禁例（347421）是内核内部焊死的实证
- **辨析**：Viro 的“五步”是**危机论证**而非字面流程，须按原文转述；RHEL 兼容级别是发行版口径
- **文献**：RHEL 兼容性文档（二手）在 347409 中被引

## 2.3 【Linux社区】发行版携带补丁的现实（Jan Kara 与厂商数据）

- **要点**：Jan Kara 给出综合数据——SLE12 SP2 基于 4.4.19、携带约 4,700 个补丁（增删 39 万行），其中约 280 个非上游回溯（增删 3.5 万行）；Linus Walleij 断言 Windows 采购级“上游存在性纳入 SoC 采购”是唯一真正改变整家公司行为的机制；Vinod Koul（Intel）补充 Brillo 已采用类 ChromeOS 上游策略。
- **史料**：`347425`（Kara 数据）、`347443/347445`（Walleij / Koul）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347425 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347443 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347445 -->`
- **史观**：经验优先（总纲 9：用补丁数/行数等定量证据而非印象，兼取当事人自陈）
- **辨析**：4,700 与 280 是**当时**快照，须注明日期口径；Kara 是 SUSE 代表，有立场但数据可复核
- **文献**：本组 claim 为一线邮件（347425/347443/347445），直接著录 `raw_source`；SUSE SLE12 SP2 补丁统计为 Kara 现场口径

## 2.4 【Linux社区】tracepoint 语义稳定性与 ftrace 现实（Masami Hiramatsu）

- **要点**：Masami 区分 formal（可机器读）与 semantic（须读码/注释）两类信息，主张各 tracepoint 需保证“用户拿来用”的最低限度；自陈写 systemtap flight-recorder 模式（后台记录、出事 dump），并点出 ftrace 本有 panic 场景支持；结论是“强依赖内核内部故不应视作稳定 API”。
- **史料**：`347435/347439/347440`
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347435 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347439 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347440 -->`
- **史观**：经验优先（总纲 9：flight-recorder 实例）、动手者叙事（总纲 10）
- **辨析**：/proc/*/pagemap 导出裸 page flags 的群嘲案例（347444 中 Dobriyan 引）说明“稳定排查接口 vs 稳定 ABI”之辨须拆开陈述
- **文献**：本组 claim 为一线邮件（347435/347439/347440），直接著录 `raw_source`；ftrace 机制说明可参内核树 `Documentation/trace/ftrace.txt`（参照）

## 2.5 【Linux社区】会议形态学：议题被一步步“从 patch 到议题”的过程

- **要点**：本线程展示了内核峰会议题如何由“Shuah 的 patch”长成一节专门议题——从 issue 提案（Corbet 将文件名打字错误）、到警惕反例、到三阵营（永不稳定/字段事实 ABI/维护者自制）、再到会场 Order（周三上午 10 点 printk 会议）。该过程本身是 BSD 史学史的“讨论生成的治理”样本。
- **史料**：`347405` 起至 `347444` 整段〔存疑：原记止号 `347255` 方向颠倒，且经候选库复核 347255 实为另一线程（Rostedt 论雇主付费代码版权，2016-08-29）之邮件；本页 tracepoint 线程止于 `347444`（Dobriyan 例证），报告所疑之 `347455` 亦系 Mark Brown 论 USB 充电之别线程邮件，故止号订为 `347444`〕；核心渲染见 `347634`（Ts'o 排程）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347405 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347444 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347634 -->`
- **史观**：循环结构呈现（总纲 4：议题多年回归）、偶然性优先（总纲 5：由个例 patch 触发）
- **辨析**：本款为“过程分析”，区分“事实”与“我的解读”——解读限于括号内
- **文献**：本组 claim 为一线邮件（347405/347444/347634），直接著录 `raw_source`