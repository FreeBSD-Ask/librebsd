# 10 【Linux社区】printk重设计深度讨论与反馈机制新线程

> 对应页面：ksummit-discuss p75（pk 347956-348005，2017-06-20 至 2017-06-25）
> 判定：50 CAND / 0 NV
> 编号：DSLXC-4178..4227 | claim 已入库（50/50，dslinux_claims.duckdb）

## 10.1 【Linux社区】printk 需求分层与缓冲模型之争

**要点**：Sergey：认同 Rostedt 需求梳理，但“get out immediately”部分很复杂——有人爱（从未杀机）、有人恨（杀机过）；“the winner prints it all”设计有时有问题；“messages are not created equal”；Sergey：支持 Mark Brown 的观察——PRINTK_TIME 是 config 且非 100% 可靠（同时间戳多打印）；时间戳本就不同 CPU 间不完全同步；Sergey：回应 Hannes 的 SCSI 自建日志（dev_printk 等）移除愿想——已有 buffered printk 需求（Tetsuo 要 OOM backtraces 少断行）；可复用 printk_safe 的 per-CPU 缓冲；buffered_printk_begin/end 概略（local IRQ disable + 拷贝到 logbuf）可行；Tony Luck：printk 深层才取 local_clock()——更早抓取更接近调用时点；乱序可接受，时间真实性优先；Sergey：确认时间戳取自“最终入 logbuf”而非调用时点；printk 不排序 logbuf；printk_safe/printk_nmi 从 irq work 刷新必乱序；CPU 号指示有帮助；Mark Brown：加 CPU 号=重造 ftrace；join 有难度但可学；Vetter（drm 侧）：console_lock 恐怖秀——重 printk 使其重竞争（kms resume 已躲 worker）；console_lock 大块头使 gfx init 数百 K 行代码在锁内无输出；与 Alan Cox 修几次都泪奔；kerneldoc 页+debug hacks 是新 gfx 工程师陷阱；Rostedt：printk 仿 ftrace——per-CPU 无锁缓冲（立即写、延迟出）；两 console 接口（normal/critical）；唤醒线程读缓冲；critical 时关闭 normal 直接接管刷屏；全 critical 命令行（Peter Zijlstra 已有 patch 转 early printk）

**史料**：`347956`、`347958`、`347959`、`347960`、`347961`、`347962`、`347963`、`347964`

**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347956 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347958 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347959 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347960 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347961 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347962 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347963 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347964 -->`
**史观**：多方平等（总纲 8：Sergey、Tony Luck、Mark Brown、Vetter、Rostedt 五方对缓冲模型的分歧并置）；经验优先（总纲 9：以 printk_safe/printk_nmi 的 per-CPU 缓冲、gfx init 数百 K 行代码在锁内无输出等实况为据）；动手者叙事（总纲 10：console_lock“恐怖秀”由 drm 侧 Vetter 自陈）
**辨析**：Mark Brown 以“加 CPU 号=重造 ftrace”质疑 Sergey，提示该方向与 ftrace 既有设施重叠；Rostedt 的 per-CPU 无锁缓冲系其 ftrace 经验迁移，非社区既有共识。
**文献**：DSLXC-4178/4180/4181/4182/4183/4184/4185/4186（`ksummit-discuss.messages.347956`、`.347958`、`.347959`、`.347960`、`.347961`、`.347962`、`.347963`、`.347964`，2017-06-20 至 2017-06-25），全文见 `raw_source.raw_json`

## 10.2 【Linux社区】console_sem 批判与 RW 转换草案

**要点**：Sergey：console_sem 啥都管（console 驱动表读写、单 CPU 打印、通用锁、TASK_UNINTERRUPTIBLE 等待、解锁时刷 logbuf、用户空间 tty_open/proc 也可取）；好奇除 vprintk_emit 与 flush_on_panic 外谁真想 console_unlock 刷屏；PoC 把 console_unlock 变纯 unlock、console_sem 转 rwsem（console_read/write_lock API）+console_tryflush/console_flush；宣称“bug free (tm)，boot tested only”；Vetter：fbdev 锁紊乱根因——fb notifier 三用途（模块化加载次序、背光、杂项）互反锁；console_lock 已成为事实最外层；fbdev->fbcon->fbdev->drm emulation->kms 链都在锁内做初始 modeset；唯修法=部分重写 fbdev（死子系统无人志愿）；Sergey RW 方案审慎乐观——serial 环境可行、fbcon 会疼；烧 fbcon 重写 kms 应急是最简治本但 kmscon 无兴趣；Vetter 给 fbdev 5 步止痛法：fbcon 并入 fb.ko（Kconfig 编译期选项）；等 1 年无人报回归；拆 notifier 改直调；审计中把 console_lock 下推到正确位置；再应用 console_lock 合理化 patch；Rostedt：NMI 打印不彻底（缓冲限量、ftrace_dump_on_oops 可巨大）；认可 throttling 方向——另法节流狂 printk 的 CPU

**史料**：`347969`、`347976`、`347977`、`347978`

**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347969 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347976 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347977 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347978 -->`
**史观**：经验优先（总纲 9：以 console_sem 六项职责清点、fb notifier 三用途互反锁等实况为据）；动手者叙事（总纲 10：fbdev 五步止痛法由 Vetter 本人给出）；偶然性优先（总纲 5：fbdev 无人志愿重写这一人事偶然构成主要约束）
**辨析**：Sergey 自陈“bug free (tm)，boot tested only”，其 console_sem 转 rwsem 草案仅经启动验证；Vetter 明言 kmscon 无人问津，故“烧 fbcon 重写 kms”只具理论可行性。
**文献**：DSLXC-4191/4198/4199/4200（`ksummit-discuss.messages.347969`、`.347976`、`.347977`、`.347978`，2017-06-20 至 2017-06-25），全文见 `raw_source.raw_json`

