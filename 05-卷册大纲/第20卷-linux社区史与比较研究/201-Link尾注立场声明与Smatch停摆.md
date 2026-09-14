# 201 【Linux社区】Link尾注立场声明与Smatch停摆

> 来源：ksummit 独有 p65（50 封全读，2021-04 至 2026-07：Linus 关于 Link 尾注的长篇立场声明必须是公开真实链接拒内部 bug ID 与 syzbot 魔数宁 Link 不用 Closes 系理解内核提交元数据社会契约的一手文本；Dan Carpenter 自述 Smatch 静态分析因筹资失败停摆零日机器人只能做低误报检查而漏掉跨函数 bug 记录社区安全工具资金困境事件；Linus 提出 AI 审查下一步由可信团队运营 AI 建高置信 trivial tree 并明确信任的是运营者而非 AI 系 2026 年 AI 审查治理辩论关键立场；Ribalda 与 Pinchart 就 ISP 驱动入 DRM 还是 V4L2 激烈争论含 99% 相机市场依赖树外驱动论据；Link 尾注规范五封、AI 审查流程四封、Bugzilla 退役四封）
> 判定：46 CAND / 4 NV。主题分布：Bugzilla退役 3、Rust绑定自动化 1、AI内容规范 1、文件系统信任标志 1、静态分析注解 1、Bugzilla改革 1、Fixes标签政策 1、Link尾注规范 5、AI审查流程 4、UMN造假事件 1、设备直通争论 1、trivial补丁政策 2、AI版权争议 1、linux-next测试 1、C结构体传参 1、安全报告渠道 1、Rust安全问题 1、内存模型语义 1、VLIW与OoO 1、字符串API迁移 1、内核报错可读性 1、ISP驱动之争 1、AI补丁法律风险 1、kerneldoc检查工具 1、Rust内核panic 1、Rust与stable 1、Rust别名规则 1、设备树绑定政策 1、Smatch资金困境 1、补丁投递工具 1、补丁CC礼节 1、用户态要求 1、gccrs编译器 1、LKML流量改革 1、邮件引用治理 1、维护者支持 1。

## 201.1 Bugzilla退役

- **要点**：Jani Nikula称GitLab免费版issue功能不及Bugzilla、好功能都进付费层，倾向社区驱动的Forgejo；Mario Limonciello建议自建gitlab.kernel.org按子系统建项目跟踪issue。Sasha Levin演示LLM把oops报告定位到xfrm_iptfs.c:905的skb_put并找出元凶提交5f2b6a9095743，提议bug@kernel.org机器人分诊；James Bottomley建议代理扫描全部列表、回复结果并标记回归。Jani Nikula指出MAINTAINERS已有B:字段记录bug提交URI（网页或mailto），支持Morton提议做网页前端：粘贴路径即返回维护者邮箱，补bugzilla退位后的报告入口。
- **史料**：`ksummit.messages.10203`（Jani Nikula，2025-12-18）、`ksummit.messages.10275`（James Bottomley，2026-03-01）、`ksummit.messages.10340`（Jani Nikula，2026-02-27）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10203 -->` `<!-- ROW_MINE: ksummit.messages.10275 -->` `<!-- ROW_MINE: ksummit.messages.10340 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 GitLab/Forgejo 自建、LLM 把 oops 定位到 xfrm_iptfs.c:905 与元凶提交 5f2b6a9095743、MAINTAINERS B: 字段网页前端等具体方案为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：GitLab 免费版不及 Bugzilla 与社区驱动 Forgejo 两方并置）
- **辨析**：三条同属 Bugzilla 退役议题；Jani 的两条为工具选型判断，Bottomley 建议代理扫描全部列表与 Levin 的 LLM 演示为可复现的具体案例。
- **文献**：DSLXC-11477、DSLXC-11493、DSLXC-11513（`ksummit.messages.10203`、`ksummit.messages.10275`、`ksummit.messages.10340`，2025-12-18、2026-03-01、2026-02-27），全文见 `raw_source.raw_json`

## 201.2 Rust绑定自动化

- **要点**：James Bottomley提议在C头文件加注解、由增强bindgen生成Rust绑定并配类sparse校验工具；强调目标非稳定C API，而是让API变更更易传导到Rust侧，Miguel Ojeda认同信息就地保存。
- **史料**：`ksummit.messages.10211`（James Bottomley，2025-02-19）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10211 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以在 C 头文件加注解、由增强 bindgen 生成 Rust 绑定并配类 sparse 校验工具这一具体方案为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：Bottomley 的方案与 Ojeda 认同信息就地保存两方并置）
- **辨析**：本块系 James Bottomley 的提议；“目标非稳定 C API，而是让 API 变更更易传导到 Rust 侧”为其定位。
- **文献**：DSLXC-11478（`ksummit.messages.10211`，2025-02-19），全文见 `raw_source.raw_json`

## 201.3 AI内容规范

