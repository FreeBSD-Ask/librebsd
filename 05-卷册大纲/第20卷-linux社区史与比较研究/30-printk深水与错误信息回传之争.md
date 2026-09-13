# 30-printk深水与错误信息回传之争.md

> 对应页面：ksummit-discuss p82（pk 348306-348355，2017-07-06/08 多线程并进 + 2014 档案信）
> 判定：50 CAND / 0 NV
> 编号：DSLXC-5132..5181 | claim 已入库（50/50，dslinux_claims.duckdb）

## 30.1 【Linux社区】printk 重设计深水：panic 卸载禁区与 fbdev 归属（5 例）

**要点（判定表逐字）**：Daniel Vetter评printk重设计TODO清单，建议将fbdev讨论从console_sem章移至fbdev/tty/drm章，并提每控制台标志需求——即便oops/panic也要kthread卸载，kms明确需要此能力，愿协助实现；David Woodhouse指printk被异步化后不再可靠、崩溃临终信息在串口不可见，主张printk回归调试诊断本源，并吁从整体审视printk该与不该用于何事；David Woodhouse续论数据中心仍有串口（RJ-45走Yost或Cisco针序、serial-over-TCP），乃至USB debug口，printk应守调试诊断本职而非向用户态滥传数据，赞同Steven所言printk被用得太随意；Sergey Senozhatsky答Daniel，panic时kthread卸载风险极高（或陷NMI、其余CPU已停），故panic禁用offloading，并欲先令call_console_drivers更可靠再谈卸载；Sergey Senozhatsky列printk三大症结——需卸载、易死锁（故有printk_deferred）、NMI不可全靠，且call_console_drivers把控制权交外部世界；举printk活锁致Tetsuo只能sysrq-c、OOM打印延迟近分钟等实例

**史料**：`348306、`348307、`348308、`348310、`348311

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348306 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348307 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348308 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348310 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348311 -->` 

## 30.2 【Linux社区】向用户态回传错误信息与 ABI 门控（18 例）

**要点（判定表逐字）**：Steven Rostedt回应Linus关于向用户态回报错误信息的消极判断，指大量-E错误并不进用户态，缺良构基础设施，tracing有回传细粒度错误之法但属特例，泛化需双向易用且要先规划；David Howells就回报错误给用户态，示意在fd仲裁挂载（fsopen/fsmount）中读回挂载错误/警告/信息，并附示例代码从fs_fd读取消息；Miklos Szeredi反驳Linus，指不必每条错误都做、内核本就在dmesg打详细信息为何不绑定触发错误的syscall、i18n应在内核之外解决，并建议极简接口return detailed_error(-EINVAL, ...)；David Howells应Miklos，建议在错误字符串前加源标签如nfs、vfs、dvb-core以区分归属；Andy Lutomirski提ABI特性门控之议，指新ABI成稳机制薄弱（六步模型：写码、审码、维护者合、Linus难审ABI、-rc1落地、发版前修），拟大特性藏具名门控（终版内核须手补方能开），并举RDMA套接字类型、O_TMPFILE、cgroup+bpf为例；Greg KH问Rust之策，赞手补补丁之想，但质疑谁来为测试打补丁、门控须等多久方解，并称此议题反复出现愈难解；Theodore Ts'o认问题真实，但门控对O_TMPFILE类标志或RDMA类新套接字须改码（CONFIG_* ifdef），不抄linux-api者难期其建门控；门控反令试用者更少，提议半自动监视linux-next的include/uapi/*.h变更、人判新旧API，对ML方案存疑；Stephen Rothwell列linux-next实际uapi变更清单（membarrier、drm/msm、userfaultfd、nf_tables、bpf、xdp等数十项），问是否每改uapi皆需文档与man页、能否先设计后实现，并叹sysfs与tracing之乱；Andy Lutomirski答Greg，Rust具具名不稳定特性，须以注解声明且仅nightly构建可用、stable拒编请求不稳定特性；Sergey Senozhatsky为Greg释Rust标法，举「#[stable(feature=rust1)]」与「#[unstable(feature=sip_hash_13)]」等注解实例；Julia Lawall应Stephen，曾做语义补丁收集系统类返回错误码，因常见以引用参数回错、文档不精而受阻，拟觅实习生补规则并随时候查变更；Daniel Vetter应ABI门控，称gpu驱动真实解法是抬高门槛——内核补丁全审、全内档、测试用例、整套用户态栈落地（非厂商fork、常改3+项目）、用户态测试与互审、uapi真文档、全CI；每条规矩皆因至少一次悔憾，故入linux-next即发鲜有追悔；Jiri Kosina应Ted，半自动系统仅及uapi，sysfs难定路径模式监视；Hannes Reinecke应Jiri，sysfs虽算kABI却无跟踪之法、只能靠侧置文档且盼人不漏，又及内部符号之争（导出符号本应仅驱动内见）致大量误报；Julia Lawall应Jiri，称Michael Kerrisk在此向有一大堆正则；Michael Kerrisk认其清单不大且手工维护，但助其捕捉本将错过的需入man页之新特性；Theodore Ts'o应Julia，将新错误返回也算ABI变更不切实际（加ENOMEM免oops无需上linux-api争论），忆某高管因非POSIX所列errno而愠，称人更忧新syscall或新标志（如O_TMPFILE），须择可驯子集而战；Julia Lawall应Ted，新syscall可借SYSCALL_DEFINE1等识别，新标志或为加进uapi头、用法类同已文档标志之#define，可作辅助判定