## 10.3 【Linux社区】offload 与 NMI：缓冲取舍与错误通道

**要点**：Hannes：Vetter 方案中丢新还是丢旧——宁可丢旧（可调缓冲大小）；critical 消息应不等普通缓冲直接刷出；OOM 前海量普通消息会让关键一条永远看不到；带时间戳/CPU 号则乱序也可排序；Petr：offload 机制刻不容缓（流传多年、kthread 版）；避免 sleep 持 console_lock 才是正路；gfx init 为何要 console_lock 不得其解；Sergey 两 RFC（offload 与新人）链接；console_lock 的暗面还没摸清；Sergey：lockless per-CPU logbuf 未必值（logbuf_lock 死锁已由 printk_nmi/safe 解决，剩下是 printk 控不了的锁）；per-CPU 要做 N 路归并；直打 vs offload 行为差异——offload 丢消息 bug 报过；单 CPU 直打场景会被 offload 破坏；或需 throttling；Petr：per-CPU 缓冲三大疑（尺寸/散乱需工具/suggest lockless 复杂如 ftrace 单读者）；printk_kthread 已在试；两大任务=存储快 vs 输出可靠；列出 8 问题清单：NMI 硬锁、递归调用、console 软锁、洪水丢消息、挂起丢消息、续行混断、时间戳不可靠排序、console 代码大泥潭；Andrew Lunn（嵌入式视角）：板子 bring-up 时串口未起、kernel 崩在串口前——JTAG 读内存要求格式简单可读；early_printk 或可解决；Andrew Lunn：排序只需序号+CPU 号原子；序号入输出、乱序自明；256 序号空间够不够要反馈；David Howells：mount 错误信息应从 dmesg 改到进程面（context）回传用户态；曾把 supplementary error buffer 放 task_struct（nfs4 mount submount 自动挂载）；贴 RFC patch——prctl(PR_ERRMSG_ENABLE/READ) 两新号；errorf/invalf 宏；Al 认为太泛不赞成；Sergey：玩过 RW console_sem 到深夜（sad）；patch 存 github（console_RW_sem 分支）以防丢；认同 Vetter 的 Big Konsole Lock（德拼）——大多场景需独占写，转读锁收益可疑；printk 可转 rwsem 保留 console_lock wrapper，但希望有更多读模式位点；Sergey 头脑风暴：现有 printk_nmi per-CPU 缓冲的“意外 hack”可绕开——仅当 NMI 恰落在持 logbuf_lock 的 CPU 时才进 per-CPU 缓冲；故 per-CPU 缓冲可小、logbuf 做大；per-CPU logbuf 则每个 CPU 都得大，双倍内存风险；Petr：early printk 直写不落任何缓冲；回应 Lunn 的 JTAG 内存读取格式要求

**史料**：`347966`、`347967`、`347970`、`347971`、`347972`、`347973`、`347984`、`347985`、`347986`、`347987`

