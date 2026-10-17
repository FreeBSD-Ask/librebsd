# 45 【Linux社区】embargo与NDA框架之争

> 对应页面：ksummit-discuss p98（pk 349106-349155，2018 embargo/NDA 框架大辩论 + 2014 档案信）
> 判定：50 CAND / 0 NV
> 编号：DSLXC-5879..5928 | claim 已入库（50/50，dslinux_claims.duckdb）

## 45.1 【Linux社区】embargo 与 NDA 框架之争（上半）（10 例）

**要点（判定表逐字）**：Thomas Gleixner 复盘 embargo 协调：L1TF 因 Intel 较早通气、各方可互通而远胜 Meltdown/Spectre；强调需控制方及时交底且不加无理限制，并指 0-bot、kernel-ci 等机制须增 embargo 模式；Mauro 指 embargo 难点在厂商必求 NDA 且各人受不同法律约束，识别谁具覆盖全员之 NDA 耗时；主张由 LF 以单一 NDA 模型统筹，并可在法律 umbrellas 下开放厂商实验室真机测试；Greg KH 直拒 Mauro 的正式法律方案，称部分人依法不能签 NDA，保持法律于门外反而运作良好；Andy Lutomirski 称自己已签 NDA，渴望有清晰机制让厂商明确许可其与相关方沟通，不必繁复法律文书，书面对载即可；James Bottomley 辩 Greg 之 blanket 说法不实，称可为个人定制可签 NDA，并指糟糕措辞之 NDA 与开源披露本质冲突可化解；提议讨论 Meltdown/Spectre 能否在 NDA 框架内处理更好；Greg KH 认同 Andy 之需，称现况是各公司各异 NDA 拼凑；透露上周哈佛会议已启动考量，数月后或有具体方案，LF 或为出路；Greg KH 回 James：自承只说 部分人 不能签，非 blanket；并指 L1TF 正是 NDA 框架内运作且明显更好，Meltdown/Spectre 已以铁证促使改变；James Bottomley 再具体化：不存在无法定制可签 NDA 的开源领导角色，因领导职责本含保密义务，NDA 可据此拟定；Jiri Kosina 指 Meltdown/Spectre 实则亦在 NDA 框架内处理，问题在时机、信息共享与反馈渠道不顺；James Bottomley 忆早期各律师给 -ENONDA 把多数人剔除，发行版后签 NDA 才回圈；若早有懂开源者建 NDA 框架或可更早入局

