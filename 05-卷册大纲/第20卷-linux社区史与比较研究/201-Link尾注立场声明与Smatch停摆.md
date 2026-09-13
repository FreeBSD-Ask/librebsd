# 201. Linus Link 尾注立场声明、Smatch 停摆与可信 trivial tree 提案（ks p65）

> 来源：ksummit 独有 p65（50 封全读，2021-04 至 2026-07：Linus 关于 Link 尾注的长篇立场声明必须是公开真实链接拒内部 bug ID 与 syzbot 魔数宁 Link 不用 Closes 系理解内核提交元数据社会契约的一手文本；Dan Carpenter 自述 Smatch 静态分析因筹资失败停摆零日机器人只能做低误报检查而漏掉跨函数 bug 记录社区安全工具资金困境事件；Linus 提出 AI 审查下一步由可信团队运营 AI 建高置信 trivial tree 并明确信任的是运营者而非 AI 系 2026 年 AI 审查治理辩论关键立场；Ribalda 与 Pinchart 就 ISP 驱动入 DRM 还是 V4L2 激烈争论含 99% 相机市场依赖树外驱动论据；Link 尾注规范五封、AI 审查流程四封、Bugzilla 退役四封）
> 判定：46 CAND / 4 NV。主题分布：Bugzilla退役 3、Rust绑定自动化 1、AI内容规范 1、文件系统信任标志 1、静态分析注解 1、Bugzilla改革 1、Fixes标签政策 1、Link尾注规范 5、AI审查流程 4、UMN造假事件 1、设备直通争论 1、trivial补丁政策 2、AI版权争议 1、linux-next测试 1、C结构体传参 1、安全报告渠道 1、Rust安全问题 1、内存模型语义 1、VLIW与OoO 1、字符串API迁移 1、内核报错可读性 1、ISP驱动之争 1、AI补丁法律风险 1、kerneldoc检查工具 1、Rust内核panic 1、Rust与stable 1、Rust别名规则 1、设备树绑定政策 1、Smatch资金困境 1、补丁投递工具 1、补丁CC礼节 1、用户态要求 1、gccrs编译器 1、LKML流量改革 1、邮件引用治理 1、维护者支持 1。

## 201.1 Bugzilla退役

- 【Linux社区】Jani Nikula称GitLab免费版issue功能不及Bugzilla、好功能都进付费层，倾向社区驱动的Forgejo；Mario Limonciello建议自建gitlab.kernel.org按子系统建项目跟踪issue。 `<!-- ROW_MINE: ksummit.messages.10203 -->`
- 【Linux社区】Sasha Levin演示LLM把oops报告定位到xfrm_iptfs.c:905的skb_put并找出元凶提交5f2b6a9095743，提议bug@kernel.org机器人分诊；James Bottomley建议代理扫描全部列表、回复结果并标记回归。 `<!-- ROW_MINE: ksummit.messages.10275 -->`
- 【Linux社区】Jani Nikula指出MAINTAINERS已有B:字段记录bug提交URI（网页或mailto），支持Morton提议做网页前端：粘贴路径即返回维护者邮箱，补bugzilla退位后的报告入口。 `<!-- ROW_MINE: ksummit.messages.10340 -->`

## 201.2 Rust绑定自动化

- 【Linux社区】James Bottomley提议在C头文件加注解、由增强bindgen生成Rust绑定并配类sparse校验工具；强调目标非稳定C API，而是让API变更更易传导到Rust侧，Miguel Ojeda认同信息就地保存。 `<!-- ROW_MINE: ksummit.messages.10211 -->`

## 201.3 AI内容规范

- 【Linux社区】Michael Tsirkin赞成“提交者须能理解并自证一切工具生成内容”的守则适用于一切工具而非仅AI，称见过太多“修checkpatch警告”式垃圾补丁，AI生成并无本质不同。 `<!-- ROW_MINE: ksummit.messages.10212 -->`

## 201.4 文件系统信任标志

- 【Linux社区】Linus Torvalds同意对不可信文件系统做内核级标记，建议利用未被充分利用的/proc/filesystems或在挂载选项中加“提示”，按文件系统拒绝以不信任方式挂载介质，回应Hellwig。 `<!-- ROW_MINE: ksummit.messages.10219 -->`

## 201.5 静态分析注解

- 【Linux社区】Arnd Bergmann归纳指针返回值四类注解（有效指针与NULL/错误指针的组合），Geert Uytterhoeven补充*_optional类第五种；Arnd称optional函数应编译期二选一，返回NULL属接口bug。 `<!-- ROW_MINE: ksummit.messages.10225 -->`

