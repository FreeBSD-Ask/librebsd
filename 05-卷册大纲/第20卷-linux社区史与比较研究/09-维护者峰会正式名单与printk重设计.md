# 09 【Linux社区】维护者峰会正式名单与printk重设计

> 对应页面：ksummit-discuss p74（pk 347906-347955，2017-04-26 至 2017-06-20 线程收束）
> 判定：50 CAND / 0 NV
> 编号：DSLXC-4128..4177 | claim 已入库（50/50，dslinux_claims.duckdb）

## 9.1 【Linux社区】峰会重启：名单、流程与议程机制

**要点**：Linus 重启线程（静默一月无变化；James 请他再发，Thorsten Leemhuis 今天来信提回归追踪）——cc 只剩 Miller（还想要 networking 替代人选，除非他 10 月来布拉格）；核心名单：Miller/Greg KH(稳定+杂项)/Vetter(drm，Airlie 建议)/Ingo(x86+核心)/Mauro(media)/Arnd(arm+杂架构)/Andrew Morton/Paul(？Ellerman powerpc)/Takashi Iwai(sound+SuSE)/Doug Ledford(rdma)，除 Greg 外都可自荐替代；加自己/Ben Hutchings(stable，Greg 建议)/Stephen Rothwell(linux-next)；次级建议：TAB 与 KS 组织者（找重叠人群）；基建（Konstantin Ryabitsev k.org、Wu Fengguang kernel test robot、Rostedt ktest、Shuah testing、Thorsten regression、Corbet docs、syzkaller/KASAN 人）；安全（Andy Lutomirski、Kees Cook、James Morris）；发行（Laura Abbott Fedora、Jiri Kosthan、MM?/SuSE 或 Fedora？、Rom/Android）；文件系统（Al Viro vfs、Darrick Wong xfs、Ted Ts'o ext4）；块（Christoph Hellwig 兼 rdma 与 taste、Bottomley、Jens Axo）——厂商/赞助商带真维护问题也欢迎（好技术 talk 我喜欢，marketing 是灾难）；Randy：补漏——Greg 还 usb/staging；Andrew 还 MM（“need more MM?”）；Hellwig“and taste”—补个 PM 代表就大致齐（otherwise looks about right）；Thomas：自荐——RT（且上游）维护者，长期做大规模 overhaul/重构，多为过程问题；Bottom：愿组织“高技术含量厂商 talk”——峰会计划半天；vendor talks 排另半天，没兴趣者可去布拉格；Linus：自荐有哪但要有“择人流程”——KS 组织者合收建议+来源（blurb）；带议程条目和(部分)解；不要只抱怨；建议以邮件+可搜 subject 提；Miller：仍研究 10 月布拉格；netconf/netdev 11 月初首尔挤；无法认真推网络代表——上次把树托人达十多年（那人 focus 已变）；Linus（公车）：会不会网络人都这样？用 git rev-list 拆你 merges（多自 Jef Kirsher/Johannes 张/Pablo 庄）但粗略可能不精确；shortlog net/ 显示你近乎直接吃 patch——那“如果 Dave 被车撞”要不要谈？；Ted Ts'o 发布正式方案（与 Linus 商议）：维护者峰会邀请名单（14 人，全部来自 Linus 核心名单）：David Miller、Greg KH、Daniel Vetter、Ingo Molnar、Arnd Bergmann、Andrew Morton、Michael Ellerman、Takashi Iwai、Linus Torvalds、Ben Hutchings、Stephen Rothwell、Ted Ts'o、Shuah Kahn、James Bottomley；由 mini-Program Committee（James、Shuah、Greg、Ted）按 Linus 准则补齐至 30 人；Linus 二线名单作为候选种子；[MAINTAINERS SUMMIT] 前缀议题聚焦流程（半日）；技术主题“Kernel Summit”与 OSS Europe 并行运行、对注册者开放；[TECH TOPIC] 前缀独立成贴；约一半 slot 当日现场安排；7/8 前被收稿者免 OSS Europe 注册费、之后需付费；未订阅者可 mailman 重订