- **要点**：Michael Tsirkin赞成“提交者须能理解并自证一切工具生成内容”的守则适用于一切工具而非仅AI，称见过太多“修checkpatch警告”式垃圾补丁，AI生成并无本质不同。
- **史料**：`ksummit.messages.10212`（Michael S. Tsirkin，2026-01-08）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10212 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：守则适用于一切工具而非仅 AI 与“AI 生成并无本质不同”两方并置）；经验优先（总纲第 9 条——经验优先：以“见过太多修 checkpatch 警告式垃圾补丁”这一实际见闻为判据）
- **辨析**：本块系 Michael Tsirkin 的赞成；“AI 生成并无本质不同”为其核心判断。
- **文献**：DSLXC-11479（`ksummit.messages.10212`，2026-01-08），全文见 `raw_source.raw_json`

## 201.4 文件系统信任标志

- **要点**：Linus Torvalds同意对不可信文件系统做内核级标记，建议利用未被充分利用的/proc/filesystems或在挂载选项中加“提示”，按文件系统拒绝以不信任方式挂载介质，回应Hellwig。
- **史料**：`ksummit.messages.10219`（Linus Torvalds，2023-09-25）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10219 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以利用未被充分利用的 /proc/filesystems 或在挂载选项中加“提示”、按文件系统拒绝不信任挂载等具体机制为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：内核级标记不可信文件系统与回应 Hellwig 并置）
- **辨析**：本块系 Linus Torvalds 的同意与建议；“回应 Hellwig”表明为对话记录。
- **文献**：DSLXC-11480（`ksummit.messages.10219`，2023-09-25），全文见 `raw_source.raw_json`

## 201.5 静态分析注解

- **要点**：Arnd Bergmann归纳指针返回值四类注解（有效指针与NULL/错误指针的组合），Geert Uytterhoeven补充*_optional类第五种；Arnd称optional函数应编译期二选一，返回NULL属接口bug。
- **史料**：`ksummit.messages.10225`（Arnd Bergmann，2021-07-26）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10225 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以指针返回值四类注解加 *_optional 第五种这一具体分类为分析单位）；经验优先（总纲第 9 条——经验优先：以“optional 函数应编译期二选一、返回 NULL 属接口 bug”这一实际判据为据）
- **辨析**：本块含 Arnd Bergmann 的归纳与 Geert Uytterhoeven 的补充两方；“返回 NULL 属接口 bug”为 Arnd 的论断。
- **文献**：DSLXC-11481（`ksummit.messages.10225`，2021-07-26），全文见 `raw_source.raw_json`

## 201.6 Bugzilla改革

- **要点**：Greg KH称LF内核实习生预算已全部用完、还有大量无薪实习生，无法资助bug分诊人力；Konstantin Ryabitsev强调此类工作需不可挪用的专项拨款。
- **史料**：`ksummit.messages.10226`（Konstantin Ryabitsev，2022-10-04）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10226 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“LF 内核实习生预算已全部用完、还有大量无薪实习生”这一实际状况为判据）；动手者叙事（总纲第 10 条——动手者创造历史：以“此类工作需不可挪用的专项拨款”这一具体制度要求为分析单位）
- **辨析**：本块含 Greg KH 与 Konstantin Ryabitsev 两方，署名为本封发件人 Konstantin Ryabitsev；“无法资助 bug 分诊人力”为 Greg KH 所述。
- **文献**：DSLXC-11482（`ksummit.messages.10226`，2022-10-04），全文见 `raw_source.raw_json`

## 201.7 Fixes标签政策

- **要点**：James Bottomley主张Fixes:适用于任何改动先前提交之处（含空白与拼写），使回移无需辩论且易验证；cc:stable才用于回归等值得回移的修复，反驳Dan Carpenter“非回归不加Fixes”。
- **史料**：`ksummit.messages.10227`（James Bottomley，2024-07-18）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10227 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：Fixes: 适用于任何改动先前提交之处与 Dan Carpenter 的“非回归不加 Fixes”两方并置）；经验优先（总纲第 9 条——经验优先：以“使回移无需辩论且易验证”这一实际效果为判据）
- **辨析**：本块系 James Bottomley 的主张；“cc:stable 才用于回归等值得回移的修复”为其界定。
- **文献**：DSLXC-11483（`ksummit.messages.10227`，2024-07-18），全文见 `raw_source.raw_json`

## 201.8 Link尾注规范

