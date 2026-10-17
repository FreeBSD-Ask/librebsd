# 70 【Linux社区】扁平树与Werror之辩

> 来源：ksummit-discuss p122（50 封全读，2019-06 MAINTAINERS SUMMIT pull network 线+Werror 策略，夹杂 2014-05 档案信）
> 判定：50 CAND / 0 NV。主题分布：media 维护模式自辩 1、扁平树信任之问 1、复审非信任而是双审 1、评审标签自动化提案 1、有条件应允实验 1、本地钩子免基建论 1、跨子树补丁与钩子 1、staging 缺陷数据 1、单驱动与重构之辨 1、桌面 40 核机复审流程 1、入乡随俗规则论 1、可持续性质疑 1、转换任务入导师名单 1、文件内一致优先 1、未转 RST 目录盘点 1、重构回归风险论断 1、drm 维护脚本三类树 1、media PM 桎梏陈情 1、维护者职责社会论 1、检查应前置分包 1、features 解析方案 1、文件本地风格之害 1、通审三理由与十年答辩 1、通用测试基建盘点 1、积压队列与升级数 1、教程级讲题拒收函 1、环形缓冲术语定调 1、arch 内存码去重议题 1、GPIO 通用查询接口 1、CI 资助与动机话题 1、退回 PR 亦是教学 1、自动化测试峰议程 1、features 脚本样张 1、日志差分工具指路 1、特性表脚本 RFC 补丁 1、缺 SPDX 审阅意见 1、特性脚本补丁进展 1、W=2 噪声与二进制比对 1、W=1 按树选项提案 1、文档注释风格之争 1、树级编译旗标先例 1、默认关的 Werror 辩护 1、Werror 跨架构隐患 1、Werror 启用法盘点 1、Werror 全局不可取论 1、Werror 敌视用户论 1、渐进推广 Werror 1、编译器 QA 现状 1、i915 告警治理细节 1、make -k 覆盖盲区 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p122 的逐封提取（50 CAND / 0 NV），全 50 块采用**单行摘要体例**（丙型）：每块由“## 70.x 【Linux社区】题名”与若干“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 70.1 【Linux社区】media 维护模式自辩

- 【Linux社区】Mauro 披露 media 每周一次约 1 小时 IRC 例会与 patchwork 统计（月收 400-1000 补丁、收 100-300），称逐一复审是识别该看哪些 PR 的方式，并指 Laurent 名下积压 2013-2018 年 23 封加 2019 年 48 封补丁。 `<!-- ROW_MINE: ksummit-discuss.messages.350306 -->`

## 70.2 【Linux社区】扁平树信任之问

- 【Linux社区】Bottomley 定性“我复审所有已收补丁”等于完全扁平树，断言无信任即无卸载，追问 Mauro 为何不敢让未经自己复审的分支入树，称此为深层树是否可能的关键。 `<!-- ROW_MINE: ksummit-discuss.messages.350307 -->`

## 70.3 【Linux社区】复审非信任而是双审

- 【Linux社区】Mauro 答复“不是信任问题”，称 V4L2 API 有 80 多个 ioctl、目标是让补丁至少获两道复审，且开发者多为子领域专家，需通观者在收口处防 API 改动伤及他类设备。 `<!-- ROW_MINE: ksummit-discuss.messages.350308 -->`

## 70.4 【Linux社区】评审标签自动化提案

- 【Linux社区】Bottomley 提议以树中累积的 Reviewed-by 标签让 pull 机制自动判定是否收 PR，可要求两道且其一出自指定评审名单，并主动请缨帮 media 写脚本试“自动化替人分活”。 `<!-- ROW_MINE: ksummit-discuss.messages.350309 -->`

## 70.5 【Linux社区】有条件应允实验

- 【Linux社区】Mauro 应允可试该自动化但须众人知晓出错可回退，重申 Media Summit 上已谈过的症结是基础设施缺资源。 `<!-- ROW_MINE: ksummit-discuss.messages.350310 -->`

## 70.6 【Linux社区】本地钩子免基建论

- 【Linux社区】Bottomley 澄清脚本无需自动化基建，只在收 PR 的本机跑 pull 钩子，坏提交即拒收并说明原因，通过后再自加检查推送 kernel.org。 `<!-- ROW_MINE: ksummit-discuss.messages.350311 -->`

