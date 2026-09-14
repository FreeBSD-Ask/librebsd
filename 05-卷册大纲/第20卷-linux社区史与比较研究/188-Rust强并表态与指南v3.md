# 188 【Linux社区】Rust强并表态与指南v3

> 来源：ksummit 独有 p52（50 封全读，2022-10 至 2025-02：Hellwig 披露 Linus 私下表态将无视维护者反对强并 Rust 并预言绑定代码蔓延与多语言碎片化系重磅反方一手立场；Dave Hansen 提交 TAB 集体产出工具生成内容指南 v3 补丁全文 97 行规则文本附 8 位维护者 Reviewed-by；Ted Ts'o 提出 DCO 与 AI 生成代码四项法律问题清单含是否强制披露模型与提示词是否记录；Andrew Morton 明确 AI 找缺陷已可用写补丁尚无用并划红线任何新规不得妨碍接收 AI 缺陷报告；Bugzilla 改革四封、AI 生成内容指南四封、加速器用户态接口三封）
> 判定：43 CAND / 7 NV。主题分布：Bugzilla 改革 4、UMN 假补丁事件 1、CXL RAS 与 EDAC 1、加速器用户态接口 3、维护者峰会存废 3、cleanup.h 规则之争 3、bcachefs 治理反思 1、设备树绑定独立仓库 1、kernel.org 信任工具 1、KTODO 工具提案 1、AI 审查工具 1、AI 生成内容指南 3、补丁审阅工具 1、DCO 与 AI 披露 1、琐碎补丁收件政策 1、devres 混用检测 1、AI 照片权限方案 1、Rust 内核政策 1、Rust 测试环境 1、设备透传争论 1、ORC 栈回溯 1、C 聚合传参之争 3、io_uring BPF 议题 1、HIGHMEM 淘汰 1、LLM 测试生成 1、stable 补丁标记 1、内核文档改革 1、LKML 通配剥离 1、Sphinx 构建工具 1、TAB 选举 1。

## 188.1 Bugzilla 改革

- **要点**：Slade Watkins 提议在 Bugzilla 减痛改革中设“联络人”衔接终端用户与开发者并代为分流，自称已两次表态愿承担此职，询 Leemhuis 是否采纳。Konstantin Ryabitsev 提议把新缺陷与评论汇入 public-inbox 数据流，可经 lore.kernel.org 与 lei 查询；战略是用可镜像的查询式订阅避免单点故障，无需全员换工作流。Artem 确认其提案实质：仅为出现在 MAINTAINERS 中的维护者自动创建 bugzilla 账号以便人工分流时抄送，并非设为默认指派，不会带来垃圾邮件。Artem 力主保留 Bugzilla：驳 GitLab 迁移（商业开源核被收购风险、单点可瘫痪），提议刷新组件、按近半年提交记录订阅开发者，或改 Discourse 八论坛；称 Linus 曾经 Bugzilla 解决其 LKML 无回应的问题。
- **史料**：`ksummit.messages.8070`（Slade Watkins，2022-10-03）、`ksummit.messages.8128`（Konstantin Ryabitsev，2022-09-29）、`ksummit.messages.8156`（Artem S. Tashkinov，2022-10-04）、`ksummit.messages.8198`（Artem S. Tashkinov，2022-09-29）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8070 -->` `<!-- ROW_MINE: ksummit.messages.8128 -->` `<!-- ROW_MINE: ksummit.messages.8156 -->` `<!-- ROW_MINE: ksummit.messages.8198 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：联络人制、public-inbox 汇流、自动建号与保留 Bugzilla 四说并置）；偶然性优先（总纲第 5 条——没有必然性，只有偶然性：改革方向由 GitLab 收购风险等外部事态牵引）
- **辨析**：四条分属 2022-09 至 2022-10 的同一改革线程；“Linus 曾经 Bugzilla 解决其 LKML 无回应的问题”系 Artem 转述，落书须与 Linus 原话核对。
- **文献**：DSLXC-10833、DSLXC-10844、DSLXC-10852、DSLXC-10869（`ksummit.messages.8070`、`ksummit.messages.8128`、`ksummit.messages.8156`、`ksummit.messages.8198`，2022-10-03、2022-09-29、2022-10-04、2022-09-29），全文见 `raw_source.raw_json`