- **要点**：Michael Tsirkin质疑Konstantin的Link尾注文档未讲清lore.kernel.org与patch.msgid.link两域名各用于何处，并抱怨git am需怪异脚本，无法再靠messageid=true自动生成链接。Linus Torvalds长文阐明Link:必须是公开可点的真实链接以杜绝内部bug ID，斥b4 am来源链接与syzbot魔数Reported-by为噪音，宁用Link不用Closes，自述常按作者加日期在lore挖多年前的讨论。James Bottomley澄清Link仅回链提交的原始邮件、工具只需最后一轮迭代即可用，Konstantin的b4 dig基于patch-id模糊匹配；否认需要Gerrit式Change-Id跨版本追踪提交。Jani Nikula以数据反驳Geert对patchwork.freedesktop.org链接的批评：指向该域的Link:标签逾99%的URL内含Message-ID，可直达原始邮件。Konstantin Ryabitsev指git notes单ref百万文件难扩展且多写者冲突，主张用public-inbox的RFC-2822消息流记录提交注解（X-For-Commit-ID头），把lore当作面向自动化代理的“消息总线”。
- **史料**：`ksummit.messages.10228`（Michael S. Tsirkin，2024-06-19）、`ksummit.messages.10312`（Linus Torvalds，2024-06-16）、`ksummit.messages.10314`（James Bottomley，2025-10-13）、`ksummit.messages.10338`（Jani Nikula，2024-06-17）、`ksummit.messages.10359`（Konstantin Ryabitsev，2025-10-15）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10228 -->` `<!-- ROW_MINE: ksummit.messages.10312 -->` `<!-- ROW_MINE: ksummit.messages.10314 -->` `<!-- ROW_MINE: ksummit.messages.10338 -->` `<!-- ROW_MINE: ksummit.messages.10359 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 public-inbox 的 RFC-2822 消息流记录提交注解、X-For-Commit-ID 头、把 lore 当作面向自动化代理的消息总线等具体机制为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：Linus 的 Link 须公开可点之立场与 Bottomley 的“工具只需最后一轮迭代即可用”两方并置）
- **辨析**：五条同属 Link 尾注规范议题，为本页一手立场文本集中处；Linus 的长文立场为理解提交元数据社会契约的关键，Jani 的“逾 99% URL 内含 Message-ID”为可核数据。
- **文献**：DSLXC-11484、DSLXC-11503、DSLXC-11504、DSLXC-11512、DSLXC-11519（`ksummit.messages.10228`、`ksummit.messages.10312`、`ksummit.messages.10314`、`ksummit.messages.10338`、`ksummit.messages.10359`，2024-06-19、2024-06-16、2025-10-13、2024-06-17、2025-10-15），全文见 `raw_source.raw_json`

## 201.9 AI审查流程

- **要点**：Sasha Levin援引其Assisted-by:（如Claude加checkpatch）披露提案，主张由各子系统自定政策并自动化工作流；Tim Bird建议用标签标注补丁经何种工具审查，缺标签可要求先补。Rodrigo Vivi赞同Guenter Roeck要求作者先处理Sashiko报出的9处问题再人工审，但Mark Brown举出周末迭代15版后被人工否定的反例；Rodrigo援引Sage“想法-架构-打磨”三层审查框架寻折中。Linus Torvalds指“顺手修预存问题”的摩擦早于AI、建数据库难解压力与摩擦，提议由可信团队运营的AI建“trivial tree”承接高置信修复，强调信任的是运营者而非AI本身。Johannes Berg主张Sashiko默认纳入、可事后退出，以免未发声者漏报而被利用，Rostedt附和宁愿多收报告；Bottomley称AI驱动补丁者借提示滥发“恶意硬件修复”，欲从源头退出。
- **史料**：`ksummit.messages.10231`（Sasha Levin，2025-10-08）、`ksummit.messages.10301`（Rodrigo Vivi，2026-07-23）、`ksummit.messages.10325`（Linus Torvalds，2026-07-17）、`ksummit.messages.10342`（Johannes Berg，2026-07-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10231 -->` `<!-- ROW_MINE: ksummit.messages.10301 -->` `<!-- ROW_MINE: ksummit.messages.10325 -->` `<!-- ROW_MINE: ksummit.messages.10342 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 Assisted-by: 披露、Sashiko 默认纳入、可信团队运营的 AI 建 trivial tree 等具体流程为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：Sashiko 默认纳入可事后退出与 AI 驱动补丁者欲从源头退出两方并置）
- **辨析**：四条同属 AI 审查流程议题；Linus 的“信任的是运营者而非 AI 本身”为 2026 年治理辩论关键立场，Brown 的“周末迭代 15 版后被人工否定”为反例。
- **文献**：DSLXC-11485、DSLXC-11499、DSLXC-11508、DSLXC-11514（`ksummit.messages.10231`、`ksummit.messages.10301`、`ksummit.messages.10325`、`ksummit.messages.10342`，2025-10-08、2026-07-23、2026-07-17、2026-07-22），全文见 `raw_source.raw_json`

## 201.10 UMN造假事件