## 201.6 Bugzilla改革

- 【Linux社区】Greg KH称LF内核实习生预算已全部用完、还有大量无薪实习生，无法资助bug分诊人力；Konstantin Ryabitsev强调此类工作需不可挪用的专项拨款。 `<!-- ROW_MINE: ksummit.messages.10226 -->`

## 201.7 Fixes标签政策

- 【Linux社区】James Bottomley主张Fixes:适用于任何改动先前提交之处（含空白与拼写），使回移无需辩论且易验证；cc:stable才用于回归等值得回移的修复，反驳Dan Carpenter“非回归不加Fixes”。 `<!-- ROW_MINE: ksummit.messages.10227 -->`

## 201.8 Link尾注规范

- 【Linux社区】Michael Tsirkin质疑Konstantin的Link尾注文档未讲清lore.kernel.org与patch.msgid.link两域名各用于何处，并抱怨git am需怪异脚本，无法再靠messageid=true自动生成链接。 `<!-- ROW_MINE: ksummit.messages.10228 -->`
- 【Linux社区】Linus Torvalds长文阐明Link:必须是公开可点的真实链接以杜绝内部bug ID，斥b4 am来源链接与syzbot魔数Reported-by为噪音，宁用Link不用Closes，自述常按作者加日期在lore挖多年前的讨论。 `<!-- ROW_MINE: ksummit.messages.10312 -->`
- 【Linux社区】James Bottomley澄清Link仅回链提交的原始邮件、工具只需最后一轮迭代即可用，Konstantin的b4 dig基于patch-id模糊匹配；否认需要Gerrit式Change-Id跨版本追踪提交。 `<!-- ROW_MINE: ksummit.messages.10314 -->`
- 【Linux社区】Jani Nikula以数据反驳Geert对patchwork.freedesktop.org链接的批评：指向该域的Link:标签逾99%的URL内含Message-ID，可直达原始邮件。 `<!-- ROW_MINE: ksummit.messages.10338 -->`
- 【Linux社区】Konstantin Ryabitsev指git notes单ref百万文件难扩展且多写者冲突，主张用public-inbox的RFC-2822消息流记录提交注解（X-For-Commit-ID头），把lore当作面向自动化代理的“消息总线”。 `<!-- ROW_MINE: ksummit.messages.10359 -->`

## 201.9 AI审查流程

- 【Linux社区】Sasha Levin援引其Assisted-by:（如Claude加checkpatch）披露提案，主张由各子系统自定政策并自动化工作流；Tim Bird建议用标签标注补丁经何种工具审查，缺标签可要求先补。 `<!-- ROW_MINE: ksummit.messages.10231 -->`
- 【Linux社区】Rodrigo Vivi赞同Guenter Roeck要求作者先处理Sashiko报出的9处问题再人工审，但Mark Brown举出周末迭代15版后被人工否定的反例；Rodrigo援引Sage“想法-架构-打磨”三层审查框架寻折中。 `<!-- ROW_MINE: ksummit.messages.10301 -->`
- 【Linux社区】Linus Torvalds指“顺手修预存问题”的摩擦早于AI、建数据库难解压力与摩擦，提议由可信团队运营的AI建“trivial tree”承接高置信修复，强调信任的是运营者而非AI本身。 `<!-- ROW_MINE: ksummit.messages.10325 -->`
- 【Linux社区】Johannes Berg主张Sashiko默认纳入、可事后退出，以免未发声者漏报而被利用，Rostedt附和宁愿多收报告；Bottomley称AI驱动补丁者借提示滥发“恶意硬件修复”，欲从源头退出。 `<!-- ROW_MINE: ksummit.messages.10342 -->`

## 201.10 UMN造假事件

- 【Linux社区】Al Viro反驳Hellwig为UMN研究者请功：对方既未公开原始数据也未公开实验协议，仅给聚合统计，论文问题远超伦理层面，无法检验提交与时间线。 `<!-- ROW_MINE: ksummit.messages.10245 -->`

## 201.11 设备直通争论

- 【Linux社区】Leon Romanovsky称信任是双向的、单一维护者否决跨子系统设备功能不健康且不可能懂一切；Laurent Pinchart澄清所指的是对维护者与核心开发者集体判断的信任。 `<!-- ROW_MINE: ksummit.messages.10255 -->`

## 201.12 trivial补丁政策

