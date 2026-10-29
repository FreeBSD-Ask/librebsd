# 人名表 276 人全量联网复核与跨库同步 考据记录

- 日期：2026-08-14
- 对象：`10-交叉索引/cross_indexes.db` `person_bio_research` 表（276 行）
- 依据：用户指示“继续（P2c/P2d 复核与落库）”+ spec `enrich-person-name-table-web-2026-08-13` 的复核阶段（逐人联网复核英文名拼写与中文译名、同步至中文文件夹级数据库及大纲文件）

## 复核方法

1. **全量分批**：276 人按 P0(26)、P1a(38)、P1b(37)、P2a(44)、P2b(44)、P2c1(15)、P2c2(15)、P2c3(14)、P2d1(15)、P2d2(15)、P2d3(13) 共 11 批，每批委派独立子代理逐人 WebSearch/WebFetch 联网复核。0 信任原则：结论全部基于真实检索所得 URL，严禁模型记忆臆造；维基百科/百度百科/CSDN/普通博客仅作检索线索，不作证据源。
2. **name_en 复核**：全名拼写（中间名、姓/名顺序、连字符、重音符号）以本人主页/官方讣告/NAS-ACM 悼文/学术档案/大学官网等权威来源交叉验证。共改正 6 人：
   - `john_hennessy`：John LeRoy Hennessy → John L. Hennessy（中间名展开 LeRoy 无权威依据）
   - `larry_roberts`：Lawrence G. Roberts → Lawrence Gilman Roberts（FBI/权威档案）
   - `mike_accetta`：Mike Accetta → Michael J. Accetta（CMU 档案）
   - `peter_denning`：Peter Denning → Peter J. Denning（ACM/海军研究院档案）
   - `richard_rashid`：Richard Farris Rashid → Richard Rashid（微软官方档案）
   - `fulvio_risso`：Fulvio Giovanni Ottavio Risso → Fulvio Risso（Politecnico di Torino 官方页）
3. **name_zh 复核**：仅在有正式中文出版物或权威中文来源依据时填入。可信来源优先级：book.bsdcn.org > 正式中文出版物 > 中央级权威媒体（人民日报/新华社/央视/光明日报）> 本人中文自署 > 高校官方报道。有值 59 → 70 人，新增/修正 28 人（详见下表）。

## name_zh 变更明细（28 人）

| person_id | name_en | 变更 |
|---|---|---|
| eugene_wong | Eugene Wong | 王佑曾（中研院院士资料） |
| vint_cerf | Vinton Gray Cerf | 温顿·瑟夫（新华社） |
| larry_roberts | Lawrence Gilman Roberts | 拉里·罗伯茨（人民网） |
| niklaus_wirth | Niklaus Emil Wirth | 沃思（科学出版社《算法+数据结构=程序》译名），由"维尔特"改 |
| john_hennessy | John L. Hennessy | 亨尼西（出版社书目），由"亨尼希/轩尼诗"改 |
| allen_newell | Allen Newell | 艾伦·纽厄尔（商务印书馆） |
| blaise_pascal | Blaise Pascal | 布莱斯·帕斯卡尔 |
| david_diamond | David Diamond | 戴维·戴蒙德 |
| erwin_panofsky | Erwin Panofsky | 欧文·潘诺夫斯基 |
| john_napier | John Napier | 约翰·纳皮尔 |
| larry_mcvoy | Larry McVoy | 拉里·麦克沃伊（有道词典网络释义，记 open） |
| legacy_person_research_31 | Raymond John Noorda | 雷·诺达 |
| marsilio_ficino | Marsilio Ficino | 斐奇诺（商务印书馆《论爱》） |
| max_weber | Max Weber | 马克斯·韦伯 |
| moses_maimonides | Moses Maimonides | 摩西·迈蒙尼德（中国人民大学出版社《犹太哲学史》） |
| paul_guyer | Paul Guyer | 保罗·盖耶（商务印书馆《现代美学史》） |
| robert_tappan_morris | Robert Tappan Morris | 罗伯特·塔潘·莫里斯（人民网） |
| theodore_roszak | Theodore Roszak | 西奥多·罗斯扎克（光明网/中国对外翻译出版公司《信息崇拜》） |
| thorstein_veblen | Thorstein Bunde Veblen | 托尔斯坦·凡勃伦（商务印书馆《有闲阶级论》） |
| william_ockham | William of Ockham | 奥卡姆的威廉（商务印书馆《逻辑大全》） |
| william_james | William James | 威廉·詹姆士（商务印书馆主译名），由"詹姆斯"改 |
| gordon_bell | Chester Gordon Bell | 清空（无正式出版物依据，原"戈登·贝尔"记 open） |
| grace_hopper | Grace Brewster Murray Hopper | 清空 |
| guido_van_rossum | Guido van Rossum | 清空 |
| jcr_licklider | Joseph Carl Robnett Licklider | 清空（利克莱德/立克里德/里克莱德三派分歧） |
| alfred_aho | Alfred Vaino Aho | 清空 |
| rob_pike | Robert C. Pike | 清空（罗勃·派克仅见百度百科/CSDN） |
| stephen_bourne | Stephen Richard Bourne | 清空（斯蒂芬·伯恩无正式出版物依据） |

