# 44 【Linux社区】API可发现性与stable回归归因之争

> 对应页面：ksummit-discuss p97（pk 349056-349105，2018 API 可发现性/stale 归因/stable-next 多线程 + 2014 档案）
> 判定：50 CAND / 0 NV
> 编号：DSLXC-5829..5878 | claim 已入库（50/50，dslinux_claims.duckdb）

## 44.1 【Linux社区】API 废弃的可发现性与 Coccinelle 脚本（13 例）

**要点（判定表逐字）**：Jani Nikula 评 Julia Lawall 的 Coccinelle 语义补丁，谓其唯一明显缺点是将废弃信息集中到语义补丁而非函数定义本身；Julia Lawall 提议在定义处附注释（已有 deprecated 字样），因复制代码者未必细看定义，将废弃信息附着于用法处更有益；Dan Carpenter 给出 scripts/check_deprecated.pl 与 deprecated_stuff 清单草案，可用简单脚本机械检查新增提交中的废弃函数（含宏），且不向普通构建加告警；Alexandre Belloni 指维护者多经口耳相传才知废弃动向，举例 treewide 的 struct_size 系列提交并未送达各维护者，新辅助函数同样难被发现；Geert Uytterhoeven 排列检查层级——git 提交钩子、checkpatch、coccinelle 机器人，主张 checkpatch 最可行，因作者与维护者都应运行；Jani Nikula 反问能否据 __deprecated 属性自动生成语义补丁；Mark Brown 指这类过渡的最大痛点是口耳相传导致混乱，自陈首次听闻 strscpy 存在及其余变体被废弃，SPDX 标签亦曾如此；Theodore Ts'o 提 strncpy 用于非 NUL 结尾字符数组的场景（以 __u8 型 s_first_error_func[32] 配 __nonstring 压制告警），blanket 废弃时该用什么替代；Kees Cook 析 strncpy 三情形——非 NUL 结尾用 memcpy、需尾随 NUL 填充则待发明 strscpy_pad、安全 strcpy 用 strscpy；Arnd Bergmann 指欲 NUL 填充者多亦不需 NUL 结尾（磁盘定长记录、网络传输防栈泄漏），strncpy 恰合此角例，gcc 除非 __nonstring 否则告警；Theodore Ts'o 述其场景为从 NUL 结尾串拷入定长字符数组，拟 copy_string_to_char_array 等于先 memset 再 strncpy，并承认或有他种角例；Maxime Ripard 谓问题在可发现性而非故意忽视，举 kmalloc_array 收益不显为例，建议仿 msleep 对 mdelay 之告警在 checkpatch 加文档链接；Geert Uytterhoeven 答 Ted，问何须 memset——strncpy 本就零填充目标，且指 Ted 把源与目标抄反了方向

