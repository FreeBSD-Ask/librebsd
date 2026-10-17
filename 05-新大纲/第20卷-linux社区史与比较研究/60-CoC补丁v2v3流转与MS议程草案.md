# 60 【Linux社区】CoC补丁v2v3流转与MS议程草案

> 来源：ksummit-discuss p112（50 封全读，2018-10-10/16，夹杂 KS2014 档案信 2014-05-02/15）。
> 判定：50 CAND / 0 NV。主题分布：coc 44、KS2014 6。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p112（pk 349806-349855）的逐封提取（50 CAND / 0 NV），全 8 块采用**导语＋带锚条目体例**：每块由“## 60.x 【Linux社区】题名”＋导语段＋“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——导语段承担“要点”职能、带锚条目承担“史料”与“史料锚”职能（ROW_MINE 坐标与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 60.1 【Linux社区】[PATCH v2/v3 0/3] 全文流转与 Acked 潮

2018-10-10/16 CoC 补丁系列的 v2→v3 全文流转：三补丁形态定型（email 修复/剥 enforcement 起点非终点/Reporting 节回归+except where required by law）、Acked-Reviewed 潮名单与 Mauro 的个人身份署名更正。

- 【Linux社区】Bottomley [PATCH v2 0/3]：重发显示累计 tags+新增第三补丁（TAB 列为报告点——几人想要；支持度相当则一并提交） `<!-- ROW_MINE: ksummit-discuss.messages.349819 -->`
- 【Linux社区】[PATCH v2 1/3] 全文：email 修复+累计 tags（Acked Geert/Shuah/Roeck+Reviewed Cox/Mauro+Fixes 8a104f8b5867） `<!-- ROW_MINE: ksummit-discuss.messages.349820 -->`
- 【Linux社区】[PATCH v2 2/3] 全文：剥 enforcement+新增段“此补丁是讨论起点非终点——社区共识足够后预期再加 Enforcement 节”（v2 应 Shuah 要求） `<!-- ROW_MINE: ksummit-discuss.messages.349821 -->`
- 【Linux社区】[PATCH v2 3/3] 全文：加回 Reporting 节 10 行（TAB 报告点+保密承诺）——“意图仍是辩论该放什么、眼下先恢复旧 code of conflict 的中央报告点” `<!-- ROW_MINE: ksummit-discuss.messages.349823 -->`
- 【Linux社区】[PATCH v3 0/3]：第三补丁改加（except where required by law）+再累计 tags——三补丁终态 5+/9- `<!-- ROW_MINE: ksummit-discuss.messages.349855 -->`
- 【Linux社区】Biederman Acked v2 1/3 `<!-- ROW_MINE: ksummit-discuss.messages.349839 -->`
- 【Linux社区】Kees Acked v2 1/3 `<!-- ROW_MINE: ksummit-discuss.messages.349851 -->`
- 【Linux社区】Mauro 接受 Cox should 措辞：“Works for me” `<!-- ROW_MINE: ksummit-discuss.messages.349828 -->`
- 【Linux社区】Konrad Wilk Reviewed-by v2 3/3（“Thank you!”） `<!-- ROW_MINE: ksummit-discuss.messages.349833 -->`
- 【Linux社区】Geert：“按 Cox 加（except where required by law）后：Acked-by v2 3/3” `<!-- ROW_MINE: ksummit-discuss.messages.349849 -->`
- 【Linux社区】Mauro：“按 Alan 提议改后可加我的 Reviewed-by” `<!-- ROW_MINE: ksummit-discuss.messages.349844 -->`
- 【Linux社区】Mauro：“请把我的 Reviewed-by 改为 mchehab@kernel.org——以个人身份非雇主” `<!-- ROW_MINE: ksummit-discuss.messages.349845 -->`

## 60.2 【Linux社区】should 措辞与执行语义之辩

right and responsibility→may→should 的措辞演化全程：Geert 五步清单与责任普遍化修正案、Cox 的 should 定稿与 0day 笑谈、Airlie 的现实主义的驳。