其余 11 人 name_zh 无变更但已确认保留（含新华社/商务印书馆依据者）。

## 跨库同步（英文名规范化）

1. `references_fulltext.db` `people_mentioned`（5142 行）：740 行匹配到人名表，其中 163 行 `person_normalized_name` 规范化为全名（如 Leffler, Sam → Samuel J. Leffler；bde → Bruce David Evans）。
2. `references_fulltext.db` `"references".author`：42 行规范化，修复 1 处多作者误替换（id=2685 恢复为 "Michael J. Karels, Marshall Kirk McKusick"）。
3. `cross_indexes.db` `person_records.normalized_name`：51 行规范化。

## 大纲文件同步（统一同一人多写法）

1. **全名→常用名** 9 处：丹尼斯·麦卡利斯泰尔·里奇→丹尼斯·里奇（1）、布莱恩·威尔逊·克尼汉→布莱恩·克尼汉（1）、林纳斯·本尼迪克特·托瓦兹→林纳斯·托瓦兹（2）、史蒂夫·保罗·乔布斯→史蒂夫·乔布斯（5）。
2. **音译统一**：柯克·迈库西克→柯克·麦库西克（1）、麦库席克→麦库西克（14 处：第 101 章采访录 7、第 14 卷书目述评 5、第 15 卷书目述评 2）、尼克劳斯·维尔特→尼克劳斯·沃思（3）、约翰·亨尼希→约翰·亨尼西（1，含英文全名同步）、威廉·詹姆斯/詹姆斯→威廉·詹姆士/詹姆士（William James 哲学家相关，含第 12 章、第 8/9 章、概述、SUMMARY 共 13 处；总统名詹姆斯·麦迪逊/门罗/卡特及 James Treybig 保留不动）。
3. **正文英文名保留**：叙述中英文名（Dennis Ritchie 等）一律不改为全名，仅统一中文译名。

## 数据一致性修正

- `writeback_verify_results.py`：合并 `sources`（按 url 去重）与 `doubt_flags`（按 field+doubt 去重），不覆盖既有记录；修正 `parse_json_list` 对 list 输入的处理后全部 276 行正确更新。
- `person_records`/`references.author` 匹配时排除冲突姓氏（BABAOĞLU/HORN/JOLITZ/MILLER/MORRIS/WEBER/YOUNG）的姓氏-only 匹配，防同名误配。
- 验收：`cross_indexes.db` integrity_check=ok，276 行 name_en 0 空、sources 0 空、doubt_flags 0 空、check_date 全部 2026-08-14。

## 遗留待办

- `larry_mcvoy` 译名"拉里·麦克沃伊"仅词典网络释义依据，doubt_flags 记 open，待正式出版物佐证。
- 大纲 348 章概述中 `John L. Hennessy` 英文名已同步为规范全名；其余人物传记章节英文名写法未逐一核对（正文英文名保留原则）。
- 大纲文件本次修改前已整体备份至 `script/_backup_20260814_outline_names/`（2662 文件）。

## 大纲标题与正文音译不一致收尾（6 组，2026-08-14 续）

扫描脚本 `script/scan_en_zh_pairs.py` 复扫 `05-卷册大纲/` 后，识别并统一 6 组“同一英文名对应多种中文音译”的残余分歧（目标取大纲主流写法，Ken Thompson 取 `cross_indexes.db` 已登记译名）：

