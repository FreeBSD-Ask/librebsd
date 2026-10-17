# 150 【Linux社区】python实测与2.2TAB结果

> 来源：ksummit 独有 p14（50 封全读，2021-04 至 2026-08，kernel-doc python3.13/3.9/3.6 耗时 31.7/59/76.5 秒实测、2022 TAB 选举 960 选民 267 票五人当选、git 统计 Fixes 仅约 2% 针对已发布版缺陷、Link-Origin/Origin 标签提案、soc-tools.git 钩子工具集、BPF CI 需专人值守倦怠论、AI 补丁回迁训练设想）
> 判定：43 CAND / 7 NV。主题分布：Rust kernel policy 1、稳定分支提交标签提案 2、DRM panel API 现代化 1、退役 bugzilla 1、trivial 补丁接受政策（UMN 事件） 1、AI 与 LLM 在内核流程中的角色 1、加速器驱动的用户态要求 1、b4 新维护者功能 1、每 cgroup 交换分区控制 1、linux-next 反馈 2、Rust 议题征集 1、替换 Link 尾注 2、工具生成内容指南 1、文件系统信任与维护 2、linus-next 功能测试 1、加速器驱动用户态要求 1、bugzilla 变更计划 2、Rust 内核策略（cleanup 属性） 1、Rust for Linux 议题 2、trivial 补丁接受政策 1、Rust 内核政策 2、TAB 选举 CIVS opt-in 1、应对新开发者洪流 1、内核文档议题 1、C 聚合传参（Rust 策略） 1、2022 TAB 选举结果 1、工具生成内容指南 v2 1、设备直通 2、C 聚合传参（gccrs） 1、LLM 相关议题 1、AI 补丁审查工具 1、API 弃用强制 1、sashiko 审查模型 1、AI 辅助代码标注 1、维护者倦怠 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p14 的逐封提取（2021-04 至 2026-08，43 CAND / 7 NV），全 35 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 150.1 Rust 内核政策

- 【Linux社区】认同改进 C 侧接口可使 C 与 Rust 双方受益，回顾合并前尽量不动 C 头文件的策略及其后来演变。 `<!-- ROW_MINE: ksummit.messages.2075 -->`

## 150.2 稳定分支提交标签提案

- 【Linux社区】提议在机器人提示文本中补充 stable+noautosel 及理由写法，并预判此类提醒邮件会随大家熟悉而减少。 `<!-- ROW_MINE: ksummit.messages.2077 -->`
- 【Linux社区】提出补丁元数据光谱 No-Fixes 到 Fixes 到 Fixes&Stable，维护者尽责标注，fork 方据元数据自行决策。 `<!-- ROW_MINE: ksummit.messages.2201 -->`

## 150.3 DRM panel API 现代化

- 【Linux社区】提交 Kernel Summit track 议题：panel API 缺原子支持与 DDIC 高级特性，致上下游碎片化与维护负担。 `<!-- ROW_MINE: ksummit.messages.2078 -->`

## 150.4 退役 bugzilla

- 【Linux社区】细化 bug@kernel.org 机器人提案：以该地址为触发标记，LLM 解码栈回溯定位提交者并转发对应列表，认同回归标记。 `<!-- ROW_MINE: ksummit.messages.2079 -->`

## 150.5 trivial 补丁接受政策（UMN 事件）

- 【Linux社区】质疑 UMN 作者“补丁均出于善意”说法，列举学生与导师诚信的多种可能，指出涉事提交未公开撤回。 `<!-- ROW_MINE: ksummit.messages.2081 -->`

## 150.6 AI 与 LLM 在内核流程中的角色

- 【Linux社区】主张 git 历史含完整补丁路径可供 LLM 用于回迁补丁，并谈 AI 助力测试覆盖及 selftests 各自为政问题。 `<!-- ROW_MINE: ksummit.messages.2109 -->`

## 150.7 加速器驱动的用户态要求

- 【Linux社区】反驳“小众设备留在树外”说，重申上游优先是数十年的立场，发行版并非主要使用场景，habanalabs 非搭便车。 `<!-- ROW_MINE: ksummit.messages.2114 -->`

## 150.8 b4 新维护者功能

- 【Linux社区】提交技术议题：介绍 b4 review 与 b4 bugs 新特性如何助过载维护者保持去中心化开发。 `<!-- ROW_MINE: ksummit.messages.2117 -->`

## 150.9 每 cgroup 交换分区控制

