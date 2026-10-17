# 38 【Linux社区】stable节奏之争与Intel-embargo之辨

> 对应页面：ksummit-discuss p92（pk 348806-348855，2018 stable 测试与发版节奏之争长线程 + 2014 档案信）
> 判定：50 CAND / 0 NV
> 编号：DSLXC-5531..5580 | claim 已入库（50/50，dslinux_claims.duckdb）

## 38.1 【Linux社区】stable 测试覆盖之争：Pavel 的 Tested 标签与 Guenter 的实测反驳（9 例）

**要点（判定表逐字）**：Ken Moffat 以 prosumer 身份反驳 Sasha 关于无人测试 Linus 正式发布的假设，自述其测试 -rc 与 .0 内核的节奏，并指 -stable 版本常被跳过；Pavel Machek 提议在提交信息中加入 Tested: no 与 Tested: compile 标签，尤其针对 -stable 从新版本无测试地回移植补丁的问题；Guenter Roeck 反驳 Pavel，详述 stable 测试从五年前几乎不构建到如今 0day、kernelci、LKFT、qemu 百五十余配置启动的飞跃，回归率约 0.1% 至 0.3%，主张靠提升覆盖率而非逐补丁测试；Pavel Machek 回 Guenter，指出 0day 与 kernelci 对驱动代码帮助有限，核心变更可自动化、驱动却难，并指主线亦存在未测试的补丁；Guenter Roeck 回 Pavel，以刚从 -stable 取到的 xhci 修复与 ext4 补丁为例说明受益，并建议为冷门驱动实现 qemu 支持纳入测试农场，坦言自身 strncpy 替换仅编译测试；Pavel Machek 回 Guenter，同意 qemu 难以全覆盖，举 get_monotonic_boottime 替换 ktime_get_boot_ns 未测试的实例，主张以 Tested: compile 标注消除猜测；Greg KH 回 Pavel，讽其翻出两个月前的旧线程，指 stable 测试已达史上最盛，并谓若不喜欢 stable 大可不用，否则其抱怨将进 killfile；Willy Tarreau 回 Pavel，论证驱动比核心代码变更慢、回植修复多可直接套用，称 stable 用户侧回归率远低于修复率，LTS 分支累计约五千修复使单版残存 bug 远小于不安更新；Pavel Machek 回 Greg，辩称自己按 stable 规则标记补丁却遭另一套未成文规则责难，重申要 Tested: no／compile 头，并以未测试的 LED 补丁在 stable 合入、借口需 USB 键盘这一罕见硬件为由