**史料**：`347931`、`347932`、`347933`、`347934`、`347936`、`347937`、`347938`、`347941`

**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347931 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347932 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347933 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347934 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347936 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347937 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347938 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347941 -->`
**史观**：多方平等（总纲 8：Linus 的核心名单、Miller 的自述、Thomas 与 Bottomley 的自荐、Ted Ts'o 的正式方案并置）；动手者叙事（总纲 10：名单与议程机制由 Linus、Ted、Shuah 等当事人自陈）；偶然性优先（总纲 5：峰会重启由 Thorsten Leemhuis 当日来信这一具体触发引出）
**辨析**：Ted Ts'o 的 14 人邀请名单全部出自 Linus 核心名单，由 mini-Program Committee（James、Shuah、Greg、Ted）补齐至 30 人属后续安排；Linus“如果 Dave 被车撞”之问是对网络子系统接班问题的直白表述，非结论。
**文献**：DSLXC-4153/4154/4155/4156/4158/4159/4160/4163（`ksummit-discuss.messages.347931`、`.347932`、`.347933`、`.347934`、`.347936`、`.347937`、`.347938`、`.347941`，2017-04-26 至 2017-06-20），全文见 `raw_source.raw_json`

## 9.2 【Linux社区】评审机制、信任因子与贡献者训练

**要点**：Brown：接 Miller“人不愿放手”——确有其事且常与缺评审互为因果（有人接手才好放手，子系统运转不良更劝退潜在新评审）；Bottomley 澄清 Dan 所指：Andrew 曾有 override 角色——拿 patch 发常规邮件强推 NAK/逼 maintainer 至少回应；只需机械 review，因为是在挑战维护者表态；Brown 续：换个说法——某区域没人干活时，谁在做就成了我们最好的专家（对 override 机制的辩护）；Petersen：netdev 的 NACK+拆小批教学不是没试——常见回复是“内部流程/版本号/qual周期/发布表比上游合入更重要”；企业存储厂商惯性使然，SCSI 比别家更严重；Miller：对 MAINTAINERS B: 条目此前一无所知，得知后立即为 networking 补上（Belloni 痛点的实证）；Miller：常有不愿放手之人——放弃守候多年之物的“控制权”很难；我们多犯此病；Jani：Bottomley“重做 review 揪漏并叫其别再来”太严格——只有 review 才能变好；我对 review 的信任靠正文实质（评论数量）而非末尾的 Reviewed-by；维护者应把 review 功绩记入 commit——review 常比写 patch 更费力，LWN v4.11 统计已开始追踪；Lee Jones：人人可评审，别设信任门槛——捞到 10% 的问题也行，维护者自己总能再补一轮；自己过载时让作者先清完所有 review 意见再终审；Hannes：最大问题是评审者短缺（应努力解决）——多数开发者自觉不够格不敢 review；“先评审后接受”只增加恐惧，吓跑新人；Bottom：立场澄清——“别人审过我就不用再审”；平时只在“本以为能依赖你的 review 却随机发现重大纰漏”时才重做；也不信“怕评审”——SCSI 人多忙于提交、没有额外带宽；Wolfram：认可 commit 记录评审/测试署名——hack git-request-pull 加“quality assurance from”清单；新 snippets repo（git.kernel.org/pub/scm/linux/kernel/git/wsa/snippets.git）——评审功劳可见化；Rafael：review 是决策进程中的建议——从常给好建议者听，但这次未必对、决定归你；不应轻易设“合入=必须有 review”的硬规则（除非确信绝不破例）；真激励=人们意识到评审让自己的 patch 更好进；“怕评审”未必成立——更多人只是没有额外时间（改动进树的感知价值被高估）

**史料**：`347906`、`347907`、`347908`、`347909`、`347910`、`347911`、`347913`、`347914`、`347915`、`347916`、`347917`、`347918`

**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347906 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347907 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347908 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347909 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347910 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347911 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347913 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347914 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347915 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347916 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347917 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347918 -->`
**史观**：多方平等（总纲 8：Brown、Bottomley、Petersen、Miller、Jani、Lee Jones、Hannes、Wolfram、Rafael 九方立场并置）；经验优先（总纲 9：以 netdev NACK+拆小批教学、LWN v4.11 review 统计、wsa/snippets.git 等实作为据）；自反性声明（总纲 7/23：本块为多立场实录，不取单一结论）
**辨析**：Jani 与 Bottomley 对“是否须先评审方可合入”分歧未收敛；Rafael 明言不应轻设“合入必须有 review”的硬规则，故本块不得读作评审准入制度成立的史料。
**文献**：DSLXC-4128/4129/4130/4131/4132/4133/4135/4136/4137/4138/4139/4140（`ksummit-discuss.messages.347906`、`.347907`、`.347908`、`.347909`、`.347910`、`.347911`、`.347913`、`.347914`、`.347915`、`.347916`、`.347917`、`.347918`，2017-04-26 至 2017-06-20），全文见 `raw_source.raw_json`

