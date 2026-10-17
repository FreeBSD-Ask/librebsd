# 61 【Linux社区】CoC补丁v3与测试基建议题

> 来源：ksummit-discuss p113（50 封全读，2018-10-16/18 为主，夹杂 KS2014 档案信 2014-05-15/16）。
> 判定：48 CAND / 2 NV。主题分布：CoC补丁v3流转 4、MS议程出席辩论 9、测试基建议题 8、CoC歧视列表之争 11、CoC email措辞之辩 11、KS2014档案 5。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p113（pk 349856-349905）的逐封提取（48 CAND / 2 NV），全 5 块采用**导语＋带锚条目体例**：每块由“## 61.x 【Linux社区】题名”＋导语段＋“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——导语段承担“要点”职能、带锚条目承担“史料”与“史料锚”职能（ROW_MINE 坐标与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 61.1 【Linux社区】CoC 补丁 v3 三连发与 MS 议程出席之辩

2018-10-16 CoC 补丁 v3 三连发（email 措辞/剥 enforcement 起点、Reporting 节回归+法定例外）与 Maintainer’s Summit 出席名单之辩：领域专家论、营销与信心工程两面论、火与怒无近事例、carefully cut 交锋与 Bottomley 道歉、讨论会非决策会定性。

- 【Linux社区】Bottomley [PATCH v3 1/3] email 措辞修复：发布“not ordinarily collected by the project”的地址才属不可接受行为；tags 累计 Geert/Shuah/Roeck/Cox/Chehab/Biederman/Cook `<!-- ROW_MINE: ksummit-discuss.messages.349856 -->`
- 【Linux社区】[v3 2/3] 剥 enforcement 段 15 行：虑 4.19 发布即具约束力、给社区时间辩论；明言共识后再加回 enforcement 章节 `<!-- ROW_MINE: ksummit-discuss.messages.349858 -->`
- 【Linux社区】[v3 3/3] 加回 Reporting 节以 TAB 为中央报告点；v3 保密义务加“except where required by law”限定 `<!-- ROW_MINE: ksummit-discuss.messages.349859 -->`
- 【Linux社区】Shuah Acked v3 3/3：TAB 中央报告点加回获认可 `<!-- ROW_MINE: ksummit-discuss.messages.349891 -->`
- 【Linux社区】Bottomley 回 Vetter：MS 场地突变总有人来不了、KS Vancouver 照开且 CoC 话题对 LPC 全体开放；“火与怒中无人举得出近期事例——一切都至少两年旧” `<!-- ROW_MINE: ksummit-discuss.messages.349860 -->`
- 【Linux社区】Triplett 领域专家论：不咨询虚拟化专家不会造虚拟化子系统、不咨询存储专家不会造存储、不动许可证不咨询法律专家——CoC 变更同理 `<!-- ROW_MINE: ksummit-discuss.messages.349861 -->`
- 【Linux社区】Brown 两面论：无公认专家也可做好 CoC，但其本质是营销与信心工程、内核背负声誉赤字，专家在场有助对外解释；可把部分决定推迟到邮件列表 `<!-- ROW_MINE: ksummit-discuss.messages.349862 -->`
- 【Linux社区】Bottomley 回 Triplett：指控其“carefully cut”回避内核内部即有领域专家＋外部专家至今无人提名；“我们通常也不恭敬听专家——spectre meltdown 即为例证” `<!-- ROW_MINE: ksummit-discuss.messages.349863 -->`
- 【Linux社区】Mason（Facebook）降温：MS 与 Plumbers 只是持续对话一部分、问题清单仍在成形、难配完美名单；强烈同意把部分决定推迟到列表 `<!-- ROW_MINE: ksummit-discuss.messages.349864 -->`
- 【Linux社区】Tim Bird 批措辞：“carefully cut”暗含恶意逾越本意；Vetter 显然指已采 CoC 的 DRM 子系统；不必恭敬也能受益于专家经验；反对此刻改名单——“我也没被邀请” `<!-- ROW_MINE: ksummit-discuss.messages.349865 -->`
- 【Linux社区】Triplett 谢 Bird 后定性：不要求改名单，而是该名单利于讨论不利于决定——与会者应视其为讨论会而非决策会 `<!-- ROW_MINE: ksummit-discuss.messages.349866 -->`
- 【Linux社区】Bottomley 道歉误读与过激：自曝“见太多人付出巨大努力而零认可故过敏”；同意开放的 KS/Plumbers 场次更重要 `<!-- ROW_MINE: ksummit-discuss.messages.349867 -->`
- 【Linux社区】Vetter 澄清：与己无关（日程已订满）、ELC 本就有一批 DRM 人在场、非差旅物流问题；“去年就有讨论我们该派谁顶替 Dave” `<!-- ROW_MINE: ksummit-discuss.messages.349869 -->`