- 【Linux社区】确认已按指引把议题提交从 Kernel Summit track 改投 LPC MM MC，属议题提交流程记录。 `<!-- ROW_MINE: ksummit.messages.2118 -->`

## 150.10 linux-next 反馈

- 【Linux社区】表态其 next 分支仅在最后手段时 rebase，以免“补丁加修复”成对进入上游，顾全可二分性。 `<!-- ROW_MINE: ksummit.messages.2129 -->`
- 【Linux社区】分享 soc-tools.git 维护者钩子工具集与安装脚本，称 Fixes 标签错误或缺 SoB 已无可借口。 `<!-- ROW_MINE: ksummit.messages.2231 -->`

## 150.11 Rust 议题征集

- 【Linux社区】提交技术议题：列出 kernel crate 拆分、外部 crate 依赖、工具链与 GCC 构建、CI 集成、rustdoc 等方向。 `<!-- ROW_MINE: ksummit.messages.2145 -->`

## 150.12 替换 Link 尾注

- 【Linux社区】指出 Link: 已成“大杂烩”，本质是命名空间问题，提议新增 Link-Origin 或 Origin 标签以明确语义。 `<!-- ROW_MINE: ksummit.messages.2150 -->`
- 【Linux社区】纠正 Doug 引错 Sasha 的 RFC 并给出正确链接，顺势示范按主题搜索会找错结果的问题。 `<!-- ROW_MINE: ksummit.messages.2181 -->`

## 150.13 工具生成内容指南

- 【Linux社区】反对文档开头就“摆臭脸”，主张面向愿意守规的人应更友善，AI slop 肇事者本就不会去读文档。 `<!-- ROW_MINE: ksummit.messages.2152 -->`

## 150.14 文件系统信任与维护

- 【Linux社区】指出 X-mount.auto-fstypes 否定写法歧义，并提醒未来文件系统若以 no 开头命名会撞语义。 `<!-- ROW_MINE: ksummit.messages.2154 -->`
- 【Linux社区】反驳用户态化会更受维护，但认同系统级影响会减轻，提及 LSFMM 曾短议弃用文件系统转 FUSE。 `<!-- ROW_MINE: ksummit.messages.2243 -->`

## 150.15 linus-next 功能测试

- 【Linux社区】说明脚本按 commit ID/patch-id/主题三键匹配以容忍 rebase 与改题，改动大则计时归零，反对 pending-fixes 因增延迟。 `<!-- ROW_MINE: ksummit.messages.2156 -->`

## 150.16 加速器驱动用户态要求

- 【Linux社区】澄清上游无线驱动并无闭源监管 blob，监管合规经 regulatory.db 或固件完成。 `<!-- ROW_MINE: ksummit.messages.2157 -->`

## 150.17 bugzilla 变更计划

- 【Linux社区】主张没有更优替代品，Red Hat 与 OpenSuse 等有实力续命 bugzilla，或雇 patchwork 团队写“bugwork”。 `<!-- ROW_MINE: ksummit.messages.2159 -->`
- 【Linux社区】以 git 统计修正论据：v5.18..v5.19 的 2531 个 Fixes 中仅约 2%（54 个）针对已发布版的既有缺陷。 `<!-- ROW_MINE: ksummit.messages.2178 -->`

## 150.18 Rust 内核策略（cleanup 属性）

- 【Linux社区】质疑 _cleanup_ 注解在无引用计数下有 use-after-free 与双重释放风险，宁忘 free 也不愿忘置 NULL。 `<!-- ROW_MINE: ksummit.messages.2187 -->`

## 150.19 Rust for Linux 议题

- 【Linux社区】提出关键技术疑问：Rust 是否支持 fentry/mcount，否则 ftrace 对所有 Rust 驱动形同全局 notrace。 `<!-- ROW_MINE: ksummit.messages.2188 -->`
- 【Linux社区】澄清升级调用可不 panic 而以 fallible 与 Option 表达失败，失败后的处理取决于调用方。 `<!-- ROW_MINE: ksummit.messages.2202 -->`

## 150.20 trivial 补丁接受政策

- 【Linux社区】回应 quilt 修复难度：并不难但需懂 bash 与 Perl，自述曾几乎修成而搁置。 `<!-- ROW_MINE: ksummit.messages.2189 -->`

## 150.21 Rust 内核政策

