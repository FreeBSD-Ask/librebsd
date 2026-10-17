# 173 【Linux社区】AI版权与API弃用定调

> 来源：ksummit 独有 p37（50 封全读，2023-08 至 2025-02：Bottomley 引美国版权局报告与国会 CRS 摘要论证纯 AI 代码不可获版权实为公有领域故 DCO 可提交；Linus 对 API 弃用一锤定音零警告不可动摇改 API 者必须修完所有现有用户；Sasha Levin 给出 6.7.2/6.9.3 回移窗口精确数据 640/427 处变更不足 4 天测试期；Ribalda 提出五条跨子系统设备直通政策标准域驱动须在内核与完整开源栈；UMN 事件争论二封、Bugzilla 困境二封、Sashiko 审查与 AI 代码版权）
> 判定：42 CAND / 8 NV。主题分布：维护者列表校验 1、next分支稳定性 1、字符串API之争 1、Werror编译争议 1、文档构建工具链 1、AI标注争议 2、LSM权限模型 1、Rust验证工具 1、AI代码版权 2、UMN事件争论 2、Baikal补丁拒收 1、展开器与栈回溯 1、邮件引用限额 1、混合会议参与 1、Sashiko审查 2、Bugzilla困境 2、稳定版回移 2、linus-next测试 1、工具生成内容 2、fwctl与RAS 1、设备直通规则 2、AI回移与测试 1、驱动对象生命周期 2、回归定位工具 1、Link标注规范 1、代码评审激励 1、Rust稳定回移 1、TAB纪要缺失 1、加速器用户态 1、bcachefs治理 1、维护者减压 1、原子内存模型 1、API弃用规则 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p37 的逐封提取（2023-08 至 2025-02，42 CAND / 8 NV），全 33 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 173.1 维护者列表校验

- 【Linux社区】Mark Brown 称发件端无法根治收件人选择问题但可改善，lei 在 Debian stable 尚不可用，支持提高 get_maintainer 的 --git-min-signatures 并质疑其对新增文件是否有效。 `<!-- ROW_MINE: ksummit.messages.5740 -->`

## 173.2 next分支稳定性

- 【Linux社区】Lee Jones 声明其 next 分支从不稳定且经常 rebase 删改提交，Rostedt 称仅偶尔移除完全损坏的提交，并援引 LWN 报道与维护者峰会既往讨论。 `<!-- ROW_MINE: ksummit.messages.5743 -->`

## 173.3 字符串API之争

- 【Linux社区】Hellwig 批评 strncpy 换 strscpy 式逐个替换可能引入比修复更多的 bug，主张改用 seq_buf 等计数式字符串，并指 Kent Overstreet 重复实现而非贡献上游。 `<!-- ROW_MINE: ksummit.messages.5745 -->`

## 173.4 Werror编译争议

- 【Linux社区】Carpenter 称内核 2930 个 Makefile 部分硬编码 -Werror 致旧内核难用新 GCC 编译；Segher 坚持修内核约三十个补丁而非改编译器，Biener 建议用脚本附加 -Wno-error。 `<!-- ROW_MINE: ksummit.messages.5746 -->`

## 173.5 文档构建工具链

- 【Linux社区】Mauro 建议内核文档构建在 python 过旧时自动选用系统已装的较新版本，列举 Fedora 与 openSUSE 多版本现状；Corbet 反对绕过用户 PATH，Mauro 接受加 --fastest-python 开关。 `<!-- ROW_MINE: ksummit.messages.5748 -->`

## 173.6 AI标注争议

- 【Linux社区】Dan Carpenter 称 Signed-off-by 规则易执行但无法识别 AI 所写补丁，现有 AI 标签仅覆盖极少数补丁，反驳“能标注大部分受影响代码”的设想。 `<!-- ROW_MINE: ksummit.messages.5753 -->`
- 【Linux社区】Mauro 称 AI 之前就常收到不同开发者几乎雷同的补丁，源于共同教科书算法，AI 产出亦将约九成相似故无差别；McKenney 表明争议解决前自用项目避开 AI 产物。 `<!-- ROW_MINE: ksummit.messages.5797 -->`