**史料**：`349056`、`349058`、`349059`、`349060`、`349061`、`349062`、`349064`、`349066`、`349077`、`349083`、`349084`、`349085`、`349105`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.349056 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349058 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349059 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349060 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349061 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349062 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349064 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349066 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349077 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349083 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349084 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349085 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349105 -->` 

**史观**：知识注定过时（总纲第 22 条——知识注定过时：Jani Nikula 的“将废弃信息集中到语义补丁而非函数定义本身”与 Julia Lawall 的“在定义处附注释、附着于用法处更有益”之争，正是接口知识如何在代际间传续的机制之辩）；经验优先（总纲第 9 条——经验优先：以 Alexandre Belloni 的“treewide 的 struct_size 系列提交并未送达各维护者”、Mark Brown 的“自陈首次听闻 strscpy 存在及其余变体被废弃，SPDX 标签亦曾如此”为判据）
**辨析**：Maxime Ripard 的“问题在可发现性而非故意忽视，举 kmalloc_array 收益不显为例”为归因判断，其“建议仿 msleep 对 mdelay 之告警在 checkpatch 加文档链接”为落地主张；Geert Uytterhoeven 的“排列检查层级（git 提交钩子、checkpatch、coccinelle 机器人），主张 checkpatch 最可行”为方案比较；Theodore Ts'o 与 Arnd Bergmann、Kees Cook 就 strncpy 角例的往复为技术细节之辩，Geert 末句“问何须 memset，且指 Ted 把源与目标抄反了方向”为事实纠正，本页未见汇总决议。
**文献**：DSLXC-5829、DSLXC-5831、DSLXC-5832、DSLXC-5833、DSLXC-5834、DSLXC-5835、DSLXC-5837、DSLXC-5839、DSLXC-5850、DSLXC-5856、DSLXC-5857、DSLXC-5858、DSLXC-5878（`ksummit-discuss.messages.349056`、`ksummit-discuss.messages.349058`、`ksummit-discuss.messages.349059`、`ksummit-discuss.messages.349060`、`ksummit-discuss.messages.349061`、`ksummit-discuss.messages.349062`、`ksummit-discuss.messages.349064`、`ksummit-discuss.messages.349066`、`ksummit-discuss.messages.349077`、`ksummit-discuss.messages.349083`、`ksummit-discuss.messages.349084`、`ksummit-discuss.messages.349085`、`ksummit-discuss.messages.349105`，2018-09-07、2018-09-07、2018-09-07、2018-09-07、2018-09-07、2018-09-07、2018-09-07、2018-09-07、2018-09-07、2018-09-07、2018-09-07、2018-09-07、2018-09-08），全文见 `raw_source.raw_json`

## 44.2 【Linux社区】stable 回归归因之争与选择偏置（13 例）

**要点（判定表逐字）**：Mark Brown 论产品化 stable 使 QA 投入偏向下游，嵌入侧 linux-next 体验因 KernelCI 与 Olof 启动农场及设备树过渡阵痛消退而明显改善；Laura Abbott 认同 Guenter 之见——真正问题是那些补丁本不该进 stable，其延长 stable -rc 的提案正为此；Sasha Levin 将争论拆为两点，主张 stable 修复与 -rc 阶段无关、质问为何 stable 回归集中于 -rc5 之后，并谓 Linus 态度会打击机器人开发；Sasha Levin 答 Ted，称 linux-next 的 pending-fixes 分支比随机 -rcX 更值得运行；Sasha Levin 举 CoreOS 本年五例用户可见 stable 回归（ext4 bg_flags、cifs slab 越界、tcp 整数溢出、hv_netvsc、xen-netfront、vxlan pmtu）问哪些本不该进 stable；Jens Axboe 认 linux-next 对集成测试有用、对运行时测试无用，几乎无人会跑 pending-fixes 分支；Linus Torvalds 长文辨析选择偏置与相关性非因果——后期 -rc 统计受非关键补丁推迟所污染，N=5 不具统计意义，并指 TCP 例系缺失后向移植依赖；Laura Abbott 承认那些补丁应进 stable，但带 bug 的版本仍随发布流出，主张区分提议进 stable 与已充分测试可进 stable 二者；Sasha Levin 提议 stable-next 分支，stable 标记修复一进 Linus 树（或 linux-next pending-fixes）即推送，以得更长测试期、Greg 从中裁发布；Linus Torvalds 补论非因果相关的另一来源是人工作节律（其合并窗口最忙、Greg 反之；L1TF 例外），相关性实指向未进 linux-next 而非 rc5+；Mauro Carvalho Chehab 答 Jens，linux-next 机器人多报无实际影响的随机配置问题，自己仍待入 -next 再上游但不久等；Mauro Carvalho Chehab 答 Daniel Vetter，谓 CI 对缺资源的小团队更有价值，但购齐各异硬件难，且部分设备（如摄像头麦克风、成像）难测；Linus Torvalds 侧议或将 stable 抓取与测试自动化——对标记 stable 者建队列即时施于旧 stable 树测试，以捕缺失依赖

**史料**：`349063`、`349067`、`349070`、`349071`、`349072`、`349073`、`349074`、`349075`、`349076`、`349078`、`349089`、`349091`、`349098`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.349063 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349067 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349070 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349071 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349072 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349073 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349074 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349075 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349076 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349078 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349089 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349091 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349098 -->` 

