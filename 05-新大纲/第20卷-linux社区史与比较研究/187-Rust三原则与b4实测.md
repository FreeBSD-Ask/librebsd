# 187 【Linux社区】Rust三原则与b4实测

> 来源：ksummit 独有 p51（50 封全读，2025-02 至 2026-08：Pinchart 把 Rust 政策争论提炼为不强制处理 Rust 不得 nack 抽象不得破坏构建三原则最多同时成立两条的矛盾系整场辩论最清晰立场陈述；Ryabitsev 给出 b4 自动化十次错九次实测与六种 Message-ID 匹配失败场景直接催生 patch.msgid.link 域约定；Laura Abbott 2021 TAB 选举完整结果原始记录 1012 名合格投票者 237 投票前五名当选；Ralf Jung 对 Miri 与 C 标准形式化 Cerberus CompCert 与规范哲学系统阐述；Rust 引入讨论六封、Rust 政策讨论四封、峰会存废讨论四封）
> 判定：47 CAND / 3 NV。主题分布：峰会存废讨论 3、TAB选举 2、Rust引入讨论 6、AI审查工具 3、AI补丁标注 1、稳定树回移 2、信任网与PGP 2、THE REST分流 1、linus-next测试 3、next隐藏提交 1、LLM标签与信任 2、设备直通争论 3、AI生成内容规范 2、Rust政策讨论 3、Bugzilla存废 2、Rust形式化验证 2、UMN假补丁事件 1、cleanup.h规则 1、回归追踪 1、补丁接收政策 1、老旧文件系统 1、stable邮件量 1、C内存安全提案 1、安全流程扩展 1、Link标签规范 1。

## 187.1 峰会存废讨论

- **要点**：Greg KH批驳Airlie的DRM合并窗口说：开发者无需停工，只需分清新功能与修复入不同队列；并称DRM树模式致Fixes:标签全错、回归与CVE追踪尽坏，殃及稳定树回移。Rostedt认同Rafael所指conclave.rst应急计划：维护者峰会已具正式地位，若大幅改格式须同步修订这份“制定计划的计划”。Airlie称AMD与Intel各50至100人跨多团队喂同一驱动，难要求全员理解上游周期；Geert指先合入next再发布有助减少冲突但破坏commit ID唯一性，殃及stable追踪与Fixes:标签。
- **史料**：`ksummit.messages.7917`（Greg KH，2026-08-12）、`ksummit.messages.7924`（Steven Rostedt，2026-08-07）、`ksummit.messages.8025`（Geert Uytterhoeven，2026-08-11）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.7917 -->` `<!-- ROW_MINE: ksummit.messages.7924 -->` `<!-- ROW_MINE: ksummit.messages.8025 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：Greg KH、Steven Rostedt 与 Geert Uytterhoeven三种立场并置）；经验优先（总纲第 9 条——经验优先：以 DRM 树模式致 Fixes: 标签全错、CVE 追踪尽坏的实际后果为判据）
- **辨析**：三条分属 2026-08 同一存废线程；Geert 的“破坏 commit ID 唯一性”为技术推断，落书不得据以断言 stable 追踪已失效。
- **文献**：DSLXC-10921、DSLXC-10923、DSLXC-10957（`ksummit.messages.7917`、`ksummit.messages.7924`、`ksummit.messages.8025`，2026-08-12、2026-08-07、2026-08-11），全文见 `raw_source.raw_json`

## 187.2 TAB选举

- **要点**：Laura Abbott澄清TAB选举投票规则：超50提交者自动获寄选票，3至49提交者须主动申请，承认表述混乱并承诺次年改进流程。2021年TAB选举结果：1012名有资格投票者中237人投票，Greg KH、Corbet、Rostedt、Ts'o、Levin当选两年任期，Hansen、Overstreet、Taht落选。
- **史料**：`ksummit.messages.7921`（Laura Abbott，2021-09-15）、`ksummit.messages.8019`（Laura Abbott，2021-09-24）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.7921 -->` `<!-- ROW_MINE: ksummit.messages.8019 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 1012 名合格投票者、237 人投票的实测计数为准）；自反性声明（总纲第 7/23 条——理论必须自反／一切历史写作都是基于哲学设定的历史小说：当事人自认投票规则表述混乱并承诺改进）
- **辨析**：两条分属 2021-09-15 与 2021-09-24 的选举公告与结果公布；投票与当选数字为公告原文，落书须以当期公告为准。
- **文献**：DSLXC-10922、DSLXC-10954（`ksummit.messages.7921`、`ksummit.messages.8019`，2021-09-15、2021-09-24），全文见 `raw_source.raw_json`