- **要点**：Al Viro反驳Hellwig为UMN研究者请功：对方既未公开原始数据也未公开实验协议，仅给聚合统计，论文问题远超伦理层面，无法检验提交与时间线。
- **史料**：`ksummit.messages.10245`（Al Viro，2021-04-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10245 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“对方既未公开原始数据也未公开实验协议，仅给聚合统计”这一实际状况为判据）；多方平等（总纲第 8 条——本体论上各方平等：为 UMN 研究者请功与无法检验提交与时间线两方并置）
- **辨析**：本块系 Al Viro 的反驳；“论文问题远超伦理层面”为其判断。
- **文献**：DSLXC-11486（`ksummit.messages.10245`，2021-04-22），全文见 `raw_source.raw_json`

## 201.11 设备直通争论

- **要点**：Leon Romanovsky称信任是双向的、单一维护者否决跨子系统设备功能不健康且不可能懂一切；Laurent Pinchart澄清所指的是对维护者与核心开发者集体判断的信任。
- **史料**：`ksummit.messages.10255`（Laurent Pinchart，2024-07-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10255 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：Leon 称单一维护者否决跨子系统设备功能不健康与 Pinchart 澄清所指为对集体判断的信任两方并置）；动手者叙事（总纲第 10 条——动手者创造历史：以“对维护者与核心开发者集体判断的信任”这一界定为分析单位）
- **辨析**：本块含 Leon Romanovsky 与 Laurent Pinchart 两方，署名为本封发件人 Laurent Pinchart。
- **文献**：DSLXC-11487（`ksummit.messages.10255`，2024-07-22），全文见 `raw_source.raw_json`

## 201.12 trivial补丁政策

- **要点**：Alexandre Belloni称Coverity会因他处检查返回值而制造无用检查、徒增内核膨胀，0day与coccinelle也引发大量无谓重构，不赞成为任何静态检查器官方背书。Thomas Gleixner回顾trivial树初衷是省维护者精力，自承已久未打理，断言“trivial该死”：连改typo也制造无谓冲突，支持从文档删除trivial@。
- **史料**：`ksummit.messages.10257`（Alexandre Belloni，2021-04-21）、`ksummit.messages.10356`（Thomas Gleixner，2021-04-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10257 -->` `<!-- ROW_MINE: ksummit.messages.10356 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：不赞成为任何静态检查器官方背书与“trivial 该死”两方并置）；经验优先（总纲第 9 条——经验优先：以“Coverity 会因他处检查返回值而制造无用检查、0day 与 coccinelle 引发大量无谓重构”这一实际见闻为判据）
- **辨析**：两条同属 trivial 补丁政策议题；Gleixner 的“自承已久未打理”与“连改 typo 也制造无谓冲突”为其亲历，支持从文档删除 trivial@。
- **文献**：DSLXC-11488、DSLXC-11518（`ksummit.messages.10257`、`ksummit.messages.10356`，2021-04-21、2021-04-22），全文见 `raw_source.raw_json`

## 201.13 AI版权争议

- **要点**：Steven Rostedt认为版权侵权与复制量有关（类比音乐采样），“Hello world”或不足受版权保护，并指出K&R书虽有保留所有权利条款却找不到授权读者使用示例。
- **史料**：`ksummit.messages.10260`（Steven Rostedt，2025-08-21）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10260 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“版权侵权与复制量有关（类比音乐采样）”“K&R 书虽有保留所有权利条款却找不到授权读者使用示例”这一实际观察为判据）；法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：版权保护边界与 AI 训练的争议）
- **辨析**：本块系 Steven Rostedt 的论证；“Hello world 或不足受版权保护”为其判断。
- **文献**：DSLXC-11489（`ksummit.messages.10260`，2025-08-21），全文见 `raw_source.raw_json`

## 201.14 linux-next测试

- **要点**：Mark Brown称scsi-fixes进linux-next偶能拦下跨架构构建破坏，pending-fixes源于修复曾依赖仅存在于-next的改动；其CI与KernelCI覆盖urgent分支还可减少bisect步数。
- **史料**：`ksummit.messages.10269`（Mark Brown，2024-10-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10269 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 scsi-fixes 进 linux-next、pending-fixes 分支、CI 与 KernelCI 覆盖 urgent 分支等具体机制为分析单位）；经验优先（总纲第 9 条——经验优先：以“偶能拦下跨架构构建破坏”“还可减少 bisect 步数”这一实际效果为判据）
- **辨析**：本块系 Mark Brown 的说明；“pending-fixes 源于修复曾依赖仅存在于 -next 的改动”为其机制归因。
- **文献**：DSLXC-11490（`ksummit.messages.10269`，2024-10-22），全文见 `raw_source.raw_json`

## 201.15 C结构体传参

- **要点**：Willy Tarreau用汇编实证x86-64与aarch64将双字结构体经寄存器对返回，而i386与32位ARM仍用隐藏指针写回，并给出宏打包为u64的等价方案，称32位不值得再优化。
- **史料**：`ksummit.messages.10270`（Willy Tarreau，2025-02-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10270 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“x86-64 与 aarch64 将双字结构体经寄存器对返回，而 i386 与 32 位 ARM 仍用隐藏指针写回”这一汇编实证为判据）；动手者叙事（总纲第 10 条——动手者创造历史：以给出宏打包为 u64 的等价方案这一具体手段为分析单位）
- **辨析**：本块系 Willy Tarreau 的实证；“32 位不值得再优化”为其结论。
- **文献**：DSLXC-11491（`ksummit.messages.10270`，2025-02-22），全文见 `raw_source.raw_json`

