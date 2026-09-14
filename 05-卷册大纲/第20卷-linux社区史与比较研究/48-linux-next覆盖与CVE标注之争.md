# 48 【Linux社区】linux-next覆盖与CVE标注之争

> 对应页面：ksummit-discuss p101（pk 349256-349305，2018 linux-next 覆盖/CVE 标注/社区治理多线程 + 2014 档案信）
> 判定：50 CAND / 0 NV
> 编号：DSLXC-6029..6078 | claim 已入库（50/50，dslinux_claims.duckdb）

## 48.1 【Linux社区】embargo 协调组与 CVE 标注之争（11 例）

**要点（判定表逐字）**：Greg KH 问 Eduardo：在 embargo 约束下本可做得更好之处；开启维护者峰会安全 embargo 讨论的追问；Greg KH 答 Dave Hansen：LF 每年有法律人会分享非 NDA 方法（依 Chatham House 规则），欢迎 Intel 向该组演示其 embargo 处理经验；Thomas Gleixner 谈 embargo 协调：Greg KH 因非披露方雇员、无 NDA 致耗时近两月才入伙；对无雇主覆盖者只能放弃；主张由 embargo 团队基于信任与技术必要引入外人，泄密即毁社区声誉；Justin Forbes 论 CVE 补丁标注：保密期前先修可不显安全问题，混淆有时有益；宁可先合入再标注；提议作者于公开后补摘要；Takashi Iwai 论 CVE 标注：曾寄望 git-notes 作发布后附注，但因分享困难等未成；延续 CVE 跟踪讨论；Greg KH 论 CVE 标注：忆及某 github 树跟踪 CVE 与提交但难维持；主因 CVE 多在补丁入树后才分配、无法改 changelog；自陈 CVEs are a joke 之感；Dan Carpenter 论 CVE 标注：忆 Eugene Teo 曾维护 CVE 与提交跟踪树，建议直接用 Ubuntu break/fix CVE 列表（launchpad）；Takashi Iwai 论 CVE 标注：git-notes 恰可事后向提交加注 CVE 号并搜于命名空间，亦可用于 Fixes 标签反查；但分享难、扩展性有限，附和 Greg 之 CVEs are a joke；Leon Romanovsky 论 CVE 标注：指法律合同迫使 HW 厂商先于公开向客户交付修复，标注 CVE 将令其延迟所有补丁，现行法律反允静默修复；Greg KH 答 Leon：此乃永不强制标注的又一理由，谢其提出；延续 CVE 流程之辩；Dave Hansen 论 embargo 安全：建议书面记录不可走 security@ 的提交流程、载明 stable 须牵 stable 维护者与时限；指书面流程代表社区分量、时间表给各方具体行动日