## 187.3 Rust引入讨论

- **要点**：Belloni审视Rust版PL061与C版反汇编对比，质疑示例关闭溢出检查、rust_helper_readb未内联成函数调用，并指简单驱动才代表多数待转换场景。Wedson详解Rust版PL061：编译期边界检查决定writeb与try_writeb取舍、drvdata类型安全免运行时代价、可撤销资源防设备移除后误用、RAII取代goto清理链。Leon Romanovsky列第二语言两大代价：跨子系统grep替换式重构变难、CONFIG组合下编译与验证矩阵翻倍；经Walleij解释“整块替换而非第二内核”后表示可以接受。Pinchart认为若目标只是RAII等特性C++勉强算替代但弊大于利，Rust是第二语言佳选；惟收益能否抵过开发流程扰动尚待观察，并希望Rust语法当初更贴近C。Pinchart部分反驳Linus对C++的否定：析构函数、unique_ptr、类型安全模板对内核有用，但承认C++无真正类型与运行时安全，只盼纯C能拥有带析构的对象。Ojeda回应Levin“抽象成孤儿”论：此问题与语言无关且RFC已承认第二语言代价；过渡期由子系统维护者与Rust团队协助重构，长期仍需多数开发者掌握Rust。
- **史料**：`ksummit.messages.7926`（Alexandre Belloni，2021-07-20）、`ksummit.messages.7939`（Wedson Almeida Filho，2021-07-19）、`ksummit.messages.8008`（Leon Romanovsky，2021-07-06）、`ksummit.messages.8013`（Laurent Pinchart，2021-07-07）、`ksummit.messages.8016`（Laurent Pinchart，2021-07-07）、`ksummit.messages.8055`（Miguel Ojeda，2021-07-06）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.7926 -->` `<!-- ROW_MINE: ksummit.messages.7939 -->` `<!-- ROW_MINE: ksummit.messages.8008 -->` `<!-- ROW_MINE: ksummit.messages.8013 -->` `<!-- ROW_MINE: ksummit.messages.8016 -->` `<!-- ROW_MINE: ksummit.messages.8055 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：Alexandre Belloni 的质疑、Wedson 的自辩、Leon Romanovsky 的代价论与 Laurent Pinchart 的两说并置）；经验优先（总纲第 9 条——经验优先：以 PL061 反汇编与编译期边界检查的实际取舍为判据）
- **辨析**：六条分属 2021-07 同一“Rust 是否引入”大线程；“收益能否抵过开发流程扰动尚待观察”为当事人明示的未决判断。
- **文献**：DSLXC-10924、DSLXC-10927、DSLXC-10950、DSLXC-10951、DSLXC-10952、DSLXC-10963（`ksummit.messages.7926`、`ksummit.messages.7939`、`ksummit.messages.8008`、`ksummit.messages.8013`、`ksummit.messages.8016`、`ksummit.messages.8055`，2021-07-20、2021-07-19、2021-07-06、2021-07-07、2021-07-07、2021-07-06），全文见 `raw_source.raw_json`

## 187.4 AI审查工具