## 70.7 【Linux社区】跨子树补丁与钩子

- 【Linux社区】2014 年档案信：Mauro 阐明 Acked-by 的意义是让维护者预知补丁将在别处合入，自述多次 nack 触碰即将删除文件的补丁，赞 git 钩子设想并愿分享 media 树在用钩子代码。 `<!-- ROW_MINE: ksummit-discuss.messages.350312 -->`

## 70.8 【Linux社区】staging 缺陷数据

- 【Linux社区】Carpenter 统计 staging 带 Fixes 补丁：初传驱动仅占约三分之一 bug，机械新手补丁约 3-5%，多数 bug 出自维护者所做的难审清理，普通用户获 Reported-by 每年仅约 2-5 次。 `<!-- ROW_MINE: ksummit-discuss.messages.350313 -->`

## 70.9 【Linux社区】单驱动与重构之辨

- 【Linux社区】Van Assche 澄清自己谈的是影响单个驱动的补丁，反问 Leon 所指是否为波及整个子系统的 API 重构，划开回归风险争议的分界。 `<!-- ROW_MINE: ksummit-discuss.messages.350314 -->`

## 70.10 【Linux社区】桌面 40 核机复审流程

- 【Linux社区】Mauro 详述现流程：桌下 40 核 HP 服务器把 PR 转 quilt 逐补丁跑 checkpatch --strict 与 smatch/sparse i386 编译，失败鸣笛人工处置，成功后脚本回写 patchwork，并称更盼 CI 机器人预先核验。 `<!-- ROW_MINE: ksummit-discuss.messages.350315 -->`

## 70.11 【Linux社区】入乡随俗规则论

- 【Linux社区】Helgaas 主张“when in Rome”随本地约定即可覆盖大半风格分歧而无需全局统一甚至无需成文，感叹该规则常被无视。 `<!-- ROW_MINE: ksummit-discuss.messages.350316 -->`

## 70.12 【Linux社区】可持续性质疑

- 【Linux社区】Babka 引 Mauro 自述 6 时至 22 时几乎不歇并搭周末的日程，直断“根本不可持续也不健康”，认为转折之日应尽早到来。 `<!-- ROW_MINE: ksummit-discuss.messages.350317 -->`

## 70.13 【Linux社区】转换任务入导师名单

- 【Linux社区】Shuah 认可先转换再更新的路径，提出转换也可立为导师计划任务并请 Mauro 提供想转文档清单，欢迎其出任导师。 `<!-- ROW_MINE: ksummit-discuss.messages.350318 -->`

## 70.14 【Linux社区】文件内一致优先

- 【Linux社区】Helgaas 补释应循同文件既有缩进注释与 git 历史的提交措辞，转述线下意见“file xyz.c 即该子系统代表风格”，主张文件内自洽最要紧、统一须专题补丁为之。 `<!-- ROW_MINE: ksummit-discuss.messages.350319 -->`

## 70.15 【Linux社区】未转 RST 目录盘点

- 【Linux社区】Mauro 列出尚无 rst 的目录仅剩 scsi、RCU、features 等，cpu-freq 内容过时维护者不愿动，ABI 另按特殊路线处理，并记两类应留纯文本的例外（含涉版权谈判的旧手册章节）。 `<!-- ROW_MINE: ksummit-discuss.messages.350320 -->`

## 70.16 【Linux社区】重构回归风险论断

- 【Linux社区】Romanovsky 断言最易引入回归的是重构、清理等大规模改动，而非个别驱动的一次性修补。 `<!-- ROW_MINE: ksummit-discuss.messages.350321 -->`

## 70.17 【Linux社区】drm 维护脚本三类树

- 【Linux社区】Vetter 介绍源自 drm-intel、现用于 drm-misc 与 drm 的脚本把树分三类：好树一键收、好树无工具偶返工、弱树须人工细查，新添 Fixes 标签校验，且“谁犯错脚本没拦住就罚谁去改进脚本”。 `<!-- ROW_MINE: ksummit-discuss.messages.350322 -->`

## 70.18 【Linux社区】media PM 桎梏陈情

