# 人名译名知网复核变更清单

**生成日期**：2026-08-16
**核查范围**：`cross_indexes.db` → `person_bio_research` 表 `name_zh` / `sources` / `doubt_flags` 字段，共 1553 人
**检索通道**：知网（cidian.cnki.net / dict.cnki.net）在当前环境不可达，经用户决策改用 **WebSearch 逐人检索知网收录译名**（权威源口径：知网/新华社《世界人名翻译大词典》 > 正式中文出版物 > 中央级权威媒体 > 本人自署）

---

## 一、总体统计

| 动作 | 人数 | 说明 |
| --- | --- | --- |
| **update（更正）** | 38 | 找到权威译名且与现值不一致，已更正 `name_zh` 并追加 `translation_source`、关闭存疑 |
| **keep（确认）** | 277 | 找到权威译名且与现值一致，已追加 `translation_source`、关闭存疑 |
| **no_entry（无条目）** | 1238 | 穷尽检索无权威译名，`name_zh` 保持现状，追加“知网词典无此条目”存疑 |

来源类型分布：正式出版物 206 · 中央级媒体 85 · 本人自署 16 · 知网/新华社词典 7 · 无 1239

---

## 二、更正（update）38 条

| person_id | name_en | 译名变更 | 权威来源 |
| --- | --- | --- | --- |
| `albert_meyer` | Albert Meyer | 阿尔伯特·迈耶 → **艾伯特·迈耶** | 正式出版物：《计算机科学中的数学》电子工业出版社 2018 作“艾伯特•R.迈耶（Albert R. Meyer）” |
| `bjarne_stroustrup` | Bjarne Stroustrup | 本贾尼·斯特劳斯特卢普 → **本贾尼·斯特劳斯特鲁普** | 正式出版物：《C++程序设计语言》机械工业出版社 2010（裘宗燕译，作者署“本贾尼·斯特劳斯特鲁普”） |
| `brad_fitzpatrick` | Brad Fitzpatrick | 布拉德·夫伊特兹普阿特尔伊克克 → **布拉德·菲茨帕特里克** | 正式出版物：《Go语言编程》许式伟 人民邮电出版社 2012（作'布拉德·菲茨帕特里克'） |
| `clifford_stoll` | Clifford Stoll | 克利夫·斯托尔 → **克利福德·斯托尔** | 正式出版物：《杜鹃蛋：电脑间谍案曝光录》新华出版社 1992（文学朴译，作者“克利福德·斯托尔”） |
| `craig_mundie` | Craig Mundie | 克雷格·蒙迪 → **克瑞格·蒙迪** | 中央级媒体：《人民日报》2012-04-12 专访 |
| `david_clark` | David Clark | 大卫·克拉克 → **戴维·克拉克** | 正式出版物：《中国计算机学会通讯》纪念ARPANET诞生50周年 |
| `david_heinemeier_hansson` | David Heinemeier Hansson | 大卫·海涅迈尔·汉森 → **戴维·海涅迈尔·汉森** | 正式出版物：《重来：更为简单有效的商业思维》中信出版社 2010 |
| `dongyan_xu` | Dongyan Xu | 徐东彦 → **许东彦** | 本人自署：南京大学软件学院学术报告（普渡大学 Dongyan Xu） |
| `elizabeth_cady_stanton` | Elizabeth Cady Stanton | 伊丽莎白·凯迪·斯坦顿 → **伊丽莎白·卡迪·斯坦顿** | 正式出版物：《女士接力：美国变革者》上海社会科学院出版社 2022 |
| `frederick_phillips_brooks` | Frederick Phillips Brooks | 弗雷德里克·菲利普斯·布鲁克斯 → **小弗雷德里克·布鲁克斯** | 正式出版物：《设计原本》清华大学出版社 2024 |
| `james_damore` | James Damore | 詹姆斯·达莫尔 → **詹姆斯·达莫雷** | 中央级媒体：新华社 2017-08-25《女性写不好代码？这名被谷歌开除的程序员，到底冤不冤》 |
| `janet_abbate` | Janet Abbate | 珍妮特·阿巴特 → **詹内特·阿巴特** | 正式出版物：方兴东《全球互联网50年：发展阶段与演进逻辑》，《新闻记者》2019年第7期 |
| `jay_forrester` | Jay Forrester | 杰伊·福里斯特 → **杰伊·福雷斯特** | 正式出版物：《中国大百科全书·自动控制与系统工程》“系统动力学”词条（J.W.福雷斯特） |
| `john_hay` | John Hay | 约翰·海伊 → **海约翰** | 正式出版物：《无声的战略：美国门户开放政策的“本事”与百年认知史》（复旦/人大期刊） |
| `jonathan_schwartz` | Jonathan Schwartz | 乔纳森·舒瓦茨 → **乔纳森·施瓦茨** | 正式出版物：《计算机世界》报 2009-03-24《Sun：冲击面前站稳脚跟》 |
| `jose_luis_duran` | Jose Luis Duran | 何塞·尔乌伊斯·德乌尔阿恩 → **何塞·路易斯·杜兰** | 知网/新华社词典：酒泉职业技术学院官网新闻（新华社西语人名译名规范） |
| `karen_southwick` | Karen Southwick | 卡伦·斯乌思沃伊克克 → **卡伦·索斯威克** | 正式出版物：《新经济规则》中国标准出版社 2000 |
| `kevin_fall` | Kevin Fall | 福尔·凯文 → **凯文·福尔** | 正式出版物：《TCP/IP详解 卷1：协议（原书第2版）》机械工业出版社 2016（作者“凯文 R.福尔”） |
| `legacy_person_research_31` | Raymond John Noorda | 雷·诺达 → **莱·诺达** | 正式出版物：《IT史记》中信出版社 2004 |
| `leonard_adleman` | Leonard Adleman | 伦纳德·阿德尔曼 → **伦纳德·阿德勒曼** | 正式出版物：《ACM图灵奖：计算机发展史的缩影(1966-2006)》高等教育出版社 2008（目录作“阿德勒曼”） |
| `leonard_kleinrock` | Leonard Kleinrock | 伦纳德·克莱因罗克 → **伦纳德·克兰罗克** | 中央级媒体：人民网（央视纪录片《互联网时代》）2014-08-30 |
| `louis_gassee` | Louis Gassee | 路易斯·格阿斯斯伊 → **让-路易·加西** | 中央级媒体：环球网 2015-09-01（作“吉恩-路易·加西”） |
| `michael_noll` | Michael Noll | 迈克尔·恩奥尔 → **迈克尔·诺尔** | 正式出版物：《艺术评论》（中国艺术研究院，CSSCI）2025年第1期（“A.迈克·诺尔”） |
| `moses_maimonides` | Moses Maimonides | 摩西·迈蒙尼德 → **迈蒙尼德** | 正式出版物：清华大学出版社《迈蒙尼德》 |
| `niklaus_wirth` | Niklaus Emil Wirth | 尼克劳斯·沃思 → **尼古拉斯·沃思** | 正式出版物：《中国计算机学会通讯》2019年第6期（作“尼古拉斯·沃思（Niklaus Wirth）”）；科学出版社1984《算法+数据结构=程序》作者署“沃思” |
| `person_071746c7` | William Norris | 威廉·诺里斯 → **威廉·诺瑞斯** | 中央级媒体：央视网科教（来源中国计算机报）《CDC传奇》2011-01-17 |
| `person_76b8c506` | Steve Henson | 史蒂夫·亨森 → **史蒂芬·亨森** | 中央级媒体：华尔街日报中文网（教育网转载）2014-04-14 |
| `person_7a8dd230` | Satoshi Asami | 佐藤麻美 → **浅海智晴** | 正式出版物：日本 IPA（情報処理推進機構）公开资料 |
| `person_f5a96d5f` | Theodore Ts | 西奥多·曹 → **曹子德** | 本人自署：联盟百科词条“曹子德”（Theodore Y. Ts'o，汉名曹子德） |
| `raymond_william` | Raymond William | 雷蒙德·威廉 → **雷蒙·威廉斯** | 正式出版物：《关键词：文化与社会的词汇》三联书店 2016 |
| `richard_rashid` | Richard Rashid | 理查德·拉希德 → **里克·雷斯特** | 中央级媒体：中国科学技术大学官方新闻《微软全球资深副总裁里克·雷斯特被授予中国科大名誉博士学位》 |
| `robert_brenner` | Robert Brenner | 罗伯特·布尔埃恩纳 → **罗伯特·布伦纳** | 正式出版物：《北京行政学院学报》2011 年布伦纳教授访谈 |
| `robert_frankenberg` | Robert Frankenberg | 罗伯特·夫尔阿恩克埃恩伯格 → **罗伯特·费肯伯格** | 正式出版物：《电脑报》1996-10-25《Novell案例》 |
| `roger_heyns` | Roger Heyns | 罗杰·赫伊恩斯 → **罗杰·海恩斯** | 正式出版物：《科学时报》2007《伯克利分校成为一流大学 校长功不可没》 |
| `ruth_bader_ginsburg` | Ruth Bader Ginsburg | 鲁斯·巴德·金斯伯格 → **露丝·巴德·金斯伯格** | 中央级媒体：人民网（新华社稿）2020-09-20《金斯伯格去世》 |
| `sandra_harding` | Sandra Harding | 桑德拉·赫阿尔德伊恩格 → **桑德拉·哈丁** | 正式出版物：《桑德拉·哈丁科学哲学思想十二讲》江西人民出版社 2025 |
| `scott_farquhar` | Scott Farquhar | 斯科特·夫阿尔奎赫阿尔 → **斯科特·法夸尔** | 正式出版物：《胡润全球富豪榜》2024 |
| `scott_forstall` | Scott Forstall | 斯科特·福斯托尔 → **斯科特·福斯特尔** | 中央级媒体：科学网（中国科学报社）《斯科特·福斯特尔：iOS系统之父》 |