- **要点**：Gushchin谈Sashiko AI审查：可用自定义提示审查LTS回移，有主线基线噪音更小；多模型并行跑发现阶段1至7可互相协作提质；可查预存缺陷库避免重复上报。Mason澄清BPF的AI评审已在GitHub kernel-patches/bpf运行（如PR 9962即评审提示产物）；Rostedt提议把AI挂到patchwork由服务器侧付费运行而非转嫁提交者。Bottomley不认同AI审查的专有技术锁定担忧：先例有BitKeeper与Kubernetes的Slack；更可能是AI泡沫破裂投资退潮、开源AI上位；无论如何AI进CI优于压给贡献者。
- **史料**：`ksummit.messages.7931`（Roman Gushchin，2026-07-15）、`ksummit.messages.7971`（Arnaldo Carvalho de Melo，2025-10-09）、`ksummit.messages.8032`（James Bottomley，2025-10-10）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.7931 -->` `<!-- ROW_MINE: ksummit.messages.7971 -->` `<!-- ROW_MINE: ksummit.messages.8032 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 Sashiko、kernel-patches/bpf 与 patchwork的实际运行实例为分析单位）；偶然性优先（总纲第 5 条——没有必然性，只有偶然性：AI 审查落地由具体工具的可用性驱动）
- **辨析**：三条分属 2025-10 与 2026-07 两个时段，讨论对象为不同工具；“AI 进 CI 优于压给贡献者”系 James Bottomley 的价值判断，非共识结论。
- **文献**：DSLXC-10925、DSLXC-10938、DSLXC-10959（`ksummit.messages.7931`、`ksummit.messages.7971`、`ksummit.messages.8032`，2026-07-15、2025-10-09、2025-10-10），全文见 `raw_source.raw_json`

## 187.5 AI补丁标注

