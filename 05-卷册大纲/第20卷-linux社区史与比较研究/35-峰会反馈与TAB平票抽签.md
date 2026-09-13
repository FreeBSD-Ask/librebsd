# 35-峰会反馈与TAB平票抽签.md

> 对应页面：ksummit-discuss p88（pk 348606-348655，2017 布拉格峰会会后收尾 + 2014 档案信）
> 判定：50 CAND / 0 NV
> 编号：DSLXC-5381..5430 | claim 已入库（50/50，dslinux_claims.duckdb）

## 35.1 TAB 选举平票随机抽签与纪要传统（6 例）

**要点（判定表逐字）**：Laurent Pinchart 就 TAB 2017 选举追问：若仅以一票之差避免的平票真的发生、有无既定处理程序；附选举结果（Rostedt 58、Corbet 57、Greg KH 57、Tim Bird 39、Ted Ts'o 37，共 73 票）；Randy Dunlap 续问 TAB 近年会议纪要去向（wiki 仅至 2010），指自己亦有逐年追问此传统的习惯，反映 TAB 透明度问题；H. Peter Anvin 答平票处理：胜者经随机抽签，扫描脚本以 /dev/urandom 给每位候选人分配 tiebreaker 号，亦曾考虑实体硬币；过去有过未越过 cut line 的平票；Matthew Wilcox 打趣索要 write-in 候选人名单并问 Batman 今年几票，属 TAB 选举线程的轻松互动；Steven Rostedt 答：Batman 仅 1 票，Joker 亦 1 票，延续选举线程的幽默；Dave Taht 引 Heinlein lottery 概念，主张候选人可完全随机抽选以鼓励参与，回应 hpa 平票随机抽签的讨论

**史料**：`348607、`348608、`348609、`348615、`348616、`348617

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.348607 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348608 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348609 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348615 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348616 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348617 -->` 

## 35.2 峰会反馈：形式、规模与信息可达性（10 例）

**要点（判定表逐字）**：Theodore Ts'o 开启 Maintainer's Summit 2017 反馈线程，征询来年办会改进意见（Linus 对形式尚满意，拟沿用）；Theodore Ts'o 开启 Kernel Summit 2017 反馈线程，并预告来年 Kernel／Maintainer Summit 将与 Linux Plumbers 在费城同地举办；Laura Abbott 询问 unconference 实际讨论了什么，指不知情导致未参与，反映非会议形式的信息可达性问题；Takashi Iwai 反馈小组规模合适（似延伸走廊谈），但房间有柱且过大、备餐噪音扰人；建议峰会前设发行版内核 open session；Theodore Ts'o 答 Laura Abbott：本年仅用一处 unconference 时段（续 Linux 安全讨论），较 Santa Fe 年逊色，拟来年设 wiki 报名；Arnd Bergmann 指许多人根本不知新形式与参与方式，当日才获悉可参加，认同 Ted 设 wiki 之议；Theodore Ts'o 反思沟通不足：曾数月前于列表公告、前一周发议程注 open to badge，却未抄 LKML 怕刷屏，自承低估告知频次；Shuah Khan 反馈小组规模利于回归与维护者讨论，但缺 lightning talks，盼纳入新形式或 unconference，并求跨子系统讨论（Kees 所提）纪要；Jiri Kosina 反馈形式总体成功，但房间有柱与噪音，且人数略偏小（建议约 40），首次限员仍在收敛最佳规模；Mark Brown 指继续称 Kernel Summit 与 Open Day 致混淆（需时方知 Kernel Summit 已成开放部分、邀请制另立名），望来年更清晰

**史料**：`348619、`348620、`348622、`348632、`348635、`348636、`348643、`348646、`348648、`348651

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.348619 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348620 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348622 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348632 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348635 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348636 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348643 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348646 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348648 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348651 -->` 

## 35.3 维护者职责文档之倡议（3 例）

**要点（判定表逐字）**：Bart Van Assche 反馈：在维护者峰会上比读 Linus 邮件更懂其对维护者的期望，提议内核树内增设说明维护者职责之文档；Dan Williams 认同并承诺一两周内起草维护者职责文档初稿，呼应 Bart 之议（此即日后维护者文档之滥觞）；Mimi Zohar 追问 Linus 峰会发言摘要，并望 Dan Williams 的维护者文档能在下个合并窗口前出炉

**史料**：`348627、`348628、`348631

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.348627 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348628 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348631 -->` 

## 35.4 0-day 与测试体系归属之辩（8 例）

**要点（判定表逐字）**：Bart Van Assche 转述 Linus 明言回归不可接受，主张扩大 0-day 自动测试覆盖并考虑把测试文档移入仓库或 kernel.org 链接；Theodore Ts'o 答 Bart：0-day 已对 v4.14-rc6 发系列报告，硬件特定驱动回归难靠自动测试，举 Intel Wireless 对 Aruba AP 回归为例，主张维护者自测方可扩展；Greg KH 答 Bart：若有 0-day 未跑的测试可自加（客户端代码在 github），反问是否要把所有测试系统都链上 kernel.org；Konstantin Ryabitsev 指 bottest.wiki.kernel.org 宜作测试系统汇总之处，回应 Greg 的链接之问；James Bottomley 补：wiki应列自动运行、须申请覆盖、须自跑三类信息，方对开发者有用；Bart Van Assche 追问开发者应在 0-day、ltp、ktest、xfstests、blktests 间如何选择新增测试，指 0-day 是其唯一所知自动运行者；Greg KH 列举 kernel.ci 等更多测试系统，并提醒 Bart 漏了 kselftest，按测试类型选择即可；Julia Lawall 澄清 0-day 系从别处取测试、并非直接往里加测试，续 Bart／Greg 的测试归属之辩

