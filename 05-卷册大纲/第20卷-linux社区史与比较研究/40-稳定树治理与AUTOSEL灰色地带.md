# 40 【Linux社区】稳定树治理与AUTOSEL灰色地带

> 对应页面：ksummit-discuss p93（pk 348856-348905，2018 稳定树治理与 AUTOSEL 灰色地带之争 + 2014 档案信）
> 判定：50 CAND / 0 NV
> 编号：DSLXC-5631..5680 | claim 已入库（50/50，dslinux_claims.duckdb）

## 40.1 【Linux社区】图形公司特殊论之争（6 例）

**要点（判定表逐字）**：Greg KH 反问图形公司何以特殊——网络驱动、CPU、IB 控制器厂商皆有同类问题；指 Rodrigo Vivi 本意是借 Plumbers 谈预发布硬件与上游协作，原提案表述不清致易被误读为自作自受；Daniel Vetter 答 Greg KH——图形之外不懂其他行业，但 Intel 各处硬件团队问题本质相同；最简解是直接放弃上游只跑 LTS，而 SoC／图形界多如此，除 AMD 与 Intel 外多数驱动靠逆向故免预发布硬件之苦；Leon Romanovsky 请 Daniel Vetter 或 Rodrigo Vivi 直陈痛点，若话题获接受愿参与分享上游优先方法论经验；Mark Brown 答 Daniel Vetter——绝非 Intel 独有，其在芯片厂商时及 Linaro 成员皆有各自上游优先困局；只要还在卖实体芯片便不能要求立即全量上游而不顾营销与 lead customer 关系；Sean Paul 答 Dan Carpenter——android 代码长期处于将毕业态；drm 亦有重构漏更 staging 驱动、跨 drm／staging 树协调难，故已劝止 staging 用于 drm；vboxvideo 因非 atomic 驱动卡 staging；Sean Paul 答 Greg KH——vboxvideo 实验证 staging 不适合 drm，对低变动子系统则问题小，若无人愿做 atomic 转换则倾向丢弃