- **要点**：Tony Luck指当前AI只会按提示在输出上贴“SPDX-License-Identifier: GPL-2.0-only”即自称成功，要确保许可兼容须付费用仅含GPL代码训练的专用模型。
- **史料**：`ksummit.messages.7933`（Luck, Tony，2025-09-16）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.7933 -->`
- **史观**：法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：许可兼容问题被还原为训练数据与付费模型的利益安排）；经验优先（总纲第 9 条——经验优先：以 AI 实际只贴 SPDX 行即自称成功这一观察为准）
- **辨析**：本块系 Tony Luck 的单方观察与建议；“须付费用仅含 GPL 代码训练的专用模型”为设想，本页未见可行方案。
- **文献**：DSLXC-10926（`ksummit.messages.7933`，2025-09-16），全文见 `raw_source.raw_json`

## 187.6 稳定树回移

- **要点**：Leemhuis提案区分紧急与非紧急回移：稳定树只回移主线存在约两周或到rc4后的修复，扩展Fixes:标签加延时注记，并指补丁系列依赖关系无从识别致回移出错。Carpenter实测Link:标签不可靠：抽查首例即v1链接配v3提交；按函数名在lore检索排第44、按作者排第113，感叹逐补丁溯源不可行。
- **史料**：`ksummit.messages.7941`（Thorsten Leemhuis，2024-06-13）、`ksummit.messages.7996`（Dan Carpenter，2024-06-17）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.7941 -->` `<!-- ROW_MINE: ksummit.messages.7996 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以抽查首例即 v1 链接配 v3 提交、lore 检索排第 44／第 113 的实测为准）；动手者叙事（总纲第 10 条——动手者创造历史：以回移操作的实际出错路径为分析单位）
- **辨析**：两条分属 2024-06-13 与 2024-06-17；Carpenter 的检索位次为单次抽查，属样本而非统计，落书须标明其抽样性质。
- **文献**：DSLXC-10928、DSLXC-10945（`ksummit.messages.7941`、`ksummit.messages.7996`，2024-06-13、2024-06-17），全文见 `raw_source.raw_json`

## 187.7 信任网与PGP

- **要点**：Mauro强调PGP信任网仍用于签git标签请Linus合并，git 2.52.0前标签签名仅允许PGP；kernel.org密钥环约600个密钥，欢迎ssh推送但须有同等信任机制。Mauro想换后量子算法主密钥加3至5年有效期可撤销子密钥，但gpg 2.4不支持、升2.5会生成不兼容LibrePGP密钥，远程重建信任网亦难，只能等新版本再动。
- **史料**：`ksummit.messages.7948`（Mauro Carvalho Chehab，2026-01-26）、`ksummit.messages.7973`（Mauro Carvalho Chehab，2026-01-26）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.7948 -->` `<!-- ROW_MINE: ksummit.messages.7973 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 kernel.org 密钥环约 600 个密钥、git 2.52.0 前标签签名仅允许 PGP 等可核验事实为判据）；知识注定过时（总纲第 22 条——知识注定过时：后量子算法受 gpg 2.4 不支持所限只能等待新版本）
- **辨析**：两条均为 Mauro Carvalho Chehab 于 2026-01-26 的技术陈述；密钥数为当事人转述，须与 kernel.org 密钥环实况核对。
- **文献**：DSLXC-10929、DSLXC-10939（`ksummit.messages.7948`、`ksummit.messages.7973`，2026-01-26、2026-01-26），全文见 `raw_source.raw_json`

## 187.8 THE REST分流

- **要点**：Bonzini质疑lore存档完整性：lkml下git仓库收不全补丁，也无从过滤非Linux项目的/all/1.git，影响“THE REST”迁出vger的可行性。
- **史料**：`ksummit.messages.7949`（Paolo Bonzini，2023-11-07）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.7949 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 lore 存档实际收不全补丁这一可复核现象为判据）；偶然性优先（总纲第 5 条——没有必然性，只有偶然性：迁出 vger 的可行性由存档完整性这一偶然技术条件决定）
- **辨析**：本块系 Paolo Bonzini 的可行性质疑，属技术条件审查；“无从过滤非 Linux 项目的 /all/1.git”为当事人实测结论。
- **文献**：DSLXC-10930（`ksummit.messages.7949`，2023-11-07），全文见 `raw_source.raw_json`

## 187.9 linus-next测试

- **要点**：Bart Van Assche建议把blktests纳入linus-next的LKFT与KernelCI测试，称该套件报出的失败多数最终证明是内核缺陷而非测试自身问题。Jiri Kosina回忆当年维护者峰会结论：多数人认为持续投入资源加固linux-next测试不划算，不如在rc1后阶段集中处理失败。Rostedt自述urgent与core双分支流程：修Linus树的紧急修复不进linux-next，经约8小时测试后直发PR；若-next反馈更好愿考虑纳入，并支持PR健康检查机器人报告抄送、bake时长与测试失败。
- **史料**：`ksummit.messages.7951`（Bart Van Assche，2024-10-21）、`ksummit.messages.7979`（Jiri Kosina，2024-10-22）、`ksummit.messages.8065`（Steven Rostedt，2024-10-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.7951 -->` `<!-- ROW_MINE: ksummit.messages.7979 -->` `<!-- ROW_MINE: ksummit.messages.8065 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 blktests 报出的失败多数证明是内核缺陷这一实测为准）；多方平等（总纲第 8 条——本体论上各方平等：加大 -next 投入与 rc1 后集中处理两说并置）
- **辨析**：三条分属 2024-10-21、2024-10-22（两封）；Jiri Kosina 所忆“当年峰会结论”属回忆材料，落书须与当年纪要核对。
- **文献**：DSLXC-10931、DSLXC-10940、DSLXC-10965（`ksummit.messages.7951`、`ksummit.messages.7979`、`ksummit.messages.8065`，2024-10-21、2024-10-22、2024-10-22），全文见 `raw_source.raw_json`

## 187.10 next隐藏提交

- **要点**：Mark Brown支持子维护者树进linux-next：修复树缺席致-next坏一周会掩盖其他测试结果；多数人乐意入next只是遗忘或不了解，另有封面信附PR未经评审即藏提交的情形。
- **史料**：`ksummit.messages.7954`（Mark Brown，2025-09-11）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.7954 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以修复树缺席致 -next 坏一周并掩盖其他测试结果这一实际后果为判据）；多方平等（总纲第 8 条——本体论上各方平等：遗忘／不了解与封面信附 PR 藏提交两类情形并置）
- **辨析**：本块系 Mark Brown 的单方支持与分类；“多数人乐意入 next”为当事人估计，本页未附统计。
- **文献**：DSLXC-10932（`ksummit.messages.7954`，2025-09-11），全文见 `raw_source.raw_json`

## 187.11 LLM标签与信任

- **要点**：Howlett认同Weiner观点：LLM参与度是巨大光谱，二值标签信噪比差且已带污名，无法传递“谁在哪步思考”的真实分工，提交元数据难以承载这些细节。Rostedt质疑Kees提议的Debian式贡献者活动仪表盘：可被xz事件式手段刷分操纵，建立信任最终仍靠人与人之间的联系。
- **史料**：`ksummit.messages.7958`（Liam R. Howlett，2026-07-17）、`ksummit.messages.7962`（Steven Rostedt，2026-07-23）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.7958 -->` `<!-- ROW_MINE: ksummit.messages.7962 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“谁在哪步思考”这一实际分工信息无法由二值标签承载为判据）；多方平等（总纲第 8 条——本体论上各方平等：Liam R. Howlett 的标签无效论与 Steven Rostedt 的仪表盘可操纵论并置）
- **辨析**：两条分属 2026-07-17 与 2026-07-23；“已带污名”“可被 xz 事件式手段刷分”均为当事人判断，非实证结论。
- **文献**：DSLXC-10933、DSLXC-10935（`ksummit.messages.7958`、`ksummit.messages.7962`，2026-07-17、2026-07-23），全文见 `raw_source.raw_json`

## 187.12 设备直通争论

- **要点**：Pinchart建议设备直通议题改到LPC开专场，因相关专家太多峰会房间装不下；但忧心演成公开争斗，且有些论据不便在开放场合陈述。Kosina以hidraw与FIDO令牌反驳直通有害论：libfido2用户态驱动已普及用于kernel.org、Google等认证，生态未碎、无工作流被破坏。Figa澄清V4L2有无状态解码器接口，命令缓冲与固定功能两种界面在DRM与V4L2各有取舍；点名Intel IPU6及更新、Qualcomm、MediaTek的ISP原生用命令缓冲。
- **史料**：`ksummit.messages.7959`（Laurent Pinchart，2024-07-26）、`ksummit.messages.7985`（Jiri Kosina，2024-07-23）、`ksummit.messages.8038`（Tomasz Figa，2024-08-13）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.7959 -->` `<!-- ROW_MINE: ksummit.messages.7985 -->` `<!-- ROW_MINE: ksummit.messages.8038 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：直通有害论与 hidraw／FIDO 反例并置）；经验优先（总纲第 9 条——经验优先：以 libfido2 已在 kernel.org、Google 认证中普及这一实况为判据）
- **辨析**：三条分属 2024-07-23、2024-07-26 与 2024-08-13；Pinchart 所称“有些论据不便在开放场合陈述”为程序性顾虑，非技术结论。
- **文献**：DSLXC-10934、DSLXC-10943、DSLXC-10961（`ksummit.messages.7959`、`ksummit.messages.7985`、`ksummit.messages.8038`，2024-07-26、2024-07-23、2024-08-13），全文见 `raw_source.raw_json`

## 187.13 AI生成内容规范

- **要点**：Stoakes主张文档明确：LLM使端到端无经验投稿成为可能，明显AI垃圾应可直接拒绝；Williams担心“猎巫”伤社区，Stoakes称只针对极端明显案例。Stoakes反驳Carpenter软化草案：能理解并辩护所提交代码是内核评审基本要求；若文档要求“多人仔细审”500个工具生成补丁，等于放弃直接拒绝AI垃圾的立场。
- **史料**：`ksummit.messages.7967`（Lorenzo Stoakes，2026-01-08）、`ksummit.messages.8067`（Lorenzo Stoakes，2026-01-13）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.7967 -->` `<!-- ROW_MINE: ksummit.messages.8067 -->`
- **史观**：拒绝进步叙事（总纲第 1/3 条——一切真历史都是古代史／不存在进步，只有权力再分配：AI 生成内容之争不写作工具“进步”）；多方平等（总纲第 8 条——本体论上各方平等：直接拒绝 AI 垃圾与担心“猎巫”两说并置）
- **辨析**：两条均为 Lorenzo Stoakes 于 2026-01-08 与 2026-01-13 的主张；“只针对极端明显案例”系其自设边界，本页未见成文条款。
- **文献**：DSLXC-10936、DSLXC-10966（`ksummit.messages.7967`、`ksummit.messages.8067`，2026-01-08、2026-01-13），全文见 `raw_source.raw_json`