**史观**：没有必然性，只有偶然性（总纲第 5 条——没有必然性，只有偶然性：Linus Torvalds 的“后期 -rc 统计受非关键补丁推迟所污染，N=5 不具统计意义，TCP 例系缺失后向移植依赖”与 Sasha Levin 的“CoreOS 本年五例用户可见 stable 回归”正面对撞，未作单方裁断）；经验优先（总纲第 9 条——经验优先：以 Laura Abbott 的“承认那些补丁应进 stable，但带 bug 的版本仍随发布流出”、Jens Axboe 的“linux-next 对集成测试有用、对运行时测试无用，几乎无人会跑 pending-fixes 分支”为判据）
**辨析**：Linus 的“长文辨析选择偏置与相关性非因果”“补论非因果相关的另一来源是人工作节律（其合并窗口最忙、Greg 反之；L1TF 例外），相关性实指向未进 linux-next 而非 rc5+”为其方法论判词；Sasha Levin 的“质问为何 stable 回归集中于 -rc5 之后，并谓 Linus 态度会打击机器人开发”为反方之陈；Mark Brown 的“嵌入侧 linux-next 体验因 KernelCI 与 Olof 启动农场及设备树过渡阵痛消退而明显改善”为其观察；Mauro Carvalho Chehab 的“CI 对缺资源的小团队更有价值，但购齐各异硬件难”为资源约束之陈。
**文献**：DSLXC-5836、DSLXC-5840、DSLXC-5843、DSLXC-5844、DSLXC-5845、DSLXC-5846、DSLXC-5847、DSLXC-5848、DSLXC-5849、DSLXC-5851、DSLXC-5862、DSLXC-5864、DSLXC-5871（`ksummit-discuss.messages.349063`、`ksummit-discuss.messages.349067`、`ksummit-discuss.messages.349070`、`ksummit-discuss.messages.349071`、`ksummit-discuss.messages.349072`、`ksummit-discuss.messages.349073`、`ksummit-discuss.messages.349074`、`ksummit-discuss.messages.349075`、`ksummit-discuss.messages.349076`、`ksummit-discuss.messages.349078`、`ksummit-discuss.messages.349089`、`ksummit-discuss.messages.349091`、`ksummit-discuss.messages.349098`，2018-09-07、2018-09-07、2018-09-07、2018-09-07、2018-09-07、2018-09-07、2018-09-07、2018-09-07、2018-09-07、2018-09-07、2018-09-07、2018-09-07、2018-09-07），全文见 `raw_source.raw_json`

## 44.3 【Linux社区】stable-next 构想与 stable 自动化（8 例）

**要点（判定表逐字）**：Greg KH 引五年前 Linus 因 -rc 补丁爆发的头条旧事，忧心本 -rc1 窗口中标 stable 的修补竟推迟至 -rc1、疑维护者图省事；Greg KH 答 Sasha，自陈本应等满一个 -rc 周期再发 stable，stable-next 无人关注、徒增延迟，仍守等待 -rc 之策；Sasha Levin 答 Greg，stable-next 之要害在 2-3 天 stable-rc 不足以做非机器人测试，描述其工作流，谓 Fedora 测试者可借 -next 分支试用；Greg KH 撤回前议，自承把 -rc1 至 -rc2 间入树者也算入，故或全然有误，暂无可抱怨；Guenter Roeck 答 Linus，0day 与其构建器已在 Greg 发布后即跑，但六条 stable 加主线加 next 资源吃紧，主张增硬件与网络测试而非加分支；Linus Torvalds 答 Guenter，澄清所想是 Greg 实际捡补丁前那一两周，建议就标记 stable 而未捡者做专门的 stable-next 自动测试；Sasha Levin 答 Linus，认同即其 stable-next 构想，自陈曾自动测试上游提交并邮件通报（lkml 2018/4/4/923）但嫌吵，或可改搭 -next 分支；Guenter Roeck 答 Sasha，谓其得出错结论——仍可跑测试但勿发结果邮件，改以结果作为是否纳入 stable 的判据并知会提交者

