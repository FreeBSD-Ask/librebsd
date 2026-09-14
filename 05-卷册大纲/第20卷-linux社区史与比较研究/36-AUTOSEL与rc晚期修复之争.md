# 36 【Linux社区】AUTOSEL与rc晚期修复之争

> 对应页面：ksummit-discuss p89（pk 348656-348705，2018 年 AUTOSEL／-rc 修复之争长线程 + 2014 档案信）
> 判定：50 CAND / 0 NV
> 编号：DSLXC-5431..5480 | claim 已入库（50/50，dslinux_claims.duckdb）

## 36.1 【Linux社区】AUTOSEL 压力与 -rc 分类提案：Ted 与 Guenter 之争（9 例）

**要点（判定表逐字）**：Theodore Ts'o 谈 AUTOSEL 乃加诸维护者的最新压力，主张优先让 linux-next 测试者满意，回归修复应尽快送 Linus 而非为 AUTOSEL 强求完美补丁、不必在 -next 浸泡一两周；Ted Ts'o 指 errseq 补丁直入 Linus 树不当（非回归而系九个月前引入），主张区分新特性／bug fix／合并窗引入的回归；stable 准入近年更激进，回归修复应快送而 stable 可暂缓一两周；Ted Ts'o 提议将 v4.16 按回归修复／普通 bug／非代码改动／其他 分类至各 -rc 级，对照历史理想（rc1-2 特性、rc3-4 修复、rc4 后仅回归），主张 -rc4 后 bug fix 延至下合并窗；Guenter Roeck 反驳 Ted，称将严重 bug 修复押后 4-6 周不现实（举 SpeckHammer〔存疑：原文如此，疑指 Spectre 类投机执行漏洞〕／PTI），指 stable 自行拣回退更糟，呼吁提升测试覆盖而非更严流程；Ted Ts'o 答 Mark，叹 Murphy 恶鬼使 A 用户回归修复破坏 B 用户略异硬件，印证维护者判断之难；Guenter Roeck 举 ext4 位图校验 CVE 与 7dac4a1726a9 及其修复 22be37acce25 为例，并指 mips／nds32 镜像不构建却无人问，倡导更精细测试而非更严流程；Guenter Roeck 答 Sasha，指 Sasha 误引其言（仅反对 -rc4 后押 bug fix，非嫌 stable 慢），忧近期 -stable 洪流动摇所有 stable 发行，甚拟不在 ChromeOS 合入；Guenter Roeck 答 Sasha，忧 CVE／崩溃／文件系统损坏修复被押后；附 v4.14.39 与 v4.4.131 构建／Qemu 测试结果（48／54 失败）示 stable 问题；Guenter Roeck 答 Sasha，讽延周期至 -rc20 如旧雇主为达标停测数周，此处则停打 bug fix 以避 -rc20

**史料**：`348659`、`348660`、`348670`、`348671`、`348673`、`348674`、`348690`、`348691`、`348699`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348659 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348660 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348670 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348671 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348673 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348674 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348690 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348691 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348699 -->` 

**史观**：权力再分配（总纲第 3 条——不存在进步，只有权力再分配：AUTOSEL 与 -rc 晚期修复之争，实为维护者与 stable 拣选者之间裁决权与流程权的再分配）；经验优先（总纲第 9 条——经验优先：以 v4.14.39 与 v4.4.131 构建／Qemu 测试结果（48／54 失败）、ext4 位图校验 CVE 与 7dac4a1726a9／22be37acce25 等实例为判据）
**辨析**：Ts'o 的“主张 -rc4 后 bug fix 延至下合并窗”为流程提案，Roeck 的“将严重 bug 修复押后 4-6 周不现实”为反驳，两说对撞未决；Roeck 的“指 Sasha 误引其言（仅反对 -rc4 后押 bug fix，非嫌 stable 慢）”为当事人澄清，属引述之辨；Roeck 的“甚拟不在 ChromeOS 合入”为个人表态。
**文献**：DSLXC-5434、DSLXC-5435、DSLXC-5445、DSLXC-5446、DSLXC-5448、DSLXC-5449、DSLXC-5465、DSLXC-5466、DSLXC-5474（`ksummit-discuss.messages.348659`、`ksummit-discuss.messages.348660`、`ksummit-discuss.messages.348670`、`ksummit-discuss.messages.348671`、`ksummit-discuss.messages.348673`、`ksummit-discuss.messages.348674`、`ksummit-discuss.messages.348690`、`ksummit-discuss.messages.348691`、`ksummit-discuss.messages.348699`，2018-05-01、2018-05-01、2018-05-03、2018-05-03、2018-05-03、2018-05-03、2018-05-03、2018-05-03、2018-05-03），全文见 `raw_source.raw_json`

## 36.2 【Linux社区】Geert 的 -rc commit 统计质疑（5 例）

**要点（判定表逐字）**：Geert Uytterhoeven 谢 Sasha 并质疑 -rc commit 命中 -stable 比例逾 20% 而合并窗仅 3% 之因，按是否修复同周期／前周期 bug 分类，问哪类最易出 bug；Geert Uytterhoeven 重发与 008 几乎相同的质询（列表疑似重复投递），再问 -rc commit 分类统计与哪些类别最 buggy；Sasha Levin 答 Geert，新特性仅合并窗可入、bug fix 随时可入；释 v4.17-rc1..rc3 中 245 带 Fixes、196 带 CC stable、395 含 fix 字串，余 200 非 bugfix 类；Geert Uytterhoeven 答 Sasha，举 v4.17-rc1..rc3 共 660 非合并提交（245 Fixes、196 CC stable、395 fix），余 200 落 bugfix 外，并指出快轨新特性／API 减依赖亦属合理非 fix -rc；Jani Nikula 反问 Ted，-rc5 及以后若非 bug fix 则为何物，表困惑

**史料**：`348663`、`348664`、`348668`、`348669`、`348675`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348663 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348664 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348668 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348669 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348675 -->` 