## 187.14 Rust政策讨论

- **要点**：Boqun Feng称其评审中Rust补丁与C补丁同标准；政策文档讲“子系统如何引入Rust”等更高层内容；并指Jarkko的DMA补丁仅有函数定义级doc测试。Pinchart点破“屋里的大象”：不强制维护者处理Rust、不得nack Rust抽象、不得破坏Rust构建三条原则最多同时成立两条，质问社区准备先放弃哪条。Ted Ts'o批评Wedson FS幻灯的绑定对C程序员过于复杂，建议改造C侧抽象使Rust绑定易维护可自动生成、新手可更新、热路径少回归，并以“同时解决多问题”作为方向判据。
- **史料**：`ksummit.messages.7969`（Boqun Feng，2025-02-19）、`ksummit.messages.7982`（Laurent Pinchart，2025-02-23）、`ksummit.messages.8069`（Theodore Ts'o，2025-02-19）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.7969 -->` `<!-- ROW_MINE: ksummit.messages.7982 -->` `<!-- ROW_MINE: ksummit.messages.8069 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：Boqun Feng 的同标准论、Laurent Pinchart 的三原则矛盾与 Theodore Ts'o 的绑定复杂度批评并置）；自反性声明（总纲第 7/23 条——理论必须自反／一切历史写作都是基于哲学设定的历史小说：以“屋里的大象”自陈本议题的结构性张力）
- **辨析**：三条分属 2025-02-19、2025-02-23 与 2025-02-19；“三原则最多同时成立两条”系 Pinchart 的逻辑推论，本页未见任一方否认。
- **文献**：DSLXC-10937、DSLXC-10941、DSLXC-10967（`ksummit.messages.7969`、`ksummit.messages.7982`、`ksummit.messages.8069`，2025-02-19、2025-02-23、2025-02-19），全文见 `raw_source.raw_json`