**史料**：`348856`、`348860`、`348863`、`348870`、`348892`、`348898`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348856 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348860 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348863 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348870 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348892 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348898 -->` 

**史观**：本体论上各方平等（总纲第 8 条——本体论上各方平等：Greg KH 的“网络驱动、CPU、IB 控制器厂商皆有同类问题”与 Daniel Vetter 的“图形之外不懂其他行业，但 Intel 各处硬件团队问题本质相同”并置，未替任一方定论）；分离聚合是永恒规律（总纲第 4 条——分离聚合是永恒规律：drm 与 staging 两树协调之难、vboxvideo 因非 atomic 驱动卡 staging，正是子系统与暂存树之间的分合相位）
**辨析**：Mark Brown 的“只要还在卖实体芯片便不能要求立即全量上游而不顾营销与 lead customer 关系”为产业约束之陈；Sean Paul 的“android 代码长期处于将毕业态”“已劝止 staging 用于 drm”为当事人自述，其“若无人愿做 atomic 转换则倾向丢弃”为处置主张；Leon Romanovsky 的“请直陈痛点，若话题获接受愿参与分享上游优先方法论经验”为响应姿态。本页未见决议。
**文献**：DSLXC-5631、DSLXC-5635、DSLXC-5638、DSLXC-5645、DSLXC-5667、DSLXC-5673（`ksummit-discuss.messages.348856`、`ksummit-discuss.messages.348860`、`ksummit-discuss.messages.348863`、`ksummit-discuss.messages.348870`、`ksummit-discuss.messages.348892`、`ksummit-discuss.messages.348898`，2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05），全文见 `raw_source.raw_json`

## 40.2 【Linux社区】稳定树膨胀成因与回移植风险（11 例）

**要点（判定表逐字）**：Jiri Kosina 指稳定队列心理层面不可忽视——维护者与作者被稳定队列持续淹没便永难回头审阅，固定节奏（如周五两小时）更易嵌入工作流，但根本仍是稳定树体量本身；Greg KH 列举稳定树变大的成因——开发更快（每小时九补丁）、维护者开始正确打 stable 标、Fixes 标签助力、Sasha 自动拣选、模糊测试 syzbot 等；称稳定仅占 Linus 树每日 216 补丁中的 12，体量增大是好事因抓到更多问题；James Bottomley 论稳定树回移植是权宜而非完美流程，列出三类风险（上游坏补丁、缺前驱、手合引入 bug），主张把上游审查当作实际审查过程并接受；Mark Brown 答 Greg KH——部分子系统已稳定打标五年以上；Sasha 拣出的与少量自漏标补丁是他唯一可靠复审者，自动化处手动核查仍有价值故复审负担相对轻；James Bottomley 提新主题“发行版内核 bugzilla 有害”——社区发行版无力 triage 云上 bug，需开发辅助工具让客户自助 bisect 定位修复并自请回移植稳定；bugzilla 作一线支持隐含企业级服务预期却无法满足；Mark Brown 答 Bottomley——缺前驱问题在自动拣选中最堪忧（无上下文），且对小问题（尤性能相关）须权衡风险收益，每次回移植出事都削弱他人采用稳定更新的意愿；Mark Brown 答 Bottomley——提升 bisectability 亦助其他测试，举 Guillaume Tucker 在 KernelCI 实现自动 bisect 支持（构建可则多顺、加 boot 问题则乱）；James Bottomley（发自安卓设备）认同前述权宜权衡论，总结规则：不修用户可见 bug 就不进稳定；Jiri Kosina 查 4.18.5 含 22 补丁，指其中 parisc 两处内存序改动（7797167、3b885ac）修无任何功能问题、上游仅存一 rc 故曝光最小，约一成补丁企业发行版不敢无充分论证即纳；Mark Brown 答 Bottomley——如今不止维护者，Sasha 的 neural net 拣选比其更 trigger happy，人虽有复查机会但性质不同于维护者自选；Greg KH 答 Daniel Vetter——说明其审计路径：stable 标则加 s-o-b、人工请求则加 cc requestor、Sasha 树带其 s-o-b、David Miller patchset 带其 s-o-b，皆可 cc s-o-b 区追溯

**史料**：`348858`、`348859`、`348864`、`348865`、`348866`、`348869`、`348873`、`348874`、`348875`、`348880`、`348889`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348858 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348859 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348864 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348865 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348866 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348869 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348873 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348874 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348875 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348880 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348889 -->` 

**史观**：本体论上各方平等（总纲第 8 条——本体论上各方平等：Greg KH 的“稳定仅占 Linus 树每日 216 补丁中的 12，体量增大是好事因抓到更多问题”与 Jiri Kosina、Mark Brown 的质疑并置，未替任一方定论）；经验优先（总纲第 9 条——经验优先：以 Greg KH 自陈“每小时九补丁”的开发速率、Jiri Kosina 查 4.18.5 含 22 补丁中 parisc 两处内存序改动为判据）
**辨析**：James Bottomley 的“稳定树回移植是权宜而非完美流程”与其三类风险清单（上游坏补丁、缺前驱、手合引入 bug）为当事人自陈；Mark Brown 的“缺前驱问题在自动拣选中最堪忧”“每次回移植出事都削弱他人采用稳定更新的意愿”为后果归因；Jiri Kosina 的“约一成补丁企业发行版不敢无充分论证即纳”为其经验估计。Greg KH 的审计路径自述（stable 标加 s-o-b、人工请求加 cc requestor、Sasha 树与 David Miller patchset 带其 s-o-b）为顶层流程说明。
**文献**：DSLXC-5633、DSLXC-5634、DSLXC-5639、DSLXC-5640、DSLXC-5641、DSLXC-5644、DSLXC-5648、DSLXC-5649、DSLXC-5650、DSLXC-5655、DSLXC-5664（`ksummit-discuss.messages.348858`、`ksummit-discuss.messages.348859`、`ksummit-discuss.messages.348864`、`ksummit-discuss.messages.348865`、`ksummit-discuss.messages.348866`、`ksummit-discuss.messages.348869`、`ksummit-discuss.messages.348873`、`ksummit-discuss.messages.348874`、`ksummit-discuss.messages.348875`、`ksummit-discuss.messages.348880`、`ksummit-discuss.messages.348889`，2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05），全文见 `raw_source.raw_json`