**史观**：经验优先（总纲第 9 条——经验优先：以 v4.17-rc1..rc3 共 660 非合并提交（245 Fixes、196 CC stable、395 fix）等量化统计为判据）；知识注定过时（总纲第 22 条——知识注定过时：-rc 提交分类统计随版本更迭而须重算，无恒定比例）
**辨析**：Levin 的“新特性仅合并窗可入、bug fix 随时可入”为规则说明；Uytterhoeven 的“指出快轨新特性／API 减依赖亦属合理非 fix -rc”为分类反例，与 Levin 的统计互补；Nikula 的“-rc5 及以后若非 bug fix 则为何物，表困惑”为开放之问。
**文献**：DSLXC-5438、DSLXC-5439、DSLXC-5443、DSLXC-5444、DSLXC-5450（`ksummit-discuss.messages.348663`、`ksummit-discuss.messages.348664`、`ksummit-discuss.messages.348668`、`ksummit-discuss.messages.348669`、`ksummit-discuss.messages.348675`，2018-05-02、2018-05-02、2018-05-02、2018-05-02、2018-05-03），全文见 `raw_source.raw_json`

## 36.3 【Linux社区】Sasha Levin 的数据论证与工具构想（8 例）

**要点（判定表逐字）**：Sasha Levin 答 Willy，若开发者无法证补丁经充分测试则宁可回退新特性而非并入未测修复；主张以 Tested-by 替代 -next 一周，必要时延周期至 -rc10+ 或回退特性；Sasha Levin 答 Daniel，认同良好测试优于强塞 -next，回归应 asap 而非立即，须经维护者认可的评审与测试，惜现状未达；Sasha Levin 答 Ted，列 4.16 各 -rc 的 Fixes 数（rc6 193 最多）与在 -next 平均天数（rc1 27.25 降至 rc7 8.7），揭示旧 bug 修复在周期末仓促并入；Sasha Levin 答 Willy，列 v4.16-rcX 修复 v4.14 前 bug 之数（rc6 113），示 Willy 所谓用户信任滞后之说未必成立；Sasha Levin 答 Willy／James，理想产出置于 scripts/ 之工具，以量化数据示补丁经常规渠道测试程度，最终仍由维护者裁决；Sasha Levin 答 James，称 Linus 正被取代（-next 已消解多数集成问题），列工具可示 -next 天数／邮件评审数／0day bot／syzbot 模糊时长／bugzilla 评论／是否 stable 等；Sasha Levin 答 Guenter，严重修复年不过数次；多数晚期修复针对旧 bug，AUTOSEL 运行逾一年其回归率与手工 CC stable 相当；Sasha Levin 答 Willy，称 2% 偏低（历史约 7%），且较合并窗每代码行多三倍 bug；提议延周期至 -rc20 直至当前合并窗回归低于阈值