- 【Linux社区】Geert 维护者执行任务五步清单（回复澄清/删改评论/编辑补丁/拒补丁/封禁——2 公开列表做不到、5 需求助管理员）；自拟修正“Maintainers are responsible→All project members are encouraged” `<!-- ROW_MINE: ksummit-discuss.messages.349806 -->`
- 【Linux社区】Cox 驳 may remove：“同样混乱——维护者对符合 CoC 的提交也有权删改——所以重点是什么？” `<!-- ROW_MINE: ksummit-discuss.messages.349808 -->`
- 【Linux社区】Mauro 答 Cox：“重点是 responsibility——听着像套法律义务；对 Github 有理（公司不想为每帖担责）但邮件流不行——分布式存储维护者无法 remove/edit/reject 邮件” `<!-- ROW_MINE: ksummit-discuss.messages.349815 -->`
- 【Linux社区】Cox 提案“Maintainers should remove, edit or reject”——保留对 abusive 行为施压之意；“当然有人会把 0day exploit+fix 附在违反 CoC 的咆哮里——那你就尴尬了 8)” `<!-- ROW_MINE: ksummit-discuss.messages.349822 -->`
- 【Linux社区】Cox 答 v2 3/3：“我会加（except where required by law.）” `<!-- ROW_MINE: ksummit-discuss.messages.349826 -->`
- 【Linux社区】Airlie 答 Cox 0day 假设：“为什么？仍可与那人谈行为、建议其改——带着 0day 的混蛋多半不会发给我们” `<!-- ROW_MINE: ksummit-discuss.messages.349829 -->`
- 【Linux社区】Mauro Reviewed-by v2 2/3；“我仍认为本系列该含第四补丁：responsibilities 节按 Alan 文本改 right and responsibility→should” `<!-- ROW_MINE: ksummit-discuss.messages.349847 -->`

## 60.3 【Linux社区】巴西 Whatsapp 群 CoC 实测与习语陷阱

CoC 执行的两组现场证据：Mauro 的百人 Whatsapp 群“回 CoC 引用无用论”与非母语习语陷阱实录（key signing party 漏词）、Triplett 的 intent 分级与 git 历史 permanence 之辩。

- 【Linux社区】Mauro 巴西 Whatsapp 群 CoC 实测：百人群禁政治帖、每次有人贴政治有人回 CoC——“没用；昨天一条引发数百帖、几十条 CoC 引用、两人退群——回 CoC 可能激化战火”；可行动作三条（任何成员回复澄清/维护者编辑违规补丁/建议 ML 管理员封禁） `<!-- ROW_MINE: ksummit-discuss.messages.349807 -->`
- 【Linux社区】Triplett 答 Mauro 习语：“无意用词一封回复即可处理；对比故意者：key-party 脚本满是双关——听着荒唐、FOSS 史上先例不少” `<!-- ROW_MINE: ksummit-discuss.messages.349816 -->`
- 【Linux社区】Mauro：“作为维护者、若补丁含此类表达我很可能直接合入而不自知” `<!-- ROW_MINE: ksummit-discuss.messages.349817 -->`
- 【Linux社区】Triplett：“intent 概念同样适用——真是错误就不致命；你会很快应用修复补丁（对比被要求改就暴跳如雷者）” `<!-- ROW_MINE: ksummit-discuss.messages.349818 -->`
- 【Linux社区】Mauro：“除非很快收到修复、我不会 rebase 树——坏措辞永远留在 git 历史、还可能被回移 -stable” `<!-- ROW_MINE: ksummit-discuss.messages.349825 -->`
- 【Linux社区】Triplett：“It happens. 不是世界末日——不会指望为这点小事 rebase 工作树” `<!-- ROW_MINE: ksummit-discuss.messages.349827 -->`

## 60.4 【Linux社区】revert 呼声与“4.19 魔力”/独裁者交锋

revert 路线的民意与程序之辩：Pavel/Dunlap 的“未走流程”双证、Luck 与 Bottomley 的“独裁者 git push 即生效吗”交锋、Kees 的 -stable 修复路径提议。