**史料**：`349081`、`349082`、`349092`、`349096`、`349099`、`349100`、`349102`、`349103`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.349081 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349082 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349092 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349096 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349099 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349100 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349102 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349103 -->` 

**史观**：动手者创造历史（总纲第 10 条——动手者创造历史：以 Sasha Levin 的 stable-next 分支构想、Linus 的“就标记 stable 而未捡者做专门的 stable-next 自动测试”、Guenter Roeck 的“改以结果作为是否纳入 stable 的判据并知会提交者”为分析单位）；理论必须自反（总纲第 7 条——理论必须自反：Greg KH 的“自承把 -rc1 至 -rc2 间入树者也算入，故或全然有误，暂无可抱怨”正是当事人对自身判据的撤回与自反）
**辨析**：Greg KH 的“引五年前 Linus 因 -rc 补丁爆发的头条旧事，忧心本 -rc1 窗口中标 stable 的修补竟推迟至 -rc1、疑维护者图省事”为其初始质疑，其后“自承或全然有误”构成自我更正；Sasha Levin 的“stable-next 之要害在 2-3 天 stable-rc 不足以做非机器人测试”“自陈曾自动测试上游提交并邮件通报（lkml 2018/4/4/923）但嫌吵”为当事人自陈；Guenter Roeck 的“谓其得出错结论——仍可跑测试但勿发结果邮件”为对其方案的修正。
**文献**：DSLXC-5854、DSLXC-5855、DSLXC-5865、DSLXC-5869、DSLXC-5872、DSLXC-5873、DSLXC-5875、DSLXC-5876（`ksummit-discuss.messages.349081`、`ksummit-discuss.messages.349082`、`ksummit-discuss.messages.349092`、`ksummit-discuss.messages.349096`、`ksummit-discuss.messages.349099`、`ksummit-discuss.messages.349100`、`ksummit-discuss.messages.349102`、`ksummit-discuss.messages.349103`，2018-09-07、2018-09-07、2018-09-07、2018-09-07、2018-09-07、2018-09-07、2018-09-07、2018-09-07），全文见 `raw_source.raw_json`

## 44.4 【Linux社区】CoreOS 五例回归个案分析（3 例）

**要点（判定表逐字）**：Dan Carpenter 就 CoreOS 五例逐一补修复提交并析因（ext4 保留 inode、cifs、tcp 缺 02db55718d53 依赖、hv_netvsc 清理实属 bugfix、xen-netfront 两 bug、vxlan pmtu 空指针），建议加静态检查告警；Mauro Carvalho Chehab 答 Linus，合并窗口期间自己摘下维护者帽做开发，修复多自 -rc2 周起、至 -rc3 后入上游，多数拉取请求在 -rc6 周送达；Sasha Levin 答 Dan，逐一回应 CoreOS 各例（ext4 三 TB 以上文件系统、cifs github issue、tcp 降至每秒三百字节、hv_netvsc、xen-netfront），指网络设备测试缺口大

**史料**：`349093`、`349094`、`349095`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.349093 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349094 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349095 -->` 