**史料**：`348665`、`348666`、`348681`、`348683`、`348684`、`348686`、`348687`、`348697`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348665 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348666 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348681 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348683 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348684 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348686 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348687 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348697 -->` 

**史观**：经验优先（总纲第 9 条——经验优先：以 4.16 各 -rc 的 Fixes 数（rc6 193 最多）与在 -next 平均天数（rc1 27.25 降至 rc7 8.7）等量化为判据）；动手者创造历史（总纲第 10 条——动手者创造历史：以置于 scripts/ 的量化工具构想、以 Tested-by 替代 -next 浸泡为分析单位）
**辨析**：Levin 的“称 Linus 正被取代（-next 已消解多数集成问题）”为强判断，属当事人立场；其“延周期至 -rc20 直至当前合并窗回归低于阈值”为提案，本页未见采纳；Levin 的“AUTOSEL 运行逾一年其回归率与手工 CC stable 相当”为自陈数据，落书须与当期统计核对。
**文献**：DSLXC-5440、DSLXC-5441、DSLXC-5456、DSLXC-5458、DSLXC-5459、DSLXC-5461、DSLXC-5462、DSLXC-5472（`ksummit-discuss.messages.348665`、`ksummit-discuss.messages.348666`、`ksummit-discuss.messages.348681`、`ksummit-discuss.messages.348683`、`ksummit-discuss.messages.348684`、`ksummit-discuss.messages.348686`、`ksummit-discuss.messages.348687`、`ksummit-discuss.messages.348697`，2018-05-02、2018-05-02、2018-05-03、2018-05-03、2018-05-03、2018-05-03、2018-05-03、2018-05-03），全文见 `raw_source.raw_json`

## 36.4 【Linux社区】Al Viro、Willy Tarreau 与 Bottomley 的方法论质疑（9 例）

**要点（判定表逐字）**：Al Viro 问 Geert，当修复自然拆为 2-3 个等效变换加一行修复时，Fixes 统计如何计；Al Viro 答 Ted，补“除非系已知被利用的提权洞”方破其 -rc4 后延窗之议；James Bottomley 答 Jani，指 -rc 修复呈光谱：明显无副作用者易证，复杂者恐带副作用；SCSI 按用户可见效应裁定，复杂修复常入合并窗树并 CC stable 附等待数周注记；James Bottomley 答 Sasha，若可脚本化品味早该用更不和气的某物取代 Linus；用户可见性测试至上，无疑似修复却常误，静态检查器常挨批；Al Viro 答 Sasha，质疑 Fixes: 解读之准（部分修复、增量提交指向何者），以 foofs_barf() 多洞与 -rc4 改方法签名之难为例；James Bottomley 答 Sasha，指所列指标皆测“是否引新 bug”之险，晚期 -rc 决断在看当前用户可见问题集对 -rc 失稳风险，举 SCSI 板启动失败为立修、冷门板错误支为缓；Al Viro 答 Sasha，直言方法签名变更（数十实例）不该入 -rc5，免与各文件系统树冲突噩梦；追问该拆分式修复的 Fixes: 元数据应如何填以减 -stable 之苦；Greg KH 答 Al Viro，言不在乎 -stable 依赖之苦，正确修复即可、依赖问题日后他来理；Sasha Levin 答 Al Viro，言 -stable 不应左右并入时机，依赖链工具可于 backport 时解；示拆分补丁（1）本地内存损坏修复、（2）方法签名树遍改、（3）后续改动的 Fixes:/Cc stable 正确标注法

**史料**：`348676`、`348677`、`348680`、`348685`、`348688`、`348696`、`348698`、`348703`、`348705`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348676 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348677 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348680 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348685 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348688 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348696 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348698 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348703 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348705 -->` 