- 【Linux社区】Pavel Machek：“正是我的想法；revert 然后正经讨论听上去合适（今年大概去不了峰会——邮件列表上也该讨论）” `<!-- ROW_MINE: ksummit-discuss.messages.349809 -->`
- 【Linux社区】Randy Dunlap：“Exactly——我们有流程、4.19-rc4 的 CoC 补丁没走它；Ditto（revert+正经讨论）” `<!-- ROW_MINE: ksummit-discuss.messages.349810 -->`
- 【Linux社区】Pavel：“若来自某种 upstream 应在文档或 git log 明示——我一直好奇谁写了这份 useful document（也想知道背景故事）” `<!-- ROW_MINE: ksummit-discuss.messages.349814 -->`
- 【Linux社区】Luck：“4.19 有什么魔力？我们的仁慈独裁者提交了补丁——他 git push 让世界可见时就生效了吧？” `<!-- ROW_MINE: ksummit-discuss.messages.349832 -->`
- 【Linux社区】Bottomley 答：“有逻辑——Linux 走编号发布、发布是止改的官方节点；4.19 是 CoC 变更后首个发布；通常人们须同意此类变更——同意是可变概念、可简单到某时限前不反对” `<!-- ROW_MINE: ksummit-discuss.messages.349836 -->`
- 【Linux社区】Luck：“也许你该复习一下独裁者一词的意思 :-)” `<!-- ROW_MINE: ksummit-discuss.messages.349837 -->`
- 【Linux社区】Kees：“Greg 说 4.19 将是下个 LTS；若把 CoC 的 bug 当 bug——修复也可进 -stable、落在 4.19.z；不必赶 4.19——花时间把 CoC 做对符合我们自己的利益” `<!-- ROW_MINE: ksummit-discuss.messages.349852 -->`

## 60.5 【Linux社区】政治声明之辩与 RFC 程序

Geert 删列表补丁的政治维度：Rowand 的“政治声明不属于文档”与 ESR 的 RFC/rough consensus 程序论、Triplett 的“不删也是政治声明”对称反驳。

- 【Linux社区】Rowand patch 1/2 措辞之疑：“‘ordinarily collected by the project’≠‘在项目公共空间提供的地址’——ordinarily collected 可含预期私密的采集；我同意底层概念、问题是措辞” `<!-- ROW_MINE: ksummit-discuss.messages.349830 -->`
- 【Linux社区】Rowand Acked Geert 删列表补丁：“被删的词是政治声明——不属于文档” `<!-- ROW_MINE: ksummit-discuss.messages.349831 -->`
- 【Linux社区】Arnaldo Acked Geert 删列表（附和 Rowand 政治声明论） `<!-- ROW_MINE: ksummit-discuss.messages.349834 -->`
- 【Linux社区】Triplett 答 Rowand：“不说是政治声明也是政治声明；见原 commit message Explicit guidelines have demonstrated success；见 FAQ 条目（我写并上游热情 merge）” `<!-- ROW_MINE: ksummit-discuss.messages.349838 -->`
- 【Linux社区】Rowand 引 ESR：“选择受保护类是 CoC 隐含政治的改变——从 LKML 流量看显然极有争议——若是纯技术事务会被描述为 not backwards-compatible——不该未经明确共识而做；我们的文化有流程叫 RFC——达成 rough consensus 才改”；“谢谢 Eric 清晰表述——我退出此点后续讨论” `<!-- ROW_MINE: ksummit-discuss.messages.349841 -->`

## 60.6 【Linux社区】Biederman 三问题与 Viro 树型论

Our Responsibilities 节的结构性批评：Biederman 三问题（git 不可编辑/责任不对称/语气失配）+ Viro 第四问题（列表 moderation 物理不可持续）与 Bottomley 的逐条回应、Mauro 的 FAQ 提议与“集中式模型不适配”总评。