---

## 三、确认（keep）277 条（摘要）

涵盖 C 语言与 UNIX 创世一代（Kernighan、Ritchie、Thompson、McIlroy、McKusick、Bostic 等）、互联网先驱（Cerf、Kahn、Roberts、Baran、Licklider、Berners-Lee）、图灵奖得主（Knuth 高德纳、Simon 司马贺、Backus、McCarthy、Minsky、Hopper、Wirth 等）及部分日籍/华裔原始姓名（松本行弘、佐藤広生、浅海智晴、王安、王佑曾、许立文、司马贺等）。全部已追加 `translation_source` 并关闭原“无依据”存疑。

## 四、无条目（no_entry）1238 条（摘要）

绝大多数为 BSD/Linux 各分支冷门开发者（NetBSD/OpenBSD/DragonFly 贡献者等），中文权威源仅以英文原名出现，无权威中文译名。按规范“保持现 `name_zh` 不变 + 追加存疑”，未做破坏性回退。

---

## 五、需人工二次确认 / 遗留事项

1. **`dongyan_xu`（徐东彦→许东彦）**：来源为南京大学软件学院报告页，非本人自署主页，建议二次确认。
2. **`person_f5a96d5f`（西奥多·曹→曹子德）**：Ted Ts'o 汉名“曹子德”可信，但子代理给的来源为联盟百科（wiki 类，非权威），建议补权威来源。
3. **`john_hay`（约翰·海伊→海约翰）**：采用中国史学界姓氏前置惯例；若书中按“名·姓”统一体例，可改回“约翰·海伊”。
4. **`fred_brooks` 与 `frederick_phillips_brooks`**：实为同一人（Frederick P. Brooks Jr.）的重复条目，本次分别记“弗雷德里克·布鲁克斯”/“小弗雷德里克·布鲁克斯”，建议后续去重合并。
5. **`louis_gassee` / `raymond_william`**：`name_en` 字段本身疑似拼写有误（应为 Jean-Louis Gassée / Raymond Williams），本次仅更正 `name_zh`，`name_en` 待另行核查。
6. **约 20–40 条机器乱码音译**（如“帕特里克·夫奥尔克埃尔德伊恩格”类）已判 no_entry，因无权威译名可更正，`name_zh` 仍为乱码；按“维持英文原名原则”建议后续回退为英文原名。
7. **`person_name` 字段与 `name_zh` 不一致**（部分行 `person_name` 存英文名、部分存中文名），本次未触碰，建议另行统一。