**史观**：本体论上各方平等（总纲第 8 条——本体论上各方平等：Viro 的“方法签名变更不该入 -rc5”与 Bottomley 的“复杂修复常入合并窗树并 CC stable”、Greg KH 的“不在乎 -stable 依赖之苦”三方并置）；经验优先（总纲第 9 条——经验优先：以 foofs_barf() 多洞、SCSI 板启动失败为立修等具体案例为判据）
**辨析**：Viro 的“补“除非系已知被利用的提权洞”方破其 -rc4 后延窗之议”为条件性反驳；Bottomley 的“若可脚本化品味早该用更不和气的某物取代 Linus”为反讽，非方案；Levin 的“-stable 不应左右并入时机，依赖链工具可于 backport 时解”为其工具论立场。
**文献**：DSLXC-5451、DSLXC-5452、DSLXC-5455、DSLXC-5460、DSLXC-5463、DSLXC-5471、DSLXC-5473、DSLXC-5478、DSLXC-5480（`ksummit-discuss.messages.348676`、`ksummit-discuss.messages.348677`、`ksummit-discuss.messages.348680`、`ksummit-discuss.messages.348685`、`ksummit-discuss.messages.348688`、`ksummit-discuss.messages.348696`、`ksummit-discuss.messages.348698`、`ksummit-discuss.messages.348703`、`ksummit-discuss.messages.348705`，2018-05-03、2018-05-03、2018-05-03、2018-05-03、2018-05-03、2018-05-03、2018-05-03、2018-05-03、2018-05-03），全文见 `raw_source.raw_json`

## 36.5 【Linux社区】维护者评审、CI 与 AUTOSEL 答问（10 例）

**要点（判定表逐字）**：Mark Brown 呼应 Ted，述某维护者令补丁在 -next 浸泡一周致依赖未被发现、整段测试覆盖缺失的过往教训；Daniel Vetter 称其 CI 常持滚动 fixup 补丁保运行，因回归修复有时需数天／小时；主张回归一旦漏过应立即修、无需不必要浸泡，应加强 CI 而非 soak；Mark Brown 答 Sasha，维护者评审缺失非普遍问题；驱动专属修复常无独立评审可能（硬件不普、须信厂商判断）；Greg KH 答 Guenter，认同众人正改善测试、随时欢迎更多，简短收束；Sasha Levin 答 Guenter，严重问题多得评审故无需久 soak；多数晚期 -rc 修复针对不甚关键的旧 bug，举 PTI 入 -stable，称企业发行版嫌快、有人嫌慢；Randy Dunlap 答 Sasha／James，比新工具于 checkpatch（有用但非唯一真理），谓维护者仍需人为评估，谨防工具反令补丁更快并入；Sasha Levin 答 Willy，列 4.17 中由 v4.16 修复作引入的修复 14／755 约 2%，主张责在维护者而非作者，应仅在确证时并入；Sasha Levin 答 Al Viro，认 Fixes: 仅为近似（部分无标签或正文提及），非强阻 -rc4 后提交，正构想工具助维护者判断而非立任意规则；Sasha Levin 答 Randy，望工具仅助维护者（较不易滥用），称今维护者不足致延迟与失误，工具或助补丁更早并入；Ted Ts'o 答 Jani，谓 -rc5+ 为回归修复；若人不再引回归或可于 -rc6 前发版，倡两月周期，反之陷入更长发布周期恶性循环