## 173.7 LSM权限模型

- 【Linux社区】Paul Moore 阐明 LSM 只能拒绝、不能授予 DAC 之外权限，拒绝更改以免安全回归；解释 do_unlinkat 安全检查先于 may_delete 的顺序，并举 Landlock 供非特权用户自设策略。 `<!-- ROW_MINE: ksummit.messages.5767 -->`

## 173.8 Rust验证工具

- 【Linux社区】Ralf Jung 列举支持 unsafe 代码的 Rust 验证工具 Kani、VeriFast、Verus、Prusti、RefinedRust 等均非生产就绪，Miri 的抽象机模型是关键，RefinedRust 源自其 Coq 博士工作 RustBelt。 `<!-- ROW_MINE: ksummit.messages.5771 -->`

## 173.9 AI代码版权

- 【Linux社区】Rafael 反驳 Bottomley“纯 AI 代码无版权即公有领域”论：若不可获版权便无法按内核要求的 GPLv2 提交，点出 AI 代码授权悖论。 `<!-- ROW_MINE: ksummit.messages.5772 -->`
- 【Linux社区】Bottomley 引美国版权局三卷报告与国会 CRS 摘要：纯 AI 生成代码不可获版权、实质公有领域，提交 DCO 无碍且未来立法不可溯及；人工改动部分仍有版权。 `<!-- ROW_MINE: ksummit.messages.5836 -->`

## 173.10 UMN事件争论

- 【Linux社区】Dreier 主张严惩 UMN 研究组并质问 IEEE 为何接受该论文，称应遵循人类受试者研究伦理；同时转述 UMN 自称经 IRB 批准、无恶意补丁入库，批评 Greg 反应过度。 `<!-- ROW_MINE: ksummit.messages.5778 -->`
- 【Linux社区】Rapoport 赞同该研究只证明开放项目可被注入恶意代码的常识，强调测试与 CI 才是防线；引用 Geert 指出 190 个待回退 UMN 补丁多为真实修复，质疑盲目回退。 `<!-- ROW_MINE: ksummit.messages.5792 -->`

## 173.11 Baikal补丁拒收

- 【Linux社区】Linus 就 Baikal 电子补丁被拒表态：技术理由仅是最低要求，维护者须信任补丁来源及其后续支持承诺，此类非技术拒收历来正当且非灰色地带。 `<!-- ROW_MINE: ksummit.messages.5783 -->`

## 173.12 展开器与栈回溯

- 【Linux社区】Rostedt 澄清内核所谓 unwinding 实为编译界的 stack walking，ORC 作者 Josh 与 GCC 方曾因此误会争论；驳斥 Kent 对 ORC 可靠性质疑，强调其为活内核补丁设计。 `<!-- ROW_MINE: ksummit.messages.5790 -->`

## 173.13 邮件引用限额

- 【Linux社区】转存 Linus 提案：列表对引用超 50 行的回信直接弹回，允许 Reviewed-by 引 15 行提交说明，须“新内容至少与引用相当”；Rostedt 戏言将波及 Paul。 `<!-- ROW_MINE: ksummit.messages.5793 -->`

## 173.14 混合会议参与

- 【Linux社区】Toke 介绍 IETF 混合会议机制：志愿 jabber scribe 将聊天区问题转述到现场话筒，远程虚拟发言队列由 session chairs 管理，回应 Rostedt“远程者注定二等公民”论。 `<!-- ROW_MINE: ksummit.messages.5794 -->`

## 173.15 Sashiko审查

- 【Linux社区】Roeck 建议 Sashiko 增加每子系统提示与“是否报告存量问题”开关，称其范围内存量问题几乎全真，常借此请补丁作者顺手修复 20 余年老驱动的真实缺陷；认同 yak shaving 不应强制。 `<!-- ROW_MINE: ksummit.messages.5798 -->`
- 【Linux社区】Bottomley 发现 Sashiko 每子系统提示词仓库分叉：masoncl/review-prompts 疑被整体拷入而非模块引用，贡献者恐须双仓重复提交。 `<!-- ROW_MINE: ksummit.messages.5811 -->`