**史料**：`348629、`348637、`348638、`348639、`348640、`348641、`348642、`348647

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.348629 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348637 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348638 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348639 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348640 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348641 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348642 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348647 -->` 

## 35.5 DT 研讨会纪要、幻灯片与 Action Items（9 例）

**要点（判定表逐字）**：Frank Rowand 在 DT 研讨会前分享 dtc 源码位置标注概念（RFC PATCH v6 2015），用 --annotate 在输出 dts 注释节点与属性的源文件行号，便于校验时回报出处；Grant Likely 通知未报名者亦可到场 DT 研讨会（房间充裕，9:30 开始），并附完整日程：YAML 编码、Schema 两方案、运行时内存、ABI 稳定性、EBBR 等；Grant Likely 发布 Devicetree Workshop 纪要幻灯片至 elinux.org（待写总结），并持全天音频录音（每文件 100-200MB 未定发布方式），点名谢 Julia Lawall 等；Frank Rowand 纠 Grant 把其名误拼为 Frank Roland，以 Rowand 更正，属研讨会纪要线程小事；Grant Likely 为误拼 Frank Rowand 之名致歉，称手快所致，延续研讨会纪要线程；Rob Herring 质疑 Grant 所传幻灯片是 2016 LPC 旧 deck（且标 PDF 实为 ODP），并问纪要中 JSON Schema 与 eBPF 取向；Grant Likely 答 Rob：2017 内容在 2016 段之下，并定案 Pantelis 与其合并方案——以 JSON Schema 为主加 DT 扩展，eBPF 编码其中；Pantelis Antoniou 建 DT 研讨会初始 Action Items wiki（elinux.org 专页），邀众人增补，续纪要线程；Matthias Brugger 于 DT 研讨会纪要线程贴出合影 flickr 链接，补全 Grant 待发之群组照

**史料**：`348611、`348614、`348624、`348625、`348626、`348630、`348644、`348649、`348655

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.348611 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348614 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348624 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348625 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348626 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348630 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348644 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348649 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348655 -->` 

## 35.6 议程后勤、tree-wide 标签、printk 复盘与 2014 档案（14 例）

**要点（判定表逐字）**：Megan Phillips 确告 Maintainers Summit 会议室为 Chez Louis，回应 Greg KH 对 Ted Ts'o 议程中房间安排的追问（布拉格峰会后勤）；James Bottomley 追问 Greg KH 关于峰会房间安排的答复是否已达，属议程后勤跟进；James Bottomley 转达 Megan 私邮确认房间为 Chez-Louis（其无法发往列表），补全议程房间疑问；Michael Kerrisk 顺带询问来年 LPC 具体日期，属峰会排期后勤；Theodore Ts'o 答 Michael Kerrisk：来年 LPC 为 2018 年 11 月 12-15 日；Bart Van Assche 回应 2017 端序标注技术议题：将查看 GCC bugzilla 第 59852 号（把 Sparse 的 __attribute__((bitwise)) 引入 GCC）提案，关乎跨树驱动代码质量；Rob Herring 于 tree-wide changes 线程提 Needs-Acked-by 标签（存于 commit、便于过滤），并主张区分子系统维护者与单驱动维护者、关 git log 猜测 Cc；Kees Cook 续 tree-wide changes：峰会拟用 [RFACK][PATCH] 主题标签求确认；主张 MAINTAINERS 增 U:（upstream）字段以建升级路径，指 wireless 有多层维护者；Joe Perches 求 printk 讨论复盘（议程中 Petr Mladek 与 Steve Rostedt 的 Printk redesign 时段），因无直播；Jonathan Corbet 答 Joe Perches 将尽快补 printk 讨论复盘；Andy Lutomirski 于 2014 QR oops 线程辨析：base32 较 base64 多约两成字符，但启用 alphanumeric 二维码可存更多字符，整体未必更浪费；Mark Brown 于 2014 子系统维护者指引线程论补丁测试属社会问题，git／-next 仅把问题下移；cross-subsystem 改动难追踪去向，主张人际沟通与跨树合并，讽手工 Applied 邮件；Mark Brown 于 2014 ACPI／DT 线程指嵌入式 x86 已有上游 ACPI（Haswell／Baytrail 音频），多为主动 ACPI 模型，关切其与 DT 风格不一；Arnd Bergmann 于 2014 ACPI／DT 线程：私下嵌入式 fork 用 out-of-tree ACPI、未审 DT 绑定或 FEX 皆可，但别指望合入上游

**史料**：`348606、`348610、`348613、`348621、`348633、`348618、`348653、`348654、`348650、`348652、`348612、`348623、`348634、`348645

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.348606 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348610 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348613 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348621 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348633 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348618 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348653 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348654 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348650 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348652 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348612 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348623 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348634 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348645 -->` 

---
注：本文件由判定表程序化生成（6 块，覆盖 50/50 CAND，两遍计数核对通过）；要点逐字取自判定表「要点」列（主代理全读审读实录），史料锚与 CAND 一一对应，全文以 raw_source.raw_json 为准。