**史料**：`348661`、`348662`、`348672`、`348679`、`348682`、`348692`、`348693`、`348694`、`348695`、`348704`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348661 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348662 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348672 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348679 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348682 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348692 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348693 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348694 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348695 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348704 -->` 

**史观**：动手者创造历史（总纲第 10 条——动手者创造历史：以 Vetter 的滚动 fixup 补丁保 CI 运行、Dunlap 比新工具于 checkpatch 为分析单位）；经验优先（总纲第 9 条——经验优先：以某维护者令补丁在 -next 浸泡一周致依赖未被发现、4.17 中由 v4.16 修复作引入的修复 14／755 约 2% 等实例为判据）
**辨析**：Brown 的“维护者评审缺失非普遍问题；驱动专属修复常无独立评审可能”为现状辩护；Vetter 的“应加强 CI 而非 soak”与 Brown 的浸泡教训构成两说；Dunlap 的“谨防工具反令补丁更快并入”为风险提示，Levin 的“望工具仅助维护者（较不易滥用）”为其回应。
**文献**：DSLXC-5436、DSLXC-5437、DSLXC-5447、DSLXC-5454、DSLXC-5457、DSLXC-5467、DSLXC-5468、DSLXC-5469、DSLXC-5470、DSLXC-5479（`ksummit-discuss.messages.348661`、`ksummit-discuss.messages.348662`、`ksummit-discuss.messages.348672`、`ksummit-discuss.messages.348679`、`ksummit-discuss.messages.348682`、`ksummit-discuss.messages.348692`、`ksummit-discuss.messages.348693`、`ksummit-discuss.messages.348694`、`ksummit-discuss.messages.348695`、`ksummit-discuss.messages.348704`，2018-05-01、2018-05-02、2018-05-03、2018-05-03、2018-05-03、2018-05-03、2018-05-03、2018-05-03、2018-05-03、2018-05-03），全文见 `raw_source.raw_json`

## 36.6 【Linux社区】DT Workshop 收尾、kselftest、oops 与 tinification 安全之议（9 例）

**要点（判定表逐字）**：Olof Johansson 接 Arnd 关于驱动模型／ACPI／DT 之议，追问 AMD 在嵌入式 ARM64 上 ACPI 规划，指 SBSA 式 ACPI 难与激进电源管理（mobile／embedded）干净契合，反对为新架构引入第二套不兼容 ACPI；Grant Likely 公布 2017 Prague Devicetree Workshop 的 slides 与笔记已上传 elinux.org，并提及全天音频录音（100-200MB）尚未决定发布方式，邀志愿者撰写当日纪要；Frank Rowand 补述与 Grant 数日来多次更新 Workshop 信息（增 slides、补评论、将 etherpad 笔记转 wiki 格式），确认 elinux 页面与合影链接；Josh Triplett 论 QR oops 编码：base32 配 QR alphanumeric 模式仅 5.5 bit／字符，较 base64（6 vs 8 bit）浪费更少，反驳 Levente 所谓 base32 多耗 20% 空间之见；Steven Rostedt 接 Masami Hiramatsu 于 stable issues 议题，赞在 MAINTAINERS 加 UT:/TS: 测试标签之议，自陈 ftrace 测试因须 root 破 selftests 规则，拟置 tools/testing/tracing 或送 LTP；Davidlohr Bueso 接 Rostedt 之 stable issues 帖，问 selftests 为何须 root（crash and burn 仅供内核开发者）；James Bottomley 接 Dave Jones 论 Kernel tinification，忧 syscall 选项海洋致各内核 ABI 微异、二进制跨发行版不跑；主张少量用例选项（CONFIG_SECURE_ROUTER／CONFIG_REDUCED_ATTACK_SURFACE），并以 C/R 容器视角证 kcmp 必要；Ted Ts'o 接 tinification 帖，论用户态（举 systemd）强制可选设施非内核可左右，称无现成方案影响用户态则不宜立题；Steven Rostedt 接 Li Zefan 引 Andrew 新特性须带测试用例之议，论 tools/testing/selftests 放置（疑顶层 makefile 全跑），主张按子系统自测而非另起 LTP

**史料**：`348656`、`348657`、`348658`、`348667`、`348678`、`348689`、`348700`、`348701`、`348702`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348656 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348657 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348658 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348667 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348678 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348689 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348700 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348701 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348702 -->` 

**史观**：分离聚合是永恒规律（总纲第 4 条——分离聚合是永恒规律：syscall 选项海洋致各内核 ABI 微异、二进制跨发行版不跑，见裁剪与兼容之分合）；本体论上各方平等（总纲第 8 条——本体论上各方平等：2014 档案诸封与 2017 DT Workshop 收尾并置，不因时隔而分高下）
**辨析**：Johansson 的“反对为新架构引入第二套不兼容 ACPI”为架构立场；Bottomley 的“忧 syscall 选项海洋致各内核 ABI 微异”为风险判断，其“以 C/R 容器视角证 kcmp 必要”为用例论证；Ts'o 的“称无现成方案影响用户态则不宜立题”为设题门槛。
**文献**：DSLXC-5431、DSLXC-5432、DSLXC-5433、DSLXC-5442、DSLXC-5453、DSLXC-5464、DSLXC-5475、DSLXC-5476、DSLXC-5477（`ksummit-discuss.messages.348656`、`ksummit-discuss.messages.348657`、`ksummit-discuss.messages.348658`、`ksummit-discuss.messages.348667`、`ksummit-discuss.messages.348678`、`ksummit-discuss.messages.348689`、`ksummit-discuss.messages.348700`、`ksummit-discuss.messages.348701`、`ksummit-discuss.messages.348702`，2014-05-13、2017-11-02、2017-11-02、2014-05-13、2014-05-13、2014-05-13、2014-05-02、2014-05-02、2014-05-13），全文见 `raw_source.raw_json`

---
注：本文件由判定表程序化生成（6 块，覆盖 50/50 CAND，两遍计数核对通过）；要点逐字取自判定表“要点”列（主代理全读审读实录），史料锚与 CAND 一一对应，全文以 raw_source.raw_json 为准。