**史料**：`349261`、`349262`、`349264`、`349280`、`349281`、`349283`、`349285`、`349286`、`349287`、`349288`、`349297`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.349261 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349262 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349264 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349280 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349281 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349283 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349285 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349286 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349287 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349288 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349297 -->` 

**史观**：法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：Leon Romanovsky 的“指法律合同迫使 HW 厂商先于公开向客户交付修复，标注 CVE 将令其延迟所有补丁，现行法律反允静默修复”与 Greg KH 的“此乃永不强制标注的又一理由”对撞，实为披露义务与交付义务的利益划分）；本体论上各方平等（总纲第 8 条——本体论上各方平等：Justin Forbes 的“保密期前先修可不显安全问题，混淆有时有益；宁可先合入再标注”与 Takashi Iwai 的“曾寄望 git-notes 作发布后附注”、Dan Carpenter 的“建议直接用 Ubuntu break/fix CVE 列表”并置，未替任一方定论）
**辨析**：Greg KH 的“自陈 CVEs are a joke 之感”“忆及某 github 树跟踪 CVE 与提交但难维持；主因 CVE 多在补丁入树后才分配、无法改 changelog”为当事人自陈；Thomas Gleixner 的“Greg KH 因非披露方雇员、无 NDA 致耗时近两月才入伙；对无雇主覆盖者只能放弃；主张由 embargo 团队基于信任与技术必要引入外人，泄密即毁社区声誉”为其顶层判词；Dave Hansen 的“建议书面记录不可走 security@ 的提交流程、载明 stable 须牵 stable 维护者与时限”为其机制提案。两造未作单方裁断。
**文献**：DSLXC-6034、DSLXC-6035、DSLXC-6037、DSLXC-6053、DSLXC-6054、DSLXC-6056、DSLXC-6058、DSLXC-6059、DSLXC-6060、DSLXC-6061、DSLXC-6070（`ksummit-discuss.messages.349261`、`ksummit-discuss.messages.349262`、`ksummit-discuss.messages.349264`、`ksummit-discuss.messages.349280`、`ksummit-discuss.messages.349281`、`ksummit-discuss.messages.349283`、`ksummit-discuss.messages.349285`、`ksummit-discuss.messages.349286`、`ksummit-discuss.messages.349287`、`ksummit-discuss.messages.349288`、`ksummit-discuss.messages.349297`，2018-09-11、2018-09-11、2018-09-11、2018-09-11、2018-09-11、2018-09-11、2018-09-11、2018-09-11、2018-09-11、2018-09-11、2018-09-11），全文见 `raw_source.raw_json`

## 48.2 【Linux社区】linux-next 覆盖与测试者处境（10 例）

**要点（判定表逐字）**：Mark Brown 论引入 bug 的补丁：以 -next 构建（135 中 2 失败）与 qemu（315 中 203 失败）数据质疑回归测试可行；指持续报告可改善（如构建错误历数年改善），并引 kernelci 当日仅四构建失败；Steven Rostedt 论引入 bug 的补丁：收回 Linus 应发飙之说，主张对推未测代码入 -next 者须有后果，最低门槛是通过 0day bot，否则不配做维护者；Guenter Roeck 答 Stephen Rothwell：-next 不可用或因 mount api 改动，未及 bisect 故未报此具体失败；延续引入 bug 补丁讨论；Guenter Roeck 答 Mark：因被人指责制造噪声而基本停报 -next 问题（分支甚至不在 -next），须有共识不斥测试者；指崩溃发生于重启或断电卸载根文件系统时，除 arm 外多数架构可见；Jani Nikula 答 Guenter：困惑为何不把子系统或驱动全部分支（含修复）都纳入 linux-next；James Bottomley 答 Guenter：不姑息无礼，但 -next 在澳洲时区构建、修复传播至多 24 小时，致同 bug 被多项目重复报告；建议跟踪项目设协调列表避免五重报告；Mark Brown 答 Guenter：认同不应斥测试者，尤当扰乱集成树测试；指 KernelCI 启动测试仅到提示符即断电，故不见重启崩溃；Mark Brown 答 Jani：有人仅 QA 通过后才入 -next（如 Steven 的 0day 流程），故可见入 -next 前于 git 中受 QA 之分支；Linus Torvalds 论引入 bug 补丁：自认仅借 -next 估量待入量、偶尔核对边际拉取，不日常跟踪；主张追踪失败并告之，持久失败则不拉，须定位到具体 -next 拉取；Tony Lindgren 答 Rostedt：所遇诸多 -next 回归本可因 Andrew mm 树先行更多测试而免（其排队复杂补丁）；建议设入 -next 前约 24 小时窗口供自动系统测试

**史料**：`349276`、`349293`、`349295`、`349296`、`349298`、`349299`、`349300`、`349303`、`349304`、`349305`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.349276 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349293 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349295 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349296 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349298 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349299 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349300 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349303 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349304 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349305 -->` 

