# 37 【Linux社区】pending-fixes机制与延时合入之争

> 对应页面：ksummit-discuss p91（pk 348756-348805，2018 年 linux-next fixes 分支机制与 AUTOSEL 延时之争 + PM/ACPI-DT）
> 判定：50 CAND / 0 NV
> 编号：DSLXC-5481..5530 | claim 已入库（50/50，dslinux_claims.duckdb）

## 37.1 【Linux社区】linux-next pending-fixes 机制与各树 fixes 分支上云（12 例）

**要点（判定表逐字）**：Stephen Rothwell 将 Tony Lindgren 的 linux-omap fixes 分支并入 linux-next，重申其用途为集成测试与降低下一合并窗口的子系统冲突，并列出补丁须满足 GPL v2、Signed-off-by、已发列表、已审阅、已单测、指向当前或下个合并窗口等条件；Mark Brown 评 Jiri Kosina 将 -fixes 并入 for-next 的做法：虽是最佳实践，但 fixes 分支未经自身 -next 之外的测试、与其他人 -next 覆盖隔离，隐含依赖恐被漏检；Stephen Rothwell 将 David Sterba 的 btrfs-fixes（kdave/linux next-fixes）并入 linux-next，重申其用途为集成测试与降低合并窗口冲突，并列出补丁准入条件；Stephen Rothwell 通告 pending-fixes 分支已上线，linux-next 的 fixes 分支数自 44 增至 55，回应 Daniel Vetter 关于把 -fixes 中间态推给测试机器人的设想；Guenter Roeck 报告 pending-fixes 构建测试匹配主线：132 项构建中 130 通过、失败为 m68k 与 xtensa 的 allmodconfig，138 项 qemu 测试全过；Ulf Hansson 感谢 Stephen Rothwell 迅速采纳 fixes 分支构想，拟请 kernelci 把该分支纳入每日构建，并请加 mmc.git fixes 分支；Stephen Rothwell 将 Ulf Hansson 的 mmc.git fixes 并入 linux-next，重申用途与补丁准入条件；Krzysztof Kozlowski 请并 samsung-krzk 的 fixes 与 pinctrl-samsung 的 pinctrl-fixes 两分支（当时皆空，为将来预置）；Stephen Rothwell 将 Krzysztof Kozlowski 的两 fixes 分支自明日并入 linux-next，重申 linux-next 集成测试之用；Mark Brown 简短告知 Ulf Hansson：kernelci 加 fixes 分支一事无需其操心，自己已添加；Vinod Koul 问 Stephen Rothwell 要维护者自送 fixes 分支还是扫描现存树添加，并请加 slave-dma/fixes；Vinod Koul 回 Stephen Rothwell 确认加 slave-dma/fixes 已办，并请把联系地址由失效的 Intel 邮址改为 kernel.org 邮址