## 187.15 Bugzilla存废

- **要点**：Weinberger发布kcontact原型：静态JS网站粘贴内核日志即分析栈回溯，查x86_64全模块预生成符号表映射到子系统L:条目并跳过前3帧入口代码，指引报告去向。Tarreau捍卫邮件为内核开发通用语：反驳“邮件在开会一周后失效”，称会议上人们屏幕只有代码、幻灯与邮件，bug报告随邮箱自然可见，bugzilla界面则无人看。
- **史料**：`ksummit.messages.7984`（Richard Weinberger，2026-03-06）、`ksummit.messages.8036`（Willy Tarreau，2022-10-02）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.7984 -->` `<!-- ROW_MINE: ksummit.messages.8036 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 kcontact 原型的实际实现路径为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：缺陷跟踪网站与邮件列表两种载体主张并置）
- **辨析**：两条分属 2026-03-06 与 2022-10-02，讨论对象跨越四年；“bugzilla 界面则无人看”为当事人断言，非使用统计。
- **文献**：DSLXC-10942、DSLXC-10960（`ksummit.messages.7984`、`ksummit.messages.8036`，2026-03-06、2022-10-02），全文见 `raw_source.raw_json`

## 187.16 Rust形式化验证

- **要点**：Ventura Jack问询Rust验证工具现状：Prusti数月无提交，Gillian-Rust未用stacked或tree borrows，RefinedRust复用Miri代码，关注研究原型与实用的距离。Jung论证Miri独一无二：C侧仅Cerberus可执行规范但只跑微型示例，C标准歧义致编译器与程序员理解冲突；Rust追求规定性无歧义规范，1.84已悄然启用新trait solver。
- **史料**：`ksummit.messages.7994`（Ventura Jack，2025-02-26）、`ksummit.messages.8029`（Ralf Jung，2025-02-26）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.7994 -->` `<!-- ROW_MINE: ksummit.messages.8029 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 Prusti 数月无提交、Gillian-Rust 未用 borrows、RefinedRust 复用 Miri 代码等工具现状为判据）；多方平等（总纲第 8 条——本体论上各方平等：C 侧 Cerberus 与 Rust 侧 Miri 两种形式化路径并置）
- **辨析**：两条分属 2025-02-26 的提问与回答；“1.84 已悄然启用新 trait solver”为 Ralf Jung 的技术陈述，须与发行说明核对。
- **文献**：DSLXC-10944、DSLXC-10958（`ksummit.messages.7994`、`ksummit.messages.8029`，2025-02-26、2025-02-26），全文见 `raw_source.raw_json`

