# 41 【Linux社区】AUTOSEL焦虑与lockdown议题

> 对应页面：ksummit-discuss p94（pk 348906-348955，2018 AUTOSEL/staging/lockdown 多线程 + 2014 档案信）
> 判定：50 CAND / 0 NV
> 编号：DSLXC-5681..5730 | claim 已入库（50/50，dslinux_claims.duckdb）

## 41.1 【Linux社区】AUTOSEL 焦虑与 opt-in／opt-out 之争（9 例）

**要点（判定表逐字）**：Steven Rostedt 谈 stable 标注：有些修复因多年既存缺陷且无人注意而未打 stable 标签，另有仅令代码更健壮的症状修复不宜回退；并评 Sasha 的 AUTOSEL 抓到的多属噪声，维护者当自行权衡；Takashi Iwai 主张 AUTOSEL 按树 opt-in 与 opt-out：其树中被 AUTOSEL 抓到的多是故意留而未标 stable 的改动，望改为需人工批准才并入；并问能否延后合并以待发布后更多测试；Mark Brown 直言 AUTOSEL 神经网拣选令其焦虑：多数补丁只是大概没问题，若真认为该进 stable 他早标了；流程上难再改进，因明确有益者他已自行标记；Sasha Levin 解释 stable 滞后上游数周：若等发布后满一月相关 stable 树已 EOL；戏称 Greg 的激进排期下自己只是勉力跟上；Sasha Levin 答 Mark Brown：AUTOSEL 对标注良好的维护者似噪声，对从不标 stable 的维护者则包办全部；并谓维护者大体已在权衡，stable 少有无谓补丁；Sasha Levin 提 stable-next 构想：把已标 stable 的提交立入 stable-next 分支供冒险者先测；末附玩笑补丁把 4.19-rc1 的 NAME 改为 Microsoft Linux；Takashi Iwai 问 Sasha：等上游合并满一月对 LTS 仍有益（普通 stable 可不要此类不急修复，LTS 确认稳定后再推）；Daniel Vetter 赞 AUTOSEL opt-in，并要更清晰审计路径（每补丁记原因）；举 drm/atomic 提交 c81350c 无 cc stable 却入 stable 后炸开的实例，怪 drm committer 漏维护者；Sasha Levin 答 Daniel：入其树者仅 AUTOSEL；反举 Hang Yuan 的 drm/i915/gvt 清理序列 oops 修复（Fixes bc7b0be、afe04fbe）未标亦未入 stable 作对照

**史料**：`348906`、`348907`、`348908`、`348909`、`348911`、`348915`、`348916`、`348926`、`348927`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348906 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348907 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348908 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348909 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348911 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348915 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348916 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348926 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348927 -->` 

**史观**：不存在进步，只有权力再分配（总纲第 3 条——不存在进步，只有权力再分配：Takashi Iwai 的“依树 opt-in／opt-out、需人工批准才并入”与 Sasha Levin 的“对从不标 stable 的维护者则包办全部”之争，实为自动拣选权与子系统判断权的再分配）；经验优先（总纲第 9 条——经验优先：以 drm/atomic 提交 c81350c 无 cc stable 却入 stable 后炸开、Hang Yuan 的 drm/i915/gvt 清理序列 oops 修复（Fixes bc7b0be、afe04fbe）未标亦未入 stable 两实例为判据）
**辨析**：Mark Brown 的“AUTOSEL 神经网拣选令其焦虑，多数补丁只是大概没问题，若真认为该进 stable 他早标了”为当事人自陈；Steven Rostedt 的“Sasha 的 AUTOSEL 抓到的多属噪声，维护者当自行权衡”为其判断；Sasha Levin 的“stable 滞后上游数周，若等发布后满一月相关 stable 树已 EOL”为流程约束之陈；Daniel Vetter 的“怪 drm committer 漏维护者”为归因主张，与 Levin 的反举证对置，本页未见裁断。
**文献**：DSLXC-5681、DSLXC-5682、DSLXC-5683、DSLXC-5684、DSLXC-5686、DSLXC-5690、DSLXC-5691、DSLXC-5701、DSLXC-5702（`ksummit-discuss.messages.348906`、`ksummit-discuss.messages.348907`、`ksummit-discuss.messages.348908`、`ksummit-discuss.messages.348909`、`ksummit-discuss.messages.348911`、`ksummit-discuss.messages.348915`、`ksummit-discuss.messages.348916`、`ksummit-discuss.messages.348926`、`ksummit-discuss.messages.348927`，2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05），全文见 `raw_source.raw_json`

## 41.2 【Linux社区】stable 节奏、EOL 与 backport 之辩（10 例）

**要点（判定表逐字）**：Mark Brown 答 Greg：arm32 回退确有用心，只缺人做老内核（尤 arm64 更活跃）的 backport；谓后续会有进展；Steven Rostedt 论 Stable Kernel ABI 商业模式：付钱做老内核 backport 的是厂商而非发行版，删去此苦活或令厂商不再雇这些高手；维稳靠这笔钱反哺上游；Thomas Gleixner 答 Sasha：临近 EOL 的树本就既拿不到下一补丁也拿不到微妙破损的修复，等一月无意义；Sasha Levin 答 tglx：内核约两月一发、stable 在新内核发后一两周 EOL，若等一月将忽略约半个发布周期（尤 -rc 期补丁更多）；Steven Rostedt 答 Paul：rebase stable 会破坏 RT stable 树流程，不推荐；对提升 bisect 性存疑（rebase 后原可用树不再存在）；Guenter Roeck 论 stable 节奏：chromeos-4.4 在 v4.4.y 上叠一万五千余补丁，每发补丁更多则冲突风险升；宁偶漏发也不要更长 -rc 周期；Paul McKenney 答 Steve：rebase 是把修复折进原缺陷提交（而非留缺陷区间），并笑言 rebase stable 必碎一地玻璃；指这是权衡取舍；James Bottomley 戴 PA-RISC 帽为 4.18.5 中两内存序补丁辩护：维护者信其修 debian parisc 端口受阻的段错误，符合标准；Dmitry Torokhov 建议不稳定处加说明为何标 stable：维护者常 trigger happy 标新硬件支持或未必触发的错误处理；标 stable 比事后送 stable 省力致滥用；Steven Rostedt 追问 Bottomley：那两 parisc 补丁 changelog 只提性能提升、未提段错误，信息是否曾 embargo；疑其不符 stable 标准

**史料**：`348914`、`348918`、`348919`、`348920`、`348925`、`348928`、`348929`、`348933`、`348939`、`348940`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348914 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348918 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348919 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348920 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348925 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348928 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348929 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348933 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348939 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348940 -->` 

