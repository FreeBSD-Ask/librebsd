# 81 【Linux社区】l2md工具链与TAB章程COVID前瞻

> 来源：ksummit-discuss p133（50 封全读，2019-09/2020-03 l2md 与 kit 基座讨论+TAB 章程 absentee 投票之辩，夹杂 2014-05 档案信）
> 判定：49 CAND / 1 NV。主题分布：Corbet数据库论 1、Sphinx扩展提案 1、l2md与kit基座 1、传输层之问 1、m文件机制 1、LKML倾倒场论 1、Corbet否认 1、HTML限定问 1、--fixes补丁 1、Kees质询 1、KS2014档案-tipbot 1、Geert实测通过 1、Perches答疑 1、Kees认错 1、Perches举例 1、procmail建议 1、位置之问 1、process定位 1、procmail版落地 1、Konstantin认可 1、KS2014档案-沙箱 1、Corbet催迁 1、Williams同意迁 1、TAB章程修改 1、塞票担忧 1、威胁模型论 1、信任与成文 1、选民池史 1、COVID前瞻重磅 1、kernelorg质疑 1、woT辩护 1、KS2014档案-QR 1、限制论 1、婴儿步 1、阶梯提案 1、透明之责 1、扩池论 1、疫情暗讽 1、firststep辩 1、渐进论 1、参选资格问 1、历史观察 1、KS2014档案-沙箱分立 1、程序披露 1、文档请求 1、章程请求 1、章程史 1、历史例外 1、利益攸关论 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p133（实锚 pk 350856-350905）的逐封提取（49 CAND / 1 NV），全 49 块采用**单行摘要体例**（丙型）：每块由“## 81.x 【Linux社区】题名”与若干“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 81.1 【Linux社区】Corbet数据库论

- 【Linux社区】Corbet：“MAINTAINERS 是数据库、线性打印不是最好呈现；18K 行打印约 300 页——HTML 便宜、其他格式痛苦；需要想清楚” `<!-- ROW_MINE: ksummit-discuss.messages.350856 -->`

## 81.2 【Linux社区】Sphinx扩展提案

- 【Linux社区】Mauro：“既是数据库可生成其他输出——.. maintainers:: <subdir> 扩展调 get-maintainers 输出维护细节、可加进子系统 profile；仍要有全集输出——单独 PDF 降低误印 300 页风险” `<!-- ROW_MINE: ksummit-discuss.messages.350857 -->`

## 81.3 【Linux社区】l2md与kit基座

- 【Linux社区】Vyukov kit 提议（UI 解耦/贡献者-维护者-评审者三人群/kit init+kit mail/CL 优先）获 Borkmann +1；Borkmann 披露 l2md：定期 pull lore git 树→maildir（bpf 8k 邮件 0.58 秒）；提议 lore git 树为 kit 基座+sendmail 兼容推入接口（CI 直接 pull/git sha 回复）；已日用 `<!-- ROW_MINE: ksummit-discuss.messages.350858 -->`

## 81.4 【Linux社区】传输层之问

- 【Linux社区】Vyukov：“git 作传输层存结构化变更？MS 已提（LWN 799134）；Konstantin 提过可扩展性问题——git 不该存 journal 型信息；需实测评估；全员 push 单 git 的认证与单用户搞砸问题” `<!-- ROW_MINE: ksummit-discuss.messages.350859 -->`

## 81.5 【Linux社区】m文件机制

- 【Linux社区】Borkmann：“lore git 每仓库单文件 m 含列表最顶邮件+对前一封的 diff；l2md 接收侧已可用；push 侧需服务器逻辑（禁 force push、m 冲突自由置顶+vger 式过滤）”；netdev 全史 l2md 转换实测 498,001 封 41 秒 `<!-- ROW_MINE: ksummit-discuss.messages.350860 -->`

## 81.6 【Linux社区】LKML倾倒场论