**史观**：本体论上各方平等（总纲第 8 条——本体论上各方平等：Steven Rostedt 的“主张对推未测代码入 -next 者须有后果，最低门槛是通过 0day bot，否则不配做维护者”与 Guenter Roeck 的“因被人指责制造噪声而基本停报 -next 问题，须有共识不斥测试者”对撞，未替任一方定论）；经验优先（总纲第 9 条——经验优先：以 Mark Brown 引的“-next 构建（135 中 2 失败）与 qemu（315 中 203 失败）数据”“kernelci 当日仅四构建失败”为判据）
**辨析**：Steven Rostedt 的“收回 Linus 应发飙之说”为当事人自反留痕；Guenter Roeck 的“指崩溃发生于重启或断电卸载根文件系统时，除 arm 外多数架构可见”为技术实况；James Bottomley 的“不姑息无礼，但 -next 在澳洲时区构建、修复传播至多 24 小时，致同 bug 被多项目重复报告”为机制归因，其“建议跟踪项目设协调列表避免五重报告”为对策；Linus Torvalds 的“自认仅借 -next 估量待入量、偶尔核对边际拉取，不日常跟踪；主张追踪失败并告之，持久失败则不拉，须定位到具体 -next 拉取”为其流程判词。
**文献**：DSLXC-6049、DSLXC-6066、DSLXC-6068、DSLXC-6069、DSLXC-6071、DSLXC-6072、DSLXC-6073、DSLXC-6076、DSLXC-6077、DSLXC-6078（`ksummit-discuss.messages.349276`、`ksummit-discuss.messages.349293`、`ksummit-discuss.messages.349295`、`ksummit-discuss.messages.349296`、`ksummit-discuss.messages.349298`、`ksummit-discuss.messages.349299`、`ksummit-discuss.messages.349300`、`ksummit-discuss.messages.349303`、`ksummit-discuss.messages.349304`、`ksummit-discuss.messages.349305`，2018-09-11、2018-09-11、2018-09-11、2018-09-11、2018-09-11、2018-09-11、2018-09-11、2018-09-11、2018-09-11、2018-09-11），全文见 `raw_source.raw_json`

## 48.3 【Linux社区】社区治理：MAINTAINERS、沟通系统与 ARM patch system（11 例）

**要点（判定表逐字）**：Jani Nikula 论社区治理：MAINTAINERS 应是流程信息中央库，维护者应主动更新各自偏好与期望（如是否看 bugzilla），可用 W 字段链接细节或增条目，而非事后随意斥责贡献者；Rafael 论内核协作通信：赞同 Laurent 对邮件系统的三点要求（推送式、可脚本化、离线），评 Konstantin 提出的 pagure.io（基于 gitolite、ssh/email 可用、无社区版商业版分裂），并指出中央 issue 跟踪须有人充当指派人；Jani Nikula 澄清：dim 工具仅当成为用 dim 维护之树的提交者或维护者时才需用，普通贡献者不必；纠正 Laurent 对 DRM dim 与 ARM patch system 的混淆；Geert 论旧硬件移除：仍以 gcc-4.1.2 构建主线（revert 两提交抬最低 gcc 至 4.6），附三处 lore 链接的修复与改进；回应 unicore32 因私有旧工具链（gcc 小于 4.6）不再构建、或应重议去留；Geert 答 Jani：ARM patch system 不像 dim 那般可免用；延续社区治理工具差异讨论；Daniel Vetter 问 Geert：ARM patch system 有无文档或链接，自称此前从未耳闻；延续治理工具差异讨论；Leon Romanovsky 论邮件评审的教化价值：公开 review 是众人可学的教材，gerrit 类工具偏好一对一；以被迫用内部 gerrit 与跨 netdev/RDMA 提交之苦佐证多工具世界之难；Geert 答 Daniel：给出 arm.linux.org.uk/developer/patches 链接，指出其仅收合规则的 git-send-email 补丁，并发现 Documentation/arm/README 仍过时（2.6、FTP）；Daniel Vetter 评 ARM patch system：本质系 patchwork 思路的另一种实现（或早于之），差别在较不宽容、不自动读取邮件列表；延续治理讨论；Geert 答 Daniel：确认 ARM patch system 仅面向已审阅补丁，非通用队列；延续治理工具讨论；Mark Brown 论旧硬件移除：稳定内核的维系思路亦被应用于设计求稳硬件（既好用何必冒新险）；回应 Linus Walleij 之 velocitate（速度盲）观察