**史料**：`349107`、`349111`、`349113`、`349117`、`349118`、`349120`、`349121`、`349122`、`349126`、`349127`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.349107 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349111 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349113 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349117 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349118 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349120 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349121 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349122 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349126 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349127 -->` 

**史观**：法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：Greg KH 的“部分人依法不能签 NDA，保持法律于门外反而运作良好”与 Mauro 的“主张由 LF 以单一 NDA 模型统筹”对撞，实为保密义务与披露自由的利益划分）；本体论上各方平等（总纲第 8 条——本体论上各方平等：Thomas Gleixner 的“L1TF 因 Intel 较早通气、各方可互通而远胜 Meltdown/Spectre”与 Jiri Kosina 的“Meltdown/Spectre 实则亦在 NDA 框架内处理，问题在时机、信息共享与反馈渠道不顺”并置，未替任一方定论）
**辨析**：Andy Lutomirski 的“称自己已签 NDA，渴望有清晰机制让厂商明确许可其与相关方沟通，不必繁复法律文书”为当事人自陈；James Bottomley 的“辩 Greg 之 blanket 说法不实，称可为个人定制可签 NDA”与 Greg KH 的“自承只说部分人不能签，非 blanket”为事实层往复，Greg 之更正属当事人自反留痕；James Bottomley 的“忆早期各律师给 -ENONDA 把多数人剔除，发行版后签 NDA 才回圈”为其亲历之陈。
**文献**：DSLXC-5880、DSLXC-5884、DSLXC-5886、DSLXC-5890、DSLXC-5891、DSLXC-5893、DSLXC-5894、DSLXC-5895、DSLXC-5899、DSLXC-5900（`ksummit-discuss.messages.349107`、`ksummit-discuss.messages.349111`、`ksummit-discuss.messages.349113`、`ksummit-discuss.messages.349117`、`ksummit-discuss.messages.349118`、`ksummit-discuss.messages.349120`、`ksummit-discuss.messages.349121`、`ksummit-discuss.messages.349122`、`ksummit-discuss.messages.349126`、`ksummit-discuss.messages.349127`，2018-09-08、2018-09-08、2018-09-08、2018-09-08、2018-09-08、2018-09-08、2018-09-08、2018-09-08、2018-09-08、2018-09-08），全文见 `raw_source.raw_json`

## 45.2 【Linux社区】embargo 与 NDA 框架之争（下半）（10 例）

**要点（判定表逐字）**：Linus Torvalds 斩钉截铁：我不签 NDA，源于早年竞品 Intel 的 f0 0f 死锁事件，改以绅士协议代之；称 Intel 知悉其不签状况并接受；James Bottomley 回 Linus：不签是 choice 非法律不能；若认签 NDA 终致厂商不改，应基于政策辩论而非假借法律障碍；Andy Lutomirski 称己 NDA 经公司，愿撤掉改由 LF 或类似实体接手，因公司不擅 Meltdown 类斡旋，专设机制更佳；Mauro 自陈合同 NDA 覆盖工作，遇 embargo 须耗时与法务解释开源需求，且有语言壁垒；主张预先备妥机制显著改善流程；Greg KH 回 James：可最终定制 NDA，但涉语言与公司等层层问题；若目标为 LF 提供三类 NDA 处理安全，可提 TAB 推动，且常规 security 邮件处理本就良好；Greg KH 答 Jiri：L1TF 未完整回退 4.4.y 作宿主机（回退太糟、主机商已迁 4.9+），arm32 的 spectre 修复未入 4.18 前稳定树；主张仅信最新 LTS；Linus Torvalds 称对硬件 bug 应叫厂商滚开，非我们背锅；若厂商要我为他们的失误签 NDA 就当面嘲笑并告诉媒体其阻碍修复；James Bottomley 归纳两选：一顺产业惯例引 NDA 框架、二逼产业采合开源之新规范；倾向二，并主张借 lwn.net 与维护者访谈出 critique 以推变革；Andy Lutomirski 提第三选项：定政策、律师同意、几不成 NDA 的中间地带；Ted Ts'o 指唯一中间地是绅士协议，难点在违约之齿；忆 TAB 为 UEFI 预标准化谈 NDA，LF 代签独立开发者不可行，专为其个人 NDA 耗时数月

**史料**：`349128`、`349129`、`349130`、`349132`、`349135`、`349136`、`349138`、`349140`、`349141`、`349142`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.349128 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349129 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349130 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349132 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349135 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349136 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349138 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349140 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349141 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349142 -->` 