- 【Linux社区】Doug：“LKML 只是倾倒场、无过滤器不是找补丁对话的地方；ksummit-discuss 这类高信噪比列表是好的前进方式”；求证 Corbet 支持全补丁 CC LKML `<!-- ROW_MINE: ksummit-discuss.messages.350861 -->`

## 81.7 【Linux社区】Corbet否认

- 【Linux社区】Corbet：“我不认为我说过——没有特别的理由主张；有人认为一切都该上 LKML、我无强烈意见” `<!-- ROW_MINE: ksummit-discuss.messages.350862 -->`

## 81.8 【Linux社区】HTML限定问

- 【Linux社区】Kees：“能从非 HTML 输出中特别排除吗？（或只在 HTML 输出包含）也许我的 RFC 只有 html 目标拿到真文件” `<!-- ROW_MINE: ksummit-discuss.messages.350863 -->`

## 81.9 【Linux社区】--fixes补丁

- 【Linux社区】Perches get_maintainer.pl --fixes 38 行补丁全文：Fixes: 行提交签名者自动加入 CC（vcs_add_commit_signers）、默认开启 `<!-- ROW_MINE: ksummit-discuss.messages.350864 -->`

## 81.10 【Linux社区】Kees质询

- 【Linux社区】Kees：“Oh yes please! 我一直手动做——nice bit of automation :)”；质询 6 位下限（12 才是惯例）并给 SHA 长度分布（31446×12/1866×13/735×16…）；“commit_authors 未使用？” `<!-- ROW_MINE: ksummit-discuss.messages.350865 -->`

## 81.11 【Linux社区】KS2014档案-tipbot

- 【Linux社区】hpa（2014-05-21）：“邮件生成器不必跑在主副本——tip-bot 只是 tip 树的 regular puller（公开 git 端口）；多项目已用变体；配置选项巨多=等价 shell 账号须沙箱” `<!-- ROW_MINE: ksummit-discuss.messages.350866 -->`

## 81.12 【Linux社区】Geert实测通过

- 【Linux社区】Geert：“从 ER 回来后第一个 fix 快速试了一下——做对了”（--fixes 补丁实测认可） `<!-- ROW_MINE: ksummit-discuss.messages.350867 -->`

## 81.13 【Linux社区】Perches答疑

- 【Linux社区】Perches：“6 位下限：你的 grep col2 不对——把 Fixes: commit <foo> 都算成 6；hex 长度无关紧要——必须是特定单一 SHA1 否则查找失败”；“所有 <foo>-by: 签名都加”；“authors 已须 sign-off 是重复” `<!-- ROW_MINE: ksummit-discuss.messages.350868 -->`

## 81.14 【Linux社区】Kees认错

- 【Linux社区】Kees：“已有 6 位 SHA1 碰撞所以用更长更好？无强意见”；发现 git-all-signature-types 默认 0 `<!-- ROW_MINE: ksummit-discuss.messages.350869 -->`

## 81.15 【Linux社区】Perches举例

- 【Linux社区】Perches：“commit 以 c 开头匹配 [a-f0-9]——试你原始 egrep；前几例=the commit referenced in Fixes: below…；用 awk if (length($2)==6)”；“通用函数” `<!-- ROW_MINE: ksummit-discuss.messages.350870 -->`

## 81.16 【Linux社区】procmail建议

- 【Linux社区】Konstantin：“我也做过类似工具没做完——用 procmail 管道写复杂规则；建议你的工具也提供可管道到 procmail 的 stdout” `<!-- ROW_MINE: ksummit-discuss.messages.350872 -->`

## 81.17 【Linux社区】位置之问

- 【Linux社区】Corbet：“我打算合入这些补丁；但 maintainer guide 讲如何当维护者、这文档讲如何与特定维护者打交道——Documentation/maintainer 可能是错误位置；要不要放 Documentation/process 或新建顶级 book？” `<!-- ROW_MINE: ksummit-discuss.messages.350873 -->`