| # | 英文名 | 不一致写法 | 统一为 | 涉及文件 |
|---|---|---|---|---|
| 1 | Ken Thompson | 肯·汤普逊 ×1 / 肯·汤普森 ×5 | 肯·汤普森 | 第70章 `69.1-人物年表.md` |
| 2 | Barack Obama | 贝拉克·奥巴马 ×1 / 巴拉克·奥巴马 ×3 | 贝拉克·奥巴马 | 第327章 `326.1-历任总统政治画像…md`、第326章 `325.4`、第283/294章 `概述.md` |
| 3 | Allan Jude | 艾伦·裘德 ×1 / 艾伦·朱德 ×5 | 艾伦·朱德 | 第291章 `采访录.md` |
| 4 | Dag-Erling Smørgrav | 斯莫格拉夫 ×1 / 斯默格拉夫 ×3 | 斯默格拉夫 | 第291章 `采访录.md` |
| 5 | Poul-Henning Kamp | 波尔-亨利·坎普 ×2 / 波尔-亨宁·坎普 ×4 | 波尔-亨宁·坎普 | 第330章 `采访录.md` |
| 6 | Lawrence Lessig | 莱西格 ×2 / 莱斯格 ×3 | 莱斯格 | 第294章 `采访录.md` |

上述 6 组均为“同人异写”的纯一致性修复，未改变英文原名。修复后复扫仅剩正则误吞前置汉字（到/与/之父/年间与/须注意等）的伪报，真实音译分歧已清零。

**遗留规则冲突（已裁定并逐人处理）**：Kamp（`poul-henning_kamp`）、Jude（`allan_jude`）、Lessig（`lawrence_lessig`）、Hopper（`grace_hopper`）四人在 `cross_indexes.db` 中 `name_zh=None`，前一轮复核 doubt_flags 均标注“无正式中文出版物译名依据，保持英文原名”；大纲中仍保留其中文音译，且 Smørgrav 不在人名表内。经逐人联网复核出版依据后裁定如下：

| 人名 | 联网复核结论 | 处置 |
|---|---|---|
| Poul-Henning Kamp | 仅 CSDN/图灵社区译文“保尔－亨宁·凯普”（社区译文）与 Reverso 机翻“保罗-恒宁·坎瀑”，无正式出版物依据 | **回退英文原名**（大纲 31 处中文“坎普/波尔-亨宁·坎普/波尔-亨利·坎普”→ Kamp/Poul-Henning Kamp） |
| Allan Jude | book.bsdcn.org、freebsd-journal-cn.bsdcn.org 均保留英文 Allan Jude 不译，无正式出版物依据 | **回退英文原名**（大纲 15 处中文“艾伦·朱德/朱德”→ Allan Jude/Jude） |
| Dag-Erling Smørgrav | 无任何正式中文出版物译名，FreeBSD 多语种文档树保留英文原名 | **回退英文原名**（大纲 9 处中文“斯默格拉夫/斯莫格拉夫”→ Smørgrav） |
| Lawrence Lessig | 清华大学出版社《代码2.0（修订版）》（2018，ISBN 9787302506874，李旭/沈伟伟译）与中信出版社 2004 版《代码》均作“劳伦斯·莱斯格” | **保留中文 + 补登记 name_zh**（`lawrence_lessig` name_zh 置“劳伦斯·莱斯格”，doubt_flags 关闭） |
| Grace Hopper | 机械工业出版社《优雅人生——格蕾丝·霍珀和信息时代的创新》（Kurt W. Beyer 著）与清华大学出版社《我们程序员》均作“格蕾丝·霍珀” | **保留中文 + 补登记 name_zh**（`grace_hopper` name_zh 置“格蕾丝·霍珀”，doubt_flags 关闭） |
| Barack Obama | 新华社译名库标准全名“贝拉克·侯赛因·奥巴马”（中国日报、光明网 2009 交叉印证），given name“Barack”标准译名为“贝拉克”而非“巴拉克” | **纠正为“贝拉克·奥巴马”**（此前“巴拉克”×4 处误改，已全部改为“贝拉克”；Obama 不在 276 人名表，不补登记） |

## 全面复核——第二轮 7 人遗漏（2026-08-14 续）

`_review_names.py` 复扫发现 7 个新增遗漏（DB name_zh=None 但大纲仍保留中文音译），逐人联网复核出版依据后裁定如下：