## 9.3 【Linux社区】跨树合入与不可变分支

**要点**：Vetter：对 Lee 规则（新跨子系统功能除非硬性 build 依赖否则单树原则）问“为什么”——看似用贡献者时间换维护者时间，应该训练更多维护者（drm 配别家不同）；Bottom：跨树 patch=潜在剧痛（conflict 直到 linux-next 才现、Stephen 设计 merge、merge window 推荐给 Linus）；非本子系统 patch 得不到好 Review（非专家在看）；规则=子系统 patch 走该子系统树，除非 patch 依赖我树里的东西；Brown：跨树维护者再强也有提交者代价（哪怕只是沟通延迟）——协调越少越顺；Olof：混容分支借别的树过河=赌别人不动近旁——最坏同时 refactor，次坏一边 refactor 一边加新；DRM 自己 refactor 多，ARM 内容走 DRM 树不放心；media/graphics 常两队分治，平台维护者可能有自己计划；overhead 多在 per-platform 层消化，只对新入职者/新平台多盯；Lee 直答 Vetter 时间数学——MFD/Backlight 近 10 版平均每 release 30 位提交者，若人人养出 30 分钟的习惯=维护者时间爆炸；不如贡献者自付 30 分钟（多数是本职内）而非维护者 30×30（多数本职外）；且是贡献者培训：patch 拆分/专家评审/冲突规避/bisect 保全

**史料**：`347919`、`347920`、`347921`、`347922`、`347925`

**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347919 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347920 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347921 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347922 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347925 -->`
**史观**：多方平等（总纲 8：Vetter 的“为什么”之问、Bottomley 与 Brown 的代价论、Olof 的分支风险、Lee 的时间数学并置）；经验优先（总纲 9：以 MFD/Backlight 近 10 版平均每 release 30 位提交者的实测数字为据）；拒绝进步叙事（总纲 1/3：不将单树原则写作协作机制“进步”）
**辨析**：Lee 以“30 位提交者 × 30 分钟”的时间数学回应 Vetter，属量级估算而非实测统计；Olof 所述混容分支“赌别人不动近旁”为概率性判断。
**文献**：DSLXC-4141/4142/4143/4144/4147（`ksummit-discuss.messages.347919`、`.347920`、`.347921`、`.347922`、`.347925`，2017-04-26 至 2017-06-20），全文见 `raw_source.raw_json`

## 9.4 【Linux社区】dt-include 跨树数值常量先行流程

**要点**：Olof 确认 Walleij 流程正是他们推的——仅一两个引用用数值、-rc1 后补符号化；简化合并、减 stable branch 依赖；量大才 pre-rc1（更别扭）；Vetter：认可——在对抗“topic/shared stable branch 增殖”上有真改进；Geert：新功能新平台 OK；但 platform→DT 迁移须三步（①新 DT 驱动 ②DTS 切换 ③优雅清理），且 ①②互相牵制可能要三个 release——已在规划 v4.15；问：②能否同 release -rc1 后做？这不只是数值改符号；Arnd：按 case——很老的 obsolete 平台可放宽“干净 bisect”直接并行合并（反正没人 run vanillia）；Olof：Renesas 案例我们特意请 ta 放慢——曾多个 dependent branch 与 respins churn（自伤 DoS）；1+2 正是鼓励的；争议核心在 dt-includes 大幅共享时——具体例欢迎；Geert：Renesas R-Car Gen2——在乎 DT 向后兼容（一段时间）与 bisect；“RST 00/23”共享 immutable 分支冲突多次；下个小了（CPG/MSSR 新驱动只 DT 依赖）；先做 platform→DT 清单；Arnd：有可工作驱动为何要快？——新平台直接上新的；老平台 OOB dts 需年限 grace；等一两个 release 不重；请先给清单

**史料**：`347926`、`347927`、`347928`、`347929`、`347930`、`347939`、`347940`

**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347926 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347927 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347928 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347929 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347930 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347939 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347940 -->`
**史观**：多方平等（总纲 8：Olof、Vetter、Geert、Arnd 四人对流程边界的分歧并置）；偶然性优先（总纲 5：流程争议由 Renesas R-Car Gen2 具体案例引出）；经验优先（总纲 9：以“RST 00/23”共享 immutable 分支反复冲突与 CPG/MSSR 新驱动为据）
**辨析**：Arnd 的“老平台给一两个 release 宽限”与 Geert 的“platform→DT 三步迁移须三个 release”并存，说明该流程并无统一定期；Olof“特意请 ta 放慢”系针对 Renesas 个案。
**文献**：DSLXC-4148/4149/4150/4151/4152/4161/4162（`ksummit-discuss.messages.347926`、`.347927`、`.347928`、`.347929`、`.347930`、`.347939`、`.347940`，2017-04-26 至 2017-06-20），全文见 `raw_source.raw_json`