**史观**：没有必然性，只有偶然性（总纲第 5 条——没有必然性，只有偶然性：Dan Carpenter 的“就 CoreOS 五例逐一补修复提交并析因（ext4 保留 inode、cifs、tcp 缺 02db55718d53 依赖、hv_netvsc 清理实属 bugfix、xen-netfront 两 bug、vxlan pmtu 空指针）”与 Sasha Levin 的逐一回应并置，五例各有偶然成因，非同一机制）；经验优先（总纲第 9 条——经验优先：以 Mauro Carvalho Chehab 的“合并窗口期间自己摘下维护者帽做开发，修复多自 -rc2 周起、至 -rc3 后入上游，多数拉取请求在 -rc6 周送达”为判据）
**辨析**：Dan Carpenter 的“建议加静态检查告警”为其工具层主张；Sasha Levin 的“逐一回应 CoreOS 各例（ext4 三 TB 以上文件系统、cifs github issue、tcp 降至每秒三百字节、hv_netvsc、xen-netfront），指网络设备测试缺口大”为其对五例成因的补充归因。本块例数少而个案密度高，属个案分析而非统计推断。
**文献**：DSLXC-5866、DSLXC-5867、DSLXC-5868（`ksummit-discuss.messages.349093`、`ksummit-discuss.messages.349094`、`ksummit-discuss.messages.349095`，2018-09-07、2018-09-07、2018-09-07），全文见 `raw_source.raw_json`

## 44.5 【Linux社区】安全议题：L1TF 回移与 secure boot 抉择（4 例）

**要点（判定表逐字）**：Jiri Kosina 问封闭安全问题该修补哪些内核（仅主线还是全部 stable），并询 Greg 过去是否真有因后向移植过难而放弃修复的情形；David Woodhouse 评 L1TF 的 stable 后向移植相对顺利，举 fd7e315988 化简 pgd_page 宏当初纯属清理、后被改作他用为例，说明难以预料的依赖；Mauro Carvalho Chehab 因 Intel 八代加 Radeon 需自编译未签名内核而关闭 secure boot，指发行版难用 CONFIG_LOCK_DOWN_MANDATORY；Andy Lutomirski 论 Meltdown／Spectre 之困非流程之过而是被禁 sane 流程，少数非 Intel 上游开发者及时获知，建议设小型协调团队与成文流程仿 MS／Apple

**史料**：`349065`、`349069`、`349086`、`349104`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.349065 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349069 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349086 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349104 -->` 

**史观**：法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：Mauro Carvalho Chehab 的“因 Intel 八代加 Radeon 需自编译未签名内核而关闭 secure boot，指发行版难用 CONFIG_LOCK_DOWN_MANDATORY”与 Andy Lutomirski 的“建议设小型协调团队与成文流程仿 MS／Apple”之争，实为合规义务与用户可择性的利益划分）；分离聚合是永恒规律（总纲第 4 条——分离聚合是永恒规律：David Woodhouse 的“L1TF 的 stable 后向移植相对顺利，举 fd7e315988 化简 pgd_page 宏当初纯属清理、后被改作他用为例”，正是提交间隐式依赖的分合相位）
**辨析**：Jiri Kosina 的“问封闭安全问题该修补哪些内核（仅主线还是全部 stable），并询 Greg 过去是否真有因后向移植过难而放弃修复的情形”为待答之问，本页未见答复；Andy Lutomirski 的“论 Meltdown／Spectre 之困非流程之过而是被禁 sane 流程，少数非 Intel 上游开发者及时获知”为其归因判断；David Woodhouse 的“难以预料的依赖”为其个案结论。
**文献**：DSLXC-5838、DSLXC-5842、DSLXC-5859、DSLXC-5877（`ksummit-discuss.messages.349065`、`ksummit-discuss.messages.349069`、`ksummit-discuss.messages.349086`、`ksummit-discuss.messages.349104`，2018-09-07、2018-09-07、2018-09-07、2018-09-08），全文见 `raw_source.raw_json`

## 44.6 【Linux社区】staging/media、kernelci、arm-soc 拆分与 2014 档案四封（9 例）

**要点（判定表逐字）**：Olof Johansson 解释 arm-soc 拆分工作的规模动因——十余家厂商协调易成冲突泥潭，宁可多费工避免依赖、亦利于后向移植与 stable 修复；Mauro Carvalho Chehab 述 media 以 drivers/staging/media 加 MAINTAINERS 条目统管，举 atomisp 大驱动为例，建议按 N 个发布周期软性清除并设机器人监控；Mauro Carvalho Chehab 评 kernelci.org 将成 LF 项目，谓三分之一补丁为驱动、媒体 CI 需真实硬件（如摄像头），应与 CI 方商如何契合驱动子系统；Dave Airlie 答 Ted 之 Edinburgh 改址公告，戏称宁娶妻也不与 Linus 厮混，提议次年再办，并问 LPC 周一空档何用；Rafael J. Wysocki 问 Russell King 的通用依赖延期胶水（component.h）如何解系统挂起依赖，疑其仅解探测期依赖而非运行期 PM 依赖；Amit Kucheria 述其 idlestat 工具追踪 cpuidle／cpufreq 并报告各状态抵达率与平均驻留，正试验输出 idle 状态误预测以关联实际功耗，答 Preeti 的 target residency 动态设定之问；Lorenzo Pieralisi 论 target_residency 须以能量而非时间评估（属盈亏平衡点），ARM 上受脏缓存行、CPU 与内存频率等牵制，曾于 2013 Linaro Connect 宣讲；Dan Carpenter 愿就 Smatch 作技术轨道演讲，谈及静态检查；Dan Carpenter 论 make C=1 或可同时调用 sparse 与 smatch，自陈 Smatch 安装不佳、拟于峰会前修好

**史料**：`349080`、`349087`、`349088`、`349097`、`349101`、`349057`、`349068`、`349079`、`349090`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.349080 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349087 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349088 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349097 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349101 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349057 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349068 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349079 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349090 -->` 

