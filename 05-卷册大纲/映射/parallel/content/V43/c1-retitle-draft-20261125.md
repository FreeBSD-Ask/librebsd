# V43 第 1 章改题拟稿（retitle-V43-c1-draft，2026-11-25）

> **性质**：子代理拟稿件，供主会话落账用；本件不改任何树件、台账、标题真值与批准件。卷／章／节题不动，只拟第 1 章 25 个小节题。
> **依据**：162 号文 v4.1 §15.4.2（拟定面免批、分布自检必填）＋V75 第 1 章三稿六规则（冒号 0／设问 ≤3／题长有意拉开／“的”题同节 ≤半数／禁默认三件套／抽象动名词尾 0／构式族每节 ≥3）＋同期经典计算机史著作题名参照 §二（实义锚作中心语、版本与机构直接入题、题长不齐为常态）。
> **形态纪律**：沿用 V50 第 1—3 章获 ykla 认可的“完整主谓句优先、主语入题、对象全称、独立可读”，不用压缩生造词；机判豁免面（C8 系）只披露。
> **实锚来源**：`www.netbsd.org/about/history.html`、`/about/`、`/about/system.html`、`/about/portability.html`、`/ports/`、`/docs/guide/en/chap-intro.html`、`/releases/release-map.html`、`/releases/formal.html`、1.0／1.5／3.0 发行公告、USENIX BSDCon 2002 van der Linden 论文；逐条引文与访问日见 `c1-evidence-draft-20261125.tsv`，访问日 2026-11-25。
> **章题**：分化轴总论：从 BSD 遗产到可移植性原则（1993–2026）（不动）。

## 一、逐题对照（25 题）

### 1.1 NetBSD 分化轴的形成：质量优先与架构独立

| subsection_id | 旧题 | 判定 | 新题 | 实锚依据 | 题长 | 句式族 |
| --- | --- | --- | --- | --- | ---: | --- |
| V43.1.1.1 | 质量优先的取向确立 | 改 | 创始者以质量与架构独立定下取向 | history 页 “NetBSD's original focus was quality and architecture independence.” | 15 | 主谓宾（施事＋以…定下） |
| V43.1.1.2 | 架构独立的工程诉求 | 改 | 架构独立靠代码质量落地 | Guide 1.2 “portability is tied to code quality” | 11 | 主谓（条件式） |
| V43.1.1.3 | 386BSD 停滞的分叉背景 | 改 | 补丁积压与上游拒收促成项目分叉 | history 页 “inability to get patches included in 386BSD led to the founding” | 15 | 因果句 |
| V43.1.1.4 | 与 FreeBSD 的路线分化 | 改 | FreeBSD 专注 i386 个人机 | history 页 “FreeBSD was formed later with a focus on the i386 PC platform.” | 19 | 对比句（他支入题） |
| V43.1.1.5 | 质量主张的文本出处 | 改 | 质量主张见诸官方目标清单 | about 页 “provides a well designed, stable, and fast BSD system” | 12 | 判断句（见诸） |

### 1.2 “运行在一切硬件上”的工程理想与文化含义

| subsection_id | 旧题 | 判定 | 新题 | 实锚依据 | 题长 | 句式族 |
| --- | --- | --- | --- | --- | ---: | --- |
| V43.1.2.1 | 单源码树的多平台承诺 | 改 | 单源码树支撑数十种系统架构 | 1.5 公告 “all from a single source tree”；3.0 公告同句 | 13 | 主谓宾（工具作主语） |
| V43.1.2.2 | 硬件覆盖的实际广度 | 改（filled 迁移） | 平台清单横跨服务器桌面与嵌入式整机 | ports 页 “modern server, embedded and desktop architectures”；Guide 1.3 平台枚举 | 17 | 并列覆盖句 |
| V43.1.2.3 | 可移植理想的工程内涵 | 改 | 可移植性属于工程能力而非宣传词 | portability 页 “code is written once, and used many times”；van der Linden “code is shared between ports” | 15 | 判断句（属于…而非） |
| V43.1.2.4 | 口号与工程能力的落差 | 改（filled 迁移） | 单一平台使用者难体会可移植成本 | Guide 1.2 “if you work on just one platform you could think that you're not interested in portability” | 15 | 难易句（否定式） |
| V43.1.2.5 | 口号的流传与接受 | 改 | 最可移植之说定型于公告 | 1.5 公告 “widely known as the most portable operating system in the world” | 11 | 来源句（定型于） |

### 1.3 MI／MD 分层背后的组织哲学与技术伦理

| subsection_id | 旧题 | 判定 | 新题 | 实锚依据 | 题长 | 句式族 |
| --- | --- | --- | --- | --- | ---: | --- |
| V43.1.3.1 | MI/MD 分层的职责划分 | 改 | 平台无关层与平台相关层各担其责 | portability 页 “cleanly split into … (MD) and … (MI) areas” | 15 | 分工句（双主语＋各担） |
| V43.1.3.2 | 平台无关改动的测试要求 | 改 | 平台无关改动须至少在一个移植上验证 | ports 页 “MI changes must be tested on at least one of these ports.” | 17 | 义务句（须） |
| V43.1.3.3 | 分层收益的分配原则 | 改 | 分层收益向重点移植倾斜 | ports 页 “MI changes should benefit these ports.” | 11 | 趋向句（向…倾斜） |
| V43.1.3.4 | 分层对弱势移植的影响 | 改 | 次级移植为分层裁决承担代价 | ports 页 “may penalize organic ports if there is a benefit for focus ports” | 13 | 代价承担句 |
| V43.1.3.5 | 三分层体系的划分标准 | 改 | 三层分级依架构重要性与社区活跃度 | ports 页 “three tiers based on … importance … community activity” | 16 | 依据句（依） |