## 40.3 【Linux社区】死内核、LTS 与固定排期之辩（8 例）

**要点（判定表逐字）**：Geert Uytterhoeven 戏言我们正缓慢演进到发行版直接跟随 Linus 树、稳定树仅留最后发布点（无人愿跑裸 rc1／rc2）的地步；Greg KH 回 Geert——我巴不得这事发生，请让我失业；Thomas Gleixner 长文主张固定排期无济于事，直言不视死内核（4.4／3.16）一眼，meltdown／spectre／L1TF 显复杂回移植彻底失败；倡严格滚动模型、LTS 限两年，斥不能改版本号 QA 论为谬，称支持二十年的内核恋尸癖当止；Jiri Kosina 答 tglx——并无企业发行版要求为极古内核做稳定 LTS（RHEL 为 2.6.32／3.10，SLE 为 3.0／4.4／4.12，交集仅 4.4）；支持古内核是厂商商业决定，SUSE 正更主动跨服务包升内核版本以趋滚动；Mark Brown 谈其用 LTS 回移植作内部测试集成点、同时以 -next 为主开发平台、可上游者即上游，营销动作时再把压制补丁一推而出，称此法颇顺；Greg KH 答 Jiri Kosina——否认曾说稳定树不为发行版（Arch／Fedora／openSUSE／Gentoo／CoreOS／Debian／Android 皆依赖），或曾言不为企业发行版；认真看待发行版不好用投诉，SUSE 目前多止于你揽太多补丁；Thomas Gleixner 答 Kosina——斥上游可 happily 忽略死内核为谬：回移植耗顶尖开发者稀缺脑力、伤众人；须反复告诫发行版其造成巨大损害；Greg KH 答 Justin Forbes／Laura Abbott——今年因安全乱局（spectre／meltdown 等）稳定发布频且量大，可改每周一版但每版补丁数不降反大；称不固定反好因无带外信息泄漏，戏问是否学雷德蒙 Patch Tuesday