- 【Linux社区】2014 年档案信：Mauro 称 media 电源管理“自始就坏”，桥驱动挂起时解绑全部驱动的补法屡治屡坏，须在 probe 时建 PM 依赖树，自荐并提名 Shuah 参与 PM dependencies 议题。 `<!-- ROW_MINE: ksummit-discuss.messages.350323 -->`

## 70.19 【Linux社区】维护者职责社会论

- 【Linux社区】Pinchart 断言维护者职责是让子系统健康前行而非通审，“过度之爱会致窒息”以子女离家喻放手，倡加深 pull 网络分摊职责，并指纯扁平单维护者模型难以为大子系统扩容。 `<!-- ROW_MINE: ksummit-discuss.messages.350324 -->`

## 70.20 【Linux社区】检查应前置分包

- 【Linux社区】Uytterhoeven 称 checkpatch 与静态检查应由发 PR 的受信子维护者及各机器人提前完成，越早发现越省，并透露 patchwork.kernel.org 有按 linux-next 收录回写状态的在制自动化。 `<!-- ROW_MINE: ksummit-discuss.messages.350325 -->`

## 70.21 【Linux社区】features 解析方案

- 【Linux社区】Mauro 判 Documentation/features 不宜直转 RST，仿 get_abi.pl 提议解析校验并生成按特性、按架构、特性×架构矩阵三种输出，主张以脚本产 ReST 分册入书。 `<!-- ROW_MINE: ksummit-discuss.messages.350326 -->`

## 70.22 【Linux社区】文件本地风格之害

- 【Linux社区】Mauro 反对逐文件随风格：内核级大补丁无从逐文件核对，举 DVB 曾写“struct dvb_foo* bar”与内核风格混烂数年、终靠加 kernel-doc 整改核心，断言纵容只会更乱。 `<!-- ROW_MINE: ksummit-discuss.messages.350327 -->`

## 70.23 【Linux社区】通审三理由与十年答辩

- 【Linux社区】Mauro 列继续通审三理由（掌握子系统动态、多一道复审提质量、“我喜欢我的工作”），称该节奏已持续十年且有家庭爱好，并用流程图驳称加深网络不会降低补丁延迟。 `<!-- ROW_MINE: ksummit-discuss.messages.350328 -->`

## 70.24 【Linux社区】通用测试基建盘点

- 【Linux社区】Brown 指议题虽以 media 为例实属全局问题，盘点 KernelCI 扩展运行时测试与 CKI 等非子系统专属基建，并点出 Tim Bird 维系的 elinux Automated_Testing 邮件列表与月度电话会。 `<!-- ROW_MINE: ksummit-discuss.messages.350329 -->`

## 70.25 【Linux社区】积压队列与升级数

- 【Linux社区】Mauro 披露当前积压约 500 补丁、近两周每周处理约 200，六月底 patchwork 由 1.0 升 2.1 并拟换将停服的 web 服务器，自 2013 起用自制脚本回写状态，media 已达 W=1 零告警。 `<!-- ROW_MINE: ksummit-discuss.messages.350330 -->`

## 70.26 【Linux社区】教程级讲题拒收函

- 【Linux社区】Ts'o 答复 Tanish Shinde：教程级报告不适合 Plumbers 与内核峰会，点名校验“文件系统结构分解”与“树莓派 3 自制 Docker 引擎”两题过浅，建议改投 Open Source Summit。 `<!-- ROW_MINE: ksummit-discuss.messages.350331 -->`

## 70.27 【Linux社区】环形缓冲术语定调

- 【Linux社区】Ts'o 附议 Howells 统一环形缓冲术语，援引 Russell King 名言“head is where the food goes in, the tail is where the ...”，请其把提案正式提交 LPC19（bit.ly/lpc19-submit）。 `<!-- ROW_MINE: ksummit-discuss.messages.350332 -->`

## 70.28 【Linux社区】arch 内存码去重议题

- 【Linux社区】Ts'o 转贴 Rapoport 议题全文：各架构 PGALLOC_GFP、early_alloc、free_initmem 等内存管理代码大量重复，主张归并公共代码并精化 arch↔mm 接口以免再添 HAVE_ARCH_* 类选项。 `<!-- ROW_MINE: ksummit-discuss.messages.350333 -->`