**史料**：`348309、`348313、`348319、`348320、`348341、`348342、`348343、`348344、`348346、`348347、`348348、`348349、`348350、`348351、`348352、`348353、`348354、`348355

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348309 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348313 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348319 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348320 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348341 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348342 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348343 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348344 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348346 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348347 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348348 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348349 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348350 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348351 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348352 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348353 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348354 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348355 -->` 

## 30.3 【Linux社区】tracing 微会、Plumbers 与 ABI 讨论（7 例）

**要点（判定表逐字）**：Mathieu Desnoyers因内核峰会与Plumbers难兼顾tracing终端用户与开发者，将Tracing Summit改为半日演讲半日讨论（Steven主持），定10月27日布拉格峰会后周五，发布CFP；James Bottomley以Plumbers程序委员身份反驳tracing不宜该会之说，称Plumbers本就汇聚终端用户；并称Tracing微会重获兴趣、大概率落地，两活动因大陆分处可并存；Steven Rostedt应Josef Bacik，允将其在wiki补记微会讨论ABI，并指Facebook生产环境遍用tracing，Josef可兼用户与维护者视角讲述；Steven Rostedt告Mathieu：Brendan Gregg已凑足提案，今年Plumbers将设tracing微会；Josef Bacik问微会是否谈ABI，自陈Facebook生产遍用tracing，可从用户与维护者双视角发言；Mathieu Desnoyers收回此前不赴Plumbers之言，因工作许可延迟装修，大概率终能出席LPC；Steven Rostedt见Mathieu已更新wiki标出席，附wiki.linuxplumbersconf.org/2017:tracing并盼相见

**史料**：`348314、`348315、`348316、`348317、`348318、`348321、`348322

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348314 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348315 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348316 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348317 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348318 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348321 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348322 -->` 

## 30.4 【Linux社区】kselftest 易用性与 O= 分离构建之争（15 例）

**要点（判定表逐字）**：Eric W. Biederman指kselftest难构建难运行，曾耗时一周才摸清组合使其可跑，未易用前不宜强推；Steven Rostedt答Eric：那或许该着力令kselftest更易运行；Eric W. Biederman仅回一词Please，认同应先令kselftest更易运行之方向；Shuah Khan答回归追踪线程，称「make kselftest」即跑全测、亦可单跑，当前痛点在于各测试输出格式不一难解析，正推进转TAP13格式；Eric W. Biederman覆Shuah，4.13-rc1下「make O=... kselftests」报无此目标，质疑何须怪异命令而非传统make路径式单测；Shuah Khan纠正Eric拼写应为「make kselftest」，并示「make -C tools/testing/selftests/ run_tests」等单跑法；Eric W. Biederman再覆，即便加O=保源码纯净仍失败、需make mrproper复原，且mpx-mini-test.c与protection_keys.c根本构建不出；Randy Dunlap附和，约半年前已报O=builddir被忽略之弊，亦无法构建mpx-mini-test；Shuah Khan答Eric，称多法可跑、愿加该用例，并询其何需make mrproper后流程方复常；Theodore Ts'o释O=分离目标目录之法（源码置SSD、构建置HDD、多配置并行），说明源码树内构建会令make O=抱怨不净需mrproper，自陈以xfstests/gce-xfstests测试、无意迁就kselftest，并警以让你发补丁未必奏效；Shuah Khan指Documentation/dev-tools/kselftest.rst已列详尽用例；Tim Bird言其嵌入式构建亦用「make O=xxx」（KBUILD_OUTPUT），本在待办欲加支持，既知阻塞他人愿提优先级、数月内尝试；Shuah Khan谢Ted详解，称既理解工作流将着手，估或不难支持；Shuah Khan谢Tim相助之意，称KBUILD_OUTPUT已有部分工作，将查能否覆盖此用例；Theodore Ts'o再答Shuah，澄清非指其 hostile，分目录只为免每次换配置重写约2GB目标文件，违背此工作流即不友好，故无意试用

**史料**：`348324、`348325、`348326、`348328、`348329、`348330、`348331、`348332、`348333、`348335、`348336、`348337、`348338、`348339、`348340

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348324 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348325 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348326 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348328 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348329 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348330 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348331 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348332 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348333 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348335 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348336 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348337 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348338 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348339 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348340 -->` 

## 30.5 【Linux社区】Devicetree 迷你会与 2014 档案五封（5 例）

**要点（判定表逐字）**：Grant Likely迟到的半日Devicetree工具与校验迷你会提案，因关键参与者赴布拉格ELCE而非洛杉矶Plumbers，遂改请于内核峰会期间办，并指wiki召集具体议题；Arnd Bergmann论ACPI/DT——powernv的rtas虽在defconfig禁用仍支持、powermac等已死；SFI曾尝试嵌入式ACPI却被弃；不主张新架构引入ACPI，ARM64若上ACPI亦不愿出现两套不兼容实现，AMD嵌入式ARM64应取DT或复用服务器固件；Takashi Iwai提git提交元数据增补之想——为每提交嵌追随后设信息（所致回归、后续修复提交、bugzilla或邮件列表链接），回归标记尤助规避二分法陷阱，拟以git-notes式入已发布树；Takashi Iwai提子系统维护者指引之题（谓之健康社区育儿手册），察各子系统回应参差，问是否需基线指引以吸引 casual 开发者，或只是 bikeshedding；Shuah Khan就PM依赖之2014旧题，问能否借pm domains概念解松散关联设备，称曾以此探媒体设备PM但未及实验

**史料**：`348327、`348312、`348323、`348334、`348345

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348327 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348312 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348323 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348334 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348345 -->` 

---
注：本文件由判定表程序化生成（5 块，覆盖 50/50 CAND，两遍计数核对通过）；要点逐字取自判定表「要点」列（主代理全读审读实录），史料锚与 CAND 一一对应，全文以 raw_source.raw_json 为准。