- 【Linux社区】治理立场：政策必须放进内核树，网页形式按流程可被直接无视，并调侃 LF 与 korg 之别。 `<!-- ROW_MINE: ksummit.messages.2193 -->`
- 【Linux社区】以 NVMe、binder、Puzzlefs、Apple AGX 等在树 Rust 驱动反驳“驱动未必写得成 Rust”的前提质疑。 `<!-- ROW_MINE: ksummit.messages.2236 -->`

## 150.22 TAB 选举 CIVS opt-in

- 【Linux社区】报告已完成 opt-in 并输入确认码仍无处投票，暴露 TAB 选举流程故障，属流程记录。 `<!-- ROW_MINE: ksummit.messages.2194 -->`

## 150.23 应对新开发者洪流

- 【Linux社区】提议更聪明的欢迎机器人：检测空白损伤、不适用于上游等情形并给新贡献者针对性建设性提示，可并入 Sashiko。 `<!-- ROW_MINE: ksummit.messages.2200 -->`

## 150.24 内核文档议题

- 【Linux社区】实测 kernel-doc.py 在 python3.13/3.9/3.6 下分别约 31.7 秒、59 秒、76.5 秒，证明 Python 版本是慢因之一。 `<!-- ROW_MINE: ksummit.messages.2205 -->`

## 150.25 C 聚合传参（Rust 策略）

- 【Linux社区】主张必须维持兼容性并举 python-3 教训，认为 C 可把部分警告升级为错误但不能擅改位运算优先级。 `<!-- ROW_MINE: ksummit.messages.2214 -->`

## 150.26 2022 TAB 选举结果

- 【Linux社区】公布 960 名合格选民、267 张选票及当选五人名单，并致谢卸任主席 Chris Mason，属治理流程记录。 `<!-- ROW_MINE: ksummit.messages.2221 -->`

## 150.27 工具生成内容指南 v2

- 【Linux社区】逐节评论 TAB 补丁：忧媒体报道引发 AI 补丁洪流，主张先严后松，明确“专家在环”与整批拒绝权。 `<!-- ROW_MINE: ksummit.messages.2229 -->`

## 150.28 设备直通

- 【Linux社区】质疑 CXL 多节点互通缺节点级授权的安全模型，主张 fwctl 尽量覆盖命令但受定义的安全模型约束。 `<!-- ROW_MINE: ksummit.messages.2230 -->`
- 【Linux社区】建议把该议题并入 LPC Complex Camera MC 的 V4L2 与 DRM 讨论，称两者覆盖面高度重叠。 `<!-- ROW_MINE: ksummit.messages.2241 -->`

## 150.29 C 聚合传参（gccrs）

- 【Linux社区】说明 gccrs 以 VaListImpl lang item 特判 LLVM 依赖代码，无需分叉标准库，并多路对比 rustc 行为保兼容。 `<!-- ROW_MINE: ksummit.messages.2235 -->`

## 150.30 LLM 相关议题

- 【Linux社区】分享 16GB 显存下 Qwen-3.6 35B 等小模型可查出真实 bug 的实测结论及 kernel-review-agent 代码。 `<!-- ROW_MINE: ksummit.messages.2239 -->`

## 150.31 AI 补丁审查工具

- 【Linux社区】支持鼓励 AI 预审以减 v1 往返，反对强制依赖专有或非本地工具，并以 bitkeeper 类比便利化陷阱。 `<!-- ROW_MINE: ksummit.messages.2247 -->`

## 150.32 API 弃用强制

- 【Linux社区】提交维护者峰会议题：描述弃用 API 仍被新增调用的困境，列举 checkpatch、构建机器人等四种方案。 `<!-- ROW_MINE: ksummit.messages.2250 -->`

## 150.33 sashiko 审查模型

- 【Linux社区】澄清 Mason 的 review-prompts 由 Sashiko 拉取故两边都提交，并问是否也存在反向同步。 `<!-- ROW_MINE: ksummit.messages.2254 -->`

## 150.34 AI 辅助代码标注

- 【Linux社区】结合 Copilot 诉讼分析 AI 产出著作权认定未定，主张标注 AI 参与以便法律有变时可复查或移除。 `<!-- ROW_MINE: ksummit.messages.2256 -->`

## 150.35 维护者倦怠

- 【Linux社区】介绍 BPF CI 需专人值守的现状，指倦怠主因是补丁洪流，呼吁文化转型让活跃开发者兼做审查。 `<!-- ROW_MINE: ksummit.messages.2258 -->`