## 201.16 安全报告渠道

- **要点**：Jiri Kosina指出security@kernel.org与linux-distros@流程迥异，文档已劝阻向后者报内核漏洞（提交4fee0915e649b）；SUSE等依赖linux-distros建立CVE与修复对应，且不以stable为主基线。
- **史料**：`ksummit.messages.10272`（Jiri Kosina，2023-08-15）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10272 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“security@kernel.org 与 linux-distros@ 流程迥异”“SUSE 等依赖 linux-distros 建立 CVE 与修复对应”这一实际状况为判据）；法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：披露渠道与 CVE 归属的边界）
- **辨析**：本块系 Jiri Kosina 的说明；“文档已劝阻向后者报内核漏洞（提交 4fee0915e649b）”为可反查的具体依据。
- **文献**：DSLXC-11492（`ksummit.messages.10272`，2023-08-15），全文见 `raw_source.raw_json`

## 201.17 Rust安全问题

- **要点**：Geert Uytterhoeven追问Rust引用升级失败后调用方仍照常访问成员会发生什么；Miguel Ojeda说明升级可设计为可失败返回Option而非panic，折射2021年峰会对Rust运行期失败的疑虑。
- **史料**：`ksummit.messages.10284`（Geert Uytterhoeven，2021-07-08）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10284 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：Geert 追问引用升级失败后调用方仍照常访问成员与 Ojeda 的 Option 返回设计两方并置）；动手者叙事（总纲第 10 条——动手者创造历史：以“升级可设计为可失败返回 Option 而非 panic”这一具体机制为分析单位）
- **辨析**：本块含 Geert Uytterhoeven 的追问与 Miguel Ojeda 的作答两方，署名为本封发件人 Geert Uytterhoeven。
- **文献**：DSLXC-11494（`ksummit.messages.10284`，2021-07-08），全文见 `raw_source.raw_json`

## 201.18 内存模型语义

- **要点**：Kent Overstreet与Boqun Feng争论RELAXED原子是否隐含编译器屏障、非原子写会否提示编译器插入额外写；Boqun以smp_store_release发布示例说明并发读者可读到0或1。
- **史料**：`ksummit.messages.10289`（Kent Overstreet，2025-02-28）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10289 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“Boqun 以 smp_store_release 发布示例说明并发读者可读到 0 或 1”这一实际语义为判据）；多方平等（总纲第 8 条——本体论上各方平等：RELAXED 原子是否隐含编译器屏障两方争论并置）
- **辨析**：本块含 Kent Overstreet 与 Boqun Feng 两方，署名为本封发件人 Kent Overstreet；“非原子写会否提示编译器插入额外写”为其争论焦点。
- **文献**：DSLXC-11495（`ksummit.messages.10289`，2025-02-28），全文见 `raw_source.raw_json`

## 201.19 VLIW与OoO

- **要点**：H. Peter Anvin称VLIW与乱序执行同题竞争、是演进死路除非逐代JIT；Kent Overstreet主张开源逐代JIT可行且收益大，并追问Transmeta经验与指针别名问题的实测数据。
- **史料**：`ksummit.messages.10290`（Kent Overstreet，2025-02-23）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10290 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：Anvin 称 VLIW 是演进死路与 Overstreet 主张开源逐代 JIT 可行两方并置）；经验优先（总纲第 9 条——经验优先：以“除非逐代 JIT”这一前提条件与追问 Transmeta 经验与指针别名实测数据为判据）
- **辨析**：本块含 H. Peter Anvin 与 Kent Overstreet 两方，署名为本封发件人 Kent Overstreet；“追问 Transmeta 经验”表明其为实证取向的争论。
- **文献**：DSLXC-11496（`ksummit.messages.10290`，2025-02-23），全文见 `raw_source.raw_json`

## 201.20 字符串API迁移

- **要点**：Christoph Hellwig批评strscpy是无文档的助手、不如snprintf；Kees Cook指出strscpy有kern-doc并渲染于内核API文档页，其余strncpy场景应改用strtomem、kmemdup_nul、memcpy。
- **史料**：`ksummit.messages.10297`（Kees Cook，2023-10-20）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10297 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：Hellwig 批评 strscpy 无文档不如 snprintf 与 Cook 指出其有 kern-doc 并渲染于 API 文档页两方并置）；动手者叙事（总纲第 10 条——动手者创造历史：以“其余 strncpy 场景应改用 strtomem、kmemdup_nul、memcpy”这一具体迁移方案为分析单位）
- **辨析**：本块含 Christoph Hellwig 与 Kees Cook 两方，署名为本封发件人 Kees Cook。
- **文献**：DSLXC-11497（`ksummit.messages.10297`，2023-10-20），全文见 `raw_source.raw_json`