**史观**：法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：Linus Torvalds 的“我不签 NDA，源于早年竞品 Intel 的 f0 0f 死锁事件，改以绅士协议代之”“对硬件 bug 应叫厂商滚开，非我们背锅”与 James Bottomley 的“不签是 choice 非法律不能，若认签 NDA 终致厂商不改，应基于政策辩论而非假借法律障碍”对撞，实为责任归属与保密义务的利益划分）；本体论上各方平等（总纲第 8 条——本体论上各方平等：Greg KH 的“可最终定制 NDA，但涉语言与公司等层层问题；若目标为 LF 提供三类 NDA 处理安全，可提 TAB 推动”与 Andy Lutomirski 的“第三选项：定政策、律师同意、几不成 NDA 的中间地带”、Ted Ts'o 的“唯一中间地是绅士协议，难点在违约之齿”并置，未替任一方定论）
**辨析**：Linus 的“称 Intel 知悉其不签状况并接受”为其转述他人立场，非其自定；Ted Ts'o 的“忆 TAB 为 UEFI 预标准化谈 NDA，LF 代签独立开发者不可行，专为其个人 NDA 耗时数月”为其亲历之陈；Greg KH 的“L1TF 未完整回退 4.4.y 作宿主机（回退太糟、主机商已迁 4.9+），arm32 的 spectre 修复未入 4.18 前稳定树”为可核之技术实况，其“主张仅信最新 LTS”为据此而生的政策倾向；James Bottomley 的“倾向二，并主张借 lwn.net 与维护者访谈出 critique 以推变革”为其路径主张。
**文献**：DSLXC-5901、DSLXC-5902、DSLXC-5903、DSLXC-5905、DSLXC-5908、DSLXC-5909、DSLXC-5911、DSLXC-5913、DSLXC-5914、DSLXC-5915（`ksummit-discuss.messages.349128`、`ksummit-discuss.messages.349129`、`ksummit-discuss.messages.349130`、`ksummit-discuss.messages.349132`、`ksummit-discuss.messages.349135`、`ksummit-discuss.messages.349136`、`ksummit-discuss.messages.349138`、`ksummit-discuss.messages.349140`、`ksummit-discuss.messages.349141`、`ksummit-discuss.messages.349142`，2018-09-08、2018-09-08、2018-09-08、2018-09-09、2018-09-09、2018-09-09、2018-09-09、2018-09-09、2018-09-09、2018-09-09），全文见 `raw_source.raw_json`

## 45.3 【Linux社区】中间地带与 MOU 之议（10 例）

**要点（判定表逐字）**：David Woodhouse 称真 NDA 与绅士协议差别不大，无人真会输房，违约至多下次不被邀；指 Spectre/Meltdown embargo 前已有泄漏仅遭 tutting；Andy Lutomirski 要 NDA 之反：绅士协议加明示相关人可互谈、embargo 有终点且可拒延；称商家深知最强 NDA 亦无用，Meltdown 若九月漏 Intel 更惨；Ted Ts'o 称 Andy 所想要约即无齿 Memo of Understanding，与 Linus 选项二无殊；若无后果则不必签，足以给律师留面即可；Andy Lutomirski 认同 MOU，但坚持须明定 Intel 违约后果：若其讼我 preexisting NDA 我可指此约反制；Jiri Kosina 赞同 Linus 叫停，但强调须向 stable 下游明示某些修复／回退不发生，否则下游或陷法律窘境（暗合 grsecurity 诉求之反）；Jiri Kosina 补注 SUSE 4.4 已完整回退 L1TF 可 cherry-pick；只要 stable 消费者清楚 Greg 所述不回退政策即无碍；Jiri Kosina 问 Ted 选项二如何落地，冀有不需整盘失败以 shock 之他法；James Bottomley 答 Jiri：除同行压力与开源基金会制度助力，唯余 PR 因子——出失败史与改进建议以启对话；Eduardo Valentin 小结：最新 LTS 近上游、余者 best effort 回退；并询 oldest 内核是否干脆不补；Eduardo Valentin 补例：meltdown 在 4.14 近主线，更旧者仅得 x86 entry 核心未含优化；问社区是否索性不补最旧内核以促升级

