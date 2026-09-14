# 177 【Linux社区】AI流程落地与Rust稳定性反驳

> 来源：ksummit 独有 p41（50 封全读，2022-09 至 2023-10：Arnaldo Melo 详述用 Claude 把 AI 报告存量问题归档进 perf TODO 文件 TODO.hardening 达 106KB 并推荐 kres 多代理审计工具与 confirmed/invalid 分级流程；Ventura Jack 对 Ralf Jung 长篇技术反驳含 Rust 1.80 破坏 time crate 波及 5000+ crates 与 trait solver 重写难题；Bottomley 依据版权局报告论证纯 AI 代码属公有领域 DCO 可接受加 Mauro 实测 AI 生成单元测试五至六成首跑失败；Bottomley 与 Greg KH 就 Rust 维护者辞职事件开发者退出仅剩 Linus 独扛正面交锋；AI 内核流程七封、内核文档建设四封、Rust 聚合传递四封、Bugzilla 退役五封）
> 判定：44 CAND / 6 NV。主题分布：API弃用治理 1、峰会疫苗之争 1、AI内核流程 7、补丁基线流程 1、文件系统维护 1、设备树绑定ABI 1、Rust进内核 3、回归治理 2、linus-next测试 2、维护者倦怠 2、stable补丁流程 1、峰会赞助机制 1、Bugzilla退役 5、Rust聚合传递 4、内核文档建设 4、TAB选举 1、DRM面板驱动 1、Link标签之争 1、生成代码入库 2、治理透明度 1、内存分配API 1、uAPI准入标准 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p41 的逐封提取（2022-09 至 2023-10，44 CAND / 6 NV），全 22 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 177.1 API弃用治理

- 【Linux社区】Laurent Pinchart 主张在 checkpatch 加弃用 API 警告，低成本提醒不知情开发者，回应 Johannes Berg“再叨扰也无用”论。 `<!-- ROW_MINE: ksummit.messages.6346 -->`

## 177.2 峰会疫苗之争

- 【Linux社区】2021 线下峰会筹备中 Enrico Weigelt 自述全家拒绝接种，称疫苗为“人体实验”并以 #faucigate 质疑疫情数据。 `<!-- ROW_MINE: ksummit.messages.6350 -->`

## 177.3 AI内核流程

- 【Linux社区】Jori Koolstra 澄清经 Paul McKenney 提醒才知峰会讨论列表公开，原以为仅委员会可见，提议公告应明示列表公开性。 `<!-- ROW_MINE: ksummit.messages.6351 -->`
- 【Linux社区】Arnaldo Melo 用 Claude 把 AI 报的存量问题归档进 perf TODO 文件（TODO.hardening 达 106KB），并推荐 Mason 的 kres 审计工具及其 confirmed、invalid、unconfirmed 分级流程。 `<!-- ROW_MINE: ksummit.messages.6375 -->`
- 【Linux社区】Steven Rostedt 称不在意变更日志由人还是 AI 写，只求说清动机；自述多年替非母语者重写日志，且不再示范写法因对方会原样照抄。 `<!-- ROW_MINE: ksummit.messages.6416 -->`
- 【Linux社区】Bottomley 引美国版权局报告称纯 AI 代码无版权即公有领域、DCO 可接受；Mauro 实测 AI 生成单元测试五至六成首跑失败，称 AI 如高级实习生需人重塑。 `<!-- ROW_MINE: ksummit.messages.6445 -->`
- 【Linux社区】Andrew Lunn 澄清 netdev 流程：补丁入 patchwork 后 CI 跑测，结果以红黄绿与链接呈现，失败不自动改状态而由人工裁定，纠正 Rostedt 的自动化误解。 `<!-- ROW_MINE: ksummit.messages.6452 -->`
- 【Linux社区】Jori Koolstra 披露内核导师计划无论对错一律拒收 AI 贡献，因导师投入旨在培养未来贡献者，须信任参与者不借 AI 刷名字；并引 Linus 的贡献信任模型。 `<!-- ROW_MINE: ksummit.messages.6490 -->`
- 【Linux社区】Dan Carpenter 称 AI 生成的锁文档自信却模糊且常有错，生成快评审慢；Julia Lawall 期望专为此设计的注释理解工具而非零散 AI 生成。 `<!-- ROW_MINE: ksummit.messages.6496 -->`

## 177.4 补丁基线流程

- 【Linux社区】James Bottomley 称维护者惯用 git/b4 am 忽略 base commit，反对用 prerequisite-patch-id，要求封面信直接给出前置系列的 lore 链接。 `<!-- ROW_MINE: ksummit.messages.6352 -->`

## 177.5 文件系统维护

- 【Linux社区】JFS 维护者 Dave Kleikamp 回应弃用讨论：称有用户希望保留 JFS，将把跟进频率从数周一次提高到每周。 `<!-- ROW_MINE: ksummit.messages.6354 -->`

## 177.6 设备树绑定ABI