## 81.18 【Linux社区】process定位

- 【Linux社区】Petersen：“Documentation/process 是所有提交共同实践与指南的正确位置；文档已很大；增强现有 process 文档好过增加更多查找处” `<!-- ROW_MINE: ksummit-discuss.messages.350874 -->`

## 81.19 【Linux社区】procmail版落地

- 【Linux社区】Borkmann：“rough version working——已 push；加了 procmail 示例配置；l2md→procmail→mutt 快速跑通” `<!-- ROW_MINE: ksummit-discuss.messages.350875 -->`

## 81.20 【Linux社区】Konstantin认可

- 【Linux社区】Konstantin：“Nice, thanks! 在有 backed by public-inbox 的整体补丁/系列管理工具前，这该能让大家预过滤消息” `<!-- ROW_MINE: ksummit-discuss.messages.350876 -->`

## 81.21 【Linux社区】KS2014档案-沙箱

- 【Linux社区】Luto（2014-05-21）：“如今必有明智方式构造沙箱——user namespaces+seccomp+VM 组合应相当安全易用；我在做基于 userns 的通用沙箱——KS 时或许有可用原型” `<!-- ROW_MINE: ksummit-discuss.messages.350877 -->`

## 81.22 【Linux社区】Corbet催迁

- 【Linux社区】Corbet：“一个月前问的没回音；想进 5.5——若我把你的补丁应用后再挪到 process guide 你反对吗？” `<!-- ROW_MINE: ksummit-discuss.messages.350878 -->`

## 81.23 【Linux社区】Williams同意迁

- 【Linux社区】Williams：“process book 是更好位置——信息现聚焦于作为提交者补充指南；我确实想 respin 去掉 Coding Style addendum 以回应具体反馈，除此之外乐见前进” `<!-- ROW_MINE: ksummit-discuss.messages.350879 -->`

## 81.24 【Linux社区】TAB章程修改

- 【Linux社区】Laura 公告 TAB 章程两改：invitees→attendees（“澄清 KS 不再仅邀请制”）+新增缺席投票条款（diff 全文）；“延续去年电子投票改革、缺席投票标准后宣布” `<!-- ROW_MINE: ksummit-discuss.messages.350880 -->`

## 81.25 【Linux社区】塞票担忧

- 【Linux社区】Pinchart：“好澄清无异议；缺席投票条款问题更大——意图好但会让塞票非常容易；不易设定不复杂的清晰规则；此刻无解可提” `<!-- ROW_MINE: ksummit-discuss.messages.350881 -->`

## 81.26 【Linux社区】威胁模型论

- 【Linux社区】Abbott：“ personally 想让更多人参与但难定现实威胁模型；TAB 靠社区信任运作；若 1 万 sock puppet 淹没投票选出多数不信任的 5 人——他们能有什么影响？章程另有 LF 董事会可终止 TAB 条款——毁灭性的边界方案”；“讨论已数月非仓促；措辞上 TAB 也可不开放缺席投票” `<!-- ROW_MINE: ksummit-discuss.messages.350882 -->`

## 81.27 【Linux社区】信任与成文

- 【Linux社区】Abbott：“刻意保持模糊以免每次微调都改章程；现行章程对投票如何进行什么都没说——社区信任我们设非候选人监票与公平程序；或许真正问题是社区是否宁愿所有选举程序显式成文而非信任 TAB” `<!-- ROW_MINE: ksummit-discuss.messages.350883 -->`

## 81.28 【Linux社区】选民池史

- 【Linux社区】Bird：“需要 TAB 随心可改之外的选民批准政策表达；选民池历来由 KS 邀请委员会决定+LF 同址活动随机性——自选但偏向能旅行/有雇主支持者；邀请委员会从未考虑 TAB 投票；愿现在 TAB 不乱来、未来 TAB 未知——成文政策更好” `<!-- ROW_MINE: ksummit-discuss.messages.350884 -->`