- 【Linux社区】Alexandre Belloni称Coverity会因他处检查返回值而制造无用检查、徒增内核膨胀，0day与coccinelle也引发大量无谓重构，不赞成为任何静态检查器官方背书。 `<!-- ROW_MINE: ksummit.messages.10257 -->`
- 【Linux社区】Thomas Gleixner回顾trivial树初衷是省维护者精力，自承已久未打理，断言“trivial该死”：连改typo也制造无谓冲突，支持从文档删除trivial@。 `<!-- ROW_MINE: ksummit.messages.10356 -->`

## 201.13 AI版权争议

- 【Linux社区】Steven Rostedt认为版权侵权与复制量有关（类比音乐采样），“Hello world”或不足受版权保护，并指出K&R书虽有保留所有权利条款却找不到授权读者使用示例。 `<!-- ROW_MINE: ksummit.messages.10260 -->`

## 201.14 linux-next测试

- 【Linux社区】Mark Brown称scsi-fixes进linux-next偶能拦下跨架构构建破坏，pending-fixes源于修复曾依赖仅存在于-next的改动；其CI与KernelCI覆盖urgent分支还可减少bisect步数。 `<!-- ROW_MINE: ksummit.messages.10269 -->`

## 201.15 C结构体传参

- 【Linux社区】Willy Tarreau用汇编实证x86-64与aarch64将双字结构体经寄存器对返回，而i386与32位ARM仍用隐藏指针写回，并给出宏打包为u64的等价方案，称32位不值得再优化。 `<!-- ROW_MINE: ksummit.messages.10270 -->`

## 201.16 安全报告渠道

- 【Linux社区】Jiri Kosina指出security@kernel.org与linux-distros@流程迥异，文档已劝阻向后者报内核漏洞（提交4fee0915e649b）；SUSE等依赖linux-distros建立CVE与修复对应，且不以stable为主基线。 `<!-- ROW_MINE: ksummit.messages.10272 -->`

## 201.17 Rust安全问题

- 【Linux社区】Geert Uytterhoeven追问Rust引用升级失败后调用方仍照常访问成员会发生什么；Miguel Ojeda说明升级可设计为可失败返回Option而非panic，折射2021年峰会对Rust运行期失败的疑虑。 `<!-- ROW_MINE: ksummit.messages.10284 -->`

## 201.18 内存模型语义

- 【Linux社区】Kent Overstreet与Boqun Feng争论RELAXED原子是否隐含编译器屏障、非原子写会否提示编译器插入额外写；Boqun以smp_store_release发布示例说明并发读者可读到0或1。 `<!-- ROW_MINE: ksummit.messages.10289 -->`

## 201.19 VLIW与OoO

- 【Linux社区】H. Peter Anvin称VLIW与乱序执行同题竞争、是演进死路除非逐代JIT；Kent Overstreet主张开源逐代JIT可行且收益大，并追问Transmeta经验与指针别名问题的实测数据。 `<!-- ROW_MINE: ksummit.messages.10290 -->`

## 201.20 字符串API迁移

- 【Linux社区】Christoph Hellwig批评strscpy是无文档的助手、不如snprintf；Kees Cook指出strscpy有kern-doc并渲染于内核API文档页，其余strncpy场景应改用strtomem、kmemdup_nul、memcpy。 `<!-- ROW_MINE: ksummit.messages.10297 -->`

## 201.21 内核报错可读性

- 【Linux社区】Artem Tashkinov列举固件缺失、省电未启用、硬件将坏等七类被含糊dmesg报错掩盖的真实问题，主张错误应可判断严重性与归属方，例如明确提示存储设备可能需返修。 `<!-- ROW_MINE: ksummit.messages.10298 -->`

## 201.22 ISP驱动之争

- 【Linux社区】Ricardo Ribalda与Laurent Pinchart激辩ISP入DRM或V4L2：Ricardo称现行路线致99%相机市场依赖树外驱动，举Synopsys可编程ISP为例；Laurent坚持开放用户态要求并质疑命令缓冲论。 `<!-- ROW_MINE: ksummit.messages.10303 -->`

## 201.23 AI补丁法律风险

- 【Linux社区】Steven Rostedt引DCO条款论证加SoB即代表“知情”：若AI引入不可提交的代码即违反(a)(b)并自负法律责任，不了解来源就不应提交，回应AI标签或在审诉讼中不利之忧。 `<!-- ROW_MINE: ksummit.messages.10305 -->`

## 201.24 kerneldoc检查工具