## 187.17 UMN假补丁事件

- **要点**：Mauro披露media子系统29个被回退补丁无恶意代码，仅1个冗余其余有效，质疑盲目回退umn.edu补丁；引Morris称因不知实验范围须审计其全部贡献。
- **史料**：`ksummit.messages.7997`（Mauro Carvalho Chehab，2021-04-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.7997 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 media 子系统 29 个被回退补丁中仅 1 个冗余、其余有效的逐条清点为判据）；多方平等（总纲第 8 条——本体论上各方平等：盲目回退与须审计全部贡献两种处置并置）
- **辨析**：本块系 Mauro Carvalho Chehab 的披露，其引 James Morris 之说；29 与 1 为当事人清点结果，本页未附逐条清单。
- **文献**：DSLXC-10946（`ksummit.messages.7997`，2021-04-22），全文见 `raw_source.raw_json`

## 187.18 cleanup.h规则

- **要点**：Bottomley谈__free变量放置：认同在分配处声明可免去空指针释放检查、便于新增早退；并提出以显式作用域块限定变量使用范围，配合scoped_guard处理锁与释放纠缠。
- **史料**：`ksummit.messages.8002`（James Bottomley，2025-11-18）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8002 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 __free 变量的声明位置与早退路径为分析单位）；经验优先（总纲第 9 条——经验优先：以显式作用域块与 scoped_guard 的实际配合为准）
- **辨析**：本块系 James Bottomley 的设计建议；“便于新增早退”为其论据，非实测对比。
- **文献**：DSLXC-10947（`ksummit.messages.8002`，2025-11-18），全文见 `raw_source.raw_json`

## 187.19 回归追踪

- **要点**：Leemhuis拟LPC回归专场：KernelCI与regzbot已合并运作，介绍回归追踪现状与计划，并讨论AI时代regzbot是否仍有用、要不要建pending与wip修复树。
- **史料**：`ksummit.messages.8003`（Thorsten Leemhuis，2026-06-28）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8003 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 KernelCI 与 regzbot 已合并运作这一实际状态为起点）；偶然性优先（总纲第 5 条——没有必然性，只有偶然性：是否仍有用由 AI 时代这一外部变化引出）
- **辨析**：本块系 Thorsten Leemhuis 的专场提案与议程设想；“要不要建 pending 与 wip 修复树”止于待议，本页无结论。
- **文献**：DSLXC-10948（`ksummit.messages.8003`，2026-06-28），全文见 `raw_source.raw_json`

## 187.20 补丁接收政策

- **要点**：Rostedt反对邮件列表强制封面信抄送校验：会破坏quilt工作流，自称、Peter Zijlstra与Andrew Morton皆用quilt；也不愿被稳定补丁封面信抄送。
- **史料**：`ksummit.messages.8006`（Steven Rostedt，2021-04-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8006 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 quilt 工作流实际会被封面信抄送校验破坏为判据）；多方平等（总纲第 8 条——本体论上各方平等：强制校验与工作流兼容两说并置）
- **辨析**：本块系 Steven Rostedt 的反对意见，其自陈与 Peter Zijlstra、Andrew Morton 同用 quilt；“不愿被稳定补丁封面信抄送”属个人偏好，非政策立场。
- **文献**：DSLXC-10949（`ksummit.messages.8006`，2021-04-22），全文见 `raw_source.raw_json`

## 187.21 老旧文件系统