- 【Linux社区】Arınç ÜNAL 主张 DT 绑定修正不应被要求先改 Linux 驱动，做设备树无需会 C，绑定兼作硬件文档；与 Woodhouse 辩 ABI 变更迁移。 `<!-- ROW_MINE: ksummit.messages.6359 -->`

## 177.7 Rust进内核

- 【Linux社区】Linus Walleij 主张 Rust 应优先用于协议栈与用户态边界等易被攻击代码如 ksmbd、nfsd，而非仅驱动，并称 ksmbd 曾被情报机构利用。 `<!-- ROW_MINE: ksummit.messages.6367 -->`
- 【Linux社区】Arnd Bergmann 担心 Rust 绑定的 CamelCase 命名使 C 与 Rust 同名结构难以 grep 与文档化。 `<!-- ROW_MINE: ksummit.messages.6391 -->`
- 【Linux社区】Roland Dreier 称 devres 采用有限；Linus Walleij 反驳 devm_ 已有 26112 处使用，输入子系统甚至强制 remove 路径用 devm 动作，视之为巨大成功。 `<!-- ROW_MINE: ksummit.messages.6463 -->`

## 177.8 回归治理

- 【Linux社区】Thorsten Leemhuis 说明 regzbot 初期不追踪 bug 跟踪器报告但预留扩展，并请回复回归报告时抄送 regressions@ 以集中可见。 `<!-- ROW_MINE: ksummit.messages.6373 -->`
- 【Linux社区】Laurent Pinchart 倡议为维护者办培训，以取代口口相传且互相矛盾的规则，称许多人不知有流程；并涉深层维护树减负与回归指南讨论。 `<!-- ROW_MINE: ksummit.messages.6430 -->`

## 177.9 linus-next测试

- 【Linux社区】Steven Rostedt 称测试需 8-13 小时故先推 urgent 分支等 zero-day 机器人，但已收不到其通知，愿加入 linus-next 统一预合并测试。 `<!-- ROW_MINE: ksummit.messages.6379 -->`
- 【Linux社区】Steven Rostedt 同意把测试通过后的 fixes 分支加入 linux-next，urgent 分支保持私有，并改为每周批量发一次拉取请求。 `<!-- ROW_MINE: ksummit.messages.6438 -->`

## 177.10 维护者倦怠

- 【Linux社区】Linus 回顾 2016-2017 年峰会曾有子系统介绍短会，2018 年 Daniel Vetter 称“不必再来”，网络组约 2020 年才开始集体维护，支持重开议题。 `<!-- ROW_MINE: ksummit.messages.6380 -->`
- 【Linux社区】Mark Brown 称嵌入式驱动评审常无人真有硬件，故更看重子系统整合与维护成本的风险画像，建议识别并利用社区已具备集体知识的领域。 `<!-- ROW_MINE: ksummit.messages.6459 -->`

## 177.11 stable补丁流程

- 【Linux社区】Dan Carpenter 说明仅需进 stable 的补丁流程：发 stable@ 并在提交信息说明为何无需上游，回应 Mimi Zohar 之问。 `<!-- ROW_MINE: ksummit.messages.6382 -->`

## 177.12 峰会赞助机制

- 【Linux社区】Theodore Tso 称维护者峰会至多 5 个赞助席位、近 3 年零赞助改由 LF 买单，企业更愿为 LSF/MM 技术讨论付费，AI 数据中心挤占会议预算。 `<!-- ROW_MINE: ksummit.messages.6385 -->`

## 177.13 Bugzilla退役

- 【Linux社区】Laurent Pinchart 力主用确定性方案解码栈回溯而非 LLM，提议建 debuginfo 数据库，并认可 Sasha 提出的 kallsyms 内嵌文件行号方案更佳。 `<!-- ROW_MINE: ksummit.messages.6386 -->`
- 【Linux社区】Geert 统计 v5.19 后主分支含 2928 个 Fixes 即日均 46 个修复；Joe Perches 指出其中多为 -rc 周期引入问题的修复，不能证明已发布版本的缺陷量。 `<!-- ROW_MINE: ksummit.messages.6462 -->`
- 【Linux社区】资深用户 Artem 叙述 20 余年 IT 经验仍不知 bug 该报给谁、抄送谁，质疑普通报告者可及性；Greg 示范 get_maintainer.pl 定位看门狗维护者。 `<!-- ROW_MINE: ksummit.messages.6475 -->`
- 【Linux社区】Hans de Goede 称 Red Hat 迁 Jira 仅限 RHEL 9 之后版本、Fedora 未定，且 RH 团队正把 Bugzilla 移植到 PostgreSQL 以摆脱停更的 MySQL 依赖。 `<!-- ROW_MINE: ksummit.messages.6487 -->`
- 【Linux社区】Laurent Pinchart 担忧资源匮乏下 bug 追踪只能在“报告者爱用”与“维护者适用”间二选一，并戏言年轻一代或逼维护者改用视频评审。 `<!-- ROW_MINE: ksummit.messages.6500 -->`

## 177.14 Rust聚合传递