**史料**：`348756`、`348758`、`348759`、`348760`、`348761`、`348767`、`348772`、`348773`、`348774`、`348775`、`348804`、`348805`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348756 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348758 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348759 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348760 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348761 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348767 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348772 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348773 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348774 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348775 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348804 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348805 -->` 

**史观**：动手者创造历史（总纲第 10 条——动手者创造历史：以 pending-fixes 分支上线（linux-next 的 fixes 分支数自 44 增至 55）、kernelci 纳入每日构建为分析单位）；经验优先（总纲第 9 条——经验优先：以 pending-fixes 构建测试 132 项中 130 通过、138 项 qemu 测试全过等实测为判据）
**辨析**：Brown 的“fixes 分支未经自身 -next 之外的测试、与其他人 -next 覆盖隔离，隐含依赖恐被漏检”为风险提示，与 Rothwell 的“用途为集成测试与降低合并窗口冲突”并列；Rothwell 的“补丁须满足 GPL v2、Signed-off-by、已发列表、已审阅、已单测、指向当前或下个合并窗口”为准入定则；Koul 的“请把联系地址由失效的 Intel 邮址改为 kernel.org 邮址”为事务性请求。
**文献**：DSLXC-5481、DSLXC-5483、DSLXC-5484、DSLXC-5485、DSLXC-5486、DSLXC-5492、DSLXC-5497、DSLXC-5498、DSLXC-5499、DSLXC-5500、DSLXC-5529、DSLXC-5530（`ksummit-discuss.messages.348756`、`ksummit-discuss.messages.348758`、`ksummit-discuss.messages.348759`、`ksummit-discuss.messages.348760`、`ksummit-discuss.messages.348761`、`ksummit-discuss.messages.348767`、`ksummit-discuss.messages.348772`、`ksummit-discuss.messages.348773`、`ksummit-discuss.messages.348774`、`ksummit-discuss.messages.348775`、`ksummit-discuss.messages.348804`、`ksummit-discuss.messages.348805`，2018-05-10、2018-05-11、2018-05-12、2018-05-12、2018-05-12、2018-05-14、2018-05-14、2018-05-15、2018-05-15、2018-05-17、2018-05-09、2018-05-09），全文见 `raw_source.raw_json`

## 37.2 【Linux社区】0day／kbuild 机器人覆盖边界与构建回归（8 例）

**要点（判定表逐字）**：Geert Uytterhoeven 提醒 Sasha Levin 漏看 Jiri Kosina 回信中的 as well，并以 renesas-drivers 双周发布为例力主维护者把自身 fixes 并入自身 for-next 以自解冲突；Geert Uytterhoeven 指一例提交在被机器人标记构建回归 18 小时后仍被选入 stable，建议 backport 脚本检索提交 ID 以规避此类问题，并引 PostgreSQL fsync 的 LWN 文与 Willy 提交未过 -next 即入主线；Boris Brezillon 附言其补丁在 Fengguang 机器人树已测逾一周、linux-next 仅两天，但仍到主线才收 bug 报告，质疑是否存仅跑 Linus 树的测试；Geert Uytterhoeven 问 Boris Brezillon 是否收到 Fengguang 机器人列全配置（含失败项）的成功报告；Boris Brezillon 贴出 kbuild 机器人 BUILD SUCCESS 报告（分支 mtd/fixes、HEAD fc3a9e15、测 142 配置），证其补丁确经构建测试；Geert Uytterhoeven 指出 Boris Brezillon 的构建成功报告未列失败项 m68k/allmodconfig，并附自己 178 配置的报告对比；Boris Brezillon 承认某些配置（如耗时久者）在其 linux-0day 树罕被测试，主张仅把 kbuild 机器人结果当指示而非保证；Fengguang Wu 解释 0day 无百分百保证：响应时间对覆盖的取舍（成功通知半日内发、后续约一周续测扩覆盖）与基于 merge-test-bisect 的工作流对难合并旧分支覆盖更少

**史料**：`348762`、`348763`、`348764`、`348765`、`348766`、`348769`、`348770`、`348771`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348762 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348763 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348764 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348765 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348766 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348769 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348770 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348771 -->` 

**史观**：经验优先（总纲第 9 条——经验优先：以 kbuild 机器人 BUILD SUCCESS 报告（分支 mtd/fixes、HEAD fc3a9e15、测 142 配置）、Geert 自测 178 配置的报告对比等实测为判据）；知识注定过时（总纲第 22 条——知识注定过时：构建覆盖与响应时间的取舍使 0day 无百分百保证）
**辨析**：Uytterhoeven 的“一例提交在被机器人标记构建回归 18 小时后仍被选入 stable”为流程缺陷实例，其“建议 backport 脚本检索提交 ID 以规避”为处方；Brezillon 的“主张仅把 kbuild 机器人结果当指示而非保证”为工具定性；Wu 的“解释 0day 无百分百保证：响应时间对覆盖的取舍”为设计取舍说明。
**文献**：DSLXC-5487、DSLXC-5488、DSLXC-5489、DSLXC-5490、DSLXC-5491、DSLXC-5494、DSLXC-5495、DSLXC-5496（`ksummit-discuss.messages.348762`、`ksummit-discuss.messages.348763`、`ksummit-discuss.messages.348764`、`ksummit-discuss.messages.348765`、`ksummit-discuss.messages.348766`、`ksummit-discuss.messages.348769`、`ksummit-discuss.messages.348770`、`ksummit-discuss.messages.348771`，2018-05-14、2018-05-14、2018-05-14、2018-05-14、2018-05-14、2018-05-14、2018-05-14、2018-05-14），全文见 `raw_source.raw_json`

## 37.3 【Linux社区】Sasha Levin 的 AI 设想与数据论证（7 例）