**史料**：`348861`、`348862`、`348867`、`348871`、`348872`、`348900`、`348903`、`348905`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348861 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348862 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348867 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348871 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348872 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348900 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348903 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348905 -->` 

**史观**：不存在进步，只有权力再分配（总纲第 3 条——不存在进步，只有权力再分配：Thomas Gleixner 的“倡严格滚动模型、LTS 限两年、斥支持二十年的内核恋尸癖当止”与 Jiri Kosina 的“支持古内核是厂商商业决定”对撞，实为支持年限决定权的再分配）；本体论上各方平等（总纲第 8 条——本体论上各方平等：Gleixner 的“斥上游可 happily 忽略死内核为谬”与 Kosina 的“并无企业发行版要求为极古内核做稳定 LTS（RHEL 为 2.6.32／3.10，SLE 为 3.0／4.4／4.12，交集仅 4.4）”并置）
**辨析**：Gleixner 的“meltdown／spectre／L1TF 显复杂回移植彻底失败”“回移植耗顶尖开发者稀缺脑力、伤众人”为其顶层判词；Greg KH 的“否认曾说稳定树不为发行版（Arch／Fedora／openSUSE／Gentoo／CoreOS／Debian／Android 皆依赖）”为当事人自我澄清，其“可改每周一版但每版补丁数不降反大”“不固定反好因无带外信息泄漏”为流程态度；Mark Brown 的“以 LTS 回移植作内部测试集成点、同时以 -next 为主开发平台”为其实践自述，未上升为通则。
**文献**：DSLXC-5636、DSLXC-5637、DSLXC-5642、DSLXC-5646、DSLXC-5647、DSLXC-5675、DSLXC-5678、DSLXC-5680（`ksummit-discuss.messages.348861`、`ksummit-discuss.messages.348862`、`ksummit-discuss.messages.348867`、`ksummit-discuss.messages.348871`、`ksummit-discuss.messages.348872`、`ksummit-discuss.messages.348900`、`ksummit-discuss.messages.348903`、`ksummit-discuss.messages.348905`，2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05），全文见 `raw_source.raw_json`

## 40.4 【Linux社区】AUTOSEL 灰色地带与 opt-in 之议（9 例）

**要点（判定表逐字）**：Takashi Iwai 答 Bottomley——AUTOSEL 与未标稳定者落入灰色地带，提议依树 opt-in／opt-out：其树多为有意不标者宜 opt-in 手动批准，无维护树则 opt-out 留至有人拒；Greg KH 答 Kosina——特定补丁信子系统维护者打 stable 标的判断；有脚本可按配置显示合并稳定发行版时实际影响自己的文件与提交，安卓用之对大体量补丁更安心；Jiri Kosina 追问 Greg KH 这些补丁本应否打 stable 标，指稳定另需信任其对稳定相关性已审慎评估，尤自动拣选时你究竟信任谁；Greg KH 答 Kosina——这些过其嗅觉测试（似简单性能胜），其会推回不显然者并常年求人复审；信任 Sasha 首轮扫描、己再全审、维护者说 NO 亦发生，三层实体足矣；Sasha Levin 答 Kosina——若不能信维护者对其子系统的判断则无计可施，此情景 Greg 权重低于维护者；自陈过每引擎拣出之上游补丁并应 Greg 批评；Sasha Levin 答 Takashi——现已可 opt-out 其树、愿逐补丁 ack 后再入；举随机拣出补丁（lore patchwork 909923）问是否不宜入稳定，称 Takashi 树状态佳故少投；Sasha Levin 答 Mark Brown——问如何改善流程，曾试更长复审期、合并即发邮件、主动追维护者显式 Ack，均未使人更满意；Takashi Iwai 答 Sasha——愿 opt-in 并可 defer 合并；以 lore patchwork 909923 为例（显为 fix 但非回归修复、无测试覆盖）愿多测后再纳，风险略高于显见 fix；Sasha Levin 答 Takashi——可在复审邮件上点明以 defer；问若限拣选上游满一月以上补丁能否缓其忧

**史料**：`348876`、`348877`、`348878`、`348887`、`348891`、`348894`、`348897`、`348899`、`348904`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348876 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348877 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348878 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348887 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348891 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348894 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348897 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348899 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348904 -->` 

**史观**：不存在进步，只有权力再分配（总纲第 3 条——不存在进步，只有权力再分配：Takashi Iwai 的“依树 opt-in／opt-out”与 Sasha Levin 的“若不能信维护者对其子系统的判断则无计可施，此情景 Greg 权重低于维护者”之争，实为自动拣选权与子系统判断权的再分配）；本体论上各方平等（总纲第 8 条——本体论上各方平等：Greg KH 的“三层实体足矣（Sasha 首轮扫描、己再全审、维护者说 NO 亦发生）”与 Jiri Kosina 的“尤自动拣选时你究竟信任谁”并置）
**辨析**：Sasha Levin 的自陈（“曾逐引擎拣出之上游补丁并应 Greg 批评”“曾试更长复审期、合并即发邮件、主动追维护者显式 Ack，均未使人更满意”）为当事人留痕；Takashi Iwai 以 lore patchwork 909923 为例的“显为 fix 但非回归修复、无测试覆盖，愿多测后再纳，风险略高于显见 fix”为具体个案判断，与 Levin 的“现已可 opt-out 其树、愿逐补丁 ack 后再入”往复；Greg KH 的“有脚本可按配置显示合并稳定发行版时实际影响自己的文件与提交”为工具层说明。本页未见定论。
**文献**：DSLXC-5651、DSLXC-5652、DSLXC-5653、DSLXC-5662、DSLXC-5666、DSLXC-5669、DSLXC-5672、DSLXC-5674、DSLXC-5679（`ksummit-discuss.messages.348876`、`ksummit-discuss.messages.348877`、`ksummit-discuss.messages.348878`、`ksummit-discuss.messages.348887`、`ksummit-discuss.messages.348891`、`ksummit-discuss.messages.348894`、`ksummit-discuss.messages.348897`、`ksummit-discuss.messages.348899`、`ksummit-discuss.messages.348904`，2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05），全文见 `raw_source.raw_json`