**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347966 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347967 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347970 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347971 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347972 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347973 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347984 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347985 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347986 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347987 -->`
**史观**：多方平等（总纲 8：Hannes、Petr、Sergey、Andrew Lunn、Howells 五方对 offload 与 NMI 的取舍并置）；经验优先（总纲 9：以 printk_nmi/safe 已解决的 logbuf_lock 死锁、printk_kthread 试验为据）；偶然性优先（总纲 5：八问题清单由本次讨论临时归纳，非预先议程）
**辨析**：Petr 的 8 问题清单（NMI 硬锁、递归调用、console 软锁、洪水丢消息、挂起丢消息、续行混断、时间戳不可靠排序、console 代码大泥潭）系其个人归纳；Howells 的 prctl(PR_ERRMSG_ENABLE/READ) 错误回传方案遭 Al 认为太泛而不赞成，属未采纳提案。〔存疑：原报告 P3 项所指“行 29”英文原句未能在 10.3 要点中定位，待回源判定表复核〕
**文献**：DSLXC-4188/4189/4192/4193/4194/4195/4206/4207/4208/4209（`ksummit-discuss.messages.347966`、`.347967`、`.347970`、`.347971`、`.347972`、`.347973`、`.347984`、`.347985`、`.347986`、`.347987`，2017-06-20 至 2017-06-25），全文见 `raw_source.raw_json`

## 10.4 【Linux社区】序号、保序与时间戳重排

**要点**：Petr：Lunn 的序号方案可行（Yup 认可）；重排多严重、256 序号够不——求反馈；Zolnierkiewicz（fbdev 维护者）：Vetter 5 步方案可行（fbcon 并入 fb.ko→等 1 年→拆 notifier→下推 console_lock→应用 patch）；Rostedt：理想=oops 的 NMI 能直打 console 完全绕开 log buffering；Mauro：开发者也要保序（让报 bug 者开 debug 重跑）；Kconfig 开关可强制（media 有 CONFIG_VIDEO_ADV_DEBUG 等类似项），选了就打日志排序默认；Lunn：从随机用户拿到 crash log 时必须能看出排序已断不可信；Mauro 对 Kconfig 排序默认的提议，重申开发机保序需求；Rostedt：排序不保证时强制时间戳；时间戳取 printk 调用时点而非入缓冲时点——事后可凭乱序时间戳序列重排；Lunn：时间戳粒度未必够，仍偏好再加序列号

**史料**：`347988`、`347989`、`347991`、`347998`、`348003`、`348004`、`348005`

**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347988 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347989 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347991 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347998 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348003 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348004 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348005 -->`
**史观**：多方平等（总纲 8：Petr、Zolnierkiewicz、Rostedt、Mauro、Lunn 五方对保序方案的并置）；经验优先（总纲 9：以 256 序号空间、CONFIG_VIDEO_ADV_DEBUG 等既有先例为据）；拒绝进步叙事（总纲 1/3：不将序号或时间戳重排写作 printk 保序问题的“解决”）
**辨析**：Lunn 的“序号+CPU 号”与 Rostedt 的“按 printk 调用时点取时间戳、事后凭乱序序列重排”为两条并行方案，本块未收敛；Mauro 的 Kconfig 强制排序提议仅针对开发机场景。
**文献**：DSLXC-4210/4211/4213/4220/4225/4226/4227（`ksummit-discuss.messages.347988`、`.347989`、`.347991`、`.347998`、`.348003`、`.348004`、`.348005`，2017-06-20 至 2017-06-25），全文见 `raw_source.raw_json`

## 10.5 【Linux社区】Bug reporting feedback loop