## 61.2 【Linux社区】回归测试基建议题与 ATS 邀请制风波

Borntraeger 从 MS 议程空 slot 引出的回归测试基建议题：Ted 的流程/技术分场与架构资源方论、SUSE 的 Power/Z 立场、Roeck 的场地重复之疑、ATS 邀请制引出的 Ellerman 慕名求入与 Tim Bird 的录像补救承诺、Shuah 的 Kselftest 代言举荐。

- 【Linux社区】Borntraeger 抓 MS 议程 2:30/4:30 TBD 空 slot 提新议题：盘点现有测试基建（syzbot、Geert/Roeck 例行报告）、缺哪些架构、in-house 测试只报错可否、缺哪些测试场景 `<!-- ROW_MINE: ksummit-discuss.messages.349870 -->`
- 【Linux社区】Ted：技术议题更适合 Vancouver KS 轨、MS 专注流程；架构缺失应问能带来资源者——Itanium/pa-risc 问 Intel/HP 恐获 obsolescent 回复；Power/Z/RISC-V 问背后公司 `<!-- ROW_MINE: ksummit-discuss.messages.349871 -->`
- 【Linux社区】Kosina：SUSE 将在 LPC/KS Vancouver 有像样代表、“我们（部分）靠 Power 与 Z 系列为生”、若其他同处境厂商到场可成有效讨论 `<!-- ROW_MINE: ksummit-discuss.messages.349872 -->`
- 【Linux社区】Roeck 列已有两场地：Edinburgh Automated_Testing_Summit＋Vancouver testing-and-fuzzing-mc；乐见兴趣增长但质疑再加一个讨论场是否合理 `<!-- ROW_MINE: ksummit-discuss.messages.349873 -->`
- 【Linux社区】Ted：忘了 Plumbers 的 Testing and Fuzzing MC、同意那是对的讨论地；MC 日程若满可排 kernel summit track，但最好都聚 MC——对的人都在那里 `<!-- ROW_MINE: ksummit-discuss.messages.349874 -->`
- 【Linux社区】Ellerman：ATS“第一次听说，Mind if I drop in? :)”——邀请制会议的信息可见性问题实例 `<!-- ROW_MINE: ksummit-discuss.messages.349875 -->`
- 【Linux社区】Tim Bird：ATS 场地有限、与 Kevin 决定邀请制且流程已毕保持小规模；Linaro 将录制、Kevin Hilman 拟在 LPC testing 场次汇报；盼未来办更开放的 automated-testing 活动 `<!-- ROW_MINE: ksummit-discuss.messages.349876 -->`
- 【Linux社区】Shuah 力荐 Ellerman 与会代言 Kselftest：其做了共同框架奠基工作、slides 已发——“有本人在场胜过一切” `<!-- ROW_MINE: ksummit-discuss.messages.349877 -->`

## 61.3 【Linux社区】删除歧视因素列表之争：UNESCO 引文与 include but not limited to

Geert 删列表补丁引发的文法与法律之辩：UNESCO 反种族文献引证、explicit list 的边际语义、Roeck 的折中措辞与政治表达质问、Bottomley 的第九修正案类比与“include but are not limited to”定案方向、Brown 的复制粘贴贬值警语。