**史料**：`348809`、`348810`、`348811`、`348814`、`348815`、`348816`、`348817`、`348818`、`348820`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348809 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348810 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348811 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348814 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348815 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348816 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348817 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348818 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348820 -->` 

**史观**：经验优先（总纲第 9 条——经验优先：以 stable 测试从五年前几乎不构建到 0day、kernelci、LKFT、qemu 百五十余配置启动的飞跃、回归率约 0.1% 至 0.3% 等实测为判据）；本体论上各方平等（总纲第 8 条——本体论上各方平等：Machek 的“Tested: no／compile”标签提案与 Roeck 的“靠提升覆盖率而非逐补丁测试”并置）
**辨析**：Roeck 的“回归率约 0.1% 至 0.3%”为其自陈统计，落书须与当期数据核对；Machek 的“以未测试的 LED 补丁在 stable 合入、借口需 USB 键盘这一罕见硬件为由”为具体反例；Greg KH 的“若不喜欢 stable 大可不用，否则其抱怨将进 killfile”为顶层态度，属措辞而非技术结论。
**文献**：DSLXC-5534、DSLXC-5535、DSLXC-5536、DSLXC-5539、DSLXC-5540、DSLXC-5541、DSLXC-5542、DSLXC-5543、DSLXC-5545（`ksummit-discuss.messages.348809`、`ksummit-discuss.messages.348810`、`ksummit-discuss.messages.348811`、`ksummit-discuss.messages.348814`、`ksummit-discuss.messages.348815`、`ksummit-discuss.messages.348816`、`ksummit-discuss.messages.348817`、`ksummit-discuss.messages.348818`、`ksummit-discuss.messages.348820`，2018-05-08、2018-07-14、2018-07-14、2018-07-14、2018-07-14、2018-07-14、2018-07-15、2018-07-15、2018-07-15），全文见 `raw_source.raw_json`

## 38.2 【Linux社区】stable 发版节奏之争：Laura 每周一发提案与各方回应（8 例）

**要点（判定表逐字）**：Laura Abbott 提交 [MAINTAINER SUMMIT] Stable trees and release time，以 Fedora 重度使用 stable 为例，提议固定周日发布、延长一周 -rc 窗口，便于规划测试与说服用户跟进；Jiri Kosina 回 Laura，以 SUSE 维护者身份要求参与，指 stable 树本非为发行版设计、应厘清目标，并问发行版反馈回路能否与 stable 闭环；Justin Forbes 回 Laura，认同每周节奏曾易用，主张每周至多一发 stable、仅严重安全问题例外，指推送每周两发对用户反成负担；Sasha Levin 回 Laura，反问何不自立发布节奏只取最新 stable，称强制 Greg 排程不过是把 .Z+1 顺延至 .Z+2，并无实质收益；Guenter Roeck 回 Laura，称延长 -rc 无益、反因大量安全修复而需抢先单独摘补丁，赞同每周至多一发（安全例外）但反对拉长 -rc；Guenter Roeck 回 Sasha，点出延长发布周期的副作用：发得更少则每发补丁更多、按恒定回归比例每发回归也更多；Laura Abbott 回 Sasha，辩称频繁更新对用户反馈不利、stable 回归后难引导用户 bisect，并称宁可测试已知提交集再发、接受顺延；Laura Abbott 回 Guenter，反驳称更长 -rc 可争取更多时间聚焦测试、在发布前抓出更多 bug

**史料**：`348828`、`348829`、`348830`、`348831`、`348832`、`348833`、`348834`、`348836`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348828 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348829 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348830 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348831 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348832 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348833 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348834 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348836 -->` 

**史观**：权力再分配（总纲第 3 条——不存在进步，只有权力再分配：stable 发版节奏之争实为发行版诉求与 stable 维护者排程权的再分配）；本体论上各方平等（总纲第 8 条——本体论上各方平等：Kosina 的“stable 树本非为发行版设计、应厘清目标”与 Abbott 的“便于规划测试”并列）
**辨析**：Abbott 的“提议固定周日发布、延长一周 -rc 窗口”为提案，Levin 的“何不自立发布节奏只取最新 stable，强制 Greg 排程不过把 .Z+1 顺延至 .Z+2”为反驳，两说对撞；Roeck 的“延长 -rc 无益、反因大量安全修复而需抢先单独摘补丁”为副作用之虑；Forbes 的“每周至多一发、仅严重安全问题例外”为折中。
**文献**：DSLXC-5553、DSLXC-5554、DSLXC-5555、DSLXC-5556、DSLXC-5557、DSLXC-5558、DSLXC-5559、DSLXC-5561（`ksummit-discuss.messages.348828`、`ksummit-discuss.messages.348829`、`ksummit-discuss.messages.348830`、`ksummit-discuss.messages.348831`、`ksummit-discuss.messages.348832`、`ksummit-discuss.messages.348833`、`ksummit-discuss.messages.348834`、`ksummit-discuss.messages.348836`，2018-09-04、2018-09-04、2018-09-04、2018-09-04、2018-09-04、2018-09-04、2018-09-04、2018-09-04），全文见 `raw_source.raw_json`

## 38.3 【Linux社区】stable 回归率与覆盖之辩（8 例）