- 【Linux社区】Miguel Ojeda 纠正 Ventura Jack：混淆了“模型不允许所有 unsafe 模式”与“无法判定 UB”，称别名规则不绑定 LLVM，其他编译器可取更保守假设。 `<!-- ROW_MINE: ksummit.messages.6390 -->`
- 【Linux社区】Ventura Jack 长文反驳 Ralf Jung：举 Rust 1.80 破坏 time crate 波及 5000 余 crates，质疑对 LLVM 的隐藏依赖，引 trait solver 难题与 Perl 6、Scala 3 教训。 `<!-- ROW_MINE: ksummit.messages.6409 -->`
- 【Linux社区】Kent Overstreet 指出内核 Rust panic 用 abort 不展开；若支持完整展开，“无 unsafe 加依赖白名单”的 Rust 或能以更易用方式取代 BPF。 `<!-- ROW_MINE: ksummit.messages.6421 -->`
- 【Linux社区】Paul McKenney 与 David Laight 讨论 READ_ONCE：gcc 对 volatile 读生成多余寄存器搬运甚至拆分访问，期待 __atomic_load_n RELAXED 日后可用。 `<!-- ROW_MINE: ksummit.messages.6448 -->`

## 177.15 内核文档建设

- 【Linux社区】Vegard 实测 PyPy 提速 22%、约 40% 构建耗时在 Sphinx resolve_xref；Mauro 主张默认保留交叉引用，指出 C domain 无法区分同名不同类符号的长期缺陷。 `<!-- ROW_MINE: ksummit.messages.6392 -->`
- 【Linux社区】Corbet 称 LF 资助付费文档实验因选题过难、写手不称职而失败；Mauro 提出书籍组织、uAPI、ABI、kernel-doc、kAPI 五类任务并介绍 get_abi 工具与 sysfs 大量缺口。 `<!-- ROW_MINE: ksummit.messages.6414 -->`
- 【Linux社区】Laurent Pinchart 指出 drm_atomic_helper.c 的 DOC: overview 块加 kernel-doc :doc: 即可把代码旁设计注释并入文档，回应 Rostedt 设计文档标记之问。 `<!-- ROW_MINE: ksummit.messages.6418 -->`
- 【Linux社区】Jani Nikula 称构建系统不支持子系统提前保持 W=1 与 kernel-doc 干净，DRM 用 Makefile 变通降低破损；Randy 实测全配置约 450 条警告。 `<!-- ROW_MINE: ksummit.messages.6439 -->`

## 177.16 TAB选举

- 【Linux社区】Laura Abbott 发布 2021 TAB 选举提名公告：十席半数换届，Greg KH、Corbet、Levin、Rostedt、Ts'o 任期届满，资格为 2020-21 年三个标签 commit，9 月 20 日硬截止。 `<!-- ROW_MINE: ksummit.messages.6426 -->`

## 177.17 DRM面板驱动

- 【Linux社区】Wacom 的 Ping Cheng 回应 Linus Walleij：公司重视 Linux 客户，但面板厂商不向其提供规格，现以 ddcutil 方案供 Linux 用户调节显示。 `<!-- ROW_MINE: ksummit.messages.6431 -->`

## 177.18 Link标签之争

- 【Linux社区】Steven Rostedt 声明若被要求手删 Link 标签他将不再添加任何链接，因其脚本自动生成且徒增负担，呼应 Greg 对源码史料损失的担忧。 `<!-- ROW_MINE: ksummit.messages.6443 -->`

## 177.19 生成代码入库

- 【Linux社区】James Bottomley 解释 aic7xxx 预生成输出因工具在树内而人人一致，该工具已悄然朽坏仅存历史意义，回应 Linus 关于随树发布工具的问题。 `<!-- ROW_MINE: ksummit.messages.6466 -->`
- 【Linux社区】Steven Rostedt 自述因用户 flex/bison 版本过旧无法构建，把生成的 C 文件提交进仓库后再无抱怨，与 Linus“永远现构建”主张形成对照。 `<!-- ROW_MINE: ksummit.messages.6479 -->`

## 177.20 治理透明度

- 【Linux社区】Bottomley 与 Greg KH 争执 Rust 维护者辞职事件：前者称开发者退出致仅剩 Linus 独扛且不透明招致猜测，后者称 35 年仅一次、流程文档无济于事。 `<!-- ROW_MINE: ksummit.messages.6469 -->`

## 177.21 内存分配API

- 【Linux社区】Vlastimil Babka 指出新写法 kzalloc_obj(*x) 已隐含 GFP_KERNEL，回应 Wilcox 提议的“仅分配内存”简易分配器与 Brown 对 kzalloc 默认化的观察。 `<!-- ROW_MINE: ksummit.messages.6484 -->`

## 177.22 uAPI准入标准

- 【Linux社区】Leon Romanovsky 主张新 uAPI 必须进入 Debian、Fedora、SuSE 软件包，GitHub 代码演示是最差凭证，自述 RDMA 面向企业与云，busybox 亦属发行版生态。 `<!-- ROW_MINE: ksummit.messages.6488 -->`