## 9.5 【Linux社区】printk redesign 技术主题

**要点**：Sergey(含 Petr/Steven 提议)：printk 完整 redesign tech topic——单体量、需求互相矛盾；问：新 printk 应否单一，或拆（核心消息与 debug/info 缓冲分离）？需要需求清单；已在试 per-CPU（per-CPU buffer+flusher 线程）；直接 vs 间接输出（核心直打、慢的走 kthread、panic 例外）——求脑暴；Hannes：支持拆——log/debug（慢、大、非常规）与紧急（快、直发：oops/KERN_EMERG）；解耦消息生成（写日志）与输出（打屏）——串行设备才是拖累；Rostedt：先收集需求（互相矛盾）——1. 关键输出（warn/error/oops，需任意上下文含 NMI）；2. 活动信息（设备上下线、spurious 中断、CPU 上下线，需串行化）；3. 状态信息（pr_info，要 log 但不紧急）；4. 非关键信息（可延迟输出，不必互斥）；5. /dev/kmsg 用户数据（独立缓冲，最多时间戳交织进 dmesg）；Andrew：开发机与生产不同——开发要求严格顺序；若允许乱序则应加 sequence number 方便恢复，乱序足够可见。；Hannes：时间戳本来就有且必续——非紧急（不属于 1、2）消息绝不拆开、整条进缓冲；若如此、SCSI 自有日志基建全移除、直接用 printk 就很好；Andrew：时间戳粒度——每秒 2-3 条 print（_err/_dbg 交错）能否重建顺序？；Brown：PRINTK_TIME 只是配置项且非 100% 可靠——自己 syslog 里就有多条同时间戳的打印；Rost：也许内核命令级选项可强制（顺序）；Andrew Lunn：对——文件内 #define DEBUG（让 _dbg 非 NOP）可能就是“需要顺序”的信号；但 scope 是问题；Triplett：CONFIG_PRINTK 关闭时也别把整套 vsnprintf/%p 格式族编入——%p 修饰符多为人类/用户可读、而非机器消费；希望新需求考虑这点；Arnd：不现实——特殊格式太多（rtc_time 近例就是为外部 ABI 服务的）；Rostedt：有可能但属另一项目——CONFIG_VSPRINTF 独立；tracing 无 printk 也需要；printk 本身的乱局更大；Senozhatsky：同意——“这点现在还有点小”