**要点（判定表逐字）**：Sasha Levin 首发长文：基于 AUTOSEL 经验拟教 AI 识别 bug-introducing 补丁，列 -next 数据、列表数据、作者维护链、复杂度、流程合规等参数，并公布统计——-rc 提交每行的缺陷率约为合并窗口三倍、维护者自写自交同日合入者易引入 bug，主张收紧 -rc 周期；Sasha Levin 回 Theodore Ts'o：非要求等更久才合入，而是合入 Linus 前多停留，指 Willy 的提交未过 -next 即入主线且带 stable 标签，呼吁维护者提升合入前测试（讽 Linus 对 -rc 提交放宽 -next 规则）；Sasha Levin 回 Willy Tarreau：把议题拉回 -rc 而非 -stable，称统计显示每改动一行 -rc 提交引入 bug 概率超合并窗口三倍，问社区是否视此为问题；Sasha Levin 回 Theodore Ts'o 提分级方案：新特性需 -next 2+ 周、合并窗口回归修复按 -rc 阶段分级、旧版 bug 修复需 2+ 周，并透露 AUTOSEL 落后 -stable 平均 9.7 个月；Stephen Rothwell 纠正 Sasha Levin：linux-next-history 树覆盖 next-20080214 至 next-20180501（v2.6.25-rc1 至 v4.17-rc3），非仅 v4.4 至 v4.16，承诺修复 git.kernel.org 上的残缺副本；Stephen Rothwell 告知 Sasha Levin：其所言 Willy 提交其实周一已入 linux-next，至少经一次发布，测试量另说；Sasha Levin 贴 v4.16-rc7 数据：若干提交自 authors 到入 Linus 树约 24 小时、或维护者自写自推自发，附提交 ID、合入时、在 -next 天数、所修提交及该提交合入时五列

**史料**：`348776`、`348777`、`348778`、`348781`、`348782`、`348783`、`348792`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348776 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348777 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348778 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348781 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348782 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348783 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348792 -->` 

**史观**：知识注定过时（总纲第 22 条——知识注定过时：拟教 AI 识别 bug-introducing 补丁、以 -next 数据与作者维护链为参数，知识须随数据更迭重训）；经验优先（总纲第 9 条——经验优先：以 -rc 提交每行缺陷率约为合并窗口三倍、AUTOSEL 落后 -stable 平均 9.7 个月等统计为判据）
**辨析**：Levin 的“AUTOSEL 落后 -stable 平均 9.7 个月”为自陈数据，落书须与当期统计核对；Rothwell 的“纠正 linux-next-history 树覆盖区间为 next-20080214 至 next-20180501，非仅 v4.4 至 v4.16”为当事人对同一史实的两造对读；Rothwell 的“其所言 Willy 提交其实周一已入 linux-next”为事实纠正。
**文献**：DSLXC-5501、DSLXC-5502、DSLXC-5503、DSLXC-5506、DSLXC-5507、DSLXC-5508、DSLXC-5517（`ksummit-discuss.messages.348776`、`ksummit-discuss.messages.348777`、`ksummit-discuss.messages.348778`、`ksummit-discuss.messages.348781`、`ksummit-discuss.messages.348782`、`ksummit-discuss.messages.348783`、`ksummit-discuss.messages.348792`，2018-05-01、2018-05-01、2018-05-01、2018-05-01、2018-05-01、2018-05-01、2018-05-03），全文见 `raw_source.raw_json`

## 37.4 【Linux社区】Willy Tarreau 与 Sasha 的交锋：延后合入与发布周期（11 例）

**要点（判定表逐字）**：Willy Tarreau 回 Sasha Levin：指 -next 受众有限而 -stable 用户众、二者覆盖不可比，不认为 -stable 现状糟糕，建议对近期合入代码连续堆叠修复者施额外审查延迟；Willy Tarreau 反对 Sasha 延后合入修复的提案：故意留已知 bug 会逐版降质、损 dot-0 声誉、向开发者发错误信号，主张对引入过多回归者设延迟惩罚；Willy Tarreau 与 Sasha Levin 论 tested-by 可替代一周 -next、对承包商设回归惩罚可作为长期威慑，并同意仅对新合入特性可改而 revert 而非合未测修复；Willy Tarreau 回 Guenter Roeck：把有效修复因少数可能错误而全数推迟只会更糟，应信任开发者所明示的测试覆盖；Willy Tarreau 赞 James Bottomley 在 SCSI 按用户可见效应取舍、复杂修复转合并窗口并附 stable 延时注记的做法为负责之举；Willy Tarreau 评 Sasha Levin 的 v4.16 各 -rc 修复统计：旧 bug 修复在 rc7 扎堆或因用户信任第 3、4 个稳定版后才切换、遇 bug、报告、维护者写修的时延；Willy Tarreau 续与 James Bottomley：用户暴露必要、稳定版多层保信任，自陈多次因测试不足搞坏 stable backport、被 Guenter 构建测试接住，公开羞辱式提醒有效；Willy Tarreau 看 Sasha Levin 的 v4.16-rcX 修早于 v4.14 引入 bug 的统计（rc7 达 61），认为其中部分本可多煮一阵；Willy Tarreau 赞 Sasha Levin 的分析，主张教育开发者莫在周期末对旧 bug 匆交修复、改等下版在 -rc 久煮，并仿 Greg 的 WTF 脚本对惹祸的晚期补丁发 WTF 提醒；Willy Tarreau 回 Sasha Levin 的 4.17 数据：755 提交中仅 14（约 2%）修了上一轮修复引入的回归，若强延必失更多正确修复，主张提认知与公开问责而非普添延迟；Willy Tarreau 反对无限延长发布周期（如 -rc20）：开发不停、下个窗口翻倍提交致更多问题，建议发布说明加 known bugs 段以给修复者时间

**史料**：`348780`、`348784`、`348785`、`348786`、`348787`、`348788`、`348789`、`348791`、`348793`、`348795`、`348796`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348780 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348784 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348785 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348786 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348787 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348788 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348789 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348791 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348793 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348795 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348796 -->` 