**史料**：`349143`、`349144`、`349147`、`349148`、`349149`、`349150`、`349152`、`349153`、`349154`、`349155`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.349143 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349144 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349147 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349148 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349149 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349150 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349152 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349153 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349154 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349155 -->` 

**史观**：法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：David Woodhouse 的“真 NDA 与绅士协议差别不大，无人真会输房，违约至多下次不被邀”与 Andy Lutomirski 的“认同 MOU，但坚持须明定 Intel 违约后果”之争，实为违约代价由谁承担的利益划分）；分离聚合是永恒规律（总纲第 4 条——分离聚合是永恒规律：Ted Ts'o 的“Andy 所想要约即无齿 Memo of Understanding，与 Linus 选项二无殊”与 Eduardo Valentin 的“最新 LTS 近上游、余者 best effort 回退”同向，正是责任在主线与 stable 之间的分合相位）
**辨析**：Jiri Kosina 的“赞同 Linus 叫停，但强调须向 stable 下游明示某些修复／回退不发生，否则下游或陷法律窘境（暗合 grsecurity 诉求之反）”“补注 SUSE 4.4 已完整回退 L1TF 可 cherry-pick”为其实务之陈；James Bottomley 的“除同行压力与开源基金会制度助力，唯余 PR 因子——出失败史与改进建议以启对话”为其方法论判词；Eduardo Valentin 的“问社区是否索性不补最旧内核以促升级”为待答之问，本页未见答复。
**文献**：DSLXC-5916、DSLXC-5917、DSLXC-5920、DSLXC-5921、DSLXC-5922、DSLXC-5923、DSLXC-5925、DSLXC-5926、DSLXC-5927、DSLXC-5928（`ksummit-discuss.messages.349143`、`ksummit-discuss.messages.349144`、`ksummit-discuss.messages.349147`、`ksummit-discuss.messages.349148`、`ksummit-discuss.messages.349149`、`ksummit-discuss.messages.349150`、`ksummit-discuss.messages.349152`、`ksummit-discuss.messages.349153`、`ksummit-discuss.messages.349154`、`ksummit-discuss.messages.349155`，2018-09-09、2018-09-09、2018-09-09、2018-09-09、2018-09-09、2018-09-09、2018-09-09、2018-09-09、2018-09-10、2018-09-10），全文见 `raw_source.raw_json`

## 45.4 【Linux社区】staging 毕业、DRM 合并模型与 succession 之谑（7 例）

**要点（判定表逐字）**：Jonathan Cameron 以 IIO 从 staging 毕业为例，主张把 staging 驱动交由对应子系统邮件列表统一管理，并借 staging 作新人导师训练场；亦呼应 Mauro 用 drivers/staging/media 配 MAINTAINERS 条目及 atomisp、lustre 之教训，提议以机器人监控长期滞留者；Mauro 就 succession planning 提反问，并以媒体子系统十年前 Mercurial 全员 commit 导致灾难为例，质疑 DRM 群组维护模式外推；倾向 x86/arm 式三人组加地理分散的层级模型；Thomas Gleixner 简短接话，戏称若按 Mauro 地理分散之说则要禁止维护者同处一地；Daniel Vetter 澄清并非主张顶层 committer 模型，而是 DRM 以文档化合并准则、强制评审、海量 CI 与 CoC 约束多 committer；指 kernel 外 commit right 已是成熟问题；Stephen Rothwell 自述 quiet time 在 rc1 至 rc3（其树已合入、各树未添新料），最忙在 rc6 至合并窗口中，因众人挤入 bits 制造冲突；Laurent Pinchart 反驳 Mauro 对 DRM 多 committer 的贬抑，称未建信任即排除是权力斗争迹象；指 DRM 非全员 commit、信任为先，revert 即可控灾，顶层 20+ committer 他存忧；Jiri Kosina 质疑 succession planning 初衷，指原系 James 玩笑，Linus 明言续任且无其他关键人 bus factor 计划，应先重述欲解何题

**史料**：`349106`、`349109`、`349110`、`349115`、`349133`、`349137`、`349151`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.349106 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349109 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349110 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349115 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349133 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349137 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349151 -->` 