## 201.21 内核报错可读性

- **要点**：Artem Tashkinov列举固件缺失、省电未启用、硬件将坏等七类被含糊dmesg报错掩盖的真实问题，主张错误应可判断严重性与归属方，例如明确提示存储设备可能需返修。
- **史料**：`ksummit.messages.10298`（Artem S. Tashkinov，2022-10-02）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10298 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“固件缺失、省电未启用、硬件将坏等七类被含糊 dmesg 报错掩盖的真实问题”这一实际清单为判据）；动手者叙事（总纲第 10 条——动手者创造历史：以“错误应可判断严重性与归属方”这一具体要求为分析单位）
- **辨析**：本块系 Artem Tashkinov 的列举；“明确提示存储设备可能需返修”为其举例。
- **文献**：DSLXC-11498（`ksummit.messages.10298`，2022-10-02），全文见 `raw_source.raw_json`

## 201.22 ISP驱动之争

- **要点**：Ricardo Ribalda与Laurent Pinchart激辩ISP入DRM或V4L2：Ricardo称现行路线致99%相机市场依赖树外驱动，举Synopsys可编程ISP为例；Laurent坚持开放用户态要求并质疑命令缓冲论。
- **史料**：`ksummit.messages.10303`（Ricardo Ribalda Delgado，2024-07-29）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10303 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：Ribalda 称现行路线致 99% 相机市场依赖树外驱动与 Pinchart 坚持开放用户态要求两方并置）；动手者叙事（总纲第 10 条——动手者创造历史：以举 Synopsys 可编程 ISP 为例、质疑命令缓冲论等具体论据为分析单位）
- **辨析**：本块含 Ricardo Ribalda 与 Laurent Pinchart 的激辩两方，署名为本封发件人 Ricardo Ribalda Delgado；“99% 相机市场”为其论据。
- **文献**：DSLXC-11500（`ksummit.messages.10303`，2024-07-29），全文见 `raw_source.raw_json`

## 201.23 AI补丁法律风险