**史观**：本体论上各方平等（总纲第 8 条——本体论上各方平等：Tarreau 的“故意留已知 bug 会逐版降质、损 dot-0 声誉”与 Levin 的“收紧 -rc 周期”逐轮对撞）；经验优先（总纲第 9 条——经验优先：以 755 提交中仅 14（约 2%）修了上一轮修复引入的回归等实数为判据）
**辨析**：Tarreau 的“自陈多次因测试不足搞坏 stable backport、被 Guenter 构建测试接住，公开羞辱式提醒有效”为当事人自陈，属经验优先之实证；其“反对无限延长发布周期（如 -rc20）”为对 Levin 提案的直接反驳；Tarreau 的“主张发布说明加 known bugs 段”为折中方案。
**文献**：DSLXC-5505、DSLXC-5509、DSLXC-5510、DSLXC-5511、DSLXC-5512、DSLXC-5513、DSLXC-5514、DSLXC-5516、DSLXC-5518、DSLXC-5520、DSLXC-5521（`ksummit-discuss.messages.348780`、`ksummit-discuss.messages.348784`、`ksummit-discuss.messages.348785`、`ksummit-discuss.messages.348786`、`ksummit-discuss.messages.348787`、`ksummit-discuss.messages.348788`、`ksummit-discuss.messages.348789`、`ksummit-discuss.messages.348791`、`ksummit-discuss.messages.348793`、`ksummit-discuss.messages.348795`、`ksummit-discuss.messages.348796`，2018-05-01、2018-05-01、2018-05-02、2018-05-02、2018-05-03、2018-05-03、2018-05-03、2018-05-03、2018-05-03、2018-05-03、2018-05-03），全文见 `raw_source.raw_json`

## 37.5 【Linux社区】Fixes 头价值、提交规范与发行版视角（7 例）

**要点（判定表逐字）**：Justin Forbes 以发行版维护者视角介入：过去已知回归被维护者压到下一合并窗口才修最遭诟病、近来已改善，反对一刀切规则、主张最佳实践而非固定时限，并忧 -stable 近期涌入过多补丁恐动摇信任；Willy Tarreau 论 Fixes 头价值：助 backport 者判断补丁是否相关、提供线索，主张勿增提交者负担，模糊信息（如 4.4 maybe 4.2）亦极有用，依赖链次之；Willy Tarreau 劝勿以繁复额外头（如 Cc stable 的复杂表达式）补偿含糊提交说明，主张自然语言描述依赖，并赞 Fixes 头让作者可标所修而不必抄 stable；Justin Forbes 回 Sasha Levin：Fedora rawhide 每日构建 Linus 树、端用户常在 24 小时内测到，故并非无人跑 Linus 树，反对据无人用 Linus 树而仓促推修复的假设；David Lang 反驳 Sasha Levin 称无人长期用 vanilla 发行版：前职曾取一版长期不更、无事则不升，证有人用 Linus 内核；Justin Forbes 澄清 Fedora 在 Linus 发版时有分支点，临近发版则锁 4.16.0 至 stable 更新，否则用 stabilization 仓测 .0 至 .1，故 .0 确有用户与测试者；Willy Tarreau 反驳 Sasha Levin 取消点发布、增频合并窗口之想：去掉一步只是下移一级、问题依旧，且 .0 是参考基线、同步全员目标，主张教育开发者少仓促多测