## 70.29 【Linux社区】GPIO 通用查询接口

- 【Linux社区】2014 年档案信：Walleij 答称 GPIO 已有 DT 与 ACPI 双后端的通用查询接口“只需继续铺开”，呼应 Arnd 以标准命名接口统一 GPIO/IRQ/DMA 查找的思路。 `<!-- ROW_MINE: ksummit-discuss.messages.350334 -->`

## 70.30 【Linux社区】CI 资助与动机话题

- 【Linux社区】Pinchart 称延续十年“并不必然是可取的”，举 DRM/KMS 自 v4.0 起合入量为 media 的 2-8 倍、X.org 基金会在 SPI 伞下募资付 gitlab CI 托管为例，并提议把贡献者去激励拆成新线程。 `<!-- ROW_MINE: ksummit-discuss.messages.350335 -->`

## 70.31 【Linux社区】退回 PR 亦是教学

- 【Linux社区】Iwai 主张缺作者 SOB 等致命错应直接拒拉而非代为修复，“推回虽断流，却能让子系统维护者学到东西”，小错可拉后再补。 `<!-- ROW_MINE: ksummit-discuss.messages.350336 -->`

## 70.32 【Linux社区】自动化测试峰议程

- 【Linux社区】Bird 预告休假一周后跟进 syzbot 通知机制（若 Linus 认可则推广并接入 Fuego）与 W=[0-3] 新告警隔离、二进制变化检查等构想，宣布 10 月 31 日里昂 OSSUE/ELCE 旁首办 Automated Testing Summit。 `<!-- ROW_MINE: ksummit-discuss.messages.350337 -->`

## 70.33 【Linux社区】features 脚本样张

- 【Linux社区】Mauro 晒 get_feat.pl 三种输出样页（特性页、arm64 页、全矩阵页）并称补丁已写妥“即将提交邮件列表征求意见”。 `<!-- ROW_MINE: ksummit-discuss.messages.350338 -->`

## 70.34 【Linux社区】日志差分工具指路

- 【Linux社区】Uytterhoeven 推介自用 linux-log-diff 脚本比对新旧 build.log，即其“v5.2-rc5 构建回归/改进”常规报告所本。 `<!-- ROW_MINE: ksummit-discuss.messages.350339 -->`

## 70.35 【Linux社区】特性表脚本 RFC 补丁

- 【Linux社区】Mauro 发 RFC 补丁新增 470 行 scripts/get_feat.pl，可校验 features 文件并按特性、按架构、矩阵三格式出 ReST，拟经 Sphinx 扩展嵌入内核文档。 `<!-- ROW_MINE: ksummit-discuss.messages.350340 -->`

## 70.36 【Linux社区】缺 SPDX 审阅意见

- 【Linux社区】Kroah-Hartman 对 get_feat.pl 补丁仅回一句“没有 SPDX 行”，即时点出新脚本须补许可证标识。 `<!-- ROW_MINE: ksummit-discuss.messages.350341 -->`

## 70.37 【Linux社区】特性脚本补丁进展

- 【Linux社区】Mauro 回应已加 SPDX，并新增几乎照搬 kernel_abi.py 的 Sphinx 扩展，将在 admin-guide 生成特性×架构矩阵与 x86 特性页，称 get_feat.pl current 可取代 list-arch.sh。 `<!-- ROW_MINE: ksummit-discuss.messages.350342 -->`

## 70.38 【Linux社区】W=2 噪声与二进制比对

- 【Linux社区】Mauro 称 syzbot 报告对 media 有用，但 W=2 因 char/unsigned char 混用“几乎不可用”而 W=1 曾助其修 bug，并提出以 inotify 监听配合 objdump -S 比对补丁前后反汇编的实现思路。 `<!-- ROW_MINE: ksummit-discuss.messages.350343 -->`

## 70.39 【Linux社区】W=1 按树选项提案

- 【Linux社区】Carpenter 建议向 kbuild 开发者提议把 W=1 做成按树选项，以兼顾 media 零告警与其他子系统的告警负荷。 `<!-- ROW_MINE: ksummit-discuss.messages.350344 -->`