## 188.2 UMN 假补丁事件

- **要点**：Kozlowski 引明尼苏达大学计算机系 4 月 21 日官方声明，质疑其 IRB 审查有效性；指出 uwn.net 缺陷提交真伪不明，信任破坏后无法验证研究是否已停止。
- **史料**：`ksummit.messages.8074`（Krzysztof Kozlowski，2021-04-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8074 -->`
- **史观**：法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：研究伦理争议落在 IRB 审查权与责任归属上）；自反性声明（总纲第 7/23 条——理论必须自反／一切历史写作都是基于哲学设定的历史小说：明示信任破坏后已无法验证研究是否停止，即证据链自身受损）
- **辨析**：本块系 Krzysztof Kozlowski 的质疑；“uwn.net 缺陷提交真伪不明”为当事人判断，本页未附鉴定结论。
- **文献**：DSLXC-10834（`ksummit.messages.8074`，2021-04-22），全文见 `raw_source.raw_json`

## 188.3 CXL RAS 与 EDAC

- **要点**：Borislav Petkov 澄清对 CXL RAS 报告系列的意见：并非要求全新设计，而是建议直接复用既有 EDAC 子系统，反问为何要另起炉灶。
- **史料**：`ksummit.messages.8075`（Borislav Petkov，2024-07-29）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8075 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以既有 EDAC 子系统这一可复用实存为判据）；多方平等（总纲第 8 条——本体论上各方平等：新设计与复用旧子系统两说并置）
- **辨析**：本块系 Borislav Petkov 的意见澄清；“反问为何要另起炉灶”属评审立场，非否决结论。
- **文献**：DSLXC-10835（`ksummit.messages.8075`，2024-07-29），全文见 `raw_source.raw_json`

## 188.4 加速器用户态接口

- **要点**：Daniel Vetter 认同 AI 计算本质受限于矩阵乘，但称 BLAS 接口对可编程设备过浅；小型 SoC NPU 可用固定接口，且不应允许厂商私有扩展或旁路上传编译产物。Mauro 指出死锁：若新内核 API 须待发行版先收用户态实现则新 API 永难落地，他作为 Fedora 维护者即会拒绝；并以 CAN 总线与 ASIL 认证说明行业专用硬件不该挤占通用发行版。Leon Romanovsky 澄清主张：用户态 API 只需“已用或将用”即有公开 PR 或新包申请即可；反对为覆盖所有设备类型定通用方案，建议聚焦企业与云 AI 设备 API 的主流发行版支持。
- **史料**：`ksummit.messages.8089`（Daniel Vetter，2021-09-14）、`ksummit.messages.8200`（Mauro Carvalho Chehab，2021-09-12）、`ksummit.messages.8222`（Leon Romanovsky，2021-09-12）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8089 -->` `<!-- ROW_MINE: ksummit.messages.8200 -->` `<!-- ROW_MINE: ksummit.messages.8222 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：Daniel Vetter、Mauro Carvalho Chehab 与Leon Romanovsky 三方并置）；经验优先（总纲第 9 条——经验优先：以发行版实际接收节奏与 ASIL 认证等既存约束为判据）
- **辨析**：三条分属 2021-09 同一加速器用户态接口线程；“新 API 永难落地”为 Mauro 所描述的循环，属机制推断而非既成事实。
- **文献**：DSLXC-10836、DSLXC-10870、DSLXC-10874（`ksummit.messages.8089`、`ksummit.messages.8200`、`ksummit.messages.8222`，2021-09-14、2021-09-12、2021-09-12），全文见 `raw_source.raw_json`

## 188.5 维护者峰会存废

- **要点**：Rafael Wysocki 提醒维护者峰会因 Documentation/process/conclave.rst 承担正式应急职能，若大幅改形式须同步修订该预案。Rostedt 回应 Linus 对峰会“小圈子”化的伤感：资深者主导属项目成熟常态，举 Miguel Ojeda 靠 Rust 进入核心为例；预计 5 年内 50 岁以上维护者交棒，Andrew Morton 已启动。Ted 说明峰会预讨论机制：ksummit 列表上的声音会实质影响场内议程；接班规划宜在 LSF/MM 等子系统场合谈，如今年 mm 接班与 FUSE 组织讨论即在 LSF/MM/BPF。
- **史料**：`ksummit.messages.8091`（Rafael J. Wysocki (Intel)，2026-08-07）、`ksummit.messages.8165`（Steven Rostedt，2026-08-07）、`ksummit.messages.8179`（Theodore Tso，2026-08-10）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8091 -->` `<!-- ROW_MINE: ksummit.messages.8165 -->` `<!-- ROW_MINE: ksummit.messages.8179 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 conclave.rst 的正式应急职能与 ksummit 列表影响议程这两项实存机制为准）；多方平等（总纲第 8 条——本体论上各方平等：小圈子化的伤感与资深者主导属常态之辩并置）
- **辨析**：三条分属 2026-08-07、2026-08-07 与 2026-08-10；“5 年内 50 岁以上维护者交棒”系 Steven Rostedt 的预测，非统计。
- **文献**：DSLXC-10837、DSLXC-10856、DSLXC-10863（`ksummit.messages.8091`、`ksummit.messages.8165`、`ksummit.messages.8179`，2026-08-07、2026-08-07、2026-08-10），全文见 `raw_source.raw_json`

## 188.6 cleanup.h 规则之争

- **要点**：James Bottomley 主张 __free 变量不初始化置于块首，混排声明规则可放宽但须注释说明必要性；强调规则应统一适用，并支持以显式作用域块界定变量生命周期。Rostedt 以环形缓冲代码为例，询问 __free 变量声明后紧接分配时能否把声明下移到普通声明之后，受 80 列换行影响可读性，请 Linus 定夺。Martin Petersen 实测 __attribute__(__cleanup__) 与 defer 方案：清理逻辑稍复杂即伤可读性，转换大型代码库后多处回退经典 goto 展开，但并非反对两者。
- **史料**：`ksummit.messages.8094`（James Bottomley，2025-11-18）、`ksummit.messages.8120`（Steven Rostedt，2025-11-18）、`ksummit.messages.8172`（Martin K. Petersen，2025-02-19）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8094 -->` `<!-- ROW_MINE: ksummit.messages.8120 -->` `<!-- ROW_MINE: ksummit.messages.8172 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以环形缓冲 80 列换行、清理逻辑稍复杂即伤可读性等实测为准）；多方平等（总纲第 8 条——本体论上各方平等：置于块首与下移声明两种写法并置）
- **辨析**：三条分属 2025-11-18（两封）与 2025-02-19；Martin Petersen 自陈“转换大型代码库后多处回退经典 goto 展开”，属个人实测范围，不代表普遍结论。
- **文献**：DSLXC-10838、DSLXC-10841、DSLXC-10859（`ksummit.messages.8094`、`ksummit.messages.8120`、`ksummit.messages.8172`，2025-11-18、2025-11-18、2025-02-19），全文见 `raw_source.raw_json`

## 188.7 bcachefs 治理反思

- **要点**：Dan Williams 反对为 bcachefs 事件过度制度化：非正式流程最终仍以项目健康为先，主张培养设定边界的成熟与勇气，引 Pat Gelsinger“少求对、多求效”。
- **史料**：`ksummit.messages.8100`（Dan Williams，2025-08-23）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8100 -->`
- **史观**：拒绝进步叙事（总纲第 1/3 条——一切真历史都是古代史／不存在进步，只有权力再分配：反对把 bcachefs 事件读作须立新制的“进步”契机）；和解优于斗争（总纲第 6 条——和解优于斗争：主张培养设定边界的成熟与勇气而非对抗）
- **辨析**：本块系 Dan Williams 的立场，其引 Pat Gelsinger 之语；“非正式流程最终仍以项目健康为先”为价值判断，非制度分析。
- **文献**：DSLXC-10839（`ksummit.messages.8100`，2025-08-23），全文见 `raw_source.raw_json`