**史料**：`349258`、`349259`、`349260`、`349263`、`349265`、`349269`、`349270`、`349271`、`349272`、`349273`、`349274`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.349258 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349259 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349260 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349263 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349265 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349269 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349270 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349271 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349272 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349273 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349274 -->` 

**史观**：本体论上各方平等（总纲第 8 条——本体论上各方平等：Jani Nikula 的“MAINTAINERS 应是流程信息中央库，维护者应主动更新各自偏好与期望，而非事后随意斥责贡献者”与 Leon Romanovsky 的“公开 review 是众人可学的教材，gerrit 类工具偏好一对一”并置，未替任一方定论）；知识注定过时（总纲第 22 条——知识注定过时：Geert 的“发现 Documentation/arm/README 仍过时（2.6、FTP）”、Daniel Vetter 的“自称此前从未耳闻 ARM patch system”，正是流程知识在代际间散失之证）
**辨析**：Rafael 的“赞同 Laurent 对邮件系统的三点要求（推送式、可脚本化、离线），评 Konstantin 提出的 pagure.io，并指出中央 issue 跟踪须有人充当指派人”为其判断；Daniel Vetter 的“评 ARM patch system：本质系 patchwork 思路的另一种实现（或早于之），差别在较不宽容、不自动读取邮件列表”与 Geert 的“确认 ARM patch system 仅面向已审阅补丁，非通用队列”构成往复，后者为事实澄清；Mark Brown 的“论旧硬件移除：稳定内核的维系思路亦被应用于设计求稳硬件（既好用何必冒新险）”为其观察。
**文献**：DSLXC-6031、DSLXC-6032、DSLXC-6033、DSLXC-6036、DSLXC-6038、DSLXC-6042、DSLXC-6043、DSLXC-6044、DSLXC-6045、DSLXC-6046、DSLXC-6047（`ksummit-discuss.messages.349258`、`ksummit-discuss.messages.349259`、`ksummit-discuss.messages.349260`、`ksummit-discuss.messages.349263`、`ksummit-discuss.messages.349265`、`ksummit-discuss.messages.349269`、`ksummit-discuss.messages.349270`、`ksummit-discuss.messages.349271`、`ksummit-discuss.messages.349272`、`ksummit-discuss.messages.349273`、`ksummit-discuss.messages.349274`，2018-09-11、2018-09-11、2018-09-11、2018-09-11、2018-09-11、2018-09-11、2018-09-11、2018-09-11、2018-09-11、2018-09-11、2018-09-11），全文见 `raw_source.raw_json`

## 48.4 【Linux社区】staging、trivial 树与旧硬件移除（10 例）

**要点（判定表逐字）**：Greg KH 谈 staging：atomisp 由 Intel 推入后遭弃置致从内核剔除，谦称此乃流程正常运作；阐明 Free Linux Driver 项目与 staging 仍活跃，被弃代码可 git revert 取回；Linus Walleij 论旧硬件移除：以 MOXA ART（Faraday IP、ARMv4 FA526）为例，指其 ventilation 与 Liebherr 液压系统仍活跃部署，移除升级能力实为不负责任；并揣测 ASIC 团队为保持技能而翻新；Arnd Bergmann 论旧硬件移除：各平台终将被移除，但加平台时应记录约束以便多年后寻用户；论产品两模型（追新内核与定居 SLTS），指出 y2038/Spectre 类事件迫使升级，怀疑 18 至 20 年安全软件自然上限；Alexandre Belloni 论社区治理：rtc/codec/IIO/power-supply/hwmon 等常有路人不经意贡献，初始配置门槛过高；强调非大公司支撑的子系统无法与 drm 类等同期待；Mark Brown 答 Belloni：认同路人不经意贡献之忧，亦指跨多 gitlab 实例会添内核级难题；即便有公司支撑者亦常费力争取提交时间，削弱 CI 收益；Daniel Vetter 答 Belloni：drm 亦有小型树与路人贡献之痛；列合并成三头维护（百补丁每周期为下限、三维护者理想）、有意弃置、平滑晋升、谈维护者等手法；以 rtc 贡献统计（Belloni 241 居首）示倾斜不可持续；Alexandre Belloni 答 Mark：常有人基于某旧 vendor 树特定内核版本让驱动工作，无法要求其测更新内核；宁可不高提交门槛，但重构时须做未经测之改动；Jiri Kosina 谈 trivial 树：自陈约一年无暇维护，乐于任何使之更易之改动（如 github 式随机树快进合并），征助；Lukasz Majewski 论旧硬件移除：ARMv4T 须支持，工业系统或逾 30 年（已认证 HW 换几次 BSP）；指内核重安全却逼长寿命设备用 2.6/2.4 内核，附和 Linus 之 velocitate；Guenter Roeck 答 Geert：问其以 gcc-4.1.2 构建如何避开 lkml 2018/8/14 所报问题；延续旧硬件与工具链讨论

**史料**：`349266`、`349277`、`349278`、`349282`、`349284`、`349289`、`349291`、`349292`、`349294`、`349302`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.349266 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349277 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349278 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349282 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349284 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349289 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349291 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349292 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349294 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349302 -->` 

