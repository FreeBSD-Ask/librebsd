# V57 判读规程卡（RULES）

## 一、我在做什么

Task 8.4／8.5 单会话卷批判读：V57“BSD 的衍生与分叉：主干诸系的分岔与扩散（1995–2026）”，30 节 150 题。
料域 4 片 890 块（P1 268／P2 122／P3 323／P4 177），机器已剔自动类后待判 806 块。
**主会话单写者**（ykla 2026-11-06 令"不使用子代理"），fork 接续会话执行。

## 二、输入与分片

- 题面真值：`parallel/content/V57/titles.tsv`（150 行，`title-design/V57.tsv` 已批面的投影）
- 块档：`parallel/content/V57/part{1..4}.blocks.jsonl`；判读摘要在 `script/_v5x_triage_V57_P{1..4}.txt`
- 分片域：P1 分叉判准／总目／身份／命名／公告＋386BSD fork 链（448.x／438.x／447.x／446.x／437.x／071.1 等）；
  P2 桌面与存储衍生（PC-BSD/TrueOS/GhostBSD 295.x·279.x·287.x·282.2；FreeNAS/TrueNAS 285.x·303.7·304.2；pfSense/OPNsense 286.x）；
  P3 厂商商用与嵌入式（JunOS/ONTAP/WhatsApp 303.x·288.x；NetBSD 嵌入式 194.x·195.x·204.5·217.1；治理 076.x·236.2·237.3）；
  P4 跨项目与衍生项目群（316.x OpenSSH/LibreSSL/pkgsrc；318–320 跨项目；Capsicum 432.x·127–129；欧洲与麒麟 364–366）

## 三、逐节边界表（判读时对题不对域）

按 `titles.tsv` 逐题归属；跨节题面（如"四主干源流的派生总目"1.2 与"衍生稀少的结构原因"9.1）
以题面论题为准，不以料域来源节为归宿。386BSD／patchkit 块归 1.1–1.2 判准与总目；
JunOS/ONTAP 块归 5.1；NetBSD 嵌入式块归 1.8／7.2；LibreSSL/OpenSSH 块归 5.2／9.1；
Capsicum 块归 9.2；欧洲立场块归 8.1；麒麟块归 8.1（按 366.11 建议宿主判断，属跨项目许可考据）。

## 四、处置阶梯＋容量规则

1. 自动类（脚本已剔）：`DB_REF`／`DB_POINTS`／卷内重复 ≥5 的 `DEEP_ANALYSIS` 模板 → 删除，不写 dec。
2. 零内容块（空块／仅元数据行）→ `删除`（reason 写明）。
3. 与题面意合的 ROW_MINE／MAIL_INSIGHT 实质块 → `归入`（sid 填 `V57.N.N.P`），单题 ≤12，超限降 `挂账`。
4. 实质块但宿主在他卷（技术流水→V49；许可证条款→V59；pf/OpenBSD 面→V46 系；发布周期面→V50 系）→ `移出`＋建议宿主。
5. 同题面但证据力弱、留待内容批核 → 原则上 `归入`（空骨架口径由 filled／skeleton 落盘器定），不轻判挂账。
6. 判据与 V51–V56 一致：`_v5x_dec.py` 自动合成 5 列契约，dec 只写 ROW_MINE 与非模板 DEEP_ANALYSIS。

## 五、输出契约＋禁止项

- 输出：`script/_v5x_dec_V57_P{1..4}.tsv`（idx／sid／action／reason 四列；TAB 分隔；UTF-8 无 BOM；LF）。
- 禁止项：不跨片改 idx；不写模板块行；不用 `python -c` 内联写中文（走 Write 工具）；
  归入 sid 必须逐字来自 `titles.tsv`；reason 措辞与既往卷一致（建议宿主写卷号）。
- 守恒：待判 806＝Σdec 行数＋自动剔除数，合并器复核多重集。