**要点（判定表逐字）**：Laura Abbott 回 Guenter，指 Fedora 本就常携带未入 stable 的补丁，并论安全修复不等价、即便修 CVE 的补丁亦可能引发回归；Sasha Levin 回 Laura，追问多长算够、请给过去一年漏过 -rc 而由 Fedora 测试管线抓出的具体数字，称测试永无足够；Guenter Roeck 回 Laura，称仅零补丁系统才免回归、关键在提升测试至可接受，并述 CVE 按严重度有既定流程、首选经 stable 发布；Guenter Roeck 回 Sasha，补问现有测试周期抓到多少 bug、发布后用户报告多少回归，自陈早年统计 stable 回归率约 0.15%；Laura Abbott 回 Guenter，谓须翻 bugzilla 取数，并提及与遇困的 CoreOS 团队交流，将设法给出数字；Laura Abbott 回 Guenter，认同 CVE 终须过 stable，但指 stable 树中任何回归皆不应被接受，引 Greg 博客称服务器应用最新 stable／LTS，并呼应 Jiri 关于 stable 目标受众之问；Guenter Roeck 回 Laura，断言零回归等价于零改动，称只能靠提升覆盖率逼近、现实中必有发布后回归，并指每轮回归换来近千 bug 修复、今之回归率五年前曾是奢望；Eduardo Valentin 以 Amazon Linux 维护者身份加入，称依赖 stable 内核、疑延长 -rc 反增回归（更长等于更多补丁），望讨论回归引入、embargo 与 CVE 管理、发行版是否该用 stable／LTS

**史料**：`348837`、`348838`、`348839`、`348840`、`348841`、`348842`、`348843`、`348844`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348837 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348838 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348839 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348840 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348841 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348842 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348843 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348844 -->` 

**史观**：经验优先（总纲第 9 条——经验优先：以 Roeck 自陈早年统计 stable 回归率约 0.15%、每轮回归换来近千 bug 修复等实数为判据）；法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：CVE 与 stable 的关系、发行版该否用 stable／LTS，实为风险与责任的分摊）
**辨析**：Roeck 的“断言零回归等价于零改动”为结构性判断；Abbott 的“认同 CVE 终须过 stable，但指 stable 树中任何回归皆不应被接受”为价值主张，与 Roeck 的“只能靠提升覆盖率逼近”构成张力；Levin 的“追问多长算够、请给具体数字”为举证要求，Abbott 的“谓须翻 bugzilla 取数”为未答。
**文献**：DSLXC-5562、DSLXC-5563、DSLXC-5564、DSLXC-5565、DSLXC-5566、DSLXC-5567、DSLXC-5568、DSLXC-5569（`ksummit-discuss.messages.348837`、`ksummit-discuss.messages.348838`、`ksummit-discuss.messages.348839`、`ksummit-discuss.messages.348840`、`ksummit-discuss.messages.348841`、`ksummit-discuss.messages.348842`、`ksummit-discuss.messages.348843`、`ksummit-discuss.messages.348844`，2018-09-04、2018-09-04、2018-09-04、2018-09-04、2018-09-05、2018-09-05、2018-09-05、2018-09-05），全文见 `raw_source.raw_json`

## 38.4 【Linux社区】bug-introducing patches 议题与各树 fixes 分支（5 例）

**要点（判定表逐字）**：Boris Brezillon 在 bug-introducing patches 线程中向 Stephen Rothwell 提交 mtd-fixes 等分支供 linux-next 的 pending-fixes 测试用，并请求移除重复的 mtd 条目、将 l2-mtd 改名为 mtd；David Sterba 请 Stephen 将 kdave/linux.git 的 next-fixes 分支加入 linux-next，呼应此前把各子系统 -fixes 分支汇总供测试机器人消费的构想；Andy Shevchenko 提供 PDx86 的 fixes 分支（linux-platform-drivers-x86.git）供 linux-next，并提及 pending-fixes 分支已增至 55 个；Sasha Levin 提交 [MAINTAINERS SUMMIT] Bug-introducing patches 议题，指邮件难达共识、愿携数据与会，称此为低垂果实、解决可防住一批 bug；Daniel Vetter 回 Sasha，称该线程已散乱蔓延、自己忘掉大半，恳请先给问题与各方观点的摘要，否则恐重演同一场讨论

**史料**：`348806`、`348807`、`348808`、`348826`、`348827`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348806 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348807 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348808 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348826 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348827 -->` 