## 40.5 【Linux社区】staging 驱动治理（10 例）

**要点（判定表逐字）**：Takashi Iwai 答 Bottomley——梦寐多年的事；构建力仍是一小时余（依架构）故需半自动减配置（localmodconfig）方可用 bisect，SUSE 通常先请测近 vanilla 再 toss 上游；Jiri Kosina 答 Takashi——忆早年有人起网页 bisect 工具未竟，用户点 Good／Bad 即得 RPM 测，若以 GSoC 拾起当大助；Daniel Vetter 答 Takashi——+1 AUTOSEL opt-in，其回移植清理补丁（看似隐秘安全修复）常弄崩他人机器；倡稳定树清晰审计路径，每补丁记引入因（Cc stable／Link／AUTOSEL 邮件）以便事后追溯；Takashi Iwai 提新主题“如何更好对待 staging 驱动”——常久留 staging 不毕业、改动多停留 checkpatch 风格清理、与对应子系统沟通少、lustre 长留后被退回；求改善 staging 与子系统／核心开发者沟通；Konstantin Ryabitsev 答 Takashi——憧憬 bisect@home（类 seti@home／folding@home），中央队列开发者投提交与测试用例、志愿机群 grab 并 bisect 构建定位引入 bug 者，称愿全力托管；Dan Carpenter 答 Takashi——staging 久留者仅 comedi 浮现（众人无异议其迁出）；无线驱动因转 mac80211 复杂故多停留，愿把 staging 驱动交现有子系统但常不明确了接收者；Takashi Iwai 答 Dan Carpenter——承认久留或属错觉；问哪些驱动是良性毕业范例可学；指问题核心是 subsystem 无恰当接收者；Greg KH 答 Takashi——其每几版即清理 staging（speakup、comedi 待迁出），子系统常自迁真核；问 sound staging 除 most 与 bcm2835 外尚有谁，否认无恰当接收者之说；Greg KH 答 Sean Paul——vboxvideo 入 staging 前确得 DRM 维护者 OK；若永不合并不如丢弃；Takashi Iwai 答 Greg KH——承认久留或错觉；staging 驱动结构大手术与正确 API 用法最需子系统协助，协调越早越易，憾存在前未被告知