### 1.4 可移植性、正确性与长期维护之间的取舍

| subsection_id | 旧题 | 判定 | 新题 | 实锚依据 | 题长 | 句式族 |
| --- | --- | --- | --- | --- | ---: | --- |
| V43.1.4.1 | 性能与正确性的权衡 | 改 | 不正确即不成立成为取舍准绳 | system 页 “It doesn't work unless it's right” | 13 | 判断句（口号作主语） |
| V43.1.4.2 | 桌面体验的让步幅度 | 改 | 桌面体验让位于包集合 | 1.5 公告 “KDE and GNOME desktops … through our package system”；Guide 1.5 两万包 | 10 | 让位句 |
| V43.1.4.3 | 长期维护的成本核算 | 改 | 代码膨胀必须压到最低限度 | system 页 “code bloat has to be kept to a minimum”；Guide 1.2 “overgrown programs” | 12 | 义务句（必须） |
| V43.1.4.4 | 移植件与发布的取舍 | 改 | 发布时不可用的移植被剔除并降级 | ports 页 “a release is done without the port and the port is moved down” | 15 | 被动句 |
| V43.1.4.5 | 工程目标的优先次序 | 改 | 质量与正确性排在可移植性考量之前 | about 页目标列序；Guide 1.2 特性列序（质量在前） | 16 | 排序句（排在…之前） |

### 1.5 NetBSD 项目史的分层：本体事件与制品事件（1993–2026）

| subsection_id | 旧题 | 判定 | 新题 | 实锚依据 | 题长 | 句式族 |
| --- | --- | --- | --- | --- | ---: | --- |
| V43.1.5.1 | 本体事件与制品事件的分野 | 改（filled 迁移） | 组织事件与制品事件分属两层证据链 | 本节 thesis 与 `section_note`（本体／制品分层、证据来源不同） | 16 | 分属句 |
| V43.1.5.2 | 版本节点的编年骨架 | 改 | 点版本向上归并成编年骨架 | release-map 页 “give rise to formal minor releases, e.g., 6.1” | 12 | 归并句 |
| V43.1.5.3 | 组织变革的事件清单 | 改（filled 迁移） | 核心组名单本身就是一手记录 | 本节 thesis（核心组人事更替为主干，名单即一手记录） | 13 | 判断句（本身就是） |
| V43.1.5.4 | 分期界面的选取依据 | 改 | 分期起点取自代码血缘交接处 | Guide 1.1 “springs from the 4.3BSD Lite … and from the 386BSD system” | 13 | 来源句（取自） |
| V43.1.5.5 | 双层叙述的史料配置 | 改（filled 迁移） | 两套分支需要两套史料 | 本节 thesis（稳定分支与开发分支记录方式不同） | 10 | 需求句（需要） |

## 二、分布自检（机判口径）

- **冒号**：0；**设问**：0（章内上限 3）。
- **题长**：10—19 字；逐节极差 1.1＝8（11—19）／1.2＝6（11—17）／1.3＝6（11—17）／1.4＝6（10—16）／1.5＝6（10—16）。
- **“的”字题**：1/25（仅 1.4.4“发布时不可用的移植被剔除并降级”），逐节均 ≤ 半数。
- **构式族**：逐节 4—5 族（1.1 五族／1.2 五族／1.3 五族／1.4 四族／1.5 五族），满足每节 ≥3。
- **抽象动名词尾**：0（无“的确立／的实现／的形成／的引入”类收尾；1.4.3 用“限度”、1.4.5 用“之前”，均为具体限定语）。
- **尾簇自检**：对 `映射/title-design/V43.tsv` 全 220 题替换本章 25 题后复算，二字尾簇无 >3 者（原在帽值 3 的“前提／要求／次序”等簇未被顶破；1.4.3 由“前提”改为“限度”即为避帽）。
- **重复题**：全卷无重复。
- **默认三件套**：未用“背景—意义—影响”“起源—发展—评价”等三元套式；五题一节的差异由实锚（history／ports／release-map／Guide）承担。
- **保留题**：0 题。原 25 题全部为 8—11 字“X 的 Y”偏正题，任取其一都同时违反“题长拉开（同节极差 ≥6）”与“的题同节 ≤半数”两条硬规则，故不设保留；各行为此在“判定”列注明改题理由属章级而非逐题特例。

## 三、需主会话注意的三点

1. **filled 迁移题**：1.2.2／1.2.4／1.5.1／1.5.3／1.5.5 为 `filled`，改题只换题名与 H1，块内容与锚不动；但 1.2.4／1.5.3／1.5.5 的现有 ROW_MINE 块与 thesis 关联偏弱（port-alpha 杂项），题名按 thesis 拟定后，块文与题面的贴合度须在迁移批披露，必要时另行补块。
2. **1.1.4 的 FreeBSD 表述**：只写“专注 i386 个人机”，不写“转向”或分家时间，避免与史页“formed later”及本卷其他章的分叉叙述冲突。
3. **1.4.5 的“列序即优先序”**：属解释性判断，正文应以原序引文呈现（about 页五项目标、Guide 六项特性），不在题面写“第一”“首要”等绝对词。