## 70.40 【Linux社区】文档注释风格之争

- 【Linux社区】2014 年档案信：Mauro 自认收过杂风格文档补丁，但拒为统一风格退回从他系统移植的 Doxygen 大驱动，主张造半自动转换工具把数百小时省给新功能与真 bug。 `<!-- ROW_MINE: ksummit-discuss.messages.350345 -->`

## 70.41 【Linux社区】树级编译旗标先例

- 【Linux社区】Vetter 称无需问 kbuild，“加个 Kconfig 为你的树设额外 cflags 即可”，i915.ko 即照此连 -Werror 一起跑，组合测试自会暴露新告警。 `<!-- ROW_MINE: ksummit-discuss.messages.350346 -->`

## 70.42 【Linux社区】默认关的 Werror 辩护

- 【Linux社区】Pinchart 称挂在默认关闭的 Kconfig 后的 -Werror 并非自动启用，机器人可开而用户忽略，自述全部编译脚本用 -Werror 屡屡更早抓到新告警，越全局越快收口。 `<!-- ROW_MINE: ksummit-discuss.messages.350347 -->`

## 70.43 【Linux社区】Werror 跨架构隐患

- 【Linux社区】Mauro 赞 W=1 按树可白得新告警，但反对自动加 -Werror：换编译器版本或怪异架构、尤其 COMPILE_TEST 下 typedef 差异会放大误报，重申 media 目标是全数通过 COMPILE_TEST。 `<!-- ROW_MINE: ksummit-discuss.messages.350348 -->`

## 70.44 【Linux社区】Werror 启用法盘点

- 【Linux社区】Mauro 认可 Kconfig 或 make CFLAGS 方式，盘点各子系统现状：有无条件 ccflags-y := -Werror、有判 EXTRA_CFLAGS 的、有 CONFIG_PPC_WERROR 专属开关，media 历史上吃过无条件 -Werror 的亏。 `<!-- ROW_MINE: ksummit-discuss.messages.350349 -->`

## 70.45 【Linux社区】Werror 全局不可取论

- 【Linux社区】Bottomley 断言成熟构建机器人不会开 -Werror（其要全树编译再差分告警），认可小项目可用但巨头将被迫标注大量 gcc 误报且被绑死特定 gcc 版本，指现状即 subdir-ccflags-y 按目录开、不应全局强制。 `<!-- ROW_MINE: ksummit-discuss.messages.350350 -->`

## 70.46 【Linux社区】Werror 敌视用户论

- 【Linux社区】Brown 断言“干净构建不靠开 -Werror，靠重视告警”，称其调试时对未用变量与罕见配置架构告警极不友好。 `<!-- ROW_MINE: ksummit-discuss.messages.350351 -->`

## 70.47 【Linux社区】渐进推广 Werror

- 【Linux社区】Pinchart 部分认同但称调试代码也该零告警只是习惯问题，-Werror 配 git rebase -x 编译测试能在出错处即停，“不求骤然全内核启用，但可逐步扩大”。 `<!-- ROW_MINE: ksummit-discuss.messages.350352 -->`

## 70.48 【Linux社区】编译器 QA 现状

- 【Linux社区】Brown 自嘲要把“只为闭嘴告警不问真伪”的回信写成模板信，称 Arnd 与 clang 团队已在新编译器发布前盯紧告警，KernelCI 基建现役支撑 clang/arm64 测试、有容量即可补旧编译器误报覆盖。 `<!-- ROW_MINE: ksummit-discuss.messages.350353 -->`

## 70.49 【Linux社区】i915 告警治理细节

- 【Linux社区】Nikula 披露 i915 以 -Wall -Wextra 起步再按需（部分按文件）关闭告警，-Werror 藏在 config 开关后，称全局配置须取各方关闭集之并，赞同不全局强制。 `<!-- ROW_MINE: ksummit-discuss.messages.350354 -->`

## 70.50 【Linux社区】make -k 覆盖盲区

- 【Linux社区】Uytterhoeven 补称 make -k 虽能编完多数组件却漏链接错误与 section mismatch，姑且“总比没有强”。 `<!-- ROW_MINE: ksummit-discuss.messages.350355 -->`