## 81.29 【Linux社区】COVID前瞻重磅

- 【Linux社区】Ted：“同址 LF 活动之选是 TAB 临场决定、章程无载——我们多年来已在不符合章程行事”；“Sad/Rabid Puppies 场景——单一 SoB 即得票则千个 sock puppet 拼写补丁涌入”；kernel.org 账户难被 sock puppet 满足；“须在下一轮提名前成文”；“COVID-19——Halifax 400-500 人会议能否办没人知道（引 Lancet 文）；若 2020 无会议可能被迫延任或纯电子投票” `<!-- ROW_MINE: ksummit-discuss.messages.350885 -->`

## 81.30 【Linux社区】kernelorg质疑

- 【Linux社区】Jani：“kernel.org 账户‘通常保留给子系统维护者或高调开发者’、管理员有裁量权——要 kernel.org 管理员对谁能投票有最终话语权？账户隐含 web of trust=须见过其他开发者——对包容不能到场者很别扭；只是代理标准且缺乏透明” `<!-- ROW_MINE: ksummit-discuss.messages.350886 -->`

## 81.31 【Linux社区】woT辩护

- 【Linux社区】Greg：“kernel.org 账户=验证你真是社区一员、在 web of trust、是真人——这是目标、有更好办法请告知；迭代多次当前最好方案；kernel.org admin 是 9 年团队非单人；账户获取有何不透明？” `<!-- ROW_MINE: ksummit-discuss.messages.350887 -->`

## 81.32 【Linux社区】KS2014档案-QR

- 【Linux社区】Kurusa（2014-05-21）：与 Teodora 团队定位——首要清理 QR 库、Teodora 或做 Android app 或 web 后端；“作为用户我完全不觉得报内核 bug 是享受——目标是让它更好；我们求的是讨论” `<!-- ROW_MINE: ksummit-discuss.messages.350888 -->`

## 81.33 【Linux社区】限制论

- 【Linux社区】Babka：“当前用途没问题、但作为 TAB 远程投票唯一标准会相当 restrict” `<!-- ROW_MINE: ksummit-discuss.messages.350889 -->`

## 81.34 【Linux社区】婴儿步

- 【Linux社区】Greg：“此前从无远程投票——所以是 less restrictive :)；这些是 baby steps——给 Laura credit：比过去十年的 nothing 好得多” `<!-- ROW_MINE: ksummit-discuss.messages.350890 -->`

## 81.35 【Linux社区】阶梯提案

- 【Linux社区】Geert：“下一步显然是‘列在 MAINTAINERS’——都可为真人；再下一步=有 SoB 的开发者+最低 commit 数防 whitespace-fixers 投票党”；“commit 计权：一年前半、N 年前 1/2^N；staging 清理加罚 ;-)” `<!-- ROW_MINE: ksummit-discuss.messages.350891 -->`

## 81.36 【Linux社区】透明之责

- 【Linux社区】Jani：“Ted 的信像抛出的想法而非定案”；“无法知道是否有投票资格直到申请获批或被拒；当前‘obvious’标准不 obvious——多少贡献够？高调如何定义？你们似乎认为 admin 团队主观裁量是好事——内部看着透明、外部不是——这就是透明的定义（或其缺失）”；附章程透明报告条款之问 `<!-- ROW_MINE: ksummit-discuss.messages.350892 -->`

## 81.37 【Linux社区】扩池论

- 【Linux社区】Greg：“是的且今天仍可现场投——这是扩池不是限池” `<!-- ROW_MINE: ksummit-discuss.messages.350893 -->`

## 81.38 【Linux社区】疫情暗讽

- 【Linux社区】Geert：“哦对——假设我们仍有线下会议与不受限旅行” `<!-- ROW_MINE: ksummit-discuss.messages.350894 -->`

## 81.39 【Linux社区】firststep辩