**史观**：分离聚合是永恒规律（总纲第 4 条——分离聚合是永恒规律：Jonathan Cameron 的“把 staging 驱动交由对应子系统邮件列表统一管理、借 staging 作新人导师训练场”与 Mauro 的“用 drivers/staging/media 配 MAINTAINERS 条目及 atomisp、lustre 之教训”并置，正是暂存树与子系统之间的分合相位）；本体论上各方平等（总纲第 8 条——本体论上各方平等：Daniel Vetter 的“并非主张顶层 committer 模型，而是 DRM 以文档化合并准则、强制评审、海量 CI 与 CoC 约束多 committer”与 Laurent Pinchart 的“反驳 Mauro 对 DRM 多 committer 的贬抑，指 DRM 非全员 commit、信任为先，revert 即可控灾”并置，未替任一方定论）
**辨析**：Mauro 的“以媒体子系统十年前 Mercurial 全员 commit 导致灾难为例，质疑 DRM 群组维护模式外推”“倾向 x86/arm 式三人组加地理分散的层级模型”为其经验归因；Thomas Gleixner 的“戏称若按 Mauro 地理分散之说则要禁止维护者同处一地”为戏语，非史家判断；Laurent Pinchart 的“称未建信任即排除是权力斗争迹象”为其立场之陈；Jiri Kosina 的“质疑 succession planning 初衷，指原系 James 玩笑，Linus 明言续任且无其他关键人 bus factor 计划，应先重述欲解何题”为程序性质问，本页未见答复。
**文献**：DSLXC-5879、DSLXC-5882、DSLXC-5883、DSLXC-5888、DSLXC-5906、DSLXC-5910、DSLXC-5924（`ksummit-discuss.messages.349106`、`ksummit-discuss.messages.349109`、`ksummit-discuss.messages.349110`、`ksummit-discuss.messages.349115`、`ksummit-discuss.messages.349133`、`ksummit-discuss.messages.349137`、`ksummit-discuss.messages.349151`，2018-09-08、2018-09-08、2018-09-08、2018-09-08、2018-09-09、2018-09-09、2018-09-09），全文见 `raw_source.raw_json`

## 45.5 【Linux社区】硬件测试实操与 stable-next 落地（7 例）

**要点（判定表逐字）**：Laurent Pinchart 反驳 Mauro 称相机麦克风难测之说，主张可用已知场景与受控光照、隔音 enclosure 测试，关键在于预算而非不可行；Mauro 续论硬件测试：DRM 与电视卡可用 HDMI grabber 置于任意机房，而相机麦克风等需受控环境与主动巡检，普通数据中心难胜任；Dan Carpenter 指 cifs 提交 f46ecbd97f5 修复 send_set_info 的 slab-out-of-bounds 属未带上前置改动即回退之例（CoreOS bug 2480）；Greg KH 响应 Linus 与 Sasha 的 stable-next 构想，称本周搭自动分支送 0-day 做基本 smoke test；Guenter Roeck 赞 stable-next 助早抓构建错，但指其无助于已报回归；主张加网络与基础虚拟／网络文件系统测试更能抓近期回归；Sasha Levin 已推 4.14 自动生成分支 linux-4.14.y-next，邀 Greg 对比其实现；Laurent Pinchart 续论测试：相机等需造硬件 enclosure 未必大于 ARM 开发板；若视测试关键就须投资源，否则毋称重视