**史观**：不存在进步，只有权力再分配（总纲第 3 条——不存在进步，只有权力再分配：Thomas Gleixner 的“临近 EOL 的树等一月无意义”与 Sasha Levin 的“等一月将忽略约半个发布周期”同向，与 Guenter Roeck 的“宁偶漏发也不要更长 -rc 周期”相对，实为发布节奏与 EOL 时限决定权的再分配）；分离聚合是永恒规律（总纲第 4 条——分离聚合是永恒规律：rebase 把修复折进原缺陷提交与保留缺陷区间两种做法之争，正是提交史分合的相位）
**辨析**：Paul McKenney 的“rebase 是把修复折进原缺陷提交（而非留缺陷区间）”“笑言 rebase stable 必碎一地玻璃”“指这是权衡取舍”为其方法论判词；Steven Rostedt 的“rebase stable 会破坏 RT stable 树流程，不推荐”“对提升 bisect 性存疑（rebase 后原可用树不再存在）”为反方经验；James Bottomley 的“戴 PA-RISC 帽为 4.18.5 中两内存序补丁辩护，符合标准”与 Steven Rostedt 的“changelog 只提性能提升、未提段错误，信息是否曾 embargo”对撞，未作单方裁断。
**文献**：DSLXC-5689、DSLXC-5693、DSLXC-5694、DSLXC-5695、DSLXC-5700、DSLXC-5703、DSLXC-5704、DSLXC-5708、DSLXC-5714、DSLXC-5715（`ksummit-discuss.messages.348914`、`ksummit-discuss.messages.348918`、`ksummit-discuss.messages.348919`、`ksummit-discuss.messages.348920`、`ksummit-discuss.messages.348925`、`ksummit-discuss.messages.348928`、`ksummit-discuss.messages.348929`、`ksummit-discuss.messages.348933`、`ksummit-discuss.messages.348939`、`ksummit-discuss.messages.348940`，2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05），全文见 `raw_source.raw_json`

## 41.3 【Linux社区】发行版 bugzilla 与 bisect 自动化（8 例）