- 【Linux社区】Geert [PATCH] 删歧视因素显式列表：显式列表给人“未列因素可歧视”的错觉；删至“harassment-free experience for everyone”句号；引 UNESCO《The Race Question》与《Declaration on Race and Racial Prejudice》 `<!-- ROW_MINE: ksummit-discuss.messages.349881 -->`
- 【Linux社区】Geert v2 增 Acked（Rowand/acme/Tomi），UNESCO 引文同前 `<!-- ROW_MINE: ksummit-discuss.messages.349882 -->`
- 【Linux社区】Triplett 反对：该印象本就错误且已讨论；原 commit 明言 explicit guidelines 有跨项目成功先例；列出不意味未列不覆盖、但确保已列情形确实被覆盖——“此补丁不 OK，击败原变更目的之一” `<!-- ROW_MINE: ksummit-discuss.messages.349883 -->`
- 【Linux社区】Geert 反问三连：CoC FAQ 不是 CoC 一部分、不精确就该改 CoC 本体；GPL/FAQ 类比不当（GPL 仍是精确法律文件）；原 commit 未经公开评审无人能要求举证——“你同意人们无法知道未列情形是否被覆盖？” `<!-- ROW_MINE: ksummit-discuss.messages.349884 -->`
- 【Linux社区】Roeck 折中建议：加“discrimination factors such as”或“or any other discrimination factors not listed here”或“regardless of, for example, ...” `<!-- ROW_MINE: ksummit-discuss.messages.349885 -->`
- 【Linux社区】Roeck 回 Triplett：数学上你的陈述不成立；政治/社会观点未列——同款 CoC 在其他项目被用来惩罚项目外的特定政治表达？CoC 将维护者单独挑出执法是否有意为之？ `<!-- ROW_MINE: ksummit-discuss.messages.349886 -->`
- 【Linux社区】Triplett 回 Geert：“regardless of ...”仍说 for everyone 故本就非穷尽；边缘群体常不知自身是否被考虑、显式纳入是优秀 CoC 的通行准则；建议添加而非删除且先上游 `<!-- ROW_MINE: ksummit-discuss.messages.349888 -->`
- 【Linux社区】Triplett 回 Roeck：三种措辞均为完美合理方案、请据此向上游提交补丁 `<!-- ROW_MINE: ksummit-discuss.messages.349889 -->`
- 【Linux社区】Bottomley 法律视角：真空中枚举特定阶层有法律风险、枚举是否贬低他人是数百年之争、美国宪法第九修正案即为此；通行做法“examples of X include but are not limited to”，美国企业 CoC/ethics 皆然 `<!-- ROW_MINE: ksummit-discuss.messages.349892 -->`
- 【Linux社区】Triplett：Bottomley 方案远优于整删列表 `<!-- ROW_MINE: ksummit-discuss.messages.349893 -->`
- 【Linux社区】Brown 现实警语：强推显式列表反而使其贬值的抱怨渐多——难辨复制粘贴还是真理解；朋友在同性恋死罪国办会质疑列入 sexuality 的轶事；此类问题从无唯一正确答案 `<!-- ROW_MINE: ksummit-discuss.messages.349894 -->`

## 61.4 【Linux社区】email 地址措辞之辩：carve out 与 public space

v3 1/3 email 措辞的语义拉锯：Rowand 的 which/where 之辨与 public 定义清单、bugzilla 与私密补丁的边界案例、Bottomley 的 carve out 非许可论与 doxxing/房产记录收束、Tim Bird 的 FAQ 路线与删 such as 方案——CoC email 例外条款的全部论证面。