## 173.16 Bugzilla困境

- 【Linux社区】Greg 澄清 LF 仅托管 bugzilla 而不涉内容处理，维护者鲜有雇主许可持续处理上游 bug 报告；LF 资助的开发者相对每年 4000+ 贡献者只是零头。 `<!-- ROW_MINE: ksummit.messages.5800 -->`
- 【Linux社区】20 余年资历用户 Artem 以 bugzilla 216274 与 dmesg 含混报错为例，说明普通用户无从判断责任人与严重性、grep 命中多模块、发 LKML 无人回应的一手受挫叙述。 `<!-- ROW_MINE: ksummit.messages.5839 -->`

## 173.17 稳定版回移

- 【Linux社区】Levin 给出实测：6.7.2 含 640 处变更、距合入 6.8-rc1 仅 4 天，其中 94 个带 stable 标签、630 个带 Fixes；6.9.3 同样不足四天，结论是短周期与大回移量不可兼得。 `<!-- ROW_MINE: ksummit.messages.5802 -->`
- 【Linux社区】Greg 说明合并窗口是 stable 团队最忙时段，带 Fixes 或 cc:stable 的补丁集中涌入但占比不大；树中无 fixes 标签的自动回移应只来自 autosel 的 stable-dep-of 或明确请求。 `<!-- ROW_MINE: ksummit.messages.5822 -->`

## 173.18 linus-next测试

- 【Linux社区】Levin 展示 next-analysis 机器人与 6.12-rc4..rc5 提交在 -next 停留时长直方图，110 个提交未经 -next 即被拉走，linus-next 拟在 Linus 拉取前补做构建与冒烟测试。 `<!-- ROW_MINE: ksummit.messages.5805 -->`

## 173.19 工具生成内容

- 【Linux社区】Rostedt 说明该文档源自 TAB、覆盖从 sed 脚本到 AI 的工具生成补丁透明披露，反对将其改造成 AI slop 专文，主张另立更严厉文档；Lorenzo 表态认同文明分歧并接受其增补。 `<!-- ROW_MINE: ksummit.messages.5806 -->`
- 【Linux社区】Ted 反对强制 AI 标注，预言 slop 洪流将挤压新贡献者并催生“老男孩俱乐部”指责；主张以声誉惩戒乃至整域封禁威慑，援引明尼苏达大学先例，类比法院惩处引用幻觉判例的律师。 `<!-- ROW_MINE: ksummit.messages.5871 -->`

## 173.20 fwctl与RAS

- 【Linux社区】Gunthorpe 向 Petkov 给出 fwctl 系列链接并划界：内存持续清洗与 EDAC 属设备主业不应经 fwctl，ECC 错误率评估采集适合；Jonathan Cameron 担忧清洗器固件 RPC 暴露。 `<!-- ROW_MINE: ksummit.messages.5807 -->`

## 173.21 设备直通规则

- 【Linux社区】Ribalda 提出跨子系统直通政策：有标准领域驱动须在内核并走通用 syscall，无标准可部分用户态；合入须有完整开源栈，既有栈如 mesa、libcamera 必须基于之，厂商直通仅限小众与开发用途。 `<!-- ROW_MINE: ksummit.messages.5812 -->`
- 【Linux社区】Leon 主张信任双向，单个维护者以不信任为由阻止他人不健康，大型子系统无法通晓全部用例；并定性与 Laurent 的分歧为哲学而非技术，故需维护者峰会裁决。 `<!-- ROW_MINE: ksummit.messages.5831 -->`

## 173.22 AI回移与测试

- 【Linux社区】Brown 质疑用 LLM 做补丁回移，称回移需大量隐性上下文易触雷；Bottomley 称 git 历史补丁路径有限可训练、覆盖率可量化；Brown 指自测框架各自为政，推广是社会问题。 `<!-- ROW_MINE: ksummit.messages.5813 -->`

## 173.23 驱动对象生命周期