**要点（判定表逐字）**：Paul McKenney 谈发行版 bugzilla：自己靠 rebase 提升 bisect 性，提议自动化从 git bisect 到内核包以助人二分；并指加工具或能改善但非易事；Sasha Levin 答 Konstantin：KernelCI 已在做自动二分，加简易测试用例即可成 bisect@home；Konstantin 此前提 seti@home 式志愿机群二分构想；Laura Abbott 谈 Fedora 二分脚本：曾试但因脆弱废弃；非内核开发者常卡于构建二分，设想用现有打包目标加 COPR，惜缺资源与网页框架；Paul McKenney 答 James：自己用日期分支保留旧提交约半年以兼顾 rebase 与下游；笑言若基于两年前 -rcu 分支开发问题更大；Laura Abbott 续发行版 bugzilla：鼓励上报与二分常遇阻（本地机慢、缺测试用例、惮构建内核）；曾起 get_maintainer.pl 网页雏形未竟；Laura Abbott 答 Greg：specdown 风暴前已现此模式，疑为新常态才提议题；不在乎补丁数多寡，含头条 bug 的 stable 另处处理；Konstantin Ryabitsev 谈 kernelci.org 将成 LF 正式项目、有望资 bisect@home 类开发；并释 kernel.org 非营利定位限于免费分发内核；Takashi Iwai 答 Konstantin：乐见 kernelci 承 bisect@home 构想，谢其把二分即服务列入未来内核 CI 建议

**史料**：`348913`、`348917`、`348934`、`348938`、`348941`、`348942`、`348950`、`348954`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348913 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348917 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348934 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348938 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348941 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348942 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348950 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348954 -->` 

**史观**：动手者创造历史（总纲第 10 条——动手者创造历史：以 Paul McKenney 的“自动化从 git bisect 到内核包”、Laura Abbott 的 Fedora 二分脚本与 get_maintainer.pl 网页雏形、Konstantin Ryabitsev 的 bisect@home 为分析单位）；经验优先（总纲第 9 条——经验优先：以 Laura Abbott 的“曾试但因脆弱废弃”“非内核开发者常卡于构建二分”“本地机慢、缺测试用例、惮构建内核”为判据）
**辨析**：Laura Abbott 的“specdown 风暴前已现此模式，疑为新常态才提议题”“不在乎补丁数多寡，含头条 bug 的 stable 另处处理”为当事人自陈；Konstantin Ryabitsev 的“kernel.org 非营利定位限于免费分发内核”为组织约束之陈；Paul McKenney 的“用日期分支保留旧提交约半年以兼顾 rebase 与下游”为其实践自述。各说并置，未决。
**文献**：DSLXC-5688、DSLXC-5692、DSLXC-5709、DSLXC-5713、DSLXC-5716、DSLXC-5717、DSLXC-5725、DSLXC-5729（`ksummit-discuss.messages.348913`、`ksummit-discuss.messages.348917`、`ksummit-discuss.messages.348934`、`ksummit-discuss.messages.348938`、`ksummit-discuss.messages.348941`、`ksummit-discuss.messages.348942`、`ksummit-discuss.messages.348950`、`ksummit-discuss.messages.348954`，2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05），全文见 `raw_source.raw_json`

## 41.4 【Linux社区】staging 退出之争与 MAINTAINERS 缺口（8 例）

**要点（判定表逐字）**：Shuah Khan 指 MAINTAINERS 中部分 staging 条目缺子系统邮件列表（如 FBTFT 帧缓冲驱动仅列 Thomas Petazzoni 无 L），建议补 L 或 linux-kernel 以便清理时相关维护者知情；Andrew Lunn 指 staging 与 netdev 零互动：首见多为 git format-patch -M 重命名致难审真码；建议文档补如何毕业出 staging、何时拉目标子系统评审；Daniel Vetter 评 vboxvideo：staging 对 drm 不合适，三年并了 2-3 个 atomic 驱动，vboxvideo 满一年仍只做重构、无人做 atomic 转换；同意移除；James Bottomley 主张子系统可整体退出 staging：SCSI 要看实质命令交互，小白格清理数月无益；polishing 不该服务于此；Daniel Vetter 附议 Bottomley 退出 staging：drm 宁可直收违反半数 checkpatch 的新驱动，只要跟最新 drm 助手与概念；打磨留待基础扎实后，并指 Documentation/gpu/todo.rst；James Bottomley 答 Paul：SCSI 也做 folding（树未交 Linus 前把修复折进缺陷提交）以利 bisect；rebase 若下游依赖则需协调但非不可能；Jiri Kosina 答 James：scsi.git 是其上游之一，rebase 会炸其 git 工作流需手动修；提醒知树有下游则勿 rebase（引 yarchive 文）；James Bottomley 答 Jiri：scsi 树类 linux-next 可更新，望了解下游情形后定可行工作流；此前不知 scsi.git 被当上游

**史料**：`348910`、`348921`、`348922`、`348930`、`348932`、`348936`、`348944`、`348947`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348910 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348921 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348922 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348930 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348932 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348936 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348944 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348947 -->` 