**史料**：`348794`、`348797`、`348798`、`348799`、`348800`、`348802`、`348803`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348794 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348797 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348798 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348799 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348800 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348802 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348803 -->` 

**史观**：本体论上各方平等（总纲第 8 条——本体论上各方平等：Forbes 的发行版视角、Lang 的“有人用 Linus 内核”与 Tarreau 的“勿以繁复额外头补偿含糊提交说明”并置）；法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：一刀切规则与最佳实践的取舍，实为发行版与上游之间的责任边界）
**辨析**：Forbes 的“Fedora rawhide 每日构建 Linus 树、端用户常在 24 小时内测到”为发行版实况，反驳“无人用 Linus 树”之假设；Lang 的“前职曾取一版长期不更、无事则不升”为个例，不得外推为通例；Tarreau 的“去掉点发布只是下移一级、问题依旧”为对 Levin 提案的结构性反驳。
**文献**：DSLXC-5519、DSLXC-5522、DSLXC-5523、DSLXC-5524、DSLXC-5525、DSLXC-5527、DSLXC-5528（`ksummit-discuss.messages.348794`、`ksummit-discuss.messages.348797`、`ksummit-discuss.messages.348798`、`ksummit-discuss.messages.348799`、`ksummit-discuss.messages.348800`、`ksummit-discuss.messages.348802`、`ksummit-discuss.messages.348803`，2018-05-03、2018-05-03、2018-05-04、2018-05-08、2018-05-08、2018-05-08、2018-05-08），全文见 `raw_source.raw_json`

## 37.6 【Linux社区】PM 议题与 ACPI／DT 统一抽象层（5 例）

**要点（判定表逐字）**：Rafael J. Wysocki 与 Olof Johansson 论 ACPI 与 DT 的统一抽象层：Rafael 主张在固件层做翻译、尽量不改驱动的 of_ 接口，Olof 反对宏大统一抽象层、指 device_node 与 struct device 非一一对应、PCIe 主桥在嵌入与 ACPI 下处理迥异，Arnd 所提 dev_property_read_bool 方案更简单；Rafael J. Wysocki 与 Mark Brown、Tomasz Figa 论 PM 依赖：runtime PM 引用计数在非驱动模型拓扑（如加 IOMMU）失效，Rafael 释 .suspend_late 与 .resume_early 原为令同一回调兼用于 runtime 与系统级 PM；Rafael J. Wysocki 追问 PM 依赖中 resume 情形：子设备 resume 会自动拉起父设备但其他依赖设备不会，请各方给细节；Rafael J. Wysocki 回应 Morten Rasmussen 的 Energy-aware Scheduling Workshop 拟议：表兴趣参与，并指其与自己提的 energy conservation bias interfaces KS 议题相关，列举测试用例、能耗评估、平台能耗数据、CPU 利用率与 cpu_power 等研讨点；Rafael J. Wysocki 与 Preeti U Murthy 论 energy conservation bias interfaces：指今 C-state 分核、包、模块且受 I/O 状态牵连，C-state 对 P-state 的取舍（低频 X 时 vs 高频 Y 时、Y 小于 X）使画面更复杂

**史料**：`348757`、`348768`、`348779`、`348790`、`348801`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348757 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348768 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348779 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348790 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348801 -->` 

**史观**：分离聚合是永恒规律（总纲第 4 条——分离聚合是永恒规律：ACPI 与 DT 的统一抽象层之争、device_node 与 struct device 非一一对应，见固件抽象路径之分合）；经验优先（总纲第 9 条——经验优先：以 runtime PM 引用计数在非驱动模型拓扑（如加 IOMMU）失效、C-state 分核包模块且受 I/O 状态牵连等机制为判据）
**辨析**：Johansson 的“反对宏大统一抽象层、指 device_node 与 struct device 非一一对应、PCIe 主桥在嵌入与 ACPI 下处理迥异”为架构反驳，与 Wysocki 的“主张在固件层做翻译、尽量不改驱动的 of_ 接口”两说并置；Wysocki 的“释 .suspend_late 与 .resume_early 原为令同一回调兼用于 runtime 与系统级 PM”为机制说明；Rasmussen 的 Workshop 拟议为待办，本页未见结果。
**文献**：DSLXC-5482、DSLXC-5493、DSLXC-5504、DSLXC-5515、DSLXC-5526（`ksummit-discuss.messages.348757`、`ksummit-discuss.messages.348768`、`ksummit-discuss.messages.348779`、`ksummit-discuss.messages.348790`、`ksummit-discuss.messages.348801`，2014-05-13、2014-05-13、2014-05-13、2014-05-13、2014-05-13），全文见 `raw_source.raw_json`

---
注：本文件由判定表程序化生成（6 块，覆盖 50/50 CAND，两遍计数核对通过）；要点逐字取自判定表“要点”列（主代理全读审读实录），史料锚与 CAND 一一对应，全文以 raw_source.raw_json 为准。