## 188.8 设备树绑定独立仓库

- **要点**：Arınç ÜNAL 自述维护 MediaTek DSA 与若干 dt-binding，主张把 dt-bindings 与 DT 源文件移出 Linux 仓库，建 Linux、U-Boot、OpenWrt 共用统一硬件描述仓库，并请求出席峰会。
- **史料**：`ksummit.messages.8115`（Arınç ÜNAL，2024-09-10）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8115 -->`
- **史观**：偶然性优先（总纲第 5 条——没有必然性，只有偶然性：统一硬件描述仓库的构想由维护者跨 Linux／U-Boot／OpenWrt 的实际处境引出）；动手者叙事（总纲第 10 条——动手者创造历史：以自维护 MediaTek DSA 与 dt-binding 的经验立论）
- **辨析**：本块系 Arınç ÜNAL 的提案与出席请求；“请求出席峰会”为程序性申请，本页未见批复。
- **文献**：DSLXC-10840（`ksummit.messages.8115`，2024-09-10），全文见 `raw_source.raw_json`

## 188.9 kernel.org 信任工具

- **要点**：Greg KH 回应 Bottomley 批评：kernel.org 与 OpenSSF 合作的 Web of Trust 新方案将于 2 月会议公开，可评审时即发布；Bottomley 斥其违背“早发布、常发布”开源准则。
- **史料**：`ksummit.messages.8123`（Greg KH，2026-01-23）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8123 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：Greg KH 的新方案说明与 Bottomley 的准则批评并置）；偶然性优先（总纲第 5 条——没有必然性，只有偶然性：发布时点由 2 月会议这一具体场合决定）
- **辨析**：本块系 Greg KH 的回应，并转述 Bottomley 的批评；“违背早发布、常发布准则”系转述他人立场，落书须区分双方原话。
- **文献**：DSLXC-10842（`ksummit.messages.8123`，2026-01-23），全文见 `raw_source.raw_json`

## 188.10 KTODO 工具提案

- **要点**：Dan Carpenter 澄清 KTODO 非代码注释，而是邮件列表中单行摘要式可检索标签，配合 Closes: 标记可写工具筛出未关闭项。
- **史料**：`ksummit.messages.8124`（Dan Carpenter，2023-10-19）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8124 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 KTODO 标签与 Closes: 标记的实际检索链路为分析单位）；经验优先（总纲第 9 条——经验优先：以邮件列表内可检索标签这一既存载体为准）
- **辨析**：本块系 Dan Carpenter 的澄清；“可写工具筛出未关闭项”止于工具设想，本页未见实现。
- **文献**：DSLXC-10843（`ksummit.messages.8124`，2023-10-19），全文见 `raw_source.raw_json`

## 188.11 AI 审查工具

- **要点**：Rostedt 表明立场：AI 审查放 CI 即可，暂不必担心专有锁定，报告同时抄送提交者与维护者双方受益；认同先做维护者侧、勿转嫁贡献者的路线。
- **史料**：`ksummit.messages.8130`（Steven Rostedt，2025-10-10）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8130 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：CI 化与专有锁定两种顾虑并置）；经验优先（总纲第 9 条——经验优先：以报告同时抄送提交者与维护者双方受益这一实际安排为准）
- **辨析**：本块系 Steven Rostedt 的单方立场；“暂不必担心专有锁定”为其判断，与同页 187 类议题的锁定之忧构成张力。
- **文献**：DSLXC-10845（`ksummit.messages.8130`，2025-10-10），全文见 `raw_source.raw_json`

## 188.12 AI 生成内容指南

- **要点**：Dave Hansen 回应 Lorenzo：现有规则暂能抵挡 LLM 滥用但堤坝随时可能溃决；并以 checkpatch 输出可被直接拒收为例，质疑指南会鼓励维护者无理由拒稿之说。Dave Hansen 发布 TAB 集体起草的工具生成内容指南 v3 全文：新增 generated-content.rst 97 行，要求披露工具、提示词与测试方式，已获 Shuah、Kees、Greg、Miguel 等 8 人 Reviewed-by。Andrew Morton 称尚未见 LLM 产出有用内核改动，但 AI 找缺陷已可用；以补丁形式出现的 AI 缺陷报告可删补丁自修，切勿制定任何妨碍接收 AI 缺陷报告的规则。
- **史料**：`ksummit.messages.8131`（Dave Hansen，2026-01-07）、`ksummit.messages.8159`（Dave Hansen，2026-01-06）、`ksummit.messages.8166`（Andrew Morton，2026-01-09）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8131 -->` `<!-- ROW_MINE: ksummit.messages.8159 -->` `<!-- ROW_MINE: ksummit.messages.8166 -->`
- **史观**：拒绝进步叙事（总纲第 1/3 条——一切真历史都是古代史／不存在进步，只有权力再分配：指南起草不写作流程“进步”）；经验优先（总纲第 9 条——经验优先：以 checkpatch 输出可被直接拒收、AI 找缺陷已可用等实测为判据）
- **辨析**：三条分属 Dave Hansen（两封）与 Andrew Morton；“堤坝随时可能溃决”为比喻性判断，8 位 Reviewed-by 名单以补丁原文为准。
- **文献**：DSLXC-10846、DSLXC-10854、DSLXC-10857（`ksummit.messages.8131`、`ksummit.messages.8159`、`ksummit.messages.8166`，2026-01-07、2026-01-06、2026-01-09），全文见 `raw_source.raw_json`