**史观**：动手者创造历史（总纲第 10 条——动手者创造历史：以 Brezillon、Sterba、Shevchenko 各送 fixes 分支供 pending-fixes 测试为分析单位）；分离聚合是永恒规律（总纲第 4 条——分离聚合是永恒规律：各子系统 -fixes 分支汇总供测试机器人消费，正是树间分合的相位）
**辨析**：Levin 的“指邮件难达共识、愿携数据与会，称此为低垂果实”为议程主张；Vetter 的“称该线程已散乱蔓延、自己忘掉大半，恳请先给问题与各方观点的摘要”为程序性要求，非议题否定；Shevchenko 的“提及 pending-fixes 分支已增至 55 个”为状态记录。
**文献**：DSLXC-5531、DSLXC-5532、DSLXC-5533、DSLXC-5551、DSLXC-5552（`ksummit-discuss.messages.348806`、`ksummit-discuss.messages.348807`、`ksummit-discuss.messages.348808`、`ksummit-discuss.messages.348826`、`ksummit-discuss.messages.348827`，2018-05-09、2018-05-11、2018-05-13、2018-09-04、2018-09-04），全文见 `raw_source.raw_json`

## 38.5 【Linux社区】stable 审阅流失与补遗（5 例）

**要点（判定表逐字）**：Theodore Ts'o 解释此前卡在 ksummit-discuss 审核队列的旧信被放出，并补刀称该线程两月前已被讨论殆尽，另讽不喜 stable 者要么不用、要么去买企业发行版；Sasha Levin 回 Laura，劝 Fedora 可在节奏不合时跳过某发 stable、以 .Z 推进而下发用 .Z+2，称二者提交集与强制 Greg 排程时完全一致；Jiri Kosina 回 Sasha，指当前节奏下排队入 stable 的邮件洪流致无人细看，降频可增审阅可能，并批 stable 准入门槛低于 stable-kernel-rules.rst 所载、恐致发行版弃用；Jan Kara 回 Jiri Kosina，同意当前 stable 审阅流于形式、根因在补丁量而非发版频率，并析发行版靠 bugzilla 反馈回路、嵌入式因回路弱须更激进捡修复，Greg 取舍偏后者；Jan Kara 回 Guenter，赞同即便企业发行版有全套 QA 与审阅亦偶发回归，对用户真正重要的是更新后工作负载崩坏的概率，可降至 1%、0.1% 或 0.01% 但永不可为 0