**要点**：Laura Abbott 发起 Bug reporting feedback loop：Fedora 紧跟 stable（4.11.6 pending）但报告脱节——bugzilla 摘要人工转上游繁琐；master 修复到 stable 有滞后（非催 stable）；早期崩溃仍靠手机拍屏“创意格式”；Jiri Kosina：SUSE 做“Kernel of the day”build 供可选仓库——报告者无须自编内核即可验是否已修；上游确证后内部负责人接单；反问还有何改进空间；Iwai（openSUSE/SUSE bugzilla 分诊）：MAINTAINERS 里报告渠道信息极少（自家 ASoC 也缺）；子系统间报 bug 方式不一（同子系统内 bugzilla 与否也分裂）；调试手段秘而不宣（“grandmother's recipe”）；旧版内核与回归跟踪脱节；bugzilla 老 bug 无人理烂掉（维护者超载、bug master 魔咒）；建议上游/发行方双方都设专人——安全 bug 协调已有，应扩到更大面；Jiri：统一 tracker 反而反效果，不为所动；专人跟踪同意但悲观——连找个人盯 regression 都难；Iwai：也不求统一，但差距该缩（多样性是开源长处此处例外）；承认不乐观，但 mindset 得先变——把 bug 处理当回事、多投资源；Bottomley：SCSI 的 bugzilla.kernel.org 流程=按子系统 vector 到 linux-scsi 列表、bugzilla 捕获邮件往来；distro bugzilla 可照抄（首次摘要邮件仍要人工、之后 bugzilla 自动捕获；列表可作 watcher）；Greg KH：stable 有快有慢——-rc1 合并窗大量 stable 标记要几周消化（多为开发者自认不严重、拖到 -rc1 前才给 Linus 的）；可随时邮件点名提前队列；-rc1 大块后通常一周内进 stable，“太快”抱怨多于“太慢”；Jiri：同意 stable 节奏对 SUSE 不是大问题（*）——等不及就自己 cherry-pick、合并进新 stable 再丢（有时反而太快）；(*) 常相反

**史料**：`347974`、`347975`、`347980`、`347981`、`347982`、`347983`、`347993`、`347994`