**史观**：分离聚合是永恒规律（总纲第 4 条——分离聚合是永恒规律：staging 驱动的毕业与整体退出、vboxvideo 满一年仍只做重构、SCSI 主张整体退出 staging，正是暂存树与子系统之间的分合相位）；本体论上各方平等（总纲第 8 条——本体论上各方平等：James Bottomley 的“子系统可整体退出 staging、polishing 不该服务于此”与 Daniel Vetter 的“drm 宁可直收违反半数 checkpatch 的新驱动”同向，与 Shuah Khan、Andrew Lunn 的“补 L 标签、补毕业文档”之程序主张并置）
**辨析**：Shuah Khan 的“MAINTAINERS 中部分 staging 条目缺子系统邮件列表（如 FBTFT 仅列 Thomas Petazzoni 无 L）”为可核查之实况；Andrew Lunn 的“首见多为 git format-patch -M 重命名致难审真码”为其经验归因；Jiri Kosina 的“scsi.git 是其上游之一，rebase 会炸其 git 工作流需手动修”与 Bottomley 的“此前不知 scsi.git 被当上游”相对，属当事人间的事实澄清，未上升为通则。
**文献**：DSLXC-5685、DSLXC-5696、DSLXC-5697、DSLXC-5705、DSLXC-5707、DSLXC-5711、DSLXC-5719、DSLXC-5722（`ksummit-discuss.messages.348910`、`ksummit-discuss.messages.348921`、`ksummit-discuss.messages.348922`、`ksummit-discuss.messages.348930`、`ksummit-discuss.messages.348932`、`ksummit-discuss.messages.348936`、`ksummit-discuss.messages.348944`、`ksummit-discuss.messages.348947`，2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05），全文见 `raw_source.raw_json`

## 41.5 【Linux社区】lockdown 与 secure boot 议题（6 例）

**要点（判定表逐字）**：David Howells 提议 TECH TOPIC：推进 secure boot 与 kernel lockdown 补丁，称多发行版已在自带该补丁集；Jiri Kosina 答 David：SUSE 是少数自带非上游 lockdown 补丁集者之一，自承已忘究竟何阻塞上游合并；Justin Forbes 答 Jiri：lockdown 应与 secure boot 分离成独立 config，并指当前 lockdown 一刀切禁用 BPF 伤及 IPAddressAllow/IPAddressDeny；David Howells 答 Justin：补丁集已有 CONFIG_LOCK_DOWN_IN_EFI_SECURE_BOOT；疑点之一是 Linus 似要编译期全锁或全不锁、而非启动期条件；Justin Forbes 续谈 lockdown config：上次推送有 CONFIG_LOCK_DOWN_MANDATORY 与 lockdown=1，独缺 UEFI 触发项；作为发行版跑 MANDATORY 不可行，曾用 4.17 rawhide 跑 KERNEL 无人觉 secure boot 关；Andy Lutomirski 评 lockdown 不必占整 TECH TOPIC：阻塞点一为启用时机、二为作用范围；主张拆小补丁集先并基础框架与一个用户，再逐个加 lockdown 用户，并提 LOCKDOWN_PROTECT_INTEGRITY/SECRECY 分级