**史料**：`348819`、`348848`、`348849`、`348853`、`348855`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348819 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348848 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348849 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348853 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348855 -->` 

**史观**：本体论上各方平等（总纲第 8 条——本体论上各方平等：Kosina 的“stable 准入门槛低于 stable-kernel-rules.rst 所载、恐致发行版弃用”与 Kara 的“根因在补丁量而非发版频率”并置）；经验优先（总纲第 9 条——经验优先：以 Kara 的“发行版靠 bugzilla 反馈回路、嵌入式因回路弱须更激进捡修复”等结构性观察为判据）
**辨析**：Ts'o 的“讽不喜 stable 者要么不用、要么去买企业发行版”为顶层态度；Kara 的“对用户真正重要的是更新后工作负载崩坏的概率，可降至 1%、0.1% 或 0.01% 但永不可为 0”为量化框架，属概念性说明；Levin 的“劝 Fedora 可跳过某发 stable、以 .Z 推进而下发用 .Z+2”为可行性主张。
**文献**：DSLXC-5544、DSLXC-5573、DSLXC-5574、DSLXC-5578、DSLXC-5580（`ksummit-discuss.messages.348819`、`ksummit-discuss.messages.348848`、`ksummit-discuss.messages.348849`、`ksummit-discuss.messages.348853`、`ksummit-discuss.messages.348855`，2018-07-15、2018-09-05、2018-09-05、2018-09-05、2018-09-05），全文见 `raw_source.raw_json`

## 38.6 【Linux社区】Intel 图形 embargo 开发之争（7 例）

**要点（判定表逐字）**：Rodrigo Vivi 提交 [MAINTAINERS SUMMIT] 议题：Intel 图形内部开发与 embargo 开发对上游的矛盾，拟谈上游优先经验，寻 hallway 或 BOF 交流各维护者 embargo 流程；Leon Romanovsky 回 Rodrigo，质问 embargo development 究竟指何物（是否美国政府限制）、外界为何须知悉 Intel 内部开发流程；Rodrigo Vivi 回 Leon，澄清 embargo 与公司临时限制无关政府，申明 i915 坚守上游优先、愿分享闭源式开发转型的经验与工具，并开放实质问题求反馈；Leon Romanovsky 回 Rodrigo，以 Mellanox 由闭源转上游的经历称改动皆在公司内部，坦言难见此议题契合 kernel summit 形式，劝其先在本列表亮明问题；Greg KH 回 Rodrigo，直问上游为何要在意 Intel 内部延迟上游的流程，称若上游优先遇公司内部阻力、开内部会议才是解法，并请其把话题讲清楚；Greg KH（自 greg@kroah.com 重发）内容与 pk 348851 几乎一致，再问上游为何须在意 Intel 的 embargo 流程、并请 Rodrigo 把欲谈的进程改进讲明白（近重复 pk 348851）；Daniel Vetter 回 Greg，为 Rodrigo 辩护：图形界除完全不在乎上游者外皆受闭门专有硬件拖累，此非 Intel 独有，邀众人交流上游优先的应对经验本在 ks／lpc 范畴

**史料**：`348825`、`348845`、`348847`、`348850`、`348851`、`348852`、`348854`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348825 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348845 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348847 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348850 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348851 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348852 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348854 -->` 

**史观**：本体论上各方平等（总纲第 8 条——本体论上各方平等：Romanovsky 的“难见此议题契合 kernel summit 形式，劝其先在本列表亮明问题”与 Vetter 的“邀众人交流上游优先的应对经验本在 ks／lpc 范畴”并置）；文化即形式主义（总纲第 15 条——文化即形式主义：上游优先与 embargo／闭门专有硬件的冲突，正是社区成文规范与企业内部流程两种形式主义的对撞）
**辨析**：Romanovsky 的“质问 embargo development 究竟指何物（是否美国政府限制）”为误解，Rodrigo 已澄清“embargo 与公司临时限制无关政府”；Greg KH 的“直问上游为何要在意 Intel 内部延迟上游的流程”为质询；Vetter 的“图形界除完全不在乎上游者外皆受闭门专有硬件拖累，此非 Intel 独有”为辩护，属立场陈述。
**文献**：DSLXC-5550、DSLXC-5570、DSLXC-5572、DSLXC-5575、DSLXC-5576、DSLXC-5577、DSLXC-5579（`ksummit-discuss.messages.348825`、`ksummit-discuss.messages.348845`、`ksummit-discuss.messages.348847`、`ksummit-discuss.messages.348850`、`ksummit-discuss.messages.348851`、`ksummit-discuss.messages.348852`、`ksummit-discuss.messages.348854`，2018-09-04、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05），全文见 `raw_source.raw_json`

## 38.7 【Linux社区】at91 树入 linux-next、2018 峰会筹备与 2014 档案五封（8 例）