**史料**：`347942`、`347943`、`347944`、`347945`、`347947`、`347948`、`347949`、`347950`、`347951`、`347952`、`347953`、`347954`、`347955`

**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347942 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347943 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347944 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347945 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347947 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347948 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347949 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347950 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347951 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347952 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347953 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347954 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347955 -->`
**史观**：多方平等（总纲 8：Sergey、Hannes、Rostedt、Andrew、Brown、Lunn、Triplett、Arnd、Senozhatsky 九方并置）；经验优先（总纲 9：以 per-CPU buffer+flusher 线程、PRINTK_TIME 实测、%p 格式族等实作为据）；拒绝进步叙事（总纲 1/3：不将 redesign 写作 printk 演进的“下一阶段”）
**辨析**：Rostedt 的需求五分层（关键输出/活动信息/状态信息/非关键信息//dev/kmsg 用户数据）为其个人归纳，非社区共识；Triplett 的“CONFIG_PRINTK 关闭时勿编入 vsnprintf/%p”被 Arnd 以 rtc_time 等外部 ABI 反例质疑，属未定论。
**文献**：DSLXC-4164/4165/4166/4167/4169/4170/4171/4172/4173/4174/4175/4176/4177（`ksummit-discuss.messages.347942`、`.347943`、`.347944`、`.347945`、`.347947`、`.347948`、`.347949`、`.347950`、`.347951`、`.347952`、`.347953`、`.347954`、`.347955`，2017-04-26 至 2017-06-20），全文见 `raw_source.raw_json`

## 9.6 【Linux社区】KS2014 档案混档

**要点**：Roedel（2014-05-12）：IOMMU 错误隔离边界——禁用 IOMMU 同时禁掉对子设备的保护、改变设备地址空间（disable IOTLB）可能令设备覆写随机内存；回应 Vetter“单子设备就全关 IOMMU”：IOMMU 侧能做的是禁 fault 和/或隔离设备使其无法再伤系统；Luck（2014-05-02）：若走向“系统调用子集化”——应用包应自带 syscall 依赖清单（装前预知跑不跑）；但 strace/kprobe/systemtap 扫描不够：bash 不用 pipe 直到用户敲“dmesg”〔存疑：原判定表该处语句残缺且残留转义反斜线，引号依上下文补全，原字待回源复核〕；Sharp（2014-05-12）：QR oops——“cut here”行本来就给 scripts/markup_oops.pl 切日志范围用的；现在更聪明了吗？；Pinchart（2014-05-12）：TECH TOPIC“PM dependencies”——现代系统很多 PM 依赖不循父-子设备模型（GPU 的 IOMMU 需通电才能 DMA）；ad-hoc 驱动专属 API（omap_iommu_*）阻碍自动化（IOMMU 该埋进 DMA map 对 master 透明）；相机接口/I2C sensor 次序挂起/恢复同型问题；目标先收集 use cases 论需要、再判能否通解；提名 Tomasz Figa；Băluță（2014-05-12）：QR oops URL+intents——已装 app 则本地解析，未装则 URL 显示文本；还能选发送到预定义服务器

**史料**：`347912`、`347923`、`347924`、`347935`、`347946`

**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347912 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347923 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347924 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347935 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347946 -->`
**史观**：自反性声明（总纲 7/23：明示本块为跨年混档，不与 2017 线程混叙）；偶然性优先（总纲 5：档案信因页面切片规则而混入本页）；拒绝进步叙事（总纲 1/3：不将 2014 议题写作其后讨论的“前身”）
**辨析**：5 封均系 2014-05-02/12 档案信（Luck、Roedel、Sharp、Pinchart、Băluță），与 p74 主体 2017 线程无回复关系；本块只作归卷登记。
**文献**：DSLXC-4134/4145/4146/4157/4168（`ksummit-discuss.messages.347912`、`.347923`、`.347924`、`.347935`、`.347946`，2014-05-02 至 2014-05-12），全文见 `raw_source.raw_json`

---
注：本文件由判定表程序化生成（9.1-9.6 共 6 块，覆盖 50/50 CAND）；要点逐字取自判定表“要点”列（审读实录），史料锚与 CAND 一一对应。