- **要点**：Hellwig反驳Linus：“别启用”不可行，老旧文件系统支持状态随内核版本变化须内核内标记，syzbot骚扰需统一停报机制；并澄清要去除的是buffer_head整文件I/O助手而非buffer cache。
- **史料**：`ksummit.messages.8017`（Christoph Hellwig，2023-09-25）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8017 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以老旧文件系统支持状态随内核版本变化的实际情形为判据）；多方平等（总纲第 8 条——本体论上各方平等：Linus 的“别启用”与 Hellwig 的内核内标记论并置）
- **辨析**：本块系 Christoph Hellwig 的反驳与澄清；“须统一停报机制”为提议，本页未见机制方案。
- **文献**：DSLXC-10953（`ksummit.messages.8017`，2023-09-25），全文见 `raw_source.raw_json`

## 187.22 stable邮件量

- **要点**：Takashi Iwai为stable抄送邮件辩护：个别补丁经带fuzz的cherry-pick会错打，须见原补丁才能核查，完全过滤将失去这一发现渠道。
- **史料**：`ksummit.messages.8023`（Takashi Iwai，2025-08-06）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8023 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以带 fuzz 的 cherry-pick 会错打、须见原补丁方能核查这一实测为判据）
- **辨析**：本块系 Takashi Iwai 的单方辩护；“完全过滤将失去这一发现渠道”为其判断，本页未见反例。
- **文献**：DSLXC-10955（`ksummit.messages.8023`，2025-08-06），全文见 `raw_source.raw_json`

## 187.23 C内存安全提案

- **要点**：Uecker提议仿GCC诊断pragma划区启用内存安全检查，含运行期陷阱的DYNAMIC模式；并展示UBSan插桩后仅当优化器未消除陷阱才告警，可借优化器证明无溢出，已有GCC补丁。
- **史料**：`ksummit.messages.8024`（Martin Uecker，2025-02-21）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8024 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以仿 GCC 诊断 pragma 的划区启用与 UBSan 插桩为分析单位）；经验优先（总纲第 9 条——经验优先：以优化器未消除陷阱才告警这一实测行为为判据）
- **辨析**：本块系 Martin Uecker 的提案，并自陈已有 GCC 补丁；补丁是否合入本页未见结论。
- **文献**：DSLXC-10956（`ksummit.messages.8024`，2025-02-21），全文见 `raw_source.raw_json`

## 187.24 安全流程扩展

- **要点**：Greg KH披露security@近月已理顺并将获约6个月专人全职经费；LLM仅限本地模型因涉法律约束，AI接入过滤不可行，真正难题是不回应的报告者与横插一手的中间商。
- **史料**：`ksummit.messages.8044`（Sasha Levin，2026-07-16）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8044 -->`
- **史观**：偶然性优先（总纲第 5 条——没有必然性，只有偶然性：security@ 理顺与约 6 个月全职经费这一资源安排带有偶然性）；法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：LLM 仅限本地模型系法律约束所致）
- **辨析**：本块系 Sasha Levin 的披露；“约 6 个月专人全职经费”为待落实安排，落书不得据以断言已到位。
- **文献**：DSLXC-10962（`ksummit.messages.8044`，2026-07-16），全文见 `raw_source.raw_json`

## 187.25 Link标签规范

- **要点**：Ryabitsev坚持自动化需可靠锚点：b4在作者微调8/10号补丁时十次错九次；列举From与Date被覆盖、误投列表等六种匹配失败场景，提议以patch.msgid.link域或“# patch”注记标示补丁来源。
- **史料**：`ksummit.messages.8060`（Konstantin Ryabitsev，2024-06-17）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.8060 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 b4 在作者微调 8/10 号补丁时十次错九次的实测为准）；动手者叙事（总纲第 10 条——动手者创造历史：以 patch.msgid.link 域约定的形成过程为线索）
- **辨析**：本块系 Konstantin Ryabitsev 的实测报告；六种匹配失败场景为其归纳，落书须以 b4 源码与实测记录核对。
- **文献**：DSLXC-10964（`ksummit.messages.8060`，2024-06-17），全文见 `raw_source.raw_json`