- **要点**：Steven Rostedt引DCO条款论证加SoB即代表“知情”：若AI引入不可提交的代码即违反(a)(b)并自负法律责任，不了解来源就不应提交，回应AI标签或在审诉讼中不利之忧。
- **史料**：`ksummit.messages.10305`（Steven Rostedt，2025-08-12）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10305 -->`
- **史观**：法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：加 SoB 即代表“知情”，若 AI 引入不可提交的代码即违反 DCO (a)(b) 并自负法律责任）；经验优先（总纲第 9 条——经验优先：以“不了解来源就不应提交”这一实际守则为判据）
- **辨析**：本块系 Steven Rostedt 的论证；“回应 AI 标签或在审诉讼中不利之忧”为对话记录。
- **文献**：DSLXC-11501（`ksummit.messages.10305`，2025-08-12），全文见 `raw_source.raw_json`

## 201.24 kerneldoc检查工具

- **要点**：Randy Dunlap发布自研Perl脚本kerndoc-export-search.pl v0.9，可同时查出缺kernel-doc与缺EXPORT符号，实测audit.c报3处缺文档、12处缺导出，欢迎并入kdoc Python系统。
- **史料**：`ksummit.messages.10307`（Randy Dunlap，2025-09-01）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10307 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以自研 Perl 脚本 kerndoc-export-search.pl v0.9 可同时查出缺 kernel-doc 与缺 EXPORT 符号这一具体工具为分析单位）；经验优先（总纲第 9 条——经验优先：以实测 audit.c 报 3 处缺文档、12 处缺导出这一结果为判据）
- **辨析**：本块系 Randy Dunlap 的工具发布；“欢迎并入 kdoc Python 系统”为其开放姿态。
- **文献**：DSLXC-11502（`ksummit.messages.10307`，2025-09-01），全文见 `raw_source.raw_json`

## 201.25 Rust内核panic

- **要点**：Miguel Ojeda指出内核Rust panic不展开栈；James Bottomley认为回溯是诊断用户bug报告的关键能力，担忧其缺失影响排障，追问是否有人在解决。
- **史料**：`ksummit.messages.10318`（James Bottomley，2025-02-26）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10318 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：Ojeda 指出内核 Rust panic 不展开栈与 Bottomley 认为回溯是诊断关键能力两方并置）；动手者叙事（总纲第 10 条——动手者创造历史：以“回溯缺失影响排障”这一具体能力缺口为分析单位）
- **辨析**：本块含 Miguel Ojeda 与 James Bottomley 两方，署名为本封发件人 James Bottomley；“追问是否有人在解决”为其诉求。
- **文献**：DSLXC-11505（`ksummit.messages.10318`，2025-02-26），全文见 `raw_source.raw_json`

## 201.26 Rust与stable

- **要点**：Miguel Ojeda回应Sasha Levin对-stable侧Rust审查人力匮乏之忧：寄望Rust知识随时间普及，复杂补丁可交抽象层维护者复审，与复杂C变更面临的困境同理。
- **史料**：`ksummit.messages.10319`（Miguel Ojeda，2021-07-06）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10319 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：Levin 对 -stable 侧 Rust 审查人力匮乏之忧与 Ojeda 的两条应对并置）；动手者叙事（总纲第 10 条——动手者创造历史：以“复杂补丁可交抽象层维护者复审”这一具体分工为分析单位）
- **辨析**：本块系 Miguel Ojeda 的回应；“与复杂 C 变更面临的困境同理”为其类比。
- **文献**：DSLXC-11506（`ksummit.messages.10319`，2021-07-06），全文见 `raw_source.raw_json`

## 201.27 Rust别名规则

- **要点**：Ventura Jack质疑“&UnsafeCell<T>等价C的T*”的说法，主张Rust引用仍受别名规则约束；Benno Lossin说明Opaque靠官方“hack”禁用&mut唯一性，树内pinned-init未用nightly特性。
- **史料**：`ksummit.messages.10322`（Ventura Jack，2025-02-24）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10322 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：Ventura Jack 质疑“&UnsafeCell<T> 等价 C 的 T*”与 Benno Lossin 说明 Opaque 靠官方 hack 禁用 &mut 唯一性两方并置）；动手者叙事（总纲第 10 条——动手者创造历史：以“树内 pinned-init 未用 nightly 特性”这一具体实现为分析单位）
- **辨析**：本块含 Ventura Jack 与 Benno Lossin 两方，署名为本封发件人 Ventura Jack。
- **文献**：DSLXC-11507（`ksummit.messages.10322`，2025-02-24），全文见 `raw_source.raw_json`

## 201.28 设备树绑定政策

- **要点**：Arınç ÜNAL主张DT绑定与源文件维护独立于内核开发，维护者不得以先修内核为接受DT补丁的条件；Conor Dooley称老平台文本绑定常以DTS与内核为准、长期错误需内核兼容。
- **史料**：`ksummit.messages.10330`（Arınç ÜNAL，2024-09-13）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10330 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：ÜNAL 主张 DT 绑定维护独立于内核开发与 Dooley 称老平台文本绑定常以 DTS 与内核为准两方并置）；动手者叙事（总纲第 10 条——动手者创造历史：以“维护者不得以先修内核为接受 DT 补丁的条件”这一具体规则为分析单位）
- **辨析**：本块含 Arınç ÜNAL 与 Conor Dooley 两方，署名为本封发件人 Arınç ÜNAL。
- **文献**：DSLXC-11509（`ksummit.messages.10330`，2024-09-13），全文见 `raw_source.raw_json`

## 201.29 Smatch资金困境

- **要点**：Dan Carpenter自述Smatch筹资失败，感谢grsecurity的Spengler资助意向；零日机器人无跨函数分析且只跑低误报检查，正漏掉缓冲溢出、差一错误与fork缺错误码等，寻求多家公司分摊薪资。
- **史料**：`ksummit.messages.10333`（Dan Carpenter，2026-02-06）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10333 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“零日机器人无跨函数分析且只跑低误报检查，正漏掉缓冲溢出、差一错误与 fork 缺错误码”这一实际能力缺口为判据）；动手者叙事（总纲第 10 条——动手者创造历史：以“寻求多家公司分摊薪资”这一具体筹资方案为分析单位）
- **辨析**：本块系 Dan Carpenter 的自述；“感谢 grsecurity 的 Spengler 资助意向”为可核的资助线索。
- **文献**：DSLXC-11510（`ksummit.messages.10333`，2026-02-06），全文见 `raw_source.raw_json`

## 201.30 补丁投递工具

- **要点**：Mauro Carvalho Chehab演示send-patches.pl整合format-patch、send-email与get_maintainer，封面信Cc逾80会被反垃圾拦截；Joe Perches用512字符阈值决定只Cc邮件列表。
- **史料**：`ksummit.messages.10336`（Mauro Carvalho Chehab，2021-04-23）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10336 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 send-patches.pl 整合 format-patch、send-email 与 get_maintainer 这一具体工具为分析单位）；经验优先（总纲第 9 条——经验优先：以“封面信 Cc 逾 80 会被反垃圾拦截”“用 512 字符阈值决定只 Cc 邮件列表”这一实际约束为判据）
- **辨析**：本块含 Mauro Carvalho Chehab 与 Joe Perches 两方，署名为本封发件人 Mauro Carvalho Chehab。
- **文献**：DSLXC-11511（`ksummit.messages.10336`，2021-04-23），全文见 `raw_source.raw_json`

## 201.31 补丁CC礼节

- **要点**：Mike Rapoport称最烦收到系列中间几片，至少应给所有收件人发封面信以便了解全局并请求重发；回应Leon对精选收件人导致反馈孤岛化的批评。
- **史料**：`ksummit.messages.10347`（Mike Rapoport，2021-04-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10347 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：Rapoport 称最烦收到系列中间几片与 Leon 批评精选收件人导致反馈孤岛化两方并置）；动手者叙事（总纲第 10 条——动手者创造历史：以“至少应给所有收件人发封面信”这一具体诉求为分析单位）
- **辨析**：本块系 Mike Rapoport 的回应；“回应 Leon 的批评”表明为对话记录。
- **文献**：DSLXC-11515（`ksummit.messages.10347`，2021-04-22），全文见 `raw_source.raw_json`

## 201.32 用户态要求

- **要点**：Laurent Pinchart以三年libcamera经验自省：按设计思路写的测试程序难发现API设计缺陷，主张加速器驱动须有完全开放的用户态实现，因其80%以上驱动逻辑本就在用户态。
- **史料**：`ksummit.messages.10348`（Laurent Pinchart，2021-09-14）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10348 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“加速器驱动须有完全开放的用户态实现”这一具体要求及“80% 以上驱动逻辑本就在用户态”为分析单位）；经验优先（总纲第 9 条——经验优先：以三年 libcamera 经验自省“按设计思路写的测试程序难发现 API 设计缺陷”为判据）
- **辨析**：本块系 Laurent Pinchart 的自省；“因其 80% 以上驱动逻辑本就在用户态”为其论据。
- **文献**：DSLXC-11516（`ksummit.messages.10348`，2021-09-14），全文见 `raw_source.raw_json`

## 201.33 gccrs编译器

- **要点**：Philip Herron说明gccrs以rustc为模板、须遵循libcore的lang items等编译器假设，暂不接受opt-out别名补丁以免添乱；称获Open Source Security与Embecosm资助，各Rust编译器项目关系友好。
- **史料**：`ksummit.messages.10349`（Philip Herron，2025-02-24）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10349 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 gccrs 以 rustc 为模板、须遵循 libcore 的 lang items 等编译器假设这一具体工程约束为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：暂不接受 opt-out 别名补丁以免添乱与各 Rust 编译器项目关系友好并置）
- **辨析**：本块系 Philip Herron 的说明；“获 Open Source Security 与 Embecosm 资助”为可核事实。
- **文献**：DSLXC-11517（`ksummit.messages.10349`，2025-02-24），全文见 `raw_source.raw_json`

## 201.34 LKML流量改革

- **要点**：Tim Bird自述把LKML倒进Gmail、极少回应的用法，询问b4、lei、lore能否回复未订阅列表的邮件，回应Konstantin将MAINTAINERS“THE REST”改指patches@lists.linux.dev的提案。
- **史料**：`ksummit.messages.10379`（Bird, Tim，2023-11-08）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10379 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以其“把 LKML 倒进 Gmail、极少回应”这一实际用法为判据）；动手者叙事（总纲第 10 条——动手者创造历史：以“b4、lei、lore 能否回复未订阅列表的邮件”这一具体功能之问为分析单位）
- **辨析**：本块系 Tim Bird 的自述与询问；“回应 Konstantin 将 MAINTAINERS‘THE REST’改指 patches@lists.linux.dev 的提案”为对话背景。
- **文献**：DSLXC-11520（`ksummit.messages.10379`，2023-11-08），全文见 `raw_source.raw_json`

## 201.35 邮件引用治理

- **要点**：Andrew Morton提议写机器人对引用文本超95%的邮件发警告，称此现象因Gmail折叠引用而明显增多，并自嘲这办法不会讨人喜欢。
- **史料**：`ksummit.messages.10385`（Andrew Morton，2023-10-23）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10385 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“写机器人对引用文本超 95% 的邮件发警告”这一具体方案为分析单位）；经验优先（总纲第 9 条——经验优先：以“此现象因 Gmail 折叠引用而明显增多”这一实际观察为判据）
- **辨析**：本块系 Andrew Morton 的提议；“自嘲这办法不会讨人喜欢”为其修辞。
- **文献**：DSLXC-11521（`ksummit.messages.10385`，2023-10-23），全文见 `raw_source.raw_json`

## 201.36 维护者支持

- **要点**：Steven Rostedt披露TAB正起草“沟通风格”文档规范提交者与维护者互相对话方式，称维护者支持组构想已与同侪酝酿许久，主张本届峰会必须讨论此议题。
- **史料**：`ksummit.messages.10389`（Steven Rostedt，2023-09-19）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.10389 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 TAB 正起草“沟通风格”文档、维护者支持组构想等具体制度安排为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：规范提交者与维护者互相对话方式与“本届峰会必须讨论此议题”的诉求并置）
- **辨析**：本块系 Steven Rostedt 的披露；“已与同侪酝酿许久”为其沿革说明。
- **文献**：DSLXC-11522（`ksummit.messages.10389`，2023-09-19），全文见 `raw_source.raw_json`