**史料**：`348881`、`348882`、`348883`、`348884`、`348885`、`348886`、`348888`、`348895`、`348896`、`348902`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348881 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348882 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348883 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348884 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348885 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348886 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348888 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348895 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348896 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348902 -->` 

**史观**：动手者创造历史（总纲第 10 条——动手者创造历史：以 Konstantin Ryabitsev 的 bisect@home 设想、Daniel Vetter 的“每补丁记引入因（Cc stable／Link／AUTOSEL 邮件）以便事后追溯”为分析单位）；分离聚合是永恒规律（总纲第 4 条——分离聚合是永恒规律：staging 驱动的久留与毕业、lustre 长留后被退回、无线驱动因转 mac80211 复杂故多停留，正是暂存与子系统之间的分合相位）
**辨析**：Takashi Iwai 两度“承认久留或属错觉”为当事人自我修正；Dan Carpenter 的“staging 久留者仅 comedi 浮现”“愿把 staging 驱动交现有子系统但常不明确了接收者”与 Takashi 的“问题核心是 subsystem 无恰当接收者”相对；Greg KH 的“其每几版即清理 staging（speakup、comedi 待迁出），子系统常自迁真核，否认无恰当接收者之说”为顶层反驳。两说并置，未决。
**文献**：DSLXC-5656、DSLXC-5657、DSLXC-5658、DSLXC-5659、DSLXC-5660、DSLXC-5661、DSLXC-5663、DSLXC-5670、DSLXC-5671、DSLXC-5677（`ksummit-discuss.messages.348881`、`ksummit-discuss.messages.348882`、`ksummit-discuss.messages.348883`、`ksummit-discuss.messages.348884`、`ksummit-discuss.messages.348885`、`ksummit-discuss.messages.348886`、`ksummit-discuss.messages.348888`、`ksummit-discuss.messages.348895`、`ksummit-discuss.messages.348896`、`ksummit-discuss.messages.348902`，2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05、2018-09-05），全文见 `raw_source.raw_json`

## 40.6 【Linux社区】2014 档案五封与 bug-introducing 议题认同（6 例）

**要点（判定表逐字）**：Rafael Wysocki 在 2014 能源偏置接口线程中追问 Sundar Iyer 究竟需要何种节能偏置接口，指前述平台相关权衡（宽与本地调度、突发与低速、资源共享范围等）皆值得考虑却未给出接口建议；Rafael Wysocki 赞同 Morten Rasmussen 把节能目标（powersave／auto／balanced）视为平台无关、由内核据目标施加技术，并补充调度器非唯一非开即关的子系统，图形适配器亦有能效与性能取舍；NeilBrown 在 2014 git 提交元数据附言线程中主张若 fixup 补丁始终强绑定其所修复的提交，bisect 时便不必反复手补，一人以正确方式提交众人受益；Julia Lawall 在 2014 内核精简（tinification）线程中问 Coccinelle 能否以可识别模式将设备树查找调用静态化为常量，借编译器常量传播与死代码消除来瘦身；Steven Rostedt 答 Daniel Vetter——认同其求 bug-introducing patches 长线程的各方观点摘要，免重演同一讨论；Josh Boyer 在 2014 QR oops 线程中认同应更广讨论如何获取有用错误报告，指发行版用户多在 N 版踩坑而上游已开发 N+2，等待模式浮现反而抬高回溯成本，开发速率正超过送达用户与收集报告的能力

**史料**：`348857`、`348868`、`348879`、`348890`、`348893`、`348901`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.348857 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348868 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348879 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348890 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348893 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348901 -->` 

**史观**：一切真历史都是古代史（总纲第 1 条——一切真历史都是古代史：2014 年的能源偏置接口、git 提交元数据附言、内核精简（tinification）、QR oops 四线程被 2018 年讨论重提，正见旧议题的当代性）；经验优先（总纲第 9 条——经验优先：以 Josh Boyer 的“发行版用户多在 N 版踩坑而上游已开发 N+2，等待模式浮现反而抬高回溯成本，开发速率正超过送达用户与收集报告的能力”为判据）
**辨析**：本块五封皆 2014 年档案，与 2018 年主线不同期，属跨期并置；Rafael Wysocki 的“前述平台相关权衡皆值得考虑却未给出接口建议”为对 Sundar Iyer 的追问，本页未见答复；NeilBrown 的“fixup 补丁强绑定其所修复提交则 bisect 时不必反复手补”、Julia Lawall 的 Coccinelle 静态化设想均为个人提案，未记采纳与否；Steven Rostedt 的“认同求 bug-introducing patches 长线程摘要，免重演同一讨论”为对 Daniel Vetter 提议的附议。
**文献**：DSLXC-5632、DSLXC-5643、DSLXC-5654、DSLXC-5665、DSLXC-5668、DSLXC-5676（`ksummit-discuss.messages.348857`、`ksummit-discuss.messages.348868`、`ksummit-discuss.messages.348879`、`ksummit-discuss.messages.348890`、`ksummit-discuss.messages.348893`、`ksummit-discuss.messages.348901`，2014-05-13、2014-05-13、2014-05-13、2014-05-14、2018-09-05、2014-05-14），全文见 `raw_source.raw_json`

---
注：本文件由判定表程序化生成（6 块，覆盖 50/50 CAND，两遍计数核对通过）；要点逐字取自判定表“要点”列（主代理全读审读实录），史料锚与 CAND 一一对应，全文以 raw_source.raw_json 为准。