**要点（判定表逐字）**：Nicolas Ferre 请 Stephen 将 at91 树改为公共 kernel.org 树（git.kernel.org/at91/linux.git）的 at91-next 与 at91-fixes 分支，替换个人 nferre 树，并附 2015 年原始请求；Stephen Rothwell 确认已将 at91 新树及 at91-fixes 加入 linux-next，并说明 linux-next 旨在集成测试、降低合并窗口冲突，要求补丁具 Signed-off-by 且经审阅与单元测试；Theodore Ts'o 发布 2018 年温哥华 Maintainer／Kernel Summit 筹备启事：11 月 12 日 Maintainer Summit（限三十人，Linus 据 git 统计点名十人），Kernel Summit 并入 LPC 并行轨道；[MAINTAINERS SUMMIT] 与 [TECH TOPIC] 标签规则与九月二十一日截稿；Jan Kara（2014 档案）就内核精简与禁用 syscall 的 CONFIG 选项回 NeilBrown，认为安全模块／审计已可限制攻击面，对发行版默认策略禁止 r_f_p 一类 syscall 表示存疑；Rafael Wysocki（2014 档案）在能耗偏置接口线程中质疑把用户一律当作懂 turbo 的决策者，并追问任务如何声明其延迟需求，主张不宜过度依赖用户输入；NeilBrown（2014 档案）支持 Takashi Iwai 的提交元数据附议，提出 git-bisect 在需后续提交才能编译的区间里反复手工套用的问题，建议标记重要后继提交并加 --always-include-important-children；Rafael Wysocki（2014 档案）在能耗偏置接口线程中总结：讨论回到实质等价于三级中央旋钮（balanced／performance／powersave），由内核据这些档自行微调底层；Jiri Kosina（2014 档案）回 NeilBrown，给出 git-bisect 的变通：把必备后继提交存单独分支、用脚本先合并再重置，git 可从容处理已合入补丁的合并

**史料**：`348821`、`348822`、`348823`、`348812`、`348813`、`348824`、`348835`、`348846`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348821 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348822 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348823 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348812 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348813 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348824 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348835 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348846 -->` 

**史观**：动手者创造历史（总纲第 10 条——动手者创造历史：以 Ferre 将 at91 树改为公共 kernel.org 树、Kosina 给出 git-bisect 变通脚本为分析单位）；知识注定过时（总纲第 22 条——知识注定过时：git-bisect 在需后续提交才能编译的区间里反复手工套用之弊，及 --always-include-important-children 之议）
**辨析**：Ts'o 的“2018 温哥华 Maintainer／Kernel Summit 筹备启事（限三十人，Linus 据 git 统计点名十人）”为组织实况；Kara 的“对发行版默认策略禁止 r_f_p 一类 syscall 表示存疑”为安全立场；Wysocki 的“总结：讨论回到实质等价于三级中央旋钮（balanced／performance／powersave）”为收敛性结论。
**文献**：DSLXC-5546、DSLXC-5547、DSLXC-5548、DSLXC-5537、DSLXC-5538、DSLXC-5549、DSLXC-5560、DSLXC-5571（`ksummit-discuss.messages.348821`、`ksummit-discuss.messages.348822`、`ksummit-discuss.messages.348823`、`ksummit-discuss.messages.348812`、`ksummit-discuss.messages.348813`、`ksummit-discuss.messages.348824`、`ksummit-discuss.messages.348835`、`ksummit-discuss.messages.348846`，2018-08-22、2018-08-22、2018-08-30、2014-05-02、2014-05-13、2014-05-13、2014-05-13、2014-05-13），全文见 `raw_source.raw_json`

---
注：本文件由判定表程序化生成（7 块，覆盖 50/50 CAND，两遍计数核对通过）；要点逐字取自判定表“要点”列（主代理全读审读实录），史料锚与 CAND 一一对应，全文以 raw_source.raw_json 为准。