## 188.13 补丁审阅工具

- **要点**：Mauro 分享用 wdiff 审阅重命名补丁的经验，给出 diff-highlight 作 git pager 的配置；称 Fedora 33 需自改 perl 脚本，git 2.29 可用，因 RH bug 1952030 从 2.30 回退。
- **史料**：`ksummit.messages.8134`（Mauro Carvalho Chehab，2021-04-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8134 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 Fedora 33 需自改 perl 脚本、git 2.29 可用、因 RH bug 1952030 从 2.30 回退等可复核事实为准）
- **辨析**：本块系 Mauro Carvalho Chehab 的工具经验分享；所述发行版与版本约束为当事人环境实况，非普遍适用结论。
- **文献**：DSLXC-10847（`ksummit.messages.8134`，2021-04-22），全文见 `raw_source.raw_json`

## 188.14 DCO 与 AI 披露

- **要点**：Ted 拟咨询法律顾问四问：DCO 是否须披露 LLM 生成、需何种细节、全盘生成与局部修改是否区别对待、提示词是否如 coccinelle 脚本般记入提交说明。
- **史料**：`ksummit.messages.8135`（Theodore Tso，2026-07-18）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8135 -->`
- **史观**：法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：DCO 披露义务被还原为法律责任的边界问题）；自反性声明（总纲第 7/23 条——理论必须自反／一切历史写作都是基于哲学设定的历史小说：明示四问须咨询法律顾问后方可作答）
- **辨析**：本块系 Theodore Ts'o 拟提的四问，属待答问题清单；落书不得据以断言 DCO 已含披露义务。
- **文献**：DSLXC-10848（`ksummit.messages.8135`，2026-07-18），全文见 `raw_source.raw_json`

## 188.15 琐碎补丁收件政策

- **要点**：Martin Petersen 实证 SCSI 已在合并大量琐碎补丁：静态检查器与编译器日益严苛，拒不应用则同型修复每周重发；有人维护与无人维护的驱动已无差别，需更好流程与辅导。
- **史料**：`ksummit.messages.8145`（Martin K. Petersen，2021-04-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8145 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以静态检查器与编译器日益严苛、拒不应用则同型修复每周重发这一实测为判据）；多方平等（总纲第 8 条——本体论上各方平等：有人维护与无人维护的驱动被并置比较）
- **辨析**：本块系 Martin K. Petersen 的实证陈述；“已无差别”为其观察，本页未附计数。
- **文献**：DSLXC-10849（`ksummit.messages.8145`，2021-04-22），全文见 `raw_source.raw_json`

## 188.16 devres 混用检测

- **要点**：Dan Carpenter 就 devres 与 uapi 资源混用给出三种检测思路：直接检查、按类型推断并建 kernel.ignore_devres_types 例外表、Sparse 手工注解，建议并行实现。
- **史料**：`ksummit.messages.8147`（Dan Carpenter，2021-07-21）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8147 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以三种检测思路与 kernel.ignore_devres_types 例外表的实现路径为分析单位）；经验优先（总纲第 9 条——经验优先：以按类型推断这一可自动化路径为准）
- **辨析**：本块系 Dan Carpenter 的技术方案；“建议并行实现”止于建议，本页未见实现进度。
- **文献**：DSLXC-10850（`ksummit.messages.8147`，2021-07-21），全文见 `raw_source.raw_json`

## 188.17 AI 照片权限方案

- **要点**：Jan Kara 认为该 AI 照片分类共享场景无需 richACL：用 AI 属主、带粘滞位的 rwxrwxrwt 目录即可实现可删己不可删人，创建限制用任意 LSM 即可施加。
- **史料**：`ksummit.messages.8154`（Jan Kara，2025-09-17）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8154 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以带粘滞位 rwxrwxrwt 目录与任意 LSM 的既存能力为判据）；多方平等（总纲第 8 条——本体论上各方平等：richACL 方案与粘滞位方案并置）
- **辨析**：本块系 Jan Kara 的替代方案；“无需 richACL”为其判断，属技术取舍而非结论性裁定。
- **文献**：DSLXC-10851（`ksummit.messages.8154`，2025-09-17），全文见 `raw_source.raw_json`

## 188.18 Rust 内核政策

- **要点**：Hellwig 强烈反对 Rust 政策网页：内容失实，并披露 Linus 私下称将无视子系统维护者反对强并 Rust；警告绑定代码将如癌症蔓延，多语言无序化会迫使他抽身。
- **史料**：`ksummit.messages.8158`（Christoph Hellwig，2025-02-18）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8158 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：Rust 推进方与 Hellwig 的反方立场并置呈现）；自反性声明（总纲第 7/23 条——理论必须自反／一切历史写作都是基于哲学设定的历史小说：明示“Linus 私下称”系转述，其证据等级低于公开邮件）
- **辨析**：本块系 Christoph Hellwig 的反方一手陈述；“Linus 私下称将无视维护者反对”为未经公开确认的转述，“如癌症蔓延”为比喻，落书须标明转述性质。
- **文献**：DSLXC-10853（`ksummit.messages.8158`，2025-02-18），全文见 `raw_source.raw_json`

## 188.19 Rust 测试环境

- **要点**：Jarkko Sakkinen 展示 NixOS 构建的 TPM 驱动测试环境：docker compose 构建镜像后 QEMU 启动，计划登记进 MAINTAINERS，与 Fiona 的 nix shell 路线不同。
- **史料**：`ksummit.messages.8160`（Jarkko Sakkinen，2025-03-04）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8160 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 docker compose 构建镜像加 QEMU 启动的实际测试环境为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：NixOS 构建与 Fiona 的 nix shell 两条路线并置）
- **辨析**：本块系 Jarkko Sakkinen 的自述；“计划登记进 MAINTAINERS”为待办，本页未见登记结果。
- **文献**：DSLXC-10855（`ksummit.messages.8160`，2025-03-04），全文见 `raw_source.raw_json`

## 188.20 设备透传争论

- **要点**：Jason Gunthorpe 反问：全开源的相机透传方案是否仅因透传形态就拒收？主张“因恐惧拒绝给用户有用的开源方案”不是 Linux 该做的事。
- **史料**：`ksummit.messages.8169`（Jason Gunthorpe，2024-07-25）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8169 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：透传形态与方案开源性被分列考量）；偶然性优先（总纲第 5 条——没有必然性，只有偶然性：拒收与否由相机透传这一具体形态触发）
- **辨析**：本块系 Jason Gunthorpe 的反问；“不是 Linux 该做的事”为价值判断，非政策文本。
- **文献**：DSLXC-10858（`ksummit.messages.8169`，2024-07-25），全文见 `raw_source.raw_json`

## 188.21 ORC 栈回溯

- **要点**：Josh Poimboeuf 力挺 ORC：多年稳健、中断异常栈迹干净，唯一失效原因是无视 objtool 告警（即将默认升为编译错误）；x86-64 帧指针已实质弃用，考虑移除该 unwinder。
- **史料**：`ksummit.messages.8173`（Josh Poimboeuf，2025-02-26）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8173 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以多年稳健、中断异常栈迹干净、唯一失效原因是无视 objtool 告警等实测为准）；知识注定过时（总纲第 22 条——知识注定过时：x86-64 帧指针已实质弃用，考虑移除该 unwinder）
- **辨析**：本块系 Josh Poimboeuf 的技术辩护；“即将默认升为编译错误”为进行中的变更，落书须以 objtool 实况核对。
- **文献**：DSLXC-10860（`ksummit.messages.8173`，2025-02-26），全文见 `raw_source.raw_json`

## 188.22 C 聚合传参之争

- **要点**：comex 考据 std::string CoW 史：C++11 未明文禁 CoW，但要求 operator[] 为 O(1) 实质封杀，迫使 libstdc++ 破坏 ABI 放弃引用计数实现。Ralf Jung 澄清 C++ 内存模型已按程序行为而非类型系统定义，原子对象只是类型系统薄层，Rust 即绕开它；并论证把数据竞争从 UB 改为确定可见值会损害顺序代码优化。Linus 实测纠正 David Laight：x86 与 arm64 ABI 下两寄存器大小的结构体同样经寄存器返回（gcc 与 clang 均生成两条 movl 加 ret），超过两寄存器才走间接内存。
- **史料**：`ksummit.messages.8176`（comex，2025-02-22）、`ksummit.messages.8185`（Ralf Jung，2025-02-28）、`ksummit.messages.8233`（Linus Torvalds，2025-02-21）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8176 -->` `<!-- ROW_MINE: ksummit.messages.8185 -->` `<!-- ROW_MINE: ksummit.messages.8233 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 x86 与 arm64 ABI 下两寄存器结构体返回的实测汇编（两条 movl 加 ret）为准）；多方平等（总纲第 8 条——本体论上各方平等：std::string CoW 史、内存模型之辩与 ABI 实测并置）
- **辨析**：三条分属 comex、Ralf Jung 与 Linus Torvalds；Linus 的实测为纠正 David Laight 之说，落书须以两造原话对照。
- **文献**：DSLXC-10861、DSLXC-10865、DSLXC-10875（`ksummit.messages.8176`、`ksummit.messages.8185`、`ksummit.messages.8233`，2025-02-22、2025-02-28、2025-02-21），全文见 `raw_source.raw_json`

## 188.23 io_uring BPF 议题

- **要点**：Pavel Begunkov 提交峰会议题：io_uring 拟把部分提交与控制权交给 BPF，进一步减少上下文切换与系统调用，作为提交队列轮询的替代，征集用例与 API 意见。
- **史料**：`ksummit.messages.8178`（Pavel Begunkov，2021-06-25）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8178 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以提交队列轮询的替代方案为分析单位）；偶然性优先（总纲第 5 条——没有必然性，只有偶然性：议题由减少上下文切换这一具体动机引出）
- **辨析**：本块系 Pavel Begunkov 的议题提案；“征集用例与 API 意见”表明方案尚未定型。
- **文献**：DSLXC-10862（`ksummit.messages.8178`，2021-06-25），全文见 `raw_source.raw_json`

## 188.24 HIGHMEM 淘汰

- **要点**：Richard Weinberger 报告受影响机型 MPC8343 与 QorIQ P1022：应用常假设内存布局，FPGA 树外驱动共享内核与用户态内存；Christophe 已发 powerpc 全量移除 HIGHMEM 补丁。
- **史料**：`ksummit.messages.8180`（Richard Weinberger，2025-09-10）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8180 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 MPC8343 与 QorIQ P1022 上应用常假设内存布局、FPGA 树外驱动共享内存等实况为判据）；动手者叙事（总纲第 10 条——动手者创造历史：以 powerpc 全量移除补丁为落点）
- **辨析**：本块系 Richard Weinberger 的受影响机型报告；“Christophe 已发全量移除补丁”为进展转述，本页未见合入结论。
- **文献**：DSLXC-10864（`ksummit.messages.8180`，2025-09-10），全文见 `raw_source.raw_json`

## 188.25 LLM 测试生成

- **要点**：Mark Brown 认同 LLM 生成测试数据比测试代码安全，因后者约束更少；场景生成是否可行因运行成本而异，预示 AI 政策将更多靠“品味”而非硬规则。
- **史料**：`ksummit.messages.8189`（Mark Brown，2025-08-05）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8189 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以测试数据比测试代码约束更少这一实际差异为判据）；拒绝进步叙事（总纲第 1/3 条——一切真历史都是古代史／不存在进步，只有权力再分配：AI 政策被预期为靠“品味”而非硬规则）
- **辨析**：本块系 Mark Brown 的判断；“预示 AI 政策将更多靠品味”为预测性表述，非成文规则。
- **文献**：DSLXC-10866（`ksummit.messages.8189`，2025-08-05），全文见 `raw_source.raw_json`

## 188.26 stable 补丁标记

- **要点**：Jiri Kosina 质询 stable 标记边界：既然 stable 只为修错，哪些非修错补丁应获 Cc: stable？点名硬件安全缓解、新设备 ID、quirk 一类，指 stable-kernel-rules 的定义早已不适用。
- **史料**：`ksummit.messages.8192`（Jiri Kosina，2024-07-23）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8192 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以硬件安全缓解、新设备 ID、quirk 三类实际补丁为质询对象）；知识注定过时（总纲第 22 条——知识注定过时：stable-kernel-rules 的定义早已不适用）
- **辨析**：本块系 Jiri Kosina 的质询；“定义早已不适用”为其判断，落书须与 stable-kernel-rules 现行文本对照。
- **文献**：DSLXC-10867（`ksummit.messages.8192`，2024-07-23），全文见 `raw_source.raw_json`

## 188.27 内核文档改革

- **要点**：Vegard Nossum 系统提案：维护者条目档案加子系统评审清单并可由 kerneldoc 自动收集、HTML 侧栏按“书”重组、设“社区”卷、翻译加语言切换栏、跨架构文档按读者分流。
- **史料**：`ksummit.messages.8196`（Vegard Nossum，2023-11-11）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8196 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 kerneldoc 自动收集与 HTML 侧栏重组等可实施路径为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：维护者、读者与译者三类受众被并列考量）
- **辨析**：本块系 Vegard Nossum 的系统提案；各项均止于提案，本页未见采纳结论。
- **文献**：DSLXC-10868（`ksummit.messages.8196`，2023-11-11），全文见 `raw_source.raw_json`

## 188.28 LKML 通配剥离

- **要点**：Konstantin 澄清“THE REST”剥离方案是“预审”而非限权：订阅仍开放，只需说明收全部补丁的理由，高知名度维护者可订阅，并举 outlook.com 断服例证 Gmail 并非唯一故障源。
- **史料**：`ksummit.messages.8205`（Konstantin Ryabitsev，2023-11-06）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8205 -->`
- **史观**：自反性声明（总纲第 7/23 条——理论必须自反／一切历史写作都是基于哲学设定的历史小说：以“预审而非限权”自我界定，回应外界对其权限制约的解读）；经验优先（总纲第 9 条——经验优先：以 outlook.com 断服这一实例反驳 Gmail 唯一故障源之说）
- **辨析**：本块系 Konstantin Ryabitsev 的澄清；“订阅仍开放”为方案口径，落书须以列表实际策略核对。
- **文献**：DSLXC-10871（`ksummit.messages.8205`，2023-11-06），全文见 `raw_source.raw_json`

