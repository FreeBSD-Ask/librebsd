# V37 批记 retitle-V37-c2＋supp-V37-b030（第 2 章 50 题改题＋1 题填充）

- **批次**：`retitle-V37-c2＋supp-V37-b030`｜2026-11-28｜G4 全责线（162 v5.0 组四）
- **范围**：第 2 章“FreeBSD 网络体系：从 BSD TCP／IP 到高速网络平台”10 节 50 题全数重拟（48 filled 迁移＋2 skeleton 改名）＋2.3.5 填充；2.9.4 单源未获一手，留 open。
- **口径**：V37 filled 369→370、skeleton 426→425；第 2 章 49/50（2.9.4 open）。

## 一、改题分布自检（章级 50 题）

| 指标 | 实测 | 判据 |
| ---- | ---- | ---- |
| 冒号 | 0 | 六规则 1 |
| 问句 | 0 | 六规则 5 |
| 题长 | 9—19 字（去空格）；8—12 字 30 席（60.0%） | 六规则 2＋C8e |
| 含“的”题 | 0/50 | 六规则 4＋C8d |
| 三并列 | 0 | 六规则 3 |
| 尾簇 | 预检 4 簇超限（分界／范围／对接／代价各 4），改 4 题尾词后 0 超限 | C8b |
| 构式 | 逐节各异（10 节各 5 席） | 六规则 6 |

- 呈审件 `title-design/retitle/V37-c2-呈审-20261128.md`；台账各 50 行＋V37-C2 同步 108 行；title.ok／land.ok 重签（`c67d2ebcab644ca1…`）；approvals 追加（supersedes `2973c6a3…`）；树件 50 件改名＋H1；merge --vols 37＋装配＋SUMMARY。

## 二、填充（2.3.5）

- **来源**：ref11414（Julian Elischer《All About Netgraph》，Daemon News 2000-03；magazine-article／L3／primary）——自述 netgraph 以速度为要、全内核运行、节点间不经排队而用直接函数调用。
- **claim** CL-RM-499166（L3）；evidence EV-SUP-005140；claim_evidence 1:1；`exceptions` 1 行 open→supplemented；`supplement`＋1；`fragments` 1 行 filled；`land.ok` 重签。
- **留 open 披露**：2.9.4 漫游支持——wireguard.com 在当前网络连接超时（curl/WebFetch 均失败），协议页与白皮书不可达；未以二手转述降格充数，留 open 待下次联网窗口。
- 水锁正常取得 499166 并释放（严格断言）。

## 三、门禁

- 39 件 C8b／C8e PASS（全库 FAIL 1＝他线）；41 件 V37 0；37 件 19/19；38 件 3/3；43 件 --vol V37 本批 0（全库 653 属 vitepress 派生件与他线）；24 件 V37 0；28 件 0；35／34／33 PASS；V37 回归 5/6（V3 深链页面级，V38 同症状）。

## 四、下一站

- ch2 余 1 题（2.9.4，联网窗口恢复后补）；ch13 已完成 20/20；第三批拟 ch3（19 open）或 ch1（7 open）；三章完成后提交三章批验收请求。