**史观**：分离聚合是永恒规律（总纲第 4 条——分离聚合是永恒规律：Greg KH 的“atomisp 由 Intel 推入后遭弃置致从内核剔除，谦称此乃流程正常运作”“阐明 Free Linux Driver 项目与 staging 仍活跃，被弃代码可 git revert 取回”与 Jiri Kosina 的“trivial 树自陈约一年无暇维护”并置，正是树与流程分合的相位）；本体论上各方平等（总纲第 8 条——本体论上各方平等：Linus Walleij 的“MOXA ART（Faraday IP、ARMv4 FA526）仍活跃部署，移除升级能力实为不负责任”与 Arnd Bergmann 的“各平台终将被移除，但加平台时应记录约束以便多年后寻用户”对撞，未替任一方定论）
**辨析**：Arnd 的“论产品两模型（追新内核与定居 SLTS），指出 y2038/Spectre 类事件迫使升级，怀疑 18 至 20 年安全软件自然上限”为其判词；Alexandre Belloni 的“rtc/codec/IIO/power-supply/hwmon 等常有路人不经意贡献，初始配置门槛过高”“强调非大公司支撑的子系统无法与 drm 类等同期待”为其经验归因，Mark Brown 与 Daniel Vetter 的答语（认同其忧、drm 亦有小型树与路人贡献之痛）为部分附和；Daniel Vetter 的“以 rtc 贡献统计（Belloni 241 居首）示倾斜不可持续”为可核之量化实况；Lukasz Majewski 的“ARMv4T 须支持，工业系统或逾 30 年”为其产业之陈。
**文献**：DSLXC-6039、DSLXC-6050、DSLXC-6051、DSLXC-6055、DSLXC-6057、DSLXC-6062、DSLXC-6064、DSLXC-6065、DSLXC-6067、DSLXC-6075（`ksummit-discuss.messages.349266`、`ksummit-discuss.messages.349277`、`ksummit-discuss.messages.349278`、`ksummit-discuss.messages.349282`、`ksummit-discuss.messages.349284`、`ksummit-discuss.messages.349289`、`ksummit-discuss.messages.349291`、`ksummit-discuss.messages.349292`、`ksummit-discuss.messages.349294`、`ksummit-discuss.messages.349302`，2018-09-11、2018-09-11、2018-09-11、2018-09-11、2018-09-11、2018-09-11、2018-09-11、2018-09-11、2018-09-11、2018-09-11），全文见 `raw_source.raw_json`

## 48.5 【Linux社区】API 废弃与警告分级（2 例）

**要点（判定表逐字）**：Mauro 论 API 替换与废弃：不应动 W 维度，media 已致力 W=1 零警告，而 W=2/W=3 在 gcc 8 核心 kAPI 下噪声过多；提议加 D=1 标记废弃项；Arnd Bergmann 论 API 废弃与警告分级：不喜新增 D=1 维度，倾向梳理 W=2/W=3 并引入 W=4；拟在 compiler-warnings.h 按编译器版本与层级标注每项，并指 Linus 刚以偏见移除 __deprecated

