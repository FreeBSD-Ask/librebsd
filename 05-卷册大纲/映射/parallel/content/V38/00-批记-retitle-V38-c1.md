# V38 批记 retitle-V38-c1（第 1 章 42 题改题＋迁移）

- **批次**：`retitle-V38-c1`｜2026-11-27｜G4 全责线
- **范围**：第 1 章“创始成员与 386BSD 交接”7 节 42 题全数重拟；22 filled 迁移保块零内容改＋20 skeleton 改名保状态；H1 同步。
- **拟题依据**：节题构式＋台账 thesis＋实义锚（Greenman／FreeBSD／Walnut Creek／Hubbard／Ports／sysinstall／Grimes／1992 至 1995／1992 至 1996／Williams／386BSD／Jolitz／麦库西克／CSRG／USENIX／ACM／Bostic／AT&T）。
- **呈审件**：`title-design/retitle/V38-c1-呈审-20261127.md`（逐题旧题→新题＋拟题依据＋分布自检）。

## 一、分布自检（章级 42 题）

| 指标 | 实测 | 判据 |
| ---- | ---- | ---- |
| 冒号 | 0 | 六规则 1 |
| 问句 | 0 | 六规则 5 |
| 题长 | 9—19 字（去空格）；8—12 字 21 席 | 六规则 2 burstiness |
| 含“的”题 | 0/42 | 六规则 4＋C8d |
| 三并列 | 1（1.4.2 散见手册、名录与访谈） | 六规则 3 |
| 构式 | 逐节 6 席、七节各异 | 六规则 6 |

## 二、批内订正（两件门禁驱动）

- **第三十九件 C6**：`V38.1.2.2` 首稿“Hubbard 起手首代 Ports 集合”经 C6 专名形态判据复核后保留“Ports”专名形态，订正题面为现形（其余 41 题不变）；approvals 追加一行。
- **第四十一件 R35**：`V38.1.6.1` 首稿用教科书级人物拉丁形，按既定中译改“麦库西克”（其余题不变）；approvals 追加一行。
- **批准指纹终值**：`12fcf7d8a7e1bd78d8c4d49dad1b8ee4fcdd9fe69fb2f6c236407d3067ff81ed`（`title.ok`／`land.ok` 同值）；approvals 三行（`aa011790…`→`f70bc7c3…`→`12fcf7d8…`，逐次 supersedes）。

## 三、迁移与再生

- **台账**：`title-design/V38.tsv`、`design/V38.tsv`、`design/fragments/V38.tsv` 各 42 行标题改；status／order／thesis 等其余字段未动。
- **树件**：42 件改名＋H1 同步；正文多重集核验守恒（逐节去 H1 后 sha256 多重集与 HEAD 相等），22 filled 零内容改。
- **再生**：`premerge_keyguard.py` → `merge_subsections.py --vols 38`（outline 42 行改）→ `assemble_index.py --write`（页版本 `2026.11.26-02:42`→`2026.11.27-02:48`；`--check` 无漂移）；SUMMARY 42 行改。
- **主题索引／章节关键词**：工作树 02:45 版已含本批题面，但此后他线内容批（V01 b044／V12 b072／V36 b040—b041／V75 b075 等）继续改树，27 件 B1 `content_sha256` 已漂移，本批不提交该两件、只披露，待全库镜像解阻后统一再生。

## 四、门禁（2026-11-27 实测）

- 第三十九件：47 项 FAIL 2＝`V09.2.2.2`／`V09.2.2.3` 与 `V09` title.ok hash（他线在途，只披露）。
- 第四十一件：PASS（3 处披露非 V38）。
- 第三十七件：L1—L19 19/19（L19 outline＝tree＝summary＝19 363）；第三十八件 3/3；第二十八件 0 处。
- 第二十四件：14 处／4 文件，均为他线 `99-考据新增` ref 卡（只披露）。
- 第三十三／三十四件 PASS；第三十五件 A／B 均 0 组。
- 第四十三件 `--vol V38`：V38 树面 0 FAIL（全库 489 FAIL 属 `目录/vitepress` 派生件与他线）。
- 装配 `--check` 无漂移；第十八件版本递增 PASS；第十三件 4/4；口径同步零未处置漂移。
- 常备：`audit_gate_registry` 8 项 0；`audit_rule_dup` 4 项 0；`_longline_status --check` PASS（2 条过期告警）；旁路备份 FAIL 2 件＝`vitepress/.build` 派生件（他线）。
- 卷级回归：V38 5/6（V3 深链 FAIL）；同页对跑 V37／V40 同症状、V01 6/6＝页面级共性，非本批引入，只披露。

## 五、账目与下一站

- 口径：V38 题 198／filled 47／skeleton 151（本批不改 filled 数）；第 1 章 42 题（22 filled＋20 open）。
- 账：changelog id=3612→92 §十一→98 §十一→本批记。
- 下一站：`supp-V38-p2-b001`（第 1 章 20 题填充；先落 `design/supplement/V38.tsv` 表头）。