## 188.29 Sphinx 构建工具

- **要点**：Mauro 解释 sphinx 检测脚本缘由：发行版 LaTeX 元包残缺致装而不能用，故脚本内置 *.sty 清单并用 kpsewhich 复核依赖；回应 openSUSE Leap 15.4 缺 tex-gyre 的问题。
- **史料**：`ksummit.messages.8209`（Mauro Carvalho Chehab，2022-07-07）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8209 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以发行版 LaTeX 元包残缺致装而不能用、kpsewhich 复核依赖等实测为准）
- **辨析**：本块系 Mauro Carvalho Chehab 的脚本缘由说明；所举 openSUSE Leap 15.4 缺 tex-gyre 为具体发行版问题，非普遍结论。
- **文献**：DSLXC-10872（`ksummit.messages.8209`，2022-07-07），全文见 `raw_source.raw_json`

## 188.30 TAB 选举

- **要点**：Shuah Khan 要求公开 TAB 选举判定 3 至 49 提交档的脚本，并追问其是否也用于候选人资格核验；引选举规则：2020-21 年三项标签提交、CIVS 投票、超 50 提交自动获票。
- **史料**：`ksummit.messages.8219`（Shuah Khan，2021-09-15）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8219 -->`
- **史观**：自反性声明（总纲第 7/23 条——理论必须自反／一切历史写作都是基于哲学设定的历史小说：要求公开判定脚本，即要求选举程序自证）；经验优先（总纲第 9 条——经验优先：以三项标签提交、CIVS 投票、超 50 提交自动获票等规则文本为准）
- **辨析**：本块系 Shuah Khan 的程序性要求；脚本是否公开、是否用于资格核验，本页未见答复。
- **文献**：DSLXC-10873（`ksummit.messages.8219`，2021-09-15），全文见 `raw_source.raw_json`