**史料**：`349108`、`349114`、`349116`、`349124`、`349125`、`349131`、`349139`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.349108 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349114 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349116 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349124 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349125 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349131 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349139 -->` 

**史观**：经验优先（总纲第 9 条——经验优先：以 Dan Carpenter 的“cifs 提交 f46ecbd97f5 修复 send_set_info 的 slab-out-of-bounds 属未带上前置改动即回退之例（CoreOS bug 2480）”、Guenter Roeck 的“stable-next 助早抓构建错，但指其无助于已报回归”为判据）；动手者创造历史（总纲第 10 条——动手者创造历史：以 Greg KH 的“本周搭自动分支送 0-day 做基本 smoke test”、Sasha Levin 的“已推 4.14 自动生成分支 linux-4.14.y-next，邀 Greg 对比其实现”为分析单位）
**辨析**：Laurent Pinchart 的“主张可用已知场景与受控光照、隔音 enclosure 测试，关键在于预算而非不可行”“若视测试关键就须投资源，否则毋称重视”与 Mauro 的“相机麦克风等需受控环境与主动巡检，普通数据中心难胜任”对撞，属资源约束之争，未作单方裁断；Guenter Roeck 的“主张加网络与基础虚拟／网络文件系统测试更能抓近期回归”为其优先级之陈。
**文献**：DSLXC-5881、DSLXC-5887、DSLXC-5889、DSLXC-5897、DSLXC-5898、DSLXC-5904、DSLXC-5912（`ksummit-discuss.messages.349108`、`ksummit-discuss.messages.349114`、`ksummit-discuss.messages.349116`、`ksummit-discuss.messages.349124`、`ksummit-discuss.messages.349125`、`ksummit-discuss.messages.349131`、`ksummit-discuss.messages.349139`，2018-09-08、2018-09-08、2018-09-08、2018-09-08、2018-09-08、2018-09-09、2018-09-09），全文见 `raw_source.raw_json`

## 45.6 【Linux社区】2014 档案五封与 API 废弃（6 例）

**要点（判定表逐字）**：Mark Brown 于 2014 PM dependencies 线程释疑：核心设备 probe 被推迟至依赖就绪，故沿设备列表后移、先被 suspend，从而也解系统挂起依赖（2014 档案）；Arnd Bergmann 于 2014 driver model/ACPI/DT 线程，主张以 dev_property_read_bool 等统一命名属性 API 服务简单驱动，复杂子节点仍须教驱动识双固件；并指正背离 IORESOURCE 趋势、转向描述符指针（2014 档案）；Rafael Wysocki 于 2014 线程认同 Arnd：简单驱动可用统一命名属性 API，复杂子节点恒需专用接口；并附和背离 IORESOURCE、转向 GPIO 描述符与 IRQ 描述符指针（2014 档案）；Guenter Roeck 于 2014 stable workflow 线程，以 Juniper 维护者身份赞成议题；指子系统维护者发 for-stable pull 请求增负担，Cc: stable 或请稳定邮件列表更简，未信服 pull 为解（2014 档案）；Rafael Wysocki 于 2014 PM dependencies 线程追问 Mark Brown：probe 延期解系统挂起依赖，但 async suspend 例外（2014 档案）；Ted Ts'o 于 API replacement/deprecation 线程，忘却 strncpy 会自动零填，主张 rename strncpy 以明示适用场景，并自嘲把 src、dest 抄反

**史料**：`349112`、`349123`、`349134`、`349145`、`349146`、`349119`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.349112 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349123 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349134 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349145 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349146 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349119 -->` 

**史观**：一切真历史都是古代史（总纲第 1 条——一切真历史都是古代史：2014 年的 PM dependencies、driver model/ACPI/DT、stable workflow 三线档案被 2018 年讨论重提，正见旧议题的当代性）；理论必须自反（总纲第 7 条——理论必须自反：Ted Ts'o 的“忘却 strncpy 会自动零填，主张 rename strncpy 以明示适用场景，并自嘲把 src、dest 抄反”正是当事人对自身判断的撤回与自反）
**辨析**：Mark Brown 的“核心设备 probe 被推迟至依赖就绪，故沿设备列表后移、先被 suspend，从而也解系统挂起依赖”与 Rafael Wysocki 的“追问 probe 延期解系统挂起依赖，但 async suspend 例外”构成往复，后者之疑未见答；Arnd Bergmann 的“主张以 dev_property_read_bool 等统一命名属性 API 服务简单驱动，复杂子节点仍须教驱动识双固件”与 Rafael Wysocki 的认同为同向之陈；Guenter Roeck 的“以 Juniper 维护者身份赞成议题”“未信服 pull 为解”为其立场自陈。本块前五封为 2014 年档案，与 2018 年主线不同期，属跨期并置。
**文献**：DSLXC-5885、DSLXC-5896、DSLXC-5907、DSLXC-5918、DSLXC-5919、DSLXC-5892（`ksummit-discuss.messages.349112`、`ksummit-discuss.messages.349123`、`ksummit-discuss.messages.349134`、`ksummit-discuss.messages.349145`、`ksummit-discuss.messages.349146`、`ksummit-discuss.messages.349119`，2014-05-14、2014-05-14、2014-05-14、2014-05-02、2014-05-14、2018-09-08），全文见 `raw_source.raw_json`

---
注：本文件由判定表程序化生成（6 块，覆盖 50/50 CAND，两遍计数核对通过）；要点逐字取自判定表“要点”列（主代理全读审读实录），史料锚与 CAND 一一对应，全文以 raw_source.raw_json 为准。