**史料**：`349267`、`349275`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.349267 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349275 -->` 

**史观**：法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：Mauro 的“不应动 W 维度，media 已致力 W=1 零警告，而 W=2/W=3 在 gcc 8 核心 kAPI 下噪声过多；提议加 D=1 标记废弃项”与 Arnd Bergmann 的“不喜新增 D=1 维度，倾向梳理 W=2/W=3 并引入 W=4”之争，实为告警噪声成本在子系统间的分配）；知识注定过时（总纲第 22 条——知识注定过时：Arnd 的“拟在 compiler-warnings.h 按编译器版本与层级标注每项”，正是对抗编译器知识过时的机制）
**辨析**：本块仅两例，为同一议题的正反对置；Arnd 的“指 Linus 刚以偏见移除 __deprecated”为其归因之陈，本页未见 Linus 回应；Mauro 的“media 已致力 W=1 零警告”为其子系统实况自述。两说并置，未作裁断。
**文献**：DSLXC-6040、DSLXC-6048（`ksummit-discuss.messages.349267`、`ksummit-discuss.messages.349275`，2018-09-11、2018-09-11），全文见 `raw_source.raw_json`

## 48.6 【Linux社区】2014 档案六封（6 例）

**要点（判定表逐字）**：Rafael J. Wysocki 响应 Olof Johansson 的 tech topic：主张驱动不应直接依赖具体固件接口（仅列匹配设备 ID），并提议新增对 ACPI 与 DT 通用、按平台切换的资源管理公共 API；提及 SPI、I2C 等非平台设备也需同类信息；并透露正扩展 ACPI 以容纳 DT 风格信息，列出 H. Peter Anvin 等参与人；Mark Brown 论 PM 依赖：核心设备探测延迟至依赖就绪，故被推到设备列表末端、先被挂起；主设备 suspend 时统一平息复合设备以解开设备间依赖；但指出 Rafael 所言异步挂起会破坏该模型；Peter Huewe 谈静态检查：赞同 ninja-check 包装器（聚合多静态分析器），请 Wolfram Sang 分享其脚本；属 2014 coverity 与静态检查 tech topic；Josh Triplett 谈 QR 编码 oops：QR 字母数字模式每字符仅 5.5 比特，base32 相较 base64 更省；指出 URL 须避用问号与百分号，可用美元星号加减点斜冒号扩至 base43，问是否值得复杂度；H. Peter Anvin 谈 QR oops：驳 Josh 称常备扫描 app 能读大 QR 之想，指原装扫描器并不处理大型 QR 符号；Andy Lutomirski 谈 QR oops：zxing 能读巨型 QR（维基 QR v40 图），但须找准对焦；承认应控制总体积

**史料**：`349256`、`349257`、`349268`、`349279`、`349290`、`349301`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.349256 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349257 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349268 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349279 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349290 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349301 -->` 

**史观**：一切真历史都是古代史（总纲第 1 条——一切真历史都是古代史：2014 年的 driver model/resources、PM 依赖、coverity 静态检查、QR encoded oops 四线档案被 2018 年讨论重提，正见旧议题的当代性）；经验优先（总纲第 9 条——经验优先：以 Josh Triplett 的“QR 字母数字模式每字符仅 5.5 比特，base32 相较 base64 更省”、Andy Lutomirski 的“zxing 能读巨型 QR（维基 QR v40 图），但须找准对焦”为判据）
**辨析**：Rafael J. Wysocki 的“主张驱动不应直接依赖具体固件接口（仅列匹配设备 ID），并提议新增对 ACPI 与 DT 通用、按平台切换的资源管理公共 API”与其“透露正扩展 ACPI 以容纳 DT 风格信息”为其设计主张；Mark Brown 的“指出 Rafael 所言异步挂起会破坏该模型”为对同行的技术纠正；H. Peter Anvin 的“驳 Josh 称常备扫描 app 能读大 QR 之想，指原装扫描器并不处理大型 QR 符号”与 Andy 的“zxing 能读”相对，属工具能力之争；Peter Huewe 的“赞同 ninja-check 包装器，请 Wolfram Sang 分享其脚本”为当事人自陈。本块六封皆 2014 年档案，与 2018 年主线不同期，属跨期并置。
**文献**：DSLXC-6029、DSLXC-6030、DSLXC-6041、DSLXC-6052、DSLXC-6063、DSLXC-6074（`ksummit-discuss.messages.349256`、`ksummit-discuss.messages.349257`、`ksummit-discuss.messages.349268`、`ksummit-discuss.messages.349279`、`ksummit-discuss.messages.349290`、`ksummit-discuss.messages.349301`，2014-05-03、2014-05-14、2014-05-14、2014-05-14、2014-05-14、2014-05-14），全文见 `raw_source.raw_json`

---
注：本文件由判定表程序化生成（6 块，覆盖 50/50 CAND，两遍计数核对通过）；要点逐字取自判定表“要点”列（主代理全读审读实录），史料锚与 CAND 一一对应，全文以 raw_source.raw_json 为准。