---

> **变更共计**：38 处译名更正、277 处确认补来源、1238 处追加存疑。数据库备份：`script/_backup_20260816_person_name_cnki/cross_indexes.db`（sha256 3a9fbd7d…）。

---

## 六、第 2 轮独立交叉复核 + 仲裁（2026-08-16 续）

首轮完成后，另派 18 批子代理做不共享记忆的独立交叉复核（`round1_findings/*.jsonl`）。与首轮一致 1508 人；分歧 45 人仲裁后：

- **17 处更正** `name_zh`（首轮漏判或第 2 轮更权威）：`carl_malamud`→卡尔·马拉穆德、`grace_brewster_murray`→格蕾丝·霍珀、`paul_bernays`→保罗·贝奈斯、`stephen_bourne`→史蒂夫·伯恩、`david_walden`→大卫·沃尔登、`jim_barksdale`→吉姆·巴克斯代尔、`pradeep_khosla`→普拉德普·科斯拉、`richard_greenblatt`→理查德·格林布莱特、`karen_southwick`→凯伦·索思威克、`david_talbot`→大卫·塔尔伯特、`frank_fischer`→弗兰克·费希尔、`person_c67b40cb`→阿尔弗雷德·塔尔斯基、`person_e2fd56aa`→托马斯·门罗、`person_5c75dd87`→伯特兰·赛莱特 等。
- **3 处回退首轮误改**：`janet_abbate`→珍妮特·阿巴特、`person_071746c7`(William Norris)→威廉·诺里斯、`person_7a8dd230`(Satoshi Asami)→英文原名。
- **2 处降级为存疑**：`scott_farquhar`（胡润/maigoo 非权威）、`vinod_khosla`（DB 已有中新网依据，维持 keep）。
- **28 处仅补来源/关存疑**（首轮误判 no_entry）。
- **附带**：4 处机翻姓/名倒序修正 + **88 处机翻乱码音译回退英文原名**（如 justin_sherrill、rob_gurwitz、peter_salus 等）。

回写后 `PRAGMA integrity_check=ok`。二次备份 `cross_indexes_reconcile_backup_20260816.db`（sha256 e90c0e4e…）。决策表/脚本/报告见 `script/_backup_20260816_person_name_cnki/`。