**史观**：分离聚合是永恒规律（总纲第 4 条——分离聚合是永恒规律：Olof Johansson 的“arm-soc 拆分十余家厂商协调易成冲突泥潭，宁可多费工避免依赖、亦利于后向移植与 stable 修复”与 Mauro 的“media 以 drivers/staging/media 加 MAINTAINERS 条目统管、按 N 个发布周期软性清除”并置，正是子系统分合的相位）；一切真历史都是古代史（总纲第 1 条——一切真历史都是古代史：2014 年的 component.h 依赖延期、cpuidle 目标驻留、Smatch 技术轨道三线档案被 2018 年讨论重提，正见旧议题的当代性）
**辨析**：Dave Airlie 的“戏称宁娶妻也不与 Linus 厮混，提议次年再办”为当事人戏语，非史家判断；Rafael J. Wysocki 的“问 Russell King 的通用依赖延期胶水（component.h）如何解系统挂起依赖，疑其仅解探测期依赖而非运行期 PM 依赖”为待答之问；Lorenzo Pieralisi 的“论 target_residency 须以能量而非时间评估（属盈亏平衡点），ARM 上受脏缓存行、CPU 与内存频率等牵制”为其技术判词；Dan Carpenter 的“自陈 Smatch 安装不佳、拟于峰会前修好”为当事人自陈。本块含 2014 年档案四封，与 2018 年主线不同期，属跨期并置。
**文献**：DSLXC-5853、DSLXC-5860、DSLXC-5861、DSLXC-5870、DSLXC-5874、DSLXC-5830、DSLXC-5841、DSLXC-5852、DSLXC-5863（`ksummit-discuss.messages.349080`、`ksummit-discuss.messages.349087`、`ksummit-discuss.messages.349088`、`ksummit-discuss.messages.349097`、`ksummit-discuss.messages.349101`、`ksummit-discuss.messages.349057`、`ksummit-discuss.messages.349068`、`ksummit-discuss.messages.349079`、`ksummit-discuss.messages.349090`，2018-09-07、2018-09-07、2018-09-07、2018-09-07、2014-05-14、2014-05-14、2014-05-14、2014-05-14、2014-05-14），全文见 `raw_source.raw_json`

---
注：本文件由判定表程序化生成（6 块，覆盖 50/50 CAND，两遍计数核对通过）；要点逐字取自判定表“要点”列（主代理全读审读实录），史料锚与 CAND 一一对应，全文以 raw_source.raw_json 为准。