- 【Linux社区】Rostedt：“若不改投票要求而会议取消或旅行受限——那些人按现章程无法投票；我们在扩展而非限制——创造从未有过的缺席投票；TAB 内部 bikeshed 结论=kernel.org 账户是很好第一步；模糊措辞是为有更好方案时可换；眼下须让塞票困难” `<!-- ROW_MINE: ksummit-discuss.messages.350895 -->`

## 81.40 【Linux社区】渐进论

- 【Linux社区】Sasha：“我们的定义该是‘社区任何成员’但不现实；这过程要花数年、每年大幅扩池——与其纠结当年限制不如学习哪些有效哪些可解除” `<!-- ROW_MINE: ksummit-discuss.messages.350896 -->`

## 81.41 【Linux社区】参选资格问

- 【Linux社区】Jani：“我欢迎 TAB 更开放主动的沟通；考虑过参选与投票资格是否应一致吗？现在任何人可自荐参选” `<!-- ROW_MINE: ksummit-discuss.messages.350897 -->`

## 81.42 【Linux社区】历史观察

- 【Linux社区】Ted：“一直如此。但历史上不在场者从未成功；去年电子投票改革=书面提名陈述取代现场短陈述” `<!-- ROW_MINE: ksummit-discuss.messages.350898 -->`

## 81.43 【Linux社区】KS2014档案-沙箱分立

- 【Linux社区】Triplett（2014-05-21）：“正是我想的：不跑在 git.kernel.org/gitolite 上而在独立沙箱；不需要 tip-bot 完整 shell 配置普遍性——curated hook 集+每仓库 git 分支启停配置即可” `<!-- ROW_MINE: ksummit-discuss.messages.350899 -->`

## 81.44 【Linux社区】程序披露

- 【Linux社区】Konstantin：“MAINTAINERS 所列者自动获批 kernel.org 账户但必须满足 WoT：key 被 2 名已有账户者签或被 6 人名单（hpa/Greg/Ted/Linus/Hohndel/Bottomley）之一签；非 MAINTAINERS 者附理由申请、转 6 人至少一人 aye；‘活跃账户’=过去 12 个月有 git+ssh 操作”；“若我有恶意可颠覆全程——最终你得信我是 lawful good” `<!-- ROW_MINE: ksummit-discuss.messages.350900 -->`

## 81.45 【Linux社区】文档请求

- 【Linux社区】Jani：“谢谢澄清。可否把这些澄清写进 kernel.org/faq.html 与 korg.wiki 两个文档并让它们一致？” `<!-- ROW_MINE: ksummit-discuss.messages.350901 -->`

## 81.46 【Linux社区】章程请求

- 【Linux社区】Jani：“可否请求把这一点在 TAB 章程中澄清” `<!-- ROW_MINE: ksummit-discuss.messages.350902 -->`

## 81.47 【Linux社区】章程史

- 【Linux社区】Bottomley：“TAB 章程写于 2006——原由=防委员会操纵提名；TAB 由不满 OSDL 的内核开发者强行上董事会成立、保持内核-only 不是问题；OSDL 预见稀释内核开发者代表即可稀释改革影响；OSDL 变 LF 后敌意消退、选举开放给同址会议作为信任改善的标志” `<!-- ROW_MINE: ksummit-discuss.messages.350903 -->`

## 81.48 【Linux社区】历史例外

- 【Linux社区】Bottomley：“那是历史观察不是规则。其实有例外：GregKH 2012 年爱丁堡当选时未亲身到场投票（虽然人在爱丁堡）” `<!-- ROW_MINE: ksummit-discuss.messages.350904 -->`

## 81.49 【Linux社区】利益攸关论

- 【Linux社区】Rostedt：“drive-by 补丁发送者该有与花费数小时的维护者同等影响力吗？TAB=LF 的技术顾问委员会——为内核社区向 LF 施加影响；利益最大者应有最大影响——否则容易暴民心态、得到美国现在这种代表制” `<!-- ROW_MINE: ksummit-discuss.messages.350905 -->`