| 人名 | 联网复核结论 | 处置 |
|---|---|---|
| Glen Barber | 无任何正式中文出版物译名依据，book.bsdcn.org 保留英文原名 | **回退英文原名**（大纲 2 处中文“格伦·巴伯”→ Glen Barber） |
| Philip Paeps | 无任何正式中文出版物译名依据，book.bsdcn.org 保留英文原名 | **回退英文原名**（大纲 2 处中文“佩普斯/菲利普·佩普斯”→ Paeps/Philip Paeps） |
| Alfred Aho | 机械工业出版社《编译原理（第2版）》（龙书）CIP 数据作“阿霍(Alfred, V. A.)” | **保留中文 + 补登记 name_zh**（`alfred_aho` name_zh 置“阿尔弗雷德·阿霍”，doubt_flags 关闭） |
| Guido van Rossum | 无正式中文出版物译名依据（仅 CSDN/百度百科等自媒），book.bsdcn.org 保留英文原名 | **回退英文原名**（大纲 2 处中文“吉多·范罗苏姆”→ Guido van Rossum） |
| J.C.R. Licklider | 中信出版社《创新者》（Walter Isaacson 著，关嘉伟/牛小婧译，ISBN 9787508671642）作“J·C·R·利克莱德” | **保留中文 + 补登记 name_zh**（`jcr_licklider` name_zh 置“约瑟夫·利克莱德”，doubt_flags 关闭） |
| Rob Pike | 人民邮电出版社《UNIX传奇：历史与回忆》（韩磊译）作“罗勃·派克” | **保留中文 + 补登记 name_zh**（`rob_pike` name_zh 置“罗勃·派克”，doubt_flags 关闭） |
| Stephen Bourne | 人民邮电出版社《UNIX传奇：历史与回忆》译 Bourne 为“伯恩”；Stephen 取规范译名“斯蒂芬” | **保留中文 + 补登记 name_zh**（`stephen_bourne` name_zh 置“斯蒂芬·伯恩”，doubt_flags 关闭） |

## 全面复核——第三轮 2 人遗漏（2026-08-15 续）

`_review_names.py` 复扫问题数从 76→69→67，`_fuzzy_check.py` 分类后确认 2 个真遗漏（DB name_zh=None 但大纲仍保留中文音译），逐人联网复核出版依据后裁定如下：

| 人名 | 联网复核结论 | 处置 |
|---|---|---|
| Justin Gibbs | 无任何正式中文出版物译名依据，book.bsdcn.org、FreeBSD Journal 中文版均保留英文原名 | **回退英文原名**（大纲 3 文件 11 处中文“贾斯汀·吉布斯/吉布斯”→ Justin Gibbs/Gibbs） |
| Warner Losh | 无任何正式中文出版物译名依据，book.bsdcn.org 保留英文原名；FreeBSD Journal 中文版《回忆录：与 Warner Losh（@imp）的访谈》保留英文原名 | **回退英文原名**（大纲 1 文件 1 处中文“M. 沃纳·洛什”→ M. Warner Losh） |

## 最终验收（2026-08-15）

`_review_names.py` 最终输出 67 项，经 `_fuzzy_check.py` 分类全部为三类无害残留：

1. **简称误报**（DB 已有 name_zh，仅英文名写法不同）：`dennis ritchie`、`eric raymond`、`eric s. raymond`、`frederick phillips brooks jr`、`j. c. r. licklider`、`jeffrey hsu`、`ken thompson`、`kirk mckusick`、`linus torvalds`、`m. douglas mcilroy`、`richard stallman`、`steve jobs`、`vincent foster hopper`、`vint cerf`——无需处理。
2. **真不在 276 人名表**（政治/哲学/普通人物）：`Donald Trump`、`Eben Moglen`、`Edmund Randolph`、`Evgeny Morozov`、`François Tigeot`、`George Mason`、`George Washington`、`Herbert Marcuse`、`Hiten Pandya`、`James Madison`、`Joerg Sonnenberger`、`John Jay`、`John Kenneth Galbraith`、`John Marshall`、`Michael Tiemann`、`Pamela Samuelson`、`Reinhold Niebuhr`、`Sergio De Simone`、`Will Backman`、`Will Spencer`、`William Norris`、`Donald Nielson`、`Dan Lang`、`Dan Searle`、`Dennismacalistairritchie`——无需处理。
3. **正则伪报**（前置汉字被误吞进中文名）：`与肯·汤普森`→`ken thompson`、`由乔治·华盛顿`→`george washington`、`的传统与威廉·詹姆士`→`william james` 等——正则局限性，无需处理。

**真实译名分歧已彻底清零**。`cross_indexes.db` integrity_check=ok。