- 【Linux社区】Randy Dunlap发布自研Perl脚本kerndoc-export-search.pl v0.9，可同时查出缺kernel-doc与缺EXPORT符号，实测audit.c报3处缺文档、12处缺导出，欢迎并入kdoc Python系统。 `<!-- ROW_MINE: ksummit.messages.10307 -->`

## 201.25 Rust内核panic

- 【Linux社区】Miguel Ojeda指出内核Rust panic不展开栈；James Bottomley认为回溯是诊断用户bug报告的关键能力，担忧其缺失影响排障，追问是否有人在解决。 `<!-- ROW_MINE: ksummit.messages.10318 -->`

## 201.26 Rust与stable

- 【Linux社区】Miguel Ojeda回应Sasha Levin对-stable侧Rust审查人力匮乏之忧：寄望Rust知识随时间普及，复杂补丁可交抽象层维护者复审，与复杂C变更面临的困境同理。 `<!-- ROW_MINE: ksummit.messages.10319 -->`

## 201.27 Rust别名规则

- 【Linux社区】Ventura Jack质疑“&UnsafeCell<T>等价C的T*”的说法，主张Rust引用仍受别名规则约束；Benno Lossin说明Opaque靠官方“hack”禁用&mut唯一性，树内pinned-init未用nightly特性。 `<!-- ROW_MINE: ksummit.messages.10322 -->`

## 201.28 设备树绑定政策

- 【Linux社区】Arınç ÜNAL主张DT绑定与源文件维护独立于内核开发，维护者不得以先修内核为接受DT补丁的条件；Conor Dooley称老平台文本绑定常以DTS与内核为准、长期错误需内核兼容。 `<!-- ROW_MINE: ksummit.messages.10330 -->`

## 201.29 Smatch资金困境

- 【Linux社区】Dan Carpenter自述Smatch筹资失败，感谢grsecurity的Spengler资助意向；零日机器人无跨函数分析且只跑低误报检查，正漏掉缓冲溢出、差一错误与fork缺错误码等，寻求多家公司分摊薪资。 `<!-- ROW_MINE: ksummit.messages.10333 -->`

## 201.30 补丁投递工具

- 【Linux社区】Mauro Carvalho Chehab演示send-patches.pl整合format-patch、send-email与get_maintainer，封面信Cc逾80会被反垃圾拦截；Joe Perches用512字符阈值决定只Cc邮件列表。 `<!-- ROW_MINE: ksummit.messages.10336 -->`

## 201.31 补丁CC礼节

- 【Linux社区】Mike Rapoport称最烦收到系列中间几片，至少应给所有收件人发封面信以便了解全局并请求重发；回应Leon对精选收件人导致反馈孤岛化的批评。 `<!-- ROW_MINE: ksummit.messages.10347 -->`

## 201.32 用户态要求

- 【Linux社区】Laurent Pinchart以三年libcamera经验自省：按设计思路写的测试程序难发现API设计缺陷，主张加速器驱动须有完全开放的用户态实现，因其80%以上驱动逻辑本就在用户态。 `<!-- ROW_MINE: ksummit.messages.10348 -->`

## 201.33 gccrs编译器

- 【Linux社区】Philip Herron说明gccrs以rustc为模板、须遵循libcore的lang items等编译器假设，暂不接受opt-out别名补丁以免添乱；称获Open Source Security与Embecosm资助，各Rust编译器项目关系友好。 `<!-- ROW_MINE: ksummit.messages.10349 -->`

## 201.34 LKML流量改革

- 【Linux社区】Tim Bird自述把LKML倒进Gmail、极少回应的用法，询问b4、lei、lore能否回复未订阅列表的邮件，回应Konstantin将MAINTAINERS“THE REST”改指patches@lists.linux.dev的提案。 `<!-- ROW_MINE: ksummit.messages.10379 -->`

## 201.35 邮件引用治理

- 【Linux社区】Andrew Morton提议写机器人对引用文本超95%的邮件发警告，称此现象因Gmail折叠引用而明显增多，并自嘲这办法不会讨人喜欢。 `<!-- ROW_MINE: ksummit.messages.10385 -->`

## 201.36 维护者支持

- 【Linux社区】Steven Rostedt披露TAB正起草“沟通风格”文档规范提交者与维护者互相对话方式，称维护者支持组构想已与同侪酝酿许久，主张本届峰会必须讨论此议题。 `<!-- ROW_MINE: ksummit.messages.10389 -->`
