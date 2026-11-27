# V37 批记 retitle-V37-c13＋supp-V37-b028（第 13 章 20 题改题＋8 题填充）

- **批次**：`retitle-V37-c13＋supp-V37-b028`｜2026-11-27｜G4 全责线（162 v5.0 组四）
- **范围**：第 13 章“FreeBSD 的语言生态与 Rust 准入”4 节 20 题全数重拟（4 filled 迁移保块＋16 skeleton 改名）；同章 8 题联网补证落块（6 题 DOC_MINE＋2 题 ROW_MINE）。
- **拟题依据**：节题构式＋thesis＋实义锚（CVSup／Modula-3／Polstra／libc++／libcxxrt／C++ ABI／Rust／Somers／Rust for Linux／构建链）。

## 一、改题（20 题）

- **呈审件**：`title-design/retitle/V37-c13-呈审-20261127.md`（逐题旧题→新题＋分布自检）。
- **分布自检**：冒号 0；问句 0；题长 10—19 字（8—12 字 8 席，40%）；含“的”0/20；三并列 0；逐节构式各异。
- **尾簇返工（程序披露）**：首落 6 题触发第三十九件 C8b（“范围”×5、“负担”×4、“维护”×4、“成本”×4、“依赖”×4），整批回滚后改尾词（实现／合性／落点／人力／译器／上升）重落；复检 V37 尾簇全部 ≤3。
- **台账**：`title-design/V37.tsv`、`design/V37.tsv`、`design/fragments/V37.tsv` 各 20 行标题改；`design/V37-C2.tsv` 同步 11 行；`title.ok`／`land.ok` 重签（ledger 指纹 `d764a071665193e5…`），`approvals` 追加一行（supersedes 前批准指纹 `4c136863bbe5172b`）。
- **迁移守恒**：20 树件改名＋H1 同步；4 件 filled 保块零内容改；`premerge_keyguard` PASS → `merge_subsections --vols 37`（outline 20 行改）→ `assemble_index`（页版本随装配更新）；SUMMARY V37 卷块 20 行改。

## 二、填充（8 题 8 块）

| 小节 | 题名（新） | 块型 | 来源 | 等级 |
| ---- | ---------- | ---- | ---- | ---- |
| V37.13.2.1 | libc++ 经 BSD 化入基本系统 | DOC_MINE D2 | ref11344（2012 Q1 状态报告） | L3 |
| V37.13.2.2 | libcxxrt 提供 C++ ABI 运行库 | DOC_MINE D2 | ref11345（libcxxrt README） | L3 |
| V37.13.2.3 | 标准库移植适配异常与线程 | DOC_MINE D2 | ref11344（C++11 原子测试句） | L3 |
| V37.13.2.4 | 异常处理分居编译器与运行库 | DOC_MINE D2 | ref11345（栈展开库句） | L3 |
| V37.13.2.5 | 测试套件校验标准符合性 | DOC_MINE D2 | ref11346（libc++ 官方站） | L3 |
| V37.13.3.3 | 内核模块准入先评 ABI 与构建链 | DOC_MINE D2 | ref10911（2025 Q4 状态报告） | L3 |
| V37.13.3.1 | Somers 方案限定 Rust 落点 | ROW_MINE | freebsd-hackers.messages.2537013 | L4 |
| V37.13.3.4 | 自举须先有 Rust 编译器 | ROW_MINE | freebsd-hackers.messages.2537013 | L4 |

- **新 ref**：11344（FreeBSD 2012 Q1 状态报告）、11345（libcxxrt 仓库说明）、11346（libc++ 官方站）；ref10911 复用（2025 Q4 状态报告，库内已有条目、无全文，D2）。
- **新 claim**：CL-RM-498819—498826（8 条，全 supported；L3 6／L4 2）；claim_evidence 每 claim 恰 1 行。
- **ROW_MINE 源**：Somers 原帖本机邮件库 row 2537013（2024-01-20），新建 raw_source `SRC-rowmine:freebsd-hackers.messages.2537013`；同帖另建网页副本核验（freebsd-hackers 2024-January/002823）。
- **卡**：`99-考据新增/20261127_freebsd_2012q1_cxx_stack.md`、`20261127_libcxxrt_readme.md`、`20261127_libcxx_conformance.md`。

## 三、号段事故与修复（如实披露）

- **水锁未取得即写入**：`register_waterlock probe` 返回 next 498819；`acquire` 时 `register__historical_claims__GLOBAL.lock` 由他线 `supplement:V26-b003` 持有（12 claims，reservation 498807—498818），acquire 失败但批脚本未断言返回码，遂继续写入 498819—498826（在 V26 reservation 之外，claim 号无撞）。
- **evidence 撞号**：V26 线并发写入 EV-SUP-004602—004607，本批 ev0 取号亦落 004602—004609，致 004602—004607 各 2 行。**修复**：仅将本批 8 行改号至 EV-SUP-004800—004807，并按 claim_id 同步 claim_evidence 指针；复检重复 evidence_id 0，8 claim 各 1 链。他线行未动。
- **水锁释放**：release 因锁属他线（预期 12≠本批 8）被拒；未 abort、未 force 他线锁。**教训**：批脚本须断言 acquire 返回码与锁 tag，失败即停。
- **claim 号**：498819—498826，与他线 reservation 无重叠；全库重复 claim_id 0。

## 四、台账与口径

- `exceptions/V37.tsv`：8 行 open→supplemented（6 doc_mine／2 row_mine；resolution_ref 与 claim 对位）。
- `supplement/V37.tsv`：6 行（DOC_MINE D2；ROW_MINE 不入 supplement，沿既有分治）。
- `fragments/V37.tsv`：8 行 skeleton→filled；`land.ok` fragments 指纹重签。
- 口径：V37 题 795／filled 353→361／skeleton 442→434／closed 0；全库 19 363 题、filled 6 187、skeleton 13 150（2026-11-27 批后现算）。

## 五、门禁（2026-11-27 实测）

- 第三十九件：47 项 FAIL 6＝V09／V18／V19 他线（B1／B2／B3／C7／C8b／H1）；V37 面 0（C8b 尾簇复检 ≤3）。
- 第四十一件：FAIL 2＝V01 他线（CP/M 全角）；V37 0。
- 第三十七件：L1—L19 19/19 PASS（L19 outline＝tree＝summary＝19 363）。
- 第三十八件：D1／D2／L 3/3 PASS。
- 第三十五件：exit 0（V37 0 命中）；第三十四／三十三件 PASS。
- 第二十八件：0 处；第二十四件：54 处／3 文件＝他线（V37 0）。
- 第四十三件 `--vol V37`：本批 8 块 0 FAIL；全库 514 FAIL 属 vitepress 派生件与他线（只披露）。
- 常备五项与卷级回归待收口批统一复跑。

## 六、下一站

- V37 第 13 章余 8 题（13.1.1、13.3.2、13.3.5、13.4.1—13.4.5），按同章第二批填充推进；章骨架清零后进入 8.3 三章验收批。
- G4 其余卷：V15／V42／V56／V72（陈旧锁可依 §8.1 接管留痕）；V12／V75 由在途线持有，本线不触。