- 【Linux社区】Biederman Our Responsibilities 节三问题：a) append-only git 无法编辑历史——要求做不可能的事；b) 非维护者无任何责任；c) 整节语气与“只能说服不能强制”的社区不符——“越来越觉得这文档不适合 Linux 开发社区——或许 revert 后从头写” `<!-- ROW_MINE: ksummit-discuss.messages.349840 -->`
- 【Linux社区】Viro 补 d) 条：“要么邮件列表豁免、要么把物理上不可持续的负担压给某人（vger 系默认 davem）——记得买包含精神治疗的保险”；“这让我想起大家都换成唯一真版本控制+唯一真 IDE 式提案——别指望所有人换” `<!-- ROW_MINE: ksummit-discuss.messages.349842 -->`
- 【Linux社区】Bottomley 答：“Git 不完全 append only——进 Linus 树前可 amend；b) 同意——无实权结构的社区里遵守 CoC 是每个人的责任；c) 说服与领导并存——说服型领导者并非无力；policing 是错词——没人有 policing power 但仍有说服力；revert 我开放——这类文档难写正是保留的理由” `<!-- ROW_MINE: ksummit-discuss.messages.349843 -->`
- 【Linux社区】Mauro 答 Biederman：“MS/KS 应多谈 rebase——rebase 该是例外不是规则；我会在 FAQ 或 CoC 本身加：维护者不会因 CoC 做 git rebase——投诉应尽快回以便合并前看到；此 CoC 模式太绑集中式网站托管模型、缺去中心化邮件流适配——后续可能须替换或大改” `<!-- ROW_MINE: ksummit-discuss.messages.349848 -->`
- 【Linux社区】Dan Carpenter：“其实你该对 TAB 之外的人保密报告——几年后他们会面试你找工作” `<!-- ROW_MINE: ksummit-discuss.messages.349850 -->`

## 60.7 【Linux社区】Maintainer's Summit 议程草案与出席名单

温哥华 Maintainer's Summit 议程草案全文与 30 人名单、Vetter 的“CoC 运营经验者缺席”程序批评——本战线下阶段的事实坐标。

- 【Linux社区】Ted 发布 Maintainer's Summit 议程草案：12:00 CoC: How did we get here report-out/12:30 CoC: next steps/1:00 stable 对社区发行版更有用（Abbott）/1:30 API 替换与弃用（Kees）/2:00 embargo 安全议题（Kosina）/3:30 旧硬件弃用（Arnd）/4:00 EXPORT_SYMBOL_GPL 指南（Greg）/5:00 峰会反馈；出席者 30 人全名单 `<!-- ROW_MINE: ksummit-discuss.messages.349853 -->`
- 【Linux社区】Vetter：“CoC 在议程上、而唯一对完全相同 CoC 有实际运营经验的子系统（fd.o/dri-devel）无人出席——也没请外部社区有真经验者或该领域顾问补位” `<!-- ROW_MINE: ksummit-discuss.messages.349854 -->`

## 60.8 【Linux社区】KS2014 档案六封

页内夹杂的 KS2014 档案信（2014-05-02/15）：syscall 攻击面 profiles、ACPI-DT 两股人流、printk 话多与 NMI 加剧、Howells 头文件重构八步纲领。

- 【Linux社区】Dave Jones 论 syscall 可选化：核心/可选分界难、CONFIG_SECURE_ROUTER/REDUCED_ATTACK_SURFACE profiles、“两个 flavor 时间长了必然蠕回”、runtime 禁用或更通用（2014-05-02 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349811 -->`
- 【Linux社区】Arnd 论 ACPI/DT 统一资源 API：IRQ/MMIO 已有可扩、两股人流需求迥异终局可能不同、点破 Olof 漏了自己的 ACPI 转 DT 提案（2014-05-03 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349812 -->`
- 【Linux社区】Triplett 响应 printk softlockups：“内核默认话太多——默认输出只该有 what went wrong”；判据法则“出问题时还能否经用户态日志取到”（2014-05-15 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349813 -->`
- 【Linux社区】Kosina printk NMI 加剧论：“NMI 上下文调用时彻底锁死机器不可调试——我们花了大量时间修”（2014-05-15 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349824 -->`
- 【Linux社区】Howells 头文件重构八步纲领：UAPI 分离 Mostly done（__KERNEL__ 残留 97/CONFIG 残留 83）、**sched.h**/**mm.h**/**fs.h**/**security.h**/**audit.h** 拆分设想、三态防重入守卫、头文件单测与 DB 工具构想（2014-05-15 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349835 -->`
- 【Linux社区】Pinchart PM dependencies 道歉信：“没 CC Rafael 是我的无心之过”（2014-05-15 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349846 -->`