- 【Linux社区】Rowand 重复 v1 意见：概念同意但“ordinarily collected by the project”≠“provided in a public space”；ordinarily collected 可含预期私有、外人不可见的活动 `<!-- ROW_MINE: ksummit-discuss.messages.349878 -->`
- 【Linux社区】Bottomley：carve out 非 blanket permission——是排除出不可接受行为清单而非授予许可；询问“还有什么 ordinarily collected 的信息该视为私有” `<!-- ROW_MINE: ksummit-discuss.messages.349880 -->`
- 【Linux社区】Rowand 深度澄清：误会源于自己该用 carve out 而非 permission 措辞；真正关切是“哪些地址”而非“何处可发”；以公司隐私披露类比；给出简明 public 定义清单（可订阅列表/公开存档/公开 chat/公开网页） `<!-- ROW_MINE: ksummit-discuss.messages.349895 -->`
- 【Linux社区】Randy Dunlap 插问：bugzilla.kernel.org 提交者邮箱算私有吗——“他们看起来是公开的” `<!-- ROW_MINE: ksummit-discuss.messages.349896 -->`
- 【Linux社区】Bottomley 点明 crux：你认为 carve out 等价许可故不够具体、我认为根本不等价故无需更具体；许可细节留给项目贡献文档定义 `<!-- ROW_MINE: ksummit-discuss.messages.349897 -->`
- 【Linux社区】Belloni：格式正确补丁（含 From/SoB）只发 maintainer 不抄列表显然是为合入内核——public 定义清单的边界案例 `<!-- ROW_MINE: ksummit-discuss.messages.349898 -->`
- 【Linux社区】Rowand 回 Bottomley：接受 goal＝carve out；关切仍是 which email addresses；提出替代措辞“address that has been provided in a public space for the project, without explicit permission” `<!-- ROW_MINE: ksummit-discuss.messages.349899 -->`
- 【Linux社区】Bottomley：carve out 应宽到覆盖贡献文档可能说的任何内容、故“not ordinarily collected by the project”外仍属不可接受行为；请 Rowand 直接提议其想见的措辞 `<!-- ROW_MINE: ksummit-discuss.messages.349902 -->`
- 【Linux社区】Rowand 最终提案：Alternative “address that has been provided in a public space for the project, without explicit permission”；“See you in Edinburgh” `<!-- ROW_MINE: ksummit-discuss.messages.349903 -->`
- 【Linux社区】Tim Bird 综述：Rowand 文案缺 not；决定不动 CoC 本体、只在上游 CoC FAQ 增澄清；理由“such as”系例示非穷尽；观点一：若改则删“such as...”整句；观点二：保留原句＋澄清文档亦可 `<!-- ROW_MINE: ksummit-discuss.messages.349904 -->`
- 【Linux社区】Bottomley 收束：美国地址本在公共空间（房产记录）——doxxing 多为从公共来源翻出并广播、这正是选“not ordinarily collected”的原因；Tim 删“such as”方案同样可行；单一 CoC 应与运作方式一致故提补丁 `<!-- ROW_MINE: ksummit-discuss.messages.349905 -->`

## 61.5 【Linux社区】KS2014 档案五封

页内夹杂的 KS2014 档案信（2014-05-15/16）：Move Fast and Oops Things 三议题与吴峰光提名、Pinchart 的 IOMMU/复合设备 PM 依赖两实例与 power domains 质疑、Zanussi 补充提名、Cooper 的 IoT 可抛弃设备思路。

- 【Linux社区】Dan Williams [CORE TOPIC][nomination] Move Fast and Oops Things：以 Facebook 开发统计对比 kernel.org 提问“能否再快 2 倍”；三议题 Merge Karma（评审数据私有收集防武器化）/Gatekeeper（qualified no、替代 CONFIG_EXPERIMENTAL、覆盖变量即 taint）/LKP 单测文化；自提名并提名吴峰光（2014-05-15 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349857 -->`
- 【Linux社区】Pinchart PM dependencies 两实例长文：IOMMU 藏于 DMA API 之后 bus master 无法显式管理其电源态；嵌入式相机复合设备——ISP 供时钟给 sensor、ISP 与 I2C 控制器同级致 resume 顺序无保、ISP 只在 PM resume 回调恢复时钟而在 complete 回调重启视频流（2014-05-15 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349868 -->`
- 【Linux社区】Pinchart 回 Shuah：power domains 建模共享电源组、疑难建模设备间 PM 依赖；DMA mapping API 藏 IOMMU 致依赖方无从接触被依赖方；ad-hoc 与通用方案之辨需全面用例清单（2014-05-15 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349879 -->`
- 【Linux社区】Triplett 补充提名 Tom Zanussi（Tinification/embedded）——Josh Boyer 提名名单汇总后的追加（2014-05-16 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349890 -->`
- 【Linux社区】Jason Cooper 2038 线：IoT 设备部署后永不更新；验证基础设施＋密钥管理否则成攻击面、对此不乐观；备选思路“设备足够可抛弃、过期设备被网络拒绝、用户下单换新”（2014-05-16 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349901 -->`