**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347974 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347975 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347980 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347981 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347982 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347983 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347993 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347994 -->`
**史观**：多方平等（总纲 8：Abbott、Kosina、Iwai、Bottomley、Greg KH 五方并置）；经验优先（总纲 9：以 SUSE“Kernel of the day”构建、SCSI 侧 bugzilla 按子系统 vector 到 linux-scsi 列表等实作为据）；自反性声明（总纲 7/23：本块为发行方与上游双视角实录，不取单一结论）
**辨析**：Jiri 明言“统一 tracker 反而反效果”，故本块不得读作统一缺陷跟踪的倡议史料；Greg KH 称 stable“太快”抱怨多于“太慢”，与发行方滞后的体感构成张力。
**文献**：DSLXC-4196/4197/4202/4203/4204/4205/4215/4216（`ksummit-discuss.messages.347974`、`.347975`、`.347980`、`.347981`、`.347982`、`.347983`、`.347993`、`.347994`，2017-06-20 至 2017-06-25），全文见 `raw_source.raw_json`

## 10.6 【Linux社区】Documentation issues：RST 转换与维护

**要点**：Corbet 发起 Documentation issues：4.13 收最后 DocBook→RST（Mauro 主导），但合并冲突不可开交（别树伸进 Documentation/ 改已转文件）；提议 session=维护不贴源码树层级体系的“子系统”；反问 RST 转换要不要继续——照 Peter 说法“删光回 80 列 7bit ASCII”？维护者想要什么样的 doc 子系统；Rafael：PM 文档继续转 RST、完成前不欢迎删 .txt；ACPI 同理；PM 侧未来冲突不会多；Mauro：冲突对转换不可避免（git 不认 rename）；回 ASCII 是坏主意——text 文件本就乱（无标题/markdown/MediaWiki/RST/自造记号混用）；RST 至少统一了风格、分册归位更清晰、编辑器高亮；media 表格 210+ 列（64-bit word bit fields）ASCII 根本放不下；uAPI 文档九十年代就 LaTeX/PDF，回 ASCII 等于重写；建议继续转换；Rafael 补充：RST 比 80 列 ASCII 吸引人至少因交叉引用；HTML 可互链浏览大大加分（kernel.org 已自动发布）；Rafael：认可 Mauro 的中量级布局改进（同文档混用用户/内核接口、cpia2 例）；生成 HTML 主动互链是巨大优势；媒体表 210+ 列回归论成立；名文件（kernel-parameters.txt 等）别搬别改名，轮换现有链接、或至少 symlink 保 Web 链接存活；Mauro 回应 Rafael：同文档混用户/kernel 信息确实难分部（cpia2、input 驱动例）；建议讨论如何更好组织；RST 编辑器高亮确实有 bug 但也有用；“知名文档”应留小 text 指向新址（1）或 symlink（2）——当前混合做、该统一；个人偏好（1）逼人更新交叉引用

**史料**：`347992`、`347995`、`347996`、`347999`、`348000`、`348002`

**史观**：多方平等（总纲 8：Corbet、Rafael、Mauro 三方对 RST 转换的分歧并置）；经验优先（总纲 9：以 media 表格 210+ 列、uAPI 文档九十年代即 LaTeX/PDF 等实况为据）；拒绝进步叙事（总纲 1/3：不将 DocBook→RST 写作文档工程“进步”）
**辨析**：Corbet 转述的“删光回 80 列 7bit ASCII”系引 Peter 之说，被 Mauro 明确否定；Mauro 指出“知名文档留小 text 指向新址”与“symlink”两种做法当前并存、应予统一，属未决。
**文献**：DSLXC-4214/4217/4218/4221/4222/4224（`ksummit-discuss.messages.347992`、`.347995`、`.347996`、`.347999`、`.348000`、`.348002`，2017-06-20 至 2017-06-25），全文见 `raw_source.raw_json`

## 10.7 【Linux社区】Media Summit 与峰会议程机制

**要点**：Mauro：Media Summit 惯例随 Kernel Summit——今年改两天（首日内部 patch 处理流程、次日对公众技术议题 uAPI/kAPI 如 Request API）；Ted 声明：峰会话题提案截止 6/26 周一；附 Linus 次级名单 preseed；[MAINTAINERS SUMMIT] 前缀限定开发流程议题

**史料**：`347997`、`347965`

**史观**：动手者叙事（总纲 10：Media Summit 安排与提案截止由 Mauro、Ted 当事人给出）；偶然性优先（总纲 5：议程机制因 6/26 周一截止这一具体时点而成型）
**辨析**：本块仅 2 封邮件（Mauro、Ted）；Ted 附 Linus 次级名单 preseed 并限定 [MAINTAINERS SUMMIT] 前缀用于开发流程议题，属峰会组织机制的直接记录。
**文献**：DSLXC-4219/4187（`ksummit-discuss.messages.347997`、`.347965`，2017-06-20 至 2017-06-25），全文见 `raw_source.raw_json`

## 10.8 【Linux社区】KS2014 档案混档

**要点**：Teodora（2014-05-12）：对 HPA 表示讨论别太技术化（实现讨论用 RFC 线程[0]）；KS 该谈的是 QR workflow 变化与要维护的基础设施；质疑现在能否直接 POST oops 到 kernel.org；Shuah Khan（2014-05-12）：PM deps 话题曾在 Media Mini-summit 短暂讨论过；media 类似用例（tuner suspend/resume 只该一次，而非每个自认独占的驱动各做一次）；请求提名；Dave Hansen（2014-05-12）：模块用 vmalloc 4K 页（巨大 TLB 压力）——模块加载早于内存碎片化，先 kmalloc 失败再退 vmalloc 大概率成功；Mark Brown（2014-05-12）：PM deps 对 ASoC 不陌生——machine driver 一直在解，Russell King 刚出通用版依赖延迟胶水（component.h）；我维护的几个 subsystem 都受影响，有兴趣；Roland Dreier（2014-05-12）：10 年前就给自己 ppc440 kernel 加过 kmalloc-vmalloc 退路 hack（避免软件灌 TLB 省 2x module code）；模块加载早期碎片少，先 kmalloc 失败退 vmalloc 可行

**史料**：`347957`、`347968`、`347979`、`347990`、`348001`

**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347957 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347968 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347979 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347990 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348001 -->`
**史观**：自反性声明（总纲 7/23：明示本块为跨年混档，不与 2017 线程混叙）；偶然性优先（总纲 5：档案信因页面切片规则而混入本页）；拒绝进步叙事（总纲 1/3：不将 2014 议题写作其后讨论的“前身”）
**辨析**：5 封均系 2014-05-12 档案信（Teodora、Shuah Khan、Dave Hansen、Mark Brown、Roland Dreier），与 p75 主体 2017-06 线程无回复关系；本块只作归卷登记。
**文献**：DSLXC-4179/4190/4201/4212/4223（`ksummit-discuss.messages.347957`、`.347968`、`.347979`、`.347990`、`.348001`，2014-05-12），全文见 `raw_source.raw_json`

---
注：本文件由判定表程序化生成（10.1-10.8 共 8 块，覆盖 50/50 CAND）；要点逐字取自判定表“要点”列（审读实录），史料锚与 CAND 一一对应。