**史料**：`348937`、`348945`、`348948`、`348949`、`348953`、`348955`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348937 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348945 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348948 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348949 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348953 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348955 -->` 

**史观**：法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：secure boot 与 kernel lockdown 的补丁之争，实为发行版合规义务与内核可配置边界的利益划分）；分离聚合是永恒规律（总纲第 4 条——分离聚合是永恒规律：Andy Lutomirski 的“拆小补丁集先并基础框架与一个用户，再逐个加 lockdown 用户”与 Justin Forbes 的“lockdown 应与 secure boot 分离成独立 config”同向，正是补丁集分合的相位）
**辨析**：Jiri Kosina 的“SUSE 是少数自带非上游 lockdown 补丁集者之一，自承已忘究竟何阻塞上游合并”为当事人自陈；David Howells 的“疑点之一是 Linus 似要编译期全锁或全不锁、而非启动期条件”为转述他人立场，非其自定；Justin Forbes 的“作为发行版跑 MANDATORY 不可行，曾用 4.17 rawhide 跑 KERNEL 无人觉 secure boot 关”为其实测经验。阻塞点之判（启用时机、作用范围）由 Lutomirski 提出，本页未见决议。
**文献**：DSLXC-5712、DSLXC-5720、DSLXC-5723、DSLXC-5724、DSLXC-5728、DSLXC-5730（`ksummit-discuss.messages.348937`、`ksummit-discuss.messages.348945`、`ksummit-discuss.messages.348948`、`ksummit-discuss.messages.348949`、`ksummit-discuss.messages.348953`、`ksummit-discuss.messages.348955`，2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05），全文见 `raw_source.raw_json`

## 41.6 【Linux社区】AUTOSEL 之辩续与 2014 档案五封（9 例）

**要点（判定表逐字）**：Daniel Vetter 续答 Sasha：所举 gvt 提交非 stable 材料（仅修开发者用的驱动卸载 bug，且需 CONFIG_EXPERT 与测试脚本方能复现）；Sasha Levin 续与 Daniel 辩 gvt/i915 卸载：在 Ubuntu 4.18 上 echo remove 后 rmmod i915 即可，质疑 Daniel 所谓需 CONFIG_EXPERT 方能复现之说；Sasha Levin 示 rmmod i915 后果：在 Ubuntu 4.18 上 echo remove 后 rmmod 触发 PCH DPLL A 断言失败 WARN 并挂起（Lenovo 4236AT9），证 Daniel 所称需 CONFIG_EXPERT 不实；Daniel Vetter 答 Sasha：强拔设备才弄挂机器，无此则连 rmmod 都不行；修 i915 加 drm core 引用计数或需数年人力，重申非 stable 材料；（2014 档案）Benjamin Herrenschmidt 荐 IBM 的 Gavin Shan 为 EEH 专家，介绍 PowerPC PCI 主桥检测错误并冻结设备、对支持钩子的驱动走恢复流程、否则模拟解绑重置再绑的作法；（2014 档案）Jan Kara 论 stable 工作流：维护者或作者加 CC stable 自动流入，与维护者建 for-stable 分支发 pull 实质无别；多级维护树下顶层控制力弱；（2014 档案）Benjamin Herrenschmidt 续设备错误处理：PowerPC EEH 已有驱动钩子、ACPI/AER 复用同一套；提醒勿轻视廉价无 ECC 总线上随机位翻转的硬件误报；（2014 档案）Masami Hiramatsu 论 stable 测试：建议 MAINTAINERS 加 UT/TS 标签指明测法；Rostedt 的 ftrace 测试因需 root 不合 selftests 规则，拟放 tools/testing/tracing 或送 LTP；（2014 档案）Li Zefan 答 Chris Mason：若回归由新 config 新特性引入则难称严格意义回归；疑少数 .config 项即可导致 10-30% 性能回退

**史料**：`348931`、`348943`、`348951`、`348952`、`348912`、`348923`、`348924`、`348935`、`348946`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348931 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348943 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348951 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348952 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348912 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348923 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348924 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348935 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348946 -->` 

**史观**：一切真历史都是古代史（总纲第 1 条——一切真历史都是古代史：2014 年的 EEH 设备错误处理、stable 工作流、stable 测试、回归定义四线档案被 2018 年讨论重提，正见旧议题的当代性）；经验优先（总纲第 9 条——经验优先：以 Sasha Levin 的“在 Ubuntu 4.18 上 echo remove 后 rmmod i915 即可”“rmmod 触发 PCH DPLL A 断言失败 WARN 并挂起（Lenovo 4236AT9）”为判据）
**辨析**：Sasha Levin 的“示 rmmod i915 后果”为可复现实测之陈，与 Daniel Vetter 的“强拔设备才弄挂机器，无此则连 rmmod 都不行”相对，两造对同一现象的解释不同，未作单方裁断；Daniel Vetter 的“修 i915 加 drm core 引用计数或需数年人力”为其代价估计；本块后五封为 2014 年档案，与 2018 年主线不同期，属跨期并置。
**文献**：DSLXC-5706、DSLXC-5718、DSLXC-5726、DSLXC-5727、DSLXC-5687、DSLXC-5698、DSLXC-5699、DSLXC-5710、DSLXC-5721（`ksummit-discuss.messages.348931`、`ksummit-discuss.messages.348943`、`ksummit-discuss.messages.348951`、`ksummit-discuss.messages.348952`、`ksummit-discuss.messages.348912`、`ksummit-discuss.messages.348923`、`ksummit-discuss.messages.348924`、`ksummit-discuss.messages.348935`、`ksummit-discuss.messages.348946`，2018-09-05、2018-09-05、2018-09-05、2018-09-05、2014-05-14、2014-05-02、2014-05-14、2014-05-14、2014-05-14），全文见 `raw_source.raw_json`

---
注：本文件由判定表程序化生成（6 块，覆盖 50/50 CAND，两遍计数核对通过）；要点逐字取自判定表“要点”列（主代理全读审读实录），史料锚与 CAND 一一对应，全文以 raw_source.raw_json 为准。