- 【Linux社区】Laurent 指出驱动常以 devm_kzalloc 分配可经用户态触达的私有数据而忽视生命周期；Carpenter 承认社区普遍未理解该问题，建议以静态分析检测并请向 kernel-janitors 提炼启发式。 `<!-- ROW_MINE: ksummit.messages.5814 -->`
- 【Linux社区】转存 Bartosz 峰会提案摘要：接续 Laurent 在 LPC 2022 对 devres 副作用的批评与 Wolfram 在 EOSS 2023 的研究，拟分多年多阶段统一子系统驱动数据与对象所有权处理；Greg 与 Laurent 均表支持。 `<!-- ROW_MINE: ksummit.messages.5876 -->`

## 173.24 回归定位工具

- 【Linux社区】Geert 建议在 scripts/ 提供 git bisect 封装：自动保存 .config 为 bisect_defconfig、逐步重配并显示配置影响；Leemhuis 补充先跑 localmodconfig 提速并讨论稳定版区间二分的坑。 `<!-- ROW_MINE: ksummit.messages.5815 -->`

## 173.25 Link标注规范

- 【Linux社区】Carpenter 建议在 checkpatch 中对 patch.msgid.link 链接发出警告，因该域名链接应由 committer 而非补丁作者添加。 `<!-- ROW_MINE: ksummit.messages.5816 -->`

## 173.26 代码评审激励

- 【Linux社区】Airlie 主张形成“想被评审须先评审他人”的社区市场机制，指出提交计数是错误绩效指标；驳斥“没有硬件”借口，称评审只需内核接口素养，异常提交须资深维护者把关。 `<!-- ROW_MINE: ksummit.messages.5819 -->`

## 173.27 Rust稳定回移

- 【Linux社区】Ojeda 说明仅当所用不稳定特性变动才需联动回移 rustc，rust/kernel 与 rust/alloc 静态限制特性集且模块不得自行引入；寻求企业资助 rustc，Rust 支持标为实验性故可不承诺回移。 `<!-- ROW_MINE: ksummit.messages.5820 -->`

## 173.28 TAB纪要缺失

- 【Linux社区】Geert 在 TAB 提名征集中指出会议纪要自 2020 年 10 月后未见更新，公开追问是缺失还是未开会，暴露 TAB 透明度问题。 `<!-- ROW_MINE: ksummit.messages.5821 -->`

## 173.29 加速器用户态

- 【Linux社区】转存 Airlie 立场：加速器 uAPI 复杂非自测可覆盖、社区靠拒绝与教育构建、厂商仅因上游客户压力最低限度参与；其已起草通用开源用户态要求文档并拟结盟推进，Laurent 请纳入相机 ISP。 `<!-- ROW_MINE: ksummit.messages.5842 -->`

## 173.30 bcachefs治理

- 【Linux社区】Bottomley 重申两点诉求：纳入与移除决定应由多人而非“最后坚持者”定夺、结果须明确记录；Ted 以人事问题类比反对纳入期设限，James 称已放弃禁入主张但应对可预见问题预作计划。 `<!-- ROW_MINE: ksummit.messages.5855 -->`

## 173.31 维护者减压

- 【Linux社区】Bottomley 提议通用版维护者压力疏导会议，聚焦压力应对而非指责施压者，可设非评判倾听环节收集主要压力源，回应 CoC 委员 Shuah 对“CoC 只管维护者”说法的异议。 `<!-- ROW_MINE: ksummit.messages.5858 -->`

## 173.32 原子内存模型

- 【Linux社区】Feng 澄清 relaxed 原子写不含编译器屏障、WRITE_ONCE 即 relaxed；发布后混入普通写即成数据竞争结果任意；LKMM 竞争须含写访问，Rust 原生模型经 Ralf 的 PR 128778 修复。 `<!-- ROW_MINE: ksummit.messages.5861 -->`

## 173.33 API弃用规则

- 【Linux社区】Linus 断然否决以 __attribute__((deprecated)) 引入警告，内核必须保持零警告；唯一有效规则是改 API 者须修完所有现有用户，否则新旧两套 API 永久由其维护。 `<!-- ROW_MINE: ksummit.messages.5868 -->`
